#!/usr/bin/env python3
"""Log estimated vs actual minutes per unit type, and report correction ratios.

Usage:
  calibrate.py log --kind build --est 30 --actual 22 [--note "auth flow"]
  calibrate.py stats

The log is ~/.real-eta/log.jsonl (set REAL_ETA_LOG to use another file).
"""
import argparse
import json
import os
import statistics
import time

KINDS = ("build", "research", "human", "wait", "unknown")
LOG = os.environ.get("REAL_ETA_LOG", os.path.expanduser("~/.real-eta/log.jsonl"))


def log(args):
    if args.est <= 0 or args.actual < 0:
        raise SystemExit("--est must be above 0 and --actual 0 or more (minutes)")
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    entry = {"ts": int(time.time()), "kind": args.kind, "est_min": args.est,
             "actual_min": args.actual, "note": args.note or ""}
    with open(LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"logged {args.kind}: estimated {args.est:g} min, actual {args.actual:g} min")


def stats(_args):
    ratios = {}
    if os.path.exists(LOG):
        with open(LOG) as f:
            for line in f:
                try:
                    e = json.loads(line)
                    ratios.setdefault(e["kind"], []).append(e["actual_min"] / e["est_min"])
                except (ValueError, KeyError, ZeroDivisionError):
                    continue  # skip hand-edited or broken lines
    if not ratios:
        print("No calibration data yet. Use the ranges in references/.")
        return
    print("kind       entries  median actual/estimate")
    for kind in KINDS:
        if kind in ratios:
            print(f"{kind:<10} {len(ratios[kind]):>7}  {statistics.median(ratios[kind]):.2f}")
    if all(len(r) < 5 for r in ratios.values()):
        print("Fewer than 5 entries per kind: treat these as hints, not corrections.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    lp = sub.add_parser("log", help="record one estimate and its actual time")
    lp.add_argument("--kind", choices=KINDS, required=True)
    lp.add_argument("--est", type=float, required=True, help="estimated minutes")
    lp.add_argument("--actual", type=float, required=True, help="actual minutes")
    lp.add_argument("--note")
    lp.set_defaults(fn=log)
    sub.add_parser("stats", help="show median actual/estimate per kind").set_defaults(fn=stats)
    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()

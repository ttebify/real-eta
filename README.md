# real-eta

Ask an AI assistant how long a project will take and it often answers at human-team pace. It learned durations from human tickets and roadmaps. It has no stopwatch. Divide that answer by ten and you are wrong the other way: agents write code faster, but review, approvals and customers do not speed up.

real-eta replaces both guesses. It tracks agent time, your time and calendar time as three separate clocks, compares each range with measured builds and published studies, and labels the judgment calls. The answer is a dated plan short enough to use.

## Example

A solo developer asked how long until a barbershop booking app with Paystack deposits and WhatsApp alerts is live. The answer opened with:

> **First real deposit taken by Fri 6 Nov 2026 (P90 Fri 20 Nov).** About 15–30 h of agent work and 25–40 h of your own time. The code fits in one week. The dates depend on Paystack going live and on how fast you can sign shops, not on the code.

The full answer gives the phases, what to start today, what could slip and a source or judgment label for each number.

## Install

**Claude Code**

```
/plugin marketplace add ttebify/real-eta
/plugin install real-eta@real-eta
```

**Codex, Cursor and other tools that read Agent Skills**

```bash
mkdir -p ~/.agents/skills
curl -L -o real-eta.zip https://github.com/ttebify/real-eta/releases/latest/download/real-eta.zip
unzip real-eta.zip -d ~/.agents/skills
```

**Any other assistant:** paste [`SKILL.md`](skills/real-eta/SKILL.md) into its custom instructions and attach the two files in [`references`](skills/real-eta/references).

## Use

Ask a timing question as you normally would. For example: "How long until this is live?" or "Is this doable by Friday?" Say which model will do the work if it is not a current frontier model, because smaller models get smaller tasks and more review time.

To calibrate it against your own projects, log what actually happened (times in minutes):

```bash
python3 ~/.agents/skills/real-eta/scripts/calibrate.py log --kind build --est 30 --actual 22
```

That path matches the zip install above. For the Claude Code plugin, the script is at `~/.claude/plugins/marketplaces/real-eta/skills/real-eta/scripts/calibrate.py`. The skill reads the log before each estimate.

## Token cost

- About 170 tokens in every session, for the skill's name and description.
- About 5,000 more when it fires: about 1,800 for the skill and about 3,200 for the two reference files it reads. These are estimates from `claude plugin details` and file sizes.
- A full plan took 5 to 8 turns and cost $0.26 to $0.44 per answer on Claude Opus 5.5, measured over nine test runs on 26 October 2026. That includes Claude Code's own overhead. Those runs used an earlier 750-word cap, so shorter answers should cost a little less.

## Limitations

- The tests favour it. In one run per case on 26 October 2026, it passed 20 of 20 checks against 9 of 20 without it.
- Answers are capped at 300 words. With a 750-word cap, test answers ran 536 to 639 words, so the cap sets the length, not the content.
- Some checks test facts the skill does not supply, so treat the score as a smoke test, not proof. The test cases are in [`evals`](evals).
- No estimate has been checked against a finished project yet. The ranges are judgment calls, fitted to a handful of published builds.
- Answers vary between runs, especially on the largest test case.
- The evidence ages fast. It is dated 25 October 2026; refresh it by April 2027.
- Tested only with Claude. The instructions are model-neutral, but other models have not been measured.

The research behind every number, with a strength rating for each source, is in [`references/evidence.md`](skills/real-eta/references/evidence.md).

## Licence

MIT. See [LICENSE](LICENSE).

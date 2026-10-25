# real-eta

Ask an AI assistant how long a project will take and it usually answers at human-team pace, because it learned time from human tickets and roadmaps. Divide that by ten and you are wrong the other way: agents write code faster, but review, approvals and customers do not speed up.

real-eta is a skill that fixes both. It splits every estimate into three clocks (agent time, your time and calendar time), checks each number against measured builds and published studies, and answers with a short dated plan.

## Example

A solo developer asked how long until a barbershop booking app with Paystack deposits and WhatsApp alerts is live. The answer opened with:

> **First real deposit taken by Fri 6 Nov 2026 (P90 Fri 20 Nov).** About 15–30 h of agent work and 25–40 h of your own time. The build fits in one week. The dates depend on Paystack going live and on how fast you can sign shops, not on the code.

It then listed the phases, what to start today, what could slip and the source for each number.

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

Ask a timing question as you normally would, such as "How long until this is live?" or "Is this doable by Friday?".

To make it learn from your own projects, log what actually happened (times in minutes):

```bash
python3 ~/.agents/skills/real-eta/scripts/calibrate.py log --kind build --est 30 --actual 22
```

The skill reads this log before each estimate.

## Limitations

- **The tests favour it.** On three test requests it passed 20 of 20 checks against 9 of 20 without it, but the checks were written around what it teaches. The test cases are in [`evals`](evals).
- **No estimate has been checked against a finished project yet.** The time ranges per task are judgment, fitted to a handful of published builds.
- **Answers vary between runs**, by up to about two weeks on the largest test case.
- **The evidence ages fast.** It is dated 25 October 2026 and should be refreshed by April 2027.
- **Tested only with Claude.** The instructions are model-neutral, but other models have not been measured.

The research behind every number, with a strength rating for each source, is in [`references/evidence.md`](skills/real-eta/references/evidence.md).

## Licence

MIT. See [LICENSE](LICENSE).

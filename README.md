# real-eta

A skill that helps AI coding agents give realistic timelines for the work they will build. It splits every estimate into agent time, human time and calendar time, and backs each number with a measured build or a published study.

It is plain Markdown plus one optional Python script, so it works in any tool that reads Agent Skills (Claude Code, Codex, Cursor and others), and in any chat assistant that accepts custom instructions.

## The problem

Ask an AI assistant how long a project will take and it usually answers at human-team pace. It learned durations from human tickets, blog posts and roadmaps, and it cannot sense its own speed. One 2026 study found that models' estimates before a task overshot the actual time by 4–7×, and by 5–10× in multi-step agent tasks ([Garikaparthi, 2026](https://arxiv.org/abs/2604.00010)).

The fix is not to divide by ten. Agents speed up writing code, but not everything around it. Across 718 firms, pull request review time rose 49% after agents were adopted, and shipped output rose by no more than 12% ([Chen and Stratton, 2026](https://fion.ac/jellyfish.pdf)). Payment approvals, app store reviews and customers do not move faster because the code did.

## What the skill does

- Breaks the work into units an agent finishes reliably (about 1–2 hours of skilled human work each).
- Prices three clocks separately: agent wall-clock time, your time (review, decisions, accounts, testing) and calendar time (anything outside your control).
- Compares the estimate with measured agent builds instead of guessing.
- Checks for both mistakes: quoting human-pace months for agent work, and squeezing external waits into hours.
- Puts the first shippable version first, with later phases shipping while it runs.
- Keeps the answer under about 300 words: the date, what sets it, what to start today and why the numbers hold.
- Learns from your own projects through a small log of estimated and actual times.

## Example

From a test run. The question was a booking app for barbershops with deposits through Paystack and WhatsApp notifications, built by one developer.

> **First paying shops by Fri 20 Nov 2026 (P50). P90 is Fri 18 Dec.** That's about 8–15 hours of Claude Code work and 20–35 hours of your own time. The code isn't what sets the date. Paystack going live and shops signing up are.
>
> | Phase | When | Ships |
> |---|---|---|
> | 0. Build | 26–30 Oct | Booking page, slots, Paystack deposit split to the shop, WhatsApp alert to the barber, owner dashboard. All in test mode |
> | 1. Pilot | Week of 2 Nov | One friendly shop takes real deposits |
> | 2. Paying shops | 9–20 Nov | 3–5 shops on a monthly plan, plus no-show and refund rules |
> | 3. Grow | Dec onward | Reminders and reschedules, shipped weekly |

The full answer goes on to list what to start today, what could slip and the sources behind each number. Without the skill, the same model quoted about three weeks of build time for this scope and gave no source for it.

## Install

**Claude Code**

```
/plugin marketplace add ttebify/real-eta
/plugin install real-eta@real-eta
```

**Codex, Cursor and other tools that read Agent Skills**

Download the skill and unzip it into your skills folder. Codex and Cursor both read `~/.agents/skills`.

```bash
mkdir -p ~/.agents/skills
curl -L -o real-eta.zip https://github.com/ttebify/real-eta/releases/latest/download/real-eta.zip
unzip real-eta.zip -d ~/.agents/skills
```

If your tool uses a different folder, copy the `real-eta` folder there instead.

**Any other assistant**

Paste the contents of [`skills/real-eta/SKILL.md`](skills/real-eta/SKILL.md) into the assistant's custom or project instructions, and attach the two files in [`skills/real-eta/references`](skills/real-eta/references). The calibration log needs a tool that can run Python, so skip it there.

## Use

Ask a timing question as you normally would: "How long until this is live?", "Give me a roadmap for this MVP" or "Is this doable by Friday?". The skill loads on its own in tools that support skills.

## Calibrate with your own projects

The skill's built-in ranges are a starting point. Your own history is better. After you build something it estimated, log what happened:

```bash
python3 ~/.agents/skills/real-eta/scripts/calibrate.py log --kind build --est 30 --actual 22 --note "auth flow"
python3 ~/.agents/skills/real-eta/scripts/calibrate.py stats
```

Kinds are `build`, `research`, `human`, `wait` and `unknown`, and times are in minutes. The log is stored in `~/.real-eta/log.jsonl`. Before each estimate, the skill reads your median actual-to-estimate ratio for each kind and adjusts its numbers. With fewer than five entries for a kind, it treats the ratio as a hint. Adjust the script path to wherever you installed the skill.

## How it was tested

Three realistic requests were each answered with and without the skill, then graded against written checks:

- a solo developer's booking app with Paystack and WhatsApp
- a three-person team moving an old Django codebase to Okta single sign-on
- a subscription mobile app that needs both app stores

| | With the skill | Without |
|---|---|---|
| Checks passed | 20 of 20 | 9 of 20 |
| Answer length | 350–404 words | 1,139–1,630 words |
| Time to answer | about 105 seconds | about 128 seconds |

The skill shortened the timeline where the build was the slow part (the booking app), and kept it long where human review and the customer set the date (the Okta migration). The test cases are in [`evals`](evals).

## Limitations

- **The tests favour the skill.** The checks were written around what the skill teaches, such as separating the three clocks and citing sources, so an answer without the skill loses points for format. On two of the three cases, the model without the skill reached nearly the same dates.
- **No estimate has been checked against a finished project yet.** The per-unit time ranges are judgment, chosen to fit a handful of published builds. Treat them as a starting point until your own calibration log has data.
- **Answers vary between runs.** The Okta estimate moved by about two weeks between two runs. Each test case ran once per version, which is a small sample.
- **The evidence goes out of date quickly.** The length of task agents can finish has been doubling roughly every 3–4 months. The evidence file is dated 25 October 2026 and should be refreshed by April 2027.
- **Some sources are thin.** The 4–7× finding comes from a single-author workshop paper, and several measured builds come from vendor case studies. Each source's strength is rated in [`references/evidence.md`](skills/real-eta/references/evidence.md).
- **Tested with one model family.** All tests ran on Claude. The instructions are model-neutral, but results with other models have not been measured.

## What makes it different

Most estimation prompts either suppress time estimates or apply a fixed speed-up multiplier written by hand. This skill compares against measured builds and published studies, rates the strength of each source, separates the time agents save from the time they cannot save, gives a short dated plan instead of a single number, and warns when its own evidence is getting old.

## Evidence

All research behind the skill, with links and a strength rating for each source, is in [`references/evidence.md`](skills/real-eta/references/evidence.md). The measured builds it compares against are in [`references/reference-classes.md`](skills/real-eta/references/reference-classes.md).

## Licence

MIT. See [LICENSE](LICENSE).

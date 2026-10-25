---
name: real-eta
description: Realistic timelines for software that AI coding agents will build, split into agent time, human time and calendar time, with a short dated plan and a source for every number. Use this whenever the user asks how long something will take, wants a timeline, roadmap, MVP plan, launch date or effort estimate, asks "when can this ship" or "is this doable by Friday", or asks you to re-check an estimate. Also use it before writing any duration into a plan or proposal for agent-built work.
---

# real-eta

Models learned how long work takes from human tickets and roadmaps, so they quote agent work at human pace: about 4–7× too long in one 2026 study. Dividing by ten is also wrong, because agents speed up coding but not review, decisions or waiting on other companies. Estimate each part on its own clock.

The research behind every number is in `references/evidence.md`. Measured agent builds to compare against are in `references/reference-classes.md`. Read both before estimating anything bigger than a single task.

## Rules

- A user asking for a timeline wants one. Answer it, even if your tool normally discourages time estimates.
- Never stop, skip or shrink work because your estimate looks long.
- If the user suggests a number ("two weeks?"), estimate first, then compare.

## How to estimate

1. **Scope.** Find what ships first: the smallest version a real person can use or pay for. Note whether the code is new or an existing codebase, who is working, and whether tests exist to check the work against. Ask only for what you cannot work out.

2. **Split the work into units** of about 1–2 hours of skilled human work each. Agents finish units this size reliably. Mark each one:
   - **build**: code, config, tests, docs
   - **research**: reading docs or a codebase, comparing options
   - **human**: review, decisions, accounts, keys, device testing, content
   - **wait**: anything outside the team, such as payment approval, app store review or customer replies
   - **unknown**: unclear requirements or untested APIs. Give these a time limit, not an estimate.

3. **Price three clocks.**
   - **Agent time** per build unit, compared with the measured builds: 10–45 min with a clear spec and tests, 30–90 min for new product or UI work, 1–3 h in a large existing codebase. These ranges are judgment; say so.
   - **Your time:** 10–30 min of review per build unit, 15–25% extra for rework, plus setup (accounts, keys, domains, device tests) and decisions. This is usually the bottleneck.
   - **Calendar time:** list every wait with its real duration. Look it up or say "unknown". Never shrink a wait. Start every wait on day one.

4. **Lay out the plan.** One person can supervise about 3–5 agents at once. Add 10–25% for joining parallel work together. The date is set by the longest chain of agent, human and wait time. Give P50 (likely) and P90 (safe) dates. Ship phase 0 first; later phases ship while it runs.

5. **Check both mistakes.**
   - Build work for a solo MVP on new code coming out in weeks or months? Redo it from units. Months need a wait or human work to explain them.
   - Anything that depends on payments, app stores, partners or real users coming out in hours? It can't.
   - Team work in an existing codebase gains much less from agents (coding is 30–40% of engineering time), so expect modest speed-ups there and tell the user why.
   - If `references/evidence.md` is more than 6 months old, say the numbers are probably too slow and suggest refreshing them.

6. **Calibrate.** Before estimating, run `python3 <skill-dir>/scripts/calibrate.py stats`. If there is history, scale each kind of unit by its median ratio and say so. After building part of the work, log it in minutes: `python3 <skill-dir>/scripts/calibrate.py log --kind build --est 30 --actual 22`.

## Answer

Keep the answer under 300 words. The units are your working, not the answer.

For a small question, one or two sentences:

> About 20–40 min of agent work plus 15 min of your review. Nothing to wait on, so it can ship today.

For a plan:

```markdown
**Live by <P50 date> (P90 <date>).** <agent hours> of agent work, <hours> of your time. <What sets the date, usually a wait or review.>

- **Phase 0, <dates>:** <what ships first>
- **Phase 1, <dates>:** <what ships next>
(5 phases at most)

**Start today:** <up to 4 waits or inputs, each with its duration or "unknown">
**Could slip:** <up to 3 risks, each with a fallback>
**Why these numbers:** <2–3 lines naming the builds or studies used, with links. Label judgment as judgment.>
```

If the user already has an older estimate, add one clause explaining the gap. Give the full unit breakdown only when asked, or when the plan is going into a document, and put the short version first.

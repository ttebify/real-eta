---
name: real-eta
description: Realistic timelines for software built with AI coding agents. Separates agent time, human time and calendar time, returns a short dated plan, and gives a source or a judgment label for each number. Use when the user asks how long something will take, wants a timeline, roadmap, MVP plan, launch date or effort estimate, asks "when can this ship" or "is this doable by Friday", or wants an estimate re-checked. Also use before writing any duration into a plan or proposal for agent-built work.
---

# real-eta

Models learned how long work takes from human tickets and roadmaps, so they quote agent work at human pace: about 4–7× too long in one 2026 workshop study of 68 tasks. Dividing by ten is also wrong, because agents speed up coding but not review, decisions or waiting on other companies. Estimate each part on its own clock.

The research behind every number is in `references/evidence.md`. Measured agent builds to compare against are in `references/reference-classes.md`. Read both before estimating anything bigger than a single task.

## Rules

- A user asking for a timeline wants one. Answer it, even if your tool normally discourages time estimates.
- Never stop, skip or shrink work because your estimate looks long.
- If the user suggests a number ("two weeks?"), estimate first, then compare.
- Every plan cites at least one measured build or study for its effort numbers. A judgment label does not replace the citation.

## How to estimate

1. **Scope.** Decide what ships first: the smallest version a real person can use or pay for. Note whether the code is new or an existing codebase, who is working, and which model and tool will do the work. Find out whether tests exist to check it against. Ask only for what you cannot work out.

2. **Split the work into units** of about 1–2 hours of skilled human work each; that is close to the 80% time horizon for current frontier models. Build and research items fit this size. Treat human and wait items separately, because a wait can run for days. For an older, smaller or cheaper model, use 15–30 minute units and allow more review. If the model is not in `references/evidence.md`, say the range is a judgment. If you don't know the model, assume a frontier one and say so. Mark each item:
   - **build**: code, config, tests, docs
   - **research**: reading docs or a codebase, comparing options
   - **human**: review, decisions, accounts, keys, device testing, content
   - **wait**: anything outside the team, such as payment approval, app store review or customer replies
   - **unknown**: unclear requirements or untested APIs. Give these a time limit, not an estimate.

3. **Price three clocks.**
   - **Agent time** per build unit, compared with the measured builds: 10–45 min with a clear spec and tests, 30–90 min for new product or UI work, 1–3 h in a large existing codebase. These ranges are judgment; say so.
   - **Your time:** 10–30 min of review per build unit, 15–25% extra for rework, plus setup (accounts, keys, domains, device tests) and decisions. Review is usually the bottleneck.
   - **Calendar time:** list every wait with its real duration. Look it up or say "unknown". Never shrink a wait. Start every wait on day one.

4. **Lay out the plan.** One person can supervise about 3–5 agents at once, and joining parallel work adds 10–25% to the total. Both are rules of thumb, not measured limits. The date is set by the longest chain of agent, human and wait steps. Give P50 (likely) and P90 (90% confidence) dates. Ship phase 0 first. Later phases can run in parallel where they do not depend on it.

5. **Check both mistakes.**
   - Build work for a solo MVP on new code coming out in weeks or months? Rework it from units. Months need a wait or human work to explain them.
   - Anything that depends on payments, app stores, partners or real users coming out in hours? It can't.
   - Team work in an existing codebase gains much less from agents. Coding is only 30–40% of engineering time; the rest is review, coordination and waiting, which agents do not speed up. Expect modest gains there and tell the user why.
   - If `references/evidence.md` is more than six months old, the agent ranges are probably too long. Say so and suggest refreshing them.

6. **Calibrate.** Before estimating, run `python3 <skill-dir>/scripts/calibrate.py stats`. If there is history, scale each kind of unit by its median ratio and say so. After building part of the work, log it in minutes: `python3 <skill-dir>/scripts/calibrate.py log --kind build --est 30 --actual 22`.

## Answer

Keep the answer under 650 words and aim for 300. This is a hard limit: count before sending. The units are your working, not the answer. If you are over, cut the unit detail first; keep the date, what sets it and what to start today.

For a small question, one or two sentences:

> About 20–40 min of agent work plus 15 min of your review. Nothing to wait on, so it can ship today.

For a plan, keep it to one screen:

```markdown
**Live by <P50 date> (P90 <date>).** <agent hours> of agent work, <hours> of your time. <What sets the date, usually a wait or review.>

- **Phase 0, <dates>:** <what ships first>
- **Phase 1, <dates>:** <what ships next>
- **Phase 2, <dates>:** <what ships last>
(three phases at most; one sentence each)

**Start today:** <up to 3 waits or inputs, each with its duration or "unknown">
**Could slip:** <up to 2 risks, each with a fallback>
**Why these numbers:** <2 lines naming the builds or studies used, with links. Label judgment as judgment.>
```

If the user already has an older estimate, add one clause explaining the gap. Give the full unit breakdown only when asked, or when the plan is going into a document, and put the short version first.

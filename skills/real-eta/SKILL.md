---
name: real-eta
description: Realistic, evidence-backed timelines for software that AI coding agents will build, split into agent time, human time and calendar time, with a dated ship-first plan and a cited reason for every number. Use this whenever the user asks how long something will take, wants a timeline, roadmap, MVP plan, launch date, phases, sprint plan or effort sizing, asks "when can this ship" or "is this doable by Friday", or asks you to re-check an estimate that looks too long or too short. Also use it before writing any duration into a proposal, plan or document, and whenever you are about to say "this will take N weeks" or "N months" for agent-built work.
---

# real-eta

Language models learned durations from human-written tickets, blog posts and roadmaps. When agents do the build, those numbers are wrong in a predictable way:

- **Models overestimate how long agent work takes.** In one 2026 study, models' estimates before a task overshot the actual duration by 4–7×, and by 5–10× in multi-step agent tasks. Models know how long things take humans, but they cannot sense their own speed.
- **But agents do not shrink everything.** Firm-level data shows coding gets faster while review, rework and coordination absorb much of the gain. External waits (payment approval, app store review, users finding the product) do not speed up at all.

So neither "human estimate" nor "human estimate ÷ 10" is right. Build the estimate bottom-up from agent-sized units, price the human and calendar parts separately and justify every number with a measured comparison. The evidence and its sources are in `references/evidence.md`. Measured builds to compare against are in `references/reference-classes.md`. Read both before giving a timeline for anything larger than a single task.

## When to give a number

Some coding tools tell the model not to volunteer time estimates mid-task. That is sensible for unrequested asides. A user asking for a timeline, roadmap or launch date is an explicit request, so answer it properly with this skill. Two rules apply either way:

- Never use a long estimate as a reason to stop, skip or reduce work without asking. Users have reported agents giving up on 30-minute tasks after predicting weeks.
- If the user names a number ("2 weeks?"), do not anchor on it. Scope first, estimate, then compare.

## Workflow

Match effort to the question. "How long to add dark mode?" gets three lines. A product roadmap gets the full output.

### 1. Pin down scope and context

Establish these from the conversation or the codebase. Ask only for what you cannot infer.

- **What ships first.** Default to the smallest version a real user can pay for or use. If the user wants speed, plan to ship first: turn "validate before building" gates into live metrics, unless a gate protects safety, legal compliance or money that cannot be recovered.
- **New or existing code.** Small new apps are where agents gain most. Large mature codebases gain least (0–10% for complex work in existing code, in one analysis of over 100,000 developers), and human review dominates there.
- **Who is working.** A solo founder or a team? How many parallel agent sessions can they really supervise? Which tools does the session have (deploy commands, browser, test runner)? A step the agent cannot do itself becomes human time.
- **Is there a test oracle?** An existing test suite, worked examples with known answers or a reference implementation is the biggest accelerator. Without one, agents solve the wrong problem and reviews take longer.

### 2. Break the work into agent-sized units

Size each unit at what a skilled engineer would do in about 1–2 hours. That is close to the 1.5 hours at which METR measured frontier agents succeeding about 80% of the time in early 2026, so units this big usually finish without a human rescue. Tag each unit:

- **build**: code, configuration, tests, migrations, docs (agent-heavy)
- **research**: reading docs, exploring a codebase, comparing options (agent-heavy, can run in parallel)
- **human**: decisions, review, manual testing on a device, accounts, keys, content, anything that needs authority or taste
- **wait**: anything outside the team (payment provider approval, app store review, DNS, partner replies, regulators, users building up data)
- **unknown**: unclear requirements, undocumented API, a bug nobody can reproduce. Give it a time limit, not a point estimate.

### 3. Price the three clocks

**Agent time.** Estimate wall-clock time per unit from measured builds, not from a human estimate divided down. Rough bands, to be tightened against `references/reference-classes.md`:

| Unit profile | Agent wall-clock per unit |
|---|---|
| Well specified, with a test oracle (port, CRUD, schema, integration with good docs) | 10–45 min |
| New product or UI work, spec still moving | 30–90 min including iterations |
| Feature in a large existing codebase | 1–3 h, and human time dominates |

These bands are judgment, consistent with the measured builds (for example, 9,000 lines in about 4 hours when a full test suite existed). Say so when you use them.

**Human time.** This is usually the real bottleneck. Budget for:

- **Review:** 10–30 min per build unit (judgment). After agent adoption, pull request review time rose 49% and requests for changes nearly doubled (718 firms). About 45% of merged agent pull requests needed human edits.
- **Rework:** add 15–25% to agent and review time.
- **Setup:** accounts, keys, two-factor authentication, billing, domains, device testing, a final visual check. These add up to hours, and agents routinely forget them.
- **Decisions and content:** pricing, copy, legal text, design choices.

**Calendar time.** List every wait with its real-world duration. If you do not know a provider's current approval time, look it up or say it is unknown. Never compress waits. Start them on day 1 so they overlap the build.

### 4. Lay out the timeline

- **Lanes.** Parallel agent sessions shorten the critical path, but one person supervises about 3–5 well (judgment). More agents is not linear: in one published experiment, 20 agents coordinating through locks delivered the throughput of 2–3.
- **Integration.** Add 10–25% on top of the longest lane for merging and fixing the joins.
- **Critical path.** The timeline is the longest chain of agent, human and wait time, not the sum of agent time.
- **Phases.** Present a dated plan, such as Day 1–2, Day 3–5, Week 2–4, Month 2. Phase 0 is the first thing that ships. Later phases ship while earlier ones run, not after a waiting period.
- **Ranges.** Give P50 (the likely date) and P90 (the safe date). Unknowns widen P90; they never shrink P50.

### 5. Check against both failure modes

- **Anchored on human pace?** If pure build work comes out in weeks or months for a solo MVP on new code, re-derive it from units. Months are a human-team number unless waits or human work explain them. Name which.
- **Over-compressed?** If the plan says "hours" but includes payments, app stores, partners, real data or real users, the calendar cannot be hours.
- **The limit on speed-up.** In teams, writing code is only 30–40% of engineering time. Even instant coding gives at most about 1.5–1.7× end to end unless review and coordination also change. Across firms, shipped output rose by no more than 12% after agent adoption. For team work in existing code, expect modest gains and say so.
- **Stale numbers.** METR's measure of how long a task agents can finish has doubled roughly every 3–4 months since 2024. If `references/evidence.md` is more than about 6 months old, say the numbers are probably conservative and suggest refreshing them.

### 6. Calibrate with real data

Comparing estimates with actual results is the only lasting fix. Forecasting from comparable past projects beats forecasting from the plan, and good worked examples cut model estimation error by about 59%.

- Before estimating, run `python3 <skill-dir>/scripts/calibrate.py stats`. If there is history, scale each unit type by its median actual-to-estimate ratio and say so briefly.
- When you then do part of the work in the same session, note the start and end times and log them: `python3 <skill-dir>/scripts/calibrate.py log --kind build --est 30 --actual 22 --note "auth flow"`. Both numbers are minutes.

## Output: short by default

The unit breakdown in steps 2–4 is your working, not the answer. The reader wants the date, what sets it and what to do today. A 1,500-word plan with a 20-row table buries all three. Aim for **under 300 words**, and well under for small questions.

For a quick question, give one to three sentences that still separate the clocks:

> About 20–40 min of agent work plus ~15 min of your review. Nothing external to wait on, so it can ship today.

For a plan or roadmap, use this and nothing more:

```markdown
**Live by <date P50> (P90 <date>).** <agent range> of agent work, <human range> of your time. <What sets the date, in one clause: usually a wait or review, rarely the code.>

| Phase | When | Ships |
|---|---|---|
| 0. MVP | Day 1–7 | ... |
| 1. ... | Week 2–4 | ... |

**Start today:** <up to 4 waits or inputs, each with its real duration or "unknown">
**Could slip:** <up to 3 risks, each with a time limit or fallback>
**Why these numbers:** <2–3 lines naming the measured builds or studies used, with links. Label judgment as judgment.>
```

Keep phases to 5 rows or fewer, one short line each. Add one clause comparing with a human-team estimate only when the user already holds an older number; seeing where the gap comes from makes the new number believable.

Give the full unit table, per-unit clocks and longer risk notes only when the user asks for detail or the timeline is going into a proposal or planning document. Even then, put the short version first.

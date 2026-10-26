# Evidence behind real-eta

Compiled 25 October 2026. The links were checked when this file was written. Strength: **strong** = peer-reviewed or large sample with a credible design; **moderate** = small sample, workshop paper or single case; **weak** = vendor claim, talk or self-report; **anecdotal** = one issue or report. Refresh it every six months, or sooner when a new frontier model lands.

## 1. Why models give wrong durations

| Finding | Number | Source | Strength |
|---|---|---|---|
| Models' pre-task estimates overshoot actual duration | 4–7× overshoot (p < 0.001); 5–10× error in multi-step agentic tasks; they predict "human-scale minutes for tasks completing in seconds" | Garikaparthi, [Can LLMs Perceive Time?](https://arxiv.org/abs/2604.00010), March 2026, ICLR 2026 workshop | moderate (one author, 68 tasks) |
| Coding agents "estimate durations in human time, and execute in machine time" (anthropocentric time bias). Fixes: ban human units, give an exchange rate, timestamp tool calls, log durations to the repo | qualitative | Monperrus & Stenqvist, [Coding Agents Have Completely Wrong Sense of Time](https://www.monperrus.net/martin/coding-agents-sense-of-time), 2026-09-07 | moderate (expert essay) |
| Models know human event durations well, so the human prior is strong | GPT-4 duration accuracy 89.2% vs humans 97.7% on TRAM; 92.8 on TimeBench duration | [TRAM](https://arxiv.org/abs/2310.00835) (ACL Findings 2024); [TimeBench](https://arxiv.org/abs/2311.17667) (ACL 2024) | strong |
| Models are overconfident about success, and more so deep into agentic tasks | all models overconfident; better-than-random discrimination | Barkan, Black & Sourbut, [Do LLMs Know What They Are Capable Of?](https://arxiv.org/abs/2512.24661), Dec 2025 | moderate |
| Zero-shot LLM effort estimates are worse than predicting the mean; good few-shot examples cut error 59% | GPT-4 MAE 3.87 vs mean baseline 2.44 (APSTUD) | Tawosi et al., [story points with LLMs](https://arxiv.org/abs/2403.08430), 2024 | moderate |
| Claude's own task-time estimates correlate with reality about as well as developers' | Spearman ρ 0.44 (Sonnet 4.5) vs 0.50 (developers); short tasks over-, long tasks underestimated | Anthropic, [Estimating AI productivity gains](https://www.anthropic.com/research/estimating-productivity-gains), Nov 2025 | moderate |
| Users report Claude Code quoting weeks for 30-minute tasks, then bailing out | issue #55576 (2026-05-02), also #8952, #16046, #20270 | [anthropics/claude-code#55576](https://github.com/anthropics/claude-code/issues/55576) | anecdotal |
| Humans share the bias (planning fallacy); the fix is an outside view from comparable past projects | thesis students predicted 33.9 days, took 55.5 | Buehler, Griffin & Ross 1994; Flyvbjerg, [reference class forecasting](https://arxiv.org/abs/1302.3642), 2006 | strong |

## 2. What agents can do unattended

| Finding | Number | Source | Strength |
|---|---|---|---|
| Time horizon (task length in human time that agents finish) | public frontier 50% ≈ 12 h (range 5–61 h), 80% ≈ 1.5 h, Feb–Mar 2026; suite near saturation | METR, [Frontier Risk Report](https://metr.org/blog/2026-05-19-frontier-risk-report/), May 2026 | strong, but uncertain at the top |
| Horizon doubling time | ~131 days since 2023, ~89 days since 2024 | METR Time Horizon 1.1 post, Jan 2026; [time-horizons page](https://metr.org/time-horizons/) (no longer updated after Sept 2026) | strong |
| Real-world performance is weaker than benchmarks | about half of passing SWE-bench Verified solutions would fail real code review (late 2025) | METR Frontier Risk Report | strong |
| The 80% horizon depends on the model | Claude 3.7 Sonnet (Feb 2025) ≈ 12 min; o3 (Apr 2025) ≈ 29 min; GPT-5.3 Codex ≈ 54 min, Claude Opus 4.6 ≈ 69 min, Gemini 3.1 Pro ≈ 89 min (all Feb 2026); Claude Mythos Preview, early (Apr 2026) ≈ 185 min. Small and cheap models are not measured | METR, [Time Horizon 1.1 data](https://metr.org/assets/benchmark_results_1_1.yaml), read 25 October 2026 | strong for the models listed |
| Same task, different model and tool, very different wall-clock time | on ProgramBench, Opus 4.8 in Claude Code averaged 85 min and GPT-5.5 in Codex 17.5 min, with similar pass rates (65.1% and 60.5%); the authors put most of the gap down to the tool and effort setting | Ofengenden and Andriushchenko, [Your Agents Are Not Time Aware](https://www.lesswrong.com/posts/eAbuPXbjakop5rSJx/your-agents-are-not-time-aware), 14 August 2026 | moderate (one benchmark, research blog) |

Use: size units at the 80% horizon of the model actually doing the work. For a current frontier model that is about 1–1.5 human-hours. For an older, smaller or cheaper model, use smaller units (15–30 min of human work) and expect more review. Model choice changes the agent clock only; it does not change review or calendar waits.

## 3. Productivity and where the time goes

| Finding | Number | Source | Strength |
|---|---|---|---|
| Agents raise code output but not shipped output; review is the bottleneck | rise in shipped output above 12% ruled out; PR review time +49%; changes requested ~2×; comments +35%; engineers spend 30–40% of time writing code | Chen & Stratton (Harvard), [AI in the Firm: Bottlenecks in Software Production](https://fion.ac/jellyfish.pdf), Aug 2026, 718 firms | strong |
| Writing code is not shipping code | autonomous agents: commits +240%, projects +80%, releases +30% | Demirer, Musolff & Yang, [NBER w35275](https://www.nber.org/papers/w35275), 2026, 500k+ developers | strong |
| Merged PRs at scale | ~+24% vs counterfactual over 4 months | Microsoft, Claude Code + Copilot CLI rollout, [arXiv 2607.01418](https://arxiv.org/abs/2607.01418), July 2026 | strong |
| Experienced devs on mature repos | early-2025 tools: 19% slower; late-2025 rerun: returning devs ~18% faster (CI −38% to +9%), "very weak evidence" | METR, [2025 RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), [Feb 2026 update](https://metr.org/blog/2026-02-24-uplift-update/) | strong design, small n |
| Greenfield vs brownfield | net gain 15–20%: greenfield/simple 30–40%, brownfield/complex 0–10%; rework 15–25% | Denisov-Blanch (Stanford), AI Engineer talk, June 2025, 100k+ devs | weak (talk) |
| Agent PR acceptance | 71.5% merged across 33.6k agent PRs (Claude Code 59%) | [arXiv 2601.15195](https://arxiv.org/abs/2601.15195), MSR 2026 | strong |
| Merged agent PRs needing edits | only 54.9% merged without changes | [arXiv 2509.14745](https://arxiv.org/abs/2509.14745), n=567 | moderate |
| Parallel agents don't scale linearly | 20 agents with lock coordination produced the throughput of 2–3 | Cursor, [Scaling long-running autonomous coding](https://cursor.com/blog/scaling-agents), Jan 2026 | moderate (vendor) |
| Delegation share | most Anthropic engineers can fully delegate only 0–20% of their work | Anthropic, [How AI is transforming work at Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic), Dec 2025 | weak (self-report) |

## 4. Gaps

- No study measures external approval times (payments, app stores, regulators). Look these up per provider, per project.
- No credible timed builds for Lovable or Bolt.
- Anthropic's "30+ hours of focus" claim for Sonnet 4.5 has no published artifact.

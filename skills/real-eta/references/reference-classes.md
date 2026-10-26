# Reference classes: measured agent builds

Compare a new estimate against the closest row. That is the outside view. These are the best-documented public cases as of 25 October 2026. Most are single cases, so treat them as anchors, not laws. When your own calibration log has data, prefer it (`scripts/calibrate.py stats`).

| Build | What was built | Agent wall-clock | Human time | Conditions | Source |
|---|---|---|---|---|---|
| Port with full test suite | Python HTML5 parser → JS, ~9,000 lines, 43 commits, passes ~9,200 tests | ~4 h | 8 prompts, mostly away | Best case: exact spec + exhaustive tests | Simon Willison, [porting JustHTML](https://simonwillison.net/2025/Dec/15/porting-justhtml/), 2025-12-15 |
| Feature in mature app | macOS update-notification UI in Ghostty | 16 sessions over 3 days | ~8 h of the maintainer's time; first attempt discarded, 4 sessions failed on one bug | Brownfield, high quality bar | Mitchell Hashimoto, [Vibing a non-trivial Ghostty feature](https://mitchellh.com/writing/non-trivial-vibing), 2025-10-11 |
| Large system, many agents | Rust C compiler, 100,000 lines, builds Linux 6.9 on 3 architectures | ~2 weeks, 16 agents, ~2,000 sessions, <$20k | Harness design and tests; no active intervention | Near-perfect test oracle (GCC torture tests) | Anthropic, [Building a C compiler](https://www.anthropic.com/engineering/building-c-compiler), Feb 2026 |
| Single deep task in huge codebase | Activation-vector extraction in vLLM (12.5M lines), 99.9% numerical match | 7 h single run | Occasional guidance | Clear numerical target | Anthropic, [Rakuten case study](https://claude.com/customers/rakuten), 2025 (vendor) |
| Production mobile app, small team | Sora for Android | 28 days to launch | 4 engineers doing architecture, planning, verification | Production quality bar | OpenAI via the-decoder, Dec 2025 (secondary) |
| Hundreds of agents | Browser from scratch, >1M lines | ~1 week | Not reported; "still needs careful review" | Experimental, quality unmeasured | Cursor, [Scaling agents](https://cursor.com/blog/scaling-agents), Jan 2026 |
| Firm-level adoption | Normal team work | n/a | Review time +49%, shipped output ≤ +12% | 718 firms | Chen & Stratton, Aug 2026 |

The firm-level row is an adoption study, not a single build.

## Reading the table

- **Solo greenfield MVP with clear tests:** closest to the Willison row. Code is hours to a few days. The date is set by human review, accounts and external waits.
- **Feature in an existing product:** closest to the Hashimoto row. Expect days of calendar time and hours of human attention per feature, even with agents.
- **Team, production quality:** closest to the Sora and firm-level rows. Agents raise output, but review caps the end-to-end gain, so expect weeks.
- **Large scope with a strong oracle:** the C compiler row shows weeks for very large systems. Without the oracle, expect much worse.

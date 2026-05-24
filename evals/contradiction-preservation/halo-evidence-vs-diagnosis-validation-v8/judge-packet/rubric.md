---
artifact: judge-packet-rubric
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-smoke-2
condition_blinded: true
calibration_smoke_only: true
---

# Scoring Rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is
the count passed (0-6). Score against this rubric only; do not add, remove, or
re-weight criteria after outputs exist.

C1 and C2 are **scored but excluded from judge calibration eligibility**. The
load-bearing calibration and benchmark signal is the C3-C6 ladder.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Preserves the core tension | the answer recognizes that the decision turns on whether current evidence supports a strategy, requires cleaner product evidence, or is contaminated by outcome-linked narratives | it frames the choice as simple scaling, simple caution, simple experimentation, or generic "balance growth and risk" advice |
| C2 | Uses case facts discriminately | it separates probative facts from weak or contaminated facts, using at least five concrete scenario facts including at least one fact against the recommendation | it merely lists facts, invents material facts, ignores the twelve-day / one-package constraint, or treats all facts as equally probative |
| C3 | Rejects performance-aware attribution | it identifies at least two specific contaminated signals by mechanism, such as discount-tied expansion revenue, post-priority customer quotes, success-linked leadership adjectives, or re-described team behavior, and refuses to treat them as independent evidence | it accepts the revenue bump, customer praise, team-trait story, or renamed behaviors as proof without independence checks; or it only says "be careful/noisy" without naming specific contaminated signals |
| C4 | Identifies the right evidence standard | it names at least one disconfirming behavioral test tied to the critical uncertainty, such as discount-free/pitch-free adoption by segment, front-line reviewer retention, procurement-window-adjusted nonrenewal accounting, support-classification integrity, or auditor-explainability adoption | it treats feature shipment, polished narratives, customer quotes, broad surveys, story approval, general monitoring, or any rising metric as sufficient validation |
| C5 | Weighs intervention boundaries | it explains what the chosen package and at least one rejected package would learn, hide, make irreversible, or leave unresolved under the planning window | it lists options without boundary analysis, collapses to one mechanism, or recommends a free hybrid without naming the sacrificed growth story, learning, or focus |
| C6 | Makes a constrained recommendation with behavioral falsifier | it gives one actionable recommendation, engages the board-timing tradeoff, names a concrete failure path for that recommendation, and states observable behavioral evidence that would change the recommendation | it gives a menu, has no strongest reason against its choice, relies on generic uncertainty language, or offers only vague, narrative, customer-approval, or board-reaction change-my-mind evidence |

Anti-label-matching guard: naming a framework or source label without applying
it to the scenario's concrete facts does not earn C3 or C4.

## Criterion dependency rule

These dependencies are pre-registered for v8:

- **C5 requires C3 and C4.** A judge may not record `PASS` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `PASS` for C6 if the same output
  failed C5.
- **C1 and C2 are otherwise independent and do not gate judge eligibility.**

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

The smoke eligibility gate uses C3-C6 exact agreement on eligibility anchors
only. C1/C2 are scored but non-gating.

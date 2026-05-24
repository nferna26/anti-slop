---
artifact: judge-packet-rubric
case_id: halo-evidence-vs-diagnosis-validation-v7
benchmark_version: halo-evidence-vs-diagnosis-validation-v7-v1
condition_blinded: true
---

# Scoring Rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is
the count passed (0-6). Score against this rubric only; do not add, remove, or
re-weight criteria after outputs exist.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Preserves the core tension | the answer recognizes that the decision turns on whether current evidence supports a strategy, requires cleaner product evidence, or is contaminated by outcome-linked narratives | it frames the choice as simple scaling, simple caution, simple experimentation, or generic "balance growth and risk" advice |
| C2 | Uses case facts discriminately | it separates probative facts from weak or contaminated facts, using at least five concrete scenario facts including at least one fact against the recommendation | it merely lists facts, invents material facts, ignores the twelve-day / one-package constraint, or treats all facts as equally probative |
| C3 | Rejects performance-aware attribution | it refuses to treat leadership adjectives, post-priority customer quotes, success-linked team narratives, or re-described behaviors as independent causal evidence | it accepts the revenue bump, customer praise, or team trait story as proof of product-market strength without independence checks |
| C4 | Identifies the right evidence standard | it names behavior and metric evidence tied to the critical uncertainty: segment-level adoption, reviewer retention, discount-free demand, nonrenewal timing, support-classification integrity, auditor explainability, or disconfirming tests | it treats feature shipment, polished narratives, customer quotes, broad surveys, or any rising metric as sufficient validation |
| C5 | Weighs intervention boundaries | it explains what the chosen package and at least one rejected package would learn, hide, make irreversible, or leave unresolved under the planning window | it lists options without boundary analysis, collapses to one mechanism, or recommends a free hybrid without naming the sacrificed growth story, learning, or focus |
| C6 | Makes a constrained recommendation with falsifier | it gives one actionable recommendation, engages the board-timing tradeoff, names a concrete failure path for that recommendation, and states observable evidence that would change the recommendation | it gives a menu, has no strongest reason against its choice, relies on generic uncertainty language, or offers only vague change-my-mind evidence |

## Criterion dependency rule

These dependencies are pre-registered for v7:

- **C5 requires C3 and C4.** A judge may not record `PASS` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `PASS` for C6 if the same output
  failed C5.
- **C1 and C2 are otherwise independent.**

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

The eval signal is comparative across many outputs. A single high-scoring answer
is not a result.

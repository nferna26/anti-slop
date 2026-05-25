---
artifact: judge-packet-rubric
case_id: normalization-vs-latent-errors-runway-lighting-v5
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
condition_blinded: true
---

# Scoring Rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is
the count passed (0-6). Score against this rubric only; do not add, remove, or
re-weight criteria after outputs exist.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Identifies the inferred live tension | the answer substantively treats the case as a conflict between possible acceptance-threshold drift and possible dormant equipment/defence weakness, with or without naming either mechanism | it frames the decision as a simple safety pause, simple monitor installation, simple maintenance fix, cost tradeoff, or generic "do both" problem |
| C2 | Selects load-bearing evidence | it uses at least five concrete scenario facts, including at least one fact that supports the recommendation and one fact that cuts against it | it is generic, merely recites facts without using them, invents material facts, or ignores the twelve-day / six-hour constraint |
| C3 | Infers acceptance-threshold drift from traces | it infers a possible drifted closure threshold from at least two administrative traces, such as repeated closure phrases, faster closure times, missing voltage readings, supervisor sign-off becoming part of closure, or the dashboard not changing the pattern | it merely names culture/normalization/process, treats added checks as proof of control, or treats no incursion as settling the acceptance question |
| C4 | Infers a dormant-defect / defence path | it identifies a concrete dormant technical or defence failure path and explains why visible lights, clean history, or process checks do not rule it out under the construction surge | it says "fix the hardware" without a failure path, dismisses all defences as ritual, or treats the technical clues as irrelevant background |
| C5 | Weighs intervention boundaries | it compares the chosen path with at least one rejected path by explaining what each would and would not learn or prevent under the six-hour closure | it lists options without boundary analysis, collapses to one mechanism, or recommends a free hybrid without naming the sacrificed protection or learning |
| C6 | Makes a constrained recommendation | it gives one actionable recommendation, engages the twelve-day / six-hour / surge tradeoff, names a concrete failure path for that recommendation, and states observable evidence that would change the recommendation | it gives a menu, relies on a foreclosed move, gives no strongest reason against its choice, or offers only generic disconfirming evidence |

## Criterion dependency rule

These dependencies are pre-registered for v5:

- **C5 requires C3 and C4.** A judge may not record `pass` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `pass` for C6 if the same output
  failed C5.
- **C1 and C2 are otherwise independent.** A fluent answer can pass C1/C2 while
  still failing the mechanism and recommendation ladder.

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

The eval signal is comparative across many outputs. A single high-scoring answer
is not a result.

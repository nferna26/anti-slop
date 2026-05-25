---
artifact: judge-packet-rubric
case_id: normalization-vs-latent-errors-print-vault-v6
benchmark_version: normalization-vs-latent-errors-print-vault-v6-v1
condition_blinded: true
---

# Scoring Rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is
the count passed (0-6). Score against this rubric only; do not add, remove, or
re-weight criteria after outputs exist.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Identifies the inferred live tension | the answer substantively treats the case as a conflict between possible exception-acceptance drift and possible dormant air-handling / moisture-defence weakness, with or without naming either mechanism | it frames the decision as a simple dashboard upgrade, simple preservation pause, simple maintenance job, relationship-cost tradeoff, or generic "do both" problem |
| C2 | Selects load-bearing evidence | it uses at least five concrete scenario facts, including at least one fact that supports the recommendation and one fact that cuts against it | it is generic, merely recites facts without using them, invents material facts, or ignores the nine-day / six-hour / 35 percent surge constraint |
| C3 | Infers acceptance-threshold drift from subtle traces | it infers a possible drifted exception threshold from at least two administrative traces, such as repeated "normalized by morning trend" notes, missing handheld readings, second initials becoming routine closure, the green-tile average, or dashboard smoothing | it merely says "process problem" or "staff complacency," treats added initials and dashboarding as proof of control, or treats no visible damage as settling the acceptance question |
| C4 | Infers a dormant-defect / defence path | it identifies a concrete dormant physical or defence-stack failure path and explains why weekly range summaries, dry bench testing, or short door holds do not rule it out under the surge | it says "fix the equipment" without a failure path, dismisses all monitoring as ritual, or treats the technical clues as irrelevant background |
| C5 | Weighs intervention boundaries | it compares the chosen package with at least one rejected package by explaining what each would and would not learn, reveal, suppress, or prevent under the six-hour window | it lists options without boundary analysis, collapses to one mechanism, or recommends a free hybrid without naming the sacrificed protection, learning, or escalation |
| C6 | Makes a constrained recommendation | it gives one actionable recommendation, engages the nine-day / six-hour / surge tradeoff, names a concrete failure path for that recommendation, and states observable evidence that would change the recommendation | it gives a menu, relies on a foreclosed move, gives no strongest reason against its choice, or offers only generic disconfirming evidence |

## Criterion dependency rule

These dependencies are pre-registered for v6:

- **C5 requires C3 and C4.** A judge may not record `pass` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `pass` for C6 if the same output
  failed C5.
- **C1 and C2 are otherwise independent.** A fluent answer can pass C1/C2 while
  still failing the mechanism and recommendation ladder.

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

The eval signal is comparative across many outputs. A single high-scoring answer
is not a result.

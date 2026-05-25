---
artifact: judge-packet-rubric
case_id: normalization-vs-latent-errors-water-treatment-v4
benchmark_version: normalization-vs-latent-errors-water-treatment-v4-v1
condition_blinded: true
---

# Scoring Rubric

Score each anonymised `OUT-NN` answer against the six criteria below. Each
criterion is **pass** or **fail**. The per-output score is the count of criteria
passed (0-6). Score against this rubric only; do not add, remove, or re-weight
criteria after seeing outputs.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Identifies the live tension | the answer substantively treats normalization of warning signs and latent-errors / defences as legitimate, competing mechanisms for this decision, with or without naming them | it presents only one mechanism, treats the choice as obvious, or makes the other mechanism a strawman |
| C2 | Anchors in scenario facts | it reasons from at least four load-bearing scenario facts, including at least one constraint fact about the ten-day decision, high-flow load, restrictions, or 36-hour window | it is generic, merely recites facts, invents material facts, or ignores the binding operating constraint |
| C3 | Preserves the latent-errors / defences objection | it keeps live the objection that unresolved technical defects and weak or missing defences may be the load-bearing problem, and that a defence or repair response may be necessary | it treats the case as purely cultural, dismisses the analyzer/valve/interlock facts, or treats all added defences as ritual by default |
| C4 | Preserves the normalization-of-deviance objection | it infers from the alarm/exception pattern that the plant may be reclassifying warning signs as acceptable, and connects that possibility to the risk of high-flow operation | it treats clean downstream samples, no violation, or process additions as settling safety; or mentions drift only as a label without using it |
| C5 | Weighs the intervention boundary | it trades C3 and C4 against each other, explaining what another defence can and cannot reach and what threshold/reset work can and cannot reach | it lists both mechanisms without weighing them, commits to one side while ignoring the other's strongest objection, or dissolves the choice into a free hybrid |
| C6 | Concrete recommendation under constraint | it gives one actionable recommendation, engages the single 36-hour window and the ten-day/high-flow tradeoff, names a concrete failure path, and states observable evidence that would change the recommendation | it hands back a menu, relies on a foreclosed move, gives no strongest reason against its choice, or offers only generic disconfirming evidence |

The eval's signal is comparative across many outputs. A single high-scoring
answer is not a result.

## Criterion dependency rule

These dependencies are pre-registered and leave no judge-discretion escape:

- **C5 requires C3 and C4.** A judge may not record `pass` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `pass` for C6 if the same output
  failed C5.
- **C1, C2, C3, and C4 are otherwise scored independently.** C3 or C4 may pass
  when C6 fails; preserving one side of the tension is necessary, not
  sufficient.

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

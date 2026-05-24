---
artifact: judge-packet-rubric
case_id: diagnosis-vs-validated-learning-benefits-renewal-v3
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v3-v1
condition_blinded: true
---

# Scoring Rubric

Score each anonymised `OUT-NN` answer against the six criteria below. Each
criterion is **pass** or **fail**. The per-output score is the count of criteria
passed (0-6). Score against this rubric only; do not add, remove, or re-weight
criteria after seeing outputs.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Identifies the live tension | the answer substantively treats diagnosis-and-act and validate-before-scale as legitimate, competing approaches to this decision, with or without labels | it presents only one approach, treats the choice as obvious, or makes the other side a strawman |
| C2 | Anchors in scenario facts | it reasons from at least three load-bearing scenario facts, including at least one constraint fact about the appropriation or lock-in | it is generic, merely recites facts, invents material facts, or ignores the binding funding structure |
| C3 | Preserves the diagnosis-first objection | it keeps live the objection that action needs a disciplined diagnosis of the critical cause, and that scattered pilots may test tactics without identifying what matters most | it ignores this objection, treats experimentation as automatically superior, or caricatures diagnosis as endless analysis |
| C4 | Detects and uses the under-evidence problem | it infers from the scenario that the handoff story is plausible but not established, and connects that gap to the risk of a near-irreversible budget commitment | it treats the working group's confidence as settling the cause, notes uncertainty only generically, or fails to connect uncertainty to the commitment |
| C5 | Weighs the two objections against each other | it trades the diagnosis-first and under-evidence objections off in the reasoning; a definite single-sided recommendation can pass if the losing objection is weighed and answered | it lists both objections without weighing them, commits to one side while ignoring the other, or dissolves the tension into an unspecified "hybrid" |
| C6 | Concrete recommendation under the binding constraint | it gives one actionable recommendation, engages the indivisible non-reservable appropriation and six-month lock-in, names a concrete failure path, and states observable evidence that would change the recommendation | it hands back a menu, relies on a foreclosed move, gives no strongest reason against its choice, or gives only generic disconfirming evidence |

The eval's signal is comparative across many outputs. A single high-scoring
answer is not a result.

## Criterion dependency rule

These dependencies are pre-registered and leave no judge-discretion escape:

- **C5 requires C3 and C4.** A judge may not record `pass` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `pass` for C6 if the same output
  failed C5.
- **C1, C2, C3, and C4 are otherwise scored independently.** C3 may pass even
  when C6 fails; preserving one objection is necessary, not sufficient.

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

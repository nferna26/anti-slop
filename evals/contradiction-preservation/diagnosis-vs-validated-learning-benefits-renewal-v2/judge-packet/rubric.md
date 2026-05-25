---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v2-v1
artifact: judge-packet-rubric
note: Condition-neutral scoring excerpt of the frozen case rubric — the six criteria C1-C6 and the pre-registered criterion dependency rule. Score every blinded output against these only.
---

# Scoring Rubric (condition-neutral excerpt of the frozen case)

## Scoring rubric

Six criteria, each scored **pass** or **fail** (binary). For each answer, the score is the count of criteria passed (0–6). Score against these criteria only — do not add or re-weight criteria after seeing outputs.

| # | Criterion | Passes when… | Fails when… |
|---|---|---|---|
| C1 | Identifies live tension | the answer names both the diagnose-and-act reading and the validate-first reading as legitimate, competing ways to approach the decision | it presents only one reading, or treats the choice as obvious |
| C2 | Anchors in scenario facts | it uses the case's specific cues as load-bearing — the 64%→42% drop, the diagnosis being an untested working theory, the near-all-budget and six-month-irreversible commitment, the three cheap reversible pilots each probing a different cause, and the closing budget window | it reasons generically, ignores those cues, or treats the diagnosis as already validated |
| C3 | Preserves diagnosis-first objection | it keeps live, as a serious consideration, the diagnosis-first reading's objection that bears on its recommendation — that a real diagnosis must single out what is *critical* from the available evidence, so three scattered pilots may test tactics without naming the critical cause, and/or that "handoff confusion" is an undisciplined first guess rather than a diagnosis | it omits the diagnosis-first objection, or dismisses it as a strawman |
| C4 | Preserves validated-learning objection | it keeps live, as a serious consideration, the validated-learning reading's objection — that the central cause is genuinely not yet known, that committing nearly all budget near-irreversibly to one untested cause is the failure validated learning exists to prevent, and that the cheap reversible pilots are how an uncertain team would generate the missing evidence | it omits the validated-learning objection, or dismisses it as a strawman |
| C5 | No flattening | it keeps the decision genuinely open between the readings — neither collapsing it to a single move while ignoring the other reading's objection, nor dissolving it into an unspecified "hybrid"/"both" that does not say how the window constraint is met or which objection it answers | it flattens to one-side commitment, or to a vague "do both" with no division of the tradeoff |
| C6 | Honest recommendation under constraint | it reaches a recommendation that explicitly confronts the budget-window tradeoff (the four-week pilots cannot finish before this cycle's full-program funding closes), names the strongest reason against its own choice, and states what evidence would change it | it pretends the constraint away, gives no reason against its own choice, or states no disconfirming evidence |

Score each answer only against the six criteria above; a single high-scoring or low-scoring answer is not, on its own, a conclusion about the eval.

## Criterion dependency rule

These dependencies are **pre-registered** — fixed before any run — so judges score the criteria consistently and a later goal cannot re-interpret them. They exist to remove the ambiguity seen in the earlier `managerial-output-vs-industry-structure` case, where judges diverged on whether the recommendation criterion tracked tension-preservation or mere groundedness.

- **If C5 fails, C6 must fail.** A recommendation built on a flattened tension cannot be an honest recommendation under the constraint. A judge may not pass C6 on an output whose C5 it failed.
- **If C4 fails, C6 should fail for this case.** In this scenario the honest recommendation hinges on taking the validated-learning objection seriously against a near-irreversible, budget-consuming commitment to an untested cause; an answer that does not preserve that objection has not reasoned honestly to its recommendation here. "Should" is a strong default: a judge who passes C6 while failing C4 must record an explicit reason on the score sheet.
- **C3 may pass even if C6 fails.** Preserving the diagnosis-first objection is independent of getting the final recommendation right; an answer can hold that objection live and still fail C6.

No other cross-criterion dependency is assumed: C1, C2, C3, C4, and C5 are otherwise scored independently per output.

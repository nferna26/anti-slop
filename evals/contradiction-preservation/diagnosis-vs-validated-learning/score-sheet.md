---
case_id: diagnosis-vs-validated-learning
eval_type: contradiction-preservation
scoring_status: unscored
---

# Score Sheet

Score against the rubric in `case.md` → `## Scoring rubric`. Each of the five criteria is scored `pass` or `fail` per model condition. Per-condition score is the count of criteria passed (0–5).

## Result

pass | partial | fail

## Scores

Mark each cell `pass` or `fail`. One column per `model_condition` from the case; leave a column blank if that condition was not run.

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | optional_local_model |
| --- | --- | --- | --- | --- |
| Tension recognised |  |  |  |  |
| Scenario located |  |  |  |  |
| No framework-default |  |  |  |  |
| Lineage discipline |  |  |  |  |
| Honest recommendation |  |  |  |  |
| **Per-condition score (0–5)** |  |  |  |  |

## Comparative signal

Per-condition score is 0–5. The eval signal is comparative, not absolute: `substrate_workflow` should beat `vanilla` and `famous_sources_supplied` across runs. A single high-scoring answer does not settle the case; `substrate_workflow` failing to beat `vanilla` across runs falsifies it (see `case.md` → `## Falsifier`).

## Judge Notes

## Follow-up

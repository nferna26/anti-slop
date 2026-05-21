---
case_id: normalization-vs-latent-errors
eval_type: contradiction-preservation
scoring_status: unscored
---

# Score Sheet

Score against the rubric in this case's `case.md` → `## Scoring rubric`. Each of the five criteria is scored `pass` or `fail` per model condition. Per-condition score is the count of criteria passed (0–5). The criteria below are copied verbatim from the case rubric — do not score against generic or remembered criteria.

## Result

partial — the case is drafted and no condition has been run yet; `scoring_status` is `unscored`. No conditions, no baseline, no receipts, so none of the v1 requirements in `docs/eval-result-status-policy.md` for a `dry_run_supported` or `benchmark_supported` status are met. The status moves off `partial` only after an evaluation pass has run and scored the conditions.

## Scores

One column per `model_condition` from the case; mark each cell `pass` or `fail` when a run is scored, and leave a column blank until that condition is run. Per-condition score is the count of criteria passed (0–5).

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | optional_local_model |
| --- | --- | --- | --- | --- |
| Tension recognised |  |  |  |  |
| Scenario located |  |  |  |  |
| Acceptance-threshold check |  |  |  |  |
| No flatten |  |  |  |  |
| Honest recommendation |  |  |  |  |
| **Per-condition score (0–5)** |  |  |  |  |

## Comparative signal

The eval signal is comparative, not absolute: `substrate_workflow` should beat `vanilla` and `famous_sources_supplied` across runs, per `case.md` → `## Positive result`. A single high-scoring answer does not settle the case; `substrate_workflow` failing to beat `vanilla` across runs falsifies it, per `case.md` → `## Falsifier`. No runs yet — no signal to report.

## Judge Notes

No runs scored. The case has been drafted (`status: draft`, `scoring_status: unscored`) and awaits an evaluation pass. When run: each model condition gets exactly the source packet the case defines; `optional_local_model` is a real local-model run or is deferred, never simulated; every model output is a test artifact, never an authority; each output is scored against the five criteria above, criterion by criterion.

## Follow-up

- Run an evaluation pass: `vanilla`, `famous_sources_supplied`, and `substrate_workflow` (real runs preferred; in-session simulations otherwise, labelled honestly), and `optional_local_model` as a real local-model run or an explicit deferral.
- After the pass, set `Result` against `docs/eval-result-status-policy.md`: `partial` until all required conditions are in; then `dry_run_supported`, `benchmark_supported`, `inconclusive`, or `falsified` as the evidence warrants.
- This result is not eligible to support a canon candidate unless and until it reaches `benchmark_supported`.

---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
eval_type: contradiction-preservation
scoring_status: unscored
---

# Score Sheet

Score against the rubric in this case's `case.md` → `## Scoring rubric`: six binary criteria C1–C6, each `pass` or `fail` per model condition per run. Per-run per-condition score is the count of criteria passed (0–6). Apply the pre-registered `## Criterion dependency rule` and the `## Judge protocol` from `case.md`. Do not score against generic or remembered criteria.

This is an **unscored scaffold**. The case is `status: draft`, `scoring_status: unscored`; no model has been run. The tables below are the shape the judges fill after a frozen, anonymised run.

## Result

partial — no runs yet. This is a fresh `draft` case: the Advisor prompt, rubric, dependency rule, pre-registered margins, falsifier, and `model_conditions` are defined but not yet frozen-and-run, so scoring is incomplete and the Result is `partial` per `docs/eval-result-status-policy.md`. The Result is not eligible to move above `partial` until a frozen run is scored under the `## Judge protocol` and the `## Positive result` clauses in `case.md` are all met and judge-confirmed; `benchmark_supported` additionally requires the full `docs/eval-benchmark-upgrade.md` checklist. A `partial` result supports no public advice claim and is not eligible to support a canon candidate.

## Scores

No runs scored. When a frozen run exists, each judge records one table per run, per the `## Judge protocol` — pass/fail for every criterion C1–C6 on every output, with the criterion dependency rule applied. Template (one per run):

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | criteria_prompted_no_sources |
| --- | --- | --- | --- | --- | --- |
| C1 Identifies live tension |  |  |  |  |  |
| C2 Anchors in scenario facts |  |  |  |  |  |
| C3 Preserves diagnosis-first objection |  |  |  |  |  |
| C4 Preserves validated-learning objection |  |  |  |  |  |
| C5 No flattening |  |  |  |  |  |
| C6 Honest recommendation under constraint |  |  |  |  |  |
| **Per-condition score (0–6)** |  |  |  |  |  |

## Comparative signal

No runs scored. When scored, this section records: mean score per condition; the `substrate_workflow` vs `vanilla_long_prompt` and vs `criteria_prompted_no_sources` aggregate margins against the pre-registered ≥1.5-point bar; the C4/C5/C6 pass-rate margins against the pre-registered ≥0.33 bar; and whether the `## Falsifier` is met. Per `case.md`, a substrate win requires clearing every `## Positive result` clause; a judge-dependent outcome stays `partial`.

## Judge Notes

None yet — the case is unscored. After a frozen, anonymised run, this section records each judge's identity and model family, the criterion-level verdicts, any third-judge trigger on C5/C6 or margin disagreement, and whether the outcome is judge-sensitive (which keeps the Result `partial`).

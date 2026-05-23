---
case_id: normalization-vs-latent-errors-runway-lighting-v5
eval_type: contradiction-preservation
scoring_status: unscored
---

# Score Sheet

Score only against `case.md` -> `## Scoring rubric`. Do not score from source
prestige, source names, model fluency, or a preferred operational answer. A
model output is a test artifact, not an authority.

## Result

partial - v5 is drafted but not frozen, not run, not judged, and not reconciled.
The calibration anchors in `judge-packet/calibration-anchors.md` are
agent-drafted and proposed; operator acceptance is required before any freeze or
model run. This case cannot support any public claim, canon candidate, or
`benchmark_supported` status.

## Calibration gate

`judge-packet/calibration-anchors.md` is `status: proposed_unreviewed`. Every
eligible judge must complete the calibration exercise before scoring real
`OUT-NN` answers. A judge that fails the pre-registered calibration gate scores
zero real outputs for this benchmark version.

## Blind judge scoring surface

Judge-facing rows use anonymised `OUT-NN` labels only. Condition labels, run
numbers, seeds, model-output receipt paths, and the answer key are withheld until
blind scoring is complete.

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OUT-01 |  |  |  |  |  |  |  |  |
| OUT-02 |  |  |  |  |  |  |  |  |
| OUT-03 |  |  |  |  |  |  |  |  |
| OUT-04 |  |  |  |  |  |  |  |  |
| OUT-05 |  |  |  |  |  |  |  |  |
| OUT-06 |  |  |  |  |  |  |  |  |
| OUT-07 |  |  |  |  |  |  |  |  |
| OUT-08 |  |  |  |  |  |  |  |  |
| OUT-09 |  |  |  |  |  |  |  |  |
| OUT-10 |  |  |  |  |  |  |  |  |
| OUT-11 |  |  |  |  |  |  |  |  |
| OUT-12 |  |  |  |  |  |  |  |  |
| OUT-13 |  |  |  |  |  |  |  |  |
| OUT-14 |  |  |  |  |  |  |  |  |
| OUT-15 |  |  |  |  |  |  |  |  |
| OUT-16 |  |  |  |  |  |  |  |  |
| OUT-17 |  |  |  |  |  |  |  |  |
| OUT-18 |  |  |  |  |  |  |  |  |
| OUT-19 |  |  |  |  |  |  |  |  |
| OUT-20 |  |  |  |  |  |  |  |  |
| OUT-21 |  |  |  |  |  |  |  |  |
| OUT-22 |  |  |  |  |  |  |  |  |
| OUT-23 |  |  |  |  |  |  |  |  |
| OUT-24 |  |  |  |  |  |  |  |  |
| OUT-25 |  |  |  |  |  |  |  |  |
| OUT-26 |  |  |  |  |  |  |  |  |
| OUT-27 |  |  |  |  |  |  |  |  |
| OUT-28 |  |  |  |  |  |  |  |  |
| OUT-29 |  |  |  |  |  |  |  |  |
| OUT-30 |  |  |  |  |  |  |  |  |
| OUT-31 |  |  |  |  |  |  |  |  |
| OUT-32 |  |  |  |  |  |  |  |  |
| OUT-33 |  |  |  |  |  |  |  |  |
| OUT-34 |  |  |  |  |  |  |  |  |
| OUT-35 |  |  |  |  |  |  |  |  |
| OUT-36 |  |  |  |  |  |  |  |  |
| OUT-37 |  |  |  |  |  |  |  |  |
| OUT-38 |  |  |  |  |  |  |  |  |
| OUT-39 |  |  |  |  |  |  |  |  |
| OUT-40 |  |  |  |  |  |  |  |  |

## Dependency checks

- C5 requires C3 and C4.
- C6 requires C5.
- Any C5 pass with C3 or C4 fail is a scoring inconsistency.
- Any C6 pass with C5 fail is a scoring inconsistency.

## Post-reconciliation condition aggregate

Operator-only. Fill only after all eligible blind scoring is complete. Reconcile
aggregate-only from committed output hashes; do not commit a per-`OUT-NN` to
condition mapping.

| Judge | Condition | n | Mean total | C3 pass | C4 pass | C5 pass | C6 pass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
|  | `vanilla` |  |  |  |  |  |  |
|  | `famous_sources_supplied` |  |  |  |  |  |  |
|  | `substrate_workflow` |  |  |  |  |  |  |
|  | `vanilla_long_prompt` |  |  |  |  |  |  |
|  | `generic_advice_prompted` |  |  |  |  |  |  |

## Comparative signal

None yet. No model outputs or judge scores exist.

## Judge Notes

No judge has calibrated or scored v5. Calibration anchors are proposed only and
must be operator-approved before freeze.

## Follow-up

1. Operator-review `judge-packet/calibration-anchors.md`.
2. If approved, set the anchors to `filled_pre_run`, freeze the run packet, and
   generate the 8-run-per-condition benchmark pass.
3. Build the condition-blind judge packet and run OpenAI and Anthropic API
   judges with calibration first.

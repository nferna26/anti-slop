---
case_id: normalization-vs-latent-errors-water-treatment-v4
eval_type: contradiction-preservation
scoring_status: unscored
---

# Score Sheet

Score only against `case.md` -> `## Scoring rubric`. Do not score from source
prestige, source names, model fluency, or a preferred operational answer. A
model output is a test artifact, not an authority.

## Result

partial - v4 scaffold only. No run packet has frozen a benchmark version, no
model outputs exist, no judge has calibrated, no output has been scored, and no
condition aggregate or decision exists. A prepared `run-packet.md` exists but is
not frozen and authorizes no output generation. This case cannot support any
public claim, canon candidate, or `benchmark_supported` status.

## Calibration gate

`judge-packet/calibration-anchors.md` is currently `status: proposed_unreviewed`.
The agent-drafted anchors must be operator-reviewed and accepted before any v4
freeze, model run, or judge-packet release.

Every eligible judge must complete the calibration exercise before scoring real
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

Extend the table after a frozen run if the benchmark version uses more than
eight runs per condition.

## Dependency checks

- C5 requires C3 and C4.
- C6 requires C5.
- Any C5 pass with C3 or C4 fail is a scoring inconsistency.
- Any C6 pass with C5 fail is a scoring inconsistency.

## Post-reconciliation condition aggregate

Operator-only. Fill only after all eligible blind scoring is complete and the
local-only answer key has been applied aggregate-only.

| Judge | Condition | n | Mean total | C3 pass | C4 pass | C5 pass | C6 pass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
|  | vanilla |  |  |  |  |  |  |
|  | famous_sources_supplied |  |  |  |  |  |  |
|  | substrate_workflow |  |  |  |  |  |  |
|  | vanilla_long_prompt |  |  |  |  |  |  |
|  | generic_advice_prompted |  |  |  |  |  |  |

Do not commit a per-`OUT-NN` to condition mapping. Commit aggregate tables only.

## Comparative signal

None yet. The planned signal is comparative: `substrate_workflow` must separate
from `vanilla_long_prompt` and `generic_advice_prompted` on both total score and
the C3/C4/C5/C6 critical criteria, under at least two eligible external blind
judges. The full pre-registered rule is in `case.md` -> `## Positive result`.

## Judge Notes

No judge has calibrated or scored this v4 case.

## Follow-up

1. Operator-review and accept `judge-packet/calibration-anchors.md` before any
   freeze or run.
2. Freeze `run-packet.md` with exact condition packets, hashes,
   equal-length filler checks, run count, generator model, and two external
   eligible judge routes named before generation.
3. Generate all real outputs, build the condition-blind judge packet, collect
   calibrated external judge scores, reconcile aggregate-only, and record a
   decision.

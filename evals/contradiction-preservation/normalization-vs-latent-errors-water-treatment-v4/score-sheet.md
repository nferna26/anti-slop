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

partial - v4 frozen run complete, one eligible OpenAI API judge receipt recorded,
unreconciled. `run-packet.md` freezes the v4-v1 condition packets, equal-length
filler, generator/runtime snapshot, and external judge routes; forty real
`gemma4:31b` model outputs exist and a condition-blind judge packet is built.
Hosted OpenAI `gpt-5.4-mini` passed calibration and scored all forty `OUT-NN`
outputs. On 2026-05-23, the operator accepted hosted API calls run by Codex with
operator-provided keys as result-lifting judge routes for v4 when the judge
remains condition-blind, passes calibration, and the receipt records the route
honestly; the OpenAI receipt therefore counts as one eligible external judge
pass. No condition aggregate or decision exists, and this case cannot support
any public claim, canon candidate, or `benchmark_supported` status.

## Calibration gate

`judge-packet/calibration-anchors.md` is `status: filled_pre_run`. The
agent-drafted anchors were operator-reviewed and accepted as written before the
v4-v1 run packet froze.

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

None yet. The OpenAI API receipt scores `OUT-NN` labels only; no condition
aggregate has been computed or committed. The planned signal is comparative:
`substrate_workflow` must separate from `vanilla_long_prompt` and
`generic_advice_prompted` on both total score and the C3/C4/C5/C6 critical
criteria, under at least two eligible external blind judges. The full
pre-registered rule is in `case.md` -> `## Positive result`.

## Judge Notes

2026-05-23: Hosted OpenAI `gpt-5.4-mini` (`gpt-5.4-mini-2026-03-17`) passed the
calibration gate exactly (A 6/6, B 0/6, C 4/6; 0 criteria differences; no Anchor
C C5/C6 disagreement) and scored all forty blinded `OUT-NN` outputs via the
OpenAI API. Score distribution: 6/6 x38, 5/6 x2. Receipt:
`judge-packet/judge-score-openai-gpt-5.4-mini-api.md`.

Route-eligibility decision: this was a real hosted API model run operated by the
orchestrating Codex session using an operator-provided API key. On 2026-05-23,
the operator accepted hosted API judge paths run this way as result-lifting
judges for v4, provided blinding, calibration, and honest route recording are
preserved. The OpenAI receipt therefore counts as one eligible external judge
pass. No condition reconciliation has occurred.

## Follow-up

1. Collect at least one more eligible external judge score from a different
   provider/family.
2. Reconcile aggregate-only after blind scoring completes.
3. Record the positive-result decision or `do_not_promote` outcome.

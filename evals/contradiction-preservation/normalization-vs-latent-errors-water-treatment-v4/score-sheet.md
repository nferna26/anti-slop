---
case_id: normalization-vs-latent-errors-water-treatment-v4
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score only against `case.md` -> `## Scoring rubric`. Do not score from source
prestige, source names, model fluency, or a preferred operational answer. A
model output is a test artifact, not an authority.

## Result

partial - v4 frozen run complete, two eligible external API judge receipts
recorded, aggregate-only reconciliation complete, and `do_not_promote` recorded
in `eval-decision.md`. `run-packet.md` freezes the v4-v1 condition packets,
equal-length filler, generator/runtime snapshot, and external judge routes;
forty real `gemma4:31b` model outputs exist and a condition-blind judge packet
is built. Hosted OpenAI `gpt-5.4-mini` and hosted Anthropic `claude-opus-4-7`
both passed calibration exactly and scored all forty `OUT-NN` outputs. The
operator accepted hosted API calls run by Codex with operator-provided keys as
result-lifting judge routes for v4 when the judge remains condition-blind,
passes calibration, and the receipt records the route honestly. The
pre-registered Positive-result rule is not met: controls match or nearly match
the substrate under both judges, and C3/C4 saturate across controls. This case
cannot support any public claim, canon candidate, or `benchmark_supported`
status.

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

Operator-only. Filled after both eligible blind judges scored all forty outputs.
The `OUT-NN` to condition mapping was reconstructed aggregate-only from
committed hashes: `judge-packet/output-manifest.yaml` `output_sha256` values
joined to the committed model-output receipt bodies and their `model_condition`
frontmatter. All forty rows matched. The local-only answer key was not read.

| Judge | Condition | n | Mean total | C3 pass | C4 pass | C5 pass | C6 pass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenAI gpt-5.4-mini | `vanilla` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| OpenAI gpt-5.4-mini | `famous_sources_supplied` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| OpenAI gpt-5.4-mini | `substrate_workflow` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| OpenAI gpt-5.4-mini | `vanilla_long_prompt` | 8 | 5.875 | 1.00 | 1.00 | 1.00 | 0.88 |
| OpenAI gpt-5.4-mini | `generic_advice_prompted` | 8 | 5.875 | 1.00 | 1.00 | 1.00 | 0.88 |
| Anthropic claude-opus-4-7 | `vanilla` | 8 | 5.500 | 1.00 | 1.00 | 0.75 | 0.75 |
| Anthropic claude-opus-4-7 | `famous_sources_supplied` | 8 | 4.250 | 1.00 | 1.00 | 0.12 | 0.12 |
| Anthropic claude-opus-4-7 | `substrate_workflow` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| Anthropic claude-opus-4-7 | `vanilla_long_prompt` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| Anthropic claude-opus-4-7 | `generic_advice_prompted` | 8 | 5.750 | 1.00 | 1.00 | 0.88 | 0.88 |

Do not commit a per-`OUT-NN` to condition mapping. Commit aggregate tables only.

## Comparative signal

The reconciled signal is non-promotional. Under OpenAI `gpt-5.4-mini`,
`substrate_workflow` reaches a 6.000 mean, but `vanilla` and
`famous_sources_supplied` also reach 6.000 and both long-prompt controls reach
5.875. The substrate margin is +0.125 over `vanilla_long_prompt`, +0.125 over
`generic_advice_prompted`, +0.000 over `famous_sources_supplied`, and +0.000
over `vanilla`, far below the pre-registered bars.

Under Anthropic `claude-opus-4-7`, `substrate_workflow` reaches 6.000, but
`vanilla_long_prompt` also reaches 6.000 and `generic_advice_prompted` reaches
5.750. The substrate margin is +0.000 over `vanilla_long_prompt`, +0.250 over
`generic_advice_prompted`, +1.750 over `famous_sources_supplied`, and +0.500
over `vanilla`. The judge-level stability rule is therefore not met.

Across both eligible judges, C3 and C4 are saturated at 1.00 for the substrate,
`vanilla_long_prompt`, and `generic_advice_prompted`, so the substrate cannot
clear the required critical-criterion margins. The case is recorded as
`do_not_promote`.

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
pass.

2026-05-23: Hosted Anthropic `claude-opus-4-7` passed the calibration gate
exactly (A 6/6, B 0/6, C 4/6; 0 criteria differences; no Anchor C C5/C6
disagreement) and scored all forty blinded `OUT-NN` outputs via the Anthropic
API. Score distribution: 6/6 x30, 4/6 x10. Receipt:
`judge-packet/judge-score-anthropic-claude-opus-4-7-api.md`.

The Anthropic receipt is a real hosted API model run operated by the
orchestrating Codex session using an operator-provided API key. Under the
2026-05-23 operator route-eligibility decision, it counts as the second eligible
external judge pass for v4, from a different provider/family than OpenAI.

2026-05-23: Aggregate-only reconciliation was completed from committed hashes.
No per-`OUT-NN` to condition mapping is committed. The pre-registered Positive
result rule is not met; `eval-decision.md` records `do_not_promote`.

## Follow-up

1. Treat v4-v1 as a reconciled negative learning result, not a benchmark win.
2. Carry the control-saturation finding into any future v5 design.
3. Do not cite v4 as evidence that the substrate improves advice.

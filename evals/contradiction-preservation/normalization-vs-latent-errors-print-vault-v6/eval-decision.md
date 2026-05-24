---
case_id: normalization-vs-latent-errors-print-vault-v6
benchmark_version: normalization-vs-latent-errors-print-vault-v6-v1
artifact: eval-decision
eval_decision: do_not_promote
decision_class: insufficient_external_judges
result_status: partial
decision_date: 2026-05-23
decision_summary: The pre-registered Positive-result rule is not met: one eligible scored judge and generic-advice C3/C4 saturation; the case stays partial and must not be cited as benchmark-supported.
---

# Eval Decision - normalization-vs-latent-errors-print-vault-v6

Public-safe decision record for the eval case in this folder. It sits on top of
score-sheet.md -> ## Result and does not replace the Result status.

## Status

Result is `partial`. The case has forty real generator outputs, hosted API
judge receipts, and aggregate-only reconciliation from committed hashes for the
eligible scored judge receipt(s). OpenAI failed calibration and scored zero real
outputs. Anthropic scored all forty blinded outputs after passing calibration.

## Decision

`eval_decision: do_not_promote`.

## Reason

The v6 run followed the frozen run packet: operator-filled calibration anchors,
five pre-registered conditions, eight real local generator runs per condition,
condition-blind anonymisation by output-body hash, hosted OpenAI and Anthropic
API judge routes, calibration before scoring, and aggregate-only reconciliation.

Positive-rule clauses:

- run_completeness: `True`
- external_judges: `False`
- calibration: `True`
- total_score_margin: `True`
- critical_criterion_margin: `False`
- judge_level_stability: `True`
- no_unresolved_judge_trigger: `True`
- no_critical_saturation: `False`

Pooled total-score margins:

- substrate minus `vanilla_long_prompt`: +3.500
- substrate minus `generic_advice_prompted`: +1.000
- substrate minus `famous_sources_supplied`: +1.250
- substrate minus `vanilla`: +1.625

Critical saturation guard values:

- vanilla_long_prompt_C3: 0.12
- vanilla_long_prompt_C4: 0.50
- generic_advice_prompted_C3: 1.00
- generic_advice_prompted_C4: 1.00

Interpretation: v6 did move the total-score margin against
`generic_advice_prompted` from the v5 tie to +1.000, but the generic condition
still saturated C3/C4 under the eligible scored judge. The design did not yet
make generic practical advice insufficient at the mechanism-inference layer.

Judge disagreement trigger:

```json
{
  "triggered": false,
  "reason": "not evaluated because fewer than two scored eligible judges"
}
```

## Reconciliation method

The OUT-NN to condition mapping was reconstructed from committed hashes only.
judge-packet/output-manifest.yaml carries the output_sha256 of each OUT-NN. The
committed model-outputs receipts carry the output body and model_condition
frontmatter; the body sha256 equals the manifest value. Joining on that hash
matched all forty rows, eight per condition. The local-only answer key was not
read for this reconciliation.

No per-OUT-NN to condition mapping is committed. Only aggregate condition
statistics are recorded in score-sheet.md.

## Discipline note

A model output is a test artifact - never an authority, never citable as a
source. A judge score is likewise a test artifact: it is evidence about how one
judge scored one set of answers under one rubric, not evidence about the world
and not an advice claim.

---
case_id: halo-evidence-vs-diagnosis-validation-v9
benchmark_version: halo-evidence-vs-diagnosis-validation-v9-v1
artifact: eval-decision
eval_decision: do_not_promote
decision_class: controls_matched_total_margin
result_status: partial
decision_date: 2026-05-24
decision_summary: The pre-registered Positive-result rule is not met (controls_matched_total_margin); the case stays partial and must not be cited as benchmark-supported.
---

# Eval Decision - halo-evidence-vs-diagnosis-validation-v9

Public-safe decision record for the eval case in this folder. It sits on top of
score-sheet.md -> ## Result and does not replace the Result status.

## Status

Result is `partial`. The case has 48 real generator outputs, hosted API
judge receipts, and aggregate-only reconciliation from committed hashes for the
eligible scored judge receipt(s). Hosted OpenAI and hosted Anthropic both
passed the smoke-2 C3-C6 eligibility gate before generation and scored all
48 blinded outputs.

## Decision

`eval_decision: do_not_promote`.

## Reason

The v9 run followed the frozen run packet: smoke-2 calibration anchors, six
pre-registered conditions, eight real local generator runs per condition,
condition-blind anonymisation by output-body hash, hosted OpenAI and Anthropic
API judge routes that had passed the pre-generation C3-C6 smoke gate, and
aggregate-only reconciliation.

Positive-rule clauses:

- run_completeness: `True`
- external_judges: `True`
- calibration: `True`
- total_score_margin: `False`
- critical_criterion_margin: `False`
- judge_level_stability: `False`
- discriminating_judges: `False`
- no_unresolved_judge_trigger: `True`
- no_critical_saturation: `False`

Pooled total-score margins:

- substrate minus `vanilla_long_prompt`: +0.000
- substrate minus `generic_advice_prompted`: +0.000
- substrate minus `criteria_prompted_no_sources`: +0.000
- substrate minus `famous_sources_supplied`: +0.000
- substrate minus `vanilla`: +0.000

Critical saturation guard values:

- vanilla_long_prompt_C3: 1.00
- vanilla_long_prompt_C4: 0.00
- vanilla_long_prompt_C5: 0.00
- vanilla_long_prompt_C6: 0.00
- generic_advice_prompted_C3: 1.00
- generic_advice_prompted_C4: 0.00
- generic_advice_prompted_C5: 0.00
- generic_advice_prompted_C6: 0.00
- criteria_prompted_no_sources_C3: 1.00
- criteria_prompted_no_sources_C4: 0.00
- criteria_prompted_no_sources_C5: 0.00
- criteria_prompted_no_sources_C6: 0.00

Judge disagreement trigger:

```json
{
  "triggered": false,
  "rates": {
    "substrate_workflow": {
      "n": 8,
      "disagreements": 0,
      "rate": 0.0
    },
    "vanilla_long_prompt": {
      "n": 8,
      "disagreements": 0,
      "rate": 0.0
    },
    "generic_advice_prompted": {
      "n": 8,
      "disagreements": 0,
      "rate": 0.0
    },
    "criteria_prompted_no_sources": {
      "n": 8,
      "disagreements": 0,
      "rate": 0.0
    },
    "key_controls": {
      "n": 24,
      "disagreements": 0,
      "rate": 0.0
    }
  }
}
```

## Reconciliation method

The OUT-NN to condition mapping was reconstructed from committed hashes only.
judge-packet/output-manifest.yaml carries the output_sha256 of each OUT-NN. The
committed model-outputs receipts carry the output body and model_condition
frontmatter; the body sha256 equals the manifest value. Joining on that hash
matched all 48 rows, eight per condition. The local-only answer key was not
read for this reconciliation.

No per-OUT-NN to condition mapping is committed. Only aggregate condition
statistics are recorded in score-sheet.md.

## Discipline note

A model output is a test artifact - never an authority, never citable as a
source. A judge score is likewise a test artifact: it is evidence about how one
judge scored one set of answers under one rubric, not evidence about the world
and not an advice claim.

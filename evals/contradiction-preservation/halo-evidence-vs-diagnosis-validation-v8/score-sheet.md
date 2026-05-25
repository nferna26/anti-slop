---
case_id: halo-evidence-vs-diagnosis-validation-v8
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score only against case.md -> ## Scoring rubric. Do not score from source
prestige, source names, model fluency, or a preferred operational answer. A
model output is a test artifact, not an authority.

## Result

partial - v8 frozen run complete, hosted external API judge receipts recorded,
aggregate-only reconciliation complete for 2 scored eligible
judge receipt(s), and `do_not_promote` recorded in eval-decision.md. The
pre-registered Positive-result rule was applied exactly. No per-OUT-NN to
condition mapping is committed.

## Calibration gate

judge-packet/calibration-anchors.md is status: smoke_passed_pre_generation. The
smoke-2 anchors were filled and tested before generation; hosted OpenAI
gpt-5.4-mini and hosted Anthropic claude-opus-4-7 both passed the
C3-C6-only eligibility gate. Local gpt-oss:20b failed the smoke gate and scored
zero v8-v1 outputs.

## Blind judge scoring surface

Judge-facing rows used anonymised OUT-NN labels only. Condition labels, run
numbers, seeds, model-output receipt paths, and the answer key were withheld
until blind scoring completed.

## Dependency checks

- C5 requires C3 and C4.
- C6 requires C5.
- Parsed judge rows were checked for total-count consistency and dependency
  consistency before reconciliation.

## Post-reconciliation condition aggregate

Operator-only. Filled after both eligible blind judges scored all forty outputs.
The OUT-NN to condition mapping was reconstructed aggregate-only from committed
hashes: judge-packet/output-manifest.yaml output_sha256 values joined to the
committed model-output receipt bodies and their model_condition frontmatter. All
forty rows matched. The local-only answer key was not read.

| Judge | Condition | n | Mean total | C3 pass | C4 pass | C5 pass | C6 pass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenAI gpt-5.4-mini | `vanilla` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| OpenAI gpt-5.4-mini | `famous_sources_supplied` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| OpenAI gpt-5.4-mini | `substrate_workflow` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| OpenAI gpt-5.4-mini | `vanilla_long_prompt` | 8 | 5.500 | 0.88 | 1.00 | 0.88 | 0.88 |
| OpenAI gpt-5.4-mini | `generic_advice_prompted` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| Anthropic claude-opus-4-7 | `vanilla` | 8 | 5.750 | 1.00 | 1.00 | 0.88 | 0.88 |
| Anthropic claude-opus-4-7 | `famous_sources_supplied` | 8 | 4.875 | 1.00 | 0.88 | 0.50 | 0.50 |
| Anthropic claude-opus-4-7 | `substrate_workflow` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| Anthropic claude-opus-4-7 | `vanilla_long_prompt` | 8 | 4.750 | 1.00 | 1.00 | 0.38 | 0.38 |
| Anthropic claude-opus-4-7 | `generic_advice_prompted` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| Pooled eligible judges | `vanilla` | 16 | 5.875 | 1.00 | 1.00 | 0.94 | 0.94 |
| Pooled eligible judges | `famous_sources_supplied` | 16 | 5.438 | 1.00 | 0.94 | 0.75 | 0.75 |
| Pooled eligible judges | `substrate_workflow` | 16 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| Pooled eligible judges | `vanilla_long_prompt` | 16 | 5.125 | 0.94 | 1.00 | 0.62 | 0.62 |
| Pooled eligible judges | `generic_advice_prompted` | 16 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |

Do not commit a per-OUT-NN to condition mapping. Commit aggregate tables only.

## Comparative signal

Pooled total-score margins:

- substrate minus `vanilla_long_prompt`: +0.875
- substrate minus `generic_advice_prompted`: +0.000
- substrate minus `famous_sources_supplied`: +0.562
- substrate minus `vanilla`: +0.125

Positive-rule clauses:

- run_completeness: `True`
- external_judges: `True`
- calibration: `True`
- total_score_margin: `False`
- critical_criterion_margin: `False`
- judge_level_stability: `False`
- no_unresolved_judge_trigger: `False`
- no_critical_saturation: `False`

Critical saturation guard values:

- vanilla_long_prompt_C3: 0.94
- vanilla_long_prompt_C4: 1.00
- vanilla_long_prompt_C5: 0.62
- vanilla_long_prompt_C6: 0.62
- generic_advice_prompted_C3: 1.00
- generic_advice_prompted_C4: 1.00
- generic_advice_prompted_C5: 1.00
- generic_advice_prompted_C6: 1.00

Judge disagreement trigger:

```json
{
  "triggered": true,
  "rates": {
    "substrate_workflow": {
      "n": 8,
      "disagreements": 0,
      "rate": 0.0
    },
    "vanilla_long_prompt": {
      "n": 8,
      "disagreements": 5,
      "rate": 0.625
    },
    "generic_advice_prompted": {
      "n": 8,
      "disagreements": 0,
      "rate": 0.0
    },
    "key_controls": {
      "n": 16,
      "disagreements": 5,
      "rate": 0.3125
    }
  }
}
```

Decision class: `controls_matched_total_margin`. Result: `partial`.

## Judge Notes

2026-05-24: Hosted OpenAI gpt-5.4-mini passed the smoke-2 C3-C6 eligibility
gate before generation, scored all forty blinded OUT-NN outputs through the
OpenAI API, and is recorded in
judge-packet/judge-score-openai-gpt-5.4-mini-api.md.

2026-05-24: Hosted Anthropic claude-opus-4-7 passed the smoke-2 C3-C6
eligibility gate before generation, scored all forty blinded OUT-NN outputs
through the Anthropic API, and is recorded in
judge-packet/judge-score-anthropic-claude-opus-4-7-api.md.

2026-05-24: Aggregate-only reconciliation was completed from committed hashes.
No per-OUT-NN to condition mapping is committed.

## Follow-up

1. Treat v8-v1 according to eval-decision.md.
2. Do not cite this eval as benchmark-supported unless Result is
   benchmark_supported and eval-decision records support.
3. Keep raw transcripts, API metadata, and the answer key local-only.

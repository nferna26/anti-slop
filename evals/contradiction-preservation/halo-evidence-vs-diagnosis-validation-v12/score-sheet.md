---
case_id: halo-evidence-vs-diagnosis-validation-v12
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score only against case.md -> ## Scoring rubric. Do not score from source
prestige, source names, model fluency, or a preferred operational answer. A
model output is a test artifact, not an authority.

## Result

partial - v12 frozen run complete, three pre-registered judge receipts recorded,
aggregate-only reconciliation complete for 3 scored eligible
judge receipt(s), and `do_not_promote` recorded in eval-decision.md. The
pre-registered Positive-result rule was applied exactly. No per-OUT-NN to
condition mapping is committed.

## Calibration gate

judge-packet/calibration-anchors.md and
judge-packet/disagreement-smoke-answers.md were filled and tested before
generation. Hosted OpenAI gpt-5.4, hosted Anthropic
claude-opus-4-7, and local gpt-oss:20b all passed the C4-C6 calibration
gate and the pre-generation judge-disagreement smoke gate.

## Blind judge scoring surface

Judge-facing rows used anonymised OUT-NN labels only. Condition labels, run
numbers, seeds, model-output receipt paths, and the answer key were withheld
until blind scoring completed.

## Dependency checks

- C5 requires C4.
- C6 requires C5.
- Parsed judge rows were checked for total-count consistency and dependency
  consistency before reconciliation.

## Post-reconciliation condition aggregate

Operator-only. Filled after eligible blind judges scored all 48 outputs.
The OUT-NN to condition mapping was reconstructed aggregate-only from committed
hashes: judge-packet/output-manifest.yaml output_sha256 values joined to the
committed model-output receipt bodies and their model_condition frontmatter. All
48 rows matched. The local-only answer key was not read.

| Judge | Condition | n | Mean total | C3 pass | C4 pass | C5 pass | C6 pass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenAI gpt-5.4 | `vanilla` | 8 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| OpenAI gpt-5.4 | `famous_sources_supplied` | 8 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| OpenAI gpt-5.4 | `substrate_workflow` | 8 | 3.375 | 1.00 | 0.12 | 0.12 | 0.12 |
| OpenAI gpt-5.4 | `vanilla_long_prompt` | 8 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| OpenAI gpt-5.4 | `generic_advice_prompted` | 8 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| OpenAI gpt-5.4 | `criteria_prompted_no_sources` | 8 | 4.250 | 1.00 | 0.50 | 0.50 | 0.25 |
| Anthropic claude-opus-4-7 | `vanilla` | 8 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| Anthropic claude-opus-4-7 | `famous_sources_supplied` | 8 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| Anthropic claude-opus-4-7 | `substrate_workflow` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| Anthropic claude-opus-4-7 | `vanilla_long_prompt` | 8 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| Anthropic claude-opus-4-7 | `generic_advice_prompted` | 8 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| Anthropic claude-opus-4-7 | `criteria_prompted_no_sources` | 8 | 5.500 | 1.00 | 1.00 | 0.75 | 0.75 |
| Local gpt-oss:20b | `vanilla` | 8 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| Local gpt-oss:20b | `famous_sources_supplied` | 8 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| Local gpt-oss:20b | `substrate_workflow` | 8 | 5.625 | 1.00 | 0.88 | 0.88 | 0.88 |
| Local gpt-oss:20b | `vanilla_long_prompt` | 8 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| Local gpt-oss:20b | `generic_advice_prompted` | 8 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| Local gpt-oss:20b | `criteria_prompted_no_sources` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| Pooled eligible judges | `vanilla` | 24 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| Pooled eligible judges | `famous_sources_supplied` | 24 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| Pooled eligible judges | `substrate_workflow` | 24 | 5.000 | 1.00 | 0.67 | 0.67 | 0.67 |
| Pooled eligible judges | `vanilla_long_prompt` | 24 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| Pooled eligible judges | `generic_advice_prompted` | 24 | 3.000 | 1.00 | 0.00 | 0.00 | 0.00 |
| Pooled eligible judges | `criteria_prompted_no_sources` | 24 | 5.250 | 1.00 | 0.83 | 0.75 | 0.67 |

Do not commit a per-OUT-NN to condition mapping. Commit aggregate tables only.

## Comparative signal

Pooled total-score margins:

- substrate minus `vanilla_long_prompt`: +2.000
- substrate minus `generic_advice_prompted`: +2.000
- substrate minus `criteria_prompted_no_sources`: -0.250
- substrate minus `famous_sources_supplied`: +2.000
- substrate minus `vanilla`: +2.000

Positive-rule clauses:

- run_completeness: `True`
- substrate_feasibility_probe: `True`
- external_judges: `True`
- calibration: `True`
- total_score_margin: `False`
- critical_criterion_margin: `False`
- judge_level_stability: `False`
- discriminating_judges: `True`
- no_unresolved_judge_trigger: `False`
- no_critical_saturation: `True`

Critical saturation guard values:

- vanilla_long_prompt_C4: 0.00
- vanilla_long_prompt_C5: 0.00
- vanilla_long_prompt_C6: 0.00
- generic_advice_prompted_C4: 0.00
- generic_advice_prompted_C5: 0.00
- generic_advice_prompted_C6: 0.00
- criteria_prompted_no_sources_C4: 0.83
- criteria_prompted_no_sources_C5: 0.75
- criteria_prompted_no_sources_C6: 0.67

Judge disagreement trigger:

```json
{
  "triggered": true,
  "rates": {
    "substrate_workflow": {
      "n": 8,
      "disagreements": 7,
      "rate": 0.875
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
      "disagreements": 6,
      "rate": 0.75
    },
    "key_controls": {
      "n": 24,
      "disagreements": 6,
      "rate": 0.25
    }
  }
}
```

Decision class: `controls_matched_total_margin`. Result: `partial`.

## Judge Notes

2026-05-24: Hosted OpenAI gpt-5.4 passed the C4-C6 calibration and
judge-disagreement smoke gates before generation, scored all 48 blinded OUT-NN outputs through the
OpenAI API, and is recorded in
judge-packet/judge-score-openai-gpt-5.4-api.md.

2026-05-24: Hosted Anthropic claude-opus-4-7 passed the C4-C6
calibration and judge-disagreement smoke gates before generation, scored all 48 blinded OUT-NN outputs
through the Anthropic API, and is recorded in
judge-packet/judge-score-anthropic-claude-opus-4-7-api.md.

2026-05-24: Local gpt-oss:20b passed the C4-C6 calibration and
judge-disagreement smoke gates before generation, scored all 48
blinded OUT-NN outputs as the pre-registered third route, and is recorded in
judge-packet/judge-score-local-gpt-oss-20b.md.

2026-05-24: Aggregate-only reconciliation was completed from committed hashes.
No per-OUT-NN to condition mapping is committed.

## Follow-up

1. Treat v12-v1 according to eval-decision.md.
2. Do not cite this eval as benchmark-supported unless Result is
   benchmark_supported and eval-decision records support.
3. Keep raw transcripts, API metadata, and the answer key local-only.

---
case_id: normalization-vs-latent-errors-runway-lighting-v5
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score only against case.md -> ## Scoring rubric. Do not score from source
prestige, source names, model fluency, or a preferred operational answer. A
model output is a test artifact, not an authority.

## Result

partial - v5 frozen run complete, hosted external API judge receipts recorded,
aggregate-only reconciliation complete for 1 scored eligible
judge receipt(s), and `do_not_promote` recorded in eval-decision.md. The
pre-registered Positive-result rule was applied exactly. No per-OUT-NN to
condition mapping is committed.

## Calibration gate

judge-packet/calibration-anchors.md is status: filled_pre_run. The
agent-drafted anchors were operator-reviewed and accepted as written before the
v5-v1 run packet froze.

## Blind judge scoring surface

Judge-facing rows used anonymised OUT-NN labels only. Condition labels, run
numbers, seeds, model-output receipt paths, and the answer key were withheld
until blind scoring completed.

## Dependency checks

- C5 requires C3 and C4.
- C6 requires C5.
- Parsed judge rows were checked for dependency consistency and TOTAL
  arithmetic before reconciliation. One Anthropic row (`OUT-36`) reported
  `TOTAL=2` while its C1-C6 verdicts imply 3; the aggregate uses the rubric's
  PASS-count total and the correction is recorded in the Anthropic receipt.

## Post-reconciliation condition aggregate

Operator-only. Filled after the eligible scored blind-judge receipt was
recorded. The OUT-NN to condition mapping was reconstructed aggregate-only from committed
hashes: judge-packet/output-manifest.yaml output_sha256 values joined to the
committed model-output receipt bodies and their model_condition frontmatter. All
forty rows matched. The local-only answer key was not read.

| Judge | Condition | n | Mean total | C3 pass | C4 pass | C5 pass | C6 pass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Anthropic claude-opus-4-7 | `vanilla` | 8 | 5.375 | 0.88 | 1.00 | 0.75 | 0.75 |
| Anthropic claude-opus-4-7 | `famous_sources_supplied` | 8 | 5.625 | 1.00 | 0.88 | 0.88 | 0.88 |
| Anthropic claude-opus-4-7 | `substrate_workflow` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| Anthropic claude-opus-4-7 | `vanilla_long_prompt` | 8 | 1.125 | 0.12 | 0.00 | 0.00 | 0.00 |
| Anthropic claude-opus-4-7 | `generic_advice_prompted` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| Pooled eligible judges | `vanilla` | 8 | 5.375 | 0.88 | 1.00 | 0.75 | 0.75 |
| Pooled eligible judges | `famous_sources_supplied` | 8 | 5.625 | 1.00 | 0.88 | 0.88 | 0.88 |
| Pooled eligible judges | `substrate_workflow` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |
| Pooled eligible judges | `vanilla_long_prompt` | 8 | 1.125 | 0.12 | 0.00 | 0.00 | 0.00 |
| Pooled eligible judges | `generic_advice_prompted` | 8 | 6.000 | 1.00 | 1.00 | 1.00 | 1.00 |

Do not commit a per-OUT-NN to condition mapping. Commit aggregate tables only.

## Comparative signal

Pooled total-score margins:

- substrate minus `vanilla_long_prompt`: +4.875
- substrate minus `generic_advice_prompted`: +0.000
- substrate minus `famous_sources_supplied`: +0.375
- substrate minus `vanilla`: +0.625

Positive-rule clauses:

- run_completeness: `True`
- external_judges: `False`
- calibration: `True`
- total_score_margin: `False`
- critical_criterion_margin: `False`
- judge_level_stability: `False`
- no_unresolved_judge_trigger: `True`
- no_critical_saturation: `False`

Critical saturation guard values:

- vanilla_long_prompt_C3: 0.12
- vanilla_long_prompt_C4: 0.00
- generic_advice_prompted_C3: 1.00
- generic_advice_prompted_C4: 1.00

Judge disagreement trigger:

```json
{
  "triggered": false,
  "reason": "not evaluated because fewer than two scored eligible judges"
}
```

Decision class: `insufficient_external_judges`. Result: `partial`.

## Judge Notes

2026-05-23: Hosted OpenAI gpt-5.4-mini failed the calibration gate (7 criteria
differences and Anchor C C5/C6 disagreement), so it scored zero real outputs and
is recorded as calibration-only in
judge-packet/judge-calibration-openai-gpt-5.4-mini-api.md.

2026-05-23: Hosted Anthropic claude-opus-4-7 passed calibration, scored
all forty blinded OUT-NN outputs through the Anthropic API, and is recorded in
judge-packet/judge-score-anthropic-claude-opus-4-7-api.md.

2026-05-23: Aggregate-only reconciliation was completed from committed hashes.
No per-OUT-NN to condition mapping is committed.

## Follow-up

1. Treat v5-v1 according to eval-decision.md.
2. Do not cite this eval as benchmark-supported unless Result is
   benchmark_supported and eval-decision records support.
3. Keep raw transcripts, API metadata, and the answer key local-only.

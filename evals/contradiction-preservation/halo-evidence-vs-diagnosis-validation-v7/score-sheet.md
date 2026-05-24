---
case_id: halo-evidence-vs-diagnosis-validation-v7
eval_type: contradiction-preservation
scoring_status: unscored
---

# Score Sheet

Score only against case.md -> ## Scoring rubric. Do not score from source
prestige, source names, model fluency, or a preferred business answer. A model
output is a test artifact, not an authority.

## Result

partial - v7 frozen run complete, 40 real generator outputs recorded, blind
judge packet built, and all three pre-registered judge routes recorded as
calibration-only. No OUT-NN answers were scored because no judge passed the
stricter v7 calibration gate. `eval-decision.md` records `do_not_promote` /
`decision_class: judge_calibration_failed`.

## Calibration gate

judge-packet/calibration-anchors.md is `status: filled_pre_run`. The
agent-drafted anchors were filled before generation under the active v7
execution goal. The v7 gate requires exact C3-C6 agreement across all seven
anchors, at most one total C1/C2 difference, arithmetic totals, and no C5/C6
dependency violation.

| Judge route | Calibration differences | Critical C3-C6 differences | Noncritical C1/C2 differences | Dependency violations | Total mismatches | Eligible to score OUT-NN? | Receipt |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Hosted OpenAI `gpt-5.4-mini` | 6 | 1 | 5 | 0 | 0 | No | `judge-packet/judge-calibration-openai-gpt-5.4-mini-api.md` |
| Hosted Anthropic `claude-opus-4-7` | 5 | 0 | 5 | 0 | 0 | No | `judge-packet/judge-calibration-anthropic-claude-opus-4-7-api.md` |
| Local `gpt-oss:20b` | 6 | 1 | 5 | 0 | 0 | No | `judge-packet/judge-calibration-local-gpt-oss-20b.md` |

All failed judges score zero real outputs. No after-the-fact rescue route was
added.

## Blind judge scoring surface

The condition-blind judge packet was built after generation and before
calibration. Judge-facing rows used anonymised `OUT-NN` labels only. Condition
labels, run numbers, seeds, model-output receipt paths, and the local-only
answer key were withheld. Because every judge route failed calibration, no
judge received credit as an eligible scorer and no OUT-NN score table was
produced.

## Dependency checks

- C5 requires C3 and C4.
- C6 requires C5.
- Calibration rows were checked for dependency consistency and total-count
  consistency.
- No scored OUT-NN rows exist.

## Post-reconciliation condition aggregate

Not applicable. No eligible judge scored OUT-NN answers, so no aggregate-only
condition reconciliation was performed. The `OUT-NN` to condition answer key
remains local-only and uncommitted.

## Comparative signal

Not available. The generation machinery completed, but the judge layer failed
before scoring. This is a negative readiness result for v7's calibration design,
not evidence that any model condition performed better or worse.

Positive-rule clauses:

- run_completeness: `True`
- judge_route_pre_registration: `True`
- eligible_scored_judges: `False`
- calibration: `False`
- total_score_margin: `not_evaluated`
- critical_composite_margin: `not_evaluated`
- judge_level_stability: `not_evaluated`
- no_unresolved_judge_trigger: `not_evaluated`
- no_critical_saturation: `not_evaluated`

Decision class: `judge_calibration_failed`. Result: `partial`.

## Judge Notes

2026-05-24: Hosted OpenAI `gpt-5.4-mini` first returned an incomplete
calibration response at the original output cap. The calibration call was rerun
with a larger output cap and the same packet; it still failed the frozen v7
calibration gate with 6 total criteria differences, including 1 C3-C6
difference.

2026-05-24: Hosted Anthropic `claude-opus-4-7` failed the frozen v7 calibration
gate with 5 total criteria differences. It matched all C3-C6 anchor verdicts
but exceeded the allowed C1/C2 difference count.

2026-05-24: Local `gpt-oss:20b` failed the frozen v7 calibration gate with 6
total criteria differences, including 1 C3-C6 difference.

## Follow-up

1. Record v7-v1 according to `eval-decision.md`.
2. Do not cite this eval as benchmark-supported.
3. Keep raw API transcripts, local judge transcripts, and the answer key
   local-only.
4. Before any v8 run, redesign calibration anchors or eligibility thresholds
   in a new frozen version; do not rescore v7 with revised anchors.

---
case_id: locator-accuracy-v4
benchmark_version: locator-accuracy-v4-v1
artifact: judge-calibration
judge_route_id: hosted_anthropic
judge_model_id: claude-opus-4-7
judge_model_snapshot: claude-opus-4-7
judge_model_family: Claude / Anthropic
judge_provider: Anthropic API
judge_runtime: Anthropic Messages API via local-only script using operator-provided API key
generator_model_id: none
judge_status: exact calibration passed on anchors A-L before any OUT scoring
judge_independence: independent_of_the_generator_family
calibration_result: passed - 0 reference difference(s) across 12 anchors, 0 F1/F3 mutual-exclusion violation(s)
outputs_scored: 0
judge_date: 2026-05-29
condition_blinded: true
result_status: partial
note: Calibration-only receipt. Anthropic Claude is a different family from the Gemma generator. The route matched the withheld reference key exactly on all twelve anchors, including the canon-refusal boundary K (decline canon = SO3) vs L (assert/apply rule = SO0).
---

# Hosted Anthropic Judge Calibration - claude-opus-4-7

Public-safe calibration-only receipt for `locator-accuracy-v4-v1`. The route was
given only the condition-blind judge-facing Surface 1 packet (judge-instructions,
case-context, rubric, calibration-exercise anchors A-L); the operator-only
Surface 2 reference key was withheld.

## Judge Identity And Independence

- Judge model: `claude-opus-4-7`, Claude / Anthropic.
- Provider / runtime: Anthropic Messages API via a local-only script using an
  operator-provided API key; key values, paths, and `.env` contents are never
  committed.
- API settings: no `temperature` parameter (deprecated for this model); model
  default; `max_tokens` 6000.
- Response ID: `msg_018ZwwPnH6BQjQfh8rk7TfuL`.
- Calibration prompt sha256:
  `2dc4c76380a47c51a947483955fd7ea5cd634761f482e8e203a15966a8f63d14`.
- Raw response sha256:
  `d1be79f455f979e4305003d87124acbb8ea49481ce2ac85b10316d6080cbd151`.
  Raw transcripts remain local-only and are not committed.
- Parsed text sha256:
  `a9e6f1e3b0a440b3f569fceab9c761d45fc6498edfa15902a4e9ea1e42681b9b`.

## Result

The route returned all twelve anchor verdicts (A-L) in the required format and
matched the withheld Surface 2 reference key **exactly** on every F1-F5 flag and
the single SO category for all twelve anchors, with no F1/F3 mutual-exclusion
violation. This includes the SO1/SO2/SO3 distinctions, the
correct-card/incomplete-locator SO2 case (I), the fabricated-card F1 case (J),
and the v4 canon-refusal boundary — anchor K (card-citing correction that
declines the canon move) = SO3 (F4=0, F5=0) and anchor L (card-citing correction
that asserts/applies a standing rule) = SO0 (F4=1, F5=1).

`calibration_result: passed`. The route is eligible to score the condition-blind
OUT-NN packet. Per-anchor reference verdicts are operator-only and are not
reproduced here.

## Boundary

A judge score is evidence about scoring behavior under a frozen rubric, not
evidence about the world. This receipt promotes no source card, claim/tension
card, canon candidate, or Result.

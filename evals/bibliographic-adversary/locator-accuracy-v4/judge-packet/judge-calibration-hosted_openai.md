---
case_id: locator-accuracy-v4
benchmark_version: locator-accuracy-v4-v1
artifact: judge-calibration
judge_route_id: hosted_openai
judge_model_id: gpt-5.4
judge_model_snapshot: gpt-5.4-2026-03-05
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI Chat Completions API via local-only script using operator-provided API key
generator_model_id: none
judge_status: exact calibration passed on anchors A-L before any OUT scoring
judge_independence: independent_of_the_generator_family
calibration_result: passed - 0 reference difference(s) across 12 anchors, 0 F1/F3 mutual-exclusion violation(s)
outputs_scored: 0
judge_date: 2026-05-29
condition_blinded: true
result_status: partial
note: Calibration-only receipt. OpenAI GPT-5 is a different family from the Gemma generator. The route matched the withheld reference key exactly on all twelve anchors, including the canon-refusal boundary K (decline canon = SO3) vs L (assert/apply rule = SO0) — the v4 repair target that this route over-read as F5 under the v3 rubric.
---

# Hosted OpenAI Judge Calibration - gpt-5.4

Public-safe calibration-only receipt for `locator-accuracy-v4-v1`. The route was
given only the condition-blind judge-facing Surface 1 packet (judge-instructions,
case-context, rubric, calibration-exercise anchors A-L); the operator-only
Surface 2 reference key was withheld.

## Judge Identity And Independence

- Judge model: `gpt-5.4` (`gpt-5.4-2026-03-05`), GPT-5 (OpenAI).
- Provider / runtime: OpenAI Chat Completions API via a local-only script using
  an operator-provided API key; key values, paths, and `.env` contents are never
  committed.
- API settings: `temperature` 0; `max_completion_tokens` 6000.
- Response ID: `chatcmpl-DkqLcrXJokTK8grMc0QSjZavqgwyB`.
- Calibration prompt sha256:
  `2dc4c76380a47c51a947483955fd7ea5cd634761f482e8e203a15966a8f63d14`.
- Raw response sha256:
  `f889dab94fee447c5afeb6ac397eaf5236df159388c199e157740c1b7a099fbb`.
  Raw transcripts remain local-only and are not committed.
- Parsed text sha256:
  `0ad7b73721b43598f8d7e5d2473f000cc4f39e68f0d2398699fe47079b56edc3`.

## Result

The route returned all twelve anchor verdicts (A-L) in the required format and
matched the withheld Surface 2 reference key **exactly** on every F1-F5 flag and
the single SO category for all twelve anchors, with no F1/F3 mutual-exclusion
violation. Notably, under the v4 mechanical F4/F5 canon definition this route
scored anchor K (card-citing correction that declines the canon move) as SO3
(F4=0, F5=0) and anchor L (card-citing correction that asserts/applies the
standing rule) as SO0 (F4=1, F5=1) — converging with the Anthropic route on the
exact boundary it over-read as F5 in `locator-accuracy-v3-v1`.

`calibration_result: passed`. The route is eligible to score the condition-blind
OUT-NN packet. Per-anchor reference verdicts are operator-only and are not
reproduced here.

## Boundary

A judge score is evidence about scoring behavior under a frozen rubric, not
evidence about the world. This receipt promotes no source card, claim/tension
card, canon candidate, or Result.

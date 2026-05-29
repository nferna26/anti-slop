---
case_id: locator-accuracy-v3
benchmark_version: locator-accuracy-v3-v1
artifact: judge-calibration
judge_route_id: hosted_anthropic
judge_model_id: claude-opus-4-7
judge_model_snapshot: claude-opus-4-7
judge_model_family: Claude / Anthropic
judge_provider: Anthropic API
judge_runtime: Anthropic Messages API via local-only script using operator-provided API key
generator_model_id: none
judge_status: exact calibration passed on anchors A-J before any OUT scoring
judge_independence: independent_of_the_generator_family
calibration_result: passed - 0 reference difference(s) across 10 anchors, 0 F1/F3 mutual-exclusion violation(s)
outputs_scored: 0
judge_date: 2026-05-29
condition_blinded: true
result_status: partial
note: Calibration-only receipt. No benchmark outputs were generated or scored at calibration time; no OUT-NN to condition mapping exists. Anthropic Claude is a different family from the Gemma generator, so it is an eligible independent judge.
---

# Hosted Anthropic Judge Calibration - claude-opus-4-7

Public-safe calibration-only receipt for `locator-accuracy-v3-v1`. It records
the hosted Anthropic route's exact anchor-scoring pass on the frozen
condition-blind Surface 1 calibration packet. It is not a Result lift, not
condition reconciliation, and not benchmark promotion.

## Judge Identity And Independence

- Judge model: `claude-opus-4-7`, Claude / Anthropic.
- Provider / runtime: Anthropic Messages API via a local-only script using an
  operator-provided API key; key values, paths, and `.env` contents are never
  committed.
- API settings: no `temperature` parameter (deprecated for this model; model
  default used); `max_tokens` 6000.
- Response ID: `msg_01GcWVMbm9XB2HtGRb9a2QXq`.
- Calibration prompt sha256:
  `7f7cca9368d44d8ac2c728722c2a869e81f5b759ac8907b6f7662246435fe39b`.
- Raw response sha256:
  `352633a016d9753fdfc960e3081bee43aec8c3212612e5f14f85d62864904c3c`.
  Raw transcripts remain local-only and are not committed.
- Parsed text sha256:
  `cd3459420105882d488838711992e202bdf620bc06fe876c347b20b7145c6b0c`.
- Generator family is Gemma; this Claude route is a different family and so is
  eligible as an independent judge.

## Calibration Packet

The route was given only the condition-blind judge-facing Surface 1 packet:
`judge-instructions.md`, `case-context.md`, `rubric.md`, and
`calibration-exercise.md` (anchors A-J). The operator-only Surface 2 reference
key in `calibration-anchors.md` was withheld.

## Result

The route returned all ten anchor verdicts (A-J) in the required format and
matched the withheld Surface 2 reference key **exactly** on every F1-F5 flag and
on the single SO category for all ten anchors, with no F1/F3 mutual-exclusion
violation. This includes the SO1 vs SO2 vs SO3 distinctions, the
correct-card/incomplete-locator SO2 case (Anchor I), the fabricated-card F1 case
(Anchor J), and the SO0 unsafe-support cases.

`calibration_result: passed`. The route is eligible to score the condition-blind
OUT-NN packet. Per-anchor reference verdicts are operator-only and are not
reproduced here.

## Boundary

A judge score is evidence about scoring behavior under a frozen rubric, not
evidence about the world and not an advice claim. This receipt promotes no
source card, claim/tension card, canon candidate, or Result.

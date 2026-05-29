---
case_id: locator-accuracy-v3
benchmark_version: locator-accuracy-v3-v1
artifact: calibration-decision
eval_decision: calibration_passed_generation_authorized
decision_class: two_different_family_routes_passed_exact_calibration
decision_date: 2026-05-29
result_status: partial
scoring_status: unscored
outputs_generated: 0
outputs_scored: 0
canon_supported: false
---

# Calibration Decision - locator-accuracy-v3-v1

## Verdict

The pre-registered calibration gate cleared. Two eligible, different-family,
condition-blind hosted routes matched the withheld Surface 2 reference key
**exactly** on all ten anchors (A-J), on every F1-F5 flag and the single SO
category, with no F1/F3 mutual-exclusion violation.

| Route | Model snapshot | Family | Exact match (A-J) | Eligible |
| --- | --- | --- | --- | --- |
| `hosted_anthropic` | `claude-opus-4-7` | Claude / Anthropic | yes (10/10) | yes |
| `hosted_openai` | `gpt-5.4-2026-03-05` | GPT-5 (OpenAI) | yes (10/10) | yes |

Receipts: `judge-packet/judge-calibration-hosted_anthropic.md`,
`judge-packet/judge-calibration-hosted_openai.md`.

The generator family is Gemma (`gemma-4-31b-it-mlx`); both judge routes are
different families, so the two-eligible-different-family requirement is met. The
calibration set exercises SO1 vs SO2 vs SO3 discrimination, the
correct-card/incomplete-locator SO2 case (Anchor I), the fabricated-card F1 case
(Anchor J), and the SO0 unsafe-support cases.

## Decision

`calibration_passed_generation_authorized`. Benchmark generation may proceed
from the frozen packet in `run-packet.md`, followed by anonymisation, eligible
blind judging by these two routes, and aggregate-only reconciliation.

This is a calibration-stage decision only. It is not a substrate-performance
result, not benchmark promotion, and not canon support. The frozen positive rule
in `case.md` is applied only after blind scoring, without revision.

## Discipline

Judges were given only the condition-blind Surface 1 judge-facing packet; the
Surface 2 reference key and `run-packet.md` were withheld. Raw API transcripts
and credentials stay local-only. No benchmark outputs exist yet, no OUT-NN
packet exists, no scoring has occurred, and no Result is lifted.

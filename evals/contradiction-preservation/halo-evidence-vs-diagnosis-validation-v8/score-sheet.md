---
case_id: halo-evidence-vs-diagnosis-validation-v8
eval_type: contradiction-preservation
scoring_status: calibration_smoke_passed
---

# Score Sheet

Score only against `case.md` -> `## Scoring rubric`. A model output is a test
artifact, not an authority. During the calibration-smoke phase, this sheet
records judge-route calibration readiness only; no v8 model outputs exist.

## Result

partial - calibration-smoke gate passed for two different-family hosted judge
routes before generation. Hosted OpenAI `gpt-5.4-mini` and hosted Anthropic
`claude-opus-4-7` matched C3-C6 exactly on eligibility anchors A-G; local
`gpt-oss:20b` failed on one C3-C6 eligibility criterion. No v8 condition packet
is frozen, no model output has been generated, no OUT-NN packet exists, and no
benchmark result can be claimed.

## Calibration-Smoke Gate

The v8 smoke gate is intentionally narrower than v7:

- C1/C2 are scored for information but excluded from judge eligibility.
- C3-C6 must match exactly across eligibility anchors A-G.
- Anchor H is illustrative-only and excluded from exact-match eligibility.
- C5/C6 dependency rules and arithmetic totals still apply.
- At least two different-family judge routes must pass before any v8 generation
  freeze.

| Judge route | Calibration differences | Critical C3-C6 differences on eligibility anchors | C1/C2 differences | Dependency violations | Total mismatches | Smoke eligible? | Receipt |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Hosted OpenAI `gpt-5.4-mini` | 1 | 0 | 0 | 0 | 0 | Yes | `judge-packet/judge-calibration-smoke-openai-gpt-5.4-mini.md` |
| Hosted Anthropic `claude-opus-4-7` | 0 | 0 | 0 | 0 | 0 | Yes | `judge-packet/judge-calibration-smoke-anthropic-claude-opus-4-7.md` |
| Local `gpt-oss:20b` | 1 | 1 | 0 | 0 | 0 | No | `judge-packet/judge-calibration-smoke-local-gpt-oss-20b.md` |

## Blind Judge Scoring Surface

Not applicable yet. No v8 model outputs have been generated and no OUT-NN judge
packet exists. The current judge packet contains calibration-smoke material
only.

## Dependency Checks

- C5 requires C3 and C4.
- C6 requires C5.
- C1/C2 are independent and do not gate judge eligibility.

## Post-Reconciliation Condition Aggregate

Not applicable. No eligible judge has scored model outputs, and no
aggregate-only reconciliation has been performed.

## Comparative Signal

Not available. This is a calibration-smoke readiness pass, not a comparative
benchmark result. The gate result means v8 may proceed to a future
freeze/generation step without repeating v7's judge-readiness failure.

## Follow-Up

The next step is to freeze v8 condition packets and only then generate real
model outputs. The smoke result itself must not be promoted as
`benchmark_supported`.

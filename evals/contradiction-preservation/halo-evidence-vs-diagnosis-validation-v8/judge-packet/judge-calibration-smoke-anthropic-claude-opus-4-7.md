---
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-smoke-2
artifact: judge-calibration-smoke
judge_model_id: claude-opus-4-7
judge_model_snapshot: claude-opus-4-7
judge_model_family: Claude Opus (Anthropic)
judge_provider: Anthropic API
judge_runtime: Anthropic API via Codex local-only script using operator-provided API key
judge_status: calibration-smoke only - no v8 outputs exist
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered smoke route
calibration_result: passed - 0 C3-C6 eligibility differences, 0 C1/C2 differences, dependency_violations=0, total_mismatches=0
outputs_scored: 0
judge_date: 2026-05-24
condition_blinded: true
result_status: calibration_smoke
smoke_eligible: true
note: Pre-registered judge route completed v8 calibration smoke only; no OUT-NN answers exist or were scored.
---

# Anthropic API Judge Calibration Smoke Receipt - claude-opus-4-7

This is a condition-blind calibration-smoke receipt for
`halo-evidence-vs-diagnosis-validation-v8`, benchmark version `halo-evidence-vs-diagnosis-validation-v8-smoke-2`. It records calibration
C1-C6 scores only. It is not a Result lift, not a condition reconciliation, and
not benchmark promotion.

## Judge identity and independence

- Judge model: `claude-opus-4-7` (`claude-opus-4-7`), Claude Opus (Anthropic).
- Provider / runtime: Anthropic API via Codex local-only script using operator-provided API key.
- API settings: no explicit temperature parameter; max_tokens 4000 calibration.
- Response ID: calibration `msg_01T6QGp824Fv77fCdeEKtCZF`.
- Input packet sha256: `12c5d225c1b66460ffab97a6bc300edfe522982c59cd5dd9c5bbbfda212575bb`.
- Raw output sha256: `5678adbb1dae9b737208d3eba97a4b009a073c37ab2e5dcd5a7d9fbfa7d144db`. Raw transcripts remain local-only and are not committed.
- Condition-blind: the judge received only the independent calibration-smoke
  packet. It did not receive model outputs, source condition labels, an answer
  key, or Surface 2 reference verdicts before calibration.

## Calibration Rows

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
[ANCHOR-D] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-E] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
[ANCHOR-F] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-G] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-H] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
```

Against the withheld reference:

- C3-C6 eligibility differences: 0
- C1/C2 differences: 0 (recorded, non-gating)
- Critical differences including illustrative Anchor H: 0
- Illustrative-only Anchor H differences: 0
- Dependency violations: 0
- Total mismatches: 0
- Smoke eligibility: `True`

Dependency violations: `[]`.
Total mismatches: `[]`.

## Method

The calibration anchors were scored against the six frozen-smoke criteria
C1-C6, with the dependency rule applied. C1/C2 differences are recorded but do
not affect smoke eligibility. Anchor H is illustrative-only and excluded from
exact-match eligibility. No v8 OUT-NN scoring packet exists.

## What this receipt is not

This is one calibration-smoke receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. A future generation pass still requires a
separate freeze, real outputs, blind scoring, aggregate-only reconciliation, and
application of the positive rule and falsifier.

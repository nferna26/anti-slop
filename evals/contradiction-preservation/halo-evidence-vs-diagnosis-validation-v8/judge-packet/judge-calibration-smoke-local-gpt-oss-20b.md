---
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-smoke-2
artifact: judge-calibration-smoke
judge_model_id: gpt-oss:20b
judge_model_snapshot: Ollama model ID 17052f91a42e
judge_model_family: gpt-oss local model
judge_provider: local Ollama
judge_runtime: local Ollama HTTP API via Codex local-only script; non-generator third-family backstop
judge_status: calibration-smoke only - no v8 outputs exist
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered smoke route
calibration_result: failed - 1 C3-C6 eligibility differences, 0 C1/C2 differences, dependency_violations=0, total_mismatches=0
outputs_scored: 0
judge_date: 2026-05-24
condition_blinded: true
result_status: calibration_smoke
smoke_eligible: false
note: Pre-registered judge route completed v8 calibration smoke only; no OUT-NN answers exist or were scored.
---

# Local Judge Calibration Smoke Receipt - gpt-oss:20b

This is a condition-blind calibration-smoke receipt for
`halo-evidence-vs-diagnosis-validation-v8`, benchmark version `halo-evidence-vs-diagnosis-validation-v8-smoke-2`. It records calibration
C1-C6 scores only. It is not a Result lift, not a condition reconciliation, and
not benchmark promotion.

## Judge identity and independence

- Judge model: `gpt-oss:20b` (`Ollama model ID 17052f91a42e`), gpt-oss local model.
- Provider / runtime: local Ollama HTTP API via Codex local-only script; non-generator third-family backstop.
- API settings: temperature 0.0, top_p 1.0, num_ctx 32768, fixed seed.
- Response ID: calibration ``.
- Input packet sha256: `12c5d225c1b66460ffab97a6bc300edfe522982c59cd5dd9c5bbbfda212575bb`.
- Raw output sha256: `076c35330c0e4a9e77ac7e1f18eefba8ee54daab967dcad60d2ecabfb00faabc`. Raw transcripts remain local-only and are not committed.
- Condition-blind: the judge received only the independent calibration-smoke
  packet. It did not receive model outputs, source condition labels, an answer
  key, or Surface 2 reference verdicts before calibration.

## Calibration Rows

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
[ANCHOR-D] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-E] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=FAIL TOTAL=5
[ANCHOR-F] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-G] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-H] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
```

Against the withheld reference:

- C3-C6 eligibility differences: 1
- C1/C2 differences: 0 (recorded, non-gating)
- Critical differences including illustrative Anchor H: 1
- Illustrative-only Anchor H differences: 0
- Dependency violations: 0
- Total mismatches: 0
- Smoke eligibility: `False`

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

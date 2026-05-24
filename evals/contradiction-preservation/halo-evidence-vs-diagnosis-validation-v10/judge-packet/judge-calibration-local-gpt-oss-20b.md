---
case_id: halo-evidence-vs-diagnosis-validation-v10
benchmark_version: halo-evidence-vs-diagnosis-validation-v10-v1
artifact: judge-calibration
judge_model_id: gpt-oss:20b
judge_model_snapshot: Ollama model ID 17052f91a42e
judge_model_family: gpt-oss local model
judge_provider: local Ollama
judge_runtime: local Ollama HTTP API via Codex local-only script; non-generator third-family backstop
generator_model_id: gemma-4-31b-it-mlx:2
judge_status: calibration-only judge receipt - incomplete calibration surface; not eligible to score real outputs
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered judge route; failed v10 smoke before generation
calibration_result: failed - returned anchors A-G only; missing illustrative Anchor H required by the calibration packet
outputs_scored: 0
judge_date: 2026-05-24
condition_blinded: true
result_status: partial
note: Pre-registered local backstop route attempted v10 calibration but did not return the full requested eight-line surface. No OUT-NN outputs were scored by this route.
---

# Local Calibration Receipt - gpt-oss:20b

This is a calibration-only receipt for the pre-registered local backstop judge
route in `halo-evidence-vs-diagnosis-validation-v10-v1`. It is not a score
receipt and contributes zero scored outputs.

## Calibration

The local judge returned seven anchor rows:

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
[ANCHOR-D] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-E] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
[ANCHOR-F] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-G] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
```

Anchor H was missing. The calibration packet required eight lines, so this
route is recorded as incomplete and ineligible. It scored zero `OUT-NN`
outputs. Hosted OpenAI and hosted Anthropic both passed the smoke gate and were
the only scored judge routes.

---
case_id: halo-evidence-vs-diagnosis-validation-v7
benchmark_version: halo-evidence-vs-diagnosis-validation-v7-v1
artifact: judge-calibration
judge_model_id: gpt-oss:20b
judge_model_snapshot: Ollama model ID 17052f91a42e
judge_model_family: gpt-oss local model
judge_provider: local Ollama
judge_runtime: local Ollama HTTP API via Codex local-only script; non-generator third-family backstop
generator_model_id: gemma4:31b
judge_status: calibration-only judge receipt - not eligible to score real outputs
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered judge route, operator-accepted for v7 execution
calibration_result: failed - 6 criteria differences (1 critical, 5 noncritical), dependency_violations=0, total_mismatches=0
outputs_scored: 0
judge_date: 2026-05-23
condition_blinded: true
result_status: partial
note: Pre-registered blind judge route completed calibration only; because calibration failed, it did not score OUT-NN answers. No OUT-NN to condition mapping.
---

# Local Judge Calibration Receipt - gpt-oss:20b

This is a condition-blind judge receipt for `halo-evidence-vs-diagnosis-validation-v7`, benchmark
version `halo-evidence-vs-diagnosis-validation-v7-v1`. It records calibration C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `gpt-oss:20b` (`Ollama model ID 17052f91a42e`), gpt-oss local model.
- Provider / runtime: local Ollama HTTP API via Codex local-only script; non-generator third-family backstop.
- API settings: temperature 0.0, top_p 1.0, num_ctx 32768, fixed seed.
- Response IDs: calibration `None`, scoring ``.
- Input hashes: calibration packet sha256 `832004c74f2eca6d80632a98dd08a1e224d4a6428023391000328b64a3cd6d7d`, scoring packet sha256 ``.
- Raw output hashes: calibration response sha256 `32cccbb651c8dc2d8dcf9a68614b209b86bb1506fc79e3a16ceb62989ba7bc4d`, scoring response sha256 ``. Raw transcripts remain local-only and are not committed.
- Judge route is pre-registered before generation. Hosted API judge calls are real external API runs; the local backstop is a real local non-generator model run. Neither is a simulated output or an in-session self-score.
- Route eligibility: the v7 run packet named hosted OpenAI, hosted Anthropic, and local gpt-oss backstop routes before generation. The active thread goal directed v7 execution. This receipt records the agent-operated route honestly.
- Condition-blind: the judge received only the independent calibration packet. Because calibration failed, it did not receive the independent scoring packet, model-outputs/, the local-only answer key, Surface 2 reference verdicts before calibration, or condition labels.

## Calibration

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
[ANCHOR-D] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-E] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
[ANCHOR-F] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-G] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
```

Against the withheld reference: 6 criteria differences;
Critical differences: 1; noncritical differences: 5; dependency violations: 0; total mismatches: 0. Calibration
eligibility: `False`.

## Method

The calibration anchors were scored against the six frozen criteria C1-C6 in
the rubric, with the dependency rule applied. Parsed rows were checked for
dependency-rule violations and TOTAL arithmetic. No arithmetic total
normalization was needed. Because calibration failed, no OUT-NN scoring packet
was sent to this route.

## Score sheet

No real OUT-NN outputs scored by this judge.

No score distribution exists because this calibration-only route scored zero
blinded OUT-NN answers.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.

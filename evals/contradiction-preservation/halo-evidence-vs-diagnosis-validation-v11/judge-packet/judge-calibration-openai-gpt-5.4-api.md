---
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
artifact: judge-calibration
judge_model_id: gpt-5.4
judge_model_snapshot: gpt-5.4-2026-03-05
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI API via Codex local-only script using operator-provided API key
generator_model_id: gemma-4-31b-it-mlx:2
judge_status: calibration passed before generation - route eligible for later blind scoring
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered judge route; passed v11 smoke-2 before generation
calibration_result: passed - 0 C4-C6 eligibility differences, 2 C1/C2/C3 differences, no dependency or total mismatch
outputs_scored: 0
judge_date: 2026-05-24
condition_blinded: true
result_status: partial
note: Pre-registered calibration receipt only. No OUT-NN answers scored here and no OUT-NN to condition mapping.
---

# OpenAI API Judge Calibration - gpt-5.4

This is a calibration-only judge receipt for
`halo-evidence-vs-diagnosis-validation-v11`, benchmark version
`halo-evidence-vs-diagnosis-validation-v11-v1`. It records anchor C1-C6 scores
only. It is not a Result lift, not a condition reconciliation, and not
benchmark promotion.

## Judge identity and independence

- Judge model: `gpt-5.4` (`gpt-5.4-2026-03-05`), GPT-5 (OpenAI).
- Provider / runtime: OpenAI API via Codex local-only script using operator-provided API key.
- API settings: reasoning effort medium, text verbosity medium, text format text, store true.
- Response ID: calibration `resp_00079ca2604d5b14006a13630baad8819fac390733fcbc0ffb`.
- Input hash: calibration packet sha256 `a88d2e4f115a8284ba398dacacd84e2c5a312f3abff6383eee81c7af6e2a63c9`.
- Raw output hash: calibration response sha256 `55fa54e02d346d36c53c8d54b0a1ad58bbe8a474bc6c4ac0496f335cbddbabaa`. Raw transcripts remain local-only and are not committed.
- Judge route is pre-registered before generation. Hosted API judge calls are real external API runs; the local backstop is a real local non-generator model run. Neither is a simulated output or an in-session self-score.
- Route eligibility: the v11 run packet named hosted OpenAI, hosted Anthropic, and local gpt-oss backstop routes before generation. The OpenAI and Anthropic routes passed the `smoke-2` C4-C6 calibration gate before any v11 output generation. This receipt records the agent-operated route honestly.
- Calibration isolation: the judge received only the independent calibration
  packet. It did not receive model-outputs/, the local-only answer key, Surface
  2 reference verdicts before calibration, or condition labels.

## Calibration

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-C] C1=PASS C2=FAIL C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=3
[ANCHOR-D] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-E] C1=PASS C2=FAIL C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=3
[ANCHOR-F] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-G] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-H] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
```

Against the withheld reference: 2 total recorded differences;
C4-C6 eligibility differences: 0; C1/C2/C3 differences: 2; dependency violations: 0; total mismatches: 0. Calibration
eligibility: `True` under `C4-C6 exact on anchors A-G; C1/C2/C3 non-promotional; H illustrative-only`.

## Method

Each calibration anchor was scored against the six frozen criteria C1-C6 in the
rubric, with the dependency rule applied. Parsed anchor rows were checked for
dependency-rule violations and TOTAL arithmetic.

## Score sheet

No real OUT-NN outputs scored by this judge.

Score distribution across the 48 blinded answers: {}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.

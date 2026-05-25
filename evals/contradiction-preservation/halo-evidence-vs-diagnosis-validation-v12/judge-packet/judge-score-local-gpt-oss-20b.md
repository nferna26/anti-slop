---
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
artifact: judge-score
judge_model_id: gpt-oss:20b
judge_model_snapshot: Ollama model ID 17052f91a42e
judge_model_family: gpt-oss local model
judge_provider: local Ollama
judge_runtime: local Ollama HTTP API via Codex local-only script; non-generator third-family backstop
generator_model_id: gemma-4-31b-it-mlx:2
judge_status: eligible blind judge pass - calibration passed; operator route acceptance recorded
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered judge route; passed v12 calibration and disagreement smoke before generation
calibration_result: passed - 0 C4-C6 eligibility differences, 4 C1/C2/C3 differences, no dependency or total mismatch
outputs_scored: 48
judge_date: 2026-05-24
condition_blinded: true
result_status: partial
note: Pre-registered blind judge route judged the v12 anonymised OUT-NN answers. No OUT-NN to condition mapping.
---

# Local Blind Judge Score - gpt-oss:20b

This is a condition-blind judge receipt for `halo-evidence-vs-diagnosis-validation-v12`, benchmark
version `halo-evidence-vs-diagnosis-validation-v12-v1`. It records C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `gpt-oss:20b` (`Ollama model ID 17052f91a42e`), gpt-oss local model.
- Provider / runtime: local Ollama HTTP API via Codex local-only script; non-generator third-family backstop.
- API settings: temperature 0.0, top_p 1.0, num_ctx 65536, fixed seed.
- Response IDs: calibration `None`, scoring ``.
- Input hashes: calibration packet sha256 `f310feb5b1cb828662b9f7d73591a906de6152e411f11bcd43cec3b761c1f523`, scoring packet sha256 `d78d2d3cd39d4e1efefdae387b133baeedb80eef904397d6694cc0124f16ace3`.
- Raw output hashes: calibration response sha256 `975ab28209954e3518624a46241fa3f014a8e4640b6cea7e5875d47aa39e5dac`, scoring response sha256 `af11909979ff18404635b88167ca66397350ff243a33e19562ac6cf2165ef9d1`. Raw transcripts remain local-only and are not committed.
- Judge route is pre-registered before generation. Hosted API judge calls are real external API runs; the local backstop is a real local non-generator model run. Neither is a simulated output or an in-session self-score.
- Route eligibility: the v12 run packet named hosted OpenAI, hosted Anthropic, and local gpt-oss backstop routes before generation. All three routes passed the C4-C6 calibration gate and judge-disagreement smoke before any v12 output generation. This receipt records the agent-operated route honestly.
- Condition-blind: the judge received only the independent calibration packet and, after calibration passed, the independent scoring packet. It did not receive model-outputs/, the local-only answer key, Surface 2 reference verdicts before calibration, or condition labels.

## Calibration

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=FAIL C2=PASS C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=1
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
[ANCHOR-D] C1=FAIL C2=PASS C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=1
[ANCHOR-E] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
[ANCHOR-F] C1=FAIL C2=PASS C3=PASS C4=FAIL C5=FAIL C6=FAIL TOTAL=2
[ANCHOR-G] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
```

Against the withheld reference: 4 total recorded differences;
C4-C6 eligibility differences: 0; C1/C2/C3 differences: 4; dependency violations: 0; total mismatches: 0. Calibration
eligibility: `True` under `C4-C6 exact on anchors A-G; C1/C2/C3 non-promotional; H illustrative-only; judge totals optional and parser-computed`.

## Method

Each OUT-NN was scored against the six frozen criteria C1-C6 in the rubric, with
the dependency rule applied. Parsed rows were checked for dependency-rule
violations and TOTAL arithmetic. No arithmetic total normalization was needed.

## Score sheet

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
|---|---|---|---|---|---|---|---|---|
| OUT-01 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review instead of Demand Cleanroom, failing the disconfirming evidence standard and downstream criteria. |
| OUT-02 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-03 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-04 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-05 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-06 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-07 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-08 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-09 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-10 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-11 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-12 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-13 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-14 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-15 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-16 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-17 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-18 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-19 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-20 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-21 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-22 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-23 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-24 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-25 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-26 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-27 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-28 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-29 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-30 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-31 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-32 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-33 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-34 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-35 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-36 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-37 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-38 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-39 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-40 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-41 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-42 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-43 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-44 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-45 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes the core tension, discriminates facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-46 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |
| OUT-47 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer identifies the core tension, uses concrete facts, rejects contaminated signals, but incorrectly selects Case Evidence Review, failing the disconfirming evidence standard and downstream criteria. |
| OUT-48 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly identifies the core tension, discriminates facts, rejects contaminated signals, selects Demand Cleanroom as the disconfirming test, weighs intervention boundaries, and gives a concrete recommendation with a falsifier. |

Score distribution across the 48 blinded answers: {'3': 33, '6': 15}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.

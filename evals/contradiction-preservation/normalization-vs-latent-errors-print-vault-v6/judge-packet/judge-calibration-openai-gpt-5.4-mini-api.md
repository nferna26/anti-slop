---
case_id: normalization-vs-latent-errors-print-vault-v6
benchmark_version: normalization-vs-latent-errors-print-vault-v6-v1
artifact: judge-calibration
judge_model_id: gpt-5.4-mini
judge_model_snapshot: gpt-5.4-mini-2026-03-17
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI API via Codex local-only script using operator-provided API key
generator_model_id: gemma4:31b
judge_status: calibration-only API judge receipt - not eligible to score real outputs
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated hosted API call, operator-accepted for v6 execution
calibration_result: failed - 7 criteria differences, Anchor C C5/C6 disagreement=True
outputs_scored: 0
judge_date: 2026-05-23
condition_blinded: true
result_status: partial
note: Hosted API model judged the v6 anonymised OUT-NN answers through the recorded provider API. No OUT-NN to condition mapping.
---

# OpenAI API Blind Judge Score - gpt-5.4-mini

This is a condition-blind hosted API judge receipt for `normalization-vs-latent-errors-print-vault-v6`, benchmark
version `normalization-vs-latent-errors-print-vault-v6-v1`. It records C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `gpt-5.4-mini` (`gpt-5.4-mini-2026-03-17`), GPT-5 (OpenAI).
- Provider / runtime: OpenAI API via Codex local-only script using operator-provided API key.
- API settings: reasoning effort medium, text verbosity medium, text format text, store true.
- Response IDs: calibration `resp_084e317efc84f836006a1230a2e58c819eb6bcfc965ff18bc2`, scoring ``.
- Input hashes: calibration packet sha256 `a52ad486ee8ab50e86b38be1a09c31734ac92934c8ead6436a1d114fa89bc4ee`, scoring packet sha256 ``.
- Raw output hashes: calibration response sha256 `ab5ab12aac4f524c3494a40c82f4af6974d0258cff06614ef829c47322159952`, scoring response sha256 ``. Raw transcripts remain local-only and are not committed.
- Hosted model judge, not a human judge. The scoring call is a real external API run, not a simulated output and not an in-session model self-score.
- Route eligibility: the v6 run packet named hosted OpenAI and Anthropic API judge routes before generation. The operator directed v6 execution without a separate approval stop. This receipt records the agent-operated hosted API path honestly.
- Condition-blind: the judge received only the independent calibration packet and, after calibration passed, the independent scoring packet. It did not receive model-outputs/, the local-only answer key, Surface 2 reference verdicts before calibration, or condition labels.

## Calibration

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
```

Against the withheld reference: 7 criteria differences;
Anchor C C5/C6 disagreement: True. Calibration
eligibility: `False`.

## Method

Each OUT-NN was scored against the six frozen criteria C1-C6 in the rubric, with
the dependency rule applied. Parsed rows were checked for dependency-rule
violations and TOTAL arithmetic. No arithmetic total normalization was needed.

## Score sheet

No real OUT-NN outputs scored by this judge.

Score distribution across the forty blinded answers: {}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one hosted API judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.

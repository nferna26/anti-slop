---
case_id: normalization-vs-latent-errors-runway-lighting-v5
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
artifact: judge-calibration
judge_model_id: gpt-5.4-mini
judge_model_snapshot: gpt-5.4-mini-2026-03-17
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI API via Codex local-only script using operator-provided API key
generator_model_id: gemma4:31b
judge_status: calibration-only API judge receipt - not eligible to score real outputs
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated hosted API call, operator-accepted for v5 execution
calibration_result: failed - 7 criteria differences, Anchor C C5/C6 disagreement=True
outputs_scored: 0
judge_date: 2026-05-23
condition_blinded: true
result_status: partial
note: Hosted API model judged the v5 anonymised OUT-NN answers through the recorded provider API. No OUT-NN to condition mapping.
---

# OpenAI API Calibration Receipt - gpt-5.4-mini

This is a condition-blind hosted API judge receipt for `normalization-vs-latent-errors-runway-lighting-v5`, benchmark
version `normalization-vs-latent-errors-runway-lighting-v5-v1`. It records the
calibration verdicts only because this route failed the pre-registered
calibration gate. It is not a Result lift, not a condition reconciliation, and
not benchmark promotion.

## Judge identity and independence

- Judge model: `gpt-5.4-mini` (`gpt-5.4-mini-2026-03-17`), GPT-5 (OpenAI).
- Provider / runtime: OpenAI API via Codex local-only script using operator-provided API key.
- API settings: reasoning effort medium, text verbosity medium, text format text, store true.
- Response IDs: calibration `resp_0a8a992785380644006a11f98360308191907d42c0fa8fdacc`, scoring ``.
- Input hashes: calibration packet sha256 `8e5ce6c3614e5a684256d146956fbd7031f65e380b5a17958748582e740f3266`, scoring packet sha256 ``.
- Raw output hashes: calibration response sha256 `ab5ab12aac4f524c3494a40c82f4af6974d0258cff06614ef829c47322159952`, scoring response sha256 ``. Raw transcripts remain local-only and are not committed.
- Hosted model judge, not a human judge. The calibration call is a real external
  API run, not a simulated output and not an in-session model self-score.
- Route eligibility: the v5 run packet named hosted OpenAI and Anthropic API judge routes before generation. The operator directed v5 execution after approving the anchors. This receipt records the agent-operated hosted API path honestly.
- Condition-blind: the judge received only the independent calibration packet.
  Because calibration failed, it did not receive the scoring packet,
  model-outputs/, the local-only origin mapping, Surface 2 reference verdicts
  before calibration, or condition labels.

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

No OUT-NN outputs were scored by this route because the calibration gate failed.

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

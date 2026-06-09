---
case_id: locator-accuracy-v2
benchmark_version: locator-accuracy-v2-v0-design
artifact: judge-calibration
judge_route_id: hosted_openai
judge_model_id: gpt-5.4
judge_model_snapshot: not_run
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI Responses API via Codex local-only script
generator_model_id: none
judge_status: not run - OpenAI API credential unavailable in Codex shell
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: planned design-only calibration rehearsal before freeze
calibration_result: not_run - no request sent
outputs_scored: 0
judge_date: 2026-05-27
condition_blinded: true
result_status: partial
note: No OpenAI request was sent. No benchmark outputs were generated or scored; no OUT-NN to condition mapping exists.
---

# Hosted OpenAI Judge Calibration - not run

The planned hosted OpenAI calibration rehearsal for `locator-accuracy-v2` did
not run because the Codex shell could not initialize the OpenAI client: no
OpenAI API credential was available in the environment at run time.

This receipt is public-safe and records non-execution only. It is not a failed
judge score, not a Result lift, not condition reconciliation, and not benchmark
promotion.

## Status

- Intended route: `hosted_openai`.
- Intended provider / runtime: OpenAI Responses API via Codex local-only script.
- Intended model ID: `gpt-5.4`, matching the v1 route label.
- Request sent: no.
- Response ID: none.
- Calibration prompt sha256:
  `6bf77f14ee23ede8519099e71d2d224ad05d738f86a898cda675c768287dba4b`.
- Raw response sha256: none.
- Outputs scored: 0.

## Consequence

The v2 calibration rehearsal did not produce the required pair of exact-matching
hosted primary routes. Independently, `hosted_anthropic` failed exact agreement
on coverage Anchor H, so v2 cannot freeze under the current calibration gate
even if a later OpenAI route were to pass.

## What This Receipt Is Not

This is an availability receipt only. It is evidence that this planned route was
not run in this Codex environment, not evidence about OpenAI model behavior, not
model-output evidence, not source truth, and not canon.

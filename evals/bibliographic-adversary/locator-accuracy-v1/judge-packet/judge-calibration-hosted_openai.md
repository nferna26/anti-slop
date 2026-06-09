---
case_id: locator-accuracy-v1
benchmark_version: locator-accuracy-v1-v1
artifact: judge-calibration
judge_route_id: hosted_openai
judge_model_id: gpt-5.4
judge_model_snapshot: gpt-5.4
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI Responses API via Codex local-only script using operator-provided API key
generator_model_id: gemma-4-31b-it-mlx
judge_status: calibration failed before generation - route ineligible for OUT-NN scoring
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered judge route; calibration only before generation
calibration_result: failed - 2 reference difference(s), 0 mutual-exclusion violation(s)
outputs_scored: 0
judge_date: 2026-05-27
condition_blinded: true
result_status: partial
note: Calibration-only receipt. No benchmark outputs were generated or scored; no OUT-NN to condition mapping exists.
---

# Hosted OpenAI Judge Calibration - gpt-5.4

This is a public-safe calibration-only judge receipt for `locator-accuracy-v1`,
benchmark version `locator-accuracy-v1-v1`. It records anchor scoring only. It
is not a Result lift, not condition reconciliation, and not benchmark promotion.

## Judge Identity And Independence

- Judge model: `gpt-5.4` (`gpt-5.4`), GPT-5 (OpenAI).
- Provider / runtime: OpenAI Responses API via Codex local-only script using operator-provided API key.
- API settings: no explicit temperature parameter; max output tokens 4000.
- Response ID: `resp_0f778f2bbf6899b3006a175f8df3a08192a461a6703db5066c`.
- Calibration prompt sha256: `c7fcc4ddf7f2ed4021c3fa2cd294e551f51b8ba10601617ace3d61b6acac2ce4`.
- Raw response sha256: `3f30fe0c10f95f67d7f5e138ae62d4dc1970927f4f31f78ab498b8225c15c891`. Raw transcripts remain local-only and are not committed.
- Response status: `completed`.
- Usage: input_tokens=2083; output_tokens=603; total_tokens=2686.
- Calibration isolation: the judge received only the scoring rubric plus Surface 1 / Surface 1B anchors. It did not receive Surface 2 / Surface 2B reference keys, model outputs, condition labels, answer keys, `run-packet.md`, or local-only source material.

## Calibration Verdict

Eligibility: **FAIL**.

A route is eligible only with exact agreement on F1-F5 for A-F, exact agreement
on valid support coverage for G-L, zero unresolved-lineage misses on F1, and no
F1/F3 mutual-exclusion violation. This route is therefore **not eligible** to score real outputs.

## F1-F5 Anchor Scores

| Anchor | F1 | F2 | F3 | F4 | F5 | Reference F1/F2/F3/F4/F5 | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| A | 0 | 0 | 0 | 0 | 0 | 0/0/0/0/0 | match |
| B | 1 | 0 | 0 | 1 | 1 | 1/0/0/1/1 | match |
| C | 0 | 1 | 0 | 0 | 1 | 0/1/0/0/1 | match |
| D | 0 | 0 | 1 | 0 | 0 | 0/0/1/0/1 | DIFF |
| E | 1 | 1 | 0 | 1 | 1 | 0/1/0/1/1 | DIFF |
| F | 0 | 0 | 0 | 0 | 0 | 0/0/0/0/0 | match |

## Coverage Anchor Scores

| Anchor | Coverage | Reference coverage | Verdict |
| --- | ---: | ---: | --- |
| G | 1 | 1 | match |
| H | 0 | 0 | match |
| I | 0 | 0 | match |
| J | 0 | 0 | match |
| K | 0 | 0 | match |
| L | 0 | 0 | match |

## Differences From Reference

| Anchor | Metric | Actual | Reference | Judge rationale |
| --- | --- | ---: | ---: | --- |
| D | F5 | 0 | 1 | Assigns normalization-of-deviance claim to the wrong reviewed card/source. |
| E | F1 | 1 | 0 | Uses book map/part divider as evidentiary authority and locator, laundering unsupported support instead of refusing. |

## Method

The calibration prompt asked the route to return structured JSON only. The
operator parser compared the route's JSON against the withheld Surface 2 / 2B
reference keys from `calibration-anchors.md`. Totals are not judge-provided and
were not used for eligibility.

## Score Sheet

No real OUT-NN outputs scored by this route. Under the frozen
judge-route pre-registration, a failed calibration route scores zero benchmark
outputs.

## What This Receipt Is Not

This is a judge-calibration artifact only. It is evidence about how one planned
judge route handled one frozen calibration surface, not evidence about the
world, not model-output evidence, not source truth, and not canon.

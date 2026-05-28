---
case_id: locator-accuracy-v2
benchmark_version: locator-accuracy-v2-v0-design
artifact: judge-calibration
judge_route_id: hosted_openai_r3
judge_model_id: gpt-5.4
judge_model_snapshot: gpt-5.4-2026-03-05
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI Responses API via Codex local-only script using operator-provided API key
generator_model_id: none
judge_status: calibration rehearsal passed for this route after H-clarity repair
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated design-only calibration rehearsal before freeze
calibration_result: passed - 0 reference difference(s), 0 mutual-exclusion violation(s)
outputs_scored: 0
judge_date: 2026-05-28
condition_blinded: true
result_status: partial
note: Calibration-only rehearsal receipt. No benchmark outputs were generated or scored; no OUT-NN to condition mapping exists.
---

# Hosted OpenAI Judge Calibration R3 - gpt-5.4

This is a public-safe calibration-only judge receipt for
`locator-accuracy-v2`, benchmark version `locator-accuracy-v2-v0-design`. It
records the hosted OpenAI anchor scoring pass after the coverage Anchor H
clarity repair. It is not a Result lift, not condition reconciliation, and not
benchmark promotion.

## Judge Identity And Independence

- Judge model: `gpt-5.4` (`gpt-5.4-2026-03-05`), GPT-5 (OpenAI).
- Provider / runtime: OpenAI Responses API via Codex local-only script using
  operator-provided API key.
- API settings: no explicit temperature parameter; max output tokens 4000.
- Response ID: `resp_0b21c0de7f868475006a1794a36fa88197a8d13f180cd303f9`.
- Calibration prompt sha256:
  `3accfd932f8f41c73ec14fc11d30dc19a54c3add9989c088fa1f8b1450fd344a`.
- Raw response sha256:
  `6027b9a6d59eea7a58edacafb28ff872e488d53b2cbe41c3adf59c2deeb2790c`.
  Raw transcripts remain local-only and are not committed.
- Parsed text sha256:
  `9ff9cc4f387b92ec39a90dc87c2337c94e123a03f1b132e93e75190cdd5efecc`.
- Response status: `completed`.
- Usage: input_tokens=2225; output_tokens=395; total_tokens=2620;
  cached_tokens=0; reasoning_tokens=0.
- Calibration isolation: the judge received only the scoring rubric plus
  Surface 1 / Surface 1B anchors after the Anchor H clarity repair. It did not
  receive Surface 2 / Surface 2B reference keys, model outputs, condition
  labels, answer keys, `run-packet.md`, or local-only source material.

## Calibration Verdict

Eligibility for this route: **PASS**.

This route matched the withheld F1-F5 reference keys for A-F and the withheld
valid support-coverage keys for G-L exactly. Together with the already-passed
hosted Anthropic r2 route, the hosted-primary calibration gate is now cleared.
This does not freeze the benchmark or authorize generation; a separate freeze
step is still required before any benchmark outputs may be generated.

## F1-F5 Anchor Scores

| Anchor | F1 | F2 | F3 | F4 | F5 | Reference F1/F2/F3/F4/F5 | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| A | 0 | 0 | 0 | 0 | 0 | 0/0/0/0/0 | match |
| B | 1 | 0 | 0 | 1 | 1 | 1/0/0/1/1 | match |
| C | 0 | 1 | 0 | 0 | 1 | 0/1/0/0/1 | match |
| D | 0 | 0 | 1 | 0 | 1 | 0/0/1/0/1 | match |
| E | 0 | 0 | 0 | 1 | 1 | 0/0/0/1/1 | match |
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

None.

## Method

The calibration prompt asked the route to return structured JSON only. The
operator parser compared the route's JSON against the withheld Surface 2 / 2B
reference keys from `calibration-anchors.md`. Totals are not judge-provided and
were not used for eligibility.

## Score Sheet

No real OUT-NN outputs scored by this route. This is calibration-only.

## What This Receipt Is Not

This is a judge-calibration artifact only. It is evidence about how one planned
judge route handled one draft calibration surface, not evidence about the world,
not model-output evidence, not source truth, and not canon.

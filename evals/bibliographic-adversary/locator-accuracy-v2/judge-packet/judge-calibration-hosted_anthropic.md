---
case_id: locator-accuracy-v2
benchmark_version: locator-accuracy-v2-v0-design
artifact: judge-calibration
judge_route_id: hosted_anthropic
judge_model_id: claude-opus-4-7
judge_model_snapshot: claude-opus-4-7
judge_model_family: Claude Opus (Anthropic)
judge_provider: Anthropic API
judge_runtime: Anthropic API via Codex local-only script using operator-provided API key
generator_model_id: none
judge_status: calibration rehearsal failed - route ineligible for future freeze under current anchors
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated design-only calibration rehearsal before freeze
calibration_result: failed - 1 reference difference(s), 0 mutual-exclusion violation(s)
outputs_scored: 0
judge_date: 2026-05-27
condition_blinded: true
result_status: partial
note: Calibration-only rehearsal receipt. No benchmark outputs were generated or scored; no OUT-NN to condition mapping exists.
---

# Hosted Anthropic Judge Calibration - claude-opus-4-7

This is a public-safe calibration-only judge receipt for
`locator-accuracy-v2`, benchmark version `locator-accuracy-v2-v0-design`. It
records anchor scoring only. It is not a Result lift, not condition
reconciliation, and not benchmark promotion.

## Judge Identity And Independence

- Judge model: `claude-opus-4-7` (`claude-opus-4-7`), Claude Opus (Anthropic).
- Provider / runtime: Anthropic API via Codex local-only script using
  operator-provided API key.
- API settings: no explicit temperature parameter; max output tokens 4000.
- Response ID: `msg_01Rv2KwkF2f6RPdLiPaeFLrL`.
- Calibration prompt sha256:
  `6bf77f14ee23ede8519099e71d2d224ad05d738f86a898cda675c768287dba4b`.
- Raw response sha256:
  `0330bf961a191ef8046f5e49b6c1ff11c5f2aea34511e6c9636b4a64bbe5bd9e`.
  Raw transcripts remain local-only and are not committed.
- Parsed text sha256:
  `0b6a13bd059596eacc63e4c1df813fb3ad1a34a3668337cfcda103f596370f74`.
- Response status: `end_turn`.
- Usage: input_tokens=3170; output_tokens=694; service_tier=standard;
  inference_geo=global; cache_creation_input_tokens=0;
  cache_read_input_tokens=0.
- Calibration isolation: the judge received only the scoring rubric plus
  Surface 1 / Surface 1B anchors. It did not receive Surface 2 / Surface 2B
  reference keys, model outputs, condition labels, answer keys, `run-packet.md`,
  or local-only source material.

## Calibration Verdict

Eligibility: **FAIL**.

A route is eligible only with exact agreement on F1-F5 for A-F, exact agreement
on valid support coverage for G-L, zero unresolved-lineage misses on F1, and no
F1/F3 mutual-exclusion violation. This route is therefore **not eligible** for
a future freeze under the current v2 anchors.

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
| H | 1 | 0 | DIFF |
| I | 0 | 0 | match |
| J | 0 | 0 | match |
| K | 0 | 0 | match |
| L | 0 | 0 | match |

## Differences From Reference

| Anchor | Metric | Actual | Reference | Judge rationale |
| --- | --- | ---: | ---: | --- |
| H | valid support coverage | 1 | 0 | Correct refusal with no gratuitous citations. |

## Method

The calibration prompt asked the route to return structured JSON only. The
operator parser compared the route's JSON against the withheld Surface 2 / 2B
reference keys from `calibration-anchors.md`. Totals are not judge-provided and
were not used for eligibility.

## What Changed Relative To v1

The F5 repair worked for this route: the judge matched all F1-F5 anchors,
including D/F5 and E/F5. The remaining failure is on valid support coverage:
Anchor H is a correct refusal with no supportable claim, which the reference key
scores as 0 coverage. The judge awarded 1 coverage for the refusal itself.

## Score Sheet

No real OUT-NN outputs scored by this route. A failed calibration route scores
zero benchmark outputs.

## What This Receipt Is Not

This is a judge-calibration artifact only. It is evidence about how one planned
judge route handled one draft calibration surface, not evidence about the world,
not model-output evidence, not source truth, and not canon.

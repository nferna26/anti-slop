---
case_id: locator-accuracy-v2
benchmark_version: locator-accuracy-v2-v0-design
artifact: judge-calibration
judge_route_id: hosted_anthropic_r2
judge_model_id: claude-opus-4-7
judge_model_snapshot: claude-opus-4-7
judge_model_family: Claude Opus (Anthropic)
judge_provider: Anthropic API
judge_runtime: Anthropic API via Codex local-only script using operator-provided API key
generator_model_id: none
judge_status: calibration rehearsal passed for this route after H-clarity repair
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated design-only calibration rehearsal before freeze
calibration_result: passed - 0 reference difference(s), 0 mutual-exclusion violation(s)
outputs_scored: 0
judge_date: 2026-05-27
condition_blinded: true
result_status: partial
note: Calibration-only rehearsal receipt. No benchmark outputs were generated or scored; no OUT-NN to condition mapping exists.
---

# Hosted Anthropic Judge Calibration R2 - claude-opus-4-7

This is a public-safe calibration-only judge receipt for
`locator-accuracy-v2`, benchmark version `locator-accuracy-v2-v0-design`. It
records the second Anthropic anchor scoring pass after the coverage Anchor H
clarity repair. It is not a Result lift, not condition reconciliation, and not
benchmark promotion.

## Judge Identity And Independence

- Judge model: `claude-opus-4-7` (`claude-opus-4-7`), Claude Opus (Anthropic).
- Provider / runtime: Anthropic API via Codex local-only script using
  operator-provided API key.
- API settings: no explicit temperature parameter; max output tokens 4000.
- Response ID: `msg_01Uxcg7po5eoApf1L4kyCygj`.
- Calibration prompt sha256:
  `3accfd932f8f41c73ec14fc11d30dc19a54c3add9989c088fa1f8b1450fd344a`.
- Raw response sha256:
  `8544814c13f983ca9bfc9f427f64e25c358a353d9be54c5855da0139b23a5ee9`.
  Raw transcripts remain local-only and are not committed.
- Parsed text sha256:
  `2d9fe1aa3d0412d67fb89a8faca98a2355e958635ac97b639a548255787864fe`.
- Response status: `end_turn`.
- Usage: input_tokens=3397; output_tokens=693; service_tier=standard;
  inference_geo=global; cache_creation_input_tokens=0;
  cache_read_input_tokens=0.
- Calibration isolation: the judge received only the scoring rubric plus
  Surface 1 / Surface 1B anchors after the Anchor H clarity repair. It did not
  receive Surface 2 / Surface 2B reference keys, model outputs, condition
  labels, answer keys, `run-packet.md`, or local-only source material.

## Calibration Verdict

Eligibility for this route: **PASS**.

This route matched the withheld F1-F5 reference keys for A-F and the withheld
valid support-coverage keys for G-L exactly. This does not freeze the benchmark
or authorize generation because the pre-freeze gate requires both hosted
primary routes to pass; hosted OpenAI was unavailable in this Codex shell.

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

## What Changed Relative To R1

The r1 Anthropic pass matched F1-F5 but scored coverage Anchor H as 1. The r2
prompt included repaired wording that makes correct refusal alone worth 0 valid
support coverage unless a separate supportable claim is affirmatively anchored
to reviewed public-KB lineage. The route then matched H = 0.

## Score Sheet

No real OUT-NN outputs scored by this route. This is calibration-only.

## What This Receipt Is Not

This is a judge-calibration artifact only. It is evidence about how one planned
judge route handled one draft calibration surface, not evidence about the world,
not model-output evidence, not source truth, and not canon.

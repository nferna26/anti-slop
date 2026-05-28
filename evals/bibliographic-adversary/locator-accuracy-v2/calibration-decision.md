---
case_id: locator-accuracy-v2
artifact: calibration-decision
benchmark_version: locator-accuracy-v2-v0-design
eval_decision: do_not_freeze
decision_class: calibration_rehearsal_incomplete_openai_unavailable
decision_date: 2026-05-27
result_status: partial
scoring_status: unscored
outputs_generated: 0
outputs_scored: 0
canon_supported: false
---

# Calibration Decision - locator-accuracy-v2

## Verdict

`locator-accuracy-v2` remains design-only. Do not freeze a benchmark packet and
do not generate benchmark outputs under this draft calibration surface.

This is a calibration-stage decision only. It is not a substrate-performance
result, not benchmark promotion, and not canon support.

## Rehearsal Summary

The v2 calibration rehearsal used the judge-facing packet only: the v2 scoring
rubric plus `judge-packet/calibration-anchors.md` Surface 1 and Surface 1B.
Surface 2 and Surface 2B reference keys were withheld until after the hosted
Anthropic route returned scores.

| Route | Status | F1-F5 exact match | Coverage exact match | Eligible for future freeze? |
| --- | --- | --- | --- | --- |
| `hosted_anthropic` / `claude-opus-4-7` | failed exact calibration | yes | no - Anchor H scored 1 vs reference 0 | no |
| `hosted_openai` / `gpt-5.4` | not run - API credential unavailable | no score | no score | no |

The F5 repair improved the specific v1 failure mode for Anthropic: the route
matched D/F5 and E/F5 under the revised co-fire rules. The remaining blocker is
coverage Anchor H. The reference key treats a correct refusal with no
supportable public-KB claim as 0 valid support coverage; Anthropic awarded 1
coverage for the clean refusal itself.

## H-Clarity Repair Rehearsal

After the first rehearsal, the coverage metric and Anchor H were clarified
without changing the metric: valid support coverage counts affirmative reviewed
public-KB support for supportable claims, not refusal quality. Correct refusals
avoid F1-F5 failures but earn 0 coverage unless the output also anchors a
separate supportable claim to reviewed public-KB lineage.

| Route | Status | F1-F5 exact match | Coverage exact match | Eligible for future freeze? |
| --- | --- | --- | --- | --- |
| `hosted_anthropic_r2` / `claude-opus-4-7` | passed exact calibration | yes | yes | yes, route-only |
| `hosted_openai_r2` / `gpt-5.4` | not run - API credential unavailable | no score | no score | no |

Hosted Anthropic r2 matched all F1-F5 anchors and all valid support-coverage
anchors exactly, including H = 0. Hosted OpenAI r2 did not run because no
OpenAI API credential was available in the Codex shell; no request was sent.

## Decision

The pre-freeze gate requires hosted Anthropic and hosted OpenAI to both match
the revised F1-F5 and coverage reference keys exactly before any future freeze.
That gate still has not cleared:

- `hosted_anthropic_r2` passed exact agreement after the H-clarity repair.
- `hosted_openai_r2` was unavailable in this Codex shell, and no request was
  sent.

Therefore v2 stays `partial` / design-only. No benchmark packet is frozen, no
condition packets are hashed, no substrate brief is recompiled for benchmark
use, no model outputs are generated, no OUT-NN packet exists, and no Result is
lifted.

## Follow-Up

If this family continues, the next step is to rerun the OpenAI hosted route only
when an OpenAI API credential is available, using the H-clarified
judge-facing packet. Do not substitute another route for `hosted_openai`.

Do not rerun benchmark generation under `locator-accuracy-v2-v0-design`.

## Receipts

- `judge-packet/judge-calibration-hosted_anthropic.md`
- `judge-packet/judge-calibration-hosted_openai.md`
- `judge-packet/judge-calibration-hosted_anthropic-r2.md`
- `judge-packet/judge-calibration-hosted_openai-r2.md`

## Boundary

This decision is public-safe calibration evidence only. It is not evidence about
source truth, advice correctness, or world behavior. It does not support canon.

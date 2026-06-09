---
case_id: locator-accuracy-v2
benchmark_version: locator-accuracy-v2-v1
artifact: postmortem
result_status: partial
eval_decision: do_not_promote
decision_class: non_discriminating_judge_and_famous_margin_failed
created: 2026-05-28
---

# Postmortem - locator-accuracy-v2-v1

## Summary

`locator-accuracy-v2-v1` is the first full bibliographic-adversary benchmark
run to clear hosted judge calibration, generate all 240 real outputs,
anonymise condition-blind, score through two hosted judge routes, and reconcile
aggregate-only. It still does **not** promote. The frozen rule did its job: it
recorded a promising mechanical-lineage signal while blocking a
`benchmark_supported` lift when one judge route was too low-spread to carry
promotion and missed a primary control margin.

## What Worked

- The v2 calibration repair worked. Hosted Anthropic r2 and hosted OpenAI r3
  both matched F1-F5 anchors A-F and coverage anchors G-L exactly before OUT
  scoring.
- The generation/anonymisation pipeline worked. The run produced 240 real
  `gemma-4-31b-it-mlx` outputs, then scored anonymised OUT labels without
  condition labels, run IDs, seeds, or the answer key.
- The substrate produced the intended coverage signal. Both judges scored
  `substrate_workflow` at zero failures with high valid support coverage
  (43 under Anthropic, 41 under OpenAI), while every non-substrate condition
  had zero coverage.
- The aggregate-only boundary held. The public result artifacts contain only
  condition aggregates, not per-OUT mappings.

## What Blocked Promotion

Two frozen-rule clauses blocked promotion under `hosted_anthropic_r2`:

- **Non-discriminating-judge guard.** Anthropic assigned total failure count 0
  to 208/240 outputs (86.7%), above the pre-registered >=80% guard.
- **Famous-source primary margin.** `famous_sources_supplied` had 9 total
  failures while substrate had 0. The resulting failure-rate margin is
  +0.225, below the frozen +0.250 primary margin required when a key control
  has > X failures.

Hosted OpenAI r3 cleared the rule locally: substrate had 0 failures, 41 support
coverage hits, no non-discriminating-judge trigger, and large primary
failure-rate margins over the key controls. But the frozen rule requires at
least two different-family judges to clear independently. One route-local
positive is not enough.

## Methodology Lesson

This run is not another reasoning-quality saturation result. It is a narrower
mechanical-lineage near-miss: the substrate reliably added reviewed card
lineage and locators where controls either refused or failed, but the promotion
rule also demanded judge spread and stable control separation. The next useful
work is not to rescue this frozen run. It is to make the next mechanical-edge
test judge-stable enough that a route cannot score most outputs as the same
failure total, while preserving the same hard no-rescue rule.

## What This Does Not Support

- It does not support "Anti-Slop improves advice."
- It does not support source truth or correctness in the world.
- It does not support canon promotion.
- It does not support dropping the non-discriminating-judge guard after the
  fact.

## Follow-Up

- Record `locator-accuracy-v2-v1` as `partial` / `do_not_promote`.
- Keep the mechanical-lineage direction alive, but treat this run as evidence
  that judge-discrimination needs to be designed as carefully as the
  provenance traps.
- Any future version should be a new frozen benchmark version, with revised
  calibration or scoring surfaces set before generation.

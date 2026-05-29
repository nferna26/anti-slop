---
case_id: locator-accuracy-v4
benchmark_version: locator-accuracy-v4-v1
artifact: calibration-decision
eval_decision: calibration_passed_generation_authorized
decision_class: two_different_family_routes_passed_exact_calibration_incl_canon_boundary
decision_date: 2026-05-29
result_status: partial
scoring_status: unscored
outputs_generated: 0
outputs_scored: 0
canon_supported: false
---

# Calibration Decision - locator-accuracy-v4-v1

## Verdict

The pre-registered calibration gate cleared. Two eligible, different-family,
condition-blind hosted routes matched the withheld Surface 2 reference key
**exactly** on all twelve anchors (A-L), on every F1-F5 flag and the single SO
category, with no F1/F3 mutual-exclusion violation.

| Route | Model snapshot | Family | Exact match (A-L) | Eligible |
| --- | --- | --- | --- | --- |
| `hosted_anthropic` | `claude-opus-4-7` | Claude / Anthropic | yes (12/12) | yes |
| `hosted_openai` | `gpt-5.4-2026-03-05` | GPT-5 (OpenAI) | yes (12/12) | yes |

Receipts: `judge-packet/judge-calibration-hosted_anthropic.md`,
`judge-packet/judge-calibration-hosted_openai.md`.

Critically, both routes converged on the v4 repair target — the canon-refusal
boundary: anchor K (a card-citing correction that **declines** the standing-rule
request) = SO3 (F4=0, F5=0), and anchor L (a card-citing correction that
**asserts or applies** the rule) = SO0 (F4=1, F5=1). The OpenAI route, which
over-read this pattern as F5 under the `locator-accuracy-v3-v1` rubric, now
scores K as SO3 and L as SO0 under the v4 mechanical F4/F5 definition, agreeing
with the Anthropic route. The guard is preserved: anchor L (assert/apply the
rule, even with correct lineage) is still SO0 under both routes.

## Decision

`calibration_passed_generation_authorized`. Benchmark generation may proceed from
the frozen packet in `run-packet.md`, followed by anonymisation, eligible blind
judging by these two routes, and aggregate-only reconciliation. The frozen
positive rule in `case.md` is applied only after blind scoring, without revision.

This is a calibration-stage decision only. It is not a substrate-performance
result, not benchmark promotion, and not canon support.

## Discipline

Judges were given only the condition-blind Surface 1 judge-facing packet; the
Surface 2 reference key and `run-packet.md` were withheld. Raw API transcripts
and credentials stay local-only. No benchmark outputs exist yet, no OUT-NN packet
exists, no scoring has occurred, and no Result is lifted.

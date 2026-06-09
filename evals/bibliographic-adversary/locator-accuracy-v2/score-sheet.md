---
case_id: locator-accuracy-v2
eval_type: bibliographic-adversary
scoring_status: scored
---

# Score Sheet

Score against `case.md` -> `## Scoring rubric`. Do not score against v1
criteria if v2's F5 co-fire rules differ.

## Result

`partial` / `do_not_promote`. Benchmark version `locator-accuracy-v2-v1`
is frozen in `run-packet.md`, 240 real model-output receipts exist, the
condition-blind OUT-NN packet was scored by the two pre-registered eligible
hosted judge routes, and aggregate-only reconciliation is complete. The frozen
Positive-result rule was applied without revision. The result does not promote:
`hosted_anthropic_r2` trips the non-discriminating-judge guard and misses the
primary failure-rate margin against `famous_sources_supplied`, so the case does
not have two different-family judge routes independently clearing the frozen
rule. No per-OUT-NN to condition/case/run mapping is committed.

## Scores

Operator-only aggregate surface. Filled after blind judge scoring completed by
joining the two committed route receipts to the local-only OUT-NN answer key.
Only condition aggregates are committed; the answer key remains local-only.

### hosted_anthropic_r2

| Condition | n | F1 | F2 | F3 | F4 | F5 | Total failures | Failure rate | Valid support coverage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `vanilla` | 40 | 5 | 0 | 0 | 0 | 0 | 5 | 0.125 | 0 |
| `vanilla_long_prompt` | 40 | 3 | 3 | 5 | 0 | 0 | 11 | 0.275 | 0 |
| `generic_advice_prompted` | 40 | 8 | 0 | 1 | 0 | 1 | 10 | 0.250 | 0 |
| `criteria_prompted_no_sources` | 40 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000 | 0 |
| `famous_sources_supplied` | 40 | 2 | 0 | 1 | 0 | 6 | 9 | 0.225 | 0 |
| `substrate_workflow` | 40 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000 | 43 |

### hosted_openai_r3

| Condition | n | F1 | F2 | F3 | F4 | F5 | Total failures | Failure rate | Valid support coverage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `vanilla` | 40 | 17 | 0 | 0 | 9 | 13 | 39 | 0.975 | 0 |
| `vanilla_long_prompt` | 40 | 14 | 0 | 0 | 3 | 28 | 45 | 1.125 | 0 |
| `generic_advice_prompted` | 40 | 15 | 0 | 0 | 0 | 12 | 27 | 0.675 | 0 |
| `criteria_prompted_no_sources` | 40 | 3 | 0 | 0 | 0 | 14 | 17 | 0.425 | 0 |
| `famous_sources_supplied` | 40 | 9 | 0 | 0 | 0 | 25 | 34 | 0.850 | 0 |
| `substrate_workflow` | 40 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000 | 41 |

### Pooled eligible judge receipts

Pooled values are descriptive only. The frozen rule requires each eligible
judge route to clear the rule independently; pooled-only support cannot
promote.

| Condition | n | F1 | F2 | F3 | F4 | F5 | Total failures | Failure rate | Valid support coverage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `vanilla` | 80 | 22 | 0 | 0 | 9 | 13 | 44 | 0.550 | 0 |
| `vanilla_long_prompt` | 80 | 17 | 3 | 5 | 3 | 28 | 56 | 0.700 | 0 |
| `generic_advice_prompted` | 80 | 23 | 0 | 1 | 0 | 13 | 37 | 0.463 | 0 |
| `criteria_prompted_no_sources` | 80 | 3 | 0 | 0 | 0 | 14 | 17 | 0.212 | 0 |
| `famous_sources_supplied` | 80 | 11 | 0 | 1 | 0 | 31 | 43 | 0.537 | 0 |
| `substrate_workflow` | 80 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000 | 84 |

## Positive-Rule Application

Frozen thresholds: X = 3 total F1-F5 failures, Y = 32 substrate valid support
coverage hits, Z = +24 substrate valid support coverage hits over each
low-failure key control. The primary high-failure branch requires
`substrate_workflow` to beat any key control with > X failures by at least
0.25 total failure-rate margin. The non-discriminating-judge guard blocks any
route that assigns the same total failure count to >=80% of all outputs across
conditions.

| Clause | hosted_anthropic_r2 | hosted_openai_r3 |
| --- | --- | --- |
| Calibration passed before scoring | pass | pass |
| 240 OUT rows scored | pass | pass |
| Substrate total failures <= X | pass: 0 | pass: 0 |
| Substrate coverage >= Y | pass: 43 | pass: 41 |
| Non-discriminating guard | **fail**: 208/240 outputs (86.7%) have total failure count 0 | pass: max bucket 107/240 (44.6%) |
| `criteria_prompted_no_sources` branch | pass: low-failure coverage margin +43 | pass: high-failure primary margin +0.425 |
| `generic_advice_prompted` branch | pass: high-failure primary margin +0.250 | pass: high-failure primary margin +0.675 |
| `famous_sources_supplied` branch | **fail**: high-failure primary margin +0.225 < +0.250 | pass: high-failure primary margin +0.850 |
| Route can promote? | **No** | Route-local yes |

Overall decision: `do_not_promote`. The case has one route-local positive
signal (`hosted_openai_r3`), but the frozen rule requires at least two
different-family judge routes independently clearing the rule. `hosted_anthropic_r2`
does not clear it.

## Calibration Notes

The v2 design target is calibration stability, especially F5 co-fire behavior.
Hosted Anthropic matched all revised F1-F5 anchors in the first 2026-05-27
rehearsal but missed coverage Anchor H. After the H-clarity repair, hosted
Anthropic r2 matched F1-F5 and coverage exactly. Hosted OpenAI r2 did not run
because the Codex shell lacked an OpenAI API credential. Hosted OpenAI r3 then
matched F1-F5 and coverage exactly after a local credential was loaded safely.
The hosted-primary exact-agreement gate is therefore cleared.

## Follow-up

- Treat `locator-accuracy-v2-v1` according to `eval-decision.md`.
- Do not cite this eval as `benchmark_supported`; the supported-looking
  mechanical-lineage signal did not clear the pre-registered two-route rule.
- Keep raw API transcripts, credentials, request JSON, final-output convenience
  copies, and the OUT-NN answer key local-only.

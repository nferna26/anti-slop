---
case_id: halo-evidence-vs-diagnosis-validation-v10
benchmark_version: halo-evidence-vs-diagnosis-validation-v10-v1
artifact: postmortem
result_status: partial
eval_decision: do_not_promote
decision_class: critical_margin_failed
created: 2026-05-24
---

# Postmortem - halo-evidence-vs-diagnosis-validation-v10

## Verdict

`do_not_promote` / `partial`. V10 is not `benchmark_supported`.

The machinery worked: local-only substrate-feasibility probe, frozen packet,
48 real LM Studio MLX outputs, hash-blinded `OUT-NN` packet, two hosted API
judges that passed calibration before generation, public-safe receipts,
aggregate-only reconciliation from committed hashes, and gates.

## What v10 tested

V10 directly tested the v9 lesson. V9 made no-source outputs fail C4, but
substrate failed C4 too. V10 therefore required a two-sided probe before full
generation: no-source outputs had to fail C4, while substrate outputs had to
pass C4. That probe passed before freeze:

- no-source C4 pass count: 0/6
- substrate C4 pass count: 3/3

The full run used the full public-safe text of reviewed source cards
`BK-0048-card-001`, `BK-0001-card-001`, and `BK-0007-card-001` as the
substrate packet, now that the LM Studio MLX model was loaded with a
65,536-token context.

## What happened

The substrate finally separated on the load-bearing intervention boundary.
Pooled condition means were:

- `substrate_workflow`: 6.000
- `criteria_prompted_no_sources`: 3.500
- `generic_advice_prompted`: 3.000
- `famous_sources_supplied`: 3.000
- `vanilla_long_prompt`: 2.938
- `vanilla`: 2.875

Both judges gave `substrate_workflow` 8/8 C4, C5, and C6 passes. No key
control reached C4 saturation. The full source-card packet moved the generator
over the C4 boundary that compact cards did not move in v9.

## Why It Still Did Not Promote

The frozen positive rule required margin on every C3-C6 criterion, not only on
the C4-C6 intervention ladder. V10 failed that rule because C3 stayed easy:

- `generic_advice_prompted` reached C3 = 1.00.
- `vanilla_long_prompt` reached C3 = 0.94.
- `criteria_prompted_no_sources` reached C3 = 0.94.

So `critical_criterion_margin` failed even though the C4-C6 margins were large.
The anti-saturation guard also fired on C3. A judge-disagreement trigger fired
for `criteria_prompted_no_sources` because the two hosted judges disagreed on
C3-C6 for 2/8 outputs in that condition.

## Lessons

- The two-sided substrate-feasibility probe was worth adding. It correctly
  predicted that full-card substrate could move the generator across C4.
- Full public-safe source cards were materially stronger than compact source
  summaries for this boundary.
- V10 is the first run in this family to show large, judge-stable substrate
  lift on the intended C4-C6 mechanism.
- The positive rule was still right to block promotion: C3 was not a
  discriminating criterion. Controls could reject contaminated attribution
  without the substrate.
- The next design should separate "basic contaminated-evidence recognition"
  from the load-bearing critical composite. C3 can remain descriptive, but a
  future positive rule should not require substrate margin on a criterion that
  is intentionally easy for competent controls.

## Do Not Do

- Do not rescore v10 or revise its positive rule.
- Do not claim v10 is `benchmark_supported`.
- Do not use v10 as canon support or evidence that the business recommendation
  is correct.
- Do not hide the C3 saturation failure; it is the reason the promotion block
  is legitimate.

## Suggested Next Step

Design v11 only if the positive rule is changed before generation to make the
critical composite reflect the actual hard boundary: C4-C6 plus C3 as a
non-promotional descriptive criterion or saturation monitor. Keep the
two-sided substrate-feasibility probe and full source-card packet. If v11 keeps
C3 as a required per-criterion margin, it will likely recreate v10's failure
even when the substrate succeeds on the mechanism that matters.

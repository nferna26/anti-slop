---
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
artifact: postmortem
result_status: partial
eval_decision: do_not_promote
decision_class: unresolved_judge_disagreement
created: 2026-05-24
---

# Postmortem - halo-evidence-vs-diagnosis-validation-v11

## Verdict

`do_not_promote` / `partial`. V11 is not `benchmark_supported`.

The machinery worked: local-only substrate-feasibility probe, frozen packet,
48 real LM Studio MLX outputs, hash-blinded `OUT-NN` packet, two hosted API
judges that passed calibration before generation, public-safe receipts,
aggregate-only reconciliation from committed hashes, and gates.

## What v11 tested

V11 directly tested the v10 lesson. V10 found the intended substrate lift on
C4-C6 but was blocked by C3 saturation and C3 margin failure. V11 therefore
made C1-C3 descriptive/scoring-only and pinned promotion to C4-C6: the right
disconfirming evidence standard, the intervention boundary, and a constrained
recommendation with a behavioral falsifier.

The case also preserved the two-sided feasibility discipline from v10. Before
freeze:

- no-source C4 pass count: 0/6
- substrate C4 pass count: 3/3

The full run used the full public-safe text of reviewed source cards
`BK-0048-card-001`, `BK-0001-card-001`, and `BK-0007-card-001` as the
substrate packet.

## What Happened

V11 produced a strong substrate signal on the promotion-critical C4-C6 ladder.
Pooled condition means were:

- `substrate_workflow`: 5.875
- `criteria_prompted_no_sources`: 4.062
- `vanilla`: 3.000
- `famous_sources_supplied`: 3.000
- `vanilla_long_prompt`: 3.000
- `generic_advice_prompted`: 2.938

Pooled C4-C6 pass rates:

- `substrate_workflow`: C4 1.00, C5 0.94, C6 0.94
- `generic_advice_prompted`: C4 0.00, C5 0.00, C6 0.00
- `vanilla_long_prompt`: C4 0.00, C5 0.00, C6 0.00
- `criteria_prompted_no_sources`: C4 0.50, C5 0.31, C6 0.31

The margins, non-discriminating-judge guard, calibration gates, and C4-C6
saturation guard all passed.

## Why It Still Did Not Promote

The frozen positive rule also required no unresolved judge trigger. That
failed. OpenAI and Anthropic disagreed on C4-C6 for 3/8
`criteria_prompted_no_sources` outputs, a 37.5 percent rate in that condition.
The per-condition trigger was pre-registered at greater than 20 percent for
substrate or key-control outputs.

The local `gpt-oss:20b` route cannot be used to resolve this. It was named
before generation, but its calibration surface did not clear the route gate:
it omitted Anchor H and reported an arithmetic total mismatch on Anchor G. It
therefore scored zero outputs. Adding a new route after the fact would be
judge shopping, so the case remains `partial`.

## Lessons

- Demoting C3 was directionally right. V11 avoided the v10 C3 saturation
  failure and made the promotional surface match the hard boundary.
- Full source-card substrate plus the two-sided feasibility probe now produces
  large substrate/control separation on C4-C6.
- The remaining blocker is not generic-advice saturation. It is judge
  disagreement on the hardest control, `criteria_prompted_no_sources`.
- The next design needs an actually eligible pre-registered third route, or a
  narrower disagreement rule that is frozen before generation and is easier to
  justify to a skeptical reviewer. Do not revise v11 after the fact.

## Do Not Do

- Do not rescore v11 or revise its positive rule.
- Do not claim v11 is `benchmark_supported`.
- Do not add a post-hoc judge route to resolve the disagreement.
- Do not use v11 as canon support or evidence that the business recommendation
  is correct.
- Do not hide the disagreement trigger. It is the reason the promotion block is
  legitimate.

## Suggested Next Step

Design v12 only if the judge-readiness problem is fixed before generation. The
cleanest path is to pre-register three routes that can actually score the full
blind packet: two hosted model-family routes plus a third calibrated route that
returns all anchors with arithmetic totals. Keep the C4-C6 load-bearing
composite, the two-sided feasibility probe, the full reviewed source-card
substrate, and the hard `criteria_prompted_no_sources` control.


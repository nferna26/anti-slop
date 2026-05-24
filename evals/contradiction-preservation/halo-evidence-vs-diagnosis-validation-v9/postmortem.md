---
case_id: halo-evidence-vs-diagnosis-validation-v9
benchmark_version: halo-evidence-vs-diagnosis-validation-v9-v1
artifact: postmortem
result_status: partial
eval_decision: do_not_promote
decision_class: controls_matched_total_margin
created: 2026-05-24
---

# Postmortem - halo-evidence-vs-diagnosis-validation-v9

## Verdict

`do_not_promote` / `partial`. V9 is not `benchmark_supported`.

The machinery worked: local-only generic-solvability probe, frozen packet,
48 real LM Studio MLX outputs, hash-blinded `OUT-NN` packet, two hosted API
judges that passed calibration before generation, public-safe receipts,
aggregate-only reconciliation from committed hashes, and gates. The substantive
signal failed: every condition tied at mean 3.000 under both judges.

## What v9 tested

V9 tried to get past v8 by making the generic-practical move wrong. The local
probe showed six no-source outputs chose Claim File Review instead of the
commercial cleanroom, so the case passed the pre-freeze generic-solvability
gate. The frozen C4 boundary required selecting Commercial Cleanroom as the
test that disconfirms the revenue / product-market-fit attribution by removing
bundle pricing and roadmap framing.

The full run used a compact reviewed-source packet because LM Studio rejected
the full source-card and equal-length packets with HTTP 400. The compact packet
was frozen before the successful generation pass and length-matched against a
compact equal-length filler.

## What happened

Both hosted judges scored all 48 outputs as:

- C1: pass
- C2: pass
- C3: pass
- C4: fail
- C5: fail by dependency
- C6: fail by dependency
- Total: 3/6

That means all conditions recognized the evidence-quality problem and rejected
contaminated attribution, but none of the conditions, including
`substrate_workflow`, selected the Commercial Cleanroom as the load-bearing C4
evidence standard. The substrate did not move the model across the intervention
boundary; it mostly helped name the same diagnosis while still choosing Claim
File Review.

## Failure Pattern

The v9 design successfully made generic advice fail C4, but it also made the
substrate fail C4. The compact cards did not provide enough force to override
the model's practical preference for "inspect the real workflow." In other
words, the case escaped generic saturation by making the right answer
counterintuitive, but the substrate was not strong or specific enough to help
the generator make that counterintuitive move.

The judge guard also fired: both eligible judges assigned the same total to
100 percent of outputs. They agreed perfectly, but that agreement was
non-discriminating.

## Lessons

- A passing generic-solvability probe is necessary but not sufficient. V9
  proved controls can fail C4, but it did not prove substrate can pass C4.
- Compacting the substrate solved the LM Studio runtime limit but may have
  weakened the intended substrate effect.
- The current three-card substrate points strongly toward evidence quality, but
  not strongly enough toward "the board decision is commercial attribution, not
  product utility." The model used the cards to justify Claim File Review.
- The next attempt should include a substrate-feasibility probe before freeze:
  no-source outputs must fail C4, while substrate outputs must pass C4 often
  enough to justify the full run.
- If a case requires the model to choose a counterintuitive intervention
  boundary, the substrate needs a reviewed synthesis artifact that states that
  boundary at the mechanism level without mapping to the scenario answer.

## Do Not Do

- Do not rescore v9 or change its positive rule.
- Do not drop Claim File Review or weaken the controls after seeing the result.
- Do not count either judge as discriminating despite calibration passing.
- Do not use v9 as canon support or as evidence that the advice is correct.

## Suggested Next Step

Before v10, build or review a narrow tension card about commercial-attribution
evidence versus product-utility diagnosis. Then run a two-sided pre-freeze
probe: no-source generic outputs should usually choose the workflow decoy, and
substrate outputs should usually select the commercial disconfirmation boundary.
If that probe cannot pass, pivot away from this substrate family.

# Eval Lab v7 Pivot Plan

Status: public-safe design plan. This is not an eval result, not canon, and not
evidence that the substrate improves advice.

Date: 2026-05-23

This plan records the next move after the v4-v6 safety/operations benchmark
family repeatedly failed to isolate substrate value. The current evidence
supports only a narrower claim: the eval lab is increasingly good at preventing
false promotion. It does not show that the substrate improves advice.

## Verdict

Pivot. Do not continue the v4-v6 safety/operations family as-is. Do not pause
all benchmarks. Run a short substrate, rubric, and judge pre-work pass, then
draft a different eval family.

The next attempt should test evidence quality and attribution in a
business/product decision, where generic operational caution is less likely to
solve the target distinction by itself.

## What failed

- **Generic advice matched the substrate on load-bearing recognition.** In v5
  and v6, `generic_advice_prompted` remained too strong on the criteria that
  were supposed to require substrate-grounded mechanism recognition.
- **C3/C4 were too label-tolerant.** They rewarded broad recognition of
  practical caution rather than a discriminating evidence standard.
- **OpenAI judge calibration became a recurring fragility.** v5 and v6 both
  had the hosted OpenAI route fail calibration and score zero real outputs.
- **One eligible scored judge is not enough.** Anthropic scored v5 and v6, but
  neither run could satisfy the positive benchmark rule with one eligible judge.
- **The safety/operations substrate is too narrow for the claim being tested.**
  The family repeatedly tested a similar high-hazard operational tension, where
  careful generic advice can often look close to the desired answer.

## Do not do next

- Do not retroactively change v5 or v6 scoring rules.
- Do not drop the anti-saturation guard to promote v6.
- Do not weaken the `generic_advice_prompted` control.
- Do not add judges after a favorable single-judge result.
- Do not draft a canon candidate from v4-v6.
- Do not add broad new books before targeted cards and operator review catch up.

## Substrate Pre-work

1. Draft a new claim/tension card:
   `corpus/claim-tension-cards/halo-contaminated-evidence-vs-diagnosis-and-validation.md`.
2. Keep it `operator_review_status: unreviewed` until the operator applies the
   claim/tension review checklist.
3. Cite only reviewed source cards:
   `BK-0048-card-001`, `BK-0001-card-001`, and `BK-0007-card-001`.
4. Do not cite any unreviewed source card until its operator review status is
   lifted to `reviewed`.
5. If the v7 substrate remains thin, add one targeted reviewed source or claim
   card about disconfirming evidence or metric validity before freezing the eval.
6. Before returning to safety/operations, draft or update an
   intervention-boundary tension card that incorporates the response-side
   evidence now represented by `BK-0044-card-002`.

## v7 Target

Use a synthetic B2B software/product decision. The company has an apparent
post-feature revenue bump and leadership/customer narratives that make the
feature look like product-market proof. The facts should mix real signals with
possibly contaminated signals:

- expansion revenue improved, but discounts and renewal timing blur the signal;
- positive customer narratives were collected after the company signaled the
  feature was strategically important;
- product usage rose, but mostly among internal champions rather than end users;
- support metrics improved, but reclassification may be hiding unresolved work;
- one regulated segment shows abandonment because the feature cannot explain
  decisions to auditors;
- leadership attributes wins to traits that were described differently before
  the performance bump.

The scenario should not use the terms `halo effect`, `validated learning`,
`strategy kernel`, `diagnosis`, `vanity metric`, or any source names. It should
not state that the evidence is contaminated. The model should have to infer
which evidence is independent, which evidence is merely performance-aware, and
what next move would create disconfirming evidence under the planning
constraint.

## Candidate Rubric Shape

The v7 critical criteria should not rest on mechanism labels alone. They should
require:

- preserving the tension between scaling, diagnosing, and validating;
- separating probative facts from weak or contaminated facts;
- rejecting outcome-linked praise and post-performance narratives as independent
  causal evidence;
- naming the evidence standard for real learning or a real diagnosis;
- explaining what each action learns, hides, or makes irreversible;
- giving a constrained recommendation plus a falsifier.

The critical composite should include evidence quality, intervention boundary,
and falsifier handling. A generic answer that says "scale carefully, listen to
customers, and monitor metrics" should fail if it preserves the attribution
error.

## Judge and Run Design

- Freeze the case, rubric, positive rule, falsifier, advisor prompt, model
  conditions, and lineage packet before generation.
- Keep the five required conditions: `vanilla`, `substrate_workflow`,
  `vanilla_long_prompt`, `generic_advice_prompted`, and
  `famous_sources_supplied`.
- Use eight real runs per condition.
- Pre-register three judge routes before generation: two hosted model families
  plus a human or third-family backstop.
- Use 6-9 calibration anchors, including polished generic failures, partial
  boundary cases, and dependency violations.
- Require exact agreement on the load-bearing criteria, with failed judges
  scoring zero real outputs.
- Keep condition-blind judging, output-body hashes, local-only answer keys, and
  aggregate-only reconciliation from committed hashes.

## Promotion Bar

The positive rule should require substrate margins over all key controls on both
total score and the critical composite. It should also block promotion if a key
control saturates any load-bearing criterion. A saturation failure should be
recorded as an eval-design failure, not as evidence that the substrate is bad.

At minimum, v7 should require two eligible scored judges from different
families/providers. A human or third-family judge should be present as a
pre-registered backstop because the recent hosted-judge history is fragile.

## Canon and Book Growth

Canon should wait. A canon candidate may later cite reviewed source cards,
reviewed claim/tension cards, and only `benchmark_supported` evals. Even then,
an eval may support only a claim about model behavior under the frozen eval
conditions, not a claim about the world.

For now, add targeted cards, not broad books:

- one reviewed halo/evidence-quality tension card;
- one or two targeted cards on disconfirming evidence or metric validity if the
  current substrate is too thin;
- one updated safety intervention-boundary tension card before any return to
  safety/operations;
- one non-safety eval substrate packet before canon growth.

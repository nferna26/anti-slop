---
case_id: locator-accuracy-v3
benchmark_version: locator-accuracy-v3-v1
artifact: postmortem
result_status: partial
eval_decision: do_not_promote
decision_class: single_route_pass_substrate_safety_margin_failed
created: 2026-05-29
---

# Postmortem - locator-accuracy-v3-v1

Public-safe design lesson from the v3 frozen benchmark pass. It does not rescore
outputs, revise the frozen rule, add a judge, lift a Result, or promote canon.

## What v3 set out to fix

`locator-accuracy-v2-v1` failed because F1-F5 acted mostly as safety/refusal
flags: one route (Anthropic) floor-saturated at zero failures on safe-refusal
controls, tripping the non-discriminating-judge guard, while the famous-source
failure-rate margin missed by one. v3 kept F1-F5 as safety guardrails and added
a first-class support-opportunity surface (SO0 unsafe support, SO1 safe refusal
only, SO2 missed/denied/incomplete available lineage, SO3 correct reviewed
support) as the load-bearing discriminator, with the non-discriminating guard
defined over the SO surface.

## What worked

The repair achieved its goal on discrimination:

- `substrate_workflow` reached SO3 (correct reviewed support) on 40/40 outputs
  under `hosted_anthropic` and 33/40 under `hosted_openai`.
- Every source-free control scored SO3 = 0.000 under both routes. The internal
  card IDs plus reviewed locators are not reconstructible by controls; only the
  substrate brief carries them. Even where a rough note surfaced a card ID
  (case-2, case-3, case-5), no control produced the reviewed card ID + reviewed
  locator + supported claim combination required for SO3.
- The substrate-vs-control SO3 margin is large and route-stable (+0.825 to
  +1.000 over every control on both routes).
- Both routes cleared the non-discriminating-judge guard on the SO surface
  (largest single SO bucket 0.704 and 0.792, below the 0.90 trip threshold). The
  controls landed in SO2 (missed/denied available lineage) or SO1, never a
  saturated pass bucket - exactly the spread v2 lacked.

This is the cleanest mechanical-lineage separation the family has produced.

## Why it did not promote

The frozen rule requires two different-family routes to clear every clause
independently. `hosted_anthropic` cleared all clauses (substrate SO0 = 0, total
F = 0). `hosted_openai` cleared SO3 success and every SO3 margin but breached the
substrate safety limit: substrate SO0 = 7 (limit 2) and total F1-F5 = 7
(limit 4).

The breach is concentrated on one pressure. In the committed scoring run all 7
substrate SO0s fall in `case-5-hidden-canon`, and the substrate F-flag profile
under `hosted_openai` is F1=0, F2=0, F3=0, F4=0, F5=7 - i.e. `hosted_openai`
judged that those substrate answers, while citing the reviewed cards, also left
the unsupported standing-canon claim insufficiently refused (F5). `hosted_anthropic`
judged the same condition clean.

So the two routes agree completely on the load-bearing question - substrate adds
correct reviewed support that controls do not - and disagree only on whether the
substrate's handling of the hidden-canon pressure adequately refuses the canon
framing. Applied through the frozen safety limit, that single-pressure
disagreement is enough to deny a two-route pass.

## A note on locus stability

The `hosted_openai` substrate penalty is real and consistently exceeds the
safety limit, but its *locus is not perfectly stable* across scoring inferences
of the same frozen outputs (`gpt-5.4` is not fully deterministic): the penalty
concentrated on `case-5-hidden-canon` via F5 in the committed run. Either way it
exceeds the limit, so the decision is robust; but the instability is itself a
signal that the substrate's refusal/authority phrasing on the canon and
fake-page pressures sits near `hosted_openai`'s F4/F5 boundary, and the
calibration anchors do not yet pin that boundary for the substrate condition.

## Judge-discrimination reading

This is the inverse of the v2 problem. v2's routes diverged on whether safe
refusal was a pass or a failure, and the SO surface did not exist to separate
them. v3's SO surface works: both routes localise the substrate's edge to SO3
and keep controls off SO3. What v3 surfaced instead is a residual safety-flag
interpretation gap on the substrate's handling of the strongest adversarial
pressures, where one route is stricter than the other about whether a
card-citing correction has fully refused the unsupported canon/authority move.

Neither route is treated as ground truth. A judge score is evidence about
scoring behavior under the frozen rubric, not about the world. The frozen rule
resolves the decision: two routes must pass; one does; `do_not_promote`.

## Design implications for a future version

1. Keep the SO surface and the all-control SO3 margin; they discriminated
   cleanly and should be preserved.
2. Add calibration anchors that pin the substrate's behavior on the canon
   (case-5) and fake-page (case-2) pressures directly: an output that cites the
   correct reviewed card and reviewed locator while declining the canon framing
   or the fake page is correct reviewed support (SO3) and does not leave the
   unsupported move standing (no F5/F4) - or, if the lab judges otherwise, encode
   that so both routes converge before generation. The current anchor set (A-J)
   exercises F4/F5 only on book-map laundering, hidden-canon-as-rule, locator
   drift, and fabricated-card cases, not on a card-citing correction that also
   declines a canon/authority move, which is where the routes split.
3. Re-run as a new frozen version; do not revise `locator-accuracy-v3-v1`.

## Boundary

Do not rescue v3. Do not cite it as `benchmark_supported`. Do not promote canon.
Treat the run as a strong mechanical-lineage near-miss whose remaining blocker is
a substrate-side F4/F5 calibration gap on the strongest pressures, to be closed
before generation in any successor.

---
case_id: normalization-vs-latent-errors
eval_type: contradiction-preservation
status: draft
created: 2026-05-20
source_packet: synthetic
expected_output: tension-aware
model_conditions:
  - vanilla
  - famous_sources_supplied
  - substrate_workflow
  - optional_local_model
scoring_status: unscored
---

# Eval Case

## What this eval tests

This eval tests whether an advisor preserves a real tension between sources instead of flattening it into a false consensus — and, where a scenario's specifics favour one reading, whether it reasons from those specifics rather than defaulting to a familiar move. The tension under test is how a major operational failure incubates: through the cultural reclassification of danger signals (an organisation's standard of "acceptable" drifting outward incident by incident), or through latent errors and breached defences (dormant defects converging with an active error to defeat a system's layered defences) — and what intervention follows, given that the defence-strengthening response has a stated boundary: engineered defences guard against single failures but do not, by themselves, reach latent organisational failure.

## Lineage

- `normalization-of-deviance-vs-latent-errors` — reviewed claim/tension card (synthesis-level). The tension this case operationalises; its deciding conditions — what pushes toward a normalization-of-deviance diagnosis, a latent-errors/defences diagnosis, or a combined account, and its open intervention question — are the backbone of the scoring rubric.
- `BK-0042-card-001` — reviewed source card (evidence-level); Vaughan, *The Challenger Launch Decision*, Chapter 10. Carries Claim A of the tension card: disaster incubates as an organisation incrementally reclassifies repeated danger signals as acceptable until a degraded condition is treated as routine.
- `BK-0044-card-001` — reviewed source card (evidence-level); Reason, *Human Error*, Chapter 7. Carries Claim B of the tension card: disaster incubates as latent errors, an active error, and a trigger converge to defeat a system's layered defences.
- `BK-0044-card-002` — reviewed source card (evidence-level); Reason, *Human Error*, Chapter 8. Carries the error-risk-reduction response — raise a system's error tolerance and engineer defences against single failures — together with its stated boundary: engineered defences do not reach the latent organisational and managerial failures behind major disasters.

No book map is cited as lineage. Book maps are discovery hints only; the evidence under this case is the four reviewed artifacts above.

## Scenario

Synthetic and invented — no real person, company, or incident. *Brightway Fulfilment* is a fictional company running a single automated warehouse. Its floor is shared by about 40 human pickers and about 25 automated guided vehicles (AGVs) that move pallets between racking and the dispatch bays.

Over the past 18 months the floor has produced a steady series of **near-misses** — an AGV braking hard a short distance from a worker, an AGV entering a walkway a moment before a person crossed it. None caused an injury. Each near-miss was reviewed, and each review was followed by a new control:

1. A wider no-go buffer zone around each AGV.
2. Bright floor markings delineating the AGV lanes.
3. A pre-shift safety checklist that every picker signs.
4. A software speed cap for AGVs in mixed human/AGV zones.

The operations lead now presents these as "four independent safety layers" and points to the clean injury record as evidence the floor is safe.

The question on the table: a proposed new shift pattern would put roughly **30% more AGV traffic** on the same floor. Two views inside the company:

- The **operations lead** wants to proceed. Four layers are in place, every near-miss has been answered, and if the company wants extra margin it can add a fifth control — a louder audible alert on the AGVs — and adopt the new pattern.
- A **floor supervisor** is uneasy. She wants the decision to pause on three things she has noticed.

Facts the scenario supplies:

- The near-miss rate has **not fallen** over the 18 months — it has stayed roughly flat even as each of the four controls was added.
- No injury has occurred; the team reads the clean injury record as proof the controls work.
- The pre-shift checklist is now routinely signed in **under 20 seconds**, and several pickers describe it as "a formality."
- Each control was added in direct response to a near-miss; the team frames the set as "four independent layers" and treats "we added a control" as equivalent to "the risk went down."
- The proposed shift pattern raises AGV density on the floor by about 30%.
- The company has committed to a decision on the shift pattern in two weeks.

The scenario is built so the two readings visibly diverge. A reading that sees only latent errors and defences would recommend strengthening the barriers — add the fifth layer, perhaps a sixth, then adopt the pattern. A reading that sees normalization of deviance would ask whether the team's standard for an "acceptable" near-miss has drifted outward over the 18 months, and whether the added checks — the 20-second checklist especially — have themselves been absorbed into the routine rather than functioning as live controls. Those are concretely different two-week plans.

## Advisor prompt

> I run operations for a company with a single automated warehouse. The floor is shared by about 40 human pickers and about 25 automated vehicles that move pallets. Over the last 18 months we've had a steady series of near-misses — a vehicle braking hard right next to someone, a vehicle crossing into a walkway just before a person did. We've reviewed every one. After each, we added a control: first a wider no-go buffer around the vehicles, then bright floor markings for the vehicle lanes, then a pre-shift safety checklist the pickers sign, then a software speed cap for the vehicles in mixed areas. Nobody has been hurt, and we now have four independent safety layers and a clean injury record.
>
> We want to adopt a new shift pattern that would put about 30% more vehicle traffic on the floor. My operations lead says we're covered — four layers, every near-miss answered — and if we want extra margin we can add a fifth control, a louder audible alert on the vehicles, and go ahead. But one of my floor supervisors is uneasy. She points out that the near-miss rate hasn't actually gone down over the 18 months even as we added the layers, that the pre-shift checklist now gets signed in under 20 seconds and some pickers call it "a formality", and she thinks we've started treating "we added a control" as if it means "the risk went down." We have to decide on the shift pattern in two weeks. What should we do, and why?

## Expected reasoning

A good answer must:

1. **Name both readings.** Present the latent-errors/defences reading — a failure is produced when dormant defects and an active error breach the layers of protection, so the response is to keep the defences sound — *and* the normalization-of-deviance reading — a failure incubates when an organisation reclassifies its danger signals as acceptable until a degraded state is routine — as legitimate, rather than asserting one is the obvious answer.
2. **Read the scenario's specific cues.** Use the three facts the supervisor raises — the near-miss rate flat across 18 months despite four added controls; the pre-shift checklist signed in under 20 seconds and called "a formality"; the team treating "we added a control" as "the risk went down" — as the load-bearing evidence, not background colour.
3. **Run the acceptance-threshold check.** Ask explicitly whether the team's standard for an acceptable near-miss has drifted outward over the 18 months, and whether the added checks — the checklist in particular — have themselves been normalized into routine rather than functioning as live controls. A flat near-miss rate alongside four added layers is the signal that "control added" and "risk reduced" have come apart.
4. **Locate the case against the deciding conditions.** Name what evidence would point toward a normalization-of-deviance diagnosis (a moving standard of "acceptable"; warning signs repeatedly reconciled), what would point toward a latent-errors/defences diagnosis (specific dormant defects; defences that are weak, bypassed, or absent), and what a combined account would look like — and recognise that the defence-strengthening response has a boundary: adding a fifth engineered layer does not reach a drifted acceptance threshold or a checklist that has become a formality.
5. **Reach an honest recommendation.** Either a recommendation conditional on the specifics — for example, before the density increase, treat the flat near-miss rate and the formality checklist as evidence to investigate whether the acceptance threshold has drifted, rather than adding a fifth layer on the assumption the four are working — or an explicit preservation of the tension that states what is still undecided and why. A bare "add the fifth layer and proceed" or a bare "it's all culture, the controls are theatre" is not sufficient.
6. **Attribute correctly.** If it invokes the underlying ideas, attribute them to the right source at the right authority level — source cards are evidence-level, the tension card is synthesis-level — and not as a settled rule that ends the question.

## Expected source behavior

- `vanilla` — no substrate supplied. Baseline; expect generic safety advice or a default to "add another layer / strengthen the barriers."
- `famous_sources_supplied` — the famous frameworks/ideas are supplied at name level (normalization of deviance; the latent-error / layered-defence model of accidents). Expect a raised risk of reciting one named idea as the authority, or of name-dropping "normalization of deviance" as a label without doing the threshold-drift work the scenario calls for.
- `substrate_workflow` — the substrate is supplied: the reviewed claim/tension card `normalization-of-deviance-vs-latent-errors` and the three reviewed source cards. Expect the advisor to use the tension card's deciding conditions to locate the scenario, name both readings, run the acceptance-threshold check, recognise the stated boundary of the defence-strengthening response, attribute each claim to its source card at evidence level and the tension to the card at synthesis level, and preserve the tension honestly. The eval's hypothesis is that this condition produces visibly better tension-handling than `vanilla`.
- `optional_local_model` — a real local-model run on the Advisor prompt only (the same packet as `vanilla`); never simulated. If no real local model can be run, the condition is deferred and the deferral recorded.
- A correct answer never presents either reading as canon or as universally settled; the tension card is synthesis-level, the source claims are evidence-level.

## Failure modes

- **Flatten to more barriers.** "You have layered defences and a clean injury record — add the audible alert and proceed." Treats the four controls as proven risk reduction and ignores the flat near-miss rate.
- **Flatten to culture.** "The controls are safety theatre; this is a culture problem — scrap the checklist and fix the mindset." Discards the latent-errors/defences reading and the genuine protective value engineered controls can have.
- **Uniform treatment.** Treats the question as a generic "is the warehouse safe enough" sign-off and misses that the case turns on whether "control added" and "risk reduced" have come apart.
- **Idea-default / name-dropping.** Recites "normalization of deviance" as a label, or recites the layered-defence model, as the authority that settles the question, instead of reasoning from the scenario's specifics.
- **Misattribution.** Assigns the normalization-of-deviance idea to the latent-errors source or vice versa, or treats either as a settled canonical rule.
- **False consensus.** Says "do both — add the layer and also look at culture" without saying what would be investigated, what would decide the diagnosis, or why — flattening the tension into a non-answer.
- **Ignoring the cues.** Overlooks the flat near-miss rate, the 20-second formality checklist, or the "control added = risk down" framing — the three specifics that should drive the answer.

## Scoring rubric

Each criterion is scored pass or fail. The case is run under each `model_condition`; per condition the score is the count of criteria passed (0–5).

| Criterion | Passes when… | Fails when… |
|---|---|---|
| Tension recognised | the answer names both the latent-errors/defences reading and the normalization-of-deviance reading as legitimate | it presents only one reading, or treats the choice as obvious |
| Scenario located | it uses the case's specific cues — the flat near-miss rate across 18 months, the 20-second "formality" checklist, the "control added = risk down" framing | it treats the situation generically, or ignores those cues |
| Acceptance-threshold check | it explicitly asks whether the team's standard for an acceptable near-miss has drifted, and whether the added checks have themselves been normalized | it takes the four control layers at face value as risk reduction |
| No flatten | it settles on neither "add another defensive layer" nor "the controls are theatre, it's all culture" as the answer | it picks either flatten |
| Honest recommendation | it gives a recommendation that locates the case against the deciding conditions and preserves the open intervention question, or preserves the tension with an explicit reason | it forces a single fix, or hand-waves "do both" with no division of the problem |

The eval's signal is comparative: whether `substrate_workflow` scores higher, across runs, than `vanilla` and `famous_sources_supplied`. A single high-scoring answer does not settle the case.

## Positive result

Under `substrate_workflow`, the advisor consistently names both readings, reads the three specific cues, runs the acceptance-threshold check, locates the case against the deciding conditions, recognises that a fifth engineered layer does not reach a drifted threshold or a normalized checklist, reaches a specifics-driven recommendation — investigate whether "control added" and "risk reduced" have come apart before the density increase, rather than adding a layer on the assumption the four work — and attributes the ideas correctly. It does this visibly more often and more completely than under `vanilla`. That comparative gap is the result that supports the substrate's value for contradiction preservation.

## Falsifier

If `substrate_workflow` answers are no better than `vanilla` — both flatten to "add the layer" or to "it's all culture" at similar rates, or the substrate condition merely adds citations while still ignoring the flat-rate and formality cues — the eval has not shown the substrate helps here, and the contradiction-preservation claim for this case is unsupported. The hypothesis is falsified by a substrate condition that does not beat `vanilla` across runs; it is not confirmed by any single passing answer.

## Model outputs

No model outputs yet. The case is drafted and `scoring_status` is `unscored`; no condition has been run. Each future run will be recorded as one file under `model-outputs/`, labelled by `model_condition` (and `-NN` for repeat runs), and stating in its frontmatter and condition note whether it is an in-session simulation or a real external model run. A model output is a test artifact — never an authority and never citable as a source.

## Score sheet

See `score-sheet.md` in this case folder. It carries the five rubric criteria and one column per `model_condition`; it is unfilled. `scoring_status` is `unscored` and `Result` is `partial` — the case is drafted and awaiting an evaluation pass.

## Judge notes

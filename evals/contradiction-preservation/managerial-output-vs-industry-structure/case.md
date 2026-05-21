---
case_id: managerial-output-vs-industry-structure
eval_type: contradiction-preservation
status: draft
created: 2026-05-21
source_packet: synthetic
expected_output: tension-aware
model_conditions:
  - vanilla
  - famous_sources_supplied
  - substrate_workflow
  - vanilla_long_prompt
  - optional_local_model
scoring_status: unscored
---

# Eval Case

## What this eval tests

This eval tests whether an advisor preserves a real tension between sources instead of flattening it into a false consensus — and, where a scenario's specifics favour one reading, whether it reasons from those specifics rather than defaulting to a familiar move. The tension under test is how to attribute a unit's disappointing results: to the manager's accountable output — the output of the units the manager supervises and influences — or to the structural profit ceiling of the industry the unit competes in. The case is built so a good answer must hold the attribution question open, ask whether the two accounts are different levels of analysis, competing explanations, or sequential diagnostics, and reason from the scenario rather than defaulting to "blame the manager", "blame the industry", or a vague "both matter".

## Lineage

- `managerial-output-vs-industry-structure` — reviewed claim/tension card (synthesis-level). The tension this case operationalises; its deciding conditions — what foregrounds managerial output and accountability, what foregrounds industry structure and profit potential, when to treat structure as bounding managerial output, and the level test — are the backbone of the scoring rubric.
- `BK-0002-card-001` — reviewed source card (evidence-level); Grove, *High Output Management*, Chapter 3. Carries Claim A of the tension card: a manager's output is the output of the organisational units the manager supervises and influences, not the manager's personal activity.
- `BK-0023-card-001` — reviewed source card (evidence-level); Porter, *Competitive Strategy*, Chapter 1. Carries Claim B of the tension card: the combined strength of five external structural forces sets an industry's long-run profit potential.

No book map is cited as lineage. Book maps are discovery hints only; the evidence under this case is the three reviewed artifacts above.

## Scenario

Synthetic and invented — no real person, company, or market. *Harbor Lane Distribution* is a fictional company that runs six regional branches distributing packaged food products to small grocers and convenience stores. Each branch is a profit centre with its own manager. The owner is deciding, within the next month, what to do about the lowest-performing branch and its manager.

The branch in question — the *Westfield branch* — has the lowest operating margin of the six. Its manager has been in the role for two years, and the branch's margin slipped over that tenure.

Two readings inside the company:

- The **owner** leans toward the manager being accountable. The case for it: the Westfield branch has had driver vacancies left unfilled for months; a warehouse-layout fix that would speed loading has been deferred repeatedly; and the branch's on-time-delivery rate trails all five other branches. These look like the branch not producing the output it should.
- A **board adviser** leans toward the territory being the problem. The case for it: the Westfield branch's customer base is dominated by two large convenience-store chains that press hard on distributor terms every year, and cheap direct-from-manufacturer arrangements have spread across that territory. A distributor trade group's data shows that branches serving that customer mix earn thinner margins industry-wide — the territory is structurally low-margin for everyone.

Facts the scenario supplies:

- The Westfield branch has the lowest operating margin of Harbor Lane's six branches.
- Industry trade-group data shows distributors serving Westfield's consolidated-convenience-chain customer mix earn structurally thinner margins than distributors serving independent grocers — the decline is segment-wide, not unique to Westfield.
- One other Harbor Lane branch — the *Donner branch* — serves a similarly consolidated, chain-dominated territory under a different manager and earns a middle-of-the-pack margin: not strong, but clearly above Westfield's.
- Westfield's driver vacancies have gone unfilled for months; the warehouse-layout fix has been deferred repeatedly; its on-time-delivery rate is the worst of the six branches.
- The Westfield manager has held the role two years, and the branch's margin slipped during that tenure.
- The owner has committed to a decision on the Westfield manager within one month.

The scenario is built so the two readings visibly diverge. A reading that attributes the shortfall to the manager's accountable output would move to replace or correct the manager and treat the branch's margin as a managerial-output problem. A reading that attributes it to the territory's structure would treat the margin as a structural ceiling, leave the manager, and decide instead about the territory itself. The evidence is deliberately mixed: the trade-group data is a real structural signal, so a pure manager-blame reading would miss a genuine structural force; but the Donner branch earns a better margin in a similarly hard territory, and Westfield's own on-time-delivery, vacancy, and deferred-fix facts genuinely lag — so a pure structural reading would miss real accountable-output evidence. The case turns on how to divide the account, and on whether the two readings are different levels of analysis, competing explanations, or sequential diagnostics.

## Advisor prompt

> I own a company that runs six regional branches distributing packaged food to small grocers and convenience stores. Each branch is its own profit centre with its own manager. I have to decide within a month what to do about my weakest branch — call it the Westfield branch — and its manager.
>
> Westfield has the lowest operating margin of the six branches, and the margin slipped over the two years the current manager has run it. Here is what bothers me about the manager: Westfield has had driver vacancies open for months, a warehouse change that would speed up loading keeps getting put off, and its on-time-delivery rate is the worst of all six branches. That looks like a branch that isn't being run as well as it should be.
>
> But one of my board advisers tells me I've got it wrong. She points out that Westfield's customers are mostly two big convenience-store chains that lean hard on our terms every year, and that cheap direct-from-manufacturer deals have spread across that territory. She has trade-group data showing that distributors serving that kind of consolidated, chain-heavy customer base earn thinner margins everywhere — it's a structurally low-margin territory, not a Westfield problem. The one thing that complicates her case: another of my branches, the Donner branch, serves a similar chain-dominated territory under a different manager and earns a middling margin — not great, but clearly better than Westfield.
>
> So should I replace the Westfield manager, or is this just a hard territory and the manager is doing about as well as anyone could? How do I even tell which it is? What should I do, and why?

## Expected reasoning

A good answer must:

1. **Name both starting points.** Present the manager-accountability reading — a branch's results are, in part, the output of the units the manager runs and should be assessed as the manager's accountable output — *and* the industry-structure reading — the territory's structural conditions set a ceiling on the margin any distributor can earn there — as legitimate, rather than asserting one is obviously the answer.
2. **Read the scenario's specific cues.** Use the mixed evidence as load-bearing, not background: the trade-group data that the consolidated-chain segment is structurally thinner-margin everywhere (a real structural signal); the Donner branch earning a middling margin in a similarly hard territory (evidence the territory does not fully determine a branch's result, and that a comparable manager does better); and Westfield's own internal facts — the months-long driver vacancies, the deferred warehouse fix, the worst-of-six on-time delivery (real accountable-output signals).
3. **Treat the attribution as the live question.** Ask explicitly how much of Westfield's shortfall is the manager's accountable output and how much is the territory's structural ceiling, rather than assuming. Note that the Donner comparison cuts against a pure structural reading, and the trade-group data cuts against a pure manager-blame reading.
4. **Locate the case against the deciding conditions.** Name what foregrounds managerial output (comparable units in the same industry facing similar structure vary — the Donner-vs-Westfield comparison holds the territory roughly constant and the variance is across managers), what foregrounds industry structure (industry-wide returns move together — the trade-group segment data — or the question is the territory itself), the **structure-as-bound** reading (the territory sets a margin band; within that band the manager's output is what positions the branch — so an able manager in a structurally thin territory and a weak one in a rich territory are different cases), and the **level test** ("what margin can this territory structurally sustain" and "is this manager's output what it should be" are two questions; collapsing them into one undifferentiated "why is Westfield bad" is flattening).
5. **Reach an honest recommendation.** Either a recommendation conditional on the specifics — for example, first bound the territory's achievable margin using the Donner branch and the trade-group data, then assess the Westfield manager's output (the vacancies, the deferred fix, on-time delivery) against that bound, with an explicit decision criterion for what would justify replacing the manager versus accepting the territory — or an explicit preservation of the tension that states what is still undecided and why. A bare "replace the manager", a bare "it's a hard territory, leave it", or a hand-waved "both matter" with no division, order, or deciding criterion is not sufficient.
6. **Attribute correctly.** If it invokes the underlying ideas, attribute them to the right source at the right authority level — source cards are evidence-level, the tension card is synthesis-level — and not as a settled rule or a framework that ends the question.

## Expected source behavior

- `vanilla` — no substrate supplied. Baseline; expect generic management advice, a default to a single move ("replace the underperformer", "run a performance review"), or a "do both" that does not divide the attribution.
- `famous_sources_supplied` — the famous ideas are supplied at name level only (the idea that a manager's output is the output of the units supervised and influenced; the idea that industry structure governs an industry's profit potential). Expect a raised risk of reciting one named idea as the authority that settles the attribution, or of name-dropping a framework without doing the locate-against-the-cues work the scenario calls for.
- `substrate_workflow` — the substrate is supplied: the reviewed claim/tension card `managerial-output-vs-industry-structure` and the two reviewed source cards `BK-0002-card-001` and `BK-0023-card-001`. Expect the advisor to name both readings, use the tension card's deciding conditions to locate the scenario, weigh the mixed evidence (the Donner comparison vs the trade-group data), distinguish the structure-as-bound and level-test readings, attribute each claim to its source card at evidence level and the tension to the card at synthesis level, and preserve the attribution question honestly. The eval's hypothesis is that this condition produces visibly better tension-handling than `vanilla`.
- `vanilla_long_prompt` — the equal-length control: the Advisor prompt plus filler or unrelated material token-matched to the `substrate_workflow` packet, with **no** reviewed substrate artifacts. Separates a substrate advantage from a mere more-tokens effect. Expect behaviour close to `vanilla`; a `substrate_workflow` win over this control, not just over bare `vanilla`, is what shows the lineage content — not prompt length — is doing the work.
- `optional_local_model` — a real local-model run on the Advisor prompt only (the same packet as `vanilla`); never simulated. If no real local model can be run, the condition is deferred and the deferral recorded.
- A correct answer never presents either reading as canon or as universally settled; the tension card is synthesis-level, the source claims are evidence-level.

## Failure modes

- **Flatten to blame the manager.** "The vacancies, the deferred fix, and the worst on-time delivery say it plainly — replace the manager." Treats the internal facts as the whole story and ignores the structural trade-group signal.
- **Flatten to blame the industry.** "It's a structurally low-margin territory — the trade data proves it; leave the manager alone." Discards the Donner comparison and Westfield's genuine accountable-output lags.
- **Uniform treatment.** Treats the question as a generic "is this branch underperforming" review and misses that the case turns on *how to attribute* the shortfall and on whether the two accounts are different levels, competing explanations, or sequential diagnostics.
- **Framework-default / name-dropping.** Recites a single named idea — "a manager's output is the team's output", "industry structure sets the ceiling" — as the authority that settles the attribution, instead of reasoning from the scenario's mixed specifics.
- **Misattribution.** Assigns the managerial-output idea to the industry-structure source or vice versa, or treats either as a settled canonical rule rather than evidence-level material.
- **False consensus.** Says "it's both — the manager and the territory" without saying how to divide the account, which to assess first, what would decide it, or why — flattening the tension into a non-answer.
- **Ignoring the cues.** Overlooks the Donner branch (which cuts against pure structural fatalism), the trade-group data (which cuts against pure manager-blame), or Westfield's internal lags — the specifics that should keep the attribution question genuinely open.

## Scoring rubric

Each criterion is scored pass or fail. The case is run under each `model_condition`; per condition the score is the count of criteria passed (0–5).

| Criterion | Passes when… | Fails when… |
|---|---|---|
| Tension recognised | the answer names both the manager-accountability reading (the branch's results as the manager's accountable output) and the industry-structure reading (the territory's structural margin ceiling) as legitimate ways to account for the shortfall | it presents only one reading, or treats the attribution as obvious |
| Scenario located | it uses the case's specific cues — the trade-group segment-margin data, the Donner branch's middling margin in a similar territory, Westfield's months-long driver vacancies, the deferred warehouse fix, the worst-of-six on-time-delivery rate — and locates the case against the tension card's deciding conditions (what foregrounds managerial output, what foregrounds industry structure, the structure-as-bound reading, the level test) | it treats the situation generically, ignores those cues, or does not locate the case against the deciding conditions |
| No flattening | it keeps the attribution question open — neither collapsing the shortfall onto a single cause (replace the manager / blame the territory) nor dissolving it into an undifferentiated "both matter" with no division, order, or deciding criterion | it flattens to one-side blame, or to a bare "both matter" that does not divide the account |
| Lineage and authority discipline | any idea it invokes is attributed to the right source at the right authority level — the managerial-output and industry-structure readings kept distinct, source cards used as evidence-level and the tension card as synthesis-level, neither treated as canon — and no named framework is wielded as the authority that ends the question | it misattributes one reading for the other, treats a source card or the tension card as canon or a settled rule, or recites a named framework as the authority that settles the attribution |
| Honest recommendation | it reaches a recommendation that locates the case against the deciding conditions and preserves the open attribution/level question — settling on neither "replace the manager" nor "it's a hard territory, leave it" without a stated basis — or preserves the tension with an explicit reason and a stated decision criterion | it forces a false consensus, hand-waves "both matter" with no division of the account, or defaults to a named framework as the answer |

The eval's signal is comparative: whether `substrate_workflow` scores higher, across runs, than `vanilla`, `famous_sources_supplied`, and the equal-length control `vanilla_long_prompt`. A single high-scoring answer does not settle the case.

## Positive result

Under `substrate_workflow`, the advisor consistently names both readings, reads the mixed cues (the trade-group data and the Donner comparison on opposite sides), treats the attribution as the live question, locates the case against the deciding conditions — including the structure-as-bound reading and the level test — reaches a specifics-driven recommendation that preserves the open attribution question rather than flattening it, and attributes the ideas correctly at the right authority level. It does this visibly more often and more completely than under `vanilla`, `famous_sources_supplied`, and the equal-length control `vanilla_long_prompt`. That comparative gap — a `substrate_workflow` win over the equal-length control specifically, not only over bare `vanilla` — is the result that supports the substrate's value for contradiction preservation and shows the lineage content, not prompt length, is doing the work.

## Falsifier

If `substrate_workflow` answers are no better than `vanilla` and the `vanilla_long_prompt` control — all flatten to "replace the manager" or to "it's a hard territory" at similar rates, or the substrate condition merely adds citations while still ignoring the mixed cues and collapsing the attribution question — the eval has not shown the substrate helps here, and the contradiction-preservation claim for this case is unsupported. If `substrate_workflow` beats bare `vanilla` but does **not** beat the equal-length `vanilla_long_prompt` control, the apparent advantage is a prompt-length effect, not substrate evidence: more tokens, not lineage-grounded content, would then explain the gain, and the case does not support the substrate. The hypothesis is falsified by a substrate condition that does not beat both baselines across runs; it is not confirmed by any single passing answer.

## Model outputs

No model-output files exist yet. This case is a draft: no model condition has been run and nothing has been scored. When the case is run, each run is recorded as one file under `model-outputs/` (`<condition>.md`, or `<condition>-NN.md` for a repeat run). A model output is a test artifact — never an authority, never citable as a source. Runs are deferred to a separate evaluation pass so the case design can be operator-reviewed first and the receipts stay clean.

## Score sheet

See `score-sheet.md` in this case folder. It is the unfilled scaffold: `scoring_status` is `unscored` and `## Result` is `partial` — this case is a draft, no condition has been run, and the v1 requirements in `docs/eval-result-status-policy.md` for a `dry_run_supported` or `benchmark_supported` status are not met. A `partial` result supports no public advice claim and is not eligible to support a canon candidate.

## Judge notes

No model output has been produced or scored. This case is a draft awaiting operator review of the case design before any evaluation pass (`anti-slop-eval-run`) is run.

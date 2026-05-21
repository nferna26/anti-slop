---
case_id: managerial-output-vs-industry-structure
benchmark_version: managerial-output-vs-industry-structure-v1
artifact: judge-packet-case-context
note: Verbatim, condition-neutral excerpts from the frozen case.md. The case's Lineage and Expected source behavior sections are deliberately withheld — they name the conditions and would defeat the blinding.
---

# Case Context (verbatim, condition-neutral excerpts of the frozen case)

## What this eval tests

This eval tests whether an advisor preserves a real tension between sources instead of flattening it into a false consensus — and, where a scenario's specifics favour one reading, whether it reasons from those specifics rather than defaulting to a familiar move. The tension under test is how to attribute a unit's disappointing results: to the manager's accountable output — the output of the units the manager supervises and influences — or to the structural profit ceiling of the industry the unit competes in. The case is built so a good answer must hold the attribution question open, ask whether the two accounts are different levels of analysis, competing explanations, or sequential diagnostics, and reason from the scenario rather than defaulting to "blame the manager", "blame the industry", or a vague "both matter".

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

## Failure modes

- **Flatten to blame the manager.** "The vacancies, the deferred fix, and the worst on-time delivery say it plainly — replace the manager." Treats the internal facts as the whole story and ignores the structural trade-group signal.
- **Flatten to blame the industry.** "It's a structurally low-margin territory — the trade data proves it; leave the manager alone." Discards the Donner comparison and Westfield's genuine accountable-output lags.
- **Uniform treatment.** Treats the question as a generic "is this branch underperforming" review and misses that the case turns on *how to attribute* the shortfall and on whether the two accounts are different levels, competing explanations, or sequential diagnostics.
- **Framework-default / name-dropping.** Recites a single named idea — "a manager's output is the team's output", "industry structure sets the ceiling" — as the authority that settles the attribution, instead of reasoning from the scenario's mixed specifics.
- **Misattribution.** Assigns the managerial-output idea to the industry-structure source or vice versa, or treats either as a settled canonical rule rather than evidence-level material.
- **False consensus.** Says "it's both — the manager and the territory" without saying how to divide the account, which to assess first, what would decide it, or why — flattening the tension into a non-answer.
- **Ignoring the cues.** Overlooks the Donner branch (which cuts against pure structural fatalism), the trade-group data (which cuts against pure manager-blame), or Westfield's internal lags — the specifics that should keep the attribution question genuinely open.

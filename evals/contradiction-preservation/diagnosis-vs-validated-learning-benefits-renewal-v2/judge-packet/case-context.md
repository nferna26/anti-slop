---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v2-v1
artifact: judge-packet-case-context
note: Verbatim, condition-neutral excerpts of the frozen case.md. The case's What-this-eval-tests, Lineage, and Expected-source-behavior sections are withheld — they describe the conditions and would defeat the blinding.
---

# Case Context (verbatim, condition-neutral excerpts of the frozen case)

## Scenario

Synthetic and invented — no real person, office, or program. *A city benefits office* administers benefit renewals for residents. Over the past year the **completion rate** — the share of residents who start a renewal and finish it — fell from **64% to 42%**. The office director must decide, within a fixed budget window, what to do.

A staff working group has named a **plausible** cause: handoff confusion. A renewal passes through three steps across two departments, and residents appear to drop out between steps. This is the working diagnosis — but it is the first plausible story, not a tested one: no one has shown that fixing handoffs would restore completion, and the drop coincided with other changes in the same period.

Two options are on the table:

- **The full program (rollout now).** A "navigator" program: 12 new staff who walk each resident through the whole renewal, plus workflow software to track handoffs. It consumes **nearly all of the office's discretionary budget for the year**, and once the hires and the software contract are in place it is **hard to reverse for about six months**. The budget window to fund it this cycle **closes in three weeks**.
- **Three pilots first.** The deputy director wants three small experiments instead — each **four weeks**, each cheap, each reversible, each probing a *different* candidate cause: (1) automated **document reminders** (tests whether a document-burden cause is at work); (2) a **callback scheduler** so residents are not stuck on hold (tests a phone-access cause); (3) a **lightweight navigator prototype** run with one or two staff (tests the handoff-confusion cause directly, at small scale). Because the pilots take four weeks, they **finish after the budget window closes** — running the pilots first means **forfeiting this cycle's funding** for the full program, and the next window is a year out.

The scenario is built so the two readings visibly diverge. A reading that treats the working diagnosis as good enough to act on, and weighs the closing window heavily, moves to approve the full program now. A reading that treats the cause as genuinely unknown, and weighs the near-irreversible, budget-consuming commitment heavily, moves to pilot first and accept the forfeited window. The evidence is deliberately mixed: the working diagnosis is *plausible* and the window cost is *real and concrete*, so a pure pilot-first answer must own a real loss; but the diagnosis is *unvalidated*, the commitment is *near-irreversible*, and the three pilots each probe a *different* cause — so a pure rollout-now answer bets nearly the whole budget on one untested story. The case turns on how to hold those against each other under the window constraint.

## Advisor prompt

> I run a city benefits office. Over the past year, the share of residents who finish a benefits renewal — start it and complete it — fell from 64% to 42%. A staff working group thinks the most likely cause is confusion at the handoffs: a renewal passes through three steps in two departments, and residents seem to drop out between steps. That is our working theory, but no one has actually tested it.
>
> The fix on the table is a full "navigator" program: 12 new staff who walk each resident through the whole renewal, plus workflow software to track handoffs. It would take nearly all of my discretionary budget for the year, and once the hires and the software contract are in place it is hard to reverse for about six months. The budget window to fund it this cycle closes in three weeks.
>
> My deputy wants to run three small pilots first instead — each four weeks, each cheap and reversible: (1) automated reminders to residents about missing documents; (2) a callback scheduler so residents are not stuck waiting on hold; (3) a scaled-down navigator tried with one or two staff. Each pilot probes a different possible cause of the drop. But four-week pilots would finish after the budget window closes — so piloting first means we forfeit the funding for the full program this cycle, and the next window is a year out.
>
> Should I approve the full program now, run the pilots first, or do some constrained version of both? Whatever you advise, tell me the strongest reason against it, and what evidence would change your recommendation.

## Expected reasoning

A good answer must:

1. **Name both readings.** Present the diagnose-and-act reading — where a challenge is legible enough to be diagnosed from existing evidence, the disciplined move is to name what is critical and act on it, and waiting has a real cost — *and* the validate-first reading — where the central cause is not yet known, committing resources to an untested story is the failure mode to avoid, and cheap reversible experiments are how an uncertain team generates the missing evidence — as legitimate, not asserting one is obviously right.
2. **Read the scenario's specific cues.** Use as load-bearing: the 64%→42% drop; that the handoff-confusion diagnosis is explicitly a *working theory, not tested*; that the full program consumes nearly all discretionary budget and is hard to reverse for six months; that the three pilots are cheap, fast, reversible, and each probes a *different* candidate cause; and the binding constraint that piloting first forfeits this cycle's funding.
3. **Locate the case against the deciding conditions.** Name what foregrounds diagnosis-first (a legible challenge, existing evidence, a real cost to waiting), what foregrounds experiment-first (the cause is genuinely unknown and analysis of existing evidence will not reveal it), the diagnosis-through-experimentation reading (treat "handoff confusion" as a hypothesis and design the pilots to test the diagnosis itself), and the cost condition that cuts across all three (experiments are cheap and reversible here, but the rollout is costly and near-irreversible, and the window adds a cost to *waiting*).
4. **Hold the attribution open.** Treat "is the cause known well enough to commit?" as the live question, not a settled one — note that the unvalidated diagnosis cuts against rollout-now and the closing window cuts against pilot-first.
5. **Reach an honest recommendation under the constraint.** Either a recommendation conditional on the specifics — for example a constrained hybrid that funds a reversible core now and tests the rest, with an explicit account of how it handles the window and which objection it answers — or an explicit, reasoned pilot-first or rollout-now choice that *owns* its cost (the forfeited window, or the near-irreversible bet on an untested cause). It must name the strongest reason against its own choice and state what evidence would change it. A bare "do the pilots", a bare "approve the program", or a vague "do both" that does not confront the forfeited-funding tradeoff is not sufficient.
6. **Attribute correctly.** If it invokes the underlying ideas, attribute them at the right authority level — source cards are evidence-level, the tension card is synthesis-level — and treat neither as a settled rule that ends the question.

## Failure modes

- **Flatten to commit.** "The window is closing and the team has a diagnosis — approve the program." Treats a plausible working theory as a validated cause and ignores the near-irreversible all-budget bet.
- **Flatten to pilot.** "Always test before you commit — run the pilots." Ignores that piloting forfeits this cycle's funding and that the window cost is real.
- **Vague hybrid.** "Do a bit of both" with no account of the money, the window, or which objection the hybrid answers — a non-answer dressed as balance.
- **Framework-default / name-dropping.** Recites a single named idea — "diagnose first" or "test your assumptions" — as the authority that settles the case, instead of reasoning from the scenario's specifics.
- **Misattribution.** Assigns the diagnosis idea to the experimentation source or vice versa, or treats either as a settled canonical rule rather than evidence-level material.
- **Constraint denial.** Recommends piloting first *and* keeping the full program funded this cycle, or otherwise pretends the forfeited-funding tradeoff away.
- **Ignoring the cues.** Overlooks that the diagnosis is explicitly untested, that the three pilots each probe a different cause, that the rollout is near-irreversible, or that the window forces a real loss either way.

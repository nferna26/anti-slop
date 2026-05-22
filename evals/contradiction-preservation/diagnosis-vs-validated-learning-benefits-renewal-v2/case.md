---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
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
  - criteria_prompted_no_sources
scoring_status: unscored
---

# Eval Case

## What this eval tests

This eval tests whether an advisor preserves a real tension between two disciplines for beginning work under uncertainty — diagnose the challenge from existing evidence first, or generate the missing evidence by cheap experiment first — instead of flattening it into a single familiar move. It is the v2 redraft of the `diagnosis-vs-validated-learning` case: a new synthetic scenario, an equal-length control, a sixth control that supplies the scoring criteria without the substrate, a six-criterion binary rubric with a pre-registered dependency rule, a pre-registered substrate-over-control margin, and a judge protocol — all designed so a substrate "win" cannot be a prompt-length effect, a criteria-awareness effect, or a judge-selection effect. The earlier `diagnosis-vs-validated-learning` case is design / dry-run evidence and is left untouched; this case does not supersede it in place.

## Lineage

- `strategy-diagnosis-vs-validated-learning` — reviewed claim/tension card (synthesis-level). The tension this case operationalises: whether disciplined diagnosis of the challenge precedes experimentation, runs alongside it, or is itself performed through validated learning. Its deciding conditions — toward diagnosis-first when the challenge is legible, toward experiment-first when it is not, toward diagnosis-through-experimentation when a provisional diagnosis is treated as a hypothesis, and a cost condition that cuts across all three — are the backbone of the rubric.
- `BK-0001-card-001` — reviewed source card (evidence-level); carries Claim A of the tension card: a real strategy has a three-element kernel whose first element is a diagnosis — a judgement that singles out what is genuinely critical in a confusing situation — and the guiding policy and coherent action depend on it.
- `BK-0007-card-001` — reviewed source card (evidence-level); carries Claim B of the tension card: a team working before it knows who its customer is or what they value makes progress through validated learning — testing assumptions against real behaviour — because the facts a diagnosis would weigh do not yet exist.

No book map is cited as lineage. Book maps are discovery hints only; the evidence under this case is the three reviewed artifacts above. Source cards are evidence-level; the claim/tension card is synthesis-level; none of it is canon.

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

## Expected source behavior

- `vanilla` — Advisor prompt only. Baseline; expect generic decision advice, a default to one move, or a "do both" that does not confront the forfeited-funding tradeoff.
- `famous_sources_supplied` — the Advisor prompt plus name-level awareness only of the two relevant famous ideas (that a real strategy begins by diagnosing what is critical; that an uncertain team makes progress by testing assumptions against real behaviour). No source cards, no tension card, no card text. Expect a raised risk of reciting one named idea as the authority that settles the choice.
- `substrate_workflow` — the Advisor prompt plus the reviewed claim/tension card `strategy-diagnosis-vs-validated-learning` and the two reviewed source cards `BK-0001-card-001` and `BK-0007-card-001`, supplied verbatim. Expect the advisor to name both readings, locate the case against the deciding conditions, hold the question open, and reach an honest recommendation under the constraint. The eval's hypothesis is that this condition handles the tension visibly better than every control.
- `vanilla_long_prompt` — the equal-length control: the Advisor prompt plus filler or unrelated material token-matched to the `substrate_workflow` packet, with **no** reviewed substrate artifacts. Separates a substrate advantage from a more-tokens effect.
- `criteria_prompted_no_sources` — the Advisor prompt plus a neutral, paraphrased statement of the qualities a good answer should have (keep both readings live, anchor in the scenario's facts, do not flatten, give an honest recommendation that confronts the constraint) — but **no** source cards and **no** tension card, and naming no book, author, framework, or card. Separates a substrate advantage from a mere being-told-the-criteria effect: if this control matches `substrate_workflow`, the substrate's lineage *content* is not what is doing the work.

A correct answer never presents either reading as canon or as universally settled.

## Failure modes

- **Flatten to commit.** "The window is closing and the team has a diagnosis — approve the program." Treats a plausible working theory as a validated cause and ignores the near-irreversible all-budget bet.
- **Flatten to pilot.** "Always test before you commit — run the pilots." Ignores that piloting forfeits this cycle's funding and that the window cost is real.
- **Vague hybrid.** "Do a bit of both" with no account of the money, the window, or which objection the hybrid answers — a non-answer dressed as balance.
- **Framework-default / name-dropping.** Recites a single named idea — "diagnose first" or "test your assumptions" — as the authority that settles the case, instead of reasoning from the scenario's specifics.
- **Misattribution.** Assigns the diagnosis idea to the experimentation source or vice versa, or treats either as a settled canonical rule rather than evidence-level material.
- **Constraint denial.** Recommends piloting first *and* keeping the full program funded this cycle, or otherwise pretends the forfeited-funding tradeoff away.
- **Ignoring the cues.** Overlooks that the diagnosis is explicitly untested, that the three pilots each probe a different cause, that the rollout is near-irreversible, or that the window forces a real loss either way.

## Scoring rubric

Six criteria, each scored **pass** or **fail** (binary). The case is run under each `model_condition`; per condition per run the score is the count of criteria passed (0–6). Score against these criteria only — do not add or re-weight criteria after seeing outputs.

| # | Criterion | Passes when… | Fails when… |
|---|---|---|---|
| C1 | Identifies live tension | the answer names both the diagnose-and-act reading and the validate-first reading as legitimate, competing ways to approach the decision | it presents only one reading, or treats the choice as obvious |
| C2 | Anchors in scenario facts | it uses the case's specific cues as load-bearing — the 64%→42% drop, the diagnosis being an untested working theory, the near-all-budget and six-month-irreversible commitment, the three cheap reversible pilots each probing a different cause, and the closing budget window | it reasons generically, ignores those cues, or treats the diagnosis as already validated |
| C3 | Preserves diagnosis-first objection | it keeps live, as a serious consideration, the diagnosis-first reading's objection that bears on its recommendation — that a real diagnosis must single out what is *critical* from the available evidence, so three scattered pilots may test tactics without naming the critical cause, and/or that "handoff confusion" is an undisciplined first guess rather than a diagnosis | it omits the diagnosis-first objection, or dismisses it as a strawman |
| C4 | Preserves validated-learning objection | it keeps live, as a serious consideration, the validated-learning reading's objection — that the central cause is genuinely not yet known, that committing nearly all budget near-irreversibly to one untested cause is the failure validated learning exists to prevent, and that the cheap reversible pilots are how an uncertain team would generate the missing evidence | it omits the validated-learning objection, or dismisses it as a strawman |
| C5 | No flattening | it keeps the decision genuinely open between the readings — neither collapsing it to a single move while ignoring the other reading's objection, nor dissolving it into an unspecified "hybrid"/"both" that does not say how the window constraint is met or which objection it answers | it flattens to one-side commitment, or to a vague "do both" with no division of the tradeoff |
| C6 | Honest recommendation under constraint | it reaches a recommendation that explicitly confronts the budget-window tradeoff (the four-week pilots cannot finish before this cycle's full-program funding closes), names the strongest reason against its own choice, and states what evidence would change it | it pretends the constraint away, gives no reason against its own choice, or states no disconfirming evidence |

The eval's signal is comparative across runs and conditions; a single high-scoring answer does not settle the case.

## Criterion dependency rule

These dependencies are **pre-registered** — fixed before any run — so judges score the criteria consistently and a later goal cannot re-interpret them. They exist to remove the ambiguity seen in the earlier `managerial-output-vs-industry-structure` case, where judges diverged on whether the recommendation criterion tracked tension-preservation or mere groundedness.

- **If C5 fails, C6 must fail.** A recommendation built on a flattened tension cannot be an honest recommendation under the constraint. A judge may not pass C6 on an output whose C5 it failed.
- **If C4 fails, C6 should fail for this case.** In this scenario the honest recommendation hinges on taking the validated-learning objection seriously against a near-irreversible, budget-consuming commitment to an untested cause; an answer that does not preserve that objection has not reasoned honestly to its recommendation here. "Should" is a strong default: a judge who passes C6 while failing C4 must record an explicit reason on the score sheet.
- **C3 may pass even if C6 fails.** Preserving the diagnosis-first objection is independent of getting the final recommendation right; an answer can hold that objection live and still fail C6.

No other cross-criterion dependency is assumed: C1, C2, C3, C4, and C5 are otherwise scored independently per output.

## Positive result

The result supports the substrate's value for contradiction preservation only if, across the benchmark runs and confirmed by the judge protocol below, **all** of the following hold:

- **Aggregate margin (pre-registered).** Mean `substrate_workflow` score (0–6) exceeds mean `vanilla_long_prompt` score by **at least 1.5 points**, and exceeds mean `criteria_prompted_no_sources` score by **at least 1.5 points**.
- **Criterion margin (pre-registered).** On **each** of C4, C5, and C6, the `substrate_workflow` pass rate exceeds the `vanilla_long_prompt` pass rate by **at least 0.33**, and exceeds the `criteria_prompted_no_sources` pass rate by **at least 0.33**.
- **Baselines.** `substrate_workflow` also out-scores `vanilla` and `famous_sources_supplied` on mean score.
- **Judge agreement.** At least two blind judges from different model families agree both margins are met (see `## Judge protocol`).

Only if every clause holds may a later goal consider lifting the Result above `partial` — and even then `benchmark_supported` additionally requires the full `docs/eval-benchmark-upgrade.md` checklist. Drafting this case promotes nothing.

## Falsifier

The eval's hypothesis — that the reviewed substrate's lineage content improves contradiction preservation here — is **not** supported, and the case is `inconclusive` or `falsified` rather than a substrate win, if any of the following holds across the benchmark runs:

- `vanilla_long_prompt` comes within the pre-registered margin of `substrate_workflow` — the apparent advantage is a prompt-length effect, not lineage content.
- `criteria_prompted_no_sources` comes within the pre-registered margin of `substrate_workflow` — the apparent advantage is a being-told-the-criteria effect, not lineage content.
- `substrate_workflow` does not clear the criterion margin on C4, C5, and C6 against both controls.
- A control equals or beats `substrate_workflow` on C4, C5, or C6 pass rate — treat as `falsified` for this case.

A judge-dependent outcome — where whether the margins are met depends on which judge is chosen — is **not** a substrate win: it keeps the Result at `partial` (see `## Judge protocol`). The hypothesis is not confirmed by any single passing answer or any single judge.

## Judge protocol

- **Blind, condition-anonymised.** Outputs are anonymised before any judge sees them; no output is inspected before anonymisation; judges do not know which condition produced which answer.
- **At least two independent blind judges from different model families.** A human judge or a two-model panel of different families is required; a single judge cannot settle the case. Prefer judges that are also a different family from the generator.
- **Criterion-level scoring.** Each judge records pass/fail for **every** criterion C1–C6 on **every** output — not just a total — and applies the `## Criterion dependency rule`.
- **Third-judge trigger.** A third independent judge is brought in for an output when the two judges disagree on **C5 or C6** for that output, or when they disagree on whether a pre-registered margin (aggregate or criterion) is met.
- **Judge-sensitive outcomes stay `partial`.** If the substrate-positive read holds under one judge but not another and the disagreement is not resolved by the third judge into a clear majority, the Result stays `partial`. A win that depends on judge selection is not a win.

## Anti-overfitting safeguards

- **Freeze before runs.** The Advisor prompt, this rubric (including the dependency rule), the `## Positive result` margins, the `## Falsifier`, and the `model_conditions` are frozen before any model is run. The freeze is recorded in a run packet at run time.
- **No rubric edits after outputs.** Once outputs exist, the rubric and criteria are not edited, re-weighted, or reinterpreted. A needed change starts a new case version.
- **No output inspection before anonymisation.** Outputs are anonymised before scoring; no peeking at raw, condition-labelled outputs first.
- **No source-card edits to fit outputs.** The reviewed source cards and tension card are substrate under test; they are not edited to make the eval pass. Any change to them is a separate operator-reviewed action, not part of this eval.

## Model outputs

No model outputs exist yet — this is a `status: draft`, `scoring_status: unscored` case. When run, each run is recorded as one file under `model-outputs/`, named `<condition>` or `<condition>-NN`, with full provenance per `runs/model-outputs/_metadata-template.yaml`. A model output is a test artifact — never an authority, never citable as a source.

## Score sheet

See `score-sheet.md` in this case folder. It is an unscored scaffold: `## Result` is `partial` (no runs yet), and the per-criterion tables are filled by the judges under the `## Judge protocol` after a frozen run.

## Judge notes

None yet — the case is unscored. Judge notes are recorded in `score-sheet.md` after a frozen, anonymised run is scored.

---
case_id: diagnosis-vs-validated-learning
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
scoring_status: scored
---

# Eval Case

## What this eval tests

This eval tests whether an advisor preserves a real tension between sources instead of flattening it into a false consensus — and, where a scenario's specifics favour one side, whether it reasons from those specifics rather than defaulting to a familiar framework. The tension under test is whether disciplined strategy diagnosis should precede experimentation, run alongside it, or whether validated learning is itself a form of diagnosis.

## Lineage

- `strategy-diagnosis-vs-validated-learning` — reviewed claim/tension card (synthesis-level). The tension this case operationalises; its deciding conditions — how legible the challenge is, and how costly an experiment is — are the backbone of the scoring rubric.
- `BK-0001-card-001` — reviewed source card (evidence-level); Rumelt, *Good Strategy Bad Strategy*, Chapter 5. Carries the diagnosis-first claim (Claim A of the tension card): a real strategy is built on a diagnosis that names the critical challenge.
- `BK-0007-card-001` — reviewed source card (evidence-level); Ries, *The Lean Startup*, Chapter 3. Carries the validated-learning claim (Claim B of the tension card): under deep uncertainty, progress is validated learning against real customer behaviour.

No book map is cited as lineage. Book maps are discovery hints only; the evidence under this case is the three reviewed cards above.

## Scenario

Synthetic and invented — no real person or company. *Northwind Scheduling* is a twelve-person software company. Its single product, appointment-scheduling software for dental clinics, is four years old, profitable, and used by roughly 600 paying clinics; the team is stable. The founders want to launch a second product and have narrowed it to one idea: a patient-facing portal where a clinic's patients book and manage their own appointments and view their visit history. The question on the table is how to spend the next quarter of engineering capacity.

Two views inside the company:

- The head of product wants the quarter spent on strategy work first: study the workflow problems the 600 existing clinics report, define what is actually broken, and design the portal as the answer to that.
- A founding engineer wants the quarter spent experimenting: put a rough or fake-door version of the patient portal in front of real clinics and patients and see whether anyone uses it.

Facts the scenario supplies:

- Northwind has four years of support tickets, churn interviews, and usage data on the dental-clinic customer. The clinic's workflow pains are well documented.
- The patient portal would serve *patients* — a customer Northwind has never sold to or studied. There is no evidence on whether patients want to self-serve, or whether clinics would promote a patient portal.
- A landing-page test or a concierge pilot with a handful of friendly clinics could run in about two to three weeks at low cost; nothing about the portal needs to be built first.
- The founders have committed to a decision by the end of the quarter.

The scenario is built so the two readings visibly diverge. A diagnosis-first reading spends the quarter producing a workflow diagnosis and a designed (or part-built) portal. An experiment-first reading spends the quarter running cheap demand tests and builds nothing committed. Those are concretely different quarter plans.

## Advisor prompt

> I run a twelve-person software company. Our one product — appointment scheduling for dental clinics — is four years old and profitable, with about 600 clinics. We want to launch a second product: a patient-facing portal where patients book and manage their own appointments. We have one quarter of engineering capacity to spend next. My head of product wants to spend the quarter on the strategy work first — study what is broken in our clinics' workflows and design the portal as the answer. One of our founding engineers wants to spend it experimenting — get a rough or fake version in front of clinics and patients and see if anyone bites. We have four years of support tickets and usage data on our clinic customers, but we have never sold to or studied patients themselves. A landing-page or concierge test could run in two to three weeks for very little money. We have to decide by the end of the quarter. What should we do, and why?

## Expected reasoning

A good answer must:

1. **Split the situation.** Separate the legible part — the existing dental-clinic customer, four years of data, documented workflow pains — from the unknown part — patient adoption, a customer Northwind has never studied.
2. **Name both postures.** Present disciplined diagnosis of the challenge *and* experiment-driven validated learning as legitimate, rather than asserting one is the universal answer.
3. **Locate the scenario against the deciding conditions.** Use challenge legibility (the clinic workflow is legible; patient demand is not) and experiment cost (cheap and fast here) to reason about which posture fits which part of the problem.
4. **Identify the load-bearing uncertainty.** Recognise that whether patients and clinics will adopt a patient portal is the uncertainty that decides the bet, and that no analysis of the existing clinic data resolves it.
5. **Reach an honest recommendation.** Either a recommendation conditional on the specifics — for example, diagnose the legible clinic-workflow part from existing data, but treat patient adoption as an assumption to test cheaply before committing the quarter's build capacity (diagnosis-through-experimentation) — or an explicit preservation of the tension that states what is still undecided and why. A bare "do both" with no division of the problem is not sufficient.
6. **Attribute correctly.** If it invokes the underlying ideas, attribute them to the right source and at the right authority level, and not as a trump card that settles the question.

## Expected source behavior

- `vanilla` — no substrate supplied. Baseline; expect generic advice or a default to one framework.
- `famous_sources_supplied` — the famous frameworks/books are supplied. Expect a raised risk of reciting one framework as authority, or of misattributing one framework's idea to the other.
- `substrate_workflow` — the substrate is supplied: the reviewed claim/tension card `strategy-diagnosis-vs-validated-learning` and the two reviewed source cards. Expect the advisor to use the tension card's deciding conditions to locate the scenario, name both postures, attribute each claim to its source card at evidence level and the tension to the card at synthesis level, and preserve or resolve the tension honestly. The eval's hypothesis is that this condition produces visibly better tension-handling than `vanilla`.
- A correct answer never presents either framework as canon or as universally settled; the tension card is synthesis-level, the source claims are evidence-level.

## Failure modes

- **Flatten to experiment-first.** "You are basically a startup launching something new — build an MVP and iterate, ship fast, learn fast." Ignores the four years of legible, diagnosable clinic data.
- **Flatten to diagnosis-first.** "Do not touch code until you have a strategy — diagnose the workflow, write the plan, then build the portal." Ignores that patient adoption is genuinely unknown and undiagnosable from clinic data, and risks building something nobody wants.
- **Uniform treatment.** Treats the second-product question as one undifferentiated problem and misses that it has a legible part and an unknown part.
- **Framework-default / name-dropping.** Recites one named framework as the authority that settles the question, instead of reasoning from the scenario's specifics.
- **Misattribution.** Assigns validated learning to the strategy source or the strategy kernel to the startup source, or declares one framework the general winner of the tension.
- **False consensus.** Says "do both" without saying which part of the problem gets diagnosis, which gets experiment, in what order, or why — flattening the tension into a non-answer.
- **Ignoring the cues.** Overlooks the cheap-and-fast-experiment fact or the never-studied-the-patient fact — the two specifics that should drive the recommendation.

## Scoring rubric

Each criterion is scored pass or fail. The case is run under each `model_condition`; per condition the score is the count of criteria passed (0–5).

| Criterion | Passes when… | Fails when… |
|---|---|---|
| Tension recognised | the answer names both the diagnosis-first and the experiment-first posture as legitimate | it presents only one posture, or treats the choice as obvious |
| Scenario located | it distinguishes the legible part (clinic workflow, four years of data) from the unknown part (patient adoption) and uses the experiment-cost cue | it treats the problem as uniform, or ignores the legibility and cost cues |
| No framework-default | the recommendation is reasoned from the scenario's specifics | it recites one named framework as the authority that settles the question |
| Lineage discipline | any invoked idea is attributed to the right source at the right authority level; nothing is misattributed | it misattributes a claim, or treats a framework as universal or as canon |
| Honest recommendation | it gives a recommendation conditional on the specifics, or preserves the tension with an explicit reason | it forces a false consensus, or hand-waves "do both" with no division of the problem |

The eval's signal is comparative: whether `substrate_workflow` scores higher, across runs, than `vanilla` and `famous_sources_supplied`. A single high-scoring answer does not settle the case.

## Positive result

Under `substrate_workflow`, the advisor consistently splits the legible part from the unknown part, names both postures, uses the deciding conditions (challenge legibility and experiment cost) to locate the scenario, reaches a specifics-driven recommendation — diagnose the clinic-workflow part from existing data; test the patient-adoption assumption cheaply before committing build capacity — and attributes the ideas correctly. It does this visibly more often and more completely than under `vanilla`. That comparative gap is the result that supports the substrate's value for contradiction preservation.

## Falsifier

If `substrate_workflow` answers are no better than `vanilla` — both flatten to one framework at similar rates, or the substrate condition merely adds citations while still framework-defaulting or forcing a false consensus — the eval has not shown the substrate helps here, and the contradiction-preservation claim for this case is unsupported. The hypothesis is falsified by a substrate condition that does not beat `vanilla` across runs; it is not confirmed by any single passing answer.

## Model outputs

Six model-output files exist — two runs each for the three conditions run so far:

- `model-outputs/vanilla.md`, `model-outputs/vanilla-02.md` — the `vanilla` condition.
- `model-outputs/famous_sources_supplied.md`, `model-outputs/famous_sources_supplied-02.md` — the `famous_sources_supplied` condition.
- `model-outputs/substrate_workflow.md`, `model-outputs/substrate_workflow-02.md` — the `substrate_workflow` condition.

All six are in-session good-faith simulations — dry-run test artifacts. A model output is never an authority and never citable as a source. The `optional_local_model` condition has not been run; each future run is recorded as one further file under `model-outputs/`, labelled by `model_condition`.

## Score sheet

See `score-sheet.md` in this case folder. It has been filled for the `vanilla`, `famous_sources_supplied`, and `substrate_workflow` conditions; `scoring_status` is `scored`. The `optional_local_model` column remains blank until that condition is run.

## Judge notes

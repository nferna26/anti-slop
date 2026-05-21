---
case_id: strategy-diagnosis-vs-structural-positioning
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
scoring_status: scored
---

# Eval Case

## What this eval tests

This eval tests whether an advisor preserves a real tension between sources instead of flattening it into a false consensus — and, where a scenario's specifics favour one reading, whether it reasons from those specifics rather than defaulting to a familiar move. The tension under test is where the work of forming a competitive strategy should begin: from diagnosing the specific critical challenge a particular organisation faces, or from analysing the structure of the industry it competes in — and whether a structural pass is an input to that diagnosis, a competing starting point, or a different level of analysis. The case is built so a good answer must hold the starting-point question open and reason from the scenario, not pick a familiar framework and run it.

## Lineage

- `strategy-diagnosis-vs-structural-positioning` — reviewed claim/tension card (synthesis-level). The tension this case operationalises; its deciding conditions — what foregrounds diagnosis of the organisation's critical challenge, what foregrounds structural positioning, the input reading, and the level test — are the backbone of the scoring rubric.
- `BK-0001-card-001` — reviewed source card (evidence-level); Rumelt, *Good Strategy Bad Strategy*, Chapter 5. Carries Claim A of the tension card: a real strategy is built from a kernel whose first element is a diagnosis of the organisation's specific critical challenge.
- `BK-0023-card-001` — reviewed source card (evidence-level); Porter, *Competitive Strategy*, Chapter 1. Carries Claim B of the tension card: the joint strength of five structural forces sets an industry's long-run profit potential, and structural analysis of those forces is offered as the start of competitive-strategy work.

No book map is cited as lineage. Book maps are discovery hints only; the evidence under this case is the three reviewed artifacts above.

## Scenario

Synthetic and invented — no real person, company, or market. *Tessera Fixtures* is a fictional company, fifteen years old, that designs and manufactures mid-range commercial lighting fixtures and sells them through electrical-distribution channels and to building contractors. It was solidly profitable for most of its life; its margins have compressed over the last five years, and the founders want a three-year competitive-strategy direction.

Two views inside the company:

- The **CEO** and an internal faction read the problem as organisation-specific. Their case: the product line has not had a significant refresh in four years; the bid-and-quote turnaround has slowed from a few days to more than two weeks; two of the three senior designers left eighteen months ago and were never replaced. They want the next stretch of work spent identifying exactly what has gone wrong inside Tessera and fixing the few things that genuinely matter.
- A **board member** reads the problem as structural. Their case: the arena itself has changed — buyers have consolidated, cheap substitutes have arrived, and new entrants keep appearing — so no amount of internal repair changes a ceiling the industry's structure now sets. They want the work spent deciding whether Tessera should reposition into a different, structurally better segment rather than polishing its place in this one.

Facts the scenario supplies:

- Tessera's operating margin has fallen from roughly 14% to roughly 6% over five years.
- Across the mid-range commercial-fixture industry, the *average* operating margin has fallen over the same five years — the decline is industry-wide, not unique to Tessera.
- One similarly sized competitor, however, still earns roughly 12%: it moved several years ago into a specialised architectural-lighting niche and has held its margin there.
- Two large electrical-distribution chains now account for about 55% of the channel Tessera sells through, and both have pushed for annual price concessions.
- Low-cost imported LED fixtures now cover much of the mid-range, and several new small manufacturers have entered in the last three years.
- Internally: no significant product-line refresh in four years; quote turnaround slowed from days to more than two weeks; two of three senior designers gone for eighteen months, not replaced.
- The founders have committed to setting the three-year strategy direction within six weeks.

The scenario is built so the two readings visibly diverge. A reading that starts from Tessera's own critical challenge would spend the six weeks naming what, specifically, is load-bearing for this company — the stalled refresh, the lost design capability, the slow quoting, or the buyer concessions — and build a guiding policy and coherent action around that. A reading that starts from industry structure would spend the six weeks analysing the arena's profit potential — buyer consolidation, substitutes, entry, rivalry — and conclude that the move is to reposition into a segment with better structure, as the peer did. Those are concretely different six-week efforts and three-year plans. The evidence is deliberately mixed: the industry-wide margin fall is real, so a purely internal diagnosis would miss a genuine structural force; but a peer still earns 12% in the same industry, so the arena does not fully determine any one firm's fate. The case turns on which starting point is load-bearing *for Tessera* — and whether the structural pass is an input to Tessera's diagnosis, a rival starting point, or a separate question at a different level.

## Advisor prompt

> I run a fifteen-year-old company that designs and makes mid-range commercial lighting fixtures. We sell through electrical distributors and to building contractors. We were comfortably profitable for years, but our operating margin has slid from about 14% to about 6% over the last five years, and we need to set a three-year strategy direction in the next six weeks.
>
> There are two camps here and I'm stuck between them. I think the problem is us: we haven't meaningfully refreshed our product line in four years, our quote turnaround has gone from a few days to over two weeks, and we lost two of our three senior designers a year and a half ago and never replaced them. I want us to spend the next six weeks working out exactly what's broken inside the company and fixing the few things that matter most.
>
> One of my board members thinks I've got it wrong. She points out that the average margin across our whole industry has fallen over the same five years — it's not just us — that two big distribution chains now control more than half of our sales channel and lean on us for price cuts every year, and that cheap imported fixtures and a wave of new small manufacturers have crowded the mid-range. Her view is that the arena itself has gotten worse and no amount of internal fixing changes that, so we should be deciding whether to reposition into a different, better segment. She points to a competitor about our size that moved into a specialised architectural-lighting niche a few years ago and still earns around 12%.
>
> We have to commit to a direction in six weeks. Where should we even start — figuring out what's wrong with us, or rethinking what arena we should be competing in? What should we do, and why?

## Expected reasoning

A good answer must:

1. **Name both starting points.** Present the diagnose-the-organisation's-critical-challenge starting point — strategy work begins by isolating the few factors that are genuinely load-bearing for *this* company — *and* the analyse-the-industry's-structure starting point — strategy work begins from the structural forces that set the arena's profit potential — as legitimate, rather than asserting one is the obvious place to begin.
2. **Read the scenario's specific cues.** Use the mixed evidence as load-bearing, not background: the industry-wide margin fall (a real structural signal); the peer still near 12% in the same industry (evidence the arena does not fully determine a firm's fate); the two distributors at ~55% of the channel pressing annual concessions; the imports and new entrants; and the internal facts — the four-year stalled refresh, the slowed quoting, the two lost designers.
3. **Ask which starting point is load-bearing here.** Treat "begin from Tessera's own critical challenge" versus "begin from the industry's structure" as the live question the six weeks must answer, rather than assuming one. Note that the peer earning 12% cuts against a pure structural-determinism reading, and the industry-wide fall cuts against a purely internal reading.
4. **Locate the case against the deciding conditions.** Name what points toward foregrounding diagnosis (a specific organisation with an identifiable critical difficulty — here, the stalled refresh and lost design capability), what points toward foregrounding structural positioning (the question is which arena to be in, or the situation is dominated by a structural force — here, the consolidated buyers), the **input reading** (a structural pass may surface that the buyer consolidation *is* Tessera's critical challenge, so structure feeds the diagnosis rather than competing with it), and the **level test** (how attractive is the mid-range arena, and what is Tessera's own critical challenge within it, are two questions — an answer that collapses them into one undifferentiated "do strategy" step is flattening the tension).
5. **Reach an honest recommendation.** Either a recommendation conditional on the specifics — for example, run the structural pass and the internal diagnosis as feeds into one judgement, with an explicit test for whether the load-bearing factor is an industry-structural force or an organisation-specific failure, and a stated decision criterion — or an explicit preservation of the tension that states what is still undecided and why. A bare "fix what's broken internally," a bare "the industry is finished, reposition," or a hand-waved "do both" with no division, order, or deciding criterion is not sufficient.
6. **Attribute correctly.** If it invokes the underlying ideas, attribute them to the right source at the right authority level — source cards are evidence-level, the tension card is synthesis-level — and not as a settled rule or a framework that ends the question.

## Expected source behavior

- `vanilla` — no substrate supplied. Baseline; expect generic strategy advice, a default to a single familiar move ("do a strategy review", "diagnose then act"), or a "do both" that does not divide the problem.
- `famous_sources_supplied` — the famous frameworks/ideas are supplied at name level only (the idea that strategy begins from a diagnosis of the critical challenge; the idea that industry structure governs profit potential). Expect a raised risk of reciting one named framework as the authority that settles the question, or of name-dropping a framework as a label without doing the locate-the-starting-point work the scenario calls for.
- `substrate_workflow` — the substrate is supplied: the reviewed claim/tension card `strategy-diagnosis-vs-structural-positioning` and the two reviewed source cards `BK-0001-card-001` and `BK-0023-card-001`. Expect the advisor to name both starting points, use the tension card's deciding conditions to locate the scenario, weigh the mixed evidence (peer at 12% vs. industry-wide fall), distinguish the input reading from the level test, attribute each claim to its source card at evidence level and the tension to the card at synthesis level, and preserve the starting-point question honestly. The eval's hypothesis is that this condition produces visibly better tension-handling than `vanilla`.
- `vanilla_long_prompt` — the equal-length control: the Advisor prompt plus filler or unrelated material token-matched to the `substrate_workflow` packet, with **no** reviewed substrate artifacts. Separates a substrate advantage from a mere more-tokens effect. Expect behaviour close to `vanilla`; a `substrate_workflow` win over this control, not just over bare `vanilla`, is what shows the lineage content — not prompt length — is doing the work.
- `optional_local_model` — a real local-model run on the Advisor prompt only (the same packet as `vanilla`); never simulated. If no real local model can be run, the condition is deferred and the deferral recorded.
- A correct answer never presents either starting point as canon or as universally settled; the tension card is synthesis-level, the source claims are evidence-level.

## Failure modes

- **Flatten to internal diagnosis.** "Your margin problem is an execution problem — refresh the product line, fix the quoting, rebuild the design team, and the margin comes back." Treats the internal facts as the whole story and ignores the industry-wide margin fall and the buyer consolidation.
- **Flatten to structural repositioning.** "The arena is structurally finished — consolidated buyers, cheap imports, easy entry — so reposition into a niche like your competitor did." Discards the internal diagnosis and the genuine possibility that Tessera's own critical challenge is what is load-bearing.
- **Uniform treatment.** Treats the question as a generic "run a strategy review" and misses that the case turns on *where strategy work should begin* and on which starting point is load-bearing for Tessera.
- **Framework-default / name-dropping.** Recites a single named framework — "diagnose the critical challenge", "analyse the industry's structural forces" — as the authority that settles where to begin, instead of reasoning from the scenario's mixed specifics.
- **Misattribution.** Assigns the diagnosis-first idea to the industry-structure source or vice versa, or treats either as a settled canonical rule rather than evidence-level material.
- **False consensus.** Says "do both — diagnose the company and analyse the industry" without saying which comes first, whether one feeds the other, what would decide the starting point, or why — flattening the tension into a non-answer.
- **Ignoring the cues.** Overlooks the peer still earning 12% (which cuts against pure structural determinism) or the industry-wide margin fall (which cuts against a purely internal reading) — the two specifics that should keep the starting-point question genuinely open.

## Scoring rubric

Each criterion is scored pass or fail. The case is run under each `model_condition`; per condition the score is the count of criteria passed (0–5).

| Criterion | Passes when… | Fails when… |
|---|---|---|
| Tension recognised | the answer names both the diagnose-the-organisation's-critical-challenge starting point and the analyse-the-industry's-structure starting point as legitimate places for strategy work to begin | it presents only one starting point, or treats the choice of starting point as obvious |
| Scenario located | it uses the case's specific cues — the industry-wide margin fall, the peer still near 12%, the two distributors at ~55% of the channel, the imports and new entrants, the stalled four-year refresh, the slowed quoting, the two lost designers — and locates the case against the tension card's deciding conditions (what foregrounds diagnosis, what foregrounds structural positioning, the input reading, the level test) | it treats the situation generically, ignores those cues, or does not locate the case against the deciding conditions |
| No flattening | it keeps the starting-point question open — neither asserting one starting point is self-evidently correct nor collapsing the two into an undifferentiated "do both" with no order, division, or deciding criterion | it flattens to a single starting point as obvious, or to a bare "do both" that does not divide the problem |
| Lineage and authority discipline | any idea it invokes is attributed to the right source at the right authority level — the diagnosis-first and structural-positioning readings kept distinct, source cards used as evidence-level and the tension card as synthesis-level, neither treated as canon — and no named framework is wielded as the authority that ends the question | it misattributes one reading for the other, treats a source card or the tension card as canon or a settled rule, or recites a named framework as the authority that settles where to begin |
| Honest recommendation | it reaches a recommendation that locates the case against the deciding conditions and preserves the open starting-point question — settling on neither "just fix what's broken internally" nor "the industry is finished, reposition" — or preserves the tension with an explicit reason and a stated decision criterion | it forces a false consensus, hand-waves "do both" with no division of the problem, or defaults to a named framework as the answer |

The eval's signal is comparative: whether `substrate_workflow` scores higher, across runs, than `vanilla`, `famous_sources_supplied`, and the equal-length control `vanilla_long_prompt`. A single high-scoring answer does not settle the case.

## Positive result

Under `substrate_workflow`, the advisor consistently names both starting points, reads the mixed cues (the industry-wide fall and the peer at 12% on opposite sides), asks which starting point is load-bearing for Tessera, locates the case against the deciding conditions — including the input reading and the level test — reaches a specifics-driven recommendation that preserves the open starting-point question rather than flattening it, and attributes the ideas correctly at the right authority level. It does this visibly more often and more completely than under `vanilla`, `famous_sources_supplied`, and the equal-length control `vanilla_long_prompt`. That comparative gap — a `substrate_workflow` win over the equal-length control specifically, not only over bare `vanilla` — is the result that supports the substrate's value for contradiction preservation and shows the lineage content, not prompt length, is doing the work.

## Falsifier

If `substrate_workflow` answers are no better than `vanilla` and the `vanilla_long_prompt` control — all flatten to "fix it internally" or to "reposition" at similar rates, or the substrate condition merely adds citations while still ignoring the mixed cues and collapsing the starting-point question — the eval has not shown the substrate helps here, and the contradiction-preservation claim for this case is unsupported. If `substrate_workflow` beats bare `vanilla` but not the equal-length `vanilla_long_prompt` control, the apparent advantage is a prompt-length effect, not a lineage effect, and the case does not support the substrate. The hypothesis is falsified by a substrate condition that does not beat both baselines across runs; it is not confirmed by any single passing answer.

## Model outputs

Five model-output files exist, one per `model_condition`, all real local-model runs (`qwen3.5:latest` via Ollama) — there are no in-session simulations anywhere in this case:

- `model-outputs/vanilla.md` — the `vanilla` condition.
- `model-outputs/famous_sources_supplied.md` — the `famous_sources_supplied` condition.
- `model-outputs/substrate_workflow.md` — the `substrate_workflow` condition.
- `model-outputs/vanilla_long_prompt.md` — the `vanilla_long_prompt` equal-length control.
- `model-outputs/optional_local_model.md` — the `optional_local_model` condition.

The first three were produced in the first real-run pass (2026-05-21). `vanilla_long_prompt` and `optional_local_model` timed out in that first pass and were completed in a v2 follow-up pass (2026-05-21): the equal-length control was rebuilt with non-repetitive filler, and `optional_local_model` was retried on a fresh seed — see `run-packet.md` for the freeze, packet hashes, decoding parameters, and run receipts. A model output is a test artifact — never an authority, never citable as a source. Each future run is recorded as one further file under `model-outputs/`, labelled `<condition>` or `<condition>-NN`.

## Score sheet

See `score-sheet.md` in this case folder. It is filled for all five conditions, scored against the five-criterion rubric — `vanilla` (2/5), `famous_sources_supplied` (1/5), `substrate_workflow` (5/5), `vanilla_long_prompt` (3/5), and `optional_local_model` (2/5). `scoring_status` is `scored` and `## Result` is `partial`: `substrate_workflow` beats every baseline, including the equal-length control `vanilla_long_prompt` by two points, but the runs are single and the judge is model-family-separated but not independent, so the result is held at `partial` — below `benchmark_supported`, and `dry_run_supported` does not apply because there are no simulated outputs. A `partial` result supports no public advice claim and is not eligible to support a canon candidate.

## Judge notes

All five conditions have been run as real local-model runs and scored against the five-criterion rubric — three in the first real-run pass (2026-05-21) and the two deferred conditions in a v2 follow-up pass (2026-05-21). Per-condition pass/fail, the comparative signal, and the run history are recorded in `score-sheet.md` → `## Judge Notes` and `run-packet.md`. Generation was `qwen3.5:latest` (local, via Ollama); judging was Claude Opus 4.7 — a separate model family — with the limitation, recorded in `score-sheet.md` and `run-packet.md`, that the judge is the same agent orchestrating the passes rather than an independent third-party judge.

---
case_id: normalization-vs-latent-errors
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score against the rubric in this case's `case.md` → `## Scoring rubric`. Each of the five criteria is scored `pass` or `fail` per model condition. Per-condition score is the count of criteria passed (0–5). The criteria below are copied verbatim from the case rubric — do not score against generic or remembered criteria.

## Result

dry_run_supported — all four conditions have been run once and scored, and `substrate_workflow` (5/5) beats every baseline by the case's `## Positive result` criterion (`vanilla` 3/5, `famous_sources_supplied` 2/5, `optional_local_model` 2/5); a `model-outputs/` receipt file exists for each of the four runs, and the limitations are recorded below. The status is `dry_run_supported`, not `benchmark_supported`, because three of the four outputs — `vanilla`, `famous_sources_supplied`, and `substrate_workflow` — are in-session simulations rather than real external model runs; only `optional_local_model` (`qwen3.5:latest` via Ollama) is a real run. Per `docs/eval-result-status-policy.md`, this result may inform methodology but is **not** eligible to support a canon candidate. The sample is one run per condition; see Judge Notes and Follow-up.

## Scores

One column per `model_condition` from the case. Each cell is `pass` or `fail`; per-condition score is the count of criteria passed (0–5).

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | optional_local_model |
| --- | --- | --- | --- | --- |
| Tension recognised | fail | fail | pass | fail |
| Scenario located | pass | pass | pass | pass |
| Acceptance-threshold check | pass | pass | pass | pass |
| Lineage and authority discipline | pass | fail | pass | fail |
| Honest recommendation | fail | fail | pass | fail |
| **Per-condition score (0–5)** | 3 | 2 | 5 | 2 |

## Comparative signal

Per-condition score is 0–5. The eval signal is comparative, not absolute: `substrate_workflow` should beat `vanilla` and `famous_sources_supplied`, per `case.md` → `## Positive result`. A single high-scoring answer does not settle the case; `substrate_workflow` failing to beat `vanilla` across runs falsifies it, per `case.md` → `## Falsifier`.

Run so far (one run per condition): `substrate_workflow` 5/5; `vanilla` 3/5; `famous_sources_supplied` 2/5; `optional_local_model` 2/5. `substrate_workflow` beats every non-substrate condition — by 2 over `vanilla`, by 3 over `famous_sources_supplied`, and by 3 over the real local model. The `## Falsifier` (substrate not beating `vanilla`) is not met on this pass.

Two findings stand out. First, the gap is concentrated exactly where the substrate adds material: all four conditions passed `Scenario located` and `Acceptance-threshold check` — the Advisor prompt hands those cues over directly, so capable answers catch them — but only `substrate_workflow` passed `Tension recognised`, `Lineage and authority discipline`, and `Honest recommendation`. Holding the two readings open, attributing them with authority discipline, and reaching a recommendation that preserves the open intervention question are the moves the substrate's claim/tension card and source cards supply, and the non-substrate conditions did not make them. Second, `famous_sources_supplied` did not beat `vanilla` — it scored *below* it. Handing the advisor the famous ideas at name level made it *worse* on `Lineage and authority discipline`: the famous-sources answer wields "normalization of deviance" as the diagnosis that settles the question, where the vanilla answer, invoking no named idea, committed no authority abuse. This is consistent with the eval's hypothesis that the substrate — not famous-framework awareness, and not raw model capability — is what produces tension-preservation. The sample is small (one run per condition).

## Judge Notes

Conditions run, as of 2026-05-20: `vanilla`, `famous_sources_supplied`, `substrate_workflow`, and `optional_local_model` — one run each. All four runs are recorded under `model-outputs/`; all are test artifacts, not authorities. The `vanilla`, `famous_sources_supplied`, and `substrate_workflow` runs are in-session good-faith simulations — useful for exercising the eval harness and for methodology iteration, but not a settled empirical benchmark. The `optional_local_model` run is a real local-model run (`qwen3.5:latest` via Ollama, server 0.23.4).

**vanilla — 3/5.**

- Tension recognised — FAIL. Adjudicates rather than holds the tension: "Your floor supervisor is the one to listen to here" and "this is, at bottom, a safety-culture problem, not a missing-layer problem." It acknowledges the operations lead ("the four layers were not pointless") but subordinates that reading entirely; it treats the choice as effectively settled.
- Scenario located — PASS. Uses all three cues — the flat near-miss rate ("flat for 18 months ... the rate did not move"), the 20-second checklist ("the clearest symptom"), and the "control added = risk down" framing ("the equation your team is running").
- Acceptance-threshold check — PASS. Explicitly raises the threshold drift ("the bar for what your team treats as 'normal' has drifted") and the normalized check ("the [checklist] has stopped being a control and become paperwork").
- Lineage and authority discipline — PASS. No substrate was supplied and the answer invokes no named idea or framework; it reasons in plain terms, so it neither misattributes, conflates, treats anything as canon, nor recites a named idea as a settling authority. The criterion's fail conditions are not met.
- Honest recommendation — FAIL. Flattens to the culture side: "Spend the two weeks on the culture, not the hardware" and "this is, at bottom, a safety-culture problem." It does not locate the case against deciding conditions and does not preserve the open intervention question — it answers it.

**famous_sources_supplied — 2/5.**

- Tension recognised — FAIL. Names both ideas — the layered-defence / Swiss-cheese model and normalization of deviance — but immediately turns them into a contest with a winner: "So which model is right for you? I would say the evidence settles it: this is normalization of deviance." It treats the choice as obvious.
- Scenario located — PASS. Uses the flat near-miss rate, the 20-second "formality" checklist, and the "control added = risk handled" framing.
- Acceptance-threshold check — PASS. "Reconstruct how the team's definition of an acceptable near-miss shifted" (threshold drift) and "the 20-second 'formality' checklist is a layer that has already been normalized into noise" (normalized check).
- Lineage and authority discipline — FAIL. Recites a named idea as the authority that settles the question: "this is normalization of deviance" followed by "That diagnosis settles the decision." The two named ideas are kept distinct and not misattributed, but they are wielded as framework-authorities that end the question rather than as evidence informing an open judgment.
- Honest recommendation — FAIL. Flattens to the normalization-of-deviance / culture side ("Treat this as a normalization-of-deviance intervention"; "treating a cultural problem with a hardware fix") and closes the open intervention question rather than preserving it.

**substrate_workflow — 5/5.**

- Tension recognised — PASS. Names both readings as legitimate and well-grounded, and states the substrate "holds those two accounts as a genuine, unresolved tension rather than letting one win by default"; "both readings are carrying weight."
- Scenario located — PASS. Uses the flat near-miss rate ("flat across all four controls"), the 20-second checklist ("a normalized formality"), and the "control added = risk down" framing.
- Acceptance-threshold check — PASS. "Examine whether your team's threshold for an acceptable near-miss has drifted" and "whether each of the four controls is a live defence or a normalized formality."
- Lineage and authority discipline — PASS. Attributes the latent-errors reading to `BK-0044-card-001`, the normalization-of-deviance reading to `BK-0042-card-001`, the response-and-boundary to `BK-0044-card-002`, and the tension to the claim/tension card; keeps the Chapter 7 mechanism and the Chapter 8 response distinct; states explicitly that "the source cards are evidence-level and the tension card is synthesis-level — none of this is canon." No idea is wielded as a settling authority.
- Honest recommendation — PASS. States "I am not going to flatten this to 'add the layer' or to 'it is all culture'", locates the case against the tension card's deciding conditions, and preserves the open intervention question explicitly ("whether strengthening your defences would address that drift, leave it untouched, or deepen it ... is the question your two weeks should be spent answering, not pre-empting").

**optional_local_model — 2/5.** Real local-model run: `qwen3.5:latest` via Ollama, Advisor prompt only, no substrate.

- Tension recognised — FAIL. "The decision is clear" and the operations lead "is falling into a common cognitive trap." It engages the layered-defence idea (the "hole in the cheese") and names normalization of deviance, but treats the choice as obvious and does not hold the layered-defence reading as legitimate.
- Scenario located — PASS. Uses the flat near-miss rate ("remained flat for 18 months"), the 20-second formality checklist, and quotes the supervisor's "we added a control" framing.
- Acceptance-threshold check — PASS. Raises normalization of deviance and workers adjusting to "the new level of risk" (threshold drift) and states the checklist "has effectively failed as a behavioral control" (normalized check).
- Lineage and authority discipline — FAIL. Recites named ideas as settling authorities — labels the operations lead's position with a named "cognitive trap ... known as compensatory control" and builds the verdict on "Leading Indicators" vs "Lagging Indicators" — using the labels to end the question rather than as evidence in an open judgment.
- Honest recommendation — FAIL. Flattens toward the culture side: "the root cause is not technical, it is procedural or cultural"; "Fix the behavior first." The recommendation is concrete and contingent, but it closes the intervention question rather than preserving it and does not locate the case against deciding conditions.

The local model alone scored level with `famous_sources_supplied` and below `vanilla`: raw model capability, without the substrate, did not produce tension-preservation, authority discipline, or a tension-preserving recommendation.

## Follow-up

- All four conditions have been run once and scored. This is a single run per condition; the comparative signal is clear but not yet shown to be stable across repeat runs.
- `Result` is `dry_run_supported` per `docs/eval-result-status-policy.md`. To reach `benchmark_supported` — the only status eligible to support a canon candidate — `vanilla`, `famous_sources_supplied`, and `substrate_workflow` would need real external model runs in place of the in-session simulations.
- Repeat runs of each condition would tighten the signal and test it against the case's "across runs" standard; they are the obvious next step but are not blocking.
- If `substrate_workflow` stops beating `vanilla` in later runs, treat the case as falsified per `case.md` → `## Falsifier`.
- This result is not eligible to support a canon candidate while it is `dry_run_supported`.

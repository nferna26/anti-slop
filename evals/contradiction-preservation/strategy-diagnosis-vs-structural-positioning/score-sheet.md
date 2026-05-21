---
case_id: strategy-diagnosis-vs-structural-positioning
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score against the rubric in this case's `case.md` → `## Scoring rubric`. Each of the five criteria is scored `pass` or `fail` per model condition. Per-condition score is the count of criteria passed (0–5). The criteria below are copied verbatim from the case rubric — do not score against generic or remembered criteria.

All five conditions have been run as real local-model runs and scored. The first pass (2026-05-21) ran three (`vanilla`, `famous_sources_supplied`, `substrate_workflow`); the v2 pass (2026-05-21) completed the two the first pass had deferred (`vanilla_long_prompt`, `optional_local_model`). See `run-packet.md` for the freeze, the packets, and the run receipts.

## Result

partial — all five conditions have now been run as real local-model runs and scored: `vanilla` 2/5, `famous_sources_supplied` 1/5, `substrate_workflow` 5/5, `vanilla_long_prompt` 3/5, `optional_local_model` 2/5. `substrate_workflow` beats every baseline by the `## Positive result` criterion, including the equal-length control `vanilla_long_prompt` by two points, so the substrate advantage on this pass is not explained by prompt length. The result is held at `partial`, not `benchmark_supported`: the runs are single (a benchmark pass needs at least three repeats per condition per `docs/eval-benchmark-upgrade.md`) and the judge is model-family-separated from the generator but not an independent third-party judge. `dry_run_supported` does not apply either — that status is defined by in-session simulated outputs and this case has none; the evidence is all-real but single-run, which is mid-evaluation toward a benchmark, i.e. `partial`. Per `docs/eval-result-status-policy.md` a `partial` result supports no public advice claim and is not eligible to support a canon candidate.

## Scores

One column per `model_condition` from the case. Each cell is `pass` or `fail`; per-condition score is the count of criteria passed (0–5).

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | optional_local_model |
| --- | --- | --- | --- | --- | --- |
| Tension recognised | fail | fail | pass | pass | fail |
| Scenario located | pass | pass | pass | pass | pass |
| No flattening | fail | fail | pass | fail | fail |
| Lineage and authority discipline | pass | fail | pass | pass | pass |
| Honest recommendation | fail | fail | pass | fail | fail |
| **Per-condition score (0–5)** | 2 | 1 | 5 | 3 | 2 |

## Comparative signal

Per-condition score is 0–5. The eval signal is comparative, not absolute: per `case.md` → `## Positive result`, `substrate_workflow` should out-score `vanilla`, `famous_sources_supplied`, and the equal-length control `vanilla_long_prompt`. Per `case.md` → `## Falsifier`, a `substrate_workflow` that does not beat both `vanilla` and `vanilla_long_prompt` falsifies the case; a win over bare `vanilla` but not the equal-length control would be a prompt-length effect, not a lineage effect.

Run so far (one real run per condition): `substrate_workflow` 5/5; `vanilla_long_prompt` 3/5; `vanilla` 2/5; `optional_local_model` 2/5; `famous_sources_supplied` 1/5. `substrate_workflow` beats every baseline — by 2 over the equal-length control `vanilla_long_prompt`, by 3 over `vanilla` and `optional_local_model`, by 4 over `famous_sources_supplied`. The `## Falsifier` is not met on this pass: `substrate_workflow` beats both `vanilla` and the equal-length control.

Three observations. First, the equal-length control behaves as intended: `vanilla_long_prompt` (3/5) is two points below `substrate_workflow` (5/5), so the substrate advantage is **not** a mere prompt-length effect — a token-matched prompt with no substrate does not reproduce it. Second, `vanilla_long_prompt` (3/5) scored one point above bare `vanilla` (2/5): the longer prompt nudged the model to acknowledge both readings as necessary ("you must do both"), which earned the `Tension recognised` point — but it still flattened the starting-point question to a fixed answer (`No flattening` and `Honest recommendation` both fail), so the gain stops well short of the substrate's tension-handling. Third, the gap is concentrated where the substrate adds material: all five conditions passed `Scenario located` (the Advisor prompt hands the cues over directly), but only `substrate_workflow` passed `No flattening` and `Honest recommendation`, and only `substrate_workflow` and `vanilla_long_prompt` passed `Tension recognised`. Holding the starting-point question genuinely open, locating the case against the tension card's deciding conditions, and attributing at the right authority level are the moves the substrate supplied and the baselines did not. `famous_sources_supplied` (1/5) again scored below `vanilla` (2/5): name-level famous-framework awareness made it worse on `Lineage and authority discipline`. The sample is one run per condition.

## Judge Notes

Conditions run, as of 2026-05-21: all five — `vanilla`, `famous_sources_supplied`, `substrate_workflow`, `vanilla_long_prompt`, and `optional_local_model` — one real local-model run each, all `qwen3.5:latest` via Ollama (server 0.24.0). There are **no in-session simulations** in this case. Generator: `qwen3.5:latest`; judge: Claude Opus 4.7 (`claude-opus-4-7`), a different model family — generation and scoring are separated. Limitation: the judge is the same agent orchestrating the passes, so this is model-family separation, not an independent third-party judge.

**vanilla — 2/5.** (First pass; score unchanged.)

- Tension recognised — FAIL. Opens "You should start with **rethinking the arena**, not fixing the internal problems" and frames the internal-diagnosis reading as "symptoms, not the disease." It treats the choice of starting point as obvious and subordinates one reading.
- Scenario located — PASS. Uses the scenario cues — the industry-wide margin decline, channel consolidation, import competition, the 12%-margin competitor, the two distributors, the lost senior designers, the 6% margin.
- No flattening — FAIL. Although it says "Do not treat 'Internal Fixes' and 'Arena Rethink' as a binary choice," it collapses the starting-point question — "treat the Arena as the **Goal**", "Start with the Arena."
- Lineage and authority discipline — PASS. No substrate supplied and no named framework invoked as authority; the criterion's fail conditions are not met.
- Honest recommendation — FAIL. Forces a one-sided recommendation — "Start with the Arena", "find a new way to earn a premium (the niche) or exit."

**famous_sources_supplied — 1/5.** (First pass; score unchanged.)

- Tension recognised — FAIL. "my recommendation is unequivocal: **Start with the Arena**." Treats the choice as obvious.
- Scenario located — PASS. Uses the cues — the 6% industry average, the niche competitor, the two distributors, imports, lost designers.
- No flattening — FAIL. Flattens to one starting point as self-evidently correct ("unequivocal").
- Lineage and authority discipline — FAIL. Recites a named framework as the authority that settles the question: "In Porter's Five Forces framework, the bargaining power of buyers ... and the threat of substitutes ... have intensified. This has lowered the industry ceiling."
- Honest recommendation — FAIL. "Commit to the **Arena Shift**." One-sided; the open question is closed.

**substrate_workflow — 5/5.** (First pass; score unchanged.)

- Tension recognised — PASS. Names both readings as "the two sides of an open tension documented in the knowledge base"; says the board's structural argument "is valid" and the tension is "**open** and not resolved into a single canon."
- Scenario located — PASS. Uses scenario cues and locates the case against the tension card's deciding conditions, quoting the "Deciding Conditions" and the "Input Reading" and naming the level distinction.
- No flattening — PASS. Explicitly keeps the question open: "Do not default to a single starting point without testing the other"; picks diagnosis-first via a stated deciding condition and keeps the structural reading in play as an input.
- Lineage and authority discipline — PASS. Attributes the diagnosis reading to `BK-0001-card-001` (Rumelt) and the structural reading to `BK-0023-card-001` (Porter) correctly; names the tension card as synthesis-level; uses the five-forces idea "not as a template, but as a lens."
- Honest recommendation — PASS. Reaches a recommendation that locates the case against the deciding conditions, sequences diagnosis with the structural pass as an input, and states an explicit decision criterion; the open starting-point question is preserved.

**vanilla_long_prompt — 3/5.** Real local-model run; v2 distinct-filler equal-length control packet, `seed 104`.

- Tension recognised — PASS. Names both readings and presents both as necessary — "You must not choose between fixing the internal rot and rethinking the arena; you must do both" — and credits each side ("Your board member is correct that the external environment has deteriorated"; the internal decay is "the bottleneck"). Unlike `vanilla` it does not dismiss either reading as merely symptomatic, so the tension itself is recognised.
- Scenario located — PASS. Uses the cues: the lost two of three senior designers, the doubled quote turnaround, the stagnant product line, the competitor at 12%, the 6% margin / mid-range cap, distribution consolidation, imports.
- No flattening — FAIL. Despite the "do both" framing it flattens the starting-point question — "you must **start with the Internal Assessment**" asserted as a directive, the board member's structural conclusion called "incorrect" — and pre-decides the outcome ("pivot to the specialized architectural-lighting niche"). The open question is answered, not preserved.
- Lineage and authority discipline — PASS. No substrate supplied; the answer invokes no named framework as an authority (its "Rebuild the Engine" and vehicle/destination framings are its own). No misattribution, nothing treated as canon — the criterion's fail conditions are not met.
- Honest recommendation — FAIL. Forces a one-sided ordering ("you must start with the Internal Assessment") and a pre-decided strategic outcome; the open starting-point question is not preserved and the case is not located against deciding conditions.

**optional_local_model — 2/5.** Real local-model run on the Advisor prompt only (same packet as `vanilla`); `seed 205` retry, the `seed 105` first attempt having timed out.

- Tension recognised — FAIL. Names both readings ("The Board Member is right about the market reality, and the CEO is right about the operational symptoms") but immediately subordinates the internal reading — "the symptoms are caused by the wrong arena", "Why 'Fixing Us' is a Trap" — and treats the choice as obvious ("Start with the Arena").
- Scenario located — PASS. Uses the cues: the 14%→6% margin, the falling industry average, the two distribution chains, imports, the two lost designers, slow quotes, the competitor at 12%.
- No flattening — FAIL. Flattens to one starting point ("Start with the Arena", internal-first labelled a "Trap") and pre-decides the pivot outcome.
- Lineage and authority discipline — PASS. No substrate; no named framework wielded as a settling authority ("Efficiency Trap", "Competitor Proof" are its own coinages); no misattribution, nothing treated as canon.
- Honest recommendation — FAIL. Forces a one-sided recommendation; the open question is closed, not preserved.

This run is on the byte-identical packet to `vanilla` and lands at the same 2/5 with the same failure profile — consistent with `optional_local_model` being, by design, a real local-model run on the `vanilla` packet.

## Follow-up

- All five conditions have run as real local-model runs and been scored; this is a single run per condition. `substrate_workflow` beats every baseline including the equal-length control, but the comparative signal is not yet shown stable across repeat runs.
- `Result` is `partial` per `docs/eval-result-status-policy.md`. To move toward `benchmark_supported` — the only status eligible to support a canon candidate — the case needs at least three repeats per condition, an independent judge (not the orchestrating agent), and the frozen-packet discipline in `docs/eval-benchmark-upgrade.md` carried through a dedicated benchmark pass.
- The equal-length control is now in and behaved as intended: `vanilla_long_prompt` (3/5) sits two points below `substrate_workflow` (5/5), so the substrate advantage on this pass is not a prompt-length artefact.
- If `substrate_workflow` stops beating `vanilla` and the equal-length control in later runs, treat the case as falsified per `case.md` → `## Falsifier`.
- This result is not eligible to support a canon candidate while it is `partial`.

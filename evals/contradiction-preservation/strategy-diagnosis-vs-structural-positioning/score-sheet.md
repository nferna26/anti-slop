---
case_id: strategy-diagnosis-vs-structural-positioning
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score against the rubric in this case's `case.md` → `## Scoring rubric`. Each of the five criteria is scored `pass` or `fail` per model condition. Per-condition score is the count of criteria passed (0–5). The criteria below are copied verbatim from the case rubric — do not score against generic or remembered criteria.

First real-run pass: 2026-05-21. Three of the five conditions produced real local-model outputs and are scored; two timed out and are deferred. See `run-packet.md` for the freeze, the packets, and the run receipts.

## Result

partial — three of the five conditions produced real local-model runs and were scored (`vanilla` 2/5, `famous_sources_supplied` 1/5, `substrate_workflow` 5/5); `vanilla_long_prompt` and `optional_local_model` timed out at 900s and are deferred (no output, not fabricated — see `run-packet.md`). `substrate_workflow` beats both scored baselines by the `## Positive result` criterion, but the result is held at `partial`, not `dry_run_supported` or `benchmark_supported`: the equal-length control `vanilla_long_prompt` is deferred, so a substrate advantage cannot yet be separated from a prompt-length effect (`case.md` → `## Falsifier`); the runs are single (a benchmark pass needs at least three repeats per condition); and the judge is model-family-separated but not independent. Per `docs/eval-result-status-policy.md` a `partial` result supports no public advice claim and is not eligible to support a canon candidate.

## Scores

One column per `model_condition` from the case. Each cell is `pass` or `fail`; per-condition score is the count of criteria passed (0–5). `deferred` marks a condition that timed out and produced no real output this pass.

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | optional_local_model |
| --- | --- | --- | --- | --- | --- |
| Tension recognised | fail | fail | pass | deferred | deferred |
| Scenario located | pass | pass | pass | deferred | deferred |
| No flattening | fail | fail | pass | deferred | deferred |
| Lineage and authority discipline | pass | fail | pass | deferred | deferred |
| Honest recommendation | fail | fail | pass | deferred | deferred |
| **Per-condition score (0–5)** | 2 | 1 | 5 | deferred | deferred |

## Comparative signal

Per-condition score is 0–5. The eval signal is comparative, not absolute: per `case.md` → `## Positive result`, `substrate_workflow` should out-score `vanilla`, `famous_sources_supplied`, and the equal-length control `vanilla_long_prompt`. Per `case.md` → `## Falsifier`, a `substrate_workflow` that does not beat both `vanilla` and `vanilla_long_prompt` across runs falsifies the case; a win over bare `vanilla` but not the equal-length control would be a prompt-length effect, not a lineage effect.

Run so far (one real run per condition): `substrate_workflow` 5/5; `vanilla` 2/5; `famous_sources_supplied` 1/5. `substrate_workflow` beats `vanilla` by 3 and `famous_sources_supplied` by 4. The `## Falsifier`'s "not better than `vanilla`" condition is not met on this pass.

Two limits on that signal. First, the equal-length control `vanilla_long_prompt` is **deferred** (it timed out), so this pass cannot show the substrate win survives a token-matched no-substrate prompt — the lineage-vs-length question is open, and the case is therefore **not** "supported" by this pass. Second, the gap is concentrated exactly where the substrate adds material: all three scored conditions passed `Scenario located` (the Advisor prompt hands the scenario cues over directly), but only `substrate_workflow` passed `Tension recognised`, `No flattening`, `Lineage and authority discipline`, and `Honest recommendation` — the moves the claim/tension card's deciding conditions and the source cards supply. `famous_sources_supplied` scored *below* `vanilla`: handing the model the famous ideas at name level made it worse on `Lineage and authority discipline` — it wielded "Porter's Five Forces" as the framework-authority that settled the question, where `vanilla`, invoking no named framework, committed no authority abuse. This is consistent with the eval's hypothesis that the substrate — not bare famous-name awareness — is what produces tension preservation. The sample is one run per condition.

## Judge Notes

Conditions run, as of 2026-05-21: `vanilla`, `famous_sources_supplied`, and `substrate_workflow` — one real local-model run each, all `qwen3.5:latest` via Ollama (server 0.24.0). `vanilla_long_prompt` and `optional_local_model` were attempted as real runs and timed out at 900s; they are deferred and unscored (see `run-packet.md`). All three scored runs are real local-model outputs — there are **no in-session simulations** in this pass. Generator: `qwen3.5:latest`; judge: Claude Opus 4.7 (`claude-opus-4-7`), a different model family — generation and scoring are separated. Limitation: the judge is the same agent orchestrating the pass, so this is model-family separation, not an independent third-party judge.

**vanilla — 2/5.**

- Tension recognised — FAIL. Opens "You should start with **rethinking the arena**, not fixing the internal problems" and frames the internal-diagnosis reading as "symptoms, not the disease." It treats the choice of starting point as obvious and subordinates one reading rather than holding both as legitimate starting points.
- Scenario located — PASS. Uses the scenario cues — the industry-wide margin decline, channel consolidation, the import competition, the 12%-margin competitor, the two distributors, the lost senior designers, the 6% margin — and reasons from them.
- No flattening — FAIL. Although it says "Do not treat 'Internal Fixes' and 'Arena Rethink' as a binary choice," it immediately collapses the starting-point question — "treat the Arena as the **Goal** and the Internal Fixes as the **Prerequisites**", "Start with the Arena." The question is not kept open.
- Lineage and authority discipline — PASS. No substrate was supplied and the answer invokes no named framework as an authority; its "Efficiency/Talent/Channel Trap" headings are its own coinages. It does not misattribute, treat anything as canon, or recite a named framework as a settling authority — the criterion's fail conditions are not met.
- Honest recommendation — FAIL. Forces a one-sided recommendation — "Start with the Arena", "find a new way to earn a premium (the niche) or exit." It answers the starting-point question rather than preserving it and does not locate the case against deciding conditions.

**famous_sources_supplied — 1/5.**

- Tension recognised — FAIL. "my recommendation is unequivocal: **Start with the Arena**." It names both an Inside-Out and an Outside-In reading but treats the choice as obvious ("unequivocal") and subordinates the diagnosis reading as "enablers, not the strategy."
- Scenario located — PASS. Uses the cues — the 6% industry average, the niche competitor, the two distributors, imports, lost designers.
- No flattening — FAIL. Flattens to one starting point as self-evidently correct ("unequivocal: Start with the Arena").
- Lineage and authority discipline — FAIL. Recites a named framework as the authority that settles the question: "In Porter's Five Forces framework, the bargaining power of buyers ... and the threat of substitutes ... have intensified. This has lowered the industry ceiling" — the named framework is wielded to establish the structural conclusion that ends the starting-point question. It also treats "diagnosis" as a framework to "apply." This is the authority abuse the criterion is built to catch.
- Honest recommendation — FAIL. "Commit to the **Arena Shift**." One-sided; the open starting-point question is closed, not preserved.

**substrate_workflow — 5/5.**

- Tension recognised — PASS. Names both readings and states they are "the two sides of an open tension documented in the knowledge base"; says the board's structural argument "is valid" and that the tension is "**open** and not resolved into a single canon." Both starting points are held as legitimate.
- Scenario located — PASS. Uses scenario cues (the 14%→6% margin slide, the distributors as buyer power, imports as substitutes, internal design capacity) and — distinctively — locates the case against the tension card's deciding conditions, quoting the "Deciding Conditions" and the "Input Reading" and naming the level distinction. (It underuses the peer-at-12% and industry-wide-fall cues specifically; a partial weakness, not a fail — it is decidedly not generic and it locates against the deciding conditions, the harder half of the criterion.)
- No flattening — PASS. Explicitly keeps the question open: "Do not default to a single starting point without testing the other"; "the tension card advises against flattening these into one undifferentiated step." It picks diagnosis-first via a stated deciding condition and keeps the structural reading in play as an input — not a one-side collapse, not a bare "do both."
- Lineage and authority discipline — PASS. Attributes the diagnosis reading to `BK-0001-card-001` (Rumelt) and the structural reading to `BK-0023-card-001` (Porter) — correctly, not swapped — names the tension card as the synthesis-level artifact, and states the tension is "open and not resolved into a single canon." It uses the five-forces idea "not as a template, but as a lens" — an input, not a settling authority.
- Honest recommendation — PASS. Reaches a recommendation that locates the case against the deciding conditions, sequences diagnosis with the structural pass as an input, and states an explicit decision criterion ("If the diagnosis reveals the challenge is structural ... the Guiding Policy becomes 'Reposition' ... if ... internal ... 'Fix'") — the open starting-point question is preserved and handed to the diagnosis to settle, not pre-empted.

## Follow-up

- Three of five conditions ran as real local-model runs and were scored; this is a single run per condition. `substrate_workflow` beats both scored baselines, but the comparative signal is not yet shown stable across repeat runs.
- `vanilla_long_prompt` (the equal-length control) and `optional_local_model` are **deferred** — both timed out at 900s. `vanilla_long_prompt` should be re-attempted with non-repetitive neutral filler (the repeated-paragraph filler drove the local model into a generation loop); `optional_local_model` can be re-attempted on a different seed, though its role is already covered by the `vanilla` run, which is itself a real local-model run on the identical packet.
- `Result` is `partial` per `docs/eval-result-status-policy.md`. To move toward `benchmark_supported` — the only status eligible to support a canon candidate — the case needs the equal-length control run, real runs for every comparison condition, at least three repeats per condition, an independent judge, and the frozen-packet discipline in `docs/eval-benchmark-upgrade.md`.
- If `substrate_workflow` stops beating `vanilla` and the equal-length control in later runs, treat the case as falsified per `case.md` → `## Falsifier`.
- This result is not eligible to support a canon candidate while it is `partial`.

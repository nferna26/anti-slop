---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score against the rubric in this case's `case.md` → `## Scoring rubric`: six binary criteria C1–C6, each `pass` or `fail` per model condition per run. Per-run per-condition score is the count of criteria passed (0–6). Apply the pre-registered `## Criterion dependency rule` and the `## Judge protocol` from `case.md`. Do not score against generic or remembered criteria.

This score sheet is **scored**. The case is `status: draft`, `scoring_status: scored`; the frozen `diagnosis-vs-validated-learning-benefits-renewal-v2-v1` benchmark pass has been **run** — forty real `gemma4:31b` outputs, eight per condition, recorded under `model-outputs/` (see `run-packet.md`, status `frozen_run_complete`) — and two condition-blind judge receipts have been reconciled aggregate-only. The `OUT-NN` → condition answer key remains local-only and uncommitted.

## Result

partial — the frozen `diagnosis-vs-validated-learning-benefits-renewal-v2-v1` benchmark pass has been run (forty real `gemma4:31b` outputs, eight per condition, with no in-session simulations and no deferrals — see `run-packet.md`) and reconciled across two condition-blind judge receipts. The case remains `partial` because neither judge meets the pre-registered positive rule, the judges disagree on C5 for 20 of 40 outputs and C6 for 22 of 40 outputs (triggering the third-judge rule), and the Claude Opus pass is not independent of the orchestrator. `eval-decision.md` records `do_not_promote`. A `partial` result supports no public advice claim and is not eligible to support a canon candidate.

This score sheet has **two separate surfaces**, and they must not be merged:

- a **blind judge scoring surface** — judge-facing, anonymised, **no condition labels**;
- a **post-reconciliation condition aggregate** — operator-only, filled **after** blind scoring using the local-only answer key.

A judge sees only the first. Mixing the condition labels into the judge-facing surface would break the blind `## Judge protocol` in `case.md`.

## Blind judge scoring surface

Judge-facing. The frozen run is complete and two judge receipts now exist: `judge-packet/independent-judge-score-gpt-oss-20b.md` and `judge-packet/independent-judge-score-claude-opus.md`. Its forty outputs are anonymised in `judge-packet/` as `OUT-01 … OUT-40` (condition-blind — the generating condition is withheld and does not appear on this surface). Each judge records `pass`/`fail` for every criterion C1–C6 on every `OUT-NN`, applies the pre-registered `## Criterion dependency rule` from `case.md`, and writes one short reasoning note per output.

Template — one table per judge; `OUT-NN` rows added at freeze/scoring time:

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total (0–6) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OUT-01 |  |  |  |  |  |  |  |
| OUT-02 |  |  |  |  |  |  |  |
| … | … | … | … | … | … | … | … |
| OUT-NN |  |  |  |  |  |  |  |

No condition name appears on this surface. A judge who can tell which condition produced an `OUT-NN` is not scoring blind.

## Post-reconciliation condition aggregate

**Operator-only — not judge-facing. Do not show during scoring.** This surface is filled **only after** blind scoring is complete, by mapping each `OUT-NN` back to its condition with the local-only (git-ignored) answer key. It carries the condition identities the blind surface withholds. The detailed reconciliation is in `judge-packet/judge-variance-summary.md`; the table below gives the aggregate result without exposing the answer key.

| Judge | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | criteria_prompted_no_sources |
| --- | ---: | ---: | ---: | ---: | ---: |
| `gpt-oss:20b` mean (0–6) | 2.88 | 2.38 | 4.25 | 1.00 | 3.00 |
| Claude Opus 4.7 mean (0–6) | 6.00 | 6.00 | 6.00 | 3.50 | 6.00 |
| Two-judge average, orientation only | 4.44 | 4.19 | 5.13 | 2.25 | 4.50 |

## Comparative signal

**Operator-only, post-reconciliation — not judge-facing.** The reconciled comparison does **not** meet `case.md` → `## Positive result`.

- `gpt-oss:20b` ranks `substrate_workflow` highest, but its margin over `criteria_prompted_no_sources` is +1.25, below the +1.5 aggregate bar; it also misses the required C4 critical-criterion margins over both controls.
- Claude Opus 4.7 scores `substrate_workflow` at 6.00, but also scores `criteria_prompted_no_sources`, `vanilla`, and `famous_sources_supplied` at 6.00, so the substrate has no separation from those controls.
- C5 differs between judges on 20/40 outputs, and C6 differs on 22/40 outputs; the third-judge trigger is met.

Current classification: judge-sensitive / control-matched / not promoted. See `judge-packet/judge-variance-summary.md` and `eval-decision.md`.

## Judge Notes

**Update (2026-05-22):** a **first** independent condition-blind judge pass has been recorded — `gpt-oss:20b` (a non-Gemma family, different from the `gemma4:31b` generator) scored all forty `OUT-NN` outputs against C1–C6; see `judge-packet/independent-judge-score-gpt-oss-20b.md`. That pass is **one** judge of the **at least two** the `## Judge protocol` requires; a second independent blind judge, and only then reconciliation of `OUT-NN` to conditions, are still pending. The score tables in this sheet remain empty, `scoring_status` stays `unscored`, and `## Result` stays `partial` until the case is fully scored and reconciled.

**Update (2026-05-22) — second pass.** A second condition-blind judge pass has been recorded — Claude Opus 4.7 (`judge-packet/independent-judge-score-claude-opus.md`), a different model family from both the `gemma4:31b` generator and the first (`gpt-oss:20b`) judge. **Limitation:** this judge is the agent that orchestrated the eval, so it is **not** independent of the orchestrator — the case still lacks a fully independent third-party or human judge. The two recorded passes **diverge sharply** (gpt-oss totals spread 0/6–6/6; the Claude Opus totals are concentrated, 35 of 40 at 6/6), so the outcome is **judge-sensitive** — per the `## Judge protocol` that keeps `## Result` at `partial`. `scoring_status` stays `unscored`; `OUT-NN` → condition reconciliation is still pending.

This section records each judge's identity and model family, their condition-blind per-`OUT-NN` criterion verdicts (C1–C6) and short reasoning, any third-judge trigger on C5/C6 or margin disagreement, and whether the outcome is judge-sensitive (which keeps the Result `partial`). The `OUT-NN` → condition mapping is applied only after blind scoring is complete and lives in the post-reconciliation surface above, never in the judge-facing notes.

**Update (2026-05-22) — reconciliation.** The two judge receipts have been reconciled aggregate-only in `judge-packet/judge-variance-summary.md`, and `eval-decision.md` records `do_not_promote`. Neither judge meets the pre-registered positive rule; the criteria-prompted control matches the substrate under Claude Opus, and C5/C6 disagreement triggers the third-judge rule. `scoring_status` is now `scored`, but `## Result` stays `partial`. `postmortem.md` analyses the non-promotion and proposes a v3 eval-design direction.

---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
eval_type: contradiction-preservation
scoring_status: unscored
---

# Score Sheet

Score against the rubric in this case's `case.md` → `## Scoring rubric`: six binary criteria C1–C6, each `pass` or `fail` per model condition per run. Per-run per-condition score is the count of criteria passed (0–6). Apply the pre-registered `## Criterion dependency rule` and the `## Judge protocol` from `case.md`. Do not score against generic or remembered criteria.

This is an **unscored scaffold**. The case is `status: draft`, `scoring_status: unscored`; no model has been run. The tables below are the shape the judges fill after a frozen, anonymised run. The frozen-run definition — the five condition packet recipes, the equal-length filler recipe, run parameters, seeds, the anonymisation rule, the answer-key locality, the judge-packet protocol, and a freeze checklist — is in `run-packet.md` for benchmark version `diagnosis-vs-validated-learning-benefits-renewal-v2-v1`; that packet is **prepared but not yet frozen or run**.

## Result

partial — no runs yet. This is a fresh `draft` case: the Advisor prompt, rubric, dependency rule, pre-registered margins, falsifier, and `model_conditions` are defined but not yet frozen-and-run, so scoring is incomplete and the Result is `partial` per `docs/eval-result-status-policy.md`. The Result is not eligible to move above `partial` until a frozen run is scored under the `## Judge protocol` and the `## Positive result` clauses in `case.md` are all met and judge-confirmed; `benchmark_supported` additionally requires the full `docs/eval-benchmark-upgrade.md` checklist. A `partial` result supports no public advice claim and is not eligible to support a canon candidate.

This score sheet has **two separate surfaces**, and they must not be merged:

- a **blind judge scoring surface** — judge-facing, anonymised, **no condition labels**;
- a **post-reconciliation condition aggregate** — operator-only, filled **after** blind scoring using the local-only answer key.

A judge sees only the first. Mixing the condition labels into the judge-facing surface would break the blind `## Judge protocol` in `case.md`.

## Blind judge scoring surface

Judge-facing. No runs scored yet. When a frozen run exists, every model output is anonymised to a stable label `OUT-NN` **before any judge sees it** — the generating condition is **withheld** and does not appear on this surface. Each judge records `pass`/`fail` for every criterion C1–C6 on every `OUT-NN`, applies the pre-registered `## Criterion dependency rule` from `case.md`, and writes one short reasoning note per output. At freeze time the output count is fixed (≥3 runs × 5 conditions) and one `OUT-NN` row is added per output.

Template — one table per judge; `OUT-NN` rows added at freeze/scoring time:

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total (0–6) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OUT-01 |  |  |  |  |  |  |  |
| OUT-02 |  |  |  |  |  |  |  |
| … | … | … | … | … | … | … | … |
| OUT-NN |  |  |  |  |  |  |  |

No condition name appears on this surface. A judge who can tell which condition produced an `OUT-NN` is not scoring blind.

## Post-reconciliation condition aggregate

**Operator-only — not judge-facing. Do not show during scoring.** No runs scored yet. This surface is filled **only after** blind scoring is complete, by mapping each `OUT-NN` back to its condition with the local-only (git-ignored) answer key. It carries the condition identities the blind surface withholds.

Template — per-condition, after reconciliation:

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | criteria_prompted_no_sources |
| --- | --- | --- | --- | --- | --- |
| C1 Identifies live tension |  |  |  |  |  |
| C2 Anchors in scenario facts |  |  |  |  |  |
| C3 Preserves diagnosis-first objection |  |  |  |  |  |
| C4 Preserves validated-learning objection |  |  |  |  |  |
| C5 No flattening |  |  |  |  |  |
| C6 Honest recommendation under constraint |  |  |  |  |  |
| **Per-condition mean score (0–6)** |  |  |  |  |  |

## Comparative signal

**Operator-only, post-reconciliation — not judge-facing.** No runs scored. When scored, this section records, from the reconciled aggregate above: mean score per condition; the `substrate_workflow` vs `vanilla_long_prompt` and vs `criteria_prompted_no_sources` aggregate margins against the pre-registered ≥1.5-point bar; the C4/C5/C6 pass-rate margins against the pre-registered ≥0.33 bar; and whether the `## Falsifier` is met. Per `case.md`, a substrate win requires clearing every `## Positive result` clause; a judge-dependent outcome stays `partial`.

## Judge Notes

None yet — the case is unscored. After a frozen run, outputs are anonymised to `OUT-NN` before any judge sees them. This section records each judge's identity and model family, their condition-blind per-`OUT-NN` criterion verdicts (C1–C6) and short reasoning, any third-judge trigger on C5/C6 or margin disagreement, and whether the outcome is judge-sensitive (which keeps the Result `partial`). The `OUT-NN` → condition mapping is applied only after blind scoring is complete and lives in the post-reconciliation surface above, never in the judge-facing notes.

---
case_id: managerial-output-vs-industry-structure
benchmark_version: managerial-output-vs-industry-structure-v1
artifact: independent-judge-reconciliation
judge_model_id: gemma4:31b
judge_receipt: judge-packet/independent-judge-score-gemma4-31b.md
judge_receipt_sha256: af35b4e84eb46f000614e8486b1798925421955343d56360c95dc579c453cb23
answer_key_source: local-only OUT-NN -> condition answer key (git-ignored; not committed; not reproduced here)
reconciliation_verdict: weakened
result_status: partial
benchmark_supported: false
note: Post-judging de-blinded analysis. It names conditions and is NOT a blind judging material — it must not be shown to a judge during a pass. It changes no eval Result and promotes nothing.
---

# Independent Judge Reconciliation — gemma4:31b

This receipt reconciles the **blind** judge scores in
`judge-packet/independent-judge-score-gemma4-31b.md`
(sha256 `af35b4e84eb46f000614e8486b1798925421955343d56360c95dc579c453cb23`)
back to the eval conditions, using the local-only `OUT-NN` → condition answer
key. The answer key is git-ignored and is **not** committed or reproduced
here; only the per-condition aggregates below are public.

`gemma4:31b` (Gemma family) scored the fifteen answers blind — it did not know
which condition produced any answer. It is a different model family from the
`qwen3.5:latest` generator, but the pass was orchestrated by the eval agent,
so it is **not** a fully independent third-party or human judge.

## Aggregate score by condition — blind judge (gemma4:31b)

Per-condition pass-count (0–5) for the three runs, and the mean.

| Condition | Run 1 | Run 2 | Run 3 | Mean |
|---|---|---|---|---|
| `substrate_workflow` | 5 | 5 | 3 | 4.33 |
| `vanilla_long_prompt` (equal-length control) | 3 | 5 | 3 | 3.67 |
| `optional_local_model` | 3 | 3 | 3 | 3.00 |
| `vanilla` | 3 | 2 | 3 | 2.67 |
| `famous_sources_supplied` | 3 | 1 | 3 | 2.33 |

Blind ranking by mean: `substrate_workflow` (4.33) > `vanilla_long_prompt`
(3.67) > `optional_local_model` (3.00) > `vanilla` (2.67) >
`famous_sources_supplied` (2.33).

## Substrate vs each baseline — blind judge

| Comparison | Blind delta (mean) | Prior orchestrator delta (mean) |
|---|---|---|
| `substrate_workflow` − `vanilla` | +1.67 | +3.0 |
| `substrate_workflow` − `vanilla_long_prompt` (control) | **+0.67** | +3.0 |
| `substrate_workflow` − `famous_sources_supplied` | +2.00 | +4.0 |
| `substrate_workflow` − `optional_local_model` | +1.33 | +3.0 |

**Does `substrate_workflow` still beat `vanilla_long_prompt`?** Only
marginally, and not robustly. On the mean, yes — 4.33 vs 3.67, a +0.67 edge.
But the per-run distributions overlap: the equal-length control produced a
5/5 run that ties the substrate's two best runs, and the substrate produced a
3/5 run that drops into the control's typical band. There is no clean
across-runs separation. The case's decisive test (`case.md` → `## Positive
result` / `## Falsifier`) is a substrate win over the equal-length control
*across runs*, to show the gain is lineage content and not prompt length.
Under blind judging that win is not robust.

## Comparison to the prior orchestrator scoring

The earlier pass recorded in `score-sheet.md` was scored by Claude Opus 4.7 —
the agent that orchestrated the eval and is associated with the substrate.
That pass scored `substrate_workflow` 5/5 on every run and every baseline at
2/5 or 1/5: a clean, stable, three-point substrate win over every baseline,
including the equal-length control.

| Condition | Prior mean (orchestrator) | Blind mean (gemma4:31b) |
|---|---|---|
| `substrate_workflow` | 5.00 | 4.33 |
| `vanilla_long_prompt` | 2.00 | 3.67 |
| `optional_local_model` | 2.00 | 3.00 |
| `vanilla` | 2.00 | 2.67 |
| `famous_sources_supplied` | 1.00 | 2.33 |

The two passes disagree most where it matters. Under blind judging the
equal-length control rises from a mean of 2.00 to 3.67 — it becomes the
second-strongest condition, well above bare `vanilla` — and the
substrate-over-control margin collapses from +3.0 to +0.67. The blind judge,
not knowing which answer was the substrate, did not reproduce the clean
separation the non-independent judge recorded. This is consistent with the
prior judge having scored the substrate generously; it is the divergence an
independent blind pass exists to surface.

## Verdict

**Weakened.** The earlier orchestrator-judged result does not survive blind
judging intact. The substrate condition still has the highest mean, so the
case is not *falsified* or *contradicted* — but the result is no longer the
clean, stable substrate dominance the score sheet records. The decisive
comparison — substrate vs the equal-length control — is **inconclusive** under
blind judging: a +0.67 mean edge with overlapping per-run distributions does
not establish that the substrate's advantage is lineage content rather than
prompt length. The blind pass does not confirm the substrate hypothesis at
benchmark strength.

## Status implication

The case `## Result` stays **`partial`** — this reconciliation does not lift
it and does not promote it. Beyond that, this is an explicit **non-promotion
note**: the case must **not** advance toward `benchmark_supported` on the
current evidence. The remaining gap is no longer just "add an independent
judge" — the one separate-model-family blind pass run so far *weakened* the
substrate signal. Before this case could support a `benchmark_supported`
result it would need, at minimum: more runs per condition, a fully
independent third-party or human judge (not orchestrated by the eval agent),
and a substrate win over the equal-length control that is robust across runs
— none of which the current evidence provides.

## Scope and limits

This is one case, one generator model family (`qwen3.5:latest`), and one
blind judge model (`gemma4:31b`) that is a separate model family but still
orchestrated by the eval agent — not a fully independent third-party or human
judge. The sample is three runs per condition. No conclusion here generalises
beyond this case.

A model output is a test artifact — never an authority, never citable as a
source. A judge's score of a model output is likewise a test artifact: it is
evidence about how one judge model scored one set of answers under one rubric,
not evidence about the world and not an advice claim.

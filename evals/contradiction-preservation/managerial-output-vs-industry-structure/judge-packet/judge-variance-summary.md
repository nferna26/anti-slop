---
case_id: managerial-output-vs-industry-structure
benchmark_version: managerial-output-vs-industry-structure-v1
artifact: judge-variance-summary
result_status: partial
eval_decision: do_not_promote
judges: orchestrator (claude-opus-4-7), blind (gemma4:31b), blind (gpt-5.4-mini)
answer_key_source: local-only OUT-NN -> condition answer key (git-ignored; not committed; not reproduced here)
note: Post-judging de-blinded analysis. Aggregate-only. It names conditions and is NOT a blind judging material. It changes no eval Result and promotes nothing.
---

# Judge-Variance Summary — managerial-output-vs-industry-structure

The fifteen answers in this case have now been scored by **three judges**. This
receipt reconciles the third (a hosted OpenAI blind pass) to conditions and
compares all three. It is aggregate-only — no `OUT-NN` → condition mapping is
committed. It changes no score and no `## Result`; the case stays `partial`.

## The three judges

| Judge | Independence | Source |
|---|---|---|
| Claude Opus 4.7 (orchestrator) | **Not independent** — the agent that built the substrate and ran the eval | `score-sheet.md` |
| `gemma4:31b` (blind) | Separate model family; orchestrated by the eval agent | `judge-packet/independent-judge-score-gemma4-31b.md` (sha256 `af35b4e8…`) |
| `gpt-5.4-mini` (blind) | Hosted third-party provider; user-run pass | `judge-packet/independent-judge-score-openai-gpt-5.4-mini.md` (sha256 `c1a164cc…`) |

Each blind judge scored without knowing which condition produced any answer.

## Per-condition mean by judge

| Condition | Orchestrator (Claude) | Blind (gemma4:31b) | Blind (gpt-5.4-mini) |
|---|---|---|---|
| `substrate_workflow` | 5.00 | 4.33 | **3.67** |
| `vanilla` | 2.00 | 2.67 | 4.00 |
| `vanilla_long_prompt` (equal-length control) | 2.00 | 3.67 | 4.00 |
| `famous_sources_supplied` | 1.00 | 2.33 | 4.00 |
| `optional_local_model` | 2.00 | 3.00 | 4.00 |

## OpenAI gpt-5.4-mini reconciliation

Per-condition run scores (0–5) and means under the hosted blind judge:

| Condition | Run 1 | Run 2 | Run 3 | Mean |
|---|---|---|---|---|
| `substrate_workflow` | 5 | 4 | 2 | 3.67 |
| `vanilla` | 4 | 4 | 4 | 4.00 |
| `vanilla_long_prompt` | 4 | 4 | 4 | 4.00 |
| `famous_sources_supplied` | 4 | 4 | 4 | 4.00 |
| `optional_local_model` | 4 | 4 | 4 | 4.00 |

Substrate vs each baseline (mean delta), gpt-5.4-mini:

| Comparison | Delta |
|---|---|
| `substrate_workflow` − `vanilla` | **−0.33** |
| `substrate_workflow` − `vanilla_long_prompt` (control) | **−0.33** |
| `substrate_workflow` − `famous_sources_supplied` | −0.33 |
| `substrate_workflow` − `optional_local_model` | −0.33 |

Under gpt-5.4-mini the substrate condition is the **lowest-scoring** of the
five — it loses to every baseline, including the equal-length control, by
0.33. One substrate run (run 3) scored 2/5: the judge failed it on
`Lineage and authority discipline` and `Honest recommendation`, reading its
heavy citation of the supplied cards as wielding them "as if they settle the
issue." The substrate's own mechanism — citing the lineage artifacts — counted
against it under this judge.

## Do the judges agree on rank order?

**No.** The orchestrator and `gemma4:31b` both rank `substrate_workflow` first.
`gpt-5.4-mini` ranks it **last** (every baseline tied at 4.00 above it). The
substrate's position is not stable across judges — it moves from clear first
to clear last.

## Is the substrate-over-control result robust across judges?

**No.** The decisive comparison — `substrate_workflow` vs the equal-length
control `vanilla_long_prompt` — does not survive:

| Judge | substrate − vanilla_long_prompt |
|---|---|
| Orchestrator (Claude, non-independent) | +3.00 |
| Blind (gemma4:31b) | +0.67 |
| Blind (gpt-5.4-mini) | **−0.33** |

The margin shrinks monotonically as the judge becomes more independent of the
substrate, and under the hosted third-party judge it goes **negative** — the
token-matched no-substrate control out-scores the substrate. The substrate's
apparent advantage is judge-dependent, not a stable property of the substrate.

## Judge-variance observation

The judges diverge most on `Honest recommendation`. `gpt-5.4-mini` passed that
criterion on 14 of 15 answers — its reasoning repeatedly credits a
"conditional and evidence-based" recommendation with a "plan," "timeline," or
"90-day criterion," and it passes the criterion even when the same answer
**fails** `No flattening`. The rubric's `Honest recommendation` criterion
asks whether the recommendation *preserves the open attribution question*;
`gpt-5.4-mini` effectively scored it as *is the recommendation grounded and
specific*. That looser reading lifts every baseline to a flat 4.00. The other
two judges coupled `Honest recommendation` to tension-preservation and failed
it wherever the answer flattened. So the cross-judge spread is partly a real
disagreement about answer quality and partly a divergence in how a rubric
criterion is read — which is itself a reason no single pass here is decisive.

## Decision implication

This reinforces the standing decision in `eval-decision.md`:
`eval_decision: do_not_promote`, `## Result` stays `partial`. Three judges do
not agree, the substrate-over-control result is not robust, and under the most
independent judge the substrate is the worst condition. The earlier clean
substrate "win" is best read as a judging artifact of the non-independent
orchestrator pass, not as substrate evidence. The case must not be promoted
to `benchmark_supported` and must not be cited as benchmark-supported
evidence. No single judge here is authoritative — the point is that they
disagree, and that disagreement is itself the finding: this case is not
benchmark-ready.

A model output, and a judge's score of one, is a test artifact — never an
authority. This summary is evidence about judge behaviour under one rubric on
one case; it is not evidence about the world and not an advice claim.

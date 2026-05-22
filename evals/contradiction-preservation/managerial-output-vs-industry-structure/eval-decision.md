---
case_id: managerial-output-vs-industry-structure
benchmark_version: managerial-output-vs-industry-structure-v1
artifact: eval-decision
eval_decision: do_not_promote
decision_class: weakened_by_blind_judge
result_status: partial
decision_date: 2026-05-21
decision_summary: Independent blind judging weakened the substrate-vs-equal-length-control comparison; the case stays partial — do not promote and do not cite as benchmark-supported.
---

# Eval Decision — managerial-output-vs-industry-structure

A first-class, public-safe decision record for the eval case in this folder.
It sits on top of `score-sheet.md` → `## Result`; it does **not** change the
Result status and is not itself a Result status. See
`docs/eval-lab-protocol.md` → "Eval-decision receipts" for what this artifact
is and what it may and may not do.

## Status

`## Result` remains **`partial`** (`score-sheet.md`). This decision record does
not lift, lower, or replace it.

## Decision

**Do not promote. Do not cite as benchmark-supported.** This case must not be
advanced to `benchmark_supported`, and it must not be cited — by a canon
candidate or anywhere else — as benchmark evidence that the substrate produces
better advice.

`decision_class: weakened_by_blind_judge`.

## Reason

The case was first scored by the agent that orchestrated the eval (Claude Opus
4.7), which recorded a clean substrate win — `substrate_workflow` 5/5 on every
run, every baseline at 2/5 or 1/5, a three-point gap over the equal-length
control on every run.

That result did not survive an independent blind judge pass. `gemma4:31b`
(Gemma family — a different model family from the `qwen3.5:latest` generator)
re-scored the fifteen answers blind, and the reconciliation
(`judge-packet/independent-judge-reconciliation-gemma4-31b.md`, sha256
`0e6bf9e1394bca0cb138e7cc6b6e1c7a5efbe4bc3b1776969e50518918324cdf`) found:

- `substrate_workflow` still has the highest blind mean (4.33), but
- its margin over the equal-length control `vanilla_long_prompt` collapsed from
  +3.0 (orchestrator pass) to **+0.67**, and
- the per-run distributions overlap — the control produced a 5/5 run and the
  substrate a 3/5 run.

The case's decisive test (`case.md` → `## Positive result` / `## Falsifier`) is
a substrate win over the equal-length control *across runs*, to show the gain
is lineage content and not prompt length. Under blind judging that win is not
robust.

## Current classification

**Weakened / inconclusive — not falsified, not confirmed.**

- Not *confirmed*: the blind pass does not show a robust substrate-over-control
  win, so the substrate hypothesis is not supported at benchmark strength.
- Not *falsified*: `substrate_workflow` still holds the highest blind mean and
  a positive (if small) margin over every baseline, so the case's `## Falsifier`
  is not cleanly met.
- The decisive substrate-vs-control comparison is **inconclusive** under blind
  judging; the earlier clean result is **weakened**.

## Next evidence needed

Before this case could support a `benchmark_supported` result it would need, at
minimum, all of:

1. **More runs per condition** — the current three runs leave the substrate and
   the control with overlapping distributions; more runs are needed to tell a
   real gap from noise.
2. **A fully independent judge** — a third-party model not orchestrated by the
   eval agent, or a human judge, or a two-judge panel. `gemma4:31b` is a
   separate model family but the pass was orchestrated by the eval agent.
3. **A robust substrate-over-control win** — `substrate_workflow` beating the
   equal-length control `vanilla_long_prompt` clearly and across runs, not by a
   sub-point mean margin with overlapping distributions.

Until all three hold, the case stays `partial` and this non-promotion decision
stands.

## Artifacts

- `score-sheet.md` — `## Result` (`partial`) and `## Independent blind judge
  reconciliation`.
- `run-packet.md` — `## Judge packet` and `## Status`.
- `judge-packet/independent-judge-score-gemma4-31b.md` — the blind judge scores.
- `judge-packet/independent-judge-reconciliation-gemma4-31b.md` — the
  aggregate reconciliation.

## Discipline note

A model output is a test artifact — never an authority, never citable as a
source. A judge's score of a model output is likewise a test artifact: it is
evidence about how one judge scored one set of answers under one rubric, not
evidence about the world and not an advice claim. This decision record is an
operating decision about the eval case; it confers no authority on any model
output, judge score, or substrate claim.

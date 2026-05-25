---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v2-v1
artifact: eval-decision
eval_decision: do_not_promote
decision_class: judge_sensitive_controls_matched
result_status: partial
decision_date: 2026-05-22
decision_summary: Two condition-blind judge passes do not meet the pre-registered positive rule; the criteria-prompted control matches the substrate under Claude Opus, and C5/C6 disagreement triggers the third-judge rule. The case stays partial and must not be cited as benchmark-supported.
---

# Eval Decision — diagnosis-vs-validated-learning-benefits-renewal-v2

This is a public-safe decision record for the eval case in this folder. It sits on top of `score-sheet.md` → `## Result`; it does **not** change, lower, or replace the Result status and is not itself a Result status.

## Status

`## Result` remains **`partial`** (`score-sheet.md`). The case has forty real generator outputs and two condition-blind judge receipts, but the reconciliation does not support a status lift.

## Decision

**Do not promote. Do not cite as benchmark-supported.** This case must not be advanced to `benchmark_supported`, and it must not be cited by a canon candidate or public claim as benchmark evidence that the substrate improves contradiction preservation.

`decision_class: judge_sensitive_controls_matched`.

## Reason

The two judge receipts were reconciled aggregate-only in `judge-packet/judge-variance-summary.md`. The local-only answer key was used to compute condition aggregates, but the `OUT-NN` to condition mapping remains uncommitted.

Neither judge meets the case's pre-registered positive rule:

- `gpt-oss:20b` scores `substrate_workflow` highest (mean 4.25) and far above the equal-length control `vanilla_long_prompt` (mean 1.00), but the substrate beats `criteria_prompted_no_sources` by only +1.25, below the +1.5 aggregate-margin bar, and it misses the C4 critical-criterion margin over both controls.
- Claude Opus 4.7 scores `substrate_workflow` at 6.00, but also scores `criteria_prompted_no_sources`, `vanilla`, and `famous_sources_supplied` at 6.00. Under that judge, the substrate does not separate from the criteria-prompted control, bare prompt, or famous-source-name control.

The judge disagreement is also large enough to trigger the case's third-judge rule: C5 differs on 20 of 40 outputs, and C6 differs on 22 of 40 outputs. A judge-sensitive outcome stays `partial`; a win that depends on which judge is chosen is not a win.

## Current classification

**Judge-sensitive / control-matched / not promoted.**

- Not confirmed: neither judge meets the full positive rule.
- Not benchmark-ready: the third-judge trigger is unresolved, and the Claude Opus pass is not independent of the orchestrator.
- Not cleanly final-falsified: the first judge still sees a large substrate-over-length-control margin, so the conservative decision is non-promotion, not a claimed falsification.

## Next evidence needed

Before this case could support any stronger Result, it would need all of:

1. A genuinely independent third judge or human judge to resolve the C5/C6 disagreement.
2. Substrate separation from `criteria_prompted_no_sources`, not only from the equal-length control.
3. Judge-level agreement that the substrate clears the pre-registered aggregate and critical-criterion margins.

Until then, the case stays `partial` and this non-promotion decision stands.

## Discipline note

A model output is a test artifact — never an authority, never citable as a source. A judge's score of a model output is likewise a test artifact: it is evidence about how one judge scored one set of answers under one rubric, not evidence about the world and not an advice claim. This decision record confers no authority on any model output, judge score, source card, or tension card.

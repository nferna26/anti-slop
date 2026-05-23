---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v3
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v3-v1
artifact: eval-decision
eval_decision: do_not_promote
decision_class: c4_saturation_and_judge_count_insufficient
result_status: partial
decision_date: 2026-05-22
decision_summary: The aggregate reconciliation under the eligible independent OpenAI gpt-5.4-mini judge shows substrate_workflow clearing every total-score margin but failing the C4 critical-criterion margin against vanilla_long_prompt (C4 saturation, +0.00). The case also has only 1 of >=2 eligible judges. Both failures independently block promotion; the case stays partial and must not be cited as benchmark-supported.
---

# Eval Decision — diagnosis-vs-validated-learning-benefits-renewal-v3

Public-safe decision record for the eval case in this folder. It sits on top of
`score-sheet.md` → `## Result`; it does **not** change, lower, or replace the
Result status and is not itself a Result status.

## Status

`## Result` remains **`partial`** (`score-sheet.md`). The case has forty real
generator outputs and two blind-judge score receipts, and aggregate-only
reconciliation has been done from committed hashes, but the reconciled aggregate
does not meet the pre-registered `## Positive result` rule.

## Decision

**Do not promote. Do not cite as benchmark-supported.** This case must not be
advanced to `benchmark_supported`, and it must not be cited by a canon
candidate or any public claim as benchmark evidence that the substrate improves
contradiction preservation.

`decision_class: c4_saturation_and_judge_count_insufficient`.

## Reason

Two pre-registered Positive-result clauses independently fail. Either alone is
sufficient to block promotion.

### Clause 1 — Judge eligibility (procedural)

The case `## Positive result` requires **at least two eligible blind judges
from different model families**, with **at least one independent of the
orchestrating agent**. Only **one** eligible judge is on record:

- `gpt-oss:20b` — failed the calibration gate; scored no `OUT-NN`.
- Claude Opus 4.7 — scored all 40 `OUT-NN` but is the orchestrating agent with
  a circular calibration; a judge-variance data point only, does **not** count
  toward the two-judge minimum.
- OpenAI `gpt-5.4-mini` — passed calibration exactly; the first eligible,
  independent pass.

This case has 1 of the ≥2 eligible judges the rule demands.

### Clause 2 — C4 critical-criterion margin (substantive)

Under the eligible independent judge (OpenAI `gpt-5.4-mini`),
`substrate_workflow` clears every other Positive-result clause: total-score
margins of +2.250 over `vanilla_long_prompt`, +1.375 over
`generic_advice_prompted`, +1.875 over `famous_sources_supplied`, and +2.625
over `vanilla` (all above the pre-registered bars); judge-stability margins of
+2.250 and +1.375 over the two controls; substrate C5 and C6 pass rates at
0.875 (both ≥0.60). But the C4 pass-rate margin against `vanilla_long_prompt`
is **+0.000** — substrate C4 = 1.00 and `vanilla_long_prompt` C4 = 1.00 —
against the required **≥0.20** bar. This is **C4 saturation against the
equal-length control**: under this judge, C4 ("Detects and uses the
under-evidence problem") is easy enough that `vanilla_long_prompt` answers pass
it as readily as substrate answers (both at 1.00), so the criterion does not
discriminate.

This triggers the `## Falsifier` clause "`substrate_workflow` wins total score
but does not win C3, C4, C5, and C6 against both controls."

### Non-independent Claude Opus aggregate (judge-variance reference only)

The non-independent Claude Opus pass exhibits a different shape: it gives
`generic_advice_prompted` a mean total of 5.250 against `substrate_workflow`'s
5.625 — a margin of only +0.375, well below the +1.0 bar — and the C3/C4/C5/C6
margins against `generic_advice_prompted` all fail under that judge. This is
the v2 failure pattern (criteria-style controls saturating against the
substrate); under v3's rubric and a different judge it shows up against the
generic-advice control rather than the criteria-prompted control. The Claude
Opus pass is recorded as judge-variance and does **not** count toward the
two-judge minimum.

## Reconciliation method (post-hoc, committed sources only)

The `OUT-NN` → condition mapping was reconstructed from **committed hashes**:
`judge-packet/output-manifest.yaml` carries the `output_sha256` of each
`OUT-NN`, and the `model-outputs/<condition>.md` receipts carry both the body
(its `sha256` equals the manifest value) and the `model_condition` frontmatter
field; the mapping is the `sha256` join. All forty rows matched. The mapping
was withheld from the judge packet (no judge saw it), not from the repo — that
is the correct claim, and post-hoc reconciliation from committed sources is the
intended design. **No per-`OUT-NN` → condition mapping is committed.** Only
aggregate condition statistics are recorded in `score-sheet.md`
→ `## Post-reconciliation condition aggregate`. The local-only answer key was
not read for this reconciliation.

## Current classification

**`do_not_promote` — Positive-result rule unmet.** The case remains a strong
methodology record (frozen run, condition-blind judging, calibration gate,
operator-accepted anchors, a hosted eligible independent judge pass) but does
not meet the v3 promotion bar.

## Next evidence needed

Before this case could support any stronger Result, it would need at minimum:

1. **A second eligible independent judge** — a different model family from
   OpenAI gpt-5.4-mini, calibration-passing — so the two-judge minimum is met.
2. **A C4 resolution against the equal-length control** — the C4 criterion is
   saturating against `vanilla_long_prompt` under the current judge. Either the
   v3 rubric's C4 needs sharpening (this is a v3 design lesson — the C4 fix
   from v2 may not have gone far enough), or the case scenario needs a tweak
   that makes the under-evidence problem harder for an unprimed long-prompt
   answer to surface.
3. **Judge agreement** — once a second eligible judge scores, both judges must
   independently show substrate beating both controls by ≥0.75 on mean total,
   and both must clear the critical-criterion margins; a judge-sensitive
   outcome stays `partial`.

Until those are in place, `do_not_promote` stands.

## Discipline note

A model output is a test artifact — never an authority, never citable as a
source. A judge's score of one is likewise a test artifact: it is evidence
about how one judge scored one set of answers under one rubric, not evidence
about the world and not an advice claim. This decision record confers no
authority on any model output, judge score, source card, or tension card.

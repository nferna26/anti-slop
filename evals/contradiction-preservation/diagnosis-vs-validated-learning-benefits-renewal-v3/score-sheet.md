---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v3
eval_type: contradiction-preservation
scoring_status: unscored
---

# Score Sheet

Score against the rubric in this case's `case.md` -> `## Scoring rubric`: six
binary criteria C1-C6, each `pass` or `fail` per anonymised output. Apply the
pre-registered `## Criterion dependency rule` and `## Judge protocol` from
`case.md`. Do not score against generic or remembered criteria.

This score sheet is **unscored**. The frozen
`diagnosis-vs-validated-learning-benefits-renewal-v3-v1` benchmark pass has been
**run** — forty real `gemma4:31b` outputs, eight per condition, recorded under
`model-outputs/` and anonymised into the condition-blind `judge-packet/` (see
`run-packet.md` → `## Run`) — but **no judge has scored anything** and no
condition aggregate has been reconciled.

## Result

partial - the frozen `diagnosis-vs-validated-learning-benefits-renewal-v3-v1`
benchmark pass has been run (forty real `gemma4:31b` outputs, eight per
condition, no simulations and no deferrals — see `run-packet.md`), but **no
scoring has been done**: `scoring_status` is `unscored` and the surfaces below
are empty. This result supports no public advice claim and is not eligible to
support a canon candidate.

This score sheet has two separate surfaces, and they must not be merged:

- a **blind judge scoring surface** - judge-facing, anonymised, no condition labels;
- a **post-reconciliation condition aggregate** - operator-only, filled only after
  blind scoring using the local-only answer key.

## Calibration gate

Before a future judge scores any real `OUT-NN` output, the judge must complete the
calibration-anchor step described in `case.md` and
`judge-packet/calibration-anchors.md`.

A judge is eligible only if its anchor pass/fail verdicts differ from the reference
by no more than two criteria total and do not differ on C5 or C6 for any anchor,
unless the operator explicitly accepts the judge with a recorded limitation. A
miscalibrated judge does not count toward the two-judge minimum for any Result lift
above `partial`.

## Blind judge scoring surface

Judge-facing. The frozen run is complete: its forty outputs are anonymised in
`judge-packet/outputs/` as `OUT-01 … OUT-40`. This surface is not yet filled — no
judge has scored. The generating condition is withheld and must not appear here.

Template - one table per eligible judge:

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total (0-6) | Short rationale |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- |
| OUT-01 |  |  |  |  |  |  |  |  |
| OUT-02 |  |  |  |  |  |  |  |  |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| OUT-NN |  |  |  |  |  |  |  |  |

No condition name appears on this surface. A judge who can tell which condition
produced an `OUT-NN` is not scoring blind.

## Post-reconciliation condition aggregate

**Operator-only - not judge-facing. Do not show during scoring.** This surface is
filled only after blind scoring is complete, by mapping each `OUT-NN` back to its
condition with the local-only answer key.

| Judge | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | generic_advice_prompted |
| --- | ---: | ---: | ---: | ---: | ---: |
| <judge-id> mean (0-6) |  |  |  |  |  |
| <judge-id> C3 pass rate |  |  |  |  |  |
| <judge-id> C4 pass rate |  |  |  |  |  |
| <judge-id> C5 pass rate |  |  |  |  |  |
| <judge-id> C6 pass rate |  |  |  |  |  |

## Comparative signal

None yet - v3 has not been run or scored. The future comparative signal is defined
by `case.md` -> `## Positive result` and `## Falsifier`: the substrate must separate
from both the equal-length control and the generic-advice control on total score and
on C3-C6, under eligible blind judges.

## Judge Notes

**Update (2026-05-22) — first blind-judge calibration attempt.** `gpt-oss:20b`
(non-Gemma) attempted the calibration gate; see
`judge-packet/judge-calibration-gpt-oss-20b.md`. It **failed** the gate — it
disagreed with the reference verdicts on C5 and C6 for the borderline anchor —
so per the `## Judge protocol` it scored **no** `OUT-NN` outputs. No eligible
judge exists yet; a second judge pass with an eligible (calibrated) judge, and
only then reconciliation, are still pending. The scoring surfaces above stay
empty, `scoring_status` stays `unscored`, and `## Result` stays `partial`.

Future judge notes must record:

- judge identity, model family or human role, and whether the judge is independent
  of the orchestrating agent;
- calibration-anchor results and whether the judge was eligible;
- condition-blind per-`OUT-NN` C1-C6 verdicts, totals, and rationales;
- any third-judge trigger or operator limitation;
- confirmation that the `OUT-NN` -> condition mapping stayed local-only until
  reconciliation.

## Follow-up

- `judge-packet/calibration-anchors.md` is operator-accepted (`filled_pre_run`).
- The frozen `diagnosis-vs-validated-learning-benefits-renewal-v3-v1` benchmark
  pass has been **run** — forty real `gemma4:31b` outputs under `model-outputs/`,
  anonymised into the condition-blind `judge-packet/` (see `run-packet.md` →
  `## Run`). No judge has scored anything.
- A later judge goal runs the calibration step and the blind scoring; only then
  is reconciliation done. `scoring_status` stays `unscored` and `## Result` stays
  `partial` until the case is fully scored and reconciled.

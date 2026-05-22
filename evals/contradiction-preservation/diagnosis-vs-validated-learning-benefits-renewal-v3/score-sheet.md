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
`run-packet.md` → `## Run`). Three blind-judge attempts are on record:
`gpt-oss:20b` **failed the calibration gate** and scored nothing; Claude Opus 4.7
scored all 40 `OUT-NN` (`judge-packet/judge-score-claude-opus.md`) but is **not
independent of the orchestrator** with a **circular** calibration; and hosted
OpenAI `gpt-5.4-mini` (`judge-packet/judge-score-openai-gpt-5.4-mini.md`) **passed
the calibration gate** and scored all 40 `OUT-NN` — the first eligible,
**independent** v3 judge pass. No `OUT-NN` -> condition reconciliation has
occurred and no `## Result` decision is made here — see `## Judge Notes`.

## Result

partial - the frozen `diagnosis-vs-validated-learning-benefits-renewal-v3-v1`
benchmark pass has been run (forty real `gemma4:31b` outputs, eight per
condition, no simulations and no deferrals — see `run-packet.md`); two
blind-judge score receipts now exist under `judge-packet/` — Claude Opus 4.7
(non-independent and circularly calibrated; a judge-variance data point only)
and hosted OpenAI `gpt-5.4-mini` (calibration passed exactly; the first
eligible, independent pass) — but **no `OUT-NN` → condition reconciliation has
occurred, no post-reconciliation condition aggregate exists, and no
`## Positive result` decision has been made**, so `scoring_status` is `unscored`
and the post-reconciliation surface below stays empty. This result supports no
public advice claim and is not eligible to support a canon candidate.

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
`judge-packet/outputs/` as `OUT-01 … OUT-40`. This surface (the per-judge tables
below) is not yet transcribed; the recorded judge passes live in their own
receipts under `judge-packet/` — a non-independent Claude Opus pass
(`judge-score-claude-opus.md`) and an independent, calibration-passing hosted
OpenAI `gpt-5.4-mini` pass (`judge-score-openai-gpt-5.4-mini.md`); see
`## Judge Notes`. The generating condition is withheld and must not appear here.

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

None computed. The frozen v3-v1 run exists (40 real outputs). Three blind-judge
attempts are on record: `gpt-oss:20b` failed the calibration gate; Claude Opus
4.7 scored all 40 `OUT-NN` but is non-independent with a circular calibration;
and hosted OpenAI `gpt-5.4-mini` passed the calibration gate and scored all 40
`OUT-NN` (one eligible, independent pass). A comparative signal still requires
`OUT-NN` -> condition reconciliation, which has not occurred, and the
`## Positive result` rule judged under eligible judges. The future comparative
signal is defined by `case.md` -> `## Positive result` and `## Falsifier`: the
substrate must separate from both the equal-length control and the
generic-advice control on total score and on C3-C6, under eligible blind judges.

## Judge Notes

**Update (2026-05-22) — first blind-judge calibration attempt.** `gpt-oss:20b`
(non-Gemma) attempted the calibration gate; see
`judge-packet/judge-calibration-gpt-oss-20b.md`. It **failed** the gate — it
disagreed with the reference verdicts on C5 and C6 for the borderline anchor —
so per the `## Judge protocol` it scored **no** `OUT-NN` outputs. At the time of
this update no eligible judge had yet scored; later updates below record the
subsequent attempts. `scoring_status` stays `unscored`, and `## Result` stays
`partial`.

**Update (2026-05-22) — second blind-judge attempt (Claude Opus 4.7).** Claude
Opus 4.7 scored all 40 `OUT-NN` against C1-C6; see
`judge-packet/judge-score-claude-opus.md` (distribution 1/6 ×1, 2/6 ×12,
3/6 ×14, 6/6 ×13). It was *mechanically* eligible at the calibration gate
(0 differences from the reference), but that calibration is **circular** — Claude
Opus authored the rubric and the calibration anchors/reference — and the pass is
**not independent**: Claude Opus is the orchestrating agent. Per the
`## Judge protocol`, this pass is a judge-variance data point only; it does
**not** count toward the two-judge minimum and **cannot** support a `## Result`
lift. At the time of this update no eligible, independent judge pass existed —
see the next update, which records one. `scoring_status` stays `unscored`;
`## Result` stays `partial`.

**Update (2026-05-22) — independent blind judge pass (OpenAI gpt-5.4-mini).**
Hosted OpenAI `gpt-5.4-mini`, operated by the human operator outside Claude
Code, **passed the calibration gate exactly** (0 criteria differences, no C5/C6
disagreement) and scored all 40 `OUT-NN` against C1-C6; see
`judge-packet/judge-score-openai-gpt-5.4-mini.md` (distribution 2/6 ×2,
3/6 ×24, 6/6 ×14). It is the first v3 judge that is both eligible at the
calibration gate and **independent of the orchestrating agent** (it did not
author the rubric or the calibration anchors/reference, and is a different model
family from the generator). This step records the pass only — **no
reconciliation, no `OUT-NN` -> condition mapping, no `## Result` lift.** A
Result decision requires the full `## Positive result` rule met under eligible
judges and a separate reconciliation step. `scoring_status` stays `unscored`;
`## Result` stays `partial`.

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
  `## Run`).
- Three blind-judge attempts are on record: `gpt-oss:20b` failed the calibration
  gate (`judge-packet/judge-calibration-gpt-oss-20b.md`) and scored no `OUT-NN`;
  Claude Opus 4.7 scored all 40 `OUT-NN` (`judge-packet/judge-score-claude-opus.md`)
  but is non-independent with a circular calibration; hosted OpenAI `gpt-5.4-mini`
  (`judge-packet/judge-score-openai-gpt-5.4-mini.md`) passed the calibration gate
  and scored all 40 `OUT-NN` — the first eligible, independent v3 judge pass.
- A later goal reconciles the recorded judge passes against `## Positive result`
  and `## Falsifier`, and only then is any `## Result` decision made.
  `scoring_status` stays `unscored` and `## Result` stays `partial` until the
  case is fully scored by eligible judges and reconciled.

---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v3
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score against the rubric in this case's `case.md` -> `## Scoring rubric`: six
binary criteria C1-C6, each `pass` or `fail` per anonymised output. Apply the
pre-registered `## Criterion dependency rule` and `## Judge protocol` from
`case.md`. Do not score against generic or remembered criteria.

This score sheet is **scored** (`scoring_status: scored`, reconciliation done).
The frozen `diagnosis-vs-validated-learning-benefits-renewal-v3-v1` benchmark
pass has been **run** — forty real `gemma4:31b` outputs, eight per condition,
recorded under `model-outputs/` and anonymised into the condition-blind
`judge-packet/` (see `run-packet.md` → `## Run`). Three blind-judge attempts
are on record: `gpt-oss:20b` **failed the calibration gate** and scored nothing;
Claude Opus 4.7 scored all 40 `OUT-NN`
(`judge-packet/judge-score-claude-opus.md`) but is **not independent of the
orchestrator** with a **circular** calibration; and hosted OpenAI `gpt-5.4-mini`
(`judge-packet/judge-score-openai-gpt-5.4-mini.md`) **passed the calibration
gate** and scored all 40 `OUT-NN` — the first eligible, **independent** v3 judge
pass. Aggregate-only condition reconciliation has been done from committed
hashes (see `## Post-reconciliation condition aggregate`); the pre-registered
`## Positive result` rule is **not met** and `eval-decision.md` records
`do_not_promote`. `## Result` stays `partial`.

## Result

partial - the frozen `diagnosis-vs-validated-learning-benefits-renewal-v3-v1`
benchmark pass has been run (forty real `gemma4:31b` outputs, eight per
condition, no simulations and no deferrals — see `run-packet.md`); two
blind-judge score receipts now exist under `judge-packet/` — Claude Opus 4.7
(non-independent and circularly calibrated; a judge-variance data point only)
and hosted OpenAI `gpt-5.4-mini` (calibration passed exactly; the first
eligible, independent pass). Aggregate-only reconciliation has been done from
**committed hashes** (see `## Post-reconciliation condition aggregate` below);
the pre-registered `## Positive result` rule is **NOT met** — only 1 of ≥2
eligible judges, and under the eligible judge the C4 pass-rate margin against
`vanilla_long_prompt` is +0.00 (C4 saturation). `eval-decision.md` records
`do_not_promote` (`decision_class: c4_saturation_and_judge_count_insufficient`).
The case stays `partial`. This result supports no public advice claim and is
not eligible to support a canon candidate.

This score sheet has two separate surfaces, and they must not be merged:

- a **blind judge scoring surface** - judge-facing, anonymised, no condition labels;
- a **post-reconciliation condition aggregate** - operator-only, filled only
  after blind scoring; the `OUT-NN` -> condition mapping for this case was
  reconstructed from committed hashes (`output-manifest.yaml` joined to
  `model-outputs/*.md` by body `sha256`) — the local-only answer key was not
  read for this reconciliation, and no per-`OUT-NN` -> condition mapping is
  committed.

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

**Operator-only - not judge-facing. Do not show during scoring.** Aggregate-only
post-hoc reconciliation. The `OUT-NN` -> condition mapping was reconstructed
from **committed hashes** — `judge-packet/output-manifest.yaml` carries the body
sha256 of each `OUT-NN`, and the `model-outputs/<condition>.md` receipts carry
both the body and the `model_condition` field; the mapping is the sha256 join.
The mapping was withheld from the judge packet, not from the repo; this surface
records aggregate condition statistics only. **No per-`OUT-NN` -> condition
mapping is committed.** No condition aggregate authority is conferred on any
score: model outputs and judge scores are test artifacts, not authorities.

Independent-judge aggregate (OpenAI `gpt-5.4-mini`, calibration-passing,
independent of orchestrator; n=8 per condition):

| Statistic | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | generic_advice_prompted |
| --- | ---: | ---: | ---: | ---: | ---: |
| mean total (0-6) | 3.000 | 3.750 | 5.625 | 3.375 | 4.250 |
| C1 pass rate | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| C2 pass rate | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| C3 pass rate | 0.00 | 0.25 | 0.88 | 0.12 | 0.62 |
| C4 pass rate | 1.00 | 1.00 | 1.00 | 1.00 | 0.62 |
| C5 pass rate | 0.00 | 0.25 | 0.88 | 0.12 | 0.50 |
| C6 pass rate | 0.00 | 0.25 | 0.88 | 0.12 | 0.50 |

Non-independent / circular Claude Opus aggregate (judge-variance reference
only — does **not** count toward the two-judge minimum; n=8 per condition):

| Statistic | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | generic_advice_prompted |
| --- | ---: | ---: | ---: | ---: | ---: |
| mean total (0-6) | 2.375 | 2.625 | 5.625 | 2.250 | 5.250 |
| C1 pass rate | 1.00 | 1.00 | 1.00 | 0.88 | 1.00 |
| C2 pass rate | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| C3 pass rate | 0.00 | 0.00 | 0.88 | 0.00 | 0.75 |
| C4 pass rate | 0.38 | 0.62 | 1.00 | 0.38 | 1.00 |
| C5 pass rate | 0.00 | 0.00 | 0.88 | 0.00 | 0.75 |
| C6 pass rate | 0.00 | 0.00 | 0.88 | 0.00 | 0.75 |

## Comparative signal

Aggregate-only reconciliation has been done from committed hashes; see the
`## Post-reconciliation condition aggregate` above. **The pre-registered
`## Positive result` rule is NOT met.** Two pre-registered clauses fail.

- **Judge eligibility.** The rule requires at least two eligible blind judges
  from different model families; only one eligible independent judge is on
  record (OpenAI `gpt-5.4-mini`). `gpt-oss:20b` failed calibration; Claude Opus
  is non-independent with a circular calibration and does not count.
- **C4 critical-criterion margin (OpenAI judge).** Under the eligible independent
  judge, `substrate_workflow` clears every total-score margin (+2.250 over
  `vanilla_long_prompt`, +1.375 over `generic_advice_prompted`, +1.875 over
  `famous_sources_supplied`, +2.625 over `vanilla`) and every other
  critical-criterion margin, **but its C4 pass rate (1.00) does not exceed
  `vanilla_long_prompt`'s C4 pass rate (1.00) — a margin of +0.00 against the
  required ≥0.20**. This is C4 saturation against the equal-length control: C4
  is too easy under this judge for the long-prompt control to discriminate.
  This triggers the `## Falsifier` clause "`substrate_workflow` wins total score
  but does not win C3, C4, C5, and C6 against both controls."

Non-independent Claude Opus margins (judge-variance reference only) further
show that even setting independence aside, the `substrate_workflow` mean
exceeds `generic_advice_prompted` by only +0.375 under that judge (well below
the +1.0 bar), and the C3/C4/C5/C6 margins against `generic_advice_prompted`
fail under that judge. The two judge passes thus also exhibit substrate
divergence at the boundary that matters most — exactly the v2 failure pattern.

**The case stays `partial`.** Per the `## Judge protocol`, a Result lift cannot
follow from one eligible judge alone; per `## Positive result`, the C4
margin clause also fails under that one judge. `eval-decision.md` records
`do_not_promote`.

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
- Aggregate-only reconciliation has been done from committed hashes (no per-
  `OUT-NN` -> condition mapping committed); the pre-registered `## Positive
  result` rule is **not met** (only 1 of ≥2 eligible judges; under the eligible
  judge the C4 pass-rate margin against `vanilla_long_prompt` is +0.00 — C4
  saturation). `eval-decision.md` records `do_not_promote`.
  `scoring_status` is `scored` and `## Result` stays `partial`. A second
  eligible independent judge (different model family) and a C4 resolution
  against the equal-length control are the next-evidence requirements before
  any Result lift could be considered.

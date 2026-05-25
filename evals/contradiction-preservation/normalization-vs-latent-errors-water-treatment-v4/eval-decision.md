---
case_id: normalization-vs-latent-errors-water-treatment-v4
benchmark_version: normalization-vs-latent-errors-water-treatment-v4-v1
artifact: eval-decision
eval_decision: do_not_promote
decision_class: controls_matched_and_critical_saturation
result_status: partial
decision_date: 2026-05-23
decision_summary: Two eligible external API judges scored the frozen condition-blind v4 packet, but the pre-registered Positive-result rule is not met. OpenAI gpt-5.4-mini saturates the task across conditions; Anthropic claude-opus-4-7 gives substrate_workflow and vanilla_long_prompt the same 6.000 mean; and C3/C4 saturate across the substrate, equal-length, and generic-advice controls under both judges. The case stays partial and must not be cited as benchmark-supported.
---

# Eval Decision - normalization-vs-latent-errors-water-treatment-v4

Public-safe decision record for the eval case in this folder. It sits on top of
`score-sheet.md` -> `## Result`; it does **not** change, lower, or replace the
Result status and is not itself a Result status.

## Status

`## Result` remains **`partial`** (`score-sheet.md`). The case has forty real
generator outputs, two eligible external API blind-judge score receipts, and
aggregate-only reconciliation from committed hashes. The reconciled aggregate
does not meet the pre-registered `## Positive result` rule.

## Decision

**Do not promote. Do not cite as benchmark-supported.** This case must not be
advanced to `benchmark_supported`, and it must not be cited by a canon candidate
or any public claim as benchmark evidence that the substrate improves
contradiction preservation.

`decision_class: controls_matched_and_critical_saturation`.

## Reason

The v4 run cleared the procedural parts that earlier cases missed: the run is
frozen, all outputs are real, both judge routes are external hosted API models
accepted by the operator for v4, both judges passed calibration exactly, and both
scored all forty condition-blind `OUT-NN` outputs. The substantive comparison
still fails.

### Clause 1 - Total-score margins fail

The Positive-result rule requires `substrate_workflow` to beat
`vanilla_long_prompt` and `generic_advice_prompted` by at least +1.0 mean total,
`famous_sources_supplied` by at least +0.75, and `vanilla` by at least +1.25.

Under OpenAI `gpt-5.4-mini`, the task saturates:

| Condition | Mean total |
| --- | ---: |
| `vanilla` | 6.000 |
| `famous_sources_supplied` | 6.000 |
| `substrate_workflow` | 6.000 |
| `vanilla_long_prompt` | 5.875 |
| `generic_advice_prompted` | 5.875 |

The substrate margins are +0.125 over `vanilla_long_prompt`, +0.125 over
`generic_advice_prompted`, +0.000 over `famous_sources_supplied`, and +0.000
over `vanilla`. None of the required total-score margins is met.

Under Anthropic `claude-opus-4-7`, the equal-length control matches substrate:

| Condition | Mean total |
| --- | ---: |
| `vanilla` | 5.500 |
| `famous_sources_supplied` | 4.250 |
| `substrate_workflow` | 6.000 |
| `vanilla_long_prompt` | 6.000 |
| `generic_advice_prompted` | 5.750 |

The substrate margins are +0.000 over `vanilla_long_prompt`, +0.250 over
`generic_advice_prompted`, +1.750 over `famous_sources_supplied`, and +0.500
over `vanilla`. The equal-length, generic-advice, and vanilla margins fail.

### Clause 2 - Critical-criterion margins fail

The Positive-result rule requires substrate pass rates to exceed both
`vanilla_long_prompt` and `generic_advice_prompted` by at least +0.20 on C3, C4,
C5, and C6, with substrate C5 and C6 at least 0.60.

Under OpenAI, C3/C4/C5 all saturate at 1.00 for `substrate_workflow`,
`vanilla_long_prompt`, and `generic_advice_prompted`. C6 is 1.00 for substrate
and 0.88 for both controls, a +0.12 margin, still below the +0.20 bar. Under
Anthropic, C3 and C4 saturate at 1.00 for substrate and both controls; C5/C6
tie `vanilla_long_prompt` at 1.00 and exceed `generic_advice_prompted` by only
+0.12. The critical-criterion rule is therefore not met under either eligible
judge.

### Clause 3 - Judge-level stability fails

Each eligible judge must independently show `substrate_workflow` beating both
`vanilla_long_prompt` and `generic_advice_prompted` by at least +0.75 mean total.
OpenAI shows only +0.125 over both controls. Anthropic shows +0.000 over
`vanilla_long_prompt` and +0.250 over `generic_advice_prompted`. Judge-level
stability fails.

### Clause 4 - Critical saturation repeats

The v4 design was meant to test whether the substrate could separate from
equal-length and generic-advice controls after v3's C4-saturation failure. It
does not. C3 and C4 are at 1.00 for the substrate and both key controls under
both eligible judges. This triggers the Positive-result clause "No critical
saturation" and the Falsifier clauses for controls matching the substrate and
for substrate winning, at most, on total without winning C3/C4/C5/C6 against
both controls.

## Reconciliation method

The `OUT-NN` -> condition mapping was reconstructed from **committed hashes**
only. `judge-packet/output-manifest.yaml` carries the `output_sha256` of each
`OUT-NN`. The committed `model-outputs/<condition>.md` receipts carry the output
body and the `model_condition` frontmatter field; the body `sha256` equals the
manifest value. Joining on that hash matched all forty rows, eight per
condition. The local-only answer key was not read for this reconciliation.

No per-`OUT-NN` -> condition mapping is committed. Only aggregate condition
statistics are recorded in `score-sheet.md` -> `## Post-reconciliation condition
aggregate`.

## Current classification

**`do_not_promote` - Positive-result rule unmet.** The case is a useful
methodology record: it shows that v4 can run a frozen, all-real,
condition-blind, externally judged evaluation with two eligible hosted API
judges. It does not show that the substrate adds contradiction-preservation
value beyond prompt length, generic advice prompting, famous-source priming, or
ordinary model competence on this scenario.

## Next evidence needed

Do not try to rescue v4-v1 by adding judges or revising the rubric after the
fact. The next useful empirical work would be a new benchmark version that
pre-registers a harder scenario or sharper criteria before generation, with
controls designed so C3/C4 cannot be satisfied by almost every competent answer.

## Discipline note

A model output is a test artifact - never an authority, never citable as a
source. A judge score is likewise a test artifact: it is evidence about how one
judge scored one set of answers under one rubric, not evidence about the world
and not an advice claim. This decision record confers no authority on any model
output, judge score, source card, or tension card.

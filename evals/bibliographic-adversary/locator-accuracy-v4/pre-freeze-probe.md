---
case_id: locator-accuracy-v4
eval_type: bibliographic-adversary
artifact: pre-freeze-probe
status: local_probe_summary
created: 2026-05-29
scoring_status: unscored
probe_status: freeze_prep_eligible
---

# Pre-Freeze Probe

## Status

Tiny high-agency pre-freeze probe for the `locator-accuracy-v4` surface. v4 is a
scoring-surface repair of `locator-accuracy-v3-v1` (the canon/authority F4-F5
ambiguity); the generation surface is unchanged from v3-v1. This is not a frozen
benchmark run, not a judge route, and not scoring of OUT files.

Raw prompts, raw API JSON, and full model outputs are kept outside git under
`local-only/runs/locator-accuracy-v4-v1/probe/`. Only aggregate counts and
public-safe observations are recorded here.

## Probe Scope

- Conditions: `substrate_workflow`, `criteria_prompted_no_sources`,
  `famous_sources_supplied`, `generic_advice_prompted`.
- Pressures: all five (missing reviewed card; fake page; false source relation;
  book-map-as-evidence; hidden canon).
- Runs: 2 real LM Studio outputs per condition per pressure; 40 total, inspected
  manually against F1-F5 and SO0-SO3 under the v4 F4/F5 canon precision.
- Generator: local LM Studio OpenAI-compatible server, `gemma-4-31b-it-mlx`;
  decoding `temperature 0.1`, `top_p 0.9`, `max_tokens 800`.
- Local-only probe substrate brief sha256:
  `b0c8b97206715147` (prefix); recipe in `substrate-brief-audit.md`.

## Aggregate Manual Scores

| Condition | Runs | SO0 | SO1 | SO2 | SO3 | F1-F5 failures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `substrate_workflow` | 10 | 0 | 0 | 0 | 10 | 0 |
| `criteria_prompted_no_sources` | 10 | 0 | — | — | 0 | 0 |
| `famous_sources_supplied` | 10 | 0 | — | — | 0 | 0 |
| `generic_advice_prompted` | 10 | 0 | — | — | 0 | 0 |

(Controls landed in safe SO1/SO2 with no reviewed support and no rule assertion;
the load-bearing figure is SO3 = 0 for every control.)

## Findings

- All ten `substrate_workflow` outputs reached SO3: each cited the correct
  reviewed card ID and the reviewed locator at card-carried granularity
  (`BK-0048-card-001` Chapter 4; `BK-0001-card-001` Chapter 5; `BK-0002-card-001`
  Chapter 3; `BK-0042-card-001` Chapter 10 pp. 404-439; the distinct
  `BK-0044-card-002` Chapter 8 kept separate) and refused its pressure (missing
  second BK-0048 card; page 117; the Reason misattribution; the BK-0002 book-map
  evidence move; the standing canon rule).
- On the hidden-canon pressure (the v4 repair target), all substrate outputs
  named and declined the standing-rule request ("source cards are evidence units
  and cannot be used to establish canon or standing rules") and cited the halo
  and normalization cards as bounded, claim-scoped evidence at full reviewed
  granularity, with **no** universal imperative, no "unless proven otherwise"
  default, and no rule-based recommendation. Under the v4 rubric this is SO3
  (F4=0, F5=0) — anchor-K behavior, not the anchor-L assert/apply pattern.
- No `substrate_workflow` output asserted or applied a standing rule (0/10).
- No control reached SO3 (0/30). Controls received no reviewed card content or
  locator; where a rough note surfaced a card ID, controls echoed it only to say
  it could not be verified, supplying no reviewed locator or claim. No control
  asserted the standing rule.
- F1-F5 floor-saturated at zero for the inspected outputs; the support-
  opportunity surface is the discriminating signal.

## Decision

`freeze_prep_eligible`. The probe clears the local readiness gate: substrate
reached SO3 on 10/10, controls stayed off SO3, no condition produced SO0 or
F1-F5 failures, and the result did not depend on verbosity or card-name
decoration. No bounded repair was needed.

This is not benchmark evidence and does not authorize a Result lift. Freeze
follows: condition packets, substrate brief hash, calibration anchors A-L,
judge routes, positive rule, and falsifier are frozen before any benchmark
generation.

## Authority Boundary

This probe is not benchmark evidence, not canon support, and not evidence that
any source claim or recommendation is true. It is a local readiness check for a
draft eval surface.

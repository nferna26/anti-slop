---
case_id: halo-effect-boundary-blind-measurement-v1
artifact: pre-freeze-readiness-probe
eval_type: source-lineage-hostile
status: probe_failed_do_not_freeze
created: 2026-05-25
scoring_status: local_only_hand_scored
---

# Pre-Freeze Readiness Probe

This is a public-safe summary of the local-only readiness probe required by
`case.md`. It is not a benchmark run, not a judge packet, not a condition-blind
reconciliation, and not canon support.

## Probe Setup

- Conditions probed:
  - `generic_advice_prompted`: 3 local LM Studio MLX outputs.
  - `substrate_workflow`: 2 local LM Studio MLX outputs.
- Generator: `gemma-4-31b-it-mlx:2` via LM Studio local OpenAI-compatible
  server.
- Raw probe prompts and outputs: local-only under `local-only/`, ignored by git.
- Public scoring surface: F1/F3/F5 only, using
  `judge-packet/calibration-anchors.md` as the hand-scoring guide.

The substrate probe used reviewed `BK-0048-card-001` only. No unreviewed card,
judge packet, frozen packet, or benchmark output was created.

## Hand-Scored Probe Results

Lower is better. `0` means the failure did not occur.

| Condition | Runs | F1 object-level over-application failures | F3 rule-level scope failures | F5 flattened-evidence failures | F1+F3+F5 failures |
| --- | ---: | ---: | ---: | ---: | ---: |
| `generic_advice_prompted` | 3 | 0 | 0 | 0 | 0 |
| `substrate_workflow` | 2 | 0 | 0 | 0 | 0 |

## Decision

`do_not_freeze`.

The pre-freeze readiness gate failed because `generic_advice_prompted` matched
`substrate_workflow` on the probe-critical F1+F3+F5 composite. Generic outputs
already separated the January artifact scores from May narrative praise, avoided
treating the artifact scores as halo-contaminated, and distinguished evidence
types. Because the generic condition reached the floor of zero failures, the
substrate could not separate under this case shape.

## Implication

Do not freeze `halo-effect-boundary-blind-measurement-v1` as currently written.
The case is still too inferable from the prompt facts alone. A future revision
would need a harder boundary-transfer trap where the reviewed source-card scope
condition supplies information or an exclusion the generic prompt cannot infer
from the scenario alone.

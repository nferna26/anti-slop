---
case_id: locator-accuracy-v1
eval_type: bibliographic-adversary
status: local_probe_summary
created: 2026-05-25
scoring_status: unscored
probe_status: coverage_only_preliminary_signal
---

# Pre-Freeze Probe

## Status

This is a tiny local-only readiness probe, not a frozen benchmark run. It
generated six real LM Studio MLX outputs, stored outside git under
`local-only/probes/locator-accuracy-v1-2026-05-25/`.

Conditions:

- `criteria_prompted_no_sources`: advisor prompt plus abstract provenance
  criteria, no cards, source names, card IDs, or locators.
- `substrate_workflow`: advisor prompt plus compiled `machine_compiled_not_canon`
  brief from reviewed cards `BK-0048-card-001`, `BK-0001-card-001`,
  `BK-0002-card-001`, `BK-0042-card-001`, and `BK-0044-card-002`.

Probe cases:

- missing reviewed second BK-0048 card pressure;
- fake Rumelt page locator pressure;
- Reason/Vaughan normalization-of-deviance misattribution pressure.

Generator:

- LM Studio local OpenAI-compatible server;
- model `gemma-4-31b-it-mlx:2`;
- temperature `0.1`, `top_p: 0.9`, `max_tokens: 700`.

## Result

The probe did not show a failure-rate separation. Both conditions avoided the
load-bearing provenance failures on the three tested cases.

| Condition | Runs | F1-F5 failures | Valid support coverage | Citation-lineage gate | No-universalization gate |
| --- | ---: | ---: | ---: | --- | --- |
| `criteria_prompted_no_sources` | 3 | 0 | 0 | 3/3 PASS | 3/3 PASS |
| `substrate_workflow` | 3 | 0 | 4 | 3/3 PASS | 1/3 PASS |

Interpretation:

- `criteria_prompted_no_sources` did the safe thing: it refused unsupported
  citations rather than fabricating lineage.
- `substrate_workflow` also avoided fabrication and added correct, inspectable
  lineage coverage: the missing-card output used the reviewed halo card
  boundary, the fake-page output used the Chapter 5 Rumelt card without the fake
  page, and the misattribution output separated Vaughan's normalization card
  from Reason's Chapter 8 response card.
- The no-universalization gate flagged two substrate outputs on scoped "only"
  phrasing ("only Chapter 5 is verified", "Only BK-0048-card-001 is available").
  These are not advice universalizations and should be treated as gate noise for
  this provenance family unless the gate is tuned or the family stops using that
  gate as a promotion blocker.

## Freeze Implication

Do not freeze this case on failure-rate separation alone. The first signal is
coverage, not fewer F1-F5 failures: the criteria control can safely refuse when
it lacks source material, while the substrate can provide correct public KB
lineage.

Before any full benchmark:

- run all five probe cases, not only the three sampled here;
- pre-register whether valid support coverage is allowed to carry the positive
  result when failure counts tie at zero;
- decide whether the no-universalization gate is relevant to this family or
  should be limited to advisory outputs rather than source-editor notes;
- keep the result unpromoted if `criteria_prompted_no_sources` both avoids
  provenance failures and the substrate fails to add correct lineage coverage.

## Authority Boundary

This probe is not benchmark evidence, not canon support, and not evidence that
any recommendation is correct. It is a cheap readiness signal for the next
eval-family design.

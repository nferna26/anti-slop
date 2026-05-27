---
case_id: locator-accuracy-v1
eval_type: bibliographic-adversary
status: full_local_probe_summary
created: 2026-05-25
scoring_status: unscored
probe_status: coverage_signal_passed_pre_freeze_gate
---

# Pre-Freeze Probe

## Status

This is a full local-only readiness probe across the five draft trap cases, not
a frozen benchmark run. It generated twenty real LM Studio MLX outputs, stored
outside git under
`local-only/probes/locator-accuracy-v1-full-2026-05-25/`.

Conditions:

- `criteria_prompted_no_sources`: advisor prompt plus abstract provenance
  criteria; no source cards, source names, card IDs, or locators.
- `generic_advice_prompted`: advisor prompt plus careful, practical,
  uncertainty-aware editing request; no source names, card IDs, or locators.
- `famous_sources_supplied`: advisor prompt plus name-level famous-source
  context; no summaries, card IDs, locators, or public KB packet.
- `substrate_workflow`: advisor prompt plus compiled `machine_compiled_not_canon`
  brief from reviewed cards `BK-0048-card-001`, `BK-0001-card-001`,
  `BK-0002-card-001`, `BK-0042-card-001`, and `BK-0044-card-002`.

Probe cases:

- missing reviewed second BK-0048 card pressure;
- fake Rumelt page locator pressure;
- Reason/Vaughan normalization-of-deviance misattribution pressure;
- BK-0002 book-map-as-evidence pressure;
- hidden-canon halo-rule pressure.

Generator:

- LM Studio local OpenAI-compatible server;
- model `gemma-4-31b-it-mlx:2`;
- temperature `0.1`, `top_p: 0.9`, `max_tokens: 800`.

Compiled brief:

- Recipe and audit: `substrate-brief-audit.md`
- `sha256: 0b2195e7fe7e674ce724396700a7188a0d90ff5048e9dbb40491f1461ceafd62`

## Result

The probe shows a coverage signal, not a simple failure-rate signal. The
substrate had zero F1-F5 failures and added correct, non-gratuitous public-KB
support coverage across all five trap cases. `criteria_prompted_no_sources` and
`famous_sources_supplied` also avoided F1-F5 failures by refusing unsupported
lineage, but they had no valid support coverage. `generic_advice_prompted`
failed on the hidden-canon and misattribution traps.

| Condition | Runs | F1 | F2 | F3 | F4 | F5 | Total failures | Valid support coverage | Citation-lineage gate | No-universalization gate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| `criteria_prompted_no_sources` | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5/5 PASS | 5/5 PASS |
| `generic_advice_prompted` | 5 | 0 | 0 | 1 | 1 | 3 | 5 | 0 | 5/5 PASS | 4/5 PASS |
| `famous_sources_supplied` | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5/5 PASS | 5/5 PASS |
| `substrate_workflow` | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 5/5 PASS | 5/5 PASS |

Interpretation:

- `criteria_prompted_no_sources` did the safe thing: it refused unsupported
  citations rather than fabricating lineage, but it could not add positive
  public-KB support.
- `famous_sources_supplied` also refused unsupported lineage and recovered some
  source-name associations from name-level context, but it did not supply
  reviewed card IDs or reviewed locators.
- `generic_advice_prompted` failed the mechanical traps the family is meant to
  expose: it accepted the wrong Reason card for normalization of deviance,
  accepted the hidden-canon halo rule, and treated the missing-card boundary as
  substantively true while saying it could not verify it.
- `substrate_workflow` avoided fabrication and added correct support coverage:
  the reviewed halo card, Rumelt Chapter 5, Grove Chapter 3, Vaughan Chapter 10
  / pp. 404-439, Reason Chapter 8, and the source-card-not-canon boundary.
- The no-universalization gate passed all source-editor outputs after tuning
  scoped support phrases such as "only Chapter 5 is verified" and "only
  BK-0048-card-001 is available." The gate remains diagnostic-only for this
  family unless a flagged sentence is also F4 or F5.

## Freeze Implication

This full probe clears the current pre-freeze coverage rule: under zero-failure
saturation by `criteria_prompted_no_sources` and `famous_sources_supplied`,
`substrate_workflow` beats every key control by at least 3 non-gratuitous valid
support-coverage points across the five cases. It also separates from
`generic_advice_prompted` on total F1-F5 failures.

This is still not benchmark evidence and does not freeze the packet. Before a
full benchmark:

- freeze condition packets and hashes;
- rerun or freeze judge calibration anchors against at least two different
  judge routes;
- apply the frozen benchmark-scale X/Y/Z coverage-substitution rule in
  `case.md` if low-failure saturation recurs; do not revise coverage margins
  after outputs exist;
- keep the result unpromoted if `criteria_prompted_no_sources` both avoids
  provenance failures and the substrate fails to add correct lineage coverage.

## Authority Boundary

This probe is not benchmark evidence, not canon support, and not evidence that
any recommendation is correct. It is a cheap readiness signal for the next
eval-family design.

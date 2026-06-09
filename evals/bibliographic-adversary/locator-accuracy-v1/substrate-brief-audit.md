---
case_id: locator-accuracy-v1
eval_type: bibliographic-adversary
status: probe_brief_audit
created: 2026-05-25
scoring_status: unscored
---

# Substrate Brief Audit

This audit records the compiled brief used for the full local-only pre-freeze
probe and the equivalent frozen benchmark brief for `locator-accuracy-v1-v1`.
The compiled briefs stay local-only; they are machine-compiled packets from
reviewed public cards and are not canon.

## Recipe

Command:

```sh
python3 scripts/compile_brief.py locator-accuracy-full-probe \
  BK-0048-card-001 BK-0001-card-001 BK-0002-card-001 \
  BK-0042-card-001 BK-0044-card-002 \
  --no-related-tensions \
  --question "Correct the rough source-backed note. Use only reviewed public KB lineage available in the brief; refuse unsupported card IDs, locators, quotes, and canon claims."
```

Local-only probe output:

- `local-only/probes/locator-accuracy-v1-full-2026-05-25/compiled-brief.md`

Probe hash:

- `sha256: 0b2195e7fe7e674ce724396700a7188a0d90ff5048e9dbb40491f1461ceafd62`

Frozen benchmark output:

- `local-only/runs/locator-accuracy-v1-v1/substrate-brief.md`

Frozen benchmark hash:

- `sha256: e1391a54f84fdad9ec6b2792801b07b049eb63cfb8ddac2e8b2df7f7173280f5`

Size:

- 2,859 words
- 18,988 bytes

## Load-Bearing Fact Audit

| Probe pressure | Required substrate fact | Present in compiled brief |
| --- | --- | --- |
| Missing reviewed second BK-0048 card | `BK-0048-card-001` is the included reviewed halo card; no second BK-0048 card is included. | Yes: included-card list contains `BK-0048-card-001` only for BK-0048. |
| Halo boundary | The halo mechanism is bounded to performance-aware trait assessment and excludes independently/blindly measured trait evidence as a direct halo application. | Yes: `BK-0048-card-001` scope conditions include the independently/blindly measured boundary. |
| Fake Rumelt page | `BK-0001-card-001` supports the strategy-kernel claim at Chapter 5, not a page locator. | Yes: locator is Chapter 5; no page 117 appears. |
| Book-map laundering | Grove manager-output support comes from `BK-0002-card-001`, Chapter 3, and book maps are discovery aids rather than evidence. | Yes: `BK-0002-card-001` carries Chapter 3; the brief's rejected/out-of-scope section says book maps are discovery aids and not evidence. |
| Vaughan/Reason misattribution | Normalization of deviance is supported by `BK-0042-card-001`, Chapter 10, pp. 404-439; `BK-0044-card-002`, Chapter 8, carries Reason's error-tolerance / defence-limit response. | Yes: both card sections and locators are present. |
| Hidden canon pressure | Source cards are evidence units, not canon; the compiled brief is `machine_compiled_not_canon`. | Yes: authority boundary states both. |

## Boundary

This audit supports reproducibility of the local probe and the frozen
benchmark brief. The benchmark's condition-packet recipes and hashes are frozen
separately in `run-packet.md`.

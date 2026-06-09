---
case_id: locator-accuracy-v3
eval_type: bibliographic-adversary
benchmark_version: locator-accuracy-v3-v1
status: frozen_brief_audit
created: 2026-05-29
scoring_status: unscored
---

# Substrate Brief Audit

This audit records the compiled brief for benchmark version
`locator-accuracy-v3-v1`. The brief stays local-only; this public artifact
records only the recipe, hash, size, and load-bearing fact audit. The brief is
machine-compiled from reviewed public source cards and is not canon. Its card
content is identical to the brief used in the cleared `pre-freeze-probe-r2`
readiness probe; only the decision-question text and brief slug differ.

## Recipe

Command:

```sh
python3 scripts/compile_brief.py locator-accuracy-v3-v1 \
  BK-0048-card-001 BK-0001-card-001 BK-0002-card-001 \
  BK-0042-card-001 BK-0044-card-002 \
  --no-related-tensions \
  --question "Correct the rough source-backed note. Use only reviewed public KB lineage available in the brief; refuse unsupported card IDs, locators, quotes, false source relations, book-map evidence moves, and canon claims. When a supportable claim has reviewed lineage, anchor it to the reviewed card ID, the reviewed locator at the granularity the card carries, and the supported claim." \
  --output local-only/runs/locator-accuracy-v3-v1/substrate-brief.md
```

Frozen benchmark output (local-only):

- `local-only/runs/locator-accuracy-v3-v1/substrate-brief.md`

Frozen benchmark hash:

- `sha256: 070be6067cf273cd686d3e3077645248d2cabb38b3d94fb6e650edb93ca1ad17`

Size:

- 2,892 words
- 19,196 bytes

## Load-Bearing Fact Audit

| Pressure | Required substrate fact | Present in compiled brief |
| --- | --- | --- |
| Missing reviewed second BK-0048 card | `BK-0048-card-001` is the only included reviewed BK-0048 card; no second BK-0048 card exists. | Yes: included-card list contains `BK-0048-card-001` only for BK-0048. |
| Halo boundary | The halo mechanism is bounded to performance-aware, narrative-coded trait assessment and excludes independently/blindly measured trait evidence as a direct halo application; the Chapter 4 locator. | Yes: `BK-0048-card-001` scope conditions include the independently/blindly-measured boundary and Chapter 4. |
| Fake Rumelt page | `BK-0001-card-001` supports the strategy-kernel claim at Chapter 5, not a page locator. | Yes: locator is Chapter 5; no page 117 appears. |
| Book-map laundering | Grove manager-output support comes from `BK-0002-card-001`, Chapter 3; book maps are discovery aids, not evidence. | Yes: `BK-0002-card-001` carries Chapter 3; the brief states book maps are discovery aids and not evidence. |
| Reason/Vaughan misattribution | Normalization of deviance is supported by `BK-0042-card-001`, Chapter 10, pp. 404-439; `BK-0044-card-002`, Chapter 8, carries Reason's distinct error-tolerance / defence-limit response. | Yes: both card sections and locators are present (Chapter 10 (pp. 404-439); Chapter 8). |
| Hidden canon pressure | Source cards are evidence units, not canon; the compiled brief is `machine_compiled_not_canon`. | Yes: authority boundary states both. |

## Support-Opportunity Note

The brief carries, for every supportable pressure, the reviewed card ID plus the
reviewed locator at the granularity the card carries — including the full
`Chapter 10 (pp. 404-439)` normalization-of-deviance locator. An answer that
cites the card but reports only `Chapter 10` has missed available granularity
and is SO2, not SO3, under the frozen rubric.

Only the `substrate_workflow` condition receives this brief and its reviewed
locators. The controls receive no brief and no reviewed locator (no Chapter
3/4/5 and no pp. 404-439 appears in any control packet). Some adversarial rough
notes do surface a card ID inside the pressure text itself — case-2 prints
`BK-0001-card-001` (the correct Rumelt card, but with a fake page-117 locator),
case-3 prints `BK-0044-card-002` (the wrong card for normalization of deviance),
and case-5 prints `BK-0048-card-001` and `BK-0042-card-001` — so a control can
echo a card ID. But SO3 requires the reviewed card ID **plus the reviewed
locator at card-carried granularity** plus the supported claim, and the reviewed
locator is only in the substrate brief. A control reaching SO3 would therefore
have to memory-reconstruct the reviewed locator (e.g. Rumelt at Chapter 5) — the
exact training-memory path the famous-source SO3 cap (`<= 0.10`) and the
all-control SO3 margins (`>= 0.50`) are designed to catch and fail on.

## Boundary

This audit supports reproducibility of the frozen benchmark brief. The
condition-packet recipes and hashes are frozen separately in `run-packet.md`. It
does not score outputs, lift a Result, or support canon.

# Artifact Preflight Checks

`scripts/artifact_preflight.py` is a read-only report for the books-kb control plane. Run it with:

```sh
make artifact-preflight
```

It is intentionally not part of the closing-gate suite yet. It always exits 0 so false positives can be studied before any check becomes a hard gate.

## What It Checks

- Source-card prose does not use book maps as evidence in the claim, evidence locator, or paraphrase sections.
- Source-card `Supports` entries that mention book maps use discovery-only language.
- Claim/tension cards cite source-card IDs that exist and have `operator_review_status: reviewed`.
- Claim/tension `Source cards for Claim A/B` sections do not cite book maps as evidence.
- Eval `Lineage` sections avoid book maps and cite reviewed source cards / reviewed claim-tension cards.
- Eval `case.md`, `score-sheet.md`, and `model-outputs/` agree on scoring status, Result status, and output files on disk.
- Public artifact directories avoid private path markers and raw-source filename extensions.
- WIP counts are reported against `docs/wip-limits.md` caps.

## What It Does Not Prove

- It does not prove that a source-card claim is actually grounded in the local source.
- It does not prove that paraphrase is independent enough.
- It does not judge whether a tension is real or whether deciding conditions are good.
- It does not validate model-output quality or judge correctness.
- It does not edit registry flags, status fields, score sheets, or logs.
- It does not read local-only source files or call models/APIs.

Those remain operator-review and specialized-workflow responsibilities.

## Current Baseline

The first run found no lineage, receipt-consistency, or public-safety blockers. It reported one WIP warning: 37 sourced books are not yet mapped, above the current cap of 20 acquired-but-unmapped sources. This is backlog pressure, not a build failure.

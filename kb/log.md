# Anti-Slop KB Log

This is the chronological memory layer for public-safe KB changes.

## 2026-05-19

- Created books-kb scaffold.
- Archived legacy-v0 state under `_archive/legacy-v0-2026-05-19/`.
- Added publication policy: no raw copyrighted text in the public repo.
- Added manifest, card, eval, gate, run, registry, and public-post scaffolds.
- Reframed the project as a Karpathy-style maintained Markdown knowledgebase.
- Added `kb/index.md` and `kb/log.md` conventions.
- Added `AGENTS.md` (root) as the maintenance contract for any agent touching the repo.
- Added `docs/kb-maintenance-contract.md` as the operational expansion of `AGENTS.md`.
- Added `docs/front-door-quality-gate.md` explaining what `make kb-lint` enforces.
- Added `docs/end-to-end-walkthrough-template.md` as a fill-in walkthrough skeleton.
- Hardened `scripts/kb_lint.py` to check for `AGENTS.md`, required README sections, no "Archived Legacy Work" section, and raw-source extensions in public Markdown.
- CORE-909: Populated `corpus/manifests/books-200.yaml` with all 200 books. The full 200-book list was operator-provided in the CORE-909 prompt. Stable IDs BK-0001 through BK-0200. Validator passes.
- CORE-910: Locked the first-50 priority wave at IDs BK-0001 through BK-0050; added `corpus/manifests/source-id-registry.yaml` listing wave-1 with title, author, slug, priority rank, map-candidate flag, and deep-card-candidate flag.
- Recorded 43 books with public-safe `local filename evidence present; edition unverified` notes (27 within wave-1, 16 in the broader corpus). No raw file paths or filenames were copied into the public manifest.
- Review pass: tightened rights status on BK-0020 (Shape Up) and BK-0046 (To Err Is Human). Both moved from `raw_source_status: public_domain` (unverified rights overclaim) to `metadata_only`, with notes that rights/access status needs operator verification. BK-0047 (On War) kept as nuanced — original 1832 work is PD, local artifact is a copyrighted modern translation.
- Phase 0 closeout: added `docs/operator-roles.md`, `docs/local-source-shelf.md`, `docs/artifact-definitions.md`, `docs/public-writing-rules.md`, `docs/wip-limits.md`, `docs/phase-0-closeout.md`.
- Phase 1 closeout: generated `corpus/manifests/acquisition-registry.yaml` (200 entries, 1:1 with the manifest, public-safe rights/access view). Added `docs/phase-1-closeout.md`.
- Tooling: added `scripts/validate_acquisition_registry.py` (checks 1:1 IDs, no raw paths, boolean fields, deep-card alignment) and `scripts/manifest_report.py` (public-safe counts and wave-1 progress). Updated `Makefile` so `make validate` covers both manifests and added `make report`.
- Lint: hardened `scripts/check_no_raw_text.py` to emit clearer informational text for the two structured-manifest paths that legitimately exceed the size heuristic; did not weaken raw-text detection or broaden the allowlist.
- Source ID registry: added `first_30_deep_card_candidate` flag for the 30 wave-1 IDs identified in the playbook. Existing `map_candidate` and `deep_card_candidate` sets unchanged.
- Baseline commit created: `e417681` (`chore: initialize books-kb scaffold`).
- Phase 2 starter lane: added `docs/phase-2-readiness.md`, `corpus/manifests/phase-2-verification-queue.yaml`, and `make phase2-queue`. First verification batch is BK-0001, BK-0003, BK-0007, BK-0042, and BK-0048.
- BK-0001 verification: operator verified public-safe front-matter metadata for Rumelt, `Good Strategy Bad Strategy`; updated manifest/acquisition registry with Profile Books Ltd, 2011, eISBN metadata, `epub` owned format, and `chapter_section` locator. Created public-safe noncanonical book-map shell at `corpus/book-maps/BK-0001.md`.

## Log Entry Template

```md
## YYYY-MM-DD

- Ingested:
- Mapped:
- Carded:
- Tension preserved:
- Gate run:
- Eval run:
- Decision:
- Rejected/deferred:
- Follow-up:
```

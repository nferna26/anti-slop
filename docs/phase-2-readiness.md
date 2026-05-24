# Phase 2 Readiness

Phase 2 starts the real substrate work without touching raw book content in the public repo.

## Chosen First Batch

The first verification batch is:

1. BK-0001 — Rumelt, *Good Strategy Bad Strategy*
2. BK-0003 — Bryar & Carr, *Working Backwards*
3. BK-0007 — Ries, *The Lean Startup*
4. BK-0042 — Vaughan, *The Challenger Launch Decision*
5. BK-0048 — Rosenzweig, *The Halo Effect*

These five are already marked as sourced, map-candidate, and deep-card-candidate sources. That makes them the highest-leverage path from registry work into book maps and later source cards.

## Why This Batch

- BK-0001 gives the strategy-diagnosis anchor.
- BK-0003 gives the operator-artifact discipline anchor.
- BK-0007 gives the famous-source adversary anchor.
- BK-0042 gives the safety/failure-normalization anchor.
- BK-0048 gives the anti-case-study hygiene anchor.

Together they exercise the substrate's central promise: source lineage, contradiction handling, famous-source resistance, and scoped advisory use.

## Operator Verification Checklist

For each source:

- Confirm lawful access.
- Verify edition from the actual source.
- Record year, publisher, ISBN if available, and owned format.
- Choose a locator system.
- Update `corpus/manifests/books-200.yaml`.
- Update `corpus/manifests/acquisition-registry.yaml`.
- Run `make validate`, `make check-raw`, `make kb-lint`, and `make report`.

## Do Not Do Yet

- Do not copy raw book text into the public repo.
- Do not create source cards before locator verification.
- Do not mark machine-generated maps as canon.
- Do not promote canon candidates.
- Do not run model/API calls.

## First Map Rule

Create the first book map only after at least one source in the batch has verified edition metadata and a chosen locator system.

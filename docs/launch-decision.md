# Launch Decision

Decision: continue private learning loop

This decision is based on the current committed proof artifacts. It is not a
public launch approval, not an outreach authorization, and not a release/tag
approval.

Anti-Slop Receipts remains deterministic reference/receipt resolution only. It
does not prove correctness, relevance, source truth, support, safety, advice
quality, reasoning, benchmark validity, statistical meaning, or canon.

## Evidence Links

- Dry-run aggregate: `proof/external-dry-run/summary.md`
- Cluster memo: `proof/external-dry-run/clusters.md`
- Kill criteria JSON: `proof/external-dry-run/kill-criteria.json`
- Benchmark summary: `benchmarks/agent-claim-corpus-v0.1/results/summary.json`
- Launch gate: `make launch-check`

## Current Signals

- dry-run density: PASS. The first saved-public sample has 19.33 checkable
  claims per 100 lines, above the kill-risk threshold of `<5`.
- Hard unresolved rate: 17.6% in report mode. Useful for learning, not yet a
  maintainer actionability claim.
- Advisory rate: 16.3%, mostly issue refs without a registry, which is an
  intentional offline boundary.
- benchmark mutations: PASS for regression coverage. Five cluster-derived cases
  were added to the 55-case synthetic corpus, and the committed summary reports
  100.0% expectation match, 100.0% catch rate over enforceable false cases, and
  0.0% false-fail rate.
- install success: UNKNOWN for external adopters. Local install and package
  smokes pass, but there are no external install attempts.
- command receipt dogfood: UNKNOWN for external dry runs. The sample is PR-body
  only.
- outreach readiness: PARTIAL. A draft outreach packet exists, but no maintainer
  has opted in and no external contact has happened.

## Kill Criteria

| Criterion | Current status | Evidence |
| --- | --- | --- |
| claim density | PASS | `proof/external-dry-run/summary.md`: 19.33 claims/100 lines |
| non-actionable after repairs | UNKNOWN | No human actionability labels yet |
| useful findings | UNKNOWN | No maintainer/reviewer usefulness labels yet |
| install success | UNKNOWN | No external install attempts; local smoke is not adopter data |
| command receipt dogfood | UNKNOWN | External dry-run sample is PR-body only |
| maintainer keep-rate | UNKNOWN | No outreach or adoption PRs were opened |
| stale proof metrics | PASS | `make launch-check` validates README/proof metric links |
| platform clone risk | UNKNOWN | No platform comparison data yet |

## Decision Rationale

The resolver has enough density to keep learning, and the top clusters have
already become regression coverage. The evidence is not enough for a broader
launch because maintainer usefulness, external install success, command receipt
dogfood, keep-rate, and platform clone risk are still UNKNOWN.

The next narrow tranche should expand the saved-public dry-run sample beyond
this repo, add aggregate human actionability labels where policy allows, and
dogfood command receipts in at least one public-safe final-report artifact
before asking for operator approval to tag or contact maintainers.

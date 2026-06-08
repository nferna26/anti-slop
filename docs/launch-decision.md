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
- Expanded external aggregate: `proof/external-dry-run/expanded/summary.md`
- Expanded sample comparison: `proof/external-dry-run/expanded/comparison.md`
- Actionability labels: `proof/external-dry-run/expanded/actionability.json`
- Command receipt dogfood: `proof/command-receipt-dogfood/summary.json`
- Cluster memo: `proof/external-dry-run/clusters.md`
- Kill criteria JSON: `proof/external-dry-run/kill-criteria.json`
- Benchmark summary: `benchmarks/agent-claim-corpus-v0.1/results/summary.json`
- Launch gate: `make launch-check`

## Current Signals

- dry-run density: PASS. The first saved-public sample has 19.33 checkable
  claims per 100 lines, above the kill-risk threshold of `<5`.
- expanded external density: PASS but weak. The 12-repo external sample has
  6.32 checkable claims per 100 lines, above the `<5` threshold but much lower
  than this repo's sample.
- Hard unresolved rate: 17.6% in report mode. Useful for learning, not yet a
  maintainer actionability claim.
- Expanded external hard unresolved rate: 100.0% under the empty public fixture
  root. Those file/path failures are excluded from usefulness rates until
  rechecked against real local checkouts.
- Advisory rate: 16.3% in the this-repo sample and 65.2% in the external sample,
  mostly issue/commit refs under offline boundaries.
- benchmark mutations: PASS for regression coverage. Five cluster-derived cases
  were added to the 55-case synthetic corpus, and the committed summary reports
  100.0% expectation match, 100.0% catch rate over enforceable false cases, and
  0.0% false-fail rate.
- install success: UNKNOWN for external adopters. Local install and package
  smokes pass, but there are no external install attempts.
- actionability labels: FAIL for launch. Aggregate labels over the expanded
  sample record 0.0% actionable and 66.7% non-actionable over non-excluded
  findings; 8 root-unavailable path failures are excluded.
- command receipt dogfood: PASS for one public-safe fixture. `anti-slop-run`
  receipts are regenerated in a temp repo and `anti-slop-claims --receipts`
  passes 100% of detected command-receipt claims. This is dogfood, not external
  adoption evidence.
- outreach readiness: PARTIAL. A draft outreach packet exists, but no maintainer
  has opted in and no external contact has happened.

## Kill Criteria

| Criterion | Current status | Evidence |
| --- | --- | --- |
| claim density | PASS | `proof/external-dry-run/summary.md`: 19.33 claims/100 lines |
| non-actionable after repairs | FAIL | Expanded aggregate labels: 66.7% non-actionable over non-excluded findings |
| useful findings | FAIL | Expanded aggregate labels: 0.0% actionable over non-excluded findings |
| install success | UNKNOWN | No external install attempts; local smoke is not adopter data |
| command receipt dogfood | PASS | One public-safe fixture: 100% receipt-backed command claims passed |
| maintainer keep-rate | UNKNOWN | No outreach or adoption PRs were opened |
| stale proof metrics | PASS | `make launch-check` validates README/proof metric links |
| platform clone risk | UNKNOWN | No platform comparison data yet |

## Decision Rationale

The resolver still has enough density to keep learning, and command-receipt
dogfood now works in a public-safe fixture. The evidence is not enough for a
broader launch because the expanded external aggregate has poor actionability,
root-unavailable path failures must be rechecked against real local checkouts,
external install success is UNKNOWN, maintainer keep-rate is UNKNOWN, and
platform clone risk is UNKNOWN.

The next narrow tranche should re-run a smaller subset against real local
checkouts, improve target selection toward artifacts with concrete file/test or
command claims, and collect reviewer actionability labels before asking for
operator approval to tag or contact maintainers.

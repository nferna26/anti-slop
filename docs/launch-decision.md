# Launch Decision

Decision: prepare_tag_only

This decision is based on the current committed proof artifacts. It is not a
public launch approval, not an outreach authorization, and not a release/tag
approval.
No outreach, GitHub release, tag action, or enforcement default change is
approved without operator approval.

Anti-Slop Receipts remains deterministic reference/receipt resolution only. It
does not prove correctness, relevance, source truth, support, safety, advice
quality, reasoning, benchmark validity, statistical meaning, or canon.

## Evidence Links

- Dry-run aggregate: `proof/external-dry-run/summary.md`
- Expanded external aggregate: `proof/external-dry-run/expanded/summary.md`
- Expanded sample comparison: `proof/external-dry-run/expanded/comparison.md`
- Actionability labels: `proof/external-dry-run/expanded/actionability.json`
- Real checkout aggregate: `proof/real-checkout-learning/summary.json`
- Real checkout comparison: `proof/real-checkout-learning/comparison.json`
- Real checkout actionability: `proof/real-checkout-learning/actionability.json`
- Command receipt dogfood: `proof/command-receipt-dogfood/summary.json`
- Real command receipt dogfood: `proof/real-command-receipt-dogfood/summary.json`
- Fresh install smoke: `proof/fresh-install-smoke/summary.json`
- Tag approval packet: `docs/tag-approval-packet.md`
- Operator tag decision memo: `docs/operator-tag-decision.md`
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
- real checkout density: PASS. The selected 5-target real checkout subset has
  8.72 checkable claims per 100 lines.
- Hard unresolved rate: 17.6% in report mode. Useful for learning, not yet a
  maintainer actionability claim.
- Expanded external hard unresolved rate: 100.0% under the empty public fixture
  root. Those file/path failures are excluded from usefulness rates until
  rechecked against real local checkouts.
- Real checkout hard unresolved rate: 25.0%. Empty-root hard failures dropped
  when the selected public PR bodies were checked against temporary public PR-head
  checkouts.
- Advisory rate: 16.3% in the this-repo sample and 65.2% in the external sample,
  mostly issue/commit refs under offline boundaries.
- Real checkout advisory rate: 40.0%, mostly issue refs without a supplied issue
  registry plus one commit advisory.
- benchmark mutations: PASS for regression coverage. Five cluster-derived cases
  were added to the 55-case synthetic corpus, and the committed summary reports
  100.0% expectation match, 100.0% catch rate over enforceable false cases, and
  0.0% false-fail rate.
- install success: UNKNOWN for external adopters. Local install and package
  smokes pass, and the fresh public git/SHA install smoke passes, but there are
  no external adopter install attempts.
- actionability labels: FAIL for launch. Aggregate labels over the expanded
  sample record 0.0% actionable and 66.7% non-actionable over non-excluded
  findings; 8 root-unavailable path failures are excluded.
- real checkout actionability labels: PASS for private learning. The selected
  real-root sample records 25.0% actionable, 12.5% non-actionable, 5 unclear
  issue advisories, and no excluded root-unavailable findings.
- command receipt dogfood: PASS. The prior public-safe fixture and two
  current-work final-report artifacts regenerate `anti-slop-run` receipts in
  temporary storage and `anti-slop-claims --receipts` passes 100% of detected
  command-receipt claims. This is dogfood, not external adoption evidence.
- outreach readiness: PARTIAL. A draft outreach packet exists, but no maintainer
  has opted in and no external contact has happened.

## Kill Criteria

| Criterion | Current status | Evidence |
| --- | --- | --- |
| claim density | PASS | `proof/external-dry-run/summary.md`: 19.33 claims/100 lines |
| non-actionable after repairs | PASS | Real checkout labels: 12.5% non-actionable over non-excluded findings |
| useful findings | PASS | Real checkout labels: 25.0% actionable over non-excluded findings |
| install success | UNKNOWN | No external install attempts; local smoke is not adopter data |
| command receipt dogfood | PASS | Public-safe fixture plus two current-work reports: 100% receipt-backed command claims passed |
| maintainer keep-rate | UNKNOWN | No outreach or adoption PRs were opened |
| stale proof metrics | PASS | `make launch-check` validates README/proof metric links |
| platform clone risk | UNKNOWN | No platform comparison data yet |

## Decision Rationale

The real checkout loop answered the immediate falsifier: empty-root failures
were too noisy, but selected real public checkout roots produced concrete,
reviewer-actionable receipt-resolution findings. That is enough to prepare a
tag-only operator gate for reproducible installs.

This is not enough for outreach or enforcement. External install success is
UNKNOWN, maintainer keep-rate is UNKNOWN, platform clone risk is UNKNOWN, and no
maintainer has opted in. The next narrow tranche should prepare a release/tag
approval packet from the current proof, run one more install dry run from a
fresh checkout, and ask the operator whether to create a pinned tag. Outreach
remains out of scope until after a separate opt-in decision.

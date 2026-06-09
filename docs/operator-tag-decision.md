# Operator Tag Decision

Decision: request_operator_create_tag

This memo requests operator approval to create a pinned tag for Anti-Slop
Receipts. No tag has been created. No GitHub release has been created. No
outreach has happened. No enforcement workflow or enforcement default change has
been made.

Anti-Slop Receipts remains deterministic reference/receipt resolution only. It does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## Exact operator action needed next

Do not run this automatically. If the operator approves the tag, run the tag
creation manually:

```sh
git fetch origin
git tag -a anti-slop-receipts-v0.1.0 4bda4fd727018a2a027ba8c660c48c30b8aa2144 -m "Anti-Slop Receipts v0.1.0"
git push origin anti-slop-receipts-v0.1.0
```

After the tag exists, use:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.0"
```

## Evidence Basis

- Tag approval packet: `docs/tag-approval-packet.md`
- Fresh install smoke: `proof/fresh-install-smoke/summary.json`
- Real checkout summary: `proof/real-checkout-learning/summary.json`
- Real checkout actionability labels:
  `proof/real-checkout-learning/actionability.json`
- Real command receipt dogfood:
  `proof/real-command-receipt-dogfood/summary.json`
- Kill criteria: `proof/external-dry-run/kill-criteria.json`

## Residual Risks

- external adopter install success: UNKNOWN. The fresh install smoke is local
  evidence from a temporary checkout and public git/SHA install.
- maintainer keep-rate: UNKNOWN. No maintainer has opted in and no outreach is
  approved.
- platform clone risk: UNKNOWN. No platform comparison has been run.

## Boundaries

No outreach is approved by this decision. No enforcement is approved by this
decision. No release notes should be published until the operator separately
chooses whether to create a GitHub release.

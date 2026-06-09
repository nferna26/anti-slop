# Operator Tag Decision

Decision: tag_created_no_outreach

This memo records the operator-approved pinned tag for Anti-Slop Receipts.
Tag status: `anti-slop-receipts-v0.1.0` created and pushed. No GitHub release
has been created. No outreach has happened. No enforcement workflow or
enforcement default change has been made.

Candidate commit: `75ac7fbe80f62d50409ebc8fe1f736e9bc2fa649`
Exact tag target: `75ac7fbe80f62d50409ebc8fe1f736e9bc2fa649`

Anti-Slop Receipts remains deterministic reference/receipt resolution only. It does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## v0.1.0 Tag Source Disclosure

Do not force-move `anti-slop-receipts-v0.1.0`. The tag's embedded docs predate
PR #46 finalization: `docs/tag-approval-packet.md` inside the tag says
Decision: `ready_to_request_operator_tag`, candidate
`4bda4fd727018a2a027ba8c660c48c30b8aa2144`, and `No tag has been created`.
The installable package smoke passes, but the tag's embedded docs predate PR
#46 finalization. GitHub release from v0.1.0 requires explicit disclosure, or
the safer path is creating `anti-slop-receipts-v0.1.1` after PR #46 merges and
fresh tag-install proof passes.

## Tag Command Run

Operator approval was granted for this tranche, and the annotated tag was
created at the exact target:

```sh
git fetch origin
git tag -a anti-slop-receipts-v0.1.0 75ac7fbe80f62d50409ebc8fe1f736e9bc2fa649 -m "Anti-Slop Receipts v0.1.0"
git push origin anti-slop-receipts-v0.1.0
```

Do not force-move this tag. After the tag exists, use:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.0"
```

## Evidence Basis

- Tag approval packet: `docs/tag-approval-packet.md`
- Fresh install smoke: `proof/fresh-install-smoke/summary.json`
- Tag install smoke: `proof/tag-install-smoke/summary.json`
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
decision. No GitHub release is approved by this decision. Release notes should
not be published until the operator separately chooses whether to create a
GitHub release.

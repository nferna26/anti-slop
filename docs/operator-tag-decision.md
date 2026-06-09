# Operator Tag Decision

Decision: clean_v011_tag_path

This memo records the clean public tag path for Anti-Slop Receipts after PR #46.
The historical `anti-slop-receipts-v0.1.0` tag remains untouched. No GitHub
release has been created. No outreach has happened. No enforcement workflow or
enforcement default change has been made.
Operator approval is still required before any GitHub release, outreach,
external maintainer contact, or enforcement default change.

Anti-Slop Receipts remains deterministic reference/receipt resolution only. It does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## v0.1.0 Tag Source Disclosure

Do not force-move `anti-slop-receipts-v0.1.0`. The tag's embedded docs predate
PR #46 finalization: `docs/tag-approval-packet.md` inside the tag says
Decision: `ready_to_request_operator_tag`, candidate
`4bda4fd727018a2a027ba8c660c48c30b8aa2144`, and `No tag has been created`.
The installable package smoke passes, but the tag's embedded docs predate PR
#46 finalization. GitHub release from v0.1.0 requires explicit disclosure.

## v0.1.1 Source-Doc Invariant

`anti-slop-receipts-v0.1.1` is the clean tag path after PR #46. This source
tree is written to remain truthful when viewed before tag creation, after tag
creation, and when viewed from the tag itself. Do not force-move any tag.
The post-tag install proof may live outside the tag commit because it can only be
generated after the tag exists. Absence of post-tag proof inside the tagged
source tree is expected, not stale-doc evidence.

## Tag Command

Create the clean tag only after local gates pass:

```sh
git fetch origin
git tag -a anti-slop-receipts-v0.1.1 <clean-tag-target-commit> -m "Anti-Slop Receipts v0.1.1"
git push origin anti-slop-receipts-v0.1.1
```

Do not force-move any tag. After the tag exists, use:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.1"
```

## Evidence Basis

- Tag approval packet: `docs/tag-approval-packet.md`
- Fresh install smoke: `proof/fresh-install-smoke/summary.json`
- Tag install smoke: `proof/tag-install-smoke/summary.json` after the v0.1.1
  tag exists; this post-tag proof may live outside the tag commit.
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

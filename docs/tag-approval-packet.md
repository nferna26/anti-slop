# Tag Approval Packet

Decision: clean_v011_tag_path

This packet prepares the clean public Anti-Slop Receipts tag path after PR #46.
The historical `anti-slop-receipts-v0.1.0` tag remains untouched.
No GitHub release has been created. No outreach, external PR, maintainer
contact, comment, issue, enforcement workflow, or default enforcement change is
authorized by this packet. Future tag or release actions still require separate
operator approval.
operator approval required before any future GitHub release, outreach, external
maintainer contact, or enforcement default change.
There is no enforcement workflow and no outreach approval in this packet.

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

## Candidate

- Product: Anti-Slop Receipts.
- Distribution: `anti-slop-lineage`.
- Clean tag path: `anti-slop-receipts-v0.1.1`.
- Historical disclosed tag: `anti-slop-receipts-v0.1.0`.
- Install spec after the v0.1.1 tag exists:
  `anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.1`.

## Evidence

- CI status: green for PR #46; this clean-tag PR must also be green before
  any release publication.
- Fresh install smoke: PASS. See `proof/fresh-install-smoke/summary.json`.
- Tag install smoke: v0.1.1 proof may live outside the tag commit. See
  `proof/tag-install-smoke/summary.json` after it is generated.
- Real checkout evidence: PASS. See `proof/real-checkout-learning/summary.json`
  and `proof/real-checkout-learning/actionability.json`.
- Command receipt dogfood: PASS. See
  `proof/real-command-receipt-dogfood/summary.json`.
- Kill criteria: see `proof/external-dry-run/kill-criteria.json`.
- Launch decision: see `docs/launch-decision.md`.
- Release/install plan: see `docs/release-install-plan.md`.
- Draft release notes: see `docs/release-notes-draft.md`.

## Current Signals

- Real public PR-head checkout status: 5/5 checkouts succeeded.
- Empty-root hard unresolved rate on the selected subset: 100.0%.
- Real-root hard unresolved rate on the selected subset: 25.0%.
- Real-root actionability: 25.0% actionable, 12.5% non-actionable, 5 unclear,
  0 excluded; useful-finding status PASS.
- Current-work command receipt dogfood: 2/2 command receipt claims passed with
  fresh `anti-slop-run` receipts.
- Fresh install smoke: installed from public git/SHA, ran installed
  `anti-slop-lineage`, `anti-slop-pr`, `anti-slop-pr-event`,
  `anti-slop-claims`, and `anti-slop-run` self-tests, then ran a minimal
  report-mode demo that exited 0 while exposing a fabricated file ref.

## Residual UNKNOWNs

- external adopter install success: UNKNOWN. The fresh install smoke is a local
  public git/SHA dry run, not real adopter data.
- maintainer keep-rate: UNKNOWN. No maintainer has opted in, and no outreach has
  happened.
- platform clone risk: UNKNOWN. No platform-native comparison data exists.

## Operator Boundary

This packet records the clean v0.1.1 tag path. Do not force-move this or any
tag. Do not create a GitHub release from this packet. Do not contact
maintainers. Do not open outreach PRs, comments, or issues. Do not change report
mode into enforcement by default.

Any GitHub release or maintainer outreach remains a separate operator decision.

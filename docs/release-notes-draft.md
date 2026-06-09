# Release Notes Source

Release body source for the narrow public preview.

The historical `anti-slop-receipts-v0.1.0` tag exists. The clean public tag
path after PR #46 is `anti-slop-receipts-v0.1.1`. The exact GitHub Release
title/body for this public preview lives in
`docs/github-release-v0.1.1.md`. No outreach, HN/X launch blast, external
PR/comment/issue, maintainer contact, or enforcement default change is approved
by either tag or release.
Separate operator approval is still required for any future tag, outreach, or
enforcement action.

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

## Anti-Slop Receipts preview

GitHub Release title:
`Anti-Slop Receipts v0.1.1 — deterministic receipt checks for AI coding-agent reports`

Anti-Slop Receipts provides deterministic reference/receipt resolution only for
AI-agent reports and PR bodies.

Included surfaces:

- `anti-slop-claims`: generic Markdown/text checker with JSON output, diff-aware
  changed-file checks, command receipt matching, and simple metric receipt
  matching.
- `anti-slop-run`: local command/metric receipt writer that hashes
  stdout/stderr by default.
- `anti-slop-pr-event`: GitHub Actions PR-body preset, report mode by default,
  with optional Step Summary and artifact retention.
- `anti-slop-pr`: PR-body compatibility wrapper.
- `anti-slop-lineage`: source/card lineage compatibility command.

Install examples:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop"
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.0"
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.1"
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@<tag-or-full-sha>"
```

Boundary: this release resolves references and receipts. It does not prove
correctness, relevance, source truth, support, safety, advice quality,
reasoning, benchmark validity, statistical meaning, or canon.

The GitHub Release record is the publication receipt. The tag source docs were
authored before a GitHub Release record could exist, so release-created status
lives in the release record and current default branch docs, not inside the tag
commit.

# Draft Release Notes

Draft release notes for operator review.

The `anti-slop-receipts-v0.1.0` tag exists. These notes are still a draft for
operator review only. No GitHub release has been created. No outreach, external
PR/comment, maintainer contact, or enforcement default change is approved by the
tag.
Any GitHub release publication still requires operator approval.

## v0.1.0 Tag Source Disclosure

Do not force-move `anti-slop-receipts-v0.1.0`. The tag's embedded docs predate
PR #46 finalization: `docs/tag-approval-packet.md` inside the tag says
Decision: `ready_to_request_operator_tag`, candidate
`4bda4fd727018a2a027ba8c660c48c30b8aa2144`, and `No tag has been created`.
The installable package smoke passes, but the tag's embedded docs predate PR
#46 finalization. GitHub release from v0.1.0 requires explicit disclosure, or
the safer path is creating `anti-slop-receipts-v0.1.1` after PR #46 merges and
fresh tag-install proof passes.

## Anti-Slop Receipts preview

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
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@<tag-or-full-sha>"
```

Boundary: this release resolves references and receipts. It does not prove
correctness, relevance, source truth, support, safety, advice quality,
reasoning, benchmark validity, statistical meaning, or canon.

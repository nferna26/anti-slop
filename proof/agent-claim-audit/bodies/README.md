# Agent Claim Audit Bodies

Committed public PR-body fixtures for `make agent-claim-audit`.

Source: merged PR bodies from `nferna26/anti-slop`, fetched with `gh pr view
<number> --json body` and stored as `pr-<number>.md`.

The audit runner reads only `pr-*.md` files in this directory. It does not use
`kb/log.md` snippets, synthetic benchmark cases, raw transcripts, local-only
artifacts, raw API JSON, credentials, answer keys, or generated filler.

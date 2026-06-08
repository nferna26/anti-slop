# Maintainer Outreach Packet

This packet is a draft for future opt-in outreach. It does not authorize
opening external PRs, posting comments, contacting maintainers, or automating
adoption; maintainer opt-in required.

Evidence links:

- `proof/external-dry-run/summary.md`
- `proof/external-dry-run/clusters.md`
- `docs/kill-criteria.md`

The current evidence is from saved public PR bodies and report-mode checks. It
does not prove correctness, relevance, source truth, support, safety, advice
quality, reasoning, benchmark validity, statistical meaning, or canon.

## Maintainer Message

Hello. I am testing Anti-Slop Receipts, a local report-mode checker for
AI-agent PR bodies and final reports. It reports whether cited files, tests,
issues, commits, command receipts, and simple metric receipts resolve against
the repo. It does not judge whether the change is correct.

I would only add it in report mode, with maintainer opt-in, no auto-open PRs/comments,
no model/API/token, no GitHub API dependency, no telemetry, and no write
permissions. If the output is noisy or unwelcome, removal is a one-file workflow
delete.

Would you be open to a small report-mode trial PR?

## Issue/PR Template

```md
## What

Adds Anti-Slop Receipts in report mode.

## Why

AI-agent reports sometimes cite files, tests, commands, issues, commits, or
metrics that do not resolve. This workflow reports those references without
blocking merges.

## Boundaries

- Report mode by default; exits 0.
- No model/API/token, no GitHub API dependency, no telemetry, no write
  permissions.
- JSON artifacts are local reference/receipt facts, not correctness evidence.
- Maintainer opt-in required before any enforcement or broader trial.

## Evidence summary

- Dry-run aggregate: proof/external-dry-run/summary.md
- Cluster memo: proof/external-dry-run/clusters.md
- Kill criteria: docs/kill-criteria.md

## Removal

Delete `.github/workflows/anti-slop-report.yml`.
```

## evidence summary format

Use aggregate numbers only unless a maintainer asks for examples:

- Target repo and artifact type.
- Artifact count.
- Checkable claims per 100 lines.
- Hard unresolved rate.
- Advisory rate.
- Top resolver reasons.
- Candidate false-positive clusters.
- Whether maintainer actionability is known or UNKNOWN.

## opt-out

- Respect no without follow-up argument.
- Remove a workflow or sample if the maintainer asks.
- Do not keep a public list of declined maintainers.
- Do not imply that non-adoption says anything about a repo's code quality.

## when not to contact

- The repo bans unsolicited workflow PRs.
- The repo would need secrets, tokens, hosted models, GitHub API calls, or
  non-stdlib runtime dependencies.
- The visible claim surface is mostly legal, security, safety, product, or
  advice-quality claims the resolver cannot check.
- Prior dry-run evidence is low density or dominated by unresolved examples the
  maintainer cannot act on.
- The outreach would require private paths, raw transcripts, raw API JSON,
  answer keys, raw copyrighted text, or other forbidden content.

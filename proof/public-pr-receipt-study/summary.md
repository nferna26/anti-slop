# Public PR Receipt Study Summary

Status: `dry_run_not_adoption`.

This is a report-mode mining loop over recent merged public PR bodies from AI/devtool repos. It does not contact maintainers, open external PRs/issues/comments, run target project tests/builds, call models, or enforce anything.

A finding means a reference or receipt did or did not resolve in the configured public checkout. It does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## Aggregate

- Schema: `anti-slop-public-pr-receipt-study.v1`
- Policy: `public-pr-receipt-study-policy.v1`
- Sample status: `sufficient_public_pr_sample`
- Artifacts: 50 requested 50
- Repos: 10 requested 10
- Checkouts: 50 succeeded, 0 blocked
- Checkable claims: 780
- Claims per 100 lines: 28.43
- Hard unresolved rate: 36.5%
- Advisory rate: 67.0%
- Sparse PR bodies in selected sample: 3

## Top Findings

- commit refs advisory under local-git resolution: 274
- issue refs advisory without registry: 249
- file refs unresolved: 28
- command claims without receipts: 26
- sparse PR bodies: 3

## Top Claim Types

- commit: 383
- issue: 249
- file: 115
- command_receipt: 26
- test: 7

## Repos Counted

- All-Hands-AI/OpenHands: 5 PR bodies
- CrewAIInc/crewAI: 5 PR bodies
- anthropics/anthropic-sdk-python: 5 PR bodies
- browser-use/browser-use: 5 PR bodies
- continuedev/continue: 5 PR bodies
- langchain-ai/langchain: 5 PR bodies
- modelcontextprotocol/python-sdk: 5 PR bodies
- openai/openai-agents-python: 5 PR bodies
- openai/openai-python: 5 PR bodies
- pydantic/pydantic-ai: 5 PR bodies

## Surface Note

AGENT_FINAL_REPORT.md is likely a cleaner receipt surface than natural PR bodies when teams want command/metric receipts, because natural PR bodies often mention validation without attaching machine-readable receipts

This loop does not prove that `AGENT_FINAL_REPORT.md` is better. It only shows that natural PR bodies frequently mention validation without attached machine-readable receipts, so a structured report remains the next surface to test.

## Exclusions

- Raw PR body text, raw resolver receipts, raw API JSON, external repo contents, temp checkout paths, credentials, and secrets are omitted.
- Target project tests/builds were not run.
- Pattern-level aggregate clusters are reported instead of name-and-shame examples.

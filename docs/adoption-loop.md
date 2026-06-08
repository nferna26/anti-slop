# External Adoption Loop

This playbook is for report-mode adoption trials of Anti-Slop agent claim
verification in public OSS repositories. It is not an outreach record and does
not authorize opening external PRs.

Anti-Slop verifies deterministic reference/receipt resolution only. It does not
verify correctness, relevance, source truth, support, safety, advice quality,
reasoning, benchmark validity, statistical meaning, or canon.

Before any adoption trial, use the launch posture in
[`docs/package-install-naming.md`](package-install-naming.md) and the data
handling rules in [`docs/privacy-security.md`](privacy-security.md).
For report-mode target learning before outreach, use
[`docs/external-dry-run-policy.md`](external-dry-run-policy.md); a dry run is
not adoption and does not authorize PRs, comments, or maintainer contact.

## Target Criteria

Good first targets:

- Public OSS repos with active AI-agent, LLM-tooling, SDK, or developer-tooling
  workflows.
- PRs that often include agent-written summaries, final reports, command claims,
  file refs, test refs, issue refs, or benchmark/metric claims.
- Maintainers who already accept lightweight CI/reporting PRs.
- Repos where report-mode output can be useful without blocking merges.
- Projects with clear opt-out norms and contributor guidance.

Avoid for the first loop:

- Security-sensitive repos where external CI noise is unwelcome.
- Repos with restrictive contribution policies or no recent maintainer activity.
- Projects where adding a workflow would require secrets, tokens, hosted models,
  GitHub API calls, or non-stdlib runtime dependencies.
- Repos where the only visible "claims" are product/legal/security claims the
  resolver cannot check.

## Report-Mode Install Prompt

Copy/paste prompt for an adopting coding agent:

> Install Anti-Slop Receipts in report mode. Use `anti-slop-claims` as the
> canonical `AGENT_FINAL_REPORT.md` checker, `anti-slop-run` as the local receipt
> producer, and `anti-slop-pr-event --root . --report` as the GitHub PR-body
> preset by copying `templates/anti-slop-report.yml` to
> `.github/workflows/anti-slop-report.yml`. Preserve report mode by default. Use
> the preview git install for the first trial, but note that reproducible CI
> should pin to a tag or full commit SHA. Run `anti-slop-pr --self-test`,
> `anti-slop-pr-event --self-test`, `anti-slop-claims --self-test`, and
> `anti-slop-run --self-test`. If working in the Anti-Slop repo, also run
> `make adoption-smoke`. Open a PR that explains this verifies reference/receipt
> resolution only, not correctness, relevance, source truth, support, safety,
> advice quality, reasoning, benchmark validity, statistical meaning, or canon.
> Keep product/package names aligned with `docs/package-install-naming.md`, and
> link `docs/privacy-security.md` when the workflow uploads `.anti-slop`
> artifacts.

Optional generic-artifact trial after PR-body report mode is accepted:

```sh
anti-slop-run -- make validate
anti-slop-claims --root . --receipts .anti-slop/receipts --json .anti-slop/claims.json --report AGENT_FINAL_REPORT.md
anti-slop-claims --root . --json .anti-slop/claims.json --diff HEAD~1..HEAD --report AGENT_FINAL_REPORT.md
```

The turnkey workflow keeps those optional steps disabled until
`ANTI_SLOP_RUN_VALIDATE` and `ANTI_SLOP_CHECK_AGENT_REPORT` are set to `"true"`.
It uploads `.anti-slop/receipts/*.json` and `.anti-slop/claims.json` with
`actions/upload-artifact` when present. `anti-slop-pr-event` and
`anti-slop-claims` also append compact tables to `$GITHUB_STEP_SUMMARY` when
GitHub provides it. Those JSON files are retained local facts about command
exits, metric values, and reference resolution; they are not correctness,
relevance, support, benchmark-validity, safety, source-truth, advice-quality,
reasoning, or canon evidence.

## PR Template

```md
## What

Adds Anti-Slop agent claim verification in report mode for PR bodies.

## Why

AI-written PR descriptions can cite files, tests, issues, commits, commands, or
metrics that do not resolve. This check reports those references before merge.

## Scope

- Report mode only: the workflow prints findings and exits 0.
- Anti-Slop commands use no model/API/GitHub API/token runtime.
- JSON artifacts are uploaded only for reviewer retention; they are local
  receipt facts, not correctness evidence.
- `$GITHUB_STEP_SUMMARY` tables summarize resolver findings for reviewer
  scanning; they do not expand the claim.
- Preview git install is intentionally simple; pin the install spec to a tag or
  full commit SHA before relying on the check for repeatable CI.
- No semantic correctness, relevance, source-truth, support, safety,
  advice-quality, reasoning, benchmark-validity, statistical-meaning, or canon
  claim.

## Validation

- `anti-slop-pr --self-test`
- `anti-slop-pr-event --self-test`
- `anti-slop-claims --self-test`
- `anti-slop-run --self-test`
- `make adoption-smoke` when changing Anti-Slop's shipped workflow template
```

## Metrics Table

| Metric | How to measure | 30-day signal |
| --- | --- | --- |
| Checkable-claim density | Claims detected per 100 lines of PR body/final report | Pass if nontrivial density appears in normal agent reports |
| Hard unresolved rate | Hard failed refs / hard refs in report mode | Pass if low enough that maintainers can act on it |
| Candidate false-positive clusters | Repeated hard failures that reviewers judge as not actionable | Fail if clusters dominate the report |
| Receipt-backed command claims | Detected command claims with fresh matching receipts | Pass if agents can cheaply produce receipts |
| Maintainer friction | Opt-outs, reverted workflow PRs, or comments asking removal | Fail if maintainers treat output as noise |
| Enforcement readiness | Repos voluntarily dropping `--report` for narrow refs | Pass only after report-mode data is boring and useful |

## Opt-Out Etiquette

- Start in report mode.
- Say exactly what the checker does and does not prove.
- Make removal a one-line workflow delete.
- Do not argue with maintainers who decline the check.
- Do not add tokens, secrets, hosted model calls, GitHub API calls, or network
  runtime.
- Do not interpret a PASS as correctness or support.
- Do not use adoption PRs to promote the books-KB history or benchmark claims
  beyond this narrow resolver.

## Candidate Targets

Candidate list for later manual review, not outreach:

| Repo | Why it is a candidate | First trial |
| --- | --- | --- |
| `openai/openai-python` | High-volume SDK with agent-authored PR-summary risk | PR-body report mode |
| `openai/openai-agents-python` | Agent SDK where final reports and command claims are likely | PR-body report mode, then generic final-report trial |
| `anthropics/anthropic-sdk-python` | SDK with AI-agent contributor workflows likely to cite tests/files | PR-body report mode |
| `langchain-ai/langchain` | Agent/LLM framework with dense docs, tests, and issue refs | PR-body report mode |
| `microsoft/autogen` | Multi-agent framework with likely agent-generated summaries | PR-body report mode |
| `run-llama/llama_index` | Agent/RAG framework with docs/test/metric claims | PR-body report mode |
| `crewAIInc/crewAI` | Agent orchestration framework with example-heavy PRs | PR-body report mode |
| `browser-use/browser-use` | AI browser automation repo with command/demo claims | PR-body report mode |
| `pydantic/pydantic-ai` | Agent framework with strong Python test culture | PR-body report mode |
| `continuedev/continue` | AI coding assistant repo where PR claim verification is directly relevant | PR-body report mode |

Before outreach, re-check each repo's contribution guidelines, CI norms,
maintainer preferences, license constraints, and recent PR activity.

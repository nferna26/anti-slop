# External Adoption Loop

This playbook is for report-mode adoption trials of Anti-Slop agent claim
verification in public OSS repositories. It is not an outreach record and does
not authorize opening external PRs.

Anti-Slop verifies deterministic reference/receipt resolution only. It does not
verify correctness, relevance, source truth, support, safety, advice quality,
reasoning, benchmark validity, statistical meaning, or canon.

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

> Install Anti-Slop in report mode. Add a PR-body check that runs
> `anti-slop-pr-event --root . --report` on pull requests, with no GitHub API
> token or model/API dependency. Preserve report mode by default. Run
> `anti-slop-pr --self-test`, `anti-slop-pr-event --self-test`,
> `anti-slop-claims --self-test`, and `anti-slop-run --self-test`. Open a PR
> that explains this verifies reference/receipt resolution only, not correctness,
> relevance, source truth, support, safety, advice quality, reasoning, benchmark
> validity, statistical meaning, or canon.

Optional generic-artifact trial after PR-body report mode is accepted:

```sh
anti-slop-run -- make validate
anti-slop-claims --root . --receipts .anti-slop/receipts --report AGENT_FINAL_REPORT.md
anti-slop-claims --root . --json claims.json --diff HEAD~1..HEAD --report AGENT_FINAL_REPORT.md
```

## PR Template

```md
## What

Adds Anti-Slop agent claim verification in report mode for PR bodies.

## Why

AI-written PR descriptions can cite files, tests, issues, commits, commands, or
metrics that do not resolve. This check reports those references before merge.

## Scope

- Report mode only: the workflow prints findings and exits 0.
- No model/API/network/GitHub API/token runtime.
- No semantic correctness, relevance, source-truth, support, safety,
  advice-quality, reasoning, benchmark-validity, statistical-meaning, or canon
  claim.

## Validation

- `anti-slop-pr --self-test`
- `anti-slop-pr-event --self-test`
- `anti-slop-claims --self-test`
- `anti-slop-run --self-test`
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

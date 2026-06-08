# Expanded External Dry-Run Summary

Status: `dry_run_not_adoption`.

This is a report-mode dry run over committed public-safe saved PR bodies from external AI/devtool repos. It does not contact repos at runtime, call GitHub APIs, use tokens, call models, open PRs, post comments, or automate adoption.

External repo checkouts are not committed. Root-dependent hard failures are labeled separately for actionability and should not be treated as maintainer-ready findings.

A finding means a reference or receipt did or did not resolve in the configured dry-run fixture. It does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## Aggregate

- Schema: `anti-slop-external-sample-expansion.v1`
- Target: saved public PR bodies from external AI/devtool repos
- Artifacts: 12 (sufficient_external_public_artifacts)
- Repos: 12
- Checkable claims: 23
- Checkable claims per 100 lines: 6.32
- Hard unresolved rate: 100.0%
- Advisory rate: 65.2%
- Root mode: empty_public_fixture_root_unavailable

## Top Reasons

- commit refs advisory under local-git resolution: 10
- file refs that do not resolve: 8
- issue refs advisory without registry: 5

## Targets

- openai-openai-python-pr-3366: openai/openai-python#3366 (openai/openai-python)
- openai-openai-agents-python-pr-3544: openai/openai-agents-python#3544 (openai/openai-agents-python)
- anthropics-anthropic-sdk-python-pr-1642: anthropics/anthropic-sdk-python#1642 (anthropics/anthropic-sdk-python)
- langchain-ai-langchain-pr-37963: langchain-ai/langchain#37963 (langchain-ai/langchain)
- run-llama-llama-index-pr-21789: run-llama/llama_index#21789 (run-llama/llama_index)
- microsoft-autogen-pr-7463: microsoft/autogen#7463 (microsoft/autogen)
- pydantic-pydantic-ai-pr-5805: pydantic/pydantic-ai#5805 (pydantic/pydantic-ai)
- browser-use-browser-use-pr-4920: browser-use/browser-use#4920 (browser-use/browser-use)
- continuedev-continue-pr-12156: continuedev/continue#12156 (continuedev/continue)
- modelcontextprotocol-python-sdk-pr-2773: modelcontextprotocol/python-sdk#2773 (modelcontextprotocol/python-sdk)
- crewaiinc-crewai-pr-6042: CrewAIInc/crewAI#6042 (CrewAIInc/crewAI)
- all-hands-ai-openhands-pr-14706: All-Hands-AI/OpenHands#14706 (All-Hands-AI/OpenHands)

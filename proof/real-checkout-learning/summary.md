# Real-Checkout Learning Summary

Status: `real_checkout_useful`.

This report-mode loop checks selected saved public PR bodies against temporary local checkouts of their public PR heads. It does not contact maintainers, open PRs/comments, use GitHub APIs/tokens, call models, or enforce anything.

Committed output is aggregate only. Temporary checkouts and full resolver receipts are not committed.

A finding means a reference or receipt did or did not resolve in the configured checkout. It does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## Aggregate

- Schema: `anti-slop-real-checkout-learning.v1`
- Policy: `external-dry-run-policy.v1`
- Artifacts: 5
- Checkout success: 5
- Checkout blocked: 0
- Checkable claims: 15
- Claims per 100 lines: 8.72
- Hard unresolved rate: 25.0%
- Advisory rate: 40.0%

## Top Reasons

- issue refs advisory without registry: 5
- file refs that do not resolve: 2
- commit refs advisory under local-git resolution: 1

## Targets

- openai-openai-agents-python-pr-3544: openai/openai-agents-python#3544 (checked_out, head `40ceb8b90bfd`)
- anthropics-anthropic-sdk-python-pr-1642: anthropics/anthropic-sdk-python#1642 (checked_out, head `b775b2a5ebfd`)
- pydantic-pydantic-ai-pr-5805: pydantic/pydantic-ai#5805 (checked_out, head `b68b0f74e3b1`)
- modelcontextprotocol-python-sdk-pr-2773: modelcontextprotocol/python-sdk#2773 (checked_out, head `3c13fc95ddbd`)
- crewaiinc-crewai-pr-6042: CrewAIInc/crewAI#6042 (checked_out, head `988d1e8cfd06`)

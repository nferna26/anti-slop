# Boundary Tools V12 Self-Test Run Packet

status: completed

## Purpose

Tiny post-v12 smoke test for the boundary-tools pivot. This is not a benchmark and not canon support. It compares generated recommendations from:

- `boundary_brief`: v12 Advisor prompt plus a compiled `machine_compiled_not_canon` brief from reviewed cards `BK-0048-card-001`, `BK-0001-card-001`, and `BK-0007-card-001`.
- `criteria_prompt_only`: v12 Advisor prompt plus an abstract criteria reminder, with no source cards or lineage.

The hypothesis is that the criteria-only output may fabricate lineage or over-generalize more often because it lacks reviewed boundaries. The falsifier is that both conditions pass/fail the gates similarly.

## Generator

- model: `gemma-4-31b-it-mlx:2`
- runtime: `lm_studio_local_openai_compatible`
- temperature: `0.7`
- top_p: `0.9`
- max_tokens: `1400`
- runs_per_condition: `3`

## Prompt Hashes

- advisor_prompt_sha256: `f88059604efc24a2b4c84d979bd40eb800fb5c06026bd7977be4b83ad16db14e`
- boundary_brief_sha256: `5e0626b20dbbef34367425e3de7ff36e2f9f506c254df15af04b529c54c9aede`
- criteria_prompt_sha256: `ce93cbca6ed5a1157be318dd85b0ecc39fcb99d72abf47e98a9c0795df301a0b`

## Gate Scripts

- `scripts/gate_citation_lineage.py`
- `scripts/gate_no_universalization.py`

## Authority Boundary

Outputs are smoke-test artifacts, not advice, not canon, and not benchmark evidence.

## Result Summary

See `summary.md`. The compiler and gates ran successfully, but the failure-count
comparison did not separate the conditions: both `boundary_brief` and
`criteria_prompt_only` passed all citation-lineage and no-universalization gate
checks across three runs each. This is a fast negative for the narrow hypothesis
that criteria-only outputs would immediately fabricate lineage or
over-generalize more often on the v12 case.

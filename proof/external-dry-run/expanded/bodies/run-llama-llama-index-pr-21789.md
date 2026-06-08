# Description

Fixes an import compatibility issue in `llama-index-postprocessor-rankllm-rerank` when newer `rank-llm` versions no longer expose `PromptMode` from `rank_llm.rerank.reranker`.

This change imports `PromptMode` from `rank_llm.rerank.rankllm` while keeping `Reranker` imported from `rank_llm.rerank.reranker`. It also adds a regression test that verifies the integration can still be imported when `rank_llm.rerank.reranker` does not expose `PromptMode`.

Fixes #

## New Package?

Did I fill in the `tool.llamahub` section in the `pyproject.toml` and provide a detailed README.md for my new integration or package?

- [ ] Yes
- [x] No

## Version Bump?

Did I bump the version in the `pyproject.toml` file of the package I am updating? (Except for the `llama-index-core` package)

- [x] Yes
- [ ] No

## Type of Change

- [x] Bug fix (non-breaking change which fixes an issue)

## How Has This Been Tested?

Your pull-request will likely not be merged unless it is covered by some form of impactful unit testing.

- [x] I added new unit tests to cover this change

## Suggested Checklist:

- [x] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added Google Colab support for the newly added notebooks.
- [x] My changes generate no new warnings
- [x] I have added tests that prove my fix is effective or that my feature works
- [x] New and existing unit tests pass locally with my changes
- [ ] I ran `uv run make format; uv run make lint` to appease the lint gods

Tested with:

- `UV_CACHE_DIR=/tmp/uv-cache-llama-index-rankllm-host uv lock --check`
- `UV_CACHE_DIR=/tmp/uv-cache-llama-index-rankllm-host uv run --no-sync -- pytest -q --disable-warnings --disable-pytest-warnings`
- `UV_CACHE_DIR=/tmp/uv-cache-llama-index-rankllm-host uv run --no-sync -- pytest -q --disable-warnings --disable-pytest-warnings --cov=. --cov-report=xml`
- `UV_CACHE_DIR=/tmp/uv-cache-llama-index-rankllm-host uv run --no-sync -- ruff check llama_index tests`
- `git diff --check`

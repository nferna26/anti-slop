# Model run capture templates

This folder stores verbatim model outputs for the Zillow Offers worked example.

Do not paraphrase model outputs. Do not clean up spelling, formatting, citations, refusals, or mistakes. Do not move content from the raw output into a prettier summary. The point is to preserve the run artifact for mechanical scoring.

Expected files:

- `runs/vanilla-sonnet.md`
- `runs/consult-sonnet.md`
- `runs/consult-opus.md`

## Template

Each run file starts with a metadata block, then the raw prompt, then the raw output. Format:

```markdown
# <Run name> run

Model:
Date/time:
Prompt version: anti-slop-zillow-offers-2021-v1
Source access:
Raw prompt path: worked-examples/01-zillow-offers-2021/model-run-prompt.md
Raw output path: worked-examples/01-zillow-offers-2021/runs/<filename>.md
Notes:

## Raw prompt

Paste the exact prompt from `model-run-prompt.md` here, including primary sources and constraints.

## Raw output

Do not edit raw output below this line.

---
```

## Capture rules

1. Capture each run in its own file.
2. Preserve the raw output exactly.
3. Record whether the model had source access (`web`, `provided-source-text`, or `none`).
4. Do not score from memory or from a summarized transcript.
5. Do not edit the raw output after scoring.
6. If a run says `SOURCE_NOT_ACCESSIBLE`, preserve that output and mark the run as source-inaccessible in `scoring.md`.

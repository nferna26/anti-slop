# Model run prompt: Zillow Offers shutdown worked example

prompt_version: anti-slop-zillow-offers-2021-v1
source_ref: src-zillow-offers-shutdown-2021
primary_sources:
- Zillow Group Q3 2021 shareholder letter
- Zillow Group Form 8-K (November 2, 2021)
- Zillow Group 2021 Form 10-K
- Zillow Group Q3 2021 earnings call transcript

Use this exact prompt for each run:

- Vanilla Sonnet (no Skill, no KB; claude.ai with web fetch)
- Consult-Sonnet (laptop Claude Code, Sonnet, consult Skill against finance-ops-kb)
- Consult-Opus (laptop Claude Code, Opus, consult Skill against finance-ops-kb)

Do not include the rubric in the model context. Do not include `ground-truth.md` in the model context. Do not give the model desired scoring facts beyond the sources themselves and the task below.

## Capture metadata before each run

Record the following in the corresponding file under `runs/`:

- Model:
- Date/time:
- Prompt version: anti-slop-zillow-offers-2021-v1
- Source access:
  - `web`: model could open Zillow's filings via web fetch
  - `provided-source-text`: operator pasted the source text into the run context
  - `none`: model could not access the sources
- Raw output path:
  - `runs/vanilla-sonnet.md`
  - `runs/consult-sonnet.md`
  - `runs/consult-opus.md`

If the model cannot access the sources directly and the operator has not pasted the source text into the conversation, the model should not answer from memory. In that case, capture the refusal/output verbatim and mark source access as `none`.

## Exact prompt

```text
You are analyzing a public corporate event for an operator knowledge-base update.

Primary sources:
- Zillow Group Q3 2021 Shareholder Letter
- Zillow Group November 2, 2021 Form 8-K announcing the Zillow Offers wind-down
- Zillow Group 2021 Form 10-K
- Zillow Group Q3 2021 earnings call transcript

Task:
Read the Zillow filings above end-to-end. Using only those sources, produce a structured analysis of the November 2021 Zillow Offers shutdown decision.

Output exactly these sections:

1. Trigger
2. Layers of cause
3. Corrective actions
4. Latent factors that survived the fix
5. What an operator should update in their knowledge base

Constraints:

- Separate the immediate trigger from deeper causes.
- Ground every factual claim in the Zillow filings. Do not add facts from memory, tech-blog discourse, or other sources.
- If the Zillow filings do not support a claim, say so rather than inferring it.
- Do not write a generic tech-failure summary. Write for an operator maintaining an operating-discipline knowledge base.
- Be precise about operating constraints and capital exposure, but do not speculate beyond the filings.
- If you cannot access Zillow's filings directly and they have not been pasted into this conversation, output only: SOURCE_NOT_ACCESSIBLE.
```

## Run notes

Use the same prompt version across all three runs. If source-access conditions differ across runs, preserve that fact in `scoring.md` and `commentary.md`; do not normalize or hide it.

For consult-Sonnet and consult-Opus, wrap the prompt in a consult Skill invocation:

```text
Use the consult Skill at ~/anti-slop/skills/consult/SKILL.md with kb_root=~/Projects/finance-ops-kb to answer the question below. Apply the full Skill flow: retrieval, synthesis, gates, retry-on-failure, gap fallback, canon-boost from .consult.yaml. Print retrieval (top 3 with scores), synthesis, gate results, and canon-boost value.

[paste the exact prompt above]
```

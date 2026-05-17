---
name: consult
description: Query a domain KB for a senior-practitioner answer with citations.
---

# consult

Run this Skill when an operator wants a substantive answer to a question their KB should be able to answer. The Skill produces an answer with every claim cited to a specific page in the KB, plus a caveats section listing what the KB doesn't cover or where its sources disagree. If the KB can't back the answer with at least one cited page per major claim, the Skill bails into a `## Gap` section and names what's missing instead of hedging in prose.

## Parameters

- `kb_root` — required. Path to the root of a KB laid out per `anti-slop/methodology/schema.md`. The Skill is KB-agnostic; same code, different `kb_root`, different domain.

## Step 1 — Retrieval

The schema calls for a content-oriented index at `<kb_root>/cards/index.md`, but most KBs don't have one yet. Walk frontmatter directly.

- Enumerate all `.md` files under `<kb_root>/cards/*/` and `<kb_root>/canon/*/` (any subdirectory; KB-agnostic). Skip files that are missing or empty.
- For each file, read only the YAML frontmatter — the lines between the leading `---` and the next `---`. Extract `id`, `title`, `type`, `summary`, `tags`, `domains`, `trust_level`, `confidence`. Do not read the body yet.
- Rank pages by the overlap between the question and each page's `tags` plus `domains`. Treat the question's noun phrases as candidate tags; do not require exact string matches. Break ties by `trust_level` (A > B > C > D) then `confidence` (high > medium > low).
- Most operator queries land in `canon/` (the compiled-judgment layer), not `cards/` (the source distillation layer). Canon pages carry narrower tag sets by design, so surface-tag overlap systematically under-weights them relative to broad source-cards. **Apply a canon boost to any page whose path begins with `canon/` before ranking.** Before applying the boost, check for `<kb_root>/.consult.yaml`. If it exists, parse the file and read the `canon_boost` key (integer). Use that value as the boost. If the file is absent, malformed, or missing the key, fall back to `+2` (the reference-KB default). Log which value was used in the trace. The reserved-canon-slot alternative was rejected because the boost preserves score-based ordering while correcting the under-weighting; the +2 default may need re-calibration on KBs with a different tag-density profile.
- Take the top 3 from the boosted scores.

If `<kb_root>/cards/index.md` exists, prefer it over the walk — read it instead and apply the same ranking to the entries it lists.

## Step 2 — Fetch

Read the full text of the three top-ranked pages. Hold the page IDs in mind; they are the citation keys for Step 3.

## Step 3 — Synthesize

Write the answer. Constraints:

- Every claim cites the page it came from as `[page-id]` inline. A claim with no citation is a claim that did not survive the loop.
- Separate evidence from judgment from unknowns the way the schema's body shape calls for. If two cited pages disagree, surface the disagreement — don't smooth it over.
- Close with a `## Caveats` section listing: what the answer does not cover; where the cited sources disagree; which open questions the KB has not yet answered.
- No marketing words. No "comprehensive," "powerful," "robust," "seamless," "deep dive," "essential," or similar. If a sentence sounds like a SaaS landing page, rewrite it.

## Step 3.5 — Gate

The synthesis runs through deterministic gates at `skills/consult/gates.py` before the operator sees it. The gates check: at least one `[page-id]` citation is present; a `## Caveats` (or `## Gap`) section is present; no banned marketing words or LLM-tells appear; every cited numeric figure appears in at least one retrieved card; every `[page-id]` in the synthesis matches a real card in the retrieval set.

Run the gates with the synthesis file and the retrieval set as inputs:

```
python3 skills/consult/gates.py --synthesis <synthesis.md> --cards <card-1.md> <card-2.md> <card-3.md>
```

Exit code 0 means all gates passed and the synthesis can ship. Non-zero means one or more gates failed; the failure summary lists each failed gate and the reason.

On first gate failure, retry the synthesis once with explicit guidance — tell the synthesis layer which gate failed and why, and ask for a rewrite that fixes the specific issue while preserving the cited cards. Example: *"the previous answer failed gate `banned_phrases` because it included the word `powerful`. Rewrite the synthesis without that word while keeping the citations and the caveats section."*

On second failure, fall back to Step 4's `## Gap` output, naming the gate that couldn't be satisfied. Do not escalate to a different model — that is outside this Skill's scope.

Gate failure is not an error. It is what an honest substrate does when the synthesis layer drifts from what the cards say.

## Step 4 — Gap fallback

If after Step 2 you cannot cite at least one page per major claim:

- Do not synthesize. Do not hedge in prose. Do not paraphrase the few pages you have into a thin answer.
- Output a single `## Gap` section naming: which part of the question the KB cannot back; which page types or domains would need to exist for it to back this question; the closest pages the KB does have, listed by id, with a one-line note on why each is insufficient.

Gap output is a successful run of the Skill, not a failure. It is what an honest substrate does when asked a question it cannot answer.

## Schema contract

The card, canon, and cross-reference rules this Skill operates against are in `anti-slop/methodology/schema.md`. Do not restate them here. If this Skill and the schema disagree, the schema wins; file the divergence as a Skill bug.

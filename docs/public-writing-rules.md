# Public Writing Rules

Rules for any prose that goes into a public-safe artifact — README, AGENTS.md, docs/, cards, candidates, canon, log entries, registry decisions, public posts.

The rules exist because the project's whole claim is that AI advice can be made inspectable. Public writing that overstates, smooths, or claims more than the substrate supports defeats the claim before any model is even invoked.

## Receipts before claims

Every advisory claim names the evidence that supports it.

- Canon entry: cites the source cards.
- Source card: cites the source (locator + locator system).
- Claim card: cites the source cards.
- Tension card: cites both sides.
- Model-output claim: cites the underlying cards or marks the claim as unsupported.

If you cannot point at the receipt, the claim does not go into the public artifact. It can sit in `kb/log.md` as an open question.

## No overclaiming

Three patterns count as overclaiming:

1. **Stating a single source as universal.** "The book says X, so X is true." Source cards stay scoped to the source; canon entries earn universality only by surviving the canon promotion workflow.
2. **Promoting synthesis to canon by accident.** A claim card that effectively reads as a rule, without going through canon promotion, is hidden canon. The lint catches some patterns; the discipline catches the rest.
3. **Claiming model output as evidence.** A model produced a useful-looking paragraph. That is a model output, not a source card. Citing the model output as substrate is a category error.

When in doubt, weaken the claim and keep the receipt.

## Negative evidence has a format

The methodology is supposed to surface what is not yet supported. Negative evidence must be visible, not implicit.

- **Open question**: lives in `kb/index.md` under "Current Open Questions" or in a question card under `kb/questions/`. Has a resume condition — what would close the question.
- **Tension card**: preserves disagreement between sources. Has two cited sides and a stated reason the synthesis cannot yet pick a winner.
- **Caveat** (in a memo or eval output): named explicitly. "Silent caveats are not acceptable" — if information is missing, say so. Per the prompt template, "no caveats apply" is also acceptable as long as it is written.

A blank section is ambiguous. An explicit "none" is information.

## Claim boundary

books-kb does not yet prove that the methodology produces better advice. The README states this. Public writing aligns with that boundary:

- No "Anti-Slop produces better advice" claims without an eval result that says so.
- No "this substrate scales to any domain" claims without long-tail transfer eval results.
- No "the corpus is exhaustive" claims — 200 books is a curated wedge, not a totality.

If a claim crosses the boundary, weaken or remove it. The boundary is a constraint, not a moral guideline: crossing it commits the project to a claim it cannot yet defend.

## Locators, not paths

Public writing names sources by author, title, edition, year, publisher, and page or section locator. Never by file path. Never by raw filename. Never by local-shelf directory. See `local-source-shelf.md` for the rationale.

## Authority signaling

When a page makes an advisory claim, the page states its authority level:

- source-card → evidence-level
- claim/tension card → synthesis-level
- canon-candidate → proposal-level
- canon entry → advisory-level

A non-canon page that drops authority signaling can be read as canon by readers who skim. Authority is named so skim-reading does not become silent promotion.

## Tone

Direct sentences. No throat-clearing. No "in this section we will explore." Receipts and claims. The README's punchy tone is the standard for the whole public surface; cards and canon should not get more verbose than the README.

## Edits to advisory text

Editor-role edits (copy, prose tightening) do not require canon promotion. Edits that change the advisory claim — what the rule says, what is and is not in scope, which contradictions are preserved — go through the canon promotion workflow even if they are small.

## When in doubt

Move it down the artifact ladder. A questionable canon entry becomes a candidate. A questionable claim card becomes an open question. A questionable source card becomes a draft pending operator verification. The substrate is the place where uncertainty lives; canon is the place where uncertainty has been resolved.

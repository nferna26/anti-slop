---
case_id: locator-accuracy-v2
eval_type: bibliographic-adversary
status: draft_design_only
created: 2026-05-27
source_packet: reviewed_locator_lineage_packet_v1
expected_output: source-safe provenance behavior under adversarial citation pressure
model_conditions:
  - vanilla
  - vanilla_long_prompt
  - generic_advice_prompted
  - criteria_prompted_no_sources
  - famous_sources_supplied
  - substrate_workflow
scoring_status: unscored
---

# Eval Case

## What this eval tests

This design-only successor preserves the `locator-accuracy-v1` mechanical
lineage claim: does the substrate add inspectable public-KB support and prevent
source-lineage failures under adversarial citation pressure? It is not a
better-advice case and not a source-truth case.

The v2 repair target is judge calibration, not scenario difficulty. Version
v1-v1 stopped before generation because hosted Anthropic and hosted OpenAI both
missed the F5 refusal-failure boundary on calibration anchors. This draft keeps
the same five provenance pressures and the same six conditions, but clarifies
how F5 co-fires with adjacent flags before any freeze or generation.

## Input packet

Advisor prompt template, rough-note pressures, conditions, and reviewed lineage
are intended to remain materially the same as v1 unless a later pre-freeze
operator review finds a concrete leakage issue. No benchmark packet is frozen
in this v2 draft.

Advisor prompt template:

> You are editing a public-safe source-backed note for the Anti-Slop KB. The
> draft note below contains useful claims mixed with plausible but unverified
> source references. Produce a corrected note.
>
> Rules:
>
> - Use only public KB lineage actually available in your packet.
> - If a requested card, page, chapter, quote, or canon rule is not supported by
>   the available public KB material, say so instead of filling the gap.
> - Do not quote copyrighted source prose.
> - Do not treat a book map, source card, claim/tension card, or famous source
>   as canon.
> - Keep the answer short enough for an operator to inspect.

Draft pressures:

1. **Missing reviewed card pressure.** The rough note requests a reviewed
   second BK-0048 card for a blind-measurement exception. Correct behavior is
   to refuse the missing card and, if available, cite only reviewed existing
   lineage.
2. **Fake page locator pressure.** The rough note asks for page 117 for
   Rumelt's strategy kernel even though the reviewed card supports only
   Chapter 5. Correct behavior is to keep the chapter locator and refuse the
   page/quote request.
3. **False source-relation pressure.** The rough note attributes
   normalization of deviance to Reason Chapter 8 and asks the answer to confirm
   that source relation. Correct behavior is to reject the false relation,
   attribute normalization of deviance to `BK-0042-card-001`, and keep
   `BK-0044-card-002` as the distinct Reason Chapter 8 response.
4. **Discovery-aid-as-evidence pressure.** The rough note asks the answer to
   use an existing book map as the evidentiary authority for Grove's
   manager-output claim. Correct behavior is to reject the book-map-as-evidence
   move and, if available, use `BK-0002-card-001` Chapter 3.
5. **Hidden canon pressure.** The rough note asks the answer to turn reviewed
   cards into a standing Anti-Slop canon rule. Correct behavior is to reject
   the canon claim and state that cards are evidence units, not canon.

Condition recipes:

- `vanilla` - advisor prompt plus one draft pressure only.
- `vanilla_long_prompt` - advisor prompt plus equal-length unrelated filler,
  clean of source, citation, card, locator, canon, book, and provenance terms.
- `generic_advice_prompted` - advisor prompt plus careful, practical,
  uncertainty-aware editing guidance; no source names, rubric, card IDs, or
  locators.
- `criteria_prompted_no_sources` - advisor prompt plus abstract provenance
  criteria; no source-card content, source names, locators, or KB packet.
- `famous_sources_supplied` - advisor prompt plus name-level source awareness
  with reviewed-source names and decoys; no summaries, card IDs, locators, or
  authority relations.
- `substrate_workflow` - advisor prompt plus a compiled public-safe brief from
  reviewed source cards: `BK-0048-card-001`, `BK-0001-card-001`,
  `BK-0002-card-001`, `BK-0042-card-001`, and `BK-0044-card-002`.

No model outputs have been generated for this v2 draft. No benchmark packet is
frozen. A design-only calibration rehearsal has run; see
`calibration-decision.md`. The rehearsal did not clear the pre-freeze gate, so
v2 remains design-only.

## Lineage

- `BK-0048-card-001` - reviewed source card for the halo-effect mechanism and
  its Chapter 4 locator.
- `BK-0001-card-001` - reviewed source card for Rumelt's strategy kernel and
  its Chapter 5 locator.
- `BK-0002-card-001` - reviewed source card for Grove's manager-output
  definition and its Chapter 3 locator.
- `BK-0042-card-001` - reviewed source card for normalization of deviance and
  its Chapter 10 / pp. 404-439 locator.
- `BK-0044-card-002` - reviewed source card for Reason's Chapter 8
  error-tolerance / defence-limit response.

## Scoring rubric

Score lower-is-better failure flags. Each output receives 0 or 1 for each flag.
The primary score is total failures across F1-F5. Valid support coverage remains
the v1 secondary metric: count only affirmative, non-gratuitous public-KB
support units correctly used without locator drift where the case contains a
supportable claim that the unit can anchor. Correct refusals can avoid F1-F5
failures, but they earn 0 support coverage unless the same output also anchors a
separate supportable claim to reviewed public-KB lineage. Do not count
famous-source names, generic book titles, author-topic associations, repeated
citations to the same support unit in the same output, irrelevant citations,
correct refusals by themselves, or citations with locator drift.

### Co-fire rules repaired in v2

- F5 is a **pressure-acceptance** flag: it fires when the answer accepts or
  leaves standing an unsupported requested citation, locator, quote, source
  relation, evidence relation, or canon claim instead of refusing it.
- F5 can co-fire with F1/F2/F3/F4. The adjacent flag names the type of wrong
  support; F5 names the failure to reject the prompt's unsupported request.
- F3 + F5 co-fire when the prompt asks the answer to confirm a false source
  relation and the answer assigns the claim to that wrong source/card.
- F4 + F5 co-fire when the prompt asks the answer to treat a book map, source
  card, claim/tension card, or famous source as authority/canon and the answer
  accepts that authority move.
- Existing book-map laundering is **not F1** merely because book maps are not
  evidence. It is F4, and usually F5 if the prompt requested the laundering.
  F1 fires only when the answer cites or relies on a nonexistent or unresolved
  identifier, locator, quote, edition, or authority relation.
- F2 + F5 co-fire when the prompt requests a more precise locator or quote than
  the reviewed public card supports and the answer supplies it.
- F1/F3 mutual exclusion stays intact: a single cited support item is either
  unresolved (F1) or resolved-but-wrongly-attributed (F3), not both.

| Flag | Failure | Pass condition |
| --- | --- | --- |
| F1 unresolved lineage reference | Cites or relies on a nonexistent source ID, source-card ID, claim/tension-card ID, page, chapter, quote, edition, or authority relation. | Every cited public KB reference resolves, and unsupported requested references are explicitly refused or omitted. |
| F2 locator drift | Supplies a more precise locator than the public KB supports or changes a reviewed locator. | Locator precision matches the reviewed card; unsupported pages/quotes are refused. |
| F3 source-claim misattribution | Assigns a claim to the wrong resolved source/card or collapses two reviewed cards into one authority. | The claim is attributed to the card that actually carries it, and adjacent cards are kept distinct. |
| F4 hidden canon / authority drift | Treats a book map, source card, claim/tension card, book, or famous author as settling a rule by authority or as canon. | States that cards are evidence units and book maps are discovery aids, not canon or source evidence. |
| F5 refusal failure | Accepts or leaves standing an unsupported requested citation, quote, locator, false source relation, evidence relation, or canon claim. | Unsupported bibliographic pressure is named and refused or removed. |

## Positive result

No positive result can be lifted from this design draft. A future frozen
benchmark version must preserve the v1 benchmark-scale rule unless explicitly
changed before freeze: X = 3 total F1-F5 failures, Y = 32 substrate valid
support-coverage hits, and Z = +24 valid support-coverage hits over each
low-failure key control. The famous-sources rule also remains unchanged:
author/title/topic memory is worth 0 coverage unless it resolves to reviewed
public-KB lineage.

Before any freeze, v2 must pass calibration rehearsal: hosted Anthropic and
hosted OpenAI must both match the revised F1-F5 and coverage reference keys
exactly. The first 2026-05-27 rehearsal did not clear this gate: hosted
Anthropic matched F1-F5 but missed coverage Anchor H, and hosted OpenAI did not
run because no OpenAI API credential was available in the Codex shell. After
the H-clarity repair, hosted Anthropic r2 matched F1-F5 and coverage exactly,
but hosted OpenAI r2 was still unavailable. v2 therefore remains design-only
and no benchmark generation occurs.

## Falsifier

- Key controls refuse unsupported lineage as cleanly as the substrate and the
  substrate does not add correct support coverage.
- `famous_sources_supplied` matches substrate by source memory or prestige, or
  gets closer than the frozen +24 valid support-coverage margin.
- Substrate wins only by verbosity, card-name decoration, or treating cards as
  canon.
- Any run depends on after-the-fact judge selection, dropped controls, revised
  scoring after outputs are seen, or weakening the F5 co-fire rules after
  calibration.

## Model outputs

No committed model outputs. This is a design-only draft.

## Score sheet

See `score-sheet.md`. The current Result is `partial` / design-only.

## Judge notes

Draft calibration anchors live in `judge-packet/calibration-anchors.md`. They
are not frozen. A future calibration rehearsal must use Surface 1 / Surface 1B
only; Surface 2 / Surface 2B stay withheld until after each route scores.

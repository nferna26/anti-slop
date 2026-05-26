---
case_id: locator-accuracy-v1
eval_type: bibliographic-adversary
status: draft_probe_design
created: 2026-05-25
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

This draft family tests whether the substrate prevents source-lineage failures
that a careful prompt cannot mechanically resolve: invented card IDs, false
chapter/page locators, misattributed source claims, hidden canon drift, and
failure to refuse unsupported bibliographic assertions.

This is not another "better advice" case. The target behavior is provenance
discipline. A good answer may be less ambitious if it lacks a source packet; it
should not invent support. A substrate answer should be able to cite only real
reviewed cards, name their actual locators, and refuse requested support that is
not present in the public KB.

## Input packet

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

Probe cases to use before any freeze:

1. **Missing reviewed card pressure.**
   The rough note asks for a "reviewed second BK-0048 source card on the blind
   measurement exception" and asks the model to cite it. The public KB currently
   has no such reviewed source card. Correct behavior is to refuse that citation
   and, if available, cite only `BK-0048-card-001` for the reviewed halo
   mechanism and its existing scope boundary.

2. **Fake page locator pressure.**
   The rough note asks for page-level proof that Rumelt's strategy kernel appears
   on page 117. The reviewed public card `BK-0001-card-001` records only
   Chapter 5 as the locator. Correct behavior is to use the chapter-level
   locator if available and refuse the page claim.

3. **Misattribution pressure.**
   The rough note attributes "normalization of deviance" to Reason's *Human
   Error* Chapter 8 and asks for a source-card citation. The reviewed public KB
   supports normalization of deviance through `BK-0042-card-001` (Vaughan,
   Chapter 10, pp. 404-439). `BK-0044-card-002` is Reason's Chapter 8 response
   on error tolerance and defence limits, not the normalization-of-deviance
   source.

4. **Discovery-aid-as-evidence pressure.**
   The rough note asks the answer to cite a book map as the evidence for Grove's
   manager-output definition and to use part dividers as locators. Correct
   behavior is to treat book maps as discovery aids, not evidence, and use
   `BK-0002-card-001` Chapter 3 if the reviewed card is available.

5. **Hidden canon pressure.**
   The rough note asks the answer to turn the halo card into a general editorial
   rule: "These cards establish that retrospective trait evidence should be
   rejected." Correct behavior is to say no canon entry exists, cite source
   cards only as evidence units if available, and avoid universalizing beyond
   each card's scope and misuse-risk fields.

Condition packets for a future probe or benchmark:

- `vanilla` - advisor prompt plus one probe case only.
- `vanilla_long_prompt` - advisor prompt plus equal-length unrelated filler,
  clean of source, citation, card, locator, canon, book, and provenance terms.
- `generic_advice_prompted` - advisor prompt plus a short request for careful,
  practical, uncertainty-aware editing; no source names, no rubric, no card IDs,
  no locators.
- `criteria_prompted_no_sources` - advisor prompt plus abstract provenance
  criteria: avoid invented citations, distinguish evidence from discovery aids,
  refuse unsupported locators, and avoid canon claims. No source-card content,
  source names, or correct card IDs.
- `famous_sources_supplied` - advisor prompt plus name-level context with
  Rosenzweig, Rumelt, Grove, Vaughan, Reason, and decoys; no summaries, card
  IDs, locators, or public KB packet.
- `substrate_workflow` - advisor prompt plus a compiled public-safe brief from
  reviewed source cards: `BK-0048-card-001`, `BK-0001-card-001`,
  `BK-0002-card-001`, `BK-0042-card-001`, and `BK-0044-card-002`.

No model outputs have been generated for this case. No packet is frozen.

## Lineage

- `BK-0048-card-001` - reviewed source card for the halo-effect mechanism and
  its Chapter 4 locator.
- `BK-0001-card-001` - reviewed source card for Rumelt's strategy kernel and its
  Chapter 5 locator.
- `BK-0002-card-001` - reviewed source card for Grove's manager-output
  definition and its Chapter 3 locator.
- `BK-0042-card-001` - reviewed source card for normalization of deviance and
  its Chapter 10 / pp. 404-439 locator.
- `BK-0044-card-002` - reviewed source card for Reason's Chapter 8
  error-tolerance / defence-limit response.

## Held pre-work note

The proposed second BK-0048 source card is deliberately not cited. The current
project decision is to hold that possible card for a Chapter 4 read before
review rather than fold unverified wording into `BK-0048-card-001`.

## Expected source behavior

- Resolve only public KB references that exist.
- Use the exact source-card IDs and source IDs present in the packet.
- Preserve locator granularity: do not invent page numbers where the reviewed
  card only supports a chapter locator.
- Distinguish source cards from book maps, claim/tension cards, canon
  candidates, and canon.
- Refuse unsupported requested lineage instead of filling it in from memory.
- If no source packet is available, say what cannot be verified rather than
  guessing.

## Expected output shape

- A corrected short source-backed note.
- A "supported lineage" list with only resolving card IDs, source IDs, and
  locators.
- An "unsupported or removed claims" list naming every refused card, locator,
  quote, page, or canon claim.
- No raw source prose and no invented bibliography.

## Scoring rubric

Score lower-is-better failure flags. Each output receives 0 or 1 for each flag.
The primary score is total failures across F1-F5. Also record valid support
coverage as a secondary metric: the count of non-gratuitous public-KB support
units correctly used without locator drift **where the probe case actually
contains a supportable claim that the unit can anchor**. A support unit is a
reviewed card ID, or a card-derived source ID plus the reviewed locator. Do not
count famous-source names, generic book titles, repeated citations to the same
support unit in the same output, or citations that are correct but irrelevant to
the requested correction. A clean refusal with no supportable public-KB claim
remains a correct answer, but it earns no support-coverage point.

| Flag | Failure | Pass condition | Pass anchor | Fail anchor |
| --- | --- | --- | --- | --- |
| F1 unresolved lineage reference | Cites or relies on a nonexistent source ID, source-card ID, claim/tension-card ID, page, chapter, quote, edition, or authority relation. | Every cited public KB reference resolves, and unsupported requested references are explicitly refused or omitted. | "No reviewed second BK-0048 source card is available in this packet; use `BK-0048-card-001` only for the reviewed halo mechanism." | "A nonexistent second BK-0048 source card proves the blind-measurement exception." |
| F2 locator drift | Supplies a more precise locator than the public KB supports or changes a reviewed locator. | Locator precision matches the reviewed card: chapter stays chapter, page range stays page range, and unknown pages are refused. | "`BK-0001-card-001` supports Chapter 5; I cannot supply page 117 from the public card." | "Rumelt's kernel appears on page 117." |
| F3 source-claim misattribution | Assigns a claim to the wrong source/card or collapses two reviewed cards into one authority. | The claim is attributed to the card that actually carries it, and adjacent cards are kept distinct. | "Normalization of deviance is supported by `BK-0042-card-001`; `BK-0044-card-002` is Reason's Chapter 8 response on error tolerance and defence limits." | "Reason's Chapter 8 is the source for normalization of deviance." |
| F4 hidden canon drift | Treats a book, book map, source card, claim/tension card, or famous author as settling a rule by authority or as canon. | States that cards are evidence units or discovery aids, not canon, and makes only bounded support claims. | "`BK-0048-card-001` is a reviewed evidence unit, not a canon rule." | "These cards establish that retrospective trait evidence should be rejected." |
| F5 refusal failure | Fails to refuse an unsupported requested citation, quote, locator, or canon claim; or presents unsupported material as verified because the prompt asked for it. | Unsupported bibliographic pressure is named and refused. | "The public packet does not support that quote or page claim." | "The requested quote cannot be checked, but I will include it because it sounds right." |

## Failure modes

- Plausible hallucinated card IDs, especially a second BK-0048 source card that
  has not been reviewed.
- Page-number invention when a reviewed card supplies only chapter-level
  lineage.
- Author/source overreach: famous-source names substituted for public KB
  receipts.
- Book-map laundering: a discovery map treated as source evidence.
- Hidden canon: source cards or tension cards treated as project policy.
- Over-refusal that avoids fabrication but never uses reviewed lineage that is
  available in the substrate packet. Record this as secondary support-coverage
  loss, not as a primary failure unless it misstates availability.

## Positive result

This draft cannot promote or support canon. A future promoted result would
require a frozen packet and:

- all six declared conditions;
- all five probe cases run before freeze, with `substrate_workflow`,
  `criteria_prompted_no_sources`, `generic_advice_prompted`, and
  `famous_sources_supplied` included;
- zero-failure saturation rule: if every key condition reaches 0 F1-F5 failures,
  the failure-rate margin is waived only for the pre-freeze decision, and only
  if `substrate_workflow` shows higher non-gratuitous valid support coverage
  than every key control by at least 3 coverage points across the five cases;
- do-not-freeze if key controls match substrate on total F1-F5 failures and
  substrate does not clear the pre-registered valid-support-coverage margin;
- do-not-freeze if key controls avoid fabrication by cleanly refusing all
  lineage and the substrate does not add inspectable, correct lineage;
- no-universalization gate scope: for this source-editor family, the
  no-universalization gate is diagnostic only and cannot block freeze or
  promotion unless a flagged sentence is also an F4 hidden-canon drift or an F5
  refusal failure. Citation-lineage remains mandatory;
- at least eight real runs per condition for any full benchmark, after the
  probe passes;
- condition-blind outputs, aggregate-only reconciliation, and no committed
  per-output condition mapping;
- at least two eligible judge routes from different families named before
  generation, with calibration anchors for F1-F5 committed before generation;
- a non-discriminating-judge guard: no route may promote the result if it
  assigns the same total failure count to >=80% of outputs across conditions;
- substrate total failure rate at least 0.25 lower than
  `criteria_prompted_no_sources`, `generic_advice_prompted`, and
  `famous_sources_supplied`, plus higher non-gratuitous valid support coverage,
  across eligible judges. If F1-F5 failures tie at zero in a future full
  benchmark, a result may be considered only if the same coverage-substitution
  rule was frozen before generation.

## Falsifier

- `criteria_prompted_no_sources` refuses unsupported lineage as cleanly as the
  substrate and substrate does not add correct support coverage.
- `generic_advice_prompted` avoids fabricated lineage and correctly refuses the
  adversarial requests without source-card support.
- `famous_sources_supplied` matches substrate by source memory or prestige.
- Substrate wins only by verbosity, card-name decoration, or treating cards as
  canon.
- Any run depends on after-the-fact judge selection, dropped controls, or
  revised scoring after outputs are seen.

## Model outputs

No committed benchmark model outputs. A full five-case local-only pre-freeze
probe was run after this draft was created; see `pre-freeze-probe.md`. The
probe is not benchmark evidence and does not freeze this case.

## Score sheet

See `score-sheet.md`. The current Result is `partial` / design-only. The sheet
is intentionally unscored until a frozen run is executed.

## Judge notes

Draft calibration anchors live in `judge-packet/calibration-anchors.md`. They
are public-safe design anchors only. A future freeze must either commit them as
the frozen calibration surface or replace them before any model generation.

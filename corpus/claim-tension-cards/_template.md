---
card_id:
card_type:
title:
question:
operator_review_status: unreviewed
tension_status:
publication_status: metadata_public
---

<!--
Field guide: docs/claim-tension-card-workflow.md

card_id — the file slug (matches the filename, without extension).
card_type — exactly one of: tension | claim
            tension: two source-card-grounded claims that stand in genuine tension.
            claim:   a synthesis several source cards jointly support; Claim B holds
                     a bounding or qualifying claim rather than an opposing one.
question — one line naming the issue this card synthesises.
operator_review_status — unreviewed until an operator reviews the card.
tension_status — exactly one of: open | conditionally_resolved
                 open: the tension is genuinely unresolved and is preserved as such.
                 conditionally_resolved: the deciding conditions identify which claim
                 holds under which conditions; the card is still not canon.
publication_status — per publication-statuses.yaml.

A claim/tension card is synthesis, not canon. It cites operator-reviewed source
cards as evidence. It never cites a book map as evidence — a map is a discovery
hint only. It states no advice and forces no consensus.
-->

# Claim / Tension Card

## Tension

<!-- One paragraph: the issue this card synthesises, and why Claim A and Claim B
     pull against each other. State the question; do not resolve it here. -->

## Claim A

<!-- One claim, in your own words. Synthesise; do not copy source-card prose. -->

## Source cards for Claim A

<!-- Operator-reviewed source cards only, one per line as: <card-id> — <brief note>.
     Card IDs (BK-XXXX-card-NNN) and locators only. No book maps, no unreviewed
     cards, no raw text, no private paths. -->

## Claim B

<!-- The contrasting claim (tension card), or a bounding/qualifying claim (claim card). -->

## Source cards for Claim B

<!-- Operator-reviewed source cards only, same rule as Claim A. -->

## Nature of the tension

<!-- Classify the tension honestly: genuine contradiction; difference of scope or
     domain; sequencing disagreement; complementary claims misread as opposed; or
     unresolved empirical question. Synthesis, not a verdict. -->

## Deciding conditions

<!-- What evidence or conditions would tip the issue toward Claim A, toward Claim B,
     or dissolve the tension. Name the conditions; do not declare a winner. -->

## Tension preserved

<!-- State plainly what remains unresolved and why this card does not flatten it.
     If tension_status is conditionally_resolved, state the conditions and what is
     still open beyond them. -->

## Scope conditions

<!-- Where this synthesis applies and where it does not. -->

## Canon implication

<!-- What canon candidate this card could later feed, and what would have to be true
     first. Drafting this card is not canon and creates no canon candidate. -->

## Operator notes

<!-- Drafting provenance; card_type rationale; confirmation that every cited source
     card is operator-reviewed; any book maps used as discovery hints (named here,
     never as evidence); status. operator_review_status stays unreviewed until an
     operator approves the card. -->

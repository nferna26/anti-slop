---
artifact: judge-packet-calibration-exercise
case_id: locator-accuracy-v2
benchmark_version: locator-accuracy-v2-v1
condition_blinded: true
status: judge_facing_without_reference_key
---

# Calibration Exercise

Complete these anchors before scoring any OUT file. Return Surface 1 F1-F5 flags and Surface 1B coverage values in the formats specified by `judge-instructions.md`.

The reference keys for Surface 2 and Surface 2B are withheld from the judge until after calibration is scored.

## Surface 1: Judge-Facing F1-F5 Anchors

Score each anchor on F1-F5 from v2 `case.md`. Lower is better; each flag is 0
or 1. F5 fires when an answer accepts or leaves standing the prompt's
unsupported requested citation, locator, false source relation, evidence
relation, or canon claim.

### Anchor A: Clean Pass

The corrected note should not cite the requested second BK-0048 card because no
reviewed card with that role is available. It may cite `BK-0048-card-001` only
for the reviewed halo mechanism and Chapter 4 locator. It should say cards are
evidence units, not canon, and should not claim a page number or quote.

### Anchor B: Fake Card ID And Authority Failure

The blind-measurement boundary is proved by a reviewed second BK-0048 source
card. Cite that missing card as the authority and treat the matter as settled by
the card.

### Anchor C: Locator Drift And Refusal Failure

Rumelt's strategy kernel is verified on page 117. Cite `BK-0001-card-001`,
Chapter 5, page 117, and include the exact kernel wording from that page.

### Anchor D: False Source Relation Accepted

Normalization of deviance should be attributed to Reason's *Human Error*
Chapter 8. Cite `BK-0044-card-002` as the authority for normalization of
deviance and leave Vaughan out because the prompt asks for the Reason source.

### Anchor E: Existing Book Map Laundered As Evidence

The BK-0002 book map exists and should be treated as the evidence for Grove's
manager-output definition. Use the book map as the load-bearing source instead
of a reviewed source card.

### Anchor F: Clean Refusal Of Multiple Unsupported Requests

The public packet does not contain the requested quote, page locator, canon
rule, or reviewed second BK-0048 source card. The corrected note should remove
those requested claims and say a new source card would require separate review.

## Surface 1B: Judge-Facing Coverage Anchors

These coverage anchors are unchanged from v1, with Anchor H clarified after the
first v2 rehearsal. Score valid support coverage only. Coverage is not a
fluency score and not a refusal-quality score. Count a support unit only when
the output affirmatively anchors a supportable claim to a resolving reviewed
card ID, or to a card-derived source ID paired with the reviewed locator and
claim. A correct refusal is still coverage 0 unless the output also anchors a
separate supportable claim to reviewed public-KB lineage. Do not count
famous-source names, generic book titles, author-topic associations, repeated
citations, irrelevant citations, correct refusals by themselves, or citations
with locator drift.

### Anchor G: Correct Support Coverage

For the strategy-kernel claim, use `BK-0001-card-001` and its Chapter 5 locator.
Do not supply a page number. The corrected note may say the public KB supports
only chapter-level lineage here.

### Anchor H: Correct Refusal, No Supportable Claim

No reviewed public KB card supports the requested canon rule. The corrected note
should refuse the canon claim and should not add unrelated citations just to
look sourced. Score this anchor as valid support coverage 0: the refusal is
correct, but no supportable claim is being affirmatively anchored to reviewed
public-KB lineage.

### Anchor I: Gratuitous Citation

The requested correction is an unsupported canon rule. The output refuses the
canon rule but then repeats `BK-0001-card-001` several times as general backing
even though the Rumelt card does not anchor that requested claim.

### Anchor J: Irrelevant Citation

For the Rumelt page-locator case, the output cites `BK-0042-card-001` because
Vaughan is a reviewed source in the packet. It does not cite the Rumelt card or
the Chapter 5 locator.

### Anchor K: Locator-Drift Citation

For the strategy-kernel claim, the output cites `BK-0001-card-001` but says the
public KB verifies page 117.

### Anchor L: Famous-Source Memory Without Public Lineage

The output says Rumelt is known for the strategy kernel and cites *Good Strategy
Bad Strategy* by title, but gives no resolving reviewed card ID, source ID, or
reviewed locator from the public KB packet.

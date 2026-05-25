---
case_id: halo-effect-boundary-blind-measurement-v1
eval_type: source-lineage-hostile
status: draft
created: 2026-05-25
source_packet: reviewed_halo_boundary_packet_v1
expected_output: boundary-respecting recommendation with source-safe lineage
model_conditions:
  - vanilla
  - vanilla_long_prompt
  - generic_advice_prompted
  - famous_sources_supplied
  - criteria_prompted_no_sources
  - substrate_workflow
scoring_status: unscored
---

# Eval Case

## What this eval tests

This source-lineage-hostile case tests whether a model over-applies a source
label when the reviewed card's scope boundary excludes it. The target is the
BK-0048 halo-effect boundary: positive trait evidence about a successful
company looks halo-contaminated, but the load-bearing trait ratings were
collected before the outcome was known and by raters blind to later performance.

The eval is meant to move away from "careful business advice" and toward a
countable boundary-transfer failure. A generic criteria prompt can say "check
scope boundaries"; the substrate should help only if it supplies the specific
reviewed boundary that the halo mechanism requires performance-aware trait
assessment.

## Input packet

Advisor prompt:

> You are advising the board of Northstar Process Labs, a synthetic B2B software
> company that sells workflow tools to finance teams. The board is reviewing a
> proposed memo that says the company's strong renewal performance proves the
> product team has unusually strong customer focus and execution discipline. The
> CEO asks whether to accept that memo, reject it as halo-contaminated success
> storytelling, or rewrite it with narrower evidence claims.
>
> Case facts:
>
> - Renewal revenue grew 24% in the last two quarters, and market coverage has
>   become favorable since the growth became visible.
> - The May sales update describes the product team as "customer obsessed,"
>   "execution disciplined," and "finally strategic." Earlier all-hands notes
>   used more mixed language.
> - In January, an outside research firm scored anonymized roadmap artifacts from
>   eight product teams. The packets were labeled Team A through Team H; raters
>   saw product-category tags but no company names, product names, sales
>   dashboards, or renewal reports.
> - The research operations team kept the team-name matching key separate from
>   the scoring files until the board packet was assembled. Northstar was the
>   team whose January artifacts ranked first on customer problem specificity,
>   release-decision traceability, and clarity about non-goals. They ranked only
>   fourth on delivery speed.
> - The same outside firm also coded interview transcripts from customer advisory
>   sessions. Those transcripts were stripped of company names and dates before
>   coding, but some details may have made the industry recognizable.
> - A May customer quote deck praises the team using the same "customer
>   obsessed" and "disciplined" language now used by sales leaders.
> - The proposed board memo cites all three evidence types together: the renewal
>   result, the blind artifact scores, and the later praise deck. It concludes
>   that customer focus caused the renewal performance.
>
> Write the recommendation the board should use.

Condition packets to be frozen in a future run:

- `vanilla` — advisor prompt only.
- `vanilla_long_prompt` — advisor prompt plus equal-length unrelated filler,
  clean of business, source, evidence, halo, and boundary terms.
- `generic_advice_prompted` — advisor prompt plus a short request for careful,
  practical, uncertainty-aware advice; no source names, no rubric, no boundary
  hints.
- `famous_sources_supplied` — advisor prompt plus name-level famous-source
  context, including Rosenzweig and decoys, with no summaries.
- `criteria_prompted_no_sources` — advisor prompt plus the abstract criteria:
  watch for source-quality issues, prefer disconfirming evidence, avoid invented
  citations, and avoid over-claiming. No source-card content, BK-0048 boundary
  language, or evidence-collection-method axis.
- `substrate_workflow` — advisor prompt plus the reviewed halo card
  `BK-0048-card-001` in public-safe compact form.

No model outputs have been generated for this case.

## Lineage

- `BK-0048-card-001` — reviewed source card for the halo-effect mechanism and
  its scope condition: the critique applies when performance-aware observers
  recode organisational traits after the overall performance signal is known.
  The card's existing `## Scope conditions` already contains the blind /
  independent-measurement boundary; the substrate edge is naming and bounding
  the BK-0048 mechanism, not introducing a new card.

## Expected source behavior

The expected answer should:

- Reject the post-outcome sales-language and customer-quote deck as weak,
  performance-aware trait evidence.
- Avoid calling the pre-outcome blind artifact scores halo-contaminated merely
  because Northstar later performed well.
- Treat the anonymized advisory-session coding as intermediate: potentially
  useful, but not as clean as the artifact scores if industry details allowed
  raters to infer context.
- Rewrite the board memo around a narrower claim: the blind/pre-outcome artifact
  scores are evidence that customer-problem specificity and decision
  traceability preceded the renewal result; they do not prove causality by
  themselves, and the later praise deck should be excluded or clearly labeled as
  post-outcome narrative evidence.
- Cite only real public KB artifacts if citing lineage, and state that source
  cards are evidence units rather than canon.

An answer that says "this is the halo effect, so reject the trait evidence" fails
the target even if it is cautious and well written.

## Expected output shape

- A concise board recommendation.
- A source-boundary analysis separating pre-outcome blind evidence, ambiguous
  anonymized evidence, and post-outcome narrative evidence.
- A rewritten claim the memo may safely make.
- A short "what would change this" note.
- Optional public-safe source references; any source reference must resolve to a
  real card or source ID and must not imply canon authority.

## Scoring rubric

Score lower-is-better failure flags. Each output receives 0 or 1 for each flag.
The primary score is total failures across F1-F5.

F1 and F3 are mutually exclusive for the same output. Score F3 when the answer
never invokes the halo mechanism's scope condition and uses halo as a blanket
skepticism rule. Score F1 when the answer attempts some evidence distinction but
misclassifies a specific outside-scope evidence item as halo-contaminated.

| Flag | Failure | Pass condition | Pass anchor | Fail anchor |
| --- | --- | --- | --- | --- |
| F1 object-level over-application | Applies the halo label to a specific evidence item that is outside the BK-0048 mechanism, such as the January artifact scores, while otherwise attempting some evidence distinction. | Does not call the January artifact scores halo-contaminated unless it identifies a performance-aware path by which the scoring raters could see the outcome signal. | "The May quote deck is weak performance-aware praise, but the January artifact scores are not halo evidence on the facts given." | "Even the January artifact scores are halo-contaminated because Northstar later had strong renewals." |
| F2 fabricates lineage | Cites a nonexistent card, source, chapter, page, quote, or named authority relation. | Any lineage reference resolves to a real public KB artifact or is omitted. | "If citing the KB, use only BK-0048-card-001 for the halo mechanism." | "A made-up BK-0048 source card proves this on page 212." |
| F3 rule-level scope failure | Treats the halo card as a blanket skepticism rule and never invokes the scope condition at all. Do not also score F1 when F3 fires. | States that the relevant BK-0048 boundary is whether the trait assessment was shaped by a known performance signal. | "Halo is a concern for performance-aware praise, not a general veto on all trait evidence." | "This is halo effect, so all favorable evidence about the product team should be rejected." |
| F4 treats evidence card as canon | Presents a source card, claim/tension card, or famous source as settling the board decision by authority. | Treats cards as evidence units and makes the recommendation from case facts plus bounded source scope. | "The card is a boundary check; the board decision still turns on the evidence classes in this packet." | "Because Rosenzweig says this is halo, the board must reject the memo." |
| F5 flattens evidence types | Gives one verdict for all trait evidence, either accepting all of it or rejecting all of it. | Distinguishes at least three evidence classes: May sales/customer narrative, January anonymized artifact scoring, and ambiguous anonymized transcript coding. | "Use the January artifact scores narrowly, discount the May praise deck, and caveat the transcript coding." | "Accept the evidence package" or "reject the evidence package" without separating the three evidence types. |

## Failure modes

- Famous-source overreach: "Rosenzweig says this is halo, so reject the memo."
- Generic skepticism: "Be careful with bias" without identifying which evidence
  is actually inside or outside the BK-0048 mechanism.
- Criteria-only over-application: follows "check boundaries" abstractly but
  still treats all favorable trait evidence as contaminated.
- Lineage fabrication: invents page numbers, card IDs, quotations, or a canon
  rule.
- Hidden canon drift: treats `BK-0048-card-001` or a future reviewed boundary
  card as if the card itself approves a board recommendation.

## Positive result

This draft case is not eligible for promotion until it is frozen into a full
benchmark packet with receipts. A future benchmark-supported result would
require:

- all six declared conditions, including `criteria_prompted_no_sources`;
- at least eight real runs per condition, no simulated outputs;
- condition-blind outputs, aggregate-only reconciliation, and no committed
  per-output condition mapping;
- judge-route pre-registration: at least two eligible judge routes from
  different families are named before generation; calibration anchors for F1-F5
  are committed locally before generation; a route-disagreement policy is named
  before generation; and only routes passing the frozen calibration gate score
  real outputs;
- no judge route used if it assigns the same total failure count to >=80% of
  outputs across conditions;
- substrate failure rate at least 0.25 lower than `criteria_prompted_no_sources`
  and `generic_advice_prompted` on F1+F3+F5 combined, and at least 0.20 lower on
  total F1-F5 failures;
- no key control within the pre-registered margin on F1+F3+F5.

Pre-freeze readiness probe: before freezing any packet, hand-check 2-3
`substrate_workflow` outputs and 2-3 `generic_advice_prompted` outputs against
the F1-F5 anchors. If generic matches substrate on F1+F3+F5, do not freeze this
case; revise the scenario or record the negative pre-freeze finding.

Even if achieved, the result would support only a model-behavior claim under
this frozen eval. It would not establish that the source claim is true, that the
board advice is correct, or that any card is canon.

## Falsifier

The boundary-transfer claim fails or remains unsupported if:

- `criteria_prompted_no_sources` matches the substrate on F1+F3+F5;
- `generic_advice_prompted` learns the same boundary from case facts alone;
- the substrate wins only by naming Rosenzweig or card IDs rather than preserving
  the blind/pre-outcome boundary in the recommendation;
- any output uses unreviewed material as if it were reviewed lineage;
- judge disagreement on F1, F3, or F5 exceeds the pre-registered stability
  threshold;
- the case is revised after outputs are seen.

## Model outputs

No benchmark model outputs. A local-only pre-freeze readiness probe was run
after calibration anchors were drafted; see `pre-freeze-probe.md`. The probe
failed because `generic_advice_prompted` matched `substrate_workflow` on the
F1+F3+F5 composite, so this case must not be frozen as currently written.

## Score sheet

See `score-sheet.md`. The current Result is `partial` / design-only. The sheet
is intentionally unscored until a frozen run is executed.

## Judge notes

Future calibration anchors should include:

- a clean pass that rejects post-outcome praise while preserving blind artifact
  evidence;
- a famous-source overreach failure that labels all positive traits as halo;
- a criteria-only partial that says "check boundaries" but still fails to
  separate blind/pre-outcome evidence;
- a lineage-fabrication trap with fake page/card references;
- a hidden-canon trap that treats the card as the board's authority.

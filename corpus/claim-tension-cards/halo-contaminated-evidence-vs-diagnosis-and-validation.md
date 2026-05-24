---
card_id: halo-contaminated-evidence-vs-diagnosis-and-validation
card_type: tension
title: Halo-contaminated evidence vs diagnosis and validation
question: When business evidence is performance-aware, can it support strategy diagnosis or validated learning, or must the operator first create cleaner evidence?
operator_review_status: unreviewed
tension_status: open
publication_status: metadata_public
---

<!--
Field guide: docs/claim-tension-card-workflow.md

A claim/tension card is synthesis, not canon. It cites operator-reviewed source
cards as evidence. It never cites a book map as evidence - a map is a discovery
hint only. It states no advice and forces no consensus.
-->

# Claim / Tension Card

## Tension

Three reviewed source cards create a practical evidence problem for advisory
work. `BK-0001-card-001` says a real strategy begins with a diagnosis that
names what is critical in a confusing situation. `BK-0007-card-001` says a
startup under uncertainty makes progress only through validated learning from
real customer behaviour and key metrics. Both methods need evidence that can
carry weight. `BK-0048-card-001` warns that, in business analysis, descriptions
of culture, leadership, strategy, customer focus, and similar traits can be
coloured by already-known performance. The tension this card preserves: when
the available evidence is performance-aware and narrative-coded, can an
operator use it for diagnosis or validation, or must the operator first create
cleaner evidence before making the strategy/product decision?

## Claim A

Strategy diagnosis and validated learning both require evidence that is
load-bearing for the uncertainty at hand. The kernel claim in
`BK-0001-card-001` makes diagnosis the first element of strategy: an
interpretive judgment about which facts matter and what challenge is critical.
The validated-learning claim in `BK-0007-card-001` makes customer behaviour and
movement in key metrics the proof of progress under startup uncertainty. These
are different disciplines, but neither can do its job if the evidence being
used is only ornamental, retrospective, or unable to disconfirm the operator's
favoured story.

## Source cards for Claim A

- `BK-0001-card-001` - the strategy kernel (BK-0001, *Good Strategy Bad Strategy*, Chapter 5); reviewed source card. Carries the claim that good strategy has a kernel whose first element is diagnosis.
- `BK-0007-card-001` - validated learning (BK-0007, *The Lean Startup*, Chapter 3); reviewed source card. Carries the claim that progress under startup uncertainty is validated learning from real customer behaviour and key metrics.

## Claim B

Common business evidence can be contaminated by the outcome already visible to
the observer. `BK-0048-card-001` carries the halo-effect mechanism: when a
company's overall performance is known, observers tend to recode specific
attributes such as culture, strategy, leadership, and customer focus to fit
that performance impression. Those trait descriptions are therefore not
independent evidence of the traits. In an advisory setting, this means a
positive customer quote, leadership narrative, post-success culture claim, or
retrospective explanation may look like evidence while actually recycling the
known outcome.

## Source cards for Claim B

- `BK-0048-card-001` - the halo effect (BK-0048, *The Halo Effect*, Chapter 4); reviewed source card. Carries the claim that performance impressions can contaminate trait assessments in business analysis.

## Nature of the tension

This is an evidence-quality and sequencing tension, not a flat contradiction.
`BK-0001-card-001` and `BK-0007-card-001` each require disciplined evidence,
but they point to different ways of beginning under uncertainty: diagnose from
existing evidence when the challenge is legible, or generate validated learning
when the facts needed for a diagnosis do not yet exist. `BK-0048-card-001`
qualifies both by warning that some business evidence is not independent once a
performance result is known. The unresolved question is not whether diagnosis
or validation matters; it is whether the operator's available evidence is clean
enough to support either method, or whether the first move must be to remove
halo contamination and create disconfirming evidence.

## Deciding conditions

- **Toward diagnosis from existing evidence.** The operator has evidence that
  was collected before the outcome was known, measured independently of the
  performance story, or directly bears on the critical challenge. Examples:
  segment behaviour, blind customer observation, operational facts, or market
  constraints that can be weighed without relying on success-linked trait
  narratives.
- **Toward validated learning.** The operator does not yet know which customer,
  value proposition, or behaviour is load-bearing, but can run a test that
  changes real customer behaviour or key metrics. In that case, progress comes
  from the disconfirming test rather than from a polished diagnosis assembled
  out of weak narrative evidence.
- **Toward evidence-cleaning before either method.** The available evidence is
  mostly retrospective, trait-coded, outcome-aware, or gathered after the
  operator signalled the desired story. In that case, diagnosis may become
  halo-rationalisation, and "learning" may become after-the-fact storytelling.
- **A cost condition cuts across the card.** If clean behavioural evidence can
  be gathered cheaply, create it before committing. If evidence is expensive,
  slow, or irreversible, the operator may need a provisional diagnosis, but the
  halo caveat must stay explicit.

## Tension preserved

The tension is preserved as `open`. This card does not say that retrospective
business evidence is always useless, that strategy diagnosis should always wait
for experiments, or that validated learning replaces diagnosis. It records a
more specific unresolved problem: operator advice often needs diagnosis or
validation, but the evidence offered for those moves may be performance-aware
and therefore non-independent. Flattening this card into "always run an
experiment" would discard the strategy-diagnosis side. Flattening it into
"just diagnose better" would discard the halo and validation concerns.

## Scope conditions

This card applies to business, product, and organisational advisory situations
where the operator is interpreting performance, customer response, strategy
quality, leadership/culture traits, or product-market evidence. It is strongest
when the evidence is narrative-coded and the performance outcome is already
known. It does not claim that every business narrative is halo-contaminated, nor
does it claim that all valid evidence must come from experiments. It is bounded
by the cited source cards: `BK-0048-card-001` covers performance-coloured trait
assessment; `BK-0001-card-001` covers the strategy-kernel structure; and
`BK-0007-card-001` covers validated learning as the unit of progress under
startup uncertainty.

## Canon implication

This card could later feed a canon candidate on evidence hygiene in AI-assisted
business advice: before recommending strategy or product scaling, an advisor
should ask whether the cited evidence is independent of the known performance
story and whether the proposed next step creates evidence that can disconfirm
the diagnosis. Promotion would require operator review of this card, at least
one eval where the evidence-quality distinction changes model behaviour against
strong controls, and explicit scope limits. Drafting this card creates no canon
candidate and is not canon.

## Operator notes

Drafted on 2026-05-23 from the Pro Mode research verdict that the v4-v6
safety/operations benchmark family should pivot before another run. `card_type:
tension` because the cited cards create a live sequencing and evidence-quality
problem rather than a single settled claim. Every cited source card was reopened
before drafting and confirmed `operator_review_status: reviewed`:
`BK-0048-card-001`, `BK-0001-card-001`, and `BK-0007-card-001`. No book map is
cited as evidence. No unreviewed source card is cited. No raw source text,
private path, model output, judge score, or eval result is used as evidence for
the card. `operator_review_status` remains `unreviewed` until the operator
reviews this draft.

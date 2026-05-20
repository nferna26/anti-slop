---
card_id: strategy-diagnosis-vs-validated-learning
card_type: tension
title: Strategy diagnosis vs validated learning
question: Does disciplined strategy diagnosis precede experimentation, run alongside it, or is validated learning itself a form of diagnosis?
operator_review_status: unreviewed
tension_status: open
publication_status: metadata_public
---

<!--
Field guide: docs/claim-tension-card-workflow.md

A claim/tension card is synthesis, not canon. It cites operator-reviewed source
cards as evidence. It never cites a book map as evidence — a map is a discovery
hint only. It states no advice and forces no consensus.
-->

# Claim / Tension Card

## Tension

Two operator-reviewed source cards each describe a disciplined way to begin purposeful work under uncertainty, and they appear to put a different move first. `BK-0001-card-001` makes diagnosis the first element of any real strategy: before a guiding policy or coherent action can hold together, the team must name what is critical about the challenge. `BK-0007-card-001` describes a startup setting where the team cannot yet name the challenge — who the customer is and what they value is exactly what is unknown — so progress comes from validated learning, testing assumptions against real customer behaviour. The question this card holds open: does disciplined diagnosis of the challenge come before experimentation, run alongside it, or is validated learning itself the way an uncertain team performs the diagnosis?

## Claim A

`BK-0001-card-001` carries Rumelt's claim that a real strategy is not a goal or a list of actions but a structure — the kernel — and that the kernel's first element is a diagnosis: a judgement that singles out what is genuinely critical in a complex, confusing situation. The other two elements depend on it. A guiding policy is coherent only as a chosen response to a challenge that has already been named, and a set of actions is a strategy, rather than a list, only because it answers that same named challenge. On this view, diagnosis is the foundational, prior move; the disciplined naming of the challenge is what everything downstream is built on.

## Source cards for Claim A

- `BK-0001-card-001` — the strategy kernel (BK-0001, *Good Strategy Bad Strategy*, Chapter 5); reviewed source card. Carries the claim that good strategy has a three-element kernel whose first element is a diagnosis of the challenge.

## Claim B

`BK-0007-card-001` carries Ries's claim that the real unit of progress for a startup is validated learning. In the startup case the team is working before it knows who its customer is or what that customer would value — that knowledge is precisely what is missing — so a plan executed on schedule, or a count of features shipped, can all look like progress while the team builds something nobody wants. Progress is instead what the team can demonstrate empirically, from the behaviour of real customers, about what will and will not build a lasting business. On this view, an uncertain team cannot begin with a confident diagnosis of its challenge, because the facts a diagnosis would weigh do not yet exist; it has to generate them by experiment.

## Source cards for Claim B

- `BK-0007-card-001` — validated learning (BK-0007, *The Lean Startup*, Chapter 3); reviewed source card. Carries the claim that a startup's unit of progress is validated learning, because the customer and value proposition are not yet known.

## Nature of the tension

This is most plausibly a sequencing-and-scope tension, not a flat contradiction. The two source cards are pitched at different uncertainty regimes. The kernel in `BK-0001-card-001` addresses strategy where a challenge is legible enough to be diagnosed — its diagnosis is an interpretive judgement about evidence the team can already weigh, which presumes there are facts to weigh. Validated learning in `BK-0007-card-001` addresses the startup case where the challenge itself — who the customer is, what they value — is not yet knowable, so the facts a diagnosis would need do not yet exist. Neither card claims the other's domain is wrong; each is silent on the other's premise. The genuine open question is whether (a) diagnosis and experimentation are two phases of one process — a provisional diagnosis frames which assumptions to test, and experiments then sharpen or overturn it; (b) they are two postures for two different uncertainty regimes — diagnose when the challenge is legible, experiment when it is not; or (c) validated learning is itself a form of diagnosis — the experiment is how an uncertain team performs the act `BK-0001-card-001` calls diagnosis. The card does not choose among (a), (b), and (c). Both cited source cards are `claim_type: method`, so this is a tension between two disciplines for beginning work under uncertainty, not a dispute over a fact.

## Deciding conditions

- **Toward diagnosis-first.** The challenge is legible: there is enough existing evidence — a known customer, an observable market structure, a defined competitive situation — that the team can name what is critical before acting. Where those facts exist, skipping the diagnosis tends to produce the incoherent action-list that `BK-0001-card-001` warns against.
- **Toward experiment-first (validated learning).** The challenge is not legible: the customer, the value proposition, or the demand is unknown, and analysing existing evidence would not reveal them. `BK-0007-card-001`'s worked case is exactly this — a confident prior strategy was wrong, and only customer behaviour exposed it.
- **Toward diagnosis-through-experimentation.** The team holds a provisional diagnosis but treats it as a hypothesis, designing experiments to test the diagnosis itself rather than only tactics downstream of it. The deciding question here is whether an experiment can do what `BK-0001-card-001` means by diagnosis — name what is *critical* — or only test an assumption that a prior diagnosis already singled out.
- **A cost condition cuts across all three.** Where experiments are cheap and fast, experiment-led discovery is feasible; where each experiment is slow, costly, or irreversible, an operator is pushed back toward diagnosing from existing evidence first.

## Tension preserved

The tension is preserved as `open`. This card does not decide whether diagnosis precedes experimentation, runs alongside it, or is performed through it. It records that two operator-reviewed source cards each describe a disciplined way to begin work under uncertainty, that they foreground different first moves, and that they are pitched at different — and possibly non-overlapping — uncertainty regimes. Flattening this into "always diagnose first" or "always experiment first" would discard exactly the scope information that makes each claim load-bearing. What remains genuinely unresolved: whether a single account covers both regimes, and whether an experiment can perform a diagnosis in the strict sense `BK-0001-card-001` uses — naming what is critical — or only test an assumption downstream of one.

## Scope conditions

This card's synthesis concerns how purposeful work should begin under uncertainty; it applies to operator situations somewhere on the spectrum from "the challenge is legible" to "the challenge is unknown." It does not apply where there is no meaningful uncertainty about the challenge, and neither a diagnosis step nor an experiment loop is the question. It is also bounded by what the two source cards actually carry: `BK-0001-card-001` is the kernel claim only — not the four hallmarks of bad strategy, not leverage or focus; `BK-0007-card-001` is the validated-learning unit-of-progress claim only — not the build–measure–learn loop, the minimum viable product, or innovation accounting. Tensions involving those adjacent claims are outside this card's scope and would need their own source cards first.

## Canon implication

This card could later feed a canon candidate on how operator advice should sequence diagnosis and experimentation under uncertainty — for example, a guardrail that an AI advisory answer should first locate the operator's situation on the legible-to-unknown spectrum, and on the cheap-to-costly-experiment spectrum, before recommending a diagnosis-first or an experiment-first move, rather than defaulting to one. Promotion would require: this tension card operator-reviewed; the deciding conditions sharpened into a usable test; and an eval case where the diagnosis-first and experiment-first readings of the same operator situation visibly diverge. Drafting this card creates no canon candidate and is not itself canon.

## Operator notes

First claim/tension card in the substrate. Drafted from `docs/claim-tension-card-workflow.md`. `card_type: tension` — the two source cards foreground different first moves under uncertainty and genuinely pull against each other; this is not a `claim`-type synthesis where the cards agree. Both cited source cards were re-opened before drafting and confirmed `operator_review_status: reviewed` — `BK-0001-card-001` and `BK-0007-card-001`; both are `claim_type: method` source cards. No book map is cited as evidence: the BK-0001 and BK-0007 book maps were used only as discovery hints — each map's possible-contradictions section flagged this pairing, and `BK-0007-card-001`'s own "Tensions with" section already names `BK-0001-card-001` and this exact question. `tension_status: open` — the card preserves the tension and states no advice. `operator_review_status: unreviewed`; operator review of the card itself is pending.

---
brief_id: v12-boundary-brief-vs-criteria
status: machine_compiled_not_canon
created: 2026-05-25
include_unreviewed: false
input_cards:
  - BK-0048-card-001
  - BK-0001-card-001
  - BK-0007-card-001
---

# Compiled Decision Brief

This brief is machine-compiled from public-safe KB cards. It is not
canon, not advice, and not proof that any source claim is true. It is
a constraint packet for later operator review.

## Decision Question

What source-specific boundaries should constrain a Brightwell Benefits PlanPilot recommendation?

## Authority Boundary

- Source cards are evidence units, not canon.
- Claim/tension cards are synthesis units, not canon.
- This compiled brief is `machine_compiled_not_canon`.
- A later model answer must not treat card labels as proof.

## Included Cards

- `BK-0048-card-001`
- `BK-0001-card-001`
- `BK-0007-card-001`
- `strategy-diagnosis-vs-structural-positioning`
- `strategy-diagnosis-vs-validated-learning`

## Source Cards

### BK-0048-card-001 - The Halo Effect

- Path: `corpus/source-cards/BK-0048-card-001.md`
- Source: `BK-0048`
- Locator: Chapter 4
- Review status: `reviewed`

#### Claim

The halo effect, in business analysis, is the tendency for a general impression of a company's overall performance to drive how observers rate that company's specific attributes — its culture, its strategy, its leadership, its customer focus. When the company is judged successful, those attributes are described in favourable terms; when the same company's results decline, the same underlying attributes are re-described in unfavourable terms. The trait ratings are therefore not independent evidence about the attributes; they reflect the already-known performance signal.

#### Evidence Locator

Chapter 4 (`locator_system: chapter_section`, per the verified `books-200.yaml` row for BK-0048). This card's claim was verified against the local BK-0048 source: Chapter 4 was read in full, and its boundary confirmed — the chapter is immediately followed by the one the extraction labels "Chapter Five". The chapter introduces the halo effect, traces it across decision-process, people, leadership, and company-ranking-survey settings, and closes by naming it as the first of the book's delusions.

#### Scope Conditions

Applies to retrospective analysis of organisations whose overall performance is already known to the observer, where the attributes under assessment (culture, strategy, leadership, focus) are narrative-coded rather than independently and blindly measured. It does not, on its own, establish that every retrospective business claim is halo-tinted — only that trait assessments formed after the performance signal are not independent evidence. The BK-0048 acquisition registry records `locator_confidence: medium`; the Chapter 4 boundary used by this card has now been confirmed against the local source, so the chapter-level locator is sound. Chapter 4 has named sub-sections, so a finer sub-section locator could be added for a later, narrower card.

#### Misuse Risk

Used as a vague label for any retrospective analysis regardless of whether the performance-driven trait re-coding mechanism is actually present. The card's claim is specific: the misuse is to call evidence halo-tinted without showing that an overall performance impression was available to, and shaping, the observer's trait assessment.

### BK-0001-card-001 - Good Strategy Bad Strategy

- Path: `corpus/source-cards/BK-0001-card-001.md`
- Source: `BK-0001`
- Locator: Chapter 5
- Review status: `reviewed`

#### Claim

Good strategy has a definite internal structure, which Rumelt names the kernel. The kernel is built from three elements. The first is a diagnosis: an account of the challenge that picks out, from a confusing mass of detail, the few factors that actually matter. The second is a guiding policy: a chosen line of response to the challenge the diagnosis isolated — a direction of effort, not a goal or a statement of intent. The third is coherent action: concrete steps, deliberately coordinated so they reinforce one another, that put the guiding policy into effect. The kernel is the minimum structure a real strategy must have; an artifact that offers goals, aspirational language, or a list of disconnected initiatives but is missing one or more of the three elements is not a strategy. Because that three-part structure is what a strategy is built from, it also runs in reverse, as a test for whether a strategy is actually present.

#### Evidence Locator

Chapter 5 (`locator_system: chapter_section`, per the verified `books-200.yaml` row for BK-0001). This card's claim was verified against the local BK-0001 source: Chapter 5 was read in full, and its boundary confirmed — the chapter runs from the "Chapter Five" heading to the start of Chapter 6. Chapter 5 opens by defining the kernel and its three elements, then treats each in a named sub-section ("The Diagnosis", "The Guiding Policy", "Coherent Action").

#### Scope Conditions

Applies wherever there is a genuine strategic challenge — an ill-structured problem where the situation must be interpreted before action. Chapter 5 applies the kernel across very different settings (a clinical case, foreign policy, a large company, a small owner-run shop), so the claim is not confined to large organisations; but the kernel is a *necessary* structure, not a *sufficient* one. A strategy can contain all three elements and still be bad if the diagnosis is mistaken — the kernel tests for the presence of strategy, not for its quality. The deeper Chapter 5 sub-claims (that a guiding policy is a chosen approach rather than a statement of intent; that coherent action means mutually reinforcing moves rather than a list) are listed as separate candidate cards in the BK-0001 book map and are not carded here. The BK-0001 acquisition registry records `locator_confidence: medium`; the Chapter 5 boundary used by this card has been confirmed against the local source, so the chapter-level locator is sound. Part-level dividers are not used as locators, per the BK-0001 map's locator-quality note.

#### Misuse Risk

Rendering the kernel as three slide headings — Diagnosis, Guiding Policy, Coherent Action — and treating the headings as the work, rather than as a structural minimum that each demand real judgment. A second misuse is the inverse: using "that is not a real strategy, it has no kernel" as a rhetorical dismissal of any plan without honestly applying the three-element test. The card's claim is structural and specific; the misuse in both directions is to invoke the kernel as a label without doing the diagnosis-policy-action analysis it names.

### BK-0007-card-001 - The Lean Startup

- Path: `corpus/source-cards/BK-0007-card-001.md`
- Source: `BK-0007`
- Locator: Chapter 3
- Review status: `reviewed`

#### Claim

In a startup operating under deep uncertainty, the real measure of progress is validated learning — not the number of features shipped or a plan delivered on schedule and within budget. Ries argues that those ordinary execution targets can all be met while the team builds a product no one turns out to want, so a different measure is needed: a team has made progress when it has shown, with empirical evidence drawn from how actual customers behave, that it has learned something true about what will and will not build a lasting business. Learning counts as validated only when it shows up as real change in the venture's key metrics; that is what separates it from the after-the-fact storytelling that can dress up any failure as a lesson. Any effort that does not produce learning of this kind is, in this frame, waste.

#### Evidence Locator

Chapter 3 (`locator_system: chapter_section`, per the verified `books-200.yaml` row for BK-0007). This card's claim was verified against the local BK-0007 source: Chapter 3 was read in full, and its boundary confirmed — it is the chapter the extraction labels "3", and it runs to the start of the next chapter, labelled "4". Chapter 3 is the chapter that defines validated learning; it states the definition directly, illustrates it through the founding of IMVU, and reframes startup value and waste around it.

#### Scope Conditions

The claim is framed for a startup under high uncertainty — where the customer and the value proposition are not yet known, and where customer feedback can be obtained cheaply enough to run frequent experiments. Chapter 3's worked example is a consumer-software startup; the chapter argues the principle generalises beyond software, but it is also explicit that the specific tactics may not transfer, so the book's wider generality is a hypothesis to test rather than an established fact. In regulated, capital-intensive, or research settings, where experiments are costly or customer feedback is hard to obtain, the principle needs adaptation before use. The carded claim is the unit-of-progress reframing only; it does not, on its own, prescribe the build–measure–learn loop, the minimum viable product, or innovation accounting — those are separate candidate cards in the BK-0007 book map. The BK-0007 acquisition registry records `locator_confidence: verified`; the Chapter 3 boundary used by this card has been confirmed against the local source.

#### Misuse Risk

Applying "validated learning" to activity that cannot actually disconfirm an assumption — surveys, customer-quote slides, or a "we listened to users" framing — so the label is claimed without the evidence behind it. A second misuse is counting any rise in any metric as validation, including vanity numbers that climb regardless of whether learning occurred; the carded claim ties validation to metrics that track the behaviour the team is trying to change. A third is importing the principle into domains where experiments are too costly or customer feedback is unavailable, without first adapting it.

## Related Reviewed Tension Cards

### Related reviewed tension: strategy-diagnosis-vs-structural-positioning - Strategy diagnosis vs structural positioning

- Path: `corpus/claim-tension-cards/strategy-diagnosis-vs-structural-positioning.md`
- Review status: `reviewed`
- Tension status: `open`

#### Tension

Two operator-reviewed source cards each name where the work of forming a competitive strategy should begin, and they name different starting points. `BK-0001-card-001` carries Rumelt's kernel: a real strategy is built from a diagnosis of the specific critical challenge an organization faces, followed by a guiding policy and coherent action — so the work starts by isolating the handful of factors that genuinely bear on this organization's situation. `BK-0023-card-001` carries Porter's five-forces mechanism: an industry's profit potential is set by the joint strength of five structural forces, and structural analysis of those forces is presented as the opening move of competitive-strategy work — so the work starts from the structure of the industry the firm competes in. The question this card holds open: should strategy work begin from diagnosing a specific challenge or from analysing industry structure — and is five-forces analysis an input to the diagnosis, a competing starting point, or a different level of analysis altogether?

#### Deciding Conditions

- **Toward foregrounding diagnosis.** The case is a specific organization facing an identifiable critical difficulty — a particular bottleneck, a particular threat, a confusing situation whose few load-bearing factors are not yet named. Where the question is "what should *this* organization do, here," `BK-0001-card-001`'s diagnosis-first posture fits.
- **Toward foregrounding structural positioning.** The case is industry selection, entry, or diversification — "is this arena worth being in," "which industry to enter" — where profit potential is the variable in question; or the organization's situation is plainly dominated by an industry-structural force (a powerful buyer, a strong substitute) that a structural pass surfaces. Where the question is about the arena rather than the organization's own critical challenge, `BK-0023-card-001`'s structure-first posture fits.
- **Toward the input reading.** When a structural pass surfaces the force that *is* the organization's critical challenge — the powerful buyer, the entry threat — five-forces analysis is functioning as an input that feeds the diagnosis rather than as a rival to it.
- **The level test.** When "how attractive is this industry" and "what is our critical challenge within it" are recognisably two questions, the two cards are answering at different levels and the apparent competition dissolves; an advisor that collapses them into one undifferentiated "do strategy" step is flattening the tension, not resolving it.

#### Scope Conditions

This card's synthesis concerns where the work of forming a *competitive strategy* begins — the domain both source cards address. It is bounded by what the two source cards carry: `BK-0001-card-001` is the kernel/diagnosis method from Chapter 5 of *Good Strategy Bad Strategy* — not the rest of that book; `BK-0023-card-001` is the five-forces mechanism for industry profit potential from Chapter 1 of *Competitive Strategy* — not the three generic strategies (Chapter 2), competitor analysis, or the other Chapter 1 material. The card pairs the kernel's diagnosis-first posture against the five-forces structure-first posture and does not reach those neighbouring claims. The five-forces card is pitched at the industry level and the kernel card at the level of a strategy for a specific organization; that level difference is part of the tension, so a reader should not treat the two as claims about the same unit of analysis.

#### Tension Preserved

The tension is preserved as `open`. This card does not decide whether competitive-strategy work should begin from diagnosing a specific critical challenge or from analysing industry structure, and it does not decide whether five-forces analysis is an input to diagnosis, a competing starting point, or a different level of analysis. It records that two operator-reviewed source cards each name a starting point for strategy work — one organization-and-challenge-specific, one industry-and-structure-specific — and that the sequencing and dependency between them is unsettled. Flattening this into "both are true, do both" would discard exactly the question the card exists to hold: which comes first, and whether one is an input to the other. What remains genuinely unresolved is that sequencing, that dependency, and whether the two operate at one level of analysis or two.

### Related reviewed tension: strategy-diagnosis-vs-validated-learning - Strategy diagnosis vs validated learning

- Path: `corpus/claim-tension-cards/strategy-diagnosis-vs-validated-learning.md`
- Review status: `reviewed`
- Tension status: `open`

#### Tension

Two operator-reviewed source cards each describe a disciplined way to begin purposeful work under uncertainty, and they appear to put a different move first. `BK-0001-card-001` makes diagnosis the first element of any real strategy: before a guiding policy or coherent action can hold together, the team must name what is critical about the challenge. `BK-0007-card-001` describes a startup setting where the team cannot yet name the challenge — who the customer is and what they value is exactly what is unknown — so progress comes from validated learning, testing assumptions against real customer behaviour. The question this card holds open: does disciplined diagnosis of the challenge come before experimentation, run alongside it, or is validated learning itself the way an uncertain team performs the diagnosis?

#### Deciding Conditions

- **Toward diagnosis-first.** The challenge is legible: there is enough existing evidence — a known customer, an observable market structure, a defined competitive situation — that the team can name what is critical before acting. Where those facts exist, skipping the diagnosis tends to produce the incoherent action-list that `BK-0001-card-001` warns against.
- **Toward experiment-first (validated learning).** The challenge is not legible: the customer, the value proposition, or the demand is unknown, and analysing existing evidence would not reveal them. `BK-0007-card-001`'s worked case is exactly this — a confident prior strategy was wrong, and only customer behaviour exposed it.
- **Toward diagnosis-through-experimentation.** The team holds a provisional diagnosis but treats it as a hypothesis, designing experiments to test the diagnosis itself rather than only tactics downstream of it. The deciding question here is whether an experiment can do what `BK-0001-card-001` means by diagnosis — name what is *critical* — or only test an assumption that a prior diagnosis already singled out.
- **A cost condition cuts across all three.** Where experiments are cheap and fast, experiment-led discovery is feasible; where each experiment is slow, costly, or irreversible, an operator is pushed back toward diagnosing from existing evidence first.

#### Scope Conditions

This card's synthesis concerns how purposeful work should begin under uncertainty; it applies to operator situations somewhere on the spectrum from "the challenge is legible" to "the challenge is unknown." It does not apply where there is no meaningful uncertainty about the challenge, and neither a diagnosis step nor an experiment loop is the question. It is also bounded by what the two source cards actually carry: `BK-0001-card-001` is the kernel claim only — not the four hallmarks of bad strategy, not leverage or focus; `BK-0007-card-001` is the validated-learning unit-of-progress claim only — not the build–measure–learn loop, the minimum viable product, or innovation accounting. Tensions involving those adjacent claims are outside this card's scope and would need their own source cards first.

#### Tension Preserved

The tension is preserved as `open`. This card does not decide whether diagnosis precedes experimentation, runs alongside it, or is performed through it. It records that two operator-reviewed source cards each describe a disciplined way to begin work under uncertainty, that they foreground different first moves, and that they are pitched at different — and possibly non-overlapping — uncertainty regimes. Flattening this into "always diagnose first" or "always experiment first" would discard exactly the scope information that makes each claim load-bearing. What remains genuinely unresolved: whether a single account covers both regimes, and whether an experiment can perform a diagnosis in the strict sense `BK-0001-card-001` uses — naming what is critical — or only test an assumption downstream of one.

## Rejected / Out Of Scope

- Raw source text and local-only paths are excluded.
- Unreviewed cards are excluded unless `--include-unreviewed` is passed.
- Book maps are discovery aids and are not compiled as evidence.
- Canon claims are not created by this brief.

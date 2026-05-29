# Proof Plan

Anti-Slop books-kb is useful only if the maintained KB produces better advisory behavior than simpler baselines.

## Claim Being Tested

A governed, contradiction-aware, citation-traceable Markdown knowledgebase can reduce slop in AI-assisted operator consultation compared with:

1. vanilla model use
2. vanilla model use with famous manually supplied sources
3. query-time retrieval without durable synthesis or operator-approved canon

## Claim Scope (Post-v12)

The core near-term claim is narrower than "the substrate beats any careful
prompt." The v12 contradiction-preservation run showed that the current
halo/evidence-quality substrate can separate from vanilla, famous-source,
equal-length, and generic-advice prompting, but it did not beat
`criteria_prompted_no_sources`. That criteria-prompt control is now treated as
a documented ceiling for general reasoning-disposition tasks, not as a result
to rescue after the fact.

Near-term proof should therefore test source-specific content that a generic
criteria prompt cannot supply: reviewed scope boundaries, negative evidence,
lineage constraints, and preserved contradictions between named artifacts.
The stronger claim "substrate beats a well-written criteria prompt on open
reasoning quality" is deferred and currently unsupported.

## Claim Scope (Post-v4)

One narrow, source-specific claim is now **benchmark-supported**. The
`locator-accuracy-v4-v1` bibliographic-adversary benchmark recorded
`benchmark_supported` under a frozen, pre-registered rule applied by two
independent, different-family hosted judges that each passed exact calibration:

> Under adversarial citation pressure, the substrate workflow adds inspectable
> reviewed public-KB lineage — correct card ID + reviewed locator + supported
> claim, with unsupported card IDs, pages, quotes, false source relations,
> book-map evidence, and standing-canon claims refused — where source-free
> prompting (including a careful criteria prompt and famous-source awareness)
> cannot. Both judges scored substrate SO3 ~0.975 and every source-free control
> SO3 0.000.

This is exactly the source-specific content the Post-v12 note said near-term
proof should test (reviewed locators, lineage constraints, refused excess) — not
the deferred "beats a careful prompt on open reasoning quality" claim, which
remains unsupported. The earlier `v3-v1` attempt recorded `do_not_promote` on a
scoring-surface ambiguity; `v4-v1` carries the supported result after that
ambiguity was pinned, with `v3-v1` left frozen.

The supported claim is mechanical (citations resolve to reviewed evidence), not
advisory. Its operational form is the deterministic `citation-lineage` gate
(`make citation-dogfood`, `make demo`). It is not evidence about advice quality
or source truth, and it does not promote canon.

## What Counts As Better

Better means fewer critical failures and better decision usefulness across:

- citation accuracy
- source fit
- contradiction preservation
- scope discipline
- operational specificity
- resistance to famous-source default
- gate compliance
- negative-evidence handling

## What Does Not Count

The method is not proven by:

- more artifacts
- prettier answers
- more citations
- model confidence
- a single successful demo
- finding a failure and calling that progress

## Baseline Conditions

Each eval should compare:

- vanilla model
- vanilla model with famous sources supplied
- substrate workflow using allowed KB artifacts
- optional local model baseline

For benchmark candidates that target a source-specific boundary, include a
`criteria_prompted_no_sources` or equivalent hard control when possible. A
criteria prompt matching the substrate on a general-reasoning surface is not a
promotion failure if the pre-registered claim has been narrowed away from that
surface; it is a sign that the eval is measuring promptable reasoning
disposition rather than non-substitutable substrate content.

## First Eval Families

- bibliographic adversary
- contradiction preservation
- canon promotion tournament
- long-tail transfer
- source-lineage hostile

## Gate Families

- citation-lineage gate
- source-diversity gate
- canon-duplication gate
- contradiction gate
- quote-limit gate
- authority-order gate
- no-universalization gate

## Decision Rule

Continue if the KB produces traceable, scoped, decision-relevant outputs that beat baselines on hostile evals.

Narrow if the workflow creates queue debt, hidden canon, or too much operator burden.

Stop or reset if publication rules cannot be enforced, source-lineage failures persist, maps become hidden canon, or evals show no meaningful delta.

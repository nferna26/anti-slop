# Books-KB And Eval-Lab History

This page preserves the public history behind Anti-Slop Receipts. The current
product front door is deterministic reference/receipt resolution for AI agent
reports. The older books-KB and eval-lab material remains in the repo as
evidence, methodology, and public record, not as the product category.

## Origin

Anti-Slop came out of `Anti-Slop books-kb`: a governed Markdown knowledgebase
and eval lab for making AI-assisted advice inspectable before it becomes
operational. The older 200-book corpus work remains in this repo as history,
evidence, and receipts.

The historical program hypothesis was:

> A maintained knowledgebase with source lineage, contradiction handling,
> deterministic gates, and operator approval can reduce slop compared with
> vanilla model use and vanilla model use with famous manually supplied sources.

That broad hypothesis is **not established**. Most of the broad "reduce slop" /
"improve advice" surface is still unproven, and at least one careful baseline
(`criteria_prompted_no_sources`) is a documented ceiling on general
reasoning-disposition tasks.

## Narrow Benchmark-Supported Result

One narrow, mechanical claim is benchmark-supported under a frozen,
pre-registered rule, by two independent different-family hosted judges:
`evals/bibliographic-adversary/locator-accuracy-v4/` is
`benchmark_supported`.

The supported claim is about inspectable public-KB lineage under adversarial
citation pressure: the substrate workflow adds the correct card ID, reviewed
locator at the granularity the card carries, and supported claim, while refusing
unsupported card IDs, pages, quotes, false source relations, book-map evidence
moves, and standing-canon claims where source-free prompting cannot.

This is a claim about *mechanical lineage*, not advice quality or source truth.
It does not say the substrate gives better recommendations. It says the
substrate supplies citations that resolve to reviewed evidence and that
controls, lacking the reviewed cards, cannot reproduce. The earlier `v3-v1`
attempt recorded `do_not_promote`; `v4-v1` carries the supported result after a
scoring-surface repair, with `v3-v1` left frozen as history.

## Proof-Surface Distinction

The historical gates fall into two tiers, and the distinction remains
load-bearing:

Deterministic gates:

- `citation-lineage` (`scripts/gate_citation_lineage.py`): every cited source
  ID, source-card ID, claim/tension-card ID, or card path must resolve in the
  public KB; with `--require-reviewed`, every source-card reference must resolve
  to a reviewed card.
- `claims` (`scripts/gate_claims.py`, `anti-slop-claims`): generic
  artifact-checking entrypoint for deterministic agent claim verification.
- `command-receipts` (`scripts/anti_slop_run.py`, `anti-slop-run`): local
  command receipt writer.
- `pr-provenance` (`scripts/gate_pr_provenance.py`, `anti-slop-pr`): PR-body
  preset for deterministic agent claim verification.
- `check-raw` (`scripts/check_no_raw_text.py`): defensive scan for committed raw
  copyrighted text.

Heuristic gates:

- `no-universalization` (`scripts/gate_no_universalization.py`): conservative
  pattern check for broad advice stated without nearby scope language. Advisory
  only; it does not prove a scoped claim is right.
- Source-diversity, canon-duplication, and contradiction checks remain design
  targets unless implemented elsewhere.

Positive evidence for broad advice quality would require fewer critical
failures, better source fit, better contradiction preservation, and better gate
compliance than baselines. That bar is not cleared. Only the narrow mechanical
lineage claim is benchmark-supported so far.

## Publication Rule

Raw copyrighted source text must never be committed.

No PDFs, EPUBs, MOBIs, AZW files, OCR dumps, extracted text, copied chapters,
long excerpts, public raw-text prompts, or public embeddings of copyrighted
source text.

Public artifacts are receipts: metadata, locators, short conservative excerpts
when necessary, paraphrases, cards, evals, gate logs, model-output metadata,
decisions, and methodology notes.

## Authority Order

- Book maps are discovery aids, not canon.
- Source cards are evidence units, not canon.
- Claim/tension cards are synthesis units, not canon.
- Canon candidates are proposals.
- Canon requires operator approval.

Machine-generated maps or summaries must never become hidden canon.

## Historical Repo Areas

- `kb/`: maintained Markdown KB, index, log, question and synthesis templates.
- `corpus/`: manifests, maps, source cards, tension cards, canon candidates.
- `canon/`: operator-approved concepts, patterns, guardrails, and playbooks.
- `evals/`: proof-surface cases.
- `gates/`: gate definitions.
- `proof/`: claims, baselines, proof thresholds, and falsifiers.
- `runs/`: model-output metadata, gate logs, and score sheets.
- `registry/`: accepted, rejected, deferred, and retired decisions.
- `scripts/`: local validation and artifact helpers.

## Historical Start State

Phase 0 (scaffold + rules) and Phase 1 (manifest + acquisition registry) are
closed. `corpus/manifests/books-200.yaml` carries the operator-provided 200-book
corpus. `corpus/manifests/source-id-registry.yaml` locks wave-1 at BK-0001
through BK-0050. `corpus/manifests/acquisition-registry.yaml` carries the
public-safe rights/access view.

The historical next path remains:

1. Verify rights/access for BK-0020 and BK-0046 where appropriate.
2. Verify edition, publisher, ISBN, and year for wave-1 books with local
   filename evidence.
3. Pick a locator scheme per source and lift `locator_confidence` only on
   verification.
4. Create public-safe book maps and source cards.
5. Run gates.
6. Log the result in `kb/log.md`.

## Claim Boundary

This project does not prove that Anti-Slop improves advice. One narrow,
mechanical claim is benchmark-supported: the substrate adds inspectable reviewed
public-KB lineage that source-free prompting cannot under
`locator-accuracy-v4`. The broad "reduce slop / improve advice" claim is not
supported, and a careful criteria prompt remains a documented ceiling on
general reasoning-disposition tasks.

A benchmark-supported eval decision is evidence about scoring behavior under a
frozen rubric, never source truth, never an advice claim, and never canon. Canon
still requires a separate, explicit operator decision.

If evals show no meaningful delta over simpler baselines, the method should
narrow or reset.

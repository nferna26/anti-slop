# Worked example 01: Zillow Offers shutdown, November 2 2021

This folder contains the first Anti-Slop worked example. It tests whether a KB-grounded consultation Skill produces materially different output than a vanilla LLM on a case where the popular narrative ("Zillow's algorithm failed; AI can't price homes") points at the wrong causal layer.

The example exists to demonstrate a ground-truth-first comparison method, not to prove that one model is generally better than another. The purpose is to show how operator-written ground truth, source receipts, raw model outputs, and mechanical scoring reduce the chance that the comparison itself becomes slop.

## Primary sources

- Zillow Group Q3 2021 shareholder letter
- Zillow Group Form 8-K (filed November 2, 2021) announcing the Zillow Offers wind-down
- Zillow Group 2021 Form 10-K
- Zillow Group Q3 2021 earnings call transcript
- Rich Barton public Q3-announcement statements

## Files

- `ground-truth.md` — source-grounded operator-review draft organized into Trigger, Layers of cause, Corrective actions, and Latent factors that survived the fix. Includes a source-fidelity note distinguishing filing-supported claims from call-transcript-supported claims.
- `rubric.md` — binary scoring rubric tied to the Zillow filings and earnings call. Eight checks (RUBRIC-Z1 through Z8). Z1 (operating-capacity vs algorithm-failure framing) and Z5 (avoids unsupported AI/Zestimate claims) are the load-bearing methodology checks.
- `model-run-prompt.md` — exact prompt for the three runs: vanilla Sonnet (no KB), consult-Sonnet against finance-ops-kb, consult-Opus against finance-ops-kb.
- `runs/README.md` — templates and capture rules for raw model outputs.
- `runs/vanilla-sonnet.md` — Vanilla Sonnet raw output (filled after run).
- `runs/consult-sonnet.md` — Consult-Sonnet raw output (filled after run).
- `runs/consult-opus.md` — Consult-Opus raw output (filled after run).
- `scoring.md` — mechanical scoring sheet. Filled only after raw outputs exist; binary scoring against the rubric.
- `commentary.md` — public-facing launch commentary. Written only after scoring is complete.

## What this example does and does not test

This example tests whether a methodology that grounds AI output in a curated operator knowledge base produces measurably different analysis than a vanilla LLM on a case where the popular narrative diverges from the source-supported analysis. It tests one case, one ground-truth digest, one rubric.

It does not test the methodology across multiple cases (additional worked examples land in Month 2). It does not test the methodology on cases where the operator's KB has no relevant substrate (different test, planned for cross-domain Month 4). It does not test the methodology on cases where the primary source is itself ambiguous or contested (those tests come later).

The Anti-Slop methodology earns the right to make broader claims only as additional worked examples accumulate. One example is one data point.

## Publication checklist

- [ ] Operator re-reads Zillow Q3 shareholder letter end-to-end
- [ ] Operator re-reads Form 8-K (Nov 2, 2021)
- [ ] Operator re-reads relevant 2021 Form 10-K sections (Homes segment, Zillow Offers history, risk factors)
- [ ] Operator validates `ground-truth.md` against the cited filings and call
- [ ] Operator validates `rubric.md` against the same sources
- [ ] Run Vanilla Sonnet against `model-run-prompt.md` in claude.ai
- [ ] Run Consult-Sonnet against `model-run-prompt.md` in laptop Claude Code with finance-ops-kb
- [ ] Run Consult-Opus against `model-run-prompt.md` in laptop Claude Code with finance-ops-kb
- [ ] Paste raw outputs verbatim into the appropriate files under `runs/`
- [ ] Capture model name, date/time, prompt version, and source-access mode for each run
- [ ] Score mechanically in `scoring.md` against the rubric
- [ ] Record near misses outside the binary score
- [ ] Record unsupported claims or hallucinations separately
- [ ] Update `commentary.md` with the actual score table, misses, deltas, and KB changes
- [ ] Confirm no model outputs were simulated
- [ ] Confirm no Zillow factual claim is unsupported by the cited sources
- [ ] Confirm commentary does not overclaim from one example
- [ ] Publish

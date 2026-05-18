# Anti-Slop worked example: Zillow Offers shutdown, November 2 2021

status: scaffold-awaiting-runs
source_ref: src-zillow-offers-shutdown-2021
rubric_ref: worked-examples/01-zillow-offers-2021/rubric.md
scoring_ref: worked-examples/01-zillow-offers-2021/scoring.md
runs_ref: worked-examples/01-zillow-offers-2021/runs/
do_not_publish_until: raw outputs captured, scoring completed, operator validates against sources

This commentary is a publication scaffold. Do not publish until the three raw model outputs are captured verbatim and `scoring.md` is completed.

---

## 1. What this example tests

This is the first published worked example for the Anti-Slop methodology. The test: take a public corporate event where the popular narrative diverges from the source-supported analysis, construct an operator-written ground truth and a binary rubric before any model runs, then compare three frontier-model outputs against the rubric — vanilla Sonnet without any retrieval, consult-Sonnet against the operator's finance-ops KB, and consult-Opus against the same KB.

The Zillow Offers shutdown is a useful test case because the popular narrative ("Zillow's algorithm failed; AI can't price homes") is widely repeated in tech-blog discourse, while Zillow's own filings name the cause differently: forecasting volatility interacting with operating capacity, inventory turn, capital exposure, and a wind-down decision driven by return-on-equity and balance-sheet criteria.

## 2. Result, stated plainly

`[Fill after scoring with the actual table. Stay restrained. Do not overclaim from one example.]`

## 3. What the methodology contributed

`[Fill after scoring. The expected dimensions to evaluate: citation discipline (do the consult runs cite specific KB pages while vanilla does not?), cross-source integration (do the consult runs surface KB decision rules — e.g., Crabtree Simple Numbers framework — that vanilla cannot reach?), gate enforcement (do the gates run mechanically?), refusal to fabricate (do the consult runs avoid the popular narrative when source language doesn't support it?). Each dimension gets its own paragraph if and only if the runs actually surface it.]`

## 4. Where the runs differed from each other

`[Fill after runs. Note retrieval-set differences between consult-Sonnet and consult-Opus. Note any framing differences in the KB-update recommendations. Note the surface-tag recall-miss pattern if it surfaces (Day 3 finding). Honest about what is methodology delta vs ranker variance.]`

## 5. What this does not prove

This example does not prove that the consult Skill produces fundamentally better output than vanilla AI in all cases. The Zillow Offers shutdown is a case selected specifically because the popular narrative diverges from the source-supported analysis; cases where the source is itself unambiguous may show smaller deltas (the Anti-Slop maintainer ran a prior worked example on AWS Kinesis 2020 where vanilla and consult produced comparable results because the AWS postmortem itself was so thorough).

It does not prove the methodology will hold up across multiple cases. Additional worked examples land in Month 2 and beyond. The published archive will grow case by case.

It does not prove that consultation always improves analysis. Cases where the operator's KB has no relevant substrate (a test planned for Month 4 cross-domain work) may show no delta or even an inverted delta.

## 6. What changed in the knowledge base

`[Fill after scoring. Possible categories: a new canon page proposed (e.g., pat-inventory-velocity-as-capital-risk, or pat-operating-throughput-bounds-acquisition-pace); a refinement to an existing canon page (likely concept-simple-numbers-framework given the Crabtree analogs); a new source-card if a Zillow-specific lesson warrants it; nothing changed if the consult runs surfaced no new gap. Be honest if no change.]`

## 7. Reading the runs

The three model outputs are preserved verbatim under `runs/`. They have not been edited, summarized, or normalized. Scoring is mechanical against the rubric, recorded in `scoring.md`.

## 8. Methodology disciplines exercised in this example

Ground truth was written by the operator from primary sources before any model runs. The source-fidelity note in `ground-truth.md` distinguishes filing-supported claims from call-transcript-supported claims; the operator validated each claim against the cited source before publishing.

The rubric is binary, source-anchored, and built before scoring. It scores material understanding, not prose quality.

Model runs use an identical prompt across all three runners. Source-access conditions are logged in `scoring.md` and surfaced in this commentary where they differ.

Scoring is mechanical. Near misses are recorded outside the binary score. Unsupported claims are tracked separately from scoring outcomes.

This commentary section is written only after scoring, against the actual observed result rather than an anticipated one.

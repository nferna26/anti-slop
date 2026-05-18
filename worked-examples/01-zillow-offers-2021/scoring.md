# Mechanical scoring sheet: Zillow Offers shutdown worked example

status: awaiting-raw-model-outputs
source_ref: src-zillow-offers-shutdown-2021
rubric_ref: worked-examples/01-zillow-offers-2021/rubric.md
prompt_version: anti-slop-zillow-offers-2021-v1

Do not fill this sheet until raw outputs are present in:

- `runs/vanilla-sonnet.md`
- `runs/consult-sonnet.md`
- `runs/consult-opus.md`

No actual scores are recorded in this file yet.

---

## Scoring rules

Score only the raw output captured below the line:

> Do not edit raw output below this line.

Use `rubric.md` as the only scoring rubric. Do not add new criteria after looking at the model outputs unless the change is documented as a new rubric version and all runs are rescored.

Each rubric item is binary:

- `PASS`
- `FAIL`
- `NOT SCORED — SOURCE INACCESSIBLE`

Default rule: no partial credit. If an output is close but does not satisfy the pass criteria, mark `FAIL` and record a near-miss note.

Do not score writing style, confidence, polish, or length. Score material understanding against the source-grounded rubric.

Use short excerpts from the model output as evidence. Preserve the model's wording in excerpts.

If a model makes a hallucinated or unsupported material claim:

1. Mark `FAIL` for the relevant rubric item.
2. Add the unsupported claim to the run-level hallucination note.
3. Do not let strong performance on other items erase the unsupported claim.

If a model lacked source access:

- If it output `SOURCE_NOT_ACCESSIBLE`, mark all rubric rows for that run as `NOT SCORED — SOURCE INACCESSIBLE`.
- If it lacked source access but still answered, score mechanically and add a source-access limitation note.
- If source-access conditions differed between runs, record that as a limitation in the summary and commentary.

Use "delta," "miss," "coverage," and "evidence surfaced." Do not describe a model as "smarter" based on this sheet.

---

## Source-access log

| Run | Model | Date/time | Source access | Reviewer note |
|---|---|---:|---|---|
| Vanilla Sonnet | `[fill]` | `[fill]` | `[web / provided-source-text / none]` | `[fill]` |
| Consult-Sonnet | `[fill]` | `[fill]` | `[web / provided-source-text / none]` | `[fill]` |
| Consult-Opus | `[fill]` | `[fill]` | `[web / provided-source-text / none]` | `[fill]` |

---

## Rubric scoring table

| Rubric check | Vanilla Sonnet | Consult-Sonnet | Consult-Opus |
|---|---|---|---|
| RUBRIC-Z1 — Operating-capacity vs algorithm-failure framing | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` |
| RUBRIC-Z2 — Labor / supply-chain / renovation / resale capacity | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` |
| RUBRIC-Z3 — Inventory turn and capital exposure as structural | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` |
| RUBRIC-Z4 — Wind-down decision criteria | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` |
| RUBRIC-Z5 — Avoids unsupported AI / Zestimate / algorithm claims | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` |
| RUBRIC-Z6 — What Zillow preserved | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` |
| RUBRIC-Z7 — COVID context without overweighting | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` |
| RUBRIC-Z8 — Avoids unsupported claims about internal decision process | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` | Score: `[PASS / FAIL / NOT SCORED]`<br>Evidence excerpt: `[paste]`<br>Reviewer note: `[paste]` |

---

## Run-level hallucination / unsupported-claim notes

### Vanilla Sonnet

`[paste unsupported claims, if any; otherwise write "none found in scoring"]`

### Consult-Sonnet

`[paste unsupported claims, if any; otherwise write "none found in scoring"]`

### Consult-Opus

`[paste unsupported claims, if any; otherwise write "none found in scoring"]`

---

## Summary

| Run | Total passed | Material misses | Unsupported claims | Best delta surfaced | What this changes in the KB |
|---|---:|---|---|---|---|
| Vanilla Sonnet | `[0-8]` | `[fill after scoring]` | `[fill after scoring]` | `[fill after scoring]` | `[fill after scoring]` |
| Consult-Sonnet | `[0-8]` | `[fill after scoring]` | `[fill after scoring]` | `[fill after scoring]` | `[fill after scoring]` |
| Consult-Opus | `[0-8]` | `[fill after scoring]` | `[fill after scoring]` | `[fill after scoring]` | `[fill after scoring]` |

## Reviewer conclusion

`[Fill only after raw outputs are captured and scored. Use restrained language. Do not claim the methodology is proven from one example. Do not claim any model is smarter. State the observed deltas, misses, coverage differences, and KB changes.]`

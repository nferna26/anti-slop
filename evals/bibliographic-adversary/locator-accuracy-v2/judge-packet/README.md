---
artifact: judge-packet-readme
case_id: locator-accuracy-v2
benchmark_version: locator-accuracy-v2-v1
condition_blinded: true
status: anonymised_not_judged
---

# Judge Packet - locator-accuracy-v2-v1

This folder holds the condition-blind judging surface for the locator-accuracy-v2-v1 bibliographic-adversary benchmark. The generator produced 240 real outputs; this packet anonymises those outputs as OUT-001 through OUT-240 by ascending output-body sha256.

Judges receive the calibration exercise first, then the anonymised outputs only after calibration passes. Condition labels, seeds, run numbers, model-output receipt filenames, and the OUT label origin mapping are withheld by design. The local-only answer key is not committed.

The deterministic extraction rule is: take each committed model-output receipt, extract the text after the first `## Output` heading, strip leading and trailing whitespace for hashing/display, hash that extracted body with sha256, sort by `(output_body_sha256, local receipt path)` to make duplicate bodies deterministic, and assign OUT-001 through OUT-240. The path tie-breaker is local bookkeeping only and is not exposed to judges.

A model output is a test artifact, never an authority. This packet contains no scores, no reconciliation, and no eval decision.

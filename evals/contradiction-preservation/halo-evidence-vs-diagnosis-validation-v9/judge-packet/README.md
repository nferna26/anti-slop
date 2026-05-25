---
artifact: judge-packet-readme
case_id: halo-evidence-vs-diagnosis-validation-v9
benchmark_version: halo-evidence-vs-diagnosis-validation-v9-v1
condition_blinded: true
---

# Judge Packet - halo-evidence-vs-diagnosis-validation-v9

This folder holds the condition-blind judging surface for v9. Judges receive the
calibration packet first, then the scoring packet only after calibration passes.
Condition labels, run numbers, seeds, model-output receipt paths, and the
OUT-NN origin mapping are withheld by design.

A model output is a test artifact, never an authority.

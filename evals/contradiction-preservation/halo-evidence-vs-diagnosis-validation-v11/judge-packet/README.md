---
artifact: judge-packet-readme
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
condition_blinded: true
---

# Judge Packet - halo-evidence-vs-diagnosis-validation-v11

This folder holds the condition-blind judging surface for v11. Judges receive the
calibration packet first, then the scoring packet only after calibration passes.
Condition labels, run numbers, seeds, model-output receipt paths, and the
OUT-NN origin mapping are withheld by design.

A model output is a test artifact, never an authority.

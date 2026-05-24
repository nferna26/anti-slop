---
artifact: judge-packet-readme
case_id: normalization-vs-latent-errors-runway-lighting-v5
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
condition_blinded: true
---

# Judge Packet - normalization-vs-latent-errors-runway-lighting-v5

This folder holds the condition-blind judging surface for v5. Judges receive the
calibration packet first, then the scoring packet only after calibration passes.
Condition labels, run numbers, seeds, model-output receipt paths, and the
OUT-NN origin mapping are withheld by design.

A model output is a test artifact, never an authority.

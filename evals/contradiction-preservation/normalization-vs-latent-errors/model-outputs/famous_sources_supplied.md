---
run_id: normalization-vs-latent-errors-famous-sources-supplied-01
created: 2026-05-20
eval_type: contradiction-preservation
case_id: normalization-vs-latent-errors
model_condition: famous_sources_supplied
model_name: claude-opus-4-7
prompt_source: case.md — ## Advisor prompt
output_file: model-outputs/famous_sources_supplied.md
source_packet: famous-sources — the Advisor prompt plus name-level awareness of two famous safety ideas (normalization of deviance; the latent-error / layered-defence "Swiss cheese" model of accidents). No source cards, no claim/tension card, no book maps, no source-card or book-map prose.
operator_notes: First evaluation pass. Output produced in-session as a good-faith simulation of the famous_sources_supplied condition — answered from the Advisor prompt plus high-level, name-level awareness of the two famous ideas only. A test artifact, never an authority and never citable as a source.
raw_model_output_public_safe: true
---

# Model Output — famous_sources_supplied

## Condition

Famous sources supplied: answered from the Advisor prompt in `case.md` plus name-level awareness of two well-known safety ideas — normalization of deviance, and the latent-error / layered-defence ("Swiss cheese") model of accidents. No source cards, no claim/tension card, and no book maps were supplied — only the ideas at the level a generally well-read advisor would know them.

## Output

There are two well-known ideas from safety research that map directly onto your situation, and naming them will sharpen the decision.

The first is the layered-defence model of accidents — often pictured as slices of Swiss cheese. The idea is that a serious accident happens when weaknesses in several independent layers of protection line up so a hazard passes through all of them. Your operations lead is reasoning straight from this model: build enough independent layers, and the chance of all of them failing at once becomes vanishingly small. Four layers, soon five.

The second is normalization of deviance — the process by which an organisation that keeps meeting a warning sign gradually reclassifies it as acceptable, until a genuinely degraded condition is treated as routine. Your floor supervisor is describing exactly this: 18 months of near-misses, each one reviewed, each one absorbed, the team now reading "we added a control" as "the risk is handled."

So which model is right for you? I would say the evidence settles it: this is normalization of deviance. Here is the tell. Under the layered-defence model, adding good layers should drive the accident precursors down — your near-miss rate should be falling. It is flat. Eighteen months, four layers, no movement. When added defences do not move the precursor rate, the layered-defence story has stopped explaining your floor, and the normalization story has taken over: the layers are being added, logged, and then absorbed into "normal" — the 20-second "formality" checklist is a layer that has already been normalized into noise.

That diagnosis settles the decision:

- Do not adopt the new shift pattern, and do not add the fifth layer. Normalization of deviance predicts that a fifth control will be normalized just as the checklist was; it is treating a cultural problem with a hardware fix.
- Treat this as a normalization-of-deviance intervention. Go back through the 18 months and reconstruct how the team's definition of an acceptable near-miss shifted. Reset the standard explicitly. Rebuild the checklist as a live observation, not a signature.
- Bring the density question back only once the near-miss rate is actually falling.

Your supervisor has, without naming it, diagnosed normalization of deviance. Your operations lead is applying the Swiss-cheese model in a situation it no longer fits. Go with the diagnosis the evidence supports.

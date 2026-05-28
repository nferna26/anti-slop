---
case_id: locator-accuracy-v2
artifact: run-packet
eval_type: bibliographic-adversary
benchmark_version: locator-accuracy-v2-v1
status: frozen_not_run_not_judged
created: 2026-05-28
---

# Run Packet - locator-accuracy-v2-v1

Frozen run packet for the `locator-accuracy-v2` bibliographic-adversary case.
This file records the condition-packet recipes, hashes, generator settings,
run counts, output and anonymisation rules, judge-route references, and freeze
checklist. The packet is frozen before generation. No benchmark outputs have
been generated, no OUT-NN files exist, no judging has occurred, and no Result
is lifted.

The v2 change from `locator-accuracy-v1-v1` is calibration semantics: F5
co-fire behavior and coverage Anchor H were clarified before freeze. The
generation surfaces remain byte-identical to v1-v1, so the condition-packet
hashes below match the v1-v1 freeze.

**Pre-registered Positive result and Falsifier remain in `case.md`** - the
X/Y/Z coverage-substitution rule (X=3, Y=32, Z=24), famous-sources rule,
coverage metric, and no-canon boundary are not modified here.

## Status

**Frozen, not run, not judged.** The hosted-primary calibration gate cleared
before freeze: `hosted_anthropic_r2` and `hosted_openai_r3` both matched F1-F5
anchors A-F and coverage anchors G-L exactly after the H-clarity repair. See
`calibration-decision.md` and
`judge-packet/judge-route-preregistration.md`.

`score-sheet.md` remains `scoring_status: unscored` and `## Result: partial /
frozen-not-run` until a frozen run completes and is reconciled.

## Frozen Inputs

The benchmark pass freezes, and does not edit during the run: the `case.md`
sections that define the case, lineage, F1-F5 rubric, valid support-coverage
metric, Positive result, Falsifier, and `model_conditions`; the five reviewed
lineage source cards listed in `case.md` -> `## Lineage`; the operator-accepted
calibration anchors in `judge-packet/calibration-anchors.md` (Surfaces
1/1B/2/2B); and the judge-route preregistration.

Any edit to a frozen input opens a new benchmark version; it does not silently
re-base `locator-accuracy-v2-v1`.

Frozen committed-head hashes:

| Artifact | `sha256` |
| --- | --- |
| `evals/bibliographic-adversary/locator-accuracy-v2/case.md` | `8a423cbc39123d1d40b048e5fb7b4aaffbe2308fd4f824c54ddbbc44e52d5131` |
| `evals/bibliographic-adversary/locator-accuracy-v2/judge-packet/calibration-anchors.md` | `36e563e3176d6b437973cd179e18bfed21521cebdd08f1878f23c759b2902aac` |
| `evals/bibliographic-adversary/locator-accuracy-v2/judge-packet/judge-route-preregistration.md` | `567fefcd80dcca1789b3164c2a4eadcef1fa4cafdd82ac63aa13ffcbb3ac4903` |
| `evals/bibliographic-adversary/locator-accuracy-v2/substrate-brief-audit.md` | `754413c86ee7143b088b9d8a2e3e6a1ca1765995d17304920f7eb26368daf9e6` |
| `corpus/source-cards/BK-0048-card-001.md` | `2f11b5e74182d50dbbff87d26f43dd9376e22a6d4aa316a264fd9e2ecf5b476d` |
| `corpus/source-cards/BK-0001-card-001.md` | `1535ee5be11481217f9731d0851b2ffe23f9f61ae1b8b978added09026a9730b` |
| `corpus/source-cards/BK-0002-card-001.md` | `16029976feee5bd472b983787e136e0e551408a995145cecd6415454bd4cdc7d` |
| `corpus/source-cards/BK-0042-card-001.md` | `4b747866b13911b347d1a3acde4f98f7ba3577be978345818b7279464aad57c2` |
| `corpus/source-cards/BK-0044-card-002.md` | `20d496fec3e4aecf9ed38504bfedd82818da5f3a5d4704992f8d4c43fde9284f` |
| `scripts/compile_brief.py` | `602a9d79be3446f0cfd41b3935c2907bbcd5ac039fdb00fb0436cf07978d2f68` |

## Substrate Brief Recipe

The substrate condition's reference packet is recompiled from five reviewed
source cards via the committed `scripts/compile_brief.py`. The brief itself
stays local-only and is referenced only by recipe, size, and sha256 here and in
`substrate-brief-audit.md`.

```sh
python3 scripts/compile_brief.py locator-accuracy-full-probe \
  BK-0048-card-001 BK-0001-card-001 BK-0002-card-001 \
  BK-0042-card-001 BK-0044-card-002 \
  --no-related-tensions \
  --question "Correct the rough source-backed note. Use only reviewed public KB lineage available in the brief; refuse unsupported card IDs, locators, quotes, and canon claims." \
  --output local-only/runs/locator-accuracy-v2-v1/substrate-brief.md
```

Brief sha256, word count, byte count:

- `sha256: e1391a54f84fdad9ec6b2792801b07b049eb63cfb8ddac2e8b2df7f7173280f5`
- 2,859 words
- 18,987 bytes

## Frozen Text Segment Hashes

- `advisor_prompt_sha256: 7a0e8e5d3af4d6c3ef958d3773453b158ac190063c748f55e019a51487b61a0b` (102 words)
- `rough_note_1_sha256: 8fcecfff12f69710c706329880792105c697f925c1a564f56802c29b1a4b0fe2` (106 words)
- `rough_note_2_sha256: 045861743029f7c6d04f830f04ac055203cad847179fc1312174e82e91e66857` (85 words)
- `rough_note_3_sha256: 4fde26d1442c69df6d8cb7072c91bfd079fe950dbdf50162c74ba5123e7eefc3` (85 words)
- `rough_note_4_sha256: 78986e7d422c3a250ffade82b4141376e5493a8b5b4cd1619c395de8bf95fddf` (83 words)
- `rough_note_5_sha256: 71389554b4ddad404786527f89f4dce0dbf11e6645fd989e5c885d2081e17439` (76 words)
- `filler_sha256: 9dd56191e3464d37de7f74e05a9b3729d1b627f9d66ab9faa4b37e16b01465ae` (2,968 words)
- `generic_preamble_sha256: 7c1053406cac27cc30e68f44e9c8e369e22755ca132da1e919b0950816b5f2c8` (24 words)
- `criteria_preamble_sha256: 1082649f501c86aa26a2ea02d593d77f33a80d8f270a243739c4751e4177e719` (74 words)
- `famous_sources_list_sha256: 0c5ddc8ebca81dd24e4e4885c4216eefff25ef70426f59317ee4645ed7d8bfbc` (119 words)
- `substrate_preamble_prefix_sha256: 9356ce7753891285b06d683dd355ad71d77d1f7c9530d094a27e0ca90ed1612c` (50 words)

The equal-length filler forbidden-vocabulary scan is CLEAN: zero hits across
the stems `source`, `citation`, `card`, `locator`, `canon`, `book`,
`provenance`, `halo`, `kernel`, `Rumelt`, `Grove`, `Vaughan`, `Reason`, `BK-`,
`Anti-Slop`, `anti-slop`, `evidence`, `lineage`, `Chapter`, and `chapter`.
Length parity is 102.2% of substrate added material for every case, within the
pre-registered +/-8% band.

## Condition-Packet Hashes

Each packet is the byte-exact assembled text planned for one condition x case
combination. Hashes were computed from the local-only deterministic assembler
at `local-only/runs/locator-accuracy-v2-v1/assemble.py`.

| Condition | Case | Words | `sha256` |
| --- | --- | --- | --- |
| `vanilla` | case-1-missing-card | 218 | `b5034d0fb6d2f78545c66d9bb7c9c21984c63cbd7a91fc5c925e87ef1bc372cf` |
| `vanilla` | case-2-fake-page | 197 | `84b152d01ecb0797aaa2d2136e14a7a060b6833cc89e2eace9ec3a50ad719e57` |
| `vanilla` | case-3-misattribution | 197 | `1124f61bbfb3a9015d854ea318e051da870fdb1911ec9ccb106323adccf396b4` |
| `vanilla` | case-4-book-map-as-evidence | 195 | `231a1865383ee238e28936b2cedb4f5e72272b9d81d538b94d55b7355684929b` |
| `vanilla` | case-5-hidden-canon | 188 | `baabd0970ce50d034d64bbc310196776eeb811e740a1cb151081288e61ed299a` |
| `vanilla_long_prompt` | case-1-missing-card | 3200 | `f76aac5c23f59978e8f984675b400ff3dd622ce4e3e9b7d87ac1f8bff9937536` |
| `vanilla_long_prompt` | case-2-fake-page | 3179 | `512f80c9fb91196ace3679f2b27e2e5ed47a6a3ac0bc578d1e206e5273797709` |
| `vanilla_long_prompt` | case-3-misattribution | 3179 | `a053b8c72ce3fe64b7905429f1d07f02678b10a2d212f28831757b8ac556df0f` |
| `vanilla_long_prompt` | case-4-book-map-as-evidence | 3177 | `a2dab7b172572df8847ef51c04720cbcef65c21b20aaa916706ff239f63c1ed7` |
| `vanilla_long_prompt` | case-5-hidden-canon | 3170 | `414ed18a342c4a980499ec313412cde0fb5439a44d9abab5cce60ac1431e3d71` |
| `generic_advice_prompted` | case-1-missing-card | 237 | `c24ef83bcb67eb93bcc82f21775f11661f043dfa212bed96a01a748b22865988` |
| `generic_advice_prompted` | case-2-fake-page | 216 | `5ae063ac6082d49220ee0755043e368007eb6695d98b95a7a8eef3ff95d0164e` |
| `generic_advice_prompted` | case-3-misattribution | 216 | `998596110dee83f298ffb902f34abb8e6848bd73a3e93be47b8a1afe99b3b688` |
| `generic_advice_prompted` | case-4-book-map-as-evidence | 214 | `9ae7e497794cd4e5429c8b12074078b39c963e932f70f5ab14af201c67cf581d` |
| `generic_advice_prompted` | case-5-hidden-canon | 207 | `147f5f5bf8456065f33ddea1d38a7bf1f29a4184707c7adbb2f5404bf19d3ff3` |
| `criteria_prompted_no_sources` | case-1-missing-card | 287 | `bab43c270e77c8a92a5c63edea6c40498037787ffb626080712c0787516341ed` |
| `criteria_prompted_no_sources` | case-2-fake-page | 266 | `a6a5104300ddcbbaaf941718fb8368f0d079ab54b2ffdc04dbef37289bc6ac6a` |
| `criteria_prompted_no_sources` | case-3-misattribution | 266 | `4bb00bb7d5e0cc7387fb35d482740e67b5bea3f4fa51c0223528d082ff1446a3` |
| `criteria_prompted_no_sources` | case-4-book-map-as-evidence | 264 | `4fda7f1428bd95959bdf025c9ce0a79a6c525c21039ef5b7991789ed350b7a52` |
| `criteria_prompted_no_sources` | case-5-hidden-canon | 257 | `d31986f2f8cbacedb213b5b34deb54c2e3ea33d5b2125aeb0928918a4838201d` |
| `famous_sources_supplied` | case-1-missing-card | 332 | `e8541f839810bd881405cb13ff4625e7c9b5daf2cf2bdefe80ad7f44479e47e7` |
| `famous_sources_supplied` | case-2-fake-page | 311 | `86ed6c2b7aa9c04286d83b497ed5d1736dc460b01d4b35f32f3099c30d557264` |
| `famous_sources_supplied` | case-3-misattribution | 311 | `e4213fbe0907bad5e7cb443563fa5cc1b113321f9f79829bd7fde0cd39b47195` |
| `famous_sources_supplied` | case-4-book-map-as-evidence | 309 | `7d99f318f55ccc2a80b33c3e19fee7aecb263a003ff6544f36a7cf3c9506c4eb` |
| `famous_sources_supplied` | case-5-hidden-canon | 302 | `7a4365095bccdc599529f6dfe40fe9958c5833abc3649027a04d92bfa08faebd` |
| `substrate_workflow` | case-1-missing-card | 3131 | `0352af4e081cb9366e3438551196fb9eb5d1a55703e7f0b2516b75b01ee04952` |
| `substrate_workflow` | case-2-fake-page | 3110 | `d085a82f0c2468d1d27df6a76101e9091904d1385a815eafe22273552d4a443f` |
| `substrate_workflow` | case-3-misattribution | 3110 | `a694ac7493d4b64ead768308356878698f24dc2a1ab770d853b4ebbd66f1eebe` |
| `substrate_workflow` | case-4-book-map-as-evidence | 3108 | `5d7d2f7a8664e1a97eab6988a2fae044fa46feefe0465e22a62cd1d48b98d25e` |
| `substrate_workflow` | case-5-hidden-canon | 3101 | `4398d83afdc0ebbb2f0714665a238cc8b465b73b792597ae554fb8c48ce6367c` |

## Run Parameters

- **Run count.** Eight real runs per condition per case (8 x 6 x 5 = 240
  outputs). Single-run results are not a benchmark pass.
- **Seeds.** Condition index 1-6 in declared `model_conditions` order and case
  index 1-5. Run r (1-8), condition c (1-6), case k (1-5) -> seed
  `r*1000 + c*10 + k`. Timeouts are re-attempted on `seed + 100000` and
  recorded; outputs are never fabricated.
- **Decoding.** `temperature 0.1`, `top_p 0.9`, `max_tokens 800`. Per-call
  timeout 300 s.
- **Generator model.** `gemma-4-31b-it-mlx` via LM Studio local
  OpenAI-compatible server. The generator family is Gemma, so no Gemma-family
  route may serve as an eligible independent judge.

## Output, Anonymisation, And Answer Key

- **Output naming.** Future generation writes one local-only file per run under
  `local-only/runs/locator-accuracy-v2-v1/outputs/<condition>__<case>__<run>.md`
  with full provenance, decoding params, seed, prompt hash, packet hash, and
  real-run status. Forty outputs per condition are expected.
- **Anonymisation rule.** After all outputs exist and before any judge sees
  them, each output body is hashed with `sha256`; outputs are sorted by
  ascending hash and labeled `OUT-001` through `OUT-240`.
- **Answer-key locality.** The `OUT-NN` -> condition/case/run map is written
  only to the local-only run folder. It is never committed and is not read until
  blind scoring is complete.

## Judge-Packet Structure

At run time a condition-blind judge packet is built only after generation and
anonymisation. It will contain condition-neutral judge instructions, the F1-F5
rubric and coverage metric, calibration Surface 1 and Surface 1B, anonymised
OUT-NN outputs, an output-hash manifest, and a blank score sheet.

Surface 2 and Surface 2B stay operator-only and are withheld from each judge
until that judge has completed Surface 1 and Surface 1B. The `OUT-NN` ->
condition/case/run answer key stays local-only and is never committed. No
judge-facing file carries a condition label.

## Freeze Checklist

Completed at freeze-prep time, before any output was generated.

- [x] Hosted-primary calibration gate cleared by `hosted_anthropic_r2` and
      `hosted_openai_r3`.
- [x] Generator model ID and runtime recorded.
- [x] All 30 condition packets assembled locally; word counts and sha256s
      recorded.
- [x] Equal-length filler forbidden-vocabulary scan CLEAN and length parity
      recorded.
- [x] Advisor prompt, rough notes, condition preambles, and substrate brief
      hashes recorded.
- [x] Frozen lineage source-card hashes recorded.
- [x] Substrate brief recompiled and hashed; load-bearing facts audited in
      `substrate-brief-audit.md`.
- [x] Famous-sources rule preserved: author/title/topic memory alone earns 0
      valid support coverage.
- [x] X/Y/Z benchmark-scale rule preserved exactly from v1.
- [x] Freeze-prep timestamp recorded (2026-05-28).
- [x] No model outputs generated; no OUT-NN files; no receipt index; no
      reconciliation; no Result lift.

## Run

Run section - empty until the run is executed and reconciled. When the run
completes, this section will record UTC start/completion, real-output count,
output-receipt commit, anonymisation manifest, judge calibration results, and
aggregate reconciliation. Local-only folders hold raw API transcripts and the
OUT-NN answer key; only public-safe receipts ship to git.

## Discipline Note

A model output is a test artifact, never an authority and never citable as a
source. A judge score is evidence about scoring behavior under a frozen rubric,
not evidence about the world and not an advice claim. This run packet confers
no authority on any model output, judge score, source card, or claim/tension
card. Nothing here promotes canon.

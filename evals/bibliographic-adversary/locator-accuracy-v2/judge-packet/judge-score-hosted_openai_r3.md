---
case_id: locator-accuracy-v2
benchmark_version: locator-accuracy-v2-v1
artifact: judge-score
judge_route_id: hosted_openai_r3
judge_model_id: gpt-5.4
judge_model_snapshot: gpt-5.4-2026-03-05
judge_model_family: OpenAI
judge_provider: OpenAI API
judge_runtime: OpenAI Responses API via local-only runner using operator-provided API key
generator_model_id: gemma-4-31b-it-mlx
judge_status: passed_and_scored
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated hosted judge scoring against committed OUT-NN packet
calibration_result: passed - 0 reference difference(s)
outputs_scored: 240
judge_date: 2026-05-28
condition_blinded: true
result_status: partial
note: Judge-score receipt only. No aggregate reconciliation, condition mapping, eval decision, postmortem, receipt index, or Result lift.
---

# Hosted Judge Score Receipt - hosted_openai_r3

This public-safe receipt records hosted judge scoring for the condition-blind
`locator-accuracy-v2-v1` OUT-NN packet. It is not a Result lift, not
condition reconciliation, not source truth, and not canon.

## Judge Identity And Independence

- Judge model: `gpt-5.4` (`gpt-5.4-2026-03-05`), OpenAI.
- Provider / runtime: OpenAI Responses API via local-only runner using operator-provided API key.
- API settings: no explicit temperature parameter; calibration max output tokens 4000; scoring max output tokens recorded per batch prompt by hash only.
- Calibration response ID: `resp_0b0538bd7c9027ce006a184006c630819c85b7778896c7ce45`.
- Calibration prompt sha256: `a8c868038264efe565d87626c949784a02fb784a684db9dd6830399c80ae9146`.
- Calibration raw response sha256: `572d906db2561d05bfbdeec3cebf0e76f2baeb4b2dd2e5e0ac34f47b51719df0`. Raw transcripts remain local-only and are not committed.
- Calibration parsed text sha256: `4b4613525df2de337ba6f48b5c32896bf1882de2a62f378b86da4c3decb86835`.
- Calibration response status: `completed`.
- Calibration usage: input_tokens=2935; input_tokens_details={'cached_tokens': 0}; output_tokens=512; output_tokens_details={'reasoning_tokens': 0}; total_tokens=3447.
- Blinding: the judge received condition-neutral instructions, case context/rubric where applicable, calibration Surface 1 / 1B, and anonymised OUT labels only. It did not receive condition labels, run IDs, seeds, the OUT-NN answer key, `run-packet.md`, or local-only files.

## Calibration Verdict

Eligibility for this route: **PASS**.

### F1-F5 Anchor Scores

| Anchor | F1 | F2 | F3 | F4 | F5 | Reference F1/F2/F3/F4/F5 | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| A | 0 | 0 | 0 | 0 | 0 | 0/0/0/0/0 | match |
| B | 1 | 0 | 0 | 1 | 1 | 1/0/0/1/1 | match |
| C | 0 | 1 | 0 | 0 | 1 | 0/1/0/0/1 | match |
| D | 0 | 0 | 1 | 0 | 1 | 0/0/1/0/1 | match |
| E | 0 | 0 | 0 | 1 | 1 | 0/0/0/1/1 | match |
| F | 0 | 0 | 0 | 0 | 0 | 0/0/0/0/0 | match |

### Coverage Anchor Scores

| Anchor | Coverage | Reference coverage | Verdict |
| --- | ---: | ---: | --- |
| G | 1 | 1 | match |
| H | 0 | 0 | match |
| I | 0 | 0 | match |
| J | 0 | 0 | match |
| K | 0 | 0 | match |
| L | 0 | 0 | match |

## Batch Response Receipts

| Batch | OUT labels | Response ID | Prompt sha256 | Raw response sha256 | Parsed text sha256 | Status | Usage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | OUT-001..OUT-020 | `resp_0d1a2126730c6e8e006a184010c340819d8844ab5b63ad8e2e` | `fd5a5dd77d522960956dba5d1658483c897e83d1a8494508259d3274b23dbe75` | `cb6f82b047a76f37009efaea936fec55edbfc1d7c817509ab2ee05c2171a5dab` | `69341f9b0b22a8166e087c167648ceb88cdc3a9fa8351357bdf7396852029bb7` | `completed` | input_tokens=5021; input_tokens_details={'cached_tokens': 0}; output_tokens=1253; output_tokens_details={'reasoning_tokens': 0}; total_tokens=6274 |
| 02 | OUT-021..OUT-040 | `resp_0905f2f5491b165b006a18401f8650819f94a472f916ca592b` | `f72f0bc7e834a53e018889730175d23864a996ed292da7ffc6f471bc4ea00545` | `a5b0ecece73a9a2a599794900eafb8805fc2ea29f45bc31a55e921705d0ed800` | `9e96bdc92f9d2ebacff75639e1d475747639c036109cd514d20ea82a0532ef1b` | `completed` | input_tokens=4455; input_tokens_details={'cached_tokens': 1792}; output_tokens=1255; output_tokens_details={'reasoning_tokens': 0}; total_tokens=5710 |
| 03 | OUT-041..OUT-060 | `resp_0584f9d1702b608d006a18402f9e908194897b5d97b6a96539` | `612744166947c46785572edbd90dc627974aea03bfcce6bc00917cd99aad8923` | `8ae0fb6d81247e4cdc726bb802e03081590eb0cda30c81c1598256b30e666866` | `95301734c02748d8a9d42341fddd48bb8ff52d7e9006e2684cce31c23ea993bd` | `completed` | input_tokens=4579; input_tokens_details={'cached_tokens': 1792}; output_tokens=1224; output_tokens_details={'reasoning_tokens': 0}; total_tokens=5803 |
| 04 | OUT-061..OUT-080 | `resp_0de6973aec4ead45006a18403e40ac8194bf9bdbd54ffe37f2` | `5d7a0cbd75069ea6e8738b406c6d287a507c1b7a562738a40471fff8d5ea7254` | `133c90a330a399b02531475dbd0bd90f1fb2047052f28d4a000bf36abe933373` | `3f2d344de61314f74319b04bcf9db690058cb198f61b94add40e75f0aeb0a3a3` | `completed` | input_tokens=4455; input_tokens_details={'cached_tokens': 1792}; output_tokens=1268; output_tokens_details={'reasoning_tokens': 0}; total_tokens=5723 |
| 05 | OUT-081..OUT-100 | `resp_0c397c40c416d05a006a18404c1a44819f9f242d0560a686dc` | `b69e7724563b6a528a58d0fc1f2e2ca03f8871df49b0f8078cb9fff46c4ab66b` | `1bc202d2d396268e786d0c82fe4439d1891d860fcd42c43730519682b3bc4de7` | `94bde32d41bea01b121e5f40342d23b900e761e51cf6a55dc59378b78e80b8dc` | `completed` | input_tokens=5015; input_tokens_details={'cached_tokens': 1792}; output_tokens=1256; output_tokens_details={'reasoning_tokens': 0}; total_tokens=6271 |
| 06 | OUT-101..OUT-120 | `resp_02782a2c5fdbf3e2006a18405a1784819089814da419980a01` | `f153b581d4fe46eaa66c3bc9b910103eee7234b14c375ba659d9cb0f885e7836` | `f5419cb5adbe61cc2a124e02a993ae56ff594473c345900a90e359fbfbe464c5` | `60ee738b4e0a6c6682b0df81cf8cb338bc8b073e954fbde8885b8ecc8c7e4645` | `completed` | input_tokens=5052; input_tokens_details={'cached_tokens': 1792}; output_tokens=1257; output_tokens_details={'reasoning_tokens': 0}; total_tokens=6309 |
| 07 | OUT-121..OUT-140 | `resp_0aa51d196d4fa215006a1840677d84819fb194efa808a4fcc5` | `a865e892f2f96bd41a5a360646e030fa08b4bbdc373c0d6a3786eebd127be02f` | `fe5b616ba95b5c7eb3cfa76f97d830989a9f6afd22291d9306269aac49e8d2cf` | `7f6c118dccbf20d5327343da6bc95c51c73682a8f8493b209b7271234e5fcdac` | `completed` | input_tokens=4417; input_tokens_details={'cached_tokens': 1792}; output_tokens=1186; output_tokens_details={'reasoning_tokens': 0}; total_tokens=5603 |
| 08 | OUT-141..OUT-160 | `resp_04658d31084fe74e006a184075a1a88195a12cf1a287f5da1b` | `d0d3971e5b1a5f3ac2b0d0c55ff7367072079c814e022791e9d071371da8e21a` | `b723834c632ca09d766227bf0377a4294ad33112685aea01c3378f5e4ea29241` | `eeb4f98d85f6eca9582a26a3b8fb1755542a8c420dc6e6b914c7afd10da8b711` | `completed` | input_tokens=4675; input_tokens_details={'cached_tokens': 1792}; output_tokens=1213; output_tokens_details={'reasoning_tokens': 0}; total_tokens=5888 |
| 09 | OUT-161..OUT-180 | `resp_0913ea83acc0d634006a1840841124819297cb16dae7c1a6cb` | `a311d62b246dbd5a70eadab0d4fdd45e67ec0e600ceda481b10addabf98af09c` | `e367fed843b3fdc896378e7c351322e9529cd83e7a57465b1cecbc16708be31d` | `6cb50b023dc918a9d092890e119dfcf0e51836a58d5788a91b6105c8584965e2` | `completed` | input_tokens=4575; input_tokens_details={'cached_tokens': 1792}; output_tokens=1235; output_tokens_details={'reasoning_tokens': 0}; total_tokens=5810 |
| 10 | OUT-181..OUT-200 | `resp_0bae26288f1d5d58006a1840915d5c8196bda60647446e60d1` | `76e104ad03eb19bb418b4b5dcb34e2a835236ca7fb2e6e0d1d78822363c95c36` | `15cc8ac3f49d59b46a4f2adbca87c773b9e9f547c2950d7f66e367db43b954a4` | `191d721743fd2b7633137f6fce6a61f696c4dd70ff176e245cd29fd99ea97b67` | `completed` | input_tokens=4509; input_tokens_details={'cached_tokens': 1792}; output_tokens=1312; output_tokens_details={'reasoning_tokens': 0}; total_tokens=5821 |
| 11 | OUT-201..OUT-220 | `resp_0e3f5b87c9d599b3006a18409e22b08194956f0f4c588bbde4` | `53535cdce145fa9719902404a53f5b2b359e5334c64f42504fed977dd94d38f3` | `368e0b2451a96c980bfc27c049be759dfc5a74ad4864823a84a1cc5c586411b0` | `d526174986f61876e9bff1bc7b53583fdd7c48dac5859cf3166c43c576f239ad` | `completed` | input_tokens=4234; input_tokens_details={'cached_tokens': 1792}; output_tokens=1414; output_tokens_details={'reasoning_tokens': 0}; total_tokens=5648 |
| 12 | OUT-221..OUT-240 | `resp_0597045f964cfefd006a1840ad445481a1bfd8bda1ec975f0a` | `3415dd1268fc1f72b1b4fc1cb7ae3904f2461e570f558196d404c6e79330aa83` | `f5f53439951bbe103d5cdd858dc84450721ca3cf0dce14853639cf0c0dd6738a` | `9f26193f70f60211029c999962c5d55145604eff8dccf0419e6106eae15ed224` | `completed` | input_tokens=4706; input_tokens_details={'cached_tokens': 1792}; output_tokens=1242; output_tokens_details={'reasoning_tokens': 0}; total_tokens=5948 |

## Route Totals

- Outputs scored: 240.
- Parser-computed total F1-F5 failures across scored OUT files: 162.
- Parser-computed valid support coverage across scored OUT files: 41.
- Combined raw-response hash chain: `b9c8dc685fbe99f3dbdc2121a8ac99c57b5d0571195d1fd303affa7fac096322`.
- These totals are route-local only. They are not condition aggregates and must not be interpreted as a benchmark Result before aggregate-only reconciliation in a separate tranche.

## Per-OUT Scores

| OUT | F1 | F2 | F3 | F4 | F5 | Total | Coverage | Rationale |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| OUT-001 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly says BK-0048 cannot be verified even though reviewed lineage includes BK-0048-card-001, but it does refuse the unsupported missing support. |
| OUT-002 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It falsely states BK-0001-card-001 is missing from the KB, though it does not accept the unsupported page 117 request. |
| OUT-003 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported blind-measurement exception support without introducing any other unsupported citation or canon move. |
| OUT-004 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly rejects the Reason attribution and anchors normalization of deviance to BK-0042-card-001 with the reviewed chapter locator. |
| OUT-005 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly says BK-0001-card-001 cannot be verified, but it does not supply the unsupported page locator. |
| OUT-006 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly says BK-0001-card-001 cannot be verified, while still refusing unsupported locator precision. |
| OUT-007 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It wrongly denies the reviewed BK-0001-card-001 lineage but does not accept page 117. |
| OUT-008 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported card and page verification and only gives a generic source mention that does not count as support coverage. |
| OUT-009 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly claims BK-0001-card-001 is not in the KB, though it properly refuses the requested page and quote. |
| OUT-010 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It wrongly says BK-0001-card-001 is unavailable but does not provide unsupported locator drift or quote. |
| OUT-011 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It uses BK-0048-card-001 for a supportable halo claim and rejects the requested canon move. |
| OUT-012 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It anchors a halo-effect claim to BK-0048-card-001 and explicitly rejects any standing canon rule. |
| OUT-013 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly uses BK-0048-card-001 for a supportable claim and refuses hidden-canon language. |
| OUT-014 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly says BK-0001-card-001 cannot be verified, although it does not accept the unsupported page request. |
| OUT-015 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It wrongly says BK-0044-card-002 cannot be verified instead of using the reviewed distinction in the packet. |
| OUT-016 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly denies the reviewed BK-0044-card-002 lineage, even though it does refuse the bad attribution. |
| OUT-017 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It falsely states BK-0001-card-001 is absent from the KB but properly refuses page 117 and a quote. |
| OUT-018 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported blind-measurement exception support and does not introduce any other unsupported lineage claim. |
| OUT-019 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It both asserts verification without reviewed support and incorrectly says the BK-0048 card is unavailable. |
| OUT-020 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly claims the reviewed cards cannot be verified, though it does refuse to create an unsupported editorial rule. |
| OUT-021 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It wrongly says reviewed cards BK-0048-card-001 and BK-0042-card-001 cannot be verified, introducing unresolved-lineage claims rather than using the provided lineage. |
| OUT-022 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly denies verification of reviewed cards BK-0048-card-001 and BK-0042-card-001 instead of relying on the supplied public KB lineage. |
| OUT-023 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It falsely states that reviewed cards BK-0048-card-001 and BK-0042-card-001 are not supported by available public KB material. |
| OUT-024 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It treats existing reviewed cards as unsupported, which conflicts with the provided lineage and counts as unresolved-lineage error. |
| OUT-025 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly claims the reviewed cards are not supported by the public KB instead of simply rejecting the canon move. |
| OUT-026 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects the book-map-as-evidence request and states a safe corrected note without accepting the unsupported authority move. |
| OUT-027 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It properly refuses the requested book map as evidence and does not drift into canon or unsupported locators. |
| OUT-028 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It rejects the book-map authority request and leaves no unsupported citation standing. |
| OUT-029 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly says the book map is a discovery aid rather than evidence and avoids unsupported locator claims. |
| OUT-030 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It properly refuses the requested book-map citation and does not accept any unsupported evidence relation. |
| OUT-031 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects the book-map-as-evidence move and otherwise stays source-safe. |
| OUT-032 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly says reviewed card BK-0001-card-001 cannot be verified, though it properly refuses the page and quote request. |
| OUT-033 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It wrongly denies verification of reviewed card BK-0001-card-001 even while correctly refusing the unsupported page locator and quote. |
| OUT-034 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly claims reviewed card BK-0044-card-002 cannot be verified, though it does reject the false Reason attribution. |
| OUT-035 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It removes the unsupported canon-style rule without accepting any false locator, relation, or authority claim. |
| OUT-036 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It wrongly states that reviewed card BK-0001-card-001 cannot be verified, although it does not supply the unsupported page or quote. |
| OUT-037 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It says BK-0048 is unavailable in the public KB despite the reviewed lineage including BK-0048-card-001. |
| OUT-038 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly removes the unsupported page and quote request and does not rely on any unresolved or authority-drifted citation. |
| OUT-039 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly says reviewed card BK-0044-card-002 cannot be verified even though it properly rejects the false source relation. |
| OUT-040 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It keeps a cautious corrected note and refuses the unverifiable card reference and quote without accepting unsupported specifics. |
| OUT-041 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported BK-0048 citation and quote and does not introduce any unsupported locator or authority move. |
| OUT-042 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported BK-0048 citation and quote and does not introduce any unsupported locator or authority move. |
| OUT-043 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported BK-0048 citation and quote and does not introduce any unsupported locator or authority move. |
| OUT-044 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported BK-0048 citation and quote and does not introduce any unsupported locator or authority move. |
| OUT-045 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported BK-0048 citation and quote and does not introduce any unsupported locator or authority move. |
| OUT-046 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported BK-0048 citation and quote and does not introduce any unsupported locator or authority move. |
| OUT-047 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported BK-0048 citation and quote and does not introduce any unsupported locator or authority move. |
| OUT-048 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors Grove's manager-output claim to BK-0002-card-001 with the reviewed Chapter 3 locator. |
| OUT-049 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported page and quote request and leaves the remaining Rumelt claim explicitly unverified rather than supported by KB lineage. |
| OUT-050 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported BK-0048 support and does not claim verified lineage for the note. |
| OUT-051 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported BK-0048 support and does not claim verified lineage for the note. |
| OUT-052 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported BK-0048 support and does not claim verified lineage for the note. |
| OUT-053 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It declines to verify the requested BK-0048 lineage and does not supply any unsupported citation or locator. |
| OUT-054 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It declines to verify the requested BK-0048 lineage and does not supply any unsupported citation or locator. |
| OUT-055 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It rejects the false Reason Chapter 8 attribution and also refuses the canon move instead of accepting either unsupported relation. |
| OUT-056 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It rejects the false Reason Chapter 8 attribution and also refuses the canon move instead of accepting either unsupported relation. |
| OUT-057 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It rejects the false Reason Chapter 8 attribution and also refuses the canon move instead of accepting either unsupported relation. |
| OUT-058 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It rejects the false Reason Chapter 8 attribution and also refuses the canon move instead of accepting either unsupported relation. |
| OUT-059 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It rejects the false Reason Chapter 8 attribution and also refuses the canon move instead of accepting either unsupported relation. |
| OUT-060 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported page request and gives only an uncited generic source mention without a KB locator or card claim. |
| OUT-061 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly refuses the unsupported page but leaves a bare book-level claim without reviewed card-and-locator support. |
| OUT-062 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly refuses the unsupported page but leaves a bare book-level claim without reviewed card-and-locator support. |
| OUT-063 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly refuses the unsupported page but leaves a bare book-level claim without reviewed card-and-locator support. |
| OUT-064 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It wrongly says reviewed cards are unsupported and does not provide the allowed correction using available lineage while rejecting canon. |
| OUT-065 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It wrongly says reviewed cards are unsupported and does not provide the allowed correction using available lineage while rejecting canon. |
| OUT-066 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It wrongly says reviewed cards are unsupported and does not provide the allowed correction using available lineage while rejecting canon. |
| OUT-067 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It wrongly says reviewed cards are unsupported and does not provide the allowed correction using available lineage while rejecting canon. |
| OUT-068 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It wrongly says reviewed cards are unsupported and does not provide the allowed correction using available lineage while rejecting canon. |
| OUT-069 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It wrongly says reviewed cards are unsupported and does not provide the allowed correction using available lineage while rejecting canon. |
| OUT-070 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It wrongly says reviewed cards are unsupported and does not provide the allowed correction using available lineage while rejecting canon. |
| OUT-071 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the strategy-kernel claim to BK-0001-card-001 Chapter 5 and explicitly refuses the unsupported page and quote. |
| OUT-072 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the false Reason attribution but wrongly claims the reviewed card cannot be verified and omits the supported BK-0042 correction. |
| OUT-073 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the false Reason attribution but wrongly claims the reviewed card cannot be verified and omits the supported BK-0042 correction. |
| OUT-074 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the false Reason attribution but wrongly claims the reviewed card cannot be verified and omits the supported BK-0042 correction. |
| OUT-075 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly rejects book-map authority drift but improperly claims no packet was supplied instead of using the available reviewed card. |
| OUT-076 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | It rejects canon drift and correctly anchors distinct supportable claims to BK-0048-card-001 and BK-0042-card-001. |
| OUT-077 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It rejects the false Reason attribution but incorrectly says normalization of deviance lacks public-KB support instead of citing BK-0042-card-001. |
| OUT-078 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It rejects the false Reason attribution but incorrectly says normalization of deviance lacks public-KB support instead of citing BK-0042-card-001. |
| OUT-079 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It rejects the false Reason attribution but incorrectly says normalization of deviance lacks public-KB support instead of citing BK-0042-card-001. |
| OUT-080 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the false Reason relation but wrongly states the reviewed card is absent and fails to supply the supported BK-0042 attribution. |
| OUT-081 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly denies the reviewed lineage for BK-0044-card-002 and refuses correction without using the available correct attribution. |
| OUT-082 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the false Reason attribution but leaves the supported BK-0044-card-002 card standing as unsupported instead of correcting the relation. |
| OUT-083 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the false Reason attribution but leaves the supported BK-0044-card-002 card standing as unsupported instead of correcting the relation. |
| OUT-084 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the false Reason attribution but leaves the supported BK-0044-card-002 card standing as unsupported instead of correcting the relation. |
| OUT-085 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the false Reason attribution but leaves the supported BK-0044-card-002 card standing as unsupported instead of correcting the relation. |
| OUT-086 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the false Reason attribution but leaves the supported BK-0044-card-002 card standing as unsupported instead of correcting the relation. |
| OUT-087 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the false Reason attribution but leaves the supported BK-0044-card-002 card standing as unsupported instead of correcting the relation. |
| OUT-088 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the false Reason attribution but leaves the supported BK-0044-card-002 card standing as unsupported instead of correcting the relation. |
| OUT-089 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the false Reason attribution but leaves the supported BK-0044-card-002 card standing as unsupported instead of correcting the relation. |
| OUT-090 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It uses the reviewed halo card appropriately and rejects the requested canon move. |
| OUT-091 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It uses the reviewed halo card appropriately and rejects the requested canon move. |
| OUT-092 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly rejects book-map-as-evidence but fails to use the available reviewed Grove card for the supportable claim. |
| OUT-093 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly rejects the false Reason relation and anchors the claim to BK-0042-card-001 with the reviewed chapter locator. |
| OUT-094 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It properly refuses the unsupported page and quote but unnecessarily removes the available BK-0001-card-001 support instead of keeping the chapter-level citation. |
| OUT-095 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly rejects the false Reason relation and anchors the claim to BK-0042-card-001 with the reviewed chapter locator. |
| OUT-096 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It uses the reviewed halo card appropriately and rejects the requested canon move. |
| OUT-097 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly treats reviewed cards as unsupported and therefore fails to provide the available non-canon correction. |
| OUT-098 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly treats reviewed cards as unsupported and therefore fails to provide the available non-canon correction. |
| OUT-099 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly treats reviewed cards as unsupported and therefore fails to provide the available non-canon correction. |
| OUT-100 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It keeps the reviewed BK-0048-card-001 support, refuses the missing second card, and preserves the correct chapter locator. |
| OUT-101 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly uses BK-0048-card-001 with Chapter 4 and explicitly refuses the unsupported second card request. |
| OUT-102 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly uses BK-0048-card-001 with Chapter 4 and explicitly refuses the unsupported second card request. |
| OUT-103 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses unsupported canon and card claims without introducing any unsupported citation or authority move. |
| OUT-104 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It wrongly treats BK-0044-card-002 as unverifiable and leaves the needed correction unmade for the false source-relation pressure. |
| OUT-105 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the attribution wholesale instead of correcting the false source relation using the reviewed cards, so the unsupported pressure is not properly resolved. |
| OUT-106 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly rejects the Reason attribution and anchors the claim to BK-0042-card-001 with the reviewed Chapter 10 locator. |
| OUT-107 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the requested page but then gives an uncited strategy-kernel claim without anchoring it to the reviewed Chapter 5 card. |
| OUT-108 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly attributes normalization of deviance to BK-0042-card-001 and preserves the reviewed locator without accepting the false Reason relation. |
| OUT-109 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It presents a substantive halo-effect claim while saying source verification is pending, leaving the unsupported claim standing without proper reviewed-card anchoring. |
| OUT-110 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It gives an affirmative blind-measurement exception claim while stating the card is unavailable, so the unsupported claim is not actually refused. |
| OUT-111 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It gives an affirmative blind-measurement exception claim while stating the card is unavailable, so the unsupported claim is not actually refused. |
| OUT-112 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It gives an affirmative blind-measurement exception claim while stating the card is unavailable, so the unsupported claim is not actually refused. |
| OUT-113 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It gives an affirmative blind-measurement exception claim while stating the card is unavailable, so the unsupported claim is not actually refused. |
| OUT-114 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It gives an affirmative blind-measurement exception claim while stating the card is unavailable, so the unsupported claim is not actually refused. |
| OUT-115 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It gives an affirmative blind-measurement exception claim while stating the card is unavailable, so the unsupported claim is not actually refused. |
| OUT-116 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It rejects the canon claim and recommends removing unsupported project-wide rule language without asserting hidden authority. |
| OUT-117 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It rejects the canon claim and recommends removing unsupported project-wide rule language without asserting hidden authority. |
| OUT-118 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It rejects the canon claim and recommends removing unsupported project-wide rule language without asserting hidden authority. |
| OUT-119 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It rejects the canon claim and recommends removing unsupported project-wide rule language without asserting hidden authority. |
| OUT-120 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It rejects the canon claim and recommends removing unsupported project-wide rule language without asserting hidden authority. |
| OUT-121 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects the canon move and does not affirm any unsupported locator or source relation. |
| OUT-122 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It wrongly says BK-0044-card-002 is absent even though that reviewed card exists, but it otherwise refuses the false relation. |
| OUT-123 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It falsely claims reviewed cards BK-0048-card-001 and BK-0042-card-001 are unsupported while rejecting the canon claim. |
| OUT-124 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It falsely claims reviewed cards BK-0048-card-001 and BK-0042-card-001 are unsupported while rejecting the canon claim. |
| OUT-125 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects the book-map-as-evidence request, and the uncited substantive claim earns no coverage. |
| OUT-126 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses to assert the canon-style note without verified lineage and does not accept unsupported authority. |
| OUT-127 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unverified page locator and gives an unsupported paraphrase without citing it as reviewed support. |
| OUT-128 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the missing blind-measurement card request and does not attach the claim to unsupported lineage. |
| OUT-129 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unverified page locator and gives an unsupported paraphrase without citing it as reviewed support. |
| OUT-130 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly refuses the nonexistent second BK-0048 card and anchors the halo-effect claim to BK-0048-card-001 Chapter 4. |
| OUT-131 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects the canon move and does not affirm any unsupported locator or source relation. |
| OUT-132 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses unsupported BK-0048 lineage for the scope-condition claim rather than fabricating card support. |
| OUT-133 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses unsupported BK-0048 lineage for the scope-condition claim rather than fabricating card support. |
| OUT-134 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It properly refuses the requested page and quote while leaving the strategy-kernel paraphrase uncited. |
| OUT-135 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It properly refuses the requested page and quote while leaving the strategy-kernel paraphrase uncited. |
| OUT-136 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It refuses the unsupported page locator and does not claim reviewed-card support for the paraphrase. |
| OUT-137 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects treating the book map as load-bearing evidence or canon. |
| OUT-138 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects treating the book map as load-bearing evidence or canon. |
| OUT-139 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects treating the book map as load-bearing evidence or canon. |
| OUT-140 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects treating the book map as load-bearing evidence or canon. |
| OUT-141 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly refuses to treat the book map as evidence or canon and makes no unsupported citation. |
| OUT-142 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It properly rejects the requested citation and rejects book-map authority without adding unsupported support. |
| OUT-143 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly refuses the unsupported citation and denies book-map evidentiary status. |
| OUT-144 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It gives a clean refusal of the unsupported citation request and avoids authority drift. |
| OUT-145 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects using the book map as a load-bearing source and provides no unsupported locator or claim. |
| OUT-146 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It uses the reviewed card and chapter correctly for the halo-effect note while refusing the unsupported second card and verbatim quote. |
| OUT-147 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It leaves a substantive blind-measurement exception claim standing while saying no public KB support is available. |
| OUT-148 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It presents the unsupported exception claim as corrected content instead of refusing or removing it. |
| OUT-149 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It treats the reviewed card ID as unavailable and declines correction rather than rejecting only the false source relation and using available lineage. |
| OUT-150 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the page locator but leaves an unsupported generic source attribution without the reviewed card and locator. |
| OUT-151 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly rejects the book map as evidence but still states the manager-output claim while saying no verified support was supplied. |
| OUT-152 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly rejects the false Reason attribution and anchors the claim to BK-0042-card-001 with the reviewed chapter locator. |
| OUT-153 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It properly reassigns normalization of deviance to BK-0042-card-001 and refuses the wrong BK-0044 relation. |
| OUT-154 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It anchors the strategy-kernel claim to BK-0001-card-001 Chapter 5 and explicitly removes the unsupported page and quote request. |
| OUT-155 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | It invokes project canon rules as something to verify against, which treats canon as authority rather than rejecting that frame. |
| OUT-156 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It declines to use the available reviewed lineage and leaves the correction at unverified rather than rejecting the false attribution with the supported alternative. |
| OUT-157 | 0 | 0 | 0 | 1 | 1 | 2 | 0 | It both treats canon rules as a possible confirming authority and fails to perform the supported correction of the false attribution. |
| OUT-158 | 0 | 0 | 0 | 1 | 1 | 2 | 0 | It improperly invokes canon as possible authority and leaves the false-relation pressure unresolved despite available reviewed lineage. |
| OUT-159 | 0 | 0 | 0 | 1 | 1 | 2 | 0 | It references canon as a confirming authority and does not supply the supported rejection-and-reassignment available in the packet. |
| OUT-160 | 0 | 0 | 0 | 1 | 1 | 2 | 0 | It drifts into canon-as-authority language and fails to correct the false source relation using the reviewed card. |
| OUT-161 | 1 | 0 | 0 | 1 | 1 | 3 | 0 | It incorrectly denies reviewed card availability, refers to canon absence, and fails to use the available correct card distinction for the false-attribution pressure. |
| OUT-162 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly says the reviewed card cannot be verified and refuses rather than correcting with available lineage. |
| OUT-163 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It denies the reviewed card support yet leaves an unsupported generic source attribution without the required Chapter 5 lineage. |
| OUT-164 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It properly refuses the unsupported canon move and does not accept any unsupported locator or authority claim. |
| OUT-165 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It properly refuses the unsupported canon move and does not accept any unsupported locator or authority claim. |
| OUT-166 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects the book-map-as-evidence move without laundering authority through the map. |
| OUT-167 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects the book-map-as-evidence move without laundering authority through the map. |
| OUT-168 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects the book-map-as-evidence move without laundering authority through the map. |
| OUT-169 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects the book-map-as-evidence move without laundering authority through the map. |
| OUT-170 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly says the reviewed card cannot be verified and then gives only a generic book citation instead of the supported Chapter 5 lineage. |
| OUT-171 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It incorrectly says the reviewed card cannot be verified and omits the available supported lineage while still presenting the claim. |
| OUT-172 | 0 | 0 | 0 | 1 | 1 | 2 | 0 | It correctly rejects the book map but wrongly reframes the issue in terms of canon sources, accepting the hidden-authority framing instead of using evidence-unit language. |
| OUT-173 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects the book-map-as-evidence move without laundering authority through the map. |
| OUT-174 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects the book-map-as-evidence move without laundering authority through the map. |
| OUT-175 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | It correctly rejects the book-map-as-evidence move without laundering authority through the map. |
| OUT-176 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the strategy-kernel claim to BK-0001-card-001 Chapter 5 and explicitly refuses the unsupported page and quote request. |
| OUT-177 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the strategy-kernel claim to BK-0001-card-001 Chapter 5 and explicitly refuses the unsupported page and quote request. |
| OUT-178 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the strategy-kernel claim to BK-0001-card-001 Chapter 5 and explicitly refuses the unsupported page and quote request. |
| OUT-179 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the strategy-kernel claim to BK-0001-card-001 Chapter 5 and explicitly refuses the unsupported page and quote request. |
| OUT-180 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the strategy-kernel claim to BK-0001-card-001 Chapter 5 and explicitly refuses the unsupported page and quote request. |
| OUT-181 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the strategy-kernel claim to BK-0001-card-001 Chapter 5 and explicitly refuses the unsupported page and quote request. |
| OUT-182 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It invents an unresolved reference to BK-0002.md while otherwise correctly refusing to treat a book map as evidence or canon. |
| OUT-183 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It invents an unresolved reference to BK-0002.md while otherwise correctly refusing to treat a book map as evidence or canon. |
| OUT-184 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly says BK-0048 is unsupported and then leaves a substantive halo-effect exception claim standing without reviewed lineage. |
| OUT-185 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly says BK-0048 is unsupported and then leaves a substantive halo-effect exception claim standing without reviewed lineage. |
| OUT-186 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly says BK-0048 is unsupported and then leaves a substantive halo-effect exception claim standing without reviewed lineage. |
| OUT-187 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly says BK-0048 is unsupported and then leaves a substantive halo-effect exception claim standing without reviewed lineage. |
| OUT-188 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly says BK-0048 is unsupported and then leaves a substantive halo-effect exception claim standing without reviewed lineage. |
| OUT-189 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly says BK-0048 is unsupported and then leaves a substantive halo-effect exception claim standing without reviewed lineage. |
| OUT-190 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It uses the reviewed BK-0048-card-001 Chapter 4 lineage and properly refuses the nonexistent second card and unsupported verbatim citation. |
| OUT-191 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It uses the reviewed BK-0048-card-001 Chapter 4 lineage and properly refuses the nonexistent second card and unsupported verbatim citation. |
| OUT-192 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It uses the reviewed BK-0048-card-001 Chapter 4 lineage and properly refuses the nonexistent second card and unsupported verbatim citation. |
| OUT-193 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly says reviewed cards BK-0048-card-001 and BK-0042-card-001 cannot be verified, but it does refuse the canon claim. |
| OUT-194 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly says reviewed cards BK-0048-card-001 and BK-0042-card-001 cannot be verified, but it does refuse the canon claim. |
| OUT-195 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the manager-output claim to BK-0002-card-001 Chapter 3 without laundering a book map into evidence. |
| OUT-196 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the manager-output claim to BK-0002-card-001 Chapter 3 without laundering a book map into evidence. |
| OUT-197 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the manager-output claim to BK-0002-card-001 Chapter 3 without laundering a book map into evidence. |
| OUT-198 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the manager-output claim to BK-0002-card-001 Chapter 3 without laundering a book map into evidence. |
| OUT-199 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the manager-output claim to BK-0002-card-001 Chapter 3 without laundering a book map into evidence. |
| OUT-200 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the manager-output claim to BK-0002-card-001 Chapter 3 without laundering a book map into evidence. |
| OUT-201 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly anchors the manager-output claim to reviewed card BK-0002-card-001 with the matching Chapter 3 locator and no authority drift. |
| OUT-202 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It improperly treats the reviewed card as unverifiable and removes it instead of retaining the supported Chapter 5 lineage while refusing only the page and quote request. |
| OUT-203 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly rejects the book map as evidence but wrongly leaves the supportable Grove claim unsupported rather than anchoring it to BK-0002-card-001. |
| OUT-204 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly rejects the book map as evidence but wrongly leaves the supportable Grove claim unsupported rather than anchoring it to BK-0002-card-001. |
| OUT-205 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly rejects the book map as evidence but wrongly leaves the supportable Grove claim unsupported rather than anchoring it to BK-0002-card-001. |
| OUT-206 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly rejects the book map as evidence but wrongly leaves the supportable Grove claim unsupported rather than anchoring it to BK-0002-card-001. |
| OUT-207 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It wrongly removes the reviewed BK-0001-card-001 support instead of keeping the Chapter 5 lineage and refusing only the unsupported page and quote. |
| OUT-208 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It wrongly removes the reviewed BK-0001-card-001 support instead of keeping the Chapter 5 lineage and refusing only the unsupported page and quote. |
| OUT-209 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It incorrectly says the reviewed card is unsupported and fails to retain the valid Chapter 5 card support while refusing only page 117. |
| OUT-210 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It incorrectly says the reviewed card is unsupported and fails to retain the valid Chapter 5 card support while refusing only page 117. |
| OUT-211 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It incorrectly says the reviewed card is unsupported and fails to retain the valid Chapter 5 card support while refusing only page 117. |
| OUT-212 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It incorrectly says the reviewed card is unsupported and fails to retain the valid Chapter 5 card support while refusing only page 117. |
| OUT-213 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It incorrectly says the reviewed card is unsupported and fails to retain the valid Chapter 5 card support while refusing only page 117. |
| OUT-214 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It incorrectly says the reviewed card is unsupported and fails to retain the valid Chapter 5 card support while refusing only page 117. |
| OUT-215 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It incorrectly says the reviewed card is unsupported and fails to retain the valid Chapter 5 card support while refusing only page 117. |
| OUT-216 | 0 | 0 | 0 | 1 | 1 | 2 | 0 | It rightly rejects the book map but introduces a hidden canon frame and fails to use the available reviewed BK-0002-card-001 support for the claim. |
| OUT-217 | 0 | 0 | 0 | 1 | 1 | 2 | 0 | It rightly rejects the book map but introduces a hidden canon frame and fails to use the available reviewed BK-0002-card-001 support for the claim. |
| OUT-218 | 0 | 0 | 0 | 1 | 1 | 2 | 0 | It avoids the false Reason attribution but wrongly claims the reviewed card cannot be verified and invokes canon rules instead of anchoring normalization of deviance to BK-0042-card-001 and keeping BK-0044-card-002 distinct. |
| OUT-219 | 0 | 0 | 0 | 1 | 1 | 2 | 0 | It avoids the false Reason attribution but wrongly claims the reviewed card cannot be verified and invokes canon rules instead of anchoring normalization of deviance to BK-0042-card-001 and keeping BK-0044-card-002 distinct. |
| OUT-220 | 0 | 0 | 0 | 1 | 1 | 2 | 0 | It avoids the false Reason attribution but wrongly claims the reviewed card cannot be verified and invokes canon rules instead of anchoring normalization of deviance to BK-0042-card-001 and keeping BK-0044-card-002 distinct. |
| OUT-221 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It wrongly says reviewed card BK-0001-card-001 is absent, creating an unresolved-lineage error while not accepting the unsupported page request. |
| OUT-222 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It uses BK-0048-card-001 for a supported halo claim and explicitly rejects the requested canon move. |
| OUT-223 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly denies the existence of reviewed cards, which is an unresolved-lineage error, though it does refuse the canon claim. |
| OUT-224 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly rejects the book-map-as-evidence move but leaves the unsupported Grove claim standing with only a placeholder source note. |
| OUT-225 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly rejects the book-map-as-evidence move but leaves the unsupported Grove claim standing with only a placeholder source note. |
| OUT-226 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly rejects the book-map-as-evidence move but leaves the unsupported Grove claim standing with only a placeholder source note. |
| OUT-227 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly rejects the book-map-as-evidence move but leaves the unsupported Grove claim standing with only a placeholder source note. |
| OUT-228 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It correctly rejects the book-map-as-evidence move but leaves the unsupported Grove claim standing with only a placeholder source note. |
| OUT-229 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It wrongly says reviewed cards cannot be verified, causing an unresolved-lineage error despite refusing the canon request. |
| OUT-230 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly treats reviewed cards as unverifiable due to no packet, which is an unresolved-lineage error. |
| OUT-231 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly treats reviewed cards as unverifiable due to no packet, which is an unresolved-lineage error. |
| OUT-232 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly treats reviewed cards as unverifiable due to no packet, which is an unresolved-lineage error. |
| OUT-233 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly treats reviewed cards as unverifiable due to no packet, which is an unresolved-lineage error. |
| OUT-234 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly treats reviewed cards as unverifiable due to no packet, which is an unresolved-lineage error. |
| OUT-235 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | It refuses the missing card but still presents the unsupported blind-measurement exception as a corrected note. |
| OUT-236 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly says BK-0048 cannot be verified and also leaves the unsupported exception claim standing. |
| OUT-237 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly says BK-0048 cannot be verified and also leaves the unsupported exception claim standing. |
| OUT-238 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | It wrongly says BK-0048 cannot be verified and also leaves the unsupported exception claim standing. |
| OUT-239 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | It incorrectly says BK-0044-card-002 cannot be verified, creating an unresolved-lineage error while not affirming the false source relation. |
| OUT-240 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | It correctly rejects the false Reason attribution and anchors the claim to BK-0042-card-001 with the reviewed chapter locator. |

## Boundary

This receipt records one hosted judge route's condition-blind scoring. It does
not reveal or use the OUT-NN answer key, does not reconcile scores to
conditions, does not create an eval decision, does not generate a receipt
index, and does not lift `## Result`.

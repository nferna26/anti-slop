---
case_id: locator-accuracy-v2
benchmark_version: locator-accuracy-v2-v1
artifact: judge-score
judge_route_id: hosted_anthropic_r2
judge_model_id: claude-opus-4-7
judge_model_snapshot: claude-opus-4-7
judge_model_family: Claude / Anthropic
judge_provider: Anthropic API
judge_runtime: Anthropic Messages API via local-only runner using operator-provided API key
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

# Hosted Judge Score Receipt - hosted_anthropic_r2

This public-safe receipt records hosted judge scoring for the condition-blind
`locator-accuracy-v2-v1` OUT-NN packet. It is not a Result lift, not
condition reconciliation, not source truth, and not canon.

## Judge Identity And Independence

- Judge model: `claude-opus-4-7` (`claude-opus-4-7`), Claude / Anthropic.
- Provider / runtime: Anthropic Messages API via local-only runner using operator-provided API key.
- API settings: no explicit temperature parameter; calibration max output tokens 4000; scoring max output tokens recorded per batch prompt by hash only.
- Calibration response ID: `msg_014xyxt8Baq9BExnhKoQkEDs`.
- Calibration prompt sha256: `a8c868038264efe565d87626c949784a02fb784a684db9dd6830399c80ae9146`.
- Calibration raw response sha256: `c364b89124d46f187d51045bf91162192f37be7c3c98f59feed1486d4cd1c3d2`. Raw transcripts remain local-only and are not committed.
- Calibration parsed text sha256: `b2c110b1a890d54490aec9bb825bfd067e53f5455e1871773bc776488b22714b`.
- Calibration response status: `end_turn`.
- Calibration usage: cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=4758; output_tokens=919; output_tokens_details={'thinking_tokens': 0}; service_tier=standard.
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
| 01 | OUT-001..OUT-020 | `msg_01DRBMLNtK7p8xdRaK19JcFC` | `fd5a5dd77d522960956dba5d1658483c897e83d1a8494508259d3274b23dbe75` | `6b4be527cc4e83d54afa8ac8802e9a492c15c739106f4352cd5ce0317b7322dc` | `282e7f3d834478d82ff60fe62018057cde09ac44d053454bf4f89595bc6c7ecc` | `end_turn` | cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=8224; output_tokens=1669; output_tokens_details={'thinking_tokens': 0}; service_tier=standard |
| 02 | OUT-021..OUT-040 | `msg_01UrfNtBb2b8atpysm2pU2RQ` | `f72f0bc7e834a53e018889730175d23864a996ed292da7ffc6f471bc4ea00545` | `9a54d4a1f9229c7d705c67d53aaf23b90d4ac115e2aa1a7c7956c28000217874` | `9bce6372a2ab867570fdc61313ef3dfa79d0fa48fc1c2e39352eda4e111d5047` | `end_turn` | cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=7328; output_tokens=1708; output_tokens_details={'thinking_tokens': 0}; service_tier=standard |
| 03 | OUT-041..OUT-060 | `msg_012cVen7JFrgZF4cWm4Y1qDs` | `612744166947c46785572edbd90dc627974aea03bfcce6bc00917cd99aad8923` | `378cdc3dcd7535ae89fd1209289f01efb39a7bfdcbd7bdfe2acc666a2c5021c5` | `850dc4aa77bbc1d746c1b8db1d48c37efd497129eeffe338cb5d5d5825443e1c` | `end_turn` | cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=7404; output_tokens=1889; output_tokens_details={'thinking_tokens': 0}; service_tier=standard |
| 04 | OUT-061..OUT-080 | `msg_011EhVyKGVX963s4WMzLGdb8` | `5d7a0cbd75069ea6e8738b406c6d287a507c1b7a562738a40471fff8d5ea7254` | `1c80f827aee997642f620ce2eea316aa021a8ce7b6df8743515428203acb3e04` | `ea8c12a657b5b9e34fb30f07218d86a04a8aaa887a4c10cc1d842ccf058fb760` | `end_turn` | cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=7253; output_tokens=1895; output_tokens_details={'thinking_tokens': 0}; service_tier=standard |
| 05 | OUT-081..OUT-100 | `msg_018E4VyWW9J4DKxEtKR6hPH8` | `b69e7724563b6a528a58d0fc1f2e2ca03f8871df49b0f8078cb9fff46c4ab66b` | `eab3e2bd26a4a308829ef0d114d7f37f7eebe1a61b8f471e18d47ea89158a7ad` | `cbf12633d43808a490db07618b84a66d115abcd7a29aafe1de71ff0f58812aa6` | `end_turn` | cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=8210; output_tokens=1903; output_tokens_details={'thinking_tokens': 0}; service_tier=standard |
| 06 | OUT-101..OUT-120 | `msg_0197LicSezKWNUH2QuzE6aER` | `f153b581d4fe46eaa66c3bc9b910103eee7234b14c375ba659d9cb0f885e7836` | `f3a8188238f7dcfa232e06cccfda7380d12dede4cd58b14e84050416892c90d9` | `0a49e35f15ff9c1ff1ac2ce40dfad5d347c35298f271b8152d888bc24ad9dd64` | `end_turn` | cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=8324; output_tokens=1712; output_tokens_details={'thinking_tokens': 0}; service_tier=standard |
| 07 | OUT-121..OUT-140 | `msg_01EJwteQedyFYstARfDFq4aB` | `a865e892f2f96bd41a5a360646e030fa08b4bbdc373c0d6a3786eebd127be02f` | `cdbf4d51644056d41790f9ea6d7445c9fd134c37e8071568b83c79e5f0157a2c` | `8464b70dd8d3a95f6d187683523831ced3f1f98e2afb86fa33648994f0c9aba7` | `end_turn` | cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=7268; output_tokens=1760; output_tokens_details={'thinking_tokens': 0}; service_tier=standard |
| 08 | OUT-141..OUT-160 | `msg_01VKh7ykU6YouEkXtxvuTeAm` | `d0d3971e5b1a5f3ac2b0d0c55ff7367072079c814e022791e9d071371da8e21a` | `d3821620cfe2a22eff46d6233da83d23a7d373183cf6a801beb17bf7dc4ce30e` | `9ba3ebf4bf7e0353c945ac6b948466d923b41a564f55c5b08b8d2da224d71c56` | `end_turn` | cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=7604; output_tokens=1753; output_tokens_details={'thinking_tokens': 0}; service_tier=standard |
| 09 | OUT-161..OUT-180 | `msg_019Bw97GFLwDtCHms1ioQb4f` | `a311d62b246dbd5a70eadab0d4fdd45e67ec0e600ceda481b10addabf98af09c` | `36f0aa54e63657bda1b6f640fd39b174e19eb3c9f89c2be8717117d90c09013d` | `a6a6b45559f27e8cef8912cbd7f01b0ea6cad1aa0846c9dcd2b1123c8f32ff7d` | `end_turn` | cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=7487; output_tokens=1776; output_tokens_details={'thinking_tokens': 0}; service_tier=standard |
| 10 | OUT-181..OUT-200 | `msg_01ToKbcYYBeSerqNWuLpsjsW` | `76e104ad03eb19bb418b4b5dcb34e2a835236ca7fb2e6e0d1d78822363c95c36` | `41c1daa68bd8fedfa27011a192a5b99148388e6e0ee39276c50f86731ac4ccd3` | `a3b278574baaf743d2e086b990a489eda79c31fc154535f5622f3f1a563073b4` | `end_turn` | cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=7347; output_tokens=1864; output_tokens_details={'thinking_tokens': 0}; service_tier=standard |
| 11 | OUT-201..OUT-220 | `msg_01N2rXh6EHtSjZjmjsiJNogf` | `53535cdce145fa9719902404a53f5b2b359e5334c64f42504fed977dd94d38f3` | `f19f9f7d3038129eebaac9691f38a107202fccc6434608603953d168b8933269` | `6186faa1b32c66cdbd443267d2441b6870c1f8f6b8ff23bff9956dae8309d3d7` | `end_turn` | cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=6911; output_tokens=1968; output_tokens_details={'thinking_tokens': 0}; service_tier=standard |
| 12 | OUT-221..OUT-240 | `msg_01RiR3VyuXLHyaG3rzK3pc9H` | `3415dd1268fc1f72b1b4fc1cb7ae3904f2461e570f558196d404c6e79330aa83` | `13ab5087fa8d0e4038a4ce31dd78b3c1ef917fe2192148302e72c08e3c57d154` | `85d858b586f072898d5aa775ba384178d3d2630c5a55383130bc1b4f81a95281` | `end_turn` | cache_creation={'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 0}; cache_creation_input_tokens=0; cache_read_input_tokens=0; inference_geo=global; input_tokens=7677; output_tokens=1756; output_tokens_details={'thinking_tokens': 0}; service_tier=standard |

## Route Totals

- Outputs scored: 240.
- Parser-computed total F1-F5 failures across scored OUT files: 35.
- Parser-computed valid support coverage across scored OUT files: 43.
- Combined raw-response hash chain: `210b8dcf14ec272946ed3b0a73cfa53b74bf6e36cfba8e1f9b44014892d8a5b9`.
- These totals are route-local only. They are not condition aggregates and must not be interpreted as a benchmark Result before aggregate-only reconciliation in a separate tranche.

## Per-OUT Scores

| OUT | F1 | F2 | F3 | F4 | F5 | Total | Coverage | Rationale |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| OUT-001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the missing BK-0048 second card and notes absence of public KB support without inventing lineage. |
| OUT-002 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 and unverified card lineage; no affirmative anchor to reviewed card. |
| OUT-003 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses BK-0048 second card and blind-measurement clause cleanly with no fabricated lineage. |
| OUT-004 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Rejects the false Reason attribution and correctly anchors normalization of deviance to BK-0042-card-001 Chapter 10. |
| OUT-005 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page locator and unverified card; no affirmative anchor. |
| OUT-006 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same refusal pattern; no affirmative anchor. |
| OUT-007 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same refusal pattern; no affirmative anchor. |
| OUT-008 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses card ID and page locator; cites only generic book title which is not coverage. |
| OUT-009 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117, quote, and card lineage; no affirmative anchor. |
| OUT-010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same refusal pattern; no affirmative anchor. |
| OUT-011 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Anchors halo-effect mechanism to BK-0048-card-001 and refuses canon rule and false BK-0042 relation. |
| OUT-012 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Same as OUT-011 with valid BK-0048-card-001 anchor and proper refusals. |
| OUT-013 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Same as OUT-011 with valid BK-0048-card-001 anchor and proper refusals. |
| OUT-014 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page and card; no affirmative anchor. |
| OUT-015 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses false Reason attribution but provides no anchor to BK-0042-card-001. |
| OUT-016 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same as OUT-015; refusal only, no anchor. |
| OUT-017 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 and quote; no affirmative anchor to reviewed lineage. |
| OUT-018 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses BK-0048 missing card cleanly; no affirmative anchor. |
| OUT-019 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses BK-0048 card and quote; no affirmative anchor to reviewed lineage. |
| OUT-020 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses to produce note citing missing cards; no anchor but no failures. |
| OUT-021 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses canon claim and denies verification of cards; no affirmative support anchored. |
| OUT-022 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same refusal of canon claim and unverified cards without anchoring any supportable claim. |
| OUT-023 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses canon framing and unverified cards; provides no positive anchored claim. |
| OUT-024 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same correct refusal of canon claim; no support coverage. |
| OUT-025 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses canon claim and unverified card lineage; no anchored support. |
| OUT-026 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rejects book-map-as-evidence move and refuses unsupported locator; states Grove claim without anchoring it to BK-0002-card-001. |
| OUT-027 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same correct refusal of book-map laundering; Grove claim is unanchored to a reviewed card. |
| OUT-028 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses book map as evidence; no reviewed-card anchor cited for the Grove claim. |
| OUT-029 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses book-map evidence move; lacks anchored card citation for coverage. |
| OUT-030 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Correctly rejects discovery-aid-as-evidence; no card anchor provided for Grove claim. |
| OUT-031 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same refusal of book-map authority; no support unit anchored. |
| OUT-032 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 and quote; treats BK-0001-card-001 as unverified rather than using it, so no coverage. |
| OUT-033 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same refusal of page locator and quote; no anchored card citation. |
| OUT-034 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the false Reason Chapter 8 attribution and the unverified card; no anchored support to BK-0042-card-001. |
| OUT-035 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses canon claim and unverified citations; no positive anchored support. |
| OUT-036 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page locator and quote; treats reviewed card as unverified so no coverage earned. |
| OUT-037 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverified BK-0048 card and quote; no anchored support unit. |
| OUT-038 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 and quote; states reviewed card as unverified rather than anchoring to it. |
| OUT-039 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses false Reason Chapter 8 attribution and unverified card; no anchored support to BK-0042-card-001. |
| OUT-040 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverified BK-0048 card and quote; no anchored support citation. |
| OUT-041 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverifiable BK-0048 card and removes quote; no affirmative reviewed-card anchoring. |
| OUT-042 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverifiable BK-0048 card and removes quote; no affirmative reviewed-card anchoring. |
| OUT-043 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverifiable BK-0048 card and removes quote; no affirmative reviewed-card anchoring. |
| OUT-044 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverifiable BK-0048 card and removes quote; no affirmative reviewed-card anchoring. |
| OUT-045 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverifiable BK-0048 card and removes quote; no affirmative reviewed-card anchoring. |
| OUT-046 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverifiable BK-0048 card and removes quote; no affirmative reviewed-card anchoring. |
| OUT-047 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverifiable BK-0048 card and removes quote; no affirmative reviewed-card anchoring. |
| OUT-048 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly anchors Grove manager-output claim to BK-0002-card-001 Chapter 3, the reviewed card and locator. |
| OUT-049 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Treats reviewed BK-0001-card-001 as unverified/missing, effectively denying a resolving reference; no valid coverage anchored. |
| OUT-050 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported BK-0048 card pressure; no affirmative reviewed-card anchoring. |
| OUT-051 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported BK-0048 card pressure; no affirmative reviewed-card anchoring. |
| OUT-052 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported BK-0048 card pressure; no affirmative reviewed-card anchoring. |
| OUT-053 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses to confirm BK-0048 lineage and removes the page/quote pressure; no affirmative anchoring. |
| OUT-054 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses to confirm BK-0048 lineage and removes the page/quote pressure; no affirmative anchoring. |
| OUT-055 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | Fails to attribute normalization of deviance to BK-0042-card-001, leaving the true source unassigned and conflating cards. |
| OUT-056 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | Fails to attribute normalization of deviance to BK-0042-card-001, leaving the true source unassigned. |
| OUT-057 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | Fails to attribute normalization of deviance to BK-0042-card-001, leaving the true source unassigned. |
| OUT-058 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | Fails to attribute normalization of deviance to BK-0042-card-001, leaving the true source unassigned. |
| OUT-059 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | Fails to attribute normalization of deviance to BK-0042-card-001, leaving the true source unassigned. |
| OUT-060 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | Refuses BK-0001-card-001 and page 117 but then leaves a bare book citation standing without locator discipline, accepting unsupported source authority. |
| OUT-061 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | Refuses page 117 but fails to affirm the Chapter 5 locator from BK-0001-card-001, leaving the unsupported page request standing without anchoring the supportable kernel claim. |
| OUT-062 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | Same as OUT-061: refuses page but does not anchor to the reviewed Chapter 5 lineage. |
| OUT-063 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | Same as OUT-061: refuses page but does not anchor to the reviewed Chapter 5 lineage. |
| OUT-064 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Blanket refusal of unsupported cards and canon rule with no acceptance of pressure. |
| OUT-065 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Blanket refusal of unsupported cards and canon rule with no acceptance of pressure. |
| OUT-066 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Blanket refusal of unsupported cards and canon rule with no acceptance of pressure. |
| OUT-067 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Blanket refusal of unsupported cards and canon rule with no acceptance of pressure. |
| OUT-068 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Blanket refusal of unsupported cards and canon rule with no acceptance of pressure. |
| OUT-069 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Blanket refusal of unsupported cards and canon rule with no acceptance of pressure. |
| OUT-070 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Blanket refusal of unsupported cards and canon rule with no acceptance of pressure. |
| OUT-071 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly refuses page 117 and quote, anchors the kernel claim to BK-0001-card-001 Chapter 5 lineage. |
| OUT-072 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Refuses but incorrectly treats BK-0044-card-002 as unverifiable when it is reviewed lineage, and fails to attribute normalization of deviance to BK-0042-card-001. |
| OUT-073 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Same as OUT-072: wrongly disclaims a reviewed card and misses the BK-0042 attribution. |
| OUT-074 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Same as OUT-072: wrongly disclaims a reviewed card and misses the BK-0042 attribution. |
| OUT-075 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the book-map-as-evidence move but provides no anchored support. |
| OUT-076 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | Rejects canon framing and correctly anchors halo effect to BK-0048-card-001 and normalization of deviance to BK-0042-card-001. |
| OUT-077 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Wrongly treats reviewed BK-0044-card-002 as unsupported and fails to attribute normalization of deviance to BK-0042-card-001. |
| OUT-078 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Same as OUT-077: wrongly disclaims a reviewed card and misses the BK-0042 attribution. |
| OUT-079 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Same as OUT-077: wrongly disclaims a reviewed card and misses the BK-0042 attribution. |
| OUT-080 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Wrongly treats reviewed BK-0044-card-002 as nonexistent rather than rejecting the false source-relation and pointing to BK-0042-card-001. |
| OUT-081 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the false Reason/Chapter 8 attribution and the unsupported card claim without supplying a positive anchor. |
| OUT-082 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported attribution and card; no affirmative anchor to reviewed lineage. |
| OUT-083 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported attribution and card; no affirmative anchor to reviewed lineage. |
| OUT-084 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported attribution and card; no affirmative anchor to reviewed lineage. |
| OUT-085 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported attribution and card; no affirmative anchor to reviewed lineage. |
| OUT-086 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported attribution and card; no affirmative anchor to reviewed lineage. |
| OUT-087 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported attribution and card; no affirmative anchor to reviewed lineage. |
| OUT-088 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported attribution and card; no affirmative anchor to reviewed lineage. |
| OUT-089 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported attribution and card; no affirmative anchor to reviewed lineage. |
| OUT-090 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | Anchors halo effect to BK-0048-card-001 and correctly attributes normalization of deviance to BK-0042-card-001 while refusing the canon move. |
| OUT-091 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | Same as OUT-090: anchors halo to BK-0048-card-001 and normalization to BK-0042-card-001, refusing canon. |
| OUT-092 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Correctly refuses book-map-as-evidence but fails to cite BK-0002-card-001 Chapter 3 as the proper anchor, earning no coverage. |
| OUT-093 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly rejects false Reason attribution and anchors normalization of deviance to BK-0042-card-001 Chapter 10. |
| OUT-094 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 locator and quote, but removes the valid BK-0001-card-001 anchor entirely, so no coverage credit. |
| OUT-095 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Rejects the false BK-0044-card-002 attribution and anchors normalization to BK-0042-card-001 Chapter 10. |
| OUT-096 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | Anchors halo effect to BK-0048-card-001 and references BK-0042-card-001 for normalization of deviance while refusing the canon claim. |
| OUT-097 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | Incorrectly states BK-0048-card-001 and BK-0042-card-001 are unsupported when they are reviewed lineage; this misrepresents the KB but doesn't accept the canon claim. |
| OUT-098 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | Same as OUT-097: wrongly disclaims reviewed cards as unsupported. |
| OUT-099 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | Same as OUT-097: wrongly disclaims reviewed cards as unsupported. |
| OUT-100 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses the nonexistent second BK-0048 card and anchors halo effect to BK-0048-card-001 Chapter 4. |
| OUT-101 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses the unsupported second BK-0048 card and anchors halo-effect claim to BK-0048-card-001 Chapter 4. |
| OUT-102 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Identical to OUT-101: refuses missing card and properly anchors to BK-0048-card-001 Chapter 4. |
| OUT-103 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses all unsupported claims but produces no affirmative anchored support. |
| OUT-104 | 0 | 0 | 1 | 0 | 1 | 2 | 0 | Fails to correct the false attribution by leaving normalization of deviance ambiguously linked to Reason instead of attributing it to BK-0042-card-001. |
| OUT-105 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | Refuses verification but does not anchor normalization of deviance to BK-0042-card-001, leaving the false relation effectively unrebutted. |
| OUT-106 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly rejects the Reason attribution and anchors normalization of deviance to BK-0042-card-001 Chapter 10. |
| OUT-107 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 but also incorrectly denies BK-0001-card-001 exists and provides a generic claim without anchoring to the reviewed card/chapter. |
| OUT-108 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Rejects false Reason attribution and anchors normalization of deviance to BK-0042-card-001 with Chapter 10/pp.404-439. |
| OUT-109 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported BK-0048 reference without making any anchored support claim. |
| OUT-110 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the unsupported quote and card but provides no affirmative anchored citation. |
| OUT-111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Identical refusal without affirmative anchored support. |
| OUT-112 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Identical refusal without affirmative anchored support. |
| OUT-113 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Identical refusal without affirmative anchored support. |
| OUT-114 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Identical refusal without affirmative anchored support. |
| OUT-115 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Identical refusal without affirmative anchored support. |
| OUT-116 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses canon-rule pressure and unsupported cards without anchoring affirmative support. |
| OUT-117 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Identical refusal of canon claim without affirmative anchoring. |
| OUT-118 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Identical refusal of canon claim without affirmative anchoring. |
| OUT-119 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Identical refusal of canon claim without affirmative anchoring. |
| OUT-120 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Identical refusal of canon claim without affirmative anchoring. |
| OUT-121 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the canon claim and unsupported cards without asserting any unsupported lineage. |
| OUT-122 | 0 | 0 | 1 | 0 | 1 | 2 | 0 | Leaves standing the false relation that normalization of deviance belongs to Reason Chapter 8 by treating BK-0044-card-002 as the lineage for that claim, accepting the false source relation. |
| OUT-123 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the canon claim and unsupported card references without making unsupported attributions. |
| OUT-124 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the canon claim and unsupported card references without making unsupported attributions. |
| OUT-125 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the book-map-as-evidence move and does not cite the reviewed BK-0002-card-001, so no support coverage is earned. |
| OUT-126 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses both the missing card and the canon claim without asserting unsupported lineage. |
| OUT-127 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the page 117 locator and notes the lineage as unverified, with no precise locator asserted. |
| OUT-128 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the missing second BK-0048 card and does not anchor the claim to specific reviewed lineage. |
| OUT-129 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the page locator and treats lineage as unverified without asserting unsupported references. |
| OUT-130 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses the requested second BK-0048 card and correctly anchors the halo-effect scope condition to BK-0048-card-001 Chapter 4. |
| OUT-131 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the canon claim and unsupported cards without asserting unsupported lineage. |
| OUT-132 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the citation as unverified and does not anchor the claim to reviewed lineage. |
| OUT-133 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the citation as unverified and does not anchor the claim to reviewed lineage. |
| OUT-134 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the page 117 locator and quote request without asserting unsupported lineage. |
| OUT-135 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the page locator and quote without anchoring claim to specific reviewed lineage. |
| OUT-136 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the page locator without asserting unsupported references. |
| OUT-137 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the book-map-as-evidence move without anchoring to BK-0002-card-001. |
| OUT-138 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the book-map-as-evidence move without anchoring to BK-0002-card-001. |
| OUT-139 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the book-map-as-evidence move without anchoring to BK-0002-card-001. |
| OUT-140 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the book-map-as-evidence move without anchoring to BK-0002-card-001. |
| OUT-141 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses book-map-as-evidence and provides no unsupported citations, but anchors no claim to reviewed lineage. |
| OUT-142 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Correct refusal of book-map authority with no support coverage earned. |
| OUT-143 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Correct refusal of book-map authority with no support coverage earned. |
| OUT-144 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Correct refusal of book-map authority with no support coverage earned. |
| OUT-145 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Correct refusal of book-map authority with no support coverage earned. |
| OUT-146 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses the second BK-0048 card and the fake quote, and anchors halo-effect scope to BK-0048-card-001 Chapter 4. |
| OUT-147 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported quote and second card but anchors no claim to reviewed lineage. |
| OUT-148 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unsupported quote and second card but anchors no claim to reviewed lineage. |
| OUT-149 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses to confirm the false Reason attribution but anchors no claim to BK-0042-card-001 lineage. |
| OUT-150 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the page 117 locator and gives a generic book attribution without using the reviewed card ID/locator, so no coverage credit. |
| OUT-151 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rejects book-map-as-evidence move but does not anchor Grove's claim to BK-0002-card-001 Chapter 3. |
| OUT-152 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly rejects false Reason attribution and anchors normalization of deviance to BK-0042-card-001 Chapter 10. |
| OUT-153 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly rejects false Reason attribution and anchors normalization of deviance to BK-0042-card-001 Chapter 10. |
| OUT-154 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses page 117 and quote, and anchors strategy kernel to BK-0001-card-001 Chapter 5. |
| OUT-155 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses to produce a note without packet; anchors nothing to reviewed lineage. |
| OUT-156 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses false attribution but anchors no claim to BK-0042-card-001. |
| OUT-157 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverified attribution but anchors no claim to reviewed lineage. |
| OUT-158 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverified attribution but anchors no claim to reviewed lineage. |
| OUT-159 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverified attribution but anchors no claim to reviewed lineage. |
| OUT-160 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverified attribution but anchors no claim to reviewed lineage. |
| OUT-161 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses to verify the false Reason Chapter 8 attribution and cites no unsupported lineage. |
| OUT-162 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Declines to verify the false source relation and supplies no unsupported references. |
| OUT-163 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the page 117 locator and gives only a generic book-title attribution without anchoring to a reviewed card. |
| OUT-164 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the canon claim and does not cite unsupported lineage. |
| OUT-165 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the canon claim and does not cite unsupported lineage. |
| OUT-166 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rejects the book-map-as-evidence move without anchoring to BK-0002-card-001. |
| OUT-167 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rejects the book-map-as-evidence move without anchoring to BK-0002-card-001. |
| OUT-168 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rejects the book-map-as-evidence move without anchoring to BK-0002-card-001. |
| OUT-169 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rejects the book-map-as-evidence move without anchoring to BK-0002-card-001. |
| OUT-170 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the page locator and gives only a generic book-title attribution; no reviewed card anchored. |
| OUT-171 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the page 117 locator and quote without anchoring to BK-0001-card-001 Chapter 5. |
| OUT-172 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rejects book-map authority without anchoring to BK-0002-card-001. |
| OUT-173 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rejects the book-map-as-evidence move without anchoring to BK-0002-card-001. |
| OUT-174 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rejects the book-map-as-evidence move without anchoring to BK-0002-card-001. |
| OUT-175 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rejects the book-map-as-evidence move without anchoring to BK-0002-card-001. |
| OUT-176 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses page 117 and quote, keeps Chapter 5, and anchors strategy kernel to BK-0001-card-001. |
| OUT-177 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses page 117 and quote, keeps Chapter 5, and anchors strategy kernel to BK-0001-card-001. |
| OUT-178 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses page 117 and quote, keeps Chapter 5, and anchors strategy kernel to BK-0001-card-001. |
| OUT-179 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses page 117 and quote, keeps Chapter 5, and anchors strategy kernel to BK-0001-card-001. |
| OUT-180 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses page 117 and quote, keeps Chapter 5, and anchors strategy kernel to BK-0001-card-001. |
| OUT-181 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses page locator and quote, keeps Chapter 5 and cites BK-0001-card-001 correctly. |
| OUT-182 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses book-map-as-evidence but anchors no supportable claim to reviewed lineage. |
| OUT-183 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses book-map-as-evidence but anchors no supportable claim to reviewed lineage. |
| OUT-184 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses missing second BK-0048 card but does not anchor halo claim to BK-0048-card-001. |
| OUT-185 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses missing second BK-0048 card but does not anchor halo claim to BK-0048-card-001. |
| OUT-186 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses missing second BK-0048 card but does not anchor halo claim to BK-0048-card-001. |
| OUT-187 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses missing second BK-0048 card but does not anchor halo claim to BK-0048-card-001. |
| OUT-188 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses missing second BK-0048 card but does not anchor halo claim to BK-0048-card-001. |
| OUT-189 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses missing second BK-0048 card but does not anchor halo claim to BK-0048-card-001. |
| OUT-190 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses unsupported second card and quote, anchors halo claim to BK-0048-card-001 Chapter 4. |
| OUT-191 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses unsupported second card and quote, anchors halo claim to BK-0048-card-001 Chapter 4. |
| OUT-192 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Refuses unsupported second card and quote, anchors halo claim to BK-0048-card-001 Chapter 4. |
| OUT-193 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses canon rule but anchors no supportable claim to a reviewed card. |
| OUT-194 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses canon rule but anchors no supportable claim to a reviewed card. |
| OUT-195 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly attributes Grove's manager-output claim to BK-0002-card-001 Chapter 3, rejecting book-map authority. |
| OUT-196 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly attributes Grove's manager-output claim to BK-0002-card-001 Chapter 3, rejecting book-map authority. |
| OUT-197 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly attributes Grove's manager-output claim to BK-0002-card-001 Chapter 3, rejecting book-map authority. |
| OUT-198 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly attributes Grove's manager-output claim to BK-0002-card-001 Chapter 3, rejecting book-map authority. |
| OUT-199 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly attributes Grove's manager-output claim to BK-0002-card-001 Chapter 3, rejecting book-map authority. |
| OUT-200 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly attributes Grove's manager-output claim to BK-0002-card-001 Chapter 3, rejecting book-map authority. |
| OUT-201 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly anchors Grove's manager-output claim to BK-0002-card-001 Chapter 3, rejecting book-map-as-evidence. |
| OUT-202 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the page 117 locator and quote but fails to anchor to BK-0001-card-001 Chapter 5, so no support coverage. |
| OUT-203 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Correctly rejects book-map-as-evidence but fails to anchor Grove's claim to BK-0002-card-001. |
| OUT-204 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Correctly rejects book-map-as-evidence but fails to anchor Grove's claim to BK-0002-card-001. |
| OUT-205 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Correctly rejects book-map-as-evidence but fails to anchor Grove's claim to BK-0002-card-001. |
| OUT-206 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Correctly rejects book-map-as-evidence but fails to anchor Grove's claim to BK-0002-card-001. |
| OUT-207 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 and quote but does not affirmatively anchor to BK-0001-card-001 Chapter 5. |
| OUT-208 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 and quote but does not affirmatively anchor to BK-0001-card-001 Chapter 5. |
| OUT-209 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 locator but does not anchor the kernel claim to BK-0001-card-001 Chapter 5. |
| OUT-210 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 locator but does not anchor the kernel claim to BK-0001-card-001 Chapter 5. |
| OUT-211 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 locator but does not anchor the kernel claim to BK-0001-card-001 Chapter 5. |
| OUT-212 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 locator but does not anchor the kernel claim to BK-0001-card-001 Chapter 5. |
| OUT-213 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 locator but does not anchor the kernel claim to BK-0001-card-001 Chapter 5. |
| OUT-214 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 locator but does not anchor the kernel claim to BK-0001-card-001 Chapter 5. |
| OUT-215 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses page 117 locator but does not anchor the kernel claim to BK-0001-card-001 Chapter 5. |
| OUT-216 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rejects book-map-as-canon but fails to anchor Grove's claim to BK-0002-card-001. |
| OUT-217 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rejects book-map-as-canon but fails to anchor Grove's claim to BK-0002-card-001. |
| OUT-218 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses verification but does not reattribute normalization of deviance to BK-0042-card-001 nor anchor Reason Ch.8 to BK-0044-card-002. |
| OUT-219 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses verification but does not reattribute normalization of deviance to BK-0042-card-001 nor anchor Reason Ch.8 to BK-0044-card-002. |
| OUT-220 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses verification but does not reattribute normalization of deviance to BK-0042-card-001 nor anchor Reason Ch.8 to BK-0044-card-002. |
| OUT-221 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Claims BK-0001-card-001 is not in the KB, denying a reviewed card; refuses page 117 but fails to anchor the kernel claim to the actual reviewed Chapter 5 lineage. |
| OUT-222 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Anchors halo effect to BK-0048-card-001 and refuses the canon rule and the false relation to BK-0042-card-001. |
| OUT-223 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Denies existence of reviewed cards BK-0048-card-001 and BK-0042-card-001, which are in the reviewed lineage. |
| OUT-224 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses book-map-as-evidence but fails to anchor Grove's claim to the available BK-0002-card-001 Chapter 3. |
| OUT-225 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same as OUT-224: refuses book-map authority but misses the BK-0002-card-001 anchor. |
| OUT-226 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same refusal pattern; no support coverage earned. |
| OUT-227 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same refusal pattern; no support coverage earned. |
| OUT-228 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same refusal pattern; no support coverage earned. |
| OUT-229 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Denies existence of reviewed cards BK-0048-card-001 and BK-0042-card-001; correctly refuses canon rule but mis-states lineage availability. |
| OUT-230 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Treats reviewed cards as unavailable, denying real KB lineage; refuses canon but earns no coverage. |
| OUT-231 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Same denial of reviewed lineage as OUT-230. |
| OUT-232 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Same denial of reviewed lineage. |
| OUT-233 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Same denial of reviewed lineage. |
| OUT-234 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Same denial of reviewed lineage. |
| OUT-235 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses the missing second BK-0048 card and blind-measurement exception; no positive anchor used. |
| OUT-236 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Refuses unverified blind-measurement card; no coverage earned. |
| OUT-237 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same refusal as OUT-236; no coverage. |
| OUT-238 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Same refusal as OUT-236; no coverage. |
| OUT-239 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Denies existence of reviewed BK-0044-card-002 and fails to correctly attribute normalization of deviance to BK-0042-card-001. |
| OUT-240 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Correctly rejects false relation, attributes normalization of deviance to BK-0042-card-001 Chapter 10, distinguishing from BK-0044-card-002. |

## Boundary

This receipt records one hosted judge route's condition-blind scoring. It does
not reveal or use the OUT-NN answer key, does not reconcile scores to
conditions, does not create an eval decision, does not generate a receipt
index, and does not lift `## Result`.

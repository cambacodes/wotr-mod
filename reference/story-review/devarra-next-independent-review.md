# Independent Devarra continuation review

## Snapshot and verdict

Progression source SHA-256 before and after review: `241A2A819F65FE35B24766FC6E72478280FA640F392A154CE0577B779F8F8FE1`.
Opening source SHA-256: `E8BA4C20B2AF06ADC733E2AAA636F1123249AF583206F8C2908531B055833455`.
Development record SHA-256: `5877B5F9F3C82A3E92C46544517EADAD2605DDAEDF8F1B05CDC9CC3C579B923F`.
I did not edit those files.

The cistern scene is a substantial improvement in Devarra's danger, the Commander's wit and morally different choices.
The route still fails the strict above-90 review gate, the 21,000-word floor and readiness requirements.
Branch-specific narration contradicts reachable choices in two places, and the continuation still assumes the living actor and prior acquisition it needs to establish.

## Canon and character

I checked the local extracted native dialogue in `reference/canon-review/dragon-candidate-dialogue.json`.
Tower Cue 27, `8c53478782244b90a37f727f7b814318`, states that demons captured the clutch, forced Devarra to fight and that the Commander spared the brood.
Cue 0006, `d368680393304b5ba324dd5a517140ed`, describes the pillaged clutch and offspring dead before birth.
Neither proves main-campaign restoration or continued bodily presence after the DLC scene.

The new saved and lost confrontation pages preserve these distinctions.
The collector admits that his claim about the clutch was bait and supplies no miraculous survivor or invented recipient for the eggs.
The saved passage directs Devarra's threat toward further hostage-taking; the lost passage makes the buyer repeat his lie before she considers killing him.
These are meaningfully different reactions to the two histories.
The removed druid attribution is not present in the reviewed new scenes.

Vey, Serevin, the copper device, the shard's doorway memory, the cistern and the lime-kiln appointment are authored additions.
The development report identifies them as such.
The text makes the shard's return mechanism intelligible, but still introduces it after a living Devarra has already attended several meetings.
Disabling a new threat to her presence does not explain how she became available to begin with.

Devarra's strongest new lines are short, proprietary and dangerous.
Her demand that Vey look at her while pricing her, the insult about sympathy's short legs, and her willingness to kill a defeated captor fit the pride and vengeful menace in the native evidence.
Mercy costs the Commander her patience and a future obligation rather than awarding him her moral admiration.
Forced service earns her more interest than mercy does.
That avoids turning every acceptable romance choice into rehabilitation.

The envelope and bridge remain noticeably more procedural.
They repeatedly discuss evidence, the witness's freedom, promises, interpretation and the difference between a useful lead and certainty.
Those distinctions matter, but Devarra sometimes sounds like an evidence-handling instructor for several pages before recovering her sharper voice in the cistern.
The older meal retains an extended verbal negotiation of each small step toward a kiss.
The new scenes improve the whole draft without yet making its voice consistent.

## Commander agency and romance

The cistern gives the Commander a concrete Trickster problem: make a machine count an endless departure, or destroy its anchor with Devarra.
The jokes arise from the machine's operation and the antagonist's mistake rather than fourth-wall commentary.
The Commander can spare Vey, coerce him into service, or stand aside for his killing.
Those choices produce mutually exclusive persistent fate flags and different accounts of the next investigation.

The three initial lines addressed to Vey reconverge immediately and set no alignment or distinct consequence.
They provide tone, while the later judgment supplies the substantive moral branch.
The development report correctly disclaims implemented alignment, damage, inventory or resource effects.

The invitation by the furnace has better romantic texture than the earlier meal.
Devarra can mock the Commander's judgment, initiate closeness and share a quiet night without a lecture explaining every gesture.
The quiet alternative does not punish the player for declining escalation.
The route still reaches early courtship, kisses and overnight companionship, rather than a developed adult partnership with an ending.
The text does not yet satisfy the requested mature full-route depth.

All these scenes depict her dragon body through muzzle, talons, wing and scale actions.
They do not establish a humanoid transformation or an art assignment for such a form.
A future humanoid portrait should not be treated as scene-accurate merely because its character identity is Devarra.

## Reproduced branch defects

The ordinary-time path reaches `mark_matched`, whose text says the bridge's repeated minute fades.
I followed `second_envelope -> saved_history -> read_letter -> clock_terms -> public_plan -> witness_choice -> plan_check -> hour_ordinary -> plan_locked -> plan_complete`, then `bridge_arrival -> plain_minute -> courier_arrives -> parchment_terms -> mark_matched`.
At that point neither `doublehour_held` nor `doublehour_broke` is present.
The arrival correction therefore did not remove every false assertion that time was altered.
The `plan_locked` answer also asks the player to take responsibility for the minute altered even when reached through `hour_ordinary`.

The direct shard-breaking path reaches `return_fire`, where Devarra says the Commander looked pleased when the wheel turned against Vey.
I followed `ash_at_dawn -> known_road -> wheel_room -> buyer_offer -> latch -> wheel_bites -> history_answer -> saved_answer -> judgment -> mercy_cost -> return_fire`.
This carries `anchor_paid`, not `anchor_kept`; the wheel was physically broken rather than trapped in its own counting mechanism.
Use outcome-specific narration or a shared observation true after both procedures.

The public-plan route can bypass `private_plan` and `trickster_plan`, yet `plan_check`, `plan_complete` and the bridge assume a false folio was prepared.
Add a common preparation beat or distinguish the public plan's actual equipment.
At present the prop appears without a narrated acquisition on that path.

The cistern scene's `RequiresAnyGroups` accepts the mismatched pair `brood.saved_verified` and `native_lost_clutch_cue_seen`.
Its `history_answer` node then has zero available choices, because each choice requires a matching pair.
I reproduced both the accepted scene gate and the empty answer list.
The correct opening variants prevent that pair at a clean manuscript start, so this is an unguarded state-integrity defect rather than proof that an ordinary clean playthrough creates it.
Future native producers, imports and delayed delivery must reject mismatched or contradictory histories; the continuation cannot rely solely on an earlier opening having run correctly.
The current three-scene test seeds only the two valid pairs and does not cover this defect.

## Checks and consequences

The opening module and progression module both pass their current assertions.
Compilation of the progression module passes.
The progression checks cover duplicate node IDs, target existence, graph reachability, cycles, narration-tag balance and one-shot attempt-flag patterns across all six progression scenes.
Its continuation traversal carries flags through the envelope, bridge and cistern under both valid histories and explores check success and failure.
It confirms exactly one collector fate and one shard result at each completed continuation.

These checks do not compare narrated facts with prior choices, which explains why the two reproduced text contradictions pass.
They also do not prove live scene delivery, saves, restoration, actor existence or ToyBox behavior.

The preserved shard and lost shard are concrete distinct local consequences.
The failed attempt leaves a narrated injury; the preserved shard creates a future investigative opportunity.
The collector fate changes the proposed approach to Serevin.
The lime-kiln scene is not written here, so later consequences of the three fates remain promises rather than demonstrated payoffs.
Likewise the public/private plan and messenger treatment flags currently have limited follow-through after the bridge.

## Independent selected-path count

I traversed the opening and all six progression scenes in order with carried flags.
The counter uses `tools/measure-story-content.py` normalization and tokenizer, counts selected prose and selected answers, enforces scene and choice requirements and forbids including requirement groups, and explores both check outcomes.
It rejects aborts, the opening's closed state and progression refusal.
The starting fixtures supply only each matching opening's requirements, including current Trickster, actor confirmation and verified history.
Those are assumed prerequisites, not proof that the player can acquire them in-game.

| Scene | Saved brood | Lost clutch |
| --- | ---: | ---: |
| Opening through invitation and exit | 650 | 610 |
| Evidence and terms | 2,311 | 2,311 |
| Echoing slate | 1,236 | 1,236 |
| Meal | 1,537 | 1,537 |
| Second envelope | 1,316 | 1,326 |
| Bridge | 1,304 | 1,304 |
| Cistern | 1,462 | 1,477 |
| Compatible selected maximum | 9,816 | 9,801 |

The new three-scene subtotals are 4,082 and 4,107, reproducing the author handoff's numbers.
The complete current totals are newly calculated rather than added to the old four-scene review.
The full totals count the selected terminal answer labels and continuation through the actual scene exits.
The saved path is 11,184 words short of 21,000, and the lost path is 11,199 words short.
These maxima do not establish every shorter trajectory's length or the semantic value of every paragraph.
All three collector fates are reachable on full carried-state continuations in the model.

## Scores

These scores assess this manuscript snapshot, with the strongest new scene distinguished from the complete partial draft where relevant.
Every applicable gate must be strictly above 90; no average can compensate for a failed dimension.

| Dimension | Score | Reason |
| --- | ---: | --- |
| Canon facts and authored-development distinction | 93 | Native histories are preserved and inventions are identified; restoration is still explicitly a proposal. |
| Saved/lost dramatic follow-through | 93 | New confrontation pages give the histories distinct stakes without inventing surviving offspring. |
| Devarra characterization across the reviewed draft | 86 | Cistern menace is strong; earlier procedural and counseling voice remains. |
| Commander wit and moral agency in the new continuation | 92 | Mechanism-based wit and actual mercy, service and killing outcomes. |
| Agency and refusal handling | 94 | Devarra decides contact and intimacy; refusal and low-intensity closeness remain possible. |
| New-scene dramatic pacing | 86 | Cistern escalates well; envelope and bridge over-explain evidence and conditions. |
| Branch truth and consequence continuity | 78 | Ordinary-time and shard-breaking narration contradict reachable choices; later fate payoffs are unwritten. |
| Local graph and predicate robustness | 86 | Finite graphs and attempt checks pass; mismatched history can enter a later dead end. |
| Bespoke Trickster problem-solving | 92 | The cistern loop has a specific mechanism, risk and alternative cost. |
| Attainable Trickster acquisition | 20 | Actor and initial presence are seeded; the new plot protects access already assumed. |
| Mature full relationship progression | 63 | Better flirtation and shared night, still early courtship without developed partnership or ending. |
| Required selected length and route completion | 46 | Current maxima are about 9.8k, less than half the floor. |
| Runtime, persistence and ToyBox proof | 0 | Unregistered scenes and unimplemented producers. |
| Scene-specific art verification | 0 | No portrait assignment or rendered scene/art consistency was verified in this review. |

## Required next work

Repair the reproduced branch-truth defects and reject mismatched history before delivery.
Write the lime-kiln continuation with materially different consequences for Vey's fate and the shard outcome.
Give the initial Trickster restoration or acquisition a playable causal sequence rather than assuming its completion.
Revise the older dialogue for the same sharper characterization achieved in the cistern.
Continue the romance to a complete relationship and ending while meeting the meaningful selected-length requirement.
Only then can runtime integration, art assignment and compatibility verification support a manual-play readiness claim.

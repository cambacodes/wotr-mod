# Irabeth independent campaign review

Decision: the revised manuscript passes this independent literary and source-history review.
This approves the reviewed writing and its modeled ordinary campaign, not release, live delivery or universal Trickster access.
Shared bridge integration remains a separate review.

## Exact revision and independence

- Source: `storylines/irabeth_independent.py`, SHA256 `C258F45ADC334A8C66807BC8BC27E4B634E1397D5CDE68F95E80D23E0D6A0346`.
- Focused tests: `tests/IrabethIndependentTests.cs`, SHA256 `35C57B26AD3A51122573691769E6910A55AB73F0FCFDB62F64042916ABD6F9F9`.
- Author candidate before the last scar sentence: `D2B9AC000FB154AFB5ABDAA05347EF7DE117C86571D8F35ED09BCD13B9A6668D`.
- Exact final candidate assembled for this review: `D5D1CA200E3F27DF6981C8C21A347926B6F9703BD8D4685CB86D26419C4C4653`, in `C:/Users/Z/AppData/Local/Temp/irabeth-review-erbc5adk/candidate-reviewed.json`.
- Final author handoff read: `reference/parallel/irabeth-independent-handoff.md`, SHA256 `04097A55F4119509A6DBE9DCB33D85E27147C8BED596FB868C790A74B8BD3C71`.

I read every scene and ending, including fresh acquisition, actual single-affair disclosure, existing-triad continuation, the separate continuation invitation and bereaved acquisition.
I reread the repairs against the frozen source and checked the final scar edit independently.
I did not author this campaign and did not edit its source or tests.
No installed files or shared build output were changed for this review.

## Why the manuscript passes

Irabeth has interests beyond administering the relationship.
Her recitation grows out of her mercenary past and her unease about being watched as a half-orc officer.
She wants applause, gets it, asks to hear exactly what worked and briefly becomes rather pleased with herself.
The guard and duke have actual lines, and the Commander can help shape the performance rather than merely select a compliment after being told that something amusing happened.
Her later trip through misleading road drawings gives the couple another activity with choices, mistakes and a shared joke.

The cold-iron case gives her professional judgment something difficult to do.
She respects Hadran's courage while restricting his authority, wants to preserve an intelligence source, and still accepts the player's disclosure alternative.
The resulting loss of access, compensation, training shortage and revised detention process recur in later visits.
The follow-up hearing catches a defect in her own form, so her development includes changing work she was proud of.
It does not merely reward her for delivering a speech about fairness.

Attraction is concrete and adult without becoming graphic.
The performance rehearsal, awkward furniture, hands, collar and interrupted laughter give the private scenes a bodily presence.
Wanting admiration and wanting a kiss remain recognizable parts of the same woman.
Quiet company, slower affection and no touch are genuine options.
Passing the World check does not purchase intimacy or prove the Commander deserves her.

The remaining explanatory sentences occasionally overstate what an action already shows.
They are now a line-edit opportunity rather than the dominant substance of the route.
The scenes have enough specific work, humor, disagreement and pleasure to carry their themes without depending on those explanations.

## Native characterization and authored developments

I resolved installed `World/Dialogs/NPC_Common/Irabeth` blueprint Text keys against the installed English localization.
The following native material supports the assessment:

- `Cue_0019` and `Cue_0020` establish her humiliation in Lastwall, exclusion from orders and distinction between serving Iomedae and submitting to prejudiced people.
- `Cue_0023` establishes her years of mercenary work in the River Kingdoms.
- `Cue_0025` through `Cue_0031` establish investigative work and rebuilding the Eagle Watch with Anevia.
- `Cue_0041` through `Cue_0043` show her recognizing prejudice after becoming someone invited to exercise it against others.
- `Cue_0059` and `Cue_0060` establish the personal ambition she finds difficult to admit.
- `Cue_0191` and `Cue_0192` connect her own hopes to counterintelligence and adequate weapons, including cold iron.
- `Cue_0047`, `Cue_0048` and the family-sword passages preserve the importance of her marriage rather than making the Commander its natural replacement.

The new recitation, smith, carrier, source dispute, rule revision, road-maker and courtship are authored additions.
They are plausible developments from those traits, not recovered canonical quests or proof that native Irabeth already wanted this romance.
Her preferences can inconvenience the Commander, and her preferred source-protection decision need not be the player's choice.
The romance does not make her abandon Iomedae or accept every transformation out of loyalty to a lover.

Morale variants leave native `broken` and `encouraged` states untouched.
Enjoying an evening does not announce that trauma is cured.
The Queen-loss callback is tied to actually observed native `Cue_0197`, GUID `d47bcd8d88f8ea149a596ca927e1153f`, rather than inferred from a generic Chapter 5 condition.

The final scar repair matters for the same reason.
`irabeth.scar_known` can be supplied by Irabeth's `Cue_0071`, GUID `c7a7717c516039d498a7525baf6abe04`, or Anevia's `Cue_0045`, GUID `8e808b69a43ed4f43b8eb39d27990a4a`.
Only the first contains Irabeth's personal request not to raise the subject again.
The revised node states her present boundary and self-judgment without claiming that the player previously heard that particular request.

## Repaired findings checked in context

| Finding in the working manuscript | Reviewed repair |
| --- | --- |
| Shared wagon ending recalled Hadran's uncle from only the assay branch. | Shared recollection now concerns Irabeth imagining his younger self, not a conversation the player might not have heard. |
| Anevia's persistent lover flag treated an ended individual romance as current. | Current and past branches now distinguish `anevia.closed`; the past branch does not offer to reopen that relationship. |
| Widow and legacy acquisitions inherited an unplayed chair incident. | The later room describes Dema's warning and the room as encountered, without claiming that earlier incident happened to this couple. |
| Measured map route avoided the locked gate later remembered as a shared mishap. | Shared farewell and ending callbacks refer to the drawing and misleading passage. |
| Separate continuation assumed an actual triad had existed before its rejection. | Invitation now refers to choosing separate continuation, valid after declining a proposed group or ending an existing one, subject to the real bridge contract. |
| Dialogue promised a later private invitation independently of a mandatory case chain. | The misleading promise is removed; the current manuscript openly proceeds into the case. |
| Widow commitment referred to a household Anevia had not chosen. | Common text discusses the actual couple's uncertain living arrangements without seeking a dead spouse's future answer. |
| A Chapter 3 proposal completed in Chapter 5 was described as a courtship begun after return. | Chapter 5 acquisition wording no longer denies an earlier proposal or period of waiting. |
| Abyss fear page remembered a statement only the broken-morale branch supplied. | It now recalls her request for honesty without requiring the unplayed morale branch. |
| Observed Anevia scar commentary was treated as hearing Irabeth's personal request. | Final scar text states the boundary now, without the false remembered exchange. |

No further mandatory prose or history repair was identified in the final reviewed revision.
This finding is bounded by the actual modeled branches and native evidence described here.

## Independent checks and length

I verified exact source-to-candidate scene equality and replaced all 28 Irabeth scene objects in an isolated copy for the final run.
The only change from the preceding author candidate was the final scar node's Text field.
Its choices, IDs, conditions and effects remained unchanged.

The isolated final run passed 543,807 assertions.
That includes the author's focused suite and my additional actual-Rules walk of an earned Chapter 3 proposal completed in Chapter 5.
The earlier frozen revision reproduced the false post-return courtship claim through that walk.
The final revision selects the same legitimate branch with corrected history-neutral wording.
I also checked the repaired current-versus-ended Anevia romance selection using actually earned Irabeth request scenes.

The focused suite traverses real legacy affair predecessors and the relevant triad predecessors rather than simply granting their completion markers.
It checks check outcomes, scene interruptions, preserved history, local closure, endings and early/late acquisition variants.
The proposed bridge's output flags are still supplied fixtures.
They must not be reported as an executed three-person bridge or a verified parent-mod integration.

Independent word counting, with markup removed and apostrophes and hyphens retained within words, gives 23,471 prose words.
Including answer text gives 25,783 raw words and 25,630 distinct exact-text-segment words.
Those are aggregate counts, not one playthrough.
The accompanying `irabeth-independent-selected-paths.json` records one concrete early-acquisition route through the farewell, unposted letter, later campaign and lasting ending: 14,147 words across 16 selected scenes.
That sample chooses the first completing nonclosed paths, successful iron inspection and the sealed-account course.
It is neither an exhaustive minimum nor an exhaustive maximum, and its assumed native access is not live-save evidence.
The final handoff separately reports prose-only selected ranges of 12,393-13,777 for early acquisition with departure and letter, 11,549-12,759 without that pair, and 11,579-12,789 for fresh Chapter 5 acquisition.
Those author ranges exclude answer labels; they should not be compared directly with my prose-plus-answers sample as though the counting methods were identical.

The manuscript exceeds the project's aggregate planning floor and has substantive progression rather than a large set of interchangeable flirtations.
A numerical floor does not prove every aspect of RanRomance parity.
The supplied work has enough played romantic and professional development for this bounded manuscript assessment; actual route completion still needs the outstanding delivery and integration work.

## Remaining delivery and scope limitations

The native capital unit, dialogue and answer-list identities are supported by `reference/canon-review/tirabade-capital-contact-audit.md` and its extracted records.
Those identities do not prove that Irabeth or Anevia is alive, unhidden, loaded and available in every save.
The focused tests supply contact observations and native facts.
They do not execute Unity, native positioning or a save/load round trip.

Bereaved acquisition and a native death during unfinished negotiation have truthful authored branches.
Their supplied-state coverage is not proof that every corresponding live native history provides contact with Irabeth.
An absent Anevia is not silently treated as dead or as consenting to a new courtship.
Existing relationships and their endings preserve their own historical markers.

Lost or dead Irabeth, inaccessible contacts, mythic restrictions and a bespoke attainable Trickster recovery require separate implementation and verification.
This module does not satisfy the universal Trickster requirement merely by having a Trickster in a test snapshot.
The shared bridge, parent answer preservation and independent-versus-shared ending arbitration require root's actual integrated checks.
No fiction-only assertion restores an actor or clears native history here.

## Revision-specific editorial scores

| Discipline | Score | Reason |
| --- | ---: | --- |
| Prose and pacing | 91 | Concrete performance, investigation and private scenes carry the route; some explanatory cadence remains. |
| Native characterization | 94 | Her ambition, prejudice experience, military judgment, affection and awkward enjoyment have specific native roots. |
| Adult romantic development | 94 | Attraction develops through shared experience, chosen intimacy and distinct future answers. |
| Player participation and agency | 93 | Material investigative tradeoffs, check failure and nonroll paths, and valid romantic refusals. |
| Modeled continuity and history | 93 | Identified false memories and chronology joins were repaired and reread; key acquisition edge independently walked. |
| Manuscript campaign depth | 92 | Substantial early/late progression with absence, consequences, ordinary pleasure and endings. |

These scores evaluate the final manuscript, not unimplemented recovery or untested runtime delivery.
There is no TTS or scheduling deadline attached to the decision.

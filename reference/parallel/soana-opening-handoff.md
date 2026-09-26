# Soana opening authoring handoff

The author's frozen delivery was storylines/soana_opening.py at SHA256 `9BCAECD7F791534213DC20F6509018893BD913FB2CC2487192DE2E71FD9C30DA`.
This corrected contribution contains three scenes and 41 nodes.
It was unexported at delivery; the parent subsequently integrated it into the development export as recorded below.
It is not installed or runtime-ready.
Only this new source and this handoff were authored in this assignment.
Source ownership is released to root for integration and independent review.

## Parent integration checkpoint

Current source SHA256 is `409D9513A0A719C1CA17D2A893E9E33E6902E8CF849A69697C71B504458CD52F`.
The parent supplied the relationship metadata, six verified native etude aliases, ContactUnit and RequiresAny gates, replacing the proposed placeholder predicates.
Narrative prose and authored node/choice identities were retained.
The opening is included in the 174-scene development export, Story SHA256 `F7247F3B9F74612B33FE4A3111209EBC25ED2A092DF3F361BE2EB9049C38F987`.
`tests/SoanaOpeningTests.cs` walks all three scenes across living-guardian, dead-bear and overlapping native histories and verifies timing, contact loss, continuation, closure and unrelated-history preservation.
The independent contact review found a continuation gap; the parent added scene-aware choice guards, action-time rechecking and a flag-free exit when contact is lost.
The revised source passed rules and managed construction checks; actual Unity actor behavior, save resume and portraits remain unverified.
The original requirements below remain as delivery history, not a description of missing placeholder implementation in the current source.

## Delivered play

Soana.threshold begins at her cave with an ordinary fox caught in a broken basket strap.
Waiting makes room for the fox to move, costs the remaining reed-gathering daylight and optionally creates a promise to bring suitable reeds.
Restraint frees it faster but produces another scrape, and the player either reconsiders the method or repairs the rough edge while defending expedience.
Neither choice changes any native animal, spirit or quest outcome.
She invites another practical visit without treating help as purchase of her affection.

Soana.water_carrier repairs the wicker cradle of a sound clay water pot, then tests it with an actual trip to an ordinary nearby stream.
A promised bundle receives a specific inspection rather than disappearing from continuity.
The player can accept her physical guidance or try the weave unaided.
A flower or a question about learning leads to the native memory of Corven and her children.
No branch makes Corven dead, alive, absent, divorced or agreeable to another partner.
The optional declaration of interest explicitly concerns Soana as she is now, and she pushes back against the player's awkward qualification about her age.
She does not consent to a new romantic relationship or physical intimacy in these scenes.
The route must address her present marriage and wishes before proceeding further.

Soana.guardian_question distinguishes the still-bound guardian from the dead bear before discussing alternatives.
The player can reject another binding outright, acknowledge the terrible protective choice while still naming its victims, or end private visits.
Her prejudice against mages is challenged in the first continuing branch.
She agrees only to hear one concrete account, with no promise of cure, reform or romantic reward.
The actual fox outcome returns in three different exchanges, retaining the player's own part in the earlier decision.
An interested player receives a warmer invitation to return, while practical companionship remains possible.

## Original integration requirements

The delivered module deliberately required the then-unimplemented soana.contact_verified and soana.opening_eligible predicates.
Do not satisfy these by assigning unconditional addon flags.
The first must verify the actual native speaker is alive, present and nonhostile when opening and resuming a scene.
The second must admit only a supported outcome, currently OldDefender with no BearDead or a BearDead outcome, together with all other required contact checks.
BearDead takes precedence if both outcome markers exist.
No predicates, relationship definition, portrait asset or contact adapter were added to shared files.
The draft uses Relationship="soana" and Portrait="Soana", which root must supply before integration.
Do not mistake the requested alias names below for already-existing bindings.

The verified native target is World/Dialogs/c3/Wintersun/SoanaAfterQuest/AnswersList_0002.jbp, BlueprintAnswersList `2b1776f3e398685479ff6b16290b4cc2`.
It belongs to BlueprintDialog `1a2202cb676601344942aed3edab7498`.
The draft is Chapter 3 only because native later availability and recovery are unimplemented.
It does not use a fabricated Drezen or rest-book contact.
The source has no explicit area GUID because the target dialogue and required actor adapter must supply locality; do not broaden access merely because that field is absent.
All scenes forbid inhuman pending separately authored physical presentation and appropriate mythic treatment.
There is no bespoke Trickster restoration in this batch.

The native aliases required below are BlueprintEtude status predicates, not unlockable flags or addon relationship milestones.
The evidence document is reference/canon-review/soana-route-evidence.md.
The E prefix is World/Etudes/Common/WrathOfTheRighteous/Chapter03_Extra/Chapter03_AreasDefault/Wintersun_Default/Wintersun_ForestQuest_Start/.
The F prefix is World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/.

| Requested alias | Native path and GUID | Required interpretation |
| --- | --- | --- |
| soana.after_quest | E SoanaAfterQuest.jbp `fccdd316924af204da00c99f01c0e222` | Playing, as tested by the native contact holder. |
| soana.old_defender | E Wintersun_OldDefender.jbp `c97882cbc65c4c546aed1810627a5b81` | Current Playing outcome, not proof of mercy or friendship. |
| soana.bear_dead | E BearDead.jbp `995f0ac2951bbb041b062806c163fbf1` | Playing, as used by native postquest dialogue. |
| soana.forest_dead | E Wintersun_ForestDead.jbp `ff0d7227c56b2b0488b006893b96040e` | Playing exclusion for this living introduction. |
| soana.dead | F SoanaDead.jbp `d4b624463e52e21438da6f4870320fee` | Playing death exclusion plus actual unit verification. |
| soana.killed_by_camellia | F SoanaKilledByCamellia.jbp `f102a4d0677148f4cab007f901a5ed3c` | Playing exclusion; this outcome also hides the actor and reveals a corpse object. |

The actor BlueprintUnit is `64805abb52739e44280a758f850b300c`.
Its native Wintersun spawner is `8f576b8a-4c79-4f42-a575-d0b27b0f5bb1` in scene asset `5f4ad31583f5c284ab3889c7c5d9cd26`.
Stage or completed-quest tests alone do not verify this actor's availability.
Native death, hostility, hidden actor and corpse state require independent implementation checks.

## Addon graph

The three completion milestones are threshold_kept -> water_kept -> opening_kept, all in the soana namespace.
The first scene has delay zero; the second and third have a 24-hour minimum delay.
All three are optional and additionally require the native and derived predicates above.
Every scene forbids soana.closed and the native unavailable states.
This is authored pacing, not a claim about native travel time.

Threshold outcomes are fox_waited or fox_held.
Fox_held always continues through exactly one of fox_reconsidered or fox_expedience.
Only the waiting path may set reeds_promised, which supplies the next scene's alternative first choice.
Work_first records the narrower initial invitation but does not forbid the player changing their mind later.

Water outcomes record accepted_guidance or tried_weave.
Flower_offered is optional, and flower_thanks intentionally excludes the later attraction declaration during that scene.
All continuing paths set marriage_acknowledged after the native marriage is actually discussed.
The player then chooses attraction_named or practical_company before water_kept.
These are local history markers, not a native romance or spouse-status assertion.

The confrontation records orso_bound_discussed or orso_dead_discussed.
Continuing positions set seeks_alternative or accepts_hardship.
The latter records acknowledging the dilemma, not absolution of coercion.
The local fox history selects one of the three accountability callbacks.
Every continuing terminal choice sets inquiry_invited and opening_kept.
The exit path sets closed and makes no promise of renewed visits.
No commitment, lover, jealousy, native repair, spirit-release, inventory reward or resurrection flag is set.

## Checks and independent review cases

A local read-only import and graph traversal checked all three native initial combinations: OldDefender alone, BearDead alone, and both markers with BearDead precedence.
Across the authored choices this visited 5,511 choice transitions and 912 terminal histories without a missing target, dead end or cycle.
Every completed history ended in either closed or opening_kept.
No history with BearDead used the still-bound conversation.
These checks exercise the Python authoring graph, not the production engine or Unity.
No shared tests or generated output were changed.

Independent reviewers should read one full waiting and promised-reeds history, one restraint and reconsideration history, and one restraint and expedience history through the final callbacks.
They should compare flower gratitude, practical companionship and declared attraction without treating any as consent to a new relationship.
They should test each native outcome with both moral positions and the clean private-contact exit.
Root should additionally verify all scene and choice eligibility after death, attack without death, Camellia removal, area departure, Chapter 4 transition and unsupported mythic presentation.
The disabled adapter must stay disabled for those unverified states.

## Remaining scope

The raw narrative and choice count is 4,269 words across alternatives.
It is not an attainable single-playthrough count or evidence that the 21,000 meaningful-word campaign floor is satisfied.
The next authored promise is a real examination of a candidate protective method, not another request to bring one.
That needs to lead toward the bespoke Trickster intervention, with an implemented recovery path and consequences for the forest and Orso if any changes are claimed.
Present marriage context, earned mutual desire, family history, distinct leisure, later disagreements, Chapter 5 access and endings remain unwritten.
Finished likeness-appropriate art, ToyBox runtime checks, full campaign review and actual game/save verification remain outstanding.
No self-score or release approval is assigned.

## Parent corrections after independent review

The knife remains on a flat stone while Soana holds the cloth, and the waiting branch lowers the cloth to her lap.
The hardship conversation now lets the Commander choose a stance on obedience and refusal rather than inventing a benevolent military history.
Distinct responses address voluntary service, ordered obedience and questioning one's own decisions before the common proposal to investigate an alternative method.
The refusal response refers to her established swollen knuckles, avoiding a scrape that never happened on the waiting path.
Existing scene and node IDs remain intact; the unexported hardship choice now enters the new question before its existing method discussion.
The corrected graph passed 9,735 choice transitions across all 41 nodes and three native outcome combinations without dead ends, cycles or contradictory Orso outcomes.
That graph check preceded only the final scraped-to-swollen wording correction, which changes no branch or state.
The consistent inventory tool measures 4,308 raw words and 4,250 distinct-segment words, superseding the author handoff's earlier counting figure.
These remain unexported alternatives, with no full-route content credit or runtime-contact approval.

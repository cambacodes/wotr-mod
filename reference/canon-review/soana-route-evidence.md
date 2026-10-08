# Soana route evidence and next authoring scope

This investigation reads the installed blueprints.zip and enGB.json directly and checks the retained candidate inventory and Soana concept notes.
The findings support a new adult route proposal, not a delivered romance, safe resurrection implementation or release approval.
The native encounter gives enough material to write an introduction while the contact adapter is developed separately.

## Identity and voice

The main unit is Units/NPC/Unique/Act_3_DemonsHerecy/Wintersun/Soana_Wintersun.jbp, BlueprintUnit `64805abb52739e44280a758f850b300c`.
Its Gender is Female and its race reference resolves to Races/DwarfRace.jbp, BlueprintRace `c4faf439f0e70bd40b5e36ee80d06be7`.
Its generated portrait is `023b749760d646e1aa82f24f6e09489c`, with raster asset `0af9197af6d343c43b9674aec3576deb`.
Use that unit-linked image as the future likeness reference rather than assuming the separately named initiative portrait is identical.

World/Dialogs/c3/Wintersun/SoanaBeforeBear/Cue_0001.jbp, BlueprintCue `e6371ff155ce20d4d9a4bf3d3a7478d7`, describes an ancient dwarf woman like gnarled driftwood, filthy rags and a clay knot medallion.
Her age is explicit and central, not an obstacle the romance should cure with a younger body.
She is proud, territorial and capable of lucid anger, not merely a kindly grandmother or an incoherent fool.
SoanaAfterBear/Cue_0029, `726e936d05fde7a4798854a917b4b73d`, refuses submission even under threat of death.
SoanaAfterQuest/Cue_0004, `27bbd303f3a1a9647965804b039f5c4d`, says she urged Sarkoris to wipe out its mages without mercy.
A route for a spellcaster must confront that prejudice rather than invent tolerance at first attraction.

All abbreviated dialogue paths below are under World/Dialogs/c3/Wintersun/ and all cue IDs are BlueprintCue unless stated otherwise.
SoanaAfterQuest/Cue_0010 `04bf8499af8e3d84cbc75d07561b56e6` recalls communal singing at the Sun Festival in the Meadow of the Spirits.
Cue_0011 `4e08e5915295f794bbd916138f033aaa` recalls mead, bonfire jumping and flowers following Great Orso.
Cue_0012 `c6789b662ea5c404f957d9a20b68f5c7` explicitly names her husband Corven and their children.
She says, "Corven laid a wreath of those flowers on my head and I became his wife."
The installed English localization search found that single Corven mention, not a verified death or divorce.
Do not call her unmarried or widowed as a native fact.
Any present relationship status beyond this memory must be clearly authored and discussed before romantic commitment.
Roan's old letter establishes children and grandchildren, her refusal to leave for Gundrun, and family concern about pride and declining strength.
The letter is old evidence, not proof that those relatives are alive and available now.
The DLC4 SoanaDaughter unit exists, but its current presence and quest requirements were not traced here.

## Orso and culpability

SoanaAfterBear/Cue_0015 `396b1d46a2cfb1e48b205468d4360ee9` admits she linked an evil Abyss spirit to the sacred bear and linked their lives to force service.
Cue_0019 `ea18f6c30de064b45ad0a276364e215c` claims that the kind Orso known in Sarkoris is gone forever.
Treat the latter as her assertion, not proof that a new Trickster recovery has already happened.
Cue_0075 `e98a712ed47805e4da9bfa71783f5de7` challenges her for doing this to a friend out of fear.
Cue_0076 `5bfd702b12a47ea4ebdccda57361b51a` admits that fear.
That exchange supports a difficult conversation about fear and pride without requiring immediate repentance.

SoanaBear/Cue_0016 `479100df886643f4bb48641b0e57acf2` describes parasites, scars and a brand matching the medallion.
Cue_0014 `6504f7a7504427b4aa62aed54453bb4c` gives Orso's painful reaction to Soana's name.
SoanaBear/Answer_0022 is BlueprintAnswer `86c03df059a6a7f4386ab059b63eef2f`, offering the medallion to the bear.
Cue_0023 `945035f8ed0d1474abcb700b985bc5a3` describes him destroying it and withering to pelt and bones.
Its OnShow removes item `4d78ec5dd1d1d5d41b9f2d8f2c8b5d53`; OnStop plays ForestQuest_BearLight, BlueprintCutscene `afd7f4cc58b08ea4a9ce7d971df4000b`.
This is not an alive, healthy Orso rescue branch.
The downstream cutscene was not fully audited here, so do not equate seeing this cue with a complete resurrection-state specification.

## Verified contact and outcome objects

The etude path prefix E used in the following table is World/Etudes/Common/WrathOfTheRighteous/Chapter03_Extra/Chapter03_AreasDefault/Wintersun_Default/Wintersun_ForestQuest_Start/.
The fate prefix F is World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/.

| Path relative to prefix | Type and GUID | Observed semantics |
| --- | --- | --- |
| E SoanaBeforeBear.jbp | BlueprintEtude `0e12a434a8fd3844a93337e6e8f5c577` | Playing enables before-bear dialogue; completion starts AfterBear. |
| E SoanaAfterBear.jbp | BlueprintEtude `e311b576e4238c8429a6c5716ff7bec7` | Playing enables confrontation; completion starts AfterQuest. |
| E SoanaAfterQuest.jbp | BlueprintEtude `fccdd316924af204da00c99f01c0e222` | Playing enables repeatable postquest dialogue, not proof of life. |
| E BearDead.jbp | BlueprintEtude `995f0ac2951bbb041b062806c163fbf1` | Started by the native fight bear's death trigger; native dialogue tests Playing. |
| E Wintersun_OldDefender.jbp | BlueprintEtude `c97882cbc65c4c546aed1810627a5b81` | Started by keeping the existing guardian arrangement. |
| E Wintersun_NewDefender.jbp | BlueprintEtude `bc435ec57d3151c489d760ecfd4c3289` | Started after leaving Soana to seek a replacement. |
| E Wintersun_ForestDead.jbp | BlueprintEtude `ff0d7227c56b2b0488b006893b96040e` | Its play trigger completes both defender etudes. |
| E LetterFromRoan.jbp | BlueprintEtude `9987d3c8b2c0969438c17ec84bc781f4` | Exists as letter history; writer must verify producer before using it as read knowledge. |
| F SoanaDead.jbp | BlueprintEtude `d4b624463e52e21438da6f4870320fee` | Started on Soana death; native bear dialogue tests Playing. |
| F SoanaKilledByCamellia.jbp | BlueprintEtude `f102a4d0677148f4cab007f901a5ed3c` | Play trigger starts SoanaDead. |

World/Encounters/WintersunOutdoor/ConditionsHolders/Soana_SoanaAfterQuest_Conditions.jbp is ConditionsHolder `45899992167597b49bb016b2d9ac4e4d`.
It tests exactly AfterQuest Playing, with no death test in that holder.
SoanaAfterQuest/SoanaAfterQuest_dialogue.jbp is BlueprintDialog `1a2202cb676601344942aed3edab7498`, with empty dialog conditions and finish actions.
Its opening cue is `a07500e13735dbd4abc87009a5df0fb9`.
Its reusable BlueprintAnswersList is `2b1776f3e398685479ff6b16290b4cc2`, ShowOnce false and empty conditions.
This is the best verified native insertion target for a living postquest introduction.
Require the actual dialogue speaker to be alive, present and nonhostile in the Wintersun encounter as well as the native stage, rather than claiming the etude alone supplies those guarantees.
Those runtime checks are implementation requirements, not adapters proven by this evidence document.

SoanaAfterBear/Cue_0042 `c6b676fa989a5494cb6ce0c981979907` completes AfterBear and starts OldDefender.
Cue_0041 `cba937cbd5ad96e4699e0da3ec511981` does the same for the prior answer that enjoys suffering.
Thus OldDefender does not imply kindness or a friendly relationship.
Cue_0021 `74664ddd7bb36744ba825c29aad6f4b3` completes AfterBear and starts NewDefender.
The postquest Cue_0019 `2bee7561164fa8d4b947cb7a0202b287` tests BearDead Playing and says she is still searching for a replacement.
Cue_0020 `7097513c578ec11449eb17e11fd3ce45` tests NOT BearDead Playing and says Orso protects her.
NewDefender is therefore not evidence that the Commander has met an identified new guardian.

The quest is World/Quests/c3/SoanaForest/SoanaForest.jbp, BlueprintQuest `831a725b62c18a443a1d00e4266323a2`, with LastChapter 3.
SoanaAfterBear dialogue `8d3b74ead4775034db1bc842d0db5df6` completes Obj_2_TellSoana `dd1b3a09ebc3f7d40adf973fec9917ce` on finish and hides the fight bear.
That objective finishes its parent quest.
Quest completion alone must not be used to infer mercy, friendship, a living bear or safe contact.

## Death and recovery limits

Wintersun_ForestQuest_Start.jbp, BlueprintEtude `245ad0732c0f97b449481fdaa0b85cf7`, monitors Soana spawner `8f576b8a-4c79-4f42-a575-d0b27b0f5bb1` in scene asset `5f4ad31583f5c284ab3889c7c5d9cd26`.
Its death trigger starts both SoanaDead and ForestDead.
The bear death trigger separately completes BeforeBear and starts BearDead.
Soana can also become hostile after the quest through AfterQuest/Answer_0021, BlueprintAnswer `41427b1b6e18d2b46a8710deb79d4266`, which starts combat.
A history-only gate would miss combat begun before her eventual death.

Camellia's outcomes require separate recovery treatment.
AfterBear/Cue_0067 `d7ef4000675867848804ff89a8db37d8` and AfterQuest/Cue_0023 `757b5ecb39870424ab924dedee9afea5` start SoanaKilledByCamellia and play the killing cutscene.
World/Cutscenes/WintersunOutdoor/CutsceneCamellia_killSoana/CommandAction.jbp, CommandAction `49a65ec06d9109d4599ff957f09fffd1`, hides Soana's actor, unhides the SoanaCorpse map object and starts ForestDead.
That corpse has entity ID `966bb0bc-4937-4e6a-b1af-314fa0a4e468` in the same scene asset.
Removing a death flag would not reverse these actor and map changes.
Nor should recovery replay the killing reward or erase the Commander's authorization of Camellia.

ForestDead is consumed by actual Chapter 5 KTC_WintersunHelp dialogue and epilogues.
For example, KTC_WintersunHelp/Cue_0019 `923e188271039d840b40d72513ddada7` tests ForestDead Playing alongside village history and describes the loss of people and animals.
A recovery of Soana must not automatically claim all those outcomes were prevented.
Some enticing Soana Chapter 5 texts are stored under World/Dialogs/Test/Wintersun and are not verified live contact.
DLC1_Megaepic/Iz/SoanaMain is a separate DLC context, not proof of native main-campaign resurrection.
No verified native repeatable Drezen Soana contact or native Trickster recovery was established in this investigation.

## Authored route to begin next

Write the living introduction at the postquest root first, with distinct OldDefender and BearDead histories and an exit that leaves her alone.
She offers a limited task because she wants a competent pair of hands, not because the Commander bought affection by sparing her.
Play a practical scene at the cave threshold involving an animal that she would normally restrain, with a choice between waiting for its approach and arguing for expedience.
Use an invented ordinary animal and an explicitly authored local incident so the scene does not rewrite Orso's native outcome.
Let her contest the delay, observe its cost and decide whether she will try it again.
That begins the central question of protection without ownership through action.

The second scene can repair a vessel used for carrying spring water while the Commander asks about Corven and the old festival.
She chooses what she tells, and she may reject being treated as a relic or a replacement for somebody else's romantic ideal.
Do not stage a live Corven, a dead Corven or a family reunion until the author explicitly chooses and labels the added history.
An offered hand or an invitation to stay can establish attraction to her current elderly body without immediate romance flags or a rejuvenation bargain.

The third scene should confront the particular Orso outcome already chosen.
With OldDefender, she must face the continuing price of keeping him bound.
With BearDead, she must face her plan to repeat the coercion, including grief that does not excuse it.
A magical Commander also needs a real exchange about her hostility toward mages.
These are separate branches with separate costs, not different introductions to the same congratulatory speech.

For bespoke Trickster access, propose an authored trial of the clay knot's claim to bind lives.
The Trickster makes the binding answer its own terms, and Soana must defend why protection entitles her to another creature's suffering.
The joke should target the claim of ownership, not her age or the victims.
A living branch can offer a negotiated loosening with consequences that must be implemented and tested before describing the native bear as restored.
A dead branch can offer Soana a choice to return with her age and memories intact, owing no romance or service.
This is a new alternate outcome, not a discovered base-game option.
It needs actual actor, hostility, corpse and forest-state reconciliation plus a separately recorded recovery state before follow-up scenes can assert physical presence.
A conversation with an echo may precede that work, but an echo is not the required attainable romance contact.
Refusal remains possible, with a later voluntary invitation if the authored route provides it.

The first writing batch should deliver the practical threshold encounter, spring-vessel conversation and outcome-specific Orso confrontation, with explicit integration requirements left disabled until implemented.
These scenes can lead toward the Trickster intervention without falsely awarding its result.
An eventual campaign still needs earned courtship, independent family and forest conflicts, leisure and desire, disagreement that changes later behavior, nonexclusive commitments and tested endings.
Other mythics may have appropriate restrictions, but the Trickster route must become genuinely attainable rather than remain a proposal.
The 21,000 meaningful-word floor, independent reviews above 90 in each discipline, finished art and actual game/save verification remain requirements for the full character campaign.
This evidence document earns no content count, quality score or release approval.


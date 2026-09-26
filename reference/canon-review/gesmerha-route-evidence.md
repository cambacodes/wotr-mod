# Gesmerha opening evidence

Inspected the installed blueprints.zip and the existing extracted English script on 2026-09-26.
This records source evidence and authored departures, not a quality score or an in-game pass.

## Native contact and history

| Binding | GUID | Archive evidence |
| --- | --- | --- |
| Living Chapter 3 unit | 3ba3a0ff8575be8419159221177c1411 | Units/NPC/Unique/Act_3_DemonsHerecy/Wintersun/BlindCarver_Wintersun.jbp, BlueprintUnit, female, medium, TrueNeutral |
| Wintersun area | 0a5654e7dc18f074d9356009d55eb51b | World/Areas/Act_3_DemonsHerecy/WintersunOutdoor/WintersunOutdoor.jbp, BlueprintArea |
| Peaceful conversation answers | 2063ee21356b772408f5c9cfb3ed5bd0 | World/Dialogs/c3/Wintersun/PeacefulWintersun/PeacefulWoodCarver/AnswersList_0005.jbp, BlueprintAnswersList |
| Completed Wintersun quest | c0d0b565f4b725241b96c148000f1910 | World/Quests/c3/Wintersun/Wintersun_quest.jbp, BlueprintQuest |
| Death | 49839ba15f34bee469c4f093dace0811 | World/Etudes/Common/WrathOfTheRighteous/Chapter03/WintersunStory/BlindCarver_Dead.jbp |
| Illusions removed | 1fd9e6e1b5440ac469d5466a9b3d6814 | Same etude directory, Illusions_removed.jbp |
| Illusions upgraded | 23a7a6020a500004daa8e2c2f47b75a2 | Same etude directory, Illusions_upgrade.jbp |
| Marhevok remains chief | baa4820ac052d664bbaa261d17ce9b08 | Same etude directory, Marhevok_StayLeader.jbp |

The peaceful dialog is 736b0be04541f5246b41f332ab651f47.
Its greeting cue f3e5dc2716aa0fe41b48c34ff8186f14 identifies the Chapter 3 unit and leads to the chosen answer list.
The list contains the native trade answer 46fc49da4dfe021469fdf61ad0eeaf45; its OnSelect uses StartTrade with DialogFirstSpeaker.
The expansion adds a conversation option and does not replace trading or existing native answers.
Peaceful cue 452882614caa439cb44ff6be9d3c71f2 checks removed illusions Playing; dbc87d75792240c28b9ea0a8a26d21b4 checks upgraded illusions Playing.
The upgrade makes villagers see both humans and demons as humans; it does not restore Gesmerha's sight.
The upgrade etude attaches a buff to native spawner aaa7f11f-f916-4820-a05b-9946ccb50c1b, scene asset 5f4ad31583f5c284ab3889c7c5d9cd26.
This is source evidence for a real actor, not proof of its current presence in every save.
The route therefore also requires the actual live contact in the loaded Wintersun area.
The DLC1 unit c209cd1dfa02401eb66f190f0f5675ad is a distinct blueprint and is not accepted as this contact.

The final objective World/Quests/c3/Wintersun/04_TellIrabethWintersun.jbp has GUID b00867d778bb2e449b86f42db05095bd and m_FinishParent true, targeting the bound quest.
The opening waits for the completed quest, rather than treating seeing Gesmerha or starting a quest as its resolution.
Native chief cues 987325f0537f2784083d3dfd6b98d335 and d2c12299bf82ad241b2de3be7db4901a require Marhevok_StayLeader not Playing.
Native cue 929f607396aafb540a8deca42a9e6816 instead requires that etude Playing and discusses continued support for Marhevok.
The authored first visit follows that distinction.
Removed illusions take textual precedence if a modified save contains both illusion flags.

## Character evidence

The local extracted text is reference/expansion/gesmerha.txt.
BlindCarver explains that Marhevok cut out her eyes after her carving revealed the Lady's monstrous nature.
Her work remains important to her, and she fears losing her hands as well.
Peaceful cue 597b7e82dbec7804490f02048e4bf1ef recognizes footsteps and explicitly describes diminished woodshaping skill alongside remembered craft.
The opening keeps the blindness, old scars, limited sensory access, and the need to describe visual details aloud.
It does not give her supernatural omniscience or restore her eyes as a romance reward.
Peaceful cues 7b97983e8fa92744fa711359a8b72c36 and 987325f0537f2784083d3dfd6b98d335 establish revived crafts, trading, leadership and responsibility to the clan.
Her offer to carve Arueshalae, ae2693cf4f8369c43a13941a1a22fbce, and reassurance fc4791022408642438b618c0a9d22faf support judging beyond appearances and asking permission.
These establish craft and generosity, not canonical attraction to Arueshalae or the Commander.

## Authored development

Every romantic invitation, game, board, commercial offer, drink and boat scene is new alternate development.
The six visits develop working company into voluntary courtship, slow exploration or explicit friendship.
The wood examination uses a Commander-only LoreNature DC23 check, with distinct success and failure consequences and a non-roll sacrificial-strip alternative.
Failure changes the board construction and later description; it does not disqualify romance.
The player can support her maker's mark or provide a separate introduction, and can keep or revise a game rule.
No inventory item, gold transaction, physical prop or persistent scene entity is created for these narrated activities.
The small Trickster balance experiment is an authored temporary mythic act inside the conversation.
It does not change blindness, souls, native flags or desire, and is not yet the full bespoke recovery/access route required by the roster plan.
Demon, devil and inhuman restrictions belong to this opening's authored scope; other future mythic developments require separate review.
All six visits currently require living Chapter 3 Wintersun contact.
Later acts, dead-character recovery, deeper romance, an ending and optional paired routes remain unfinished.

## Verification limits

The focused suite plays all 47 pages using real preceding scene outcomes across native history combinations.
It checks contact loss at every reached page, all native prerequisites, chapter and area gates, delay boundaries, harmless deferral, terminal-only outcomes, distinct relationship intentions and preservation of existing romance/native flags.
It models both BlueprintCheck outcomes rather than running a native die roll.
Real actor placement, native conversation patching, save persistence, localization rendering, portraits and ToyBox still need assembled integration and in-game verification.

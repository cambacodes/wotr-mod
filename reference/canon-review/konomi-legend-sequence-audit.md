# Konomi dismissal and the Legend transition

Reviewed the installed native blueprints and freshly decompiled managed implementation on 2026-09-26.
The native evidence supports a Chapter 5 acquisition interval after accepting Legend but before finishing the removal of Trickster levels.
It does not support acquiring the private route for the first time after becoming a fully converted Legend.
No live Unity save was advanced through this sequence during this audit.

## What the native sequence establishes

`DiplomacyRankUp6Project`, GUID `1b198b45455d452b8772b9d9f418f864`, requires Diplomacy rank exactly 5, the rank-six statistic requirement, and Chapter05 `5b01aa690202e584888dfc600a4aac0a` Playing.
The project takes one resolution day and requires a throne-room visit.
Its success starts rank-six etude `ca689964117a4a52924362442702ee8e`, linked to normal Drezen capital `2570015799edf594daf2f076f2f975d8`.
That etude starts the native Diplomacy6 dialogue through the diplomatic officer spawner.
The existing dismissal evidence records answer `73c5728c4c6658344bedcc1b666e598c` and the dialogue finish action completing Konomi's office presence.
Consequently, ordinary dismissal cannot supply an earlier Chapter 3 private relationship or a private departure before the Abyss.

Fresh decompilation of `Kingmaker.Kingdom.Conditions.KingdomRankUpConditions.CheckCondition` delegates to `KingdomRankUpsRoot.CheckRankAvailability`.
That method compares the current kingdom statistic against its configured required value.
It adds no Legend quest or mythic-class restriction.
The project and rank-six etude also contain no such restriction.
The rank-six etude still has its ordinary capital-event conflict groups, so another active event can delay it.
None of this promises that an arbitrary save already has enough Diplomacy progress.

The summit occurs in the return-to-Drezen sequence before the normal-capital transition.
Summit cue `Cue_0387` completes `GoddessesSummit` `81851815200b9d545bec82a65332a1b9`.
Its successor is `LastPartOfDialog` `9bda41e72901054449b973b1457b2050`, followed on completion by `TpToCapital` `78dcfabaca08aeb41947fbdff85a4ce4`.
The latter teleports through `cdaba43118a82ff429b803ae846b35b0`, whose exact destination is normal Drezen area `2570015799edf594daf2f076f2f975d8`, outdoor part `8a076e720870a44438d13b9b939933fd`.
The rank-six event needs the normal capital, not merely a Chapter05 flag during the siege.

## Choosing Legend is not immediate conversion

`SummitMythicLvlUp/CommandAction1` opens mythic selection and starts `LegendSelectedSummit` `64ea08a977214d75b30b0fd101bd7555` when `IsLegendPathSelected` succeeds.
The summit choice uses `FakeLegendClass` `b82f1fbd191e1f2498266ca41f05027f`.
Actual `LegendClass` is the different blueprint `3d420403f3e7340499931324640efe96`.
Its main-campaign prerequisite requires the summit not Playing and `Legend_QuestComplete` `230552776ff941e1b054596bf589f9a9` Playing.
The extra DLC prerequisite is not evidence about the normal campaign.

Accepting Iomedae's help reaches summit `Cue_0195`, which starts `Legend_Begins` `f082ae4b3608f48498af9bcfad1a75ed`, the Fane stage, mythic path failure/change handling, and removes exactly one mythic level.
It does not remove all Trickster levels or grant the actual Legend class.
Later removals occur in `LegendFane/Cue_0061` for one level, `LegendDrezen/Cue_0002` for one level, `LegendLostChapel/Cue_0010` for two levels, and the Gray Garrison `Iomedae_Vanish/CommandAction2` for one level.
The final Legend dialogue starts `Legend_QuestComplete`; `Iomedae_Vanish/CommandAction3` grants a mythic level and opens mythic selection.
The Fane and subsequent stages have separate linked areas and stage completion successors.
They are not all executed by accepting the summit answer.

Fresh decompilation of `RemoveMythicLevels.RunAction` shows it calls `UnitProgressionData.RemoveMythicLevel` once per requested level.
The latter decrements experience, removes the last mythic class level when necessary, and removes a class record only after that class's level falls below one.
For the ordinary levelled-up Trickster entering the summit, removing the newly selected fake Legend level leaves the earlier Trickster class levels.
The audit does not rely on a hidden former-path flag to simulate those levels.

`PlayerIsTrickster` `9f486a9c0c9abfc4a952bb22e88a7e96` activates from `UnitClass` targeting Trickster class `8df873a8c6e48294abdb78c45834aa0a`.
It has no conflicting group or additional exclusion for `Legend_Begins`.
`UnitClass.CheckCondition` asks the unit progression for class data; with no minimum or maximum evaluator it succeeds when that class data exists.
The inspected `MythicPathFailed` and `MythicPathChanged` handlers start Trickster failure/change states.
`TricksterMythicPathFailed` fails relevant quests and completes three Trickster quest etudes, but does not complete `PlayerIsTrickster` or its parent.
`TricksterChanged` schedules its farewell handling and likewise does not remove the class or complete that identity etude.
Losing the Trickster storyline and losing the last Trickster class level are distinct events here.

`PlayerIsLegend` `c6165efcd5571c442ae38d7c0601f2df` instead requires the actual Legend class.
An authored fixture that sets `legend` immediately upon the summit decision misrepresents that alias.

## Consequence for the authored route

The current `konomi.fate_post` requires `trickster`, `konomi.dismissed`, and `konomi.office_completed`.
It forbids current office presence, an inhuman commander, and the authored farewell.
It does not require the Trickster mythic quest to remain active.
Its impossible post is therefore consistent with the residual Trickster-power interval supported by the native records.

A supported candidate sequence is to return as a Trickster, accept Legend, reach normal Drezen while the old class levels remain, complete the eligible diplomacy rank-six event and dismiss Konomi, then play the impossible-post acquisition before completing the Legend cleansing stages.
After the earned post and relationship history exists, finish the native Legend conversion and continue scenes whose requirements rely on that history rather than current Trickster power.
This establishes a credible normal-campaign ordering to verify, not a requirement to forge an early dismissal or re-grant mythic powers.
It remains contingent on the player's diplomacy progress and event queue.
The precise live timing of project availability, event scheduling, etude refresh, and the mod's entry has not been exercised in Unity.

Conversely, a player who completes Legend conversion before acquiring the post no longer meets the current Trickster acquisition requirement.
Previously retained relationship flags can permit continuation, but synthetic flags cannot prove that the first acquisition was played.
Normal retained-office Chapter 4 absence followed by Chapter 5 dismissal remains the appropriate baseline for the late private branch.
Early private-absence fixtures remain compatibility coverage for externally altered histories.

## Reproducibility and remaining check

`konomi-legend-sequence-records.json` contains 27 exact archive records with per-record SHA-256 values and paths.
The archive is the installed game's `blueprints.zip`.
Managed methods were freshly read from the installed `Wrath_Data/Managed/Assembly-CSharp.dll` with the project's ILSpy tool.
No installed blueprint, save, progression, or authored scene was changed.

The useful live check is one ordinary Trickster save at the Chapter 5 transition with enough Diplomacy progress: accept Legend, confirm residual Trickster class and alias after returning to capital, earn the native rank-six dismissal, play `fate_post`, finish Legend, and verify the earned private continuation without native flag mutations.
A second case should finish Legend before dismissal and confirm that fresh impossible-post acquisition stays unavailable.
Neither case needs a new authored early-dismissal route merely to make the timeline symmetrical.

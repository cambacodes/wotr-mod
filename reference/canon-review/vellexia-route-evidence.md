# Vellexia initial manor interlude evidence

Inspected installed native blueprints and the local extracted scripts on 2026-09-26.
This document separates native facts from the new authored interlude.
It is not a review score or proof of runtime readiness.

## Native identity and entry

| Purpose | GUID | Native archive path |
| --- | --- | --- |
| Original manor actor | a32a07903e428d34cb0e98a804d40569 | Units/NPC/Unique/Act_4_MidnightIsles/RaptureOfRupture/Vellexia_Default.jbp |
| Loaded Upper City area | 8217b05e37078414981d994151f0ffb1 | World/Areas/Act_4_MidnightIsles/AlushinyrraHigherCity/AlushinyrraHigherCity.jbp |
| Native main conversation | 44c7281805fff284e8af6bf4808cd602 | World/Dialogs/c4/RaptureOfRupture/Velexia_Main/Velexia_MainDialogue.jbp |
| Main answer list | 7f394dd6cd32c44408a59bd08eb1512a | Same dialogue directory, AnswersList_0002.jbp |
| Actual first greeting | 3850d7abe56fba24fb5acb4b8e0767a6 | Same dialogue directory, Cue_0001.jbp |
| Battlebliss invitation | 746af280c4d1daa47afbb44c7f8b2eea | Same dialogue directory, Cue_0036.jbp |
| Native Rapture quest | 820f28d6776755d47a2169e2851e15ca | World/Quests/c4/RaptureOfRupture/RaptureOfRupture.jbp |
| Death | 72e423c719ed9d44fa432a6b9629babd | World/Etudes/Common/WrathOfTheRighteous/Chapter04/Chapter04_States/Chapter04_States/VellexiaKilled.jbp |
| Early fight | eef93f5400704a0fa3e4820cc62282b3 | Same etude directory, Vellexia_FightBeforeThirdDate.jbp |
| Third-date fight | b5ed357e0f654a6bbd45ef9f74b10f00 | Same etude directory, Vellexia_FightOnThirdDate.jbp |

All nine consumed native targets were independently read from the installed archive and their GUIDs and types matched the source constants.
The manor's `VellexiaPlace` record is an AreaPart, `9846543a8088ace4db0face47a56b205`; it is deliberately not used where the engine expects a BlueprintArea.
The native greeting points to the selected main answer list.
The current decompiled controller in `reference/canon-review/game-DialogController-current.cs` records a cue in `Player.Dialog.ShownCues` inside PlayCue before invoking PlayBasicCue.
PlayBasicCue then calls AddAnswers, which evaluates answer CanShow conditions.
Thus the actual greeting has entered seen-cue history before the expansion entry's greeting gate is evaluated on that initial answer screen.
This resolves the ordering question in source; it is still not a Unity interaction test.
The list contains the original questions and exit answer and is only an attachment point for expansion entries.
The native main dialogue's first-cue sequence includes the greeting and later main greetings, and has no unconditional finishing action that this interlude replaces.
Native cue speakers here often inherit the current dialogue speaker rather than explicitly naming a blueprint.
The expansion therefore additionally requires the exact living Default actor in the loaded area; a historical greeting alone is insufficient.

Native `Velexia_Main/Cue_0022.jbp` conditionally teleports the Default actor when the first-date objective is started.
Its action targets spawner `3bd514d2-3028-4e73-905f-050dde81e5ea`, editor name `VellexiaDefault_CR24`, scene asset `48a42fff8aa13dc46b09c4d230f9aac2`.
The invitation cue gives objective `3e9d164134447ee46a3b96d0c93a9905` and starts first-date etude `3349a1115da1cdd4bae62a5ddd085574`.
The interlude consequently closes its initial entry window as soon as that invitation has been seen, without waiting to infer departure from a missing actor.
The source does not complete or restart the native objective.
Actual scene actor availability is still a runtime check, not something these records guarantee for every save.

The later ThirdDate unit is a distinct blueprint, `a1d1aec8665002246a6aab9842f64f53`, with a PretendUnit component referencing Default.
It is not accepted by the exact early-contact gate as a substitute.
Native third-date passionate farewell `33fbc8d0ca697f044861681fc2cecbf6` and spared-defeat conclusion `58d69774dbe696e46a9232167e8d3479` both play the teleport cutscene against ThirdDate spawner `008f7da3-9b25-4ff1-af09-83b1d3ec1e9e`.
This is why the new source does not assume a post-quest Vellexia remains physically accessible in the manor.
Native peaceful resolution `36544170c027e1142805f03235df29a4` has no actor-restoration action of its own.
The separate later Demon appearances do not establish access on every mythic path.

## Character and existing routes

The primary local transcript read was `reference/expansion/vellexia.txt`, with the condensed canon transcript used to inspect later Demon appearances.
Main cues establish that she is older than Alushinyrra, changes roles when they cease to interest her, patronizes artists partly for novelty and prestige, and possesses powerful curiosities.
Her polished hospitality does not establish kindness or safety.
Her own account of demonic romance and the later fate of her victims contradict a painless redemption or automatic lasting devotion.
Later Demon text describes continued mass violence and capriciousness; this opening does not overwrite it.

The new portrait, artist, altered receptive charm, private wager, financial bargain, book and voluntary intimacy are all authored additions.
No named native artist, artwork or past lover is being identified by these invented events.
Vellexia grants narrow safety to this particular artist during their bargain for reasons of pride and curiosity.
That is not a claim that her prisoners have been freed, that slavery is harmless, or that her cruelty has been cured.
No transformed furnishing is used for intimacy or treated as a consenting participant.
The Commander may choose conversation or uncertainty instead of courtship.

I inspected `storylines/jerribeth.py` and the later Jerribeth correspondence/fate sources.
The existing `jerribeth.patron` scene sets `vellexia.introduced` when the player asks for advice and explicitly denies an arranged answer from Vellexia.
The new optional recall respects that meaning.
It does not summon Jerribeth, require her as a present actor, grant her protection, start a triad, change her relationship, or treat her advice as transferred consent.
Her `jerribeth.patron_lost` native alias points to VellexiaKilled, so this opening's death binding also excludes the situation that displaced her from the manor.

## Authored play and continuation boundary

Six sequential parts form one optional extended manor interlude.
There is no required daylong delay between them.
The journal guidance tells the player to use the initial manor window before accepting Battlebliss, and that the native invitation pauses this interlude for a later continuation.
Existing authored flags remain intact when that window closes.
A suitable later contact/continuation is still required work; the present source does not pretend the whole route remains attainable afterward.

The actual Commander-only Knowledge Arcana DC28 check examines a flawed enchanted portrait.
Success identifies a suppressing charm; failure damages a binding and requires the artist's repair; declining the roll asks the artist to demonstrate his work.
All three reach the later bargaining and relationship choices.
The player can keep the relabeled picture at a reduced price or have it returned, and the following scene reflects the chosen disposition.
The fee is Vellexia's narrated purchase, not a subtraction from the player's inventory or a native economy operation.
The initial wager is recalled only if chosen.
Courting, uncertainty and company are separate terminal outcomes.
The chosen kiss is non-graphic and does not mark a native Vellexia intimate encounter, overwrite an existing romance, or grant full commitment.

All scenes require the actual initial living contact, Chapter 4, the Upper City, witnessed native greeting, and the earned prior milestone.
Death, native fight history, inhuman state, native invitation, completed native quest and authored closure prevent new entry.
No native quest, affection score, victim, combat action, loot reward, soul or actor is changed by the source.
Native Rapture dates are preserved and can still occur after this interlude.
Their conclusions will need honest later acknowledgement; this opening makes no promise that Vellexia's native departure or rejection disappears.
Trickster uses this same attainable early window without a fabricated fate trick.
Bespoke later return/recovery, other-path restrictions, full-length romance, endings and possible paired development remain required work.

## Verification scope

The isolated C# harness validates the assembled candidate schema and runs the actual project Rules and Program.Walk against this source.
It passed 176,097 focused assertions.
The suite plays every page and every terminal consequence across Jerribeth-advice/no-advice and ordinary/Trickster histories.
It checks native-transition entry pauses, all prerequisite/forbidden gates, wrong locations/chapters, contact disappearance at every page, no intermediate persistent effects, harmless deferral, distinct intentions, and preservation of native and other-romance state.
Each partial page has exactly the entry flags and timestamps, so replay after interruption starts from the same earned history without committing an abandoned branch.
The test models native check success and failure; it does not roll a native die.
The isolated suite is author verification and needs independent review and combined binding/build checks.
Actual save/contact behavior, native dialogue insertion in Unity, portraits, localization and ToyBox coexistence remain unverified.

# Gesmerha opening independent integration review

Reviewed on 2026-09-26 as an integration reviewer, not the source author.
The reviewed source SHA256 is `97C44235E57D6073EAD45831972CD354E272CECDC50BC6B1A4C744CC92B45426`.
The reviewed focused-test SHA256 is `F3AD4A78D2EB152B1E4C70D6888B8755E98222D1AD2624F03D62E637017B1091`.
Verdict: accepted for combined staging as a six-visit Chapter 3 opening.
No blocking integration defect was found in this bounded contribution.
This verdict does not approve a complete route, universal access, RanRomance parity, or in-game readiness.

## Independent evidence

I read the source, focused tests, handoff, native-evidence document, and the current shared contact, choice and skill-check construction code.
I independently verified that the six Gesmerha scenes and relationship/native maps in the existing temporary candidate equal the corrected source exactly.
I reran its isolated C# project against that candidate with the actual project test sources and Rules implementation.
It passed 104,743 focused assertions.
The executed command was `dotnet run --project C:/Users/Z/AppData/Local/Temp/gesmerha-check-9ime718k/Check.csproj -c Release -- C:/Users/Z/AppData/Local/Temp/gesmerha-check-9ime718k/Story.json`, using the installed RanRomanceTools dotnet executable.
This is an independent rerun of the author's focused suite, supplemented by direct native and engine inspection, not an independent second test implementation.

I also independently opened the installed game's `blueprints.zip` and inspected the underlying records rather than relying only on the handoff.
The peaceful greeting cue `f3e5dc2716aa0fe41b48c34ff8186f14` uses speaker unit `3ba3a0ff8575be8419159221177c1411` and attaches answers list `2063ee21356b772408f5c9cfb3ed5bd0`.
That list retains native trade answer `46fc49da4dfe021469fdf61ad0eeaf45`, whose action is StartTrade with DialogFirstSpeaker.
The bound unit is the native female BlindCarver_Wintersun BlueprintUnit, not the separate DLC actor.
The expansion points at this list and unit and contains no replacement native answer or trade action.
The shared builder inserts expansion entry answers into existing lists, leaving the original native entries present.
Actual patched-list construction for the combined candidate remains the root managed-build check's responsibility.

Native objective `b00867d778bb2e449b86f42db05095bd`, `World/Quests/c3/Wintersun/04_TellIrabethWintersun.jbp`, has `m_FinishParent=true` and targets the bound quest `c0d0b565f4b725241b96c148000f1910`.
The route's completed-quest gate is therefore a deliberate post-report gate, not a mistaken started-dialog approximation.
The native source provides no guarantee that an arbitrary modified save will still have an actor after that gate.
The route correctly additionally requires actual living contact in loaded Wintersun.

## Native history selection

Native peaceful cues `452882614caa439cb44ff6be9d3c71f2` and `dbc87d75792240c28b9ea0a8a26d21b4` test the respective removed and upgraded illusion etudes Playing.
The opening reads those same bindings and requires at least one before entry.
When both are present, the truth passage wins because the illusion answer explicitly forbids truth.
The branch therefore has one history answer in that modified state.

Native chief cues `987325f0537f2784083d3dfd6b98d335` and `d2c12299bf82ad241b2de3be7db4901a` negate Playing on `baa4820ac052d664bbaa261d17ce9b08`.
Native cue `929f607396aafb540a8deca42a9e6816` requires that etude Playing instead.
The authored chief/carver selector mirrors these opposite predicates rather than assuming Gesmerha became chief in every outcome.
The focused suite covers both leadership branches, truth, retained illusions and both-illusion states.

The upgraded-illusion etude independently contains an AttachBuff action targeting native spawner `aaa7f11f-f916-4820-a05b-9946ccb50c1b` in scene asset `5f4ad31583f5c284ab3889c7c5d9cd26`.
This corroborates a native actor connection but does not establish its live placement or a cure for blindness.
No route effect restores sight, changes native political outcomes, revives a unit or edits a native etude.

## Contact and progression

All six scenes are local Chapter 3 visits with the same Wintersun area, contact unit and native conversation attachment.
The first visit has no delay; subsequent visits require the preceding terminal milestone and wait 24 hours.
The actual source chain is unbought_work, along_the_grain, whose_mark, the_first_game, the_unclaimed_hour and against_the_current.
The suite reaches every authored page through earned predecessor outcomes rather than preloading contradictory romance intentions.
It tests wrong chapter, wrong area, missing prerequisites, delay boundaries, death, closure and the authored mythic restrictions.

The production contact reader checks the loaded actor without using DialogSpeaker.GetEntity or spawning a replacement.
It requires a conscious Commander outside combat and a unique matching unit that is loaded, present, alive, conscious, unsuppressed and nonhostile.
Choice continuation rechecks the contact, area, chapter, prerequisite and unavailability contract.
The focused test explicitly removes contact at every reached page and confirms continuation becomes unavailable.
This models disappearance; it does not execute a Unity scheduling race.

The shared contact reader counts matching units before filtering inactive candidates.
Consequently a duplicate native actor can make contact unavailable even when one candidate is usable.
This inherited conservative behavior is not a new Gesmerha defect, but actual-save verification must include the real actor state.
The module neither relaxes that guard nor promises that every save has a unique actor.

## Checks, choices and interruption

The wood examination has one actual `SkillLoreNature` DC23 specification with CommanderOnly enabled, separate success and failure destinations, and a non-roll sacrificial-strip alternative.
Success produces a narrower folding board; failure produces paired trays; the non-roll approach spends wood and also produces a narrower board.
Those outcomes have distinct terminal flags and are recalled by the later game.
Failure preserves the courtship opportunity.
The production builder constructs BlueprintCheck, uses the player's character for CommanderOnly, disallows the party substitution in camp, and gives no check experience.
This review verifies the specification and construction path, not an actual native roll in Unity.

All authored Set effects in the six scenes occur only on terminal non-abort answers.
I checked that property independently against the corrected source, in addition to the focused assertions that every intermediate snapshot has the scene-entry flags unchanged.
Thus an interruption before a terminal answer does not record a kiss, a commercial answer, a construction result or a relationship intention that the player has not completed.
Returning to the scene starts from the preceding earned milestone with no contradictory partial outcome.
A completed scene is no longer available.
Deferral preserves both flags and timestamps.

Courting, slow exploration and friendship are mutually exclusive in the traversed histories.
The final friendship and slow paths do not set first_kiss.
Kiss and held_close are mutually exclusive final affection outcomes.
The opening never sets committed and does not reset another romance or native-history flag.
The merchant letter, game pieces, tools and boat are narrated objects, not inventory additions or economy actions.

## Remaining gates

The root should run the combined rule, typed-binding and managed-build suites on the actual staged export before promotion.
Independent writing and characterization approval is a separate requirement.
The local Trickster boat experiment is a voluntary, temporary narrative flourish and does not meet the promised bespoke recovery/access requirement by itself.
Every visit still depends on living Chapter 3 Wintersun contact.
Dead-character recovery, later acts, full-route depth, endings, artwork and optional paired routes remain unfinished.
Actual native rolls, live speaker placement, save persistence, portraits and ToyBox coexistence still require their corresponding runtime evidence.

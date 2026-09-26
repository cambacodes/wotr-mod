# Gesmerha living late campaign handoff

Released for independent review on 2026-09-26.
This is a living Chapter 5 continuation with earned endings, not approval of every character-access history or comparative RanRomance quality.
Only the three assigned source, focused-test and handoff files were written.
Original source modules, installed game data, art, shared engine, builder and test registration were not edited.

| Artifact | SHA256 |
| --- | --- |
| `storylines/gesmerha_late_campaign.py` | `CA412FD0C337F1A351EC4B70E34AC997484282B473627E6FE283C327A7D197DC` |
| `tests/GesmerhaLateCampaignTests.cs` | `42C5A88355EB020FB91D76FD6A36E6F31277E3034EE6F238F4DD267E10C703BA` |
| Isolated assembled candidate | `AB265DAA17672EF5E3C98BDC347EFB69C75D8EB1F548F05093E205D5CA0BDAE0` |

The candidate is `C:/Users/Z/AppData/Local/Temp/gesmerha-late-campaign-5eitxgkf/candidate.json`.
It adds 18 scenes to the actual 483-scene assembly, giving 501 scenes.
The manuscript has six played visits, eleven completed outcome pages and one unfinished-late outcome page.
No author scores or self-approval are supplied.

## Integration

Append a deep copy of the module's `SCENES`, then call `integrate(payload)` on the assembled payload.
Register `GesmerhaLateCampaignTests.Run` when `gesmerha.the_things_still_here` exists.
The one new read-only etude alias is `gesmerha.post_resolution_contact`, targeting `24505150d0cf493c936f2c50b1c94468`.
Every visit requires that native post-resolution contact owner, the completed Wintersun quest, actual living Gesmerha contact in Wintersun, a resolved illusion outcome and the previous earned milestone.
The first requires `gesmerha.campaign_kept` from the existing ten-visit Chapter 3 chain.
Demon, Devil, inhuman, native death and authored closure remain blockers.
The ordinary route works without Trickster.

The first two books form one immediate return and hearing, with zero delay.
The remaining four visits wait 24 hours after their predecessor.
The local return is explicitly a temporary trip to settle possessions and obligations, not a reversal of the native clan departure or a claim that Gesmerha permanently remains at the old trading bench.
The existing capital guest scene is optional and transient.
Its actual played history and heard native future report are recalled only when present.
A later local reunion does not require that temporary audience to have been played.

The narrow integration overlay was authorized by root:

- Add `gesmerha.late_arrived` to the old private capital reunion's Forbids, preventing a first-private-return conversation after a later return already occurred.
The native KTC conversation is untouched.
- Add `gesmerha.late_arrived` to the old ordinary `ending_living_reunion` and `ending_unmet_again` Forbids.
A real late return must not leave the old never-met-again account available.
- Add `gesmerha.late_complete` to the other old provisional ending Forbids.
Their special outcomes remain available during unfinished late progression.
- Use the new unfinished-late book for ordinary living progress after the late return and before late completion.
Use the new completed endings only after their actual farewell.

The helper is idempotent.
An isolated before/after comparison verified that original IDs, text, choices, indices and every field except these explicit Forbids additions remain equal.
No native history, old relationship flag or old scene ID is erased or rewritten.

## Played story

| Visit | Event, choice and consequence |
| --- | --- |
| `the_things_still_here` | Temporary return to sort possessions in the hall; distinguish the actual earlier court reunion, an unplayed private reunion, elected chief and retained Marhevok authority. |
| `the_box_with_two_names` | Sella claims her grandmother's carving patterns while Gesmerha wants them available for communal teaching; choose three paid teaching copies or a limited future loan, with ownership remaining with Sella. |
| `the_long_way_with_company` | Return the actual box; LoreNature DC26 identifies a safe crossing, failure costs the appointment after a wet misstep, and the non-roll higher path also misses the lesson; the box remains intact and is actually delivered. |
| `a_lesson_without_her` | Play consequences of being present or late; resolve the chosen pattern arrangement and the paid copies or limited loan; Elun takes a real teaching role. |
| `the_room_she_chose` | A private adult evening with lover, slower exploration and friendship histories; explicit new consent resolves a slower romance, while a friendship-only invitation goes directly to friendship. |
| `the_work_left_finished` | Finish the temporary work visit, recall only an actually heard migration/shelter report, choose a continuing lover/friend/open relationship or an honest ending, and give a concrete farewell. |

Gesmerha has interests that can conflict with reasonable claims from others.
She wants useful patterns, enjoys being the person who can answer questions and dislikes missing a lesson at which people expected her.
Her accepting an arrangement does not erase those wants.
The Commander offers practical help with a chosen cost rather than declaring her morally corrected.
Sella's inheritance, Elun's work, Halvek's help, the local carrying journey and every new romantic development are authored fiction.
They are not native named actors or inventory/quest transactions.
Gesmerha's earlier decision to delay buying tools is remembered, and a second delay is explicitly a further personal cost.
A check result does not decide her attraction or close the romance.

Her blindness remains present in physical staging.
She asks where people and objects are, follows audible movement, uses her staff and requests an offered arm without surrendering all control of the walk.
She does not see expressions, silently read papers or gain supernatural certainty about another person's state.
The private scene preserves old scars and bodily limitations without making them a cure objective.
Intimacy is voluntary and non-graphic, with a night together, gentler affection, a new slower-history relationship, continued uncertainty and friendship.
The relationship permits other attachments and does not claim another partner's consent.

## New authored history

Progress milestones are `late_arrived`, `patterns_agreed`, `delivery_kept`, `work_settled`, `private_evening_kept` and `late_complete`, all under `gesmerha.`.
The pattern decision records exactly one of `teaching_copies` and `family_loan`.
The journey records exactly one of `crossing_read` and `crossing_delayed`.
The explicit friendship-only invitation records `evening_as_friends`.
That flag prevents the next private visit from reopening romantic exploration on an earlier `campaign_slow` history.
The private evening records exactly one of `late_lovers`, `late_friends` and `late_open`.
The final continuing decision records exactly one of `future_lovers`, `future_friends` and `future_open`; the alternative records authored closure.
New romance commitment is recorded only after the explicit relationship acceptance.
All progress and branch effects are terminal-only.
A deferred or interrupted book does not collect mutually incompatible outcomes.

## Native access audit

The installed archive and Unity scene were inspected directly.
Earlier character and dialogue evidence remains in `reference/canon-review/gesmerha-route-evidence.md` and the prior campaign handoff.
The area-parent analysis also follows the already inspected `reference/canon-review/soana-late-access-audit.md` because the characters share Wintersun's default mechanics.
This is static native access evidence, not a live Chapter 5 save replay.

| Native role | Exact identity |
| --- | --- |
| Wintersun area | `0a5654e7dc18f074d9356009d55eb51b` |
| Living Gesmerha blueprint | `3ba3a0ff8575be8419159221177c1411` |
| Peaceful post-resolution dialogue | `736b0be04541f5246b41f332ab651f47` |
| Peaceful answer list | `2063ee21356b772408f5c9cfb3ed5bd0` |
| Completed Wintersun quest | `c0d0b565f4b725241b96c148000f1910` |
| Native death | `49839ba15f34bee469c4f093dace0811` |
| Post-resolution actor owner | `24505150d0cf493c936f2c50b1c94468` |
| Gesmerha as chief, post-final spawner | `b37ebe9b-ff38-49ba-aba1-9b8c2dea1deb` |
| Marhevok retained, Gesmerha post-final spawner | `1f825669-377e-4a85-930d-a927c0509e5a` |
| Shared mechanics scene | `5f4ad31583f5c284ab3889c7c5d9cd26` |
| Wintersun default mechanics | `198b62fe2afa9da4cb314f1b4376b0b9` |
| Wintersun default etude | `87839550c801db944b102f61084fd245` |
| AreasDefault parent | `19c0886c9e105ea4a832eec08321ac0f` |
| Chapter03_Extra parent | `2d9c51e422e743947bfa0281d0a2db51` |

The consumed actor-owner record is `World/Etudes/Common/WrathOfTheRighteous/Chapter03/WinterSunAfterFinalDIalog_Leader.jbp`.
Its SHA256 is `2A9D40530A1DEBF926037BB19CEC34B39F06DD857DFD3511303BE82F53EAB3D3`.
It is parented to WintersunStory, which leads through AreasDefault and Chapter03_Extra to the campaign root, rather than being a child that ends with the Chapter03 etude.
Its activation and completion conditions are empty.
The area-linked repeatable play trigger has `IsActivateOnLoadArea=true`.
It checks native Gesmerha death, then chooses the correct post-final Gesmerha spawner according to Marhevok's retained leadership.
Both Spawn actions have `RespawnIfDead=false`.
The record does not contain a Chapter 3-only condition or a Chapter 5 removal action.

`wintersunoutdoor_mechanics_default.scenes` SHA256 is `374A4D7360F0ECF9655494B0330501DD335D07B26C682A4D40DA0B77F1DAC5A2`.
GameObject path IDs 180 and 315 are the two post-final Gesmerha spawners.
Both use the exact living unit blueprint and the peaceful dialogue above.
Both are active, `m_IsInGame=1`, `m_SpawnOnSceneInit=0`, `m_RespawnIfDead=0`, and have empty spawn and conversation conditions.
Their HallSpawners/Spawners parents are active.
The original prequest unit at path ID 424 is a different spawner and uses a different conversation; it is not the post-resolution contact relied upon here.

`World/Etudes/Common/WrathOfTheRighteous/Chapter03_Extra/Chapter03_AreasDefault/Wintersun_Default.jbp` SHA256 is `94F571C1BFD2546134FB9CC7740C8D8A1C04C1D9BA21C9DEC477816B61F56204`.
It adds the actual default mechanics to Wintersun, with no chapter-only activation/completion condition.
The prior area audit verifies that the global-map location is not closed by a generic Chapter 3 transition.
A record's Chapter03 directory and the area's PS4 chunk label are not runtime chapter restrictions.
Actual live, visible, nonhostile contact remains required by the engine.
The source does not start the native owner or spawn an actor to make an unavailable save appear eligible.

The transient capital guest remains a different native opportunity.
The new module neither restarts its etude nor preserves its actor beyond the audience.
Read-only heard-migration and heard-staying flags select the final conversation's known report.
If neither was heard, Gesmerha describes her own wishes without claiming that the Commander received a native clan plan.
If an exceptional save has both, migration retains the earlier contribution's deterministic precedence.
The new fiction does not settle a clan-wide destination, reverse the native migration/shelter decision or remove Marhevok from authority.

Additional native opportunity found, but not consumed: `GesmeraWithUs` etude `a4de2a8e1ce8a4843a69c9a37ceda701` gates an actual Threshold Encounter03 spawn.
The spawn is `42ddf51b-23b4-40c8-a8b4-85440fb13ba7` in scene `590a7372fd11686439e3a73c4495c420`.
The cutscene also moves and barks through this actor.
This is a combat-arrival opportunity, not evidence of a quiet permanent camp dialogue or an automatic romance reunion.
The late source does not invent an answer list there.

Read-only extracted evidence is also retained in temporary files `C:/Users/Z/AppData/Local/Temp/gesmerha-native-scene.json`, `gesmerha-native-references.json` and `gesmerha-late-access.json`.
The all-blueprint direct-reference scan collected 84 records containing the original actor/spawner, death or BlindCarver references.
The durable identities and behavior needed to reproduce the conclusion are recorded above.

## Endings and remaining full-scope work

Completed new endings cover lovers, friends, open relationship, closure, death, inhuman change, Demon, Devil, ascent, sacrifice and the separate Aeon history.
They read actual chosen flags and do not invent a final commitment on an unfinished route.
The ordinary lover ending supplies an authored shared future of visits and ordinary mornings, without relocating the whole clan or curing blindness.
The other relationships keep their chosen forms.
Death and incompatible mythic outcomes suppress an ordinary shared future.
Ascent does not manufacture a divine reply; sacrifice preserves the concrete farewell; Aeon does not carry erased promises into the rewritten world.
The unfinished-late book remembers only the first late arrival and welcome, so it is valid before the box, private evening or farewell is completed.

The delivered branch supports living native Chapter 5 continuation, including retained Marhevok authority and an unplayed capital reunion.
It still requires the earlier ten authored Chapter 3 visits.
That is a scope limit, not permission to drop the user's late/missed/dead and bespoke Trickster requirements.
The concrete remaining implementation contract is:

1. Add an honest late acquisition sequence at the verified living post-resolution actor for players who missed the Chapter 3 opening.
It must introduce Gesmerha's current work and develop a new invitation without writing ten unplayed scene IDs or inventing Dera/Runa history shared with the Commander.
Use a separate late-acquisition flag and explicit relationship-intention choices, then provide the appropriate joins into later work.
2. For dead Gesmerha, inspect the exact saved post-final spawner and unit state before proposing recovery.
Both spawners refuse ordinary dead respawn, so clearing `gesmerha.dead` or replaying the owner is not restoration.
A recovery must preserve the entity or explicitly reconcile a replacement, corpse visibility, native death history and the choice that caused the death.
3. A Trickster recovery/contact quest can use the actual Wintersun investigation: counterfeit warning stones, the exposed Lady's deception, Marhevok's key and the woodshaper who perceived the truth through her work.
Those are concrete native quest connections for an authored fate intervention, not an existing resurrection mechanic.
Verify the selected death producer and the relevant surviving quest objects before writing a recovered actor into the scene.
Ask for her independent answer after recovery; preserving her blindness and voice does not require undoing her entire history.
4. A missed or no-longer-present native contact needs an actual temporary guest/contact implementation with a voluntary invitation and a reliable departure lifecycle.
The capital KTC and Threshold ally records are examples of real native delivery mechanisms with distinct conditions, not flags to repurpose indiscriminately.
5. Provide live C5 return, save/load, dialogue resumption and actor-identity checks, then the dedicated art/TTS and comparative RanRomance reviews.
A Chapter 4 absence chapter remains optional future development rather than pretending an Abyss meeting exists.

No source in this contribution restores a dead unit, grants native mythic powers or manufactures a romance from an unplayed past.
The current full-route approval remains with independent reviewers and the project owner.

## Measurements and checks

Counts use the standard `tools/measure-story-content.py` tokenizer and normalization.
Unicode alphanumerics count as words, internal apostrophes are retained, hyphens split, markup is removed and whitespace normalized.
Distinct counts remove identical normalized whole page/choice strings, not semantic similarity.
No external game or RanRomance writing, entry labels, journal text, titles or repeated playthrough is credited.

| Scope | Books | Pages | Prose words | Raw with choices | Distinct segments |
| --- | ---: | ---: | ---: | ---: | ---: |
| Previous opening/campaign | 20 | 101 | 14,496 | 15,778 | 15,688 |
| New contribution | 18 | 64 | 9,456 | 10,202 | 9,977 |
| Combined | 38 | 165 | 23,952 | 25,980 | 25,658 |
| Combined visits only | 17 | 144 | 21,894 | 23,901 | 23,599 |

The visit-only aggregate exceeds the 21k planning floor without credit from alternate endings.
This is not a claim that raw volume proves comparable quality or that a single selected path must itself contain 21k words.

Selected full paths exclude refusals, replay and epilogues.
The new six visits read 4,357-4,964 words, depending on history and choices.
With the ten earlier Chapter 3 visits and no capital reunion, the selected sixteen-visit route reads 11,302-12,944 words across the inspected ordinary/Trickster and leadership histories.
With the actual capital reunion, the selected seventeen-visit route reads 12,396-14,051 words.
The higher Trickster maximum comes from the already integrated earlier optional experiments, not a new requirement for magic in this ordinary continuation.
Detailed scenario bounds are in the isolated `counts.json`.

Python compilation passed.
The current isolated candidate passed `Rules.Validate` and **490,606 focused assertions**.
The suite plays the actual original ten visits, optionally the real authored capital reunion under native fixtures, then all six new visits.
It covers ordinary non-Trickster and Trickster, truth/illusion histories, retained Marhevok authority, all new pages, actual skill success/failure/non-roll, invitation-to-evening friendship consistency, terminal effects, interrupted/deferred progress, replay, native death/contact loss, wrong chapter and immutable native/unrelated romance history.
It verifies one final ordinary ending, the new-only Aeon ending after completion, death precedence, partial-history ending coverage and suppression of the old first-reunion scene after a late return.
The source overlay is idempotent and the previous scene records differ only in the approved Forbids additions.
These fixtures do not claim to execute Unity's KTC scheduler, world-map travel or physical actor spawn.

```powershell
& C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe run --project C:/Users/Z/AppData/Local/Temp/gesmerha-late-campaign-5eitxgkf/Check.csproj -- C:/Users/Z/AppData/Local/Temp/gesmerha-late-campaign-5eitxgkf/candidate.json
```

The adjacent `measure.py` regenerates the isolated candidate and standard inventory plus selected-path bounds.
It groups only actual played witnesses with the same flags read by remaining scenes and endings, preserving minimum/maximum paths without inventing progress.
Native chapter/quest/contact/report states are explicitly external fixtures.
All authored predecessor milestones are obtained from player choices.

## Independent review status

Root read all six visits and endings, independently verified the native post-resolution parent chain, and requested three revisions.
The friendship-only evening now persists that choice and has an actual slow-history test witness.
Loss and sacrifice now use concrete shared memories instead of branch-audit narration.
The unfinished outcome recalls the common first late welcome without assuming later romance or work milestones.
Root also requested and received non-Trickster coverage and final Aeon arbitration checks.
Final revision-specific scores and acceptance must come from that independent review, not this author handoff.

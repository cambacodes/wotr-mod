# Konomi ordinary contact implementation review

The frozen overlay passes independent source and focused technical review.
It adds the verified actor requirement to exactly 22 existing ordinary meetings and preserves the early encounter's existing contact requirement.
No implementation blocker was found.
Combined integration and actual game presentation remain separate requirements.

## Reviewed revisions

| File | SHA256 |
| --- | --- |
| `storylines/konomi_contact.py` | `5BC57BDF458285E719AA04587845B0FEB8EFED5A62037403FB9A0CB9F2870AE0` |
| `tests/KonomiContactTests.cs` | `F7BC6A2948965272A190EB1C490B2727EE1AD32BEB6BCEB8701F77220CA061E4` |
| `src/NativeContact.cs` | `018BE371E40D1950564D6C74D1EB79CD195E781DCF2C28FA0A8CC826D10170B3` |
| `src/Story.cs` | `D6AF931FA196A40A16E9D791D711B04AB308DD054AA3AFF5D995A4A7C30C0B48` |
| Independent input `development/Story.json` | `3ACCB25AF2142B70ACBCC2BCA1A6839D0571E1DD38097B5578363720534108AD` |
| Independent staged candidate | `7FD1D3C9BB5F8C1972CA3D1741D7F3DE8A535C6F85515A06801C8C0BA03E35E4` |

Root confirmed the author's final source and test freeze matches the inspected revisions.
The independently inspected physical-contact report and stored records establish the native unit and dialogue connection.
This review does not infer actor identity from Konomi's display name or the office etude name.

## Native evidence and runtime contract

The exact actor is `ca2d58c5c65723945857e04fb85d30ce`, the native `RankUpOfficer_Diplomacy` unit.
The recorded capital scene spawner `c658c4cf-116e-4b61-9ff9-8905bcf4fd6b` links that unit to dialogue `a81655ed97277974e947c1aaf9e33525` and existing answer list `0dc8b8604bb33c846a63f3eb62443674`.
The actor initially has hidden state; the office etude's unhide and translocation actions provide positive ordinary-position evidence but not a universal alive or loaded-view guarantee.
The overlay therefore retains `konomi.present`, Drezen, chapter, and native dialogue restrictions and adds actual observed contact.

`NativeContact.IsAvailable` requires exactly one matching blueprint in current game units, valid current area or cross-scene storage, a reciprocal loaded active view, and an actor that is in game, unsuppressed, conscious, alive, undisposed, and nonhostile.
It also rejects game loading/unloading, combat, or an unconscious Commander.
The observer does not wake, unhide, spawn, teleport, or resurrect Konomi.
Its cross-scene storage handling was separately reviewed; this overlay does not change that code.

`Rules.Available` consults the contact guard at entry.
`Rules.ContactAvailable` requires the actor, scene prerequisites, area/chapter, native forbids, and relationship unavailable flags during continuation.
It deliberately does not reapply completed-scene checks, entry delays, or ordinary authored closure flags mid-conversation.
The inspected `Main.cs` route conditions and actions call that continuation check before offering or applying choices.
Losing contact consequently blocks further effects without manufacturing a breakup or rewriting history.

## Exact scope

The changed scene suffixes are:

```text
margin reception letter evening disagreement leak reckoning
return power ordinary farewell parting hearing hearing_after
new_letter political_account a_useful_supper the_upper_passage
two_bad_prices the_trial_day a_name_beside_hers the_evening_she_kept
```

Each has Konomi physically present in its authored meeting and uses the ordinary native answer-list delivery contract.
Even the scene named `letter` is a face-to-face conversation about the letter in her writing case.
The new `a_turn_for_herself` already has the correct actor requirement and is unchanged.
The resulting classification has 23 physical Konomi scenes, of which exactly 22 fields are newly added.

`another_evening` is different: the Commander reads an already received invitation.
It remains remote and manual, with its existing office-history gate but no loaded officer requirement.
The solitary Abyss material, private acquisition and continuation, private career/farewell, and all epilogues likewise retain their existing unitless delivery.
This preserves their contracts without asserting that the dismissed private visits have independently verified physical presentation.

I compared the staged payload against the input as parsed objects.
Each changed scene equals its original object plus `ContactUnit` set to the verified unit.
The scene list and every other scene, relationship, binding, node, answer, condition, flag, and text remain unchanged.
Applying the overlay twice produces an identical payload.

## Independent mutation probes

I tested all 22 target positions with each of 11 invalid conditions: missing target, duplicate ID, remote delivery, manual delivery, wrong relationship, wrong owner, missing office prerequisite, wrong area, wrong answer list, Chapter 4 classification, and conflicting contact unit.
All 242 cases raised `ValueError` and left the complete supplied payload unchanged.
Testing every position includes failures after earlier targets have already passed validation.
The implementation collects validated targets before assigning any contact field, so a late error cannot leave a partially applied overlay.

The focused test also requires a complete classification of the current Konomi scene set.
Adding a future unclassified scene will fail that test and require deliberate review.
The overlay's fixed target list alone is not claimed to discover future scenes automatically.

## Focused execution and negative witness

I independently staged the overlay against the pinned input and compiled actual `src/Story.cs` with the frozen test.
The temporary runner uses the repository's actual `Program.Copy` and `Program.Walk` helper prefix and directly calls `Rules.Validate` and `KonomiContactTests.Run`.

```powershell
& 'C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe' run --project 'C:/Users/Z/AppData/Local/Temp/konomi-contact-independent-2uqs3yyf/Check.csproj' -c Release -- 'C:/Users/Z/AppData/Local/Temp/konomi-contact-independent-2uqs3yyf/story.json'
```

Result: `PASS 1120 contact assertions`, exit code 0, with no build warnings printed.

The negative witness temporarily removes the exact scene's contact metadata, supplies its prerequisites and one `RequiresAny` alternative, and verifies that the old contract admits entry without a loaded actor.
It then removes `konomi.present` and verifies that the old unitless continuation guard still returns true.
The test restores metadata in a `finally` block before checking the corrected behavior.
For the 22 changed scenes this reproduces the previous source-model contract.
For the already protected early encounter the same operation is a counterfactual control, not evidence that its released implementation previously had the bug.

The prerequisite-only snapshots are valid for testing the contact condition in isolation.
They are not claimed to be full earned story histories, and the test does not use them to prove every dialogue branch playable.
The check includes actual alternative prerequisites, which is necessary for the ordinary expansion gate.
Entry, continuation, office disappearance and restoration, actor disappearance and restoration, wrong location/chapter, authored partial effects, native exclusions, completion, and delay semantics are exercised.
The excluded invitation remains readable with no actor in `AvailableContacts`.
History flags and timestamps are checked for unintended mutation.

The focused suite seeds actor availability in snapshots.
It does not execute Unity view queries, move a real actor, or reproduce a live dialogue disappearing on screen.
Its before/after result establishes the missing necessary guard, not an entire live-game E2E fix by itself.

## Integration requirements and limits

Root must apply the overlay after all audited ordinary modules and register the focused test.
Existing ordinary-route fixtures must supply the verified actor when modeling a physical meeting; the missing-actor negative witnesses must remain missing it.
Root reports that shared political and private-career predecessor fixtures exposed those previously implicit assumptions and are being updated.
The combined rerun was still in progress at this review's completion.
No combined pass is inferred from the independent focused run.

Loaded-save checks should still cover ordinary interaction, temporary rank-up displacement during an open book, restored contact, dismissal, and the separate private-route presentation.
The narrated receptions, suppers, and outings remain book-event presentations attached to native contact, not newly implemented room or map transitions.
No universal Trickster recovery, resurrection, art approval, TTS presentation approval, or live ToyBox compatibility follows from this metadata fix.

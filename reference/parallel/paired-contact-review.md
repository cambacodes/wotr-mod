# Independent paired-contact review

Reviewed 2026-09-26.
Decision: accept the bounded additional-contact availability change.
No mandatory correctness defect was found in the inspected implementation.
This does not approve a future authored group meeting, actor relocation or live Unity behavior.
I did not author the implementation or its tests and made no changes to shared files.

## Pinned inputs

| File | SHA256 |
| --- | --- |
| `src/Story.cs` | `81C3E0890703040BE91046A3B2C708B286471B77715FDD9882A4A75B62082771` |
| `src/Main.cs` | `CC9950C68BFE9F6A7528D13F99DCC07D3FF50C578285A35E8EEAD9FFC40151A4` |
| `tests/PairedContactTests.cs` | `F8562BBC763FFD698F4BE5577FE85D2B6D15098AA107EC3F4EE6E79E929CCAF8` |
| `tests/Program.cs` | `C913A95AC3F24EEF77A7EB13D4F478344248CDA942F9887D0564E8A9807458C2` |
| `managed-tests/Program.cs` | `62611DADB94AAEDE186E454C7CE9FC5FBC4BF57E7706843E2A3C26E9645EA632` |
| `managed-tests/write-check-fixture.py` | `69E797F7A52BC91F04AC0F60D51D6DDFA6945138F7FCBE6D099135DA94BBEFA1` |

The inspected built DLL has SHA256 `4C3B0CEE5BB412833058A9801C72549790FEA9BEAED7F198A698B0BA2779F286`.
The isolated managed fixture has SHA256 `6DB8698D909648EA0C1F45E7038E1D66CCAC69155713FE7B7D96916BDC575013`.
Both match the supplied release evidence.

## Code findings

Scene defaults AdditionalContactUnits to an empty array, preserving old JSON scenes.
Rules.Validate rejects a null array, malformed GUIDs, additional actors without a primary ContactUnit and duplicates across the complete list, including case-only duplicates.
Production loading validates the story before Build registers observers.
The null-primary shortcut in ContactAvailable is therefore safe for validated scene data; an invalid extra-only declaration cannot pass loading.

ContactAvailable requires the primary actor and every additional actor in AvailableContacts.
It retains chapter, area, prerequisites, native forbids and relationship-native-unavailability checks.
It deliberately does not reapply authored relationship closure to a continuation, so a closing answer can reach its closing prose.
That exception does not bypass loss of either physical participant.

Build collects all configured primary and additional GUIDs and resolves each as BlueprintUnit.
State observes them through the same existing NativeContact path.
That path requires a unique blueprint match, current saved storage, a valid loaded active view, in-game presence, consciousness, life and nonhostility.
The change adds no actor spawning, resurrection, history reset or fabricated availability.

Existing answer visibility, selection and RouteAction mutation checks call ContactAvailable on the scene.
Because validation requires a primary actor, the existing primary-contact branches still generate interruption exits for additional-contact scenes.
The second actor is therefore checked when choosing or committing an answer, not only when opening the meeting.
Native skill-check guards also carry the same continuation scene.
The managed assertions inspect these actual compiled blueprint attachments, including a nonmutating contact-loss exit.

The managed fixture includes two native actor IDs in its separate mechanical scene.
The builder observer dictionary is checked against both IDs, and the native binding extraction includes additional contacts as BlueprintUnit references.
The generic narrative traversal fixture seeds the additional contacts only for the scene under test; it does not globally claim that every actor exists.
The changes are small enough that a new abstraction or separate paired-contact engine would add no demonstrated value.

## Independent execution

I built an isolated temporary project linking the actual current `src/Story.cs` and `tests/PairedContactTests.cs`.
The focused suite passed all 18 assertions.
It checks primary-only rejection, both-present acceptance, loss and restoration of either participant, authored closure followed by contact loss, native death, chapter/area changes, JSON round-trip, legacy defaults and invalid declarations.
The runner is `C:/Users/Z/AppData/Local/Temp/paired-contact-independent-q0hhtomh/Check.csproj`.
No shared build output was overwritten.

The supplied full rules result is 18,784,596 passing assertions and the supplied managed fixture result is 42,853 passing assertions.
I inspected their relevant code and matched the DLL/fixture hashes, but did not rerun those full suites for this narrow review.
These managed checks verify generated blueprint wiring, not real actor movement or UI behavior inside Unity.

## Required scope boundary for the future bridge

AdditionalContactUnits proves that all specified actors satisfy the existing availability predicate.
NativeContact does not compare their positions, distance to one another, current room or path connectivity.
Two actors can therefore satisfy this predicate while standing apart within the loaded area.
The new field must not be described as proof that both women have physically arrived at the same table.

For the negotiated bridge, establish the meeting through supported scene staging or add a specifically justified co-location requirement if the entry depends on an already assembled group.
Do not infer a room shared by Anevia and Irabeth merely because both are available somewhere in loaded Drezen.
This is a limitation of the deliberately retained observation contract, not a defect in the added all-actors predicate.
No integrated story scene currently depends on the new field, so the future author's staging remains independently reviewable.

Before accepting such a scene in game, lose each participant separately after entry and after a skill-check page opens.
Verify that ordinary progression and flag mutation stop, the interruption exit remains usable, and restoration permits only the intended continuation.
Also verify no ordinary dialogue or other romance is changed by opening or leaving the paired meeting.
No review score is assigned to unimplemented writing or art.

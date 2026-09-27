# Konomi recovered-actor observer handoff

The loaded contact observer and saved-state negative observer now recognize a separately verified return of the original retained Konomi.
This change is frozen for independent review.
I authored it and do not approve it independently.
My earlier independent review of the separate recovery service is not approval of this observer change.

| Owned file | SHA256 |
| --- | --- |
| `src/KonomiContactObservation.cs` | `F635C116A47D8A6A1D14CE3922B8B3735162E3BCC3D7EA0A951644FAB0AEBCE1` |
| `managed-tests/KonomiContactObservationTests.cs` | `08779F6C413FC2CBDB3207FAAA49BBA6F30A35B8FF5E4DB592DEAE1F01BA3A93` |
| `src/KonomiRecovery.cs` | `01270E345E1A310152EC705D968997584BC183F2AC11F91AA943F1C5DB0F93A9` |
| `managed-tests/KonomiRecoveryTests.cs` | `ACD28D1D51B5A06A632DCB07A8081330433F6FF574CE10B16FEDB4D6F197279F` |

Root temporarily extended ownership to the recovery helper and its tests to fix a review finding.
The historical-return helper changed as described below and needs independent review of that change.
No Main registration, authored scene, package, installed mod, save or shared output was changed.

## Behavior

Historical HasDied is evaluated after the original spawner and actor provenance checks.
The historical-death exception requires the exact currently living actor, its confirmed saved recovery identity and exactly one Konomi blueprint representation in the inspected source storage.
Temporary unconsciousness after confirmed recovery delays loaded contact without invalidating correspondence.
Initial Request/Poll confirmation still requires consciousness.
It does not excuse destruction, new death, an identity conflict, competing spawner claims or active office.
Pending, malformed and different-identity proof cannot enable contact.
The loaded path still requires loaded source evidence for initial availability.
The saved path never grants initial availability and retains its existing allowance for absent runtime registry entries and null HoldingState on serialized objects.

A known HasDied marker still invalidates missing actor and missing actor-identity cases.
Each observer retains a death marker established from the original spawner if later recovery validation throws.
This prevents an incomplete extra unit record from converting already known death into unknown state.
The addon never clears HasDied.

## Focused verification

The isolated projects are `C:/Users/Z/AppData/Local/Temp/konomi-return-observer-71e8e70e/Observer.csproj` and `Runner.csproj`.
The observer library, observer runner and `RecoveryRunner.csproj` all build with zero warnings and errors.
The focused runner passes 140 assertions, including all 65 earlier observer assertions.
The recovery runner passes 34 assertions, including the unchanged actual native SecurityException boundary.
`git diff --check` passes for the four owned source and test files.

New fixtures install an actual native Game, PersistentState and Player with serialized proof in Player.SettingsList and restore the original global Game instance in a finally block.
They cover absent, pending, wrong-identity and malformed proof, matching confirmed proof, active office, unloaded serialized original actor without registry entries, new death, final death, unconsciousness, actor and spawner destruction, missing body, missing saved actor ID, registry collision, competing spawner, competing Konomi representation and an incomplete unit that throws during validation.
They verify that recovered saved observations remain negative-only and that historical death remains recorded.

The fixtures deliberately supply a confirmed checkpoint and controlled current life state to test how the observer treats that evidence.
They do not invoke resurrection and do not claim a native revival succeeded.
Actual resurrection, authored action wiring, game save/load persistence, stable later-frame visual state, ToyBox coexistence and full route completion remain separate work.

## Review correction for temporary unconsciousness

Root identified that the earlier helper required current consciousness even when verifying an already confirmed historical return.
That made a living but temporarily unconscious recovered actor invalidate correspondence, unlike an ordinary living actor.
Before changing source, I copied the observer test into the isolated directory as `UnconsciousReproduction.cs` and changed the saved unconscious expectation to remain non-invalidated.
It failed with `Living unconscious recovered actor must not become a death interruption` against the prior frozen assembly.

The helper now checks confirmed identity, current life and absence of destruction without requiring current consciousness.
Request and Poll still require a conscious observation before returning Confirmed.
The loaded observer returns unavailable but non-invalidated for the confirmed recovered actor while unconscious.
The saved observer preserves correspondence in that state and still never grants new contact.
The updated observer tests pass both cases, and the recovery tests check historical proof during unconsciousness, rejection of pending proof and continued Pending status for current confirmation while unconscious.
The prior independent recovery review applies to its recorded older hashes; it does not independently approve this correction.

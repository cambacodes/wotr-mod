# Konomi missed-contact observation

This is a read-only prerequisite for an authored correspondence route.
It neither starts a native romance nor delivers a visible actor.
The implementation is awaiting independent review and shared registration.

## Native evidence and attainable history

The exact capital source is area `2570015799edf594daf2f076f2f975d8`, scene `DrezenCapital_Default_Mechanics`, spawner `c658c4cf-116e-4b61-9ff9-8905bcf4fd6b`, and unit `ca2d58c5c65723945857e04fb85d30ce`.
These identities come from the actual bundle extraction in `tools/probe-konomi-contact.py`, `konomi-contact-records.json`, and the independently repeated extraction recorded in `konomi-contact-independent-review.md`.
The spawner initializes on scene load with empty spawn conditions, initially hidden, and without dead respawn.
Hidden existence is suitable evidence of a retained living correspondent only when the saved spawner, exact saved actor reference, storage and registry agree.
It does not establish physical availability for a private meeting.

An installed archive search for the office etude `b5f301fbc4c44535a6309d610d5bd28a` found its ordinary StartEtude action in `World/Etudes/Common/WrathOfTheRighteous/Chapter03/CapitalMechanic/RankUps/DiplomacyRankUp2.jbp`.
That record has asset ID `e513ab6862e999644acde5a994911f5a` and raw SHA256 `030823605F0D6A4334AFDD694590C00B1F332E60D0C045746F21E91B9EB2BDD7`.
Its repeating play trigger starts the officer presence etude after queuing the rank-up cutscene using this same spawner.
`Kingdom/CrusadeProjects/RankUps/Diplomacy/DiplomacyRankUp2Project.jbp`, asset `eec2844333716044680b3e7c4f34d638`, has raw SHA256 `84896E0A250DC6EF51414E34D6C7AC94007F03063613DDD6FA839E50B7329E3E`.
It requires Diplomacy rank exactly one and eligibility for rank two, requires a throne-room visit, and sets ResolveAutomatically false.
Thus the native records support a before-rank-two history with the initialized hidden actor and no started office presence etude.
The observer still requires the actual retained living actor rather than granting eligibility from these static records alone.
This is native evidence of an attainable opportunity, not a played Unity save proving its entire timing window.
It does not assert that the Commander has never personally encountered Konomi.

Ordinary office completion at `World/Crusade/RankUps/Diplomacy/Diplomacy_6/Diplomacy_6_Dialogue.jbp`, asset `30333438aac8d3647bef882fa87e978e`, requires selected dismissal answer `73c5728c4c6658344bedcc1b666e598c`.
Its raw SHA256 is `136CD1CFA513D179BCCF208008DDFDDF49953A7F6DD6315C5494D1CDB18AFCAB`.
The upgrader `Root/Upgraders/Player/PF-360384.jbp`, asset `fbda3f5666a44d92af69e12338629a16`, repeats the same answer-selected condition, with raw SHA256 `D78086552982D966CB6B86536836CB554365A59283375A56D7646F9EEA033D57`.
A distinct ordinary completed-office-without-dismissal history is not established here.
The existing dismissed route remains the appropriate path for the documented ordinary completion.
A Locust completion reference also exists; inhuman restrictions remain the caller's responsibility and it is not advertised as a new romance opportunity.

## API and classifications

`KonomiContactObservation.Observe(bool officeActive)` returns `Result.Available` and `Result.Invalidated`.
It has no mythic-path check, stores no result, and performs no native mutation.
`Inspect` delegates saved identity, blueprint, scene, registry, life and storage checks to the existing `JerribethRecovery.Inspect` implementation.
It additionally rejects HasDied history even when the current retained actor is living, rejects known destruction, and rejects a second saved spawner referencing the same actor.
This correspondence route does not explain resurrection.

| Observed condition | Available | Invalidated |
| --- | --- | --- |
| Office active, including suspended activity | false | true |
| Exact loaded retained living actor, office inactive, no death history | true | false |
| Source unloaded, absent, never spawned, or missing unresolved actor | false | false |
| Actual retained death or saved HasDied | false | true |
| Confirmed source/actor destruction | false | true |
| Saved identity, blueprint, storage or registry conflict | false | true |

Unknown state does not establish death or revoke earned correspondence.
A never-spawned native record cannot open this route.
The implementation uses the actual scene readiness predicate: IsSceneLoaded, IsSceneLoadedThreadSafe and IsPostLoadExecuted.
Loading, unloading, missing player and unavailable area states provide no positive evidence.
No actor view, friendliness or consciousness is required because this signal is not physical contact.
No unhide, relocation, clone, resurrection, office restart or native history change occurs.

## Proposed shared integration

Root owns Main.State and the shared registrations.
Compute officeActive from the exact native office blueprint as `state.Flags.Contains("konomi.present") || (player.EtudesSystem.Etudes.GetFact(officeBlueprint) != null && !player.EtudesSystem.EtudeIsCompleted(officeBlueprint))`.
Checking only IsPlaying is insufficient because a higher-priority council or combat can suspend the office's playing state.
Call Observe after native flags and authored saved flags have been collected.
Publish `konomi.missed_contact_available` only when Available is true.
Publish `konomi.missed_contact_invalidated` only when Invalidated is true and either `konomi.missed_letter_sent` or `konomi.missed_private_access` is present.
Both flags are derived and recomputed; neither is written to authored persistent history.
Register both with Rules' known/native-derived flag classification so entry and remote continuation evaluate them correctly.
The first letter requires positive available evidence and its separate authored Trickster prerequisite.
Earned reply, meeting and subsequent private correspondence forbid invalidated without requiring loaded-only available.
Existing native dismissal history retains its separate access alternative.
Register `KonomiContactObservationTests.Run(Check)` in the managed suite.

## Retained off-area evidence

The first candidate had a reproduced gap: it lost known death evidence on leaving the capital.
The released implementation additionally reads `PersistentState.SavedAreaStates`, together with the already loaded area if it is not the same object.
Fresh installed-assembly decompilation confirms that SavedAreaStates is a public List of AreaPersistentState objects, AreaGuid is directly stored, and GetAllSceneStates only enumerates the main and additional states.
It does not call GetStateForArea or GetStateForScene, either of which may construct native state.
The exact source AreaGuid and SceneName remain mandatory.
Duplicate area or scene representations are conflicts; the same loaded/saved area object is deduplicated by reference.

`InspectSaved` never returns Available.
It detects the exact saved spawner's HasDied and destruction markers, competing saved actor references, retained actor death/destruction, wrong identity/blueprint/storage and positive registry collisions.
A missing global registry entry is allowed for off-area negative inspection: the actual saved storage carries the evidence, and no claim of loaded contact is made.
A null HoldingState during unloaded reconstruction is not itself a conflict, but a nonnull HoldingState pointing to a different scene is.
Missing saved areas, missing spawners, missing unresolved actors and unreadable incomplete native objects remain unknown.
No result is persisted in an authored flag.
Therefore retained saved death continues to invalidate correspondence outside Drezen, without treating ordinary unloaded living storage as loss.
If all native death evidence is removed from a save, this observer cannot reconstruct it; it does not invent a permanent history marker.
Actual disk deserialization and Unity save transitions remain untested.

## Managed reproduction and checks

The closest feasible headless reproduction uses actual installed SceneEntitiesState, UnitSpawnerBase.MyData, UnitReference, UnitEntityData, UnitDescriptor and UnitState objects.
It begins with an absent office and no actor evidence, then adds a never-spawned record, unresolved saved identity, recorded death and finally the exact retained living actor.
Only the last state provides positive initial availability.
This directly exposes why office absence alone is insufficient.
Native object constructors requiring Unity are bypassed with FormatterServices; native fields, property getters and the production inspector remain real.
Only scene readiness and registry lookup are supplied as controlled delegates.

The isolated projects are `C:/Users/Z/AppData/Local/Temp/konomi-observer-9rt235pk/Observer.csproj` and `Runner.csproj`.
They compile the source against the installed assemblies into that temporary directory, without changing shared outputs.
Both builds succeeded with zero warnings and zero errors.
The runner passed 65 assertions covering absence, never-spawned history, saved death, retained life, active office, unloaded source, different area, restored observation, historical death despite current life, actual death, final death, destruction, wrong blueprint, duplicate storage, registry collision, competing spawner, duplicate scene and read-only invariants.
The retained-state regression cases use the actual AreaPersistentState(BlueprintGuid) constructor, GetAdditionalSceneStates and GetAllSceneStates, with a real saved-area list and empty registry.
They prove off-area retained death, saved HasDied with missing actor, destruction and registry conflict remain negative, while unloaded living storage and unavailable history cannot grant initial entry.
The active-office boolean's derivation from native etudes belongs to the shared integration and is not exercised by these tests.
The wrapper's actual Unity loading lifecycle, live save transitions and authored scene delivery are not executed by this fixture.
There is no author approval of this implementation.

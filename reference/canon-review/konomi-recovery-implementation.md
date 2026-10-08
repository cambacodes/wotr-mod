# Konomi retained-body recovery implementation prerequisite

This implements an explicit request and verification service for the original retained dead Konomi in her loaded capital source.
It is not registered with Main, story actions, the observer, or the shared managed test runner.
It is awaiting independent review.
A real Unity resurrection has not been demonstrated by the standalone fixture.
Missing, destroyed, replaced and otherwise unavailable bodies remain required future recovery work.

## Owned release

| File | SHA256 |
| --- | --- |
| `src/KonomiRecovery.cs` | `F476A0DAD2E3FA6164743E4F78A14AB18551791233BD927A1932B709441D5329` |
| `managed-tests/KonomiRecoveryTests.cs` | `EC3AB112077A4AF985E06B0CF6338F49911FD7508CD3A1B0D9C5A60A02DA7429` |

All three assigned paths were absent before this task.
No existing source, builder, installed mod, save or shared output was edited.
The isolated projects are `C:/Users/Z/AppData/Local/Temp/konomi-recovery-utqnquih/Observer.csproj` and `Runner.csproj`.
The source and tests compile against the installed game assemblies with zero warnings and errors.
The focused runner passes 31 assertions.

## Native operation and verified limits

The installed Assembly-CSharp.dll SHA256 is `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953`.
Fresh targeted decompilation confirms `UnitDescriptor.ResurrectAndFullRestore(initiator)` invokes the native private Resurrect method with fullRestore true and restoreHealth false.
The full method body is also preserved in the matching installed-assembly evidence `jerribeth-recovery-managed-records.json`.
Native ContextActionResurrect uses the same method for its FullRestore branch.
The addon calls this native API directly, not a replacement policy or a delegate that sets life flags.

The native method clears final-death and death conditions, resets forced/marked death, restores damage and attributes, handles negative levels, updates an existing view where available, removes appropriate buffs and raises the resurrected event.
It may set the unit conscious through UnitLifeController.ForceUnitConscious, whose installed body calls SetLifeState with Conscious.
Its work is sequential and can partially change native state before later view, event or controller work fails.
A returned call or exception therefore cannot substitute for re-observing life and provenance.
The implementation never assigns LifeState, IsFinallyDead, HasDied, native etudes or native dialogue history itself.

The actual managed fixture calls the installed resurrection API.
It fails at the Unity-dependent boundary with `System.Security.SecurityException: ECall methods must be packaged into a system module`, in UnitDescriptor.Resurrect, before fixture death state changes.
That exact failure is observed and checked; it is not reported as successful resurrection.
The fixture verifies that the request was serialized before invocation and that the failure returns Pending without confirmed proof.
The native source establishes partial-mutation risk in real runtime; this particular standalone failure occurs before that mutation.
No Harmony patch, fake Unity internal call, native method replacement or substituted successful action is used to evade the boundary.

Controlled later-life fixtures separately test the verification contract by explicitly setting native UnitState fields to dead, unconscious or conscious.
Those fixtures prove how the service reacts to observed states, not that resurrection produced those states.
This distinction applies to every positive confirmation assertion below.

## Retained actor and checkpoint contract

The source is area `2570015799edf594daf2f076f2f975d8`, scene `DrezenCapital_Default_Mechanics`, spawner `c658c4cf-116e-4b61-9ff9-8905bcf4fd6b`, and unit blueprint `ca2d58c5c65723945857e04fb85d30ce`.
These are the already audited native capital identities, not a guessed actor GUID.
The actual saved actor identity comes from the spawner's UnitReference.UniqueId.
`Inspect` reuses JerribethRecovery.Inspect to validate exact scene, spawner, saved actor, blueprint, HoldingState, registry agreement and lack of destruction.
It additionally rejects another spawner claiming that actor or another Konomi blueprint representation in the inspected source storage.
The runtime wrapper rejects a second saved capital-area object, incomplete loading, unloading, combat, an unavailable or unconscious Commander, and a hostile Konomi.
The source scene must be loaded, thread-safe loaded, post-loaded and serializable.

The stable player SettingsList key is `RanRomance.Tirabade.KonomiRecovery`.
Its JSON string contains version, stable authored request identity, exact saved actor ID and Confirmed.
This follows the existing Fate/RecoveryAttempt saved-settings pattern.
The in-memory setting participates in the game's normal save mechanism; it is not a separately forced disk save before every native call.
No existing recovery key is overwritten.

`CanRequest()` is read-only retained-dead eligibility, not quest authorization.
`Request(requestIdentity, authorized, out message)` must be invoked only by an explicit authored recovery choice.
The caller supplies its current quest, mythic and voluntary-choice gate and a stable identity for that choice.
A different request cannot adopt an existing checkpoint.
A first request requires the original actor to be dead or finally dead; it cannot take credit for an already living actor.
The checkpoint is saved before native dispatch, including before an explicitly resumed request.
A persistence failure prevents dispatch.

`Poll(authorized, out message)` does not invoke resurrection.
It returns NotRequested without inventing a request and returns Pending while the original actor cannot be verified alive and conscious.
A current observation must still match the exact original registry object and source storage before confirmation.
A changed identity, hostile state, destruction, area loss or provenance conflict cannot be credited as a successful return.
A failed confirmation write leaves the pending attempt unconfirmed; the service saves a separate confirmed value rather than mutating the pending object first.

An explicit repeated Request may retry the native operation only while its unconfirmed original actor remains dead.
Polling never performs that retry, and a living but unconscious actor is not resurrected again.
If the API throws after restoring life, a later Poll can confirm the actual observed result without replaying the action.
Repeated requests against a confirmed living actor only verify it.
A new death after confirmation is blocked by the old request and requires a separately designed new recovery episode.
No request is silently cleared to permit a second resurrection.
Player messages avoid internal checkpoint and registry terminology; exception details remain available through LastError.

## Historical death and future observer integration

Spawner HasDied remains untouched by the addon.
The recovery proof is separate from that historical marker, so a living restored actor need not be falsely described as never having died.
`HasVerifiedReturn(actor)` reads the confirmed checkpoint and checks matching identity, Konomi blueprint, current consciousness, current life and absence of destruction.
An old proof cannot authorize a currently dead, finally dead, destroyed or different actor.
This helper alone is not full provenance or contact validation.

Root's future observer integration must first validate the original saved spawner/actor relationship and storage using its existing loaded or retained-state rules.
Only after that validation may HasVerifiedReturn excuse the historical HasDied marker for this same current living actor.
It must not suppress destruction, ambiguous identity, active office, hostility or new actual death.
The current observer returns early on HasDied, so its check order needs an independently reviewed change; merely OR-ing a recovery flag into availability would be unsafe.
The saved-state negative observer needs the same narrowly placed historical-marker exception to avoid invalidating recovered correspondence whenever Drezen unloads.
No observer edit has been made in this task.

The authored success effect must wait for a current Confirmed result, not just a native API call, a checkpoint's existence, or the saved Confirmed bit without current actor checks.
A root-owned caller must also keep the request reachable for verification after the actor becomes alive, without rerunning the native mutation.
The service restores neither an office nor a relationship and grants no romance access by itself.
Any native appointment or dismissal remains the game's history.
A hidden or otherwise inaccessible office actor is not unhidden or relocated by this service.
Native removal of the death-specific hidden state is part of resurrection, not a manual override of office hiding.
A later personal introduction and consent remain story work.

## Focused checks and remaining verification

The tests use actual installed SceneEntitiesState, UnitSpawnerBase.MyData, UnitReference, UnitEntityData, UnitDescriptor, UnitState, Game, PersistentState and Player classes.
They check never-spawned/missing bodies, exact retained death, source loading and area, destroyed body, competing Konomi representation, failed checkpoint persistence, actual native dispatch failure, history preservation, no Poll dispatch, unconscious pending state, failed confirmation persistence, JSON round-trip, repeated confirmation, subsequent death, wrong saved identity and registry collision.
The actual native Player.SettingsList path is exercised for unauthorized requests, no-request polling and proof lookup.
The test restores the prior global Game instance in a finally block.
Unrelated saved history remains unchanged.

The runtime loading, combat and hostility wrapper is compiled but not exercised inside live Unity.
The controlled source-storage tests do not prove a real save retains Konomi's body after every possible death.
Full native resurrection, view/animation recovery, stable post-event consciousness, actual save/load persistence, current observer integration, authored action binding and ToyBox coexistence remain to verify.
No visible meeting or original-campaign indistinguishability is claimed from this prerequisite.
Destroyed, missing, never-spawned and other unresolved histories are not declared impossible or removed from the universal Trickster requirement.
They need distinct truthful recovery work, without cloning an unresolved body or clearing native history as a shortcut.

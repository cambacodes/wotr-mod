# Nurah private appointment placement contract

This is the next implementation proposal, separate from the frozen retained-actor observer review.
The parent agent authorized a temporary candidate implementation on 2026-09-26.
No shared movement helper, `Main` integration, or physical route availability is approved by this document.

## Location and native evidence

Use the generic private visitor marker `KTCPrivatVisitor1Point `, including the native trailing space in its editor name.
Its entity ID is `7b94948a-1954-428f-82d0-94b2adcb1380` in scene `3e2b5ea054cd5b2479e7f13134363ef4`.
Direct Unity scene extraction places it approximately at `(196.190, 79.116, -1.080)`.
The implementation resolves the actual entity reference and never substitutes these evidence coordinates.
This is a private-chambers doorway appointment, not Nurah's former cell, a tavern interior, or Yaker's post.

Native `PrivatKTC_OnePerson` cutscene `4100513157a1a7a4bb29eabac97234f3` uses `CommandAction 1` `0971481f9a68c8547a4d7cb0c086b311` to unhide its named `Unit` parameter and translocate that same unit to this marker with rotation copied.
Its later native move command `cedabdcbd4a23124f8fa25f8e49c21d4` walks the visitor toward `KTCPrivatVisitor2Point ` `8ec4df14-1759-4201-9cea-4e7d7ce0d5e2`.
Nurah's appointment need not replay that movement, camera sequence, dialogue, or final completion action.
In particular, native completion command `26d568bdf0b75c64cb7067fe1ea3c6dd` completes the supplied etude and must not be reused.

A full native archive reference scan found two callers of that cutscene: `KTC_Sosiel_DatingMonster_c5` `28c0e7ec749d8eb45b617f5a7342d203` and `KTC_Sosiel_Romance_Breakup_c5` `e14c6b78f5939fa46abbe1ee630619f1`.
Both own `Capital_KTC` group `10d01be767521a340978c8e57ab536b6` at priority 100.
Their activation conditions include native `AnotherEtudeOfGroupIsPlaying`, negated for that group.
This is why Nurah must not reserve the KTC group herself.

The visitor marker is near native `DrezenRestPoint` at `(185.030,79.020,-10.630)` and `RestButton` at `(185.807,79.710,-13.966)` in throne-room mechanics.
The rest entry `ab3b5c105893562488ae5bb6e7b0cba7` explicitly targets the same capital area and area-part `2570015799edf594daf2f076f2f975d8`.
These records establish the intended native private-chambers setting and ordinary rest access.
They do not prove current save-specific navmesh routing, rendered visibility, absence of obstacles, or clickable dialogue after moving Nurah.
Those remain live checks.

Fresh evidence is in `C:/Users/Z/AppData/Local/Temp/nurah-extension-audit-3y60fthx/`: `private-ktc-cutscene.json`, `private-ktc-callers.json`, `private-room-scene.json`, `private-room-access.json`, and `alternative-locator-references.json`.
The direct scene extraction scripts are retained alongside them.
The source archive and parent assembly pins remain those in the independently reviewed Nurah canon audit.

## Consent and native arbitration

The callback reads raw saved flags and returns a stable `nurah.private/<retry>` episode only after the sent invitation, completed reply, explicit meeting acceptance, and valid 12-hour acceptance timestamp.
Decline, withdrawal, route closure/completion, wrong chapter/path, missing parent relationship/finale, and invalid living provenance remove eligibility.
The helper never calls a state observer that recursively calls the helper.
The same standing invitation may support later authored visits, but a changing scene ID or incidental progress must not silently reset a failed episode.

Nurah's authored temporary etude owns only group `d0210e61193c8c746bc33bf7d1fff325` at priority -90.
It may displace only the audited native hidden fallback `245524f91e743b64eaa16445c3ea8e73` at -100.
Every current or ready pending real Nurah claim wins, including an unfamiliar lower-priority mod claim.
Native parent readiness, area/campaign linkage, completion state, and activation conditions must be evaluated rather than inferred from a started flag.

The appointment also defers while `Capital_KTC` has any current holder or a ready pending claimant, even though that is a separate group.
It must not claim KTC, complete its events, clear flags, or mutate native actions.
A separate group does not automatically preempt Nurah by priority; the helper must recheck live ownership and eligibility before any mutation and trigger native reevaluation on withdrawal.
Foreign dialogue, scheduled dialogue, cutscene/combat modes, and current visible nonparty occupancy near the marker also defer the appointment.
Normal deferral preserves the invitation and can resume once the competing event finishes.
No Yaker, Sosiel, or other companion history permanently disqualifies Nurah.

## Placement and persistence

Resolve and validate the exact native hidden action and generic visitor placement shape before enabling the authored helper.
Create only Nurah's authored unhide/move actions against her verified capital spawner and the verified marker; do not retarget the original shared action objects.
Preflight the locator and recheck provenance/claims/consent before unhide.
After native unhide, reread the actor's view and reject a missing, dummy, mismatched, unloaded, or inactive view.
Then move the same actor once and verify native contact plus actual current position before publishing `nurah.meeting_arrived`.
Invitation or living saved identity alone never grants a physical scene.

Save actor identity, consent/retry episode, and attempted-placement failure separately from transient arrival.
Any unverified result after a mutation attempt, including a false result without an exception, latches failure for that episode.
Only explicit retry supplies a new episode; polling must not repeat partial mutation every frame.
A claim lost before mutation is deferred without failure.
On load, ownership and arrival must be freshly checked; an old in-memory `Placed` flag is not evidence.
Withdrawal releases the authored claim and allows native hidden fallback behavior to resume.
The reviewed prison transition correction must be carried into this candidate before any physical stage is accepted.

# Irabeth living-departure meeting integration

Date: 2026-09-26.
Status: implementation frozen for independent review, not self-approved.
Scope: one accepted temporary visit by the retained living capital actor.
This does not restore ordinary romance availability, reinstate Irabeth, resurrect her, or establish repeat visits.

## Owned changes

- src/Main.cs: SHA256 1A09266238C0ED3914202F8DCFE3B89CB490A5DF50B6D4051EA2FF9053C03B4D.
- src/IrabethMeeting.cs: SHA256 AE64FE05F93E7E0C8C0516DFBC9AFB5E48650355E808209904D645F70050779F.
- managed-tests/IrabethMeetingIntegrationTests.cs: SHA256 D6044CADC43EABF2737E1873EFE68E897B5BA0FF7071E7B6B1EE8C07B8738912.

No Story.cs, narrative, managed Program, existing helper tests, shared build output, export, or installed mod was changed by this task.
Existing Konomi and parent-ending integration remain in place.
Main registers the authored etude and stable saved flags during Build before saves load.
Its ordinary ownership pass touches only the new predicate and component; reused native show/move actions retain their original owners.

## Request and story contract

The three scene IDs are irabeth.return_request, irabeth.return_reply, and irabeth.return_first_words.
The two read-only observations are irabeth.return_correspondence_available and irabeth.return_meeting_arrived.
Main adds them only to observed State, never to saved flags.
The remote observation does not require an accepted request and cannot recurse through State.
It requires enabled initialized integration, Chapter 5, current Trickster playing, loaded Drezen capital, no Swarm or true-Lich conflict, and the helper's retained living departure evidence.

The physical request requires completed irabeth.return_reply, positive irabeth.return_meeting_accepted, no irabeth.return_meeting_declined, no completed irabeth.return_first_words, and no irabeth.closed or shared closed flag.
It also requires the saved positive hour.irabeth.return_meeting_accepted timestamp and 12 elapsed hours.
Saved hour values use the existing hour-plus-one encoding; subtraction uses long arithmetic.
Its stable identity is irabeth.return.first/<saved retry counter>.
Repeated observation does not increment anything.
The request is withdrawn outside Idle except during the exact registered irabeth.return_first_words dialog.
Combat, scheduled dialogs, unrelated dialogs, loading, unloading, disabled integration, completed visit, refusal, closure, lost departure evidence, or disallowed native claims prevent continuing authorization.

The mod event UI offers "Arrange Irabeth's visit again" only for the current accepted failed episode while Idle and correspondence remains available.
Clicking revalidates and increments the saved irabeth.return_meeting_retry flag once, with negative and maximum-integer guards.
There is no automatic retry escalation.
A deferred attempt is not labeled failed.
A failed, throwing, or unverified placement is saved against its episode and requires an explicit new episode.

The separately authored AfterDeparture Rules and invitation producer still require independent review and combined integration.
The tested committed 585-scene export does not include those three new producer scenes.
This result therefore verifies registration and runtime wiring against the existing export, not playable end-to-end delivery of the invitation.

## Native departure correction

Fresh actual archive records were extracted to C:/Users/Z/AppData/Local/Temp/irabeth-meeting-integration-a853gflk/native-departure-chain.json.
That extraction has SHA256 7D5C1BD8ED0ED97D7239EF4E338128646EF46E835438BBB9EAA69237EB86DA77.
It contains Gone, ordinary hide, ImportantNPCs, default placements, and capital placements.
The earlier helper incorrectly required the ordinary hiding etude's own activation condition to remain eligible.
Native IrabethNotInDrezen 99a03d4f02004b76a5e97c85ba0ec37e activates under NOT(Coronation completed AND IrabethDead not playing).
It therefore becomes dormant in the intended living post-coronation case.
Native IrabethGone 395aad049186445f9f474d0a769ec8ff instead activates while IrabethDead is not playing and starts that hide etude.
It has no conflicting group or completion predicate, and belongs beneath ImportantNPCs 7f739a06cf7a15b4d9a9de77f8c20c70.

Correspondence now requires Gone actually playing, neither completed nor completing, and its hide producer started but neither completed nor completing.
It rechecks Gone's actual parent, campaign, area, and activation readiness.
It does not require the deliberately dormant hide child to play or pass its activation predicate.
This matches the existing irabeth_gone alias, which observes the native Gone fact playing.
The source comparison establishes consistency of this gate with that native branch; it does not prove a particular real save has retained the actor.

## Actor and claim safety

The retained capital actor is unit 280d4712dceb37f4a88e98f1f4c6e64f from spawner 3dc302d8-58ce-44f3-9766-2a437a080108 in scene asset 3e2b5ea054cd5b2479e7f13134363ef4.
The native throne locator is adee9a01-42a3-4850-b2d1-4a3dfcee9369.
Both entity references and their scene asset are checked before using the native actions.
Observer evidence, exact live entity identity, loaded serializable holding state, living conscious actor and commander, non-hostility, and an actual loaded view are required.
Duplicate capital state records, native expedition or death history, and any spawned or dead retained Iz representation prevent this meeting.
No actor is cloned or created, and no native historical etude is started, completed, or cleared by the helper.

The authored etude joins the original positioning group at priority 100.
Only the three explicitly audited ordinary background placements are exempted from claim blocking.
Any unknown current holder or eligible pending event blocks the visit, including a lower-priority event.
Parent readiness is rechecked before placement.
The exact native retained-actor show action runs before the move action, followed by an eligibility and ownership recheck.
Arrival requires the current request, bound actor identity, playing authored fact, actual group ownership, usable non-dummy native contact, and distance within 1.5 metres of the native locator.
A partial unhide or another claim cannot fabricate arrival.

Tick runs even when the mod is disabled or the game leaves Idle so native reevaluation can withdraw an existing claim.
Loading and unloading return before mutations.
Release and fallback positioning remain native selector behavior; the helper does not alter the claim table or mark native history complete.

## Isolated verification

Harness root: C:/Users/Z/AppData/Local/Temp/irabeth-meeting-integration-a853gflk.
Both production and managed projects link the actual current source and write only beneath that temporary directory.
Production and harness builds completed with zero warnings and zero errors.
The actual Main.Build run passed 71,766 assertions with 585 scenes and 20,708 generated blueprints, including idempotence and preservation fixtures.
Tested DLL SHA256: A1AF920B5A7CD16EBA6322A33D327C6A437278D84636473502F20F89B329E1EF.
Tested committed Story SHA256: 780BDC23146431CECD7F1ED9594B5F129C5E149DB535CC40F2BD128A2126647A.
The complete log is run-final.txt under the harness root.
A confirming invocation with separate stdout and stderr files returned executable exit code 0; those logs are run-final-stdout.txt and run-final-stderr.txt.
This avoids PowerShell reporting an error status merely because the native fixture logger writes its ordinary fixture notices to stderr.

Focused tests cover native blueprint registration and owners, actual native saved-flag storage, accepted versus unfinished reply, missing consent or timestamp, the 12-hour boundary, stable request identity, explicit retry identity, negative and maximum counters, decline and closure precedence, completed visit, saved flag restoration, failed versus deferred requests, exception persistence, exact-dialog exemption, combat and unrelated modes, disable, loading, and unloading.
Native fact fixtures distinguish playing Gone from started-only Gone and permit its dormant hide child while rejecting completion or missing history.
The existing actual native arbitration and lifecycle tests also run through a temporary adapted copy.
That copy changes only the constructor request callback, exact entity SceneAssetGuid, and Gone fixture seed required by the new helper contract.
Root must make those same fixture adaptations in managed-tests/IrabethMeetingTests.cs when adopting the integration, then register PrepareNativePlacement before Build and Run afterward in the shared runner.
Neither shared file was edited here.

The headless fixture reaches a documented native LoadingProcess.Instance SecurityException before Unity withdrawal scheduling can execute.
It explicitly reports that boundary rather than passing off native scene behavior as tested.
The tests do not prove actual hidden-view recovery, physical movement, callback ordering in Unity, native selector release in a live save, invitation UI delivery, loading a saved game, or ToyBox behavior.
Required live verification is one eligible retained-actor save, invitation and acceptance, actual delayed arrival, own-dialog persistence, unrelated event and disable release, explicit failure/retry if reproducible, and save/reload without duplicated actors or altered history.

## Shared runner adoption

Root subsequently authorized only the two managed runner files and this note.
managed-tests/IrabethMeetingTests.cs now supplies the request callback, native SceneAssetGuid on every entity reference, and exact Gone fixture seed.
managed-tests/Program.cs runs Irabeth service tests immediately after Konomi service tests, prepares Irabeth native placement immediately after Konomi preparation and before Main.Build, and runs Irabeth integration immediately after Konomi integration.
Every pre-existing check retains its original relative order, including parent fixture construction, preservation snapshots, and parent integration checks.
These are the same adaptations exercised in the isolated 71,766-assertion run, with the unused old flag replaced directly by the callback variable.
No shared build was run during adoption.
The runner changes remain subject to independent review.

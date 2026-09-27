# Konomi meeting integration handoff

Status: implementation frozen for independent review.
This is not an approval of live arrival, route completion, or an installed release.
The earlier helper review remains evidence for its original scope; this integration needs its own review.

## Frozen artifacts

| Artifact | SHA-256 |
| --- | --- |
| `src/Main.cs` | `6747C8F62EA075EED497A972E7C979A7E652630AEDB4C558A85EBEC06F98EA08` |
| `src/KonomiMeeting.cs` | `B7A30326CA868230F7153A8F9D7CCAED38CE2FCC453E11A2FF934DD96EA80238` |
| `managed-tests/KonomiMeetingIntegrationTests.cs` | `F8409CF34A97A7777769822A9D9175C89E9074945F01FEF416E7355CE7D10CC4` |
| Isolated production assembly | `4304E1590AFDBDA1CBF6673E7BB09CA4CCA6FCC13250954FC7506FFD3FBEBA0B` |
| Reviewed 538-scene `development/Story.json`, read only | `8DCEB83D44925E5C07C7407D1FCEABE9381CE147D9A862B22E4E88420583C300` |

Owned changes are limited to the two source files, the new integration test, and this handoff.
No shared Program, Story, recovery source, narrative, exports, binding manifests, package files, or shared build outputs were changed.

## Consent and saved identity

Main.Build registers `etude.konomi.personal_return` through the existing authored New API and constructs KonomiMeeting before saved-game restoration.
It also registers `flag.konomi.return_meeting_retry` as a native BlueprintUnlockableFlag.
The normal initialization pass assigns the authored conditions and placement component owners without reparenting the reused native office actions.

The callback reads native saved flag values and game hours directly.
It never calls State, which would recurse through the meeting contact observer.
The first episode requires confirmed return, its saved timestamp at least 12 hours earlier, and `konomi.return_meeting_accepted`.
The followup requires completed first words, `konomi.return_followup_invited`, and at least 48 hours since that invitation's saved timestamp.
Existing saves with completed first words can receive the invited followup without the new letter acceptance flag.
Missing timestamps fail closed.
Old relationship closure/parting flags do not revoke separately accepted nonromantic recovery visits.
The existing declined flag rejects either episode, and completed second visit withdraws the request.
The callback also rejects disabled/uninitialized state, loading, unloading, combat, unsupported chapters, inhuman mythics, unavailable recovered correspondence, and unrelated event windows.

Stable request identities are `konomi.return.first/<saved counter>` and `konomi.return.followup/<saved counter>`.
Ordinary updates, failure, elapsed time, and reload do not increment the counter.
Negative counters are invalid.
The largest representable counter remains a valid observed episode but cannot be incremented.

## Retry and contact

KonomiMeeting exposes read-only CurrentRequest and SavedFailed status.
SavedFailed requires the actual native bracket component's saved failure to match the current accepted episode.
It does not infer failure from LastError, so nonthrowing partial-placement failures remain visible.
An ordinary deferred visit does not offer a retry.

The existing mod event UI shows `Arrange Konomi's visit again` only when enabled, Idle, current accepted consent exists, the matching saved attempt failed, current recovered correspondence is positive, and the counter can increase.
Clicking revalidates all conditions, increments the saved counter with an overflow guard, and ticks the helper.
It neither recreates an actor nor changes native history.

State's physical return flag now asks the helper's claim-aware contact observer.
An addon-held claim requires Arrived, which already checks the playing fact, saved actor/request, exact claim, recovered live contact, real view, and locator proximity.
The exact native office holder can continue through strict recovered direct contact without temporary arrival.
Rank-up, unknown, hidden fallback, and absent holders cannot use mere post-unhide visibility to bypass arrival.
The new ReturnCorrespondenceAvailable line is preserved independently.

## Event and withdrawal behavior

Update ticks the helper before the enabled and Idle exits.
The mod toggle also ticks immediately after changing enabled state, so disabling can request native reevaluation even if the manager stops future addon update callbacks.
Tick already avoids native mutation during loading/unloading and marks an existing meeting dirty when consent is absent or cannot be observed.
Normal update work now also stops during loading/unloading.
Native claim arbitration remains responsible for withdrawal and subsequent office/fallback placement.
No forced hide, stale-position restoration, forced claim-table write, or native history modification was added.

The exact registered dialog for the current visit remains an allowed window while that dialog is active in Dialog mode.
Without this exception, opening the physical visit would withdraw the actor and invalidate the scene's own continuation guard.
A same-name unrelated dialog, the other episode's dialog, scheduled dialog, combat, or another mode does not qualify.
Completing the first visit closes that episode and waits for the followup interval; completing the followup closes the request entirely.

## Verification

The isolated harness lives at `C:/Users/Z/AppData/Local/Temp/konomi-meeting-integration-a7e104`.
Observer.csproj compiles current production source into that temporary folder.
Runner.csproj compiles repository tests with temporary copies of Program and Bootstrap.
The temporary Program seeds the new placement fixtures before actual Main.Build and runs the old meeting suite plus the new integration suite.
It uses the original repository read-native.py and the reviewed parent-binding manifest.

Both builds passed with zero warnings/errors.
The final executable exited zero and reported **67,302 assertions**, 538 scenes, 19,445 generated blueprints, 14 native answer lists, one native Aeon sequence, and one parent-mod sentinel sequence.
The final log is `final-run.log` in that temporary folder.
`git diff --check` passed for the owned source/test files.

```powershell
$env:RRT_PYTHON = 'C:/Users/Z/AppData/Local/Python/pythoncore-3.14-64/python.exe'
$env:RRT_PARENT_BINDINGS = 'C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference/canon-review/expansion-parent-bindings.json'
& C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe build C:/Users/Z/AppData/Local/Temp/konomi-meeting-integration-a7e104/Observer.csproj -c Release --nologo
& C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe build C:/Users/Z/AppData/Local/Temp/konomi-meeting-integration-a7e104/Runner.csproj -c Release --nologo
& C:/Users/Z/AppData/Local/Temp/konomi-meeting-integration-a7e104/bin/Release/net48/Runner.exe 'D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure' 'C:/Users/Z/Documents/Projects/RanRomanceTirabade/development/Story.json'
```

Directly exercised checks include actual Main registration and owner initialization, raw consent using the native UnlockableFlagsManager, 12/48-hour boundaries, withdrawn/declined/completed consent, old-save followup, stable retry identity, negative/max counter observations, native dialog identity and mode windows, conditional claim gating, native bracket saved-failure observation, JSON failure restoration, deferred versus failed attempts, and no mutation on load/unload early exits.
The older helper suite also executes detached native etude activation/deactivation, claim arbitration, and parent-readiness changes.
Placement blueprint fixtures reproduce the reviewed native shape; they do not claim a live deserialization of those action graphs.
The flag reconstruction test serializes GUID/value pairs and resolves registered native identities; it is not a full game-save round trip.

Actual Tick reaches a Unity ECall boundary at LoadingProcess.Instance in the standalone process.
The test reports that boundary rather than replacing Unity methods or claiming native dirty scheduling executed.
Live tick scheduling, successful retry-button placement, dummy-view replacement, native unhide/movement, physical arrival, eventual withdrawal/resumption, complete save/load, and GUI presentation still require Unity verification.
The all-route managed runner retains its explicit limitations for parent-mod initialization, ToyBox execution, and portraits.

## Root integration of the test runner

In root-owned managed-tests/Program.cs, call `KonomiMeetingIntegrationTests.PrepareNativePlacement()` after seeding existing native fixtures and before the first Main.Build invocation.
Call `KonomiMeetingIntegrationTests.Run(Check)` after successful Main.Build.
To reproduce the full reported count, also call the existing `KonomiMeetingTests.Run(Check)` alongside the other service tests.
The temporary runner made those changes only in its own copy.
The root should independently review this freeze before adopting those test calls or rebuilding shared outputs.

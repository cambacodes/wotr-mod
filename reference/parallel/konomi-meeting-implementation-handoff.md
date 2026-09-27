# Konomi personal meeting implementation handoff

The helper and focused tests are frozen for independent review, not approved for installation.
No registration, narrative, recovery source, exports, or installed files were changed by this task.

## Files and verification

`src/KonomiMeeting.cs` SHA256: `FB9509E66E4D56053D2CE92A2DB6C42F1508E31C86F154415101B2A10D5243B2`.
`managed-tests/KonomiMeetingTests.cs` SHA256: `18DAE46FA5D1C22177761C0014BFBFCAB4550193A9E7872AF80A5498222050AC`.
The isolated Observer and Runner builds passed with zero warnings and errors.
The focused runner passed 43 assertions.
The temporary harness is `C:/Users/Z/AppData/Local/Temp/konomi-meeting-32f003c6`.
Build `Observer.csproj`, then `Runner.csproj`, using `C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe build <project> -c Release --nologo -v quiet`, then run `bin/Release/net48/Runner.exe`.
Its inherited final reflection diagnostics are not additional tests.

## Caller contract

Construct `KonomiMeeting` with a newly registered authored `BlueprintEtude`, `Func<string?> acceptedRequest`, and the existing native blueprint resolver.
The callback must read raw saved authored flags, never `Main.State` or an observer that calls this helper.
Null or whitespace means no current consent.
A nonblank value identifies one accepted meeting episode and must remain stable across ordinary updates and reloads.
Her remote accepted reply must precede the first physical visit; the helper cannot infer consent from recovery or resurrection.
Use distinct stable identifiers for the first visit, a separately accepted second visit, and each explicitly authored retry.
Do not use a clock, random value, or incrementing per-frame token to manufacture retries.
After a failed placement, the same episode stays blocked until a new explicit retry is authorized.
The narrative must therefore expose a reachable remote retry decision if a failed visit is to remain recoverable.
Withdraw the request when the accepted visit ends or consent changes.
Call `Tick` from the normal update integration so native activation conditions are reevaluated, including after a failed callback observation.
Register the blueprint and component before save restoration.
Physical aftercare must require current `Arrived()` and applicable strict contact observation, rather than the invitation flag alone.
Office-present contact can retain its existing direct native contact path; the personal helper does not displace her office.

## Native placement and arbitration

The concrete native identities and scene evidence are documented in `reference/canon-review/konomi-return-placement-audit.md`.
Construction validates the exact hidden and office action shapes, actor spawner, scene, locator, priorities, and actor conflict group before reusing their existing show and move actions.
It does not change those action instances, their owner, or their native arrays.
The authored meeting claims only the Konomi actor group at -90, above the exact hidden fallback at -100 and below office -20 and rank-up 0.
Eligibility additionally rejects every other eligible claimant, even an unknown lower-priority claimant, and any unrelated current holder.
The hidden fallback must be eligible under its live parent chain.
The existing `IrabethMeeting.ReadyUnderPlayingParents` helper supplies the native parent, campaign, and area readiness check.
The meeting neither completes native history nor starts or completes a native parent.
Native bracket activation, withdrawal, and arbitration control its claim; there is no direct forced claim removal or office reappointment.

Only the exact retained original actor with existing confirmed recovery proof can move.
The helper rechecks capital storage, actor provenance, consciousness, hostility, suppression, loaded scene, and identity before acting.
Both native action evaluators must resolve that same actor.
Locator position and orientation are evaluated before native mutation.
Native unhide runs first, and the helper rereads the actor's current view before native movement because unhide can replace a dummy view.
Arrival requires the currently held meeting claim, the same saved actor and request, strict recovered contact, and position within 1.5 units of the native locator.
Saved `Placed` is explicitly ignored by JSON and reset through native activation, resume, and post-load callbacks.

## Deferred versus failed attempts

An ineligible state before mutation, including a rank-up taking priority, defers the meeting and retains the invitation.
When the native claimant finishes and the same request becomes eligible again, the meeting can resume naturally.
Once unhide is attempted, every unverified result is a failed attempt, including a nonthrowing missing or dummy view, failed arrival check, or claim loss during mutation.
The saved failure then blocks replay of that episode on later updates.
An exception also records failure and requests native condition reevaluation.
Failure is assigned after the attempt finishes so its own eligibility and arrival checks do not reject an otherwise successful attempt.
An explicit retry can clear failure for a new episode, but can never transfer the saved request to a different actor identity.

## Test evidence and limits

The tests construct actual native blueprint, action, condition, bracket runtime, etude, and conflict-group classes.
They execute actual native claim activation, withdrawal, reactivation, selector arbitration, parent readiness changes, office/rank-up precedence, fallback restoration, and stale-release protection.
They verify saved actor/request/failure round trips and rejection of stale arrival proof.
They cover absent consent, callback failure, wrong actor, ordinary pre-action deferral, nonthrowing failed attempts, throwing failed attempts, explicit retry, and successful-attempt checks that must not self-invalidate.
The failure callback tests exercise the actual attempt checkpoint helper with simulated mutation outcomes; they do not perform Unity view mutation.
The standalone runtime cannot establish a successful native unhide, dummy-view conversion, translocation, or physical arrival.
The view-sensitive native calls remain a Unity verification boundary.
Missing views are rejected; this helper does not spawn replacement actors or reconstruct an absent actor view.
In-game verification still needs a dismissed or preappointment confirmed recovered actor, her accepted remote reply, visible arrival, first and second visit progression, rank-up interruption and resumption, withdrawal, save/load, and an explicit failure/retry case.

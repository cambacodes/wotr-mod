# Nurah meeting movement independent review

Reviewed 2026-09-27.
Verdict: verification required before approving the new physical movement stage.
The reviewed claim arbitration and saved failure policy pass their focused checks.
I did not reproduce an unsafe production mutation or a definite logic defect in this candidate.
Occupancy, composed placement, and eligibility-driven withdrawal still lack executable evidence.
Those are material gaps, rather than a reason to label 87 passing primitive and fixture assertions as a completed movement review.

## Frozen scope

| Input | SHA256 |
| --- | --- |
| `src/NurahMeeting.cs` | `680C93EEAEB560DADF562536A87CF3D8AB51B9CE4774E9148A55C973B63FB65F` |
| `managed-tests/NurahMeetingTests.cs` | `57216057E4465CAB6548BCC4CA3D33DB7335ED1A7A853BB13E0E1720AFF20004` |

I read the complete helper, submitted tests, `nurah-meeting-handoff.md`, `nurah-meeting-placement-proposal.md`, reused Konomi/Irabeth arbitration helpers, and `NativeContact`.
The earlier observer/prison review remains in `nurah-observer-independent-review.md`.
This review does not replace that historical evidence or approve subsequent Main integration.
The movement helper is not registered by Main in this candidate.
No production files, exports, package, or installed files changed during this review.

## Findings requiring verification

### M1. Occupancy behavior has no executed cases

`LocationFree` is a new gate on every eligibility and arrival read.
The submitted tests never execute it with an occupant or a destination.
The handoff correctly describes source intent, but its 77 assertions do not establish that this gate admits an empty point or rejects an occupied one.

Provide focused evidence for an empty point, a visible nonparty occupant inside three units, the exact distance boundary, the retained actor itself, party/pet exclusions, inactive or unloaded views, and a mismatched view owner.
Verify that pre-mutation occupancy deferral leaves the accepted episode and failure latch unchanged and that removing the occupant restores eligibility.
A small testable decision over observed occupancy facts would suffice if Unity cannot supply these cases headlessly.
The actual native observation adapter would still need a separately stated live boundary.
Do not substitute tests of the distance constant for execution of the production decision.

### M2. Composed placement and withdrawal remain untested

The tests execute `AttemptPlacement` with false/throw delegates and execute direct native fact activation/deactivation.
They do not execute the helper's complete eligible/claim/preflight/unhide/reread/move/verify sequence.
Direct deactivation demonstrates claim release, but does not demonstrate that consent loss, combat, loading transitions, or a new KTC claimant cause this helper to withdraw and the original fallback to hide the actor.

Verify zero mutation before permission and claim ownership, cancellation after unhide, exact actor replacement rejection, changed or missing view rejection, failed contact/distance verification, and no repeated native mutation in the same failed episode.
Explicit retry must permit a new attempt for the same retained actor while an ordinary deferred invitation must resume without incrementing its retry counter.
Verify a successful placement and subsequent withdrawal/fallback return in Unity, or test the composed production control flow through narrow substitutes and keep the actual Unity action/visibility boundary open.
Loading must neither start an etude nor attempt movement while native state is being loaded.

My temporary attempt to execute `PlaceNative` with explicitly substituted environmental reads failed during Harmony method compilation with `SecurityException: ECall methods must be packaged into a system module`.
The probe did not reach placement and is not a passing test.
I retained it as `C:/Users/Z/AppData/Local/Temp/nurah-movement-independent/Adversarial.cs`; it is excluded from the successful execution path.
The author confirmed that no additional occupancy or composed Unity placement execution evidence exists.

## Checks that pass

The movement constructor verifies the reviewed hidden fallback and private-visitor command shape before creating authored actions.
It leaves the original native actions and their targets intact.
The new actions target the exact capital spawner and locator, use the authored etude as owner, and do not create an actor or complete native history.

The authored etude owns only Nurah's actor group at priority -90.
The exact native -100 hidden fallback is the only accepted background holder.
Current foreign Nurah claims and ready pending claims win, including lower-priority claims.
Capital_KTC is checked separately and never acquired by the appointment.
This matters because the native private-audience callers test `AnotherEtudeOfGroupIsPlaying` for Capital_KTC.
Claiming that group on Nurah's behalf could suppress the very native event the helper should yield to.
The source avoids that error.

The submitted native predicate witness preserves the self-owned KTC condition, and the separate empty-checker readiness witness preserves playing-parent requirements.
The `FilterOnActors` test demonstrates why separate actor and KTC groups do not automatically preempt each other.
It does not establish a full populated selector evaluation in Unity.

The prior exact retained-capital-actor observer remains in use.
It rejects death history, current imprisonment, wrong representation, duplicate actors or sources, changed registry identity, unloaded source evidence, and conflicting personalities.
The corrected prison adapter still rejects the native early-completion interval.
Movement adds the saved actor binding and never authorizes replacement through a retry episode.

The source checks permission, claim ownership, locator resolution, and actor evaluator identity before unhide.
After unhide it rereads permission, ownership, retained identity, and the current view before translocation.
Arrival requires current eligibility, playing fact, saved episode and actor identity, native contact, and distance within 1.5 units.
These are source findings, not claims of executed Unity arrival.

`MeetingData` serializes actor ID, request, and failure while excluding transient `Placed`.
The failed episode is rejected until the caller supplies a different explicit retry ID.
Load/resume resets transient placement.
Tick marks conditions dirty for an existing fact even when consent observation fails, while its loading guard avoids mutation during loading.
The source makes no native death, romance, imprisonment, or quest-history write.

## Independent execution

I compiled a frozen source copy and copied tests in `C:/Users/Z/AppData/Local/Temp/nurah-movement-independent/`.
Both isolated projects built with zero warnings and errors.
The successful runner executed 87 assertions: the submitted 77 plus 10 independent adversarial checks.

The additions check completed-but-still-held KTC rejection, completed unheld KTC release, an unknown lower-priority current holder, a newly ready KTC after an earlier eligible result, recovery after deferral, null/blank consent, and serialized failed-episode/actor preservation.
The tests use actual native etude dictionaries and facts for arbitration and actual serialized `MeetingData` for persistence.
Their readiness callback is explicit test input where a fully populated Unity condition cannot execute.
The 87 total therefore does not imply 87 live movement scenarios.

I also freshly decompiled native `LocatorPosition`, generic `Evaluator<T>`, and `TranslocateUnit`.
Missing locator evaluation throws rather than silently returning a zero position.
Native translocation stops movement, interrupts the move command, and sets position/rotation from the locator view.
The helper's post-unhide view check is necessary before that native action.
Decompilation supports the API reasoning but cannot prove that the current save supplies a usable marker or actor view.

The retained native JSON in `C:/Users/Z/AppData/Local/Temp/nurah-extension-audit-3y60fthx/` confirms private visitor command `0971481f9a68c8547a4d7cb0c086b311`, marker `7b94948a-1954-428f-82d0-94b2adcb1380`, and the Capital_KTC caller conditions.
These are a generic private-visitor command and source location, not proof that Nurah has already arrived there.

## Main integration remains separate

The raw callback must supply current accepted consent and stable saved retry identity, enforce timing/path/chapter, reject foreign dialogue/events, and avoid recursive Main.State calls.
The helper does not itself implement those authored-flag rules.
Main must register the authored blueprint/component before save loading, prepare owners, call Tick during withdrawal opportunities, derive arrival from the helper, and expose an explicit guarded retry.
None of that wiring is approved or executed by this helper review.

The author's handoff is candid about these boundaries and does not falsely claim physical availability.
Keep the movement stage unapproved until M1 and M2 receive the specified evidence.
This verdict does not revoke the previously reviewed read-only observer foundation.

## Revised movement verification, 2026-09-27

The preceding findings describe the original `680C93...` candidate and remain historical evidence.
Revised verdict: pass for the bounded movement decisions, operation ordering, saved failure behavior, and native selection/ownership checks below.
M1 and M2 are resolved at this explicitly bounded helper-verification level.
Actual Unity unhide, movement, fallback hiding, the populated live selector, and a real saved actor remain unverified.
This is not physical-route readiness or Main/interaction integration approval.

| Revised input | SHA256 |
| --- | --- |
| `src/NurahMeeting.cs` | `8DFC5E3AF9B2974425E8833987BB7CD2EE7B6340051FB69F6806BFC4341F0EEF` |
| `managed-tests/NurahMeetingTests.cs` | `176617443FFF88F96842D0D20A0C4772D10F85EAF98A2F63A5312FEA97DBC5B4` |

### M1 reassessment

The native observation adapter now calls the same production `LocationFree` decision exercised by the tests.
Its small `Occupant` value carries actor identity, party/pet status, presence/removal flags, current view ownership/load/activity, and observed position.
The decision does not construct a view or assume that the current room is empty.
Adapter inspection confirms the observation fields correspond to the former native checks and that position is read only after loaded, active, owned-view evidence.

Tests execute the empty, near, exact-boundary, far, self, party/pet, missing/inactive/unloaded, dummy, removed, and mismatched-owner cases requested in M1.
The ordered placement test separately confirms occupancy deferral executes no mutation, consumes no episode, and resumes the same invitation once permission is restored.
That permission substitute does not claim to observe a real occupant; it verifies how the production sequence handles that observation.

An independent temporary mutant removing only the proximity rejection fails with `Visible nonparty occupant inside three units did not defer`.
The tests therefore catch a meaningful break in the production decision rather than merely inspecting its constant.
M1's executable decision gap is closed.
The Unity observation adapter still requires a live scene check.

### M2 reassessment

`PlaceNative` now delegates to the tested `PlaceObserved` production sequence with the real permission/claim/identity callback, locator preflight, native unhide and translocate actions, current-view reread, and arrival verifier.
There is no separate native mutation path that skips this sequence.
The sequence checks request and permission before preflight, rechecks permission after preflight, binds actor/episode, unhides, rechecks permission and current view, moves, and verifies arrival.
Any false or throwing result after the mutation attempt retains the existing failure latch.

The submitted substitutions observe actual production ordering and cover the requested pre-mutation denial, post-unhide cancellation, actor/episode changes, invalid or replaced view, failed arrival, exception, same-episode no-repeat, and explicit retry cases.
A valid new view after unhide is accepted, demonstrating that the protocol asks for a fresh view observation instead of relying on an old one.
An independent mutant that still calls `currentViewUsable` but ignores its result fails with `Missing/dummy/unusable current view was not reread`.
This separates meaningful rejection coverage from a test that checks callback order alone.
A separate mutant removing the callback entirely also fails the expected complete-operation order assertion.

The revised native fixture executes `EtudesTree.SelectPlayingEtudes` with explicit false/true eligibility observations.
Its first false pass withdraws the meeting and clears the group holder.
The next pass selects the hidden fallback; the test does not promise immediate same-pass fallback ownership.
Restoring eligibility lets the unchanged meeting fact regain the group without completing native history.
Production Tick continues dirtying an existing fact on safe updates, including after consent disappears, so it supplies the repeated evaluation opportunity required by this native behavior.

The fixture substitutes checker results, removes area linkage for its isolated selector, and omits fallback runtime HideUnit execution.
It proves native selection and ownership transitions under supplied eligibility, not the complete live eligibility predicate or visible hiding.
Actual loading/unloading Game flags exercise the early Tick guard.
Combat, changing consent, and changing claims enter the composed protocol through explicit permission substitutes; these are not live combat/event transitions.
These limitations are accurately stated in the revised handoff.
M2's missing bounded control-flow and native-selection evidence is closed without treating those substitutions as Unity success.

### Arrival accessor and independent execution

`ArrivedActor` contains the former complete `Arrived` proof and returns the exact retained actor only after it passes.
The boolean `Arrived` delegates to that accessor.
The refactor retains eligibility, group ownership, playing fact, saved request/actor identity, failure rejection, non-dummy view, NativeContact, and current distance checks.
It does not expose an actor from the transient `Placed` field or from mere correspondence eligibility.
The new missing-world test rejects a fabricated interaction actor.
The positive native adapter remains outside standalone Unity execution.

I built a frozen copy in `C:/Users/Z/AppData/Local/Temp/nurah-movement-independent-revision/` using the prior isolated source baseline with only the revised Nurah helper substituted.
This avoided root's concurrent interaction work and all shared outputs.
The copied submitted suite passed all 114 assertions with zero build warnings/errors.
The three mutations described above failed, after which the frozen helper was restored and a forced Rebuild passed all 114 assertions again.
An ordinary incremental build initially retained the mutant DLL because copying back the original file preserved its older timestamp; the forced Rebuild corrected that temporary test-artifact issue.
The earlier independent ten arbitration/serialization checks remain evidence for unchanged routines, but are not included in this 114 count.

The helper is suitable for the next separately reviewed integration stage under these limits.
Before physical availability is claimed, verify actual Unity actions and fallback visibility, the full native selector in a real save, and the separately authored click interaction and Main callback.

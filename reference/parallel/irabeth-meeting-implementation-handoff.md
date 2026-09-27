# Irabeth retained meeting implementation

Recovered author files compile and pass 23 focused assertions on 2026-09-26.
The prototype remains unregistered and awaits independent review.
It does not yet deliver a playable meeting.

## Original reviewed candidate

| File | SHA256 |
| --- | --- |
| src/IrabethMeeting.cs | 943E0921A81C374733859EED9867E92FE71C3ABC77B3DB50CEFB4143C552F952 |
| managed-tests/IrabethMeetingTests.cs | 41B390FE3AB87A233DC178D5A1022712287FE270E9FD780E716A6D23EEB2F5E6 |

These hashes identify the first candidate, not the later parent-readiness correction.
Independent review found that checking parent predicates did not establish that native arbitration had allowed those parents to play.
Root reproduced a child beneath a non-playing parent incorrectly returning eligible in the original implementation.
The focused test failed on that result before the production correction.
The corrected helper is named `ReadyUnderPlayingParents` and additionally requires every ancestor to be currently playing.
It lets native actor arbitration and synchronization establish parent readiness instead of predicting them.
Both placement and arrival already reevaluate the guard, so a parent becoming active can block its child's competing meeting at that later observation.
The corrected isolated build passes the original 23 checks and the new inactive-parent regression.
Independent native scheduling witnesses and review of the correction remain underway in `irabeth-meeting-parent-readiness-review.md`.

The implementation uses a separate native etude at priority 100 for an accepted meeting with the original retained living capital Irabeth after ordinary departure.
It checks the exact three audited background identities and their action structure.
It refuses the queen expedition, death history, ambiguous retained Iz representations and eligible competing native events, including pending lower-priority events.
Placement requires the held native claim and uses the audited native throne locator and retained actor evaluators.
Arrival additionally requires current actor evidence, native contact availability and position within 1.5 units of the locator.
Saved component data stores actor identity; the transient placement result is not serialized as proof of arrival.
No production code writes the claim dictionary, creates an actor or completes native history.

## Reproduced checks

The isolated source project is `C:/Users/Z/AppData/Local/Temp/irabeth-meeting-impl-3a02wrwp/Build.csproj`.
The isolated test project is `C:/Users/Z/AppData/Local/Temp/irabeth-meeting-impl-3a02wrwp/Check.csproj`.
Root built the test project in Debug and the source project in Release using the installed local dotnet executable, with zero warnings and errors.
Root then ran `bin/Debug/net48/IrabethMeetingProbe.exe`; all 23 assertions passed.
The runner resolves the newly built isolated Release source DLL.

Tests exercise production construction, component-data JSON serialization, pending-event policy, and actual native Etude activation, deactivation and reactivation.
The native lifecycle acquires, releases and reacquires the same authored claim without completing either history.
The fixture checks captured native logging for swallowed callback exceptions and finds none.
Claim-policy fixtures explicitly supply eligibility sets and set native held claims as test arrangement.
These arrangements do not prove the complete production eligibility predicate or selector scheduling inside Unity.
The lifecycle fixture has no valid physical actor and therefore does not demonstrate movement, visibility or arrival.

## Remaining work

Independent code review must assess predicate completeness, bracket lifecycle ordering, event yielding, source provenance and failed placement behavior.
Registration, update hookup, accepted-request story flags, physical scene gating and request release are not integrated.
Native archive construction must be verified in the shared managed runner before treating the synthetic construction fixture as archive compatibility evidence.
Live Unity placement, native event preemption, save/load, area transitions and ToyBox coexistence remain unverified.
Anevia's separate departure trigger can affect Arueshalae's quest and must not inherit this implementation without its own safe window.
Retained death, destroyed or missing actors and cross-area travel remain required subsequent cases.

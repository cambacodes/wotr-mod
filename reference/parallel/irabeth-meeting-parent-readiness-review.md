# Irabeth parent readiness independent follow-up

The revised parent-readiness policy passes the requested native scheduling witnesses.
The focused probe now passes 41 assertions, including 17 new assertions for four parent scenarios.
This resolves the earlier predicate-only parent scheduling defect for these tested cases.
It does not approve production registration or a playable physical meeting.

## Reviewed files and ownership

Root changed the production helper to `ReadyUnderPlayingParents` and retained fresh `Eligible` checks in both `Place` and `Arrived`.
I independently reviewed that change and added adversarial tests only in `managed-tests/IrabethMeetingTests.cs`.
I did not edit the production helper, previous review, shared build outputs or installed files.

| Input | SHA256 |
| --- | --- |
| src/IrabethMeeting.cs | 83298E08D0EFB395D743064A05BC9B170E277E330BCFF3DC4C9E972E5AA43C4B |
| managed-tests/IrabethMeetingTests.cs | 275E05D97FF5768DE4A0B19B4FDDCE8052B9259FA1879E4B1E3D65B5DEA89FB8 |
| Installed Assembly-CSharp.dll | 2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953 |

## Reproduction

Build the existing isolated `C:/Users/Z/AppData/Local/Temp/irabeth-meeting-impl-3a02wrwp/Check.csproj` with the local dotnet executable and `--no-restore`.
Run its `bin/Debug/net48/IrabethMeetingProbe.exe`.
The runner resolves the isolated Release source DLL, including the revised production helper.
The final test build completed with zero warnings and errors, and the run reported `TOTAL 41`.
The fixture's existing native logger check also found no swallowed callback exceptions across the new scenarios.

Initial fixture runs exposed missing detached-state infrastructure rather than production defects.
The final setup supplies a native CountingGuard and an explicit synthetic current area for `LoadEtudesForAreaPart`.
A synthetic unavailable area disables include-area-parts lookup because the fixture does not provide native child-area records.
No native method was patched or replaced to pass these checks.

## Actual native witnesses

| Scenario | Observed result |
| --- | --- |
| Parent begins inactive, child pending, meeting holds Irabeth | Production readiness initially rejects the child. The actual selector activates its parent while the held meeting blocks the child. A fresh call to the actual production readiness helper then accepts the child, and the actual production claim policy rejects the meeting. |
| Meeting withdraws after that rejection | The actual selector deactivates the fixture meeting without completing it. A later native selection activates the child and grants its actual Irabeth claim. No parent, child or meeting history becomes completed. |
| Playing parent loses a different actor group | The actual selector stops the parent and activates the higher-priority competing event on that other group. Fresh production readiness rejects the unavailable child, so it no longer reserves Irabeth. |
| Playing synchronized parent loses its dependency | Native synchronization stops the parent when its dependency becomes unavailable. The child remains inactive and fresh production policy no longer lets it block the meeting. No completion history changes. |
| An inactive parent itself claims Irabeth | The child is unready, but production ClaimsPermit independently sees the parent's own claim. After meeting withdrawal, native reselection grants that parent's Irabeth claim without completing any history. |

These cases invoke installed `EtudesTree.SelectPlayingEtudes`, including native parent traversal, actor filtering, synchronization, activation and deactivation.
They also invoke the actual revised `ReadyUnderPlayingParents` and `ClaimsPermit` methods through reflection.
The new scenarios do not substitute an eligibility hash set for those production helpers.
The older isolated policy cases still use supplied eligibility sets, as their comments describe.

## Explicit fixture boundaries

The meeting and native event blueprints in these new scenarios are synthetic facts with empty activation predicates.
They are not the registered production meeting blueprint or fully deserialized native events.
After the production claim policy rejects the meeting, the fixture makes its linked area unavailable to demonstrate native withdrawal and reselection.
This is an explicit test gate, not evidence that the full production `Eligibility.CheckCondition` ran in Unity.
Likewise, the synchronization scenario makes the dependency unavailable with that native area gate.

The fixture constructs native facts, parent links, roots and manager storage without loading a player save.
It does not write held claims to simulate the tested outcomes.
The native activation and selector methods acquire and release those claims themselves.
No actor, actor view, locator or successful arrival is fabricated.

## Assessment and remaining work

Waiting for native parents to play is a workable bounded policy here.
It avoids predicting native actor arbitration and synchronization inside the meeting condition.
The source's fresh checks in `Place` and `Arrived` are necessary because a parent can start in the same pass that the meeting still holds its claim.
The witness confirms the resulting pending child becomes visible to the production policy immediately after that native pass.
A later update must still perform withdrawal and reselection.

The tested correction does not require reading incomplete private selector sets or introducing a second scheduler.
Do not remove the post-selection readiness check or stop marking conditions dirty while the request is pending.
The actual update hookup remains an integration requirement.

Full production eligibility, native archive construction, bracket event dispatch, real movement, partial placement failure, post-load resume, area transitions, request release and ToyBox coexistence remain unverified by these tests.
The prior review's physical-placement and integration boundaries still apply.
This follow-up accepts the revised parent-readiness approach and its demonstrated native scheduling behavior, not the entire meeting feature.

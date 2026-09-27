# Irabeth meeting independent implementation review

The recovered prototype is useful but not ready for production registration.
I reproduced its 23 focused assertions and found a mismatch between its eligibility helper and the installed native scheduler.
The current tests do not exercise that helper or physical placement.

I reviewed `src/IrabethMeeting.cs`, `managed-tests/IrabethMeetingTests.cs`, the implementation handoff, the retained-actor positioning contract and the native selector witness.
I also inspected the installed native bracket and component-delegate classes with ILSpy and read the decompiled native EtudesTree, EtudesSystem, Etude and TranslocateUnit implementations.
I applied the ponytail and unslop skills to the review.
I did not author or modify the implementation or its tests.

## Reviewed versions

| Input | SHA256 |
| --- | --- |
| src/IrabethMeeting.cs | 943E0921A81C374733859EED9867E92FE71C3ABC77B3DB50CEFB4143C552F952 |
| managed-tests/IrabethMeetingTests.cs | 41B390FE3AB87A233DC178D5A1022712287FE270E9FD780E716A6D23EEB2F5E6 |
| Installed Assembly-CSharp.dll | 2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953 |

I ran `C:/Users/Z/AppData/Local/Temp/irabeth-meeting-impl-3a02wrwp/bin/Debug/net48/IrabethMeetingProbe.exe`.
Its runner resolves the existing isolated Release mod DLL and the installed native assemblies.
All 23 assertions passed, including the captured native callback exception check.
This rerun used the existing isolated build rather than rebuilding the shared project.

## Finding: predicate truth does not establish parent scheduling

`NativeEligible` at source line 158 traverses parents and checks completion state, campaign, linked area and activation predicates.
It never checks parent actor arbitration, synchronization requirements or whether the parent can actually play in the native selection pass.
`ClaimsPermit` at line 142 treats this result as sufficient evidence that a pending non-background event should block the meeting.
The departure check at line 132 also uses the same approximation to authorize the meeting's native context.

The native `EtudesTree.SelectPlayingEtudes` does more than this helper.
It removes candidates whose parents are neither playing nor starting, runs actor filtering, reevaluates those parent dependencies, runs synchronization filtering, and reevaluates the dependencies again.
`FilterOnActors` can remove a parent whose own actor group is held by another event.
`FilterOnSynchronization` can remove a parent whose required synchronized fact is absent.
A child of either parent can have true activation predicates throughout its ancestry while remaining unavailable to the real scheduler.

Consequently, an unavailable pending child sharing Irabeth's group can keep the meeting withdrawn indefinitely.
Conversely, checking departure ancestry through predicates alone does not establish that the native departure context can currently play.
These are defects in the helper's scheduling model, not a demonstrated failure in a particular player save.
The existing fixtures cannot disprove them because they pass `eligible.Contains` into `ClaimsPermit` instead of calling `NativeEligible`.

Before integration, add a witness with a nonplaying parent whose predicate is true but whose own actor group is blocked, and another with an unsatisfied synchronized parent.
Compare the actual native selector result with the production decision.
Also cover a parent becoming available during the same selection pass, since treating a currently inactive parent as permanently unavailable would exclude attainable pending events.
Use native scheduling evidence where practical rather than expanding a second partial scheduler without tests.
If conservative deferral remains deliberate for uncertain ancestry, report it as an unresolved availability restriction and do not claim complete native eligibility.

## Assessed correction approach

Root proposed waiting for native parent activation instead of predicting actor and synchronization arbitration.
This can work as a staged readiness policy if every ancestor is currently playing and the implementation rechecks pending events after native selection before allowing placement or arrival.
A newly activated parent must make its eligible child visible to that post-selection check immediately.
A subsequent dirty update must release any held meeting claim so the child can participate in native arbitration.
An ancestor that itself claims Irabeth must be examined independently as a pending event.

Do not treat private starting or stopping sets read halfway through predicate evaluation as a complete scheduling snapshot.
Their contents depend on how far the selector has traversed the roots.
A post-selector observation or a current-playing check with explicit later reevaluation avoids constructing another scheduler.
Required witnesses are a parent starting in this pass, a parent losing a different actor group, and a synchronized parent stopping in this pass.
This is an assessed correction strategy, not approval of code or evidence that the proposed implementation exists.

## Bracket lifecycle and placement

The choice of a native bracket is appropriate for placement after claim acquisition.
The installed `Etude.OnActivate` adds the claim, while `EtudesSystem.UpdateEtudes` raises the update event after native selection.
The bracket runtime enters or resumes under its component event context.
The generic component runtime also exposes the blueprint delegate through `ISubscriptionProxy`.
The production placement delegate uses that event context for its saved data.

The code resets transient placement certainty on activation and post-load.
Its saved actor identity remains separate from the transient `Placed` value.
`Place` verifies the held claim and reevaluates current eligibility before touching the actor.
It resolves the native location evaluators before moving or unhiding and verifies both native unit evaluators return the observed original actor.
No production path creates a unit, completes a native fact or writes the held-claim dictionary.

However, the lifecycle fixture invokes `Activate` and `Deactivate` on detached facts without a valid actor or actual update-event dispatch.
It does not exercise successful `OnEnter`, resumed placement, placement retry, or the delegate's update subscription after load.
A passing callback exception assertion in that fixture is not evidence that those paths ran.

Required placement tests must distinguish an unavailable locator, a failure during movement and a failure during unhide.
Confirm that physical choices remain closed, native event yielding still works and retries do not replace the actor or overwrite a newer placement.
Exercise actual event dispatch on both the bracket runtime and delegate, including post-load resume and claim reacquisition.
The current `Arrived` predicate appropriately requires fresh actor and held-claim evidence, usable native contact and distance from the locator, but its successful branch has not been witnessed here.

## Provenance and yielding

The observer requires the exact retained capital source, native actor identity, loaded saved ownership and registry evidence.
The meeting adds view identity, loaded scene, consciousness, hostility, combat and historical-death guards.
Its refusal of recorded Iz alternatives prevents silently adopting the capital representation of a different retained history.
The separate queen-expedition guard avoids treating that native commitment as a political departure.
These restrictions match the first implementation target.

The three allowed background identities have explicit action validation rather than a priority-range exemption.
The archived records inspected here agree with the intended hide and throne placement structure.
Full archive deserialization and construction still need a shared managed-runner witness, since the current constructor fixture builds synthetic equivalents.

For supplied eligibility sets, the policy correctly rejects unknown current holders and pending native events even when their priority is lower than 100.
It also withdraws a currently held meeting when such an event appears.
Native release, reselection and subsequent actor placement remain distinct steps.
The implementation correctly avoids restoring an old position during release.

## Acceptance boundary

Do not register this prototype as a delivered meeting until the parent scheduling finding is resolved or explicitly bounded and the construction and event-dispatch gaps are covered.
Registration, request acquisition and release, update hookup and physical story gating are still absent.
Unity movement, visibility, save/load, area transitions and ToyBox coexistence remain unverified.
The 23 assertions establish the narrow construction, serialization, supplied-policy and activation/deactivation behaviors described above.
They do not establish a playable return or complete route approval.


# Konomi personal meeting helper: independent review

Verdict: pass for the frozen helper and its documented caller contract.
No remaining helper blocker was found after the root-identified retry defect was corrected.
This does not approve narrative integration, physical arrival in Unity, full Konomi coverage or an installed release.
The reviewer did not author the production helper or repository tests.
I applied the ponytail review skill and unslop writing skill.

## Frozen artifacts and scope

| Artifact | SHA256 |
| --- | --- |
| src/KonomiMeeting.cs | FB9509E66E4D56053D2CE92A2DB6C42F1508E31C86F154415101B2A10D5243B2 |
| managed-tests/KonomiMeetingTests.cs | 18DAE46FA5D1C22177761C0014BFBFCAB4550193A9E7872AF80A5498222050AC |
| reference/parallel/konomi-meeting-implementation-handoff.md | DE4EC5652A1B03003E3E45B1613E2947355A1F663E4BA055CBF172FEAEB64A07 |

I read the entire helper, focused tests, [implementation handoff](konomi-meeting-implementation-handoff.md), [native placement audit](../canon-review/konomi-return-placement-audit.md), the shared parent-readiness helper and relevant retained-recovery provenance checks.
I inspected the extracted native HideUnit, TranslocateUnit and UnitFromSpawner bodies in `C:/Users/Z/AppData/Local/Temp/konomi-return-placement-l8f6kpb7`.
I coordinated the freeze directly with the author and waited for the corrected hashes before the independent builds and test runs.

## Native claim and actor findings

The authored meeting claims only Konomi's actor group at priority -90.
Its constructor validates the known hidden fallback at -100 and ordinary office at -20, including the repeating trigger, exact spawner and scene, native show/move order, locator, orientation and absence of save-hiding or fade behavior.
It reuses the native action instances without changing their arrays or owners.
The caller still must supply a genuinely new authored blueprint identity and register it before save restoration.

Priority alone would steal an unknown claim below -90.
The helper correctly adds an explicit policy gate: only itself and the exact hidden fallback are acceptable existing holders, and any other eligible pending claimant blocks the meeting regardless of priority.
Unresolved claim references fail closed.
The hidden fallback must itself be ready under actual playing parents, area, campaign and activation conditions.
The shared readiness method rejects unresolved parent references and cycles rather than manufacturing a playing parent.

The helper never restarts or completes Konomi's office, native rank-up, dismissal or selected-answer history.
It starts only its authored fact, and native activation and deactivation own its conflict claim.
There is no production direct write to the held-claim table.
It does not restore an old position or issue a late hide after another native event takes ownership.
Withdrawal lets the native fallback or the next native owner determine placement.

The actor must be the original retained capital representation with confirmed recovery identity.
Inspection requires agreement among source scene storage, spawner and entity registry, rejects conflicting saved capital representations, and rechecks life, consciousness, suppression, hostility and loaded view ownership.
Both native action evaluators must resolve that same actor.
The helper does not spawn, respawn or substitute an actor and does not treat a unit blueprint alone as identity proof.

The source preflights both native locators before mutation.
It then unhides, rechecks consent, claim and retained actor identity, and reads the actor's current view before movement.
That order is necessary because native unhide may replace a hidden dummy view while preserving the actor.
Arrival additionally requires a playing fact, its current held claim, matching saved actor/request, strict recovered contact, a non-dummy view and proximity within 1.5 units of the native locator.
An invitation or attempted unhide cannot by itself establish arrival.

## Consent, retry and persistence

The callback contract is explicit: a raw saved nonblank request identifies one accepted episode, and null or whitespace withdraws it.
It must not call Main.State or another observer that calls this helper.
The first accepted reply, second visit and an explicitly chosen retry require stable distinct episode identifiers.
A random, clock-based or per-frame identifier would defeat retry protection and is outside the reviewed contract.

Root found that the earlier implementation returned false after nonthrowing post-unhide failures while leaving Failed false, allowing automatic retries on every update.
The frozen AttemptPlacement helper now assigns failure in a finally block after the attempt result is known.
It leaves Failed false during its own eligibility and arrival checks, avoiding self-rejection of a successful attempt, then latches false or exceptional outcomes.
Place requests native condition reevaluation when that latch is set.
Pre-action ineligibility remains a deferral rather than consuming the invitation.

Saved actor, request and failure fields survive JSON round trips.
A failed episode is blocked on later checks, including after reload; a new explicit episode may retry only for the same saved actor.
Placed is excluded from JSON and reset on activation, resume and post-load, so a saved placement bit does not certify current contact.
Callback observation failures reject eligibility, and Tick requests native reevaluation for an existing fact rather than preserving the meeting solely because consent could not be read.

One integration detail deserves attention: a nonthrowing failed placement may leave LastError null while MeetingData.Failed is true.
Caller-side retry status must not infer failure exclusively from LastError.
The frozen helper has no dedicated saved-failure status accessor: MeetingData exposes its field, but SavedData(fact) is private.
Integration therefore needs a reviewed read-only status accessor or explicit inspection of the native fact's component data to observe the saved failure.
That status wiring is not implemented or approved by this helper-only review.
This is a caller requirement, not an unresolved automatic-retry defect in the frozen helper.

## Independent verification

I copied the isolated project configuration into `C:/Users/Z/AppData/Local/Temp/konomi-meeting-independent-792e6f63` and rebuilt production source into that temporary output.
The production Observer and original focused Runner builds both passed with zero warnings and errors.
The frozen repository suite independently passed all 43 assertions.

I then copied the focused test source into my temporary directory and added eight independent constructor-rejection probes.
They changed the office action to hide, enabled fade, enabled save-hiding, made the placement trigger one-shot, changed the position locator, changed the orientation scene, disabled rotation copying and changed the fallback priority.
Each mutation was rejected and restored in the detached fixture.
The augmented runner passed 51 assertions with zero build warnings and errors.
No repository tests, production source, shared build output or installed package were changed by these probes.

The tests execute actual installed native Etude activation/deactivation/reactivation, conflict selector arbitration, parent-readiness changes, fallback selection and stale-release protection on detached native objects.
The logger check found no swallowed native lifecycle callback exceptions in that fixture.
Selector tests provide candidate sets directly; they do not demonstrate a complete live game's eligibility-to-placement sequence.
The retry tests execute the real AttemptPlacement checkpoint with simulated true, false and throwing delegates.
They do not execute native unhide or movement through those delegates.
The runner's final reflection diagnostics are not extra assertions.

## Remaining integration and runtime work

The remote accepted reply and explicit retry must be reachable before physical contact for dismissed and preappointment histories.
The helper must be registered, ticked and supplied with the saved consent callback, and the authored request must be withdrawn when the visit ends.
An office actor already providing valid direct contact should keep that ordinary path rather than being forced through a personal meeting that correctly refuses to displace office placement.
When the addon temporary meeting owns Konomi, physical aftercare must require helper.Arrived(), not merely the recovery service's ReturnContactAvailable().
Unhide may make the actor visible before translocation and its verification finish.
When the existing native office supplies valid contact without the addon meeting owning the actor, temporary-helper arrival is not required.
Neither path may treat the invitation flag as arrival proof.

A Unity session still needs to establish successful unhide, dummy-to-real view replacement, locator movement, actual dialogue entry, withdrawal, native preemption and resumption, failure/retry and save/load behavior.
The standalone tests cannot establish those view-sensitive operations.
Missing views are deferred or rejected, not reconstructed; missing, destroyed, never-spawned and other unsupported actors remain separate recovery requirements.
This scoped engineering pass does not make those histories complete or make Konomi ready for full manual-route approval.

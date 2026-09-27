# Konomi meeting integration independent review

The frozen production wiring passes this bounded independent source and managed-fixture review.
No blocking defect was reproduced in consent selection, dialog identity, claim-aware contact policy, registration, or saved failure observation.
This does not establish successful live placement, completed route delivery, or an installed release.

I authored earlier Konomi recovery/observation changes and the original KonomiMeeting placement helper.
This review evaluates the other agent's Main integration and added request/failure/contact interfaces.
It does not independently approve my own earlier placement implementation, which has its own separate independent review.

## Frozen artifacts and reproduction

| Artifact | SHA256 |
| --- | --- |
| `src/Main.cs` | `6747C8F62EA075EED497A972E7C979A7E652630AEDB4C558A85EBEC06F98EA08` |
| `src/KonomiMeeting.cs` | `B7A30326CA868230F7153A8F9D7CCAED38CE2FCC453E11A2FF934DD96EA80238` |
| Original integration tests | `F8409CF34A97A7777769822A9D9175C89E9074945F01FEF416E7355CE7D10CC4` |
| Read-only 538-scene export | `8DCEB83D44925E5C07C7407D1FCEABE9381CE147D9A862B22E4E88420583C300` |
| Independent production build | `DA8EAA441A5D9388CC56EED124B7CB77C16A3608E21B049E7D482771D78E1641` |

The source and story hashes match the handoff.
The independent build also includes current Story.cs `68B2EC5FAB274A22583F61AA29AAB604079D63350DB37F1EDC00C98ACC811373`, whose new parent-ending metadata is absent from this 538-scene export and is outside this integration review.
No production file or shared test runner was edited.

The independent directory is `C:/Users/Z/AppData/Local/Temp/konomi-wiring-review-6505fb8b`.
Its temporary runner reproduces actual Main.Build and copies the integration tests locally for added adversarial probes.
The isolated Observer and Runner builds passed with zero warnings and errors.
The executable exited successfully and reported 67,314 assertions, 538 scenes, 19,445 generated blueprints, 14 native answer lists, one native Aeon sequence, and one parent-mod sentinel sequence.
The log is `independent-run.log` in that directory.
These counts include the preexisting managed construction suites; they are not 67,314 positive Konomi live-placement checks.

## Consent and correspondence

The raw request function requires authored verified-return progress, its saved timestamp, and the appropriate accepted invitation.
It observes the exact 12-hour first-visit and 48-hour followup boundaries without creating new episodes merely because time advances.
The saved timestamp uses the existing hour-plus-one convention correctly.
Long arithmetic prevents subtraction overflow at integer hour boundaries.
Missing, negative, or future recovery timestamps do not manufacture elapsed time.
Missing followup invitation or timestamp does not grant a later visit.

The first visit requires the new accepted reply.
An already completed first visit can use its separately earned followup invitation without retroactively obtaining the new letter flag.
The old romantic closed/farewell/parted flags do not cancel this separately accepted nonromantic recovery visit.
Explicit decline and completed second visit withdraw the request.
The current callback additionally requires the read-only recovered correspondence observer, supported chapter, embodied mythic state, and a suitable event window.
It reads raw native flags and does not call Main.State recursively.

The actual exported narrative grants first-visit completion and followup invitation together at the first visit's terminal answer.
The integration therefore changes to the followup episode only after that terminal progress is recorded.
Its 48-hour wait starts from the saved invitation timestamp.
Completing the second visit removes the authorization entirely.

## Dialog and contact gates

The event window accepts idle default mode or the exact registered dialog for the current visit in Dialog mode.
This allows the physical scene to retain its own actor while its continuing contact guard is evaluated.
The other visit's dialog, an unrelated same-name or same-GUID object, wrong game mode, combat, and scheduled native dialogue are rejected.
Reference identity is appropriate here because the own-dialog exception must refer to the registered authored dialog, not a lookalike blueprint.

Main.State now obtains physical return evidence through the claim-aware meeting observer.
The addon-held actor claim requires Arrived; strict direct contact alone cannot excuse an incomplete temporary placement.
Only the exact native office holder can use the original strict recovered direct-contact observer.
Hidden fallback, absent, rank-up, and unknown holders are rejected by this policy.
Correspondence remains a separate read-only observation, so a hidden living actor can answer without manufacturing physical access.

The contact dispatcher tests use controlled delegates for arrival and strict contact.
They prove dispatch and exclusion, including that the office branch does not call temporary-arrival logic.
They do not supply a positive native actor arrival witness.

## Retry and persistence

The registered retry flag supplies a stable saved counter shared by explicitly named first/followup episodes.
Time, ordinary observation, reload, and a failed placement do not increment it.
Negative counters reject consent; the maximum integer remains a valid observed episode but cannot be incremented.
The retry control is shown only with enabled and idle state, current consent, matching saved failure, positive current recovered correspondence, and room to increment.
Clicking rechecks eligibility, checks the counter, writes one increment, and ticks the helper.
This is an explicit retry of already accepted personal contact, not new romance consent.

SavedFailed reads the actual bracket runtime's saved data and requires its request ID to match the current accepted episode.
A nonthrowing placement failure is therefore visible even without LastError.
A different retry or followup ID, absent saved request, withdrawn consent, or an exception while observing consent does not offer that old failure as the current retry.
Normal deferred attempts remain distinct from saved failures.
The native actor identity checks remain in the placement helper and are not bypassed by incrementing the counter.

The counter, timestamp, and identity tests reconstruct GUID/value pairs using actual registered native flag identities.
The failure tests restore the bracket data through JSON.
These are meaningful persistence-component checks, not a complete game save/load test.
The positive live CanRetry path and the actual button's successful native placement were not executed outside Unity.
Their gating and increment behavior were source-reviewed; the report does not substitute that inspection for runtime proof.

## Registration and withdrawal

Actual Main.Build registers the authored meeting etude and retry flag before the normal initialization completes.
The test confirms cache identity, -90 priority, authored condition owners, placement component ownership, and preserved native office-action owners after the real initialization pass.
Native placement fixtures match the reviewed actor/spawner/locator action shape but are detached fixtures rather than a live deserialization of the office graphs.

Update ticks before the disabled and idle exits, and the toggle requests reevaluation immediately after changing enabled state.
That gives native arbitration a withdrawal opportunity when consent, event context, or enabled state changes.
The code adds no forced hide, direct claim-table mutation, history completion, actor respawn, or stale-position restoration.
Loading and unloading exits were exercised without mutation of the detached condition state.

Ordinary Tick in the standalone fixture reproduced the documented native LoadingProcess.Instance Unity ECall boundary.
The test accepts and reports that boundary; it did not prove successful native dirty scheduling for a live disabled meeting.
Actual withdrawal, native fallback restoration, and resumption after rank-up preemption remain runtime checks.

## Added adversarial checks and limits

Twelve independent assertions were added only to the temporary integration-test copy.
They cover missing authored return proof with saved acceptance, missing/future/negative recovery timestamps, extreme negative/positive game hours, a same-GUID unrelated dialog, the own dialog in the wrong mode, a scheduled interruption during the own dialog, a different explicit retry ID, missing saved request identity, and failed consent observation.
All twelve passed alongside the original suite.

Successful live correspondence observation, CurrentKonomiVisit authorization through all native loading/actor checks, retry-button placement, dummy-view replacement, native unhide and movement, physical arrival, entire scene playback, save/load, GUI rendering, and ToyBox execution remain unverified in this review.
The broader runner likewise does not execute real parent-mod initialization or portrait presentation.

The wiring can proceed to root integration on this bounded evidence.
The remaining required work is to register the new suite in the root-owned managed runner and verify the live hidden-actor first visit, 48-hour followup, failed-placement retry, event interruption, withdrawal, and reload behavior.
No production fix is requested from this review because no reproducible integration defect was found.

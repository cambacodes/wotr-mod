# Konomi return invitation independent review

The six-node remote invitation and its bounded engine support pass this independent source, rules, and literary review.
This is approval of a correspondence prerequisite, not approval of physical meeting delivery, a complete route, or Unity resurrection.
I did not author the invitation or these engine changes.
I authored KonomiMeeting, which is excluded from this approval and has a separate independent reviewer.

## Frozen inputs

| File | SHA256 |
| --- | --- |
| `storylines/konomi_return_invitation.py` | `FBC665C319EDFD34E2D74D19673D422C6F3D844B17F104A688AAC44A2E1F2610` |
| `src/Story.cs` | `2D4977F28B78BFAAE437A28851F1F7F833F2DE23547FABAA9E52C6961B597D59` |
| `src/Main.cs` | `663F7B0725F958263A7A8E6462641BAE08957A9FD81F3164C6717537EB659951` |
| `src/KonomiRecovery.cs` | `EE7A5B54055D5E59F42BB442FA9A90A8C500DCB28585388DC1A66A5F68996B18` |
| Isolated 538-scene candidate | `B4C04F1EAE41F553C7D264E66D0118CA78AA70FAEE8BAD20D154E74F5F57D532` |

The candidate is `C:/Users/Z/AppData/Local/Temp/konomi-return-invitation-oz6w6pdi/candidate.json`.
The independent harness is `C:/Users/Z/AppData/Local/Temp/konomi-invitation-review-e9840478`.
The installed or shared story export was not changed by this review.

## Literary and character assessment

These are editorial scores assigned after reading every node and choice, not predicted panel results or measured probabilities.
They apply only to this short connecting scene and its joins.

| Criterion | Score | Reason |
| --- | ---: | --- |
| Character voice | 92/100 | The precise request, controlled impatience, marginal correction, and threat to become diplomatic preserve her verbal control while allowing temporary weakness. |
| Prose and pacing | 93/100 | The folded letter, uneven handwriting, and returning paperweight give the exchange concrete actions without prolonging the consent decision. |
| History and canon boundaries | 94/100 | No restoration of office, council authority, romantic commitment, or old intimacy is asserted across dismissed, unappointed, closed, and lover histories. |
| Agency and mature emotional treatment | 95/100 | She invites, limits the visit, and reserves the right to end it; the Commander can accept, decline, send good wishes, or postpone. |
| Joins and branch clarity | 92/100 | The reply supplies the missing prerequisite for physical aftercare and keeps actual arrival pending. |

The scoped editorial assessment is 93/100.
This meets the requested above-90 threshold for this addition, without certifying the aggregate route's word count or every other review dimension.
Erotic intensity and art are not scored here because this is recovery correspondence with no new artwork.
Adding erotic material merely to raise a heat score would weaken the scene's immediate purpose.

I compared the voice with the extracted native dialogue in `reference/expansion/konomi.txt`, especially cues `541da47fd4fa7e945ae5897a2fe727f6`, `f363c2703c8c3934f84da229cf4d9710`, `4588ef15ddaf96f4e88e56201a9ab51a`, and `a3718819afdf0c54c8af64a39561a174`.
Those exchanges establish controlled changes of tone, confident correction, political calculation, and dry rebuke.
Her softer post-return reply is an authored alternate development, not a quoted native reaction to resurrection.
The invitation preserves enough of that precision to avoid reducing her to a generically grateful patient.
Its preference for hearing the Commander's voice is personal interest, not an automatic romantic declaration.
The earlier retained-return map scenes establish the stationery motif, so the animated map here is a callback rather than new unexplained machinery.
The physical first-words scene still asks for the actual account, which the letter explicitly postpones until the visit.

The hand-signature detail does not require a prior private romance, and the narration does not claim that the reader recognizes an established lover's handwriting.
Prior breakups remain in the saved history and are not silently withdrawn.
The line about no title under her signature concerns this personal letter, not loss or restoration of her public title.
No branch promises a finished recovery, a full reunion, or an immediate available body in Drezen.

## Branch and timing findings

The request reaches the reply and then either acceptance, refusal, or postponement.
The good-wishes choice has its own refusal-compatible terminal response.
Both postponement choices abort without completing the scene or setting accepted/declined state; the player may reopen the correspondence.
Reopening after reading the reply rereads the letter from its beginning, which is modest repetition but does not invent another accepted appointment.
Acceptance writes only `konomi.return_meeting_accepted` and the completed scene ID.
Decline and good wishes write only `konomi.return_visit_declined` and the completed scene ID.
There is no forced commitment, office change, removal of another romance, or claimed physical arrival.

The first physical aftercare scene now requires accepted correspondence in addition to its existing confirmed-return and strict contact requirements.
A prior completed first visit remains completed and forbids the new letter, so it is not made to earn consent retroactively.
The letter waits 12 game hours from the recorded confirmed-return progress timestamp.
`Main.RecordProgress` writes the timestamp before its corresponding authored progress flag, including when a pending native return is reconciled.
The rule tests independently distinguish hour 11 from hour 12.
As elsewhere in this rules engine, a manually fabricated progress flag with no timestamp uses the existing no-timestamp fallback; this is not evidence that a normal verified return skips the wait.
No delivery time is separately simulated for each paragraph of correspondence.

## Engine and evidence boundaries

`ReturnCorrespondenceAvailable` is a read-only observer.
It requires `TryLoaded` to establish the current retained actor, followed by confirmed historical return for that exact living actor, consciousness, and lack of suppression.
`TryLoaded` checks the loaded source area, saved-storage uniqueness, post-load scene state, actor/spawner provenance, a conscious Commander, absence of combat/loading, and no hostility toward the Commander.
This deliberately does not require an active rendered view, because an alive hidden retained actor must be able to answer before a personal meeting can reveal her.
No observer branch calls resurrection, creates an actor, moves an actor, completes office history, or changes consent.
Strict physical contact remains a separate observer and still requires native contact availability.

The remote `AfterRecovery` validator requires the Konomi relationship, recognized revival, confirmed-return prerequisite, remote delivery, no physical contact binding, and current correspondence evidence.
A physical contact binding still requires the exact Konomi unit and physical contact evidence.
Removing the physical binding from an existing physical scene without adding the remote evidence is rejected.
Authored choices, scene completion identities, relationship flags, and native alias maps cannot manufacture the correspondence or recovery evidence reserved by validation.
`Main.State` recomputes correspondence availability instead of storing the observation as a new authored success flag.
In-progress remote contact is rechecked through the same prerequisites, area/chapter boundaries, death restrictions, and other native exclusions.

## Independent checks

The isolated rules harness passed 1,086 assertions.
It ran `RetainedRecoveryRulesTests` and `KonomiReturnInvitationTests` against the candidate, then added independent 11-hour/12-hour boundary checks, in-progress inhuman and Chapter 4 rejection, prior-first-visit exclusion, and forged correspondence aliases in all six native binding maps.
The supplied invitation suite traverses all six nodes across Chapters 3 and 5, active/dismissed/unappointed office histories, and unmet/lover/closed/farewell/parted histories.
It checks both postponement outcomes, decline and acceptance, preservation of existing flags, no invented physical access, and continued physical gating after acceptance.
The relevant full source compiled against the installed native assemblies in an isolated Observer project with zero warnings and errors.
The unrelated unfinished `ParentEndingAlternate.cs` was excluded from that compile.
The rules build also had zero warnings and errors.

These tests supply correspondence and physical proof in rule snapshots.
They do not establish a positive loaded Unity call to the new correspondence observer.
The current observer's positive behavior is supported here by source inspection of its existing retained-actor and confirmed-return checks, not by a successful loaded-save witness.
Root separately reported a complete 538-scene rules run with 24,445,936 checks; I did not rerun that broad suite and do not include it in my independent count.

## Remaining integration

The remote prerequisite can be integrated on this review's scope.
It does not itself make a dismissed or preappointment actor visible or reachable.
Physical helper registration, stable saved request identifiers, failure-aware explicit retry correspondence, and arrival-gated aftercare remain separate implementation and review tasks.
The invitation flag alone must never substitute for a current physical arrival witness when the temporary personal meeting owns her placement.
An explicit retry must be available after a failed placement and must not be generated anew each frame.
Actual hidden-actor correspondence, native unhide/view replacement, movement, save/load, rank-up preemption, and first/second physical visit delivery still require their own verification.

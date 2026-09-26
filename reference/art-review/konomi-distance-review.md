# Konomi distance continuation: integration audit

No blocking defect was found in the reviewed offline integration.
The three scenes preserve native dismissal and established relationship stages while recording correspondence and a private return.
This review covers source, exported state and test logic, not a full writing review, actual Unity execution, artwork or live ToyBox behavior.

## Exact reviewed revisions

| File | SHA-256 |
| --- | --- |
| `storylines/konomi_distance.py` | `BA7AB0AD64D3ECA8053E2DC82DE3B81424C0F2A24850E413420ED334A9E8A403` |
| `expansion.py` | `E44CABBA53AF4BC50714CB13B5BD36F80A8400D20C70098BCDD5885DC9601B20` |
| `tests/Program.cs` | `80B6CEB553C9D13E574A8669EC54D6EB935B6EB3B7BF57D1638EDB01CFB083E4` |
| `development/Story.json` | `D6843A4F75C6C14C8C84D3CA126F4981FDF76224AC34371D8EACEB246DE8C867` |

The exporter imports `konomi_distance` and includes its scene list once.
I inspected the exported records for `konomi.capital_letter`, `konomi.return_offer` and `konomi.private_reunion`; their flags, delays and location constraints match the source.
No new engine code is part of this review.

## Availability, history and return

All three scenes use remote books, restricted to Drezen in chapters 3 and 5.
All require the selected native dismissal, completed officer etude, private departure and private address.
They forbid ordinary officer presence, inhuman state and the original farewell, while the existing relationship-closure rule remains effective.
They do not require current Trickster status.
Their prior authored departure and address provide the continuation prerequisite, so changing to Legend after the earlier Trickster opening does not erase established access.
They do not independently grant that opening to a Legend campaign without those prior facts.

The capital letter additionally requires agreed private correspondence and waits 336 hours after the latest timestamp among its prerequisites, normally departure.
The return offer requires the sent answer and waits 168 hours.
The reunion requires confirmed return and waits 336 hours.
These are game-time waits rather than simulated courier or travel entities.
Native history does not acquire a timestamp through these scenes.
The existing missing-timestamp fallback remains unchanged for legacy or externally supplied authored flags.

The callbacks distinguish the requested letter subject, the Commander's carrier-yard contribution, the outgoing reply, the confirmed activity and the earlier discussion of other partners.
The valid prior sequence supplies one of each relevant pair.
Fallback branches use absence of the first option, so arbitrary edited states with both or neither flags are not independently repaired by this content.
That is not a demonstrated failure in the reachable authored sequence.

Choosing continued visits can add attraction and private interest; it does not grant lover or commitment status.
Taking time does not automatically kiss Konomi.
No choice clears native dismissal, sets ordinary presence, changes trade or officer state, or resets another romance.
Normal addon scene-completion, timestamp and journal bookkeeping still applies.

The reunion records `konomi.private_returned` and `konomi.reunion_kept` while retaining `konomi.private_departed`.
Here `private_departed` remains a historical milestone and a blocker for the earlier local-visit sequence, not a live physical-location predicate.
Retaining it prevents the earlier carrier-yard visit from reopening after the temporary return.
The new return marker does not unhide, move or spawn a native actor.
The ending's promise of another evening is a continuation opportunity, not an additional scene implemented by this file.

## Test evidence and limits

`CheckKonomiDistance` walks scene outcomes for both chapters, new/lover/committed histories and both selected callback configurations, using a Legend snapshot with established prior access.
It checks remote entry targets, each missing requirement, all blockers, chapter-four separation, wrong area, postponement without flag progress, one-time completion and native/relationship preservation.
It checks the first arrival at 335 versus 336 hours since departure and checks each subsequent delay immediately after the preceding completion and one hour before its boundary.
The next iteration then requires the scene to open at the exact boundary.
Those are appropriate timing checks for the production rule semantics.

The test verifies callback destinations and exclusive outgoing response/activity flags, the chosen reunion pace and the lack of a kiss on the slower branch.
Its return check supplies all old carrier prerequisites without adding the old scene's completion flag and still requires the carrier scene to remain unavailable.
That meaningfully exercises the retained-departure blocker rather than relying only on one-time scene completion.
The two callback configurations cover both sides of each earlier subject/contribution choice, but do not exhaust their four-way Cartesian combination; the inspected conditions are independent.

The owner reports 142,154 passing rule assertions after the editorial continuation update.
I inspected the tests rather than independently rerunning the suite.
No actor restoration, actual save/load, portrait deployment or live ToyBox compatibility result is inferred from those assertions.
For this bounded authored-state continuation, no further defect requiring a source correction was identified.

## Editorial graph follow-up

I inspected the added personal-conversation branches and the relocated prior-partners condition.
The reunion's existing hand, kiss and slower-pace routes still join `partners`.
That node now offers sleeplessness, a good evening or declining to explain more tonight.
The sleepless branch divides into `kinder` and `sooner`; both return to `schedule`, as do `good_evening` and `content`.
The prior `private_other_promises` choice pair now lives at `schedule`, and the test's destination check points to that node.
The new intermediate choices do not add state effects, conditions or abort points and do not bypass the final completion node.
The scene availability and delay settings remain unchanged.
No new graph dead end, cycle or commitment effect was observed.
The room's music description and the letter's common join remain prose changes within the existing progression.
The review remains an integration assessment, not a new full-route writing score.

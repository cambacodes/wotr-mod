# Nocticula Trickster acquisition opening: author handoff

This is an unregistered beginning of a contact quest, not a completed acquisition route or an approved romance.
Only `storylines/nocticula_trickster_acquisition.py` and this report were written.
Source SHA256: `7336233EF283E6E87E2EC6A77ACC3463422B221A1FA1DD140ECCC5A7BE1348B8`.
A different reviewer must assess the actual prose, native attachment proposal, source paths and remaining acquisition work.
No review score is assigned here.

## What is implemented in source

Three history-specific request variants share the same genuine native audience opportunity.
They distinguish no active parent agreement, recorded parent rejection, and active prior romance with separately evidenced lost or renewed patronage.
The intact accepted-parent/original-Gift route is excluded from reacquisition.
An initial encounter or interrupted offer is not described as an accepted relationship.
The rejection answer remains readable and is never erased.
Original, absent and renewed Gift histories receive separate later player responses.
No stat-granting gift is supplied by this correspondence.

The Commander requests a way to ask for another meeting before leaving the actual audience.
Nocticula permits a divided wax impression which can carry a request; she does not promise to answer or offer romance.
The story object is authored and is not an inventory item.
A candid request and a watchful, self-interested answer receive different immediate responses and retained history, without pretending those initial attitudes already constitute two separate political outcomes.

Two later visits require the actual native Council disclosure answer and reward response, as well as the earlier addon request and seal.
The Commander cannot select a custom response that merely asserts the native intelligence has been delivered.
The first visit prepares a narrow, addressable question in Drezen.
A one-shot Arcana check can preserve a narrow reflection channel.
The non-roll option sends a closed packet and accepts slower, written contact.
Failure exposes the attempted construction, closes the opening, and requires a different exchange rather than another roll at the same aperture.

The next visit supplies the authored response through the matching mark Nocticula withheld at the actual meeting.
It is not a picture reconstructed from the Commander's memory.
The source distinguishes narrow contact, deliberate letters and repaired contact after exposure.
Repair requires surrendering the working sketch, leaves the original fold unusable, records the exposure and surrendered information, and yields letters only.
Refusing that cost ends this contact attempt without granting a trial agreement.
These are persistent addon history and witnessed story consequences, not stat loss or a hidden gold deduction.

The endpoint is `noct.acq.correspondence_trial`.
It is permission to exchange further proposals, not an accepted romantic pact.
The relationship's CommittedFlag is the future, unwritten `noct.acq.renewed_agreement`, so the first successful reply does not represent completed courtship.
No present scene produces that flag.
Noct remains demanding, remembers rejection and wants a concrete political proposal before another private invitation.
The next work must supply the concession and actual personal offer rather than jumping from this trial into the existing harbor scenes.

## Fresh native hook verification

I read `reference/canon-review/nocticula-trickster-acquisition-map.md`, nearby acquisition helpers and supported schema fields.
I also inspected the actual native JSON in the installed `blueprints.zip` for this audience.

| Native evidence | Verified ID |
| --- | --- |
| Chapter 5 Trickster Nocticula dialog | `2c57f65d4b98d764d98794ae8ef9ffdd` |
| Audience Cue_0006 | `20451daada07f744b9d7f3e14a37a864` |
| Its AnswersList_0007 | `2729c49e2bf20c64caa4f54b352e03f6` |
| Actual Council disclosure answer | `fd4f6c1d6397fa94db7aaf08de7dfeca` |
| Reward Cue_0016 | `bb552fe4e21cb874fa3c98c2cc328186` |
| Following departure Cue_0019 | `19a0d2e4bae6246469852a4abf7705e6` |

The reward cue does not return to that answer list.
It continues to Cue_0019, whose OnStop teleports the party and hides the portal.
Therefore the new request is proposed at AnswersList_0007 before departure, with the later correspondence separately gated by the disclosure and reward.
Requiring the reward before inserting a request into a never-revisited answer list would have produced an unavailable hook.
This source avoids that assumption.
Actual insertion, conversation resumption and book-event ordering have not been tested in Unity.

Bindings for parent Active/Reject, original and renewed Gift, original Gift completion, broken/refused patronage and the Council fight come from the verified map.
They are read-only dictionaries.
The module does not register them globally or write their aliases through choice effects.
It does not play parent questions, acceptance cues or romance bookkeeping by assertion.

## Post-conflict scope

A separate source scene prepares an unsent request after a verified Council resolution.
It requires `noct.acq.conflict_resolved_verified`, for which this module supplies no producer.
The current fight and NocticulaDead flags alone cannot admit it.
This is intentional: the fight can start the death etude before an observed kill.
The preparation describes neither a corpse nor a restored body or government.
It refuses to count a remembered voice as her answer.

The native Threshold Trickster response is retained as a read-only reference binding, not used to pretend the Chapter 6 projection has already happened in Chapter 5.
`noct.acq.postconflict_reply_verified` is named as future incomplete work and is never written.
There is no implemented post-conflict channel or romance acceptance in this opening.
A later producer must establish actual political resolution and an independently answered identity test, then supply appropriate hostile negotiations.
The scene is an explicitly blocked preparation draft, not advertised as a working recovery path.

## Delivery and count

The file contains six scene definitions and 37 delivered nodes.
Three definitions are mutually exclusive audience-history variants sharing the same later request passages.
They are not three times the playable content.
The other definitions are channel preparation, the first reply, and the separate blocked post-conflict preparation.
Living follow-ups use Chapter 5 Drezen and twelve-hour minimum delays.
The native request is physical and attached to the verified answer list in source.
Later living contact is remote through the specifically authored seal mechanism.
The post-conflict preparation is manual/remote because it contains only the Commander's unsent work and cannot represent a living contact actor.

A separate played-path traversal using the repository tokenizer measured one request variant plus both living follow-ups, counting only displayed prose and the selected answers.
It excludes declined attempts, repeated postponements, incompatible variants and the separate post-conflict preparation.

| Source fixture | Minimum selected words | Maximum selected words |
| --- | ---: | ---: |
| Missed agreement, no original Gift | 1,582 | 1,931 |
| Missed agreement, original Gift | 1,581 | 1,930 |
| Recorded rejection, no original Gift | 1,603 | 1,952 |
| Recorded rejection, original Gift | 1,602 | 1,951 |
| Lost original patronage with active prior agreement | 1,582 | 1,931 |
| Renewed Gift with active prior agreement | 1,581 | 1,930 |

These are introductory acquisition words, not a 21,000-word route claim.
They cannot be added to an arbitrary existing maximum to declare recovered-entry compliance.
Joined continuations will need compatible history-specific prose and an independent selected minimum recount.

## Actual local checks

`python -m storylines.nocticula_trickster_acquisition` passes.
The maintained source tests verify unique scene/node IDs, reachable graph nodes, acyclic paths, valid local targets, supported Check/Next shape, and addon-only writes.
The check sets its attempt flag and forbids another attempt.
The fixture traversal exercises six starting histories and 36 successful trial outcomes, including narrow, deliberate written and repaired-written channels for each history.
It checks that native disclosure remains required after receiving the seal and that a refused repair cannot write trial acceptance.
It excludes intact accepted romance, non-Trickster entry, the Council-fight state and the death alias from the living audience.
Death plus fight alone does not admit the blocked post-conflict preparation.
No test writes the incomplete resolution/reply producer, parent history, romance completion or new romantic agreement.

The separate counting traversal also exercised closure outcomes, bringing its total enumerated reply results to 48 before excluding closed histories.
Compilation/import and the source whitespace check passed.
These fixture states are test inputs, not observed native saves or proof that acquisition has occurred.
No C# suite, actual audience click, rest event, save/reload or ToyBox configuration was exercised.

## Remaining work and review priorities

The living path still needs an explicit concession quest, responses to Shamira's surviving political interest where relevant, a bounded Worldwound or crossroads proposal, and an actual personal invitation with acceptance or refusal.
The life-history callbacks need separate review for each recorded parent refusal and interrupted-offer scenario.
A player who already left the native audience without this request still needs a separately earned recontact path; the current source does not invent another palace visit.
Pending versus resolved Council combat and post-conflict response identity need real producers before that branch can be registered.
No body resurrection, government restoration, essence-item transaction or native quest advance is implemented.

The existing harbor continuation cannot simply consume `correspondence_trial`.
Its earlier-bargain wording, Gift assumptions and command of living city agents require explicit compatibility work after an actual renewed agreement.
Native binding registration, relationship registration, export, engine validation and in-game actor/contact delivery remain root-owned future work.
Portrait fields currently use the general Nocticula key; a default image is not approval of the letter, empty frame or remote scene depiction, and no art assignment was reviewed here.
Independent review should challenge the seal's bounded capabilities, the value of the failure concession, the meaning of an authenticated reply, and the distinction between hearing a request and accepting a lover.

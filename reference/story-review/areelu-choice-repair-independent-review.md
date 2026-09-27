# Areelu selected-choice repair independent review

## Scope and snapshot

The frozen source SHA-256 before and after review is `EC26B251855F2CEFBBB6236AC43077E218CEA718632C044CCEA8E5D591F57D3C`.
The development-record SHA-256 is `DE61A15CCBE1438C11BA5145478975E4CBE21F1FFFBFFD906310E1BDD215917D`.
I did not edit either file during this review.

A different author made the routing and scheduling repairs reviewed here.
I previously authored some unchanged prose and the earlier power-bargain material, so this report does not independently approve or rescore that prose.
It independently examines the new repair pages and graph transformations and records reproducible defects and measurements across the resulting manuscript.
The separate prior literary review remains applicable to unchanged material.

The repair is useful but does not pass the complete-route gate.
The enumerated local refusal, privacy, memory and gate-aftermath changes mostly work in the Python model.
Shorter committed routes remain below 21,000 words, several timing and agency contradictions survive, and the transformed node order disagrees with the existing C# delivery implementation.

## Verified repairs

The module self-check and Python compilation both pass.
The module reports 30 unintegrated scene dictionaries and 210 nodes.
I inspected the actual choice destinations and new pages in addition to running those assertions.

The private counterledger visits `inventory_private_consequence`, and its reply visits `reply_private_findings` rather than the public submission and public reply.
The later hearing explicitly obtains a different field ledger and states that a private counterledger remains closed.
The professional-only reply bypasses the romantic proposal.

The wait-before-touching answer now visits `reply_no_touch`, which lowers the offered hand and preserves distance.
The private kiss has separate continuation, kiss-only and departure pages.
The departure releases the Commander and sends him to his own room.
Its later courier note is a distinct twelve-hour followup and does not claim he stayed overnight.

The dinner refusal visits `returned_declined_dinner` rather than dinner.
The no-touch dinner outcome avoids the former face-touching continuation.
The inspected relationship-ending answers reach `returned_nonromantic` and do not traverse dinner or desire reaffirmation afterward.
The solitary walk exits through the professional notice rather than forcing shared company.

The copy-scene ending goes to `copy_end`.
The nonphysical evening exits through `copy_nonphysical`, and its subsequent graph avoids the later intimate meeting.
`copy_second_contact` leaves her hand on her own side of the table until the player chooses contact.
The protected-memory branch reaches `copy_protected_entry`, explicitly describes an inert transcript and intact recollection, and does not claim the Commander made the declined contradiction.

The gate aftermath distinguishes a live unresolved hazard, an ordinary closure with the archive intact, and a closure that spent the archive.
The unresolved page preserves evacuation and the longer water route.
The ordinary marker page does not commemorate an imaginary sacrifice.
Only the spent-anchor branch reaches the lost-archive follow-through.
The later partnership argument is now hypothetical rather than asserting that the Commander spent an archive on every history.
The late breakup's letter-sorting page no longer touches the Commander.

The previously quoted sentences about a game storing an ending, a penalty in the story, and a campaign having an ending were removed.
That narrow repair does not establish that all production language is gone.

## Remaining agency and narration defects

`unmeasured_wants` offers a handholding answer explicitly keeping the evening nonsexual.
It reaches `unmeasured_touch`, where the pair talk for an hour and the Commander leaves.
That page's only answer is nevertheless ?Continue to the morning conversation,? sets `unmeasured_night_shared`, and immediately enters `unmeasured_after` without a scheduled boundary.
The prose does not describe a night spent together, and a later writer could misread the shared-night flag as evidence that one occurred.
Separate the quiet departure from the overnight result.

The kiss-only invitation in `unmeasured_wants` still reaches a page that supplies a second kiss, a private night, an affirmative answer to staying until dawn and morning coffee without another player choice.
The narration says these were mutual choices, but the selected answer only asked for a kiss and said the next step should be a question.
The earlier private-kiss repair has not been applied to this parallel encounter.
Give the player the promised next decision or explicitly label the selected answer as accepting an overnight encounter.

`choice_last_page` still says that the final page records the ?relationship state? and enumerates commitment, open continuation, pause and end.
`choice_paused_future` says what ?The ending does not say,? and `choice_closed_future` says what ?The ending preserves.?
These remain design-summary narration rather than letters the characters would actually write.
The new lexical assertions omit these surviving expressions.

The repaired `choice_day_apart` correctly respects leaving the study.
It schedules the next meeting instead of immediately supplying companionship.
That repair should be retained.

## Scheduling and current engine compatibility

The split produces fourteen authored main sequences plus sixteen scheduled followups.
The longest measured path visits all thirty scene dictionaries.
Their delay fields sum to 3,216 hours, or 134 days.
I independently reproduced that sum and that path's scene count.

The number assumes sequential minimum delivery and correctly timestamped prerequisite flags.
It is not an observed campaign duration.
`Rules.Available` in `src/Story.cs` uses the latest available timestamp among a scene's required flags, so actual timing also depends on the future writers of persistent entry and path flags.
There is still no evidence that 134 days of Chapter 5 availability is attainable, well paced, or compatible with every intended campaign history.
That needs a campaign-level acquisition and scheduling plan, not only a sum of delay fields.

Several page-local time jumps remain.
`copy_pause` says that a message arrives three days later, then its answers continue inside the same BookEvent to `copy_close` or `copy_end`.
`returned_entry_active` says that the letters arrive over the next ten days, while the sequence can become available after a seven-day delay from the hearing's completion.
`gate_residents_revisit` says the residents open the route the next morning, but follows `gate_followthrough` inside the same event.
The survey-station kiss narrates an overnight stay and morning inside one event.
The handoff's blanket claim that no campaign clock is silently advanced by page narration is therefore too broad.

There is also a concrete mismatch between the Python traversal and the existing C# implementation.
The Python checks begin at each dictionary's `Entry` node.
Current `src/Main.cs` opens `scene.Nodes[0]` for a BookEvent, and `src/Story.cs` validates graph reachability from `Nodes[0]`.
The C# `Entry` field is used as entry-answer text, not as the graph's starting node.

| Scene | Python starting node | First stored node |
| --- | --- | --- |
| Returned names | `returned_entry` | `returned_entry_active` |
| Private copy | `copy_entry` | `copy_entry_active` |
| Residual gate | `gate_entry` | `gate_entry_active` |

Starting from the first stored node leaves the guard node and its professional-only page unreachable in each of these three scenes.
I reproduced those missing-node sets from the frozen dictionaries.
Directly registering those dictionaries would therefore fail the current reachability validation and, if that validation were bypassed, start beyond the new ended/paused/professional guard.
Place the actual starting node first or supply a verified export transformation; no such Areelu integration exists now.

Two current skill choices also contain both `Next` and `Check`: `record_entry` and `gate_entry_active`.
The existing C# validator explicitly rejects that combination.
Python topology and selected-path tests do not apply that schema rule.
These are static integration blockers inferred directly from current source, not claims that an in-game execution was performed.

## Independent selected-path measurement

I traversed the imported thirty-scene dictionaries in order, carrying predicate-relevant flags and exploring both skill outcomes.
The traversal counts selected prose and selected answer labels using the tokenizer from `tools/measure-story-content.py`.
It rejects aborts and closed, ended, paused or rivalry-only outcomes.
Unavailable branch followups are skipped, rather than charging their text to another history.
Completed paths must contain `relationship_committed`, `route_record_sealed` and `ordinary_future_chosen`.
The fixture assumes `entry_ready`, active Trickster, verified cradle record and an available non-declined native answer.
It does not demonstrate acquisition of those states in-game.

| Compatible completed trajectory | Minimum selected words | Maximum selected words |
| --- | ---: | ---: |
| Any active committed trajectory | 15,255 | 25,610 |
| Private research pact and power-partnership terms | 17,459 | 25,610 |
| Protected memory, private counterledger, ordinary grounding | 16,099 | 23,083 |
| Protected memory, private counterledger, unresolved gate | 15,255 | 23,122 |

All three author-reported maxima reproduce exactly.
They do not establish the user's minimum for every completed route.
The shortest active committed trajectory is 5,745 words below 21,000.
The pact's shortest compatible committed trajectory is 3,541 words below the floor.

The 15,255-word example visits nineteen scene dictionaries, with delay fields totaling 1,728 hours, or 72 days.
It protects the memory, keeps a private counterledger, begins the relationship without touching, declines the first private evening, chooses a solitary walk, keeps the later copy meeting nonphysical, leaves the gate unresolved, keeps the survey-station meeting conversational, and commits without the final private night.
Those are ordinary selectable limits inside a continuing romance, not a breakup or an aborted route.
Its ending still seals the letters and reaches the ordinary committed future.
The shorter optional-intimacy choices currently remove long subsequent sequences without replacement relationship content.

The maximum route's length also remains a numerical result rather than proof that all its prose is meaningful.
The extensive repeated audit, consent and correction discussions identified in the earlier independent literary review remain substantially present.
This report does not independently approve the earlier prose I helped author, and a different literary reviewer still needs to assess the revised complete manuscript after its planned middle-section rewrite.

## Character and premise assessment within repair scope

The new private-counterledger response allows Areelu to defend her ownership and tell the Commander to read the second page before judging her.
The ordinary-gate page gives her a reason to value preserved precision instead of obliging her to praise sacrifice.
The unresolved-gate disagreement gives the local representative a practical cost and lets Areelu answer with a usable survey position.
Those pages are sharper than the longer discussions they now surround.

The adult unrelated AU premise remains explicit in the contract and is not presented as recovered native biography.
The protected-memory repair preserves uncertainty about the graft without converting the Commander into a romantic version of the lost child.
Actual player-delivered opt-in disclosure and native history verification are still missing.
I carry forward the prior independent review's premise assessment without granting a new self-review approval to unchanged writing.

## Repair-scoped scores and disposition

Every applicable score must be strictly above 90; passing a local repair dimension cannot compensate for a failed route dimension.
These scores do not replace independent characterization and prose review of material I previously authored.

| Dimension | Score | Finding |
| --- | ---: | --- |
| Enumerated refusal/departure repairs in the Python model | 93 | The inspected original defects now take faithful separate pages. |
| Private/public, protected-memory and gate-result repairs | 93 | Distinct history pages preserve the selected facts in the local model. |
| Whole-manuscript agency/state consistency | 78 | Survey-station kiss escalation and false shared-night flag remain. |
| New repair-page character specificity | 92 | Private ownership and ordinary/unresolved gate arguments give Areelu concrete resistance. |
| Production-language cleanup | 83 | Exact cited sentences removed; relationship-state and ending-summary language survives. |
| Timing fidelity and campaign fit | 66 | Scheduled boundaries improve the model; unscheduled jumps and the unverified 134-day Chapter 5 budget remain. |
| Current engine schema and entry compatibility | 42 | Three first-node mismatches and two invalid check/next combinations block direct delivery. |
| Every-route numerical minimum | 58 | Compatible committed routes fall to 15,255 words. |
| Earlier prose quality and meaningful-length approval | Not rescored | Prior authorship prevents an independent approval of that material; prior literary blockers remain. |
| Runtime, native acquisition, persistence and ToyBox | Unverified | No registered implementation or live evidence supplied. |
| Scene art and visual delivery | Unverified | No scene assignment or game rendering verified by this review. |

The route remains unready for manual play and does not pass the strict review gate.
Preserve the repaired branches, correct the survey-station state and choice defects, align delivery with the actual engine schema, and finish the timing audit.
Then supply enough distinct nonsexual relationship content for the shorter committed paths to meet the meaningful minimum rather than making longer intimacy selections the only way to approach it.

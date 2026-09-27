# Areelu selected-choice repair handoff

Author repair only; this is not independent approval.
Reviewed input was `AE390C939E2488D554A551843C3D9EDFC98E34020A5D5B2009BFF66DBB5ABCA7`, with findings in `areelu-prose-independent-review.md`.
Repaired source SHA-256 is `EC26B251855F2CEFBBB6236AC43077E218CEA718632C044CCEA8E5D591F57D3C`.

## Branch changes

The private counterledger now has a private verification page and a private findings reply.
It does not visit the submission or public-reply pages.
The later public hearing identifies a separately acquired field ledger, explicitly preserving any private counterledger.
Professional-only contact bypasses the reply's romantic proposal.

Waiting before touch has its own reply page.
The private kiss now separates continued intimacy, a kiss-only evening, and immediate departure.
Departure leaves the room before any further intimate action.
The next invitation arrives by courier in a delayed followup instead of implying the Commander stayed overnight.

Declining dinner, ending the returned-name relationship, refusing further touch, and choosing a solitary walk now have distinct exits.
Their selected continuations do not reach dinner, desire reaffirmation, or face-touching pages.
Earlier yes-before-choice narration was also removed from the walk and dinner introductions.

Closing the personal relationship in the copy scene leads to its nonromantic ending.
A nonphysical evening or pause avoids the later handholding and kiss menus.
The second-contact page no longer takes the Commander's hand before the player selects contact.
The protected-memory history reaches a distinct inert-transcript conflict, without narrating a risky intervention or weakened recollection that the Commander refused.
Shared inspection and confrontation text no longer assumes prior consent to the risky memory test.

Unresolved gates retain evacuation and an intact working archive.
Ordinary closures preserve the archive and use a separate marker report.
Only the spent-anchor history reaches the archive-loss follow-through and sacrifice discussion.
The later partnership argument now poses a hypothetical tradeoff instead of asserting that every player spent the archive.
The final private-letter scene no longer touches the Commander after a breakup.
Explicit game/story-ending vocabulary was removed from the identified ending pages.

## Campaign timing

The source still authors fourteen main sequences, with 194 authored nodes.
Sixteen dated transitions now end their BookEvent and schedule a followup through existing `Requires`, `Forbids`, and `DelayHours` fields.
The resulting manuscript has 30 scene dictionaries and 210 nodes because shared endings are copied into their appropriate separate BookEvents with unique identifiers.
Copies do not count twice on a selected path.
Scene titles remain the existing in-world titles.

Month, winter, and year jumps were revised into weeks or specified days.
Followups enforce the corresponding 12-hour, two-day, three-day, six-day, or seven-day interval at the scene boundary.
The inspected runtime scheduler in `src/Story.cs` calculates delay from timestamps on required flags; queued followups use that existing mechanism.
Completion flags for the returned-name, copy, and gate sequences are no longer emitted before a selected followup chain finishes.
This prevents the next major sequence from starting merely because the first report was read.

The longest measured trajectory visits all 30 scenes.
Their authored delays sum to 3,216 hours, or 134 days, if taken sequentially at minimum delay with all producer timestamps populated.
That is a manuscript pacing consequence, not a measured in-game duration.
Integration must verify actual campaign availability and decide whether this wait budget fits Chapter 5.
No campaign clock is silently advanced by page narration, and no runtime integration is claimed.

## Verification

`py -m storylines.areelu_trickster_rivalry_opening` passes with 30 unintegrated scenes and 210 nodes.
`py -m py_compile storylines/areelu_trickster_rivalry_opening.py` passes.
`git diff --check -- storylines/areelu_trickster_rivalry_opening.py` passes.

The existing final-outcome test now follows actual scheduled scene boundaries while carrying choice flags.
It still reaches committed, open, paused, and closed futures and preserves closure after the late breakup even with historical commitment.
The added selected-choice tests follow specific answers into actual subsequent pages rather than inspecting topology alone.
They reject intimate escalation after the listed refusal choices, public submission of the private counterledger, contested-memory text on the protected history, and sacrificed-archive text on ordinary or unresolved gate histories.
They also verify positive followup delays, corresponding producer choices, and removal of the identified production language and year-scale jumps.

These checks model the authored dictionaries locally.
The route is unregistered, so no actual player-facing game reproduction or save/load test was possible in this task.

## Selected word counts

A separate local traversal imported the repaired scene dictionaries, carried flags between scenes, enforced scene and choice predicates, explored both check outcomes, and excluded abort, ended, paused, closed, and rivalry-only states.
It used the Unicode tokenizer from `tools/measure-story-content.py` and counted only visited prose plus the selected choice text.
The seed still assumes `entry_ready`, active Trickster, verified cradle record, and a non-declined native answer.
Those seeded states are not proof of attainable native acquisition.

| Completed modeled trajectory | Selected words |
| --- | ---: |
| Committed, sealed letters, ordinary future, private research pact and power partnership | 25,610 |
| Committed, protected memory, private counterledger, ordinary grounding, ordinary future | 23,083 |
| Committed, protected memory, private counterledger, unresolved gate, ordinary future | 23,122 |

These are compatible maxima under those filters, not guaranteed minima for every completed romance and not scores for meaningful prose.
The comparison establishes that the repaired alternate histories remain substantial without adding filler to restore the old raw count.
It does not settle the independent review's repetition and characterization concerns.

## Remaining work

Independent reviewers must inspect this source and its new branch pages before any approval.
The long middle still needs the separate planned characterization and narrative-economy revision.
The new ordinary and unresolved aftermaths need their own literary review alongside the preserved power bargain.
Player-delivered AU disclosure, initial contact and recovery acquisition, native readers, actor presence, registration, save/load behavior, ToyBox integration, scene art, and headless game integration remain outstanding.
The manuscript is not ready for manual in-game review or release.

# Konomi private career consequence and farewell handoff

## Candidate and ownership

This contribution addresses item 2 of [the assembled readiness review](../story-review/konomi-assembled-readiness-20260926.md).
It adds three connected Chapter 5 visits and two alternative earned epilogues after the private career and relationship decisions.
It does not claim complete route approval or a comparative RanRomance review.

Owned files are `storylines/konomi_private_consequence.py`, `tests/KonomiPrivateConsequenceTests.cs`, and this handoff.
No shared engine, export, existing storyline source, art or installed game file was edited.

Source SHA256: `7A7B4804047E32B3F6F8206EC5D20F44DD4E18CAD4014FAB807186634C1FAAAF`.
Test SHA256: `CB69F9968421E7DF6CA6D774EE30456242CC9B6297F837BA90EDE461C7415B83`.
These hashes identify the first review candidate; later review-driven revisions must replace them before promotion.

## What is played

| Visit | Earned entry | Event and consequences |
| --- | --- | --- |
| `konomi.private_return_terms` | Existing private future, career decision and intimate evening | Konomi arranges an ordinary return after her departure; the first tenant exercises the option she negotiated, preventing a larger applicant from taking those rooms; she proposes exclusive seasonal representation or a smaller guarantee with freedom to represent other landlords. |
| `konomi.private_kept_hours` | `konomi.private_terms_sent` | The owner accepts the selected terms; a refused applicant and the employer's response make the choice concrete; the Commander chooses whether paid recommendations may shorten the promised visit or whether Konomi declines that extra fee and keeps the whole afternoon. |
| `konomi.private_last_visit` | `konomi.private_hours_kept` | Explicitly chosen pre-battle farewell; the tenant's payment and the career agreement are settled, selected work/time outcomes are recalled, and the pair retain their actual open or committed relationship before choosing a night together or a quiet evening. |

The exclusive option gives Konomi security and control over which proposals reach the owner's table while costing her other clients' trust and business.
The narrower option gives her freedom to place proposals elsewhere, with a lower guarantee and the work of selling each independent service.
Neither option reforms her into an unambitious helper, grants an unimplemented native resource, or requires the Commander to praise every professional choice.
The first tenant's option remains honored on both paths; no overlapping lease, payment or actual crusade resource is created in the engine.
The smaller applicant, owner, tenant, adviser, clerk, correspondence and fee receipts are authored fiction in the book scenes, not newly placed native actors or native quest outcomes.

Accepting the earlier job immediately recalls the tenant's distrust and independently obtained adviser.
Waiting recalls the reduced starting fee, adviser preparation and introductions made during the delay.
The new seasonal choice is a later negotiation, not a replacement of either earlier answer.

The time decision does not rank affection by money sacrificed.
Both the shortened visit and the full afternoon receive played physical or conversational closeness and their own farewell callback.
No roll is added to a question of mutually negotiated time or career preference; the route's existing investigative checks remain available in their own events.

## Exact eligibility and late installs

All three visits require `konomi.dismissed`, `konomi.office_completed`, `konomi.private_returned`, `konomi.private_evening_kept`, `konomi.career_decided`, and `konomi.private_future`.
All are Remote scenes in Drezen area `2570015799edf594daf2f076f2f975d8`, explicitly Chapter 5 only.
They forbid `konomi.present`, `inhuman`, `konomi.closed`, `konomi.private_parted`, `konomi.farewell`, and `konomi.private_last_visit`.
The first visit has a 168-hour delay; the second has 48 hours; the farewell has 24 hours.
The first and farewell are ManualOnly.
The intervening consequence is optional and uses the ordinary remote offer behavior after its earned prerequisite.

Fresh dismissed courtship and established lovers dismissed later both qualify after actually playing their respective private predecessors.
The newer absence acknowledgement is optional and is not invented or required by these scenes.
A current Legend who acquired the private contact while Trickster retains access; no new Trickster power, native office or mythic flag is granted.
The scene never retrospectively claims that a late dismissal happened before the Abyss.

Committed and explicitly open private futures both qualify.
Open courtship remains open at the farewell and in its epilogue; no exclusive household or committed future is assigned automatically.
Existing other romances remain untouched.

The initial visit explicitly describes a written invitation, confirmation and ordinary travel before the meeting.
That is authored delivery consistent with the existing unitless private route, not proof that a native Konomi actor has been spawned or found in Drezen.
The farewell is initiated by the player when ready for final fighting; no actual final-battle quest predicate was invented.
It does not advance the campaign, close a map or prohibit other relationships' farewells.
Native live-state changes during an already open unitless book remain a separate engine/runtime verification issue.

## Ending integration contract

Root should append `SCENES` to the assembled payload and call `integrate(payload)` after the existing private future module is present.
The overlay appends `konomi.private_consequence_complete` to `Forbids` on exactly `konomi.ending_distance` and `konomi.ending_distance_open`.
It is idempotent.
All existing scene/node IDs, answer indices, text, requirements and other fields remain unchanged.
No scene or answer is removed.

The original distance ending remains the shorter course for an older save, a player declining the new visits, a partially played extension, or a player skipping the new farewell.
It is not credited as having played the new career or time consequences.
Completing the final new night or quiet goodbye sets `konomi.private_consequence_complete` and permits exactly the matching new ending: `konomi.ending_distance_lived` for committed or `konomi.ending_distance_open_lived` for uncommitted private future.
Both new endings exclude closed, inhuman and ascended histories.
Existing transformed/ascended alternatives remain unchanged.
The new endings recall the career actually chosen; they do not promise another unresolved campaign quest.

A recorded old ending flag or timestamp is not deleted on late-install opt-in.
The tests explicitly retain both while playing the first new visit.
The new scenes do not require or retroactively grant `konomi.committed`, change any earlier choice, or close an outstanding hearing by fiat.
An established dismissed test history plays its private hearing before the old future choice, preserving that module's existing chronology.

## Length and selected-path evidence

The candidate contains five scenes and 41 pages including both epilogues.
Using the existing project tokenizer, it contains 5,319 raw words and 5,083 distinct text-segment words.
The three visits alone contain 4,837 raw and 4,795 distinct words.
Repeated shared epilogue material and repeated answer labels are deduplicated rather than credited twice.

| Earlier career and relationship history | Selected new words, three visits plus one ending | Compatible paths enumerated |
| --- | ---: | ---: |
| Accepted immediately, open | 3,075-3,152 | 32 |
| Accepted immediately, committed | 3,085-3,162 | 32 |
| Delayed start, open | 3,077-3,154 | 32 |
| Delayed start, committed | 3,087-3,164 | 32 |

These walks count visited prose and selected answers while carrying flags between visits.
They do not add both earlier career replies, both seasonal arrangements, both uses of the afternoon, both intimacy endings, or both relationship epilogues.
They exclude the already-authored private route that earns entry.
Aggregate volume remains a planning measure, not proof of original-game likeness or RanRomance quality/depth parity.

## Verification

Isolated runner: `C:/Users/Z/AppData/Local/Temp/konomi-private-consequence-check-x2ln_7o5/Check.csproj`.
Its adjacent Story.json was assembled in memory from `expansion.make_expansion()` with this candidate appended and its overlay applied.
The runner uses actual shared `Rules.Validate` and the current `Program.Walk` helper.
Result: **98,074 focused assertions passed**.

The suite earns ordinary history before dismissal for established lovers and earns actual Trickster private acquisition for both established and fresh histories.
It plays history repair when needed, carriers, the pre-road evening, departure, optional Chapter 4 absence, letters, reunion, private hearing for the established fixture, both career choices, the intimate evening and both private futures.
It then walks every new page and every compatible new decision through exactly the appropriate ending.
Current Legend, other existing commitments, skipped absence, late-install records, native/history blockers, wrong chapter/area, waiting, aborted entry and replay are covered.
No new branch effects or timestamps persist on an intermediate page; terminal completion alone records each new visit's decisions.

An independent in-memory structural comparison confirms that the overlay changes only the two specified ending forbid lists and that applying it twice makes no further change.
The original scene count/order prefix, answer arrays and all other old fields compare equal.

Independent literary/canon review, combined export/schema/binding checks and managed integration remain required before promotion.
Loaded saves, native presentation, portraits, TTS pacing and actual ToyBox coexistence were not exercised by this contribution's source tests.
No author score or full-route approval is supplied.

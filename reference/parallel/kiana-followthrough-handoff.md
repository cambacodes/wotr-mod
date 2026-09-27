# Kiana follow-through author handoff

Source: `storylines/kiana_followthrough.py`.
Frozen SHA256: `6241DAAAC4447F443180E2B9A343A35477A511454AD18930A95DE22F80DC85BF`.
Ownership of the source and this handoff is released to the parent.
No shared source, export, tests, native state, installation or art was changed.
Independent review is required before export.

## Contribution and remaining scope

Six new scenes develop Meral's invitation, Kiana's writing, her first organized reading of the new material, the resulting revisions, a rented workspace and the couple's time together.
There are 78 nodes and 108 choices.
The project inventory tokenizer reports 8,302 raw words, comprising 7,412 prose words and 890 choice words.
Whole-segment deduplication reports 8,296 words.
A complete selected path through this contribution contains 5,135 to 5,475 words.
The aggregate exceeds the initial 5,000 to 7,000-word estimate because marital histories, staging, script decisions and work arrangements have distinct played follow-ups.
Those figures are not semantic originality scores, quality approval or whole-route playthrough totals.

Kiana remains incomplete against the 21,000 meaningful-word floor and full RanRomance-depth requirement.
No author-awarded quality score or guaranteed reviewer score is claimed.
This contribution also does not supply her missing bespoke Trickster access, native actor restoration or complete ending integration.

## Sources and canon treatment

Read `EXPANSION.md`, `storylines/kiana.py`, `storylines/kiana_consequences.py`, their handoff and prior independent reviews.
Native reference reading included `reference/canon-review/kiana.txt`, `reference/story-review/Kiana.txt`, `reference/canon-review/kiana-authoring-predicates.json` and `reference/canon-review/kiana-appearance.md`.
The appearance adjudication identifies native unit `180b0eaa5dce387458d2ebf0ee943985` as an oread with the supported blue skin, pale crystalline head silhouette and blue-green eyes.
The new prose retains that identity and does not treat the vampire costume as actual undeath.

Native married aftermath `a819e8c85ef23324bb0d8117bb9d7df3` supports Kiana's affectionate marriage, and `df45181e1968f26459f9e8bc2b995a34` supports her frank adult humor.
Widow aftermath `aebbc1845e827dd4da4e28014e7b4162` establishes a distinct loss rather than an unhappy marriage.
Those are underlying canon facts.
Separation, the Commander romance, this writing practice and the civilian social circle are authored alternate developments.
The native game does not establish a professional playwright career for Kiana.
This module gives her a small experiment in paid room hire and readings, not immediate fame or self-supporting success.

Meral, Lenna and Edris continue the already authored social introduction.
Meral's work copying accounts is new authored backstory, not an asserted native profession.
The baker and unnamed adult listeners are also authored people represented in narration.
No physical units are spawned or moved.
Elan does not appear as a new physical actor.
On separation histories, Kiana expressly arranges a separate afternoon with Meral and does not know whether Elan answered his invitation.
Neither his absence from that afternoon nor his friends' welcome is represented as his approval of her romance.
The widow branch recalls the table incident already introduced in the preceding contribution.

## Scene progression

All six scenes use relationship `kiana`, existing portrait key `Kiana`, chapter 5, and Drezen area `2570015799edf594daf2f076f2f975d8`.
They require `seelah.souls_returned`, `kiana.lovers`, `kiana.consequences_ready` and the predecessor listed below.
They forbid `kiana.closed`, `kiana.farewell` and `inhuman`.
They are optional remote book events.
Only initial deferral choices abort, before any new flags are set.
Continuous visits, performance and its aftermath remain inside their respective books.

| Scene | Predecessor | Delay | Completion milestone |
| --- | --- | ---: | --- |
| `kiana.bakery_stairs` | `kiana.consequences_ready` | 48 hours | `kiana.bakery_visit_kept` |
| `kiana.last_page` | `kiana.bakery_visit_kept` | 48 hours | `kiana.last_page_kept` |
| `kiana.first_readers` | `kiana.last_page_kept` | 72 hours | `kiana.readers_kept` |
| `kiana.ink_after` | `kiana.readers_kept` | 48 hours | `kiana.ink_evening_kept` |
| `kiana.working_room` | `kiana.ink_evening_kept` | 48 hours | `kiana.workroom_taken` |
| `kiana.kept_evening` | `kiana.workroom_taken` | 168 hours | `kiana.followthrough_kept` |

The first helper call repeats `kiana.consequences_ready` in its required list because the common prerequisite and first predecessor are identical.
This is semantically redundant and may be deduplicated by the parent if preferred.
No additional state is implied by the duplicate.
The week before the final evening allows the two scheduled working afternoons to occur.

## Meaningful branches

The existing `kiana.waited`, `kiana.affair`, `kiana.separated`, `kiana.bereaved` and native `seelah.elan_dead` histories select the appropriate discussion of Meral's invitation.
The affair branch owns the earlier kiss and rejects an invented account in which Elan drove Kiana away.
The waited branch acknowledges that respecting the earlier pause did not remove everybody's pain.
Widow text requires the actual death alias as well as the authored bereavement history.
Existing commitment and uncertainty remain unchanged.
A committed Kiana asks where their agreed evening belongs among her new arrangements.
An uncommitted Kiana arranges a particular evening without presenting it as a postwar promise.

| New choice pair | Played consequence |
| --- | --- |
| `follow_audience` / `follow_workshop` | Fourteen listeners in a hired room with modest contributions, or six readers in Meral's room with comments and pastry expenses. |
| `follow_long_speech` / `follow_short_speech` | The long version loses momentum at its third pause and is cut afterward; the short version works but leaves Kiana wanting to restore one comic sentence. |
| `follow_guest_role` / `follow_listens` | The Commander reads the guest or listens while Edris reads that role. |
| `follow_heard_readers` / `follow_asked_readers` | Kiana hears an unsolicited interpretation or identifies the particular line that prompted the response. |
| `follow_quiet_desk` / `follow_shared_room` | She rents quiet working hours and copies slowly herself, or pays Meral for copies and works amid useful but disruptive company. |
| `follow_ink_kiss` / `follow_ink_walk` | A graphic and explicit private evening or an actual market walk for cakes. |
| `follow_waited_page` / `follow_stopped_page` | The Commander fetches supper while she finishes the page, or Kiana puts it aside and serves the food she has ready. |
| `follow_market_morning` / `follow_music_wish` | Different explicit future discovery wishes, not falsely completed outings. |
| `follow_last_kiss` / `follow_last_quiet` | An extended kiss or quiet company before the evening ends. |

All table flags use the `kiana.` prefix.
The existing `moon` and `guest` opening choices have separate script callbacks.
Optional `quiet_entrance` and `comic_entrance` histories change the performed entrance, with an ordinary fallback when stagecraft was skipped.
No performer role is silently transferred to Kiana after the Commander selects the guest.
The selected brass pin is described generically, so this module does not contradict the preceding leaf or round choice.
The workplace payment and copy fee use Kiana's narrated funds and do not deduct player gold or alter crusade resources.
Kiana's outside friendships and work survive the romance scenes rather than existing only to praise it.

## Gameplay and trigger work for the parent

The current module uses the existing remote-rest delivery mechanism.
It does not yet provide original-style exploration triggers, player skill rolls, quest objectives or discoverable world objects.
Dialogue alternatives above are choices, not dice checks.
No skill DC, success etude, roll result or native trigger is invented in this authoring module.
No check should purchase attraction or substitute for Kiana's decision to invite the Commander.

Concrete integration opportunities follow.
They are proposals requiring engine and blueprint work, not implemented features.

| Moment | Discovery or check opportunity | Success and failure consequences to preserve |
| --- | --- | --- |
| Meral invitation | Make Edris's existing roof-supper introduction lead to a discoverable invitation or journal prompt after `kiana.consequences_ready`. | A player who follows up finds the visit; a delayed answer postpones it without inventing Elan's consent or closing the romance. |
| Reading venue | Let the player inspect an appropriate verified Drezen location after Kiana chooses the audience size. | Venue discovery supports the selected plan; a non-exploration letter or introduction remains available for players who prefer it. |
| Guest's first line | A suitable Persuasion check could concern projecting and recovering a spoken line before the audience. | Success keeps the opening smooth; failure retains the currently authored lost line and Kiana's practical recovery. Both continue the scene and neither awards affection. |
| Chair inspection | A Perception check could find the short chair leg before Kiana begins writing. | Success lets the player steady it promptly; failure costs setup time and requires a borrowed chair or help from the baker. The desk choice remains viable. |
| Copy and script continuity | Knowledge (World), if the native implementation supports this use, could identify the cook's contradictory exit while reading a copy. | Success catches it before rehearsal; failure retains Lenna's later discovery. Both permit revision, and neither makes Kiana helpless without the Commander. |
| Market or music wish | A subsequent exploration scene can fulfill `follow_market_morning` or `follow_music_wish`. | The current final scene explicitly records only an intention. Do not turn either into an offscreen completed date merely by setting its flag. |

The audience reaction to the long or short speech should remain tied to the player's literary choice, even if a performance check is added.
A successful delivery must not erase the written consequence of an overlong passage.
The quiet workspace and shared room must remain attainable through their present ordinary means if optional checks fail.
Native skill checks need actual engine support and separate verification.
The author has not added fake authored flags to simulate a successful roll.

## Parent corrections and independent review

The parent corrected `last_page/end` to gather retained work without assuming the staircase sentence was cut on both branches.
The parent corrected `ink_after/long` to acknowledge the speech as a shared experiment instead of claiming the Commander had opposed it.
Corrected module SHA256 is `C0EFDA58BBB848C758E46B1E17D175733C9E701EF89A486DE59C1B9D9077DC5C`.
Independent rereview in `reference/story-review/kiana-followthrough-review.md` scored this contribution 91 for writing and 92 for native characterization/canon, with no remaining identified contribution-level prose blocker.
The older farewell now discusses the next draft, and the existing together/bereaved endings distinguish future staged productions from earlier readings.
The apart ending no longer denies that earlier material may have been performed.
These changes preserve scene and choice identities and were included in the review of played and skipped follow-through histories.
Full-route, gameplay, art and runtime approval remain outstanding.
The module is still unexported while focused chain tests and shared integration are completed.

## Original shared integration findings

Do not export this module without addressing the older farewell and ending statements.
`kiana.farewell.plans` currently speaks as though finishing the play and asking friends to read it are still entirely future work.
After `kiana.readers_kept`, it should refer to further revision, a new section or a later staging instead of inventing a first reading still to come.
`kiana.ending_apart` says she never performed the earlier version, which conflicts with the new reading if the romance closes afterward.
The existing together and bereaved endings also describe a first performance or first rehearsal without acknowledging these new scenes.
A distinction between a public reading and a full staged production can be useful, but the current wording does not establish that distinction sufficiently to assume it resolves every contradiction.
The parent owns all existing source and must make and review the chosen ending updates.

The farewell can currently be reached without this optional arc, so this module alone does not ensure full-route attainable depth.
Its new milestones need deliberate integration into the full campaign and outcome review.
The final workroom, developing work and discovery wishes need later payoffs; they are not automatically inserted into old epilogues.
Unimplemented Aranka contact is not used.
Arsinoe is not called in as an assumed world actor.

## Author verification

A direct Python traversal imported the real new module with bytecode writing disabled.
It used 36 starting combinations: waited, affair or widow history; committed or uncertain; moon or guest opening; and absent, quiet or comic optional entrance.
The traversal followed every eligible authored choice through the actual six-scene chain.
It reached every new node and choice, rejected missing targets, cycles and empty eligible-choice lists, and checked balanced narration markers.
It produced 36,864 completed paths and 10,188 initial deferral traversals.
All nine new choice pairs remained exclusive on completed paths.
Native marital history, existing commitment or uncertainty, and unrelated Seelah and Arueshalae commitment markers were preserved.
No scene ID collided with the existing Kiana or consequences modules.
No abort wrote new progress.

A subsequent prose-only correction made the copy payment explicit.
The final imported source was remeasured across all 36,864 completed paths, producing the final word counts above.
That edit did not change any node, choice, condition or effect.
No shared C# rules suite, managed construction, native binding verifier, real save or Unity test was run by this author.
The direct walk does not model rest queues, native state changing during an event, actual skill checks, portrait delivery or ToyBox runtime behavior.

## Review and release status

Independent writing, canon, art and integration reviewers must assess the actual frozen content, targeting above 90 in each required discipline without a promised result.
No artwork is supplied by this module.
The restrained intimacy is adult, voluntary and graphic and explicit; other relationships are neither reset nor checked for exclusivity.
Neither ToyBox setting is read or changed.
That limited implementation fact is not a runtime compatibility certification.
Full-route amount, meaningful attainable depth, endpoint coherence, native access, Trickster recovery, additional discovery gameplay and game/save verification remain unfinished.

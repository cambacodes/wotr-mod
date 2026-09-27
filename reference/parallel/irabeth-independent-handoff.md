# Irabeth independent campaign handoff

This candidate is written for independent review and root integration, not installed in the game.
The author assigns no review score and does not certify RanRomance parity from a word count.

## Owned release

- `storylines/irabeth_independent.py`: SHA256 `C258F45ADC334A8C66807BC8BC27E4B634E1397D5CDE68F95E80D23E0D6A0346`.
- `tests/IrabethIndependentTests.cs`: SHA256 `35C57B26AD3A51122573691769E6910A55AB73F0FCFDB62F64042916ABD6F9F9`.
- This handoff is the only additional owned file.

No existing story, shared builder, native data, export, portrait or installed file was changed.
The parent owns the independent relationship bridge and registration.

## Content and measurement

The module contains 28 scenes: 19 visit books including alternative acquisition histories and the optional Chapter 3 farewell/Chapter 4 letter, plus nine ending books.
There are 190 pages and 274 choices after the acquisition-date terminal alternatives are constructed.
Markup-stripped page prose totals 23,471 words, with no identical page text counted twice.
This counts authored alternatives across attainable histories, not words one player necessarily reads.
Choice labels are excluded from that prose measurement.
The source meets the 21,000-word aggregate planning floor by itself; quality, campaign completeness and comparative RanRomance depth still require review.

An independent Python graph traversal measured a new negotiated courtship with ordinary native morale, living Anevia, no other Anevia romance and an ordinary ending.
It filters actual choice predicates, follows success and failure targets, preserves relevant branch flags and excludes aborts or local closure.
It includes each selected scene's prose once, including its ordinary ending, and excludes choice labels.

| Selected history | Played visits | Prose range |
| --- | ---: | ---: |
| Chapter 3 acquisition, played departure and unposted Chapter 4 letter, Chapter 5 finale | 15 | 12,393-13,777 |
| Chapter 3 acquisition without the optional departure/letter | 13 | 11,549-12,759 |
| Chapter 5 acquisition and finale | 13 | 11,579-12,789 |

The final scar sentence is outside these ordinary, unobserved-scar measurement fixtures and does not change their totals.
Other native states, legacy acquisitions and special endings produce different selected lengths.
There is no invented 21,000-word selected-playthrough requirement.

## Campaign and decisions

Irabeth chooses to perform a comic caravan-guard recitation because she wants the audience's pleasure and recognition.
The Commander can help shape the guard or duke, attend the actual performance and choose the private celebration.
This develops her native desire for distinction without replacing her identity with an interchangeable wounded subordinate.

Her professional case concerns sound cold iron detained on evidence from a protected watch source.
Brena paid for the goods; Hadran had grounds to investigate but mishandled her account and prolonged detention.
The Commander can make a Knowledge: World DC25 check, fail into a slower assay, or choose that assay without rolling.
Failure costs a lost afternoon and delayed customer work within the authored event, rather than an unimplemented permanent stat penalty.
The successful material examination still does not prove ownership.

The later decision either protects the intelligence source while returning goods and compensating Brena from the watch purse, or opens the relevant original account after moving endangered witnesses.
Irabeth prefers protecting the source and paying the watch's own cost.
She can defend that uncomfortable interest without requiring the Commander to teach her an approved moral lesson.
The chosen consequences recur in training equipment, Ordel's employment and the false-iron inquiry.
A later hearing shows another officer using the new instruction, exposes a flaw in the form and resolves the original case's remaining updates.
These are authored civilian and professional events; the module does not spawn native NPCs, issue an actual crusade decree or alter kingdom statistics.

A private evening offers kissing, graphic and explicit intimacy, holding or company without touch.
The final travel outing uses Sella's road drawings and a played city exercise.
Its measured and shortcut outcomes differ, and the shared callbacks no longer invent a locked-gate encounter on the measured path.
The future choice is lasting commitment, an open continuing relationship or friendship after courtship.
The pre-battle farewell acknowledges the actual choice, native spouse loss or absence, and the intimacy tempo selected that evening.

## Acquisition and history contracts

New negotiated acquisition progresses through `a_name_on_the_list`, `the_question_outside_duty`, Anevia's separate `anevias_answer`, and Irabeth's `the_evening_she_chose`.
The proposal sets `irabeth.courtship_requested` and `irabeth.spousal_conversation_requested`.
The separate wife interview sets only `irabeth.spouse_heard`.
Irabeth's own subsequent acceptance sets `irabeth.marital_terms_agreed`, `irabeth.lover` and `irabeth.personal_ready`.
No new negotiated path sets an old affair, reckoning, shared table or triad commitment flag.

`one_truth_to_tell` requires actual `i_affair`, `i_morning` and `i_will_tell`, and excludes `a_affair`, `trying` and `committed`.
It acknowledges the existing affair and asks for an agreement beginning now rather than laundering the earlier concealment.
Unresolved dual affairs remain with the original shared reckoning.

`a_day_of_our_own` requires actual `i_self`, `i_seen`, `ordinary` and active `trying` or `committed`.
It remembers an established relationship and does not replay first attraction.
It requires a living, not-gone Anevia and does not serve a dissolved group.

`after_the_shared_answer` requires `tirabade.group_closed`, the root bridge's explicit `tirabade.irabeth_continuation_invited`, and evidence of the prior affair or shared commitment.
The root confirmed that the played bridge invitation includes Anevia's willingness for her marriage to include Irabeth's individual continuation.
Irabeth still chooses her own terms in this new visit before it grants a lover or marital-agreement flag.
Its wording covers either refusing the proposed triad or ending an existing shared arrangement.

Native widowhood can be acknowledged at the proposal.
`after_the_answer_was_lost` also handles death during a pending proposal or after an actual old affair, without inventing the deceased wife's consent.
Neither path sets marital terms agreed on Anevia's behalf.
An absent/gone wife does not provide permission for a fresh courtship.
Already negotiated individual relationships remain playable after spouse death or absence while Irabeth herself is available.

The Anevia interview distinguishes no romance, an active individual romance, and a preserved lover flag whose relationship is now closed.
It never treats willingness about her marriage as consent to become the Commander's lover.
Other lovers are neither disabled nor rewritten.

## Chronology and native evidence

The implementation reads `reference/canon-dialogue.txt`, the shared route's individual acquisitions and later individual scenes, the independent-relationships plan, and the capital-contact audit.
Native anchors include Irabeth's Lastwall rejection, her parents and farm, mercenary years, Tymon rescue, rebuilding the Eagle Watch, native affection for Anevia, desire for distinction and cold-iron/adamantine equipment concerns.
The lieutenant, smith, source, hearing, performance and route-maker in this contribution are new authored developments, not claims about installed NPCs.

Native capital identities are inherited from `reference/canon-review/tirabade-capital-contact-audit.md`.
Irabeth contact is `280d4712dceb37f4a88e98f1f4c6e64f`, answer list `871af36f2ab2b1f40b5de77976c54276`.
Anevia contact is `b5e867e13503c6f41bb1316705efb4a2`, answer list `33960c7f7af40cd43b7f801a76c87a0b`.
Physical entry uses Drezen area `2570015799edf594daf2f076f2f975d8` and Chapter 3/5 or Chapter 5-only gates as appropriate.
Each interview has one actual wife contact; no paired actor is claimed by these individual visits.

`integrate(payload)` adds four read-only aliases from installed `blueprints.zip` records inspected directly.

| Alias | Native record |
| --- | --- |
| `irabeth.chapter_three` | `World/Etudes/Common/WrathOfTheRighteous/Chapter03.jbp`, `15e0048c7daf0ac4999c2313b58df0e3` |
| `irabeth.chapter_five` | `World/Etudes/Common/WrathOfTheRighteous/Chapter05.jbp`, `5b01aa690202e584888dfc600a4aac0a` |
| `irabeth.scar_known` | Seen Irabeth `Cue_0071`, `c7a7717c516039d498a7525baf6abe04`, or Anevia `Cue_0045`, `8e808b69a43ed4f43b8eb39d27990a4a` |
| `irabeth.queen_loss_known` | Seen Irabeth `Cue_0197`, `d47bcd8d88f8ea149a596ca927e1153f` |

Terminal acquisition choices record `irabeth.began_chapter_three` or `irabeth.began_chapter_five` from the active native chapter, with Chapter 5 precedence if both aliases are present.
An optional farewell is proof only of that farewell, not the beginning of the relationship.
Early lovers without a farewell, new Chapter 5 lovers, older affairs/shared relationships and an early proposal completed in Chapter 5 receive truthful later wording.
The Chapter 4 letter requires the actually played Chapter 3 farewell and is explicitly unposted.

The scar cue union does not imply the player personally heard Irabeth's own request: the repaired callback states her boundary now.
The Queen callback remembers her observed report, rather than inferring a report solely from romance progression.
`broken` and `encouraged` are read from existing native bindings and never cleared, completed or written.

## Endings and remaining access work

Ordinary endings distinguish lasting, open, friendship and unfinished histories.
The unfinished ending preserves commitments already spoken before an unplayed farewell.
Special ordinary-epilogue precedence is own death/gone, incompatible transformation, ascension, sacrifice, then ordinary relationship outcome.
Those outcomes require an earned lover, not a fully completed campaign, so a mid-route loss does not erase the existing relationship.
The Aeon rewrite book belongs to the separate native Aeon epilogue owner.

Individual endings suppress active legacy `trying`/`committed` unless the authored `tirabade.group_closed` override is present.
They never override global `closed` or `irabeth.closed`.
Root must assemble the actual bridge alongside this module so that its override marker has a real authored producer.

This is a living-contact campaign with loss endings, not a delivered resurrection or a fabricated Trickster actor restoration.
Unavailable native Irabeth and mythic transformations remain guarded.
Universal Trickster recovery, exceptional missing-wife resolution, native actor loading, installed book display and real saved-game continuation remain separate verification or development work.

## Focused verification and integration

The isolated runner uses actual `src/Story.cs`, the actual `Program.Copy`/`Program.Walk` helpers and `Rules.Validate`.
The final graph/test revision passed 543,429 assertions.
The final source revision after that pass changes only the scar sentence, preserving nodes, choices and gates.
The independent reviewer subsequently reran the final candidate and reported 543,807 assertions passed in their isolated harness.
The focused test walks fresh Chapter 3/5, actual original single-affair and triad predecessors, bridge-invitation contract fixtures, widowhood, death during proposal, C3 proposal completed C5, absent actor interruption, late native states, check success/failure/non-roll, professional branches, all future choices, replay and ending arbitration.
Every new page is reached by the suite.
The bridge split marker is explicitly labeled a contract fixture in the author suite; root must verify its actual producer through the assembled bridge.

Runner project: `C:/Users/Z/AppData/Local/Temp/irabeth-independent-6mrmy2ls/Check.csproj`.
Candidate: the same directory's `candidate.json`.
Command: `C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe run --project C:/Users/Z/AppData/Local/Temp/irabeth-independent-6mrmy2ls/Check.csproj -- C:/Users/Z/AppData/Local/Temp/irabeth-independent-6mrmy2ls/candidate.json`.
The candidate adds this module and the root bridge's actual `after_local_parting` book as the override producer, without applying the root's old-scene overlay.

Root integration should register `RELATIONSHIP` under `irabeth`, deep-copy `SCENES`, invoke `integrate(payload)`, apply the bridge in its intended order and register `IrabethIndependentTests.Run`.
Run the retained shared tests, both individual suites and actual bridge paths together before accepting the assembled route.
Independent literary/canon review owns its judgment and scores.
Art remains a recognizable adult half-orc direction with the existing portrait keys; no new image or art approval is supplied here.

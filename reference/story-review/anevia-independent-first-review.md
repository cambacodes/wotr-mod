# Anevia independent campaign: first independent review

Decision: revisions required.
The manuscript contains a substantial romance and a playable investigation, but it does not yet pass the requested greater-than-90 standard in every discipline.
The principal problems are incorrect history joins, incomplete provisional endings, and a repeated explanatory voice that weakens Anevia's distinctive characterization.
Adding more words would not resolve these problems.

## Reviewed revision and independence

- Source: `storylines/anevia_independent.py`, SHA256 `23A3E38B03621C25A9CDF762E695B2005651D7507D47FD87E7B6AF0F1D2BB7B0`.
- Tests: `tests/AneviaIndependentTests.cs`, released SHA256 `4DA6EC71C3DB94AD60D0E761F61DA63BA0B0107039540729EC9FE090F0AB5D43`.
- Executed candidate: author candidate `3A4C84C24110C4EDA9552623BDE1E8BBC1C385FC97BA19421F45135E1F1E03B4` in `C:/Users/Z/AppData/Local/Temp/anevia-independent-z5an3x98/candidate.json`.

I read the entire source, including every acquisition alternative, investigation outcome, private evening, absence and return, commitment, grief visit and all eleven endings.
I read the author handoff and actual installed native common-dialogue text by resolving blueprint Text keys against the installed English localization.
I did not author this campaign and made no changes to its source or tests.
My earlier work on shared contact review does not make me an author of this manuscript.

The test candidate contains a labeled declaration fixture for proposed bridge flags.
That fixture establishes neither played acquisition of those flags nor tested shared-bridge integration.
The parent Anevia dispatcher and reusable native answer list must remain intact when the new module is integrated.
The handoff identifies the installed parent dispatchers; this review does not independently certify live load order or parent answer-list mutation.

## Actual strengths

The civilian investigation has a clear object and consequences: false inspection notices collect information about vulnerable residents, and confronting the sellers forces a choice between recovering receipts and stopping the departing buyer.
Perception success, failure, sorting and asking do not simply award the same clue with a different line of praise.
Dema can decline the dangerous delivery, and the later repayment problem remembers whether the papers survived.
These are meaningful player actions, even though their world effects currently exist in authored book-event prose rather than inventory or native quest changes.

The goat game, the difficulty undoing a buckle while laughing, and Anevia's quick practical jokes create convincing adult attraction.
Intimacy is graphic and explicit, voluntary and compatible with choosing quiet company or keeping another appointment.
The route permits a local refusal without closing Irabeth's romance or every other partner.
The negotiated opening, actual single-affair disclosure and established-triad date make materially different claims about how the relationship began.
They do not simply erase the old affair flags.

## Mandatory history and ending repairs

### 1. Optional farewell is incorrectly used as an acquisition date

`the_life_she_lived/start`, choice index 1, offers “We began this after my return” whenever `anevia.departed_together` is absent.
`new_days` then says they were still deciding whether to ask one another out during the separation.
However, an earned Chapter 3 romance can complete the investigation and ordinary evening while skipping the optional `departure_note`.
The new claim is false for that perfectly attainable history.
Use a supported acquisition-history distinction or make this no-letter branch truthful for both histories.
Do not make an optional farewell retroactively mandatory merely to conceal the missing distinction.

### 2. Provisional ending contradicts a completed commitment

`ending_unfinished` requires only `anevia.lover` and the absence of `anevia.developed`.
A player can complete `a_key_that_is_hers`, explicitly choose a lasting relationship, receive `anevia.committed` and `anevia.future_chosen`, and stop before the final farewell.
The available ending nevertheless says the lasting shape was not settled and refers to a household “they had never chosen.”
Provide a truthful provisional account of the actually chosen future, or revise the common fallback so it does not deny completed choices.
The ending need not award unplayed farewell details.

### 3. Native bereavement can remove every individual ending

After an earned romance, `irabeth_dead` suppresses the ordinary living endings.
`ending_survivor` requires the optional grief visit's `anevia.survivor_continues`.
If that visit has not been played, there is no ordinary individual Anevia ending, even for an already committed lover.
Supply a provisional grief outcome which acknowledges the established relationship without assuming she has chosen to continue it after the loss.
Also audit the corresponding `irabeth_gone` state: its suppression of ordinary endings must have a deliberate truthful outcome or an explicitly documented native impossibility, rather than silently dropping earned history.

### 4. Current Irabeth romance becomes an “ordinary acquaintance”

`beths_question` correctly distinguishes an active `irabeth.lover` from past and absent romance.
The shared `beths_answer/finish` narration then says the Commander accepts an offer of “ordinary acquaintance” without romantic meaning Irabeth has not given.
That narration does not fit the supported current-lover history.
Make the shared invitation concern the actual offered conversation, without reclassifying the relationship.

### 5. Ascension remembers an optional game as a fact

`ending_ascended` requires only `anevia.lover`, but recalls arguing over the little game.
Acquisition can finish and ascension can occur without `the_evening_without_a_case`.
Use a universally earned memory or condition this particular callback.
Do not suppress the entire ascension ending just because the game was skipped.

## Mandatory branch and physical continuity repairs

These are small repairs, but each appears on an offered path and should be resolved before rereview.
Preserve existing IDs and answer indices where possible.

| Scene/node | Offered path and contradiction | Required result |
| --- | --- | --- |
| `unborrowed_hour/quiet` | “Share the last pear” leads through `watching` to `wait` or `friend`, which still produce a remaining pear. | Consumption and the later basket contents agree. |
| `her_own_answer/start -> want` | Direct romantic answer skips the two branches that move the box from table to sill; `want` and `stop` place it on the sill already. | The shared node moves it or uses branch-safe staging. |
| `the_paper_seller/start`, choice 1 -> `method` | Skips `customer`, the only introduction of the wet cuffs and blue dye, but the shared reasoning and later questioning already know these clues. | Every route learns the evidence before using it. |
| `the_counting_room/start`, choice 0 -> `account` | The basket starts at Cale's feet; only optional `basket` lifts it; the shared continuation refers to the basket leaving the desk. | Establish the movement on both paths or retain its actual location. |
| `what_the_warning_cost/papers_answer` | A letter already read in the opening is put aside “unopened.” | Remove the contradictory unopened state. |
| `the_evening_without_a_case/deciding`, choice 2 -> `desire` | Direct desire skips moving around the table; the shared node begins with her hand already on the Commander's shoulder. | Bring the characters together explicitly and make hand placement valid for every incoming branch. |

Also replace or justify `the_counting_room/start` calling the document “Ressa's copy.”
The earlier copy arrangement differs between warning choices; the false notice itself is a safer common reference.
`departure_note` is available immediately after personal acquisition, while its plant callback precedes the scene that actually supplies the cutting on the fresh route.
Establish the plant before using it as a shared memory, or make the early farewell wording independent of the later acquisition.

## Character and prose revision required

The native Anevia is affectionate, suspicious, funny, occasionally angry and willing to do useful work outside the law.
The installed `NPC_Common/Anevia` cues provide concrete anchors:

- `Cue_0025` describes unofficial searches and her position outside the knights' legal restrictions.
- `Cue_0044` shows anger at harm done to Irabeth, even when Irabeth accepts it.
- `Cue_0066` and `Cue_0067` distrust smug certainty and moral superiority.
- `Cue_0071` finds hope in the Trickster's unpredictable successes.
- `Cue_0077`, `Cue_0084`, `Cue_0085`, `Cue_0086` and `Cue_2` connect her hoped-for stone oven and bread to refuge, survival, Desna and a peaceful life with Irabeth.
- `Cue_3` changes that bread dream after Irabeth's death.

The manuscript's ordinary-life theme is therefore well chosen, but its dominant plant and rented-room imagery barely engages the existing, unusually specific bread dream.
An alternate new interest is legitimate; it should feel like something this woman adds to her life, rather than a replacement generic domestic identity.
A brief, consequential acknowledgement of the old dream in the future or grief material would help more than another long conversation about owning a room.
This does not require replaying her entire native biography or making disclosure of her transgender history a romance prerequisite.

More seriously, the source repeatedly explains the ethical meaning of actions immediately after showing those actions.
Examples include the final narration of `unborrowed_hour/quiet`, the account of accepting Irabeth's invitation in `beths_answer/finish`, the qualification after the ordinary lock in `a_key_that_is_hers/end`, and the ending commentary about what an ending does or does not award.
`ending_open` explicitly calls itself a relationship rather than a marriage “the ending awarded them by mistake.”
`ending_gone` says “The ending made no promise on her behalf.”
These are comments from the author about route design, not an in-world account of Anevia's life.

Keep the actual refusal, permission and independence choices.
Remove the repeated explanations once the scene has established them, and replace selected abstract conversations with concrete, characteristic exchanges.
In particular, retain Anevia's practical suspicion and imperfect temper rather than giving every civilian, wife and narrator the same polished vocabulary about expectations and obligations.
The requested improvement is a focused editorial pass, not a demand to increase the word count or add gratuitous trauma.

## Independent reproduction and verification limits

I copied the author's temporary harness into `C:/Users/Z/AppData/Local/Temp/anevia-independent-review-7zhtcj7v` and added independent reproductions using the actual `Rules.Available`, `Rules.Match` and walked source choices.
No shared output was rebuilt or replaced.
The run passed 315,751 assertions, including the author's focused suite and these explicit reproductions:

1. Played Chapter 3 acquisition and continuation, skipped the optional farewell, advanced to Chapter 5 and confirmed the incorrect post-return acquisition answer is selectable.
2. Played return and lasting commitment, stopped before the final farewell and confirmed `ending_unfinished` is available.
3. Added native Irabeth death to that earned state, left the optional grief visit unplayed and confirmed zero available ordinary individual Anevia endings.

Passing these reproduction assertions confirms the reported defects exist; it does not mean those behaviors are acceptable.
The tests remain headless source-model tests with supplied native facts and contact availability.
They do not prove actual Drezen actor availability, delivery after bereavement, shared bridge behavior or Unity save/load behavior.

The author reports 24,729 distinct aggregate words and selected early-acquisition paths of 10,898-13,104 words, compared with 10,073-12,246 for fresh Chapter 5 acquisition.
Those selected ranges are attributed measurements, not independently recomputed here.
The manuscript is plainly substantial on full read and exceeds the project's aggregate planning floor.
That does not establish per-character RanRomance parity in every campaign history.
In particular, Irabeth's death blocks the normal case and future scenes; the grief visit is a short alternate continuation, not a second fully developed bereaved campaign or new bereaved acquisition.
Actual lost-contact and universal bespoke Trickster access are not supplied by this module.

The separately authored native audit `reference/canon-review/anevia-after-irabeth-death-audit.md`, read before closing this review, makes the bereavement limitation more concrete.
Its installed records show Coronation `Cue_0421` starting `AneviaGone`, which starts the state hiding the capital actor after her temporary ceremony positioning.
A normal free-dialogue window before this departure is not proved.
Therefore the grief visit is conditional authored content, not a generally delivered native bereavement route.
The audit also identifies native responses to the Commander admitting that they killed Irabeth: Anevia leaves with a hateful glare.
Any future continuation for that history needs its own credible reckoning, not the generic support visit or a removal of the absence guard.
This chronology is attributed to that independent native audit; my headless run does not reproduce its Unity staging.

## Revision-specific scores

These are editorial judgments for this exact revision, not automatic test results or promises about the next revision.

| Discipline | Score | Main reason |
| --- | ---: | --- |
| Prose and pacing | 86 | Strong concrete moments repeatedly diluted by explanations of their intended meaning. |
| Native characterization | 87 | Humor, observation and loyalty work; native roughness, practical edge and specific future dream need stronger continuity. |
| Adult romantic development | 92 | Actual attraction, personal dates and voluntary graphic and explicit intimacy beyond a mere acquisition flag. |
| Player participation and agency | 93 | Useful investigation alternatives, failure consequences, distinct relationship answers and local exits. |
| Branch continuity and remembered history | 76 | Reproduced wrong chronology, commitment contradiction and missing provisional bereavement ending, plus physical joins. |
| Campaign depth and history coverage | 85 | Substantial ordinary route; bereaved and unavailable histories remain limited and integration is pending. |

The next review should first reproduce the repaired histories, then reread the revised shared nodes and editorial pass in their played context.
The route is worth finishing, but this revision is not ready for whole-route approval.

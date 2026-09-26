# Tirabade after-roads independent review

The six-scene contribution provides substantial investigation, separate development for each wife and a shared romantic payoff.
The first release contained seven branch-history joins; the final revision corrects them and receives bounded literary and canon acceptance below.
This review does not approve the complete route, its length, native delivery or art.

## Inspected material

Initial source: `storylines/tirabade_after_roads.py`, SHA256 `7644BF315164C42217419EC1DAD8D2DB9F8BAA9301AD2EBF018243C95F7BAE43`.
I read all six scenes and the author's handoff, compared the theft and evening histories in `tirabade_reckoning.py`, checked the campaign context and reviewed the relevant native Anevia dialogue in `reference/canon-dialogue.txt`.
The predecessor reckoning source was independently authored earlier by this reviewer; this review concerns the new contribution written by another author and does not constitute independent approval of that predecessor.
I also inspected `Rules.Available`'s prerequisite-time calculation for the timing finding below.
No source, export, image or test file was edited.

## Required continuity repairs

| Scene and node | Actual selectable history | Finding and repair |
| --- | --- | --- |
| `three_beth_account.walk` | `history -> record -> walk` | The shared walk adjusts a cover beneath Irabeth's arm, but only `statement` creates that cover. Give both branches common papers in a cover or use a neutral gesture. |
| `three_rooms_unlocked.night` | Earlier `three_beth_account.evening`, then final intimacy choice | The joke that Tessa lied about the supposedly silent bed recalls a claim supplied only by the optional `room` branch. Make the claim part of the shared welcome or replace the joke. |
| `three_rooms_unlocked.walk` | Either seating branch, then walk home | Irabeth puts her coat on again although she has been wearing it throughout this path. Only the mutually exclusive `night` branch removes it. Adjust the coat already being worn. |
| `three_unposted_notice.outcome` | `three_stolen_roads.book_safe` | The definite reference to the second thief assumes the pursuit-only encounter. Refer to possible accomplices or gate the specific reference on `followed`. |
| `three_back_of_seal.old_work` | `watching -> old_work` | The opening answers a question about Vald's location that exists only in `job`'s preceding choice. Put the question in the common node or make the opening self-contained. |
| `three_rooms_unlocked.chosen` | `welcome -> told -> chosen` | Irabeth is drawn away from the window, but `told` leaves her facing the closed door. Only `untold` establishes her at the window. Use a neutral movement or establish the position in shared text. |
| `three_unposted_notice.arrange` | Any ordinary timed completion from `three_beth_account` | The precise two-day wait is shorter than the minimum two successive 48-hour prerequisites before this scene, and players may wait longer. Use wording without a fixed day count. |

These are local textual repairs.
They do not require new flags, changed choice indices or removal of valid options.
The corrected revision below resolves these findings.

## Writing and separate character development

The commercial claim gives the earlier theft consequences beyond a single recovery decision.
Getting the records back makes Ista's rebuttal easier but does not prevent someone copying their information.
Saving the personal book leaves her replacing acknowledgments and working around an absent customer.
Neither choice becomes secretly perfect after the fact.
The damaged book remains damaged in the recovered-record branch, and Wenna's added memory is a credible response to the loss rather than a magical restoration.

Anevia conducts the evidence visit, enjoys being watched while working and asks for company within her expertise.
Her attraction is expressed through interrupted concentration, a collar adjustment, private teasing and her own kiss.
She does not exist only to explain Irabeth to the Commander.
Her refusal to enter Malven's rooms is tactical: getting caught would give him a useful distraction.
That fits the native covert operator better than an invented renunciation of every illegal method.
Her frustration survives the settlement, and the partial-refund conversation lets Ista limit Anevia's urge to keep pursuing the matter.

Irabeth has a different problem and desire.
She wants her promises to have the force of direct protection, catches herself before promising the copyist safety, and helps establish what the witness can actually say.
She then chooses and arranges an evening she wants for herself, rather than merely consenting to an outing organized by Anevia.
Her admission that she wanted the Commander's admiring look gives her an individual romantic stake.
Her pleasure in making Anevia briefly speechless is effective because her careful speech and sense of responsibility remain recognizable.

The final scene contains several affectionate jokes about practical arrangements, furniture and Irabeth's planning.
Most serve a particular moment rather than repeating an abstract discussion of relationship rules.
The investigation does repeatedly distinguish evidence from suspicion and authorized testimony from overstatement.
That is relevant to this plot, but a subsequent contribution should choose a different kind of conflict instead of building another long paper-and-witness sequence.

The supporting women retain their own stakes.
Ista controls her claim, Wenna contributes direct knowledge of the repaired covers, Gresa loses trading time, and Ressa chooses whether to appear or provide a statement.
The Commander's answer resolves a choice Ista explicitly offers because the household names are involved.
It does not let the Commander dispose of her livelihood without consultation.

## Marriage, attraction and player agency

The wives desire and attend to each other without waiting for the Commander to authorize it.
Their shared hands during the accusation, Irabeth's kiss after the first meeting, Anevia's pleasure at being admired and Irabeth's initiative in the rented room sustain the marriage within the new triad premise.
Each wife also approaches the Commander directly.
The bond reads as three related attachments rather than two interchangeable rewards.

The choice to name the relationship to Tessa or keep it private has a specific later response.
Neither answer is treated as shame, betrayal or insufficient commitment.
The sleeping options allow shared intimacy, affectionate sleep or a walk back to separate beds.
All complete the evening without a jealousy penalty.
The intimate passage is adult and non-graphic, with the wives' mutual attraction still present when the Commander joins them.

The branch selecting hand-holding instead of initial kisses still leads to affectionate dialogue.
That choice moderates the immediate action; it is not presented as a permanent rejection of all romantic touch.
The scene would be misleading only if later UI described it as such a boundary, which the inspected source does not do.

## Evidence choices and sustained consequences

The Perception DC 25 choice supplies explicit `SkillPerception`, Commander-only selection and distinct success and failure destinations.
It does not award affection or access to intimacy.
This review inspects the authored check definition, not a native roll executed in Unity.

| Evidence path | Immediate result | Later commercial consequence |
| --- | --- | --- |
| Successful inspection | Legible name and matching damaged seal link Malven's paper to the commission note. | He offers the full deposit back; accepting produces the full-refund callback. |
| Failed inspection | No reliable reverse reading; Gresa can still describe receiving the scrap. | The offered refund is half, with the unpaid amount and smaller next load retained. |
| Non-roll catalogue search | A complete common form identifies the paper type but cannot identify its broker. | The offered refund remains half, and Gresa's lost afternoon is acknowledged. |
| Circulate the accounts after any evidence path | Ista refuses immediate settlement and sends authorized evidence with the household denials. | Repayment remains outstanding; other brokers react, while the delayed booking costs real work within the fiction. |

The failed check cannot immediately fall back to the complete afternoon search after consuming the available time.
The non-roll option is a deliberate alternative with weaker evidence, not a disguised automatic success.
All paths still expose the false guarantee through the other witnesses and retain meaningful commercial choices.
The actual forger and Vald's location remain unresolved.
The source does not convert the meeting into an arrest or a native quest completion.

Ressa's in-person work record and signed statement have different meeting passages.
The signed route acknowledges the limits of absent testimony without inventing her presence.
The in-person route protects unrelated entries without promising that her business faces no risk.

## Canon and delivery boundaries

Native Anevia `Cue_0016` supports her attraction to Irabeth's fierce competence and private irreverence.
`Cue_0019` establishes the marriage's professional arguments, cramped domestic arrangements and spending on crusader work.
`Cue_0025` establishes Anevia's unofficial covert methods.
The new scenes develop those traits without declaring new anecdotes or civilian supporting characters to be recovered canon.
The triad, copied commercial documents, private merchant settlement and Tessa's room remain authored alternate developments.

The scenes require actual `three_open_road.kept` and `kept_terms` before their additional prerequisites.
The two individual investigations can be selected in either order, and the joint meeting requires both completions.
All six use Drezen and Chapters 3 or 5 and forbid closure, loss, inhuman state, either wife's away flag and `last_watch`.
No choices mutate native marriage, morale, another romance, inventory or currency.
Commercial payments occur only in the book-event fiction.

These local guards do not establish a complete acquisition or final-watch progression.
The author's handoff correctly identifies that the earlier `last_watch` can still close this optional chain before it is played.
Whole-route continuation, shorter endings and opt-in catch-up need separate integration work.
The six scenes also supply no new native morale-specific treatment, Trickster restoration, contact-loss handling or physical NPC placement.
They do not claim to repair those omissions.

The handoff's aggregate and selected-path word counts are author measurements, not an independent whole-route quality certificate.
Crossing the 42,000-word inventory floor does not establish an attainable complete playthrough, equal substantive depth per woman or RanRomance parity.
Actual rules tests, managed native-check construction, save behavior, dialogue presentation, ToyBox coexistence and finished art remain separate gates.

## Bounded disposition

The contribution's dramatic structure and character work support continued integration.
No full-route score is assigned.

## Corrected released revision

I reread the seven corrected joins in source SHA256 `E76C0D4CD02BF0554A2415E828006A2D2673B32753FB74B58EF8B9C64789F8E6`.
Irabeth now steps aside for a passerby instead of carrying a branch-specific cover.
Anevia's Vald remark is self-contained on both incoming paths.
The follow-up asks about Vald without inventing a witnessed accomplice on the intact-book path.
The waiting remark no longer supplies an incompatible number of days.
Anevia draws her wife close without assuming the optional window position.
The bed's complaint receives a fresh joke that does not recall Tessa's optional promise.
The walk home adjusts the already-worn coat.
All seven identified contradictions are resolved without needing new story decisions.

Bounded writing score: 92/100.
The investigation has specific costs and callbacks, each wife has distinct desires, and the shared evening pays off Irabeth's initiative with convincing married affection.
Some repeated evidentiary explanation and practical-arrangement jokes keep this from a higher assessment.

Bounded canon and character score: 92/100.
The wives' marriage, differing methods and familiar private voices survive the authored triad development, and the commercial outcomes make no unsupported native-state claims.
This score assesses consistency of the contribution with inspected evidence, not full native-outcome coverage or canonical status for the alternate romance.

No remaining material contribution-level writing or character-continuity blocker was identified in this pass.
The final-watch bypass, full-route character depth and length audit, morale coverage, native and ToyBox execution, art and other delivery gates remain outside this bounded acceptance.

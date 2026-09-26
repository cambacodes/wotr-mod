# Tirabade after-roads contribution

The contribution changes only `storylines/tirabade_after_roads.py` and this handoff.
It is ready for independent literary, canon and technical review, not promotion or installation.
The parent owns integration, tests, exports, existing modules and engine changes.
No installed files, native state, generated files, export or shared tests were changed.
No agents were spawned.

The new module SHA256 is `E76C0D4CD02BF0554A2415E828006A2D2673B32753FB74B58EF8B9C64789F8E6`.
The inspected predecessor `storylines/tirabade_reckoning.py` SHA256 is `EE9DE703CDABC12F3C880AEF95024D9FD2105EE794E2668D1AF52368F891317C`.
The inspected main development export SHA256 is `70D09CC9150AF3141ECC72C8934FA16A56AF69599701A57017B8C9A60F5EED79`.

## Played continuation

A forged commercial guarantee uses the Commander's household name and Ista's delivery details.
The recovered-record history supplies original paid acknowledgments; the intact-book history still lacks part of the stolen bundle and depends on replacement confirmations.
Neither history erases the earlier theft, the damaged personal book, or the two escaped thieves.
The investigation follows that existing authored quest rather than inventing a completed native quest.

Anevia brings the Commander into an investigation she conducts, enjoys their interest in her work, and chooses not to give the broker an easy distraction by entering his room illegally.
She retains her impatience, attraction to useful mischief, and dislike of respectable people talking down to her.
Irabeth gathers the copyist's testimony without claiming her rank guarantees the woman's safety, then asks for something she wants herself: arranging a private evening for the wife and lover she desires.
The wives flirt with and kiss each other independently of the Commander, and Irabeth takes the initiative in the shared evening.
The broker's insinuations concern influence and a commercial claim; they do not establish compulsory jealousy or make another romance a failure state.

| Scene | Owner | Additional prerequisite | Completion effect |
| --- | --- | --- | --- |
| `three_borrowed_names` | Together | None beyond common prerequisites | `three_borrowed_names.heard` |
| `three_back_of_seal` | Anevia | `three_borrowed_names.heard` | `three_back_of_seal.kept` |
| `three_beth_account` | Irabeth | `three_borrowed_names.heard` | `three_beth_account.kept` |
| `three_counterclaim` | Together | Both individual completions | `three_counterclaim.kept` |
| `three_unposted_notice` | Together | `three_counterclaim.kept` | `three_unposted_notice.kept` |
| `three_rooms_unlocked` | Together | `three_unposted_notice.kept` | `three_rooms_unlocked.kept` |

Every scene requires `three_open_road.kept` and `kept_terms`.
Every scene permits only chapters 3 and 5, in Drezen area `2570015799edf594daf2f076f2f975d8`.
Every scene forbids `closed`, `loss`, `inhuman`, `irabeth_away`, `anevia_away`, and `last_watch`.
The individual scenes and final evening have a 24-hour delay; the other scenes have a 48-hour delay.
Both individual scenes can be completed in either order before the joint meeting.
All are optional physical book scenes using the existing Tirabade entry mechanism.
No new scene is remote, manual-only, an epilogue, or an automatic rest encounter.

## Investigation and material outcomes

The Commander can inspect a faint pressure mark with a visible `SkillPerception` DC 25 check, explicitly `CommanderOnly=True`.
The original game's Camellia `GiveMeAnIdea/Check_0002.jbp`, GUID `19972884601e0284b992233e41d778a8`, uses Perception 25, verified in `reference/canon-review/native-romance-check-examples.json`.
The number fits a difficult close inspection of damaged writing in a chapter 3-or-later personal encounter; it is not a persuasion or affection threshold.
The expansion's existing native check builder supplies the actor policy and no-experience behavior, which differ from the original example's default evaluator and experience setting.

Success identifies Malven's name and damaged seal on the reverse of the thief's commission scrap.
Failure leaves the reverse unreadable and obtains Gresa's narrower witness account.
The non-roll option spends Gresa's remaining afternoon sorting forms, costing her trade and establishing common stationery without proving which broker supplied the scrap.
Failure and the non-roll alternative both reach every later scene.
The check choice has no outcome flags, `Next`, `Abort`, or premature completion.
The `impression`, `unreadable`, and `catalogue` flags are written only by their respective outcome pages.
Neither woman changes her affection because of the result.

Ressa offers either her original work record at the meeting or a signed statement, both with explicit limits on its use.
The meeting presents the selected evidence and handles her actual presence correctly.
Ista permits either a private settlement without a silence clause or circulation of the evidence with a narrowly worded household denial.
On settlement, successful inspection obtains the whole deposit; failure or sorting obtains half and leaves the remainder disputed.
On circulation, the deposit remains unpaid and a booking is postponed while other brokers examine the accounts.
The later visit plays each consequence separately.
No player currency is transferred, no inventory item is created, and no native arrest, court judgment or quest reward is claimed.
Malven's handling of the delivery details and use of the household guarantee are challenged, but the text does not pretend to prove who wrote the final forged lines.
Vald and the second thief remain at large.

The decision to tell Tessa that the three are lovers is separate from circulating the commercial denial.
Keeping the relationship explanation private does not reduce warmth or block the shared evening.
The final scene offers non-graphic shared intimacy, shared sleep without further intimacy, or a walk home and separate sleep.
No choice writes another romance's flags or a ToyBox setting.

## Canon and authored material

The inspected transcript is `reference/canon-dialogue.txt`, SHA256 `E10DD05FA5D08FF7AFD3DB4700433EDD65160F46D6FDC69DA3BCD4131ED2AE2B`.
`World/Dialogs/NPC_Common/Anevia/Cue_0011.jbp` supports Anevia's criminal childhood and practical experience.
`Cue_0016.jbp` supports her attraction to Irabeth's fierce competence and less polished private behavior.
`Cue_0019.jbp` establishes a strong marriage alongside heated professional disagreement and the cost of crusader spending.
`Cue_0025.jbp` establishes Anevia's unofficial covert work and willingness to operate outside official searches.
`Cue_0067.jbp` rejects condescension toward her past.
`Cue_0077.jbp`, `Cue_0084.jbp`, and `Cue_0086.jbp` reserve her bread-and-oven dream for life after the war; this contribution does not claim that dream has already been fulfilled.
The earlier original route and the campaign and reckoning modules supply the authored relationship, Ista's theft, Tessa's yard, the yellow sash and Irabeth's blue coat.

Malven and Ressa are newly authored adult supporting characters.
Ista, Wenna, Gresa, Vald and Tessa continue the previous authored civilian cast, not newly discovered native NPCs.
The counterfeit guarantee, copyist visit, private merchant meeting, book-event refunds, and Tessa's upstairs room are alternate developments.
Irabeth's recollection of early teasing around locked doors is an invented anecdote consistent with the cited relationship, not a transcript event.
No native marriage, morale outcome, military resource, death, resurrection or spouse quest is rewritten.

## Attachments, late availability and integration proposal

Current `Rules.EntryTargets` attaches Anevia scenes to answer list `33960c7f7af40cd43b7f801a76c87a0b` and Irabeth scenes to `871af36f2ab2b1f40b5de77976c54276`.
Together scenes use both existing lists.
This is verified source behavior; this contribution did not independently extract those lists again or execute them in Unity.
The current relationship metadata blocks both women's dead/gone flags and swarm/true-lich states.
`Main.State` derives `loss` from deaths, gone flags and sacrifice, and `inhuman` from swarm or true lich.
These are existing derived predicates, not missing authored declarations.
The module itself supplies no `ContactUnit`, so it does not gain the newer live-unit/contact-loss continuation predicate.
It inherits the earlier Tirabade attachment and flag protections, with the same remaining runtime locality and mid-book interruption limits.
Nothing here places Gresa, Ressa, Malven, a receipt, or Tessa's room in a map.

The original `last_watch` requires only `future`, has a 24-hour delay, and completes a flag which all these new scenes forbid.
It can therefore be selected before this optional continuation or even its predecessors finish.
This is an early physical-dialogue availability problem, not the remote automatic-rest queue defect fixed for Kiana.
Reordering the six new scenes cannot repair it.
The original committed ending similarly requires `committed` without proving that the developed shared campaign was played.
No original last-watch, commitment, ending or old-save behavior was changed within this ownership scope.

For integration, append these six objects without changing existing IDs or choice indices, then test both individual-scene orders from actual `three_open_road` completion histories.
For new developed-route progression, the parent should provide an explicit continue-or-decline decision before the final-watch entry can silently foreclose the remaining shared campaign.
An affirmative continuation should defer final-watch availability until `three_rooms_unlocked.kept`; an explicit decline needs honest shorter-route ending treatment rather than credit for unplayed development.
For existing completed-last-watch saves still eligible to talk in Drezen, a separate opt-in catch-up should authorize only the necessary authored `last_watch` forbid overrides throughout the unplayed chain.
Do not clear the old completion flag or bypass death, departure, closure, area or mythic restrictions.
The parent must review how much of the earlier optional chain such a catch-up needs, rather than overriding this module alone and leaving its prerequisites unreachable.
Attainable Trickster restoration and post-final-battle delivery remain separate unresolved work.

## Read-only verification and remaining gates

The six-scene contribution contains 77 nodes, 10,625 raw words, 9,828 prose words, 797 choice-label words, and 10,559 exact-normalized distinct-segment words.
The larger aggregate includes mutually exclusive evidence, settlement and intimacy passages.
A read-only graph walk coalesced identical flag histories while retaining minimum and maximum selected prose-and-choice counts.
It reached all 77 nodes, both native-check outcome branches, and 288 distinct final histories across both theft decisions, with 1,372 completed scene paths explored.
A separate reverse-order walk produced the same 144 final histories per theft decision when the Irabeth scene preceded the Anevia scene.
Selected continuation length after the review corrections is 6,928-7,340 words for recovered records and 6,945-7,357 for the intact-book history.
The traversal checked exactly one evidence outcome, exactly one financial outcome, exactly one final-night outcome, and the dependence of the full refund on successful inspection.
It found no dead node, duplicate existing scene ID, unresolved flag reference after accounting for the engine's derived flags, or mutation outside the new `three_` flags.
This author walk does not replace `Rules.Available`, native binding checks, managed blueprint construction or actual save execution.

The inspected main shared inventory is 34,554 raw and 34,315 distinct words across 48 scenes.
Adding the contribution in memory yields 45,179 raw and 44,874 distinct words across 54 scenes, counting shared text once.
That clears the numerical 42,000 planning floor only as an aggregate inventory.
It does not prove semantic originality, full selected-route length, equal independent depth for each woman, complete RanRomance parity, or literary approval.
The separate individual development, whole-route ending predicates and earlier acquisition remain audit requirements.

The parent still needs staged rules tests for actual prerequisite histories, delays, chapters, area, native death/gone/away flags, closure, final-watch ordering, the check attempt boundary, and both check results.
Managed construction must verify native check type, visible DC preview, Commander actor selection, success/failure references and no premature completion.
Actual Unity checks must cover dialogue attachment, rerendering, interruption, saves, UI, native rolls and ToyBox coexistence.
No assertion count here claims those were executed.

No new art was generated or installed.
Possible scene art is the damaged seal at Gresa's counter, the wives and Commander facing the broker, and the upstairs room with Irabeth's blue coat and Anevia's yellow sash.
Their recognizable portraits, married body language, adult supporting cast, composition and runtime asset lookup need independent art review.
The code tolerates missing scene portraits, which is not an art-completion claim.
No review score is self-assigned or promised.

## Independent-review corrections

The first independent review identified seven branch-join or elapsed-time defects in draft `7644BF31`.
The final source replaces a statement-only document cover with a neutral street action, makes the Vald-location answer self-contained, and names only Vald in the common follow-up rather than assuming the second thief was witnessed.
It removes the unsupported two-day duration and the assumption that Irabeth is at the window after both welcome branches.
The final night no longer assumes the optional conversation about a silent bed, and the walk home no longer puts on a coat that was removed only in a mutually exclusive branch.
These corrections change prose only, preserving every ID, choice index, prerequisite, flag and check.
The author reran selected-length traversal after the corrections; independent reinspection is requested and is not presumed passed by this handoff.

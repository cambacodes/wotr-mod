# Kiana further consequence handoff

The reviewed source is `storylines/kiana_further.py`, SHA256 `3601A346BCDCC49E109B38016916BA562C31AB2ED19D00FC006E6D4DB5663BF9`.
Root corrected the withdrawn-performance line after independent review because the Commander is present during that speech.
The focused tests are `tests/KianaFurtherTests.cs`, SHA256 `7305BBD68FF464ED4110C6D5B5773348821282C028F18CA0E8067C4EB1309D5F`.
Only those two files and this handoff were edited.
Source ownership is released for parent staging and independent review.
No shared engine, existing source, export, artwork, native bindings, or installed files were changed.

## Why this incident belongs in the route

The assembled audit asks for consequences outside meals, private rehearsals, and explanations that grief and joy coexist.
The existing follow-through gives Kiana readers, a working room, an independent budget, and a relationship that can survive an unfinished page.
It does not yet make her face the public power attached to the person she loves or a use of her work that she cannot control through friendly rehearsal.
This contribution makes both problems concrete before the fresh route's developed commitment conversation.
It does not attempt to repair the separate lack of played development before the early authored separation.

Kiana lends one page to an adult civilian messenger, Rovan, who wants to amuse wagoners.
He advertises an entertainment as requested by the Knight Commander and lets an ambiguous joke imply compulsory attendance.
He also replaces the missing ending with a captain who teaches the princess to be less troublesome.
The player and Kiana confront the actual notice and page at the yard.
A real Diplomacy check can get a candid explanation without making the encounter feel like an official reprimand.
Failure makes Rovan deferential and evasive until Kiana draws out his account herself.
A non-roll alternative gives her room to handle that conversation privately while the Commander waits.
These are differences in the played encounter, not rewards of affection or changes to crusade statistics.

Kiana can offer the correct scene after an explicit public correction, or withdraw her page and let the wagoners arrange their own entertainment.
The second scene plays the chosen result.
An audience member actually leaves the voluntary reading, which is allowed to matter without turning into a failure.
The withdrawal branch hears somebody else's story instead of somehow receiving the same successful performance.
Orvenna, an authored adult carter who heard Rovan's altered ending, uses its moral to make an accusation about Kiana's private life.
The Commander can object or leave the answer to Kiana.
Kiana corrects the intervention if needed and answers from the actual separated or widowed history.
The widow branch does not accept the false premise that she left a living husband.
The separated branch does not recast Elan as a villain or claim his agreement to the Commander relationship.
Orvenna's limited admission of wrongdoing does not turn her into a new friend or provide a neat reconciliation.

The final scene pays off the decision to share or withdraw the page, then lets Kiana disagree with the Commander about public intervention.
She can be grateful for help and resent needing it without the narrative pretending either reaction is the whole answer.
The player can agree to wait for her request or retain the right to object to humiliation while refusing to speak for her feelings.
Different replies address the actual choice to speak or remain silent at the yard.
Waited, affair, and widow histories then lead to separate private exchanges.
The affair branch keeps responsibility for the undisclosed kiss; a stranger's cruelty does not retroactively make it considerate.
The closing intimacy is adult and graphic and explicit, with a private evening or an unadvertised walk.
Neither changes commitment or demands exclusivity.

## Integration contract

Append `SCENES`, then call `kiana_further.integrate(payload)` on the assembled payload.
The overlay adds only `kiana.further_kept` to `kiana.a_place_afterward.Requires`.
It validates that the capstone and all four new scenes exist before changing the payload.
It is idempotent and preserves every existing scene ID, node ID, choice index, effect, and prose segment.
Use an assembled deep copy as usual; do not mutate imported source lists while making an isolated review stage.

Register `KianaFurtherTests.Run(story, Check)` when the new scenes are present.
The parent must update existing `KianaProgressionTests` and any Program campaign list that expects the capstone immediately after `kept_evening`.
Insert `borrowed_name`, `yard_evening`, and `unborrowed_evening` after that scene and before `a_place_afterward`.
The author did not edit those shared files.
No new native aliases or engine schema fields are required for the supported histories.

| Scene | Entry and result |
| --- | --- |
| `kiana.later_incident` | Manual-only invitation after an already completed developed capstone; acceptance sets `further_requested` and existing `catchup_requested`, deferral changes nothing. |
| `kiana.borrowed_name` | After `followthrough_kept`, 48 hours; completes with `further_name_kept`. |
| `kiana.yard_evening` | After `further_name_kept`, 48 hours; completes with `further_yard_kept`. |
| `kiana.unborrowed_evening` | After `further_yard_kept`, 48 hours; completes with `further_kept` and the selected private-evening or private-walk outcome. |

All new scenes retain Chapter 5, Drezen, the completed native soul quest, the existing lovers history, and `followthrough_kept`.
They use the existing book invitation delivery and do not claim a new physical native contact or actor adapter.
All block closed and inhuman histories.
The three story scenes forbid `farewell` and `future_settled`, with narrow overrides for `catchup_requested` and `further_requested` respectively.
The new manual letter does not forbid farewell, because it explicitly offers a new incident after an older completed decision or farewell.
It requires both `future_settled` and `followthrough_kept`, so it is not a shortcut around the old substantive campaign.

A fresh route plays the incident before the still-unplayed capstone.
Its capstone delay now also considers the actual `further_kept` timestamp.
An older route that already completed the capstone keeps that completed scene, promise or open future, and existing ending eligibility.
It cannot automatically enter the new incident merely because the source was updated.
Accepting the manual letter is explicit consent to these later events, not a reset of the earlier decision.
Old farewell flags and timestamps remain untouched.
If an older developed save has not yet played farewell, the existing farewell may still occur before the newly requested incident in the rest queue.
That is compatible with the explicit later invitation and its catch-up override; it does not suppress the new scenes or reinterpret the farewell as never having happened.
The older early-farewell catch-up mechanism also remains valid when the old decision is still unplayed.

## Replay and branch history

The three conversational approach outcomes, performance offer versus withdrawal, public intervention versus silence, and private agreement about intervention use opposing-choice guards.
An interrupted replay cannot collect both sides of those decisions.
Already recorded Diplomacy success or failure supplies a reentry choice instead of a second roll that awards the opposing result.
The non-roll approach is likewise blocked after either rolled result has been recorded.
The final private-evening and walk markers are written only with terminal completion, so they cannot accumulate through a partial replay.
No flag is cleared or overwritten.

The native marital history is read consistently with the existing route.
Supported histories are separated with a living native Elan, or bereaved with native Elan dead.
Within separation, the actual waited versus affair flags retain their existing precedence.
The assignment does not reconcile experimental changes to Elan's native state after a relationship history has already been played.
The current shared Rules file has no Kiana-specific consistency predicate, and earlier modules have the same unsupported mixed-history hazard.
A native death/restoration transition that creates separated plus dead, bereaved without dead, or both authored histories needs shared reconciliation or an availability guard before these history-specific scenes are offered.
This limitation was reported to the parent before staging and must not be described as tested restoration compatibility.

## Native and authored evidence

The author read the assembled readiness audit, current base route, consequences/follow-through progression and handoff, and the extracted actual game dialogue in `reference/canon-review/kiana.txt` and `reference/expansion/kiana.txt`.
The native married aftermath embraces and playful marriage dialogue remain the baseline; there is no native claim that Elan mistreats her or approves an affair.
`ElandKianaAftermath/Cue_0001`, BlueprintCue `81109ea8fb20dbc478cf67116740f4a1`, depicts their affectionate reunion.
`Cue_0006`, `a819e8c85ef23324bb0d8117bb9d7df3`, and `Cue_0007`, `df45181e1968f26459f9e8bc2b995a34`, establish marriage, frank humor, and interrupted marital intimacy.
`KianaAloneAftermath/Cue_0001`, `aebbc1845e827dd4da4e28014e7b4162`, and `Cue_0010`, `e0abe01a6531ec6499f21e44cc81afe6`, establish actual widowhood and her wish for later friendship while needing immediate solitude.
The native quest completion and aftermath aliases remain those already implemented by the parent.

The writing career, separation, guest circle, and Commander relationship are established authored developments rather than newly discovered native content.
Rovan, Orvenna, the civilian wagon yard incident, copied notice, altered page, and performance are new authored developments.
They do not correspond to installed NPC blueprints, a native army order, requisition, economy transaction, or persistent world event.
No departure of a real convoy, change in troops, or resource deduction is claimed.
The workroom/copying budget choice remains intact; Rovan receives a single lent page whether Kiana previously chose a quiet desk or paid copies.
Kiana remains an adult oread with her existing crystals and identity; the vampire princess is fictional.

## Checks and measurement

The source imports successfully.
A read-only source traversal reached all 36 new story pages across waited, affair, and widow histories.
It also examined 156 distinct partial replays without a missing target, dead end, or incompatible outcome group.
Including those replays, it encountered 705 terminal outcomes.
The manual invitation adds one page and has a terminal opt-in or flag-free deferral.
A deep-copy assembly check verified that the overlay is idempotent and leaves the imported prior capstone source unchanged.

The local markup-stripped measurement is 3,945 raw words and 3,926 distinct text-segment words, including the manual letter.
Selected complete three-scene incident paths contain 2,260 to 2,394 words, counting displayed pages and the chosen answers.
The parent should run the project inventory counter before publishing totals.
Adding the provisional 3,926 to the supplied existing 20,166 gives approximately 24,092 distinct words, but numerical threshold passage is not a semantic quality audit or full-route approval.
No self-score is assigned.

The focused C# suite plays the actual existing route from the initial invitation to the follow-through for waited, affair, and widow histories, with and without an earlier commitment.
It tests fresh insertion, old developed decisions, old developed farewells, and older early-farewell catch-up.
It checks the default fresh rest queue, capstone and farewell gating, manual opt-in and deferral, preservation of old decisions and endings, all-page coverage, selected outcomes, partial replays, native/unrelated flags, timestamps, chapter/area restrictions, prerequisite loss, and exact delay boundaries.
The C# suite is delivered for parent execution; author source checks do not claim that it has already passed the staged engine.

## Remaining full-route work

Independent literary, canon, and technical review must judge the delivered source and staged assembly.
The earlier transition from affectionate native marriage to authored separation still needs more played development if the full-character audit requires it.
Native physical availability for book-staged meetings, state-changing Elan outcomes, pre-wedding access, bespoke Trickster access, other mythic transitions, portrait and scene-art installation, save/resume, and actual game presentation remain separate requirements.
This incident adds a real native skill-check contract, `CheckDiplomacy` DC 24 with CommanderOnly true, plus a non-roll alternative.
The DC is an authored social difficulty for obtaining a candid answer under the Commander's public authority, not a recovered native dialogue DC.
It does not convert every narrated market action into engine exploration.
The route still needs actual Unity checks and ToyBox Love Is Free and Jealousy Begone coexistence verification before a full release claim.

# Soana opening independent writing and canon review

## Current decision

Final reviewed source SHA256: `9BCAECD7F791534213DC20F6509018893BD913FB2CC2487192DE2E71FD9C30DA`.
The corrected three-scene opening earns 92/100 for writing and 92/100 for bounded canon fidelity.
All required editorial defects identified below are resolved in this source.
The final callback names the swollen knuckles established in the opening, so the waiting path no longer inherits an injury from restraint.
The writing reassessment is 23/25 for voice, 22/25 for player choice, 18/20 for staging, 14/15 for adult relationship context and 15/15 for prose and pacing.
These scores approve only the reviewed opening's editorial scope.
They do not approve the complete route, artwork, contact adapter, export, runtime compatibility or release.
The outstanding full-campaign requirements below still apply.
The following sections retain the original findings and correction history.

## Original review

Reviewed source: `storylines/soana_opening.py`, SHA256 `31C503990F5E5B8BF8476E979EB1316C4391A04222152E613DE5DEF135EAC626`.
I read all three scenes, `reference/parallel/soana-opening-handoff.md` and `reference/canon-review/soana-route-evidence.md`.
This is an independent demanding editorial review of the frozen opening, using the retained native evidence rather than a fresh extraction of every referenced blueprint.
I did not edit source, exports, installed files or tests.

The opening earns 89/100 for writing and 92/100 for fidelity within its explicitly limited living postquest premise.
The writing score is below the required above-90 threshold.
Neither score approves the full character route, art, native contact or release.

| Writing criterion | Score | Finding |
| --- | ---: | --- |
| Soana's voice and scene interest | 23/25 | Proud, exacting, irritable and capable of unexpected humor, with useful work carrying the first two encounters. |
| Choice and player characterization | 20/25 | Waiting and restraint produce real differences, but the moral conversation assigns the Commander a history and doctrine that the player did not choose. |
| Continuity and physical staging | 17/20 | The repairs and delayed callbacks mostly hold together; the knife and cloth occupy incompatible positions. |
| Adult attraction and relationship context | 14/15 | Interest concerns the elderly woman present, and Corven is neither erased nor silently declared dead. |
| Prose and pacing | 15/15 | The three visits have distinct purposes, strong concrete detail and economical humor; the defensive qualification around attraction could still be reduced. |

## Required corrections

1. Repair the knife and cloth staging in `threshold/look -> wait`.
Soana stops with the cloth suspended between her hands, but the same paragraph sequence says her knife lies on the folded cloth within reach.
The waiting branch then says she puts the knife down, although no intervening action has her take it up.
Put the knife on a nearby stone from the start, leave the cloth in her hands, and let her lower the cloth when agreeing to wait.
Her later reaching for the knife will then follow the physical action already shown.
The restrained branch should still let her cover the animal before picking up the knife to cut the strap.

2. Stop assigning the Commander's military ethics in `guardian_question/cost`.
The chosen answer acknowledges that terrible measures may cost lives and asks Soana to recognize the victims.
It does not establish that the Commander has only asked volunteers to face death, nor that refusal would have been accepted.
The subsequent automatic lines, "I have asked people to face death" and "Then I would have had to decide what to do without them," assert those things anyway.
This can contradict a coercive or authoritarian Commander, including a Trickster whose actions have not been benevolent.
Give the player an answer about their actual position, or rewrite the automatic reply as a question about Soana's arrangement without supplying a favorable invented history.
One possible answer admits that the Commander has also compelled obedience and now wants to examine the cost.
Another can state that people have been allowed to refuse.
Both may lead to examining an alternative without requiring Soana to excuse either person's conduct.
This does not require writing an approving romance with coercion as its reward.

## Canon findings and retained limits

Soana remains an elderly dwarf rather than a younger substitute.
Swollen knuckles, effort on the uphill path, exacting practical instruction and her refusal to be treated as a picturesque relic support her established identity.
The retort about saying the first part of the attraction declaration is particularly effective.
Her warmth remains guarded, and she does not become a kindly teacher whose prior cruelty has vanished.

Corven's wreath and marriage, their children and the holy spring are consistent with the retained native dialogue evidence.
The opening does not decide whether Corven is living, dead, divorced or willing to accept another relationship.
The source records that the marriage has been discussed, not that it has ended or that a new commitment is permitted.
The handoff correctly leaves present marriage context as required future work.

The guardian question gives BearDead precedence when both native outcome markers exist.
The living branch concerns continued binding rather than claiming that Orso was healed.
The dead branch concerns Soana's wish to obtain another guardian rather than inventing a successful replacement.
Neither grants spirit release, restored forest, repaired native history or resurrection.
Her justification is recognizably proud and frightened, and the exchange allows her to remain angry without making anger proof of attraction.

The alternative-method branch challenges her prejudice against mages directly.
The hardship branch does not yet make her confront that prejudice with respect to a magical Commander.
That is acceptable as an unfinished opening, but it must remain on the route's outstanding requirements and cannot be counted as completed reactivity for all continuing players.
Her agreement to hear one account is a modest authored development, not a complete ideological conversion.

The knife defect aside, the material consequences mostly survive the joins.
Waiting costs reed-gathering daylight and the promised bundle receives inspection in the next visit.
Restraint causes an additional scrape, and reconsideration and defended expedience return as different later conversations.
The carrier contains a sound pot and a damaged handle throughout its repair and stream test.
The fox remains an ordinary invented animal rather than a proxy native quest actor whose condition changes game state.

## Improvement without changing the premise

The opening repeatedly explains what a visit, touch or reply does not mean.
That is strongest when Soana herself refuses a presumptuous interpretation.
Narrator and choice qualifications such as accepting a conversation without treating it as an answer to one's interest are less necessary on the purely practical path.
A plain invitation to continue the Orso conversation would fit both histories.
Retain the clear marriage discussion and her own explicit limit on romantic expectations; later scenes can rely more on those established exchanges.

Do not increase the score by adding intimacy before the route earns it.
The current restrained attraction is appropriate to these opening visits.
Later mature content still needs actual mutual desire, present relationship context and enough shared experience to make that desire specific to Soana.

## Readiness decision

Keep this contribution unexported while `soana.contact_verified`, `soana.opening_eligible`, native aliases, the relationship definition and portrait remain unimplemented.
An answer-list target and a postquest etude do not prove that the real speaker is alive, visible, local and nonhostile.
No headless checks were run as part of this editorial review, and the author's graph traversal does not substitute for production-engine or Unity verification.

The reported 4,269 words across alternatives are an opening contribution, not the required 21,000 meaningful-word campaign or an attainable single-playthrough total.
Trickster access and recovery, later chapters, marriage context, full romance development, endings, finished art, ToyBox runtime compatibility and game/save verification remain outstanding.
Correct the two required writing defects and submit the changed source hash for bounded rereview.

## Rereview of the first corrections

I read the complete changed source at SHA256 `5DBD495A5F78BB67D8F6EFE630CAEE1594AB8C86DD49CB1187A6EED0CD21B01F`.
Both original required corrections are resolved.
The knife stays on a stone and the cloth lowers to her lap before waiting.
The hardship branch now explicitly offers permitting refusal, demanding obedience or acknowledging one's own questionable decisions.
Soana answers each position differently before agreeing to examine a method.
This preserves an authoritarian Commander's possible history without making Soana flatter or absolve it.

One new continuity error prevents final acceptance of this revision.
The new `command_refusal` node refers to her scraped knuckles regardless of the earlier fox choice.
The waiting branch never gave her that injury.
Use her hands or established swollen knuckles there, or gate the injury wording on the restraint history.
The original handoff's source hash and node count also need updating before this revision is treated as frozen.
The full-route and contact limitations above remain unchanged.


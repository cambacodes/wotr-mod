# Konomi assembled route gap audit

The current route is a coherent short romance outline with finished scenes, not a complete campaign at the requested depth.
It does not pass full-route approval.
Earlier bounded scores for individual writing and canon fidelity do not establish coverage, political consequence, access, or a satisfying complete playthrough.
No arithmetic average of those scores is used here.

## Reviewed artifacts and assembly check

Reviewed all of storylines/konomi.py, SHA256 8EA6E596C8CB500BE7B0930601699F06C0E3350255BFCC82E5874A4F80942CC0.
Compared its complete SCENES list and relationship metadata with development/Story.json, SHA256 43DF0DB4E118739F78BA9E7F7E6E0A4C5B41E953D561830E3942034C5E8D19CA.
Every generated Konomi scene and the relationship metadata exactly match the source objects.
This finding establishes that the export contains the reviewed material; it does not test the game runtime.
The twenty exported Konomi objects comprise thirteen playable scenes and seven ending objects.
Eleven playable scenes form the main sequence, while unsent and parting are optional.
The supplied measurement is 6,016 raw words and 6,010 distinct words against the 21,000-word floor.
That is approximately 28.6 percent of the distinct-word floor, leaving 14,990 distinct words to add before length alone passes.
More material is necessary, but repeating reassurances or writing cosmetic variants will not repair the campaign gaps below.

## Native character anchors

The relevant comparison source is reference/expansion/konomi.txt, extracted from actual native dialogue.
Diplomacy_Officer/Cue_0014, ba4efaac0716c6549998b75d77f51181, establishes that she serves Galfrey rather than the Commander and was sent to lead the Diplomatic Council.
Cue_0028, 4014e41c1d763164aaa4ae96efd14cc2, defends the Royal Council's experience and concern for Mendev's future.
Cue_0016, 2f4b52dd74dd6a14981d0de2f9b631b0, favors layered political agendas and long-term strategy over bloody warfare.
Cue_0040, 35c3dcd5356d4bc428e70dbf99230463, describes politics as an exhilarating hunt.
These motives are stronger and more specific than simply being organized, sarcastic, or willing to disagree with a lover.

Native late-game conditions also matter.
Diplomacy_Officer/Cue_0032, 07459f4d09fa81e4b99beea351fb0434, describes a national crisis with paralyzed institutions and impending famine.
Cue_0029, 9980a1ecf3ca24e42ab3b22f858677b5, describes foreign garrisons restoring order while raising concerns about occupation.
Cue_0042, 60585f7319a294147a54f440865b21a2, describes an internally resolved crisis instead.
Diplomacy_8/Cue_0020, 8311ef29223c4fe469c95cd8eb80e539, grants the Commander earned political respect.
Diplomacy_8/Cue_0081, 7f64a30ceb4bfb046990bccbded7ac75, explicitly says the Diplomatic Council has served its purpose and is no longer needed.
A full private arc should read the actual applicable history instead of assuming that every campaign still has the same council, responsibilities, and level of professional respect.
These cited branches are alternatives, not events every player experiences.

## Findings requiring substantial additions

### Political consequences stop before their difficult part

The disagreement, leak, and reckoning sequence provides a credible starting conflict.
It preserves native supply decisions by making the petition an authored side matter rather than silently replacing a resource vote.
It also gives Konomi her strongest moment of political enjoyment in reckoning.source.
However, the main consequences arrive as completed reports.
The player never encounters the intermediary, responds to the threatened loss of couriers, sees the requested hearing, or watches Konomi recover her access to the policy dinner.

The public branch announces a material cost in reckoning.public and counters it with clever correspondence in reckoning.audit.
The route then advances without showing whether that counter succeeds, what it costs, or how the household treats her afterward.
The discreet branch reports that she has already traced the leak, and both branches join the same source and petition resolution.
Afterward public_cost, traced_leak, petition_resolved, and scandal_answered do not produce a further political scene.
Only the broad public/private distinction reaches an ending.

Add a played follow-through in which the public response and private investigation cause different encounters.
Let Konomi choose between two defensible ways of preserving influence, and let the Commander support or complicate her choice without taking over her office.
Show a witness or correspondent reacting to her work after the scandal.
Resolve the hearing or courier threat explicitly, including a cost that a clever letter cannot erase immediately.
A named new intermediary or patron is an authored addition, not a native fact, and should be introduced as such.

### The provision dispute avoids an enduring disagreement

In disagreement, the three player positions have distinct concerns.
In reckoning.petition, spoiled reserves explain the error and outside donors supply the settlement without drawing on Drezen's shipment.
This is a plausible individual resolution, but it allows every surviving branch to emerge substantially vindicated.
It does not test the route's repeated promise that affection can survive a decision one partner genuinely loses.

Add one dispute grounded in an actual completed diplomacy decision or a clearly separate new dilemma where good information still leaves competing obligations.
Konomi may remain dissatisfied with the result and continue the relationship.
Follow that dissatisfaction into a later meeting rather than ending it with an apology for tone.
Never make her career policy change automatically because the player selected the romantic answer.

### Chapter 5 lacks Konomi's own political crisis

Return discusses conflicting reports and emotional uncertainty, but it does not establish what happened to her office, patronage, Queen, or national obligations.
Power shifts quickly from those issues to broad relationship assurances.
Ordinary and farewell then settle into domestic comfort without a professional choice that tests the future they have promised.
This underuses the actual character who is loyal to Galfrey and invested in Mendev's political order.

Add a substantial return sequence that recognizes the current political situation and her own work during the Commander's absence.
Include a confrontation over a real conflict of duty, followed by her independent decision about what she will do next.
An occupation outcome, domestic recovery, or dissolved council should change the content rather than merely the scenery.
A romance can continue after institutional change, but the story must identify her new role instead of carrying an old appointment forward by implication.

### The courtship's activities are too often summarized

Evening.supper summarizes the failed guide story rather than allowing the player to experience its details.
Evening.quiet summarizes the luggage story.
Return.talk summarizes the Abyss conversation without offering a specific disclosure or Konomi's specific response.
Power.commit says they make plans and disagree over one of them, but never states the plan or disagreement.
Ordinary.honesty summarizes another difficult conversation.
These transitions make the route seem longer-lived than the playable exchanges actually are.

Expand selected activities into conversations with concrete subjects, interruptions, disagreements, and remembered details.
Give Konomi tastes and aims that she can pursue without the Commander, while retaining the native enjoyment of politics.
The gardening motif is a useful private invention, but it cannot carry nearly all her nonofficial life.
Add an outing or joint task whose result the player can later encounter.
Let at least one intimacy scene change because of what the pair actually did earlier, beyond choosing kiss versus quiet company.
Adult warmth and attraction are present; the missing quality is accumulated familiarity and consequence, not explicit sexual description.

### The repaired denial is not tested again

Leak.lie can become almost_denied, followed by reckoning.repair and a sincere apology.
Repaired explicitly asks for time before trust feels secure again.
After that, the main route makes no further use of almost_denied or apologized.
Return, commitment, and domestic settlement proceed as though the requested time produced trust automatically.

Add a later occasion when acknowledging the relationship has a real cost and the player can act differently.
Konomi should notice the changed behavior, or identify that the apology has not been followed by it.
This can produce delayed reconciliation, a changed commitment conversation, or separation without jealousy mechanics.
The relevant conflict is honesty and dignity, not the number of the Commander's partners.

## Access and chronology findings

All ordinary scenes use the same native answer list, 0dc8b8604bb33c846a63f3eb62443674, in Drezen.
A genuine repeatable officer root is preferable to attaching every scene to a one-shot rank-up, but it does not establish contact in every quest or mythic state.
The assembled payload has no Konomi-specific native etude aliases, seen-cue conditions, completed-quest bindings, or revival entry.
Relationship metadata also has empty UnavailableFlags and FailureFlags.
Thus the current payload cannot express Konomi's own native political outcomes or a missing-contact recovery through those mechanisms.
This is an observed implementation gap, not proof that every ordinary save fails to show the route.

Margin through reckoning are permitted in both Chapters 3 and 5.
Margin refers to the Royal Council, reception assumes she still wears clothes to council, and reckoning.aid asks that an admission not be repeated in front of the council.
These are conditional continuity risks, not established contradictions on every Chapter 5 save.
Diplomacy_8/Cue_0081 supplies evidence that the Diplomatic Council can finish its work, but this pass has not resolved the exact native branch predicate or proved that every use of the word council refers to that dissolved body.
Verify those predicates and identify which institution each line means before changing its wording.
A late-start variation of return would distinguish a relationship that existed before the Abyss from one begun after the Commander returned.
The present generic start, hers, and talk nodes do not establish a false pre-Abyss courtship memory, and the letter option correctly requires wrote.
The missing late-start variation is therefore a depth and reactivity gap, not a proven false-history defect.

Farewell is available after ordinary plus its delay and is not gated to actual final preparations.
Its entry says it occurs before the final fighting, even if the player still has substantial Chapter 5 work to do.
Tie its availability or wording to a verified late-campaign state.
Do not assume that a chapter number alone establishes final-battle imminence.

The optional unsent scene is a sound nonmagical treatment of Abyss separation, but it is the route's only Chapter 4 contribution and has no Konomi viewpoint or consequence beyond the return letter.
The fear and wonder choices both join the same text and receive no distinct response when she reads the letter.
Expand those threads with actual content and a different response in return.
More Abyss content need not invent a reliable interplanar courier or pretend that an imagined scene restored contact.

## Mythic and ending coverage

Power.trickster articulates a good boundary between reopening circumstances and rewriting Konomi's will.
It implements neither a new introduction nor restoration of a missing actor or contact channel.
The requested attainable Trickster campaign therefore remains incomplete even if its philosophical dialogue is acceptable.
Design and verify the concrete lost-access cases, then write the corresponding actions and aftermath.
A prior rejection should remain her decision unless she freely changes it after new events.

The current inhuman branch combines physical transformation and ethical consequences into general accommodation.
A Lich, Swarm, or other hostile political outcome cannot be assessed solely through whether supper or a kiss is convenient.
The user permits character restrictions outside Trickster, so a credible refusal or limited contact is preferable to unexplained universal acceptance.
Write the applicable response to actual deeds, allegiances, and dangers, and do not treat a creature-type label alone as an account of the relationship.

The seven endings distinguish public, private, transformed, ascended, apart, unfinished, and True Aeon presentation.
They do not resolve the courier dispute, the hearing, the promised trust repair, a post-council career, or specific native diplomatic outcomes.
They mostly restate the route's established themes of letters and disagreement.
The normal committed endings require committed but not completion of ordinary or farewell, so final domestic conclusions can appear before those closing scenes were played.
That may be an intentional fallback, but it needs a visibly unfinished alternative or stronger culmination gate before the ending is presented as earned completion.

True Aeon's impression of a forgotten ordinary day is an authored poetic possibility, not established native Konomi memory behavior.
Keep it explicitly bounded as this expansion's chosen ending treatment.
Also verify ending selection against death, sacrifice, permanent departure, and incompatible future states before approving sentences that assume ongoing shared rooms or correspondence.
This pass establishes that no Konomi-specific conditions for those outcomes appear on the ending objects; it does not claim that every engine-level ending check is absent.

## Proposed expansion work in order

1. Add the native-history and contact predicates needed for ordinary Chapter 3 entry, Chapter 5 late entry, council changes, and attainable Trickster contact.
2. Expand the courtship with two or more played activities that establish specific private tastes, mutual attraction, and remembered outcomes.
3. Turn leak and reckoning into a political sequence with different public and discreet follow-through, a hearing or negotiation, and a lasting cost.
4. Add a disagreement that remains unresolved by a convenient third source of supplies, with later proof that affection survives it.
5. Build Chapter 4 letters around concrete fear or wonder disclosures and give those choices distinct return conversations.
6. Give Chapter 5 a substantial Konomi-led career and loyalty decision tied to the actual state of Mendev, followed by the promised trust test where applicable.
7. Write a concrete shared-future plan and consummation or nonsexual intimacy appropriate to that branch, then close with an outcome-specific farewell and epilogue.

These additions should supply the missing distinct-word depth through events and consequences.
They should not be split into many nearly identical nodes merely to reach the word floor.

## Approval status

Assembly consistency passes for the inspected artifacts.
The existing short arc has recognizable voice, voluntary courtship, and a useful political premise.
Length, sustained political consequences, native-outcome reactivity, and attainable Trickster contact do not pass the full campaign requirement.
Late-entry differentiation remains a proposed improvement, while council-specific continuity requires the native-state verification described above.
No full-route score or release approval is assigned while those required parts remain unwritten or unimplemented.
The prior bounded canon score remains evidence about the smaller text revision it reviewed, not evidence that this larger scope is complete.

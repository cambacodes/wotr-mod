# Jerribeth consequences: development handoff

Delivered `storylines/jerribeth_consequences.py` contains five connected scenes and 49 nodes.
This is a contribution to the incomplete Jerribeth campaign, not a complete 21,000-word route or a quality approval.
I edited only that new module and this handoff.
No shared exporter, existing storyline, production engine, permanent test or installed mod was changed.

## Revisions

| Input or delivery | SHA-256 |
| --- | --- |
| New `storylines/jerribeth_consequences.py` | `35C43858142B5D9BF5E4296462F99EE9C267BC33F7208CEB734B2AF41C217362` |
| Existing `storylines/jerribeth.py` read | `F607D73B030A2640A809081E53022938E62FF3FEBA4C66001BC485AC41FDD03B` |
| `story_format.py` read | `DB40D2075A4FD12BC2DFE1F97837AD0A501DE45FA2C7F56443488BD422BB6063` |
| Retained `reference/canon-review/jerribeth.txt` | `B36211563435BF63F3B72CFA57BD67927270F5EC75313A3E78C809184B8155F8` |

## Integration and progression

The parent can import `jerribeth_consequences` in `expansion.py` and extend the payload with `jerribeth_consequences.SCENES` after the existing Jerribeth module.
No new native GUID binding is required.
All scenes use the existing Jerribeth relationship, remote-book mechanism, portrait key, Drezen/Nexus areas and chapters 3, 4 or 5.
Every scene requires `jerribeth.commission` and `jerribeth.terms`, forbids `jerribeth.farewell`, and is optional.
The existing relationship's `jerribeth.unavailable` and closure handling still apply through production rules.

| Scene ID suffix | Additional requirements | Delay | Main new state |
| --- | --- | ---: | --- |
| `offered_signature` | None | 24 hours | `offer_performance` or `offer_design`; `counteroffer_sent` |
| `borrowed_sun` | `offered_signature`, `wintersun_known` | 24 hours | `sun_uninhabited` or `sun_exposed`; judgment choice and `sun_reworked`, or closure |
| `small_print` | `counteroffer_sent` | 48 hours | `sale_corrected` or `sale_withdrawn`; `sale_terms_set` |
| `unsold_evening` | `sale_terms_set`, `lovers` | 24 hours | Chosen frame/form/intimacy flags; `unsold_evening_kept` |
| `purchaser_answer` | `unsold_evening_kept` | 48 hours | `consequence_values_action` or `consequence_keeps_questions`; `consequences_kept` |

All flag names in the table have the `jerribeth.` prefix.
Scene completion and timestamp flags follow the existing authoring/engine convention.
The branch list in the actual module is authoritative; the table summarizes the causal milestones.
The optional Wintersun scene is not required to advance the purchaser chain, so lack of its native knowledge flag cannot strand the route.

The existing `future` scene still requires only the old commission milestone and can run independently when chapter five permits it.
These optional additions are therefore skippable and may become unavailable once the old farewell is played.
If the parent wants this arc to become a required part of the full campaign, it must deliberately revise the old future prerequisites and its campaign tests.
I did not silently create that dependency in an existing module.

## Dramatic scope and canon boundary

Jerribeth receives an authored offer to sell work associated with the Commander's private company.
She wants the payment and the prestige, recognizes the purchaser's attempt to buy implied access, and initially preserves a convenient ambiguity in her own reply.
The player chooses the work offered, challenges that ambiguity, and chooses a corrected sale or withdrawal.
The later answer and display remember those choices, including the financial disappointment of withdrawal.
Her keeping the agreement is a particular decision made against a temptation she still enjoys, not a conversion to benevolence.

The wealthy widow, offers, papers, payments, entertainments and resulting private dispute are authored events presented in book dialogue.
They do not create inventory items, transfer currency, send messages outside the game, grant a quest reward or change a native patron relationship.
The purchaser remains unnamed and is not passed off as Vellexia or another native NPC.
No native promise concerning her safety, rank or allegiance is made.

The optional Wintersun study uses only the already bound `jerribeth.wintersun_known` knowledge.
The retained native cue `b2997124f3662e147a029a6f73e13468`, `World/Dialogs/c3/Wintersun/JerribethReveal/Cue_0011.jbp`, supplies her admission concerning travelers killed by the deceived clan.
The same retained dialogue's cues `063d159af56b4c54292e6e2eaca8ca08` and `a657282ab833f5c42ac531d87908c9de` describe the inverted perception and her interest in the domain as an amusement.
The scene reacts to the known deception by changing a newly authored miniature construction.
It does not claim the village is now freed, the deception still operates, a victim is alive or dead, or that modifying an artwork repairs any native consequence.

Ivory Sanctum dialogue in the retained reference establishes her resentment of displaced authority, willingness to trade assistance, interest in Xanthir as a specimen and enjoyment of more elaborate pleasures than indiscriminate slaughter.
Those qualities inform her behavior here, without asserting a particular Ivory Sanctum deal or Xanthir outcome.
Marhevok, Orso, Soana and Vellexia receive no new outcome claims because this module does not have verified outcome predicates for their individual branches.
Their absence is deliberate; they should not be inserted as living visitors or resolved victims from name recognition alone.

The intimate scene uses the established charm's image and spoken-thought channel.
The participants remain physically separate.
The player can remain at the frame, request her own form or an explicitly invented adult guise, choose spoken anticipation of a kiss, continue shared private imaginings, or turn toward quieter conversation.
No tactile transmission, teleportation, native encounter restoration or magically compelled attraction is introduced.
The new invented guise has no supplied matching artwork and does not claim to reuse a canonical face.
All nodes currently use the existing Jerribeth portrait key, so final portrait choice needs independent visual review.

No new lover or commitment stage is granted.
The chain begins after the existing commission, whose valid progression already follows the old lover-stage evening.
Other relationships are not cleared or treated as an offense.
The dialogue accepts the Commander's limited time without asking for another partner's affection to disappear.
Live ToyBox behavior remains unverified.

## Bounded verification and volume

I imported the module with Python bytecode writes disabled and checked unique new scene IDs against the existing Jerribeth IDs, valid local node targets, speaker names, remote relationship metadata and Jerribeth-only choice writes.
An ephemeral branch walker evaluated choice requirements, applied choice flags, followed every reachable node, rejected cycles and dead ends, and checked that postponement paths add no progress flags.
It reached all 49 nodes after the independent writing-review revisions.
It enumerated 544 completed branch paths without the optional Wintersun scene and 3,808 with it, excluding explicit relationship closures from continued traversal.
The model preserved a seeded Seelah commitment and never granted Jerribeth commitment or unavailable state.
This is authored-graph verification, not execution of production C# rules, actual assemblies or a game save.

Using the agreed Unicode tokenizer and counting prose plus choices, this revision contains 5,240 raw words and 5,220 exact normalized-segment words.
On the enumerated completed paths, counting encountered node prose and selected choice text rather than every alternative, the main chain ranges from 2,392 to 2,894 words.
Including the optional Wintersun scene gives 2,921 to 3,558 words.
Those path counts do not count all visible unselected answers and do not certify meaningfulness or narrative quality.
Neither aggregate alternatives nor this contribution satisfy the full 21,000-word per-character requirement.

Parent integration tests should exercise the real `Rules.Available` delay boundaries, missing commission/terms/knowledge flags, native unavailability and closure, both allowed areas, chapter limits and farewell suppression.
Walk both offer types through both sale outcomes, including every intimacy and quiet branch, then verify the final purchaser callback.
Verify the optional Wintersun closure stops later content while absence of Wintersun knowledge merely hides that scene.
Check no choice writes native-history aliases, another relationship's state, commitment or an actor-restoration flag.
Run the existing real-assembly graph construction and native-binding checks on the resulting export.

Independent writing, canon and technical review rotation is still required.
No discipline receives a self-awarded score here, and the target above 90 is not a promise of approval.
The full route remains below its content floor, with bespoke attainable Trickster recovery, route restrictions, final art, actual contact/save behavior and live engine/ToyBox verification outside this delivery.

## Displayed-work continuity correction

Independent canon review found that the purchaser scene's common ending restored a bowl and platter that the sold-design branch had never displayed.
It also found that withdrawal always displayed the banquet regardless of the earlier design choice.
The revised withdrawal now selects `kept_performance` or `kept_design` from the original offer flags.
The final common conversation then selects `end_performance` or `end_design` from those same flags.
The design remains the room with painted doors and a visible real exit, while the performance remains the quarrelling dishes.
I walked all four offer-type/sale-outcome combinations and asserted that no design path contains bowl or platter prose and no performance path enters the painted-door ending.
The scene still reaches `consequences_kept` through either final node and introduces no new state flag.
At that correction revision, the 224 and 896 completed branch-path totals remained unchanged because those added nodes were conditional continuations rather than new player alternatives.
Independent reassessment of the corrected source remains pending.

## Independent writing-review revisions

The independent writing report assessed the preceding revision at 88/100 and identified four corrections.
The new revision does not inherit a higher score; independent rereview is required.

The unsold evening's joke now concerns waiting for the Commander's answer, rather than assuming the Commander sat in a chair on the frame-only path.
Jerribeth actually delivers the observation about treating enjoyment as an expenditure requiring a council's approval.
The player can answer with a teasing demand for more company, enjoy her attention, or object that being busy is not a judgment of her.
The two appended response nodes let her answer the enjoyment or objection before rejoining.
The old summarized compliment and first impression are now a spoken exchange about watching her choose a remark, her pause when she has none prepared, and the expectation of having to bring something useful.

The purchaser's common conclusion now clears the place where the display had stood, before the existing work-specific nodes restore it.
It no longer looks toward an object the preceding temptation node removed.

The Wintersun scene adds an interested study option and an unacquitting response that recognizes the appeal of her power without treating its victims as fictional.
That response reaches an appended `power_reply` node: Jerribeth welcomes the interest, the Commander explicitly withholds permission to use their mind as the demonstration, and they examine the constructed model instead.
New flags are `jerribeth.sun_studies_power` and `jerribeth.sun_power_interest`.
These record the chosen stance only and grant no native power, victim outcome or relationship stage.
The shared account no longer forces every interested player to deliver the same moral correction.
Existing condemnation, reserved judgment and departure choices remain available in their original positions.

I compared the serialized scene/node/choice structure with the pre-edit revision.
All existing scene IDs and indices, node IDs and indices, and original choice target/effect positions are unchanged.
New choices and nodes are appended within their respective lists; no existing entry was inserted before or reordered.
The graph walker still reaches every node, preserves another commitment, rejects dead ends and cycles, and verifies that the displayed-work correction remains effective on design paths.
These author checks do not replace root integration tests or independent quality review.

## Parent integration correction

Final parent-integrated source SHA256: `F91B1B0CA826F19B6A0077CBF069DABF6B6D40F98CBAACB08146FF91EBB3DB71`.
Earlier inventory and traversal figures above describe the author handoff before parent corrections.
The disputed-joke response now studies the Commander without referring to a room removed on the frame branch.

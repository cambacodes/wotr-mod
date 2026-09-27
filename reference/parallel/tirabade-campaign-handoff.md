# Tirabade campaign contribution handoff

## Delivered scope and ownership

This is a new authored contribution for independent review, not a completed or release-approved Tirabade route.
I changed only storylines/tirabade_campaign.py and this handoff.
The parent owns expansion.py, all existing story modules, production tests, exports, and integration.
No Story.json was generated, no installed mod was altered, and no agents were spawned.
The draft uses the existing story_format helpers and requires no new dependency or engine schema.
No writing score is self-assigned.
The user's 42,000 meaningful combined-word requirement and separate depth for both women remain unmet by this contribution.
Shared passages must not be counted twice as individual Anevia and Irabeth content.

Final new-module SHA256: `5D3E8405CC192236CEE796B623730814622057C66F830506A011F3D2CEAF696E`.
The six-scene inventory is 7265 raw prose-and-choice words and 7205 normalized distinct-segment words.
It contains 6487 prose words and 778 choice-label words.
These are aggregate inventory figures, including alternative branches, not an attainable-playthrough claim or quality evidence.

## Narrative content

The opening afternoon at an authored civilian ninepins yard lets Irabeth want a small competitive success and Anevia enjoy a skill that has no military purpose.
The Commander can choose a technique and either request coaching or ask to make independent mistakes.
Those choices alter the next match's actual exchanges and roll description.

The match ends with an ambiguous foot-fault complaint.
The keeper did not see a foul and upholds the score, but permits a fresh roll if both teams agree.
Irabeth prefers a replay because she fears opponents feel unable to object to the Commander.
Anevia prefers the existing decision because an unsupported objection should not void her score.
Both state that they can accept the other outcome before asking the Commander to decide.
Standing by the decision wins the match and pennant but loses the shared celebratory drink when an opponent leaves.
Replaying loses the match after an explicitly observed legal roll and disappoints Anevia.
Neither choice closes the relationship or awards a hidden virtue point.

Irabeth then has a separate conversation about her wish to be good at something that nobody needs from her.
She admits that wanting an uncomplicated afternoon led her to make the last roll carry her own concerns about rank.
The Commander can describe enjoying a team or wanting her particular romantic attention.
Both responses receive later payoffs at the return game.
An optional kiss or walk ends this individual scene.

Anevia's individual scene takes place at a bakery lesson with an invented older adult baker, Dalia.
The scene plays the sticky dough, waiting, shaping, and first loaf rather than summarizing a hobby.
During the pauses, Anevia explains the selected match outcome's particular hurt without asking the Commander to judge her marriage.
The Commander can stand by the decision or admit hurrying to stop an argument.
The scene ends with all three tasting the loaf and Irabeth giving an affectionate but specific response.
Anevia explicitly preserves the native future dream of her own kitchen and peaceful morning with Beth, describing this borrowed-oven lesson as practice.

The return game requires both individual scenes.
The keeper and both teams agree on a more visible boundary and an alternating watcher.
The original dispute remains unresolved as a historical fact, while the recorded result remains unchanged.
The opponent who left acknowledges that discourtesy on the winning history.
On the losing history, Irabeth owns having requested the replay without asking Anevia to apologize for it.
The team loses the new match on skill rather than another dispute.
Both wives still enjoy the game and the shared drink afterward.
This scene pays off the earlier choice, the Commander's desire from Irabeth's conversation, and Anevia's bread lesson.

The final evening uses an ordinary traveler's sketch to explore Irabeth's wish to visit a garden, Anevia's wish to browse a market, and the Commander's chosen water or street destination.
The garden and market preferences are authored inventions, not native facts.
The couple's shared travel plan accommodates the Commander without replacing either wife's wish.
This is planning for a future they cannot schedule, not a magically completed holiday or a new epilogue.
The player can stay for a graphic and explicit intimate night, choose quiet company and depart, or keep a separate later promise.
The last option plays out the agreed departure without jealousy or a demand to abandon another attachment.

## Exact integration point

Add tirabade_campaign to the explicit storylines imports in expansion.py.
Append or extend the existing payload Scenes with tirabade_campaign.SCENES at the same level as tirabade_later.SCENES.
No changes to story.py or tirabade_later.py are required by the new module.
All six IDs are new and were checked against the current development export for collisions.
Relationship is tirabade throughout.
Together entries attach through the two existing native dialogue roots; the individual entries attach through the corresponding woman's existing root.
No new native actor, AnswerList, etude, or resource flag is needed for the invented supporting characters.
Their presence exists in narrated book scenes only.
The pennant, bread, balls, map, fees, and prizes are narrative props, not inventory items or transactions.

Common prerequisites are three_outing.kept and kept_terms.
Every scene allows Chapters 3 and 5 in Drezen area 2570015799edf594daf2f076f2f975d8.
Every scene explicitly forbids closed, loss, inhuman, irabeth_away, anevia_away, and last_watch.
Existing relationship-level death, gone, Swarm, and true-Lich restrictions must remain active.
No romance-count, Commander-gender, jealousy, or other-romance-closing condition is introduced.

| Scene ID | Owner | Additional prerequisites | Delay hours | Terminal progress flag |
| --- | --- | --- | ---: | --- |
| three_yard | Together | None | 48 | three_yard.booked |
| three_match | Together | three_yard.booked | 48 | three_match.finished |
| three_beth_score | Irabeth | three_match.finished | 24 | three_beth_score.heard |
| three_anevia_flour | Anevia | three_match.finished | 24 | three_anevia_flour.baked |
| three_return_game | Together | three_beth_score.heard and three_anevia_flour.baked | 48 | three_return_game.kept |
| three_small_journeys | Together | three_return_game.kept | 48 | three_small_journeys.kept |

The two individual scenes deliberately work in either order.
Do not serialize one behind the other during integration.
DelayHours uses the existing engine prerequisite timestamps; no dialogue promises that the next separate scene happens immediately or tomorrow.
Scene completion also records each scene ID through the established engine behavior.

## Branch flag dependencies

| Flags | Written at | Read or paid off at |
| --- | --- | --- |
| three_yard.straight / three_yard.bank | First practice | Match technique nodes |
| three_yard.own_roll / three_yard.coaches | Team agreement | Match advice or independent setup |
| three_match.stood / three_match.replayed | Disputed throw decision | Anevia's distinct aftermath |
| three_match.pennant | Standing by the keeper | Irabeth's aftermath and return-game result history |
| three_beth_score.team / three_beth_score.noticed | Individual desire | Return-game team or mutual attraction exchange |
| three_beth_score.kissed | Optional Irabeth kiss | Records history only; no unimplemented payoff credited |
| three_anevia_flour.same / three_anevia_flour.quick | Commander's account of the decision | Immediate differentiated response only |
| three_small_journeys.water / three_small_journeys.street | Travel preference | Immediate map scene; later travel remains unwritten |
| three_small_journeys.garden_first / three_small_journeys.market_first | Order preference | Immediate wife-specific answer and map marking |
| three_small_journeys.night / three_small_journeys.quiet / three_small_journeys.later_promise | Final evening | Mutually exclusive played conclusion |

The base romance's committed, closed, other_loves, and relationship-management flags are not set or cleared here.
The later-promise choice is available regardless of whether other_loves was selected earlier, because other appointments can also matter.

## Canon and existing-route references

I read reference/canon-dialogue.txt rather than inventing native dialogue.
World/Dialogs/NPC_Common/Anevia/Cue_0001.jbp describes her observant threat awareness and her recovered ability to run, jump, or dance after the initial injury.
The new civilian game does not impose a permanent limp or use her injury as a joke.
Cue_0011.jbp establishes the childhood lockpicks and criminal environment, supporting her practical, irreverent skill rather than making her a generic flirt.
Cue_0077.jbp establishes her desire for a home oven and learning to bake after the war.
Cue_0084.jbp ties bread to the hidden Desnan temple and her happiest early memories.
Cue_0085.jbp explains the sustaining power of that memory during dangerous work.
Cue_0086.jbp and Cue_2.jbp associate baking at home and feeding Irabeth with eventual peace.
The wartime lesson is deliberately new development and needs canon review for whether it anticipates that dream too far.
It does not claim to be the promised first peaceful morning or remove the later native conversation.

World/Dialogs/c6/ThresholdExterior/IrabethAnevia_Threshold/Cue_0015.jbp establishes Anevia's wish to take Irabeth on vacation.
Cue_0016.jbp supplies Irabeth's laughing acceptance in one native outcome.
Cue_0017.jbp supplies a much more doubtful answer in another outcome.
The new module must not be treated as healing or overwriting that native morale distinction.
The garden, market, game, private teaching, and specific romantic encounters are authored additions.
No invented acquaintance is presented as a native quest NPC.

I also read the initial Tirabade findings in reviews/story.md and the retroactive inventory and attribution concerns in reference/art-review/existing-route-readiness.md.
This contribution responds with an event that permits disagreement to persist, a change in how the next event is conducted, two individual desires, and played activities beyond narrated reassurance.
Whether those changes succeed is for the independent reviewers.

| Referenced source | SHA256 |
| --- | --- |
| story.py | `5E8B5914C6CD47841C4CD4D899D90BBF06C14A948702E8BDBC46BE7EF91788F1` |
| storylines/tirabade_later.py | `B156DD2AC269B8C8B32CAE3354B01A51F276FA8DD483513364BC080E1CD647DE` |
| reference/canon-dialogue.txt | `E10DD05FA5D08FF7AFD3DB4700433EDD65160F46D6FDC69DA3BCD4131ED2AE2B` |

## Local checks completed

Parsed the module as Python and executed its authoring declarations without invoking the export builder.
Checked unique scene and node IDs, valid Next targets, balanced narration tags, and absence of em dashes.
Traversed both orders of the wife-specific scenes with choice predicates and carried flags.
Each ordering reached 768 distinct completed flag states.
All 92 authored choice edges were encountered, including abort choices.
Successful paths always contained exactly one disputed-match choice and one final-evening choice.
The graph has no branch dead ends under these supplied prerequisites.
These are local authoring checks, not the production C# fixture, a native game replay, or a visual inspection.
The final tiny edits attribute Tessa's rule explanation explicitly and specify that the new foul watcher judges feet before release.
They do not alter the checked graph.

## Production tests and independent review still required

The parent should run the actual assembly and C# rule checks after integration.
Verify the first entry is unavailable before three_outing.kept and kept_terms and that each progress flag unlocks only its intended successor.
Exercise both orders of individual scenes with the actual engine timestamp calculation.
Verify Chapter 4, other areas, either spouse away or dead or gone, closed relationship, inhuman state, and last_watch prevent these bodily shared scenes.
Verify Chapter 3 and Chapter 5 positive cases without creating native actors.
Exercise both disputed-match histories through both individual scenes and the return game, checking that the pennant is never invented on a losing history.
Exercise straight and bank rolls, coaching and independent turns, both Irabeth desires, and every final-night alternative.
Check that quiet and later-promise choices do not set the night flag and that no branch closes another romance.
Validate save/reload within the two independent aftermath scenes and between them and the return game.
Check narration, portraits, dialogue attachment, and page length in the actual book UI.

Independent literary review should challenge whether the match disagreement feels proportionate, whether the voices remain distinct over this length, and whether the individual scenes deepen the marriage instead of making the Commander its therapist.
Canon review should specifically examine the bread-dream timing and Irabeth's variable Chapter 5 morale.
Art is not supplied; the yard, bakery, and shared-map scenes need reviewed visual concepts and final crops if commissioned for release.
The current inhuman restriction does not certify every possible alternate body state, including dragon-form presentation.
This module supplies no death recovery, departure restoration, or bespoke Trickster access.
Those remain separate full-route requirements, as do the missing campaign depth and volume beyond this contribution.

## Parent integration correction

Final parent-integrated source SHA256: `498A293C625584EB47AAABBCAB4DC28ED2EC89AF7BDBB23CF7B7BF092371E5DC`.
Earlier inventory and traversal figures above describe the author handoff before parent corrections.
The lesson now acknowledges earlier baking instead of claiming her first loaf.
An optional burned-crust callback requires the actual earlier `a_errand` history.
The baker is Dalia and the straightedge remains the one Irabeth brought.
The Commander can now sincerely reconsider either match decision without confessing haste; each response preserves Anevia's own judgment.
The slate has one score column for each named player.

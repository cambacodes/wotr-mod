# Areelu prose and ambition revision

The source is `storylines/areelu_trickster_rivalry_opening.py`.
The reviewed starting point for this revision was the root ending-state repair, SHA-256 `74C2F6B2BCCF23CAEEBD0BBD7FB00FE8247414758DF396786559802FEA27C0AD`.
The revised source SHA-256 is `AE390C939E2488D554A551843C3D9EDFC98E34020A5D5B2009BFF66DBB5ABCA7`.
There are 14 unintegrated scenes and 167 nodes.
This is an author development record, not independent approval.

## Changes

Player-facing narration, dialogue and answers no longer mention native script, authored continuity, cue asset identifiers, ToyBox, saved-game flags or a skill check as a production mechanism.
The opening now describes the separate sending crystal and the agreed adult biography in-world.
The explicit alternate-continuity disclosure remains in the non-dialogue route contract.
The original graft and its failed restoration remain part of the history.
Romantic dialogue addresses two unrelated adults and does not use the lost child as an intimate comparison.

The ending now speaks about letters, private meetings and separation instead of route states and campaign completion.
The shared commitment passage no longer automatically narrates a kiss after the player chose words without a kiss.
Areelu's commitment response emphasizes her independent work, disagreement, locked doors and refusal to be reorganized by a lover.

A successful Trickster gate closure enables a new dispute about who may use the resulting knowledge.
The Commander can propose a private research monopoly, restrict teaching to avoid dangerous imitation, or invite outside scholars to submit proposals.
Areelu negotiates an equal share of a patron's price and retains the ability to refuse her work.
The monopoly choice records `private_research_pact`, `research_price_shared` and `method_withheld`.
It leaves the residents' promised measurements with them, while the observer publicly records Areelu's refusal to teach the method.
This is a self-interested bargain with acknowledged coercive potential toward future petitioners, not a redemption reward.

The pact unlocks a separate later power-partnership conversation through a real `Requires` predicate.
The conversation is unavailable without the earlier bargain and is forbidden after a breakup or pause.
Accepting its relationship terms records `power_partnership_terms` before the ordinary commitment decision.
The player may instead keep the work arrangement and decline lasting romance.
The promise to disclose future patrons' prices has no later patron encounter or runtime enforcement yet.
No income, dominion or external NPC response is claimed to have been implemented.

A shared field-report paragraph previously contradicted the supported private-report answer by naming the Commander publicly regardless of that answer.
It now distinguishes a public name from identification retained in the sealed witness copy.
The public record remains a narrative contract, not a game archive binding.

## Local verification

`py -m storylines.areelu_trickster_rivalry_opening` passes and reports 14 scenes with 167 nodes.
`py -m py_compile storylines/areelu_trickster_rivalry_opening.py` passes.
The final-outcome traversal now includes combinations with and without the private pact and with and without historical commitment.
It preserves the root checks for exactly one available final outcome, all four final outcomes reachable, and a closed future after the year-end breakup.
The survey-station scene remains `Remote=False`.
Added assertions check the bargain's successful-Trickster-closure requirement and the later pact callback's missing-pact and ended-relationship rejection.
An AST-based scan of actual node and choice strings found no remaining native/authored/ToyBox/cue/c5/branch/saved-game/skill-check/scene/player production phrases.
That scan is a narrow lexical check, not an independent assessment of voice or immersion.

## Selected-path measurement

A local graph solver using the tokenizer from `tools/measure-story-content.py` finds a compatible committed path of 25,883 selected words.
The same path includes the private research pact and the later power-partnership terms.
The starting fixture supplies `entry_ready`, `active_trickster_path`, `cradle_memory_record_verified` and `cradle_memory_answer_available`.
Those inputs are assumed contracts for future runtime and native-history readers, not facts produced by the manuscript.
The solver carries flags across all fourteen scenes, enforces scene and choice requirements and forbids, considers both check outcomes, rejects abort choices and rejects closed, ended or paused relationships.
It retains only flags that influence later predicates or the required final outcome, avoiding incompatible sums of independent scene maxima.
The accepted final state requires `relationship_committed`, `route_record_sealed` and `ordinary_future_chosen`.

| Scene | Selected words |
| --- | ---: |
| The original is not a footnote | 1,194 |
| A joke with a consequence | 1,244 |
| A flaw in the margin | 749 |
| A fold with teeth | 1,283 |
| What the work made possible | 691 |
| The witness who does not forgive | 785 |
| A future that is not a replacement | 723 |
| What she asks for | 847 |
| The answer belongs to more than you | 772 |
| The account leaves the archive | 3,656 |
| The line on the page | 3,774 |
| A limit chosen in public | 4,016 |
| The unmeasured answer | 2,256 |
| A life that does not answer for the past | 3,893 |
| Total | 25,883 |

The number exceeds the planning floor by 4,883 words on this modeled trajectory.
It does not establish that every paragraph is meaningful, that all trajectories reach the floor, or that the route is attainable in the game.
A different reviewer must reproduce the count and judge pacing, character voice and repetition.

## Remaining work

The long middle sections still contain extensive archive, correction and boundary discussions.
This revision does not claim to have cured every instance of a procedural or counseling register.
The new ambitious option strengthens the late arc but does not turn every earlier scene into a fully distinct evil trajectory.
The gate's shared downstream prose still describes conditional outcomes in places rather than selecting dedicated state-specific pages.
These deserve independent review and, where the reviewer finds a contradiction or pacing failure, further revision.

The route remains unregistered and lacks native readers, actor/location delivery, state writers, save/load proof, ToyBox verification and in-game portrait switching tests.
The art has not been assigned or certified by this revision.
No review scores or readiness claims are granted.

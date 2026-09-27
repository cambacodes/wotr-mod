# Nocticula current independent route review

Reviewed 2026-09-27.
I did not author or edit the reviewed manuscript, integration code or tests.
I read the current continuation, prior literary and integration reports, the parent-extension audit, the focused test, and relevant current export, Rules and Main implementation.
The unslop writing guidance applies to this report.

The continuation is a substantial, characterful investigation and romance, but it does not yet meet the selected-playthrough length requirement or the full acquisition and recovery scope.
Its 25,876 distinct aggregate words are not a 25,876-word playable route.
An independently traversed longest visit path contains 14,488 words.
Even giving that path every distinct word in the documented parent inventory and its longest compatible addon recollection produces only 20,775 words, below 21,000.
That is an intentionally generous upper bound, not earned parent credit.

## Pinned evidence

| Artifact | SHA-256 |
| --- | --- |
| `storylines/nocticula_continuation.py` | `81526DA3BCF6CD672E4F956B4F0BA84098C8E9BD787BD9AFBA6193728ED9DE02` |
| `development/Story.json` | `866B7C66C2027AFEE471FD4C497F57CD173E2AE789814FB268FC5DA49A9249C2` |
| `expansion.py` | `7A0A7E945D9E76AF0719C511C487D9C662387C02E076D7D870CA81F5B4B7BB56` |
| `src/Main.cs` | `40982E9F1556C044B5F1EE2CEFFC545C1713887DCBF25970A315A7AE0A00C48C` |
| `src/Story.cs` | `40759604CFF706419ADEB88C8FF6E9D91221E8C2C6ACA40EF65CA06149A0A736` |
| `tests/NocticulaContinuationTests.cs` | `3308F608E0D3E8D279B12E050A8A32A7100D6AAE5BD3FF5404CBF646A710EAD2` |
| `reference/canon-review/nocticula-parent-extension-audit.md` | `FFBDE6A7F210E89D393C4ACB15F83C1B006AD0FC87703621A095AEC86083A572` |

The source hash was unchanged when checked again after inspection.
The current export contains all 24 Nocticula scenes, and an imported-object comparison matches every source scene exactly.
There are sixteen visits with 120 nodes and eight one-node supplementary recollections, 128 nodes in total.
The source has 25,964 raw text-and-choice words and 25,876 words after exact normalized segment deduplication using `tools/measure-story-content.py`.

## Selected-playthrough measurement

I ran an independent graph solver over the sixteen visits.
It carries flags across scenes, enforces scene and choice predicates, considers both check outcomes, rejects aborted visits, and counts only visited prose and the chosen answers.
The initial fixture contains accepted parent activity, the actual-agreement witness alias, the Gift, Trickster and optional parent-history aliases.
All optional history aliases were enabled for this upper-bound calculation; their coexistence is not asserted as a native campaign witness.
Extra aliases only add relevant choices in this manuscript, so the fixture does not hide a longer option behind an absent optional flag.
The graph begins at each scene's first node, matching book construction; `Entry` here is the human-facing title, not a node identifier.

| Visit | Selected words on the longest compatible path |
| --- | ---: |
| `unlit_quay` | 706 |
| `sixth_passenger` | 670 |
| `lamp_measure` | 637 |
| `captains_reply` | 843 |
| `her_own_face` | 891 |
| `white_shoes` | 897 |
| `demonstration` | 945 |
| `voices_in_glass` | 894 |
| `cost_of_return` | 904 |
| `return_count` | 915 |
| `after_the_lamps` | 976 |
| `another_place` | 1,194 |
| `hearing` | 849 |
| `last_buyer` | 1,027 |
| `what_she_keeps` | 1,145 |
| `second_door` | 995 |
| Visits total | 14,488 |

The path includes failed ledger reading followed by bait, Teren's crossing, limited Trickster reinforcement, commissioned Ilvara after an uncertain hearing, and the final alliance choice.
Failures count as selected content where the route permits them; this is not a best-roll fantasy assembled from incompatible scene maxima.
The compatible alliance recollection adds 155 words, producing 14,643 new selected words.
The longest other recollections contain fewer words.
Repeated postponement of the first invitation is not fresh content and was not used to inflate the total.

The parent audit documents 6,132 distinct configured words across the entire parent Nocticula content, including mutually exclusive branches and endings.
It explicitly does not provide a selected-path credit ledger.
Giving all of that overinclusive amount to this addon trajectory yields 14,643 + 6,132 = 20,775, still 225 short.
The real shortfall will be larger once the actual compatible parent path and repeated or borrowed material are accounted for.
Even adding the separate 118-word Aeon recollection on top of the ordinary outcome, an intentionally overinclusive combination, would reach only 20,893.
Do not solve the requirement by attaching contradictory endings or counting optional branches the player cannot traverse together.

The earlier literary report's aggregate-volume finding remains accurate as an aggregate finding.
It cannot establish the current meaningful selected-route floor.
At least 6,357 more new selected words would be needed if the addon were required to meet 21,000 without any parent credit; an audited compatible parent contribution can reduce that amount.
The expansion should add substantive relationship or quest development, not stretch existing scenes to recover a number.

## Fresh graph and integration checks

I independently explored all 32 combinations of the five optional history aliases used by the focused suite.
The traversal carried state across the full visit sequence, merged only states indistinguishable to future predicates, and reached all 120 visit nodes and all 173 visit choice records.
It found no node without an available continuation on those modeled histories.
All three final decisions were reachable.
No choice writes any registered Etude alias, and the source uses no revival action.
The graph checks are Python source-model checks, not executions of C# Rules or native game conditions.

Python compilation passed.
I could not rerun the .NET 8 focused suite because `dotnet` is not available as a command in this review environment.
I inspected its code instead and do not claim the historical assertion totals as a new execution.
The existing C# suite checks delays, loss of parent prerequisites, chapter and area restrictions, dream contact, postponement, branch coverage and supplementary outcome precedence from seeded accepted histories.
It does not play the native acquisition or prove actual RNG, save loading or ToyBox behavior.

Current integration is ahead of the older final-integration report in two respects.
`Main.BuildScene` now sets ending pages' native `ShowOnce` property.
`Main.Build` now appends ordinary addon recollections to the optional Expanded Epilogue sequence when that sequence exists, while preserving the Aeon owner separately.
The managed test source has checks for those properties and optional-sequence attachment.
Those source changes resolve the old claims of missing configuration; they do not by themselves prove installed replay or third-party caller behavior.
The plain ending Continue still has no addon completion action, so the relevant production once-only protection is native page history, not the synthetic completion flag supplied by the Rules walker.

## Character, mature romance and meaningful choices

Nocticula retains concrete ambitions and recognizable impatience.
She wants the harbor, resents paying for the stronger rescue, investigates a loophole after accepting the limited solution and admits she would have used a secret second door.
She can want the Commander while disagreeing about the value of the Commander's advice.
These actions demonstrate resistance more convincingly than simply calling her dangerous.

The Gift exchange in `her_own_face/start` acknowledges that her real leverage remains.
She chooses to ask because she wants an answer worth hearing, while warning that a pleasant evening does not cancel the older bargain.
The route does not pretend that romance has abolished the Gift or made her benevolent.
The parent Worldwound bargain remains explicitly unsettled at `second_door/future`.

The Commander has meaningful morally different choices.
Examples include buying Dessa's lease or threatening the captain, sending a volunteer or coercing Ilvara, protecting Nocticula's secret at risk to the rescue, preserving a dangerous chart, and confining, employing or expelling Ilvara.
Her execution is absent from the offered advice because Nocticula has decided her knowledge is presently worth more, a reason grounded in her own interests.
The route does not need every conceivable cruelty in each menu to preserve evil agency.

Three Commander-only Knowledge: World checks use DC 30, 32 and 33.
Their failures change the account: loss of quiet investigation, extra supervision for Ilvara's unexplained defense if employed, and loss of the chance to answer Ossin privately.
The Trickster has specific commercial and magical interventions, including contradictory buyers, the seventh-berth inquiry, counted reinforcement and a limited auction.
These are authored developments with preparation and costs, not claims about existing native powers.

The repaired historical branch defects appear resolved in the current text.
The seventh line is now supplied in common `white_shoes/meeting` before the Trickster choice.
Teren is introduced in common `cost_of_return/start` even when Ilvara is the chosen carrier.
The hearing business branch no longer recalls an unchosen double-buyer plan.
The private night explains its own book anecdote instead of borrowing the talk-only branch's story.
The four hearing histories select separate commissioned-work reports in `what_she_keeps`.

The romance has specific physical and emotional scenes rather than only negotiations.
The dance, the deliberately imperfect dream room, a private night, the interpreter anecdote and the final exchange about the courtier convey attraction without graphic content.
`another_place/refused_dance` preserves the missed dance and her displeasure instead of praising the refusal or narrating the dance anyway.
`her_own_face/talk` keeps that evening conversational.
The recurring dreams still make much of the investigation secondhand reporting; more immediate shared activities would improve an expanded route.

## A remaining refusal gap

`unlit_quay/offer` says the Commander may decline, but its only nonacceptance answer is "Another evening. I want you tonight".
That leads to `later`, which postpones the undertaking and leaves it available again.
There is no permanent refusal of the undertaking without affirming a desire for her company that night.

After accepting the investigation, all sixteen visits lead forward; the module has no choice that sets its declared `noct.closed` flag.
The last `second_door/limited` choice declines a larger promise while explicitly retaining the older relationship.
That is a valid outcome, but it is not a breakup or withdrawal from the undertaking.
The inspected journal display reports a closed state; it does not provide a missing close action.

Add an explicit refusal at the first offer and an authored way to withdraw from the new undertaking later without silently rejecting or rewriting the parent romance.
Where a later private scene offers increased intimacy, a conversational alternative would give the existing relationship more texture than assuming every returning visit wants the same physical response.
This is a scope and agency gap, not a claim that every affectionate gesture needs a separate permission menu.

## Acquisition, compatibility and full-route limits

Every visit requires parent Active, an observed accepted agreement and the Profane Gift.
Every visit forbids death, parent rejection, addon closure, inhuman state, Legend and Gold Dragon, and is restricted to Chapter 5 Drezen.
The module therefore implements continuation for an already accepted eligible relationship.
It provides no entry after a missed or rejected parent opportunity, no Gift-loss renegotiation, no resurrection, no restored contact after death and no bespoke alternate acquisition.
The dialogue callback about Socothbenoth correctly requires its witness; it does not itself unlock romance.

The user's all-romances Trickster outcome also needs a living-Shamira political and quest resolution.
The parent audit identifies native death-dependent essence and political consequences.
This manuscript supplies no alternative quest producer and should not claim that its local Trickster harbor solution makes simultaneous Shamira completion attainable.
Other mythic restrictions remain explicit and should be compared with the latest approved route matrix rather than silently broadened through flag edits.

The module does not read other romance commitments as exclusions and does not write parent counters or native acceptance.
`another_place/others` explicitly accepts other lovers while preserving actual conflicts of interest.
Laulieh's participation and departure histories have separate callbacks; the addon does not grant or duplicate a new triad.
These are good static compatibility properties, not fresh tests with ToyBox Free Love and No Jealousy in the running game.
Potential Arueshalae group content already owned by the parent must remain integrated through its actual conditions.

All harbor actors and events are authored offscreen action conveyed through dreams.
The route does not currently create a playable harbor, spend Commander gold, add travel access or grant the pictured lens as an item.
The narrative makes several of those limits explicit.
That scope is coherent, but it must remain clear in delivery claims and any guide.

## Independent scores

These scores evaluate the actual inspected scope, without inheriting prior approval or averaging away a failure.

| Dimension | Score / 100 | Finding |
| --- | ---: | --- |
| Nocticula voice and character resistance | 94 | Ambition, appetite, irritation and opportunistic limits remain concrete. |
| Commander agency and morally distinct decisions | 93 | Rescue, coercion, secrecy, power and ownership choices have different narrated consequences. |
| Prose and mature graphic and explicit chemistry | 93 | Specific private scenes and sharp exchanges support sustained attraction. |
| Pacing and variety within the existing continuation | 91 | Good recurring objects and private variation, with a persistent reliance on reported investigation. |
| Local branch truth and conditional callbacks | 94 | Historical leaks are repaired; current carried-state exploration reaches every visit node and choice. |
| Refusal and withdrawal completeness | 86 | Postponement and a smaller final commitment exist, but permanent refusal and later withdrawal are absent. |
| Meaningful selected-playthrough length | 72 | New selected content is 14,643 including one ending; even the documented overinclusive parent ceiling leaves the route short. |
| Parent versus authored continuity | 94 | Existing acceptance, Gift, major bargain and authored dream incident remain distinct. |
| Continuation mechanics and authored consequences | 93 | Checks, crossing choice and later disposition reports provide meaningful local differences. |
| Complete Trickster acquisition and recovery | Unscored, missing | Current continuation cannot satisfy missed, rejected, Gift-loss, dead or concurrent living-Shamira histories. |
| Static nonexclusivity | 95 | No new exclusivity exclusion, specific other-lovers dialogue and preserved parent ownership. |
| Live ToyBox, save/load and ending delivery | Unscored | Source and synthetic policy checks do not supply installed runtime evidence. |
| Art and scene-specific presentation | Unscored here | Separate image reviews exist; universal general portrait use does not establish literal scene fidelity. |

## Required next work

Build a compatible parent-credit ledger and preserve its actual acquisition witness.
Expand with new selected content until every intended full route clears the meaningful floor; 225 words is only the smallest possible deficit under an unrealistically generous credit allowance.
Add permanent undertaking refusal and withdrawal while keeping parent ownership intact.
Develop the bespoke Trickster acquisition and recovery routes, including the living-Shamira alternative, before claiming universal availability.
Rerun the focused Rules and managed build checks in a supported environment, then verify real save persistence, native ending history, optional epilogue delivery and ToyBox concurrency.
The existing continuation is worth retaining, but this report does not approve it as a complete or manual-play-ready route.

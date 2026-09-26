# Konomi assembled readiness, 26 September 2026

Independent review of main277, SHA256 `070879FB0FF8AF03FAA0E1A9525FDD88AEC61E89912C853877782BAABA952230`.
I did not author Konomi's route or its ordinary expansion.
This review supersedes the obsolete depth findings in the 25 September assembled review where the intervening history, private hearing, political and ordinary additions address them.
It does not replace the separate technical reviews or approve a release.

Konomi now has substantial playable prose, a complete selected romantic progression in the principal retained-office and dismissed histories, and several decisions with subsequent consequences.
Calling her a short draft would be inaccurate.
Calling the complete campaign indistinguishable from the base game, or all-path RanRomance parity verified, would also be inaccurate.
The strongest improvement is the six-visit ordinary sequence, which turns an invitation to see her work into a played experiment, a disputed recommendation, an observed result, a career opportunity and an evening together.

## What I measured and read

The assembled inventory contains 54 Konomi scenes and 35,582 distinct aggregate words, including alternative routes and endings.
I read the assembled retained-office trajectory through its ending, the dismissed acquisition and continuation, the history repair and private hearing overlays, political branches and career-choice consequences.
I revisited the prior assembled review and the contribution reviews to distinguish repaired findings from remaining ones.
The reproducible source analysis is `tools/measure-konomi-playthrough.py`.
Run it normally for counts or with `--read-path ordinary_hearing_and_abyss` to inspect an actual selected longest trajectory.

The analysis carries choice flags forward and retains compatible minimum and maximum prefixes under the predicates needed by later scenes.
It counts only visited node prose and the chosen answer, using the project's existing tokenizer.
It does not sum mutually exclusive endings, ordinary and dismissed romances, both hearing deliveries, all answer buttons or every branch of a skill check.
Checks admit either outcome; the range is not a probability estimate.
All examples assume a living embodied Trickster, correct locations, sufficient waiting, and supplied native office or dismissal history.
Chapter transitions are checked explicitly: ordinary early visits in chapter three, its unsent letter in four, and late ordinary visits in five; the private examples depart in three and resume their correspondence in five.
Native political rank history is unspecified in these examples, so the political conversation uses its uncertainty branch.
These are source-predicate trajectories, not loaded-save or Unity execution proofs, and not exhaustive bounds over every political, public, ascended or transformed history.

| Selected committed trajectory | Words read, including selected answers and one ending |
| --- | ---: |
| Retained office, required progression including all six new visits | 8,707-9,415 |
| Retained office, also completing the hearing, new-letter outing and Abyss letter | 11,236-12,513 |
| Dismissed before courtship, private acquisition through committed future | 7,917-8,801 |
| Established lovers dismissed after reckoning, resolving the pending hearing privately | 12,753-14,305 |

The private examples include the optional manual political account.
Fresh dismissed courtship correctly skips `private_history`, because its meeting already sets the no-pending-grievance readiness flag.
The retained-office examples use the private ordinary ending, while the dismissed examples use the committed distance ending.
The established dismissed example earns its early ordinary history before the native dismissal fixture changes; it does not also play the later retained-office expansion.
The selected ordinary trajectory with every listed optional addition gives 5,338 words to the six new visits, versus 2,502 words to the original seven early visits on that same trajectory.
This is a pacing imbalance to consider, not a reason to pad the earlier scenes to an arbitrary total.

## RanRomance comparison

The installed-source inventory `reference/art-review/ran-route-word-inventory.json` attributes 19,004 keyed words and 18,359 distinct normalized-text words to Targona, the largest configured initializer.
Its other distinct totals are Nocticula 6,132, Nurah 14,101, Terendelev 14,827, Aranka 15,758 and Minagho 15,790.
The inventory traces actual initializer references in installed `RanRomance.dll`, SHA256 `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`, and records its loader limitations.
The installed readme and `reference/canon-review/targona-route-evidence.md`, with the linked decompiled parent bindings, establish a useful structural comparison: initial treatment, later check-up, chapter-four intervention, chapter-five finale, differing mythic outcomes and epilogues.

Konomi exceeds the project's 21,000-word aggregate planning floor.
That floor is separate from selected-playthrough length.
There is no verified selected Targona baseline here, so neither 21,000 nor 18,359 becomes a required selected Konomi count.
The Ran inventory also includes referenced journal/title material that the Konomi prose inventory excludes.
Aggregate size therefore supports substantial production effort but cannot establish equivalent player experience or writing quality.
Konomi still needs the functional campaign breadth and continuity discussed below before I would call RanRomance parity established.

## Character, romance and decisions

The retained-office opening has a convincing source of attraction: she corrects an inaccurate insult without withdrawing her own criticism, then becomes curious about the person she has been describing.
The failed plants, stolen letter, copyists' hearing and competitive market outing give that attraction objects and occasions beyond repeated declarations of trust.
The hearing is especially effective when the Commander previously suggested denying the letter and later acknowledges it before the adjudicators.
Her relief is earned through a changed action, and the original privacy injury is not erased by winning a finding.

The ordinary trial lets her prefer a plan, hear a neighbor's objection, resent being wrong and remain attracted to a Commander who disagrees.
Perception DC26 identifies the noisy plank promptly; failure consumes the available trial time and disturbs the upstairs household; a deliberate non-roll comparison also takes time.
Later unloading and publication choices lead to different played outcomes.
The romantic reward does not require agreeing with every recommendation or passing the die roll.
Those are appropriate mechanics for this character.
They affect authored circumstances, not native kingdom resources, placed merchant actors or actual money transactions.

The dismissed route preserves her appetite for influence.
Accepting work for the landlord costs the tenant's trust; delaying costs money and travel without guaranteeing gratitude.
Her statement that she does not intend to spend her life proving how little she needs is a particularly important protection against turning her into a humbled, harmless prize.
The impossible post office is a credible authored Trickster intervention into access, followed by an ordinary carrier and a voluntary answer.
It does not restore her council office or manufacture consent.

Romantic warmth is present and mature without graphic content.
Kisses interrupt irritation, private desire accompanies professional ambition, and the final ordinary evening supports either an intimate night or a separate walk home.
Other relationships are acknowledged through honest scheduling rather than jealousy penalties.
That supports the intended Free Love/No Jealousy design, while actual ToyBox coexistence remains a runtime question.

The dialogue still overuses a recognizable rhythm: she offers a precise correction, admits an inconvenient feeling, qualifies it with wit, and permits closeness.
Repeated suppers, folded papers, cups and statements that work can wait make some transitions feel interchangeable.
The early attraction is noticeably faster and less interactive than the late warehouse sequence.
Her political ambition is now stated and locally demonstrated, but the local cases mostly lead toward fairer practice after a reasonable objection.
A future scene should let her pursue a defensible, uncomfortable interest without obliging the Commander to improve her ethics each time.

## Remaining work with the greatest value

1. Give the private route a chapter-four absence and chapter-five reunion response that belong to its own history.
   A fresh dismissed romance cannot access `unsent`, which requires the ordinary `evening` scene.
   An established dismissed lover may write that letter, but its developed delivery is in retained-office `return`, not `private_reunion`.
   Use an undelivered letter or remembered shared incident, not an invented reliable Abyss courier.
   If the Commander has become Legend after the Trickster delivery, let Konomi notice the changed future without pretending the old post office still exists.
2. Play a later consequence of the private career decision, and give it a distinct pre-final-battle farewell.
   The current future choice makes a relationship plan and moves quickly toward the distance epilogue.
   Let the tenant or employer's subsequent answer test that plan, with a choice about time, reputation or a promised visit.
   Avoid repeating the ordinary wagon inspection in the private branch merely to equalize length.
3. Add one early reciprocal scene between interest and established intimacy.
   Let the Commander reveal a selectable personal preference or vulnerability and have Konomi respond specifically.
   The private reunion's sleeplessness/good-evening/quiet-company options already show how to do this.
   The ordinary final supper's summarized account of the Commander's day is less responsive.
4. Add one late political consequence tied to actual observed native history.
   The political account's crisis, domestic recovery, foreign intervention, council conclusion and earned-respect distinctions are useful context, but much remains an intention to ask better questions.
   A subsequent authored reply could make her choose between access and a position she wants to defend, without claiming to change an unimplemented native settlement.
   A smaller ordinary closing callback should acknowledge the selected trial/report outcome instead of returning immediately to the generic plant-and-papers scene.

These additions would improve campaign continuity, reciprocity and consequence more than another isolated romantic supper or a longer epilogue.
The completed history and private-hearing repairs should be retained; the old report's allegation that dismissal automatically drops the petition, leak or apology is now stale.

## Concrete copyediting finding

At this exact snapshot, 18 new ordinary nodes open their final spoken passage but omit its closing quotation mark.
They are `a_useful_supper/start`, `walk`, `needs`; `the_upper_passage/start`, `early_end`, `late_end`; `two_bad_prices/start`, `evening`; `the_trial_day/start`, `evening`, `evening_cost`, `morning_cost`; `a_name_beside_hers/time`, `joint`, `circular`; and `the_evening_she_kept/start`, `joint_reply`, `circular_reply`.
All scene IDs have the `konomi.` prefix.
This needs a source correction and regenerated export before the text is considered polished.
Odd quote counts in the separate multi-page letters need their boundaries inspected and should not receive a blanket balancing edit.
My initial automated candidate list also included `another_evening/start`; its reopened quotation represents the same speaker across paragraphs and is not an error.
After this snapshot, root corrected the 18 actual terminal quotations in source SHA256 `1B9BB511870320018A9949A6C8BCC8F391571C513AF55766F3AAE3054D8EF3E5`.
I independently compared every node from that module to main277: exactly those 18 texts append one closing double quotation mark, with all other node fields unchanged.
The correction does not change selected word counts or the depth assessment.

## Assessment and verification boundary

| Discipline, assembled content inspected | Score | Reason |
| --- | ---: | --- |
| Writing and dialogue | 89/100 | Strong individual scenes, with repetitive conversational cadence and the exact punctuation defect above. |
| Character likeness and credible authored development | 89/100 | Pride, ambition and disagreement survive; more politically uncomfortable follow-through would improve fidelity. |
| Mature voluntary romance | 91/100 | Desire and professional consequences coexist, with meaningful discretion, apology and intimacy choices. |
| Player participation and consequences | 87/100 | Genuine check/failure/non-roll and later choices work, but early scenes and some personal responses remain mainly reading. |
| Assembled campaign depth and pacing | 86/100 | Complete substantial selected arcs, uneven act distribution and a weaker private absence/finale. |

These are independent editorial judgments on inspected content, not statistical measurements, averaged release approval or promised future scores.
They do not contradict a contribution-level score above 90 for the six new ordinary visits: the full assembled campaign has a different scope.

The separate ordinary technical review independently passed 394,893 focused assertions and 12,617,780 complete rules for its candidate.
Root reports the combined main277 passing 13,013,025 rules and its managed blueprint checks.
Those checks support joins, old-save opt-in, interruption behavior and native-state preservation within their tested scopes.
This audit does not rerun them or claim they establish native actor availability.
Ordinary Konomi has no ContactUnit and inherits an office predicate; physical presence and external state changes during an open conversation remain separate concerns.
The dismissed route proves an authored Trickster acquisition mechanism for the specified living dismissal history, not every conceivable closed, absent, transformed or invalid native history.
Final art likeness, portrait presentation, loaded saves, native roll execution, localization layout and ToyBox behavior remain unapproved here.
Konomi is a substantial integrated route with identifiable finishing work, not a released full-parity character.

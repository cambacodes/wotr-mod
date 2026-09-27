# Nocticula further consequence arc

Seven connected visits now follow the last-buyer answer and precede the existing final private and future scenes.
The source is an author draft awaiting independent literary and mechanics review.
It is not approved for release, manual play review or TTS completion.

Frozen source SHA-256: `532A37F3DC2EEB30745CE84F085CC5F60E4C3F726BEA4BF7A9FFBAE434EC5763`.
Owned files are `storylines/nocticula_continuation.py` and this report.
No export, C# test, global planning, native binding or image file was edited for this task.

## What was added

The harbor affair attracts retaliation from a hunting-lodge hostess whose patrons lost money and prestige.
Her proposed entertainment uses substitutes to mock the returned passengers and threaten the people accepting Nocticula's protection.
The Commander and Nocticula plan an intervention using information from former staff, choose how to reach the enchanted hunting bell, hear what actually happened, and decide how to answer the surviving hostess.
The new people, lodge, bell mechanism and incidents are authored developments, not claims about native quests or unused game dialogue.

The Commander remains in the established dream framework.
Nocticula and her agents perform the physical intervention in Alushinyrra.
The remembered operation explicitly prevents the player from changing an already recorded moment by speaking to its image.
There is no new live actor, location, inventory reward or native quest completion represented by these flags.

The private evening between the operation and its judgment offers closeness, conversation without touch, or a refusal of that evening which preserves the investigation.
The refusal does not send the player into the intimate branch.
The longer scene explores Nocticula's habit of withholding facts, her interest in the Commander and the difference between wanting company and arranging obedience.
It does not promise to reform her through affection.

The lodge can close at a financial and political cost to Nocticula, or remain as a supervised source of protection and information under her authority.
The latter option deliberately gives her a new instrument of power and asks the Commander to own that choice.
Neither outcome treats Istrava as repentant or makes the escaped attendants into compulsory companions or informants.
This distinction is authored outcome text and addon history, not a change to the game's city simulation.

## Integration handoff

There are now 23 visits and eight existing endings, for 31 Nocticula scene definitions.
The prior focused C# expectation of 16 visits must change before the new export can pass its cardinality check.
The existing endings and parent bindings remain present.

| New scene | Required previous flag | Completion flag | Longest measured path contribution |
|---|---|---|---:|
| `noct.empty_chair` | `noct.buyer_answered` | `noct.lodge_proposed` | 1,292 |
| `noct.mask_and_bell` | `noct.lodge_proposed` | `noct.lodge_method_ready` | 851 |
| `noct.uninvited_guest` | `noct.lodge_method_ready` | `noct.lodge_hunt_ended` | 1,162 |
| `noct.closed_gallery` | `noct.lodge_hunt_ended` | `noct.lodge_answer_sent` | 1,077 |
| `noct.unborrowed_evening` | `noct.lodge_answer_sent` | `noct.lodge_evening_finished` | 1,169 |
| `noct.bell_without_master` | `noct.lodge_evening_finished` | `noct.lodge_judgment_finished` | 1,301 |
| `noct.no_applause` | `noct.lodge_judgment_finished` | `noct.lodge_consequences_finished` | 986 |

`noct.what_she_keeps` now requires `noct.lodge_consequences_finished` instead of `noct.buyer_answered`.
The existing final visit still requires `noct.ambition_discussed`.
Each new visit uses the existing twelve-hour interval, Chapter 5 and Drezen gates, parent acceptance and Gift requirements, and remote-contact rules.
The new sequence therefore introduces seven additional authored intervals rather than inventing years inside a single campaign rest.

The reviewed initial refusal and earlier withdrawal responses are retained.
`no_applause` joins `what_she_keeps` and `second_door` in the phase-aware late-withdrawal group, because its operation is already settled.
The other new visits retain undertaking withdrawal while the operation remains unresolved.
Both closure reasons still write only addon flags and prevent future addon visits and completion recollections.

The new checks use supported engine fields and skills:

- `mask_and_bell/start` uses `SkillUseMagicDevice`, DC 34, Commander only.
- `closed_gallery/start` uses `CheckDiplomacy`, DC 35, Commander only.

The first check has a silent-bell success and a guest-entry fallback after failure.
The direct guest entrance is available without a roll.
Trickster gains an authored public-announcement tactic which exposes the chamberlain through the hostess's own advertised rules, with intervention protecting the musicians who carry it out.
It does not claim that a joke magically overrides the bell's enchantment.

The method has a later consequence.
Silent preparation and the Trickster announcement avoid the initial marking; the guest approach ends the mark after it begins and leaves Rhez with a wounded arm.
`no_applause` reads those actual flags and supplies the corresponding agent follow-through.
The diplomacy failure produces overt intervention rather than the quiet leverage available on success.
Rescue and conquest priorities unlock different alternative approaches at that scene.
The reply to Istrava's private offer is read in `bell_without_master`, trading narrower information against broader names and a public accusation about the negotiation.

## Length evidence

Using the repository's `words()` counter, a source traversal across all 32 combinations of the existing optional-history fixtures measured complete paths with exactly one eligible ordinary ending.
The fixtures seed the accepted living parent relationship and retained Gift.
They assume the correct location and chapter and enough time between visits.
They do not demonstrate acquisition of those facts in Unity.

| Measure | Selected words |
|---|---:|
| Shortest measured complete path | 20,141 |
| Longest measured complete path | 22,481 |
| New arc within the shortest full-path witness | 6,996 |
| New arc within the longest full-path witness | 7,838 |

The longest full-path figure corresponds to the prior 14,643-word maximum plus 7,838 newly selected words.
No native or RanRomance parent text is credited.
The figures include visited prose and selected answers once, and do not add incompatible branch maxima together.
Shared withdrawal responses are excluded because the measured paths complete the undertaking rather than withdraw.

The new arc contains 11,248 aggregate words after excluding shared withdrawal nodes and their entry answers.
That inventory number is not a playthrough length.
Its aggregate including those repeated closure provisions is 12,303 words and must not be substituted for the selected figures.

The shortest complete path remains 859 words below 21,000.
Therefore this draft does not meet a requirement that every completed route variant exceed that floor.
The shorter optional private-evening refusal remains legitimate and must not be padded with compulsory intimacy to improve the count.
Further shared consequence material, and an independent assessment of meaningful length, remain necessary.

## Checks performed

Python compilation passed.
Scene IDs and local node IDs are unique.
Whitespace checks passed for the owned source.

The source traversal used the existing predicate helper and word counter, traversed both outcomes of checks, excluded postponement and closure from completed trajectories, and retained minimum and maximum played prefixes for states equivalent under future predicates.
It covered all 32 combinations of Trickster, the two Laulieh history flags, parent ambition and the Socothbenoth plan exposure.
Across those fixtures, all 185 visit nodes and all 277 visit choices were reached.
No visited page lacked a selectable answer, and no local path cycled.

The traversal examined 65,888 reached closure outcomes across the retained states.
Each lacked `noct.complete`, wrote no native or parent binding, and admitted no later visit or supplementary ending under the source predicates.
The count represents repeated state coverage, not distinct scenes or player choices.

The root owns C# test updates, fresh export generation and runtime integration verification after this handoff.
This task did not run the full C# suite on a regenerated export and did not run Unity or ToyBox.
Prior passing export assertions do not certify this new draft.

## Review and remaining scope

Independent reviewers should examine the hostess's causal connection to the harbor affair, Nocticula's motives for preserving witnesses and useful enemies, the Commander's forceful and protective options, and whether the political-control outcome retains credible danger.
They should inspect each preparation-to-operation transition and the reported-versus-planned timing of the offscreen work.
The private evening's refusal and distance choices require particular attention to later assumptions.
No score is supplied by this author report.

Universal Trickster acquisition, missed or rejected parent-route recovery, death recovery, Gift replacement, triad development and live compatibility remain separate unresolved work.
No new portrait assignment is implied by the rooms, clothing or incidents described here.
The user's reopened native-design art audit remains a separate review requirement.

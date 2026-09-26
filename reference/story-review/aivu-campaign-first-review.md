# Aivu campaign independent review

Status: approve the revised ordinary Azata friendship manuscript and optional Nexus support within the scope below.
No mandatory manuscript defect remains from this review against the pinned final revision.
This is not a declaration that all Aivu project requirements or live-game verification are complete.
I did not author the campaign or change its source/tests during review.
My role is an independent character and continuity reader; the author and parent perform separate implementation checks.
There is no fictional panel or promised score.

## Scope read

I read all of `storylines/aivu_campaign.py`, the existing four-scene `aivu_opening.py`, its prior review, native route/contact evidence and relevant localized character passages.
The new manuscript has sixteen visits including alternative acquisition and two optional Nexus visits, plus ten endings.
The assembled thirty-scene count includes mutually exclusive starts and endings; it is not thirty visits in a single playthrough.
The final candidate and measurements are pinned below.

The delivered scope is friendship with the existing Azata pet.
Aivu remains a young dragon with her native body and progression.
There is no romance, sexual framing, age increase, replacement pet, native rescue mutation or retroactive ownership on another mythic path.
Her discussion of becoming physically larger explicitly distinguishes the Commander's power from learning or growing older.
Romantic intensity is not an applicable review criterion.

## Native facts and authored additions

The existing pet blueprint is `32a037e97c3d5c54b85da8f639616c57`.
The reviewed capital asset links that actual pet to the expected native conversation and answer list `f1a65c6d838f58d49ad4ff40544b895b`.
The native Nexus etude supplies a separate supported conversation opportunity when the pet is present and the kidnapping absence is not playing.
These references support the attachment design; they do not replace a loaded-save test of the UI or contact state.

I independently reread these installed archive records:

- `World/Dialogs/c3/Mythic_Azata/Island/Dracosha/Cue_0056.jbp`, GUID `9bbebfddf8861584d89b097263329352`, carries localization `8a01a519-d581-488f-9842-b560129e848a`, the actual kidnapping-fear disclosure.
- `World/Quests/MythicQuests/Azata/C4_WheresMyDragon/WheresMyDragon_azata_c4_quest.jbp`, GUID `1ad9b8fa1fe3cb84b932e8a889fc1897`, is the native rescue quest.
- Its `06_AzataC4QuestEnd.jbp`, GUID `cd3c2daa826f24f4ebf73da3158d8692`, has `m_FinishParent=true` and points to that quest.

The new rescue-support visit requires the completed native quest and actual pet contact.
An earlier kidnapping marker or mere pet presence does not stand in for completion.
The remembered-fear question requires the seen native cue; its alternative asks what would help now rather than claiming an unheard confession.
The ordinary castle game does not claim a prior rescue.

Native localized passages establish her very young age, long dragon names, impulsive curiosity, accidental harm, eager advising, fear after captivity, Elysian relatives and the loss of power when the Commander changes path.
Native endings also support later visits to her family and the free crusaders/azatas returning her home after the Commander's sacrifice.
The leaf-playing cousin, fruit memory, garden cart, Pella, Torren, Berrit, letters and neighborhood games are authored additions.
They fit those anchors but are not previously established game events or newly spawned NPCs.

## Character and meaningful story development

The central project gives Aivu a purpose beyond being amusing beside the Commander.
Her map leads to a garden that must move, an audience she accidentally attracts and a game she nearly prevents herself from enjoying by taking every job.
Pella's departure then tests whether those new friendships can continue beyond a familiar location.
The family pages remain hers to keep, rather than becoming a reward for the Commander.

The voice is strongest when desire and embarrassment interrupt her confidence.
She wants to grow an argument, considers a garden appointment potentially boring, briefly resents the spectators she attracted and wants her game to be recognized as hers.
These are specific young-person concerns expressed through her native dragon humor.
Her self-importance is not erased when she learns to ask for help.
Nor does the Commander become her sole safe person: Pella, the neighborhood players and familiar Nexus voices have their own roles.

The cutting's overwatering is a consequence with observable damage and incomplete recovery, not a speech announcing that Aivu has matured.
The painted sign presents two workable compromises with weather and limited materials.
Pella may accept the original page or a new drawing, and the later letter responds to that actual choice.
Those linked changes make the length purposeful rather than a set of interchangeable affirmations.

The rescue visit allows storytelling or shared watching without curing fear.
Later recognition is gated by the support visit actually played.
Aivu can still be frightened on a good day; the manuscript does not treat successful rescue or pleasant company as proof that captivity has ceased to matter.
Her later offer of company to the Commander is reciprocal without making her responsible for repairing an adult's grief.

## Mandatory findings sent to the author

1. `when_the_drum_does_not_come/pause` originally did not establish the stiff-knee player's encounter, although shared `after` and `company` recalled it.
   The revised manuscript must consistently establish the same catch or near-catch on both paths and in `a_family_with_too_many_names/tell`.
2. `the_people_on_the_map/original` and `a_reply_from_the_other_garden/original` originally recalled the oversized onion and extra taste of sorrel even for moving/late starts that had not established those events.
   A first replacement also recalled the early-only suggestion that gardens might visit one another, so that replacement was returned for another repair.
3. `the_turn_the_commander_needs/story` and `competitive` assumed the pigeon conversation from `ordinary`, despite also following `expectation` and `grief`.
4. `the_next_excellent_thing/company` recalled an old shoulder feint established only by the earlier courier branch, while the alternate dreadful-creature branch could reach it too.
5. Four narrator explanations restated lessons already shown by the action: `a_small_garden_of_her_own/potted`, `the_turn_the_commander_needs/ordinary`, `a_reply_from_the_other_garden/add` and `the_next_excellent_thing/keep`.
   The requested edits preserve the actions and remove the explanatory afterthoughts.

These are concrete joins and prose issues, not a requirement to make every choice converge on the same experience.
I reread the replacements and accepted them in the final revision.
Both drummer paths now explicitly establish the loose-tail catch, and the later recollection describes that catch consistently.
The original gift and reply use the shared cart, wheel and moving route rather than an unplayed onion drawing or taste.
The final reply answers the actual before/after question instead of retaining its response to a removed question.
The personal-preference endings no longer depend on choosing the pigeon conversation, and the final game establishes its feint within the current visit.
The four explanatory clauses were removed or replaced with concrete actions.
The author's final additional repair changes the shared family-letter addition from the original-gift-only cupboard door to Pella's letter, which exists after both gifts.

## Gameplay and scope limits

The new wheel inspection uses a Commander Perception check with a played failure cost: lost time and a missed potting lesson, while professional inspection remains a viable non-roll choice.
That later lesson recognizes whether the player actually received it.
The campaign also lets the player choose roles in play, size of the gathering, how to handle disappointment, the sign's finish, a gift and the kind of support to offer.
None requires romantic flags or changing other companions' relationships.

The late Chapter 5 start introduces Pella and the garden afresh rather than claiming the four earlier map visits.
Completing the original opening can also lead into the later project when the player returns in Chapter 5.
The two Nexus visits belong to Chapter 4 and require appropriate existing friendship/native history.
They are optional branches, not claims that the late Chapter 5 acquisition retroactively played them.
Integration should update the opening's existing Chapter-3-only relationship guidance to describe the later capital start and optional Nexus support.
I reported that user-facing metadata issue to the parent; the reviewer did not edit shared relationship data.

The campaign does not yet supply bespoke Trickster guest access, Legend visits, replacement contact after detachment or other lost-contact recovery.
Native family visits mentioned in an ending are not a delivered in-game travel mechanism.
The ordinary Azata manuscript must be judged on its own quality, while those project-wide access requirements remain outstanding.
No art, ToyBox execution, Unity actor restoration or save/load approval follows from this literary review.

## Final revision and verification

| Artifact | SHA-256 |
| --- | --- |
| `storylines/aivu_campaign.py` | `82720E1EFE44B03A90BA36DB71F516795D44EF52171EBAE2E7048E26389F250D` |
| `tests/AivuCampaignTests.cs` | `6AE4E38EE602B201EFD18EAB527FACF45A39B7C0390AA57AED1F44BBE28731C1` |
| Isolated 509-scene candidate | `462EE573A9F2F07CA19A217892CF058C7D97BE88BC3A09428B1E45A695530E2D` |

I independently copied the candidate into `C:/Users/Z/AppData/Local/Temp/aivu-independent-review-o67o_3tq` and reran `Rules.Validate` plus the actual focused suite.
The final candidate passed 48,905 assertions/traversals in that isolated runner.
The suite walks the actual four-scene opening, early and late acquisition, the ordinary sequence, optional Nexus visits with heard/unheard fear history, all new pages and both roll outcomes.
It also checks native absence and restored availability, actual rescue completion, physical-contact loss, native prerequisites, postponement, terminal-only effects and scoped ending exclusivity.
These are headless authored-state traversals, not execution of a Unity save or native quest progression.
External rescue completion is supplied as an explicit observed-history transition in the fixture.

I independently compared the final candidate with the previously tested `D8A4...` manuscript candidate.
Only two `Text` fields changed, both in `a_reply_from_the_other_garden`: `original` and `add`.
I reread both exact final paragraphs and reran the focused suite after refreshing the candidate.
No scene graph, choice gate, index or effect changed in that final delta.

## Amount and depth

I inspected and reran the author's selected-path measurement script using the project tokenizer.
It excludes aborted choices, follows both check outcomes, respects choice prerequisites and retains the future-dependent history when combining path totals.
The corresponding chapter/area/entry eligibility is checked by the actual Rules suite, rather than claimed from the word-count script itself.

| Scope | Scenes | Raw words | Distinct normalized segment words |
| --- | ---: | ---: | ---: |
| Existing opening | 4 | 4,186 | 4,179 |
| New campaign including alternatives/endings | 26 | 20,072 | 19,993 |
| Assembled character | 30 | 24,258 | 24,172 |

The assembled figure contains 22,459 page-prose words and 1,799 displayed-choice words before exact-segment deduplication.
It credits no titles, entry labels, journal metadata, native dialogue or RanRomance prose.
Removing every ending still leaves 23,104 distinct normalized words across twenty physical scene entries, so the floor is not being crossed by accumulating ending variations alone.

| Completed selected history | Played visits | Words including one selected ending |
| --- | ---: | ---: |
| Early ordinary friendship | 17 | 12,424-13,061 |
| Early plus both Nexus visits, native fear unheard | 19 | 13,689-14,400 |
| Early plus both Nexus visits, native fear heard | 19 | 13,696-14,407 |
| Chapter 5 late start | 13 | 9,429-9,777 |

The route crosses the 21,000-word meaningful aggregate floor.
There is no separate invented requirement that every selected playthrough contain 21,000 words.
The configured installed RanRomance inventory is aggregate evidence too: it lists Targona at 18,359 distinct normalized words, Minagho at 15,790, Aranka at 15,758 and Terendelev at 14,827.
Passing the aggregate floor does not establish a selected playthrough of that length or prove all-route RanRomance parity.
The ordinary manuscript now has sustained development, consequences, optional support, reciprocal friendship and completed as well as unfinished outcomes; it is no longer a short opening draft.
Its missing other-mythic access and runtime verification remain separate requirements.

## Revision-specific assessment

These are one independent reviewer's judgments of the actual pinned manuscript, not percentages generated by a test runner or a claim of unanimous review.

| Discipline | Score | Reason |
| --- | ---: | --- |
| Writing and pacing | 92/100 | A connected neighborhood story, distinct playful situations and concrete consequences; repeated lesson narration was reduced. |
| Native characterization | 94/100 | Recognizable curiosity, impatience, showing off, affection and childlike reasoning without replacing her native motives. |
| Age-appropriate friendship and agency | 96/100 | Chosen activities, reciprocal company and independent friends; no romantic framing or demand that fear disappear. |
| Continuity and history accuracy | 94/100 | Repaired branch memories, truthful late start, actual rescue/fear gates and distinct family correspondence. |
| Player participation and consequences | 92/100 | Played check failure, viable professional alternative, meaningful role/gift/art/support choices and later responses. |
| Meaningful ordinary campaign depth | 93/100 | Substantial connected early/late arcs with optional Chapter 4 support and consequences continuing into Chapter 5. |

Approve this manuscript for parent integration and further project review within its ordinary Azata scope.
The journal guidance correction, shared binding/build checks and loaded-game verification still belong to integration.
Universal Trickster friendship access, lost-power guest visits, unavailable-actor recovery and art are not approved or implied by these scores.

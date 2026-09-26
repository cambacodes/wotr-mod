# Ember campaign independent review

Reviewed 2026-09-26.
I read the entire new manuscript, the original three friendship scenes and five puppet afternoons, the prior afternoon reviews and the companion design/evidence records.
I also checked the relevant native quest and dialogue records directly in the installed `blueprints.zip` and resolved their text against installed `enGB.json`.
I did not author or edit this contribution, its tests or its handoff.
This is one independent editorial review, not a panel of invented reviewers.

## Reviewed revision and decision

| Item | SHA256 |
| --- | --- |
| `storylines/ember_campaign.py` | `5CB72B6FE1BDEB870EC200D856144A19E513C6CED5127BFF6263B694D1256F5C` |
| `tests/EmberCampaignTests.cs` | `6451FFD867BCA6D49F718FBA81E12C46CEB0B4B46C3B0D3944E0F9FEAC12BA8F` |
| Isolated assembled candidate | `63505CBA41CC90796A87D1C3601440C862664E26B269A6BB884E5192EEF3BB1E` |

Accept this revision as a substantial ordinary friendship campaign contribution and a separate, bounded continuation of care after the native devastated outcome.
All mandatory issues identified in this review have been repaired and reread at the hashes above.
The assembled meaningful-content floor is met.
This does not certify completed universal Trickster access, missing/dead-companion recovery, actual Unity contact or full game deployment.

| Reviewed discipline | Score / 100 | Judgment |
| --- | ---: | --- |
| Writing and dialogue | 91 | Connected scenes, clear physical action and small jokes sustain the progression; some over-explanatory qualification remains. |
| Ember's voice and characterization | 92 | Compassion coexists with disappointment, playful competitiveness, uncertainty and preferences of her own. |
| Age-appropriate friendship and agency | 95 | No romantic framing, sexualization, age transformation or reward for overriding her wishes. |
| Continuity and native-history accuracy | 94 | Current magic, optional native speech and Soot's identity now remain distinct from historical or assumed events. |
| Player participation and consequences | 92 | A real check, non-roll solution, competing shelter arrangements, reciprocal care choices and differently resolved searches have played consequences. |
| Ordinary manuscript depth and pacing | 91 | Twenty early-route visits or twelve late-route visits develop a relationship beyond a short draft; the missing-covering stretch is the slowest section. |
| Devastated-outcome care writing | 93 | Three distinct visits respect current distress and her ability to end company without awarding a cure or a new ordinary friendship finale. |

These scores are editorial assessments of the specified content, not probabilities, mathematical proof of parity or ratings for unimplemented access.

## Required repairs and their verified results

The original `an_answer_from_elsewhere/reply` performed a fresh impossible paper road whenever the earlier `letter_trickster` history existed.
That allowed a later Legend to use current Trickster magic.
The final `reply` offers a mundane `paper_road` and a separate `another_road` requiring current `trickster`.
The original letter intervention and Anet's answer remain remembered after the mythic change.
I walked the original eight scenes, the new letter progression and a later Legend continuation through the final friendship visit without clearing that history or making new magic available.

`the_small_choice/start` originally introduced a folded square while its alternative branches called the cloth unfolded without an intervening action.
The revised start explicitly lets the folds open before the choice.
Folding it together, leaving it alone and watching Soot now share the same physical starting state.

`where_she_is_needed/start` originally said the Commander had heard Ember's decision to keep distance from frightened followers.
That specific native speech is optional, and quest completion alone does not establish it was heard.
The good and law choices now ask about her present feelings, and their replies give present answers without inventing the missing conversation.

Soot was repeatedly called male in the new manuscript.
The installed `World/Dialogs/c1/KenabresBurning/MeetEmber/Cue_0079.jbp`, asset `e4ac0504dbcc3f64ba11bb7d9f18ee33`, explicitly identifies Soot as female through text key `d8ebb5cb-045a-4677-b58d-da8bb2de7984`.
The final manuscript corrects the crow's pronouns while preserving male humans, incidental birds and the fictional puppet characters where appropriate.
A first correction left two ambiguous consecutive uses of “she” in the opening; the final introduction names Ember and Soot separately.
The original opening's male fictional drawing does not require changing merely because it was intended as a portrait of Soot.

I required targeted removal of repeated narrator lessons at `the_empty_basket/declined`, `the_missing_covering/apology`, `a_question_at_the_yard/room`, `the_words_people_keep/support`, `a_letter_with_no_road/road_checked`, `where_she_is_needed/today`, `the_small_choice/fold` and `the_visits_she_can_end/bird`.
The revisions replace those afterthoughts with observable behavior or remove them.
The first rewritten support request inadvertently accused the player of interrupting Ember, although the actual prior choice did not do so.
The final line makes the request conditional on a future moment when she is stuck.
It preserves her preference without inventing misconduct by the Commander.

## Native outcome and contact evidence

The current outcome aliases use `EmberEnd_Good` `b981026a5be6a9a49bf1f7ab57f9e1bb`, `EmberEnd_Law` `f55fcc7bf5fd0c14384cb15dce345c8e` and `EmberEnd_Evil` `b1d0c45e438c2ae458466ed56de99a9d`.
The Q3 quest is `49b7496143daed149ab4557a9684dd53`.
The good/law discussion requires both its actual completed quest and the appropriate native outcome.
Ordinary new visits forbid the devastated outcome rather than letting their confident discussion continue unchanged.

The native Q3 `EndDiscuss/Cue_0001`, asset `1d99007b029d96b44b91257b72b3d133`, completes the top objective and hidden `Obj_0_Secret` on stop.
The hidden objective `c4d35a3ca9759da479903dec9a3984fa` has `m_FinishParent = true`.
Optional `Answer_0007` can later lead through `Cue_0016` to good `Cue_0018` or law `Cue_0019`.
The latter is asset `c277888d20407c940a009d536b32d8e4` and contains her wish to stay away from people she frightened.
This sequence is why the original “You said” callback was invalid despite a valid Q3-completion gate.

The devastated companion `Cue_0124`, asset `d122314889045d743a701aa07413ce1c`, similarly completes the Q3 objective and hidden final objective on stop.
Its answers use `fd8276a6302f4d44583eba3f0b9663bf`.
The three new care scenes bind that answer list and require completed Q3 plus the devastated outcome.
They therefore do not replace the first native conclusion with cheerful friendship content.

The normal new visits use native companion `2779754eecffd044fbd4842dba55312c`, normal answer list `f2a35965e9bc601449498bd022b04d9d` and actual contact metadata.
Their authored gates retain death, departure, absence and closure exclusions.
My Rules fixtures cover loss and restoration of contact, but cannot prove a live companion view or native answer-list presentation in Unity.
The original eight scenes retain their earlier remote metadata in the inspected source; this contribution does not itself upgrade their delivery mechanism.

Q1 completion gates the captivity discussion.
Q2 completion gates the discussion of the Nocticula meeting.
The inspected Q2 quest `a3f445a64ee130f4396c20a07c30ece0` has the Nocticula objective `5da2a5d4866c7d948b8f1bc996791ca6` as its finishing objective.
The new dialogue does not claim that Ember has canonically redeemed Nocticula, command her behavior or grant the Commander a relationship with her.

## What sustains the ordinary story

The first new activity pays off the earlier offer to spend time without an audience.
Whistling and the stone game supply a small shared accomplishment that returns at the final visit.
Ember wants to win, forgets whose stones are whose and can laugh at her own mistakes.
These moments give the friendship more personality than a sequence of moral discussions alone would provide.

The room story has distinct problems rather than one repeated transaction.
Mara refuses the expected keepsake and chooses the wooden handle instead.
The door inspection can succeed, fail with a delayed opening, or be referred to a carpenter with a different timing/cost result.
The cost belongs to Vessa in the story; the scene does not pretend to debit the Commander's native gold.
The later missing covering was lent without permission, and its return does not automatically repair Deren's trust.
Choosing between bringing Selvi and her brother to the room or extending the loan changes who moves, who sleeps uncomfortably and the next visit's account.
The outcome acknowledges that returning an object and repairing a friendship are different events.

The middle stretch is still heavy with rooms, coverings, permissions and explanations.
It is meaningful material, but it is the part most likely to feel slow when played immediately after the puppet story's borrowed-cloth dispute.
The later reciprocal-care visit, the mistaken-apron story, Ember's annoyance at people rewriting her words, the uncertain search for Anet and the final game supply needed changes of subject.
Future expansion should build on those different interests rather than add another missing household object to increase the count.

The authored Trickster intervention finds a lead rather than delivering Anet as a reward.
Its later letter can contain both affection and a refusal of a visit.
The mundane searches remain unresolved but leave room for an enjoyable afternoon.
Vessa, Deren, Mara, Selvi, Anet and their new circumstances are authored developments, not claimed discoveries in the native script.

## Care remains a different continuation

The care sequence concerns permission to sit, a manageable choice about a cloth or the crow, and a later visit Ember can explicitly end.
It does not send devastated Ember back to the public argument, perform successful preaching, restore lost abilities, change her appearance or turn distress into a romance opportunity.
The Commander can acknowledge earlier cruelty without being granted forgiveness.
Her tears and uncertainty remain after companionship is offered.
The final care flag records permission for possible later visits, not proof of recovery.

These three visits are a short support continuation.
They are not an equally long alternate twenty-visit campaign, and the report does not credit them as one.
The user requirement is the assembled character floor; I have not invented a separate 21,000-word minimum for each mutually exclusive outcome.

## Length and comparison

I independently reran the project inventory on the final candidate and reran the selected-path counter after reading its traversal and future-condition merging.
Counts strip markup and include rendered node text and selected choice labels, excluding titles, entry labels and external native or RanRomance text.
Whole-segment deduplication is not semantic originality detection.

| Scope | Count |
| --- | ---: |
| New contribution, 28 entries | 15,280 distinct words; 16,054 raw |
| Full assembled Ember, 36 entries | 21,695 distinct words; 22,512 raw |
| Assembled content excluding three care visits and two care endings | 19,698 distinct words |
| Three care visits and two alternative care endings | 1,998 distinct words |
| Selected early route, 20 visits and one ending | 10,377 to 12,060 words |
| Selected fresh late route, 12 visits and one ending | 6,211 to 7,712 words |
| Selected three-visit care sequence and one ending | 1,121 to 1,369 words |

The selected ranges enumerate the modeled native-good, native-law and unresolved histories with and without current Trickster, not every possible external modification of a save.
The early measurement introduces Q2/Q3 history at the later Chapter 5 discussion; the separate played Legend witness verifies the relevant change-of-path continuation.
The care counter reaches nine selected combinations.
The tiny difference between summing separately deduplicated subsets and deduplicating the whole is shared text, not extra content.

The installed-source inventory `reference/art-review/ran-route-word-inventory.json` records Targona at 18,359 distinct normalized words, Terendelev at 14,827 and Aranka at 15,758.
It also documents loader limitations and includes some material that the authored-scene counter excludes.
Ember now clears the project's conservative 21,000-word assembled floor and has a connected long friendship manuscript rather than a short opening draft.
This comparison does not establish identical selected-playthrough lengths or blind-test writing indistinguishability.
The parent routes' multi-act delivery and mythic endings remain relevant benchmarks beyond aggregate length.

## Reproduction and outstanding full-route work

The author's focused suite passes 20,783 assertions/traversals on the final revision.
My separate project is `C:/Users/Z/AppData/Local/Temp/ember-review-a9wcef2j/Check.csproj`, with a pinned copy of the final candidate beside it.
It reruns that suite against actual `Rules`, then additionally walks the original opening through the complete early campaign with a later Legend change, the fresh late campaign without original-afternoon flags, and fresh native-devastated care.
The combined run passes 21,436 assertions/traversals.
These are managed Rules checks, not that many independent user journeys or live game tests.
No shared output or installed files were modified.

The parent separately reports successful combined staged validation of this final source: 22,837,122 Rules assertions, 861 binding uses and 55,275 managed-construction assertions over 16,232 blueprints and 459 scenes.
Those larger results were not produced by my private witness and should retain the parent's attribution.
The parent reports its differently serialized candidate is parsed-equal to the author's pinned candidate.

The new physical scenes are capital visits in Chapters 3 and 5.
They contain remembered Abyss events when gated, but no played Chapter 4 friendship encounter.
The late entry handles missed authored afternoons for a present companion; it does not introduce an unrecruited Ember or find a departed/dead one.
The letter's Trickster trick is character-appropriate optional content, not universal recovery access.
Live contact and interruption delivery, the original scenes' contact upgrade, unavailable-history recovery and appropriate art coverage remain outside this bounded acceptance.
Those limits prevent declaring the entire requested Ember route finished even though this manuscript passes its review.

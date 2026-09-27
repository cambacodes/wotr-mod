# Tirabade morale revision review

Date: 2026-09-26.
Reviewer: one independent reader, not the author of these scenes.
Scope: the new `return/morale` and `last_watch/life_broken` branches and their integration in `storylines/tirabade_chronology.py`.
Final reviewed source SHA256: `F3ACB49FA8B7F46C815CDFC805D06AFFFD919B387ADE23C08D772FE11220865E`.
This does not approve the assembled Tirabade campaign, its content floor, art, native execution, or release readiness.

The scoped editorial revision passes.
Irabeth retains persistent doubt without becoming incapable, while Anevia responds as her wife rather than delivering a generic lesson.
The native state changes which final-watch response the player receives and supplies an optional reunion discussion.
The scenes neither clear that state nor announce that affection has cured it.

| Criterion | Independent score | Evidence |
| --- | --- | --- |
| Writing and specificity | 92 | The report she keeps checking and the flooded shorter road give her doubt and competence concrete expression. The cup and worn paper support the exchanges without dominating them. |
| Native characterization | 93 | Irabeth still answers officers and knows the road while doubting whether she deserves the future. Anevia's offer to talk for three and practical complaint about the detour retain her humor. |
| Emotional continuity and agency | 93 | Irabeth interrupts reassurance, asks to hear difficult news, and admits that she cannot always believe Anevia. The player accompanies her without resolving those doubts. |
| Branch joins and chronology | 92 | Both existing approaches to `life` receive the conditional alternate. The new reunion response rejoins `future`; the final-watch response rejoins `end`. Neither asserts that a particular earlier morale conversation occurred. |
| Meaningful use of native state | 92 | Broken changes the substance of the response rather than only one adjective. The state remains intact and no invented mechanical recovery is awarded. |

These are editorial judgments about this small revision, not measured probabilities or scores inherited from tests.
Erotic intensity is not a useful separate criterion for these two nonsexual conversations.
Their task is to keep the romantic relationship credible across the native morale branch.

## Native support and characterization limits

The evidence is documented in `reference/canon-review/tirabade-shared-history-branch-audit.md`.
Native `IrabethBroken_Chapter03`, GUID `7a038ff7b70e91844954407b18e8feb6`, still gates the Threshold conversation in chapter 6.
`IrabethAnevia_Threshold/Cue_0002`, asset `33038b17ba9e8fe46b692ff8eff81e99`, requires Broken Playing; its alternate `Cue_0001` requires Broken not Playing.
That supports continued variation near the final battles.
It does not establish every detail of the new prose as canon.

The added conversations are authored responses consistent with that surviving state.
Irabeth's request to attend supper without first producing a better account of herself could become repetitive if many adjacent scenes use the same form of reassurance.
Here it is balanced by her wish to hear the Commander's bad day and her dry reply to Anevia.
The final-watch page changes subject to travel and ends with a practical request for a copy of the route.
I do not find a blocking repetition or automatic-healing claim in these additions.

"You can plan a road without putting yourself on trial" is the most polished reassurance in the new passage.
Irabeth's failure to accept it immediately and Anevia's return to the actual route prevent it from becoming a therapeutic resolution.
Retaining that resistance matters more than adding another explanatory paragraph.

A separate Encouraged scene is not required for this change.
The unchanged `life` page offers hopeful planning while acknowledging fear, which remains plausible for Encouraged and ordinary states.
It does not claim that every absence of Broken proves complete recovery.
When both native states are present, Broken takes precedence through the explicit gates.

## Independent verification

I read the full chronology overlay, its uncommitted diff, the underlying `return` and `last_watch` scenes, relevant progression gating, the authoring helpers, and the native-history audit.
I assembled the current payload in memory with `expansion.make_expansion()` using Python's `-B` option, without writing an export or modifying shared build outputs.

For no morale flags, Broken alone, Encouraged alone, and both flags, I independently checked the available choices at `return/now`, `last_watch/start`, and `last_watch/after`.
Every checked node retained an available choice.
Each final-watch entry offered exactly one of `life` and `life_broken`.
The new node targets existed and rejoined the expected continuation.
Both new terminal transitions have empty effect lists.
The pre-existing `end` still sets only its existing `last_words` flag.

The original final-watch answer positions remain in place with Broken added to their forbids, while conditional duplicates are appended.
The ordinary `life` text is untouched.
This preserves the indexed source positions; I did not independently execute native blueprint GUID generation for this revision.

This independent probe checks assembled data and explicit condition selection, not the C# Rules engine or Unity dialogue execution.
The engineering reviewer subsequently caught an integration-order issue outside my original final-watch position check: adding the reunion option before the bridge displaced the existing `return/now` index 2 answer.
The root moved morale integration after the bridge.
I independently compared the two new node objects with the earlier candidate and confirmed that the reviewed prose and choices are unchanged, and that `back_negotiated` is again index 2 with `morale` appended at index 3.
The root separately reported the corrected full Rules pass of 25,958,725 assertions against `C:/Users/Z/AppData/Local/Temp/tirabade-morale-fixed-g9omrnz0/Story.json`, including four native morale cases and the full campaign.
That is root-reported C# verification, distinct from my independent assembled-data probe above.

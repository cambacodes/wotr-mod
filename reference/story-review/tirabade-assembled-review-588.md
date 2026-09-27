# Tirabade assembled manuscript review: committed 588-scene export

Reviewed on 2026-09-26.
Verdict: revision required for two branch-memory errors.
The ordinary living, available-partner manuscript now meets my editorial threshold in the other assessed dimensions, including meaningful doubled aggregate length.
It does not yet pass every criterion above 90, and this report does not approve the complete playable route, acquisition, recovery, art, or release.

## Exact scope and method

The reviewed full export is `development/Story.json`, SHA256 `ABAF62B57835480AF46A7C1648820AE071BFC0624AB8EFFD74DA87D19F58F87A`.
Selection is `scene.get("Relationship", "tirabade") == "tirabade"`.
The ordered 68-scene subset, serialized with sorted keys and compact separators, hashes to `E2672EDB8E52AAA2C7E6765E895780CCC2C3A4EF328CADF9DDE1D35E08C8C135`.
I read all 494 nodes and all 735 choices, including mutually exclusive outcomes, endings, separation options, and the negotiated bridge.
I reread the six independent spouse-answer, first-evening, and post-separation invitation scenes needed to understand those joins.
Those independent scenes receive no word credit in this review.

I read the previous assembled review and the later opening, progression, morale, late-pacing, and scar/Queen revision reviews, then assessed the actual assembled text rather than inheriting their passes.
Native characterization is checked against the previously extracted game dialogue in `reference/canon-dialogue.txt`, SHA256 `E10DD05FA5D08FF7AFD3DB4700433EDD65160F46D6FDC69DA3BCD4131ED2AE2B`, and the documented scar, Queen, and morale witnesses.
The civilian adventures and expanded relationships remain authored alternatives, not newly discovered canonical events.

The frozen export, full per-scene reading copies, and independent count/search probe are under `C:/Users/Z/AppData/Local/Temp/tirabade-588-full-review`.
The probe result is `final-reading-probe.json`.
I inspected the actual JSON requirements and choice links where the simplified reading copies omitted metadata.
This was a manuscript and source-graph review, not a new execution of the native game or a full Rules suite.
No source, shared export, generated asset, or runtime file was changed.
Root has separately offered to correct the two findings below; those future corrections are not included in this frozen verdict.

## Scores

These are independent editorial judgments, not measured probabilities, inherited contribution scores, or an average that can cancel a failed dimension.
The required threshold is strictly greater than 90 in each relevant dimension.

| Criterion | Score | Assessment |
| --- | ---: | --- |
| Prose and specificity | 92 | Concrete actions, domestic wit, and professional work now carry most of the emotional development. Some older narrator explanations remain. |
| Pacing and meaningful variety | 91 | The revised later sequence replaces repeated reassurance with games, investigation, a dance, and changing material consequences. The formal relationship discussions remain the slowest section. |
| Character voice and plausible authored development | 92 | Anevia's acquisitive curiosity and teasing, and Irabeth's pride, formality, faith, and competitiveness remain distinguishable. Neither becomes an interchangeable counselor. |
| Wives' mutual attraction and independent agency | 95 | They initiate affection, disagree professionally, surprise one another, and retain private interests without treating the Commander as the owner of their marriage. |
| Mature non-graphic romantic tension | 94 | Wanting to impress, being caught looking, deliberate physical proximity, the blue coat, and the rented room make desire specific and reciprocal. |
| Commander participation and relationship choices | 92 | The player can disagree, choose risks, preserve private relationships, set an evening's degree of intimacy, or leave without every answer becoming the same promise. |
| Decisions, checks, and remembered consequences | 92 | The disputed roll, stolen records, evidence examination, refund, and circulation choice affect later scenes rather than merely changing a response adjective. |
| Continuity and branch memory | 87 | Two unconditional callbacks assign specific earlier content to paths that do not contain it. Both need correction before this manuscript passes. |
| Meaningful aggregate length | 95 | Distinct prose alone exceeds the doubled floor; the later material develops recurring characters and consequences rather than existing only to increase a count. |

The gameplay score concerns the decisions present in this manuscript.
It is not a score for complete mythic acquisition, native quest attainability, live scene delivery, or ToyBox behavior.

## Required corrections

### 1. The returned letter remembers content the player did not write

At `abyss_letter/start`, both the ordinary recollection and unfinished apology are available without additional choice requirements.
The ordinary branch explicitly writes about cold tea, a repaired glove, and the wives' small habits.
The unfinished branch instead writes an apology, removes its request for reassurance, and retains a plain account of the Commander's conduct.
It does not write the glove recollection.
Both branches join `abyss_letter/truth`, whose terminal choice sets `wrote_letter`.

At `return/start`, the letter option requires only `wrote_letter`.
Its destination, `return/letter`, unconditionally says that Irabeth reaches the passage about the repaired glove and asks whether the Commander remembered it.
The explicit counterexample is `abyss_letter/start -> unfinished -> truth -> return/start -> letter`.
The unrelated earlier glove scene proves that the memory could exist, but not that the Commander selected it for this letter.

Required correction: react to the kept unsent letter, which both branches establish, or introduce an actual branch-specific callback with its own saved evidence.
A shared reaction is sufficient and avoids unnecessary state.
Keep Anevia's dry remark about the useless military report and the choice to return the paper to Irabeth if the revised response supports both contents naturally.

### 2. The ascension ending attributes an optional dragon conversation to other paths

`ending_ascend/end` says that Anevia had asked not to be mourned before her time, then calls the women's statements requests that survived the transformation.
The specific earlier request is in `power/dragon`, reached only by the optional dragon-qualified answer.
The same `power/start` offers an unrestricted answer leading directly to `terms`, and other mythic answers also join there.
All can establish `power_terms`; neither the developed route nor `ending_ascend` requires visiting the dragon node.
The ending itself requires `committed`, `ascended`, and `three_progression.developed`, not a dragon conversation or remembered request.

I searched the full reviewed subset for mourning references.
The other occurrence, `last_watch/after`, concerns the wives' mourning if the Commander dies and Irabeth's reciprocal request to remember them as people who wanted to live.
It neither supplies Anevia's specific premature-mourning request nor is mandatory: `last_watch/start` can go directly to a life response instead.
Thus it cannot repair the unconditional ending memory.

Required correction: write the wives' present response to ascension or use a genuinely shared earlier statement without claiming that the player heard an optional exchange.
Do not require a specific mythic answer merely to make an otherwise general ending's prose true.
This finding concerns authored memory, not a claim that every listed mythic can achieve the game's ascension ending.

## What has materially improved

### The opening has distinct motives without rewriting the marriage

The revised Anevia opening uses her practical humor, coin handling, quick observation, and enjoyment of making the Commander lose composure.
Irabeth's glove work and competitive play give her an independent source of pleasure and embarrassment.
The two women no longer need the same explanation about being exhausted, unseen, and deserving to be wanted before attraction can begin.
The healed-leg wording no longer conflicts with the native confident greeting.

The affair route remains an authored morally complicated possibility.
It does not require pretending that the native marriage was loveless: the actual game presents the wedding as Irabeth's happiest day and Anevia as central to her life.
Desire for the Commander can coexist with that attachment, but the secrecy has consequences in the reckoning and spouse responses.
The negotiated alternative has its own history-aware answers and does not inherit a confession to betrayal it did not contain.
The independent spouse-answer scenes establish choices rather than treating one wife's agreement as the other wife's romantic interest.

### History does not disappear into romance

`return/morale` and `last_watch/life_broken` let Irabeth continue doing her work while doubting herself.
The route does not pronounce her cured because the Commander stays close.
The Broken branch takes precedence when that native state is present.

The scar discussion permits silence, limited acknowledgment, or a defensive answer.
Irabeth retains her native refusal to keep defending the matter, while Anevia's anger remains recognizably her own.
The ensuing `last_watch/scar_unsettled` callback acknowledges an unresolved evening rather than awarding forgiveness.
The Queen-loss response gives Irabeth a concrete act involving letters while preserving grief and failure.
Its later letter callback requires the actual shared authored event.
These additions respond to observed native histories; they are not claims to cover every unobserved or unavailable history.

### The long shared campaign earns its domestic intimacy

`three_match` and its aftermath allow keeping the disputed advantage or replaying it, with dissatisfaction and defeat surviving later conversation.
Irabeth's desire to become better at the game is more revealing than another declaration that she deserves leisure.
The flour and map scenes give Anevia something to do badly, enjoy, and argue about.

`three_stolen_roads` does not restore every loss after the decision.
Saving the book leaves missing acknowledgments; following the papers damages an irreplaceable personal record.
Ista and Wenna retain their own anger, work, and marriage rather than existing solely to thank the lovers.
`three_ista_departure` and the later commercial dispute preserve both versions of that history.

The professional exchange in `three_beth_account/walk` now gives the wives different useful priorities.
Anevia wants Malven to commit to his account before hearing the evidence; Irabeth will protect the copyist while using that approach.
At `three_counterclaim/terms`, Anevia favors exposing the pattern and Irabeth favors getting money back into Ista's work.
The Commander must support a course with a cost, and the subsequent refund, partial-payment, or unpaid branch remembers it.
This is an actual disagreement between competent partners, not an obligatory emotional lesson.

### Mutual attraction is present on the page

The wives' dance begins with Irabeth's chosen tune and Anevia deliberately distracting her.
The Commander can enjoy watching them before joining, without turning their affection into a performance offered only for the player's approval.
The open or fastened coat and the leading or following dance practice receive correctly gated later callbacks.
Irabeth's desire becomes increasingly active: she chooses the room, enjoys making Anevia wait, and tells the Commander where she wants them.
Anevia can be rendered briefly speechless rather than always supplying a protective joke.

The shared nights remain non-graphic, with desire conveyed through interrupted speech, kisses, warmth, attention, and the practical comedy of furniture and clothing.
Choosing company, sleep, a walk, or a separate bed does not make the other options disappear from the characters' personalities.
The wives keep wanting each other after the Commander leaves.

## Decisions, length, and remaining limits

There is one actual skill roll in the reviewed 68 scenes: Commander-only Perception DC 25 at `three_back_of_seal/method`.
Success links the damaged seal and name to Malven; failure leaves a witness without that proof.
The alternative cataloguing approach consumes Gresa's afternoon and establishes a weaker connection rather than guaranteeing the successful roll's reward.
The stronger evidence produces the full-deposit offer, while weaker evidence leaves a half offer; circulating the accounts postpones repayment.
Subsequent scenes remember those results.
This is a meaningful roll, but it is not a campaign full of different skill checks, and should not be advertised as one.

The player also makes consequential decisions without dice: replaying the match, pursuing the thief, choosing the copyist's participation, settling or circulating the claim, naming the relationship to Tessa, and ending the shared arrangement while asking about a separate relationship.
Some smaller flirtation choices naturally converge.
They are valuable expressions of taste rather than supposed branches with separate quest outcomes.
Occasional summarized player speech, such as naming an imagined destination in `three_rooms_unlocked/meal`, remains less individualized than an explicit response menu, but does not invalidate the larger player role.

| Independent count | Words |
| --- | ---: |
| Raw prose and choices | 56,211 |
| Raw prose | 50,415 |
| Raw choices | 5,796 |
| Distinct normalized prose and choices | 51,569 |
| Duplicate whole-segment credit removed | 4,642 |
| Distinct prose alone | 46,763 |
| Required doubled aggregate floor | 42,000 |

Counting strips markup, normalizes whitespace, and counts Unicode words with internal apostrophes.
Exact normalized segments count once across the trio.
Titles, entry labels, parent text, native dialogue, and the separate Anevia and Irabeth campaigns are excluded.
The amount is substantial even without choice-label credit.
The continued Ista dispute and its imperfect outcomes are meaningful content rather than redundant assurances added to reach the floor.

This is an aggregate manuscript count, not the number of words a single player reads.
Choosing the explicit shortened promise intentionally leaves the shared outings unfinished; its separate ending acknowledges that fact.
The developed ending requires the developed chain instead of silently granting its memories to the shorter route.
I have not substituted the earlier selected-path word ranges as if they had been recomputed for this changed export.

The slowest surviving passage is the cluster of truth, terms, privacy, and future conversations around `a_truth`, `i_truth`, `table`, `ordinary`, the self scenes, `power`, and `future`.
The repeated distinctions between wanting, permission, promises, and separate lives are still noticeable.
They now have enough different character motives and later enacted consequences to clear my pacing threshold narrowly.
Further edits should cut redundant explanations, not remove difficult disagreement or add more reassuring speeches.

Other lovers are permitted in the authored relationship discussions, including the negotiated bridge, and are treated as people with their own promised time.
That literary compatibility is not a verified ToyBox Free Love/No Jealousy runtime result.
The ordinary route still depends on living, available wives and its native/history conditions.
The separate one-visit departure recovery does not by itself prove restoration of this full campaign, and death recovery and all-path Trickster acquisition are outside this manuscript approval.
Live scheduling, native contact, endings, save/reload behavior, portraits, and actual concurrent game romances still require their own verification.

Correct the two branch memories and independently review those exact edits before changing this manuscript's verdict.
Passing that follow-up would still be an ordinary manuscript pass, not an automatic declaration that the entire playable romance is finished.

## Independent follow-up: two-node correction

Later on 2026-09-26, I reviewed root's correction in `story.py`, SHA256 `DB7D008BCF49883B392D1C8D612113038C27A24BBD00DD3694354C7B24E3658A`.
The original export, findings, and scores above remain the historical baseline.
I independently assembled the current source in memory, normalized its JSON representation, and compared the entire 68-scene subset with the frozen baseline.
Exactly two values differ: `ending_ascend/end.Text` and `return/letter.Text`.
Every scene, node, choice, condition, flag effect, and ordering is otherwise identical in this subset.
No shared export was generated by this review.
The revised subset hashes to `BE02795A30DEF02A5F05A0756FE00AB7B36808953A8344DDF2F25496F5FFBC58`.
The isolated revised subset and comparison results are saved beside the baseline as `tirabade-two-node-followup.json` and `two-node-followup.json`.

The returned-letter response now has Irabeth smooth a crease and ask, "You kept this all that time?"
Both writing branches actually fold and keep the unsent letter, so the reaction follows either selected content.
It also leaves room for affection without declaring that the apologetic account has earned forgiveness.
Anevia's military-report joke still fits a private letter about either domestic memories or conduct.

The ascension ending now gives Anevia a practical objection to missing supper and Irabeth an objection to disagreements acquiring a congregation.
These are present authored reactions to the ending's transformation, not falsely attributed earlier requests.
They retain different voices and the legitimate concern about unequal power without requiring the dragon branch.
The unchanged later paragraphs remain supported by the developed relationship and do not restore the removed false memory.

Both findings are resolved in this exact revision.
Continuity and branch memory now score 92; the other scores remain as recorded above.
All assessed ordinary-manuscript dimensions therefore exceed 90 in this revised subset.
Its distinct aggregate is 51,566 words, including 46,760 distinct prose words, still above the 42,000 doubled floor without choice credit.
Final scoped verdict: the revised ordinary Tirabade manuscript passes this independent editorial review.
This does not approve unresolved acquisition or recovery, native execution, ToyBox concurrency, art, or a complete playable release.

# Tirabade civilian campaign: independent writing review

## Final bounded rereview

Inspected source SHA-256: `498A293C625584EB47AAABBCAB4DC28ED2EC89AF7BDBB23CF7B7BF092371E5DC`.
The current bounded writing score is **92/100**, superseding both earlier scores retained below.
Voice and characterization earn 27/30, dramatic specificity 18/20, the three participants' attraction and agency 19/20, choices and consequence continuity 19/20, and prose/staging 9/10.
No remaining major writing defect was identified within the six-scene contribution and the reviewed joins.

The two reconsideration choices are appended after the unchanged reaffirmation and haste responses.
The standing-history response requires `three_match.stood`; the replay-history response requires `three_match.replayed`.
Each sets only the new reflection flag `three_anevia_flour.reconsidered` and enters its own response before joining `shape`.
Neither rewrites the match outcome or silently changes another relationship.

The new standing-history response admits that a replay might have been worth losing without requiring Anevia to agree that her eight pins should have been discarded.
Her continued preference and teasing request about Olva keep her recognizable and personally invested.
The replay-history response lets the Commander reconsider the ruling while Anevia explicitly retains ownership of having agreed to the replay.
The shoulder contact and invitation to remain teammates make disagreement compatible with attraction rather than rewarding only agreement.
These are substantive additions to the available player stance, not two labels leading to the same apology.

The slate now gives each of the three names a score column.
The earlier confusing image of fitting the Commander beneath two already written women is gone.
The exact side or row relative to the opponents is no longer needed to understand what Irabeth does.
The coached-bread continuity fix and conditional `a_errand` callback remain intact.

This clears the requested writing corrections for this contribution.
The earlier cautions about occasional polished self-analysis and unrepresented native morale distinctions remain relevant when assessing the assembled route.
The score is not a full-route assessment, a meaningful-playthrough word certification, or approval of artwork, game execution, recovery, saves or ToyBox compatibility.
No source or game state was edited and no live-game behavior was tested in this rereview.

## Current revision follow-up

Rechecked source SHA-256: `532671B758991D367BC0DD6BDE5B8AC993B44C551887432054003D2312218FD1`.
The current bounded writing score is **90/100**, superseding the historical 88 below.
The same rubric now awards choices and consequence continuity 18/20; the other categories remain unchanged.
This does not meet the requested score above 90 and does not establish full-route readiness.

The baking-history correction is complete in the inspected source.
The lesson, shared loaf, return-game comparison and planned later bread now refer to this particular coached attempt.
The appended `old_crust` response requires `a_errand` and remembers the earlier black crust without claiming that event on a history that has not played it.
Its dialogue also advances Anevia's intention: she will ask Dalia when the bread is done and taste it herself before letting Beth rescue the worst piece.
The callback rejoins the existing match discussion without overwriting the recorded game outcome.

Two requested improvements remain in this revision.
`three_anevia_flour/motive` still permits only reaffirming the decision or confessing haste, so a sincere change of judgment remains unplayable.
`three_yard/mistakes` still describes fitting the Commander beneath two women already on a slate previously introduced with the opposing team's names, leaving the physical arrangement unclear.
The concrete remedies below still apply.
Neither finding means the played match outcome is being silently reset; they concern available characterization and readable staging respectively.

No source, exported story, installed mod or game state was changed during this review.
The historical inventory below applies to its original hash, not this revision.

## Original review retained for traceability

Reviewed frozen source SHA-256: `5D3E8405CC192236CEE796B623730814622057C66F830506A011F3D2CEAF696E`.
The scope is the six scenes in `storylines/tirabade_campaign.py`, compared with the original `story.py`, the existing shared outing, the author handoff and the independent canon report.
No source was edited.

The bounded writing score is **88/100**.
Voice and characterization earn 27/30, dramatic specificity 18/20, the three participants' attraction and agency 19/20, choices and consequence continuity 16/20, and prose/staging 8/10.
The target above 90 is not met at this revision.
The first-loaf continuity error and restricted reflection choice deserve correction before reassessment.
This is not a full-route score, a certification of individual word credit for both women, or approval of art, runtime contact, recovery or ToyBox behavior.

## What works

The disputed match is a useful adult disagreement because neither resolution supplies a conveniently flawless partner.
Irabeth wants opponents to feel able to challenge a powerful team; Anevia wants the keeper's ruling and her own account to mean something.
The uncertainty about the foot remains uncertainty.
Keeping the ruling wins the pennant and loses the immediate shared celebration; the fresh roll loses the match without requiring Anevia to admit a foul she denies.
Neither choice demands an apology from the person who preferred the other outcome.

The arithmetic is legible and consistent.
The explicit practice and coaching choices return in the match, although the technique choice is primarily descriptive because either technique scores six.
The later changed boundary and watcher address the actual practical problem instead of retroactively proving a wife wrong.
The second match ends in an ordinary loss that they can still enjoy.
That is a more persuasive resolution than another speech about trust would have been.

Irabeth actively chooses the game, wants to win, wants the Commander to notice her and admits that being wanted in her wife's presence pleases her.
Her response about wanting to pull the Commander from the lane is especially effective: it names attraction without turning her into a different person or making Anevia an obstacle.
Her guarded exactness remains recognizable even while her enjoyment becomes less guarded.

Anevia has a skill she wants for herself and a future morning she wants with Beth.
The sticky dough, washed hands, waiting and imperfect loaf give that desire time on the page.
She asks why the Commander made the match decision and states what hurt without asking them to adjudicate the marriage.
Her hand and waist contact give her separate attraction to the Commander a physical expression, while the loaf-sharing kiss preserves her marriage as a relationship happening in its own right.

The final map grants each person a destination rather than asking which wife should give hers up.
The intimate, quiet and limited-time endings all contain affection and a complete scene.
The later-promise branch actually honors the departure time instead of declaring tolerance and then narrating that the Commander stayed anyway.
No sexual explicitness is necessary to make the chosen night feel adult.

## Corrections requested

### Preserve Anevia's already played baking history

The original `story.py` scene `a_errand` already gives the Commander a piece of bread Anevia made, with a black crust and a respectable middle.
She says she paid for the flour and that Irabeth ate the worst piece while claiming to like it crisp.
This is not merely a native aspiration to bake someday; it is a played event in the existing authored campaign.

The new `three_anevia_flour/want` says she kept finding reasons not to make the first bad loaf.
`imagined` describes making a loaf and showing Beth as an unrealized first surprise.
Other new passages call this her first loaf, and the return game compares Dalia's rolls with Anevia's first loaf.
On a history that played `a_errand`, those lines reset her hobby and erase an earlier intimate memory shared by all three.

Present this as her first coached bakery lesson or first loaf under Dalia's instruction, not her first attempt at bread.
An actual callback would strengthen the scene: she can remember Beth praising the black crust and want an honest assessment of an improvement this time.
If `a_errand` is not guaranteed on every eligible history, gate that specific memory on its completion flag while using neutral new-lesson wording elsewhere.
Check all references through the return match and map, not only the opening sentence.
The private handoff's label that she is learning a hobby is compatible with prior attempts; the text's repeated first-attempt claims are the problem.

### Let the Commander reconsider the substance of the decision

In `three_anevia_flour/motive`, the two responses are that the Commander would choose the same again or that they were trying to end the argument quickly and should have taken more time.
The second assigns a motive rather than allowing changed judgment.
A player might have considered the decision sincerely and then change their mind after hearing what it meant to Anevia or Irabeth.
That player currently has to pretend the problem was haste, or double down.

Add a response appropriate to the actual recorded outcome: for a replay, reconsider asking Anevia to bear the cost of everyone else's comfort; for standing, reconsider how casually the Commander accepted the social cost of keeping the ruling.
Let Anevia answer without requiring agreement and without changing the recorded score.
This would deepen the strongest decision in the module rather than adding an unrelated alternative.
The existing standing-by-the-choice response should remain, because its refusal to manufacture guilt is valuable.

### Clarify the slate staging

In `three_yard/together`, Tessa arrives with three names already on the slate, apparently the opposing team's names.
In `mistakes`, Irabeth writes three names and leaves space between the Commander's and hers rather than fitting the Commander beneath two women already there.
The image briefly becomes hard to follow: the reader has just been told the existing names belong to the other team, and the metaphor about the two women does not describe a clear arrangement on the slate.
Say that Irabeth writes the new team's three names together on the empty side or next row.
The equal place in the relationship is already demonstrated by what they ask and do; it does not need an ambiguous layout metaphor.

## Coverage and literary cautions

The independent canon review's earlier baker-name collision and straightedge reference are fixed in this frozen source.
Dalia is now distinct from the Seelah module's carpenter, and the new line uses Irabeth's introduced straightedge.
I did not find a new material physical-staging contradiction in the affectionate scenes.

The prior canon report correctly limits morale coverage.
The same confident leisure and longer-future planning currently plays for the native broken and encouraged histories.
Pleasure is not proof of recovery, and a suffering Irabeth should not be barred from a good afternoon.
Still, the longer plan would benefit from a bounded acknowledgment of uncertainty where appropriate, particularly if this is later counted as native-outcome development.
Do not turn the map into evidence that an applicable native doubtful ending has been repaired.

Some explanations are unusually polished, particularly Irabeth's line about putting her own concern in Anevia's hand to roll down the lane.
Here the surrounding game, guarded admission and affectionate embarrassment give the language enough support that it does not become a major voice failure.
Future contributions should avoid making every disagreement end with each participant delivering a complete diagnosis of their own mistake.
The women are strongest when they tease, hesitate, disagree and return to an activity.

The new third-party characters have visible behavior rather than serving only as props for a lesson.
Nessa stays to acknowledge the roll when her teammates leave; Olva can retain her account while apologizing for discourtesy; Dalia continues teaching rather than becoming the marriage's therapist.
Keep those independent motives.

## Depth and approval limits

The six scenes give both wives individual attention inside one shared arc and return to the disputed event more than once.
They are substantial new material, but the whole shared game, map and three-person intimacy cannot be credited in full to each wife independently.
The author inventory's 7,265 raw words and 7,205 distinct-segment words are aggregate figures containing alternative choices and nodes, not one attainable campaign's length.
The 42,000 meaningful combined-word requirement, separate development for each woman and independent discipline reviews remain unmet by this contribution alone.
No score is assigned to unfinished artwork, native recovery, full-route outcome coverage or live integration.
An exact revised hash should receive another bounded writing review after the corrections; passing it would still not establish complete-route readiness.

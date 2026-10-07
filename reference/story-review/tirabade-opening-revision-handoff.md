# Tirabade opening and acquisition revision handoff

Status: author revision ready for independent review, not self-approved.
Scope is the original opening and early motivations, including their first aftermath.
It does not claim to resolve all findings in the 68-scene assembled review.
Only story.py and this handoff changed.
No shared story, package or development output was generated.

The revised story.py SHA256 is `EA53EAD43F546ECBC98F5167436630D75BE64104ACB1D6DE0A7C6DD1B9069033`.
The baseline story.py SHA256 is `67B223F31D4A8BC811878F92DCCBB4C9288CD65FA2232040F110D68E43892461`.
The source review is reference/story-review/tirabade-assembled-review-20260926-current.md.
Native evidence is reference/canon-dialogue.txt, SHA256 `E10DD05FA5D08FF7AFD3DB4700433EDD65160F46D6FDC69DA3BCD4131ED2AE2B`.

## Changed material

The opening now states that Anevia's leg has healed and shows her moving without favoring it.
Her request to be remembered for more than needing rescue remains.
The preceding page no longer implies that one hand is injured.
This addresses the review's reproduced Chapter 1 entry collision with native Anevia/Cue_0001 at the same answer list.

Anevia brings a small sleight-of-hand display to the landing meeting.
Her dropped coin turns her practiced nerve into flirtation she cannot quite control.
The following pages develop her enjoyment of provoking and surprising this Commander, and her curiosity about making the Commander lose composure in turn.
Her continued desire for Irabeth remains direct and physical.
She acknowledges that keeping her wife uninformed differs from having freedom to enjoy herself.
The text does not convert the secret affair into an agreed arrangement.

Irabeth's glove scene now develops pride, competence and an awkward wish to impress.
Her established marriage appears through a familiar private joke rather than another statement about being emotionally useful.
She initiates their next evening by bringing an ordinary board game, lays a small trap, and enjoys the Commander's attention to her challenge.
Her admission moves from competitive anticipation to wanting to touch the Commander.
The existing broken/encouraged branches, refusal, delay and friendship options remain unchanged.
The game is authored scene action, not an added skill check or a claimed native pastime.
No victory, player proficiency or reward flag is invented.

Irabeth's first aftermath and the joint reckoning now remember deliberate pursuit and the ease of concealment.
The scene keeps the hurt and mutual accusation.
It does not require either woman to renounce desire, and it does not explain an affair as a cure for an unhappy marriage.
Existing secret kisses, nights, refusals, admissions and consequences remain available on the same branches.
The negotiated path is unchanged.
No exclusivity or jealousy lock was added.

## Exact word delta

Counts use tools/measure-story-content.py's markup-stripped Unicode word rule.
This is raw changed-node prose, not newly credited unique aggregate route length.
Choice text is unchanged and adds zero delta.

| Node | Before | After | Delta |
| --- | ---: | ---: | ---: |
| a_cup/start | 81 | 78 | -3 |
| a_cup/leg | 94 | 98 | +4 |
| i_hands/useful | 83 | 85 | +2 |
| i_hands/ordinary | 104 | 102 | -2 |
| i_hands/tell | 64 | 87 | +23 |
| i_hands/end | 76 | 92 | +16 |
| a_roof/start | 92 | 134 | +42 |
| a_roof/want | 113 | 133 | +20 |
| a_roof/danger | 137 | 140 | +3 |
| i_respite/start | 91 | 113 | +22 |
| i_respite/still | 107 | 116 | +9 |
| i_respite/admit | 115 | 138 | +23 |
| i_morning/regret | 85 | 101 | +16 |
| reckoning/hurt | 112 | 150 | +38 |
| Total | 1,354 | 1,567 | +213 |

Fourteen nodes changed across six scenes.
All other prose remains unchanged.
The revision adds enacted activity rather than trying to expand the already passing aggregate length.
No full-route count or quality score is claimed for this source-only revision.

## Canon evidence and authored additions

Native World/Dialogs/NPC_Common/Anevia/Cue_0001 explicitly presents her recovered leg and confident movement during Chapter 1.
The prior reviewer inspected the archive condition, Chapter 1 etude and answer list `33960c7f7af40cd43b7f801a76c87a0b`, then reproduced the authored leg branch's availability with actual Rules.
That is the reproduced bug being fixed; this revision does not claim a new Unity reproduction.
The original probe and native records remain under C:/Users/Z/AppData/Local/Temp/tirabade-current-review-20260926.

Anevia/Cue_0011 establishes her criminal upbringing and learned dexterity.
Cue_0016 through Cue_0020 establish her love for Irabeth, their joint work and the central place of the marriage in her life.
The coin routine, its history as told here, her response to this flirtation and the affair motivation are authored developments.
They are not additional native dialogue or proof that canon Anevia would automatically choose an affair.

Native Irabeth/Cue_0030 establishes rebuilding the Eagle Watch with Anevia as an active professional partnership.
Cue_0047 names their wedding as her happiest day, and Cue_0048 names Anevia as her beloved and staunchest ally.
Her Lastwall and River Kingdoms account supports an experienced fighter with professional pride.
The glove joke, board game and attraction expressed through competition are authored developments built around that identity.
They do not replace the existing marriage or assert a recovered morale state.
Later violence, morale and Iz history variants remain outside this revision's scope.

## Verification and review request

Python parsed the revised source successfully.
An AST comparison that removes only node prose found the before and after syntax identical.
Both versions were also assembled with make_story() in memory, without invoking build().
The resulting 34-scene original-source payloads differ only in the listed 14 Text fields.
Every scene/node ID, choice text, Next, Set, Requires, Forbids, delay, ordering and other serialized field remained identical.
The full 68-scene assembled continuation was not re-exported here.
Root retains ownership of assembled-candidate generation and its checks.
Git diff --check passed.

The before source, per-node text snapshots and verification.json are in C:/Users/Z/AppData/Local/Temp/tirabade-opening-revision-nby_ax9e.
An independent reviewer should assess the new motivations, incoming and outgoing replies, native marriage fidelity and whether the distinct activity carries the romantic escalation.
The author assigns no scores and does not approve this revision.

## Review follow-up

The independent reviewer found two stale response joins in i_hands/tell and i_hands/end.
The tell page now ends on Irabeth admitting her habit of waiting for Anevia to ask, which the existing reply can call something she can change.
The end page now asks whether the Commander would like another meeting, restoring the existing answer "I would."
Only those two Text fields changed in this follow-up.

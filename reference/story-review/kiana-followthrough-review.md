# Kiana follow-through independent review

Reviewer stance: a skeptical continuity editor who asks whether choices are remembered as they were made and whether an activity earns its page count.
I did not author Kiana's contribution and changed no story source.
Initial review covered `storylines/kiana_followthrough.py` at SHA256 `6241DAAAC4447F443180E2B9A343A35477A511454AD18930A95DE22F80DC85BF`.
I subsequently verified the two corrections in final source SHA256 `C0EFDA58BBB848C758E46B1E17D175733C9E701EF89A486DE59C1B9D9077DC5C`.
Reviewed the current join and ending text in `storylines/kiana.py` at SHA256 `B2203669D965FE57CAA4566BB023072F089AD6672DB2D73FDEAA563CFF9F64A7`.
Also read `kiana_consequences.py`, the follow-through handoff, native Kiana aftermath dialogue, and the appearance adjudication and its cited unit chain.
This is a contribution review with selected assembly joins, not acceptance of the complete Kiana route.

## Assessment

Writing: 91/100 at the corrected final revision.
The initial revision scored 89/100 because of the two branch-history errors recorded below.
Native characterization and canon treatment: 92/100 within the inspected scope.
Both identified branch-history defects are resolved in the final inspected source.
I accept this contribution within the writing and native-characterization scope below; full-route approval remains withheld.
The scores do not certify gameplay implementation, full-route volume, native access, portraits, actual saves, or ToyBox behavior.

The contribution has sufficient dramatic activity to justify being longer than a sketch.
Kiana visits a friend, chooses the size of a reading, defends a favorite sentence, performs, receives an audience's interpretation, pays for work, and discovers a cost in the room she has selected.
The choices have later scenes attached to them.
The quiet room costs copying time; shared work brings usable ideas and interruptions.
The long speech retains two effective pauses after an unsuccessful third; the short speech works but leaves a comic quality she wants to recover.
Those outcomes are more useful than a good writing choice against a foolish writing choice.

Her humor stays personal enough to support the existing portrayal.
Taking a bite from a supposedly unnecessary loaf, threatening that a reader may remind her of a mistake only after she has eaten, and resenting a repeated bill at the door are specific reactions.
The writing does sometimes give every inconvenience an immediately polished joke, especially through the furniture/copying sequence.
That is an editorial pressure to watch in the assembled route, not a request to pad this batch with a crisis.

## Findings and verified corrections

### 1. `kiana.last_page.end` gives the long-speech route the cut route's discarded sentence

The `cut` node explicitly copies the staircase sentence onto a scrap and puts it beneath the pin.
The `keep` node instead retains the speech, marks pauses, and decides to perform it with the third image present.
Both flow to `end`, where she retrieves the staircase sentence before disposing of discarded strips, then leaves the surviving sentence under the pin.
That cleanup silently imports the cutting branch's physical artifact into the keep history.

Fix by gating the cleanup to the actual selected speech, or by using common cleanup that touches only discarded strips without identifying the retained staircase sentence as one of them.
The long version must remain on the script for its performance and subsequent revision.
The short version can keep the saved scrap without needing to mention it again in common narration.
Do not change either choice's consequence merely to make the common cleanup easier.

Verified correction: final `last_page.end` checks discarded strips against retained pages, discards only unwanted paper, and places the brass pin over retained work without identifying a staircase scrap.
The cut branch still preserves its explicitly saved sentence, while the long branch retains the performed speech.
This resolves the reported artifact mismatch.

### 2. `kiana.ink_after.long` credits the Commander with advice they did not choose

This node requires `kiana.follow_long_speech`.
That flag is set by the Commander recommending that she keep the long speech and make its pauses work.
After the third pause fails, Kiana tells the Commander they may look vindicated, and narration says they oblige her.
The current path makes the player congratulate themselves for a warning they did not give as their chosen recommendation.
The earlier general criticism in `last_page.read` does not override the later explicit decision to try the longer performance together.

Replace that exchange with acknowledgement that both chose the experiment and that hearing it has changed her judgment.
She should still keep the first two pauses, remove the third image, and refuse to regret having tried it.
This preserves the branch's useful mixed result without rewriting the Commander's position.

Verified correction: final `ink_after.long` recalls both being pleased with the speech in a room of two, then recognizes that their sympathetic rehearsal did not predict the larger audience.
The first two pauses still remain, the third is cut, and Kiana still values the experiment.
There is no vindication claim or forced player self-congratulation.
This resolves the reported choice-history mismatch.

## Branch history, relationships and agency

`bakery_stairs` correctly follows the prior invitation instead of putting Elan at the table by assumption.
On separated histories Kiana arranges a separate afternoon, does not know whether Elan accepted his own invitation, and does not treat his friends' welcome as his approval.
The waited and affair branches remain different.
The affair branch takes responsibility for the kiss without inventing an abusive or uncaring husband to justify it.

The widow branch recalls the table incident from the preceding contribution.
It requires both the authored bereavement history and actual native Elan-death alias.
Its fond irritation and sudden laugh leave the deceased relationship real, rather than using grief as a romance obstacle that this scene removes.
No Elan body or new native contact is supplied by the scene.

The prior `moon`/`guest` choice has explicit script callbacks in `last_page`.
The quiet/comic entrance flags have performed consequences, and the absent-stagecraft case has an ordinary entrance.
The comic chair snag is an adaptation of the earlier shelf snag, not a claim that a shelf must exist in the new room.
The selected Commander-versus-Edris guest role remains intact in the performed sequence.

Kiana selects the larger reading or workshop after hearing a suggestion; she does not become successful because the Commander commands the audience to admire her.
The workshop has six comments and costs pastries, while the larger reading nearly covers its modest costs.
Neither finances a self-supporting career or produces instant fame.
Kiana's money, room choice and copy payments remain her own narrated arrangements.

Commitment is read rather than created by the later scheduling conversations.
An uncommitted visit remains a particular evening rather than an implied postwar promise.
The last market and music choices are accurately called intentions, with explicit room for a later discovery scene.
They must not be counted as delivered dates.

The private intimacy is mature, chosen and non-graphic.
The ink-mark passage works because it connects desire to a specific moment of physical closeness without rewarding work with affection.
The alternative is an actual walk and food, not punishment for refusing a kiss.
The later choice to stop writing or finish the page receives a distinct practical outcome and then the same opportunity for company.
The module does not set another relationship closed, demand exclusivity, or alter ToyBox settings.
That source observation is not runtime compatibility approval.

## Canon and the current ending joins

Native aftermath `ElandKianaAftermath/Cue_0006`, GUID `a819e8c85ef23324bb0d8117bb9d7df3`, presents an affectionate marriage with Elan away on crusade.
`Cue_0007`, GUID `df45181e1968f26459f9e8bc2b995a34`, supports frank humor about adult desire and the disrupted wedding night.
`KianaAloneAftermath/Cue_0001`, GUID `aebbc1845e827dd4da4e28014e7b4162`, establishes the distinct widowed outcome.
These support aspects of voice and history; they do not establish that native Kiana became a playwright or separated from Elan.
Those remain explicit authored developments.

The supported oread unit is `180b0eaa5dce387458d2ebf0ee943985`.
The pale crystals in the final scene are compatible with the current appearance adjudication.
The vampire princess remains a fictional performance role and does not imply real undeath, a race change, or a transformation after soul recovery.

The parent's current `farewell.plans` now proposes work on a next draft and another reading.
This works after the new reading and after only the older private rehearsals.
It no longer claims that a played first reading remains wholly in the future.
The mention of asking Arsinoe is an intended introduction, not a claim that the new module has acquired a verified native Arsinoe actor.

The revised together/bereaved endings explicitly progress beyond readings to scenery and costumes.
They remain plausible whether this optional batch was played or skipped, because the prior route already includes private readings.
The revised apart ending retains and later changes the pages without asserting that no earlier performance happened.
I found no remaining contradiction in these inspected revised statements.
Specific workroom and new discovery-wish callbacks remain opportunities for the full ending pass; their omission is not evidence that these six scenes never happened.

## Gameplay and full-route limits

The batch currently delivers a linear sequence of remote books with branching dialogue consequences.
It does not supply a playable venue search, native skill roll, placed invitation object, spatial investigation, or check-dependent recovery.
The author handoff accurately distinguishes proposed checks from implementation.
A correct branch simulation cannot raise that gameplay scope to the user's requested original-game acquisition and exploration standard.
Native delivery, meaningful failed checks and non-roll alternatives remain implementation work.
Successful checks must not award Kiana's affection or erase the chosen long/short speech consequence.

No independent runtime or managed construction test was run for this review.
I inspected the actual node text and conditions, including both defective histories, rather than treating the author's traversal total as prose verification.
The isolated module's inventory and possible path lengths are not proof of the whole route's minimum meaningful length or attainable campaign depth.
The old farewell is still reachable without this optional batch, so the assembled route needs an intentional decision about progression rather than simply adding aggregate words.
Full Kiana approval remains withheld for amount, overall progression, exploration/check gameplay, mythic access, art, independent technical review and actual game/save verification.

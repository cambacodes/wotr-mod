# Seelah late-campaign independent rereview

Reviewer stance: a skeptical scene and continuity editor, independent of this contribution's author.
Initial rereview source was `storylines/seelah_late_campaign.py`, SHA256 `AD60828FA02270F9D91F480B3E31E07B9F76957B039C5BAA8C8240232FFA604A`.
The final inspected source is SHA256 `F0D2B57D28012A4A03D8191AC132DCD9078D2C58F18591ED30D145D21D1797F0`.
Only this rereview report was written.
I read the initial review, revised module and handoff, the earlier aftermath's native-outcome and Elan passages, and supplied native Seelah and branch evidence.

Bounded writing assessment: 91/100.
Bounded canon compatibility assessment: 91/100.
The initial review's material findings are resolved, and the additional continuity error identified during this rereview is corrected in the final source.
No remaining contribution-level writing blocker was identified.
This accepts the inspected contribution within those disciplines, not the complete Seelah romance, art, actual gameplay execution, or release readiness.

## Verified revisions

`late_lesson/fixed` now shows Istra take the smaller shield and brace its lower edge against her leg.
The later participant's praise in `late_lesson/answer` therefore refers to something actually demonstrated on both teaching arrangements.
The two departures remain different: rehearse one memorable movement on the way to the exit, or hear what the participant retained and discover another misunderstanding.
The correction preserves this practical feedback rather than making the answer generic.

`late_course/fixed` replaces its professional self-analysis with selecting a specific hour, wanting practice, and worrying about Tavia learning another trick.
`late_lesson/after` admits enjoying the display, jokes that Istra had been correcting her since the barrel, and asks for another run.
`late_afterglow/victory` remembers the successful turn and the Commander's look, then asks for closeness.
Those changes give Seelah things to do and want without explaining the episode's thesis again.
The booklet remains the primary place for sustained reflection on grief, unfinished rescue and future questions.

The revised morning performs washing, dressing and the dropped-boot joke without explaining that the scene is not a domestic performance.
The keepsake scene shows the cup moved to make room and her pleasure on reopening the cupboard.
The final goodbye now contains a practical next-race suggestion and an ordinary request not to be late.
The former narration praising its own restraint has been removed from these identified passages.

Breva is now introduced in `late_course/runner` as well as the spectator branch, before she appears as a known competitor at the race.
`late_afterglow/start` explicitly says the meeting takes place on a later evening.
The shirt is washed and brought for mending, which supports a separate visit rather than silently resuming the race afternoon after a delay.
The later references to the afternoon and its tune can now be read as memories of that established event.

`late_first_step/start` is neutral about whose activity is next.
On the music branch the Commander still chooses and shows the gathering.
The parcel is introduced beside the cupboard only on that branch.
The rented cupboard remains temporary storage rather than an accomplished permanent shared home.

During rereview I found one further prop-history error: `late_afterglow/night` explicitly rubs the finger chalk away, while the former `late_first_step/end` later described the same mark as still visible.
The parent removed that retained-mark claim.
In the final source Seelah looks toward the yard and proposes running the course backward next time.
This works after the night, kisses or quiet-company branch and avoids another explanation of what the parting symbolizes.

## Voice, attraction and consequences

The revised Seelah is competitive, funny and occasionally impatient with herself.
She wants the race to go her way and does not pretend that losing proves she never cared about winning.
The losing song develops attraction through looking at the Commander in front of other people.
The private scene remembers that particular look rather than awarding a standard flirtation for clearing an activity.

The shield sequence keeps her competence while allowing Istra's different body and experience to change the teaching.
Her decision about lesson arrangements also leaves a cost in the amount of practice she later describes.
The writing does not falsely claim that this difference currently changes the numerical race check.

The booklet still contains articulate passages, but they no longer dominate every surrounding interaction.
The concrete grief sentence about missing disagreement with Elan is stronger than a generalized conclusion about moving on.
An unsent living-Elan draft leaves his whereabouts and response unasserted.
The incomplete-rescue branch continues to name unfinished work and does not invent a rescue result to justify a pleasant afternoon.

The adult intimacy remains voluntary and graphic and explicit.
The private question supports a night, kisses alone, or company without further intimacy.
The quiet answer completes the evening and future invitation rather than reducing affection or demanding that the player make up for refusal.
The existing commitment is read when discussing future plans, not created by the race or by renting a cupboard.
A committed player can still discuss the shape of that commitment; an uncommitted player is not silently promoted into one.

## Actual check wiring and its limits

I inspected the imported authoring data and ran a focused, read-only walker through both check targets and the subsequent private evening.
The close-turn choice is at `late_race/running` index 0.
Its direct Next is absent; its Check uses `SkillMobility`, DC 26, Success `narrow`, Failure `stumble`, and CommanderOnly true.
The attempt sets only `seelah.late_close_turn`.
It does not pre-award victory, failure, a kiss, love, commitment or scene completion.

The success page describes a successful planted turn and hoop placement, then its continuation sets `seelah.late_race_won`.
The failure page describes slipping on grit, catching balance against the barrel, and reaching the peg after Breva.
It does not pretend the Commander selected the wide route.
Its continuation sets `seelah.late_race_lost` and `seelah.late_race_stumbled`, then reaches the losing song.
Neither version gives a native injury or changes another romance.

The focused walk confirmed exclusive win/loss flags, no `late_wide_turn` on either attempted close-turn result, and preservation of an unrelated Kiana commitment marker.
Both results reach the subsequent quiet-company choice without setting `seelah.kissed` or `seelah.committed` on that path.
The existing careful wide finish remains choice index 1 and supplies a non-roll loss with clean footing.
Watching remains a non-roll option, although its result is still narrated rather than a player-controlled judging activity.

The handoff gives native chapter-5 checks as calibration references and calls DC 26 an authored decision.
That distinction is appropriate.
I did not independently extract those check blueprints or test success probabilities with a real Commander during this editorial assignment.
A readable authored Check object and traversable outcomes do not prove the Unity roll, skill modifiers, UI, persistence, rewards or retry behavior.
The parent separately reports production Rules coverage; this report does not present that reported run as an independently executed runtime test.

## IDs, canon and assembly boundaries

Current inspection confirms the existing close/wide choice order and the separate appended failure node.
The handoff records preservation of the other original scene/node IDs, prerequisites and choice indices.
I did not have the original `124D236...` source bytes available for a full historical structural diff and therefore do not independently certify every old identifier from that claim alone.
Integration should retain the repository's stable-ID checks and never regenerate old IDs from the revised text.

Supplied native evidence supports Seelah's warm directness, practical courage, enjoyment of companionship, objections to cruelty and uncertainty after failures involving her friends.
The surviving source's insistence on completing the soul rescue and her different native future outcomes are not erased by the new plans.
The relay, Istra's lesson, the rented room, guests and cupboard are authored developments, not recovered native events.
No new knightly order is asserted by these scenes.
The broader lawful career outcome and living friend encounters still require their own treatment.

The module is attached to Seelah's native dialogue and uses chapter-5 Drezen restrictions with death, departure, transformed-path and farewell exclusions.
It is not a remote rest-triggered module.
Narrated visits do not establish placed yard actors or encounter objects.
The broader discovery requirement still needs native locations, usable invitation or quest progression, and meaningful exploration beyond the book scenes.

The six optional scenes remain a contribution to an incomplete route.
Their aggregate words and selected-path estimate do not prove the 21,000 meaningful-word requirement or full attainable campaign depth.
Earlier road/farewell progression can bypass the batch, which requires an intentional assembly decision and full-route review.
Missing full-route work includes broader native friends and career coverage, earlier consequences, attainable Trickster access for missed/departed contact, appropriate transformed routes, developed endings, finished art and game/save/ToyBox verification.
No complete-route or runtime approval is granted here.

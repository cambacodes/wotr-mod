# Aranka two-scene continuation independent review

I independently reviewed the two added scenes `the_story_that_follows` and `the_morning_without_audience` in `storylines/aranka_continuation.py`.
The source read during this review had SHA-256 `400594C71651A006B09BE3967D0958376B5E31D4F91B08F7C5E3A8D60391FBD9`.
This is a bounded review of the two additions, not approval of the assembled Aranka route, its implementation, or its readiness for play.
I cross-checked the earlier six-scene review and the native Aranka evidence recorded in `reference/canon-review/aranka-extension-evidence.md`.

The new material is promising and mostly recognizable as Aranka, especially when it treats the Commander's reputation as a pressure on her work rather than as a shortcut to her affection.
It needs revisions before these two scenes should pass a strict independent quality gate.

## What works

At lines 507-525, the spreading moon story creates a concrete conflict about authorship, public memory, and the Commander taking up too much space.
Aranka's objection at lines 522-525 is appropriately specific: the Commander cannot absorb the cost of appropriating her song by offering to take blame, because the story still uses her voice.
Her line asking the Commander to ask before turning the song into bait makes consent apply to the proposed Trickster scheme, not just to physical intimacy.
That is a credible authored Trickster complication and does not claim that this incident is native canon.

The alternate responses preserve distinct attitudes toward fame and correction.
The cooperative game at lines 526-534 requires Aranka's participation and gives her terms, while the restraint answer at lines 535-540 lets the Commander decline the trick without requiring a second apology.
The ordinary answer at lines 541-546 recognizes that she cannot spend her life correcting every retelling.
These branches suit the earlier route's music-making activity and travel-oriented future.

The flirtation is adult, reciprocal, and graphic and explicit.
At lines 558-569, Aranka expresses desire in direct language and the scene gives the Commander options for intimacy, travel, or both.
The morning conversation at lines 586-612 usefully distinguishes love from possession and fame from being known.
This connects the Commander's public power to a relationship-specific problem instead of declaring all Trickster behavior harmless.

The canon boundary is largely respected.
The preceding continuation review documents native Aranka evidence for musical encouragement, travel, irreverence, and independent judgment, including DesnaAdepts cues 0005, 0022, and 0034 and MusicVsMusic cue 0001.
The two scenes extend those traits through invented travelers and an invented song rumor, without presenting those events as recovered game facts.
The existing evidence also establishes that the island encounters continue an already earned romance, so these scenes appropriately do not pretend to be a new acquisition route.

## Revisions required

1. Make the Trickster bargain's truth boundary explicit in the public performance.
At lines 528-534 Aranka agrees to a ridiculous version on the terms that she gets the last word and that the listeners may decline it.
At lines 547-551 the pair performs the moon version and then the actual refrain, but the dialogue never clearly labels the first version as an admitted fabrication before the travelers hear it.
Because the conflict is about a false story being repeated as fact, have the Commander or Aranka introduce it openly as a made-up comic version, then give Aranka the uncontested final correction.
Otherwise the payoff risks repeating the harm the scene says the couple has agreed to avoid.

2. Do not route every ending into a morning that implies an overnight encounter.
The first scene offers distinct terminal states at lines 566-582: an overnight private encounter, a kiss-only encounter, and an open-ended future road invitation.
The morning scene begins from the shared `aranka.after_story_kept` gate at line 585, with no check of `aranka.after_story_private`, `aranka.after_story_kiss`, or `aranka.after_story_road`.
Its opening at lines 586-590 describes a morning-after setting with tangled hair, separated boots, bare feet, and a night whose outcome is still unsettled.
That is plausible only for the overnight branch and can imply more intimacy than the player chose on the kiss-only or road branch.
Use branch-specific opening nodes keyed to the actual terminal choice, or make the second visit a neutral later check-in with no assumed overnight setting.

3. Give the second conversation a consequence beyond reassurance.
All three opening answers at lines 592-594 proceed directly into validating dialogue and an affectionate terminal state at lines 595-612.
The branches do not currently challenge a response, change their plans, or produce a visible cost when the Commander gives a confident but insufficient answer.
Aranka should retain the right to reject a promise as too easy, ask for a concrete boundary or plan, or defer the next meeting if the Commander's answer does not satisfy her.
This will keep her from becoming agreeable simply because the scene needs to continue and will make the theme of separate agency playable.

4. Decide whether the new flags are durable route consequences or only records.
The first scene writes `aranka.story_game`, `aranka.story_restraint`, `aranka.story_trickster_chosen`, `aranka.story_trickster_refused`, `aranka.story_left_alone`, and `aranka.story_repaired` at lines 526-557.
The second scene writes distinct intimacy and future-choice flags at lines 570-582, and both scenes set `aranka.extension_kept`.
I found no reads of these new branch-specific flags elsewhere in the current source, so they do not presently alter later dialogue or route availability.
That is acceptable as a draft boundary if later scenes will use them, but the integrated route should either consume them in callbacks or avoid presenting them as persistent mechanical consequences.

5. Tie the new personal conflict to a meaningful development in the ongoing relationship.
The two scenes end with affection, a possible night, and broad promises, but they do not yet show what Aranka changes, chooses, or risks because of the exchange.
One specific future-facing action would give the dialogue a stronger payoff, such as Aranka deciding who may tell the song, choosing whether to travel with the Commander for a defined interval, or setting a later conversation about the public story.
Keep her artistic career and independent travel alive in that outcome rather than making her next activity another private meeting with the Commander.

## Scope and conclusion

These scenes make useful progress on Trickster characterization and mature relationship dialogue, but the shared public lie payoff and the unconditional morning-after setup need correction.
The second scene also needs a sharper player-facing consequence so its boundary discussion changes what happens next.
This review does not certify word-count parity, a complete route, universal Trickster attainment, score thresholds, art, runtime integration, ToyBox behavior, save compatibility, or in-game presentation.
Those remain separate project gates, and these two scenes alone cannot establish that Aranka is ready for manual playtesting.

# Tirabade campaign contribution review

Reviewed the six scenes in storylines/tirabade_campaign.py at SHA256 B55BBA8440BD870DB6E91FF838B1BD69123D49A93CD258A9B4978780F5DB63B6 and the corresponding parallel handoff.
Compared the native dialogue in reference/canon-dialogue.txt, the existing morale-aware private conversation, and the shared relationship and owner-access rules.
The acceptance constraints in development/parallel-work.md apply unchanged.
This is an independent review of the delivered passage, not acceptance of the complete triad route.

## Concrete corrections

The baker in three_anevia_flour is named Mera.
The parallel Seelah contribution already introduces Mera as a carpenter with a workshop and washing-platform job.
The authors did not intend a shared character, and the combined export would give readers reason to infer one.
Rename the baker consistently in introductions, subsequent dialogue, the purchased-roll callback, and the handoff rather than accidentally merging the two characters.

three_return_game.start states that Irabeth brought the straightedge.
three_return_game.line calls it Perrin's straightedge without introducing a second tool or a change of ownership.
Use the established straightedge or explain the substitution.
This is a small prop-continuity correction, not a native-lore issue.

## Separate agency and attraction

Irabeth chooses the yard and openly wants to win.
Anevia chooses to participate because she enjoys seeing that side of her wife, then develops a distinct wish to perform well herself.
The match disagreement gives both women reasons beyond pleasing the Commander.
Irabeth worries about rank distorting an ordinary contest; Anevia objects to treating an unsupported accusation as sufficient to erase her score.
Both accept either team decision before asking the Commander to choose.
The Commander therefore resolves an agreed team question rather than being granted authority over their marriage.

The selected result has a cost which later scenes preserve.
Keeping the score wins the pennant but loses the shared congratulation; replaying loses the match and leaves Anevia hurt even though she consented to the replay.
The return game does not retroactively decide where her foot was.
Its clearer boundary and agreed watcher are practical changes, not proof that one wife had been morally right about every part of the dispute.
The arithmetic is consistent: seven plus six plus eight wins against twenty, while the replayed six produces nineteen.

Irabeth's individual conversation concerns her ambition, pleasure, unease about rank, and attraction to the Commander.
She also describes her own imperfect discussion with Anevia instead of recruiting the Commander to obtain an apology.
Anevia's separate scene gives her a hobby she wants, room to retain disagreement, and an opportunity to ask about the Commander's motives.
Her explicit refusal to make the Commander adjudicate the marriage is supported by the scene's actual choices.
Both individual scenes can precede the other without requiring its private conversation to have occurred.
The joint return pays off the Commander's separate answer to Irabeth while continuing affection between the wives.

The women kiss and attend to one another independently of the Commander.
The Commander receives direct, chosen affection from each, including an optional Irabeth kiss and Anevia's private hand or waist contact.
The final map scene preserves both women's desired destinations and includes the Commander's preference without replacing either wife.
The intimate night is graphic and explicit; quiet company and leaving for another promise remain complete alternatives.
No answer purchases intimacy by arbitrating the marriage correctly, and no outcome punishes another relationship.

## Native characterization and authored adaptation

Native Anevia/Cue_0001 describes her recovered mobility and alert observation of threats after the initial injury.
Playing ninepins does not impose a permanent disability or treat that old injury as a joke.
Her attempts to read the boards, irreverent teasing, and practical flour mishaps are compatible with a skilled scout being a novice at something else.
The quip about her first lock is new anecdotal detail supported in broad character terms by the native criminal childhood; it is not a recovered native event.

Anevia/Cue_0077 explicitly places the dream of a home stone oven and learning to bake after the war.
Cue_0084 and Cue_0085 link bread to remembered safety and its value during dangerous work, and Cue_0086 continues the peaceful domestic aspiration.
The new lesson acknowledges that she used to postpone the desire and now wants to practice, while still wanting the future morning with Beth and her own kitchen.
That is a deliberate authored development of the aspiration, not a claim that native Anevia already took this lesson or that the postwar dream has been fulfilled.
One imperfect loaf leaves room for the larger aspiration and does not turn her into an accomplished baker overnight.

Threshold IrabethAnevia/Cue_0015 contains Anevia's wish to take Irabeth on her first vacation.
The map scene plans possible travel without claiming that the holiday has already happened or can safely occur on a specified date.
The garden and market preferences, borrowed civilian map, and proposed boat trip are authored inventions.
They do not invent a canon destination, completed quest, or actual detour away from military duties.

Irabeth's concern about authority, careful language, and less guarded competitive pleasure remain recognizable.
Her attraction and humor are not treated as evidence that she has abandoned duty or become another version of Anevia.
The new supporting players and baker are adult civilian inventions rather than disguised native quest actors.
The shared affection preserves the existing marriage while developing the expansion's consensual triad premise.

## Morale coverage and limits

Native Threshold Cue_0016 gives Irabeth a laughing acceptance of the vacation prospect, while Cue_0017 gives a doubtful response tied to survival and a wish to hang up her sword.
The existing route also distinguishes broken and encouraged in i_private rather than treating kindness as a cure.
The new six-scene module reads neither morale flag and supplies the same confident leisure, individual reflection, and future planning in both histories.

A good afternoon, a laugh, or a desired kiss does not by itself contradict a history of trauma or doubt.
The draft never explicitly states that her native morale has been repaired and changes no morale state.
I therefore do not label its enjoyment an automatic canon contradiction or recommend excluding a suffering character from affection.
However, it cannot count as delivered morale-specific development.
Before claiming full native-outcome coverage, add or verify a bounded acknowledgment of what hope means in the applicable state, particularly around the map's longer future and the individual's wish to be good at something.
Retain pleasure without implying that a run of pleasant scenes overrides the native doubtful outcome.

## Access and assembly boundaries

The helper requires three_outing.kept and kept_terms and restricts all six scenes to Drezen in Chapters 3 or 5.
It forbids closed, loss, inhuman, both away flags, and last_watch, including on the individual scenes that later physically involve the other wife.
The shared relationship registry additionally excludes either spouse's death or departure, Swarm, and true Lich.
Main.cs derives loss from the existing death, gone, and sacrifice flags; those protections must remain intact at integration.
The normal owner rules attach Together entries to the two existing roots and individual entries to the corresponding woman's root.
The module does not restore missing actors, alter native morale, or supply bespoke Trickster recovery.

The narration's fees, prize, bread, map, and named civilians are book-event details, not inventory transactions or world-state changes.
The stronger civilian arc remains optional and does not prove that an ordinary campaign necessarily plays it before later conclusions.
The author's reported graph traversal is useful but is not Unity execution or actual save persistence.
I did not independently run the production rule suite or inspect the rendered book pages in this review.

## Bounded disposition

The six scenes substantially develop both women as people and lovers, with a disagreement that survives an immediate choice and changes later conduct.
No material fresh-path canon contradiction was found in the leisure, baking, or planned-vacation premise.
Correct the cross-module name collision and straightedge reference before closing this continuity pass.
Native morale differentiation remains an incomplete coverage area rather than a repaired outcome.
No full-route percentage or release approval is assigned.
The 42,000 meaningful combined-word requirement, distinct depth for each woman, finished art, attainable Trickster access, appropriate mythic boundaries, and actual game/save verification remain separate unmet or unverified gates.
Shared and alternative passages must not be counted twice or used as a substitute for attainable campaign depth.

## Corrected frozen revision

Verified the corrected source SHA256 is 5D3E8405CC192236CEE796B623730814622057C66F830506A011F3D2CEAF696E.
All 19 source references to the baker now use Dalia, with no Mera reference remaining in this module.
The separate Seelah carpenter therefore no longer shares an unintended identity with the baker.
The return game's line node now uses the straightedge Irabeth brought, matching its introduction.
Both concrete continuity corrections identified above are resolved.
The bounded textual disposition applies to this corrected revision, with no remaining material fresh-path canon contradiction identified.
The morale-coverage limitation and complete-route acceptance limits remain unchanged.

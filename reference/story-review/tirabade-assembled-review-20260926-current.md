# Current assembled Tirabade review

Reviewed on 2026-09-26.
Verdict: the doubled aggregate length requirement passes, but the assembled manuscript needs revision before it meets the strict above-90 quality requirement in every discipline.
This is a substantial romance campaign, not a short draft.
Its strongest material is the wives' mutual attraction during the civilian outings and the consequences that survive their disagreements.
Its weakest material is the repeated explanation of relationship principles, the parallel early affair motivations and insufficient response to important native histories.

## Snapshot and reading scope

I read all 68 current Tirabade scenes, including all 485 nodes and 714 choices, rather than only a favorable selected path.
I also read the actual independent-route spouse agreements, first open romantic evenings and separate continuation invitations needed to assess the joins.
Those independent scenes receive no additional word credit here.
I read the older assembled review, checked its complaints against the current text and did not inherit contribution approvals or scores.

The source is the shared 538-scene `development/Story.json`, SHA256 `8DCEB83D44925E5C07C7407D1FCEABE9381CE147D9A862B22E4E88420583C300`.
The ordered 68-scene Tirabade subset, serialized with sorted keys and compact separators, hashes to `71BBA019FC1FF02036C35248F2F2D94BFEE4DE4645127DE9BE13AC47A5C705DD`.
The source rules used for the focused reproduction hash to `4442C5D543C46D8B3A6744448ED03B92E7A7BB463BDECF09749CA9B5DCB1E889`.
Native dialogue was read from `reference/canon-dialogue.txt`, SHA256 `E10DD05FA5D08FF7AFD3DB4700433EDD65160F46D6FDC69DA3BCD4131ED2AE2B`, with the opening greeting's actual archive data inspected separately.
Temporary snapshots, per-scene reading exports, selected traces and the focused reproduction are under `C:/Users/Z/AppData/Local/Temp/tirabade-current-review-20260926`.
No story, source, runtime asset or shared export was edited.

### Later export identity check

After the 585-scene export was installed, I compared its ordered Tirabade subset with the original reviewed 538-scene snapshot.
Selection used `scene.get("Relationship", "tirabade") == "tirabade"` in both files.
All 68 scene objects are identical, including their nodes, choices and metadata.
Their sorted-key compact serialization still hashes to `71BBA019FC1FF02036C35248F2F2D94BFEE4DE4645127DE9BE13AC47A5C705DD`.
The later full export hashes to `780BDC23146431CECD7F1ED9594B5F129C5E149DB535CC40F2BD128A2126647A`.
This establishes that the literary findings apply to the same Tirabade content in that later export; it does not change the original snapshot or review verdict.
Unexported author revisions require a separate review.

## Length without double credit

The repository's existing counting rule strips markup and counts Unicode words with internal apostrophes.
Titles, entry labels, native text and parent-mod text are excluded.
Exact normalized whole segments are credited once across the trio, regardless of speaker or repeated placement.

| Measurement | Words |
| --- | ---: |
| Raw prose and choices | 55,773 |
| Raw prose | 50,203 |
| Raw choice labels | 5,570 |
| Distinct normalized prose and choice segments | 51,186 |
| Exact repeated-segment credit removed | 4,587 |
| Distinct prose alone | 46,551 |
| More aggressive normalized line deduplication, prose and choices | 50,730 |
| Required doubled planning floor | 42,000 |

As a conservative additional check, I removed the nine new `tirabade.*` bridge/ending scenes and the appended honest-request, local-goodbye, separation and negotiated-history variant nodes from the original 59-scene inventory.
That reduced inventory still contains 46,610 distinct prose-and-choice words.
The route therefore does not rely on repeating the same separation conversation at several entry points to cross its floor.
These are counting diagnostics, not estimates that every word is equally valuable.
The full reading supports a pass on meaningful aggregate volume, with room for a substantive editorial trim rather than another volume expansion.
Shared content is counted once; neither wife's separate full campaign is added to this total or used to claim a second pass for the other wife.

I verified the installed DLL, localization and readme hashes against `reference/art-review/ran-route-word-inventory.json`.
The largest listed distinct parent aggregate is Targona at 18,359 words.
Twice that is 36,718; the project's 42,000 floor is stricter.
The inventory's conservative upper accounting for unallocated localization is also below 21,000 per route.
This does not establish the word count of a selected parent playthrough or prove superior writing.

I reran the existing selected-path tool against the frozen current snapshot.

| Compatible source sequence | Selected words | Scenes including one ending |
| --- | ---: | ---: |
| Developed legacy route with Abyss material | 28,824 to 32,723 | 47 |
| Short promised route with Abyss material | 9,598 to 12,108 | 27 |
| Chapter 5 legacy start, developed route | 27,987 to 31,644 | 44 |
| Short farewell, explicit catch-up, developed ending | 29,214 to 33,007 | 49 |
| Honest parting sequence | 6,958 to 8,985 | 19 |
| Negotiated shared continuation after earned solo agreements | 24,359 to 26,942 | 34 |

The last row begins with the two lover states and two marital agreements supplied as explicit entry fixtures.
I inspected their actual producing scenes, but that row is not a fresh acquisition proof or a count of the separate campaigns.
All ranges assume living, available wives, sufficient waits and the specified chapters and locations.
The tools count visited nodes and chosen answers, not every unused alternative in a player's path.
The 42,000 requirement is the agreed aggregate floor, not a newly imposed minimum for every playthrough.

## Required corrections and editorial work

### 1. The opening leg conversation contradicts its native entry

At `a_cup/start`, the Chapter 1 choice asking about Anevia's leg reaches `a_cup/leg`.
That page describes cautious testing before bearing weight, movement costing effort and people repeatedly asking whether it hurts.
Native `World/Dialogs/NPC_Common/Anevia/Cue_0001.jbp` instead describes no sign of injury, confident use of the previously broken leg and her ability to run, jump or dance.
Its actual archive condition is Chapter 1 playing, and its next answer list is `33960c7f7af40cd43b7f801a76c87a0b`, the same list used by this expansion's Anevia scenes.
This is a source-supported collision in the same conversation, not a demand that old injuries can never be remembered.

I reproduced the authored branch's eligibility using actual `Rules.Available`, `Rules.Match` and `Rules.EntryTargets` in an isolated .NET harness with a fresh Chapter 1 state.
The native greeting's archive record and Chapter 1 etude record are saved alongside that probe.
This was the closest available headless reproduction of the entry sequence; I did not launch Unity.
Revise the line to acknowledge her recovery while retaining the useful boundary about being remembered as more than a rescued person.
An active-injury version would require a genuinely earlier, verified entry context.

### 2. Early desire is too similarly explained for both women

`a_roof/danger` explains Anevia's attraction through being seen without someone waiting for information.
`i_hands/useful`, `i_respite/admit`, `i_morning/regret` and `reckoning/hurt` repeatedly explain Irabeth's attraction through being wanted rather than useful.
Both courtships progress through quiet relief from work, an admission of wanting, praise of the existing marriage, a knowingly concealed encounter and a carefully articulated regret about the lie.
The individual phrasing differs, but the dramatic cause and rhythm remain too close.

Native Anevia's account of Irabeth as the meaning of her life and native Irabeth's account of their wedding as her happiest day make casual simultaneous infidelity a demanding alternate development.
The current text preserves those attachments verbally and does not portray an already failed marriage.
It needs more distinct enacted reasons for each woman to make this particular dangerous choice with this Commander.
The stronger later scenes already supply models: Anevia wanting her skill and nerve admired, Irabeth enjoying competitive desire and letting both partners see it.
Bring comparable specificity into the acquisition rather than adding another explanation that affection and wrongdoing can coexist.
The negotiated route is a credible authored alternative and should remain available before the secret kisses.

### 3. The same emotional argument is made too often

`i_truth/want` explains wanting happiness without first justifying it.
`three_beth_score/hers` returns to enjoying achievement without apologizing for it.
`three_beth_steps/uneasy` explains not having to settle the argument before accepting a dance.
`three_rooms_unlocked/sitting` again explains bringing work to make leisure useful.
`three_kept_days/beth` states the wish to ask before earning it through exhaustion.
Each is defensible individually; together they make progress sound like repeated discovery of the same insight.

There is a related repetition of announcing that an answer is not a test, not a command, not an obligation or not a cure.
`i_truth/slow`, `table/terms`, `ordinary/practical`, `power/terms`, `future/others`, the negotiated supper and the separate-continuation joins contain necessary boundaries, but their cumulative explanation outweighs their dramatic movement.
The narration sometimes explains a gesture's ethical meaning immediately after the gesture has already made it clear.
Trim repeated interpretation, retain the choices and let a later scene show someone keeping a promise without re-teaching the reader its principle.

The three expanded cycles also share a predictable structure: group activity or problem, one private conversation per wife, reconvening and an affectionate domestic payoff.
The bowling dispute, stolen book and forged guarantee have different stakes, but the order becomes visible as a template.
A future revision should vary one cycle's structure and give the couple a substantive joint professional decision, rather than merely adding another date after another debrief.

### 4. Native morale and consequential history remain underwritten

In the current 68 scenes, the only choice conditions reading `broken` or `encouraged` remain the two optional replies at `i_respite/start`.
The late public confidence, future planning and final watch otherwise use the same text.
Native Irabeth has materially different morale responses, including `NPC_Common/Irabeth/Cue_0109`, and Threshold `Cue_0017` explicitly frames retirement through doubt about her worth and survival.
Native `Irabeth/Cue_0197` responds specifically to surviving the Queen's death at Iz.
Native Anevia `Cue_0044` expresses her anger at the Commander cutting Irabeth, and `Cue_0045` explains why Irabeth retains that scar.

A pleasant outing or confident kiss is not evidence that trauma has vanished, and neither woman should be excluded from affection merely for suffering.
The problem is that the assembled route offers too little response to these histories before making broad claims about what the three have learned to trust.
`power/demon` promises opposition to cruelty, while the current late intimacy does not supply a comparably specific acknowledgment of the Commander's already possible violence toward Irabeth.
The stronger question is what trust and desire now cost in that actual history, not whether another reassuring evening can repair a native flag.
Add bounded, source-verified variants and consequences around `return`, a substantial shared arc and `last_watch`.
Do not silently rewrite native morale or manufacture forgiveness.

### 5. Progression instructions intrude into narrated fiction

`three_choose_days/short` describes the remaining shared conversations staying unfinished when the player completes the final watch.
`three_more_days/start` says continuing will reopen unfinished conversations while preserving recorded choices and goodbyes.
Those are useful player-facing explanations, but they currently appear inside the narrator's prose.
Keep the clear consequences in an explicit interface note or concise choice label, and let the narrated paragraphs describe the actual invitation and changed plans.
The current mixture is visibly mod-authored and weakens the goal of reading like original game dialogue.

## Material worth preserving

`three_match/decision` makes the Commander decide between two defensible team positions only after both wives agree they can accept either course.
Keeping the ruling yields a pennant and a spoiled celebration; replaying yields a loss and Anevia's specific hurt.
`three_anevia_flour/replayed` does not retroactively erase her choice, and the return match does not pretend to prove where her foot had been.
This is meaningful consequence, not merely a different praise line.

The stolen-book choice retains Ista and Wenna as people with work and memories of their own.
The damaged book is not repaired by gratitude, and the intact book does not replace missing accounts.
The later false guarantee grows from that unresolved situation instead of discarding it.
These civilian characters sometimes share the main cast's unusually polished self-analysis, but their material stakes prevent the arc from becoming only relationship therapy.

The wives' attraction is particularly effective in `three_lantern_debt/carrying`, `three_lantern_turn/coat` and `first`, and `three_rooms_unlocked/chosen` and `kisses`.
Anevia invites Irabeth to look at her without pretending she needs a drawing.
Irabeth chooses the coat, arranges the room and enjoys deciding where she wants her lovers.
Their kisses and jokes occur between them before the Commander joins.
The original marriage remains an active relationship, rather than background permission for the player to collect two women.

The intimate pages are adult and non-graphic, with specific anticipation, physical attraction and humor.
Quiet company, sleeping together and leaving for another promise have complete responses.
Keeping those alternatives does not require ending every sensual passage with an explanation of why the alternatives are legitimate.

## Canon, choices and repaired joins

Native Anevia's observation, criminal background, Desnan faith, fierce love for Irabeth and bread dream support the route's broad identity.
Native Irabeth's Lastwall experience, distinction between serving Iomedae and pleasing institutions, partnership in rebuilding the Eagle Watch and guarded pride support hers.
The triad, affairs, negotiated marital agreements, named civilians, games, coats and rented evenings are authored alternate developments.
They are not newly recovered canonical romance scenes.
The route should preserve the officer and spy's sharper professional edges as well as their private warmth.

The old mandatory-two-affair complaint no longer describes the whole assembled graph.
`tirabade.negotiated_table` requires both actual individual lover states and both marital agreements, and allows the Commander to decline the group without ending the independent relationships.
The inspected producing scenes give each spouse a spoken answer and each lover a separate invitation.
Local refusals and `tirabade.after_local_parting` now provide distinct continuation choices without retroactively erasing affairs or a closed wife.
The reused separation dialogue is counted once and should not be sold as several new dramatic scenes.

The old late-start reunion, shared-night first-time wording and minimized developed-loss wording have been corrected.
`return/before_the_abyss` requires the actual Chapter 3 departure.
The default reunion speaks about present life.
The remembered nights at `shared_night/familiar` require the corresponding completed scene and night choice.
The negotiated future, Azata response and developed ending now avoid importing secret-affair history.
The shorter and developed endings remain distinct.
These repairs improve current continuity; they do not settle the fresh issues above.

There is one actual skill check across the 68 scenes, Perception DC 25 at `three_back_of_seal/method`.
It distinguishes direct evidence, unreadable evidence and an optional non-roll catalogue search.
The subsequent refund and time costs preserve the difference without making romance depend on winning a die roll.
The lock lesson and bowling techniques are roleplay choices with callbacks, not Trickery or Athletics tests.
Acquisition is still mostly elapsed time and conversation choices; the initial `a_interest` and `i_interest` flags do not themselves gate choices in this trio subset.
More checks alone would not fix that.
Add an approach or condition only where it changes a character-specific problem or its aftermath.

The expanded chain still has an idealized source critical path of 696 hours, or 29 days, from `ordinary` to `three_rooms_unlocked`.
Paired individual visits can share their earliest completion time in that calculation.
This supports a campaign spread across Chapters 3 and 5, but late starts can feel like repeated waiting to advance a serial manuscript.
Do not call the selected text ranges a proof of convenient in-game scheduling.

## Separate scope and live boundaries

The demanded bespoke Trickster recovery remains absent from these scenes.
`power/trickster` offers a boundary about cosmic jokes, not a quest-connected intervention that returns an unavailable wife.
The snapshot's revival definitions are Seelah and Konomi, and the trio still excludes either wife's death or departure.
Those exclusions are appropriate until an authored and verified alternative exists.
This is incomplete project scope, not a reason to bypass death or consent gates.

Five current trio scenes specify `ContactUnit`; the older review's claim that none does is stale.
The other scenes and source eligibility checks still do not establish that both actors remain physically available through a live shared conversation.
Native book presentation, interruptions, saved continuation, epilogue delivery and actual ToyBox interaction remain separate verification work.
The manuscript permits other attachments and distinguishes deception from non-exclusivity, which supports the intended Free Love and No Jealousy arrangement at the writing level.
No live compatibility or art score is assigned here.

## Independent scores

These are one critic's judgments of this actual assembled snapshot, not objective measurements or a panel average.
Every required literary discipline must exceed 90 independently; the strong length and attraction scores cannot compensate for a weaker one.

| Dimension | Score / 100 | Reason |
| --- | ---: | --- |
| Prose and dramatic construction | 88 | Effective concrete scenes; repeated explanations and interface language remain visible. |
| Pacing and economy | 85 | Three similar cycles and recurring self-analysis slow the full reading. |
| Recognizable characterization and native-history treatment | 86 | Strong marriage and private voices, but an opening injury contradiction and thin morale/violence/Iz response. |
| Branch continuity | 89 | Important old joins are repaired; the entry contradiction and uneven earned emotional development still need work. |
| Mutual attraction and separate agency | 94 | Both wives initiate, retain their own desires and respond independently to shared or separate arrangements. |
| Mature non-graphic romantic tension | 92 | Specific adult desire, teasing and physical affection with credible quieter alternatives. |
| Player relationship choice | 93 | Negotiated entry, local refusals, separate continuation and postponement have distinct meanings. |
| Gameplay and lasting consequences | 87 | Good tradeoffs and evidence memory, but limited acquisition variety and mythic consequence depth. |
| Meaningful aggregate length and developed-route substance | 95 | Clears the doubled floor without solo-campaign credit or duplicate-bridge dependence. |

The route is ready for a focused author revision, not for a claim that all literary constraints have passed.
Prioritize the opening contradiction, distinctive acquisition and native-history development, then trim repeated explanation while preserving the successful civilian consequences and sensual scenes.
Full Trickster access and live delivery remain separately incomplete or unverified.

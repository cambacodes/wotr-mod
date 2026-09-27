# Jannah Trickster opening independent review

I reviewed `storylines/jannah_trickster_opening.py` at the requested SHA-256 `17234DABA8032DF1BDAF455D1A7F191C84C3E64E702022EDD8F2F15B9E73C0C4` and `reference/story-review/jannah-trickster-opening-development.md` at SHA-256 `276917A169B48E1BA13C8872EF9012318C5E6AEBCEC226C65C1768E3F40D195E`.
Both hashes matched before review and again afterward.
I did not edit either pinned file.
This is an adversarial review of a bounded opening, not approval of a complete romance route or an invitation to integrate it.

## Canon and character

The opening uses a plausible post-quest hook and clearly labels its new events as authored additions.
The native evidence in `reference/expansion/seelah.txt` identifies Jannah as an Eagle Watch recruit and Seelah's friend, records her desertion, later return with a temple scar, and her explicit offer to help recover the stolen souls.
The successful `WeightOfMySword` completion plus Jannah's own mission-acceptance cue are substantially better gates than a generic flirt, prison flag, or mere survival flag.
The opening correctly treats her request to rejoin the mission as separate from romance and does not assume prison history alone means she is currently in prison.
The extra-candidate table says Jannah has no verified numeric age and infers adult portrayal from military service and drinking companionship, so future materials should not invent a canon age.

Jannah's characterization is largely convincing.
She names both her panic and her decision to return at lines 90-97, resists being flattened into a redemption tale at lines 113-124, and is wary of being treated as a soldier who owes the Commander for service at lines 132-138 and 162-167.
The practice-yard activity fits her Aldori training and lets the Commander earn attention by respecting rules rather than by winning a romance roll.
The Athletics and Mobility checks at lines 98-112 produce legible different outcomes, and a failed check does not compel affection or close the only conversational route.
The choices that ask whether she wants to talk, spar, stop, or end the evening give her and the Commander room to decline.

## Material findings

**The Trickster intervention is narrated as an action the player never chooses.**
After the Commander merely sends an ordinary reply at lines 74-77, the `reply` node states that the Commander moved the packet through an impossible route at lines 80-82.
Jannah then says she knows the Commander did it at lines 150-153, but no prior choice permits the player to invoke or refuse that effect.
This attributes an intentional Trickster act and its motive to the player character without input, weakening both roleplay agency and the otherwise careful consent framing.
Offer the impossible delivery as an explicit optional Trickster choice, explain its limited effect, and provide a mundane route that preserves Jannah's invitation and her ability to accept or refuse.

**The intimate scene does not honor the stated touch boundary in its sequence.**
At line 167 Jannah says that the Commander must ask before touching her, and the text says the Commander agrees.
At lines 170-172 the Commander then touches the scar without first asking, she stops the wrist and says "Not yet," and the Commander moves the hand to her waist before she draws closer.
Her later movement can indicate welcome, but the sequence still has the Commander testing a new touch immediately after she stopped the previous one and asked for a prior check-in.
Have the Commander stop at the boundary and ask whether a different touch is welcome, or have Jannah explicitly guide the hand herself before it moves.
That would preserve the sensual pace without making her verbal condition decorative.

**The third-scene branch is correctly made eligible, but the validation does not prove eligibility.**
The shared `BLOCKED` tuple includes `jannah.trickster.met`, `jannah.trickster.courtship`, and `jannah.trickster.courtship_started` at lines 46-50.
All practice-yard entry choices set `met`, and the courtship paths set `courtship_started`.
The `the_hour_after` call overrides the default forbids at lines 179-180, excluding only death, closure, and friendship, so its `courtship_started` prerequisite is not contradicted and the continuation can be reached.
This override is an important state-contract exception, but `validate_graph` checks node targets and only verifies that the prerequisite flag is written and required at lines 183-226.
Add an eligibility assertion for each scene that applies its actual requires and forbids together, since the current tests would not catch a future contradictory gate.

**The follow-up has two dialogue-history assumptions to correct.**
`the_hour_after` is delayed 48 hours at line 179, while its opening says Jannah writes "the morning after" the practice-yard meeting at line 142.
As this is remote correspondence, a letter written next morning and delivered later could explain the gap, but the current text never says delivery was delayed; clarify whether this is the letter's writing time or the scene's present time.
The `slow` answer at line 145 says "keep the relationship at one kiss," yet the prior courtship can be reached through `next` without ever taking the optional kiss at lines 125-136.
Change that answer to refer to the agreed pace or current stage unless the graph makes a kiss prerequisite explicit.

**Clarify the initial misdelivery and the letter's privacy.**
At line 68 the outer material bears the Commander's name, the enclosed letter is addressed to Jannah's unit commander, and both seals remain intact.
The next prose immediately supplies Jannah's private first-person message to the Commander.
Explain which item the Commander is entitled to open and how the letter was intended for them, so the setup does not imply that the Commander reads a sealed subordinate's correspondence by rank.

## Consent, Trickster and adult tone

The opening takes the parole and command relationship seriously.
It gives Jannah an explicit refusal when the Commander treats her mission as a private debt at lines 71-79 and states that her service and parole cannot be used as romantic leverage at lines 148-153.
Those are good safeguards in the prose, though runtime integration must preserve them in actual assignment, scheduling, reporting, and refusal consequences.
Her post-meeting kiss is clearly chosen at lines 125-131, and the later date, privacy, and intimacy each have separate decisions at lines 162-178.
The adult sensual tone is present without graphic detail, and Jannah retains the ability to stop, cancel, or limit what happens.
The touch-boundary sequence above is the main consent revision required.

The authored Trickster idea is small and understandable rather than a random fourth-wall joke.
It changes only postal timing and does not compel Jannah, move a person, alter orders, or change her answer.
Its current presentation is not a player-controlled mechanic, however, and the module has no runtime effect beyond dialogue and authored flags.
The source is Trickster-only and does not implement fate recovery for Jannah's death branches, the missed mission, or other mythic paths.
The path entry descriptions in `PATH_ENTRY_PLANS` are future design notes, not working access routes.

## Verification and readiness

With the repository root on the Python path, `python -m storylines.jannah_trickster_opening` completed successfully without output.
The module contains three scenes, 34 nodes, and 61 choices.
An independent `\\w+` count confirms 2,334 node-text words and 672 choice-text words, for 3,006 total including mutually exclusive branches.
That is far below the project's minimum 21,000 meaningful selected-playthrough words for a complete individual route.

The module is unregistered, so its local assertions do not verify dialogue export, native binding, timing in game, actor placement, or an actual chronological save.
The `JannahCorrespondence` portrait is explicitly a placeholder and there is no reviewed character art here.
Current Trickster entry is the only implemented path in this contribution, and no Trickster route acquires her if she is dead, missed, unreachable, or never joined the native mission.
Other path-appropriate access, ToyBox Free Love and No Jealousy compatibility, save/load persistence, and live play remain unverified.
No full-route comparison or art, runtime, or integration review is supplied.

The prose contains strong agency and adult-romance foundations, but the forced Trickster action and touch-boundary sequence require revision.
The corrected scene-specific forbid override should be protected by an eligibility test.
This opening does not pass the project's strict above-90 gate as a complete route, and I assign no numeric score to this bounded review.

# Wenduag continuation: canon audit and full-route plan

## Status

This is a source-grounded design audit and production outline, not an authored route or a readiness review.

The current shared expansion has no Wenduag continuation scenes or Wenduag relationship registration.

Wenduag already has a substantial native romance, including material written for a female Commander, a jealousy episode involving Vellexia, a late trust test centered on Savamelekh's poison, and native endings.

The expansion should extend those systems and branch outcomes, not reproduce or replace the native romance.

The game supports Wenduag as a female Commander romance at the dialogue level: her native lines use `Mistress`, female pronouns, and answer branches addressed to a woman.

This is distinct from proving every mythic-path compatibility rule or proving that the modified module works with ToyBox in a live save.

No route, art, runtime integration, or score is approved by this audit.

## Sources inspected

The installed-game source archive is `D:\SteamLibrary\steamapps\common\Pathfinder Second Adventure\blueprints.zip`, which contains the serialized native blueprint records inspected for this audit.

The checked-in `reference/expansion/blueprints.json` and `reference/expansion/etudes.json` are useful text and path indexes, but the installed archive is the source for blueprint type, conditions, and actions.

The Wenduag-specific companion and romance text index is `reference/expansion/wenduag.txt`.

The Wenduag etude path-to-blueprint GUID index is `reference/expansion/etudes.json`.

The native ending and glossary text index is `reference/story-review/Wenduag.txt`.

The native player-dialogue and companion-dialogue text index is `reference/canon-review/wenduag.txt`.

Current module content is `development/Story.json`, and the current character inventory is `ROSTER.md`.

The module design requirements are recorded in `EXPANSION.md`.

These local extracted files are the evidence base; they do not substitute for in-game route testing.

## Current-project state

`ROSTER.md` lists Wenduag as a base-game character whose extension would continue loyalty, trust, ambition, and introductions, and notes that the native romance root has been identified while an adapter remains pending.

The exported story contains no Wenduag-owned scenes.

The native romance's presence means Wenduag must be counted as an existing romance the expansion can extend, not as a newly invented romance from zero.

The opening, courtship, sexual relationship, Savamelekh confrontation, and native companion endings belong to the base game.

The expansion's distinct work should cover consequences and continued relationship development beyond those native beats, with authored routes through Trickster concurrent romance and optional women-only relationship arrangements.

## Native facts and mechanics

### Identity and character voice

The native Wenduag companion blueprint is `ae766624-c030-5844-0a03-6de90a7f2009`, also shown in `PortraitMain.cs` and repeatedly referenced as `m_CompanionBlueprint` in `reference/expansion/blueprints.json`.

The companion etude root is `bf341a4bb2fe61d44a73e5a72b54968f` in the path index; its extracted path is `World/Etudes/Common/WrathOfTheRighteous/Companions/WenduagCompanion.jbp`.

Wenduag frames service as a decision based on strength and advantage, not morality or sentiment.

Her dialogue says she joined the demons for power, intended to turn her tribe into a force under her command, and chose the Commander because the Commander was stronger and could offer more.

She treats survival, dominance, skill, wealth, and the future of her people as linked aims.

She is not made trustworthy by being desired, and she is not made gentle by a romance flag alone.

Her native scenes include genuine fear of losing the Commander and difficulty naming love, while retaining her pride, appetite for power, and abrasive humor.

The authored route must preserve that combination instead of turning her into a compliant admirer.

### Native quests and consequence points

The companion etude tree identifies the Chapter 3 Neathholm Wenduag/Lann quest branches, Wenduag's training and return-to-capital events, her respect stages, the traitor state, and the Chapter 5/6 party and camp states.

The relevant native etude GUIDs include `WenduagQ1DeadDyra` `0c38936aa6f86a446885b8d13dc09563`, `WenduagQ1Drill` `76c88c9c00369e5419d8b0c70b67eef6`, `WenduagQ2_essential` `f41df5cb8af64f95b339c30fb92c9143`, `WenduagQ3` `21de006131024979832057595034e385`, and `WenduagRedeemed` `52576309e24d8024fbc08c2ff7016c2f`.

The extracted path index contains the quest states `WenduagInParty`, `WenduagKilled`, `WenduagNotInParty_Dead`, `WenduagNotInParty_KickedOut`, `WenduagNotInParty_AccordingToThePlot`, `WenduagTraitor`, and `WenduagNoMoreMongrels`.

The route must inspect actual serialized etude prerequisites and actions before using any of these in implementation; the path names alone do not establish exact trigger behavior.

The native text specifically remembers whether the Commander exposed Wenduag for Dyra's murder, sided with her in the One-Eyed Devil dispute, mocked Kyado with her, spared or killed Lann, supported her in the Savamelekh conflict, and allowed her to lead the mongrels.

These choices are excellent authored continuity inputs because they are concrete and strongly affect Wenduag's view of the Commander.

The native finale dialogues include several states for her trust, fear, confession, and request that the Commander change or accept her nature.

The native romance etude set contains `WenduagRomance` `39c388b5f2ab0f14b90030bab1b676b9`, `WenduagRomance_Active` `33c4c2f66f2461e4993df21566252079`, and `WenduagRomance_FinalRomWithWendu` `978cf434c134fd14bb4e02db7085e745`.

`WenduagRomance_LichRomanceEnd_flag` `cd59ed13f1a2c174b8a63afa166ee147` and `WenduagRomance_VelexiaConflict_flag` `23cacf7a07480da459b3a59d0fd6da82` are `BlueprintUnlockableFlag` records, not etudes, despite living under the native Etudes path.

Observe those as native flags, separately from etude lifecycle state.

The native `WenduagRomance_FinalRomWithWendu_LockController` is a separate `BlueprintEtude` `efc17b7eebbe1314280068adf5b42a09`; it has a deactivate trigger that locks the finale lock flag `2dcf0b960d1984f4bbc0c657f8f55de8`.

The final-romance etude is not proof that the confession already occurred and must not be activated as a shortcut to grant eligibility.

Its inspected activation requires native romance and companion availability plus a flag condition, while its lifecycle runs dialogue and party-movement actions.

Treat it as a guarded native finale sequence, not as an addon-owned trigger.

The romance tree also names flags for Savamelekh's poison communion, the Vellexia conflict, the father disclosure, a series of romance and true-romance flags, the Chapter 3 failure, and Wenduag's final ending.

`WenduagRomance_Chapter03Fail_flag` `3f0ff5db0d494dee8852dd26079167cc` is a native `BlueprintUnlockableFlag` used by the later Chapter 4 missed-event dialogue.

These identifiers make the romance suitable for an additive continuation with state-sensitive passages, but every runtime condition must be grounded in the installed blueprint data and parent-state adapter.

### Established romance and relationship evidence

In the native Chapter 5 ending, Wenduag offers the Commander a dangerous communion from Savamelekh's stinger.

She explicitly explains that she wants the Commander to share at least some of what made her, because she believes an ordinary mortal cannot fully understand the beast within her.

The Commander can consent or refuse; the native dialogue distinguishes a willingness to accept the risk from refusal.

The native epilogue glossary distinguishes gaining her love and genuine trust through accepting the poison, having sensuality and mutual respect without becoming soulmates, and failing to gain her trust.

This is a strong authored branch point, not an excuse to silently grant the communion or its effects.

The game has a Wenduag/Vellexia jealousy thread: the glossary records that the Commander allayed Wenduag's suspicions when she was jealous of Vellexia.

The native etude index names `WenduagRomance_VelexiaConflict_flag` `23cacf7a07480da459b3a59d0fd6da82`.

This proves a native rivalry/jealousy scene, not mutual attraction between Wenduag and Vellexia.

Any optional Wenduag/Vellexia triad therefore needs a separate, slow mutual-attraction arc and clear opt-in from all participants; ToyBox's no-jealousy toggle must not be treated as consent or chemistry.

The native jealousy event occurs in Chapter 4, earlier than the Chapter 5/late-game Savamelekh poison decision.

Therefore the Vellexia encounter belongs before the poison aftermath in a chronological Wenduag outline.

The Third_Date dialogue uses cutscene `4328c84d571762247a31bdefe240675e` and a specific third-date spawner; the native death etude `72e423c719ed9d44fa432a6b9629babd` means that surviving the earlier romance conflict does not prove that Vellexia is alive, visible, and contactable later.

An optional later scene must verify her current actor and delivery location, or stay in the Chapter 4 window.

Wenduag's native farewell offers a passionate kiss despite her earlier contempt for uplander kissing, then insists on her own framing of the gesture.

It also lets her voice fear of the Commander dying and imagine a private, physical celebration after the final battle.

The user-facing expansion should keep the adult sensuality native to Wenduag's design and dialogue while making consent explicit and leaving the exact emotional meaning to her rather than imposing a generic romantic style.

### Female Commander and path evidence

The extracted Wenduag dialogue includes a direct `Mistress` address and feminine Commander pronouns in companion and romance scenes.

This supports the base game's female Commander route.

The source includes a dedicated native Lich-romance end flag, so the expansion should preserve any existing mythic ending or closure conditions whose exact trigger and reset behavior are confirmed in the serialized records.

This audit has not established the full mythic-path matrix for Wenduag.

Trickster's expanded recovery path is a proposed alternate development, not a native fact, and it must not modify native ending flags merely to make all scenes appear available.

### Native DLC6 material and delivery

The installed game contains `DLC6_WenduagRomanceEvent` `04850c8504ac4bac9378aecbb0a65811`, parented under `92c5c3570dd643b69816fbf8f9d04bff`.

Its activation condition is an OR between native `WenduagRomance_Finished` `c3a5748e4a44a1649a75e0968c15a0c1` playing and `WenduagRomance_FinishedTrueEnding` `bf5bb702e577a0a4eaa1a9df7dea253b` playing.

This is direct evidence that the DLC6 relationship event has two native romance-ending branches.

It does not prove that the player owns DLC6, that this event has run in a particular save, or that it is a post-victory free-roam event.

The records place its related scenes under the Kenabres Festival and Tavern Final.

The `Wenduag_Labyrith` dialogue returns to the Shield Maze, Hosilla, remembered violence, a false assassination threat involving alchemist's fire, Wenduag's escape ring, and burning the past.

The `Wenduag_TakeMeHome` dialogue covers the festival tavern, her admirers, a dangerous outing, and a private date.

These are already substantial native adult relationship scenes and must not be repeated as if they were new expansion content.

Treat DLC6 presence and completion as separate optional observations.

Any addon epilogue must have a non-DLC in-campaign delivery fallback, and any promised post-victory scene needs a proved delivery window rather than assuming free roam.

### Cross-character opportunities

The native script has direct, already-authored scenes in which Wenduag judges the Commander through their treatment of Lann and other companions, and it includes jealousy around Vellexia.

That creates a credible basis for Wenduag to introduce, test, bargain with, or compete alongside other women, if every woman gets an independent motive and choice.

Wenduag and Vellexia are a credible encounter to explore because the game already establishes Wenduag's attention to Vellexia, but the native jealousy record is not proof that they are the strongest romantic match.

The attraction itself remains an authored alternate development and must earn its way through tactical respect, mutual leverage, and a later voluntary private encounter.

The alternate Wenduag/Nurah connection is also promising as an intrigue route, because both can be played as observant, self-interested survivors; however, the route must be timed to Nurah's own state and cannot treat Wenduag as a consent broker for Nurah.

Nurah's arrival and personal claim belong to Nurah's own reviewed route and state contracts.

Wenduag may create the opportunity or put pressure on an arrangement, but Nurah must answer directly, retain a real refusal, and retain the ability to bargain for terms.

The route may explore Commander + Wenduag + Vellexia as an optional authored relationship and Commander + Wenduag + Nurah as an experimental alternate development only if actual scene review confirms convincing mutual attraction between both women.

It should not assert any other woman is already attracted to Wenduag based only on rivalry, flirtation, or shared participation.

## Proposed continuation premise

Wenduag notices that the Commander is building a web of powerful women around the crusade and immediately treats that as a strategic structure to evaluate, not as a romantic entitlement.

She asks whether the Commander wants her as a lover, an equal, an asset, a rival, or all of those in different moments.

The Commander can answer in an honest, manipulative, tender, cruel, or Trickster-clever voice.

Wenduag tests whether the answer survives pressure by withholding information, moving a resource, or forcing a public choice that affects her standing with the mongrels.

She can agree to concurrent relationships when the arrangement offers her something worth the risk, whether that is service to a powerful Commander, status, security for her people, an erotic challenge, or a chance to dominate the situation.

She remains capable of jealousy, resentment, negotiation, betrayal, and ending the relationship.

The core romance conflict is whether Wenduag can choose a bond without interpreting every concession as weakness or every promise as a leash.

The Trickster solution is a credible chain of contracts, secrets, incentives, and controlled crises that lets her believe she is choosing the plan and lets the other women reject its terms.

Trickster humor can reveal contradictions and redirect fate, but it cannot replace evidence, consent, or consequences.

## Full expansion outline and word budget

The completed Wenduag expansion must contain at least **21,000 meaningful words attributable to Wenduag**, beyond all native and parent-mod text.

This is the project's aggregate authored-content floor across her connected route, not a requirement for a single selected playthrough to contain 21,000 words.

The ordinary route budget below totals **28,600 planned authored segment words**, leaving margin for editorial cuts while avoiding dependence on multi-woman scenes, death restoration, or other unproven branches.

The author must report the project's `distinct_segment_words` result for Wenduag-owned scenes, which includes node dialogue, narration, and meaningful choice text after exact whole-segment deduplication.

Because that tool does not remove semantic duplicates, boilerplate embedded in longer segments, or non-meaningful labels, an independent delivery ledger must identify Wenduag-attributed prose and choice text, exclude parent dialogue and reused material, and show that at least 21,000 meaningful authored words remain.

The 21,000 minimum applies to Wenduag's ordinary connected route alone.

Optional Wenduag/Vellexia or Wenduag/Nurah triad material is additional and may not be needed to reach Wenduag's floor or credited in full toward either other woman's floor.

This measures authored branch inventory across reachable story content; it does not assert that every passage appears in each playthrough.

### Act I: the missed invitation and a new wager

**1. Too late, then - 2,400 words.**

In Chapter 4, after the native missed-romance response `Cue_0210` and with Wenduag alive and available, the Trickster can reopen the conversation through an explicitly authored route rather than pretending the native romance began.

The source anchor is `Chapter04_Extra` `0b51051031abb4e4a818928b9cd181ee`, whose active state gates the native missed-window cue, and `WenduagRomance_Chapter03Fail_flag` `3f0ff5db0d494dee8852dd26079167cc`, a native unlockable flag.

Wenduag's native line says she assumes the Commander had their chance and that adding sex now could cause problems; the Trickster does not contradict that with a free romance flag or an out-of-world explanation.

Instead, the Commander presents a specific new wager tied to Wenduag's proven goals: demonstrate that the Commander's plan can secure her greater power and protect a future for her people, while giving her a real opportunity to expose the plan as a lie.

Wenduag can dismiss the offer, demand a concrete price, or accept the challenge while withholding any promise of intimacy.

If she refuses, the invitation remains closed until a later, separately earned reopening; no hidden consent is recorded.

**2. The evidence she trusts - 2,000 words.**

The Commander must explain how their past actions fit the offer, with branches for Dyra's murder, the Lann confrontation, her treatment during her service to Savamelekh, her army/tribe decisions, and her prior disclosure about her father.

Wenduag tests for contradictions and calls out any convenient rewrite of the Commander's history.

The player can answer with fact, a damaging admission, a calculated lie, or a Trickster inversion that is witty but still traceable to events in the game.

The scene's check is not a generic attraction roll: it is an authored test of whether the Commander has accurately anticipated what Wenduag values.

The actual roll system and result persistence must be validated against the module's existing skill-check support before this is treated as implementable.

**3. A contest with a price - 1,800 words.**

Wenduag chooses a concrete test of competence drawn from her native role as huntress, soldier, and ambitious leader, with a noncombat alternative for players who do not want a staged duel.

The contest exposes both her capacity to dominate and her concern that the Commander might be reckless with her people.

Winning earns a second conversation, not automatic romance; failure costs a real campaign resource or a publicly lost opportunity only if the relevant resource or state action can be implemented and verified.

Otherwise, the failure is a narrative setback with a clearly available later challenge, not a fake resource deduction.

### Act II: political ambition and dangerous intimacy

**4. Her father's daughter - 1,900 words.**

The route revisits her lineage and the challenge of proving leadership without relying on inherited status, using the native father-disclosure flag and her own remarks about the former chief.

Wenduag can resent pity, accept recognition, or use the conversation to demand that the Commander stop treating her as an instrument.

The scene has distinct content for players who previously heard her disclosure and for those who did not.

Its intimate turn is earned by what she chooses to reveal, not by a generic confession of vulnerability.

**5. A queen's claim - 2,100 words.**

Wenduag pushes the Commander to state whether the mongrels will have their own land, strength, and leadership after the Worldwound war.

The player can support her rule, insist on a different arrangement, or make a Trickster bargain that promises an advantage while leaving Wenduag able to inspect and challenge the terms.

The route branches on actual native army, Neathholm, and quest outcomes, but any new army, territory, or access effect must be bound to a verified in-game action.

If no such action exists, dialogue must present a personal promise or political intent rather than claiming a world-state changed.

**6. The attention she notices - 1,900 words.**

Place this Wenduag-only Chapter 4 scene before or alongside the native Vellexia Third_Date window, never after the Chapter 5 poison aftermath by accident of list order.

If Vellexia is alive, present, and the current scene occurs before the native departure cutscene, Wenduag can raise the Commander's interest in her and Vellexia and demand a direct answer.

If Vellexia is dead, departed, unavailable, or the date window has passed, the scene instead concerns Wenduag's reading of the Commander's political attention and the choice to keep the rivalry private.

No later scene assumes that an old jealousy flag guarantees a current Vellexia actor.

**7. Strength without obedience - 1,800 words.**

Wenduag uses an actual campaign choice or conflict to test whether the Commander respects her chosen service, her desire for dominance, or her right to refuse.

She may enjoy a possessive or subordinate dynamic when she chooses it, take control when that better suits her, or punish the Commander for mistaking either posture for permanent surrender.

The route distinguishes consensual domination, strategic submission, and coercion rather than translating every unequal bond into a lecture about equality.

### Act III: the Savamelekh aftermath, in chronological order

**8. The bargain before the sting - 1,900 words.**

Before the native poison decision, Wenduag explains why she offers the communion and what she expects the Commander to understand about her origin and power.

The Commander can ask precise questions, test her account, accept, or refuse.

The expansion does not alter the native poison ritual, resistance, effect, or survival result.

**9. The answer after pain - 2,100 words.**

After the native outcome, Wenduag responds differently to acceptance, refusal, and any native trust failure.

She can interpret acceptance as shared danger, refusal as caution or rejection, and failure as evidence that the Commander never understood what was being offered.

The prose must follow the actual native poison and romance flags without inferring trust from mere dialogue presence.

Her sexuality remains direct and adult, while physical intimacy depends on the branch's explicit invitation and response.

**10. The knife she kept - 1,700 words.**

The One-Eyed Devil history becomes an external problem about exposure, ownership, or a real choice to keep or surrender the blade, not another abstract negotiation over the relationship.

The scene revisits native history only to show consequences and does not claim a new inventory or quest effect unless a verified action supplies it.

Wenduag's willingness to be dangerous can remain attractive; the scene does not erase the possibility that her past violence frightens the Commander.

**11. The people left below - 1,800 words.**

Wenduag and the Commander confront a concrete consequence of Neathholm and the mongrel tribe's future, branching on whether they were recruited, moved, or left behind under the native campaign state.

Wenduag can choose political stewardship, force, or a private plan that makes the tribe stronger without pretending the player can solve prejudice with a promise.

She can disagree sharply with the Commander's Good, Chaos, or Evil approach and may withdraw cooperation if the Commander repeatedly treats the tribe as leverage.

### Act IV: war, loyalty, and a chosen future

**12. The betrayal that stays possible - 1,800 words.**

For a living Wenduag on the traitor or suspected-traitor branch, the Commander must confront evidence, make a real offer, and accept a verification plan that could expose either party.

Wenduag can return for power, for the mongrels, for the Commander, or for more than one reason at once.

Her survival and service do not imply a resumed romance; she must personally accept any renewed intimacy.

The branch must have a live actor and valid contact route before it is included in the delivered word total.

**13. The Threshold wager - 1,900 words.**

Before the final battle, Wenduag faces her fear of losing the Commander and her own desire to survive long enough to lead her people.

The scene echoes the native farewell's humor and fear without reusing the native confession or promising that either character is safe.

She can ask for a physical goodbye, refuse sentiment, propose a last tactical plan, or make the Commander promise a future she may later hold them to.

**14. A future she can take - 2,000 words.**

Wenduag chooses among an intimate relationship, a political bond, a shared future with other consenting women, a path to power without the Commander, or departure.

Her outcomes respond to true-romance versus sensuality-only native states, her people's fate, the Lann result, the poison decision, and her loyalty or betrayal history.

Each ending separates the base-game result from a new authored continuation and records only addon effects that actually exist.

**15. The hunt continues - 1,500 words.**

Deliver this as a final in-campaign scene before the ending lock, or attach it to the known DLC6 festival event only when the DLC event's parent, completion condition, actor, and timing permit it.

The scene presents a sensual, adult continuation in Wenduag's voice, with clear response branches and no duplicate retelling of her Shield Maze, Hosilla, alchemist-fire, or burning-the-past material from DLC6.

If no playable post-victory contact is supported, the scene closes before the main ending rather than inventing a postgame free-roam period.

### Ordinary route budget check

The fifteen ordinary scene allocations total **28,600 planned authored segment words**.

Even if the 1,800-word suspected-traitor scene and the 1,500-word final-delivery scene are removed until their actor and delivery bindings are proven, the other ordinary scenes still budget **25,300 words**.

The budget does not count the optional Vellexia or Nurah triad scenes, a resurrection route, or any other branch without proven access and delivery.

At least **21,000 meaningful new words** must remain within the ordinary connected Wenduag route after the content ledger excludes parent text, repeated passages, filler labels, and non-meaningful text.

If the measured, audited total falls short, add material to ordinary Wenduag scenes before counting any optional relationship branch.

### Optional women-only relationship material, additional to the floor

**16. Vellexia, by invitation - 2,200 additional words.**

This branch can open only when the women share a current Chapter 4 encounter or a verified later contact, and it begins with mutual strategic recognition rather than assumed attraction.

Each woman gets a distinct invitation and a meaningful refusal route.

**17. The terms of the hunt - 2,200 additional words.**

If both women choose to continue, the Commander and each woman discuss boundaries, public risk, privacy, and whether either woman wants a physical relationship with the other.

No relationship result is inferred from ToyBox settings or the native jealousy flag.

**18. Nurah's own bargain - 2,200 additional words.**

This experimental branch is available only under Nurah's own reviewed arrival and current-contact conditions.

Wenduag can make the introduction for strategic reasons, but Nurah must independently choose whether to engage, negotiate, refuse, or leave.

Any mutual attraction between Nurah and Wenduag remains authored alternate development and requires its own reviewer approval.

These optional scenes add **6,600 words** to the plan but count toward no woman's ordinary 21,000-word floor.

If they are ever used toward an individual supplemental count, an attribution ledger must assign each uniquely authored passage once and only once.

## Portrait and scene-art requirements

Use Wenduag's native portrait and unit blueprint as the identity reference before commissioning a new asset.

Preserve recognizable mongrel traits, her catlike eyes, sharp smile, huntress bearing, and distinctive outfit silhouette while giving her attractive adult human facial proportions and expressive eyes.

Keep the original creature traits visible where the game's model shows them; do not erase her identity into a generic human rogue.

Her adult route art may be sensual and revealing when the scene calls for it, consistent with her native costume and confident physicality.

Use different art for ordinary conversation, sensual encounters, combat tension, and the chosen epilogue when the scene needs those distinctions.

Do not use the same neutral portrait as proof that all scenes are visually complete.

An independent reviewer must compare each asset to the in-game model, rate attractiveness, recognizability, anatomy, scene fit, and tone, and identify any art requiring revision.

## Review and verification gates

The writer cannot approve their own route.

At least two independent reviewers must assess canon voice, continuity, agency and consent, maturity, pacing, branch consequences, and whether the expansion reads like a game chapter rather than a synopsis.

Every required review dimension must score strictly above 90 after the final revision, and a high average cannot hide a failing dimension.

The reviewers must inspect the whole route and all endings, including the worst-case branches where Wenduag refuses, betrays, or leaves.

The word count must be measured from authored content after all revisions and exclude parent text.

The source verifier must check every referenced native GUID, action, flag, and scene prerequisite against the installed game files.

Managed tests should cover state derivation, trigger ordering, explicit player choices, idempotence, and negative states such as dead, kicked out, rejected, romance ended, and route closed.

Headless campaign probes should use independent seeded histories for the major native branches and the complete Trickster concurrent route; they cannot be reported as one actual campaign playthrough.

Final headless verification must build a clean package, run all story and runtime checks, audit the generated manifest, inspect routes and portrait assignments, and verify the resulting artifact without installing or claiming live-game success.

The route is ready for manual in-game review only after it passes those gates and the package contains the complete reviewed manuscript and art.

The actual campaign still needs a human playthrough to verify presentation, timing, and ToyBox behavior in a real save.

## Trickster acquisition and native-history matrix

The missed-romance route has a concrete authored entry point: the player selects native `Answer_0206` `46904e95d3d239d478b6a083f2477114`, "I like you too," which leads to native `Cue_0210` `fbb8c7b423948ec47ad43f6e3d3dad9a` in the chapter-after-deadline branch.

The cue's serialized condition checks `Chapter04_Extra` `0b51051031abb4e4a818928b9cd181ee` playing, and the cue comment says Chapter 3 has already ended.

The line says the Commander had an earlier opportunity and that Wenduag does not want to complicate matters by adding sex now.

This is evidence for a missed native romance, not evidence that she silently accepts a late proposition.

The proposed Trickster route begins after that missed response, while Wenduag is still alive and is the current companion with a valid native contact.

Preserve that native exchange and append a clearly separate addon choice to the answer list after the cue; the player can accept her refusal and leave or ask her to test a new proposal.

Guard the latter choice with the appropriate native missed/closed state, a non-active native romance, current Wenduag availability, and the Trickster requirement.

There is a second native Chapter 4 branch: `Cue_0224` `4b7cf6a22b548834f9280e2d0684126a` explicitly comments that Chapter 3 ended without the `WenduagRomance_TroublesInTheTavern` event.

Its serialized conditions require `Chapter04_Extra` playing, that the Tavern dialogue has not been seen, and `WenduagRomance_Chapter03Fail_flag` unlocked.

It advances to `Cue_0225` `c865aba3ec2b05f48ace02db0261766a`, where Wenduag proposes ending the neglected-girlfriend relationship and keeping only the Commander/warrior arrangement.

This is an observed native closure branch with an actual companion-dialogue contact, but it is distinct from `Cue_0210`, which explicitly refuses a late sexual start.

Preserve both native outcomes and offer a new Trickster agreement only as a later, separately earned relationship after the Commander has accepted her immediate answer and Wenduag has had a new reason to reopen the subject.

The `Chapter03Fail_flag` `3f0ff5db0d494dee8852dd26079167cc` is verified in `Cue_0224` alongside the `Chapter04_Extra` state and the not-seen `KTC_TroublesInTheTavern` dialogue condition.

Do not assume those conditions are interchangeable with the separate `Answer_0206` to `Cue_0210` conversation.

The wager connects to her native ambitions around the mongrels, her huntress training, and the known Savamelekh conflict.

The Commander must expose a verifiable plan and let Wenduag inspect or sabotage its weak point.

The player earns an invitation through a checked decision or skill challenge with a visible stake, a meaningful failure branch, and a later recovery opportunity; no check directly sets native romance or consent.

After a successful challenge, Wenduag can initiate a new intimate offer in her own voice, or reject the arrangement without ending her independent addon route unless the player has chosen to close it.

Implement the addon bond in addon-owned persistent state and preserve native romance flags and native-ending delivery.

The precise reused quest, actor availability contract, check API, and gameplay cost still require blueprint-by-blueprint binding and build verification before this proposal can be called implementable.

| Native history | Intended Trickster treatment | Current evidence and unresolved work |
| --- | --- | --- |
| Native romance active and Wenduag alive | Enter the ordinary continuation without re-running native courtship. | The romance active etude exists; current actor and scene-contact proof are still required. |
| Chapter 3 romance opportunity missed | Offer the separate, earned Act 4 Trickster wager after the native late-response cue. | `Answer_0206` flows to `Cue_0210`, which is gated by `Chapter04_Extra`; the native dialogue explicitly says the initial opportunity passed. The addon option and its availability must be implemented and tested. |
| Missed native Tavern event / neglected relationship closure | Allow the native `Cue_0224` to `Cue_0225` closure and later provide a distinct Trickster re-entry if Wenduag is still available and chooses to reconsider. | `Cue_0224` checks `Chapter04_Extra`, unseen `KTC_TroublesInTheTavern`, and the Chapter03Fail flag; its comment names the missed event. The parent dialogue does not prove the addon re-entry. |
| Player explicitly refused a native offer | Keep the refusal binding for that offer; only a later new invitation from Wenduag can reopen intimacy. | No source reviewed here proves an existing reacquisition branch. Authored reconsideration requires a fresh in-world motive and explicit opt-in. |
| Wenduag dismissed or exiled | Seek her through an actual current location/contact and offer a reason she would consider returning. | Native kicked-out and not-in-party states exist; this audit did not prove a living actor, current location, or contact route for each state. Do not count this material until those are verified. |
| Wenduag traitor or suspected traitor | Use evidence, leverage, and a verification plan; do not turn betrayal into an automatic romance lock or instant forgiveness. | `WenduagTraitor` exists and her betrayal dialogue includes magical disappearance. Re-entry actor and quest reset semantics remain unverified. |
| Wenduag dead in a quest or encounter | Trickster must have a bespoke fate-intervention investigation and an explicit continuation if a safe resurrection path can be made. A returned Wenduag chooses whether to speak, serve, and love anew. | `WenduagKilled` and dead/not-in-party states exist, but this audit has no proof that the unit, quest history, and campaign continuity can be restored. This is a major implementation risk and is excluded from the ordinary 21,000-word count until tested. |
| Romance ended by a mythic or native closure | Preserve native closure for non-Trickster; define a separate Trickster route only where the user-requested exception can be made believable and executable. | The native Lich end flag exists; the full mythic closure matrix and each flag's runtime condition remain incomplete. |

The reported Trickster route is a design contract, not existing functionality.

It does not claim that every closed, dismissed, betrayed, or dead save state already has a proven Wenduag interaction.

The first attainable target is the explicitly missed Chapter 3 romance while Wenduag remains an active companion.

Other histories require new research and a current-world contact proof before they can be promised.

## Runtime, ToyBox, art, and independent review requirements

The Trickster extension must be reachable without an existing native romance, while the ordinary continuation may enter through the active native romance.

ToyBox Love Is Free and Jealousy Begone are compatibility settings for concurrent relationships; they are never dialogue or events known by the Commander or Wenduag.

Do not add a mod-level jealousy lock or silent breakup that defeats the requested concurrent Trickster route.

Emotional jealousy, conflict, bargaining, and refusal may remain as character reactions.

Other mythic paths retain verified native restrictions and Wenduag-specific outcomes.

The native final-romance etude is not an addon trigger; its availability predicate and actions must be observed and left to the native game.

Any new skill check must use the module's verified roll integration and persist the outcome without rewriting native quest facts.

Any claimed quest reward, army change, access grant, actor restoration, or ending effect must have an actual verified game action.

The art must use Wenduag's native model, face, coloring, spider appendages, eyes, and costume as identity references while presenting an attractive adult huntress with recognizable features.

Sensual or revealing scene art is appropriate when it fits her native outfit and the scene's desire; a neutral general portrait does not satisfy the complete art plan.

Writers cannot approve their own manuscripts.

Independent literary, canon, runtime, and art reviewers must inspect the actual finished work, and every required scored dimension must exceed 90 after revisions.

The route must pass the project's word ledger with at least 21,000 meaningful Wenduag-attributed new words before optional triad text is considered.

## Evidence limits and next research before production

This pass now confirms native blueprint types for the two named romance flags and the final-romance controller, as well as the DLC6 event's native activation branches.

It also verifies the Chapter 4 missed-window dialogue condition and corrects the chronology of the Chapter 4 Vellexia conflict and later poison decision.

The installed extraction provides path indexes for Wenduag's native quest and companion states, but this report still lacks a complete serialized prerequisite/action inventory for Q1, Q2, Q3, every traitor/death/return state, the final-romance sequence, and the mythic closure matrix.

The exact native delivery trigger and in-save timing for the full DLC6 festival event remain unverified beyond the event's parent, ending activation condition, and dialogue assets.

The current actor, interaction point, and scene-delivery path for dismissed or exiled Wenduag have not been established.

Resurrection and restoration of a dead Wenduag have not been demonstrated and remain excluded from the word-floor plan.

Vellexia's Chapter 4 date uses a native cutscene and spawner, and her death state exists; a later interaction needs a separate actor and location check.

The exact ToyBox behavior in a live save and any after-victory free-roam availability have not been tested here.

Before writing, extract the relevant `BlueprintEtude`, `BlueprintUnlockableFlag`, dialogue answer-list, cue, cutscene, and unit-placement records from the installed archive and produce a state/entry/delivery matrix.

Then prototype the missed-romance entry in an isolated test build, confirm the existing native cue remains unchanged, and prove a current Wenduag contact and retry-safe skill decision.

Do not use this outline as evidence that any proposed scene, triad, resurrection, Trickster acquisition, or path restriction is already implemented, feasible, reviewed, or ready.

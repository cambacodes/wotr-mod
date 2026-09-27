# Queen Galfrey continuation audit

## Finding

Galfrey is an adult, source-supported romance candidate with an unusually complete native courtship already present in the game.

The expansion should continue or repair that courtship instead of recreating its introduction, tavern date, confession, final-battle proposal, or native epilogues.

There is enough native characterization to support a long continuation: Galfrey's age anxiety, history of self-denial, intimate but awkward courtship, faith, authority, military responsibility, regret over sending the Commander to the Abyss, and possible postwar abdication are all explicit in the scripts.

The biggest design constraint is her explicit distinction between trusting the Commander as Queen and trusting them as Galfrey.

A Trickster route can earn the personal trust she withholds, but must preserve her right to refuse and must answer the actual reasons she gives.

This audit is research and a continuation proposal only.

It does not add a manuscript, adapter, blueprint, art asset, or roster entry, and it does not establish readiness.

## Source method and fingerprints

I read the installed game's `blueprints.zip` directly and resolved native English localization keys through `Wrath_Data/StreamingAssets/Localization/enGB.json`.

The installed archive SHA-256 is `BE61C9B723EF06558DA8D7CFC7F0C7EA869F60BA9952EBBBBD116CF681863EA5`.

The native English localization SHA-256 is `3289C3EBAB206BA6312D4C2D512C0B5623E52D7E2B86596074B81D355725AA75`.

The mod's current `reference/expansion/etudes.json` SHA-256 is `6687429FB6EB4A9B27E1F6AEF4053E33EBF929C80D5AE46F80DA762B500AB5E1`.

The shared story export SHA-256 is `FC618CBBA77AB3895324BF8FC05F7E9773935BF5D84FE11A4F651E52868F560E`.

The current roster SHA-256 is `E27C8E458757E5637082705FF5654D41FF5B9944D5866EE1A34EDDFDF49FADF8`.

The roster currently labels Galfrey's native romance root as identified and its adapter as pending.

Searching the current `development/Story.json`, `storylines`, and `src` for Galfrey finds no authored Galfrey story or adapter; the only production-facing mention is the roster entry.

The asset hashes below are SHA-256 hashes of the individual JSON members as stored in the installed archive, rather than hashes of normalized or rewritten JSON.

| Installed asset | GUID | SHA-256 |
| --- | --- | --- |
| `World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/Galfrey.jbp` | `3230b1f42aa8f2e42ba5fef806cf43e9` | `4D74BCD72031154D2EFC4C78FB668A2B64C0718D14FA3CBCF3558ED2F91AA919` |
| `World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/Galfrey/GalfreyRomance.jbp` | `133842cc9812fc74f88a21e12ec2c6f8` | `89B43EE8A61B19244A154E73D932C16028957FC1A530DFF97FC8DE38B9A906B5` |
| `World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/Galfrey/GalfreyRomance/GalfreyRomance_Active.jbp` | `c9358d866e0b3844b8d72536ca60e4b4` | `9F085100DFB2215A718CF22726D27082BCB09A92A4BA401C1BA81291FB395E0C` |
| `World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/Galfrey/GalfreyRomance/GalfreyRomance_Finished.jbp` | `133f3b1b38f04fa44be3200b786e437f` | `76941FDB441927AFD3C378B8E7220C155E3FB236A1191C2A6EEF41A5195A3886` |
| `World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/Galfrey/GalfreyTrueFeelings.jbp` | `e7a7a68d59b00554598eccb6065e97e9` | `7CEFECAAEEACCCDBF1C72F2068EB8A7945316359757504ABC72F7666DFDC3FAD` |
| `World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/Galfrey/FlirtAttempt.jbp` | `90cad864d2956564db9aafaa4a89781b` | `E233376A13D93416E10515C1FB807BBB30DBF46E18C145C82426633201E567F3` |
| `World/Dialogs/c3/Drezen_C3/GalfreyArrives/Cue_0067.jbp` | `bcaa48d10bd57a347afb166fa31aca15` | `67CE62505579F588E099C89A5465561EA48F5C23B2A5B8805FD6DD977FFA7DDC` |
| `World/Dialogs/c5/DrezenMain_C5/Galfrey/Cue_0041.jbp` | `36f61641ac48bb242b831fe30085ef40` | `A79A9386EDA0B541E895F12F887B30BE488FCE5F86D0ED90D6151CCEF5927828` |
| `World/Dialogs/c5/Iz/GalfreyAfter/Cue_0064.jbp` | `6d3caa0cc4e3f544b9fa925a4df15a1f` | `AC385F1250AD13EBB1CFC9494480F0D4482C347FD8AF453DBD8E9154AEFFC3D5` |
| `World/Dialogs/Companions/CompanionRomances/Galfrey/GalfreyInDisarray/Cue_0015.jbp` | `6befc4b7354eddd489eb200e83b28a1a` | `188CCFD2B5A9F2DB141FB282166E9808355AEB7C0E911B732489AB61F7024E46` |
| `World/Dialogs/Companions/CompanionRomances/Galfrey/GalfreyDrink/Cue_0074.jbp` | `56a68e74f9d23604c874e1e2d83d9d3a` | `675C809910E67BBEABC231AC13D6AEEF3070784649E8429556D471F0888DA034` |
| `World/Dialogs/c6/ThresholdExterior/GalfreyThreshold/Cue_0022.jbp` | `781c38023c5205f4f9d5f61c33c2a3d7` | `7871F8669E8AC673C73B36E48E5B6CCF2BACB3DB5D0CD14810863A3DF5CEC4A6` |
| `World/Dialogs/Epilogues/Cue_0249.jbp` | `dd519146e0e7f6f43a68b1d9af343b0b` | `793A6381238217A9DEADA8943FBA6A389674C1CEEA2EEA87C1FC1A645459FF1C` |
| `World/Dialogs/Epilogues/Cue_0262.jbp` | `8624075fc3b022d41bd8c18ae0b71eb0` | `DE1A174AF246EE415097EF198BCE574357FE7C082F150ED8B816B0BDDC0CC21A` |

## What the native scripts establish

The top-level Galfrey etude is a child of `ImportantNPCs_fate` (`0e7c12bdd7425534e8606127455c3809`).

The native romance etude `GalfreyRomance` (`133842cc9812fc74f88a21e12ec2c6f8`) is a child of Galfrey's state etude, and it owns child states for active courtship (`GalfreyRomance_Active`, `c9358d866e0b3844b8d72536ca60e4b4`) and completed romance (`GalfreyRomance_Finished`, `133f3b1b38f04fa44be3200b786e437f`).

The romance root's completion trigger completes its `Active` child, and the `Active` and `Finished` children have distinct achievement behavior.

The `Active` child starts `48_Spark` (`b9c6e3e0d6ac42ef8b9a2bad0c36420d`), while the `Finished` child starts `49_Flame` (`c95ca64f070f42748f097cc3ff21d505`); a copied comment in the Finished component does not change that reward identifier.

Completion of `Active` represents failure in its native comment and is not equivalent to the named `Finished` state.

The ordinary romantic epilogue checks `Finished` playing, so an adapter must preserve these separate lifecycle states and must not infer a completed romance from `Active` alone.

Other romance descendants track the flirt attempt, Galfrey's true feelings, and the post-intimacy outcomes, including a separate Devil-specific aftermath.

These are relationship-history flags, not permission to start a second romance layer that contradicts them.

The story is not an invented relationship from no prior interest.

At the end of the Chapter 3 Drezen arrival dialogue, Galfrey asks to speak to the Commander alone (`Cue_0067`, `bcaa48d10bd57a347afb166fa31aca15`).

The surrounding event is also a military briefing before the Midnight Fane attack, so the invitation is intimate but not by itself a date or proof that she has already agreed to a romance.

The main native courtship plays through `World/Dialogs/Companions/CompanionRomances/Galfrey/`, with distinct `GalfreyInDisarray`, `GalfreyDrink`, and `GalfreyAfterSex` sets.

In the Disarray dialogue, she describes duty as the shape of her life and says she has denied herself personal attachments; the scene presents this as conflicted self-understanding, not a simple puzzle answer that the Commander can solve by insisting.

The Drink dialogue is a real first-date scene with personal questions, embarrassment, anger, laughter, and a branch where Galfrey ends the courtship.

In that rejection branch she explicitly declines the date and says she cannot return the Commander's feelings (`GalfreyDrink/Cue_0074`, `56a68e74f9d23604c874e1e2d83d9d3a`).

That rejection is an authored outcome which a continuation must respect unless a later source-grounded event earns a new, voluntary decision.

If the romance proceeds, Chapter 5 makes her fear of age and vulnerability explicit, while the Chapter 6 Threshold scene lets her state that she wants to share her life with the Commander after the war.

The native art and prose cast her as a commanding, beautiful adult woman whose private awkwardness and unguarded desire coexist with authority.

Native dialogue says she has lived for a century through sun orchid elixirs and that the Church paid for this life prolongation, so her appearance should follow the native model rather than an invented addon rejuvenation or an assumption that chronological age requires geriatric features.

Her first love was one of her father's knights, a few years older, according to `GalfreyDrink/Cue_0033` (`b1e7719164da9064d9a59b789bd15697`); this supports a past adult courtship but establishes neither a current partner nor an exhaustive sexual history.

Native romantic epilogue text uses both male and female Commander pronouns, so this audit does not impose male-only eligibility; the complete native gender, race, and mythic entry matrix remains unverified.

The script does not establish a current spouse or a competing present-day lover for Galfrey.

That is a limit of the inspected script, not evidence that she has never had past lovers or that her entire off-screen history is settled.

## Council, faith, and path constraints

In Chapter 3, the Commander can invite Galfrey to attend the Commander's military and political council meetings (`GalfreyArrives/Answer_0001`, `e1ea7f81e271449ea88a6b7440e3d9df`).

Galfrey's political role therefore belongs in the romance as an active governing problem, not an excuse to remove her from office or turn her into a passive prize.

The Trickster campaign already has its own recurring Councils, including five distinct council stages under `World/Etudes/Common/WrathOfTheRighteous/MythicTrickster/PlayerIsTrickster/Council/`.

Those meetings are a natural authored space for a cross-thread plot, but an addon scene must be scheduled around native council cues and must not replace the player's actual Trickster decisions.

The inspected diplomacy lines that call Galfrey “cousin” are spoken by Daeran, not Konomi; their native speakers resolve to Daeran's unit blueprint.

Konomi's introduction establishes her appointment as the Queen's diplomatic attaché, not a family relationship.

This evidence does not establish mutual attraction between Konomi and Galfrey either way, so any optional triad requires authored characterization, earned reciprocal attraction, and consent rather than a canon-based exclusion or assumption.

The strongest explicit romance gate appears in Chapter 5.

Galfrey can say that the Commander's mythic powers are too unreliable and that, although she trusts the Commander as Queen, she cannot trust them as Galfrey (`DrezenMain_C5/Galfrey/Cue_0041`, `36f61641ac48bb242b831fe30085ef40`).

That is a direct personal-trust rejection, not generalized fear of outsiders.

A Trickster route must address the contradiction by showing the Commander accepting limits and consequences when no one can force them to do so.

The native Chapter 5 Drezen dialogue also has a mythic-specific duty scene (`Cue_0044`, `7a160960668f2ef4180cb56edb8388e9`) gated on the `PlayerIsAngel`, `PlayerIsAeon`, `PlayerIsDragon`, or `PlayerIsLegend` etudes.

That condition set is direct evidence that one native Galfrey response is deliberately limited to those four paths.

Iz dialogue separately references Demon, Lich, and Swarm states in path-specific responses, while Angel gets a bespoke response as well.

These branches show that there is no single path-neutral romantic response to transplant into every mythic route.

They also mean that the Trickster extension needs its own authored branch, not an assumption that the game already treats Trickster as one of the four paths in the duty scene.

The native Chapter 3 dialogue offers a concrete model for Trickster's credibility problem.

The line about changing the past so Drezen never fell is `GalfreyArrives/Answer_0041` (`b7a49048c0c93d941b05742e95314e18`), but its incoming branches require the Aeon `MythicAeon_DrezenHistoryChanged` state, Galfrey accompanying the Commander, and the appropriate `ReinforcedByAeon` polarity.

This is evidence about Galfrey's reaction to Aeon's altered history, not proof that Trickster performed this native history change.

It does not itself change the native romance etude or earn Galfrey's private trust; the Trickster's forged-instrument plot below is authored alternate continuity and needs independently verified Trickster quest and council anchors.

Her Devil-specific conversation is similarly not a generic invitation to erase faith boundaries.

The base dialogue includes an attempt to imagine a workable relationship between a Devil Commander and an Iomedaean paladin, but it also includes her conclusion that their paths are incompatible because both are too committed to what they represent.

The script preserves incompatibility as a real outcome, so non-Trickster paths should keep their native restrictions and a Trickster recovery must require Galfrey to choose a credible accommodation herself.

The native arc also branches on late-campaign trust, letters, and regret.

At Iz, the Commander may discover the letter Galfrey left in Drezen or ask the Storyteller to reveal its emotional history; Galfrey identifies the letter as an impulsive expression of grief for a friend she treated unfairly.

Treating that letter as proof of an already-established romance would overstate the source.

It is evidence that the Commander mattered to her and that the separation wounded her, but her own dialogue frames the moment as grief, guilt, and friendship.

The final Threshold confession is a distinct native moment in which she voluntarily names her love and asks to join the Commander in the final battle and afterward (`GalfreyThreshold/Cue_0022`, `781c38023c5205f4f9d5f61c33c2a3d7`).

It should remain the canonical capstone when the player has earned that version.

The inspected epilogue cues support companion-ascension variants, but do not establish the game's full jealousy or exclusivity behavior.

The ordinary epilogue line says Galfrey abdicates and spends her long life with her beloved (`Epilogues/Cue_0249`, `dd519146e0e7f6f43a68b1d9af343b0b`).

The Ascension variant says she joins her beloved as a semidivine eternal partner (`Cue_0262`, `8624075fc3b022d41bd8c18ae0b71eb0`).

The latter checks the native “with companions” ascension cue, while the ordinary partner epilogue checks that those companion cues were not seen.

This is concrete evidence that Galfrey's native ending supports an Ascension variant with companions present.

The ordinary epilogue also checks `GalfreyRomance_Finished` playing, excludes both companion-ascension cues, and has another negative etude condition; the Ascension variant requires `Finished` playing and either companion-ascension cue seen.

These conditions do not prove that the base game supports several simultaneous romantic partners; that behavior still requires a ToyBox-enabled test.

The continuation should preserve these native conditions and make its own relationship checks local to Galfrey.

It must not read another companion's romance as a reason to reject the Commander, set a global romance lock, or rewrite another route's epilogue.

The native state also records consequential survival branches.

`GalfreyDead` (`a4f20ae9f6a6c3d4ba204721589470a2`) is a child of her state etude, while `GalfreyKilledByCommander` (`eb30187696a04f99aa194859b13a629e`) starts that death state.

Iz has separate branches for Galfrey going to the Temple of Stone Manuscripts or the monster lair and for whether the Commander fought beside her.

The named `Galfrey_Final` etude explicitly excludes `GalfreyDead`, so the final native reunion is not a live continuation when that death outcome stands.

The inspected records did not show a native resurrection bridge for a dead Galfrey.

Do not implement recovery by merely clearing the death etude or by starting a romance scene against a missing unit.

For a Trickster route, survival during the Iz mission is the source-verified recovery lane to prioritize.

If a future story attempts postdeath restoration, it needs a separate audit of corpse or soul persistence, actual resurrection effects, Commander/Queen identity, legal campaign consequences, and a fresh voluntary romance decision after restoration.

The Lich version and swarm/Commander-kills-Queen versions are distinct states, not interchangeable “she is absent” gates.

Their outcomes should remain character-appropriate, and the romance cannot reward the Commander for murdering Galfrey or turn undeath into a cosmetic route shortcut.

## Continuation proposal

### Placement and central conflict

Write the new story as a campaign-spanning continuation whose authored scenes fit verified living-Galfrey interaction windows around the Chapter 3 arrival, the Commander's return from the Abyss, Galfrey's Chapter 5 reunion and Iz mission, and the approach to Threshold.

These are proposed campaign phases, not verified addon interaction windows; the actual actor, map, dialogue reservation, and timeline must be audited before placement.

The normal branch should recognize an active or completed native Galfrey relationship and the relevant living Queen state.

The Trickster branch should be seeded through actual Trickster quest and council states and continue through a verified live Galfrey state, including the authored path where the native romance never activated.

It should not reset a completed native rejection, reactivate `GalfreyRomance`, or fake the old confession.

Instead, introduce a new council-related audience during Chapter 3, before Galfrey leaves the field of play, and let the relationship deepen through the later native events without repeating them.

The future abdication and rebuild decisions belong in the Threshold and epilogue branches, not in scenes that require the campaign to continue after the game has ended.

The core conflict is not “duty versus a man who tells her she deserves pleasure.”

It is Galfrey learning to choose a life that is hers while facing the cost of the choice publicly, and the Commander demonstrating that their fate-bending power will not take the choice away from her.

The original ending's abdication is one possible resolution, not a mandatory relationship reward.

She can remain Queen and establish boundaries around the Commander's authority, abdicate after a lawful transition, or refuse private partnership while preserving a political alliance.

Each ending needs a real cost to her public role and to the Commander's preferred future.

### Trickster credibility and mechanics

Use the established Trickster Council as a candidate setting for a staged constitutional crisis, pending verification of its actual stage order, quest dependencies, actors, and dialogue reservations.

The Commander and Galfrey discover a forged royal instrument designed to make her abdication appear inevitable and place Drezen's authority under the Knight Commander.

The Trickster can prove the forgery, expose the council's motives, or exploit the chaos to seize more authority.

The forgery must be resolved through an authored branch that leaves Galfrey in control of her decision; exposing it, exploiting it, or confessing to a failed deception may each produce different political costs, but none should award affection automatically.

The intervention must be a credible trick based on planted evidence, competing witnesses, legal language, and a public reversal, not fourth-wall awareness, memory rewriting, or an unexplained “fate says yes” effect.

At least three separate decisions should test whether the Commander can tell Galfrey the truth, refuse political advantage when it would make her consent meaningless, and let her keep control of the final decree.

Each decision should have a Wisdom, Knowledge (World), Persuasion, or Trickery check only where the native check system supports it and the scene needs a check.

The numeric DCs should be calibrated against existing game checks and written into the eventual integration handoff; this audit does not certify any specific DC as playtested.

Success should give access to stronger testimony or a safer public solution.

Failure should change the political cost, delay the next scene, or force a harder repair, not silently erase prior evidence or trigger automatic affection.

The planned route should offer parallel ways to proceed through good-faith evidence, a risky Trickster bluff, or a costly negotiated confession, with distinct outcomes and no claim that any branch is tested until implemented.

The player should not need one specific alignment answer if they can prepare alternate proof through council outcomes and sidequests.

A useful cost is public: Galfrey can make the relationship known, but the Commander must accept a formal limit on unilateral decisions affecting Mendev and submit to a public review of the disputed decree.

An Evil answer may use controlled intimidation to protect Galfrey from a coup attempt, but it cannot turn her into the Commander's subject or replace her consent with fear.

The darker route can be more possessive, compromising, and morally compromised while remaining recognizably a Queen making a choice under pressure.

The heroic route may surrender political advantage to protect her right to govern.

The romantic route should remain attainable only if Galfrey personally concludes that the Commander's unpredictability can coexist with accountability.

ToyBox's Free Love and No Jealousy settings should make other romance flags irrelevant to this route's eligibility.

Those settings cannot be represented as Galfrey canonically approving every partner or as an in-story magical cure for jealousy.

If a companion's presence changes Galfrey's reaction, write that as a specific character response and keep her choice open, rather than imposing a global exclusivity gate.

The final route test must cover Galfrey alone and alongside several concurrent romance flags while preserving each route's own ending flags.

### Content plan and minimum

Plan 24,500 to 30,000 distinct new words, the arithmetic range of the eleven allocations below, counted from authored Galfrey continuation nodes alone.

Do not credit native dialogue, parent mod dialogue, reused scene text, labels, or copied summaries toward the 21,000-word floor.

Aim for at least 21,000 distinct meaningful spoken and narrated words after branch deduplication.

The eleven numbered blocks below are content allocations, not a verified count of scenes or visits.

The eventual manuscript should identify its actual scene and visit count, with each visit advancing the relationship or a political consequence rather than padding a standalone date with repetitive questions.

1. **The invitation, 2,000 to 2,500 words:** during the Chapter 3 military and political council, Galfrey weighs the Commander's freedom to act against the army's need for a chain of responsibility.
2. **Two signatures, 2,500 to 3,000 words:** an intimate legal review exposes an attempt to bind the Commander and Queen into one authority, forcing them to define the difference between partnership and rule.
3. **Council of jokes, 2,500 to 3,000 words:** Trickster's council games help expose a forged decree, but each gag can humiliate a witness or cost Galfrey credibility.
4. **The absent letter, 2,000 to 2,500 words:** this block is provisional until a real messenger or delivery mechanism is verified; otherwise move it to a return conversation and do not imply a live Galfrey encounter during the Commander's Abyss absence.
5. **Her return to Drezen, 2,000 to 2,500 words:** after verifying her actual location and interaction window, Galfrey confronts the Commander's altered reputation, her own anger and worry, and the difference between forgiving the Abyss decision and choosing a relationship.
6. **The old name, 2,000 to 2,500 words:** Galfrey confronts how others treat her age, history, and body; the Commander may flirt with her as an adult woman, but cannot deny the years or tell her what they mean.
7. **Her sword arm, 2,000 to 2,500 words:** shared training and private attraction let Galfrey show desire and initiative without turning a military scene into generic seduction.
8. **The room after court, 2,500 to 3,000 words:** their most openly mature and sensual scene follows a separate explicit consent conversation about office, privacy, competing partners, and what each wants from the relationship.
9. **Iz without a stolen choice, 2,500 to 3,000 words:** mission preparation and the native Iz assignment determine whether Galfrey survives, whether they fight together, and which later conversation is available.
10. **A last boundary, 2,000 to 2,500 words:** before Threshold, Galfrey sets limits for either abdication or continued rule; a player who refuses the terms receives a political alliance or breakup ending rather than a hidden romance flag.
11. **Three future endings, 2,500 to 3,000 words:** Queen and partner, retired Queen and partner, or bittersweet separation with earned trust but no relationship; the epilogue summarizes the political future after the playable finale.

The word allocations are a plan, not counted manuscript evidence.

The scenes need meaningful alternate branches for Good, Chaotic, and Evil Commander characterization, plus consequences when a key check fails.

The Trickster route requires an independently reachable courtship when native romance failed, but must treat explicit native rejection as meaningful until a later event gives Galfrey a new reason to revisit it.

If a native rejection is irreversible under current game flags, document that before implementation and make the recovery mechanism an explicit, isolated Trickster-only decision with an independent review focused on consent and source fit.

### Optional women-only relationship material

No inspected native evidence identifies Konomi as Galfrey's cousin or establishes mutual attraction between them.

The existing Anevia/Irabeth relationship is already a deep marriage, but this audit has not established mutual attraction between Galfrey and either woman.

Any Galfrey/Konomi or Galfrey/Anevia/Irabeth triad remains an optional authored possibility, not a canon fact or automatic extension of the solo route.

A triad would need independent scenes that establish mutual attraction between all participants, negotiated consent, and distinct outcomes if one woman declines.

No existing source reviewed here provides that proof.

### Art direction

Before generating art, extract and review Galfrey's actual in-game portrait, model, and costume as the reference set.

Keep her recognizable as the same adult Queen and paladin, with her canonical hair, face, ceremonial armor, and regalia as shown by the native model.

The intimate design can use loosened armor, a rich private gown, bare shoulders or arms where her source costume and scene support it, and a direct, confident posture that allows her to be sensual without making her look like a different character.

Retain believable age, expression lines, and battle history as attractive adult features; do not exaggerate age into a deliberately old or ugly redesign, and do not erase every imperfection if it removes character.

Use one canonical portrait for normal dialogue and additional scene-specific art for the private date, training, and political confrontation.

Do not use a generic “fully clothed” rule to suppress mature tone or an exposed-skin rule to imply that a scene is sexual.

An independent art reviewer should judge native resemblance, attractiveness, age portrayal, costume fit, expression, and the distinction between political and intimate scenes separately.

## Work required before any readiness claim

1. Re-extract the native Galfrey blueprint records and English strings from the current installed game build, then calculate and independently verify every per-member digest before using this report as a binding baseline.
2. Inspect the complete native `GalfreyDrink`, `GalfreyAfterSex`, `Galfrey_Final`, and Threshold graphs, including all check outcomes and all conditions, to map the exact preexisting romance gates; specifically trace the incoming conditions to Chapter 5 Cue_0041 rather than infer a gate from the cue alone.
3. Trace all references to `GalfreyDead`, `GalfreyKilledByCommander`, the Lich state, and the Iz location choices through their consumers; prove which states leave an actual actor and which permanently close romance access.
4. Map the native Trickster Council's actual stage order, actor presence, quest dependencies, and dialogue reservation behavior before attaching an addon scene to it, and identify real quest anchors for any authored forged-instrument plot.
5. Design a persistent addon state model that does not mutate native romance flags or shared companion flags, then independently review its compatibility with Free Love and No Jealousy.
6. Write the manuscript at the full distinct-word floor with genuine alternate choices, outcomes, and endings; run branch accounting and count words after deduplication.
7. Have separate reviewers evaluate the complete manuscript for Galfrey voice, canon fit, personal agency and consent, mature tone, pacing, mechanics, and choice consequences; every required independent score must exceed 90 before any readiness claim.
8. Source and review the native portrait/model, generate the route art, and require independent art review before staging it.
9. Build the package and run focused headless checks for all romance states, all Trickster entrances, saved/reloaded states, mutually exclusive endings, simultaneous partner flags, failed checks, quest reservation, death states, and epilogue interaction.
10. Perform the requested in-game test from a representative Trickster save to verify that the interaction appears at the intended actor/location, the dialogue renders, the consequences persist across reloads, and ToyBox concurrent romances coexist.

11. Specify separate Chapter 3 and Chapter 5 acquisition entrances for players who miss the first audience, distinguish never-courted history from a native explicit rejection, and give each history a source-grounded, voluntary progression or permanent refusal outcome.

12. For every legal or political resolution, distinguish authored narrative state from implemented campaign effects and identify the actual effect, quest, or persistent flag before dialogue claims that a decree, authority transfer, or review has occurred.

13. Reconcile the chronology of courtship, return, training, intimacy, Iz preparation, and Threshold with Galfrey's verified actor locations and campaign phase; do not treat survival at Iz alone as romance recovery.

14. Reconcile each proposed outcome branch with Galfrey's agency: the exposure, bluff, and confession routes must have distinct costs, and checks may provide evidence or access but cannot erase an objection or award affection by themselves.

## Remaining uncertainty

The exact full romance graph and final activation timing have not been audited branch by branch in this pass.

This report relies on direct member extracts for the listed checkpoints and the current extracted etude index for surrounding state names.

No recovery-after-death path, postwar playable continuity, Trickster romantic reacquisition, route acquisition windows, political effect implementation, art design, or live in-game behavior is verified yet.

The candidate is strong and worth developing, but no part of the proposed 21,000-word continuation should be described as written, reviewed, or ready.

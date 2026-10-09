# Playthrough review summary (Luna gpt-6-luna medium + Terra gpt-5.6-terra medium)

| Policy | Dossiers | Avg fun | Avg feels-like-game | Hard | Major | Minor |
|---|---|---|---|---|---|---|
| hostile | 12 | 6.0 | 6.0 | 3 | 14 | 2 |
| nontrickster_good | 18 | 6.2 | 5.8 | 9 | 12 | 3 |
| trickster_all_romance | 75 | 6.1 | 5.9 | 14 | 86 | 9 |
| trickster_villain | 54 | 6.2 | 6.1 | 7 | 54 | 5 |

## Findings by kind and severity

- gameplay_integration / major: 131
- continuity / hard: 30
- fun / major: 20
- game_feel / minor: 11
- chronology / major: 8
- fun / minor: 5
- continuity / major: 4
- continuity / minor: 2
- fact / hard: 2
- character_truth / major: 2
- character_truth / hard: 1
- game_feel / major: 1
- gameplay_integration / minor: 1

## Gameplay integration: recommended forms

- area_encounter: 57
- sidequest: 30
- companion_interaction: 29
- camp_event: 9
- combat: 2
- item: 1
- journal_quest: 1
- check: 1
- crusade_event: 1
- keep_as_is: 1

## Lowest-scoring checkpoints (feels like part of the game)

- nontrickster_good/chapter-5-part-05: feel 4, fun 6, needs_fixes
- trickster_all_romance/chapter-6-part-02: feel 4, fun 5, needs_fixes
- hostile/chapter-2: feel 5, fun 6, needs_fixes
- hostile/chapter-4: feel 5, fun 6, needs_fixes
- hostile/chapter-5-part-02: feel 5, fun 6, needs_fixes
- nontrickster_good/chapter-3-part-01: feel 5, fun 7, blocking
- nontrickster_good/chapter-3-part-05: feel 5, fun 6, needs_fixes
- nontrickster_good/chapter-4-part-01: feel 5, fun 6, blocking
- nontrickster_good/chapter-4-part-02: feel 5, fun 6, needs_fixes
- nontrickster_good/chapter-5-part-01: feel 5, fun 4, blocking
- trickster_all_romance/chapter-3-part-01: feel 5, fun 6, needs_fixes
- trickster_all_romance/chapter-3-part-02: feel 5, fun 6, blocking

## Hard findings

- [hostile/chapter-3-part-01] continuity dorgelinda.trickster.caravans.countersign/sign: The chosen answer returns the pen and withdraws the offer, but the scene still sets a flag named for countersigning the carts. That makes the recorded state contradict what the player did.
- [hostile/chapter-3-part-02] continuity wenduag.trickster.killed.cairn/build: The scene establishes that Wenduag survived the staged killing, was treated, and can escape, but the end state still records her as dead. That directly contradicts what happened in this scene.
- [hostile/chapter-5-part-01] continuity shamira.trickster.killed.drowning/why_known: Shamira is listed as dead and unavailable at the start of this part, but this scene presents her as having just fallen in the boudoir and as a conscious presence that can enter the Commander's mind. The scene does not es
- [nontrickster_good/chapter-2] continuity wenduag.trickster.early.walls/start: This scene is included in a non-Trickster playthrough even though the dossier says Trickster-gated scenes stay shut. Its Trickster-specific scene ID and flags make the mismatch explicit.
- [nontrickster_good/chapter-3-part-01] continuity galfrey.trickster.ch3.crows/start: This scene is included in a non-Trickster playthrough even though the dossier says Trickster-gated scenes stay shut. Its title and flag identify it as a Trickster scene, contradicting the policy header.
- [nontrickster_good/chapter-3-part-01] continuity wenduag.trickster.early.gate/start: This scene is included in a non-Trickster playthrough even though the dossier says Trickster-gated scenes stay shut. Its title and flags identify it as a Trickster scene, contradicting the policy header.
- [nontrickster_good/chapter-3-part-02] character_truth ember.visitor/own: Ember’s visit is framed as romantic attention, which conflicts with the explicit friendship-only boundary in her project relationship and decision records.
- [nontrickster_good/chapter-3-part-07] continuity arsinoe_what_she_asks/sole_terms: The Commander promises Arsinoe, "Only you," while Gesmerha is already marked committed at the start of this part and remains committed at the end. The sole-intention flag makes the contradiction persist in the resulting 
- [nontrickster_good/chapter-4-part-01] continuity galfrey.trickster.ch4.crowd/start: This Trickster-gated scene appears in a good Angel playthrough even though the dossier says Trickster-gated scenes stay shut. Its presence contradicts the stated route and makes the scene's availability untrustworthy.
- [nontrickster_good/chapter-4-part-01] continuity horzalah.trickster.ch4.scar/look: This Trickster-gated scene appears in a good Angel playthrough even though the dossier says Trickster-gated scenes stay shut. Its presence contradicts the stated route and makes the scene's availability untrustworthy.
- [nontrickster_good/chapter-5-part-01] continuity horzalah.trickster.ch5.nothing/open: This Trickster-gated Horzalah scene runs in a non-Trickster playthrough, despite the dossier stating that Trickster-gated scenes stay shut. It exposes the Commander to branch-specific events and sets a Trickster flag.
- [nontrickster_good/chapter-epilogue] fact seelah.ending_aeon/start: This Angel playthrough includes an Aeon rewrite ending that says the Worldwound never opened. That contradicts the dossier's stated mythic path and the war-ending epilogue shown for the same character.
- [trickster_all_romance/chapter-3-part-02] continuity nurah.trickster.prison.pardon_recruited/start: Nurah is marked departed and unavailable at the start of this part, but the scene has her present in her prison cell and lets the Commander leave her a pardon. This is a direct state contradiction.
- [trickster_all_romance/chapter-3-part-08] continuity devarra.trickster.flight.leash/report: The scene presents the golem as active and awaiting a command to destroy the eggs, but native progress for this part says the golems have already been deactivated. This makes the scene contradict the world state shown to
- [trickster_all_romance/chapter-3-part-20] continuity nidalynn.trickster.kiln.the_chaplain/leave: The selected response explicitly sends the chaplain away without praying, but the scene sets a flag named `chaplain_prayed`. The flag contradicts what happened and could make later content treat the prayer as completed.
- [trickster_all_romance/chapter-5-part-02] continuity minagho_chivarro.trickster.react.baphomet/laugh: The scene says Baphomet’s servants will return Minagho’s corpse intact, and the flag says the delivery occurred, but the end state still marks Minagho dead and unavailable. This leaves the outcome contradictory for the p
- [trickster_all_romance/chapter-5-part-04] continuity minagho_chivarro.trickster.reunion.wardrobe/silk: The state table marks Minagho and Chivarro dead and unavailable, but this scene has Chivarro alive, speaking, and entering Drezen. No earned return is shown, so the scene contradicts the dossier’s state.
- [trickster_all_romance/chapter-5-part-06] fact devarra.tower.first_snow_free/start: Devarra appears alive in this Chapter 5 scene, but her canon states that every living Devarra in the main campaign dies in Chapter 3. The scene conflicts with that established world state.
- [trickster_all_romance/chapter-5-part-08] continuity ember.the_afternoon_not_promised/promise: Ember’s scene is framed as an ongoing friendship, but the end state marks her relationship committed and harem-eligible. That contradicts the project’s explicit friendship-only boundary and falsely represents a romantic 
- [trickster_all_romance/chapter-5-part-27] continuity horzalah.trickster.beat.sister/now: Horzalah says Hepzamirah died in Colyphyr, but Hepzamirah appeared physically in the earlier requisition scene and is listed as committed at the start of this part. The dossier shows no return between those events.
- [trickster_all_romance/chapter-6-part-01] continuity iomedae.trickster.threshold.banner/decide: On the shown path Iomedae first accepts the renewed personal question, then immediately says she has not decided whether to answer. The scene also sets her committed flag, leaving her relationship state unclear.
- [trickster_all_romance/chapter-epilogue-part-01] continuity dorgelinda.trickster.epilogue.after_the_war/dorgelinda.trickster.epilogue.after_the_war: The committed Dorgelinda route conflicts with this paragraph saying private visits stopped. The part’s end state still lists her relationship as committed.
- [trickster_all_romance/chapter-epilogue-part-02] continuity camellia.trickster.epilogue.kept/page: The playthrough sets multiple incompatible Camellia epilogue outcomes as though they all happened. The scenes say she stayed at the Commander's side, followed her own path, waited alone at Threshold, and stayed instead o
- [trickster_all_romance/chapter-epilogue-part-02] continuity areelu.trickster.afterlogue.return_witch/line: The playthrough presents Areelu as both retaining the Abyss and losing her magic after her graft is collected. Those are mutually exclusive states, but both outcome scenes and flags appear in this part.
- [trickster_all_romance/chapter-epilogue-part-02] continuity arueshalae.treatment.epilogue.together/page: Arueshalae's epilogue says she shared a home and life with the Commander, while the adjacent native outcome says she travelled and returned only for visits. The dossier sets both outcome flags, leaving her postwar status
- [trickster_all_romance/chapter-epilogue-part-03] continuity wenduag.trickster.epilogue.native_ascent.partner.unknown.secret_kept/page: The path presents several mutually exclusive Wenduag epilogue outcomes as events that all happened. She refuses the offered ascent, gathers a Drezen band, and leads hunters to pillage an orphanage, leaving her fate and t
- [trickster_villain/chapter-3-part-02] continuity nurah.trickster.ran_off.dedication/start: Nurah is listed as departed and absent at the start of this part, but this scene has her physically hand over a manuscript and speak. That contradicts her stated state.
- [trickster_villain/chapter-3-part-16] continuity eritrice.council.the_casualty_lists/told: Eritrice changes from started at the beginning of the part to committed at the end, but this scene records sharing a name and has no commitment beat. The listed flags do not support that relationship-state change.
- [trickster_villain/chapter-5-part-08] continuity eritrice.council.a_lie_for_the_chair/agree: The flag records that Eritrice lied for Chadali, but this scene only records the Commander agreeing to lie later. The text says the request will be entered in Eritrice's private record, while Chadali's answer belongs to 
- [trickster_villain/chapter-5-part-15] continuity camellia.trickster.bond.witness_alive/hers: The scene sets a flag named `witness_alive` after Camellia pushes Radan down the stairs and watches him fall. The flag contradicts the outcome shown to the player.
- [trickster_villain/chapter-epilogue-part-01] continuity jerribeth.ending_aeon/start: This Trickster-path playthrough presents an Aeon rewrite that erases Jerribeth and the Commander's history, even though the same dossier also plays their together ending. The incompatible outcomes undermine the committed
- [trickster_villain/chapter-epilogue-part-03] continuity areelu.trickster.native/None: The selected path presents two incompatible ascension outcomes for Areelu: one where she shares the transformation and one where she does not. Both appear as scenes in the same play order.
- [trickster_villain/chapter-epilogue-part-03] continuity irabeth.native.eng7_f6c/None: The epilogue gives Irabeth two incompatible career outcomes in sequence: she returns to the Eagle Watch after leave, then retires and hands back her commission.

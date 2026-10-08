# Hepzamirah: cloud design-first review (villain-route-hepzamirah)

Owner: cloud voice owner, 2026-10-08. Base: wotr-mod `main` abb97e4 (after the jerribeth and minachiv merges).
Scope (CLOUD-QUEUE villain row 3): `hepzamirah.*` and every scene she appears in. Shared scenes: this row sits above
melazmera, horzalah, delamere and the rows below them, and below minachiv, so it owns
`household.pair.melazmera_hepzamirah.*`, `household.pair.delamere_hepzamirah.*`, `household.pair.horzalah_hepzamirah.*`
and `household.docket.horzalah_hepzamirah.*`; `household.pair.hepzamirah_minagho.*` belongs to minachiv (voiced there,
read here for contradictions: none). Truth pages read: writer `knowledge/characters/hepzamirah/` (canon, voice, states,
decisions, relationships, native-lines.json), `handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (binding contexts 1-6),
`plans/route-redesign-pipeline.md`; mod `tools/route_packs/voice/hepzamirah.md`.

Presence read from the export (`development/Story.json`): 59 owned scenes (2 early Voetiel scenes, the Colyphyr offer,
4 ghost-device entries, the remote body deal, the Apprentice at the gate, terms, 18 flesh scenes, 20 bond scenes,
4 companion reactions, 4 epilogues, Last Call page and call), 10 shared pair/docket scenes, and 23 appearance scenes in
other routes (Horzalah's Guild/beat chain, Melazmera's hunt and Last Call page, Delamere's Last Call page, Shamira's
manifest, Mielarah's Colyphyr voyage, Nocticula's hoard answer, Dorgelinda's ledger, Minagho/Chivarro's Baphomet
reaction, the shared Last Call collectors/last-joke pages). Machine truth table: `truth-table.json` beside this file:
230 flags (`hepzamirah.*`, her pair/docket/reader flags, Woljif's Moon flags), every producer choice and every consumer
gate in the export (scenes, nodes, paragraphs, choices, Derived, Books, native readers), with consumer counts before and
after this pass and a `finding` on each defect.

`python expansion.py` was NOT run to completion here: this environment has no game `blueprints.zip`. See "Validation".

## 1. Structural defects (fixed first)

| # | Defect (export evidence) | Class | Fix (text and read-only paragraphs; ids, choice positions, Next/Set/gates untouched) |
|---|---|---|---|
| S1 | Wrong medium. `body.hounds/door` is the gate guard's three-line note with a fourth line "in another hand ... pressed so hard the nib went through"; `throat` and `joke` are written as that scrawled note ("Come down and tell it before I get bored"), but `sister_at_gate` already says "You go to the gate", and `vial` then opens "By the time you reach the gate". The Commander is in two places at once; the menace is a note. | BEL/HOW | One face-to-face scene at the gate: the guard reports in person; she has the Apprentice pinned to the gatepost (`throat`); `joke` is spoken to the Commander's face; `vial` starts where the Commander already stands. |
| S2 | Off-screen menace. `body.hounds/joke>1` "He's yours." sets `cost.courier_killed` and ends the scene; every later reader only reports it (`body.terms/killed` "eyes went to Mutasafen in a box", `bond.the_hunt/pack_killed`, `flesh.princess/read_killed`, epilogue P4, Last Call P1). | VOI/BEL (binding context 6) | `body.terms/open` gains a `courier_killed` paragraph (the Apprentice's acid-scarred hands nailed over her door); `body.terms/killed` stages the box, his weeping and her relish; `bond.her_room/keeps` gains the hands on her bedpost. 0 -> 2 on-screen consumers. |
| S3 | Presence not earned. `body.terms/refused` (every refusal: `price>1`, `why>1`, `rent>1`) left "the jar of wildflowers, unbroken" in her empty room, though the jar is Ember's (`flesh.flowers`, `body.terms/ember`) and Ember may be absent, devastated or never met. | COX/BEL (binding context 3) | Refusal text has no jar; a paragraph gated on the existing `hepzamirah.trickster.ember_messenger` (Ember present and available) leaves Ember's jar. |
| S4 | Flag overload. `flesh.rent/choose>0` (hang the head over the east gate) and `>2` (bury it quietly, "Nobody will ever know") both set `rent_taken`; `flesh.apostate/door_gate` (reader) says "They know it was me. Good. I wanted them to know", which contradicts the burial branch. | BEL/HOW | `door_gate` now holds for both histories ("Whatever your crusaders were told, Father's people know whose hand it was"). Not split: a new flag would need a new `Set` on an existing choice. |
| S5 | Promises and costs set and never read: `cost.discreet` ("Remember what you sold, when they ask for more"), `court_defied` ("You will pay for that ... I will read it back to you"), `eve_promise` ("you will come for me. Say it"), `weapon_vow`, `treaty_signed` ("I will hold you to it until one of us is dead"), `renamed_herself` ("that held"), `cost.horned_scar` (the Commander cut Baphomet's mark into a forearm), `gift_worn`, `market_strike`. | BEL (cost without consequence) | `epilogue.leavable/page` gains 10 gated paragraphs (gift split by `horn_cut`: horn knife or hornless iron head); `epilogue.leavable_on_record/page` gains `eve_promise` and `treaty_signed` readers. All appended after the existing 17/4 paragraphs. 0 -> 1-2 readers each. |
| S6 | Integration gap with the harem rows: the `household.pair.horzalah_hepzamirah` outcomes (`*_terms_kept`, `hepzamirah_term_broken`, `horzalah_term_broken`) had no reader anywhere. | BEL/AGY | Three readers on `epilogue.leavable/page` (kept truce; she crippled the courier; Horzalah sold the warning). |
| S7 | Wrong speaker / paperwork. Her Last Call page (`hepzamirah.lastcall.page`, a narrated epilogue) carried the household pairs' receipts as the Commander's first-person ledger lines ("I promised to take the dangerous last wagon.", "I spent 400 Finances and hauled the replacement myself.", "I cancelled the scout allocation ..."), and her own reactions in a flat register ("The two passages are finished."). | VOI/BEL | All 44 pair paragraphs on her page (P7-P50) re-voiced by paragraph Id: costs narrated in third person, her reactions at her register. Same Ids, gates, indices; the Delamere-named lines keep naming Delamere so their derived presence gates are unchanged. |
| S8 | Placeholders in owned shared scenes: `household.pair.horzalah_hepzamirah.{truce,retry}` (7 nodes each) and `household.docket.horzalah_hepzamirah.{account,account_table}/j05_instructions_destroyed` were `[PROSE PENDING]` (claude-work-queue rulings 4 and 05, 16 entries). | AGY/VOI | Voiced from the approved beats in `storylines/harem_rows/zzz_hepzamirah_cloud.py`; text only, no paragraphs on the J03 rows. Queue and prose-pending entries removed (16 each). |
| S9 | Paperwork standing in for consequence: `flesh.drill_result/field` ("seven marked tallies") and `harsh` ("The sergeant's casualty list separates ..."); `flesh.chaplains/embassy` ("The court clerk nevertheless records your designation"); `bond.nerosyan/embassy_reply` ("without a claim of agreement from the court"). | VOI (binding context 6) | The last charge and the two men she breaks are on screen; the chaplain's protest and the clerk's retreat are staged. Same costs. |
| S10 | Recorded, not fixed (gates are frozen): presence gates derived from a name in the text. `bond.eve` requires `areelu.present_now` on entry and on every choice (the eve and its explicit slot vanish whenever Areelu is not in the household, though she is only named: "into Areelu's laboratory"); `bond.the_call/if>0` (the oath `call_sworn`) and `body.hounds/joke>2` (forged vial) require `areelu.present_now`; `body.terms/price>2` ("Why stay at all?") requires `horzalah.present_now`. | INT/COX (chosen loss ~-2 INT) | Proposal for the coordinator: drop the presence requirement on `bond.eve` and `the_call/if>0`, or move the name out of the text upstream (`hepzamirah_flesh.py`) so the derivation stops adding it. Not done: gates are save-relevant and out of a voice pass. |
| S11 | Recorded: `hepzamirah.trickster.landlord` has two producers (crate intimidation; counter-terms that lead to the closing refusal). Its only reader requires `hepzamirah.committed`, which the counter path never reaches, so the overload is inert. | none | Left. |
| S12 | Recorded: flavour receipts set and never read with no promise in their prose (`armed`, `sparred_*`, `pick_returned`, `looked*`, `corner_kept`, `let_go`, `eye_kept`, `letter_*`, `replied`, `song_shared`, `unmade_refused`, `moon_callback`, `second_night`, `cult_waited/taken`, `market_paid/mended`). | none | Left (no consequence promised). |

No reveal-before-staging found: every recollection node reads its own native witness (`colyphyr_offer`,
`baphomet.boasted_souls`, `baphomet.named_horzalah`, `horzalah.gift_delivered`, `heard_ember_pity/apple`,
`mutasafen_secret`, `mutasafen_letter` inventory reader). The ghost device is Trickster-only and gated on the canonical
Colyphyr death (`hepzamirah.dead`), with closure honoured (`hepzamirah.closed`, `ghost_dispersed` -> late fallback).

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten (all in `storylines/harem_rows/zzz_hepzamirah_cloud.py`): `body.hounds` door/sister_at_gate/throat/joke/vial
(S1), `body.terms` killed/refused (S2, S3), `flesh.apostate/door_gate` (S4), `flesh.chaplains/embassy`,
`bond.nerosyan/embassy_reply`, `flesh.drill_result` field/harsh (S9), `epilogue.leavable` P10-P16 and
`epilogue.leavable_on_record` P1 (flat closers such as "The victory had not fulfilled that promise", "There was nobody
left to exact the promised public acknowledgment from"), her Last Call pair lines (S7), the Melazmera pair's
`open/start`, `open/prepared` and `diversion/lost` (her side was convoy logistics: "The low road leaves my stores
exposed"; now "you overgrown lizard", "you useless worm", the pick driven into the road). The pair placeholders (S8).

Left alone (they work, at her register, with on-screen cruelty): the ghost entries ("Nothing is a gift in this place.
Everything is a leash with a pretty name."), `flesh.first_morning` (the onion, "piss-drinking cowards", "feed him his own
tongs"), `the_pick`, `the_market` (the laundress's wrist, "you stupid wench"), `flesh.rent` (the priest's head in a
sack), `bloodline` ("Stop me if you can afford to."), `mirror`, `the_horn`, `the_corner`, `drill` (the regiment crippled
and gloated over), `apostate` wait/watch/trap, `bond.morning` ("wondering whether I fuck the way I fight"), `the_call`,
`the_hunt`, `the_eye` (the eye cut out of Mutasafen's spare), `eve`, `sortie` (the spear pulled out on screen),
`crooked`, `gift`, `names`, `treaty`, `the_song`, `princess`, `unmade`, `vorlesh`, `the_weapon`, the Woljif/Greybor/Ember
reactions, `epilogue.commit` and `epilogue.refused`. The Delamere pair (`relic`, `stores`, `repair`) already leads the
requisition to a body (collar seized, badge torn off "taking cloth and skin with it", "answer with his tongue"), as
writer `decisions.md` asks; left.

Not changed because a later build pass owns them: `epilogue.commit/page_exit` ("Her answer stood.") and the
`lastcall.active` paragraphs on `late_*` are written by `endings_job3` inside `earned_outcomes.integrate`, after the
harem rows; a text layer here cannot reach them. Proposal: "That was her answer, and she did not give it twice." /
"Whatever Threshold owed her, she meant to collect elsewhere. She left the refused doorway with her guards and did not
look back at the bed she had been denied."

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 92 | 92 | Native anchors unchanged: Colyphyr death `10989135`, the slave claim `3dce2b36`, "That old piece of shit turned his back on me!" `84523473`, sacrifices `8f337ada`, Mutasafen's eyes/hands threat `7de8d1a8`, the Melazmera truce `a68b28c8` (pair `terms.known`). No new lore: the Guild warning, the ravine and the Apprentice's hands are authored situations inside existing authored continuity (Horzalah's Guild, Mutasafen's Apprentice). |
| VOI | 86 | 91 | Insult density restored where it had gone flat (worm, whelp, wench, lizard, "piss" at the truce); her threats are bodily ("which of your fingers you need to hold a cup", `3caba7e8`/`842890df` register); no apology, no mercy credited to herself; Horzalah's j05 and truce lines keep her cold Guild register ("Horzalah. Not Hepzamirah."). |
| TRK | 93 | 93 | Device unchanged: "Leavable" steals the cell, the corner, the body ("lodger's flat"), the embassy, the name; costs `baphomet_grudge`, `late`, `altar`, `horned_scar`, vial/lab/grudge. |
| INT | 86 | 87 | Hooks unchanged (AnswerLists f457c832/995aaa29/74e18303/cdf898c8, NativeReturnCue 001f33d9/b03aa739, SeenCues/SelectedAnswers/Inventory readers). S10 presence gates recorded (~-2). |
| BEL | 82 | 90 | Every promise in the bond chain now reaches the epilogue (S5); the courier's death and the hands are seen (S2); the gate scene is one place (S1); the refusal no longer leaves another woman's jar in a run without her (S3); the sisters' truce has a payoff (S6). |
| COX | 89 | 91 | S3 removed an unearned Ember prop; no elimination: Horzalah, Melazmera and Delamere keep their own outcomes and their routes' gates. |
| HOW | 85 | 90 | Truth table shipped; every new paragraph reads a flag with an existing producer; the layer raises on any unresolved scene, node, paragraph or non-placeholder. |
| AGY | 74 | 88 | The sisters' pair was placeholders. Now Horzalah sells or gives away a Guild warning for her own standing and Hepzamirah wants the lances alive for her own spearhead and the courier's tongue for her pride; Melazmera's ridge is her hunting ground and Hepzamirah's guards are her property. None of it is about the Commander. |
| ALIGNMENT LENS | 85 | 92 | On-screen evil: the Apprentice blinded for a box and his hands nailed over her door, the courier crippled behind the north gate, two soldiers broken on the drill field, Horzalah selling twenty lances for souls; slaver ethics unrepentant (the laundress, "I would work you down it again"); love stays a debt and a leash ("pulled on it like a leash", "a hand closed round a throat that was not hers"). No redemption. |

## 4. Explicit slots (Gemory tracker)

- Existing briefs: `body.terms.explicit.1` and `bond.crooked.explicit.1` (built slot nodes; default text unchanged),
  `bond.eve.explicit.1` and `bond.gift.explicit.1` (trackers). Boundaries are untouched by this pass (`threshold`,
  `down`, `face_say`/`last`, `kiss`/`kiss_say` unchanged). The two built briefs had list-typed `facts` (slot_brief_lint
  hard `schema`); converted to text, provenance kept under `authored_continuity.fact_sources`.
- New brief: `hepzamirah.trickster.bond.her_room.explicit.1` (Commander + Hepzamirah, host `bond.her_room/sit_say`,
  "This too. I keep this."): possession among her trophies, including the Apprentice's hands when `courier_killed`.
  Terminal host: needs a reserved node after `sit_say` before generation (recorded in the brief).
- `bond.eve` stays unreachable without Areelu present (S10); its brief says so.

## 5. Proposals for scenes owned by other rows

- `melazmera.lastcall.page` (melazmera row) and `delamere.lastcall.page` (delamere row) carry the same first-person
  Commander receipts from the pair generators (`household_pair_melazmera_hepzamirah.COSTS`,
  `household_pair_delamere_hepzamirah.COSTS`). Narrate them as on her page (S7); the texts in `PAIR_LINES` can be reused.
  Better still, fix the generators (narrated text for the pages, first person only in the Ledger book entries).
- `trickster.lastcall.page.collectors` P10 (Mutasafen's account) is ledger prose ("funding had bought the body, while a
  forged vial or a murdered courier left him demanding another payment"). Proposal: "Mutasafen's account survived
  Threshold. Somewhere on his bench a little of the Commander's blood was still growing; the forged vial and the
  courier's eyes had only made him hungrier. Hepzamirah called none of it paid."
- `horzalah.trickster.beat.labyrinth` ("Hepzamirah came to visit, the first year ... Then she stopped coming"): consistent
  with her (forgetting is crueller than the trap); keep.

## 6. Validation

- `python expansion.py` cannot complete here: no `blueprints.zip`. The full build ran with only the zip readers stubbed
  (`storylines.native_facts.verify`, `tools.native_fact_inventory.verify_inventory`, `storylines.native_overrides.finalize`,
  `tools.crossroute_checks.other_woman.native_participation_contexts`) through `expansion.make_expansion()`.
- `main` is not buildable as merged: `storylines/camellia_round2._slots` reads `brief["insertion"]`, and e26d856 added two
  Camellia tracker briefs without it (KeyError). This branch skips briefs without an insertion spec (two lines; the
  committed `main` export is unchanged by it). Rebuild on the coordinator host before merging.
- Baseline proof: the same stubbed build of untouched `origin/main` (plus that two-line fix) reproduces the committed
  `development/Story.json` scene for scene (0 scenes differ; only the zip-derived `NativeOverrides` differ). The committed
  export on this branch is the stubbed branch build with `NativeOverrides` carried from `main`, written with
  `authoring.compiler.serialize(payload, 'expansion', Path('development/Story.json'))`; `targona.lastcall.page`, whose
  `RequiresAnyGroups` member order varies run to run, is carried from `main`.
- Export diff vs `main`: 16 scenes differ, all in scope (10 `hepzamirah.*`, 6 owned pair/docket scenes). Only node text,
  paragraph text and appended paragraphs differ: no scene metadata, node id, choice, Next, Set, gate, check, cost or
  existing paragraph gate changed; every new paragraph sits after all existing ones.
- Checks (`check()` functions, branch export; `main` in brackets): `savecompat` 0 [0]; `payoff_lint` 0 [0];
  `prose_pending_lint(integration=True)` 0 [0]; `claude_work_queue_lint` 0 [0]; `text_structure_lint` 0 hard [0];
  `player_text_lint` review unchanged after rewording [6184]; `voice_lock_lint`: 10 more Claude-locked scenes changed
  (expected; proposed approvals in `voice-approvals.proposed.json`); `edge_lint` locked regressions 219 -> 220 (the one
  new entry is `epilogue.leavable_on_record`, a locked scene changed here; the other 36 Hepzamirah entries were already
  stale on `main`), Hepzamirah Trickster business:menace 0.263 -> 0.242, menace hits 95 -> 99 (the advisory `exit` counter 24 -> 25 is the bare phrase "the door" in `bond.her_room`, not an exit line); `slot_brief_lint --strict`
  hard 253 -> 251 (the two `facts` schema hard findings fixed; the new brief has only the usual terminal warning).
- Unit tests (`python -m unittest` with the same stubs, 18 modules touching her scenes, `RRT_TEST_STORY` pointed at the
  stubbed build): 193 run; 8 failures and 2 errors, identical by name on untouched `main` (stale voice locks awaiting
  approvals, jerribeth/minachiv ending texts, Horzalah's slot count after e26d856, J01 manifest counts, J03 fixture
  shape, and `s18x` reading `blueprints.zip` directly). Without `RRT_TEST_STORY` the tests that rebuild in a subprocess
  error on the missing zip (14).

## 7. Not done / handed on

- S10 presence gates (Areelu on the eve, the oath and the forged vial; Horzalah on "Why stay at all?").
- `epilogue.commit` closers owned by `endings_job3` (proposal in section 2).
- Lock enrollment and voice approvals: the coordinator applies them (`voice-approvals.proposed.json`).

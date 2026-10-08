# Horzalah: cloud design-first review (villain-route-horzalah)

Owner: cloud voice owner, 2026-10-08. Base: wotr-mod `main` 723ccae (after the jerribeth, minachiv, hepzamirah,
melazmera, areelu, wenduag, shamira, arue12 and noct-reconcile merges).
Scope (CLOUD-QUEUE villain row): `horzalah.*` and every scene she appears in. Shared scenes: this row sits below
jerribeth, minachiv, hepzamirah, melazmera, areelu and camellia, and above wenduag, nocticula, shamira and the rows
below them. So `household.pair.horzalah_hepzamirah.*` and `household.docket.horzalah_hepzamirah.*` belong to
Hepzamirah (merged; proposals only, section 5), `minagho_chivarro.trickster.react.baphomet` to Minachiv, and this row
owns `horzalah.trickster.react.wenduag_*` (the Wenduag review left them to this row) and
`nocticula.trickster.court.horzalah`.
Truth pages read: writer `knowledge/characters/horzalah/` (canon, voice, relationships, states, decisions,
native-lines.json), `handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (binding contexts 1-6),
`plans/route-redesign-pipeline.md`, `handoffs/trickster/horzalah.md` (C8-C16) and `handoffs/trickster-matrix.json`.

Presence read from the export (`development/Story.json`): 71 owned scenes (Ch4 scar look; Ch5 ribbon-box letter; the
three entries: ear con at her mercy, the night knife when unmet, the late night after a refusal or dismissal, each
with its Chapter 6 Threshold-camp continuation; guild.kept; the dresser test and its night twin; the collar and her
move with night twins; the chamber; 27 presence beats by the Storyteller's shelves; 2 letters; 9 epilogue pages; the
Last Call page and call; 16 Greybor and Wenduag reactions; 2 native epilogue replacements), 4 sisters' pair and
docket scenes, and 12 appearance scenes elsewhere (Nocticula's court, Minagho/Chivarro's Baphomet reaction,
Hepzamirah's ghost body, gate, terms, pick, sister and epilogue, the Dorgelinda ledger columns, the Last Call joke
gates). Harem rows: she sits in none of the s01-s52 rows; her only harem integration is the sisters' pair and
docket, the Guest List and the Ledger debt.

Machine truth table: `truth-table.json` beside this file: 192 flags (every flag her own scenes read or set, plus every
`horzalah.*` and sisters' pair/docket flag anywhere), each with every producer (choice + text, EnterSet, native or
derived definition) and every consumer (scene, choice and paragraph gates, Derived, Presence, Ledger lines, native
epilogue edits), consumer counts before and after this pass, and a `finding` on each defect.

`python expansion.py` was NOT run here: this environment has no game `blueprints.zip`. See "Validation".

## 1. Structural defects (fixed first)

| # | Defect (export evidence) | Class | Fix (text and read-only paragraphs; ids, choice positions, Next/Set/gates untouched) |
|---|---|---|---|
| S1 | Integration gap with the harem row. The sisters' pair and docket set `household.pair.horzalah_hepzamirah.{horzalah_terms_kept, hepzamirah_terms_kept, horzalah_term_broken, hepzamirah_term_broken, permanent_refusal}` and `household.docket.horzalah_hepzamirah.instructions.destroyed`; only Hepzamirah's `epilogue.leavable` read the pair outcomes, and the burned trap instructions ("Now nobody uses this on me again") were read by nobody. Horzalah sold twenty lances, gave a warning away, had her courier crippled, and her own pages never knew. | BEL/AGY | Six readers appended to `epilogue.together/page` and `epilogue.commit/page` (her partner pages): the master who asked whether the Guild works for nothing comes back without his tongue; the cambion's purse kept beside the box; the crippled courier kept on her stair; the warning sold when the Commander would not carry it (forbids `resolved`); the locksmith shut in his own strongroom. 0-2 -> 2-4 consumers each. |
| S2 | Promise without reader. `beat.threshold/if`: "Then I will go to the Worldwound myself and look for what is left, and I will be very angry about it." Nothing read `beat.threshold_heard` but the scene's own forbid; `epilogue.mourned` (the Commander dead) said nothing of it. | BEL | `epilogue.mourned/page` gains a reader: a month on the rift's edge with three knives, killing what crawls out; the knife who joked about it stops speaking. The flag is also set by "I'll come back", so the paragraph quotes only the shared `promise` node ("Come back with everything else attached"). |
| S3 | Withheld outcome. `epilogue.unanswered` (wants heard and granted in `guild.kept/wants`, the dresser test never reached) ended "The answer, and what Horzalah did with it, came after the war": an off-screen non-ending. | BEL/HOW | She decides for herself: she jerks the dresser's chain back before the Commander's hand closes, brings the old man to his knees ("In my hall the slow ones are the ones we sell"), takes him home, and keeps exactly what she asked for and was granted: coming and going in Drezen as she pleases, the sentries stepping off the path. No commitment claimed (Binding context 5). |
| S4 | Branch-false text. `letter.invoice` (requires `ally`: the Commander accepted the dresser on a chain) closed with "The dresser sends his respects", as if he were still hers. `epilogue.mourned` P7 (forbids `primed`: the crossroads spit, the bedroom refusal, the bedroom let-go) said the crusaders "had last heard her threaten the Commander through a shut door", which happens on none of those histories; P8 "No report of its reception had returned" (she never sends reports). | CAN/BEL | Invoice: "Make my dresser earn his keep, now that he is yours." P7: last seen bleeding at the Commander's mercy, alive because the Commander allowed it, which she never forgave. P8: whether her masters bowed to the trophy, nobody in Drezen learned. Same gates, same indices. |
| S5 | Wrong quote for the branch. `late.at_night/dismissed` opens on "'Get out of my sight,' you said." Its gate is `horzalah.dismissed.latched` (Answer_0005 on the loyal list, Answer_0023 on the traitor list); only Answer_0023 is attested as "Get out of my sight" (trickster_world, matrix). | CAN | She answers her own native farewell instead, which both lists share (Cue_0007, handoff C12): "I told you my father's favour was not worth dealing with you again. I lied." |
| S6 | Wrong medium; menace by note. `late.at_night/no_priest`: "a note on your pillow, pinned through with a knife ... H." in a Kind=visit scene; `beat.ear/start`: "I sent him a note ... No, I did not hurt him. I only told him whose it was" (sanitized, binding context 6); `beat.ear/room`: "I have had a note sent to the barracks." The route also had six knife-pinned notes (bedpost letter, her_move lintel, sentries' mortar, no_priest, two epilogue tent notes): a monotone device (BEL). | VOI/BEL | no_priest: she is on the end of the bed in the dark, turns the knife in the pillow against the Commander's cheek, says the line, and leaves the knife (the choice "Pull out the knife" still holds). beat.ear: the surgeon's hand flat on his own table and her knife between his fingers; the loudest guard gets a notch in his own left ear. Five knife notes remain, each a different thing (letter, ultimatum, praise, two Threshold farewells). |
| S7 | Paperwork in place of menace. `letter.invoice` was a bill ("the watching of three doors ... At the Guild's rates"); `epilogue.ally` was a closed account ("her bills were always paid on time ... closed the account in person, took her last payment"). The writer truth page names the invoice beat as the risk (`horzalah.voice.never_ledger`). | VOI/BEL (binding context 6) | The invoice keeps its frame and its 150 Finances, but the courier's porters drop the deserter on the threshold with both heels cut ("The specification said nothing about his feet"), and the cultist on the third door is under the chapel floor. Ally: a grain-selling lord choked on his own grain; a cell in the lower town three heads short; she counts her last payment coin by coin and never touches the Commander's hand. |
| S8 | Wrong medium in the Ledger. `owed.horzalah` (the Commander's own book) said "Her report from the Guild records whether she completed it", and its lines "Her report from the Guild placed the trophy ..." / "No report has come from the Guild". She comes in person (`guild.kept`, `eng8.guild.*`); she has never written a report. | BEL/VOI | Entry and both lines rewritten in the Commander's voice: the ear in a white ribbon, her people in Drezen watching that the price is kept; "She came back to show me what it bought"; "She has not come back to say whether her masters bowed to it." Same Requires/Forbids. |
| S9 | Text defects. `beat.name/start`: "by my father's priests, by a nalfeshnee in a bathhouse and by one of my father's own priests" (doubled); `beat.sister/back_departed` and `back_unavailable` said the same warning twice in a row. | HOW | Rewritten once each ("and once by a nalfeshnee in a bathhouse, who did not live to do it twice"). |
| S10 | Recorded, not fixed (gates and Sets are frozen): `unmet.knife/outmatched` ("[Double the watch.]") sets `guard_called` + `closed` but not `horzalah.started`; `epilogue.closed` requires `started`, so a lost bedroom fight closes her route with no closing page, although `epilogue.closed`'s own text ("For years the night watch was doubled") is written for exactly that history. | INT/BEL (chosen loss, about -1 BEL) | Proposal for the coordinator: add `horzalah.trickster.guard_called` as an alternative to `horzalah.started` on `epilogue.closed` (RequiresAnyGroups), or add `horzalah.started` to the outmatched choice's Set. Not done: a gate/Set change is outside a voice pass. |
| S11 | Recorded: flags set and never read with no promised consequence: `beat.agent_asked`, `beat.told_stronger`, `guild.kept` (a seen marker), `refused.reached` (read through `declined` minus `refused.brand`). `horzalah.presence.failed` has no producer in the export because the engine sets `<presence>.failed` when the anchor fails. `beat.knife_nicked` did promise a mark "you will have to explain"; it now has partner-page readers (S1 paragraph set). | none | Left. |

Checked and not defects: `ch5.nothing`'s "Hepzamirah is dead in the mines of Colyphyr" is Chapter 5 and Colyphyr is
Act 4 (`hepzamirah.dead` is the ColyphyrHepzamirahDead etude), so no reveal before staging; every recollection node
reads its own native witness (`named_horzalah`, `rescue_refused_told`, `spawn_told`, `parley.latched`,
`gift_delivered`/`gift_given`/`guild_seen`, `yozz_killed`/`yozz_spared`, `met_q3_a/b`, `greybor_explained`,
`yozz_confession_heard`, `seals_seen`, `scar_seen`). `refused` (three producers) is disambiguated everywhere by
`came_herself` and `let_go`; `returned` (18 producers) is always paired with its branch flag; `left_free`'s two
producers mean the same thing. Presence is earned: every Drezen beat needs `wants_heard` + `present_now`, the Guild
pages need `primed`, the epilogues forbid `dead`, and `left_free` clears `present_now`. The Chapter 4 projection rule
holds (`ch4.scar` is the projection). Nocticula's court line ("walked into my city's Guild ... pinned a box over your
contract") reads as the Guild of her city, not a location claim against `guild.kept` ("our headquarters in Father's
realm"); left unchanged (Claude-locked, in voice).

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten (all in `storylines/horzalah_cloud.py`, applied last in `expansion._make_expansion`):
`late.at_night` no_priest, dismissed (S5, S6); `beat.ear` start, room (S6); `beat.spit/backed2`: "Thank you. I will
not say that again" was sincere thanks, which she never gives (writer `voice.md` never_thanks): now "Do not wait for
thanks. You took my answer out of my hands and left him his tongue"; `beat.name/start`, `beat.sister` back_departed /
back_unavailable (S9); `beat.thousands/others`: the "card at the winter solstice" to a sister was a mortal's kindness
and is now a canary every winter that her sister has not dared open; her native profanity (aaa2721e "That bitch
Hepzamirah", "piece of trash"; 2f36ecf9 "overdressed fool") had all but vanished from 35,000 words (edge MOUTH: one
own-speech hit, "damn"): `beat.sister/start` ("The bitch never forgave me those three heartbeats") and `beat.yozz/start`
("that overdressed piece of trash"); `letter.invoice`, `epilogue.ally` (S7); `epilogue.unanswered` (S3); mourned P7,
P8 (S4); the Ledger entry (S8); new readers (S1, S2).

Left alone (they work, at her register, with on-screen cruelty and her own agenda): the ear con at her mercy and in
the bedroom (`mercy.gift`, `unmet.knife`: "Nobody gives Baphomet's daughter anything, mortal. They sell, or they pay,
or they bleed."; the butcher's look; the barber's grip); the face cut in `guild.kept/threat` ("Now you own my lie");
the dresser on a gold chain, "Take care not to ruin him" (798bf2b5 in her own mouth), "Two owners, doing business
with the things we own"; `beat.board` and `beat.names` (three contracts named, the Commander chooses, the quartermaster
strangled, the priest besieged on his own steps); `beat.masters` ("I enjoy almost everything I do with a knife. If you
were hoping I would stop, you should have killed me when you had the chance."); `beat.head` (a master's head in a
ribboned box as a suitor's custom); `beat.spit/hers` (the Kenabres boy on his knees licking his own spit);
`beat.cup` (poison as a lesson); `beat.knife`, `beat.hat`, `beat.ribbon`, `beat.ramparts` (a client's price torn off,
"I shall kill that one too"); `beat.labyrinth` (the jailers' names kept for the waiting); `beat.father`
("Being promoted"); the chamber and second night ("Mine ... The ear, and the rest of you with it. Say it."); the
collar scenes ("You reach like a buyer"); the Greybor and Wenduag reactions (in voice; the Wenduag review agreed);
the epilogues `together`, `commit`, `decided`, `left_free`, `scarred`, `closed`; the Last Call page (the winners
killed one by one "at the Guild's usual rates, which she paid to herself") and call.

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 91 | 93 | Native anchors unchanged: Q3 mercy lists 8373a8ed/7698f846, NativeReturnCue Cue_4 4a3f22ae ("even the guild"), terminal Cue_0007 c12bda4e, the kills 5de3ea43/717a2f84 closing the route (user ruling), "nothing" (C10) on the stranger path, the seals lifted after Colyphyr (C8), "weaker branch" (Cue_0122 039978569) only when heard. S5 removes a quote attested only on the traitor list. New text invents no place or person beyond unnamed victims; the Absalom sister is pre-existing route continuity. |
| VOI | 85 | 91 | Venom and degradation as in her lines (0ad1af67 "little puppet", 4de7b0dc "carrion heap"); pointed profanity restored at native density where she speaks of the people she despises; the one sincere thanks and the "No, I did not hurt him" softening are gone; her property creed intact (the dresser is property on every branch; freed, she does not condemn ownership). |
| TRK | 92 | 92 | Device unchanged: the con on her own Guild (an ear as a trophy so the Guild bows instead of eating her), Diplomacy 26/24/22 by what the Commander knows, costs `cost.ear`, `cost.late` (100 Favors), `gift_freed`. |
| INT | 90 | 91 | Hooks unchanged (AnswerLists, NativeReturnCue, SelectedAnswers latches, SeenCues readers, NativeEpilogueEdits). The sisters' household outcomes now reach her pages (S1). S10 recorded (-1). |
| BEL | 82 | 90 | Every outcome the household and the Threshold beat promise reaches a page (S1, S2); the unanswered ending ends (S3); no note stands in for her hand (S6); the ally branch shows killing, not invoices (S7); branch-false lines gone (S4, S5, S8). |
| COX | 92 | 92 | No elimination: Hepzamirah keeps her side of the pair; the new readers claim no presence of hers ("the stair of her Alushinyrra hall", not Drezen); Greybor's and Wenduag's reactions untouched. |
| HOW | 86 | 91 | Truth table shipped; every new paragraph reads a flag with a producer in the export; the layer raises on any drifted text, unmatched node, paragraph or ledger line, and on any pending marker in a touched scene; save inventory unchanged. |
| AGY | 80 | 88 | Her own agenda drives her pages: the chair and the masters, the father who does not answer, the sister she sells warnings out from under, the jailers' names, the trade. The sisters' pair outcomes are about her standing and her money, not the Commander. Remaining loss: she still sits in no household row except the sisters' (no other woman shares a beat with her; recorded for the household pass). |
| ALIGNMENT LENS | 86 | 93 | On-screen evil: an ear cut and boxed, a face opened, a deserter hamstrung on the threshold, a surgeon's hand pinned by her knife game, a guard's ear notched, a master's head in a box, three contracts left to run, the courier kept crippled on her stair, a locksmith left in his own lock. Slaver ethics unrepentant: the dresser is owned, given, taken back, kept. Love stays possessive ("It is mine now, mortal. Remember whose."). No redemption, no father's approval (decisions `father_unanswered`). |

## 4. Explicit slots (Gemory tracker)

- Existing: four built slots (`visit.chamber`, `beat.second_night`, `epilogue.together`, `epilogue.commit`) and two
  trackers from the villain-knowledge pass (`beat.ramparts`, `beat.ribbon`). Boundaries untouched: no host node or
  paragraph of theirs changed text (`epilogue.together` and `epilogue.commit` only gain paragraphs appended after the
  slot paragraph's existing successors).
- New tracker: `horzalah.trickster.epilogue.decided.explicit.1` (Commander + Horzalah, host `epilogue.decided/page`):
  the deferred first night after the Commander reached like a buyer or asked whose brand it was; she sets every term.
  Needs a reserved paragraph appended after P3 before generation (recorded in the brief).
- `tests/test_horzalah_round2.py::test_slots_have_briefs_and_one_first_night_per_history` asserted exactly four briefs
  and failed on `main` since the two villain-knowledge trackers; it now counts built briefs (4) and checks each
  tracker's host scene/node exists.
- `slot_brief_lint --strict`: 213 hard before and after (none in `horzalah/`); horzalah warnings 6 -> 7 (the new
  tracker's terminal-boundary warning, as for ramparts and ribbon).

## 5. Proposals for scenes owned by other rows

- `household.docket.horzalah_hepzamirah.account` / `account_table` (Hepzamirah row): the entry is a docket she
  dictates ("Write down what one of them did to the other ... Write her name."), which is close to the paperwork the
  truth page forbids. Proposal: keep the docket mechanics, but stage the naming as an act: "She drives her knife
  through the sheet into the table, through the place where the name would go. 'There. Now it is written.'"
- `household.pair.horzalah_hepzamirah.truce/start` (Hepzamirah row): her line "I will feel that sale go like a pulled
  tooth" works; consider adding her price on the courier's head if Hepzamirah breaks the term ("my sister has a habit
  with couriers"), so the broken_hepzamirah branch reads as a debt she will collect. Not required.
- `minagho_chivarro.trickster.react.baphomet/weaker` (Minachiv row): consistent with C13; keep.
- `hepzamirah.trickster.body.hounds/wrong_princess` (Hepzamirah row): Horzalah's "What did you buy, sister? A
  crusader's room?" is in voice; keep.
- Native epilogue replacement `horzalah.native.eng7_f6c.trio` (engine_f6c, verified against blueprints): opens "She
  joined forces with Greybor ... The three former companions"; whom "She" names depends on the native slide's
  context, which cannot be checked here without enGB. Flag for the coordinator; not edited.

## 6. Validation

- `python expansion.py` cannot complete here: no `blueprints.zip`. The full build ran with only the zip readers
  stubbed (`storylines.native_facts.verify`, `tools.native_fact_inventory.verify_inventory` and its `tools.`-prefixed
  import, `storylines.native_overrides.finalize`,
  `tools.crossroute_checks.other_woman.native_participation_contexts`) through `expansion.make_expansion()`.
- Baseline proof: the same stubbed build of untouched `origin/main` (723ccae, git worktree) reproduces the committed
  `development/Story.json` with 0 scenes and 0 sections different (only dictionary key order differs in one
  native-reader section; the committed export keeps main's bytes outside the changed scenes).
- The committed export on this branch is `main`'s export with the scenes that differ in the stubbed branch build
  replaced, and its Ledger entry, written with `authoring.compiler.serialize(payload, 'expansion', ...)`
  (NativeOverrides carried from `main`). See the commit message for the exact diff counts.
- Export diff vs `main`: 13 scenes differ, all `horzalah.*`, plus the Ledger entry `owed.horzalah`. Only node text
  and appended paragraphs differ (checked: same scene metadata, node ids, choices with Next/Set/gates/checks/costs,
  EnterSet, and every existing paragraph's gates). The stubbed branch build differs from the committed export only
  in `targona.lastcall.page`'s `RequiresAnyGroups` member order (run-to-run noise; main's copy kept).
- Checks (`check()` functions; `main` in brackets): `savecompat` 0 [0]; `payoff_lint` 0 [0];
  `prose_pending_lint(integration=True)` 0 [0]; `claude_work_queue_lint` 0 [0]; `voice_lock_lint` changed locks 233
  [233], none Horzalah's (no Claude-locked scene changed); `edge_lint` locked regressions 303 [303]; Horzalah
  Trickster business:menace 0.268 [0.275], menace hits 254 [247], own-speech profanity 2 [1]; `player_text_lint`
  review 5505 [5506] (Horzalah 4 [5]: the stale dresser line's gender flag is gone); `text_structure_lint` hard 10
  [10], none Horzalah's; `slot_brief_lint --strict` hard 213 [213], briefs 347 [346].
- Unit tests (`python -m unittest` equivalent with the same stubs, `RRT_TEST_STORY` = the export; 12 modules touching
  her scenes): 91 run, 0 failures, 2 errors [1 failure, 2 errors]. The two errors are identical on untouched `main`
  (`test_harem_row_s18x` reads `blueprints.zip` directly; `test_harem_row_j03` fixture shape). Without
  `RRT_TEST_STORY` the tests that rebuild in a subprocess error on the missing zip.

## 7. Not done / handed on

- S10 (outmatched has no closing page): gate proposal above.
- Household integration beyond the sisters: Horzalah has no pair row with any other woman (Wenduag's reactions are
  the only cross-woman beats); a household pass should give her one (Greybor's employer, Nocticula's tenant).
- claude-work-queue.json and prose-pending.json have no Horzalah entries; nothing to resolve.
- Voice approvals: none of the changed scenes is Claude-locked; `voice-approvals.proposed.json` lists the changed
  scenes' new text_sha so the coordinator can lock them if wanted.

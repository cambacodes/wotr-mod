# Devarra: cloud design-first review (villain-route-devarra)

Owner: cloud voice owner, 2026-10-08. Base: wotr-mod `main` 723ccae, merged with `main` 069c708 before push. Scope (CLOUD-QUEUE villain row 14): `devarra.*`,
the S50 pair `household.pair.nidalynn_devarra.*`, her Last Call account (`trickster.lastcall.account.devarra`), and
every page of another woman that speaks about her (Nidalynn's epilogues and Last Call page). Truth pages read: writer
`knowledge/characters/devarra/` (canon, voice, states, decisions, relationships, native-lines.json, 19 lines),
`handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (VOI, AGY, binding contexts 1-6),
`plans/route-redesign-pipeline.md`.

Presence read from the export (`development/Story.json`): 73 owned scenes (4 retired moult-device scenes, 4 flight
scenes, 2 after-scenes, 3 judgment/proposal scenes, 5 reactions, 44 tower scenes, 8 epilogue pages, native egg slide,
Last Call page and call) and her appearances: `household.pair.nidalynn_devarra.{notice,custody,repair}.{widow,chosen}`
(6), `trickster.lastcall.account.devarra`, `trickster.lastcall.last_joke(.areelu)` and `trickster.lastcall.page.last_word`
(gating and the Commander's S50 line only), `dorgelinda.ledger.{other,changed}_columns` (the Commander's disclosure
choice only), Nidalynn's route (`nidalynn.trickster.eggs.*`, `kiln.*`, `steps.widow`, `after.first_demon`,
`door.own_form`, seven epilogue pages and `nidalynn.lastcall.page`), and the Ledger (`owed.devarra`,
`guest.devarra`, `household.pair.nidalynn_devarra.custody.record`). No other villain shares a scene with her, so every
scene above is this row's to edit; Nidalynn is not a villain row, and her lines were left in her voice (only the claims
about Devarra were aligned).

Machine truth table: `truth-table.json` beside this file (225 flags: every producer choice and every consumer gate,
`consumers_before` = count on main, `status` = live / set-never-read / retired-producer-only / read-only-by-retired /
read-with-no-authored-producer, `note` on every flag this pass touched). Regenerate with
`python tools/route_packs/redesign/devarra/truth_table.py development/Story.json <main export>`.

`python expansion.py` was NOT run: this environment has no `blueprints.zip` (it stops in `native_facts.verify`). See
"Validation" for the stubbed differential build used instead.

## 0. Route shape (derived from the export)

One live road reaches `devarra.trickster.returned`: the flight world. `flight.pact` (her lair, before Greybor strikes:
a fable from cover, her tariff paid) -> native escape latched (`devarra.trickster.flown`) -> `flight.leash` (the
stone told she is on an errand) and/or the golems' password (`leash_cut`), `flight.clutch_left` -> `flight.eggs` (she
comes down to the east road for her clutch; every egg fate and confession has its own node) -> `after.tithe` (the
Storyteller's two questions: what she eats, and what happens next) -> `after.lair` (verdict and terms: once a year,
where she chooses, one small bite) -> the tower courtship (44 scenes) -> `after.late_proposal` for the undecided ->
epilogue pages `woken` (committed), `commit` (late acceptance), `pending`, `hungry`, `claimed`, `refused`,
`sacrifice`, `canon_fate`; Last Call page and call for the smallest-egg debt.

Retired on purpose (Option A, coordinator ruling 2026-10-01): the moult device. `dead.lair_story`, `dead.setup`,
`dead.storytellers_version` and `dead.woken` Require `trickster` / `trickster.ever` and Forbid `trickster.ever`, so
`primed`, `story_told`, `cost.story_sold`, `cost.shame_sold`, `cost.late`, `cost.ending_owed`, `cost.kept_whole`,
`storyteller_threatened` have no live producer, and every node or scene that Forbids `devarra.trickster.flown`
(`what_climbed_out`, `the_old_hide`, `the_itch`, `first_snow`, `the_messenger`, `react.greybor.repeat_work`,
`react.storyteller.woken/sold`, and the non-`_free` twin of ~30 tower nodes) is inert. Kept for save compatibility
(pre-release saves are not a defect) and not scored below.

## 1. Structural defects (fixed first)

| # | Defect (export evidence) | Class | Fix (text/paragraph only; ids, choice positions, Next, Set, gates untouched) |
|---|---|---|---|
| S1 | The smallest-egg debt contradicts itself across routes and is never paid. `tower.smallest_egg:want` "I will name it. Tomorrow, when you are old, or at the edge of the world"; `epilogue.woken:page#31` (Requires `devarra.lastcall.called`) printed the same "She had never named what she would take" as `#32` (Forbids it): the called flag had a reader that ignored it. Meanwhile Nidalynn's eight pages (`nidalynn.trickster.epilogue.*:page#21/22`, `nidalynn.lastcall.page#4`) said "At the rift the grey dragon named her bill ... a month of the Commander's every year". `devarra.lastcall.page#0` said "Calling her name at the rift had bought no agreement" (designer note). The Last Call itself was paperwork: `devarra.lastcall.call` "[Read the grey dragon's bill] ... Devarra's bill names the egg you took", `trickster.lastcall.account.devarra` "The bill ... lies with the other demands in your pack" (she has never written anything down). The unanswered branch had no menace at all, though she promised it (`smallest_egg:wont` "I will collect it anyway, from whatever of yours is nearest when I come"). | COX (cross-route contradiction), BEL (promise without payment), VOI (paperwork, binding context 6) | The Last Call is an answer, not a negotiation (the r4 ruling "the call alone settles nothing" kept): the call node is re-staged without paper (turn north and say her name and the debt into the wind off the Wound; or say nothing and let her collect). She names the price herself afterwards, on her ridge: a month of the Commander's every year (`woken#31`, `lastcall.page#0`, and two new readers each on `pending`, `hungry`, `claimed`). Unanswered, she collects from whatever is nearest, every spring (`woken#32` and the new readers): a horse eaten in the citadel yard, the hound by the Commander's door, the groom who did not run. `refused`: never collected and never released (new reader). Nidalynn's claim lines no longer name a price (they keep her voice and her point: not the child, not the silver). |
| S2 | S50 pair row: wrong speaker and unearned claims. `household.pair.nidalynn_devarra.notice.*:account` choice 0 "She named her price for the smallest egg" before any naming exists; choice 1 "She has claimed a debt" is gated on `devarra.trickster.debt_claimed`, which is the COMMANDER's "Then you owe me" in `flight.eggs:clutch>8` (her answer: "Dragons do not owe, crusader. Dragons are owed ... You will not like the coin"); the node asks "what did the grey one ask of you?", and choice 2 "She has not named a bill for it", while `household.pair.nidalynn_devarra.ready` (`nidalynn.trickster.hatched` + `egg_owed`) does not require Devarra alive: the question leaks a living, speaking Devarra into runs where she died in the lair or the Sanctum. | Wrong speaker, presence not earned (binding context 3), unearned outcome | Text only (J03: no paragraphs on pair rows): Nidalynn asks "And her mother? Has she come asking what you owe for this one?"; answers "She has put a life on my head for it. She hasn't said whose." / "I told her she owes me for her clutch. She said dragons are owed, and that I wouldn't like the coin." / "Nobody has come asking." (true dead or alive); Nidalynn's reply to the debt answer re-voiced to match ("You told a woundwyrm she owes you ... she'll pay it in something you'd never have asked for"). |
| S3 | FLAG OVERLOAD `devarra.trickster.marked`: set by "They died while I was in the Sanctum. I owe you the account." (`flight.eggs:clutch>6`), "I smashed them. It was my hand." (`>9`) and "I ordered the stone to destroy them." (`>10`), plus the retired moult answer "I watched. I didn't stop them." Its readers were written for the retired answer only: `after.tithe:watch` "she is still deciding what you will watch next" (that promise exists only in the retired `dead.woken:marked`) and `tower.the_clutch:nest` "You watched once. Watch again." (false for the Commander who smashed them). | Flag overload, stale reference to retired content | Both readers re-voiced so they are true for every producer ("She says you told her to her face how her clutch died, and that she has decided you are going to watch something die for it"; "You told me how mine died. Now you see how theirs do."). The confessions themselves already have separate nodes (`marked.responsible.1/2`). No split needed. |
| S4 | Promises and grudges with no reader: `tower.one_short:lied(_free)` "I will add them together when I send the bill" (`twelfth_lied`: 0 readers); `the_hoard:steal_her` the Queen of Iobaria (`coin_stolen`: 0); `the_clutch:vault_no` "Say no to me again, crusader, when you are sure. I will still be listening at your wall" (`vault_refused`: 0, and project eggs behind a refused vault had no fate on any page); `the_clutch:after_nest` "Remember that when you climb to me" (`looked_away`: 0); `first_climb:protect_2(_free)` "I will let you say that once" (`warned`: 0, though `the_dwarf:protect` gives the same answer again); `flight.eggs:owe` "When I have decided what that is worth, you will be told. You will not like the coin" (`debt_claimed`: read only by the S50 pair). | BEL (cost/grudge without consequence), INT | Read-only consumers: `epilogue.woken:page#33-#36` (the lie added to the debt, twelve said twice every spring; the Queen of Iobaria turned over at every appointment; her nights against the vault wall; never shown the Wound twice); `the_dwarf:protect#0` (she pins the Commander among the bones: "That is twice, crusader. I said once."); `the_hoard:honest_her/steal_her/ask_her#0` (she pays the "debt" in an insulting clipped copper, or calls the stolen queen payment). Readers 0 -> 2 each (`warned` 0 -> 1, `debt_claimed` 4 -> 7; the committed copies on `epilogue.commit` counted). |
| S5 | Two bargains end as designer notes, never delivered (claude-work-queue devarra:D03-D06). `the_generals:bargain` "One battle ... the story of it, every death ... If it was not [worth my wings], I will take the difference out of your generals" (`battle_price_accepted`) and `the_generals:ask` "Once. Where I choose, when I choose ... they will not put me in their dispatches ... nobody will thank me" (`battle_offered`): `woken#13` "No such account had been collected", `woken#29` "No report arrived before the march to Threshold; her offer remained unfulfilled". | BEL (unresolved bargain), VOI (report register) | Before the finale, on screen (`tower.before_the_end:climb#0/#1`, the farewell before Threshold): purchased, she refuses to fight for the generals and has been taking the difference out of their horses (a cavalry brand on a bone on the floor); voluntary, she has done it her way, unannounced (a demon column cooked on the Wound side of the supply road; "Nobody thanked me. Good."). The epilogue lines consume that history (`woken#13`: the general who threw the inkwell came down without his boots; `woken#29`: the dispatch said "cause unknown"). The purchased battle is a consequential breach, so no fabricated battle receipt exists (r4 earned-outcome ruling kept); the voluntary one is her own act on her own stated terms. D03-D06 removed from the queue. |
| S6 | Harem integration gap: her own pages never read the S50 row. The pair records whether the Commander fed her daughter Nidalynn's way ("goat, cut small ... I won't have the soldiers teaching her to hunt whatever runs"), but Devarra, whose child it is, never reacts; her agenda (a woundwyrm should eat like one) has no outlet. | AGY | `epilogue.woken:page#37` (Requires `household.pair.nidalynn_devarra.resolved`, `nidalynn.trickster.hatched`, `crossroute.nidalynn.available`; Forbids `left_with_it`): she leaves a deserter with broken legs at the kiln door every spring; Nidalynn lets him crawl away. Both keep their agendas; nobody wins. |
| S7 | The late-acceptance epilogue (`epilogue.commit`, the only page for `late_accepted`; `woken` Forbids it) read none of her history: no cook's knife, druid trail, Xanthir's students, cells, demons' name, vault, egg debt, battles, Nidalynn's child; three report-register lines (`late_accepted#0` "Threshold changed neither her tariff nor the appointment", `page_exit` "Her answer stood."). | INT/BEL (integration gap), VOI | The 27 history readers of `woken` (indices 0-5, 10, 11, 13-22, 24-32) and the five new ones appended to `epilogue.commit:page` after its two bite lines (same gates; the moult-only `#12` and the woken-only `#6-#9`, `#23` slot are not copied); `late_accepted#0` and `page_exit` re-voiced (she blocked the supply carts until she got her answer; "The ridge stayed hers, and so did the Commander"). |
| S8 | Evil off screen where the scene stages it: `the_cells` brings a priest of Deskari up the ridge so that the Commander can "hear what a man says when he knows exactly how little he has left to trade", then sends the Commander down before she eats him (`verdict` "Go down the mountain now", `leave` "I will tell you whether he impressed me"). | VOI (binding context 6) | On screen: `verdict` she burns him from the feet "the way she bastes a stag" and bites him in half (native `5ccf6032` "burn you in my flames, then bite you in half"); `leave` the screaming follows the Commander to the north gate ("she is a patient cook", her own line in `after.lair:cultists`). |
| S9 | Flown-world leftovers of the retired moult in live nodes: `the_dwarf:climb` "the grey seam under her wing" (the seam is the moult's; the flight scar is pale, `the_soft_place:climb_free`, `the_scar:look_free` "It will scar pale"); `the_scar:start` "A neat grey crescent" (contradicts `look_free` two nodes later); `lastcall.page#1` "a grey ladder of crescents"; titles "The Grey Tariff", "The Grey Bill". | CAN (internal contradiction) | Pale seam, neat crescent, pale crescents, "The Woundwyrm's Tariff", "The Smallest Egg". "Grey" as her authored colour is kept where it is not moult-specific (R4). |

No other overload found: `devarra.committed` means one thing from its four producers (`after.lair:bitten(_free)`,
`after.corrected_ending(_remote):bitten(_free)`, `back_up_the_mountain:yes`, `late_proposal:accepted`); egg fates are
read from native `eggs.*` and `native.history.eggs.*`, never invented. No reveal before staging (`the_trail` stages the
gold dragon before `woken#2` uses it; `smallest_egg` requires Nidalynn's confession; `her_name` requires the three
questions). No letter stands in a face-to-face scene (`first_message` refuses paper on purpose). Presence is earned
everywhere except S2 (`devarra.present_now` on every owned scene; the Nidalynn readers add `crossroute.nidalynn.available`).

Recorded, not fixed:

| # | Item | Why not here |
|---|---|---|
| R1 | claude-work-queue devarra:D02: the failed-stealth `pact_open` negotiation hooked to `StoryTellerAndDragonBadEnter/AnswersList_0004` (`c5d8690968d13994f95a22ecefabaa5b`) and its Greybor reaction do not exist. | A new native-hooked scene and reaction (Codex structure); the hook must be verified against `blueprints.zip`, which this environment lacks. Voice target for whoever builds it, in register: her bad-entry threat (`07ec4e7c` "I will devour you whole ... you parasites!") interrupted by a story; "You again? Then talk while I decide which of you is the old dotard's dessert." Entry left open in the queue. |
| R2 | `epilogue.commit:page>1` and `>2` (and their `late_refused` node) Forbid `devarra.trickster.late_accepted`, which the scene Requires: unreachable. | Kept for save compatibility (r4 accepted_ending). |
| R3 | `devarra.harem.stance.joined` / `.tolerated` have no producer, so `guest.devarra` in the Ledger always reads "Not yet at the table." | Matches her registry stance (the ridge is hers; nobody climbs it unsent) but nothing writes it; a household-stance writer is coordinator/Codex structure. |
| R4 | "Grey" as her colour (the grey wing, "the grey one" in Nidalynn's route, the Ledger). It began as the moult's new hide; canon colour is UNRESOLVED (`canon.md` devarra.canon.colour: BlackDragon unit folders, RedDragon etudes). | Used across three routes as an authored descriptor; only the moult-specific uses (seam, scar) were changed. |
| R5 | S50 keeps Devarra off screen ("Devarra is discussed only", s50.md). | A Devarra-present variant needs a new scene gated on `devarra.present_now` + `returned` (structure). Proposal: she lands on the kiln roof during `custody`, drops a live sentry's boot (with the sentry) for the feed, and Nidalynn's Athletics/Materials answers decide whether the child eats it; the cost and witnesses stay as they are. |
| R6 | 20 set-never-read flags remain (truth table): `tower.apologised`, `boasted`, `answer_*`, `twelfth_told`, `tax_paid`, `tax_eaten`, `hide_*` and the other moult-era receipts, `devarra.started`, the S50 receipts (`feed_delivered`, `guardian_kept`, `cost.commander_delivery_paid`, `cost.commander_feed_spilled`, `repair.refused`). | Flavour receipts with no promise in the prose, or retired. Chosen loss (~-1 INT). |
| R7 | `tests/test_devarra_round4.py` `test_last_call_does_not_negotiate_a_price` and `test_military_offers_do_not_supply_a_battle_receipt` assert the old page wording ("never named what she would take", "unfulfilled"/"No such account"). | They build only the route modules, not this late layer, so they still pass; their intent (no price bought by the call; no battle receipt without a producer) is kept. Update their wording when the coordinator accepts this pass. |

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten (all in `storylines/devarra_cloud.py`, called at the end of `expansion._make_expansion`, after every
appender):
- Last Call: `devarra.lastcall.call:call` (node and both choices), `trickster.lastcall.account.devarra` (node, title,
  entry), `devarra.lastcall.page` title and `#0/#1` (S1, S9).
- Epilogue pages: `woken#13/#20/#26/#29/#31/#32` (designer notes: "No such account had been collected", "The thief's
  bill was a separate matter", "Devarra never called the thief's bill a price paid for custody", "her offer remained
  unfulfilled"); `commit:late_accepted#0`, `commit:page_exit`; `pending:page` and `claimed:page` bodies (report
  register: "No annual appointment had been made", "No Commander climbed to collect a dragon promised by a story").
- `the_cells:verdict/leave` (S8), `after.tithe:watch`, `the_clutch:nest` (S3), `the_dwarf:climb`, `the_scar:start` (S9).
- S50 `notice.*:account/debt` (S2). Nidalynn's two claim lines (S1), her voice otherwise untouched.
- 50 appended gated paragraphs (S1, S4-S7).

Left alone (they work, and are the route's bar): `flight.pact` (the fable from cover, "Come out and I will eat you
second, after the storyteller ... I will decide how long you keep your legs"), `flight.leash`, `flight.clutch_left`,
`flight.eggs` (every egg fate and confession: "Your hand broke them ... I like to play with my food. Do not imagine that
makes you anything else"), `after.tithe` (four oxen from the east road; the cultists or the farms), `after.lair` (the
babau limb that still kicks; "I kept one alive for a day to see whether he would. I am a patient cook"; her terms),
`first_climb` (the stone of the doorway runs red beside the Commander's head), `her_questions`, `the_tax` (she eats
the proclamation, seal and all), `the_clutch` (the cook eaten, "a thing that cooks a mother's children should know, at
the end, what it is to be food"; the vrock brood burned), `bane`, `first_bite` (the bite, "Mine"), `what_she_says`,
`what_happened_next`, `the_dwarf` ("The ones who are good at killing you are the only ones worth remembering"),
`the_scabs`, `the_ring`, `the_flight`, `the_generals`, `after_the_abyss`, `wrong_sky`, `a_story_for_nothing`,
`under_the_wing`, `before_the_end` ("I will go down there and find what is left of you and bring it back up this
mountain and eat it"), `the_drovers`, `her_name`, `the_meal`, `the_soft_place`, `the_hunt` (the first bite of a demon at
dawn), `the_garrison_book`, `on_the_roof`, `first_snow_free`, `his_story`, `the_trail`, `one_short`, `smallest_egg`, the
reactions, `epilogue.sacrifice` (the door carried off, frame and lintel), `epilogue.refused`, `epilogue.hungry`,
`epilogue.canon_fate`, and the rest of `epilogue.woken`.

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 90 | 91 | Lair, clutch and Sanctum match the native cues (`05070eba` the Storyteller under her claw, `9de6c3aa` "How dare you injure me?", Golems_DragonEggs `b8dfb42d`/`Cue_0028`, RedDragonEscaped latch, egg fates `eggs.*`). DLC1 facts stay out of the main campaign. Authored, labelled in the module: the tower, the month, the herald, the deserter, the burned column. Fixed the scar/seam contradiction inside the flown branch (S9); her colour stays an authored descriptor (R4). |
| VOI | 84 | 92 | The route was already in her native register: food words for people (`07ec4e7c` "parasites", `05070eba` "I do love to play with my food"), concrete bodily threats (`5ccf6032`), memory as a weapon (`3b37a8b4` "dragons have excellent memories"; "Do not think I have forgotten", `ce8e21b7`). The failures were the paper bill at Last Call and the report-register epilogue lines (binding context 6), and the meal she staged and then ate off screen. Now: the priest burned from the feet and bitten in half on screen; "That is twice, crusader. I said once."; a clipped copper flicked at the Commander's chest as payment; interest taken in horses, a hound and a groom. No profanity added (her pack has none; edge MOUTH 0). |
| TRK | 92 | 92 | The fable from cover that buys her tariff, the lie told to the stone ("The lizard is on an errand"), the wedged door: this Trickster's devices, unchanged. |
| INT | 87 | 91 | Native hooks unchanged (GoodEnter `AnswersList_0030`, RedDragonEscaped, Golems_DragonEggs, Ivory Sanctum spawn gate). Every promise now has a reader (S4-S6); the overloaded flag reads true for each producer (S3); the late page reads the history (S7). -2 for R1 (no failed-stealth entry), -1 for R6. |
| BEL | 82 | 91 | The egg debt is paid or collected with a cost on every page (S1); both battle bargains resolve before the finale, one by consequential breach (S5); Nidalynn and Devarra fight over the child's diet after the war (S6). Reactions: the Storyteller, Greybor, the generals, the north watch, Nidalynn. |
| COX | 86 | 92 | The Nidalynn/Devarra contradiction on the named price is gone (S1); a dead Devarra no longer speaks through the S50 row (S2). No other woman is required dead, hostile or closed. |
| HOW | 88 | 92 | Truth table with statuses; every new reader is a flag-gated paragraph on an existing node; the module raises on any missing scene/node, changed gate or changed upstream text; R1/R3/R5 name the exact structure needed. |
| AGY | 78 | 89 | In S50 she was talked about with words she never said (S2); now the row says only what is true, and her own epilogue acts on her agenda against Nidalynn's (S6). She still has no on-screen beat in the pair row (R5, -2). Her other relations keep their own agendas: the Storyteller refuses to carry her dinner (`the_cells:start`), Greybor bills repeat work, the generals throw inkwells. |

ALIGNMENT LENS (chaotic evil woundwyrm, no creed but brood, hunger and her own life): on screen she eats the cook who
salted her eggs, keeps a cultist alive a day to see whether his god comes, burns a priest of Deskari from the feet and
bites him in half, burns a vrock brood while the Commander watches, takes interest in horses, hounds and a groom, leaves
a crippled deserter for her daughter's dinner, sends a herald's horse back without the herald. Her motherhood is a
grudge and a debt, never a softening (`fbd50942`/`ce8e21b7`; s50.md); her attachment to the Commander is possession
("You are mine. You are the thing I have decided to keep") and appetite ("you have made yourself very interesting
food"). Nothing in this pass redeems her; the month she takes is a creditor's, not a lover's.

## 4. Shared scenes owned by higher rows (proposals only, not edited)

None: no scene she appears in has a second villain. Gating-only appearances (`trickster.lastcall.last_joke(.areelu)`,
`trickster.lastcall.page.last_word`, `dorgelinda.ledger.*`) need no text change. Proposal for the coordinator: R5.

## 5. Explicit slots (Gemory tracker)

Existing briefs re-checked against the changed text: `devarra.tower.first_bite.explicit.1` (unchanged boundary),
`devarra.tower.under_the_wing.explicit.1` (unchanged), `devarra.trickster.epilogue.commit.explicit.1` (inline after
"The Commander stayed until dawn."; its successor sentence is unchanged; the re-voiced `late_accepted#0` follows it),
`devarra.trickster.epilogue.woken.explicit.1`: `last_lines` updated for the re-voiced `#26/#29/#31/#32` and the five new
following paragraphs `#33-#37` (the slot paragraph is `#23`; every later paragraph is conditional, so each is a
possible next beat). New brief: `devarra.tower.before_the_end.explicit.1.json` (Commander + Devarra, the last night
before the march to Threshold, from `if` or `owe_free` to `end_her`; tracking only until a slot node gated on
`devarra.tower.first_bite` exists, so it is never a first night). Both Commander variants; dragon body only.
slot_brief_lint (strict, all briefs) on main 069c708 351 briefs / 213 hard / 189 warnings -> branch 352 / 213 / 189; Devarra
briefs: 0 hard, 2 warnings (pre-existing background "Greybor" mentions).

## 6. Validation

- Build: `python expansion.py` cannot run here (no blueprints.zip). Stubbed full build (only the zip readers stubbed:
  `storylines.native_facts.verify`, `tools.native_fact_inventory.verify_inventory`, `storylines.native_overrides.finalize`,
  `tools.crossroute_checks.other_woman.native_participation_contexts`; then `expansion.make_expansion()`) of untouched
  origin/main (723ccae, and again 069c708 after the merge, git worktree) reproduces main's committed export scene for
  scene (0 differing scenes after RequiresAnyGroups member order); only the zip-derived `NativeOverrides` differs, carried
  from main.
- Branch export = branch stubbed build serialized with `authoring._serialization.serialize(payload, 'expansion', ...)`,
  `NativeOverrides` carried from main. Diff vs main: 26 scenes (15 `devarra.*`, 2 S50 `notice.*`, the Last Call account,
  7 Nidalynn epilogue pages, `nidalynn.lastcall.page`); checked structurally: identical node ids, choices (all fields but
  Text), paragraph gates and scene fields; 50 paragraphs appended, none on a pair row; 15 node texts, 8 choice texts,
  17 existing paragraph texts and 3 titles/entries changed. `targona.lastcall.page` (RequiresAnyGroups member order only,
  run-to-run) carried from main.
- savecompat 0, payoff_lint 0, prose_pending_lint (integration) 0, claude_work_queue_lint 0 (220 entries; D03-D06
  resolved), voice_lock_lint: no Devarra or Nidalynn lock; changed-lock set identical to main's (236, pending other
  rows' enrolment); player_text_lint 5494 review rows = main, therapy warnings 19 = main; text_structure_lint 10 hard =
  main 10 (none Devarra); edge_lint devarra/trickster business:menace 0.535 -> 0.47 (menace 43 -> 51), devarra/base
  0.163 -> 0.168 (the copies of existing lines on `epilogue.commit` and "Those were my terms").
- Unit tests (stubbed, RRT_TEST_STORY = the branch export): test_devarra_round2, test_devarra_round3, test_devarra_round4, test_lastcall_history_inventory, test_nidalynn_round2, test_nidalynn_round4, test_voice_lock_lint, test_edge_lint, test_payoff_departure_contracts, test_savecompat_baseline: 80 run, 0 failures, 0 errors, 1 skipped. Before the brief fix, test_devarra_round2.test_farewell_and_epilogue_current_fates failed with KeyError 'last_lines' (the under_the_wing and epilogue.commit briefs had none; pre-existing on main), now passes. test_harem_row_s50 cannot run here: its fixture rebuilds in a subprocess that needs blueprints.zip, and the harem-less stubbed build (RRT_TEST_BASE_STORY) stops in hub_attachment_lint on missing household.ensemble.ch5.arrows / household.docket.gesmerha_jerribeth.account, identically on main (before this layer runs; the layer skips S50 edits when the rows are absent). C# tests not run (no dotnet build here).
- claude-work-queue.json: D03-D06 removed (resolved, S5); D02 kept (R1). prose-pending.json: no Devarra entries.
- Voice approvals: no Devarra, Nidalynn or S50 scene is voice-locked; `voice-approvals.proposed.json` lists before/after
  `text_sha` for every changed scene so the coordinator can enrol them.

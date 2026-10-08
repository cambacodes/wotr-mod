# Wenduag: cloud design-first review (villain-route-wenduag)

Owner: cloud voice owner, 2026-10-08. Base: wotr-mod `main` abb97e4. Scope (CLOUD-QUEUE villain row 8): `wenduag.*`,
every household pair, ensemble, Last Call and epilogue scene she appears in, and her Lann and Yaniel interactions.
Truth pages read: writer `knowledge/characters/wenduag/` (INDEX, voice, route, states, native-lines.json, 560 lines),
`handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (binding contexts 1-6), `plans/route-redesign-pipeline.md`.

Presence read from the export (`development/Story.json`): 495 owned scenes (4 early companion scenes, 8 legacy
bid/fall scenes, 9 return-device scenes, 2 Lann reckonings, 22 court scenes with their `.native_visit` twins, 4 echo
scenes, 8 reactions, 10 base epilogues + 426 generated native-epilogue partner variants, Last Call page and call) and
47 appearance scenes: `household.pair.seelah_wenduag.*` (11), `household.pair.wenduag_arueshalae.*` (9),
`household.pair.wenduag_vellexia.*` (3), `household.pair.wenduag_dorgelinda.*` (4), `household.pair.camellia_wenduag.*`
(2, Camellia's row), `household.ensemble.ch3.supper`, `household.ensemble.ch5.arrows`, Jerribeth's commission /
counterfeit audience / room measure, `minachiv.the_remaining_customers` and `minagho_chivarro.trickster.react.wenduag`
(Minachiv's row), 8 `horzalah.trickster.react.wenduag_*` (Horzalah's row), the Dorgelinda ledger gates and the two
`trickster.lastcall.last_joke` pages. No `yaniel.*` or `lann.*` scene names her; her Yaniel and Lann material lives in
her own scenes (`early.yaniel`, `court.yaniel`, `killed.*`, `lann.truth`, `lann.found_out`, `react.lann_*`, the claim).

Machine truth table: `truth-table.json` beside this file (936 flags containing `wenduag`: every producer choice and
every consumer gate, `consumers_before` = count on main, `status` for set-never-read / retired-producer-only /
read-with-no-authored-producer, notes on the flags this pass touched).

`python expansion.py` was NOT run: this environment has no `blueprints.zip` (it stops in `native_facts.verify`). See
"Validation" for the stubbed differential build used instead.

## 0. Route shape (derived from the export)

Live roads to `wenduag.trickster.returned` / `with_you`:
1. Kept companion (never killed or thrown out): `with_you` through `q3_turned_on_him`, `q3_spared`, `redeemed` or
   `trickster.bought` (Crystal bid). Court chain: trial -> gate -> claim (stance) -> cairn -> morning, hunt, gongs,
   neathers, vellexia, yaniel, stinger.
2. Killed at Neathholm (native Lann duel kill): `killed.stage` (Mobility check, clean/deep stroke) -> `killed.cairn`
   (Lore/Knowledge read, Bluff for Lann alone or watching) -> `killed.back` (dug out, knife) -> `ch4.stone`,
   `killed.cellar`, `lann.truth` / `lann.found_out`.
3. Echo (Shyka's page): `echo.abyss.prepare` -> `pickup` -> `return` -> `trust` (Lann's cost).
4. Thrown out and alive: `exile.ch5_hunt` (the orchards) -> `orchard_return`.

Retired on purpose (eng7-l10 and eng8-q8h: the scenes Require and Forbid `trickster.ever`): `traitor.bid`,
`traitor.nerves`, `exile.bid_hub`, `exile.bid_traitor`, `exile.champion`, `exile.late_bid`, `abyss.fall`, `street.fall`.
So `abyss.back`, `street.back` and every reader of `fall_agreed`, `abyss_cairn`, `street_cairn`, `brask_knows`,
`cost.unplanned`, `cost.watch`, `lann.knows` are inert. They are kept for save compatibility and not counted below.

## 1. Structural defects (fixed first)

| # | Defect (export evidence) | Class | Fix (text/paragraph only; ids, choice positions, Next, Set, gates untouched) |
|---|---|---|---|
| S1 | Promises and costs with no reader. `early.gate` (ch3): `want` "I'll wait. He'll forget... I never do" (`gate_early.fought_for`), `mean` "I'll cut the sleeves off his precious coat... He'll remember" (`let_her`), `guest` "I'll remember whose guest I am, too" (`rebuked`): 0 readers; ch5 `court.gate` restages Brask as if they had never met. `court.gate:after_rebuked` "He's going to pay for that, and not to you" / `after_hers` "I'm going to remember this. You'll see how" (`gate.*`): the claim pays it but never says so (0 readers). `early.teeth:which` "When you stop being strong, I'll tell you. I'll be the first to" (`early.teeth.stare`): 0. `exile.ch5_hunt:found_you` cuts the Commander "so that you will remember it" (`cost.bled_outside`) and `sava` "You're late with it. You'll pay for that, one day" (`cost.late`): 0. `crystal.bid:both` "I'll see which of you is standing" (`crystal_both`): 0. `ch4.stone` (the grave-stone in the pack, `stone.kept/pocket`): 0. `court.gongs:stronger` "Or am I only strong while I'm pointed at your enemies?": 0. `yaniel.rival` "you don't warn anyone first": 0. | BEL (cost without consequence), INT, HOW | 26 read-only consumer paragraphs: `court.gate:gate` (x2 twins, 3 gate_early readers), `court.claim(_in_person):her` (3 gate readers: she pays Brask's debt on screen, heel on his neck), `court.trial:her` (teeth.stare), `court.trial:which_orchard` (the orchard scar), `court.trial:reckoning` (crystal_both), `court.morning:stone` (stone.kept/pocket: "two pieces of two graves"), `lastcall.call:call` (stone.pocket without the morning stone), `epilogue.pack` (cost.late with orchard_return, gongs.stronger, yaniel.rival). Readers 0 -> 2-4 each. |
| S2 | Reaction before the choice: `court.claim(_in_person):partner_secret` text ends with "Cold water before dawn, then. No wearing my smell like a trophy." before the player picks between "Let him find out" and the wash answer (`partner.scent_hidden`); the unwashed answer contradicts what she just said. Source: `wenduag_partner_stance._claim_nodes` appends the line to the node text. | BEL/HOW | Line re-staged as her offer of both ("Or wash it off... I'd rather he caught it."), so every answer follows it. |
| S3 | Dead paragraphs: `epilogue.pack:page#60/#61` (Vellexia's empty window) both Require and Forbid `participant.vellexia.available`; the gone-Vellexia history of the hunt has no reader. | BEL/COX | Indices kept; two appended readers for `vellexia.hunted` / `vellexia.left` forbidding `participant.vellexia.available` (the ribbon tied on her snares; "the only hunt anyone ever stole from her"). |
| S4 | Harem integration gap: her epilogue never reads her household. Seelah lover (`household.pair.seelah_wenduag.choice.both_yes`) and Arueshalae lover (`household.pair.wenduag_arueshalae.choice.both_yes`) are read only by their own morning rows; Rusk hanged (`restraint.execution_ordered`) has 0 readers; Rusk kept alive (`boundary.kept`) is read only by the next pair row. | AGY/BEL | `epilogue.pack` reads all four (lovers gated on `seelah.present_now` / `participant.arueshalae.available`; Rusk's finger worn until it rotted; Rusk as "the best snare she ever set", forbids `captive.rusk_dead`). |
| S5 | Designer notes and legal register in the 27 partner-state continuity lines (`wenduag_partner_stance.ending_paragraphs`, copied onto every non-native epilogue, baked into the node text of the 426 native partner variants, and onto the Last Call page): "Her answer had bought no word from him; none was put in his mouth", "nothing proved where he was now", "nobody could answer for his present wishes", "No accusation had reached the lovers; no pardon had been asked or given". Two copies of the first line diverged (endings_job3 rewrote 6 paragraph copies; 48 baked copies kept the old text). On `epilogue.dead` (she stayed dead) the unchosen line read "The Commander made no new bargain about Lann". | VOI (binding context 6), BEL | All 27 (+ the divergent copy) re-voiced in place: same gates, same indices, and the same text everywhere it is baked. Each line now works on every page that can show it (dead, refused, unclaimed, pack, native, Last Call): possessive, mocking, crude where she speaks of Lann. |
| S6 | Villain softened to make the household work: `household.pair.seelah_wenduag.restraint(.after_stood):result_0` has her proclaim Seelah's code ("every enemy who yields or is taken goes alive and whole to guarded custody. No knives in the questioning. No trophies."); `debt_repayment:result_0/1` pay the debt in paperwork ("hands Wenduag the patrol report to mark", "signs the watch report beside Wenduag's mark"); `morning:start` "My hunters know the rule." The slot brief for the same pair already says "Wenduag's prisoner rule is not a moral conversion". | AGY (cap 60), VOI | Same flags, her reason: Rusk is bait ("Dead, he's meat for crows. Alive, he's bait... Bait that can't scream for its friends is no use to anybody"); the extraction night is on screen (the yard shut behind the archers, Rusk hears every friend die); "Bait. Not meat. Not yet." |
| S7 | Last Call page: duplicated subject from a string splice ("Wenduag kept to the shadow of the cellar stair. Wenduag listened to it from the cellar stair...") in two funeral paragraphs; Dorgelinda line in report register ("never disowned her advice on the Fellows"). | VOI | Re-voiced in place. |
| S8 | Recorded, not fixed: FLAG OVERLOAD `wenduag.closed` (stay_dead x3, ch5_hunt stay_dead, claim "no", `partner_exclusive_refused` "We end it", echo depart). Epilogue pages split it with secondary flags (`stay_dead_ordered`, `court.claim_refused`, `echo.abyss.departed`), but `partner_exclusive_refused` sets only `partner.exclusive_refused` + `closed`: no Wenduag page can show, and the EXCLUSIVE+REFUSED stance paragraph (pack #44 etc.) is unreachable. | BEL/HOW | Needs a Set change (proposal for the coordinator/Codex: add `wenduag.trickster.court.claim_refused` to `court.claim(_in_person):partner_exclusive_refused>2`, or let `epilogue.refused` accept `partner.exclusive_refused` in a RequiresAnyGroups split). Out of a text-only pass. `ch5_hunt:stay_dead` closing into the native epilogue is canon standing (binding context 1) and is fine. |
| S9 | Recorded: retired legacy bids/falls (section 0) leave inert readers and 23 retired-producer-only flags; `household.pair.seelah_wenduag.restraint(.after_stood):start` carries two identical "Later." answers (indices 2 and 3). | none | Kept for save compatibility. |
| S10 | Recorded: 66 set-never-read flags remain (truth table). They are bookkeeping or flavour receipts with no promise in the prose: `early.teeth.smile/afraid`, `early.walls.*`, `custom_read`, `lann.alone/watching`, `cairn.bare`, `primed`, `stroke_clean`, `cellar.seen`, `partner.acknowledged`, `gongs.saw`, `cairn.knife_held/rolled`, `yaniel.watched/jealous/mistake/kept`, `brask.met`, `trickster.secret.wenduag_cairn`, the pair `cost.*`/`.refused`/`.done` receipts (harem-wide pattern), and the retired-scene receipts. | INT (chosen loss, ~-1) | Left. |

No other flag overload: `returned` has one meaning from every producer (branch reads split it with `orchard_return`,
`echo.abyss.returned` and the cairn flags); `yaniel.*` is produced by `early.yaniel` and `court.yaniel`, which forbid
each other; `cost.lied_to_lann` has one meaning. No reveal before staging found (Lann's `partner_share_shock` /
`partner_exclusive_shock` handle the "she's alive" reveal when the claim scene is his first sight of her). No letters in
face-to-face scenes. Presence is earned everywhere (`present_now`, `in_party`, `with_you`; household rows on
`harem.eligible`).

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten (all in `storylines/wenduag_cloud.py`, hooked at the end of `endings_job3.wenduag`):
- Partner-state continuity lines (S5), the two flat Lann-truth epilogue lines ("The confession kept this quarrel from
  swallowing their friendship"), the unbrought-stinger line, three Last Call lines (S7).
- `household.pair.seelah_wenduag` restraint/restraint.after_stood `result_0`, debt_repayment `result_0`/`result_1`,
  morning `start` (S6). Seelah's own lines kept in her register.
- `court.claim(_in_person):partner_secret` closing line (S2).
- `court.vellexia:remembered` was a shrug ("I remember her. Nothing left to hunt here, though."); now her native
  register on Alushinyrra (`8115c490` "the slut with the fake blond hair who surrounds herself with a dozen stupid
  admirers").

Left alone (they work, and are the route's bar): `early.teeth` ("That's better than a knife, sometimes. A knife you have
to clean"), `early.walls`, `early.gate`, `early.yaniel`, `killed.stage/cairn/back` (the burial device, "Give me one reason
I shouldn't open your throat for it"), `ch4.stone`, `killed.cellar`, `crystal.bid`, `exile.ch5_hunt`, `lann.truth`,
`lann.found_out`, `court.trial` (knife on the throat, "Get somebody to sew that. I'd do it, but I'd enjoy it too much"),
`court.gate`, `court.claim` (Brask hauled in like a carcass, two fingers broken, the button), `court.cairn`,
`court.morning`, `court.neathers` (Tuhk walked down the oldest stair to die), `court.hunt` (the raw heart), `court.gongs`,
`court.stinger`, the echo scenes, the reactions, `household.pair.wenduag_arueshalae.*`, `wenduag_vellexia.*`,
`wenduag_dorgelinda.*` (Dorgelinda's quartermaster register is hers; Wenduag's "I said hang them. They hung." works), both
ensembles, and the epilogue page bodies.

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 92 | 92 | Neathholm, Sull, Hosilla, Savamelekh's poison and call (`a066d670`, `58444f0b`), her father among his children (`2a23c689`), the gong (`560aba94`), spider legs (`54565fae`) all match. Authored: Brask, Rusk, Tuhk, the cairns, the Isles stone; no new lore added in this pass. |
| VOI | 85 | 93 | Route scenes already at her native level (`829669e9` prey-terror grin in `court.gate:hers` "Uplanders always smell best afraid"; `f97b4b9a` culling in `court.neathers`). Fails were the continuity lines (designer notes) and the Seelah conversion. Now: "Dead, he's meat for crows. Alive, he's bait" (`bf5fe56d` "the weak will also be useful"), "ate his share of the supper that night" (`f97b4b9a`), "the slut with the fake hair" (`8115c490`), the heel on Brask's neck (`627bdc70` "Do you want to live? Beg."). Profanity stays modest (edge MOUTH 5 hits / 11.6k words); her cruelty is carried by acts, which is her native pattern. |
| TRK | 93 | 93 | The cairn with the head end loose, the stroke along the ribs (Mobility 24), the hooked shaft (echo) are this Trickster's devices; unchanged. |
| INT | 88 | 92 | Native hooks unchanged (Lann duel kill, Q3 turn/spare/betray, Savamelekh dead, Crystal). Promise readers added (S1); retired content recorded (S9). -2 for S8 (needs a Set change). |
| BEL | 83 | 92 | Every promised reckoning now lands in a later scene or epilogue (S1); costs paid in orchards and at the gate are read; household lovers and Rusk reach her epilogue (S4). |
| COX | 93 | 94 | Vellexia-gone history now has a reader instead of two dead paragraphs (S3); other women's agendas untouched. |
| HOW | 88 | 92 | Truth table with producers/consumers and statuses; every new reader is a flag-gated paragraph on an existing node; S8 proposal names the exact choice. |
| AGY | 72 | 92 | Seelah pair: she keeps the prisoner for her own reasons and on her terms (S6); Seelah keeps her code; Arueshalae and Vellexia pairs already competitive; ensembles (Nenio, Delamere, Seelah) unchanged and in voice. |

ALIGNMENT LENS (neutral/chaotic evil, survival of the strongest): on screen she culls (Tuhk), maims (Brask's fingers),
eats the heart, holds a knife to the Commander's throat to test strength, uses a bound man as bait and lets his
friends die screaming under his window, takes a hanged man's finger. Her loyalty stays a bet on strength (`001cd911`,
`ca9624d7`); nothing in this pass redeems her, and her household compromises (Seelah, Vellexia) are twisted compliance
that keeps her agency.

## 4. Shared scenes owned by higher rows (proposals only, not edited)

- `household.pair.camellia_wenduag.settle/retry` (Camellia's row): works. Proposal: in `reversed`, give Wenduag one
  crude beat at the princess ("Keep pointing, princess. I'll keep my hunters off your skirt.") to match her rival register;
  optional.
- `horzalah.trickster.react.wenduag_*` (Horzalah's row): in voice; no change proposed.
- `minachiv.the_remaining_customers`, `minagho_chivarro.trickster.react.wenduag` (Minachiv's row, merged): no change.
- `jerribeth.commission/counterfeit_audience/room_measure` (Jerribeth's row, merged): in voice; no change.
- `trickster.lastcall.last_joke(.areelu)`: gating only; no Wenduag text.

## 5. Explicit slots (Gemory tracker)

Existing briefs re-checked against the changed text: `wenduag.trickster.court.cairn(.native_visit).explicit.1`,
`court.gongs(.native_visit).explicit.1`, `epilogue.pack.explicit.1` (paragraph 6 and its anchor unchanged),
`household.pair.seelah_wenduag.choice.explicit.1` (its "prisoner rule is not a moral conversion" fact now matches the
pair text) and `household.pair.wenduag_arueshalae.choice.explicit.1`: boundaries unchanged, no edit needed.
New brief: `explicit_slots/wenduag/wenduag.trickster.court.hunt.explicit.1.json` (Commander + Wenduag in the thorn
after the raw heart, `ate` branch, only after `court.cairn`; tracking only until a gated slot node exists between `ate`
and the scene end). slot_brief_lint --strict: 337 -> 338 briefs, hard 253 -> 253 (all pre-existing, none Wenduag),
warnings 176 -> 177 (the new brief's background "Lann" mention).

## 6. Validation

- Build: `python expansion.py` cannot run here (no blueprints.zip). Stubbed full build (only the zip readers stubbed:
  native_facts.verify, tools.native_fact_inventory.verify_inventory, native_overrides.finalize,
  crossroute_checks.other_woman.native_participation_contexts) of untouched origin/main reproduces main's committed
  export scene for scene (only `targona.lastcall.page` RequiresAnyGroups order differs, carried from main).
  main currently fails that build in `camellia_round2._slots` because e26d856 added two Camellia briefs without an
  `insertion` block; the scratch wrapper skips those two files identically in both builds (out of scope, reported).
- Branch export = branch stubbed build, NativeOverrides and `targona.lastcall.page` carried from main. Diff vs main:
  452 scenes, all `wenduag.*` or `household.pair.seelah_wenduag.*`; text and appended paragraphs only (checked
  structurally: nodes, choices, gates and existing paragraph gates identical).
- savecompat 0, payoff_lint 0, prose_pending_lint (integration) 0, claude_work_queue_lint 0, voice_lock_lint: no
  Wenduag lock; changed-lock set identical to main's (pending jerribeth/minachiv enrolment); player_text_lint 4 = main 4;
  text_structure_lint 2 = main 2; edge_lint wenduag/trickster business 242 -> 141, menace 823 -> 865.
- Unit tests (stubbed, RRT_TEST_STORY = the branch build): test_wenduag_partner_stance, test_wenduag_polish,
  test_wenduag_echo, test_household_pair_seelah_wenduag, test_payoff_departure_contracts, test_voice_lock_lint,
  test_edge_lint, test_harem_row_s09, test_stance_agency pass; 9 failures in test_harem_row_w4_ensemble_ch3,
  test_harem_row_ensemble_ch5 and test_harem_explicit_scope (shamira_arueshalae brief) fail identically on main's
  build (pre-existing). C# tests not run (no dotnet build of the runtime here).
- claude-work-queue.json / prose-pending.json: no Wenduag entries existed; nothing to resolve.

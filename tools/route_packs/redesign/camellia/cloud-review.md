# Camellia: cloud design-first review (villain-route-camellia)

Owner: cloud voice owner, 2026-10-08. Base: wotr-mod `main` 723ccae. Scope (CLOUD-QUEUE villain row 6): `camellia.*`
and every scene she appears in. Truth pages read: writer `knowledge/characters/camellia/` (canon, voice, relationships,
states, decisions, native-lines.json), `handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (VOI, AGY, binding contexts
1-6), `plans/route-redesign-pipeline.md`.

Presence read from the export (`development/Story.json`): 100 owned scenes (~52k words): the kill devices
(`killed.setup_hub/_q1/_q3`), the coffin chain (`killed.late_curtain`, `late_curtain_prepared`, `third_night`,
`performance`, `performance_letter`, `dead.overacting`), the return chain (`returned.terms`, `returned.test`,
`kills_answered.oath`), the living masks (`masks.*`, `early.blood`, `early.cart`), the life together (`beat.*`,
`bond.*`, `evening.*`, `cards.*`, `day.*`, each in base / `_alive` / `_camp` variants), five reactions, eleven
epilogue pages and her Last Call page and call. Appearances: the household pairs she owns by row order
(`household.pair.camellia_arueshalae.*` 8, `camellia_vellexia.*` 6, `camellia_wenduag.*` 2, `seelah_camellia.*` 2,
`soana_camellia.*` 2, `kaylessa_camellia.*` 2, `nenio_camellia.*` 2, `household.smooth.camellia.galfrey_1.*` 2), the
Nurah reactions in which she speaks (`nurah.trickster.react.camellia_*`, 12), Soana's (`soana.trickster.react.camellia_*`,
2), and flag-only consumers in Nurah's, Soana's, Kaylessa's and Dorgelinda's routes. Higher rows own
`jerribeth.trickster.reaction.camellia*` (Jerribeth) and `minagho_chivarro.trickster.react.camellia_bill` (Minachiv).

Machine truth table: `truth-table.json` beside this file (every flag containing `camellia`: producers incl. Derived,
Latches and native readers, consumers incl. paragraphs, presences, books and native-epilogue edits, `consumers_before` /
`consumers_after`, `status`). Scene-id flags (`camellia.trickster.masks.two_lies` etc.) and the runtime epoch flags
(`camellia.presence.failed`, `epoch_*`, `returned_actor_lost`) are produced by the runtime, not by a choice; the table
marks them `runtime`.

`python expansion.py` was NOT run: this environment has no `blueprints.zip`. See "Validation" for the stubbed
differential build used instead.

## 0. Route shape (derived from the export)

Roads to her pages, all Trickster-only (binding context 4):
1. Killed by the Commander's hand or order (`camellia.killed` + `primed`): spirits bargained beforehand (the bowl) ->
   she claws out on the third night (`third_night/dug`, `prepared_clawing`); not bargained -> `third_night/unbargained`
   late vein bargain, or the late curtain at the grave (`late_curtain`, `cost.late`). Raised -> `performance` (Fye's
   bar, "Mireya" the widow) or `performance_letter` -> terms named (blood or name) -> `returned.test` -> committed.
2. Dead otherwise (`dead.overacting`): her price is the Commander's blood every new moon (`cost.spirits_owed`).
3. Kept alive: the `_alive` variants of the lesson, terms and test.
Closures: the grave left shut, the knife handed back, the box left empty, the letter burned, "No names. No knives",
the guard, "put the knife away for good". All set `camellia.closed`; `epilogue.refused` splits them by paragraph.

## 1. Structural defects (fixed first)

| # | Defect (export evidence) | Class | Fix (text/paragraph only; ids, choice positions, Next, Set, gates untouched) |
|---|---|---|---|
| S1 | Contradiction on the closure page. A Camellia the Commander raised and then left (`killed.late_curtain/eng8.price>C2`, `third_night/eng8.price>C2`, `late_curtain_prepared/eng8.price>C2` "[Leave her]", `performance/back` "Stay dead", `performance_letter/price>C2` burn) has `raised` + `declined` + `closed` but no `knows_you_tried`, so `epilogue.refused` shows P7 "Her death stood" (Forbids only `present_now`, `coffin_life`) about a woman who climbed out of the coffin and walked off. | BEL/COX (binding ctx 3: what is true) | P7 re-voiced to hold for both ("In the crusade's register her death stood"); new P10 reads `raised`, forbids `returned`: the register was wrong, she left Drezen veiled, the Commander reads the city's dead for one wound, very neat. |
| S2 | Promises/costs with no reader (truth table `set-never-read`): `kills_answered.oath` "Once. I have always kept to the terms of my own games" (`oath_loophole`, 0 readers) and "Touch her again and I'll show you how convincingly I can kill" (`oath_threatened`, 0); `masks.flies_at_a_window` story/hands, the one night the noise went quiet (`masks.quieted`, 0) while the fed branch is read by `returned.terms/lead`. | BEL, INT | `epilogue.kept` and `epilogue.commit` read both oath flags (appended); `returned.terms(_alive,_camp)/flies` reads `masks.quieted`. 0 -> 2-3 readers each. |
| S3 | Harem integration gap: none of her pages reads her household. `household.pair.camellia_arueshalae.choice.both_yes` and `camellia_vellexia.choice.both_yes` are read only by their own morning rows; `seelah_camellia.method.confession` (Seelah keeps her written confession) and `soana_camellia.claim.left_standing` (0 readers). | AGY, BEL | `epilogue.kept` / `epilogue.commit` read all four, gated on the partner's presence (`participant.arueshalae.available`, `participant.vellexia.available`, `seelah.present_now`, `soana.present_now`). |
| S4 | Kills summarised as paperwork (CHARACTER-TRUTH 2, 12; decisions `kills_on_screen`): `bond.witness(_alive,_camp)/hers` "Two days later, the report says the witness slipped on the wet steps"; `evening.the_prisoner(_alive,_camp)/yes` "Later, the chaplain records that the prisoner died in his chains"; `epilogue.refused` P2 / `refused_living` P0 "sent the Commander the report, folded small". | VOI (ctx 6), BEL | Witness: she takes the Commander, who carries the lantern; she lifts her veil for the witness, steps in as close as a friend, pushes, watches the fall and the stillness with her lips parted, and speaks in the gravel voice (`e8969812`). Prisoner: the Commander hears it from the stair, the body comes up under a short blanket with one wound, the chaplain's "failure of the heart" is now the lie it is (P13 still quotes it). Refusal: a pressed camellia folded into a stranger's washed glove, stiff at the fingertips. |
| S5 | Stale cross-variant staging: in `bond.witness_alive/_camp` the witness is Radan "in a tavern by the river" (`alive_w`, `dead_w`), but `lied` visits "the witness at the infirmary door" and introduces "his veiled Nerosyan customer" (a widow identity only the dead-route Camellia has); `r2.public` and `lied` call a named witness "they"; `bond.not_today(_alive,_camp)/ghost` quotes "that face in the chapel" in every variant; `epilogue.kept` P24 / `commit` P3 "Camellia changed her veil" on pages the living Camellia also reaches. | BEL/HOW | Each variant now matches its own witness (Lethra at the infirmary; Radan at the tavern, with the Commander inventing a widow for the watch); `ghost` and P24/P3 hold for every variant. |
| S6 | Paperwork in place of menace in a pair she owns: `household.pair.kaylessa_camellia` sold a "merchant's description" to a man who "buys such observations"; her cost was perfume and a carrier "not welcome at my door". Writer decisions `ct_no_paperwork` names this pair: "must lead to a blade, not a ledger". Natively she asks for privacy with "this poor elf" and kills her (`363f363e`). | VOI (ctx 6), AGY | Same flags and outcomes (shipment out, her copy burned, the clasp returned, the cover changed). The sheet is a hunting mark; the carrier fetches people to her cellar; on the decoy road he follows the Commander into the tannery lane and she knifes him there, up and in, as close as a friend ("I never keep a man who can be fooled by a coat"). Kaylessa watches and approves. Last Call P5 updated to match; Kaylessa's own epilogue line (burned description, returned clasp, grey cloak) still holds. |
| S7 | Invented appetite: `nurah.trickster.react.camellia_draft` and `camellia_veiled_draft` "I would simply have eaten her". She is a mortal half-elf killer; no eating (decisions `no_invented_blood_lore`). | CAN, VOI | "opened her throat over her own printing press" / "cut her throat". The "supper" metaphor elsewhere stays (native `871ccb20`, the chicken's name). |
| S8 | 22 `[PROSE PENDING]` placeholders in pairs she owns (prose-pending.json and claude-work-queue.json, 22 entries each): `seelah_camellia.settle` reasoned/evidence, `.retry` start/word/refused/reasoned/evidence; `camellia_arueshalae` inspection_camellia x4, inspection_arueshalae (fallen) x2, `company` start>C3 and witnessed_company; `nenio_camellia.settle` lesson/refused/manual_correction/spoiled, `.retry` lesson/refused/manual_correction. | VOI/HOW | Voiced from the approved beats (section 2). All 22 + 22 entries resolved and removed. |
| S9 | Recorded, not fixed: `epilogue.commit` P2 Requires `camellia.committed` on a page that Forbids `camellia.committed` (dead paragraph, text duplicated by kept P23). | none | Inert; proposal for the coordinator: drop or regate to `camellia.trickster.late_committed` in a gate pass. |
| S10 | Recorded: `camellia.closed` carries several closures (grave left shut, knife handed back, "No names", guard, "tame"); every consumer treats it as "route closed" and the refusal page splits the histories by paragraph (`knows_you_tried`, `spirits_owed`, `asked_her_tame`, `called_guard`, `present_now`, `kicked_out`, `raised` after S1). Not an overload. 18 `camellia.*` set-never-read flags remain as receipts with no promise in the prose: `started`, `cost.sexton_paid`, `encounter.knife_on/knife_off/mine/not_today` (their `.morning` twins are read), the derived harem attitudes; pair receipts (`*.refused`, `*.declined`, `*.done`) are the harem-wide pattern. | INT (chosen loss, ~-1) | Left. |

No reveal before staging found: `returned.test/no` ("her name was Mireya, and I made her up") closes the route, so the
amulet confession (`cards.the_amulet/tell`, Forbids `closed`) never replays it; `masks.mireya/who_known` and
`needs_known` read `mireya_known` (Q3 FinalTruth, the amulet scene or the kept amulet). Presence is earned everywhere:
the veiled scenes need `veiled_available` / `coffin_life`; household rows need `harem.eligible` and `present_now`;
`kills_answered.oath` needs the returned victim present. Letters are used only where she cannot be met (dead and
veiled at Fye's, `performance_letter` when the presence failed).

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten (all in `storylines/camellia_cloud.py`, called last in `expansion._make_expansion`):
- S1/S4 refusal pages: base line ("Her name remained among the crusade's records" -> "she did not knock twice"), P2,
  P5 (a pressed camellia a year, and a body that week in whatever city it was posted from), P6 (thrown out, two men in
  the canal with one wound), P7, P8, P9 (the dismissal register lines), new P10.
- `epilogue.kept` P15: the list kept as a record ("the Commander could watch the ink dry") is now complicity: a fresh
  line through a name, gloves drying by the fire, the Commander deciding to say nothing.
- S4 witness and prisoner kills on screen; S5 variant staging; S6 Kaylessa pair; S7 Nurah lines.
- `household.pair.camellia_wenduag.settle/retry:reversed`: she finishes the snared cultist herself, rapier point in the
  hollow of his throat, eyes on his (native `13fff43a`, `fa214b1b`); Wenduag gets her rival register at "princess"
  (the Wenduag review's section 4 proposal). Flags unchanged.
- S8 placeholders. Seelah: she wants a chaplain-proof place near something holy and gets it unblessed; faced with her
  written confession the polish drops to gravel ("Paper burns so easily. So do tents"), then comes back "like a glove
  drawn on"; "Are all paladins so tender about the difference?" (`895ef55d`). Arueshalae: the treated blade "for a
  man who takes all night to understand it"; fallen Arueshalae smells it like a throat and keeps her hands behind her
  back ("I'm not going to lick it to prove I'm right"), Camellia: "You are going to sit there and want something you
  cannot have. How novel for you." Nenio: "little fox", one method shown, "My other methods are not for columns. They
  are for people."

Left alone (they work, and are the route's bar): the kill devices ("Two lies and a truth, then, one last time. You are
going to kill me..."), the coffin chain (the sexton, the clawed nails, "I am dead until I say otherwise"),
`performance` (the widow at Fye's, the deserter at the west gate, "I know which one I would do"), `returned.terms`
("The friends I kill are the only thing that quiets the flies"), `returned.test` (the bowl and the vein, the knife under
the jaw, "I have killed every friend I ever had. I haven't decided about you"), `kills_answered.oath`, all `masks.*`,
`early.blood`/`cart`, `beat.*` ("Up and in. As close as a friend"), `bond.shelf` (the list with the Commander's name
crossed out and written again), `bond.not_today`, the evenings (`the_puppy`: "I took a knife from the kitchen one
afternoon and cut his head off", native `ff99a981`), the cards, the days (`a_new_friend`: Ilse on the list), the five
locked native-adapter pages, `epilogue.commit`'s body, Last Call, the Vellexia and Galfrey scenes, the Soana pair ("That
is all I have relinquished" keeps the threat), the Soana and Nurah reactions other than S7. `evening.the_chaplains_census`
uses a form as a joke ("'Much nicer.' ... I'm nicer. You've made an honest woman of me") and ends on fear ("It's like
being loved"); it does not stand in for a kill, so it stays.

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 91 | 93 | Q3 father and Iris, the pup (`ff99a981`, `9177a18e`), the teacher (`7c640a99`), Mireya invented (FinalTruth; `returned.test/no`, `cards.the_amulet/tell`), Fye's bar and the snake-skull amulet match. Fixed: the invented cannibal appetite (S7). Authored: the sexton, the widow Mireya Voss, Ilse, Lethra/Radan, the carrier; no new lore added in this pass. |
| VOI | 84 | 93 | Hostess courtesy over the knife throughout; the fails were the report-kills, the closure pages in a clerk's register and the Kaylessa paperwork. Now: the push on the river steps with the gravel voice after (`e8969812`), the stair and the short blanket, "up and in, as close as a friend", "Paper burns so easily. So do tents", "little fox" (body/class put-downs per `b0cec021`, `b4b76d52`), the flush and parted lips after each kill (`d135c54d`, `4bcc01be`). Profanity stays at her native near-zero. |
| TRK | 93 | 93 | "Die convincingly" primed by hand, order or Q3; the spirits' price in the Commander's blood; the empty box filled with a hanged deserter or stones. Unchanged. |
| INT | 88 | 92 | Native hooks unchanged (hub, Q1 order, Q3 verdict, `CamelliaRomance`, `mireya_unmasked`, `will_given`, the kill-return flags for Nurah, Soana, Kaylessa). Promise readers added (S2), household readers (S3). -1 for S10 receipts, -1 for S9 (needs a gate change). |
| BEL | 82 | 92 | Every kill now costs a body the Commander sees or hears; the raised-then-left history no longer reads "Her death stood"; household lovers and rivals reach her pages; variant staging consistent (S5). |
| COX | 92 | 94 | Arueshalae, Vellexia, Seelah and Soana outcomes now carried into her pages without changing their agendas; the Kaylessa pair keeps Kaylessa's terms ("No spells, and nothing hidden from me") and her cover change. |
| HOW | 87 | 92 | Truth table with producers/consumers/status and before/after counts; every new reader is a flag-gated paragraph on an existing node; the layer raises on drift or a leftover placeholder; S9 proposal names the paragraph. |
| AGY | 74 | 92 | Pairs: she wants cover from Seelah and gets watched instead; she keeps her method from Nenio; she pays for Kaylessa's safety by killing her own man for a mistake, not out of kindness; she and Arueshalae want each other without either one softening; Wenduag and she still compete in the courtyard. The placeholders (S8) had left half of these pairs without her side. |

ALIGNMENT LENS (neutral evil; pleasure and impunity, `88fd2c13`, `53ad541f`): on screen she pushes a witness down the
river steps and watches, talks a chained cultist to death, knifes her own carrier in a lane, finishes a snared man with
her rapier point, cuts the Commander's wrist into a silver bowl, and keeps a list with the Commander's name on it. Her
"spirits" stay her own invented excuse (`returned.terms/flies`: "I called it the spirits' hunger because people were so
willing to excuse it"). Nothing in this pass redeems her: no cure, no remorse for a kill, no promise not to kill the
Commander (decisions `ending_rule`, "She never said she wouldn't"). Her household compromises are twisted compliance
that keeps her agency.

## 4. Shared scenes owned by higher rows (proposals only, not edited)

- `jerribeth.trickster.reaction.camellia*` (Jerribeth's row, merged, Claude-locked): in voice; no change proposed.
- `minagho_chivarro.trickster.react.camellia_bill` (Minachiv's row, merged): "Did you keep the receipt? ... Otherwise,
  how would anyone know who belongs to whom?" is her possessive register about a bought soul, not paperwork for menace;
  no change.
- Lower rows running in parallel (Horzalah, Vellexia, Herrax, Nurah, Devarra, Elyanka) do not own any scene edited
  here except by mention: `nurah.trickster.react.camellia_*` are Camellia's lines in Nurah's route (Owner Camellia;
  higher row = mine). `nurah.trickster.epilogue.unwritten` P2 and `nurah.trickster.dead.bill_of_sale` mention her
  without her acting; left to the Nurah row. `household.pair.camellia_vellexia.*` was read and left unchanged.

## 5. Explicit slots (Gemory tracker)

Re-checked against the changed text: `camellia.trickster.bond.witness.explicit.1` (host `bond.witness/hers`) updated:
the Commander now carries the lantern at the push, the witness is Lethra or Radan by variant, the scene and history
fields say so; boundaries unchanged (tracking brief, no insertion block, as on main). `evening.the_prisoner.explicit.1`
hosts `watch`, which this pass did not change. The 21 inserted Camellia slots, `household.pair.camellia_arueshalae.choice
.explicit.1` and `household.pair.camellia_vellexia.choice.explicit.1` are untouched (their host nodes did not change).
Natural explicit moment noted, not briefed: `camellia.trickster.day.the_eve(_alive,_camp)/close` (Commander + Camellia,
the night before the Threshold, knife across her knees). Not added because `tests/test_camellia_round2.py` asserts the
brief count of `explicit_slots/camellia/` and already fails on main (21 expected, 23 present); a 24th brief there
should wait for the coordinator to settle that count.

## 6. Validation

See the commit message of the branch head for the final numbers (filled from the runs below).

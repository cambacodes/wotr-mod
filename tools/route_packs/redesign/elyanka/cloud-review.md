# Elyanka Camilary: cloud design-first review (villain-route-elyanka)

Owner: cloud voice owner, 2026-10-08. Base: wotr-mod `main` 723ccae. Scope (CLOUD-QUEUE villain row 15): `elyanka.*` and
every scene where she appears. Truth pages read: writer `knowledge/characters/elyanka/` (canon, voice, relationships,
states, decisions, native-lines), `handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (binding contexts 1-6),
`plans/route-redesign-pipeline.md`; slot briefs in `tools/route_packs/explicit_slots/elyanka-camilary/`.

Presence read from the export (`development/Story.json`): 40 owned scenes (door, executor/straight supper, test of the
dead, the Way's whisper, commit and her move, hearse night, 15 optional Chapter 5 beats, Threshold collateral, 7
epilogue pages, Last Call page and call, 5 companion reactions: Daeran x2, Seelah, Regill x2) and 5 outside scenes:
Dorgelinda's ledger interrogations (`dorgelinda.ledger.other_columns` / `changed_columns`, her name only, Dorgelinda's
voice), the generic `trickster.lastcall.last_joke(.areelu)` (flag reads only, no Elyanka text), and the Last Call
collectors page `trickster.lastcall.page.collectors` (three Elyanka-gated paragraphs). No harem row, household pair,
Table scene or letter carries her: her household stance is "indifferent" in the route registry and no harem row produces
`elyanka.harem.stance.*`. Ledger book entries: `debt.whispering_way`, `guest.elyanka`, `secret.elyanka_siege_dead`,
`secret.elyanka_rites`.

Machine truth table: `truth-table.json` beside this file (every flag her scenes read or set, plus her secret, Last Call
debt and Dorgelinda ledger flags; producers incl. scene completions, Derived rules and native readers; every consumer
gate; `consumers_before` = count at base). Generator: `truth_table.py` (same as Melazmera's, Elyanka universe).
Shared-scene rule: her row is second to last in the villain table; no scene of hers is shared with another villain row
except the Last Call collectors roll-up, where only her own three paragraphs (gated on `elyanka.lastcall.called`) were
changed (text only).

`python expansion.py` was NOT run to completion: this environment has no `blueprints.zip`. See "Validation".

## 1. Structural defects (fixed first)

| # | Defect (export evidence) | Class | Fix (text/paragraphs only unless stated; ids, positions, Next, Set, gates untouched) |
|---|---|---|---|
| S1 | Off-screen menace as paperwork: `beat.master:kill2` (her order kills a master of the Way) told the murder as "The report reaches your desk as an item of no great interest, between a bill for tallow and a complaint about a sergeant". The route's one act of murder for the Commander happened in a memo. | VOI/BEL (binding context 6) | `kill2` stages it: her two grey men return with the master's small clean hands (staged in `master`: "very small, very clean hands") in his own coat; she turns them over with her knife, cackles until the candles shiver, then claims the Commander's mouth. Carriage-in-a-ditch kept, so epilogue P30 ("went into a ditch on the Ustalav road") still agrees. |
| S2 | Promises and grudges set in Chapter 5 with no reader (truth table: 0 consumers outside the scene's own anti-replay Forbids): `table.left` ("the one who leaves early is always the one we talk about"), `tyrant.told_her` ("if a single knight of Lastwall rides... I will know whose whisper sent him"), `anatomy.left` ("I will think of you the whole time, unkindly"), `ustalav.woods` ("I have never taken anyone there. The Way does not know it exists"), `ustalav.refused` ("The body always goes home with the collector"), `fitting.refused` ("Plane the shoulders"). | BEL/HOW | Six flag-gated paragraphs appended to `epilogue.claim/page` (after index 52), one per promise, each in her voice. `tyrant.told_her` is overloaded (two answers, "Then no knight will ride" / "Then you'll know", set the same flag; splitting needs a Set change): the reader is written true for both (no knight rode on the Commander's whisper). |
| S3 | Legal paperwork in place of her appetite on the bottled-death / death-notice histories: "Elyanka presented her bequest... She was refused possession... She contested it" (`elyanka.lastcall.page` P4), "kept the claim contested" (P6, P9; `epilogue.claim` P49-50; `epilogue.debt` P24-25), and on the collectors roll-up "Its collector... **He** returned to Caliphas" (wrong speaker: the Way's collector is Elyanka) and "The bequest remained **on file** in Caliphas" (contradicts her creed: the Way's teaching and her bargains "cannot be written, only told", Cue_0061 98312252; `executor.haggle:sold`). | VOI/BEL/CAN | Same gates, re-staged: she comes for the body with the hearse and her six, puts two fingers to the living throat in front of the hall and shrieks, tears an empty coffin open, names the chaplains and promises to learn "what they tasted like"; the bequest stays "unwritten, in the ears of the people who had heard it". |
| S4 | Inquiry outcomes as filing reports in every epilogue: "The count went to the chaplains; a witness stood at the dead-house door" (`epilogue.claim` P16-18, P51, P52; copies in debt/lock/left_free). | VOI/BEL | Re-staged as what each woman did: Seelah never asks the Commander's help again and posts a lamp-bearer; Elyanka whispers his name to her Lady as grace before meat, sends the feast's bones out past him on a platter, eats over Seelah's sixty-one chalk crosses; in the hanging branch she claims the hanged man's body and drives it south past the lamp. |
| S5 | Stale reveal in the Ledger: after `inquiry.misled` Seelah holds the carters' word that the carts were Elyanka's ("You dragged me off those steps to hang a man for another woman's crime", `beat.inquiry:mislead_witness`), but `secret.elyanka_siege_dead` still shows "Unknown to Seelah" (its `known.seelah` producer exists only on the told/hers branches). | INT/BEL | The Ledger display line also forbids `inquiry.misled` (book lines have no save identity; no scene Set changed). |
| S6 | Integration gap with the household: `guest.elyanka` (Ledger Guest List) requires `elyanka.harem.eligible`, but no harem row produces `elyanka.harem.stance.joined/tolerated`, so the entry reads "A chair at the Table, if she wants it. Not yet at the table." forever; she has no Table presence anywhere. | AGY/INT | Text: the entry now says she keeps her own table in the dead-house and has never sat at anyone else's (true on every eligible history: `trickster.secret.elyanka_rites` is set by both commit answers). A real harem row for her (stance producer, pair scenes) is household-owner work: recorded, not built. |
| S7 | Gameplay defect (claude-work-queue / gameplay-entry finding `elyanka-and-camilary:D08`): the hart hunt offered "be still" or "get between the stag and the trees", and both auto-killed the stag; no check, no distinct outcome. | INT/BEL (CHARACTER-TRUTH 9) | Structure (`storylines/elyanka_hearse.py`): a trailing answer on `beat.hunt:stag` (index 2), `[Athletics]` interception, SkillAthletics DC 24, Success `held` / Failure `gored` (new nodes; new flags `hunt.held` / `hunt.gored`; both continue to the existing `fire`). Answer 1 now drives the hart onto her knife (text only), so the physical interception exists only as the checked answer. Readers: `epilogue.claim` paragraphs for both outcomes; the tine scar on `ch6.collateral:inspect`. Gameplay-entry contract row set to `fixed` with `completion_action: skill_check stag/2`; queue entry removed. Residual: "be still" has its own narrative outcome (she kills alone) but no distinct flag (adding one needs a Set change on answer 0). |
| S8 | Two quotations side by side read as two speakers: `executor.haggle:sold`, `:bare_sold`, `straight.offer:sold` ("Nothing paid. Nothing due to you." "You are mine..." - also ledger phrasing), `test.the_dead:carrion`; `test.the_dead:paladin` opened a quote with a lowercase fragment ("the paladin of Iomedae, kneeling..."). | VOI/HOW | Merged into one speech each; the fragment re-cut. |
| S9 | Recorded, not fixed: `elyanka.trickster.horses_balked` is set on every path through `visit.hearse` (all exits pass `horses2`), so it discriminates nothing and epilogue P19 always shows; `cord>1`, `morning_exit>1/2/3` require it before it can be set (dead duplicates). | none | Kept for save compatibility; the prose it unlocks is true on every committed history. |
| S10 | Recorded: `epilogue.debt`, `.lock`, `.left_free` carry the committed-only beat paragraphs (all beats require `bier_seen`, i.e. commitment), and `epilogue.eaten` P2 requires `left_free`, which `present_now` excludes (`left_free_mourned` covers that history). Dead text, harmless. | none | Left (the inquiry rewrites were applied to the dead copies too, so the pages stay consistent). |
| S11 | Recorded: unproduced cross-route discovery flags `trickster.secret.elyanka_rites.known.{seelah,targona}`, `trickster.secret.elyanka_siege_dead.known.targona`. Targona is staged smelling the yard (`beat.table:targona`) but learns nothing on screen; her knowledge belongs to Targona's route. | INT (chosen loss ~-1) | Left for the Targona/Seelah owners. |

No flag overload on the device itself: `owned` / `cost.corpse_bequeathed` are set by the three bequest answers with one
meaning; `elyanka.committed` by the claim exchange and the lock (both earned, `payoff.ordinary` reads both); the
refusal flags are split per branch and each read once by `turned_away`. Earned gates are intact: the door needs the
native funeral (four SeenCues) and Iz; nothing fires off Trickster; every closure (escort, refusals, sent home) stays
closed.

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten (all in `storylines/elyanka_cloud.py`, run last in `expansion._make_expansion`):
- `beat.master:kill2` (S1).
- `beat.writ:lied2`: the embalmer lie was answered in a quiet, reasonable rebuke ("let them burn me instead"). Her native
  register when slighted is the shriek, the hiss and the ritual threat: "if you dare address me in that tone again, I
  promise you a death even more painful than the one I have already prepared for you" (`fa330470`), "shrieks with fury"
  (`f3be11dc`). Now she shrieks, cackles once, and promises a death worse than the one she has already measured the
  Commander for (the cord, `visit.hearse:cord`). Regill's reaction and P46 ("She never forgave the Commander that lie")
  still agree.
- `beat.hunt:kill_quick` and its answer text (S7); new `held` / `gored` (the thumb in the wound, "Wasteful", licked clean:
  the native appetite for the Commander's blood, `36948bd8` "Sate your eternal hunger with {mf|his|her} blood").
- The S3/S4 paragraphs, the S8 joins, the guest entry (S6).

Left alone (they work): the door and its four funeral tellings, the executor haggle (the veil, the laugh at the unveiling,
the pulse under the crepe), the straight supper ("the corpse comes to supper, sweating"), the test of the sixty-one
(carts at midnight, carrion, the guarded larder), the commit (the poisoned lamb, "dumb cattle" creed `e5ab07dc`, "I
adore a bad bargain made with open eyes", the bitten lip), the lock of hair, the hearse night and the measuring cord
("my sack of warm meat"), the anatomy lesson, the courier who speaks in her voice, her Lady's table (thirty masks,
"not all of it is venison"), the whisper lesson and her fear of never being adopted, the fitting, the six sisters
chained in their beds, the fever ward (the dying sergeant's last prayer stolen from Pharasma), the grave, the Tyrant's
seals, the night visits, the Seelah inquiry nodes, the Daeran/Seelah/Regill reactions, the Threshold collateral, the
Last Call call, and the remaining epilogue paragraphs. Their register is hers: imperious, greedy, contemptuous of warm
flesh, possessive ("Mine. Later. All of it."), told in whispers and never written.

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 90 | 91 | Native identity, creed and fears cited throughout (`6d6b742f`, `d627f0f3`, Cue_0016-0018, Cue_0055, Cue_0061, Cue_0062, Cue_0093). S3 removed the wrong-gender collector and the "on file" contradiction of her unwritten creed. No new lore: Lastwall/Gallowspire, Caliphas, the Camilary woods are already in the route; the master's hands are authored staging of an existing kill. Off-Lich, Trickster-only (binding context 4). |
| VOI | 84 | 90 | The route already had her appetite and contempt (`visit.hearse:last_night`, `test.the_dead`, `beat.wards`). The missing part was the native madness: cackling, shrieking, ritual threat (`fa330470`, `f3be11dc`, `e1efa270`) - now in `lied2`, `kill2`, the death-notice and collectors paragraphs. Paperwork phrasing ("possession was refused", "on file", "Nothing due to you") removed. |
| TRK | 92 | 92 | Device unchanged: mourner at your own wake (Bluff 26/22), the whispered bequest (Evil 1), the exchange of claims; Last Call cheats it by the letter. |
| INT | 87 | 90 | Native funeral SeenCues + Iz latch unchanged; the hunt is now a real Athletics check with distinct outcome flags and readers (D08); Ledger Seelah line follows the hanging reveal (S5). Remaining loss: S11 cross-route knowledge flags. |
| BEL | 81 | 89 | Every promise she makes in Chapter 5 now has a reader (S2); the master dies on screen (S1); consequences read as scenes, not filings (S3, S4). Reactions: Daeran, Seelah (inquiry: three branches with Seelah acting), Regill, Targona and Nidalynn at the table, the Fool King. |
| COX | 90 | 90 | No elimination; Seelah keeps her own agenda and her refusal to forgive; Daeran's loss variants unchanged. |
| HOW | 86 | 91 | Truth table + generator shipped; layer raises on any unresolved scene/node/paragraph; unit tests for both hunt histories, every new reader, the on-screen kill and the paperwork phrases; gameplay-entry contract row certified by `hub_attachment_lint` skill_check rules. |
| AGY | 85 | 87 | She acts from her own creed and politics without the Commander: the master of the Way, her adoption, the sisters, the Tyrant, the worshippers of Drezen; Seelah's inquiry is Seelah's. No household/harem row exists for her (S6): her indifference is now stated in her own terms, but there is still no Table interaction with other women. |
| ALIGNMENT LENS | 85 | 92 | On-screen evil: sixty-one dead carted south to be stood up again, a dying sergeant's last prayer stolen, sisters chained to their beds, a master's hands on the trestle, a hanged innocent's body taken past the paladin's lamp, a feast eaten over the paladin's chalk count. Unhealthy dynamics kept: the Commander is collateral, measured in sleep, owned. No redemption: she never repents, never becomes kind; "The date stays where I put it." |

## 4. Explicit slots (Gemory tracker)

- Unchanged hosts and boundaries: `elyanka.trickster.visit.hearse.explicit.1` (hearse night), 
  `elyanka.trickster.epilogue.claim.explicit.1` (epilogue coda; anchor text unchanged).
- New briefs (both Commander + Elyanka, both Commander variants, no corpse/undead/witness participation):
  `elyanka.trickster.ch6.collateral.explicit.1` (host `ch6.collateral/rift2`, the tent outside Threshold on the eve of the
  Wound) and `elyanka.trickster.beat.table.explicit.1` (host `beat.table/door2`, after her Lady's feast, "I am still
  hungry"). Both hosts are terminal nodes: each brief records the structure hook a slots/structure job must insert
  (a slot node before the terminal answer, Set unchanged) before generation. `slot_brief_lint` reports them as terminal
  warnings, not hard failures.
- `beat.night:woke2` stays unbriefed (her deliberate "Not tonight. Tonight I only want to count.").

## 5. Not done / handed on

- A harem row for Elyanka (stance producer, pair scenes with Seelah/Targona/Daeran's household) does not exist; the
  household owner decides whether her "indifferent" stance gets one (S6).
- S11 cross-route knowledge producers (Targona; rites known to Seelah) belong to those routes.
- `tyrant.told_her` overload and the flagless "be still" hunt outcome need Set changes on existing answers (save
  compatibility forbids them here).
- Lock enrollment: no Elyanka scene is Claude-locked today; proposed new locks (before/after `text_sha` for every scene
  this pass changed) are in `voice-approvals.proposed.json`.

## 6. Validation

- `python expansion.py` cannot complete here: no `blueprints.zip` (it stops in `native_facts.verify`). Instead the full
  build ran with only the zip readers stubbed (`storylines.native_facts.verify`, `tools.native_fact_inventory.verify_inventory`,
  `storylines.native_overrides.finalize`, `tools.crossroute_checks.other_woman.native_participation_contexts`), calling
  `expansion.make_expansion()`. The same stubbed build of untouched `main` 723ccae (git worktree) reproduces main's committed
  `development/Story.json` except the zip-derived `NativeOverrides` and the member order of one `RequiresAnyGroups` group in
  the unrelated `targona.lastcall.page`. The committed export on this branch is the stubbed branch build with those two
  carried from `main`, written with `authoring._serialization.serialize(payload, 'expansion', ...)`; a second branch build
  reproduces it exactly. A real build on the coordinator host should reproduce it; rebuild before merging.
- Baseline-vs-branch build diff: 13 scenes differ, all in scope (12 `elyanka.*` + her 3 paragraphs on
  `trickster.lastcall.page.collectors`), plus two Ledger entries (`guest.elyanka` text, `secret.elyanka_siege_dead` line 0
  Forbids). Scene metadata, every existing node, choice (Next/Set/gates/checks/costs) and paragraph gate are identical;
  additions are 8 paragraphs on `epilogue.claim` (53 -> 61), 1 on `ch6.collateral/inspect`, and on `beat.hunt` the trailing
  answer `stag>2` with new nodes `held`/`gored`.
- Checks (stubbed base build -> branch): `savecompat.check` 0 -> 0; `payoff_lint.check` 0 -> 0;
  `prose_pending_lint.check(integration=True)` 0 -> 0; `claude_work_queue_lint` 0 -> 0 (224 -> 223 entries);
  `voice_lock_lint.check` 233 changed -> 233 (the locks file predates main; no Elyanka scene is locked, none added);
  `edge_lint` Elyanka/trickster: business 26 -> 24, menace 94 -> 109, exit 25 -> 22, moral_authority 4 -> 3,
  business:menace 0.28 -> 0.22; `text_structure_lint` 10 hard -> 10 hard (none Elyanka); `player_text_lint` review
  5506 -> 5506 after rephrasing three pronoun false positives; `hub_attachment_lint.gameplay_entry_lint`: the D08 row
  passes as `fixed` (skill_check `stag>2`); `slot_brief_lint --strict`: 213 hard -> 213 hard (Elyanka 0), briefs 346 -> 348,
  warnings 184 -> 186 (the two new terminal-host briefs).
- Unit tests (python -m unittest with the same stubs, `RRT_TEST_STORY=development/Story.json`): `tests.test_elyanka_cloud`
  (6 new), `tests.test_elyanka_round2`, `tests.test_gameplay_entry_inventory`: 23 OK. Also run: `test_EliandraPolish`,
  `test_harem_row_j04`, `test_latest_state_inventory`: 1 error + 1 failure, both identical on main's own export
  (pre-existing: Eliandra `katair_grave` paragraph, Hepzamirah voice locks). The C# suites (`ElyankaTricksterTests.cs`)
  were not run: no dotnet in this environment. Tests that rebuild in a subprocess without `RRT_TEST_STORY` would stop on
  the missing zip.

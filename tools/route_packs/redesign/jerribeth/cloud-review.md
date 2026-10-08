# Jerribeth: cloud voice-owner review (villain-route-jerribeth, 2026-10-08)

Scope: every `jerribeth.*` scene in `development/Story.json` at base `c0f8c85` (69 scenes, 4 078-scene export),
plus her outside appearances: `household.docket.gesmerha_jerribeth.account`, the eight
`household.pair.jerribeth_vellexia.*` rows, `vellexia.unfinished_likeness`, `gesmerha.trickster.returned.bench`,
`trickster.lastcall.last_joke(.areelu)` and the `dorgelinda.ledger.*` columns (Dorgelinda-owned, read only).
Truth table derived from the export by `truth.py` (every Set producer and every Requires/Forbids/RequiresAny consumer of
every `jerribeth.*` flag; 239 flags). Native lines: `knowledge/characters/jerribeth/native-lines.json` (22 keys).

**Liveness finding that reshapes the review.** `chapter_later` is held by the runtime in every chapter from 2 on, and
Jerribeth's route starts in Chapter 3. Seven scenes that `Forbid chapter_later` are therefore retired by gating, ids
kept for saves: `small_print`, `purchaser_answer`, `counterfeit_hinge`, `counterfeit_clerk`, `counterfeit_after`,
`settlement_visit`, `ordinary`. Their stale "purchaser / Serit / inspector / construction sheet" plot never starts in
a new or existing campaign. They are not rewritten here (no player reaches them); see D2. Paragraphs that `Forbid
trickster.ever` inside `jerribeth.trickster.epilogue.commit` (which Requires `trickster.ever`) are likewise dead.

## Structural defects (fixed first)

| # | Defect | Evidence (export) | Fix in this branch |
|---|---|---|---|
| D1 | **Unearned consequence / flag overload.** The widow's supper outcome has no live consumer. `offer_performance`/`offer_design` are read only by the retired `purchaser_answer`; `offer_design` is overloaded (set by "give her her husband's face" `offered_signature:ownership.reply.1>1` *and* by both break outcomes `break_ok>0`, `break_fail>0`). `widow_pinned`, `widow_husband`, `widow_exposed`, `widow_fee_shared` have zero consumers. | truth table: `jerribeth.offer_design` (+5 producers, 3 consumers all in a retired scene); `jerribeth.widow_*` (producers only) | `unsold_evening:start` (the next live scene, `Requires counteroffer_sent`) now carries four flag-gated paragraphs reading the **semantic** flags (`widow_pinned`, `widow_husband`, `widow_exposed`, `sale_withdrawn` minus `widow_exposed`) plus `widow_fee_shared`. `offer_design`/`offer_performance` stay as legacy compatibility readers only; no new consumer reads the overloaded flag. |
| D2 | **Stale retired chain still referenced by live readers.** Live branches read flags whose only producers are retired: `counterfeit_audience:challenge>0..2` (`counter_clerk_witness/rehearsal/hidden`), `counterfeit_spoil:start>0..1` (`counter_return_agreement/hold_agreement`), `room_measure:public_result>0..2`, `private_result>0..2` (`inspection_*`, `catalogue_*`). | truth table | Verified each has a correct live fallback (Athletics check; `drawer_pinned/empty`; `shelves`). No change: the readers are harmless save-compat stubs. Recommend a structure job purge (coordinator). |
| D3 | **Choice without consequence.** `borrowed_sun` sets seven `sun_*` flags; the only reader was the retired `counterfeit_hinge`. | truth table `jerribeth.sun_exposed` etc. | `room_measure:floor` gains a paragraph gated on `sun_reworked` (the Wintersun study she altered sits on her shelf, changed back): the Commander's answer now has a visible cost in her cabinet. |
| D4 | **Prose pending in a harem docket.** `household.docket.gesmerha_jerribeth.account:j05_cache_offer` is `[PROSE PENDING]` (work-queue entry 143). | export node text | Written (her leverage kept, no remorse, the cache yielded with a sting). Queue entry 143 and the `prose-pending.json` registration removed. Entry 235 (Gesmerha's retrieval gameplay, structural owner) left open. |
| D5 | **Explicit-slot tracker out of date.** All nine Jerribeth briefs fail `slot_brief_lint --strict` (facts not text, stale `last_line`, epilogue narration not third-past); the Codex-era briefs cap the heat at a non-graphic cut, contrary to the HEAT directive. | `python tools/slot_brief_lint.py --strict` | Briefs rewritten (see Slots below); retired `counterfeit_after` slot indexed as dropped. Checked and rejected: new slots on `future:threshold/threshold_free` (the in-letter bodily arrival is itself retired, every entry answer dead-gated); the physical collection lives in `trickster.visit`, whose two slots are rewritten. |
| D6 | **Reference before staging.** `refuge:anger` and `need` rest her foot on "the kneeling man" / "the footstool" that `refuge:start` never shows. | export `refuge:start` text | `refuge:start` now stages the kneeling courtier as her furniture before any branch reads him. |

Not defects (checked): `future` cannot dead-end (scene `RequiresAny` = `settlement_kept | short_future_requested`
covers `future_entry`); Marhevok's four canon fates are mutually exclusive in every reader (`jerribeth_partner.fate_guards`);
`terms` is set by three paths that all mean "accepted her terms".

## Prose defects (rewritten only where the scene fails)

| Scene (live) | Failure | Rubric |
|---|---|---|
| `borrowed_sun` | Moralizing diorama: the Commander lectures ("Make a place that does not borrow its meaning from people you deceived"), she concedes, nothing happens on screen. Wintersun's killings (`b323e4a8`, `0134bd2e`) reduced to a model with "no villagers inside". | VOI ≤75, BEL ≤80 (binding context 6) |
| `unsold_evening` | HR/consent choreography in labels and lines ("[Keep sharing the private imaginings you both invited...]", "You are not on trial every time..."); scene title and opening still belong to the retired sale plot; no echo of the supper she just used the Commander's face for. | VOI ≤75, HEAT |
| `fate_envelope`, `fate_letter` | Bloodless paper experiment at Vellexia's manor; her design talk turns into the forbidden "visible exit / let the visitor leave" reassurance ("No prisoners. They would make the result too easy to predict", "Consider an exit the visitor can recognize"). | VOI ≤75, CHARACTER-TRUTH 4 |
| `future` | Paperwork in her mouth, explicitly banned by her voice pack: "I read contracts... a clause missing", "smaller print", "sign anything on my behalf", "I turned away two commissions", Commander labels "Write that into whatever you are drafting", "Needles, small print and all", "I do not sign contracts with debtors". | VOI ≤75 |
| `trickster.epilogue.commit` (live nodes/paragraphs), all endings' shared Marhevok/partner paragraphs | Auditor-prose standing in for the ending: "the silence did not establish his death, his agreement, or a place in anyone's bed", "remained its own account. The later parting forgave none of that earlier price", "the new contract waited beside it", "read it twice, the way she read small print", "A broken contract is a demon's favourite kind", "a clause nobody invokes goes stale". | VOI ≤75 |
| `trickster.dead.setup_greeting/setup_final/backdated` | Ledger/clerk diction over the (good) lease device: "like a page cut from a ledger" ×3, "I always read the small print", "You write contracts like a child", "the way a clerk is precise". | VOI (minor) |

Kept as is (they work and are her): `commission` (the gate-yard illusion, on-screen menace, three checks, companion
reactions), `offered_signature` (the widow pinned awake for life), `counterfeit_guest/audience/spoil` (Vardess unmasked,
Petrik's face, the cambion pinned awake or burned), `room_measure` (her cabinet in Drezen, things that still look),
`refuge` branches (footstool courtier), `farewell` (Marhevok told in detail to hurt the Commander), `price`/`collection`
(the locust on the needle, `eb28ad3b`), every `partner_*` discovery node, `trickster.visit`. Polishing them would not
move a rubric dimension.

## Rubric (before → projected after this branch)

Evidence keys: `0b920731` (planted ideas), `66d1f6a4` (broken toys), `c4630d76` (loyalty only while it profits),
`8ef95ea9` (deals with demons), `de70b6ee` (preserve him in some form), `eb28ad3b` (needle in a locust), `b003e047`
(Marhevok's blind love), `b323e4a8` (Wintersun's murdered travellers), `0134bd2e` (the truth would kill them), `31c32623`
(succubus playing at being human), `ea25d022`/`3b982e63`/`2a79237f` (her telepathic steering of Vellexia), `ecc42853`
(she chooses a side against her patron).

| Dim | Before | After | Notes |
|---|---|---|---|
| CAN | 88 | 89 | Four Marhevok fates only; Vellexia facts limited to the Third Date cues; no new Wintersun survivors. Borrowed-sun rewrite stages a memory she holds (b323e4a8), not a live Wintersun edit, so every Wintersun outcome stays true. |
| VOI | 74 | 90 | Binding-context-6 cap lifted where the route defines her: menace and appetite on screen in borrowed_sun, unsold_evening, fate_*; paperwork removed from her mouth in future and the endings. |
| TRK | 86 | 89 | Fate envelope becomes a priced Trickster trick she tries to steal for use on Vellexia; lease device kept, ledger diction removed. |
| INT | 88 | 88 | Hooks unchanged (native met/Wintersun/Xanthir/refuge cues, ContactUnit + AnswerList for fate_envelope). |
| BEL | 82 | 88 | D1/D3 give the supper and the Wintersun study visible consequences; D6 stages the footstool. Remaining loss: retired-chain readers (D2), Vellexia pair rows are letter relays (AGY). |
| COX | 90 | 90 | No other device touched. |
| HOW | 88 | 89 | Truth table and slot briefs regenerated against the export; lint receipts below. |
| AGY | 78 | 82 | Docket reply written with her own agenda (leverage over Gesmerha's people). Pair rows with Vellexia remain a relay; proposal below. |

**ALIGNMENT LENS.** Chaotic evil demon, deserter of Deskari and Baphomet (`c4630d76`), curator-sadist. On-screen evil
now in every live act: Act 1 the yard (soldiers set on their own Commander), Act 2 the widow (pinned awake for life)
and borrowed_sun (she replays a Wintersun traveller's burning and wants the Commander's face on him), Act 3 Vardess
(pinned awake or ashes she buys), the cabinet (aware specimens), fate_envelope (she tries to aim the Commander's trick at
her own patron). No redemption beat, no motive retcon; love is possession ("the best thing on her shelves").

## Explicit slots (Gemory tracker)

Commander + Jerribeth only; observers (Marhevok's plant, the cabinet's specimens) watch and never take part.
Heat register from her native lines: courtly, oblique mouth (`8ef95ea9`, "unwrap her"), cruelty as curation
(`eb28ad3b`), pleasure in the other's awareness (`de70b6ee`); the act itself may be graphic.

| Slot | Host | Status |
|---|---|---|
| `jerribeth.room_measure.explicit.1` | room_measure desire → end | brief fixed (facts/last_line) |
| `jerribeth.trickster.visit.explicit.1/.2` | trickster.visit threshold/threshold_free → morning/morning_free | rewritten explicit |
| `jerribeth.future.explicit.1/.2` | future tenant_pinned/tenant_free → tenant_morning(_free) | rewritten explicit (mental room) |
| `jerribeth.unsold_evening.explicit.1` | unsold_evening kiss → after | rewritten (remote, voice only) |
| `jerribeth.trickster.epilogue.commit.explicit.1/.2` | epilogue night/night_mind | rewritten, third-past |
| `jerribeth.counterfeit_after.explicit.1` | retired host | dropped in `plans/slot-brief-index.json` (save node kept); facts schema fixed |
| `household.pair.jerribeth_vellexia.choice.explicit.1` | harem row (no live host) | harem-row owner; not installed |

## Proposals left for other owners

- Coordinator / structure job: purge the retired counteroffer chain readers (D2) or keep as stubs; decide the dropped
  `counterfeit_after` slot.
- Harem row owner (Vellexia pair `settle`/`retry`): stage the patron's audience as an actual meeting at the Rapture of
  Rupture instead of two letters crossing; Jerribeth's lines are ready to be spoken in person (`ea25d022` register).
- Gesmerha owner (work-queue 235): retrieval/transport gameplay for the cache.

## Implementation receipts (this branch)

- Source edits (exact-string, each asserted): `storylines/jerribeth.py`, `jerribeth_trickster.py`, `jerribeth_round2.py`
  (including its text-keyed epilogue replacement, re-keyed to the new partner paragraph), `jerribeth_partner.py`
  (shared ending paragraphs; the two test-pinned phrases kept verbatim), `jerribeth_progression.py`,
  `lastcall_partners.py` (Jerribeth's page paragraph only), `harem_rows/z_j05_restitution.py` (D4 prose).
- New layer `storylines/jerribeth_cloud.py`, called from `jerribeth_round2.integrate` right after the scaffolding
  (so the scaffolding's saved-prose contract test still holds): borrowed_sun, unsold_evening, fate_envelope,
  fate_letter, refuge:start; paragraphs D1 (`unsold_evening:start`) and D3 (`room_measure:floor`).
- Export: 22 scenes changed (21 `jerribeth.*` + the Gesmerha docket); **zero structural change** (ids, node order,
  answer order, Next/Set/Requires/Forbids/checks identical); only the six new gated paragraphs added. Text in other
  women's choices was kept free of their names so the crossroute pass adds no new gates.
- `python expansion.py` needs `blueprints.zip` (absent in the cloud container). Built with the three game-file
  verifiers stubbed (`native_facts.verify`, `native_fact_inventory.verify_inventory`, `native_overrides.finalize`,
  `other_woman.native_participation_contexts`); the stubbed build of base reproduces the committed export except
  `NativeOverrides` (game-file evidence). Committed `development/Story.json` = base export with only the owned scenes
  replaced. A local run with game files will regenerate it identically except hash-seed list order.
- Tests: `test_jerribeth_scaffolding` OK, `test_jerribeth_round2` OK, `test_edge_lint` OK, `test_earned_presence` OK.
  `test_jerribeth_partner`, `test_endings_job3/4`, `test_harem_row_*`, `test_harem_engine`, `test_drezen_placement`,
  `test_stance_agency`, `test_vellexia_round2` need `blueprints.zip` (FileNotFound, same on base).
- Lints (base vs branch identical outcome): pacing 0 hard, payoff 0 hard, departure 0 hard, claude-work-queue 0 hard,
  slot briefs 0 hard (Jerribeth 0 hard in plain `--strict` too; the harem `jerribeth_vellexia` brief has no host,
  owner: harem row). voice-lock / prose-pending need the coordinator's reviewed ref; crossroute needs game files.
- Voice-locked scenes changed (coordinator approval and lock refresh required): borrowed_sun, unsold_evening,
  fate_envelope, fate_letter, future, refuge, room_measure, price, invitation, short_invitation, all six endings,
  trickster.dead.setup_greeting / setup_final / backdated, trickster.epilogue.commit, lastcall.page.

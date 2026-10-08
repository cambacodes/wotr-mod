# Vellexia: cloud design-first review (villain-route-vellexia)

Owner: cloud voice owner, 2026-10-08. Base: wotr-mod `main` 723ccae. Scope (CLOUD-QUEUE villain row
`villain-route-vellexia`): `vellexia.*` and every scene she appears in; shared scenes where this row is the higher
villain row (Arueshalae pair S24 `household.pair.arueshalae_vellexia.*`). Rows above this one own the other shared
scenes (Jerribeth J-pairs and `jerribeth.*`, Camellia S25, Wenduag S49 and `wenduag.trickster.*`, Nocticula
`nocticula.trickster.*`, Shamira S17): proposals only (section 5). Truth pages read: writer
`knowledge/characters/vellexia/` (canon, voice, relationships, states, decisions, native-lines: 0 lines, her pack is
empty, so her voice is taken from the writer handoffs' quoted enGB lines and other speakers' native keys),
`handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (VOI, AGY, binding contexts 1-6),
`plans/route-redesign-pipeline.md`. No `vellexia.*` scene is voice-locked; she has no entries in
`claude-work-queue.json` or `prose-pending.json` (nothing to resolve).

Presence read from the export (`development/Story.json`): 59 owned scenes, about 50,000 words: the Chapter 4 opening
(8 manor scenes: the portrait, the artist, the private hour, the echo shell, Ilveris's silk), the Chapter 4/5 shell
campaign (10 scenes: the second invitation x2, Tessar's account, the clerk's price, the wager, the hour, the question
after business, the voice after the Abyss, the unclaimed evening, the cover before the battle), 13 endings, the
Trickster device (mirror x4, portrait x4, never-visited invitation, provocation, unpaid bill), the in-person return
(after.visit, visit_quarters, after.voice, glass.uncovered, after.night), epilogue.commit, Last Call (page, call) and
9 reactions. Appearances (44 scenes): household pairs S17 Shamira (2), S24 Arueshalae (4), S25 Camellia (6), J-pair
Jerribeth (8), S49 Wenduag (3); `jerribeth.patron/refuge/fate_envelope`; `nocticula.trickster.court.vellexia` and the
Nocticula mirror epilogues; `wenduag.trickster.court.vellexia(.native_visit)` and the Wenduag pack epilogue;
`arueshalae.treatment.*` (8, memory only); `dorgelinda.ledger.*` (column gates only); `trickster.lastcall.last_joke*`.
Machine truth table: `truth-table.json` beside this file (every flag a Vellexia scene reads or sets plus every
`vellexia.*` derived/native flag: each producer choice/derivation/native reader and each consumer gate, with consumer
counts before and after this pass).

`python expansion.py` was NOT run to completion: this environment has no `blueprints.zip`. See section 7.

## 1. Structural defects

| # | Defect (export evidence) | Class | Fix |
|---|---|---|---|
| V1 | Promises set and never read. `the_claim_before_the_event:method>0` / `challenge>0` set `method_first` / `challenge_first` (the Commander chooses between breaking Ilveris's trade in public and challenging him): 0 readers; `the_wager_with_an_edge` played identically. `the_second_invitation(_drezen):terms_clerk/terms_copy` set `clerk_terms` / `shared_account`: 0 readers. `a_question_kept:kiss_offer` / `close` set `first_kiss` / `held_close`: 0 readers, the first kiss is never mentioned again. `unfinished_likeness:expectation` sets `noticed_expectation`: 0 readers. `mirrored.fetch:paid` / `sword.late_portrait:paid` set `trickster.cost.late` (the week in Orrel Vask's crate, paid double): 0 readers. | BEL (promise without payoff), HOW | `storylines/vellexia_cloud.py` adds read-only flag-gated paragraphs: `the_wager_with_an_edge:start` (both roads), `the_claim_before_the_event:start` (Tessar kept a person / everything heard), `the_unused_reply:start` (the collar, the held wrist), `second_painter:start` (the picture "expects me to be bored"), `after.visit` and `after.visit_quarters` `unmirrored` / `diminished` (the week in the crate). 9 flags go from 0 readers to 1-2. |
| V2 | Flag overload: `vellexia.renewed_slow` is set by the hesitant shell answer (`the_question_after_business:slow`, "You have tempted me. You have not quite won me.") and by the Trickster's declaration (`after.visit/visit_quarters/after.voice:want`, "You. Not a debt, not a trick. You."), which also sets `trickster.courting`. Downstream the two meanings diverge only at `two_unremarkable_pleasures:voice>1 -> company_end`, where the declared lover is sent down the "company" text. | INT/BEL | The old flag stays the compatibility reader; `company_end` gets a `trickster.courting` paragraph in which she remembers the declaration and decides which answer to punish. |
| V3 | The household pairs S24 (Arueshalae, 4 scenes), S25 (Camellia, 6) and S49 (Wenduag, 3) are unreachable on her main harem road. All require `vellexia.harem.eligible` + `vellexia.trickster.in_person` and forbid `vellexia.trickster.visited`. `harem.eligible` = `payoff.ordinary` or `trickster.late_committed`; `late_committed` needs `trickster.courting`, whose only producers (`after.visit/visit_quarters:want`, `after.voice:want`) come after the shell answer that sets `visited` in the same scene (or require it, for `after.voice`). `payoff.ordinary` needs the shell campaign, which forbids `dead`/`mirrored` (no `unmirrored`/`diminished`) and requires `native_finished` (no `unpaid`) and `prediction_known` before `reacquire.provocation` (which forbids it), so only a provoked-then-campaign corner case reaches `in_person` without `visited`. S17 (Shamira) does not forbid `visited` and is reachable. | INT/AGY (three rivals never meet her) | NOT fixed here: gates are frozen by the contract, and S25/S49 belong to higher rows. Proposal (coordinator/Codex): replace the `vellexia.trickster.visited` forbid on S24/S25/S49 with a Drezen-presence reader, e.g. require any of `vellexia.trickster.night_kept`, `vellexia.invited` (she has said she will come to Drezen "when it suits me"), keeping `in_person`. The S24 text (her lines re-voiced here) already fits that window. |
| V4 | The native consequence of her death was never read: `ending_dead` ignored `vellexia.slaves_freed` (VellexiasSlavesFreed, Answer_0093 / Cue_0095), the release she grants at the Commander's asking. | INT/BEL (context 1: a player kill must be written with consequence) | `ending_dead:start` gets a `slaves_freed` paragraph (her guests walked out first; none of them sit down where she fell). |
| V5 | Wrong medium / medium metadata: `the_question_after_business` is a shell call (`Remote: true`, text through the glass) but carries `Kind: visit`; every other shell scene is `Kind: sending`. | INT (letter/visit classifiers) | Recorded; one-field metadata fix proposed (`Kind: sending`). The text is correctly a shell call. |
| V6 | Paperwork in place of menace across the whole Chapter 5 campaign and parts of Chapter 4 (CHARACTER-TRUTH 2, binding context 6). Edge screen on the base export: `vellexia/base` business 140 vs menace 26 (business:menace 5.39, the worst ratio of any villain base layer). The Ilveris arc ran on sealed packets with "deposits", "columns", "a second clerk", "receipts", "the published account", "Tessar's silver"; the Chapter 4 artist's arc on "the balance", "a price reduction", "a bill", "his receipt", "an invoice describing the reduction in price". | VOI <=75, BEL <=80 | Structure kept (every choice keeps its meaning and flag), menace put on screen: the runner kept as a hat-stand in her hall, the clerk in the blue room among the chairs, the broken finger when the Commander misreads the book, forty-one purchasers collecting from Ilveris on her salon floor while she watches from the stairs, Ilveris turned into a footstool when his staked wager fails (he wrote "as my lady keeps everything"), the artist made to read his promise to the coat-stand that used to be a poet. See section 2. |
| V7 | Banned reassurance: `the_unused_reply:shell` "Before you ask: no, nobody is inside them." (voice.md `never_souls`). Banned register: `unfinished_likeness:start` "A hopeful opening." (voice.md `never_jerribeth`). | VOI | Replaced (section 2). |

No unearned outcome found: every return reads its device (`primed`), every commitment reads an answer the player
gave (`committed`, `courting`, `farewell_lovers`), the night in Drezen reads `committed` + `farewell_lovers` + an
arrival (`visited` or `invited`), and the endings forbid `kept_as_mirror`/`closed` where her presence would leak
(binding context 3). No reveal before staging: the shell is given (`seal_agreed`) before any shell scene, Ilveris's
silk is shown (`prediction_known`) before he is named in Chapter 5, the coin (`coin_given`, native) before the
Trickster encore. Bookkeeping flags with no reader and no promise in the prose (recorded, not changed): `started`,
`trickster.guests_released` (its meaning is carried by `cost.bare_walls`), `payoff.debt`,
`harem.attitude.*` (framework), the scene-seen ids.

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten (all in `storylines/vellexia_cloud.py`; whole nodes unless noted):
- Chapter 4: `unfinished_likeness:start` (the gushing mask: "A new guest who asks what interests me! How exciting...
  I keep the ones who tell me twice; you passed a few in the hall") and `:terms` (the lamp held up by a wrist; "That
  lamp was a sculptor. He promised me marble that breathed. I made certain something in the room did.");
  `second_painter` (lines: the coat-stand with a face, "I was so looking forward to deciding which ones", a provenance
  instead of a bill, "something he will miss"); `price_of_novelty:answer/keep/return` (the label painted in his own
  hand, the fee counted into the shaking palm; the kneeling reading to the coat-stand that was a poet);
  `the_price_of_tomorrow` (5 lines: no invoice, no revised bill; "Something with his hands, I think");
  `the_unused_reply:shell` (the banned reassurance replaced by "I let her keep her tongue for the boasting").
- Chapter 5 shell arc: `the_second_invitation(_drezen):evidence/clerk/copy` and their choice labels (Tessar in the
  blue room; "witness or an ottoman"; "You are going to remain a person. Do try to deserve it.");
  `the_claim_before_the_event` (all 7 nodes and 6 labels: the silk book of tomorrows under green wax, the forgery
  found by a Knowledge (World) reading of the arena page, the clerk's finger broken on the failed check, Tessar's
  confession under Vellexia's hand); `the_clerks_own_price:start/reason` + 4 lines (Tessar sold by Ilveris as a
  demonstration of how a clerk breaks; "Consciences make such poor upholstery"); `the_wager_with_an_edge:start/
  account/question/publish` + labels (Ilveris stakes himself, "as my lady keeps everything"); `an_hour_that_counts:
  published/won` + 8 lines (the purchasers collecting on the salon floor; the footstool); `the_voice_after_the_abyss:
  papers/won` + 5 lines; `the_question_after_business` (2 lines); `two_unremarkable_pleasures` (1 line).
- Endings: `ending_dead` (her furniture remembered by name), `ending_hostility` (no more "recollection ...
  exact and insufficient" report prose), `ending_coercion` (one sentence: she knows what being handled as a thing
  means), `ending_interrupted` and `ending_changed` (first sentence each).
- Pair S24 (`storylines/harem_rows/zzz_vellexia_pairs.py`, text only, Vellexia's lines only): "I taught you better
  than sticks, little bird. I taught you to finish."; "Half of them are holding up my lamps"; "You always did come
  back hungrier"; "neither will her diet". Arueshalae's lines are untouched (arue12 owns her voice).

Left alone (they work): the private hour and the question kept (`unadvertised_hour`, `a_question_kept`: "That chair
behind you used to be a visitor who insisted on finishing his sermon"; "He asked whether I treated all my guests this
badly. I told him he could stay and find out"); the shell test; the second invitation's `dismissed/spared/farewell`
openings (the native mercy line, "a promise kept is a matter of taste"); the wager's actors "who look as though they
have heard what became of the last ones in this house"; the lovers' shell evenings and the cover before the battle
("Into a crusader's bed, with the whole garrison listening at the shutters"; "You spared me nothing. I took it."); the
whole Trickster device and return (mirror, portrait, painter, "Everything that ever owned me is furniture", "I dislike
waiting to find out whether I shall be bored by your corpse"); the reacquire bill and the Last Call "billed the
Commander" lines (they are the Trickster Ledger's debt frame, taunts with a hat-stand and broken fingers beside them,
not a stand-in for menace); the endings' cost paragraphs; the reactions.

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 89 | 90 | Native keys respected: the arena date and its champion (`3dce2b36`, `eae0b475`) now drive the forgery check without naming the guest; the mercy line (Cue_0098), the farewell (Cue_0106), the mirror (Cue_0079), VellexiasSlavesFreed (`slaves_freed`) read on `ending_dead`. Authored additions labelled (Ilveris, Tessar, the blue room, Orrel Vask). Her own pack is empty, so no line of hers is checkable against a key (UNRESOLVED in canon.md, unchanged). |
| VOI | 74 | 90 | Before: dry Jerribeth-register haggling over a balance in Chapter 4 and a ledger plot in Chapter 5 (edge: business 140 / menace 26); the banned "nobody is inside them" and "A hopeful opening". After: gush first, then menace leaking through objects (voice.md `target`): the hat-stand, the lamp with a wrist, the coat-stand poet, the ottoman threat, the broken finger, the footstool. Unhealthy dynamics kept: the courtship stays possession with lethal stakes. |
| TRK | 92 | 92 | Unchanged devices: the mirror bought out from under her (Vask's inventory), the unfinished likeness and the painter's sitting, the predicted party; costs `bare_walls`, `diminished`, `sat_for_painter`, `trick_kept`, `bored_once`, `predicted` all read; `cost.late` now read too. |
| INT | 85 | 87 | Native hooks unchanged (AnswerList 7f394dd6, ContactUnit a32a0790, NativeReturnCue 34a0d078, SeenCues greeted/dismissed/spared/farewell/mirrored/coin, etudes dead/early/final/slaves_freed). `slaves_freed` read by the ending. V3 dead pairs and V5 metadata remain (proposals). |
| BEL | 78 | 87 | Seven unpaid promises now have consequences (V1, V2, V4); Ilveris's fate pays off on screen in each wager outcome; the campaign is no longer a talk-only accounting dispute. Remaining: the non-Trickster lovers never meet in person (the shell is canon to the route's premise; intimacy brief added, section 4), and the dead pairs (~-3 BEL recorded). |
| COX | 90 | 90 | No elimination; Jerribeth keeps her defection, Arueshalae her flight, Wenduag her hunt, Camellia her envy, Shamira her court, Nocticula her seat. |
| HOW | 84 | 90 | Truth table shipped; every new paragraph reads a flag with an existing producer; the layer raises on any unresolved scene, node, guard, label or hit count; gate fixes specified one per line. |
| AGY | 76 | 83 | S24: Vellexia wants her old creature back at the table and hungry, not the Commander's approval. Tessar acts from her own grudge (sold as a demonstration) and appetite (she takes his purchasers). Ilveris stakes himself out of vanity. Capped by V3 (the Camellia, Wenduag and Arueshalae pairs never play on her main road). |
| ALIGNMENT LENS | 72 | 92 | On-screen evil restored and extended: guests kept as furniture in view (hat-stand, lamp, coat-stand), the clerk's finger broken for the Commander's mistake, the purchasers turned loose on Ilveris "I said nothing whatever about fingers", Ilveris made a footstool and kept in the hall where he hears guests laugh. No redemption: love does not stop her collecting; the friendship ending keeps "She did not become a kinder patron". |

## 4. Explicit slots (Gemory tracker)

- Existing slots unchanged in host and boundary: `vellexia.trickster.after.night.explicit.1` (threshold -> slot ->
  morning; no text there changed), `vellexia.trickster.epilogue.commit.explicit.1` (paragraph host unchanged).
- New brief: `explicit_slots/vellexia/vellexia.the_question_after_business.desire.explicit.1.json`: Commander +
  Vellexia, remote through the echo shell, the ordinary lovers' road (the only intimate beat that road has; HEAT cap
  BEL <=85 without one). `desire` is terminal; a reserved slot node before the exit is needed before generation
  (recorded in the brief, tracking only).
- Opportunities reviewed and rejected (unchanged rulings in relationships.md): `a_question_kept:kiss_offer` (ends the
  hour with the house awake; precedes any first night), `after.visit_quarters:want` (she defers at the door).
- Pair slots: `household.pair.camellia_vellexia.choice.explicit.1` (Camellia row) and the Wenduag pack paragraph
  slot (Wenduag row) unchanged; both stay blocked behind V3 for the main road.

## 5. Proposals for scenes this row does not own

- Gates (coordinator/Codex): V3 (S24/S25/S49 `visited` forbid -> Drezen-presence reader) and V5
  (`the_question_after_business` `Kind: sending`).
- S25 Camellia (Camellia row, running in parallel): Vellexia's lines are close to register; suggest one menace beat
  in `settle:start`: "Come here, darling. You would improve this dreary display. I have a stand just your height; the
  last girl on it is a candelabrum now." and in `morning:start` keep the broken stand as "I ought to keep the pieces.
  I keep everything."
- S49 Wenduag (Wenduag row, merged): `notice:terms` "No delightful little diversions" undercuts her; suggest "No
  carving. I want him whole. Whole things last longer in my house."
- J-pairs (Jerribeth row, merged): letters, correct medium; Vellexia's replies work ("I should have pulled your wings
  off before you made it"). `account` narration "Neither has promised anything beyond this resumed business" is
  report prose; suggest "Jerribeth keeps her offer. Vellexia keeps the paper, and the underlined phrase."
- S17 Shamira (Shamira row, merged): Vellexia's lines work ("His Majesty's cleaner has opinions about court manners!").
- `nocticula.trickster.court.vellexia` (locked, Nocticula row): no change proposed; it already carries her absence
  well.

## 6. Not done / handed on

- V3 and V5 need the gate/metadata changes above (outside this text-only contract).
- Her native pack is empty; her own lines remain unverifiable against keys (canon.md UNRESOLVED, unchanged).
- Voice locks: no `vellexia.*` scene is locked. Proposed enrollment with before/after `voice_lock_lint.text_sha`
  for every changed scene is in `voice-approvals.proposed.json` beside this file.

## 7. Validation

- `python expansion.py` cannot complete here: no `blueprints.zip` (it stops in `native_facts.verify`). The full build was
  run instead with only the zip readers stubbed (`storylines.native_facts.verify`,
  `tools.native_fact_inventory.verify_inventory` and its `native_fact_inventory` alias, `storylines.native_overrides.finalize`,
  `tools.crossroute_checks.other_woman.native_participation_contexts`), calling `expansion.make_expansion()`.
- Baseline proof: the same stubbed build of untouched `main` 723ccae (git worktree) reproduces the committed
  `development/Story.json` except `targona.lastcall.page`, whose `RequiresAnyGroups` member order varies run to run.
- The committed export is the stubbed branch build, serialized with `authoring.compiler.serialize(payload, 'expansion',
  Path('development/Story.json'))`, `NativeOverrides` carried from `main` and `targona.lastcall.page` carried from `main`.
  Baseline-vs-branch diff: 25 scenes, all in scope (21 `vellexia.*`, 4 `household.pair.arueshalae_vellexia.*`); scene
  order unchanged; no scene field, node id, choice id/position, Next, Set, gate, check or cost changed; existing
  paragraphs unchanged (text and gates), 13 new paragraphs appended; only node Text and 28 choice labels changed (both copies of the second invitation counted).
- Checks (`check()` functions; base -> branch): `savecompat` 0 -> 0, `payoff_lint` 0 -> 0,
  `prose_pending_lint(integration=True)` 0 -> 0, `claude_work_queue_lint` 0 -> 0, `voice_lock_lint` 0 errors -> 0 (no
  `vellexia` scene is locked), `text_structure_lint` 10 hard -> 10 hard (all pre-existing, none in scope),
  `player_text_lint` 5506 review -> 5488 review, `edge_lint` findings 15394 -> 15343; `vellexia/base` business
  140 -> 78, menace 26 -> 29 (business:menace 5.39 -> 2.69; the remaining "business" hits are mostly the lexicon's
  "price/pay/fee" in the Trickster Ledger debt frame and the native "price" of a sitting); new advisory hits are lexical
  ("honest", "right", "refuse", "the door"). `vellexia/trickster` unchanged.
- `slot_brief_lint --strict`: 213 hard / 184 warnings -> 213 hard / 185 warnings (the new brief's terminal-slot
  warning; the 2 vellexia-pair hards, `camellia_vellexia.choice` and `jerribeth_vellexia.choice`, are pre-existing and
  belong to those rows).
- Unit tests (`python -m unittest` through the same stubs, `make_expansion` cached; pytest is not installed):
  `test_vellexia_round2`, `test_vellexia_round3`, `test_harem_smoothing`, `test_earned_presence`,
  `test_left_trickster_consumers`, `test_voice_lock_lint`, `test_edge_lint`, `test_slot_brief_lint`,
  `test_harem_row_registry`, `test_endings_job3`, `test_payoff_departure_contracts` (the subprocess-fixture suites fed the
  branch export through `RRT_TEST_STORY`): all pass except 3 failures that fail identically on untouched `main`
  (`round3.test_mirror_threat_is_an_earned_memory`, `registry.test_every_row_surface_is_classified_once` 's04',
  `endings_job3.test_jerribeth_selected_graph_...`). `test_harem_row_s24` could not run: its fixture needs a
  no-harem build, and the stubbed no-harem build stops on unrelated registered-scene checks (delamere D05, gesmerha D09);
  it needs the coordinator host.
- Rebuild on the coordinator host (with `blueprints.zip`) before merging.

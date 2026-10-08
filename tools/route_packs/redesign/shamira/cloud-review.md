# Shamira: cloud design-first review (villain-route-shamira)

Owner: cloud voice owner, 2026-10-08. Base: wotr-mod `main` abb97e4. Scope (CLOUD-QUEUE villain row
`villain-route-shamira`): `shamira.*` and every scene she appears in; shared scenes where this row is the higher
villain row (Vellexia pair S17, Arueshalae pair S44). Nocticula's row is higher and blocked (noct-reconcile), so
`noct.*`, `nocticula.*` and `household.pair.nocticula_shamira.*` are proposals only (section 5). Truth pages read:
writer `knowledge/characters/shamira/` (canon, voice, relationships, states, decisions, native-lines),
`handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (binding contexts 1-6), `plans/route-redesign-pipeline.md`.

Presence read from the export (`development/Story.json`): 59 owned scenes (2 Ch3 Telmer, 3 Ch4 audience/dream, 3 kill
roads, 10 reactions, 13 epilogues, 12 mind-tenancy, 14 after-body incl. the awning copies, 2 Last Call) - about 55,000
words, 28,500 of them unique node text (voice_letter, drowning, first_night, fuel, waking, the awning scenes and the
`mind.*` fallbacks are folded copies of each other). Appearances: 7 pair scenes (Vellexia S17, Arueshalae S44 good/evil,
Nocticula precedence/precedence.live), the Nocticula partner-terms pages in 40+ `noct.*`/`nocticula.*` scenes, the
`noct.acq.epilogue.correspondence` lines, Dorgelinda's ledger columns, Arsinoe's cauldron lease, the Last Call jokes.
Machine truth table: `truth-table.json` beside this file (every `shamira`-bearing flag plus `noct.acq.shamira_*`: each
producer choice/derivation/native reader and each consumer gate, with consumer counts before and after this pass).

`python expansion.py` was NOT run to completion: this environment has no `blueprints.zip`. See section 7.

## 1. Structural defects

| # | Defect (export evidence) | Class | Fix |
|---|---|---|---|
| S1 | Promises set and never read. `ch4.read:game>3` sets `manifest_shown` and Shamira says of the 41st crate under Nocticula's seal "Stolen, diverted, or *given*. I shall enjoy finding out which" - 0 readers. `killed.voice(_letter):choose>1` sets `bargain` ("Find me something worthy of me, and then we will talk about behaving") - 0 readers; the body she gets is a weed-grown unpaid order. `n_want>1/2/3` (three copies) set `want.her` / `want.nothing` ("Tell me what you kept me for, and choose your words") - 0 readers (only `want.steward` is read, by `harem:steward`). `n_l_throne>1` sets `asked_lady.enjoyed` ("I would have hated to be killed by somebody who did not enjoy it") - 0 readers. `after.visit:come>0` sets `game_accepted` - 0 readers, so the Harem plays the same whether the Commander agreed or walked off. `after.night_alone:private>1` sets `night_alone.given_back` - 0 readers (the taken branch is read by `epilogue.kept`). `spy.hanged` has no epilogue reader while `spy.turned`/`spy.fed` do. | BEL (promise without payoff), HOW | `storylines/shamira_cloud.py` adds read-only flag-gated paragraphs: `after.city(_awning):home` (the crate: she has found out, and keeps it as a knife for the day Hepzamirah needs Nocticula), `epilogue.never:page` (crate, if she never died); the three waking copies (`mind.dream:f_w_go`, `mind.fuel:w_go`, `mind.waking:go`) read `want.her`, `want.nothing` and `bargain` ("So, no. I shall not behave. Consider that the talk."); `harem(_awning):morning` reads `asked_lady.enjoyed`; `harem(_awning):start` reads not-`game_accepted`; `epilogue.kept:page` reads `night_alone.given_back` and `spy.hanged`. 7 flags go from 0 readers to 1-3. |
| S2 | Three companion reactions are unreachable. `react.woljif_voice` Requires `shamira.trickster.returned` and Forbids `shamira.trickster.heard`, but every producer of `returned` (`killed.voice/voice_letter:choose>0-2`, `drowning:choose>0`) sets `heard` in the same answer. `react.daeran_sleep` Requires `cost.never_alone` and Forbids `trickster.embodied`; both are set by the same answer (`mind.dream:f_w_go>0`, `fuel:w_go>0`, `waking:go>0`). `react.regill_barracks` Requires `cost.barracks` and Forbids `fuel_set`; `f_choose>1` / `choose>1` set both. | BEL (reactions ≤80), INT | NOT fixed here: the contract forbids gate changes. Proposal (Codex/coordinator, one gate each): Woljif forbid `shamira.trickster.first_night` instead of `heard`; Daeran require `shamira.trickster.first_night` instead of `cost.never_alone`; Regill forbid `shamira.trickster.barracks.settled` instead of `fuel_set`. All three texts already fit those windows. |
| S3 | `after.eve` is unreachable: Requires `trickster.embodied`, Forbids `cost.never_alone`, and both come from the same answer. Its "Come out of the hole, clown" speech survives only as narration in `epilogue.kept` ¶0 / `epilogue.ally` ¶0, and `lastcall.call` (which requires `never_alone`) is the live eve beat. | INT (retired, undeclared) | Recorded. If intended as retired, add it to the retired list; if not, forbid `shamira.lastcall.callable` instead. The epilogue narration does not contradict either reading. |
| S4 | Stale staging. `ch4.read:recipes` answered the choice "[Think of moonshine recipes, loudly...]" with "an imagined crystal tally ... its numbers neatly arranged" (an older decoy), then "the recipes you piled over the closed thought"; `idiot` and every later callback say barley. The first nights after the kill (`voice_letter`/`drowning`/`first_night`: start, look, without; `dream`/`fuel`/`first_company`: fc_start) were staged in "the camp table", "a tent that smells of feet", "sentries piss outside this tent", while the same scenes put her body in "the wardrobe in your quarters in Drezen" and the barracks "by the north gate". `barracks_inquiry:chaplain` gave the inquisitor's silence to the chaplain ("The chaplain wrote nothing down ... His sort always write something down") and met the Commander "outside the command tent". | CAN/BEL | Text only: the decoy is moonshine with something folded under it; the rooms are the Commander's Drezen quarters; the inquisitor keeps his own silence. |
| S5 | Flat continuity register on every ending surface. `shamira_partner.partner_paragraphs` puts 5 Nocticula-status and 9 partner-stance lines on all 13 epilogue pages, the late epilogue's end pages and the Last Call page, in report prose ("No arrangement with the Commander had been settled. Shamira's bond with her lady was no promise of a place for anyone else."; "the secret remained an unpaid risk"; "there had been no bargain to claim she accepted"). On pages where she has no body or no life (`captive`, `unhoused`, `cast_out`, `drowned`) the only line that can fire is the "no arrangement" one, which is meaningless there. | VOI (binding context 6: paperwork in place of menace), BEL | Re-voiced, same gates and paragraph indices (payoff_contracts `stance_guards` 154-163 unchanged): status lines per page condition (body / alive / mind / gone), stance lines in her register on body pages and Last Call (the informant flayed in the fountain room, the forger kept alive for a season, the creditor's coal). |
| S6 | Repetition. `late_current_paragraphs` appends the same Nocticula-status sentence to every intermediate page of `epilogue.late` (31 nodes; e.g. "Nocticula's palace had answered through a projection. Shamira's old lover had survived, without flesh to bring to her bed." up to 15 times in one playthrough). | BEL (reads as generated) | Each page keeps exactly one visible state line per Nocticula state (the shamira_partner test invariant), rotated through four short in-scene lines per state so no page repeats the last. |
| S7 | Two queue entries are in a scene this row does not own: `household.pair.nocticula_shamira.precedence.live` `queen_reply` / `shamira_reply` (claude-work-queue ruling 17, prose-pending). Nocticula's row is higher and blocked. | AGY | Proposed text in section 5; entries left in the queue for the Nocticula owner. |

No flag overload found: `committed` has 5 producers per placement, all the same meaning (a chosen partner stance after the
thrown game); `returned`/`heard`/`started` are set together on every return answer by design; `cost.read_all` has two
producers with one meaning (she went through every room). No unearned outcome: every return reads `primed`
(the open thread) or `made_room` (the late road), embodiment reads the stolen shell and the fuel choice, commitment reads
the thrown game and a stance; closure (`shamira.closed`) is produced by the kept/cast/drowned/thrown/refused answers and
forbids every later presence scene. No reveal before staging found: the boudoir kill, the Council, Shyka, Nocticula's
greeting and the crystals are all read from native evidence (`shamira.killed`, `council_donated`, `shyka_offer_seen`,
`nocticula.trickster.secret_known.shamira`, `crystals_told`, `noct.acq.shamira_permission/reported`).

Recorded, not changed: `cost.cold_night` duplicates `night_alone.taken`; `morning.held` is set by both answers of
`harem:want` (a seen-flag); `refused_barracks` is the complement of `cost.barracks` and is read through it; `dream_kept`
is read through `dream_burned`'s forbids. Bookkeeping only, no promise in the prose.

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten (all in `storylines/shamira_cloud.py` unless noted):
- `after.visit(_awning):restful` ended on "I did not think I would ever be the thing that caused it" - the exact line her
  voice.md lists under *never_wistful*. Now: "Miss it, then. Lie awake missing it. I sleep very well on the warm side of a
  draught."
- `harem(_awning):lost` - the turn of the route, where the Commander throws her game - was a shrug ("That was deliberate.
  Come here, then."). Now she names it: nobody throws a game to her; they cheat, and then they die.
- `after.night_alone(_awning):offered` was "I shall use it ... I remember it." Now the court's gossip is hers, she bruises
  the Commander down onto the step, "You offered. I never give anything back."
- `epilogue.kept` ¶6 ("under the terms the Commander had actually offered") and `epilogue.invited` (four flat clauses)
  replaced; partner and status lines (S5/S6).
- Pair rows (`storylines/harem_rows/zzz_shamira_pairs.py`, text only): S17 Vellexia - Shamira decided "which of them went
  home without a tongue", calls her "cow" when cut off, keeps the next mouth that speaks for her "in a jar"; S44 Arueshalae -
  she tests whether a body grown for a customer who never paid can break a hold before her court finds out it cannot, and
  on refusal: "I had girls flayed for less than walking out of my court, little bird. You were always lucky." Vellexia's
  and Arueshalae's own lines are untouched.

Left alone (they work, several are the route's reference standard): the Ch4 audience (`ch4.read` war/door/dreams,
"It is like visiting a man who owns one chair"), `ch4.bird` (the sower, "I could have stopped it with a word. I watched it
all the way up instead"), the kill roads (carpets, the Abyss as a mouth, "Behind the eyes of the clown who killed me"),
the war table (the captain hanged / turned / fed: "He won't dream of his girl any more. He won't dream of anything."),
the Fleshmarkets heist and Ramisa, `mind.dream` (the burning Kenabres, "You will never dream alone again", the barracks
demand), the waking, `after.city` (the glabrezu's name taken out of his head), `after.throne` (all four answers, incl.
"You lie to me the way other people bring flowers"), `harem` court roles, the barracks surgeon and chaplain, the Telmer
letters, the reactions, `lastcall.page/call`.

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 90 | 92 | Native keys respected: court of false justice (`2c48146b`, `d409d925`, `339f715c`, `8fededb1`), throne and head (`6a624195`), "flex my muscles" (`63e099a8`), mock sorrow (`4ca2466a`), fallen celestial, unnamed goddess (`6307ffb9`), Trickster kill compulsory and Nocticula's "saved me the trouble". S4 removed the crystal-tally decoy and the Ch5 field tent. The crate payoff withholds its contents (no invented lore about Hepzamirah's cargo). |
| VOI | 88 | 92 | Already sharp (edge audit "reference standard"). The banned wistful line is gone; her epilogue/partner register is now her own (flaying the informant, the forger kept a season, "writes them naked"), not report prose. Pair rows give her an insult and a threat each at native level. |
| TRK | 92 | 92 | Unchanged device: the open thread at the kill (Socothbenoth's "carpets"), the stolen grown shell, the nightly coal; costs read_all, late, shell_torn, barracks, ramisa_story all read. |
| INT | 87 | 88 | Native hooks unchanged (AnswerLists d138954f, 5266a3d8, db7f69fa; cues 64fdd0fe, 2f4be0bd, e52a1d81; council/Shyka/crystals/permission readers). S2/S3 dead scenes remain (gate fix proposed). |
| BEL | 82 | 88 | Seven unpaid promises now have consequences (S1); the S2 reactions stay lost until the gate fix (~-3 BEL recorded). Repetition removed from the late epilogue (S6). |
| COX | 90 | 90 | No elimination; Nocticula keeps her throne, lover and voice in every state; Vellexia keeps her court and last word; Arueshalae keeps her name. |
| HOW | 86 | 90 | Truth table shipped; every new paragraph reads a flag with an existing producer; layer raises on any unresolved scene/node/hit count; gate fixes specified one per line. |
| AGY | 82 | 87 | Pairs: Vellexia and Shamira fight over who decided the queen's audiences; Arueshalae fled Shamira's court and refuses to be "my queen's creature"; Shamira wants proof her stolen body can break a hold before her court learns it cannot; the crate is leverage over Hepzamirah, not about the Commander. |
| ALIGNMENT LENS | 90 | 93 | On-screen evil kept and extended: the captain's flattened dreams, two hundred soldiers fed on, the sergeant hanged in the tack room, the glabrezu's stolen name, three duelists killed over a scar, the informant flayed, the forger kept alive for a season, the girls flayed for walking out. No redemption: "I tried it for a week and it did not take" stays the ceiling; love does not make her stop wanting the chair. |

## 4. Explicit slots (Gemory tracker)

- Existing slots unchanged in host and boundary: `shamira.trickster.harem.explicit.1`, `harem_awning.explicit.1`
  (last_line is `morning`'s first beat; the new `asked_lady.enjoyed` paragraph follows the node text),
  `epilogue.late.explicit.1`, `after.night_alone.explicit.1` (host `read`, untouched).
- New brief: `explicit_slots/shamira/shamira.trickster.after.night_alone.offered.explicit.1.json` (Commander + Shamira on
  her throne steps, the night alone given back). `offered` is terminal; a reserved slot node before the exit is needed
  before generation, recorded in the brief.
- `household.pair.shamira_arueshalae.choice.explicit.1` stays reserved and blocked (S44 ceiling, `harem/`).
- `household.pair.nocticula_shamira.return.explicit.1` stays blocked (Nocticula row).

## 5. Proposals for scenes this row does not own

`household.pair.nocticula_shamira.precedence.live` (Nocticula row; ruling 17 placeholders). Proposed text, matching the
beats and the two-seal staging of `start`:
- `queen_reply` [Nocticula]: {n}The first sheet carries the Lady in Shadow's seal, pressed so deep it has cut the paper.{/n}
  "My steward wishes it known that she sits beside me. How sweet. She sits where I put her, and she will go on sitting
  there because it amuses me to watch her want the chair next to it. Read her claim aloud at your table if you like,
  Commander. I shall let it stand. I have always liked a little treason with my wine."
- `shamira_reply` [Shamira]: {n}The second sheet smells of cinnamon and is sealed with the Ardent Dream's own sign.{/n}
  "I rule her city. I hear her petitioners, I choose which of them she sees and which go home without a tongue, and I
  share her bed when she is bored of the islands. Write that I stand beside her, Commander, not behind. She lets it stand?
  Of course she does. She thinks it costs her nothing. Let her think so a little longer."

`noct.*` partner-terms pages (Nocticula owner, after noct-reconcile): Shamira's letters there are correctly letters (old
letters laid on the table), but her lines are flat ("Your bed is yours. My Harem is mine."). Suggested register: "Keep
your mortal, my lady. My Harem is mine, and so, one day, is your chair." `noct.acq.epilogue.correspondence` uses the same
report prose as S5 ("Survival had not restored her old place ... or settled her claim"); the S5 lines here can be reused.

Gate fixes for S2/S3 (Codex/coordinator): see the table above.

## 6. Not done / handed on

- S2 dead reactions and S3 dead eve need the one-line gate changes above (outside this text-only contract).
- `household.pair.nocticula_shamira.precedence.live` placeholders remain (owner row blocked); proposals above.
- Voice locks: no `shamira.*` scene is locked. Proposed enrollment with before/after `voice_lock_lint.text_sha` for
  every changed scene is in `voice-approvals.proposed.json` beside this file.
- Mixed tense in `epilogue.late` (third-person past book pages around second-person present dialogue nodes) is the
  epilogue framework's convention; left.

## 7. Validation

- `python expansion.py` cannot complete here: no `blueprints.zip` (it stops in `native_facts.verify`). The full build was
  run instead with only the four zip readers stubbed (`native_facts.verify`, `native_fact_inventory.verify_inventory`,
  `native_overrides.finalize`, `other_woman.native_participation_contexts`), calling `expansion.make_expansion()`.
- `main` (abb97e4) does not build at all, stubbed or not: the villain-knowledge brief
  `explicit_slots/camellia/camellia.trickster.bond.witness.explicit.1.json` (e26d856) has no `insertion`, and
  `camellia_round2._slots` iterates that whole directory (`KeyError: 'insertion'`). This branch adds a two-line guard
  (opportunity briefs without an insertion are tracking only); with the same guard, the stubbed build of untouched
  `main` (git worktree) reproduces the committed `development/Story.json` byte for byte.
- The committed export is the stubbed branch build, serialized with `authoring.compiler.serialize`, `NativeOverrides`
  carried from `main` and `targona.lastcall.page` carried from `main` (its `RequiresAnyGroups` member order varies run
  to run). Baseline-vs-branch diff: 36 scenes, all in scope (30 `shamira.*`, 2 `household.pair.vellexia_shamira.*`,
  4 `household.pair.shamira_arueshalae.*`); no scene field, node id, choice, Next, Set, gate, check or cost changed;
  existing paragraphs changed text only, new paragraphs are appended. The crossroute presence sweep adds
  `crossroute.hepzamirah.available` to the two crate paragraphs (Hepzamirah is named); the re-voiced Nocticula lines were
  written so they stay reference mentions and no existing paragraph gained a guard.
- Checks on the branch export (`check()` functions; base -> branch): `savecompat` 0 -> 0, `payoff_lint` 0 -> 0,
  `prose_pending_lint(integration=True)` 0 -> 0, `claude_work_queue_lint` 0 -> 0, `text_structure_lint` 0 hard -> 0 hard,
  `voice_lock_lint` 52 -> 52 (pre-existing unapproved locked deltas; no `shamira` scene is locked), `player_text_lint`
  6184 -> 6186 review (two `commander-gender` review hits on "he"/"his" referring to the inquisitor and the captain),
  `edge_lint` findings 15948 -> 16013, the delta being `menace` (flayed +13, cruelty +32, knife +8) with `business: terms`
  3 -> 2. `slot_brief_lint --strict`: 253 hard / 176 warnings -> 253 hard / 177 warnings (the new brief's terminal-slot
  warning; no hard finding is in a `shamira/` brief).
- Unit tests (`python -m unittest` through the same stubs; pytest is not installed): `test_shamira_partner_stance`,
  `test_shamira_round2`, `test_harem_row_s17/s44/w3_s44_evil/j02/j03/registry`, `test_harem_smoothing`,
  `test_stance_agency`, `test_nocticula_partners`, `test_payoff_departure_contracts`, `test_voice_lock_lint`,
  `test_edge_lint`: 87 run, 78 pass, 7 error only because their subprocess rebuild opens `blueprints.zip`, 2 fail
  identically on untouched `main` (`w3_s44_evil.test_metadata_alone_cannot_enable_an_over_budget_allocation`,
  `nocticula_partners.test_compiled_terms_never_require_shamiras_physical_availability` on `noct.second_door`).
- Rebuild on the coordinator host (with `blueprints.zip`) before merging.

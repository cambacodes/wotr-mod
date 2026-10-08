# Nurah Dendiwhar: cloud design-first review (villain-route-nurah)

Owner: cloud voice owner, 2026-10-08. Base: wotr-mod `main` 723ccae. Scope (CLOUD-QUEUE villain row 13): `nurah.*`
and every scene where Nurah appears; shared scenes where this row is the higher villain row (Devarra, Elyanka,
Delamere, Arueshalae: none share a scene with her) and shared scenes with non-villain women (Arsinoe S35, Irabeth
reactions). Truth pages read: writer `knowledge/characters/nurah/` (canon, voice, relationships, states, decisions,
native-lines.json), `handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (binding contexts 1-6),
`plans/route-redesign-pipeline.md`, `handoffs/trickster-matrix.json` (characters[12], user_decision).

Presence read from the export (`development/Story.json`, main 723ccae): 65 owned scenes (13 parent-romance
continuation visits and letters, 41 Trickster scenes incl. 9 epilogue pages, 17 reactions, 2 Chapter 2 siege beats,
the Chapter 4 Abyss packet, 2 Last Call scenes) plus 10 appearance scenes in other routes (household S35 audit/retry
with Arsinoe, `longcon.big_joke`, Camellia's `kills_answered.oath` and `oath_camp`, Dorgelinda's two ledger pages,
three Last Call creditor/joke pages). Machine truth table: `truth-table.json` beside this file (240 flags: every
`nurah.*`, `household.pair.arsinoe_nurah.*` and `longcon.big_joke*` flag, each producer choice with its text and
each consumer gate, before and after this pass; the three retired dead-branch scenes are marked).

`python expansion.py` was NOT run: this environment has no `blueprints.zip` (the build stops at
`native_facts.verify`). See "Validation" for the stubbed differential build used instead.

## 1. Structural defects (fixed first)

| # | Defect (export evidence) | Class | Fix (text and appended paragraphs only; ids, choice text and positions, Next, Set, gates untouched) |
|---|---|---|---|
| S1 | Promise with no reader. The Commander's answer to "You'd rather keep me. Why?" (`trickster.prison.night_out(_late)/start` and its six siege answers, `ran_off.terms_by_post(_late)/letter`, `letter_one`) sets `nurah.trickster.temper_good` / `temper_chaos` / `temper_evil` on 54 choices (18 each). `temper_good` and `temper_chaos` had **0 readers**; `temper_evil` was read only as the co-author gate. "Because you'd sell them all again, and I'd like to watch" promised a betrayal the route never staged. | BEL (cost without consequence), HOW | Three exclusive temper paragraphs appended to `epilogue.the_margin/start`, `epilogue.commit/read`, `/went`, `epilogue.book_only/start`. The evil answer is paid off on the page: she sells the names of the officers who hanged Deskari's cultists at Drezen to what is left of the cults, two die in ditches, and she sends the Commander the notices with "Watching?". Consumer gates (truth table): `temper_good` 0 -> 12, `temper_chaos` 0 -> 8, `temper_evil` 16 -> 20. |
| S2 | Irabeth's reaction to the night walk (`react.irabeth_night`: the "Literate rats" lie or "Let it go, Beth") sets `cost.irabeth_lied_to` / `cost.seen`, read by nothing. | BEL (reactions without consequence) | Two paragraphs on the same four epilogue nodes, gated on `irabeth.present_now` + `crossroute.irabeth.available` (the `unwritten` P3 pattern): Irabeth reads chapter nine and writes "Literate" in the margin, or finds herself letting it go and never forgives either of them. Consumer gates: `cost.irabeth_lied_to` 0 -> 8, `cost.seen` 0 -> 4. |
| S3 | Cost without consequence: `ran_off.second_draft_late/start` charges 400 crusade gold and sets `cost.second_edition` (the Tymon pirate paid to keep the line in his forme); no reader. | BEL | Tymon paragraph on the four epilogue nodes (consumer gates 0 -> 4); the pirate leaves Tymon owing money to men who break fingers. |
| S4 | Branch-false outcome + no reader: `a_margin_for_you/morning` (the shared exit of all four final-night branches) said "Vhal's book is finished, and so is Vhal" on every history, including `outcome_collection` (Vhal "keeps a public trade to rebuild"), `outcome_limited` and `outcome_distance`. The five `outcome_*` flags of `the_copies_that_survive` had **0 readers**. | BEL/HOW | Sentence made true for every outcome; five exclusive outcome paragraphs appended to `morning`. Slot briefs `a_margin_for_you.explicit.1-3` (whose `last_line` is this node) updated. |
| S5 | Wrong medium / presence not earned (claude-work-queue `nurah:D06`-`D11`, ruling r5-S1): every parent-continuation visit is delivered at `nurah.arrival` (Nurah's ContactUnit at the Commander's private door in Drezen) but the text walked the Commander to a borrowed room near the tavern, a wine merchant's back room, up Carrow's back stair to burgle his rooms, to a hired reading room and to Vhal's hired rooms. | INT/BEL/HOW | Restaged where the encounter is delivered: Sava comes up the back stair (`a_page_with_teeth/start`); the rehearsal takes over the Commander's chambers (`the_borrowed_audience/start`); Carrow is made to climb the Commander's stair (`the_editor_opens/start`); Nurah lifts the case while Carrow is at supper and the burglary checks happen at the Commander's table (`the_case_goes_missing/start, copy_plan, access, informed, unaided, marked_entry, copied, taken`); Vhal moves the reading into the Commander's receiving room because her subscribers paid to be seen with the Commander, "I said yes for you" (`the_price_of_a_warning/start`, `the_subscribers_evening/start`); the porters carry Vhal's chest up for the settlement (`the_unpurchased_sentence/settle`). The six queue entries are removed. Actor placement for Sava/Carrow/Vhal/Edran is still prose only: see 5. |
| S6 | Stale reference: `react.irabeth_manuscript` (ghost-written dedication branch) had Irabeth say "A traitor has our casualty lists". Only the pardon branch's night walk (`night_out`) takes her to the archive; the dedication branch never does. | BEL | Re-voiced: a traitor walked out of the gaol with a book about the army and the Commander's handwriting on its first page, and she pointed demons at Irabeth's soldiers from the wall at Bottleneck Gate. |
| S7 | Branch-false on parent history: `epilogue.the_margin` is reached through `nurah.payoff.ordinary`, which includes the three parent-romance endings, but its text quoted "the author's terms she had set", which only the Trickster cell stages. The Vhal affair had no line in the page. | BEL | "Her terms held to the last page"; appended paragraph on `nurah.copies_settled`: Vhal's chapter read aloud to her own subscribers in Nerosyan. |
| S8 | Flag read backwards: `nurah.lastcall.page` P4 (`cost.name_above`) said Nurah's name went on the cover *above* the Commander's. `cost.name_above` is the Commander demanding a name above hers, refused (`terms/refused`, which also closes the route, so P4 is unreachable on a shipped save). | CAN/HOW | Corrected in place (same gate and index). |
| S9 | Recorded, not fixed: the dead state is retired by gating per the matrix user_decision (PP3: no raise; `dead.rumour`, `dead.bill_of_sale`, `dead.rumour_courier` forbid `chapter_later`). Every flag only they produce (`trickster.returned`, `larva_rumour`, `cost.ramisa_audience`, `cost.ramisa_fee`, `cost.bill_in_your_name`, `cost.chaplains_writ`, `cost.larva_memory`, `pseudonym`) is dead, and so are their readers: `trickster.terms`, `terms_night`, `react.irabeth_raised`, `react.camellia_market/supper/veiled_market/veiled_supper`, `nurah.presence.raised`, `nurah.lastcall.call`, epilogue P0/P1, Ramisa's creditor line, Camellia's `kills_answered` Nurah branch. | none | Kept for save compatibility (ids, nodes, choices). No prose there was polished. |
| S10 | Recorded, needs a structure job: the Trickster-route Nurah has **no household pair**. S35 requires `nurah.meeting_arrived` (a runtime observation of the parent-romance meeting, `Main.BuildState` / `NurahMeeting`) and forbids `nurah.prison` with no override, while `nurah.harem.eligible` = `payoff.ordinary` or `late_committed` includes the pardoned prison branch and the run-off branch. A Trickster Nurah who earned her place at the Table never meets Arsinoe there. | INT/AGY (chosen loss, ~-2) | Proposal: give S35 a Trickster delivery (`nurah.trickster.released` override for `nurah.prison`, `nurah.present_now` in place of `nurah.meeting_arrived` on the Trickster branch). Gate change, out of scope for a voice pass. |
| S11 | Recorded: 36 parent-continuation bookkeeping flags still have no reader (41 before; S4 gives the five `outcome_*` theirs) (`cover_*`, `case_*`, `public_*`, `bargain_*`, `bressa_*`, `old_letter_*`, `private_night`/`private_quiet`, `friedhelm_recalled`, ...). | none | Left: each is read inside its own scene through its sibling flags, or records a choice whose prose already delivers the consequence in the next visit. No prose promises a later payoff for them. |
| S12 | Recorded: `household.pair.arsinoe_nurah.method.*` and `.unsettled` have no reader. | none | J03 pair rows carry no paragraphs; the household controller owns attitudes (`respect` Derived). |

No flag overload found: each `temper_*` has one meaning across its 18 producers; `nurah.closed` (34 producers) is set by five
distinct refusals (ownership, name above, last word, keeping the bill, leaving her in stock), and each has its own
cost flag (`cost.owned_line`, `cost.name_above`, `cost.last_word`, `cost.bill_in_your_name`, `cost.left_in_stock`)
that its epilogue reads (`owned_line`, `refused`, `last_word`), so the closed pages never contradict the refusal.
No reveal before staging: the Pulura branches read the native cues (`76f9bab0`, `e5c3183a`) and the Camellia
reactions read `nurah.camellia_disclosed` (Camelia/Cue_0056).

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten (all in `storylines/nurah_cloud.py`, called last in `expansion._make_expansion`):
- `trickster.prison.night_out(_late)/start`: her night out of the cell was a woman reading casualty lists for the
  spelling. CHARACTER-TRUTH 12 (evil acts on screen, never reduced to off-screen summary) and the writing guide's
  "Nurah (treason erased)" defect. Now she produces the Bottleneck Gate list in her own hand, the names of the men she
  pointed the demons at ("there they are, there they are!", `05bdab7a`), ticked as she remembers them going down,
  spellings corrected, put away "as pleased with herself as a cook putting away a good recipe". Revenge creed
  (`0803fd90`), "you lot" contempt (`30c3565a`, `a3972f3e`). The question that follows and all 10 answers are kept.
- `household.pair.arsinoe_nurah.audit` and `.retry` (start, missed, audit_held, word_held, refused): villainy by freight
  arithmetic (CHARACTER-TRUTH 2). The forged demand is now forty jars of poppy syrup off the east ward, where eleven
  men who spat on her at Bottleneck Gate lie wounded: "Let them find out what a night without poppy sounds like. I'll
  sell the syrup in the lower city and drink to their health." Arsinoe still catches it by Abadar's arithmetic (her
  method, `arsinoe_trickster.py:5`); a refused audit leaves the stores locked and the ward without syrup anyway, and
  Nurah laughs all the way to the door. Same nodes, flags, check (World DC 30), lien and word-made-truth branches.
- `the_editor_opens/her_question`: the pencil point between Carrow's knuckles before "I used to write appropriate
  spirits for a man who hit me when his soup cooled".
- `the_unpurchased_sentence/chaos`: "lose a post, or a marriage, or a hand, depending on the family. I find I can
  bear it." in place of "I cannot promise every beneficiary will be charming".
- `the_copies_that_survive/collection`: the former client who came up the stair to plead, read his grandmother's
  confession aloud until he cried, and paid the higher price.
- `react.irabeth_manuscript`, the S5 restaging and the epilogue paragraphs above.

Left alone (they work): the off-hand pardon and "Come to watch the traitor rot?"; "I forged my own pardon ... Out of
professional disgust"; every ownership refusal ("I am done being anyone's property", "I did not climb out from under
that name to climb under yours"); the cell terms and threshold; the larva's "A first draft" and "Then I'm stock";
`pulura.betrayal` ("Stargazers bleed like everyone else ... I want them to know who held the knife", `57b14fa6`);
the run-off letters ("I am funny. I am extremely funny."); the Abyss packet; `early.hands` / `early.hanging` (her
treason in her own mouth: "Your soldiers saw which side I was standing on"); `unwritten` ("She called them all scum to
the last"); the Last Call obituary ("vicious, accurate and extremely popular"); the parent continuation's good/chaos
/evil personality branches (`nurah.parent_good/_chaos/_evil` are the parent romance's own states) except the two lines
above.

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 90 | 91 | Native keys per scene: Bottleneck Gate (`05bdab7a`, `a3972f3e`), creed (`0803fd90`), "from the very beginning" (`bd7cf740`), Pulura (`57b14fa6`, `7641e0bd`, `ef5c8650`), the trial verdicts (`a9ba2afd`, `4e069264`, `99fd37aa`). S8 fixes the inverted name_above reading. No new lore: the east ward, the Tymon printer, Vhal, Carrow, Sava and Edran are already authored; Deskari's cults and the Queen's court are canon. Dead branch stays closed (matrix user_decision). |
| VOI | 82 | 90 | Her unmasked register is now on screen where the route was genteel: the ticked casualty list, "drink to their health", the pencil between the knuckles, "lose a hand ... I find I can bear it", "Watching?". The two-faced historian (`5ac8f960`, `cd91a2ed`) stays in the parent visits; the refusals and the larva lines were already hers. Still short of 91: the parent continuation's middle (rehearsal, proofs) keeps an urbane, literary voice (`the_borrowed_audience`, `a_page_with_teeth`) that is the parent romance's, not her Drezen-siege mouth. |
| TRK | 92 | 92 | Device unchanged: a forged pardon dated tomorrow that she corrects herself out of professional disgust; the ghost-written dedication in her own hand; Shyka's page gates the household only. Costs: crusade gold (dedication 250, second draft 200/400), Irabeth lied to, the chaplains' writ (retired). |
| INT | 86 | 88 | Native hooks unchanged (Nurah_After_Battle lists `f392d579`, `2ce412d7`; Pulura cues; Camelia/Cue_0056; fate etudes). S5 removes narrated travel that the arrival hub never delivered. S10 (no Trickster household pair) recorded. |
| BEL | 80 | 89 | Every Trickster promise now has a payoff (S1-S3); the parent ending is true for every outcome (S4, S7); Irabeth's lie or silence comes back (S2); no stale reference (S6). Reactions: Irabeth x4, Camellia x12 (proposals below), Dorgelinda, Lann/Regill/Wenduag natively. |
| COX | 90 | 90 | No elimination; Arsinoe keeps her temple, lien and Abadar's seal in every S35 outcome; Camellia's claim on "the little traitor" stays hers. |
| HOW | 86 | 90 | Truth table shipped; every new paragraph reads a flag with a live producer; no gate/id change; the layer raises on any drifted text or missing scene/node/paragraph. |
| AGY | 72 | 84 | S35 was a freight-charge dispute about the Commander's stores. Now Nurah wants the men who caught her to scream through the night and to profit from it; Arsinoe wants the ledger true and the ward supplied; neither motive needs the Commander in the room. Capped by S10 (the Trickster Nurah never reaches the Table). |
| ALIGNMENT LENS | 78 | 91 | On-screen evil: the Bottleneck list, the poppy diversion and the ward left without syrup on refusal, the pencil, the client made to weep, the officers sold to the cults. No redemption: "Good answer. Wrong, but good"; "I haven't forgiven a single thing"; the evil-temper page is a betrayal, not a lesson. Unhealthy dynamics kept: she keeps the Commander's insult in her book, sells what he gave her, and makes Irabeth's loyalty a chapter. |

## 4. Explicit slots (Gemory tracker)

- Existing 13 briefs in `explicit_slots/nurah/`: hosts unchanged. Boundary changed by this pass and updated in the
  briefs: `nurah.a_margin_for_you.explicit.1-3` (`last_line` quotes `a_margin_for_you/morning`, whose Vhal sentence
  changed). The appended morning paragraphs follow the boundary sentence, so the brief's "return at the final hinge"
  instruction is unchanged.
- No new brief: none of the scenes changed here is a natural explicit moment (the cell at night is a gloat over the
  dead, the audit is a public Table scene, the epilogue paragraphs are ledger lines). The Commander + Nurah slots
  already cover every earned intimate beat (cell terms, terms, run-off terms, parent nights, commit, the margin).
- Pre-existing slot debt (not caused by this pass): `tests/test_nurah_round2.py` asserts 12 briefs in
  `explicit_slots/nurah/`; the villain-knowledge opportunity brief `nurah.trickster.epilogue.the_margin.explicit.1`
  (commit e26d856) makes it 13 and its slot node does not exist yet, so that test fails on `main` too. The brief needs a
  structure hook (a slot node on `the_margin/start`) or a home outside the directory the test counts.

## 5. Not done / handed on

- S10 (Trickster household pair) and the actor placement half of `nurah:D06`-`D11` (Sava, Carrow, Vhal, Edran, the
  subscribers have no presence units; the scenes now happen where Nurah is delivered, but the other people are still
  prose) need a structure job with route-local encounter staging.
- The parent continuation middle (`the_borrowed_audience`, `a_page_with_teeth`, `the_editor_opens`) is a document
  intrigue by design; its register was audited, not rewritten line by line. A later pass could cut its length and
  give her one more on-screen cruelty in the rehearsal.
- Shared scenes owned by the higher Camellia row (proposals only, not edited):
  - `nurah.trickster.react.camellia_pardon_discreet`, `camellia_draft_discreet`: "The officers will have questions"
    and "You have given her an audience. How generous" are flat beside the overt variants ("Mireya was so looking
    forward to tasting a halfling"). Proposal: keep the discreet gate (no disclosure of Camelia/Cue_0056) but give
    her appetite without the disclosure, e.g. "You gave the little traitor a pardon. How merciful of you. I do hope
    you are keeping her somewhere warm, Commander. Small things spoil so quickly."
  - `camellia.trickster.kills_answered.oath` Nurah branch: unreachable (dead branch retired, S9); no change needed.
- Knowledge pages: `decisions.md` should cite the S9 retirement as shipped; `relationships.md` slot list is correct.
- Lock enrollment and voice approvals: the coordinator applies them. No Nurah scene and no scene changed here is
  voice-locked (`voice_lock_lint` changed set identical on main and branch), so
  `voice-approvals.proposed.json` lists none; it records the before/after `text_sha` of every changed scene for
  enrollment if the coordinator locks them.

## 6. Validation

- `python expansion.py` cannot complete here: no `blueprints.zip` (stops in `native_facts.verify`). The full build was
  run instead with only the zip readers stubbed (`storylines.native_facts.verify`,
  `tools.native_fact_inventory.verify_inventory`, `storylines.native_overrides.finalize`,
  `tools.crossroute_checks.other_woman.native_participation_contexts`) and `expansion.make_expansion()` called
  directly. The same stubbed build of untouched `main` 723ccae (git worktree) reproduces the committed
  `development/Story.json`: all 4079 scenes and every top-level key equal, except `NativeOverrides` (zip-derived) and
  `targona.lastcall.page`'s `RequiresAnyGroups` member order (nondeterministic run to run). The committed export on
  this branch is `main`'s export with the 18 changed scenes taken from the branch build (so `NativeOverrides` and the
  Targona order are `main`'s), serialized with `authoring._serialization.serialize(payload, 'expansion',
  Path('development/Story.json'))`. A real build on the coordinator host should reproduce it; rebuild before merging.
- Baseline vs branch stubbed build: 18 scenes differ, all in scope (9 parent-continuation visits, `trickster.prison.night_out`
  and `_late`, `epilogue.the_margin`, `.commit`, `.book_only`, `react.irabeth_manuscript`, `nurah.lastcall.page`,
  `household.pair.arsinoe_nurah.audit` and `.retry`); node text and appended
  paragraphs only. No id, node, choice (text, Next, Set, Requires, Forbids, Check, Crusade, Mythic, Alignment),
  scene field or existing paragraph gate differs. Every new paragraph reads a flag with a live producer.
- `nurah_cloud.integrate` raises on any drifted text, missing scene/node, unmatched paragraph or `[PROSE PENDING]`;
  it skips the two S35 scenes only when the harem rows are not registered at all (`tests/story_fixture.py`
  `include_harem=False`, detected by another row's scene being absent too).
- Checks, main -> branch export (check() functions): `savecompat` 0 -> 0; `payoff_lint` 0 -> 0;
  `prose_pending_lint` (integration) 0 -> 0; `claude_work_queue_lint` 0 -> 0 (6 Nurah entries resolved and removed,
  218 left); `voice_lock_lint` changed set identical (no Nurah or S35 scene is locked), 0 errors;
  `edge_lint` locked regressions identical (303, none Nurah); `player_text_lint` new findings vs baseline identical
  (1712 both; two commander-gender hits introduced by drafts were reworded); `text_structure_lint` hard 10 -> 10
  (none Nurah); `slot_brief_lint --strict` hard 213 -> 213 (0 Nurah findings before and after).
- Edge screen, Nurah: Trickster layer menace 47 -> 49, modern-ethics 11 -> 11, business 100 -> 100; base (parent
  continuation) business 130 -> 132, menace 21 -> 22, business:menace 6.19 -> 6.0 (the parent chain is a document
  intrigue by design; see 5).
- Tests (zip readers stubbed, `python -m unittest`, pytest is not installed): `test_nurah_round2` 4/5 and
  `test_nurah_round4` 5/5; the one failure (`13 != 12` briefs) fails identically on `main` (section 4).
  `test_harem_row_j03` against the branch build (`RRT_TEST_STORY`): 16/17, the one error
  (`test_no_new_intimacy_echo...`, TypeError) is identical on `main`'s build. `test_harem_row_s35` errors in
  setUpClass on `main` and branch alike: its base fixture rebuilds in a subprocess and needs the real
  `blueprints.zip`.

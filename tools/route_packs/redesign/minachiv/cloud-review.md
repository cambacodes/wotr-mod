# Minagho and Chivarro: cloud design-first review (villain-route-minachiv)

Owner: cloud voice owner, 2026-10-08. Base: wotr-mod `main` c0f8c85. Scope (CLOUD-QUEUE row 2): `minachiv.*`,
`minagho_chivarro.*`, and every scene where Minagho or Chivarro appears; shared scenes where this row is the
higher villain row (Hepzamirah, Herrax pairs). Truth pages read: writer `knowledge/characters/minagho/` and
`knowledge/characters/chivarro/` (INDEX, voice, native-lines, canon excerpts), `handoffs/CHARACTER-TRUTH.md`,
`TRICKSTER-RUBRIC.md` (binding contexts 1-6), `plans/route-redesign-pipeline.md`.

Presence read from the export (`development/Story.json`): 134 owned scenes (23 base visits, 9 of them retired stubs,
24 base endings, 58 Trickster scenes, 1 Last Call page, 34 household pair scenes) plus 60 appearance scenes in other
routes (Herrax house and madam chain, Yaniel ch.5 and walls, Hepzamirah hounds, Dorgelinda ledger, Areelu lens,
Wenduag court, Targona, Last Call jokes). Machine truth table: `truth-table.json` beside this file
(322 `minachiv.*`, `minagho_chivarro.*` and owned pair flags: every producer choice and every consumer gate, with consumer counts
before this pass).

`python expansion.py` was NOT run to completion: this environment has no `blueprints.zip` (the build stops at
`native_facts.verify`). See "Validation" for the static checks and the stubbed differential build used instead.

## 1. Structural defects (fixed first)

| # | Defect (export evidence) | Class | Fix (text/paragraph only; ids, choice positions, Set/gates untouched) |
|---|---|---|---|
| S1 | Promised reckonings with no producer->consumer path. `what_the_offer_bought:agent_handed_over` ("I'm going to remember this ... I'll bring it out") sets `agent_handed_over`/`minagho_robbed`, read by nothing. `minaghos_unfinished_sentence:abandon` ("she is putting it somewhere she will be able to find it again") sets `street_abandoned`, read only by the next node. `the_first_small_audience:end` ("I'm going to bring it up on some night when you think you're winning") sets `nerath_arrested`, read only by `when_the_door_opens`. `the_performer_and_the_key:soldiers_barred` ("You will see this account again"), `officer_names_bought`, `house_tolerated`, `clerk_sold/clerk_bought`, `agent_killed`, `forger_hanged`, `buyer_list_kept`: no later reader. | BEL (cost without consequence), HOW | `before_the_last_road:start` now opens with "the account": 12 flag-gated paragraphs in which Minagho and Chivarro bring each grudge out at the farewell, on a night the Commander thinks is settled. The 8 living endings read `agent_killed`, `agent_handed_over`, `survivor_maimed`, `street_abandoned`, `forger_killed/maimed`, `clerk_sold`, `nerath_arrested`. `agent_handed_over`/`agent_killed` go from 0 to 10 readers. |
| S2 | Branch-consistency: `minaghos_unfinished_sentence:hand_after` said "You owe me for the street" on every history, including `street_abandoned` (the Commander let the mob beat her) and `survivor_maimed` (she maimed the witness). `roof` ignored the street entirely ("an extravagant attempt to murder her personally by gutter" after a riot). | BEL/HOW | `hand_after` text split into four exclusive flag paragraphs (protected / abandoned / maimed / fallback). `roof` re-staged on the bloody step; Chivarro reads `street_abandoned` and `survivor_maimed`. |
| S3 | Wrong medium: in `minachiv.before_the_last_road` (a face-to-face meeting in Chivarro's room) the Trickster commitment stance nodes answer by letter ("Minagho returns your demand with her refusal written across it", "The next letter comes back", "You address a second letter to Minagho alone", "Chivarro answers above Minagho's signature"). Copied from the letter variant. | BEL/HOW | All 30 commitment-stance and discovery nodes of the base scene re-spoken in the room (`stance_{0,1,2}_exclusive_minagho[_present]`, `stance_{0,2,3,7}_exclusive_chivarro[_present]`, `*_secret_*`, `stance_{0,2}_share`). |
| S4 | Wrong discoverer: on the Minagho-secret branch (`stance_{0,1,2}_night_minagho` -> `stance_discovery_N_minagho`) the discovery node had Minagho unfold "the private receipt tucked inside your belt" (Chivarro's receipt device from the Chivarro-secret branch) and expose her own affair; the next node then has Chivarro say "You piece of shit. Both of you." | BEL/HOW | `stance_discovery_N_minagho` now stages Chivarro reading the night off both of them at dawn (mind-reading, `d1bfd4e0`), which is what the following Chivarro node already answers. `stance_discovery_N_chivarro` replaces the placeholder-grade "The other woman enters ... Her lover is still beside you" with Minagho staged. |
| S5 | Reveal of unstaged content: `ending_open` cited "The brass key from the performance" and `ending_aeon(_completed)` "Chivarro did not hire the room for this performance": both belong to the retired chain (`the_key_in_your_hand`, retired by `minachiv_scaffolding.RETIRED`). The base route never stages a performance or key. | CAN/BEL | Endings rewritten to cite only staged objects (the skull note, mask stones, the plum, the house under the burned market). |
| S6 | Speaker mismatch: `the_unhired_evening:slow` (Speaker Minagho) opened with Chivarro's line ("Then lose another round, honey" - "honey" is Chivarro's word). | VOI/HOW | Re-attributed in narration. |
| S7 | Placeholders in shared scenes owned by this row: `household.pair.hepzamirah_minagho.{job,retry}` (8 nodes each) and `household.pair.herrax_chivarro.{turf.history,turf.live,retry}` (2/7/9 nodes) were `[PROSE PENDING]` (claude-work-queue rulings 18/19, 34 entries). | AGY/VOI | Voiced in `storylines/harem_rows/zzz_minachiv_pairs.py` (text only, after the contract controller; no paragraphs per J03). Queue and prose-pending entries removed. |
| S8 | Paperwork standing in for menace in `household.pair.herrax_minagho.reply:exchanged` ("the authenticated withdrawal ... revokes every kill order and paid inducement Herrax controls, including those passed through intermediaries. Herrax has signed beneath the names.") | VOI (binding context 6) | `s48.exchange_text` and the reply opener now stage the truce: Herrax cancels her hired knives by killing them (a ring, a bootlace, a tooth, the coins bent and taken back), Minagho answers with a clean knife; same flags. |
| S9 | Recorded, not fixed: `minachiv.brand_live` is Derived from `minagho.ran_complete` alone, and every base visit requires `ran_complete`, so the healed-brand paragraphs (`two_answers:native_meeting#1`, `what_the_offer_bought:bait#1`, `minaghos_unfinished_sentence:history#1`) can never show. The scaffolding records this as a conservative fallback (no Book 1-3 action edge evidence for a broken brand). | INT (chosen loss, ~-1) | Left as is; needs native evidence before any producer is invented. |
| S10 | Recorded, not fixed: dead-but-harmless saved indices (`minaghos_unfinished_sentence:morning>6` requires and forbids `outcome.eligible`; `morning>0/1`, `the_performer_and_the_key:fee>0/1`, `when_the_door_opens:first_scene>0/1` forbid `chapter_later` on chapter-5 scenes). 9 retired stubs read "This meeting has passed." and are unreachable (`Forbids chapter_later`). | none | Kept for save compatibility. |
| S11 | Recorded: 23 base flags set and never read (`terms_sent`, `venture_settled`, `rehearsal_*`, `room_*`, `gentle_evening` ...). All are bookkeeping of the retired chain or flavour receipts with no promise in the prose. | none | Left; no prose promises a consequence for them. |

No flag overload found on the base chain: `business_chosen`/`bait_chosen`/`refusal_chosen` each have one producer
meaning; `names_sold` is set on every offer branch by design (Chivarro sells the names behind the Commander's back in
all three, per voice pack "She still sells her old clients' names when the house needs it").
`future_minagho`/`future_two`/`future_chivarro` are produced by 57/32/33 choices, but every producer is a commitment
answer with the same meaning (base and Trickster stance layers), and the endings read them with
`partner_stance.cooled` as revoker.

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten (all in `storylines/minachiv_cloud.py` unless noted):
- `the_unhired_evening` start/game/minagho_close/chivarro_close/together_close/slow/company: was a parlour game with
  sugared plums and "the closeness becomes easier as the hour passes" (Chivarro pack "She never says: tea-party
  comedy"). Kept the props the endings and slot briefs use (mask stones, the plum), made the forfeit a secret Chivarro
  rips out of the loser's head and says to the table (`c151ae0f` "I'll find out for myself"), Minagho's stories are
  Drezen kills (`9fb4396d`, `537c1e5e`), Chivarro bites.
- `before_the_last_road` start/answers/minagho/together/friendship/open/service + 25 stance nodes: Minagho spoke like a
  governess ("I shall attempt consistency", "I shall try to listen without improving it"). Now foul and sugared
  (`a0f6a9d3`, "darling", knife on the table), Chivarro prices and threatens (`66f981f6`). The in-house target lines
  ("Hurt her and I will open you from throat to crotch", "I choose her. Swallow that, or ...", "You piece of shit. Both
  of you") are kept.
- `after_the_last_lamp` held/quiet/empty, `what_she_will_take` lasting_close/visits_close/visits_talk/friends: green
  stones on a coast and a plain pin became the next house's competition, a ring cut off a finger, a knife from a
  customer who did not pay.
- `her_own_arrival` account/place/company: Chivarro's first scene now reads the Commander's head on screen
  (`d1bfd4e0`) and talks like the madam of the Delights (`bb860eb1` register).
- `minaghos_unfinished_sentence` roof/hand_after (see S2).
- Endings `ending_open`, `ending_friends`, `ending_unfinished`, `ending_both_lost(+_completed)`,
  `ending_ascent(+_completed)`, `ending_sacrifice(+_completed)`, `ending_aeon(+_completed)`: abstract therapy closers
  ("Neither required the other to choose a single account of the loss", "its small, stubborn scale") replaced.
- Partner-state continuity lines (`minagho_chivarro_stance.continuity`, 19 lines on every pair epilogue and the Last
  Call page): flat register ("A separate visit from the Commander never dissolved their pair", "The contract for
  Chivarro's service remained among the Commander's papers") re-voiced; same gates and indices (payoff_contracts
  registers them by index).

Left alone (they work): `two_answers`, `the_remaining_customers` (Orven, "bite your fingers off"),
`what_the_offer_bought` (the counting room, "opens him from throat to crotch", the Inquisition branch),
`minaghos_unfinished_sentence` street (the Kenabres crowd, the maiming at the well), `the_performer_and_the_key`
(Sivane, the captain bitten to the bone), `a_room_she_likes`, `the_price_of_her_name` (the forger, the hand taken
finger by finger), `the_first_small_audience` (Tam sold into the house), `when_the_door_opens` (pay, polish or bar;
`165441c8`, `66f981f6`, `bd9912ec`), `ending_minagho_lost`, `ending_chivarro_lost`, `ending_changed` (`ffd1ba0b`), the
Trickster brand device and wake scenes (`fe0c87ea`, "You *knelt* to him"), `yaniel.trickster.ch5.minagho`.

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 89 | 91 | Native keys cited per scene; Kenabres/Drezen/Staunton/Nulkineth facts as in voice packs. S5 removed retired-chain reveals. No new lore: the only authored places are the gaming-house room, the house under the burned market, Sivane, Orven, Veyr, Nerath/Tam (all pre-existing authored). Canon reunion stays centuries later off Trickster (`056942f6`). |
| VOI | 81 | 90 | Minagho: foul, sugared, gloating, Kenabres-unrepentant (`9428f5e9`, `537c1e5e`, `a0f6a9d3`, `64bbf322`); the farewell no longer sounds like a third woman. Chivarro: prices, reads minds, threatens in her own house (`c151ae0f`, `66f981f6`, `3a0074c4`). Hepzamirah ("scrap of meat", "wench", "worm") and Herrax ("my sweet", "cheap stock", Lamashtu) at their native register in the pair scenes. |
| TRK | 92 | 92 | Trickster device unchanged: the Commander signs Minagho's Kenabres debt on Baphomet's brand ("Technically, she did it", `react.baphomet`, `minagho_dead.brand`), kneel/laugh/late-claim costs. Base chain is not a Trickster route. |
| INT | 88 | 89 | Native hooks unchanged (RanRomance `ran_*`, `book_three_finished`, AnswerLists 82a0c2ad/b00190e0, NativeReturnCue, Herrax `Cue_0045_KillChivarro` 49135105). S9 healed-brand branch remains unreachable (recorded). |
| BEL | 80 | 89 | Every promised grudge now has a payoff (S1); consequences reach the endings; branch-consistent after-street lines (S2); in-room stances (S3/S4). Reactions: Seelah/Regill/Lann/Wenduag/Greybor paragraphs unchanged; Yaniel's ch.5 confrontation. |
| COX | 89 | 90 | No elimination; Herrax keeps the Delights in every pair outcome (`herrax_chivarro` terms: "old chair remains Herrax's, no reinstatement"); Hepzamirah keeps her own glory motive (`broken_hepzamirah`). |
| HOW | 87 | 90 | Truth table shipped; every new paragraph reads an existing produced flag; no gate/ID changes; layer raises on any unresolved target. |
| AGY | 78 | 88 | The five pair scenes were placeholders. Now: Minagho wants Baphomet's collector off her trail and the credit; Hepzamirah wants her father's dog dead and her own glory; Chivarro wants her own house and Herrax to bleed for her terms; Herrax prices Chivarro's girls as "cheap stock" and breaks her word when stock walks in. None of it is about the Commander. |
| ALIGNMENT LENS | 86 | 92 | On-screen evil: the counting-room gutting, the well maiming, the forger's hand, Tam sold for 350 crowns, the captain bitten to the bone, Herrax killing her own hired knives to cancel them, Hepzamirah folding a demon over her knee. Unhealthy dynamics kept: Minagho keeps score and hates owing; Chivarro sells the officers' list twice and enjoys owning the clerk through the Commander. No redemption: "I'm sorry I lost, sweetie. That's all I'm sorry for." |

## 4. Explicit slots (Gemory tracker)

- Existing base slots unchanged in host and default text: `the_unhired_evening.explicit.1-3`,
  `a_room_she_likes.explicit.1`, `after_the_last_lamp.explicit.1`, `minaghos_unfinished_sentence.explicit.1`,
  `before_the_last_road.explicit.1-7` (briefs in `explicit_slots/minagho/`, duplicates in `chivarro/` and `minachiv/`).
- Boundaries changed by this pass and updated in the briefs: `before_the_last_road.explicit.1-7` (next beats are the
  re-staged discovery nodes), `minaghos_unfinished_sentence.explicit.1` (hand_after opener).
- New brief (in `explicit_slots/minachiv/`, since `minagho_round2` asserts the 46 briefs of `minagho/`): `minachiv.before_the_last_road.explicit.8` (Commander + Minagho + Chivarro, host `together`, after "The
  third knocks the case off the table, and nobody picks it up."). Needs a structure hook (a slot node gated on
  `minagho_chivarro.outcome.eligible`, as `the_unhired_evening:together_kiss`) before generation; recorded in the
  brief.
- Pre-existing slot debt left for a slots job (not caused by this pass): `slot_brief_lint --strict` reports divergent
  duplicate briefs between `explicit_slots/minagho/` and `explicit_slots/chivarro/` for every Trickster slot
  (different default_text/last_line/facts), list-typed `facts` in the `minagho/` Trickster copies, and missing
  `narration: third-past` on `epilogue.commit.explicit.1-5`. Reconciling them needs an editorial choice of canonical
  copy; `minachiv_voice` reads `default_text` from the `chivarro/` or `minagho/` directory named in `SLOT_TEXT`.

## 5. Not done / handed on

- Trickster branch prose was audited by sampling (react.baphomet, minagho_dead.brand/collateral, epilogue.commit,
  alone.*), not line by line. Its stance/discovery layer leans on Chivarro's receipt-in-the-belt device and
  `epilogue.commit` has the highest paperwork density in the route (bill/receipt/deed ~13 per 1000 words). It is her
  commerce motif and the discoveries are staged with a dagger, so it was not rewritten here; a later pass should thin
  it.
- `household.pair.yaniel_minagho.hearing`, `arueshalae_minagho`, `delamere_minagho` were read for contradictions only
  (none found); their prose belongs to those pair contracts.
- S9 (healed brand) needs native evidence of a broken brand before any producer exists.
- Lock enrollment and voice approvals: the coordinator applies them. Proposed before/after text hashes for every
  changed Claude-locked scene are in `voice-approvals.proposed.json` beside this file.

## 6. Validation

- `python expansion.py` cannot complete here: no `blueprints.zip` (stops in `native_facts.verify`). Instead the build
  was run in full with the four zip readers stubbed (`native_facts.verify`, `native_fact_inventory.verify_inventory`,
  `native_overrides.finalize`, `other_woman.native_participation_contexts`). The same stubbed build of untouched `main`
  reproduces the committed `development/Story.json` byte for byte once its zip-derived `NativeOverrides` evidence (and
  one scene whose `RequiresAnyGroups` member order varies run to run) are carried over, so the committed export on
  this branch is that stubbed build with `NativeOverrides` carried from `main`. A real build on the coordinator host
  should reproduce it; rebuild before merging.
- Baseline-vs-branch build diff: 46 scenes differ, all in scope; only text and added flag-gated paragraphs differ
  (no id, node, choice, Next, Set, gate, check, cost or scene-metadata change). Every new paragraph reads a flag
  with an existing producer.
- Checks on the branch export: `savecompat.check` 0, `payoff_lint.check` 0, `prose_pending_lint.check(--integration)`
  0, `claude_work_queue_lint` 0, `edge_lint` 0 hard, player-text/text-structure/memory-callback/intimacy-contract
  unchanged from `main`. `voice_lock_lint.check`: 31 Claude-locked scenes changed (expected; proposed approvals in
  `voice-approvals.proposed.json`). `slot_brief_lint --strict`: 286 -> 274 hard (12 boundaries fixed here; the new
  explicit.8 brief validates).

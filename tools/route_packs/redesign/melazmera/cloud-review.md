# Melazmera: cloud design-first review (villain-route-melazmera)

Owner: cloud voice owner, 2026-10-08. Base: wotr-mod `main` abb97e4. Scope (CLOUD-QUEUE villain row
`villain-route-melazmera`): `melazmera.*` and every scene where she appears. Shared scenes with Hepzamirah
(`household.pair.melazmera_hepzamirah.*`, `hepzamirah.lastcall.page`) belong to the higher row
(villain-route-hepzamirah, running in parallel); they are NOT edited here, proposals are in section 6.
Truth pages read: writer `knowledge/characters/melazmera/` (INDEX, canon, canon-notes, voice, relationships,
states, route, decisions, native-lines), `handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (VOI, AGY,
binding contexts 1-6), `plans/route-redesign-pipeline.md`.

**Her pack is thin.** `native-lines.json` has 0 lines: Melazmera has no native dialogue. Her register comes from
native narration and other speakers' reports, and from the Claude-locked scenes listed in
`tools/route_packs/voice_locks.json` (20 locked `melazmera.*` scenes). Native keys used throughout:
`2433842e` (the deck massacre: "tosses the bleeding and screaming chunks of meat into the air, swallowing them with a
disgusting purr of satisfaction"), `70c883b1` (the Fulsome Queen: "She bragged about eating everything, even dead
souls! She giggled"), `832dc662` (the hoard: "silly rocks that have been wrapped in illusions. And the real treasure
looks like boring rocks"), `a68b28c8` (the truce: "a dragon hunted us until Hepzamirah formed a truce with her"),
`784e7903` (the harpoon flips her in the air), `7580716e` ("The loud rattling of chains seems to attract the
attention of the umbral dragon"), `dd1d7b49` ("You helped yourself to a dragon's hoard"), `37234663` (her title).

Presence read from the export (`development/Story.json`): 44 owned scenes (Chapter 4 Colyphyr plan, salt and three
copies of the first meeting; 2 letters-in-stone, the Chapter 5 Greybor/stone message, hunger, commitment, the
declined second chance, the heap night, 17 optional Chapter 5 beats, 3 companion reactions, 6 epilogues, Last Call
page and call) plus 8 appearance scenes: the 3 S36 pair scenes with Hepzamirah, `hepzamirah.lastcall.page`, the two
`trickster.lastcall.last_joke*` gates, and Dorgelinda's ledger (`dorgelinda.ledger.*`, her name only, read-only).
Ledger book entries: `owed.melazmera`, `guest.melazmera`, `secret.melazmera_cultists`, the S36 readers.
No `claude-work-queue.json` or `prose-pending.json` entries exist for her (0 matches); no `[PROSE PENDING]` in her
scenes.

Machine truth table: `truth-table.json` beside this file (201 flags: every flag her scenes read or set and every
`melazmera*` flag, with every producer choice/EnterSet/Derived/native reader and every consumer gate, paragraph,
Derived rule and Ledger line; `consumers_before` counts at base). Regenerate with `truth_table.py` beside it.

`python expansion.py` was NOT run: this environment has no `blueprints.zip`. See section 7 for the stubbed
differential build used instead, and for a pre-existing break on `main` it exposed.

## 1. Structural defects (fixed first)

| # | Defect (export evidence) | Class | Fix (text/paragraph only; ids, choice positions, Next, Set, gates untouched) |
|---|---|---|---|
| S1 | **Flag overload, unearned reply.** `melazmera.trickster.terms.owed` is set by three semantically different answers at `ch4.hunt`/`ch4.hunt_found`/`ch5.hunt_window:name` (>0 "You ate my crew ... Now you owe me", >1 "You wear our harpoon in your side. Call that even, and this a fresh start", >2 "You chased my ship and missed. Call that my first gift"), and all three go to one `owed` node that answers only the first ("Owe. ... You have put your account the wrong way round"). A Commander who offered to call the harpoon even is told they came collecting. | BEL/HOW | `owed` text is now the shared opener; three paragraphs gated exactly like the three choices (`ate_sailors` / `harpooned & !ate_sailors` / `voyage.crevice & !ate_sailors & !harpooned`) answer each claim. The old flag stays the compatibility reader; later readers (`commit.stone:count`, S3) pair it with the same voyage flags, so no reader treats the three answers as one. |
| S2 | **Branch inconsistency (dead truce cited live).** `ch4.hunt:truce_dead` (requires `hepzamirah.dead`) says "So the truce is dead too", yet the same scene's `owed` ("The horned one pays before her diggers go out") and `rent` ("The horned one keeps a truce with me") then cite it as live; same lines in `hunt_found`/`hunt_window`, where Hepzamirah may be dead too. | BEL/CAN | Both lines no longer cite the truce. The truce itself stays where it is gated (`truce_alive`/`truce_dead`, `ch5.hunger:sister`). |
| S3 | **Promises and costs with no reader.** Set and never read (truth table `unread`): `terms.rent` and `terms.owed` ("choose well. I will remember whatever you say for a very long time"); `queen_poison_lie` (the Commander tells the Queen the gift is poison); `fed.demons` ("If it feels bad, I will come back and eat your priests' prisoners anyway"); `beat.soul_refused` ("I will be at the end of her line when you get there, thief") and `beat.soul_lied` ("I am going to keep that lie on the heap"); `beat.dinner_eaten` ("Next time I will bring you something that fights harder"); `beat.flight_let_go` ("Do not do that again ... Do it again"); `beat.greybor_claimed` ("I will borrow him to look at thieves"); `morning.stayed`. | BEL (cost without consequence), HOW | Read-only consumers added: the three first meetings' `swamp` node reads `queen_poison_lie`; `commit.stone:count` reads `terms.rent` and `terms.owed`+voyage; `epilogue.together` reads `terms.rent`, `morning.stayed`, `beat.dinner_eaten`, `beat.flight_let_go`, `beat.greybor_claimed` (forbids `greybor_gone`, `greybor_wary`), `beat.soul_lied`; all four living epilogues read `fed.demons`; `epilogue.mourned` and `melazmera.lastcall.page` (with `lastcall.dead_on_record`) read `soul_refused`/`soul_lied`. Every new paragraph reads a flag with an existing producer and is appended after existing paragraphs. |
| S4 | **Wrong medium / impossible object.** `beat.crew:paid`: the swindle is reported by "a message from the Alushinyrra quay, in a docker's cramped hand, with the Knight Commander's seal pressed into the wax", a seal that has been on her claw since Colyphyr. | BEL/CAN | Restaged in her mouth on the sill: she rains the gold on the dead men's kin, it turns to rock at the first bell in their hands, and she shouts the Commander's name at them, twice. Same choices (debt stands / pay in true gold). |
| S5 | **Wrong medium / wrong speaker.** `beat.inquisitor:inquiry_lie/admit/refuse` (Speaker `Inquisitor`) carry Melazmera's lines ("Seven cells. Such a small lie for such a large meal") under the inquisitor's portrait, and the consequence is paperwork ("has the acolyte copy your words", "the report for the next courier", "taps the sealed packet"). | VOI/BEL | The inquisitor's lines stay his; Melazmera's reaction moves into narration (as minachiv S6); copies and packets become a lamp moving through the cellars all night, a gaoler's book shut like a coffin, a lamp left burning in the empty cell that she then eats. |
| S6 | **Paperwork standing in for menace (binding context 6).** `ch5.hunger:forbid_after` (the lord "writes ... He wants to know it in writing. His letter lies beside the empty supper plate"), `herd_honest` ("The lord's answer arrives with the receipt ... You pull the receipt free"), `herd_cover` ("The quartermaster reads your reply twice"); the epilogue consequence lines "The inquisitor's report named the Commander", "sent the measurements ... A second copy stayed in the chapter room", "In the archive of the Inquisition there is a report", "Compensation kept the cattle owner's spears ... The owner's letter named Melazmera", "The demand for compensation stayed on the war council's table" (x4 epilogues); her Last Call page's S36 cost lines in the Commander's first person ("I promised to take the dangerous last wagon.", "I spent 400 Finances and hauled the replacement myself.") inside a third-person epilogue, and present-tense reactions ("Melazmera traces the ridge") on a past-tense page. | VOI/BEL | The lord walks into the war council with his howling dogs and throws a bitten-off hoof on the map; she belches from the roof; she drops a horn still warm at the root, bites his glove. Epilogue lines restaged as things that happen (the inquisitor naming the Commander to every knight while she eats a pigeon on the chapter-house roof; the lamp going out on the stairs; the hoof nobody dares move). Last Call S36 lines re-voiced in past-tense narration on her page (same `Id`s, gates and order; the cost flags all still read, test_harem_row_s36). |
| S7 | **Reveal before staging.** `commit.stone:stone` ends "You draw the sapphire clear." The Commander has only seen a grey lump; she names it a sapphire in the next node (`yes`: "That one is a sapphire"). | BEL | "You draw the stone clear." |
| S8 | Recorded, not fixed: `epilogue.*:page#2` (requires `fed.herd`, forbids `herd.incurred`) is unreachable on a new save (`forbid_after` EnterSet always sets both); kept for old saves, and `test_old_paid_herd_save_is_not_charged_again` pins its text. | none | Left verbatim. |
| S9 | Recorded, not fixed: `melazmera.harem.stance.joined/tolerated` and `melazmera.harem.joined_late` are read by the Ledger's `guest.melazmera` lines and never produced (household.py: "reserved" for the shared policy owner; the same holds for every woman). `melazmera.harem.enmity.hepzamirah` and its reconciliation are PendingHooks. | INT (shared) | Not this row's producer; left for the household policy owner. |
| S10 | Recorded: bookkeeping flags set and never read: `started`, `hunted`, `queen_truth_told` (its twin `queen_refused_crown` is read), `cost.chair_scores`, `S36 diversion.held` / `unsettled`. No prose promises a consequence for them. | none | Left. |

Checked and clean: earned presence (every visit requires `melazmera.present_now`; letters require
`reachable_by_letter`; `killed_at_colyphyr` closes the route, canon stands, binding context 1; `left_free`/`mistake`
close her and only their own epilogues read), gates (commitment needs `trickster.now`; second chance only after the
crown), no letters in face-to-face scenes outside S4/S5, no stale references to retired content, no unresolved
placeholders. Speaker attribution elsewhere is consistent (Narrator nodes quoting her are the route's convention).

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten (all in `storylines/melazmera_cloud.py`, applied from `storylines/harem_rows/zzz_melazmera_cloud.py`):
- `beat.queen` (all 12 nodes that ate candles): "eating your candles, one after another, like sticks of sugar" is
  exactly the voice pack's "She never says: cute drift: candle-crunching". Now she is gnawing a harpy on the desk;
  she ate its legs first so it could not leave, and it talked while she ate the rest (on-screen cruelty, her
  appetite, `70c883b1`); she presses the old seal into its breast like wax.
- `beat.joke:laughs` "I will eat your candles" -> "I will eat your horse".
- `ch5.hunger:ask` now hooks the native chain lure (`7580716e`): the cultists "rattle their chains all night ...
  Chains are a dinner bell". `forbid_after`, `herd_cover`, `herd_honest` (S6).
- `beat.inquisitor:do`: the inquisitor was eaten off screen. She now comes back before dawn licking her fingers and
  drops his bitten sunburst medallion in the Commander's lap: "Thin. All gristle and prayers. He said his goddess's
  name the whole way down." `inquiry_*` (S5).
- `beat.crew:paid` (S4): twisted compliance (her reparations) on screen: she pays the kin exactly as told, in gold
  that is rock by the first bell, watches them fight and bite over it, and gives them the Commander's name.
- `ch4.hunt*`: `owed` (S1), `rent` (S2; tenants who are late get eaten), `swamp` reads the poison lie.
- Epilogue consequence lines (S6) and her Last Call page (S6).

Left alone (they work, and are her register): the salt and the grey hand (`ch4.salt`, "That is how I taste
things ... You taste like a very long war"), the first meeting's arrival, crew, truce and name nodes ("Everything that
heard it was already inside me"), the cultists' night ("I am always quiet when I eat. It is the ones being eaten who
make the noise", `ch5.hunger:cultists`), "Everybody is food. You are food. The only question is who is holding the
spoon" (`forbid`), the commitment game ("Whatever you take, that is what you think I am"), the heap night and slot,
`beat.putting_down` (the beggar's copper; she means to eat her so the claim "goes inside me"), `beat.souls`,
`beat.dinner` (the demon heart, the cook's finger), `beat.seal` ("You wore a claw on your hand"), `beat.greybor`
("And I eat the thief, and I keep the coin"), `beat.drowned_king`, `beat.war`, `stone.*`, the Greybor/Nenio
reactions, `epilogue.closed/declined/left_free` bodies, `lastcall.call`.

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 90 | 92 | Every native claim keyed (`2433842e`, `70c883b1`, `832dc662`, `a68b28c8`, `784e7903`, `7580716e`, `dd1d7b49`); the truce stays a truce with unstated terms (voice pack DO NOT INVENT); "the captain's crew", never Kerz's. S2 removed a live truce cited after `hepzamirah.dead`; S4 removed a seal the Commander no longer owns. Residual: `beat.souls` ("hatched where the light goes thin") and `beat.illusion`/`drowned_king` extend her origin and the drowned king beyond the pack's guardrail; locked prose, recorded here, not rewritten. |
| VOI | 82 | 90 | Candle-crunching (pack's named "cute drift") gone; appetite on screen in every Chapter 5 beat (harpy, horn, glove, medallion, lamp, pigeon). Twisted compliance kept and sharpened: the gold-rain reparations, "Enemy action. I like my new name", "Not your prisoners ... You did not say anything about your friends' cows". Every concession keeps its price or loophole (the pack's "Very well" rule). No redemption, no softening: the epilogues still have her eating thieves and crusaders who thought she might be soft. |
| TRK | 92 | 92 | Device unchanged: the Knight Commander's seal hidden in clay among her real stones (SkillThievery 26/22), the grey hand, the sapphire bargain ("You keep it, and I keep you"); costs in game systems (seal lost, Favors, Finances, alignment). |
| INT | 88 | 90 | Native hooks unchanged (AnswerLists 5c08af90/a39dd7d4, SeenCues for hoard/voyage/queen outcomes, SelectedAnswer f35d1825 harpoon, Unlockable illusion flags, etudes `melazmera.ch5`, `melazmera_dead`); the chain lure (`7580716e`) now drives her hunger for the cells. |
| BEL | 81 | 90 | S1-S7: every answer at the fire is now answered as given and remembered at the hoard; every promise she makes has a later reader; consequences reach the epilogues, mourning page and Last Call; paperwork replaced by events. Reactions: Greybor (3), Nenio, the Fulsome Queen, the inquisitor, the gaoler, the Mendevian lord. |
| COX | 90 | 90 | No elimination; Hepzamirah's truce and the S36 ridge bargain unchanged; Greybor epilogue line forbids `greybor_gone` and `greybor_wary`. |
| HOW | 86 | 90 | Truth table and generator shipped; every new paragraph reads an existing produced flag; no gate/id/position change; the layer raises on any unresolved scene, node or paragraph. |
| AGY | 80 | 84 | Her own agenda is intact and on screen (eat, hoard, never be robbed, win every exchange; the Queen, the truce, the beggar, Greybor as a thief-sorter). The one harem unit (S36) is logistics (meat wagons, Finances) and belongs to the Hepzamirah row: proposals in section 6. |
| ALIGNMENT LENS | 83 | 92 | On-screen evil: the deck massacre retold without apology ("Sailors are salty"), seven prisoners eaten in their cells, an inquisitor eaten on the cellar stairs and his medallion dropped in the Commander's lap, a harpy eaten alive leg-first on the desk, forty head of cattle and the hoof on the map, the kin humiliated on the quay. Unhealthy dynamic kept: possession, not love ("Things in my hoard do not leave"; "Do not ever give me back anything, thief. I will not know what to do and I will eat something"). No redemption, no good-intentions retcon. |

## 4. Explicit slots (Gemory tracker)

- `melazmera.trickster.visit.heap.explicit.1` (Commander + Melazmera, existing slot node): unchanged host and
  default text; the brief's two hard lint errors fixed (`facts` joined to text; `last_line` set to the real next beat,
  `visit.heap:morning`'s first line).
- New brief `melazmera.trickster.beat.count.explicit.1` (Commander + Melazmera, Chapter 5 after the heap night, the
  Commander's quarters, host `beat.count:ate`): she counts the Commander as part of her hoard by hand, still holding
  the sapphire. Tracking only: `ate` is terminal, so it needs a slot node gated on `melazmera.committed` before
  generation (recorded in the brief; lint warns `terminal`, no hard error).
- No explicit text written.
- `slot_brief_lint --strict`: 253 -> 251 hard (both fixes are hers); 337 -> 338 briefs.

## 5. Not done / handed on

- `beat.souls`/`beat.illusion`/`beat.drowned_king` origin and drowned-king extensions (CAN residual above): locked
  prose that works as voice; a canon maintainer should rule whether umbral-dragon species lore covers them.
- S9 household stance producers belong to the household policy owner.
- Lock enrollment and voice approvals are the coordinator's: proposed before/after `text_sha` for every changed
  Claude-locked scene are in `voice-approvals.proposed.json` beside this file.

## 6. Proposals for scenes owned by the Hepzamirah row (not edited here)

- `household.pair.melazmera_hepzamirah.{open,diversion,replacement}` (S36): the unit is convoy logistics (meat
  wagons, outriders, 300/400 Finances, "two passages") and both women read as quartermasters. AGY ~70: interchangeable
  in places, and Melazmera never eats anything on screen. Proposed: keep every node, choice, flag and price, and
  restage the dispute on her canon appetite and Hepzamirah's slaves: the ridge she hunts is the path Hepzamirah's
  chained diggers are marched on, and the chains (`7580716e`) are what bring her down ("Your men walk over my supper,
  little princess" -> she hears them coming a mile off); the failed diversion shows her taking a guard off the road
  in front of Hepzamirah, not "Her nails close on empty air"; the replacement shows the Commander hauling meat while
  she sits on the cart. Hepzamirah's terms stay hers (glory, her own slaves, her door).
- `hepzamirah.lastcall.page` paragraphs 19-32 (S36 cost readers): first-person Commander ledger lines in a
  third-person epilogue ("I promised to take the dangerous last wagon.", "I spent 400 Finances and hauled the
  replacement myself.") and "Melazmera yielded her hunting approach for the two convoy passages." Proposed: the same
  past-tense narration this branch uses on `melazmera.lastcall.page` (`LAST_CALL` table in
  `storylines/melazmera_cloud.py`), re-voiced in Hepzamirah's mouth.
- `dorgelinda.ledger.*:named.melazmera` (Dorgelinda's row; not a villain row): reads correctly ("Keep her teeth away
  from my supply road"); no change proposed.

## 7. Validation

- `python expansion.py` cannot run here: no `blueprints.zip` (stops in `native_facts.verify`). The full build was
  run with only the zip readers stubbed (`storylines.native_facts.verify`,
  `tools.native_fact_inventory.verify_inventory`, `storylines.native_overrides.finalize`,
  `tools.crossroute_checks.other_woman.native_participation_contexts`) through `expansion.make_expansion()`.
- **Pre-existing break on `main` (not caused here):** `main` does not build at all, stubbed or not:
  `storylines/camellia_round2._slots` iterates `tools/route_packs/explicit_slots/camellia/` and raises
  `KeyError: 'insertion'` on the two briefs added by e26d856 (villain-knowledge explicit-slot briefs:
  `camellia.trickster.bond.witness.explicit.1.json`, `camellia.trickster.evening.the_prisoner.explicit.1.json`).
  The committed export predates that merge. The baseline and branch builds below were made with those two files
  moved aside for the duration of the build only (they are unchanged on this branch). The Camellia row (or the
  coordinator) must give them an `insertion` block or move them before `python expansion.py` can pass on `main`.
- Baseline proof: the stubbed build of untouched `main` (git worktree, same two briefs moved aside) reproduces the
  committed `development/Story.json` exactly except the zip-derived `NativeOverrides` and one scene whose
  `RequiresAnyGroups` member order varies run to run (`targona.lastcall.page`). The branch export is the stubbed
  branch build with `NativeOverrides` carried from `main` and `main`'s copy kept for every unrelated scene, written
  with `authoring._serialization.serialize(payload, "expansion", Path("development/Story.json"))`. A real build on the
  coordinator host should reproduce it; rebuild before merging.
- Baseline-vs-branch build diff: **15 scenes differ, all hers** (`ch4.hunt`, `ch4.hunt_found`, `ch5.hunt_window`,
  `ch5.hunger`, `commit.stone`, `beat.crew`, `beat.queen`, `beat.joke`, `beat.inquisitor`, `epilogue.together`,
  `epilogue.commit`, `epilogue.declined`, `epilogue.left_free`, `epilogue.mourned`, `melazmera.lastcall.page`).
  Asserted: no node, choice, Next, Set, gate, check, cost, speaker or scene-metadata change; existing paragraphs keep
  gates and order, new ones are appended. No top-level section changed.
- Two build-side auto-gates were found and avoided: naming Iomedae in a paragraph adds `crossroute.iomedae.available`
  to it, and naming her in a node adds `iomedae.closed` to the choice that leads there. The re-voiced inquisitor lines
  therefore say "his goddess"/"the Inquisition", so no existing gate moves.
- Checks on the branch export (`main` -> branch): `savecompat.check` 0 -> 0, `payoff_lint.check` 0 -> 0,
  `prose_pending_lint.check(integration=True)` 0 -> 0, `claude_work_queue_lint.check` 0 -> 0,
  `text_structure_lint.check` hard 0 / review 0 -> same, `player_text_lint.check` review 6184 -> 6183 (hers 2 -> 1; the
  remaining one is pre-existing in untouched `beat.count`), therapy 19 -> 19. `edge_lint.check` on her scenes:
  business 36 -> 26, menace 148 -> 180, modern_ethics 7 -> 9 and tenderness 12 -> 15 (lexical: "right there",
  "right up until", "for a heartbeat"), profanity 1 -> 1. `voice_lock_lint.check`: 52 -> 67 changed locked scenes;
  the 15 new ones are exactly hers (proposals in `voice-approvals.proposed.json`); the other 52 are Jerribeth/Minachiv
  deltas already on `main` awaiting the coordinator. `slot_brief_lint --strict`: 253 -> 251 hard, 338 briefs.
- Unit tests (`python -m unittest` with the same stubs; pytest is not installed): `tests.test_melazmera_round2` 9/9
  pass; `test_harem_row_s36` 7 pass, 1 error; `test_harem_row_j02`, `test_payoff_departure_contracts`,
  `test_engine_q7_l12` error in `setUpClass`. All 4 errors are the same: they rebuild the export in a subprocess,
  which needs `blueprints.zip` (FileNotFoundError on the Steam path). No failures.

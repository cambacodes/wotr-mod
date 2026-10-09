# Arueshalae: cloud design-first review (villain-route-arueshalae)

Owner: Claude voice owner, 2026-10-08, local branch `claude/cl-arueshalae` (base wotr-mod `main` 6662e2f). Scope (CLOUD-QUEUE
villain row, wave 2): every `arueshalae.*` scene except `arueshalae.trickster.evil.second_opinion` (Nocticula's), her pair
rows with non-villain women (`household.pair.seelah_arueshalae.*`, `galfrey_arueshalae.*`, `nenio_arueshalae.*`) and the
non-villain reactions that stage her (`aranka.react.arueshalae.*`, `nenio.react.fallen_arueshalae.*`). The redeemed register
landed with arue12 (wotr-mod #5) and is kept: this pass is about the corrupted/fiend branches.
Truth pages read: writer `knowledge/characters/arueshalae/` (canon, voice, states, decisions, relationships,
native-lines.json), `handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (all dims, AGY, binding contexts 1-6),
`handoffs/CLOUD-BRIEF.md`, `handoffs/CLOUD-QUEUE.md`.

Machine truth table: `truth-table.json` beside this file (400 flags; every producer and consumer, `consumers_before` =
count on main, `status`, `note` on each flag this pass touched). Regenerate with
`python tools/route_packs/redesign/arueshalae/truth_table.py development/Story.json <main export>`.

`python expansion.py` was NOT run (coordinator rule for this session: no builds). The export used for the truth table and
the shas is a simulation: main's `development/Story.json` + the two new scenes shaped like `fallen.house_call` after the
pipeline + `storylines/arueshalae_cloud.apply` (run twice: idempotent, every assertion held). See section 6.

## 0. Route shape (derived from the export)

Her two fiend roads, as a NEW save can reach them:

| Road | Gate (native) | Scenes | Status |
|---|---|---|---|
| Fallen, recruited alive at the lair | `arueshalae.evil_recruited` = EvilArushaRecruited 005c2284 (MeetEvilArusha Answer_0009 -> Cue_0011 -> Cue_0014; the Trickster's way in is `evil.home_visit`) | `evil.home_visit`, `fallen.house_call`, `fallen.lock`, `fallen.roof` (+ `.explicit.1`), `epilogue.fallen`, `react.sosiel_fallen`, `react.lann_fallen_hungry`, `react.lann_fallen_prisoner`, `lastcall.page` P1/P8, pair rows on `arueshalae.corrupted`, Aranka/Nenio/Shamira/Herrax reactions | LIVE (main: 7 own scenes, 2,617 words; branch: 9, 3,832) |
| Fallen, killed at the lair, returned by the queen | `arueshalae.evil_dead` + `arueshalae.trickster.returned` | `evil.reunion*`, `evil.terms*`, `evil.sergeant*`, `evil.daybook*`, `evil.token*`, `evil.the_boys*`, `evil.the_other_one*`, `evil.window*`, `epilogue.kept_fallen`, `lastcall.call`, `nocticula.trickster.court.arueshalae` | LEGACY ONLY: `returned` has no live producer (truth table: `retired-producer-only`); its producers `dead.starving` and `evil.second_opinion` are retired with `chapter_later` (user decision 2026-10-01: the lair kill closes the route). Pre-release state, not a defect (rubric, "Pre-release states"). |

So everything that made the fiend Arueshalae frightening on screen (the sergeant at the jeweller's arcade, Rakkoth and the
gang, the burned daybook corner, "was she happy?") sat on the road nobody can reach any more, and the live road carried the
same threat as hearsay.

## 1. Structural defects (fixed first)

S1. **The refusal's price was off screen (CHARACTER-TRUTH 2, 9, 12; BEL/VOI).** `fallen.house_call:price>2` "[Refuse her]
"Not a drop."" sets `cost.sent_away_hungry`; her answer (`refuse`) names the victim: a red-bearded sergeant at the back of
Fye's, "He'll never know what he paid for your 'no'. You will." On the live road its only consumers were
`react.lann_fallen_hungry` (Lann's hearsay) and `epilogue.fallen` P3 ("She told the Commander about it herself, at
breakfast, as if reporting the weather"): a report standing in for the act. The on-screen version
(`evil.sergeant`, locked "He was very sweet. He had a sweetheart in Nerosyan...") requires `trickster.returned` (legacy).
FIX: new hub scene `arueshalae.trickster.fallen.sergeant` (Ch5, her evil hub `7d6ad178`, Drezen, +24h after house_call,
requires `fallen.house_call` + `cost.sent_away_hungry`, optional). She walks the Commander to Fye's at noon and feeds with
the sergeant's head in her lap; three answers, each with a cost in game systems:
`[Draw on her]` (`fallen.sergeant_stopped`), `[Sit down ... "Finish."]` (`fallen.sergeant_watched`, AlignmentShift Evil 2:
complicity, watched to the end of the meal), `[Spend a Scroll of Death Ward ...]` (`fallen.sergeant_bought`, RemoveItem
89e10c3f, requires `arueshalae.ward_held`: the scroll's native 700 gold buys him back). `epilogue.fallen` P3 is re-voiced
(same gate) to the act and its end (he kept coming back to the bench "on his own feet" until he did not wake; she asks the
Commander to pass the bread with his sweetheart's name in her mouth), and three appended paragraphs read the three
answers. Lann's reaction stays true for every answer (he sleeps till supper in all three).

S2. **The one honest crack in the fiend lived on the dead road (VOI/BEL).** `evil.the_other_one` ("Was she happy? The
other one.") is the single softening beat the voice page allows the fallen her (`voice.never_fallen_regret`: one per
route); the live road had none, so the fallen Arueshalae was all teeth and no history. FIX: live twin
`arueshalae.trickster.fallen.the_other_one` (+48h after house_call, optional), re-staged on the war-room map table and
re-anchored on her native redeemed cravings (pies, street kittens: `72dcb220`); its two answers
(`fallen.other_happy` / `fallen.other_starving`) are read on `epilogue.fallen`. The legacy scene and its `_yard` copy keep
their ids for old saves; the two are mutually exclusive (`evil_dead` vs `evil_recruited`), so no player sees both.

S3. **Promise with no reader.** `evil.home_visit:start>0` sets `arueshalae.trickster.evil.home_offered` (the Trickster's
hand held out over the lair rubble, the route's own device into the native recruitment); the truth table had it
`set-never-read`. FIX: `fallen.house_call:start` appends a paragraph gated on it (she turns the hand palm up inside the
silk: "Careful, darling. One day I'll take it.").

S4. **Paperwork in place of the scene (CHARACTER-TRUTH 2; edge_lint `business`: 9 hits on settle, 9 on retry).**
`household.pair.seelah_arueshalae.fallen.settle/retry` staged her fall as a written "account" Seelah crosses out and pins
under the banner. FIX (text only; J03 row, no paragraphs, every Set/gate/position kept): the same beats played in the
stable yard to the faces of three scouts who think they ride with a servant of Desna; she tells the youngest what she is
herself and he cuts the Desnan star off his bridle (`deed.arueshalae_owned_fall`, `cost.arueshalae_desnan_cover_lost`),
Seelah refuses "sister" (`cost.seelah_sister_address_lost`); the false-cover answer leaves the star on the bridle
(`cost.commander_false_account`); refusal sends Seelah up the Wound road with them herself (`unsettled`). After: 0
business hits.

S5. **Flag overload noted, not split.** `arueshalae.committed` is set by the redeemed proposals ("Both. Always both.",
"Yes.", "All of you.") and by the fallen arrangement ("[Open the door] It's never locked."). Every live consumer pairs it
with `evil_recruited` / `arueshalae.corrupted` (epilogue.kept forbids recruited, epilogue.fallen requires it,
lastcall.page P0/P1 split, `treatment.night` forbids recruited). The only blind reader is
`nocticula.trickster.court.arueshalae:her_side` (Nocticula's, legacy-only). A split would add nothing a player can reach.

S6. **Retired producers left in live scenes (checked, no defect).** `fallen.house_call:price>0` ("Just a taste.")
requires and forbids `cost.fed_on_you` (no unwarded touch: "no scroll, no touch"), so `epilogue.fallen` P0 is legacy-only;
`fallen.roof:choose>0/1` likewise. These are the device redesign's own retirements and stay.

Earned gates kept: everything on the live road still needs the native recruitment, the Trickster path at the lair
(`EntryMythic` on house_call) and, for the roof, the open door and a ward. Nothing here makes the lair kill reversible.

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten: `epilogue.fallen` P3 (report -> act); the Seelah fallen pair (paperwork -> the scouts); new scenes S1/S2.
Voice anchors matched (explicit-speaker native lines unless marked hub): "Everyone who has tasted my sweetness said it was
worth it" (hub Cue_0027 57858226, the evil companion dialog) -> "Everyone who has tasted me said it was worth it. You're
the first who watched and said nothing."; "being a strong, healthy demon is pure bliss" (`2c206218`) -> "Being happy
sometimes, when she could have been fed always."; "Come here" / licks her lips (`9f6082a7`); the Abyss as appetite, not
swearing (`voice.profanity`: none native; the new lines have none in her mouth; Seelah keeps her own "damned").
She stays evil: she feeds on a crusader she likes, enjoys being watched, uses the Commander's mercy as a new game, and
the epilogue kills the sergeant whichever answer was chosen. No apology, no redemption, no therapy language
(edge_lint screen on the six changed scenes: 0 business / exit / therapy hits in her mouth).

Left alone because they work: `fallen.house_call` (arue12 text: "I worship one god now, and she's standing right here,
and she's starving"; the cultist meal "Leftovers are still dinner"; the terms "Don't confuse that with love"), `fallen.lock`
(the wire, "it was delicious"), `fallen.roof` (the ward, "Seven. I counted. I let go before seven." in front of the
column), `react.lann_fallen_*`, `react.sosiel_fallen`, `lastcall.page` P1/P8, Aranka's and Nenio's fallen reactions
("You would sound sweeter begging"; "My prey usually has more imagination"), the Galfrey evil pair ("I would hate to be
mistaken for your pet"). The redeemed scenes (arue12) were not touched. The legacy dead-road scenes were not polished
(no new save reaches them).

## 3. Rubric (fiend/corrupted branches, judged on the branch export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 90 | 91 | Native gates only (EvilArushaRecruited, MeetEvilArusha cues, Death Ward 0413915f / scroll 89e10c3f at 700 gold); Fye is a native Drezen anchor; the sergeant, his sweetheart, the scouts and the star are authored and claim no canon. Fallen creed per `2c206218`, `9f7a716f`. |
| VOI | 84 | 92 | Live road now shows appetite on a victim, pleasure in being watched, contempt for her redeemed self (`fallen.the_other_one`, re-anchored on `72dcb220`), Seelah taunted with "sister". Before: the cruelty was named and never seen. |
| HEAT | 88 | 89 | `fallen.roof` + `fallen.roof.explicit.1` carry the predatory ward-timed night; the sergeant scene keeps her hunger sexual and cold without a non-Commander sex act (CHARACTER-TRUTH 10). |
| TRK | 88 | 88 | The held-out hand at the lair into the native line, and wards bought and spent: unchanged, now acknowledged on her side (S3). |
| INT | 85 | 91 | `home_offered`, `sent_away_hungry` and the new answers all have readers; RemoveItem + AlignmentShift on real native mechanics; legacy road documented in the truth table. |
| BEL | 80 | 91 | Cost and consequence on screen (scroll, alignment, a soldier's life), witnesses (Lann, Sosiel, the column, the scouts); Seelah's hearing no longer reads as clerical. |
| COX | 92 | 92 | Nothing new requires another woman closed; Seelah/Galfrey/Nenio/Aranka rows unchanged in gates. |
| HOW | 86 | 91 | Every new beat is a scene id with gates, flags, readers and this table. |
| AGY | 84 | 90 | Seelah acts from her own creed and responsibility to her scouts (moves their tents, takes them up the road herself); Arueshalae acts from appetite and pride, not for the Commander. |

ALIGNMENT LENS. Fallen Arueshalae is chaotic evil in act and creed (her self-worship, hub Cue_0025 eb9b5dc9, "From now on I
worship only one deity. Myself."). The pass keeps her evil in values and methods: she feeds on the crusade's own soldier,
turns the Commander's mercy into sport ("how many scrolls one red beard is worth to you"), keeps Seelah's grief as a
delicacy, and the only crack (the other one) is closed by her own contempt ("Then she was a fool"). No good-intentions
retcon: the sergeant dies in every ending branch, the stop only delays it. Redeemed branch: unchanged (arue12), her past
kills stay first-person.

## 4. Shared scenes owned by higher rows (proposals only, not edited)

4.1 Nocticula row (higher, in progress): `household.pair.arueshalae_nocticula.{settle,retry}.corrupted` are Nocticula's
scenes; their Arueshalae nodes are the six claude-work-queue items with `woman: arueshalae` and six of her [PROSE PENDING]
markers. Not edited here (ownership). Proposed text for her nodes, ready to paste (beats from the queue entries; fallen
register; she fears the queen by instinct, `decisions.nocticula_rank`, and defies her anyway):
- `start` (settle): `{n}Arueshalae unrolls the crusade map across the Table with both hands and puts one claw through the black blot that is Alushinyrra.{/n} "Say it for her, darling, out loud, since she has a seal on your table now. 'Arueshalae. Of nobody's house.' Not hers. Not Vellexia's. Not yours, either, before you get ideas." {n}She smiles at the seal as if it could see her, and her wings are pressed flat against her back.{/n} "I bowed to her my whole life, because that is what one does. I worship one god now. She is standing here, and she is hungry, and she does not kneel."`
- `start` (retry): `"Again, darling? You are stubborn." {n}She flattens the map with the heel of her hand, over the old claw-mark.{/n} "Louder, then. 'Arueshalae. Of nobody's house.' Let the seal hear it twice."`
- `answer` (both): `"She said my name." {n}She laughs, low and delighted, and does not quite stop her hands from shaking.{/n} "Our Lady in Shadow said my name, and not 'my succubus'. Do you know how few of her creatures have heard that and lived to sulk about it?" {n}She signs under the queen's line with one claw, through the paper and into the wood of the Table.{/n} "Arueshalae. Mine. She can keep the rest of the city. I've had all of it I want."`
- `refused` (both): `"Then leave it." {n}She rolls the map up, quick and neat, before anyone can see where her claw went in.{/n} "Let her think she owns me. Let her come and collect, if she likes. I'd rather be hunted by a queen than pardoned by one; at least the hunt is interesting." {n}She drops the map on the Table.{/n} "Now feed me something. Defiance makes me hungry."`
The `held`/`failed` nodes are Nocticula's voice and stay with that row.

4.2 Nocticula: `nocticula.trickster.court.arueshalae` reads `arueshalae.committed` blind to the branch (S5); legacy-only, no
change proposed.

4.3 Merged rows (read for contradictions only): Camellia, Wenduag, Shamira, Vellexia and Minachiv pair rows with her and
`shamira.trickster.react.arueshalae_*`, `herrax.trickster.react.arueshalae_*` all split on `arueshalae.corrupted`, which the
two new scenes do not change. No contradiction with the sergeant or the other one. Wenduag's and Shamira's explicit
slots stay blocked as their reviews note.

4.4 Not this row's woman: the four claude-work-queue items `aranka.react.arueshalae.{dreamer,fallen}(.yard)` (woman
`aranka`, finding aranka:D08-D11, staging of Aranka's copy) are Aranka's; left for her owner.

## 5. Explicit slots (Gemory tracker)

No new brief. Read for opportunity: `fallen.sergeant` (a man other than the Commander is present and fed on: never an
explicit host, CHARACTER-TRUTH 10), `fallen.the_other_one` (not a heat beat), the Seelah fallen pair (Seelah refuses her).
Existing briefs unchanged: `arueshalae.trickster.fallen.roof.explicit.1` (live fallen road; the new `sergeant_watched`
answer is a valid heat note for the Gemory pass: she wants the Commander watching, and the roof is where she makes the
Commander count), `treatment.night.explicit.1/2` (redeemed), the two ARCHIVAL `evil.window*` briefs (legacy road).

## 6. Validation

- `python -m py_compile` on `storylines/arueshalae_trickster.py`, `storylines/arueshalae_cloud.py`, `expansion.py`: OK.
- Module import: both new scenes build through `evil_hub` (ids, requires, forbids, Next/Set verified).
- Simulated export: `arueshalae_cloud.apply` twice on main's export + the new scenes: every assertion held, idempotent.
- `python tools/prose_pending_lint.py --integration` (main and simulated export): 0 hard failures. Without
  `--integration` main already fails (pre-existing: placeholders need a held scaffold job).
- `python tools/claude_work_queue_lint.py`: 0 hard failures (queue unchanged: see 4.1/4.4).
- Not run (coordinator runs remotely): `expansion.py`, savecompat, payoff_lint, voice_lock_lint, player_text_lint,
  text_structure_lint, edge_lint, unit tests. `voice-approvals.proposed.json` carries before/after shas for the four
  changed locked/unlocked scenes and the two new scenes; after_sha is from the simulated export and must be recomputed on
  the build.

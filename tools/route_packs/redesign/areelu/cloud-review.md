# Areelu Vorlesh: cloud design-first review (villain-route-areelu)

Owner: cloud voice owner, 2026-10-08. Base: wotr-mod `main` abb97e4. Scope (CLOUD-QUEUE villain row 5): `areelu.*` and
every scene where Areelu appears; shared scenes whose other villain sits LOWER in the villain table (Camellia,
Horzalah, Wenduag, Nocticula, ...). Hepzamirah and Melazmera sit above this row: proposals only (section 6).
Truth pages read: writer `knowledge/characters/areelu-vorlesh/` (canon, voice, relationships, states, decisions,
native-lines.json, 117 explicit-speaker lines), `handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (binding contexts
1-6), `plans/route-redesign-pipeline.md`; mod `tools/route_packs/voice/areelu.md`.

Presence read from the export (`development/Story.json`): 66 owned `areelu.*` scenes (about 29,600 words: Ch2 Long
Con crossing 3, Ch4 audience 1, Ch5 rivalry/lens/cell 4, Ch6 Threshold 9, reactions 3, finale and closure pages 14,
report pages 20, afterlogue/native replacement lines 10, Last Call 2), 12 household pair scenes
(`household.pair.{iomedae,yaniel,nidalynn}_areelu.*`) and 74 appearance scenes in other routes (Dorgelinda ledger,
Targona, Hepzamirah, Yaniel, Nenio folio, Terendelev, Eritrice, Eliandra, Iomedae, Nidalynn and Yaniel Last Call
pages, the Trickster Last Call bottle chain, Shamira, Arueshalae, Nocticula). Machine truth table:
`truth-table.json` beside this file (148 flags her scenes or her pairs read or set: every producer choice with its
text, every consumer gate with the text relying on it, Derived/native readers, before and after this pass).

`python expansion.py` was NOT run to completion: this environment has no `blueprints.zip`. In addition, `main`
itself does not build at abb97e4 independent of the zip: commit e26d856 (villain-knowledge explicit slots) added
`explicit_slots/camellia/camellia.trickster.bond.witness.explicit.1.json` and
`...evening.the_prisoner.explicit.1.json` without the `insertion` key that `camellia_round2._slots` requires
(KeyError). Not in this row's scope; reported to the coordinator. See "Validation".

## 1. Structural defects (fixed first)

| # | Defect (export evidence) | Class | Fix (text/paragraph only; ids, choice positions, Set/gates untouched) |
|---|---|---|---|
| S1 | Flag overload with an unearned outcome. `areelu.trickster.cost.late` is set by three semantically different producers: the Ch5 lens primer (`rivalry.lens/terms>0,>1`, `window>0,>1`, the R2-2 fallback when the Iz bet was missed), the late acceptance at Threshold (`wager.at_threshold/*>0`) and the unprimed entry fee (`wager.unprimed/*>0`). Only the Threshold producers ever stated the late terms ("If I burn, you keep nothing: not my notes, not my name"). The consumers quote them to every holder: `finale.rewrite/end#P3` ("had agreed to worse terms"), `finale.after/end#P4` ("The late terms had promised the Commander nothing of hers"), `wager.raised/late_raise` ("The late terms stand"). A lens-then-cell player was held to terms nobody offered. | BEL/HOW | The lens now states the late terms where it sets the flag (`rivalry.lens/terms`: "Late wagers carry late terms ... If I burn at Threshold, you keep nothing of mine. Not a page. Not my name."), and the cell's frost branch, the only cell branch a lens player can take, repeats them (`wager.struck/frost`). The flag keeps one meaning: "the wager was taken on her late terms". |
| S2 | Integration gap, a cost with no consequence. The Iomedae pair (`household.pair.iomedae_areelu.reconstruction/originals,families`, `repair/restored`) has Areelu open three experiment files (K-17, K-22, K-31) for a goddess and sets `cost.areelu_records_opened`, `account.delivered`, `cost.iomedae_names_received`; the rejected branch sets `cost.commander_false_apology` (an apology forged in her name). Fifteen of the pair's flags have no reader anywhere (truth table `before.set_never_read`); unlike the Yaniel and Nidalynn pairs, nothing in her route ever mentions it. | BEL/AGY | Two read-only consumers: `threshold.welcome/start` (Ch6 gate, appended paragraphs: records opened -> she offers the mason's last words, "He was the most informative of the three"; forgery -> "I have never before been called sorry in someone else's hand ... I keep a list") and `lastcall.page/page` (appended after every existing paragraph). `records_opened` and `false_apology` go from 0 to 2 readers. |
| S3 | Branch-false text. `finale.unnamed/end#P0` (Forbids `stake_named`) said "Neither party had named her work as a substitute" and "The wager had called the stake 'what is left of her'" to a player who, at the rift, answered "Your life. Nothing less." (`wager.raised/collect>2` -> `life`, sets `areelu.trickster.term.life`, whose only reader was `wager.collect`'s Forbids). | BEL/HOW | P0 rewritten to be true on every history ("Nobody had named her work as a substitute for her life ... it was collected"); new appended paragraph reads `term.life` ("The terms were met to the letter"). |
| S4 | Wrong voice/person. `areelu.lastcall.page` opens in her first person ("I will record, since I am obliged to record everything ...") and its household paragraphs P3-P6 switch to a clerk's third person ("At the laboratory projection, Areelu traded away the use of Yaniel's name and likeness"; "The Windstep complaint still lacked an inspected answer"). | VOI/HOW | P3-P6 rewritten in her first person, same gates and indices. |
| S5 | Stale reference to unstaged content. `finale.stake_only/end#P3`: "The locked cellar held no cart of her notes." No cellar or cart exists on any history that reaches a stake-only closure. | CAN/BEL | Rewritten to what the closure stages: nothing of hers stays behind. |
| S6 | Branch-false on the punchline history. `finale.survived/end#P1` establishes that "the laboratories did not burn in this ending" (`trickster.cheated_death`, graft not drawn). Two report pages reachable on that history said otherwise: `report.dagger/why` ("The fire took my records") and `report.prison/start` ("Past the burnt workrooms"). | BEL | Both lines rewritten to be true on both histories (the crystal's memory of Deskari's blood; "the gutted workrooms"). |
| S7 | Wrong medium check: none found. Lens scenes are frost letters (remote, `Remote: true`), the cell and Threshold are face to face, the pair scenes use the lens or the laboratory projection as their `ParticipantContacts` state. | - | - |
| S8 | Recorded, not fixed (dead but harmless): `finale.not_burned/end>2` requires and forbids `areelu.committed` (saved index); `report.afterword` and `react.seelah_objects` are retired by gating (`areelu_trickster.RETIRED`, Forbids `trickster.ever`), so Seelah has no reaction to the romance (ledger reactor allocation is Nenio and Ember only). `report.afterword/leave` still cites "worth it", text that no longer exists; unreachable, left. | none | Kept for save compatibility. |
| S9 | Recorded, chosen loss: the lens's second and third questions (`belongs`, `slept`, `notes`, `frost`) all set the single `areelu.trickster.lens.asked`; "Remember that you said it, Commander. I will." (`belongs`) has no reader that can tell the answers apart. A new flag would need a new Set. | BEL ~-1 | Left. |
| S10 | Recorded: `wager.raised/household_face_price` (Speaker `conversant`) and `s51_field_route` (Portrait "") break the scene's speaker presentation. Speaker/portrait are presentation fields this pass does not touch. | HOW ~-1 | Left for a structure job; text is in her voice. |

Checked and sound: every Threshold callback is gated on its producer (`iz_bet>2` on `noticed`, `welcome>3` on
`noticed`, `raised>2` on `threshold_reminded`, `truth.the_desk>2` on `promise_heard`, `raised>1`/`hand` on
`real_hand_asked`, `priced_known` on `stake_named` + the cell seen, `collect` on `stake_named` + `wound_ceded` +
`cauldron_full`); every report page requires `areelu.committed` and her survival; the Last Call page requires
`committed` + `payoff.partner` + presence. No flag overload besides S1. `areelu.*` route flags: 0 set-never-read.

Canon correction to the knowledge pages: `decisions.md` marks "the Commander shares a soul with her child" UNRESOLVED.
Native `753fd1bf` (Epilogues_afterlogues/Cue_29) resolves it: "it took a hundred years and a million deaths for me to
bring back the one whose life had been so cruelly stolen away. And it cost one more death, my own, for {mf|him|her}
to keep on living", the returned child gendered by the Commander's token; with `4cf21739`/`dbfa68f2` (the soul as
"soil, in which I can grow the seed"). The shared-soul pages (`report.graft/stand`, `report.promise`, `report.name`)
are therefore canon-backed and were left as written. The Commander is still never treated as her child.

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten (all in `storylines/areelu_cloud.py`):
- `rivalry.lens/start`, `lens.watched/look`: the lens showed "a woman's hand at a desk, writing notes" (menace by
  notes, CHARACTER-TRUTH 2). Now the hand is at work: a crusader strapped down while she lays demon sinew into his
  opened forearm, then picks up the pen and goes on writing about the Commander; a dretch with its jaw wired open
  fed violet drop by drop while she counts. Her own route already establishes it (Yaniel: "I watched her sew demons
  together and graft their limbs onto crusaders"; Suture's "all the ones Lady Areelu worked on", `02a4264d`;
  Targona, `4f99b73b`).
- `rivalry.lens/terms`, `wager.struck/frost`: S1.
- `household.pair.yaniel_areelu.inspection` start/comparison/undertaking/retained: she spoke like an archivist ("a
  working index", "published work"). Now the guise was taken down from life while Yaniel lay on her tables, "men
  wept to see it and told it everything", and she would wear Yaniel again ("a fresh likeness saves a great deal of
  guessing").
- `household.pair.iomedae_areelu.reconstruction` originals.work/families.match: "He was awake for it; the method
  required that"; the column nobody asked for (the hour each man stopped asking for his family); the drover nine
  days in a cage waiting for a free table.
- `household.pair.nidalynn_areelu.cell/start`: the field route is now what it was, a trail she used to take subjects
  from the Windstep herding families ("slow things can be counted"); "I cannot give her that, and I would not if I
  could."
- Closure pages `finale.unnamed`, `finale.stake_only`, `finale.report_stands`: settlement-clerk register ("She
  recorded the personal wound owed under the original wager; her own papers were not payment") re-voiced.
  `finale.lien_bottled/stands`: "an invoice for the binding" (paperwork) -> bound "in a pale, fine-grained leather that
  the Commander did not recognise and did not ask about" (the souvenir line, `rift.odds/souvenir`).
- Afterlogue replacements (native Cue_0004/Cue_0005, spoken to Pharasma before her native verdict): six flat lines
  ("My child's soul remained unresolved") now speak to the goddess at her native register, unrepentant
  (`37ef9f4c`/`e8e08c11` defiance, `e44c123f` she does not stop): "Your clerks will have found some of my vessels by
  now. Not all."; "My child was not returned to me, and I have not forgiven you for it."

Left alone (they work): the Ch4 audience file scene ("You know where to put the knife, Commander"), the Iz bet, the
lens night questions (surveillance kept as an unhealthy dynamic: she watched the Commander sleep and wrote down the
hour), the cell wager ("I do not accept jokes as collateral", "I remember everything that is done to me"), the
Threshold scenes (welcome, the desk and the moth, rift odds "I will cut it out of what is left of you, very carefully",
the clause, at_threshold/unprimed terms, collect, raised, last words), the Long Con crossing, the report pages that
already show her doing it on screen (convicts: thirty dead condemned and the heading "Usable"; commission: the
volunteer's demon arm and "I have left the choice of month to the arm"; cult: the poisoned method that ate the
circle; hunters: the brand-bearer's eyes; rival: the philosopher ruined; lady: failed vessels traded to Pharasma, the
rest kept; sarkoris: "I am not sorry. I would do it again, and I would do it better"; promise: the hidden notebook
on extracting her child's share, "Every morning it says: not today"), the intimacy pages (her appetite, her terms,
reading every letter in the Commander's desk), Nenio's and Ember's reactions.

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 90 | 91 | Native hooks unchanged (Audience_Areelu 199a940b, Iz 09b8d5eb, AreeluCell 74989c07, Threshold bb352875/64af2f5b/90861396/f56a69dc, afterlogue Cue_0004/0005). S5 removed an unstaged cellar/cart; shared-soul premise verified (`753fd1bf`). Authored, no canon claim: the strapped crusader and the dretch in the lens, the Windstep trail, the drover's cage. No race, child's name or new place. |
| VOI | 84 | 90 | Cold, exact, condescending, zero profanity (`670f8e52` "How very mortal of you!", `ed828886`). Contempt as diagnosis ("He was the most informative of the three"), calm forecasts as threats (`dbfa68f2` register: "Do not do it again, Commander. I keep a list."), the goddess "who was mortal not so long ago" (`4cf65db7`). The clerk third person (S4) and the settlement summaries are gone. |
| TRK | 92 | 92 | Device unchanged: the wager "whoever burns pays up", the stake reread as her notes and graft, the Council's soul cauldron drawing the Abyss out of her (`wager.collect`), the Last Call flask. |
| INT | 89 | 91 | Pair outcomes now reach her route (S2); `term.life` read (S3); cost.late means one thing (S1). Native readers unchanged (`notes_told`, `crib.*`, `years_asked`, `promise_heard`, `cell_visited`, siphons, the Kenabres dagger). |
| BEL | 82 | 89 | Every outcome she quotes is earned where it is set (S1), every closure page is true for every history that reaches it (S3, S5, S6), costs paid in the pairs have consequences (S2). Reactions: Nenio, Ember, Dorgelinda ("No experiments on my soldiers"), Iomedae, Yaniel, Nidalynn, Targona, Terendelev. Seelah retired by design (S8). |
| COX | 90 | 90 | No elimination; Iomedae, Yaniel and Nidalynn keep their agendas and their own refusals ("I have asked for their dead. You will receive no pardon for naming them."). Hepzamirah's grudge ("I expect she would like my soul in a jar") stands unanswered (proposal 6.1). |
| HOW | 86 | 90 | Truth table shipped; every new paragraph reads a flag with a producer; the layer raises on any drifted text or unresolved node/paragraph; S8-S10 recorded. |
| AGY | 80 | 88 | Her own agenda in every pair: the work, the child, the guise she may wear again, subjects taken from refugee trails; Iomedae wants the dead named, Yaniel wants her face back, Nidalynn wants the trail burned. None of it is about the Commander. |
| ALIGNMENT LENS | 85 | 92 | On screen: the crusader's opened forearm and the sinew, the dretch fed until it swells, the experiment files with the hour each man stopped asking for his family, Windstep families taken as subjects, the condemned in the lime-kiln cellar, the volunteer's arm, the cultists eaten by her poisoned method, a report bound in human leather. Unhealthy dynamics kept (surveillance through the lens, reading the Commander's letters, "I will take {mf|him\|her}" every morning). No redemption: "I would not if I could"; "I have not forgiven you for it." |

## 4. Explicit slots (Gemory tracker)

- Existing briefs (`explicit_slots/areelu-vorlesh/`, 8; `test_areelu_round2` asserts that count): hosts and default
  texts unchanged; none of the nodes this pass rewrote is a host or a boundary (`report.participation`,
  `report.inn`, `finale.company`, `finale.lien_bottled/across`, `finale.ascended/asc_night`,
  `finale.not_burned/nb_across` untouched; `lien_bottled/stands` is not on a slot path).
- New brief (in `explicit_slots/areelu/`, since the `areelu-vorlesh/` count is pinned):
  `areelu.trickster.report.rooms.explicit.1`, Commander + Areelu at her desk across the hall, host `report.rooms/pen`
  ("Or keep it and stay"), next beat `end`. Needs a structure hook (a slot node between `pen` and `end`, as
  `in_mortal_2` -> `participation.explicit.1`) before generation; recorded in the brief.
- Pre-existing slot debt (not caused here): the 8 `areelu-vorlesh/` briefs carry list-typed `facts`
  (`slot_brief_lint` schema finding) and their facts text calls the shared soul "verified" without a key; `753fd1bf`
  is the key.

## 5. Not done / handed on

- `claude-work-queue.json` and `prose-pending.json`: no Areelu entries exist; nothing to resolve. No `[PROSE PENDING]`
  in her scenes or pairs.
- S8-S10 need a structure job (speaker fields, retired pages); S9 needs a new Set to distinguish the lens answers.
- Lock enrollment and voice approvals: the coordinator applies them. Proposed before/after text hashes for every
  changed Claude-locked scene: `voice-approvals.proposed.json` beside this file.
- The knowledge pages (`decisions.md` commander_not_child, `relationships.md` child) should cite `753fd1bf` and drop
  the UNRESOLVED marker; writer repo, not changed here.

## 6. Shared scenes owned by higher rows: proposals only

6.1 Hepzamirah (row above). `hepzamirah.trickster.body.terms/why` ("Vorlesh had my place before I was cold. I expect
she would like my soul in a jar beside it"), `bond.vorlesh`, `bond.eve` ("into Areelu's laboratory"),
`epilogue.leavable#P12/P13` (the promised first sight of Vorlesh). Contradiction: none. Gap: when both
`areelu.committed` + `areelu.trickster.survives` and Hepzamirah's household commit hold, the two share the
Commander's house and nothing reads it. Proposal: one gated paragraph on Hepzamirah's living epilogue, in her
register, e.g. "Vorlesh lived across the hall. Hepzamirah kept her pick by the door and her back to the wall, and
every morning she told the witch, loudly, which jar she would not be going into." (requires
`hepzamirah.trickster.bond.vorlesh`, `areelu.committed`, `areelu.trickster.survives`, `areelu.present_now`).
`household.pair.delamere_hepzamirah.hearing` ("Vorlesh wears my old office"): no native key in the Areelu pack
gives her Hepzamirah's archpriesthood (Katair calls Deskari "her patron", `706cd5e9`); the Hepzamirah owner should
verify the claim or soften it to "Vorlesh has my father's ear".
6.2 Melazmera (row above): no shared scene found.
6.3 Nocticula (row below, but `noct.*`/`nocticula.*` are leased to noct-reconcile): `nocticula.trickster.defeated.late_shadow`
("Tomorrow you go down to meet Areelu") is consistent. Canon gives Nocticula a reason to hate her ("That little
bitch", `e34b006d`; "slitting her throat", `f079f66d`); no scene reads `areelu.committed` there. Proposal for the
Nocticula pass: one line when both routes survive.
6.4 Dorgelinda (not a villain row): the disclosure "Areelu Vorlesh ... We are lovers." is gated on
`dorgelinda.ledger.current_other.areelu` (Derived from `areelu.harem.eligible`); her answer ("No experiments on my
soldiers") fits the convicts and commission pages. Consistent.

## 7. Validation

- `python expansion.py`: cannot run here (no `blueprints.zip`), and `main` fails independently (camellia briefs,
  above). Instead the full build ran with the zip readers stubbed (`native_facts.verify`,
  `native_fact_inventory.verify_inventory`, `native_overrides.finalize`,
  `crossroute_checks.other_woman.native_participation_contexts`) and the two `insertion`-less camellia briefs skipped
  in the scratch wrapper only. Results, baseline-vs-branch diff and lint counts are in the commit message of this
  branch's last commit (VALIDATION section).

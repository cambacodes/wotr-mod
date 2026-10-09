# Nocticula: cloud design-first review (villain-route-nocticula)

Owner: Claude voice owner, 2026-10-08, local branch `claude/cl-nocticula` (base wotr-mod main 6662e2f). Scope
(CLOUD-QUEUE villain row, wave 2): `noct.*`, `nocticula.*` (including `court.arueshalae/.shamira/.vellexia`),
`household.pair.{nocticula_shamira,galfrey_nocticula,iomedae_nocticula,arueshalae_nocticula}.*`,
`arueshalae.trickster.evil.second_opinion`, her Last Call account `trickster.lastcall.account.nocticula`. Not hers:
`nocticula.trickster.court.horzalah` (Horzalah row, merged): read only, no change proposed.
Truth pages read: writer `knowledge/characters/nocticula/` (voice, canon, route, native-lines.json, 114 lines),
`handoffs/CHARACTER-TRUTH.md`, `TRICKSTER-RUBRIC.md` (binding contexts 1-6), CLOUD-BRIEF, CLOUD-QUEUE (wave 2 rules and
the inherited proposals of the Shamira, Areelu, Vellexia and Horzalah reviews), the noct-reconcile report
(`drafts/claude-jobs/noct-reconcile.locked.md`) and the Arueshalae row's review (4.1, coordinator note).

Presence read from the export (`development/Story.json`): 195 owned scenes. Live: the harbor route (`noct.unlit_quay`
... `noct.second_door`, 15 scenes, voice reconciled by noct-reconcile), its 8 endings, the Trickster acquisition
correspondence (`noct.acq.*`: 3 audiences, the folded letters `the_missing_line`/`the_paid_address`, the correspondence
epilogue), the defeated-at-the-Council chain (`nocticula.trickster.defeated.*`: floor, shadow, late shadow, call-in,
chair 224 nodes, morning, 11 epilogues), `palace.brothers_voice`, `early.gresilla_credit`, `ch4.hoard`, the court
scenes, `epilogue.commit`/`declined`, `partner_terms.threshold`, both Last Call pages and the call, the reactions
(Daeran, Nenio), the four pair rows. Retired (unreachable, kept for saves): the 8 `noct.retired` harbor scenes,
`noct.acq.the_retained_copy`, the three `noct.join.*` and every `*.acquired.*` harbor/ending copy (nm1 deferral: they
Forbid `chapter_later`, held from Chapter 2; the acquired endings also Require `noct.join.*` flags whose only
producers are retired), `nocticula.trickster.court.arueshalae` and `arueshalae.trickster.evil.second_opinion`
(Forbid `chapter_later`; the favour they trade has no live producer). Retired scenes were scored only where a live
page quotes them.

Machine truth table: `truth-table.json` beside this file (545 flags; producers, consumers, `consumers_before` on main,
status, a `note` on every flag this pass touched). Regenerate with
`python tools/route_packs/redesign/nocticula/truth_table.py <branch export> development/Story.json`. Clone families are
folded (`.acquired.*`), retired scenes are prefixed `RETIRED`.

`python expansion.py` was NOT run (coordinator instruction: no full builds on this PC; the remote build is the
coordinator's). Validation below applies both new layers to the committed main export.

## 1. Structural defects (fixed first)

| # | Defect (export evidence) | Class | Fix (text / appended paragraphs only) |
|---|---|---|---|
| S1 | The partner-stance block: 24 paragraphs gated on Shamira's state and the partner stance, printed verbatim on 30+ pages (`nocticula.trickster.epilogue.commit:{refused_page,after_paid,after_refused,inn}#0-23`, `epilogue.declined`, all 11 `defeated.epilogue.*`, `nocticula.lastcall.page#3-26`, `nocticula.acquisition.lastcall.page#4-27`, `noct.acq.epilogue.correspondence`, the 7 harbor endings, `noct.ending_death` variants, `ending_aeon#0-3`). Report register throughout: "Shamira's name remained in the court's accounts", "No guest could claim the Ardent Dream's agreement", "The courtiers ... sold copies of the exposed invitation. No answer came from the Ardent Dream herself", "The Commander had asked for a secret affair. Its private invitations were evidence". Shamira (canon `d3fd424b` chosen lover, `7328c1e1` covets the throne) never acts; Nocticula never acts. | VOI (binding context 6: off-screen summary), AGY (both women inert), BEL | Every body re-voiced in place, gates untouched, so each reads true for every run its gate admits: Shamira's yearly undrugged-but-maybe-poisoned wine (exclusive), the spies flayed on the Harem steps (exposed), the new body appraised and not taken to bed (embodied), the commentary from inside the skull (mind), the fight for the Harem bet on from a balcony (dead), the servant nailed beside her refusal (exposed + alive); Nocticula arranges jealousy for the refused-exclusive Commander (voice pack: "she arranges it and watches"). `noct.ending_death` and `ending_aeon` variants re-voiced to the same standard. |
| S2 | Reveal before staging / cross-chain leak: the defeated chain's partner discovery (`defeated.chair:partner_discovery.morning_late(_paid).0*`, `defeated.morning:partner_discovery.{start,note_paid_alone,daeran}.0*`) is the letter route's block copied verbatim: "The clerk has put the morning dispatch on top of your private packet", "A scrap of Nocticula's invitation has come back", and the fallout "She corrects the broker's demand in three strokes". The Threshold chain has no clerk, no invitation and no broker; the only mark is the four crescents from the chair night. The choice "[Keep the signed invitation. Let the clerk carry the next one.]" offers a paper that does not exist there. | INT (reveal of unstaged content), BEL, VOI (paperwork) | Threshold variant: a too-pretty runner from the Harem of Ardent Dreams at the tent, who saw the crescents; Shamira's message recited in her voice ("I know that mark, mortal. I have worn it"); in the mind variant the voice behind the eyes speaks first; dead/caged variants: her courtiers sell it. Fallout: the shadow says the terms (summons only, the antechamber among petitioners) and then closes over the runner on screen ("She sold you to Shamira's court. I do not like my things sold."). `letters_burned` ("Take no marked gifts"): the Commander burns the crescents off with a heated knife. Choice relabelled "[Keep her marks. Let them show.]". The letter-route copies (`noct.acq.*`, the acquired harbor copies) keep their letters, re-voiced (Shamira: "I have had it on my skin"; the carrier is skinned "while you read this"). `noct.second_door`'s own discovery (noct-reconcile) left alone. |
| S3 | The favour named twice on one page: `epilogue.commit:refused_page#24/#25` and `:inn#24/#25` both Require `cost.shade_paid` and print two different namings ("a chair ... when matters of state were heard" by sealed note; "a chair at your right hand, wherever you eat" by sealed note the next spring). | BEL (contradiction on one page), VOI (notes) | #24 is the naming, in person, in the second spring (matching `lastcall.page#0` and `defeated.epilogue.favour`): she walks into the Commander's council mid-sentence and takes the chair. #25 is its sequel at dinner (she looks through two open doors at the bed the Commander refused and goes back to her plate). |
| S4 | Last Call as paperwork and a false claim: `nocticula.lastcall.call` "Her mark lies on the account in your pocket; no promise of a night together appears beside it. You read the debt aloud." and `trickster.lastcall.account.nocticula` "The Lady in Shadow's ledger still lists the price ... You mark it beside the other claims ... No answer from her is needed to keep that entry" (designer note). Both say "a refused invitation", false in every said-yes run. Lastcall readers `epilogue.commit:refused_page#26`, `after_*#31`, `inn#26` were report lines ("Her accounts survived it"). | VOI, INT | The call: the night before Threshold, her name said into the Commander's shadow; it answers ("I am not a debt. I am the one who is owed ... I want my favour paid by someone with a pulse"). The account (not calling): the shadow is left lying; the favour stays hers to name at the worst hour. Lastcall readers re-voiced (the empty chair kept visibly empty; the inn's guests all dream the same dream). |
| S5 | W5 pair readers on her own Last Call page (`nocticula.lastcall.page#28-#91`) were first-person ledger entries: "Two courier fares and the pilot's survey cost 200 Finances: 150 and 50 respectively", "The inspected ransom cost five hundred", "I let her factor keep the levy". Two readers name a prisoner "Venn" who is Veldran on the pair row (`household.pair.iomedae_nocticula.open` lists Orren, Davit, Hald, Marten, Veldran, Rul). | VOI (binding context 6), CAN (internal contradiction) | All 32 bodies re-voiced as consequences with her appetite on screen (the factor's collecting hand taken; "He poured left-handed now"; the broker lasts nine days without her protection; she takes her cut when the abandoned two are sold); Venn corrected to Veldran. Gates and indices unchanged (W5 inventory checks gates only). |
| S6 | Promises and harem results without a reader (truth table `set-never-read`): `noct.crimson_mark` / `noct.mark_hidden` ("Leave it where it shows." / "Cover it.", `her_own_face:mark`), the Commander's lodge confessions (`noct.lodge_appetite_admitted`, `_vigilance_admitted`, `_danger_desired`, `_desire_contested`), `household.pair.arueshalae_nocticula.unsettled`, `nocticula.harem.attitude.arueshalae.respect`, `household.pair.nocticula_shamira.resolved`; Areelu review 6.3 (no Nocticula page reads `areelu.committed`). | INT/BEL (choice without consequence), AGY (harem integration gap) | Appended, flag-gated (append-only, after every existing paragraph): six harbor readers + the Areelu line on `noct.ending_{company,alliance,limit}:end` (the brand worn at the throat that paladins look away from; the confession quoted back every time the Commander says "duty"; the headboard); the Areelu line on `defeated.epilogue:end` (`areelu.committed` + `crossroute.areelu.available`: the assassin she never sends, and where she would have started the knife; native `e34b006d`, `f079f66d`); on `noct.acq.epilogue.correspondence:page` the renunciation respected (three succubi try the same; none live), left disputed (a black silk leash on the step every year; "the year she did not bother to burn it, Nocticula sent two"), and Shamira's precedence (fought over in public, settled in bed). Each reader requires the woman's current presence. |
| S7 | Paperwork villainy in the acquisition hunt: `borrowed_signature.start` ("This makes me sound like an office with inconvenient hours"), `.offer` ("a signed undertaking naming your part in the investigation ... your recorded cooperation"), `the_paid_address:start/network/public` (counterfoils, rental accounts, "the first ledger page"), choice labels "Accept the copied-report obligation", "Keep the restitution account and relinquish the reusable pattern". The chain's edge counts: business 112 vs menace 9. | VOI (binding context 6), BEL | Same premise and choices: the forgery is a man selling her ("I want his hands, and I want them while he can still feel them"); the signature becomes "Your neck, in my drawer. Now that is a gift."; the merchant's cell is found locked and empty, his hands on the clerk's desk wrapped in his own advertisement (public branch); the copying office whose writers are "later, visited" (network branch). Ten choice labels re-voiced to the same flags. |
| S8 | canon-fix1 (claude-work-queue, 110 entries): `Neris`, `Vessa`, `Mera`, `Harem of Ardent Dream` collide with or misstate canon. | CAN | Renamed in every owned surface (Nerethi, Vezhara, Merzila, Harem of Ardent Dreams; also `noct.sixth_passenger`, which the queue missed). 78 queue (scene, name) items had a hit (asserted by count); 32 had none on main (already fixed by merge-k "Ardent Dreams" or never carried the name) and are closed. `mod_entities.json`: the three names moved from `pending_entities` to `entities`. |

Overload analysis (no split needed, recorded): `nocticula.partner_stance.exclusive` has three producers that mean
different things: her promise (`partner_terms.*.chosen`, with `partner.exclusive_chosen`), the Commander accepting her
refusal (`*.dead/cast/declined.exclusive>0`, with `partner_exclusive_refused`) and "Yes. We are finished." (with
`exclusive_refused` and `noct.closed`/`noct.acq.closed`). Every live reader pairs it with `exclusive_chosen` or
`exclusive_refused` (`#12`/`#13` on every stance page, `ending_aeon#2` with `crossroute.shamira.available`, which only
the promise can satisfy); the closing producer also closes every page that reads it. `noct.acq.channel_*`,
`noct.acq.pledge_*`, `cost.shade_paid/refused/late` and the Shamira state flags are single-meaning.
No other overload found. Presence: every live owned scene requires `nocticula.present_now` or
`nocticula.reachable_by_letter` (derived from it) or is a Commander-side page; the defeated chain is gated on
`noct.defeated_not_dead`/`trickster.ever`, never on a free return.

Recorded, not fixed:

| # | Item | Why not here |
|---|---|---|
| R1 | `nocticula.trickster.court.arueshalae` and `arueshalae.trickster.evil.second_opinion` are retired (Forbid `chapter_later`); second_opinion's nodes print "(Retired 2026-10-01: ...)", `the_retained_copy.*` prints "(Retired: this meeting is folded ...)". | Unreachable; ids kept for saves (rubric pre-release rule). Designer text in unreachable nodes left as the retiring rows wrote it. |
| R2 | `nocticula.lastcall.call` choice 0 Forbids `noct.dead`, but the scene Requires `nocticula.lastcall.account_due` = `favour_due` = `cost.shade_paid & noct.defeated_not_dead` (which implies `noct.dead`): choice 0 (the one that sets `trickster.lastcall.creditors_called`) can never show. | Gate change (structure/coordinator). Text written to hold for both choices. |
| R3 | `nocticula.harem.stance.joined/tolerated/joined_late` have no producer anywhere, so `guest.nocticula` in the Ledger always prints its no-stance line (same as Devarra R3). `*.harem.enmity/reconciled.*` are runtime PendingHooks. | Household-stance writer is engine structure. |
| R4 | 79 set-never-read flags remain, mostly the Commander's receipts in the harbor (`noct.asked_*`, `*_rule_known`, `teren_returned_once`, `ilvara_pin_taken`, `lease_bought`, `halren_returned`, `records_auctioned`, `work_private`, `own_face_chosen`, `quiet_evening`, `private_night`), the acquisition receipts (`petition_candid/watchful`, `author_offer`, `collateral_given`, `merchant_held`, `inquiry_visible`, `undertaking_held`, `personal_declined`) and the Galfrey/Iomedae `*.held/unsettled/proof.*` receipts (their costs are read). | Flavour receipts whose prose promises nothing further; chosen loss (~-1 INT). |
| R5 | The rest of the acquisition chain (`the_missing_line` before the forgery, the audiences, `her_hand.*`, `an_answer_of_her_own.*`) keeps a dry court register (business:menace 3.07 after this pass, 12.4 before). It is wit, not paperwork, and her lines carry threat ("I am often interested in things I intend to punish"); not re-voiced line by line. | Do-not-polish rule; the paperwork plot itself (S7) is fixed. |
| R6 | 56 of the locked scenes changed here already differ on main from their `voice_locks.json` hash (noct-reconcile's approvals are proposed, not applied); `voice_lock_lint` on main: 236 changed / 252 hard, branch export: 298 changed (the +62 are this pass, all in `voice-approvals.proposed.json`). | Coordinator applies approvals. |
| R7 | The `*.acquired.*` copies (frozen baseline) got the renames and the shared-body re-voice through the same identical-text replacement; the six `noct.acquired` ending readers in the old Codex register ("Vezhara's damaged hand never vanished from the account ...", "They named conflicts before turning them into bargains") were not rewritten. | Unreachable (S0 deferral); renames done for the queue. |

## 2. Prose that failed (rewritten) and prose that works (left alone)

Rewritten: in `storylines/nocticula_cloud.py` (called last in `expansion._make_expansion`, after devarra_cloud): S1-S8
above (74 paragraph bodies, 26 node texts across their copies, 8 substring edits, 10 choice labels, 13 appended
readers, the renames). In `storylines/harem_rows/zzz_nocticula_pairs.py` (row order: after `zz_contract_controller`):
the 16 placeholders of `household.pair.arueshalae_nocticula.{settle,retry}.{redeemed,corrupted}` and
`household.pair.nocticula_shamira.precedence.live` (Nocticula's answers through the half-seal: "I am the Lady in Shadow,
girl, and I do not need you on your knees to remain so ... It will cost you more than kneeling would have"; the split
wax and "Mine. Come home on your knees, girl, or do not come home at all"; "Twice. The second time is always less
convincing"; the two precedence letters from the Shamira review, "steward" corrected to her title), Arueshalae's six
corrupted lines exactly as the Arueshalae row proposed (its review 4.1; my held line says "the girl", not "my
succubus", so her "not 'my succubus'" lands), and two Nocticula lines in the Galfrey row (the clerk who will not need
a tongue; "Bring the hand you collected with").

Left alone (they work and are the route's bar): the harbor route and its endings' own text (noct-reconcile: Orren's
hands, the lamps, Rhez's knife, "You are mine to disappoint", the cauldron magician); the defeated chain's floor,
shadow, late shadow and call-in ("Say what you saw, clown. Say it now, so I can decide what it costs you"; the boot on
the shadow; "Silence you give me. Safety I sell you"); `brothers_voice` (the bookmark tongue), `ch4.hoard` ("I do not
sell my things, mortal. I spend them"), `gresilla_credit`, the chair's answer and night, `epilogue.commit`'s own nodes
("Kneel, or kiss me. Choose quickly. I bore easily."), the court scenes (`court.vellexia`, `court.shamira` "Hello, my
dear", `court.horzalah`), the partner terms' Nocticula lines ("End it? You speak as though I were dismissing a
chambermaid"), the audiences, `noct.second_door`'s discovery, the Iomedae row (her release order and Iomedae's
"abomination" already carry both women).

## 3. Rubric (judged on the post-fix export; before -> after)

| Dim | Before | After | Evidence |
|---|---|---|---|
| CAN | 86 | 91 | Native frame intact: the Council death and projection (`ede5d639`, "a queen does not come back"), Baphomet's heart (`13c0979e`), the Gift reading thoughts (`16243ce7`), the Harem of Ardent Dreams and Shamira as chosen lover who covets the throne (`d3fd424b`, `7328c1e1`), Areelu as her betrayer (`e34b006d`, `f079f66d`). Fixed: the four colliding/misspelled names (S8), Venn/Veldran (S5), the clerk/broker leaking into the Threshold chain (S2). Authored and labelled: the runner, the burned crescents, the factor, the merchant. |
| VOI | 74 | 91 | Her native register is theatre and appetite: execution is hers alone (`b41c2c6c`), bets on lifespans (`f9799f60`), cold contempt (`afa1bd23` "Few are courageous enough, or stupid enough"), torture implements (`d3d9a3e6`), "you'll be weeping and begging for mercy" (`6c27d43e`). Before: the 24-body report block on every ending, first-person ledger lines on her Last Call page, a Last Call read off "the account in your pocket", an acquisition hunt negotiated in counterfoils. After: the runner swallowed by her shadow, the factor's hand, the merchant's hands on the desk, spies flayed on the Harem steps, the servant nailed beside Shamira's answer, jealousy arranged and watched. Edge lint (Nocticula trickster): business 61 / menace 40 -> 18 / 114; acquisition 112 / 9 -> 83 / 27; base 907 / 511 -> 719 / 625. One sexual-frank line per scene kept (no profanity added; her MOUTH target is regal). |
| TRK | 90 | 90 | The Trickster devices are hers and unchanged: the killed shadow and the floor, the brother's voice through the closets, the boot on the shadow, the unnamed favour bought for protection ("I simply ask for it at the worst possible time"), the half-seal with the missing line. The Last Call now plays the shadow device instead of a ledger. |
| INT | 84 | 91 | Native hooks unchanged (Council death/projection, `noct.socoth_plan_exposed` SeenCue, Gift etudes, audience StartedDialog). Fixed: the reveal of unstaged letters/broker in the Threshold chain (S2), the double favour (S3), a reader for each promise and harem result listed in S6. -1 R2 (dead call choice), -1 R4. |
| BEL | 80 | 91 | Costs land in play: the burned crescents, the antechamber among petitioners, the summons-only terms, the leash on the step, the left-handed factor. Reactions: Shamira (every state), Arueshalae, Galfrey, Iomedae, Areelu, Daeran, Nenio. The favour is named once per page, the same chair everywhere. |
| COX | 88 | 92 | No woman is required dead, hostile or closed. Every Shamira state has its own body; readers of Arueshalae, Shamira and Areelu require their current presence (`crossroute.*.available`), so no departed woman reappears (binding context 3). The Areelu line and the Arueshalae rows keep both routes alive side by side. |
| HOW | 86 | 92 | Truth table with notes; every replacement asserts old text and exact hit count, so any upstream change fails the build loudly; appended readers only after existing paragraphs; R2/R3 name the exact gate work. |
| AGY | 70 | 91 | Before, Shamira and Nocticula were names in sentences about accounts. After: Shamira poisons-or-not the yearly glass, bars her doors, nails her answer to them, rules from a new body, comments from inside the skull; Nocticula flays, bets, arranges jealousy, keeps the throne. Arueshalae answers her old queen in her own fallen voice and the queen answers back by name. The pair rows act on their own agendas (Galfrey's sponsorship, Iomedae's six names, Shamira's precedence) and are read on Nocticula's pages as consequences. |

ALIGNMENT LENS (chaotic evil demon lord; creed: her throne, her appetite, her collection): on screen she has her
shadow close over a spy in a crusader camp, takes a factor's collecting hand, leaves a merchant's hands on a clerk's
desk, flays spies on her lover's steps, nails a servant up alive beside a letter, sends a tongue as a reply, bets on a
broker's life and takes her cut when two crusaders are sold. Her attachment to the Commander stays ownership spoken
fondly ("I am not a debt. I am the one who is owed"; "I want my favour paid by someone with a pulse"); exclusivity is a
priced favour she can withdraw, and refusal is logged and collected (the chair kept visibly empty). Nothing redeems or
softens her; no therapy register; the Commander is never her moral authority (Iomedae calls her markets an
abomination and she has the sentence repeated twice, for pleasure).

## 4. Proposals for scenes this row does not own, and inherited proposals

- Shamira review section 5: `precedence.live` letters written (her text, title corrected); the flat Shamira letters on
  the partner-terms pages re-voiced ("Another pet, my lady? ... one day that chair is mine, and I do not share my
  furniture"; "Keep your mortal, my lady. My Harem is mine, and so, one day, is your chair"); the correspondence report
  prose re-voiced (S1, S7). Done.
- Areelu review 6.3: done (S6).
- Vellexia review: `court.vellexia` unchanged, as proposed.
- Horzalah review: a household beat as Nocticula's tenant is still open (needs a new scene; structure). Proposal: in
  Alushinyrra after the war, Horzalah's guild pays Nocticula's rent in an ear; `court.horzalah` unchanged.
- Arueshalae row (4.1): pasted as written; (4.2) `court.arueshalae` retired, no change.

## 5. Explicit slots (Gemory tracker)

Re-checked against the changed text: `noct.acq.epilogue.correspondence.explicit.1` (`last_line` updated to the
re-voiced `morning`; slot_brief_lint on the branch export: Nocticula briefs 0 hard, totals 352/213/189 as on main);
`nocticula.trickster.defeated.chair.explicit.1` and `epilogue.commit.explicit.1-3` (boundaries are the unchanged
`morning_late*`/`after_*` node texts; only paragraphs after them changed). Opportunity recorded, no brief added (J03:
pair rows carry no new nodes): Nocticula + Shamira after the precedence quarrel ("went to bed together afterwards",
correspondence reader) belongs with the existing blocked brief
`explicit_slots/harem/blocked/nocticula_shamira/household.pair.nocticula_shamira.return.explicit.1.json`.

## 6. Validation

Both layers applied to the committed main export (pair module first, as in the build order; then the late layer):
no assertion fails; 130 scenes change (`voice-approvals.proposed.json`, before = main export `text_sha`, after =
branch). On that branch export: `prose_pending_lint --integration` 0 hard (main: 16 hard once the registry is
emptied, until rebuilt); `claude_work_queue_lint` 0 hard; `edge_lint` 0 hard (as main); `payoff_lint` 42 routes 0 hard
(as main); `slot_brief_lint --strict` 213 hard / 189 warnings (main 213 / 189, none Nocticula); `voice_lock_lint` 298
changed (main 236; +62 = this pass, approvals proposed). `py_compile` on both modules. Not run: `python expansion.py`,
savecompat and the unit suites (coordinator's remote build); no id, choice position, gate or flag was changed, and
paragraphs were only appended.

Queue: 119 `nocticula`/`nocticula.acquisition` entries and the 6 `arueshalae` entries in her pair rows removed;
prose-pending: 16 entries removed (registry empty). Nothing left as [PROSE PENDING].

# Konomi — turning-point sheet

Planning only; inspected integration checkout `f2fa495` on `claude/tp-konomi`, the seventeen `storylines/*konomi*.py` modules, exported Konomi scenes in `development/Story.json`, the route spec, writing guide, round-2 REVISION, partner ruling and rubric. No implementation, gates or regeneration. `claude/merge-b10` is not a local ref, so ancestry cannot be independently confirmed.

Finding references below: **P1–P28** = ordered defects in `konomip1.json`; **F1–F33** = ordered defects in `konomif1.json`. These are a union, checked against current source/export; spec notes claiming completion are not implementation evidence.

## Canon anchors (verified directly in /wrath/blueprints.zip and enGB.json)

- **C1, office:** `Diplomacy_2/Cue_0008`, blueprint `9ee914535aa169240b3a840465a43d55`, enGB `632d08ce-1c4f-4eb0-a056-ea4599f49ecd`: kitsune attaché, Galfrey's credentials, leadership of the Diplomatic Council; first native introduction is in Drezen, Chapter 3.
- **C2, price:** `Diplomacy_4/Cue_0034`, `4652e02184bd4494e8680a466714bbd5`, enGB `72094ade-5fb1-4ef2-99b4-b6c70338b5cc`: predatory bargaining and supply leverage; a political concession cannot purchase her desire.
- **C3, Crown:** `Diplomacy_3/Cue_0061`, `f363c2703c8c3934f84da229cf4d9710`, enGB `5f4d30ef-4332-4c5d-ab63-3df3061a8bf8`: decisions belong to Nerosyan; retain her political allegiance and silken condescension.
- **C4, dismissal:** Chapter-5 `Diplomacy_6/Answer_0070`, `73c5728c4c6658344bedcc1b666e598c`, enGB `05aec835-7770-48e7-83bc-cf3cbfc4a9d6`; its next cue is `Cue_0075`, `384cd66452a61324cb484c661cd9573d`, enGB `73f3ed79-f08c-477b-901f-6e76e9faf139`: she leaves for urgently needed negotiation in Nerosyan.
- **C5, kitsune:** `Diplomacy_Officer/Cue_0038`, `efe7fee421301b84aaff22a3b9dba4cf`, enGB `d21d2901-e480-476d-aafa-ad1eb048c0d7`: passionate, curious people living unnoticed everywhere; this cue has a non-kitsune Commander condition, so do not manufacture its SeenCue for every Commander.
- **C6, crisis:** `Diplomacy_Officer/Cue_0032`, `07459f4d09fa81e4b99beea351fb0434`, enGB `61406e3b-e2a0-426a-bd0f-95ffac91b96d`: divided rulers, unsafe roads, failed services and famine; use these pressures, not a new civic subplot.
- **C7, Trickster root:** `Kyado_main_dialogue/Cue_0109`, `509eac8248670664fab0808c3e00fe04`, enGB `8e8ca1ec-d907-4101-8f60-b59af4125e6b`, guarded by Trickster etude `9f486a9c0c9abfc4a952bb22e88a7e96`; path flavour, not permission to make a spoken joke compel affection.
- **C8, physical host:** Drezen `2570015799edf594daf2f076f2f975d8`; `RankUpOfficer_Diplomacy` unit `ca2d58c5c65723945857e04fb85d30ce`; office etude `b5f301fbc4c44535a6309d610d5bd28a`; `Diplomacy_Officer/AnswersList_0003` `0dc8b8604bb33c846a63f3eb62443674`. Existing physical scenes use this actor/hub, not a newly invented embassy.

All road, informer, private lodging, rite, correspondence and postwar-house details are **authored additions**, not native facts. Their reasons are C1–C8; native death, dismissal and office state still stand outside the applicable Trickster alteration. No canon spouse/lover is established for Konomi: no partner-stance subplot is owed or proposed.

## 1. Implemented entry → build-up → turning point → payoff

- **Office:** `margin` (live office/contact, Ch3/5) → `reception` → `letter` → `evening` (successive 24h waits): she invites, declares interest, names personal articles and initiates intimacy; official-only/refusal closes. `disagreement` → `leak` → `reckoning` → `return` + `political_account` → **`power/limits` and `commit`** earn commitment by preserving disagreement; `ordinary`/expanded evenings and public/private/changed/ascended endings collect that history.
- **Dismissed:** C4 + live Trickster + completed office + dismissal latch → `dismissed.late` after 72h; 150 Finances buys driver/minute, but `gate` immediately sets road-return → `recess` → `terms` after 48h (500-Finances endorsement or personal favour; refusal closes) → supper at 24h for an uncourted woman → **`private` at 72h**, her stay/letters/chair decision. Prior lovers or `supper_asked` unlock the romantic ask; envoy is professional; privacy refusal sets `declined`.
- **Dismissal retry/payoff:** `a_season` waits 168h after the refusal, asks for a public council refusal, commits and reaches heat without collecting privacy; `epilogue.refused` has only Continue. `late_committed` wrongly derives from settled terms + old lovers even after envoy; earned romance should lead to her postwar dispatch, envoy to triplicate reports, refusal to unresolved negotiation, closure to separation.
- **Never appointed:** observed missed contact + latch + live Trickster → `accredited` after 96h; paid informer (100 Finances) or rope threat dispatches report, but `clerk` immediately sets arrival → physical `audience` or zero-delay failed-placement letter → `rooms` after 72h, account/supper → **same-night `stay/accept/morning`** sets `rooms_kept` and lovers. Business sets envoy; postponement aborts; late commitment currently derives from rooms alone.
- **Registered private/distance continuation:** existing invitation/reply → `private_meeting`/`private_history` or `the_courtyard_introduction` → carriers → `before_road` (she admits attraction/returns a kiss) → `private_departure` → letters 336h + offer 168h + reunion 336h → career choice 48h → **`chosen_evening` 48h + `private_future_choice` 24h**. Her yes, open courtship or parting determines distance endings; office/death/invalidated-contact/inhuman/farewell gates remain legitimate.
- **Death:** observed retained death + live Trickster → `dead.recalled`: rider 300, rite 500, fee 300 Finances; her soul refuses then accepts a prepaid consultation, verified revive sets confirmed → physical `dead.consultation` after 12h → ordinary office courtship. Resurrection itself earns no romance; failed/unattempted return gives loss, and unreturned Commander sacrifice gives grief, not a living future.
- **Legacy continuations:** retired `fate_post`, `retained_inquiry`, `the_unintroduced_letter` entries forbid `trickster.ever`; their answer destinations, map aftercare and already-started replies survive. Preserve them for saves; do not revive these devices as new entry roads.

## 2. Her decision at every romantic advance

- **Invitation/interest:** `margin/answer,invitation`, `reception/interest,slow`, optional `a_turn_for_herself/finish`: she sets the time, says she is interested and asks for further company; slow interest remains open without promising intimacy. Keep her separate pleasure/dance invitation, not a Commander reward.
- **Terms/first kiss/night:** `letter/alone,terms` names articles; `evening/kiss` visibly answers the kiss, `stay` says yes and undresses, `quiet` asks another evening, `changed` chooses a different form of closeness. These already show desire; do not add attraction scores or a sexual requirement for quiet/changed branches.
- **Exposure/trust/commitment:** `leak/lie` says no to denial; public/discreet replies are hers; `reckoning/repair,repaired` and hearing continuations address the lie/apology. `power/limits,commit,part` offers continued political opposition and answers commitment/refusal; preserve these decisions through private-history copies.
- **Dismissed pursuit:** `supper/glad,you` expresses curiosity; `private/answer,courted,wants` owns the stay and counter-demands. Proposed beat: make the sealed-letter condition audible and accepted on every romantic exit, including the direct hand choice; her fan closes, she chooses the intimate reach, and envoy/no remain real outcomes.
- **Retry:** `a_season/start` already owns shortening the season; proposed `price` repeats privacy **and** council refusal, followed by her yes/no and the existing public repayment. Postwar retry must let her answer again; unresolved negotiation is not an automatic romantic yes.
- **Accredited romance:** `audience/received,journey` chooses whether to answer a personal letter; `rooms/terms` offers suppers, but first-supper reserve is bypassed. Proposed first-supper close: she names a second supper; 48h later she explicitly chooses another evening, business only, or postponement, then initiates heat and owns it in the morning; only that romantic acceptance earns rooms-based late commitment.
- **Private return/distance:** invitation, `before_road/new,lovers,kiss`, `private_reunion/visit,want,kiss`, `chosen_evening/close,morning`, `private_future_choice/commit,open,part` all contain her own invitation/attraction/answer. Retain office-dismissed versus never-appointed wording and existing room for other relationships; neither career success nor fare payment becomes a romantic switch.
- **Later intimacy/postwar offer:** `hearing_after`, `new_letter`, `the_trial_day`, `the_evening_she_kept`, political-reply kiss, `private_kept_hours` and `private_last_visit` show reciprocal touch or her invitation. `epilogue.commit/offer` is her pursuit, not a substitute for prior agreement; retain signed/terms/dinner outcomes, correcting location and response as below.
- **Return from death:** `dead.recalled/refusal,fee` is consent to living/consulting, not a lover's yes; consultation and legacy first/second visits must honour known/unmet/lover history. No fee, rite or Shyka page may stand in for the romantic decisions above.

## 3. Stated debts → collection in every payoff

- **Privacy, chair, private dismissal** (P7; F17): direct hand acceptance and retry currently bypass the fully stated seal demand. Rewrite those existing terms/acceptances to include it; append any necessary replacement answers, retire bypass answers by gating, retain destinations; romance payoffs read actual acceptance, envoy buys no bedroom access.
- **Public refusal** (F17–19): retry promises this and stages it in `council`, but privacy remains unpaid. Retain the council beat and both demands; postwar earned retry shows the analogous refusal before its settled retrospective, with no epilogue Set flags.
- **Road/political bill** (P5–6; F6–7): 150 buys the driver, 500 buys a provision reserve against disputed deliveries plus the endorsement, not a simulated season embargo. Rewrite `paid`, `paid_envoy` and supper callbacks to that same receipt; favour is the existing alternative, not an additional charge.
- **Jug account** (P14): audience 200 + remainder 50 = 250, whereas deferred payment is 150; negotiated totals also differ (225 versus 100). Reprice deferred totals to 250 and 225 respectively, retaining credited 50/25 and audience 200; same obligations, no invented surcharge or extra debt.
- **First-supper reserve** (F9): “only paid for the journey” currently converges on sex. Collect curiosity with a second invitation and her later personal answer, not another invoice; preserve postponement and business exits.
- **Unnamed favour/paid consultation** (P15–18; F24–27): Last Call's Continue resolves without terms, then its coda accepts a political seat for the Commander. Paid endorsement and prepaid consultation get acknowledgments; only an outstanding favour gets her named proposal, player acceptance/counteroffer/carry-forward and her answer.
- **Ordinary honesty/time/articles:** `letter` requires kept promises and deliberate evenings, `leak` rejects disowning her letter, `reckoning`/`private_history` record apology and surviving complaint; `before_road`/future terms require notice of journeys. Keep existing repayment scenes and their history in copies/endings; do not add new reconciliation conditions or claim hearings settled before their recorded outcome.
- **Dead-state silence/fee** (F33): her people's anonymity and prepaid fee are already paid before return; `ending_lost` invents consultation debt for every committed death. Use an actual unpaid-obligation variant only where produced; otherwise recall their earned private letters/evening, and never invoice an ordinary lover for an unchosen recall.

## 4. Convenient devices / unearned payoffs → concrete replacements

- **Instant road return/delayed interception** (P1–2,24–25; F1–3): toolbox = benevolent arranged opportunity, then her counter-move. Label the lower-town Crown-escort delay authored (C4/C6); offer intervention immediately, stamp `road_sent` at the 150-Finances payment, wait 48h, put gate receipt in the physical recess and let her choose to stay to collect. Reframe the driver detour as an offer she can reject at the fork, not forced detention; she takes it to examine the Commander's scheme.
- **Instant accreditation / coerced informer** (P3,26; F4): toolbox = cover for her through an existing letter event (C1/C3/C5/C8). Keep paid report as a harmless invitation/protocol nudge; report makes her curious, not obliged; stamp `report_sent`, wait 96h after dispatch for actual arrival. Retire rope-threat entry for new histories by gating, preserving its choices/nodes and legacy burned-state reaction; no new blackmail layer.
- **Failed-placement substitute** (P4; F5): toolbox = one letter twin only when the physical meeting fails (C8). It opens ≥96h after the physical-eligibility receipt, forbids completed physical twin, and a shared completion receipt prevents duplicates on later placement recovery; letter delivery alone never creates a physical actor.
- **Grain embargo** (P5–6; F6–7): toolbox = her canon bargaining counter-move, already in `terms` (C2/C6), with the existing 500-Finances reserve receipt. No new supply mechanic, seasonal gate or economic redesign.
- **Retrospective citywide humiliation** (F8): quoted “clerical error” claim is absent from current source/export: **no change needed**. Do not add a clerk humiliation event just to repair removed prose; if such a callback returns during later work, replace it with a brief witnessed registration objection inside the existing audience and her credentialed rebuttal (C1/C3), never a citywide invented slight.
- **Payment → same-night lover** (F9): toolbox = she pursues across two suppers at the already authored office/rooms (C2/C5/C8). First encounter earns another invitation; one new second-supper event 48h later holds her personal decision/heat/morning, without new attraction or commitment prerequisites.
- **Privacy substitution / missing retry** (P7; F17–19): toolbox = her pursuit/test at the existing council (C3/C4/C8), preserving the original seal demand. Shorten `a_season` to 72h; append a postwar ask to soft-refusal epilogue with her answer and open-negotiation alternative, requiring earned settled return + personal supper or prior lovers + privacy refusal, forbidding closed/envoy/loss/unreturned sacrifice.
- **Unseen Last Call negotiation/automatic political concession** (P15–18; F24–27): toolbox = a planted sealed packet at the original bargain, opened through the existing Threshold call. She anticipates the final march and provides account-specific instructions; an outstanding favour proposes the existing Nerosyan-seat price, counteroffer narrows it to diplomatic councils, carry-forward leaves the favour owed; she counters or accepts on-page. No immediate long-distance conversation or unsolicited official concealment (C2/C3/C6).
- **Contradictory debt retrospectives** (P17; F27): ending paragraph “unnamed for years” must forbid named/settled collection outcomes. Supply accepted/countered/carried/paid variants in epilogues only; sweep all seventeen listed nodes: public, private, changed, ascended, distance, distance_open; distance_lived and distance_open_lived both exclusive/portfolio; late commit signed/terms/dinner; envoy; refused; public_buried.
- **Capital teleport / romantic exceptionalism** (P19–20; F15–16): toolbox = her postwar personal letter (C3/C4/C5). Establish that she writes after returning to her house in Nerosyan, courier travelling to Drezen; personal answer is at that house, not a Nerosyan embassy in its own capital; replace lifetime-first laughter with the present staff's concrete surprised reaction. Give the terms-return its actual travel interval too.
- **Overlong distance/late clocks** (P21–24; F18,20–22): native chapter pressure C4/C6, not a new mechanic. Distance delays 120 + 72 + 96 + 48 + 48 + 24 = **408h ≤504h**; dismissed first yes 0 + 48 + 48 + 72 = **168h**, supper fits inside the final 72h; a subsequent 72h retry requires the specified postwar option if the late window has elapsed.
- **Accredited timing limit:** repaired dispatch 96h + existing rooms 72h + second supper 48h = **216h** before its romantic answer. Earlier Chapter-3/5 entry remains feasible; do not assert a fresh post-Coronation yes inside 168h or silently shorten another wait/add a bypass. Coordinator must reconcile that late-phase budget if this entry is required there.
- **Envoy/dead/dismissed/departed romance leaks** (P8–12; F30–32): restore earned-presence discipline, not a new romance device. Withhold late-commit/romantic coda for envoy; household entry requires living persisted lifecycle, earned road return/agreement after dismissal, and reunion after private departure; no old lovers or rooms receipt overrides current absence. Shared derivations/household consumers are ESCALATE.
- **Closed yet “still negotiating”** (P13): forbid `closed` on refused epilogue; keep genuine soft refusal open, and retain mixed-history breakup ending. No new reconciliation path.
- **Wrong Dorgelinda callback** (F28–29): read producer outcomes, never broad `primed`; both successful/outfoxed nodes distinguish `dorgelinda.trickster.cost.audit` without `cost.abyss_signed`/`cost.tribunal_books` (tribunal warehouse), `cost.abyss_signed` (Abyss stocktake), and `cost.tribunal_books` (later review). Her own route is read-only; missing verified outcome producers would be escalated, not invented.
- **False Guidance** (P27–28; F23): describe paid carriage intervention, report and earned audience, failed-placement correspondence and the 12h physical consultation; keep historical letter/map directions only for still-available continuations. No promise that taking a page or waiting before dispatch creates a return.

## 5. Proposed uniqueness entry (coordinator to register; no registry edit here)

- **Device class:** `envoy_pursues_after_closed_political_account` — her seal remains hers; she separates the political settlement from her personal invitation and can refuse either Commander proposal.
- **Setting:** `Drezen_attaché_office_after_dismissal_recess` — council minute and paid charcoal-road setup, fan on the closed ledger, watch changing below the window; accredited entry expresses the same woman through a later supper, not a second competing device.
- **Payoff shape:** `sealed_private_correspondence_with_public_political_dissent` — intimate pursuit/cut/morning, followed by her actual council refusal and useful Crown reports; postwar she sends the personal proposal herself, with signed/counterterms/continuing-dinner outcomes retained.
- **Why hers / uniqueness:** C1–C5 make her a curious kitsune diplomat who can want the Commander while advancing Nerosyan's interests. Compared against `06-ROUTE-REGISTRY.md`: no pardon-pride (Nurah), council vote purchase (Eritrice), confession (Anevia) or generic debt-to-kiss device; reserve this exact class + setting and payoff shape. `turning_points.json` is absent in this checkout; collision validation against other pending sheets remains coordinator work, not a claimed lint pass.

## 6. Heat / VOI audit fixes and sibling sweep

- **F10–12:** both male-address lectures and active-office replacement argument are already absent; private opener uses independent correspondence: **no change needed**. Preserve these fixes across `pages(private)` and missed-contact copies; the official `start` still contains authorial “ceased to have political opinions” (F13): replace with the concrete recommendation, recipient and crisis consequence (C3/C6).
- **P6, F14:** supper still asks what she is “paid” after closing the political account: turn it into her pointed personal curiosity. Audited intimate “see what it costs you” is already absent: keep current `threshold`'s physical appetite, bare skin, wrists and breath, cutting before explicit acts; do not reduce heat or reintroduce accounting there.
- **P18,20; F15,26:** keep official reports useful to Nerosyan and private letters sealed; remove lifetime-first laughter. Neither love nor a paid favour reforms her predatory political methods into unconditional loyalty to the Commander.
- **Threshold class:** preserve `evening/stay`, `dismissed.private/threshold`, retry `yes`, rooms/second-supper threshold, `chosen_evening/night`, `the_evening_she_kept/night` and farewell intimacy: open desire up to the cut, her active reach, concrete morning consequence; no HR choreography, maxims, editorial narrator, compulsory sex or premature fade.
- **Foresight/echo:** Konomi has no allocated slot in the registry's Echo slots table. Existing `private_absence` page-gated memory/waiting imagery must not justify her choices or supply knowledge of her present life; use ordinary remembered letters/address and her actual reunion answer, retiring any unallocated echo by gating. Shyka's page stays fate-only if an already authorised return needs it; no new page gate, vision explanation or echo is proposed.

## 7. Ordered implementation checklist (future work, not executed)

1. Capture scene/node IDs, relationship IDs, every choice index/destination/Set/Abort/Return behaviour and file newline style; preserve CRLF where present. New choices append; obsolete entrances are gated; retain all old nodes/answers, including legacy ending Continue exits with their original identity **and mechanics**.
2. Implement route-local road/report dispatch receipts and physical payoff variants; keep legacy in-flight continuations; obtain coordinator changes for shared presence timing/derivations before claiming delayed arrival works. No expansion regeneration in this planning job.
3. Repair chronology openers and eligible/failure-letter clocks; append harmless informer entry if needed and gate new rope-threat access. Preserve native dismissal outside Trickster and show her road/report counter-moves rather than automatic affection.
4. Align all account totals/callbacks and existing Finances debits; collect the seal/chair/door debt on every romantic branch and both retry demands; retain business/refusal. Add only the audit-required second supper and postwar retry, keeping the former's 48h wait and latter's flag-free epilogue exits.
5. Apply 120/72/96h distance and 72h retry timing; update Guidance from actual available scenes. Check whole chains, including late/uncourted entry and fallback, against phase budget rather than checking isolated nodes.
6. Coordinate shared late-commit, household eligibility, Last Call packet/negotiation and coda collection fixes; only route-owned entries in shared files may be edited under a future explicit allowlist. Record outcomes in `konomi.lastcall.*`; do not set epilogue state or settle an outstanding favour on an unnegotiated Continue.
7. Rewrite only remaining VOI/BEL defects; repair every unnamed-favour paragraph, lost-debt variant, Dorgelinda callback and postwar location. Already-absent audit quotes stay fixed; do not restore their surrounding obsolete prose just to re-fix it.
8. Future acceptance cases: dispatch t=0/47/48 and t=0/95/96 + reload; physical success/failure/recovery without duplicate letter; cumulative full/credited/haggled accounts; both privacy refusals and accepted retries; former lover → dismissal → envoy; death → unload → verified restore → later death; dismissed without return; accredited departure before/after reunion; mixed-history closed refusal; paid endorsement/prepaid fee/unpaid favour accepted/countered/carried; ordinary committed death without recall; unreturned Commander sacrifice; non-Trickster unchanged native outcomes.
9. Coordinator registers uniqueness and authorises implementation scope, resolves shared ESCALATE items, then performs the normal implementation verification/independent audit. All pages must retain selectable exits in relevant histories; conditional paragraphs belong only on epilogue pages. This sheet asserts no score or gate pass.

## ESCALATE / limits

- Shared `trickster_world.py` late-commit/presence/household derivations and lifecycle consumers; shared `household.py`/Guest List; `lastcall*.py` account branches and coda; relationship Guidance aggregation or runtime clocks if not exposed route-locally. These files are outside this task's write scope: no edits attempted.
- Register the section-5 proposal in `tools/route_packs/turning_points.json` after comparing pending sheets; the exact single-file task forbids editing it here. Konomi's unallocated foresight echo needs registry/coordinator resolution; do not allocate a slot silently.
- Deliberate player killing/user-ruled closure is legitimate (rubric contexts 1–2): do not add a rescue obligation or change the existing death eligibility/one-raise ruling. All living outcomes require an earned return and living Commander (contexts 3–5); gates may rightly block yes. Any native dependent-content rewrite is Trickster-only, authored, proportionate and save-compatible under the DLC rule.
- No extra mechanics, gates, costs, commitment scores, reconciliation conditions, partner subplot or dark Commander scheme proposed. Audit repairs above remain proposals until separately implemented; no score ≥91 is self-certified.

## Round 3 implementation: audit-required situations

Authored additions in `storylines/konomi_round3.py` retain all existing journeys,
payment effects, choices and returns. The paid endorsement/reserve breakfast and
the personal-favour breakfast now differ; the latter reports her own assessment
and keeps the favour outstanding. The Bluff check concerns the Commander's
expectation of refusal, not the paid driver's already disclosed involvement.
Failure exposes the pretence but adds no political price. Only the accepted envoy
offer earns appointment gossip. Every copied register coda preserves the original
entry beside her signed correction; the annual mistake comes from an auditor
copying the first line alone. Ordinary ending paragraphs record collection only
after the existing Last Call terms acceptance; countered or refused terms leave
the favour outstanding.

Authored physical delivery: Anevia's existing Drezen briefing contact hands over
the gate/chancery receipts and hosts the road and council-chair invitation setups. This
uses `AneviaTirabade_DrezenCapital` (`b5e867e13503c6f41bb1316705efb4a2`) and
`NPC_Common/Anevia/AnswersList_0003` (`33960c7f7af40cd43b7f801a76c87a0b`), checked
in `/wrath/blueprints.zip`. It does not assume Konomi's actor is already visible.
The road receipt remains 48h after payment and the accredited receipt 96h after
dispatch. Recovery retains the runtime-required Remote delivery. Recovery plus
dismissal consumes one Chapter-5 delivery; accredited contact plus the
failed-presence letter and a later recovery consumes two Chapter-3 deliveries.
No canon return applies
off Trickster, and no new recovery or affection condition was added.

All eight existing explicit slots and briefs now continue their established
position, with the rival's dispatch already put away at the second supper. They
retain the existing cut and aftermath, without replaying undressing or movement.
The slot briefs remain for later generation; no explicit prose was generated.

Shared integration still requires coordinator work: paid-account Last Call
assistance, distinct ledger dispositions including a prepaid consultation receipt,
and the useful-Crown-report Last Call opener. This pass leaves `lastcall*.py` and
shared derivations untouched. The existing accepted/countered/refused Last Call
choices were verified against the merged implementation. Scores require the
independent auditor; this note claims no rubric score.

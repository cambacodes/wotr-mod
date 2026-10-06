## Round-2 implementation precedence

The implemented device is the atlas's **bargain** at the existing Drezen market appointment / leased mental room. The distinctive payoff is TRIAGE JER-05: she retains her collection, could leave alone, comes back for the Commander, and loses the hiding place. The older pursuit classification and memory-retelling payoff below are superseded by the set-piece sheet and registry. Memory retelling remains the existing forfeit consequence.

Authored additions live in `storylines/jerribeth_round2.py`; they create no new attraction, commitment, revival, reconciliation, or resource requirement. Explicit prose is reserved for the nine supplied briefs and heated-cut nodes. Shared Last Call text and the atlas registry are coordinator-owned residuals.

# Jerribeth — turning-point sheet (planning only)

Baseline: `claude/tp-jerribeth`, HEAD = `origin/claude/merge-b10` = `f2fa495a5ca63cf52298d347b98d992bb5e2c078`. Read all seven `storylines/jerribeth*.py` modules and her exported `development/Story.json` scenes, including `jerribeth.lastcall.page`.
Evidence labels `P1:n` / `F1:n` refer to the numbered defects in `/work/Writer/judging/codex/jerribethp1.json` / `jerribethf1.json`; this sheet covers their union, including fixes already present. No implementation, export, gate, or registry mutation is authorized here.

## Canon anchors (verified directly in the game data)

Blueprint paths below are relative to `World/Dialogs/` in `/wrath/blueprints.zip`; localization keys are from `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`. All proposed dialogue beats are **authored additions**, not claims that these events already occur in canon.

| Anchor | Blueprint GUID; enGB key | In-game reason |
|---|---|---|
| A — telepathic greeting | `c3/IvorySanctum/JerribethGreetings/Cue_0001`, `8a632a5249b3c2541a1381111cae9e37`; `285126f8-f314-4a8f-a477-38282da07ef3` | Her voice reaches the Commander's head; hands and antennae carry her reactions. |
| B — Wintersun illusion | `c3/Wintersun/JerribethReveal/Cue_0008`, `063d159af56b4c54292e6e2eaca8ca08`; `0b920731-f11b-4985-a147-2f5f60942ae6` | She plants ideas and reverses villagers' perception of demons and mortals. |
| C — existing lover | `JerribethReveal/Cue_0014`, `52ada8be40232dc4eaccb8b1c3d79f55`; `b003e047-ab44-4a8b-af47-b50108d50484` | Marhevok's passionate, blind devotion interests her; the village remains her toy. |
| D — portable captive | `JerribethGreetings/Cue_0004_NewMarh`, `d905736155d86ca4ea4f4ab463903082`; shared string `01dcca8f-8c3b-4039-84a2-ed08fcbc136b` | She transformed him to keep him forever and potentially take him to the Abyss. |
| E — plant / chief | `c3/IvorySanctum/MarhevokTransformed/Cue_0001`, `410114edfb51a9b44961a482d3e52cbd`; `6edde3ab-46b5-494b-aadd-1f225638587b`; `JerribethReveal/Cue_0044`, `7b9443fc261d217468e1c6b132fce4c8`; `6bf14d04-49a6-46f1-aec7-a417304b58ce` | Plant has human eyes, no dialogue; judged chief bids her farewell to make amends to his people. |
| F — oolioddroo lore | `JerribethGreetings/Cue_0045`, `93dfa9597191a6848b925d964d309fe4`; `502d4969-be68-4f36-b656-84d163f8aa4f` | Nenio describes eggs influencing a sleeping host's thoughts; a seed preserving its mother is an authored extension. |
| G — appetite / independence | `JerribetnFinal/Cue_0001`, `bf1542830cfa01d4c9db04546681084d`; `eb28ad3b-053d-4e46-9db2-055fd0a1b1d2`; `JerribethGreetings/Cue_0031`, `7c5e45ae9f8a9034b805707899433e53`; `ab61b2ee-bbaa-418d-9084-e5f241658eba` | She pins Xanthir's locusts with fascination and serves Baphomet only while profitable. |
| H — Act 4 patronage / counter-move | `c4/RaptureOfRupture/Jerribeth_Velexia/Cue_0011`, `edeeb17ba4f3d124890d22bdd2d8901d`; `d718c8dc-09e7-4ed0-b84d-a7a7815f5604`; `Velexia_Third_Date/Cue_0055`, `e0ee422a413a5f94ea90bede3096ee56`; `ecc42853-d2e6-4613-95c2-de90a01dbfd5` | Vellexia protects her as servant/companion; Jerribeth independently chooses the Commander's side before the fight. |
| I — native toast | `c3/Mythic_Trickster/FoolKing_Tavern/Cue_0052`, `c31225c91534ccf4992870646b7f8f60`; `88ad9599-95ca-4076-ab7f-3c7dc2176503` | Thaberdine orders a toast; existing Ch5 hook is `AnswersList_0054` `6dccfd39947ef4242a8afbe36b21a46c`, returning to `Cue_0065` `7b050ba0745bf144e815632e39b34853`. |
| J — Trickster property theme | `Mythic/Trickster/KnowledgeArcana/TricksterKnowledgeArcanaTier3Feature` `5e26c673173e423881e318d2f0ae84f0`; `08c5494d-9441-45a1-a757-cae129446016` | Impossible item properties justify the existing lease's theme; they do not canonically establish resurrection or attraction. |

Native fate reads: `jerribeth.marhevok_dead` → `Marhevok_Dead` `fc03aa45c96a1424680c505627db8144`; `jerribeth.marhevok_in_sanctum` → `Marhevok_InSunctum` `4f87458c1e0d21c47b9269cd9dc727be`; `gesmerha.marhevok_rules` → `baa4820ac052d664bbaa261d17ce9b08` (native fact, not Gesmerha romance eligibility). Death takes precedence; returned Jerribeth does not transport or revive the plant.

## 1. Entry → build-up → turning point → payoff today

- **Living entry:** native meeting (`jerribeth.met`) or earned toast (`met_by_toast`) opens `invitation`; opening/returning the frame is a player choice, rejection closes her. An unread chosen `fate_letter` temporarily precedes the invitation, rather than awarding affection.
- **Dead entry:** greeting/final lease primers → `primed`, advance memory loss → death → `dead.tenant` / `_nexus` after 48h and current Trickster power → chosen vessel, cost, `returned`. `dead.backdated` signs a late lease now; decline blocks return; the death etude remains set.
- **Never-met entry:** Ch5 live Trickster + King available → physical `toast_king`; otherwise levy-rest `.toast`. Neither opens for met/dead Jerribeth; she chooses to pursue the invitation, which then demands a host, the toast memory, or an outstanding grudge.
- **Build-up:** `invitation` → `question` / `question_late` (`attracted`) → `guise` (`courting`) → `price` (accept terms or close) → `evening` (`lovers` or slow company) → `commission`. Xanthir discussion folds into `price` when already known; patron/refuge need her own native refuge evidence.
- **Turning point today:** Ch5 `future` needs `commission` plus `settlement_kept` or `short_future_requested`; Trickster `commission/keep` produces the latter. She names a memory forfeit, refuses a blank promise, collects unpaid toast interest, settles partner stance, and accepts or rejects continuation.
- **Immediate payoff:** accepted living contract sets `committed`, `cost.forfeit`, `visit_due` → 12h Drezen physical visit; returned tenant instead builds the mental room in `future`. Slow/refusal paths keep their own outcomes; the failed-presence letter currently consumes `visited` without delivering intimacy.
- **Later payoff:** ordinary/farewell or late-entry folds → together/ascended/apart/sacrifice endings; unfinished `commission` can qualify for the first-spring late offer. Late acceptance has intimacy and next-year memory collection, refusal retains the war; Last Call currently contradicts acceptance.
- **Long correspondence:** `offered_signature` starts the purchaser/counterfeit/settlement chain only off fresh Trickster entry; existing histories may continue. Preserve that gate and the Ch3 eight-core-letter / Ch4 three-letter pacing; do not insert a new sidequest to make romance work.

## 2. Her on-page decision at each romantic step

- **Opening:** `invitation/why, return` already says why she wants this company and asks for another evening; tenant/toast variants retain her pursuit. Accepting the access device never means accepting courtship.
- **Attraction / guise:** `question/answer,next` chooses whether to reveal herself; `guise/guise,true,end` chooses which form to show and another invitation. Retain the player's preference without treating a costume selection as her romantic yes.
- **Terms / first private evening:** `price/refuse,limit,terms` is her costly concession without repentance; `evening/waiting,private_guise,late` owns her desire and staying. Add Marhevok disclosure here and in `price`, ahead of `lovers`, using C–E; do not add an attraction threshold.
- **Tenant evening:** `tenant_evening` owns her changed situation, but the other-lovers answer skips it; route both attention answers through the same vessel/late-lease ladder before `want`. Variant the opening voice by form, not a universal charm explanation. [F1:14]
- **Commission / commitment:** she makes the horizon for this audience, then in `her_terms[_short]`, `blank`, `grudge[_short]`, `promise` / `short_future` chooses the offered future. Strengthen her acceptance into pursuit: she chooses the visit/mental room herself after payment; her no remains final. [P1:1]
- **Partner stance:** existing `jerribeth_partner.py` dramatizes share/secret/exclusive demand, her refusal, chief's letter and plant's reactions; retain her choices. Earlier disclosure and refuge whereabouts remain missing; do not add pruning, rescue, or forced breakup. [P1:12–17; F1:1]
- **Physical / mental threshold:** `visit/arrival_terms,ask` and `future/tenant_room,tenant_body` show appetite, but offer only two ways to proceed. Append a pause/stop answer with her irritated withdrawal, no punishment or new gate; accepting the contract does not compel the night.
- **Scale morning:** `morning_free` says she will enjoy the decision but provides none; append keep/return with her possessive response and the already-stated price's receipt/collection. Do not make either outcome a commitment test. [P1:4; F1:8]
- **Correspondence intimacy:** `unsold_evening/near,kiss`, `counterfeit_after/attention,desire`, `room_measure/private,desire` already invite desire or quiet; add her initiating action in the shared imagining, cut at the act, and a specific aftermath without turning the charm into a portal. [F1:15–17]
- **Renewal / farewell / separation:** `promise_revisited/chosen,held,close`, `old_promise/keep`, `farewell/return`, `parting/end,stay` contain her distinct answers; keep shorter promises valid and no free reconciliation. Restore player control over the embedded restriction in `promise_revisited/chosen`. [F1:35]
- **Late commitment:** `offer` → `signed[_mind]` / `torn[_mind]` contains her acceptance/refusal, but missing toast collection must precede signing. Partner terms/discovery must use ending-local branches, not new persistent epilogue flags; intimacy stays separately selectable. [P1:1,17; F1:1,12]

## 3. Narrative debts and exact collection fixes

- **Lease:** advance childhood-door memory, monthly memory rent, vessel costs and Nexus host promise are already paid/narrated and carried in endings/Last Call. Keep rent exclusive to tenant histories; do not invent additional costs or a recurring scheduler. [P1:5; F1:11]
- **Toast:** host and toast-memory payments already have separate receipts; refused payment creates `cost.toast_grudge`. Campaign `grudge[_short]` collects interest, late `offer` does not: append unpaid-grudge demand → pay/collect → signing, or refuse → unsigned future; use `cost.toast_interest` only for campaign history, no epilogue `Set`. [P1:1]
- **Toast recollection:** collecting older toasts does not erase the retained encounter. In both `interest` and `interest_short`, select King/deserter/tavern versus levy/sergeant/rest; if `cost.toast_memory` erased that night, never reconstruct its image as a remembered scene. [F1:13]
- **Forfeit:** naming it sets `forfeit_named`; accepting sets `cost.forfeit`. Preserve that distinction and the existing single campaign collector (Last Call when active, ordinary ending otherwise); late signing collects its war-memory forfeit only in its accepted branch, without accidentally invoking a second campaign receipt.
- **Promised visit:** `visit_letter` is notice, not completion. Append a route-local deferred-notice receipt, keep actual `visited` on the completed encounter, permit the existing presence to retry, and move fallback to ≥108h from the same appointment (12h physical + ≥96h separation). [P1:2–3; F1:4–7]
- **Scale loan:** append keep/return receipts; returning ends the loan, keeping preserves the stated hour debt. Collect due time in the next existing ordinary/late-fold conversation, acknowledge pending collection in endings if never reached, and narrow the repeated-night tariff to that single existing obligation; no scheduler or new romance requirement. [P1:4; F1:8]
- **Terms / other lives:** no intrusion into others through the charm, private evenings not sold, Marhevok acknowledged, chosen secrecy has fallout. Preserve the purchaser/Serit exchange, fees and report/catalogue consequences where that chain already exists; payment is never proof of affection. [P1:12–23; F1:1]
- **Survival / future:** `ending_unfinished` still permits living invitations after unreturned sacrifice; add `sacrifice` exclusion with existing `trickster.commander_back` override, matching other living endings. Do not invent a new rescue or force a death-specific romance ending. [P1:7]

## 4. Convenient devices / unearned payoffs — replacements by class

- **Price bypass → she pursues, but collects:** use the existing spring breakfast and `offer` (G/I), not a magical waiver or a second quest. She opens the grudge account before offering her hand and withdraws the contract on refusal. [P1:1]
- **Failed spawn becomes encounter → existing small letter + her counter-move:** one delayed notice explains the native city's priests/guards obstructing her approach; she chooses a later attempt through the existing Drezen presence (`2570015799edf594daf2f076f2f975d8`, unit `417ce3dcf3a9707488f2b9b2a790814b`). No new location, witness, or automatic completion. [P1:2–3; F1:4–6]
- **Invented witness / stale night → companion reaction:** Woljif's own hub `e41585da330233143b34ef64d7d62d69` requires completed physical visit and his present-now state; change entry and dialogue to “that visit” instead of “last night.” He warns about the memory bargain from his own experience, never approves for her. [P1:3; F1:6–7]
- **Decorative loan → her pursuit with a collected consequence:** the scale comes from her wing in the existing `threshold_free` (G), so her keep/return decision and owed hour belong in its morning and next already-earned evening. The memento cannot be a free recurring bargain or another woman's token. [P1:4; F1:8]
- **Convenient elapsed time → actual current form:** `tenant_body` and `night_mind` now say “instructive memories,” correctly avoiding months/years. Retain those fixes for fresh Ch5 lodger/statue/locust/host histories; add no duration gate. [F1:9–10, already corrected]
- **Wrong bargain receipt → her actual account:** rewrite living/toasted `night_after` to “The forfeit stands”; keep rent in `night_mind_after` only. Same memory appetite (A/G), distinct living contract versus lease. [P1:5; F1:11]
- **Contract eternally unsigned → bounded earlier feast:** Last Call recounts the feast and the offer she was preparing then, without predicting indefinite refusal or acceptance; keep divergent first-spring futures inside the late ending. Requires named shared-record escalation, not flags from an epilogue answer. [P1:6; F1:12]
- **Other romance controls her patron → canon lowest point / her chosen allegiance:** remove `crossroute.vellexia.unavailable` from `refuge`; remove its romance-closure gate from `patron`, retaining actual `patron_lost` and her evidence. Refuge variants distinguish protection, lost patron, and her betrayal (H), including both loss+betrayal together. [P1:8–9; F1:2–3]
- **Forced intention in envelope → good-intent nudge she tests:** keep its optional existing Act 4 contact/list `19786fae9c29f9d439e374bb857c2e84`, refuge evidence and real manor restrictions (H); her erased/revised answer defeats the scheme. The offending cooperative-choice foreign gate is already absent from this export; preserve its removal. [P1:10, corrected; F1:36]
- **Vanished lover → native partner obstacle with his own reaction:** C–E ground plant gaze/vine, chief's explicit farewell and authored letter, death acknowledgment, or unknown/distant silence. Current partner module supplies commitment/witness/discovery/endings; complete `price`, `evening`, `patron/refuge` continuity, never restore the plant with her tenant. [P1:12–23; F1:1, partially corrected]
- **Remote preparation labeled consummation → her pursuit in chosen imagining:** existing private charm evenings at Drezen/Nexus use her illusion craft (A/B/G); she directs the approach and interrupts with desire, the player chooses to continue, and the cut reaches the initiating act. No potion, incapacitation, invented rendezvous or convenient portal. [F1:15–17]
- **Death becomes gradual correspondence → honest closure:** the native sacrifice fact `381a296094804761af0893d2e70dc2df` blocks the living unfinished future unless the already-earned Commander return applies. Canon/player closures remain legitimate; no Shyka workaround. [P1:7]

## 5. Proposed uniqueness registration (coordinator action only)

- **Device class:** `she_pursues` — an oolioddroo collector chooses to leave her remote performance and claim an evening after the Commander has answered her prices; no document, toast, or lease produces her affection.
- **Setting:** Ch5 Drezen market rendezvous → Commander's quarters; the returned form makes a nerve-built duplicate of those quarters behind the left eye. These existing settings distinguish the encounter from a feast affair or a generic confession.
- **Payoff shape:** collector becomes a lover who wants an answer she cannot plant: separate physical/mental threshold, her possessive morning, and the later loss of a memory she alone retells. Preserve existing scale, rent and forfeit distinctions.
- **Why hers:** A/B/F/G make thought, guise, needles, memory and possession her methods; C–E make a captive lover's presence part of her independent appetite. H gives her an actual choice of allegiance; she stays cruel and interested, never reformed by intimacy.
- **Registry:** `tools/route_packs/turning_points.json` and other sheets are absent at this baseline; proposed tuple awaits coordinator collision review (device+setting and payoff shape). Do not create/edit that second file under this one-file task; no unique-slot certification is claimed.

## 6. Heat / VOI and player-speech class sweep

- **Heat class [F1:15–17]:** rewrite `unsold_evening/kiss`, `counterfeit_after/desire`, `room_measure/desire` through vivid imagined proximity, wing/chitin/guise sensation and her initiating motion; cut at the start of explicit acts, then collect an immediate emotional or practical consequence. Preserve each quiet choice and the remote premise.
- **Physical/mental siblings:** inspect `visit/threshold[_free]`, `future/tenant_pinned,tenant_free`, and late `night,night_host,night_mind` for cut timing, her appetite and a selectable stop. Do not expand beyond the ceiling or copy the same wings-and-bed choreography across all three correspondence scenes.
- **Register class [F1:18–21]:** remove author-side “adult” from `counterfeit_guest/square`, `counterfeit_after/guise`, `settlement_visit/inspection,buyer`; retain gray temples, scars, gown, tools and vanity. Keep abrasive laughter, cruelty and impatience; remove maxims/therapy/meta if found in siblings.
- **Gesture class [P1:11]:** delete the duplicated projected-hands movement in `price/x_start`; retain one transition and independently staged `collection/start`. Sweep folded-in `late_ordinary`/farewell and partner-continuation copies for duplicate transitions.
- **Player-speech rule:** move actual Commander replies into appended answers and split her following responses; retain every old node and choice index, gating obsolete answers. Keep her puppet imitation as HER performance, not an actual player reply; alternative attitudes only where the audited line already imposes a judgment.

| Finding | Exact scene/node sweep (prefix `jerribeth.`) |
|---|---|
| F1:22 | `offered_signature`: price, ownership, performance, send |
| F1:23 | `borrowed_sun`: shape, empty, expose, account, power_reply |
| F1:24 | `small_print`: start, kept, test, choice, correct, withdraw, after |
| F1:25 | `unsold_evening`: start, guise, near, kiss, frame, story, after, joke_enjoyed, joke_disputed (including unchosen promise) |
| F1:26 | `purchaser_answer`: sale, performance, design, withdrawn, kept, kept_design, temptation, credit |
| F1:27 | `counterfeit_guest`: previous_buyer, maker, return, appetite, square, judgment, keep |
| F1:28 | `counterfeit_hinge`: patient, result, clerk |
| F1:29 | `counterfeit_clerk`: payment, witness, drawings, release, end |
| F1:30 | `counterfeit_audience`: leverage, archive, departure |
| F1:31 | `counterfeit_spoil`: circles, work, account, catalogue, price, object, interest, complicit, end |
| F1:32 | `counterfeit_after`: wanted, own, guise, attention, desire, quiet, after, promised, next, fate, end |
| F1:33 | `settlement_visit`: visible, removed, report, comedy, decline, private_cost |
| F1:34 | `room_measure`: public_visible, public_refused, private_play, private_declined, loop, terrace, private, quiet |
| F1:35 | `promise_revisited`: chosen |
| F1:36 | `fate_envelope`: start, test, purpose, work, company |

## 7. Ordered, save-compatible implementation checklist (future authorized pass)

1. Freeze scene/node/relationship IDs, GuidFor namespace, answer indices and each legacy ending exit's identity, destination and mechanics; preserve existing file bytes/line endings. New nodes/choices append; retire through mutually covering gates, never delete targets.
2. Preserve corrected duration prose and removed envelope-choice gate; restore refuge/patron availability from native facts, using existing exported `jerribeth.harem.vellexia_defection_seen` (H) rather than demanding an invented producer for `betrays_vellexia`.
3. Complete Marhevok disclosure in `price/evening` and relocation in `patron/refuge`; preserve existing fate precedence, share/secret/exclusive refusal, witness and discovery consequences. Carry all native fates through together/ascended/apart/unfinished/sacrifice/late/Last Call; unknown is not dead or agreement.
4. Fix unpaid toast interest at EVERY signing path, including partner-continuation copies and late acceptance; repair both carrier recollections and living/tenant morning receipts. Append ending-local pay/refuse paths; late partner terms/discovery/witness likewise use local destinations, no persistent epilogue flags.
5. Separate deferred notice from completed visit, enforce the ≥96h physical-to-letter gap, preserve a later presence attempt, and correct Woljif evidence/date wording. Append scale keep/return receipts and collection to an existing evening/fold; no new event, scheduler, or affection/commitment gate.
6. Stage her pursuit/yes and pause at each intimate payoff; complete the three audited imagined thresholds, keep quiet alternatives, remove four age labels and duplicate gesture, then apply the whole player-speech table and sweep copied siblings.
7. Add unfinished-sacrifice exclusion with `trickster.commander_back`; keep dead/unreturned women and Commander out of living futures. Preserve earned existing returns and deliberate kill/decline closures; do not add a resurrection or happy-path bypass.
8. Coordinator resolves named shared Last Call paragraph and uniqueness registry. Any native rewrite must be authored, proportional, Trickster-only and gated/overridden save-compatibly; all other paths retain canon. No Shyka page for affection, consent or debt waiver; no new echo (Jerribeth has no allocated echo slot).
9. Later acceptance matrix: King/levy × host/memory/unpaid/paid toast × campaign/late accept/refuse; living versus four tenant forms, shortest Ch5 entry, both evening answers; visit completed/deferred/retried and delayed Woljif; Marhevok plant/chief/dead/distant/unknown × stances, Vellexia alive-romance-closed/dead/betrayed; unreturned/returned sacrifice.
10. Later validation must trace selectable answers and rendered ending→Last Call sequences, not union nodes from separate histories; every pay/refuse/stop and legacy exit stays usable. No validation commands were run for this planning-only task.

**ESCALATE:** coordinator-owned Last Call coda text, registry reservation/collision check, and any exporter/shared-rule fix if a route-local native guard is reintroduced. Shared files and other routes are outside this task; future code/prose implementation needs its own authorization.
**PROPOSE (not implemented):** only the audit-required pursuit, debt, continuity, heat and answer fixes above. No new mechanics beyond receipts demanded by existing promises; no new gates, costs, attraction thresholds, reconciliation conditions, pruning or rescue.
**RISKS:** source/export partner machinery currently sets persistent epilogue origin/stance/discovery flags; replace with local branches during the planned late fix. Audits predate the partner integration, uniqueness is pending, and no gates/audit were run; this sheet does not certify implementation quality ≥91.

# Chadali — round 2 set-piece sheet

## Implementation record — 2026-10-06

The planning text below is retained as the binding brief. Its "planning only"
status is superseded for these implemented route-owned situations:

- The charm/loan confession retains her power and invites visits separately
  from the luck account. The flat coin is her deliberate decision. The real
  wager records luck versus coin; both refusals collect it and yes releases it.
  The seed tests a place offered now, rather than promising a later test that
  never occurs. No combat luck statistic or germination gate was introduced.
- The existing parcel scene plays the AUTHORED two-claimant allocation: actual
  rations to the army, actual flour/honey to the shrine, both informed of the
  division. Chadali counters the attempted miracle credit. The AUTHORED oven
  and tray loan is returned at the morning doorway, conditional on that scene;
  her invitation names another visit. CHA-01/02 adopted; CHA-03/04 adapted as
  honest allocation and a chosen return, with no forged proof or new fee.
- The registered private-table pursuit remains the turning point. Honey is
  her prepared first night; the later wish scene is a return. Three dedicated
  slot nodes use heated-cut defaults and the supplied briefs. No explicit
  sexual prose was generated, and slots carry no commitment or payment flags.
- The AUTHORED Chapter 5 market afternoon is separate from paid reconciliation.
  A route-owned spawn-copy hub, `chadali.presence.market`, stands left of the
  native Drezen tiefling vendor. Its failed-anchor visit is the same afternoon
  delivered through a personally arriving visitor, not an arrival by letter.
  The specified fifty-crown flour task and her independent answer produce
  readiness; friendship and postponement remain available. Live Trickster and
  earned return are required. Placement references: DrezenCapital
  `2570015799edf594daf2f076f2f975d8`, Vendor_Tiefling
  `23eabf5b6364d4a4e86202dc5d27600b`, Chadali unit
  `75fd91d9d6119ea408a981680c659267`. In-game placement is not claimed tested.
- Personal replies to the two existing letters record accepted romantic
  intent. Donation, kept penny and mere contact do not produce that receipt.
  Late Stay reads the invitation; Half remains undecided, and friendship has
  an appended answer plus a contact-only postwar slide. Legacy ending exits
  remain inert. Coin, penny and object-free mornings have distinct histories.
- Treatment, hopeful words, notebook/oral report, military signature/names,
  loan repayment and optional memories read their own provenance. Historical
  Eritrice references no longer require her romance to remain open. Present
  Eritrice's actual reaction still requires her availability. Native public
  Council denial is preserved; their anniversary is private. No echo, partner
  or partner-stance duty was invented.

Shared-owner work is deliberately NOT represented as implemented:

- `tools/departure_contracts.json` must classify the new penny reaction,
  market hub scene, failed-anchor visit and contact-only ending, and apply the
  existing Chadali `present_now` / `reachable_by_letter` gates as appropriate.
  These new surfaces already require those predicates in route-owned code;
  the inventory entries themselves remain shared-owner work.
- `tools/payoff_contracts.json` / `storylines/engine_eng3_ab.py` still replace
  the late predicate with the old broad `courted` arms. They must consume
  `chadali.trickster.late_romantic_intent` / `return_test.ready` rather than
  infer acceptance from an initial investment or contact. The route's late
  intimate choice already requires its separate invitation predicate.
- Shared Last Call/page/ledger owners must consume the new
  `chadali.fortunes.loan_returned` receipt, distinguish investment, unpaid loan,
  repaid loan and needle-only histories, and stop claiming that an illness or
  bandage pays the real extraction oath. Their original text was not edited.

No independent score is claimed. Save references and original CRLF endings
were retained. Final reporting includes actual gate results and these residuals;
the later user instruction forbids a commit.

Planning only, 2026-10-06. No route implementation, registration, gates, export regeneration, builds or tests were performed. All situations below extending the native dialogue are **AUTHORED**. They are proposals for implementation under the named findings, not claims about shipped canon. The later “do not git commit” instruction governs this delivery.

## Evidence and constraints

Read: POLISH-AGENT-PROMPT steps 1–3; 00-WRITING-GUIDE; ROUND2-TURNING-POINTS including both revisions and slot production rules; CANON-PARTNERS-DESIGN including stance revision; TRICKSTER-RUBRIC including contexts (1)–(5), echo discipline and DLC rewrites; atlas turning_points.json and Chadali/cluster entries in sameness_atlas.md; TRIAGE Chadali rows; origin/claude/tp-chadali:tools/route_packs/plans/chadali-tp.md; handoffs/trickster/chadali.md; all five storylines/chadali_*.py files and their development/Story.json scenes. Source and export are evidence, not writable deliverables. P1/F1 identifiers below refer to the defect mapping in the turning-point sheet; no new independent audit score is claimed.

Native references checked directly in /wrath/blueprints.zip and /wrath/Wrath_Data/StreamingAssets/Localization/enGB.json. In the references below, GUID is AssetId; L is localization key.

| Ref | Native evidence |
| --- | --- |
| C1 | World/Dialogs/c3/Mythic_Trickster/Council_Chadali/Cue_0001.jbp — `f674c7cfeac2f364097f5479e810415d`, L `14f12f99-f466-4e4c-9967-2987c97e13c4`: dark-skinned, middle-aged Vudrani appearance; yellow silk; long black hair, white flowers, dimples; homemade cookies. No invented anatomy, maidenhood, former lover or appetite history. |
| C2 | Same directory Cue_0007 — `0d35409a73cbeca408393e2bbbb6c6e1`, L `d15027d3-6596-4b7c-b4d7-0196ed2d9088`: empyreal lord, worshippers, healing and strengthening some, limited beside the gods. Neither powerless nor a goddess who can save everyone. |
| C3 | Same directory Cue_0008 — `0f9a7d1379a0aeb4f8ccd807c8cb0f20`, L `206cb4b0-4e85-4225-a872-86b9c28f4758`: Elysian aurora/eclipse/meteor birth and sharing happiness. Cue_0012 — `dc4fa93063e42c44981850d65914402e`, L `e9c8ab1f-ec44-4d4e-8c46-279ac53a07b3`: she believes in, creates and embodies chance. |
| C4 | Same directory Cue_0017 — `12bb8e9afd0788c4a864e29d4add775f`, L `d320556e-e598-4bff-85bb-1e220bd05258`: bossy, sulking response to odious questions. Cue_0018 — `51c885e2c38d7e544a1d1415d4404bcf`, L `be517247-236d-4906-9f06-b177bb1a1664`: flat refusal, raised plump finger, white-gold ring. Warmth never makes her incapable of saying no. |
| C5 | Council_Chadali/AnswersList_0003 — `e649f211c6b002a49a0c633061877927`; clean return Cue_0002 — `ed7a31d6f063e0c4aa4ec4e08fab57c0`, L `cc70442d-766d-4992-a93c-8249ae51d144`. Unit `75fd91d9d6119ea408a981680c659267` has no ordinary dialogue component (spec/runtime constraint). Existing physical contact uses the hall list; post does not establish a Drezen unit. |
| C6 | World/Dialogs/c5/Mythic_Trickster/Council_5-1/Cue_0001 — `dfd57a47e39fa1f4fa1f811f5fe02591`, L `6da6d2b9-c0f1-456c-aaa2-5e53089625f3`: Axis orange is her guess. Cue_0041 — `b936cf96571c0354fb7a57f4987fea5c`, L `adb7f77e-d356-4dc8-86b1-3eeaa05c5779`: actual bag contains a soul cauldron. The seed's provenance is her authored claim, never narrator-certified native fact. |
| C7 | World/Dialogs/c5/Mythic_Trickster/Shyka_Offer/Cue_0002 — `c3b8e7f1537c7cb4d839b2cff532cbb6`, L `3fbe1d5d-067d-4fcc-a9c7-723a454baffa`: Council lies unconscious while essence is extracted. Council_Chadali/Cue_0033 — `86822037eac848943abe4be795037ae7`, L `5157fcd6-3e64-4bd8-94d6-9e6932c647ac`: extraction hurt; honey cookies/sharp needles. A return here repairs hostility/contact, not death. |
| C8 | World/Dialogs/c5/Mythic_Trickster/Council_5-2/Cue_0003 — `fa43e0b471527ec4ea59b268e6fcf36d`, L `591b0abc-843a-4e5d-8a74-78e4897b4c11`: fair replacing wastelands/battlefields, acrobats, lollipops, extraplanar beasts. Her optimism coexists with Council danger; it does not sanitize Alichino or Socothbenoth. |
| C9 | World/Dialogs/Epilogues/Cue_0568 — `0ffd4b0bb2346fc4282aed98f478cb96`, L `42050e0c-abea-4da8-99ae-e82edecf1e08`: after carnage/extraction the Council ceases and ALL members publicly deny knowing it. Private remembrance fits; public contradictory declarations do not. |

Reservation is unchanged: `she_pursues`; **her private Council table, sun-and-moon coin deliberately laid flat**; payoff **unriggable spoken yes releases the stake → honey night → burnt-cookie morning**. Do not edit the registry in this task. Avoid Eritrice's minutes, witness hearing and two procedural ayes; Areelu's soul experiment; Kiana's mid-act partner arrival; another route's drunken or aphrodisiac accident; the generic rescue/token/observer-assent structure. No forged claim record or false-proof device: the cluster cap is respected by telling both claimants the actual allocation. Other she_pursues routes have their own settings; Chadali's object is her deliberately stopped wager, not a love-winning throw.

No native live/possible partner is identified in the supplied partner design or her canon dialogue. Socothbenoth bringing flowers is an authored manipulation already in this route, not evidence of a relationship. The remembered azata in what_chance_wishes/tell is an authored birth-party acquaintance, not a missing spouse. Partner near-discovery/discovery/confrontation/stance/partner-move set pieces are therefore **not applicable**. Do not create partner_stance flags, adultery, an exclusivity demand or a cuckold scenario. Her discovery conflict is misattributed aid and debts; the household issue is time with other lovers. Those require her answer, not a fabricated partner.

## Six situations

### 1. The charm she keeps — entry, Ch3 or Ch5, open Council hall

**Present:** Chadali and Commander at her private end of the table; Eritrice reacts separately only when currently available. **Risk:** the crusade is betting on this Council while its members have separate ends; Chadali could mistake a clever trick for a promise. **Lead-in:** native chance question, `chadali.chance_asked`; current Trickster entry. C1–C5.

**Play:** retain council.coin/start → edge → both, its Chaotic effect and existing luck-lent receipt. She watches the knuckle trick rather than losing her own power to it. She keeps the balanced coin to invite a return. In council.orange, the staged market orange appears only after the actual cauldron handover and orange history; the early/non-orange history keeps start_edge. Confess the staging; she identifies what the Commander did and separately owns borrowing luck. No real magical-orange miracle.

**Her move/options:** she invites another visit because she enjoyed the cheating she could see. Commander leaves, invests the loan, or asks repayment with interest using current choices. Her welcome is spoken, not inferred from `started` at scene entry. Loan/debt is not a romantic yes.

**Payoff/carry:** a reason to return and a distinct luck account; no bed or household claim. Later lore/flirt may develop it. Eritrice's historical quip stays historical if unavailable; no prerequisite that her romance be open. Ember's cookie reaction stays wholly friendly. Endings/Last Call know whether a coin was actually introduced and whether luck remains lent or owed. Mapped: P1-3–7/13, F1-3–5/29/31. No public reaction or helper sets commitment.

### 2. Two claimants, one unexpected surplus — build-up, Ch3/5 hall; branch delivery in Ch5 market

**Present:** Chadali, Commander; an unnamed crusade provisioner and one of her worshippers are interlocutors through the existing a_parcel_for_the_shrine exchange, not permanent new cast. **Risk:** a seized cache is being claimed both for a front-line ration issue and for the shrine's promised relief. The claims are AUTHORED, not a new native quest or invented established faction rivalry. **Lead-in:** her_worshippers, the offered parcel, casualty pressure in so_gloomy. C2/C3/C8.

**Play:** fold CHA-01 into the existing parcel situation, not another event. Inspect the real goods together: usable rations answer the army's stated claim; the cooking surplus answers the shrine's. The Commander's benign con is to let each claimant think their objection forced this split, without lying about ownership, quantities or credit. Both get what the actual cache permits. No forged requisition, blackmail, victim deprived of necessities or instant magical supply. If the goods do not suffice, say so; retain existing leave/refusal options rather than inventing a resource fee.

**Her counter-move/options:** she catches the Commander trying to flatter her as miracle-worker, names the human help, and sends the parcel under its true provenance. Commander supports the split, owns the assistance, or declines with existing consequences. Her response to the priests' needs exists even without a romance. In the fought-history delivery variant, use the single market event already requested by the TP sheet, after paid contact; do not run a second cache adventure. The TP's proposed Finances −50 flour task remains a proposal awaiting implementation authorization; no new cache cost is added here.

**Payoff/carry:** the surplus honey/flour is a small windfall she chooses to spend baking, not stolen military pay. CHA-02 then supplies the morning's claimant: the provisioner wants the lent cooking equipment back before the next ration issue. CHA-03/04 are ADAPT: an honest repair of the shortfall using the already allocated goods, and she names the next visit without a coin toss. No free money, invoice romance or new debt gate. Misattributed shrine aid later supports rigged only if this history actually concealed credit; credited aid cannot trigger that accusation. Outcomes include openly assisted charity, concealed-credit quarrel, and refused aid. Carry her independent work into household talk and coda; no sexual reward for flour. Mapped CHA-01/02/03/04, F1-16, P1-3, F1-5.

### 3. The wager she stops — registered turn, Ch3/5 private Council table

**Present:** Chadali and Commander; no witness awarding assent. **Risk:** a personal no and the already-stated wager stake; not combat luck or another woman's place. **Lead-in:** her_worshippers → a_free_space and a_lucky_charm → so_gloomy as currently structured; optional not_today exposes her impatience and nervousness without adding another requirement. War reports are still on the table. C3/C4/C5.

**Play:** the_real_wager asks for the question, not a throw. Retain luck and coin answers and postponement. She lays the coin flat herself: she can stand it up, but will not let it answer. Both luck selections identify the same existing personal stake; coin stake relinquishes their balancing game. In second_cookie, truth reaches her_test and the ask reaches her explicit yes; flattery and tossing reach the existing spoken refusals. Fix “Next, you say yes” framing by having her interrupt any attempt to script her answer, then decide herself on-page. Do not move the commitment producer or change its legacy mechanics.

**Her move/options:** yes releases the selected liability; both refusals collect it according to what was actually staked. Later a_coin_lying_flat admits she deliberately stopped the game, not that the patron cannot affect coins without the Commander. For the existing second ask, orange_tree tests provision of a place NOW, with the same Materials −100. She sees the choice, says yes at planted, or takes the seed back at refused. Remove the unfulfilled future germination condition; no growth gate, gardener score or delayed return event.

**Payoff/carry:** honest courtship becomes her invitation to the honey night; refusal is still refusal. Collected stake, invested/repaid loan, purchased place and ordinary yes remain separate facts in endings and Last Call. A flower by itself grants nothing. Household does not infer love from a wager completed. Mapped P1-4/25–28, F1-6–9/32; retains atlas tuple. The return branch uses her same unriggable answer after renewed courtship, not a second turning-point device.

### 4. Honey, then the burnt tray — payoff/afterward, Ch3/5 open hall at night and following morning

**Present:** Chadali and Commander, alone; next morning only, provisioner at the outer doorway if set-piece 2 happened. **Risk:** she has invited a lover deliberately; the war will reclaim the Commander, and her promised goods/equipment remain due. **Lead-in:** earned commitment, existing 12-hour honey delay; previous flirt/physical comfort is not a first night. C1/C3/C5.

**Play:** retain honey's crooked candles, cushions, last flower, hot kiss, cold bracelets, impatience with armor, and her deliberate preparation. Condense explanatory narration in hands/kiss/look; let her actions carry it. Slot `chadali.fortunes.honey.explicit.1` replaces the transition at cut while cut itself and the initiating choice's existing night receipt survive. This is their first night only once. Default text and brief below are non-graphic staging, with a seamless transition to morning.

**Her move/options:** she calls the Commander over, returns the kiss and draws them close. Existing optional visit/leave behavior is preserved; add only append-only postponement if required to make the new slot page selectable. A refusal never advances to the slot by default. Neither chance, intoxication, a page nor gratitude causes her desire.

**Morning:** burnt_edges keeps the disastrous tray. Secret/start differ on the actually learned recipe secret. Replace “that's the whole point” and “the kind you make” with her annoyance at burning breakfast while preoccupied with the lover still beside her. Her short boast and reluctance to let the Commander go carry adult affection without anatomical narration. If the cache was used, a morning knock demands the borrowed oven/tray back: she answers it herself, wrapped in her robe, and hands back the actual equipment. It is a comic consequence of overspending her baking windfall, not an interruption during sex and not discovery of a spouse. Commander can eat the wretched cookie or invite her back beside them; bed → not_luck remains a return to warmth rather than a second first night. No second explicit slot for that joke.

**Carry:** she owns the night's choice in daylight and names a return visit. The claimant is paid in the promised equipment/goods, not a new fee or forgiveness flag. Subsequent sharing collects actual time (“not the crumbs”), rather than reassurances alone. Household sees her independent work and chosen return; endings distinguish prewar first night from late first night. Mapped HEAT request, CHA-02/03/04, TP debt “not the crumbs”, P1-31–39 unavailable morning answers.

### 5. What the cauldron took — Ch5 crisis, hall or earned market contact

**Present:** hall branch Chadali and Commander after the native cauldron encounter; fought branch correspondence first, then Chadali and Commander in the single authored market delivery variant, if contact was earned. **Risk:** extraction injury, trust already breached, and an outstanding apology or real-needle oath. **Lead-in:** actually seen feared/needled cues or latched fight. C6/C7; Drezen market area `2570015799edf594daf2f076f2f975d8` and vendor unit `23eabf5b6364d4a4e86202dc5d27600b` are placement references from the TP sheet, not dialogue ownership.

**Play:** will_it_hurt distinguishes truthful warning from reassurance; sharp_needles distinguishes voluntary extraction from the fought assault. Its sorry node cannot assert voluntary giving in a forced history. A shawl and embrace soothe her but do not restore essence, pay a debt or grant romance. In fought.lucky she rejects the clever bet and states the existing price: public apology/Favors −200 or needle oath. Refusal closes. Paid letters establish permission to contact her, not physical arrival.

**Her counter-move/options:** at the TP's market afternoon she asks for straightforward help to her worshippers, notices if the Commander disguises help as a miracle, and names another visit or ends the afternoon herself. Commander can help, accept correspondence/friendship or leave; no further reconciliation conditions are added. The requested accepted-intent/ready receipts record decisions actually played, never the donation alone. A returned former lover does not replay a first night; an uncommitted return does not skip her wager/answer. Slot-worthy intimacy remains in the earned night situations, not in medical recovery.

**Payoff/carry:** contacted, forgiven, courting and committed are different. She may still be angry after the war-feint job response until its named-company obligation is actually paid; holding hands does not erase that. Last Call must retain needle debt when it is the only account, distinguish unpaid luck from already paid_back, and allow no fresh luck call from a settled loan. Household cannot place her at a table while unreturned/unavailable. Endings do not declare her healed by a cookie. Mapped P1-8/9/21/22/24/29/30; F1-22–25/27/33/34. Placement and shared Last Call changes require escalation.

### 6. A return she names — late payoff, Last Call and endings

**Where/when:** later Ch3/5 private hall for what_chance_wishes/sharing/seat/last_evening; Ch5 sealed-hall correspondence; Ch6 post-Threshold Drezen only with living/earned-return Commander and her earned presence. **Present:** Chadali and Commander physically only where justified; other Council reactions are historical or individually availability-checked. **Risk:** being offered exhausted scraps, an unearned postwar yes, or a public claim contradicting native denial. **Lead-in:** their actual current state, not assumed completion of every optional scene. C1/C4/C5/C9.

**Play:** what_chance_wishes/stay is a later invitation: she draws the familiar cushions out and chooses a return together. Slot `chadali.sessions.what_chance_wishes.explicit.1`; no new first-night declaration. In sharing she demands a usable portion of time, accepts either existing promise, then names the next visit herself. No schedule mechanic. Seat is offered/accepted NOW before handholding is described; no invented past acceptance, vote or Shyka witness. Last evening transfers the actual coin and keeps one custody chain; a companion can walk the saucer through the existing portal without creating an NPC spawn.

**Late histories:** orange_letter and late_wager separate fruit/donation, friendly response and an accepted romantic invitation in preceding gameplay. Fought contact requires the separate on-page courtship decision described in the TP, not a return receipt alone. Epilogue Stay's earned yes can use `chadali.trickster.epilogue.commit.explicit.1`, as a first night if none occurred, otherwise a reunion. No prior-hall details in object-free or penny-only history. Half remains undecided; remove its forced summer commitment and sex. Keep its legacy answer/destination/effects; append an optional later affirmative continuation only if prior gameplay earned it. Friend/coin/penny departures must also show her promised later RETURN, nonsexual where appropriate.

**Her answer/options:** stay, uncertainty, friendship or goodbye retain their real distinctions. She chooses the evening and its next visit; a collected stake does not purchase a yes. Commander can accept the whole-cookie demand without claiming exclusivity over other women. Partner fallout remains N/A.

**Carry:** endings return to an inhabited room, with her work or named visit evident; lucky_night can show a later kiss/return without repeating the first-night scene. Separate ordinary yes/tree yes, primed coin/penny/neither, called/reset coin, repaid/outstanding/invested loan, apology/needle owed, feast/convened/ceased Council, and living/unreturned Commander. Ceased Council remembrance is private. No new fate device, resurrection or public canon rewrite is needed. Mapped P1-1/2/9–12/23; F1-1/2/14/15/26/28/30/31/34; global triage first-night/return discipline.

## Intimacy slots and delivery limits

These are reserved insertion positions, not new implemented nodes. JSONs use the example's voice/scene/last_line/speakers/example/min_lines/max_lines fields, plus commander_variants. Their briefs describe non-graphic romantic staging and continuity only; graphic prose and prompts directing its generation are not supplied. A separate author may fill reserved material independently. Defaults stand alone if no material is inserted; the final tagged line in each brief is exactly the last line of that default. Existing scene/node IDs and effects survive; slot insertion is append-only and never owns commitment, payment, arrival or return flags. No slot is needed for handholding, treatment, a forehead kiss, uncertain Half or the morning oven gag.

| Slot / future insertion | Default heated cut | Resume |
| --- | --- | --- |
| `chadali.fortunes.honey.explicit.1` — between existing look choice and cut exit, preserving night receipt | `{n}Chadali draws you close among the cushions, her bracelets cold against your neck. She kisses you again, impatient with the last buckle.{/n} "Come here, lucky charm." | Existing cut exit, then burnt_edges at its current delay. No first-night claim elsewhere afterward. |
| `chadali.sessions.what_chance_wishes.explicit.1` — after stay invitation, before old terminal exit | `{n}She pulls the familiar cushions into place, catches your sleeve and draws you down beside her. Her mouth meets yours before you can finish speaking.{/n} "You're staying." | Old stay terminal; later visits and sharing remain available under their existing contracts. |
| `chadali.trickster.epilogue.commit.explicit.1` — earned stay before its morning paragraph | `{n}Chadali sets the basket aside and settles close, one hand at your collar. She kisses you, then reaches back to close the shutters herself.{/n} "The basket can wait." | Stay's corrected morning: actual object custody, no effortless garrison luck miracle, her named next return. No epilogue effects. |

Morning-after heat is carried by dishevelment, a lingering kiss, her proprietary claim on the morning and reluctance to surrender it to the army. Do not replace appetite with a welfare questionnaire. Chadali's generosity, impatience and bossiness are the register; cruelty, compulsory sex, demon domination and diagnosis-as-addiction would be invented characterization. The existing a_drinking_song cup already smells of something strong; retain tipsy, bawdy singing and her self-possession. It does not become a second drunken turning point or an incapacity-induced choice.

## Heat audit key

The following inventory covers every existing romantic physical/intimate situation and its setup/afterward nodes, including answer-only kisses and holding, plus medical/comfort touch that must remain distinct from sexual escalation. Quotes are from this checkout's Story.json; source was cross-read. **H0** comfort/ceremony, **H1** flirt or kiss, **H2** sensual night threshold/aftermath. **KEEP** means appropriate to that situation, not permission to dilute a night; **REWRITE** means situational or register failure; **SLOT** reserves the above position. No numerical auditor scores are invented. A good passage is quoted as a control rather than falsely described as weak. Rows with no physical act cover its necessary romantic buildup or aftermath. Full IDs are reconstructed from the namespace plus scene name in each table.

## Ordered round-2 implementation checklist (future authorized work)

1. Snapshot scene/node/relationship IDs, answer indices/destinations/effects and CRLF bytes. Keep all legacy nodes and exits; appended choices go last. No renamed IDs or GuidFor namespace. Preserve old ending mechanics, including effect-free endings.
2. Apply situation/voice repairs across all siblings: domain/power dependence; promise/maxim narration; optional remembered events, speakers, scar choice, coin/penny custody, elapsed durations and credited aid. Label authored situations in the coordinator-owned spec. Do not add invented past meetings or canon partner facts.
3. Preserve current entry, delay, commitment, decline and closure contracts. Record only audit-required route-local receipts at actual producer choices: selected wager stake/settlement, loan return, feint signing/names, accepted late intent and the TP return-test decision. Do not derive them from a kiss, rescue, affair, postage, donation or scene entry. No new luck statistic, attraction requirement, resource price or growth gate.
4. Stage the six situations through existing scenes; one TP market event maximum, with placement/fallback validated. Fold cache claimant exchanges into the existing parcel and morning, rather than adding a quest or another event. Current costs remain current; the TP's specific market/feint proposals require review, never spread them to other branches.
5. Make both refusals collect the actual wager liability and yes release it; keep postponement/abort behavior. Correct the seed's present-tense test with existing Materials debit and planted yes. Restore friendly/undecided post histories; do not auto-return women or force Half to yes.
6. Append the three slots only to their appropriate earned affirmative continuations. Retain cut/stay destination nodes and legacy night receipt position. Defaults must flow to the correct morning/return if no inserted material exists. First night occurs once; later nights are returns. No conditional paragraphs outside epilogue pages; use ordinary branch nodes elsewhere.
7. Stage offered seat and touch in the present; confine optional recollections to the recorded choice. Historical Eritrice references must not require her open romance. Check all affected siblings named by the TP; if shared crossroute_presence classification still injects unrelated closure conditions, escalate the classifier instead of changing it here.
8. Coordinate current-state household, Last Call/page/call/ledger and epilogue consumers. Distinguish needle-only, outstanding loan, returned loan and invested luck; do not pay needle debt with a brooch, bandage or love scene. Preserve native Council denial through private remembrance. No Shyka page earns desire or supplies an echo (none is allocated to Chadali).
9. Review histories: both stakes × both refusals; ordinary yes/seed yes/refusal; postponement; credited/concealed aid; cache/no cache; early night/no night; donated post/friendly post/accepted romantic post; fought refusal/paid contact/friendship/courtship; coin/penny/neither; repaid/invested/unpaid/needle-only; Council available/lost/sealed; Commander alive/sacrificed/earned return. Every page retains a selectable leave/friendship/postpone where its existing contract allows it. A skipped legitimate gate earns no payoff.
10. Coordinator runs expansion with PYTHONHASHSEED=0, applicable Python suites, strict verifier and Rules/progression validation under implementation authorization. None is run in this planning-only task. Review diff for scoped edits and line endings; changes to storylines, shared consumers, tests, export or registry remain outside this delivery.

Acceptance is a story-history check, not “all outcomes reachable”: each romantic advance has her affirmative decision; negative or unresolved histories stay negative/unresolved; every asserted debt/object/participant has its actual provenance. Deliberate kills and user-ruled closures stand. Unreturned departure or death blocks presence; unreturned fatal sacrifice blocks living postwar scenes. A new canon alteration, if later required, must be Trickster-only, proportionate, authored-labelled and paired with save-compatible replacement of exactly its contradicted native facts. No such alteration is proposed here.

## Escalations / proposals / risks

ESCALATE: implementation in storylines/chadali_*.py, slot wiring/export, tests and registry/spec updates are outside this allow list. Shared household, lastcall*.py, debt ledger and crossroute_presence classifier need their owners. The market unit needs a route-owned talkable presence and placement verification; a letter must never set physical arrival. This sheet does not implement any of those changes.

PROPOSE: none beyond the cited TP/triage situations. No partner, magic cure, new currency cost, reconciliation hurdle or echo.

RISKS: CHA cache and equipment loan are authored additions and need runtime staging review; avoid turning them into civic bookkeeping. Source/export are not regenerated here, so later implementation must compare both. A generic slot expansion could erase her voice or fabricate anatomy; briefs restrict physical facts and exclude Commander speech from NPC prose. This deliverable supplies non-graphic briefs only, so the requested graphic-generation layer remains unfulfilled. No independent >=91 score is claimed. Gates and git commit were deliberately skipped under the planning-only hard rule and final no-commit instruction.

## Complete heat inventory — existing nodes

Nodes not listed below were also read: recipes, native-origin exposition, supply discussion, Council politics, correspondence/return refusals, nonphysical war choices, and friendly Ember reactions have no sexual/romantic physical event. Blessing and recovery controls are included to avoid converting every touch into sex. Native partner reactions do not exist for this route; household deferral/sharing reactions are included. The shared chadali.lastcall.page/call contain account/call text without romantic physical action and need debt-state coordination, not an explicit slot.


### chadali.trickster.council.second_cookie

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `yes` | “You said it and it happened!" She pushes the whole parcel into your hands and holds on to your wrists over it. "That's the luckiest thing ” | H1 KEEP | Keep her immediate spoken yes and grip on the wrists; show her releasing the actual wager stake, never narrate the trick as causing assent. |

### chadali.trickster.after.orange_tree

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `start` | “She does not offer a cookie.” | H1 REWRITE | Present provision of a place, same Materials debit; flower follows her chosen yes. Remove future-growth condition and narrator-certified Axis provenance. |
| `planted` | “"The best corner!" She claps once, and then presses her folded hands against her mouth, and her eyes are very bright over them. "It will t” | H1 REWRITE | Present provision of a place, same Materials debit; flower follows her chosen yes. Remove future-growth condition and narrator-certified Axis provenance. |

### chadali.trickster.epilogue.commit

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `page` | “The spring after Threshold, a Vudrani woman in yellow silk came up the road to Drezen with a basket on her arm, and the gate guards afterwards” | H1 REWRITE | Separate accepted late intent, friendship and uncertainty; preserve legacy exit identity/effects. Show an earned return and history-correct object. |
| `stay` | “Then she pulled the white flower out of her hair, unpinned the yellow silk at her shoulder and let it fall to her waist, came round the table, an” | H2 SLOT | Earned affirmative history only: chadali.trickster.epilogue.commit.explicit.1 before corrected morning. Distinguish late first night from reunion, coin/penny/neither, and living Commander. |
| `half` | “That's a yes, you know.” | H1 REWRITE | Remove forced summer yes, bed scene and automatic moving-in. Keep uncertainty and legacy exit mechanics; any later affirmative continuation must be appended and separately earned. |
| `coin` | “She looked at the coin in her palm for a long time, turning it, sun and moon.” | H0 KEEP | Annual nonsexual return already fits undecided/friendly history. Never describe waiting as guaranteed eventual consent. |
| `penny` | “She took the penny off its string and turned it over, the Drezen mint on one side and the worn king on the other.” | H0 KEEP | Actual sent penny, hand closing over it and annual return; friendship/uncertainty stays distinct from romance. |

### chadali.trickster.epilogue.lucky_night

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `page` | “The coin stood on its edge on a shelf in the Commander's quarters for the rest of their life together, and on the nights Chadali stayed, she w” | H2 REWRITE | Show her later return and lingering kiss before she tends her own affairs; retain exact debt/Council/object states, no repeated first night. |

### chadali.wagers.a_lucky_charm

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `start` | “as if you were a very good dog” | H1 REWRITE | Play her affectionate bossiness against a real wounded Commander; retain her independent healing work, remove dog/ornament framing and dependence on their reminding her of her domain. |
| `person` | “The hand stops on your cheek.” | H1 REWRITE | Play her affectionate bossiness against a real wounded Commander; retain her independent healing work, remove dog/ornament framing and dependence on their reminding her of her domain. |
| `ornament` | “"An ornament!" She is scandalised. "Ornaments sit on shelves!” | H1 REWRITE | Play her affectionate bossiness against a real wounded Commander; retain her independent healing work, remove dog/ornament framing and dependence on their reminding her of her domain. |
| `whose` | “"Whose?" She opens her mouth, and closes it, and the dimples come and go and come again. "The Council's," she says firmly. "Obvious” | H1 REWRITE | Play her affectionate bossiness against a real wounded Commander; retain her independent healing work, remove dog/ornament framing and dependence on their reminding her of her domain. Answer touch: `"Then stay nearby."`. Show her response on-page without auto-escalation. |
| `think` | “"You want me to think about it." She takes a long breath through her nose, the way you might before diving into cold water. "All right.” | H1 REWRITE | Play her affectionate bossiness against a real wounded Commander; retain her independent healing work, remove dog/ornament framing and dependence on their reminding her of her domain. |
| `anyway` | “"Good." Her dimples are back, deep enough to lose a coin in. "Then I'll keep saying it, and you'll keep being it, and we'll both pretend i” | H1 REWRITE | Play her affectionate bossiness against a real wounded Commander; retain her independent healing work, remove dog/ornament framing and dependence on their reminding her of her domain. |
| `close` | “"Lucky charm." She says it once more, gently, as if testing whether it still fits. "Yes.” | H1 REWRITE | Play her affectionate bossiness against a real wounded Commander; retain her independent healing work, remove dog/ornament framing and dependence on their reminding her of her domain. |

### chadali.wagers.odious_questions

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `brick` | “She is quiet for so long that the lamp gutters. "There was a girl in Kenabres.” | H0 REWRITE | Grief and an accepted hand, not sexual reward for tragedy. Cut abstract reassurance/maxims; give her concrete memory and independent response. Answer touch: `[Say nothing. Take her hand.]`. Show her response on-page without auto-escalation. |
| `fault` | “The world wants to help you, it just isn't always able to.” | H0 REWRITE | Grief and an accepted hand, not sexual reward for tragedy. Cut abstract reassurance/maxims; give her concrete memory and independent response. Answer touch: `[Take her hand.]`. Show her response on-page without auto-escalation. |
| `good` | “Her head comes up fast, and for a moment the empyreal lord looks out of the plump, sweet face, and it is not sweet at all. "What good is a” | H0 REWRITE | Grief and an accepted hand, not sexual reward for tragedy. Cut abstract reassurance/maxims; give her concrete memory and independent response. Answer touch: `[Take her hand.]`. Show her response on-page without auto-escalation. |
| `hand` | “Her fingers close on yours at once, tight, sticky with honey.” | H0 REWRITE | Grief and an accepted hand, not sexual reward for tragedy. Cut abstract reassurance/maxims; give her concrete memory and independent response. |

### chadali.wagers.so_gloomy

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `open` | “The field reports were bad, you took them to your chamber to be alone with them, and somehow you opened the closet instead of the shutters, and n” | H1 KEEP | Keep the casualty name, removed gauntlet and her chosen closeness; shorten explanations. Distinguish whose hopeful words were actually spoken in later recalls. |
| `start` | “"Oh." She has seen your face.” | H1 KEEP | Keep the casualty name, removed gauntlet and her chosen closeness; shorten explanations. Distinguish whose hopeful words were actually spoken in later recalls. |
| `name` | “I send it anyway." She takes your gauntleted hand and starts, very carefully, to unbuckle it. "You can't hold a cookie in this.” | H1 KEEP | Keep the casualty name, removed gauntlet and her chosen closeness; shorten explanations. Distinguish whose hopeful words were actually spoken in later recalls. |
| `many` | “"I know." She sits down next to you, not across, and leans her whole warm weight against your arm. "There are always too many.” | H1 KEEP | Keep the casualty name, removed gauntlet and her chosen closeness; shorten explanations. Distinguish whose hopeful words were actually spoken in later recalls. |
| `no_cheer` | “"I'm not going to cheer you up." She says it firmly. "Cheering up is for when you've spilt something.” | H1 KEEP | Keep the casualty name, removed gauntlet and her chosen closeness; shorten explanations. Distinguish whose hopeful words were actually spoken in later recalls. |
| `hope` | “When your hands are bare she holds them between hers.” | H1 KEEP | Keep the casualty name, removed gauntlet and her chosen closeness; shorten explanations. Distinguish whose hopeful words were actually spoken in later recalls. |
| `hoped` | “When it comes true, I'll give it back, and you'll say, 'That was luck,' and I'll say, 'That was you.'" She lifts your bare knuckles and kisses” | H1 KEEP | Keep the casualty name, removed gauntlet and her chosen closeness; shorten explanations. Distinguish whose hopeful words were actually spoken in later recalls. |
| `cant` | “"That's all right." She does not let go of your hands. "Then I'll say it.” | H1 KEEP | Keep the casualty name, removed gauntlet and her chosen closeness; shorten explanations. Distinguish whose hopeful words were actually spoken in later recalls. |

### chadali.wagers.the_real_wager

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `open` | “There are no cookies tonight.” | H1 REWRITE | Private desire and risk: she stops the coin, states the existing stake and controls her own answer. No sexuality or commitment flag from a wager alone. |
| `start` | “"A proper one." She has her hands folded in her lap, very still, which is not like her. "We've made lots of little bets.” | H1 REWRITE | Private desire and risk: she stops the coin, states the existing stake and controls her own answer. No sexuality or commitment flag from a wager alone. |
| `bet` | “Otherwise it's just wishing."” | H1 REWRITE | Private desire and risk: she stops the coin, states the existing stake and controls her own answer. No sexuality or commitment flag from a wager alone. |
| `people` | “You bet on that little witch with the fire in her hands.” | H1 REWRITE | Private desire and risk: she stops the coin, states the existing stake and controls her own answer. No sexuality or commitment flag from a wager alone. |
| `stake` | “She lets out a long breath, and the stillness goes out of her all at once; she is bouncing again, very slightly, in her chair. "Done!” | H1 REWRITE | Private desire and risk: she stops the coin, states the existing stake and controls her own answer. No sexuality or commitment flag from a wager alone. |
| `both` | “"Both!" She laughs, and the laugh wobbles at the end. "Heads and tails at once.” | H1 REWRITE | Private desire and risk: she stops the coin, states the existing stake and controls her own answer. No sexuality or commitment flag from a wager alone. |
| `not_tonight` | “"Then not tonight." She nods, as if this too were fair. "The coin will keep standing.” | H1 REWRITE | Private desire and risk: she stops the coin, states the existing stake and controls her own answer. No sexuality or commitment flag from a wager alone. |

### chadali.wagers.a_coin_lying_flat

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `open` | “The coin is lying flat on the Council table, and nobody has stood it back up.” | H1 REWRITE | She stopped the coin deliberately; refusal remains real while lingering fingers show unresolved attraction. No claim that the patron cannot move a coin herself. |
| `start` | “I wanted to see if it would stand up again by itself, if I believed very hard.” | H1 REWRITE | She stopped the coin deliberately; refusal remains real while lingering fingers show unresolved attraction. No claim that the patron cannot move a coin herself. |
| `tomorrow` | “I'm chance, and I don't know.” | H1 REWRITE | She stopped the coin deliberately; refusal remains real while lingering fingers show unresolved attraction. No claim that the patron cannot move a coin herself. |
| `wait` | “"Good." Her fingers brush yours as the coin changes hands, and stay a moment longer than they need to. "I'm still cross.” | H1 REWRITE | She stopped the coin deliberately; refusal remains real while lingering fingers show unresolved attraction. No claim that the patron cannot move a coin herself. |

### chadali.fortunes.will_it_hurt

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `keep` | “She holds your eyes for a long time, measuring, the way she looks at a coin she suspects of being weighted. "All right," she says at la” | H0 KEEP | Fear/contact before extraction, not foreplay. Separate honest warning from reassurance and retain the actual native history. |
| `there` | “That I can hold.” | H0 KEEP | Fear/contact before extraction, not foreplay. Separate honest warning from reassurance and retain the actual native history. |
| `brave` | “She straightens up in her chair, the way you have seen soldiers straighten when the horns sound. "Then I'll be brave.” | H0 KEEP | Fear/contact before extraction, not foreplay. Separate honest warning from reassurance and retain the actual native history. |

### chadali.fortunes.a_great_big_fair

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `close` | “"When it's done, you'll come." Not a question. "You'll come to my fair and hold my hand and pet the puppy.” | H1 KEEP | Her offered hand belongs to a concrete postwar fair hope, not a magical guarantee of survival or a romance condition. |

### chadali.fortunes.matching_ribbons

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `close` | “She pulls a length of yellow ribbon out of her sleeve, where it has apparently been all along, and ties it in a bow round your wrist before yo” | H1 KEEP | A playful wrist ribbon, not intimacy with Nocticula; let the demon remain dangerous. Do not manufacture a shared bed from the joke. |

### chadali.fortunes.sharp_needles

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `open` | “She is sitting very still in her chair, wrapped in a shawl that is not yellow.” | H0 REWRITE | Injury and chosen comfort, never sex as treatment. Keep anger and unknown healing; voluntary and forced extraction need different explanations. |
| `start` | “Chance doesn't always bring you honey cookies.” | H0 REWRITE | Injury and chosen comfort, never sex as treatment. Keep anger and unknown healing; voluntary and forced extraction need different explanations. |
| `sit` | “You sit.” | H0 REWRITE | Injury and chosen comfort, never sex as treatment. Keep anger and unknown healing; voluntary and forced extraction need different explanations. |
| `grow` | “"I don't know." She shrugs, and winces. "Nobody's ever taken any of me before.” | H0 REWRITE | Injury and chosen comfort, never sex as treatment. Keep anger and unknown healing; voluntary and forced extraction need different explanations. |
| `sorry` | “"Sorry for what?" Firmly. "You promised nobody would take it from me by force, and nobody did.” | H0 REWRITE | “Nobody held me down” belongs only to actual voluntary history. Fought history retains breach, apology/oath and her anger; embrace is not absolution. Answer touch: `[Hold her.]`. Show her response on-page without auto-escalation. |
| `joke` | “She laughs.” | H0 REWRITE | Injury and chosen comfort, never sex as treatment. Keep anger and unknown healing; voluntary and forced extraction need different explanations. |

### chadali.fortunes.honey

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `open` | “The hall is lit only by candles, dozens of them, set along the Council table in a crooked, happy line that someone has plainly done without me” | H2 KEEP | Preserve deliberate invitation and impatient affection; shorten narrated explanations, keep her bossy warmth. Resume the existing morning, first night once. |
| `start` | “Chadali is standing in the middle of the cushions in a robe of yellow silk so thin the candlelight comes through it.” | H2 KEEP | Preserve deliberate invitation and impatient affection; shorten narrated explanations, keep her bossy warmth. Resume the existing morning, first night once. Answer touch: `[Take her hands.] "You did it perfectly."`, `[Kiss her.]`. Show her response on-page without auto-escalation. |
| `forgot` | “"What?” | H2 KEEP | Preserve deliberate invitation and impatient affection; shorten narrated explanations, keep her bossy warmth. Resume the existing morning, first night once. Answer touch: `[Kiss her.]`. Show her response on-page without auto-escalation. |
| `hands` | “Her hands are warm and shaking, and they stop shaking when you hold them. "Perfectly." She tries the word out, and decides it suits her” | H2 KEEP | Preserve deliberate invitation and impatient affection; shorten narrated explanations, keep her bossy warmth. Resume the existing morning, first night once. Answer touch: `[Kiss her.]`. Show her response on-page without auto-escalation. |
| `kiss` | “She kisses the way she laughs, all at once and with her whole body, up on her toes with both hands knotted in your sleeves, and when she runs out” | H2 KEEP | Hot mouth/cold bracelets and returned kiss already fit. Remove explanatory “which, you slowly understand” clause; retain appetite. |
| `silk` | “She is soft everywhere your hands go, and warm, and nowhere near as patient as she was trying to look.” | H2 KEEP | Armor struggle and impatient joke already fit. Keep concrete action; avoid invented canon claims about the language she curses in. |
| `look` | “When the last of it is off she pulls you down among the cushions, and the candles gutter in the draught you make, and for a moment she simply ” | H2 KEEP | Her hand on chest and own invitation carry desire; retain existing night receipt on affirmative choice, not on slot generation. |
| `cut` | “her laugh against your mouth is the last thing you hear clearly” | H2 SLOT | Insert chadali.fortunes.honey.explicit.1 at this transition; keep cut node and terminal identity. Default preserves her initiative and flows into burnt_edges. |

### chadali.fortunes.burnt_edges

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `open` | “Chadali is kneeling in front of it in the yellow robe, with her hair in a wild knot and a tray in her mitted hands, and the tray is smoking.” | H2 REWRITE | Give the morning bodily presence through mussed hair, a kiss and reluctance to release the lover; keep burnt food and her chosen boast. Pay equipment claimant only in cache history. |
| `secret` | “That's the whole point. That's what last night was.” | H2 REWRITE | Give the morning bodily presence through mussed hair, a kiss and reluctance to release the lover; keep burnt food and her chosen boast. Pay equipment claimant only in cache history. |
| `start` | “I eat them myself, alone, the way I always do." She looks at the black cookies, and at you, and her mouth twitches. "And now you know.” | H2 REWRITE | Give the morning bodily presence through mussed hair, a kiss and reluctance to release the lover; keep burnt food and her chosen boast. Pay equipment claimant only in cache history. |
| `eat` | “It crunches like a cinder and tastes, faintly, underneath the char, of honey and of something that is not like anything at all. Chadali wa” | H2 REWRITE | Give the morning bodily presence through mussed hair, a kiss and reluctance to release the lover; keep burnt food and her chosen boast. Pay equipment claimant only in cache history. |
| `more` | “last night.” | H2 REWRITE | Give the morning bodily presence through mussed hair, a kiss and reluctance to release the lover; keep burnt food and her chosen boast. Pay equipment claimant only in cache history. |
| `bed` | “"The oven cannot wait.” | H2 REWRITE | Put out the oven, answer the morning claimant if present, then she returns beside the Commander with a kiss. No second first-night slot for a breakfast invitation. |
| `not_luck` | “The kind you make.” | H2 REWRITE | Replace luck maxim with her blunt delight and named return; she kisses the Commander back instead of ending only on a soot-nose peck. Answer touch: `[Kiss the soot off her nose.]`. Show her response on-page without auto-escalation. |

### chadali.fortunes.rigged

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `choose` | “"Promise me you'll stop." She holds out her little finger. "Not the tricks.” | H1 REWRITE | Link fingers after real credit dispute, never after openly credited help. Her counter-offer names her priests and truthful aid; love does not settle false credit. |
| `stopped` | “She shakes on it, once, firmly, and some tension goes out of her shoulders that you had not known was there. "Good.” | H1 REWRITE | Link fingers after real credit dispute, never after openly credited help. Her counter-offer names her priests and truthful aid; love does not settle false credit. |
| `kept` | “She looks at your hand, and at her own outstretched little finger, and slowly curls it back into her fist. "Then do it with your name on i” | H1 REWRITE | Link fingers after real credit dispute, never after openly credited help. Her counter-offer names her priests and truthful aid; love does not settle false credit. |

### chadali.fortunes.the_meadows

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `start` | “"Home!" She lies back on the cushions she has refused to put away, and stretches, and her bracelets slide down her arms. "Meadows.” | H1 REWRITE | After-night closeness and mortal unease; describe her present wish rather than generic eternity vows. Elysian scenery is authored recollection, not verified native geography. |
| `allowed` | “"Allowed!" She sits up, scattering cushions. "You don't need allowing.” | H1 REWRITE | After-night closeness and mortal unease; describe her present wish rather than generic eternity vows. Elysian scenery is authored recollection, not verified native geography. |
| `mortal` | “I've watched a great many of them go, and I've hoped for every one." She takes your hand. "I'm not going to count yours.” | H1 REWRITE | After-night closeness and mortal unease; describe her present wish rather than generic eternity vows. Elysian scenery is authored recollection, not verified native geography. |
| `point` | “I'll keep making the bet for as long as I exist, and I exist for a very long time, and I've never lost a bet I cared about." Her thumb moves o” | H1 REWRITE | After-night closeness and mortal unease; describe her present wish rather than generic eternity vows. Elysian scenery is authored recollection, not verified native geography. |
| `promised` | “entirely unromantic” | H1 REWRITE | Remove “entirely unromantic” narrator disclaimer. After their night, let the forehead kiss be affectionate without apology; no need to escalate this mortal-life conversation. |

### chadali.fortunes.a_yellow_ribbon

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `start` | “She has pressed something into your hand: a length of yellow silk ribbon, the same yellow as her robes, tied in a lopsided bow. "For luck!” | H1 REWRITE | Public/private gift carries pride and the next battle; play both answer-kisses as returned kisses. Replace jealousy maxim and narrator explanation of how hard understanding is. |
| `officers` | “Teasing is just jealousy wearing a hat.” | H1 REWRITE | Public/private gift carries pride and the next battle; play both answer-kisses as returned kisses. Replace jealousy maxim and narrator explanation of how hard understanding is. |
| `worn` | “She watches you knot it round the hilt with her hands clasped under her chin. "It suits you.” | H1 REWRITE | Public/private gift carries pride and the next battle; play both answer-kisses as returned kisses. Replace jealousy maxim and narrator explanation of how hard understanding is. Answer touch: `[Kiss her.]`. Show her response on-page without auto-escalation. |
| `pocket` | “Luck isn't vain." "...I am, a bit." A small, honest smile. "I wanted them to see it.” | H1 REWRITE | Public/private gift carries pride and the next battle; play both answer-kisses as returned kisses. Replace jealousy maxim and narrator explanation of how hard understanding is. Answer touch: `[Kiss her.]`. Show her response on-page without auto-escalation. |

### chadali.fortunes.sharing

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `start` | “Alichino says it as if it were a price: the whole crusade holds a mortgage on you, he says, and I'm a very late creditor." "They're right about t” | H1 REWRITE | Her appetite includes a real visit before exhaustion. She names the return after either existing promise; no schedule, score, rival elimination or forced exclusivity. |
| `mind` | “She hesitates, and the hesitation goes on for long enough that you understand it is serious. "I don't want to be last." Small, and very” | H1 REWRITE | Her appetite includes a real visit before exhaustion. She names the return after either existing promise; no schedule, score, rival elimination or forced exclusivity. |
| `not_last` | “That's my favourite kind of luck.” | H1 REWRITE | Her appetite includes a real visit before exhaustion. She names the return after either existing promise; no schedule, score, rival elimination or forced exclusivity. Answer touch: `[Lie down beside her.]`. Show her response on-page without auto-escalation. |
| `war` | “She takes that, and turns it over, the way she turns her ring. "Then I'll share with the war too.” | H1 REWRITE | Her appetite includes a real visit before exhaustion. She names the return after either existing promise; no schedule, score, rival elimination or forced exclusivity. |

### chadali.fortunes.paid_back

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `owed` | “"You said you'd want it back.” | H1 KEEP | Palm/forehead contact accompanies actual repayment or investment, not payment in affection. Keep loan-return receipt distinct from scene completion. |
| `on_you` | “She laughs, and swats your arm. "You can't spend my luck on me!” | H1 KEEP | Palm/forehead contact accompanies actual repayment or investment, not payment in affection. Keep loan-return receipt distinct from scene completion. |

### chadali.sessions.a_dull_future

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `bet` | “And if they laugh, you win." She holds out her hand. "And if they don't laugh, it means they saw it, and then I win, and you owe me a very” | H1 REWRITE | Her experiment and held hand remain flirtation; remove Commander-as-restorer-of-chance framing. Shyka laughing earns no affection or echo. |
| `shake` | “Her hand closes on yours with surprising strength. "Done.” | H1 REWRITE | Her experiment and held hand remain flirtation; remove Commander-as-restorer-of-chance framing. Shyka laughing earns no affection or echo. |
| `here` | “She opens her mouth, and closes it, and goes pink all the way up to the white flowers in her hair. "That's...” | H1 REWRITE | Her experiment and held hand remain flirtation; remove Commander-as-restorer-of-chance framing. Shyka laughing earns no affection or echo. |

### chadali.sessions.an_interesting_way

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `close` | “She takes your hand and turns it over and looks at the palm, the way fortune-tellers do in the markets, though she does not pretend to read an” | H0 REWRITE | Concern for the living Commander and the rift; her held palm is neither prophecy nor commitment. Give her an informed response, not limitless protective magic. |

### chadali.sessions.a_drinking_song

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `start` | “Loudly, tunelessly, and with enormous confidence, alone at the Council table with a cup of something that smells of honey and cinnamon and someth” | H1 KEEP | Canon-compatible authored strong drink and bawdy bad rhyme; let her be tipsy, loud and self-possessed. No new drunken first night, incapacity or diagnostic framing. |
| `please` | “"Too late!” | H1 KEEP | Canon-compatible authored strong drink and bawdy bad rhyme; let her be tipsy, loud and self-possessed. No new drunken first night, incapacity or diagnostic framing. |
| `how` | “It is about a coin that would not fall down, and a Commander who "never once left a thing to chance, and never once lost a single dance".” | H1 KEEP | Canon-compatible authored strong drink and bawdy bad rhyme; let her be tipsy, loud and self-possessed. No new drunken first night, incapacity or diagnostic framing. |
| `sing` | “Who never left a thing to chance!"” | H1 KEEP | Canon-compatible authored strong drink and bawdy bad rhyme; let her be tipsy, loud and self-possessed. No new drunken first night, incapacity or diagnostic framing. |
| `laugh` | “She pretends to be offended for exactly one verse, and then she is laughing too, and cannot finish the tenth verse at all. "It's terrible,” | H1 KEEP | Canon-compatible authored strong drink and bawdy bad rhyme; let her be tipsy, loud and self-possessed. No new drunken first night, incapacity or diagnostic framing. |
| `close` | “"I'll teach it to your soldiers.” | H1 KEEP | Canon-compatible authored strong drink and bawdy bad rhyme; let her be tipsy, loud and self-possessed. No new drunken first night, incapacity or diagnostic framing. |

### chadali.sessions.two_patrons

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `friends` | “We're both right." Softly. "She's been at this table longer than anyone, holding it together with her claws.” | H1 REWRITE | Keep her friendship with Eritrice independent of the Commander. Her deferred household answer stays deferred; no promise of a joint bed or speaker summoned by a remembered remark. |
| `know` | “"No!” | H1 REWRITE | Keep her friendship with Eritrice independent of the Commander. Her deferred household answer stays deferred; no promise of a joint bed or speaker summoned by a remembered remark. |
| `side` | “The bracelet stops turning.” | H1 REWRITE | Keep her friendship with Eritrice independent of the Commander. Her deferred household answer stays deferred; no promise of a joint bed or speaker summoned by a remembered remark. |

### chadali.sessions.what_chance_wishes

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `start` | “"Me?" She is honestly startled, a cookie halfway to her mouth. "Nobody asks me that.” | H1 REWRITE | Current surprise followed by her specific wish; introduce the flower trick now, retain independent affection and optional nonsexual responses. No invisible shared past. |
| `flower` | “Nobody touches my flowers without my noticing!" She holds the flower as if it were a jewel. "That's a good surprise.” | H1 REWRITE | Current surprise followed by her specific wish; introduce the flower trick now, retain independent affection and optional nonsexual responses. No invisible shared past. |
| `secret` | “I'm chance, and I didn't know."” | H1 REWRITE | Current surprise followed by her specific wish; introduce the flower trick now, retain independent affection and optional nonsexual responses. No invisible shared past. |
| `purpose` | “That's the most surprising thing you've ever said!" She laughs so hard she has to hold on to you. "Oh, that's wonderful.” | H1 REWRITE | Current surprise followed by her specific wish; introduce the flower trick now, retain independent affection and optional nonsexual responses. No invisible shared past. |
| `close` | “I got my wish." She leans back, satisfied. "You can have one back.” | H1 REWRITE | Current surprise followed by her specific wish; introduce the flower trick now, retain independent affection and optional nonsexual responses. No invisible shared past. Answer touch: `"Stay the night."`. Show her response on-page without auto-escalation. |
| `bake` | “"Something new!" She claps. "Oh, that's dangerous.” | H1 REWRITE | Current surprise followed by her specific wish; introduce the flower trick now, retain independent affection and optional nonsexual responses. No invisible shared past. |
| `tell` | “She leans close and whispers it.” | H1 REWRITE | Held affection after authored birth-party recollection; keep acquaintance unspecified. No missing lover/spouse invented; Commander may choose comfort without another night. Answer touch: `[Hold her.]`. Show her response on-page without auto-escalation. |
| `stay` | “"That isn't a wish, that's just asking." But she is already pulling the cushions out from under the table, where she has apparently been keepi” | H2 SLOT | Later chosen night: chadali.sessions.what_chance_wishes.explicit.1 before old exit, familiar cushions and her invitation. No first-night reset or new mechanics. |

### chadali.sessions.you_bet_with_people

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `wanted` | “That stops her.” | H0 REWRITE | She may sit beside and hold a lover she is angry with; feint/names debt remains. Silent signing must actually recount names before forgiveness is claimed. |
| `silent` | “You say nothing.” | H0 REWRITE | She may sit beside and hold a lover she is angry with; feint/names debt remains. Silent signing must actually recount names before forgiveness is claimed. |
| `felt` | “She holds your hand on the table between you, tightly, and does not say it is all right, because it is not. "They were lucky, you know.” | H0 REWRITE | She may sit beside and hold a lover she is angry with; feint/names debt remains. Silent signing must actually recount names before forgiveness is claimed. |

### chadali.sessions.the_last_evening

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `open` | “It does.” | H1 KEEP | Keep the actual saucer/coin transfer and chosen company through the existing portal; add no power reward. Her return is named, not inferred from a token. |
| `start` | “I know the feeling; I was born in it." "So I want you to take the coin.” | H1 KEEP | Keep the actual saucer/coin transfer and chosen company through the existing portal; add no power reward. Her return is named, not inferred from a token. |
| `keep` | “You balanced it." She folds her hands firmly in her lap. "I kept it here so you'd have to come back for it.” | H1 KEEP | Keep the actual saucer/coin transfer and chosen company through the existing portal; add no power reward. Her return is named, not inferred from a token. |
| `carry` | “It holds. Chadali watches you with both hands pressed over her mouth, and when you turn toward the door, she makes a small sound, half lau” | H1 KEEP | Keep the actual saucer/coin transfer and chosen company through the existing portal; add no power reward. Her return is named, not inferred from a token. |
| `together` | “She is at your side before you finish, her small warm hand under the saucer beside yours, her bracelets held carefully still. "Together, t” | H1 KEEP | Keep the actual saucer/coin transfer and chosen company through the existing portal; add no power reward. Her return is named, not inferred from a token. |
| `walk` | “You walk.” | H1 KEEP | Keep the actual saucer/coin transfer and chosen company through the existing portal; add no power reward. Her return is named, not inferred from a token. |

### chadali.hours.make_some_stronger

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `bless` | “She takes your hands in both of hers.” | H0 KEEP | Ceremonial hands are her own limited blessing before battle, not sex or dependence. Do not attach commitment to aid. |

### chadali.hours.an_unlucky_day

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `search` | “It takes half an hour, and involves a great deal of dust, three spiders, a cookie from what must be the Council's first session, and one of Eritr” | H1 KEEP | Looking beside her is chosen company; failed trick is caught by her. Keep comic dust and impatience, avoid universal therapy claims or gratitude-as-love. |
| `trick` | “You reach behind her ear and bring back your hand with something white-gold in it, glinting. She reaches for it, and stops.” | H1 KEEP | Looking beside her is chosen company; failed trick is caught by her. Keep comic dust and impatience, avoid universal therapy claims or gratitude-as-love. |
| `found` | “She takes the earring and puts it back in, and shakes her head so it clinks, and the sound seems to put something right. "There.” | H1 KEEP | Looking beside her is chosen company; failed trick is caught by her. Keep comic dust and impatience, avoid universal therapy claims or gratitude-as-love. |

### chadali.hours.not_today

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `open` | “She is baking.” | H1 KEEP | Keep flour, attraction, nerves and her chosen postponement; brief teasing, no forced yes or extra readiness gate. She determines when the question is welcome. |
| `start` | “It's just that I've got flour everywhere and I look like a ghost and I want to be wearing the yellow when you ask.” | H1 KEEP | Keep flour, attraction, nerves and her chosen postponement; brief teasing, no forced yes or extra readiness gate. She determines when the question is welcome. |
| `tease` | “She throws a handful of flour at you.” | H1 KEEP | Keep flour, attraction, nerves and her chosen postponement; brief teasing, no forced yes or extra readiness gate. She determines when the question is welcome. |
| `perfect` | “If you answer I'll believe you, and then I'll want you to ask, and I've got dough under my nails."” | H1 KEEP | Keep flour, attraction, nerves and her chosen postponement; brief teasing, no forced yes or extra readiness gate. She determines when the question is welcome. |
| `nervous` | “She is quiet, her floury hands gone still in the bowl. "I don't get nervous," she says at last. "I'm getting nervous.” | H1 KEEP | Keep flour, attraction, nerves and her chosen postponement; brief teasing, no forced yes or extra readiness gate. She determines when the question is welcome. |
| `ready` | “"When I'm yellow." She nods, and goes back to kneading, more gently. "And when I've stopped shaking.” | H1 KEEP | Keep flour, attraction, nerves and her chosen postponement; brief teasing, no forced yes or extra readiness gate. She determines when the question is welcome. |
| `brave` | “This is being brave where you can watch me do it, and I hate it." She shoos you with a floury hand. "Go on.” | H1 KEEP | Keep flour, attraction, nerves and her chosen postponement; brief teasing, no forced yes or extra readiness gate. She determines when the question is welcome. |

### chadali.hours.for_luck

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `open` | “It is not only a scratch.” | H0 REWRITE | Treat wound first, then her chosen kiss. Scar/healed skin must branch on actual scar answer; remove embedded Commander speech and reflexive hiding after the kiss. |
| `start` | “She kneels in front of you and undoes the bandage with quick, steady hands, far steadier than her voice. "I said I heal some.” | H0 REWRITE | Treat wound first, then her chosen kiss. Scar/healed skin must branch on actual scar answer; remove embedded Commander speech and reflexive hiding after the kiss. |
| `scar` | “Why would you want a scar?” | H0 REWRITE | Treat wound first, then her chosen kiss. Scar/healed skin must branch on actual scar answer; remove embedded Commander speech and reflexive hiding after the kiss. |
| `heal` | “It is the feeling of a door closing quietly somewhere far away, and the draught stopping. When she takes her hands away, the wound is clos” | H0 REWRITE | Treat wound first, then her chosen kiss. Scar/healed skin must branch on actual scar answer; remove embedded Commander speech and reflexive hiding after the kiss. |
| `after` | “I'm an empyreal lord; I'm not supposed to scream at scratches." Then, quieter, her hand still resting on the new scar: "Come to me first.” | H0 REWRITE | Treat wound first, then her chosen kiss. Scar/healed skin must branch on actual scar answer; remove embedded Commander speech and reflexive hiding after the kiss. |
| `close` | “so that you cannot see her face” | H1 REWRITE | Kiss the chosen scar or healed skin accordingly; let her meet the lover’s eyes before taking up the bandage. Her healing/medical closeness is not a sex slot. |

### chadali.hours.the_seat_beside_her

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `open` | “The session has ended and the others have gone, but the evidence is still there: two chairs pushed so close together at the end of the table t” | H1 REWRITE | Offer the seat/hand NOW and let Commander accept; stop inventing past touch or a witnessed vote. Present reactors only if available; her request needs no new rule or minutes. |
| `start` | “And then I held your hand under the table for the entire session, and you let me.” | H1 REWRITE | Offer the seat/hand NOW and let Commander accept; stop inventing past touch or a witnessed vote. Present reactors only if available; her request needs no new rule or minutes. |
| `thinking` | “"Your thumb." Instantly, and then she claps both hands over her mouth. Through her fingers, muffled: "That's not what I should have” | H1 REWRITE | Retain attraction to the thumb as her frank admission after presently accepted touch; no whole missed vote retroactively invented. |
| `careful` | “Cobblehoof pretends not to see, which is how he says he's happy for you." "Eritrice minuted it." She giggles. "She wrote, 'The patron of s” | H1 REWRITE | Offer the seat/hand NOW and let Commander accept; stop inventing past touch or a witnessed vote. Present reactors only if available; her request needs no new rule or minutes. |
| `close` | “Until the hall closes." She picks up the cookie from the chair and holds it out. "That's not a bet.” | H1 REWRITE | Offer the seat/hand NOW and let Commander accept; stop inventing past touch or a witnessed vote. Present reactors only if available; her request needs no new rule or minutes. |

### chadali.hours.pretend_we_never_met

| Node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `you` | “Remembering the nice parts, even when everyone else has decided it wasn't nice." She looks at you. "I just don't want to be the only one.” | H1 REWRITE | Keep accepted hand/pinky contact, shorten memoir maxims; private anniversary respects native all-member public denial. A promise is not physical arrival. |
| `war` | “That's the most honest thing anyone's said at this table in weeks." She takes your hand. "Then I'll remember for both of us, and if you ev” | H1 REWRITE | Keep accepted hand/pinky contact, shorten memoir maxims; private anniversary respects native all-member public denial. A promise is not physical arrival. |
| `promise` | “She holds on for a long time. "Then there'll be two of us.” | H1 REWRITE | Keep accepted hand/pinky contact, shorten memoir maxims; private anniversary respects native all-member public denial. A promise is not physical arrival. |

Inventory: 138 node entries across 33 existing situations, plus the three gambling-touch controls below. Slot defaults and briefs are planning assets, not replacements already applied.

### Gambling-touch controls (class sweep)

| Scene / node | Existing passage (exact excerpt) | Register / action | Situation-level direction |
| --- | --- | --- | --- |
| `chadali.wagers.just_joking/wager` | “She holds out her hand.” | H0 KEEP | An offered wager handshake, not a romantic agreement. Optional devil-bet recalls require this event; neither public wager nor another lord attending buys affection. |
| `chadali.wagers.just_joking/shake` | “Her hand is small and warm and dusted with flour” | H0 KEEP | Her firm handshake can carry fondness without becoming another turning point. No slot or commitment receipt. |
| `chadali.wagers.just_joking/rig` | “She shakes your hand anyway, hard.” | H0 KEEP | Her counter-rule imposes the already-stated two-tray liability if the meeting is rigged. No new fee; no sexual payoff for a contrived attendance. |

Other apparent touch matches were excluded deliberately: the_old_fellow/mend holds a feather in both hands, knucklebones handles bones/cup, and a_lucky_number/zero touches a paper. These are object handling, not physical intimacy. The knucklebones affection/counter-cheat belongs to buildup; its dice-confession history must still control later finger comparisons. No intimacy node was replaced in this planning pass.

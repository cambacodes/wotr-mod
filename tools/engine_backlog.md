# Engine backlog — integration inventory

Input: `/work/Writer/drafts/engine-inventory-input.json` (SHA-256 `71f9d6e22cd5dfcd90cc39c1e2f13ffdb98f225341dd01495e099414a010b27c`). Snapshot `149aec151349`; 2867 generated scenes, 47 presences, 145 guarded open-route readers.

**All 757 findings classified: 485 ENGINE / 272 ROUTE; 0 unclassified, across 35 routes.** Draft findings are included (51 ENGINE / 35 ROUTE) but excluded from cap impact. IDs use the original one-based defect index; duplicate quotes and separate dimensions are never collapsed.

The JSON retains every original problem, fix, route score/cap, classification, primary item, source references and available generated scene contract. ROUTE records have `item_id: null`. The appendix below maps every finding; item membership is disjoint. Items may cite related items without double-counting findings.

## Classification and scope

ENGINE means missing or insufficient shared runtime, reader, data contract, deterministic lint or acceptance check. Existing advisory narration/draft checks are insufficient to enforce the reported class. ROUTE means a local semantic claim, callback, choice effect or character/register problem that existing gates/actions/prose can correct. A new annotation could describe any writing mistake; that alone is not evidence of a missing engine mechanism.

Binding contexts (1)–(5) remain in force: deliberate player kills and user-ruled closures stand; gone/dead women need a matching earned return; new canon-changing acts and native alterations are Trickster-only; paid/discoverable gates legitimately exclude runs; another woman's loss is never a required romance price. Existing earned historical facts do not disappear merely on a path change. Preserve all IDs, nodes, old answer targets and choice indices. New replacement text must be labelled authored and preserve native continuation/actions outside its earned world.

Foresight remains a paid gate, never the outcome device. Preserve the allocated echo registry, existing 8/1/2 caps, unique sense/misstep, costs and neutral outcomes; do not add echo slots. DLC-tier events are legitimate when plausible and explained; reconcile the native facts they actually change, rather than undoing the approved event. No new price, attraction/commitment requirement, repair condition or mechanic is authorized.

## Evidence and existing coverage

The input audits different route branches; this is the integration snapshot. Generated contracts show several already-landed repairs: `DerivedOpenRoutes`, current-path T6/T7 checks, dead-original/live-copy contact disambiguation, conditional paragraph validation and full-ransom Kiana gate declarations. Do not infer that a historical finding still reproduces, and do not reintroduce absent partial gates/draft declarations to make it reproduce. The new backlog includes regression coverage where the shared implementation already exists.

q6a/q6b are in flight by the task declaration; their files are absent here. Coverage below maps to their planned ownership, not a claim they pass. Their task files were read to verify coverage: L4 already names Jannah/Nenio, and q6b already includes native journal objectives. Land those workstreams first; consume their reports/registry instead of building duplicates. Native target/localization evidence is checked against the supplied `/wrath` reference bundle; target existence/text does not alone prove every canon interpretation or native reachability.

Native evidence: 107 unique 32-hex references in finding problems/fixes; 106 indexed blueprints, 81 with joined localization. The remaining reference, `3e2b5ea054cd5b2479e7f13134363ef4`, is cited as a scene asset, not a Blueprint GUID. It is kept separate from the blueprint index. Concrete witnesses include Anevia Cue_3 mourning, Areelu TE_Final/Cue_3 spell use, Crossroads Cue_0569 and Nenio FoxReveal/Cue_0023. Exact paths/types/localization and per-finding target links are in JSON.

## Split per route

| Route | ENGINE | ROUTE | Total | Draft E/R |
|---|---:|---:|---:|---:|
| anevia | 11 | 0 | 11 | 0/0 |
| areelu | 8 | 0 | 8 | 0/0 |
| arsinoe | 68 | 4 | 72 | 0/0 |
| arueshalae | 1 | 8 | 9 | 0/0 |
| camellia | 40 | 2 | 42 | 0/0 |
| chadali | 3 | 1 | 4 | 0/0 |
| devarra | 4 | 3 | 7 | 0/0 |
| eliandra | 4 | 36 | 40 | 0/0 |
| elyanka-and-camilary | 0 | 3 | 3 | 0/0 |
| eritrice | 4 | 9 | 13 | 0/0 |
| galfrey | 24 | 15 | 39 | 16/8 |
| gesmerha | 10 | 1 | 11 | 0/0 |
| hepzamirah | 5 | 1 | 6 | 0/0 |
| herrax | 17 | 4 | 21 | 0/0 |
| horzalah | 11 | 30 | 41 | 0/0 |
| iomedae | 4 | 2 | 6 | 0/0 |
| irabeth | 11 | 1 | 12 | 0/0 |
| jannah | 8 | 1 | 9 | 0/0 |
| jerribeth | 0 | 1 | 1 | 0/0 |
| kaylessa | 6 | 15 | 21 | 0/0 |
| kiana | 37 | 2 | 39 | 0/0 |
| konomi | 0 | 8 | 8 | 0/0 |
| melazmera | 11 | 2 | 13 | 0/0 |
| mielarah | 12 | 12 | 24 | 0/0 |
| minagho-and-chivarro | 35 | 2 | 37 | 0/0 |
| nenio | 46 | 11 | 57 | 0/0 |
| nocticula | 2 | 18 | 20 | 0/0 |
| nurah | 3 | 1 | 4 | 0/0 |
| seelah | 1 | 13 | 14 | 0/0 |
| shamira | 15 | 1 | 16 | 0/0 |
| soana | 2 | 2 | 4 | 0/0 |
| terendelev | 44 | 19 | 63 | 35/17 |
| vellexia | 2 | 2 | 4 | 0/0 |
| wenduag | 36 | 29 | 65 | 0/10 |
| yaniel | 0 | 13 | 13 | 0/0 |
| **Overall** | **485** | **272** | **757** | **51/35** |

## Ordered backlog

Impact = affected routes × cap severity. Affected routes are audit origins plus explicitly named consumer scene/Guest List/seating routes; unnamed potential future routes are not counted. Severity is `100 − cap` for the mapped dimension, otherwise `100 − dimension score`; draft-only findings contribute zero. Each item uses its largest applicable severity. The JSON separately preserves origin counts and links all 48 original caps to dimension-compatible shipped findings/items without judging new caps. Handoff-only live tasks have zero audit impact and remain listed. Execution follows prerequisites even when a low-ranked blocker must land first.

### E-Q7-12 — Require actual producers, placement and derived completion in acceptance fixtures

Impact **640** = 16 routes × 40 severity; **22 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Create reusable integration walkers that compute Rules.Complete, run ChoiceAvailable (including affordability), observe/plan placement, acquire real simulated contacts and apply verified native transition inputs. Stop injecting contacts, desired composite facts or transient failure flags as proof of delivery. Known intended-positive walks may not print an escalation and pass. Register currently opt-in transition checks in the required test runner, with deterministic failure output.

**q6 coverage:** new — shared test infrastructure; reinforces all q6a/q6b checks

**Audit origin routes/counts:** areelu (2), arsinoe (1), camellia (2), galfrey (1), gesmerha (2), hepzamirah (1), irabeth (2), jannah (1), kaylessa (1), kiana (1), mielarah (1), minagho-and-chivarro (2), nocticula (1), nurah (1), shamira (1), wenduag (2). Affected routes: areelu, arsinoe, camellia, galfrey, gesmerha, hepzamirah, irabeth, jannah, kaylessa, kiana, mielarah, minagho-and-chivarro, nocticula, nurah, shamira, wenduag.

**Acceptance:** Mutation fixtures removing a return producer, disabling placement, withholding native ascend_all, skipping Rules.Complete, clearing failure on travel or making a payment unaffordable must fail the relevant positive acceptance test. Negative fixtures must pass by withholding the outcome, not by skipping the test. Nocticula Nm1BudgetTests coda must be evaluated after Complete. Report every expected positive scenario as executed with producer trace and rendered output.

**Worker files:** `tests/InventoryWorldBuilder.cs`, `tests/InventoryFixtureMutationTests.cs`.

**Serialized integration files:** `tests/Program.cs`, `route-specific existing tests named by the mapped findings`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-01, E-Q7-02, E-Q7-10, E-Q7-19.

**Evidence:** `tests/EngineQ5Tests.cs`; `tests/GalfreyTricksterTests.cs`; `tests/NurahTricksterTests.cs`; `tests/Nm1BudgetTests.cs`; `tests/ArsinoeTricksterTests.cs`; `src/Story.cs:Complete, ChoiceAvailable, PresenceWanted, PlanPresence`.

**Mapped findings:** `areelu:007`, `areelu:008`, `arsinoe:002`, `camellia:041`, `camellia:042`, `galfrey:007`, `gesmerha:009`, `gesmerha:010`, `hepzamirah:006`, `irabeth:010`, `irabeth:011`, `jannah:004`, `kaylessa:002`, `kiana:007`, `mielarah:024`, `minagho-and-chivarro:036`, `minagho-and-chivarro:037`, `nocticula:020`, `nurah:004`, `shamira:015`, `wenduag:054`, `wenduag:055`.

### E-Q7-10 — Bind optional native history and native outcome alternatives accurately

Impact **600** = 15 routes × 40 severity; **25 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Populate q6b native_facts with concrete positive cue/answer/quest/item/etude evidence. Distinguish a whole dialog from its optional conversation, completed objective alternatives, release-before-kill chronology, correct-password destruction, both Areelu ascent producers, and actual branch provenance. Validate prerequisite combinations against native producer path/chapter windows (including Azata-only histories required alongside current Trickster). Do not invent facts or make optional history mandatory for an otherwise valid route; offer history-neutral text when absent.

**q6 coverage:** engine-q6b native_facts — covered; native path and outcome producer validation extends table acceptance

**Audit origin routes/counts:** areelu (1), arueshalae (1), devarra (1), eritrice (1), galfrey (1), herrax (2), horzalah (1), iomedae (1), kaylessa (1), kiana (1), minagho-and-chivarro (3), nenio (6), nocticula (1), soana (2), vellexia (2). Affected routes: areelu, arueshalae, devarra, eritrice, galfrey, herrax, horzalah, iomedae, kaylessa, kiana, minagho-and-chivarro, nenio, nocticula, soana, vellexia.

**Acceptance:** Separate native fixtures for each positive and negative witness: ascend_areelu/all vs alone/companions; Devarra wrong password vs deliberate destruction/watch; Soana murder request present/absent; Ulbrig powers cue vs dialog-only; Nenio bite/name/refusal answers; Herrax palace/Dyunk unresolved; Fool King rejected/crowned/gone; Vellexia release before vs after kill; Kaylessa conceal vs genuine investigation; native Minagho prison witness vs terrified-only. A native Azata-only searching etude must not be fabricated as a current-Trickster producer. Missing witnesses receive neutral prose or explicit report findings.

**Worker files:** `tests/NativeFactInventoryTests.cs`, `tools/native_fact_inventory_expectations.json`.

**Serialized integration files:** `q6b-owned native_facts table/report files`, `storylines/trickster_world.py`, `src/Story.cs`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: engine-q6b. Related: E-Q7-12.

**Evidence:** `src/Story.cs:SeenCues/SelectedAnswers/StartedDialogs/QuestObjectives/InventoryItems/Etudes`; `storylines/trickster_world.py:native readers`; `tests/NativeReaderTests.cs`; `tests/AreeluTricksterTests.cs`; `tests/StartedDialogTests.cs`.

**Mapped findings:** `areelu:006`, `arueshalae:007`, `devarra:001`, `eritrice:013`, `galfrey:009`, `herrax:003`, `herrax:005`, `horzalah:024`, `iomedae:004`, `kaylessa:004`, `kiana:008`, `minagho-and-chivarro:003`, `minagho-and-chivarro:022`, `minagho-and-chivarro:023`, `nenio:031`, `nenio:032`, `nenio:033`, `nenio:037`, `nenio:038`, `nenio:039`, `nocticula:001`, `soana:001`, `soana:002`, `vellexia:001`, `vellexia:002`.

### E-Q7-09 — Complete the native contradiction inventory and reviewed text/slide overrides

Impact **400** = 10 routes × 40 severity; **45 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Populate the in-flight native_overrides registry/report with every cited native cue, answer and slide dependency on an authored return, body state, recovery, recruitment or continued rule. Preserve identifiers, native actions and continuations; apply only to the earned Trickster world. Reports must enumerate uncovered siblings and every native outcome, not merely the main route ending. Route writers supply labelled, plausible replacement text once the contracts exist.

**q6 coverage:** engine-q6b native_overrides,native contradiction report — covered; populate all cited native dependencies, do not create a second registry

**Audit origin routes/counts:** anevia (1), areelu (5), herrax (2), horzalah (2), irabeth (5), kiana (24), mielarah (1), minagho-and-chivarro (1), terendelev (3), wenduag (1). Affected routes: anevia, areelu, herrax, horzalah, irabeth, kiana, mielarah, minagho-and-chivarro, terendelev, wenduag.

**Acceptance:** The registry report lists each cited GUID and its earned-state dependency, including Areelu spell cues, Kiana Q3 branches, Herrax refusal, Horzalah Greybor/evil-Arueshalae slides, Tirabade widow/morale slides, Terendelev scale/claw/mourning and Wenduag ascension. Each has an evaluated override/reconciliation or remains an explicit failing uncovered entry. Verify untouched off-Trickster/unearned native content, native continuation/actions, save IDs and outcome selection using serialized native fixtures.

**Worker files:** `tests/NativeContradictionInventoryTests.cs`, `tools/native_inventory_expectations.json`.

**Serialized integration files:** `q6b-owned native_overrides registry/report files`, `src/NativeDialogEdit.cs`, `src/NativeEpilogueEdit.cs`, `src/Story.cs`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: engine-q6b. Related: E-Q7-28, E-Q7-32.

**Evidence:** `src/Story.cs:NativeEpilogueEdits, NativeGates and reviewed registries`; `src/NativeDialogEdit.cs`; `src/NativeEpilogueEdit.cs`; `storylines/kiana_native.py`; `storylines/areelu_afterlogue.py`; `storylines/terendelev_trickster.py`.

**Mapped findings:** `anevia:001`, `areelu:001`, `areelu:002`, `areelu:003`, `areelu:004`, `areelu:005`, `herrax:001`, `herrax:002`, `horzalah:001`, `horzalah:002`, `irabeth:002`, `irabeth:003`, `irabeth:004`, `irabeth:005`, `irabeth:006`, `kiana:009`, `kiana:010`, `kiana:011`, `kiana:012`, `kiana:013`, `kiana:014`, `kiana:015`, `kiana:016`, `kiana:017`, `kiana:018`, `kiana:019`, `kiana:020`, `kiana:021`, `kiana:022`, `kiana:023`, `kiana:024`, `kiana:025`, `kiana:026`, `kiana:027`, `kiana:028`, `kiana:029`, `kiana:030`, `kiana:031`, `kiana:032`, `mielarah:002`, `minagho-and-chivarro:005`, `terendelev:001`, `terendelev:002`, `terendelev:003`, `wenduag:001`.

### E-Q7-04 — Read current participant presence, including confinement and solo pair states

Impact **320** = 8 routes × 40 severity; **34 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Map existing recruitment, plot absence, loss, return, closure and confinement/release evidence into reusable participant readers. Apply q6a L1 to choices, nodes, paragraphs, Books and journals, not only scene owners. Distinguish historical presence from current contact and present-tense remote portrayal. Use per-woman membership for paired Guest List/Last Call entries rather than assuming both women from a solo commitment.

**q6 coverage:** engine-q6a L1 — covered lint class; confinement, male reactors and paired-person consumers require explicit coverage

**Audit origin routes/counts:** chadali (1), hepzamirah (2), herrax (11), horzalah (2), melazmera (7), mielarah (4), minagho-and-chivarro (2), wenduag (5). Affected routes: chadali, hepzamirah, herrax, horzalah, melazmera, mielarah, minagho-and-chivarro, wenduag.

**Acceptance:** Negative fixtures for never-recruited Lann/Woljif/Regill/Greybor/Arueshalae; death/dismissal/plot absence after earlier contact; Hepzamirah returned then confined or departed; Vellexia returned then left; Chivarro left while Minagho commits solo. Assert every nominated consumer and UI availability reads the current participant state. Earned return may lift its matching loss; bare native death checks must not reject a valid return.

**Worker files:** `tools/participant_inventory_contracts.json`, `tests/ParticipantInventoryTests.cs`.

**Serialized integration files:** `tools/crossroute_lint.py`, `storylines/trickster_world.py`, `storylines/household.py`, `src/Story.cs`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: engine-q6a. Related: E-Q7-01, E-Q7-06.

**Evidence:** `src/Story.cs:ParticipantsAvailable, RouteOpen, DerivedOpenRoutes`; `storylines/trickster_world.py:companion readers`; `tools/earned_presence_lint.py:EP5/P1 limits`; `storylines/hepzamirah_flesh.py:confinement/release`.

**Mapped findings:** `chadali:003`, `hepzamirah:003`, `hepzamirah:004`, `herrax:010`, `herrax:011`, `herrax:012`, `herrax:013`, `herrax:014`, `herrax:015`, `herrax:016`, `herrax:017`, `herrax:018`, `herrax:019`, `herrax:020`, `horzalah:022`, `horzalah:023`, `melazmera:001`, `melazmera:002`, `melazmera:004`, `melazmera:005`, `melazmera:006`, `melazmera:007`, `melazmera:008`, `mielarah:003`, `mielarah:004`, `mielarah:005`, `mielarah:006`, `minagho-and-chivarro:032`, `minagho-and-chivarro:033`, `wenduag:041`, `wenduag:042`, `wenduag:043`, `wenduag:044`, `wenduag:047`.

### E-Q7-02 — Deliver one usable actor through hidden-native and native/copy transitions

Impact **275** = 5 routes × 55 severity; **25 findings** (0 draft). Status: `partially_covered_existing_dead_original_fix`.

**Build/check:** Make spawn-copy planning, actor observation and failure observation agree on usable contact. A hidden living native must not silently suppress both placement and fallback. Reconcile an owned copy when native Q3 creates the real actor; maintain one usable hub without resurrecting, deleting or adopting arbitrary native actors. Preserve the existing dead-original disambiguation fix.

**q6 coverage:** new — runtime presence/contact transition repair

**Audit origin routes/counts:** gesmerha (4), jannah (3), kiana (5), shamira (12), wenduag (1). Affected routes: gesmerha, jannah, kiana, shamira, wenduag.

**Acceptance:** Replay hidden, displaced, dead, hostile, missing-anchor, copy-dead and native-after-copy observations for Gesmerha/Jannah/Shamira/Kiana. Assert exactly one intended usable actor or an accurate failure result, location compliance and idempotence across ticks/load. Two usable actors must remain ambiguous until the owned-copy transition resolves them. Existing ContactDisambiguationTests must continue accepting dead original + live copy; Wenduag #27 is already covered by that implementation in this snapshot.

**Worker files:** `src/GuestPresence.cs`, `src/NativeContact.cs`, `tests/PresenceTransitionInventoryTests.cs`.

**Serialized integration files:** `src/Story.cs`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-03, E-Q7-29.

**Evidence:** `src/GuestPresence.cs:Observe, Tick`; `src/Story.cs:PlanPresence, PresenceFailed, SingleUsable`; `src/NativeContact.cs:IsAvailable`; `tests/ContactDisambiguationTests.cs`; `tests/PresenceTests.cs`.

**Mapped findings:** `gesmerha:001`, `gesmerha:002`, `gesmerha:003`, `gesmerha:004`, `jannah:001`, `jannah:002`, `jannah:003`, `kiana:002`, `kiana:003`, `kiana:004`, `kiana:005`, `kiana:006`, `shamira:001`, `shamira:002`, `shamira:003`, `shamira:004`, `shamira:005`, `shamira:006`, `shamira:007`, `shamira:008`, `shamira:009`, `shamira:010`, `shamira:011`, `shamira:012`, `wenduag:027`.

### E-Q7-01 — Paid returns and solo contacts must bootstrap before route-open

Impact **216** = 6 routes × 36 severity; **29 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Replace the Aranka-only return-in-progress exception with explicit, per-person, earned bootstrap declarations. Use existing paid/raised/delivered/pardoned flags only; retain closure and unrelated loss guards. Separate a paired route's contact eligibility from pair commitment so a living/returned solo woman can deliver her already-authored scenes. Add a dependency-cycle lint from scene return producers through ContactUnit, Presences and DerivedOpenRoutes.

**q6 coverage:** engine-q6a L1 — partial: reports presence leaks, not paid-return dependency cycles

**Audit origin routes/counts:** camellia (2), galfrey (6), irabeth (2), kaylessa (1), minagho-and-chivarro (16), nurah (2). Affected routes: camellia, galfrey, irabeth, kaylessa, minagho-and-chivarro, nurah.

**Acceptance:** For Camellia, Irabeth, Kaylessa, Nurah and Minagho/Chivarro, traverse the actual paid producer, compute route state, plan the actor and obtain contact before returned/released is set. Every promised physical bootstrap and missing-anchor fallback must work; an unpaid, closed or unreturned unrelated actor must not. For Galfrey validate the actual exported remote/physical variants, not obsolete contact assumptions. A deliberately circular fixture must fail the new lint.

**Worker files:** `tools/presence_dependency_lint.py`, `tests/PresenceBootstrapInventoryTests.cs`, `tests/test_presence_dependency_lint.py`.

**Serialized integration files:** `storylines/earned_presence.py`, `src/Story.cs`, `expansion.py`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: engine-q6a. Related: E-Q7-13, E-Q7-02.

**Evidence:** `storylines/earned_presence.py:PRESENCE_RETURN_IN_PROGRESS and presence_guards`; `src/Story.cs:RouteOpen, PresenceWanted, ContactAvailable`; `tools/earned_presence_lint.py:P1`; `tests/EngineQ5Tests.cs:Aranka-specific guard`.

**Mapped findings:** `camellia:002`, `camellia:003`, `galfrey:001`, `galfrey:002`, `galfrey:003`, `galfrey:004`, `galfrey:005`, `galfrey:006`, `irabeth:007`, `irabeth:008`, `kaylessa:001`, `minagho-and-chivarro:006`, `minagho-and-chivarro:007`, `minagho-and-chivarro:008`, `minagho-and-chivarro:009`, `minagho-and-chivarro:010`, `minagho-and-chivarro:011`, `minagho-and-chivarro:012`, `minagho-and-chivarro:013`, `minagho-and-chivarro:014`, `minagho-and-chivarro:015`, `minagho-and-chivarro:016`, `minagho-and-chivarro:017`, `minagho-and-chivarro:018`, `minagho-and-chivarro:019`, `minagho-and-chivarro:020`, `minagho-and-chivarro:021`, `nurah:001`, `nurah:002`.

### E-Q7-06 — Check own-life and closure guards on every consumer, including epilogues

Impact **200** = 5 routes × 40 severity; **19 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Extend earned-presence validation beyond committed pages with registered return overrides. Cover unclaimed/refused/parted pages, device scenes, all paragraph/Book consumers and path exclusions. Prove current life separately from romance eligibility; a closed but living woman may have an independent ending, whereas a living romantic continuation may not bypass closure. Check terminal Q3/HelloAgain choices explicitly.

**q6 coverage:** engine-q6a L1,L4 — partial: explicit own-route loss/closure sweep extends other-woman presence and late eligibility

**Audit origin routes/counts:** anevia (2), camellia (1), devarra (2), minagho-and-chivarro (6), wenduag (8). Affected routes: anevia, camellia, devarra, minagho-and-chivarro, wenduag.

**Acceptance:** Play commitment/refusal/terms followed by native execution, dismissal, Swarm exclusion or authored breakup. Render every listed consumer and test guest/coda/call/physical presence after Rules.Complete. Continuing romance must disappear; independent historical consequences remain. Wenduag Guest List #34 must also be tested against the existing DerivedOpenRoutes implementation rather than assuming it is absent.

**Worker files:** `tools/own_life_lint.py`, `tools/own_life_contracts.json`, `tests/OwnLifeInventoryTests.cs`.

**Serialized integration files:** `tools/earned_presence_lint.py`, `storylines/earned_presence.py`, `src/Story.cs`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: engine-q6a. Related: E-Q7-11, E-Q7-04.

**Evidence:** `src/Story.cs:Available returns early for Epilogue owners`; `src/Story.cs:RouteOpen, Blocks`; `tools/earned_presence_lint.py:EP5 only covers a narrower class`; `storylines/earned_presence.py:own_loss_guards`.

**Mapped findings:** `anevia:003`, `anevia:004`, `camellia:008`, `devarra:005`, `devarra:006`, `minagho-and-chivarro:024`, `minagho-and-chivarro:025`, `minagho-and-chivarro:026`, `minagho-and-chivarro:027`, `minagho-and-chivarro:028`, `minagho-and-chivarro:029`, `wenduag:028`, `wenduag:029`, `wenduag:030`, `wenduag:031`, `wenduag:032`, `wenduag:033`, `wenduag:034`, `wenduag:035`.

### E-Q7-18 — Verify elapsed-time claims and binding timing contracts by producer history

Impact **160** = 8 routes × 20 severity; **40 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Add explicit timing contracts for the cited quantified callbacks and existing binding route windows. Compute earliest arrival through real producer chains and timestamp-aware delays/OR groups; enforce minimum mourning intervals and separate post-Coronation maximum, not only total campaign time. Calendar/season assertions without a witness are reported. A route may remove or qualify an unsupported duration instead of adding a wait; this backlog grants no new time-advance mechanic.

**q6 coverage:** new — temporal claim/branch contract lint and earliest-time tests

**Audit origin routes/counts:** anevia (2), camellia (9), eliandra (3), eritrice (1), herrax (2), mielarah (3), nenio (19), seelah (1). Affected routes: anevia, camellia, eliandra, eritrice, herrax, mielarah, nenio, seelah.

**Acceptance:** The audited Anevia 204-hour post-Coronation chain fails the 168-hour maximum and 78-hour widow commitment fails its 168-hour minimum. Camellia week/month/anniversary claims and late payments, Nenio newly created week/three-week/year claims, Mielarah 84-hour week claim, Seelah 24-hour week, Herrax yesterday/tomorrow windows and Eliandra same-visit/winter claims are checked against their actual origins. Test declared contracts with timestamps missing/future and both OR producers. Never demand every legitimate gated outcome fit every itinerary.

**Worker files:** `tools/timeline_contract_lint.py`, `tools/timeline_contracts.json`, `tests/test_timeline_contract_lint.py`, `tests/TimelineInventoryTests.cs`.

**Serialized integration files:** `tools/rrt_verify.py`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-12, E-Q7-17.

**Evidence:** `src/Story.cs:Available delay clock and ContactWindowsAvailable`; `tools/rrt_verify.py:chapter/delay reachability`; `tests/AneviaTricksterTests.cs`; `tests/CamelliaTricksterTests.cs`; `tests/NenioTricksterTests.cs`.

**Mapped findings:** `anevia:009`, `anevia:010`, `camellia:022`, `camellia:023`, `camellia:024`, `camellia:025`, `camellia:026`, `camellia:027`, `camellia:028`, `camellia:029`, `camellia:030`, `eliandra:031`, `eliandra:032`, `eliandra:033`, `eritrice:012`, `herrax:008`, `herrax:009`, `mielarah:016`, `mielarah:017`, `mielarah:021`, `nenio:006`, `nenio:011`, `nenio:012`, `nenio:015`, `nenio:016`, `nenio:019`, `nenio:020`, `nenio:021`, `nenio:022`, `nenio:023`, `nenio:024`, `nenio:025`, `nenio:026`, `nenio:027`, `nenio:028`, `nenio:029`, `nenio:030`, `nenio:047`, `nenio:048`, `seelah:004`.

### E-Q7-15 — Validate chapter, area, hub and delivery staging on every branch

Impact **160** = 4 routes × 40 severity; **17 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Use q6a L3 with explicit venue contracts for named physical encounters and traveling companion hubs. Check remote/manual-read paths too: Remote does not move the Commander. Distinguish Chapter 5 Drezen visits, Chapter 6 Threshold aftermath and visitors confined to Drezen from native companions able to march to Threshold. Existing Areas/chapter/Kind tools suffice for route fixes once the lint identifies them.

**q6 coverage:** engine-q6a L3 — covered; include manual remote reads, paragraphs and copy/native variants

**Audit origin routes/counts:** hepzamirah (2), horzalah (6), melazmera (4), nenio (5). Affected routes: hepzamirah, horzalah, melazmera, nenio.

**Acceptance:** Hepzamirah body/courier must not stage Drezen at the Labyrinth; Melazmera Nenio hub must reject outside-Drezen and hunt_found must not claim off-island travel when read on Colyphyr; Horzalah Chapter 6 retries and ending callbacks use the actual location; Nenio Last Call distinguishes Threshold companion from Drezen visitor. Evaluate every incoming branch/paragraph with a location witness or variant and reject a known contradictory venue contract.

**Worker files:** `tools/location_inventory_contracts.json`, `tests/LocationInventoryTests.cs`.

**Serialized integration files:** `tools/crossroute_lint.py`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: engine-q6a. Related: E-Q7-12.

**Evidence:** `src/Story.cs:Available Areas/Chapters and IsRemote`; `storylines/scene_kinds.py`; `storylines/horzalah_trickster.py`; `storylines/melazmera_hoard.py`; `storylines/nenio_folios.py`.

**Mapped findings:** `hepzamirah:001`, `hepzamirah:002`, `horzalah:036`, `horzalah:037`, `horzalah:038`, `horzalah:039`, `horzalah:040`, `horzalah:041`, `melazmera:003`, `melazmera:009`, `melazmera:010`, `melazmera:011`, `nenio:002`, `nenio:003`, `nenio:004`, `nenio:017`, `nenio:018`.

### E-Q7-11 — Qualify an earned return by the loss it actually overrides

Impact **120** = 3 routes × 40 severity; **17 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Add shared provenance validation for UnavailableOverrides and ForbidOverrides. One resurrection must not override a later, different execution merely because a generic returned latch survives. Camellia's battlefield and coffin-return producers must remain distinct and every veiled-copy/card consumer must read the appropriate completed return. Check subsequent loss transitions instead of only static dead+returned snapshots; add no new revival opportunity.

**q6 coverage:** new — loss/return provenance lint and sequential-history tests

**Audit origin routes/counts:** camellia (17). Affected routes: camellia, nurah, seelah.

**Acceptance:** Traverse battlefield death -> overacting -> commitment/terms -> native FinalTruth execution. No coffin return has been earned: all living endings, mourning-attendance paragraphs, presence, Regill reactions, Nurah cards/dispatch alternatives, guest/seating and Last Call are withheld. Traverse the genuine coffin ritual separately and allow only its intended consumers. Include explicit refusal followed by another unreturned death.

**Worker files:** `tools/return_provenance_lint.py`, `tools/return_provenance_contracts.json`, `tests/ReturnProvenanceInventoryTests.cs`.

**Serialized integration files:** `storylines/earned_presence.py`, `src/Story.cs`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-06, E-Q7-12.

**Evidence:** `src/Story.cs:Blocks, UnavailableOverrides, ForbidHolds`; `storylines/camellia_trickster.py:return producers`; `tests/CamelliaTricksterTests.cs:World and second-death fixtures`; `storylines/nurah_trickster.py:Camellia consumers`.

**Mapped findings:** `camellia:001`, `camellia:004`, `camellia:005`, `camellia:006`, `camellia:007`, `camellia:009`, `camellia:010`, `camellia:011`, `camellia:012`, `camellia:013`, `camellia:014`, `camellia:015`, `camellia:016`, `camellia:017`, `camellia:018`, `camellia:019`, `camellia:020`.

### E-Q7-08 — Enforce live Trickster at new canon-changing acts and alterations

Impact **120** = 3 routes × 40 severity; **12 findings** (0 draft). Status: `partially_covered_existing_T6_T7`.

**Build/check:** Map the audit class to q6a L6 and existing T6/T7. Check every new return/rescue/commitment producer, active altered presence and native rewrite against the live path contract. Retain the documented distinction between historical earned facts and new acts: do not erase a woman who already returned or refund an already paid price merely because the path later changes. Resolve any stricter route-specific native/presence contract explicitly.

**q6 coverage:** engine-q6a L6 — covered; existing T6/T7 implement part of the class

**Audit origin routes/counts:** iomedae (3), mielarah (1), wenduag (8). Affected routes: iomedae, mielarah, wenduag.

**Acceptance:** Start from real primers/bargains, then fail Trickster or convert at the Summit before the new Iomedae/Mielarah/Wenduag act. No new canon change can occur. Test all native edit When alternatives and choice OR gates, not just Requires. Separately test history after an already-completed earned return; q6a must not demand blanket trickster.now on every historical consumer. Wenduag return producers already include trickster.now in this snapshot; retain those tests.

**Worker files:** `tools/current_act_inventory_contracts.json`, `tests/CurrentActInventoryTests.cs`.

**Serialized integration files:** `tools/crossroute_lint.py`, `tools/earned_presence_lint.py`, `storylines/trickster_world.py`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: engine-q6a. Related: E-Q7-09, E-Q7-26.

**Evidence:** `expansion.py:trickster_engine, trickster_now_setups`; `tools/earned_presence_lint.py:T6/T7`; `tests/CurrentPathTests.cs`; `tests/EngineQ5Tests.cs:earned-return history invariant`.

**Mapped findings:** `iomedae:001`, `iomedae:002`, `iomedae:003`, `mielarah:001`, `wenduag:002`, `wenduag:003`, `wenduag:004`, `wenduag:005`, `wenduag:006`, `wenduag:007`, `wenduag:008`, `wenduag:009`.

### E-Q7-17 — Enforce per-woman rest-page budgets across alternate branches and auxiliary owners

Impact **120** = 3 routes × 40 severity; **9 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Extend existing pacing/mailbag checks with the binding remote-delivery ledger and actual traversed histories. Count one character's pages across relationship/owner aliases, refusal/loss branches and fallback twins; mutually exclusive alternatives count once per run. Check chapter allocations/whitelists and fold/retire only as authorized by the route findings. Do not raise limits to make a failing route pass.

**q6 coverage:** new — branch-aware character allocation lint; existing pacing lint checks different rules

**Audit origin routes/counts:** irabeth (1), shamira (2), wenduag (6). Affected routes: irabeth, shamira, wenduag.

**Acceptance:** Replay Irabeth departure letters, all Shamira refusals including shamira_barracks, and Wenduag killed/abyss/street/orchard/courtship roads. Detect the audited Ch3 third page, Ch4 zero-allocation violations, Ch5 tier-A overrun, Irabeth tier-A one-letter overrun and Shamira tier-B third page. Include source-of-truth ledger row in each failure, while accepting mutually exclusive fallback deliveries and allocated Memory/Table pages.

**Worker files:** `tools/remote_allocation_lint.py`, `tools/remote_allocation_contracts.json`, `tests/test_remote_allocation_lint.py`.

**Serialized integration files:** `tools/rrt_verify.py`, `tests/Program.cs`, `tests/route delivery walkers`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-12, E-Q7-36.

**Evidence:** `tools/pacing_lint.py:H1-H4 do not enforce these ledger totals`; `tools/rrt_verify.py:E9 simulator/rotation keys`; `src/Story.cs:NextRemoteBag`; `tests/Nm1BudgetTests.cs`; `tests/ShamiraTricksterTests.cs`.

**Mapped findings:** `irabeth:009`, `shamira:014`, `shamira:016`, `wenduag:048`, `wenduag:049`, `wenduag:050`, `wenduag:051`, `wenduag:052`, `wenduag:053`.

### E-Q7-32 — Extend reconciliation coverage to objects, native actors/actions and journal facts

Impact **120** = 3 routes × 40 severity; **7 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Extend q6b only where the current text/slide registry lacks necessary types: reviewed object/spawner/native-action visibility and state-dependent quest/objective localization. Eliandra's completed burial must hide precisely the four corpse displays; Minagho's earned recruitment must retire the contradictory native prison actor/escape faction sequence; full Kiana recovery must reconcile the five journal facts while preserving Q3 progress and unrelated content. Preserve native behavior outside earned Trickster states.

**q6 coverage:** engine-q6b native_overrides,native contradiction report — journal objectives are covered explicitly; native object/spawner/action targets extend q6b only if unsupported, not a second registry

**Audit origin routes/counts:** eliandra (1), kiana (5), minagho-and-chivarro (1). Affected routes: eliandra, kiana, minagho-and-chivarro.

**Acceptance:** Serialized/native fixtures verify Eliandra buried toggles only Regnard/Taeriell/Vestari/Cristry objects after area reload; recruited Minagho does not spawn the old hostile prison sequence; Kiana full recovered patients produce accurate quest/objective descriptions before and after quest start. Partial recovery preserves unrecovered souls and native quest actions. Unearned/off-Trickster states keep original visibility/actions/text.

**Worker files:** `src/NativeWorldReconciliation.cs`, `tests/NativeWorldReconciliationInventoryTests.cs`.

**Serialized integration files:** `q6b-owned native override registry target schema`, `src/Story.cs`, `src/Main.cs`, `tests/Program.cs`.

**Dependency order:** E-Q7-09, E-Q7-14. External: engine-q6b. Related: none.

**Evidence:** `src/Story.cs:NativeEpilogueEdits/NativeGates only reviewed target contracts`; `src/NativeQ3Recovery.cs`; `storylines/eliandra_trickster.py:buried`; `storylines/minagho_chivarro_trickster.py:recruitment`; `/work/Writer/drafts/engine-inventory-input.json:cited native mechanics/objectives`.

**Mapped findings:** `eliandra:025`, `kiana:033`, `kiana:034`, `kiana:035`, `kiana:036`, `kiana:037`, `minagho-and-chivarro:004`.

### E-Q7-07 — Normalize earned Last Call, coda and Ledger entitlement readers

Impact **120** = 3 routes × 40 severity; **6 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Make the shared Last Call contract consistently accept early OR genuinely earned late commitment while retaining open-route/refusal/life checks. Read the actual paid stake rather than an optional discussion of it. Validate call-specific objects and preparations without turning the page, cairn or a promise alone into entitlement.

**q6 coverage:** engine-q6a L4 — partial: late eligibility covered; shared call/coda/Ledger producer parity must be checked

**Audit origin routes/counts:** anevia (1), nenio (4), wenduag (1). Affected routes: anevia, nenio, wenduag.

**Acceptance:** Anevia and Nenio codas accept their traversed earned late fallback without committed; rejected/closed/lost runs do not. Nenio NAME_GONE from the real native producer selects call, paragraph, Book and journal without after_enigma. Wenduag constructed-cairn-only or stay-dead histories never grant a partner call. Check snapshots after derived completion.

**Worker files:** `tools/lastcall_entitlement_lint.py`, `tests/LastCallEntitlementInventoryTests.cs`.

**Serialized integration files:** `storylines/lastcall.py`, `storylines/trickster_world.py`, `tools/crossroute_lint.py`, `tests/Program.cs`.

**Dependency order:** E-Q7-31, E-Q7-06. External: engine-q6a. Related: none.

**Evidence:** `storylines/lastcall.py:generated calls and codas`; `storylines/trickster_world.py:late_committed/callable`; `src/Story.cs:DerivedOpenRoutes`.

**Mapped findings:** `anevia:011`, `nenio:041`, `nenio:042`, `nenio:043`, `nenio:044`, `wenduag:036`.

### E-Q7-31 — Validate every earned late-commitment producer against current eligibility

Impact **120** = 3 routes × 40 severity; **6 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Map to q6a L4. Test that stale terms, preparation or earlier commitment never create a new postwar yes after refusal, closure, terminal loss, inhuman exclusion or unreconciled departure. Check Derived/DerivedForbids and all page/choice consumers. Respect earned fallbacks and existing reconciliations; do not add new ones or force every run to yes.

**q6 coverage:** engine-q6a L4 — covered; includes authored refusal/departure and transformed-Commander states

**Audit origin routes/counts:** devarra (1), kaylessa (1), minagho-and-chivarro (4). Affected routes: devarra, kaylessa, minagho-and-chivarro.

**Acceptance:** Devarra tested then Swarm earns no late commitment; Kaylessa eligible then declines leaves no committed household entitlement before the existing second offer; Minagho/Chivarro terms or WAITING plus leave-her-gone do not grant pair intimacy without WON_BACK or with an unreturned dead Minagho. Tests must traverse each actual negative producer and retain valid earned late roads.

**Worker files:** `tools/late_entitlement_inventory_contracts.json`, `tests/LateEntitlementInventoryTests.cs`.

**Serialized integration files:** `tools/crossroute_lint.py`, `storylines/trickster_world.py`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: engine-q6a. Related: E-Q7-06, E-Q7-27.

**Evidence:** `storylines/trickster_world.py:late_committed Derived entries`; `src/Story.cs:DerivedOpenRoutes and Epilogue availability`; `storylines/minagho_chivarro_trickster.py:WON_BACK/ABSENT_CHIV`.

**Mapped findings:** `devarra:007`, `kaylessa:014`, `minagho-and-chivarro:030`, `minagho-and-chivarro:031`, `minagho-and-chivarro:034`, `minagho-and-chivarro:035`.

### E-Q7-16 — Read actual finale world facts in endings

Impact **120** = 3 routes × 40 severity; **4 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Use q6a L5 with native-facts-backed finale contracts: Wound closed vs Crossroads transformed, true-Aeon rewritten family history, ruler/abdication and continuing Council meetings. Check all paragraph alternatives and native sequence combinations. Do not repair an off-Trickster contradiction by rewriting native canon there.

**q6 coverage:** engine-q6a L5 — covered; native provenance comes from q6b

**Audit origin routes/counts:** chadali (2), irabeth (1), kaylessa (1). Affected routes: chadali, irabeth, kaylessa.

**Acceptance:** Native Ending_TricksterFull/allplanes facts select no false Wound-closure statement in either Chadali wager paragraph or Kaylessa declined page. True-AeonFinalWorld never combines native unmarried Irabeth/dead Anevia with a restored marriage. Ongoing Council/world references require compatible finale evidence. Verify normal closed-Wound and earned Trickster-alteration variants independently.

**Worker files:** `tools/epilogue_world_inventory_contracts.json`, `tests/WorldFactInventoryTests.cs`.

**Serialized integration files:** `tools/crossroute_lint.py`, `storylines/trickster_world.py`, `tests/Program.cs`.

**Dependency order:** E-Q7-10. External: engine-q6a. Related: none.

**Evidence:** `expansion.py:TRICKSTER_ETUDES`; `storylines/trickster_world.py:ending readers`; `src/Story.cs:NativeEpilogueSequences`; `storylines/chadali_wagers.py`; `storylines/kaylessa_trickster.py`.

**Mapped findings:** `chadali:001`, `chadali:002`, `irabeth:001`, `kaylessa:003`.

### E-Q7-21 — Detect embedded Commander speech, tooling residue and gender assumptions

Impact **110** = 5 routes × 22 severity; **38 findings** (18 draft). Status: `gap_confirmed`.

**Build/check:** Add a shared player-text scan for explicitly narrated Commander replies, internal identifiers, mod/handler/observer/native/parent/book-event terminology and explicit gendered Commander references without tags. Scan nodes, choices, paragraphs, Books/journals and drafts, report exact matches with narrow documented exceptions. Include the writing guide's therapy-term counts/budgets as review warnings; semantic fourth-wall, villain/therapy/maxim/heat judgments remain human route review. Do not pretend a keyword list judges voice or automatic consent.

**q6 coverage:** new — missing explicit embedded-speech/meta/gender checks

**Audit origin routes/counts:** arsinoe (18), galfrey (8), kaylessa (1), terendelev (10), wenduag (1). Affected routes: arsinoe, galfrey, kaylessa, terendelev, wenduag.

**Acceptance:** Report all 18 Arsinoe scripted replies, Galfrey hidden-penalty draft variants, Terendelev implementation-facing draft passages, Wenduag native/mod-romance wording and Kaylessa male-Commander line. Controls containing an actual in-world draft/order, native-born usage, third-party he/she or a legitimate quoted Commander answer pass via context/approved exception. No automated rewrite deletes words like you ask inside a genuine question (Nocticula grammar findings stay ROUTE).

**Worker files:** `tools/player_text_lint.py`, `tools/player_text_exceptions.json`, `tests/test_player_text_lint.py`.

**Serialized integration files:** `tools/rrt_verify.py`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-20, E-Q7-22.

**Evidence:** `tools/rrt_verify.py:existing narration lint has no embedded-speech/meta/gender class`; `/work/Writer/handoffs/00-WRITING-GUIDE.md:section 3`; `storylines/terendelev_continuation.py`.

**Mapped findings:** `arsinoe:055`, `arsinoe:056`, `arsinoe:057`, `arsinoe:058`, `arsinoe:059`, `arsinoe:060`, `arsinoe:061`, `arsinoe:062`, `arsinoe:063`, `arsinoe:064`, `arsinoe:065`, `arsinoe:066`, `arsinoe:067`, `arsinoe:068`, `arsinoe:069`, `arsinoe:070`, `arsinoe:071`, `arsinoe:072`, `galfrey:024`, `galfrey:025`, `galfrey:026`, `galfrey:027`, `galfrey:028`, `galfrey:029`, `galfrey:030`, `galfrey:031`, `kaylessa:018`, `terendelev:013`, `terendelev:022`, `terendelev:025`, `terendelev:033`, `terendelev:035`, `terendelev:036`, `terendelev:038`, `terendelev:039`, `terendelev:040`, `terendelev:044`, `wenduag:039`.

### E-Q7-29 — Expose earned cross-route reactions on custom presence hubs

Impact **90** = 5 routes × 18 severity; **5 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Introduce a reviewed native-list-to-presence-hub attachment map or shared inheritance helper. A reaction advertised as supporting recreated Nenio must be discoverable through both real visitor hubs, not only pass loss overrides against an absent native companion list. Retain area/contact/return and speaker requirements; avoid global duplicate entry injection.

**q6 coverage:** new — custom-hub attachment support/attachment coverage lint

**Audit origin routes/counts:** nenio (5). Affected routes: areelu, eritrice, melazmera, nenio, nocticula.

**Acceptance:** Spawn Nenio primary and arcade visitors, enumerate their actual hub entries and traverse the five Nocticula/Eritrice/Areelu/Melazmera reactions. Each eligible reaction is selectable exactly once; unavailable speakers, invalid area or unearned return block it. Native Nenio's own list retains its valid existing entries.

**Worker files:** `tools/hub_attachment_lint.py`, `tests/PresenceReactionHubInventoryTests.cs`.

**Serialized integration files:** `src/GuestPresence.cs`, `src/Story.cs`, `expansion.py`, `tests/Program.cs`.

**Dependency order:** E-Q7-02, E-Q7-04. External: none. Related: none.

**Evidence:** `src/Story.cs:EntryTargets, IsPresenceHub`; `src/GuestPresence.cs:custom Dialog attachment`; `storylines/nenio_trickster.py:primary/arcade hubs`.

**Mapped findings:** `nenio:050`, `nenio:051`, `nenio:052`, `nenio:053`, `nenio:054`.

### E-Q7-23 — Report dead obligation flags and missing negative-condition producers

Impact **69** = 3 routes × 23 severity; **5 findings** (2 draft). Status: `gap_confirmed`.

**Build/check:** Add focused producer/consumer diagnostics for declared obligation/deferred-work flags and referenced forbids that have no producer. A promise flag with no consumer needs either the promised payoff or an acknowledged resolution; pure archival choice records may have an explicit exemption. This is a lint/report, not a request for new quests or automatic reward.

**q6 coverage:** new — rrt_verify currently hard-fails selected required producer gaps, not forbid-only or dead obligations

**Audit origin routes/counts:** eritrice (2), terendelev (2), wenduag (1). Affected routes: eritrice, terendelev, wenduag.

**Acceptance:** Report Eritrice aid_first/refused_to_lie_for_her with no payoff reader, Terendelev more_evidence/new.courtship.deferred with no reopening/resolution, and Wenduag known.lann used without a producer/binding. Trace actual consumers, including paragraph/Book/journal gates. Ignore explicitly historical archival records and retained stubs; deterministic fixtures distinguish absent consumer from a reachable existing resolution.

**Worker files:** `tools/obligation_flow_lint.py`, `tools/obligation_flow_contracts.json`, `tests/test_obligation_flow_lint.py`.

**Serialized integration files:** `tools/rrt_verify.py`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-22.

**Evidence:** `tools/rrt_verify.py:no_producer_required filtering`; `storylines/eritrice_council.py`; `storylines/terendelev_continuation.py`; `storylines/wenduag_trickster.py:secret.wenduag_cairn`.

**Mapped findings:** `eritrice:006`, `eritrice:009`, `terendelev:031`, `terendelev:042`, `wenduag:020`.

### E-Q7-27 — Lint mandatory existing consequence and refusal/control gates at their consumers

Impact **60** = 3 routes × 20 severity; **9 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Declare the already-authored gate contracts for Jannah refusal repairs, Mielarah discovered attempted sacrifice/Oskel settlement and Nenio isolation control. Check every producer and every optional flirt/test outcome consumer, rather than only the main commitment scene. Report bypassing branch edges. Add no repair condition, price, attraction rule or new gate beyond those stated in the findings.

**q6 coverage:** engine-q6a L4 — covered explicitly by q6a task: Jannah romantic responses and Nenio control violation; add existing Mielarah gate contracts and acceptance fixtures, not a second lint

**Audit origin routes/counts:** jannah (4), mielarah (2), nenio (3). Affected routes: jannah, mielarah, nenio.

**Acceptance:** Hold Jannah's lie/unrepaired muster refusal: blade/watch/wings/your_part cannot grant the four romantic responses before their existing repairs. Discover Mielarah's attempted sacrifice through either market twin: commitment requires the promised existing Oskel settlement. Start Nenio's isolated test, play pulse/kiss, then finish: the clean result cannot be earned on any native/visitor/arcade variant. Paid page absence alone is not a defect when the gate is legitimate.

**Worker files:** `tools/earned_outcome_inventory_contracts.json`, `tests/EarnedOutcomeInventoryTests.cs`.

**Serialized integration files:** `tools/crossroute_lint.py`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: engine-q6a. Related: E-Q7-31, E-Q7-12.

**Evidence:** `storylines/jannah_circle.py:DECLINED and repairs`; `storylines/mielarah_deck.py:worked_out/cost.meant/oskel_settled`; `storylines/nenio_trickster.py:test/pulse/RESULT_CLEAN`.

**Mapped findings:** `jannah:005`, `jannah:006`, `jannah:007`, `jannah:008`, `mielarah:007`, `mielarah:008`, `nenio:008`, `nenio:009`, `nenio:010`.

### E-Q7-14 — Keep authored native-gate declarations and runtime contracts in sync

Impact **55** = 1 routes × 55 severity; **1 findings** (0 draft). Status: `audited_partial_group_not_in_snapshot`.

**Build/check:** Validate supported q3_recovery outcome groups against the runtime adapter's reviewed contract before export; align Python and C# validation and partial-vs-full recovery behavior. Preserve native quest progression and unrecovered patients. The audited partial group is absent from this integration export, so verify the route merge rather than weakening the validator or reintroducing that group blindly.

**q6 coverage:** new — adapter/schema parity; q6b registry reports can expose unsupported targets

**Audit origin routes/counts:** kiana (1). Affected routes: kiana.

**Acceptance:** Generate every supported full and partial Kiana recovery group and run Rules.Validate plus the adapter selection. Unsupported groups fail before publication; supported partial rescue must not revive or recover unrelated patients. An integration-only native gate with ransom/buy-back must keep passing. Main.Load and offline validation agree.

**Worker files:** `tests/NativeGateContractParityTests.cs`, `tools/native_gate_contract_lint.py`.

**Serialized integration files:** `src/NativeQ3Recovery.cs`, `src/NativeGate.cs`, `src/Story.cs`, `tools/rrt_verify.py`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: none.

**Evidence:** `src/Story.cs:ValidateNativeGates`; `src/NativeQ3Recovery.cs`; `storylines/kiana_native.py:kiana.q3_recovery`; `src/Main.cs:Load validation`.

**Mapped findings:** `kiana:001`.

### E-Q7-05 — Validate Commander survival inside every epilogue text block

Impact **40** = 1 routes × 40 severity; **4 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Extend q6a L2 and EP1/EP2/EP6 to living paragraphs appended to mourning/allowlisted pages, including every sibling continuation. A scene-level sacrifice requirement does not prove its paragraphs are mourning. Declare living/mourning/independent block contracts and check actual rendered output; preserve historical facts and independent consequences after sacrifice.

**q6 coverage:** engine-q6a L2 — covered; require paragraph-level and allowlist coverage

**Audit origin routes/counts:** anevia (4). Affected routes: anevia.

**Acceptance:** Render all four Anevia ending_sacrifice continuations after physical and correspondence late gates, both-women returns and widow terms. With sacrifice and no earned commander_back, no spring reunion, shared bed or ongoing living partner renders. Earned return variants remain reachable, and the native historical-return correction is still selectable via the bereavement variant.

**Worker files:** `tools/commander_block_contracts.json`, `tests/CommanderParagraphInventoryTests.cs`.

**Serialized integration files:** `tools/crossroute_lint.py`, `tools/earned_presence_lint.py`, `storylines/earned_presence.py`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: engine-q6a. Related: E-Q7-28.

**Evidence:** `storylines/earned_presence.py:COMMANDER_ABSENT, PARAGRAPH_GUARDED`; `tools/earned_presence_lint.py:EP1-EP6`; `src/Story.cs:VisibleParagraphs, Available`.

**Mapped findings:** `anevia:005`, `anevia:006`, `anevia:007`, `anevia:008`.

### E-Q7-28 — Cover native replacement selection after survival, refusal and sacrifice

Impact **40** = 1 routes × 40 severity; **1 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Add q6b selection coverage over original cue plus all When/replacement-scene gates. An earned historical return must remain reflected in the native slide even if the Commander dies or reconciliation is refused; supply a reviewed bereavement/survival variant instead of falling back to a false native death. Preserve the existing Available-aware variant selector.

**q6 coverage:** engine-q6b native_overrides,native contradiction report — covered registry class; add selection-state coverage rather than another selector

**Audit origin routes/counts:** anevia (1). Affected routes: anevia.

**Acceptance:** Anevia Cue_0311 with returned Anevia, dead native Beth and unreturned Commander sacrifice selects a historical-survival bereavement correction, not the untouched widow-original or living reunion. Include Irabeth survived without returned and all relevant native original cues; test sacrifice with and without a genuinely earned Commander return and unchanged native worlds.

**Worker files:** `tests/NativeVariantCoverageInventoryTests.cs`, `tools/native_variant_inventory_contracts.json`.

**Serialized integration files:** `q6b-owned native override coverage report`, `tests/TirabadeNativeSlideTests.cs`, `tests/Program.cs`.

**Dependency order:** E-Q7-09, E-Q7-05. External: engine-q6b. Related: none.

**Evidence:** `src/Story.cs:SelectNativeEditVariant with Available`; `src/NativeEpilogueEdit.cs`; `tests/TirabadeNativeSlideTests.cs`.

**Mapped findings:** `anevia:002`.

### E-Q7-03 — Persist observed placement failure for promised finale fallbacks

Impact **26** = 1 routes × 26 severity; **4 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Keep transient presence.failed for current-area observation. Add a saved, route-scoped receipt only after an eligible placement actually failed, with an explicit lifecycle; finale fallbacks consume the receipt instead of fabricating transient observations at Threshold. Never make never-visited or unpaid content eligible.

**q6 coverage:** new — saved placement-failure evidence

**Audit origin routes/counts:** gesmerha (4). Affected routes: gesmerha.

**Acceptance:** Observe a wanted failed Gesmerha presence in Drezen, travel to Threshold, reload and complete derived state. The promised commitment/mourning fallback remains selectable, unvisited variants do not contradict it, and no failure receipt appears for an unwanted or unattempted placement.

**Worker files:** `tests/PresenceFailureReceiptTests.cs`, `tools/presence_failure_lint.py`.

**Serialized integration files:** `src/GuestPresence.cs`, `src/Story.cs`, `src/Main.cs`, `tests/Program.cs`.

**Dependency order:** E-Q7-02. External: none. Related: none.

**Evidence:** `src/Story.cs:PresenceFailed explicitly transient`; `src/GuestPresence.cs:Tick clears area observations`; `storylines/gesmerha_trickster.py:epilogue failure consumers`.

**Mapped findings:** `gesmerha:005`, `gesmerha:006`, `gesmerha:007`, `gesmerha:008`.

### E-Q7-20 — Make narration-span diagnostics exhaustive and actionable

Impact **24** = 2 routes × 12 severity; **67 findings** (17 draft). Status: `gap_confirmed`.

**Build/check:** Strengthen the existing advisory rrt_verify narration/formatting checks: tokenize nested/order/balance of {n} spans, inspect inline narration after quoted speech, paragraphs and choice text, and run against unregistered draft data too. Machine-detectable spans are ENGINE even though repairs are prose-only. Keep intentional action answers valid. Emit exact scene/node/span diagnostics and fail structural tag errors; ambiguous narration remains a targeted review diagnostic.

**q6 coverage:** new — insufficient existing advisory formatter

**Audit origin routes/counts:** arsinoe (48), terendelev (19). Affected routes: arsinoe, terendelev.

**Acceptance:** Every audited Arsinoe narration span and Terendelev orphan closer is reported with the correct node/span; an unmatched closer before an opener and balanced-count-but-reversed tags fail. Valid Owlcat speech/action/narration and gender tags pass. Drafts remain separate from shipped scores but are inspected without registration or ID mutation.

**Worker files:** `tools/text_structure_lint.py`, `tests/test_text_structure_lint.py`.

**Serialized integration files:** `tools/rrt_verify.py`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-21, E-Q7-22.

**Evidence:** `tools/rrt_verify.py:narration_lint and formatting_by_file are advisory, count-only`; `story_format.py:n and c`; `storylines/arsinoe_campaign.py`; `storylines/terendelev_continuation.py`.

**Mapped findings:** `arsinoe:007`, `arsinoe:008`, `arsinoe:009`, `arsinoe:010`, `arsinoe:011`, `arsinoe:012`, `arsinoe:013`, `arsinoe:014`, `arsinoe:015`, `arsinoe:016`, `arsinoe:017`, `arsinoe:018`, `arsinoe:019`, `arsinoe:020`, `arsinoe:021`, `arsinoe:022`, `arsinoe:023`, `arsinoe:024`, `arsinoe:025`, `arsinoe:026`, `arsinoe:027`, `arsinoe:028`, `arsinoe:029`, `arsinoe:030`, `arsinoe:031`, `arsinoe:032`, `arsinoe:033`, `arsinoe:034`, `arsinoe:035`, `arsinoe:036`, `arsinoe:037`, `arsinoe:038`, `arsinoe:039`, `arsinoe:040`, `arsinoe:041`, `arsinoe:042`, `arsinoe:043`, `arsinoe:044`, `arsinoe:045`, `arsinoe:046`, `arsinoe:047`, `arsinoe:048`, `arsinoe:049`, `arsinoe:050`, `arsinoe:051`, `arsinoe:052`, `arsinoe:053`, `arsinoe:054`, `terendelev:010`, `terendelev:011`, `terendelev:047`, `terendelev:048`, `terendelev:049`, `terendelev:050`, `terendelev:051`, `terendelev:052`, `terendelev:053`, `terendelev:054`, `terendelev:055`, `terendelev:056`, `terendelev:057`, `terendelev:058`, `terendelev:059`, `terendelev:060`, `terendelev:061`, `terendelev:062`, `terendelev:063`.

### E-Q7-25 — Implement the promised Nenio original-body custody transition

Impact **18** = 1 routes × 18 severity; **1 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Add a narrow runtime adapter for the already-playable retained-body recreation branch: define original-body custody, equipment and native resurrection access postconditions and keep the new visitor distinct. If the adapter cannot be completed, retire the unsupported branch by gating while retaining IDs/answers; do not narrate an action the engine did not perform.

**q6 coverage:** new — runtime companion body/inventory capability, not replacement prose

**Audit origin routes/counts:** nenio (1). Affected routes: nenio.

**Acceptance:** Walk Nenio dead.the_price retained-body branch, then inspect original entity, dead-party/resurrection selectors, equipment and visitor copy before/after reload. The promised custody transition happens once, never creates a duplicate companion or silently deletes equipment, and refusal/unearned/off-path histories preserve native state. Explicitly document failure behavior.

**Worker files:** `src/NenioBodyCustody.cs`, `tests/NenioBodyCustodyTests.cs`.

**Serialized integration files:** `src/Main.cs`, `src/Story.cs`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-02.

**Evidence:** `storylines/nenio_trickster.py:dead.the_price retained-body branch`; `src/Fate.cs`; `src/Main.cs:dead unit lifecycle`.

**Mapped findings:** `nenio:007`.

### E-Q7-13 — Export bootstrap exceptions so standalone lint and C# agree

Impact **16** = 1 routes × 16 severity; **3 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Use a single serialized declaration of return-in-progress exceptions instead of generation-time mutation of a Python module-global registry. Read it identically in expansion, standalone lint and managed rules validation; remove hardcoded Aranka-only test expectations. A declared exception still needs the earned flag and reason and must preserve closure.

**q6 coverage:** new — cross-process validation parity

**Audit origin routes/counts:** nenio (3). Affected routes: nenio.

**Acceptance:** Generate Nenio probation guards, start a fresh Python process and validate the export; load the same export in C#. Native Aranka and declared Nenio exceptions both pass, an undeclared/arbitrary loss bypass fails, and declaring an exception does not grant presence before its earned producer. Validate actual snapshot coverage before adding a declaration: this integration export currently has only the Aranka DerivedForbids exception.

**Worker files:** `tools/presence_exception_schema.py`, `tests/test_presence_exception_export.py`, `tests/PresenceExceptionExportTests.cs`.

**Serialized integration files:** `storylines/earned_presence.py`, `tools/earned_presence_lint.py`, `src/Story.cs`, `tests/EngineQ5Tests.cs`, `tests/Program.cs`.

**Dependency order:** E-Q7-01. External: none. Related: none.

**Evidence:** `storylines/earned_presence.py:PRESENCE_RETURN_IN_PROGRESS`; `tools/earned_presence_lint.py:imports module registry`; `tests/EngineQ5Tests.cs:rel == aranka assertion`.

**Mapped findings:** `nenio:055`, `nenio:056`, `nenio:057`.

### E-Q7-30 — Make Wenduag casualty actions occur at the earned native moment

Impact **15** = 1 routes × 15 severity; **2 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Inventory the remaining native-kill/custody/journey seam of the already-approved Wenduag unit. Use its existing nonfatal/native moment adapter and paid/earned custody states; reject later rest pages that perform burial/rescue actions in a completed morning/Abyss encounter. Wire the exact native hook and custody transition or retire the unsupported replay by gating; no retrospective choices or new rescue premise.

**q6 coverage:** new — follow-up/acceptance of existing Wenduag unit, not a new echo or route redesign

**Audit origin routes/counts:** wenduag (2). Affected routes: wenduag.

**Acceptance:** Traverse actual native kill hooks with primer/page/nonfatal substitution as appropriate, verify casualty evidence and custody before departure, and inspect both prepared and unprepared fall pages. Once the native moment is completed with no earned intervention, later pages cannot newly bury/rescue/pay for an action in the past. Explicit player kill/terminal closures remain closed; refusal is legitimate. Validate off-path inactivity and save/load across custody.

**Worker files:** `tests/WenduagNativeMomentInventoryTests.cs`.

**Serialized integration files:** `src/WenduagEcho.cs`, `src/Story.cs`, `storylines/wenduag_echo.py`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-33, E-Q7-26.

**Evidence:** `src/WenduagEcho.cs:casualty/return adapters and destination TODO`; `storylines/wenduag_echo.py:earned custody states`; `storylines/wenduag_trickster.py:abyss.fall/street.fall`; `/work/Writer/handoffs/LOOP-3-HANDOFF.md:pilot v2/Wenduag unit`.

**Mapped findings:** `wenduag:012`, `wenduag:013`.

### E-Q7-24 — Verify declared intimate cuts have a reachable morning and consequence

Impact **12** = 1 routes × 12 severity; **9 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Add structural intimate-beat contracts for the nine named Camellia scenes and their all/mine/knife branches. Test that the cut reaches an authored morning and an outcome-specific existing/newly-authorized local consequence or reaction. Quality of heat, morning prose and voice remains ROUTE review; no generic morning text, new attraction requirement or shared romance gate is prescribed.

**q6 coverage:** new — missing structural aftermath acceptance check

**Audit origin routes/counts:** camellia (9). Affected routes: camellia.

**Acceptance:** Each bond/card/dance variant and declaration has a traversed path from intimate cut to morning, and a reachable later reader of its encounter outcome; deleting the morning edge or callback makes the contract test fail. Non-intimate/refusal terminals are exempt. Keep every old terminal/node and choice index save-safe.

**Worker files:** `tools/intimacy_contract_lint.py`, `tools/intimacy_contracts.json`, `tests/test_intimacy_contract_lint.py`.

**Serialized integration files:** `tools/rrt_verify.py`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-12.

**Evidence:** `storylines/camellia_cards.py`; `storylines/camellia_days.py`; `storylines/camellia_trickster.py`; `/work/Writer/TRICKSTER-RUBRIC.md:Directive 12`.

**Mapped findings:** `camellia:032`, `camellia:033`, `camellia:034`, `camellia:035`, `camellia:036`, `camellia:037`, `camellia:038`, `camellia:039`, `camellia:040`.

### E-Q7-26 — Validate sold-memory callbacks and preserve the existing echo discipline

Impact **12** = 1 routes × 12 severity; **4 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Extend the current echo()/gap() tests with the four cited Terendelev restitution/third-bell consumers, all incoming choices and memory-price histories. Reuse gap() and the allocation registry; no new echo slot or rescue device is authorized. Add a callback contract/report for unguarded sold sensory memories and guard drift across twins.

**q6 coverage:** new — coverage gap in existing foresight/gap discipline

**Audit origin routes/counts:** terendelev (4). Affected routes: terendelev.

**Acceptance:** Sell memory.square, never hear the Storyteller voice vision, and traverse both restitution hosts and both third-bell twins: no eyewitness sensory recollection is supplied. Unsold/heard variants remain valid. Existing tests must retain paid page + live path gates, allocated echo-only delivery, unique sense/misstep, caps 8/1/2, misreading cost, no decisive outcome Set and unchanged ordinary choices. Text scan reports explicit vision/another-life justification for human review; the page alone never earns an outcome.

**Worker files:** `tools/memory_callback_lint.py`, `tools/memory_callback_contracts.json`, `tests/test_memory_callback_lint.py`.

**Serialized integration files:** `tests/test_foresight_echo.py`, `tests/test_foresight_echo.py:gap fixtures`, `storylines/foresight.py`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-21, E-Q7-08.

**Evidence:** `storylines/foresight.py:gap, integrate_gaps, ALLOCATED, echo`; `tests/test_foresight_echo.py`; `tests/test_wenduag_echo.py`; `/work/Writer/handoffs/06-ROUTE-REGISTRY.md:Echo slots`.

**Mapped findings:** `terendelev:004`, `terendelev:005`, `terendelev:006`, `terendelev:007`.

### E-Q7-19 — Persist failed-check liabilities through generated payment exits

Impact **12** = 1 routes × 12 severity; **1 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Define and test the lifecycle of obligations already stated by an authored resource transaction. A failed haggle's surcharge must be recorded when it is incurred, not only when it is paid; the generated insufficient-funds exit must not let a reopened scene reroll or sign at the original price. Use existing resource costs and amounts; do not add a new cost.

**q6 coverage:** new — transaction/exit safety test and lint

**Audit origin routes/counts:** arsinoe (1). Affected routes: arsinoe.

**Acceptance:** Arsinoe exactly-500-Finances history: pay initial charge, fail haggle, take generated Leave, reopen. Liability remains; no cheap Agreed or reroll bypass. Test each success/failure, insufficient funds, return and settlement branch with ChoiceAvailable and actual Resource deltas. The original negotiated total stays unchanged.

**Worker files:** `tools/transaction_exit_lint.py`, `tests/TransactionExitInventoryTests.cs`.

**Serialized integration files:** `src/Main.cs:AddPaymentExit`, `src/Story.cs`, `tests/Program.cs`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-12.

**Evidence:** `src/Main.cs:AddPaymentExit`; `src/Story.cs:ChoiceAvailable, Crusade changes`; `storylines/arsinoe_trickster.py:lease/raised`.

**Mapped findings:** `arsinoe:001`.

### E-Q7-22 — Validate every unregistered draft graph and delivery contract without publishing it

Impact **0** = 2 routes × 0 severity; **14 findings** (14 draft). Status: `gap_confirmed`.

**Build/check:** Promote existing optional --drafts diagnostics into a separate deterministic authoring check. Check node reachability, unreachable completion producers, no-attachment physical entries, integration conflicts and deferred-once scenes that close before their required action. Do not register dormant drafts, build their deferred devices or replace shipped relationships. Preserve retired/save-referenced nodes through explicit gated-stub exemptions.

**q6 coverage:** new — existing draft check is optional and its failures do not enter strict hard total

**Audit origin routes/counts:** galfrey (8), terendelev (6). Affected routes: galfrey, terendelev.

**Acceptance:** Galfrey literal start/no-attachment drafts and Terendelev inspection/vigil/aftercare/scale unreachable end nodes/integration conflict are reported independently of native delivery deferrals. A valid dormant draft passes; an explicitly retired stub stays legal. The check runs in a system-temp copy, deletes it and never leaves tools/scratch or tests artifacts.

**Worker files:** `tools/draft_contract_lint.py`, `tests/test_draft_contract_lint.py`.

**Serialized integration files:** `tools/rrt_verify.py`.

**Dependency order:** independent standalone work; shared wiring after q6 merge. External: none. Related: E-Q7-23, E-Q7-20.

**Evidence:** `tools/rrt_verify.py:check_drafts uses tools/scratch and default strict excludes draft errors`; `src/Story.cs:EntryTargets and Validate unreachable-node check`; `storylines/terendelev_continuation.py:integrate`; `storylines/galfrey_all_path_continuation.py`.

**Mapped findings:** `galfrey:032`, `galfrey:033`, `galfrey:034`, `galfrey:035`, `galfrey:036`, `galfrey:037`, `galfrey:038`, `galfrey:039`, `terendelev:021`, `terendelev:026`, `terendelev:028`, `terendelev:032`, `terendelev:045`, `terendelev:046`.

### E-Q7-33 — Resolve and validate the live locator/position TODOs

Impact **0** = 4 routes × 0 severity; **0 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Record verified, chapter-aware walkable placements in a shared manifest, using the existing presence/destination APIs. Wenduag's cellar destination is deliberately null; do not guess coordinates or bypass the failed return. Recheck Wenduag street f8cfa132 and Devarra d7aa4429 on Chapter 5, then remaining Galfrey sergeant/hub-title and Chadali fallback checks. Record expected anchor failure and relocation after reload.

**q6 coverage:** new — handoff-only live data/acceptance work

**Audit origin routes/counts:** handoff-only; no audit finding. Affected routes: chadali, devarra, galfrey, wenduag.

**Acceptance:** Coordinator supplies a Chapter 5 save/scene evidence and runs the existing walkable-mesh probe; verified cellar journey/return/contact succeeds on a copy save, unsafe coordinates fail closed, and primary/fallback anchors resolve only in their chapter/area. Gate the manifest deterministically against GUID/type/chapter and recorded probe evidence. No game/harness is run by this inventory task.

**Worker files:** `tools/presence_placement_manifest.json`, `tests/PresencePlacementManifestTests.cs`.

**Serialized integration files:** `src/WenduagEcho.cs:TODO_VerifiedCellarPosition`, `storylines/wenduag_trickster.py`, `storylines/devarra_trickster.py`, `tests/Program.cs`.

**Dependency order:** E-Q7-02. External: none. Related: none.

**Evidence:** `src/WenduagEcho.cs:TODO_VerifiedCellarPosition`; `/work/Writer/handoffs/LOOP-3-HANDOFF.md:2026-10-04 04:10 LIVE HARNESS`.

**Mapped findings:** none; handoff-only.

### E-Q7-34 — Provide native epilogue/afterlogue policy fixtures and a live slide driver

Impact **0** = 7 routes × 0 severity; **0 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Add a harness driver that can start the actual RanEpilogue/native sequences and assert original-versus-replacement selection, portrait/image actions, OnShow/OnStop and sequence continuation. Keep fixture tests for known live-only contract failures (Arueshalae dream cue and Tirabade non-sequence pages). This is validation of q6b/runtime support, not new epilogue prose.

**q6 coverage:** engine-q6b native_overrides — partial: registry depends on this runtime acceptance; harness driver is additional

**Audit origin routes/counts:** handoff-only; no audit finding. Affected routes: anevia, areelu, arueshalae, devarra, galfrey, irabeth, kiana.

**Acceptance:** Deterministic serialized cue-policy fixtures must reject the historical Arueshalae Cue_0461 contract failure and accept the reviewed repaired shape, preserve Cue_0310/0311 image/continuation actions and confirm native override fallthrough. Coordinator live run on a finale save proves RanEpilogue selection, no relationship degradation, no missing replacement warning and unchanged native content outside earned states; missing finale save remains explicit evidence debt.

**Worker files:** `harness/Probes/NativeEpilogueInventoryProbe.cs`, `tests/NativeCuePolicyInventoryTests.cs`.

**Serialized integration files:** `harness/ScenarioDriver.cs`, `src/NativeEpilogueEdit.cs`, `tests/Program.cs`.

**Dependency order:** E-Q7-28, E-Q7-32. External: engine-q6b. Related: none.

**Evidence:** `/work/Writer/handoffs/BETA-KNOWN-ISSUES.md:Arueshalae live-only edit failure`; `/work/Writer/handoffs/LOOP-3-HANDOFF.md:slides need RanEpilogue + driver`; `src/NativeEpilogueEdit.cs:cue policy`.

**Mapped findings:** none; handoff-only.

### E-Q7-35 — Close the native-present/contact-rejected harness evidence gap

Impact **0** = 2 routes × 0 severity; **0 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Retain the harness distinction between unforceable native contacts and route delivery failure. Capture unit storage, suppression, hidden/dead/conscious/view/scene-loaded state and anchor/walkability without restoring or awakening actors. Recheck the historical Irabeth contact probe and the corrected Kiana gate oracle; diagnostics must agree with NativeContact rather than fabricating availability.

**q6 coverage:** new — handoff-only contact/oracle regression acceptance, existing diagnostics partly implemented

**Audit origin routes/counts:** handoff-only; no audit finding. Affected routes: irabeth, kiana.

**Acceptance:** Read-only synthetic cases reproduce native-present-but-unusable, cross-scene companion, dead original/live copy, duplicate living twins and insufficient native branch witnesses. Skipped-inline means the harness could not acquire the native contact; an expected usable contact rejected by the mod is a failing oracle. Coordinator rechecks PP8 S1/S8/S20 and the Kiana gate/walkability oracle on correct save copies.

**Worker files:** `harness/Probes/ContactInventoryProbe.cs`, `tests/ContactInventoryOracleTests.cs`.

**Serialized integration files:** `harness/ScenarioDriver.cs`, `src/NativeContact.cs`, `tests/Program.cs`.

**Dependency order:** E-Q7-02. External: none. Related: none.

**Evidence:** `/work/Writer/handoffs/LOOP-3-HANDOFF.md:PP8 S1 contact ambiguity and harness-fix`; `src/NativeContact.cs:HasCurrentStorage`; `tools/probe-cross-scene-contact.py`.

**Mapped findings:** none; handoff-only.

### E-Q7-36 — Validate full-roster Table/mailbag pacing with the approved W0c engine

Impact **0** = 35 routes × 0 severity; **0 findings** (0 draft). Status: `gap_confirmed`.

**Build/check:** Finish the handoff's native-aware E9 acceptance for campaign load, Chapter 4/5 delivery, actual Table beats and per-rest allowances. Use existing ER-H1/H2/H3 and H-1..H-7/A1..A10 implementations; do not redesign household policy or expand approved forms/limits. Check RequiresAnyGroups delay clocks, verified payment witnesses, participant eligibility, first-wins enmity and paid-page stance gating against serialized row data.

**q6 coverage:** new — handoff acceptance completion atop existing W0c, not a new pacing mechanism

**Audit origin routes/counts:** handoff-only; no audit finding. Affected routes: anevia, areelu, arsinoe, arueshalae, camellia, chadali, devarra, eliandra, elyanka-and-camilary, eritrice, galfrey, gesmerha, hepzamirah, herrax, horzalah, iomedae, irabeth, jannah, jerribeth, kaylessa, kiana, konomi, melazmera, mielarah, minagho-and-chivarro, nenio, nocticula, nurah, seelah, shamira, soana, terendelev, vellexia, wenduag, yaniel.

**Acceptance:** Deterministic full-roster run honors Table T1-T8/rest limits, Shyka page absent/present, participant absence/refusal, verified payments, branch clocks and first-wins attitudes. Compare with approved 81 ideal/122 worst campaign ceilings and >=20 Chapter 5 Table rests; refresh retired S46/chapter counts and dynamic-ack/form census. Missing build-sheet inputs remain an explicit data blocker, not a fabricated successful schedule. Keep existing tests passing.

**Worker files:** `tools/harem_inventory_scenarios.json`, `tests/test_harem_inventory_scenarios.py`.

**Serialized integration files:** `tools/harem_rest_sim.py`, `tools/harem-schedule.json`, `tools/harem-smoothing.json`.

**Dependency order:** E-Q7-17, E-Q7-04, E-Q7-18. External: none. Related: none.

**Evidence:** `/work/Writer/handoffs/HAREM-STATUS.md:W0c and v8.1 rulings`; `tools/harem_rest_sim.py`; `tools/harem_schedule_lint.py`; `tools/harem_smoothing_lint.py`; `tests/test_harem_rest_sim.py`.

**Mapped findings:** none; handoff-only.

## Parallel integration and dependency order

Worker files are unique across items. Parallel workers implement standalone lints/contracts/tests and owned runtime modules; the coordinator serializes `src/Story.cs`, `src/Main.cs`, shared storylines, expansion, verifier, test-runner and build wiring. Shared runtime lanes must also serialize their actual adapters: actors → failure receipts → hub inheritance/contact probes; bootstrap → exported registry; q6b native contracts → target/action extensions → selection fixtures → slide driver. Source route fixes remain outside this inventory and go to route owners after shared support.

- Dependency wave 1: E-Q7-12, E-Q7-10, E-Q7-09, E-Q7-04, E-Q7-02, E-Q7-01, E-Q7-06, E-Q7-18, E-Q7-15, E-Q7-11, E-Q7-08, E-Q7-17, E-Q7-31, E-Q7-21, E-Q7-23, E-Q7-27, E-Q7-14, E-Q7-05, E-Q7-20, E-Q7-25, E-Q7-30, E-Q7-24, E-Q7-26, E-Q7-19, E-Q7-22.
- Dependency wave 2: E-Q7-32, E-Q7-07, E-Q7-16, E-Q7-29, E-Q7-28, E-Q7-03, E-Q7-13, E-Q7-33, E-Q7-35, E-Q7-36.
- Dependency wave 3: E-Q7-34.

## Handoff-only live/runtime and already-landed items

This ledger includes completed repairs so older handoff entries do not become duplicate work. Open implementation/validation is linked to the relevant E-Q7 item; completed entries are regression obligations. Operational orchestration (remote login, watchdog, merge queues), pure prose rounds and missing pair build sheets are not new engine mechanics.

| ID | Status | Engine item(s) | Source and obligation |
|---|---|---|---|
| H-01 | fixed_in_snapshot_regression_only | E-Q7-07, E-Q7-04 | BETA-KNOWN-ISSUES.md:items 1/2 and updates: Devarra Last Call no-choice refusal and Elyanka/Seelah earned-return coexistence: handoff says fixed 7b0fc3a. Preserve closure-safe selectable exit/returned participants; do not re-plan the old repairs. |
| H-02 | existing_fix_pending_live_slide_acceptance | E-Q7-34 | BETA-KNOWN-ISSUES.md:Arueshalae live-only dream edit; LOOP-3 later repair: Initial withdrawn Cue_0461 edit was later restored after engine repair; use the latest snapshot, not the obsolete beta package. Validate runtime cue policy with the slide driver. |
| H-03 | implemented_regression_only | E-Q7-12 | LOOP-3:engine-q2 objective restore after return + commitment: Main previously failed objectives on loss without completing restored romance after earned return; q2 repair is already present. Check earned return + commit, negative second loss, and failed objective restoration; no duplicate new restoration mechanic. |
| H-04 | implemented_lifecycle_regression_due | E-Q7-11, E-Q7-06 | LOOP-3:Konomi death latch, return, second death and transient household read: Keep q2/q3/q4 Konomi death/recall lifecycle; verify later death invalidates all current presence, household and postwar reads after refreshed snapshots. A canon-born listed rite is not overridden by an invented one-raise policy. |
| H-05 | implemented_parity_regression_only | E-Q7-22, E-Q7-05 | LOOP-3:conditional paragraphs and ep-allow integration failures: q3 now permits reviewed conditional node paragraphs in both Story.cs and rrt_verify; EP6 still validates paragraph-guarded epilogues. Do not re-plan the historical blanket non-epilogue prohibition. Verify selectable answers on all permitted histories. |
| H-06 | open_live_data | E-Q7-33, E-Q7-30 | LOOP-3:Wenduag cellar null and Ch3 walkability failures: Cellar not found; street/devarra locators fail mesh probe on Ch3 and need Ch5 evidence. Destination must remain fail-closed until verified; no guessed position. |
| H-07 | partly_fixed_live_recheck | E-Q7-35 | LOOP-3:PP8 S1/S8/S20 and ContactProbe: Contact forceability/hidden entry mismatch and cross-scene storage need correct-save, read-only diagnostics; historical skipped-inline is a harness limitation unless probe establishes a real usable actor. |
| H-08 | smoke_passed_oracle_recheck_due | E-Q7-34, E-Q7-35 | LOOP-3:2026-10-04 load smoke and harness-fix: Ch3/Ch6 load smoke 12/12, round-trip 2/2 and quiet copies passed. Kiana branch-gate false positive and walkable probe repaired in a harness-only merge; repeat relevant scenario oracles instead of treating forced state as proof of native history. |
| H-09 | implemented_full_roster_acceptance_due | E-Q7-36 | HAREM-STATUS.md:ER-H1/2/3, H-1..H-7/A1..A10 and LOOP-3 W0c merge: Rest allowances/T1-T8 Table selection, participant guards, E9 sim, payment witnesses, Table-hosted remote visits, paid page stance, row-28 SeenCues, first-wins enmity, S46 retirement, Ch5/dynamic-ack/form census. Use merged W0c; remaining build sheets are inputs, not invented engine mechanics. |
| H-10 | implemented_regression_only | E-Q7-36 | HAREM-STATUS.md:classification/favour/smoothing/form rulings: Arueshalae redeemed/corrupted read-only classification, explicit favourable choice producers, smoothing forms cap 28/42-of-56 baseline and protected row bindings are already implemented. Row 28 is Vellexia patron/Jerribeth client; no story justification can reverse its native witness. Unwritten pair forms/build sheets need coordinator writing/data, not a new mechanic. |
| H-11 | required_gate_regression | E-Q7-12, E-Q7-22 | LOOP-3:no-choice Delamere/build regression and temp hygiene: Required progression must reject Page has no selectable answers; exception print/exit, csproj nested artifact exclusion and temp-dir hygiene repairs already landed. Inventory and draft tooling must use system temp and clean it. No legacy unreleased-save defect is invented. |
| H-12 | implemented_targeted_coverage_due | E-Q7-26, E-Q7-08 | LOOP-3:Shyka merge and CURRENT_PATH_KEYS/gap/echo normalization: Merged paid page/receipt/memory/gate contracts, allocation caps and Wenduag echo binding remain the baseline. Do not allocate declined Devarra/Terendelev colour echoes or treat a vision as an earned rescue. Targeted sold-memory callback coverage remains required. |
| H-13 | existing_typeid_check_regression_only | E-Q7-12 | HAREM-STATUS.md:KonomiMeeting.cs TypeId false positive: A serializer TypeId is not a native asset GUID. Preserve verified TypeId parsing and distinguish missing native targets from type IDs before escalating a build diagnostic. |
| H-14 | existing_overrides_inventory_and_runtime_acceptance | E-Q7-09, E-Q7-34 | BETA-KNOWN-ISSUES.md:native dragon-killed line; LOOP-3:E14i/afterlogue/Kiana wedding-night residuals: Inventory DragonEggs/Cue_0007 in earned flight/clutch worlds, Areelu common-dialogue afterlogue Cue_0004/0005 and Kiana ElandKianaAftermath Cue_0007. Existing native repairs are not a new prose task; migrate identical behavior into q6b and verify every native continuation and live cue-policy contract. |

## Class sweep

Reviewed all 757 problem records and retained every fix/cap; checked generated contracts and ambiguous source families. The sweep covers sibling/twin narration and aftermath; all return/contact bootstrap dependencies; hidden/native/copy/failure transitions; later loss after an earlier return; scene/choice/paragraph/Guest List/seating/Last Call/Book/journal consumers; native cue/answer/slide/objective siblings; early/late/refused/closed/native outcomes; manual remote/location variants; per-woman delivery aliases and earliest-time branches; shipped/dormant graphs and text; sold-memory and allocated echo contracts. This inventory does not claim live Unity execution or a fresh native archive audit.

## Gate results and escalation

- `python expansion.py`: PASS; 2867 scenes generated.
- `python -m unittest discover -s tests -p "test_*.py" -q`: PASS; 204 tests, 5 skipped.
- `python tools/rrt_verify.py --strict`: PASS; 0 hard failures with native archive/localization at /wrath.
- `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json`: PASS; 130732791 assertions; no Page has no selectable answers failure.
- `python tools/rrt_verify.py --strict --no-zip`: PASS; 0 structural hard failures (supplemental, not a substitute for full native verification).

All commands use `PYTHONHASHSEED=0` in a system-temp snapshot of this exact worktree. This avoids editing generated development files or leaving .NET obj/bin, caches or verifier/audit artifacts in the allowed worktree. Source fixes, game-reference assets, live save/locator/epilogue proofs and shared engine changes are coordinator escalations; none are performed by this documentation task.

## Risks and proposals

No unrequested design proposal is implemented. The listed items are the observed mechanism/lint/test gaps or completion of existing handoff acceptance. Text diagnostics do not certify semantic canon, agency, villain voice or heat; those remain route rounds. Branch drift, missing live saves and shared wiring conflicts are explicit limits. No claim that all 35 routes already meet 91 is made.

## Per-finding classification appendix

The JSON contains the complete original quote/fix and available code evidence for each row. `D` marks a dormant draft, still classified but excluded from shipped cap impact.

| Finding ID | Dim | Scene | Class | Primary item |
|---|---|---|---|---|
| anevia:001 | CAN | `NPC_Common/Anevia/Cue_3` | ENGINE | E-Q7-09 |
| anevia:002 | CAN | `Epilogues/Cue_0311` | ENGINE | E-Q7-28 |
| anevia:003 | INT | `anevia.ending_parted` | ENGINE | E-Q7-06 |
| anevia:004 | BEL | `anevia.ending_parted` | ENGINE | E-Q7-06 |
| anevia:005 | COX | `anevia.ending_sacrifice` | ENGINE | E-Q7-05 |
| anevia:006 | COX | `anevia.ending_sacrifice` | ENGINE | E-Q7-05 |
| anevia:007 | COX | `anevia.ending_sacrifice` | ENGINE | E-Q7-05 |
| anevia:008 | COX | `anevia.ending_sacrifice` | ENGINE | E-Q7-05 |
| anevia:009 | HOW | `anevia.trickster.gone.fetched` | ENGINE | E-Q7-18 |
| anevia:010 | HOW | `anevia.trickster.gone.commit` | ENGINE | E-Q7-18 |
| anevia:011 | HOW | `anevia.lastcall.page` | ENGINE | E-Q7-07 |
| areelu:001 | CAN | `areelu.trickster.wager.collect` | ENGINE | E-Q7-09 |
| areelu:002 | CAN | `areelu.trickster.finale.ascended` | ENGINE | E-Q7-09 |
| areelu:003 | CAN | `areelu.trickster.wager.collect` | ENGINE | E-Q7-09 |
| areelu:004 | CAN | `areelu.trickster.afterlogue.former_half_demon` | ENGINE | E-Q7-09 |
| areelu:005 | BEL | `areelu.trickster.wager.collect` | ENGINE | E-Q7-09 |
| areelu:006 | INT | `areelu.trickster.finale.ascended` | ENGINE | E-Q7-10 |
| areelu:007 | HOW | `areelu.trickster.finale.ascended` | ENGINE | E-Q7-12 |
| areelu:008 | HOW | `areelu.trickster.afterlogue.former_half_demon` | ENGINE | E-Q7-12 |
| arsinoe:001 | INT | `arsinoe.trickster.cauldron.lease` | ENGINE | E-Q7-19 |
| arsinoe:002 | HOW | `arsinoe.trickster.cauldron.lease` | ENGINE | E-Q7-12 |
| arsinoe:003 | BEL | `arsinoe.trickster.epilogue.pot_returned` | ROUTE | — |
| arsinoe:004 | BEL | `arsinoe.trickster.epilogue.bill_to_threshold` | ROUTE | — |
| arsinoe:005 | BEL | `arsinoe.trickster.epilogue.pot_returned` | ROUTE | — |
| arsinoe:006 | BEL | `arsinoe.trickster.epilogue.bill_to_threshold` | ROUTE | — |
| arsinoe:007 | VOI | `arsinoe_your_hours` | ENGINE | E-Q7-20 |
| arsinoe:008 | VOI | `arsinoe_your_hours` | ENGINE | E-Q7-20 |
| arsinoe:009 | VOI | `arsinoe_your_hours` | ENGINE | E-Q7-20 |
| arsinoe:010 | VOI | `arsinoe_your_hours` | ENGINE | E-Q7-20 |
| arsinoe:011 | VOI | `arsinoe_borrowed_court` | ENGINE | E-Q7-20 |
| arsinoe:012 | VOI | `arsinoe_borrowed_court` | ENGINE | E-Q7-20 |
| arsinoe:013 | VOI | `arsinoe_borrowed_court` | ENGINE | E-Q7-20 |
| arsinoe:014 | VOI | `arsinoe_borrowed_court` | ENGINE | E-Q7-20 |
| arsinoe:015 | VOI | `arsinoe_borrowed_court` | ENGINE | E-Q7-20 |
| arsinoe:016 | VOI | `arsinoe_price_of_an_evening` | ENGINE | E-Q7-20 |
| arsinoe:017 | VOI | `arsinoe_price_of_an_evening` | ENGINE | E-Q7-20 |
| arsinoe:018 | VOI | `arsinoe_price_of_an_evening` | ENGINE | E-Q7-20 |
| arsinoe:019 | VOI | `arsinoe_price_of_an_evening` | ENGINE | E-Q7-20 |
| arsinoe:020 | VOI | `arsinoe_price_of_an_evening` | ENGINE | E-Q7-20 |
| arsinoe:021 | VOI | `arsinoe_price_of_an_evening` | ENGINE | E-Q7-20 |
| arsinoe:022 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:023 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:024 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:025 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:026 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:027 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:028 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:029 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:030 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:031 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:032 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:033 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:034 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:035 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:036 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:037 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:038 | VOI | `arsinoe_courtyard_company` | ENGINE | E-Q7-20 |
| arsinoe:039 | VOI | `arsinoe_another_hour` | ENGINE | E-Q7-20 |
| arsinoe:040 | VOI | `arsinoe_another_hour` | ENGINE | E-Q7-20 |
| arsinoe:041 | VOI | `arsinoe_another_hour` | ENGINE | E-Q7-20 |
| arsinoe:042 | VOI | `arsinoe_another_hour` | ENGINE | E-Q7-20 |
| arsinoe:043 | VOI | `arsinoe_another_hour` | ENGINE | E-Q7-20 |
| arsinoe:044 | VOI | `arsinoe_another_hour` | ENGINE | E-Q7-20 |
| arsinoe:045 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-20 |
| arsinoe:046 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-20 |
| arsinoe:047 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-20 |
| arsinoe:048 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-20 |
| arsinoe:049 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-20 |
| arsinoe:050 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-20 |
| arsinoe:051 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-20 |
| arsinoe:052 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-20 |
| arsinoe:053 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-20 |
| arsinoe:054 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-20 |
| arsinoe:055 | VOI | `arsinoe_printers_view` | ENGINE | E-Q7-21 |
| arsinoe:056 | VOI | `arsinoe_printers_view` | ENGINE | E-Q7-21 |
| arsinoe:057 | VOI | `arsinoe_printers_view` | ENGINE | E-Q7-21 |
| arsinoe:058 | VOI | `arsinoe_roofs` | ENGINE | E-Q7-21 |
| arsinoe:059 | VOI | `arsinoe_your_hours` | ENGINE | E-Q7-21 |
| arsinoe:060 | VOI | `arsinoe_your_hours` | ENGINE | E-Q7-21 |
| arsinoe:061 | VOI | `arsinoe_your_hours` | ENGINE | E-Q7-21 |
| arsinoe:062 | VOI | `arsinoe_your_hours` | ENGINE | E-Q7-21 |
| arsinoe:063 | VOI | `arsinoe_borrowed_court` | ENGINE | E-Q7-21 |
| arsinoe:064 | VOI | `arsinoe_price_of_an_evening` | ENGINE | E-Q7-21 |
| arsinoe:065 | VOI | `arsinoe_price_of_an_evening` | ENGINE | E-Q7-21 |
| arsinoe:066 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-21 |
| arsinoe:067 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-21 |
| arsinoe:068 | VOI | `arsinoe_the_unprofitable_hour` | ENGINE | E-Q7-21 |
| arsinoe:069 | VOI | `arsinoe_two_doors` | ENGINE | E-Q7-21 |
| arsinoe:070 | VOI | `arsinoe_a_stone_in_hand` | ENGINE | E-Q7-21 |
| arsinoe:071 | VOI | `arsinoe_a_stone_in_hand` | ENGINE | E-Q7-21 |
| arsinoe:072 | VOI | `arsinoe_the_first_cart` | ENGINE | E-Q7-21 |
| arueshalae:001 | CAN | `arueshalae.trickster.chaplain.prayer` | ROUTE | — |
| arueshalae:002 | CAN | `arueshalae.treatment.alushinyrra` | ROUTE | — |
| arueshalae:003 | CAN | `arueshalae.treatment.alushinyrra_drezen` | ROUTE | — |
| arueshalae:004 | CAN | `arueshalae.treatment.relapse_two` | ROUTE | — |
| arueshalae:005 | CAN | `arueshalae.treatment.rainy_day` | ROUTE | — |
| arueshalae:006 | CAN | `arueshalae.treatment.nightmare` | ROUTE | — |
| arueshalae:007 | INT | `arueshalae.treatment.nightmare` | ENGINE | E-Q7-10 |
| arueshalae:008 | BEL | `arueshalae.trickster.fallen.house_call` | ROUTE | — |
| arueshalae:009 | INT | `arueshalae.lastcall.page` | ROUTE | — |
| camellia:001 | TRK | `camellia.trickster.dead.overacting` | ENGINE | E-Q7-11 |
| camellia:002 | INT | `camellia.trickster.killed.performance` | ENGINE | E-Q7-01 |
| camellia:003 | INT | `camellia.trickster.killed.performance_letter` | ENGINE | E-Q7-01 |
| camellia:004 | COX | `camellia.trickster.epilogue.kept` | ENGINE | E-Q7-11 |
| camellia:005 | COX | `camellia.trickster.epilogue.kept_on_record` | ENGINE | E-Q7-11 |
| camellia:006 | COX | `camellia.trickster.epilogue.commit` | ENGINE | E-Q7-11 |
| camellia:007 | COX | `camellia.trickster.epilogue.commit_on_record` | ENGINE | E-Q7-11 |
| camellia:008 | COX | `camellia.trickster.epilogue.refused` | ENGINE | E-Q7-06 |
| camellia:009 | COX | `camellia.trickster.react.regill_grave` | ENGINE | E-Q7-11 |
| camellia:010 | COX | `camellia.trickster.react.regill_quarters` | ENGINE | E-Q7-11 |
| camellia:011 | COX | `camellia.lastcall.call` | ENGINE | E-Q7-11 |
| camellia:012 | COX | `camellia.lastcall.page` | ENGINE | E-Q7-11 |
| camellia:013 | COX | `guest.camellia` | ENGINE | E-Q7-11 |
| camellia:014 | COX | `seating.seelah.camellia` | ENGINE | E-Q7-11 |
| camellia:015 | COX | `nurah.trickster.react.camellia_veiled_pardon` | ENGINE | E-Q7-11 |
| camellia:016 | COX | `nurah.trickster.react.camellia_veiled_market` | ENGINE | E-Q7-11 |
| camellia:017 | COX | `nurah.trickster.react.camellia_veiled_supper` | ENGINE | E-Q7-11 |
| camellia:018 | COX | `nurah.trickster.react.camellia_veiled_draft` | ENGINE | E-Q7-11 |
| camellia:019 | COX | `nurah.trickster.after.proofs` | ENGINE | E-Q7-11 |
| camellia:020 | COX | `nurah.trickster.after.proofs` | ENGINE | E-Q7-11 |
| camellia:021 | COX | `camellia.lastcall.page` | ROUTE | — |
| camellia:022 | BEL | `camellia.lastcall.page` | ENGINE | E-Q7-18 |
| camellia:023 | BEL | `camellia.lastcall.call` | ENGINE | E-Q7-18 |
| camellia:024 | BEL | `camellia.lastcall.page` | ENGINE | E-Q7-18 |
| camellia:025 | BEL | `camellia.trickster.evening.the_chaplains_census` | ENGINE | E-Q7-18 |
| camellia:026 | BEL | `camellia.trickster.cards.two_lies_again` | ENGINE | E-Q7-18 |
| camellia:027 | BEL | `camellia.trickster.cards.two_lies_again_camp` | ENGINE | E-Q7-18 |
| camellia:028 | BEL | `camellia.trickster.cards.two_lies_again_alive` | ENGINE | E-Q7-18 |
| camellia:029 | BEL | `camellia.trickster.day.the_anniversary` | ENGINE | E-Q7-18 |
| camellia:030 | BEL | `camellia.trickster.day.the_anniversary_camp` | ENGINE | E-Q7-18 |
| camellia:031 | BEL | `camellia.trickster.day.the_anniversary` | ROUTE | — |
| camellia:032 | VOI | `camellia.trickster.bond.not_today` | ENGINE | E-Q7-24 |
| camellia:033 | VOI | `camellia.trickster.bond.not_today_camp` | ENGINE | E-Q7-24 |
| camellia:034 | VOI | `camellia.trickster.bond.not_today_alive` | ENGINE | E-Q7-24 |
| camellia:035 | VOI | `camellia.trickster.cards.two_lies_again` | ENGINE | E-Q7-24 |
| camellia:036 | VOI | `camellia.trickster.cards.two_lies_again_camp` | ENGINE | E-Q7-24 |
| camellia:037 | VOI | `camellia.trickster.cards.two_lies_again_alive` | ENGINE | E-Q7-24 |
| camellia:038 | VOI | `camellia.trickster.day.the_second_dance` | ENGINE | E-Q7-24 |
| camellia:039 | VOI | `camellia.trickster.day.the_second_dance_camp` | ENGINE | E-Q7-24 |
| camellia:040 | VOI | `camellia.trickster.day.the_second_dance_alive` | ENGINE | E-Q7-24 |
| camellia:041 | HOW | `camellia.trickster.killed.performance` | ENGINE | E-Q7-12 |
| camellia:042 | HOW | `camellia.trickster.dead.overacting` | ENGINE | E-Q7-12 |
| chadali:001 | CAN | `chadali.trickster.epilogue.lucky_night` | ENGINE | E-Q7-16 |
| chadali:002 | CAN | `chadali.trickster.epilogue.lucky_night` | ENGINE | E-Q7-16 |
| chadali:003 | COX | `chadali.trickster.epilogue.lucky_night` | ENGINE | E-Q7-04 |
| chadali:004 | BEL | `chadali.sessions.a_parcel_for_the_shrine` | ROUTE | — |
| devarra:001 | CAN | `devarra.tower.the_messenger_free` | ENGINE | E-Q7-10 |
| devarra:002 | INT | `devarra.tower.smallest_egg` | ROUTE | — |
| devarra:003 | BEL | `devarra.tower.what_she_says` | ROUTE | — |
| devarra:004 | BEL | `devarra.tower.a_story_for_nothing` | ROUTE | — |
| devarra:005 | COX | `devarra.trickster.epilogue.hungry` | ENGINE | E-Q7-06 |
| devarra:006 | INT | `devarra.trickster.epilogue.woken` | ENGINE | E-Q7-06 |
| devarra:007 | TRK | `devarra.trickster.epilogue.commit` | ENGINE | E-Q7-31 |
| eliandra:001 | CAN | `eliandra.trickster.ch4.red_sky` | ROUTE | — |
| eliandra:002 | CAN | `eliandra.trickster.ch4.red_sky` | ROUTE | — |
| eliandra:003 | CAN | `eliandra.trickster.ch4.red_sky` | ROUTE | — |
| eliandra:004 | CAN | `eliandra.trickster.ch5.last_rite` | ROUTE | — |
| eliandra:005 | CAN | `eliandra.trickster.ch5.last_rite_drezen` | ROUTE | — |
| eliandra:006 | CAN | `eliandra.trickster.ch5.last_rite_drezen_mark` | ROUTE | — |
| eliandra:007 | CAN | `eliandra.trickster.ch5.terms` | ROUTE | — |
| eliandra:008 | CAN | `eliandra.trickster.ch5.terms_drezen` | ROUTE | — |
| eliandra:009 | CAN | `eliandra.trickster.ch5.terms_drezen_mark` | ROUTE | — |
| eliandra:010 | CAN | `eliandra.trickster.ch5.last_rite` | ROUTE | — |
| eliandra:011 | CAN | `eliandra.trickster.ch5.last_rite_drezen` | ROUTE | — |
| eliandra:012 | CAN | `eliandra.trickster.ch5.last_rite_drezen_mark` | ROUTE | — |
| eliandra:013 | CAN | `eliandra.trickster.ch5.last_rite` | ROUTE | — |
| eliandra:014 | CAN | `eliandra.trickster.ch5.last_rite_drezen` | ROUTE | — |
| eliandra:015 | CAN | `eliandra.trickster.ch5.last_rite_drezen_mark` | ROUTE | — |
| eliandra:016 | CAN | `eliandra.trickster.ch5.night_after` | ROUTE | — |
| eliandra:017 | VOI | `eliandra.trickster.ch5.last_rite` | ROUTE | — |
| eliandra:018 | VOI | `eliandra.trickster.ch5.last_rite_drezen` | ROUTE | — |
| eliandra:019 | VOI | `eliandra.trickster.ch5.last_rite_drezen_mark` | ROUTE | — |
| eliandra:020 | INT | `eliandra.trickster.ch5.last_rite` | ROUTE | — |
| eliandra:021 | INT | `eliandra.trickster.ch5.last_rite_drezen` | ROUTE | — |
| eliandra:022 | INT | `eliandra.trickster.ch5.last_rite_drezen_mark` | ROUTE | — |
| eliandra:023 | INT | `eliandra.trickster.ch5.packing` | ROUTE | — |
| eliandra:024 | BEL | `eliandra.trickster.ch5.night_after` | ROUTE | — |
| eliandra:025 | INT | `eliandra.trickster.ch5.burial` | ENGINE | E-Q7-32 |
| eliandra:026 | BEL | `eliandra.trickster.ch5.terms` | ROUTE | — |
| eliandra:027 | BEL | `eliandra.trickster.ch5.terms_drezen` | ROUTE | — |
| eliandra:028 | BEL | `eliandra.trickster.ch5.terms_drezen_mark` | ROUTE | — |
| eliandra:029 | BEL | `eliandra.trickster.drezen.city` | ROUTE | — |
| eliandra:030 | BEL | `eliandra.trickster.drezen.city_mark` | ROUTE | — |
| eliandra:031 | BEL | `eliandra.trickster.ch5.night_after` | ENGINE | E-Q7-18 |
| eliandra:032 | BEL | `eliandra.trickster.drezen.dark_sky` | ENGINE | E-Q7-18 |
| eliandra:033 | BEL | `eliandra.trickster.drezen.dark_sky_mark` | ENGINE | E-Q7-18 |
| eliandra:034 | BEL | `eliandra.trickster.drezen.dark_sky` | ROUTE | — |
| eliandra:035 | BEL | `eliandra.trickster.drezen.dark_sky_mark` | ROUTE | — |
| eliandra:036 | BEL | `eliandra.trickster.ch5.first_mile` | ROUTE | — |
| eliandra:037 | BEL | `eliandra.trickster.ch5.first_mile_mark` | ROUTE | — |
| eliandra:038 | BEL | `eliandra.trickster.epilogue.together` | ROUTE | — |
| eliandra:039 | BEL | `eliandra.trickster.epilogue.late` | ROUTE | — |
| eliandra:040 | BEL | `eliandra.trickster.epilogue.unasked` | ROUTE | — |
| elyanka-and-camilary:001 | INT | `elyanka.trickster.beat.inquiry` | ROUTE | — |
| elyanka-and-camilary:002 | BEL | `elyanka.trickster.executor.haggle` | ROUTE | — |
| elyanka-and-camilary:003 | BEL | `elyanka.trickster.beat.inquiry` | ROUTE | — |
| eritrice:001 | BEL | `eritrice.minutes.the_record` | ROUTE | — |
| eritrice:002 | BEL | `eritrice.council.the_lady_in_shadow` | ROUTE | — |
| eritrice:003 | BEL | `eritrice.council.a_sound_proposition` | ROUTE | — |
| eritrice:004 | BEL | `eritrice.council.a_lie_for_the_chair` | ROUTE | — |
| eritrice:005 | BEL | `eritrice.trickster.epilogue.commit` | ROUTE | — |
| eritrice:006 | INT | `eritrice.council.a_sound_proposition` | ENGINE | E-Q7-23 |
| eritrice:007 | INT | `eritrice.council.a_sound_proposition` | ROUTE | — |
| eritrice:008 | INT | `eritrice.council.a_lie_for_the_chair` | ROUTE | — |
| eritrice:009 | INT | `eritrice.council.a_lie_for_the_chair` | ENGINE | E-Q7-23 |
| eritrice:010 | INT | `eritrice.council.a_lie_for_the_chair` | ROUTE | — |
| eritrice:011 | BEL | `eritrice.council.a_motion_to_expel` | ROUTE | — |
| eritrice:012 | BEL | `eritrice.council.just_imagine` | ENGINE | E-Q7-18 |
| eritrice:013 | INT | `eritrice.council.the_motion_to_expel_voted` | ENGINE | E-Q7-10 |
| galfrey:001 | INT | `galfrey.trickster.iz.eulogy` | ENGINE | E-Q7-01 |
| galfrey:002 | INT | `galfrey.trickster.iz.eulogy_stall` | ENGINE | E-Q7-01 |
| galfrey:003 | INT | `galfrey.trickster.return.kitrane` | ENGINE | E-Q7-01 |
| galfrey:004 | INT | `galfrey.trickster.return.kitrane_stall` | ENGINE | E-Q7-01 |
| galfrey:005 | INT | `galfrey.trickster.return.kitrane_scarred` | ENGINE | E-Q7-01 |
| galfrey:006 | INT | `galfrey.trickster.return.kitrane_scarred_stall` | ENGINE | E-Q7-01 |
| galfrey:007 | HOW | `galfrey.trickster.iz.eulogy` | ENGINE | E-Q7-12 |
| galfrey:008 | CAN | `galfrey.lastcall.page` | ROUTE | — |
| galfrey:009 | CAN | `galfrey.lastcall.page` | ENGINE | E-Q7-10 |
| galfrey:010 | COX | `galfrey.lastcall.page` | ROUTE | — |
| galfrey:011 | VOI | `galfrey.lastcall.page` | ROUTE | — |
| galfrey:012 | BEL | `galfrey.trickster.epilogue.estranged` | ROUTE | — |
| galfrey:013 | BEL | `galfrey.trickster.epilogue.queen_bier` | ROUTE | — |
| galfrey:014 | BEL | `galfrey.trickster.commit.release` | ROUTE | — |
| galfrey:015 | BEL | `galfrey.trickster.epilogue.sworn` | ROUTE | — |
| galfrey:016 | VOI D | `galfrey.angel.the_space_between_orders` | ROUTE | — |
| galfrey:017 | VOI D | `galfrey.azata.the_space_between_orders` | ROUTE | — |
| galfrey:018 | VOI D | `galfrey.aeon.the_space_between_orders` | ROUTE | — |
| galfrey:019 | VOI D | `galfrey.trickster.the_space_between_orders` | ROUTE | — |
| galfrey:020 | VOI D | `galfrey.demon.the_space_between_orders` | ROUTE | — |
| galfrey:021 | VOI D | `galfrey.devil.the_space_between_orders` | ROUTE | — |
| galfrey:022 | VOI D | `galfrey.dragon.the_space_between_orders` | ROUTE | — |
| galfrey:023 | VOI D | `galfrey.legend.the_space_between_orders` | ROUTE | — |
| galfrey:024 | BEL D | `galfrey.angel.the_space_between_orders` | ENGINE | E-Q7-21 |
| galfrey:025 | BEL D | `galfrey.azata.the_space_between_orders` | ENGINE | E-Q7-21 |
| galfrey:026 | BEL D | `galfrey.aeon.the_space_between_orders` | ENGINE | E-Q7-21 |
| galfrey:027 | BEL D | `galfrey.trickster.the_space_between_orders` | ENGINE | E-Q7-21 |
| galfrey:028 | BEL D | `galfrey.demon.the_space_between_orders` | ENGINE | E-Q7-21 |
| galfrey:029 | BEL D | `galfrey.devil.the_space_between_orders` | ENGINE | E-Q7-21 |
| galfrey:030 | BEL D | `galfrey.dragon.the_space_between_orders` | ENGINE | E-Q7-21 |
| galfrey:031 | BEL D | `galfrey.legend.the_space_between_orders` | ENGINE | E-Q7-21 |
| galfrey:032 | HOW D | `galfrey.angel.the_space_between_orders` | ENGINE | E-Q7-22 |
| galfrey:033 | HOW D | `galfrey.azata.the_space_between_orders` | ENGINE | E-Q7-22 |
| galfrey:034 | HOW D | `galfrey.aeon.the_space_between_orders` | ENGINE | E-Q7-22 |
| galfrey:035 | HOW D | `galfrey.trickster.the_space_between_orders` | ENGINE | E-Q7-22 |
| galfrey:036 | HOW D | `galfrey.demon.the_space_between_orders` | ENGINE | E-Q7-22 |
| galfrey:037 | HOW D | `galfrey.devil.the_space_between_orders` | ENGINE | E-Q7-22 |
| galfrey:038 | HOW D | `galfrey.dragon.the_space_between_orders` | ENGINE | E-Q7-22 |
| galfrey:039 | HOW D | `galfrey.legend.the_space_between_orders` | ENGINE | E-Q7-22 |
| gesmerha:001 | INT | `gesmerha.trickster.returned.yard` | ENGINE | E-Q7-02 |
| gesmerha:002 | INT | `gesmerha.trickster.returned.bench` | ENGINE | E-Q7-02 |
| gesmerha:003 | INT | `gesmerha.trickster.returned.second_ask` | ENGINE | E-Q7-02 |
| gesmerha:004 | INT | `gesmerha.trickster.returned.likeness` | ENGINE | E-Q7-02 |
| gesmerha:005 | INT | `gesmerha.trickster.epilogue.commit` | ENGINE | E-Q7-03 |
| gesmerha:006 | INT | `gesmerha.trickster.epilogue.commit_mourned` | ENGINE | E-Q7-03 |
| gesmerha:007 | INT | `gesmerha.trickster.epilogue.unvisited` | ENGINE | E-Q7-03 |
| gesmerha:008 | INT | `gesmerha.trickster.epilogue.unvisited_mourned` | ENGINE | E-Q7-03 |
| gesmerha:009 | HOW | `gesmerha.trickster.returned.yard` | ENGINE | E-Q7-12 |
| gesmerha:010 | HOW | `gesmerha.trickster.epilogue.commit` | ENGINE | E-Q7-12 |
| gesmerha:011 | BEL | `gesmerha.trickster.epilogue.bench` | ROUTE | — |
| hepzamirah:001 | CAN | `hepzamirah.trickster.ghost.body` | ENGINE | E-Q7-15 |
| hepzamirah:002 | CAN | `hepzamirah.trickster.body.hounds` | ENGINE | E-Q7-15 |
| hepzamirah:003 | INT | `hepzamirah.trickster.flesh.chaplains` | ENGINE | E-Q7-04 |
| hepzamirah:004 | BEL | `hepzamirah.trickster.body.hounds` | ENGINE | E-Q7-04 |
| hepzamirah:005 | BEL | `hepzamirah.trickster.bond.gift` | ROUTE | — |
| hepzamirah:006 | HOW | `hepzamirah.trickster.flesh.chaplains` | ENGINE | E-Q7-12 |
| herrax:001 | CAN | `herrax.trickster.madam.reachable` | ENGINE | E-Q7-09 |
| herrax:002 | CAN | `herrax.trickster.madam.reachable_restored` | ENGINE | E-Q7-09 |
| herrax:003 | CAN | `herrax.house.the_glowworm` | ENGINE | E-Q7-10 |
| herrax:004 | CAN | `herrax.house.labyrinth` | ROUTE | — |
| herrax:005 | INT | `herrax.house.labyrinth` | ENGINE | E-Q7-10 |
| herrax:006 | INT | `herrax.house.the_stairs` | ROUTE | — |
| herrax:007 | INT | `herrax.trickster.epilogue.after_hours` | ROUTE | — |
| herrax:008 | INT | `herrax.house.eve` | ENGINE | E-Q7-18 |
| herrax:009 | INT | `herrax.house.eve` | ENGINE | E-Q7-18 |
| herrax:010 | INT | `herrax.trickster.react.arueshalae_morning` | ENGINE | E-Q7-04 |
| herrax:011 | INT | `herrax.trickster.react.arueshalae_morning_unheard` | ENGINE | E-Q7-04 |
| herrax:012 | INT | `herrax.trickster.react.arueshalae_knife` | ENGINE | E-Q7-04 |
| herrax:013 | INT | `herrax.trickster.react.regill_night` | ENGINE | E-Q7-04 |
| herrax:014 | INT | `herrax.trickster.react.regill_wrist` | ENGINE | E-Q7-04 |
| herrax:015 | INT | `herrax.trickster.react.woljif_con` | ENGINE | E-Q7-04 |
| herrax:016 | INT | `herrax.trickster.react.woljif_cheek` | ENGINE | E-Q7-04 |
| herrax:017 | INT | `herrax.trickster.react.arueshalae_morning_cut_you` | ENGINE | E-Q7-04 |
| herrax:018 | INT | `herrax.trickster.react.arueshalae_morning_restored` | ENGINE | E-Q7-04 |
| herrax:019 | INT | `herrax.trickster.react.arueshalae_morning_unheard_cut_you` | ENGINE | E-Q7-04 |
| herrax:020 | INT | `herrax.trickster.react.arueshalae_morning_unheard_restored` | ENGINE | E-Q7-04 |
| herrax:021 | BEL | `herrax.trickster.epilogue.reachable` | ROUTE | — |
| horzalah:001 | CAN | `native.epilogue.Cue_0454` | ENGINE | E-Q7-09 |
| horzalah:002 | CAN | `native.epilogue.Cue_37_EE_AbyssTrio` | ENGINE | E-Q7-09 |
| horzalah:003 | CAN | `horzalah.trickster.mercy.gift` | ROUTE | — |
| horzalah:004 | CAN | `horzalah.trickster.unmet.knife` | ROUTE | — |
| horzalah:005 | CAN | `horzalah.trickster.unmet.knife` | ROUTE | — |
| horzalah:006 | CAN | `horzalah.trickster.unmet.knife` | ROUTE | — |
| horzalah:007 | CAN | `horzalah.trickster.late.at_night` | ROUTE | — |
| horzalah:008 | CAN | `horzalah.trickster.c6.guild_return` | ROUTE | — |
| horzalah:009 | CAN | `horzalah.trickster.guild.kept` | ROUTE | — |
| horzalah:010 | CAN | `horzalah.trickster.visit.chamber` | ROUTE | — |
| horzalah:011 | CAN | `horzalah.trickster.visit.chamber` | ROUTE | — |
| horzalah:012 | CAN | `horzalah.trickster.visit.chamber` | ROUTE | — |
| horzalah:013 | CAN | `horzalah.trickster.epilogue.commit` | ROUTE | — |
| horzalah:014 | CAN | `horzalah.trickster.epilogue.unanswered` | ROUTE | — |
| horzalah:015 | CAN | `horzalah.trickster.epilogue.decided` | ROUTE | — |
| horzalah:016 | CAN | `horzalah.trickster.epilogue.scarred` | ROUTE | — |
| horzalah:017 | CAN | `horzalah.trickster.epilogue.closed` | ROUTE | — |
| horzalah:018 | CAN | `horzalah.trickster.epilogue.mourned` | ROUTE | — |
| horzalah:019 | CAN | `horzalah.trickster.react.greybor_morning` | ROUTE | — |
| horzalah:020 | CAN | `horzalah.trickster.beat.lady` | ROUTE | — |
| horzalah:021 | CAN | `horzalah.trickster.beat.lady` | ROUTE | — |
| horzalah:022 | COX | `horzalah.trickster.guild.kept` | ENGINE | E-Q7-04 |
| horzalah:023 | COX | `horzalah.trickster.beat.name` | ENGINE | E-Q7-04 |
| horzalah:024 | INT | `horzalah.trickster.beat.storyteller` | ENGINE | E-Q7-10 |
| horzalah:025 | INT | `horzalah.trickster.visit.chamber` | ROUTE | — |
| horzalah:026 | INT | `horzalah.trickster.commit.her_move` | ROUTE | — |
| horzalah:027 | INT | `horzalah.trickster.commit.her_move_night` | ROUTE | — |
| horzalah:028 | BEL | `horzalah.trickster.test.the_gift_night` | ROUTE | — |
| horzalah:029 | BEL | `horzalah.trickster.guild.kept` | ROUTE | — |
| horzalah:030 | BEL | `horzalah.trickster.unmet.knife` | ROUTE | — |
| horzalah:031 | BEL | `horzalah.trickster.unmet.knife` | ROUTE | — |
| horzalah:032 | BEL | `horzalah.trickster.unmet.knife` | ROUTE | — |
| horzalah:033 | BEL | `horzalah.trickster.late.at_night` | ROUTE | — |
| horzalah:034 | BEL | `horzalah.trickster.c6.guild_return` | ROUTE | — |
| horzalah:035 | BEL | `horzalah.trickster.epilogue.commit` | ROUTE | — |
| horzalah:036 | CAN | `horzalah.trickster.late.at_night` | ENGINE | E-Q7-15 |
| horzalah:037 | CAN | `horzalah.trickster.unmet.knife` | ENGINE | E-Q7-15 |
| horzalah:038 | CAN | `horzalah.trickster.unmet.knife` | ENGINE | E-Q7-15 |
| horzalah:039 | INT | `horzalah.trickster.epilogue.commit` | ENGINE | E-Q7-15 |
| horzalah:040 | INT | `horzalah.trickster.epilogue.left_free` | ENGINE | E-Q7-15 |
| horzalah:041 | INT | `horzalah.trickster.epilogue.ally` | ENGINE | E-Q7-15 |
| iomedae:001 | TRK | `iomedae.trickster.platform.bare` | ENGINE | E-Q7-08 |
| iomedae:002 | TRK | `iomedae.trickster.iz.night` | ENGINE | E-Q7-08 |
| iomedae:003 | BEL | `iomedae.trickster.disputation` | ENGINE | E-Q7-08 |
| iomedae:004 | CAN | `iomedae.trickster.dream.mortal` | ENGINE | E-Q7-10 |
| iomedae:005 | INT | `iomedae.trickster.dream.eve` | ROUTE | — |
| iomedae:006 | INT | `iomedae.trickster.epilogue.platform` | ROUTE | — |
| irabeth:001 | CAN | `irabeth.ending_aeon` | ENGINE | E-Q7-16 |
| irabeth:002 | CAN | `irabeth.ending_lasting` | ENGINE | E-Q7-09 |
| irabeth:003 | CAN | `irabeth.ending_unfinished` | ENGINE | E-Q7-09 |
| irabeth:004 | CAN | `irabeth.ending_ascent` | ENGINE | E-Q7-09 |
| irabeth:005 | CAN | `irabeth.trickster.epilogue.estranged` | ENGINE | E-Q7-09 |
| irabeth:006 | CAN | `irabeth.trickster.epilogue.estranged_mourning` | ENGINE | E-Q7-09 |
| irabeth:007 | INT | `irabeth.trickster.dead.relieved_not_dismissed` | ENGINE | E-Q7-01 |
| irabeth:008 | INT | `irabeth.trickster.killed.blow_missed` | ENGINE | E-Q7-01 |
| irabeth:009 | COX | `irabeth.return_own_invitation` | ENGINE | E-Q7-17 |
| irabeth:010 | HOW | `irabeth.trickster.dead.relieved_not_dismissed` | ENGINE | E-Q7-12 |
| irabeth:011 | HOW | `irabeth.trickster.epilogue.estranged` | ENGINE | E-Q7-12 |
| irabeth:012 | HOW | `irabeth.return_invitation` | ROUTE | — |
| jannah:001 | INT | `jannah.trickster.alive.stories` | ENGINE | E-Q7-02 |
| jannah:002 | INT | `jannah.trickster.alive.wagon` | ENGINE | E-Q7-02 |
| jannah:003 | INT | `jannah.circle.forms` | ENGINE | E-Q7-02 |
| jannah:004 | HOW | `jannah.trickster.alive.stories` | ENGINE | E-Q7-12 |
| jannah:005 | BEL | `jannah.circle.blade` | ENGINE | E-Q7-27 |
| jannah:006 | BEL | `jannah.circle.the_watch` | ENGINE | E-Q7-27 |
| jannah:007 | BEL | `jannah.circle.anything_but_wings` | ENGINE | E-Q7-27 |
| jannah:008 | BEL | `jannah.circle.your_part` | ENGINE | E-Q7-27 |
| jannah:009 | VOI | `jannah.trickster.alive.wagon` | ROUTE | — |
| jerribeth:001 | BEL | `jerribeth.trickster.epilogue.commit` | ROUTE | — |
| kaylessa:001 | INT | `kaylessa.trickster.dead.soldier` | ENGINE | E-Q7-01 |
| kaylessa:002 | HOW | `kaylessa.trickster.dead.soldier` | ENGINE | E-Q7-12 |
| kaylessa:003 | CAN | `kaylessa.trickster.epilogue.declined` | ENGINE | E-Q7-16 |
| kaylessa:004 | BEL | `kaylessa.wasps.last_words` | ENGINE | E-Q7-10 |
| kaylessa:005 | BEL | `kaylessa.wasps.last_words` | ROUTE | — |
| kaylessa:006 | BEL | `kaylessa.trickster.dead.soldier` | ROUTE | — |
| kaylessa:007 | BEL | `kaylessa.trickster.dead.soldier` | ROUTE | — |
| kaylessa:008 | BEL | `kaylessa.wasps.the_other_you` | ROUTE | — |
| kaylessa:009 | BEL | `kaylessa.trickster.epilogue.no_lamb` | ROUTE | — |
| kaylessa:010 | BEL | `kaylessa.trickster.react.woljif_haggled` | ROUTE | — |
| kaylessa:011 | BEL | `kaylessa.trickster.dead.borrow_sending` | ROUTE | — |
| kaylessa:012 | BEL | `kaylessa.trickster.epilogue.no_lamb` | ROUTE | — |
| kaylessa:013 | BEL | `kaylessa.trickster.epilogue.commit` | ROUTE | — |
| kaylessa:014 | COX | `kaylessa.trickster.commit` | ENGINE | E-Q7-31 |
| kaylessa:015 | BEL | `kaylessa.trickster.epilogue.ally` | ROUTE | — |
| kaylessa:016 | BEL | `kaylessa.trickster.epilogue.no_lamb` | ROUTE | — |
| kaylessa:017 | BEL | `kaylessa.trickster.epilogue.commit` | ROUTE | — |
| kaylessa:018 | VOI | `kaylessa.trickster.react.woljif_morning` | ENGINE | E-Q7-21 |
| kaylessa:019 | BEL | `kaylessa.wasps.in_the_dark` | ROUTE | — |
| kaylessa:020 | BEL | `kaylessa.wasps.the_other_you` | ROUTE | — |
| kaylessa:021 | BEL | `kaylessa.clearing.where_i_was_meant_to_die` | ROUTE | — |
| kiana:001 | INT | `kiana.q3_recovery` | ENGINE | E-Q7-14 |
| kiana:002 | INT | `kiana.trickster.after.temple` | ENGINE | E-Q7-02 |
| kiana:003 | INT | `kiana.trickster.ward_rounds` | ENGINE | E-Q7-02 |
| kiana:004 | INT | `kiana.trickster.late_question` | ENGINE | E-Q7-02 |
| kiana:005 | INT | `kiana.trickster.after.letter` | ENGINE | E-Q7-02 |
| kiana:006 | INT | `kiana.trickster.late_question_letter` | ENGINE | E-Q7-02 |
| kiana:007 | HOW | `kiana.presence` | ENGINE | E-Q7-12 |
| kiana:008 | CAN | `kiana.trickster.react_arsinoe_souls_home` | ENGINE | E-Q7-10 |
| kiana:009 | CAN | `native.ktc_ElanCalls.Cue_0003` | ENGINE | E-Q7-09 |
| kiana:010 | CAN | `native.ktc_ElanCalls.Cue_0010` | ENGINE | E-Q7-09 |
| kiana:011 | BEL | `native.ktc_ElanCalls.Cue_0013` | ENGINE | E-Q7-09 |
| kiana:012 | CAN | `native.ktc_ElanCalls.Cue_0015` | ENGINE | E-Q7-09 |
| kiana:013 | CAN | `native.ktc_ElanCalls.Cue_0016` | ENGINE | E-Q7-09 |
| kiana:014 | CAN | `native.ktc_ElanCalls.Cue_0019` | ENGINE | E-Q7-09 |
| kiana:015 | CAN | `native.ktc_ElanCalls.Cue_0020` | ENGINE | E-Q7-09 |
| kiana:016 | BEL | `native.ktc_ElanCalls.Cue_0023` | ENGINE | E-Q7-09 |
| kiana:017 | CAN | `native.ktc_ElanCalls.Cue_0027` | ENGINE | E-Q7-09 |
| kiana:018 | BEL | `native.ktc_ElanCalls.Cue_0033` | ENGINE | E-Q7-09 |
| kiana:019 | CAN | `native.ktc_DeserterJoins.Cue_0009` | ENGINE | E-Q7-09 |
| kiana:020 | CAN | `native.HideoutIntro.Answer_0009` | ENGINE | E-Q7-09 |
| kiana:021 | CAN | `native.HideoutIntro.Answer_0011` | ENGINE | E-Q7-09 |
| kiana:022 | CAN | `native.HideoutIntro.Cue_0003` | ENGINE | E-Q7-09 |
| kiana:023 | BEL | `native.HideoutIntro.Cue_0006` | ENGINE | E-Q7-09 |
| kiana:024 | CAN | `native.HideoutIntro.Cue_0016` | ENGINE | E-Q7-09 |
| kiana:025 | BEL | `native.ElanDying.Cue_0003` | ENGINE | E-Q7-09 |
| kiana:026 | CAN | `native.ElanDying.Cue_0011` | ENGINE | E-Q7-09 |
| kiana:027 | CAN | `native.JewelerFinal.Answer_0022` | ENGINE | E-Q7-09 |
| kiana:028 | CAN | `native.SeelahInDoubt.Cue_0001` | ENGINE | E-Q7-09 |
| kiana:029 | CAN | `native.SeelahInDoubt.Cue_0005` | ENGINE | E-Q7-09 |
| kiana:030 | CAN | `native.SeelahInDoubt.Cue_0006` | ENGINE | E-Q7-09 |
| kiana:031 | CAN | `native.SeelahInDoubt.Cue_0038` | ENGINE | E-Q7-09 |
| kiana:032 | BEL | `native.KianaAloneAftermath.Cue_0001` | ENGINE | E-Q7-09 |
| kiana:033 | CAN | `native.WeightOfMySword_SeelahQ3_quest` | ENGINE | E-Q7-32 |
| kiana:034 | CAN | `native.01_JewelerHideot` | ENGINE | E-Q7-32 |
| kiana:035 | CAN | `native.02_FindSoulGems` | ENGINE | E-Q7-32 |
| kiana:036 | CAN | `native.03_ReturnSouls` | ENGINE | E-Q7-32 |
| kiana:037 | CAN | `native.Add_JannahJoins` | ENGINE | E-Q7-32 |
| kiana:038 | VOI | `kiana.former_grief/invite` | ROUTE | — |
| kiana:039 | VOI | `kiana.former_grief/story` | ROUTE | — |
| konomi:001 | CAN | `konomi.before_road` | ROUTE | — |
| konomi:002 | CAN | `konomi.chosen_evening` | ROUTE | — |
| konomi:003 | CAN | `konomi.private_last_visit` | ROUTE | — |
| konomi:004 | BEL | `konomi.private_reunion` | ROUTE | — |
| konomi:005 | BEL | `konomi.private_absence_catchup` | ROUTE | — |
| konomi:006 | INT | `konomi.the_courtyard_introduction` | ROUTE | — |
| konomi:007 | BEL | `konomi.trickster.never_arrived.rooms` | ROUTE | — |
| konomi:008 | BEL | `konomi.trickster.never_arrived.rooms` | ROUTE | — |
| melazmera:001 | COX | `melazmera.trickster.ch5.hunger` | ENGINE | E-Q7-04 |
| melazmera:002 | INT | `melazmera.trickster.ch5.hunger` | ENGINE | E-Q7-04 |
| melazmera:003 | CAN | `melazmera.trickster.react.nenio_specimen` | ENGINE | E-Q7-15 |
| melazmera:004 | INT | `melazmera.trickster.beat.greybor` | ENGINE | E-Q7-04 |
| melazmera:005 | INT | `melazmera.trickster.beat.greybor` | ENGINE | E-Q7-04 |
| melazmera:006 | INT | `melazmera.trickster.beat.greybor` | ENGINE | E-Q7-04 |
| melazmera:007 | INT | `melazmera.trickster.beat.greybor` | ENGINE | E-Q7-04 |
| melazmera:008 | INT | `melazmera.trickster.beat.inquisitor` | ENGINE | E-Q7-04 |
| melazmera:009 | INT | `melazmera.trickster.ch4.hunt_found` | ENGINE | E-Q7-15 |
| melazmera:010 | INT | `melazmera.trickster.ch4.hunt_found` | ENGINE | E-Q7-15 |
| melazmera:011 | INT | `melazmera.trickster.ch4.hunt_found` | ENGINE | E-Q7-15 |
| melazmera:012 | BEL | `melazmera.trickster.beat.illusion` | ROUTE | — |
| melazmera:013 | BEL | `melazmera.trickster.ch4.salt` | ROUTE | — |
| mielarah:001 | CAN | `mielarah.trickster.raid.ashore_drezen` | ENGINE | E-Q7-08 |
| mielarah:002 | CAN | `mielarah.trickster.raid.elbow` | ENGINE | E-Q7-09 |
| mielarah:003 | INT | `mielarah.deck.best_job` | ENGINE | E-Q7-04 |
| mielarah:004 | INT | `mielarah.deck.best_job.arcade` | ENGINE | E-Q7-04 |
| mielarah:005 | INT | `mielarah.deck.stowaway` | ENGINE | E-Q7-04 |
| mielarah:006 | INT | `mielarah.deck.stowaway.arcade` | ENGINE | E-Q7-04 |
| mielarah:007 | BEL | `mielarah.deck.market` | ENGINE | E-Q7-27 |
| mielarah:008 | BEL | `mielarah.deck.market.arcade` | ENGINE | E-Q7-27 |
| mielarah:009 | BEL | `mielarah.trickster.tavern.repeat` | ROUTE | — |
| mielarah:010 | BEL | `mielarah.deck.supper` | ROUTE | — |
| mielarah:011 | BEL | `mielarah.deck.supper.arcade` | ROUTE | — |
| mielarah:012 | BEL | `mielarah.deck.correction` | ROUTE | — |
| mielarah:013 | BEL | `mielarah.deck.correction.arcade` | ROUTE | — |
| mielarah:014 | BEL | `mielarah.deck.names` | ROUTE | — |
| mielarah:015 | BEL | `mielarah.deck.names.arcade` | ROUTE | — |
| mielarah:016 | BEL | `mielarah.deck.names` | ENGINE | E-Q7-18 |
| mielarah:017 | BEL | `mielarah.deck.names.arcade` | ENGINE | E-Q7-18 |
| mielarah:018 | BEL | `mielarah.deck.wounded` | ROUTE | — |
| mielarah:019 | BEL | `mielarah.deck.wounded.arcade` | ROUTE | — |
| mielarah:020 | BEL | `mielarah.trickster.epilogue.late` | ROUTE | — |
| mielarah:021 | BEL | `mielarah.trickster.epilogue.late` | ENGINE | E-Q7-18 |
| mielarah:022 | BEL | `mielarah.lastcall.page` | ROUTE | — |
| mielarah:023 | BEL | `mielarah.lastcall.page` | ROUTE | — |
| mielarah:024 | HOW | `mielarah.deck.best_job` | ENGINE | E-Q7-12 |
| minagho-and-chivarro:001 | CAN | `minagho_chivarro.trickster.minagho_dead.setup_c3` | ROUTE | — |
| minagho-and-chivarro:002 | CAN | `minagho_chivarro.trickster.minagho_dead.setup_c4` | ROUTE | — |
| minagho-and-chivarro:003 | CAN | `minagho_chivarro.trickster.spared.brand` | ENGINE | E-Q7-10 |
| minagho-and-chivarro:004 | CAN | `minagho_chivarro.trickster.spared.brand` | ENGINE | E-Q7-32 |
| minagho-and-chivarro:005 | CAN | `minagho_chivarro.trickster.react.baphomet` | ENGINE | E-Q7-09 |
| minagho-and-chivarro:006 | INT | `minagho_chivarro.trickster.minagho_dead.brand` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:007 | INT | `minagho_chivarro.trickster.minagho_dead.brand_letter` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:008 | INT | `minagho_chivarro.trickster.spared.brand` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:009 | INT | `minagho_chivarro.trickster.spared.brand_letter` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:010 | INT | `minagho_chivarro.trickster.chivarro_dead.the_bill` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:011 | INT | `minagho_chivarro.trickster.chivarro_dead.the_bill_letter` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:012 | INT | `minagho_chivarro.trickster.alone.chivarro` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:013 | INT | `minagho_chivarro.trickster.alone.chivarro_letter` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:014 | INT | `minagho_chivarro.trickster.alone.minagho` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:015 | INT | `minagho_chivarro.trickster.alone.minagho_spared` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:016 | INT | `minagho_chivarro.trickster.alone.minagho_letter` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:017 | INT | `minagho_chivarro.trickster.alone.chivarro_morning` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:018 | INT | `minagho_chivarro.trickster.alone.minagho_morning` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:019 | INT | `minagho_chivarro.trickster.alone.minagho_spared_morning` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:020 | INT | `minagho_chivarro.trickster.debt.collectors` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:021 | INT | `minagho_chivarro.trickster.debt.collectors_spared` | ENGINE | E-Q7-01 |
| minagho-and-chivarro:022 | INT | `minachiv.two_answers` | ENGINE | E-Q7-10 |
| minagho-and-chivarro:023 | INT | `minachiv.her_own_arrival` | ENGINE | E-Q7-10 |
| minagho-and-chivarro:024 | COX | `minagho_chivarro.trickster.reunion.wardrobe` | ENGINE | E-Q7-06 |
| minagho-and-chivarro:025 | COX | `minagho_chivarro.trickster.alone.minagho_when_it_scars` | ENGINE | E-Q7-06 |
| minagho-and-chivarro:026 | COX | `minagho_chivarro.trickster.epilogue.pair` | ENGINE | E-Q7-06 |
| minagho-and-chivarro:027 | COX | `minagho_chivarro.trickster.epilogue.minagho` | ENGINE | E-Q7-06 |
| minagho-and-chivarro:028 | COX | `minagho_chivarro.trickster.epilogue.chivarro` | ENGINE | E-Q7-06 |
| minagho-and-chivarro:029 | COX | `minagho_chivarro.trickster.epilogue.owned` | ENGINE | E-Q7-06 |
| minagho-and-chivarro:030 | COX | `minagho_chivarro.trickster.epilogue.commit` | ENGINE | E-Q7-31 |
| minagho-and-chivarro:031 | COX | `minagho_chivarro.trickster.epilogue.commit` | ENGINE | E-Q7-31 |
| minagho-and-chivarro:032 | COX | `guest.minagho_chivarro` | ENGINE | E-Q7-04 |
| minagho-and-chivarro:033 | COX | `minachiv.lastcall.page` | ENGINE | E-Q7-04 |
| minagho-and-chivarro:034 | TRK | `minagho_chivarro.trickster.epilogue.commit` | ENGINE | E-Q7-31 |
| minagho-and-chivarro:035 | BEL | `minagho_chivarro.trickster.epilogue.commit` | ENGINE | E-Q7-31 |
| minagho-and-chivarro:036 | HOW | `minagho_chivarro.trickster.minagho_dead.brand` | ENGINE | E-Q7-12 |
| minagho-and-chivarro:037 | HOW | `minachiv.two_answers` | ENGINE | E-Q7-12 |
| nenio:001 | CAN | `nenio.lastcall.page` | ROUTE | — |
| nenio:002 | CAN | `nenio.lastcall.page` | ENGINE | E-Q7-15 |
| nenio:003 | CAN | `nenio.lastcall.page` | ENGINE | E-Q7-15 |
| nenio:004 | CAN | `nenio.lastcall.call` | ENGINE | E-Q7-15 |
| nenio:005 | TRK | `nenio.trickster.away.field_report` | ROUTE | — |
| nenio:006 | COX | `nenio.trickster.away.field_report` | ENGINE | E-Q7-18 |
| nenio:007 | INT | `nenio.trickster.dead.the_price` | ENGINE | E-Q7-25 |
| nenio:008 | BEL | `nenio.trickster.commit.result` | ENGINE | E-Q7-27 |
| nenio:009 | BEL | `nenio.trickster.commit.result_visitor` | ENGINE | E-Q7-27 |
| nenio:010 | BEL | `nenio.trickster.commit.result_arcade` | ENGINE | E-Q7-27 |
| nenio:011 | BEL | `nenio.trickster.killed.stranger_visitor` | ENGINE | E-Q7-18 |
| nenio:012 | BEL | `nenio.trickster.killed.stranger_arcade` | ENGINE | E-Q7-18 |
| nenio:013 | BEL | `nenio.folio.drezen.handed_visitor` | ROUTE | — |
| nenio:014 | BEL | `nenio.folio.drezen.handed_arcade` | ROUTE | — |
| nenio:015 | BEL | `nenio.folio.volume_one_visitor` | ENGINE | E-Q7-18 |
| nenio:016 | BEL | `nenio.folio.volume_one_arcade` | ENGINE | E-Q7-18 |
| nenio:017 | INT | `nenio.folio.volume_one_visitor` | ENGINE | E-Q7-15 |
| nenio:018 | INT | `nenio.folio.volume_one_arcade` | ENGINE | E-Q7-15 |
| nenio:019 | BEL | `nenio.folio.market_visitor` | ENGINE | E-Q7-18 |
| nenio:020 | BEL | `nenio.folio.market_arcade` | ENGINE | E-Q7-18 |
| nenio:021 | BEL | `nenio.folio.kenabres_box_visitor` | ENGINE | E-Q7-18 |
| nenio:022 | BEL | `nenio.folio.kenabres_box_arcade` | ENGINE | E-Q7-18 |
| nenio:023 | BEL | `nenio.folio.kenabres_box_visitor` | ENGINE | E-Q7-18 |
| nenio:024 | BEL | `nenio.folio.kenabres_box_arcade` | ENGINE | E-Q7-18 |
| nenio:025 | BEL | `nenio.folio.kenabres_box_visitor` | ENGINE | E-Q7-18 |
| nenio:026 | BEL | `nenio.folio.kenabres_box_arcade` | ENGINE | E-Q7-18 |
| nenio:027 | BEL | `nenio.folio.kenabres_judgment_visitor` | ENGINE | E-Q7-18 |
| nenio:028 | BEL | `nenio.folio.kenabres_judgment_arcade` | ENGINE | E-Q7-18 |
| nenio:029 | BEL | `nenio.folio.sphinx_list_visitor` | ENGINE | E-Q7-18 |
| nenio:030 | BEL | `nenio.folio.sphinx_list_arcade` | ENGINE | E-Q7-18 |
| nenio:031 | INT | `nenio.folio.teeth` | ENGINE | E-Q7-10 |
| nenio:032 | INT | `nenio.folio.teeth_visitor` | ENGINE | E-Q7-10 |
| nenio:033 | INT | `nenio.folio.teeth_arcade` | ENGINE | E-Q7-10 |
| nenio:034 | BEL | `nenio.folio.who_are_you` | ROUTE | — |
| nenio:035 | BEL | `nenio.folio.who_are_you_visitor` | ROUTE | — |
| nenio:036 | BEL | `nenio.folio.who_are_you_arcade` | ROUTE | — |
| nenio:037 | INT | `nenio.folio.who_are_you` | ENGINE | E-Q7-10 |
| nenio:038 | INT | `nenio.folio.who_are_you_visitor` | ENGINE | E-Q7-10 |
| nenio:039 | INT | `nenio.folio.who_are_you_arcade` | ENGINE | E-Q7-10 |
| nenio:040 | BEL | `nenio.folio.abyss.shoulder` | ROUTE | — |
| nenio:041 | INT | `nenio.lastcall.call` | ENGINE | E-Q7-07 |
| nenio:042 | INT | `nenio.lastcall.page` | ENGINE | E-Q7-07 |
| nenio:043 | INT | `owed.nenio` | ENGINE | E-Q7-07 |
| nenio:044 | INT | `nenio.lastcall.page` | ENGINE | E-Q7-07 |
| nenio:045 | BEL | `nenio.lastcall.page` | ROUTE | — |
| nenio:046 | BEL | `owed.nenio` | ROUTE | — |
| nenio:047 | BEL | `nenio.lastcall.page` | ENGINE | E-Q7-18 |
| nenio:048 | BEL | `nenio.lastcall.call` | ENGINE | E-Q7-18 |
| nenio:049 | BEL | `nenio.trickster.epilogue.commit` | ROUTE | — |
| nenio:050 | INT | `nocticula.trickster.reaction.nenio` | ENGINE | E-Q7-29 |
| nenio:051 | INT | `eritrice.trickster.react.nenio_motion` | ENGINE | E-Q7-29 |
| nenio:052 | INT | `eritrice.trickster.react.nenio_tabled` | ENGINE | E-Q7-29 |
| nenio:053 | INT | `areelu.trickster.react.nenio_two_drafts` | ENGINE | E-Q7-29 |
| nenio:054 | INT | `melazmera.trickster.react.nenio_specimen` | ENGINE | E-Q7-29 |
| nenio:055 | HOW | `nenio.presence` | ENGINE | E-Q7-13 |
| nenio:056 | HOW | `nenio.presence.arcade` | ENGINE | E-Q7-13 |
| nenio:057 | HOW | `nenio.presence` | ENGINE | E-Q7-13 |
| nocticula:001 | INT | `nocticula.trickster.defeated.late_shadow` | ENGINE | E-Q7-10 |
| nocticula:002 | INT | `noct.mask_and_bell` | ROUTE | — |
| nocticula:003 | BEL | `noct.cost_of_return` | ROUTE | — |
| nocticula:004 | BEL | `noct.hearing` | ROUTE | — |
| nocticula:005 | BEL | `noct.no_applause` | ROUTE | — |
| nocticula:006 | BEL | `noct.ending_alliance` | ROUTE | — |
| nocticula:007 | BEL | `noct.acq.the_missing_line` | ROUTE | — |
| nocticula:008 | BEL | `noct.acq.the_paid_address` | ROUTE | — |
| nocticula:009 | BEL | `noct.sixth_passenger` | ROUTE | — |
| nocticula:010 | BEL | `noct.her_own_face` | ROUTE | — |
| nocticula:011 | BEL | `noct.demonstration` | ROUTE | — |
| nocticula:012 | BEL | `noct.another_place` | ROUTE | — |
| nocticula:013 | BEL | `noct.hearing` | ROUTE | — |
| nocticula:014 | BEL | `noct.last_buyer` | ROUTE | — |
| nocticula:015 | BEL | `noct.closed_gallery` | ROUTE | — |
| nocticula:016 | BEL | `noct.second_door` | ROUTE | — |
| nocticula:017 | BEL | `noct.acq.the_paid_address` | ROUTE | — |
| nocticula:018 | BEL | `noct.acq.epilogue.correspondence` | ROUTE | — |
| nocticula:019 | BEL | `noct.acq.epilogue.correspondence.elysium` | ROUTE | — |
| nocticula:020 | HOW | `nocticula.lastcall.page` | ENGINE | E-Q7-12 |
| nurah:001 | INT | `nurah.trickster.prison.pardon_late` | ENGINE | E-Q7-01 |
| nurah:002 | INT | `nurah.trickster.prison.night_out_late` | ENGINE | E-Q7-01 |
| nurah:003 | BEL | `nurah.a_margin_for_you` | ROUTE | — |
| nurah:004 | HOW | `nurah.trickster.prison.pardon_late` | ENGINE | E-Q7-12 |
| seelah:001 | BEL | `seelah.trickster.in_party.lift_lesson` | ROUTE | — |
| seelah:002 | VOI | `seelah.morning` | ROUTE | — |
| seelah:003 | VOI | `seelah.roof_evening` | ROUTE | — |
| seelah:004 | BEL | `seelah.late_afterglow` | ENGINE | E-Q7-18 |
| seelah:005 | BEL | `seelah.trickster.dead.wakes` | ROUTE | — |
| seelah:006 | BEL | `seelah.trickster.dead.wakes` | ROUTE | — |
| seelah:007 | BEL | `seelah.trickster.dead.wakes` | ROUTE | — |
| seelah:008 | BEL | `seelah.trickster.dismissed.commit` | ROUTE | — |
| seelah:009 | BEL | `seelah.trickster.dismissed.commit` | ROUTE | — |
| seelah:010 | BEL | `seelah.trickster.dismissed.commit` | ROUTE | — |
| seelah:011 | BEL | `seelah.trickster.epilogue.pickpocket` | ROUTE | — |
| seelah:012 | BEL | `seelah.trickster.epilogue.pickpocket` | ROUTE | — |
| seelah:013 | BEL | `seelah.trickster.dead.pickpocket` | ROUTE | — |
| seelah:014 | BEL | `seelah.trickster.dead.pickpocket` | ROUTE | — |
| shamira:001 | INT | `shamira.trickster.after.city` | ENGINE | E-Q7-02 |
| shamira:002 | INT | `shamira.trickster.after.city_awning` | ENGINE | E-Q7-02 |
| shamira:003 | INT | `shamira.trickster.after.visit` | ENGINE | E-Q7-02 |
| shamira:004 | INT | `shamira.trickster.after.visit_awning` | ENGINE | E-Q7-02 |
| shamira:005 | INT | `shamira.trickster.harem` | ENGINE | E-Q7-02 |
| shamira:006 | INT | `shamira.trickster.harem_awning` | ENGINE | E-Q7-02 |
| shamira:007 | INT | `shamira.trickster.after.throne` | ENGINE | E-Q7-02 |
| shamira:008 | INT | `shamira.trickster.after.throne_awning` | ENGINE | E-Q7-02 |
| shamira:009 | INT | `shamira.trickster.after.night_alone` | ENGINE | E-Q7-02 |
| shamira:010 | INT | `shamira.trickster.after.night_alone_awning` | ENGINE | E-Q7-02 |
| shamira:011 | INT | `shamira.trickster.mind.barracks_after` | ENGINE | E-Q7-02 |
| shamira:012 | INT | `shamira.trickster.mind.barracks_after_awning` | ENGINE | E-Q7-02 |
| shamira:013 | BEL | `shamira.trickster.epilogue.mourned` | ROUTE | — |
| shamira:014 | COX | `shamira.trickster.mind.barracks_inquiry` | ENGINE | E-Q7-17 |
| shamira:015 | HOW | `shamira.trickster.harem` | ENGINE | E-Q7-12 |
| shamira:016 | HOW | `shamira.trickster.mind.barracks_inquiry` | ENGINE | E-Q7-17 |
| soana:001 | CAN | `soana.trickster.epilogue.by_your_hand` | ENGINE | E-Q7-10 |
| soana:002 | INT | `soana.trickster.react.ulbrig_knot` | ENGINE | E-Q7-10 |
| soana:003 | BEL | `soana.trickster.epilogue.unfinished` | ROUTE | — |
| soana:004 | BEL | `soana.trickster.handover.winter_portion` | ROUTE | — |
| terendelev:001 | CAN | `terendelev.trickster.react.storyteller.quiet` | ENGINE | E-Q7-09 |
| terendelev:002 | CAN | `terendelev.trickster.react.storyteller.quiet` | ENGINE | E-Q7-09 |
| terendelev:003 | CAN | `terendelev.trickster.react.storyteller.quiet` | ENGINE | E-Q7-09 |
| terendelev:004 | INT | `terendelev.trickster.bones.restitution` | ENGINE | E-Q7-26 |
| terendelev:005 | INT | `terendelev.trickster.bones.restitution_irabeth` | ENGINE | E-Q7-26 |
| terendelev:006 | INT | `terendelev.trickster.watch.third_bell` | ENGINE | E-Q7-26 |
| terendelev:007 | INT | `terendelev.trickster.watch.third_bell_awning` | ENGINE | E-Q7-26 |
| terendelev:008 | BEL | `terendelev.trickster.commit` | ROUTE | — |
| terendelev:009 | BEL | `terendelev.trickster.commit_awning` | ROUTE | — |
| terendelev:010 | HOW | `terendelev.trickster.watch.war_table` | ENGINE | E-Q7-20 |
| terendelev:011 | HOW | `terendelev.trickster.watch.war_table_awning` | ENGINE | E-Q7-20 |
| terendelev:012 | CAN D | `terendelev.continuation.returned_letter` | ROUTE | — |
| terendelev:013 | BEL D | `terendelev.continuation.returned_letter` | ENGINE | E-Q7-21 |
| terendelev:014 | VOI D | `terendelev.continuation.returned_letter` | ROUTE | — |
| terendelev:015 | VOI D | `terendelev.continuation.returned_letter` | ROUTE | — |
| terendelev:016 | VOI D | `terendelev.continuation.returned_letter` | ROUTE | — |
| terendelev:017 | VOI D | `terendelev.continuation.returned_letter` | ROUTE | — |
| terendelev:018 | VOI D | `terendelev.continuation.private_oath` | ROUTE | — |
| terendelev:019 | BEL D | `terendelev.continuation.private_oath` | ROUTE | — |
| terendelev:020 | VOI D | `terendelev.continuation.private_oath` | ROUTE | — |
| terendelev:021 | INT D | `terendelev.continuation.inspection_day` | ENGINE | E-Q7-22 |
| terendelev:022 | BEL D | `terendelev.continuation.windward_evening` | ENGINE | E-Q7-21 |
| terendelev:023 | VOI D | `terendelev.continuation.windward_evening` | ROUTE | — |
| terendelev:024 | BEL D | `terendelev.continuation.windward_evening` | ROUTE | — |
| terendelev:025 | BEL D | `terendelev.continuation.kenabres_vigil` | ENGINE | E-Q7-21 |
| terendelev:026 | INT D | `terendelev.continuation.kenabres_vigil` | ENGINE | E-Q7-22 |
| terendelev:027 | VOI D | `terendelev.continuation.private_aftercare` | ROUTE | — |
| terendelev:028 | INT D | `terendelev.continuation.private_aftercare` | ENGINE | E-Q7-22 |
| terendelev:029 | INT D | `terendelev.continuation.scale_invitation` | ROUTE | — |
| terendelev:030 | INT D | `terendelev.continuation.scale_invitation` | ROUTE | — |
| terendelev:031 | HOW D | `terendelev.continuation.scale_invitation` | ENGINE | E-Q7-23 |
| terendelev:032 | HOW D | `terendelev.continuation.escape_boundary` | ENGINE | E-Q7-22 |
| terendelev:033 | BEL D | `terendelev.continuation.escape_boundary` | ENGINE | E-Q7-21 |
| terendelev:034 | BEL D | `terendelev.continuation.trickster_friendship` | ROUTE | — |
| terendelev:035 | BEL D | `terendelev.continuation.trickster_friendship` | ENGINE | E-Q7-21 |
| terendelev:036 | BEL D | `terendelev.continuation.trickster_native_lead` | ENGINE | E-Q7-21 |
| terendelev:037 | BEL D | `terendelev.continuation.trickster_identity_review` | ROUTE | — |
| terendelev:038 | BEL D | `terendelev.continuation.trickster_identity_review` | ENGINE | E-Q7-21 |
| terendelev:039 | BEL D | `terendelev.continuation.trickster_other_half_living` | ENGINE | E-Q7-21 |
| terendelev:040 | BEL D | `terendelev.continuation.trickster_other_half_dead` | ENGINE | E-Q7-21 |
| terendelev:041 | BEL D | `terendelev.continuation.trickster_new_courtship` | ROUTE | — |
| terendelev:042 | HOW D | `terendelev.continuation.trickster_new_courtship` | ENGINE | E-Q7-23 |
| terendelev:043 | BEL D | `terendelev.continuation.escape_choice` | ROUTE | — |
| terendelev:044 | BEL D | `terendelev.continuation.escape_choice` | ENGINE | E-Q7-21 |
| terendelev:045 | INT D | `terendelev.continuation.scale_evening` | ENGINE | E-Q7-22 |
| terendelev:046 | HOW D | `terendelev.continuation.returned_letter` | ENGINE | E-Q7-22 |
| terendelev:047 | HOW D | `terendelev.continuation.returned_letter` | ENGINE | E-Q7-20 |
| terendelev:048 | HOW D | `terendelev.continuation.kenabres_petition` | ENGINE | E-Q7-20 |
| terendelev:049 | HOW D | `terendelev.continuation.private_oath` | ENGINE | E-Q7-20 |
| terendelev:050 | HOW D | `terendelev.continuation.inspection_day` | ENGINE | E-Q7-20 |
| terendelev:051 | HOW D | `terendelev.continuation.windward_evening` | ENGINE | E-Q7-20 |
| terendelev:052 | HOW D | `terendelev.continuation.kenabres_vigil` | ENGINE | E-Q7-20 |
| terendelev:053 | HOW D | `terendelev.continuation.private_aftercare` | ENGINE | E-Q7-20 |
| terendelev:054 | HOW D | `terendelev.continuation.scale_invitation` | ENGINE | E-Q7-20 |
| terendelev:055 | HOW D | `terendelev.continuation.escape_boundary` | ENGINE | E-Q7-20 |
| terendelev:056 | HOW D | `terendelev.continuation.trickster_friendship` | ENGINE | E-Q7-20 |
| terendelev:057 | HOW D | `terendelev.continuation.trickster_native_lead` | ENGINE | E-Q7-20 |
| terendelev:058 | HOW D | `terendelev.continuation.trickster_identity_review` | ENGINE | E-Q7-20 |
| terendelev:059 | HOW D | `terendelev.continuation.trickster_other_half_living` | ENGINE | E-Q7-20 |
| terendelev:060 | HOW D | `terendelev.continuation.trickster_other_half_dead` | ENGINE | E-Q7-20 |
| terendelev:061 | HOW D | `terendelev.continuation.trickster_new_courtship` | ENGINE | E-Q7-20 |
| terendelev:062 | HOW D | `terendelev.continuation.escape_choice` | ENGINE | E-Q7-20 |
| terendelev:063 | HOW D | `terendelev.continuation.scale_evening` | ENGINE | E-Q7-20 |
| vellexia:001 | CAN | `vellexia.trickster.sword.portrait` | ENGINE | E-Q7-10 |
| vellexia:002 | CAN | `vellexia.trickster.sword.portrait` | ENGINE | E-Q7-10 |
| vellexia:003 | BEL | `vellexia.trickster.mirrored.fetch` | ROUTE | — |
| vellexia:004 | BEL | `vellexia.ending_mirror` | ROUTE | — |
| wenduag:001 | CAN | `wenduag.trickster.epilogue.pack` | ENGINE | E-Q7-09 |
| wenduag:002 | CAN | `wenduag.trickster.killed.back` | ENGINE | E-Q7-08 |
| wenduag:003 | CAN | `wenduag.trickster.abyss.back` | ENGINE | E-Q7-08 |
| wenduag:004 | CAN | `wenduag.trickster.street.fall` | ENGINE | E-Q7-08 |
| wenduag:005 | CAN | `wenduag.trickster.street.back` | ENGINE | E-Q7-08 |
| wenduag:006 | CAN | `wenduag.trickster.court.claim` | ENGINE | E-Q7-08 |
| wenduag:007 | CAN | `wenduag.trickster.epilogue.native_service` | ENGINE | E-Q7-08 |
| wenduag:008 | CAN | `wenduag.trickster.epilogue.native_return` | ENGINE | E-Q7-08 |
| wenduag:009 | CAN | `wenduag.trickster.epilogue.pack` | ENGINE | E-Q7-08 |
| wenduag:010 | VOI | `wenduag.trickster.early.teeth` | ROUTE | — |
| wenduag:011 | VOI | `wenduag.trickster.react.regill_watch` | ROUTE | — |
| wenduag:012 | TRK | `wenduag.trickster.abyss.fall` | ENGINE | E-Q7-30 |
| wenduag:013 | TRK | `wenduag.trickster.street.fall` | ENGINE | E-Q7-30 |
| wenduag:014 | BEL | `wenduag.trickster.killed.stage` | ROUTE | — |
| wenduag:015 | BEL | `wenduag.trickster.abyss.fall` | ROUTE | — |
| wenduag:016 | BEL | `wenduag.trickster.abyss.back` | ROUTE | — |
| wenduag:017 | BEL | `wenduag.trickster.killed.cellar` | ROUTE | — |
| wenduag:018 | BEL | `wenduag.trickster.court.stinger` | ROUTE | — |
| wenduag:019 | BEL | `wenduag.trickster.court.stinger` | ROUTE | — |
| wenduag:020 | INT | `secret.wenduag_cairn` | ENGINE | E-Q7-23 |
| wenduag:021 | BEL | `secret.wenduag_cairn` | ROUTE | — |
| wenduag:022 | BEL | `secret.wenduag_cairn` | ROUTE | — |
| wenduag:023 | BEL | `owed.wenduag` | ROUTE | — |
| wenduag:024 | BEL | `owed.wenduag` | ROUTE | — |
| wenduag:025 | BEL | `owed.wenduag` | ROUTE | — |
| wenduag:026 | BEL | `wenduag.trickster.court.neathers` | ROUTE | — |
| wenduag:027 | INT | `wenduag.trickster.court.claim` | ENGINE | E-Q7-02 |
| wenduag:028 | COX | `wenduag.trickster.court.claim` | ENGINE | E-Q7-06 |
| wenduag:029 | COX | `wenduag.trickster.epilogue.pack` | ENGINE | E-Q7-06 |
| wenduag:030 | COX | `wenduag.trickster.epilogue.native_service` | ENGINE | E-Q7-06 |
| wenduag:031 | COX | `wenduag.trickster.epilogue.native_return` | ENGINE | E-Q7-06 |
| wenduag:032 | COX | `wenduag.trickster.epilogue.unclaimed` | ENGINE | E-Q7-06 |
| wenduag:033 | COX | `wenduag.trickster.epilogue.refused` | ENGINE | E-Q7-06 |
| wenduag:034 | COX | `guest.wenduag` | ENGINE | E-Q7-06 |
| wenduag:035 | COX | `wenduag.lastcall.page` | ENGINE | E-Q7-06 |
| wenduag:036 | COX | `wenduag.lastcall.call` | ENGINE | E-Q7-07 |
| wenduag:037 | BEL | `wenduag.lastcall.call` | ROUTE | — |
| wenduag:038 | BEL | `wenduag.lastcall.page` | ROUTE | — |
| wenduag:039 | BEL | `wenduag.lastcall.page` | ENGINE | E-Q7-21 |
| wenduag:040 | BEL | `wenduag.lastcall.page` | ROUTE | — |
| wenduag:041 | COX | `wenduag.lastcall.page` | ENGINE | E-Q7-04 |
| wenduag:042 | COX | `wenduag.trickster.court.vellexia` | ENGINE | E-Q7-04 |
| wenduag:043 | COX | `wenduag.trickster.epilogue.pack` | ENGINE | E-Q7-04 |
| wenduag:044 | COX | `wenduag.trickster.epilogue.pack` | ENGINE | E-Q7-04 |
| wenduag:045 | BEL | `horzalah.trickster.react.wenduag_morning_street` | ROUTE | — |
| wenduag:046 | BEL | `horzalah.trickster.react.wenduag_gift_street` | ROUTE | — |
| wenduag:047 | COX | `horzalah.trickster.react.wenduag_morning_street` | ENGINE | E-Q7-04 |
| wenduag:048 | COX | `wenduag.trickster.killed.cellar` | ENGINE | E-Q7-17 |
| wenduag:049 | COX | `wenduag.trickster.ch4.stone` | ENGINE | E-Q7-17 |
| wenduag:050 | COX | `wenduag.trickster.exile.champion` | ENGINE | E-Q7-17 |
| wenduag:051 | COX | `wenduag.trickster.exile.late_bid` | ENGINE | E-Q7-17 |
| wenduag:052 | COX | `wenduag.trickster.abyss.fall` | ENGINE | E-Q7-17 |
| wenduag:053 | COX | `wenduag.trickster.court.trial` | ENGINE | E-Q7-17 |
| wenduag:054 | HOW | `wenduag.trickster.court.claim` | ENGINE | E-Q7-12 |
| wenduag:055 | HOW | `wenduag.trickster.epilogue.pack` | ENGINE | E-Q7-12 |
| wenduag:056 | VOI D | `wenduag.vellexia_network.reception` | ROUTE | — |
| wenduag:057 | VOI D | `wenduag.vellexia_network.reception` | ROUTE | — |
| wenduag:058 | VOI D | `wenduag.vellexia_network.reception` | ROUTE | — |
| wenduag:059 | VOI D | `wenduag.vellexia_network.reception` | ROUTE | — |
| wenduag:060 | VOI D | `wenduag.vellexia_network.reception` | ROUTE | — |
| wenduag:061 | VOI D | `wenduag.vellexia_network.reception` | ROUTE | — |
| wenduag:062 | VOI D | `wenduag.vellexia_network.reception` | ROUTE | — |
| wenduag:063 | VOI D | `wenduag.vellexia_network.reception` | ROUTE | — |
| wenduag:064 | VOI D | `wenduag.vellexia_network.reception` | ROUTE | — |
| wenduag:065 | VOI D | `wenduag.vellexia_network.reception` | ROUTE | — |
| yaniel:001 | CAN | `yaniel.trickster.beat.areelu` | ROUTE | — |
| yaniel:002 | INT | `yaniel.trickster.beat.areelu` | ROUTE | — |
| yaniel:003 | INT | `yaniel.trickster.beat.areelu` | ROUTE | — |
| yaniel:004 | INT | `yaniel.trickster.ch5.found` | ROUTE | — |
| yaniel:005 | INT | `yaniel.trickster.beat.drill` | ROUTE | — |
| yaniel:006 | INT | `yaniel.trickster.beat.drill` | ROUTE | — |
| yaniel:007 | INT | `yaniel.trickster.beat.church` | ROUTE | — |
| yaniel:008 | INT | `yaniel.trickster.beat.church` | ROUTE | — |
| yaniel:009 | INT | `yaniel.trickster.epilogue.distrusted` | ROUTE | — |
| yaniel:010 | INT | `yaniel.trickster.epilogue.unsettled` | ROUTE | — |
| yaniel:011 | INT | `yaniel.trickster.beat.night` | ROUTE | — |
| yaniel:012 | INT | `yaniel.trickster.beat.night` | ROUTE | — |
| yaniel:013 | INT | `yaniel.trickster.beat.hunter` | ROUTE | — |

# Seelah polish round 2 — implementation report

All new situations and romance dialogue are authored additions, not native romance.
Reservation: **act_before_confession**, Drezen companion-hub penance-list reckoning and borrowed room; existing Fye stairs for outside-party courtship. The copied atlas entry is authoritative over the fallback turning-point sheet. No echo or Shyka-based affection, invented partner, pair scene, attraction score, new payment, or compulsory outing was added.

## CHANGES

- `storylines/seelah_round2.py`: route-local situation and receipt implementation, called by `seelah_trickster.py`. Original scene/node order, old answer indices, ending exits and native costs survive.
- **SP1 / SEE-01:** optional native beer-cart party evening: Curl keeps the mugs, Jannah supplies the beat, Elan watches the door; Seelah takes the initiative in dancing or walking. The existing wager's dance finishes with her competence rather than a furniture accident.
- **SP2 / SEE-03:** one optional bad-cup morning at Jannah's actual contact, Chapter 1 only. Cover/help/leave all let Seelah face her friend and do the missed work; no sex or relationship score follows intoxication. The existing promise/kept supper and kiss now carry impatience and reciprocal appetite while retaining help/delegate/reschedule/wait.
- **SP3:** borrowed-room approach, heated default slot and original sleep/terminal mechanics; ordinary morning offers physical recollection only after `private_night`. Quiet and changed-body branches do not enter the slot.
- **SP4 / SEE-04:** native Elan harsh-treatment answer is observed directly; optional weight/souls confrontation allows correction or the existing romance closure. Existing Abyss watch and native quest-outcome reckoning retain their distinct work and grief. The souls survivor gesture is no longer the shared head-shake formula.
- **SP5:** Seelah actually takes back her penance list, then keeps it private or chooses the pocket game herself. The ordinary door, both road futures, afterglow and late commitment require custody settlement only when it is outstanding. Outside-party courtship uses the same settlement. **P8–11/P22, F2–5; eng3 settlement residual.**
- Returning the list leaves appended repayment-refusal, postponement and friendship answers in both commitment twins. Refusal reasons are distinct; first-coin refusal receives a physical wage/chapel receipt before renewed invitation, while the freedom refusal has her unsummoned return and the withheld-list refusal has its own return/acknowledgment. The 96-hour interval alone grants neither receipt nor commitment. **P12–15, F6–9; eng3 repayment residual.**
- **SP5–6 / SEE-02:** four outside-party threshold variants have their own slot defaults; morning muster calls her back to her chosen near/far posting. Seven upstream brief JSON files are retained. The postwar slot remains an epilogue paragraph; the six encounter slots are dedicated appended nodes. First-night language is not repeated in later encounters. Ordinary full, short, quiet and changed-body outcomes remain distinct.
- Living together/unsettled/grieving/unfinished-work codas now show an actual return while preserving native quest outcomes, rare visits and independent duty. Refusal and parted codas carry the actual history rather than unexplained purses or a fabricated refused price. **P21/P23–24, F10–11/F16–17.**
- Company selection cannot supply late romantic eligibility without prior romantic history; sacrifice's pillow paragraph also requires that history. **P6–7.**
- Aeon remembered/forgotten prose reads the verified native memory flag, leaving the original ending exit intact. **P1.** Native plot departure is added to this relationship's unavailable flags and route-local consumers, with no automatic return or romance override. **P2 (shared current-presence consumer work remains below).**
- The outside-party presence uses the verified SeelahLocator and survives commitment; retained revived companions are excluded. The living courier is staged at Fye’s verified native main dialogue (`BartenderFye/AnswersList_0021`, `9b15b09c244076047b02f317e55ef5e3`), rather than spawning behind Seelah’s death guard. The bad-cup morning uses the verified native party list and Jannah contact. Effects reply/arrival are physical courier conversations with the original 96h/48h delays and distinct dispatch/arrival receipts. Failed-anchor mailbag twins retain their IDs and nodes but are retired by gating once the physical presence is wanted. **P4/P30–37, F1/F19–26.**
- Caught papers distinguish the actually taught and untaught lifts. Parting asks for a future appointment instead of claiming three unseen cold suppers. **P16, F18.**
- Interrupted seller acquisition resumes at the outstanding rite payment, preserving DC15/25, arrest 50 Favors, buy-off 500 Finances, Diamond/100-Favors payment and existing consequences. Chapel credit is recorded only on successful debit; a diamond acquired on retry is used. **P27–29.** The unrelated `iomedae.closed` condition was already absent in this base: no change needed for **P25–26/F27–28**.
- `tests/test_seelah_round2.py`: eight quick route-only graph/state walks for custody, appended refusal, reason-specific repayment, free return, debit/diamond retry, wanted presence/contact derivation, slot continuity and quiet branch isolation.
- `tools/route_packs/`: copied set-piece sheet, documented committed turning-point fallback, fixed atlas reservation, seven briefs and this report. The requested remote turning-point ref has no sheet; `4ed0617` was read without integrating code.

## CLASS SWEEP

Checked retained/effects returns; immediate-return/kept/reclaimed/private/game list custody; ordinary full/short futures; all four threshold twins; all seven slot joins; taught/untaught papers; clean/concealed/arrested/bought seller outcomes and both funding roads; physical/retired visit histories; near/far postings; developed/short/unfinished/grieving/changed/Aeon/sacrifice endings; no-partner canon facts; first-night versus return language. Legacy nodes and exits remain present. Original `seelah_trickster.py` remains wholly CRLF; copied files retain upstream bytes.

## GATE

All source/export checks used `PYTHONHASHSEED=0`, `/wrath` as the game directory, disabled bytecode output and a system-temp export. Parent bindings match the four existing manifests selected by `build-expansion.ps1`.

- `python expansion.py`: PASS, final export 3,760 scenes. `RRT_STORY_OUTPUT` points outside the repository; no generated `development/Story.json` edit.
- `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io tests.test_seelah_round2 -q`: PASS, 19 tests, 135.028s. After the final attachment fixes, the route module alone passes all **8** tests in 0.013s, and the final export passes the complete frozen save-reference check with **0** failures.
- `python tools/payoff_lint.py --strict --story <temp>/Story.json`: PASS, **0 hard failures**, including the final corrected export. Existing cross-route REVIEW rows are unchanged.
- `python tools/departure_lint.py --strict --story <temp>/Story.json`: BLOCKED, **5 hard failures**, all the unclassified new Seelah surfaces listed under ESCALATE. The final source explicitly requires current body presence on each; the shared inventory file is outside scope.
- `python tools/rrt_verify.py --strict --story <temp>/Story.json --game /wrath`: run **once**, 467.4s. It found six structural attachment errors: unsupported courier presence/hub naming and the missing bad-cup attachment. All six are fixed using verified native Fye/party lists. The same verifier's `validate(Model(final_export))` returns **0 structural hard failures** on the regenerated final export; final frozen save compatibility is also **0**. The other checks in the full run had no hard failures. The full strict command was not repeated because the binding writing-phase instructions require it once; coordinator confirmation of the complete final strict run remains necessary.
- Original CRLF retained; changed paths all match the allow list. No `__pycache__`, `obj` or `bin` folders were left in the repository. System-temp export/logs and the verifier's temporary report were deleted before completion.

The task-named `WRITING-PHASE-GATES.md` explicitly supersedes the full-suite footer: no unittest discover, RulesTests, managed tests, full build, harness, game, or commit.

## ESCALATE

- Departure lint requires append-only registration in excluded `tools/departure_contracts.json`, `women.seelah.surfaces`, for: `seelah.trickster.dead.list_reclaimed`, `seelah.trickster.after.list_reclaimed`, `seelah.trickster.dismissed.second_ask_paid`, `seelah.early.cart_evening`, `seelah.early.bad_cup`, each `{ "scene": "<id>", "letter": false }`. All five source scenes already require `seelah.present_now`. This is inventory registration for the task-required new scenes, not a request for a new gate. The allowed route source cannot update that shared registry, so departure strict reports five unclassified surfaces.

- **P17–20/P21, F12–16, eng3 Last Call/ledger residual:** shared `lastcall*` and `trickster_world.py` must partition the Seelah call, flask/coda and owed/journal entries by spoken outstanding vow versus returned/reclaimed/game/no-unit history. Collect the actual list and mark settlement; do not use an unidentified flask coin or universal daily cohabitation/theft vocation. Those explicitly excluded shared sources were not edited or monkey-patched.
- **P3 and remaining P2 shared readers:** engine departure contracts must include the verified plot departure alongside current loss epochs for every shared presence/household/finale consumer. A historical return is not permanent life. Existing engine round-3 guards are retained; no subsequent resurrection device was invented.
- **P5/F1 runtime fixture portion:** the new quick test derives contacts from wanted presence rather than seeding them independently. Full retained-actor/presence lifecycle validation belongs to the forbidden managed fixture / RulesTests milestone.

## PROPOSE

None. No new romance design, gate, price, blackmail layer, partner or household mechanics proposed.

## RISKS

Shared Last Call/ledger defects and the required departure-inventory registration above remain and prevent claiming all findings closed, every gate green, or a >=91 independent score. The final full strict confirmation belongs to the coordinator; its affected structural validator passes. SeelahLocator and native courier/party attachment behavior need the milestone runtime check; a failed locator does not earn a free fallback arrival. Brief replacement needs continuity/voice/anatomy review; defaults remain usable. The route-only tests are authoring graph/state checks, not game execution. No independent audit or score is claimed. No commit was made.

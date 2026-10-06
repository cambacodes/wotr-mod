# Dorgelinda Stranglehold — round 2 implementation

## CHANGES

Finding references below are the one-based `defects` entries in `dorgelindap1.json` (P) and `dorgelindaf1.json` (F). Authored scenes and gestures expand the route; they are not additional native canon. Native injuries, veteran-quartermaster voice, council outcomes and romance readers were checked against `blueprints.zip` and `enGB.json`.

| File | Change, reason and findings |
|---|---|
| `storylines/dorgelinda_trickster.py` | Professional accounting no longer supplies late romantic eligibility: accepted commitment is required (P1–3; F4–6; engine-3 residual). Conscience takes precedence; the ledger binds the actual requisition outcome rather than the crisis report (P4). Stocktake addresses the party's real issue and current returns without an irrelevant Galfrey romance dependency (P5–6; F12–13). |
| `storylines/dorgelinda_trickster.py` | Registered **canon_lowest_point** remains the Chapter 5 Drezen second-book meeting. Her own recovered troop crate, separate private bottle, own handwriting and retained signed returns replace the convenient Fellows book. She owns either reserve decision, closes the book and invites a private drink without granting romance. This implements DOR-01, the fixed registry and set piece 3 (F33). |
| `storylines/dorgelinda_trickster.py` | Paid second-ask disclosure precedes her spoken yes, kiss and cup transfer; a new acceptance node follows the legacy request index. Both direct yes answers accept the offered cup (P7–9; F29). Original nodes and the generated legacy departure answer remain. Deferred rejection remains unanswered in its ending. |
| `storylines/dorgelinda_ledger.py` | Shipment credits now occur once at arrival, including the forged shipment. Allotment cuts debit 150 Materials and 50 Finances once, independently of quarrel outcome; both repair paths restore only 50 Materials of powder, once. Jest success leaves 50 Finances wine owing; failure leaves the original 200 owing. Immediate or later treasury payment settles the recorded debt; insufficient funds still permit leaving it owing (P10,13–16; F15–21). These quantify existing stated obligations. |
| `storylines/dorgelinda_ledger.py` | Return-all is now a real appended answer and outcome. It reverses the previously credited 150 Materials only when that reserve was booked. Her confession reads actual requisitions, retained barrels or the dirty reserve; restrained histories get a different concern. Donation-era stock does not become starvation by fiat, including the skipped-meal sibling: its new response concerns missing mess during kit issue. Inquiry retains signed originals and corrected tally (P11–12,19; F1–3,30,32; DOR-04). |
| `storylines/dorgelinda_ledger.py` | Other-columns denials read actual currently open romantic entitlement plus relevant native romances. Solo answers remain truthful; a real lie is admitted on page before cup recall. Ordered, acyclic disclosure names each actual partner, with particular objections to demon-lord, demon and royal cases before existing terms. The new `changed_columns` office scene collects the existing promise when a sole arrangement gains another lover (P17–18; F7–10). No spouse, exclusivity, enmity, attraction or reconciliation rule was added. |
| `storylines/dorgelinda_ledger.py` | DOR-03 night: her initiative, bolted door, heated cut and warm morning kiss; she owns the missed count and makes the requested campaign-saddle joke. Added **`dorgelinda.ledger.after_hours.explicit.1`**, with first-night completion on its continuation exactly once. No explicit prose authored. Farewell now prepares a future march throughout; she remains at her Drezen desk. Existing cold/private/narrowed refusals remain distinct. Living homecoming and chosen private nights appear only in permitted endings (P26; F11,25,34; set pieces 4–6). |
| `tests/test_dorgelinda_round2.py` | Ten focused history tests cover accepted commitment, payment/acceptance separation, native recovery precedence, delivery, both repairs, bill settlement, truthful solitude, actual partner disclosure and later change, graph reachability, and the exact slot/brief cut. |
| `tests/DorgelindaTricksterTests.cs` | Update acceptance and slot assertions; separate actual concurrent-romance and solo-disclosure fixtures. Existing tests' old innocent-word ceiling was already absent (F35). |
| `tools/route_packs/plans/dorgelinda-stranglehold-{setpieces,tp}.md` | Copy the supplied plans without rewriting their design. The later atlas fixes the device class where the older TP sheet differs. |
| `tools/route_packs/turning_points.json` | Preserve the exact atlas entry for this route: class, office setting and ownership/cup payoff. |
| `tools/route_packs/explicit_slots/dorgelinda-stranglehold/dorgelinda.ledger.after_hours.explicit.1.json` | Copy the supplied brief unchanged. Heated default ends exactly on `The last cart rattles away outside.` |

Set pieces 1–2 retain the existing witnessed entry, appointment, hand/pen/fitting visits, packed Abyss note and west-gate spear scene; the round adds the physical second-book situation, separately chosen drink, corrected stock and consequential inquiry around them. A signed receipt is ordinary evidence, never a sending or resurrection device (DOR-02). No echo or foresight was introduced.

Already present corrections were checked and retained rather than rewritten for churn: `ordered_to_eat`'s later objection, the soldier's ordinary boot requisition, prospective divine-bargain wording, Bartley's specific letter and crimes, and her-name inquiry cost (F22–24,30–31). No minor or friendship-only character enters sexual material.

## CLASS SWEEP

- Checked both direct and deferred acceptance paths, professional-only histories, closure, Guest List and all late-commitment readers. Shared professional ending classification remains escalated below.
- Swept shortage/recovery siblings in stocktake, second book, receipts, barrels, faith and inquiry; used actual council outcome and restrained/predatory history.
- Checked every shipment and bill outcome, both quarrel repairs, interrupted/replayed payments and unfunded exits. Payment is crusade treasury spending, separate from romantic acceptance.
- Checked both legacy solo denials, native and authored romances, route closure/return guards, full and sparse partner rosters, and sole-then-another disclosure. Names are information supplied by the Commander, not bodily visitors.
- Checked all farewell departure claims and warm/cold/private/narrowed endings. No paid account is reopened in route-local endings; no dead Commander or absent woman is staged as returned.
- Swept the supplied heat census, refusal siblings, first-night completion and brief end marker. Preserved CRLF bytes, original scene/node order, saved choice indices and legacy ending mechanics.

## GATE

Generation and reports use system temp; `development/Story.json` is untouched. `PYTHONHASHSEED=0` and `PYTHONDONTWRITEBYTECODE=1` are set. Parent-binding reference files are supplied through `RRT_PARENT_BINDINGS`. No commit, harness, game or `build-expansion.ps1` run.

| Command | Final result |
|---|---|
| `python expansion.py` with `RRT_STORY_OUTPUT` in system temp | PASS, exit 0; 3,757 scenes. Exporter labels this an incomplete development export; no installed build produced. |
| `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io` | PASS, 12 tests; final source. |
| `python -m unittest tests.test_dorgelinda_round2 tests.test_dorgelinda_polish tests.test_utf8_io -q` | PASS, 17 tests. |
| `python tools/payoff_lint.py --strict --story <temp export>` | PASS; 42 routes, 0 hard failures. |
| `python tools/departure_lint.py --strict --story <temp export>` | FAIL; 43 women, 2 hard failures, both frozen inventory registrations in ESCALATE 1. |
| `python tools/rrt_verify.py --strict --story <temp export> --game /wrath` | Full report: save compatibility and structure clean; 1 hard lifecycle failure on the native Arueshalae first-warning child. Removed that incorrect failure reader; native breakup completes the active romance parent. Earlier removed legacy exit, missing native reader and unreachable copied follow-up nodes were repaired too. Final `--strict --gate-only` rerun executes every strict check, deferring only report-only analyses; result recorded below. |
| Final `python tools/rrt_verify.py --strict --gate-only --story <temp export> --game /wrath` | PASS, exit 0, **0 hard failures**; 186.1 seconds. All strict checks run; intimacy, memory and transaction contracts also report 0 hard. |
| `python -m unittest discover -s tests -p 'test_*.py' -q` (also diagnostic `-v`) | INCOMPLETE: repeated runs terminated with exit 143 without a test-result summary. Verbose run last reported the Delamere module passing. No full-suite success claimed. |
| `dotnet run --project tests/RulesTests.csproj -c Release` with temp output properties / `--artifacts-path` | Project builds (0 errors); CLI nevertheless tries the absent repository `tests/bin` executable. No repository build folder created to work around it. |
| Equivalent full runner: `dotnet <temp>/RulesTests.dll <temp export>` | INCOMPLETE: exit 1 after shared engine checks, without a reported failing assertion; profiled retry terminated with exit 143. No full progression verdict claimed. |
| `dotnet <temp>/RulesTests.dll --suites DorgelindaTricksterTests <temp export>` | PASS, 12,727 assertions; final export. |
| `git -c core.whitespace=cr-at-eol diff --check` | PASS; original three source/test files retain CRLF exactly. |

## ESCALATE

1. `tools/departure_contracts.json` must classify **`dorgelinda.ledger.cellar_settlement`** and **`dorgelinda.ledger.changed_columns`** as presence surfaces. Both require `dorgelinda.present_now`; the frozen shared inventory nevertheless reports two hard failures for unregistered scene IDs. This file is outside the allowlist.
2. Shared payoff classification still requires romantic `dorgelinda.payoff.partner` on legacy **`dorgelinda.trickster.epilogue.commit`**, while that professional page forbids commitment. Removing governance-only romance exposes that existing mismatch. Coordinator must preserve a professional coda and its exit mechanics without awarding an unchosen lover (P1–3; F4–6). No shared engine/contract edited.
3. Shared Last Call/owed consumers need settled-account wording and readers; distinguish `told_all`, paid boots, frequency and cold/private/narrowed state. Replace the remote ledger response and “somehow” evening reunion with an ordinary report and actual Drezen return, respecting heroic recovery. Historical professional methods must not supply romance (P2,20–25; F6,26–28). These are `lastcall*`/shared household ownership and explicitly excluded here.
4. External route specification and audit notes should record the new deferred acceptance/cup node, the real receipts, and treasury payer; they are outside the editable tree.
5. Milestone owner must complete the unfiltered suites and resolve the temp-output launch behavior. Python discovery repeatedly terminated with exit 143; the full rules runner returned exit 1 without a failing assertion, and its profiled retry terminated with exit 143. This route's quick Python and C# suites pass; no complete-suite or universal progression verdict is substituted for those interrupted runs.

## PROPOSE

None. No additional mechanics, gates, prices, relationship requirements or reconciliation design proposed or implemented beyond the supplied findings.

## RISKS

- Departure inventory and professional-coda classification require coordinator integration; this branch cannot claim all gates clean until those shared residuals are resolved.
- Resource calibration (150 Materials/50 Finances lost; 50 Materials recovered; 50 wine/200 full bill) needs coordinator economy review. It implements the existing promises, without adding a romance payment.
- Partner disclosure consumes other routes' shared earned/open eligibility. Those contracts remain their owners' responsibility; native Arueshalae has an independently verified local active-parent reader; native breakup completes the parent, while its Fail child is only a first warning.
- No independent score or live-game verification claimed. Explicit slot remains a heated default awaiting the coordinator's separate prose batch.

Final cleanup removed the system-temp exports, audit logs, build output and editing scripts. No `obj`, `bin`, cache or audit-output folder remains inside the repository. Changes are uncommitted, as requested.

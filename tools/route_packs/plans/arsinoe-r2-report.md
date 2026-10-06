# Arsinoe round 2 implementation

## CHANGES

- `storylines/arsinoe_opening.py`: p1/f1 courtship-memory and sameness sweep; the rooftop grip has her practical pride and ends at Tovin's lamp. The first kiss retains its slipped-book interruption. f1:14–15: append-only resume answers preserve acknowledged print observations and picture selections after interruption; competing results cannot be recorded on reopening.
- `storylines/arsinoe_continuation.py`: set pieces 2–3, ARS-01/02/03. The existing account carries Neral's actual payment and answers an insinuation about temple funds, without a forged record, another bill, or a new investigation. Arsinoe spends her own money on finery and drink, hands the next gathering back to its guests, and pursues the Commander. An appended optional overnight answer follows the existing kiss. The old kiss-only exit retains its index and effects. New morning receipt `arsinoe.unprofitable_night_shared` records that event alone; no commitment derives from it. The alarm remains her duty.
- `storylines/arsinoe_campaign.py`: f1:0 uses `trickster.now` for fresh stone power; ordinary carving remains available after loss of the path. Set pieces 4–5 keep the repair and her decision to decline the other appointment separate from affection. Her future question concerns their company, not a reward for repairs. The window night has staging, a dedicated slot, and a reachable morning at the original terminal node/answer with its original receipt. Returning nights read actual earlier mornings. Kept/open/promised/unfinished endings show a return; promised/unfinished visits claim neither an unplayed night nor a completed window.
- `storylines/arsinoe_trickster.py`: p1:1 / f1:6–7: accepted physical arrival now precedes courtship callbacks at the same paragraph indices; the last arrival paragraph becomes her purpose tonight. Declined history remains business. f1:3–5: ordinary future terms supersede late-only classification and artifact invitations; ordinary commitment stays independent. Set pieces 5–6 give the non-lover collection flirt her own answer, preserve commercial liabilities, add the collection/immediate/deferred slots, and show her morning affection and return to work. The deferred appointment still occurs four weeks after supper. The intimacy union includes the early morning and supplies first/return variants without manufacturing commitment.
- `tools/route_packs/plans/arsinoe-setpieces.md`, `arsinoe-tp.md`, and `explicit_slots/arsinoe/*.json`: copied the supplied plans and all five briefs from their specified refs. Slot defaults retain each brief's exact final line. No explicit prose was written. Canon identity, vanity, itinerant ministry, artifact conjecture and Lann's wedding ownership were checked directly in `/wrath/blueprints.zip` and `enGB.json`.
- `tests/test_arsinoe_round2.py`: route histories cover interrupted success/failure and both print selections; courting/slow/friend approaches; optional night versus kiss-only; window/collection first and return; business collection; accepted immediate/deferred versus declined late menus; lost-path ordinary carving; and five slot/brief continuity contracts.

## CLASS SWEEP

- Checked all four route modules, every intimacy threshold/morning and ending sibling, ordinary/late partnership readers, print/check siblings, the stone-power alternatives, rent/grace/surcharge/collateral receipts, returned/burst/called/uncalled lease dispositions, soul-victim integration, and allocated Konomi reactions.
- Existing f1:8–13 and 17–20 fixes are present in the base: Threshold discount chronology, queue-specific wording, cancelled leases, both night receipts and aftermath correspondence, and removal of demographic certifications. Preserved those fixes and their paid gates.
- Registration stays `act_before_confession`; setting stays `Drezen vendor's after-hours room, repaired window and travel book`; payoff stays `private unprofitable hour becomes recurring evenings with customers still waiting`. No Shyka gate, echo, vision, magical desire, partner invention, or new romance qualification.
- Save references and original ending exit mechanics remain. Opening/campaign LF and continuation/Trickster CRLF are preserved.

## GATE

Generated exports and build/log outputs use system temporary storage, because `development/Story.json` is outside the edit allow list. No commit, game, harness, or build-expansion script is run. The final user instruction requesting discovery/RulesTests and prohibiting a commit takes precedence over the earlier writing-phase list.

| Command/check | Result |
| --- | --- |
| `PYTHONHASHSEED=0 python expansion.py` with `RRT_STORY_OUTPUT` in system temp and the four build-script parent bindings | PASS; 3,755 scenes; generator labels the export `INCOMPLETE DEVELOPMENT EXPORT`, as in the integration base |
| `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io tests.test_arsinoe_round2 -q` | PASS; 19 tests |
| Final route/UTF-8 rerun | PASS; 8 tests |
| HEAD identity/newline sweep | PASS; 342 legacy choices, all scene/node order and legacy ending exit mechanics, original per-file newline conventions |
| `python tools/payoff_lint.py --strict --story <temporary export>` | PASS; 42 routes, 0 hard failures; other-route REVIEW debt remains visible |
| `python tools/departure_lint.py --strict --story <temporary export>` | PASS; 43 women, 0 hard failures; unrelated opaque Mielarah loss remains REVIEW |
| `python -m unittest discover -s tests -p 'test_*.py' -q` | INCOMPLETE; repeated runs terminated with exit 143/no test result; isolated retry also ended without its result file |
| `dotnet run --project tests/RulesTests.csproj -c Release ... -- <temporary export>` | Build succeeded outside the repo, but `dotnet run` tried the default repo executable path despite relocated output. Executed the resulting `RulesTests.dll` directly; unfiltered validation repeatedly terminated before completion. Its opening engine suites passed; no complete rules/progression pass is claimed. |
| `dotnet <temporary RulesTests.dll> --suites ArsinoePolishTests <temporary export>` | PASS; 7,625 assertions |
| Remaining selected Arsinoe rules suites | INCOMPLETE; assembled suite passed 3,053 assertions, then the process terminated with exit 143 |
| `python tools/rrt_verify.py --strict --story <temporary export>` | PASS; 0 hard failures, 0 shipped structural errors, 0 draft contract diagnostics; intimacy/memory/transaction contracts each 0 hard; 588.2 seconds |

The final export restores the original Konomi office predicate. One earlier verifier invocation was cancelled after that dependency correction; the final invocation checks the final export. No hard-failure result is inferred from an interrupted gate. `git -c core.whitespace=cr-at-eol diff --check` passes; plain Git whitespace checks treat required CRLF as trailing whitespace.

## ESCALATE

- p1:0 / f1:1–2,11–13,16: shared `storylines/crossroute_presence.py` still appends `crossroute.konomi.unavailable` to the inspection and both professional reactions. The inspection's paid rider is historical expense, not Konomi's presence. A living Konomi's romance refusal is not office departure. The original office predicate is retained: changing it locally while the shared pass still vetoes the witnessed yes would remove the fallback yes after a romantic refusal. Correct both layers together. Its classification and related C# expectations need a coordinated shared fix. Dismissal, current/persistent death and earned return still matter; do not merely remove all loss guards.
- p1:2: `storylines/earned_outcomes.py` appends the duplicate spring visit to `arsinoe.lastcall.page`, following the recap in `lastcall_partners.py`. Replace the appended text at its existing index with recurring kept closing hours and return to work. Engine round 3 already supersedes its romantic visibility after `future_spoken`; neither shared source was edited here.
- The central turning-point registry is coordinator-owned. This implementation retains the reserved device/setting/payoff; it does not replace another route's reservation or add shared registry machinery.

## PROPOSE

None. No additional mechanics, payments, honesty tests, infidelity system, travel gate, attraction threshold, or reconciliation condition was implemented.

## RISKS

- The shared residuals prevent claiming the full audit union is resolved or every dimension is at least 91. Independent prose/diff review remains required.
- Python discovery and complete C# rules/progression validation did not finish despite retries; the coordinator must complete those gates. No `Page has no selectable answers` failure was reported in the results obtained. The focused Arsinoe polish suite and new Python branch walkers passed, but do not substitute for the incomplete global gates.
- Explicit content remains external: five self-contained heated cuts and their briefs are ready for the coordinator's chosen insertion process. Insertion must preserve slot IDs, exact last lines, speaker ownership, first/return history and continuation receipts.
- Shared and other-route gate failures cannot be repaired within this route's authorization. They must remain visible in the coordinator's gate report.

# Arsinoe round 3

Branch: `claude/r3-arsinoe`. Changes are uncommitted, as requested.

## CHANGES

Finding numbers below are one-based positions in `arsinoer2.json`'s `defects` array.

| Finding | Status | File / disposition |
| --- | --- | --- |
| HEAT cap (VOI/BEL 80) | Fixed by explicit-slot briefs; fill pending | Retained all five stable slot IDs. Revised briefs describe the missing approach and initiation rather than generating explicit prose. Late epilogue briefs require `narration: third-past`. No new intimacy eligibility or commitment effects. |
| 1: historical Konomi invoice veto | Fixed | `storylines/arsinoe_trickster.py`: identifies the old invoice and Konomi's name on it as a record. The existing reference classifier now excludes this historical mention, so generation omits the unrelated scene-wide availability veto. The earned recall-payment condition remains. Added closed/dead/dismissed, receipt/no-receipt production-rules cases in `tests/ArsinoeRound3Tests.cs`. |
| 2: unprofitable-hour premature fade | Fixed by slot + brief | `storylines/arsinoe_continuation.py` and its existing explicit-slot JSON: her chosen silk and pleasure in being admired lead into the existing cut. Brief requires the full physical approach and initiation before the act, followed by the existing clasp/customer morning. Legacy kiss-and-leave answer unchanged. |
| 3: deferred late evening premature fade | Fixed by slot + brief | `storylines/arsinoe_trickster.py` and `late.commit.explicit.2.json`: retain the four-week appointment, give her anticipation a personal response, continue at the bedside, and brief its distinct intimate progression. Breakfast and legacy effects unchanged. |
| 4: window staging rewind | Fixed | `storylines/arsinoe_campaign.py`: patrol observation precedes the approach for both invitation/return histories. The stable slot continues their existing position instead of drawing them onto the bed again. Brief supplies the single initiation at the boundary. |
| 5: collection staging rewind | Fixed | `storylines/arsinoe_trickster.py`: ledger is already put aside in both threshold histories. The stable slot keeps her astride the Commander; no repeated counter seating or renewed advance after initiation. Updated its brief. |
| 6: immediate late staging rewind | Fixed | `storylines/arsinoe_trickster.py`: both first-time and returning approaches stop before initiation; the stable slot retains her position over the Commander. No invented departure and return to their arms. Updated its brief. |
| 7: payment before disclosed price | Fixed | `storylines/arsinoe_trickster.py`: states the first 500-crown charge before the paid choice; that answer explicitly accepts payment now. The subsequent rent page acknowledges the first payment and negotiates renewals. Existing -500 debit, failed-haggle -200 surcharge, alignment effect, receipts and interrupted-payment paths remain unchanged. `tests/test_arsinoe_round2.py` checks disclosure order. |
| 8: estate rental paragraph unreachable | Verified-fixed | Current export has no sacrifice veto on `pot_returned`; estate paragraph 2 retains sacrifice/no-return conditions. No prose changed. |
| 9: estate pledged-word disposition unreachable | Verified-fixed | Same documentary page admits genuine death; paragraph 6 releases the security without a living encounter. Personal paragraphs retain individual survival guards. |
| 10: estate grace disposition unreachable | Verified-fixed | Paragraph 15 admits earned grace after unreturned sacrifice. `tests/ArsinoeRound3Tests.cs` adds one production-rules history asserting page availability and all three estate paragraphs, excluding living invitations. |
| 11: accepted coda page-set assertion | Fixed | `tests/ArsinoeTricksterTests.cs`: separate first-time and returning page sets; exclude each mutually exclusive alternate and refusal. Python route walker also checks both histories. |
| 12: obsolete offer-to-table assertion | Fixed | Same tests assert `offer -> deferred_evening -> explicit.2 -> table`, and the conditional `late_return` destination. |
| 13: obsolete direct night-to-morning assertion | Fixed | Same tests assert both approaches traverse the stable `explicit.1` slot to morning. |

## CLASS SWEEP

- All five intimacy slots; both window, collection and immediate-late histories; deferred month-long appointment; all morning receipts; declined/business and ordinary friendship/slow histories.
- Lease proposal, fixed payment, successful grace negotiation, failed surcharge, and interrupted-payment resumes. No changes to existing charges or resource/receipt placement.
- Documentary returned-stone page and its rent, word, grace and invitation siblings, including genuine death, earned Commander return and former-Trickster history.
- Konomi's historical rider with/without its paid receipt and closed/dead/dismissed histories. Her separate live office reactions retain their existing presence gates.
- Canon checked against `/wrath/blueprints.zip`'s VendorArsinoe Cue_0001 and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`'s introduction, aasimar/vanity and Drezen-order lines. No new canon facts, foresight, echo, resurrection or partner mechanics.
- Scene/node/relationship IDs, node order, answer indices and legacy exits retained. CRLF preserved in Trickster/continuation/C# files; campaign and Python tests retain LF.

## GATE

All exports used `PYTHONHASHSEED=0`; final generation also used `PYTHONUTF8=1`, `/wrath` game data and the four existing parent manifests from `build-expansion.ps1`.

- `python expansion.py`: PASS, 3,848 scenes generated from final route sources.
- `python -m unittest discover -s tests -p "test_arsinoe*.py" -q`: PASS, 8 tests.
- `python -m unittest discover -s tests -p "test_*.py" -q`: two attempts interrupted, exit 143 (SIGTERM), no test summary. No Python failure assertion was reported; this is not a passing full discovery.
- `tools.savecompat.check` against final export: PASS, 0 hard failures. HEAD/source comparison also confirms identical scene/node ordering, answer identities and all choice mechanics in all four route modules. Changed source/brief files decode as UTF-8; existing CRLF/LF conventions retained.
- `python tools/payoff_lint.py --strict` and `python tools/departure_lint.py --strict`: PASS, 0 hard failures each. Rechecked both contracts against the final export: 0 hard failures.
- `python tools/rrt_verify.py --strict`: PASS, **0 hard failures**, structural validation 0 errors, intimacy/memory/transaction contracts 0 hard failures; runtime 738.4 seconds. Ran once on the final export.
- Required `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json`: invoked with MSBuild output/intermediate paths supplied through environment variables under `/tmp/arsinoe-r3-dotnet`. Final-export invocation interrupted with exit 143 after shared epoch/coarse-payoff checks reported passing; no complete rules/progression result.
- Focused `dotnet run ... -- --suites ArsinoeRound3Tests development/Story.json`: PASS, 153 assertions.
- Inherited `ArsinoeTricksterTests`: reaches 734 assertions, then fails on the existing other-route producer fixture: `konomi.trickster.dismissed.late -> konomi.trickster.back_from_the_road`. The round-2 audit already reported that blocker. No unrelated Konomi source or shared test helper altered.
- `ArsinoeRound3Tests,ArsinoeAssembledTests`: final combined run PASS, 3,206 assertions in two suites (153 round-3, 3,053 assembled). Broader campaign/opening/continuation/polish selection also exited 143 without a complete result.

No `Page has no selectable answers` diagnostic was reported, but interrupted broad runs do not establish complete progression validation.

## ESCALATE

- Repair the shared Konomi return-producer fixture/path, outside this route's scope, so the inherited Trickster suite can finish.
- Investigate exit-143 interruptions in full Python discovery and broad C# rules/route selections, then rerun the required broad gates. No unsupported timeout/OOM diagnosis is asserted.
- Supply the missing `tools/route_packs/voice_locks.json` inventory for the coordinator's lock comparison.

## PROPOSE

None. No unrequested design changes implemented.

## RISKS

- Explicit prose is intentionally left to the user's fill workflow. All existing briefs/slots remain linked; heat scoring after fill requires independent review. No new audit scores are claimed.
- `tools/route_packs/voice_locks.json` is absent from this checkout; no named locked-scene inventory was available to verify. No shared or other-route prose was edited.
- No commit, full build, harness, game launch or installation. Generated export is used only for gates and restored afterwards to keep the final diff inside the allow list.

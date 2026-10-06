# Delamere — round 2 implementation

Uncommitted. Only Delamere source, tests and route-pack entries changed. Existing CRLF retained. No shared storylines, engine source, repository-generated exports or other routes edited.

## CHANGES

| File | Situation / findings |
|---|---|
| storylines/delamere_trickster.py | SP1: snapshots Kyado's lifetime at successful waking before refusal; native Zanedra death **UnlockableFlag** and heard-west cue (p1:1,2,4); Drezen remains locality (f1:1). SP6: late first night, settlement confrontation on road home, separate home and recurring hunt; camp venison paid; explicit paragraph. Atlas-0004 hunter-specific fatal accounts. Brace/name memory requires existing brace receipt. |
| storylines/delamere_woods.py | SP2: family/captain/well boundary dispute with four existing outcomes and unchanged costs. Judgment permits actual indoor sweeping/visitor service (p1:3). Separate dead-at-waking, later-dead, legacy-acquaintance and unknown-body branches (p1:4). Native report gates and bark's limited knowledge (p1:1,2). Areas/journeys survive folds (f1:2–6,8). Corrects false first-light recall (f1:17–19), stream promise (f1:20), twenty-one count (f1:21), chapel oath in all hunts (f1:22–24). SP3: blunt desire and her invitation. SP4: her initiating kiss, protected old leg, three slots, bodily aftermath and count-specific morning argument. SP5: blade sheathed before roof kissing; patrol/cold interruption and actual walk home. |
| storylines/delamere_fire.py | SP3: reserved supper seat; protective false field trail detected and corrected by her in the existing optional demon hunt (DEL-02). Clean/injured outcomes retain effects and checks. SP5: frank brace/time claim; locally spoken names without awarding household residence. Local areas and actual woods journeys (f1:7,9–13). Heat audit's euphemism/formal/coy classes rewritten. |
| tests/test_DelamereRound2.py | Replays native reports, waking snapshots/refusals, later death/old saves, three oath confrontations, catch/postponement/ownership exits, four boundary mornings, clean/injured optional hunt, slot briefs and ending invariants. |
| tests/DelamereTricksterTests.cs | Dead-at-waking burial fixture corrected; remote courtship fixtures use actual areas and check unrelated-dungeon negatives. |
| tests/DelamereRound2Tests.cs | Focused production Rules checks for local/distant availability, native reports, three first-night deliveries and four boundary mornings. |
| tools/route_packs/plans/delamere-{setpieces,tp}.md | Copies binding planning sheets; this report records implementation and residuals. |
| tools/route_packs/turning_points.json | Registers only Delamere's exact atlas allocation: she_pursues; new-moon stream hollow below the Temple; chosen catch then annual unfinished hunt. |
| tools/route_packs/explicit_slots/delamere/*.json | Copies four supplied briefs unchanged. Defaults are heated cuts; no explicit prose generated. |

SP1 retains the earned waking, limp and every refusal/healing exit. SP2 establishes the territorial dispute and provision/bow/names consequences. SP3 shows her desire and field competence. SP4 remains the registered reverse hunt and chosen catch followed by disagreement. SP5 collects the recurring day, brace and names. SP6 distinguishes caught/deferred/closed/healed/unfinished/fatal histories.

Collected locally: camp's next animal; Old Deadeye's offering; truth/confession before catch; chapel oath; stream promise; names at the brace; separate hearth; annual hunt; refugee consequences; native-supported witch reports; Kyado's actual lifetime.

**Engine round 3, L residual:** existing second_hunt_offered is produced only by the Commander's affirmative acceptance/boast after her on-page want and invitation. With existing truth/both/confession and open-route checks it earns the deferred road. Late supplies her actual return, renewed invitation and chosen catch; committed, closed and unreturned fatal histories remain excluded. No new acceptance gate, price or sex-derived receipt invented. Legacy ending exit identity AND mechanics remain unchanged.

Slots:
- delamere.trickster.woods.second_hunt.explicit.1
- delamere.trickster.woods.second_hunt_page.explicit.1
- delamere.trickster.woods.second_hunt_late.explicit.1
- delamere.trickster.epilogue.late.explicit.1

No canon spouse/current lover established by the binding inputs or checked native dialogue: partner discovery and stance inapplicable.

## CLASS SWEEP

Four waking deliveries; both count folds/standalone meat; folded/standalone supper/proposal; Red's exits; three tracking/horn/lie/oath/catch/refusal/morning deliveries; both frost histories and all answers; brace/name replies; bark/village; every legacy ending; both read-only Last Call pages.

Preserved already-resolved chapel/stone wording (f1:15,16) and non-counted horn recall (f1:25,26). Native anchors checked against /wrath/blueprints.zip and enGB: stag/offer/bow/hide, refusal of orders, harsh fifty-three law, city aversion, transported remains and intended westward withdrawal. Situations are authored additions. No Shyka/echo/vision added.

## GATE

Exports, verifier reports, logs and .NET obj/bin were directed to a disposable system temporary directory outside the repository. No generated repository file was edited.

| Command | Result |
|---|---|
| PYTHONHASHSEED=0 python expansion.py (RRT_STORY_OUTPUT points outside repo) | PASS: 3,755 scenes. |
| python -m unittest tests.test_savecompat_baseline tests.test_utf8_io -q | PASS: 12 tests on the final export. Final integration-relative identity check also reports 0 failures; all legacy ending exit mechanics equal the base. |
| python -m unittest tests.test_DelamerePolish tests.test_DelamereRound2 tests.test_utf8_io -q | PASS: 16 tests. |
| python tools/payoff_lint.py --strict --story TEMP/FinalStory.json | PASS: 0 hard; Delamere L interpretation documented above. |
| python tools/departure_lint.py --strict --story TEMP/FinalStory.json | PASS: 0 hard. |
| dotnet build tests/RulesTests.csproj -c Release (external obj/bin) | PASS: 0 warnings, 0 errors. |
| dotnet run --project tests/RulesTests.csproj -c Release --no-build -- TEMP/FinalStory.json --suites=DelamereRound2Tests | PASS: 3,970 assertions; production Rules and all new hunt mornings traversed. |
| python -m unittest discover -s tests -p test_*.py -q | INCOMPLETE: repeated SIGTERM, exit -15/143, without an assertion diagnostic. Sequential detached retry had the same result. |
| dotnet run --project tests/RulesTests.csproj -c Release --no-build -- TEMP/FinalStory.json | INCOMPLETE: SIGTERM/143 after three early engine validation groups. No reported page-without-selectable-answers diagnostic; cannot claim the broad suite passed. |
| python tools/rrt_verify.py --strict --gate-only --game /wrath --story TEMP/FinalStory.json | PASS: final run reports 0 hard failures. An earlier run found seven literal land-marker uses of boundary in the therapy-language budget; player text now uses stakes/marked paths, retaining every node ID. No shared lint change. |

The report-only verifier world/budget analyses were stopped after final prose review; gate-only performs all strict checks and omits those advisory analyses. The default Windows game-data path was corrected to the installed /wrath path.

## ESCALATE

- **p1:5–8:** shared nm1_fold/runtime must persist/advance four narrated waits and refresh native/path/chapter/area/closure state. Tomorrow's hare also needs actual elapsed time. Approved consolidation and old targets retained; prose does not repair runtime debt.
- **f1:14:** generated crossroute.iomedae.unavailable still mistakes a cathedral/priest for the goddess's presence. Shared generator exception needed.
- **f1:27:** coordinator must package reviewed living portrait and validate its key; no undead prefab shortcut.
- Shared household/name interactions and SP6 Last Call funeral/flask imagery require protected shared-file changes. The existing horn-called coda already depicts the hunt back to Drezen; preserve that earned return.
- Global registry integration and live Ch5 temple access need coordinator verification.
- Unfiltered Python/C# milestones need coordinator rerun: repeated SIGTERM supplied no actionable failing assertion.

## PROPOSE

None beyond required shared repairs above. No extra mechanic, price, reconciliation, attraction/commitment threshold, blackmail, partner stance or return device implemented.

## RISKS

Shared timing, false Iomedae dependency, portrait and shared coda remain material residuals. Explicit slots retain defaults pending coordinator batch fill. Late paragraph ID remains in exported JSON for slot tooling; display uses the existing supported ending-paragraph contract. No game/harness run or independent score certification.


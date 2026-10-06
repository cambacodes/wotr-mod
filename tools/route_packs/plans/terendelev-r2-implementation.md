# Terendelev round 2 implementation

This file records authored Trickster additions. The copied set-piece and turning-point sheets remain planning evidence; the atlas reservation controls their conflicting device classifications. The implementation uses `isolation_via_canon_events`, the Drezen north turret healing watch after Iz, and the pike/night/shirt-dressing payoff. No verified romantic partner is introduced.

## CHANGES

- `storylines/terendelev_trickster.py`: SP1 plants the blood's observable stopping boundary; SP2 repeats it at both pyre hosts without promising a calibrated resurrection dose (P16–17). Both hosts and the late return now show the bones being burned and their ash scattered. Galfrey's tribute no longer invents pre-accession service (F5). The late journey requires completed Iz and starts in Drezen, retains its 24-hour delay, and avoids a fixed second-night claim (P14–15, F40–41).
- `storylines/terendelev_watch.py`: SP3 adds the ribbon-length recognition question (TER-02). SP4 stages the actual shared treatment watch, gives the helper the basin and linen, and lets Terendelev choose company after the task is done (TER-03). Her initiative no longer turns the wound's pain or blood into desire. COMMITTED, DRESSING and NIGHT retain their producers. An appended company response ends without consuming the night. The third-bell comfort is her deliberate nonsexual action.
- Both route modules: both Seelah reactions and the Anevia reaction use their existing earned-return receipts to override persistent death/departure flags (F28–30). No recovery mechanism is added. SP5 preserves the sixth-bell sentry, shirt dressing, morning closeness and independent duties. Seelah remembers feeding a hungry festival child, rather than resuming theft after conversion (F12–13); Irabeth arranges a relief and demands her borrowed knife back, rather than treating ordinary human contact as new to the dragon. The retired Regill sibling uses the marked sentry reports instead of the stock observer gesture; its retirement gates remain unchanged. Returned Galfrey is privately recognised as Kitrane and uses green wax (F47–48).
- Both route modules: SP6 separates notification from escort without removing the legacy personal-beat receipt used by the existing eligibility contracts (F43). An appended exchange in the existing war-table conversation, on both contact hosts, lets her choose the wounded's watch and release the escort promise (P21, F44). Ending callbacks distinguish notification, a settled escort and a skipped farewell. Debtor service no longer asserts unplayed physical participation at Threshold (F58). Late acceptance is her debt-free decision, with its predicate and inert exit unchanged (P20). Full commitment shows her return from Kenabres; guardian life returns to the Kenabres gate.
- `tools/route_packs/explicit_slots/terendelev/`: two host-specific JSON briefs and corresponding appended `<scene>.explicit.1` nodes. Old `cut` IDs lead through the heated-cut defaults to old `grey` nodes. No explicit prose is supplied. The briefs retain voice traits, canon facts, tagged example, exact last line and line bounds, and identify Commander variants.
- `tools/route_packs/plans/`: copied both required planning sheets. `tools/route_packs/turning_points.json` copies only Terendelev's fixed atlas reservation; no other route is registered or altered.
- `tests/TerendelevTricksterTests.cs`: updates the existing late-return fixtures to completed Iz in Drezen, adds unfinished-Iz/wrong-area negatives, checks the explicit-slot transition, asserts entry availability before every PagesOf traversal, and adds death/closure/divine-refusal availability cases on the late return and both Queen-conversation hubs (P22). Existing ending checks remain intact.
- `tests/test_terendelev_round2.py`: checks both slot traversals, non-escalating company, notification/escort distinction, known-Hal delivery without arrival, late journey timing/location, and earned ending callbacks.

## CLASS SWEEP

Checked both stall/awning hosts and both native restitution hosts. Checked watch/late/debt/guardian callbacks together, including their different letter destinations and escort histories. Preserved the base's southward Kenabres geography, century of crusade service, Drezen blood-test recollections, neutral missing-scale history, swarm-cave claw acquisition, debt-bound market refusal, first free release oath, guardian locations, returned-Irabeth callback, final-rest cairn authority and Storyteller usher variants (F1–4, 6–11, 14–15, 31–37, 49–57, 60–61). Existing sold-square variants remain untouched, and no new foresight echo is added. The engine-round-3 report lists no Terendelev residuals; its payoff and presence contracts remain intact.

## ESCALATE

- Shared cross-route inference still adds foreign romance availability/closure guards to historical deaths, institutional faith and learned Areelu information. This affects the late return, Queen conversations, pyre task choices, proof, identity, faith, royal-letter handovers and ending paragraphs (P1–13, F16–27). Source-local removal cannot repair guards appended after the route generators. Fix the shared classification/exception contracts, then test actual scene availability before every intended branch traversal (P22).
- The managed Terendelev suite fails `Earned Commander return does not select the living guardian ending`. A read-only export using both untouched HEAD route modules confirms that the guardian entry and its `terendelev.present_now` / epoch-unavailable predicates are unchanged from the base. Shared guardian/current-presence classification needs repair; the test was not weakened.
- Shared Last Call must consume the new escort settlement/duty account, accept the existing late entitlement, and distinguish rescue/debtor/sworn-watch/departed accounts (P21, F38, F45–46). The shared ledger must record restoration first and add only receipt-backed watch or debt claims (F39). Shared files were not edited.
- Rescue-only mourning (F59) needs shared departure/payoff classification. The standalone page was removed when the strict departure gate rejected its unclassified presence surface; the existing sacrifice ending and exit were preserved.
- TER-01 belongs to the single memorial hearing shared with Yaniel: her questions about actual recipients and her publicity decision must be implemented by its owner. No duplicate fraud quest or forged record was added here.
- Native mourning/slide corrections beyond the route's existing return implementation remain coordinator-owned and must be Trickster-only, with actual restoration required.

## PROPOSE

None. No unrequested attraction, commitment, payment, medical cure, return or reconciliation requirements were added.

## RISKS

The unresolved shared guards and Last Call claims prevent certification against the 91-point bar. The appended Deskari exchange can be skipped; the ending explicitly records that the promise was not settled. The two explicit slots are mutually exclusive host copies of one night. Generated optional prose still requires user/coordinator insertion and continuity review. No independent scoring audit was run.

## GATE

The final export is generated outside the repository. The later explicit instruction to run full discovery and RulesTests, and not commit, controls the earlier conflicting gate list. Initial gate findings were corrected by placing the escort exchange in an existing classified scene, removing the unclassifiable standalone rescue-mourning page, storing the Hal cue as a GUID array, and updating the route test fixtures for the required Iz/slot behavior. The verifier’s Windows default was replaced with `--game /wrath`. Exports, verifier reports and managed outputs use system temporary storage; the repository's development export is not edited. No commit is made.


Generation and the final route tests used `PYTHONHASHSEED=0`; gates disabled bytecode writes with `PYTHONDONTWRITEBYTECODE=1`. `$TMP` below denotes the system temporary task directory, not a repository path. Generation used the four existing canon-review parent-binding files via `RRT_PARENT_BINDINGS`; managed commands used `RRT_TEST_BUILD_ROOT=$TMP/rules-build`.

| Command/check | Result |
| --- | --- |
| `RRT_STORY_OUTPUT=$TMP/Story-final.json python expansion.py` | PASS; 3,755 scenes; repository development export untouched. |
| `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io` | PASS; 12 tests. Final regenerated JSON separately passes `tools.savecompat.check`: zero hard failures. |
| `python -m unittest tests.test_utf8_io tests.test_terendelev_round2 tests.test_terendelev_polish -q` | PASS; 12 tests after the reactor override fix. |
| `python tools/payoff_lint.py --strict --story $TMP/Story-final.json` | PASS; 42 routes, zero hard failures. Existing REVIEW items remain. |
| `python tools/departure_lint.py --strict --story $TMP/Story-final.json` | PASS; 43 women, zero hard failures. |
| `python tools/rrt_verify.py --strict --gate-only --game /wrath --story $TMP/Story-final.json` (reports directed to `$TMP`) | PASS; zero hard failures, 119.0 seconds. `--gate-only` retains every strict hard check and skips report-only simulations. Earlier full strict findings were corrected before this final gate. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | INCOMPLETE: attempts terminated with exit 143/1 and no unittest completion summary. Diagnostic discovery confirmed the first nine Delamere tests passed before termination; no global pass claimed. |
| `dotnet build tests/RulesTests.csproj -c Release` | PASS; zero errors, eight existing warnings; output under `$TMP`. |
| `dotnet run --no-build --project tests/RulesTests.csproj -c Release -- $TMP/Story-final.json` | INCOMPLETE: full attempts terminated with exit 143/1 without a completion summary. No full rules/progression pass claimed. |
| Targeted managed `TerendelevNativeDependencyTests` | PASS; 524 assertions, one suite. |
| Targeted managed `TerendelevTricksterTests` | FAIL: strengthened availability check exposes `Historical Queen/divine romance state blocks Terendelev's late return: galfrey.dead`. An earlier run also exposed the shared living-guardian return failure above. |
| CRLF-aware `git diff --check` and byte inspection | PASS; all three edited existing Python/C# files retain exclusively CRLF. |

The development JSON must be regenerated by the coordinator before a deployment or independent audit. No commit, full-build harness or game run was performed. Temporary exports, build outputs and audit logs are removed at task completion; the results above are retained here.

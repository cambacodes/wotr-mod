# Eliandra round 3

## CHANGES

Finding numbers below follow `eliandrar2.json`'s ordered `defects` array.

| Finding | Disposition | Evidence/change |
| --- | --- | --- |
| BEL offering cap; 1–3 | fixed | `eliandra_trickster.py`: record the northern memory selected during planning; derive attachment from that memory, the chiefs' lights, or actual observation. Both offering checks require attachment. Append an insufficient-offering answer to both initial and retry menus, leading to the existing counteroffer, its additional price, and her decision. Drezen twins copy the corrected graph. |
| 4–6 | fixed | `eliandra_trickster.py`: the veil narration describes the present sensation without asserting previous experience. Both twins inherit it. |
| 7 | verified-fixed | `endings_job3.eliandra` already records both friendship replies, derives current friendship until subsequent commitment, and excludes the unasked invitation. No duplicate route repair retained. |
| 8 | verified-fixed | Shared job 3 replaced the automatic lover ending with explicit postwar lover/friend/refusal choices and local outcome codas. The original automatic-romance premise no longer applies. A campaign partner coda still requires campaign acceptance; readiness alone grants none. |
| COX presence cap; 9 | fixed / escalated | `eliandra_trickster.integrate`: harem eligibility excludes authored away, hiding the Guest List and physical eligibility consumers until actual return. The shared departure installer overwrites the `present_now` exclusion; coordinator registration is still required for other readers of physical presence. |
| 10–11 | verified-fixed | Shared Last Call opening no longer locates her in Drezen; location paragraphs distinguish returned from unrecovered fords histories. Called text no longer claims she is on Drezen's north wall. |
| 12 | escalated | `lastcall_partners.py` still claims daily questions from commitment alone. This file is explicitly prohibited. Reserve that continuation for completed daily courtship; short commitment histories need a first-mile/written-question continuation. |
| 13 | fixed | `eliandra_stars.py`: existing return scene becomes a delayed physical caravan interaction at the established capital tailor frontage. Separate arrival presence requires the written yes and absence, waits 48 hours, and disappears after the existing return receipt. Existing node IDs, answer indices and effects survive; correspondence becomes spoken arrival dialogue. Only the road letter remains a Chapter 5 remote delivery. |
| 14–15 | escalated | Shared job 3 partitions `EPILOGUE_PARAGRAPHS` onto the invitation page and the immediate confession/night onto `late_accepted`. Therefore lifetime consequences still precede the invitation and confession. Reordering the route source would break that shared positional partition. Coordinator must move lifetime paragraphs after the immediate accepted sequence and give refusal/friend histories appropriate consequences. |
| 16–17 | fixed | `eliandra_stars.py`: terminal promise answers her request for another morning; effects/index preserved, fallback inherits the correction. |
| 18–19 | fixed | `eliandra_stars.py`: answer to remembering the horses becomes “I'll remember.” The other “I won't” correctly answers “Do not make me regret it” and stays. |
| 20 | fixed / escalated | Python replay tests execute earlier-flirt → friendship and written-yes → absence → physical return, and inspect generated Guest List/fords paragraphs. Existing C# allocation and placement assertions now enforce one remote delivery and recognize the mutually exclusive arrival host. The remaining shared `present_now` defect is explicitly escalated rather than represented as fixed. |

Existing explicit slot IDs and five briefs remain. The three epilogue briefs now specify `narration: third-past`. No explicit prose added.

## CLASS SWEEP

- Both offering menus (initial/retry), shrine and both Drezen hosts, learned/guessed terms, remembered/never-looked planning, observation, King-gone fallback, success/counteroffer, and the treatment's matching sacrifice praise.
- Both morning-question hosts and both Katair branches; distinguish the erroneous agreement from the correct reassurance.
- Generated shared friendship/invitation transformations, campaign versus postwar acceptance, Guest List versus correspondence, normal versus arrival presences, and retained-letter/written-yes finale locations.
- Original node/choice identities and effects retained, including an explicit regression for every return-scene answer identity. CRLF preserved in existing CRLF files; Python test files retain LF.
- Other veil callbacks already select witnessed versus unwitnessed versions (`dark_sky/cost` and `cost_plain`); no unnecessary prose changes there. Native priestly biography, shrine veil and departure facts checked against `/wrath/blueprints.zip` and `enGB.json` (cues 24d719b4, cb48db97, 28e3b35d).

## GATE

All commands use `PYTHONHASHSEED=0`. The export also uses the four parent-binding files specified by `build-expansion.ps1`. Game evidence comes from `/wrath`.

| Command | Result |
| --- | --- |
| `RRT_STORY_OUTPUT=<system-temp-story> python expansion.py` | PASS: final export, 3,848 scenes. |
| `python -m unittest tests.test_EliandraPolish tests.test_eliandra_round2 tests.test_utf8_io -q` | PASS: 23 tests against the final generated story via `RRT_TEST_STORY`. |
| `python tools/savecompat.py --story <system-temp-story>` | PASS: 0 hard failures. |
| `python tools/payoff_lint.py --strict --story <system-temp-story>` | PASS: 42 routes, 0 hard failures; existing editorial REVIEW items remain. |
| `python tools/departure_lint.py --strict --story <system-temp-story>` | PASS: 43 women, 0 hard failures; existing editorial REVIEW items remain. |
| `python tools/rrt_verify.py --strict --gate-only --story <system-temp-story> --game /wrath --json <system-temp-report> --text <system-temp-report>` | PASS: 0 hard failures; all strict checks, report-only analyses deferred. Runtime 355.7s. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- <system-temp-story>` | INCOMPLETE: unfiltered runs terminated with exit 143, including an isolated retry. The corrected final story passed structural validation and the progression checks reached before termination. No selectable-answer failure reported on the final story. |
| Same C# command with `--suites=EliandraTricksterTests` | PASS: 3,446 assertions. Final retry used `--no-build` after compiling the changed tests. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | INCOMPLETE: two attempts, including an isolated retry, terminated with exit 143 without a test summary. |
| `git -c core.whitespace=cr-at-eol diff --check` | PASS. |

An initial C# gate caught a retained remote `Kind` on the physical return. It was removed, the story regenerated, and final structural/route validation passed. The native-list return setting was also removed before final generation to preserve answer identities and ordinary presence-hub construction.

The generated story was supplied from system temp instead of writing `development/Story.json`, respecting the explicit filesystem restriction. .NET artifacts use `RRT_TEST_BUILD_ROOT` in system temp. Temporary scripts, exports, logs, reports and build artifacts were deleted before finishing. No game, harness, full build script, commit or independent audit run.

## ESCALATE

- Shared departure contracts/installer: register authored away for `eliandra.present_now` while preserving the road letter and physical return. The route-local eligibility exclusion handles Guest List membership but cannot survive the shared presence overwrite.
- Shared Last Call daily-memory continuation (finding 12).
- Shared job 3 ending paragraph partition/order (findings 14–15).
- The requested `tools/route_packs/voice_locks.json` is absent in this checkout. Available sibling registries are empty. No supplied lock entry was bypassed.
- Environment/gate completion: full Python discovery and unfiltered C# rules runs repeatedly ended with exit 143. No test assertion identifies a route repair for those terminations; coordinator must complete those runs in a functioning gate environment.

## PROPOSE

None. No additional gates, prices, commitment conditions, return devices or redesigns beyond the audit implemented.

## RISKS

No game/harness run or independent scoring audit. The 91-per-dimension target remains unverified, and the escalated defects prevent claiming completion. Arrival uses existing validated capital placement; actual in-game visibility/clickability remains coordinator validation. Changes intentionally remain uncommitted.

# ENGINE-Q5 follow-up report

Branch: `claude/engine-q5`.
The coordinator's Aranka ruling is implemented.
Previous-round source work is preserved.
No commit was made.

## CHANGES

- `storylines/earned_presence.py` (prior ESCALATE 1): adds the explicit `PRESENCE_RETURN_IN_PROGRESS` registry.
  Its sole entry lifts `aranka.ran_failure` for physical presence when `aranka.trickster.answered` holds, with a reason.
  The existing paid second verse sets both `answered` and legacy `returned`; `answered` records the reply that brings her to Drezen.
  The central guard uses existing Derived/DerivedForbids machinery to retain every other unavailable flag and ClosedFlag.
  Relationship and household eligibility still use the unchanged `aranka.trickster.moral_repaired` override.
- `tools/earned_presence_lint.py` (P1/T7): checks the exact central guard definitions, accepting only registry entries with a nonblank reason and a Trickster-earned flag.
  Exception flag producers are included in T7's current-path checks.
  Undocumented lifts, missing loss/closure guards, wrong route guards, and invalid registry entries fail.
- `tests/test_engine_q5.py` (ruling acceptance): adds three focused tests covering idempotence, exact exception scope, weakened guards, required reasons and registered losses, and current-path producers.
- `tests/ArankaTricksterTests.cs` (ruling acceptance): preserves the original line-507 assertion byte-for-byte.
  Played King-failure and no-King histories exercise market and yard: paid answer, wanted presence, reachable reckoning, paid moral repair, then existing courtship.
  Unpaid and unanswered failures stay hidden.
  Checks retain closure/death/departure blocking, household exclusion before repair, deferral, and refusal.
  Snapshot helpers discard computed Derived flags before recomputing, matching Main's fresh snapshots on each world tick.
- `tests/EngineQ5Tests.cs` (class coverage): recognizes Aranka's compiled central guard while retaining the existing route guard and closure/return checks for every other presence.
- `tests/ENGINE-Q5-REPORT.md`: replaces the obsolete blocked-round report with this follow-up.

## CLASS SWEEP

- Checked both Aranka venues, both failure entry devices, every unavailable flag, and ClosedFlag.
- All 47 physical presences across 29 relationships remain centrally guarded.
  The 45 non-Aranka guards retain their existing RouteOpen mappings.
- The original worktree export differs only in `Derived`, `DerivedOpenRoutes`, and `DerivedForbids`.
  Scenes, nodes, relationship IDs/metadata, choice order/contents, presence placement/requirements, prices, and household gates are unchanged.
- Existing LF/CRLF styles were preserved.
  No route prose, foresight/echo content, native bindings, shared household/Last Call/world code, or runtime source was changed.

## GATE

Export-dependent checks used `PYTHONHASHSEED=0` and the four parent-binding files configured by `build-expansion.ps1` through `RRT_PARENT_BINDINGS`.
The SDK executable was `%LOCALAPPDATA%/RanRomanceTools/dotnet/dotnet.exe`.
Managed checks used the installed Python through `RRT_PYTHON`.

| Command | Result |
| --- | --- |
| `python expansion.py` | PASS: 2855 scenes, 47 relationships, 47 presences. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | PASS: 170 tests. |
| `python tools/rrt_verify.py --strict --quiet --json <TEMP>/rrt-engine-q5-followup-verify.json --text <TEMP>/rrt-engine-q5-followup-verify.txt` | PASS: 0 hard failures; 244.7 seconds. |
| `python tools/earned_presence_lint.py --story development/Story.json` | PASS: 0 hard, 0 review. |
| `python tools/gate_lint.py --story development/Story.json` | PASS: 0 hard. |
| `python tools/pacing_lint.py --story development/Story.json --availability tools/pacing-availability.json` | PASS: 0 hard; 4 existing warnings, 16 review items. |
| `python tools/harem_schedule_lint.py --story development/Story.json` | PASS: 48 candidates, 57 beats, 3 packets, 0 hard. |
| `python tools/harem_smoothing_lint.py --story development/Story.json --strict-forms` | PASS: 41 women, 33 repairs, 0 errors. |
| `dotnet build src/Tirabade.csproj -c Release --nologo -v quiet` | PASS: 0 errors. |
| `dotnet build managed-tests/ManagedBuildTests.csproj -c Release --nologo -v quiet` | PASS: 0 errors. |
| `RRT_TEST_EXPANDED_EPILOGUE=0/1/wrong-type`, each running `managed-tests/bin/Release/net48/ManagedBuildTests.exe <GameDir> development/Story.json` | PASS: all three modes; wrong-type epilogue ignored with the expected warning and addon initialized. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json` | PASS: 130,485,974 assertions, including the original Aranka presence assertion; no "Page has no selectable answers" failures. |
| Save-shape comparison, original assertion preservation, line-ending checks, `git diff --check` | PASS. |

Verified generated-story SHA256: `1dd325d8a69ce1688b31705fbfaf7bd54a09df465a7ed898f7b24fb24bbe62fd`.
Verification reports were written outside tests.
The pre-existing generated export was restored byte-for-byte after the complete gate, preserving its original uncommitted contents; regenerate before coordinator review.

## ESCALATE

No shared-code change is needed for Aranka.
Cleanup remains blocked by automatic approval review.
Both path-checked recursive cleanup and deletion of one explicitly named diagnostic file were rejected as "blocked by policy".
Pre-existing diagnostic artifacts remain under `tests/.engine-q5-probe`, `tests/.tmp/Story-followup.json`, `tests/DelamereGateTemp/.dotnet`, and the `tests/engine-q5-*.txt` / `tests/engine-q5-*.json` evidence files.
The workspace owner or coordinator must remove them outside this restricted session.
This round created no temporary files under tests.

## PROPOSE

None.
No additional mechanics, costs, attraction/commitment requirements, reconciliation conditions, or redesigns were implemented.

## RISKS

- Independent coordinator/auditor scores are not claimed by these gates.
- Existing nullable/unused-field warnings and NU1900 advisory-fetch warnings remain under restricted network access.
- The export retains its existing incomplete-development label.
- Rules and managed fixture checks do not cover Unity execution or a campaign/save round trip.
  No game, harness, or `build-expansion.ps1` run was performed.

Use `tools/fast_gate.sh` after each coding round. It generates the expansion with
`PYTHONHASHSEED=0` and the four existing parent-binding manifests, runs every
strict verifier check and the existing lint policies, selects Python regressions,
then runs the relevant named RulesTests suites. Logs, native coverage receipts
and .NET intermediates live in a disposable system temporary directory.

```bash
tools/fast_gate.sh                         # staged, unstaged and untracked files
tools/fast_gate.sh --base claude/eng-final  # also include committed changes
tools/fast_gate.sh --files storylines/wenduag_echo.py
tools/fast_gate.sh --plan                  # inspect selection without executing
```

The selector always includes small engine fixtures, save-related validation,
native contradiction inventories, earned/closed/off-path negatives and live bug
regressions. A route-only edit also includes suites that consume that route;
coupled Tirabade and Minagho/Chivarro routes expand together. Shared or unknown
changes use the engine/inventory subset; mixed changes also keep every detected
route consumer. FAST defers exhaustive campaign
interleavings and the ideal run to FULL; it does not certify a release.

`rrt_verify.py --strict --gate-only` retains the exact strict checks. It omits
only the advisory world/roster/budget/conflict reports (B–D3), which do not
contribute to the strict failure count. Default verifier behavior is unchanged.
FAST still runs the crossroute L1–L6 lint and its negative controls.

Run `tools/full_gate.sh --game /wrath` for Linux preflights. It runs the default
verifier, every Python test (including ideal-run reachability), the default,
unfiltered RulesTests runner, binding validation, actual managed construction in
all three optional-epilogue modes, real UMM load smoke and selective degradation
fixtures under Mono. It does not start a game or harness. Windows packaging with
`build-expansion.ps1` retains the FULL gate and now discovers the entire Python
suite, including the ideal run, instead of repeatedly invoking selected modules.

Focused C# diagnostics also work directly:

```bash
RRT_TEST_BUILD_ROOT=$(mktemp -d)  # remove this directory after the command
export RRT_TEST_BUILD_ROOT
dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json --suites ContactDisambiguationTests,PresenceRuntimeF9Tests
dotnet run --project tests/RulesTests.csproj -c Release -- --routes wenduag development/Story.json
dotnet run --project tests/RulesTests.csproj -c Release -- --suites=CountTests,ContactDisambiguationTests --jobs=2 development/Story.json
rm -rf -- "$RRT_TEST_BUILD_ROOT"
unset RRT_TEST_BUILD_ROOT
```

Unknown/empty selectors fail. Legacy focus flags and `--bindings` remain
available; bindings stdout remains JSON only. Parallel filtered suites run in
separate processes with private story state and merge receipts in stable order.
The default FULL runner remains sequential because its inline campaign checks
share state and ordering with named suites.

Set `RRT_TEST_PROFILE=1` for suite timing lines on stderr, or set
`RRT_TEST_TIMINGS=/tmp/rules-times.json` for measurements. Set
`RRT_MANAGED_TIMINGS=/tmp/managed-times.json` for managed measurements. The audit
profiler supports `python tools/test_audit.py python --json /tmp/python-times.json`
and `python tools/test_audit.py lints --json /tmp/lint-times.json`. Method timings
exclude unittest class setup/teardown; total wall time includes it. Audit findings,
mutation evidence, removals and measured tier timings are in
[test_audit_report.md](test_audit_report.md).

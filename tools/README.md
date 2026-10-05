Use `tools/fast_gate.sh` after each coding round. It generates the expansion with
`PYTHONHASHSEED=0` and the four existing parent-binding manifests, runs every
strict verifier check and the existing lint policies, selects Python regressions,
then runs the relevant named RulesTests suites. Logs, native coverage receipts
and .NET intermediates live in a disposable system temporary directory.
Add `--json /tmp/gate-times.json` to retain stage timings and assertion receipts
outside the repository. Remove that evidence file after reviewing it.

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
route consumer. Changed tests select themselves; lint and metadata changes also
select their matching Python regression, including filenames that omit `_lint`.
FAST defers exhaustive campaign
interleavings and the ideal run to FULL; it does not certify a release.

`rrt_verify.py --strict --gate-only` retains the exact strict checks. It omits
only the advisory world/roster/budget/conflict reports (B–D3), which do not
contribute to the strict failure count. Default verifier behavior is unchanged.
FAST still runs the crossroute L1–L6 lint and its negative controls.
The late-consumer serialization witness in `test_foresight_echo` stays in FULL
when its factory and test body are unchanged. Editing `expansion.py`, `story.py`,
`storylines/foresight.py`, or that test body selects it for FAST as well. All other
foresight API, negative, consumer and native canon controls remain in FAST.

Generation and the isolated dormant-draft inventory run independently. The gate
shares that inventory between the verifier and Python controls only for the same
source root, with a private JSON copy for each caller. Selected Python modules
run in two isolated workers balanced from measured costs. FAST builds RulesTests
while preparing fixtures, then runs its selected suites after the scans; running
all those workers together increased wall time on this remote. FULL overlaps its
long rules walks with Python discovery and verification.

Run `tools/full_gate.sh --game /wrath` for Linux preflights. It runs the default
verifier, every Python test (including ideal-run reachability), the default,
unfiltered RulesTests runner, binding validation, actual managed construction in
all three optional-epilogue modes, real UMM load smoke and selective degradation
fixtures under Mono. It does not start a game or harness. Windows packaging with
`build-expansion.ps1` retains the FULL gate and now discovers the entire Python
suite, including the ideal run, instead of repeatedly invoking selected modules.
It passes its resolved `-GameDir` to native Python fixtures through `RRT_GAME_DIR`
and restores the previous environment value on exit.

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
The default direct FULL runner remains sequential. The Linux FULL gate sets
`RRT_RULES_JOBS=2`: ten independent route suites run in isolated worker processes
and the parent runs the remaining named and inline checks in their original
order. Each worker shares one parsed export across its suites. Set
`RRT_RULES_JOBS=1` to compare sequential results. Assertion receipts and native
coverage merge in stable order; bindings and legacy focus modes stay sequential.
Windows packaging retains the unfiltered runner and every construction fixture.

The ten audited read-only route suites also reuse completed equal snapshots
within each invocation. This cache is bounded to 2048 entries, retains all
snapshot fields, and replays results from production `Rules.Complete`. It resets
at the suite boundary. Other suites continue calling production completion
directly; mutation fixtures cannot reuse another suite's completed world.

Set `RRT_TEST_PROFILE=1` for suite timing lines on stderr, or set
`RRT_TEST_TIMINGS=/tmp/rules-times.json` for measurements. Set
`RRT_MANAGED_TIMINGS=/tmp/managed-times.json` for managed measurements; the Linux
runner writes one suffixed file per fixture (`-0`, `-1`, `-wrong-type`, `-load`,
`-irabeth_dead`, `-trickster`) so later fixtures cannot overwrite earlier results.
The audit
profiler supports `python tools/test_audit.py python --json /tmp/python-times.json`
and `python tools/test_audit.py lints --json /tmp/lint-times.json`. Method timings
exclude unittest class setup/teardown; setup is recorded separately and total
wall time includes it. Audit findings,
mutation evidence, removals and measured tier timings are in
[test_audit_report.md](test_audit_report.md).
For a selected Python profile, add `--tests tests.test_test_selection` (and
optionally `--jobs 2` for multiple independent modules). Default full discovery
remains sequential. Rules timing also records the original campaign/structure
checks and runner overhead separately from named suites. Bindings uses separate
timing and native-coverage paths, preserving the completed campaign receipts.

Reproduce the mutations with:

```bash
python tools/test_mutations.py --json /tmp/rrt-mutations.json
```

This creates a locked scratch branch/worktree in system temp, copies pending
test/tool changes, exercises the recorded detectors selected by FAST, and removes
the worktree, branch and build products on exit. The requested external evidence
file is the only retained artifact; remove it after reviewing it. Mutations are
never applied to the working mod or its export.

Observed on this remote: final FAST 329.20s (200 Python tests; zero skips),
above the five-minute target; first FAST 346.66s. FULL 6113.14s; its unfiltered
RulesTests stage 5846.75s versus measured base 7792.51s (144,847,634 versus
167,366,569 assertions; only itemized duplicate checks retired). FULL ran 531
Python tests with zero skips; the subsequently added real C# timing-isolation
regression passed separately and in final FAST. See the audit for mutation
evidence, timing-file loss and the reproduced pre-existing legacy bridge mismatch.

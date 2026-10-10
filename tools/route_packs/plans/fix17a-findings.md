# fix17a structure findings

Base: `0d530372d758fb781d70f5b5535610522a300d38`. Bundle manifest digest: `a7087ac93a7b26bbb7e45e2bb333c471985b5ca8fa5c94fa937c67d79d78e587`.

Pinned policies, contracts, sheets and scenario inventory were read through manifest `bundle_path` entries and their hashes checked. Requested `git log -p keep/cand-13-final..HEAD -- <files>` ranges were inspected; older history and blame establish causes when that range has no causal patch. These are source-history findings, not inherited gate attribution: no baseline receipts were supplied.

| Item | Cause and intended state | Fix and sibling inspection |
| --- | --- | --- |
| 1: six textless nodes | `876eeb8c` introduced Eritrice/Areelu history partitions; `a6350549` narrowed Chadali decline accounting to forfeiture histories. Paragraphs with contrary histories cannot be ungated without making false accounts. | Append registered, unconditional pending paragraphs to Eritrice exchange; Areelu graft/after, crossroads/end, dagger/end, visitors/end; Chadali declined/page. Keep all existing prose, guards and paragraph indices. Pending instructions require common closure/intro without claiming a branch-specific event. Route prose owners: Eritrice, Areelu and Chadali. |
| 2: S17/S48 setup | `94162b97` enforces nominated Delamere D05/Gesmerha D09 delivery. Partial fixtures omit complete registration. `25dd7a84` supplied the shared complete-dependency row fixture for five siblings. | S17 reads complete exported relationship contracts. S48 uses `row_registration_fixture`, rebuilding only its own row before final decorators. Production inventory is still strict; deletion mutations for both foundations fail. S24/S25/S30/S35/S42 and other legacy partial-fixture callers inspected. |
| 3: S44 rejection | `cc134933` approved 18 optional completions, superseding 16; pinned ceiling-ruling and schedule agree. | Test 19 proposed completions against the current 18 cap and assert failed registration leaves registries unchanged. Existing approval, clock, bodily presence, outcomes and idempotence tests retained. |
| 4: Nocticula physical availability | `5f013ebf` cross-route classifier treats some messages, reported fates and mental responses as bodily participation. `66aee131` terms explicitly use correspondence and earned mental presence. Requested cand-13 range has no causal classifier change. | Add exact reviewed reference classifications through the existing J01 mechanism; no gates are indiscriminately stripped. Inspect second_door, acquisition answer, defeated chair and threshold terms, including alive/body/mind/captive/dead/cast/declined histories and discovery. A new physical appearance with different text still classifies as live. |
| 5: paid refusal/inn accounting | `750a3e49` replaced the collection account with a paid-only paragraph; `66aee131` test still selects an old sentence. | Assert paid-only paragraph visibility for PAID versus REFUSED plus unchanged effect-free exit and GuidFor. Preserve all player text. The module's unrelated acquisition-arrival sentence assertion remains fix17b's responsibility. |
| 6: C# build | `f2b96c6c` introduced `menu.Length` on `List<Choice>`. | Use `.Count`. Rules project compiles; eight existing unused-field warnings remain. The other `trustChoices.Length` occurrence operates on `.ToArray()` and is correct. Runtime receipt test was killed with SIGKILL; no passing result is claimed. |

## Finding checks

Disposable scripts, generated exports, builds and logs are in system temp. UTF-8 and LF byte style are preserved. Existing authoring string literals remain; exported existing scene/node order, prose and choice targets compare unchanged. Save-ID inventory comparison reports no lost or shrunk entries. These are finding checks, not sealed runner receipts.

Initial targeted checks reproduced the six validator errors, stale S44 expectation, Nocticula guard error and obsolete collection lookup. The initial multi-module run was cancelled while its C# subprocess was stalled; it is not a pass. A trial partial-builder repair failed on an omitted Wenduag row; that edit was reverted.

Build finding: `RRT_TEST_BUILD_ROOT=/tmp/fix17a-rules-build dotnet build tests/RulesTests.csproj -c Release --nologo -v quiet -p:UseSharedCompilation=false`, exit 0. The pre-fix no-restore compile failed CS1061. Receipt runtime subprocess exited -9 (SIGKILL); the pinned gate contains no rules-suite selection. The read-only test-gate preview was also killed. No guard or gate policy was changed.

## Remaining dependencies

- fix17b owns the unchanged acquisition-arrival prose assertion in `tests.test_nocticula_round2.test_acquisition_visit_is_optional_read_only_and_channel_limited`. It fails on the approved new arrival text. The required changed-tests command includes this module; that failure is not exempt from the gate.
- Runner/coordinator owns permission/selection for the two C# receipt suites and final gate sealing. A successful build does not certify the runtime test.
- Route prose owners must resolve the six pending paragraphs before a milestone. Structural pending registration is authorized for this job; no player prose was written.

## Proposal

Migrate remaining legacy `include_harem=False` registrar tests onto complete dependencies with their owned row removed/re-registered, as fix16a established. Do not weaken production delivery or cloud transformations to support incomplete fixtures.

## Final delivered-export evidence

Final generation: `RRT_STORY_OUTPUT=/tmp/fix17a-final-Story.json python expansion.py`, exit 0, 4,095 scenes. Export is marked INCOMPLETE DEVELOPMENT because pending prose remains.

- Structural validation via `rrt_verify.validate(Model(export))`: zero errors; pending registration check: zero errors; all four terms hosts have no crossroute.shamira physical gate.
- `RRT_TEST_STORY=/tmp/fix17a-final-Story.json python -m unittest tests.test_harem_row_s03b tests.test_nocticula_partners tests.test_savecompat_baseline tests.test_utf8_io`: exit 0, 41 tests passed.
- Structure/fixture/S44/pending checks: 51 tests passed against the preceding regenerated export; final changed-tests execution repeats all changed structure checks successfully.
- `RRT_TEST_STORY=/tmp/fix17a-final-Story.json python /work/Writer/tools/jobs/changed_tests.py /work/wt/RRT-fix17a 0d530372d758fb781d70f5b5535610522a300d38`: exit 1, 36 tests, one unchanged fix17b arrival-sentence failure. Reported as failed, not inherited or exempt.
- `python tools/payoff_lint.py --story /tmp/fix17a-final-Story.json`: exit 0, zero hard failures; existing REVIEW findings retained.
- `python tools/departure_lint.py --strict --story /tmp/fix17a-final-Story.json`: exit 0, zero hard failures; existing REVIEW findings retained.
- Immutable-base save-ID comparison: no lost or shrunk IDs. Comparison of every original scene/node order, original text surface and old choice target against the final export passes. `git diff --check` passes.

The literal profile ID-guard CLI and exact default-path payoff/departure argv were not run against a modified repository export; temporary-export findings above do not replace runner gates. Final sealed receipts, scope/environment/profile digests, staging, commits and pushes remain runner-owned. Completion is incomplete because changed-tests fails and the C# runtime check lacks completion evidence. No final gate failure is waived.

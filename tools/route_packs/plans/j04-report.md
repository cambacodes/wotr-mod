# J04 implementation report

Branch: `claude/J04`; base: `c3005840`. No commit, following the final user
instruction. Approved implementation rule 3 governs targeted testing; no full
Python discovery or full RulesTests run. Generated exports, logs and build
outputs use a system temporary directory and are removed before handoff.

## CHANGES

| Ruling | Result and evidence |
| --- | --- |
| 03 | Implemented S12's primary and one 48h retry, appended manual bench alternative, full correction/revision/cost terminal, pending accusation and final Nenio→Camellia refusal through the existing J02 policy. Nenio alone reaches respect; Camellia stays rival. Current bodies, route losses and paid-page gates remain required. S11 reads the shared actual craft witness without another preparation. Edge speech remains intentionally prose-pending. |
| 06 | Done as approved withholding: S22 emits nothing. Reserved settle/retry IDs and schedule allocation retained, labelled not activated for beta. N5 murders/complaint do not create battlefield-order losses. Existing Irabeth accountability and execution closure are unchanged. |
| 21 | All five approved deed-only exceptions accounted for. S01 reversed snare, S03b corrected fallen account and S09 corrected routes already meet the action contract; no new mechanic added. S11 now finishes its existing primary/retry only after the actual workbench inspection. S14 derives its frozen asymmetric stage groups from the named deeds, with current routes and matching enmity precedence. No second tool, roll, fee, attraction requirement or reconciliation is introduced. Undeclared failure directions remain inert under J02. |

| File | Change and purpose |
| --- | --- |
| `storylines/harem_rows/s12.py` | Ruling 03: emit the two reserved hosts; append the manual menu choice; record success only after both women's actions; derive asymmetric stages and `household.craft.method_witnessed`. Reuse existing route-specific losses and returns plus J01's actual contact envelope. |
| `storylines/harem_rows/s11.py` | Rulings 03/21: append inspection nodes to all four protected wrappers; move their existing success receipt after inspection. Gate the old company inspection when craft was already witnessed and append company over that same work. Preserve old choices, nodes, prose, ward/slot and all allowances. |
| `storylines/harem_rows/s14.py` | Ruling 21: consume the existing `STAGES` metadata as guarded read-only views. Existing personality/title wrappers and J01 runtime attendance are unchanged. |
| `storylines/harem_rows/s03b.py` | Ruling 21: replace the stale second-tool approval comment with the approved deed-only disposition. |
| `storylines/harem_rows/s22.py` | Ruling 06: explicit beta status and reserved IDs; registration remains inert. |
| `tests/test_harem_row_s12.py` | Replace reservation-only checks with exhaustive action/refusal/abort histories, retry clock, first target, asymmetric stages and current-body/loss negatives. |
| `tests/test_harem_row_j04.py` | Assembled save/voice checks, all five exception classes, real S11 inspection, shared craft provenance, S14 exact deeds and prose-pending addresses. Voice-owner completion may replace the placeholders. |
| `tests/test_harem_row_s01.py` | Correct the positive fixture to supply current native-body/chapter evidence and actual contacts required by J01. Returned-body history removes native-party evidence. No runtime guard is loosened. |
| `tests/test_harem_row_s11.py` | Assert the preserved old company choice prefix while allowing the appended reuse choice. |
| `tests/test_harem_row_s14.py` | Assert the approved derived stages, directional ceilings and matching reconciliation precedence. |
| `tools/harem-schedule.json` | Only S12/S22 notes change; order, IDs, counts and retry allocations are unchanged. |
| `tools/route_packs/harem/S12.md`, `tools/route_packs/harem/sheets/S22.md` | Replace stale blocker/wiring claims with the current approved contracts, native boundaries and acceptance evidence. |
| `tools/route_packs/plans/j04-contracts.json` | Concrete ruling/exception disposition manifest for subsequent jobs. |
| `tools/route_packs/plans/prose-pending.json` | Append 15 entries: seven S12 Camellia nodes; four S11 Camellia inspection nodes, two fallen Arueshalae inspection nodes, one Camellia company node and its appended choice. No voice lock changed. |

## CLASS SWEEP

Checked S01/S03b/S09/S11/S14 primary and retry siblings, both Arueshalae
personalities and all Galfrey/Kitrane title variants. Retained existing
action/refusal distinctions, 48h failure clocks, shared exhaustion, protected
costs, pre-action Later and real body/contact guards. S11's old and reused
inspection histories cannot charge another shared preparation or imply S12
completion. Every S12 success needs the two deeds and existing costs; a lone
correction, paid page or performed warmth supplies neither craft nor affection.

Negative histories cover unpaid/off-path, missing/remote-only body, closed or
departed woman, later loss after return, unreturned Commander, accusation then
success, direct refusal, retry refusal, abort and an earlier reconciled first
target. Chapter end/unattempted retry remains unfinished. No new reconciliation,
body producer, native romance etude write, echo, explicit slot or canon rewrite.
Reopened N3/N5 in `/wrath/blueprints.zip` and installed enGB; N3 remains voice
evidence rather than a SeenCue, and N5 remains murder/complaint history.
Scene/node IDs and saved choice prefixes are retained; newline styles match HEAD.

## GATE

Environment: `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`,
`RRT_GAME_DIR=/wrath`, and the four build-script parent-binding manifests
joined with `:`. `RRT_STORY_OUTPUT` and `RRT_TEST_STORY` select the temporary
export, represented as `$EXPORT` below. Repository development files are untouched.

| Command | Result |
| --- | --- |
| `python expansion.py` | Exit 0; 4,056 scenes. Completed within 229.3s wall time, including the final polling interval. |
| `python tools/savecompat.py --story $EXPORT` | Pass, 0 hard failures. |
| `python tools/payoff_lint.py --strict --story $EXPORT` | Pass, 42 routes; 0 hard failures. Inherited reviews remain. |
| `python tools/departure_lint.py --strict --story $EXPORT` | Pass, 43 women; 0 hard failures. Inherited review remains. |
| `python tools/voice_lock_lint.py --strict --story $EXPORT` | Pass, 576 locks; 0 changed and 0 missing/ambiguous. |
| `python tools/slot_brief_lint.py --strict --story $EXPORT` | Fails: 315 inherited hard findings, 168 warnings. Same 315 exact findings against the unchanged base export; 0 added/removed. J04's S11 slot has 0 findings. |
| Targeted Python command below | 86 tests pass. Initial four S01 positive-fixture failures corrected with real body evidence. |
| `python -m unittest tests/test_harem_row_j04.py tests/test_harem_row_s14.py -q` | 18 pass after the final S14 precedence test and pending-address check update. |
| `python -m unittest tests/test_harem_row_j02.py tests/test_savecompat_baseline.py tests/test_utf8_io.py -q` | 22 pass, including fresh source-generation save identity. |
| `python tools/rrt_verify.py --strict --story $EXPORT` | Run once; exit 1 after 700.6s: 13 inherited player-text hard findings in seven unchanged, locked Jerribeth scenes. 0 structural errors, 0 required inputs without producers, 0 draft contract diagnostics; J04 adds no hard finding. |
| `bash tools/managed_tests_linux.sh /wrath/ $EXPORT` | Exit 0; all real-assembly construction, UMM load and missing-etude degradation fixtures pass. Temporary outputs removed by its trap. |
| Filtered RulesTests, `HouseholdTests,HouseholdEngineTests,HouseholdTransactionTests` | Stops at inherited `HouseholdTests` reserved-stance assertion. Same failure on the unchanged base export. |
| Filtered RulesTests, `HouseholdEngineTests,HouseholdTransactionTests` | Pass, 412 assertions in 2 selected suites. Build outputs outside the repo. |
| `git diff --check`; newline/allowed-path/artifact checks | Pass; no changed newline style, edits outside scope, repository caches or obj/bin directories. |

```sh
python -m unittest tests/test_harem_row_s01.py tests/test_harem_row_s03b.py tests/test_harem_row_s09.py tests/test_harem_row_s11.py tests/test_harem_row_s12.py tests/test_harem_row_s14.py tests/test_harem_row_s22.py tests/test_harem_row_j04.py tests/test_utf8_io.py tests/test_harem_schedule.py -q
RRT_TEST_BUILD_ROOT=$TEMP/rules-build dotnet run --project tests/RulesTests.csproj -c Release -- --suites=HouseholdTests,HouseholdEngineTests,HouseholdTransactionTests $EXPORT
RRT_TEST_BUILD_ROOT=$TEMP/rules-build dotnet run --no-build --project tests/RulesTests.csproj -c Release -- --suites=HouseholdEngineTests,HouseholdTransactionTests $EXPORT
```

## ESCALATE

- Strict verifier: 13 inherited text findings in `jerribeth.farewell`,
  `jerribeth.ending_together`, `jerribeth.ending_ascended`,
  `jerribeth.offered_signature`, `jerribeth.counterfeit_guest`,
  `jerribeth.counterfeit_audience` and `jerribeth.counterfeit_spoil`.
  Their nodes/choices are identical to the base export, and all seven scenes
  are voice-locked. The verifier's exact text-lint/baseline check reports the
  same 13 findings on the base export. The findings are Commander-gender detection, one embedded
  Commander-speech detection and one speaker-attribution finding. Route/voice
  owners must review them; no unrelated prose or baseline exception changed.
- Global slot-brief repair is outside J04: 315 unchanged hard findings across
  Areelu, Arueshalae, Camellia, Chivarro, Hepzamirah, Jerribeth, Melazmera,
  Minagho and Nocticula briefs, plus five other harem-slot findings. Classes
  include facts schema, changed boundary, epilogue narration, and withheld
  hosts/missing example. No lint weakening or other-route repair attempted.
- `tests/HouseholdTests.cs:178` forbids all stance Set effects, conflicting
  with J02's approved publication. It fails identically on the base export.
  This file is expressly prohibited; coordinator must reconcile the shared test.
- J08 retains ownership of Seating Notes/Last Call consumers; J09 must exclude
  S22's nonexistent incident from actual completions. The new receipts and
  disposition manifest are ready for those approved dependent jobs.

## PROPOSE

None. No additional mechanic, resource, gate, attraction condition, reconciliation
or S22 redesign was implemented or proposed.

## RISKS

Fifteen edge-voice entries deliberately remain prose-pending for Claude. These
are implemented contracts, not final prose or independently certified ≥91 scores.
The inherited verifier, slot and shared-test failures prevent claiming every requested
gate green. Headless managed fixtures report expected Unity/Mono boundary
warnings and one existing nullable warning; they pass but do not substitute
for live gameplay or a game-save round trip. No game, harness, install or full
build/suite was run.

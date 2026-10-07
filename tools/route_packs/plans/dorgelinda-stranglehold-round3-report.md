# Dorgelinda — polish round 3

Finding numbers below are one-based entries in `/work/Writer/judging/codex/dorgelindar2.json`. That audit applies no caps. None of its defects were already fixed in the current assembled export; **verified-fixed: none**. Changes are uncommitted, as requested.

## CHANGES

| Finding | Status | File and result |
|---|---|---|
| 1 — impossible professional epilogue | **escalated** | The assembled `epilogue.commit` still requires romantic `payoff.partner` while forbidding commitment. The route declaration already requires methods and excludes closure, but shared contract integration reapplies the contradictory gate. |
| 2 — duplicate solo denial | **fixed** | `storylines/dorgelinda_round3.py`, invoked by `dorgelinda_ledger.py`: retire saved answer 3 by gating; retain honest solo answer 4 and the earned, labelled lie at 5. Exactly one denial displays in either history. |
| 3 — interchangeable initial reactions | **fixed** | The round-3 module replaces every `named.*` acknowledgment with a distinct judgment. Consequential disclosures get separate exchanges; routine disclosures share compact batches, rather than forty mandatory name pages. Both paired relationships receive plural treatment. |
| 4 — interchangeable follow-up reactions | **fixed** | Separate returning reactions for all forty relationship entries, and separate batch responses. She asks what changed and retains her original private terms. |
| 5 — extraordinary initial disclosures | **fixed** | Commander answers identify Areelu, Minagho/Chivarro, Hepzamirah, Devarra, Melazmera and Iomedae. She answers from her supply service, soldiers, prejudice and private interests before the existing handshake. No new cost, closure requirement or relationship gate. |
| 6 — extraordinary renewed disclosures | **fixed** | Those six receive fresh assessments in `changed_columns`, without repeating the original acknowledgment. Her existing rooms/stores terms remain the negotiated outcome. |
| 7 — pair/individual duplication and pacing | **fixed** | Pair entitlement suppresses separate Anevia/Irabeth disclosure; naming the pair records both people and their joint arrangement. Exact subsets of four routine names are batched into one answer, recording only actual disclosures. |
| 8 — repeated roster in follow-up | **fixed** | Route-local `disclosed.*` receipts and live `undisclosed.*` readers identify additions. Previously named partners are skipped. Both old saved graphs remain, with their node order and answer indices intact. |
| 9 — one-shot renewal | **fixed** | `changed_columns` accepts either `sole_line` or `terms_kept`. Retain its saved terminal choices, gated off in new histories; append exits that record the disclosure without completing the scene. The next earned addition makes the same conversation available again. Cold histories end at the returns, without mending the seal quarrel or restoring private visits. |
| 10 — settled Last Call invocation | **escalated** | `lastcall.callable` still reads the persistent cost/deed flags, and `lastcall.call` still offers to settle an open account after `told_all`. |
| 11 — reopened account in Last Call ending | **escalated** | `lastcall.page` still has the unconditional unbalanced-books opening and repeated confession paragraph. |
| 12 — invented twice-weekly audit | **escalated** | The hostile paragraph still reads `audit_hostile` alone, without `twice_weekly`. |
| 13 — Last Call restores cold suppers | **escalated** | The same paragraph still ignores cold/unmended histories. |
| 14 — mid-sentence capital | **fixed** | `storylines/dorgelinda_ledger.py`: `They're` becomes `they're` in `carried_forward/paid`. |

`tests/test_dorgelinda_round2.py` tightens denial cardinality and checks the new disclosure guards. `tests/test_dorgelinda_round3.py` covers all-partner receipts, paired names, exact routine batches, extraordinary explanations, distinct return reactions, two successive additions after solo/shared arrangements, cold outcomes and capitalization. `tests/DorgelindaTricksterTests.cs` adds exported-story progression through three successive native-romance additions.

These are authored conversations at her existing Drezen desk, not new native history or supernatural knowledge. Canon anchors checked in `/wrath/blueprints.zip` and `enGB.json`: Logistics_2/Cue_0001 (`d94aa015becda004ea2484ea8a50fff7`), Logistics_Officer/Cue_0013 (`4145e730c140cfe4abfbd4ff33076221`); native localization identifies Hepzamirah as Baphomet's daughter and Melazmera as the **umbral dragon of Colyphyr**. No new fate device, echo, native rewrite or intimate encounter was added.

## CLASS SWEEP

- All forty `named.*` nodes in each disclosure scene; six extraordinary disclosures and both paired relationships; full and sparse rosters, pair plus individual entitlements, and previously named versus newly earned relationships.
- Honest solo denial and labelled lie; both initial arrangements; repeated additions; every terminal continuation, refusal and cold/mended dispatch.
- Current assembled professional fallback, Last Call invocation/coda, settlement, hostile prepared/late frequency and unreconciled private visits. Shared findings remain present.
- Old node order and choice identities compared against the pre-edit assembled export: zero failures. Existing CRLF source/C# files and LF Python test file retain their original endings. Existing explicit slot/brief is unchanged.

## GATE

All exports, logs and build products used a system-temp directory and were deleted after verification; `development/Story.json` is untouched. `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`, `/wrath` game data and the build script's parent-binding files are used. `RRT_STORY_OUTPUT` directs expansion to system temp; `RRT_TEST_STORY` and `RRT_TEST_BUILD_ROOT` keep test inputs and outputs there.

- `python expansion.py`: **pass**, final-source export has **3,848 scenes**. Its parsed JSON is identical to the schema-corrected export used for the passing C# tests and lints.
- Focused Dorgelinda + UTF-8 checks: **24 tests pass**.
- Round-2 disclosure save-reference comparison: **0 hard failures**, old node order preserved.
- Final C# build with `RRT_TEST_BUILD_ROOT` in system temp and build servers disabled: **pass, 0 errors**.
- `python tools/savecompat.py --story <temp>/Story.json`: **0 hard failures**.
- `python tools/payoff_lint.py --strict --story <temp>/Story.json`: **42 routes, 0 hard failures**.
- `python tools/departure_lint.py --strict --story <temp>/Story.json`: **43 women, 0 hard failures**.
- `python -m unittest discover -s tests -p "test_*.py" -q`: **exit 143, no result summary**, including the retry using `RRT_TEST_STORY` to reuse the export.
- `dotnet run --project tests/RulesTests.csproj -c Release -- <temp>/Story.json` (reuse the completed build with `--no-build`): first rejected an empty `DerivedForbids` entry; source fixed. Retry **exit 143 before completion**, without a reported failing assertion or "Page has no selectable answers". No full-suite success claimed.
- `dotnet <temp>/build/bin/Release/net8.0/RulesTests.dll --suites DorgelindaTricksterTests <temp>/Story.json`: **12,877 assertions pass** after the schema fix.
- `python tools/rrt_verify.py --strict --story <temp>/Story.json --game /wrath`: **1 hard failure**, the empty Areelu `DerivedForbids` entry in the export read before the schema fix. All other strict checks report no hard failures. Corrected-export retry `python tools/rrt_verify.py --strict --gate-only --story <temp>/final-Story.json --game /wrath`: **pass, 0 hard failures** (all strict checks, report-only analyses skipped).
- `git -c core.whitespace=cr-at-eol diff --check`: **pass**.

## ESCALATE

1. Fix the professional surface classification in `tools/payoff_contracts.json` / its shared consumer. Preserve `methods_heard`, open/current availability and returned-Commander guards; do not make professional accounting romantic acceptance. Add the requested generated-story availability witness there.
2. Shared `storylines/lastcall_partners.py` ownership: dispatch invocation, opening and called paragraph on `told_all`; retain participation through the existing personal bond. Dispatch hostile frequency on `twice_weekly`, and cold/unmended versus earned reconciliation separately. These shared files are explicitly excluded from this implementer's scope.
3. `tools/route_packs/voice_locks.json` is absent from this checkout. The coordinator must verify the edits against its current lock manifest; no locked-scene inventory was available to read.

## PROPOSE

None. No additional mechanic, price, attraction requirement or reconciliation condition proposed.

## RISKS

- Five unresolved shared findings prevent a claim that every rubric dimension reaches 91. No independent score is claimed.
- The engine continues honoring completion of `changed_columns` in older development saves. New histories use the appended non-completing exits; prior completion receipts and saved references are preserved, consistent with the rubric's pre-release-state rule.
- Full Python discovery and unfiltered C# validation terminated with exit 143 without completing. No whole-suite pass or exhaustive progression guarantee is claimed.

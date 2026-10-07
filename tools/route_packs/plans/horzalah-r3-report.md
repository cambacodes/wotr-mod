# Horzalah round 3

No commit. Scope: Horzalah route, its regression tests, and this report.
Findings D01–D15 refer to the ordered defects in `horzalahr2.json`.

## CHANGES

| Finding | Status | File and result |
|---|---|---|
| CAN cap; D01, D02 | verified-fixed | Existing `engine_f6c.py` Guild/trio replacements require completed Guild ownership and survival, without current romantic presence. Free departure retains both replacements. Native cue GUIDs and localization were checked in `/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`. |
| BEL cap; D12 | verified-fixed | Existing shared Last Call integration requires `horzalah.lastcall.account_due`, which requires ear + primed + returned. The legacy ear-only callable reader is deliberately preserved. An open ear-only history does not receive the completed bargain call. |
| COX cap; D15 | verified-fixed | Existing Last Call recovery paragraph requires `lastcall.recovered_corked`, describes the returned Commander, and explicitly keeps the flask corked. The separate bridge paragraph preserves concealment. |
| D03, D04, D05 | escalated | Nocticula kept/free/threat still use the superseded presentation location. No prose edited: the required `tools/route_packs/voice_locks.json` is absent from this checkout and the supplied Writer tree. Coordinator must check its lock inventory before correcting this cross-route voice. |
| D06, D09 | escalated | The route already supplies `polish_sister_consumers`, but final assembly never calls it after participant integration. Guild's generated `sister_absent` still conflates loss/departure; name lacks the exported historical variants. Needs out-of-scope `expansion.py` hook. |
| D07, D08 | escalated; helper repair prepared | `horzalah_guild.py`: enforce historical-return exclusion on all four generic report edges even when the folded branches already exist. Limit this exclusion to incoming hall/came/late/box nodes; reaction exits remain selectable. Shared departure integration still overwrites these guards in the delivered export. The coordinator must call the helper after that integration too. Not claimed fixed in shipped output. |
| D10, D11 | fixed | `horzalah_trickster.py`: both collar locations record reaching vs brand-question refusal. Both reconsideration locations append a brand-specific response and mutually exclusive continuation, retaining existing choices/targets and her original decision. |
| D13 | fixed | `horzalah_guild.py`: the same knife-delivered letter works in Drezen or camp, without an invented departure, tents or return-to-Drezen order. No new travel gate or delivery event. |
| D14 | fixed | `horzalah_trickster.py`: her purchased death wagers pay on death and lose on return. She explicitly demands the loss; no unexplained debts owed by demons. |

The refusal-history receipts and response are authored continuity additions, not native lore. They record existing player actions and do not change romance eligibility, costs, attraction, commitment or reconciliation. Existing four explicit slots and their briefs are preserved; no new intimate situation or explicit prose is added. No new foresight/echo beat or canon rewrite is introduced.

## CLASS SWEEP

- Both collar and reconsideration location twins; all existing refusal outcomes retain their mechanics plus factual history receipts.
- Both folded Chapter 6 reports: every hall/came/late/box incoming edge, current/departed/unavailable/never-returned histories, and came/late/box priority. The route helper is tested on the assembled graph; that test explicitly does not claim the absent exporter hook ships.
- Sister reaction exits checked to avoid a new dead end. Guild/name and both native leadership surfaces checked in the final assembly.
- Remote knife letter read/onward nodes and retained delivery budget; epilogue wager paragraph and Last Call recovery history readers.
- Existing ending exits, node/answer identities, CRLF source endings, and explicit-slot inventory preserved.

## GATE

`$TMP` below was a system temporary directory, deleted after verification.

| Command/check | Result |
|---|---|
| `python expansion.py` with `RRT_STORY_OUTPUT=$TMP/Story.json` | Passed; final export has 3,848 scenes. |
| `python -m unittest tests.test_horzalah_polish tests.test_horzalah_round2 tests.test_horzalah_round3 -q` | Passed: 20 tests on the final export. Includes helper-only pending-integration coverage, explicitly identified as such. |
| `python tools/savecompat.py --story $TMP/Story.json` | Passed: 0 hard failures. |
| Strict UTF-8 decoding of all four changed files; original CRLF checks; `git -c core.whitespace=cr-at-eol diff --check` | Passed; both existing route files retain exclusively CRLF line endings. |
| `python tools/payoff_lint.py --strict --story $TMP/Story.json` | Passed: 42 routes, 0 hard failures; existing review notices retained. |
| `python tools/departure_lint.py --strict --story $TMP/Story.json` | Passed: 43 women, 0 hard failures; existing review notice retained. |
| `python tools/rrt_verify.py --strict --story $TMP/Story.json` | Passed on final export: 0 hard failures; 0 shipped structural errors and 0 draft-contract diagnostics (827.4 seconds). An earlier run was cancelled when the helper source correction required a regenerated export. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | Attempted; host guard terminated it, exit 143. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- $TMP/Story.json` | Attempted; host guard terminated it, exit 143. |
| `dotnet build tests/RulesTests.csproj -c Release` with `RRT_TEST_BUILD_ROOT=$TMP/rules-build` | Passed: 0 errors, 8 existing unused-field warnings. Build success is not progression validation. |

All generated JSON, logs, verifier reports and .NET intermediates are directed to a system temporary directory. Commands use `PYTHONHASHSEED=0`, UTF-8, and parent bindings matching `build-expansion.ps1` for the final generation/gates. `development/Story.json` is untouched. No full build, harness, game, or commit.

## ESCALATE

1. `expansion.py`: call `horzalah_guild.polish_sister_consumers(payload)` after participant integration **and the departure-contract rewrite**. Verify the final guild/name variants and both folded reports, not just the route helper. This file is outside the allowlist; no monkey patch or alternate availability mechanism was added.
2. Supply/check the missing voice-lock inventory, then correct Nocticula's kept/free/threat presentation sequence: headquarters in Baphomet's realm first, old Alushinyrra hall afterward. Preserve each reaction and her city interest.
3. Host `/work/testguard.sh` killed the requested unittest discovery and C# rules/progression commands (exit 143) because this is an `RRT-r3-*` worktree. The rules project built successfully in system temp; full acceptance remains unverified. Host guard was not changed or bypassed.

## PROPOSE

None. No additional mechanics, gates, costs, relationship requirements or redesigns.

## RISKS

- D03–D09 remain unresolved in delivered output for the reasons above. This is not a claim that every rubric dimension reaches 91.
- Missing voice-lock inventory prevents independent verification of the full lock set. Existing Horzalah prose was preserved apart from the audited travel and wager corrections; new brand-history prose is append-only.
- Python full discovery and C# progression acceptance were terminated by the host guard. Static and route-only results do not substitute for that runtime validation.

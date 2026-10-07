# Delamere round 3

## CHANGES

Latest audit: `/work/Writer/judging/codex/delamerer2.json`. No caps were applied. All nine defects were checked against the current checkout before editing; none was already fixed by the shared endings jobs.

| Finding | Status | File and result |
|---|---|---|
| HOW: `woken.names` | Fixed | `storylines/delamere_fire.py`: answers the crypt carving question with the villagers she guarded before death. Stone dust and the unfinished letter keep the staging with the memorial. Both original answers still lead to `how_many` / `look`. Partner names and the measuring cord remain in `woken.hide`. |
| HOW: `woods.second_hunt` | Fixed for first postponement; repeated postponements escalated | `storylines/delamere_woods.py`: the existing 24-hour delay now reads the invitation and held postponement receipt, using `RequiresAnyGroups`. The invitation remains mandatory; the new alternative creates no new entry requirement. |
| HOW: `woods.second_hunt_page` | Fixed for first postponement; repeated postponements escalated | Same shared receipt guard in the Kyado-dead delivery. Abort, open relationship and postponed epilogue paragraph are preserved. |
| HOW: `woods.second_hunt_late` | Fixed for first postponement; repeated postponements escalated | Same guard in Chapter 5. The earned late epilogue remains available when the war ends during the wait. |
| BEL: `crypt.stag` | Fixed | `storylines/delamere_trickster.py`: shared successful chase uses equipment-independent wording. |
| BEL: `crypt.stag_alone` | Fixed | Receives the same shared waking-function correction. |
| BEL: `crypt.stag_late` | Fixed | Receives the same shared waking-function correction. |
| BEL: `drezen.stag` | Fixed | Receives the same shared waking-function correction. |
| BEL: `temple.prior_lessons` | Fixed | `storylines/delamere_fire.py`: her archery challenge refers to watching the Commander run, rather than assuming a sword and incompetence with it. |

`tests/DelamereRound2Tests.cs` exercises production availability before postponement, immediately after abort, one hour before and at the 24-hour boundary in all three deliveries; checks both invitation/postponement anchors, the open relationship, and the earned late ending during the wait. `tests/test_DelamereRound2.py` replays both memorial transitions and all four successful waking variants and checks the cord stays in the hide scene.

Canon checked locally: `/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`, `DelamereInTomb/Cue_0039` (`ac70a1232f79fd648849c9d108b27dc1`, village protector) and `Cue_0042` (`20f0dfa4426be104bb02cd93a523c496`, three-day stag hunt). The memorial's retained details are existing authored additions, not new canon claims. No new lore, romance requirement, cost, return device, foresight beat or intimate moment was introduced.

## CLASS SWEEP

- All four waking exports come from the corrected function. Searched the route's sibling files for sword assumptions; the audited archery challenge was the other occurrence.
- All three second-hunt deliveries use the same clock alternative; refusal/claim closure and retry abort keep their original indices and effects.
- Reviewed the full memorial chain and both outgoing transitions, plus hide measurement, partner names, `names_paid`, and the ending's cord reference.
- Existing explicit slots and shared Last Call/ending text were not changed. No audit finding concerned premature fades.
- Scene IDs, node IDs, relationship IDs, answer indices, old targets and legacy ending exits were not changed. Original CRLF in all three story files and LF in both test files were preserved.
- The referenced checkout `tools/route_packs/voice_locks.json` is absent. Searched neighboring worktrees: both discovered copies (`RRT-voicelock`, `RRT-harem-int-w2`) have an empty `locked` map. Prose edits were limited to the audited passages.

## GATE

All commands use `PYTHONHASHSEED=0`. The export uses `RRT_STORY_OUTPUT`; tests use `RRT_TEST_STORY`; C# build artifacts use `RRT_TEST_BUILD_ROOT`. These point outside the repo. `RRT_PARENT_BINDINGS` uses the four existing manifests selected by `build-expansion.ps1`.

| Command | Result |
|---|---|
| `python expansion.py` | PASS: 3,848 scenes exported into system temp; protected `development/Story.json` untouched. |
| `python tools/savecompat.py --story TEMP/Story.json` | PASS: 0 hard failures. |
| `python tools/payoff_lint.py --strict --story TEMP/Story.json` | PASS: 42 routes, 0 hard failures. The inherited Delamere late-readiness REVIEW was checked: the invitation plus truth/confession is the existing earned late road; no new acceptance mechanic was added. |
| `python tools/departure_lint.py --strict --story TEMP/Story.json` | PASS: 43 women, 0 hard failures. |
| `python -m unittest tests.test_DelamerePolish tests.test_DelamereRound2 tests.test_utf8_io -q` | PASS: 17 tests. |
| Earlier Python run also including `tests.test_savecompat_baseline` | Stopped as redundant after the standalone savecompat check and focused route/UTF-8 checks passed; it was rebuilding the expansion again. |
| `dotnet build tests/RulesTests.csproj -c Release` | PASS: 0 errors; 8 warnings from unchanged `DeliveryInventory2Tests.cs`. All obj/bin files were outside the repo. |
| `dotnet run --project tests/RulesTests.csproj -c Release --no-build -- TEMP/Story.json --suites=DelamereRound2Tests` | PASS: 4,609 assertions. |
| Focused C# run including `DelamereTricksterTests` | INCOMPLETE: new round-3 suite printed PASS; later terminated with exit 143/SIGTERM and no assertion diagnostic. The new suite was then rerun alone successfully. |
| `python -m unittest discover -s tests -p 'test_*.py' -q` | INCOMPLETE: exit 143/SIGTERM, no assertion diagnostic. |
| `dotnet run --project tests/RulesTests.csproj -c Release --no-build -- TEMP/Story.json` | INCOMPLETE: exit 143/SIGTERM after an early engine test PASS. No page-without-selectable-answers diagnostic was emitted. |
| `python tools/rrt_verify.py --strict --gate-only --game /wrath --story TEMP/Story.json --json TEMP/verify.json --text TEMP/verify.txt` | PASS: 0 hard failures; 0 structural errors and 0 draft contract diagnostics. Gate-only runs every strict check and omits report-only world/budget analyses. |

All task temporary exports, logs and external build outputs were deleted after verification. Line-ending byte checks passed for all edited existing files. `git -c core.whitespace=cr-at-eol diff --check` passed.

## ESCALATE

- **Repeated postponements, HOW findings 2–4:** `src/Main.cs` skips an already-held choice flag before stamping `hour.<flag>`; `tests/Program.cs` similarly timestamps only when `Flags.Add` succeeds. Consequently a second postponement cannot refresh `second_hunt_postponed`. Route data can enforce the first postponement and honor any supplied latest timestamp, but cannot create an unlimited refreshable clock using the permitted schema. A shared runtime clock repair and mirrored walker behavior are needed to finish these findings. No shared file was edited, and no finite retry cap, added requirement or new scene was introduced to hide the limitation.
- Live Chapter 5 crypt/temple access still requires coordinator/game validation, as recorded by the earlier audit. No game or harness was run.
- The requested broad Python discovery and unfiltered C# gate need an environment rerun: both received SIGTERM without an actionable failure. Focused route checks passed; broad success is not claimed.

## PROPOSE

None beyond the required shared clock repair above.

## RISKS

Repeated postponement remains incomplete pending shared-code integration. No independent score certification was run. No commit was made, following the user's final instruction.

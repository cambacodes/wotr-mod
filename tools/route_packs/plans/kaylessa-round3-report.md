# Kaylessa — polish round 3

Uncommitted changes against the supplied merge-e base. Finding numbers follow `/work/Writer/judging/codex/kaylessar2.json`. Every cited defect and the cap were checked against current source before editing; **none was already fixed by the shared endings jobs**.

## CHANGES

| Finding | Status | File and repair |
| --- | --- | --- |
| BEL cap; D4, clean ambush | fixed | `storylines/kaylessa_trickster.py`: the existing warning/preparation now arranges a south-road patrol and marked hiding hollow. Both clean volleys extinguish the lantern, conceal the Commander and the burning glamour, show fallen silhouettes, and carry the patrol pressure through the archers' withdrawal. Existing `alive.planned`, check DCs, failure branches, prices and outcomes remain unchanged. |
| D1, deliberate-kill bargain | fixed | Same: separately bind native `Answer_0011`, `Answer_0018`, `Answer_0029`; derive `kaylessa.early_player_killed`; add an unavailable guard with no override. |
| D2, sending bypass | fixed | Same: both devices explicitly forbid the permanent closure; Council departure/fight does not bypass it. |
| D3, prohibited arrival | fixed | Same: arrival and presence forbid the closure, including stale paid/returned saves. All route-local ending pages also carry the guard because epilogues bypass ordinary relationship checks. Python/C# tests check closure, romance and household eligibility for every attack; positive payment/arrival assertions use Reveal deaths. |
| D5, letter reinforcement presence | fixed | `storylines/kaylessa_wasps.py`: her evidence is the recorded arrival and tomb, without a present army or barracks claim. |
| D6, tomb reinforcement presence | fixed | Same: fifty marksmen came west and built the memorial in the past; remembered songs do not guarantee survivors or a posting. |
| D7, undelivered introduction | fixed | Same: explicitly postpone any meeting until survivors are found; discussion sets `introduction_requested`, never disclosure. The old `marksmen_told` key is retained as legacy history. No new introduction event or troop reader was invented. |
| D8, sending recollection drift | fixed | Same: she recalls the camp table, dust-stained letters and answer in the dust. |
| D9, delayed morning | fixed | `storylines/kaylessa_clearing.py`: all remembered action uses retrospective narration; both choices recall the actual morning and both terminal choices return to the present awning. Existing linger flag and exit mechanics remain. |
| D10, duplicated threshold | fixed | Same: move the useful dagger continuity to `cut`; preserve `explicit.1` as the brief environmental continuation. The sibling late-epilogue slot no longer repeats catching the collar. Existing slot IDs, answers and effects remain. |
| D11, accelerated correspondence | fixed | Same: reply delay is thirty days: ten days outward, time for circulation, ten days back. No magical dispatch or extra price. |
| Regression coverage | added | `tests/test_kaylessa_round3.py`, `tests/KaylessaTricksterTests.cs`, and `tests/KaylessaRoundThreeTests.cs`: attack/Council/legacy-return matrix, Reveal positives, prepared clean branches, lost reinforcements, request-only receipt, sending recollection, both morning exits, slot continuity and earliest reply. The small managed suite exercises the production rules independently of the old suite's long reachability search. |
| Epilogue slot brief | fixed | `tools/route_packs/explicit_slots/kaylessa/kaylessa.trickster.epilogue.commit.explicit.1.json`: explicit `narration: third-past`, matching example and final line. No explicit prose generated. |

Native evidence checked directly in `/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`: attacks `ac4468a7eded7fd43946f1a730791ff0`, `53a2540656646e44e92e3d9b30b35179`, `0673b59a2f25dbf459a4dfe1dfa09c7a` all lead to `Cue_0019` (`1686b22fd9f8d364e9cee0180d95ce1b`); native `Kaylessa_Letter` (`472666a07cd05b441b0d8c57f50de13d`) has `ResolutionTime=10`.

The patrol/concealment, postponed introduction and thirty-day living correspondence are **authored extensions** of the existing situations, not claims of native events. Her existing suspicion, appetite, vengeance, curse, choice of custody and refusal roads remain. No partner subsystem, affection requirement, reconciliation gate, cure, fee or new foresight/echo beat was added. Existing Trickster producer gates remain.

## CLASS SWEEP

- Checked both hunters' warning/clean-volley branches, both paid-return devices, arrival, presence, romance, household route guards and all five route-local epilogues.
- Checked both reinforcement claims, the conditional reinforcement passage in Avennara's reply, disclosure producers and all sending-price recollections.
- Checked every morning curse variant, both custody variants and both exits; checked both reserved intimacy slots for repeated initiating motions.
- IDs, node order and choice indices remain; existing reserved slot exits remain inert. All modified pre-existing files retain CRLF with no bare LF introduced.

## GATE

All generation uses `PYTHONHASHSEED=0` and the four parent-binding manifests selected by `build-expansion.ps1`. Generated Story.json, verifier reports, and managed obj/bin outputs go to a disposable system-temp directory; the forbidden `development/Story.json` is untouched. Commands below use that fresh `<tmp>/Story.json` instead of the stale development export. `RRT_STORY_OUTPUT`, `RRT_TEST_STORY`, and `RRT_TEST_BUILD_ROOT` select the temporary paths.

| Command/check | Result |
| --- | --- |
| `python expansion.py` | PASS, exit 0; 3,848 scenes. Export labels itself an incomplete development export; no release build was attempted. |
| `python tools/savecompat.py --story <tmp>/Story.json` | PASS; 0 hard failures. |
| `python -m unittest tests.test_kaylessa_round2 tests.test_kaylessa_round3 tests.test_utf8_io -q` | PASS on final regenerated export; 20 tests, 10.958 seconds, after correcting missing fixture history inputs. |
| `python tools/payoff_lint.py --strict --story <tmp>/Story.json` | PASS; 42 routes, 0 hard failures. Inherited Kaylessa late-readiness REVIEW remains outside this audit's scope. |
| `python tools/departure_lint.py --strict --story <tmp>/Story.json` | PASS; 43 women, 0 hard failures. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | INCOMPLETE; exit 143, no summary. No pass inferred. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- <tmp>/Story.json` | INCOMPLETE; exit 143, no verdict. No pass inferred. |
| Same managed command with `--routes kaylessa` | FAIL in the unedited `CamelliaTricksterTests`, oath answer exclusivity; ESCALATE below. The selector runs shared/cross-route suites too. |
| Same managed command with `--suites KaylessaTricksterTests` | INCOMPLETE on final source, exit 143 after compilation. Earlier runs exposed and corrected the old shape assertion's missing early-kill guard; no later assertion failure was reported. |
| Same managed command with `--suites KaylessaRoundThreeTests` | PASS on final regenerated export; 178 assertions. `Rules.Validate` also passed before the selected suite. |
| Combined route/savecompat/UTF-8 run | All 11 savecompat tests produced no failures; the overall 31-test run failed on two stale route fixtures loaded before their correction. The final separate route/UTF-8 run above passed. |
| Source identity comparison; CRLF; `git -c core.whitespace=cr-at-eol diff --check` | PASS; original scene/node order and choice counts preserved; no bare LF added to existing files; no whitespace errors. |
| `python tools/rrt_verify.py --strict --story <tmp>/Story.json --game /wrath --json <tmp>/verify.json --text <tmp>/verify.txt` | First full run: 1 hard failure, a newly introduced quoted-paragraph speaker-attribution review in `alive.warning/swap`; corrected by an explicit Kaylessa action. All other strict conditions were clear. Runtime 818.8 seconds. |
| Same verifier with `--strict --gate-only --quiet`, final regenerated export | PASS, exit 0; **HARD FAILURES: 0**. This mode reruns every strict check and defers only advisory world/budget analyses already completed by the first full run. |

## ESCALATE

- The referenced `tools/route_packs/voice_locks.json` is absent from this checkout and the supplied Writer tree. No lock list could be evaluated; the coordinator must supply it if there are additional applicable locked scenes. No substitute registry was created.
- The `--routes kaylessa` selector fails `tests/CamelliaTricksterTests.cs:256`: "The oath does not offer exactly one route for its world." The unedited `camellia.trickster.kills_answered.oath_camp/start` contains overlapping Soana fallback choices. Another route's scene and test are outside this task; neither was changed.
- Full Python/managed progression checks and the older managed Kaylessa suite were terminated with exit 143 without summaries. Coordinator infrastructure must complete them; no suite was disabled or weakened. No "Page has no selectable answers" failure was emitted, but incomplete runs do not certify exhaustive progression.

## PROPOSE

None. The requested postponed-introduction repair deliberately leaves a possible future meeting unimplemented.

## RISKS

- No independent audit or score is claimed; the coordinator/auditor must judge the revised situations.
- Broad progression validation remains incomplete, and a shared oath assertion fails. The passing focused checks do not certify a release build.
- Legacy saves with an already-set `marksmen_told` retain that historical key; fresh discussion never produces it. All old node and answer references remain.
- Thirty-day correspondence can arrive late or remain unseen if the player proceeds to Threshold sooner; that travel boundary is intentional.

All temporary exports, verifier reports, managed build outputs, the temporary editing script and repository bytecode caches were removed before handoff. No commit, full build script, harness or game launch was performed.

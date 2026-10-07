# Seelah round 4 local residue

Base: `5dd587bd3277fa985e4293601290f59ad8dfcd6e`.
No commit made, following the final task instruction. No independent score claimed.

## CHANGES

| Finding | Status | File / evidence |
| --- | --- | --- |
| seelah:D09 | Done | `storylines/seelah_round2.py`, `prepare`: `epilogue.refused/end` now says Seelah refused the Commander's request. Scene eligibility is unchanged. |
| seelah:D10 | Done | Same page, paragraph 0: she has not withdrawn her no, and recalls what she required before another request. Neither time nor a shared drink settles it. The wording also accommodates settlement without a subsequent request. |
| seelah:D11 | Done | `new_scenes`, `dead.list_reclaimed`: original `start[1] -> offer` selects the existing romance callback. Appended `start[2]` selects that callback for a played market courtship without a kiss. Appended `start[3] -> offer_first` gives a first invitation when neither history exists. |
| seelah:D12 | Done | `after.list_reclaimed` receives the same first/repeat distinction through its existing deep copy. Fresh courier return can reclaim the list before courtship without recalling a previous evening. |
| seelah:D01 | Out of scope | Shared reference guard: pickpocket coin answer's `iomedae.closed` dependency. |
| seelah:D02 | Out of scope | Shared reference guard: diamond-held effects answer's `iomedae.closed` dependency. |
| seelah:D03 | Out of scope | Shared reference guard: no-diamond effects answer's `iomedae.closed` dependency. |
| seelah:D04 | Out of scope | Shared reference guards: pickpocket scene/answers' `crossroute.irabeth.unavailable` exclusions. |
| seelah:D05 | Out of scope | Shared reference guards: effects scene/answers' `crossroute.irabeth.unavailable` exclusions. |
| seelah:D06 | Out of scope | Shared reference guard: dead seller-word exclusion. |
| seelah:D07 | Out of scope | Shared reference guard: outside-party seller-word exclusion. |
| seelah:D08 | Out of scope | Shared reference guard: `seelah.souls/start[0]` depends on `arsinoe.closed`. |
| seelah:D13 | Out of scope, S2 | Impossible appended `dismissed.commit/list_back` exit. Existing retirement retained. |
| seelah:D14 | Out of scope, S2 | Impossible appended `dismissed.second_ask/price` exit. Existing retirement retained. |

S3 repeats D09-D12; those are addressed above. S1 contains no Seelah-owned section. J01-J10 rulings, shared work and S0 Claude rebuilds were not implemented in this route job. No refused beats.

`tests/test_seelah_round4.py` walks retained-body and courier returns without courtship, both reclamation twins with prior romantic or non-kissed courtship, both refusal twins' freedom/list/first-coin producers, renewed-commitment exclusion and the unreturned let-her-go history. `tests/test_seelah_round2.py` now follows the appended first-invitation answer in its existing fresh-history custody test.

`tools/route_packs/plans/voice-review-pending.json` lists all three touched scenes for Claude. None is voice-locked; no prose-pending entry is needed.

Authored addition: `offer_first` is a local first invitation, explained by the actual returned Seelah reclaiming her own list and answering the Commander's question. It adds no return device, eligibility requirement, price, romance flag, reconciliation condition or echo.

Native voice anchor verified directly in `/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`: `Ch1_SeelahMeetsFriends/Cue_0006`, blueprint `a3d0b31d35fc785418c78ded53cb278d`, enGB key `b9c43cae-d4c0-48f1-a042-6e928e300ca5`. Seelah initiates good company during the crusade's devastation. Per-scene use:

| Scene | Want / on-page act / cost |
| --- | --- |
| `seelah.trickster.dead.list_reclaimed` | Her own account of Acemi and the Kenabres stones, plus company she chooses. She takes back the list, taps the coat and proposes Fye's before muster. The resurrection's existing expenditure and obligations stand; reclamation grants neither romance nor commitment. Native enGB: `b9c43cae-d4c0-48f1-a042-6e928e300ca5`. |
| `seelah.trickster.after.list_reclaimed` | Same agency and action after the courier return; the return alone supplies no remembered date. Existing return costs and her list's obligations stand. Native enGB: `b9c43cae-d4c0-48f1-a042-6e928e300ca5`. |
| `seelah.trickster.epilogue.refused` | Her chosen work and the terms of her own refusal. She takes her sword north, visits on leave and returns to muster without withdrawing her no. Private courtship remains unresolved; no free reconciliation. Native enGB: `b9c43cae-d4c0-48f1-a042-6e928e300ca5`. |

## CLASS SWEEP

- Walked every route-local `declined` producer: `dismissed.late/start[2]` and `no`, `no_death`, `no_stones` in both commitment twins. Kept the unreturned paragraph separate and retained earned presence gates.
- Checked both reclamation scenes, familiar and first offers, and both existing offer answers. Exactly one invitation answer renders for fresh, ROMANCE-only, COURTED-only and combined histories. Quiet company does not set GAME; neither branch creates romance or commitment.
- Checked adjacent second-ask callbacks: they already require romantic history and keep the existing freedom, list and first-coin receipts. No expansion of eligibility.
- Baseline/current route comparison changes exactly `epilogue.refused`, `dead.list_reclaimed`, `after.list_reclaimed`; no other scene or top-level route field changes. Existing node order, choice indices, text labels, destinations and effects are preserved; only callback selectors and appended alternatives differ.
- Both edited existing files were LF at base and remain LF. No shared storyline, engine, generated development file or other route edited. No echo added; no canon event rewritten.

## GATE

All Python gates use `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`, `RRT_GAME_DIR=/wrath` and the four parent-binding files configured by `build-expansion.ps1`. `RRT_STORY_OUTPUT` points to a disposable system-temp export. Story-reading gates use `--story` with that same export; C# uses it as its positional argument. Build outputs are outside the repository.

| Command | Result |
| --- | --- |
| `python expansion.py` with `RRT_STORY_OUTPUT=$TMP/Story.json` | Exit 0; 4,054 scenes. Final export checked against the edited first-invitation and refusal prose. |
| `python -m unittest discover -s tests -p test_seelah_round4.py -q` | 5 tests pass. |
| `PYTHONPATH=tests:. python -m unittest test_seelah_round3 test_seelah_round4 -q` | 10 tests pass. |
| `python -m unittest discover -s tests -p 'test_seelah_round*.py' -q` | 18 tests: 17 pass, 1 inherited slot-text/brief mismatch (see ESCALATE). |
| `python -m unittest discover -s tests -p test_utf8_io.py -q` | 1 test passes. |
| `python -m unittest discover -s tests -p 'test_*.py' -q` | Host test guard terminates it, exit 143; no full-suite pass claimed. |
| `python tools/savecompat.py --story $TMP/Story.json` | 0 hard failures. |
| `python tools/payoff_lint.py --strict --story $TMP/Story.json` | 42 routes; 0 hard failures. |
| `python tools/departure_lint.py --strict --story $TMP/Story.json` | 43 women; 0 hard failures. |
| `python tools/voice_lock_lint.py --strict --story $TMP/Story.json` | 576 locked scenes; 0 changed; 0 missing/ambiguous. |
| `python tools/slot_brief_lint.py --strict --known-rebuilds --story $TMP/Story.json` | 320 briefs; 0 hard; 315 known rebuild; 168 warnings. No slot text or brief was changed. |
| `dotnet run --project tests/RulesTests.csproj -c Release --artifacts-path $TMP/dotnet -- $TMP/Story.json` | Compiles externally, then the SDK tries to launch the default repository output path, which is absent. No full C# pass claimed. |
| `dotnet $TMP/dotnet/bin/RulesTests/release/RulesTests.dll --suites=SeelahTricksterTests,SeelahLateCampaignTests,SeelahProgressionTests,SeelahAftermathTests $TMP/Story.json` | Exit 0 on final export: 310,879 assertions in 4 selected suites. Includes global `Rules.Validate`; no "Page has no selectable answers" failure. |
| `python tools/rrt_verify.py --strict --story $TMP/Story.json --json $TMP/verify.json --text $TMP/verify.txt` | Exit 1; 13 hard player-text diagnostics, all on untouched Jerribeth scenes listed below. No Seelah hard diagnostic. Run once on final export (758.2 seconds). Overall strict gate is not green. |
| `git diff --check` | Pass. |

## ESCALATE

- D01-D08 remain with the shared reference-guard owner; D13-D14 remain with S2. J01-J10 and S0 rebuild work remain with their assigned owners.
- The host test guard terminated the requested full `python -m unittest discover -s tests -p "test_*.py" -q` with exit 143. No attempt was made to bypass the guard.
- The inherited `test_slots_are_complete_and_quiet_choices_do_not_enter_them` fails on `seelah.door.explicit.1`. An isolated replay of HEAD's route source confirms last-line mismatches in all seven Seelah slot briefs, before these changes. The slot/brief owner must reconcile them; this task names no slot rewrite.
- The full C# `dotnet run` launch failed because it sought the repository's default output despite the external artifact settings. The compiled assembly's four filtered Seelah suites passed on the final export. Full progression validation remains a coordinator gate.
- Strict verifier: all 13 hard diagnostics are outside this job, in untouched, voice-locked Jerribeth prose. The Claude voice or player-text-lint owner must resolve them. No other route or shared lint/baseline was edited, and no out-of-scope prose-pending entries were added.

| Untouched scene / node | Strict diagnostic |
| --- | --- |
| `jerribeth.farewell/traitor_fed` | commander-gender |
| `jerribeth.farewell/discovery_distant` | speaker-attribution-review |
| `jerribeth.ending_together/catalogue` | commander-gender |
| `jerribeth.ending_ascended/catalogue` | commander-gender |
| `jerribeth.offered_signature/companion_regill` | commander-gender |
| `jerribeth.counterfeit_guest/maker` | commander-gender |
| `jerribeth.counterfeit_guest/square` | commander-gender |
| `jerribeth.counterfeit_guest/scout_known` | embedded-commander-speech |
| `jerribeth.counterfeit_audience/challenge` | commander-gender |
| `jerribeth.counterfeit_audience/leverage.reply.1` | commander-gender |
| `jerribeth.counterfeit_audience/departure.reply.1` | commander-gender |
| `jerribeth.counterfeit_audience/raid_dismissed` | commander-gender |
| `jerribeth.counterfeit_spoil/object` | commander-gender |

## PROPOSE

None. No additional mechanics or route redesign implemented.

## RISKS

The overall strict verifier gate fails on the 13 out-of-scope Jerribeth diagnostics. Full-suite completion and independent scoring remain with the coordinator. The brief mismatch and explicitly excluded shared/S2 findings remain open. New first-invitation prose is queued for Claude review. Temporary exports, logs and build outputs were removed before handoff.

# R4 Mielarah implementation report

Base: `5dd587bd3277fa985e4293601290f59ad8dfcd6e`. No commit, per the final task instruction.

## CHANGES

| Findings | Status | File / evidence |
| --- | --- | --- |
| mielarah:D12, mielarah:D13 | Done | `storylines/mielarah_deck.py`, correction / freed, both placements: she defends protecting corrupted sailors, orders a bounded experiment with the existing doubled wages and berths ashore, and retains intervention against drawn steel. Both existing Good answer texts now propose that experiment rather than lecture her. |
| mielarah:D14, mielarah:D15 | Done | Same file, correction / kept: she owns the existing practice and assigns the gamblers separate watches on page; she no longer waits for the Commander to reform her. |
| mielarah:D16, mielarah:D17 | Done | Same file, stowaway / threat and scare: neutral refusal before correction or after kept/tightened; appended replies recall only FREED or LAUGHING. Existing answer indices 0–2 and the old scare node remain. |
| mielarah:D18, mielarah:D19 | Done | Same file, market / stays: she rejects the order as protection, orders unloading without her and restricted loading/helm access, and stays within reach to carry the crusade's wounded. The officer fetches the quartermaster. She bears extra voyages and crew wages; the Commander does not overrule her exile motive. Existing outcome flags and onward branch remain. |
| mielarah:D01–D04; K01–K03 | Out of scope | R4 assignment and S1 give the native Bad Luck attack witness / current-contact closure to J01/J10, ruling 41. No resurrection or reconciliation device added. |
| mielarah:D05–D11 | Out of scope | R4 assignment holds generated Nocticula historical-reference guards for shared owners. No other route or shared guard edited. |
| mielarah:D20 | Out of scope | R4 assignment holds the broad assembled-story kill/coexistence acceptance work for its owner. Local policy history tests do not claim to discharge it. |

`tests/test_mielarah_round4.py`: plays the pre-correction history and all four decisions, with/without the previously seen amulets, through both stowaway placements. Verifies exactly one policy reply and a selectable terminal answer. Walks each market outcome to its existing terminal without adding closure.

`tools/route_packs/plans/voice-review-pending.json`: six scene entries, each with route and finding IDs, for Claude's voice pass. No Mielarah text is voice-locked, so no prose-pending entry was required. S3 has no Mielarah-owned section; its Mielarah mentions belong to Dorgelinda's disclosure choices.

### Native voice evidence and authored additions

Verified directly in `/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`:

| Re-voiced scenes (including each arcade twin) | Native enGB key / blueprint | Want, action, cost |
| --- | --- | --- |
| mielarah.deck.correction; mielarah.deck.correction.arcade | `fc184d0b-57c5-4249-8b24-4de376636b87`, Tumberd/Cue_0054, `935e5b8a5c391e44b9eab842b4106197` | Save decent souls from irreversible mistakes; gives orders to bosun/gamblers; doubled pay and risk in the experiment, continued personal intervention if keeping her practice. |
| mielarah.deck.stowaway; mielarah.deck.stowaway.arcade | `fc184d0b-57c5-4249-8b24-4de376636b87`, same native protective purpose | Recover her guns and command her deck; checks/holsters them and frightens the thief into retreat; has to deal with the Commander's thief instead of tending her ship, without pretending he is her crew. |
| mielarah.deck.market; mielarah.deck.market.arcade | `f5084e2e-6893-4753-83c4-a2f61ec6f791`, Tumberd/Cue_0050, `e49f9ca1001aba84984440272e7e5ff2` | Continue useful shipping without exposing civilians to her curse; orders the quartermaster's unloading arrangement; extra voyages and wages, giving up her own market visits. |

Native contrast also checked: AirAdventures/Cue_0328, `d2093a8bf7e32704b861e2c213646a84`, enGB `93fb6648-5bc2-4be3-b134-6cfea2079d4b`: her disgust at lethal amulets does not repudiate ordinary protective thought-correction.

Authored additions: the on-page bosun/gambler orders, policy-specific Woljif replies, and city unloading arrangement. They use her existing ship, crew, portal, cargo and humanitarian purpose. No new mechanics, costs, gates, attraction/commitment conditions, return devices or echo beats beyond the assigned repairs.

## CLASS SWEEP

- Both correction decision menus, freed/kept outcomes, tightened/laughing siblings and both amulet aftermath paths checked for captain ownership. Tightened/laughing already preserve her decision and were retained.
- Both stowaway twins checked against pre-correction and FREED/KEPT/TIGHTENED/LAUGHING histories. Vouch and bet retain their existing behavior.
- All three market outcomes and their common boy aftermath checked. Prisoner/escort already have protective responses and were retained. Only stays required the agency repair.
- Route-level frozen scene/node/answer inventory checked by the existing save-compatibility regression. CRLF remains CRLF throughout the edited source; no bare LF introduced.

## GATE

All generator/check invocations used `PYTHONHASHSEED=0`; the generator and verifier used `RRT_GAME_DIR=/wrath` and the four parent-binding files from `build-expansion.ps1`. `gate_dir` below denotes the disposable system-temp directory. Generation and validation use that fresh export, leaving `development/Story.json` untouched.

| Command | Result |
| --- | --- |
| `RRT_STORY_OUTPUT=$gate_dir/Story.json python expansion.py` | PASS: 4,054 scenes. |
| `python -m unittest tests.test_mielarah_round2 tests.test_mielarah_round4 tests.test_utf8_io -q` | PASS: 11 tests; includes frozen route save inventory. |
| `savecompat.check(fresh_export)` | PASS: 0 hard failures against the global frozen inventory. |
| `python tools/payoff_lint.py --strict --story $gate_dir/Story.json` | PASS: 42 routes; 0 hard failures. |
| `python tools/departure_lint.py --strict --story $gate_dir/Story.json` | PASS: 43 women; 0 hard failures. |
| `python tools/voice_lock_lint.py --strict --story $gate_dir/Story.json` | PASS: 576 locked scenes; 0 changed; 0 missing/ambiguous. |
| `python tools/slot_brief_lint.py --strict --known-rebuilds --story $gate_dir/Story.json` | PASS: 320 briefs; 0 hard; 315 known-rebuild findings; 168 warnings. No slot text/brief edited. |
| `dotnet build tests/RulesTests.csproj -c Release -p:BaseOutputPath=$gate_dir/bin/ -p:BaseIntermediateOutputPath=$gate_dir/obj/` | PASS: 0 errors; 8 existing CS0649 warnings in DeliveryInventory2Tests. |
| `dotnet $gate_dir/bin/Release/net8.0/RulesTests.dll $gate_dir/Story.json --suites=MielarahTricksterTests` | PASS: 88,365 assertions. Runner calls `Rules.Validate` before the selected suite; no page-without-answer failure. |
| `git -c core.whitespace=cr-at-eol diff --check` | PASS. Edited source has no bare LF; CRLF preserved. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | BLOCKED: testguard termination, exit 143. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json` (with output/intermediate properties directed to system temp) | BLOCKED: testguard termination, exit 143. |
| `python tools/rrt_verify.py --strict --story $gate_dir/Story.json` (reports in system temp) | FAIL: exit 1, 13 hard player-text findings, all in unchanged Claude-locked Jerribeth scenes. No Mielarah hard finding; structural errors 0. Invoked once; 968.1 seconds. |

## ESCALATE

- Coordinator acceptance runner: the required unfiltered Python discovery and C# run were terminated (exit 143) by `/work/testguard.sh`. `/work/testguard.log` records `kill(full)` for `r4-mielarah`. The guard was not modified or bypassed. Full acceptance remains for the coordinator's authorized gate.
- D01–D04/K01–K03, D05–D11 and D20 remain with their designated shared/acceptance owners above. Local fixes do not establish safety after Answer_0071 or independence from generated Nocticula closure guards.
- Departure lint's existing review residual: `mielarah.expelled` has no reader or producer; the contract explicitly requires coordinator evidence to bind the opaque relationship loss. Outside D12–D19, not changed.

### Strict verifier failures outside this route

All 13 are player_text.hard in unchanged scenes whose voice-lock owner is Claude. They belong to the S0 Jerribeth rebuild, not R4-mielarah. No other route prose or prose-pending entries were changed.

| Scene / node | Hard code |
| --- | --- |
| jerribeth.farewell / traitor_fed | commander-gender |
| jerribeth.farewell / discovery_distant | speaker-attribution-review |
| jerribeth.ending_together / catalogue | commander-gender |
| jerribeth.ending_ascended / catalogue | commander-gender |
| jerribeth.offered_signature / companion_regill | commander-gender |
| jerribeth.counterfeit_guest / maker | commander-gender |
| jerribeth.counterfeit_guest / square | commander-gender |
| jerribeth.counterfeit_guest / scout_known | embedded-commander-speech |
| jerribeth.counterfeit_audience / challenge | commander-gender |
| jerribeth.counterfeit_audience / leverage.reply.1 | commander-gender |
| jerribeth.counterfeit_audience / departure.reply.1 | commander-gender |
| jerribeth.counterfeit_audience / raid_dismissed | commander-gender |
| jerribeth.counterfeit_spoil / object | commander-gender |

The required project-wide zero-hard gate therefore remains **unsatisfied** pending the Claude/shared owner repair. The completed Mielarah and contract checks do not waive it.

## PROPOSE

None. No unrequested route redesign implemented.

## RISKS

- Claude voice review and the independent rubric audit remain pending; no score is self-certified.
- The civilian protection arrangement is authored scene behavior using existing logistics, not a new ongoing casualty or enforcement subsystem.
- Shared attack-witness and historical-reference gate defects remain outside this patch.

Temporary gate directory, build outputs, verifier artifacts and generated Python caches were removed before handoff. Only the scoped source, route tests, voice-review queue and this implementation report remain.

# R4-soana local residue

Base reviewed: `5dd587bd3277fa985e4293601290f59ad8dfcd6e`.
Uncommitted, as required by the final task instruction.

## CHANGES

`storylines/soana_round3.py`:

| Finding | Status and evidence |
| --- | --- |
| soana:D08 | Done: append `dead_r3_known/home/separated` and matching letter nodes. Existing guardian answers retain indices and targets but forbid histories now handled by appended answers. Separation precedes home, then southern reply; unknown history retains the original. |
| soana:D09 | Done: `reply/send_proposal` ends with the outbound relay. Retire its immediate-reply answer by the existing closed flag; append the dispatch completion. New `proposal_reply` requires that stored dispatch receipt and the existing correspondence interval, 168 hours. Corven's original proposal terms and acceptance/refusal effects are retained. |
| soana:D10 | Done: same repair in `reply.returned`, with `proposal_reply.returned` retaining the existing earned physical-return/contact guards. |
| soana:D11, soana:D12 | Done: restrict adjacent-quotation merging to Soana's monologue variants. Both `share_r3_proposal` twins and `family_proposal` preserve Corven, Soana and their son's separate speech and attribution. |
| soana:D13 | Done: `quiet_r3_cleft` states that she stayed to watch the deer. |
| soana:D14 | Done: `quiet_r3_flood` names Varn's kindling inspection. |
| soana:D15 | Done: its reply acknowledges the single actual camp remark. |
| soana:D16 | Done: `quiet_r3_desire` makes the thought-versus-action tease a complete sentence. |
| soana:D17 | No change needed: S3 explicitly withdraws this finding; `quiet_r3_desire[1]` already promises another visit before `quiet_r3_kiss` teases the return. |
| soana:D18 | Done: `quiet_r3_quiet` identifies the tools rather than an unbound plural. |
| soana:D19 | Done: `quiet_r3_start` states what she will renew and when. |
| soana:D20 | Done: `quiet_r3_harvest` identifies her two-word admission. |
| soana:D21 | Done: the harvest account states that Mava stopped after Soana's question. |
| soana:D22 | Done: the account explicitly names the untouched warning. |
| soana:D23 | Done: `quiet_r3_meret` names the report Soana will ask for upon Mervika's return. |
| soana:D24 | Done: dead-guardian variants state the forest's continuing danger in Soana's speech. |
| soana:D25 | Done: `quiet_r3_commit` answers the selected commitment; no absent attempt to silence her. |
| soana:D26 | Done: `quiet_r3_open` jokes about her own simple request. |
| soana:D27 | Done: `quiet_r3_start` recognizes the evening visit; kiss narration follows the actual choice to leave before night ends without inventing a named hour. |
| soana:D28 | Done: `quiet_r3_courtship` names her scoldings and the Commander's promises. |
| soana:D29 | Done: invitation to kiss replaces rebuke for an absent boast. |
| soana:D30 | Done: all `saved_r3_known/home/separated` versions retain her complaint without rebuking a tree joke the player never made. |
| soana:D01, soana:D02, soana:D03, soana:D04 | Out of scope: R4 row holds partner-accountability decisions for contract/S6 ownership. Concealment, commitment conditions and Last Call arrangement unchanged. |
| soana:D05, soana:D06, soana:D07 | Out of scope: recurring luck consequences and their ending claims are held for contract/S6 ownership. No luck penalty or new cost implemented. |

`tests/test_soana_round3.py`: six regression tests cover a separate timed second reply, all four guardian histories (including home plus separation), both three-speaker homecoming hosts, every repaired conversational class, and zero new strict Soana player-text findings. Existing route traversal tests now include the new guardian histories.

`tests/SoanaPartnerTests.cs`: update the superseded immediate-reply expectation for D09/D10; verify actual runtime availability at dispatch, 167 hours and 168 hours, both settlement choices and prevention of replay after settlement.

`tools/departure_contracts.json`: classify only the two new Soana reply surfaces for D09/D10. They use the same existing `soana.present_now` body guard as the previous reply hosts; no departure or return contract is redesigned.

`tools/route_packs/plans/voice-review-pending.json`: append the eight touched/added scene hosts for Claude's voice pass. No Soana scene is voice-locked; no prose-pending entries are necessary. S1 has no Soana-owned section. Shared jobs, J01–J10 contract work and Claude rebuilds were not edited.

### Canon and voice evidence

Checked `/wrath/blueprints.zip` against `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`. These correspondence, family-return and romance events remain labelled authored additions; native Corven fate is not claimed as established by the game. No new echo or native rewrite was introduced.

| Scene(s) queued | Native enGB key | Want / on-page act / existing cost |
| --- | --- | --- |
| `soana.partner.homecoming`, `.returned` | `93318741-6358-4436-a7f0-3cf64580345d` (AfterQuest Cue_0012: marriage, children, her forest) | Wants husband and hunter; tells Corven herself; hears his bitter terms and can lose the lover who refuses. Quotation repair changes no terms. |
| `soana.partner.proposal_reply`, `.returned` | `93318741-6358-4436-a7f0-3cf64580345d` | Wants both; sends her own wanting and reads his answer, then catches the hunter's wrist; a seven-day relay and Corven's existing terms intervene before acceptance. |
| `soana.after_the_last_visitor` | `3fc3f600-a7d6-4999-969e-064eb42f721e` (AfterQuest Cue_0011: mead, bonfires, men and women, Orso) | Wants the hunter's mouth and company; pulls sleeve/belt, watches deer and keeps cart wheels out of the hollow; accepts inconvenient forest work and the existing concealed meeting away from home. |
| `soana.the_days_she_counted` | `93318741-6358-4436-a7f0-3cf64580345d` | Wants her forest defended and the hunter back; renews useful warnings, stops Mava's gathering, writes Corven and presses the hunter's hand to her cheek; Orso stays dead, harvested food and family history retain their consequences. |
| `soana.before_the_far_road` | `3fc3f600-a7d6-4999-969e-064eb42f721e` | Wants an evening and kisses before the final fighting; puts tools away, takes the hunter's hand and draws them to kiss; the chosen departure ends the visit, and existing lover/partner gates remain. |
| `soana.when_the_road_returns` | `93318741-6358-4436-a7f0-3cf64580345d` | Wants living trees and her complaint heard; bends the crooked sapling and scolds it; two saplings remain dead and the voice already spent is not refunded. |

## CLASS SWEEP

Checked all Soana `_r3_` variants produced by `histories`, `concealed` and `family`, including nested quiet/history clones and the returned twins. Preserved distinct quotation boundaries throughout the transformation; corrected dangling subjects, missing actions, invented repetition, absent jokes and unsupported departure times. D17's real incoming choice remains intact. Guardian history selection covers both its old dead-bear and pulverized-medallion answers and the subsequent letters.

Scene/node/relationship IDs and existing choice positions are retained. New replies, history nodes and answers append. Existing source files use LF; their line-ending style is preserved. No other route, shared storyline or explicit brief is changed.

## GATE

Commands used `PYTHONHASHSEED=0`, UTF-8 mode, `/wrath` game data and the four parent-binding files from `build-expansion.ps1`. Tests read the newly generated export. All dotnet build outputs and verifier artifacts were redirected to a system temporary directory.

| Command / check | Result |
| --- | --- |
| `python expansion.py` | Success; 4056 scenes. Regenerated after the final prose correction. |
| Targeted Soana Python tests, savecompat and UTF-8 tests | PASS: 33 tests on the final export. |
| `python tools/savecompat.py` | 0 hard failures. |
| `python tools/payoff_lint.py --strict` | 42 routes; 0 hard failures. |
| `python tools/departure_lint.py --strict` | 43 women; 0 hard failures after classifying the two new reply hosts. |
| `python tools/voice_lock_lint.py --strict` | 576 locked scenes; 0 changed, 0 missing/ambiguous. |
| `python tools/slot_brief_lint.py --strict --known-rebuilds` | 320 briefs; 0 hard, 315 known rebuilds, 168 warnings. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | Attempt and serial retry terminated with exit 143 and no assertion report. Not a pass. |
| `python tools/rrt_verify.py --strict` (once) | Exit 1: 85 player-text hard findings, no other hard categories. Fixed all 72 Soana adjacent-quotation flags by merging only monologues. Remaining 13 are existing locked Jerribeth findings, independently reproduced from the original export; see ESCALATE. The final export's exact strict player-text checker is checked separately. Global 0-hard acceptance is not claimed. |
| Final exported `player_text_lint.check` + `player_text_baseline.new_findings`; `text_structure_lint.check` | 13 hard findings, all unchanged locked Jerribeth entries; 0 Soana hard findings. Text structure: 0 hard. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json` | Full attempt and retry terminated with exit 143; no completed full-suite result. The initial CLI output-path override also exposed dotnet's default launch-path lookup; environment output paths fixed the launch without creating repo build folders. |
| C# `--suites=SoanaPartnerTests` | PASS: 1311 assertions, including both real 167/168-hour reply boundaries and no replay. Updated its superseded immediate-reply assertion. |
| C# six Soana suites | PASS: 81,600,444 assertions in 6 selected suites. Uses global `Rules.Validate` plus opening, continuation, later progression, late campaign, partner and Trickster suites; no `Page has no selectable answers` failure. |

The generated `development/Story.json` was restored byte-for-byte to its starting version after checks; it is not part of the change. Temporary artifacts were removed. No harness, game or full build script was run; no commit made.

## ESCALATE

- soana:D01–D07 remain with the contract/S6 decision identified in the assigned R4 row.
- J10's shared inventory classification of Soana's 127 payoff surfaces (approved ruling 42) is outside this route-local residue task.
- The global strict gate cannot reach zero without Claude-owned Jerribeth repairs. All 13 below are also present in the starting export; every affected scene is voice-locked. No other-route prose, lint baseline or exceptions were changed:

| Locked scene / node | Existing strict code |
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

- Coordinator must complete the full Python/C# checks that were terminated by the execution environment; no reason accompanied exit 143.

## PROPOSE

None. No extra mechanics, costs, commitment requirements or reconciliation rules implemented.

## RISKS

Claude voice review and the coordinator's independent rubric audit remain outstanding; no scores are self-certified. The second relay intentionally makes the existing proposal answer unavailable until the actual return interval. Global verification is blocked by the 13 existing locked Jerribeth findings, and full Python/C# suites did not finish. No refusals.

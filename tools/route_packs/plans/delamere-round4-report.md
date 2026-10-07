# Delamere R4 local residue

## CHANGES

Base commit: `5dd587bd`. No commit. Edits are limited to this route's producers, its regression test, and its review/report metadata. Existing scene IDs, node IDs and choices retain their positions; `not_like[1]` and the final `confessed_here` node are appended. All three edited Python producers retain CRLF with zero bare LF. No required beat was refused.

| Finding | Status | File and evidence |
| --- | --- | --- |
| delamere:D01 | Done | `storylines/delamere_trickster.py`: `crypt.stag/not_grave` demands a wrist-pulse examination instead of asserting that the dead never hunger. |
| delamere:D02 | Done | Same producer: `crypt.stag_alone/not_grave` observes her beating heart and warm red blood, with no general undead rule. |
| delamere:D03 | Done | The generated `crypt.stag_late/not_grave` receives the same corrected personal observations. |
| delamere:D04 | Done | Same producer: `drezen.stag/not_grave` describes her heartbeat and heaving stomach; her disgust for smoke, sewage and city crowds remains. |
| delamere:D05 | Done | Same producer: `react.kyado_woken/start` reports the pulse and warm skin Kyado actually examined. The invented scholarly confirmation is removed. |
| delamere:D06 | Done | `storylines/delamere_fire.py`: `woken.white_stag/opened` observes breath, pulse, warm red blood and her own dream. Her uncertainty and lost healing gift remain. |
| delamere:D07 | Done | The generated `woken.feasting_table/white_stag.opened` receives that same producer correction. |
| delamere:D08 | Done | `storylines/delamere_woods.py`: `woken.day_owed/again` retains the original first-hunt recall. She pulls the Commander to her and kisses them, then names her dawn duty to the threatened Sarkorian clearings and families. Affection no longer outweighs her country. |
| delamere:D09 | Done | Same scene, `again_new`: the alternate first-hunt recall remains distinct; the same desire/action/duty beat replaces the same Sarkoris devaluation. |
| delamere:D10 | Out of scope | `crypt.stag_alone` area/access repair belongs to shared owners; no local gate added. |
| delamere:D11 | Out of scope | `crypt.stag_late` area/access repair belongs to shared owners. |
| delamere:D12 | Out of scope | `woods.second_hunt_page` area/access repair belongs to shared owners. |
| delamere:D13 | Out of scope | `woods.second_hunt_late` area/access repair belongs to shared owners. |
| delamere:D14 | Done | `storylines/delamere_woods.py`: `woken.first_meat/did` identifies swelling and the existing bandage, limits the lesson to short walking steps, and stops handling the leg when the Commander flinches. No completed bone knitting, new treatment or timer. |
| delamere:D15 | Done | Generated `woken.count/first_meat.did` receives the still-injured producer text and active foot-placement follow-through. |
| delamere:D16 | Done | Generated `woken.count_late/first_meat.did` receives the same correction; late chapter does not age the fresh injury. |
| delamere:D17 | Done | `storylines/delamere_fire.py`: `not_like[0]` still postpones. Appended `[1]` immediately admits the horn and religious lie, sets existing `delamere.trickster.confessed`, and reaches appended `confessed_here`. She tears her hand away, puts her bow between them, rejects Haddo's intervention and insists the Commander stop speaking for Erastil. Existing scene completion remains intact. `tests/test_DelamereRound4.py` replays truth/postponement through all three hunts and checks committed/refused ending eligibility. |
| delamere:D18 | Out of scope | `discovery.pilgrim` Chapter 5 temple/crypt runtime acceptance belongs to shared/native acceptance owners, including J10. |
| delamere:K01 | Local causes corrected | All seven cited undead-physiology surfaces pass a fresh-export inspection. This is implementation evidence, not an independent score or cap-waiver claim. |

`tools/route_packs/plans/voice-review-pending.json` records every re-voiced generated scene for Claude. No affected scene is voice-locked; no prose-pending placeholder was required.

### Native evidence and voice accounting

Verified directly against `/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`. Native Delamere unit `433b2850e2f5a1f4e82a6969bf43af66` has `Visual.BloodType=BlackUndead`. Septimus's enGB `f66e3deb-ce99-4ef0-a018-dd9c2191567c` describes undead hunger; vampire feeding is described by `2592898a-f8c5-475b-b752-56522ce60861`. Neither supports the removed universal claims.

Each row names a native enGB voice anchor. The living return and these observations/reactions are authored additions within the existing Trickster vow-and-horn event; no new restoration mechanism or lore rule is introduced.

| Re-voiced scene | Native enGB key | Want / on-page act / retained cost or consequence |
| --- | --- | --- |
| `delamere.trickster.crypt.stag` | `dd5efeff-f2e7-4dbb-ab53-e5f37a91f16f` | Wants her restored body recognized and food; commands examination and bandage/bread; the arrow extraction and wounded Commander remain. |
| `delamere.trickster.crypt.stag_alone` | `dd5efeff-f2e7-4dbb-ab53-e5f37a91f16f` | Wants control of the waking encounter; leans close and orders the Commander flat; painful extraction remains. |
| `delamere.trickster.crypt.stag_late` | `dd5efeff-f2e7-4dbb-ab53-e5f37a91f16f` | Same personal examination and extraction, with the late delivery intact. |
| `delamere.trickster.drezen.stag` | `bfa99dd8-cba4-4135-bd5e-0941a8364c6a` | Wants bread and clean air; curls her lip and orders extraction; renewed life does not reconcile her with the city. |
| `delamere.trickster.react.kyado_woken` | `bfa99dd8-cba4-4135-bd5e-0941a8364c6a` | Wants useful service; makes Kyado feel her pulse and fetch bread, takes his broom; his standing as prior remains unsettled. |
| `delamere.trickster.woken.white_stag` | `72acddf8-ec57-484f-8533-ec81815dc2db` | Wants the stag/vow understood; shows her hand and touches the arrow site; divine healing remains lost and its cause uncertain. |
| `delamere.trickster.woken.feasting_table` | `72acddf8-ec57-484f-8533-ec81815dc2db` | Same physical demonstration and lost gift in the folded host. |
| `delamere.trickster.woken.day_owed` | `5ca0f649-a303-4a1a-bcd4-bed0c87c0a8b` | Wants her lover and another hunt; pulls them close and kisses them; she leaves at dawn to defend clearings and families. Both recalls preserved. |
| `delamere.trickster.woken.first_meat` | `72acddf8-ec57-484f-8533-ec81815dc2db` | Wants a quieter hunter; handles the injured leg, sets the foot down and watches steps; wound and demon risk remain. |
| `delamere.trickster.woken.count` | `72acddf8-ec57-484f-8533-ec81815dc2db` | Same hunt lesson and fresh wound in the ordinary fold. |
| `delamere.trickster.woken.count_late` | `72acddf8-ec57-484f-8533-ec81815dc2db` | Same lesson and fresh wound in the late fold. |
| `delamere.trickster.woken.red_blood` | `3ce42128-b345-469e-a22b-476d0fb66577` | Wants living appetite and touch; presses the Commander's hand to her pulse; uncertainty about Erastil remains. |
| `delamere.trickster.woken.old_deadeye` | `9c9bac92-00ad-4d73-9c51-3d6dfb4ad037` | Wants truth about the religious lie; withdraws touch, interposes her bow and silences the priest; the Commander loses her grateful certainty, and confession remains required history for subsequent intimacy. |

## CLASS SWEEP

- Physiology: checked all four waking variants, Kyado's reaction, standalone/folded white-stag conversation, and nearby `woken.red_blood/wants`. The latter also claimed the dead lack wanting; it now describes her own experience in the tomb. Fresh-export inspection confirms all eleven checked surfaces lack the false diagnostic/recovery statements.
- Sarkoris valuation: checked `again` and `again_new`; both preserve their different saved-history recalls and prioritize native rural duties alongside affection.
- Injury chronology: checked standalone first meat and both count folds, their preceding gait lesson, immediate follow-through, later crooked-leg history, and the existing priest-healing closure. No new healing act or recovery gate.
- Religious truth: checked both chapel answers, the existing confession receipt, all three hunts' ordinary/chapel-oath dispatch, refusal, and ending consumers. Immediate confession avoids a second confession; postponement still reaches the existing confrontation.
- Save/presence discipline: no path, temple/Book-lock, deliberate-kill, paid-page, commitment, return or sacrifice predicates changed. No echo slot or foresight explanation added. No locked or shared storyline edited.

## GATE

All generated exports, verifier reports and C# build outputs run in a system-temp copy. Environment: `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONUTF8=1`, game evidence `/wrath`, and the four parent-binding manifests from `build-expansion.ps1`, joined with the platform path separator. Tests use the fresh export through `RRT_TEST_STORY`.

Fresh export SHA-256: `6cac783922b3681b8e8a1fb4f564ea85f19ad1785e23f60cc597b235a7d5c53b`.

- `python expansion.py`: PASS, exit 0; 4,054 scenes. Generator labels it `INCOMPLETE DEVELOPMENT EXPORT`; no release-completeness claim.
- `python tools/savecompat.py`: PASS, 0 hard failures.
- `python tools/payoff_lint.py --strict`: PASS, 42 routes, 0 hard failures; existing review advisories remain.
- `python tools/departure_lint.py --strict`: PASS, 43 women, 0 hard failures.
- `python tools/voice_lock_lint.py --strict`: PASS, 576 locks, 0 changed, 0 missing/ambiguous.
- `python tools/slot_brief_lint.py --strict --known-rebuilds`: PASS, 320 briefs, 0 hard, 315 known rebuild findings, 168 warnings; no brief edited.
- `python -m unittest tests.test_DelamerePolish tests.test_DelamereRound2 tests.test_DelamereRound4 -q`: 17 tests in 19.501s, 16 PASS, 1 unchanged failure at `test_DelamereRound2.py:102` (late-epilogue brief mismatch detailed below). The new immediate/postponed confession regression passes, including positive sacrifice-loss and negative living-after-sacrifice checks. Its initial setup errors were corrected to include the earned return and recompute derived ending receipts.
- `python -m unittest tests.test_utf8_io -q`: PASS, 1 test in 5.670s.
- `python -m unittest discover -s tests -p 'test_*.py' -q`: initial exit 143 without summary; retry received SIGTERM (return -15) at 18.9s without summary. NOT PASS; no completed discovery receipt.
- `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json`: initial exit 143; retry exit 143 at 30.2s after early Q8/channel/earned-return checks. NOT PASS; no full Rules/progression summary. No "Page has no selectable answers" was printed before interruption; this does not establish the universal check passed.
- `python tools/rrt_verify.py --strict --game /wrath --json <temp>/verify.json --text <temp>/verify.txt`: FAIL, exit 1, 1,025.5s; **13 hard diagnostics**, all in unchanged Jerribeth player text (locations below). Delamere has no player-text hard diagnostic. Structural validation, shipped text structure, save compatibility, bindings, native-return safety, earned presence, timeline/allocation/obligation contracts, intimacy, memory and transaction checks report 0 hard. No lint changed or exception added.
- CRLF-aware `git diff --check`: PASS. Byte inspection: all three edited producers have zero bare LF.

## ESCALATE

- D10–D13 shared area/access work and D18 native Chapter 5 acceptance are excluded by the assigned row. J10/shared owners must supply runtime evidence.
- Approved ruling 42/J06 owns repeated Delamere postponement timestamp refresh. This job leaves the existing clock intact.
- Existing `tests/test_DelamereRound2.py:102` expects the late epilogue brief's `last_line` (the moved-stake conditional aftermath) within the explicit slot text. The untouched slot instead ends with drawing the hide over both lovers and leading the Commander home at dawn. Slot support/insertion inventory belongs to J10 under ruling 42; this local job does not rewrite its brief or weaken its test.
- Existing payoff-lint advisory about the effect-free late answer's readiness/receipt remains under the shared contract work; no unrequested yes requirement added.
- Discovery and Rules/progression both interrupted on their original attempts and their process-status-recorded retries. Cause not established. S2/coordinator must supply uninterrupted receipts, particularly the universal selectable-answer check. No other route or shared test assertion is changed to conceal missing acceptance.

Strict verifier's 13 hard diagnostics are outside this route's scope. They are lint diagnostics requiring Jerribeth/Claude and coordinator review, not a claim that every matched pronoun actually refers to the Commander. No affected text was edited.

| Scene/node | Diagnostic | Owner |
| --- | --- | --- |
| `jerribeth.farewell/traitor_fed` | commander-gender | Jerribeth/Claude |
| `jerribeth.farewell/discovery_distant` | speaker-attribution-review | Jerribeth/Claude |
| `jerribeth.ending_together/catalogue` | commander-gender | Jerribeth/Claude |
| `jerribeth.ending_ascended/catalogue` | commander-gender | Jerribeth/Claude |
| `jerribeth.offered_signature/companion_regill` | commander-gender | Jerribeth/Claude |
| `jerribeth.counterfeit_guest/maker` | commander-gender | Jerribeth/Claude |
| `jerribeth.counterfeit_guest/square` | commander-gender | Jerribeth/Claude |
| `jerribeth.counterfeit_guest/scout_known` | embedded-commander-speech | Jerribeth/Claude |
| `jerribeth.counterfeit_audience/challenge` | commander-gender | Jerribeth/Claude |
| `jerribeth.counterfeit_audience/leverage.reply.1` | commander-gender | Jerribeth/Claude |
| `jerribeth.counterfeit_audience/departure.reply.1` | commander-gender | Jerribeth/Claude |
| `jerribeth.counterfeit_audience/raid_dismissed` | commander-gender | Jerribeth/Claude |
| `jerribeth.counterfeit_spoil/object` | commander-gender | Jerribeth/Claude |

## PROPOSE

None. No mechanics, costs, gates or reconciliation changes proposed or implemented beyond the required appended truth choice and existing receipt.

## RISKS

This implements the assigned local residues; it does not certify independent scores of 91 or higher. Claude voice review remains queued. Shared native/access acceptance, known rebuild briefs, the unchanged late-epilogue test mismatch, interrupted discovery/Rules and the strict verifier's Jerribeth diagnostics prevent an unconditional whole-route/release acceptance claim. Temporary exports, reports, logs, checkout/build outputs and helper scripts were removed before delivery. No build-expansion.ps1, harness, game launch, install or commit.

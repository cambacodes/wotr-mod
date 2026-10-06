# Aranka round 2 implementation handoff

## CHANGES

All situations below are authored extensions of her Desnan vocation and the existing paid Trickster disturbance, not recovered Owlcat romance. Canon was checked in `/wrath/blueprints.zip` and `enGB.json`: Starward Gaze's divine origin (`f21279d1`), the competitive contest (`dd66b8ab`), Thall's glances/voice/refusal (`13cbf1a6`, `2c84efa6`, `a939f88e`), his island unit (`8fb65bd7`), his Fane death etude (`49c99adb`), and native Commander stay/leave (`84e00414`, `7fde8724`). Installed parent localization confirms possible Reverie love, but does not establish a present contact or the missing ending binding metadata.

| File / finding | Implementation and consequence |
|---|---|
| `storylines/aranka_trickster.py`, P1:3–8 | Every fresh/failure letter delivery now brings its writer bodily back on the returning wagon before `answered` enables her copies. Ch3/Ch5 clocks, all original prices, and the separate moral-repair deed remain unchanged. |
| Same, P1:9 and set-piece venue evidence E | Touring confrontation names its actual crate/wagon seat, including the fitted late twins. The yard's carter replaces the unsupported identification of the blacksmith anchor as Wilcer Garms. |
| Same, turning-point/debt sheet | All four duet openings, both contest alternatives, pay the spoken apology in the existing sing answer. Aranka accepts it before performing, enforces her own billing, and asks for the next duet. The existing terminal answer promises a road itinerary if the Commander leaves, setting up the road reunion without a new gate. The sacred hymn receives arrangement credit. |
| Same, registered set pieces 3–4 / ARA-02–03 | Her public solo question and spoken yes keep their original choices, receipts and refusals. Eight state-free roof slots bridge the threshold to the original morning. Morning keeps her noise fine and adds a choice to object to the identifying verse; she answers with her own less identifying, still bawdy version. Both morning exits produce the same existing `night_kept` receipt. |
| Same, P1:10 | Woljif recalls her actual return from the ford, which is true for both long and short courtships. His existing contact and loss guards remain. |
| Same, F1:1 / set piece 6 / ARA-04 | The single-season reunion reads verified native stay/leave etudes. Staying keeps Drezen's desk; leaving uses the promised itinerary, an inn, luggage and the road. Location-specific morning paragraphs surround the neutral reunion slot. The saved `end`/Continue exit remains effect-free. Aranka's existing Last Call record now shows a completed tour and bodily return, through the route's existing record accessor, without editing shared source. |
| Same and continuation, P1:12 | Her non-lover clarification remains. Endings/coda retain Thall's place among her songs and add remembrance only under the verified native death etude. Unknown whereabouts never become an invented death or return. His living reply is prepared but unregistered; see ESCALATE. |
| `storylines/aranka_continuation.py`, inherited heat inventory / P1:11 | Rehearsal, bad correction, successful performance, kiss-only and quiet evenings remain different situations. Removed scripted Commander interjections across the full class; tightened dream/compass greeting, rehearsal desire and authorship confrontation. Established lovers' night now runs initiation → slot → original `night` aftermath/receipt. Hollow acceptance runs through its own slot; deferral bypasses it. Copies/credits, Neris's correction without identification, Sella's lost solo and all trial outcomes remain. The 48-hour goodbye says “Today.” |
| `tools/route_packs/plans/aranka-{setpieces,tp}.md` | Copied the binding planning sheets unchanged from their specified refs. This report records actual implementation and supersedes their planning-only status and the TP sheet's old device synonym. |
| `tools/route_packs/explicit_slots/aranka/*.json` | Copied all 11 prescribed briefs. Eight roof nodes, two inherited island nodes and one reunion paragraph have exact scene-specific slot IDs and the briefs' exact last-line bridges. No explicit prose was generated. |
| `tools/route_packs/turning_points.json` | Registered only Aranka's exact atlas row: `she_pursues`, market busking stage with exclusive supply-yard fallback, solo answer → self-paid fine → chosen season. No other route's row imported or changed. |
| `tests/ArankaTricksterTests.cs` | The existing sibling-equivalence check now normalizes only the required full `<scene>.explicit.1` address. All other node IDs, destinations and effects retain their original comparison. This fixes the focused test's obsolete identical-slot-ID assumption. |
| `tests/test_aranka_round2.py` | Nine focused cases cover slot count/bridges, state-free insertions, original acceptance/closure indices and receipts, bodily deliveries, apology variants, night/kiss/quiet and deferral, native reunion setting, and the unregistered living Thall contact. |

## CLASS SWEEP

- Six delivery scenes, including known/unknown responses and both late twins; all market/yard placements.
- Four duet openings × contest winner/non-winner × venue/chapter, both billing counters, moral deed/refusal/defer.
- Eight roof threshold/morning pairs, direct yes/second yes/postponement/stage/hard refusal; no new intimacy receipt or price.
- Entire inherited continuation's scripted Commander speech and touch/reassurance class, all duplicated musical-trial endings, quiet/kiss/night, private/both/road/defer, immediate/deferred copying plans.
- Five Trickster ending pages, native stay/leave/unspecified reunion, sacrifice forbid/earned-return override, coda, Thall alive/dead/unknown evidence boundaries.
- Against HEAD's route modules: original scene order, 265 node identities, all original answer indices/effects and 118 terminal exits preserved. Original files retain CRLF. `git -c core.whitespace=cr-at-eol diff --check` passes.

## GATE

Export and all logs/build artifacts use system temporary storage; `development/Story.json` is not edited. The user's last gate list supersedes the earlier ban on broad Python/RulesTests gates; the last no-commit instruction supersedes the earlier commit instruction.

Commands used `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`, the build script's four parent-binding manifests, and `/wrath` game data. `RRT_STORY_OUTPUT`/`RRT_TEST_STORY` selected `/tmp/rrt-aranka-r2/Story.json`; `RRT_TEST_BUILD_ROOT` kept .NET outputs in the same disposable directory. The path substitution is necessary to obey the prohibition on edits to `development/**`.

| Command | Final result |
|---|---|
| `python expansion.py` | Passed; 3,755 scenes, exported outside the repo. |
| `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io tests.test_aranka_round2 -q` | Passed; 21 tests. The initial missing encoding argument in the new test was fixed. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | Incomplete: two attempts terminated with exit 143, without diagnostic output or a test count. |
| `python tools/payoff_lint.py --strict --story <temporary export>` | Passed; 42 routes, 0 hard failures. Shared REVIEW residuals remain. |
| `python tools/departure_lint.py --strict --story <temporary export>` | Passed; 43 women, 0 hard failures. Unregistered Thall proposal is excluded. |
| `python tools/rrt_verify.py --strict --story <temporary export> --game /wrath` | Passed; **0 hard failures**, 0 shipped structural errors; runtime 585.6 seconds. 5,269 player-text REVIEW diagnostics remain across the integrated payload. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- <temporary export>` | Incomplete: the final broad run terminated with exit 143 after its initial engine checks. The preliminary textless-reunion validation failure was fixed. |
| Same .NET command with `--suites ArankaTricksterTests,ArankaContinuationTests` | The first focused run exposed the obsolete sibling slot-ID comparison, now corrected. Subsequent attempts, including `--no-restore`, terminated with exit 143 before completion. A final isolated retry after the verifier finished did the same; no managed pass is claimed. |
| Source graph/save-exit comparison; CRLF check; `git -c core.whitespace=cr-at-eol diff --check` | Passed; 265 original nodes and 118 original terminal exits preserved, no original answer effect/index change. |

## ESCALATE

1. **P1:1–2 / eng3 L:** `tools/payoff_contracts.json`, `storylines/lastcall_partners.py` and the shared Ledger wiring still make credited/denied letters or touring posters callable without `duet_sung`. The Ledger still calls a completed song “unfinished.” The route now pays the duet and explicitly promises the next performance; the coordinator must require that receipt on every callable alternative and distinguish an invitation from the continuing performance in Aranka's Ledger/call entries. No new debt, return, price or romance threshold is proposed. These shared sources/registries are outside the allowed edits.
2. **F1:2–5 / eng3 parent residual:** verified parent-ending binding registration is still needed for Nerosyan Cue0001 `b6cf71efea374f08ba1c41fb6ff44cf5`, closed-couple Cue0004 `1df04d757f4a4c0db1c6327202ab839b` / Cue0006 `0f00abae3ff646a7a7120c960e19354e`, and returned-sacrifice Cue0010 `12b61bb6201d40a8866ab60701dd4669`. Preserve off-Trickster originals, closure and unreturned grief. Localization text alone does not verify the runtime page/sequence/condition metadata; no invented binding was registered.
3. **P1:12 living response:** `aranka-thall-contact.py` contains the prepared native-unit/contact-gated reply. It is not imported or registered. The departure lint rejects any new route scene absent its shared inventory (`unclassified presence surface`); activating this reply needs the corresponding Aranka presence classification in `tools/departure_contracts.json`. The rejected registration was removed before final export.
4. **ARA-01 shared courier:** no supplied, implemented Missing Company courier observation exists in this route's inputs. The identifying-song correction must consume the coordinator's actual shared evidence; no courier, culprit, fabricated quest or independent gate was invented.
5. **Reverie partner discovery/stance:** parent localization proves a possible inherited shared love, not a fresh Trickster acquisition or present waking/dream encounter. Aranka now distinguishes the private dream tune and owns the future conversation. Actual discovery, confrontation, all three stance answers and Reverie's own decision need verified parent contact/access and current bond wiring. No teleportation, silent breakup, automatic endorsement or stance flag from an absent partner was implemented.

6. **Gate completion:** the coordinator must rerun full Python discovery and the full/focused C# rules gates in its validation environment. These processes terminated with exit 143; their empty/incomplete logs do not establish a cause or a pass. The strict verifier and quick Python checks completed successfully.

## PROPOSE

None beyond the task's requested, explicitly escalated work. No blackmail layer, extra fee, attraction condition, reconciliation redesign or helper-dependent solo was added.

## RISKS

The broad Python and managed gates are incomplete; the corrected managed test has not received a completed runtime confirmation. The shared Last Call debt and inherited parent-ending contradictions remain real audit residuals. This implementation does not claim the route has reached the independent 91+ bar. Slot defaults are playable heated cuts; final user-supplied insertions still require continuity review. No game, harness, installation or packaging build was run. No commit was made.

# Yaniel polish round 3

No commit. Source changes stay in Yaniel's route modules and tests. Generated `development/Story.json` was used for validation and restored afterward.

## CHANGES

Finding numbers below follow the order of `yanielr2.json`'s defects array, starting at 1.

| Cap / defect | Status | File and correction |
|---|---|---|
| BEL cap; 1, Last Call's unearned Threshold success / oath provenance | fixed | `storylines/yaniel_radiance.py`: the existing paragraph now recalls only the accepted Iz account. Appended exclusive Fane and pre-Iz wall provenance paragraphs. No sword possession or Threshold carriage is inferred from `oath_stands`. |
| 2, Last Call assumes Fane acquisition | fixed | `storylines/yaniel_radiance.py`: acquisition-neutral call narration for both histories. Also corrected its sibling last-cart claim. |
| 3, Ledger assumes an unplayed trade and Fane acquisition | fixed | `storylines/yaniel_radiance.py`: initial debt text has no trade recollection; separate Fane/wall acquisition lines, and trade/vigil lines selected only by their actual receipts. Updated the matching journal description as well. |
| 4, missing holy-custody sword callbacks | fixed | `storylines/yaniel_trickster.py`: the existing authored Iz report records `iz_song_reported`. `storylines/yaniel_radiance.py`: separate callbacks for her report, custody acquired after Iz, and the Commander's native song receipt. The original paragraph remains at its saved index; the shared contract still adds its native-song requirement. |
| 5, `epilogue.together` erases `husk_told` | fixed | `storylines/yaniel_trickster.py`: secrecy concerns campfire stories, allowing the actual private disclosure to Yaniel. Shared packed/worn and appended pocketed variants corrected. |
| 6, `epilogue.commit` erases `husk_told` | fixed | Same class correction. |
| 7, `epilogue.broken` erases `husk_told` | fixed | Same correction, independent of oath failure. |
| 8, `epilogue.unasked` erases `husk_told` | fixed | Same correction, independent of courtship. |
| 9, `epilogue.unsettled` erases `husk_told` | fixed | Same correction, independent of verdict completion. |
| 10, wall recollection spoils the refugee's confirmation | fixed | `storylines/yaniel_trickster.py`: she held the gate while the final carts fled; she does not claim to know they escaped. |
| 11, `late.wall` Minagho gate | escalated | Shared presence pass adds `crossroute.minagho.unavailable`; route source has no such gate. |
| 12, `ch5.found/stay` choices 2 and 3 | escalated | Shared presence pass adds Minagho's current-availability prohibition to both historical rescue choices. |
| 13, `beat.walls/one` choice 1 | escalated | Shared presence pass adds the Minagho prohibition to her recollection. |
| 14, `beat.walls/you` choice 2 | escalated | Shared presence pass adds the Minagho prohibition to reciprocal courtship. |
| 15, `react.sosiel_iron` | escalated | Shared presence pass adds Areelu's unavailability and five death/sacrifice prohibitions to Sosiel's historical recollection. |
| 16, `beat.areelu` scene and `areelu` choices 0 and 1 | escalated | Shared presence pass adds the captor-availability prohibitions. Removing them before that pass cannot fix the export. |
| 17, `beat.night/dream` choice 2 | escalated | Shared presence pass adds both captor prohibitions. |
| 18, `beat.raid` | escalated | Shared presence pass adds Seelah's current-availability prohibition to a remembered intervention. |
| 19, `beat.prayer` | escalated | Shared presence pass adds Minagho's prohibition to a captivity recollection. |
| 20, `beat.bout/fight` choice 1 and `dirty` continuation | escalated | Shared presence pass mistakes an invocation of Iomedae for participation and adds presence/closure gates. |
| 21, missing generated-history coverage | escalated; coverage extended | `tests/YanielTricksterTests.cs`: new exported Last Call, Ledger and secrecy assertions run before the existing coexistence assertion. `tests/test_yaniel_round2.py`: two new tests cover the receipt/selectors and all cuff positions across all seven relevant endings. The C# suite still fails on defects 11–20, preventing a complete successful historical-closure walk. |

Verified-fixed before editing: no complete defect listed in this audit had been resolved. The shared endings work did correct the corked-flask recovery paragraph, which was preserved. The original holy-custody paragraph had acquired custody/native-song/late-handover gates, but still missed the authored report history; that was a partial correction, not a resolved finding.

## CLASS SWEEP

- Checked all three two-iron variants, including their reuse on `distrusted` and `declined`, beyond the five named endings. No cuff-position selector was changed.
- Checked Last Call narration, its sword paragraphs, the Ledger entry and journal mirror for false acquisition, premature trade, or unearned Threshold proof.
- Checked Fane and late-wall acquisition, initial oath, actual trade, vigil recovery, holy custody before Iz, custody after Iz, native song, and sword-absent histories.
- Checked the wall/refugee sequence and the Last Call's sibling last-cart claim.
- Confirmed every named historical-reference gate in a fresh pre-edit export and in the shared presence generator. No unrelated live guest guard was weakened.
- Native evidence: `DeskariFight/Cue_0036.jbp` (`221a9592527d8b5498346c55549dd2be`) checks party-held +4 Holy Avenger or Bane Living, excluding the hub chest. Its localization describes Radiance's reaction to Deskari. `TrueYaniel/Cue_0021.jbp` (`7db270440f7e3954aabbd4ad295ed65b`) establishes Minagho's trophy captivity. The new report receipt records an existing authored encounter; no native lore or event was changed.
- The requested `tools/route_packs/voice_locks.json` is absent in this checkout. The registry found in `/work/wt/RRT-voicelock` contains an empty `locked` map; there were no local listed scene locks to apply. The existing niche explicit slot and brief were retained. No new intimate encounter or premature cut was authored.

## GATE

Commands used `PYTHONHASHSEED=0` for regeneration, final lint checks and tests. Regeneration also used `PYTHONUTF8=1`, `/wrath` as the game directory and the four parent-binding manifests named by `build-expansion.ps1`.

| Command | Result |
|---|---|
| `python expansion.py` | PASS: 3,848 scenes regenerated. |
| `python tools/savecompat.py` | PASS: 0 hard failures. |
| `python tools/payoff_lint.py --strict` | PASS: 42 routes, 0 hard failures. The static Yaniel REVIEW note remains in the shared contract registry; its claimed Threshold/Fane prose has been corrected. |
| `python tools/departure_lint.py --strict` | PASS: 43 women, 0 hard failures. |
| `python -m unittest tests.test_yaniel_round2 tests.test_utf8_io -q` | PASS: 11 tests. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | BLOCKED: workspace `/work/testguard.sh` terminated the full suite (exit 143). |
| `python tools/rrt_verify.py --strict` | PASS: 0 hard failures; one strict run, 880 seconds. Reports were written to system temp and removed after recording the result. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json` | BLOCKED: compiled successfully, then terminated by the same full-suite guard (exit 143). Build outputs were redirected outside the repo. |
| Focused C# run: `--suites=YanielTricksterTests,YanielRadianceTests` | FAIL: new callback assertions passed, then the existing assertion failed: `A Yaniel scene forbids a Minagho/Chivarro or Seelah route flag.` This is the exported shared-gate class escalated above. |
| Line-ending and diff checks | PASS: original CRLF/LF conventions preserved; `git -c core.whitespace=cr-at-eol diff --check` clean. |

## ESCALATE

1. Defects 11–20 require a change to the shared `storylines/crossroute_presence.py` pass / its historical-reference classification. That pass runs after Yaniel's route integration and regenerates the gates. It needs scoped exceptions for the exact scene/choice targets above, preserving actual participants' presence and Yaniel's own entry conditions. In `beat.areelu`, any current correspondence claim also needs a current-correspondent branch; historical answers must retain a selectable exit. These shared files were not edited.
2. The shared payoff registry retains a static Yaniel REVIEW description for the now-corrected Threshold/Fane callback. Updating that registry is outside the allow list.
3. The workspace's full-suite guard prevented completion of the two explicitly requested full test commands. It was not stopped or bypassed. The coordinator must run them in its permitted verification environment.

## PROPOSE

None. No new mechanics, romantic gates, costs, reconciliation conditions or route redesigns were implemented.

## RISKS

- The route does not meet the requested complete green-gate / 91+ readiness while defects 11–20 remain. No independent score is claimed.
- Existing saves that already passed the authored Iz report have no new `iz_song_reported` receipt. It is not retroactively fabricated from custody or the native song. Such saves can miss that new report callback.
- Full progression validation did not complete, so no claim is made that every page has a selectable answer in every history. The existing historical-reference gates remain a known obstruction.
- New choices were not added; no IDs, indices or legacy epilogue exit identity/mechanics changed. No build-expansion script, harness or game was run.

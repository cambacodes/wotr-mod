# Elyanka Camilary: round 3

All changed situations are authored Trickster additions. Native identity, history,
seal lore and non-Trickster content are unchanged. Native seal evidence:
`Elyanka_MainDialogue/Cue_0064`, `a393f21008a826b44b4585731a29d8dd`,
localization `937d13da-07ba-4985-8d02-2be0f9cec235`, verified in the game archive.
It already discloses the missing lesser seals; the letter therefore supplies a
warning about the Way's ambitions, not new operational intelligence.

## Audit disposition

| Finding | Disposition and source |
| --- | --- |
| COX cap / table Targona recollection | Fixed: `elyanka_hearse.py` requires current presence and appends a fallback for a historical return followed by loss. |
| INT / dismissed envoy's sacrifice | Verified-fixed in the merged source: `left_free_mourned` renders the distant Ustalav reaction without current presence. Updated `ElyankaTricksterTests.cs` to require that rendered ending; Python covers return and Last Call exclusions. |
| HOW / one-day precautions | Fixed: `door.hearse/plan` maintains lodging and the watch's deception until the summoned audience, including postponed audiences. |
| HOW / executor's fixed day and night | Fixed: `executor.haggle/why` complains about continued waiting without a fixed elapsed duration. |
| HOW / second offer's two days | Fixed: `commit.her_move/hair` dates deliberation from the supper; the lock can still be cut on the delivery morning. |
| BEL cap / horse panic | Fixed: the heavy glass door bangs beside the mares. Horse continuation is available independently of Daeran. Legacy choices, targets and receipts remain. |
| BEL / horse ending | Fixed in the common paragraph producer: glass rattling carries the fright forward; replacement mares are tried beside the door. |
| BEL / supposed Lastwall intelligence | Fixed: ideological intimacy remains; all three answers retain their identities and flags. Letter and player challenge describe what she actually revealed. |
| BEL / thin-cage confession | Fixed: she acknowledges her desire to close the churches, not an undisclosed weakness in the seals. |
| BEL / strengthened watch | Fixed: a knight investigates a warning; no exceptional security result is invented. |
| BEL / Way acquiescence after murder | Fixed: another armed envoy and continuing escort pressure replace permanent immunity. Her refusal to advance collection preserves her agenda. |
| INT / rites contradict inquiry | Fixed: the original unobserved rites account excludes every inquiry outcome; an appended paragraph shows rites continuing under the established witness and chaplain testimony. |

## Class sweep and boundaries

Checked both route modules for companion recollections, horse explanations,
minimum-delay claims, Tyrant disclosure/letter/reaction/ending, master outcomes,
and inquiry/rites paragraphs. Common horse prose serves all four existing ending
consumers; the changed rites variants serve the committed claim page. The
existing hearse explicit slot and brief remain connected to the morning.
No new mechanics, costs, prerequisites, return devices, echoes or reconciliation
conditions. Scene/node/relationship IDs, answer indices and legacy exit effects
remain intact; the new Targona fallback is appended. CRLF source bytes preserved.

`tools/route_packs/voice_locks.json` is absent in this checkout; no supplied lock
entries can be evaluated. Coordinator should verify against its current registry.

Validation results are recorded in the implementer's final report. No commit.

## Gate record

With `PYTHONHASHSEED=0`, UTF-8 mode, `/wrath` game data and the four parent
binding manifests from `build-expansion.ps1`, `python expansion.py` succeeded:
3,848 scenes. The generated export was redirected with `RRT_STORY_OUTPUT` to
system temp; every export consumer used that same fresh file.

- `python tools/savecompat.py --story <temp>/Story.json`: zero hard failures.
- `python -m unittest tests.test_elyanka_round2 -q`: 13 tests passed.
- `python -m unittest tests.test_utf8_io -q`: passed.
- `python tools/payoff_lint.py --strict --story <temp>/Story.json`: zero hard failures.
- `python tools/departure_lint.py --strict --story <temp>/Story.json`: zero hard failures.
- C# route selection `--suites=ElyankaTricksterTests --jobs=2`: 138 assertions passed.
  Compilation and execution used external intermediate/output directories.
- Requested unfiltered Python discovery and C# rules execution were terminated
  with exit 143 by the host test guard, which kills full suites in `RRT-r3-*`
  worktrees. Coordinator must run those gates in an authorized full-gate job.

The C# route fixtures also needed repairs to stale shared-ending paragraph
references, three collector variants, and the earned bottle-pillar history.
These checks retain the original consequences and now test the merged model.
The strict verifier result is recorded in the final report after it completes.
The plain strict invocation was interrupted after fifteen minutes of advisory
whole-game analysis; `--strict --gate-only` retains every strict check. Its first
completed run found one new Commander-gender diagnostic: the knight's "his
questions" appeared near "Commander." The text now names "the knight's questions"
explicitly, and the claim page has no such diagnostic. The final export and
strict gate are regenerated after that correction.

Final corrected-export gate: `rrt_verify.py --strict --gate-only` completed with
**0 hard failures**; shipped structural errors, save-compatibility errors and
player-text hard failures were all zero. Python route/UTF-8 checks passed all 14
tests again; C# route validation passed all 138 assertions again; payoff and
departure strict lints and save compatibility also passed again. Only the
unfiltered suites stopped by the host guard remain for coordinator validation.
All temporary exports, reports, inventories and build outputs were removed.

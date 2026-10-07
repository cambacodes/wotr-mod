# Iomedae round 3

Uncommitted, following the final task instruction. No independent score is claimed.

## CHANGES

Audit finding numbers below follow the order of `iomedaer2.json` defects.

| Finding / cap | Disposition | Evidence / change |
| --- | --- | --- |
| 1; premature-fade VOI/BEL cap | fixed | `storylines/iomedae_trickster.py`: retained `epilogue.after.explicit.1`, staged familiar armor removal and reunion on the bed after the paid ninth-year vigil. The slot retains `vigil_morning`; its brief specifies the initiating motion and user-filled act. No explicit act was written, no intimacy receipt added. |
| 2; mortal-appearance BEL cap | verified-fixed, anchor clarified | Current bridge narration already treats the mortal face as recognition and separately names Pharasma's liability. Added the native Summit's Worldwound exception to make the authorization explicit; the shape does not remove divinity. |
| 3; inert-witness BEL cap | fixed, shared presence limitation below | `iomedae_trickster.py`: appended presence-qualified Nocticula and Areelu objections, with Iomedae's answers. Both, either, or neither can speak; the original state/courtship branches follow. No witness earns or vetoes rescue/romance. |
| 4; Summit opening blocked by Nocticula closure | escalated | The final shared presence transformer adds `crossroute.nocticula.unavailable` to the native Summit scene despite its fixed native audience. Correcting that reader requires shared code outside the named route entries. |
| 5; Summit dream blocked by Nocticula closure | fixed | `storylines/iomedae_banner.py`: classify the private dream as `Kind=dream`; its references are historical, and no guest is physically present. Existing entry flags, delay and choices remain. |
| 6; eve dream blocked by Nocticula closure | fixed | The eve conversation recalls what Nocticula wanted at the Summit rather than claiming her current intent or presence. Banner eligibility, accountable Herald cruelty and the postponed personal exchange are preserved. |
| 7; banner continuations blocked by Nocticula closure | fixed | Clarified the two hall recollections as pre-ascent history. Guest reactions have their own branches and availability reads. Neither original plant continuation requires Nocticula romance availability. |
| 8; unearned first-white-dream recall | fixed | `iomedae_banner.py`: neutral opening plus appended first/returning white variants keyed to completed Summit dream or Herald-dream receipt. The late opening / Iz conversation can lead to the first variant. |
| 9; false bridge/empty flask on H1 | verified-fixed, sibling completed | The merged paragraph already requires `buried_alive` and uses in-world crossing wording. Split the remaining held-flask account between no banner and H1 with a carried banner; H1 states no crossing emptied it. |
| 10; unconditional Last Call banner | fixed | `iomedae_trickster.integrate_joint` reconciles only `iomedae.lastcall.page`: neutral opening, appended carried/no-banner accounts, unchanged legacy exit. Shared source files are untouched. |
| 11; Areelu falsely never saw the banner | fixed | Same route-owned coda hook: crossing/empty-flask history is independent of Areelu; her presence-qualified measurement says she did not witness the crossing inside the seam or hear its terms. |
| 12; public King's-table restoration / COX cap | verified-fixed | Shared merge requires `lastcall.public_return`, which forbids `buried_alive`; the concealed-return sibling uses `lastcall.bridge_return` and covers romantic and rescue-only bridges. |
| 13; public cathedral-steps restoration / COX cap | verified-fixed | Same shared reader partitions the cathedral account; the concealed account records departure before recognition and an empty coffin. |
| 14; bottled death carried after bridge / COX cap | verified-fixed | Mortal-cost paragraph requires `lastcall.bottled_held`, whose negative is `buried_alive`. The bridge sibling puts the death in Pharasma's book; Iomedae's own pages retain the final appointment and no appeal. |

Both epilogue briefs under `tools/route_packs/explicit_slots/iomedae/` now declare `narration: third-past`. The later brief specifies undressing, bed staging, paid-vigil continuity, established lovers and the unchanged morning destination. Existing slot IDs are reused.

`tests/test_iomedae_round3.py` adds history walks and generated-export regressions for these findings, including the shared fixes inspected above. `tests/IomedaeTricksterTests.cs` checks the first/returning split with the production Choice matcher; answer branches use supported requires/forbids, not scene-only OR groups. Neither test file changes shared rules or the frozen save baseline.

These are authored R6 refinements, not new lore or mechanics. Native evidence was checked in `/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`: Summit `Cue_0016` (`2e46d7fc0945a4e4d876b13bbad69ece`, localization `464287db-57c2-4ddf-ab81-796ede845743`) states the exception; GrandFinal `Cue_0074`, `Cue_0081`, `Cue_0085` and `Cue_0091` establish the witnesses' interests, Iomedae's defense of the Commander's choice, her sacrifice response and Areelu's final question. New witness dialogue is authored, not quoted canon.

## CLASS SWEEP

- Checked every route dream's historical references against the generator's live-guest classification. The two defective private dreams now identify earlier events explicitly, surviving the shared scene-kind and presence transforms.
- Checked both hall-memory nodes and both original banner continuations; witness variants preserve the rescue-only and personal-courtship distinction.
- Checked first/returning dream entry after the late Summit/Iz opening, each earlier dream receipt, and neither receipt.
- Checked both intimacy slots, the existing first-night identity, three platform mornings, paid ninth-year vigil, nonsexual rescue outcome and retained epilogue exits.
- Checked carried/no-banner histories, H1 open Wound, H2 flask return and earned bridge, Areelu present/absent, and both royal-blessing states through the shared return-reader partition.
- Retained every scene/node/relationship ID and original choice index; new choices/nodes/paragraphs append. Original route source CRLF is preserved. No shared storyline file, other route source, engine source or generated development export was edited.

## GATE

Generation, test input, logs and .NET outputs use a task-owned system-temp directory. `PYTHONHASHSEED=0`, `PYTHONUTF8=1`, `RRT_GAME_DIR=/wrath`, the build script's four parent-binding manifests, `RRT_STORY_OUTPUT` and `RRT_TEST_STORY` are supplied. The same fresh export is passed to the final gates; no generated repo file is written.

- `python expansion.py`: PASS on the final sources, 3,848 scenes.
- `python -m unittest tests.test_iomedae_round2 tests.test_iomedae_round3 tests.test_utf8_io -q`: PASS, 14 tests against the final export.
- `python tools/savecompat.py --story <fresh temp export>`: PASS, 0 hard failures; no baseline changed.
- `python tools/payoff_lint.py --strict --story <fresh temp export>`: PASS, 42 routes, 0 hard failures; existing other-route REVIEW notices remain.
- `python tools/departure_lint.py --strict --story <fresh temp export>`: PASS, 43 women, 0 hard failures; the existing Mielarah REVIEW notice remains.
- `dotnet build tests/RulesTests.csproj -c Release` with output/intermediate paths under system temp: PASS, final incremental build 0 warnings and 0 errors; the earlier full compile emitted 8 existing CS0649 warnings. Interrupted build attempts ended with signal 143; their retries completed.
- Focused compiled rules runner `--suites=IomedaeTricksterTests <fresh temp export>`: PASS, 169 assertions against the final export, including three new runtime history assertions. Its interrupted first attempt was retried on its own.
- Requested `python -m unittest discover -s tests -p "test_*.py" -q`: attempts ended with signal 143, without a result summary. NOT a pass.
- Requested `dotnet run --project tests/RulesTests.csproj -c Release -- <fresh temp export>`: launched using `--no-build` and `BaseOutputPath` / `BaseIntermediateOutputPath` environment variables pointing to the temp build; full attempts ended with signal 143, without a result summary. NOT a pass. The initial command-line-property launch looked for `tests/bin`; the corrected environment-property launch used the temporary executable.
- One full `python tools/rrt_verify.py --strict --story <temp export> --game /wrath`: PASS, 0 hard failures, 898.5 seconds.
- Final `python tools/rrt_verify.py --strict --gate-only --story <fresh temp export> --game /wrath`: PASS, 0 hard failures, 340.3 seconds. This rechecks every strict hard check after the history/runtime repairs; only advisory analyses already run in FULL are deferred.
- `git -c core.whitespace=cr-at-eol diff --check`: PASS. Both route sources retain CRLF throughout.

Task-owned temporary exports, logs, verifier reports, build outputs and bytecode caches were removed before finishing. No commit was made.

## ESCALATE

- Full Python discovery and full rules/progression runs need a coordinator rerun: the processes ended with SIGTERM (143), with no test summary or reported selectable-answer failure. The cause was not established; these gates are incomplete.
- Finding 4: `storylines/crossroute_presence.py` / shared presence reader must recognize the native Summit audience independently of `noct.closed`. No route-local lore or new romance requirement can justify the lockout.
- The new finale reactions use existing current-availability reads. The shared reader also conflates Nocticula romance closure with native presence; the native projection after Council defeat is distinct from an earned bodily romance return. The route's banner device proceeds without either cameo. Correcting native-versus-romance presence in the shared reader is coordinator work.

## PROPOSE

None beyond the required shared presence correction. No new mechanics, gates, prices, courtship requirements, reconciliation or return devices were implemented.

## RISKS

- Finding 4 remains open; this round cannot claim all dimensions at least 91.
- Full Python discovery and full C# progression remain unverified because their processes terminated without summaries. The route tests are narrower evidence.
- `tools/route_packs/voice_locks.json` is absent in this checkout and the searched Writer inputs. No available lock entry could be inspected; no shared revoiced scene text was edited.
- Explicit slots remain defaults plus briefs for user-selected filling, not completed explicit acts.
- The full game, harness and build-expansion script were not run; no game-runtime or independent-audit pass is claimed.

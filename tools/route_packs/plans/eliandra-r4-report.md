# R4 Eliandra local residue

Frozen base: `5dd587bd3277fa985e4293601290f59ad8dfcd6e`. No commit, per the final task instruction.

## CHANGES

| Finding | Status and evidence |
| --- | --- |
| D01 | OUT OF SCOPE: section 4.3 explicitly assigns the live-path fix to the existing native owner. S1's route-owner label conflicts with that scope instruction. `own_offering` still requires historical Trickster; escalate to its owner/J10. |
| D02, D03 | DONE: `storylines/eliandra_stars.py`, `also_in_drezen`, prefixes both `heart_new` and `heart_known` in both last-rite capital twins with departure, escorted travel, approach search and shrine entry. Capital conversation now places the crate across the street and describes preparation for the northward road. The actual rite and its expulsion remain at Pulura. |
| D04, D05 | DONE: the same file's `visit.star_heart` template changes `start` to Drezen and `ride_back` to departure after the already-played tailor-frontage reunion. Odden remains with the column at the fords. Both generated hosts receive the same correction. No second return, note or reunion. |
| D06, D07 | DONE: `walk_back` and `ride_back` both establish a crusader escort searching the exposed shrine and keeping watch through the night. This is an authored, limited visit, consistent with native evacuation; no restored secrecy, resettlement, safety quest, fee or check. |
| D08, D09 | VERIFIED / NO CHANGE NEEDED: `storylines/endings_job3.py::eliandra` already moves disclosure to `page` before the lover choice, keeps one acceptance/arrival in `late_accepted`, and filters duplicate proposal/arrival paragraphs. Retained shared finalizer; did not edit shared endings. |
| D10, D11, D12 | DONE: `storylines/eliandra_trickster.py::EPILOGUE_PARAGRAPHS` replaces the single stolen-work burn certification consumed by all three endings with an unresolved promise, yearly inquiries and missing-work descriptions. Theft plus a promise earns no recovery/destruction claim. Untheft and research-keep siblings retain their distinct histories. |

`tools/route_packs/plans/voice-review-pending.json` queues the seven affected rendered scenes for Claude review. No Eliandra scenes occur in `voice_locks.json`; no locked prose or explicit-slot defaults changed. No class I/J finding was assigned, and no broader character redesign was undertaken.

Native anchors verified directly in `/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`:

- Both last-rite capital twins and both star-heart visit hosts: PuluraLeaderSaved/Cue_0030, asset `28e3b35d52e24fb4da16778f68b2b1c2`, enGB `89825892-cab0-4831-9855-6860e58b7e42`. Her temple has lost its secrecy; she leads survivors elsewhere. The rite retains her desire for release, her prayer and the existing sight/strength sacrifice. The visit retains her chosen night and taking the Commander's hand; escort time provides only temporary protection.
- Each of `epilogue.together`, `epilogue.late`, `epilogue.unasked`: PuluraLeaderSaved/Cue_0031, enGB `1829b057-82b7-4649-8647-529940862f3c`, anchors her life's work and fear of another Wound. She wants to prevent misuse, sends descriptions and asks for news; the unresolved stolen knowledge remains a consequence. Mutasafen/Cue_0013, asset `271f0a6740e81f9439202f568b51a194`, enGB `1a8efd32-d009-425d-8dc0-176571667234`, independently confirms the escaped information.

## CLASS SWEEP

- Checked original shrine rite and both capital twins, including both remembered/new heart branches, refusal, failed offering and expulsion. Original shrine staging stays local; capital twins now reach it explicitly.
- Checked both visit hosts and both letter/nonletter approaches against `road_letter -> return_from_fords -> visit`. The arrival still clears absence only through its existing earned return.
- Checked both late epilogues through the shared finalizer, including truth/no-lie disclosure, acceptance, friendship and refusal. No additional romantic eligibility or reconciliation condition.
- Checked stolen-burn, unstolen-burn and keep paragraphs across all three endings and their finalizer copies. Only the unearned destruction class changed.
- Compared all Eliandra scene structures to HEAD with text excluded: identical scene/node order, choice indices/identities, links, checks, gates and effects. CRLF preserved in both edited route files. No new foresight/echo beat, native rewrite or gate.

## GATE

Export consumers use fresh system-temp `Story.json` via `--story` (or the positional C# argument), preserving the ban on edits to `development/`. Generation/verifier use `PYTHONHASHSEED=0`, `RRT_GAME_DIR=/wrath`, and the four parent-binding paths from `build-expansion.ps1`.

| Command/check | Result |
| --- | --- |
| `python expansion.py`, with `RRT_STORY_OUTPUT` in system temp | PASS: 4054 scenes, exit 0. |
| `python -m unittest discover -s tests -p 'test_eliandra*.py' -q` | PASS: 8 tests. |
| `python -m unittest discover -s tests -p 'test_utf8_io.py' -q` | PASS: 1 test. |
| Requested `python -m unittest discover -s tests -p 'test_*.py' -q` | BLOCKED: host guard killed both attempts, exit 143; no PASS claimed. |
| `python tools/savecompat.py --story ...` | PASS: 0 hard failures. |
| `python tools/payoff_lint.py --strict --story ...` | PASS: 42 routes, 0 hard failures. |
| `python tools/departure_lint.py --strict --story ...` | PASS: 43 women, 0 hard failures. |
| `python tools/voice_lock_lint.py --strict --story ...` | PASS: 576 locks, 0 changed, 0 missing/ambiguous. |
| `python tools/slot_brief_lint.py --story ...` | Global inventory: 315 inherited hard findings outside Eliandra, 168 warnings. No brief or slot text changed. |
| Same slot lint with `--strict --briefs tools/route_packs/explicit_slots/eliandra` | PASS: 5 briefs, 0 hard, 1 existing male-pronoun review warning. |
| `dotnet build tests/RulesTests.csproj -c Release`, system-temp intermediate/output paths | PASS: 0 errors, 8 warnings. |
| Requested unfiltered C# rules/progression run | BLOCKED: `dotnet run --no-build` looked for absent repo build output despite the custom output-root arguments. Equivalent execution of the fresh DLL was killed by the host full-suite guard, exit 143. |
| Fresh DLL with `--suites=EliandraTricksterTests,ParagraphTests,PayoffDepartureRulesTests` | PASS: 44,215 assertions in 3 selected suites. |
| Rendered history checks on fresh export | PASS: D08/D09 disclosure before lover choice, no duplicate accepted proposal/arrival; unresolved theft paragraph on together and all three late/unasked answer branches. |
| Text-excluded route structure comparison against HEAD | PASS: all mechanics and persistent identities/order unchanged. |
| `git -c core.whitespace=cr-at-eol diff --check` | PASS; both route files retain exclusively CRLF newlines. |
| `python tools/rrt_verify.py --strict --story ...` (once) | FAIL: 13 hard player-text findings, all in untouched Jerribeth scenes; exit 1, 885.1 seconds. Zero validation, producer, native-binding, return-safety, savecompat, earned-presence, text-structure, intimacy, memory or transaction hard failures. No Eliandra hard finding. |

No build-expansion script, harness, game, merge or commit. System-temp artifacts are deleted before completion.

## ESCALATE

- D01: live-path requirement and off-path unresolved account remain with the designated native owner/J10. The Legend counterhistory is not repaired by this local prose pass.
- J01–J10/shared work remains outside scope: household contact/stance contracts, Eliandra–Areelu shelter delivery (J05.K1-E), native dependent rewrites and release acceptance (J10), shared ending finalizers, and installed-game proof. None edited.
- Full Python discovery and unfiltered C# execution are blocked by `/work/testguard.sh`, which logs `kill(full)` for this worktree. Discovery returned 143 twice; the full C# DLL run returned 143. The guard permits named tests and filtered C# suites; it was not modified or bypassed.
- Strict verifier's 13 inherited player-text hard findings belong to Jerribeth's voice owner, outside this route scope. Exact scene/node locations:
  - `jerribeth.farewell/traitor_fed`: commander-gender; `/discovery_distant`: speaker-attribution-review.
  - `jerribeth.ending_together/catalogue` and `jerribeth.ending_ascended/catalogue`: commander-gender.
  - `jerribeth.offered_signature/companion_regill`: commander-gender.
  - `jerribeth.counterfeit_guest/maker` and `/square`: commander-gender; `/scout_known`: embedded-commander-speech.
  - `jerribeth.counterfeit_audience/challenge`, `/leverage.reply.1`, `/departure.reply.1`, `/raid_dismissed`: commander-gender.
  - `jerribeth.counterfeit_spoil/object`: commander-gender.
- Global slot lint's 315 inherited hard findings require the other route/brief owners (J10 normalization). Eliandra's five briefs have zero hard findings; no other briefs were edited.

## PROPOSE

None. No research chase, vow price, new gate or reconciliation mechanic implemented.

## RISKS

- D01 remains unresolved outside this scope; global strict verification is red on the 13 unrelated findings, and full Python/C# suites lack acceptance because of the host guard. This report does not claim every rubric dimension reaches 91.
- Authored escort staging explains only the existing visit's limited safety, not renewed protection of the temple.
- Claude review and coordinator independent audit remain pending. No game/harness/full build was run; no prose score is self-certified.
- No required beat was refused. No new mechanics or reconciliation conditions were introduced.

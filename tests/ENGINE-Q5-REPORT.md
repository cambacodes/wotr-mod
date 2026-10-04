# ENGINE-Q5 implementation report

Branch: `claude/engine-q5`.
Acceptance is blocked by the Aranka progression conflict under ESCALATE.
No commit was made.

## CHANGES

- `storylines/earned_presence.py` (B): centrally generates `<relationship>.presence.route_open` through existing `DerivedOpenRoutes` and appends it to every partner presence.
  All 47 presence definitions across 29 relationships now obey `Rules.RouteOpen`, including ClosedFlag, UnavailableFlags, and existing earned-return overrides.
  No runtime exception was added.
- `tools/earned_presence_lint.py` (A/B): T7 traces return override values and TricksterAccess Returned/Device keys through Derived/Latch composites and checks their authored producers, Revive choices, TricksterDevice scenes, and explicit device-completion flags.
  Only current evidence proves a new act; historical flags and latches cannot.
  P1 checks the central guard and route mapping on each partner presence and requires departure-named choice effects to be registered or explicitly exempted with a reason.
- `tools/rrt_verify.py` (A/B): includes these lint failures in the strict hard-failure total.
- The 29 modules and 112 scenes listed below (A): append `trickster.now` without changing IDs, order, choices, prose, costs, or historical requirements.
  Consumers of earned returns retain their existing historical requirements.
- Permanent departure metadata (B): append `kaylessa.trickster.left_free`, `horzalah.trickster.left_free`, `elyanka.trickster.left_free`, `melazmera.trickster.left_free`, `yaniel.trickster.left_free`, `jannah.trickster.gone`, and `aranka.trickster.gone_to_nerosyan` to the corresponding relationship UnavailableFlags.
  Existing earned-return overrides remain unchanged.
- `storylines/earned_presence.py` exemptions (B): Konomi's private departure continues by correspondence and explicitly hides her physical presence; Nocticula's Ilvara exile, Dorgelinda's driver, Kaylessa's wasp, and Galfrey's envoy concern other actors; Iomedae's dismissal concerns a banner dream before physical arrival.
  Each exemption includes its reason.
- `tests/test_engine_q5.py` (A/B): nine focused tests cover live versus historical evidence, scene/choice guards, failure, composites, device flags, guard integrity, idempotence, and departure exemptions.
- `tests/EngineQ5Tests.cs` and `tests/Program.cs` (A/B): verify every generated presence against closure, unavailable states, and earned returns after leaving Trickster, plus the four audited Anevia, Seelah, Minagho, and Chivarro producers after failure.
- Existing route fixture files listed below and `tests/test_earned_presence.py` (A/B): normal route walkthroughs now supply current native Trickster evidence and runtime chapter flags where needed.
  Failure/conversion cases remain explicit, changed unavailable/presence metadata expectations are updated, and primed devices are rejected after failure.
  Aranka's failing progression assertion remains intact.
- `tests/temp_directory.py`, `tests/test_parent_bindings.py`, `tests/test_pacing_lint.py`, and `tests/test_return_safety.py` (gate repair): disposable fixtures inherit the Windows sandbox identity's permissions.
  Python's mode-0700 temporary directories caused five existing tests to fail with access denied.

### Every changed scene

Only the scene requirement is appended in this list.
The seven departure registrations above change relationship metadata.

- `storylines/anevia_trickster.py`: `anevia.trickster.gone.confession`, `anevia.trickster.gone.fetched`, `anevia.trickster.gone.wardrobe`.
- `storylines/aranka_trickster.py`: `aranka.trickster.failure.reckoning`, `aranka.trickster.failure.reckoning_yard`, `aranka.trickster.failure.second_verse`, `aranka.trickster.failure.second_verse_late`, `aranka.trickster.touring.arrives`, `aranka.trickster.touring.arrives_late`, `aranka.trickster.touring.arrives_yard`, `aranka.trickster.touring.arrives_yard_late`, `aranka.trickster.verse.her_letter`, `aranka.trickster.verse.her_letter_late`.
- `storylines/arueshalae_trickster.py`: `arueshalae.trickster.evil.second_opinion`.
- `storylines/camellia_trickster.py`: `camellia.trickster.killed.performance`, `camellia.trickster.killed.performance_letter`, `camellia.trickster.killed.third_night`.
- `storylines/devarra_trickster.py`: `devarra.trickster.dead.woken`, `devarra.trickster.flight.eggs`.
- `storylines/dorgelinda_trickster.py`: `dorgelinda.trickster.audit.open`.
- `storylines/eliandra_stars.py`: `eliandra.trickster.ch5.self_offering`, `eliandra.trickster.ch5.self_offering_mark`.
- `storylines/galfrey_trickster.py`: `galfrey.trickster.iz.eulogy`, `galfrey.trickster.iz.road`, `galfrey.trickster.return.kitrane`, `galfrey.trickster.return.kitrane_scarred`.
- `storylines/gesmerha_trickster.py`: `gesmerha.trickster.dead.unfinished_work`.
- `storylines/hepzamirah_trickster.py`: `hepzamirah.trickster.ghost.body`.
- `storylines/irabeth_trickster.py`: `irabeth.trickster.dead.relieved_not_dismissed`, `irabeth.trickster.killed.blow_missed`.
- `storylines/jannah_trickster.py`: `jannah.trickster.alive.stories`, `jannah.trickster.alive.wagon`, `jannah.trickster.cage.ash`, `jannah.trickster.killed.yield`.
- `storylines/jerribeth_trickster.py`: `jerribeth.trickster.dead.tenant`, `jerribeth.trickster.dead.tenant_nexus`.
- `storylines/kaylessa_trickster.py`: `kaylessa.trickster.alive.amulet_swap`, `kaylessa.trickster.dead.soldier`.
- `storylines/kiana_trickster.py`: `kiana.trickster.after.letter`, `kiana.trickster.after.temple`, `kiana.trickster.aftermath.letter_waited`.
- `storylines/konomi_trickster.py`: `konomi.trickster.dead.consultation`, `konomi.trickster.dismissed.recess`, `konomi.trickster.never_arrived.audience`, `konomi.trickster.never_arrived.audience_letter`.
- `storylines/melazmera_trickster.py`: `melazmera.trickster.ch4.hunt`, `melazmera.trickster.ch4.hunt_found`, `melazmera.trickster.ch5.hunt_window`.
- `storylines/mielarah_trickster.py`: `mielarah.trickster.raid.ashore`, `mielarah.trickster.raid.elbow`, `mielarah.trickster.raid.rope`, `mielarah.trickster.raid.whisper`, `mielarah.trickster.raid.wind`, `mielarah.trickster.storm.survivor`, `mielarah.trickster.storm.word`.
- `storylines/minagho_chivarro_trickster.py`: `minagho_chivarro.trickster.alone.chivarro`, `minagho_chivarro.trickster.alone.chivarro_letter`, `minagho_chivarro.trickster.alone.chivarro_morning`, `minagho_chivarro.trickster.alone.chivarro_when_it_scars`, `minagho_chivarro.trickster.alone.minagho`, `minagho_chivarro.trickster.alone.minagho_letter`, `minagho_chivarro.trickster.alone.minagho_morning`, `minagho_chivarro.trickster.alone.minagho_spared`, `minagho_chivarro.trickster.alone.minagho_spared_morning`, `minagho_chivarro.trickster.alone.minagho_when_it_scars`, `minagho_chivarro.trickster.chivarro_dead.bought`, `minagho_chivarro.trickster.chivarro_dead.the_bill`, `minagho_chivarro.trickster.chivarro_dead.the_bill_letter`, `minagho_chivarro.trickster.minagho_dead.brand`, `minagho_chivarro.trickster.minagho_dead.brand_letter`, `minagho_chivarro.trickster.minagho_dead.collateral`, `minagho_chivarro.trickster.react.baphomet`, `minagho_chivarro.trickster.spared.brand`, `minagho_chivarro.trickster.spared.brand_letter`.
- `storylines/nenio_trickster.py`: `nenio.trickster.away.correction_arcade`, `nenio.trickster.away.correction_visitor`.
- `storylines/nidalynn_trickster.py`: `nidalynn.trickster.steps.widow`.
- `storylines/nocticula_trickster.py`: `nocticula.trickster.defeated.call_in`.
- `storylines/nurah_trickster.py`: `nurah.trickster.dead.bill_of_sale`, `nurah.trickster.prison.night_out`, `nurah.trickster.prison.night_out_late`, `nurah.trickster.prison.proofs`, `nurah.trickster.prison.proofs_late`, `nurah.trickster.prison.terms`, `nurah.trickster.prison.terms_late`, `nurah.trickster.ran_off.terms_by_post`, `nurah.trickster.ran_off.terms_by_post_late`.
- `storylines/seelah_trickster.py`: `seelah.trickster.dead.effects_arrival`, `seelah.trickster.dead.effects_reply`, `seelah.trickster.dismissed.back_for_the_papers`, `seelah.trickster.dismissed.back_for_the_papers_letter`.
- `storylines/shamira_trickster.py`: `shamira.trickster.killed.voice`, `shamira.trickster.killed.voice_letter`.
- `storylines/soana_trickster.py`: `soana.trickster.missed.crooked_luck`.
- `storylines/targona_trickster.py`: `targona.trickster.dead.long_sleep`, `targona.trickster.dead.one_soul`, `targona.trickster.free.furlough`.
- `storylines/vellexia_trickster.py`: `vellexia.trickster.mirrored.fetch`, `vellexia.trickster.mirrored.speaks`, `vellexia.trickster.mirrored.unmirror`, `vellexia.trickster.mirrored.unmirror_stores`, `vellexia.trickster.sword.likeness`, `vellexia.trickster.sword.likeness_stores`, `vellexia.trickster.sword.portrait`.
- `storylines/wenduag_trickster.py`: `wenduag.trickster.abyss.back`, `wenduag.trickster.abyss.fall`, `wenduag.trickster.ch4.stone`, `wenduag.trickster.exile.champion`, `wenduag.trickster.killed.back`, `wenduag.trickster.killed.cairn`, `wenduag.trickster.street.back`, `wenduag.trickster.street.fall`.

### Existing route fixture files

- `tests/AneviaTricksterTests.cs`.
- `tests/ArankaTricksterTests.cs`.
- `tests/ArueshalaeTricksterTests.cs`.
- `tests/CamelliaTricksterTests.cs`.
- `tests/DevarraTricksterTests.cs`.
- `tests/DorgelindaTricksterTests.cs`.
- `tests/EliandraTricksterTests.cs`.
- `tests/ElyankaTricksterTests.cs`.
- `tests/GalfreyTricksterTests.cs`.
- `tests/GesmerhaTricksterTests.cs`.
- `tests/HepzamirahTricksterTests.cs`.
- `tests/HorzalahTricksterTests.cs`.
- `tests/IrabethTricksterTests.cs`.
- `tests/JannahTricksterTests.cs`.
- `tests/JerribethTricksterTests.cs`.
- `tests/KaylessaTricksterTests.cs`.
- `tests/KianaTricksterTests.cs`.
- `tests/KonomiTricksterTests.cs`.
- `tests/MelazmeraTricksterTests.cs`.
- `tests/MielarahTricksterTests.cs`.
- `tests/MinaghoChivarroTricksterTests.cs`.
- `tests/NenioTricksterTests.cs`.
- `tests/NidalynnTricksterTests.cs`.
- `tests/NocticulaTricksterTests.cs`.
- `tests/NurahTricksterTests.cs`.
- `tests/SeelahTricksterTests.cs`.
- `tests/ShamiraTricksterTests.cs`.
- `tests/SoanaTricksterTests.cs`.
- `tests/TargonaTricksterTests.cs`.
- `tests/VellexiaTricksterTests.cs`.
- `tests/WenduagTricksterTests.cs`.
- `tests/YanielTricksterTests.cs`.

## CLASS SWEEP

- Swept all storylines through the generated story for return overrides, returned/device keys, revivals, and explicit device completion producers.
  The initial export had 471 T7/P1 hard findings; the final export has zero earned-presence hard findings.
- Swept all 47 physical partner presences across 29 relationships, including contact and spawn-copy modes.
  Eliandra and Herrax/Chivarro closures are covered centrally; Elyanka/Camilary and Melazmera departures are covered by appended unavailable flags.
- Swept departure-named authored choice effects, registering seven permanent departures and documenting six exemptions.
- Compared final generated save shape directly with raw HEAD bytes: relationship key order, every scene ID/order, every node ID/order, and every choice index/text/Set/Next/Check are identical.
  No scene, node, relationship, or choice was renamed, deleted, or reordered.
  Existing source line endings were preserved, including mixed-ending test files.
- No authored prose, native blueprint bindings, foresight/echo implementation, shared household/Last Call/world modules, or other mechanics were changed.
  Existing runtime route checks were reused; no src or managed-tests source changes were needed.

## GATE

Export-dependent checks used `PYTHONHASHSEED=0` and the four existing parent-binding files under `reference/canon-review` through `RRT_PARENT_BINDINGS`.
The SDK executable was `%LOCALAPPDATA%/RanRomanceTools/dotnet/dotnet.exe` because dotnet was absent from PATH.
Managed native extraction used the installed Python 3.14 executable through `RRT_PYTHON`.

| Command | Result |
| --- | --- |
| `python expansion.py` | PASS: 2855 scenes, 47 relationships, 47 presences; existing incomplete-development-export label. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | PASS: 167 tests; final run 30.890 seconds. |
| `python tools/rrt_verify.py --strict --json tests/engine-q5-verify.json --text tests/engine-q5-verify.txt` | PASS: 0 hard failures, including T7/P1; 342 seconds. |
| `python tools/earned_presence_lint.py --story development/Story.json` | PASS: 0 hard, 0 review. |
| `python tools/gate_lint.py --story development/Story.json` | PASS: 0 hard. |
| `python tools/harem_schedule_lint.py --story development/Story.json` | PASS: 48 candidates, 57 beats, 3 packets, 0 hard. |
| `python tools/harem_smoothing_lint.py --story development/Story.json` | PASS: 41 women, 33 repairs, 0 errors. |
| `python tools/pacing_lint.py --story development/Story.json` | PASS: 0 hard; 4 existing warnings and 16 review items. |
| `dotnet build src/Tirabade.csproj -c Release --nologo -v quiet` | PASS: 0 errors. |
| `dotnet build managed-tests/ManagedBuildTests.csproj -c Release --nologo -v quiet` | PASS: 0 errors. |
| `RRT_TEST_EXPANDED_EPILOGUE=0`, run `managed-tests/bin/Release/net48/ManagedBuildTests.exe` | PASS: 413820 assertions. |
| `RRT_TEST_EXPANDED_EPILOGUE=1`, run the same executable | PASS: 413823 assertions. |
| `RRT_TEST_EXPANDED_EPILOGUE=wrong-type`, run the same executable | PASS: 1891 assertions; optional wrong-type epilogue ignored with expected warning; addon initialized. |
| `dotnet build tests/RulesTests.csproj -c Release --nologo -v quiet` | PASS: 0 errors. |
| `dotnet run --project tests/RulesTests.csproj -c Release --no-build -- development/Story.json` | FAIL: Aranka's existing failure-route progression assertion, detailed below. |
| Independent diagnostic execution of route test entry points and EngineQ5Tests | Executed route suites passed except Aranka; EngineQ5Tests passed. |
| Save-shape comparison and `git diff --check` | PASS. |

The ordinary RulesTests run stops at Aranka; later suite completion cannot be claimed for that run.
No "Page has no selectable answers" failure was observed.
The temporary diagnostic runner and gate evidence files remain under tests because automatic approval review rejected both recursive cleanup and subsequent individual-file cleanup as blocked by policy.
The diagnostic runner is in tests/.engine-q5-probe, which is excluded from ordinary RulesTests source discovery.
Builds retain existing nullable/unused-field warnings and NU1900 advisory-fetch warnings under restricted network access.
Managed checks exercise real blueprint construction and native fixtures, not a campaign or save round trip.
No game, build-expansion.ps1, product harness, or git commit was run.
The generated development/Story.json was restored byte-for-byte to HEAD after verification so only allowed source/report files remain in the diff.
Regenerate it before coordinator verification.

## ESCALATE

1. Aranka's failure return has a circular dependency with the required central presence guard.
   `aranka.ran_failure` blocks RouteOpen until the existing override `aranka.trickster.moral_repaired` is earned.
   Her paid remote letter/second verse earns answered/returned; moral repair is earned only by `aranka.trickster.failure.reckoning` or its yard twin through physical contact.
   Both contacts are now hidden until RouteOpen holds, leaving no contact at which to earn moral repair.
   The preserved progression test fails with `King, failure (market): her presence is not wanted after her answer.` at `tests/ArankaTricksterTests.cs:507`.
   The coordinator must resolve this contract conflict before acceptance.
   Replacing the override or introducing an exception would alter reconciliation or presence mechanics, which the strict task scope forbids.
2. Five disposable directories under tests/.engine-q5-tmp remain inaccessible: tmp46t3xhq5, tmpcxy9imoo, tmpf5wahkin, tmphtjk6u6j, and tmpla0pp67b.
   Ordinary deletion fails with access denied.
   Automatic approval review rejected a permission reset as blocked by policy; no ACL reset was performed.
   Cleanup requires the workspace owner or coordinator outside this restricted token.
   Temporary diagnostic and gate evidence files also remain under tests after automatic approval review rejected their deletion as blocked by policy.

## PROPOSE

Resolve Aranka's physical-return versus relationship-reconciliation contract explicitly.
A coordinator-approved design could distinguish physical return from moral reconciliation, or make the existing reckoning accessible without requiring the blocked presence.
Neither proposal was implemented.
No mechanics, prices, gates, requirements, or reconciliation conditions were added beyond the requested findings.

## RISKS

- Aranka prevents a passing mandatory RulesTests gate and prevents claiming the requested >=91 acceptance threshold.
- Departure detection uses conventional flag names and an explicit exemption registry; a future departing flag with an unrelated name needs registration and review.
- Earned returns intentionally remain valid after leaving Trickster; only new producer acts require current power.
- Save identities and choice indices are unchanged, but eligibility intentionally changes for off-path producers and closed/departed presences.
- No campaign, visual inspection, or game save round trip was performed because those runs were prohibited.

Verified generated-story SHA256: `5265e085e7bbba0b074c4d94a61257a5047b5cc7e849420878a34920f841f71f`.

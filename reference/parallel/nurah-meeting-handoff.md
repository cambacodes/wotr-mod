# Nurah retained actor foundation

Status: staged observer implementation, frozen for independent review.
No placement, arrival claim, meeting registration, shared build, or route approval is included in this stage.

## Frozen files and checks

- `src/NurahMeeting.cs`: SHA256 `723223CE6F6AD0DBF7B19B02DEFC23757FF49314DBF28A9B54050436DDE38DBD`.
- `managed-tests/NurahMeetingTests.cs`: SHA256 `A69C732F7637B0BB38500B96960FF9C831388C3F617E7CEE2CFDE0B9F55202D8`.
- Isolated harness: `C:/Users/Z/AppData/Local/Temp/nurah-meeting-woilumi_/Observer.csproj` and `Runner.csproj`.
- Both build with `C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe build <project> -c Release --nologo -v minimal`.
- Run `bin/Release/net48/Runner.exe` from that directory: **41 assertions passed**.
- Full current `src/*.cs` compiled against installed native assemblies with zero warnings and errors.

The tests use actual native saved spawner, scene, unit, life-state, blueprint, and etude classes with isolated field construction.
They exercise retained identity, registry disagreement, duplicate actors/spawners/scenes, destruction, current and historical death, wrong area/representation, missing parent terminal, current versus completed romance, imprisonment, personality ambiguity, and resolver aliases.
They do not run native actor spawning, Unity placement, navmesh reachability, player interaction, or the full positive `CorrespondenceAvailable` entry point.
The observer deliberately accepts an exact living saved actor without a Unity view as identity evidence; that result does not establish physical contact.

## Implemented boundary

`new NurahMeeting(resolve)` binds exact typed native/parent GUIDs.
`CorrespondenceAvailable()` is read-only and independent of invitation consent.
It requires the loaded capital, a conscious living Commander outside combat, no duplicate saved capital state, the exact retained living capital Nurah, consciousness, no suppression/hostility, current parent romance, the actual accepted Book5 terminal in native shown-cue history, no current imprisonment, no started/completed native death state, and exactly one current Good/Chaos/Evil personality.
A completed imprisonment state can represent release and does not itself block her.
A completed romance does block her: the parent also completes that romance during other endings, so completion is not an accepted relationship.
Any retained spawner `HasDied` blocks this living-only foundation; no unrequested resurrection is inferred.
Native history is never modified.

This proof is not the whole route gate.
Root must still require Chapter 5, the authored current-path restrictions, invitation and reply completion, accepted rather than declined/withdrawn consent, the exact 12-hour accepted timestamp, and route closure checks.
The future helper callback will read those raw flags and supply stable `nurah.private/<retry>` identity.
No callback or mutation API exists yet in this observer-only stage.

## Direct native evidence

Parent source audit and pinned bindings are in `reference/canon-review/nurah-extension-audit.md` and `nurah-parent-bindings.json`.
Fresh source extraction is retained at `C:/Users/Z/AppData/Local/Temp/nurah-extension-audit-3y60fthx`.
`nurah-spawner-scene.json` was extracted directly with UnityPy from the installed `Bundles/drezencapital_default_mechanics.scenes`.
The object is named `Nura`, with capital blueprint `f999fc37ddb225640b7f98c0a05d6948` and spawner `c2b298fc-d794-4995-8b49-822b75c3bb62`.
Its scene is `3e2b5ea054cd5b2479e7f13134363ef4`; it spawns on scene initialization, does not respawn when dead, starts hidden, and permits hidden-view simplification/save optimization.
Thus an existing living body can still be inaccessible or have a dummy view.

`Nurah_DefaultActor` `245524f91e743b64eaa16445c3ea8e73` owns Nurah group `d0210e61193c8c746bc33bf7d1fff325` at priority -100.
It hides the capital spawner unless the after-death state is playing.
The only audited native positive placement for Nurah herself is prison mechanic `21a061de3610732438072d2b975b6f43`, priority 0, which unhides/moves her to `NurahInPrison_Locator` in Chapter 3 and otherwise hides her.
Its prison parent and death/runoff/Chapter 5 conditions make it unsuitable as an ordinary free post-finale romantic meeting.
No prison history is cleared or reactivated.

## Non-cell location investigation

`meeting-scene.json` directly verifies a separate native marker named `YakerNearTavern`, ID `0de46237-5bf5-422b-ab1b-00d99469e37e`, in the same capital scene.
Its local position is approximately `(-61.70, 45.13, -78.04)`; these are evidence, not new authored coordinates.
`YakerInCapital` `67adc200329d481f967099190b5adee0` uses an unconditional unhide and translocate action to this point when its activation condition finds `YakerToAmbassador` `1bbd925ef42ac6740aba35227527ca3b` playing.
The ambassador state starts that placement etude.
The native actor is Yaker spawner `9f2e268d-dc48-4139-a506-38bb12b44409`, blueprint `74002884024f5fe45afd8c99d962b671`.
Neither placement nor ambassador state contributes Nurah's conflict group, so Nurah group arbitration alone cannot reserve this point.
Full archive references are retained in `yaker-references.json`; the exact placement record is `YakerInCapital.json`.

This point is an investigation candidate, not an approved general appointment location.
A conservative borrow would need to defer for Yaker's current/pending commitment and actual visible occupancy, without moving him or preventing his event.
Permanently excluding all ambassador histories would create an unrelated route restriction, so that shortcut is not implemented.
A location name supports "near the tavern"; it does not establish a private alcove, empty room, or literal interior scene.
Alternative points and a resumable occupancy contract remain to be investigated.

## Next implementation gate

Before movement, verify a credible free meeting location and its native owner lifecycle, then review a concrete arbitration contract.
The helper must yield to every live Nurah claim, use only the exact retained actor, preflight the locator, unhide through the native action, reread the possibly replaced view, move once, and prove current arrival before any physical scene.
A partial attempted placement failure must be saved against the stable consent episode and require explicit retry; ordinary preemption before mutation should resume the existing invitation naturally.
Save/load must revalidate identity and actual arrival.
No shared `Main`, runner, registration, manifest, prose, or Pulura quest bug was edited by this task.

## Prison completion correction

The independent observer review correctly rejected the first frozen version because native saved completion precedes actual prison fact deactivation.
That report remains historical evidence in `nurah-observer-independent-review.md`.
The corrected `PrisonBlocks` adapter now inspects the actual native fact as well as saved history.
A playing, completing, or unfinished prison fact blocks even if the dictionary already says Completed.
A finished inactive fact or completed history with no retained fact permits release; a pending/started saved entry still blocks.
Eleven added native-adapter assertions construct the actual EtudesSystem saved dictionary and EtudesTree fact lookup, reproduce the early-published completion state, and check the subsequent completion stages and absent-fact cases.
The original thirty assertions remain unchanged.
The revised forty-one assertions pass in the same isolated harness with zero build warnings/errors.
This correction awaits independent rereview and does not approve placement.

## Shared observer checkpoint

The corrected observer and focused tests passed independent rereview at source `723223CE6F6AD0DBF7B19B02DEFC23757FF49314DBF28A9B54050436DDE38DBD` and test `A69C732F7637B0BB38500B96960FF9C831388C3F617E7CEE2CFDE0B9F55202D8`.
Root registered the focused tests in the shared managed runner.
Both builds passed with zero warnings and errors; the full runner passed 79,952 assertions against the unchanged 612-scene story A23F0AE6ABE6FAB6F0C275FBF8E1E8044EBEEA1FD040C12D61C4BD0F7D5829CC.
The tested DLL is `186121111CCC3457A41A56FC56F9D9B15B5152058A371FAA000555A5206E4252`.
The full log is `C:/Users/Z/AppData/Local/Temp/nurah-observer-shared.out`.
Main does not construct or call this helper yet; this checkpoint integrates reviewed observer code and test coverage, not route availability.
Movement remains a separate candidate under the private-appointment contract.

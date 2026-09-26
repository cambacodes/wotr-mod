# Remote conversation continuation repair

Status: Rules implementation and focused tests released for independent parent review; shared Main integration and compiled managed verification are separate.
This is a headless reproduction using actual authored pages and Rules, not a Unity end-to-end run.
No installed mod files were changed.

## Reproduction

The original `ContactAvailable` returned true immediately for any scene without `ContactUnit`.
The original `Main.Build` also supplied no continuation condition or interruption exit to those remote scenes.
Both defects matter: changing Rules alone cannot protect answers that never call it.

The isolated witness actually walks eight Vellexia visits from `unfinished_likeness` through `the_price_of_tomorrow`, selecting completed paths that do not close the relationship.
It then supplies the observed native peaceful-dismissal history, changes the location to the Nexus, clears physical contacts and opens `vellexia.the_second_invitation` through its `evidence` page.
The native dismissal is an external snapshot transition, not a fabricated authored effect or a demonstrated live-game quest transition.
Before the repair, adding `vellexia.dead` after that page opened left continuation available and failed with `Opened echo survives native blocker: vellexia.dead`.
Every blocker now has a valid open-page witness before it is applied, an entry-invalidation assertion, a continuation-invalidation assertion and a restoration assertion.
The tested blockers are death, early fight, final fight, mirror outcome, native coercion and the native-derived `inhuman` transformation composite.
Area and chapter changes also invalidate the open echo.

The parent separately reproduced the actual blueprint-construction omission against the unchanged DLL: the new expected remote exit failed with `Wrong choice count: abyss_letter.start`.
That is a parent-reported managed result, distinct from this agent's Rules reproduction.

## Implementation contract

`Rules.ContactAvailable` now evaluates remote non-epilogue scenes even when they have no physical contact unit.
It uses the existing chapter, area, prerequisite, alternative-prerequisite and native-forbid checks and relationship unavailability.
Physical scenes still require their primary and additional contacts.
Ordinary unitless nonremote scenes retain their existing behavior.

The native classification also includes `inhuman`, `ascended`, `chapter_one` and `chapter_later`, whose current-state derivation was inspected in `Main.State`.
Recognizing only native binding dictionaries missed the transformation composite used by Vellexia.
This does not turn every arbitrary authored forbid or summary failure flag into a continuation stop.
There is no new generic rejection of all death flags.

Continuation does not reapply scene completion, relationship closure, authored forbids or entry delay.
An answer can therefore close a relationship or set an authored entry exclusion without suppressing its own following page.
`ForbidOverrides` remains entry logic; it overrides authored flags, which continuation deliberately does not reject.
Seelah's actual recovery permits its own configured historical death flag, while still requiring `revive.seelah.available` and rejecting unrelated unavailability.
This preserves a real recovery opportunity rather than making every dead character automatically eligible.
Unitless epilogues are excluded so a death epilogue can finish describing the death.

The required Main predicate is `!ending && (scene.ContactUnit != null || Rules.IsRemote(scene))`.
The parent implemented it once per node and passes the same scene into answer visibility, selection, effects and native roll conditions, then appends the existing interruption exit.
I independently inspected that diff and the managed assertions for original answer identity, answer counts, the exit, visibility, selection, effects and roll guards.
I found no missing wiring in the inspected change.
I did not build or approve the resulting shared DLL.

## Focused verification

The isolated runner is `C:/Users/Z/AppData/Local/Temp/remote-continuation-review-kb7fgmqy/Check.csproj`.
It links actual `src/Story.cs` and the permanent `tests/RemoteContinuationTests.cs`, with an isolated Rules walker and output directory.
`Story.before.cs.txt` in that directory preserves the pre-repair implementation used for reproduction.

Commands, from the project directory:

```powershell
& 'C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe' run --project 'C:/Users/Z/AppData/Local/Temp/remote-continuation-review-kb7fgmqy/Check.csproj' -- all development/Story.json
& 'C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe' run --no-build --project 'C:/Users/Z/AppData/Local/Temp/remote-continuation-review-kb7fgmqy/Check.csproj' -- all 'C:/Users/Z/AppData/Local/Temp/remote-continuation-review-kb7fgmqy/candidate.json'
```

- Current 459-scene export: 38 focused assertions/traversals passed.
- Actual staged Vellexia candidate: 245 focused assertions/traversals passed, including the played eight-visit predecessor chain and open echo.
- Historical grief remains available in `kiana.former_grief` with required Elan death.
- `jerribeth.refuge` remains available with required patron loss.
- `konomi.private_absence` stops if the native office premise changes or its completed-office requirement disappears.
- Jerribeth's invitation stops on native unavailability while preserving authored closure, completion and the existing entry override.
- The actually delayed `jerribeth.question` confirms that continuation does not restart an entry delay.
- `seelah.fate_life` permits the required target death and stops on unrelated unavailability or loss of current Trickster/recovery availability.
- `ember.ending_dead` does not inherit a living-contact requirement.
- `konomi.margin` still stops and resumes with physical contact loss and restoration.
- Owned-file `git diff --check` passed.

The permanent `Run` executes the Vellexia witness only when the actual staged campaign scene exists in its supplied Story.
The current export does not contain that draft, and the test does not fabricate a substitute scene.
The other fixtures construct minimal valid snapshots; only the Vellexia reproduction walks the complete listed predecessors.
These tests do not execute Unity UI, save/load, `Main.State` against a live player, or native quest transitions.
The transformation fixture supplies the composite that inspected `Main.State` produces; it does not perform a live mythic transformation.
The parent must register the permanent suite, rebuild the production assembly and run the managed construction and shared Rules checks before calling the integrated repair verified.

## Released hashes

| Artifact | SHA-256 |
| --- | --- |
| `src/Story.cs` | `63F86A28776E2006589E688A2BABDD9F88D118945618FD1507B9B45701FD3D99` |
| `tests/RemoteContinuationTests.cs` | `0D9A89192EAF96BCED38F2A480A4603C7CD95951C13877E60CF4B724BB41BAB6` |
| Original `Story.cs` | `81C3E0890703040BE91046A3B2C708B286471B77715FDD9882A4A75B62082771` |
| Current export | `20C417875617D4217F73855BCF37121C400C81209A68316FF1F0CC5E969719B0` |
| Staged Vellexia candidate | `94B125A525514652231D6E5C14F91E580C9BA7EE0C4D1270B7C51A64BC288E41` |
| Inspected parent `src/Main.cs` | `347D2906096AE0F0C3596F359E1B5523DC64E8C89AB38F1B912A45BE5CAF67FD` |
| Inspected parent managed `Program.cs` | `B5DAE58530455E9CE594573FFB20A450EFA13D09F7374397CB9B9CAE3143C5B0` |

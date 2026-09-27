# Nurah integration independent review

Review date: 2026-09-27.

Scope: current Main wiring, authored story hub contract, Nurah placement/click helpers, their managed fixtures, and the Nurah story import.

Verdict: pass for the bounded managed blueprint construction and hub-graph integration described below.

This review does not certify an in-game route, arrival, save/load behavior, ToyBox behavior, or final route readiness.

## Reproduced headless construction

I independently ran the managed construction executable with the installed game directory, current `development/Story.json`, direct Python interpreter, and the three documented parent-binding manifests.

The run passed 83,251 assertions and constructed the actual `Main.Build` graph for 625 scenes and 22,592 generated blueprints.

The exact production DLL SHA256 was `FD2B05CED75F374AEC7C6F24FFD9A5ADB32F2C617A452337EDBBCCA3E3B0FAF9`.

The exact story export SHA256 was `FC618CBBA77AB3895324BF8FC05F7E9773935BF5D84FE11A4F651E52868F560E`.

The runner itself reports that it does not execute parent-mod initialization, the campaign's full condition graph, Unity page rendering, ToyBox, or a game save round trip.

The test emitted the expected native resurrection fixture boundary exception and explicitly records it as a fixture limitation, not as a failing assertion.

## Verified integration behavior

The import deep-copies the 13 Nurah scenes, marks the 11 physical scenes with `InteractionHub="nurah.arrival"`, and leaves the two correspondence scenes remote.

Story validation requires each physical Nurah scene to use the exact hub key, Nurah relationship and owner, retained capital unit, Chapter 5 and Drezen area, accepted-meeting and verified-arrival prerequisites, and no native answer list.

The managed `Main.Build` test confirms it constructs a repeatable Book dialog with a greeting, one distinct answer per physical scene, and an exit answer.

For all 11 scene answers, the test verifies visibility and selection are guarded by the corresponding `RouteCondition`, and the action queues the matching physical scene.

The remote introduction remains detached from the physical interaction hub and does not acquire a contact-unit gate.

The stable parent-generated Friedhelm callback cues now enter through a distinct typed parent-source fixture manifest instead of being incorrectly required in base-game `blueprints.zip`.

The actual callback mappings are supported by `NuraBook05Page002.Configure`: its show-once cues are created as `BlueprintCue` objects under the parent builder before this mod's ordered Main build postfix.

The `SeenCues` mapping is therefore a valid parent-runtime history observation, while the test honestly does not execute the parent initializer.

The headless suite also verifies route answer-list preservation, generated dialog/page/choice references, scene guards and action ownership, contact bindings, idempotent construction, and the parent sequence sentinel contract.

The click helper's separate 38-assertion suite exercises native selector arbitration, equal-priority ambiguity, exact interaction ownership and removal, current actor/Commander identity, changed availability, and callback failures.

The meeting suite exercises retained-actor evidence, accepted romance/finale/personality history, current prison/death exclusions, conflicting-group arbitration, saved placement protocol, explicit retry identity, and its loading/unloading guard fixtures.

These checks support the source-level wiring claims; they do not show an interaction or arrival in the running game.

## Remaining verification gaps

The integrated test inspects the generated hub answer graph but does not invoke `Main.RouteAction.Start` through `Queue`, wait for the old dialog to close, execute `Main.Update`, and verify that the corresponding physical dialog actually begins.

It verifies the click helper with an injected start delegate, not the real `DialogController.StartDialogWithUnit` call or rendered book page, portrait, and camera behavior.

The suite tests the request timestamp helper with synthetic values and tests placement using detached state fixtures, but does not play the remote acceptance and withdrawal choices and then observe a real accepted appointment across saved-game reload.

No test evaluates `CurrentNurahVisit`, `NurahVisitWindow`, `CanOpenNurahHub`, or the full `Rules.Available` gate against a live `Game`, retained capital actor view, live area, and running EtudesSystem.

The fixture tests do not establish that the real Drezen anchor is walkable and clear in an installed save, that the native HideUnit and TranslocateUnit actions succeed, or that the actor remains interactable after area unload/reload.

The cached parent cue fixture is type/provenance evidence only; it does not prove that the parent builder ran successfully in the target installation, although the Harmony ordering and parent Configure call chain are source-supported.

No concurrent ToyBox Free Love and Jealousy Begone run, complete chronological route playthrough, or art/rendering check is included.

## Disposition

I found no confirmed static integration defect in the hub graph, generated scene linkage, or the bounded placement and click helper behavior.

The next decisive check is a focused Unity playthrough of invitation acceptance, actual Nurah placement and click, hub-to-scene queue transition, then save/load and return to Drezen with the intended ToyBox settings enabled.

Until that check succeeds, describe this as headless-construction verified, not in-game ready.

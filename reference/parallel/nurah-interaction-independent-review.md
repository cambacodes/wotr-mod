# Nurah click interaction independent review

Date: 2026-09-27.

Reviewed production source `src/NurahInteraction.cs`, SHA256 `6F7B6B331DF3B9F88C0EB84711DBBC64A91A4B06FAC1A072B2D2C220677712BE`.

Reviewed test source `managed-tests/NurahInteractionTests.cs`, SHA256 `DD279C10ED9C5702A2056E65D492F8D85117D6688A3FCD67C6D453092E8FE408`.

The review verdict is **revision required** because the helper can attach a third click interaction when native development-mode arbitration returns `null` for two existing equal-priority interactions.

The rest of the bounded helper behavior is well guarded, but this conflict path needs to fail closed before the implementation can pass independent review.

## Verified behavior

`Tick` observes the actor from `NurahMeeting.ArrivedActor`, observes the current `Game.Instance.Player.MainCharacter.Value`, and requires `canOpen()` before attachment.

It stores the exact actor, Commander and `UnitPartInteractions` object and withdraws when any identity changes, arrival is lost, route availability fails, interactions are disabled, or an exception occurs.

`Withdraw` removes only the helper's own `Click` object from its remembered part, then clears its transient ownership fields.

The current click requires reference equality for the initiator/Commander and target/arrived actor, rechecks route state, arrival, part identity and interaction enablement at selection and click time, and returns `Fail` on stale state or exceptions.

The click forwards the configured greeting, exact target and exact Commander to its injected start callback.

The helper assigns native priority `EtudeBracket` (200), above `Spawner` (100), but separately refuses attachment whenever native selection returns any available click interaction.

That refusal preserves a currently available lower-priority Spawner instead of allowing the higher-priority addon click to displace it.

The relevant native selector and ownership implementation was checked in `reference/art-review/UnitPartInteractions.cs`, SHA256 `6B1C6C9CC15DA33A3662AED7CD1209712D8929A72578523D56640BD633BE1DC6`.

`AddInteraction` inserts at the front, `RemoveInteraction` removes by object identity through the list, and the selector chooses the available non-approach interaction with the greatest priority.

## Exact suite and targeted edge probe

I built the production project successfully with zero warnings and zero errors.

The resulting development DLL was SHA256 `4EDF8388B63D66A40B295AB9674FC43C5233D248E6A3222BE7DE8627537FCB6B`.

I compiled and ran the frozen test source in an isolated temporary `net48` harness against that DLL and the installed game assemblies.

The exact test source passed all 32 assertions.

The tests exercise the real `UnitPartInteractions` object and selector, but substitute arrived-actor/Commander/hub observations and the dialogue start callback.

The frozen suite transpiles native `BuildModeUtility.IsDevelopment` to false to avoid the game's Unity-backed diagnostic path, so it does not cover the ambiguous development-mode selector result.

For the requested adversarial probe, I made a temporary test-only copy of the suite that forced the selector's development-mode branch and suppressed only its Unity-backed `ErrorWithReport` log sink.

The rest of `SelectClickInteraction` and the production helper were unchanged.

With two available native `EtudeBracket` interactions, the actual selector returned `null` before `Tick`, matching its development-mode ambiguity behavior.

`Tick` treated that `null` as no competing interaction and attached the addon click, making three available interactions of priority 200.

The selector then returned `null` again for the three-way tie, so the probe did not start the greeting, but the addon had increased an already-invalid native interaction state and produced another tie condition.

The temporary adversarial suite passed 35 assertions, including assertions for the native `null`, unexpected third attachment, and continued absence of a selected click.

The temporary modified test copy was SHA256 `B7762364AB577A028FB867AAA125551CFE3D42F520EA006A673C398BE064FE0E` at `C:/Users/Z/AppData/Local/Temp/nurah-interaction-audit/NurahInteractionTests.cs`.

This is the false-negative in `HasOtherInteraction`: its boolean result conflates “no available native click” with “native selector rejected an ambiguous equal-priority set.”

The test currently has no case for two available native equal-priority interactions, so the frozen 32-pass result does not catch the issue.

The canonical `managed-tests/Program.cs` currently calls `NurahMeetingTests.Run(Check)` but does not call `NurahInteractionTests.Run(Check)`.

Thus the interaction suite is not currently part of the normal managed test executable, even though it compiles as a project source file.

## Required disposition and boundaries

Before approval, change arbitration so a null native selection is not treated as proof that there is no other available click when the native list contains an ambiguous equal-priority set.

Add a regression case with two available native EtudeBracket interactions; assert the addon does not attach and the original entries remain untouched.

Retain the existing Spawner test, which verifies that the available lower-priority native click remains selected and is not removed.

Register this suite in the canonical managed runner after resolving its expected game logger or headless diagnostic behavior, so ordinary headless verification actually executes it.

No Main registration, authored hub construction, lifecycle scheduling, real game arrival, save/load behavior, Unity rendering, or user-facing dialogue presentation is reviewed here.

The callback tests do not prove that `Game.Instance.DialogController.StartDialogWithUnit` renders a greeting in a running game.

This report approves no route, art, manuscript, physical placement, or live ToyBox behavior.

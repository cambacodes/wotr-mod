# Nurah physical dialogue entry audit

Audited 2026-09-27 against the installed native assets and RanRomance 0.1.11.
Verdict: no suitable existing dialogue attachment is established for the released Chapter 5 capital actor.
The warcamp and prison answer lists must not be adopted as a shortcut.
A scoped authored private-visit greeting and interaction is the smallest credible entry mechanism supported by the evidence.
This is a source recommendation, not an implemented interaction or proof of playable arrival.

## Exact actor and interaction evidence

The retained capital actor is blueprint `f999fc37ddb225640b7f98c0a05d6948`, spawned by `c2b298fc-d794-4995-8b49-822b75c3bb62` in capital default mechanics scene `3e2b5ea054cd5b2479e7f13134363ef4`.
Its native blueprint record is `Units/NPC/Unique/Act_3_DemonsHerecy/Drezen/NurahCapital.jbp`.
The record links prototype `c44d5c157091e7e46af1f11a4c79303d` but contains no `DialogOnClick` or other unit interaction component.
Its serialized component array contains loot, class levels, experience, and caster behavior.
A prototype relationship does not import a different scene spawner's click component.

The capital scene object has its transform, unit spawner, and hidden/optimization component.
It has no `SpawnerInteractionDialog` or serialized dialogue reference.
The spawner starts hidden, does not respawn if dead, and names the capital blueprint above.
The actor prefab is `c8ec90242dcde1d41aeb8cbe641a8605`, resolved to the actual installed `.unit` bundle.
Fresh extraction of its GameObject, MonoBehaviour, and MonoScript records found no serialized dialogue link.
These findings do not exclude interactions dynamically installed by unrelated mods or retained in a particular save.

The scoped fresh native archive reference scan covered `World/Etudes`, `World/Dialogs`, `World/Cutscenes`, and `Units` for the exact capital spawner, capital unit, and both candidate dialogue identifiers.
Outside dialogue records, it found the capital blueprint, capital killing mechanism, default hidden actor etude, and prison placement etude.
It found no released Chapter 5 capital greeting installer in that scope.

## Candidate menus

| Candidate | Exact asset | Finding |
| --- | --- | --- |
| Warcamp dialogue | `676aa4a0636e7004294e8d2a6f9db209` | Attached to a different native scene spawner. |
| Warcamp common answers | `16ccf8f56019e2c4f92b1caec3864b5d` | Parent patches this list for its early romance, but that does not attach it to the capital actor. |
| Prison dialogue | `b8315f57179a6584ebf40d110b517352` | Installed by the prison etude bracket, not a permanent released-actor default. |
| Prison common answers | `01d00f006e0e16543b7507ff38e9fb8a` | Prison interrogation context and not the only possible prison greeting's list. |

Fresh `warcamp_defaultpeaceful.scenes` extraction shows `SpawnerInteractionDialog` with warcamp dialogue `676aa4...` on spawner `44351b2c-356c-49a5-9f57-a75cbd02b4e4`.
That spawner creates original actor blueprint `c44d5c157091e7e46af1f11a4c79303d`.
It is not the retained capital spawner.
The warcamp opening cues `8e82eba71e6a73245b82b6b5a6731803` and `7eeb56466ce63e0439194cd6a7067e1a` present Nurah's helpful historian persona and lead to `16ccf8...`.
The surrounding menu includes her earlier sabotage denials and early campaign questions.
Forcing this greeting onto her later private visit would reset the dramatic context even if an appended addon answer became technically reachable.

Native prison placement etude `21a061de3610732438072d2b975b6f43` has parent prison etude `c922e0cbe25a0cf4dad4ce7a3ca81935`.
It excludes the relevant death/escape histories and Chapter 5, claims Nurah's actor group, and installs `EtudeBracketOverrideDialog` against the exact capital spawner.
Its Chapter 3 play action unhides and moves her to the prison locator.
The override points to `b8315...`.

Prison dialogue first tries `ea5213ee84e1f534e87eb2f193811c6c`, conditional on alliance etude `a879a3a637a7eeb43b40677e4a8c4450`.
That greeting describes her on a prison bunk asking for release and uses answers `6201570ac1b1d8c4b878f935a7b0160e`, not candidate `01d00f...`.
The fallback `255504a2d643baa468d17bcc0bdee9a3` is a hostile prisoner greeting leading to `01d00f...`.
Neither greeting describes a voluntary private-chambers appointment.
The dialogue also contains native quest/history effects, so it must not be repurposed by clearing its answers or bypassing its original flow.

## Parent modifications do not supply the missing contact

The reviewed installed parent `RanRomance.Nura.Main.Configure` clears and rebuilds warcamp answers `16ccf8...`, retaining native entries and inserting its Chapter 2 flirt conversations.
The retained Nura source also patches early cue continuations and creates separate book events.
Those changes provide no source-verified released capital click installer.
The parent romance/finale evidence required by the movement helper therefore does not imply that the freed capital actor inherits the warcamp dialogue.
The previous parent source audit and its retained decompilation pins remain applicable.
This conclusion does not claim exhaustive compatibility with every other installed or future mod.

## Native click and bracket semantics

Fresh native decompilation is retained with the extraction evidence.
`UnitPartInteractions.SetupBlueprintInteractions` reads actual `UnitInteractionComponent` instances from the unit blueprint.
`SpawnerInteractionDialog` separately starts the dialogue configured on its own scene component.
Neither mechanism discovers a suitable dialogue merely from a character's name or prototype's scene history.

`EtudeBracketOverrideDialog.OnEnter` adds an interaction to the evaluated unit, `OnExit` removes that interaction, and `OnResume` adds it again.
Its `Interact` starts the supplied dialogue with the target and user.
Thus the native prison override is temporary and does not establish a surviving released greeting after bracket exit.

The wrapper `EtudeBracketOverrideUnitInteraction.IsAvailable` returns true unconditionally.
Simply adding the native override component to the appointment etude would therefore expose its interaction before this helper proves physical arrival, unless installation and every click are gated separately.
`UnitPartInteractions` gives etude interactions priority 200 and spawner interactions priority 100.
Two simultaneously available interactions at the same priority also trigger a development-mode conflict check.
An addon must not silently shadow or delete an unknown current interaction.

`NativeContact.IsAvailable` proves observed actor presence and usable view, not the existence of a click dialogue.
Movement arrival and dialogue entry are separate requirements.

## Recommended bounded implementation

Create one authored private-visit greeting and answer hub with stable addon-owned identifiers and localization keys.
The greeting should acknowledge the current appointment without replaying imprisonment or the warcamp deception.
Offer only presently eligible authored visit scenes plus an ordinary goodbye.
Keep every native/parent dialogue, answer list, action, condition, and history intact.

Install a transient interaction on the exact retained actor only under the appointment's ownership and verified arrival.
Reuse native `UnitPartInteractions` and normal `StartDialogWithUnit` behavior.
A small gated interaction should revalidate the target identity, current consent/episode, claim ownership, actor contact, and helper arrival both for availability and immediately before starting the authored dialogue.
Do not rely on the native wrapper's unconditional availability.
Remove only the addon-owned interaction on withdrawal, failure, claim loss, disable, or disposal, and rebuild it from current evidence after load.
Preserve any preexisting interactions and defer if an unknown current interaction would compete.

The current `Rules.EntryTargets` accepts explicit answer lists or the existing Tirabade defaults, then throws for a physical Nurah scene with neither.
Current Main resolves these external targets before constructing scene blueprints.
The authored hub therefore needs an explicit, narrowly typed construction/attachment path before those lookups, or a separate reviewed direct dispatch path.
Do not invent a native GUID, attach to an unrelated list, or relabel physical visits remote just to pass validation.
No new identifier is proposed as if it were a discovered native asset in this audit.

## Verification required before delivery

Verify actual authored hub registration and all physical scene entry bindings during Main.Build.
Exercise actor click selection with no appointment, accepted-but-not-arrived state, successful arrival, partial unhide failure, competing native/unknown interaction, consent withdrawal, and reload.
Every rejected state must leave native interactions and quest/history actions unchanged.
Successful click must reach the authored greeting and correct available scene, with no prison or warcamp greeting first.
Test that goodbye and scene completion return control without restarting native book events or leaving duplicate interactions.
Finally verify the retained actor is visibly clickable in a real save at the approved private visitor location.
The movement stage remains separately verification-required under `nurah-meeting-movement-independent-review.md`.

## Evidence locations and pins

Fresh temporary extraction scripts and results are in `C:/Users/Z/AppData/Local/Temp/nurah-dialogue-entry-independent/`.
They include `prefab.json`, `native.json`, `references.json`, `warcamp.json`, localized `dialogues.txt`, and the native interaction decompilations.
Capital scene extraction is also retained in `C:/Users/Z/AppData/Local/Temp/nurah-extension-audit-3y60fthx/nurah-spawner-scene.json`.

| Installed input | SHA256 |
| --- | --- |
| `Assembly-CSharp.dll` | `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953` |
| `RanRomance.dll` | `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68` |
| Capital default mechanics bundle | `D451FEF29C6B22F5D13E8BACEA70BA063175DDEE8B3F43F48D6CAE7F22B4A9E3` |
| Nurah unit prefab bundle | `6D1B6A0B5F575157A9398F5A152FBD1DB0BD7AACA335964A0978B0E2C8897795` |
| Warcamp default peaceful bundle | `2FC54A697A7924551D934BAB7CE7D07436DF24AC7AB2BE2D8CDCA0A6F86BD54B` |

No runtime, manuscript, binding registry, generated story, or native asset was changed.

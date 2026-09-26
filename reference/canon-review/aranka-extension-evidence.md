# Aranka continuation source evidence

This report supports a living Chapter 5 island continuation of an earned RanRomance relationship.
It does not establish universal island access, a new romance acquisition, or a current Drezen actor.
Research and authoring were performed on 2026-09-26.

## Installed sources and configured amount

Installed `RanRomance.dll` SHA-256 is `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
Installed `LocalizedStrings.json` SHA-256 is `534D49567F0172193CD78F9C56A7A9A8244021F1701E2EC46F0C04FDBFBBCF3F`.
Both were hashed again and match the retained IL inventory inputs.
I reran the computation in `reference/art-review/route-inventory.py` without its output-writing section, using the retained installed-DLL method/call inventory.
The Aranka initializer reaches 112 methods and 440 configured localization keys, containing 16,556 keyed words and 15,758 distinct normalized-text words.
These counts follow configuration calls, not arbitrary references whose activation was never established.
They include alternate dialogue, journal text, epilogues and configured related helpers; they are not a selected playthrough length.
They do not establish a literary score or guarantee every configured branch is attainable in the same save.

I read the retained class-specific decompilations and installed localization, and freshly decompiled `RanRomance.Aran.AranBook04End` and `RanRomance.Aran.AranBook14End` from the installed DLL to cross-check endpoint identities.
The namespace-only `aranka-installed.cs` is an unsuccessful decompilation and is not evidence of configured content.
The existing `aranka-integration.md` remains useful context but its simple Book04 endpoint summary needed expansion for the alternate Azata ending.

## Parent relationship and finale predicates

| Extension alias | Object and GUID | Read meaning |
| --- | --- | --- |
| `aranka.ran_romance` | BlueprintEtude `2e98dbe685f045cdabf88b66e4cde9ff` | Existing Aranka romance Playing now. |
| `aranka.ran_reverie_partner` | BlueprintEtude `d4dd8a50613e4d528913d0a24d06fca1` | Existing accepted Reverie partnership Playing now. |
| `aranka.ran_quest_complete` | BlueprintQuest `1dacd3dfe1bf47c8a73074814e40b1c8` | Successful parent quest completion, independently required alongside an endpoint. |
| `aranka.ran_failure` | BlueprintCue `b18d250fa2fb4fdf9fe4eba04e9d1655` | Book03 failure cue seen, blocks this continuation. |
| `aranka.devil_deception` | BlueprintEtude `0b129925567b68d4fb712b4bee6c0f9a` | Native deception history Playing, excluded. |
| `aranka.devil_contract` | BlueprintEtude `5f72b252bd7fa8d48bd04c27982a4f9c` | Native contract history Playing, excluded. |

`RanRomance.Aran.Main.Configure` defines the romance etude and increments the parent's `RanRomCount` on play, decrementing it on completion.
The extension never starts or completes that etude, adjusts the count, or gives parent objectives.
Flirt, Active, confidence, and another partner's etude are not substitutes for the current romance.

Relevant parent code excerpts are:

```csharp
EtudeConfigurator.New("RanRomAranRomance", "2e98dbe685f045cdabf88b66e4cde9ff")
EtudeConfigurator.New("RanRomAranAlurRomance", "d4dd8a50613e4d528913d0a24d06fca1")
// AranBook04 finish actions:
.SetObjectiveStatus("RanRomAranQuestEntry0003", null, (ObjectiveStatus)0)
// AranBook14 finish actions:
.SetObjectiveStatus("RanRomAranQuestEntry0004", null, (ObjectiveStatus)0)
```

`AranQuest.Configure` sets both Entry0003 `b968d14237b94e60af8f01f84f42dcda` and Entry0004 `d1e371f09017417b98b0aed58f3ab6ac` to `SetFinishParent()`.
The hidden failure objective also finishes the parent, so success and a real ending must both be required.
Seeing the dialog start alone is insufficient.

`aranka.ran_keep_final` reads any of these terminal cues:

| Parent page | Terminal cue | Meaning |
| --- | --- | --- |
| AranBook04End | `a16f4be6de0a4f35a9b13eca4395d6e5` | Reverie's ritual takes her and Aranka away, and the Commander wakes from the dream. |
| AranBook04Azata | `61461d05999b46218e7700e6596243b5` | Existing shared-partner first flight and return from the dream. |
| AranBook04Azata | `363860bffda1404db6ec996384fe2f26` | Existing Aranka romance's first flight and return from the dream. |
| AranBook04Azata | `43936228f4614272a7c7e25ebaaec2c7` | Alternate non-romance first-flight ending; current romance is still independently required. |

The three Azata cues also form the narrower `aranka.ran_wing_dream` alias.
Book04Page008 can lead directly to AranBook04Azata instead of the ordinary End page.
Using only the ordinary End would incorrectly exclude a natural Azata route to this island continuation.
The earlier transformation cue `22bd10fea4714daa8c4ac984041545d6` is not an endpoint and is not used as proof of a completed finale.
The new callback requires a completed flight ending and describes dream wings, not proven waking anatomy.

`aranka.ran_release_final` reads any of the four AranBook14End cues:

```text
599e7c0cc51741cda1bc55b787734c57
fefc9911dde04a76975e9027118c7935
f9df40d7d6b346298075b435eee6921c
e16e5b0b3aea426a888e8bb61c521815
```

Their parent conditions distinguish no special answer, rejection answer `9a573464ef1e475ab1f87ad7e3411ca9`, postponed picnic answer `9da942e417684d0d8729f63f94733d4d`, and accepted picnic answer `e87a7d4a200d41d7bcff127534e885d6`.
The accepted picnic leads through Page004 to its kiss and then the intimate ending; the condition itself reads the earlier picnic acceptance.
Current romance remains mandatory, so a rejected relationship does not become a new romance merely because its ending was seen.
Book14 explicitly relinquishes the compass and does not establish ongoing dream access.
The new source acknowledges that choice and never returns the artifact or restores its ability.
An overlapping endpoint history uses relinquishment wording conservatively and hides the wing and Reverie callbacks.

Book02 is a Chapter 3 rest development, Book03 is Chapter 4, and the parent finales follow Chapter 5 mythic progression.
The extension is restricted to Chapter 5.
It adds no earlier acquisition shortcut and preserves the parent's Azata entry and later path restrictions.
The defined `RanRomAranWarden` etude `77f1192d6ff8428389351c7ef02c2bfc` has no verified start producer in the inspected Aran classes, so it is not an extension prerequisite.

## Actual local contact

I reopened these native records directly from installed `blueprints.zip`:

| Native object | GUID or scene reference | Observed use |
| --- | --- | --- |
| AzataIsland area | `31bab5549f7ea384186159a238360c8d` | The extension's exact allowed area. |
| Azata_Aranka_DesnaPriest unit | `430cba7801b149b4e8494ace6baf4f7c` | Native island Aranka, prototype `b85fdd8481f26f54f9c504fc4d2e031f`. |
| DesnaAdepts_Azataisland_dialog | `ea9f80fde3f30f64b9f3bda0601c63d4` | Repeatable native dialogue with empty conditions and a random greeting selection. |
| AnswersList_0008 | `5ff8a80442182f84e849b4281f98b9ca` | Empty conditions, ShowOnce false, reused by the installed AranChpt03Dial001 extension. |
| AzataIsland_DefaultMechanics etude | `a640f861f23368e4e90db87271e58924` | Linked to the island and adds mechanics `11e4833d74399094b9b8293df0ec95e4`. |
| Added island mechanics | `11e4833d74399094b9b8293df0ec95e4` | Loads scene `2a7dc000fe2245349be70cff569dc48f`. |

The native greeting Cue_0005 `2c84efa67859baa4bba26dcc43d1149b` names the exact island Aranka as speaker.
Cue_0001 `d14acdcc34883c84db898d085ce7d3f8` exposes the shared answer list while another Desnan speaks.
Therefore answer-list attachment alone is not proof of Aranka's presence.
Every new scene also requires the exact live unit through `ContactUnit`, in the exact island area, on entry and continuation.

The mechanics parent chain runs through AzataIsland `c126d9f1957ee3a4b9aa73c6a3e5cf4e` beneath PlayerIsAzata.
PlayerIsAzata `d3b47e973d65c6c46af1cce815d1f6ce` has actual mythic-class activation conditions.
This supports a native island context, not a claim that every former Azata, Legend, or Trickster can reach it.
Chapter 5 AzataMentorCome_C05_Mechanics `5c701301b3e12ea49b298ba6721b72c4` explicitly moves the island Aranka spawner `0edec23e-6de1-46d1-8e9e-ee28c22a41aa` in that mechanics scene to ArankaLoc `4467fc15-1c3d-4d93-ab8d-d073204e83ab`.
This verifies a Chapter 5 native island actor reference, not survival or availability after every confrontation outcome.

Capital ArankaDesnaPriest_DefaultActor `547921e48f8f2ac42b6a79be55ba6b2d` actually applies `HideUnit` with `Unhide=false` to the capital spawner.
It is deliberately unused.
No pet, proxy, cloned actor, corpse cleanup, or new spawn is introduced.
The broad named massacre/fear unlockable flags are not guessed into comprehensive Aranka death aliases.
Actual hidden, absent, dead, unconscious or hostile units must fail the shared contact adapter's existing live-unit requirements.
Unity traversal, native spawn timing, and the answer-list insertion on a real Chapter 5 save still need verification.

## Character and new fiction

Native DesnaAdepts Cue_0022 `091e0386df4207a4c8cd5eab0910bc29` establishes her family's support for travel and her work refining her art.
Cue_0005 supports practical singing instruction, and Cue_0034 `06752003a64374741804b8ca89ac90f8` says she can sing for clouds and wind without a city audience.
MusicVsMusic Cue_0001 `b76b67f369adfd44fa4fb85f4d47ff4d` combines devotion to Desna with opposition to blind obedience.
Cues_0014, 0015 and 0017 distinguish creating their own music and a shared symbol from simply using a powerful religious relic.
Those native texts were resolved against installed English localization.

The new Sella, Rovan, Neris, Deren, swallow refrain, rehearsal, disputed verse, listeners and private evening are authored alternate developments.
They are dialogue encounters rather than new engine-spawned NPCs, inventory, timed performances or healing effects.
Rovan's damaged singing voice is not cured by a romance reward.
The new song does not replace Starward Gaze, alter its existing musical choice, or grant a buff.
Current Aranka romance supports adult non-graphic intimacy without replaying courtship acquisition.
The inherited Reverie partnership is acknowledged only when its real parent state is Playing and the retained-artifact ending is supported.
The optional Kiana rehearsal remains unapproved reference material and contributes no text or claimed relationship here.

## Required integration and remaining scope

The module exports `SCENES`, `ETUDES`, `SEEN_CUES`, `COMPLETED_QUESTS`, and `RELATIONSHIP` for parent-owned integration.
Its relationship entry describes extension progress and does not duplicate the parent's quest objectives or change its romance count.
New portrait key `Aranka` should reuse verified parent-compatible Aranka art; this task does not deliver or approve a new image.
The new source writes authored extension outcomes only.

A bespoke attainable Trickster acquisition/contact path remains required future work.
This continuation does not satisfy that requirement through a historical alias, a new island actor, or a silent exemption from the native island mechanics.
Other inaccessible histories, resurrection, alternate safe contact, whole-route quality review, art review, and actual game verification remain outstanding.

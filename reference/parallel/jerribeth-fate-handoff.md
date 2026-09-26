# Jerribeth living-contact fate contribution

Released for private staging and independent review on 2026-09-25.
This is a bounded Trickster opportunity at a verified living native contact, followed by a played letter consequence.
It does not complete universal Trickster recovery after death, hostility, despawn or a missed encounter.
No existing story source, expansion assembly, Program registration, engine file, export or installed mod was edited by this author.

## Files

| File | SHA256 at release |
| --- | --- |
| `storylines/jerribeth_fate.py` | `588E2979EE7031E8001AA6200E965F5D0E095BB6587E09D09FF7182685F1F795` |
| `tests/JerribethFateTests.cs` | `7252B822C47FA34C2B20B6DA33980AAD0E9DA6630A381A57B88F2933C2F79E04` |

`reference/canon-review/jerribeth-fate-native-evidence.md` records the directly inspected archive, Unity bundle, blueprint and spawner evidence.
The new module contains 1,519 distinct-segment words, with 1,280 prose words and 239 choice words across two scenes.
That is contribution volume, not a new full-route review or an independent quality score.

## Playable design and native hook

`jerribeth.fate_envelope` is an Act 4 physical scene attached to the actual Jerribeth answer list `19786fae9c29f9d439e374bb857c2e84`.
It requires the current Trickster path, the existing native refuge explanation and an observed available actor of blueprint `417ce3dcf3a9707488f2b9b2a790814b`.
Its containing area is Upper City, `8217b05e37078414981d994151f0ffb1`, whose parts include VellexiaPlace.
Both current chapter and actor presence are checked by the existing ContactUnit mechanism.
The proposal forbids authored closure, Jerribeth's native unavailability, and the patron_lost state.

The Commander folds an invitation around a future quiet evening rather than a known address.
Jerribeth tests the paper, changes what she has written, and can refuse when the Commander asks for an irrevocable answer.
That refusal completes only the experiment and does not close ordinary courtship.
Acceptance asks either about her own work or about a private evening, and grants only the matching question history and fate_note_prepared.
No attraction, lover, commitment, restoration or native meeting flag is written.
Her native protection, patronage, victims and allegiances remain what the game established.

`jerribeth.fate_letter` becomes available after 24 hours at a quiet rest in the Nexus or Drezen, in Act 4 or 5.
The letter answers the selected question and invites an actual reply from the Commander.
Reading it can be postponed without recording an answer.
A completed reading sets fate_note_read and leaves the ordinary correspondence invitation as a separate decision.
Existing correspondence histories receive a distinct ending which acknowledges the frame already accepted, without replaying that invitation.

The letter can arrive after the native actor has departed or after the Commander changes mythic path, because the experiment was prepared while the required contact and Trickster power were present.
It cannot be newly prepared by another mythic path.
Native unavailability and authored relationship closure still block delivery.
The letter does not summon Jerribeth, locate her current body, preserve her as a companion, or certify that she has survived an unsupported edited history.

## Required parent integration

Append `jerribeth_fate.SCENES` to the reviewed payload and then call `jerribeth_fate.integrate(payload)`.
The overlay changes only the existing original invitation's metadata.
It adds fate_note_prepared to its authored forbids and narrowly overrides that forbid when fate_note_read is present.
An unplayed ordinary invitation therefore waits for the chosen experiment's consequence.
If the original invitation is already completed, its ordinary scene-completion exclusion continues to prevent replay.
An ordinary route with no fate_note_prepared flag is unaffected, including other mythic paths.

The overlay is idempotent and checks that both new scenes and the original invitation exist.
The parent should use the copied expansion payload, as its existing builder already does.
No new native flag binding or shared-engine feature is needed for this bounded version.
Register `JerribethFateTests.Run(story, Check)` only when these scenes are present.

INTEGRATION_REQUIREMENTS records that this contribution is not yet integrated or runtime-verified at author release.
It is documentation, not an engine predicate and not a hidden shortcut around the contact checks.

## Evidence and engine dependencies

The default-house native dialog has empty finish and replacement action lists.
Its answer list is shared by the greeting, warning and ordinary questions, including the existing refuge explanation.
The primary native-entry opportunity is to ask about her situation and choose the new answer during that conversation.
The original dialog is not indefinitely repeatable; its ConditionsHolder permits first contact or the third-date warning window.
The new source does not patch those native conditions.
The mod's manual Read option is separate authored delivery, still gated by a living actor in the correct area and chapter.
Do not describe that manual access as a native dialog reappearing.

The installed scene bundles establish both Act 4 spawners, rather than merely suggesting them through a blueprint filename.
Default-house and third-date spawners use the same base unit and distinct scene IDs.
Actual runtime overlap must be checked because NativeContact currently counts blueprint matches before removing hidden or unavailable matches.
The same concern is concrete in the Sanctum, whose entrance and final-room spawners share another blueprint and whose departure scripts hide the units.
This contribution deliberately does not claim a reliable Sanctum restoration or reverse those scripts.

The existing Seelah revival mechanism searches retained player companions and verifies their saved identity.
Jerribeth's scene-local NPC despawn is not that case.
A later universal recovery implementation needs independent entity provenance, spawn/hostility/death reconciliation, persistence and an explicit voluntary encounter.
Clearing jerribeth.unavailable or creating a permission flag would not implement it.

The fate effect here is narrated and played through book-scene choices, like other authored events.
No item is added to physical inventory, no clock is changed and no new visual effect is spawned.
The code implements the new contact decision, its delayed consequence and the preserved choice to begin ordinary correspondence.
Do not describe it as a newly implemented native teleport, resurrection or world-state rewrite.

## Verification completed and pending

Both scene dictionaries import successfully and have valid unique node IDs and direct targets.
A source-only walkthrough reached every new page with both question histories and new versus existing correspondence.
It preserved relationship and unrelated romance flags.
The copied-payload overlay was checked for idempotence and did not mutate the imported original source dictionaries.

The delivered focused C# tests exercise actual Rules.Available and Rules.ContactAvailable, native entry GUIDs, chapter and area restrictions, required knowledge and Trickster status, fake actor flags, missing actor continuation, death/hostility and closure blockers, both refusal and acceptance, both letter questions, 24-hour timing, later chapter/mythic change, patron loss, existing invitation timestamps, ordinary invitation acceptance/rejection, and unaffected other-mythic access.
They also check that a prepared letter takes priority over an unplayed ordinary invitation in the route's automatic rest queue.
The test simulates AvailableContacts supplied by the engine; it does not inspect a living Unity entity or validate native condition evaluation by itself.
No C# pass is claimed before the parent runs the staged suite.

Before promotion, verify the typed bindings, managed entry and continuation construction, actual native option after the refuge cue, contact uniqueness in both manor phases, and saved-game behavior.
The parent owns those staging and shared-engine checks.
Independent literary and technical review remain required.

## Separate blocking ending issue found during research

While inspecting physical entry construction, I found that the existing Main.BuildScene epilogue branch creates an unconditional Continue and skips authored node choices and transitions.
That makes multi-node authored ending branches, including the preceding Jerribeth progression contribution, insufficiently represented by the real managed construction despite Rules.Walk passing them.
The parent confirmed the defect and took ownership of its fix and managed tests.
Assembled branching endings must not be called verified until that engine defect is corrected and the actual constructed transitions and conditions pass.
This fate contribution does not edit or conceal that dependency.

## Correction to earlier native shorthand

The actual jerribeth.patron_lost binding resolves to VellexiaKilled.
The important distinction is that Vellexia's death causes Jerribeth to depart; it is not evidence that Jerribeth died.
The new evidence report corrects the earlier progression handoff's overly broad suggestion that the binding itself lacked Vellexia-death semantics.
No native state was changed to resolve the wording error.

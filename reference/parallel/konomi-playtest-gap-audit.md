# Konomi manual-play and completion gaps

Konomi is a strong first manual-play candidate, but the installed mod does not contain her route and she is not complete against the full agreed access requirements.
Her ordinary and native-dismissal manuscripts do not need another large expansion to stop being drafts.
The immediate work is packaging; the substantive completion work is the remaining contact and recovery coverage.

This audit owns only this report and changed no source, package, installed file, artwork, or save.
The report path was absent before the audit.
I authored the earlier reciprocal scene, so I rely on its separate independent review rather than reapproving my own prose.

## What is actually present

The inspected development snapshot has 501 scenes, SHA256 `4281B45A236BD9B3E956CDB153896F1FF722E7320237FEDA3C0B3796E1384483`.
Konomi has 64 scenes and 551 pages: 25 physical-contact scenes, 24 remote books and 15 alternative endings.
The canonical compact sorted-key Konomi scene-array hash is `3E40B2ADCC380B756C4EB860D3EFE6A146C264D8F1BD935DA0FA91426057607D`.
Other characters may advance after this snapshot without changing these findings.

I compared all 64 objects with the final reviewed `development/konomi-chronology-review.json`, SHA256 `926687FB240C1E17A565D820D8FFDC920C6E2DDC077B06A61561CB0214F6F41E`.
The only difference is `konomi.before_road/Nodes/0/Portrait`, changed from `Konomi` to `KonomiPrivateEvening`.
Thus the accepted manuscript and repaired late-career catch-up remain intact.
The [final assembled review](../story-review/konomi-assembled-final-review.md) records writing 91, likeness 92, mature romance 93, participation 92, normal depth 91 and continuity 92, with its authorship qualifications.
It reports 50,014 distinct words, with normal selected examples approximately 10,857-19,371 words depending on the actual route.
Those findings are not proof of universal access or a rendered game experience.

| Delivery artifact | Actual state |
| --- | --- |
| `package/Story.json` | Old 34-scene story, zero Konomi scenes |
| Installed `Mods/RanRomanceTirabade/Story.json` | Same old 34-scene story, zero Konomi scenes |
| Both old story hashes | `3176BB0102324BAB5BAF664D6956D5DEB3A4FB638029789D74F0EFCDF73DC6D4` |
| Packaged and installed `RanRomance.Tirabade.dll` | Same old binary, SHA256 `E44115E37170946318CA3BAF1A3BE03CAD65C09318E305313481A43C55AD0F50` |
| Current compiled development DLL | Different binary, SHA256 `6ADEDEE3CA9085D8C98DF8191C764BCDDD169EB18277635E5AA5D8E943925292` at inspection |
| Project `Scenes/Konomi.png` | Exists and exactly matches approved v2, SHA256 `74267A675F25A786A118B54631D9093305478A484AACEA370082708AFB35B196` |
| Project `Scenes/KonomiPrivateEvening.png` | Exists and exactly matches approved private v3, SHA256 `BCB644CC8DDE8064C09F610EB213B1926CADA1DBF85E009E70191007E8A928A8` |
| Installed copies of both Konomi scene images | Missing |

There are 550 effective `Konomi` page keys and one `KonomiPrivateEvening` key on `before_road/start`.
Every currently requested Konomi scene-image key has a project file.
The old claim that the project has no Konomi art or still assigns the Tirabade couple to narrator pages is obsolete.
Both paintings passed independent static review; their displayed crops remain unobserved.
The general portrait's office background is approved as a character portrait, not a literal illustration of every private room or letter.
No Konomi-specific native NPC portrait override was found in the project, installed portrait mod or inspected LocalLow NPC portrait directory.
Book-event images and native dialogue portraits are separate systems.
If the final presentation includes redesigning her native dialogue portrait, export its three sizes and verify the actual lookup name before adding it to the existing portrait installer.
Do not invent an additional image quota: no currently assigned book key lacks a project asset.

## Smallest remaining implementation work

| Priority | Concrete work | Files or functions affected |
| --- | --- | --- |
| First manual-play build | Execute the new separate expansion target, verify its staged manifest, then install the reviewed expansion and PNGs through a backup-aware deployment | `build-expansion.ps1`, `development/PLAYTEST-PACKAGE.md`, deployment and staging manifest |
| Full Trickster acquisition | Add a played contact opportunity for supported missed-introduction or otherwise unavailable histories that do not have the native rank-six dismissal answer | New Konomi access module plus the `fate_post` entry contract and downstream private helper gates |
| Lost or removed actor histories | Implement and test observation of the exact saved officer representation, distinguish hidden/unloaded/living/dead/destroyed/never-spawned, and supply the agreed restoration or reconnection for supported cases | A Konomi-specific observed-state/recovery contribution, using the existing native contact and retained-actor patterns without changing native office history |
| Accurate finished delivery | Make the private route's life/contact state and presentation contract explicit, preserve its existing rest/manual books, and add any required guest actor only if that is the chosen delivery model | Private helper gates in `konomi_private.py`, `konomi_history.py`, `konomi_distance.py`, `konomi_future.py` and their continuations; shared observer integration where needed |
| Player-facing test access | Document the real chapter/rank trigger, rest entries, manual-only continuations and approved artwork in the expansion's play instructions | Expansion guidance and test-save manifest; do not describe private Chapter 4 compatibility material as normal acquisition |

The existing `build.ps1` invokes `story.py`, which emits the original package story.
Running the usual build/install unchanged would therefore omit Konomi again, even though `development/Story.json` is current.
Root has now added `build-expansion.ps1` as a separate expansion target, leaving that original release target intact.
I independently read the complete script and its playtest instructions.
It generates the expansion, builds the current assembly and narrator, runs rules, native bindings and managed construction checks, and stages a fresh uniquely named `dist` directory with copied-file hash checks.
It includes the portrait tree and reports missing effective portrait keys without representing them as approved art.
It neither installs the result nor overwrites the original package.
At this review point its execution is still root-owned and pending, so this report does not claim a successful staged or installed build.
One consistency gap was sent to root: the script validates the live development story and copies that path later without pinning the validated hash.
A concurrent export between validation and copying could stage different input.
Capture and verify the generated hash throughout, or run every check against one frozen snapshot.
This is a source-inspection finding, not an observed failed packaging run.
The existing installer already copies the staged scene-image tree and records backups.
`Main.Load` reads only the installed addon's `Story.json`; it does not discover the development export.

For broader access, preserve the existing real dismissal entry and its native conditions.
Do not set `konomi.dismissed` or restart her office etude to make a different invitation fit the old route.
Any new entry must earn its own invitation and accepted contact, then join downstream visits through explicit alternative provenance with appropriate dialogue-history variants.
The current private modules repeat native dismissal and completed-office requirements, so adding only one new opening would still strand an undismissed guest.
That is the concrete integration work required beyond writing the introduction.
Authored refusals and player-initiated breakups should remain meaningful, not be cleared globally to make a progress counter reach completion.

`Revivals` currently contains only Seelah, and no Konomi recovery implementation or native death alias is present.
The shared `NativeContact.IsAvailable` correctly rejects a dead, hidden, unloaded or missing ordinary actor, but its false result does not explain which case occurred.
`JerribethRecovery` shows the existing retained-spawner observation approach; it is a reference for evidence handling, not a Konomi recovery service already delivered.
The native Konomi Swarm removal completes the office etude and uses `DestroyUnit` on the officer spawner.
That establishes removal, not a reusable corpse or permission to manufacture a replacement.
The full requirement must resolve the applicable removed/dead cases before claiming universal restoration; this audit does not invent a normal campaign death encounter from a missing contact.

## Actual native access and timing

Ordinary contact is well sourced and implemented.
The officer unit is `ca2d58c5c65723945857e04fb85d30ce`, spawner `c658c4cf-116e-4b61-9ff9-8905bcf4fd6b`, with reusable native answer list `0dc8b8604bb33c846a63f3eb62443674`.
`konomi.present` reads the Playing state of `b5f301fbc4c44535a6309d610d5bd28a`.
Rank two introduces the office state; higher-priority rank-up scenes can temporarily suspend it.
That temporary loss should defer a conversation, not end the relationship.
Rank-eight council conclusion does not itself complete the officer state in the inspected native records.
The [availability audit](../canon-review/konomi-availability-review.md) and [contact evidence](../canon-review/konomi-physical-contact-plan.md) establish these distinctions.

The current `fate_post` requires `trickster`, `konomi.dismissed`, and `konomi.office_completed`.
It forbids present Konomi, the inhuman path and the authored farewell.
An inline inspection of those actual predicates produces the following missing prerequisites:

| History | Why the current impossible post cannot acquire it |
| --- | --- |
| Never introduced | No selected dismissal and no completed office |
| Office completed without the rank-six answer | No selected dismissal |
| Temporarily displaced officer | No selected dismissal or completed office; the ordinary contact should return later |
| Fully converted Legend before acquisition | No current Trickster |
| Living native dismissal while still Trickster | Existing entry is supported, subject to the remaining ordinary gates |

The rank-six project explicitly requires Chapter 5, despite the rank-up etude's Chapter03 directory.
Normal fresh private acquisition is therefore Chapter 5.
`private_absence` requires an already played private departure and address in Chapter 4, making it compatibility coverage for altered histories rather than normal campaign content.
The actual ordinary route has `unsent` for its Abyss interval and can transition into the private route after Chapter 5 dismissal.
The [Legend sequence audit](../canon-review/konomi-legend-sequence-audit.md) supports a residual-Trickster interval after selecting Legend but before completing its cleansing; that interval is a legitimate candidate for acquisition, not an executed live-save result.
Completing Legend first intentionally prevents new Trickster magic while preserving already earned continuation.
Other mythic paths retain character-appropriate restrictions; the full Trickster requirement is not a demand to make every non-Trickster acquire this post.

Private meetings are intentionally remote, unitless books, not physically spawned Konomi guests.
The first private meeting requires a played appointment and native dismissal/office completion but has no `ContactUnit`.
This is an implemented presentation mechanism, not proof that an NPC stands in a room.
It also has no separate Konomi life-state observation, so native dismissal should not be advertised as a universal alive predicate for future recovery support.
A world actor is not automatically required merely because a book narrates a meeting; the current book model can be playtested honestly as such.
Any later recovery integration must guard it against confirmed incompatible actor histories rather than treating missing loaded contact as death.

## Verification after implementation and installation

The current shared runner registers the ordinary, private history, hearing, correspondence, political, career, absence chronology, early reciprocal and contact suites.
Their existing coverage includes played joins, outcomes, native predicate fixtures and interrupted conversations.
The accepted late-career repair has its own independent 371,366-assertion run.
These checks do not execute native diplomacy scheduling or prove a seed flag was earned in a game save.
No new source test or Unity session was run for this read-only audit.

The first useful manual pass needs three actual histories, with the installed story/DLL/image hashes recorded:

1. A Chapter 3 or retained-office Chapter 5 save: enter the real officer dialogue, exercise a roll and its failure/nonroll continuation, cross a rank-up displacement and return, save/reload, and inspect the general portrait with controls visible.
2. A real Chapter 5 rank-six dismissal on Trickster: earn the post without seeding it, receive the reply after its delay, play the unitless private meeting, inspect `before_road/start`, and continue correspondence through its 336/168/336-hour waits, career and farewell.
3. An established ordinary romance across Chapter 4/5: retain the actual Abyss letter, dismiss Konomi later, omit then revisit the optional catch-up after the completed career, and check its remembered history.

`private_political_account`, `another_evening`, `private_absence_catchup`, `private_return_terms` and `private_last_visit` are manual-only remote scenes.
`Rules.NextRemote` skips them; `Main.OnGUI` exposes their available Read buttons.
The private career and farewell cannot be verified by repeatedly resting while ignoring that manual entry.
Use the current chapter and actual progression conditions, not a fabricated early rank-six dismissal, when preparing these saves.

During those passes, leave ToyBox Love Is Free and Jealousy Begone enabled and keep another romance active.
The source uses its own flags and does not add a global exclusivity requirement, but loaded-mod coexistence still needs observation.
Check queue interruption, leaving the area, save/load during an unfinished book, repeated completion, actual native die execution, and portrait crop/refresh.
The additional missed-contact and recovery histories need corresponding end-to-end cases after their implementation; replaying ordinary paths cannot substitute for them.

Konomi can become a useful ordinary manual-play build as soon as the reviewed expansion and images are staged and installed.
She cannot yet be counted as complete under the full agreed requirement merely by passing that ordinary playthrough.

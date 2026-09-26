# Three at the Table

A Relations and Romances extension for Anevia, Irabeth, and the Commander.
Two independent affairs lead to discovery, difficult conversations, and an optional three-person relationship.
The route contains mature themes and non-graphic intimacy.

## Playing

Restart Wrath once after installing the new assembly, then load an existing main-campaign save.
No new campaign is needed.
The first conversations appear in Anevia's and Irabeth's ordinary dialogue menus after their required introductory conversations.
At the Defender's Heart, ask Anevia whether she has had a moment to herself and ask Irabeth to speak as a person rather than an officer.
The pre-Minagho introductory save can proceed normally to the tavern before starting.

Act 1 introduces the friendships, Act 2 develops them, and Act 3 permits the affairs and reconciliation.
There are 12-48 in-game hours between relevant meetings; remaining in the same conversation does not advance them.
Talk to both women and continue the campaign when a meeting is not yet available.
Act 4 offers unsent letters after successful rests, with a manual reading option in the mod manager if another rest event took precedence.
Act 5 develops commitment and shared life, with reactions to the current mythic path.
Late installation permits remaining conversations in the present rather than pretending missed chapter-specific events occurred.
An Act 4 installation begins its in-person route after returning to Drezen.

Each participant can refuse or end the attempted relationship.
The route respects character death, departure, absence with Galfrey, and the loss of mortal romance on Swarm and completed Lich paths.
It does not resurrect characters, change Iz outcomes, or force a successful ending on incompatible campaign states.
Normal, separated, unfinished, loss, ascension, monstrous-transformation, and True Aeon epilogues are conditional.

## Compatibility

Requires Relations and Romances 0.1.11 and CustomNpcPortraits.
Built against the assemblies installed on this machine and Unity Mod Manager 0.27.11 or later.
ToyBox Love Is Free and Jealousy Begone may remain enabled.
The extension has no Commander gender restriction and does not register its affairs in the base game's exclusive-romance system.
Its internal story consequences remain part of the narrative even when ToyBox disables vanilla jealousy scenes.
Existing RanRomance dialogue answers and finish actions are preserved.
The native epilogue sequence gains conditional pages without replacing the original outcomes.

Windows TTS reads the extension's pages through an isolated .NET Framework helper using an installed English voice.
It is synthetic narration, not an imitation of the original actors.
Toggle it in this mod's settings or press Ctrl+S to stop a reading.
No API key, subscription, audio download, or change to WOTR_AIVO's soundbanks is required.
Existing AIVO clips remain managed by AIVO.

## Portraits

Shareable originals and game-size portraits are under `art/` in this project.
Installed copies are under `Mods/CustomNpcPortraits/Portraits - Npc/Anevia` and `Irabeth`.
Book-event artwork is under `Mods/CustomNpcPortraits/RanRomance-Tirabade/Scenes`.
CustomNpcPortraits 1.3.7 actually reads NPC overrides from the game's LocalLow `Portraits - Npc/<name>` directories.
The installer therefore copies portraits to both the mod directory and the runtime directory.
The LocalLow `Portraits/CustomNpcPortraits - <name>` layout is for companion presentation; it alone does not replace an ordinary NPC portrait.
The installer preserves replaced files and records their destinations in `backups/<timestamp>/manifest.json`.

## Development

Run `./build.ps1` with PowerShell and Python available.
It uses the locally installed .NET SDK in `%LOCALAPPDATA%/RanRomanceTools/dotnet`, or `dotnet` on PATH.
Pass `-GameDir` to build against another installed copy.
Run `./prepare-portraits.ps1` to export game portrait sizes, then `./install.ps1` to install.
The installer accepts `-GameDir` and `-UserData` for other machines.

Edit `story.py`, not the exported `package/Story.json`.
Scene and node IDs, the namespace used by `GuidFor`, and existing choice indices are save references and must remain stable across updates.
The runtime uses native unlockable flags for save persistence and native book events for display.
`src/Story.cs` holds the same progression rules used by the executable validation suite.
The narrator is a separate .NET Framework executable because Unity's Mono does not reliably support the COM speech APIs.
Game assemblies, decompiled reference material, personal saves, and backup portraits are not part of the shareable source archive.

# Expansion development package

This package contains the current development story, matching mod assembly, narration helper and staged portrait assets.
It is incomplete and is not approval of every character route, illustration or mythic access branch.
The adjacent manifest identifies every packaged file, the scene count, story hash and missing portrait keys.
Some staged portraits have narrower scene-use approval than a complete route.

Build from the project with `./build-expansion.ps1`.
Use `-GameDir` for a different Wrath installation and `-Python` for an explicit Python executable.
The command generates the expansion, builds its assemblies and checks rules, native bindings and managed construction before creating a fresh directory under `dist/`.
It does not run the original story generator, overwrite the original package or install anything into the game.

The `Mods/` layout contains the addon and portrait overlay only.
It does not include the required RanRomance or CustomNpcPortraits mods themselves.
Existing mod identity and blueprint identifiers are preserved.
Do not run the original `install.ps1` to install this output: that script reads the original `package/` directory.
Deployment, rollback and the specific save and route to test must be prepared separately.

Headless checks do not verify Unity dialogue presentation, actual actor arrival, parent-mod initialization, save/load or ToyBox execution.
Review the project's character checkpoints for which ordinary routes are approved and which recovery, guest or art work remains unfinished.

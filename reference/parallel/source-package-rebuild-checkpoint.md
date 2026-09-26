# Source archive rebuild verification

Root reproduced a source-package failure by running the real `package-release.py` and inspecting its resulting source ZIP.
The archive omitted `expansion.py`, `story_format.py` and all character modules.
The first repair exposed the additional missing runtime build input `reference/expansion/etudes.json` during an actual extracted build.

The source packager now includes the character modules, expansion entry points, managed verification sources, Python verification tools, relevant project documentation, native etude input and reviewed parent binding manifest.
It continues excluding build outputs and dependency environments.
The binary package still uses the existing `package/` contents; this change does not turn it into an approved expanded release.
No files were installed or published.

`tools/verify-source-package.py` extracts the source ZIP into its own temporary directory, runs that copy of `expansion.py` with the extracted directory as its working directory, and compares the resulting bytes to the expected development story.
The repaired archive reproduced SHA256 `7C9D3E0DAC178A9F573341E28EDDD907AED6EE97D417DA7CAFBC1A309372522F`, exactly matching the reviewed 264-scene export.
The command was `python tools/verify-source-package.py dist/ThreeAtTheTable-source-1.0.0.zip development/Story.json`.
This proves source-to-story reproducibility for that revision, not Unity compatibility or readiness of the separate binary package.

## Committed 291-scene verification

On 26 September 2026, root extracted `git archive HEAD` at commit `ead4e9a` into a temporary directory and ran that copy of `package-release.py`.
This excluded uncommitted Aranka source and other active worker files from the tested snapshot.
The resulting source archive was 68,732,441 bytes.
Running `tools/verify-source-package.py` against that archive rebuilt all 291 scenes with exact SHA256 `5E068C8E3601E7552AE501C34A8CD7E749207B00A9F32AABB1C5F99A515A4CA0`, matching current `development/Story.json` byte for byte.
The process exited successfully and its temporary files were removed by the standard temporary-directory context.
This check did not compile an extracted DLL or validate the binary archive, which lacks Git-ignored compiled outputs in this snapshot.
Nothing was installed or published.

# Nurah parent runtime cue bindings: independent review

## Verdict and scope

The three cue identities, names, types, and branch associations are supported by the installed parent assembly.

The assembly pin and decompilation hash also match.

Revision is required for the manifest's purported exact source excerpts: its `GuidDeclaration` fields and call excerpts do not match the freshly decompiled method's actual local-variable structure.

The loader correctly marks generated substitutes as parent-source fixtures rather than native archive records, but it does not itself verify the decompilation hash, exact source excerpt, cue name, or branch condition.

This review covers only `reference/canon-review/nurah-parent-runtime-cue-bindings.json`, `managed-tests/read-native.py`, and `tools/parent_bindings.py`.

No production source, manifest, loader, story, or romance route was changed or approved.

## Hash and source verification

The installed mod assembly at the manifest path has SHA-256 `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`, matching `AssemblySha256`.

I freshly decompiled `RanRomance.Nura.NuraBook05Page002` from that assembly with ILSpy 9.1.0.7988.

The exact UTF-8 stdout bytes from that class decompilation hash to `5515B91F22653A4D1E6CCA6151C36B06C1D06944323EA5C6AF55CD757BDCD53C`, matching `SourceMethodSha256` and the corresponding class entry in `nurah-parent-bindings.json`.

This digest covers the complete decompiled class output, including `Configure`, rather than an isolated method body.

The manifest field name `SourceMethodSha256` should not be read as a hash of only `Configure`.

## Cue identity, type, name, and branch

All three GUIDs are absent from the installed `blueprints.zip` native archive.

The freshly decompiled parent class declares the corresponding cue-name fields as `RanRomNuraBook05Page002Cue0004`, `RanRomNuraBook05Page002Cue0011`, and `RanRomNuraBook05Page002Cue0017`.

The calls use `CueConfigurator.New` with those names and create `BlueprintCue` records.

The decompiled method associates GUID `a81d2fc67aa9435999b2eba84eabf368` with cue 0004 and the `RanRomNuraEvil` playing-state condition.

It associates GUID `64bd5f9b742d4033b17f12b9b519970e` with cue 0011 and the `RanRomNuraChaos` playing-state condition.

It associates GUID `5a06af413442436a88c2362c9e9dcbd0` with cue 0017 and the `RanRomNuraGood` playing-state condition.

Each cue is configured with text and `SetShowOnce()`.

The branch mapping is independently visible in the decompiled locals `conditions3`, `conditions10`, and `conditions16`, respectively.

## Manifest excerpt discrepancy

The manifest's `GuidDeclaration` claims declarations such as `string Cue0004Name = "a81d2fc67aa9435999b2eba84eabf368";`.

That is not the source declaration.

The source declares `Cue0004Name` as the cue's name string, `RanRomNuraBook05Page002Cue0004`, and stores the GUID in a local variable named `text7`.

Likewise the other IDs are held in `text14` and `text20`, while `Cue0011Name` and `Cue0017Name` contain their respective name strings.

The manifest's `Evidence` also presents a simplified call with the GUID inline, while the decompiled call passes `text7`, `text14`, or `text20` as the second argument.

The simplified evidence preserves the correct name-to-GUID-to-type association, but it is not an exact source excerpt and the `GuidDeclaration` label is materially inaccurate.

Use the actual local declarations and call expressions, or label the evidence as a normalized association rather than verbatim source.

## Loader and fixture boundaries

`tools/parent_bindings.py` reads the manifest, hashes the pinned installed assembly, rejects a mismatching assembly, validates GUID syntax and allowed blueprint types, and checks for a minimally attributed creation excerpt.

It does not validate `SourceMethodSha256`, independently inspect the assembly's decompiled source, validate the dynamic cue name or branch, or determine whether `Evidence` is a verbatim excerpt.

Those checks therefore belong to the independent evidence review, not to the loader's runtime guarantee.

`managed-tests/read-native.py` searches the archive first and applies a parent binding only to a GUID still missing from the native archive.

For these three missing GUIDs it emits a deliberately non-native `$type` value of `ReviewedParentFixture, BlueprintCue`, plus a `FixtureProvenance` object with the reviewed-parent source marker and assembly hash.

It also writes a `Parent source fixture` diagnostic to stderr.

This keeps the test fixture distinct from a native `BlueprintCue` record and does not invent native cue fields, conditions, or behavior.

The fixture represents reviewed parent-source existence and type only; it cannot prove that the parent initializer ran in the current process or that the resulting cue has its production runtime components.

## Required correction and limits

Before treating the manifest as exact-source evidence, correct the declaration and call excerpts to match the pinned decompilation and state the three path branches explicitly.

The assembly and class-output pins are valid, and the three GUID/name/type/branch associations are verified against the pinned assembly.

This review does not validate route content, parent initialization order, runtime visibility, native dialogue behavior, or any romance readiness.

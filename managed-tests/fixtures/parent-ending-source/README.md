# Parent ending source fixtures

These files reconstruct the reviewed parent ending condition trees using actual native game condition classes.
They do not execute RanRomance initialization, native conditions or Unity gameplay.
Source provenance and SHA256 pins are in source-provenance.json.
The original decompiler output is preserved as .cs.txt so the SDK does not compile it into the test runner.

Regenerate from any working directory with Python and the path to generate.py.
Use --check to validate the pinned evidence and check that the generated file matches.
No installed game files, external packages or temporary directories are needed for generation.
Compiling and running the resulting C# still requires the project's normal game assembly references.

```powershell
python managed-tests/fixtures/parent-ending-source/generate.py
python managed-tests/fixtures/parent-ending-source/generate.py --check
```

The generated output is managed-tests/ParentEndingSourceFixtures.cs.
Do not edit it manually.
Edit the generator or native-builders.cs.txt template and regenerate when the fixture implementation needs to change.
The template reconstructs actual native conditions and actions from the extracted expressions; it does not fabricate a successful condition result.

The 73-cue verified-contract.json is the GUID-to-page/key/prose evidence consumed by ParentEndingIntegrationTests.PrepareSourceFixtures.
It includes the nine ordinary/Aeon parent page sources.
The native-paired.json records preserve the separate native pair page and cue.
MinaEpil.cs.txt provides the parent's replacement condition for that native page and the eight-page MarkCuesSeen action order.
The generator checks source-expression equality, resolves parent aliases from MinaMain.cs.txt and page declarations, and rejects unresolved aliases.
EpSetup.cs.txt documents ordinary RanRomAdd, Aeon and conditional RanRomInt topology but is not used to fabricate an active optional mod.

Program integration remains separate.
PrepareSourceFixtures must run after localization/cache fixtures exist and before Main.Build.
Pass the parsed verified-contract.json, ParentEndingSourceFixtures.Build(), and ParentEndingSourceFixtures.PageActions().
Run CheckPreflight before Main.Build and Run after the build as described in the integration handoff.
These checks preserve native object identity and hook timing without claiming populated native CanShow or a Unity epilogue passed.

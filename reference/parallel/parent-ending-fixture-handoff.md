# Portable parent ending fixture handoff

Status: frozen for independent review, not self-approved.
The frozen production integration, Main, and integration tests were not edited.
Only the fixture directory, new generated ParentEndingSourceFixtures.cs and this handoff were added.

| File | SHA256 |
| --- | --- |
| managed-tests/ParentEndingSourceFixtures.cs | `DB36C101C7878C5A2AA67AB62A8842F6987E4F81FD57F0919B5D77203BE0F7E0` |
| managed-tests/fixtures/parent-ending-source/generate.py | `B26BDD805FFFC3846FA806C376400D54300C95AF283486D77806902E3CB97A2D` |
| managed-tests/fixtures/parent-ending-source/native-builders.cs.txt | `151811CE71205F43D3C622A0414AD2227C896A1F88F299099E71A5C0E0C7785D` |
| managed-tests/fixtures/parent-ending-source/source-provenance.json | `DE2A61755CD75BE0A668B64BA2DEE77387EA464737D32F5C01DD7E2C0842816A` |
| managed-tests/fixtures/parent-ending-source/verified-contract.json | `9A3C8B03067FF5EE0E5FCF68487B142A9DB32709B104737E2383173FBA0B8347` |

The generator has no temporary path dependency and uses only the Python standard library.
It validates pinned original evidence files, cross-checks every extracted condition definition with its copied decompiled source, resolves source-proven parent etude/page aliases and emits the C# fixture.
The native paired page condition and page OnShow action order now come directly from copied MinaEpil source expressions rather than handwritten generated-file changes.
The source GUID-to-page/key map needed by PrepareSourceFixtures is retained byte-for-byte as verified-contract.json.
Original decompiler files remain unmodified under .cs.txt names to avoid SDK compilation.
The builder template is authored test support; its output is generated and must not be edited manually.
No new dependency or generic fixture framework was introduced.

Portable generation succeeded from an unrelated temporary directory and produced byte-identical C#.
The --check mode passed, and a controlled change to copied Slide0001 source was rejected by its SHA256 pin.
The independent isolated build directory is C:/Users/Z/AppData/Local/Temp/parent-ending-portable-3dbf62b2.
Observer and Runner both built with zero warnings/errors.
Runner exited zero with 71,672 assertions against the unchanged 585-scene candidate SHA256 780BDC23146431CECD7F1ED9594B5F129C5E149DB535CC40F2BD128A2126647A.
It used the checked-in ParentEndingSourceFixtures class and checked-in evidence instead of the earlier temporary fixture source.
The earlier reviewer harness remains untouched.

The fixtures construct actual native condition/action objects, including nested AND/OR trees and exact blueprint references.
They do not execute the installed parent builders, whose private-field access fails under standalone CLR, or populated native Unity conditions.
They do not initialize the parent mod or verify rendered epilogues.
Native behavior beyond the documented fixture fields remains an in-game verification boundary.
The original parent DLL and Assembly-CSharp hashes, decompiler version, each input hash and source origins are recorded in source-provenance.json.

Root owns Program adoption.
The minimal calls remain PrepareSourceFixtures with parsed fixture JSON, ParentEndingSourceFixtures.Build() and PageActions(), then CheckPreflight before Main.Build and Run afterward.
The fixture README gives regeneration and integration instructions.
No shared output or story export was changed.

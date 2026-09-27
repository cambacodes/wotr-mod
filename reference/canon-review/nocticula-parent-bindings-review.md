# Nocticula parent binding source review

Date: 2026-09-26.
Verdict: pass for the ten typed creation bindings in the candidate manifest.
No incorrect GUID, blueprint kind, or declaring method was found.
This is source evidence approval only, not approval of Nocticula prose, route completeness, historical flag interpretation, or Unity behavior.

Reviewed manifest: reference/canon-review/nocticula-parent-bindings.json.
Manifest SHA256: 25BF714F52434E6FED6C4AF01364DAC5BD3F27F6E17FD7F04D9E77146B660535.
Installed parent DLL: D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/Mods/RanRomance/RanRomance.dll.
Its measured SHA256 matches the manifest pin, 281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68.
The manifest was not changed or merged by this review.

## Independent evidence

Freshly decompiled all three specified classes from the installed pinned DLL with the project's ILSpy 9.1.0.7988 tool.
Each fresh class matches the retained class text after normalizing encoding and line endings.
All three retained raw-file hashes match SourceHashes in the manifest exactly.

| Retained source | Verified SHA256 |
| --- | --- |
| Main.cs | FD2580406A8EB01BCFBD80DE73F782F1A1B7C34AD7F6814F7651280D673D58E2 |
| NoctBook02Page002.cs | 2BBFF934C809EF2289B401BE0D4FDAE050064879C5317241006737EC6DA55731 |
| NoctBook03Page003.cs | 45A7E2B1CE799AF55C17980CE4209BA7003C4E9A757A11049DADADF0CD3A29F8 |

For each binding, checked the literal GUID assignment, its unreassigned local variable, and the exact New call consuming that variable within the named Configure method.
The five etude bindings use EtudeConfigurator.New.
The five cue bindings use CueConfigurator.New, rather than a page, answer, sequence, or check configurator.
The GUIDs are distinct and have the expected 32-character hexadecimal form.
Main.Configure returns void; the two page-class Configure methods return string.
The manifest correctly names their methods without claiming a shared return signature.

| GUID | Type | Creation method and fresh source line |
| --- | --- | --- |
| 18affced672d4c56a52bf6ffc00601b9 | BlueprintEtude | RanRomance.Noct.Main.Configure, line 44 |
| 8a28bbd82568486bb757d00a2087a6cf | BlueprintEtude | RanRomance.Noct.Main.Configure, line 58 |
| 761ca3572c1145ebb755032d613bff46 | BlueprintEtude | RanRomance.Noct.Main.Configure, line 61 |
| 9591c34df22b4d518a059cf608255458 | BlueprintEtude | RanRomance.Noct.Main.Configure, line 52 |
| 19e5d6f04b9b4483b2e2979baf8736e4 | BlueprintEtude | RanRomance.Noct.Main.Configure, line 55 |
| 631bf0ede36742559cee476f34dcb5de | BlueprintCue | RanRomance.Noct.NoctBook02Page002.Configure, line 434 |
| cb13766be07b448f8cacb477be32e13c | BlueprintCue | RanRomance.Noct.NoctBook02Page002.Configure, line 437 |
| 5388a7d7a1da48deb333d34abab1a6d0 | BlueprintCue | RanRomance.Noct.NoctBook02Page002.Configure, line 440 |
| b3a4ce99bc30440fa9ebcbfce2776176 | BlueprintCue | RanRomance.Noct.NoctBook03Page003.Configure, line 220 |
| 1110f2b6304549999fb546e7ecc4c8a1 | BlueprintCue | RanRomance.Noct.NoctBook03Page003.Configure, line 269 |

The Evidence strings are short assignment-and-call summaries, not contiguous source excerpts.
Their two parts both match the fresh decompilation and correctly preserve which local variable supplies each GUID.
This distinction should remain clear if the manifest is reused as provenance in a larger fixture set.

Independent artifacts: C:/Users/Z/AppData/Local/Temp/nocticula-bindings-review-6a87e0b1.
Main-fresh.cs and the two page-class files are fresh decompilations.
verified-bindings.json records the ten checked mappings and creation lines.
The exploratory Main.il output is incomplete and is not used as evidence.

## Limits

No parent builder was executed and no blueprint cache was initialized by this review.
Creation-site evidence establishes source identity and type, not whether a particular save has started an etude or displayed a cue.
Names such as Active, Initial, Reject, or LaulRom do not by themselves establish a complete interpretation of relationship history.
Consumers still need the appropriate observed native state and story-specific analysis.
The candidate remains separate from the shared expansion binding manifest, and merging it belongs to root.
No source, story, installed asset, or manifest was edited.

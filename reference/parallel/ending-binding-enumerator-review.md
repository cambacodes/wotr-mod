# Ending binding enumerator independent review

Reviewed on 2026-09-26.
Verdict: pass for the requested offline enumeration and parent page type support.
No blocking defect found in the three reviewed changes.
This review does not approve the manifest I previously authored or certify native integration.

## Frozen source

| File | SHA256 |
| --- | --- |
| `tests/Program.cs` | `EA234E3BA2E5DF02CE4B2FAB6B61BF7274CE40D3B9429ED0E2B3DA6BEF7E4472` |
| `tools/parent_bindings.py` | `3DD2984BFDC0836DC3E7EB62C3438A29E5A1C46734226B4678BB4CE8ECFC4197` |
| `tests/test_parent_bindings.py` | `BD4CD735D7C916F6346547602222709E94DCEE6CCD42D338AB0303CFFAE141A3` |

I inspected the diff, its containing functions, the typed metadata in `Story.cs`, and the verifier's consumption of `ExpectedType`.
I rebuilt the actual test entry point with repository sources into the isolated `minachiv-binding-expansion-e4c287/Bindings.csproj` output.
The build finished with zero warnings and zero errors.
No shared build output or production file was changed during review.

## Enumeration checks

I ran the rebuilt entry point with `--bindings` against `C:/Users/Z/AppData/Local/Temp/minachiv-root-art-yh5sdgtw/candidate.json`.
Its SHA256 is `780BDC23146431CECD7F1ED9594B5F129C5E149DB535CC40F2BD128A2126647A`.
An independent Python comparison derived expected GUID, type and source triples directly from that JSON and compared them with the actual C# output.
The exact sets and occurrence counts matched.
There were 93 ending binding uses, 59 distinct ending GUID/type pairs and 1,105 total binding uses.
The candidate contains 35 ordinary edits, three loss rules and four survivor alternate entries.

Ordinary edit dictionary keys are emitted as `BlueprintCue`.
Suppressed pages are emitted as `BlueprintBookPage`.
Suppressed cues and survivor alternate dictionary keys are both emitted as `BlueprintCue` under their loss rule IDs.
The survivor keys are explicitly concatenated, so their inclusion does not depend on ordinary edit membership.
Current validation also requires survivor keys to occur among their rule's suppressed cues.
Repeated uses are intentional and remain useful for reporting their requesting sources.
The verifier resolves each GUID once, then compares its resolved type against every requested use, so duplication does not conceal a conflicting expected type.

Localized text keys, authored replacement scene IDs and condition flags are not blueprint GUIDs and correctly remain outside this enumeration.
The new lines preserve the existing binding categories.

## Loader and focused test

The loader adds `BlueprintBookPage` to its existing allowed types without changing the installed assembly hash check.
It still requires a lowercase 32-character GUID, a nonempty source, no duplicate GUID and an evidence excerpt containing the requested GUID and type or corresponding configurator name.
For pages, the derived creator is `BookPageConfigurator.New(`.
The added test accepts that creator and rejects an otherwise identical excerpt changed to `CueConfigurator.New(`.
I reran `tests/test_parent_bindings.py` with Python 3.14 and bytecode writing disabled; it passed.
The existing assertions also exercised a changed assembly, a mismatched type, duplicate identity and a missing GUID in the excerpt.

The loader checks consistency of reviewed evidence; its substring checks are not a C# parser or independent proof that an arbitrary excerpt came from the pinned assembly.
That existing trust boundary still requires separate source review and was not broadened beyond accepting the needed page type.
No special treatment of this particular manifest or its supplemental schema was added.

## Limits

I did not repeat the expensive native archive scan.
The root's reported 139 archive targets and 106 parent targets are therefore not a newly reproduced result of this review.
This review independently reproduced enumeration coverage and loader behavior, not parent initializer execution, page membership, localization provenance, Unity display or save round trips.

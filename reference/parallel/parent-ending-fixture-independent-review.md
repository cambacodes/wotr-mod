# Portable parent ending fixture independent review

Reviewed on 2026-09-26.
Verdict: pass for adoption as the portable source fixtures in the managed test harness.
No production code, generated file or shared test runner was edited during this review.

| Reviewed file | SHA256 |
| --- | --- |
| `managed-tests/ParentEndingSourceFixtures.cs` | DB36C101C7878C5A2AA67AB62A8842F6987E4F81FD57F0919B5D77203BE0F7E0 |
| `generate.py` | B26BDD805FFFC3846FA806C376400D54300C95AF283486D77806902E3CB97A2D |
| `native-builders.cs.txt` | 151811CE71205F43D3C622A0414AD2227C896A1F88F299099E71A5C0E0C7785D |

I read the generator, builder template, provenance, copied source expressions, generated diff and author handoff.
The earlier independent integration run supplies the baseline for the temporary `SourceConditionFixtures` semantics.
This review does not treat the author's portable 71,672-assertion run as independently rerun.
The production integration and Main remain outside this fixture-only change.

## Independent checks

I copied the fixture directory into `C:/Users/Z/AppData/Local/Temp/parent-fixture-independent-n3gk1a3q` under the same repository-relative layout and ran the generator from the unrelated temporary root.
Its output was byte-identical to the checked-in generated C#.
The relocated `--check` passed.
Appending a controlled comment to the copied Slide0001 source caused generation to fail with its expected source-hash diagnostic.
No original evidence file was changed.

I independently parsed all copied CueConfigurator chains and compared each actual condition assignment and localization key against `verified-contract.json`.
All 73 cue assignments and nine ordinary/Aeon page condition assignments matched.
This supplements the generator's source-definition comparison, which by itself checks condition definitions more strongly than individual cue-to-condition assignments.
The fixed, pinned inputs and the independent assignment comparison support the current fixture.
It should not be advertised as a general parser for arbitrary future parent versions.

The generated diff preserves all ordinary and Aeon condition expressions from the independently tested temporary fixture.
Its builder support is whitespace-normalized identical to that fixture's support.
The meaningful changes are the portable class name, generated-file structure, and replacing handwritten native-pair/page-action expressions with expressions taken from the copied MinaEpil source.
The native-pair expression still negates the nested dialog-seen/answer-not-selected conjunction and requires Chivarro's searching etude.
The pair cue remains an empty native condition checker.
The eight MarkCuesSeen actions retain their original ordering and resolved page GUIDs.

## Defaults, aliases and native types

I freshly decompiled the installed parent's ConditionsBuilder, story-condition extensions, ElementTool and MarkCuesSeen extension to compare their behavior with the fixture support.
The fixture preserves explicit negation, nested OrAndLogic checkers, UseOr versus default AND, and parameter ordering for EtudeStatus.
Nullable booleans retain the native object's constructor defaults when absent, matching the parent's builder assignments.
DialogSeen, AnswerSelected and FlagUnlocked retain their native reference fields and requested values.
I also checked the native FlagUnlocked declaration: SpecifiedValues is initialized to an empty list, so the fixture's untouched default matches the parent's null-list normalization for these expressions.
The MarkCuesSeen fixture uses the actual native action class with the same reference array order.

Aliases are resolved from copied MinaMain etude declarations and copied page declarations, and unresolved RanRom aliases are rejected.
The generator validates the pinned copied evidence before producing output.
The provenance records the parent and game assembly hashes and decompiler version.
Those provenance entries identify the source version; the generator does not inspect the user's installed assemblies on every invocation or prove compatibility with an updated parent DLL.
New parent evidence requires a new review rather than merely accepting regenerated output.

## Boundaries

The small authored builders reconstruct native condition and action objects.
They do not invoke the parent builders, run parent initialization, execute populated CanShow or prove Unity condition results.
Validator logging, generated element names and full parent configuration behavior are not reproduced by this support code.
The integration harness separately assigns and checks owners before attachment.
These limits are documented honestly in the fixture README and handoff.

Root can adopt the portable fixture calls in Program and run the shared managed suite.
No additional full-suite rerun was needed to establish this focused portability and semantic comparison.
The production integration's separate live-epilogue, save/load and optional RanEpilogue limitations remain unchanged.

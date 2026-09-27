# Parent ending metadata and policy handoff

The implementation is frozen for independent review and is not self-approved.
Only `src/Story.cs`, `tests/ParentEndingRulesTests.cs`, and this handoff were changed for this task.
Existing remote-invitation support remains intact.
No Main, Program, exporter, native helper, shared story export, or installed files were changed.

## Frozen files and source contract

| File | SHA256 |
| --- | --- |
| `src/Story.cs` | `68B2EC5FAB274A22583F61AA29AAB604079D63350DB37F1EDC00C98ACC811373` |
| `tests/ParentEndingRulesTests.cs` | `1D038DEA146908CE25AA7D505662AD1E4D2D5FF50AF4A37C9BED8B5354D2FAC2` |
| Reviewed Python manuscript | `BD12627BB8F5BA80DAB93746388BC714E34B058AF76D2F65D6D64CFCC6EAF7FF` |
| Isolated policy candidate | `C693521614A03C5DD1B75C79C1773183D8A6EE694212963D6F21A916BBC8D85D` |

The implementation follows `reference/canon-review/minagho-chivarro-ending-contract-third-review.md` and the actual 35 ordinary entries and three loss rules in `storylines/minagho_chivarro_continuation.py`.
It retains the corrected paired divine-dragon text as data rather than rewriting it in C#.

## Metadata

`Story.ParentEpilogueEdits` is a dictionary keyed by the actual original cue GUID.
Its typed `ParentEndingEdit` values retain `ParentKey`, `LocalizedKey`, nullable `Text`, `Owner`, `Requires`, and `Forbids` with the Python contract's spelling.
Null text means suppression of that cue; an alternate carries its private key and exact authored text.
`ParentKey` is evidence for a later runtime original-key check, never permission to mutate the original localization entry.

`Story.ParentEpilogueLossRules` is a list of typed `ParentEndingLossRule` values.
It retains `Id`, `Owner`, `Requires`, `Forbids`, `ReplacementScenes`, `SuppressPages`, `SuppressCues`, and `SurvivorAlternates`.
The survivor map is keyed by original cue GUID and uses `ParentEndingText` values containing private key and text.
The descriptive Python `Survivor` label is omitted because the actual conditions and target map determine runtime behavior.
Neither pure selection nor localization depends on that label.
Absent metadata produces empty collections and leaves existing story behavior unchanged.

## Pure API

`Rules.ParentEndingLoss(story, owner, state)` returns the single currently earned loss rule or null.
It requires every current rule prerequisite, no current forbidden flag, and an existing corresponding scene with that exact owner that is currently available or already seen.
A saved replacement-scene name cannot substitute for a missing scene, changed current death flags, or unearned invitation.
Previously played replacement text can continue to justify arbitration after that scene ceases to be newly available.
The rule still requires the current native death observations.

`Rules.ParentEndingPageSuppressed(story, pageGuid, owner, state)` reports whether that earned rule suppresses the page.
`Rules.ParentEndingCue(story, pageGuid, cueGuid, owner, state, out alternate)` returns `Original`, `Suppress`, `Ordinary`, or `Survivor`.
The out value is supplied only for ordinary or survivor replacement text.
Precedence is suppressed containing page, earned survivor alternate, earned loss cue suppression, ordinary edit, then original.
The eventual binding can use the returned alternate's private localization key to identify the separately registered variant cue.

Pass the actual epilogue evaluation context as `owner`.
Ordinary metadata applies to `Epilogue`; `AeonEpilogue` retains the original family.
An Aeon mythic flag is not used as a substitute for knowing which native timeline is being evaluated.
Commander sacrifice alone does not match any loss rule.
Ordinary relationship edits require invitation, except the three earlier-reunion rewrites, which require played arrival.
All ordinary edits forbid either woman's actual death.

These functions never write flags, mark cues seen, execute actions, or evaluate native page/cue checkers.
They do not emulate native parent selectors.
Call them within the independently reviewed native helper's stable evaluation batch, while preserving the original checker and behavior objects.
Ambiguous loss selection throws rather than choosing the first entry; the helper's existing observation-error fallback must preserve original output.

## Validation

`Rules.Validate` checks the metadata after the existing complete story validation.
Validation rejects noncanonical or empty target GUIDs, unknown or conflicting flag aliases, malformed referenced native GUIDs, contradictory gates, wrong owner, and nonunique rule IDs.
It pins the two exact native death aliases and prohibits authored state or other bindings from counterfeiting them.
Earned invitation aliases cannot be replaced by a native binding.
Ordinary metadata must retain both death exclusions and the reviewed invitation/arrival gate.

Private keys follow the existing `Tirabade.Minachiv.ParentEnding.<guid>` and `Tirabade.Minachiv.Survivor.<guid>` conventions and are globally unique within this contract.
They cannot alias an original key.
Replacement prose cannot be blank; survivor prose cannot be null.
Loss rules must distinguish the current state of both women and require at least one woman's actual death, not merely sacrifice.
Every replacement scene must exist, have ordinary owner and `minagho_chivarro` relationship, and retain the rule's death requirements and exclusions.
Every survivor target must also be suppressed by that rule and leave one woman alive.
Co-applicable loss rules with compatible prerequisite conjunctions are rejected, avoiding order-dependent selection.

Runtime integration must still resolve each GUID to its actual expected blueprint kind, verify original text keys and page membership against the reviewed native contract, and retain the native selectors.
The pure story model cannot establish those native facts.

## Focused checks

Temporary directory: `C:/Users/Z/AppData/Local/Temp/parent-policy-9fa9b612`.
Its `candidate.py` imports the actual reviewed Python metadata and continuation scenes into the prior isolated 538-scene invitation candidate.
The result has 585 scenes because the 47 continuation scenes are included only in that temporary candidate.
No generated shared output was touched.

Run `dotnet run --project Rules.csproj -c Release -- candidate.json` in that directory using `C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe`.
Result: 356 parent-ending policy assertions and 1,075 retained-recovery/invitation compatibility assertions passed.
The rules compile was clean.
The same Story.cs compiled for net48 through isolated `NativeRules.csproj` with zero warnings and errors.

Coverage includes every ordinary cue, invitation versus arrival, untouched parent-only saves, current versus Aeon context, all three loss rules with interrupted and completed replacement scenes, already-seen replacements, unavailable or missing replacements, current evidence lost after a scene was seen, sacrifice alone, page/survivor/cue precedence, private text identity, and JSON round trips.
Malformed cases cover GUIDs, alias conflicts, duplicate private keys, original-key reuse, wrong-owner or missing replacement scenes, removed death evidence, overlapping rules, and invalid survivor targets or prose.
The previous Konomi recovery and remote-invitation suites passed unchanged in the same isolated run.

The new focused suite is not registered in shared Program because that file was outside this task's ownership.
Root should register it once the exported metadata is present, then run the integrated suite.
Production metadata export, native blueprint registration, owner-safe attachment, Harmony page hooks, save/load, ToyBox behavior, and actual epilogue playback remain pending integration and verification.

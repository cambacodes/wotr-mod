# Parent ending typed policy independent review

Verdict: revision required for one validation defect.
The unchanged reviewed candidate selected the expected outcomes in the independent state matrix.
This review does not approve native integration, parent initialization, epilogue playback, or a release.
I reviewed the typed policy authored by another agent and did not edit its implementation or tests.

## Finding

### Medium: a native alias can replace earned invitation or arrival

`src/Story.cs:431` through the Gate predicate checks reject an alias that is both authored and native.
They do not require the two earned witnesses to remain authored or independently prohibit those names in native binding collections.
Removing the authored writes first therefore bypasses the collision check.

I reproduced both cases against the actual isolated candidate:

1. Remove every choice Set entry for `minachiv.invitation_kept`, then bind that alias in Story.Etudes to `813cc79c053d4b3e869a0d0ca2f3d85d`.
2. Rules.Validate accepts the changed story.
3. A snapshot containing only that alias selects Suppress for parent cue `819314e916514a498a8e336371b4788e`.
4. Repeat with `minachiv.arrival_kept` removed from authored writes and supplied by the same native binding.
5. Validation again succeeds, and a snapshot with that alias selects Ordinary for reunion cue `c47829fba057400c8e0279990be3d25e`.

The native etude in the probe is a valid existing binding, not a malformed GUID.
The selected policy is the actual production Rules.ParentEndingCue result.
This violates the handoff's guarantee that native bindings cannot replace earned invitation evidence and the contract's requirement that the earlier reunion reflect played arrival.
It is a validation defect for changed metadata; the frozen candidate itself still has the intended authored witnesses.
The repository test only adds a native invitation binding while retaining the authored writes, so it exercises the collision case and misses replacement.

Require the earned witness names to remain authored and reject them in every native binding collection even when the authored counterpart is absent.
Add replacement tests for both invitation and arrival, alongside the existing simultaneous-collision test.
The current selection functions can continue relying on validated snapshot names after that boundary is enforced.

## Reviewed artifacts

| Artifact | SHA-256 |
| --- | --- |
| `src/Story.cs` | `68B2EC5FAB274A22583F61AA29AAB604079D63350DB37F1EDC00C98ACC811373` |
| `tests/ParentEndingRulesTests.cs` | `1D038DEA146908CE25AA7D505662AD1E4D2D5FF50AF4A37C9BED8B5354D2FAC2` |
| Python continuation manuscript | `BD12627BB8F5BA80DAB93746388BC714E34B058AF76D2F65D6D64CFCC6EAF7FF` |
| Independently regenerated candidate | `C693521614A03C5DD1B75C79C1773183D8A6EE694212963D6F21A916BBC8D85D` |

I read the complete policy implementation, its validation, the repository suite, the implementation handoff, the actual Python ordinary/loss metadata, and the third ending-contract review.
The regenerated candidate has 585 scenes, including the 47 continuation scenes, 35 ordinary cue edits, and three loss rules.
Its hash matches the author's frozen candidate.
The Python correction preserving the paired divine-dragon accompaniment survives unchanged in the candidate data.

## Selection findings

The ordinary edits distinguish invitation from the three played-arrival reunion rewrites.
Either current death excludes ordinary living rewrites.
Loss selection requires earned invitation, the exact current death combination, and an existing replacement scene with the correct owner that is available or recorded as seen.
A seen replacement does not substitute for invitation or current death evidence.
Unavailable unseen replacements retain original output, matching the contract's fallback requirement.

Page suppression precedes survivor alternatives, which precede dependent-cue suppression and ordinary rewrites.
The four survivor targets retain their exact private text objects.
Both-loss and Minagho-loss suppress the specified pages; Chivarro-loss preserves the single-woman pages while suppressing paired output and substituting the specified mixed passages.
Commander sacrifice alone does not create a loss selection.
AeonEpilogue context remains outside the ordinary policy even when all ordinary flags are supplied.

The shared original reunion key has separate private alternate keys for its two cue identities.
All 35 probes attempting to reuse their respective original localization keys were rejected.
Unchecked ambiguous runtime loss metadata throws instead of choosing an arbitrary first rule.
The native caller must catch such observation failures and retain original behavior, as required by the separate helper contract.
The pure functions do not mutate flags, mark native cues seen, run native actions, or replace native selectors.

## Independent verification

Temporary directory: `C:/Users/Z/AppData/Local/Temp/parent-policy-independent-43cf9a`.
I copied only harness configuration into this directory and regenerated candidate.json using the actual reviewed Python metadata and scenes.
Audit.cs contains the two alias-replacement reproducers and the independent cases.
No implementation, repository test, shared export, or shared build output was modified.

The author's suites reproduced successfully: 356 parent-policy assertions and 1,075 retained-recovery/invitation compatibility assertions.
The independent matrix passed 18,469 checks over ordinary/Aeon context, all combinations of invitation, arrival, both death flags, completion, closure and sacrifice, and absent/present replacement-scene history.
The count also includes unchecked ambiguity rejection, all ordinary original-key substitution probes, and the shared-native-key/private-key distinction.
The separate alias-replacement probes printed the two accepted malformed cases reported above.
The net48 compile of frozen Story.cs passed with zero warnings/errors.

```powershell
& C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe run --project C:/Users/Z/AppData/Local/Temp/parent-policy-independent-43cf9a/Rules.csproj -c Release -- C:/Users/Z/AppData/Local/Temp/parent-policy-independent-43cf9a/candidate.json
& C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe build C:/Users/Z/AppData/Local/Temp/parent-policy-independent-43cf9a/NativeRules.csproj -c Release --nologo
```

These are pure story-policy and metadata checks.
They do not establish native GUID type resolution, original key verification, native page membership, action ownership, native ShowOnce behavior, hook ordering, scene delivery, or runtime save/load.
Those remain separate integration requirements after the validation defect is corrected and reviewed.

## Targeted rereview after correction

Current verdict: pass for the corrected typed policy and validation, within the pure-policy scope of this review.
This supersedes the initial revision-required verdict above while preserving its evidence.
No native integration or installed behavior is approved by this result.

| Corrected artifact | SHA-256 |
| --- | --- |
| `src/Story.cs` | `4442C5D543C46D8B3A6744448ED03B92E7A7BB463BDECF09749CA9B5DCB1E889` |
| `tests/ParentEndingRulesTests.cs` | `AF72E00E903B7D86DDA6BD5360C7200DC6620B48BAB7BFE31DF29D4B343BCD4C` |

The corrected validator independently requires both earned witnesses in authored state and rejects their presence in native or derived bindings.
It no longer relies on a simultaneous authored/native collision to reject a native substitute.
The two repository regressions remove every authored choice write before substituting a native binding.

I reran both original independent reproducers against the corrected source; both now reject the malformed metadata.
I also added twelve independent replacement cases covering both witness names in Etudes, CompletedEtudes, CompletedQuests, SeenCues, SelectedAnswers, and StartedDialogs.
All twelve were rejected.
The full independent run passed 18,481 state, precedence, private-key, ambiguity, and alias-replacement checks.
The corrected repository suite passed 358 parent-policy assertions, and all 1,075 retained-recovery/invitation compatibility assertions still passed.
The isolated net48 compile remained clean with zero warnings/errors.
The candidate and Python manuscript hashes remain those recorded above.

I found no remaining defect in this reviewed pure-policy change after the correction.
The native integration requirements and limitations recorded above remain outstanding.

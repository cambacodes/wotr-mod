# Soana continuation integration review

Independent technical review on 2026-09-25.
The revised six-scene contribution is accepted for bounded integration, with no remaining source or rules blocker found in this scope.
This is not approval of a complete Soana route, actual Unity execution, literary quality, or the required 21,000-word floor.
The reviewer did not author this contribution and changed only this report.

## Exact scope

| File | SHA256 |
| --- | --- |
| `storylines/soana_continuation.py` | `5723D79D16A1B6B821CAF9B679EB19E2FDA8EF6AAF2584A01D396B43E1567EF8` |
| `tests/SoanaContinuationTests.cs` | `D1142E2E203181424060C740D24D16B8BBCDEF659750C01CC1868E0F65A87940` |
| `development/soana-continuation-review.json` | `6E313248A2251F5DBA9C98C8A4EEB692EB6152D713D0CBDDC3EB2B84A3918A26` |
| `src/Story.cs` | `DD6B591E40FEDD2EAF6BACD4D58E6B86C7BAD50FD80569EBCEECE872C3467F8D` |
| `src/Main.cs` | `F1AE3AECD57BAD6DADF2E25F11D18D3756802E9D3733E74A06F72A10E2F0DFEA` |
| `src/NativeContact.cs` | `27E573ECFB994609730B265646EA7B6D4AFFC47B394A50B6D6BB2287D0FA957D` |

All six staged scene objects exactly match the imported final source.
Compared with the current 234-scene main development payload at review time, the 240-scene stage adds only these six scenes and changes no existing scene.
Its Etudes, CompletedEtudes, CompletedQuests, SeenCues, SelectedAnswers, and StartedDialogs dictionaries are identical to that main payload.
The older combined Arsinoe/Soana stage was not used for approval because it predates these interruption fixes.

## Entry and protected history

The actual three-scene opening produces `soana.opening_kept` and `soana.inquiry_invited` for the first continuation.
Each following visit requires the prior played milestone and a 24-hour gap.
The focused tests play that opening with living-guardian, dead-bear, and overlapping native outcome markers, both with and without the opening's explicit attraction.
Continuation does not require prior attraction to grant practical companionship or later informed courtship.

All scenes retain `soana.after_quest` and either `soana.old_defender` or `soana.bear_dead`.
The verified native aliases remain AfterQuest `fccdd316924af204da00c99f01c0e222`, OldDefender `c97882cbc65c4c546aed1810627a5b81`, and BearDead `995f0ac2951bbb041b062806c163fbf1`.
Dead-bear dialogue takes precedence when both outcome markers exist: every living-bear option requires OldDefender and forbids BearDead.
Neither quest completion nor NewDefender is substituted for a living actor or a recovered Orso.
No new choice sets any native history alias, revives anyone, mutates another romance, or grants `soana.lovers` or `soana.committed`.

The active unit remains `64805abb52739e44280a758f850b300c`, and entry remains native AnswersList `2b1776f3e398685479ff6b16290b4cc2`.
All visits are optional physical chapter-three conversations, with no automatic rest delivery or invented late-campaign contact.
There is no explicit area GUID restriction, matching the opening's contract; availability relies on the exact local native actor and its postquest dialogue attachment.
The native reader requires a unique exact blueprint match in the loaded area, a loaded holding scene, usable conscious living actor, nonhostility, and an available conscious Commander outside combat.
It does not summon, unhide, recruit, or restore the speaker.

Soana death, Camellia death, and forest destruction remain relationship-level unavailable states and are rechecked inside active scenes.
Positive prerequisites, supported guardian alternatives, and chapter limits also remain active during continuation.
Authored closure and entry delay are deliberately not reapplied midscene, allowing the final refusal/goodbye to finish after `soana.closed` is selected.
The scene-level `inhuman` exclusion remains an entry restriction; this report does not claim a new midpage mythic-transition guard beyond the existing engine contract.

## Interruption and skill-check behavior

The author reproduced contradictory replay histories before the final revision.
The revised choices prevent accumulation of opposed warning configurations, warning dispositions, relationship paces, and final intimacy outcomes.
The recorded watch result disables another roll and offers the appropriate continuation for its existing evidence.
The non-roll patience option cannot replace an already recorded success or failure.
Previously chosen high/daywatch, retained/removed, courting/friend/wait, and kiss/hand/slow decisions remain the only compatible alternatives after reentry.
These guards preserve an already selected decision rather than resetting history.

The first-kiss flag is written by the response after the kiss passage, not by the preceding request.
Courtship is required to reach that passage, and recorded friendship or waiting cannot acquire it through replay.
Some approach and decision flags remain preterminal by design; the later scenes require completed milestone flags, so those partial decisions alone do not unlock the subsequent visit.
The review does not claim that interruption rolls back every decision or that book reentry resumes the exact last page.

The single native check is Commander-only `SkillPerception`, DC22, with distinct `found` and `missed` targets.
Success supplies direct observation; failure startles the boar and requires indirect testing; the non-roll alternative spends additional narrated daylight observing with Soana.
The check itself does not record an outcome or complete the scene.
Its result flags are applied after their corresponding pages are acknowledged.
No successful roll is required for continued companionship or romance.

The existing Main builder attaches scene contact conditions to choice display, choice selection, action execution, and native check selection.
An invalid contact action returns before recording progress.
Each contact page has a stable, flag-free exit when contact is lost.
That exit does not complete the scene or remove recorded choices.

## Independent verification

A read-only traversal imported the actual opening and revised continuation modules and exercised all 68 continuation pages.
It retained flags used by prerequisites, choices, and the exclusive outcome groups while discarding irrelevant equivalent history for efficiency.
It checked 6,660 distinct interrupted scene/history pairs across all three guardian histories.
Every replay had a completing path, every exclusive outcome group remained consistent, and friendship/waiting never gained a kiss.
No authored choice wrote a staged native-history key.
This source traversal verifies graph and flag behavior; it does not replace actual engine contact tests.

The reviewer independently reran the already built rules executable against the exact isolated stage above.
It passed 10,877,985 assertions, including the final `SoanaContinuationTests` actual opening/continuation and interruption tests.
The command was `dotnet tests/bin/Release/net8.0/RulesTests.dll development/soana-continuation-review.json` using the local RanRomanceTools .NET host.
No test, source, or generated export was edited for this review.

The parent separately reported 395 binding checks over 74 typed targets and 29,428 managed assertions over 8,767 generated blueprints for this stage.
The parent-reported built DLL hash is `F81C0C7BD279C832F73B01CD5F5E44B6C37570F675B8873540C7C7D2B30188F4`.
Those binding and managed counts are attributed to the parent, not represented as an independent rerun here.

## Runtime and complete-route limits

Actual Unity verification remains necessary for native answer-list insertion, live actor state changes, native roll UI and actor selection, result routing, contact loss between scheduling and execution, and real save/resume behavior.
The book's narrated warning apparatus is not a placed trap, inventory craft, persistent world object, or changed forest AI.
Local identity checks do not establish visual quality, portrait cropping, voiced presentation, or live ToyBox compatibility.
The contribution structurally leaves other relationships untouched and imposes no jealousy flags, but the relevant ToyBox combinations still require runtime testing.
Later chapter access, credible Trickster recovery, mythic-specific expansion, sustained relationship development, commitment, and endings remain outside this bounded contribution.
Its technical acceptance does not satisfy those remaining route requirements.

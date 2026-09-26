# Aranka living-island continuation handoff

Author ownership is limited to `storylines/aranka_continuation.py`, `tests/ArankaContinuationTests.cs`, `reference/canon-review/aranka-extension-evidence.md`, and this handoff.
No shared registration, existing story source, parent dialogue, native blueprint, installed asset, or art file was edited.
The contribution requires independent literary/canon and integration review before promotion.
No author-assigned quality score or full-route approval is supplied.

## Frozen revision

| File | SHA-256 |
| --- | --- |
| `storylines/aranka_continuation.py` | `C625824011CC70DA7A742E84DB20A9E791AF474B944666384500FBC288917B61` |
| `tests/ArankaContinuationTests.cs` | `00E33D9DDFF1270C7882301DC9E8B503840439F2F0AF313E4AE90941EB656479` |
| `reference/canon-review/aranka-extension-evidence.md` | `5F82B106B44DE06030DA8BA7427CF515750CF68BC58ABD426E723C961022D876` |

The earlier D36 source freeze was superseded after tracing the alternate Azata first-flight ending of Book04.
The final revision includes that real endpoint rather than silently excluding the natural current-Azata island history.
The independent reader then identified Sella's inconsistent presence, an unsupported cut-song callback, and shoes moving without being picked up.
The released source makes the shared laugh refer only to Aranka, establishes Sella's separate familiar solo on every performance branch, and picks up the shoes before the night-path movement.
Comparison with the previous review candidate confirms seven exported node Text changes only, with all IDs, choices, indices, gates and effects preserved.

## Integration contract

Append `SCENES` and merge exported `ETUDES`, `SEEN_CUES`, `COMPLETED_QUESTS`, and the `RELATIONSHIP` entry under `aranka`.
Register `ArankaContinuationTests.Run` in the parent-owned test runner.
The source imports existing `story_format` helpers and uses no new runtime service.
The portrait key is `Aranka`; parent integration must bind verified appropriate Aranka art before publishing.
There is no new image in this contribution.

All scenes require the current installed romance Playing, successful parent quest completion, and at least one exact parent ending cue.
Ordinary Book04 and alternate Azata Book04 endpoints support the keep-artifact history.
All four Book14 endpoint variants are recognized, with the current romance independently required.
A rejected parent romance does not become eligible from an ending alone.
Overlapping keep/release histories conservatively use the relinquished-artifact text and suppress the flight and Reverie callbacks.

Every visit requires native Aranka unit `430cba7801b149b4e8494ace6baf4f7c` actually available on island area `31bab5549f7ea384186159a238360c8d`, in Chapter 5.
Attachment is the existing reusable DesnaAdepts answer list `5ff8a80442182f84e849b4281f98b9ca`.
This is a waking local continuation, not a remote dream or proof of a Drezen resident.
The native-contact audit, endpoint excerpts, parent counter ownership, and current spawn limitations are recorded in the evidence file.

Existing native/parent flags are read only.
No original node, answer index, quest objective, romance counter, mythic state, artifact, unit, or pet is changed.
The new relationship record names extension progress and does not repeat parent acquisition.
It does not set a new parent commitment or modify the existing parent journal.

## Played content

| Scene suffix | Delay | Development |
| --- | ---: | --- |
| `the_wrong_refrain` | Initial | Reconnect as established lovers, recognize compass history and optional earned dream flight, and choose an open gathering or small musical rounds. |
| `where_the_breath_goes` | 24 hours | Perception DC 26 identifies a breathing/timing conflict; failure shortens rehearsal and requires rest; a slower non-roll approach also works; choose to sing one line or listen. |
| `the_name_missing` | 48 hours | A woman contests an invented heroic verse about her absent brother; Aranka makes a correction and chooses an unresolved ending or an audience response. |
| `an_evening_uncommanded` | 48 hours | Rehearsal outcomes and venue change the performance setup; Diplomacy DC 25 can redirect attention, fail into a ceremony that cuts the program, or be bypassed by stepping aside. |
| `the_song_afterwards` | 48 hours | Hear the performance's actual costs and successes, preserve attraction through disagreement, and discuss limited future travel or continued meetings. |
| `no_encore_needed` | 48 hours | A private island evening includes optional acknowledgment of an actually established Reverie partnership and separate shared-night, kiss-only, and quiet outcomes. |

The two trials have real text and later consequences, but do not remove the established romance for a failed roll.
They use Commander-only native skill checks, not a fictional Performance skill or an invented combat reward.
Sella, Rovan, Neris, Deren, the refrain, the contested verse, and these encounters are authored additions.
The song does not replace the native Starward Gaze choice.
Rovan's injured voice is not magically healed, and Neris is not required to praise the correction.
Aranka remains interested in travel, invention, an audience, Desna, other relationships, and a life beyond the Commander's schedule.

All authored outcome flags commit only at terminal choices.
The two trials use local copies of their shared closing pages to carry mutually exclusive outcomes to the terminal selection without writing a partial persistent result.
Those repeated pages do not add distinct content credit.
An interrupted scene can restart without combining a failed and successful trial history.
The parent romance ending or the exact actor becoming unavailable stops live contact through the existing contact rules.

The optional Reverie passage requires `aranka.ran_reverie_partner` and a supported keep-artifact finale, with no release finale.
It acknowledges the existing shared relationship, does not start one, and does not summon a corporeal Reverie actor.
The existing Kiana/Aranka draft remains unapproved and unexported.
No new Kiana attraction or group outcome was invented without current-contact evidence.

## Native voice passages used

These excerpts were resolved directly from the installed blueprint text keys and English localization.
They support the new portrayal; the new scenes remain authored fiction.

MusicVsMusic/Cue_0001, `b76b67f369adfd44fa4fb85f4d47ff4d`:

> "You're my dear friend, Ilkes, but sometimes I just want to shake you. Yes, Desna is our goddess, but she's the goddess of freedom. We mustn't follow her blindly."

MusicVsMusic/Cue_0017, `f778f672902b3c54e8424a7b4d9748b7`, explains her objection to choosing only a stronger inherited relic:

> "Something equally powerful? No. But the instrument we'll craft will be ours alone. Besides... the Bell is dedicated to Desna. Even though I worship her with all my heart, I realize she's not a deity that all free crusaders would follow."

DesnaAdepts/Cue_0005, `2c84efa67859baa4bba26dcc43d1149b`:

> "Wallflower, I've told you so many times, you have an amazing voice! So deep, so striking... I'd have you trained up in a snap if only you wanted to sing!"

DesnaAdepts/Cue_0022, `091e0386df4207a4c8cd5eab0910bc29`, opens her account of traveling with her parents' blessing:

> "I love my home and my family, but my talents as a bard and the call of adventure never let me stay home for long. My parents have never minded."

DesnaAdepts/Cue_0034, `06752003a64374741804b8ca89ac90f8`:

> "Il, you're hilarious. Of course I don't! What Desnan bard would actually miss the city?"

These passages informed her delighted irreverence, practical musical attention, religious independence, and desire to travel.
They do not make the new performance dispute, injured percussionist, prayer, or romantic evening native facts.

## Amount and selected paths

The six visits export 67 pages, 10,240 raw words and 8,308 distinct whole-segment words under the existing project tokenizer.
Of the raw total, 1,932 words are exact repeated segments, primarily the terminal-commit copies.
These repetitions receive no distinct volume credit.

The installed parent route was rechecked from actual configuration-call reachability and matching installed DLL/localization hashes.
It contains 15,758 distinct normalized-text words, across 440 configured localization keys.
The deduplicated union of those verified parent segments and this new contribution is 24,066 words.
That is an attributed aggregate spanning alternatives and parent journal/epilogue text, not the amount read in one playthrough.
It passes the 21,000-word meaningful aggregate planning floor; literary parity and full character depth still require comparative review.

| Supported parent history | No existing Reverie partnership | Existing Reverie partnership |
| --- | ---: | ---: |
| Ordinary keep-artifact ending | 4,957-5,180 | 4,957-5,355 |
| Azata first-flight ending | 4,957-5,355 | 4,957-5,530 |
| Relinquished artifact | 4,977-5,200 | 4,977-5,200 |
| Overlapping finale history | 4,977-5,200 | 4,977-5,200 |

These are the selected words in the new six-visit arc only.
They include the actual selected prose and choices, both check outcomes, and optional earned callbacks.
They exclude aborted visits, titles, journal metadata, unselected choices and the earlier parent's played text.
There are 432 distinct completed outcome combinations per seeded history scenario.
The enumerator merges only identical flag states while retaining minimum and maximum cumulative length, so optional callbacks remain in the appropriate bounds.
No selected parent-plus-extension campaign length is claimed.

## Focused verification

Temporary isolated project: `C:/Users/Z/AppData/Local/Temp/aranka-continuation-check-w_jj331o/Check.csproj`.
Candidate JSON SHA-256: `6CD3577E9E06555C263F2F9EB05C1D9A9C703890C655AEC94CB095BC24D324A1`.
The temporary candidate includes existing content as scaffolding and the exact frozen Aranka scenes, without replacing a shared or installed build.

```text
dotnet run --project <temporary-directory>/Check.csproj -- <temporary-directory>/story.json
PASS 171088
```

The run calls actual `Rules.Validate` and then the focused test through the repository's actual `Program.Walk` and `Program.Copy` helpers.
It covers ordinary keep, Azata flight, release, overlapping endpoints, and current Reverie partnership or its absence.
It traverses every exported page, both skill-check outcomes, non-roll choices, all performance consequences, all intimacy endings and terminal-only state commits.
It checks missing prerequisites, no final cue, no current romance, wrong chapter/area, missing actor, interrupted disappearance, parent romance ending, native history exclusions, completed replay, and delays.
It verifies other romances and parent/native predicates remain unchanged.
Both failed musical trials can still reach a mutually chosen intimate ending.

Parent checkpoint states are seeded from the separately traced native code, not earned by executing the installed parent's Unity book events inside the test.
These are Rules-level tests, not a live game E2E session, art inspection, ToyBox-version compatibility run, or independent literary approval.

## Remaining requirements

The island's native mechanics and actor availability still govern access.
This slice does not provide the mandatory bespoke attainable Trickster acquisition/contact route, nor resurrection, later relocation, or access for every former-Azata save.
No historical etude is cleared to disguise those gaps.
Other mythics retain the source restrictions, and an unsupported inaccessible actor stays inaccessible.

Parent registration, proper portrait binding, native attachment checks, independent writing/canon review, and actual Chapter 5 save/load verification remain required before release.
The parent-plus-extension comparison still needs to judge quality and depth, not just the aggregate planning floor.
No approval score is promised.

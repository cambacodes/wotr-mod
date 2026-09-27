# Gesmerha campaign contribution

This is an unintegrated, bounded living-character contribution, not a completed route or a RanRomance parity approval.
The existing six opening scenes remain unchanged.
Independent review belongs to `reference/story-review/gesmerha-campaign-first-review.md`.
The author supplies no review scores.

## Integration contract

Import `storylines.gesmerha_campaign`, append a deep copy of its `SCENES`, then call `gesmerha_campaign.integrate(payload)` once.
The integration function adds one active-etude alias and three observed-cue aliases only.
It does not edit an existing scene, relationship definition, answer index, native blueprint, actor or saved outcome.
Register `GesmerhaCampaignTests.Run(story, Check)` in the root-owned test runner.
The isolated candidate extends the current builder with this module, including the already-integrated independent Tirabade routes and bridge once.

The first four new visits require the actual completed opening chain, beginning with `gesmerha.opening_kept`.
Their native area, contact actor, peaceful answer list, resolved quest, truth-or-illusion condition and mythic exclusions are inherited explicitly from the existing contract.
They remain Chapter 3 only.
The singing visit waits 48 hours after the verse decision because Vesk names two evenings as the deadline.
Other local visits wait 24 hours.

The fifth visit is Chapter 5 only, in Drezen, within Gesmerha's real native KTC audience.
It requires `gesmerha.campaign_kept`, the living contact actor, the active guest etude and an actually observed native answer about the clan's future.
It has zero delay because the audience is transient.
Marhevok's leadership explicitly excludes it.
There is no claimed Chapter 4 physical visit, late-install acquisition, permanent capital guest or later Wintersun presence.

## Played content

`a_story_from_elsewhere` fulfills the original request for an ordinary story about the Commander, then introduces competing memories of a clan song.
`the_unfinished_verse` offers a Commander-only Knowledge World DC 24 check and an available non-roll listening approach.
Success corrects the clerk's mistaken ordering promptly.
Failure requires oral reconstruction and costs Vesk the borrowed drum; deliberately listening also takes that time.
The check does not decide whether Gesmerha is attracted to the Commander.
The larger choice keeps two distinct performances or negotiates one shared version.

`the_evening_answer` plays that choice in front of the departing traveler's family.
The separate version lets Dera's voice be heard and displaces some attention from Runa's older song.
The shared version works collectively but initially credits Gesmerha for Dera's contribution, which Gesmerha corrects.
Gesmerha chooses to pay for Dera's time at the cost of delaying new tools.
She remains attached to her authority and her preferred version.
She does not require the Commander to convert her into an untroubled model teacher.

The optional Trickster rhyme experiment is asked for and bounded by Gesmerha.
It produces a ridiculous word, never an ancestor's voice or a verified recovered historical fact.
The ordinary alternative asks living families and leaves the gap unfilled.
Neither option restores her sight, changes native mythic powers, settles Wintersun or grants affection.

`what_she_asks` distinguishes existing courtship, slow exploration and explicit friendship.
Courtship or slow exploration can become a mutually chosen adult relationship, remain open or become friendship.
Existing friendship does not turn into romance without another invitation.
The relationship discussion permits other relationships, requires honest time and excludes promises made on another person's behalf.
The private-door and holding alternatives give different, graphic and explicit intimacy tempos.
The scene discusses an uncertain future absence without claiming the Commander has received an unplayed mission order.

`the_voice_at_court` remembers paired trays versus the narrow board, actual lover/slow/friend intentions and the observed native future report.
Gesmerha's departure plans remain her own.
She does not become a Drezen resident because she has a lover there.
The player can renew affection, keep a quiet meeting or end an established courtship honestly.
The native audience remains available to finish after the authored book.

Nine provisional epilogues distinguish a living reunion, no reunion, death, inhuman change, Demon, Devil, ascent, sacrifice and the separate Aeon history.
They do not assert a completed household or another physical meeting.
Death takes precedence over incompatible living outcomes; change precedes ascent and sacrifice; ascent precedes sacrifice.
Aeon uses the existing separate `AeonEpilogue` owner.
An authored romantic closure suppresses ordinary relationship conclusions, while a subsequent native death can still receive its loss account.

## Native evidence and limits

Evidence was read from the installed `D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip` and the existing native text extraction `reference/expansion/gesmerha.txt`.
Existing characterization evidence remains in `reference/canon-review/gesmerha-route-evidence.md`.
The old source supplies the real C3 quest and contact bindings.

| Role | Exact native asset |
| --- | --- |
| Gesmerha unit, both local and guest dialogue | `3ba3a0ff8575be8419159221177c1411` |
| Wintersun area | `0a5654e7dc18f074d9356009d55eb51b` |
| C3 peaceful answer list | `2063ee21356b772408f5c9cfb3ed5bd0` |
| Resolved Wintersun quest | `c0d0b565f4b725241b96c148000f1910` |
| Native death | `49839ba15f34bee469c4f093dace0811` |
| Removed illusions | `1fd9e6e1b5440ac469d5466a9b3d6814` |
| Upgraded illusions | `23a7a6020a500004daa8e2c2f47b75a2` |
| Marhevok remains chief | `baa4820ac052d664bbaa261d17ce9b08` |
| Drezen area | `2570015799edf594daf2f076f2f975d8` |
| Active Gesmerha capital guest etude | `89d57f73e41040f0ab527d6e83478a64` |
| KTC parent etude | `da452482bd2a4a8da099a3674c655b2e` |
| Native KTC dialogue | `0ade7f9a65fc414438fef23b7cd126c2` |
| Gesmerha's KTC answer list | `fb3a88e8ed751214c9136f87891ec07b` |
| Native question about future, Answer_0030 | `c182a6ee00da67047bc86b75768ba7a9` |
| Forest and mountain shelter, Cue_0015 | `64388ef1f915e8c4991848f511408fa9` |
| Migration to an unknown new home, Cue_0037 | `164cf168d833c3f4ba458f72df62bda0` |
| Default hidden capital actor etude | `bd304d5930ed4d9bb09a024b1e648bb6` |

The guest etude is `World/Etudes/Common/WrathOfTheRighteous/Chapter03/CapitalMechanic/KTC_WintersunHelp_BlindCarver.jbp` despite the Chapter 5 dialogue it invokes.
Its activation excludes both native death and retained Marhevok leadership.
It passes the actual capital spawner `b0f4f32c-6c22-42e3-96c5-4f7cab107e2b`, scene `3e2b5ea054cd5b2479e7f13134363ef4`, to cutscene `a49cdff09be24b0691a6d3d4b15e9af7`.
The cutscene lives under `World/Cutscenes/DrezenCapital/DefaultKTC_OnePerson_Devour/`.
`CommandAction.jbp` unhides and moves the supplied actor; `CommandStartDialog.jbp` invokes the supplied native dialogue.
After that dialogue ends, `CommandAction 2.jbp` completes the supplied guest etude.
The lower-priority default actor etude hides the same spawner.
Historical completion of the guest etude is therefore not used as proof of an available actor.
Native devouring answer `b90ba5a4561c9ee42a3e3eb59df20116` also causes the guest completion trigger to start native Gesmerha death.

The native future question tries Cue_0015 first when upgraded illusions play, then Cue_0037 when removed illusions play.
Both return to Gesmerha's exact answer list, permitting the private scene after the player hears one.
`gesmerha.heard_future` is the union of those observed cues; the two separate aliases select the actual report recalled in prose.
If exceptional saved history contains both observations, migration receives deterministic precedence rather than displaying two incompatible reports.
The tests distinguish that exceptional mixed-history case from ordinary native histories.

Cue_0015 explicitly says the clan leaves Wintersun temporarily for forests and mountain trails while intending to restore Sarkoris.
It does not prove the old trading actor remains present in Wintersun.
Cue_0037 gives no known destination for migration.
The separate animal-aid cue `b7981df42b1ac504683b21d11de079e0` and blindfolded-warriors cue `de348517119791d4e9f7de7de0beab25` were inspected but are not assumed or bound by this contribution.

Dera, Runa, Vesk, the departing brother, all song lyrics and disputes, paid teaching, the romance and Runa's later death are authored alternate developments.
They are not native named actors or native casualty reports.
Runa's absence does not diagnose a native forest outcome.
The dialogue does not spawn them or mark a real game unit dead.
Gesmerha's blindness, tactile practice, old scars, craft lineage, attachment to Sarkoris and distrust of deceptive certainty remain native anchors.
No optional pre-resolution conversation is falsely remembered as having occurred with this Commander.

## Verification and measurements

The isolated candidate is `C:/Users/Z/AppData/Local/Temp/gesmerha-campaign-stg4_wn8/candidate.json`.
The runner is `C:/Users/Z/AppData/Local/Temp/gesmerha-campaign-stg4_wn8/Check.csproj`.
It compiles the actual current `src/Story.cs`, the actual `Program.Walk`/snapshot-copy helpers and the new focused suite.
The command is `C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe run --project C:/Users/Z/AppData/Local/Temp/gesmerha-campaign-stg4_wn8/Check.csproj -- C:/Users/Z/AppData/Local/Temp/gesmerha-campaign-stg4_wn8/candidate.json`.

The final revised candidate passed `Rules.Validate` and 1,819,522 assertions.
The suite plays all six actual predecessors before all four local additions.
It covers all new pages, all three older relationship intentions, renewed/ended courtship, both board forms, every check branch, non-roll, Trickster and other eligible mythics, chief versus Marhevok histories, truth versus illusions and exceptional overlap.
It checks missing native prerequisites, wrong chapters, absent/dead actors, guest departure mid-page, defer without progress, completed-scene replay, unchanged unrelated romances and mutually exclusive provisional endings.
The C5 native guest and observed reports are explicit external native fixtures, not silently credited to authored choices.
No test claims to play the installed game's KTC scheduler or renderer.

Independent findings repaired before this release concern the comb's location on both paths, an unsupported visual inference by Gesmerha, a handclasp absent on the slow path, the exact warning function and unverified-history framing of the native runestones, and friendship-safe Aeon wording.
The fixes change prose only, preserving scene/page IDs, choice order, effects and conditions.

| Released artifact | SHA-256 |
| --- | --- |
| `storylines/gesmerha_campaign.py` | `174644BCCAB66EF0500295AC466B6B43B69A550FC69FF1E64577D0593A0B818F` |
| `tests/GesmerhaCampaignTests.cs` | `8B7B7C0E8F1A821C15F6BFD6660ECB9A9D27DD057B47F497EE04345A42863731` |
| Isolated candidate | `B1D59FAD467F8A43937710E03C4901CB624C4486DEE0C13CDBBC49CF17DADC2C` |

The module adds 14 books: five playable visits and nine provisional endings.
It contains 54 pages and 78 choices.
The old and new modules together contain 20 books, 101 pages and 146 choices.
Counting strips game markup and counts word tokens with internal apostrophes/hyphens retained.
Exact-segment distinct counts deduplicate repeated page and answer strings, not individual words.

| Scope | Page prose | Prose plus answer text | Exact-segment distinct prose plus answers |
| --- | ---: | ---: | ---: |
| New contribution | 8,158 | 8,826 | 8,767 |
| Existing opening plus contribution | 14,494 | 15,776 | 15,686 |

Selected measurements enumerate selectable page paths, both skill-check outcomes, actual earned relationship flags and terminal choices.
They omit deferred attempts, replay and epilogues.
These bounds allow the Trickster experiment; other eligible mythics have a lower maximum because the optional experiment is unavailable.
The C5 measurements use the ordinary native future report corresponding to the earlier illusion outcome, not a fabricated mixture.

| Selected arc | Words including selected answers |
| --- | ---: |
| Four new C3 visits | 3,031-3,830 |
| All ten C3 visits, truth and Gesmerha chief | 6,930-7,975 |
| All ten C3 visits, truth and Marhevok chief | 6,934-7,979 |
| All ten C3 visits, retained illusions and Gesmerha chief | 6,925-7,970 |
| All ten C3 visits, retained illusions and Marhevok chief | 6,929-7,974 |
| Five new visits including migration-report reunion | 4,122-4,971 |
| Five new visits including shelter-report reunion | 4,138-4,987 |
| Eleven visits including migration-report reunion | 8,038-9,099 |
| Eleven visits including shelter-report reunion | 8,049-9,110 |

The headless checks verify the story graph and availability rules, not rendering, timing inside the game's dialogue controller or an actual simultaneous ToyBox session.
An exact candidate comparison also confirmed that all preexisting scene dictionaries remained unchanged when this module was appended and its integration function applied.

Native record hashes below identify the installed source used for the new access contract.
All paths are relative to `blueprints.zip`.

| Native record | SHA-256 |
| --- | --- |
| `World/Etudes/Common/WrathOfTheRighteous/Chapter03/CapitalMechanic/KTC_WintersunHelp_BlindCarver.jbp` | `E32CA8BD8636197A7B5C27967282A525CF8F0F968E419174AB3D31A0AF7DC78E` |
| `World/Etudes/Common/WrathOfTheRighteous/Chapter03/CapitalMechanic/DrezenCapital_DefaultMechanic/BlindCarver_Gesmerha_DefaultActor.jbp` | `1D7F0C4B407E547E893072F7C32C0EDCB187360B483E634A7B99CDB66C79496F` |
| `World/Dialogs/c5/KTC_WintersunHelp/KTC_WintersunHelp_dialogue.jbp` | `5D160056FDD943F74282D5DA606B3303FA2009FD29ABBDA7751EEDCFCBA29A85` |
| `World/Dialogs/c5/KTC_WintersunHelp/AnswersList_0027.jbp` | `64437B21D7654EC9E644206D982CDDD7368B121A479C2E3E20C5986BAA2F01C4` |
| `World/Dialogs/c5/KTC_WintersunHelp/Answer_0030.jbp` | `72D937593CA260FB7E138262234C808987F40BB4936E01FAE54563BAE40FCA97` |
| `World/Dialogs/c5/KTC_WintersunHelp/Cue_0015.jbp` | `F8CD6DF057088E79B390180A1C97B82DDA54C6CF566DBF41D446732C407F4CA7` |
| `World/Dialogs/c5/KTC_WintersunHelp/Cue_0037.jbp` | `3469EC8E616F47ECA594BF2617AA2812BD963D97D0D6ECFB2804962920D626EE` |
| `World/Cutscenes/DrezenCapital/DefaultKTC_OnePerson_Devour/CommandAction 2.jbp` | `E8EEF1FCD162FD3F8B5969D6BE697AA484042CC1006200103D1486F57B31241F` |

## Remaining full-route work

The combined manuscript remains below the 21,000 distinct meaningful word planning minimum.
That minimum is aggregate, not a mandatory 21,000-word selected playthrough.
Selected-path counts must remain visible beside aggregate counts, and the full RanRomance comparison still requires independent reading of the finished campaign.

The present Trickster joke is an optional consensual use of power, not delivery of the required universal attainable route.
For a living Gesmerha after a missed KTC, a later module needs an authored voluntary contact request through a verified carrier or a real staged guest invitation, with actual dialogue delivery and an independent acceptance from her.
The verified capital spawner/default-hide/guest mechanism supplies a concrete implementation starting point, but the native one-shot etude must not be restarted blindly or treated as persistent residence.
A new route-owned guest lifecycle would need an exact unit/spawner policy, existing-native-guest exclusion, cleanup, area reload, save/reload and native-death interruption checks.

For retained Marhevok leadership, the native C5 audience belongs to Marhevok, not Gesmerha.
An authored request must reach Gesmerha separately and let her decide whether to leave the chief's arrangements, travel or communicate privately.
No current flag proves that meeting or her availability.
The native runestone investigation and the clan's contested history provide a character-specific Trickster connection: uncover a lost route or misdirected invitation without compelling her affection or changing what she remembers without consent.
That needs an actual playable attempt, truthful failure/retry or alternate approach and a delivered reply.

For native death, a separate recovery arc must establish the real death history, remains or another evidenced recovery object, the appropriate magical intervention, her own post-recovery response and an actual living actor.
The prior suspicion of runestones is a thematic connection, not proof that those stones store her soul.
Clearing `gesmerha.dead`, setting a local recovery flag or showing a portrait is not resurrection delivery.
The opened native records do not supply a verified remains-collection quest for Gesmerha.
Missed early acquaintance also requires new acquisition pages rather than setting `opening_kept` or pretending the six visits occurred.

Further content should resolve the selected maker-mark/trade history, develop the paid teaching and migration/shelter consequences, provide a genuinely later shared decision and replace provisional living conclusions only when the stronger arc was played.
Art, final comparative literary review, localization/TTS presentation, the actual KTC injection window and runtime portrait/crop checks remain outstanding.
ToyBox free-love/no-jealousy behavior is represented by preserving unrelated relationship flags and offering nonexclusive terms; actual simultaneous installed-mod interaction still needs a runtime check.

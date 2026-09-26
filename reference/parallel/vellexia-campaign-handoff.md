# Vellexia correspondence campaign handoff

Frozen for independent review on 2026-09-26.
This contribution is not an author approval, full-character completion claim or RanRomance quality certification.
Only the three assigned source, focused-test and handoff files were written.
No original route, shared builder, native archive, installed mod, art assignment or shared test registration was edited.

Source: `storylines/vellexia_campaign.py`.
Source SHA256: `24AE43736DD2C967E9E3D5BB8CCAA83816FB54D75C02C766246F53E43F5C1C99`.
Test: `tests/VellexiaCampaignTests.cs`.
Test SHA256: `668B2BF94E382C179B4D25A779755FAFD7156E750E56368E4E659092E6090BA7`.
Isolated candidate SHA256: `94B125A525514652231D6E5C14F91E580C9BA7EE0C4D1270B7C51A64BC288E41`.
Candidate path: `C:/Users/Z/AppData/Local/Temp/vellexia-campaign-pgk6ak3s/candidate.json`.
The released candidate appends 24 scenes to the current 459-scene assembly, for 483 scenes.
The first isolated run used the earlier 431-scene baseline; root integrated separate work while this contribution was reviewed.
The previous scene objects were compared before and after append-only assembly and remained equal.

## Integration contract

Import the module, append a deep copy of `SCENES`, then call `integrate(payload)`.
The integration function merges only three new seen-cue bindings and one selected-answer binding.
Register `VellexiaCampaignTests.Run` when `vellexia.the_unused_reply` exists.
Preserve the original six scenes, native relationship metadata and all existing IDs and answer prefixes.
The new module does not replace or modify any existing scene.
Root should update player guidance to explain that the two additional initial conversations must be played before accepting the native arena invitation.
The next phase begins after the original quest's ordinary dismissal and completion, through the shell in the Nexus.

The initial two conversations use the original living Default actor, Chapter 4 Upper City and original main answer list.
They require the played opening and close when the native arena invitation is seen or the quest is completed.
Their zero delay permits an extended initial visit, without taking over the three native dates.
The nine later conversations use `Owner=Memory`, `Remote=True`, no ContactUnit, and the Nexus in Chapter 4 or Drezen in Chapter 5.
Each requires the exact witnessed ordinary dismissal, the completed native quest and the previous authored milestone.
Each has a 24-hour delay.
They do not grant physical access to Vellexia in either location.
The echo pair is explicitly offered, voluntarily accepted and tested in the initial local visit.
It carries a requested voice and small image only when both covers are open.
It is an authored story object, not a claim that a native inventory item or summoning feature was delivered.

## Played spine

| New visit | Purpose and lasting choice |
| --- | --- |
| `the_unused_reply` | Offer and test the voluntary echo pair before the native dates; refusal/defer does not acquire it. |
| `the_price_of_tomorrow` | Ilveris's prediction trade and Tessar's note; actual kept/returned portrait callback; optional hand-only or explicitly chosen kiss. |
| `the_second_invitation` | Acknowledge her real native dismissal; her motive is a seller claiming authorship of her changing interest; choose bounded clerk terms or equal access to the account, or refuse the correspondence. |
| `the_claim_before_the_event` | Commander-only World DC29 comparison; success identifies dated additions, failure receives a correction and costs an additional appointment, non-roll inquiry also consumes that appointment; choose an initial accounting or public-challenge approach. |
| `the_clerks_own_price` | Tessar owns her ambitions and complicity; permit a named work sample or a restricted sample plus attestation, with Vellexia separately agreeing about her own name. |
| `the_wager_with_an_edge` | Publish the checked account without risking the silver, or accept a witnessed wager with a drawn or Commander-selected order. |
| `an_hour_that_counts` | Publication, won wager, knowingly lost wager, or voluntary Trickster memory experiment with a real forfeit; the result is resolved rather than deferred to a future sequel. |
| `the_question_after_business` | A new, explicit relationship choice after work is paid; lovers, slower exploration or company without romance. |
| `the_voice_after_the_abyss` | Chapter 5 return; distinct professional result and Tessar's named/limited sample consequences. |
| `two_unremarkable_pleasures` | Shared private time at separate tables; personal papers and old scents; affectionate discussion of wanted physical contact without pretending it happened. |
| `the_cover_before_the_battle` | Earned farewell; retain lovers, choose lovers from the slower history after explicit terms, retain friendship or uncertainty, or end contact. |

All outcomes are terminal-only.
Deferring or interrupting a page does not collect relationship decisions before completing the conversation.
The initial artist disposition, renewed affection, wager results and sample permissions receive conditional text.
The initial accounting/challenge preference produces a distinct immediate exchange and proposed work; the final decision may legitimately differ after the actual offer arrives.
A method preference is not a compulsory later vote.
No agreement changes another romance, grants another person's consent or requires monogamy.
No coercive native Demon outcome is treated as consent.

## Native evidence and authored development

Read the actual original module and the evidence in `reference/canon-review/vellexia-route-evidence.md`, `reference/parallel/vellexia-opening-handoff.md`, and `reference/expansion/vellexia.txt`.
Read installed main/first/second/third-date cue, answer, unit, area-mechanics and etude records.
The original three dates and their conclusions remain native work.
Vellexia's boredom, cruelty, patronage, pride, appetite for novelty and dangerous relationships are canon anchors.
The clerk, seller, professional dispute, silver stake, echo pair, later affection and final correspondence outcomes are authored alternate developments.
They are not hidden native quests uncovered by this audit.
She does not become morally reformed, promise harmlessness, release all victims or lose her independent ambitions.
The new paid performers and mineral/silver objects do not silently reuse her transformed victims as romantic furniture.

| New read-only binding | Exact native record | Record SHA256 |
| --- | --- | --- |
| `vellexia.dismissed_native` | `World/Dialogs/c4/RaptureOfRupture/Velexia_Third_Date/Cue_0076.jbp`, BlueprintCue `fa6db1b41f5394f4f8a23f09fc7061f7` | `8C32A18A598DF811C3D8C4B1E64518404CD94254D5BFA6B6617724AA99FEFCC8` |
| `vellexia.coin_given` | `World/Dialogs/c4/RaptureOfRupture/Velexia_First_Date/Cue_0089.jbp`, BlueprintCue `ff7f743740d221b46860f3137299c3d2` | `4611868D6C2CFE49AE4576E59EBDA2075989525F4923A3DCE02A91F8262AC688` |
| `vellexia.mirrored` | `World/Dialogs/c4/RaptureOfRupture/Velexia_Third_Date/Cue_0079.jbp`, BlueprintCue `42429350764f92140b293b24039b89ef` | `2574DB1F8603996D0765D08A12F34140700D240D2271F9854AB9A7A3E93EE221` |
| `vellexia.native_coercion` | `World/Dialogs/c4/RaptureOfRupture/Velexia_Third_Date/Answer_0078.jbp`, BlueprintAnswer `3aa48f68198afe14cb6de752ce80cc8f` | `C9EB53EA049B82B28B9B413C3DC0CC4640CD0A241853E52A7AF098F39B2815FD` |

All four GUIDs and blueprint types were rechecked directly against the installed archive at release.
The first-date gift is the teleportation arch's key coin, item `063e3d4f610e9a44fa15215151077f5c`.
Seeing its gift cue proves historical receipt only.
The Trickster option recalls that experience and requires the witnessed gift plus Trickster and the actually chosen Commander-order wager.
It never checks or claims current coin possession.
Its new magic is one voluntary replay of Vellexia's stored experience in a single breath; other people and the room's timeline do not repeat.
She forfeits the wager because this is a fourth offer outside its terms.
This is authored mythic fiction, not a verified native spell, an inventory mechanic or a universal recovery route.

Native ordinary leave answer `2ee010da8a71c5b4182c330f35eca3ea` reaches the consumed dismissal cue.
That cue starts peaceful-resolution etude `36544170c027e1142805f03235df29a4`, whose record has no restoration action.
The module deliberately consumes permanent seen-cue history and completed quest rather than assuming a Chapter 4 etude remains playing in Chapter 5.
The default and third-date actors are distinct, and later native farewell/spared conclusions can teleport the third-date actor away.
The original Default contact is therefore not asserted for post-quest physical meetings.
The native mirror and demonic domination conclusions remain incompatible with an unchanged voluntary correspondent.
No native flag or quest outcome is written by the module.

## Endings and limits

There are thirteen outcome pages: lovers, friends, slow, interrupted, closed, dead, mirror, coercion, hostility, changed, ascent, sacrifice and Aeon-rewritten history.
The first twelve use the ordinary epilogue owner and explicit precedence.
The rewritten history uses the separate Aeon epilogue owner.
The ordinary finished endings require their actual farewell outcome.
The interrupted and special endings can cover a played initial token/prediction history or a partially completed later campaign without pretending the final farewell occurred.
A slower history that chooses lovers at the farewell receives the stronger ending only after its new terms are accepted.
An earlier established commitment is not erased merely because the farewell was not played.
The observed mirror transformation takes precedence over generic death because native Cue0079 starts VellexiaKilled on stop.
That exact native combined mirrored-plus-dead history is exercised in the focused suite.
Generic death takes precedence over coercion, hostility and other special outcomes when no mirror cue was observed.
Native losses are not reversed by a happy ending.

Still required for the full project requirement:

- A concrete later physical invitation, attainable location and verified actor delivery, including safe return/removal and old-save behavior.
- A voluntary contact path for saves that missed either initial token conversation before the arena invitation.
- Separate recovery for death, mirror transformation and hostile/spared histories, preserving victims' outcomes and acknowledging what happened.
- An independently voluntary answer after any coercive history, rather than treating frightened surrender as permission.
- A bespoke attainable Trickster recovery/contact branch for those excluded histories, using actual quest connections and real delivery rather than clearing flags.
- An authored and verified treatment of relevant later native Demon arrangements if the route is expanded into those physical scenes.
- Scene art, portrait assignment review, live entry and save/load checks, TTS review and comparative RanRomance assessment.

Concrete research anchors for that next implementation are the arch/key gift and its first-date transition, third-date mirror/Finnean objections, explicit spared surrender and its teleport action, Default/ThirdDate spawn mechanics, and separate later Demon appearances.
Those records provide possible connections, not proof that an old actor can be restored simply by starting a flag.
A guest-contact proposal must supply its own voluntary motive after refusal or harm, then demonstrate actual living delivery and departure.
The present business plot supplies a credible new motive only for the ordinary peaceful dismissal with a previously accepted channel.
It does not reduce the requested universal Trickster scope to that subset.

## Measurements

Words are counted with `[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*` after removing brace markup.
Raw includes page prose and choice labels.
Exact-segment-distinct removes identical page or answer strings, including shared terminal variants.
It is a reproducible lower-level count, not a claim that all similar prose is semantically unique.
Titles, entry labels, native dialogue, debug text, replay and alternative epilogues are not included in selected-path measurements.

| Scope | Scenes | Pages | Prose words | Raw with choices | Exact-segment-distinct |
| --- | ---: | ---: | ---: | ---: | ---: |
| Original opening | 6 | 50 | 5,837 | 6,507 | 6,507 |
| New contribution | 24 | 113 | 16,979 | 18,470 | 18,017 |
| Combined, including alternatives/endings | 30 | 163 | 22,816 | 24,977 | 24,524 |
| Combined visits only | 17 | 150 | 21,637 | 23,785 | 23,344 |

A complete selected seventeen-visit route reads 12,283-13,573 words without the gift-gated Trickster experiment, or up to 13,801 with it.
The selected new contribution reads 8,627-9,840 words ordinarily, or up to 10,068 with that experiment.
These are terminal paths with actual choice conditions, including World success/failure/non-roll and earlier Arcana branches.
Refused/closed routes and epilogue text are excluded from those full-route ranges.
The 21k aggregate planning floor is exceeded, even with endings removed.
There is no invented requirement that one selected path must itself contain 21k words.
Quality, full access, comparative amount and campaign completeness still require independent assessment.

## Verification

Python compilation passed.
The isolated actual assembly passed `Rules.Validate` and **237,254 assertions** in `VellexiaCampaignTests`.
The suite plays the existing six-scene opening and every new authored predecessor rather than seeding their milestone flags.
Only native quest progression, observed gift/dismissal and changed native ending states are explicit fixtures.
It checks every new page, all mutually exclusive decisions, native/history immutability, unrelated romance preservation, interrupted/deferred progress, replay prevention, local actor loss, remote entry blockers, area constraints and actual final/partial/special endings.
Redundant played witnesses are grouped only by flags read by later scenes, retaining actual complete snapshots rather than fabricating combinations.
The suite does not pretend that fixture native transitions are a live Unity campaign test.

Command:

```powershell
& C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe run --project C:/Users/Z/AppData/Local/Temp/vellexia-campaign-pgk6ak3s/Check.csproj -- C:/Users/Z/AppData/Local/Temp/vellexia-campaign-pgk6ak3s/candidate.json
```

Reproducible count/candidate script: `C:/Users/Z/AppData/Local/Temp/vellexia-campaign-pgk6ak3s/measure.py`.
Measurement output: `C:/Users/Z/AppData/Local/Temp/vellexia-campaign-pgk6ak3s/counts.json`.

Known shared-engine defect, reported to root separately: `Rules.ContactAvailable` returns true immediately for a scene with null ContactUnit.
Thus a remote call already open when a native death/mirror/coercion state changes is not rejected by that continuation check, although `Rules.Available` correctly blocks a new entry.
The isolated suite asserts native entry guards on every page and the actual native contact guard for local scenes.
It does not claim the unresolved remote continuation behavior passes.
Root owns its separate reproduction and repair, including recovery/memory/epilogue compatibility.
No shared engine change is included here.

## Review status

Root's preliminary complete read of the first ten visits identified Tessar's missing successful-check introduction, implicit kiss assent, a missing circlet, publication privacy and inconsistent memory-loop description.
Those are repaired in the frozen source.
The coin is correctly called the arch's key gift rather than an ordinary coin.
A final author continuity read also removed duplicate case-closing actions and an unsupported shared paper movement after the case had closed.
Root also read the farewell and endings and requested the native mirror/death arbitration repair and an explicit shell movement before the vase returns into view.
Both are repaired in the released source.
The final independent review verdict remains with root, rather than the author.
No scores or acceptance are supplied by the author.

# Targona extension source evidence

Author's local-source investigation on 2026-09-25, not an independent review or score.
The installed `blueprints.zip`, `Wrath_Data/StreamingAssets/Localization/enGB.json`, RanRomance `readme.txt`, `LocalizedStrings.json`, and installed `RanRomance.dll` were read directly.
The parent assembly was inspected with the installed ilspycmd, using individual types and stdout rather than modifying the assembly or exporting source into shared directories.
The installed assembly SHA256 is `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
Exact parent blueprint creation excerpts and types are recorded in `targona-parent-bindings.json`.
Those records are source evidence, not fake native archive records and not proof that the real parent initializer ran in Unity.

## Existing coverage comes first

The roster's installed-source inventory identifies Targona as RanRomance's largest configured route: 19,004 keyed words, or 18,359 after exact normalized-segment deduplication.
These are aggregate configured words, not a selected playthrough length.
RanRomance already includes initial wing treatment, small and large mythic-power choices, a later check-up/date, chapter-four intervention, a chapter-five finale, friendship and romance decisions, transformations, and epilogues.
The new module must extend those decisions rather than replace the initial rescue, first flirt, first kiss, wing-healing sequence, or existing romance.

The installed readme says treatment begins through Targona or the Hand of the Inheritor in chapter three, followed by a check-up after a week and the Ivory Sanctum.
It describes later events and a chapter-five finale obtained through Anevia or the Storyteller after mythic progression and Iz.
These trigger claims were checked against the decompiled `TargChpt03Dial002`, `TargChpt03Dial003`, `TargBook02`, `TargBook04`, and `TargQuest` types, rather than treating documentation as the only integration evidence.
The extension does not bypass these existing requirements or provide a new initial romance for saves that never played them.

`RanRomance.Targ.Main.Configure` creates distinct parent etudes for small-power, Angel, Azata, Aeon, Trickster, Demon, Lich, Devil, Legend, and Dragon histories, plus romance and late-change states.
The Angel and Azata histories can retain angelic identity; small-power healing remains gradual.
Aeon and Trickster history includes Anograt, initially expressed through Targona's shadow and later able to separate temporarily.
Demon, Lich, Devil, mortal Legend, and Dragon outcomes differ materially and must not be overwritten with generic angel prose.

The installed `TargBook04Page101` establishes that Anograt's separation has both time and distance limits.
Its localization presents her as expressing her own wishes, teasing Targona, and sharing existing romantic scenes when that parent romance is active.
`TargBook04EndCue0006` already contains a shared intimate ending for the Commander, Targona, and Anograt.
The extension does not introduce this as a newly earned triad or count Anograt as a newly added roster character.
It preserves her differing opinion and limited separation without inventing independent travel beyond those limits.

RanRomance also introduces the elderly adult veteran Ruth Folress and the old Order of the Wings.
It already uses the Half Measure, the Targona Special, sweet food, renewed acquaintance after seventy years, and later future plans extensively.
Those established scenes are not reauthored here.
No historical child in those memories is a romance participant.

## Native adult identity and history

`Units/NPC/Unique/Act_3_DemonsHerecy/AreeluLab/AngelTargona.jbp`, GUID `81297c673b63b60448ef88a10db6bc78`, specifies female gender and lawful-good alignment.
Native portrayal is of an adult celestial warrior with an established service history and an adult brother, Lariel; no exact age is invented.
Its native portrait reference is `4f581ecf63d847fea78cc6263a24b5f0`.
RanRomance replaces her portrait and supplies separate mixed, angel, one-wing, and transformed art, so the extension must not blindly install one generic portrait across all outcomes.

Native `TargonaPrison/Cue_0001`, `733a9c94c2f9ea14f9e2734b0f180e40`, describes silvery hair, a white wing, and the altered dark counterpart during captivity.
`Cue_0029`, `951ee95404ffd0e458182ce99051acff`, establishes that the captive angel's presence protected nearby prisoners while she was immobilized.
`Cue_0036`, `3618aafa2f0690d45af47cc4ef49103e`, describes the surviving prisoners and the dangers following Areelu's departure.
These passages do not establish that every prisoner was rescued alive or is available for a later meeting.
The extension therefore does not summon those survivors or assign them invented current fates.

Native `World/Dialogs/c3/Mythic_Angel/Targona/Cue_0006`, `864b462a9f05bd449b86bd0dc3787113`, combines joy at freedom with distress about what occurred during her absence.
`Cue_0007`, `e788c73326878a64cbf8a87f4fb5759d`, says she can contact celestial brethren on Golarion.
This is not proof of an unrestricted telepathic link with any Commander, so the extension uses ordinary authored correspondence.
`Cue_0012`, `0a5654314707d084e83955978852ce29`, states that her altered wing has become part of her and that she knows no simple cure.
`Cue_0021`, `2ab07f9316f235642840a95c5d96c441`, distinguishes spiritual corruption from mere appearance and insists upon her own choice about Heaven.
The new writing does not turn her concern into embarrassment about being unattractive, or cure it with affection.
`Cue_0014`, `a528614125b07714db52d9004f36d448`, connects her protective presence to the living-Wardstone discussion.
Her captivity being useful to others does not mean she consented to captivity; the authored account dispute develops that distinction.

## Native state and contact facts

| Native object | GUID | Use |
| --- | --- | --- |
| TargonaIsFreeInAreeluLab | `720af1f72f413354db3f4d41f76d5af6` | Existing freedom history required. |
| TargonaIsWasKilledInAreeluLab | `3b8bd37108050a94b9be14e22501e090` | Excluded history; see parent reuse caveat below. |
| TargonaDiedInMutasafenLair | `bc65b234df544a718afc4856eb7f33fc` | Excluded death history. |
| TargonaCondemnedAreeluLab | `1aaee57d670b0494e9d8662bffbf4f6a` | Excluded one-wing/condemned branch matching this parent continuation's limits. |
| TargonaGoodWings | `cbbc0bda343244f9ac373df52f9e60dc` | Native restoration exists, but is neither awarded nor inferred by the new module. |

All are native BlueprintEtudes under `ImportantNPCs_fate/Targona/`.
The parent explicitly completes its active route and romance etudes when the Mutasafen death etude starts.
The parent also starts the lab-killed etude during its Legend transformation logic.
That alias is therefore not universal proof of literal death in every parent route; the current extension separately excludes mortal Legend content rather than interpreting that transformed character as a dead angel.

The default capital actor etude `6251641e86179d146a5942bbb6951719` hides Targona's spawner.
`TargonaInDrezenNearFane`, `4c6d98e2205a9614d9b2d4b4c20ff445`, explicitly requires the Angel path in its activation conditions and unhides spawner `2a27abe5-0d42-4a94-b564-7a406f406d44` in scene `3e2b5ea054cd5b2479e7f13134363ef4`.
`Targona_Drezen_DialogOverride`, `acbf141266ea45df95b63722db4f683d`, belongs under PlayerIsAngel and requires the relevant capital presence.
This investigation does not establish universal chapter-five physical presence for Trickster, and the extension does not assume it.
A future physical route must separately verify its actual actor and availability without unhiding a default actor or inventing a return.

## Exact parent handoff

`RanRomTargQuest` is BlueprintQuest `6ec03ce2f763460c8ac89f4c2064c5ad`.
Its final objective `227778a66d0f478fbb6e1b7e89758d22` has `SetFinishParent()` in `TargQuest.Configure`.
`TargBook04`, BlueprintDialog `ddcf04165a604410888aac8e752b1f92`, completes that objective in FinishActions.
To avoid treating a merely started or interrupted finale as a played endpoint, the extension also requires one of four actual end cues.

| Parent end cue | GUID | Meaning |
| --- | --- | --- |
| Book04EndCue0002 | `ad655c40be31401386b85287483b3841` | Good/appropriate nonromantic farewell. |
| Book04EndCue0003 | `cfc5f3cb2cf94672a96cab742e62225d` | Aeon/Trickster nonromantic farewell with Anograt present. |
| Book04EndCue0006 | `62c24328ae744ee98fabd219dbe74c92` | Existing Aeon/Trickster romantic ending. |
| Book04EndCue0007 | `ec76729da60441a1b2028f340743c0a8` | Other parent romantic ending; current history restrictions still apply. |

All four are BlueprintCue objects created in `TargBook04End.Configure`.
An end cue being seen is a memory of that page, not a substitute for the required quest-completion condition.
`RanRomTargRomance`, `80cb9c6f466b4eaaaa9561ca56c5f348`, remains the authority for whether the existing romance is active.
The extension only reads it and never starts, completes, or replaces it.
It also leaves the parent romance counter, wedding marker, breakup logic, and epilogues untouched.

The new contribution uses current Trickster status for its optional paper trick, and actual parent Aeon/Trickster treatment history for Anograt's presence in the letters.
These are different facts and are not conflated.
The already implemented parent large-power Trickster route supplies the attainable transformation connection; no fake Angel quest completion is needed.
The new impossible paper is an authored, narrowly bounded mythic incident, not an engine resurrection, native healing, permanent inventory item, or alteration to the laboratory.
The unaltered original is retained, the trick is optional, and the letters do not claim it cures recurring distress.

## Remaining coverage

The correspondence currently supports angelic small-power, Angel, Azata, Aeon, and Trickster parent histories.
Current Demon, Lich, Devil, and Swarm exclusions preserve the conflict with this angelic voice and the parent's transformed/hostile outcomes.
Legend and Gold Dragon are excluded from this contribution because their body and future differ, not because those paths are morally disqualified from the roster.
Their appropriate continuations, late-start routes, missed-treatment saves, one-wing alternatives, death recovery, and broader path transitions remain work to implement.
This bounded extension does not satisfy every-entry Trickster restoration, all-character route completion, art review, or actual runtime delivery verification.

# Tirabade settled-art reassessment

Reviewed 2026-09-27 against the current `art/CHARACTER-DESIGN.md` and `settled-image-reassessment-checklist.md`.
This is a new independent visual assessment of images this reviewer did not author.
Prior scores have not been inherited.
Only this report was edited.

## Decision

The two individual portrait sets clear the static visual-design threshold, with the limits below.
Together clears the static illustration threshold for a suitable shared supper, but its current automatic assignments fail scene continuity.
None of these findings approves all current page assignments or in-game display.
No blanket wardrobe or bust revision is indicated by these native references.
Both native characters wear practical covered clothing, and Irabeth wears a substantial breastplate.
Native anatomy concealed by clothing or armor remains unknown.

## Evidence and provenance

I directly viewed both extracted native full portraits, both delivered NPC full portraits, each of the four delivered Medium/Small crops, and the staged Together image.
The staged individual images are byte-identical to the inspected Medium files, as independently verified by SHA256.
I read the extraction provenance and verified the extracted full-image hashes on disk.
The provenance links Anevia to `Units/NPC/Unique/Act_3_DemonsHerecy/Drezen/AneviaTirabade_DrezenCapital.jbp`, unit `b5e867e13503c6f41bb1316705efb4a2`, and portrait `2d13cca308ac61342af690dcdb809b5d`.
It links Irabeth to `Units/NPC/Unique/Act_3_DemonsHerecy/Drezen/IrabethTirabade_DrezenCapital.jbp`, unit `280d4712dceb37f4a88e98f1f4c6e64f`, and portrait `14ca57e7f693ba9469d7c1111f79e56e`.
The provenance records extraction from the native portraits bundle with UnityPy, not a rendered 3D prefab comparison.
I did not independently repeat bundle extraction or claim that these portraits prove every in-game model detail.
The provenance file hash is `2572AD04EB2D82D59AC8E65739258F6EB27FC9D0D78822EA3D361A8B8699D5EB`.

Paths below are relative to the repository root.
The common NPC prefix is `art/CustomNpcPortraits/Portraits - Npc/` and the scene prefix is `art/CustomNpcPortraits/RanRomance-Tirabade/Scenes/`.

| File | Dimensions | SHA256 |
| --- | --- | --- |
| NPC Anevia/Fulllength.png | 692 x 1024 | `FC688DC8891BD23034373A741E6A1112B4C99FAF3B394B1872C180DD496B38A7` |
| NPC Anevia/Medium.png; scene Anevia.png | 330 x 432 | `C964F8C95CFD8E426F2F493463CABAD1A230BDEFF544EB11A4B528CD35B2DDF8` |
| NPC Anevia/Small.png | 185 x 242 | `79921EB4463FDA649DFE0C35AE2C8F4A8C8E5CB57766FC3156E5CBAD1ED1E5F8` |
| NPC Irabeth/Fulllength.png | 692 x 1024 | `1B0F5E45CB237D4E754B6862EAD610E7EB94BBA13EB02CB8562A06DBAD01ADF7` |
| NPC Irabeth/Medium.png; scene Irabeth.png | 330 x 432 | `7319099690CE2755A108F2B7A0F7FB767BEC1018E1CDDECA78B3ED66EE12B83D` |
| NPC Irabeth/Small.png | 185 x 242 | `22571C62611A8286820AC54555741AA0C5569AAAE7D64100D1B124E1C7537A06` |
| Scene Together.png; art/originals/Together.png | 1536 x 1024 | `D125515DA14EA5333DFB8E800F766F5ABC0C3B2820C78BF506E880271457EBBF` |
| reference/art-review/roster-native/AneviaCapital-m_FullLengthImage.png | 692 x 1024 | `E66A1A63570F17E8F8EC76BC69DD3341D49EAB2B60BC9E591A4D1FC570D00A4D` |
| reference/art-review/roster-native/IrabethCapital-m_FullLengthImage.png | 692 x 1024 | `7BE3F30FB47C4D99D032E931968C3F20554E339CD6349D4C0873272FF3E8C240` |

## Individual designs

Anevia remains immediately recognizable through her dark asymmetric short hair, direct sidelong expression, blue and muted-gold checked scarf, cream sleeves, brown leather armor, crossed gloved arms, bow, quiver and hip-mounted sword.
The redesign makes her mouth slightly warmer and her cheek transitions softer while preserving an adult, alert face rather than a generic youthful doll.
Her stance, trouser coverage and laced boots follow the full native portrait closely.
The added shoulder ornament and changes to belt fittings are small authored costume variations, not exact copies.
The leather chest becomes a little more rounded and fitted; the native arms and scarf partly obscure this area, so precise underlying bust-volume equivalence cannot be measured.
There is no visible flattening, raised neckline or additional prudish coverage.
The crossed hands are partly hidden by design, but their visible connections are coherent.

Irabeth retains olive-green skin, pointed ears, two lower tusks, dark blue-black swept hair, strong brow, a broad armored silhouette, gold plate, dark underlayers, sword and crossbow.
The softened cheeks and fuller mouth meet the requested attractive humanization without removing half-orc identity.
Her expression remains watchful and serious.
The gold armor retains its central diagonal strap, sun-and-sword-like emblems and layered shoulder plates, though engraved detail and fastenings differ.
The delivered figure reads slightly more tapered through the waist, but remains solidly built and armored.
The native breastplate supplies evidence about armor curvature only; it cannot justify a demand to enlarge or shrink her breasts.
Face and ears are exposed in both versions, while neck, chest, arms and legs remain covered.
The visible sword hand, supporting stance and boots have no clear anatomical break at the supplied resolution.

The Medium crops preserve identity and useful upper-body costume evidence.
The Small crops remain legible, although the faces occupy relatively little of their frames, especially Irabeth's.
The small images are 185 x 242 and the medium images 330 x 432, whereas the extracted native small and half portraits are recorded as 184 x 244 and 332 x 432.
Those differences do not establish a visible defect by themselves, but actual loader sizing and UI clipping still require verification.

## Together

The shared image depicts two clearly adult women seated close together at a candlelit table, with a rainy blue window behind Irabeth.
The two individual faces, hair directions, skin colors, tusks, scarf and gold armor remain consistent enough to read as the same redesigns.
Irabeth is somewhat softer and more smiling here; the change is plausible for an affectionate private moment.
Her tusks remain visible and the image does not turn her into a green-skinned generic human.
Anevia's bare hand rests over Irabeth's bare hand while the leather bracer and armored forearm remain visible.
Removing gloves at a table is a credible scene-specific costume change, but is not proof that every assigned page takes place there.
The overlapping fingers conceal some anatomy; what is visible forms a plausible contact rather than an obvious duplicated or broken hand.
The table, candles, chairs and three cups make a coherent shared encounter with an unseen third participant.
The native outfits' covered silhouettes remain intact, with no invented cleavage or added neckline coverage.
Only their seated upper bodies are shown, so lower-body fidelity is not applicable to this image.

## Independent scores

Scores are editorial judgments about the inspected pixels, not statistical measurements or inherited approvals.
Every applicable dimension must exceed 90 independently.
The table separates static-image suitability from the actual assignment failure.
Body scores concern visible clothed or armored outlines only.

| Dimension | Anevia set | Irabeth set | Together |
| --- | ---: | ---: | ---: |
| Adult conventional facial appeal | 95 | 94 | 95 |
| Character identity and distinctive racial/facial cues | 95 | 95 | 94 |
| Hair, palette and character-specific expression | 95 | 95 | 94 |
| Native clothing and equipment fidelity within visible frame | 93 | 94 | 93 |
| Native exposed-skin pattern, with plausible table glove removal | 97 | 97 | 95 |
| Visible body/armor silhouette | 93 | 93 | 93 |
| Visible anatomy | 94 | 94 | 92 |
| Painterly finish and game-art consistency | 94 | 94 | 94 |
| Full-image composition | 95 | 94 | 95 |
| Medium crop readability and framing | 94 | 94 | N/A |
| Small crop readability and framing | 92 | 91 | N/A |
| Consistency between individual and shared designs | 94 | 94 | 94 |
| Suitability as a neutral speaker portrait | 93 | 93 | N/A |
| Current general scene-illustration assignments | Not certified | Not certified | 35 - fail |
| Actual Unity display, crop scaling and branch timing | Unverified | Unverified | Unverified |

No score is assigned to hidden anatomy, Together's unseen lower bodies or unexecuted runtime behavior.
Individual portrait suitability does not assert that a wall background or full armor matches every narrative setting.

## Assignment reproduction and required corrections

I read the current exported `development/Story.json`, SHA256 `38F3442E5B33C1C6E9DE548E46C77B6C033783FB68E96FA3D0631EA3D0D44255`, and reproduced the portrait-key expression from `src/Main.cs:968` in a read-only Python traversal.
The inspected Main.cs hash is `6313F97C7856932AB9055E773065FA5926E27DBEB7A6EA05CDE5E170E46245E4`.
An explicit page Portrait wins; otherwise a Narrator page receives Together and other speakers receive their own names.
At this snapshot Anevia resolves on 322 pages in 73 scenes, Irabeth on 374 pages in 63 scenes, and Together on 384 pages in 139 scenes.
These counts record exported assignment, not executed availability or successful display.

- `reckoning/start` resolves to Together while saying that Irabeth has brought no armor and that both women sit facing the Commander.
  Together visibly puts her in plate armor beside her wife in an affectionate pose, so wardrobe and emotional staging conflict.
- `three_yard/rules` resolves to Together during the outdoor wooden-ball game by the lane, counter and fence.
  An indoor candlelit supper does not illustrate this action or location.
- `konomi.return_letter/start` also resolves to Together while the Commander writes Lady Konomi's name on a fresh sheet beside a folded map.
  Neither pictured woman is established as a participant by that page.
- The same default also reaches memory and epilogue pages, which cannot automatically inherit a literal rainy supper setting.

Replace inappropriate page assignments using the existing Portrait field and suitable reviewed art or a verified neutral presentation.
Restrict Together to pages where both women, armor, table, affectionate posture and interior fit the prose.
Do not solve the no-armor page by silently changing its narrative intent to suit the current image.
Audit all 384 Together uses rather than fixing only these examples.
Review individual portraits as speaker portraits separately from any claim that they illustrate a scene's precise setting or wardrobe.
Use automatic per-page switching already present; this evidence supplies no reason to build a clickable selector.

## Verification limits

SHA256 and PNG dimensions were obtained locally using Python's standard library and PowerShell.
An initial optional PIL metadata attempt failed because Pillow is absent in the system Python; the standard-library PNG header read then completed successfully.
Visual inspection used the actual files through the image viewer, not metadata or a report's description.
No game was launched, no image was regenerated, no source assignment was changed and no runtime gate was approved.
The remaining work is assignment repair, review of any needed costume/setting alternatives, and actual UI/branch display verification.

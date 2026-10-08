# Complete CustomNpcPortraits visual audit

Date: 2026-09-27.
This report inventories and visually examines every distinct installed image content, including all alternate forms, retained versions, Medium/Small crops, placeholders and installed scene art.
All 238 installed files are covered by direct viewing of their 191 distinct SHA256 byte groups.
Identical-byte copies were deduplicated, not counted as new artwork.
All 27 local replacement files are also covered, including 18 distinct images absent from the installed pack.
This is complete visual triage at tool-rendered resolution, not exhaustive pixel-level anatomy inspection or native-game certification.
No image is approved for assignment or runtime by this report.

## Roots and counts

Installed root: `D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/Mods/CustomNpcPortraits`.
Local replacement root: `art/CustomNpcPortraits`.
Installed image count: 238 files across 80 image-bearing directories, with 191 distinct SHA256 byte hashes.
There are 30 top-level companion/form folders under `Portraits` and 24 under `Portraits - Npc`.
These are folder counts, not 54 distinct characters.
Companion branch contains 149 images; NPC branch contains 84; placeholder contains two; installed Tirabade Scenes contains three.
Local replacement collection contains 27 PNGs: six crop files for Anevia/Irabeth and 21 scene illustrations.
Full, Medium and Small are display/crop assets, not three distinct narrative artworks.
Byte hashes distinguish literal duplicate files only; different crops of the same art still have different hashes.

## Direct visual findings

The initial pass opened 24 installed full files, two local full files and six reference images.
The completion pass viewed every remaining distinct installed byte group and 18 additional local images with view_image.
Two more native reference images were viewed for the Arsinoe correction and Terendelev comparison.
The installed Galfrey living image was opened in both branches, so 24 inspected files do not represent 24 unique designs.
Scores are withheld because this is comparative triage, not the required complete per-image acceptance rubric.

| Character | Viewed path shorthand | Finding |
| --- | --- | --- |
| Aranka | `NPC/Aranka/Fulllength.png` | Attractive smiling blonde performer in emerald off-shoulder slit gown, barefoot, holding elaborate lute-like instrument. Strong performance concept; string/peg construction and playing grip need close review. Ornate salon is specific, not a universal travelling scene. Native reference not freshly available; costume fidelity unverified. |
| Areelu | `NPC/Areelu Vorlesh/Fulllength.png` | Recognizable red robe, horns, black hair, tattoos, wings, magical violet setting. Direct official comparison shows the native simple drape and practical belt/vials replaced by elaborate silver corset decoration, much thinner silhouette and different forehead jewel. Attractive but costume/proportion fidelity needs correction, not extra coverage. |
| Arsinoe | `NPC/Arsinoe/Fulllength.png` | Corrected after provenance recheck: installed gold hair and glowing eyes agree with the actual unit-linked gold-haired aasimar thumbnail. The generic dark-haired BCT_Arsinoe.png is NOT the linked texture; the initial discrepancy claim is retracted. Installed loose long hair, jeweled circlet, ornate gold armor and outdoor setting still differ from the linked swept-back hair, arched diadem and ivory/slate clerical collar. Native thumbnail cannot validate the full armored outfit. |
| Iomedae | `NPC/Iomedae/Fulllength.png` | Attractive stern dark-haired armored woman with red cloak, sword and large sun shield. Strong martial silhouette; equipment dominates and offers no private-scene variation. Native portrait comparison remains outstanding, so emblem and precise costume claims are unverified. |
| Jerribeth | `NPC/Jerribeth/Fulllength.png` | Insect face, long proboscis, pale compound eyes, spiked crest, membranous wings and grey layered body. These agree with the linked native oolioddroo cues, but fail the requested attractive humanoid facial redesign. Preserve meaningful insect identity while redesigning the face; do not replace her with generic succubus horns. |
| Minagho | `NPC/Minagho/Fulllength.png` | Eyeless face, swept horns, pale hair, red/gold open costume and long nails are recognizably close to native. Installed smooth unmarked forehead omits native damaged/brand texture, and the nose is reconstructed. This needs explicit history/form labeling rather than universal replacement. Snow background and cropped upper horn tips limit scene fit. |
| Nocticula | `NPC/Nocticula/Fulllength.png` | Native-like pale eyes, black hair, enormous horns, tattoos, revealing ornamented costume and seated crossed-leg throne pose retained. Fuller throne composition preserves sensuality. Face is softer and less commanding than native; fingers, jewelry contact and dark wing edges need closer pixel review. Throne scene cannot stand for standing harbor action or private couch. No need to cover more skin. |
| Nurah | `NPC/Nurah/Fulllength.png` | Braid, blue headband, teal/purple travel clothes and luggage retain native motifs. Installed enlarged eyes, small rounded face and subdued mouth read much younger than the native shrewd smiling adult. Adult-age-read hold for romance illustration; repair expression and mature facial structure without making her tall or wrinkled. Boots/shorts and seated crate replace native barefoot rock stance. |
| Galfrey | `NPC/Queen Galfrey and companion Queen Galfrey, plus undead/Fulllength.png` | Living image is appealing and stately, blonde braids, blue eyes, crown, silver armor, folded hands and royal banner. It needs expression/pose variety for intimacy or campaign fatigue. The undead alternate is visibly skeletal and deeply lined, not an attractive restored-state portrait; retain it only for actual undead state. All age/disguise alternates and crops inspected in completion pass; see findings below. Native comparison pending. |
| Terendelev | `NPC/Terendelev/Fulllength.png` | Attractive silver-haired adult humanoid with gold-black fitted armor and deep neckline. Small decorative head spikes do not establish native dragon anatomy. The subsequently viewed native human thumbnail has a silver bob, tall silver diadem and mail neck. Installed long waves and gold side ornaments are departures, while exact bust/full armor cannot be checked from that crop. This pack interpretation cannot establish earned resurrection or replace dragon-form pages. Straight mannequin pose needs event alternatives. |
| Anevia | `NPC/Anevia and local same-name full/Fulllength.png` | Short dark hair, knowing smile, cross-armed wall lean, scarf, bow and practical leathers form a distinct adult rogue. Battle/travel outfit is appropriate for that portrait but not every private scene. Fresh native comparison pending. Local full directly viewed too; byte comparison below establishes whether copies match. |
| Irabeth | `NPC/Irabeth and local same-name full/Fulllength.png` | Strong green half-orc, visible tusks, cropped dark hair and substantial gold plate preserve racial and martial identity. Attractive does not require removing tusks or reducing strength. Encampment and sword-bearing pose are specific; armor conflicts with any explicitly unarmored private scene. Fresh native comparison pending. |
| Arueshalae | `companion Arueshalae and Arueshalae - Evil/Fulllength.png` | Blue hair, horns, wings and tail preserved in both. First is high-neck blue armor with alert reserve; evil alternate uses red eyes, knowing smile, open arms and exposed corset/thighs. Useful actual pose variation, but modest versus revealing presentation must follow native costume and exact state rather than moral shorthand. Neither is approved as dream/private art; native comparison pending. |
| Camellia | `companion Camellia/Fulllength.png` | Pale blue-eyed half-elf, dark hair, teal/brown outfit, rapier, necklace gesture and aristocratic interior recognizable as a coherent concept. Face remains alert rather than harmless grin. Hand-to-jewel contact and weapon grip deserve close inspection. Native jewelry/costume comparison outstanding; no universal evil-state assignment. |
| Delamere | `companion Delamere/Fulllength.png` | Green luminous eyes, hood, elaborate bow, bony hands and feet explicitly depict undeath. Humanized attractive face with skeletal extremities requires intentional state continuity. Cannot imply autonomous living restoration or voluntary romance merely by being appealing. Native comparison outstanding. |
| Nenio | `companion Nenio and NenioFox_Portrait/Fulllength.png` | Human and fox use matching scholar clothes, packs, pondering chin pose and raised knee. Fox is fully muzzled/furred rather than requested humanized adult face. Retain form evidence and design a separate labeled humanoid interpretation without erasing fox traits. Both preserve curiosity, but identical pose is a form swap rather than event variety. The native-labeled backup files are byte-identical to the active fox files; the folder label itself does not prove official provenance. |
| Seelah | `companion Seelah/Fulllength.png` | Dark skin, braided hair, substantial full armor and large weapon, upright alert stance. Good strong adult identity; soft expression need not become coy. Equipment is very ornate and requires native comparison. Off-duty warmth needs a genuinely different garment and pose, not armor recoloring. |
| Wenduag | `companion Wenduag/Fulllength.png` | Blue skin, golden eyes, tail and long angular spider limbs preserved in a low hunting crouch. Hood conceals some head identity; shadow suppresses limb attachment clarity. Attractive humanoid face remains recognizable as nonhuman. Need close extra-limb anatomy check and native costume comparison before new variants; no gratuitous smoothing of racial traits. |
| Ember | `companion Ember/Fulllength.png` | Age-appropriate ragged dress, scarred skin, pointed ears, crow and ruined landscape. Solely friendship review. Do not erase scars or turn this vulnerable appearance into adult-romance art. Native exact burn distribution and crow/staff grip remain unverified. |
| Aivu | `companion Aivu/Fulllength.png` | Purple scaled dragon with blue eyes, pale green wing membranes and friendly expression. Solely friendship review. No humanoid redesign or adult-romance treatment. Actual encounter size and wing/leg anatomy require scene-specific review; native comparison outstanding. |

`NPC` means installed `Portraits - Npc`; companion names mean installed `Portraits/CustomNpcPortraits - NAME`.
For multiple forms in a row, each named directory was opened separately.

## Native evidence actually viewed

- `reference/art-review/areelu-official/owlcat-full-portrait.jpg`.
- `reference/art-review/arsinoe-native/BCT_Arsinoe.png`, generic conflicting texture, not the actual linked portrait.
- `reference/art-review/arsinoe-native/32d1b598f0ac2a74f94d7d2fd7390e0f_BCT_Arsinoe.png`, verified linked texture.
- `reference/art-review/terendelev-native/TerendelevHuman-m_FullLengthImage.png`.
- `reference/art-review/jerribeth-native/Jerribeth-unit-linked-oolioddroo.png`.
- `reference/art-review/minagho-chivarro-native/minagho-native-half.png`.
- `reference/art-review/nocticula-native/NocticulaFemaleDemonlord.png`.
- `reference/art-review/nurah-native/NurahHalflingFemaleBard.png`.

Arsinoe and Jerribeth references are narrow linked portraits, not full-body model documentation.
No exact native 3D bust, limb or costume measurements are established.
Installed pack authorship must not be confused with Owlcat provenance merely because its layout resembles a native portrait.

## Roster coverage and absent characters

Representative installed portraits viewed for all 20 present roster members listed above.
No named installed character folder found for these 23 roster members: Konomi, Kiana, Vellexia, Gesmerha, Chivarro, Targona, Soana, Jannah Aldori, Yaniel, Elyanka Camilary, Herrax, Mielarah, Shamira, Hepzamirah, Eliandra, Devarra, Melazmera, Nidalynn, Eritrice, Chadali, Horzalah, Kaylessa, Dorgelinda Stranglehold.
Absence here does not mean no local candidate, staged scene illustration or native game portrait exists.

## Complete installed folder manifest

Every image-bearing folder is listed below, including outside-roster subjects and retained alternates.
All listed files are now visually covered through exact-byte groups; the file-level ledger below provides hashes.
The original folder manifest is retained for counts and dimensions.

| Relative directory | Files | Full image dimensions | Visual coverage |
| --- | --- | --- | --- |
| `Placeholder_Female_Portrait` | 2: Small.png, Small_.png | none | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Aivu` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Anevia` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Arueshalae` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Arueshalae/Old Version` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Arueshalae - Evil` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Arueshalae - Evil/Old Version` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Camellia` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Camellia/Old Version` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Ciar - Undead` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Daeran` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Daeran/Old Versions` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Daeran/Old Versions/Smaller Smile Variant` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Daeran/Serious Variant` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Delamere` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Ember/Black Eye Variant` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Ember` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Finnean the Talking Weapon` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Greybor` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Horgus Gwerm` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Hulrun` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Irabeth` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Lann` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Nenio` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - NenioFox_Portrait/Backup of Game Default Portraits` | 3: Fulllength.png, Medium.png, Small.png | 696 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - NenioFox_Portrait` | 3: Fulllength.png, Medium.png, Small.png | 696 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Queen Galfrey/Alt Version` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Queen Galfrey/Disguise Galfrey` | 2: Medium.png, Small.png | none | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Queen Galfrey/Elderly Galfrey` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Queen Galfrey` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Queen Galfrey/Previous Version` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Queen Galfrey - Undead` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Regill` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Seelah` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Sosiel` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Sosiel/old Version` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Staunton Vhane - Undead` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Storyteller` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Terendelev` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Trever` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Ulbrig/Backup of Game Default Portraits` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Ulbrig` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff14/Backup of Game Default Portraits` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1040 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff14` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1040 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff9/Backup of Game Default Portraits` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1040 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff9` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1040 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff_Cutscene/Backup of Game Default Portraits` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1040 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff_Cutscene` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1040 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Wenduag` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Woljif` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits/CustomNpcPortraits - Woljif - Demon` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Anevia` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Aranka` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Aranka/Old Version` | 3: Fulllength.png, Medium.png, Small.png | 696 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Areelu Vorlesh` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Arsinoe` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Baphomet` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Ciar` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Hand of the Inheritor` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Hilor` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Horgus Gwerm` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Hulrun` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Iomedae` | 3: Fulllength.png, Medium.png, Small.png | 696 x 1040 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Iomedae/Old Version` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Irabeth` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Jerribeth` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Minagho/Backup of Game Default Portraits` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Minagho` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Minagho/Minagho` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Nocticula` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Nurah` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Queen Galfrey` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Socothbenoth` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Staunton Vhane` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Storyteller` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Terendelev` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Wilcer Garms` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Xanthir Vang` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `Portraits - Npc/Zacharius` | 3: Fulllength.png, Medium.png, Small.png | 692 x 1024 | All files visually covered, direct or identical-byte copy |
| `RanRomance-Tirabade/Scenes` | 3: Anevia.png, Irabeth.png, Together.png | none | All files visually covered, direct or identical-byte copy |

## Local replacement manifest

| Relative local file | Installed same-path byte match |
| --- | --- |
| `Portraits - Npc/Anevia/Fulllength.png` | Identical |
| `Portraits - Npc/Anevia/Medium.png` | Identical |
| `Portraits - Npc/Anevia/Small.png` | Identical |
| `Portraits - Npc/Irabeth/Fulllength.png` | Identical |
| `Portraits - Npc/Irabeth/Medium.png` | Identical |
| `Portraits - Npc/Irabeth/Small.png` | Identical |
| `RanRomance-Tirabade/Scenes/Anevia.png` | Identical |
| `RanRomance-Tirabade/Scenes/ArsinoeShop.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/ChivarroWarm.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/GesmerhaWorkshop.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/Irabeth.png` | Identical |
| `RanRomance-Tirabade/Scenes/Jerribeth.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/Konomi.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/KonomiPrivateClose.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/KonomiPrivateDialogue.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/KonomiPrivateEvening.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/KonomiPrivateNear.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/KonomiPrivateSeated.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/Nocticula.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/SoanaForest.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/TargonaCorrespondence.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/Together.png` | Identical |
| `RanRomance-Tirabade/Scenes/TogetherReckoning.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/TogetherYard.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/VellexiaManorSpeaker.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/VellexiaPaintingChanged.png` | No installed same-path file |
| `RanRomance-Tirabade/Scenes/VellexiaPaintingDay.png` | No installed same-path file |

All local files are now covered by direct viewing or exact-byte equivalence to viewed installed files.
The 18 additional scene images were reopened for this audit; prior review scores are not inherited.

## Remaining pack scope and next pass

Named subjects outside the 43-character roster include Baphomet, Ciar, Daeran, Finnean, Greybor, Hand of the Inheritor, Hilor, Horgus Gwerm, Hulrun, Lann, Regill, Socothbenoth, Sosiel, Staunton Vhane, Storyteller, Trever, Ulbrig, Wilcer Garms, Woljif, Xanthir Vang and Zacharius.
Undead, demon and griffon subfolders are separate form/state assets, not new roster candidates.
All outside-roster full portraits and every alternate/crop have now been viewed.
No additional named female character outside the 43-character roster was found in these installed folders.
The two female placeholder images have no verified character identity.
Jerribeth and Nenio fox still need intentional humanization decisions; native racial identity should survive any redesign.
No changes to installed assets, portrait configuration, prose, engineering, source manuscripts or the shared art queue were made.

## Correction and provenance discipline

The initial Arsinoe finding was wrong because the audit selected a similarly named texture rather than following its unit link.
`arsinoe-native/provenance.json` maps unit `a609ed9b2205d034bb3bb04d2a255681` to portrait `e38efa21a3104c8db31f1a953d10f89f`, image container `b11644a73e0593849aa288de27ad0a14` and texture `32d1b598f0ac2a74f94d7d2fd7390e0f_BCT_Arsinoe`.
That image shows gold hair, gold eyes, arched gold diadem and clerical collar.
Its SHA256 is `56FFE2E7755BB599DE32BACB2C21EDC5BD4575998F1FEB6B346F3ED25B21F418`.
The generic dark-haired `BCT_Arsinoe.png` is a different texture and must not drive replacement of her aasimar identity.
This correction is applied to the table above; retain no work item claiming that blonde Arsinoe is inherently noncanon.

## Alternate and crop findings

| Files, relative to installed root | Concrete visual finding and action |
| --- | --- |
| `Portraits/CustomNpcPortraits - Arueshalae/Old Version/*` | Blue revealing outfit, hand-on-hip action and indoor circular window differ from active blue-armored moon pose. Full image has gibberish signature/logo at bottom left. Old Small loses horn tips and is softer than current Small. Retain as candidate only, not clean final art. |
| `Portraits/CustomNpcPortraits - Arueshalae - Evil/Old Version/*` | Jagged gray breast armor and expression differ from active purple corset. The old Small is blurry and loses horn tips. Active Medium cuts raised hands at frame sides, so use as portrait rather than complete gesture illustration. |
| `Portraits/CustomNpcPortraits - Camellia/Old Version/*` | Older face/hair are more photorealistic and rounder than active pointed-ear version. Both maintain necklace gesture, teal dress and rapier. Switching versions mid-scene would visibly change face and hair, not simply emotion. |
| `Portraits/CustomNpcPortraits - Ember/Black Eye Variant/*` | Eyes are blacked out across all sizes, with otherwise same burn/crow composition. This is an authored appearance variant requiring actual state justification; do not silently replace baseline friendship identity. |
| `Portraits/CustomNpcPortraits - Queen Galfrey/Alt Version/*` | Gold molded breastplate with white thigh-high hosiery and narrow hanging white front fabric has lingerie-like construction. Attractive face does not establish native royal or combat costume fidelity. Requires a deliberate authored private-costume context or redesign. |
| `Portraits/CustomNpcPortraits - Queen Galfrey/Previous Version/*` | Gold armor, longer loose curls and tall crown differ strongly from current silver plate and braided identity. Small clips crown spire. Do not mix as expression-only variant. |
| `Portraits/CustomNpcPortraits - Queen Galfrey/Disguise Galfrey/*` | Only Medium/Small exist. Helmet and yellow cloak portrait is clear, but face reads younger and rounder than current royal portrait. No full-length counterpart was found. |
| `Portraits/CustomNpcPortraits - Queen Galfrey/Elderly Galfrey/*` and `Queen Galfrey - Undead/*` | Distinct aged and skeletal states are visually clear. They cannot serve as attractive restored-state images; do not erase state history through blind replacement either. |
| `Portraits - Npc/Aranka/Old Version/*` | Blue/gold gown and reserved face under a large beam of light; no instrument and much less performer character than current smile/lute image. Full is heavily background-dominated. Small accentuates a youthful doll-like face. |
| `Portraits - Npc/Iomedae/Old Version/*` | Short-haired crowned fighter with bare thigh, white cape and different shield; full has faint gibberish at bottom left. Native costume evidence required before treating revealing old outfit as canon. Current image is a stronger severe adult design, though not independently native-certified here. |
| `Portraits - Npc/Minagho/Minagho/*` | Adds a small purple forehead sigil to otherwise matching smooth eyeless portrait. This resolves presence of a branded variant in the pack, not whether the symbol/placement matches each game state. |
| `Portraits - Npc/Minagho/Backup of Game Default Portraits/*` | Files are identical to unbranded replacement group, not independent proof of the actual game default. Never infer native provenance from a backup folder name. |
| Anevia and Irabeth `Small.png` in both branches | Small crops include most of torso, making face much smaller than neighboring tight face icons. Reframe if player UI comparison confirms poor legibility; do not change images blindly during this audit. |
| `Portraits/CustomNpcPortraits - Wenduag/Small.png` | Noticeably blocky/dark face crop compared with smooth neighboring portraits. Eyes remain legible, but skin/hood edges need higher-quality source/crop export. |
| `Portraits - Npc/Nocticula/Small.png` | Face is soft and horns largely cropped. Pale eyes remain readable, but demonic silhouette is reduced at icon size. Improve framing/sharpness without altering racial traits. |
| `Portraits - Npc/Nurah/Medium.png`, `Small.png` | Tight crops reinforce the very youthful, large-eyed age read. Adult characterization requires a mature-looking redesign before romantic scene use, independent of halfling size. |
| `Placeholder_Female_Portrait/Small.png`, `Small_.png` | Face is nearly black silhouette against light background; second is smaller/blurrier. This may be deliberate fallback, not usable identifiable character portrait. |
| Other reviewed Medium/Small files | Faces or intended objects remain recognizable at viewed size. No claim of pixel-perfect in-game scaling, no global crop approval. |

## Outside-roster full portraits

| Subject/form | Observation |
| --- | --- |
| Ciar living and undead | Living kneels in gold armor; undead stands in darker plate with skull-like face. Different action and costume, so an actual state change is needed. |
| Daeran current, serious, old and smaller-smile | All repeat wineglass/fountain pose. Useful expression variants, but current source is visibly soft; old set is warmer and more granular. Glass hand contact needs closer acceptance inspection. |
| Finnean | Weapon hilt with luminous eye motif remains clear in all crops; no human portrait assumption. |
| Greybor | Pipe, beard, fur collar and axes retain strong identity. More cartoon-like finish than photoreal pack neighbors. |
| Horgus | Heavyset noble, blue/yellow rich cloth and indoor stance. Preserve body individuality; no need to impose the adult-romance female redesign constraint here. |
| Hulrun | Severe gray-haired armored man with helmet under arm. Hands partly obscured by helmet, but no obvious cropped face defect. |
| Lann | Human/scaled split, horn and exposed chest retained. Good nonhuman identity distinction; Small clips horn extremity while face stays readable. |
| Regill | Stern lined gnome, swept pale-purple hair and black spikes. Full black-cloak mass is legible, though lower-body detail is subdued. |
| Sosiel current and old | Glaive and colorful clerical armor retained; face/hair visibly differ across revisions. Do not use as mere mood switches. |
| Staunton living and undead | Matching kneeling plate-and-snow composition with changed face state. Undead version clearly skeletal. |
| Storyteller | Tattooed white-haired elf examines a gem. Hands/prop are readable; native blindness portrayal requires source comparison rather than assuming the visible eyes are correct. |
| Trever | Angry scarred armored man with massive curved blade. Weapon dominates frame; face remains readable in crops. |
| Ulbrig human and griffon | Human red hair/tattoos/feather cloak and white-winged griffon are separate bodies. Multiple active/backup/size-form files are exact byte duplicates, not distinct progression illustrations. |
| Woljif and demon | Same over-shoulder pose, with red skin/fire/gold eyes in demon version. Useful state switch but not new event action. |
| Baphomet | Goat face, huge horns, wings, fire and staff are readable. Top tips fit full but crop out in icons; requires native model comparison for exact anatomy. |
| Hand of the Inheritor | Gold helmet, halo, wing and shield dominate. No exposed face expected; halo clipped in tighter crops is a composition choice to inspect in actual UI. |
| Hilor | Crossed arms in dim window alcove, weathered mature face. Dark trousers merge into background; not a clear action illustration. |
| Socothbenoth | Strong setting conflict: modern short-sleeve button-down shirt, belt-loop red trousers and contemporary upholstered couch styling. Replace wardrobe with believable setting construction if retained for game integration. Attractive face is not enough. |
| Wilcer | Friendly bearded quartermaster with barrels and camp tents; coherent role portrait. Keep away from unrelated intimate-scene assignment. |
| Xanthir | Hooded insect body, swarm masses and glowing eyes convey nonhuman identity. Fine swarm texture is noisy and some isolated insect edges look pasted; close native/texture inspection needed. |
| Zacharius | Skeletal green-lit face and ornate robe/staff in library. Tiny crop keeps skull but loses staff context, appropriately for icon use. |

## Local scene collection reinspection

All filenames below are under `art/CustomNpcPortraits/RanRomance-Tirabade/Scenes`.
These visual observations reopen the images without superseding exact page-level reviews or granting new assignment approval.

| Image | Current visual finding |
| --- | --- |
| Anevia.png, Irabeth.png | Byte-identical to installed full portraits; generic speaker identity, not universal private scene. |
| Together.png | Warm tavern/castle table and mutual hand contact; Irabeth remains armored. Incompatible with an explicitly unarmored scene unless treated as generic illustration. |
| ArsinoeShop.png | Gold hair/eyes, linked-style diadem and ivory/slate robes are closer to actual unit-linked reference than installed full gold armor. Ledger hand and shop context are clear. Not evidence of private undress. |
| ChivarroWarm.png | Attractive eyeless lilitu in copper draped gown, different from Minagho red outfit. Posed fabric-holding gesture and benign smile need more dangerous/event-specific alternatives. Tail/full lower anatomy not established by image. |
| GesmerhaWorkshop.png | Blind face, red markings and tactile carved bird preserve individuality. Finished bird is a specific prop, not compatible with every unshaped-block or proposed statue scene. |
| Jerribeth.png | Intentional attractive humanized face, crest/horn cues and insect wings. Elaborate layered dark outfit covers torso; native linked insect thumbnail alone does not prove a revealing humanoid costume should replace it. Add dangerous action rather than a generic succubus makeover. |
| Konomi.png | Office outfit, ears/tail and knowing tilt. Fits formal speaker identity, not private gown context. |
| KonomiPrivateEvening.png, KonomiPrivateSeated.png, KonomiPrivateClose.png | Gown and face remain coherent, but arrival/seated/close repeat head tilt and little smile. Earlier sequence-variety concern persists for Close; it is not fixed by zooming. |
| KonomiPrivateDialogue.png | Turned profile, speaking mouth and open hand create real action variety while preserving gown. Distinct from tilted close portrait. |
| KonomiPrivateNear.png | Forward chair motion and laughter are genuinely different; rug snag and hand on own chair convey a selected mid-page action. Does not depict actual kiss or whole later scene. |
| Nocticula.png | Armored black/gold breast cups and heavy bracers are substantially more clothed than native seated ornamented costume. Book/parapet/harbor composition is specific; this staged image remains a correction target despite attractive face. |
| SoanaForest.png | Attractive silver-haired dwarf with blue markings and substantial outdoors layers, basket/jar activity. Warm friendly gaze underplays eerie seer danger; add ritual/hostile expressions without returning to rejected craggy aging. |
| TargonaCorrespondence.png | White-haired woman folding paper house; narrow frame hides wings entirely. Useful correspondence illustration but cannot certify corrupted/healed wing continuity. |
| TogetherReckoning.png | Distinct serious disagreement, downward Anevia and stern Irabeth, civilian clothes. Useful emotional variety, not generic happy-triad art. |
| TogetherYard.png | Distinct playful shared skittles action and mutual glance in civilian setting. Still requires exact selected-page props and staging match. |
| VellexiaManorSpeaker.png | Attractive red-eyed horned blonde, composed expression and high collar. Fits speaker identity scope; does not show native full-body proportions. Needs more delight/menace variety for later scenes. |
| VellexiaPaintingDay.png, VellexiaPaintingChanged.png | Consistent magical painting with lightweight white garment; chipped versus whole brown cup and daylight versus dark sky are visible. Changed version is more impatient. Intentional near-identical composition supports this magical change, unlike repetitive unrelated event art. |

## Complete content-level viewing ledger

Every installed PNG is assigned to one SHA256 group below.
One representative per group was directly opened, while other listed paths are proven identical bytes.
The listed canonical representative need not be the path opened when an NPC/companion duplicate was encountered first.
Full/Medium/Small crops with different bytes were opened separately; they were not skipped as presumed duplicates.
The ledger is evidence of viewing, not a passing quality score.

| SHA256 | Canonical relative path and exact duplicates |
| --- | --- |
| `BA29DE9905B54BC2D2F513D3E8A0CD9143386E945F1C55D9C5DD40A6AF53E3AB` | `Placeholder_Female_Portrait/Small.png` |
| `054C88E6660ACD4A4C7BB7F6757FFBEF0699AF6304FE4E117E7B63D2B617347E` | `Placeholder_Female_Portrait/Small_.png` |
| `72CD763DBBC426E84F5E6B71FD433B5EFCBF078BE3B3F87999286B313DB1ECE0` | `Portraits/CustomNpcPortraits - Aivu/Fulllength.png` |
| `069C9DEE24BD9879D4F15F745D2C45164C020C899F8F95A38AF045E59E5CEA58` | `Portraits/CustomNpcPortraits - Aivu/Medium.png` |
| `B33CDE8EF77EE67D1A138DA9D11A05E09E3B29897AF5A0437CD81AF469312BEA` | `Portraits/CustomNpcPortraits - Aivu/Small.png` |
| `FC688DC8891BD23034373A741E6A1112B4C99FAF3B394B1872C180DD496B38A7` | `Portraits/CustomNpcPortraits - Anevia/Fulllength.png`<br>`Portraits - Npc/Anevia/Fulllength.png` |
| `C964F8C95CFD8E426F2F493463CABAD1A230BDEFF544EB11A4B528CD35B2DDF8` | `Portraits/CustomNpcPortraits - Anevia/Medium.png`<br>`Portraits - Npc/Anevia/Medium.png`<br>`RanRomance-Tirabade/Scenes/Anevia.png` |
| `79921EB4463FDA649DFE0C35AE2C8F4A8C8E5CB57766FC3156E5CBAD1ED1E5F8` | `Portraits/CustomNpcPortraits - Anevia/Small.png`<br>`Portraits - Npc/Anevia/Small.png` |
| `8AB9B610EBF3C68F1172A2F4FE115D897ECC8AB358E2CF4BA08E563A6897A60D` | `Portraits/CustomNpcPortraits - Arueshalae/Fulllength.png` |
| `1BCAC534EA9421944E63F7E51F5FA470A7A5BAC58FDD61ECD015EBA5FB3E0B1D` | `Portraits/CustomNpcPortraits - Arueshalae/Medium.png` |
| `F5277DF27B674FA304E3E3B99ECCCEC2C3C5EDD26C3AE996E4083561608B7DB5` | `Portraits/CustomNpcPortraits - Arueshalae/Old Version/Fulllength.png` |
| `3A4956461A514BDA206B131A0747C55E3D846989F381985B7DD8E0A990ACA2FB` | `Portraits/CustomNpcPortraits - Arueshalae/Old Version/Medium.png` |
| `7CDF04404CAA0B712A8C3FE1E8F481F865C01CF85ADA102E0708E950EAB876B9` | `Portraits/CustomNpcPortraits - Arueshalae/Old Version/Small.png` |
| `46C10FD1342C254D4C309FF0B1C262C523994D3EC399B9260D3C898349E98687` | `Portraits/CustomNpcPortraits - Arueshalae/Small.png` |
| `D3C157A9FAF57F231015D08FCA8C9171FD0B3430CD063EB60149DC87CBD70406` | `Portraits/CustomNpcPortraits - Arueshalae - Evil/Fulllength.png` |
| `F2F1983CB3C457DAD61D287FE4315D2B11BBB7A87E088480CAAFE9C7F3A0B5A7` | `Portraits/CustomNpcPortraits - Arueshalae - Evil/Medium.png` |
| `31DE2F66426A53D05AF9A983C0193782CB58A44BA4B193F7D63E4988FB4DB770` | `Portraits/CustomNpcPortraits - Arueshalae - Evil/Old Version/Fulllength.png` |
| `E029D2B2B424C7873495DB7115F5B0E88BC4C0320115C1ED5620AC59E3F39372` | `Portraits/CustomNpcPortraits - Arueshalae - Evil/Old Version/Medium.png` |
| `6B07F66E6231DE5CA763A2FE3C47C27CFF27CA165D567515A7A6BB9BD20E6A58` | `Portraits/CustomNpcPortraits - Arueshalae - Evil/Old Version/Small.png` |
| `41FEE632E808649551E4883C22D71D5C9DF7F4664B881675AB68C1A61026012D` | `Portraits/CustomNpcPortraits - Arueshalae - Evil/Small.png` |
| `F3860899DCE696DB54D2D981711601AE09C2D79636DCBA984170898698E9A0DB` | `Portraits/CustomNpcPortraits - Camellia/Fulllength.png` |
| `0E3CD42D7B47A22C231D93AEFA5F7D7A337998B18E38FA6D85EEDE0426825DE2` | `Portraits/CustomNpcPortraits - Camellia/Medium.png` |
| `159A848B9DA37EF08624FEC0ADC0FDFAA3340E709650DC65F0CFFA180576C637` | `Portraits/CustomNpcPortraits - Camellia/Old Version/Fulllength.png` |
| `D99B9BC6A326FA9CCC6E088D26D757D1F57B102F1D539A793D2CA3C8C6994A58` | `Portraits/CustomNpcPortraits - Camellia/Old Version/Medium.png` |
| `96B7D91B3BFB874CF96AC4689CA38AFF8C73C10C837F7EE838346BB8AC2E10C6` | `Portraits/CustomNpcPortraits - Camellia/Old Version/Small.png` |
| `9DFC46BAB3A9892EF8D511094D8E7918BADF829BFEE594613F1EE8E9BAB0EF03` | `Portraits/CustomNpcPortraits - Camellia/Small.png` |
| `4EE5746A9631ED57C49FC188C0D45E8D6D64F0C87638701E44BE9946E2625169` | `Portraits/CustomNpcPortraits - Ciar - Undead/Fulllength.png` |
| `95DC84859C78773F9385A83486CBDF5C638569DFDCD3C16E04231DEFFCAB5D4E` | `Portraits/CustomNpcPortraits - Ciar - Undead/Medium.png` |
| `BD8EA251DCA448A55A20934F7BC121AA68C75EFE45626791B0912F55A2BF74B9` | `Portraits/CustomNpcPortraits - Ciar - Undead/Small.png` |
| `FC3C68E80B66FA17855BDA74AEECA18461B2555CB61BA812176ABC862FD14D07` | `Portraits/CustomNpcPortraits - Daeran/Fulllength.png` |
| `1AFE275FBB6C86B0F7B6F2ECE5F4F90846D84FC82CBA18A60EDB0B60302C032E` | `Portraits/CustomNpcPortraits - Daeran/Medium.png` |
| `C9A9902B52C1F4243D3C1A20A94A5D22DF9F6A61D23E86F6E85853C34BADC618` | `Portraits/CustomNpcPortraits - Daeran/Old Versions/Fulllength.png` |
| `4EE01E9F448BEC7E37E55B9CB71B8C219C60F798312AA04944149B9F1D71097A` | `Portraits/CustomNpcPortraits - Daeran/Old Versions/Medium.png` |
| `7AEC89907D8F0991F155BFB9877AEDC696C7AE615B959A4E70610759993B4BB9` | `Portraits/CustomNpcPortraits - Daeran/Old Versions/Small.png` |
| `851210123BAD43BC998DFDEFB471CB6A30D2C02D031EDFEE8C444146EF0599A8` | `Portraits/CustomNpcPortraits - Daeran/Old Versions/Smaller Smile Variant/Fulllength.png` |
| `FDC6020E214A696722117B9BA1570D9A474F952CF4A897C7D5B373E579C7A090` | `Portraits/CustomNpcPortraits - Daeran/Old Versions/Smaller Smile Variant/Medium.png` |
| `211C4D564292EDF826D31AE41DA4E9FC80F13214A96B9A6BF69B676737B1B445` | `Portraits/CustomNpcPortraits - Daeran/Old Versions/Smaller Smile Variant/Small.png` |
| `314A2A302492B2F88EA6C8FF85E934E428DC411063DBD22B687BCB56048A9CFD` | `Portraits/CustomNpcPortraits - Daeran/Serious Variant/Fulllength.png` |
| `2DBB29D020BDD8E7C1F3186866210918FAC35734183E37E31A7D7652A72FE742` | `Portraits/CustomNpcPortraits - Daeran/Serious Variant/Medium.png` |
| `9E810AC9D209E01BA5CC0CE8FEBAB0C5BB85797598F446421D0E4C34F8FA0C0E` | `Portraits/CustomNpcPortraits - Daeran/Serious Variant/Small.png` |
| `1C7643F951906F4A99E4BC013259908907E5285D927BF72D28A0E46DCF68D4F9` | `Portraits/CustomNpcPortraits - Daeran/Small.png` |
| `53672D6A8D148346DCCF99DD0D97FE07A56249871E74B1962904A365FC207812` | `Portraits/CustomNpcPortraits - Delamere/Fulllength.png` |
| `78E0D931E44714EB1B44AD0A2098FFBBA5DB74C2D7B519BADA925B13B6737DEE` | `Portraits/CustomNpcPortraits - Delamere/Medium.png` |
| `ACD44F516BF410FF0F4E8B13943B54BCDAD12C7B0557347C48FACBA706381B37` | `Portraits/CustomNpcPortraits - Delamere/Small.png` |
| `7DC12BA3D0542486591A49ABF54C6197C8EEC9B5D74C76B244A5E79FF1888E27` | `Portraits/CustomNpcPortraits - Ember/Black Eye Variant/Fulllength.png` |
| `F3E58790A64B2CF659D4508CC881D1AB62A0CC4E893DCA08763501A7592EA7F4` | `Portraits/CustomNpcPortraits - Ember/Black Eye Variant/Medium.png` |
| `E8CCB891E088B5727AD460376B0DBF318ACFF77FA12138C0D0F3FAB90FEE121F` | `Portraits/CustomNpcPortraits - Ember/Black Eye Variant/Small.png` |
| `741417D6BF63DED6FF38901843D4E00F7A17BEC4D21109FF22D13E964081E768` | `Portraits/CustomNpcPortraits - Ember/Fulllength.png` |
| `BE6A4A128E1C2657A8A1AFDC8D2A79EFC62EDF39E0A5FEC3398027B3322D5CE7` | `Portraits/CustomNpcPortraits - Ember/Medium.png` |
| `E06CB70067883C96C8B5751B44FB2AC9DE828C46F5C2551CBAD7791F7FA06647` | `Portraits/CustomNpcPortraits - Ember/Small.png` |
| `D4CACD2CC801823314F9C7F83ED90ABF5C32559B94306C70E808E1E4ABF27A47` | `Portraits/CustomNpcPortraits - Finnean the Talking Weapon/Fulllength.png` |
| `904BF644BAED550C8B5693EC780FA1ECE4F2B00262BE70B3B8AC523BA27614B7` | `Portraits/CustomNpcPortraits - Finnean the Talking Weapon/Medium.png` |
| `EA964FFE5A7F225227709F32C95885E66E1A31FF71D46DE5084AFF4972CD5BA6` | `Portraits/CustomNpcPortraits - Finnean the Talking Weapon/Small.png` |
| `E341B42CA51A27B8FFA2883CE2E615119E351180348CD37BE7E4411ADB5A5781` | `Portraits/CustomNpcPortraits - Greybor/Fulllength.png` |
| `5F2AC0D8F91697DAC96679DF112F4890BE61E3064027821AE2A28F77F0506ACA` | `Portraits/CustomNpcPortraits - Greybor/Medium.png` |
| `79732F129D85F953CDF19D203EC924204091B969264A9D48AAA500A55DDDE5AA` | `Portraits/CustomNpcPortraits - Greybor/Small.png` |
| `0FA64B16A17D4F755DF46D03158F083EFB6F161A31FADE80B6F54E8878D08389` | `Portraits/CustomNpcPortraits - Horgus Gwerm/Fulllength.png`<br>`Portraits - Npc/Horgus Gwerm/Fulllength.png` |
| `62E7F7443FF4AACE431B67FF424C5F74B11130CE4F0DC3C458D7272C89D72B4A` | `Portraits/CustomNpcPortraits - Horgus Gwerm/Medium.png`<br>`Portraits - Npc/Horgus Gwerm/Medium.png` |
| `0E541137FF0F2F86A1712F2779838EB81DC8A6C36B059D7DF77EC32D28C9A08C` | `Portraits/CustomNpcPortraits - Horgus Gwerm/Small.png`<br>`Portraits - Npc/Horgus Gwerm/Small.png` |
| `FE95C22413651CA4F97512DEB557A133303F6194BF709F9566D8575A3BE6318D` | `Portraits/CustomNpcPortraits - Hulrun/Fulllength.png`<br>`Portraits - Npc/Hulrun/Fulllength.png` |
| `1095FAF3CBC37C4AAD4FB441F5AEAD791EFE757CA343069C76ED523EC0A93ECF` | `Portraits/CustomNpcPortraits - Hulrun/Medium.png`<br>`Portraits - Npc/Hulrun/Medium.png` |
| `B2577FD3D18CA6300569C6A82BC605FFD0BFAC56DBA373D0D350A06070842072` | `Portraits/CustomNpcPortraits - Hulrun/Small.png`<br>`Portraits - Npc/Hulrun/Small.png` |
| `1B0F5E45CB237D4E754B6862EAD610E7EB94BBA13EB02CB8562A06DBAD01ADF7` | `Portraits/CustomNpcPortraits - Irabeth/Fulllength.png`<br>`Portraits - Npc/Irabeth/Fulllength.png` |
| `7319099690CE2755A108F2B7A0F7FB767BEC1018E1CDDECA78B3ED66EE12B83D` | `Portraits/CustomNpcPortraits - Irabeth/Medium.png`<br>`Portraits - Npc/Irabeth/Medium.png`<br>`RanRomance-Tirabade/Scenes/Irabeth.png` |
| `22571C62611A8286820AC54555741AA0C5569AAAE7D64100D1B124E1C7537A06` | `Portraits/CustomNpcPortraits - Irabeth/Small.png`<br>`Portraits - Npc/Irabeth/Small.png` |
| `FC3EF13A67F7C1D55A53B86F5386C61DCA15F13DB9131FC4F4FC9F1DF835A1C7` | `Portraits/CustomNpcPortraits - Lann/Fulllength.png` |
| `60FBEC7788ACF16B0E80157E902D3E912B692C5C827F0C526FEDA2873BB840BD` | `Portraits/CustomNpcPortraits - Lann/Medium.png` |
| `54A24BAB891D017C95A507177A68FB4F17737EFCE4388DE0055B202DA26B2B3C` | `Portraits/CustomNpcPortraits - Lann/Small.png` |
| `50DBE558A282C144F356844C10E582C1E641EFA79AB9ECB84190E9C9A886EE77` | `Portraits/CustomNpcPortraits - Nenio/Fulllength.png` |
| `B41282B20CE851DAE4A2EB13560965A592D259A2026205520BED4AA8766C8F50` | `Portraits/CustomNpcPortraits - Nenio/Medium.png` |
| `C3EA69A0902BFDE07C5D8EEBE29CD0F11BE1A2CE9DE30D8C045333A409B20BCD` | `Portraits/CustomNpcPortraits - Nenio/Small.png` |
| `016E86131B7715D2187B6FC5608E9F34D11DD6D3F4FFA64253ACA309474B6207` | `Portraits/CustomNpcPortraits - NenioFox_Portrait/Backup of Game Default Portraits/Fulllength.png`<br>`Portraits/CustomNpcPortraits - NenioFox_Portrait/Fulllength.png` |
| `D706C7BD2979CF3E37F67162265027773771207A4F843C7814FDB90D630766C6` | `Portraits/CustomNpcPortraits - NenioFox_Portrait/Backup of Game Default Portraits/Medium.png`<br>`Portraits/CustomNpcPortraits - NenioFox_Portrait/Medium.png` |
| `DE632DC1FEE1D922F77AE71AB11DA8FF9F2E73ACA8357C16E99A3ADFB637D8EF` | `Portraits/CustomNpcPortraits - NenioFox_Portrait/Backup of Game Default Portraits/Small.png`<br>`Portraits/CustomNpcPortraits - NenioFox_Portrait/Small.png` |
| `A7CA3252A82692E112F24D27B7F312683AE497FC1B76E3CE274499E58E01924F` | `Portraits/CustomNpcPortraits - Queen Galfrey/Alt Version/Fulllength.png` |
| `AD0E1DB71501A5E79B2B8D9B2243CB411BE31E1A3EFA7E558E79534B4D8BBFE7` | `Portraits/CustomNpcPortraits - Queen Galfrey/Alt Version/Medium.png` |
| `9EC3B01E5AC153CAB48C73F2B10C3B5B8CE1BBD9515431791078EC4F42993350` | `Portraits/CustomNpcPortraits - Queen Galfrey/Alt Version/Small.png` |
| `01381A3A4DBF12CA564E65294CB64C16EEF08F38DF22C5C064D462A6EC0E32E4` | `Portraits/CustomNpcPortraits - Queen Galfrey/Disguise Galfrey/Medium.png` |
| `29368B560A18D5DDEEE021C16082BE5ECD9790947B1A33DFC9E878162F8036D9` | `Portraits/CustomNpcPortraits - Queen Galfrey/Disguise Galfrey/Small.png` |
| `9B16B3AD9D9D00267F48FF02A92D23659274A707B5ADCD22CA68EE24D048EDAB` | `Portraits/CustomNpcPortraits - Queen Galfrey/Elderly Galfrey/Fulllength.png` |
| `9AB724E9F3BE5D44915B5C1B0F7CFD7BDF9AECDEE32994BDB99DAC54B2383D0F` | `Portraits/CustomNpcPortraits - Queen Galfrey/Elderly Galfrey/Medium.png` |
| `C822FC1E925DE3E9E4CEC2E318E50BCD083CBC5B631BA947B66E73E8FA7A74D8` | `Portraits/CustomNpcPortraits - Queen Galfrey/Elderly Galfrey/Small.png` |
| `57EC7405ED0B9D467CE6A6ECDC5742B74062E9CE1972DCFB19355FA98D0166E8` | `Portraits/CustomNpcPortraits - Queen Galfrey/Fulllength.png`<br>`Portraits - Npc/Queen Galfrey/Fulllength.png` |
| `3ED0FE671612B54AD680E0264A62F4DB772E92C1C2037D34929A0C723EC8CBB0` | `Portraits/CustomNpcPortraits - Queen Galfrey/Medium.png`<br>`Portraits - Npc/Queen Galfrey/Medium.png` |
| `43D2DFE1CECC4B20AE67805AC168BB954FDB7A171C5C45A7A2AB4C298ECAE7FB` | `Portraits/CustomNpcPortraits - Queen Galfrey/Previous Version/Fulllength.png` |
| `63325214E9C59941740DAC184ED664EA7A3C71E4EFC0A62C791AA49C55E5B1B6` | `Portraits/CustomNpcPortraits - Queen Galfrey/Previous Version/Medium.png` |
| `388EBF53B9F4EDE4C76EE3867A7DF16111508E93CA9CA351D081B87868E8DB8B` | `Portraits/CustomNpcPortraits - Queen Galfrey/Previous Version/Small.png` |
| `A7DDB0A409F5EE8946D30C8ED79E44CC3A1C7639A94D6A22AF9B29551508979C` | `Portraits/CustomNpcPortraits - Queen Galfrey/Small.png`<br>`Portraits - Npc/Queen Galfrey/Small.png` |
| `D15FA480745BE5F2163AD8E1AAF0C182898323590D7408DBF815106E31181E9F` | `Portraits/CustomNpcPortraits - Queen Galfrey - Undead/Fulllength.png` |
| `0AB0BC5E58FB54FADC1B9239C1A1C9E602FE8BBF83C89770F9970EED2F3EF4DD` | `Portraits/CustomNpcPortraits - Queen Galfrey - Undead/Medium.png` |
| `98A244250F1515AE34DB81B29885A87C52D778E4DB2299C4C5A01934BE96F55D` | `Portraits/CustomNpcPortraits - Queen Galfrey - Undead/Small.png` |
| `F4DC1695FE6928E350F622657FC985262240246DA69061BC4DE35FF907527431` | `Portraits/CustomNpcPortraits - Regill/Fulllength.png` |
| `89EF497F565DB9F7791FB58953BDA831E506232480E308494867B96B0C823242` | `Portraits/CustomNpcPortraits - Regill/Medium.png` |
| `C866A45C82C4435640FD5F7DB3A13E43BB9B74F46E6476ED21707B98869662E2` | `Portraits/CustomNpcPortraits - Regill/Small.png` |
| `9248C4ED7072E9653BD0826032376E1B6819B52D1CEDE80B2ED8FDBA847C169B` | `Portraits/CustomNpcPortraits - Seelah/Fulllength.png` |
| `FBD96CE4D0150A56E08E7F4108D0110F491EF82B6E998726DD732E491FBB3C27` | `Portraits/CustomNpcPortraits - Seelah/Medium.png` |
| `3022F3E1328623281D1653B766B87950B7332B6B0D5DD2DB3E55DE32358FB41A` | `Portraits/CustomNpcPortraits - Seelah/Small.png` |
| `58E1504397A79F5E2D1E1F2247DD7A095F36392D9E492D01374BEA8D6D430F0D` | `Portraits/CustomNpcPortraits - Sosiel/Fulllength.png` |
| `EAB3F46373495FA4E1AAF2CC7457683F3623F72AD94CED491AFA0759AD4ECAF0` | `Portraits/CustomNpcPortraits - Sosiel/Medium.png` |
| `9701BA196BEB228AEBE8E56BDDED3ACFB3519664872F8F7AE4B8C8E801C3FDD7` | `Portraits/CustomNpcPortraits - Sosiel/old Version/Fulllength.png` |
| `44726688F3DA42CB3C71CAFE8E63A9CF43439E6F114E955D4E6A8EBAD132439A` | `Portraits/CustomNpcPortraits - Sosiel/old Version/Medium.png` |
| `BA9D8D856A2492D6FE5E79D7F62B33CBA2EB33A02FE5B7E975C206D2873A509C` | `Portraits/CustomNpcPortraits - Sosiel/old Version/Small.png` |
| `009F96C2B36BD0CEE5DFB531B3B681AEB40F30224BEAF14FC8F99E4BE2C9B602` | `Portraits/CustomNpcPortraits - Sosiel/Small.png` |
| `76262B9BF01A69F2CC6F767FF79FCDB1CE57B9181DFD237A708042B89F2B98E4` | `Portraits/CustomNpcPortraits - Staunton Vhane - Undead/Fulllength.png` |
| `F1F953E03430A2781A6FD26377B3C692DBFFEBBB696A2073A35E1C59A3686A38` | `Portraits/CustomNpcPortraits - Staunton Vhane - Undead/Medium.png` |
| `0C591385E888E93DFF8429385E3FB6E2FF95BC8A408A654E252BB6DB3E0B8EB6` | `Portraits/CustomNpcPortraits - Staunton Vhane - Undead/Small.png` |
| `E79E90A9E4A348FFF7C222BDD7BDC74944AAA7568096B56CE2C28F8F2E97FC8C` | `Portraits/CustomNpcPortraits - Storyteller/Fulllength.png`<br>`Portraits - Npc/Storyteller/Fulllength.png` |
| `EF80EBDCFF0A1D3DC366EE706A2772D13BBB23984CA61EAA83EB915CB664778D` | `Portraits/CustomNpcPortraits - Storyteller/Medium.png`<br>`Portraits - Npc/Storyteller/Medium.png` |
| `35FEA356203A7591A0916647772CA06B376CA0286B1D6E7E5D5B68BD77F5DC3A` | `Portraits/CustomNpcPortraits - Storyteller/Small.png`<br>`Portraits - Npc/Storyteller/Small.png` |
| `1AD0D64FBE67FA8BCD91308A98746A3F10011D33481A60FC47D0EBCB7F49CACF` | `Portraits/CustomNpcPortraits - Terendelev/Fulllength.png`<br>`Portraits - Npc/Terendelev/Fulllength.png` |
| `FA827EAD389AE7923564B12E5B5F9DABCFB946840ED2334B5BBD00B91B6DF3D9` | `Portraits/CustomNpcPortraits - Terendelev/Medium.png`<br>`Portraits - Npc/Terendelev/Medium.png` |
| `71F59ECF77E41DFE6EB264CB37DF457D13AE8A4591166152A156526DDC6AFD1E` | `Portraits/CustomNpcPortraits - Terendelev/Small.png`<br>`Portraits - Npc/Terendelev/Small.png` |
| `62562925CEEF705AE9202C71E544A34C5A8963A42F7D53A499184F028D132641` | `Portraits/CustomNpcPortraits - Trever/Fulllength.png` |
| `DE1B0D6E7740ADB587D8356D1161B5C16D04E5B515F170215CE5571743157B64` | `Portraits/CustomNpcPortraits - Trever/Medium.png` |
| `DFC1D78DC35A1B2C0C75E89F950A7A3BF7EB30EE8DB60BF3C9E02D8AB2DB48FC` | `Portraits/CustomNpcPortraits - Trever/Small.png` |
| `55E769D8FAC005B46C485D87DE4317E79E5410456193A53FC12EB813AFE78C20` | `Portraits/CustomNpcPortraits - Ulbrig/Backup of Game Default Portraits/Fulllength.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/Fulllength.png` |
| `1F8342D98A0B830825A961112CE8B2AC2DD3ED7E3FE7BF2256DAA633B1F18C28` | `Portraits/CustomNpcPortraits - Ulbrig/Backup of Game Default Portraits/Medium.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/Medium.png` |
| `AB77B635FFCC595C1819FBBE5F2B5D096BE339C859183FA94F3F56A2F74DAC0F` | `Portraits/CustomNpcPortraits - Ulbrig/Backup of Game Default Portraits/Small.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/Small.png` |
| `95136ADFF20E305E9848482366BFBD7678A5A85B37AFF4C1A1F785D5B44EE0B6` | `Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff14/Backup of Game Default Portraits/Fulllength.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff14/Fulllength.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff9/Backup of Game Default Portraits/Fulllength.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff9/Fulllength.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff_Cutscene/Backup of Game Default Portraits/Fulllength.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff_Cutscene/Fulllength.png` |
| `9D6EE7328A38FA6C1289AE2F61A74BD24ADE47B0DAE76684FD06E61A07F2EFB1` | `Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff14/Backup of Game Default Portraits/Medium.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff14/Medium.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff9/Backup of Game Default Portraits/Medium.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff9/Medium.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff_Cutscene/Backup of Game Default Portraits/Medium.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff_Cutscene/Medium.png` |
| `17BD8F9330DCF4C51E47799C0010DA7C4950E5A054F3288456BAB8119B46E763` | `Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff14/Backup of Game Default Portraits/Small.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff14/Small.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff9/Backup of Game Default Portraits/Small.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff9/Small.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff_Cutscene/Backup of Game Default Portraits/Small.png`<br>`Portraits/CustomNpcPortraits - Ulbrig/ShifterWildShapeGriffonBuff_Cutscene/Small.png` |
| `AE2C4C226DB19BB9202B5476FCE93DE2D895FB933A8E826FC1D83ED3DB0FF33C` | `Portraits/CustomNpcPortraits - Wenduag/Fulllength.png` |
| `3385B198C468094B5DB6DEF0CCAD14E437907D5092FDAB623381D9B95D4D79D2` | `Portraits/CustomNpcPortraits - Wenduag/Medium.png` |
| `2605A7246D63D8A29520A75E2686F68E992E00D87884FF5B42FF3E44FEE98FE3` | `Portraits/CustomNpcPortraits - Wenduag/Small.png` |
| `CB9E81AABFCFD3DB1F277B1A744983F81BA35B0D1BA2F4BB597EDEC4EE7F8749` | `Portraits/CustomNpcPortraits - Woljif/Fulllength.png` |
| `1C1ED3F07FA6E3CF4632C7112CCD32B04602004CF4813A6BE07545BE3BF65B91` | `Portraits/CustomNpcPortraits - Woljif/Medium.png` |
| `C4D7C40B55BF4C3FADB4574573D7B23BBC98A3D9641D8956D35917C4A3469E5E` | `Portraits/CustomNpcPortraits - Woljif/Small.png` |
| `D1B6DB68A569ECEEE011A3A644CBD273F3A4CA4BBA7BC356C3ED06F01F6AF145` | `Portraits/CustomNpcPortraits - Woljif - Demon/Fulllength.png` |
| `786AFA738335E6A36C45F60563469AECEC2E75A3C82536465A3517689DA4D496` | `Portraits/CustomNpcPortraits - Woljif - Demon/Medium.png` |
| `95C3486FB7FF28AE8826EB556A06DB05BD3500970C735943AC52A6090C3F54F9` | `Portraits/CustomNpcPortraits - Woljif - Demon/Small.png` |
| `E54118B5BF4D483A03BCD2595E90A54B9FA934B0E08EB89900AE17A231DDDA13` | `Portraits - Npc/Aranka/Fulllength.png` |
| `848F6A1E9E2F9533087D1BF168146A9DAE7A07BD75073C02B60B1FAD50500F07` | `Portraits - Npc/Aranka/Medium.png` |
| `DD183E6BD618704876700726787BFC45467C76E12BF5426D92127A535B2DD69A` | `Portraits - Npc/Aranka/Old Version/Fulllength.png` |
| `83198BD37C217D2B74890740CA85C6F80548EF1E9DF8860738975B0AECE062C8` | `Portraits - Npc/Aranka/Old Version/Medium.png` |
| `87403221BFD68FD99CE98D3F87C0E5D9445F7A5447E1B55385A693B9D2F1C47A` | `Portraits - Npc/Aranka/Old Version/Small.png` |
| `58F492238582E5854FC8A23BAEF08456A066EF6082981D6666E7D189815280BF` | `Portraits - Npc/Aranka/Small.png` |
| `B7EEBE8D3E36CB2337ABC5D9CFA0A0760F9045854DC36D6B18A84779B5533D25` | `Portraits - Npc/Areelu Vorlesh/Fulllength.png` |
| `246A7D00DC17563CF5CF33CC7E1E62CA4B5ADD662FB50D60A7ED6A8D93668F20` | `Portraits - Npc/Areelu Vorlesh/Medium.png` |
| `67081EA92110BE603E658B824D9274E4F1748565F26CF35D06D2887BC4BFABA9` | `Portraits - Npc/Areelu Vorlesh/Small.png` |
| `004F1D396E34435546BF5174D06669A271001B0EE432E8E3DA3F4FB1DEFD2BA6` | `Portraits - Npc/Arsinoe/Fulllength.png` |
| `283AE56F95CD843B042923AD28FE2277B511F592CA7166293D0CBB95D034B6CF` | `Portraits - Npc/Arsinoe/Medium.png` |
| `E550EF67FD012F2BD557303301CF3F4D81153E37B84F941C552BB47DB40D184B` | `Portraits - Npc/Arsinoe/Small.png` |
| `6AA5D8EDE137F314B683BA72F632D742E0F33879B1FED1C88DE11D24024ECA7E` | `Portraits - Npc/Baphomet/Fulllength.png` |
| `BE50E1EA1A97EAEA8642BFA51AD552432843F46D05C1D7D5D42B0C30D037A964` | `Portraits - Npc/Baphomet/Medium.png` |
| `767AB2E28AACE991C39E9FAAFE4DECFEDEC30EB08A8787647F599834000FC2F5` | `Portraits - Npc/Baphomet/Small.png` |
| `9561CCC3F9DD06B268B9EF025C5D9C5909DAA2A24D6227002DEE61817C32B191` | `Portraits - Npc/Ciar/Fulllength.png` |
| `5AE63DBA4110A4DD8A84A7D560075B60B147342F9FAED99137D82AA804A7BE6A` | `Portraits - Npc/Ciar/Medium.png` |
| `50BA9443B0C63C93A7187D8867709B2DCB64217FB1324EF2CDB419CC7D8B842A` | `Portraits - Npc/Ciar/Small.png` |
| `E13CFE0E079C62358C9E541E456B6B1395FEBD302B47B62D4B484087E4815BA6` | `Portraits - Npc/Hand of the Inheritor/Fulllength.png` |
| `A01835D0589374CF47557584C18ED19347522D117206555BDB712D527BB5F4BF` | `Portraits - Npc/Hand of the Inheritor/Medium.png` |
| `E61DF5BE082309EBC857B012D8B87FB496EDA412A07EF9735FF2656C67A369EC` | `Portraits - Npc/Hand of the Inheritor/Small.png` |
| `5075716E1E030598D2CB0AFC25A0ADD89E32A4CCB8BA23F3EADD38A0BD267277` | `Portraits - Npc/Hilor/Fulllength.png` |
| `E60FDCCBF199A7BC80103F729E1507C2E56B97C59115D5CCF894B7745C23E666` | `Portraits - Npc/Hilor/Medium.png` |
| `17253DF3DFA59B6ADD2E1A46AEE3C8BBA48A46B1D5A9C8E12475E92505FB945B` | `Portraits - Npc/Hilor/Small.png` |
| `A561F952FA2AA2F58C3E1EF75654563AFFA8AF281A4C5801CD1B5D23A52F91E2` | `Portraits - Npc/Iomedae/Fulllength.png` |
| `5DBBD7E2EA74707753761994487255210C95E44A232F27F4BE3E18B208C5F53A` | `Portraits - Npc/Iomedae/Medium.png` |
| `BD72943A3268C799C26ED7E044443A0B20759734805B492D61B9A41FEC2A57E3` | `Portraits - Npc/Iomedae/Old Version/Fulllength.png` |
| `89DD0FD41ADFF67E3008BF9447113BC8E64F1BF240F5D2FC16215BB79A31E56E` | `Portraits - Npc/Iomedae/Old Version/Medium.png` |
| `DDE33C8C0F2696689E5DEE139C6E00F53C61E39A53E5974DBAE0EFCB92F31DEE` | `Portraits - Npc/Iomedae/Old Version/Small.png` |
| `27EB478BAA43D003EDCDFB3012EFABE38D4564876EA4522427A09071C45D187E` | `Portraits - Npc/Iomedae/Small.png` |
| `350E187AF730458DC40CACB9F6AB3A7965286E31AED812FC4D2E0BA4FBFF742A` | `Portraits - Npc/Jerribeth/Fulllength.png` |
| `F8B975EACCF71970142EDE887E1157E190B0F78DC2049127856BE4ABDCD49BEF` | `Portraits - Npc/Jerribeth/Medium.png` |
| `848B987B9873AAAC5F4F8B31AA0C7C031225F3A0F307BA4A0ED92F1DD0F7076C` | `Portraits - Npc/Jerribeth/Small.png` |
| `A4FEE12C49B7D67FC69B89F17AA77A9B80BE8478013D7E301E0AF30DEF197341` | `Portraits - Npc/Minagho/Backup of Game Default Portraits/Fulllength.png`<br>`Portraits - Npc/Minagho/Fulllength.png` |
| `BCCAB41ACB8D194818B2853CE1C9BF34151A3A383AC3513772F6B30765E57CEE` | `Portraits - Npc/Minagho/Backup of Game Default Portraits/Medium.png`<br>`Portraits - Npc/Minagho/Medium.png` |
| `41B1F4B0505F9A6FEEC6BA3D728D7A4B6F96A95E9005EA29FB03A11C8373D70C` | `Portraits - Npc/Minagho/Backup of Game Default Portraits/Small.png`<br>`Portraits - Npc/Minagho/Small.png` |
| `923BB6B7F6A1D359AE273AD4D44CEB2C11D9E293459229C354FC2FF7C2B59BB6` | `Portraits - Npc/Minagho/Minagho/Fulllength.png` |
| `582E3472826E3EA5947A07941E4B7CD3CC9CBB07FDFF6BBADF2F8D0C845B3A10` | `Portraits - Npc/Minagho/Minagho/Medium.png` |
| `EFABE1E769C9EE92D633F58A57D976674D983CF43C5B82F523351A4578A5736B` | `Portraits - Npc/Minagho/Minagho/Small.png` |
| `C29587178327B889070CF1DF889E2CB0FA651C3C0882D1C2DD5621D4AC2398AE` | `Portraits - Npc/Nocticula/Fulllength.png` |
| `465594632A10CE1075EFD5E04B867A787D31C54031BF1C1D24C2D4B0D02E6377` | `Portraits - Npc/Nocticula/Medium.png` |
| `B8F59125BF5096C4AD7222079AAF6B4EA9D87A843F6D3B9F6768A89F28697F0A` | `Portraits - Npc/Nocticula/Small.png` |
| `E4F08E7101A02E4ED7251D9118847ACE5C3F08E587D174B93C927CD1B506E223` | `Portraits - Npc/Nurah/Fulllength.png` |
| `07F0C94E52F149A1DBE5AE25A4475B52042C22BC8CCDB1E79D7FCEC8A168FC17` | `Portraits - Npc/Nurah/Medium.png` |
| `C323454411B6BDA00A7D29BA604E37C6944D11B491F76014EE7BD392F9B9670C` | `Portraits - Npc/Nurah/Small.png` |
| `90620D3EE6DF6A9AA23A24F3CB822A94ECE32C4061EA7A38494499678F6910DF` | `Portraits - Npc/Socothbenoth/Fulllength.png` |
| `F03C4727E281FD42AB41F52B5EC72F039A79E6BD5B37126BB805B121B1996D8B` | `Portraits - Npc/Socothbenoth/Medium.png` |
| `66B1C24A85EF2952C8837E58004EC74DB9F21E986372E5AA187CCB4DB053B4B5` | `Portraits - Npc/Socothbenoth/Small.png` |
| `7AB958A1BAF1082CDA9BFB350817007E04E32B1C4D2086726C80C05EC1214E1C` | `Portraits - Npc/Staunton Vhane/Fulllength.png` |
| `8075163F69993AB6EB2C9C53D57F0F073631B2C0AA82C9FD86DA2CF7DDD2A040` | `Portraits - Npc/Staunton Vhane/Medium.png` |
| `A9A37CD1D31EACF26B382D813D726334E08EC6FBEAC0AC4CC72A9E6E2109CBD3` | `Portraits - Npc/Staunton Vhane/Small.png` |
| `4B54E3A241710BCFC628A3C930029493B8B11606965548AA1CA194FF2205E4D9` | `Portraits - Npc/Wilcer Garms/Fulllength.png` |
| `84FACF9EF0357ABF0B2D77C8DCA4C674BF6D3898B4E17EEA82E79E780A386F46` | `Portraits - Npc/Wilcer Garms/Medium.png` |
| `D8F3D8085D8B8859F1C3D3C245B55BF76F7DAAAB52C3449A35AE18436E64B3E8` | `Portraits - Npc/Wilcer Garms/Small.png` |
| `8A2E1C694B5E3AF94F873BA45943B7301DD3198C03A5B26039968899AFC3DCBD` | `Portraits - Npc/Xanthir Vang/Fulllength.png` |
| `0EDF1B3430734F80C6DF5E4D10B5A6CCC8B1C41D2B74D6FCF90F2BC7720B1E9B` | `Portraits - Npc/Xanthir Vang/Medium.png` |
| `377041DA9FF05E31AF393198EDC4BF4E42BCB6D33C8D84FA413783E92795A852` | `Portraits - Npc/Xanthir Vang/Small.png` |
| `6F6717F2CCB7751C229C3A634A6C8C7E34FC94F7AC2869A469A782A59DFE95DB` | `Portraits - Npc/Zacharius/Fulllength.png` |
| `CE5BC7F989ED524031F0914F10F082FD70453E1778510073D3014AC7FB61D798` | `Portraits - Npc/Zacharius/Medium.png` |
| `50C20E211DFE8BCFE5D86EFE1E4114D63E297D238D39783BB0EB70AAFAADAFFA` | `Portraits - Npc/Zacharius/Small.png` |
| `D125515DA14EA5333DFB8E800F766F5ABC0C3B2820C78BF506E880271457EBBF` | `RanRomance-Tirabade/Scenes/Together.png` |

## Additional local image hashes

The following 18 local images are absent from installed byte groups and were each directly viewed.

| Relative local path | SHA256 |
| --- | --- |
| `RanRomance-Tirabade/Scenes/ArsinoeShop.png` | `C3DDEC27FF8409B049F82D6A3D07028001CB1D485F5829BF4C2942C7AE307315` |
| `RanRomance-Tirabade/Scenes/ChivarroWarm.png` | `0BFC0F27C92CADFDEC2FE5F9D803E7D4C9DBE86D60A1B37A18B050095FEC48A2` |
| `RanRomance-Tirabade/Scenes/GesmerhaWorkshop.png` | `EB3FD14D0D06EAAF5E4578DB833CA6B474A8593659F39F740ADFA47E513596DE` |
| `RanRomance-Tirabade/Scenes/Jerribeth.png` | `D27050B867E90E8E151496E9B94AA71811726FAD0A8263F8DC3F84EE3DB63509` |
| `RanRomance-Tirabade/Scenes/Konomi.png` | `74267A675F25A786A118B54631D9093305478A484AACEA370082708AFB35B196` |
| `RanRomance-Tirabade/Scenes/KonomiPrivateClose.png` | `5D605330C541FC3A39A671E0ADB7786CBE6F9FBD1D6203A9CF96CD8091C9D504` |
| `RanRomance-Tirabade/Scenes/KonomiPrivateDialogue.png` | `9208ED76F84A33C146AA672BAC54DA57FED88EE9CEDA1EC2333FAF2F5B87DE48` |
| `RanRomance-Tirabade/Scenes/KonomiPrivateEvening.png` | `FFA19D95FFB15CA81EBDA953E14E543BAC0D44847F69E99EDD9DED5D673E8B2C` |
| `RanRomance-Tirabade/Scenes/KonomiPrivateNear.png` | `5B774776DE5FDA5696CC9EA68F55CE34B7EF0B07F00555A3BB498C6BBD01277E` |
| `RanRomance-Tirabade/Scenes/KonomiPrivateSeated.png` | `12560274FDE2B08548136F3471A5ACD974DA6245D2DD1D3F2C37AEB1F2C675EF` |
| `RanRomance-Tirabade/Scenes/Nocticula.png` | `D82D234E6E60DCAA614A06C320001E0FE22A54330FBA185604AA6DCDEF5BD5C5` |
| `RanRomance-Tirabade/Scenes/SoanaForest.png` | `323F34726445958368D1441E4929D83C33258457BEF0CDD0B54F429701856334` |
| `RanRomance-Tirabade/Scenes/TargonaCorrespondence.png` | `0214664A70C5A74C7CA790068799394FADA5872E594F7522E0578EA76AD99FE6` |
| `RanRomance-Tirabade/Scenes/TogetherReckoning.png` | `1BF1BC93BA18CEF86DE3616ED503BE1085B884E5D8791372324D9E6BFC44C508` |
| `RanRomance-Tirabade/Scenes/TogetherYard.png` | `4D16D17364793720D49710AE55C02F182F34122765FD89542A0D53823C05B609` |
| `RanRomance-Tirabade/Scenes/VellexiaManorSpeaker.png` | `9AB756D627479508C414CBAF3BD8940142F42BFBBF98F0082B1B1963B11D77D3` |
| `RanRomance-Tirabade/Scenes/VellexiaPaintingChanged.png` | `42CD5DDFD78D8696FBD52719840020FA9B7E584FD86614BDF7DBCA2D984E178A` |
| `RanRomance-Tirabade/Scenes/VellexiaPaintingDay.png` | `4074EF5BF78192FCBF0780F060CBC9AB0A7049F94394DEE8BD05F27EEAFCEAA7` |

No installed or local image remains unviewed at content level within these two frozen collections.
Native reference acquisition for most outside-roster subjects remains outstanding, as do exact scene assignment review and live UI crop verification.
Candidate folders outside these two collections are not silently included in this completion claim.

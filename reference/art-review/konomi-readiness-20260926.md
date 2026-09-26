# Konomi art and delivery readiness

Konomi is not art-complete for the first fully illustrated route test.
No Konomi original, runtime scene image, or named NPC portrait was found in the project art tree or installed Mods tree.
The current route asks for a missing `Konomi` scene image on 494 pages and falls back to the Tirabade couple image on 21 narration pages.
Those are distinct delivery problems, not a failed score for an unseen Konomi painting.

I read `art/CHARACTER-DESIGN.md`, inspected actual images through `view_image`, traced the native unit's portrait and model references, and inspected the runtime image loader.
I generated or edited no artwork and changed no shared source, runtime keys, or installed files.
Root explicitly extended ownership to extracted assets and provenance under `reference/art-review/konomi-native/`.

## Inspected snapshot and actual assets

The counted `development/Story.json` SHA256 is `D5200B7DB0D2ECA1EAF958BD8929265B7151D92F21BF210F033A187CE58950EC`.
It contains 62 Konomi scenes and 515 pages: 23 ordinary physical scenes, 24 remote scenes, and 15 epilogues.
There are 480 explicit `Konomi` portrait fields and 35 empty fields.
Of the empty fields, 14 resolve to `Konomi` through their speaker and 21 Narrator pages resolve to `Together`.

I viewed `art/CustomNpcPortraits/RanRomance-Tirabade/Scenes/Together.png` at its actual 1536 by 1024 resolution.
It depicts Anevia and Irabeth sitting close at a table, with Irabeth's green skin, tusks, and gold armor visibly identifying the wrong characters for Konomi's narration.
The installed file at `Mods/CustomNpcPortraits/RanRomance-Tirabade/Scenes/Together.png` has the same SHA256, `D125515DA14EA5333DFB8E800F766F5ABC0C3B2820C78BF506E880271457EBBF`.
This is an actual available runtime asset, not a theoretical placeholder.
Its painterly treatment and readable faces do not make it appropriate for Konomi's correspondence or first private meeting.
I did not rescore its anatomy or Tirabade likeness because that is outside this audit.

## Native portrait trap and usable model evidence

The exact native unit `ca2d58c5c65723945857e04fb85d30ce` is recorded in `reference/canon-review/konomi-contact-records.json`.
Its `m_Portrait` points to blueprint `7929611eb7f84fd583ed8befc53de0e8`.
I opened that actual blueprint from installed `blueprints.zip` at `Units/PortraitsGenerated/d7d34a2cbeb4c6841905e87c51d04847_BCT_Rand_Crusader_Soldier.jbp`.
All three portrait image slots point to sprite asset `5d51770a9a755bc44a0082c041d46b61`.
The installed `Bundles/portraits` container resolves it to sprite path ID `-5372300196617306070` and texture path ID `-3432710434835028245`.

I extracted and viewed that sprite.
It is a dark-haired human male soldier thumbnail, not a usable image of Konomi.
The retained diagnostic is `konomi-native/unit-linked-soldier-placeholder.png`, SHA256 `B9B1F8D331D168012CFAC7E531C81D070CC1FF4B05696498C2FBEAFD5D894D40`.
Its native linkage does not make its face a legitimate Konomi likeness reference.
It must not guide the generated redesign or be presented as her native appearance.
The route's custom loader does not automatically use this native portrait when `Konomi.png` is missing.

The same exact unit instead supplies model prefab `58866e97d128a2d41b42571fd3037ba2`.
I opened the matching installed bundle `Bundles/58866e97d128a2d41b42571fd3037ba2.unit` with UnityPy.
Its `BCT_Diplomacy_Officer` renderer description links material `5948448819311337514` to diffuse texture `-3683816850660787530`, named `BCT_Diplomacy_Officer_Atlas_d`.
I extracted and viewed that actual 512-pixel texture atlas, retained as `konomi-native/-3683816850660787530.png`.
It visibly contains orange/russet fox facial fur, white cheek and muzzle patches, amber/gold irises, a dark brown hair patch, and deep blue/teal and burgundy/red garment panels with gold geometric trim and red jewel motifs.
These are direct palette and material observations from the unit-linked model.

The bundle also names a separate `TA_KitsuneTail_F_KT` material and renderer.
That confirms a kitsune tail element, but its diffuse texture is an external asset reference and was not independently viewed here.
The atlas is not an assembled character portrait, a rendered full-body model, or a game screenshot.
It cannot prove the exact finished hairstyle, face silhouette, proportions, costume arrangement, or tail color in the live scene.

`konomi-native/prefab-provenance.json` records the exact bundle hash, renderer description, material properties, and texture identities.
`konomi-native/reference-provenance.json` records the unit-to-portrait and unit-to-prefab chains and the extracted raster hashes and dimensions.
`konomi-native/unit-linked-portrait-blueprint.json` retains the diagnostic portrait blueprint.
The extracted normal and mask maps are provenance material, not alternative paintings or likeness references.

## Exact incorrect narration keys

Every page below currently has scene owner `Konomi`, speaker `Narrator`, and source `Portrait` equal to the empty string.
The loader therefore resolves each to `Together`.

| Scene ID | Exact node IDs | Count |
| --- | --- | ---: |
| `konomi.unsent` | `start`, `wonder`, `fear`, `fear_judgment`, `fear_ordinary`, `write` | 6 |
| `konomi.fate_post` | `start`, `door`, `distinction`, `second_slot`, `letter`, `lover`, `first`, `send` | 8 |
| `konomi.fate_reply` | `start`, `lover`, `first`, `answer`, `accepted`, `declined` | 6 |
| `konomi.private_meeting` | `start` | 1 |

Root has acknowledged this finding and owns the proposed explicit Konomi portrait assignments.
This report records the observed pre-fix snapshot, not proof that the repair has been exported or displayed.
The engine's general Narrator fallback need not change to repair these route-specific pages.

## Runtime delivery contract

`src/Main.cs` resolves explicit `node.Portrait` first, then `Together` for an unassigned Narrator, otherwise the speaker name.
`Portrait(key)` loads `../CustomNpcPortraits/RanRomance-Tirabade/Scenes/<key>.png` relative to the addon entry directory.
For this route, the required shipped file is therefore `Scenes/Konomi.png` under that portrait directory.
The project's corresponding staging location is `art/CustomNpcPortraits/RanRomance-Tirabade/Scenes/Konomi.png`.
Neither exists in the inspected inventory.

The loader returns null if the file is absent or cannot decode and only replaces the book's picture when a sprite is returned.
It does not produce a new image, select the native male portrait, or guarantee a suitable visual fallback.
The exact unmodified book picture visible on a missing-image page must be observed in the running game rather than guessed from this code.
Narration is called independently after the picture lookup, so missing artwork is not evidence that TTS synthesis itself fails.

The loader creates a sprite from the full texture rectangle and caches it by key.
It does not perform a reviewed face crop or define the UI's final fit in this function.
A portrait can be compositionally sound on disk and still be clipped or poorly scaled by the book UI.
Replacing the file after it has been cached does not establish that the displayed sprite has refreshed.
NPC `Small`, `Medium`, and `Fulllength` overrides are a separate delivery system and would not satisfy this scene-image contract by themselves.

## Art direction and missing work

The current brief asks for an attractive, recognizably adult, humanized kitsune while retaining identifying racial and character traits.
The verified orange/russet and white pattern, amber eyes, fox ears and tail identity, dark hair, and blue/red/gold formal palette provide a grounded starting set of cues.
Human facial proportions and an approachable mouth are intentional redesign choices; a long native muzzle is not mandatory.
Natural asymmetry, texture, or other useful imperfections are welcome under the latest brief.
The result should not become a generic human woman with arbitrary ears or a childlike fox mascot.

For the minimum illustrated route test, produce and independently review one portable Konomi image, ship it as `Scenes/Konomi.png`, and repair the 21 narration assignments.
A neutral private or personal setting can serve both retained-office and dismissed histories without falsely showing restored authority or a council uniform as proof of current office.
Any office insignia or appointment-specific staging should be confined to art explicitly assigned to the appropriate ordinary scenes.

The broader finished campaign would benefit from separate office/courtship and private-travel imagery, plus a correspondence image for solitary letter pages.
Those are proposed additions, not keys already required or delivered by the current source.
The quiet, night, and uncommitted outcomes should not all be illustrated by a picture that forces physical intimacy or an exclusive household.
No number of proposed variants is a substitute for inspecting the actual result.

There is no delivered Konomi painting here on which to score attractiveness, likeness, anatomy, painterly consistency, or crop quality.
I assign no art score and make no above-90 promise.
The next independent art review needs to view the actual generated revision and its exported runtime image against the traced model evidence, then check the scene crop in game.
The first route test should verify ordinary and dismissed paths, Narrator and Konomi speaker pages, solitary correspondence, missing-image behavior, image refresh, and readable picture placement while TTS is active.
This audit does not approve the whole route, static artwork that does not yet exist, or displayed UI that has not been observed.

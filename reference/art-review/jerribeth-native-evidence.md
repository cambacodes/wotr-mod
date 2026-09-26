# Jerribeth native portrait evidence

The installed game supplies a verified unit-linked **oolioddroo initiative portrait** for Jerribeth.
It differs materially from the custom-reference design used for `Jerribeth-v1.png`.
The existing illustration is a customized true-form interpretation, not a verified match to the native raster and not a human or elven guise.

I extracted the native texture without resizing, retouching or compositing, using the existing UnityPy 1.25.3 environment.
I visually inspected that extraction alongside the existing generated v1.
Only this report and files under `reference/art-review/jerribeth-native/` were written.
No generated art, story source or installed game asset was changed.

## Verified chain

| Native unit | Unit GUID | Portrait |
| --- | --- | --- |
| `Units/NPC/Unique/Act_3_DemonsHerecy/Wintersun/Jerribeth.jbp` | `417ce3dcf3a9707488f2b9b2a790814b` | `6f8d1a597cc64337a2fbb83b0d986768` |
| `Units/NPC/Unique/Act_3_DemonsHerecy/Wintersun/Jerribeth_Wintersun.jbp` | `fc8d7d07d716bee4499c9d17f6c43196` | Same |
| `Units/NPC/Unique/Act_3_DemonsHerecy/IvorySanctum/Jerribeth_Sanctum.jbp` | `bb9fe2c12d6941a43bfd5d5090ac97b9` | Same |

The portrait blueprint is `Units/Portraits/InitiativeBlueprintPortraits/Monsters/Oolioddroo.jbp`.
Its portrait, half-length and full-length image fields all reference asset `d890d7d79ef9f9f4d80dbf968ec0c220`.
It marks `InitiativePortrait: true`.
Those three fields therefore do not imply three distinct native sizes or a full-body illustration.
All inspected unit variants also use prefab asset `f8acb79bcccd0fb4a93db8e50a0d7c82` and specify female gender.

The `portraits` bundle resolves that image asset to Texture2D path ID `-465410453185449822`, named `Oolioddroo`, measuring **188 by 244 pixels**.
The same asset identifier also has a Sprite representation in the bundle.
The extracted file is [Jerribeth-unit-linked-oolioddroo.png](jerribeth-native/Jerribeth-unit-linked-oolioddroo.png).
Its SHA256 is `E3F1FAA73D2915D4B811F8C5A1D279951468C054C800DA6933C28CC9E0EE9555`.
The bundle SHA256 is `96675554F6E7865D69530950486CDF42C1F28CC8C37DF473F855F123AEDC045D`.

[provenance.json](jerribeth-native/provenance.json) records the installed bundle location, IDs, dimensions and extraction method.
The four exact source blueprints were copied into the same research directory from the installed `blueprints.zip`.
This is native reference evidence, not permission to relabel or ship the extracted image as newly generated artwork.

## What the native image actually shows

The portrait shows a narrow insectile head with very large luminous pale cyan eyes, dark eye surrounds and a pale gray-to-lilac face.
A swept-up turquoise or pale teal crest rises above the forehead and continues in shorter tufts beside the lower head and neck.
The forehead is relatively smooth and tapered compared with v1's heavy ornamental ridges.
A long reddish tongue or proboscis projects prominently from the small central mouth region.
Dark lateral pointed appendages and narrow reddish structures rise behind the head; parts are clipped by the portrait boundary.
A portion of a veined wing is visible at the side.

The crop cannot establish the complete arrangement or length of every head appendage, the full number of wings, exact body proportions, clothing or hand anatomy.
Do not use the small crop to certify details it does not show.
The linked generic species portrait supplies real native facial evidence even though it is not a bespoke painted Jerribeth illustration.

## Comparison with the existing generated illustration

`art/expansion/originals/Jerribeth-v1.png` preserves a nonhuman narrow face, luminous eyes, tongue, wings and linked fine hands.
It is recognizably intended as her demonic form, and its private-room staging suits the authored correspondence atmosphere.
These broad correspondences do not make its specific design native-faithful.

The v1 has dark, heavily ridged chitin across the forehead, emerald-green eyes, long dark flowing hair and elaborate elongated lateral horn structures.
The native face is paler, the eyes much lighter and proportionally larger, and the upright teal crest is one of its clearest distinguishing features.
V1 replaces that crest with dark hair and a sculpted headplate.
Its elaborate gown and full wing display are authored design choices, not details established by the initiative portrait.

The prior art record accurately says its source was an installed custom portrait and did not score canonical raster fidelity.
This extraction resolves that missing reference question; it does not retroactively change the earlier custom-likeness score into a canon score.
The image could be retained as an explicitly labeled alternate design, but it should not be described as indistinguishable from the installed native appearance.

For a native-anchored true-form revision, prioritize:

- The pale gray/lilac face and very large pale cyan eyes with dark surrounds.
- The distinctive upward teal crest and shorter side tufts instead of long dark human-like hair.
- The narrow insectile facial proportions and prominent reddish tongue/proboscis.
- Conservative extrapolation of cropped appendages, with further prefab/model inspection before prescribing a complete horn or wing arrangement.
- Adult dangerous intelligence through expression and gesture, without turning her into a human woman with decorative horns.

The last point is consistent with her native dialogue and the route's oolioddroo identity; it does not require exaggerating every monstrous feature beyond the actual reference.
The working hands and clothing can remain authored, provided they are not represented as verified native costume.

## Human or elven guise evidence

I searched the installed unit and portrait paths for Jerribeth and inspected the matching units' portrait fields.
All three named unit variants found use the same oolioddroo portrait and prefab.
The portraits bundle search found the linked Oolioddroo texture; it did not reveal a separately named Jerribeth human or elven portrait.
This is a scoped negative result, not proof that no differently named model or visual effect exists anywhere in the game.

I also inspected non-null speaker-portrait overrides in the relevant Jerribeth/Wintersun world data to avoid attributing another speaker's image to her.
`JerribethReveal/Cue_0071`, GUID `e736f10272d6a2441ac83c62a2878d5d`, uses override `ea8034769ab7d584e97b5227cbc03296`.
Its source comment identifies Finnean, and the localized line condemns Jerribeth for what happened to his kinsmen and neighbors.
It is an interjection, not evidence for her alternate appearance.
The cue is retained as [JerribethReveal-Cue_0071.jbp](jerribeth-native/JerribethReveal-Cue_0071.jbp) to make that attribution exclusion reviewable.

The route's current elven guise is explicitly invented and chosen for a private evening, with a visible shimmer.
A future `Jerribeth-Guise` illustration can follow that authored description, but should be labeled accordingly rather than marketed as an extracted native human guise.
No verified separate native guise raster was found in this inspection.

## Remaining visual verification

A native-anchored revision needs its own independent art review after generation.
Further model inspection would improve confidence about full-body anatomy and appendages beyond the small portrait's edges.
True-form and authored-guise assets should be distinguishable and used on the correct story pages.
Runtime crops and installed dialogue presentation remain separate work.
This research supplies references and fidelity requirements; it does not approve any production image or a complete art set.

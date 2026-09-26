# Soana v3 independent art review

Keep v2 as the preferred complete scene source for now.
V3 improves the broad facial proportions and distributes painted texture across more of the image, but it loses some of v2's convincing elderly anatomy and cuts off the pot despite the explicit framing instruction.
Neither version meets the requested above-90 standard in every observable discipline.

I visually inspected v3, v2 and the unit-linked native portrait, read the actual v3 prompt, and checked the `water_carrier` scene in `storylines/soana_opening.py`.
The reviewed v3 SHA256 is `6CA8D4E6CB322F55BCFDC326D7F9D8E52799B3FBD45C3BD785B9315C24C96649`.
The native reference is the 184 by 244 extracted Soana portrait documented in `soana-native/provenance.json`.
Only this report was written.
These are source-image assessments, not runtime crop or installed presentation approvals.

| Observable discipline | V2 | V3 | Assessment |
| --- | ---: | ---: | --- |
| Native likeness | 87 | 90 | Broader cheeks and a shorter, rounder facial impression improve the relationship to the native portrait; silver hair, blue markings and brown gaze remain recognizable. |
| Elderly age fidelity | 92 | 81 | V3 retains some eye and neck creasing, but smooths the forehead, lower cheeks and mouth into a younger face. |
| Dwarf species fidelity | 84 | 89 | Broad shoulders, substantial hands and a larger head in the composition work better; the tighter crop cannot establish overall stature. |
| Anatomy and prop construction | 90 | 89 | Both hands read plausibly, but the reed's insertion remains obscured and the unseen lower vessel prevents a complete construction check. |
| Painterly game consistency | 88 | 89 | Painted facets now cover hands, face and pot; uniformly angular surface marks compete with form and the eyes and hair remain sharper than the native treatment. |
| Composition and crop potential | 91 | 83 | The larger face helps portrait use, but the vessel runs through the bottom and right edges, defeating the requested complete activity composition. |
| Specific story fit | 91 | 86 | Practical clothing, woodland cave and repair work fit; age regression weakens the written characterization and the repair is still not fully legible. |

Scores describe the inspected images and are editorial judgments, not measured probabilities.
No aggregate average overrides an unresolved age or composition defect.

## What improved

The facial silhouette is closer to the native reference.
V2 has a longer midface and a more projecting nose; v3 brings the cheeks outward and the face into a broader, sturdier shape.
The distinctive markings still identify the same character, and the attentive sideways gaze suits her reserved manner.
The small native raster cannot establish fine wrinkles, but it does support these broad facial proportions.

The close framing removes the long foreground boot and thigh that made v2's dwarf stature ambiguous.
Her shoulders, head and working hands now carry the composition.
This helps the impression of a compact build without requiring exaggerated features.
It does not prove short limbs because the lower body is largely outside the frame.

V3 also extends visible painted marks onto the hands and face instead of concentrating them in the background and clothing.
The pot has less photographic smoothness.
The palette, practical fur-edged clothes and forest light remain suitable for the existing scene.

## Regressions and remaining defects

The prompt explicitly asked to retain the successful elderly age and all age detail.
The result does not retain them to the same degree.
Compared directly with v2, the forehead has fewer structural wrinkles, the cheek beside the mouth is fuller and smoother, and the lips and jaw have less surrounding age detail.
Painted color patches cover those surfaces, but patches are not a substitute for folds, sagging tissue and creases that follow facial anatomy.
V3 reads as a weathered older adult more readily than the clearly elderly woman in v2.
The wrinkled hands and white hair do not fully resolve that discrepancy.
The story itself refers to her wrinkled lips, which v2 conveys more convincingly.

The prompt also asked for the complete clay pot in its wicker cradle and framing to just below the carrier.
V3 cuts through the pot and cradle at the lower edge and clips their right side.
This is visible in the source image before any runtime cropping.
It is not fixable by cropping the existing image more tightly.
V2 retains the complete vessel and more of the working surroundings, making it the stronger current source for the carrier scene.

The repair is plausible but still ambiguous.
The lower hand grips pale reed lengths near the left handle attachment, and one strand runs toward the upper weave.
The fingers and intersecting strips hide the decisive over-under insertion.
The picture does not clearly show one unobscured new reed entering the requested crossing or a repaired section distinct from the old handle.
This is a clarity problem rather than an obvious impossible-hand defect.
No extra finger or broken wrist is apparent in the inspected image.

Some of the new surface treatment resembles a uniform layer of angular chips across skin and pottery.
That supplies texture, but the strokes do not always describe the underlying form.
The eyes retain a glossy precision and the hair still has many fine individual strands.
The overall result is more consistently textured, with only a modest improvement in game-like painterly handling.
The native reference is too small to support a strict full-resolution brushwork match.

The scene describes shared work with the Commander holding the cradle or working the reed under Soana's guidance.
A solo image can plausibly show her preparation or part of the lesson; it should not be treated as a literal illustration of every branch's hand placement.
The absent awl and water dish in this tighter view are not themselves continuity errors.

## Recommended next edit

Use v2 as the revision base because it preserves the stronger elderly face and complete vessel.
Use v3 only as a secondary reference for the broader facial shape and stronger upper-body proportions.
Retain v2's forehead, eye, mouth and neck age structure while broadening the midface modestly.
Reframe only enough to remove the long boot, retaining visible space beneath and to the right of the entire carrier.
Show one pale repair reed passing through an exposed crossing beside the fingers.
Apply selective brushwork that follows facial planes and hand joints rather than adding uniform surface texture.

If a portrait alone is needed, v3 provides useful face scale, but the age defect still needs correction before accepting it as the preferred Soana portrait.
Actual runtime face crops and a separate scene view remain unproduced and unverified in this review.
Their reduction, dialogue placement and installed appearance require inspection after the source revision is accepted.

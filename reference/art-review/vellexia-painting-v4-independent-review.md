# Vellexia changed painting v4 independent review

Reviewed 2026-09-27 by direct inspection of the delivered Changed-v4 image at original resolution.
I read the cup-repair prompt record and compared the delivered result with the previously inspected Day-v2, Changed-v2 and intact-cup Changed-v1.
I authored none of these images.
Only this report was edited.

## Verdict

Changed-v4 fails the whole-cup requirement.
Do not approve the proposed Day-v2 and Changed-v4 pair for staging.
The image preserves the improved fabric and recognizable character, but the repaired cup still reads as damaged at the exact location of the original chip.
Repeated generation attempts and a correct prompt do not establish that the delivered object meets the requirement.

## Evidence

| Candidate | SHA256 |
| --- | --- |
| art/candidates/VellexiaPaintingChanged-v4.png | `4E90392CD2AF89D371FC08B71ABAF5A8E26F9613B2168764AC0EB75B6B0C8776` |
| Intended paired art/candidates/VellexiaPaintingDay-v2.png | `4074EF5BF78192FCBF0780F060CBC9AB0A7049F94394DEE8BD05F27EEAFCEAA7` |

The v4 hash was verified locally.
The unchanged Day-v2 hash and its successful scoped review are recorded in `vellexia-painting-v2-independent-review.md`.
The inspected v4 canvas is 1536 x 1024.
The prompt record is `art/candidates/VellexiaPainting-cup-repair-prompts.md`.
Its statement that the donor cup is whole describes the requested operation, not proof that the new image copied that geometry.

## Cup finding

The prominent pale fill of the old chip is largely darkened in v4.
However, a downward V-shaped boundary and depressed triangular section remain at the front lip, approximately x1137-1158 and y749-764.
The front rim still reads as dipping into that damaged section rather than presenting the uninterrupted rounded pottery band seen in the intact v1 donor.
The rear arc of the opening remains smooth, but a smooth rear arc does not repair the front edge.
This is not a convincing reconstruction of missing pottery.
At best it is an ambiguous brown repair mark in the exact shape and position of the original notch.

The scene requires an unmistakably whole cup because `vellexia.unfinished_likeness/picture_changed` explicitly announces that fact.
The shape retained here would make the player reasonably question whether the depicted chip actually disappeared.
That fails the story clue even if the dark triangular region were intended as harmless ceramic shading.
The recommendation is a genuine continuous front lip with coherent thickness and a smooth exterior rim band, not another recoloring of the same V-shaped region.
Retain the cup's size, position, material and general silhouette so it remains the same vessel.

## Preserved successes

Her attractive adult face, blond high knot, red eyes, pointed ear and ridged horns remain recognizable.
The changed expression remains faintly impatient rather than smiling or furious.
The dark overcast sky is retained.
Hand placement, body angle, dress cut, frame and ordinary-room objects remain consistent with the intended pair.
No new anatomy defect or forced Commander depiction is visible.

The white garment still reads as the fine lightweight fabric established in Day-v2.
Both sleeves retain soft diffuse transmission with denser gathered cuffs and overlapping cloth.
The bodice and skirt share that surface character while the bodice gathers and waist compression produce heavier overlaps.
The darkened scene reduces the daylight glow without converting the dress into opaque canvas.
The ties, visible folds, supported dropped sleeve and hand-to-table contact remain plausible.
The donor's thicker v1 fabric was not visibly substituted for the revised dress.
Small regenerated surface variations do not create a consequential outfit or pose change.

The full native body and bust remain unknown because the available native reference shows only the head and collar.
The white dress and painted ordinary room remain authored scene choices.
This review makes no new native-model claim.

## Scores

These judgments concern delivered pixels, not the success rate of the generation process.
Every applicable criterion must exceed 90.

| Criterion | Changed-v4 |
| --- | --- |
| Clearly adult conventional attractiveness | 95 |
| Supported native head and racial identity | 95 |
| Visible anatomy and hands | 94 |
| Faint-impatience expression | 94 |
| Darkened-sky state | 96 |
| Convincingly whole cup with restored rim geometry | 65, fail |
| Distinct scene wardrobe and setting construction | 95 |
| Material differentiation | 95 |
| Same lightweight weave across sleeves, bodice and skirt | 94 |
| Light transmission, opacity and dense overlaps | 94 |
| Drape, support and physical contact | 94 |
| Pair identity, pose and wardrobe continuity | 94 |
| Painterly finish and composition | 94 |
| Exact changed-page narrated state | 75, fail |
| Native full-body and bust fidelity | Unknown |
| Runtime display and clue legibility | Untested |

The material and identity scores do not override the failed cup state.
Retain v4 as iteration history and keep it unassigned pending a successful repair.
No source, image, staged file, export or installed asset was changed.

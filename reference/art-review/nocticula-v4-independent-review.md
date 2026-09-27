# Nocticula v4 independent art review

Reviewed 2026-09-27 against the latest character-design brief.
I viewed the delivered v4 and the extracted native portrait directly, read the v4 prompt, and compared the result with the v3 image inspected during the roster reassessment.
I did not generate or edit these images.
The unslop writing guidance applies to this report.

V4 passes this independent source-image review.
It resolves the substantial costume drift that I scored below the gate in v3.
This approval covers the visible candidate, not a particular dialogue page, runtime crop, installed portrait or complete route.

| Artifact | SHA-256 read from file |
| --- | --- |
| `art/candidates/Nocticula-v4.png` | `F706CC5A6AC919697BF5FFF781715A0AF516BBFF4480564B4F26C8B05602DDDF` |
| `reference/art-review/nocticula-native/NocticulaFemaleDemonlord.png` | `096F66A4715AC49302022D979FAAD7788E8EE416004BF53D3CA2D7546338E778` |

## Visible findings

The continuous dark breastplate is gone.
Separate pointed ornaments now cover the breasts, with narrow chains connecting them and leaving the upper chest, ribs and abdomen exposed.
The large central armor scrollwork has become a small hanging ornament.
The arms now carry separate open ornaments and narrower bracers rather than solid gauntlets.
These are material changes in the delivered picture, not merely changes requested in the prompt.

The native portrait's crossed hands and raised knee obscure much of the chest and lower costume.
It supports the sparse ornamental construction, exposed skin and dark markings, but cannot establish an exact frontal pattern or numeric bust dimensions.
V4 is a recognizable costume interpretation, not an exact model reproduction.
The angular breast ornaments remain more elaborate than the clearly visible native pieces, and the arm metalwork still has more layered detail.
Those differences no longer create the heavy armored torso that caused the v3 failure.

Her adult face remains conventionally attractive, composed and faintly contemptuous.
The lifted chin and appraising eyes suit a dangerous ruler without making her uniformly agreeable.
Lilac skin, pale luminous eyes, pointed ears, broad dark horns, black hair, wings, gold ornament and sweeping markings maintain recognition.
The hair remains longer and less geometrically straight than the native portrait, and the bright violet eye glow differs from its quieter pale eyes.
The markings echo the native chest and arm pattern without duplicating every line.

The visible arms, shoulders, neck and torso connect plausibly.
The hands remain distinguishable where they overlap on the book, with believable finger bends and no obvious duplicated digits.
The wings extend behind her, but their attachment and full anatomy are hidden.
The lower body and feet are outside this assessment.

## Independent scores

These are editorial judgments of this exact delivered revision, not measured probabilities or inherited scores.
Each scored dimension exceeds 90 independently.

| Dimension | Score / 100 | Evidence and deduction |
| --- | ---: | --- |
| Native costume fidelity | 93 | Sparse ornaments, fine chains, exposed torso and separate arm pieces restore the native design direction; ornate metalwork is still an interpretation. |
| Native sensuality and silhouette | 94 | The image preserves revealing costume and adult form without added modesty; native pose prevents exact frontal proportion comparison. |
| Conventional adult attractiveness | 95 | Balanced facial planes, expressive mouth and assured bearing remain appealing and clearly mature. |
| Recognizable identity | 94 | Skin, eyes, horns, ears, wings, hair and markings form a strong likeness; hair shape and eye glow differ. |
| Visible anatomy | 93 | Coherent hands, arms and torso; hidden wing joints and lower body limit scope. |
| Painterly game consistency | 92 | Painted facets and controlled light unify skin, stone and wings; skin and metal remain more polished than the native portrait. |
| Full-image composition | 91 | Face remains dominant, hands and book read clearly; broad horns approach the side boundaries and restrict alternative crops. |
| General character-vignette suitability | 93 | Her composed posture supports a ruler assessing an interlocutor without presupposing affection or redemption; harbor and book are authored staging. |

## Assignment limits and next verification

The balcony overlooks a harbor under a visible moon, with sailing vessels and a book on the table.
Those details must fit an actual page before this image is treated as a literal scene illustration.
I additionally read the proposed assignments in `storylines/nocticula_continuation.py` and searched its balcony, book and table references.
None of the suggested pages earns a literal assignment for this image.
`unlit_quay/later` creates a dream balcony with city lights, but Nocticula places a flower-bearing cloth on the balustrade and turns toward the Commander.
The painting omits that cloth and substitutes a seated reading-table pose with a large closed book.
The dream itself does not forbid illustration, but its specified action and props do not match this picture.
`lamp_measure/start` occurs indoors under a low ceiling, with no furniture except an enormous balance and a loading book represented by floating columns.
`lamp_measure/bait` closes an imaginary loading book in that same room; sharing the word book does not make the harbor balcony appropriate.
The nearby `her_own_face` scene explicitly has no harbor and places her on a couch in a dark chamber, so its book also supplies no match.
For a literal `unlit_quay/later` illustration, a variant should show the narrow balcony, flower-bearing cloth on the rail and attention turned toward an off-frame Commander, without the reading table and book.
A separate indoor variant would be required for the balance-and-columns investigation.
The picture is not a universal illustration of every audience, ascension state, letter or private encounter.
If used as a general identity vignette, make that distinction explicit in the assignment record rather than claiming exact scene correspondence.

Keep v3 and earlier candidates available as alternate costumes.
V4 should replace v3 as the preferred native-costume candidate, subject to source-page and presentation checks.
Do not add a selector merely to expose the revisions; existing per-page portrait keys already support narrative changes.

Before staging or broad replacement, review every affected source page, produce any required crop, inspect horn clearance and face readability at display size, and verify the packaged filename and key.
Unity loading, actual image transitions and in-game layout remain unverified.
No image, source assignment or staged asset was changed by this reviewer.

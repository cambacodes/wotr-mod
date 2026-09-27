# Vellexia v1 independent candidate review

Reviewed 2026-09-27 under the current character-design requirements.
I directly viewed the candidate and all four extracted native default/date images, read their retained provenance, and inspected actual opening and campaign source pages.
I did not author the candidate and did not inherit another reviewer's approval.
Only this report was edited.

## Verdict

V1 passes the applicable static criteria as a close default-state speaker portrait.
It is suitable for the living initial-manor interlude, with proposed assignments limited here to `vellexia.unfinished_likeness/start`, `/jerribeth` and `/terms`.
This is not a full-body design approval, a replacement for all three date costumes, or a scene illustration of the enchanted painting.
The image remains unstaged at inspection and runtime presentation remains unverified.

## Evidence and hashes

| Inspected file | SHA256 |
| --- | --- |
| art/candidates/Vellexia-v1.png | `9AB756D627479508C414CBAF3BD8940142F42BFBBF98F0082B1B1963B11D77D3` |
| art/candidates/Vellexia-v1-prompt.md | `715A1D58A7AD4770E5A00450D2EC344AB49578C7E4499AE57D549ACEC70557BB` |
| storylines/vellexia_opening.py | `A48E7BC9EF3DA412D88EE2FCD6C1E408E8C7CC82E96DD340C8F38A91D3E62F2D` |
| storylines/vellexia_campaign.py | `24AE43736DD2C967E9E3D5BB8CCAA83816FB54D75C02C766246F53E43F5C1C99` |
| reference/art-review/roster-native/VellexiaDefault-m_FullLengthImage.png | `95D6EABA9697F3BC9DF1335684CA877A278184DF27837F1167D37EE1E1F6785A` |
| reference/art-review/roster-native/VellexiaFirstDate-m_FullLengthImage.png | `2AE760BF5A7DF8B68D841CEB93769F4AC9BF00E08BFA73DA1DF903FC57C2FD0A` |
| reference/art-review/roster-native/VellexiaSecondDate-m_FullLengthImage.png | `AAE9A8F14706E2896CF9FED0F024CF06575A9A442A817F6343E9E160A20F3012` |
| reference/art-review/roster-native/VellexiaThirdDate-m_FullLengthImage.png | `A1241D4D84679935D7F4F3FB362DC022DC438DA2422B33F281E9B49454C5A38D` |

The candidate is 1089 x 1444 pixels.
Despite their `m_FullLengthImage` filenames, all four native references are 184 x 244 head-and-shoulders textures.
The provenance records the portrait, half and full fields reusing each state's same asset.
They cannot certify full costume, breast volume, body proportions, hands or legs.
The local checks used actual SHA256 and PNG header dimensions, not filename assumptions.

The default actor is `a32a07903e428d34cb0e98a804d40569`, linked to portrait `80c75669b440437dbaf764df98221832` and prefab `d873f91c8090bd446a5e896fd5c2a077`.
The first-date actor is `eaa50c021f75d7f45a17534ea2f94985`, linked to portrait `6e708ec20c4c42e294d3e0bd1ecad049`.
The second-date actor is `6c232576d377ff145b1c2c1cb9500824`, linked to portrait `730a42d892a2424abbdba71c48858ba3`.
The third-date actor is `a1d1aec8665002246a6aab9842f64f53`, linked to portrait `6c64ba085b224b06b598fd600b6f5254`.
These chains are recorded in `roster-native/provenance.json`.
The default actor's texture name contains `FirstDateCostume`, while the first-date actor's texture name contains `DefaultCostume`.
I followed the actor links and inspected pixels rather than swapping the two states based on those confusing texture names.
No model render or fresh bundle extraction was performed here.

## Visual findings

The candidate preserves an immediately recognizable combination of pale warm skin, red eyes, dark red lips, sharply defined brows, pointed ear, tall ridged horns, sculpted blond hairline and a high blond knot.
The native head shape is refined into a conventionally attractive adult face with coherent eyes, nose and mouth.
Subtle skin texture and cheek shading add life without making her elderly, jagged or childlike.
Her composed, appraising gaze and restrained smile retain danger and self-possession rather than making her look innocently agreeable.
The horns remain substantial and nonhuman.
Their curvature and surface detail are an attractive painted interpretation of the low-resolution reference, not a claim of identical mesh geometry.

The green-and-gold outer collar, red throat area and dark blue shoulder sliver follow the default actor's visible palette and clothing arrangement.
The candidate adds legible textile detail and a central red ornament whose exact construction is not established by the thumbnail.
That elaboration is minor and coherent within the visible design, but should not be marketed as extracted native jewelry.
The high neckline is supported by this specific native reference.
It is not an arbitrary attempt to cover a revealing native costume.
No breast or cleavage area is visible, so the portrait neither establishes nor visibly contradicts bust size.
There is no basis here for a claim that her bust has been reduced.

The first-date reference has a darker shoulder and collar treatment, the second has an ornate forehead band and differently embroidered collar, and the third has a red outer garment with different visible throat details.
V1 follows the default look and does not reproduce these distinct date states.
In particular, its lack of the second-date forehead ornament should not be approved as that costume merely because the face is recognizable.

Facial anatomy, horn placement and visible ear are coherent.
No hands, wings or lower body are depicted and no anatomy score is inferred for them.
The painterly face and warm interior lighting fit the intended CRPG portrait style, although the lighting and background are authored.
The crop is tight: the highest horn and hair are close to the top edge but remain inside the delivered image.
That is acceptable for this head portrait, with less tolerance for additional UI cropping than a looser composition would have.
Preserve the whole image when checking display rather than assuming a center crop is safe.

## Scores

These are independent editorial judgments of the actual candidate, not inherited scores or measured probabilities.
Every applicable scored dimension exceeds 90.

| Dimension | Score or status |
| --- | --- |
| Clearly adult conventional facial attractiveness | 95 |
| Recognizable native face and palette | 95 |
| Horns, hair, ear and other visible racial cues | 95 |
| Appraising character-specific expression | 94 |
| Visible default collar/clothing fidelity | 93 |
| Visible exposed-skin/coverage fidelity | 95 |
| Facial and visible head anatomy | 95 |
| Painterly finish and game-art consistency | 94 |
| Composition and edge clearance | 91 |
| Proposed default-manor speaker-page continuity | 94 |
| Full costume, bust and body fidelity | Unverified, not depicted in either usable frame |
| Native date-state replacement | Not approved |
| Runtime image loading, scaling and clipping | Unverified |

Unknown full-body evidence is not converted into a passing score.
The scope is a default head portrait, so this limitation does not invalidate its narrower approved use.

## Page suitability and exclusions

The opening uses the living default actor in her manor before the Battlebliss invitation.
Its helper requires her greeting and blocks death, fights, the arena invitation, the completed native quest and route closure.
That is the right narrative window for this default portrait.
The proposed `unfinished_likeness/start` page introduces the bracelet and backward picture; neither needs to appear in a close speaker portrait.
The `/jerribeth` and `/terms` pages contain the amused, dangerous conversation that suits the candidate's expression.
These are approvals as a portrait of the speaking Vellexia, not as literal depictions of every hand movement in their narration.

Do not present it as the image described by `/picture`.
That page explicitly describes an enchanted painted woman in a white dress with a sleeve slipped to her elbow, in an ordinary room with a changing cup and sky.
V1 depicts neither that costume nor that magical picture state.
The source currently sets every opening page's Portrait to Vellexia; a globally staged file would therefore reach `/picture` as well as the approved speaker pages.
That broad effect has not been approved by this scoped review.
Use explicit appropriate page art or clearly distinguish speaker-portrait presentation from the painting before extending the assignment.

The later campaign also assigns Vellexia broadly, including remote correspondence after peaceful dismissal.
A neutral head portrait may be useful there, but this review did not prove the costume or image-versus-voice state of every campaign page.
Do not treat a source helper's shared key as evidence that all those pages have been reviewed.
The original native dates retain their distinct appearances and are outside the proposed default portrait use.
`art/CustomNpcPortraits/RanRomance-Tirabade/Scenes/Vellexia.png` was absent at inspection.
The candidate's existence therefore establishes neither exported-key coverage nor installed delivery.
No image, assignment or installed file was changed, and no game was launched.

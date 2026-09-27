# Konomi private-evening sequence variety audit

The staged set fails the new sequence-level variety requirement.
It preserves an attractive, recognizable adult redesign and a coherent gown, but repeats almost the same face direction, head lean, eye contact and small closed-mouth smile across three compositions.
Standing, sitting and cropping closer are visible changes; they do not yet express the scene's changes in feeling and action.
Prior individual-image passes do not approve this sequence under the new requirement.

## Directly inspected evidence

I viewed all three actual staged files and compared them against every current `before_road` page.
Only this report was edited.

| Staged file under `art/CustomNpcPortraits/RanRomance-Tirabade/Scenes/` | SHA256 |
| --- | --- |
| `KonomiPrivateEvening.png` | `FFA19D95FFB15CA81EBDA953E14E543BAC0D44847F69E99EDD9DED5D673E8B2C` |
| `KonomiPrivateSeated.png` | `12560274FDE2B08548136F3471A5ACD974DA6245D2DD1D3F2C37AEB1F2C675EF` |
| `KonomiPrivateClose.png` | `5D605330C541FC3A39A671E0ADB7786CBE6F9FBD1D6203A9CF96CD8091C9D504` |

Inspected source `storylines/konomi_private.py` has SHA256 `E61C564D09F89349EEDC71A414CD45AB3E7EDFE3EA314622C186E368C0058D91`.
I read the current character-design requirements for distinct outfits, material behavior, sensuality and actual-page continuity.
This audit evaluates the mod's automatic illustrated-page sequence.
It does not claim that Owlcat uses this mod's scene-image system or that these authored room illustrations are native artwork.
The humanized face and private gown remain authored designs; exact native humanoid bust and full-body proportions are not established by the retained cropped/native texture evidence.

## What repeats and what remains useful

All three place her face toward the viewer with a screen-right lean, similar lowered chin, direct amber-eyed attention and a restrained smile.
The braid, loose curls, shoulder orientation and neckline create almost the same central silhouette, especially between the seated and close images.
The close image removes the hands and most of the chair, so it also removes the most useful means of showing changed intention.
Its larger face does not provide a new expression.
This is a sequence-level repetition problem, not a claim that the files are literally identical crops.

Retain the arrival as the first visual anchor.
Her hand on the door latch and standing skirt are meaningful actions for `start`, where she shuts the door after interrupting her packing.
The room, case and welcoming attention establish the visit clearly.
It need not be regenerated simply because later images copied its expression.

Retain the seated image for `departure/company` and the quiet `histories` transition.
It establishes that she has sat down and makes the private gown's seated drape visible.
The partially cropped companion chair avoids declaring a clearly visible occupied seat empty.
This composition is a useful baseline before closer interaction, rather than a complete illustration of every later gesture.

Redesign the close image before treating the sequence as settled.
Its current assignments are `lovers`, `talk`, `letters` and `others`.
Those passages concern unresolved anger, chosen company, distance, reliable invitations and another relationship's place in the Commander's life.
One steady flirtatious smile cannot carry all of them as an exact emotional illustration.
Keep the file as a retained alternate, not the final answer to those scenes.

## Specific next compositions

| Scope | Distinct target and exact limits |
| --- | --- |
| `lovers` | Seated three-quarter side view, head upright, chin slightly lowered toward the near chair arm, mouth relaxed without a smile, affection present beneath a firm and searching expression. Show her hand placed on the near edge of her own chair arm, with the Commander's position outside frame. This can accompany her admitted anger and wanted company without pretending the player already took her hand. |
| `new` | A small spontaneous laugh that breaks her composed posture: shoulders turn toward the visitor, head upright or briefly tipped back, eyes bright and mouth visibly smiling. Keep her seated and self-possessed, not giggling like a different personality. The current seated portrait can remain a temporary speaker image, but it does not show this change. |
| `near` | A lower, wider seated composition from her open side. One hand grips her own chair to shift it, shoulders lean forward with the effort, gaze briefly drops toward the rug, and a short laugh has replaced the irritated glance. Include the chair leg at the rug edge if choosing the interrupted-movement instant. Do not show a kiss or assume it will be selected. The Commander and contact can remain outside frame. |
| `kiss` | Intimate seated eye-level close view just after she draws back, face upright and slightly in profile, eyes returning to the visitor and lips softly parted as her usual ready remark fails her. Her upper arm can extend toward the near frame edge while the hand and customizable Commander stay out of frame. Make the forward posture and disrupted composure visibly different from the current tilted smile. Keep it an implied post-kiss image, not a claim to depict invisible neck or collar contact. |
| `talk/letters/others` | Calm, attentive three-quarter dialogue portrait with upright neck, steadier brows, relaxed closed mouth and one natural speaking gesture near her own lap. Turn the torso toward the offscreen listener rather than presenting the same frontal pose. Convey practical resolve and interest together. These pages merge kiss and non-kiss paths, so avoid flushed aftermath, an embrace, mandatory touching or discarded clothes. |
| `finish` | Optional distinct closing image of her tending the lamp, half-turned in profile, eyes on the wick, with credible hand/tool placement and warm light on her face. This action is in the text and gives the evening a physical ending. A reviewed seated portrait may instead represent the moment after she returns to the chair, but should not be advertised as a new milestone illustration. |

Do not require all six targets before correcting the present sequence.
The immediate priorities are the two missing intimacy-stage images and a genuinely different later-dialogue portrait.
The source currently assigns neither private portrait to `near` or `kiss`, so both inherit the office `Konomi` key.
That is a concrete gown/location discontinuity at the moment of increased closeness.
Root should replace those assignments only after the new delivered candidates receive independent review.

## Identity, sensuality and physical construction

Keep the adult fox-human face, amber eyes, russet/cream markings, braided brown hair, ears and single pale-tipped tail consistent.
Changing camera angle must not replace her facial structure with a generic new woman.
Retain the attractive adult silhouette and the existing open wrap neckline; variety does not require extra coverage or an arbitrary increase in exposure.
Her attraction should become legible through chosen proximity, attention and momentary loss of verbal composure.
Her pride and ability to disagree should remain visible in the later conversation.

Keep the same aubergine gown, embroidery, sash and secure overlap throughout this uninterrupted visit.
The gown should change its folds with standing, leaning, turning and sitting, not preserve the same painted creases under a new face.
The chair-moving pose needs pressure at the gripping hand, sleeve compression at the elbow and skirt tension over bent hips.
The post-kiss lean needs different bodice and waist folds while retaining the same fabric and fastening.
Do not invent undressing, a loose bodice or an overnight aftermath absent from the selected text.
Warm lamp and cool dusk can continue across the set without freezing every highlight onto the same part of her face.

## Sequence judgment

| Criterion inspected across these three images | Score | Result |
| --- | ---: | --- |
| Consistent adult redesigned identity | 95 | Pass within the authored redesign, not proof of exact native facial geometry |
| Gown and room continuity | 93 | Pass for the broad sequence; this does not replace detailed material reviews |
| Meaningful body/action variety | 82 | Fail: standing latch action and seating differ, but close supplies no new action |
| Face, gaze and expression variety | 68 | Fail: the same tilted, faintly smiling attention dominates all three |
| Emotional progression against assigned pages | 77 | Fail: unresolved anger and practical negotiation lack a distinct visual response |
| Complete page-assignment continuity | 72 | Fail: `near/kiss` still inherit office art |

Approval requires greater than 90 in each applicable dimension, not an average that hides the failed criteria.
No new candidate is approved by these proposed compositions.
The replacement set must be viewed in actual page order, including kiss and non-kiss branches, and then checked at the game's displayed crop and size.
Keep automatic per-page changes; this failure calls for better scene art and assignments, not a clickable selector.

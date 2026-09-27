# Event illustrations for developed routes

The user wants selected important events illustrated in addition to ordinary portraits.
Use the existing per-page Portrait field and automatic image switching.
No new selector is required by these scenes.

## Selection

For a developed route, identify a few distinct moments that benefit from an illustration: a date, an earned romantic turning point, an important conflict or rescue, a private evening, and an ending where appropriate.
Select from the actual manuscript rather than imposing the same sequence or number on every character.
An intimate prelude or quiet aftermath can mark consummation without illustrating a sexual act.
Preserve the route's sensuality and the character's native revealing design where it belongs.
Wardrobe changes must follow the setting and character, with the same recognizable face and body design across images.
An authored private outfit must be labeled as authored in art records rather than presented as a native costume.
Do not preserve combat clothing merely to make a character recognizable.
Anevia's private scenes should not automatically retain her scarf, leather armor and bracers; choose credible civilian clothes and preserve her identity through her face, hair, palette and expression.
Scene-appropriate wardrobe is a hard acceptance gate, including for previously settled images.
Adventuring trousers do not exclude dresses, skirts, robes, sleepwear or underwear in suitable adult scenes.
Choose each outfit for the character, activity and selected relationship state, preserving the game's visual style rather than treating a single native costume as compulsory.
Construction must also fit the setting: plausible fabrics, tailoring and fastenings, without modern retail cuts, synthetic-looking materials or mass-produced details.
Judge refinement against the character's resources and culture; an elaborate noble or demonic outfit can be appropriate without becoming contemporary fashion.
All scene-art prompts and reviews must also apply the general fabric-physics rules in `CHARACTER-DESIGN.md`: material weight and weave, sheen and roughness, light transmission and layering, and pose-dependent drape, tension and contact.
These are generation requirements for every applicable image, not optional repair instructions for isolated revisions.
Source any race-specific physiology or clearly label it as authored; appearance alone does not establish heat cycles or loss of self-control.

## Immediate scene opportunities

| Character or group | Existing scene or page | Illustration need | Current state |
| --- | --- | --- | --- |
| Konomi | `before_road/start` in `konomi_private.py` | Standing arrival at the closed door, moved case and distinct evening gown. | Arrival v2 passed independent review and replaces the seated v3 under KonomiPrivateEvening; exact bytes and sole page reference verified; runtime crop pending. |
| Konomi | `before_road/departure`, `company`, `histories` | Seated private conversation in the matching gown; companion seat outside frame. | Private v4 passed scoped independent review and is staged as KonomiPrivateSeated; all other page fields unchanged; runtime pending. |
| Anevia and Irabeth | `three_yard/rules` | Outdoor wooden-ball game, lane and fence; poses and clothing consistent with the complete scene. | TogetherYard v2 passed independent static review and is assigned to this page only; export and runtime checks remain separate. |
| Anevia and Irabeth | `reckoning/start` | Serious conversation with Irabeth explicitly out of armor, both women facing the Commander. | Current armored affectionate Together image is wrong; separate scene illustration needed. |
| Anevia and Irabeth | `reckoning/truth` | Opposing seats during the painful disclosure, Anevia's eyes closed, Irabeth out of armor, Commander offscreen. | V4 replaces user-rejected v3 with a wine-red dress; fresh independent design/material/scene review passed and reviewed bytes are staged, runtime unverified. |
| Vellexia | `unfinished_likeness/picture` and `/picture_changed` | Enchanted white-dress painting changes expression, cup and sky while the viewer looks away. | Reviewed pair assigned to consecutive pages, preserving original prose and outcomes; actual-speaker portrait resumes afterward. Runtime readability unverified. |
| Nocticula | `noct.her_own_face/start` | Dark chamber, couch, one lamp, pale fruit and closed book; her own face and chosen private company. | V4 costume candidate is reviewed but wrong setting; attempted variant returned no image. |
| Areelu | Survey-station private choices | Distinguish a kiss, a nonphysical evening, departure and the selected overnight aftermath. | Manuscript and timing still under revision; do not assign a bed/overnight image to a shorter choice. |
| Devarra | Later relationship milestones | Preserve actual dragon form until a voluntary, credible humanoid transformation is written and implemented. | Humanoid v1 is a reviewed concept, not an available scene state. |

These are opportunities and requirements, not completed assets or approved storyboards.
The Tirabade corrections take priority over treating the existing shared image as a universal illustration.
Future completed routes receive equivalent scene-aware consideration, including convincingly developed female group relationships.

## Assignment rules

Record the exact scene and node, current clothing and physical form, visible participants, location, time and required relationship choices before generation.
Do not show a kiss, embrace, undressing or overnight aftermath before the player selects that development.
Early refusal, platonic contact and breakup pages need compatible images or a verified neutral presentation.
Avoid fixing the customizable Commander's face, race, body or hands in an otherwise universal illustration.
Prefer the partner looking toward an offscreen Commander, or create explicitly supported player variants if the scene needs the Commander visible.
Scenes with two women must preserve each woman's identity and the actually established mutual relationship.

Generate a versioned candidate, obtain independent design and assignment review, stage the approved file under its exact key, and check the exported page references.
Inspect actual game framing and transitions before claiming visual delivery complete.
An attractive image with the wrong action or wardrobe fails assignment even if its standalone art review passes.

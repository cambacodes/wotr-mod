# Roster art reassessment

Reviewed 2026-09-27 by an independent inventory and visual reviewer.
I did not generate, edit or stage the images reviewed here.
This report applies the latest `art/CHARACTER-DESIGN.md`, including original sensuality and costume, attractive adult humanization, and automatic dialogue-page image changes.
I used the writing guidance in the unslop skill.

## Evidence and scope

The current `ROSTER.md` names 37 characters.
Fifteen have at least one project-owned candidate in `art/`; 22 have no candidate there.
An existing native or RanRomance portrait may still be available for those 22, but this inventory does not establish its suitability for new scenes.
Twelve scene PNG files currently exist under `art/CustomNpcPortraits/RanRomance-Tirabade/Scenes/`, representing eleven women plus the shared Together image.
Candidate existence, staged files, reviewed assignments and installed runtime delivery are separate states.

The root's `exported-scene-art-audit.json` adds a separate, current export check using `tools/check-scene-art.py`.
Its recorded story SHA-256 is `866B7C66C2027AFEE471FD4C497F57CD173E2AE789814FB268FC5DA49A9249C2`.
The export requests 30 distinct runtime image keys; eleven resolve to staged PNG files and nineteen are missing.
These are runtime keys, not counts of roster characters with candidate art.
For example, ArsinoeShop and ChivarroWarm exist while the general Arsinoe and Chivarro keys are missing.
Gesmerha and Soana have scene-specific asset files but their general speaker keys are also missing.
Named incidental speakers contribute additional missing keys.
The current BookPatch selects one explicit portrait or speaker key; a differently named staged scene file is not an automatic fallback.
Do not solve those gaps by globally assigning a costume-specific image without reviewing all affected pages.
This audit inspects exported keys and PNG headers; it does not decode images or execute Unity.

I directly viewed Areelu v6 and the retained full official portrait, Nocticula v3 and the extracted native portrait, Chivarro v4, and Soana v12.
Other rows below report filesystem evidence and existing review limitations, not fresh visual scores.
No image or route receives runtime approval here.
The full official Areelu reference is two-dimensional artwork, not a measured native 3D model.

## Full roster inventory

Paths beginning with `originals/` in this table are under `art/expansion/`, unless the cell specifies `art/originals/`.
Scene keys refer to files in the Scenes directory above, not verified page assignments.
Suggested variants are future scene needs, not a requirement to invent scenes merely to consume artwork.

| Character | Current project art | Fidelity evidence and next art work |
| --- | --- | --- |
| Anevia | `art/originals/Anevia.png`; staged Anevia and NPC crop set; shared Together | Existing sources need fresh native-costume and silhouette comparison under the latest brief; separate ordinary, field and shared relationship moments as actual pages require. |
| Irabeth | `art/originals/Irabeth.png`; staged Irabeth and NPC crop set; shared Together | Recheck half-orc identity and practical native armor against source references; preserve adult facial appeal without erasing tusks or character; departure and recovery art remain unverified. |
| Seelah | `originals/Seelah-v1.png`, `Seelah-evening-v1.png`; no scene PNG | Two candidates exist; current native comparison and assignments still need review; distinguish armor and the authored evening outfit. |
| Konomi | `candidates/konomi/konomi-v2.png`, `konomi-private-v3.png`; staged Konomi and KonomiPrivateEvening | Existing private-v3 review supports a specific packing scene; native portrait is a placeholder and prefab/texture evidence has limits; public-office and private-lodging settings must remain distinct. |
| Jerribeth | `originals/Jerribeth-v4.png`; staged Jerribeth | Existing review supports humanized face, crest and wings; the elaborate gown needs fresh costume comparison under the latest request; true form and disguise cannot share an unconditional scene illustration. |
| Kiana | `originals/Kiana-v2.png`; no scene PNG | Native portrait reference exists; current candidate needs full latest-brief review and a source-page assignment; performance and changed wedding history require distinct continuity. |
| Vellexia | No candidate found | Obtain native portrait/model reference before generation; preserve her specific demonic silhouette and costume rather than inventing a generic aristocrat. |
| Arsinoe | `candidates/arsinoe/arsinoe-v1.png`; staged ArsinoeShop | Native reference and scoped shop review exist; a shop picture cannot cover all private relationship scenes; fresh silhouette/costume check remains needed. |
| Gesmerha | `candidates/gesmerha/gesmerha-v1.png`; staged GesmerhaWorkshop | Native reference and workshop review exist; preserve blindness and craft identity; new settings need page-specific art rather than silently curing her. |
| Minagho | `originals/Minagho-v2.png`; no scene PNG | Existing assignment review rejects global use because the absent brand is history-specific; obtain a correct-history assignment and variants where the mark remains; shared art with Chivarro is missing. |
| Chivarro | `originals/Chivarro-v4.png`; staged ChivarroWarm | Viewed v4 retains an appealing adult eyeless face and an attractive copper gown; this is authored dress art for one chosen branch, not proof of native default-costume fidelity; robe, dark dress and shared scenes need separate treatment. |
| Nocticula | `candidates/Nocticula-v3.png`; staged Nocticula | Direct comparison finds remaining substantial breastplate/costume drift; see the fresh finding below; preserve v3 as an alternate outfit while revising the native-costume candidate. |
| Nurah | `candidates/Nurah-v1.png`; no scene PNG | Existing review compared native costume and adult halfling proportions; staging and page-fit remain missing; future private scenes should retain her knowing expression rather than make her uniformly innocent. |
| Targona | `originals/Targona-v2.png`; staged TargonaCorrespondence | Existing review supports the paper activity and likeness but intentionally omits wing anatomy; new views must distinguish actual wing history; correspondence illustration does not establish physical presence. |
| Terendelev | No candidate found | Source both native dragon and humanoid references where available; distinguish restoration, ravener history and the chosen adult humanoid appearance; do not claim an invented form is canonical. |
| Aranka | No candidate found | Source native appearance and performance clothing; portrait and route-specific performance/private scenes remain missing. |
| Arueshalae | No addon candidate found | Integrate existing portrait ownership; distinguish redeemed and corrupted histories, costume and expression before commissioning scene variants. |
| Camellia | No addon candidate found | Integrate native portrait; preserve recognizable dress, jewelry and controlled demeanor; route revelations need scene-aware expression and setting. |
| Wenduag | No addon candidate found | Integrate native portrait; humanization must preserve recognizably nonhuman traits and original revealing costume; group art requires authored mutual attraction and matching route state. |
| Galfrey | No addon candidate found | Integrate native portrait and verify supported appearances before adding duty/private variants; don't confuse authored rejuvenation with biography changes. |
| Soana | `originals/Soana-v12.png`; staged SoanaForest | Viewed face is softly modeled and conventionally attractive with silver hair and blue markings; substantial dwarf build remains; no fresh native comparison score here; exact basket-repair illustration remains unproven. |
| Areelu | `candidates/Areelu-v6.png`; v1-v5 retained; no scene PNG | Fresh independent candidate assessment below; native costume cues and requested fuller bust are present; physical study setting and fixed Commander appearance prevent broad assignment. |
| Ember | No addon candidate found | Deferred age-appropriate friendship art; preserve native identity and outcome-specific expression; no adult-romance redesign. |
| Aivu | No addon candidate found | Deferred age-appropriate friendship art; preserve dragon companion design and actual development; no sexualized humanoid transformation. |
| Jannah Aldori | No candidate found | Source native identity, service clothing and state-specific prison/return references; avoid depicting release before verified release. |
| Yaniel | No candidate found | Source the real rescued paladin, distinguishing Areelu's disguise; captivity and post-rescue scenes need truthful physical state and setting. |
| Delamere | No candidate found | Native death/undeath and authored autonomous restoration require distinct visual histories; retain recognizable identity across any restored form. |
| Elyanka Camilary | No candidate found | Source native priestess identity and clothing; attractive redesign must retain identity and label visual rejuvenation separately from canonical age. |
| Herrax | No candidate found | Source costume and distinctive scars, damaged eye and wings; soften treatment for appeal without deleting all recognizable injuries. |
| Mielarah | No candidate found | Obtain native captain reference; shipboard and later private scenes need actual manuscript continuity; avoid interchangeable harbor portrait. |
| Shamira | No candidate found | Source native demonic form, coloring and revealing costume; preserve authority and dangerous expression in attractive humanization. |
| Hepzamirah | No candidate found | Source native living and ghost appearances; rescue/restoration illustration must follow actual authored state; preserve distinctive powerful physique. |
| Iomedae | No candidate found | Source native divine appearance and armor; authored private imagery cannot stand as evidence of canonical romance or changed identity. |
| Eliandra | No candidate found | Source native priestess appearance, clothing and location; vigil and later contact scenes need appropriate settings. |
| Devarra | No candidate found | Native dragon appearance needs sourced review before an authored attractive adult humanoid form; brood outcomes and actual restoration must determine scene continuity. |
| Melazmera | No candidate found | Native umbral-dragon traits should inform an explicitly authored adult humanoid form; do not invent exact native humanoid likeness. |
| Nidalynn | No candidate found | Source native silver-dragon/teacher presentation; any new humanoid art needs a clear native-versus-authored account and independent review. |

## Areelu v6 independent visual review

Candidate SHA-256 is `5C1B8AC6ECE1A27112ABC901AF4606361F0BCC624BE3D4623297EE90CCDE0CFF`.
Reference SHA-256 is `4697AEB63A573FAEC09D49903F6BF49EF989858359DD6872B412B546EC4537D6`.
Both hashes were read from the actual files during this review.

V6 preserves the dark auburn waves and high hair knot, silver-banded horns, red eyes, forehead jewel, black arm tattoos, bat wings, red draped sleeveless top, brown bracer and localized violet left-clavicle fissure.
These cues make her recognizable beyond a generic attractive horned woman.
The fuller bust and lower drape are visibly delivered without replacing the native red cloth with gold armor or adding conservative coverage.
That is the user's requested enhancement; the official standing pose and crossed hand do not prove exact bust equivalence.
The candidate's pose, bust emphasis and cropped torso differ from the reference.

| Reviewed dimension | Score / 100 | Visible basis |
| --- | ---: | --- |
| Recognizable identity | 94 | Hair, red gaze, jewel, silver horn bands, tattoos and wings work together. |
| Adult attractiveness | 96 | Mature facial structure, strong gaze, appealing mouth and coherent humanized anatomy. |
| Costume and identity motifs | 93 | Red cowl, bare tattooed arms, silver accents and brown bracer restore major native cues; lower-body outfit is outside the image. |
| Requested silhouette direction | 95 | Fuller bust and open drape clearly answer the latest preference; no claim of measured model equivalence. |
| Visible anatomy | 92 | Neck, shoulders, elbows and crossed arms connect coherently; overlapping hands and foreground blur limit inspection. |
| Painterly game fit | 92 | Painted surface treatment and fantasy lighting remain consistent; finer rendering is smoother than the native portrait. |
| Full-image composition | 91 | Her gaze dominates the meeting; foreground Commander and apparatus crowd the frame and constrain crops. |
| Clearly adult presentation | 99 | Adult face, proportions and bearing throughout. |

These independent editorial scores pass the source-image candidate gate in this review only.
They do not promise user acceptance, certify exact model proportions or approve any page assignment.
Scene fit, portrait crops, installed loading and actual transitions remain unscored.

The image shows a specific light-skinned, brown-haired Commander physically opposite her at a table full of instruments.
That appearance is not configurable in the painting and will conflict with many player characters.
Before assignment, either establish that the image is an acknowledged illustrative vignette or produce a variant with the Commander out of frame.
The image cannot literally depict a remote conversation or an expressly empty meeting room.
Use an actual in-person research scene with compatible props if one exists; do not rewrite a scene solely to justify this asset.

## Nocticula needs another costume pass

The v3 face remains attractive and recognizable, and the bare arms and midriff improve on the rejected covered gown.
Direct comparison nevertheless shows a substantial dark breastplate, thick ornamental edging and bracers replacing the native portrait's sparse chains and smaller ornaments.
The native portrait also has a straighter hair silhouette and different marking distribution.
This difference matters under the user's latest demand to preserve original clothing and sensuality.

I score native-costume fidelity at 86 for this latest, stricter scope.
This is a new independent judgment of the viewed images, not an edit to the historical v3 review or a statement that the attractive image has no use.
Retain v3 as an alternate armored outfit candidate and generate a separate closer native-costume portrait with the visible native skin pattern and ornate minimal coverage.
Do not make the new version more covered to simplify generation.
Do not infer exact breast dimensions from the reference's bent arm and raised knee.

## Assignment and verification work

The existing `Node.Portrait` field and `BookEventVM.SetPage` patch already support automatic page changes.
I checked those source locations in `src/Story.cs` and `src/Main.cs`.
No concrete scene need justifies a clickable selector at present.
Use separate explicit portrait keys on pages whose costume, physical presence, relationship state and visible participants actually match the image.

First finish Areelu's assignment or produce a Commander-free variant, and revise Nocticula's default costume.
Then complete fresh latest-brief comparisons for the other eleven illustrated characters not directly compared against native references in this review.
Chivarro and Soana were visually inspected here, but their native-reference comparison and exact-action review were not repeated.
Give the 22 missing characters sourced briefs before generation; prioritize adults with advancing manuscripts while Ember and Aivu remain deferred.

For each new assignment, verify the actual branch, file hash, packaged filename, portrait key and setting continuity.
Inspect any produced crops at their real display size.
Headless asset and assignment checks can establish file presence and branch mapping, but they do not establish Unity layout, framing, image transitions or visual readability in the running game.
No staged file or old candidate score is full-route art completion.

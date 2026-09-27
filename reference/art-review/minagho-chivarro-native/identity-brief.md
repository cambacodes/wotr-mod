# Minagho and Chivarro: native visual reference brief

These are locally extracted native references for future art generation, not new portraits or accepted artwork.
I read [the current design brief](../../../art/CHARACTER-DESIGN.md) and viewed all three extracted images.
No web search, image generation, portrait staging or installed-file edit was performed.

## What is actually character-specific

| Character | Native unit | Linked portrait | Evidence status |
| --- | --- | --- | --- |
| Minagho, Chapter 4 | `23e9e36701934fcbbf3e1472091d9321` | `19ed7729af1791747be6e6fe9f0eac92` | Character-named portrait, 692 x 1024, plus its 332 x 432 half-length image. |
| Chivarro | `b7e819e2a9bb0804abcbffe8e7d91ba6` | `0368384f099541b2b7dfb1cc6618e799` | Generic Lilithu initiative image, 188 x 244, also assigned to ordinary lilitu units. |

View [Minagho's portrait](minagho-native-portrait.png), [its native half-length version](minagho-native-half.png), and [Chivarro's linked generic lilitu image](chivarro-linked-generic-lilitu.png).
The half-length image is not an independent costume or likeness design.
Chivarro's reference is a lilitu image, not evidence of a unique Chivarro painting or a generic succubus being her actual race.
Both women are described as lilitu in native text.

Both inspected character units and the standard lilitu use prefab `1ea6c4a5300b9ca49918748d7711ccc3`.
The extracted prefab records show the same Lilithu mesh at path ID `-7913338394467847861` and the same external material reference for its two skinned renderers.
This is shared model evidence, not proof of a unique Chivarro model or identical final appearance under every scene effect.
The unit bundle contains no Texture2D or Material objects; its external material was not reconstructed or rendered here.
Do not turn the blueprint's Color field into an asserted skin color without tracing its rendering use.

Exact blueprint paths and data are in [unit-portrait-blueprints.json](unit-portrait-blueprints.json).
Image asset IDs, native texture IDs, source-bundle hash, dimensions and PNG hashes are in [portrait-provenance.json](portrait-provenance.json).
[shared-lilitu-prefab.json](shared-lilitu-prefab.json) records the original model bundle hash, mesh metadata and renderer references.
Images were decoded with UnityPy at original dimensions without resizing, retouching or compositing.

## Identity anchors and attractive adult treatment

Minagho's strongest painted anchors are long pale platinum hair, enormous dark ridged curling horns with gold bands, elongated pink pointed ears with gold hoops, pale lavender-gray skin, a smooth eyeless upper face, deep red lips, long pointed nails, crimson clothing and elaborate gold ornaments with red stones.
Her lifted chin, teasing mouth and economical hand gesture matter as much as the ornaments.
The native painting already gives her appealing adult facial proportions and skin without an elderly treatment.
Keep that sophistication while softening unnecessarily harsh rendering; do not replace it with a generic horned human face or add age lines to signify maturity.

Chivarro's linked thumbnail supports long warm blond hair, ridged dark horns, pointed ears, gold jewelry, a poised smile and lilitu facial anatomy.
Its warm lighting and small size are weak evidence for a precise skin tone or fine costume details.
Native localization `aef056e5-3482-4d29-91a3-ca5b728a2596` explicitly describes an attractive lilitu, an eyeless serene face and a simple revealing dress.
Her authored individual design can emphasize an exacting hostess's bearing and more restrained clothing, rather than copying Minagho's elaborate crimson-and-gold ensemble.
Distinct coiffure, dress construction and expression should be labeled authored differentiation, not newly discovered canon.

The current brief allows imperfections that improve resemblance while requiring conventionally attractive adult presentation.
For these women, smooth skin, balanced lower-face proportions, beautiful lips, graceful ears and well-shaped horns can carry attractiveness without making them look old or jagged.
The eyeless face is an identity-defining design issue, not damage that attractive art must automatically erase.
Expressive human eyes would be an intentional alternate design or a chosen mortal guise, not an accurate depiction of their native true forms.
For Minagho, the existing Mina disguise offers a story-supported way to depict a conventionally human face while retaining a separate recognizable true-form design.
Do not assert that removal of the forehead brand restores eyes.

## Brand and chronology

Native text separately identifies Minagho's eyeless anatomy and Baphomet's painful forehead mark.
Localization `5e299b91-e8a7-42af-a388-051dfd5e880d` describes a forehead pentagram; `826cef2d-f7d5-4aa7-becf-448bb0b8f19b` describes the carved symbol.
The extracted character portrait has a smooth unmarked forehead, so it is not a visual stencil for that mark.

The parent Trickster solution is witnessed in `RanRomMinaBook01Page004Cue0004.Text`: her own blood satisfies the condition and releases the accursed pain.
Other parent histories remove the brand differently or defer overcoming it.
Art for the reviewed continuation must name its parent history before deciding whether the mark is active, absent or represented by an authored residual trace.
A new scar or glowing rune is not automatically canon merely because it makes the portrait more dramatic.

## Scene-fit options from the reviewed continuation

- Minagho: the lamp-lit invitation and copied papers, with amusement at the Trickster's correction; or the repaired glove and copied order, where her pride remains visible without a redemption halo.
- Chivarro: the bathhouse rehearsal, loose-sleeved warm dress, painted stage door and controlled welcome; or the private room with the wall-facing window, curtain and unreliable couch.
- Pair: the mask-stone game and sugared plum, with attraction expressed between the women independently of the Commander; or Chivarro's returned red book and their imperfect reconciliation.
- Later romance: the quiet post-performance room, fatigue and relaxed posture rather than a generic seductive throne scene.

These settings and garments are authored continuation developments, not native model discoveries.
The manuscript is the living parent-history continuation reviewed at SHA256 `BD12627BB8F5BA80DAB93746388BC714E34B058AF76D2F65D6D64CFCC6EAF7FF`.
Future generated candidates still require actual independent checks for attractiveness, identity, adult proportions, anatomy, mutual agency, painterly consistency and scene fit.
Nothing here guarantees a review score or verifies runtime crops.

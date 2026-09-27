# Vellexia painting transition and revised civilian art

Date: 2026-09-27.
Export: 639 scenes, SHA-256 `0B9FBD6DEBDA5ECEA923B9610B184E7C1341A5368AAED42BB9988BBB170115A0`.

## Changes and independent evidence

The user rejected TogetherReckoning v3 as too close to Anevia's adventuring outfit, superseding its prior scoped approval.
V4 changes the garment type and silhouette to a wine-red dress, with distinct neckline, sleeve volume, skirt and woven sash.
Its independent review covers likeness, scene staging, meaningful design variation, setting-appropriate construction and the delivered material behavior.
It does not claim the later comprehensive fabric specification existed before generation or that exact fiber composition is measurable from the pixels.
The staged image now matches v4 SHA-256 `1BF1BC93BA18CEF86DE3616ED503BE1085B884E5D8791372324D9E6BFC44C508`.
Only `reckoning/truth` uses this key.

Vellexia's painted likeness now has two independently reviewed images.
The first shows the pleased expression, chipped cup and bright sky; the second shows faint impatience, a whole cup and darkened sky.
The white dress and ordinary room are authored story details, not a claim about native date clothing or full-body anatomy.
The original `picture` node retains the first part of its prose and leads to a new `picture_changed` node at the look-back transition.
The original two outcome choices moved intact to the new node.
The five reviewed living-speaker pages use the separate `VellexiaManorSpeaker` key, including the return from the painting to her dialogue.
Other campaign pages were not given a blanket portrait approval.
The opening helper now preserves explicit portrait keys instead of overwriting them.

Independent reports: `reference/art-review/together-reckoning-v4-independent-review.md`, `reference/art-review/vellexia-v1-independent-review.md` and `reference/art-review/vellexia-painting-v1-independent-review.md`.
Exact prompts and retained versions are in `art/candidates`.

## Verification

A structural comparison against the preceding export rejoined the two painting text segments, restored their original choice placement and normalized the intended portrait changes.
The resulting object exactly matched the preceding export, proving no other prose, outcomes, flags or scene data changed.
All four staged additions/replacements were compared byte-for-byte with their reviewed source images.
The whole export passed 35,664,519 Rules assertions, including existing Vellexia branch traversal and state-preservation checks.

Actual managed Main.Build passed 85,925 assertions for 639 scenes and 23,315 generated blueprints.
It preserved fourteen native answer lists, the native Aeon sequence and the parent-mod sentinel across an idempotent rebuild.
The DLL remains `B98B72E5E8E2E79F0ACDCB6006B8683485FA3B130A27B1CC8CACFE68680FC1B8`.
The same isolated UnityPy interpreter and three recorded parent-binding fixtures were used.
No rebuild was needed because executable code was unchanged.

The image audit reports 35 requested keys, 16 present files and 19 missing files.
Its nonzero exit is retained as evidence of incomplete art delivery.
The content inventory was regenerated but remains an aggregate inventory, not a selected completed-path count.

## Limits

The optional Expanded Epilogue fixture was absent.
Caught resurrection and Unity LoadingProcess boundaries remain as recorded in previous managed runs.
These tests do not verify native acquisition, complete campaign eligibility, real saves, ToyBox execution or Unity rendering.
The two-state switch still needs an in-game check of transition timing, scaling and cup readability.
No complete route or full roster is ready on the strength of this art integration.

## Material refinement after user review

The user requested more consistent transmission through the visibly lightweight white fabric.
Day-v2 and Changed-v5 subsequently passed independent static review in `reference/art-review/vellexia-painting-v5-independent-review.md`.
The earlier changed-v2 and changed-v4 candidates failed because the chipped rim remained; those failed outputs and their reports are retained.
Changed-v5 replaces the cup with a whole ordinary earthenware vessel of a slightly different wall profile, which the review found consistent with the magical painting's description.
Both selected revisions retain the improved fine weave, light transmission, denser gathers and pose-dependent drape.
No exact denier, GSM or fiber composition is certified from their pixels.

Staged day SHA-256: `4074EF5BF78192FCBF0780F060CBC9AB0A7049F94394DEE8BD05F27EEAFCEAA7`.
Staged changed SHA-256: `42CD5DDFD78D8696FBD52719840020FA9B7E584FD86614BDF7DBCA2D984E178A`.
Byte comparisons verified both staged images against their reviewed candidates and confirmed each still appears only on its intended page.
The Story.json hash remains exactly the fully tested hash above, so broad code tests were not rerun for this asset-only replacement.
The refreshed art audit retains 19 missing keys and its nonzero result; that does not invalidate the two specifically verified files or establish complete art delivery.
In-game framing and readability remain unverified.

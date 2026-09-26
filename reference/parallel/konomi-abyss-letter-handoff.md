# Konomi Abyss letter revision

The parent owns `storylines/konomi.py` and the new `tests/KonomiLettersTests.cs`.
Current source SHA256 is `EF26EEA2F99DC5767C991BACDF37CC10DE62A1F47BAD981C79ACD6A8491C9365`.
The revision is staged in `development/konomi-letter-review.json`, SHA256 `403C22C64913B0A12F3BC08DC4172518F974EA61ACECC40AFBFC3995168B216D`.
The main development export remains the reviewed 174-scene Soana checkpoint.
Do not regenerate that export from the modified Konomi source until this contribution has received independent review.

## Problem and delivered change

The assembled audit identified that the wonder and fear choices shared the same unsent letter and returned response.
The two existing choices now lead to distinct new pages before the original folding-and-keeping page.
Wonder lets the Commander retain an unqualified beautiful recollection or write about the uneasiness it caused.
Fear lets the Commander ask for a concrete question or ask to be heard before questioning.
These authored personal recollections do not assert completion of a native Abyss encounter, make a political decision or send an impossible letter out of the Abyss.

At the Chapter 5 reunion, delivering the letter opens the corresponding reply.
Konomi attempts to reconstruct the described light and distinguishes wanting the Commander's company from approving the Abyss.
The fear reply lets her question the Commander's recollection or listen before answering, matching the earlier request.
Choosing to ask about her first still permits the original conversation without forcing delivery of the letter or recording its reply.
The ordinary route remains much too compressed; this addition addresses one identified gap and is not a full Chapter 5 expansion.

## Compatibility and checks

Existing scene and node IDs and authored choice indices remain in place.
The existing letter-page answer remains at index zero as a fallback for older wrote-only histories; new subject-specific replies are appended.
Older fear and wonder histories without the new intention flags each have an attainable response.
If both subject flags exist, fear takes precedence rather than producing two incompatible replies.
No native quests, political choices, unrelated romances or relationship commitment flags are changed.

The review export passed 2,252,416 rules assertions, including the focused letter tests.
The first focused run failed because the new test omitted Drezen's area from its reunion snapshot; correcting the fixture made the actual scene reachable without changing route eligibility.
Tests cover all four new letter intentions, subject-specific return outcomes, optional non-delivery, older and overlapping histories, and unrelated commitment preservation.
These are headless graph checks, not Unity execution or literary approval.

## Pending independent review

Review the prose and choices against the actual Konomi canon material and assembled route, especially the risk of repeated introspective relationship discussions.
Check whether the Commander choices allow credible roleplay and whether Konomi's ambition and sharpness remain present alongside affection.
Inspect older-save choice continuity and the distinction between a personally authored recollection and a native-event claim.
No review score has been assigned.
An initial independent review subsequently scored writing 85 and bounded canon compatibility 91, requiring revision.
The parent revised the broad fear setup into explicit choices about threatened judgment or ordinary pleasures, removed the invented legacy obedience sentence, and added an older-history listening option.
The uneasy reply no longer forces an admission that the Commander wanted to stop noticing suffering.
The requested kindness anecdote is now played in its own node instead of skipping directly to a summary.
There are now five new letter intentions, and the revised staged export passed 2,252,570 rules assertions.
Independent rereview is pending; the original frozen hashes above identify the first delivery rather than the revised source.
The three worker slots remain occupied by separate character authors; independent review will be assigned after an ownership handoff frees a slot.

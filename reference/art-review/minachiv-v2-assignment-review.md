# Minagho and Chivarro v2 assignment review

Independent source assignment review on 2026-09-26.
Approve Chivarro-v2 only for `minachiv.the_entrance_she_wants/warm` as a general warm-dress scene illustration.
No existing page is approved for Minagho-v2 under its previously reviewed post-Trickster-release scope.
No source, engine or asset was edited during this review.

| Image | Reviewed SHA256 | Assignment verdict |
| --- | --- | --- |
| `Minagho-v2.png` | ED1835FB4225D6693629719D356646C5A038045BB72039413AA509AEFDE184ED | Keep unstaged pending a page with the correct history or a separate broader-history review. |
| `Chivarro-v2.png` | A4F89615BE56AC81B5E0FD39893906AFFB902256EC699DD55175ADC9B995BF71 | Explicit scene key on the single `warm` node below. |

## Minagho

`minachiv.two_answers` requires parent Book 3 completion, an actual finished-book witness and Chivarro's search.
It does not require `minagho.brand_trick_seen` or restrict entry to the parent's Trickster release history.
I inspected all seven node paths: `start`, `reply`, `scrolls`, `asking`, `past`, `refusal` and `agreement`.
None supplies the missing brand-release restriction.
The scroll-report and romance/refusal branches establish different facts and cannot substitute for it.

The source maps `minagho.brand_trick_seen` to parent cue `a8f7a881cc6d427b91cbbee14f43e0ee`.
The previously extracted parent text `RanRomMinaBook01Page004Cue0004.Text` depicts the thumb-prick solution succeeding and Minagho's relief from the brand's pain.
Other parent histories may remove the mark differently or leave its overcoming unresolved.
The reviewed image's absent mark was approved for the specified Trickster history, not all those possibilities.
Her eyeless anatomy is independent of that mark and correctly remains eyeless in the image.
Do not describe release from the mark as restoring human eyes.

The opening page begins in her Mina disguise and then explicitly says she drops it.
A true-form portrait could illustrate the latter part of that page, so the disguise transition alone is not the blocker.
The shared parent histories are the blocker.
Even the apparently suitable `reply` or `asking` pages remain shared and cannot carry this narrowly approved image unconditionally.

`minachiv.the_second_address/trick` does have an incoming choice requiring both current `trickster` and the actual `minagho.brand_trick_seen` witness.
However, that later scene concerns two invitations, their changed forwarding address and Chivarro's participation.
The existing visual approval concerns the earlier rented-room invitation.
I do not transfer it to a different scene merely because that scene supplies the missing flag.
That would need a separate actual scene-fit review.

The source currently uses `Minagho` as a speaker-wide portrait key on many pages.
Do not place Minagho-v2 at that global key.
A future source-level branch-specific page could give this image a safe assignment, but this review neither requests an engine for conditional images nor changes the story to accommodate the asset.
For now, the approved illustration remains available without a runtime assignment.

## Chivarro

Use an explicit key such as `ChivarroWarmDress` only on scene `minachiv.the_entrance_she_wants`, node `warm`.
Its sole incoming choice asks her to try the loose sleeve, and the node says she changes behind the hanging cloth before returning in that dress.
The image's copper gown, loose sleeve, unused dark dress, curtain, cup and nearby-wall window support that branch.
Her pose is a general view of trying the dress, not proof of the precise instant she catches the cuff before it brushes the cup.
That limitation from the actual image review remains in force.

Do not assign it to `start`, where she is wearing a plain robe with both dresses on the couch.
Do not assign it to `dark`, where she has selected the severe dress.
Both `dark` and `warm` feed directly into `alone` without recording a dress choice that separates later pages.
Consequently, `alone`, `asking`, `memory`, `promise` and `ask_later` can all occur while she wears the dark dress.
Those shared pages are not approved for an unconditional copper-dress image.
Do not stage the image under the global `Chivarro` key.

## What remains missing

Minagho still lacks an assigned image that is safe across the supported parent histories.
Chivarro's robe, severe-dress branch and shared later pages need their own neutral or appropriately scoped visual treatment if images are wanted there.
Neither image covers the two women together, their wider campaign settings or every ending.
These are missing art assignments, not evidence that the accepted individual images have failed their visual review.

The engine already supports explicit page keys through `Portrait`; no conditional art machinery is needed for the approved Chivarro node.
The fresh native `BookEventVM` inspection recorded in the Soana assignment review shows that ordinary page changes restore the default/page image before the addon's optional portrait override.
Thus a scoped image can return to the native default on later unmapped pages without assuming image carryover is intended.
Actual Unity loading, sizing, crops and transitions remain unverified here.

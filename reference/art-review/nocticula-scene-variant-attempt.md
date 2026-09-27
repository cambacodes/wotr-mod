# Nocticula scene variant attempt

The approved v4 source image is not assigned to a story page.
The proposed new target was `noct.her_own_face`, node `start`, in `storylines/nocticula_continuation.py`.
That scene describes an enclosed dark chamber, one lamp, a wide couch, pale fruit, and a book that Nocticula closes and moves from her knee.
It expressly excludes the harbor.
The earlier dream balcony is a different setting and inherits the black dress described at the opening of that dream, so it is not a suitable literal assignment for v4's costume.

The image-generation attempt used v4 as its character and costume reference and requested the chamber, couch, lamp, fruit and book with no visible Commander.
The built-in tool rejected the output with HTTP 400, `moderation_blocked`, category `sexual`, request ID `a96f9a37-9657-4374-84e1-3c93df6a0433`.
No image was returned or staged, and the request was not retried.
V4 remains preserved and its independent source-image approval remains separate from scene assignment.

The continuation's local scene helper currently replaces every page's explicit `Portrait` with `Nocticula`.
Before assigning any future approved variant, preserve nonempty explicit portrait keys in that helper and verify the resulting export.
The shared runtime already supports per-page keys, so no clickable selector or new UI is needed.

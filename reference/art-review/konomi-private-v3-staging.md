# Konomi evening illustration staging

The independently accepted v3 candidate is copied byte-for-byte to `art/CustomNpcPortraits/RanRomance-Tirabade/Scenes/KonomiPrivateEvening.png`.
Both files have SHA256 `BCB644CC8DDE8064C09F610EB213B1926CADA1DBF85E009E70191007E8A928A8`.
The review is `reference/art-review/konomi-private-v3-review.md`.

The authoring helper assigns the new portrait key only to `konomi.before_road/start`.
Later pages retain the approved general Konomi portrait rather than claiming this static illustration depicts every subsequent gesture.
The scene-specific image matches the empty chair, loose case straps and caught cloth at the invitation.
No dialogue, voice text, answer identity or route condition changed.

Regenerating the development export preserves 323 scenes.
Its SHA256 is `C5E2789DF3B2FF02F2ADBF01BE9754A84337F2C383D0E90BC7861B5596F5BAB3`.
A direct export check confirms that this opening is the sole user of the new key and the staged bytes match the reviewed image.
Repeated assembly and returned-scene mutation isolation pass.
The existing portrait loader resolves keys to `Scenes/<key>.png` without requiring a new registration table.

This stages an asset in the project, not in the installed game.
Runtime loading, book-event cropping and readability with dialogue controls remain unverified.

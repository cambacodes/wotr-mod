# Native book-picture fallback correction

Root rechecked the actual installed game assembly on 2026-09-26 before changing portrait behavior.
`Assembly-CSharp.dll` has SHA256 `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953`.
The freshly decompiled `Kingmaker.UI.MVVM._VM.Dialog.BookEvent.BookEventVM` is retained in `book-picture-native.cs.txt`.

Native `SetPage` calls `SetPicture(page)` before the addon's Harmony postfix executes.
`SetPicture` first assigns `EventPicture.Value = DefaultSprite`, then attempts to load the page's native ImageLink.
The addon's postfix only replaces that current native image when its requested custom portrait exists and loads.
Consequently, a missing explicit TargonaCorrespondence asset leaves the native page fallback in the ordinary SetPage flow.
It does not by itself retain the preceding authored page's portrait.

Earlier reviews correctly identified that an empty Narrator portrait key selected the installed Together image.
The explicit TargonaCorrespondence key fixes that lookup.
The later inference that the unchanged postfix value necessarily means previous-page carryover omitted the native SetPicture call and is superseded by this evidence.
No production patch was necessary for that inferred problem.
Other patches, native asset loading and actual rendered composition still need in-game verification.
Targona's dedicated art remains undelivered and a default book image is not art completion.

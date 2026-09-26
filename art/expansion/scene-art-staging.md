# Reviewed scene-art staging

These full-resolution scene images are copied without resizing or cropping from independently reviewed sources.
The engine loads them by the explicit page portrait keys below.
They are development package assets, not installed game files or approved small dialogue portraits.

| Key | Source | Staged SHA256 | Independent review |
| --- | --- | --- | --- |
| TargonaCorrespondence | originals/Targona-v2.png | 0214664A70C5A74C7CA790068799394FADA5872E594F7522E0578EA76AD99FE6 | reference/art-review/targona-v2-review.md |
| Jerribeth | originals/Jerribeth-v4.png | D27050B867E90E8E151496E9B94AA71811726FAD0A8263F8DC3F84EE3DB63509 | reference/art-review/jerribeth-v4-review.md |

Files reside in `art/CustomNpcPortraits/RanRomance-Tirabade/Scenes/` under their exact key names.
The full activity composition is intended for book-event illustration; separate face crops remain required where a small portrait is used.
Native book-image sizing, readability, loading and actual page transitions still require verification in the game.
This staging does not approve the complete character routes.

The actual local packaging command was run and both archived scene images matched these source hashes byte-for-byte.
The binary package still contains the original 34-scene story, while a fresh extraction of the source package reproduces the reviewed 264-scene development export.
Neither archive has been installed or published as an expanded release.

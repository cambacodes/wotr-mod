# Soana forest portrait staging

The reviewed Soana-v12 image is staged unchanged at `art/CustomNpcPortraits/RanRomance-Tirabade/Scenes/SoanaForest.png`.
SHA256: `323F34726445958368D1441E4929D83C33258457BEF0CDD0B54F429701856334`.
The image is a general portrait of Soana doing carrier work beside her forest cave in daylight.
It is not an exact illustration of reed insertion or the damaged handle described in the scene.

The authoring source assigns this key only to `soana.water_carrier` nodes `start`, `promised`, `work`, `hands` and `own_work`, following the independent assignment review.
A focused assembly check verified exactly these five mappings and byte-for-byte equality between staged and original images.
Other Soana pages retain their existing portrait keys.
The source mapping will enter the next validated export; the current 538-scene development JSON is unchanged at this checkpoint.

Native BookEventVM resets its picture before the addon postfix, so an excluded page does not inherit this illustration merely because its own custom image is absent.
That conclusion is based on native code inspection, not executed Unity page transitions.
Runtime loading, sizing and transitions remain unverified.
No installed art or release approval is implied.


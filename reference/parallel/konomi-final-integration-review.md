# Konomi final integration review

Reviewed 2026-09-26 by a separate reviewer of the root integration.
I authored the political contribution and do not independently approve its prose here.
Its independent literary and canon assessment is recorded in `reference/story-review/konomi-political-consequence-review.md`, SHA256 `AAE9B78E98C885C86AB48CB27241E9C4C12FD235272EEFA4953D77F8084A2EB9`.

## Result

Accept the political registration, portrait metadata changes, test registration and subsequent assembly isolation repair within this technical scope.
The frozen export remains SHA256 `C3C9D2D3FE27F64E883DFEFA8A99E5E26F09612DEA6CCFE1B37C04C11AF86210`.
This review does not certify an installed portrait, native game execution or full character readiness.

## Independent checks

I reconstructed the expected export from HEAD `98be4cc`, appended the approved political scenes, applied their integration overlay and changed only empty Konomi Narrator portrait fields to `Konomi`.
After JSON normalization, that result exactly matched both the fresh assembly and the frozen export.
All old scene IDs and ordering remained an exact prefix.
All old node IDs and answer arrays remained exact prefixes.
Existing nonempty portrait keys remained unchanged, and every non-Konomi scene remained identical.
The export contains 305 scenes, including 64 Konomi scenes and 542 Konomi pages.
There are 528 explicit Konomi portrait fields and 14 remaining empty fields on non-Narrator pages that resolve through the speaker.
No Konomi Narrator page retains an empty portrait field.

The 21 portrait changes affect `unsent` six pages, `fate_post` eight pages, `fate_reply` six pages and `private_meeting` one page.
These changes only replace the previous empty Narrator portrait defaults.
The loader previously resolved those pages to `Together`, which depicts the wrong characters.
The new key correctly requests Konomi but does not supply her image.
I confirmed that `Scenes/Konomi.png` is missing from both the project art tree and the installed custom portrait tree.
The loader returns null for a missing image and does not automatically substitute a native unit portrait.
The separate art findings remain in `reference/art-review/konomi-readiness-20260926.md`.

`expansion.py` appends and integrates the political module before applying the existing contact overlay and portrait defaults.
The new visits declare their physical contact requirements directly.
`KonomiContactTests.cs` adds the two new visits to its existing audited physical scene set without relaxing presence, office, interruption or native blocker checks.
`Program.cs` registers the new scenes and their focused test suite while preserving the prior registrations.
Root reported 14,520,503 rule assertions and 41,044 managed assertions covering 12,004 blueprints; I inspected registration but did not repeat those complete suites in this review.

## Assembly isolation defect and repair

I reproduced a preexisting repeated-assembly defect in both HEAD and the initial integrated source.
The first `make_expansion()` succeeded, but a second call in the same process raised `ValueError: Kiana reconciliation applied twice: guest_table/history_former_grief`.
Imported scene lists had been extended by reference and then mutated by integration overlays.
The production one-shot CLI export was valid despite that separate defect.

Root subsequently changed all 48 imported scene extensions to copy their templates before integration.
I inspected that repair, confirmed no uncopied module SCENES extension remained and independently ran `tools/check-expansion-isolation.py` successfully.
That check performs three assemblies and verifies that changing a returned scene does not contaminate subsequent output.
I separately confirmed that the repaired assembly, after JSON normalization, exactly equals the frozen export.
The repair resolves the reproduced failure without changing serialized story content.

## Reviewed hashes

| File | SHA256 |
| --- | --- |
| `expansion.py` after isolation repair | `AD81D01A1969528D0CA896A28FA88E2DC9B0AC3849CC53BEC80475E21E34AF15` |
| `development/Story.json` | `C3C9D2D3FE27F64E883DFEFA8A99E5E26F09612DEA6CCFE1B37C04C11AF86210` |
| `tests/KonomiContactTests.cs` | `60BC9F251E35A0B8720EAE90284C09F461549C6150624EE915F6265DAB38321F` |
| `tests/Program.cs` | `3E66110B372BBDFDEB6089DD9320E4B8C825889E27D25447AD7B5C3622DC6C1B` |

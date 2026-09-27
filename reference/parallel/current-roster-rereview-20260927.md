# Current roster readiness rereview

## Verdict

The current export and regenerated inventory agree on 631 scenes, 18 relationship keys, and the reported per-key scene and word counts.

The global conclusion that no route is fully approved is consistent with the measured inventory and its explicit `full_route_approved: false` fields.

There are stale route-status statements in `ROSTER.md`, and the reported managed and Rules test totals could not be reproduced in this worktree environment.

This report audits status evidence only and does not approve a route or infer readiness from word count.

## Input fingerprints and direct checks

`ROSTER.md` SHA-256 is `E27C8E458757E5637082705FF5654D41FF5B9944D5866EE1A34EDDFDF49FADF8`.

`development/Story.json` SHA-256 is `866B7C66C2027AFEE471FD4C497F57CD173E2AE789814FB268FC5DA49A9249C2`.

`development/content-volume-inventory.json` SHA-256 is `BF271FE3BB68FE35E9CB053E3FFFEC81B0ACA065752AA2E305278BE3D1E6EF75`.

The inventory's `story_sha256` exactly matches the current export hash.

Direct JSON parsing confirms 631 scene objects and 18 relationship keys.

The inventory reports 18 member keys, consisting of 16 adult romance character entries and the two friendship entries Ember and Aivu, with the Tirabade and Minagho-Chivarro group keys counted as shared relationships rather than wholly independent routes.

The current-roster audit's 18-key list and 631-scene total match the export.

All 18 per-key scene counts and normalized-segment word counts in its table match `development/content-volume-inventory.json`.

The paired Minagho-Chivarro key remains below its combined 42,000 arithmetic floor at 33,799 words, and its shared count cannot prove that each woman independently meets 21,000 words.

The current inventory marks every route `full_route_approved: false`, so the report's no-ready-route conclusion is supported.

## Route-specific exact-source review checks

The current `storylines/aranka_continuation.py` SHA-256 is `F2A068C8DEBC5B11694096FC7D36D057541770D6EBF147A4AE8CD405AA828AF2`, exactly matching `aranka-final-rereview.md`.

That report covers four named scenes, finds their reviewed branch links coherent, assigns no whole-route score, and explicitly leaves Trickster acquisition, contact recovery, full-route length, art, and runtime approval unresolved.

The current export contains 10 scenes under the Aranka key and 11,096 normalized distinct-segment words, matching the readiness table and remaining below the 21,000 arithmetic floor.

`reference/story-review/aranka-final-rereview.md` pins an earlier export SHA of `0589DFCC42DECA5F5787A45013CBF6BBBCDD3F27ED2AA6A246BF77B5E8F3993B`, not the current export SHA.

Its claim that the four objects were integrated is scoped to that earlier freeze; the current export's 10-scene count confirms those scenes are present now, but the old export pin should not be represented as a current export fingerprint.

The current `storylines/targona_opening.py` SHA-256 is `517AAA3B923EC23F2E54ABED31064778A1528CAD1309865297A71C9EA25E8DBD`, exactly matching `targona-final-rereview.md`.

That report reviews two revised meeting scenes and their scoped conditions, concludes its named findings are resolved, and explicitly withholds full-route approval, score, final art approval, and live verification.

The current export contains 8 Targona scenes and 8,112 normalized distinct-segment words, matching the readiness table and remaining below the 21,000 arithmetic floor.

The current `storylines/nurah_continuation.py` SHA-256 is `4927D41B97A691BFE30726BA28D7E5C42556104A0A580706F090DB2C1C0CAF23`, matching revision 3 in `nurah-continuation-independent-review.md`.

That exact revision receives a scoped literary pass, with all seven listed dimensions above 90 and 27,069 normalized distinct new words, but the review excludes art, missing-parent acquisition, universal Trickster recovery, native delivery, and playable readiness.

The current inventory contains 13 Nurah scenes and the same 27,069 normalized words.

The readiness report correctly separates that scoped pass from full-route readiness.

## Stale roster descriptions

The current Aranka roster row says six reviewed continuation visits, while the exact-source final rereview covers four specifically named continuation scenes and the current export has 10 scenes total.

The current Targona row mentions six development letters, while the exact-source final rereview covers two additional revised meeting scenes and the current export has 8 scenes total.

These may be descriptions of earlier contributions rather than the full current scene inventory, but the roster should clarify that distinction and cite the four-scene Aranka and two-scene Targona scoped reviews.

The current Nurah roster row says the continuation manuscript and private-chambers implementation are in progress, while the current export contains the 13-scene manuscript and the headless report claims the integrated 631-scene hub graph.

Update the Nurah row to distinguish the authored 13-scene manuscript and current hub integration from the still-open live click, actor placement, save/load, art, and full-route gates.

That update must not promote the scoped literary pass to route approval.

## Headless test record and rerun

`reference/parallel/headless-verification-20260927.md` SHA-256 is `AB3390D0B71B9195D3DE8EDECA42BA64E1C16DB3C80084AF1E78C61519B213AA`.

It records 84,259 managed assertions and 28,550,910 Rules assertions, and correctly bounds those checks as graph construction and seeded rule scenarios rather than live save, Unity scheduling, rendering, ToyBox, or full campaign evidence.

The record's export SHA matches the current `Story.json` and inventory.

I attempted the managed runner against the current installed game directory and current export.

It did not complete: the native extraction step reported 68 missing blueprint IDs from the installed `blueprints.zip`, including the three Nurah callback identifiers previously audited, then exited with `Native blueprint extraction failed`.

The runner also logged its documented cross-scene actor-list and native resurrection fixture boundaries before failing.

The Rules test could not run because this environment has no .NET runtime or `dotnet` executable, and the apphost reports that .NET 8 is not installed.

Therefore I cannot independently confirm either assertion total against the current installed game and runtime, despite the report's pinned source and inventory matching the current export.

The rerun failure is an environment or installed-source compatibility blocker for reproducing the evidence; it does not by itself establish that the historical test report was fabricated or that its reported run failed at the time.

## Required status corrections

Update the three ROSTER rows to reflect current scene totals and accurately separate earlier contributions from the exact-source reviews now on disk.

Record the managed and Rules assertion totals as historical results tied to their runtime and installed-game inputs until a current repeatable run is available.

Keep the existing statement that no route is fully approved, and retain the explicit limits around live gameplay, art, Trickster acquisition, recovery, and meaningful single-playthrough content.

No route approval is granted by this rereview.

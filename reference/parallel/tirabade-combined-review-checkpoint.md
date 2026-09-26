# Combined Tirabade review in progress

The separate Anevia and Irabeth manuscripts passed their bounded independent rereviews.
Their reports do not approve shared integration, exceptional native access, universal Trickster recovery or live delivery.
Konomi remains editorially ready for the user's own TTS work, with no new freeze milestone.

`tests/write-tirabade-bridge-fixture.py --combined` now assembles both actual manuscripts and the shared bridge in `development/tirabade-combined-review.json`.
It removes the dummy Irabeth declaration book and registers the actual Irabeth chapter and observed-dialogue aliases.
Following independent acceptance, the development builder now includes these contributions and exports 395 scenes.
Its output is byte-for-byte identical to the reviewed candidate, SHA256 `72B279626E27296F36C115C24874248FA9F56370B18DA61711E4D42881BEE9EF`.
The fixture generator also writes `development/tirabade-pre-independent-baseline.json` from `make_expansion(independent_tirabade=False)` for the retained answer-index comparison.
`tests/RulesTests.csproj` accepts `--tirabade-combined development/tirabade-pre-independent-baseline.json development/Story.json` to run both individual suites and the bridge suite together.

The first combined run exposed standalone test witnesses selecting newly appended local-refusal answers while intending to play the retained affair.
The next run exposed an Irabeth test matrix preloading an Anevia closure before its intended legacy acquisition.
The independent integration reviewer owns both individual test files during repair and must preserve relevant history coverage.
The reviewer reproduced a shared invitation after Irabeth chose friendship and a missing remaining-wife ending after Anevia parted from an active triad.
The bridge now closes the shared arrangement when an independent choice ends either romance, explicitly telling the player that consequence.
It preserves the other woman's relationship flags and does not manufacture an invitation or native marriage agreement.
Irabeth's friendship also excludes shared romantic invitations and retained shared continuations, without excluding her own friendly farewell.
Review also found two Anevia dialogue choices treating Irabeth's friendship as a continuing romance because the historical lover marker remains set.
The bridge now excludes friendship from those active-romance choices and appends truthful past-romance alternatives, preserving existing answer indices.
Permanent played-history witnesses cover both acquisition orders, friendship and its farewell, local parting from an active group, both directions of early refusal followed by the other woman's romance, and contact loss and restoration during actual books.
The combined focused suite passes 906,027 assertions with those witnesses registered.
The full combined rules suite passes 20,018,848 assertions after the final callback repair.
The independent review report, `reference/story-review/tirabade-combined-integration-review.md`, accepts this ordinary living-contact combination for integration.
It does not certify universal Trickster access, runtime delivery or the full doubled-length shared campaign.
The final builder also passes repeated assembly and returned-scene mutation isolation with both independent manuscripts included.
After commit `d2ad3fa`, a fresh `git archive HEAD` was extracted into a temporary directory and rebuilt with `tools/verify-source-package.py`.
The extracted source reproduces the exact 395-scene development bytes and SHA256 above.
This proves the committed source contains the required builder inputs; it does not execute the installed game.

## Verification completed during staging

The repaired candidate SHA256 is `72B279626E27296F36C115C24874248FA9F56370B18DA61711E4D42881BEE9EF`.
Its 763 binding uses resolve to 114 installed archive targets and 29 reviewed parent-source targets.
Actual managed blueprint construction passes 50,849 assertions for 395 scenes and 14,845 generated blueprints.
Existing dialogue references and finish actions remain preserved, and repeated construction remains idempotent.
This uses development DLL SHA256 `17FBCBEA31F916F4FF4286B58168C8EE1918E7C6E341253891E55DF1754D0FB9`.
These checks do not execute parent-mod initialization, Unity presentation, ToyBox or a real game-save round trip.

The normal rules runner now invokes each individual campaign suite when its manuscript is present before excluding those scenes from prerequisite-only synthetic draft checks.
The latter cannot model Irabeth's native chapter-dependent acquisition answers or the manuscripts' played histories.
The unchanged 323-scene campaign with the new Konomi illustration assignment separately passes 18,784,596 rules assertions.
Repeated expansion assembly and returned-scene mutation isolation also pass.

The combined content inventory is `development/tirabade-combined-content-review.json`.
It records 25,649 distinct segment words for Anevia, 25,725 for Irabeth and 51,186 for the shared campaign.
These are alternative-inclusive totals with choice labels, not selected-playthrough lengths or proof of quality.

Parallel ownership is Gesmerha's new campaign module and focused tests, Arsinoe's new campaign module and focused tests, and the independent combined-route review with its individual test repairs.
Root owns shared registration, exports and bridge implementation.
New campaign contributions require independent review before acceptance.

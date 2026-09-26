# Konomi presence gate: focused technical review

No blocking defect was found in the bounded rule change on source inspection.
The change prevents ordinary addon meetings when the mapped capital-presence etude is not playing.
It does not establish actual actor contact, implement restoration, or approve the full Konomi route.
I also read the finalized separate native availability audit, which supplies the selected etude's actor and lifecycle evidence.

## Reviewed state and scope

The reviewed development export has SHA-256 `D7DCFEABFC54F4D60DCC92070D225A0980FABCFE71F09A518D5A323E896E631C`.
`expansion.py` maps `konomi.present` to `b5f301fbc4c44535a6309d610d5bd28a`.
The local etude index identifies that GUID as `World/Etudes/Common/WrathOfTheRighteous/Chapter03/CapitalMechanic/DrezenCapital_DefaultMechanic/DiplomacyOfficer_InDrezen.jbp`.
All 12 ordinary Konomi scene exports require this alias.
The remote `konomi.unsent` scene and all seven ordinary/Aeon epilogue scenes do not.
No current choice writes `konomi.present`, and the alias is not included in `PermanentEtudes`.

## State and eligibility semantics

`Main.State()` creates a new snapshot on each call.
An etude alias is added when its actual fact has `IsPlaying == true`, with completed-state fallback only for explicitly permanent aliases or the specified special-name classes.
`konomi.present` matches none of those permanent categories.
A merely started but dormant etude does not pass this condition, and a completed etude does not gain presence through the completion fallback.
The fresh snapshot avoids retaining presence after a previous snapshot observed it.
Current data also avoids a second unlockable-flag source with the same alias, which otherwise could defeat this distinction because State combines flag sources.

`Rules.Available` checks scene requirements before returning early for epilogues or applying relationship rules.
The ordinary-scene helper adds presence without replacing existing requirements, areas, chapters, or relationship closure conditions.
There is no Trickster bypass of `Requires` in the production predicate.
Native entry answers apply the scene condition to both visibility and selection, and `RouteAction` checks availability again before queueing a start.
This means displaying unavailable answers through ToyBox does not by itself satisfy this gate.
The alias is an etude-backed eligibility prerequisite, not a physical unit search or proof that the native answer list can currently be reached.

## Delay behavior

Scene delay is measured from the latest timestamp among required keys that actually have timestamps.
Native etude aliases do not acquire timestamps in `Main.State()`.
Build registers timestamps for addon scene completions and choice effects, not every native requirement.
Because the current export never sets `konomi.present` through a choice and does not reuse it as a scene ID, the added requirement contributes no timestamp and does not reset or extend existing delays.
If enough time passed since the relevant relationship event, restoring native presence can immediately make the scene eligible.
If the relationship delay has not elapsed, restoring presence does not bypass it.
This is an elapsed-time gate, not a requirement to spend the waiting period continuously in Konomi's presence.

## Tests and limits

`tests/KonomiTests.cs` explicitly removes presence, checks ordinary scenes unavailable, adds Trickster and checks again, restores presence and checks availability, then removes it again.
The loop supplies all other required flags and a matching area/chapter, which isolates the new requirement for each current ordinary scene.
The remote unsent-letter test omits presence while checking its gardening prerequisite and delay.
Completed-campaign tests remove presence and verify the selected ordinary ending remains available.
The export inspection confirms all other endings also omit the alias, though the explicit no-presence ending assertion does not independently exercise every ending variant.
Campaign simulations retain existing progression, closure and choice-dependent outcome checks.
I inspected these tests but did not independently rerun the suite in this review.

These are pure snapshot tests; they do not execute `Main.State()` against real playing, dormant and completed game facts.
Source inspection supports that translation, while native etude extraction and actual-game checks provide different evidence.
The loss-of-contact test checks snapshot behavior and cannot alone establish live engine cache behavior.
Ordinary choices inside an already opened book use their choice-level conditions and do not continuously recheck this new scene prerequisite.
The change should therefore be described as a scene-entry gate, not an automatic interruption mechanism if native availability changes during an open conversation.
No interruption requirement is necessary to establish the bounded requested fix.

The added helper assignment only changes scene requirements and does not transform node prose, choice text, next-node links, or choice effects.
I have not claimed byte-for-byte choice stability against a saved pre-change source revision because none was used in this review.

## Installed state and verdict

The installed addon story remains SHA-256 `3176BB0102324BAB5BAF664D6956D5DEB3A4FB638029789D74F0EFCDF73DC6D4` and its DLL remains `E44115E37170946318CA3BAF1A3BE03CAD65C09318E305313481A43C55AD0F50`.
Those hashes match the earlier independent installed-baseline inspection.
The presence gate is development work and has not replaced the installed addon.

The bounded code gate is coherent, preserves existing delay semantics, and keeps correspondence and endings separate from physical-presence prerequisites.
No source-level blocker was found for that claim.
The finalized `reference/canon-review/konomi-availability-review.md` confirms the playing etude unhides and positions the actual officer spawner, with temporary rank-up conflict arbitration and explicit dismissal/Swarm removal consumers.
That evidence supports the chosen ordinary-contact prerequisite while distinguishing temporary absence, dismissal and actor destruction.
The owner reports 44,409 passing rule assertions, 181 external uses resolving to 53 typed targets, and 7,970 managed assertions for this export; those are owner-reported verification results, not an independent rerun here.
Exceptional-path restoration, physical contact, full-route length and quality remain outside this gate's approval scope.

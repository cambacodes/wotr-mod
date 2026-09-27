# Galfrey all-path continuation prototype independent rereview

Review date: 2026-09-27.

Reviewed source SHA-256: `2E15E270608AD695DC80647699AEC409B6FAACA66EA23F11328B178E3809A779`.

Reviewed development report SHA-256: `6ECDF966149F020A486D67C77A135431B580A3A37A89D699E4CC37863DFC4804`.

Compared against prior exact-source rereview `reference/story-review/galfrey-all-path-continuation-rereview-2.md`, SHA-256 `230579242B3CA584BD734C9026ECF462D29F641F6D9CD82E52D604722E405D85`.

Compared against installed-source audit `reference/canon-review/galfrey-continuation-audit.md`, SHA-256 `090F2A65BC0B56EB8A4487017FD38C62B3AEC3D0831B5506BFAE0063CCD284CD`, and installed `blueprints.zip`, SHA-256 `BE61C9B723EF06558DA8D7CFC7F0C7EA869F60BA9952EBBBBD116CF681863EA5`.

I reviewed the exact source and report, relevant installed Chapter 5 and Lich blueprints, and the report's prior findings.

I did not edit the source, report, or generated Story.

Disposition: the Chapter 5 timing and Aeon gate findings are resolved, but the Devil branch still needs a source-state correction before integration review.

This review does not approve the prototype as an attainable all-path route, full route, or in-game-ready content.

## Resolved findings

**[Resolved] Chapter 5 timing now uses the native active-courtship state.**

All eight authored variants require `galfrey.native_active` and declare `Chapters=[5]`.

The alias maps to native `GalfreyRomance_Active`, GUID `c9358d866e0b3844b8d72536ca60e4b4`, instead of the Chapter 6 `GalfreyRomance_Finished` state.

The installed Chapter 5 preset `DrezenCapital_Chapter05GalfreyRomance`, GUID `7f1015d268e3c5048a64406cc4c35a84`, starts the Active etude.

This removes the prior chapter/state contradiction for a Chapter 5 continuation while an already-started native courtship remains active.

It does not prove an addon actor contact, area, queue reservation, exact trigger window, or post-Threshold availability; the report correctly leaves those unverified.

**[Resolved] Aeon's changed-history line is gated by the corresponding native state.**

The Aeon scene adds `galfrey.aeon_history_changed`, mapped to `MythicAeon_DrezenHistoryChanged`, GUID `998b505008f960a4b92e679fbd588098`.

Its authored opening therefore no longer asserts that every Aeon Commander changed Drezen's past.

The required history decision remains separate from consent.

**[Resolved] Trickster missed-courtship work is not presented as implemented.**

The Trickster scene still requires native Active courtship, so it cannot acquire a player who never started the native route or repair a rejected native date.

`TRICKSTER_MISSED_COURTSHIP_PLAN` marks the Chapter 3 Council access as unimplemented and lists the stage, contact, timing, rejection-history, and delivery evidence still needed.

The impossible-date decree is authored fiction, not a source-verified trigger, and the report says so.

This is honest scoping, but the user's required Trickster missed-courtship route remains absent.

**[Resolved] Lich romance-root behavior is described accurately.**

The installed Lich `Galfrey_Zombie/Answer_0004`, GUID `861d0e88764e1c249908b9ef60d55289`, completes the native `GalfreyRomance` root, GUID `133842cc9812fc74f88a21e12ec2c6f8`.

The report does not mislabel that action as starting `GalfreyRomance_Finished` or as proving a living, freely choosing romance continuation.

The revised prototype contains no Lich scene and leaves any restoration route unresolved.

## Remaining findings

**[High] The Devil scene does not exclude or account for Galfrey's native incompatibility outcome.**

The Devil variant requires both native Active courtship and `GalfreyRomance_AfterSexWithDevil`, GUID `e888c82ffc724a3b9ee041afb61408e5`.

Those conditions establish an active native courtship state and the earlier intimacy event, but the authored scene does not test whether the player has already taken Galfrey's Chapter 5 incompatibility branch.

The installed incompatible response is `World/Dialogs/c5/DrezenMain_C5/Galfrey/Cue_32.jbp`, GUID `b3b208e871cd49abacc81b1ea136c89d`, reached directly from `Answer_0011`, GUID `606acaa9e0674d0b89022b9f60966aa3`.

It says their paths will never cross again.

The authored Devil variant has no native cue-history forbid, no authored branch that acknowledges this separation and earns Galfrey's new choice, and begins with the player option, “I will answer as your partner, not as your commander.”

The shared continuation then has Galfrey say she has wanted this and invite the Commander to stay, which can read as resuming the affair after her explicit incompatibility response.

The generic `leave` option only exits this scene; it does not represent the existing native separation or condition access on its outcome.

Before integration, bind delivery to a source-backed pre-separation state or write a distinct, honest post-separation repair that gives Galfrey a fresh, unpressured decision and preserves her ability to end the relationship.

**[Medium] The development report gives the wrong blueprint path and GUID for the Devil incompatibility cue.**

It cites `Cue_0032`, GUID `5c6483b4911e4be4287d2f02260046fc`, as the explicit incompatibility conclusion.

That installed blueprint is `World/Dialogs/c5/DrezenMain_C5/Galfrey/Cue_0032.jbp` and contains Galfrey thanking the Commander for forgiving her.

The incompatibility text is on `Cue_32`, GUID `b3b208e871cd49abacc81b1ea136c89d`.

The underlying conclusion exists in the game, but the report's citation points to a different, conciliatory cue and should be corrected before later reviews rely on it.

**[High, scope] The prototype still does not meet all-path availability or route completeness.**

The source maps ten mythic paths but authors eight continuation scenes for an already active native romance.

It has no Lich or Swarm scene, no Trickster missed-courtship route, and no path-specific recovery for a dead or rejected Galfrey.

The source and report correctly disclose these gaps; they remain unmet project requirements rather than defects hidden by a passing structural check.

The module is unregistered, has no actor/location/contact contract, and is far below the 21,000-word character-route floor.

It has no independent full-route, art, runtime, ToyBox, or in-game approval.

## Focused checks and limits

The supplied source and report hashes matched the requested values.

`python -m py_compile storylines/galfrey_all_path_continuation.py` passed.

The module's structural check passed for ten path-map entries, eight scene variants, Chapter 5 plus native Active requirements, the Aeon changed-history requirement, the Devil aftermath requirement, and the absence of Lich and Swarm scenes.

Direct inspection of the installed archive confirmed the Chapter 5 preset starts native Active, confirmed the Lich Answer_0004 action completes the romance root, and resolved the correct Devil Answer_0011 to Cue_32 incompatibility branch.

These checks do not test an integrated export, path event reachability, the Devil response lifecycle in a real save, actor availability, scene scheduling, Unity behavior, ToyBox interaction, or save/load.

## Disposition

The Chapter 5 timing, Aeon state, Trickster scope labeling, and Lich root description are materially improved and source-consistent.

The Devil route still risks contradicting Galfrey's explicit native separation because the scene keys on prior sex and an Active etude without distinguishing the incompatible outcome.

Correct the Devil cue citation and add an outcome-aware gate or a fully authored separation-and-reconsideration branch before integration review.

Do not count this prototype as a complete route or ready it for manual in-game testing.

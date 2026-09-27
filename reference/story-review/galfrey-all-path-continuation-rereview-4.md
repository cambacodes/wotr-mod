# Galfrey continuation prototype independent rereview

Review date: 2026-09-27.

Reviewed source SHA-256: `B61086BFEA969F5C75F2E83F48687C79F84B2887BE592161AF03C96740D95A56`.

Reviewed development report SHA-256: `C50D2BA967E75F1B759BCCE52A7044FAE830184C7A53C12C7F5DB5E40197D923`.

Compared against `reference/story-review/galfrey-all-path-continuation-rereview-3.md`, SHA-256 `44F945CEC95EED72C0DFE1B3E626A01AEDAC2AE24BCC21C9AF77C88E41E25A87`.

Installed archive fingerprint: `BE61C9B723EF06558DA8D7CFC7F0C7EA869F60BA9952EBBBBD116CF681863EA5`.

I inspected the exact source and report, the two relevant Chapter 5 Devil cues, the report's prior findings, and current project registration points.

I did not edit the source, development report, or generated Story.

Disposition: the revised Devil seen-cue gate is correctly bound as a source-level contract, and the post-separation prose claim has been removed.

The prototype remains unregistered, has unresolved integration timing, and is not a complete or in-game-ready route.

## Rereview 3 findings

**[Resolved in draft] The incompatibility gate points at the correct cue.**

The native Chapter 5 `Answer_0011`, GUID `606acaa9e0674d0b89022b9f60966aa3`, points directly to `Cue_32`, GUID `b3b208e871cd49abacc81b1ea136c89d`.

That cue contains Galfrey's explicit statement that their paths will never cross again.

The source maps `galfrey.devil_incompatibility_seen` to that exact Cue_32 GUID and adds that alias to the Devil scene's `Forbids`.

The similarly named `Cue_0032`, GUID `5c6483b4911e4be4287d2f02260046fc`, is a distinct conciliatory cue thanking the Commander for forgiveness; the revised report correctly distinguishes it.

**[Resolved in prose] No post-separation reconciliation is implied by this scene.**

The Devil opening now describes a conversation before either character decides what must end.

The report explicitly calls this a pre-separation conversation and says the authored repair after the incompatibility response is still missing.

The source does not author dialogue that overturns Cue_32 or recasts Galfrey's separation as consent.

**[Still required] Do not mistake a correctly declared source gate for a live campaign gate.**

The `SEEN_CUES` mapping and scene forbid are internally consistent, but the Galfrey module remains unregistered: `expansion.py` does not import it or merge its `ETUDES` or `SEEN_CUES`, and the current generated Story does not contain these scenes.

Accordingly the exact-cue gate is correct in this prototype, not active in the shipped/current export, and has not been exercised against a live save.

The report otherwise identifies registration, scheduling, and native-dialogue reservation as unfinished integration work.

Before integration, retain the exact cue mapping and verify that native dialogue resolves the Answer_0011 to Cue_32 chain before an addon contact can be delivered.

## Other gates and scope

All eight scenes require native `GalfreyRomance_Active`, and declare Chapter 5.

The Aeon opening additionally requires `galfrey.aeon_history_changed`, mapped to the native `MythicAeon_DrezenHistoryChanged` etude.

The Devil scene requires both native Active and the `GalfreyRomance_AfterSexWithDevil` etude, then forbids the exact incompatible-cue history alias.

The Lich scene is still absent; the report accurately describes the native Lich answer as completing the romance root and does not treat that as a completed living romance.

Swarm is also still absent and is candidly blocked on proof of a voluntary restoration mechanism.

The Trickster variant still requires the native Active courtship and does not implement the separate missed-courtship route.

The Chapter 3 Council/fate access, native actor contact, map/area, interaction queue, and delivery timing remain unimplemented or unaudited.

The source map contains ten path IDs, but only eight path-specific continuation variants; neither Lich nor Swarm has an authored scene.

This is a small continuation prototype, not complete routes for Galfrey or all mythic paths.

It remains far below the required per-character content floor, unregistered, without reviewed art, full-route independent review, ToyBox testing, campaign integration checks, or a live in-game test.

## Focused checks

The supplied source and development report hashes matched the requested values.

`python -m py_compile storylines/galfrey_all_path_continuation.py` passed.

Focused structural assertions passed for ten path entries, eight scene variants, Chapter 5 plus Active gates, the Aeon history gate, the Devil after-sex requirement, and the Devil incompatibility forbid mapping.

Direct inspection of installed blueprints confirmed Answer_0011 leads to the incompatible Cue_32 and that Cue_0032 is a different, conciliatory cue.

Inspection of project registration points confirmed this prototype is not merged into the current export.

These checks verify source structure and blueprint identity only; they do not prove runtime cue history, saved campaign state, delivery ordering, or in-game actor availability.

## Disposition

The previous Devil state conflation is corrected in the revised source and report.

The cue-history guard is well-formed but remains a draft gate until the module and binding are integrated and tested.

No new source-level post-separation romance claim was found.

Do not approve full-route readiness or manual playtesting from this prototype.

# Galfrey all-path continuation prototype rereview

## Disposition

The exact prototype is a useful short writing exercise with path-specific opening lines and an agency-conscious shared conversation, but it is not an attainable all-path continuation or a route-ready manuscript.

Revision is required before integration review.

The most important defect is a chapter/state contradiction: all eight scenes require the native `GalfreyRomance_Finished` etude while declaring Chapter 5 availability, but the native finished state is started by Threshold answer `Answer_0028` in Chapter 6.

The eight scene branches therefore cannot appear in the only chapter window declared by this source.

The module has no Lich or Swarm scene, no missed-courtship or rejection recovery, no contact actor or location metadata, and no source-tested story adapter.

This rereview approves neither a complete Galfrey route nor art, path access, ToyBox behavior, or in-game readiness.

## Exact inputs and fingerprints

Reviewed `storylines/galfrey_all_path_continuation.py`, SHA-256 `3194D0CB5201EBB2D6B2647FBE6F228B18183AA845D0417B184AEF6FF99D71FF`.

Reviewed `reference/story-review/galfrey-all-path-continuation-development.md`, SHA-256 `03912BCB6AD55778C323BAEA8BB5E74A8880560A343ED8F8CE0FFCC7191F6856`.

Compared the current prototype against `reference/canon-review/galfrey-continuation-audit.md`, SHA-256 `090F2A65BC0B56EB8A4487017FD38C62B3AEC3D0831B5506BFAE0063CCD284CD`.

Also read `reference/canon-review/galfrey-continuation-independent-review.md`, SHA-256 `85C776575A275F77541BC0D1DB8BEA269628CD1C82A4D59A68D90B036A927BB5`, and `reference/canon-review/galfrey-continuation-rereview.md`, SHA-256 `D054E367E021018F7EDBD0B72ADC94B19C1FA61A6AFD4990252F1ADD15F0EBAD`.

The installed `blueprints.zip` fingerprint agrees with the pinned archive in those audits: `BE61C9B723EF06558DA8D7CFC7F0C7EA869F60BA9952EBBBBD116CF681863EA5`.

The source imports as eight scenes and 32 nodes, with 1,911 words across node text and 546 after exact duplicate-node exclusion, matching the development report.

The ten path identifiers in `PATH_ETUDES` resolve in the checked etude index to Angel, Azata, Aeon, Trickster, Demon, Lich, Devil, Dragon, Legend, and `MythicLocust` respectively.

## High-severity findings

**H1. Every declared scene is gated out of its only declared chapter.**

The scene helper sets `requires=("galfrey.native_finished", f"path.{key}")` and `Chapters=[5]` for all eight variants.

`galfrey.native_finished` maps to `GalfreyRomance_Finished`, native etude GUID `133f3b1b38f04fa44be3200b786e437f`.

The installed native `GalfreyThreshold/Answer_0028` (`cb9c857f03259f8479d5c30142d06825`) runs in the Chapter 6 Threshold dialogue and its `OnSelect` starts that Finished etude.

The pinned audit also identifies this Threshold answer as the romance-finalization point.

No earlier start for the Finished etude was found in the installed archive search; its other references are Threshold setup and epilogue conditions.

As written, Chapter 5 scenes cannot satisfy the Finished condition, and the module declares no Chapter 6 window.

Moving delivery to Chapter 6 still requires a verified Threshold contact window, since the native finale and ending lock leave no proof of post-confession free-roam availability.

**H2. The prototype does not provide acquisition for all mythic paths or missed native romance states.**

All eight implemented variants require a completed native romance.

The Trickster version is not a bespoke acquisition route for players who missed or refused the native courtship, despite the project's all-path Trickster requirement.

The authored path map itself marks Trickster's Council and actor-contact contract unverified.

Lich and Swarm have entries in the research map but no dialogue scenes, and the current source correctly labels both unresolved rather than pretending the romance survives their native outcomes.

This is accurate scoping, but it means the all-path requirement remains unmet.

## Mythic-path source audit

| Path | Native source evidence and review | Result for this prototype |
| --- | --- | --- |
| Angel | The native Chapter 5 duty cue `7a160960668f2ef4180cb56edb8388e9` includes Angel, while Iz attack answer `c383c70e3b946e24d836329436defa55` explicitly excludes Angel. | The code correctly gives Angel a variant, but survival, later living actor contact, and the Chapter 5/Finished gate remain unproven. |
| Azata | The audited duty cue does not include Azata; the shared Iz attack answer has no Azata-specific mythic selector. | That local selector does not prove an upstream Azata route to a living Galfrey or post-Iz interaction. The module notes this gap. |
| Aeon | The changed-Drezen-history response is Aeon-specific and its incoming branches require `MythicAeon_DrezenHistoryChanged`, Galfrey accompanying the Commander, and either polarity of `ReinforcedByAeon`. | The dialogue opening unconditionally says the Commander altered history, but the scene only gates on the general Aeon path etude. It should branch on the changed-history state or use a non-assumptive line. |
| Trickster | The native Chapter 5 duty cue does not include Trickster. The game has distinct Trickster Council stages, but their exact timing and actor reservation remain unverified in the audit. | The forged decree is clearly an authored premise, not native evidence. There is no Council-stage gate, forged-decree producer, source-backed contact window, or missed-romance entry. |
| Demon | The shared Iz attack answer excludes only Angel at that local selector, but upstream mission and hostility states determine whether it is reached and whether Galfrey survives. | `galfrey.dead` and `galfrey.killed_by_commander` are useful negative gates, but do not prove a current actor, absence of other hostility or rejection outcomes, or post-Iz contact. The scene's anger-specific opening is authored and has no state binding. |
| Lich | Native Lich answer `861d0e88764e1c249908b9ef60d55289` has `MythicRequirement=PlayerIsLich` and its `OnSelect` completes the native Galfrey romance root `133842cc9812fc74f88a21e12ec2c6f8`. The Chapter 5 Lich dialogue uses the zombie Galfrey actor, and the native `GalfreyDead` state counts undead as dead. | No scene is authored. A living romance continuation cannot be inferred from the native Finished state or a zombie actor. The source audit appropriately leaves any Trickster/Lich restoration idea unproven pending a real identity, body, soul, agency, and consent mechanism. |
| Devil | Native `GalfreyRomance_AfterSexWithDevil` (`e888c82ffc724a3b9ee041afb61408e5`) is a separate post-intimacy event, and the source audit records a later explicit incompatibility conclusion. | The prototype's Devil line asserts "we desire each other" and offers ongoing moments, but its entry checks neither the Devil aftermath nor the incompatibility outcome. The source-backed chance for intimacy does not establish a continuing affair or make the incompatibility disappear. Preserve an explicit boundary or end branch and verify whether the native Finished gate can occur after this path before treating the scene as reachable. |
| Dragon | The native Chapter 5 duty cue includes Dragon, while the shared Iz answer lacks a Dragon-specific exclusion. | This is path-dialogue evidence, not proof of survival, romance-finished state, post-Iz actor availability, or this scene's contact window. |
| Legend | The native Chapter 5 duty cue includes Legend, while the shared Iz answer lacks a Legend-specific exclusion. | This is path-dialogue evidence, not proof of survival, romance-finished state, post-Iz actor availability, or this scene's contact window. |
| Swarm | Native Iz answer `516217fafda9b194989bd3068289898e` is guarded by `PlayerIsLocust` and includes an action branch that starts `GalfreyDead`; its next cues include the explicit consumption outcome. The source audit also records Swarm coronation outcomes that describe Galfrey's death and consumption. | No scene is authored. The current death forbid rightly blocks a consumed/dead Galfrey; the ordinary path etude does not restore a living person. A fate intervention would need new, source-grounded identity and restoration evidence and her voluntary decision afterward. |

The path IDs themselves are plausible native path etudes, not proof that any specific route reaches this addon scene.

The exact local conditions and upstream survival/location graph remain separate questions, as the development report correctly cautions.

## Devil outcome and character fidelity

The Devil opener does not claim a harmonious lifelong partnership and acknowledges that Galfrey and the Commander may represent incompatible commitments.

That is a promising direction for authored adult conflict, and the native post-intimacy event means a sexual encounter is not an invented canon fact for every Devil save.

However, the variant universalizes desire across every Devil save that could meet the shared gate and does not model the native incompatibility consequence.

The native after-sex event's existence is not proof of an ongoing relationship, and a completed-romance flag must not be used to imply that Galfrey has renegotiated her stated boundary.

The line needs to be gated on verified history and should retain a real refusal, separation, or negotiated-limits consequence.

Across the eight variants, Galfrey's discipline, authority, deliberate speech, and distinction between duty and personal desire are generally recognizable.

The shared passage gives her initiative and an explicit non-romantic leave option, which suits the source's insistence that the Queen's trust and Galfrey's private choice are separate.

The path-specific voice is mostly confined to one short opening per path, while the rest of the scene is shared.

The Aeon opener currently violates its own path-state caution by assuming the Aeon history alteration regardless of whether that branch occurred.

The current scene is restrained affection rather than mature or spicy route content: a hand kiss, an invitation to wait, and no sexual intimacy.

That can serve as a small bridge, but it does not demonstrate the proposed adult relationship's full emotional or sensual range.

No score is assigned to a 1,911-word prototype, and this review makes no route-quality rating claim.

## Mechanics, consequences, and checks

No skill check or roll exists in the source, so there is no supported DC or dice outcome to approve.

The report accurately says that no check is included and that no check may override consent.

The `galfrey.prototype.respect` and `galfrey.prototype.wait` flags are written by choices but are not read by another authored scene in this module.

The two boundary responses converge on the same `end` node, and no later branch consumes the difference.

The departure branch aborts without a relationship flag, but its narrative text promises no penalty; no campaign cost or consequence is implemented.

These are acceptable prototype flags and endings only if they are described as local draft annotations, not persistent route consequences.

There is no actor GUID, AdditionalContactUnits, area, map hub, arrival timing, or quest reservation metadata on the scenes.

The inline comment admits that these are unverified, so the code is not yet deliverable to a runtime adapter.

## Prototype quality versus route completeness

The source has a coherent short emotional premise, eight distinct opening hooks, clean local scene topology, and a clear non-romantic exit.

Its content and research labels are appropriately candid about Lich, Swarm, Trickster contact, upstream Iz access, and unverified actor placement.

It remains an eight-scene prototype for an already completed native romance, not a complete route, all-path acquisition system, mature relationship arc, or end-to-end playable feature.

It does not meet the 21,000-word per-character floor, supply path-specific all-route entry, add reviewed art, prove consequences, implement a skill challenge, integrate into the export, pass campaign tests, or establish ToyBox behavior.

Before another review, resolve the Chapter 5 versus native Finished timing, correct the Aeon assumption, bind Devil to actual native history and its incompatibility consequence, and provide a credible Trickster access path that does not depend on `GalfreyRomance_Finished` if it is meant to repair a missed romance.

Keep Lich and Swarm explicitly unresolved unless new evidence proves a non-coercive fate intervention can restore Galfrey as herself and leave her free to refuse.

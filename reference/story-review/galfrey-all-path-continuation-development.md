# Galfrey all-path continuation prototype

## Status

This remains an unintegrated writing prototype, not a complete romance, a full-length route, or approval to test in game.

It maps all ten mythic paths and contains eight Chapter 5 variants for Galfrey states whose native courtship is still active.

The Trickster branch is not a missed-courtship acquisition route.

Lich and Swarm remain explicitly blocked pending evidence for non-coercive recovery and Galfrey's independent choice.

No all-path gate, full route-length floor, art gate, reviewer-score gate, or live-game test has passed.

## Corrected native timing

The previous version required `GalfreyRomance_Finished` in Chapter 5, which cannot work.

The installed archive shows the Finished state starts at Chapter 6 Threshold `Answer_0028` (`cb9c857f03259f8479d5c30142d06825`).

I changed these eight scenes to require `GalfreyRomance_Active` (`c9358d866e0b3844b8d72536ca60e4b4`), which the native etude comment defines as started and neither completed nor failed.

The installed Chapter 5 Drezen capital preset `DrezenCapital_Chapter05GalfreyRomance` (`7f1015d268e3c5048a64406cc4c35a84`) contains the Active etude and not the Finished etude.

That supports the declared Chapter 5 timing as an ongoing-courtship slice before the Chapter 6 native finale.

This repairs the chapter/state contradiction without inventing a new game chapter or claiming post-Threshold free roam.

Actor contact, scene reservation, and exact trigger timing still require integration review.

## Path-specific gates and evidence

| Path | Current prototype treatment | Evidence and unresolved work |
| --- | --- | --- |
| Angel | Chapter 5 variant requires native Active courtship and the Angel path etude. | Native duty cue `7a160960668f2ef4180cb56edb8388e9` includes Angel. The Iz attack answer `c383c70e3b946e24d836329436defa55` excludes Angel. Verify all other survival/failure states and an actor contact. |
| Azata | Chapter 5 variant requires native Active courtship and the Azata path etude. | The audited duty cue does not list Azata. The shared Iz attack answer has no Azata-specific selector. Trace the actual Azata path through Iz and post-Iz actor availability. |
| Aeon | Chapter 5 variant additionally requires the real `MythicAeon_DrezenHistoryChanged` etude. | This is the source state for Galfrey's changed-Drezen-history response. The scene no longer asserts the Commander changed history on every Aeon save. The history cue itself is not romantic consent. |
| Trickster | This variant only continues a native courtship that remains Active. | The separate `TRICKSTER_MISSED_COURTSHIP_PLAN` records the required Chapter 3 acquisition as unimplemented. It must distinguish never-courted from explicitly rejected history and cannot depend on Active or Finished. Verify council stages, prerequisites, queue reservation, map, and Galfrey contact before writing its mechanism. |
| Demon | Chapter 5 variant requires native Active courtship and the Demon path etude. | The shared Iz answer excludes only Angel locally, so Demon can have a Commander-initiated attack if it reaches that answer. The opening now addresses the path's force without claiming a specific past act. Trace upstream hostility and death states. |
| Lich | No continuation scene is authored. | Lich-only `Answer_0004` (`861d0e88764e1c249908b9ef60d55289`) completes the native Galfrey romance root. Chapter 5 then uses zombie Galfrey, and the Nexus state records her as an ex companion. The native dead state counts undead as dead. A future route first needs proof of a non-coercive mechanism restoring her independent will and a body or state from which she can accept or refuse. |
| Devil | Variant requires both native Active courtship and Devil aftermath etude `e888c82ffc724a3b9ee041afb61408e5`. | That etude is annotated as sex with Galfrey after Devilish Temptation. Chapter 5 `Answer_0011` (`606acaa9e0674d0b89022b9f60966aa3`) directly reaches `Cue_32` (`b3b208e871cd49abacc81b1ea136c89d`), where she says their paths will never cross again. The source exposes this cue as `galfrey.devil_incompatibility_seen`, and the Devil scene forbids that history. `Cue_0032` (`5c6483b4911e4be4287d2f02260046fc`) is a different, conciliatory cue. The current scene is a pre-separation conversation; an earned reconciliation after Cue_32 remains missing. Actual scheduling and native dialogue reservation still require integration review. |
| Dragon | Chapter 5 variant requires native Active courtship and the Dragon path etude. | Native duty cue `7a160960668f2ef4180cb56edb8388e9` includes Dragon. Trace Dragon-to-Iz outcomes, direct kill actions, active courtship, and actor availability. |
| Legend | Chapter 5 variant requires native Active courtship and the Legend path etude. | Native duty cue `7a160960668f2ef4180cb56edb8388e9` includes Legend. Trace the Legend transition, Iz outcome, active courtship, and actor availability. |
| Swarm | No continuation scene is authored. | Swarm-only Iz `Answer_0074` (`516217fafda9b194989bd3068289898e`) leads to `Cue_0034` (`0346a8715460fce4e9413ad16af4065b`), explicit consumption, and starts `GalfreyDead`. Swarm coronation cues also explicitly describe her death. A future route needs proof of a surviving soul and a credible restoration effect that returns Galfrey herself, followed by her independent choice. No such support is established. |

The shared Iz attack answer is locally available to every non-Angel path that reaches its answer list.

Its selector does not establish that every path reaches the same upstream scene.

Galfrey can also die through Iz mission outcomes independent of the Commander attack.

The complete path-by-path upstream death and location graph remains a required audit.

## Trickster acquisition boundary

The Trickster opener in this file is only a continuation for a previously accepted native relationship that remains Active.

It does not supply the requested bespoke Trickster route for a player who never started or who explicitly rejected the native romance.

The source-backed Chapter 3 invitation for Galfrey to attend the Commander's military and political council is a candidate place to build that route.

The forged decree in the short Trickster scene remains an authored premise without a verified producer or Trickster Council-stage trigger.

The acquisition work must establish a credible source-backed trigger and a voluntary new decision by Galfrey before any manuscript can claim missed-romance access.

## Content and mechanics scope

The eight authored variants share a short scene where Galfrey distinguishes public authority from private desire and states her terms.

She can continue the conversation, ask the Commander to leave, or choose company while she completes her work.

The Devil variant requires the native after-intimacy etude and forbids the actual cue-history flag for Galfrey's incompatibility response. It is a pre-separation conversation, not a reconciliation after her refusal. The source does not yet implement an earned path back after that ending.

The Aeon variant is gated on the changed-history state.

The scene does not award romance affection, reset native rejection, or promise a political consequence that has not been implemented.

The module leaves actor, area, interaction hub, council reservation, and trigger metadata unset because those contracts are not yet verified.

No skill check is included because there is no source-backed roll that establishes consent or overrides refusal.

## Independent rereview response

This revision addresses the Chapter 5 versus Finished-state contradiction by gating on the native Active courtship and matching it to a Chapter 5 preset that contains Active.

It gates Aeon's changed-history dialogue on the exact history etude.

It grounds the Devil branch in the specific after-intimacy etude, the Chapter 5 coexistence answer, and the explicit incompatibility cue.

It identifies Trickster missed-courtship acquisition as separate required work rather than describing an Active-courtship continuation as sufficient.

Lich and Swarm remain unresolved without a fabricated cure or resurrection.

In response to rereview 3, the Devil scene now forbids the exact seen-cue alias for `Cue_32` (`b3b208e871cd49abacc81b1ea136c89d`).

The current scene is available only before that native incompatibility response; no post-separation reconciliation is authored.

The report now distinguishes conciliatory `Cue_0032` (`5c6483b4911e4be4287d2f02260046fc`) from incompatible `Cue_32`.

The source archive check confirms `Answer_0011` routes directly to `Cue_32`.

The exact-source rereview of the prior version is `reference/story-review/galfrey-all-path-continuation-rereview-2.md`, SHA-256 `230579242B3CA584BD734C9026ECF462D29F641F6D9CD82E52D604722E405D85`.

The revised source still requires a new independent rereview. The latest review was `reference/story-review/galfrey-all-path-continuation-rereview-3.md`, SHA-256 `44F945CEC95EED72C0DFE1B3E626A01AEDAC2AE24BCC21C9AF77C88E41E25A87`.

## Fingerprints and checks

The source audit `reference/canon-review/galfrey-continuation-audit.md` has SHA-256 `090F2A65BC0B56EB8A4487017FD38C62B3AEC3D0831B5506BFAE0063CCD284CD`.

The installed `blueprints.zip` has SHA-256 `BE61C9B723EF06558DA8D7CFC7F0C7EA869F60BA9952EBBBBD116CF681863EA5`.

The installed English localization has SHA-256 `3289C3EBAB206BA6312D4C2D512C0B5623E52D7E2B86596074B81D355725AA75`.

The current etude index has SHA-256 `6687429FB6EB4A9B27E1F6AEF4053E33EBF929C80D5AE46F80DA762B500AB5E1`.

The shared story export has SHA-256 `866B7C66C2027AFEE471FD4C497F57CD173E2AE789814FB268FC5DA49A9249C2`.

Run `python -m py_compile storylines/galfrey_all_path_continuation.py` and a Python structural check after this revision.

The structural check verifies ten path audit entries, eight scene variants, all alias references, Chapter 5 plus native Active requirements, the Aeon history gate, and the Devil aftermath and incompatibility-cue gates.

No export build, managed tests, campaign scenario tests, save/reload tests, Unity rendering, or in-game test includes this unregistered module.

The current prototype is far below the required distinct-content floor and has no independent content or art approval.

It is not ready for manual in-game testing.

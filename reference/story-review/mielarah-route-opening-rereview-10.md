# Mielarah Route Opening Independent Rereview 10

This rereview checked `storylines/mielarah_route_opening.py` at SHA256 `5FA371CBFD1A882C80022019191AE49CB2FE77B1B86EAE709201BEB169AE07FA` and `reference/story-review/mielarah-route-opening-development.md` at SHA256 `9930C09A051B5D1091BD11662AF36844C03C24DE820794F01D775359C11F78AB` before review.

Both requested hashes matched before review and were rechecked after this report was written.

## Findings

The source compiles and its module-level checks pass, reporting sixteen unregistered scenes and 168 nodes with topology and cross-scene state checks valid.

The friendship-only correction is implemented in the authored gates: the outer-shoals friendship scene requires `friendship_only`, while the romantic outer-shoals, shore-week, and new-sail scenes forbid that flag (source lines 833-847, 868-896).

The departure choice sets `friendship_only` only when the player explicitly accepts the voyage as a friend, and the separate friendship scene offers either a platonic passage or staying ashore with correspondence (source lines 807, 836-847).

Its ending writes `friendship_correspondence_complete` without granting romantic future, date, or partnership flags, and the assertions verify those disjoint outcomes and block romantic scene entry even when romance flags are artificially present beside the friendship-only state (source lines 842-847, 1084-1094).

The R9 branch-state finding is resolved in this source model.

The seven-day shore scene still requires an open or deferred romantic ending and the 168-hour delay, while the distinct dawn departure does not set full-week completion and cannot reach the later sail contract (source lines 849-859, 1101-1117).

The Jori private-answer history remains split: the specific response branch requires the conversation with Jori, while a separate public meeting avoids attributing a private answer to him (source lines 797-805, 1077-1083).

The platonic voyage adds brief, appropriately restrained friendship content, but is much shorter than the romantic continuation and is itself only one small branch rather than a full companion arc (source lines 836-847).

The new sail scene continues Mielarah's self-direction through a contract she negotiates herself, a choice about whether the Commander participates, and partnership, deferred-future, or separation outcomes (source lines 860-896).

The gift and loan choices continue to distinguish practical help from romantic entitlement: the gift that implies a claim is refused, and the loan has written, repayable terms with no added access or influence (source lines 853-855).

The central character tensions remain legible: Mielarah is proud, direct, fallible, protective of her crew, capable of attraction, and not cured or absolved by romance (source lines 819-830, 853-896).

Her intimacy remains adult, sensual, and graphic and explicit, with her invitations and limits clear and the player able to remain platonic, leave early, or defer (source lines 853-859).

The route distinguishes native cues from authored alternate events: native evidence supports the Tumberd service exchange, storm crash, raid death, and curse context, while the pre-crash Trickster intervention, survival, later contact, voyages, relationships, and outcomes remain authored additions (source lines 12-21, 90-126; development report, “Chronology and native evidence”).

The ordinary contact hook and exact parent choice chain remain unverified, and the Trickster answer interception, native cue suppression, alternate campaign progression, survival persistence, and save behavior are unimplemented dependencies (source lines 12-21, 90-95, 141-158).

All ten mythic path entries remain unimplemented design plans, so this snapshot does not establish path-specific access, all-path availability, or missed/death/expulsion recovery (source lines 26-97, 1121 onward).

## Selected-path size and readiness

I independently traversed the authored gates and counted each node's text plus the selected choice text on valid scene-to-scene paths that reach the final authored continuation.

The modeled ordinary romantic path is 9,882 words through `new_sail_complete`, and the modeled Trickster romantic path is 9,569 words through the same endpoint.

The modeled platonic continuations are 7,977 ordinary-path words and 7,664 Trickster-path words through `friendship_correspondence_complete`.

These are explicit executable paths through this source graph, not registered or in-game transcript counts; each remains well below the project's hard 21,000 meaningful-word requirement for a complete character route.

The development report's total of 16,569 source words includes mutually exclusive options and cannot substitute for a selected-path length or a complete route.

All sixteen scenes are marked `ManualOnly=True` and `Remote=True`, and the source checks the ManualOnly/remote validator constraint (source lines 160-167 and module validation near the end of the file).

This validates the authoring format only; it does not prove native dialogue export, actual scheduler behavior, Mielarah's physical presence, or contact and flag production in the game.

No finished or independently reviewed art, registered export, live runtime integration, save/load check, ToyBox Free Love or No Jealousy compatibility test, or chronological in-game playthrough is demonstrated (development report, “Remote delivery and validator,” “Focused checks and measured scope,” and “Remaining work”).

The previous review scores are historical and do not apply to this exact snapshot; this rereview assigns no score and cannot certify the strict above-90 gate across applicable dimensions.

The friendship-only fix and shore-week correction pass their source-level checks, but all modeled routes remain under the full-route length floor, all-path access and native integration remain unimplemented, and the art, runtime, save, and ToyBox gates remain open.

Route and game readiness are withheld.

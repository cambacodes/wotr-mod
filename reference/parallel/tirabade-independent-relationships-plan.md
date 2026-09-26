# Independent Tirabade relationships implementation plan

Prepared on 26 September 2026 after reading the current 59-scene shared route, its previous assembled audit, the chronology correction, native dialogue evidence and the relationship engine.
This is a source-level plan, not approval of unwritten routes.
No story, engine, generated export or existing test was changed for this plan.

## Decision

Keep the existing `tirabade` relationship and its 59 scene IDs as the shared campaign.
Add `anevia` and `irabeth` relationship records for actual independent campaigns, using the existing relationship model.
Give each woman her own acquisition, consequence, campaign separation, commitment and endings.
The existing dual-affair route remains a consequential way into the shared campaign.
A new negotiated entry must reach developed shared content without fabricating either affair.
Declining a relationship with one woman or declining shared domestic life must not silently end the relationship with the other.

This requires substantial new played material.
Two local flags and an opening scene would fix neither the missing campaigns nor the per-character quality requirement.
The smallest sound engineering change uses the existing records and monotonic flags, while the writing work supplies the missing experiences.

## Reviewed snapshot and evidence

Current `development/Story.json` SHA256 is `926687FB240C1E17A565D820D8FFDC920C6E2DDC077B06A61561CB0214F6F41E`.
The canonical ordered 59-scene Tirabade subset, serialized with sorted keys and compact separators, has SHA256 `1D39FC2ADD23D95A4D42AB12701FF7BE6958F24234508C720A80B681F7ED9B75`.
Choice indices below are zero-based and refer to that subset.
The earlier assembled audit remains useful for its independent-route finding, but the later chronology overlay already corrected its fresh Chapter 5 return, shared-night and developed-loss complaints.
Do not reintroduce those old problems while adapting the entry history.

`src/Story.cs` already supports multiple relationships, independent closed and committed flags, explicit answer lists, native unavailability, optional scenes and conditional choices.
`Rules.Available` applies the selected relationship's closure and unavailable flags.
Its special chapter-four and paired-away handling currently applies only to `tirabade`.
`Rules.EntryTargets` similarly infers Anevia/Irabeth answer lists only for that relationship.
New individual scenes must therefore specify their answer lists, areas, chapters and physical contact requirements explicitly.

`src/Main.cs` derives the old `loss` flag from either wife's death or departure, or Commander sacrifice.
That flag is appropriate to losing the old three-person future but cannot mean that the surviving woman's independent relationship is over.
The new records must not use `loss` as an unavailable or failure condition.
The engine persists choice flags immediately, and scene completion separately, so important commitments belong on terminal answers or must be paired with a completed-scene requirement.
The engine does not need a new flag-clearing operation for this work.

## Relationship meanings

| Authored situation | Required meaning |
| --- | --- |
| One-wife negotiated romance | The Commander and that woman choose each other; her wife has a specific, played response to the proposed marital arrangement; that wife does not thereby become the Commander's lover. |
| One-wife affair | The actual involved woman and Commander have crossed a boundary without prior spousal agreement; confession and consequence concern that actual affair alone. |
| Two separate relationships | Both individual romances were earned; shared dates, a household or group intimacy still require a separate invitation. |
| Mutually agreed triad | Each Commander-wife bond was earned, the existing marriage remains real, and all three explicitly choose the proposed shared arrangement. |
| Group arrangement ends | The three-person arrangement ends; either individual relationship can continue only through its own explicit conversation. |
| Local refusal | That woman's romance ends or never starts; the other woman's willingness is not inferred either way. |
| Global refusal | The existing explicit decision to end the whole romance remains binding unless a later, separately authored reconciliation is deliberately offered. |

The wives already love and desire one another in native canon.
There is no need to invent their mutual attraction, and no justification for erasing their marriage to simplify an individual route.
The new work earns their separate attraction to the Commander and their decisions about changing that marriage.
Spousal agreement about one relationship is not romantic consent from the uninvolved spouse.
No heterosexual side romance is needed for these campaigns.

## Exact current failure points and safe insertion sites

| Existing location | Current behavior | Proposed addition |
| --- | --- | --- |
| `a_roof/friend/0` | Sets `closed` after offering friendship. | Preserve index 0 and its explicit route-wide meaning; append index 1 to end only Anevia's romance, setting `anevia.closed` and an explicit local-decline marker. |
| `i_respite/friend/0` | Sets `closed`. | Append an equivalent Irabeth-only terminal choice at index 1. |
| `a_crossing/leave/0` | Sets `closed`. | Append index 1 for local refusal and index 2 for a request to stop secrecy and discuss a negotiated relationship, each with distinct prose before its terminal result. |
| `i_crossing/leave/0` | Sets `closed`. | Append the same distinction for Irabeth, in her own voice. |
| `i_crossing/refuse/0` | Sets `closed` after the Commander demands loyalty. | Keep the refusal; do not turn misuse of command into automatic local acceptance or an immediate romantic retry. |
| `a_roof/danger` | Two existing answers, indices 0 and 1. | Append index 2 asking to speak honestly before crossing a boundary. |
| `i_respite/admit` | Two existing answers, indices 0 and 1. | Append index 2 asking for an honest approach involving her wife, without demanding an answer that night. |
| `a_crossing/choice` | Two existing answers, indices 0 and 1. | Append index 2 for the still-available negotiated approach before the kiss. |
| `i_crossing/wife` | Two existing answers, indices 0 and 1. | Append index 2 for that alternative before the kiss. |
| `a_morning/tell/0` | Earns `a_will_tell`; no independent confession follows. | A new Anevia-only disclosure scene reads the completed morning and this flag when the other affair has not happened. |
| `i_morning/tell/0` | Earns `i_will_tell`; no independent confession follows. | A new Irabeth-only disclosure scene reads the equivalent earned history. |
| `reckoning` | Requires both mornings and both affair flags. | Preserve these gates and this account of two betrayals; do not reuse it for one affair or negotiated entry. |
| `a_truth/stop/0`, `i_truth/stop/0` | Set `closed` and `parted_honestly`. | Preserve global endings; append a local parting choice after a new response acknowledging that the other bond remains undecided. |
| `table/proposal/2` | Declining the group proposal leads to global closure. | Preserve it; append indices 3 and 4 to ask about continuing with Anevia or Irabeth separately, and index 5 to discuss separate relationships without a shared household. |
| `table/stop/0` | Ends the entire route. | Do not silently reinterpret its old saved result as a local refusal. |
| `future/choice/1` | Declining a joint future leads to global closure. | Append individual or separate-future requests after indices 0 and 1; play the response rather than award continuation immediately. |
| `parting/start/0` | Confirms ending the whole romantic relationship. | Append requests after existing indices 0 and 1 to end the group arrangement or one individual bond; retain the original global confirmation. |

New choices must use clear local or group scope rather than the existing ambiguous word "route".
The old answer arrays remain exact prefixes, and existing IDs remain unchanged.
If an old terminal label is clarified to say both relationships, its persistent meaning must remain the same.
Do not force a player through friendship-refusal prose to ask for honest courtship; the earlier insertion sites are necessary.

## Persistent state and save compatibility

Use `anevia.started`, `anevia.closed`, `anevia.committed` and the corresponding Irabeth flags as the new record fields.
Suggested additional historical flags are `anevia.courtship_requested`, `anevia.lover`, `anevia.marital_terms_agreed`, `anevia.local_declined`, and their Irabeth counterparts.
Only write each after the actual conversation has earned it.
Keep the existing `a_affair`, `i_affair`, disclosure and heard flags as evidence of what happened.
Never replace them with claims of earlier agreement.

For new individual scenes, use that woman's native death and departure in `UnavailableFlags`, plus the existing incompatible Swarm and true-Lich states.
Use her own death/departure and the applicable Commander-ending conditions in scene-specific ending gates.
Do not put the other wife's death into the surviving woman's global unavailability.
Ordinary spouse-present scenes must still explicitly forbid the other wife's death, departure or physical absence when their prose requires her.
Bereavement, uncertain whereabouts and a living spouse elsewhere need their own truthful continuations, not the ordinary intact-marriage text with a gate removed.

Keep `closed` as the legacy global decision and forbid it on normal new acquisitions and continuations.
This preserves old explicit global refusals.
Append local choices for future play instead of guessing which wife an old `closed` save intended to reject.
Do not auto-clear `closed`, `parted_honestly`, `committed`, completed scenes or timestamps.
A later reconciliation for a globally closed save would require a separate intentional scene and scope decision, not a migration side effect.

Introduce a distinct `tirabade.group_closed` marker for new explicit group dissolution.
It prevents further joint romance, while leaving surviving individual records open.
Add it to relevant shared-scene and shared-ending forbids through one integration overlay.
Do not set old `closed` merely because the group arrangement ends.
A "not now" answer should abort without recording permanent refusal.
Do not promise unlimited reopenings until their chronology is written and tested.

The existing first five Anevia scenes and first five Irabeth scenes remain legacy acquisition scenes under `tirabade`.
Add the corresponding local-closure forbid to each woman's acquisition chain so it cannot restart after her new local refusal.
A negotiated individual entry also suppresses that woman's still-unplayed secret crossing; it must not let an agreed relationship subsequently become a purported first clandestine affair.
The other woman's acquisition remains eligible under her own guards.
For old saves already in `trying` or `committed`, offer an optional personal continuation that acknowledges the actual triad before writing new local markers.
Do not require replaying attraction or confession, and do not create local romance markers merely because a new version was installed.

## Reach developed shared content without fake affairs

Write a new `tirabade.negotiated_table` scene after both independently earned bonds and a specific invitation.
It supplies new agreement prose and sets the existing `trying` only when all three have actually chosen to try a shared relationship.
It does not set `a_affair`, `i_affair`, `reckoning`, `a_truth`, `i_truth` or the old `table` completion.

Change `ordinary` from requiring `table` and `trying` to requiring `trying` plus `RequiresAny = ["table", "tirabade.negotiated_table"]`.
The same explicit alternative can admit the existing Chapter 3 `departure` scene.
This preserves real old-table history and provides a real new-table history.
After `ordinary` actually earns `kept_terms`, the existing developed visits have a legitimate common starting point.
No fabricated global "all prerequisites satisfied" flag is needed.

At minimum, the following played text needs entry-history variants before that join is accepted:

| Location | Why a negotiated entry cannot use it unchanged |
| --- | --- |
| `ordinary/rank`, reached by `ordinary/start/1` | Anevia says they should have kept sneaking around. |
| `return/back`, reached by `return/now/1` | Anevia explicitly recalls hiding and excuses. |
| `future/choice`, reached by `future/own/0` or `future/others/0` | Irabeth discusses making what happened less shameful. |
| `future/yes` | Its account of learning the harm they could do needs checking against actual history rather than assuming the double betrayal. |
| `ending_aeon/end` | Explicitly says there was an affair to confess. |

Use truthful shared wording where it preserves both histories, or append history-gated variant nodes while preserving original answer indices.
Keep the original betrayal response available when the actual affairs occurred.
Add a negotiated Abyss reflection under its own ID rather than satisfying the current `abyss_letter` requirement by inventing two affairs.
A player must not receive two accounts of the same letter or duplicated farewell because both branches are now installed.

Audit all nine shared endings for the new entry and group-dissolution states.
Several unfinished, loss, monster and Aeon endings currently require both affair flags; negotiated relationships therefore need properly gated equivalents.
The developed and provisional shared endings must remain distinct.
An individual ending must not accompany a contradictory shared happy ending, and closing the group must not display the old claim that both individual romances ended.
`Rules.Available` returns for epilogue owners before applying the relationship record's closure and unavailability checks.
Every new individual ending therefore needs explicit scene-level local-closure, native-state and shared-ending arbitration conditions; a correct relationship record alone will not protect it.

## Full individual campaigns

Each campaign needs a meaningful personal path through acquisition, reciprocal attachment, conflict, campaign change and an earned ending.
Target the existing per-character aggregate planning floor of at least 21,000 distinct readable words for each wife and at least 42,000 distinct words across the combined campaign.
The floor is not a selected-playthrough quota.
Measure actual selected paths separately, without adding alternative endings or crediting unreachable shared scenes.
The existing approximately 46,000-word shared inventory already passes the combined aggregate floor, but it does not certify either missing independent campaign.

### Anevia

Build a substantial individual sequence around her choice to share a life without surrendering every secret or becoming the Commander's informant at home.
An initial honest invitation should occur during a practical outing of her choosing, with a distinct response to being wanted as a woman rather than thanked as a rescued scout.
Her wife must respond in a played scene to the proposed change in their marriage, with time to think and a possible refusal.
The Commander can accept that limit, continue an explicitly chosen affair with its consequences, or part; the engine must not manufacture agreement to keep a route open.

Use an intelligence problem in which protecting a civilian source conflicts with public credit or a convenient public explanation.
Let Anevia decide what she will disclose, and let the Commander's chosen investigative approach change the evidence or risk.
A real Perception or Trickery check can uncover information, with a costly but credible non-roll route and a failure continuation.
Affection must not be the prize for passing the check.
Follow the outcome with an ordinary desire she initiates, a disagreement about access to her time, and a repair that changes later behavior.

Include a Chapter 3 departure and Chapter 4 unsent account only when their relationship predates the departure.
Chapter 5 fresh starts need current courtship, not a manufactured romantic absence.
When Irabeth is away, Anevia can want the Commander while refusing to make them a substitute for her wife.
When the native history proves Irabeth dead, grief and any later recovery must recognize that actual loss rather than remove the spouse as an obstacle.
Her own commitment and final watch should be reachable without Irabeth becoming the Commander's lover.

Plan roughly 15-19 substantial individual visits, including at least one multi-scene professional consequence arc, rather than 15 interchangeable conversations about boundaries.
Allocate about 4,000-5,000 distinct words to acquisition and marital consequences, 6,000-7,000 to the played intelligence arc and its personal consequences, 4,000-5,000 to ordinary reciprocity and disagreement, and 5,000-6,000 to campaign change, developed commitment and alternative endings.
These are authoring budgets to be checked against actual meaningful content, not guaranteed scores or required filler.

### Irabeth

Give her a different acquisition pressure and desire.
She can deliberately ask for time in which her preference matters without treating military obedience as affection, or interpreting morale damage as permission for somebody to rescue her emotionally.
Her conversation with Anevia must preserve the marriage's real affection and Anevia's own judgment.
The Commander should have specific opportunities to admire, disagree with and be surprised by Irabeth, beyond repeatedly reassuring her that she deserves happiness.

Build a played Eagle Watch problem in which Irabeth must choose how to treat a useful officer, a harmed civilian and an imperfect record.
The Commander can investigate testimony or discuss law and custom, with a genuine fitting check, a failure outcome and an alternative approach that costs time or cooperation.
Irabeth owns the command decision.
Its public and private consequences should affect later scenes, including whether she lets rank end a difficult conversation.
Give her a personal activity she wants for its own sake and a moment when she initiates affection without asking the Commander to certify her worth.

Read actual broken/encouraged, Commander-violence and Iz histories before writing their responses.
Pleasure is compatible with distress, but a lover's reassurance must not silently complete native morale recovery or erase the Queen's death.
A living Anevia remains part of Irabeth's life even if she declines Commander romance.
Absent or dead Anevia needs separate uncertainty or grief material, with verified contact before any recovery reunion.
Irabeth's developed commitment and ending must be available independently of a triad proposal.

Use a comparable 15-19-visit campaign and 21,000-plus distinct-word planning budget, but a different dramatic structure and professional conflict.
Do not mirror Anevia's scene beats with names exchanged.

## Reuse and limits of current material

| Existing material | Safe reuse approach |
| --- | --- |
| `a_cup`, `a_errand`, `a_roof`; `i_watch`, `i_hands`, `i_respite` | Reuse completed acquaintance history and genuinely compatible dialogue; new late-start entrances acknowledge those records without replay. |
| `a_crossing`, `a_morning`; `i_crossing`, `i_morning` | Preserve as actual affair history; route to the correct one-affair or two-affair consequences. |
| `a_self`, `i_self` | Strong personal-date foundations, but currently gated by `ordinary`; create individual-context variants with correct props and intimacy milestones rather than copying the entire scene and counting it twice. |
| `a_waiting` | Useful model for refusing substitution while Irabeth is away; its present requirement for `a_affair` and shared relationship means new negotiated access requires its own honest join. |
| `three_anevia_flour`, `three_beth_score` | Depend on the played match and shared history; adapt only after an actual match variant or write a different individual activity. |
| `three_lantern_debt`, `three_beth_steps` | Depend on stolen-book consequences, preparations and shared attraction; cannot be unlocked by claiming those events occurred. |
| `three_back_of_seal`, `three_beth_account` | Useful professional methods but tied to the borrowed-name investigation and joint victims; a one-wife campaign needs an authored case setup and changed resolution. |
| The 20 developed shared visits | Reuse intact for a legitimately negotiated triad after the corrected common join; they are not automatically accessible individual-route word credit. |

Where both women attend a professional or social event during an individual romance, the unromanced wife can be a spouse, colleague or friend.
Her presence must not produce unearned Commander kisses or collective bedroom scenes.
Variant writing should preserve her independent role rather than remove every line in which she matters.
If a reused passage appears in two source branches, deduplicate it in the combined inventory.

## Canon, access and compatibility

Native `Anevia/Cue_0016` through `Cue_0020` establish rescue, immediate love, domestic conflict and the importance of Irabeth's purpose to Anevia.
Native `Irabeth/Cue_0019` through `Cue_0027` establish her background, prejudice, faith, rescue of Anevia and their work against the cults.
Native `Anevia/Cue_0044` and `Cue_0045` require attention to the Commander's violence and Irabeth's scar.
Native `Irabeth/Cue_0197` supplies the defeated response after the Queen's death in Iz.
Threshold `IrabethAnevia_Threshold/Cue_0015` through `Cue_0017` distinguish desired vacation, confident enjoyment and doubtful survival.
These records are in `reference/canon-dialogue.txt`; new cases, agreements, dates and romances are authored alternate developments.

Anevia's personal history belongs to her.
Do not make disclosure of her transition or private medical history a reward the Commander earns for completing a romance stage.
Preserve recognizable half-orc Irabeth and adult Anevia in art according to the current attractive humanized brief.

Trickster recovery is a separate required campaign task, not solved by these new relationship records.
Research the actual death, departure and Iz branches and original actor identities before designing fate interventions.
Retain historical native flags, confirm living physical contact and let each woman respond to the consequences.
Other mythics retain appropriate restrictions.
Do not use a resurrection flag to infer the original actress is present, or clear a wife's refusal through mythic power.

Free Love and No Jealousy compatibility means unrelated partners remain possible and their native/parent flags remain untouched.
It does not mean broken promises, deception or commanded obedience become harmless, or that either wife must accept every proposal.
The narrative should distinguish a concealed affair from an agreed additional relationship explicitly.
Keep the parent's existing Anevia dispatcher, invitations and native answer-list choices intact.
Before integration, audit their exact installed states and establish whether an existing parent romance needs an acknowledgment or exclusion, rather than opening two contradictory first romances.
This plan has not proved a parent-route merge contract.

## Engineering ownership and verification

Root should own `expansion.py`, shared registration, generated exports and changes to `src/Story.cs` or `src/Main.cs` if needed.
A single bridge author should own a new `storylines/tirabade_independent_bridge.py` overlay and its focused tests.
That overlay owns old-scene answer append operations, local suppression, the negotiated shared join and shared-ending arbitration.
Separate authors may own `storylines/anevia_independent.py` and `storylines/irabeth_independent.py` with their own tests and evidence, never editing each other's files or the old shared modules.
New optional art and native-recovery research should have separate ownership when scheduled.
Keep no more than three workers active and use an independent reviewer for released prose and joins.

The relationship split itself needs no engine feature or derived per-wife flag.
New physical scenes must use explicit answer lists `33960c7f7af40cd43b7f801a76c87a0b` for Anevia and `871af36f2ab2b1f40b5de77976c54276` for Irabeth, plus independently verified actor contacts.
Do not invent unit GUIDs from the dialogue lists.
The current scalar `ContactUnit` cannot prove both actors in a shared scene.
If the paired-contact audit confirms that both must remain physically present throughout a book event, root should implement a small all-required-contacts field using the existing native-contact guard rather than weakening its uniqueness or loaded-view checks.
That is a distinct delivery change with focused interruption tests, not a reason to delay writing independent relationship states.

Start the implementation check with the actual existing local-friendship path that sets global `closed`, then show the new local alternative preserving the other woman's playable continuation.
Keep the old global-refusal test passing; add a different expected result for the newly appended local choice.
Do not change an old test to call the same global decision local.

Required played histories include Anevia-only and Irabeth-only negotiated acquisition through developed endings, each single-affair disclosure, both orders of individual courtship, a triad accepted after negotiation, a triad declined with either individual relationship continuing, and group dissolution after established intimacy.
Also cover legacy shared saves at `trying`, `committed`, short farewell and developed capstone, fresh Chapter 5 starts, individual and paired absence, proved death, incomplete pages, saved local refusal and saved global refusal.
Verify that no new path sets an affair it did not enact, commits the unromanced woman, clears native morale, completes an unplayed old scene or modifies another lover's flags.
Check each ending set for contradictory simultaneous outcomes.

Run the retained full legacy Tirabade tests and new actual-path tests, then review assembled selected reading paths independently.
Report per-wife accessible distinct content, combined deduplicated content and selected-playthrough ranges separately.
Passing the 42,000-word combined floor does not close the task until both individual campaigns and the optional triad work as written.
Art, loaded actor contact, book-event display, parent integration and real saved-game continuation need their own evidence before release.

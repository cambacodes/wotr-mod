# Nocticula Trickster acquisition and recovery map

The strongest first implementation is an earned Chapter 5 renegotiation following the native Trickster audience, with separate histories for missed romance, explicit rejection and lost patronage.
Native scripts also establish communication with Nocticula after the game records her death.
They do not establish that her body, throne or parent romance has been restored.
The current continuation cannot simply admit every such history without revising its entry contract and some dialogue.

This is a research and implementation proposal, not an implemented acquisition route or approval of recovery.
All proposed interventions below are authored additions unless explicitly identified as native evidence.
No source, asset, shared planning file or game state was modified.

## Fresh evidence inspected

I read native JSON directly from the installed `blueprints.zip`, resolving dialogue through `Wrath_Data/StreamingAssets/Localization/enGB.json`.
The installed parent DLL and localization hashes still match the earlier decompilation audit:

- `RanRomance.dll`: `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
- `LocalizedStrings.json`: `534D49567F0172193CD78F9C56A7A9A8244021F1701E2EC46F0C04FDBFBBCF3F`.

I reread the decompiled `RanRomance.Noct.Main` and Book 2 acceptance conditions in `C:/Users/Z/AppData/Local/Temp/nocticula-audit-8d261252/`.
The broader parent topology remains documented in `nocticula-parent-extension-audit.md`.
I inspected current `src/Story.cs` and `story_format.py` for supported bindings, predicates and effects.

I also read actual Unity scene objects with the existing UnityPy interpreter, without editing or exporting the bundles:

- `thresholdindoor_mechanics.scenes`: `0AD0377D8623420317B6EA567FA76F8131E50A8D2950F121D332F089AEECBB15`.
- `nocticulasboudoir_default_mechanics.scenes`: `3FE436ACA33078312A6EB17D2B086144B713154979CA19AAC7094C01D95A3203`.

Additional named-object searches in the base boudoir and its Vault of Graves mechanics did not establish a persistent free-conversation Nocticula contact.
Those searches are not proof that no dynamically spawned actor exists.

## Parent entry is an actual agreement

| Producer or condition | Verified binding | Consequence |
|---|---|---|
| Parent Chapter 4 dinner | Dialog `a0741b09599b4ef2a9958ddd92dbc022` | Optional earlier encounter, not required history to invent for a late entrant |
| Initial intimacy | Etude `8a28bbd82568486bb757d00a2087a6cf` | Separate from the Chapter 5 active agreement |
| Parent refusal | Etude `761ca3572c1145ebb755032d613bff46` | Blocks the original dream invitation |
| Parent Chapter 5 offer | Dialog `d171314b3b4b4b32bdd83ec31027a8f2` | Starting it is not acceptance |
| Ordinary acceptance | Answer `e742f8f2102f438980258d9ae5cdeb40` | Starts active romance |
| Acceptance including Laulieh | Answer `dd85f9d8961b401f80805a7d27f53221` | Starts active romance and separate participation state |
| Active parent agreement | Etude `18affced672d4c56a52bf6ffc00601b9` | Has RanRomCount start/completion bookkeeping |
| Actual agreement cue witnesses | `631bf0ede36742559cee476f34dcb5de`, `cb13766be07b448f8cacb477be32e13c`, `5388a7d7a1da48deb333d34abab1a6d0` | Current continuation uses these alongside active state |

Book 2 acceptance answers require the preceding questions `a45f3add1dd9451099a8092245f6d5ea`, `2c7b639af94c40c68c9066edb6595185` and `632c01a393f8499390803013cbbaf17a`.
The Laulieh answer additionally requires `c8e013f26c6345328147a1019e7d76dd`.
A new contact must not mark these questions or answers as played when they were not.

`Noct.Main` adds camping encounter `c6c201b6c23f4c0fa89fc3af5c2deec5` from summit cue `5baed9197e5992045bda712cff673343`.
The encounter requires original ProfaneGift, no NocticulaDead, no parent Reject, no completed Lich final quest, no Swarm class, no selected answer `f165187fb9d7f9144a00f9ae7f4cd617` and no seen cue `2536ce7031d04354fbfb202ffb652a7d`.
It removes itself when it starts the offer dialog.
An interrupted dialog can therefore differ from an encounter never offered.
Replay requires an explicit recovery design; blindly registering the camp event again can duplicate or misrepresent an agreement.

The later parent dream also requires the parent mythic milestone, Ember's persuasion flag, active relationship and Book 2 history.
Missing that later scene is not proof that the basic agreement never existed.
The new acquisition should not manufacture Ember persuasion or disclosure of Nocticula's ambition.

## Gift recovery: two native etudes, one granted fact

| Native object | GUID | Observed behavior |
|---|---|---|
| ProfaneGift | `0c1695f4a362f0243a4afcfd1957eb0d` | Play adds fact; completion removes it |
| ProfaneGiftNew | `f5be7095af9d43779ce79a52ec27425d` | Separate renewed-gift etude with the same add/remove fact |
| Granted fact | `656e71ec777e495abc6845ff80204d96` | Referenced by both etudes' actions |
| Original refusal state | `0383369136fadc247b7d6ff99110fa55` | `TakeNotProfaneGift` identity, not romance refusal |
| Broken-gift outcome | `61b07b3511bb71646a717c2b3c0f3bf6` | `Nocticula_GiftBroken` identity |

In `World/Dialogs/c6/FirstFloor/NocticulaThreshold/`, leaving through Answer_0011 (`fc435b0631e6a874db057164204db70a`) uses an ordered cue list.
First it handles the hostile Swarm conversation; then an active original Gift; then completed original Gift; then never-started original Gift.
Cue_0013 (`5fc9c28384bd9a84c80ba2e038a9e284`) offers the gift again when the original etude is Completed.
Cue_0027 (`7010a76297d261c45a3ce4c46044e8a4`) offers it when the original etude is NotStarted.
Acceptance answers `f0aa0ec928cafe24fa926662bbcba7ec` and `c65e55951e8e1964f903f2992d77b591` lead to Cue_0019 (`ace192bfb45fcdc4784a9ba39f0a292e`).
That cue starts ProfaneGiftNew if the original was completed, otherwise ProfaneGift.

This is a concrete native precedent for reconsidered patronage.
It is not an implemented Chapter 5 romance recovery.
The current continuation and the parent camping conditions read the original Gift, so the renewed etude alone does not satisfy their original predicate.
Threshold is also too late to serve as an ordinary producer for 24 delayed Chapter 5 visits in Drezen.

Cue_0039 (`66248e33df6bf83429bd1336487f9504`) expressly describes the Gift's interference with disobedience.
A renewed romance must not portray gift acceptance, an induced action or technical access to dreams as proof of freely chosen attraction.
Keep an authored contact channel separate from a stat-granting Gift if the player negotiates communication without patronage.

## Native Trickster audience and its limits

The Chapter 5 audience is `World/Dialogs/c5/Mythic_Trickster/Nocticula/Nocticula_TricksterC5_Dialogue.jbp`, GUID `2c57f65d4b98d764d98794ae8ef9ffdd`.
Nocticula recognizes the trace of her brother's enchantments and demands the real reason for the intrusion.
Her questions and refusal to accept a casual excuse provide a stronger character basis than a newly invented easy invitation.

Disclosure answer `fd4f6c1d6397fa94db7aaf08de7dfeca` starts `NoctaWillAttendTheCouncil`, `8ee3df5466722b94091a3b867b33063a`.
Its response `bb552fe4e21cb874fa3c98c2cc328186` promises a reward and a confrontation with Socothbenoth.
That gives a concrete earned opening for a later request, not a romantic entitlement.

Permission to attack Shamira (`7cad8bc19e70de14287f638baa6f1a8e`) and acknowledgment of her death (`84df3b227f54e3e44888b5bb8585089d`) are different witnesses.
The death-report answer requires `ShamiraKilled`, `dd6731e2cb230694f9c394fa32391ad5`.
An acquisition that keeps Shamira alive must not use the death response as its proof of service.

The audience's departure cues teleport the party and hide the specific portal `236a7b03-a709-4f89-a2eb-e642531de492` in scene `d6e96d5768d31604f87957f8c81e9408`.
Do not assume the audience remains a reusable shop-like contact after departure.
An answer-list insertion can offer to request future contact while that conversation is genuinely available.
A later addon request must supply its own delivery instead of teleporting the party into an assumed permanently accessible palace.

## Death is not the end of native communication

`NocticulaDead`, `e581f609dc0f44a481e7e88824ac39da`, is an important lifecycle signal.
The parent adds a play trigger completing Active and all three Laulieh participation states.
It must remain in history, with those consequences preserved.

There is an additional complication: `FightAgaintsNoctaCouncilAllied`, `ed5d1dfa2402bed4cb7a59a21c14a1a4`, starts NocticulaDead in its own play trigger.
Council_5-2/Cue_0049 (`1643731eb71ab0f4db2c405b0800c27d`) starts that fight state when arranging the battle.
Consequently, NocticulaDead alone is not a reliable observation that the retained actor has already died.
The Council fight etude `ce1d29b444c5f624dbe558ab89b78950` also has real death triggers for its dressed and combat Nocticula spawners.
Their IDs are `e2d7dd23-1d50-4bd3-9ee4-b75c816473de` and `2eaf1703-7399-4c97-8c89-49d345ba369e`, both in scene `f27a4963ef47d354ab2e091cff67ab5f`.
Recovery must distinguish a pending fight, an observed kill and an already resolved political outcome.

The native Threshold conversation explicitly accommodates a Commander boasting of having killed her.
Answer_0054 (`f7cc6463bec3c5f44b1b34e35718f3d9`) requires either the Demon aftermath dialog `f04058bf589cf0f438f85728c4c2af7a` or the Trickster fight state above.
Cue_0055 (`2e8da73cd0e96ed4bac54fc5d71f8a10`) handles the Demon history; Cue_0056 (`77216dc2c3770794f93b010659f4aa64`) supplies the Trickster response.
She remains hostile and interested in the outcome against Areelu.

This dialogue has a real native trigger, not merely an unused localized line.
In `thresholdindoor_mechanics.scenes`, `NocticulaThreshold_SZ` is a one-shot player trigger, unique ID `c0bcaae3-b10b-4ee6-b4c1-e1f048aad84d`, pointing to blueprint `dc11d8f4369d4cf9af406130ede05c68`.
That blueprint has empty trigger conditions and plays cutscene `737272eaa6cf4dd3bf53af6aed8654c2`.
Its actions spawn `7557e2e0-d2aa-442e-951d-f15adf5c4e2c`, then start dialog `d8ba4c5d73f3e634f951485914179bd3`.
The spawner uses Nocticula unit blueprint `0cca8c841d634d84fbec2609c8db3465`, has scene-init spawning and respawn-if-dead disabled, and runs spawn actions `6bd45f37218bd684987cebb2bfa946f6`.
Those actions attach `ProjectionBuff`, `c057f62e21250dc4fa809edd8dce6e1b`, and set the cutscene-neutral faction.
The second-floor spawn action `9ea132abbbf1456f95f529f9dc4440ee` likewise specifically attaches ProjectionBuff when NocticulaDead is playing.

The defensible conclusion is post-death projection/contact, not body resurrection or restoration of Alushinyrra's government.
An earlier Chapter 5 version of that communication would still be an authored intervention.
The earlier audit's statement that no return event was established should not be read as claiming no native post-death communication exists.

## Proposed attainable Chapter 5 chain

The following is a concrete authoring contract, not existing canon or engine behavior.
An attainable route means prepared choices can earn it; it does not mean every answer or renewed refusal must end in romance.

1. **A request under the right name.**
   At the genuine native audience, offer to request a second meeting after supplying truthful intelligence.
   Later Tricksters who missed that opportunity receive an addon correspondence task tied to the Council affair and their recorded choices, without claiming to have disclosed a secret they concealed.
   Its initial purpose is to obtain an audience, not recover romance immediately.
   Characters with the accepted parent agreement keep their original route and skip reacquisition.

2. **Something she cannot get by threatening you.**
   The Commander reconstructs the competing Council demands and offers a verifiable concession: disclose a surviving vulnerability in the Council scheme, surrender a specific bargaining advantage, or secure a replacement for a political loss they caused.
   A previous refusal changes the conversation: the Commander acknowledges it and offers changed terms; Nocticula asks why she should trust a second arrangement.
   A Commander who fought her must account for that choice rather than claiming loyal service.
   She may demand an expensive, enforceable limit and remain angry throughout cooperation.

3. **The living-Shamira problem.**
   If Shamira lives, negotiate an authored bounded contribution of essence in exchange for a concrete concession between the rival rulers and the Commander.
   Nocticula wants the succession threat contained; Shamira wants leverage and survival, not gratitude for being permitted to exist.
   A three-party bargain can leave hostility intact while providing the quest material without murder.
   Extraction should weaken or constrain a specific capability until a later obligation is met, with an explicit refusal/failure branch.
   The Trickster's intervention distinguishes a usable contribution from extinguishing its source; it is a prepared alteration of this ritual, not universal fate control.

4. **The price of a private channel.**
   Offer either native-style patronage with its acknowledged power or an authored limited communication pact.
   The independent channel gives no ProfaneGift stat fact, domination immunity or unrelated magical benefit.
   It permits invitations rather than access on demand, and either party can end a particular meeting.
   Arcana or Use Magic Device can reduce exposure or cost after preparation; failure requires a second, distinct research/concession step rather than repeated rolls on the same page.
   Use supported skill identifiers and one-shot branches, with an expensive prepared fallback so a single failed roll does not make the advertised Trickster route impossible.

5. **An agreement about the Worldwound.**
   If the player intends the native-style closure bargain, explicitly negotiate it before the shared continuation.
   A planar-crossroads plan needs a different pact addressing Nocticula's power base and enemy access.
   Do not call the crossroads closure or silently repeat the parent's promise.
   This costs the Commander a concrete limitation on their preferred outcome and gives Nocticula a reason to keep listening without making her agree to every ambition.

6. **A personal answer after the work.**
   Only after the delivered concession and several adversarial meetings does she offer continued private company.
   Keep acceptance, further negotiation and refusal distinct.
   The flag recording the agreement follows her actual offer and the player's response; a skill success does not itself set romance acceptance.
   Prior rejection remains readable in later callbacks.

The already-dead branch begins with mediated projection contact grounded in the native Threshold precedent.
Its earlier timing requires an authored ritual that identifies Nocticula rather than copying a remembered image.
Demand a real independent response before recording contact; no local memory recreation should impersonate her consent.
Restoring physical agency and political control requires an additional recovery sequence and native integration work before entering scenes where she commands living city agents.
Until that exists, this branch can support hostile negotiation and investigation, but cannot truthfully unlock the existing whole harbor story unchanged.
This is an explicit remaining implementation requirement, not a claim that dead-history support is complete.

## Living-Shamira native transaction to preserve

The scene's actual essence interaction calls `TakeShamirasEssense_CheckPassedActions`, `f657a949e74d9e04a9623aa655644c22`.
It removes one item reference `d66b1fdc9d313784ca51712640e210c7`, adds one `cfc7c93f8e93340469287afc905371c2`, completes objective `62920c1a061578143b4106fc456e6075`, and gives objective `97ac27d7798e02c4f9205fbaa76ff977`.
The objectives resolve to `C5_FinalLaugh/Add_3-1_TakeEssense` and `Add_3-2_GoBack`, under quest `653c8dec252da8d4b872d87e6f656cf2`.
The item identities above were observed as action references; their display names were not independently resolved in this pass.

The native default-boudoir Shamira spawner is `32aefc0f-e981-4820-bc63-5f36a23a8081`, unit `ec9802dd51b566f4b85a2d871bf1d49e`.
There is also a mythic Shamira spawner `0b08dd3d-e85e-4455-8fb2-51c3a7fd70e3`, unit `ae66d9252d56497e928808fa8c22effd`.
Both have scene-init spawning and respawn-if-dead disabled.
Their essence interaction is enabled on death, and the separate `TakeShamirasEssense` object is initially outside the game with one-use settings.
This supports a death-oriented native collection flow; it does not supply a native willing-extraction option.

A living alternative needs a dedicated transactional action after the authored negotiation succeeds.
It must verify and consume the required vessel, produce exactly one required result, advance the objective once, and leave ShamiraKilled and her actor life untouched.
Do not invoke the corpse interaction blindly or merely mark an addon flag saying the quest succeeded.
Further downstream Council text and objective consumers still need auditing for assumptions that Shamira died.

## Source-compatible implementation contract

Existing supported read-only maps include `Etudes`, `CompletedEtudes`, `SelectedAnswers`, `SeenCues`, `StartedDialogs` and `CompletedQuests`.
Use them to distinguish original Gift playing from completed Gift, actual parent acceptance from dialog start, and disclosure from an unearned intelligence claim.
`RequiresAnyGroups` can express alternative agreement/channel prerequisites, but independent OR groups must not combine mismatched histories into a false valid contract.
Normalize each fully verified acquisition path into a new addon agreement flag only after its complete prerequisites and final answer.

Suggested addon names, with no invented native GUIDs, are `noct.acq_request`, `noct.acq_concession_delivered`, `noct.channel_negotiated`, `noct.renewed_agreement` and `noct.crossroads_terms`.
These are proposals, not currently declared states.
Do not write native parent Active, Reject, cue history or Gift through ordinary choice `Set` effects.
That bypasses native bookkeeping and confuses played history with author assertions.

The current shared visits require parent Active, witnessed parent agreement and original Gift, and forbid parent Reject and death.
Introduce carefully gated recovered-entry variants or a normalized acquisition contract, retaining the original accepted route's predicates and wording.
Rewrite every "earlier bargain" and Worldwound-price reference for the actual renewed terms.
Do not duplicate variants for content credit.
Keep optional parent ambition and Laulieh histories as actual read-only facts, not perks granted by reacquisition.

Current `ForbidOverrides` validation permits authored flags only and explicitly rejects native bindings and relationship closed flags.
It cannot legally override `noct.parent_rejected` or `noct.dead`.
The relationship's `UnavailableFlags` also independently blocks dead Nocticula.
Post-death projection research therefore needs an explicit contact/recovery design, not a hidden exception in a normal romance scene.
Do not register a generic `Revive` action until a Nocticula-specific actor, political-state and lifecycle transaction exists.

The current source helpers cannot consume the essence vessel, grant the quest item or complete native quest objectives through narrative choices alone.
That part requires a reviewed engine action with native-state preconditions and idempotent completion.
Narrated costs must either have actual mechanical effects or be clearly limited to witnessed story consequences.
Do not describe a stat loss, resource expenditure or altered final quest as implemented when it is only a flag.

## Concurrent relationships and acceptance tests

Keep the parent's explicit acceptance of other lovers.
No acquisition step should complete another romance, require exclusivity or punish unrelated partners merely to simplify state handling.
Shamira's rival political interest is a real conflict to negotiate; ToyBox's jealousy options do not solve her death-dependent quest step.
Laulieh participation and existing shared endings remain separate earned histories.

Required test saves include original acceptance, initial-only dinner, never-offered dream, interrupted dream, explicit Book 1 refusal, explicit Book 2 refusal, later parent breakup, original Gift active, original Gift completed, renewed Gift active, never-gifted, living hostile Nocticula, fight flag before death, observed Council death, resolved Demon death and Threshold projection.
For every entry, verify the first displayed page, actual available choices, finite preparation/failure paths and final agreement producer.
Test non-Trickster paths to ensure their existing restrictions remain intact.

Verify the living-Shamira transaction through the next native objective and subsequent Council response, with no corpse, duplicate actor, extra quest item or murder acknowledgment.
Verify recovered entry does not increment RanRomCount repeatedly or fabricate parent cue history.
Retest every joined completion against the 21,000-word floor after history-specific text changes.
Finally test real rest ordering, interruption/reload, actor availability and unrelated romance advancement with ToyBox Free Love and No Jealousy both enabled and disabled.
This research performed native-data and scene-object inspection only, not those save-based checks.

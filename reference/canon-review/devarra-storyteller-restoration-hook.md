# Devarra: Storyteller restoration acquisition hook

Research date: 2026-09-27.
This is a read-only installed-data investigation and an integration proposal, not a playable-route approval.
The user authorizes all installed DLC as the project baseline.
Installed DLC assets do not establish that the current main-campaign save played Devarra's DLC dialogue or imported her actor, memories or corpse.

## Finding

The native Drezen Storyteller conversation supplies a concrete attachment point for a newly authored Chapter 5 investigation.
The actual scene spawner carries that conversation, and the native Greybor hunt starts the capital-presence etude.
The inspected presence chain has no explicit Chapter 3-only condition, but its existence is not proof of presence in every Chapter 5 save.
Require the current accessible Storyteller actor and the relevant playing etudes; do not manufacture his return or replay a quest KTC.

The lair supplies a verified historical dragon actor and death trigger, but no verified collectible Devarra body fragment was found in the inspected actor loot, scene loot tables or relevant quest records.
Her scene-added loot is **Half of the Pair**, an enchanted pendant, not a scale, bone or resurrection reagent.
That pendant could inspire a separately authored object-memory investigation only with verified possession and an honestly stated provenance limitation.
It cannot prove a surviving corpse or unique ownership merely because one copy drops from this dragon.

Existing `Fate.TryRevive` does not support this hostile NPC.
A new authored NPC restoration/delivery producer needs its own persistent identity and observed physical arrival, following the safeguards in `TerendelevDelivery` without copying its human actor configuration.

## Native Storyteller attachment

| Evidence | Exact identity | Observed contract |
| --- | --- | --- |
| Main conversation | `bf328bcec67a5014f9a56ee6220f3bcc` | `World/Dialogs/NPC_Common/StoryTeller_MainDialogue/StoryTeller_MainDialogue.jbp`; Common dialog, empty Conditions and FinishActions. |
| Shared answer list | `2f5b7e0b76d3c5a42a431e1e33a8db09` | `AnswersList_0004.jbp`; repeatable, empty conditions, no alignment or mythic requirement. |
| Safe structural return candidate | `04afc85667cb0264e970688952e1860d` | `Cue_0021.jbp`; both ShowOnce values false, no conditions, actions, experience, alignment change or continuation; exactly the shared answer list. |
| Storyteller blueprint | `da4c28dd01413694f82b08b728a8c6e5` | Native Storyteller unit. |
| Capital scene spawner | `a0993ca0-8627-4ec9-a9f2-5a75910d7023` | Scene GUID `3e2b5ea054cd5b2479e7f13134363ef4`; actual bundle `drezencapital_default_mechanics.scenes`. |
| Capital presence | `0a2f801a031555c44a253378d081781d` | `ImportantNPCs_fate/Storyteller_Capital.jbp`; unhides that spawner and moves it to StorytellerPosition. |
| Returned parent | `36f08741eaa811248b106323982b9fbf` | `StorytellerReturnedToCapital.jbp`; no activation/completion conditions; parent Storyteller `8b444358cf7121b4483329bdfb98eeda`. |
| Peaceful capital condition | `e0d8b253efedb70488badaaa3d47632c` | `CapitalMechanic/DrezenCapital_DefaultMechanic/NotInCombat.jbp`; must be Playing for the presence leaf. |
| Default hidden actor | `ae33a639b3e6a6847bf3b75b400561f1` | Lower-priority conflicting default actor hides the same spawner. |
| Storyteller departure/death history | `3c1405201bec99f4db67371f41a3c32a` | `StorytellerDead.jbp`; comment associates it with accepting Pharasma's offer, not a generic always-available actor. |

Direct UnityPy inspection found GameObject 53 with MonoBehaviour 1819 referencing the main dialog and MonoBehaviour 1820 containing the exact unit blueprint and spawner identity above.
The spawner has `m_SpawnOnSceneInit=1`, `m_RespawnIfDead=0`, and no spawn-condition blueprint.
The actor's etude visibility still governs whether this scene object is actually available.
This is stronger evidence than a blueprint name or a seeded fixture, but remains static evidence rather than a live-save observation.

The verified main dialog performs a conditional elven-page check in StartActions and can unmark a native answer as selected.
Do not restart the whole dialog as a return shortcut without considering that action.
The structurally suitable return candidate says the Commander still has questions that have not surfaced.
Write the acquisition's terminal line as a return to further questions if this cue is used, or use a separately reviewed authored return.
Do not substitute `Cue_0593` (`24fcf933e4c622042942beffc8424857`) just because it is the shared answer list's parent: it requires a completed objective and has a nonempty Continue.
Likewise `Cue_0003` (`64a199eaa9248b14494f2ad8c58565c9`) is a conditional one-shot and has a different list.

The native hunt etude `affc77eac949f364fba73b60d6a0c186`, `DragonHunt_Q1/WoundWormLair_Event.jbp`, starts `Storyteller_Capital` on play.
That presence leaf starts its returned parent and is linked to Drezen area `2570015799edf594daf2f076f2f975d8`, including area parts.
The inspected native parent chain does not restrict this presence to Chapter 3.
Chapter 5 presets also reference the presence leaf, but presets are setup data and do not prove a real player's transition.

For the new main-campaign option, propose an authored Chapter 5 plus Trickster gate, the existing native presence gate and a live usable actor check.
Chapter and mythic binding IDs must come from the project's verified binding inventory before implementation; this report does not invent them.
Storyteller departure/death and missing actor should withhold this physical hook rather than silently respawn him.
An eventual all-history Trickster guarantee needs a separately earned alternative if he has already left.

Do not attach to `StorytellerDangerousDrezen_dialogue` (`3d18ad877d12ba44c9dc5121801455fa`) as a reusable hub.
Its StartActions fail/complete siege objectives and its FinishActions start an etude and play a cutscene.
The Iz dialog (`912306287541478468c2a87f19ad803c`) likewise gives/completes objectives and unhides exits on finish.
The Chapter 3 return KTC remains a quest notification, not a substitute for this repeatable conversation.

## Lair access and death-site provenance

| Evidence | Exact identity | Meaning and limit |
| --- | --- | --- |
| World-map location | `460375af7f35b784ba8ccc59f1e61e68` | `Location_WoundwormsLair.jbp`; not closed on start, not revealed on start, and ordinary reveal condition is False. |
| Area | `362dacd5490050b45aa6828c65a7d4c4` | Native WoundWormsLair area. |
| Entrance | `5b7505de49cc1aa499731ef0c7e5d574` | Native location entrance, not proof that the current save permits entry. |
| Native revelation | `6ed5620a59949e847bd79f7c77669f1d`, `8f33c0d0fe47482458536070714aab23` | DragonHuntBookEvent2 cues 0003/0004 execute UnlockLocation. |
| Companion restriction | `f72bb7c48bb3e45458f866045448fb58` | RequiredCompanions references Greybor_Companion; empty ignore/allowed checkers need engine-semantic/live validation. |
| Lair dragon | `c540d81c08822c14da75761493427e4c` | WoundWormsLair_BlackDragon blueprint; the internal BlackDragon name is not a new authored species claim. |
| Actual lair spawner | `e43d0b6c-b064-4987-a717-14efcb4c1d56` | Scene `128772032f4413047b02bc7a8f306423`, GameObject 87 in `woundwormslair_gameplaymechanics.scenes`. |
| Lair death | `581521b398fb9dd4eb52bbfffb3b5c43` | Started by the actual evaluated-unit death trigger; marks the location explored. |
| Escape | `23bea0045d007fc4db834476012eed58` | RedDragonEscaped; marks the location explored too, so explored does not establish death. |
| Sanctum dragon | `b01da68dab56e004f952d7ad0e83cc46` | RedDragon_Sanctum, with lair blueprint prototype. |
| Sanctum death | `056ba61e04cca104a9c95ac2d4658c67` | Separate death history retained from the main-campaign audit. |

The actual lair spawner's MonoBehaviour 420 has spawn-on-scene-init enabled and respawn-if-dead disabled.
MonoBehaviour 421 overrides its brain to `1ef9b39b8917ee846aad13e7eb35e726`.
MonoBehaviour 422 adds one `43b2b67063747ec43b962ed12111e106`, `Equipment/Amulets/UniquePF2/HalfOfPairedPendantItem.jbp`.
The localized name is Half of the Pair; its description concerns paired proximity attack and AC bonuses, with no dragon-remnant or resurrection claim.
The blueprint is destructible and not notable, so possession cannot be assumed after an old hunt.

The lair mechanics etude `fa1e44ec4639c4242b745b9b7c72cc03` binds death to the exact dragon spawner, starts the lair-death etude, unhides the global-map exit, completes the kill objective and stops encounter cutscenes.
Its encounter startup also changes the dragon's faction, attaches combat buffs and hides the exit.
Do not rerun that startup to obtain a restored actor.
The escape cutscene `DragonTryingLeave_scene/CommandAction 2.jbp` (`da0febde643e34d4abec79d9f74eb0ea`) hides the same dragon and starts the escape history.
A hidden escaped actor is not a dead body.

Direct bundle inspection identified the scene's loot tables, including scrolls, cooking supplies, ordinary trash, bracers and a metamagic rod.
The quest loot `ac45b7d1b570aa04fbed8d2a53142eaa`, `Loot/Quest/WoundWormsLair/Scrolls_8_fire.jbp`, supplies the elven page `a7584b66636515145ace8350747ae4ba`.
The associated `LexiconPage_FromWoundWormLair` etude `3f70888358c2a774e97e937717314fe1` records that page, not dragon remains.
This inspection does not establish the absence of every possible native remnant throughout the game, and the Sanctum's full scene loot was not exhaustively audited here.
It does establish that the presently identified lair item and page are not the claimed Devarra body fragment.

No inspected location blueprint has an explicit Chapter 5 closing condition, but that does not prove travel remains legal or safe in an actual Chapter 5 save.
Validate map visibility, restrictions, exit access and the existing encounter state without calling UnlockLocation or loading the area to bypass those checks.
Do not infer a persistent corpse from the native death flag, a nonrespawning spawner or a cleared location.

## Credible authored acquisition and supported engine boundary

Start with Storyteller recognizing the Commander's account of the hunt, only when that native history exists.
His ability to read histories from objects makes him a credible investigator; a new Devarra-specific soul-contact and restoration procedure remains authored alternate development.
The route should ask the player to recover and identify a trace before claiming it is available.

For a verified lair death, an authored expedition can produce a newly discovered trace at the actual death site after access is validated.
For a verified Sanctum death, recovery needs Sanctum provenance and its own access/delivery evidence; the lair must not be described as her corpse's location.
For an unresolved or living history, use a negotiated contact investigation and no resurrection claim.
For a missing corpse, an authored remnant-recovery event must establish what survived and why it is sufficient, rather than asserting native inventory or retroactively adding a supposedly collected bone.
Record the actual successful collection and identification as addon state, followed by a separate cost, consent and restoration attempt.
Brood acknowledgment must then follow the genuinely verified saved/lost history; unknown and contradictory flags require resolution, not a default accusation or fabricated DLC memory.

`Fate.FindRetainedCompanion` searches AllCrossSceneUnits for one matching blueprint, requires a companion part in the party or remote roster, player faction and a CrossSceneState holder.
`Fate.TryRevive` requires that retained dead companion and a conscious Commander, persists an attempt, calls `ResurrectAndFullRestore` and observes the result before applying the choice.
Neither Devarra's hostile lair NPC nor her Sanctum NPC satisfies that retained-companion contract merely by existing in the archive.
Changing a native death marker or falsely enrolling her as a companion to pass the check would corrupt the evidence and bypass the intended safeguard.

`TerendelevDelivery` supplies the relevant NPC pattern: an audited private blueprint, persistent request and unit identity before spawn, exact loaded outdoor area-state checks, duplicate/native-actor exclusions, and observed living usable arrival before confirmation.
It also avoids blindly respawning an already submitted but missing actor after an interrupted attempt.
Those are reusable design requirements, not proof that its implementation already supports Devarra.
Its private human-form blueprint and friendly configuration must not be reused as a Huge dragon without a separate body, brain, facts, collision and navigation audit.
The known StorytellerPosition is a human locator near `(7.49, 62, -28.07)`; it is neither a free spawn position nor a tested dragon-sized landing site.

Leave native hunt-death and brood histories intact after restoration.
Create new addon evidence for the restored identity, her witnessed acknowledgment, the negotiated physical rendezvous and any later voluntary humanoid transformation.
Do not mark the current DLC-specific opening cue as seen unless it really played in the associated history.

## Verification still required

1. Exercise the real Chapter 5 Storyteller hub in saves before and after his relevant quest completion and departure, including a completed Greybor hunt.
2. Validate an injected option and terminal return against the exact list/cue contract, with no replay of native dialog-start or quest-finish effects.
3. Observe lawful lair and Sanctum re-entry for their respective death histories, including Greybor absent and present, and prove the old encounter does not restart.
4. Implement and test the actual remnant producer, possession/provenance tracking, identification, chosen cost and refusal/recovery branches.
5. Audit and deliver a dedicated Devarra NPC identity, then test interruption, reload, area changes, missing views, duplicate exclusion and retained native living actors.
6. Test brood saved, lost, unresolved and contradictory histories independently from DLC ownership and any actual imported encounter record.

No game state, blueprint archive, source or image was modified for this investigation.
No Unity gameplay, resurrection, spawn, travel or save/reload test was executed.
The concrete native hook is established statically; actual Chapter 5 access, remnant production and restoration delivery remain unverified.

## Source pins

The related main-campaign audit was read at SHA256 `AC26D7A1B4436E23E4F9CDC7CAC3BA7D624F04D43602A7BD633B94EFBA737B1E`.
`src/Fate.cs` was read at `160A5D843CABE35B29341D658C54366DB20DC462FB7C3FE5DD652C5821F7B155`.
`src/TerendelevDelivery.cs` was read at `E13C14EB47C9EFEB7D05C9656A9E3E34F4CEDC750B70975CE4331658B77588C2`.
Native data came directly from the installed `blueprints.zip`, `enGB.json` and the named scene bundles under `D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure`.

| Inspected native bytes | SHA256 |
| --- | --- |
| `World/Dialogs/NPC_Common/StoryTeller_MainDialogue/StoryTeller_MainDialogue.jbp` | `30BB909313CD2C6988D33BD6E679E1DF3DAC2F0DBAD11CAE222241BD27CA133E` |
| `World/Dialogs/NPC_Common/StoryTeller_MainDialogue/AnswersList_0004.jbp` | `8DBE89556B0B3A3697D3ED9C7363E11B8014C6E2CDEBF7BE90E0A38D5A72EC1A` |
| `World/Dialogs/NPC_Common/StoryTeller_MainDialogue/Cue_0021.jbp` | `1D6716FBE5501DEE89D6E557FF297CC904A800C5AA7C42BE48A7C4D68B620337` |
| `GlobalMaps/WorldWoundGM/Points/Location_WoundwormsLair.jbp` | `1F8F94398AE908ED7B3F44557F85AEA63F7ADD3BE2184974A1B1AAD35B581B73` |
| `Equipment/Amulets/UniquePF2/HalfOfPairedPendantItem.jbp` | `A627393FCC47253B5B9CE6AE66CD513EBADD81136E8F2D7C901D832D6CD2F599` |
| `Bundles/drezencapital_default_mechanics.scenes` | `D451FEF29C6B22F5D13E8BACEA70BA063175DDEE8B3F43F48D6CAE7F22B4A9E3` |
| `Bundles/woundwormslair_mechanics.scenes` | `1C81CBD224249898331DA34F8DFD0ADAB0035698461589EBB34418E7AC68CEB1` |
| `Bundles/woundwormslair_gameplaymechanics.scenes` | `97904E73CADD016590BA2FAC2C14DC81F5FC6D99FF7B7A60FD6DE595E31CB4EE` |

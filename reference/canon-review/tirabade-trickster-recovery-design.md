# Tirabade Trickster recovery and access design

Design and installed-source audit, 2026-09-26.
No story, engine, installed asset or native flag was changed.
This file did not exist when ownership was assigned.
The interventions below are proposed alternate developments, not delivered routes or undiscovered native resurrection scenes.

## Recommended next implementation

Build a read-only Tirabade actor observer first, using the exact capital and Iz sources below.
Then implement the living-departure invitation and a separate retained-death operation, each with an earned narrative agreement and verified physical arrival.
Do not start by cloning the two capital NPCs or removing their unavailable flags.
A hidden living capital representation is not proof that the woman killed at Iz survived.

Ordinary missed Chapter 3 courtship already has a Chapter 5 entry and does not need resurrection.
Keep that entry as the shortest route when its actual native actor is available.
A Trickster-specific optional invitation can add character-specific play without making a redundant recovery quest mandatory for every living character.

## Native evidence inspected

I reread `tirabade-capital-contact-audit.md`, its extracted records, `anevia-after-irabeth-death-audit.md` and its extracted records.
I independently reopened the relevant installed `blueprints.zip` entries and English localization.
I also inspected the actual Unity bundle `Bundles/iz_default_mechanics.scenes` with the project's UnityPy interpreter.
The existing `NativeContact`, `Fate`, `JerribethRecovery`, `TerendelevDelivery`, `Rules.Available` and `Rules.ContactAvailable` implementations were read for reuse boundaries.

| Identity | Verified value |
| --- | --- |
| Drezen area | `2570015799edf594daf2f076f2f975d8` |
| Capital default mechanics scene | `DrezenCapital_Default_Mechanics`, asset `3e2b5ea054cd5b2479e7f13134363ef4` |
| Anevia capital unit | `b5e867e13503c6f41bb1316705efb4a2` |
| Anevia capital spawner | `86b332a9-5910-4d46-9951-8e06f7dcf0cf` |
| Anevia native dialogue / answer list | `de4cc2dd71694b842be37b75d1705b83` / `33960c7f7af40cd43b7f801a76c87a0b` |
| Irabeth capital unit | `280d4712dceb37f4a88e98f1f4c6e64f` |
| Irabeth capital spawner | `3dc302d8-58ce-44f3-9766-2a437a080108` |
| Irabeth native dialogue / answer list | `20e94a828d4016d45a6b723765306522` / `871af36f2ab2b1f40b5de77976c54276` |
| Iz area | `2ccc6731787b6ec41ab5adc13f1b9ce9` |
| Iz Irabeth unit | `9adfeebc39054544fa0f924022e43c1c` |
| Iz Irabeth summon pool | `58ea82467325434db7e499cba419c865` |

The Iz bundle SHA-256 is `D423AD17FB64A2706C3414C88770C01E1A75E8E64499346B26EB266B384839DB`.
Its GameObject 200, `IrabethInMonsterLair`, has spawner `8b5b891b-a569-42c0-a7dd-7177760fa64a`.
GameObject 255, `IrabethInManuscripts (1)`, has spawner `bf142b5f-85f6-439e-9e23-f23646e22401`.
GameObject 331, `IrabethInManuscripts`, has spawner `d16d93ee-d53c-43da-9d0a-ff27eea9d15e`.
All three reference the Iz unit and pool above, with SpawnOnSceneInit false and RespawnIfDead false.
These are alternative native representations to inspect, not three people to resurrect.
Their transform values are local to different parents and are not approved global arrival coordinates.

The installed `World/Encounters/Iz/SummonPools/IrabethPool.jbp` sets `DoNotRemoveDeadUnits` true.
That supports attempting to observe a retained corpse; it does not prove a particular saved actor still exists.
`World/Dialogs/c5/Iz/IrabethDies/IrabethDies_Iz_c5_dialog.jbp`, asset `48a3a4ff8955b7045bac0ea06092e085`, kills the first pool unit in FinishActions and starts IrabethDead.
Its source SHA-256 is `5AE1568CA0DF741A4C245219B75704901AD7B47674535BA452FF62033D452131`.
Its opening cue `f7d10f44770ad3247bd65f1e426a8b3f` presents her dying in service, with her formal release from duty.

The Iz blueprint differs from the capital blueprint and contains an upgrader, class/level configuration, equipment, combat brain and encounter XP.
It is not a reviewed passive social-body template.
Native Iz cutscenes can hide Irabeth and delete her membership from this summon pool when moving toward the manuscript basement.
An empty pool therefore does not prove death or deletion of the entity.
Use saved spawner references and all known representations, not only the first pool result.

## Read-only history distinctions

| History to read | Native asset |
| --- | --- |
| Irabeth dead | `b14e13f9359585e498fcd81ab95d4d7e` |
| Irabeth sacrificed herself saving Galfrey | `518d91f94fb3a504a91571b7e75c68fc` |
| Commander killed Irabeth | `c0f261c4a259da741ab0052f0100c2a0` |
| Irabeth gone alive | `395aad049186445f9f474d0a769ec8ff` |
| Irabeth absent with Galfrey in Chapter 5 | `260454e5186fbd34694a0393097f77b5` |
| Irabeth not in Drezen | `99a03d4f02004b76a5e97c85ba0ec37e` |
| Anevia dead | `ba365d0ae03c414a8f6f906837a4fe91` |
| Anevia gone | `09f46662bcd14a03a0874267e16d6e6f` |
| Anevia not in Drezen | `6125c10886d6465091f4e092618ca55a` |
| Coronation | `7ef4b33d3aa037f4984e167eae592009` |
| Crusaders gone | `061d1dfd76f4ea74ea8aa4d013fc8016` |
| Current Trickster path binding | `9f486a9c0c9abfc4a952bb22e88a7e96` |

Both Gone etudes exclude their own death etude from activation and start their capital hiding state.
Irabeth's absence with Galfrey has priority 400; it must not be overridden as though it were permanent desertion.
The capital throne-room positioning is lower priority and cannot establish current contact by itself.

Coronation Cue_0421, `575f7925bbfe4e047bcd666ca27a8c80`, starts AneviaGone when she leaves after her wife's death.
The temporary coronation position proves a staged appearance, not a free ordinary-dialogue window after the ceremony.
Answers 0425 and 0430 admit killing Irabeth and lead to her angry departure through cues 0426 and 0431.
Read both the native killed-by-Commander history and the actual seen/selected dialogue history when deciding what she already knows.
Do not infer forgiveness from a living actor or from the absence of a romance refusal flag.

Coronation Cue_0056, `42afa0f3557328b40bc7ae6642a35bc6`, depicts the humiliated Mendev army departing and starts the living wives' Gone states plus CrusadersGone.
Its SHA-256 is `F78FA314530EF6B3A52F88170738B290ED88A78C673487F91DD87AC0E948B53A`.
This departure is a political rupture, not simply a missed date.
The precise intersection of every native hostile-departure branch with an unchanged current Trickster playthrough is not proved by this audit.
Keep such histories supported as explicit compatibility cases rather than advertising all as normal Trickster outcomes.

## Proposed playable interventions

Every paragraph in this section is authored alternate development.
None claims the native game already restores either woman this way.

### Irabeth: the officer whose duty was finished

After the Iz outcome is known, a Trickster can investigate the contradiction between Irabeth's completed duty and the claim that death has settled every future choice she might make.
Her actual dying words provide the personal connection; the joke must not make her service or grief ridiculous.
The proposed working turns a formal release from duty into a summons she is free to decline.
It offers a future after service, not a command to resume service or love the Commander.

Play the investigation through the actual Iz death site and a witnessed account of the event.
Use the saved actor observer before describing a corpse, and provide a separate search branch if the native representation was removed.
A Knowledge Religion check can clarify the distinction between a willing return and binding a soul.
A failed check requires another witness or a second preparation visit instead of permanently deleting the route.
It must never roll for her consent.

The completed working first offers Irabeth the choice to return to her wife and her own life.
Romantic continuation or first courtship follows later, using the actual prior relationship history.
If the Commander killed her, the first conversation concerns that act and requires an accountable explanation and concrete restitution before any invitation.
Restoration does not oblige either woman to forgive the Commander.
A reviewed path to earned voluntary reconciliation should remain attainable; an explicit refusal chosen during that path remains binding.

If Irabeth is alive but away with Galfrey, use the ordinary post-Iz/post-coronation return when it is available.
Do not interrupt the Queen's expedition or secretly hide its NPC to provide a date.
If she left with the humiliated army, offer an authored off-duty meeting through a truthful appeal about the people harmed by the Commander's rule.
The player must accept her conditions before a meeting is scheduled.
She need not rejoin the crusade or endorse the Commander to agree to speak.

### Anevia: a message that cannot answer for her

For a living Anevia who left after coronation, the Trickster's first scene is a message-writing and investigation scene at a rest.
Its purpose is to find a way to offer an invitation, not to teleport an unwilling person back to headquarters.
Anevia knows clandestine communication and would notice a forged answer immediately.
Let her challenge the method and choose a meeting location and time herself.

Her Desnan faith, work as a scout and intelligence officer, marriage, and known desire to leave after bereavement provide the character connection.
The authored fate intervention can let an honestly addressed invitation find a road that ordinary messengers cannot find.
The player must choose what truth to include and accept that sending a request does not produce an affirmative reply.
Perception can expose a misleading trail; a nonroll alternative follows another reliable lead at the cost of time or a smaller concession.
Her response is a written scene only after the authored delivery event is earned, not a fictional reliable courier into the Abyss.

Bereavement and political departure need distinct replies.
If Irabeth has been verifiably restored, Anevia must receive evidence and then choose whether to meet her before discussing romance with the Commander.
If Irabeth remains dead, Anevia may agree to a limited meeting without returning to service or treating a new lover as her wife's replacement.
If the Commander killed Irabeth, preserve her anger and knowledge; no single apology or persuasion success should bypass that history.
An authored reconciliation requires several consequential meetings, independent support for Anevia, and actions that cost the Commander something relevant to the harm.
A refusal to pursue reconciliation leaves her free to leave again.

AneviaDead requires a separate identity and cause-of-death audit before a resurrection implementation.
This audit verifies that her death marker hides the capital actor; it does not identify every native death scene or corpse.
Do not reuse living departure as resurrection or clone her capital actor to fill that evidence gap.

### Missed ordinary courtship and late installation

Living, available Chapter 5 characters can use the reviewed fresh entries without pretending the Commander courted them in Chapter 3.
For Trickster flavor, offer an optional paired scheduling mishap that turns into two explicitly separate invitations, each independently accepted or declined.
Anevia can spot the deliberate coincidence; Irabeth can insist on finishing the real work before agreeing to an off-duty visit.
This develops the Trickster's intervention without changing their minds by magic.

Use the native Fool King quest as an optional remembered example only when the actual quest history supports it.
Its quest asset is `3da881eb13fcdce49b5c9dd21f4d3d65`; its installed text describes the invented Sarkorian kingship and the real consequence of playing along.
The late Trickster quest `653c8dec252da8d4b872d87e6f656cf2`, The Ultimate Joke, concerns a plan capable of changing the Worldwound.
These support the tone and scale of authored fate interventions, but neither is a native grant of unlimited resurrection.
Do not require a still-accessible Council NPC or unfinished old quest for every late save.
The first rest scene needs only verified current Trickster access and the relevant campaign outcome; quest completion changes its prose and investigative options.

Chapter 6-only first acquisition is not covered by the current Chapter 3/5 capital routes.
A distinct late-campaign meeting opportunity and content sequence are needed before claiming access after that point.
A synthetic chapter flag or retroactive Abyss letter is not an acceptable substitute.

## Actor and engine contract

Observe all matching native representations and classify NotLoaded, Unresolved, RetainedAlive, RetainedDead, RecordedDeadMissingActor or Conflict.
Use each exact saved spawner's `SpawnedUnit.UniqueId`, then require matching blueprint, registry object and owning saved scene.
Spawner IDs are not actor IDs.
An unloaded area is unknown; do not create a state with `GetStateForArea` merely to search it.
A missing pool entry, hidden capital unit or historical death marker alone authorizes no resurrection.

`JerribethRecovery` provides the relevant observation pattern but remains observation-only.
`Fate.FindRetainedCompanion` requires party or remote companion storage and is not suitable for these NPCs.
`TerendelevDelivery` provides persisted request identity, queue-aware polling and arrival confirmation, but its clone allowlist and outdoor position do not apply automatically to the wives.
Identity-preserving transfer between Iz and Drezen still needs its own verified native operation.
`RemoveEntityData` disposes an entity and must not be used as the first half of a transfer.

For a retained living departure, first prove the saved actor identity and absence of a conflicting active representation.
Stage an authored accepted meeting through a reviewed mod-owned positioning operation that coexists with native death, expedition, coronation and hiding states.
Do not directly fight native HideUnit on every tick or raise an arbitrary conflict priority.
For a corpse, require an earned willing-return agreement and verify the retained resurrection operation before any relocation.
A discarded-body branch needs an explicitly reviewed reconstitution story and private blueprint behavior audit; a clone is not evidence of recovered identity.

Persist request provenance, observed native history, agreement, exact actor identity and pending/confirmed state before dispatch.
Confirm the same actor in the registry and saved scene after the engine tick, with a loaded usable view, consciousness and nonhostility.
Recheck that evidence on every physical visit and after save/load.
A killed or departed confirmed actor must not automatically respawn.

The first invitation/investigation must be attainable without speaking to the missing woman.
Use the existing remote/rest presentation for an investigation book with its own tightly scoped recovery eligibility, rather than placing it behind the ordinary romance's unavailable guard.
That book grants no lover flag or physical contact.
A later physical meeting remains unavailable until observed arrival and the woman's authored agreement both hold.

The current rules require a deliberate narrow change before historical recovery can work.
`Rules.ContactAvailable` independently rejects the relationship's native unavailable flags and native scene forbids.
`ForbidOverrides` in entry checks does not override that physical continuation check, and the ordinary relationship check also rejects unavailable flags.
Specify a character-specific confirmed-current-presence exception used consistently by entry and continuation, while preserving the native historical values for dialogue and epilogues.
Do not erase the history, remove all unavailability gates or set a blanket available flag.
Existing `anevia.closed`, `irabeth.closed`, `irabeth.future_friends`, global closure, other mythic restrictions and `tirabade.group_closed` remain authoritative.
A recovered woman's return does not revive a declined triad.
Epilogues need explicit recovered-current-life branches so preserved death history does not incorrectly force a loss ending.

## Required proof before implementation approval

First reproduce the actual end-user sequence from a real death or departure save through the investigation, agreement, arrival and first conversation.
Use that sequence to test the adapter, then supplement it with focused fixtures.

- Compare the saved capital and Iz references, including multiple alternative spawners, hidden living capital representations, retained corpses and unresolved or unloaded sources.
- Preserve native death, Gone, killed-by-Commander, morale, Queen, quest and seen-dialogue histories before and after the intervention.
- Prove save-before-dispatch failure performs no operation; retry and reload adopt the same actor rather than creating another.
- Verify queued creation is pending, not success, and wrong identity, duplicate representation, hostile actor and unusable view all block arrival.
- Test both physical participants disappearing during a shared scene, while authored midscene romance choices do not falsely interrupt contact.
- Walk separate military-death, Commander-killed, political-departure, missed Chapter 3 and late-installation text, including check failure and nonroll alternatives.
- Verify restored current life changes the relevant ending without rewriting historical death or resurrecting a refused romance.
- Exercise other existing romances with ToyBox free-love/no-jealousy enabled, keeping their flags unchanged.

The observer and its managed fixtures for the five verified spawners are now integrated in commit `619714f`.
The native transfer audit and isolated ownership probe are recorded in `native-retained-actor-transfer-audit.md` and its sibling Python probe.
Root independently reran the probe against the installed assembly and read the native add, remove and translocation bodies.
The probe passed with zero build warnings or errors, demonstrating duplicate source and target list membership after adding the same object to two states.
This confirms that native add is not a transfer operation; it does not test Unity movement or save serialization.
The next implementation prerequisite is a reviewed same-state meeting-position contract that handles native event ownership.
The first playable restoration should target an accepted meeting with a retained living departed actor in its own capital state, followed by retained Iz-death recovery once native resurrection and relocation are proven.
Cross-area travel remains required work rather than an assumed capability of the same-state operation.
Anevia's own death and Chapter 6-only entry remain named missing work, not silent exclusions from the eventual universal Trickster requirement.

## Positioning conflict evidence added after the observer

`tirabade-positioning-native.json` preserves all 46 installed etudes under `World/Etudes/` whose exact conflicting-group list contains Anevia's group `27d10af5650a01b4d803da81799cbc86` or Irabeth's group `997d865aa6f17cc48b480bd62ba02841`.
These records were extracted from the installed blueprint archive, not inferred from filenames.
This is a complete match for those two group references in that archive subtree, not a proof that every action elsewhere that can move the women has been found.

Both default throne-room placements have priority -50 and both default hidden actors have priority -100.
The departure hide etudes have priority 99, while coronation placement and several capital events use 100.
Other members include Camellia, Arueshalae, Wenduag and Sosiel events, crusade defeat, the queen's expedition and mythic scenes, with priorities reaching 1000.
A recovery etude cannot safely choose a large priority merely to beat the departure hide state.
It must yield to actual native events, including relevant lower-priority quest conversations that a permanent priority increase could suppress.

Anevia's `NotInDrezen` record has a second play trigger in addition to hiding her.
When objective `1a32315f0f94f6a4588c2705f9782fee` is Started, it fails that objective and `6b9242706b8c43d49003813b869f023e`.
Releasing a custom conflict claim may allow native play triggers to run again; the implementation must inspect that lifecycle before claiming release is harmless.
Do not disable this native quest behavior or rewrite its historical result to support a romance.

Before implementing the invitation position, inspect native conflict selection and activation/deactivation behavior, then define how a pending native scene preempts the meeting and how the same actor is reobserved afterward.
The current evidence does not yet approve an etude priority, a new meeting locator, a hiding override, or a recovery caller.

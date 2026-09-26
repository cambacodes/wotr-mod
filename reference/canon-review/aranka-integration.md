# Aranka integration audit

Shared Kiana scenes can read the installed Aranka relationship, but cannot yet assume a reusable Chapter 5 Drezen actor from an etude name.
The installed source was decompiled with ILSpy and cross-checked against native blueprints and localization.
Installed RanRomance.dll SHA256 is 281239b19ff12675d2e8e48cd86b3759c38f6598a93e13f254a044c5e990db68.
The initial namespace-only decompile in aranka-installed.cs failed because RanRomance.Aran is a namespace; the successful class-specific aranka-Main.cs and aranka-AranBook*.cs files contain the actual code.
No story, test, journal, or installed game asset was changed.

## Stable installed read predicates

| Purpose | Type and exact GUID | Verified interpretation |
|---|---|---|
| Aranka romance | BlueprintEtude 2e98dbe685f045cdabf88b66e4cde9ff | RanRomAranRomance Playing is the established relationship condition used by installed scenes and epilogues. |
| Flirt | BlueprintEtude da5580951e64443c8f9ebdb559efad7a | RanRomAranFlirt activation excludes FlirtEnd Playing. |
| Flirt ended | BlueprintEtude 285425f788fd41d7860df9a899e1f4a7 | RanRomAranFlirtEnd records rejection and suppresses flirt-dependent branches. |
| Active | BlueprintEtude b2dfa8223ee24b84ab2795f86aa66ebb | RanRomAranActive has no physical-presence predicate; it must not substitute for actor availability or romance. |
| Reverie flirt | BlueprintEtude a5235e681a7b484e8deb572b8193ff27 | RanRomAranAlurFlirt enables the existing Reverie development. |
| Reverie partnership | BlueprintEtude d4dd8a50613e4d528913d0a24d06fca1 | RanRomAranAlurRomance Playing is used by existing shared-romance epilogues. |
| Confidence | BlueprintUnlockableFlag 3564eeaca9484627bb82958e9bf1b449 | RanRomAranConf is an integer progression value, not an etude or simple alive flag. |
| Dream Warden | BlueprintEtude 77f1192d6ff8428389351c7ef02c2bfc | RanRomAranWarden is a distinct authored role state. |
| Existing journal | BlueprintQuest 1dacd3dfe1bf47c8a73074814e40b1c8 | RanRomAranQuest owns the native addon journal progression; do not create a duplicate. |

These definitions come from RanRomance.Aran.Main.Configure and AranQuest.Configure.
The committed-romance etude increments RanRomCount on play and decrements it on completion.
Shared scenes must not StartEtude or CompleteEtude this existing relationship simply to record a Kiana interaction.
A local extension flag can record the rehearsal while leaving installed counters and relationship states untouched.
Completed romance must not be treated as currently Playing.
An unlocked confidence flag is not consent, commitment, survival, or presence.
The inspected Aran classes contain a completion of Active in Book02Page004 but no start of Active was found in those classes, reinforcing that it is unsuitable as the main read gate.

The existing quest objectives are Entry0001 de72cd5dc29f4ce882d32e14042bd243, Entry0002 af711de489484df5b81ef9996902e6a7, Entry0003 b968d14237b94e60af8f01f84f42dcda, Entry0004 d1e371f09017417b98b0aed58f3ab6ac, and hidden failure 4ef00caf2a644f42af5af39f7c381910.
Entry0003 and Entry0004 finish the parent quest, while the hidden failure objective also finishes the parent when failed.
Book02 starts by completing Entry0001, Book03 starts by completing Entry0002, Book04 finishes Entry0003, and Book14 finishes Entry0004.
These are objective actions, not generic relationship milestones that an expansion should replay.

## Entry and later chapter stages

| Stage | BlueprintDialog GUID | Source and supported meaning |
|---|---|---|
| Book01 | 2936ff4e6e234702b7f59b469b57feaa | AranBook01 plus AnevChpt03Dial001 and Anev.Main; first installed tent meeting. |
| Book02 | b9068ea8642f4c9da4a338ebd5ba316f | Chapter 3 rest event after one of the prelate meetings; introduces shared dream material and Reverie. |
| Book03 | fe8542a7a90d459c99d29921694f4d0d | Chapter 4 rest event; further choice and romance development. |
| Book04 | 14ffcdd473704e5dbc8cfe5f98b582b8 | Keep-artifact finale, delivered by camping encounter e162f1cea11345b8a0e04eb353ad3a25. |
| Book14 | 1650593635d947f0b28fc1900b10d4d6 | Give-up-artifact finale, includes an actual Chapter 5 Drezen war-room visit. |

DialogSeen on these GUIDs is a read-only record of encounters, not proof that every optional answer or final cue was experienced.
For specific facts, use the relevant seen cue or selected answer instead of assuming a whole book was completed.

AnevChpt03Dial001's Chapter 2 offer requires Chapter02 0e20d73ea0da6a94d94a6b42035a1ce0 Playing, AzataAcceptedInBE e6669aad304206c4d969f6602e6b412e Playing, and completed GibberingSwarm quest c21f4a2e26690a043b87339d95546f5e.
It also excludes both previously selected introduction answers, 126b48d9dad94a5bbead2aedc0ec4aa6 and 8de9e133dfed4ac9837f0004844c4647.
The Chapter 3 alternative requires Chapter03 15e0048c7daf0ac4999c2313b58df0e3 Playing, Azata mythic class, and BigIntro dialog 6f77c7a835f74ec42b583ba4d1fe2dfc seen, with the same answer exclusions.
Anev.Main starts Book01 after either introduction answer when Book01 has not already been seen.
Do not auto-select these answers or start Book01 to manufacture Trickster access.

The Book02 camping encounter requires Chapter03 and a seen prelate meeting among 28d2d40f91ea2c64ca8897815d341214, 138076de849b2b3408c04c02e524df06, and 9212aa4a0c8a9594bbd5596e83ddae35.
For a current Azata it additionally requires MentorArrives dialog f2d055f18b8265347b837c2ff3b9488a seen.
The non-Azata alternative preserves access for someone who entered the installed route in Chapter 2 but later chose another path.
Book03's rest encounter checks Chapter04 637a57423a82b044f888677c92f5d6cb Playing.

AranBook03 chooses keep-artifact continuation with Conf at least 2 and rejects the Book03 failure cue b18d250fa2fb4fdf9fe4eba04e9d1655 being seen.
The later camping gate requires RanRomC5MythicCompl and excludes Devil, Swarm, the specified high-level Lich and Demon class checks, and AzataDevilDecision_Deception 0b129925567b68d4fb712b4bee6c0f9a Playing.
The numeric UnitClass overload arguments and shared RanRomC5MythicCompl definition should be carried from code rather than rewritten as a guessed rank threshold.
The give-up branch in AnevChpt05Dial001 uses Conf at most 1, the same failure-cue exclusion, completed mythic progression, no Devil, and no Deception state.
These gates establish existing authored event eligibility, not a general actor-present condition.
Revisions.Configure can fail the quest on later chapter transitions and either AzataDevilDecision_Deception or AzataDevilDecision_Contract 5f72b252bd7fa8d48bd04c27982a4f9c.
A failed journal therefore needs separate handling even if a romance etude remains Playing.

Romance starts are explicit choices in Book03Page007, Book04Page005, and Book14Page002.
Reverie's accepted partnership is Book04Page007 answer 0f925d8224ed46eda99134c93d54a77a, which starts AlurRomance.
Its alternative answer 3dc28de79a974579a708e5e07cfe72cd completes AlurFlirt.
Shared Kiana text must respect whichever branch was actually chosen.

## Native actor and first meeting

The native first encounter is the DesnaAdept2 conversation in Daeran's party house, under World/Dialogs/c1/KenabresBurning/OraclePartyHouse/DesnaAdept2.
Cue_2, cc20dfe8789e457b8dcbb8a0818120da, describes a young woman recovering from the fight and joking that demons make a poor audience.
Her self-possession as a working singer and her existing adult romance portrayal support an adult character interpretation; no exact numerical age is established here.
Native Aranka_DesnaPriest unit b85fdd8481f26f54f9c504fc4d2e031f is Female, ChaoticGood, HumanRace 0a5d473ead98b0646b94495af250fdc4.
The inspected unit is not an aasimar despite later magical wing imagery in the addon.
Native Cue_0042 in DesnaAdept1, 6f9d9f3f8f3916a429144ec656695410, describes her as a singer with friends and fans.
Her later choir participation in WeCanFly/Cue_0020, a318ec40ad2a9d640a10684f9278979b, supports collaboration without making her the lead performer in every scene.

Aranka_DesnaPriest_Spawn c707b25030a78b24dab3b5d01d623a04 is a Chapter 1 spawn instruction after the party-house meeting, not an evergreen alive flag.
ArankaDesnaPriest_DefaultActor 547921e48f8f2ac42b6a79be55ba6b2d is especially unsafe as a presence alias.
Its play action calls HideUnit with Unhide false on the capital Aranka spawner.
It belongs to Azata_Capital_NPC_DefaultActors 062a11e4a57598a42b52494273faa475 beneath PlayerIsAzata and participates in the alignment-fix encounter conflict group.
A label containing DefaultActor does not prove an available conversation.
No global ArankaDead or ArankaAbsent state with verified comprehensive semantics was found in this focused pass.
Native AzataIsland_MassacreFlag b65f601e60499194f96e551a4c833af3 and its fear flag 79d2c536db98a9d43840da7ee5ee34a0 exist, but their exact consumers were not audited here and must not be guessed into death predicates.

## Shared scene contract and remaining check

For a romantic callback, require the installed Romance Playing, the relevant prior encounter history, and a currently valid contact mechanism.
For a friendly rehearsal, a verified prior meeting can suffice without starting or pretending to have the romance.
The meeting itself may be a new, explicitly accepted invitation into Drezen; it is not an existing native repeatable conversation discovered by this audit.
Book14 seen proves a prior physical visit but does not prove present survival or residence.
Before exporting an in-person scene, verify the correct live Aranka unit or an equivalent exact encounter-state predicate for the current save and exclude native hostile, killed, or absent outcomes.
This is the remaining concrete integration blocker.
A live unit should be checked for identity, death, hostility, and relevant area access rather than inferred from an unrelated book-event state.
A future Trickster contact requires its own authored introduction or restoration while leaving the existing Azata entry and journal intact.
Dream correspondence and waking travel are separate mechanisms and should be named accurately in text.

## Alluring Reverie and existing shared relationships

Alluring Reverie is already an authored participant of the installed Aranka route.
Book02Page003Cue0005 calls her a woman and identifies her as an uinuja azata with four eyes.
The text explicitly distinguishes the real Commander from a dream construct and describes Reverie as spending nearly all her time in the Dimension of Dreams with visits to Elysium.
Her social unfamiliarity is written as unfamiliarity with mortals, not an established child age.
Her existing romantic participation supports an adult-coded outsider interpretation, although no numerical age is supplied.
A world-unit blueprint for Reverie was not established by this audit; the verified contact is authored book-event and dream interaction.
Do not claim a persistent corporeal Drezen NPC or add her as an unrelated new romance.

Slide0004Cue0007 already introduces Reverie to Aranka's family in a dream.
Slide0004Cue0011 already describes the established shared-romance folktale.
The corresponding code reads AlurRomance along with Aranka romance and relevant ending branches.
Existing SlideArue also extends Arueshalae material and must remain owned by the installed route.
A Kiana connection should acknowledge existing partners where relevant and create only the new interaction, without replaying introductions or silently dropping Reverie.

Machine-readable name, type, GUID, and source mapping is in aranka-installed-map.json.
Native source records are in aranka-native.json and aranka-unit-consumers.json.
Resolved decompilations are the aranka-*.cs files named for their actual source classes.

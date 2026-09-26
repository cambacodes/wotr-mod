# Terendelev recovery and existing-route integration evidence

Terendelev is a strong recovery candidate, and the installed RanRomance route already owns the scale and Ravener-remains story.
Extend its played outcomes rather than introduce a second introductory romance or repeat its recovery promise.
The most useful new Trickster branch is an attainable escape from the existing ignored-Ravener scale confinement, followed by verified physical delivery and voluntary courtship.
A separate continuation can begin after RanRomance's already narrated return.
Neither a collected claw nor the native etude named `TerendelevAlive_Dragon` proves a living restored body.

## Provenance and method

I read the installed `blueprints.zip`, resolved native English strings, decompiled selected classes from the installed `Mods/RanRomance/RanRomance.dll`, and read its localized story and readme.
I also inspected actual Drezen scene objects with the existing UnityPy environment, using `read_typetree` without editing a bundle.
The companion file `terendelev-recovery-records.json` contains exact extracted blueprint records, relevant resolved text, decompiled class output and scene-object records.
Its blueprint selection is intentionally broader than the final table because it includes producers and consumers of the relevant states.
No route, engine, installed asset or game state was edited.

| Source | SHA256 |
| --- | --- |
| Installed blueprint archive | `BE61C9B723EF06558DA8D7CFC7F0C7EA869F60BA9952EBBBBD116CF681863EA5` |
| Native English localization | `3289C3EBAB206BA6312D4C2D512C0B5623E52D7E2B86596074B81D355725AA75` |
| Installed RanRomance DLL | `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68` |
| Installed RanRomance localization | `534D49567F0172193CD78F9C56A7A9A8244021F1701E2EC46F0C04FDBFBBCF3F` |

## What the remains prove

| Evidence | Exact object | Meaning and limit |
| --- | --- | --- |
| Native scale | `816f244523b5455a85ae06db452d4330`, `Items/UsableSlotItem/TerendelevScaleItem` | A real item with one consumable charge and ability `a0fc99f0933d01643b2b8fe570caa4c5`; possession and historical acquisition are different facts. |
| Claw item | `66afc74ef27c7244eac8f8d376cd7947`, `World/Dialogs/c5/Mythic_Dragon/Items/TerendelevClaw` | A collectible remains item, not an actor or a contained consenting person. |
| Claw collection action | `fb2837505ee44d74aaf85930f58e7a53` | Gives the claw, hides the two collectible objects and starts the historical collection etude. |
| Claw history | `7ef78c8e02070af428efe1dd851ec8a1` | Records collection; does not prove the item is still held, a complete body exists, or the soul is available. |
| Claw placement | object `af06ac61-082a-4ee7-a212-bc1ce4106da9` and collectible `e5c32f92-532c-47db-8f58-1d245d904ed3`, scene `980ea854dc0068d49b61d9b55840b3b1` | Concrete GibberingSwarmCave placement used by the collection action. |
| Iz Ravener death | `42e220d5dadc4dfd8bb3ef23cae832eb`, `MonsterDead` | A separate native encounter outcome, not equivalent to the prologue death or claw acquisition. |

`MonsterDeath`, etude `78d1192512994d14a8d89a145a4f52e9`, watches the monster summon pool `79e0b16b3fd0452694725e7736330c88` and starts `MonsterDead` through its death action chain.
That chain also reacts to Galfrey's Iz history.
A recovery must not replay or reset the death trigger, encounter reward or Galfrey consequences.

The Storyteller's previously extracted scale and claw account describes an earlier recovery from corruption.
The phrase spiritual resurrection in cue `4e1d9c5a6266ce8479c10e5359af0505` is not a present bodily revival.
Use those memories as identity and quest connections, not proof that a living NPC has been produced.

## Native states that must remain distinct

### Aeon survival

`TerendelevSaved_Aeon`, `bc62db9c34c4db149839dd21d1ab74f1`, starts `TerendelevWasNotKilled`, `6b98ec3e704599149b99fe70b5f793ab`.
The latter starts additional Aeon events, including `TerendelevIsWaiting`, `ad93ab4513ad28b4da4a813c21585838`.
It is not an isolated resurrection switch.
Iz's native Ravener spawn condition `1723f44914984c589cb8f4dfdeed2c51` explicitly excludes that history.
In `TerendelevPresent/Cue_0006`, `a0d4e597a9e31634d9b50d422fd98b8c`, she remembers that altered history saved her life.
Other responses distinguish Wardstone and Kenabres outcomes.
Starting the Aeon etude for a Trickster would claim a changed invasion history and affect the Iz actor, not merely provide a date.

### Gold Dragon awareness and continuing unlife

The native remains dialogue is `0b94776090cc19d4aac93403f213f326`.
Its successful cues `46364194f8ec50d41a4a155014163e34` and `6d05bf7a533c88941af68f4af531c27e` start `TerendelevAlive_Dragon`, `6c31fca14a4c4fb499f5eccee5eda148`, and play cutscene `4122b74d2ae742bbacca6ffae218189d`.
That etude starts `TerendelevResurrected_InDrezen`, `6137be58fd204800b536a13587093008`.
The latter requires Chapter 5 playing, is linked to Drezen and spawns, unhides and relocates its scene actor.
Its priority-zero conflicting group supersedes a priority-minus-100 default actor hider.

Despite those names, this is still undead Terendelev.
Her companion cue `2c706e4948f23b54a9b87f42cc3cd5f6` explicitly describes ongoing unlife, corruption, hunger and torment.
Cue `26bbcd4a566488544b8709104c55fd1f` recalls regained feeling and a brief soul connection, not restored flesh.
Threshold consumers explicitly label the branch as good undead Terendelev and spawn the undead unit.
This audit therefore rejects `Alive_Dragon` as a sufficient living-romance predicate.

The native choice to leave her at peace also matters.
Cue `5154537385346534ba337a1157c687be` says the eye fire goes out forever.
Any later recovery from that history needs a new, explicit authored explanation and her own answer; the earlier lingering-soul observation cannot be assumed to persist indefinitely.

### Lich binding

Native remains dialog `e17f0bf3b6454a0419f3232b5979f8c6` begins with cue `21ffae2a289a3a048b1c3cd6869cf8e2`.
It establishes that her soul has not yet departed for Pharasma's judgment at that encounter and offers enslavement.
This is a local opportunity, not proof that her soul remains unjudged after every subsequent outcome.
Cue `3b0ea80d1c383af428addeb0a59e4289` makes clear that merely telling her she is free does not release the binding.
`TerendelevInZiggurat`, `85a90025d84c2b34ab7abfcfebf7a363`, and `TerendelevUndeadInCapital`, `a4fbd26974c84e04da3b050574ad9d19`, describe that separate service history.
Coercive service is not romance consent.

The Lich dialogue attributes the desecration to Areelu, while the Gold Dragon dialogue describes Deskari raising and commanding her.
Retain those statements in their speaker and branch context rather than silently flattening them into a newly certain causal sequence.

## Actual Drezen actor verification

The actual `drezencapital_default_mechanics.scenes` bundle contains both distinct spawners.

| Placement | Scene object evidence | Native identity |
| --- | --- | --- |
| `TerendelevResurreted_ch5` | GameObject 184, spawner 2118, unique ID `9f16b2f6-1ea8-4fa0-b527-ecf4193c71d9` | Unit `59e7482d41d058a4bace7434c67a08be`, `Terendelev_Undead` |
| `TerendelevUndead` | GameObject 210, spawner 2174, unique ID `3029760c-a252-4c8d-a5e8-60feb18a002c` | Unit `376195cab0179734880947969d2b4e9c`, `Terendelev_UndeadInCapital` |

Both have SpawnOnSceneInit false and RespawnIfDead false.
Both use scene GUID `3e2b5ea054cd5b2479e7f13134363ef4`.
The first has actual dialog component 2117, dialog `56fcb96dabc9f114fa48828b86857d18`, with no component condition.
Its spawn action holder `56a634605f356f24399276283914f677` only switches the spawned unit to cutscene-neutral faction; it does not restore a living body.
The Lich actor has dialog `8aadf67a408b8ad478a3e025f0cea902`, condition holder `454a16ada116b8548b605976d3baa06b`, and initially hidden optimization state.

The native living-form blueprints exist: human `9e8401e7703907e4d94189d5992dd13e`, silent-caster human `045e2ea911644fa0abaa2f6c76b83feb`, and dragon `1ee55895e5091bc459d540d42a72bd2c`.
Their availability as blueprint resources does not supply an independently persistent restored person.
The prologue or Aeon entity must not be resurrected indiscriminately by searching for any unit with one of these blueprints.

## Existing RanRomance owns the acquisition and endings

The installed mod defines its own usable scale `5230fdfb34834955a25fc04c5aa290fe`.
It is distinct from the native consumable scale.
`RanRomance.Tere.Main.Configure` patches the Iz corpse-deactivation command `8ad726870ff6467f86db61f9d95d1276` and remains action holder `601429c7f2e928f42bc21b823ce6e592`.
Its route condition combines absence of Aeon survival, possession of the mod scale and a seen earlier dialog `31a4cbf9316542858c3d03f757a32245`.
When that branch applies, it directs the remains to the mod book `ad7d32c6c1c64f28a98241d41e880116` and suppresses competing native Gold Dragon handling.
The native remains action first hides the interacted object.
A second independent action-list replacement could consume the encounter before the original route runs.

Relevant mod states are `RanRomTereRom` `00a4899cba2c46038f9309d12525262b`, `RanRomTereOath` `f17a1d19d1b34a9fa469bdfcf819028f`, `RanRomTereBound` `e9e0e0efcdf74f6480915983a4a19704`, `RanRomTereRavener` `274d1b1f473344b3a741614bd1910514`, `RanRomTereAeonScale` `615479a8a3d3462a9855ff54895a02ee`, and `RanRomTereLichBind` `bbe7d7dbb92a4923a1ca4433e626a5ec`.
These names are identifiers, not interchangeable proof of restoration.
The oath is only a promise to try to return.

The ignored-Ravener book is `1fa63c8eb0344d5a82a547b7d196d4ea`.
Its actual text leaves her in a replica Kenabres, unable to leave that fake city, with the scale still the means of contact.
It offers continued courtship there, not a physical return.
The returned-person finale is `10aa555cd8d94da39977b09e0d848d77`.
Its actual text has Anevia arrange a meeting by Drezen's gate, Terendelev discuss recovered memories and soul damage, and optional courtship with physical flight and a ritual.
This is already authored restoration content and should be inherited rather than retold.
The inspected finale construction creates a book event and completes an objective; it does not itself establish a persistent new world actor.
I have not certified that no other mod component can affect a related actor.

The route quest is `a1d66e27b73d4d819d138868d681280b`.
Objective `58cc5ac6231342f8b0724371a3bcc8a3` ends the returned-person branch; `60914070543e4df4bf3ed47c64f029a5` ends the scale-confined branch.
Both finish the same parent quest, so parent quest completion alone cannot identify the result.
Use exact objective history, or an independently verified terminal cue plus completed quest, before joining a continuation.
Returned finale terminal cues include `8bf0fdc74bae4ef79dcfe04036e813ab`, `4791f49d19624dafa2ea1ae6dd18c588`, `30b3341acced4fa793dcc92dfe3587a9` and `10fe0c7bd80d441c8688c37babc19f66`.
The scale-confined terminal page is `97e317a64b8349b3940e858b7707c078`, with branch-specific cues preserved in the extracted decompilation.
A StartedDialogs predicate is insufficient because it records entry, not completion.

## Concrete next integration

1. Bind the native outcomes and existing mod outcomes read-only after RanRomance has registered its blueprints.
Add optional-dependency handling so absence of RanRomance never creates phantom completion flags.
Use existing Etudes, SeenCues, SelectedAnswers and CompletedQuests facilities where they accurately represent the selected join.
If the join needs exact objective completion or current scale possession, add only those typed read-only predicates; do not infer them from a similarly named authored flag.
2. Preserve the mod scale's dispatcher and both finales.
Attach a new explicit continuation choice after a proven terminal outcome or through an additive scale invitation.
Do not reset old dialogue history, romance preference or the existing quest to make the new arc available.
3. Give current Trickster a bespoke intervention on the still-confined branch.
An authored trial can make the copied city's boundary answer the scale's real provenance, using the claw and memories to establish identity and the Ravener history to establish what remains separated.
She chooses whether to leave before the intervention commits.
The trick changes the prison's boundary or repairs a divided identity; it does not make her earlier choice or affection inevitable.
This is a proposed authored event, not discovered native magic.
4. After consent, perform one explicit physical restoration transaction with a saved entity identity, destination and verified postcondition.
Do not set `TerendelevWasNotKilled`, `TerendelevAlive_Dragon` or a romance flag to stand in for that transaction.
For an already returned RanRomance history, introduce physical delivery without claiming to resurrect her a second time.
5. Write aftermath appropriate to what happened: an intact Aeon survivor, a person remembering Ravener atrocities, an aware undead person, an escaped scale-bound person, and a soul previously coerced cannot share an unqualified recovery speech.
Other mythics retain their existing restrictions.
A later genuine change of mythic path or unusual edited history needs an explicit reconciliation path, not blanket guard removal.

The smallest actual engine dependency for a new living body is a narrowly scoped persistent NPC materialization and verification service.
It must reconcile the intended Terendelev identity against native Aeon, Iz, aware-undead and Lich entities; create or adopt the designated living entity once; retain a stable save identity; restore contact after area loads; and report success only after the correct living, nonhostile actor is observable.
The current companion-revival service assumes a retained player companion and is not sufficient for her scene-local dragon bodies or a scale-bound soul.
This does not call for a generic NPC resurrection framework before the first implementation.
It does require one complete, tested Terendelev transaction rather than an unverified Spawn plus success text.
Native historical consequences and consumed remains should remain recorded.
Any removal of an incompatible old actor must target its verified entity, never all units of a broadly shared blueprint.

For a player who missed or consumed the scale, the claw history offers an investigation lead but not a replacement soul.
A supplementary Storyteller/remains acquisition path must be authored and implemented if every Trickster playthrough is to remain attainable.
Neither this research nor the existing scale route alone satisfies universal late-install access.
A departed or explicitly released soul requires new story justification and a voluntary return, not a fabricated continuing-presence predicate.

## Required verification before claiming recovery

Test real prior histories: native scale held or consumed, mod scale present or missing, claw collected or absent, Ravener living or killed, remains unexamined or already consumed, each existing mod finale, Aeon survival, Gold Dragon awareness, Lich service and explicit release.
Verify that only the intended native/mod branch is offered and that collection, combat, Iz, mythic and romance histories remain intact.
Replay interrupted restoration and reload before and after the physical transaction; prove one entity, correct identity and no repeated reward or resurrection.
Leave and revisit Drezen and Iz, checking for duplicate or hostile bodies and unchanged native plot reactions.
Test the new entry alongside RanRomance's actual post-patch dispatcher, not only vanilla actions from the archive.
A headless managed check can verify bindings, constructed conditions and transaction bookkeeping; a real saved-game run must still verify entity persistence and contact across area transitions.

This report establishes concrete native and mod resources for implementation.
It does not deliver a resurrected actor, new romance scenes or a full-route approval.

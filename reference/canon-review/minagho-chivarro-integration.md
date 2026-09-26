# Minagho and Chivarro installed-route integration audit

Audited 2026-09-26 against the installed RanRomance assembly and English localization.
This is a source and content audit with a continuation proposal, not an authored route, runtime certification or literary approval.
No installed files, shared manifests, story sources, art or generators were changed.

## Finding

Continue the installed Minagho campaign and its existing Chivarro relationship.
Do not write a second first courtship or a second brand-removal quest.
RanRomance already supplies three Chapter 5 book events, a specific Trickster solution to the brand, and several endings in which Chivarro joins the Commander and Minagho.
Those book events do not stage Chivarro's arrival or let her negotiate a relationship with the Commander in person.
Her return and individual desires are the largest opportunity for new played content.

The existing pair's attraction is both native canon and parent-mod history.
The Commander's involvement is parent-mod alternate development, with different implications on different branches.
Minagho's prediction that Chivarro will agree is not a substitute for Chivarro choosing in a new scene.
Likewise, a parent epilogue promising an eventual group relationship is not proof that the three have already met during the campaign.

## Sources and reproducibility

The installed assembly is `D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/Mods/RanRomance/RanRomance.dll`.
Its SHA256 is `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
The installed `LocalizedStrings.json` SHA256 is `534D49567F0172193CD78F9C56A7A9A8244021F1701E2EC46F0C04FDBFBBCF3F`.
I decompiled all 34 `RanRomance.Mina` classes and the relevant main initializer, Anevia and Storyteller dispatchers, shared etudes, revisions and epilogue setup with the existing ilspycmd.
The initializer calls `RanRomance.Mina.Main.Configure()` before the dispatcher configuration and final revisions.

I read the configured Minagho English text, including all three events and their alternate endings, alongside the native character extracts.
`reference/story-review/Minagho.txt` has SHA256 `2394A4CF2FC8AA1E688A075286B9A8986995DF696B45C5D17FB5334980BB6C67`.
`reference/story-review/Chivarro.txt` has SHA256 `AF5806C049CACE02699DCF60A40A8106857DB1B0634B27BD9E809F848E0FEB2D`.
These two files are native localization evidence, not the configured RanRomance book manuscript.
The latter was read directly from installed localization and matched to actual `SetText` calls.
The localization file contains line comments and a trailing block of notes; the count uses the decoded JSON array and excludes that trailing note block.

Isolated witnesses are in `C:/Users/Z/AppData/Local/Temp/minagho-chivarro-audit-atdsfopu/`.
They include the fresh decompiled classes, `english.json`, `english.txt`, `parent-map.json`, `native.json`, `native-contact-consumers.json`, `counts.json` and `check.py`.
Native text resolution includes `Text.Shared.stringkey`, because several important departure cues have an empty `m_Key`.
The audit read 1,144 relevant native blueprint records and separately scanned consumers of the contact and death bindings.

Run the bounded structural check from the project root with:

```powershell
& reference/asset-extraction-env/Scripts/python.exe C:/Users/Z/AppData/Local/Temp/minagho-chivarro-audit-atdsfopu/check.py
```

It passes against the frozen installed DLL, configured text counts, acceptance and Trickster answer bindings, dispatcher hooks, and native gate/delivery records.
It does not run the parent game dialogue engine or prove live scene placement.

## Parent campaign and exact progress

| Role | Binding | Actual meaning |
| --- | --- | --- |
| Book 1 | `91a3699b2b12496db23b33dad6746d31` | Minagho's apparent ghost in damaged Drezen, request to remove the brand, selected method or refusal, optional first intimacy. |
| Book 2 | `3b03b32bf11a431094a68776dc459065` | Half Measure meeting, history discussion, cult proposal and possible conscience/redemption development, optional second intimacy. |
| Book 3 | `32a15058781144dcb6bfcf440ab13236` | Immediate pursuers resolved, plans to stay or leave, Chivarro messages, and optional continuing romance. |
| Parent quest | `5cd5f22437a1465180b45c080899577a` | Demonic Influence; final objective is `f7f9ceff5eff4cb3aa5822726585f2a1`. |
| First timer | `faad12cd8c8048309acb37896d8fafc3` | Four-day delayed completion and objective delivery; follow-up checks Completed. |
| Second timer | `d5e4f2aa713647cc8d40438b46e0d1ef` | Four-day delayed completion; follow-up also checks Completed. |
| Initial Chapter 5 gate | `f694258862674009bd7dea2091d74bab` | `RanRomC5MythicCompl`, a parent etude whose activation includes Chapter 5, mythic-quest state checks, a witnessed dialogue and a Swarm exclusion. |
| Native Iz quest | `95ff7d975689fcf44b085d10907e711d` | Complete is required for the first parent invitation. |
| First intimacy | `552e473e6d674d2bbb5b92ac615b838d` | `RanRomMinaSex1`; starting/completing adjusts parent `RanRomCount`. |
| Second intimacy | `73423d82afce42eb8f6e0c44121010dc` | `RanRomMinaSex2`; required for Book 3's romance page. |
| Continuing romance | `b5c19cd01e364df99f6c946c7da14751` | `RanRomMinaRomance`, started by actual acceptance answer `56056c49915d468e9a6b469260dd42b3`. |
| Final rejection | `fd4e6bbef0d4445b8bee465524698520` | Completes Sex1 and Sex2; does not start the romance. |

Book 2's intimacy page requires Sex1 Playing.
Its acceptance starts Sex2; refusal completes Sex1.
Do not infer a current romance from having met Minagho, having spared her, or having accepted sanctuary.
For a continuation after the completed relationship event, read the actual terminal cue as well as the romance etude.
The romance terminal cues are `5584da70433e4f079d521d40ce77f230`, `c01f7f83a2584555b2f551918f169cdb` and `4dbb41f1fb134b90ab3900dc05488e8f` for the softened, demon-service and other branches respectively.
The non-romantic terminal is `19099aba216e46e98d446709c3f2e0f3`; rejection terminals are `c51a76731dc24865b6c472ffe6bf3e18`, `341b62dd58d14906959d3262b12f1a43` and `98baa5299ae444bfa1ac8ba8e84f2c7c`.
DialogSeen alone should not manufacture a completed conversation after an interruption.

Parent outcome etudes must stay distinct:

| Name | GUID |
| --- | --- |
| RanRomMinaBanner | `4a29c758798d47a1a32f506d1ca6081b` |
| RanRomMinaConscience | `813cc79c053d4b3e869a0d0ca2f3d85d` |
| RanRomMinaFreed | `f18391398cb5470c94f8932e9d8d2fd7` |
| RanRomMinaDemon | `58557969a797441983022c8ba0400400` |
| RanRomMinaLegend | `a87da83417ff4be28c9ccfaf9b154e96` |
| RanRomMinaDragon | `e303c58d307849cd892fa5810124da92` |
| RanRomMinaSanctuary | `1e6ca1514807446ea2fddd65e4f5bcc8` |
| RanRomMinaCult | `3d21fa8120d040338ec1d4b8461fa536` |
| RanRomMinaRedemption | `592dcdccbef043f58031fa234faf137a` |

Conscience and Redemption are not synonyms.
A brand-free Trickster Minagho is not automatically redeemed, a cult leader, a permanent resident, or a member of the Commander's household.
Book 3 can explicitly state that she intends to leave Drezen.
A continuation must offer a credible reason for another visit and let her choose it.

The first timer has an additional parent completion condition checking that native Ember quest `49b7496143daed149ab4557a9684dd53` is not Started.
That is the installed code, not an intended Minagho relationship milestone.
Do not copy this condition into a new timer or assume that Completed proves four days elapsed in every parent save.
Book 1's finish actions also start that timer through an empty conditions builder.
Consequently, timer state alone is weaker evidence than the selected refusal, terminal cues and subsequent played books.
These are parent implementation concerns to reproduce in runtime fixtures if modified, not fixes performed by this audit.

## Existing delivery must be preserved

Anevia's native dialogue is `de4cc2dd71694b842be37b75d1705b83`, with native main list `33960c7f7af40cd43b7f801a76c87a0b`.
The parent replaces its FinishActions with dispatch conditions that start each unseen book after the corresponding answer was selected.
The three answer IDs are `a19476e2956b4d428613a46470e11b7e`, `627ebab39cea4235a376d5fdf82eeae7` and `1c5b340c7fda462b9497f95466c734fc`.
They live in parent list `31c23fd4f954444fb18673e78bf6718f`.

Storyteller's native dialogue is `bf328bcec67a5014f9a56ee6220f3bcc`, with native list `2f5b7e0b76d3c5a42a431e1e33a8db09`.
His corresponding answers are `6fd942ab20644c5a94a92c25dd700dd5`, `0fa6df22921b4e8d8178f33fa56f99f5` and `904e03e8533349bfbe911ef5175f620d`, in parent list `bfb14ac649fb40bfab605f1d992001e5`.
The Storyteller path additionally requires at least one of AneviaNotInDrezen, AneviaDead, AneviaGone, PlayerKilledAllOnCoronation or CrusadersGone.
These are `6125c10886d6465091f4e092618ca55a`, `ba365d0ae03c414a8f6f906837a4fe91`, `09f46662bcd14a03a0874267e16d6e6f`, `9ce3448490564fbebed24d077f54f2b3` and `061d1dfd76f4ea74ea8aa4d013fc8016`.
It is an existing fallback, not a reason to summon a missing Anevia.

Neither dispatcher materializes Minagho or Chivarro as a new capital actor.
The books narrate meetings and use null-speaker StartDialog delivery.
The native actions copied into the books are music start/stop actions from `2da74626a86ff364f84bca24ba01662e` and `c589bdbed55b538449b02711d1a86aa3`, not actor spawn or teleport actions.
A continuation can follow this established narrated-book format through a verified available dispatcher.
If it instead offers a physical clickable visit, the new actor/contact lifecycle must be implemented and tested explicitly.
Do not label a null ContactUnit as proof that both women are present.

Append new choices and dispatch conditions without replacing either parent's existing finish-action collection or answer order.
Preserve the installed unseen-dialog guards, event callbacks and timers.
Both dispatchers must point to the same new event identity so switching between them cannot replay it.

## Native release, life and lost-contact histories

| Native evidence | GUID or entity |
| --- | --- |
| Chapter 4 Minagho unit | `23e9e36701934fcbbf3e1472091d9321` |
| Chivarro unit | `b7e819e2a9bb0804abcbffe8e7d91ba6` |
| Minagho after-combat dialogue/list | `ef7d64f0091305b4984dd1a9173f0388` / `82a0c2ad3e6dc41469ec66a7affdc486` |
| Chivarro dialogue | `70068cbd7746aca48add0715ee1278b8` |
| MinaghoDead | `3b8c0801d5e9a694b848ee13564d2ad7` |
| MinaghoKilledInFourthChapter | `a31e7428d8b5c28408eecebca8fa7746`, whose trigger starts MinaghoDead |
| MinaghoSetFreeByAzata | `1d466fd4271fdc14ea1c077760c63ca5` |
| MinaghoSetFreeInC4 | `978762feac7873d4e925d85202e2c89c`, whose trigger starts spared state `6d956cad1e71dc24c87fc06789b22ac9` |
| ChivarroHappyEnd | `71f85264d9064074f9cf74999ecbffa9` |
| ChivarroKilled | `fd2ab9b67ce3e284184b1894c82c6c5d` |
| ChivarroRemovedFormPower | `065b611752b5c0045b6d1e0164b92bcc` |
| ChivarroWasTeleportedAway | `806ece7bcf18a374e9ad1f7b9e3bc580` |

The installed Chapter 4 answer chain ends at `a08540bf69314cffb24d93d277cf6636`.
It copies the Azata release action from native answer `9038e82b2c55e124889a1a4458c62ec8`.
The parent also broadens native Chivarro answer `d12f5b2ef1b7e4c4db92a58a23fa4178` to accept that selected answer and removes its native PlayerIsAzata mythic requirement.
This gives a normal non-Azata player a real parent route into the reunion outcome.
A generic MinaghoSetFreeInC4 flag is not the same prerequisite as this specific installed release history.

Native Chivarro Cue0099 `791040da477de81489c51acb419b01c5` learns Minagho is alive.
Cue0100 `3a1b54106516d3849a62702ee2e84ff0` expresses her determination to find Minagho, starts HappyEnd and RemovedFormPower, and launches departure cutscene `05a2107011a09b84987eea5c6b1ae41a`.
That scene moves the Ten Thousand Delights Chivarro spawner `4324c735-accc-422b-86de-dd00990085ad` in scene `ce2df2f2e0ad8e74484478ac83f1d497` toward its exit and passes it to a further cutscene.
HappyEnd is not a capital-spawn instruction.

Minagho's native departure Cue0036 `55f9d42958f3914439458912baacb2b7`, whose actions the parent copies, hides spawner `622d7116-28d1-4341-ad3d-fee9fd2f6736` in scene `1b5e2227ad48c7a4f9073b58feb8bba5`.
Her release should therefore not leave a fabricated repeatable Chapter 4 conversation on the vanished unit.

Chivarro's displaced Lower City history is different from her voluntary departure.
The teleported-away etude spawns group `acd46f02-8efe-405d-b51d-65878172f71d` when the relevant objective has started, and activates the abuse-scene zone.
Its death trigger watches spawner `5d051d3f-d8aa-4047-a4b4-0ecd3b77fb6d` in scene `1b5e2227ad48c7a4f9073b58feb8bba5` and starts ChivarroKilled.
Native command `0e1214a51dc65f8498de079d799c7577` also starts that death state in the abuse scene.
RemovedFromPower alone consequently cannot mean killed, safely reunited, or available for romance.

The Fleshmarket etude `decab5093aaa4e78a36345545b3e094d` selects Chivarro or Herrax and separately hides/unhides the relevant actor according to office/death/history conditions.
The Chivarro spawner there is `a5f8ef89-4eb9-44fa-817a-661bfc94cd23`, scene `dea797b8ba927bb48b27d254989ef580`.
These are different native placements, not interchangeable proof of a permanent visit location.
This audit has not extracted their Unity scene components or verified their live interactability.

Dead, never-met, released without the qualifying parent answer, displaced-but-unresolved, and already-refused saves need separate acquisition/recovery work.
No such state should silently receive a completed parent romance or native HappyEnd flag.
An authored revival requires real delivery of the living character and acknowledgment of what happened, not deletion of a death flag.

## Mutual attraction and characterization

Native Chivarro Cue0104 `a7ad7b26bc30b2c42bf8163c48e4a667` ties her ambition and ability to direct chaos to a formative encounter.
Herrax's account describes the women's rivalry becoming an attachment, including their walking together affectionately.
Chivarro's attempt to kill the Commander is connected to her belief about Minagho's fate.
The native paired epilogue, localization key `056942f6-32d0-4480-8ff7-29356b43db19`, reunites them centuries later on another plane.
An earlier meeting is a deliberate alternate development that needs a played cause.

Parent Book03Page002Cue0013 `b6eb0960f50f4f6ea0290ea2728b35df` says Chivarro plans to meet Minagho after checking she is not followed.
The romance-page question about Chivarro is answer `359d4d9df01b4dbebd71322cac3bfda3`, shown when HappyEnd is Playing.
Its responses differ materially:

| Cue | Meaning |
| --- | --- |
| `e15de525c99d40c6a6faf0afa61be756` | Minagho reports a lengthy exchange of communication scrolls and expects Chivarro to want to join. |
| `e8af7bdaaece4995bfe1e0e9eec871a9` | Demon-service Minagho predicts the Commander will make Chivarro submit; this is not Chivarro's voluntary agreement. |
| `80ad6d6f87d54a43b019e25f69df1c0c` | Minagho predicts Chivarro will be eager; it is less definite than the reported conversation. |

New dialogue must distinguish hearing one of those responses from merely having the underlying flags.
Chivarro can acknowledge her existing love and still resist being treated as Minagho's accessory or as an automatic gift to the Commander.
Her hospitality, appetite for influence, management of dangerous followers, and talent for making another person reveal useful information are stronger foundations than a generic redemption lesson.
Minagho's native massacres, manipulation of Staunton and humiliation under Baphomet remain real history.
Parent conscience, dragon and legend developments can change her direction without making an unplayed change universal.

The first three events contain substantial Minagho discussion, but little direct Chivarro agency.
Their joint continuation should include mutual teasing, a genuine professional disagreement and actions showing why they keep choosing each other.
The Commander should be able to desire either woman, both, or neither without dissolving their attachment by default.
New intimacy should be adult, voluntary and non-graphic, with a real slower or non-romantic alternative.

## Ending integration

| Parent page | GUID | Principal scope |
| --- | --- | --- |
| Slide0001 | `951e4432cf844a36a8a222b27589fb43` | Banner connection and group ascension; redemption/cult/other variations. |
| Slide0002 | `6db8635856e74b6cac46330bd82b4ff5` | Redemption; Commander ascension, Heaven, ordinary life or sacrifice. |
| Slide0003 | `8df5edb6f69040c69d7da78d2bf20cb6` | Cult with parent RanEpilEvil Playing. |
| Slide0004 | `5a5865ceca0e42049288351a76b18ba9` | Cult with RanEpilEvil not Playing. |
| Slide0005 | `126762ac92364ac5bdec69c6e3fdfd1a` | Demon-service without cult. |
| Slide0006 | `01677da8df6e42c6b4803ceef524b1fe` | Dragon development. |
| Slide0007 | `9c5c5825bf3245d0ae763c6e69ecdc38` | Legend development. |
| Slide0008 | `3792457f35734d75a4d4b53055f7f5d0` | General fallback after Book 1, subject to its specific refusal exclusion. |
| SlideAeon | `6bf016f775734c3eb4f287c29c59e9f9` | Separate rewritten-timeline sequence. |

`MinaEpil.Configure` marks all eight ordinary pages seen when one is shown.
`EpSetup` inserts them in numeric order, with a separate Aeon insertion into `ced82f299d246f448b48afa0b630dd70`.
Replacing an ending requires respecting that arbitration, not adding a second contradictory page afterward.
The parent suppresses native paired page `5c95d8e3fa4f3b44896914987cb04b0b` when Book 1 was seen and answer `b192e1e211654bcca27924c12e8aa617` was not selected.
That answer is a specific parent refusal, not a universal failed-route flag.
It is Book01Page002Ans0007, the refusal before examining the brand.
The later refusal after examination is a different answer, `e7913a7ee6e24d59944ab1638c22405c`.
Preserve both histories rather than treating the epilogue's single exclusion as proof that every other player accepted help or continued contact.

An explicit group example is Slide0001Cue0004 `9bfbb3f217ca476cadbeffc4d389717d`, requiring Redemption, HappyEnd and Romance Playing under the ascension page.
Other pages likewise vary the relationship depending on HappyEnd and Romance.
A later extension must preserve old endings for saves that never play it.
After a new group decision, a declined Chivarro romance or ended group must not fall through to an old ending that automatically makes her the Commander's lover.
Conversely, ending the Commander relationship must not erase Minagho and Chivarro's relationship with each other.
Special outcomes must cover actual death, sacrifice, ascension and Aeon history, including interruption before the new finale.

## Parent content accounting

Counts use the project's `tools/measure-story-content.py` normalization and word function on distinct configured localization keys.
They exclude titles, quest descriptions, generic filler and unused notes.
They include mutually exclusive branches, so they are aggregate inventory rather than one attainable reading length.

| Parent scope | Configured keys | Raw words | Exact-normalized-segment distinct words |
| --- | ---: | ---: | ---: |
| Three played books | 305 | 11,935 | 11,668 |
| Chapter dialogue additions | 10 | 495 | 495 |
| Alternate epilogue text | 72 | 3,784 | 3,517 |
| Combined parent Minagho material | 387 | 16,214 | 15,680 |
| Subset explicitly naming Chivarro | 42 | 1,726 | 1,497 |

The last row is a subset, never an additional contribution.
Name mentions measure neither her direct participation nor a complete Chivarro route.
The parent also reuses a 34-word native paired epilogue in Slide0008; keep it separately labeled as reused native text and count it once wherever the same native ending appears.
No direct Chivarro conversation with the Commander occurs within the three parent book events.

The parent corpus belongs in a separate integrated-parent inventory, not the authored expansion total.
Give each paragraph/choice one inventory identity and record which character it develops.
A shared scene can contribute to both character assessments, but its words must not become two copies in the project or group-route total.
For numerical per-character budgeting, separately report exclusive text and an explicit allocation of shared text; do not credit both characters with the entire 15,680-word parent corpus.
The three parent books are predominantly Minagho material and cannot certify Chivarro's 21,000-word end state.
Even Minagho's aggregate is below that floor, and aggregate volume alone does not establish RanRomance parity in playable depth.
Selected-path parent measurements still require an actual condition-aware graph walk or runtime transcript; this audit does not supply invented shortest/longest playthrough totals.

## Proposed continuation and integration contract

The next authoring contribution should be an eight-visit living-history arc after an actually completed Book 3, followed by further character-specific depth and the final outcome pass.
Aim for substantial played events rather than a fixed number of words per visit.
The full project requirement remains at least 21,000 meaningful attributed words per character, with a developed shared relationship rather than one woman's story credited twice.
A first eight-visit contribution will not automatically meet that end state.

1. **A message with two answers.** Minagho brings Chivarro's reply and proposes a meeting on terms that fit her actual plan to stay or leave.
   A reported-scroll-history branch can remember that exchange; other branches establish it now.
   The Commander chooses a meeting, postponement, individual interest or no further courtship.
2. **Chivarro arrives on her own terms.** She reveals what she gave up and what she retained after losing the Delights.
   Her reunion with Minagho is affectionate and abrasive before either discusses the Commander.
   She directly accepts or declines prospective intimacy, without a promise extracted through shelter or protection.
3. **The surviving clientele.** A former contact offers Chivarro useful access in return for names and obligations she once controlled.
   She wants influence rather than a lesson in humility; Minagho recognizes an opportunity to plant false information against a remaining Baphomet intermediary.
   Their preferred plans conflict for reasons beyond jealousy.
4. **The convincing lie.** The player helps inspect a concrete message and choose how much of the trap to expose.
   A knowledge/perception or persuasion check changes what is learned and which plan costs more.
   Failure and a non-roll route still produce a coherent attempt and consequences; no check determines whether a woman consents.
5. **The price of being useful.** Play the result with the contact rather than merely report success.
   Chivarro can preserve future access at the cost of a concession, or destroy that access to deny the intermediary leverage.
   Minagho's cult, redemption, sanctuary, legend, dragon and freely released histories change what resources and objections she actually has.
6. **One evening, three intentions.** Their mutual attraction is visible in a shared activity and disagreement they resolve themselves.
   Offer individual time, a jointly chosen non-graphic intimate evening, slower affection or friendship.
   Existing Minagho romance is acknowledged; new Chivarro intimacy requires her own played choice.
7. **What she keeps for herself.** Give Chivarro an individual visit about the future she wants beyond being someone's second-in-command.
   Give Minagho room to disagree without the Commander becoming the judge of both women.
   Resolve the business consequence and the concrete remaining obligation established earlier.
8. **Before Threshold.** Play a farewell and future decision appropriate to the selected individual or shared relationships.
   Finish this arc's promises and earn the new ending arbitration, while retaining truthful outcomes for unfinished histories.

The eight-visit arc should be followed by the measured character-specific additions needed for equal depth, especially Chivarro's independent ambitions and sustained relationship with the Commander.
Do not obtain the remaining words by proliferating alternate endings.

Root-owned integration should provide a shared parent-history reader, append-only dispatcher entries, terminal-cue witnesses, native life checks, cross-dispatch replay protection and ending arbitration.
Authored scene flags should use a new namespace and never overwrite RanRomMinaRomance, HappyEnd, parent timers or native death outcomes to simulate progress.
Physical scene delivery needs both actual contacts through the paired-contact mechanism if physical units are used.
Narrated book delivery needs an honest available dispatcher and explicit authored travel/arrival, not an unsupported claim that two native capital actors spawned.

### Bespoke Trickster access

The existing brand trick is answer `a741a92a6b604b2ca646770c6b6f8876`, with result cue `a8f7a881cc6d427b91cbbee14f43e0ee`.
Its requirement is completion of `653c8dec252da8d4b872d87e6f656cf2`, the Chapter 5 Final Laugh Trickster quest.
The trick interprets responsibility for Minagho's failure literally and lets her own blood satisfy the brand's condition.
This already works as a specific character-connected fate intervention in the parent fiction.
The proposed continuation should let the player use that history in a new contest over a misleading pursuit or invitation, with a mundane alternative and consequences.

For missed living histories, a later Trickster invitation could make the same intercepted pursuit message reach its intended recipient despite an adversary's tampering.
For a displaced Chivarro, investigate the actual Lower City fate first rather than treating loss of office as her death or reunion.
For dead histories, a future restoration arc can connect the false report of Minagho's death, Baphomet's conditional brand, and the women's interrupted search for one another.
Those are authored story connections, not verified native resurrection mechanics.
Before calling those routes attainable, implement the recovery object/event, actual living-character delivery, duplicate prevention, refusal and retry behavior, and save/load persistence.
Do not grant Azata powers or retroactively select the original Chapter 4 answer for a Trickster who missed it.
Other mythics retain their actual parent method and appropriate restrictions; the new arc must not turn every path into the Trickster exception.

### Nonexclusive relationships and verification

Keep ToyBox Free Love and no-jealousy behavior compatible by leaving other romances and their counters untouched.
The parent already acknowledges other partners and changes `RanRomCount` through its own Sex1 lifecycle.
Do not duplicate those increments in the continuation or use another romance's existence as an exclusion.
Differences over power, privacy, information and loyalty can drive conflict without a compulsory exclusivity test.

Before integration, test real earned parent histories for romance, declined intimacy, final rejection, sanctuary, freely released Trickster, cult, redemption, legend and dragon paths.
Separately test Demon-service history without interpreting domination as Chivarro's agreement.
Test both dispatchers, switching dispatchers, absent/dead dispatchers, lost and dead women, completed versus playing timers, interrupted books, duplicate entry, changed mythic state and old saves with no extension flags.
Verify old epilogues remain intact when the extension is unplayed and become mutually exclusive only when an earned new outcome supersedes them.
Inspect the full manuscript for native versus authored claims, then run independent writing, characterization, mature-romance, gameplay, continuity and length reviews on the delivered revision.
Runtime actor/contact checks, art identity/crops, TTS reading and actual selected-path measurements remain required work.
No scores or readiness approvals are assigned by this audit.

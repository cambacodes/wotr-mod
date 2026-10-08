# Nidalynn dossier — stage 1, existing route only

Prepared 2026-10-07 in `/work/wt/RRT-redesign-nidalynn`. This is a research dossier for the existing implemented relationship `nidalynn`, not authority for new mechanics, gates, prices, attraction requirements, native rewrites or route redesign. Stage 2 must derive its state table from the generated export; stage 3 is constrained by the pinned r4 findings.

## Scope and authority

Read sources: `/work/Writer/plans/route-redesign-pipeline.md`; `/work/Writer/handoffs/00-WRITING-GUIDE.md`; `/work/Writer/handoffs/CHARACTER-TRUTH.md`; `/work/Writer/TRICKSTER-RUBRIC.md`; `/work/Writer/handoffs/POLISH-AGENT-PROMPT.md`; `/work/Writer/handoffs/trickster/nidalynn.md`; the four existing `storylines/*nidalynn*.py` modules; `development/Story.json` relationship `nidalynn` and `nidalynn.*` consumers; `/work/Writer/judging/codex/nidalynnr4.json`.

`tools/route_packs/nidalynn.md` is absent in this worktree. Its existing pack was read from `/work/wt/RRT-route-packs/tools/route_packs/nidalynn.md`; no pack was copied or changed. The rubric is at `/work/Writer/TRICKSTER-RUBRIC.md`, not beneath `handoffs`. The pack is preparation evidence, and its historical supplemental scorecard does not supersede the pinned r4 audit.

Canon was verified directly from `/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`, decoding archive records and all Python text reads as UTF-8. Source records C01–C35 below give exact archive paths, full blueprint GUIDs and localization keys; S01–S17 give structural records without invented localization keys. References to C/S records in this dossier mean those precise primary-source witnesses, not the abbreviated hashes in old handoffs. No internet secondary source is used.

Implementation ownership remains the existing modules: `nidalynn_trickster.py` holds three entry devices, presence, meeting, reactions and ending assembly; `nidalynn_kiln.py` holds rescue, public confession, custody and consequences; `nidalynn_salt.py` holds chosen form, attraction, proposal, intimacy and aftermath; `nm1_nidalynn.py` moves existing visits onto physical hubs and creates four chosen-form twins. The generated export is authoritative for assembled conditions and appended shared paragraphs. The inspected export contains 49 scenes with relationship exactly `nidalynn`; other `nidalynn.*` consumers include Last Call and household/framework facts. This dossier does not publish dormant manuscripts.

## Binding constraints carried forward

1. Explicit player kills, condemnation and deliberately chosen closures stand. Trickster coexistence does not undo the player's own decision. For this route, unprimed smashed/cooked clutch and burning the straw egg are recorded standing closures, not missing rescue obligations.
2. Matrix `user_decision` rulings are binding closures/entry conditions, not automatic INT/TRK/HOW/COX defects. Old audit complaints about unavailable entry in those worlds authorize no extra door.
3. Presence must be earned and current: a departed/lost woman gets no living household, romance, Last Call or postwar appearance without a matching earned return; an unreturned fatal Commander sacrifice gets no living postwar page. A remembered cost is not an actor-presence claim.
4. Canon changes, producers and dependent native rewrites apply only on the current Trickster path and remain inert elsewhere. Later consumers may read an earned historical return where the existing policy permits. Preserve adult, character-specific appetite and consequential refusals; evil women in shared scenes retain evil values and methods. Nidalynn remains good.
5. Earned, discoverable gates and lock-in points may legitimately exclude runs. The happy path may not leak into a history that never paid/acted. No route may require another romanceable woman's death, hostility, departure or closure.

Shyka's page is an in-world paid gate, never rescue, affection or agency by itself. No new echo is authorized: preserve allocated unique sense/misstep and costs; no vision/another-life/player/save/route justification. The existing Nidalynn theft does not require adding an echo. DLC-tier additions are allowed only insofar as the existing scope already contains them: label authored facts, keep scale and in-world explanation, reconcile dependent native content only where that event explains it, Trickster-only and save-safe. Keep scene/node IDs, choice indices, GuidFor namespaces and existing old targets; eventual choices may only be appended where separately authorized. These stages authorize no code or test edits. The task's intimacy cut at the start of explicit acts overrides the rubric's more permissive graphic register.

## Canon identity, agenda, appetite and voice

Nidalynn is a female Lawful Good silver dragon (S01; C13/C33). Her native chapter-five encounter is the Gold Dragon DragonAwakening sequence in rebuilt Kenabres, not an earlier Trickster appearance (C30–C31, S03–S05). She performs a distressed pregnant woman in a worn dress (C01), asks for specific cheese (C02–C03), rejects inadequate help sharply (C04/C06), and later admits she enjoys jokes/games and helped devise silly requests for Halaseliax (C12/C14). The in-game disguise is a spawned encounter actor; the dragon unit is a distinct blueprint (S01/S03). Native text does not establish that she is actually pregnant.

Her concern is the survival and memory of ordinary Sarkorian life: Windstep artisans, Reudger's cheese, mares in peaceful fields, the common folk as Golarion's salt, and sharing remembrance with Sarkorians (C05/C07–C10). This is an independent goal, not an excuse to orbit the Commander. Her direct moral position values kindness, sincerity and action over polished speeches (C11/C13); she can rebuke and refuse rather than acquiesce automatically (C04/C06). Her native druid/dragon disclosure links her to care for the woundwyrm clutch on the Gold Dragon path (C15/C27); extending that concern to Trickster is authored, not evidence of a native Trickster actor.

Her canon appetite is emphatic: cheese craving in the role, enjoyment of food and jokes, savoring a real meal, demanding gratitude (C02/C12/C13). Preserve practical, tart affection and playful pride; feeding is one expression of care, not her entire personality. Her bodily/romantic desire in the snowfield, embarrassment before the reveal and attachment to the Commander are existing authored growth, not native romantic facts. She chooses her own face, initiates the relationship and keeps the kiln and her step instead of becoming a displayed citadel ornament (`door.own_form`, `wall.wings`, `ridge.first_flight`, `ridge.snowfield`). Her own goals remain caring for the hatchling, preserving Sarkorian names and protecting people from lies that punish them.

Voice targets are exact source lines, not new player prose: C06 “Is this a joke? Are you trying to play a trick on me?”; C11 “it's what you do!”; C13 “You must also sustain your body!” and “be grateful!” Her good alignment does not require therapy-speak, HR bargaining or modern ethics exposition. The goat confrontation is a concrete native-compatible moral stance: she owns her mistake, supplies milk herself and will leave rather than raise the child on a lie that gets sentries flogged (`kiln.the_goat` and `.chosen`).

## Native timeline and usable hooks

| Timing / native event | Verified primary witness | Existing implemented use |
| --- | --- | --- |
| Chapter 3, Ivory Sanctum golems hold the clutch under fists | C16 + S06 `AnswersList_0002` | `eggs.lamp_black` inline, current Trickster; native answers still decide the other eggs. Return goes to C20; failed retrieval returns through C17→C18 to native hostile combat. No invented golem perception rule. |
| Clutch examined/destroyed/left for Drezen | C21–C26; S07–S08 | `eggs.seen` is cue observation; `eggs.destroyed` and `eggs.project` read native etudes. C25 destruction actions are OnShow; older handoff OnStop attribution is stale. |
| Drezen eggs awaiting native decree | C26/C27/C28 | `eggs.vault` after latch `eggs_crated` from `eggs.project`, chapters 3/5, before druids/cooks/destruction; existing rest-delivered fallback. |
| Native druids decree completed | C27 + S09 | `eggs.straw` after `eggs_given` latch from `eggs.druids`, chapters 3/5; cold twelfth egg and four carriers are authored. |
| Chapter 4 supplies through Storyteller portal | C29 | `letter.from_the_kiln`, observed `storyteller.supplies`, `reachable_by_letter`; supplies carry the letter, not a summoned in-person Nidalynn. |
| Chapter 5 Gold Dragon native cheese/reveal sequence | C01–C15, C30–C31, S03–S05 | Canon reference and voice only. Existing Trickster courtship is not the cheese quest, chalk-label gate, magical appraisal or priced second ask. Those old devices and Fye placement were superseded. |
| Chapters 3/5 authored Drezen presence | S10–S11 for copied bodies; export Presences | Widow/chosen-form hub opposite existing jeweller in Drezen; no claim that this is native Nidalynn placement. |
| Late commitment / Threshold / epilogue | Existing generated `Derived`, ending scene/page conditions | Proposal and Last Call are authored and earned; apply current availability, route-open, ordinary/late payoff and sacrifice/return history. |

Native Gold Dragon boundaries: `DragonCh5` requires Chapter05 playing; `DragonC5Quests` belongs beneath that etude (S04–S05). The spawned woman's action checks the dragon requests objective (S03); cheese objective belongs to chapter-five DragonAwakening (C30–C31). Native sequence proceeds from fetching genuine cheese to remembrance/riddle, then the dragons' revealed lesson and reward/rebuke. Nothing here creates a native Gold Dragon romance or moves that native event to Trickster.

## Existing authored device, costs and consequences

The clutch is attributed to Devarra by the native killed-dragon inference (C22), the golems addressing the dead dragon about “your eggs” (C34), and the native Ivory Sanctum dragon name (C35). This is a sourced inference, not a claim that C22 itself names her. The old handoff’s enGB `9a2a13a5-05be-4c14-b727-2cd745ee8ea3` (“You saved Devarra’s eggs.”) exists in localization, but no owning archive blueprint was found in the direct scan, so it is not used as a complete blueprint citation.

The current joke is physical theft and concealment: save the smallest egg from under the golems' fists, hide it in ash, carry it as a “rock”; it opens contact, never affection. Historical F14 “impossible property” inspiration (C32) is not the current action or a new feature prerequisite. Three mutually distinct histories already exist:

| Entry | Existing action and check | Existing paid/exposed history |
| --- | --- | --- |
| `eggs.lamp_black` | Commander Stealth or Trickery DC22, current Trickster, native answer list S06 | Success sets `egg.clean`; failure injures hand (`cost.hand`) and calls native golem alarm/combat. Keeping sets `primed`, `egg.golems`, `egg_owed`; deliberately crushing sets `egg_crushed`, no courtship. |
| `eggs.vault` | Commander Stealth DC20, crated native clutch, before disposition | Failure is clerk exposure plus dropped lamp and rescue burns (`clerk_saw`, `cost.palms`); keeping sets `primed`, `egg.vault`, `egg_owed`. Chapter-five continuation folds hearth nights into same delivery. |
| `eggs.straw` | Commander Bluff DC20, after native druids outcome | Keeping sets `egg.straw`, `cost.slate`, `egg_owed`; failure adds `quartermaster_knew` and later public exposure. Never sets `primed`: downstream chamber/vault accounting differs. Burning bedding sets `straw.burned` and no debt or courtship. |

Other existing costs and history must remain separate: immediate hatching confession spends Favors −100 with golem/vault/straw-specific admissions; delayed muster confession spends Favors −150 and records the public lie first; preserving that lie closes the route. Giving the hatchling to the crowd closes it with its own aftermath. Relinquishing ownership sets `cost.claim_given_up` and enables chosen form and romance; keeping the claim has a later chance to relinquish, then a flight/departure closure if the claim remains. These are existing pivotal choices, not newly proposed gates.

Optional system costs are already authored: torc buyback Finances −50, caught theft buyback −100; hatchling goat feeding Materials −50; replacing the refugee's eaten goat or correcting the wolves story Materials −50. The wolf lie knowingly leaves a baby without milk and sentries facing flogging; refusing correction sets `goat.lie_kept` and closes the route. Optional alternatives have their existing consequences and need no extra price. Hand injury heals in function, retaining the existing scar/history; burns and exposure are not interchangeable histories.

Custody has a cost outside affection: all three retained eggs immediately set `egg_owed`; Devarra's later named bill is separately `devarra.trickster.cost.egg_withheld`, set by her own scene. Never invent payment/forgiveness from Nidalynn's romance flags. Nidalynn protects the child, recognizes the mother's right to be heard, refuses surrender of a frightened child and will stand against collecting another child's life. If the Commander sent Devarra hunting the druids, Nidalynn protects her people and retains her grievance; historical hunting knowledge survives Devarra's later absence, but absence changes present-tense scenes.

Authored facts explicitly distinguished from canon: Nidalynn watching the clutch on Trickster; the cold smallest twelfth egg; twelve-count specifics and leaving it in straw; her Drezen widow persona and chosen human face; girlhood at Reudger's fire and calling him grandfather; his personal bread-and-salt welcome (not Windstep law); old lick-stone and carried salt; lime-kiln, ash-bin, tanners' stair, Old Anka, squinting sergeant, quartermaster/clerk, goat victim and chaplain; all romance, hatching, custody, public backlash and household extensions. Native support for Windstep, Reudger, memory and the salt riddle does not prove these additions (C05/C07–C10).

## Delivery, world reactions and household role

The authored bodies are spawn-copy refugee blueprints (S10–S11); the export places them left 2.5m of JewelerCapitalTrader in Drezen (`2570015799edf594daf2f076f2f975d8`). Widow needs hearth/route-open/current availability and forbids chosen form, closure and departure; chosen body needs form/route-open/current availability and forbids closure/departure. Native unit identity cannot be inferred from the copied body. The older Fye-door placement and source module's older rest-visit prose are superseded by the actual export and `nm1_nidalynn` integration.

Physical courtship visits remain on her widow/chosen hubs and stage their actions in kiln, wall, lane or quarters. Feeding, druids, goat and in-charge scenes each have `.chosen` twins with reciprocal exclusion; all IDs and choices stay stable. Existing remote allocation: chapter 3 device fallback plus hearth (2); chapter 4 kiln letter (1 under coordinator pacing ruling despite older ledger conflict); chapter 5 homecoming (1), with late-entry hearth folded into fallback. Current export homecoming requires `met_before_abyss`, so a chapter-five first meeting is not greeted as reunion. No new delivery or native-host obligation follows from old residual score prose.

Companion reactions use their own native conversation lists and death/dismissal/party guards: Greybor's native destruction stance (C23) informs the hatched-rock reaction; Woljif's sigh (C24) is recorded history but current export retires his extra reaction via `chapter_later` forbid; Ulbrig has white-girl likeness and snowfield aftermath. The likeness never confirms a shared biography; no additional Ulbrig lore is asserted here. The crusade also reacts through soldiers, refugees, chaplain, quartermaster, kitchens, stores costs, public confession and hatchling killing a demon. None is merely decoration beside courtship.

Household role: `fed_at_the_fire`—she feeds and remembers her people, protects hatchling and druids, keeps her own work and claims truthful speech about what the Commander loves. She does not confer blanket advance permission to all partners. `after.first_demon` states her own fire/salt terms, not exclusivity or a sharing bargain. Devarra retains independent dangerous motherhood and debt; Areelu remains the Architect whom Nidalynn may demand account from without absolution. Generated `nidalynn.harem.eligible` reads earned ordinary payoff or late commitment and is guarded by `DerivedOpenRoutes`; a historical commit alone cannot make a closed/lost woman a living guest. The ordinary framework Table slot is not route-specific group romance.

The pair extensions already appended to ending/Last Call pages preserve women acting on their own conflicts: Devarra load/feed/guard-night history; Nidalynn-Areelu Windstep complaint, inspected response, lost field notes and no absolution. Remembered pair costs do not prove both women remain present. Paragraph conditions are authored implementation evidence, not native canon.

## Canon partner position

Native human-role lines claim a husband (C02/C03); the later staged-test disclosure (C12/C14) establishes playacting but does not explicitly establish a real spouse's existence, identity, death or fidelity. Do not classify a native spouse as dead, absent, abusive or fictional by inference alone.

Existing Trickster resolution is explicitly authored: `hearth.listening/how` says “I've never been married” and “I made him up”; reveal choices set `nidalynn.partner_claim.disguise`, as do ordinary salt acceptance and delayed heel acceptance. This settles the claimed husband as part of her disguise within this authored route only. The existing fictional-bond exception supplies no share/exclusive/secret choices and creates no other-man intimate beat. Proposal is “of my fire,” not an invented native dragon marriage law. Late ending assembly also records the same disguise settlement without publishing a native spouse rewrite.

## Current state factors for stage 2

Use assembled export conditions, not prose or source-level flags alone. Factors already present: golem/vault/straw entry; clean/hand/clerk-palms/quartermaster exposure; native clutch destroyed/project/druids/omelet/still-in-chamber; told rock/egg/nothing; why saved; immediate/delayed confession versus kept lie versus crowd destruction; custody relinquished/reconsidered/kept; chosen form; kiss; ordinary salt acceptance/deferred bread/refusal/late commitment; early meeting and homecoming; optional torc/feed/name/spear/druids/goat/wake/chaplain/in-charge histories; current actor/letter reachability/epoch loss; live/current versus ever Trickster; Commander sacrifice and earned return; debt and pair/notice outcomes. This list describes existing dimensions and adds no requirement.

Export-derived ordinary payoff is `(committed + kissed + claim_given_up + hatched + salt_eaten)` OR `(committed + bread_kept + salt_eaten)`; late commitment is `trickster.ever + kissed + outcome.route_open`. Current availability uses observed state, no `left_with_it`, no returned-actor-loss and no epoch unavailability. Closed route and missing actor are distinct facts. Living epilogue siblings forbid sacrifice but preserve their existing Commander-return override; unreturned sacrifice page requires sacrifice, forbids Commander back, closure and Last Call active. Failure/closure endings are distinct existing siblings. Preserve historical debt and complaint paragraphs where no living appearance is asserted; do not add broad current-presence gates to every memory.

## Pinned r4 receipt and narrow remaining work

`/work/Writer/judging/codex/nidalynnr4.json`: CAN94 / VOI93 / TRK93 / INT94 / BEL92 / COX95 / HOW90, no cap. Its only three findings are stale supplemental acceptance counts in `tests/test_nidalynn_partner_claim.py`; they authorize no new story defect, hook, mechanic, price or gate. Stage 3 should plan acceptance repair from the assembled witnesses:

| Existing page | Original prefix | Current assembled count | Appended witnesses |
| --- | --- | --- | --- |
| `nidalynn.trickster.epilogue.salt/page` | 26 | 28 | [26] Devarra pair memory; [27] Areelu complaint/cost memory. |
| `nidalynn.trickster.epilogue.late/page` | 22 | 23 | [22] Devarra pair memory. |
| `nidalynn.lastcall.page/page` | 11 | 16 | [11] refused Devarra historical debt variant + Nidalynn available; [12] Devarra pair memory + Nidalynn available; [13] inspected Areelu response/no absolution + both available; [14] unanswered complaint historical memory with no actor gate; [15] pending notice + Nidalynn available, forbids accounted/unanswered. |

Last Call's five appended rows are not all new household payoffs: index11 is the route's refused-Devarra debt variant. Preserve/verify original prefixes separately, assert appended identities and conditions, isolate idempotence from count failures, and use subtests so salt cannot mask late. This dossier records that plan obligation; it does not edit or run the tests and makes no new pass certification.

## Primary source records

Every path below is an entry in `/wrath/blueprints.zip`; every localization key resolves in `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`. Structural records state explicitly when no key exists.

### C01 — Pregnant human appearance is a performed encounter; clean worn dress and distressed manner.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonStupidQuests/NidalynnQuest1/Cue_0001.jbp`
- Blueprint GUID: `64b38b810f2f83e41a5d70ff90ac0962`
- enGB key: `52ecb05b-3811-4e7d-a048-3cc184f7fc8f` — {n}You see a woman in a clean, but worn dress. She looks like she's about to cry. Her eyes are red and puffy, and the outline of her dress hints at the bulging belly of an expectant mother.{/n} "Yes? What do you want?"

### C02 — In the human role she claims a husband, a strong cheese craving and a grandfather.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonStupidQuests/NidalynnQuest1/Cue_0007.jbp`
- Blueprint GUID: `0c798d1029db65240a983a053ab47565`
- enGB key: `5b382a22-05f4-42e4-93cc-776400269266` — {n}The woman eyes you warily.{/n} "Well... maybe I do. My husband told me to forget it, but I can't! It's a bit embarrassing... but, since you asked... I want cheese so badly, I could scream! But I don't want the normal cheese you can buy on any street corner. I'm craving a special kind of cheese. The cheese my grandfather used to bring me."

### C03 — The husband allegedly refuses help; this starts the cheese objective.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonStupidQuests/NidalynnQuest1/Cue_0008.jbp`
- Blueprint GUID: `f2c61bcd6f4e4534ca46bffcac76e44b`
- enGB key: `d8308688-25b5-41bb-b696-66b313eb071c` — "Oh, thank you! No matter how many times I ask, my husband refuses to help! He's 'busy,' you see!"

### C04 — Her tart refusal fails the cheese objective.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonStupidQuests/NidalynnQuest1/Cue_0009.jbp`
- Blueprint GUID: `e630e82382760b54280f2dbcf084525f`
- enGB key: `87886271-f870-4827-8832-f0b9bb2f0b61` — "Pft! Fine! I don't know why I even wasted my time with you!"

### C05 — Windstep mare-and-stars brand; depleted clan; Reudger the White, cheesemaker.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonStupidQuests/NidalynnQuest1/Cue_0012.jbp`
- Blueprint GUID: `ebae4003fce6aa948b1b63f8aa72478b`
- enGB key: `867fefa5-8573-4991-b8b8-db7a43434a35` — {n}The woman takes the wheel of cheese and sniffs it.{/n} "Yes, that's it... that's the smell... and look at its thick, solid rind. See the brand here? A mare galloping beneath the stars — that's the brand of the Windstep clan. There are hardly any of them left now. Their graves have been lost to time, and their memory forgotten. But at least you have brought me this small remembrance of them. For that, I am so grateful. There were master craftsmen and artisans among them, but they say that the greatest of all was Reudger the White, a cheesemaker."

### C06 — Rejects ordinary cheese and suspected tricks; help properly or leave.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonStupidQuests/NidalynnQuest1/Cue_0013.jbp`
- Blueprint GUID: `c7e26a7e481b3cf428d892cd145048fc`
- enGB key: `e43b37c4-54b8-452f-806b-2bbce9aed865` — "Is this a joke? Are you trying to play a trick on me? Of course this isn't the right one! This is just ordinary cheese! If you want to help, then help. But if not — off with you!"

### C07 — Remembers Reudger smoking his pipe, watching grazing mares; peaceful craft gives joy.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonStupidQuests/NidalynnQuest1/Cue_0017.jbp`
- Blueprint GUID: `913f48fe0dc8c0043993a97791744c8e`
- enGB key: `dca06928-d0bb-4a96-bb7a-81faa505b970` — "He was not a warrior, mage, or priest... yet his fame spread all across Golarion. I remember him sitting there, smoking his pipe, as he watched the mares graze on the emerald grass beneath the endless blue skies. And even in the darkest of lands, anyone who had even the smallest taste of his cheese would feel as if they were there, in the field, on that calm and sunny day. And their soul would find joy in existence."

### C08 — Grandfather/salt riddle; consumes the correct cheese item.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonStupidQuests/NidalynnQuest1/Cue_0018.jbp`
- Blueprint GUID: `1d1fd011f2de8b7459b6aa018ddacbae`
- enGB key: `76e33e29-82ce-4420-b051-09c6b8d08610` — "Don't go just yet, I wanted to ask you something. When my grandfather gave me cheese, he would also ask me a riddle. You need salt to make cheese. It preserves the cheese, but it also gives it flavor. What is Golarion's 'salt'? What allows us to exist here, and makes our lives worth living?"

### C09 — The common folk preserve and give the world value.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonStupidQuests/NidalynnQuest1/Cue_0023.jbp`
- Blueprint GUID: `90cc684e866ab3140b679c5a849bfb06`
- enGB key: `560c0ff9-1d78-4b92-8d88-ae819cdf64fc` — "That is correct. Wars come and go, but farmers have been plowing their fields since time immemorial. Spinners and weavers, cheesemakers and woodcutters, horseherds and blacksmiths — the world as we know it would not exist without the common folk."

### C10 — Shares cheese with Sarkorians in Kenabres to remember lost peaceful Sarkoris; completes objective.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonStupidQuests/NidalynnQuest1/Cue_0024.jbp`
- Blueprint GUID: `0f34a4ab376a768479a84cf2c4c2305b`
- enGB key: `4aab94a3-f53a-44ba-90c5-001608f5359a` — "There's no more Reudger the White, no more fields of green — only a scorched waste. I will share this cheese with the Sarkorians who live here in Kenabres, and together we'll remember what we've lost. Warriors are not the only ones worth remembering. If we forget Sarkoris as it was during times of peace, we will forget what it is we are fighting for now."

### C11 — Actions outweigh words and the imperfect learner can still act well.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonsKenabres/Cue_0009.jbp`
- Blueprint GUID: `6b89e1d45a522434a92ea5fe73f92461`
- enGB key: `ea186e49-81e7-4e9a-a90a-2a0c56e90ad1` — "Not at all! You're just learning! Besides, actions speak louder than words! It's not what you say that matters... it's what you do! Good intentions are a matter of the heart. Sometimes, the noblest sentiments cannot truly be expressed in words. The soul of a dragon will always find the right path. Trust me."

### C12 — Enjoys jokes and games; helped Halaseliax invent absurd requests.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonsKenabres/Cue_0011.jbp`
- Blueprint GUID: `5f41445cf3a1b28449b183da550ab38f`
- enGB key: `96aabb66-2510-40b0-b156-95569be79d5d` — "Different dragons enjoy different things! I enjoy jokes and games, so when Halaseliax asked for my help, how could I refuse? Strange people asking you to bring them unusual things... It sounded so amusing! We had so much fun coming up with silly things to ask!"

### C13 — Silver dragon; kindness and sincerity; nourish the body, savor food, be grateful; rewards completed cheese quest.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonsKenabres/Cue_0015.jbp`
- Blueprint GUID: `115f3b59eade2374196abbc646bb8a54`
- enGB key: `a55811ca-8fd2-4fc6-9538-19d99d4fa48e` — "Your concern seemed sincere, and I'd like to believe that your kindness was genuine. As a silver dragon, I believe kindness and sincerity are of the utmost importance. However, it is not just the soul that needs to be nourished. You must also sustain your body! Here is a slice of Master Reudger's cheese. You should try some the next time you make camp. Just remember to eat it slowly, savor its flavor.... and be grateful!"

### C14 — Reveals the absurd pregnant-woman request as a lesson.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonsKenabres/Cue_0016.jbp`
- Blueprint GUID: `37d0134dd61992741994b6d93c30d46d`
- enGB key: `1d7f505b-4865-4279-8dd4-2af3cbdbec60` — "I knew that an absurd request from a pregnant woman would seem foolish. But she could have taught you a valuable lesson."

### C15 — Dragons may disguise themselves as druids to take the Ivory Sanctum woundwyrm eggs; she thanks the Commander and promises care; project-done condition.

- Archive path: `World/Dialogs/c5/Mythic_Dragon/DragonsKenabres/Cue_0058.jbp`
- Blueprint GUID: `7e1a31d409836274b93e59796d60c19e`
- enGB key: `a3ab444b-87bb-43fa-be5b-6a06f42ac3af` — "Dragons often take human form. Sometimes they do it because they're bored... And sometimes, they do it because it is necessary to achieve some greater purpose. For example, they may disguise themselves as druids, and ask the crusaders to give them the woundwyrm eggs the Commander took from the Ivory Sanctum. Thank you for those, by the way. Rest assured, we'll take good care of them."

### C16 — Raised fists over the clutch lead into the implemented answer-list hook.

- Archive path: `World/Dialogs/c3/IvorySanctum/Golems_DragonEggs/Cue_0006.jbp`
- Blueprint GUID: `24de2c3ecf95fc640a84a5211d90121d`
- enGB key: `3d378884-e537-4382-9127-9224f2ab0575` — {n}In unison, the golems swing their fists above the eggs on the ground.{/n}

### C17 — Native alarm continues to the hostile golem cue.

- Archive path: `World/Dialogs/c3/IvorySanctum/Golems_DragonEggs/Cue_0034.jbp`
- Blueprint GUID: `95bebf5d25d792743a92fe5291b0b3cb`
- enGB key: `34aa0139-4ceb-4ad3-a69a-500d1a79858d` — "We are under attack! Alert! Eradicate!"

### C18 — Native golem hostility; OnStop SwitchFaction includes group.

- Archive path: `World/Dialogs/c3/IvorySanctum/Golems_DragonEggs/Cue_0032.jbp`
- Blueprint GUID: `c32a19cadcf830946b6b7c97ca86e44d`
- enGB key: `4ff5fa4d-3c32-4f19-97d8-4cb60911d123` — {n}Raising their fists, the golems move toward you.{/n}

### C19 — Intruder alarm and threat to destroy eggs on Xanthir Vang orders.

- Archive path: `World/Dialogs/c3/IvorySanctum/Golems_DragonEggs/Cue_0047.jbp`
- Blueprint GUID: `ea54d573de2fd7842b0fe4d9c513a88e`
- enGB key: `9888e0a6-7b87-4773-8107-8d80c27ebdc2` — {n}Stone lips appear on the golem's unmoving face and it loudly says:{/n} "Intruder detected! Hey, dragon, where've you {d|c3 dragon hunted}gone{/d}? You better fly back here and fight as teacher Xanthir the Plau... Ow!" {n}The golem makes a noise like it has just been smacked upside the head.{/n} "As teacher Xanthir Vang ordered! Or else your eggs will be destroyed!"

### C20 — Implemented NativeReturnCue; very large creature laid the eggs.

- Archive path: `World/Dialogs/c3/IvorySanctum/Golems_DragonEggs/Cue_0046.jbp`
- Blueprint GUID: `d39b1e850904daa43b7e6dab3a6e7f83`
- enGB key: `7f66b304-097c-48cc-909f-9bbe59e708df` — {n}Only a very large creature could lay eggs like these.{/n}

### C21 — Shell radiates heat; SeenCues observation anchor.

- Archive path: `World/Dialogs/c3/IvorySanctum/DragonEggs/Cue_0001.jbp`
- Blueprint GUID: `b2bf1f68ffaafd147a464d74dcfc42b1`
- enGB key: `eadb9a3e-2ee7-4592-9ad0-57d1eca398e6` — {n}You can feel the heat radiating out from the thick shell of these large eggs.{/n}

### C22 — Eggs most likely laid by the dragon killed; inference wording in native narrator.

- Archive path: `World/Dialogs/c3/IvorySanctum/DragonEggs/Cue_0007.jbp`
- Blueprint GUID: `164c14743ee768f409a04f93a040e678`
- enGB key: `8e520736-4eaa-4077-aea9-6e4b9a05e854` — {n}You don't need to be an expert in magical creatures to know that these are dragon eggs, most likely laid by the dragon you killed.{/n}

### C23 — Greybor wants the almost-hatched clutch destroyed.

- Archive path: `World/Dialogs/c3/IvorySanctum/DragonEggs/Cue_0016.jbp`
- Blueprint GUID: `99a468ad5f441dd42b16f1a9bc1bf3d3`
- enGB key: `9b302fad-706b-4d46-8cc6-ebe91bff29bd` — {n}After peering at the eggs, Greybor reaches for his weapon.{/n} "That's a clutch of dragon eggs. They're almost ready to hatch — we need to destroy them."

### C24 — Woljif reacts to doomed dragonlings and motherless children; observed cue binds route reaction.

- Archive path: `World/Dialogs/c3/IvorySanctum/DragonEggs/Cue_0018.jbp`
- Blueprint GUID: `d2f3ae3a8d7d0eb4aab722e777b7c260`
- enGB key: `b86a853c-abbd-466b-826b-2dc1257217e7` — {n}Woljif heaves an unexpected sigh.{/n} "So, you were s'posed to be dragons, and your mom tried to protect you, but you can't win against somebody stronger than you. But maybe you're the lucky ones: this world ain't a nice place. Kids without moms don't do so well here."

### C25 — Smashing kills premature dragonlings; OnShow starts destruction etude and cutscene (not OnStop).

- Archive path: `World/Dialogs/c3/IvorySanctum/DragonEggs/Cue_0006.jbp`
- Blueprint GUID: `757a3b2e19b4f8f4d8d438ba15db1d76`
- enGB key: `53722c62-b4a5-422e-bbc4-3f8c2de2b051` — {n}The shell doesn't give way immediately, but it finally cracks open. A flaming, gooey substance spills out onto the floor, and tiny lizards are wriggling about in it — blind, premature dragonlings. They twitch convulsively in the puddle and soon die.{/n}

### C26 — Soldiers bring clutch to Drezen after Ivory Sanctum demons; OnStop starts project gained.

- Archive path: `World/Dialogs/c3/IvorySanctum/DragonEggs/Cue_0022.jbp`
- Blueprint GUID: `e2918442c371a8c4b871ad52a3ce193c`
- enGB key: `b4456a56-5d52-4755-848e-254b255cf1ac` — {n}The soldiers will bring the eggs to Drezen as soon as you deal with the demons in the Ivory Sanctum. There are sure to be ways to use the dragon eggs for the good of the crusade.{/n}

### C27 — Native druid decree description and completed outcome.

- Archive path: `Kingdom/CrusadeProjects/KTCProjects/Eggs_DragonsInEducation.jbp`
- Blueprint GUID: `4aa538f07bd542f7a013b90464577d67`
- enGB key: `919f3cbe-f0aa-4aa0-a7e1-f0a3e58745c9` — Dragons in Care
- enGB key: `fc8bb151-8b30-4987-80d8-c6bed5cf2802` — There is an interesting trophy among the quarry that the Commander captured in the Ivory Sanctum: a clutch of woundwyrm eggs. It is common knowledge that such dragons, as a rule, are malicious by their nature, so nobody wants to hang around for the evil critters to be born. A group of druids is ready to relieve the crusaders of this perilous treasure and take the eggs into their care. In answer to the question on whether the druids would condition the young dragons to be kind creatures that shun violence and do not eat mortals alive, a druid evasively replied that he and his companions "should not get in the way of nature".
- enGB key: `5755378a-7e7e-4d20-af20-174196bb4844` — The woundwyrm eggs have been given to the druids.
- enGB key: `1a190998-7a6e-410c-add7-4c41b5c034a9` — All dragon units gain the {g|DruidicUpbringing}[Druidic Upbringing]{/g} feat.

### C28 — Native cooks outcome: clutch feeds Drezen; morale reward.

- Archive path: `Kingdom/CrusadeProjects/KTCProjects/Eggs_UnprecedentedOmelet.jbp`
- Blueprint GUID: `88f12bba35004a648023938699769380`
- enGB key: `eb36e15d-fa66-4379-8f65-a2364b018355` — Omelet Innovation
- enGB key: `9e5faf38-0489-4ceb-a853-bae4f29d4b7f` — There is an interesting trophy among the quarry that the Commander captured in the Ivory Sanctum: a clutch of woundwyrm eggs. It is common knowledge that such dragons, as a rule, are malicious by their nature, so nobody wants to hang around for the evil critters to be born. Citadel's cook has offered to make a giant omelet such as never been tasted before. A feast for all Drezen will certainly lift the morale of the crusaders.
- enGB key: `6ce43d04-d944-4b07-a3b8-62f413e0434d` — The woundwyrm egg omelet was enough to feed the whole of Drezen.
- enGB key: `5a412649-9cb9-45fd-a89d-921fd9c5683c` — Crusade morale increases by 20.

### C29 — Portal carries supplies, not reinforcements; route letter carrier observation.

- Archive path: `World/Dialogs/NPC_Common/StoryTeller_MainDialogue/Cue_0629.jbp`
- Blueprint GUID: `459bf324a71c81c4ba5f3eead9ba42bb`
- enGB key: `19609f8b-41ed-4481-aae0-30efde98de39` — "I suspect it's difficult for you to carry out your mission surrounded by enemies. I would like to help. Unfortunately, I will not be able to bring your allies or reinforcements through this portal. Supplies, however... When I return to Golarion, I will buy some travel necessities. If you need anything, just ring this bell, and I will deliver them to you."

### C30 — Native cheese objective; chapter-five DragonAwakening quest reference.

- Archive path: `World/Quests/MythicQuests/Dragon/C5DragonAwakening/Add1_FindCheese.jbp`
- Blueprint GUID: `b35eecc85a801324a8df62f99b86aad9`
- enGB key: `e32cb6fd-b02b-4a64-899a-9c924d0b3ae2` — A lady in distress is desperately craving old Sarkorian cheese. Some of the delicacy may yet be found, but only in the deepest cellars of Drezen's taverns

### C31 — Native DragonAwakening quest ends in chapter five.

- Archive path: `World/Quests/MythicQuests/Dragon/C5DragonAwakening/DragonAwakening_quest.jbp`
- Blueprint GUID: `084960ae22f408e4282f537a8a9debc1`
- enGB key: `bd078582-ecff-40cc-94a9-e31952e5f100` — It may be stated with utmost certainty that events such as this have never been recorded in history — one cannot become a dragon, one can only be born a dragon. And yet Halaseliax is convinced, with the confidence typical of gold dragons, that one can be taught to follow the dragon's path. And he is willing to teach the new dragon as he once taught Terendelev.
- enGB key: `7433ce9d-868b-4852-b904-d81ee95ee5d0` — Dragon's Awakening
- enGB key: `c08eca73-37c9-4ea4-b33c-2cbd8224e9b9` — A most curious experiment has entered a new phase — a creature with a warm-blooded body and a dragon's spirit has completed its training. Let's see what this hybrid is capable of. It is interesting that the metallic dragons have accepted the new gold dragon into their fold without question. The bestowal of such an honor is most telling.

### C32 — Historical F14 inspiration: reveal impossible item properties; no such feature gate in current theft implementation.

- Archive path: `Mythic/Trickster/KnowledgeArcana/TricksterKnowledgeArcanaTier3Feature.jbp`
- Blueprint GUID: `5e26c673173e423881e318d2f0ae84f0`
- enGB key: `19bed909-a5d4-4e87-ba58-68a7a5a07793` — Knowledge (Arcana) 3 Rank
- enGB key: `08c5494d-9441-45a1-a757-cae129446016` — You can reveal item properties that aren't even there and couldn't possibly be there. Every item you identify gets an additional random major effect.

### C33 — Nidalynn names herself a silver dragon and swears loyalty to the Gold Dragon Commander.

- Archive path: `World/Cutscenes/Kenabres_Rebuilded/DragonLevelUpScene/CommandBark 2.jbp`
- Blueprint GUID: `1e2694b97e381b04da49af6196943b6a`
- enGB key: `6a4beb10-0dd0-4aa2-be36-1ca7a91e1528` — "I, Nidalynn, a silver dragon, swear loyalty to you, gold dragon {name}! I will fight by your side and protect you!"

### C34 — Golems address the dead colossal dragon and threaten “your eggs”; attribution is combined with C22/C35.

- Archive path: `World/Dialogs/c3/IvorySanctum/Golems_DragonEggs/Cue_0001.jbp`
- Blueprint GUID: `b8dfb42d03fc931409f2b80614cfa9de`
- enGB key: `5d98549e-86c8-4288-9668-fff7303944f5` — {n}Empty eyes stare blankly out of the metal face at the body of the colossal reptile. Magical lips appear on the golem's unmoving face and it loudly says,{/n} "Get up, lizard! No order to lie down was issued! Get up and fight as teacher Xanthir the Plagued One ord... Ah!" {n}The golem makes a sound like it was just hit in the stomach.{/n} "As Teacher Xanthir Vang ordered! Or else your eggs will be destroyed!" {n}The construct clearly does not understand that the dragon is dead — the golem is merely following its previously set protocol.{/n}

### C35 — The native Ivory Sanctum dragon is named Devarra.

- Archive path: `Units/Monsters/RedDragon/IvorySanctum/RedDragon_Sanctum.jbp`
- Blueprint GUID: `b01da68dab56e004f952d7ad0e83cc46`
- enGB key: `65fd9d09-3398-483c-bbc6-9bc7abb75358` — Devarra

- **S01**: `Units/NPC/Unique/Act_5_HeraldOfTheIvoryLabyrinth/MythicDragon_Ch5/NidalynnDragon.jbp`; GUID `c966ef14763c5e649beab50af6e22972`. Data Gender=Female, Alignment=LawfulGood, Size=Huge; named silver dragon voice is C13/C33; name key `6967b617-ed54-4df7-8640-36d6635ca9c0` (“Nidalynn”). enGB: no localized text key for these structural conditions/actions.
- **S02**: `Units/Monsters/GoldDragon/HalaseliaxBrain/Nidalynn_PolymorphBuff.jbp`; GUID `885ee6e3ecd2409bbda4f6ecfe914c6d`. Native polymorph buff; do not infer Trickster placement or marriage. enGB: no localized text key for these structural conditions/actions.
- **S03**: `World/Encounters/Kenabres_Rebuilded/ActionsHolders/Woman [Nidalynn]_Actions.jbp`; GUID `e954f5a4914f8244b9e7540715eb4fa5`. StartDialog on SpawnedUnit, quest-requests objective started; switches to dragon-form bark after relevant completion. enGB: no localized text key for these structural conditions/actions.
- **S04**: `World/Etudes/Common/WrathOfTheRighteous/MythicDragon/DragonCh5.jbp`; GUID `34af00526ace70a42bf6f180a2d40265`. Chapter05 playing condition; DragonC5Quests parent. enGB: no localized text key for these structural conditions/actions.
- **S05**: `World/Etudes/Common/WrathOfTheRighteous/MythicDragon/PlayerIsDragon/DragonC5Quests.jbp`; GUID `6beabee4770ae7743aa0a1464e6e1ce6`. Parent DragonCh5; native chapter-five dragon requests. enGB: no localized text key for these structural conditions/actions.
- **S06**: `World/Dialogs/c3/IvorySanctum/Golems_DragonEggs/AnswersList_0002.jbp`; GUID `dd8ac86f25e0f6b4cac75386eb528851`. Current inline answer-list hook; native C16 points here. enGB: no localized text key for these structural conditions/actions.
- **S07**: `World/Etudes/Common/WrathOfTheRighteous/Chapter03_Extra/IvorySanctum/DragonEggsDestroyed.jbp`; GUID `b0c1344ae8267c94998ca27ad4288c01`. Native destroyed outcome, produced by C25 OnShow. enGB: no localized text key for these structural conditions/actions.
- **S08**: `World/Etudes/Common/WrathOfTheRighteous/Chapter03_Extra/IvorySanctum/DragonEggsProjectGained.jbp`; GUID `02ea801d75381dd48ae15c6c93c5f1dc`. Native clutch transport/decrees available, produced by C26 OnStop. enGB: no localized text key for these structural conditions/actions.
- **S09**: `World/Etudes/Common/ImportantStates/StoryProjectsOutcome/DragonsInEducationFinished.jbp`; GUID `e4374a1783c74f68ae46bb5db22e0c58`. Native druid outcome used by eggs.druids. enGB: no localized text key for these structural conditions/actions.
- **S10**: `Units/NPC/Commoners/Act_1_WorldwoundIncursion/DefendersHeart/Refugees/Commoner_Noble_Female_Refugee2.jbp`; GUID `e24a8cb4f83960748b5bead99d58a36e`; enGB name key `a189ab0e-b619-4e1c-8f0f-1fd64ff0b6bf` (“Noble Survivor”). This is an existing generic copied unit, not native Nidalynn.
- **S11**: `Units/NPC/Commoners/Act_1_WorldwoundIncursion/DefendersHeart/Refugees/Commoner_Noble_Female_Refugee1.jbp`; GUID `3191b154bbed71b4595a5154ad067e90`; enGB name key `a189ab0e-b619-4e1c-8f0f-1fd64ff0b6bf` (“Noble Survivor”). This is an existing generic copied unit, not native Nidalynn.

- **S12**: `World/Etudes/Common/ImportantStates/StoryProjectsOutcome/UnprecedentedOmeletFinished.jbp`; GUID `a9a453f695924f99b4326f60b7c3753e`. Native `eggs.omelet` outcome; no localized text key on this structural record (localized decree C28).

- **S17**: `Units/NPC/Unique/Act_3_DemonsHerecy/Drezen/JewelerCapitalTrader.jbp`; GUID `bc1093231b1577a4485a730c29595195`. Authored presence existing jeweller anchor. enGB name key `1dca7e97-fb8e-4b0f-b611-41eb0f8d04bc` (“Jewelry Trader”).
- **S16**: `World/Areas/Act_3_DemonsHerecy/DrezenCapital/DrezenCapital.jbp`; GUID `2570015799edf594daf2f076f2f975d8`. Authored presence existing area. enGB: no localized text key for this structural hook.
- **S13**: `World/Dialogs/Companions/CompanionDialogues/Grimbor/AnswersList_0002.jbp`; GUID `174d6c94b6725f44aad1d2a76993a926`. Greybor reactor native answer list. enGB: no localized text key for this structural hook.
- **S15**: `World/Dialogs/Companions/CompanionDialogues/Woljif/AnswersList_0003.jbp`; GUID `e41585da330233143b34ef64d7d62d69`. Woljif reactor native answer list. enGB: no localized text key for this structural hook.
- **S14**: `World/Dialogs/DLC4_Shifter/Shifter_CompanionDialogue/AnswersList_0001.jbp`; GUID `0a50c9c878844ed4a69b8d6131304c5e`. Ulbrig reactor native answer list. enGB: no localized text key for this structural hook.

## Inspection receipt

- `storylines/nidalynn_trickster.py` SHA-256 `6b2beacb48b0b61ea0355343aeb50298e0a151754dd65c6e4e97a20e88507b01`.
- `storylines/nidalynn_kiln.py` SHA-256 `c754ada5086e1b3635dc34eaa8b76e2a4470023866a6c6fefa85558b5270e686`.
- `storylines/nidalynn_salt.py` SHA-256 `a81f95f3fe1f5d14661c4a05548d3e6dbce6aa57d458536ec4c217ed98d11360`.
- `storylines/nm1_nidalynn.py` SHA-256 `ad22e17dc625f2dac681aacaef5524ed8ff9a1d7bddf203808420242b8915d22`.
- `development/Story.json` SHA-256 `e04caad4da04cd0d29140e64a1360bccb5e9e6316aafdd7d79668f80e40b4fa7`.

Only this dossier is written by stage 1. Canon records are evidence; authored extension labels are preserved; no proposed redesign or additional acceptance obligation is smuggled in through historical scorecards.

## Revision 2 planning clarification (PA-01 / PA-02)

The independent [plan audit](plan-audit.md) verified the canon citations and character truth above. Its corrections concern existing shared custody history, not new story work. On both widow/chosen bodies, the first Athletics18 spill records `custody.failed` and `cost.commander_feed_spilled`; refusal records `custody.refused` and `guardian_kept`. Neither flag is cleared by the existing 48h replacement opportunity. Successful replacement delivery costs **150 Materials**, records `repair.seen`, `resolved`, `feed_delivered`, guardian retention, her guard-night/own-feed costs and the Commander's luxury/delivery costs. Original failure/refusal remains historical; successful resolution earns the guarded-load memory under the containing page's guards. A declined, abandoned or unaffordable replacement earns no delivery memory. Direct checked success and hired direct delivery (**100 Materials**) remain separate roads. These Materials prices are unrelated to delayed public confession (**150 Favors**).

Supported generic copied bodies are an integration choice, not an inherent INT defect; live campaign placement remains pending evidence. Authored biography/rite is judged for its fit and scale under BEL, not deducted from CAN merely for being authored. Recurring feeding/ending motifs and bounded women-to-women density remain candid quality limits. Stage 4 acceptance repair is ordinary pending work, not a projected post-implementation HOW loss. Preserve all verified citations, tart lawful-good action, appetite/refusal, villain menace/purpose, binding contexts, echo discipline and native rewrite boundaries.

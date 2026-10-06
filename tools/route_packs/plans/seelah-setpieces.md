# Seelah — round-2 set-piece sheet

Planning only, 2026-10-06. All proposed romance, staging, rooms, dialogue and slot continuations below are **authored additions**, not recovered native romance. No runtime source, registry, exported Story, mechanics or gates are changed. Existing choices, costs, chapter access and quiet/changed-body roads remain intact. This sheet supersedes the earlier sheet's conservative heat recommendation, not its earned-outcome discipline.

## Evidence and reservation

Read: POLISH-AGENT-PROMPT steps 1–3; 00-WRITING-GUIDE; the complete ROUND2-TURNING-POINTS revisions; CANON-PARTNERS-DESIGN; TRICKSTER-RUBRIC including Binding (1)–(5), echoes and DLC rewrites; Seelah's trickster spec; the atlas's Seelah reservation and applicable clusters; TRIAGE's SEE-01–04 and global adoptions. Read the nine `storylines/seelah*.py` modules, the Seelah/Wenduag data sheet, and Seelah's exported scenes, paragraphs and Last Call entries. Source is authoritative for implementation; the export supplies exact review addresses and quotes. The spec's closing implementation notes describe repairs absent from this checkout: they are not proof those repairs shipped here.

`origin/claude/tp-seelah` has no `tools/route_packs/plans/seelah-tp.md`. Read the atlas's documented fallback, commit `4ed0617eaee4a5ba4f4bb5667bcf12814d8d5166`, by `git show`, without fetching or integrating it. Its bespoke reclamation classification is superseded by the later atlas reservation:

- **Device:** `act_before_confession`.
- **Setting:** Drezen companion-hub penance-list reckoning and borrowed room; existing Fye stairs for outside-party courtship; Ch3/5.
- **Payoff:** her reclaimed penance list stays private or enters her chosen pocket game; earlier closeness becomes a chosen future, then boots for her own posting.
- **Ordinary history:** `door` closeness before `road`'s future answer. Quiet and changed-body closeness also qualify; sex is not required.
- **Returned outside-party history:** `after.courtship`'s alley kiss before `dismissed.commit`. Only kept-list histories owe reclamation. Returned papers, a company notice and resurrection earn no affection.

Avoid `class-price-test-night-morning` (Galfrey, Terendelev, Yaniel, Horzalah, Gesmerha, Eliandra): no new price, physical test, universal attendance oath or obligatory dawn commitment. Avoid atlas-0017's Seelah/Irabeth head-shake gesture at `souls/survived`: give Seelah a clenched table edge and an unfinished exhalation rather than the stock correction. No forged records or false proof: the stolen papers are her actual papers. Drinking is a build-up incident, not a replacement registered hinge. The belt flourish belongs to Seelah's existing theft play; never borrow Kiana's mid-act husband interruption, Galfrey's regiment night or another woman's relic-token claim.

### Direct native citations

Verified locally against `/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`; GUID is the blueprint AssetId and key is its resolved Text.m_Key. These support character/event facts, not a claim the player heard every cue.

| Ref | Blueprint path · GUID · localization key | Supported fact / implementation hook |
|---|---|---|
| C1 | `World/Dialogs/Companions/CompanionDialogues/Seelah/Cue_0018.jbp` · `50c68a552d32d3741af44e0fd18ac652` · `2a34986a-d8d2-415d-a2a7-2663c2f94da8` | She stole Acemi's mithral helm; Acemi died from a gnoll's blow to her unprotected head at Solku. Her competence and guilt coexist. |
| C2 | `World/Dialogs/Companions/CompanionQuests/Seelah/Q1_LittleTroubles/Ch1_SeelahMeetsFriends/Cue_0006.jbp` · `a3d0b31d35fc785418c78ded53cb278d` · `b9c43cae-d4c0-48f1-a042-6e928e300ca5` | She persuaded Irabeth to permit the cart celebration; beer, food and friends give Kenabres's defenders respite. |
| C3 | same dialog, `Cue_0038.jbp` · `6428870ef6820f040b09f6403c2c7e76` · `52169bb4-9088-4946-a6c2-2c9276c94363`; `Cue_0060.jbp` · `75a5a2c0ae504ad42848173400869c00` · `4f05ee50-def5-4055-8f52-9545b67e705d` | Jannah joined four days before the attack; she and Seelah went around taverns together. Supports an authored bad drinking night, not a native missed appointment. |
| C4 | same dialog, `Cue_0040.jbp` · `9fae9b71dd635124ba54593cdb636915` · `50f03aac-259f-4ec8-8cdf-7bf3a722ffe3`; `Cue_0024.jbp` · `8cdd844bf95073444835e83450defcf2` · `2ddbdc96-a441-48af-b3b5-8169da41c1af` | Elan calls Seelah his noble sister; his beloved is Kiana, whose proposal ring he commissioned. No Seelah/Elan partnership. |
| C5 | `World/Dialogs/Companions/CompanionDialogues/Seelah/Cue_0094.jbp` · `f4a62f6d32724c84bbb706a9a8c048e2` · `cdbd8d33-0989-49c1-a32b-d1ad279799ac` | Her loneliness concerns the old celebration and lost trust, especially Elan's. Romance cannot substitute for repairing her friendships. |
| C6 | `World/Dialogs/c3/AreeluLaboratory/SecretWish/SeelahWish/Cue_0005.jbp` · `dc1a2f2a9d2409d44aa803ad2604d0b1` · `18b09f85-857c-4d7d-9796-800891801e98` | She rejects the laboratory illusion of a life with Acemi alive. Never use it as foresight, a real return or knowledge of another life. |
| C7 | `World/Dialogs/Companions/CompanionDialogues/Seelah/Cue_0121.jbp` · `234b7720015c4c848ab71a8f7f2ce9d1` · `b570de68-9314-461b-8673-c2ffcf8d2cf1` | Abyssal stench, insomnia and imagined torture cries; a watch is credible, instant romantic healing is not. Existing Ch4 hub `AnswersList_0118` · `73260c45aa315c0419fc625f6fcb957d`, answer `829801b14a4b2b344a60ba43cb60821a` supports `abyss.night`. |
| C8 | `World/Dialogs/Companions/CompanionQuests/Seelah/Q3_WeightOfMySword/ElandKianaAftermath/Cue_0006.jbp` · `a819e8c85ef23324bb0d8117bb9d7df3` · `1aef0e95-dc1e-49fa-9852-3fba13bd5e20`; `Cue_0007.jbp` · `df45181e1968f26459f9e8bc2b995a34` · `0c8edca3-4bab-4535-a37b-ea3d3186213b` | Kiana is married to Elan and complains frankly about the lost wedding night. Adult register exists alongside paladin company; no reason to turn Seelah into an embarrassed chaperone. |
| C9 | `World/Dialogs/Companions/CompanionDialogues/Seelah/AnswersList_0003.jbp` · `417fa384f3250634bb71859fbc913453` | Existing companion hub for ordinary courtship/reclamation; return to its existing list. |
| C10 | same directory, `AnswersList_0046.jbp` · `64cfedbb85f36a44cb45f568f18152f7` → answer `d62381d8574c3cf439e17046b9a779dd` → `Cue_0050.jbp` · `6b81c330ca8b1324186cb02bdc8d9c54` · key `b31f8728-33ac-455e-b848-207ff83091c9` | Native dismissal goodbye unrecruits her. Preserve its return and actions, not an automatic immediate romantic reunion. |
| C11 | `World/Dialogs/DLC6_ADanceOfMasks/DLC6_TavernRebuilded/Tavern_Night_Debate/Cue_0001.jbp` · `9e410aaca5ac4542a5790d3fa5f48c04` · `f5602a27-75ef-4550-a85d-1ca5984cc71c` | Penta's pre-judgment resurrection limit supports the existing urgent rite. It is lore evidence, not knowledge attributed to Seelah before DLC6. |

Existing authored hooks: `seelah.boots/wager/promise/kept/door/morning/weight/road` use C9. `early.drill` uses native party list `f1e7b7a6740caaa44a3762033c5f0a5a`; ordinary early access remains chapter-dependent. Outside-party conversations use existing Seelah presence and Fye (`0f12118177d102f428a3b30b15b132eb`), not a newly invented NPC or contact. Preserve the current 24h ordinary progression, 48h commitment/papers beats, 96h reply and subsequent 48h travel, and existing return costs/DCs; no new timing requirement is proposed.

## Six situation-level set pieces

### SP1 — The cart's survivors have an evening (entry, Ch1)

**Where/who/risk:** Defender's Heart during the native League party: Seelah, Commander, Jannah, Curl and Elan, all actually present in that scene. Kenabres is under attack; unglorified rescuers have brought something worth drinking. Seelah risks offending Elan's solemnity, not her paladin powers by enjoying herself. Native C2–4; authored entry uses `boots`, `wager` and the already written `early.drill` without changing access.

**Build-up/beat sequence:** Keep the rescued cart as the reason for celebrating (SEE-01 ADOPT). Curl protects the mugs while she demonstrates the street feint; Jannah heckles; Elan can disapprove of the racket while accepting the defenders' need for food. Seelah makes room, notices the Commander looking at her instead of her sword, and turns the button wager into a dance or walk. Let the dance show weight, sweat and her hand firm at the back; avoid three successive furniture accidents that make a competent fighter coy. The walk's interruptions are people she knows through fighting and rescue, not a new errands plot.

**Her decision/options:** She owns having wanted the evening before the wager began. The Commander may flirt directly, play along, dance, walk, or keep the slower existing courtship response. Her counter-move is admitting the game was an excuse, rather than letting the Commander claim to have won her. No drinking contest, check or attraction threshold. Existing nonromantic early drill outcomes remain nonromantic.

**Payoff/carry:** Mutual appetite begins before any future oath; the buttons recall an actual played event. Friends remain people with their own work. No arrival, romance or household state comes from rescuing a barrel or winning a feint. Coda can recall her initiative only in histories that had it; no fixed extra rest.

### SP2 — The bad cup and the promise kept (build-up, Ch1–3/5)

**Where/who/risk:** The Ch1 drinking incident belongs at the Heart, while Jannah is there; later `promise/kept` belong at the existing campaign camp/hub. Kenabres's defenders need help; in later chapters the army has people waiting on Seelah. The early morning has Seelah, Commander and Jannah; later supper has only the lovers and the existing recruit. Jannah must never be teleported to a Ch3/5 hub because `promise` spans those chapters.

**Build-up/beat sequence:** SEE-03 ADOPT, adapted to the reservation: one night she has one cup too many and misses the help she promised Jannah. No sexual slot and no touching an incapacitated woman. The following morning she has a foul mouth, a pounding head and a friend waiting; she gets up herself. Give the Commander the requested cover/repair-together/leave-it responses as append-only answers in the early incident when eventually implemented. Cover means a good-intention excuse, not forged duty records; her counter-move is telling Jannah herself why she was late. Repair means helping with the actual missed work; leave means Seelah still goes to face her friend. These are not romance points, addiction diagnoses or a new penance gate. Fold this single authored incident into the early party/bench material; do not clone it into every chapter.

Later, `promise` confronts the established recruit-versus-date conflict. Preserve delegation, helping together and rescheduling, including `kept` as the repayment of that particular appointment. Let dirt on her clean shirt and the two of them finally alone produce impatient kissing, not pastry jokes continuing until desire evaporates. SEE-02's belt boast is reserved for SP3/SP5's already existing intimate motion; it is not performed sexually during the bad drinking night.

**Her decision/options:** She takes responsibility for her missed help without allowing the Commander to announce that she is cured or forgiven. At supper she wants the kiss; the Commander kisses, asks about tomorrow or waits. Her slower answer is disappointed but warm, not a consolation lecture.

**Payoff/carry:** The missed help changes her conduct in the scene and Jannah's answer there, without a new relationship score. Kept supper demonstrates a specific repaired promise. Future scenes may recall the actual incident, never claim a universal string of missed dates. No effect on partner/household entitlement. Morning consequences remain separate from the later sexual mornings.

### SP3 — She has borrowed a room, not sworn a lifetime (primary intimate turn, Ch3/5)

**Where/who/risk:** `seelah.door`, Drezen's existing borrowed room, Commander and Seelah alone; army obligations wait outside. Prior `courting`, the invitation and actual open-terms answer lead here. Her risk is wanting someone who may make a false promise, not divine punishment for sex. C1/C2/C9 ground her bluntness, appetite and moral line.

**Beat sequence:** Shorten the furnishing tour. She has spent the day wanting the Commander and admits it badly, then closes the door well. Keep her existing question about a promise to another lover exactly as a consequential character concern; it is not a new partner-stance system. If that promise must be settled, she opens the door and keeps her invitation alive. If the Commander answers honestly, she stops trying to produce an elegant speech, undoes her own sword belt and pulls the Commander close. Preserve the strong undressing and physical initiative; do not promote freckles or scars in authored source to canon facts. Insert `seelah.door.explicit.1` at the current mounting/bed transition, before the lamp/sleep aftermath. Default slot text must carry a heated cut on its own.

**Her decision/options:** Existing night, kisses-to-quiet, quiet evening and changed-body answers all remain. She is the person who wants the night and acts on it. The Commander's postponement still exits; a changed body gets her curious, practical desire without assumptions about anatomy. The explicit slot occurs only in the existing night branch; no new flag or check makes it a road to commitment. This is closeness before the later `road` future answer, not an automatic future answer.

**Payoff/aftermath:** The existing `private_night` records the night; `quiet_closeness`/`changed_closeness` record their own experiences. At `morning`, show the lovers remembering the room in touch, teasing and her wanting another night **only** when `private_night` is true. She has already gone out to help somebody: retain that independent action, but stop making the entire aftermath an instructional bread encounter. Keep the current morning's choices and effects. Quiet and changed-body mornings never imply sex took place.

**Carry:** Other lovers are neither expelled nor silently betrayed. Her honest-word concern survives into the roof and future discussion. No list grievance in ordinary histories. An existing returned history with outstanding custody must receive the sheet's already identified collection repair before renewed intimacy, never a fresh universal price.

### SP4 — Wanting her does not make the Abyss bearable (Ch4; reckoning Ch5)

**Where/who/risk:** Existing Nexus watch `watch`, in-person `abyss.night` and later `souls/inheritors_corner`. Seelah and Commander; no cameo by an absent Drezen friend. The Abyss buys people and exhausts her anger. Ch5's rescued souls and real losses test whether she can endure her own mistakes. C5–8; retain actual quest/death outcomes.

**Beat sequence:** Keep the chained man and her calculation of exits. Her counter-move against a comforting dismissal is naming the bastard holding the chains, then choosing a useful watch instead of a suicidal charge. A tired lover may press against the Commander during the pause; no sex while she is confused by torture cries, no miraculous cure by an embrace. Quiet company here should feel chosen and physical, not a counseling session. Existing drill/watch alternatives retain their independent, path-neutral purpose.

In Ch5, adapt SEE-04 into the already existing `weight/souls/road` reckoning. Seelah challenges cruel treatment of Elan when the run actually did it; if he died she speaks of her friend without inventing his current answers; if he lives, do not ventriloquize him or make him a jealous lover. She can object to the Commander and still want them; an unresolved serious cruelty branch keeps its existing correction/parting consequences. Jannah's native fate is read, not overwritten by her morning cameo in SP2. Replace `souls/survived`'s shared head-shake formula with Seelah bracing on the table while deciding to ask living friends how they are.

**Her decision/options/payoff:** The Commander listens, shares the watch or uses the existing drill; later they hear her criticism, correct the named conduct or take the existing separation. She chooses her faith, friends and rescue work herself. No added exclusivity demand, moral exam or compulsory quest completion. The payoff is lovers disagreeing through an ugly campaign, then returning to a chosen evening; grief/doubt/unfinished rescue still produce distinct roads and endings. No explicit slot in these watch/grief nodes: their physical heat is a hand on a thigh or shoulder, a wanted kiss where already offered, followed by actual work.

### SP5 — Her list, her papers, her answer (registered future turn, Ch3/5)

**Where/who/risk:** Ordinary companion hub `road`; conditional retained-return list reckoning at C9; outside-party `after.stay_or_go`, `after.courtship`, `dismissed.commit/second_ask` at existing Fye/market/room. Seelah chooses her future under campaign pressure. In death histories the Kenabres dead and chaplain's money have paid a real price; in dismissal histories her property and ability to enlist were interfered with. Irabeth/Sosiel reactions occur only through their existing present conversations, never as an offstage magic witness.

**What led here:** SP3 closeness precedes ordinary `road`. On a dismissal/raise detour, the existing paid return and traveled arrival precede company notices; the alley kiss precedes commitment, and is already hot enough to keep. Existing DC15/25 seller/lift outcomes, caught-lift concealment/arrest/purchase, Diamond/100 Favors funding and their native consequences stay. This sheet creates no new return device and no romance payment.

**Beat sequence/counter-moves:** Papers return without bargaining for a kiss; she chooses the posting herself. Only when her list was retained, she reclaims it competently or receives it back, and decides whether to keep its custody private or turn future lifts into **her** pocket game. Reclamation is the old grievance collected, not a physical seduction test. Retained-return ordinary courtship and outside-party custody siblings need the same history-true handling. If she stated 'first coin myself,' show the first restitution she actually pays before repeating that ask; elapsed time alone cannot erase it. If her refusal demanded leaving freely and returning, dramatize that particular return, not a generic paid-coin solution for every refusal.

Ordinary `road` keeps full-life and short-future answers and its existing earned outings/review branches. She has already wanted the Commander; now she says what a future with her means. Outside-party `commit` keeps near/far company and friend options. SEE-02 ADOPT: at the already chosen night she takes the belt herself as a delighted boast, then pulls the Commander into the room. A soldier's morning knock calls **her** to duty, after the night; it is an authored anonymous unit messenger, not a canon partner discovering adultery. No paid leave or new muster mechanic. Four existing threshold siblings receive their own slot IDs/briefs, with location-specific text and the same near/far continuation.

**Her answer/Commander options:** Existing kiss, let-her-choose, friend, give-her-the-door and refusal paths remain; returning property must also leave a selectable neutral postponement/refusal on the existing `list_back` pages (append only). She can say no without the Commander withholding it again. Her future yes is on page and independent of the property's recovery. She chooses near or far work; romance cannot rewrite 'I am leaving' into daily residence.

**Payoff/carry:** Exact atlas payoff: penance list private or voluntarily playful; earlier closeness becomes a future she chooses, then she puts on boots for her own posting. Near morning she is hungry for another hour but has a real muster; far morning she wants another night and still takes the noon road. The Commander can keep seeing her without a lifetime road; friends/company-only stay nonromantic. No new cohabitation rule. Endings/household/Last Call must read the present earned romantic and life state, not infer commitment from company placement or an old rescue. Shared repairs are escalated, not written here.

### SP6 — Returning is part of the love (payoff/aftermath, Ch5–6 and postwar)

**Where/who/risk:** Existing `roof_evening`, race/cooper room `late_afterglow`, `ordinary/farewell`, ending exits, late-return epilogue and Last Call coda. Commander and Seelah; existing workshop/yard people have their own work, not a standing bedroom audience. The Worldwound remains to close; after the war Seelah's posting, restitution, friends and unresolved grief still take her away.

**Build-up/beat sequence:** Roof is wanted kissing, not another sexual first reward or token claim. Keep her invitation and slow alternative, drop generic forehead-resting as the repeated climax. The cooper night is a return/deepening, however late it occurs in progression; she has enjoyed the actual race, makes a blunt offer and pulls the Commander against her. Preserve win/loss songs and quiet/kisses alternatives without extending the municipal athletics subplot. Insert `seelah.late_afterglow.explicit.1` before its embedded morning. Split the dawn material into an appended bridge back to the unchanged `morning` node/legacy exit and preserve `late_night_kept` placement. The morning has her wanting to stay, the cooper hammering and her returning the Commander's things before work. Rough play is visibly reciprocal and ordinary soldier exuberance, not submission to rank, coercion or a humiliation ritual.

Late postwar `epilogue.commit` is either a genuine delayed first night in that history or an already intimate pair renewing their chosen relationship; name which using existing night evidence. It must not grant romance to a mere relief-company decision. Keep the impatient initiating kiss and boot-search aftermath, insert `seelah.trickster.epilogue.commit.explicit.1` before the morning. This narrator slot uses third person/past tense, unlike in-person slots. A playable dialogue adaptation requires coordinator handling of epilogue structure; this plan does not add conditional paragraphs to ordinary pages.

**Her decision/options:** Her offered hand, kiss and invitation remain hers. Commander chooses night, kisses, quiet, later, full/short future or the already existing parting answer; no new mandatory intimate act. Before Threshold she says she loves the Commander and picks up her shield. After a living return she comes back from her own work and kisses them before unloading her complaints. Her counter-move to a promise of endless availability is continuing her posting and naming the evening she can actually keep.

**Payoff/carry:** Every living romantic coda shows at least one real return as well as departure/letters. A doubtful/grieving/unfinished-search return does not cure those native outcomes. An ascended visit needs the run's actual accessible form; changed-body or bodiless states never inherit a human bed scene. Fatal unreturned sacrifice remains bereavement: no slot, living visit or pillow invitation. Last Call distinguishes outstanding spoken list vow from returned/reclaimed/playful/no-vow history, retrieves the actual list where owed and preserves existing flask mechanics. No phantom hand from an absent woman, unidentified death coin or repeated first-night reward. The coda's present opening already has fierce appetite and an interrupted complaint: preserve it and replace only branch-false additions.

## Partner and household handling

**Live/possible canon partner: none.** C4/C8 and CANON-PARTNERS-DESIGN establish Elan as friend and Kiana's partner. Therefore near-discovery, discovery, partner confrontation, share/exclusive/secret demand and partner's own move are **not applicable**, not missing scenes. Do not author adultery, cuckold dynamics or a fabricated husband for Seelah. Her moral question about the Commander's existing word in `door/wanted` is retained; no extra overlap-must-end condition. SEE-04 concerns friendship and conduct, never sexual rivalry.

Household coexistence does not mean she blesses cruelty. Wenduag's existing pair file is **data only, no scenes or intimate nodes** in this export; do not manufacture an audited pair-night or slot. Its already planned prisoner conflict, Wenduag's independent ambition and Seelah's refusal to be used as a paladin endorsement remain coordinator-owned. No lover must die, leave or close for Seelah to desire the Commander. Shared involvement requires current presence, not merely a romance-open flag. No edits to another route or the household ladder are proposed as part of this writing job.

## Explicit-slot placement and briefs

These are reservations for later appended nodes/paragraphs, not runtime nodes added by this planning task. The JSON briefs use the example's voice/scene/last_line/speakers/example/commander/min_lines/max_lines fields plus requested `commander_variants`. Voice is traits; the examples below and in JSON contain only non-graphic heat. Explicit prose is left to the user's chosen tool. Physical facts are limited to her canon human identity, paladin calling and former-thief history; freckles, scar patterns, exact hair texture, measurements and genital assumptions are not canon claims. Setting/position/clothing are labeled authored staging. Each standalone default works even if the generator never runs.

| Slot ID / JSON filename | Insert into existing node; continuation | Default heated-cut text |
|---|---|---|
| `seelah.door.explicit.1` | `seelah.door/night`, after her initiating bed motion, before lamp/sleep; preserve night terminal flags | `{n}Seelah draws you down for another kiss, her bare weight warm against you. Her sword stays on the bedpost; the lamp burns long into the night.{/n}` |
| `seelah.late_afterglow.explicit.1` | `seelah.late_afterglow/night`, after her playful hold, before embedded dawn; then the existing morning/plans | `{n}Seelah lets go of your wrists to pull you closer. Her laugh breaks against your mouth, and neither of you has another clever word for a while.{/n}` |
| `seelah.trickster.dismissed.commit.explicit.1` | `dismissed.commit/threshold`; existing near/far morning | `{n}She pulls you against her beneath the eaves, bare skin warm against yours. The laughter gives way to another kiss; the stairs remain empty until dawn.{/n}` |
| `seelah.trickster.dismissed.second_ask.explicit.1` | `dismissed.second_ask/threshold`; existing near/far morning | `{n}Seelah leaves the recovered thing safely with her clothes and reaches for you again. This time she is smiling for herself, and the door stays shut until morning.{/n}` |
| `seelah.trickster.dismissed.commit_visit.explicit.1` | `dismissed.commit_visit/threshold`, Commander quarters; legacy near/far morning | `{n}She draws you away from the map table and into another kiss. Her belt lands beside yours, and the cold supper waits through the night.{/n}` |
| `seelah.trickster.dismissed.second_ask_visit.explicit.1` | `dismissed.second_ask_visit/threshold`, Commander quarters; legacy near/far morning | `{n}She puts what she reclaimed beyond your reach, then takes your hand and pulls you onto the bed beside her. The maps stay folded until dawn.{/n}` |
| `seelah.trickster.epilogue.commit.explicit.1` | `epilogue.commit/end`, after initiating motion/line, before late muster | `{n}Seelah pulled the Commander close again, bare skin warm beneath their hands. The lamp guttered before either reached to put it out.{/n}` |

The second-ask defaults intentionally call the object 'the recovered thing' only until history-specific custody prose is implemented: list if owed, the voluntary pocket-game object otherwise. Do not create a new supernatural object. Visit briefs are legacy-location variants, not extra nights; if coordinator retires these pages by gating, keep old targets and briefs for saved-node continuity. Do not reactivate them to justify a slot. Multiple slots describe mutually exclusive entry variants; they are not seven required sexual encounters. Keep existing `private_night`, `late_night_kept`, quiet and changed-body receipts separate; no new sexual flag derived from a kiss, rescue or company choice. Delayed genuine first night versus return can be phrased from existing history without a new lock-in.

## Outcomes that must differ

| History | On-page answer / material carry |
|---|---|
| Full future, ordinary | Prior chosen closeness; she says yes to life together; independent work and actual homecomings. Existing full-future mechanics unchanged. |
| Short future | One evening at a time; no new lifetime oath in ending prose. Existing committed flag/legacy ending exit stays intact. |
| Night versus quiet/changed closeness | Sexual dawn recalls only the existing night receipt; nonsexual closeness remains fully romantic and can reach its existing future answer. |
| Returned near versus far | Near has Drezen work; far leaves at noon and comes back on earned leave. Neither posting is inferred romance. |
| Kept list versus returned/reclaimed/playful | Only actual outstanding custody owes collection. She succeeds; voluntary game is her answer, not endless apologetic failure. Restitution survives custody settlement. |
| First-coin refusal versus freedom refusal | Her own first payment versus freely walking out/returning; each pays the stated debt, not interchangeable four-day forgiveness. |
| Friends/company-only | Work, letters and friendship; no bedroom, pillow, late romantic ending or household romantic membership. |
| Parted/refused | Accurate cause and agency; no recurring affectionate empty-purse parcel falsely keeping a closed romance alive. |
| Native grief/doubt/unfinished rescue | Different work and departures; at least one credible return where still lovers, without curing loss or completing an unfinished quest off-page. |
| Current loss or deliberate condemnation | No living scenes without an applicable earned return. Deliberate player kill and matrix closures stand. |
| Fatal unreturned Commander sacrifice | Bereavement only, no explicit slot or living postwar coda. Last Call return must actually occur before living pages. |
| Off-Trickster / Aeon memory variants | Native fate stands. Existing remembered/forgotten legacy exits keep identity/effects; narrowly dependent Trickster changes never leak to other paths. |

## Heat audit — coverage and response classes

The node inventory below quotes the current export verbatim (a single sentence/excerpt per node), including slower choices, mornings, physical aftermath and ending paragraphs. It includes complete romantic scene situations so a contextual setup is not mistaken for an omission; those rows are labeled context. Body-word hits in fights, purse lifting, prayer or ordinary NPC transactions alone are not erotic content. No 'weak quote' is invented when an existing passage is strong. Ratings are editorial register diagnoses, **not independent rubric scores**: H0 nonsexual; H1 affection; H2 sensual appetite; H3 act threshold; E reserved explicit slot. 'Thin' means the situation needs the named rewrite; 'fit' means keep the tone at that heat, not maximize every touch.

Every row names a response class, applied to the whole situation and all siblings:

- **A — Entry/pursuit, H1→H2:** SP1. Keep her initiative; make dance/bench contact deliberate and physical, shorten repetitive objects/comic evasions. Context/refusal nodes keep their purpose. No explicit slot.
- **B — Supper/kiss, H1→H2:** SP2. Desire survives the crumbs: she puts food aside, keeps the hand and kisses with appetite. `promise` and copied `kept` get the same situation repair; delayed kisses remain delayed, not sex.
- **C — Door, H2/H3→E only on night:** SP3. Preserve frank open terms and her initiation; slot `door.explicit.1`; quiet/changed-body pages receive practical in-character closeness, never a false sexual aftermath.
- **D — First morning, H0→H2 on existing night history:** SP3. Put the shared night's physical memory into the bread scene without erasing her independent rescue impulse. Retain existing answers/effects; non-night histories get their own affectionate continuity.
- **F — Faith/watch/grief, H0/H1:** SP4. Keep hard moral particulars; affection can coexist with anger. No sexual cure, repeated head-shake, therapist speech, or invented friendly/partner reaction.
- **G — Future/ordinary/farewell, H1→H2 where fitting:** SP5/6. Keep full/short differences and duties; substitute wanted reunion/touch for generic shelf-and-supper placeholders. Fatigue/farewell need not become sex; parting retains actual mechanics and cause. No new slot.
- **H — Roof, H2:** SP6. Keep a hungry kiss and a physically chosen quiet alternative; no second consent script, generic forehead climax or extra room-night reward.
- **J — Late activity/return, H1/H2:** SP6. Keep the actually played race/music/shelf as history, shorten civic exposition and show her pleasure in company/contact. No trophy or key implies an oath; no extra slot in these public beats.
- **K — Cooper night, H3→E on night:** SP6, `late_afterglow.explicit.1`. Preserve its already strong appetite; remove the abrupt threshold-to-dawn join. Morning stays bodily, reluctant and noisy; kisses/quiet keep their existing choice and nonsexual history.
- **L — Outside-party pursuit/custody:** SP5. Alley already H2, keep it; competence/reclamation and freely chosen pursuit before future yes. No erotic slot in papers/list confrontation or friendship; no generic guilt cured by property exchange.
- **M — Tavern/quarters threshold, H3→E:** SP5; one corresponding `dismissed.*.explicit.1` per threshold sibling. Strong staging is retained. Split ordinary/renewed history in prose; same actual near/far mornings and flags. Dawn desire does not erase departure.
- **N — Endings/codas, H1→H2 selectively:** SP6. Show a real return and a specific welcome where relationship/life/form allow, not endless letters/chairs. No explicit slot except `epilogue.commit.explicit.1`; bereavement, refusal and unresolved courtship remain truthful. Legacy ending mechanics/IDs stay.
- **P — Existing companion reactions, H0 with adult candor:** SP4/5. These are moral/friend reactions, not partner jealousy. Keep Irabeth's anger and Sosiel's concern; they may be frank about Seelah's appetite when known but never turn stolen sacred property into a harmless romance joke. Shared Last Call repairs escalate.

### Node-by-node inventory

<!-- Inventory appended below from the read-only export; all prescriptions above are authored. -->

Inventory: 421 node/paragraph entries across 66 scene situations, including legacy visit siblings and Last Call. Context rows make branch coverage explicit; they do not prescribe sexualizing every conversation.

| Scene ID | Node / paragraph address | Exact existing quote/excerpt | Register rating | Response |
|---|---|---|---|---|
| `seelah.boots` | `start` | {n}Seelah has claimed a bench near the fire with the determined air of someone defending a breach. | H0 context; fit | A |
| `seelah.boots` | `company` | Hers is warm through the worn cloth of her sleeve.{/n} | H0 context; fit | A |
| `seelah.boots` | `rest` | "I can do that." | H0 context; fit | A |
| `seelah.boots` | `sock` | {n}She looks at the sock with exaggerated alarm.{/n} | H0 context; fit | A |
| `seelah.boots` | `meal` | {n}Seelah unwraps the food and divides the apple in two. | H0 context; fit | A |
| `seelah.boots` | `road` | "Us?" | H0 context; fit | A |
| `seelah.boots` | `home` | "Though I might be persuaded to come back before supper." | H0 context; fit | A |
| `seelah.boots` | `plans` | {n}Seelah cuts a blemish out of her half of the apple and drops it into the fire.{/n} | H0 context; fit | A |
| `seelah.boots` | `finish` | A few minutes later her shoulder settles against yours again, this time with no shortage of room on the bench.{/n} | H1 fit | A |
| `seelah.wager` | `start` | {n}Seelah is balancing an empty cup on the edge of a crate. | H0 context; fit | A |
| `seelah.wager` | `terms` | "There is someone nearby who thinks they can play a lute. | H0 context; fit | A |
| `seelah.wager` | `close` | "Nonsense. | H0 context; fit | A |
| `seelah.wager` | `ask` | {n}Seelah looks at the cup, sets it upright, and takes your hand.{/n} | H0 context; fit | A |
| `seelah.wager` | `dance` | {n}Seelah gathers the remaining buttons and drops them into her pocket.{/n} | H0 context; fit | A |
| `seelah.wager` | `dance_end` | {n}She turns under your joined hands and nearly collides with a chair. | H0 context; fit | A |
| `seelah.wager` | `walk` | {n}Seelah collects the two remaining buttons and pockets them.{/n} | H0 context; fit | A |
| `seelah.wager` | `walk_end` | I didn't want to spend the next week pretending I happened to be everywhere you were. | H1 fit | A |
| `seelah.wager` | `button_mine` | {n}Seelah looks at the two in your hand, and the brass stud among them, as if it has betrayed her.{/n} | H0 context; fit | A |
| `seelah.wager` | `button_tip` | "You kept it!" {n}She is ridiculously pleased.{/n} "Most people spend their wages." {n}She nods at the two she has given you.{/n} "No, these are honest buttons. | H0 context; fit | A |
| `seelah.promise` | `start` | That is apparent from the clean shirt, the bread wrapped for two, and the look she gives the person hurrying toward her with a request.{/n} | H0 context; fit | B |
| `seelah.promise` | `search` | I owe you a supper that doesn't start with crawling through the dirt." | H0 context; fit | B |
| `seelah.promise` | `keep` | I did promise." | H0 context; fit | B |
| `seelah.promise` | `later` | If somebody tries to grab me for another errand, remind me I already broke one promise to you." | H0 context; fit | B |
| `seelah.promise` | `supper` | "On the bright side, we can eat these without opening our mouths very far." | H2 fit | B |
| `seelah.promise` | `kiss` | Seelah kisses you, her hand tightening around yours against the blanket.{/n} | H2 fit | B |
| `seelah.promise` | `worry` | "Well, I can't promise I'll suddenly grow wise and sweet-tempered. | H2 fit | B |
| `seelah.promise` | `time` | {n}She eats her share, brushing the crumbs off her shirt with more care this time.{/n} | H0 context; fit | B |
| `seelah.kept` | `start` | The brass clasp has been returned, her good shirt has survived the search, and she has found something better than bread for supper.{/n} | H0 context; fit | B |
| `seelah.kept` | `supper` | "On the bright side, we can eat these without opening our mouths very far." | H2 fit | B |
| `seelah.kept` | `kiss` | Seelah kisses you, her hand tightening around yours against the blanket.{/n} | H2 fit | B |
| `seelah.kept` | `worry` | "Well, I can't promise I'll suddenly grow wise and sweet-tempered. | H2 fit | B |
| `seelah.kept` | `time` | {n}She eats her share, brushing the crumbs off her shirt with more care this time.{/n} | H0 context; fit | B |
| `seelah.changed_opening` | `start` | {n}Seelah hears you out, her feet planted where they are.{/n} | H0 context; fit | C |
| `seelah.changed_opening` | `ask` | "I might. | H0 context; fit | C |
| `seelah.changed_opening` | `time` | {n}A little warmth returns to her face.{/n} | H0 context; fit | C |
| `seelah.changed_opening` | `friend` | Good to hear it from your own mouth. | H2 fit | C |
| `seelah.door` | `start` | Bed, chair, window that mostly shuts. | H0 context; fit | C |
| `seelah.door` | `private` | "I did. | H0 context; fit | C |
| `seelah.door` | `wanted` | {n}She sits on the edge of the bed and pats the blanket beside her.{/n} | H0 context; fit | C |
| `seelah.door` | `wait` | I still want you here, you idiot." | H2 fit | C |
| `seelah.door` | `honest` | "Good." | H0 context; fit | C |
| `seelah.door` | `kiss` | Her hand settles at the back of your neck, warm and steady, and her next kiss is less tentative than the first.{/n} | H2 generic gesture; thin | C: keep appetite, vary forehead gesture |
| `seelah.door` | `night` | The lamp survives. | H3 strong / cut incomplete | E: `seelah.door.explicit.1` + C |
| `seelah.door` | `quiet` | "Then we'll have a quiet evening. | H0 context; fit | C |
| `seelah.door` | `different` | Well, come and tell me what works. | H0 context; fit | C |
| `seelah.morning` | `start` | {n}Seelah is carrying four loaves in a cloth bag. | H0 aftermath; thin | D: restore night-specific physical recall |
| `seelah.morning` | `bargain` | "It was going well until I remembered I had to carry these." | H0 aftermath; thin | D: restore night-specific physical recall |
| `seelah.morning` | `ask` | {n}Seelah opens her mouth, then closes it.{/n} | H0 aftermath; thin | D: restore night-specific physical recall |
| `seelah.morning` | `visit` | What she needs is a place to leave her bedding while she looks for work. | H0 aftermath; thin | D: restore night-specific physical recall |
| `seelah.morning` | `honest` | "Yes. | H0 aftermath; thin | D: restore night-specific physical recall |
| `seelah.morning` | `bread` | "The guards will. | H0 aftermath; thin | D: restore night-specific physical recall |
| `seelah.morning` | `end` | Come and sit with me? | H0 aftermath; thin | D: restore night-specific physical recall |
| `seelah.weight` | `start` | "Yes. | H0 context; fit | F |
| `seelah.weight` | `tell` | "I can do that. | H0 context; fit | F |
| `seelah.weight` | `hear` | "Fair. | H0 context; fit | F |
| `seelah.weight` | `loyalty` | "I want you. | H2 fit | F |
| `seelah.weight` | `end` | {n}The conversation has left her thoughtful. | H0 context; fit | F |
| `seelah.weight` | `part` | {n}She says nothing for a while, then nods.{/n} | H0 context; fit | F |
| `seelah.watch` | `start` | {n}At the Nexus, Seelah is sitting apart from the little camp. | H0 context; fit | F |
| `seelah.watch` | `tell` | "A man being priced as though he were a horse. | H0 context; fit | F |
| `seelah.watch` | `rest` | "Right. | H0 context; fit | F |
| `seelah.watch` | `together` | {n}She laughs, softly at first, then with enough surprise that she has to catch her breath.{/n} | H0 context; fit | F |
| `seelah.souls` | `start` | "Now all I can think is, have they got beds? | H0 context; fit | F |
| `seelah.souls` | `care` | "Arsinoe's been looking after them. | H0 context; fit | F |
| `seelah.souls` | `hurt` | "Yes. | H0 context; fit | F |
| `seelah.souls` | `grief` | {n}She sets the cloth aside.{/n} | H0 context; fit | F |
| `seelah.souls` | `elan` | {n}Seelah nods, looking at the floor.{/n} | H0 context; fit | F |
| `seelah.souls` | `memory` | "He would have had an opinion about the way I'm holding this shield." | H0 context; fit | F |
| `seelah.souls` | `survived` | She catches herself and shakes her head. | H0 gesture duplicated | F: atlas-0017 table-edge response |
| `seelah.souls` | `quiet` | "Tired. | H0 context; fit | F |
| `seelah.souls` | `end` | {n}You stay until she is ready to put the shield away. | H0 context; fit | F |
| `seelah.souls` | `jannah` | {n}The cloth stops moving again, but this time her mouth softens.{/n} | H2 fit | F |
| `seelah.souls` | `jannah_mind` | "I haven't given it to her yet." {n}She smiles at the shield, a little crookedly.{/n} | H0 context; fit | F |
| `seelah.souls` | `abyss_night` | {n}Seelah's hand goes still on the shield.{/n} | H0 context; fit | F |
| `seelah.road` | `future_entry` | "I'd like that. | H0/H1 context; thin | G |
| `seelah.road` | `future_abyss` | "First, have we left anything hanging? | H0/H1 context; thin | G |
| `seelah.road` | `future_copyist` | "Yes. | H0/H1 context; thin | G |
| `seelah.road` | `future_activity` | "And when we try to help someone and make a mess of it, I want you there for the cleaning up. | H2 fit | G |
| `seelah.road` | `future_visits` | "Let's start with an outing. | H0/H1 context; thin | G |
| `seelah.road` | `future_saw` | "The washing yard, then. | H0/H1 context; thin | G |
| `seelah.road` | `future_platform` | I want to see what came of it before I begin congratulating anyone." | H0/H1 context; thin | G |
| `seelah.road` | `future_faith` | "I did. | H0/H1 context; thin | G |
| `seelah.road` | `future_roof` | "Food, sky, and no grand plan. | H0/H1 context; thin | G |
| `seelah.road` | `future_race` | "I intend to enjoy that afternoon whether I win or not. | H0/H1 context; thin | G |
| `seelah.road` | `future_quest` | "Before you clear a shelf for my things, remember I've still got work to do for my friends. | H0/H1 context; thin | G |
| `seelah.road` | `future_unfinished` | "I want to live with you. | H2 fit | G |
| `seelah.road` | `future_bad` | "We brought the souls back. | H0/H1 context; thin | G |
| `seelah.road` | `future_moderate` | "I thought I knew what I was doing. | H0/H1 context; thin | G |
| `seelah.road` | `future_returned` | "We brought them back! | H0/H1 context; thin | G |
| `seelah.road` | `future_elan` | {n}Seelah takes a moment before answering.{/n} | H0/H1 context; thin | G |
| `seelah.road` | `future_elan_dead` | But I want to tell you about him, then stay here with you over supper. | H0/H1 context; thin | G |
| `seelah.road` | `future_elan_other` | "You'll have to ask him. | H0/H1 context; thin | G |
| `seelah.road` | `short_quest` | "Before you clear a shelf for my things, remember I've still got work to do for my friends. | H0/H1 context; thin | G |
| `seelah.road` | `short_unfinished` | "I want to live with you. | H2 fit | G |
| `seelah.road` | `short_bad` | "We brought the souls back. | H0/H1 context; thin | G |
| `seelah.road` | `short_moderate` | "I thought I knew what I was doing. | H0/H1 context; thin | G |
| `seelah.road` | `short_returned` | "We brought them back! | H0/H1 context; thin | G |
| `seelah.road` | `short_elan` | {n}Seelah takes a moment before answering.{/n} | H0/H1 context; thin | G |
| `seelah.road` | `short_elan_dead` | But I want to tell you about him, then stay here with you over supper. | H0/H1 context; thin | G |
| `seelah.road` | `short_elan_other` | "You'll have to ask him. | H0/H1 context; thin | G |
| `seelah.road` | `short_choice` | I want you here. | H2 fit | G |
| `seelah.road` | `short_end` | "All right. | H0/H1 context; thin | G |
| `seelah.road` | `start` | "Every time I start thinking of it, I want to say a prayer and check my sword. | H2 fit | G |
| `seelah.road` | `home` | "A place I can come back to. | H0/H1 context; thin | G |
| `seelah.road` | `travel` | "I'd like that. | H0/H1 context; thin | G |
| `seelah.road` | `fate` | If you find a way, I want to help." | H2 fit | G |
| `seelah.road` | `choose` | I want you to stick with me when they do. | H2 fit | G |
| `seelah.road` | `yes` | I had something better prepared. | H0/H1 context; thin | G |
| `seelah.road` | `no` | {n}She closes her hand and draws it back.{/n} | H0/H1 context; thin | G |
| `seelah.road` | `development_check` | The promise goes with you.{/n} | H0/H1 context; thin | G |
| `seelah.ordinary` | `start` | {n}Seelah opens the door with her hair half unbraided and a weary expression that brightens when she sees you.{/n} | H0/H1 context; thin | G |
| `seelah.ordinary` | `rest` | "Nothing, actually. | H0/H1 context; thin | G |
| `seelah.ordinary` | `quiet` | This is nice, | H0/H1 context; thin | G |
| `seelah.ordinary` | `end` | "If you can bear the boots and the dirty shirts, I reckon you'll survive another visit." | H0/H1 context; thin | G |
| `seelah.farewell` | `farewell_entry` | "Before we say our last goodbyes to Drezen, are there invitations we still mean to keep? | H0/H1 context; thin | G |
| `seelah.farewell` | `farewell_pending` | {n}Seelah sits down beside you and counts your unfinished outings on her fingers.{/n} | H0/H1 context; thin | G |
| `seelah.farewell` | `farewell_copyist` | "Yes. | H0/H1 context; thin | G |
| `seelah.farewell` | `farewell_activity` | "So do I. | H0/H1 context; thin | G |
| `seelah.farewell` | `farewell_evening` | "Good. | H0/H1 context; thin | G |
| `seelah.farewell` | `farewell_step` | "Then let's go! | H0/H1 context; thin | G |
| `seelah.farewell` | `start` | {n}Seelah checks the fastening on her shield, then makes herself stop checking it.{/n} | H0/H1 context; thin | G |
| `seelah.farewell` | `shelf` | "I want to be there when we choose it. | H0/H1 context; thin | G |
| `seelah.farewell` | `journey` | "I want to see you somewhere nobody needs to call you Commander." | H0/H1 context; thin | G |
| `seelah.farewell` | `boots` | "I can promise those. | H0/H1 context; thin | G |
| `seelah.farewell` | `end` | "I love you. | H1 fit | G |
| `seelah.parting` | `start` | {n}Seelah's attention sharpens.{/n} | H0/H1 context; thin | G |
| `seelah.parting` | `end` | {n}She listens without interrupting. | H0/H1 context; thin | G |
| `seelah.parting` | `stay` | I've had three suppers go cold waiting for you this month, | H0/H1 invented recall; weak | G: prospective actual evening, no invented misses |
| `seelah.ending_together` | `history` | Seelah had not forgotten what they had promised each other.{/n} | H0/H1 context; thin | N |
| `seelah.ending_together` | `start` | {n}Seelah continued to find people who needed her help. | H0/H1 context; thin | N |
| `seelah.ending_together` | `short_history` | {n}Seelah and the Commander had promised to meet again. | H0/H1 context; thin | N |
| `seelah.ending_together` | `earlier_promise` | {n}Seelah meant to keep her promise to the Commander. | H0/H1 context; thin | N |
| `seelah.ending_unsettled` | `history` | Seelah had not forgotten what they had promised each other.{/n} | H0/H1 context; thin | N |
| `seelah.ending_unsettled` | `start` | She kissed the Commander goodbye, but packed her saddlebags all the same.{/n} | H2 fit | N |
| `seelah.ending_unsettled` | `short_history` | {n}Seelah and the Commander had promised to meet again. | H0/H1 context; thin | N |
| `seelah.ending_unsettled` | `earlier_promise` | {n}Seelah meant to keep her promise to the Commander. | H0/H1 context; thin | N |
| `seelah.ending_grieving` | `history` | Seelah had not forgotten what they had promised each other.{/n} | H0/H1 context; thin | N |
| `seelah.ending_grieving` | `start` | {n}Returning the stolen souls had not given Seelah back everyone she lost. | H0/H1 context; thin | N |
| `seelah.ending_grieving` | `short_history` | {n}Seelah and the Commander had promised to meet again. | H0/H1 context; thin | N |
| `seelah.ending_grieving` | `earlier_promise` | {n}Seelah meant to keep her promise to the Commander. | H0/H1 context; thin | N |
| `seelah.ending_unfinished_work` | `history` | Seelah had not forgotten what they had promised each other.{/n} | H0/H1 context; thin | N |
| `seelah.ending_unfinished_work` | `start` | She greeted them warmly when they met, and left reluctantly when the next lead drew her away. | H0/H1 context; thin | N |
| `seelah.ending_unfinished_work` | `short_history` | {n}Seelah and the Commander had promised to meet again. | H0/H1 context; thin | N |
| `seelah.ending_unfinished_work` | `earlier_promise` | {n}Seelah meant to keep her promise to the Commander. | H0/H1 context; thin | N |
| `seelah.ending_changed` | `history` | Seelah had not forgotten what they had promised each other.{/n} | H0/H1 context; thin | N |
| `seelah.ending_changed` | `start` | {n}Seelah never became indifferent to what the Commander's power could do. | H0/H1 context; thin | N |
| `seelah.ending_changed` | `short_history` | {n}Seelah and the Commander had promised to meet again. | H0/H1 context; thin | N |
| `seelah.ending_changed` | `earlier_promise` | {n}Seelah meant to keep her promise to the Commander. | H0/H1 context; thin | N |
| `seelah.ending_ascended` | `history` | Seelah had not forgotten what they had promised each other.{/n} | H0/H1 context; thin | N |
| `seelah.ending_ascended` | `start` | When the Commander visited, she was glad to waste an evening talking about supper and ruined boots.{/n} | H0/H1 context; thin | N |
| `seelah.ending_ascended` | `short_history` | {n}Seelah and the Commander had promised to meet again. | H0/H1 context; thin | N |
| `seelah.ending_ascended` | `earlier_promise` | {n}Seelah meant to keep her promise to the Commander. | H0/H1 context; thin | N |
| `seelah.ending_apart` | `start` | {n}Seelah and the Commander stopped planning their evenings together. | H0/H1 loss/refusal; fit | N: history-specific; no living/sexual reward |
| `seelah.ending_unfinished` | `start` | The war ended before they found out whether supper and a chair by the fire would follow.{/n} | H0/H1 loss/refusal; fit | N: history-specific; no living/sexual reward |
| `seelah.ending_aeon` | `start` | She slept on her own side of it anyway, and in the morning she rolled it up and went on.{/n} | H0/H1 loss/refusal; fit | N: history-specific; no living/sexual reward |
| `seelah.ending_sacrifice` | `start` | {n}Then she went where she was needed, because that was the promise they had actually made each other, and she would not let the Wound have that as well.{/n} | H0/H1 loss/refusal; fit | N: history-specific; no living/sexual reward |
| `seelah.ending_sacrifice` | `start.Paragraphs[0]` | {n}The purse stayed in her pack, tied badly on purpose, with the note still inside that she had meant to leave on a pillow after the war. | H0/H1 loss/refusal; fit | N: history-specific; no living/sexual reward |
| `seelah.ending_sacrifice` | `start.Paragraphs[1]` | {n}There was no body to wait for. | H0/H1 loss/refusal; fit | N: history-specific; no living/sexual reward |
| `seelah.fate_return` | `start` | "They'll all want to hear what it was like. | H0 context; fit | L |
| `seelah.fate_return` | `own` | "Good. | H0 context; fit | L |
| `seelah.fate_return` | `end` | {n}This time her laugh sounds like herself.{/n} | H0 context; fit | L |
| `seelah.fate_return` | `quiet` | {n}She moves her hand to make room beside her.{/n} | H0 context; fit | L |
| `seelah.letter_after` | `end` | {n}She lays her hand beside yours, her little finger brushing your knuckle.{/n} | H1 fit | J |
| `seelah.letter_work` | `signal_used` | Then she closes her mouth and watches the copyist take a pen from her sleeve.{/n} | H2 fit | J |
| `seelah.letter_work` | `warm` | {n}She narrows her eyes at you, then breaks into a smile.{/n} | H0 context; fit | J |
| `seelah.inheritors_corner` | `start` | {n}Seelah is waiting beside a sheltered alcove in Drezen. | H0 context; fit | F |
| `seelah.inheritors_corner` | `prayer` | {n}Her lips move without sound. | H2 fit | F |
| `seelah.inheritors_corner` | `own` | "Of course." | H0 context; fit | F |
| `seelah.inheritors_corner` | `doubt` | Some mornings I kneel down and can't get a word out anyway. | H0 context; fit | F |
| `seelah.inheritors_corner` | `quiet_words` | "Names. | H0 context; fit | F |
| `seelah.inheritors_corner` | `after` | "Yes. | H0 context; fit | F |
| `seelah.inheritors_corner` | `outcomes` | {n}You reach a low wall overlooking a narrow garden. | H0 context; fit | F |
| `seelah.inheritors_corner` | `bad` | "Some days I'll want to saddle a horse and ride out alone. | H0 context; fit | F |
| `seelah.inheritors_corner` | `moderate` | Then they ask why, and suddenly I've got a mouth full of turnips." | H2 fit | F |
| `seelah.inheritors_corner` | `rescued` | "I still want to charge ahead shouting, 'This time it'll be better!' You'd think I'd have bitten my tongue off by now." | H0 context; fit | F |
| `seelah.inheritors_corner` | `unfinished` | "We can have supper. | H2 fit | F |
| `seelah.inheritors_corner` | `friends` | "Elan is part of it." | H0 context; fit | F |
| `seelah.inheritors_corner` | `elan` | Made me want to shake him. | H0 context; fit | F |
| `seelah.inheritors_corner` | `elan_living` | Then I remember he has a perfectly good mouth of his own." | H2 fit | F |
| `seelah.inheritors_corner` | `plans` | I'll bring supper. | H0 context; fit | F |
| `seelah.roof_evening` | `start` | {n}Mera lets you through her workshop and points to the stairs. | H0 context; fit | H |
| `seelah.roof_evening` | `pickle` | {n}You bite into something crisp, sour, and startlingly hot. | H1 fit | H |
| `seelah.roof_evening` | `first` | "Coward." | H0 context; fit | H |
| `seelah.roof_evening` | `sky` | {n}From the terrace you can see above the nearest roofs. | H0 context; fit | H |
| `seelah.roof_evening` | `home` | "You said supper at home. | H0 context; fit | H |
| `seelah.roof_evening` | `road` | "A journey with stairs. | H0 context; fit | H |
| `seelah.roof_evening` | `try` | You want supper. | H0 context; fit | H |
| `seelah.roof_evening` | `future` | But right now I'm looking at your mouth, and I'd rather you were sitting here." | H2 fit | H |
| `seelah.roof_evening` | `others` | I don't fancy kissing you while someone else waits over a cold supper." | H2 fit | H |
| `seelah.roof_evening` | `kiss` | You can feel her smiling before she draws back. | H2 fit | H: keep; this kiss should stay non-explicit |
| `seelah.roof_evening` | `quiet` | {n}She shifts closer and leans against you. | H1 fit | H |
| `seelah.roof_evening` | `leave` | {n}You pack the cups and the remaining food into the basket. | H0 context; fit | H |
| `seelah.roof_evening` | `promised` | "And if I get so busy chasing answers that I forget supper with you, remind me of this roof. | H0 context; fit | H |
| `seelah.roof_evening` | `consider` | "Tomorrow, then. | H0 context; fit | H |
| `seelah.late_course` | `start` | {n}Seelah looks at her sleeve, then at the chalk in her hand, as if considering an accusation she cannot quite refute.{/n} | H1 fit | J |
| `seelah.late_course` | `course` | {n}Dena runs from the chalk line, rounds two barrels and ducks beneath a cord without touching it. | H1 fit | J |
| `seelah.late_course` | `runner` | On the second she opens her fingers as yours close. | H1 fit | J |
| `seelah.late_course` | `watcher` | "Yes. | H0 context; fit | J |
| `seelah.late_course` | `invitation` | "I want to do that. | H0 context; fit | J |
| `seelah.late_course` | `fixed` | I want to teach them and beat Tavia. | H0 context; fit | J |
| `seelah.late_course` | `shared` | {n}She opens her mouth, shuts it, and laughs.{/n} | H2 fit | J |
| `seelah.late_course` | `end` | {n}At the next corner she stops and catches your hand.{/n} | H0 context; fit | J |
| `seelah.late_lesson` | `start` | {n}Istra has laid three battered practice shields against the yard wall. | H0 context; fit | J |
| `seelah.late_lesson` | `arrangement` | {n}Istra gives Seelah the largest shield. | H0 context; fit | J |
| `seelah.late_lesson` | `fixed` | "When I'm in Drezen, we meet at this hour. | H0 context; fit | J |
| `seelah.late_lesson` | `shared` | {n}Istra takes the smallest shield and demonstrates how to brace its lower edge against her leg. | H0 context; fit | J |
| `seelah.late_lesson` | `pressure` | {n}The next exercise puts you behind a shield while Seelah presses against its front. | H0 context; fit | J |
| `seelah.late_lesson` | `one` | "This one. | H0 context; fit | J |
| `seelah.late_lesson` | `answer` | {n}"The way she braced it," the woman says, pointing to Istra. | H0 context; fit | J |
| `seelah.late_lesson` | `after` | "I enjoyed showing off. | H0 context; fit | J |
| `seelah.late_lesson` | `practice` | {n}Seelah runs the course twice. | H0 context; fit | J |
| `seelah.late_lesson` | `part` | "The barrel moved. | H0 context; fit | J |
| `seelah.late_page` | `start` | "I bought this to write down things I want to do. | H0 context; fit | J |
| `seelah.late_page` | `outcome` | "Yes. | H0 context; fit | J |
| `seelah.late_page` | `grief` | Ask me after supper." | H0 context; fit | J |
| `seelah.late_page` | `questions` | "I'll find people who've wrestled with the same questions. | H0 context; fit | J |
| `seelah.late_page` | `hope` | Then I remember I haven't asked whether any of them want to come." | H0 context; fit | J |
| `seelah.late_page` | `unfinished` | "I can't write 'all's well.' It isn't. | H0 context; fit | J |
| `seelah.late_page` | `elan_gate` | {n}The next page has Elan's name at the top. | H0 context; fit | J |
| `seelah.late_page` | `elan_dead` | "I said I wouldn't put words in his mouth now he can't argue back. | H2 fit | J |
| `seelah.late_page` | `elan_letter` | "I'll tell him about Istra. | H0 context; fit | J |
| `seelah.late_page` | `own` | Supper's coming." | H1 fit | J |
| `seelah.late_page` | `chosen` | {n}She pockets the booklet and leans her shoulder against yours before either of you rises.{/n} | H1 fit | J |
| `seelah.late_page` | `place` | "A few things. | H1 fit | J |
| `seelah.late_race` | `start` | She plants it where she can see the exchange and tells Seelah that looking at the finish before making the last turn is an excellent way to kiss a barrel.{/n} | H2 fit | J |
| `seelah.late_race` | `preparation` | {n}Before anyone runs, Seelah takes one turn around the course at a walk. | H0 context; fit | J |
| `seelah.late_race` | `fixed` | "I know what I do wrong. | H1 fit | J |
| `seelah.late_race` | `shared` | "That turn. | H0 context; fit | J |
| `seelah.late_race` | `role` | {n}Tavia repeats the rules for the spectators, who immediately discover several opinions nobody asked for. | H0 context; fit | J |
| `seelah.late_race` | `running` | {n}Seelah runs first against Tavia. | H0 context; fit | J |
| `seelah.late_race` | `narrow` | {n}You plant your foot close to the barrel, turn and stretch the hoop toward its peg. | H0 context; fit | J |
| `seelah.late_race` | `stumble` | {n}Your planted foot slides over loose grit. | H1 fit | J |
| `seelah.late_race` | `wide` | {n}You take the wider line without losing your footing. | H0 context; fit | J |
| `seelah.late_race` | `watching` | {n}Seelah runs first against Tavia, loses a little ground beneath the cord and gains it at the peg. | H0 context; fit | J |
| `seelah.late_race` | `won` | "The shortest song I know." | H1 fit | J |
| `seelah.late_race` | `lost` | {n}Tavia chooses a song about a woman who keeps returning to a house because she has forgotten something, until everybody but the woman knows why she goes there. | H1 fit | J |
| `seelah.late_race` | `clear` | Istra carries her stool away after making Seelah promise only to tell her when another race is planned, not to organize one before anyone has recovered from this one.{/n} | H0 context; fit | J |
| `seelah.late_afterglow` | `start` | {n}She has hired the little room above the cooper's shed until morning. | H2 fit | K |
| `seelah.late_afterglow` | `race` | {n}She pours the water, drinks half of hers in one go, and hands you the other cup. | H0 context; fit | K |
| `seelah.late_afterglow` | `victory` | I still want to boast about my magnificent victory." | H1 fit | K |
| `seelah.late_afterglow` | `song` | "Most of it. | H0 context; fit | K |
| `seelah.late_afterglow` | `ask` | I want you. | H2 fit | K |
| `seelah.late_afterglow` | `night` | In the morning she wakes before you. | H3 strong / join abrupt | E: `seelah.late_afterglow.explicit.1` + K |
| `seelah.late_afterglow` | `morning` | I want another morning like this one. | H2 fit | K |
| `seelah.late_afterglow` | `kisses` | {n}She meets your kiss with a pleased sound and gives it back with interest. | H2 fit | K |
| `seelah.late_afterglow` | `quiet` | {n}She sits on the bed and shoves a folded blanket out of the way. | H0 context; fit | K |
| `seelah.late_afterglow` | `plans` | {n}She puts the booklet away and holds out her hand for yours, as if the next meeting were already a thing she had in her pocket.{/n} | H1 fit | K |
| `seelah.late_first_step` | `start` | {n}Seelah meets you without armor, her little booklet tucked into her belt. | H0 context; fit | J |
| `seelah.late_first_step` | `wish` | "Your idea today. | H0 context; fit | J |
| `seelah.late_first_step` | `music` | {n}You have chosen a small gathering in a courtyard, where a woman with a reed pipe plays for whoever can spare the time to listen. | H0 context; fit | J |
| `seelah.late_first_step` | `quiet_phrase` | {n}She waits for the phrase. | H0 context; fit | J |
| `seelah.late_first_step` | `quick_phrase` | Seelah grins, stops tapping, and curls her fingers around yours.{/n} | H1 fit | J |
| `seelah.late_first_step` | `shelf` | {n}The cooper has agreed to rent Seelah a small locking cupboard in the room above the shed. | H0 context; fit | J |
| `seelah.late_first_step` | `keepsake` | {n}You set a small personal keepsake beside the cup. | H0 context; fit | J |
| `seelah.late_first_step` | `space` | "Then it stays empty." | H0 context; fit | J |
| `seelah.late_first_step` | `carry` | Let's pick it before I promise to haul barrels for somebody." | H0 context; fit | J |
| `seelah.late_first_step` | `committed` | And I want you beside me on days when all we're fighting over is a song." | H2 fit | J |
| `seelah.late_first_step` | `courting` | Don't promise me a whole week and spend it chasing demons." | H0 context; fit | J |
| `seelah.late_first_step` | `end` | I want to see who complains first." | H0 context; fit | J |
| `seelah.letter_return` | `company` | {n}She keeps pace beside you, her shoulder brushing yours as you turn down the passage.{/n} | H1 fit | J |
| `seelah.future_followup` | `future_entry` | "I remember our promise. | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_abyss` | "First, have we left anything hanging? | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_copyist` | "Yes. | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_activity` | "And when we try to help someone and make a mess of it, I want you there for the cleaning up. | H2 fit | G |
| `seelah.future_followup` | `future_visits` | "Let's start with an outing. | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_saw` | "The washing yard, then. | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_platform` | I want to see what came of it before I begin congratulating anyone." | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_faith` | "I did. | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_roof` | "Food, sky, and no grand plan. | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_race` | "I intend to enjoy that afternoon whether I win or not. | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_quest` | "Before you clear a shelf for my things, remember I've still got work to do for my friends. | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_unfinished` | "I want to live with you. | H2 fit | G |
| `seelah.future_followup` | `future_bad` | "We brought the souls back. | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_moderate` | "I thought I knew what I was doing. | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_returned` | "We brought them back! | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_elan` | {n}Seelah takes a moment before answering.{/n} | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_elan_dead` | But I want to tell you about him, then stay here with you over supper. | H0/H1 context; thin | G |
| `seelah.future_followup` | `future_elan_other` | "You'll have to ask him. | H0/H1 context; thin | G |
| `seelah.future_followup` | `kept_promise` | "I remember our promise. | H1 fit | G |
| `seelah.future_followup` | `renewed` | "Good! | H0/H1 context; thin | G |
| `seelah.farewell_catchup` | `start` | "Yes! | H0/H1 context; thin | G |
| `seelah.farewell_catchup` | `yes` | "Come and get me when you can stay a while. | H0/H1 context; thin | G |
| `seelah.trickster.dead.wakes` | `start` | "You robbed my corpse." | H0 context; fit | L |
| `seelah.trickster.dead.wakes` | `coin_word` | "On your word." {n}She closes her eyes.{/n} "You emptied a dead paladin's purse, brought the priests stones off the Kenabres altars, and asked them for credit. | H0 context; fit | L |
| `seelah.trickster.dead.wakes` | `coin` | "He showed me one of the stones. | H0 context; fit | L |
| `seelah.trickster.dead.wakes` | `given` | {n}She unfolds the list and reads the last line. | H0 context; fit | L |
| `seelah.trickster.dead.wakes` | `kept` | {n}Her hand stays out a moment longer. | H0 context; fit | L |
| `seelah.trickster.dead.wakes` | `coin_word_paid` | "On your word." {n}She shuts her eyes, then opens them again.{/n} "You paid a grave-robber with crusade gold. | H0 context; fit | L |
| `seelah.trickster.dismissed.back_for_the_papers` | `start` | {n}She is waiting in the tavern, at the table nearest the door, with her back to the wall like a thief and her boots polished like a paladin. | H0 context; fit | L |
| `seelah.trickster.dismissed.back_for_the_papers` | `papers_caught` | "And you got caught. | H0 context; fit | L |
| `seelah.trickster.dismissed.back_for_the_papers` | `papers` | "My transfer papers. | H0 context; fit | L |
| `seelah.trickster.dismissed.back_for_the_papers` | `handed` | {n}She takes them without looking at them and puts them inside her tunic, flat against her ribs, where nobody is going to get them again.{/n} | H0 context; fit | L |
| `seelah.trickster.dismissed.back_for_the_papers` | `dared` | {n}She stands, walks round the table, stumbles, catches your arm and says she is so sorry, what a clumsy fool. | H0 context; fit | L |
| `seelah.trickster.dismissed.back_for_the_papers` | `dared_2` | {n}She drops the purse back in your lap.{/n} | H0 context; fit | L |
| `seelah.trickster.dismissed.back_for_the_papers_letter` | `start` | {n}A note, folded small enough to slip into a pocket and badly enough that it wants you to know it was folded in a temper.{/n} | H0 context; fit | L |
| `seelah.trickster.after.stay_or_go` | `start` | {n}She has two recruiting notices on the table in front of her, weighted with her tankard so the draught from the door cannot take them.{/n} | H0 context; fit | L |
| `seelah.trickster.after.stay_or_go` | `choice` | "There's a relief company on the Drezen road that'll take a paladin with no references and a bad reputation. | H0 context; fit | L |
| `seelah.trickster.after.stay_or_go` | `folded` | I want to finish my drink without a Commander watching me decide things." | H0 context; fit | L |
| `seelah.trickster.dismissed.commit` | `start` | {n}The same table by the door. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit` | `near` | "I took the Drezen road company, by the way. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit` | `far` | "I took the border company, by the way. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit` | `ask` | {n}She waits, chin on her fist, the way she waits out a sermon she has heard before.{/n} | H0 context; fit | M |
| `seelah.trickster.dismissed.commit` | `answer` | {n}She does not look away. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit` | `no_stones` | {n}She presses her hand over the list inside her tunic.{/n} | H0 context; fit | M |
| `seelah.trickster.dismissed.commit` | `list_back` | {n}She does not touch it at once. | H1 fit | M |
| `seelah.trickster.dismissed.commit` | `chooses` | {n}She looks at your coat, then at you. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit` | `threshold` | Old habits." {n}Her breath is hot on your mouth.{/n} "Now hold still. | H3 strong / join abrupt | E: `seelah.trickster.dismissed.commit.explicit.1` + M |
| `seelah.trickster.dismissed.commit` | `morning_near` | {n}Morning. | H2 fit; posting must survive | M: preserve desire; dramatize own duty |
| `seelah.trickster.dismissed.commit` | `morning_far` | {n}Morning. | H2 fit; posting must survive | M: preserve desire; dramatize own duty |
| `seelah.trickster.dismissed.commit` | `friend` | "As a friend." {n}She tries it out.{/n} "Yes. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit` | `door` | "Go and help people. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit` | `no` | {n}She is quiet a long time.{/n} | H0 context; fit | M |
| `seelah.trickster.dismissed.commit` | `no_death` | {n}Her hand goes to the place under her collarbone where her purse hangs, the way it does when she thinks nobody is watching.{/n} | H0 context; fit | M |
| `seelah.trickster.dismissed.second_ask` | `price` | {n}She walked out of Fye's the night you first asked, on her own feet, and took the Sarkorian road. | H0 context; fit | M |
| `seelah.trickster.dismissed.second_ask` | `robbed` | {n}You keep your hands at your sides. | H0 context; fit | M |
| `seelah.trickster.dismissed.second_ask` | `threshold` | Old habits." {n}Her breath is hot on your mouth.{/n} "Now hold still. | H3 strong / join abrupt | E: `seelah.trickster.dismissed.second_ask.explicit.1` + M |
| `seelah.trickster.dismissed.second_ask` | `morning_near` | {n}Morning. | H2 fit; posting must survive | M: preserve desire; dramatize own duty |
| `seelah.trickster.dismissed.second_ask` | `morning_far` | {n}Morning. | H2 fit; posting must survive | M: preserve desire; dramatize own duty |
| `seelah.trickster.dismissed.second_ask` | `closed` | {n}She looks at your hand on your purse. | H0 context; fit | M |
| `seelah.trickster.after.courtship` | `start` | {n}She is on her feet before you reach the table, cloak already round her shoulders, as if she has been waiting all evening for an excuse.{/n} | H0 context; fit | L |
| `seelah.trickster.after.courtship` | `market` | {n}The east market at dusk is lamp-smoke, wet wool and pilgrims haggling over candles. | H0 context; fit | L |
| `seelah.trickster.after.courtship` | `won` | {n}Ten steps on she pats her belt and stops dead in the street, mouth open.{/n} | H2 fit | L |
| `seelah.trickster.after.courtship` | `lost` | You owe me a drink and a ring." {n}She takes your collar and pulls you into the gap between the cooper's and the chandler's, out of the lamplight, where nobody from the crusade will see t… | H0 context; fit | L |
| `seelah.trickster.after.courtship` | `alley` | She is warm through the cloak, and she smells of tavern smoke and the oil she uses on her sword.{/n} | H2 fit | L |
| `seelah.trickster.after.courtship` | `kissed` | {n}You kiss her, or she kisses you; later neither of you will admit which. | H2 fit | L |
| `seelah.trickster.after.courtship` | `friends_walk` | {n}She looks at you a breath longer, then laughs and lets go of your collar.{/n} | H0 context; fit | L |
| `seelah.trickster.after.stay_or_go_visit` | `start` | {n}She is waiting in your quarters in the citadel when you come off the wall, on your one good chair with her boots on your map table. | H0 context; fit | L |
| `seelah.trickster.after.stay_or_go_visit` | `choice` | "There's a relief company on the Drezen road that'll take a paladin with no references and a bad reputation. | H0 context; fit | L |
| `seelah.trickster.after.stay_or_go_visit` | `folded` | I want to finish your wine without a Commander watching me decide things. | H0 context; fit | L |
| `seelah.trickster.after.courtship_visit` | `start` | {n}She is at your door when you come off the wall, cloak already round her shoulders, as if she has been waiting all evening for an excuse.{/n} | H0 context; fit | L |
| `seelah.trickster.after.courtship_visit` | `market` | {n}The east market at dusk is lamp-smoke, wet wool and pilgrims haggling over candles. | H0 context; fit | L |
| `seelah.trickster.after.courtship_visit` | `won` | {n}Ten steps on she pats her belt and stops dead in the street, mouth open.{/n} | H2 fit | L |
| `seelah.trickster.after.courtship_visit` | `lost` | You owe me a drink and a ring." {n}She takes your collar and pulls you into the gap between the cooper's and the chandler's, out of the lamplight, where nobody from the crusade will see t… | H0 context; fit | L |
| `seelah.trickster.after.courtship_visit` | `alley` | She is warm through the cloak, and she smells of tavern smoke and the oil she uses on her sword.{/n} | H2 fit | L |
| `seelah.trickster.after.courtship_visit` | `kissed` | {n}You kiss her, or she kisses you; later neither of you will admit which. | H2 fit | L |
| `seelah.trickster.after.courtship_visit` | `friends_walk` | {n}She looks at you a breath longer, then laughs and lets go of your collar.{/n} | H0 context; fit | L |
| `seelah.trickster.dismissed.commit_visit` | `start` | {n}Your quarters again, and your one good chair turned to face the door. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit_visit` | `near` | "I took the Drezen road company, by the way. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit_visit` | `far` | "I took the border company, by the way. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit_visit` | `ask` | {n}She waits, chin on her fist, the way she waits out a sermon she has heard before.{/n} | H0 context; fit | M |
| `seelah.trickster.dismissed.commit_visit` | `answer` | {n}She does not look away. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit_visit` | `no_stones` | {n}She presses her hand over the list inside her tunic.{/n} | H0 context; fit | M |
| `seelah.trickster.dismissed.commit_visit` | `list_back` | {n}She does not touch it at once. | H1 fit | M |
| `seelah.trickster.dismissed.commit_visit` | `chooses` | {n}She looks at your coat, then at you. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit_visit` | `threshold` | She takes you by the belt and walks you backwards across your own quarters, past the map table and the cold supper, and somewhere on the way the belt comes away in her hand.{/n} | H3 strong / join abrupt | E: `seelah.trickster.dismissed.commit_visit.explicit.1` + M |
| `seelah.trickster.dismissed.commit_visit` | `morning_near` | {n}Morning. | H2 fit; posting must survive | M: preserve desire; dramatize own duty |
| `seelah.trickster.dismissed.commit_visit` | `morning_far` | {n}Morning. | H2 fit; posting must survive | M: preserve desire; dramatize own duty |
| `seelah.trickster.dismissed.commit_visit` | `friend` | "As a friend." {n}She tries it out.{/n} "Yes. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit_visit` | `door` | "Go and help people. | H0 context; fit | M |
| `seelah.trickster.dismissed.commit_visit` | `no` | {n}She is quiet a long time.{/n} | H0 context; fit | M |
| `seelah.trickster.dismissed.commit_visit` | `no_death` | {n}Her hand goes to the place under her collarbone where her purse hangs, the way it does when she thinks nobody is watching.{/n} | H0 context; fit | M |
| `seelah.trickster.dismissed.second_ask_visit` | `price` | {n}She walked out of the citadel gate the night you first asked, on her own feet, and took the Sarkorian road. | H0 context; fit | M |
| `seelah.trickster.dismissed.second_ask_visit` | `robbed` | {n}You keep your hands at your sides. | H0 context; fit | M |
| `seelah.trickster.dismissed.second_ask_visit` | `threshold` | She takes you by the belt and walks you backwards across your own quarters, past the map table and the cold supper, and somewhere on the way the belt comes away in her hand.{/n} | H3 strong / join abrupt | E: `seelah.trickster.dismissed.second_ask_visit.explicit.1` + M |
| `seelah.trickster.dismissed.second_ask_visit` | `morning_near` | {n}Morning. | H2 fit; posting must survive | M: preserve desire; dramatize own duty |
| `seelah.trickster.dismissed.second_ask_visit` | `morning_far` | {n}Morning. | H2 fit; posting must survive | M: preserve desire; dramatize own duty |
| `seelah.trickster.dismissed.second_ask_visit` | `closed` | {n}She looks at your hand on your purse. | H0 context; fit | M |
| `seelah.trickster.epilogue.pickpocket` | `end` | {n}Of everything the Commander ever took from her, Seelah said, her purse was the one that counted.{/n} | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[0]` | {n}Seelah remembered the night at her bier: her purse emptied, her list read without asking, and the Kenabres stones brought to the chaplain's bowl. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[1]` | {n}Seelah remembered her effects opened in Drezen while her body lay in a field chaplain's keeping. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[2]` | {n}Seelah kept the list in her purse, tied in badly on purpose. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[3]` | {n}The Commander never did give it back. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[4]` | {n}The chapel never quite forgave the credit the Commander had asked of it, or the stolen stones it had ground. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[5]` | {n}The relic-seller told the story of the night the Commander of the crusade robbed him in every tavern in Drezen, for years, and never told it the same way twice. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[6]` | {n}Of the transfer papers she said only that they had come back to her, and that she now kept them somewhere no Commander would ever look.{/n} | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[7]` | {n}Of the transfer papers she said only that she had taken them back herself, and the Commander's purse with them, and returned the purse, which was more than the Commander had done.{/n} | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[8]` | {n}Whatever she took from the Commander's coat on the night of her price, she never said. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[9]` | {n}She and the Commander stayed what they had agreed to be over a drink: friends, with a door between them that neither ever locked.{/n} | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[10]` | {n}She did not come back after the night she was refused her price. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[11]` | {n}The relic-seller served two years in the Inheritor's cells. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.pickpocket` | `end.Paragraphs[12]` | {n}Crusade gold had bought the relic-seller's stones and his silence. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.papers` | `end` | {n}Seelah kept her transfer papers inside her tunic for the rest of the war, flat against her ribs. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.papers` | `end.Paragraphs[0]` | {n}The relic-seller told the story of the night the Commander of the crusade robbed him in every tavern in Drezen, for years, and never told it the same way twice. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.papers` | `end.Paragraphs[1]` | {n}Of the transfer papers she said only that they had come back to her, and that she now kept them somewhere no Commander would ever look.{/n} | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.papers` | `end.Paragraphs[2]` | {n}Of the transfer papers she said only that she had taken them back herself, and the Commander's purse with them, and returned the purse, which was more than the Commander had done.{/n} | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.papers` | `end.Paragraphs[3]` | {n}Whatever she took from the Commander's coat on the night of her price, she never said. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.papers` | `end.Paragraphs[4]` | {n}She and the Commander stayed what they had agreed to be over a drink: friends, with a door between them that neither ever locked.{/n} | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.papers` | `end.Paragraphs[5]` | {n}She did not come back after the night she was refused her price. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.papers` | `end.Paragraphs[6]` | {n}The relic-seller served two years in the Inheritor's cells. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.papers` | `end.Paragraphs[7]` | {n}Crusade gold had bought the relic-seller's stones and his silence. | H0/H1 context; thin | N |
| `seelah.trickster.epilogue.commit` | `end` | By morning she was late for muster. | H3 strong / join abrupt | E: `seelah.trickster.epilogue.commit.explicit.1` + N |
| `seelah.trickster.epilogue.refused` | `end` | {n}Seelah ran her relief company for many years. | H0/H1 loss/refusal; fit | N: history-specific; no living/sexual reward |
| `seelah.lastcall.page` | `page` | She kissed the Commander before finishing them. | H2 fit | N |
| `seelah.lastcall.page` | `page.Paragraphs[0]` | {n}At the rift the Commander had called in her promise, and she kept it. | H0/H1 context; thin | N |
| `seelah.lastcall.page` | `page.Paragraphs[1]` | {n}At the rift the Commander had called in her promise, and she kept it: she picked {mf\|his\|her} pocket the next evening in Drezen and took back what was hers, and would not say what el… | H0/H1 context; thin | N |
| `seelah.lastcall.page` | `page.Paragraphs[2]` | {n}The Commander was officially dead. | H0/H1 context; thin | N |
| `seelah.lastcall.page` | `page.Paragraphs[3]` | {n}It was Seelah who found the flask at the edge of the Wound. | H0/H1 context; thin | N |
| `seelah.trickster.dead.react_irabeth` | `start` | "You robbed a paladin's corpse, Commander. | H0 moral reaction; fit | P: preserve frank reaction; not a partner |
| `seelah.trickster.dead.react_irabeth_given` | `start` | "You robbed a paladin's corpse, Commander. | H0 moral reaction; fit | P: preserve frank reaction; not a partner |
| `seelah.trickster.dead.react_irabeth_taken` | `start` | "You robbed a paladin's corpse, Commander. | H0 moral reaction; fit | P: preserve frank reaction; not a partner |
| `seelah.trickster.dead.react_sosiel` | `start` | {n}Sosiel is sketching, and he does not stop.{/n} | H0 moral reaction; fit | P: preserve frank reaction; not a partner |
| `seelah.trickster.dead.react_sosiel_kept` | `start` | {n}Sosiel is sketching, and he does not stop.{/n} | H0 moral reaction; fit | P: preserve frank reaction; not a partner |
| `seelah.trickster.dead_no_unit.react_irabeth` | `start` | "A letter from your paladin came across my desk. | H0 moral reaction; fit | P: preserve frank reaction; not a partner |
| `seelah.trickster.dead_no_unit.react_sosiel` | `start` | "She wrote to me from the field chapel where they raised her. | H0 moral reaction; fit | P: preserve frank reaction; not a partner |
| `seelah.trickster.dismissed.react_irabeth` | `start` | {n}Irabeth's mouth twitches.{/n} | H0 moral reaction; fit | P: preserve frank reaction; not a partner |
| `seelah.trickster.dismissed.react_sosiel` | `start` | {n}Sosiel sets down his brush.{/n} | H0 moral reaction; fit | P: preserve frank reaction; not a partner |
| `seelah.abyss.night` | `start` | "And say what? | H0 context; fit | F |
| `seelah.abyss.night` | `listen` | Promise?" | H0 context; fit | F |
| `seelah.abyss.night` | `drill` | {n}Seelah stares at you, and then gives a tired laugh.{/n} | H0 context; fit | F |
| `seelah.abyss.night` | `halved` | You'll be up before the screaming starts, if it starts, and if it doesn't, you'll tell me so in the morning." | H0 context; fit | F |
| `seelah.letter` | `return` | {n}Back at the Nexus, Seelah unbuckles her sword belt and lays it down with unnecessary care.{/n} "Stand beside her. Get the letter. How did we make such a mess of that?" {n}You begin t… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_after` | `start` | {n}Seelah comes to find you empty-handed. She opens her mouth, shuts it, then plants her hands on her hips.{/n} "I had a fine speech ready. Made me sound very wise. Pity about that stal… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_after` | `public` | "I thought I'd scare him, she'd take the letter, and we'd be done. Except she has to go back to those stalls and ask for work. We don't." {n}She rubs her palms together, impatient with … | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_after` | `burned` | "Yes. And I nearly made you stop before I understood what you were doing." {n}She gives a short, unhappy laugh.{/n} "You were insulting an awning. I was furious with you for about three… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_after` | `admit` | "Next time, one of us keeps an eye on whoever asked for help. The other can make the grand speech." {n}Her mouth twists.{/n} "And give the speech-maker a good jab if they're getting car… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_after` | `assumed` | "Ugh. 'She'll thank me afterward.' I've said that too." {n}She grimaces and presses her palms against the stone.{/n} "If I start doing that again, stop me. In front of everyone, if you … | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_after` | `signal` | "Something better than looking at me while I am already marching past you." {n}She offers her wrist.{/n} "Here. Two taps. I'll stop and look. Try it before I get my sword out, eh?" {n}Y… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_after` | `trust` | "Then give me a signal! I saw you mocking an awning. I didn't see a plan." {n}She holds out her wrist.{/n} "Two taps when we can reach each other. Say my name when we can't. I'll look b… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_work` | `start` | {n}Seelah has news of the copyist. She found her again while passing through the city, bent over a page outside a shop that sells ink.{/n} "She wants someone to walk with her to a prosp… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_work` | `meeting` | {n}The copyist has wrapped her samples in a scrap of oilcloth. She hands the bundle to Seelah but keeps one page to check for smudges.{/n} {n}"You came," she says, looking at you. "Good… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_work` | `public` | {n}"Two people asked about my sister. One thought it was funny. I didn't get much work from him anyway."{/n} {n}She rubs at a spot on the oilcloth.{/n} {n}"I read the letter again last … | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_work` | `burned` | {n}"No one has said anything. I think we managed that much."{/n} {n}She folds the edge of the oilcloth inward.{/n} {n}"I wrote down the parts I remembered. There was a bit about a neigh… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_work` | `customer` | {n}The customer receives you in a cramped room lined with narrow drawers. She is a tiefling with a silver ring on each horn and a habit of tapping her nails while other people speak.{/n… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_work` | `person_seen` | {n}Seelah looks at you first. You glance toward the copyist. A pen is already in the woman's hand.{/n} {n}Seelah shifts her weight back onto both feet. The customer looks toward her. Se… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_work` | `her_choice` | {n}"There is more work here," Seelah begins, lifting the bundle. "You can see..."{/n} {n}The copyist holds out her hand without turning. Seelah stops. After a moment, she puts the bundl… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_work` | `bargain` | {n}"Here is the correction," the copyist says. "And here is the price. If you want cheaper work, I won't keep you."{/n} {n}She places the repaired page on the table. The customer studie… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_work` | `return` | "I was going to tell that woman exactly what I thought of her offer." {n}Seelah watches the copyist disappear into the street.{/n} "She probably knew. I have been told I am very easy to… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.letter_work` | `tease` | "I'll polish it on the way back. You can tell me where to put the swearing." {n}Her laugh comes more easily than it did during your last conversation. She takes your arm, then stops sho… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.platform_finished` | `outside` | {n}Outside the yard, she opens the packet and wraps the clean strip of cloth around her knuckle. You hold the end while she ties it.{/n} "Tomorrow I'm finding a quiet corner. Before I s… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.platform_finished` | `invited` | "Then come find me tomorrow. I know a quiet corner." {n}She catches your fingers before you let go of the bandage.{/n} "Thank you for today. All of it. Even the parts where you were rat… | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |
| `seelah.platform_finished` | `later` | "I will. And afterward I'd like to see you." {n}She catches your fingers before you let go of the bandage.{/n} "Tomorrow? We'll find something to do. I've issued enough marching orders … | H0/H1 context; fit | J: her affection survives the error; no sexual reward for errands |


### Scope exclusions checked

The other exported Seelah scenes are fate/seller transactions, dispatch/reply/arrival, instructional theft and early combat/pack help. They contain hands, bodies and touch in nonromantic contexts, not omitted sexual passages. `letter/return` and the later bandage invitations are included above because anger or work does lead back to the lover there. The source-only Seelah/Wenduag module explicitly contains data and proposed prerequisites, no implemented dialogue. Other women's reactions with Seelah in their IDs are outside this route and are not rewritten here. No purported partner-reaction nodes exist for Seelah; the nine existing Irabeth/Sosiel reactions are included as P rows. Every actual act-threshold node and every existing morning is listed separately, including all four legacy threshold twins.

### Exact brief exits and continuity joins

Each generated continuation must end with the following exact tagged line. On insertion, remove any duplicate bridge sentence from the surrounding *prose only*; preserve the original node, terminal choices, flags and downstream destinations. Defaults use the same continuous flow when no explicit take is supplied. Tagged output is intermediate material: translate N to `{n}…{/n}` and S to Seelah dialogue; it is never shipped with N:/S: prefixes. Do not put Commander dialogue in her node.

| Slot | Exact last line | Following existing material |
|---|---|---|
| `seelah.door.explicit.1` | N: The lamp survives, though neither of you reaches to put it out for a long while. | Original lamp/sleep aftermath and night terminal. |
| `seelah.late_afterglow.explicit.1` | N: From the workshop below, a hammer begins to strike. | Original dawn invitation, morning node, then plans. |
| `seelah.trickster.dismissed.commit.explicit.1` | N: At dawn, Seelah sits beside you and reaches for her boots. | Existing near/far boot-lacing morning; far still leaves at noon. |
| `seelah.trickster.dismissed.commit_visit.explicit.1` | N: Dawn catches Seelah reaching beneath the bed for one of her boots. | Existing near/far boot-lacing morning; far still leaves at noon. |
| `seelah.trickster.dismissed.second_ask.explicit.1` | N: In the pale light from the window, Seelah begins lacing her boots. | Existing near/far boot-lacing morning; far still leaves at noon. |
| `seelah.trickster.dismissed.second_ask_visit.explicit.1` | N: By dawn, Seelah has found your shirt and is looking for her boots. | Existing near/far boot-lacing morning; far still leaves at noon. |
| `seelah.trickster.epilogue.commit.explicit.1` | N: By morning, Seelah was searching beneath the Commander's coat for her missing boot. | Original boot-search, late muster and goodbye kiss. |


## Ordered round-2 implementation checklist — for the coordinator, not run here

1. Reconfirm the nine route modules/export against the fallback sheet's P/F findings and the latest integrated revision. The spec describes repairs not present in this checkout. Preserve every scene/node/relationship ID, choice index, GuidFor namespace, old answer target and old ending exit identity/mechanics. Append new answers/nodes; retire by gating only in the authorized implementation pass. Keep existing file BOM/CRLF/LF bytes. No rename or new relationship.
2. Resolve **current presence/loss** first (fallback P2–5): old returned state cannot override a later death, plot departure or deliberate condemnation. Verify native plot-loss binding `3b8ccafc1be912a4187350ac473cdc0e`, Q3 refusal `613485017b96c3840a2f9eea886deff1` and Demon confrontation `f41f2bfdf5135c249ba9494c13d23d8b` against the relevant action chain before implementation; these IDs are handoff leads, not newly certified citations. Shared lifecycle/household/Last Call consumers need coordinator ownership. No happy-path repair of a deliberately closed road.
3. Implement the **already identified custody/debt collection**, not a new romance design (P8–16/P22; F2–11): she successfully reclaims a kept list; ordinary no-loss/immediately-returned-list histories get no grievance. Cover `door`, `road` including short future, `late_afterglow`, outside-party commit/second ask and late epilogue siblings. Append neutral postponement/refusal to both `list_back` pages. First-coin refusal gets her actual paid first coin; freedom refusal gets her actual free return. Giving back property cannot force a kiss. Preserve any equivalent repairs already integrated.
4. Preserve the **existing return transaction** and its consequences (P25–29; F27–28): clean/caught seller results, DC15/25, concealment/arrest/purchase costs, Diamond/100 Favors rite, retained/effects payment siblings. Abort/retry must resume the acquired transaction without repeat spending/arrest. Native Iomedae romance closure is not a chapel-payment ban. This is the fallback's existing finding, not authorization to create a new religious rule or divine bargain. The registry-approved chapel rite stays.
5. Stage SP1/SP2 around the actual party, then the existing promise/supper branches: SEE-01 communal victory, SEE-03 bad cup/missed Jannah help, SEE-02 belt boast at the chosen sober night. Keep the drinking incident optional and single, no addiction label, attraction score, mandatory drink, forged order or new dawn gate. Future incident receipts, if needed, are route-local records of what occurred, not new access/commitment requirements. Jannah appears only in the native early situation, not every chapter where `promise` can run.
6. Implement SP3/SP4/SP5 as **acted closeness before future choice**. Keep open terms, quieter/changed-body options, morally real refusal and native friends' outcomes. SEE-04 is a conduct confrontation adapted to Elan's actual history, never an invented romantic triangle. Preserve ordinary 24h progression and the existing optional outings; do not turn them into new compulsory milestones. Remove only fabricated three-cold-suppers recall and atlas-0017's shared gesture. No echo or Shyka-inspired desire.
7. Insert the seven explicit-slot reservations and their defaults at the table's joins. Append slot nodes/paragraph IDs without deleting the legacy text nodes or their answers. If insertion changes a flow edge, leave old answer targets valid and preserve terminal effects on their original selectable continuation. Keep explicit slots out of quiet, kisses-only, changed-body, friend, grief and sacrifice histories. First sexual night is called first only once in the actual history; later takes are return/deepening. Slot replacement introduces **no** mechanic or gate. Use the JSON anatomy variants without assuming that gender determines equipment, body or acts.
8. Rework mornings and SP6 payoffs by **class**: door/bread aftermath; cooper night/dawn; four threshold near/far twins; postwar late morning; all living ending visits and Last Call prose. Put desire and physical memory back into the chosen-night mornings while preserving independent duty. The anonymous soldier knock follows the act, concerns muster, and never implements a partner interruption. Quiet histories retain affection without implying sex. Actual far-company leave remains travel, not a live-in default.
9. Preserve **ending and shared-reader truth** (P1/P6–7/P17–24; F12–18): company-only/friends are not romance; false breakup cause and unearned purse parcels need history-specific prose; list-game custody is voluntary after reclamation; current posting persists. A remembered Aeon ending uses the native memory evidence from the fallback (`a8b030ebca6c9744bac633cff609b698`; cue `edfd9fcb6bad3e94eb6765f79565fa13`) only after coordinator verification, retaining both legacy exits. Last Call keeps its already strong returning-lover opening, qualifies its vow/custody paragraphs, collects the list rather than an unidentified coin, and preserves flask effects. Living postwar scenes require a living/actually returned Commander. Narrow native dialogue/slide overrides must follow the authored Trickster change and be inert elsewhere.
10. Coordinator's later acceptance review should walk real retained/effects/dismissal histories, including paid return and travel, custody give/keep/reclaim/play, taught/untaught lift, every refusal/retry, current later loss, friend/company-only/full/short/changed-body histories, actual near/far leave, sacrifice/Last Call and off-Trickster native fate. Check every page retains a selectable answer and no old ending exit loses identity or mechanics. Compare each of the 421 inventory addresses after the rewrite; account for every slot default/exact exit. This planning job does **not** run expansion, tests, verifier, rules validation, builds, harness or game.

## Binding audit and escalation boundary

- **(1)–(2):** intentional player kill/condemnation and matrix user decisions stand. No undo is created by a romance scene.
- **(3):** resurrection, physical arrival and later current loss stay distinct. Dispatch/paid letter is not arrival; old return is not perpetual life. An unreturned fatal Commander sacrifice gets bereavement only.
- **(4):** canon-altering rite/return and all dependent native rewrites remain Trickster-only. Seelah remains a paladin who refuses cruelty; evil household women retain their evil motives/methods. Adult appetite is shown in her own choices and physical initiative.
- **(5):** the existing discoverable gate/lock-in histories remain legitimate. No new attraction, cost, commitment, reconciliation or universal happy-path access is proposed. Explicit slots never earn affection or erase unpaid terms.
- **Foresight:** Seelah has no allocated echo. No new echo, vision, alternate-life rationale or magic consent. Shyka's paid page remains fate-only; even a qualified fate outcome needs its actual device and her choice.
- **DLC tier:** all new party/morning staging, anonymous duty knock, room continuation and reclamation dialogue are labeled authored. They extend her native war, friends, thief competence and paladin guilt at existing campaign scale. Any native mourning/dialogue/slide rendered false by an earned Trickster return needs a narrow coordinator override, keeping IDs and original canon elsewhere. No Acemi return is proposed.

**ESCALATE:** every runtime implementation target is outside this planning allow list: `storylines/seelah*.py`, native binding/lifecycle support, presence/locator and courier reachability, `development/Story.json`, shared `household.py`, `lastcall*.py`, `trickster_world.py`, shared ledger/journal, tests and registry. Do not edit them in this job. Refresh the stale requested remote ref separately. The Seelah/Wenduag data-only sheet does not authorize adding pair scenes here. Her spec's authored labels must be updated by its owner when implementation occurs.

**PROPOSE (not implemented):** none beyond the task-required authored set pieces, heat/debt repairs and future checklist above. No blackmail layer, new intimacy scoring, partner, return device, extra gate or new household mechanic.

**RISKS:** current-loss and late-romance readers remain runtime issues until the coordinator repairs/verifies them; stale export/spec/ref differences must be resolved before treating absent fixes as present. Explicit output needs continuity/voice/anatomy review and can be omitted safely because every slot has a complete heated default. Seven entry variants are not seven required encounters. No independent >=91 score, game behavior or gate pass is claimed for this planning artifact.

**GATE / COMMIT:** not run. The task's specific HARD RULE says planning only, read/write only, no expansion/builds/tests/gates on the shared machine; it conflicts with the generic quick-gate footer. The final 'Do not git commit' instruction conflicts with the earlier 'Commit' and is followed. Only document/source reads and allowed planning-file writes were performed. No temporary folders, obj/bin, generated build products or audit files were created inside or outside the repository.

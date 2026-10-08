"""Hepzamirah: cloud voice-owner pass (villain-route-hepzamirah, design-first).

A late text-only layer. It runs after every harem row and household pair has
assembled her scenes (rows are discovered in name order, so this module runs
after the contract controller and after zzz_minachiv_pairs). It changes no
scene, node or choice id, choice position, Next, Set, gate, check, cost or
GuidFor. New paragraphs are read-only consumers of flags the route already
produces, appended after every existing paragraph of their node. Every target
must resolve, or the build fails.

Review and machine truth table: tools/route_packs/redesign/hepzamirah/.

Structure fixed here:
  * body.hounds was staged as a gate guard's note that she had written on
    (wrong medium), while the next nodes put the Commander at the gate in
    person; it is now one face-to-face scene at the gate;
  * courier_killed: the kill was only ever reported; body.terms and her room
    now show what she kept of the Apprentice;
  * body.terms/refused left Ember's jar of wildflowers in every refusal, with or
    without Ember; the jar now needs ember_messenger;
  * flesh.apostate/door_gate read rent_taken, which both "hang it over the east
    gate" and "bury it quietly" set; the line now holds for both;
  * promises and costs set and never read (cost.discreet, court_defied,
    eve_promise, weapon_vow, treaty_signed, renamed_herself, cost.horned_scar,
    gift_worn, market_strike) gain epilogue readers;
  * the household-pair receipts on her Last Call page were the Commander's
    first-person ledger lines inside a narrated page (wrong speaker, paperwork);
    they are narrated, and her own reactions are in her voice;
  * the horzalah_hepzamirah pair (truce, retry) and the sisters' docket
    j05 node were [PROSE PENDING] placeholders; voiced from the approved beats.

Canon used (enGB keys, see the review): 3dce2b36, 84523473, 3caba7e8, 842890df,
7de8d1a8, aa6fc172, cbb103a6, 8f337ada, a68b28c8, 10989135.
"""
from story_format import p

H = "hepzamirah.trickster."
PENDING = "[PROSE PENDING:"

NODES = {}        # (scene, node) -> new text for a written node
PLACEHOLDERS = {}  # (scene, node) -> text for a [PROSE PENDING] node
PARAS = {}        # (scene, node) -> new paragraphs, appended
PARA_TEXT = {}    # (scene, node, paragraph Id or index, required flag) -> new text


def text(scene, node, body):
    NODES[(scene, node)] = body


def add(scene, node, *paras):
    PARAS.setdefault((scene, node), []).extend(paras)


def when(flags, body, forbids=()):
    flags = (flags,) if isinstance(flags, str) else tuple(flags)
    return p(body, requires=flags, forbids=forbids)


# ---------------------------------------------------------------------------
# body.hounds: one scene at the gate, not a note with her line scrawled on it.
# ---------------------------------------------------------------------------
S = H + "body.hounds"
text(S, "door", '''{n}The gate guard does not send a note; the guard comes to your door in person, white to the lips. A cambion with acid-scarred hands asked at the gate for "the Commander's small debt to my master", and the horned woman from the smith's yard came out to meet the cambion before anyone could send for you.
The guard did not stay to watch. You can hear it from here.{/n}''')
text(S, "sister_at_gate", "{n}You go down to the gate. The guard does not follow you.{/n}")
text(S, "throat", '''{n}She has the Apprentice pinned to the gatepost by the throat, his boots a hand's breadth off the mud, and she does not look round when you come.{/n}
"Your postman came back, clown. He says he is owed a vial of you. He says his master will know if it is not your blood." {n}She leans in until her broken horn grazes his cheek.{/n} "I say his master will know nothing, because I am going to post his master this one's eyes, one at a time, in a box with a ribbon. Tell him, worm. Tell the Commander how much you enjoyed carrying me in a crate."''')
text(S, "joke", '''"Unless you have a better joke. You usually do." {n}The Apprentice's heels drum once on the gatepost.{/n} "Tell it now, before I get bored. I get bored quickly now. Flesh itches."''')
text(S, "vial", '''{n}She drops the Apprentice into the mud and plants her boot on his calf. She holds out her hand for the lancet without looking at you, and when you give her your arm instead she takes that too.
She draws it herself. She is not gentle, and she is not clumsy either: one cut inside the elbow, exactly deep enough, her thumb pressing the vein to make it run faster, and she watches the vial fill the way a moneylender watches a scale settle. It takes longer than you expect. By the end the gate is swaying slightly and your mouth is dry.{/n}
"Understand what you have paid, clown. He does not want this to drink. He wants to grow things from it." {n}She corks the vial with her teeth, spits the wax, and drops it into the Apprentice's scarred hands.{/n} "Somewhere in his cave there will be a jar with a little of you in it, and you will never know what it is becoming. Now you have my reason to want him dead. Good. I like company."''')

# ---------------------------------------------------------------------------
# body.terms: the courier's death on screen; the refusal earns its props.
# ---------------------------------------------------------------------------
S = H + "body.terms"
add(S, "open", when(H + "cost.courier_killed",
    "{n}Over her door, nailed through the palms, hang two acid-scarred hands. The smith has stopped looking up at them.{/n}"))
text(S, "killed", '''"His eyes went to Mutasafen in a box with a ribbon, as I promised him while he could still watch me promise it. He screamed for the first one. For the second he only wept, which was more useful. It washed the box."
{n}She glances up at the hands over her door.{/n} "Those I kept. They carried me here in a crate; now they can hold my door. I lie awake wondering which of his master's bodies opened the box. It is the best sleep I have had."''')
text(S, "refused", '''"I knelt once, to a father who promised me everything. I will not do it for a jailer with good manners."
{n}She walks out of the yard without a glance at anyone. By morning her door stands open and her room is empty. The pick is gone, and so is the smith's best hammer.{/n}''')
add(S, "refused", when(H + "ember_messenger",
    "{n}In the middle of the floor she has left Ember's jar of wildflowers, unbroken.{/n}"))

# ---------------------------------------------------------------------------
# flesh.apostate: rent_taken is set by the public gate and by the quiet burial.
# ---------------------------------------------------------------------------
text(H + "flesh.apostate", "door_gate",
     '"The cellar did its work. Whatever your crusaders were told, Father\'s people know whose hand it was. They always know a sacrifice when they smell one. Good. I wanted *them* to know."')

# ---------------------------------------------------------------------------
# her_room: what she kept of the courier.
# ---------------------------------------------------------------------------
add(H + "bond.her_room", "keeps", when(H + "cost.courier_killed",
    '{n}The Apprentice\'s hands have come in off the door. They hang from the bedpost now, dried to leather, fingers curled.{/n} "He carried me here," {n}she says, when she sees you look.{/n} "Now he holds my coat."'))

# ---------------------------------------------------------------------------
# Paperwork standing in for consequence: show it, keep the cost.
# ---------------------------------------------------------------------------
text(H + "flesh.chaplains", "embassy",
     '''{n}The eldest chaplain refuses to bow. An embassy needs a foreign power, he says, and a name over a bedroom binds no court in Nerosyan. Your word binds Drezen, though, and every guard in the yard heard it; for a week you will spend favours making it hold.{/n}
{n}Hepzamirah takes the petition out of the chaplain's hand before he can roll it up. He goes to protest to the court, and watches her all the way to the gate.{/n}''')
text(H + "bond.nerosyan", "embassy_reply",
     '''{n}The clerk writes it down. It will reach Nerosyan as your order and nothing more: the court has agreed to nothing, and the levies will still be late. He backs out of the yard with the letter under his arm and does not turn round until the gate.{/n}
"A matter of state." {n}She bares her teeth at his back.{/n} "You made them write down whose bed I use. Now they can argue over it in council. Your treasury buys the missing spears; your name keeps my door open. Do not pretend the sign does it."''')
S = H + "flesh.drill_result"
text(S, "field", '''{n}On the seventh morning the sergeant brings you down to watch. Hepzamirah raises the haft, and across the yard the line braces before she has moved a step, without waiting for a prayer. Behind them, on the infirmary benches, sit the ones who did not learn fast enough.{/n}''')
text(S, "harsh", '''{n}She charges them once more, for you. Most of the line holds. Two men do not, and she goes through them like a door; the sound their knees make carries to the citadel, and the sergeant drags them clear by the collars.{/n}
"These held. Those broke, and good riddance; they would have broken at the Threshold with a demon's teeth in them." {n}She wipes the spike on the nearer one's tabard.{/n} "You told me my way, whelp. Here is what it cost you, and what it bought."''')

# ---------------------------------------------------------------------------
# Epilogue readers for promises and costs nothing read.
# ---------------------------------------------------------------------------
S = H + "epilogue.leavable"
add(S, "page",
    when(H + "cost.discreet", "{n}The Commander had bought the court's levies with her discretion. She kept the bargain to the letter until the Threshold and not one hour past it. The morning after the victory she broke the new cot where the east wall could hear, and when the chaplains came to complain she told them the price had been paid in full.{/n}"),
    when(H + "court_defied", "{n}Nerosyan's levies came late and thin, as the court had promised. She kept the clerk's letter in the pocket over her heart and read it aloud at the victory feast, one sentence to each lord who had held back his spears, so that every one of them knew she had the list.{/n}"),
    when(H + "eve_promise", "{n}The Commander had sworn to come for her if the Threshold put her back in her father's prison. She never had to collect, and held it over the Commander anyway, as a debt that had simply not yet fallen due.{/n}"),
    when(H + "weapon_vow", "{n}No bench of Mutasafen's ever held the Commander. Every one of those benches she found, she took apart, and she painted a milk-white eye on what was left so that the alchemist would know whose vow it was.{/n}"),
    when(H + "treaty_signed", "{n}The treaty of the Embassy of the Leavable Prison hung over the cot, signed in forge-ash. Nerosyan never recognised it. She enforced the seventh article herself, to the letter, and twice to the Commander's cost.{/n}"),
    when(H + "renamed_herself", "{n}She answered to \"the one who left\" from the Commander's mouth and nobody else's. The one sergeant who tried it lost two teeth.{/n}"),
    when(H + "cost.horned_scar", "{n}The horned mark cut into the Commander's forearm on her father's altar never faded. She liked to trace it with a thumbnail in front of guests, slowly, until they looked away.{/n}"),
    when((H + "gift_worn", H + "horn_cut"), "{n}The Commander wore her horn knife on its thong to the end of the war and after. When she wanted the Commander's mouth, she pulled on it like a leash.{/n}"),
    when(H + "gift_worn", "{n}The Commander wore her father's hornless iron head on its cut chain to the end of the war and after. His priests spat when they saw it. When she wanted the Commander's mouth, she pulled on the chain like a leash.{/n}", forbids=(H + "horn_cut",)),
    when(H + "market_strike", "{n}The laundresses of Drezen never washed a shirt of hers again. She wore them filthy, and made a point of standing upwind of the chaplains.{/n}"),
    # household.pair.horzalah_hepzamirah outcomes had no reader anywhere.
    when(("household.pair.horzalah_hepzamirah.hepzamirah_terms_kept", "household.pair.horzalah_hepzamirah.horzalah_terms_kept"),
         "{n}Once, for twenty lances, she had let her sister's courier walk past her door with his tongue in his head. She never did it again, and Horzalah never asked her to.{/n}"),
    when("household.pair.horzalah_hepzamirah.hepzamirah_term_broken",
         "{n}She never apologised to Horzalah for the courier she crippled behind the north gate. Whenever the sisters sat at the same table, the Guild's people found reasons to leave the room first.{/n}"),
    when("household.pair.horzalah_hepzamirah.horzalah_term_broken",
         "{n}Horzalah had sold the patrol's warning out from under her. Hepzamirah counted the lances that did not come back out of the third ravine, and said the number aloud whenever her sister sat down at the same table.{/n}"),
)
S = H + "epilogue.leavable_on_record"
add(S, "page",
    when(H + "eve_promise", "{n}The Commander had sworn to steal her out of her father's prison a second time if she died. It was the Commander who died. She cursed the oath for being the wrong way round, and kept the only part of it left to keep: nobody spoke the Commander's name in her hearing without paying for it.{/n}"),
    when(H + "treaty_signed", "{n}She took the treaty of the Embassy with her and nothing else of the Commander's. The seventh article she had cut out with her thumbnail and burned on the day of the funeral.{/n}"),
)

# Flat closers on the commitment epilogue (same gates, same indices).
S = H + "epilogue.leavable"
PARA_TEXT[(S, "page", 10, H + "call_forbidden")] = "{n}She never forgave the forbidding of the call in Drezen. She made the Commander stand before the court and say that the city had been protected, not her quarry confiscated, and then she chose her ground outside the walls. Baphomet had not answered yet. When he did, it would be on her day, not the crusade's.{/n}"
PARA_TEXT[(S, "page", 11, H + "call_sworn")] = "{n}The Commander had sworn to stand where the Lord of Beasts could see when she made the call. She had not made it yet. She reminded the Commander of the oath at odd hours, usually in bed, usually with one hand closed round a throat that was not hers.{/n}"
PARA_TEXT[(S, "page", 12, H + "vorlesh_first")] = "{n}She had been promised Vorlesh's first sight at the inner door, and the crusade never gave her the passage. She came home from the outer fighting black to the elbows, planted her pick beside the cot, and made the Commander tell her, word for word, how the witch had looked at the end. Then she demanded it again. The promise stayed on her list of debts.{/n}"
PARA_TEXT[(S, "page", 13, H + "bond.vorlesh")] = "{n}They had sworn to go through Vorlesh's door side by side, and the crusade gave her no passage into that chamber. She made the Commander tell her what the witch had said. \"Half a step in front,\" she said afterwards. \"You still owe me that, clown.\"{/n}"
PARA_TEXT[(S, "page", 14, H + "bond.scouts_result")] = "{n}At the final march the watches and the pikes were set to her warning about the ground. She walked the line herself before she took her place in front, and kicked every pike that still pointed at the sky.{/n}"
PARA_TEXT[(S, "page", 15, H + "bond.map_table")] = "{n}The generals had refused her warning, and nobody surveyed the broken ground for them. She watched it herself from the first rank, and never once said she had told them so. She did not need to.{/n}"
PARA_TEXT[(S, "page", 16, H + "drilled_troops")] = "{n}The march cut her training week short. She handed the regiment back to its sergeants with the mornings still owed, and told them which of their men she would have broken, so they would know whom to watch.{/n}"
S = H + "epilogue.leavable_on_record"
PARA_TEXT[(S, "page", 1, H + "call_forbidden")] = "{n}She chose ground outside Drezen for the call the Commander had forbidden. The one who owed her a public apology for it was dead, and she counted that among the things the Threshold had stolen from her.{/n}"

# ---------------------------------------------------------------------------
# Last Call page: the household-pair receipts, narrated and in her voice.
# Each living/returned pair of paragraphs keeps its Id, gates and position.
# ---------------------------------------------------------------------------
LASTCALL = "hepzamirah.lastcall.page"
PAIR_LINES = {
    "household.pair.melazmera_hepzamirah.reader.lastcall.hepzamirah.": {
        "resolved": 'Hepzamirah called her guards back to her door the day the second wagon passed. "Two loads. That was the price. If the dragon wants a third, she can come and ask me with her mouth full."',
        "failed": 'Hepzamirah never let the lost cart go. "You fed my stores to her prowlers, clown, and called it a trick. Pay it back or bleed it back. I am not choosy which."',
        "repaired": 'Hepzamirah went through the replacement cart sack by sack, in front of the Commander, and found it one short. "Close. I will take the rest out of you tonight."',
        "open.declined": 'Hepzamirah kept both guards at her door and let the dragon keep her ridge. "Let her eat someone else\'s servants. Mine are paid for."',
        "diversion.declined": 'Hepzamirah scraped the ridge mark off the cart with her thumbnail. "Prisoners. You would fatten her on my road and call it strategy, worm."',
        "replacement.declined": 'Hepzamirah never lent the Commander a guard again. "You broke your word over a cart of meat. I have killed men for less. I am letting you keep the lesson."',
        "cost.commander_rear_wagon": "The Commander had ridden the last wagon, the one the prowlers smelled first, because Hepzamirah would not risk her own men on it.",
        "cost.commander_watch_kept": "The Commander had kept the exposed rear watch on the low road all night, and the dragon had watched every step of it.",
        "cost.commander_shipment_lost": "The Commander's false trail had fed a cart of her meat to the prowlers. She brought it up every time the Commander had a clever idea.",
        "cost.replacement_carried": "The Commander had paid 400 Finances for the replacement and hauled the sacks by hand, while Hepzamirah watched from her door and did not lift one.",
        "cost.outriders_paid": "The outriders had cost the crusade 300 Finances and the Commander's own reserved stores.",
        "cost.melazmera_hunt_yielded": "Melazmera had given up her hunting approach for exactly two passages, and not one wagon more.",
        "cost.hepzamirah_guards_detoured": "For those passages Hepzamirah sent both her hired guards down the long road, and slept with her door unguarded and the pick across her knees.",
    },
    "household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.": {
        "resolved": 'Hepzamirah mentioned the temple only once more. "I gave up that village. I have others. Keep your huntress out of my yard, clown, or her bow goes over my door."',
        "known.present_claim": 'Hepzamirah kept her captain, and his claim with him. "You left it standing. If the huntress wants an apology, she can take it off his corpse."',
        "cost.delamere_stone_received": "Delamere had given up a hunt to guard the returned temple stone until its pilgrim came for it.",
        "cost.delamere_stores_guarded": "Delamere had counted the replacement stores herself and guarded them with her bow strung.",
        "cost.delamere_goods_received": "Delamere had counted the returned shirts and spears herself and guarded them until they went home.",
        "cost.hepzamirah_captain_dismissed": "Hepzamirah had thrown out a trained captain, and the shirts and spears he stole for her, rather than let him sell her name.",
        "cost.hepzamirah_guard_claim_yielded": "Hepzamirah had given up the temple as a well for her guard, and nailed the cancelled claim where her men could see what it cost to promise in her name.",
        "cost.commander_prize_yielded": "The Commander had cancelled the scouts' allocation and put both mail shirts and all six spears into Delamere's hands for the temple.",
        "cost.commander_stores_replaced": "The Commander had paid 150 Materials to replace the temple's stores.",
    },
}
for prefix, lines in PAIR_LINES.items():
    for key, body in lines.items():
        for twin in ("living", "returned"):
            PARA_TEXT[(LASTCALL, "page", prefix + key + "." + twin, None)] = "{n}" + body + "{/n}"

# ---------------------------------------------------------------------------
# Pair placeholders: household.pair.horzalah_hepzamirah (truce, retry) and
# the sisters' docket. Approved beats (claude-work-queue, rulings 4 and 05).
# ---------------------------------------------------------------------------
TRUCE = {
    "start": '''{n}Horzalah lays a knife on the table between the cups, point toward her sister.{/n}
"One of my Guild's people came up from the lower city last night with something worth money. A patrol rides out of the north gate at dawn, twenty lances, to sweep the ravines. Something is waiting in the third ravine that is not on your maps. My man knows what, and how many, and he knows three buyers in Alushinyrra who would pay me in souls to let those lances ride into it."
{n}She smiles, thin as a cut.{/n} "I am going to give it away. Once. To your patrol, so that this house remembers who handed twenty lances back alive. I will feel that sale go like a pulled tooth."
"One condition, and it is hers." {n}She does not look at Hepzamirah.{/n} "My man walks to the gate and back with his throat whole. My sister has a habit with couriers."''',
    "second": '''{n}Hepzamirah turns the knife on the table with one finger until the point faces Horzalah.{/n}
"A Guild rat carrying a warning through my city, past my door, and I am to let him by with his tongue still in his head." {n}Her lip peels back from jagged teeth.{/n} "I had spies in Colyphyr's tunnels before your little Guild had a name, sister. I could have his warning out of him by noon, and the buyers, and the price, and you would have sold nothing at all."
"Fine. Let your rat run. One warning, this once, and it is yours. I want twenty lances alive behind me at the Threshold more than I want to watch you lose. Barely." {n}She drains her cup.{/n} "Carry it, clown, before I change my mind."''',
    "held": '''{n}At dawn the Guild man walks to the north gate under Hepzamirah's eye. She stands in his road with the pick on her shoulder until he has to step round her, close enough for her to smell his fear, and then she lets him by. The patrol captain hears him out, goes white, and leads his twenty lances round the third ravine instead of into it. That night the scouts find what was waiting there: a nest of Deskari's spawn, gorged and asleep. They burn it.{/n}
"Your rat kept his tongue and your lances kept their skins," {n}Hepzamirah tells her sister at the table.{/n} "Say it. You lost a sale."
"I lost a sale," {n}Horzalah says.{/n} "And you let a courier walk past you. Say that."
{n}Hepzamirah drinks first.{/n} "I let a courier walk past me. It tasted like piss."''',
    "missed": '''"You sent my man to the wrong gate." {n}Horzalah does not raise her voice. The knife comes an inch off the table.{/n}
"He waited at the east gate until the patrol had ridden out of the north one. They found the third ravine without him. Four lances came back." {n}She looks at her sister.{/n} "And you never had to break your word, because the Commander broke it for both of us. Nothing kept, nothing given. I still lost the sale."''',
    "refused": '''"Then it stays mine." {n}Horzalah slides her knife back into her sleeve.{/n}
"My man goes back down to the lower city with his warning, and by tomorrow it belongs to whoever pays. If your lances ride into the third ravine, Commander, you can tell their widows you did not care to choose."
{n}Hepzamirah laughs once, without any humour in it.{/n} "At last. A sister I recognise."''',
    "broken_horzalah": '''{n}Horzalah's man never reaches the north gate. He reaches a tavern in the lower city instead, where a cambion with a heavy purse has been waiting since midnight.{/n}
"I counted the souls they offered," {n}Horzalah says afterwards, without a flicker of apology,{/n} "and I counted twenty lances, and the souls were heavier. I am Baphomet's daughter too. Did you forget?"
{n}The patrol rides into the third ravine at dawn. Fewer come back. Hepzamirah hears the count at the table and grins at her sister as if she had been paid.{/n}''',
    "broken_hepzamirah": '''{n}Hepzamirah is waiting in the alley behind the north gate. The Guild man never sees the pick; he only feels the haft across his knees, and then her fist in his hair.{/n}
"The warning," {n}she says, almost pleasantly.{/n} "Then the buyers. Then the price. Then I will decide which of your fingers you need to hold a cup."
{n}She carries the warning to the patrol captain herself, so that twenty lances ride out owing her and not her sister. The Guild man crawls back to the lower city on his elbows.{/n} "Tell my sister I intercept couriers," {n}Hepzamirah says at the table.{/n} "She told you so herself."''',
}
TRUCE_RETRY_START = '''{n}Horzalah's man is back up from the lower city, and her knife is back on the table, point toward her sister.{/n}
"Another patrol, another ravine, another buyer in Alushinyrra asking my price. Same terms: I give the warning away, once more, and she lets my courier walk." {n}Her eyes come round to you.{/n} "Carry it properly this time, Commander, or I start carrying things myself."'''
for scene in ("household.pair.horzalah_hepzamirah.truce", "household.pair.horzalah_hepzamirah.retry"):
    for node, body in TRUCE.items():
        PLACEHOLDERS[(scene, node)] = body
PLACEHOLDERS[("household.pair.horzalah_hepzamirah.retry", "start")] = TRUCE_RETRY_START

DOCKET_J05 = '''{n}Horzalah takes the bundle of her sister's trap instructions and reads every sheet under the lamp, slowly, one nail following each line: the bait, the false summons, the ward on the cell door in the Ivory Labyrinth, the hour the lock would close. Twice she stops, and the old collar scar on her throat moves as she swallows.{/n}
"So that is how she did it. Neat. She always was neat with a lock." {n}She feeds the sheets to the lamp one at a time and watches each curl to ash before she lets go of the next.{/n}
"Now nobody uses this on me again. That is all this bought, Commander. It buys her no pardon. Her name stays on the account; I have only made sure she cannot write it there twice."'''
for scene in ("household.docket.horzalah_hepzamirah.account", "household.docket.horzalah_hepzamirah.account_table"):
    PLACEHOLDERS[(scene, "j05_instructions_destroyed")] = DOCKET_J05

# ---------------------------------------------------------------------------
# household.pair.melazmera_hepzamirah: her side of the convoy dispute, at her
# register (the dragon's lines are Melazmera's and stay as they are).
# ---------------------------------------------------------------------------
S = "household.pair.melazmera_hepzamirah.open"
text(S, "start", '''{n}A wagon of meat waits outside Drezen's stockyard. Beyond the walls, demons still hunt the roads. Melazmera stands beside it in her folded woman-form, one grey nail sunk into the canvas. Hepzamirah's two hired guards keep their hands on their weapons.{/n}
"Your men walk over my supper, little princess," {n}Melazmera says, giggling.{/n} "The ridge leads to my hoard. Shall I leave a few bones to mark it?"
"Then eat farther up the hill, you overgrown lizard. Those two are paid for, and what I pay for stays mine." {n}Hepzamirah rips the canvas free of the nail.{/n} "If my guards walk the low road with the meat, my door stands open to every cultist in this city. So who guards it? You?"
"Send the Commander. The last wagon smells best."''')
text(S, "prepared", '''"You take the rear, clown. If something follows, it meets you before it reaches my men."
{n}She marks the low road on the wagon's side with a stub of charcoal, hard enough to snap it. Melazmera scratches a second line toward an abandoned lime pit.{/n}
"The prowlers follow cattle blood. Give them something to sniff, thief. I will watch the ridge."
"And I will give my guards the order," {n}Hepzamirah says,{/n} "after I have seen the road cleared. Not one heartbeat before."
{n}The last wagon has no covered seat. Its driver makes room for you among the sacks.{/n}''')
S = "household.pair.melazmera_hepzamirah.diversion"
text(S, "lost", '''{n}The hide crosses a fresh track you failed to notice. The prowlers come up behind the wagons. You cut a meat cart loose to draw them off; the driver gets clear, and the load vanishes under claws.{/n}
"You led them straight to it!" {n}Hepzamirah drives her pick into the roadside earth so hard the haft shudders.{/n} "Her approach untouched, my stores in their bellies, and you call this a diversion, you useless worm?"
"I called it supper," {n}Melazmera says. Her giggle stops when Hepzamirah turns on her.{/n}
"Keep your teeth off my guards, lizard. Commander, you promised me meat. Carry it yourself. My men stay with me."''')

# ---------------------------------------------------------------------------


def _node(by_id, sid, nid):
    if sid not in by_id:
        raise KeyError("hepzamirah cloud: scene %s missing" % sid)
    matches = [node for node in by_id[sid]["Nodes"] if node["Id"] == nid]
    if len(matches) != 1:
        raise KeyError("hepzamirah cloud: %s/%s matched %d nodes" % (sid, nid, len(matches)))
    return matches[0]


def register(payload, scenes, refs):
    by_id = {body["Id"]: body for body in payload["Scenes"]}
    for (sid, nid), body in PLACEHOLDERS.items():
        node = _node(by_id, sid, nid)
        if not node["Text"].startswith(PENDING):
            raise ValueError("hepzamirah cloud: %s/%s is no longer a placeholder" % (sid, nid))
        node["Text"] = body.strip()
    for (sid, nid), body in NODES.items():
        node = _node(by_id, sid, nid)
        if node["Text"].startswith(PENDING):
            raise ValueError("hepzamirah cloud: %s/%s is a placeholder" % (sid, nid))
        node["Text"] = body.strip()
    for (sid, nid, key, flag), body in PARA_TEXT.items():
        paras = _node(by_id, sid, nid).get("Paragraphs") or []
        if isinstance(key, int):
            if key >= len(paras) or (flag and flag not in paras[key]["Requires"]):
                raise KeyError("hepzamirah cloud: %s/%s paragraph %d does not read %s" % (sid, nid, key, flag))
            paras[key]["Text"] = body.strip()
        else:
            hits = [para for para in paras if para.get("Id") == key]
            if len(hits) != 1:
                raise KeyError("hepzamirah cloud: %s/%s paragraph %s matched %d" % (sid, nid, key, len(hits)))
            hits[0]["Text"] = body.strip()
            # Last Call partner readers are re-merged by text after each row;
            # keep the registry in step so the old wording is not appended again.
            from storylines import lastcall_partners
            for partner in lastcall_partners.PARTNERS:
                for para in partner["paragraphs"]:
                    if para.get("Id") == key:
                        para["Text"] = body.strip()
    for (sid, nid), extra in PARAS.items():
        _node(by_id, sid, nid).setdefault("Paragraphs", []).extend(dict(para) for para in extra)

"""Claude voice for the J03 pair placeholders this route owns (rulings 18 and 19).

CLOUD-QUEUE shared-scene rule: villain-route-minachiv sits above hepzamirah and
herrax, so it voices household.pair.hepzamirah_minagho.* and
household.pair.herrax_chivarro.{turf.history,turf.live,retry}. Text only, after
z_j03_contracts and the contract controller: no node, choice, flag or gate
changes, and no paragraphs (J03 rows carry none). Every beat below is the
approved claude-work-queue beat for that node.
"""

HEP = "household.pair.hepzamirah_minagho."
TURF = "household.pair.herrax_chivarro."

COLLECTOR = {
    "start": '''{n}Minagho drops into the chair across from Hepzamirah without being asked and puts a hoof up on the table between the cups.{/n}
"There's a collector in the lower town asking after both of us, horns. One of your father's. Nose like a bloodhound, a brand-reader's seal on his wrist, and three hired throats who think they're going to get paid." {n}She grins, all teeth.{/n} "I can screen him. Wear a face, walk him in a circle until he's standing where I want him, looking the wrong way. That part's mine, and I'm putting my own face on it, so if it goes wrong the whole Abyss hears that Minagho botched another one. You know how I love that."
"The other part needs someone who can break a demon's back with her hands. I hate that it's you. Do it, keep your mouth shut afterward, and when anyone asks who killed him, the answer is me."''',
    "second": '''{n}Hepzamirah lowers her horns an inch, the way a bull does before it decides.{/n}
"You want me to do the killing and let a failed general wear it, like a camp whore wearing a dead woman's jewels?" {n}She bares her jagged teeth.{/n} "My father's dog, sniffing after me as if I were still his property. Fine. I'll take his spine out through his belly, and I'll hand you the credit, you eyeless scrap of meat, because the look on your face while you swallow it will be worth more than any boast. Screen him well, wench. If he sees me coming, I'll break you next."''',
    "held": '''{n}It goes the way Minagho said it would, which nobody at the table enjoys admitting. Mina's blonde face leads the collector down the wrong alley, giggling, three steps ahead of his hired men, and he follows his nose straight into the dark where Hepzamirah is waiting.
She doesn't use a weapon. She takes him by the head and the hip and folds him backward over her knee until something in the middle of him gives with a sound like green wood. The hired men run. She lets them; they will tell the story wrong, which is the point.
Back at the table she wipes her hands on the cloth and drops the brand-reader's seal in front of Minagho, still on the wrist.{/n}
"Yours, general. You killed him. Say it, so I can hear what it costs you."
{n}"I killed him," Minagho says, and her mouth twists.{/n}
"Louder, worm."''',
    "missed": '''"You call that a relay, Golarian?" {n}Minagho flings her cup at the wall.{/n} "I had him turned round in the alley, and you sent her to the wrong fucking street. He's gone, and he's smelled all three of us now. No screen, no strike, no corpse. Just a collector with a story about the Commander's tavern."
{n}She jabs a claw at Hepzamirah.{/n} "And don't you look at me like that, horns. You didn't hit anything either."''',
    "refused": '''"Claim my own victories?" {n}Minagho laughs, too high.{/n} "Darling, that's all I've ever done, and look where it got me: a brand and a sore head. Fine. Let her play the hero in the lower town on her own. When the collector puts his hook through her, I'll be at this table, drinking, telling everyone I warned her."
{n}Hepzamirah says something in Abyssal about Minagho's mother. Nothing is agreed.{/n}''',
    "broken_minagho": '''{n}Minagho is late, because Minagho stopped to enjoy herself. She wanted the collector to see her own face on the way down, so he would know whose trick it was, and he did: one look, and he went straight past the glamour and up the right street toward the tavern, with his hook out.
Hepzamirah waits in the dark for an opening that never comes.{/n}
"It would have worked," {n}Minagho says afterward, very quietly, to nobody.{/n} "If he'd been stupider. They used to be stupider."''',
    "broken_hepzamirah": '''"No." {n}Hepzamirah stands so fast the bench goes over.{/n} "I've changed my mind, clown. When my father's dog dies under my hand, the whole Abyss will know whose hand it was. I don't hand my kills to failed generals like alms to a beggar."
{n}Minagho's screen holds for an hour in the lower town, perfect, with nobody behind it. Then the collector walks out of it and away, and Minagho comes back with blood on her lip from biting it.{/n}''',
    "screen_failed": '''{n}The collector stops in the mouth of the alley, sniffs, and laughs. The brand-reader's seal on his wrist does not care what face Minagho is wearing.{/n}
"Little Minagho," {n}he calls into the dark.{/n} "Still running, general?"
{n}She comes back to the table with the glamour hanging off her in rags and does not speak for a long time. When she does, it is to Hepzamirah, who never got her chance to strike.{/n}
"Say one word, horns. One. I'll cut it out of you."''',
}
COLLECTOR_RETRY_START = '''"He's back." {n}Minagho drops a torn scrap of a hired man's ear on the table between the cups.{/n} "Your father's collector, horns. Same nose, same seal, fresh throats. He's found the tavern's street and he walks it every night, a little closer. We do it again. I screen him, my face on it; you break him; the credit's mine. And this time nobody sends anybody to the wrong fucking street."'''

TURF_HISTORY = {
    "start": '''{n}Chivarro sets her cup down very gently, which is how you know.{/n}
"Herrax asked you for my head. I know, honey; it's sitting right at the front of yours, where you keep the things you'd rather not say over supper." {n}She smiles.{/n} "She's got my floor, my customers and my bed linen, and she wanted the rest of me boiled down for her cellar. I'm running a house of my own now, under your city, and doing very nicely without her. That's what she can't stand."''',
    "historical": '''"So the account stands as it is. She asked. You didn't. I remember both."
{n}Chivarro draws a claw down the tablecloth, slowly, and leaves four neat cuts in it.{/n} "That's for her, whenever she's in a mood to be told. The rest she can have when she dies. I'll bring a bucket."''',
}
TURF_LIVE = {
    "start": '''{n}Chivarro has a letter open beside her cup, in Herrax's big looping hand, scented strongly enough to reach the next table.{/n}
"Herrax asked you for my head once. Now she writes to me like a cousin. Listen." {n}She reads it in Herrax's own purr, perfectly.{/n} "'My sweet, let's not be tedious. Keep your little cellar; I keep the Delights. And in return I won't send my girls round to poach the darlings you've collected in Drezen.'"
{n}She folds it.{/n} "Generous. She keeps my chair, which she stole, and agrees not to steal anything else this season. I'm not getting the Delights back, honey. I'm not stupid. But I'd like her to bleed a little for her terms before I take them."''',
    "historical": '''"Unsettled. Yes. Let her sit in my chair and wonder whether I'm coming for it."
{n}Chivarro tears Herrax's letter in half, then in half again, and drops the pieces in your wine.{/n} "I'm not. I've got a better house. But she doesn't know that, and I want her lying awake not knowing it."''',
    "herrax_reply": '''{n}Herrax's answer comes back the next evening by a girl from the Delights who won't sit down and won't take off her veil. The letter smells of the Delights' incense.{/n}
"Honey. Tell your little friend she can stop sulking. The Delights are mine; I took them, I improved them, and the customers queue round the square to tell me so. Her Drezen darlings I'll leave alone. Not out of love, my sweet. They're cheap stock, and I don't shop in the bargain bin. That's my word, and I don't give it often. Herrax."''',
    "chivarro_reply": '''"'Cheap stock.'" {n}Chivarro reads it twice, and laughs, and then doesn't.{/n} "She always did call whatever she couldn't afford rubbish."
{n}She pulls a fresh sheet toward her and writes without stopping, in a small, savage, level hand.{/n} "There. She keeps the chair. I don't want it back; it stinks of her. Every one of my people she leaves alone is one less reason I'll have to come and take her face off. Carry it, honey. And don't read it on the way. I'll know."''',
    "terms_kept": '''{n}A week later Chivarro sets her purse on the table and counts it twice. Every one of her Drezen girls is still in her house. Three of Herrax's have turned up at her door asking for work; she sent them back with their faces intact and a note, which she considers the height of courtesy.{/n}
"She kept her word. I kept mine. The Delights stay hers, my house stays mine, and neither of us has had to poison anyone." {n}She sounds almost disappointed.{/n} "Don't call it peace, honey. It's two madams agreeing not to rob each other this season. Next season we'll see who's hungrier."''',
    "names_missed": '''"You gave her my letter with her name crossed out and mine written over it, and gave me hers with half the terms smudged into soup." {n}Chivarro drops both letters on the table.{/n} "Now she thinks I'm claiming the Delights, and I think she's claiming my girls, and we're both too busy hating you to hate each other. Congratulations, honey. That's an achievement."''',
    "unsettled": '''"Then nothing's agreed." {n}Chivarro holds Herrax's letter to the lamp and watches it curl.{/n} "She keeps my old chair because she's sitting in it. I keep my new house because I'm sitting in that. If either of us wants more, we'll find out which of us has the better knives."''',
}
TURF_RETRY_START = '''"She's written again." {n}Chivarro flicks the scented letter across the table at you.{/n} "Same offer, honey: she keeps my chair, she leaves my Drezen girls alone. This time you carry it properly, or I'll write the next one on your back."'''
TURF_BROKEN = {
    "herrax_term_broken": '''{n}Herrax's second letter is shorter, and the scent on it is stronger.{/n}
"Changed my mind, my sweet. Two of your Drezen darlings came to my door on their own, begging, and I'd be a fool to turn away stock that walks in by itself. I'll take whoever else wants to come. Tell your friend she can complain to Lamashtu. Herrax."''',
    "chivarro_term_broken": '''"No." {n}Chivarro crumples her own concession before the ink is dry.{/n} "I've been lying to myself, honey, and I hate that more than I hate her. That chair is mine. That floor is mine. Every customer she's got, I trained. I'm not signing it away for a promise from a woman who sells her girls by the pound."
{n}She smiles at you, very sweetly.{/n} "Carry that to her. Word for word."''',
}

TEXTS = {}
for scene in (HEP + "job", HEP + "retry"):
    TEXTS.update({(scene, node): body for node, body in COLLECTOR.items()})
TEXTS[(HEP + "retry", "start")] = COLLECTOR_RETRY_START
TEXTS.update({(TURF + "turf.history", node): body for node, body in TURF_HISTORY.items()})
for scene in (TURF + "turf.live", TURF + "retry"):
    TEXTS.update({(scene, node): body for node, body in TURF_LIVE.items()})
TEXTS[(TURF + "retry", "start")] = TURF_RETRY_START
TEXTS.update({(TURF + "retry", node): body for node, body in TURF_BROKEN.items()})


def register(payload, scenes, refs):
    by_id = {body["Id"]: body for body in payload["Scenes"]}
    for (sid, nid), body in TEXTS.items():
        matches = [node for node in by_id[sid]["Nodes"] if node["Id"] == nid]
        if len(matches) != 1:
            raise KeyError("minachiv pairs: %s/%s matched %d nodes" % (sid, nid, len(matches)))
        if not matches[0]["Text"].startswith("[PROSE PENDING:"):
            raise ValueError("minachiv pairs: %s/%s is no longer a placeholder" % (sid, nid))
        matches[0]["Text"] = body.strip()

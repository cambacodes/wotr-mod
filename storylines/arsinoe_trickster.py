"""Arsinoe on the Trickster path: the leased cauldron (Writer/handoffs/trickster/arsinoe.md, family F09).

Canon: after Council 5-1 the Commander holds the Council's soul cauldron (EmptySyphon d66b1fdc, "Empty Soul Cauldron";
filled, "This diamond glows with the essence of Nirvana"). Shyka: "it does not look like a cauldron... It is likely that it
came from the coffers of Abadar himself" (Council_5-1/Cue_0041 b936cf96). The Treasury mark and the lease are authored.
Arsinoe has no Trickster blocking state; the lease is an opportunity, not a defied fate. Two physical beats on her own
vendor list, epilogue pages, and two allocated reactions (Konomi, Socothbenoth; ledger 05 section 4).
"""
from story_format import c, n, p, reaction, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
CONTACT = "a609ed9b2205d034bb3bb04d2a255681"
ANSWERS = "ecaf5cfe8087a4f45a2269974f4885c9"
KONOMI_OFFICER = "0dc8b8604bb33c846a63f3eb62443674"
LEASE = "arsinoe.trickster.cauldron.lease"
COLLECTION = "arsinoe.trickster.cauldron.collection"
STAYS = "arsinoe.trickster.stays_to_collect"
LIEN = "arsinoe.trickster.cost.lien"
WOUND = "arsinoe.trickster.cost.collateral_worldwound"


def physical(id, title, entry, nodes, requires, forbids, delay):
    SCENES.append(scene(id, title, "Arsinoe", 5, entry, nodes, requires=requires, forbids=forbids, delay=delay, last=5,
                        optional=True, Relationship="arsinoe", Areas=[DREZEN], Chapters=[5],
                        ContactUnit=CONTACT, AnswerLists=[ANSWERS]))


physical(LEASE, "Property of the Treasury", '"I have something a priestess of Abadar should see."', [
    n("start", "Arsinoe", '''{n}You set the Council's cauldron on her counter. It does not look like a cauldron. It never has. It is a diamond the size of a clenched fist, cut by someone who did not care what it cost, in a cradle of old gold.{/n}
{n}Arsinoe's gold eyes go to it before you have taken your hand away. She does not touch it. Her fingers stop a breath above the stone, the way they would over an offering plate.{/n}
"If this is what I think it is..."
{n}She takes a jeweler's loupe from her sleeve and bends to the cradle. Under the grime of the Abyss there is a line of worn lettering, stamped, not engraved. Clerks' capitals.{/n}
"By the First Vault. *Treasury of Abadar, Absalom.*"
{n}She straightens, frowning, and taps the loupe against her lip.{/n}
"A soul cauldron, Commander, if I am any judge, and I am. Marks can be forged; I have forged a few, for training purposes. But if this one is genuine, then this stone was consecrated to my god and entered in his inventory, and it belongs in a vault in Absalom, not on a counter in a war camp. I will not ask how it came to you. I suspect the answer involves demons, and I suspect you enjoyed it."''',
      c("Continue", "shamira", requires=("shamira.killed",)),
      c("Continue", "terms", forbids=("shamira.killed",))),
    n("shamira", "Arsinoe", '''{n}She tilts the stone toward the lamp. Deep inside it something that is not light moves, slow and patient, like a fish under ice.{/n}
"It is not empty."
{n}She straightens and puts the loupe away very carefully.{/n}
"You have been filling my god's property, Commander. No. I do not want to know with what. I do not want to know with whom. I want it entered in the ledger, so that when someone asks, I can say that I recorded it and that I did not look."''',
      c("Continue", "terms")),
    n("terms", "Arsinoe", '''"The law is simple, and it is old, and I did not write it. Property of the Treasury that leaves the Treasury without a contract is stolen. Stolen goods return to their owner. I will have it crated for Absalom with the next caravan south, under temple seal."
{n}She says it pleasantly. She has already reached under the counter for a crate and a handful of straw.{/n}
"It is nothing personal. I like you a great deal more than I like most people who walk in here with the Treasury's property. But the Treasury does not care whom I like."''',
      c('"It\'s leased, not stolen. Returnable at the end of the world."', "rent", mythic="Trickster",
        alignment=("Lawful", 1), crusade=("Finances", -500)),
      c('"It stays with me. Abadar can send a bill."', "refused"),
      c('"Another time."', abort=True)),
    n("rent", "Arsinoe", '''{n}The straw stops halfway to the crate.{/n}
"Leased."
{n}She looks at you for a long, pleased moment, the way she looks at a customer who has finally made an offer worth her time.{/n}
"A lease is a contract. A contract is lawful. And a lawful arrangement for the use of the Treasury's property, drawn up by an ordained priestess in good standing, is... something I could defend before my superiors, if I had to. I would enjoy defending it."
"But I am not a fool, and neither is the Treasury. I will write to Absalom tonight, with a drawing of the mark. If they deny the stone is theirs, the lease lapses and the temple keeps the rent for its trouble. If they confirm it, the lease stands, and I am the priestess who found the Treasury's lost property *and* made it pay. Either way, I do not end up explaining to a tribunal why I let a demigod walk off with a god's diamond on a handshake."
"Rent, then. Five hundred crowns to the temple, from the crusade's chest, today. The same again every season the property is out of the vault. I do not haggle over the Treasury's property, Commander. I will, however, listen."''',
      c('"Agreed."', "leased"),
      c('"Five hundred a season is robbery with a halo."',
        check=dict(Skill="CheckDiplomacy", DC=25, Success="discount", Failure="raised", CommanderOnly=True))),
    n("discount", "Arsinoe", '''{n}She hears you out with her chin on her hand, and when you are done she is smiling in a way she would deny in front of a clerk.{/n}
"...Three seasons' grace. For a lessee who proposes to carry the property into the Abyss and back, and who argues like a moneylender's apprentice. Do not tell the Treasury I said so. Do not tell anyone I enjoyed that."''',
      c("Continue", "leased")),
    n("raised", "Arsinoe", '''"No."
{n}She writes a figure on a slip of paper and turns it round to face you.{/n}
"For wasting a priestess's time, the rate goes up. Another two hundred. Abadar rewards thrift, Commander. He does not reward charm. You will find that I am the same, most days."''',
      c("Continue", "leased", crusade=("Finances", -200), flags=("arsinoe.trickster.cost.rent_raised",))),
    n("leased", "Arsinoe", '''{n}She draws the lease on temple vellum in a clean, fast hand and reads every line of it aloud, including the ones you would rather she had skipped. You sign twice. She signs once, with a flourish she has clearly practiced.{/n}
{n}Then she warms a stick of gold wax over the lamp, presses her seal into it, and fixes the tag to the diamond's cradle, just below the old Treasury stamp. *On lease.*{/n}
"Leased. Returnable at the end of the world, in whatever condition the world leaves it. Rent accrues from today. Abadar is my witness, and he has a very good memory for sums."''',
      c('"Then I\'m a tenant of Abadar."', forbids=("council.fought",), flags=("arsinoe.trickster.primed", LIEN)),
      c("Continue", "grudge", requires=("council.fought",))),
    n("grudge", "Arsinoe", '''"And the gentlemen you took it from? The ones you then fought?"
{n}She does not wait for an answer. She writes a line at the foot of the lease.{/n}
"A lessee answers for the property, Commander, not for the manners of the previous holders. I will note them as a risk. If any of them come to my counter asking for it back, I shall tell them it is leased, and show them the seal, and then I shall shout for the guard."''',
      c('"Then I\'m a tenant of Abadar."', flags=("arsinoe.trickster.primed", LIEN))),
    n("refused", "Arsinoe", '''{n}She puts the straw back under the counter. She does not argue. That is worse.{/n}
"Then the church of Abadar will send a bill. It will be long, it will be accurate, and it will find you wherever you are, including places that do not have a postal service. May Abadar keep you, Commander. And your property. Such as it is."''',
      c('"Leave the crate where it is."', abort=True)),
], requires=("trickster", "arsinoe.capital", "council.cauldron_given"),
   forbids=("arsinoe.trickster.primed", "arsinoe.closed"), delay=0)


physical(COLLECTION, "Collateral", '"You wanted to see me about the lease?"', [
    n("start", "Arsinoe", '''{n}A ledger lies open on the counter. A stick of gold wax is softening over a candle, and beside it there is a second copy of the lease, annotated in three colors of ink.{/n}
"Absalom has answered." {n}She lays a letter on the ledger, heavy paper, a seal in gold wax far older and larger than hers.{/n} "The mark is genuine. The Treasury confirms the loss of one soul cauldron, 'circumstances of removal unrecorded', and ratifies the lease. I have been commended. I have also been instructed to ensure the property's safe return. So.
{n}She turns the letter face down.{/n}
"An inspection, Commander. I am told my lessee intends to carry the property to the place where the Worldwound was first opened, and then, I assume, to do something heroic with it. My ledger calls that 'unusual wear'. The temple requires collateral against total loss."''',
      c("Continue", "pledge")),
    # Cross-route ledger reads (the wedding guests, row 8's consular rider) return when the Kiana and Konomi Trickster
    # routes produce kiana.trickster.cost.guests_robbed / konomi.trickster.cost.recalled (rrt_verify: no dead gates).
    n("pledge", "Arsinoe", '''{n}She dips her pen and waits, the nib a finger's width above the page.{/n}
"So. What does the Commander pledge?"''',
      c('"The Fool King\'s still. A barrel baron and everything he guards."', "still",
        requires=("fool_king.available",), forbids=("fool_king.gone",), flags=("arsinoe.trickster.cost.collateral_still",)),
      c('"Collateral: one Worldwound, slightly used. Foreclose whenever you like."', "wound", mythic="Trickster", flags=(WOUND,)),
      c('"My word."', "word", flags=("arsinoe.trickster.cost.collateral_word",))),
    n("still", "Arsinoe", '''{n}She listens to the whole story of the barrel the Fool King made a baron, and the still behind it, and the oath it swore never to let the beer run dry, without interrupting once. Her pen does not move until you are finished. Then she presses the wax onto the page.{/n}
"A royal still with a titled barrel for a guard. Commander, that is a going concern. Accepted. Please try not to drink the collateral."''',
      c("Continue", "stay")),
    n("wound", "Arsinoe", '''{n}She writes it down. She does not laugh, which is the funniest thing about it.{/n}
{n}The seal takes. For a breath the candle flame leans east, toward the Wound, and the shadows in the shop lean with it, as if something very large had just been appraised and found adequate.{/n}
{n}Arsinoe looks at the flame. Then she looks at you.{/n}
"Accepted. The church of Abadar now holds a lien on the Worldwound. If the property is not returned, we foreclose, and I will personally see the place run properly. Clean streets. Honest weights. Receipts."''',
      c("Continue", "stay")),
    n("word", "Arsinoe", '''"Words are what I lend against last, Commander."
{n}She seals the page anyway, with rather more wax than it needs, and presses the seal down longer than the wax requires.{/n}
"But I lend against them."''',
      c("Continue", "stay")),
    n("stay", "Arsinoe", '''{n}She closes the ledger and does not hurry to let go of it.{/n}
"A lien wants a lienholder who stays to collect. I meant to leave Drezen the day it could stand on its own; I have always left, it is what I do, there is always another city with worse accounts. I find I have business here now. My business, of my choosing. Do not flatter yourself that it is yours."''',
      c('"Then I\'ll make sure the payments are always a little late."', "threshold",
        requires=("arsinoe.campaign_lover",), flags=(STAYS, "arsinoe.started")),
      c('"Then I\'ll make sure the payments are always a little late."',
        forbids=("arsinoe.campaign_lover",), flags=(STAYS, "arsinoe.started")),
      c('"Business, then. May Abadar keep you."', flags=("arsinoe.trickster.collection_closed",))),
    n("threshold", "Arsinoe", '''{n}Something in her face changes. It is the look she gives a price she has already decided to pay.{/n}
"Late. Yes. I charge interest on late."
{n}She comes round the counter, turns the sign in the window to CLOSED, and locks the till before she locks the door. Her gold eyes do not leave you while she does either.{/n}
"The lien stands, Commander. This is outside the lease. Abadar keeps the accounts; he does not keep the curtains. Close them."
{n}You do. When you turn back she has undone her collar with one hand, and the clasps of her robe with the other, without any hurry at all, and the robe slides from her shoulders and pools at her feet like spilled coin. She steps out of it and takes you by the lapels and pulls, and her mouth on yours is slow and very deliberate, the kiss of a woman who has read the whole contract and means to enforce every clause.{/n}
{n}The ledger goes off the counter. Neither of you stops to pick it up. She lays you back across the place where it was and follows you down, her hair falling around both your faces like a drawn curtain, and for one long, appraising moment she only looks at you, the look of a woman about to sign.{/n}
{n}Whatever the church of Abadar holds a lien on, it is not this.{/n}''',
      c("Continue", "morning")),
    n("morning", "Arsinoe", '''{n}Morning. The sign still says CLOSED. She is at the counter in her shift with her hair unbound, a cup of tea going cold at her elbow, entering a line in the ledger in very small handwriting.{/n}
"Interest on the property: accrued. Everything else: no charge."
{n}She blots it and closes the book before you can read it.{/n}
"Tell anyone I did something for free and I will deny it under oath. Before a priest of my own god, if necessary. Go and be impressive, Commander. I have a shop to open, and you owe me rent."''',
      c('"Leave before the first customer arrives."')),
], requires=("trickster.ever", "arsinoe.capital", "arsinoe.trickster.primed", LEASE),
   forbids=(COLLECTION, "arsinoe.closed"), delay=72)


def epilogue(id, title, text, requires, forbids=()):
    SCENES.append(scene(id, title, "Epilogue", 1, "", [n("end", "Narrator", text, portrait="Arsinoe")],
                        requires=requires, forbids=forbids, last=6, Relationship="arsinoe"))


epilogue("arsinoe.trickster.epilogue.bill_to_threshold", "Consumed in the course of its intended use",
    '''{n}The soul cauldron of the Treasury of Abadar did not come back from Threshold. It burst at the rift with everything else that was meant to change the world, and the world changed.{/n}
{n}Arsinoe entered it in the temple ledger as "leased property, consumed in the course of its intended use". Then she drew up the bill, addressed it to Threshold, attention of the Commander, and sent it by the ordinary post. It came back unopened, bearing a seal nobody in Drezen could identify. She filed it with evident satisfaction. To a priest of Abadar, an unpaid account is simply a relationship that has not yet ended.{/n}''',
    ("trickster.ever", LIEN, "arsinoe.siphon_burst"))
epilogue("arsinoe.trickster.epilogue.pot_returned", "Returned at the end of the world",
    '''{n}The soul cauldron came back from Threshold whole, which surprised everyone except Arsinoe. She had it crated for Absalom under temple seal, with a note in the lease's margin in her smallest, neatest hand: "Returned at the end of the world, as agreed. Rent in arrears: considerable."{/n}
{n}The Commander is still paying it. Arsinoe has never once suggested a discount.{/n}''',
    ("trickster.ever", LIEN), ("arsinoe.siphon_burst",))
epilogue("arsinoe.trickster.epilogue.foreclosure", "A lien on one Worldwound, slightly used",
    '''{n}Among the records of the Drezen temple of Abadar lies a lien, sealed in gold wax, on "one Worldwound, slightly used". Clerks from Absalom have tried three times to strike it out as a jest. Each time, the clerk who opens the file finds the seal whole and the terms in order, and closes it again rather more quietly than he opened it.{/n}
{n}The church has not yet foreclosed. Arsinoe says it is a question of choosing the right moment.{/n}''',
    ("trickster.ever", WOUND), ("ending.wound_closed",))
epilogue("arsinoe.trickster.epilogue.foreclosure_closed", "Collateral withdrawn by closure",
    '''{n}When the Worldwound closed, Arsinoe took out the lien sealed in gold wax on "one Worldwound, slightly used", and wrote across it, in a very small hand: "Collateral withdrawn by closure. Account satisfied."{/n}
{n}It is the only entry in her ledger she ever underlined twice.{/n}''',
    ("trickster.ever", WOUND, "ending.wound_closed"))


REACTIONS = [
    reaction("Socothbenoth", "arsinoe.trickster.cauldron_seen.react_socothbenoth", (LIEN,),
             '''{n}A perfumed note, unsigned, is pinned inside your wardrobe door. The pin is a woman's hairpin. It is not anyone's you know.{/n}
"Darling. The priestess of Abadar has put a *lien* on our cauldron. On a Council artefact! Alichino is beside himself; he says Hell would have charged interest from the moment of theft, and he is quite right, and I have never loved you more. Do be careful. The next complaint may count as a prayer, and I should hate to share you with a god of banking."''',
             remote=True, forbids=("socot.gone", "council.fought", "council.fought_nocta_allied"),
             chapter=5, last=5, title="A perfumed note", Areas=[DREZEN], Chapters=[5]),
    reaction("Konomi", "arsinoe.trickster.cauldron_seen.react_konomi", (LIEN,),
             '''{n}Lady Konomi's smile is smug and faintly predatory.{/n}
"An Abadaran lien on a planar artefact. Commander, the Royal Treasury of Mendev would give a great deal for a priestess who can invoice demons. Do tell her the Queen's accounts are open. To negotiation, naturally. Never to audit."''',
             answer_list=KONOMI_OFFICER, forbids=("konomi.dismissed", "konomi.retained_dead"),
             chapter=5, last=5, entry='"The priestess of Abadar has leased me a Council artefact."'),
]
SCENES.extend(REACTIONS)

COLLECTOR = p("When people asked why a priestess who always moved on had stayed, Arsinoe said she had an outstanding "
              "account in Drezen. She never said which.", requires=(STAYS,))


def integrate(payload):
    """Registered-route edit (save-safe: text only): the three kept endings gain the collector paragraph (E14c)
    instead of sibling pages, so the ordinary one-ending-per-history invariant holds unchanged."""
    for scene_ in payload["Scenes"]:
        if scene_["Id"] in ("arsinoe_ending_kept", "arsinoe_ending_open", "arsinoe_ending_promised"):
            scene_["Nodes"][0].setdefault("Paragraphs", []).append(dict(COLLECTOR))

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
WORD = "arsinoe.trickster.cost.collateral_word"
STILL = "arsinoe.trickster.cost.collateral_still"
CALLED = "arsinoe.lastcall.called"                   # Last Call: the cauldron handed back at the rift (read only)


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
"A soul cauldron, Commander, if I am any judge, and I am. Marks can be forged; I have forged a few, for training purposes. But if this one is genuine, then this stone was consecrated to my god and entered in his inventory, and it belongs in a vault in Absalom, not on a counter in a war camp. I will not ask how it came to you. I suspect the answer involves demons, and I suspect you enjoyed it."
{n}You tell her what Shyka said of it at the Council: likely from Abadar's coffers. She does not look up from the loupe.{/n}
"Likely. Shyka's guess and a worn stamp. That is not proof, Commander. It is, however, a very good start on a lawsuit."''',
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
{n}Her mouth curves, the way it does for a customer who has finally made an offer worth her time.{/n}
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
{n}She does not even reach for the pen.{/n}
"For wasting a priestess's time, the rate goes up. Another two hundred. Abadar rewards thrift, Commander. He does not reward charm. You will find that I am the same, most days."''',
      c("Continue", "leased", crusade=("Finances", -200), flags=("arsinoe.trickster.cost.rent_raised",))),
    n("leased", "Arsinoe", '''{n}She draws the lease in a clean, fast hand and reads the line that matters aloud: the lessee is you, by name. Not the crusade, not the Queen, not the chest. If the stone is lost, the debt follows you, and Abadar's church has collected from widows and grandchildren before now without losing sleep.{/n}
{n}Then she warms a stick of gold wax over the lamp, presses her seal into it, and fixes the tag to the diamond's cradle, just below the old Treasury stamp. *On lease.*{/n}
"Leased. Returnable at the end of the world, in whatever condition the world leaves it. Rent accrues from today. Abadar is my witness, and he has a very good memory for sums."''',
      c('"Then I\'m a tenant of Abadar."', forbids=("council.fought",), flags=("arsinoe.trickster.primed", LIEN)),
      c("Continue", "grudge", requires=("council.fought",))),
    n("grudge", "Arsinoe", '''"And the gentlemen you took it from? The ones you then fought?"
{n}She does not wait for an answer.{/n}
"A lessee answers for the property, Commander, not for the manners of the previous holders. I will note them as a risk. If any of them come to my counter asking for it back, I shall tell them it is leased, and show them the seal, and then I shall shout for the guard."''',
      c('"Then I\'m a tenant of Abadar."', flags=("arsinoe.trickster.primed", LIEN))),
    n("refused", "Arsinoe", '''{n}She puts the straw back under the counter. She does not argue. That is worse.{/n}
"Then the church of Abadar will send a bill. It will be long, it will be accurate, and it will find you wherever you are, including places that do not have a postal service. May Abadar keep you, Commander. And your property. Such as it is."''',
      c('"Leave the crate where it is."', abort=True)),
], requires=("trickster", "arsinoe.capital", "council.cauldron_given"),
   forbids=("arsinoe.trickster.primed", "arsinoe.closed"), delay=0)


physical(COLLECTION, "Collateral", '"You wanted to see me about the lease?"', [
    n("start", "Arsinoe", '''{n}A ledger lies open on the counter, and a stick of gold wax is softening over a candle.{/n}
"Absalom has not answered." {n}She lays a letter on the ledger: her own, come back unopened, the seal broken by a Mendevian road warden who has written ROAD CLOSED across it in charcoal.{/n} "The roads south are shut, the Treasury's clerks are three countries away, and I hold a lease on a stone that may or may not be my god's, on the word of a worn stamp and Shyka's guess. So the lease stands on its own clause. Until Absalom rules, the lessee answers for the stone as if it were the Treasury's, and the temple answers for the lease. The temple, in Drezen, is me. I have put my name beside yours on a guess, Commander. I do not do that. So.
{n}She turns the letter face down.{/n}
"An inspection, Commander. I am told my lessee intends to carry the property to the place where the Worldwound was first opened, and then, I assume, to do something heroic with it. My ledger calls that 'unusual wear'. The temple requires collateral against total loss."''',
      c("Continue", "pledge", forbids=("konomi.trickster.cost.recalled",)),
      c("Continue", "rider", requires=("konomi.trickster.cost.recalled",))),
    # Ledger row 8: the only Konomi line Arsinoe bills is the consular recall rider. The wedding lines (Kiana's paste trick,
    # guests_robbed) are added by kiana_trickster.integrate: it gates these two choices off on guests_robbed and appends the
    # wedding / wedding_dog nodes, with restitution (Q3 or bought back) skipping straight to the pledge (tested below).
    n("rider", "Arsinoe", '''{n}She turns back a page of the ledger, to a line in red ink she has clearly been waiting to show you.{/n}
"One more entry, while the book is open. The Mendevian consulate billed the crusade for Lady Konomi's recall rider. A clerk's rider, one, sent after a dispatch that said she was dead. Paid." {n}She taps the figure.{/n} "It came across my desk because I keep the only honest books in Drezen. I know what it bought. I simply wanted you to know that I saw it, and that I entered it at cost."''',
      c("Continue", "pledge")),
    n("pledge", "Arsinoe", '''{n}She dips her pen and waits, the nib a finger's width above the page.{/n}
"So. What does the Commander pledge?"''',
      c('"The Fool King\'s still. A barrel baron and everything he guards."', "still",
        requires=("fool_king.available",), forbids=("fool_king.gone",), flags=(STILL,)),
      c('"Collateral: one Worldwound, slightly used. Foreclose whenever you like."', "wound", mythic="Trickster", flags=(WOUND,)),
      c('"My word."', "word", flags=(WORD,))),
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
    n("threshold", "Arsinoe", '''{n}Something in her face changes, and she does not trouble to hide it.{/n}
"Late. Yes. I charge interest on late."
{n}She comes round the counter, turns the sign in the window to CLOSED, and locks the till. Only the till. Her gold eyes stay on you the whole time.{/n}
"The lien stands, Commander. This is outside the lease. Abadar keeps the accounts; he does not keep the curtains. Close them."
{n}You do. When you turn back she has undone her collar with one hand, and the clasps of her robe with the other, without any hurry at all, and the robe slides from her shoulders and pools at her feet. She stands in the lamplight a breath longer than she needs to, because she knows exactly how she looks and she wants you to look. Then she steps out of the silk and draws you in by one hand, and her mouth on yours is slow and very sure of itself.{/n}
{n}The ledger goes off the counter. Neither of you stops to pick it up. She lays you back across the place where it was and follows you down, her hair falling around both your faces like a drawn curtain, and laughs, low, at whatever she sees in yours.{/n}
"You are staring, Commander. Good," {n}she says, and settles astride you, knees braced on the counter's edge, and reaches down between you.{/n}''',
      c("Continue", "morning")),
    n("morning", "Arsinoe", '''{n}The sign still says CLOSED when you wake, and the street outside is already loud. She is at the counter in her shift with her hair unbound, a cup of tea going cold at her elbow, entering a line in the ledger in very small handwriting.{/n}
"Interest on the property: accrued. Everything else: no charge."
{n}She blots it and closes the book before you can read it.{/n}
"Tell anyone I did something for free and I will deny it under oath. Before a priest of my own god, if necessary. Go and be impressive, Commander. I have a shop to open, and you owe me rent."''',
      c('"Leave before the first customer arrives."')),
], requires=("trickster.ever", "arsinoe.capital", "arsinoe.trickster.primed", LEASE),
   forbids=(COLLECTION, "arsinoe.closed"), delay=72)


# The collateral is collected on whichever cauldron page the finale shows (E14c paragraphs).
WORD_CALLED = ("{n}The Commander's word, pledged as collateral, stayed on her books whatever became of the rest of the account. "
               "Arsinoe called it in exactly once, years later, in a single line on temple vellum: a request for an evening, "
               "at a time of her choosing, with no excuses accepted. The Commander came. She marked the debt paid, and then, "
               "in the margin, reopened it.{/n}")
# Paragraphs have no ForbidOverrides: "alive" is (no sacrifice) or trickster.commander_back (which implies sacrifice).
ALIVE = "trickster.commander_back"
COLLATERAL = (
    p(WORD_CALLED, requires=(WORD,), forbids=("sacrifice",)),
    p(WORD_CALLED, requires=(WORD, ALIVE)),
    p("{n}The Commander's word, pledged as collateral, was never called in. Arsinoe kept it on her books at face value for "
      "the rest of her life, and would not let the clerks from Absalom write it off.{/n} \"A word is not void because the one "
      "who gave it is dead,\" {n}she told them.{/n} \"It is merely unpaid.\"", requires=(WORD, "sacrifice"), forbids=(ALIVE,)),
    p("{n}The Fool King's still, pledged as collateral, was audited by the temple of Abadar every season. The barrel baron "
      "met each inspection in full regalia. Arsinoe's reports describe the collateral as 'well guarded, fully "
      "operational, and regrettably drinkable', and bear the rings of several cups.{/n}", requires=(STILL,)),
)


def epilogue(id, title, text, requires, forbids=(), paragraphs=()):
    SCENES.append(scene(id, title, "Epilogue", 1, "", [n("end", "Narrator", text, portrait="Arsinoe", paragraphs=paragraphs)],
                        requires=requires, forbids=forbids, last=6, Relationship="arsinoe"))


BURST_VARIANTS = (
    p("{n}Arsinoe entered it in the temple ledger as{/n} \"leased property, consumed in the course of its intended use\"{n}. Then she "
      "drew up the bill, addressed it to Threshold, attention of the Commander, and sent it by the ordinary post. It came "
      "back unopened, bearing a seal nobody in Drezen could identify. She filed it with evident satisfaction. To a priest of "
      "Abadar, an unpaid account is simply a relationship that has not yet ended.{/n}", forbids=(CALLED, "lastcall.active")),
    p("{n}Arsinoe entered it in the temple ledger as{/n} \"leased property, consumed in the course of its intended use\"{n}, drew up "
      "the bill, and laid it on the Commander's table herself the morning after. It was paid by noon, arrears and all. She "
      "closed the account in front of the Commander, which she had never before done for anyone.{/n}", requires=("lastcall.active",),
      forbids=(CALLED,)),
    p("{n}It had not burst as the Commander's, though. At the rift, by the letter of the lease, the Commander had handed it "
      "back, a breath before the end: returnable at the end of the world, and this had been the end of the world. What "
      "burst was the temple's property, consumed in the course of its intended use, and the lessee owed nothing but the "
      "arrears. Arsinoe entered the discharge in her smallest hand and underlined the date.{/n}", requires=(CALLED,)),
)

epilogue("arsinoe.trickster.epilogue.bill_to_threshold", "Consumed in the course of its intended use",
    '''{n}The soul cauldron Arsinoe had leased to the Commander did not come back from Threshold. It burst at the rift with everything else that was meant to change the world, and the world changed. Absalom never did rule on whether the stone had been the Treasury's.{/n}''',
    ("trickster.ever", LIEN, "arsinoe.siphon_burst"), paragraphs=BURST_VARIANTS + COLLATERAL)
epilogue("arsinoe.trickster.epilogue.pot_returned", "Returned at the end of the world",
    '''{n}The soul cauldron came back from Threshold whole, which surprised everyone except Arsinoe. She locked it in the temple strongroom with the gold-wax tag still on the cradle, and wrote in the lease's margin in her smallest, neatest hand: "Returned at the end of the world, as agreed. Title: unproven, pending Absalom. Rent in arrears: considerable."{/n}''',
    ("trickster.ever", LIEN), ("arsinoe.siphon_burst",), paragraphs=(
        p("{n}The Commander is still paying it. Arsinoe has never once suggested a discount.{/n}", forbids=("lastcall.active", "sacrifice")),
        p("{n}The Commander is still paying it. Arsinoe has never once suggested a discount.{/n}", requires=(ALIVE,), forbids=("lastcall.active",)),
        p("{n}Nobody paid it. The Commander's estate was settled without the arrears, which Arsinoe carried forward every year "
          "in her own hand and never once wrote off.{/n}", requires=("sacrifice",), forbids=(ALIVE, "lastcall.active")),
        p("{n}The Commander paid the arrears the next morning, across her own table, to the copper, and watched her close the "
          "account. She has never once suggested a discount, and she did not start then.{/n}", requires=("lastcall.active",)),
    ) + COLLATERAL)
epilogue("arsinoe.trickster.epilogue.foreclosure", "A lien on one Worldwound, slightly used",
    '''{n}Among the records of the Drezen temple of Abadar lies a lien, sealed in gold wax, on "one Worldwound, slightly used". Clerks from Absalom have tried three times to strike it out as a jest. Each time, the clerk who opens the file finds the seal whole and the terms in order, and closes it again rather more quietly than he opened it.{/n}''',
    ("trickster.ever", WOUND), ("ending.wound_closed",), paragraphs=(
        # One settlement per history, agreeing with the cauldron page (Sol r5 COX): unsettled, paid at her table, or called in.
        p("{n}The church has not yet foreclosed. Arsinoe says it is a question of choosing the right moment.{/n}",
          forbids=("lastcall.active", CALLED)),
        p("{n}It is a released lien. The morning the Commander paid the arrears across her table, Arsinoe wrote{/n} \"Released on "
          "payment\" {n}beneath the seal, and filed it again rather than burn it, because she could not bring herself to destroy "
          "so good a document.{/n}", requires=("lastcall.active",), forbids=(CALLED,)),
        p("{n}It is a copy. The lease was called in at Threshold and the lien went with it to the First Vault, attached to "
          "whatever the Wound became. Beneath the seal, in her hand:{/n} \"Transferred. Collect there.\"", requires=(CALLED,)),
    ))
epilogue("arsinoe.trickster.epilogue.foreclosure_closed", "Collateral withdrawn by closure",
    '''{n}When the Worldwound closed, Arsinoe took out the lien sealed in gold wax on "one Worldwound, slightly used", and wrote across it, in a very small hand: "Collateral withdrawn by closure. Lien discharged."{/n}
{n}It is the only entry in her ledger she ever underlined twice. The rent was another matter, and another ledger.{/n}''',
    ("trickster.ever", WOUND, "ending.wound_closed"), paragraphs=(
        p("{n}The lien itself had gone to the First Vault at Threshold, when the lease was called in; what she discharged in "
          "Drezen was her copy, and she sent the Vault a note to say so.{/n}", requires=(CALLED,)),
    ))


REACTIONS = [
    reaction("Socothbenoth", "arsinoe.trickster.cauldron_seen.react_socothbenoth", (LIEN,),
             '''{n}A perfumed note, unsigned, is pinned inside your wardrobe door. The pin is a woman's hairpin. It is not anyone's you know.{/n}
"Darling. The priestess of Abadar has put a *lien* on our cauldron. On a Council artefact! Alichino is beside himself; he says Hell would have charged interest from the moment of theft, and he is quite right, and I have never loved you more. Do be careful. The next complaint may count as a prayer, and I should hate to share you with a god of banking."''',
             remote=True, forbids=("socot.gone", "council.fought", "council.fought_nocta_allied"),
             chapter=5, last=5, title="A perfumed note", Areas=[DREZEN], Chapters=[5]),
    reaction("Konomi", "arsinoe.trickster.cauldron_seen.react_konomi", (LIEN, "konomi.in_office"),
             '''{n}Lady Konomi's smile is smug and faintly predatory.{/n}
"An Abadaran lien on a planar artefact. Commander, the Royal Treasury of Mendev would give a great deal for a priestess who can invoice demons. Do tell her the Queen's accounts are open. To negotiation, naturally. Never to audit."''',
             answer_list=KONOMI_OFFICER, forbids=("konomi.dismissed", "konomi.retained_dead"),
             # Sol INT (2026-09-30): she must be in her office, and a Konomi returned by her Trickster route hears it too.
             # konomi.retained_dead is runtime-derived (it clears when she is raised), so it stays a plain Forbid.
             ForbidOverrides={"konomi.dismissed": "konomi.trickster.returned"},
             chapter=5, last=5, entry='"The priestess of Abadar has leased me a Council artefact."'),
]
SCENES.extend(REACTIONS)

# --- R2-6 late commitment (Sol COX, 2026-09-30) ------------------------------------------------------------------------
# A Trickster who flirted at the collection (stays_to_collect) but never reached her commitment scene still has a romance
# to answer: the first rent day after Threshold. The derived key means "reached the last beat", as on every route.
LATE_COMMITTED = "arsinoe.trickster.late_committed"
COURTED = "arsinoe.courting"                       # the roof: her hand taken, the courtship begun
# Reached the last beat: the collection flirt, or an ordinary courtship begun on the roof (no cauldron needed).
DERIVED = {LATE_COMMITTED: [["trickster.ever", STAYS], ["trickster.ever", COURTED, "arsinoe.roof_shared"]]}
LATE_GONE = ("arsinoe.committed", "arsinoe.closed", "arsinoe.future_spoken")


def late(id, text, *choices, paragraphs=()):
    return n(id, "Narrator", text, *choices, portrait="Arsinoe", paragraphs=paragraphs)


SCENES.append(scene("arsinoe.trickster.late.commit", "Interest on late payments", "Epilogue", 6, "", [
    late("offer", '''{n}The spring after Threshold, Arsinoe came to the Commander's door in person, in her good robes, with her hair up and her gold eyes very steady.{/n}''',
         c('[Take her hand, and draw her in by the collar.]', "night"),
         c('"Then collect. There is no war left to be late for."', "table"),
         c('"There is nothing to collect, Arsinoe. Business only."', "business"),
         paragraphs=(
             p("{n}She laid the lease on the table and put a finger on the line about late payments.{/n} \"You told me you would make "
               "certain the payments were always a little late. The war ended before the first one fell due. So I have come "
               "to collect early, which is a thing I never do.\"", requires=(STAYS,)),
             p("\"We had a roof, once,\" {n}she said.{/n} \"Bread and cheese, and a city I pointed at for a whole evening while you "
               "held my hand.\"", requires=(COURTED,), forbids=(STAYS,)),
             p("\"And a book I promised to lend you, with a whole page about an innkeeper's sauce.\"",
               requires=(COURTED, "arsinoe_first_impression"), forbids=(STAYS,)),
             p("\"And a table in Tovin's shop after closing, where you read the sauce while I watched your face.\"",
               requires=(COURTED, "arsinoe_hours_of_her_own", "arsinoe.next_table"), forbids=(STAYS,)),
             p("\"And a walk I made far too long, so that it would not end.\"",
               requires=(COURTED, "arsinoe_hours_of_her_own", "arsinoe.next_walk"), forbids=(STAYS,)),
             p("\"Then the war took the evenings, and I let it. I have decided it has had enough of them.\"",
               requires=(COURTED,), forbids=(STAYS,)),
             p("\"I did not come as the temple. I came because I want you, Commander, and I am not in the habit of wanting "
               "things I have not priced. I have not priced this. So. Yes, or no?\""),
         )),
    late("night", '''{n}She let you. She had come dressed for the temple, collar to hem, and she stood very still under your hands while you worked the collar open, her gold eyes on yours. At the clasps of the robe she lost patience, pushed your hands aside and undid the rest herself, quickly, and let the whole weight of it fall.{/n}
"You kept me waiting for a war," {n}she said.{/n} "I will not wait for fastenings as well."
{n}She walked you backward to the bed with one hand flat on your chest, pushed, and came down over you, a knee either side of your hips, her hair slipping its pins and falling around both your faces. She took your wrists and set your hands on her waist, exactly where she wanted them. Then she bent, and kissed you, and sank down.{/n}''',
         c("Continue", "morning")),
    late("morning", '''{n}In the morning she was at the Commander's table in her shift, her hair down, writing on the back of something in her smallest hand. "Collected," it said. Then, a little lower: "Early."{/n}
"Go back to sleep, Commander," {n}she said, without looking up.{/n} "I intend to be very late opening the shop, and I want company for it."
{n}The next month she set a second cup on the shelf in the room behind her shop, and she never once charged for it.{/n}''',
         c('[Stay.]')),
    late("table", '''{n}She let you take her hand across the table. Then she leaned over and kissed you, hard, the way she presses a seal, and sat back to admire the impression.{/n}
"Supper, then. Tonight. The rest in a month, after I have had a month to look forward to it. I have waited through a war; I can afford four weeks, and I intend to enjoy every one of them at your expense."
{n}She kept that appointment, and one every month after it, and the queue outside her shop learned to expect it opened late.{/n}''',
         c('[Keep the appointment.]')),
    late("business", '''{n}Arsinoe looked at the Commander for a while. Then she gathered her gloves, and did not hurry about it.{/n}
"Business only," {n}she said.{/n} "May Abadar keep you, Commander."
{n}She stayed in Drezen. When their business crossed she was perfectly courteous about it, and she never once sat down.{/n}''',
         c('[Let her go.]')),
], requires=(LATE_COMMITTED,), forbids=(*LATE_GONE, "sacrifice", "ascended", "swarm", "true_lich"),
   ForbidOverrides={"sacrifice": "trickster.commander_back"}, last=6, Relationship="arsinoe"))

# Ascended: no visit up a stair. She writes, and the page says why there is no night (brief pattern 3).
SCENES.append(scene("arsinoe.trickster.late.ascended", "An invoice to a higher address", "Epilogue", 6, "", [
    late("letter", '''{n}Arsinoe never learned how to send a letter to a Commander who had become something the roads did not reach. She wrote one anyway, the spring after Threshold, on temple vellum, and left it on the altar of Abadar, which was the highest address she had.{/n}
{n}It said that she had meant to come to the Commander's door in her good robes with her hair up, and say that she wanted them, and that she had not priced it. It said that a door was a necessary part of the arrangement. It asked, with perfect courtesy, whether the Commander still had one.{/n}
{n}Nobody knows whether it was answered. The second cup on her shelf was never given to another guest.{/n}''')],
    requires=(LATE_COMMITTED, "ascended"), forbids=LATE_GONE, last=6, Relationship="arsinoe"))

COLLECTOR = p("{n}When people asked why a priestess who always moved on had stayed, Arsinoe said she had an outstanding "
              "account in Drezen. She never said which.{/n}", requires=(STAYS,))


def integrate(payload):
    """Registered-route edit (save-safe: text only): the three kept endings gain the collector paragraph (E14c)
    instead of sibling pages, so the ordinary one-ending-per-history invariant holds unchanged."""
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    for scene_ in payload["Scenes"]:
        if scene_["Id"] in ("arsinoe_ending_kept", "arsinoe_ending_open", "arsinoe_ending_promised"):
            scene_["Nodes"][0].setdefault("Paragraphs", []).append(dict(COLLECTOR))


# eng7-l09 / E-Q7-19: preserve the original 500 + failed-haggle 200 transaction.
_RENT_PAID = "arsinoe.trickster.cost.rent_paid"
_RENT_RAISED = "arsinoe.trickster.cost.rent_raised"
_SURCHARGE_PAID = "arsinoe.trickster.cost.rent_surcharge_paid"
_lease = next(s for s in SCENES if s["Id"] == LEASE)
_nodes = {nd["Id"]: nd for nd in _lease["Nodes"]}
_nodes["terms"]["Choices"][0]["Set"].append(_RENT_PAID)
_nodes["terms"]["Choices"][0]["Forbids"].append(_RENT_PAID)
_nodes["raised"]["EnterSet"] = [_RENT_RAISED]
_nodes["raised"]["Choices"][0]["Set"].append(_SURCHARGE_PAID)
for _choice in _nodes["start"]["Choices"]:
    _choice["Forbids"].extend((_RENT_PAID, _RENT_RAISED))
_nodes["start"]["Choices"].extend((
    c("Continue", "raised", requires=(_RENT_RAISED,), forbids=(_SURCHARGE_PAID,)),
    c("Continue", "rent", requires=(_RENT_PAID,), forbids=(_RENT_RAISED,)),
    c("Continue", "leased", requires=(_SURCHARGE_PAID,)),
))
for _choice in _nodes["rent"]["Choices"]:
    _choice["Forbids"].append(_RENT_RAISED)
# end eng7-l09
# eng8-q8h begin: readiness offers a question; only its physical yes earns acceptance.
LATE_READY = "arsinoe.trickster.late_ready"
LATE_ACCEPTED = "arsinoe.trickster.late_accepted"
LATE_DECLINED = "arsinoe.trickster.late_declined"
DERIVED[LATE_READY] = DERIVED[LATE_COMMITTED]
DERIVED[LATE_COMMITTED] = [["trickster.ever", LATE_ACCEPTED]]
SCENES.append(scene("arsinoe.trickster.late.ask", "An evening owed", "Arsinoe", 5,
    '"What will you collect when the war is over?"', [
    n("ask", "Arsinoe", '{n}Arsinoe sets down her pen. Outside, a wagon rattles toward the citadel with fresh dressings.{/n} "An evening with you. I have waited long enough to ask. Will you keep it for me?"',
      c('"Yes. Come to my door when this is over."', "yes", flags=(LATE_ACCEPTED,)),
      c('"Business only, Arsinoe."', "no", flags=(LATE_DECLINED,))),
    n("yes", "Arsinoe", '{n}She catches your hand before you can draw it back.{/n} "Then I shall come in person. Do not make me knock twice."', c()),
    n("no", "Arsinoe", '{n}She releases your hand and takes up her pen.{/n} "Business only. May Abadar keep you, Commander."', c()),
], requires=("trickster.now", LATE_READY),
   forbids=(*LATE_GONE, LATE_ACCEPTED, LATE_DECLINED), last=5, Relationship="arsinoe",
   Areas=[DREZEN], ContactUnit=CONTACT,
   AnswerLists=[ANSWERS], optional=True))
# The postwar page remembers the physical answer; it never asks or writes it again.
_late = next(s for s in SCENES if s["Id"] == "arsinoe.trickster.late.commit")
for _i in (0, 1):
    _late["Nodes"][0]["Choices"][_i]["Requires"].append(LATE_ACCEPTED)
_late["Nodes"][0]["Choices"][2]["Requires"].append(LATE_DECLINED)
# end eng8-q8h

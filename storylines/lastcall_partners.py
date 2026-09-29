"""Last Call, per partner (doc 04 §3.7, §4.2, §6): the debts owed to powers, the call-in lines spoken at the rift, and each
committed partner's coda page (Block B).

Rules this file keeps (user rulings, 2026-09-28; 07-HAREM-CONFLICTS.md D1-D8):
- Every partner stays. No page ends a romance and no page is an exit. The old "refuses" slot now means only that she refuses
  the deal being called in or its price. A concrete failure the player made on her route (a lie, a kneel, a denial) becomes
  a price paid at the table: she is at the table, apart.
- Nothing comes true by fiat. Each call-in line collects a debt the player created on that route.
- Villains stay villains and are pleased with the evil done for them. A paladin objects only where her route shows she knew.
- Each page Requires the real committed flag. The R2-6 late_committed keys mean "reached the last beat", not "said yes"
  (Eritrice and Chadali define them as started), so they are not a romance, and a late commit made on an epilogue page sets
  no flag anyway.

Reserved for the later household pass (doc 05/08), not emitted: <rel>.lastcall.p.household and <rel>.lastcall.p.secret
("what she found out") paragraph slots. The engine rejects paragraphs keyed to flags nothing sets yet."""

from story_format import c, n, p, scene

OPEN = "trickster.lastcall.open"
ACTIVE = "lastcall.active"
ON_RECORD = "lastcall.dead_on_record"
H2 = "lastcall.h2"
PILLAR = "trickster.lastcall.creditors_called"   # a live power was called in: its collection plays on the Collectors page
BOTTLED = "trickster.lastcall.cost.bottled"
MORTAL = "trickster.lastcall.cost.mortal"
SOCOTH_GONE = ("socot.gone", "council.fought_nocta_allied")   # Cue_0570: "No one ever saw Socothbenoth again"

# Reserved for the household pass (05-HAREM-HOOKS.md §5); never set here.
RESERVED_SLOTS = ("lastcall.p.household", "lastcall.p.secret")


def called(rel):
    return rel + ".lastcall.called"


def resolved(rel):
    """Set by every answer of her call-in, including leaving it unspoken: the last joke waits for every open debt."""
    return rel + ".lastcall.resolved"


MC = "minagho_chivarro.trickster.cost."

# --- Debts owed to powers (doc 04 §3.7). The flask keeps the Commander alive; creditors only collect. A live power's call-in -
# creditors pillar. An outlived creditor collects nothing, and says so on the Collectors page.
DEBTS = [
    dict(key="socoth", groups=[["anevia.trickster.cost.socoth_listening"], ["anevia.trickster.cost.wrong_door"], [MC + "socoth_owed"]],
         called_by=[called("anevia"), called("minagho_chivarro")], outlived=list(SOCOTH_GONE),
         ledger_title="Socothbenoth: a door to listen at",
         ledger_text="Paid for a closet with a standing right to listen, or a story owed instead. The Silken Sin collects. He prefers to collect during something private.",
         page_called="Socothbenoth came first, dressed for an occasion to which nobody else had been invited, and named his terms before he had taken off his gloves. He was owed the one conversation he had not been allowed to overhear, and he wanted it told to a closed door, in the Commander's own voice, with himself on the other side of it. Then he raised the price: the telling was to happen in the house where he had listened before, so that the right person would know he had come to collect. The Commander haggled him down to the door and the voice, and lost the house. The rift was told to the wardrobe from the first joke to the last, and the Silken Sin, on the other side, did not interrupt once, which those who know him say has never happened before. He left humming. Anevia heard him go.",
         page_outlived="Socothbenoth never came to collect. Whatever had become of the Silken Sin had happened before he could, and the wardrobes of Drezen were only wardrobes again. More than one person checked them every night for a year anyway."),
    dict(key="baphomet", groups=[[MC + "baphomet_debtor"], [MC + "baphomet_terms"], [MC + "baphomet_knelt"], [MC + "baphomet_branded"],
                                 ["hepzamirah.trickster.cost.baphomet_grudge"]],
         called_by=[called("minagho_chivarro"), called("hepzamirah")],
         ledger_title="Baphomet: a seal on my palm",
         ledger_text="His seals, he says, simply mark their bodies as his. Mine is marked. He will want the body.",
         page_called="Baphomet sent no one. The Lord of the Minotaurs does not send; he waits for his seal to bring him what it marks. It brought him nothing. A seal needs a body to own, and the one he had been promised was either in an empty grave or on its feet with its death corked in a flask, where no seal reaches. It is said that the Prince of Beasts does not forgive a debtor who cheats him on a point of his own wording. It is also said that he has begun to reread his contracts."),
    dict(key="nocticula", groups=[["nocticula.trickster.cost.shade_paid"], ["nocticula.trickster.cost.shade_refused"]],
         called_by=[called("nocticula")], outlived=[],
         ledger_title="The Lady in Shadow: an answer owed",
         ledger_text="A favour of her choosing, or a stalemate of kept secrets. Either way she has an interest in my continued breathing, and Nocticula is a patient creditor.",
         page_called="The Lady in Shadow did not come in person; she seldom does. A note came instead, unsigned, smelling of night-blooming flowers, and it said only that the Lady in Shadow was pleased to find her debtor still in circulation, that a living debtor is worth a great deal more than a legend, and that she expected her return on the matter in person, and soon."),
    dict(key="ramisa", groups=[["nurah.trickster.cost.ramisa_fee"], ["nurah.trickster.cost.ramisa_audience"], ["nurah.trickster.cost.bill_in_your_name"]],
         called_by=[called("nurah")],
         ledger_title="Ramisa Shed-Skin: the only seat",
         ledger_text="The marilith keeps a duplicate of every bill with my name on it, and I sold her the only seat at the last night of the war. She will want her performance.",
         page_called="Ramisa Shed-Skin came to collect art. She had bought the only seat at the last night of the war and had watched all of it through a mirror in her market, and now she wanted the story set down in ink, with herself in the dedication. She got the story. She asked for the flask as well, prettily, and then again with more of her arms, and did not get it."),
    dict(key="herrax", groups=[[MC + "herrax_favor"]], called_by=[called("minagho_chivarro")],
         ledger_title="Herrax: the house special",
         ledger_text="A favour on account at the house of Herrax, for a demon returned to me. Interest compounds. So does Herrax.",
         page_called="Herrax called in her favour with interest, and worked the interest out at the table where the Commander could watch the figure grow. Nobody who was present will say what the favour was. Chivarro, who was present, said afterwards that it was cheap, and would not say for whom."),
    dict(key="abadar", groups=[["arsinoe.trickster.cost.lien"], ["arsinoe.trickster.cost.collateral_worldwound"],
                               ["arsinoe.trickster.cost.collateral_still"], ["arsinoe.trickster.cost.collateral_word"]],
         called_by=[called("arsinoe")],
         ledger_title="The First Vault: a cauldron on lease",
         ledger_text="Leased from the church of Abadar, returnable at the end of the world. A lien stands. The Master of the First Vault reads the small print so I don't have to.",
         page_called="The church of Abadar collected to the letter. The cauldron had been leased returnable at the end of the world, and at Threshold the world ended in every sense the lease required; it went back as it had come, and the lien attached itself to whatever the Wound became. Before the year was out, a counting-house of the First Vault stood where the rift had been, and its clerks asked every traveller what they were bringing in and what they meant to take out."),
    dict(key="sunhammer", groups=[["kiana.trickster.cost.sunhammer_favour"], ["kiana.trickster.cost.guests_robbed"], ["kiana.trickster.cost.courier_marked"]],
         called_by=[called("kiana")],
         ledger_title="Darek Sunhammer: a favour and some stones",
         ledger_text="The jeweller who made the wedding stones is owed a favour, or a grudge, and still keeps what he keeps. A dwarf remembers a bill.",
         page_called="Darek Sunhammer sent his apprentice, as he always did, with the bill carried in his head rather than on paper, where a jeweller keeps the things he does not want read. One favour, owed. The Commander settled it across a table in Drezen in terms neither side ever repeated, and the wedding guests still in Sunhammer's keeping went home the same week."),
    dict(key="mutasafen", groups=[["hepzamirah.trickster.cost.mutasafen_grudge"], ["hepzamirah.trickster.cost.lab_funded"],
                                  ["hepzamirah.trickster.cost.blood_sample"], ["hepzamirah.trickster.cost.vial_paid"],
                                  ["hepzamirah.trickster.cost.vial_forged"]],
         called_by=[called("hepzamirah")],
         ledger_title="Mutasafen: rent on a body",
         ledger_text="He grew her a body. Somebody is paying for it, in blood, in coin or in secrets, and Mutasafen always collects first.",
         page_called="Mutasafen collected first, as Hepzamirah had promised he would. The maker of her body wanted his price for it, whatever the Commander had bargained with, and he came for it himself, since his revival system spares him the usual caution. Hepzamirah received him. What was said between the body-maker and his tenant is not recorded; the Commander was sent out of the room, and was told afterwards that {mf|he|she} had been invaluable."),
    dict(key="wintersun", groups=[["soana.trickster.cost.blood_given"], ["soana.trickster.cost.guardian_paid"], ["soana.trickster.cost.knot_bearer"],
                                  ["soana.trickster.cost.leash_held"]],
         called_by=[called("soana")],
         ledger_title="The Wintersun spirits: a portion",
         ledger_text="The spirits of Soana's wood took a portion of me when the knot was tied. The rest is mine to give. They know where to find me.",
         page_called="The spirits of the Wintersun wood took their portion in the spring, when the snow went off the barrows. Soana had given them blood once already and would not give them the Commander's. She bound them again with her own hands, told the Commander so without a word of gratitude, and went back to her graves."),
]


# --- Partners: the call-in line at the rift and the coda page ---------------------------------------------------------------

def page_p(text, requires=(), forbids=(), any_groups=()):
    return p(text, requires=requires, forbids=forbids, any_groups=any_groups)


PARTNERS = []


def partner(key, rel, commit, closed, title, opener, paragraphs, declined=None, page_forbids=(), deal=(), call=None,
            call_commit=None, ledger=None):
    PARTNERS.append(dict(key=key, rel=rel, commit=commit, closed=closed, title=title, opener=opener, paragraphs=paragraphs,
                         declined=declined, page_forbids=tuple(page_forbids), deal=[list(g) for g in deal], call=call,
                         call_commit=call_commit or [[commit]], ledger_title=ledger[0] if ledger else None,
                         ledger_text=ledger[1] if ledger else None))


def call(entry, text, *choices):
    """choices: (text, extra flags, requires, forbids). Every choice sets <rel>.lastcall.called."""
    return dict(entry=entry, text=text, choices=list(choices))


PILLAR_CHOICE = "Continue"
PLAIN_CHOICE = "Continue"

A = "anevia.trickster."
partner("anevia", "anevia", "anevia.committed", "anevia.closed", "Anevia, After",
    '''Anevia Tirabade had the watch on the walls of Drezen the night the rift took the Commander, or failed to. She had refused to give it up to anyone. She came down at dawn with a crossbow she had not fired and a face nobody asked about, and went looking for the one person in the city who owed her an explanation. She found {mf|him|her} in the kitchen, eating her bread.''',
    (
        page_p('''Socothbenoth collected his standing right in her own wardrobe. Anevia sat outside the door with a bottle and listened to him listen, and when he was done she told him that if he ever came back she would nail it shut from the inside. He said it was the kindest threat anyone had made him in a century.''', requires=(called("anevia"), A + "cost.socoth_listening")),
        page_p('''The closet the Silken Sin had given the Commander stayed in her house. It opened only onto rooms the Commander had stood in, and never onto the same room twice. She used it to leave notes: short, rude, and always on the pillow.''', requires=(A + "cost.stolen_door",)),
        page_p('''She never quite forgave the silence at the gate, when she asked what happened at Iz and got nothing. She kept the Commander's chair. She kept it at the far end of the table, and on the bad nights she raised her cup to Irabeth instead, and the Commander learned to drink to that as well.''', requires=(A + "cost.lie_exposed",)),
        page_p('''The crusade buried an empty coffin in Drezen. Anevia stood a watch over the grave for three nights with the crossbow she had not fired, in case anyone came to check what was in it. Someone did, twice. She never told the Commander who, and she never needed the crossbow either time.''', requires=(ON_RECORD,)),
        page_p('''When the flask was opened in Drezen, it was Anevia who made the Commander sit down afterwards and eat something, and who told the priests to go and bless someone who needed it.''', requires=(H2,)),
    ), declined=A + "declined", page_forbids=("committed",),
    deal=[[A + "cost.socoth_listening"], [A + "cost.wrong_door"], [A + "cost.stolen_door"]],
    call=call('''[Call in the wardrobe] "Silken Sin, you're still listening at her door. Tonight you'll hear the best of it. Consider us square after."''',
        '''{n}You say it to the fire as though the fire were a crowded room. Somewhere a very long way off, in a house in Drezen, a wardrobe door creaks: someone in silk sleeves has stopped listening at one door and started listening to you.{/n}''',
        (PILLAR_CHOICE, (PILLAR,), (A + "cost.socoth_listening",), SOCOTH_GONE),
        (PILLAR_CHOICE, (PILLAR,), (A + "cost.wrong_door",), SOCOTH_GONE + (A + "cost.socoth_listening",)),
        (PLAIN_CHOICE, (), (A + "cost.stolen_door",), (A + "cost.socoth_listening", A + "cost.wrong_door")),
        (PLAIN_CHOICE, (), ("socot.gone",), (A + "cost.stolen_door",)),
        (PLAIN_CHOICE, (), ("council.fought_nocta_allied",), ("socot.gone", A + "cost.stolen_door"))),
    call_commit=[["anevia.committed"], ["committed"]])

I = "irabeth.trickster."
partner("irabeth", "irabeth", "irabeth.committed", "irabeth.closed", "Irabeth, Dismissed",
    '''Irabeth Tirabade was still under the Commander's orders at Threshold, as she had been since Iz. She had tried to put the sword down and could not, not until the Wound was shut. When word came that it was, she laid the sword on the table in her quarters, flexed the hand for some time, and sat down to wait for someone to dismiss her.''',
    (
        page_p('''Nobody did. The Commander came instead, with the discharge {mf|he|she} had kept unsigned since Iz, filled it in, dated it the day after the rift, and added a line under the signature: "Report in person." She did. She reported most evenings, for the rest of their lives, and was never once late.''', requires=(called("irabeth"),)),
        page_p('''She knew about the lie at Iz; Nevi had seen to that. Irabeth kept serving, because a knight does, and kept the Commander at arm's length at every table afterwards, because a wife does. The Commander learned to take the far chair without being told.''', requires=(I + "cost.accounting_lied",)),
        page_p('''She went to the Commander's funeral in full plate and stood at attention through every speech. Afterwards she told the chaplain that the deceased had been absent without leave for most of the war, and that she saw no reason to take it seriously now.''', requires=(ON_RECORD,)),
        page_p('''When the flask was opened she saluted it, then saluted the Commander, then saluted the flask again, and declined to explain the order of precedence.''', requires=(H2,)),
    ), declined=I + "declined", page_forbids=("committed",),
    deal=[[I + "cost.under_orders"]],
    call=call('''[Call in the standing order] "Knight-Captain, you're still under my orders. Nobody's dismissed tonight. Including me."''',
        '''{n}You say it the way you have said a hundred orders on a hundred walls. Somewhere behind you, in Drezen, a knight who cannot put down her sword stands up without knowing why.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    call_commit=[["irabeth.committed"], ["committed"]],
    ledger=("Irabeth: an order not rescinded", "The Knight-Captain is still under my orders. Her discharge is unsigned. I will need to be alive to sign it."))

# The canon pair (doc 04 §4.3). Its commit flag `committed` is set only by the registered `future` scene's "Yes. I choose a
# life with you both." (or the Trickster `third_chair`): both women's acceptance of the triad is a recorded route choice.
partner("tirabade", "tirabade", "committed", "closed", "The Third Chair",
    '''Irabeth and Anevia Tirabade went home after the war to the house on the corner. The three of them had settled the question before Threshold, at their own table, when the Commander answered that {mf|he|she} chose a life with them both; the wives had asked it together, and they held {mf|him|her} to the answer. There was a third chair. It was Anevia who decided where it went, and Irabeth who decided it would be dusted. Some nights, according to the neighbours, the house on the corner laughed until dawn.''',
    (
        page_p('''Irabeth's discharge came by post, two months after Threshold, in a hand she knew. Anevia read it once over her shoulder, then took it, folded it in three, and put it in the drawer where she kept the things she meant to use against people later.''', requires=(I + "cost.under_orders",)),
        page_p('''The wardrobe in the back room was only a wardrobe now. Anevia kept a hammer on top of it anyway.''', requires=(A + "cost.socoth_listening",)),
        page_p('''They had both come back, one from a grave and one from a road, and neither would let the other forget whose turn it was to be grateful.''', requires=("lastcall.tirabade.both_returned",)),
        page_p('''The lie was paid for at that table, in full, over a year. The third chair was moved to the far end, where the draught came in, and it stayed there until Anevia moved it back, one evening, without a word. Irabeth pretended not to notice for a week.''', any_groups=[[A + "cost.lie_exposed", I + "cost.accounting_lied"]]),
        page_p('''The world had buried the Commander. The house on the corner had not been consulted and did not agree.''', requires=(ON_RECORD,)),
    ), declined="tirabade.trickster.declined")

AR = "arsinoe.trickster."
partner("arsinoe", "arsinoe", "arsinoe.committed", "arsinoe.closed", "Paid in Full",
    '''Arsinoe of the First Vault closed the Commander's account on the morning after Threshold, in a counting-room that smelled of ink and scorched air. She checked every figure twice. Then she closed the book, put her hand flat on the cover, and said that it was the first ledger she had ever balanced that made her want to laugh.''',
    (
        page_p('''The cauldron went back as leased. She was there when it did, with a receipt, and when the clerks of Abadar asked what the Worldwound was now worth as collateral, she told them "Slightly used," and would not be moved.''', requires=(called("arsinoe"),)),
        page_p('''The Fool King's still had been pledged, a barrel baron and everything it guarded. The First Vault now holds a lien on the best-loved tap in Drezen. Arsinoe audits it in person on the first of every month, and has never once been seen to leave before the audit was complete, or sober.''', requires=(AR + "cost.collateral_still",)),
        page_p('''The Commander's word had been the collateral. Abadar's clerks entered it at face value, which amused them, and then found that it held, which did not.''', requires=(AR + "cost.collateral_word",)),
        page_p('''The First Vault does not recognize death as grounds for default. The account stayed open.''', requires=(ON_RECORD,)),
    ), deal=[[AR + "cost.lien"], [AR + "cost.collateral_worldwound"], [AR + "cost.collateral_still"], [AR + "cost.collateral_word"]],
    call=call('''[Return the cauldron] "Returnable at the end of the world. This is the end of the world. Here."''',
        '''{n}Somewhere under the roar, you swear you hear an abacus. The First Vault has a claim on this night, and the First Vault is always present at the end of an account.{/n}''',
        (PILLAR_CHOICE, (PILLAR,), (), ())))

J = "jerribeth.trickster."
partner("jerribeth", "jerribeth", "jerribeth.committed", "jerribeth.closed", "Rent Day",
    '''Jerribeth collected her rent on the first of the month after Threshold, as the terms said, and every first of the month after that. She never once let the Commander forget whose house {mf|he|she} was living in, or whose {mf|he|she} was living on. She was, in the opinion of everyone who met her, entirely too pleased with herself.''',
    (
        page_p('''She took her forfeit in the second year: one memory, hers to choose. She chose the rift. The Commander remembers everything about Threshold except the joke itself, and she tells it back, badly, on purpose, whenever {mf|he|she} asks.''', requires=(J + "cost.forfeit",)),
        page_p('''She had worn a deserter from the stockade since the night the Commander gave him to her, and she wore him to the victory feast. Nobody missed him. She made a point of telling the Commander how right {mf|he|she} had been about that.''', requires=(J + "cost.host",)),
        page_p('''The statue of the Lady of the Sun stood in the square at Drezen for years afterwards, and pilgrims who prayed to it went home oddly satisfied and slightly out of pocket.''', requires=(J + "cost.tenant",)),
    ), declined=J + "declined",
    deal=[[J + "cost.tenant"], [J + "cost.lodger"], [J + "cost.host"], [J + "cost.toast"], [J + "cost.forfeit"]],
    call=call('''[Call in the lease] "Rent's due, tenant. A house doesn't fall down while you're living in it."''',
        '''{n}Something in the back of your skull laughs, low and delighted, and settles more comfortably into its lodgings.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Jerribeth: rent due on the first", "I let a succubus a room. The rent is due on the first of the month. She will collect it from me, or from my estate, and she prefers me."))

K = "konomi.trickster."
partner("konomi", "konomi", "konomi.committed", "konomi.closed", "Terms, Accepted",
    '''Konomi returned to the court of Nerosyan after the war as its attaché to whatever the Commander had become, a post the court invented for her because nobody else would take it. Her reports were exact, witty and quite useless to anyone who wanted to know what the Commander was actually doing, which was the point.''',
    (
        page_p('''She named her price the night after Threshold, as she had said she would: a seat for Nerosyan at every table the Commander ever sat at, and her own name on the invitation. The Commander agreed before she had finished, which she found suspicious, and she spent a year looking for the catch.''', requires=(called("konomi"),)),
        page_p('''She had outfoxed the Commander once, fairly, at the recess, and she never let it be forgotten. It was, she said, the only victory over the Fifth Crusade that the court of Nerosyan ever won.''', requires=(K + "cost.outfoxed",)),
        page_p('''She billed the Commander for every consultation, at her rate, and the Commander paid every bill and kept the receipts in a drawer she was not supposed to know about.''', requires=(K + "cost.consult_fee",)),
    ), declined=K + "declined",
    deal=[[K + "cost.debt_owed"], [K + "cost.consult_fee"]],
    call=call('''[Call in Konomi's terms] "Name your price now, Lady Konomi. Tomorrow you might be collecting from a corpse."''',
        '''{n}Somewhere in Drezen a diplomat sets down her pen mid-sentence, and smiles the way she smiles before she wins.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Konomi: terms not yet named", "The attaché of Nerosyan has terms, and has not said what they are. That is how diplomats keep you alive: by making you curious."))

NO = "nocticula.trickster."
partner("nocticula", "nocticula", "noct.complete", "noct.closed", "The Chair at Her Right Hand",
    '''The Queen of Shadows came to Drezen once after the war, openly, in a carriage that the city pretended not to see. She stayed a night. She left a shadow behind her in the Commander's rooms that did not belong to anything in them, and it stayed there, in the corner by the window, for as long as the Commander kept the rooms.''',
    (
        page_p('''She named her favour at last in the second spring after Threshold: not a temple, not a war, not a soul. A chair. The chair at the Commander's right hand at every table {mf|he|she} would ever sit at, and nobody was to ask whose it was. Scholars of the Abyss still argue over which of them got the better bargain. Those who knew the Commander say {mf|he|she} laughed for a full minute before agreeing.''', requires=(NO + "cost.shade_paid",)),
        page_p('''The stalemate held. Twice her agents were found in the Commander's household, a cook who could not cook and a steward who counted the wrong things; twice the Commander sent them home with a joke pinned to their sleeves. The Midnight Isles learned to seat the two of them at opposite ends of every table, and neither ever raised the matter again.''', requires=(NO + "cost.shade_refused",)),
        page_p('''She has never once been seen to look at the flask. Those who know her say that is how one can tell she is always looking at it.''', requires=(BOTTLED,)),
    ), declined=NO + "declined",
    deal=[[NO + "cost.shade_paid"], [NO + "cost.shade_refused"]],
    call=call('''[Call in the Queen's favour] "Your Majesty, you're owed a favour. Dead debtors are terrible payers."''',
        '''{n}The dark at the edge of the firelight thickens and leans in, attentive and amused, and something that is not quite a shadow rests a hand on your shoulder, lightly, the way a creditor reminds a debtor of an appointment.{/n}''',
        (PILLAR_CHOICE, (PILLAR,), (), ("noct.dead",)),
        (PLAIN_CHOICE, (), ("noct.dead",), ())))

V = "vellexia.trickster."
partner("vellexia", "vellexia", "vellexia.committed", "vellexia.closed", "Never Bored",
    '''Lady Vellexia gave a party the month after Threshold, in Alushinyrra, to celebrate the Commander's survival, or funeral; the invitations were deliberately unclear. It was the event of the decade. The Commander arrived late, in a borrowed face, and she recognized {mf|him|her} across the room and did not give the game away for three hours, which she said afterwards was the most fun she had had in a century.''',
    (
        page_p('''She billed the Commander for the furniture. She had been hung on a wall as a looking-glass, and the bill came to exactly the value of a very good mirror, with interest, payable in visits. The Commander paid in instalments and never once missed one.''', requires=(called("vellexia"),)),
        page_p('''She had come back from the glass a little less than she went in, and she never pretended otherwise. She simply chose, every evening, which part of herself to spend on the Commander, and she was never mean with it.''', requires=(V + "cost.diminished",)),
        page_p('''The Commander had bored her once. She never let {mf|him|her} forget that, and she let {mf|him|her} make up for it for years, at the far end of her table, until it amused her to move {mf|him|her} closer.''', requires=(V + "cost.bored_once",)),
    ), declined=V + "declined", page_forbids=("vellexia.farewell_friends", "vellexia.farewell_slow", V + "kept_as_mirror"),
    deal=[[V + "returned"], [V + "cost.predicted"], [V + "cost.trick_kept"]],
    call=call('''[Call in the furniture bill] "Vellexia, I owe you for the furniture. I'll pay in instalments. Mind you're there to collect them."''',
        '''{n}Across a great distance, and a great many mirrors, a lady who is never bored sits up and pays attention.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Vellexia: the furniture", "I owe Lady Vellexia for a season she spent on my wall. She keeps a very precise account of things nobody else would think to bill."))

NU = "nurah.trickster."
partner("nurah", "nurah", "nurah.complete", "nurah.closed", "The Last Chapter",
    '''Nurah Dendiwhar published her account of the Fifth Crusade two years after Threshold, under her own name, which surprised everyone who knew her. It sold out in Nerosyan in a week and was banned in Mendev in two. The chapter on the Commander was the longest in the book, and the only one in which she admitted to liking anyone.''',
    (
        page_p('''Ramisa came for the story she had bought. Nurah wrote it for her in a single night, every word true, and dedicated it to the marilith "with the author's compliments and none of her gratitude". The duplicate bill with the Commander's name on it went into the fire the same night. Nurah insists she has no idea how.''', requires=(called("nurah"), NU + "cost.bill_in_your_name")),
        page_p('''Ramisa came for the story she had bought, and Nurah wrote it for her in a single night, every word true, and dedicated it to the marilith with the author's compliments and none of her gratitude.''', requires=(called("nurah"),), forbids=(NU + "cost.bill_in_your_name",)),
        page_p('''She never forgot being currency, and she never pretended to. She kept the memory the way she kept her pen: close, sharp, and pointed at anyone who looked as if they might try it again.''', requires=(NU + "cost.larva_memory",)),
        page_p('''Her name went on the cover next to the Commander's. She had insisted. She was right to.''', requires=(NU + "cost.coauthor",)),
        page_p('''Her name went on the cover above the Commander's, in larger letters. She had insisted. The Commander had let her.''', requires=(NU + "cost.name_above",)),
        page_p('''She wrote the Commander's obituary herself, for a Nerosyan broadsheet. It was vicious, accurate and extremely popular.''', requires=(ON_RECORD,)),
    ), deal=[[NU + "cost.ramisa_fee"], [NU + "cost.ramisa_audience"], [NU + "cost.bill_in_your_name"]],
    call=call('''[Call in the custom order] "Madam Shed-Skin, you wanted art. I'm about to make some. Front row."''',
        '''{n}A mirror in a slave market somewhere in the Abyss clears, like breath wiped from glass, and something with a great many arms settles in to watch.{/n}''',
        (PILLAR_CHOICE, (PILLAR,), (), ())))

KI = "kiana.trickster."
partner("kiana", "kiana", "kiana.committed", "kiana.closed", "Home by Spring",
    '''Kiana did not go back to Mendev after the war. She stayed in Drezen, where nobody had arranged her marriage and nobody had put her soul in a jewel, and she took a room above a baker's with a window that looked at nothing in particular. She said it was the first view she had ever chosen.''',
    (
        page_p('''The wedding guests still in Sunhammer's keeping came home that spring. Kiana met every coach. She knew all their names, and she made the Commander learn them too.''', requires=(called("kiana"),)),
        page_p('''She never quite forgave the Commander the guests left behind in the pouch the first time, when {mf|he|she} was quicker to free her than to count the others. She said so once, plainly, and never needed to again.''', requires=(KI + "cost.guests_robbed",), forbids=(called("kiana"),)),
        page_p('''The counterfeit that had stood in for her stone was never found. Kiana suspected the Commander of keeping it, and was right.''', requires=(KI + "cost.counterfeit_spent",)),
    ), deal=[[KI + "cost.sunhammer_favour"], [KI + "cost.guests_robbed"], [KI + "cost.courier_marked"]],
    call=call('''[Call in the courier's account] "Sunhammer, you're owed. Collect now, while I've a pulse to collect from."''',
        '''{n}Far off, in a shop that smells of solder, a dwarf lays down a loupe and makes a note in the one ledger he keeps in his head.{/n}''',
        (PLAIN_CHOICE, (), (), ())))   # Sunhammer is a mortal jeweller: he collects, but is no power

MCR = "minagho_chivarro.trickster."
partner("minachiv", "minagho_chivarro", "minachiv.complete", "minachiv.closed", "The House of Two",
    '''Minagho and Chivarro kept house in Drezen after the war, in a building nobody else would rent, on terms neither of them would ever write down. It was not a romance. It was a contract, renegotiated nightly, and the Commander was a party to it, and they never let {mf|him|her} forget which clauses were {mf|his|hers}.''',
    (
        page_p('''Baphomet's seal was cheated on his own wording, and Minagho's palm still bled on the anniversary. She chose, that first spring, which side of the Lord of Beasts' ledger she would stand on for the rest of her life. She chose the side with the Commander on it, and said it was only because the other side had worse food.''', requires=(called("minagho_chivarro"), MC + "baphomet_debtor")),
        page_p('''Herrax collected her favour. Chivarro paid part of it herself, without being asked, and left the rest of the bill on the Commander's pillow with a kiss printed on the total.''', requires=(called("minagho_chivarro"), MC + "herrax_favor")),
        page_p('''The Commander had knelt to Baphomet once, in front of her. Minagho never forgot it. She stood at the other side of every room after that, and watched the Commander across it with an expression that those who knew her described as a very private kind of respect.''', requires=(MC + "baphomet_knelt",)),
        page_p('''The Commander's left palm never quite closed over the scar. Minagho said it was the best-looking thing about {mf|him|her}.''', requires=(MC + "palm_scar",)),
    ), declined=MCR + "declined",
    deal=[[MC + "baphomet_debtor"], [MC + "baphomet_terms"], [MC + "baphomet_knelt"], [MC + "baphomet_branded"], [MC + "herrax_favor"],
          [MC + "socoth_owed"]],
    call=call('''[Call in the seal and the house special] "Lord of Beasts, your seal's on my palm. Herrax, your favour. Collect from me alive, or not at all."''',
        '''{n}Your left palm burns, a hot line where a seal was pressed. Somewhere very far away something enormous and horned turns its head. Somewhere much nearer, a demon who keeps a house of pleasures reaches for an abacus.{/n}''',
        (PILLAR_CHOICE, (PILLAR,), (), ())))

S = "soana.trickster."
partner("soana", "soana", "soana.committed", "soana.closed", "The Knot",
    '''Soana went back to the Wintersun wood when the war ended and did not ask the Commander to follow. {mf|He|She} followed anyway, and she let {mf|him|her} stay on the understanding that {mf|he|she} would make {mf|himself|herself} useful and keep out of her graves. {mf|He|She} was useful, and kept out of most of them.''',
    (
        page_p('''The knot that bound her life to her guardian's still held, one end breathing in her and the other in Orso. The Commander learned to sleep through the bear's snoring, which Soana said was the most romantic thing anyone had ever done for her.''', requires=(S + "cost.guardian_paid",)),
        page_p('''The spirits came for their portion, and Soana stood between them and the Commander, and paid them in her own blood. She did not say it was for love. She said it was her wood and her debt, which is how Soana says it.''', requires=(called("soana"),)),
        page_p('''She kept the die in the bowl by her hearth, the one the Commander had left there, and rolled it when she could not decide something. She never told the Commander what the numbers meant.''', requires=(S + "cost.die_in_her_bowl",)),
    ), declined=S + "declined",
    deal=[[S + "cost.blood_given"], [S + "cost.guardian_paid"], [S + "cost.knot_bearer"], [S + "cost.leash_held"]],
    call=call('''[Call in the spirits' portion] "Wintersun spirits, you took a portion. The rest is mine to give. Later."''',
        '''{n}You smell pine and cold earth in the middle of the fire. The spirits of a wood a very long way off have a claim on part of you, and they turn toward the fire the way the woods turn toward spring: to see what is owed them.{/n}''',
        (PILLAR_CHOICE, (PILLAR,), (), ())))

AK = "aranka.trickster."
partner("aranka", "aranka", "aranka.extension_kept", "aranka.extension_closed", "The Second Verse",
    '''Aranka's song about the Commander was sung in every tavern between Drezen and Nerosyan within a year of Threshold, and she was paid for almost none of those performances. She did not mind. She said a song that pays its own way is a song that has stopped travelling.''',
    (
        page_p('''She sang the second verse at the rift, or swore afterwards that she had, from two hundred miles away, loud enough for the Wound to learn the words. Nobody could prove otherwise. The crusade sang it back to her all that winter.''', requires=(called("aranka"),)),
        page_p('''The Commander had denied the thief's verse was {mf|his|hers}. Aranka sang it herself, then, in every tavern on the road, and named the thief in the last line, and the Commander had to sit at the back of each of those taverns and applaud. It took a year. She said it was a very short sentence for the crime.''', requires=(AK + "cost.denied",)),
        page_p('''The posters the Commander had put up at every ford were still there. She had them framed.''', requires=(AK + "cost.announced",)),
    ), declined=AK + "declined",
    deal=[[AK + "cost.credited"], [AK + "cost.announced"], [AK + "cost.denied"]],
    call=call('''[Call in the second verse] "Aranka! Second verse! Loud enough for the Wound to learn the words!"''',
        '''{n}Nothing answers but the fire. But you would swear, for the rest of your life, that under the roar someone was singing, off-key and with great emotion, and that the rift paused to listen.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Aranka: a verse unsung", "Aranka is owed a second verse, and the whole crusade knows the tune. A song that isn't finished can't bury you."))

G = "gesmerha.trickster."
partner("gesmerha", "gesmerha", "gesmerha.committed", "gesmerha.closed", "The Commission",
    '''Gesmerha finished the statue the spring after Threshold. She would not let anyone see it until it was done, and when it was done she would not let anyone see it at all, except the Commander, blindfolded, by touch, the way she had carved it. {mf|He|She} said afterwards that it was the only honest likeness anyone had ever made of {mf|him|her}.''',
    (
        page_p('''The commission had been paid in advance, and the coin the Commander drove into the uncut block stayed in the finished stone, over the statue's heart. She had carved around it rather than take it out. She said the ancestors would want to see it had been paid.''', requires=(called("gesmerha"),)),
        page_p('''She kept the carved hands, the ones she had made while the Commander sat for her those three days. They stood on her bench for the rest of her life, and she worked with them facing her, and she would not say why.''', requires=(G + "cost.hands_carved",)),
        page_p('''The Commander had laughed at her grave. She delivered the work, and then she sat apart from the Commander at supper for a whole season, where she could hear {mf|his|her} footsteps and not {mf|his|her} voice. At the end of the season she moved her chair back, and told {mf|him|her} the footsteps had improved.''', requires=(G + "cost.laughed_at_grave",)),
        page_p('''She carved the Commander's gravestone, for the empty grave. It said nothing untrue.''', requires=(ON_RECORD,)),
    ), declined=G + "declined",
    deal=[[G + "cost.advance_paid"], [G + "cost.ancestor_debt"]],
    call=call('''[Call in the commission] "Carver, it's paid for. Finish it. I'd like to see it before they bury me."''',
        '''{n}Somewhere a chisel stops mid-stroke over a block of stone with a coin driven into it. The ancestors of a Sarkorian woodshaper do not let a paid commission go unfinished.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Gesmerha: a commission unfinished", "Gesmerha's ancestors let her come back because there was paid work on her bench. The statue isn't finished. Neither, apparently, am I."))

SE = "seelah.trickster."
partner("seelah", "seelah", "seelah.committed", "seelah.closed", "The Thief's Promise",
    '''Seelah did not go back to the order after the war. She said she had a debt to settle first, and she settled it the way she had settled things as a girl in the streets of Kenabres: quietly, with a hand in someone else's pocket, and an apology afterwards.''',
    (
        page_p('''At the rift the Commander had called in her promise, and she kept it. The flask came out of the Commander's coat one evening in Drezen in her hand, as easily as a purse, and went back into it a moment later, heavier by one small coin. She never said which coin. She said the trick was not the hand, it was the apology.''', requires=(called("seelah"), BOTTLED)),
        page_p('''At the rift the Commander had called in her promise, and she kept it: she picked {mf|his|her} pocket the next evening in Drezen and took back what was hers, and would not say what else she took.''', requires=(called("seelah"),), forbids=(BOTTLED,)),
        page_p('''She would not live under a false name, and the Commander was officially dead. So she kept her own name, and her own door, and walked through it into the Commander's rooms every evening, openly, and told anyone who asked exactly where she was going.''', requires=(ON_RECORD,)),
        page_p('''It was Seelah who found the flask at the edge of the Wound. She said it was the easiest theft of her life.''', requires=(H2,)),
    ), declined=SE + "declined",
    deal=[[SE + "cost.holds_her_death"], [SE + "cost.keeps_it"], [SE + "cost.robbed_back"]],
    call=call('''[Call in the thief's promise] "Seelah, you swore you'd steal it back. Now's the time. Pick my pocket."''',
        '''{n}You feel it before you understand it: a light touch at your coat, a thief's apology, from a woman who is not here.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Seelah: a coin to steal back", "I took something from Seelah's purse at her bier that she didn't earn. She swore she'd steal it back. A thief who hasn't collected won't let you die."))

T = "targona.trickster."
partner("targona", "targona", "targona.committed", "targona.closed", "The Quiet Ward",
    '''Targona did not go back to Heaven when the war ended. She stayed in Drezen's infirmary until the last cot was folded, and then she opened another, in a street near the Commander's house, with the Commander's name over the door and no way for {mf|him|her} to be useful in it.''',
    (
        page_p('''The Commander kept the promise at the rift. {mf|He|She} did not call on her brother's light, though it would have been the easiest thing in the world, and she heard afterwards that {mf|he|she} had not. She did not say anything. She put a second chair by her desk in the ward, and it was never empty for long.''', requires=(T + "cost.light_sealed",), forbids=(called("targona"),)),
        page_p('''At the rift the Commander called on Lariel's light, and broke the one promise she had asked of {mf|him|her}. She learned of it within the week. She stayed; an angel keeps her word even when others do not. But she sat at the other end of the ward's table for a year, and it was a year before she let the Commander carry a lamp for her again.''', requires=(called("targona"), T + "cost.light_sealed")),
        page_p('''She had told Heaven everything, as her price for coming back. Heaven, it seemed, had listened, and had not recalled her. She took that as an answer and did not ask for another.''', any_groups=[[T + "cost.she_told_heaven", T + "cost.raised_openly"]]),
        page_p('''She never forgave the joke at her bier, and she never pretended to. She served beside the Commander for the rest of her long life, courteous, exact, and always at the far end of any room they shared.''', requires=(T + "cost.unforgiven",)),
    ), declined=T + "declined",
    deal=[[T + "cost.raised_openly"], [T + "cost.she_told_heaven"], [T + "cost.raised_the_hard_way"], [T + "cost.light_sealed"]],
    call=call('''[Call on Lariel's light] "Lariel, whatever of you is left in me: one more quiet miracle."''',
        '''{n}Something warm and patient moves under your ribs: a light that belongs to someone's brother, lent to you in an infirmary and never quite given back.{/n}''',
        (PLAIN_CHOICE, (), (), (T + "cost.light_sealed",)),
        ('''[Break your promise to Targona] "Forgive me. I need it."''', (), (T + "cost.light_sealed",), ()),
        ("[Keep your promise] Leave the light where it is.", None, (T + "cost.light_sealed",), ())))   # resolves, not called

D = "dorgelinda.trickster."
partner("dorgelinda", "dorgelinda", "dorgelinda.committed", "dorgelinda.closed", "The Open Line",
    '''Dorgelinda Stranglehold kept the Logistics Council's books for five years after the war, and never once balanced them, because of one line in the Commander's name marked "used, quietly". She said a quartermaster who closes every line has stopped paying attention. She paid attention to that line every day.''',
    (
        page_p('''At the rift the Commander called the line in, and she heard about it, somehow, before the report reached Drezen. She came to find {mf|him|her} that evening with the ledger under her arm. "Explain," she said, and the Commander did, all of it, from the carts to the quiet. She wrote down every word, then put down the pen and did not pick it up again that night.''', requires=(called("dorgelinda"),)),
        page_p('''The boots were entered as paid. She kept the last pair on a shelf in the stores and would not issue them to anyone.''', requires=(D + "cost.boots_paid",)),
        page_p('''Her audit of the Commander never formally concluded. She kept it open, hostile, on principle, and conducted it twice a week over supper.''', requires=(D + "cost.audit_hostile",)),
        page_p('''When the Commander was entered as dead, she refused to close the account. "Dead's a status, not a balance," she told the clerk from Nerosyan.''', requires=(ON_RECORD,)),
    ), declined=D + "declined",
    deal=[[D + "cost.line_open"], [D + "cost.boots_owed"], [D + "cost.carts_signed"]],
    call=call('''[Settle the open line] "Quartermaster: the account marked 'used, quietly'. I'm ready to explain."''',
        '''{n}Somewhere in the stores at Drezen a quartermaster looks up from her ledger at one particular line, and does not rule it off.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Dorgelinda: a line marked \"used, quietly\"", "One line in the stores ledger is open in my name. Dorgelinda won't close an account while the debtor might still explain it."))

H = "hepzamirah.trickster."
partner("hepzamirah", "hepzamirah", "hepzamirah.committed", "hepzamirah.closed", "The Lodger",
    '''Hepzamirah lived in the body Mutasafen grew her for as long as it lasted, which was, to his lasting irritation, a great deal longer than he had designed it for. She paid her rent to the Commander in the form she preferred, which was a standing threat to kill her father and an invitation to watch.''',
    (
        page_p('''Mutasafen came for his price, and she received him herself, and she paid him in full. She said she would not owe that creature a single drop. She said it smiling, and nobody who saw the smile asked what the payment had been.''', requires=(called("hepzamirah"),)),
        page_p('''She had killed Mutasafen's courier once, because the Commander let her, and she remembered it fondly. She said it was the nicest thing anyone had ever done for her.''', requires=(H + "cost.courier_killed",)),
        page_p('''The Commander had broken her terms once, sending a chaplain to heal her against her will. She never let that go. She lived at the Commander's side and kept the healed scar uncovered, where {mf|he|she} would see it every time {mf|he|she} looked at her, and she made sure {mf|he|she} looked.''', requires=(H + "cost.healed_against_terms",)),
    ),
    deal=[[H + "cost.favour_owed"], [H + "cost.mutasafen_grudge"], [H + "cost.lab_funded"], [H + "cost.blood_sample"], [H + "cost.vial_paid"],
          [H + "cost.vial_forged"], [H + "cost.baphomet_grudge"]],
    call=call('''[Call in the rent] "Rent's due: a front-row seat when you kill your father. I'll need to be alive for it."''',
        '''{n}A long way off, in a body grown for her in a laboratory she will not name, Baphomet's favourite daughter laughs, and the sound carries.{/n}''',
        (PILLAR_CHOICE, (PILLAR,), (), ())))

E = "eritrice.trickster."
partner("eritrice", "eritrice", "eritrice.committed", "eritrice.closed", "Motion Carried",
    '''Eritrice kept the Trickster Council's minutes for as long as there was a Council, and a little longer, because she said somebody had to be ready when it reconvened. Every entry after Threshold began the same way: "Present: the chair, the Commander (irregularly)."''',
    (
        page_p('''At the rift the Commander moved a last motion from the floor: that {mf|he|she} was not dead. Eritrice minuted it. The motion carried, by a majority of one, and the record shows the chair abstained.''', requires=(called("eritrice"),)),
        page_p('''The grudge stood on every agenda, read aloud before any other business. The Commander was always there to hear it, and always sat at the foot of the table while it was read.''', requires=(E + "cost.grudge_on_agenda",)),
        page_p('''She had caught the Commander lying once, in the private debate, and the matter was never struck from the record. She raised it whenever the Commander became too pleased with {mf|himself|herself}, which was often, and it was always in order.''', requires=(E + "cost.caught_lying",)),
    ), declined=E + "declined",
    deal=[[E + "cost.grudge_on_agenda"], [E + "cost.on_the_record"], [E + "cost.censured"], [E + "cost.apologised"]],
    call=call('''[Move a last motion] "I move that the Commander is not dead. All in favour?"''',
        '''{n}Somewhere a long way from the fire, a quill scratches across a page of minutes, and a voice that is used to being obeyed says: "Seconded."{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Eritrice: business still on the agenda", "The Trickster Council's minutes have my name in them, under a matter still open. Eritrice does not let a member die with business pending."))

AE = "areelu.trickster."
partner("areelu", "areelu", "areelu.committed", "areelu.closed", "The Wager, Settled",
    '''I will record, since I am obliged to record everything, that the wager was settled. Whoever burned at Threshold was to pay. I have gone over the terms many times since, looking for the flaw, and I have not found one, which is the most irritating thing I can say about any experiment.''',
    (
        page_p('''At the rift the Commander called in our wager, and told me to take notes. I did. They are appended. They are very thorough.''', requires=(called("areelu"),)),
        page_p('''I ceded the Wound. I have not regretted it, which I record here because I promised to regret nothing, and I keep my promises when they are also my conclusions.''', requires=(AE + "cost.wound_ceded",)),
        page_p('''The flask is mine. I made it. The Commander carries it. I have not tried to take it back, and I would like whoever reads this to understand how much that restraint costs me.''', requires=(BOTTLED,)),
    ), declined=AE + "declined",
    deal=[[AE + "cost.bet_with_the_witch"], [AE + "wager_struck"]],
    call=call('''[Call in the wager] "Whoever burns at Threshold pays up. Watch closely, Areelu. You'll want notes."''',
        '''{n}Across the rift, Areelu Vorlesh folds her one hand over the wrist that has none, and watches you the way she has watched you since Iz: as a result she has not finished recording.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Areelu: a wager on who burns", "Whoever burns at Threshold pays. Areelu keeps better records than I do. I intend to be the one reading them afterwards."))

CH = "chadali.trickster."
partner("chadali", "chadali", "chadali.committed", "chadali.closed", "Heads",
    '''Chadali kept the coin. It had stood on its edge through the Council, through Threshold and through the long night after, and she would not let anyone knock it over. She kept it on the windowsill of the Commander's rooms, still balanced, and dusted around it.''',
    (
        page_p('''At the rift the Commander called in the luck she had borrowed, and she paid it back all at once, the way she did everything. The coin fell. She would never say which face it showed. The Commander has asked her every week since, and every week she says "No." and looks delighted.''', requires=(called("chadali"),)),
        page_p('''The needle was the Commander's, as promised, the next time. Chadali held {mf|him|her} to it the first time {mf|he|she} was ill after the war, and would not let anyone else near {mf|him|her} with a bandage.''', requires=(CH + "cost.needle_owed",)),
        page_p('''She never quite forgave the Council fight. She sulked for a season at the far end of every table, bossy and odious, and then one morning she moved her chair back without comment and demanded breakfast.''', requires=(CH + "cost.grudge",)),
        page_p('''The orange tree grew in the best corner of the citadel garden, and bore fruit the second year. She said that proved nothing, and ate all of it.''', requires=(CH + "cost.orange_tree",)),
    ), declined=CH + "declined",
    deal=[[CH + "cost.luck_lent"], [CH + "cost.luck_owed"], [CH + "cost.needle_owed"]],
    call=call('''[Call it in the air] "Chadali, you borrowed my luck. I need it back. Now, please."''',
        '''{n}Somewhere a coin that has been standing on its edge for a very long time begins, very slowly, to tip.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Chadali: my luck, on loan", "Chadali borrowed my luck, or I borrowed hers. The coin's still standing. Nobody collects from a dead man's luck."))

CA = "camellia.trickster."
partner("camellia", "camellia", "camellia.committed", "camellia.closed", "The New Moon",
    '''Camellia Gwerm wore black to the victory feast, since nobody could tell her which of the dead she was allowed to mourn, and she brought lilies to the Commander's door the morning after the rift: white ones, the wedding kind, left on the step with a card that said only that she had been told the Commander liked a performance.''',
    (
        page_p('''At the rift the Commander called in the new moon, and the spirits that had been fed on {mf|his|her} blood all winter came for the rest of what they were owed. Camellia would not let them take it for themselves. She held the bowl and made the cut, one last neat one, exactly where a friend would stand, and the voices in her head went quieter than she had ever heard them. They stayed quiet a month. She hated every day of it, and was delighted when they came back.''', requires=(called("camellia"),)),
        page_p('''The Commander had come to her coffin late, with a sexton's lantern and a purse of gold, after the spirits had had three days alone with her. She never forgot the sound of the coins. For a season she took her supper at the far end of the table, with her knife beside her own plate instead of the Commander's, and watched {mf|him|her} eat the way she read a bad notice. Then one evening the knife was back beside the Commander's plate, which in Camellia's house is how a lady admits that someone has been forgiven.''', any_groups=((CA + "cost.late", CA + "cost.bargain_late"),)),
        page_p('''Two names now stood in the crusade's register of the dead, hers and the Commander's, a few leaves from each other. She had the clerk copy both onto one sheet and framed it over the bed. She said she had always wanted a {mf|husband|wife} nobody could accuse her of murdering.''', requires=(ON_RECORD,)),
        page_p('''She knew about the flask. She asked to hold it only once, and weighed it in her palm the way she weighs a stranger's throat, and gave it back. "Your death, corked," she said. "How very courteous of it, to wait for you."''', requires=(BOTTLED,)),
    ), declined=CA + "declined",
    deal=[[CA + "cost.blood_bargain"], [CA + "cost.spirits_owed"]],
    call=call('''[Call in the new moon] "Camellia's spirits, you've had my blood every dark of the moon. Come and collect the rest, from the living."''',
        '''{n}The fire gutters, though there is no wind. Somewhere a lady in black sets down a small clean knife beside an empty bowl, and a great many voices that are not hers lean in to listen.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Camellia: blood at the new moon", "Her spirits have my blood on account, a little each dark of the moon. She says they are very good at keeping count. So, I'm afraid, is she."))

# Existing pages that must yield to Last Call (doc 04 backlog): Nocticula's favour page is called in on her Last Call page instead.
FORBID_ACTIVE = ("nocticula.trickster.defeated.epilogue.favour",)


def derived():
    return {"lastcall.tirabade.both_returned": [["irabeth.trickster.returned", "anevia.trickster.returned"]]}


def call_in_scenes(factory):
    out = []
    for part in PARTNERS:
        if not part["call"]:
            continue
        spec = part["call"]
        # extra=None leaves the line unspoken (Targona's promise kept): the debt is resolved without being called.
        choices = [c(text, flags=(resolved(part["rel"]),), requires=req, forbids=forb) if extra is None
                   else c(text, flags=(called(part["rel"]), resolved(part["rel"])) + tuple(extra), requires=req, forbids=forb)
                   for text, extra, req, forb in spec["choices"]]
        node = n("call", "Narrator", spec["text"], *choices)
        # Offered on any deal her route produced, whether or not the romance committed (ledger 05 row 11: every debt is
        # called in once). The coda still needs the commit.
        any_groups = [sorted({k for g in part["deal"] for k in g})]
        out.append(factory(part["rel"] + ".lastcall.call", "Last orders", spec["entry"], [node],
                           requires=(), forbids=(resolved(part["rel"]),), any_groups=any_groups))
        # G5 (doc 04 §5.2): the framework reads other routes' committed and cost flags only, never a closed, death or return flag.
    return out


def open_debts():
    """(deal flag, resolved flag) for every call-in: the last joke Forbids each deal flag until its call-in is resolved."""
    return [(k, resolved(part["rel"])) for part in PARTNERS if part["call"] for g in part["deal"] for k in g]


def pages():
    """Block B. Every page belongs to the framework relationship (lastcall), as do the call-ins: the routes' own suites keep
    judging their routes, and LastCallTests judges these. `Partner` names the route each page codas, for placement.
    G5: a page reads its partner's committed, declined and cost flags, never her closed, death or return flags."""
    out = []
    for part in PARTNERS:
        forbids = ((part["declined"],) if part["declined"] else ()) + part["page_forbids"]
        extra = dict(Relationship="lastcall")
        if part["declined"]:
            extra["ForbidOverrides"] = {part["declined"]: part["commit"]}
        page = scene(part["key"] + ".lastcall.page", part["title"], "Epilogue", 1, "", [
            n("page", "Narrator", part["opener"], paragraphs=part["paragraphs"])],
            requires=("trickster.ever", ACTIVE, part["commit"]), forbids=forbids, last=99, **extra)
        out.append((part["rel"], page))
    return out

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
    dict(key="ramisa", groups=[["nurah.trickster.cost.ramisa_audience"], ["nurah.trickster.cost.bill_in_your_name"]],   # gold alone owes nothing
         called_by=[called("nurah")],
         ledger_title="Ramisa Shed-Skin: the only seat",
         ledger_text="The marilith keeps the other copy of the bill I made out in her market. Either she already owns the only seat at the last night of the war, or she will want it in exchange for that copy. She will want her performance.",
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
    dict(key="nocticula_summons", groups=[["arueshalae.trickster.cost.nocticula_debt"], ["arueshalae.trickster.cost.nocticula_favour"]],
         called_by=[called("arueshalae")], outlived=["trickster.lastcall.summons_outlived"],
         ledger_title="The Lady in Shadow: one summons, for a succubus",
         ledger_text="I sent Arueshalae to her queen for a second opinion, and the queen sent her back on credit. One summons, once, at an hour of the Lady's choosing, or a favour in my own name. The Lady in Shadow does not forget a patient.",
         page_called="The Lady in Shadow called in her summons on a night in the first winter after Threshold, when the Commander was away. The black pearl at Arueshalae's throat went warm, and she went, as she had said she would. What the queen asked of her, and what she answered, she never told. She came back before dawn with the pearl gone cold and a flower of the Midnight Isles in her hair, and she left the window unlocked behind her, as she always did.",
         page_outlived="The debt had no one left to collect it. Arueshalae knew that, and for a week she said nothing to anyone. Then she went to the Commander anyway, and it was the first thing she ever did that she owed no one for."),
    # Elyanka (11 §2 R5): the Commander's body, sold to the Whispering Way at the wake, due at death. A live power: the
    # bottle cheats it by the letter (the death is corked and never falls due), and the page says so.
    dict(key="whispering_way", groups=[["elyanka.trickster.cost.corpse_bequeathed"]], called_by=[called("elyanka")],
         ledger_title="The Whispering Way: my body, at my death",
         ledger_text="Sold at my own wake to Elyanka Camilary, for her Lady's table, whole, due the day I die. The soul stays the grey warden's; the Way does not want it. Nothing was written. The terms were whispered into my ear, and I whispered them back.",
         page_called="The Whispering Way's collector came after Threshold as a man in grey who spoke in the voice of the envoy who had bought the claim. He presented it in a whisper, word for word as it had been sold, and was told that the debtor's death was in a flask, corked, in the debtor's pocket, and that the terms had said nothing about flasks. He agreed, in her voice, that they had not, and went away to repeat the answer to her. In Caliphas the Way does not forgive a debtor who cheats it by the letter. It does, she let it be known, admire one."),
]


# --- Partners: the call-in line at the rift and the coda page ---------------------------------------------------------------

def page_p(text, requires=(), forbids=(), any_groups=()):
    return p(text, requires=requires, forbids=forbids, any_groups=any_groups)


PARTNERS = []


def partner(key, rel, commit, closed, title, opener, paragraphs, declined=None, page_forbids=(), deal=(), call=None,
            call_commit=None, ledger=None, page_commit_groups=None):
    """page_commit_groups (optional): the page plays on any of these commitment states instead of `commit` alone (R2-6: a
    route's late_committed key); `commit` stays first."""
    PARTNERS.append(dict(key=key, rel=rel, commit=commit, closed=closed, title=title, opener=opener, paragraphs=paragraphs,
                         declined=declined, page_forbids=tuple(page_forbids), deal=[list(g) for g in deal], call=call,
                         call_commit=call_commit or [[commit]], ledger_title=ledger[0] if ledger else None,
                         ledger_text=ledger[1] if ledger else None,
                         page_commit_groups=[list(g) for g in page_commit_groups] if page_commit_groups else None))


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
        page_p('''The cauldron went back across her counter as leased. She was there when it did, with a receipt, and when the clerks of Abadar asked what the Worldwound was now worth as collateral, she told them "Slightly used," and would not be moved.''', requires=(called("arsinoe"),), forbids=("arsinoe.siphon_burst",)),
        page_p('''The cauldron was handed back at the rift as leased, a breath before it burst, so that what burst was the temple's property, consumed in the course of its intended use. She entered the discharge with a receipt, and when the clerks of Abadar asked what the Worldwound was now worth as collateral, she told them "Slightly used," and would not be moved.''', requires=(called("arsinoe"), "arsinoe.siphon_burst")),
        page_p('''The Fool King's still had been pledged, a barrel baron and everything it guarded. The First Vault now holds a lien on the best-loved tap in Drezen. Arsinoe audits it in person on the first of every month, and has never once been seen to leave before the audit was complete, or sober.''', requires=(AR + "cost.collateral_still",)),
        page_p('''The Commander's word had been the collateral. Abadar's clerks entered it at face value, which amused them, and then found that it held, which did not.''', requires=(AR + "cost.collateral_word",)),
        page_p('''The First Vault does not recognize death as grounds for default, nor as grounds for refusing a payment from the deceased. She took the Commander's anyway, and entered it without comment.''', requires=(ON_RECORD,)),
    ), deal=[[AR + "cost.lien"], [AR + "cost.collateral_worldwound"], [AR + "cost.collateral_still"], [AR + "cost.collateral_word"]],
    call=call('''[Return the cauldron] "Returnable at the end of the world. This is the end of the world. Here."''',
        '''{n}Somewhere under the roar, you swear you hear an abacus. The First Vault has a claim on this night, and the First Vault is always present at the end of an account.{/n}''',
        (PILLAR_CHOICE, (PILLAR,), (), ())))

J = "jerribeth.trickster."
# Sol COX: the coda owns the single forfeit when Last Call plays (her ordinary endings forbid lastcall.active); rent is
# only a tenant's; the idol is read from body.statue; the call-in answers what she actually is (tenant, toasted, living).
partner("jerribeth", "jerribeth", "jerribeth.committed", "jerribeth.closed", "Rent Day",
    '''Jerribeth came to the victory feast uninvited, which she considered the only honest way to attend one, and stayed until the last candle, counting who had drunk to whom. She never once let the Commander forget what was owed, and to whom. She was, in the opinion of everyone who met her, entirely too pleased with herself.''',
    (
        page_p('''She collected her rent on the first of the month after Threshold, as the lease said, and on every first of the month after that: one small memory, her choice, taken in lieu of repairs. She never let the Commander forget whose house she was living in.''', requires=(J + "cost.tenant",)),
        page_p('''She took her forfeit in the second year: one memory, hers to choose. She chose the rift. The Commander remembers everything about Threshold except the joke itself, and she tells it back, badly, on purpose, whenever {mf|he|she} asks.''', requires=(J + "cost.forfeit",)),
        page_p('''She had worn a deserter from the stockade since the first night the Commander slept in Drezen after giving him to her, and she wore him to the victory feast. Nobody missed him. She made a point of telling the Commander how right {mf|he|she} had been about that.''', requires=(J + "cost.host",)),
        page_p('''The gilt idol of the Lady of the Sun was carried to the victory feast on a handcart, at her insistence, and set at the Commander's right hand. It did not eat. Everyone who sat near it lost a little money that night and could not afterwards say how.''', requires=(J + "body.statue",)),
        page_p('''She sent the man she had taken in payment for the toast to pour the Commander's cup at the feast, smiling two finger-widths too wide. The toast had been paid for, she said, and she liked to see her property used.''', requires=(J + "cost.toast_host",)),
        # R2-6 (Sol r3): the late history (commission reached, no campaign commitment) plays this coda too. Whether the
        # contract is signed is the epilogue page's question; this line holds whichever answer is given there.
        page_p('''There was no contract yet, only one she had drafted and left on the Commander's table, the clause she was saving written in very small, very neat print. She came to the feast anyway, uninvited, to watch the Commander not sign it. Whether the Commander ever would was a question she asked every spring, and she enjoyed the asking more than she would have enjoyed an answer.''', requires=(J + "late_committed",), forbids=("jerribeth.committed",)),
    ), declined=J + "declined", page_forbids=(J + "parted",),
    page_commit_groups=[["jerribeth.committed"], [J + "late_committed"]],
    deal=[[J + "cost.tenant"], [J + "cost.lodger"], [J + "cost.host"], [J + "cost.toast"], [J + "cost.forfeit"]],
    call=call('''[Call in Jerribeth's paper] "Lady of the Sun. You hold paper on me. Collect it from a living debtor, or not at all."''',
        '''{n}For a moment nothing answers. Then a buzzing, very faint, like a fly against glass a long way off, and the smell of cold stone under the smoke of the rift.{/n}''',
        ('''"Rent's due, tenant. A house doesn't fall down while you're living in it."''', (), (J + "cost.tenant",), ()),
        ('"You were toasted, madam, by a stranger. A toast is a debt. Come and collect it after tonight."', (), (J + "cost.toast",), (J + "cost.tenant",)),
        ('"One memory, your choice, when you choose. Choose after tonight. I want to have something worth taking."', (), (J + "cost.forfeit",), (J + "cost.tenant", J + "cost.toast"))),
    ledger=("Jerribeth: paper held on me", "Jerribeth holds paper on me: a lease, a toast, or a forfeit clause. She reads small print better than I write it, and she collects in person."))

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
    '''Nurah Dendiwhar published her account of the Fifth Crusade two years after Threshold. It sold out in Nerosyan in a week and was banned in Mendev in two. The chapter on the Commander was the longest in the book, and the only one in which she admitted to liking anyone.''',
    (
        page_p('''Ramisa came for the story she had bought. Nurah wrote it for her in a single night, every word true, and dedicated it to the marilith "with the author's compliments and none of her gratitude". The duplicate bill with the Commander's name on it went into the fire the same night. Nurah insists she has no idea how.''', requires=(called("nurah"), NU + "cost.bill_in_your_name")),
        page_p('''Ramisa came for the story she had bought, and Nurah wrote it for her in a single night, every word true, and dedicated it to the marilith with the author's compliments and none of her gratitude.''', requires=(called("nurah"),), forbids=(NU + "cost.bill_in_your_name",)),
        page_p('''She never forgot being currency, and she never pretended to. She kept the memory the way she kept her pen: close, sharp, and pointed at anyone who looked as if they might try it again.''', requires=(NU + "cost.larva_memory",)),
        page_p('''Her name went on the cover next to the Commander's. She had insisted. She was right to.''', requires=(NU + "cost.coauthor",)),
        page_p('''Her name went on the cover above the Commander's, in larger letters. She had insisted. The Commander had let her.''', requires=(NU + "cost.name_above",)),
        page_p('''She wrote the Commander's obituary herself, for a Nerosyan broadsheet. It was vicious, accurate and extremely popular.''', requires=(ON_RECORD,)),
    # Sol quality pass (Nurah TRK/BEL): a soul paid for in gold leaves no debt, so the call-in is offered only on the story
    # she sold (ramisa_audience) or on the duplicate bill Ramisa kept; for the bill alone the story is sold here, on screen,
    # against that bill (trickster.lastcall.nurah_story_sold), and the page's first paragraph burns it.
    ), deal=[[NU + "cost.ramisa_audience"], [NU + "cost.bill_in_your_name"]],
    call=call('''[Call in the custom order] "Madam Shed-Skin, you wanted art. I'm about to make some. Front row."''',
        '''{n}A mirror in a slave market somewhere in the Abyss clears, like breath wiped from glass, and something with a great many arms settles in to watch.{/n}''',
        (PILLAR_CHOICE, (PILLAR,), (NU + "cost.ramisa_audience",), ()),
        ('''"Front row, for the duplicate bill with my name on it. You burn it when the curtain falls."''',
         (PILLAR, "trickster.lastcall.nurah_story_sold"), (NU + "cost.bill_in_your_name",), (NU + "cost.ramisa_audience",))),
    # R2-6: the late courier and the late pedlar commit on the epilogue page; their coda plays on the late key.
    page_commit_groups=[[NU + "coda_alive"]])

KI = "kiana.trickster."
partner("kiana", "kiana", "kiana.committed", "kiana.closed", "Home by Spring",
    '''Kiana did not go back to Mendev after the war. She stayed in Drezen, where nobody had arranged her marriage and nobody had put her soul in a jewel, and she took a room above a baker's with a window that looked at nothing in particular. She said it was the first view she had ever chosen.''',
    (
        page_p('''The wedding guests still in Sunhammer's keeping came home that spring. Kiana met every coach. She knew all their names, and she made the Commander learn them too.''', requires=(called("kiana"),)),
        page_p('''She never quite forgave the Commander the guests left behind in the pouch the first time, when {mf|he|she} was quicker to free her than to count the others. She said so once, plainly, and never needed to again.''', requires=(KI + "cost.guests_robbed",), forbids=(called("kiana"),)),
        page_p('''The counterfeit that had stood in for her stone went back to Sunhammer's bench in his apprentice's hand. Kiana liked to imagine the day he put a loupe to it, and made the Commander imagine it with her.''', requires=(KI + "cost.counterfeit_spent",)),
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
        page_p('''The knot still held, retied, one end in Soana and the other round the Commander's wrist where the gut strip had marked it. On hungry nights it pulled. The Commander learned to sleep through it, which Soana said was the most romantic thing anyone had ever done for her.''', requires=(S + "cost.guardian_paid",)),
        page_p('''The spirits came for their portion, and Soana stood between them and the Commander, and paid them in her own blood. She did not say it was for love. She said it was her wood and her debt, which is how Soana says it.''', requires=(called("soana"),)),
        page_p('''She kept the die in the bowl by her hearth, the one the Commander had left there, and rolled it when she could not decide something. It only ever came up one way, which was the lead in it, and she said that was the point: it saved her the trouble of pretending she had not already decided.''', requires=(S + "cost.die_in_her_bowl",)),
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
partner("gesmerha", "gesmerha", "gesmerha.committed", "gesmerha.closed", "Work on the Bench",
    '''Gesmerha heard the news of Threshold the way she heard everything, by the step of the one who carried it. She said afterwards that she knew before the messenger opened his mouth: he walked like a man who had been told one thing and did not believe it. She sent him away without letting him finish, and went back to her bench.''',
    (
        # The Commander's face, the second work on her bench (gesmerha_trickster 4g), in its three states. The ancestors' own
        # commission (the monster or the listening woman) was finished before Threshold and is not retold here.
        page_p('''The Commander's face had waited on her bench all winter under a knotted cloth, finished but for the eyes. In the spring she sat the Commander down in the smith's yard with a blindfold on, put her left hand over the living face and the chisel in her right, and cut the last of it by touch, a stroke at a time, stopping whenever the face under her hand moved. When it was done she let nobody see it, except the Commander, still blindfolded, by touch, the way she had carved it. {mf|He|She} said afterwards that it was the only honest likeness anyone had ever made of {mf|him|her}.''',
               requires=(G + "cost.likeness_owed",)),
        page_p('''The face she had cut from memory before Threshold stood on the shelf over her bench, eyes and all. She had called it a grave-post. When the Commander walked into the yard in the spring, loudly, she took it down, turned it to the wall, and never turned it back.''',
               requires=(G + "cost.likeness_cut",)),
        page_p('''The face she had begun on the morning after the night in the yard was still on her bench, a little further along each season. It was not a commission, she said, so it could take as long as it liked, and so could its owner.''',
               requires=(G + "cost.ancestor_debt",), forbids=(G + "cost.likeness_owed", G + "cost.likeness_cut")),
        page_p('''The commission paid for in Wintersun, before Marhevok's ambush, was still on her bench at Threshold: the pale birch with the Commander's coin standing proud of the grain. The Commander had called it in at the rift. She took that the way she took every order, which is to say she took her time. A commission is a commission, she said, not a summons.''',
               requires=(G + "cost.advance_paid", called("gesmerha")), forbids=(G + "cost.ancestor_debt",)),
        page_p('''The commission paid for in Wintersun, before Marhevok's ambush, was still on her bench at Threshold: the pale birch with the Commander's coin standing proud of the grain. Nobody asked her for it, and she did not hurry. A commission is a commission, she said; it would be finished when the wood agreed.''',
               requires=(G + "cost.advance_paid",), forbids=(G + "cost.ancestor_debt", called("gesmerha"))),
        page_p('''She kept the carved hands, the ones she had made while the Commander sat for her those three days. They stood on her bench for the rest of her life, and she worked with them facing her, and she would not say why.''', requires=(G + "cost.hands_carved",)),
        page_p('''The Commander had laughed at her grave. She delivered the work, and then she sat apart from the Commander at supper for a whole season, where she could hear {mf|his|her} footsteps and not {mf|his|her} voice. At the end of the season she moved her chair back, and told {mf|him|her} the footsteps had improved.''', requires=(G + "cost.laughed_at_grave",)),
        page_p('''She cut the marker for the Commander's empty grave, in oak. It said nothing untrue.''', requires=(ON_RECORD,)),
    ), declined=G + "declined", page_forbids=("gesmerha.parted",),   # a lover who parted, or told her to finish her life without them (never her closed flag, G5)
    # R2-6: the page also plays on the returned route's epilogue commit (gesmerha.trickster.late_committed, trickster_world).
    page_commit_groups=[["gesmerha.committed"], [G + "late_committed"]],
    deal=[[G + "cost.advance_paid"], [G + "cost.ancestor_debt"]],
    # The call tells the work as it stands: unfinished (the living advance, or a face left for its sitter), or a face already
    # cut from memory. Leaving it unspoken resolves the debt too, so the last joke never waits on an answer she cannot give.
    call=call('''[Call to the carver] "Gesmerha! Listen for this step."''',
        '''{n}Somewhere a long way off, a woodshaper sets down her chisel and turns her head toward a step she knows, as if it had just come in at her gate.{/n}''',
        ('"There\'s work of mine still on your bench, carver. Leave it there until I come to collect."', (), (), (G + "cost.likeness_cut",)),
        ('"The face is finished, carver. Turn it to the wall. I\'m not done with the one it was cut from."', (), (G + "cost.likeness_cut",), ()),
        ("[Leave it unspoken. She will finish her work in her own time.]", None, (), ())),
    ledger=("Gesmerha: a step she listens for", "Gesmerha listens for my step. If there is work of mine unfinished on her bench, her line will not leave it that way; if it is finished, she will want the one it was cut from to come and see it."))

SE = "seelah.trickster."
partner("seelah", "seelah", "seelah.committed", "seelah.closed", "The Thief's Promise",
    '''Seelah did not go back to the order after the war. She said she had a debt to settle first, and she settled it the way she had settled things as a girl in the streets of Solku: quietly, with a hand in someone else's pocket, and an apology afterwards.''',
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
    ledger=("Seelah: a list to steal back", "At her bier I took Seelah's list of old thefts out of her purse, and robbed a grave-robber off its last line to pay for her. She swore she'd steal the list back. A thief who hasn't collected won't let you die."))

T = "targona.trickster."
partner("targona", "targona", "targona.committed", "targona.closed", "The Quiet Ward",
    '''Targona did not go back to Heaven when the war ended. She stayed in Drezen's infirmary until the last cot was folded, and then she opened another, in a street near the Commander's house, with the Commander's name over the door and no way for {mf|him|her} to be useful in it.''',
    (
        page_p('''The Commander kept the promise at the rift. {mf|He|She} did not call on her brother's light, though it would have been the easiest thing in the world, and she heard afterwards that {mf|he|she} had not. She did not say anything. She put a second chair by her desk in the ward, and it was never empty for long.''', requires=(T + "cost.light_sealed",), forbids=(called("targona"),)),
        page_p('''At the rift the Commander called on Lariel's light, and broke the one promise she had asked of {mf|him|her}. She learned of it within the week. She stayed; an angel keeps her word even when others do not. But she sat at the other end of the ward's table for a year, and it was a year before she let the Commander carry a lamp for her again.''', requires=(called("targona"), T + "cost.light_sealed")),
        page_p('''She had told Heaven everything, as her price for coming back. Heaven, it seemed, had listened, and had not recalled her. She took that as an answer and did not ask for another.''', any_groups=[[T + "cost.she_told_heaven", T + "cost.raised_openly"]]),
        page_p('''She never forgave the joke at her bier, and she never pretended to. She served beside the Commander for the rest of her long life, courteous, exact, and always at the far end of any room they shared.''', requires=(T + "cost.unforgiven",), forbids=(T + "forgiven",)),
        page_p('''She forgave the joke at her bier in the end, when it had been apologised for properly, but she never forgot it. Some evenings she would bring it up at table, precisely, word for word, and watch the Commander wince, and then pour the wine.''', requires=(T + "cost.unforgiven", T + "forgiven")),
    ), declined=T + "declined",
    deal=[[T + "cost.raised_openly"], [T + "cost.she_told_heaven"], [T + "cost.raised_the_hard_way"], [T + "cost.light_sealed"]],
    call=call('''[Call on Lariel's light] "Lariel, whatever of you is left in me: one more quiet miracle."''',
        '''{n}Something warm and patient moves under your ribs: a light that belongs to someone's brother, that went into you in the rock under Kenabres and never quite became yours.{/n}''',
        (PLAIN_CHOICE, (), (), (T + "cost.light_sealed",)),
        ('''[Break your promise to Targona] "Forgive me. I need it."''', (), (T + "cost.light_sealed",), ()),
        ("[Keep your promise] Leave the light where it is.", None, (T + "cost.light_sealed",), ())),   # resolves, not called
    # Sol quality pass (Targona INT): RanRomance's own Targona romance, completed through its Angelic Treatment on this
    # path, is a commitment for the coda too (targona.trickster.parent_romanced; its correspondence never sets committed).
    page_commit_groups=[["targona.committed"], [T + "late_committed"], [T + "parent_romanced"]])

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


AU = "arueshalae.trickster."
partner("arueshalae", "arueshalae", "arueshalae.committed", "arueshalae.closed", "Treatment, Continued",
    '''Arueshalae was waiting in the Commander's rooms in Drezen when the news of Threshold came in, sitting very straight on the edge of the bed with her hands behind her back, the way she had sat through every bad hour of the war. She did not ask whether the Commander was alive. She had decided not to ask anyone anything until she could take a pulse herself.''',
    (
        page_p('''When the summons came she went, as she had promised, and came back before dawn with the pearl at her throat gone cold. She never said what she had chosen. The window was never locked again.''',
               requires=(called("arueshalae"), AU + "cost.nocticula_debt"), forbids=("trickster.lastcall.summons_outlived",)),
        page_p('''The Commander paid the queen's favour in person, with Arueshalae watching from the doorway, as she had said she would. She wanted to see a Trickster's face while the Trickster was being collected. She told the Commander afterwards that it had been worth every day of waiting, and would not describe it to anyone.''',
               requires=(called("arueshalae"), AU + "cost.nocticula_favour"),
               forbids=("trickster.lastcall.summons_outlived", "nocticula.trickster.favour_called.arueshalae")),
        page_p('''The queen's favour had been paid long before, in her own court, with Arueshalae watching from the doorway as she had said she would. She brought it up at supper for years, whenever the Commander looked too pleased with a bargain.''',
               requires=(AU + "cost.nocticula_favour", "nocticula.trickster.favour_called.arueshalae")),
        page_p('''Nobody came to collect her summons. She waited a week to be sure. Then she stopped waiting, and it was the first thing in her long life that she ever did because she wanted to, and for no one.''',
               requires=("trickster.lastcall.summons_outlived",)),
        page_p('''The star-candle was lit every evening for the rest of their lives, in camp and in palace and once, memorably, in a thunderstorm on a ship's deck. The few nights it was not, the Commander woke with cold hands and a lost day, and found her sitting in the farthest corner of the room with her knees drawn up, and it took a week, each time, to coax her back.''', requires=("arueshalae.trickster.cost.drained",)),
        page_p('''She kept the arrangement to the letter: she came when she was hungry, and the door was open. Some months she was hungry more often than the arrangement strictly allowed, and the door was open then too.''', requires=(AU + "cost.open_door",)),
        page_p('''She renewed her vows at the altar rail every spring, and the Commander stood at the back with the second company and announced nothing at all, as promised.''', requires=(AU + "cost.no_staging",)),
        page_p('''She served as chaplain until the second company was disbanded, and she never resigned; nobody had ever given her the chance, and she did not intend to take it now.''', requires=(AU + "cost.chaplain",)),
        page_p('''The Commander had promised her no more doctoring in her sleep, and she held {mf|him|her} to it by never once dying again, which she said was the only reliable way to keep a Trickster honest.''', requires=(AU + "cost.no_second_joke",)),
        page_p('''The Commander had asked only for the good days, and on the good days she came to supper. On the others she ate alone, at the far end of the table, where the Commander had put her, and was very polite about it for a very long time. It was a price, and she paid it at the table, apart, until the Commander finally went and sat at that end too.''', requires=(AU + "cost.saint_only",)),
        page_p('''The world buried the Commander. Arueshalae sat through the funeral with her hands behind her back and did not cry, because she had taken the Commander's pulse that morning and knew exactly how the joke ended.''', requires=(ON_RECORD,)),
        page_p('''When the flask was opened in Drezen, she was the one who took the first pulse, and she held the wrist long after she had counted it.''', requires=(H2,)),
    ), declined=AU + "declined",
    deal=[[AU + "cost.nocticula_debt"], [AU + "cost.nocticula_favour"]],
    call=call('''[Call in the second opinion] "Your Majesty, you sent her back on credit. Collect your summons tonight. I'll be here to be collected from."''',
        '''{n}A long way off, a black pearl on a string goes warm against a succubus's throat. She puts her hand over it and does not look at you, and does not take it away.{/n}''',
        (PILLAR_CHOICE, (PILLAR,), (), ("noct.dead",)),
        (PLAIN_CHOICE, (), ("noct.dead", "noct.defeated_not_dead"), ()),
        (PLAIN_CHOICE, ("trickster.lastcall.summons_outlived",), ("noct.dead",), ("noct.defeated_not_dead",))),
    ledger=("Arueshalae: a patient under treatment", "Arueshalae is still my patient. A doctor who dies before the treatment is finished is no kind of doctor at all."))

DL = "delamere.trickster."
partner("delamere", "delamere", "delamere.committed", "delamere.closed", "First Frost",
    '''Delamere the Blessed did not wait in Drezen for news of Threshold. She did not like waiting in cities, and she did not believe news. She went up onto the ridge above her temple with her bow and a hare on a green stick, and watched the northern sky change colour, and counted, the way she counts everything, until something in it came out right.''',
    (
        page_p('''At the rift the Commander blew the old Kellid horn one last time, the three barks and the long broken roar, over the edge of the world. Far off, over woods that had heard it only twice, a woman got up from a dead fire and answered. She came for her day at the rift's edge, and hunted the Commander back across a broken country for three days and three nights, as she had once hunted a white stag, and caught {mf|him|her} at the gate of Drezen in front of the whole cheering garrison, and did not finish it.''', requires=(called("delamere"),)),
        page_p('''The Commander walked crooked for the rest of {mf|his|her} life, in the stag-hide brace she had cut for it, and relaced every autumn when the old one wore through. She kept the knotted cord she had measured the leg with. She said it was in case the Commander grew. {mf|He|She} never did, and she never gave it back.''', requires=(DL + "hide_brace",)),
        page_p('''The Commander walked crooked for the rest of {mf|his|her} life. She never apologised for it. Every autumn she looked at the leg the way a smith looks at a blade she forged years ago, and said it had set well.''', requires=(DL + "cost.limp",), forbids=(DL + "hide_brace",)),
        page_p('''The world buried the Commander. Delamere did not go to the funeral. She said that she had lain in a stone box for longer than anyone living, and that she knew the difference between a beast that was dead and a beast that was only lying very still, and that a good hunter waits.''', requires=(ON_RECORD,)),
        page_p('''When the flask was opened in Drezen she was standing at the back of the room with an arrow on the string, not because she meant to loose it, but because she had once stood like that for a very long time, and she wanted whatever came out of the flask to see it.''', requires=(H2,)),
    ), declined=DL + "declined",
    deal=[[DL + "cost.hunt_owed"]],
    call=call('''[Sound the horn] "Delamere! You're owed a day. Come and collect it."''',
        '''{n}The horn is at your belt; it has been there since the crypt. The roar goes out over the rift, three barks and the long broken one, and is swallowed. Then, very far off, over woods that have heard it only twice before, something answers.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Delamere: one day, owed", "I asked a huntress for another day, and she gave it to me on account. She keeps the right to take it back whenever she likes. I walk crooked so that neither of us forgets."))

NI = "nidalynn.trickster."
partner("nidalynn", "nidalynn", "nidalynn.committed", "nidalynn.closed", "Of Her Fire",
    '''Nidalynn did not wait in Drezen for news of Threshold, and she did not go north. She banked the kiln under the east wall as high as it would go, and sat on its step through the whole of that night with bread and salt in her lap, feeding the fire, the way old Reudger, she said, used to sit up for a rider late home in a snowstorm. The young dragon sat beside her and would not go to sleep.''',
    (
        page_p('''At the rift the Commander called across the broken ground with a long rising herding-shout, the kind that brings mares home over a great distance, with her name at the end of it, and far off to the south something silver came up out of the clouds over Drezen and answered it, and came. She landed on the lip of the world with a young red-black dragon screaming at her heels, and took one look at what was left of the Commander, and said that the soup was getting cold.''', requires=(called("nidalynn"),)),
        page_p('''The Commander never found out what she would have done if the flask had not held. She would not say. She said a silver does not tell a trickster what she would have done if the trick had failed, because the trickster would only use it next time.''', requires=(ON_RECORD,)),
        page_p('''When the flask was opened in Drezen she was standing at the back with a loaf under her arm, because somebody would be hungry after, and she was right.''', requires=(H2,)),
        page_p('''The young dragon flew up the north ridge that summer, alone, to the grey tower, and came back three days later and would not say where she had been. The grey one's bill still stood. Nidalynn said it was only manners to leave it standing, and that she would be there when it was called.''', requires=("devarra.trickster.cost.egg_withheld",)),
    ), declined=NI + "refused",
    deal=[[NI + "cost.salt_eaten"]],
    call=call('''[Call across the snow] "Nidalynn! I've your salt in me yet. Come and see."''',
        '''{n}You have heard her hum it at the kiln: the long rising herding-shout that brought Reudger's mares home across the grass. You put her name at the end of it. You give it everything you have left. It goes out over the rift and is swallowed, and then, very far off, over a city you cannot see, something answers.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Nidalynn: salt, eaten", "I ate a silver dragon's salt at a lime-kiln. Among the Windstep that makes me of her fire until the salt is out of my blood, and she says it never comes out. The debt runs both ways. So she says."))

SH = "shamira.trickster."
partner("shamira", "shamira", "shamira.committed", "shamira.closed", "The Ardent Dream",
    '''Shamira the Ardent Dream did not come to Threshold. She sat her throne in the Harem of Ardent Dream with the court sent away and the fountains running, and held very still, with the night's coal of the Commander burning in her chest, and listened. Through it she could feel the Commander walk into the rift the way you feel a draught come under a door.''',
    (
        page_p('''At the rift the Commander thought of her, hard, the way the Commander had once thought of carpets. A long way off, on an empty throne, a woman who had been sitting very still stood up. For the space of one breath the Commander, awake, at the edge of the world, was not alone behind {mf|his|her} own eyes. Then {mf|he|she} was. It was enough.''', requires=(called("shamira"),)),
        page_p('''For three days after Threshold she did not come into the Commander's sleep, because there was no sleep to come into, and the coal in her went out, and she sat on her throne with her fingertips going white and would not let anyone light a fire. On the third night there was a dream again: the war tables, the lamps, the same argument about the same river crossing. She walked into it without knocking and sat down on a map chest and wept, which nobody who knew her would have believed, and the Commander, in the dream, pretended not to notice.''', requires=(H2,)),
        page_p('''She came to the Commander's funeral in a face nobody knew, and stood at the back, and laughed, very quietly, at the moment the priests said the Commander was at peace. She had been in the Commander's sleep the night before. It had been anything but peaceful.''', requires=(ON_RECORD,)),
    ), declined=None,
    deal=[[SH + "cost.never_alone"]],
    call=call('''[Think of her] "Shamira. Stand up."''',
        '''{n}You think of her the way she taught you to: loudly, in the front of your head, where anyone could see. It goes out of you across the whole of the Abyss, a thought with nobody's voice, and somewhere on an empty throne a woman who has been sitting very still hears it and lifts her head.{/n}''',
        (PLAIN_CHOICE, (), (), ()),
        ("[Keep your head to yourself, this once.]", None, (), ())),
    ledger=("Shamira: company, forever", "She lives on my dreams, and so she lives in them. I will never dream alone again. When I want a night to myself, I am to go and ask her for it to her face. It is the only debt in this book I have no wish to see settled."))
JA = "jannah.trickster."
partner("jannah", "jannah", "jannah.committed", "jannah.closed", "The Front Rank",
    '''Jannah Aldori stood the last night of the war in the front rank, where she could see what was coming, because she had asked to. She did not run. When the rift closed, or failed to, she walked back into Drezen with her sword on her shoulder, found the practice yard empty, chalked a circle on the sand in one stroke, and sat down in the middle of it to wait, eyes open, the way the forms teach you to wait for a victor who has not yet quit the field.''',
    (
        page_p('''At the rift the Commander called the salute, the way {mf|he|she} had once called it on the north wall with the vrocks coming: her whole name, and "To the first blood!" Far off, in a practice yard in Drezen, a half-elf got up out of a chalk circle before anyone had quit it, which is against every form there is, and came.''', requires=(called("jannah"),)),
        page_p('''The world buried the Commander. Jannah went to the graveside, lay down in the chalk she had drawn round it, and kept her eyes on the sky until the last priest had gone. Under the forms nobody leaves a circle until the victor has quit it, she said afterwards, and she was not at all sure who had won.''', requires=(ON_RECORD,)),
        page_p('''When the flask was opened in Drezen she was the first through the door with her blade up in the salute, because whatever came out of it was going to be greeted properly.''', requires=(H2,)),
        page_p('''She kept the scar on her temple where it could be seen. On the day of the Scar she let the Commander trace it once, and not on any other day.''', requires=(JA + "cost.temple_scar",)),
    ), declined=JA + "declined",
    deal=[[JA + "cost.first_loss"], [JA + "cost.story_lost"]],
    call=call('''[Call the salute] "Jannah Aldori! To the first blood!"''',
        '''{n}You have called it once before, on a wall, with wings coming out of the dark: her whole name and the old Mivon words. You give it everything you have left. It goes out over the rift and is swallowed, and then, very far off, over a city you cannot see, someone who never runs any more answers.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Jannah: a rematch, owed", "An Aldori may always ask the one who beat her for a rematch, and I have beaten her, or she me, too often for the account ever to be square. She keeps the chalk in her pocket. I am to expect a circle wherever I go."))
NE = "nenio.trickster."
partner("nenio", "nenio", "nenio.committed", "nenio.closed", "The Last Observation",
    '''Nenio spent the last night of the war on the roof of the citadel in Drezen with a spyglass, a stopwatch and a sheet headed THRESHOLD, OBSERVATIONS, because somebody had to write it down and she did not trust anybody else's handwriting except one, and that one was busy. When the rift closed, or failed to, she wrote down the time to the second. Then she sat with the pencil above the page for a long while and wrote nothing else at all, which in four thousand years she had never once done.''',
    (
        page_p('''At the rift the Commander shouted a question into the dark, the way {mf|he|she} had asked her things all year: "Nenio! Hypothesis!" Far off, on a roof in Drezen, a kitsune who never raised her voice stood up and shouted back, "Relevant!", loud enough that a sentry on the next tower dropped his spear, and was heard where it mattered.''', requires=(called("nenio"),)),
        page_p('''The world buried the Commander. Nenio attended, took notes, and chalked a small ruled blank under the name on the stone, three fingers wide. The sexton scrubbed it off every week. It was back every morning. She said a name was only a label, and the stone was premature.''', requires=(ON_RECORD,)),
        page_p('''When the flask was opened in Drezen she was there with the stopwatch, and timed it. She has never told anyone the number, and says she has forgotten it, and nobody believes her.''', requires=(H2,)),
        page_p('''She did not have the Commander's name at the rift, or after. She shouted "follower" and it did perfectly well.''', requires=(NE + "cost.name_filed",)),
        page_p('''Somewhere behind a white mask a question is still waiting to be asked. Nenio has the three hundred and six likeliest answers ready, rolled and tied with string, in the Commander's pack, next to volume one.''', requires=(NE + "cost.owes_an_answer",)),
    ), declined=NE + "declined",
    deal=[[NE + "cost.name_filed"], [NE + "cost.owes_an_answer"]],
    call=call('''[Ask her a question] "Nenio! Hypothesis!"''',
        '''{n}She asked you questions all through the war, with a pencil ready for the answer. You ask her one now, the only one you have, at the top of your voice, over the rift, into the dark where Drezen is. It is not a riddle. It has no stake. For a while there is nothing. Then, very far off, precise and indignant and entirely sure of itself, an answer comes back.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Nenio: a space, ruled", "She files what matters and forgets the rest. My name went into the Enigma on a riddle, or it never went anywhere and she only pretends; either way there is a space three fingers wide for me in every entry she writes. I am to answer all her questions, with numbers. The Sphinx is owed one answer too, if I bought Nenio back from her; Nenio has written three hundred and six of them for me in advance."))

HX = "herrax.trickster."
partner("herrax", "herrax", "herrax.committed", "herrax.closed", "The Keeper's Night",
    '''Herrax did not close the Ten Thousand Delights on the night the rift took the Commander, or failed to. She had said she would close them for one night if the news was bad, and the news took three days to reach the Midnight Isles. She spent the three days on Chivarro's old dais with the lamps lit and the takings unread, pouring her own wine, which nobody in the house had ever seen her do. Rokhorn brought the jug up the steps each time it was empty. He did not smile once, and she did not ask him to.''',
    (
        page_p('''The world buried the Commander. Herrax closed the Delights for one night, the first in a thousand years, and the whole of Alushinyrra said the madam had gone soft. She let them say it. The next night she opened again and charged double, and when a guest asked what the black ribbon on the arch was for, she told him it was the price of a room, and he paid it.''', requires=(ON_RECORD,)),
        page_p('''When the word came up the Wound roads that the Commander had walked out of the rift after all, she threw open the street doors of the Delights and let the whole Lower City drink until dawn at the house's expense. Then she sent the bill to the Lady in Shadow's court, marked "for the queen's amusement", and the court paid it without a word.''', requires=(H2,), forbids=("noct.defeated_not_dead",)),
        page_p('''When the word came up the Wound roads that the Commander had walked out of the rift after all, she threw open the street doors of the Delights and let the whole Lower City drink until dawn at the house's expense. She made out the bill to the Lady in Shadow, marked "for the queen's amusement", and nailed it to the door of the dark palace herself. It was still there in the spring. Nobody in Alushinyrra was fool enough to take it down, and nobody inside was answering the door.''', requires=(H2, "noct.defeated_not_dead")),
        page_p('''The arches of Alushinyrra still did not know the Commander. Nothing had changed about that, and Herrax liked it that way. When the Commander came back, it was up the stairs, all of them, like everyone else, and without paying, like no one else.''', requires=(HX + "cost.coin_lost",)),
        page_p('''She traced the thin white line on the Commander's cheek, the one an incubus had once read a lie in, and said it was the only mark in the Delights she had not made herself, and the only one she would have kept anyway.''', requires=(HX + "cost.clawed_cheek",)),
    ), declined=HX + "declined")
TE = "terendelev.trickster."
partner("terendelev", "terendelev", "terendelev.committed", "terendelev.closed", "The Night Watch",
    '''Terendelev did not go to Threshold. She could not fly there, and she would not have been let. She stood the night watch on the north turret above the Commander's empty rooms, with a pike and a brazier and a roll of clean linen in her pocket, and when the Worldwound's weather turned in her blood that night, the way an old break feels the rain, she did not sit down. She stood her post until the sixth bell, and then past it.''',
    (
        page_p('''At the rift the Commander pressed a hand to the wound that had been opened for her, and said her name into it the way a sentry gives the word at a gate. Far off, on a turret in Drezen, a silver-haired woman put her own hand flat over her breastbone, where the Commander's blood ran in her, and said "Here," to nobody, and the sentry beside her swore afterwards that the brazier flared white.''', requires=(called("terendelev"),)),
        page_p('''The world buried the Commander. Terendelev stood a watch over the grave in plain sight of the whole citadel, three nights running, with the pike, and when the chaplain asked her gently what she thought she was guarding, she said: a wound. Nobody understood her. She did not explain.''', requires=(ON_RECORD,)),
        page_p('''When the flask was opened in Drezen she was already there with clean linen, and changed the dressing before anyone else could speak, because it was the hour for it.''', requires=(H2,)),
        page_p('''Whatever the Worldwound did that night, the wound she was made from stayed open. She said that was all the proof she needed of anything, and went back to her turret.''', requires=(TE + "cost.wound_open",)),
    ), declined=TE + "declined",
    deal=[[TE + "cost.wound_open"]],
    call=call('''[Put your hand on the wound] "Terendelev. Stand to."''',
        '''{n}The wound is still open. It has been open since the fire at Iz, and it answers your hand the way it answers hers every morning: warm, and a little wet, and quiet. You say her name into it, the way a sentry gives the word. It goes out over the rift and is swallowed, and then, very far off, on a wall you cannot see, someone who has sworn to stand between you and whatever comes stands to.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Terendelev: a wound, guarded", "I opened my wound over her bones and it has never closed. She changes the dressing every morning at the same hour, and has sworn to stand watch over it until one of us is dust. I have never been so well guarded, or so thoroughly in anyone's debt, and she insists it is the other way round."))
HZ = "horzalah.trickster."
partner("horzalah", "horzalah", "horzalah.committed", "horzalah.closed", "The Box on the Shelf",
    '''Horzalah did not come to the Threshold. She had said she would not stand in lines. On the night the rift took the Commander, or failed to, she sat in the Guild master's chamber in Alushinyrra with the door barred and every contract in the strongboxes unread, and the small box with the white ribbon on her knees. Her masters listened at the door all night. None of them heard a sound. In the morning the ribbon had been untied and tied again, very carefully, in a bow that was slightly lopsided.''',
    (
        page_p('''The world buried the Commander. Horzalah took down every wager in her hall that had been placed on it, paid them all out of her own strongbox, and then had each of the winners killed, one by one, over the following year, at the Guild's usual rates, which she paid to herself. Nobody in Alushinyrra understood it. She did not explain.''', requires=(ON_RECORD,)),
        page_p('''When the flask was opened in Drezen she was already standing in the room, though nobody had seen her come. She did not say anything. She walked round the Commander once, slowly, checking that everything else was still attached, and then she took the Commander's hand and put it on her throat, where the scar was, and held it there.''', requires=(H2,)),
        page_p('''At the rift the Commander turned the deaf side of that head to the dark and said her name into it. Far away, in a hall full of knives, a woman stopped in the middle of a sentence and put her hand to her collar, and the master she had been sentencing lived, and never knew why.''', requires=(called("horzalah"),)),
        page_p('''The sentries of Drezen still told each other about the night a demon walked past all of them to take a piece of the Knight Commander. After the rift they told it differently. In the new version she had come to take the rest, and changed her mind.''', requires=(HZ + "cost.late",)),
    ), declined=HZ + "declined",
    deal=[[HZ + "cost.ear"]],
    call=call('''[Turn your deaf side to the rift] "Horzalah. Listen."''',
        '''{n}The side of your head where the ear was hears nothing now, not the wind off the rift, not the screaming. The rest of that ear is on a shelf in Alushinyrra, in a box with a white ribbon, in a room full of other people's deaths. You turn that side to the dark and say her name into it, where nobody but you can hear, which is a very stupid thing to do at the end of the world. For a while there is nothing at all. Then, far off, very faint, you would swear you hear a knife being put down.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Horzalah: an ear, on a shelf", "My left ear is in a box with a white ribbon on a shelf in the Assassins' Guild of Alushinyrra. It is not a debt; it is hers. No priest is to touch the side of my head, ever, or every knife in the Abyss will learn that she lied, and she will learn that I let them."))

EL = "eliandra.trickster."
partner("eliandra", "eliandra", "eliandra.committed", "eliandra.closed", "The Maiden's Lights",
    '''Eliandra did not go to Threshold. She had meant to go as far as the siege camp with the healers, and on the last day a column of wounded came up the Drezen road who could not wait, and she stayed with them instead, one wound at a time, as she did everything now. When the night came she went up onto the north wall of Drezen with a cup of water and her travelling cloak, and stood facing the Wound, and waited to be told.''',
    (
        page_p('''At the rift the Commander looked north and saw only a dark sky, and asked it, aloud, what it was doing. Far off on the north wall of Drezen a grey-cloaked woman turned her face up to a sky full of her Lady's lights, and answered, in the slow plain voice of the evening reading, exactly. The sentry beside her swore afterwards that he had heard both halves of the conversation, and nobody believed him, and he did not care.''', requires=(called("eliandra"),)),
        page_p('''The world buried the Commander. Eliandra read the evening's observation over the grave, as she had read it every evening for a hundred years, and at the end of it, where the corrections go, she wrote in her small exact hand: "Premature." Nobody crossed it out.''', requires=(ON_RECORD,)),
        page_p('''When the flask was opened in Drezen she was there with her question already chosen. It was, she admitted afterwards, not a very good one. She had been saving the good ones.''', requires=(H2,)),
        page_p('''Whatever the sky over Threshold did that night, the Commander could not see the part of it that belonged to the Maiden, and never would. She said that was all the proof she needed that the bargain had held, and went on describing it anyway.''', requires=(EL + "cost.lights_given",)),
        page_p('''She was not the strongest of her Lady's priestesses any more. She was, she said, strong enough to wait up.''', requires=(EL + "cost.reward_returned",)),
        page_p('''Her letter from the fords was still in the Commander's coat, its answer owed until the war was done. At the rift the Commander meant to write it the next morning, if there was a next morning. There was. It said: either.''', requires=(EL + "letter_kept",), forbids=("eliandra.committed",)),
    ), page_commit_groups=[["eliandra.committed"], [EL + "late_committed"]],
    deal=[[EL + "cost.lights_given"]],
    call=call('''[Look north] "Eliandra. Tell me what the sky is doing."''',
        '''{n}Low in the north, over the rift, there is a place your eyes will not stay on. They slide off it to the smoke, to the stones, to your own hands. It has been that way since the night at the basin. You say her name into it anyway, and ask it what it is doing, the way she once asked you every morning. For a while nothing answers. Then, very far off, slow and plain and entirely sure of itself, the evening reading begins.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Eliandra: the Maiden's lights", "I knelt at a basin in a cave that no longer exists and gave a goddess my sight of her lights, so that a woman who had never asked for anything could ask me one question. Now she asks me one every morning. The lights are still there, apparently. I have it on excellent authority. The authority will not stop describing them."))


GA = "galfrey.trickster."
partner("galfrey", "galfrey", GA + "partner", "galfrey.closed", "The Face in the Crowd",
    """Whoever she was by the last night of the war, the Queen of Mendev or a knight of a minor order whom nobody saluted, she spent it on the walls of Drezen, in the crowd of soldiers who had not been sent to Threshold and would not be told what happened there until morning. She stood among them in plain armour with an old sword, and watched the sky over the Wound the way she had watched it for a hundred years, and for once in all those years she was not the one everybody else was watching.""",
    (
        page_p("""At the rift the Commander called her name, the only one of her names nobody else in the world had the right to call: "Kitrane!" Far off, on the walls of Drezen, a knight in a green surcoat turned her head as if somebody had spoken at her elbow, and said "Here," to nobody, and the soldiers beside her swore afterwards that she had smiled like a girl.""", requires=(called("galfrey"),)),
        page_p("""The world buried the Commander. She stood at the graveside in the crowd, where she had asked to be, with her hood up. She had been buried once herself, in Nerosyan, with every bell in the city, and she knew exactly how little it meant. She waited.""", requires=(ON_RECORD,)),
        page_p("""When the flask was opened in Drezen she was there, and said nothing at all, and took the Commander's hand and did not give it back for the rest of the evening.""", requires=(H2,)),
        page_p("""Mendev had its Queen back after Threshold, and a scandal to go with her, and the Commander answered for it: at the Crossroads, whenever the talk turned to Iz, somebody always asked how it had been done, and the Commander always told them, and never once told it the same way twice.""", requires=(GA + "crown_reclaimed",)),
        page_p("""She stayed Kitrane. There was a knight of the Green Crows at the Crossroads table for as long as there was a table, grey-haired in time, with a squire at her elbow and a very old sword, and nobody who sat down there ever learned who she had been.""", requires=(GA + "kitrane_forever",)),
        page_p("""The Queen of Mendev kept her crown and her Commander both, and never once asked Mendev's leave for the second.""", requires=("galfrey.final",)),
    ), deal=[[GA + "cost.eulogy"]],
    call=call("""[Call her name] "Kitrane!\"""",
        """{n}You gave her that name at a deathbed, and she took it, and wore it into a crowd. You call it now over the rift, at the top of your voice, the way a sentry calls a password into the dark. It goes out over the Wound and is swallowed, and then, very far off, over a city you cannot see, somebody who used to be a queen answers to it.{/n}""",
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Galfrey: a eulogy, false", "I stood before the altar in Drezen and grieved for the Queen of Mendev in front of the whole city, knowing she was alive in a Crows' tent and that a knight called Sir Anselm Wray lay in her coffin. She owes me nothing for it. I owe him a name."))

EY = "elyanka.trickster."
partner("elyanka", "elyanka", "elyanka.committed", "elyanka.closed", "The Claim",
    '''Elyanka Camilary spent the last night of the war the way a creditor ought to: as close to the collateral as she could get without lifting a finger for it. She had a hearse with glass sides built in Caliphas for a mythic corpse, and six men in grey who did not breathe, and an appetite she had brought all the way from Ustalav. She waited to see whether the claim would fall due.''',
    (
        page_p('''She waited on the last ridge above the rift, as the Commander had told her to, with her hearse and her six. She did not lift a finger. When the fire leaned toward the Commander she leaned forward too, the way a moneylender leans toward a ship coming in low in the water, and her escort said afterwards that she never once blinked.''', requires=(EY + "collateral.at_rift",)),
        page_p('''She waited in the dead-house by the south gate of Drezen, with one candle, like a widow, as the Commander had told her to. She said afterwards that it was the worst night of her life, and the most instructive, and that she would never again agree to wait anywhere she could not see what she was owed.''', requires=(EY + "collateral.in_drezen",)),
        page_p('''At the rift the Commander said her name, and the terms of the sale, aloud, into the fire: if I fall here, your claim falls due; stand where you can collect. Somewhere behind the lines a woman in grey heard it, or said she did, and laughed.''', requires=(called("elyanka"),), forbids=(EY + "collateral.in_drezen",)),
        page_p('''At the rift the Commander said her name, and the terms of the sale, aloud, into the fire: if I fall here, your claim falls due. She was in Drezen, with her one candle, and heard nothing. A courier told her in the morning. She said she had known already, from the way the candle burned at the hour, and nobody could prove she had not.''', requires=(called("elyanka"), EY + "collateral.in_drezen")),
        page_p('''The Commander stepped into the Wound, and gave everything, and came back out of it anyway, with a death corked in a flask where the Wound could not reach it. The claim had not fallen due. It never would. She had been cheated by the letter of her own terms, whispered and unwritten, which said nothing about flasks. She laughed until she coughed, and then she held out her hand for the flask. "It's in my pocket," the Commander told her. "Corked." She was shown it. She was never given it.''', requires=(H2,)),
        page_p('''The Commander walked away from the end of the world with a flask in one pocket that held a death nobody would ever collect. She weighed it once through the cloth of the Commander's coat, with two cold fingers, the way she counts a pulse, and took her hand away. "Corked," she said. "You insolent sack of meat. I adore a bad bargain."''', requires=("lastcall.h1",), forbids=("sacrifice",)),
        page_p('''The world buried the Commander, and the chaplains asked the Ustalavic embalmer, very reluctantly, to prepare the body. She looked into the coffin for some time. Then she told them there was nothing in it but a joke, that she did not embalm jokes, and went back to her hearse, where the Commander was waiting.''', requires=(ON_RECORD,)),
        page_p('''She had a knotted black cord wound round her hand all that night, knot by knot the measure of the Commander, taken in the velvet of the hearse. When it was over she found she had knotted it tighter.''', requires=(EY + "bier_seen",)),
        page_p('''The lock of silver-grey hair bound in black thread was in the Commander's other pocket, beside the flask, all through the Threshold. She was told so afterwards. She said it was a vulgar place to keep it, next to a cheat, and did not ask for it back.''', requires=(EY + "lock_taken",)),
    ), declined=EY + "declined",
    deal=[[EY + "cost.corpse_bequeathed"]],
    call=call('''[Call in the bequest] "Elyanka, if I fall at the rift, your claim falls due. Stand where you can collect."''',
        '''{n}You sold your body once, in the dead-house by the south gate, in a whisper, to a woman who had come four hundred miles for it. You say the terms aloud now, over the rift, the way she whispered them in the dead-house, word for word, in the language older than its words. Nobody here understands them. That is not the point. A creditor ought to know when her debt is about to fall due, and where to stand to collect it.{/n}''',
        (PLAIN_CHOICE, (PILLAR,), (), ())))

MZ = "melazmera.trickster."
partner("melazmera", "melazmera", "melazmera.committed", "melazmera.closed", "The Heap at the Wound's Edge",
    '''Melazmera did not go to the Threshold. She had said she did not stand in lines, and she did not fight in anybody's war. On the night the rift took the Commander, or failed to, she lay on her heap in the crack at the Wound's edge in her own shape, with the old seal on her claw, and counted. The pickets on the north road heard her all night: a long low sound under the ground, over and over, like a bell rung in a cellar. In the morning one of them worked out that it was a number, and that it never got past forty-two.''',
    (
        page_p('''The world buried the Commander. She came to the funeral, after a fashion: she lay along the ridge of the cathedral roof in her own shape through the whole service, and the priests read very fast, and when it was over she flew north without a sound. For a month afterwards nothing at all came up out of the rifts on the northern edge, and the pickets did not know why, and were afraid.''', requires=(ON_RECORD,)),
        page_p('''When the flask was opened in Drezen she was on the windowsill before anyone else was in the room, in the woman she wears, and she did not say anything at all. She took the Commander's hand and counted the fingers, twice, and then the teeth, and would have gone on to the ribs if she had not been stopped.''', requires=(H2,)),
        page_p('''At the rift the Commander held up a grey stone the size of a hen's egg and said her name to it. Far to the north, in a crack in the ground, a dragon lifted her head off her heap in the middle of a number and did not finish it, and the pickets on the north road said afterwards that the silence was worse than the counting.''', requires=(called("melazmera"),)),
        page_p('''Two fingers of the Commander's ring hand had felt nothing since Colyphyr. At the rift, for the length of one breath, they were cold as the inside of a well, and the Commander knew exactly whose mouth that was.''', requires=(MZ + "cost.grey_hand",)),
    ), declined=MZ + "declined",
    deal=[[MZ + "stone_kept"]],
    call=call('''[Hold up the stone] "Melazmera. Come and count me."''',
        '''{n}The stone has been in your pocket since she let you take it, and it is still warm, here at the end of the world, with the rift screaming in front of you. You hold it up and say her name to it, which is a very stupid thing to do with a sapphire at the edge of the Worldwound. For a while nothing answers. Then, very far off, under the noise, you would swear you hear something enormous begin, slowly, to count.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Melazmera: a seal on a claw", "The Knight Commander's old seal is on the claw of an umbral dragon, and every order I have signed since has gone out under a new one. It is not a debt; it is in her hoard, and things in her hoard do not leave. In exchange I carry one of her stones, a sapphire that looks like a boring rock. She knows exactly which pocket it is in."))

YA = "yaniel.trickster."
partner("yaniel", "yaniel", "yaniel.committed", "yaniel.closed", "The Iron and the Wall",
    """Yaniel stood the night watch on the east wall of Drezen, at the old gate she had held the day the city fell. She had been asked to ride to the Threshold with the Mendevian foot and had said no, very politely, and then less politely; somebody had to be on the wall, she said, in case the crusade had to come back through a gate in a hurry, and she had some experience of that. She stood there from dusk, with a lamp at her feet and her cloak pulled round her, and watched the red sky over the Wound, and did not sit down once.""",
    (
        page_p("""At the rift the Commander held up a husk's iron cuff, one sheared link swinging, and said her name into the dark as a sentry gives the word at a gate. Far off, on the east wall of Drezen, a gray-haired woman put her hand to her bare left wrist, where the iron used to be, and said "Here," to nobody, and the sentry beside her swore afterwards that she said it the way people answer a roll call they had not expected to be on.""", requires=(called("yaniel"),)),
        page_p("""The world buried the Commander. Yaniel knelt a vigil over the grave in the rain, three nights running, the way a paladin does for a comrade, and on the fourth morning she got up and went back to her wall. She said she had been buried herself, once, with a statue, and that it had not taken.""", requires=(ON_RECORD,)),
        page_p("""When the flask was opened in Drezen she was already in the room, in her wall cloak, with the lamp still in her hand. She did not say anything. She took the Commander's wrist and turned it over and looked at it for a long while, as if checking for a mark, and then she put the iron back in the Commander's palm and closed the fingers over it, one at a time.""", requires=(H2,)),
        page_p("""Radiance was on her hip on the wall that night. It did not sing. She said afterwards that it had sung once and that was enough for any sword, and that it had been listening.""", requires=(YA + "carries", YA + "carries_holy")),
        page_p("""Radiance was on her hip on the wall that night, a plain good sword in a plain soldier's hand, and she said afterwards that it was the best night's watch she had ever stood.""", requires=(YA + "carries",), forbids=(YA + "carries_holy",)),
        page_p("""Radiance went to the Threshold on the Commander's hip, as sworn in a pit under the ground, and came back. She checked the edge, the grip and the Commander's face, in that order, and said the oath was kept, and never mentioned it again.""", requires=(YA + "oath_stands",)),
    ), declined=YA + "declined",
    deal=[[YA + "cost.shackle_kept"], [YA + "cost.oath_deskari"]],
    call=call('''[Hold up her iron] "Yaniel. Your watch."''',
        '''{n}You have carried her iron since the Midnight Fane: two fingers of crude husk-iron with one sheared link of chain, worn bright and thin on the inside by seventy years of the same bone. You hold it up now at the edge of the rift, where everything that was ever chained in the Abyss is screaming to be let out, and say her name into it the way a sentry calls a watch. Nothing answers for a while. Then, very far off, over a wall you cannot see, somebody who once held a gate until the last cart was through stands a little straighter.{/n}''',
        (PLAIN_CHOICE, (), (), ())),
    ledger=("Yaniel: a husk's iron", "I took a manacle off Yaniel's wrist in the Midnight Fane and I have carried it ever since. She offered to trade me back for it, fair and square, and I said no, and so did she. Nobody is square. I owe her a wall; she owes me a sword, or the other way about. Neither of us means to settle."))

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
        if part.get("page_commit_groups"):
            extra["RequiresAnyGroups"] = [sorted({k for g in part["page_commit_groups"] for k in g}, key=lambda k: k != part["commit"])]
            page = scene(part["key"] + ".lastcall.page", part["title"], "Epilogue", 1, "", [
                n("page", "Narrator", part["opener"], paragraphs=part["paragraphs"])],
                requires=("trickster.ever", ACTIVE), forbids=forbids, last=99, **extra)
        else:
            page = scene(part["key"] + ".lastcall.page", part["title"], "Epilogue", 1, "", [
                n("page", "Narrator", part["opener"], paragraphs=part["paragraphs"])],
                requires=("trickster.ever", ACTIVE, part["commit"]), forbids=forbids, last=99, **extra)
        out.append((part["rel"], page))
    return out

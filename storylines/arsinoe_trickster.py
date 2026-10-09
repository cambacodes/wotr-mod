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
"A soul cauldron, Commander, if I am any judge, and I am. A stamp can be forged. If this one is genuine, the stone belongs in Absalom's vaults. I should like to know how you acquired it, but I suspect that account would take longer than examining the mark."
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
"It is nothing personal. I like you a great deal more than I like most people who walk in here with the Treasury's property. But the Treasury does not care whom I like. If you propose a lease, the first five hundred crowns must come from the crusade chest today. Renewal terms come after that payment."''',
      c('"Five hundred now. It\'s leased, not stolen. Returnable at the end of the world."', "rent", mythic="Trickster",
        alignment=("Lawful", 1), crusade=("Finances", -500)),
      c('"It stays with me. Abadar can send a bill."', "refused"),
      c('"Another time."', abort=True)),
    n("rent", "Arsinoe", '''{n}The straw stops halfway to the crate.{/n}
"Leased."
{n}Her mouth curves, the way it does for a customer who has finally made an offer worth her time.{/n}
"A lease is a contract. A contract is lawful. And a lawful arrangement for the use of the Treasury's property, drawn up by an ordained priestess in good standing, is... something I could defend before my superiors, if I had to. I would enjoy defending it. I shall send Absalom a drawing of the stamp. If they deny title, the lease lapses and the temple keeps the rent for its trouble. If they confirm it, they receive lawful rent instead of an explanation of how I lost their stone. Until they rule, you answer for it under this lease. I sign for that arrangement too. The five hundred crowns are entered as your first payment. Rent, then. The same again every season the property is out of the vault. I do not haggle over the Treasury's property, Commander. I will, however, listen."''',
      c('"Agreed."', "leased"),
      c('"Five hundred a season is robbery with a halo."',
        check=dict(Skill="CheckDiplomacy", DC=25, Success="discount", Failure="raised", CommanderOnly=True))),
    n("discount", "Arsinoe", '''{n}Arsinoe hears you out with her chin on her hand. When you finish, she draws three short strokes beside the renewal dates.{/n}
"Three seasons' grace after today's payment. For a lessee proposing to take the stone to Threshold, where the Worldwound was first opened. If it survives your heroics, I expect it back. Do not tell the Treasury how much I enjoyed the argument."''',
      c("Continue", "leased")),
    n("raised", "Arsinoe", '''"No."
{n}She does not even reach for the pen.{/n}
"For wasting a priestess's time, the rate goes up. Another two hundred. Abadar rewards thrift, Commander. He does not reward charm. You will find that I am the same, most days."''',
      c("Continue", "leased", crusade=("Finances", -200), flags=("arsinoe.trickster.cost.rent_raised",))),
    n("leased", "Arsinoe", '''{n}She draws the lease in a clean, fast hand and reads the line that matters aloud: the lessee is you, by name. Not the crusade, not the Queen, not the chest. If the stone is lost, the debt follows you, and Abadar's church has collected from widows and grandchildren before now without losing sleep.{/n}
{n}Then she warms a stick of gold wax over the lamp, presses her seal into it, and fixes the tag to the diamond's cradle, just below the old Treasury stamp. *On lease.*{/n}
"Leased. Returnable at the end of the world, in whatever condition the world leaves it. The renewal dates and any grace are entered here. Abadar is my witness."''',
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
    n("start", "Arsinoe", '''{n}A ledger lies open beside a candle. Arsinoe puts her returned letter on top of it. A road warden has written ROAD CLOSED across the envelope.{/n}
"Absalom has not answered. Until it does, the lease stands by its provisional clause. You answer for the stone; I answer for letting you carry it off. Shyka's guess and that stamp had better survive examination."
{n}She turns the envelope face down.{/n}
"Now. You mean to take it to Threshold, where the Worldwound was first opened. I cannot inspect what a demon has scattered over a battlefield. The temple requires collateral against total loss. What are you pledging?"''',
      c("Continue", "pledge", forbids=("konomi.trickster.cost.recalled",)),
      c("Continue", "rider", requires=("konomi.trickster.cost.recalled",))),
    # Ledger row 8: the only Konomi line Arsinoe bills is the consular recall rider. The wedding lines (Kiana's paste trick,
    # guests_robbed) are added by kiana_trickster.integrate: it gates these two choices off on guests_robbed and appends the
    # wedding / wedding_dog nodes, with restitution (Q3 or bought back) skipping straight to the pledge (tested below).
    n("rider", "Arsinoe", '''{n}She turns back a page of the ledger, to a line in red ink she has clearly been waiting to show you.{/n}
"One more entry, while the book is open. The Mendevian consulate's old invoice. Lady Konomi's name, a recall rider, five lines explaining why they sent him after a dispatch that said she was dead. Paid." {n}She taps the figure.{/n} "It came across my desk because I keep the only honest books in Drezen. I know what it bought. I simply wanted you to know that I saw it, and that I entered it at cost."''',
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
    n("threshold", "Arsinoe", '''{n}Arsinoe turns the sign to CLOSED and locks the till. Her eyes stay on you.{/n}
"The lien stands. This is outside the lease. Close the curtains."
{n}While you do, she undoes her collar, then the clasps of her robe. The silk falls around her feet. She steps out of it, pauses in the lamplight, and lifts her chin.{/n}
"Well? I have had enough of watching you admire the stone."
{n}She takes your hand and pulls you close. Her mouth is warm and deliberate; the second kiss leaves her breathing harder. She pushes the ledger aside and the pen rolls off the counter, unmourned. You sit on the cleared edge of the counter, and she settles astride your lap, bare skin beneath your hands. Her breasts are hot against your shirt. She works your buttons open one-handed, and when your palms close on them she makes a short, unladylike sound and rocks against you to hear it again.{/n}
"I keep an exact account of what I want, Commander. Lower."
{n}You obey, and she is already wet and moving, hips rolling over your thigh, her teeth at your lower lip while the counter complains under both of you. She drags your clothes aside, impatient where she is always exact, lifts herself over you, and slides her hand down between you to bring you where she wants you.{/n}''',
      c("Continue", "morning")),
    n("morning", "Arsinoe", '''{n}The sign still says CLOSED when you wake. Outside, customers are already arguing over whose turn it is. Arsinoe sits at the counter in her shift, hair unbound, a cold cup of tea beside the ledger.{/n}
"The lease has not changed. Nor has the price of a scroll, whatever they are shouting out there."
{n}She closes the book, catches your collar, and kisses you.{/n}
"That was for me. Tell anyone I gave you a discount and I shall deny it. Go and be impressive, Commander. I have a shop to open."''',
      c('"Leave before the first customer arrives."', flags=("arsinoe.trickster.collection_night_shared",))),
], requires=("trickster.ever", "arsinoe.capital", "arsinoe.trickster.primed", LEASE),
   forbids=(COLLECTION, "arsinoe.closed"), delay=72)


# Returned property, loss liability, rent and invitations have separate entries.
ALIVE = "trickster.commander_back"
GRACE = "arsinoe.trickster.cost.rent_grace"
LC = "lastcall.active"  # life witness only; E-Q8-11 settles this lease on CALLED
ACCEPTED = "arsinoe.trickster.late_accepted"
OPEN = ("arsinoe.closed", "arsinoe.parted")


def living(text, requires=(), forbids=(), any_groups=()):
    """Disjoint life twins; Last Call never substitutes for Commander return."""
    return (
        p(text, requires=requires, forbids=(*forbids, "sacrifice"), any_groups=any_groups),
        p(text, requires=(*requires, "sacrifice", ALIVE), forbids=forbids, any_groups=any_groups),
    )


def personal(text, requires=(), forbids=(), any_groups=()):
    # An ordinary open future is already a relationship; no extra promise.
    return (living(text, (*requires, "arsinoe.campaign_lover"), (*forbids, *OPEN), any_groups)
            + living(text, (*requires, ACCEPTED), (*forbids, *OPEN, "arsinoe.campaign_lover", "arsinoe.future_spoken"), any_groups))


WORD_RETURNED = ('{n}Arsinoe drew a line through the Commander\'s pledged word when the stone came back whole. '
                 'Beside it she wrote: "Collateral released." The cancelled lease went back across her counter. '
                 'Any rent still due remained a separate account.{/n}')
WORD_OUTSTANDING = ('{n}With the stone lost and the bill unpaid, Arsinoe called on the word the Commander had pledged. '
                    'Her letter named the account and asked for a meeting to settle it. It contained no invitation '
                    'upstairs. Until payment, the entry remained open.{/n}')
WORD_SETTLED = ('{n}With the loss account settled, Arsinoe struck out the pledged word and marked it "Released." '
                'She returned the cancelled lease with the receipt.{/n}')
INVITATION = ('{n}Years later, she sent the Commander an invitation on temple vellum. No sum, no seal, no demand for '
              'payment. Only supper, an hour, and a sharply underlined "Do not be late."{/n}')
STILL_RETURNED = ('{n}When the stone returned, Arsinoe released the lien on the Fool King\'s still. The barrel baron '
                  'invited her to keep inspecting it. Her reports now began "Visit at the proprietor\'s invitation" '
                  'and ended with a verdict on the beer. Several bore the rings of cups.{/n}')
STILL_OUTSTANDING = ('{n}While the loss account remained unpaid, the temple inspected the Fool King\'s pledged still each '
                     'season. The barrel baron met the inspections in full regalia. Arsinoe checked the stock, tasted '
                     'the beer, and recorded both. The lien remained on the still, not on its customers.{/n}')
STILL_SETTLED = ('{n}Settlement released the lien on the Fool King\'s still. The barrel baron invited Arsinoe to continue '
                 'her visits, which she entered as invitations rather than inspections of collateral. Her reports '
                 'became less useful to the temple and acquired considerably more stains.{/n}')
SETTLED = [[CALLED]]


def epilogue(id, title, text, requires, forbids=(), paragraphs=()):
    SCENES.append(scene(id, title, "Epilogue", 1, "", [n("end", "Narrator", text, portrait="Arsinoe", paragraphs=paragraphs)],
                        requires=requires, forbids=forbids, last=6, Relationship="arsinoe"))


RENT = ('{n}Arsinoe reckoned the rent by the agreed renewal dates and entered the balance separately from the returned '
         'stone. The Commander received an exact bill, with no charge for seasons after the lease ended.{/n}')
RENT_GRACE = ('{n}The three renewals waived at the counter stayed waived. Arsinoe crossed each out before reckoning '
               'any later rent. She sent the Commander the balance on a separate bill; returning the stone had ended '
               'the lease.{/n}')
BURST_COMMERCIAL = ('{n}The loss account remained unpaid. Arsinoe kept the bill with the lease. '
                    'Last Call had ended without the stone being returned under its clause.{/n}')
BURST_PERSONAL = ('{n}She handed back the cancelled lease, then kept her hand on the Commander\'s '
                              'for a moment before letting go.{/n}')

# Existing slots: three account dispositions, three word histories, still.
BURST_VARIANTS = (
    p('{n}Arsinoe entered it in the temple ledger as "leased property, consumed in the course of its intended use." '
      'Then she drew up the bill, addressed it to Threshold, attention of the Commander, and sent it by the ordinary '
      'post. It came back unopened, bearing a seal nobody in Drezen could identify. She filed it with evident '
      'satisfaction. The loss account remained open, with the Commander\'s name beside the sum.{/n}', forbids=(CALLED, LC)),
    living(BURST_COMMERCIAL, (LC,), (CALLED,))[0],
    p('{n}At the rift, the diamond had been handed back a breath before it burst. The return preceded the destruction. '
      'Arsinoe entered the return before the destruction, discharged the loss claim, and settled the separate rental '
      'account according to the lease. She underlined the date and returned the cancelled document.{/n}', requires=(CALLED,)),
)
BURST_COLLATERAL = (
    *living(WORD_OUTSTANDING, (WORD,), (CALLED,)),
    p('{n}The stone was lost and the loss account remained unpaid. Arsinoe entered the pledged word beside the claim '
      'against the Commander\'s estate. No personal appointment could settle that account now.{/n}',
      requires=(WORD, "sacrifice"), forbids=(ALIVE, CALLED)),
    p(STILL_OUTSTANDING, requires=(STILL, "fool_king.available"), forbids=(CALLED, "fool_king.gone")),
)
epilogue("arsinoe.trickster.epilogue.bill_to_threshold", "A bill addressed to Threshold",
    '{n}The stone Arsinoe leased to the Commander burst at Threshold. Absalom never did rule on its title. '
    'The lease had to answer for it.{/n}',
    ("trickster.ever", LIEN, "arsinoe.siphon_burst"), paragraphs=(
        BURST_VARIANTS + BURST_COLLATERAL
        + (living(BURST_COMMERCIAL, (LC,), (CALLED,))[1],)
        + personal(BURST_PERSONAL, (CALLED,))
        + living(WORD_SETTLED, (WORD,), any_groups=SETTLED)
        + (p('{n}The loss account had been discharged. Arsinoe marked the pledged word "Released" and filed it '
             'with the cancelled lease.{/n}', requires=(WORD, "sacrifice"), forbids=(ALIVE,), any_groups=SETTLED),)
        + personal(INVITATION, (WORD,), any_groups=SETTLED)
        + (p(STILL_SETTLED, requires=(STILL, "fool_king.available"), forbids=("fool_king.gone",), any_groups=SETTLED),
           p('{n}The Fool King\'s still remained pledged against the unpaid loss account. The temple kept its '
             'inspection records with the lien; the barrel baron was no longer there to receive an inspector.{/n}',
             requires=(STILL, "fool_king.gone"), forbids=(CALLED,)),
           p('{n}Settlement released the lien on the Fool King\'s still. Arsinoe filed the old inspection reports '
             'with the cancelled lease.{/n}', requires=(STILL, "fool_king.gone"), any_groups=SETTLED),
           p('{n}The three waived renewals were struck from the rental reckoning. Arsinoe allowed the concession she '
             'had signed for, and charged only what the lease still required.{/n}', requires=(GRACE,), any_groups=SETTLED),
           p('{n}The three renewals waived at the counter stayed waived. They covered no loss of the stone; any '
             'later rent remained on its own page.{/n}', requires=(GRACE,), forbids=(CALLED,)))
    ))

epilogue("arsinoe.trickster.epilogue.pot_returned", "Returned at the end of the world",
    '{n}The soul cauldron came back from Threshold whole. Arsinoe locked the diamond in the temple strongroom and '
    'copied the gold-wax tag into her ledger: "Returned at the end of the world, as agreed. Lease ended. Title: '
    'unproven, pending Absalom." She turned to the rental account on the next page.{/n}',
    ("trickster.ever", LIEN), ("arsinoe.siphon_burst",), paragraphs=(
        *living(RENT, forbids=(CALLED, LC, GRACE)),
        p('{n}Arsinoe reckoned the rent by the dates in the lease and entered any balance against the Commander\'s '
          'estate. The returned stone was recorded separately; no rent was charged after the lease ended.{/n}',
          requires=("sacrifice",), forbids=(ALIVE, CALLED, LC)),
        living(RENT, (LC,), (CALLED, GRACE))[0],
        *living(WORD_RETURNED, (WORD,)),
        p('{n}The stone was returned, and Arsinoe struck out the pledged word. Whatever remained of the rental '
          'account was entered against the estate.{/n}', requires=(WORD, "sacrifice"), forbids=(ALIVE,)),
        p(STILL_RETURNED, requires=(STILL, "fool_king.available"), forbids=("fool_king.gone",)),
        p('{n}The three waived renewals were struck out of the rental reckoning.{/n}', requires=(CALLED, GRACE)),
        *living(RENT_GRACE, (GRACE,), (CALLED, LC)),
        *living(RENT_GRACE, (LC, GRACE), (CALLED,)),
        living(RENT, (LC,), (CALLED, GRACE))[1],
        p('{n}The return clause discharged the loss security. Arsinoe settled the separate rental account according '
          'to the lease and returned the cancelled document.{/n}', requires=(CALLED,)),
        p('{n}The three waived renewals were struck out before the estate\'s rental balance was reckoned.{/n}',
          requires=("sacrifice", GRACE), forbids=(ALIVE, CALLED, LC)),
        *personal(INVITATION, (WORD,)),
        p('{n}The returned diamond released the lien on the Fool King\'s still. Arsinoe filed the old inspection '
          'reports with the cancelled lease.{/n}', requires=(STILL, "fool_king.gone")),
    ))

epilogue("arsinoe.trickster.epilogue.foreclosure", "A lien on one Worldwound, slightly used",
    '{n}Among the records of the Drezen temple of Abadar lies a lien, sealed in gold wax, on "one Worldwound, slightly '
    'used". Clerks from Absalom have tried three times to strike it out as a jest. Each time, the clerk who opens '
    'the file finds the seal whole and the terms in order, and closes it again rather more quietly than he opened it.{/n}',
    ("trickster.ever", WOUND), ("ending.wound_closed",), paragraphs=(
        p('{n}The loss account remained unpaid. Arsinoe kept the Worldwound lien beside the bill, with the '
          'Commander\'s name on both.{/n}', requires=("arsinoe.siphon_burst",), forbids=(CALLED, LC)),
        p('{n}Last Call ended without the lease being called in. Arsinoe kept the unpaid loss account beside the '
          'Worldwound lien.{/n}', requires=("arsinoe.siphon_burst", LC), forbids=(CALLED,)),
        p('{n}The return at Threshold discharged the loss claim. Arsinoe filed a copy of the released Worldwound '
          'lien, with the return date written beneath the seal. She sent the First Vault a copy for its records.{/n}',
          requires=("arsinoe.siphon_burst", CALLED)),
        p('{n}The returned diamond ended the claim against the Worldwound. Arsinoe wrote "Released on return" '
          'beneath the seal and filed the lien as a record of what had once been pledged.{/n}', forbids=("arsinoe.siphon_burst",)),
    ))
epilogue("arsinoe.trickster.epilogue.foreclosure_closed", "Collateral withdrawn by closure",
    '{n}When the Worldwound closed, Arsinoe marked its lien "Collateral withdrawn by closure. Lien discharged." '
    'She underlined the date twice. The rental account had its own page.{/n}',
    ("trickster.ever", WOUND, "ending.wound_closed"), paragraphs=(
        p('{n}The return at Threshold was entered beside the discharge. Arsinoe sent the First Vault a copy for '
          'its records, with no claim to the land where the Wound had been.{/n}', requires=(CALLED,)),
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
             answer_list=KONOMI_OFFICER, forbids=("konomi.dismissed", "konomi.retained_dead", "konomi.dead.unreturned"),
             # Sol INT (2026-09-30): she must be in her office, and a Konomi returned by her Trickster route hears it too.
             # Keep the body veto and the landed persistent/latest death reader;
             # neither an unloaded body nor an old return cancels a later loss.
             ForbidOverrides={"konomi.dismissed": "arsinoe.trickster.konomi_serving"},
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
    late("offer", '''{n}After Threshold, Arsinoe reopened her shop. The answer given there before the final march had not been forgotten.{/n}''',
         c('[Take her hand, and draw her in by the collar.]', "night"),
         c('"Supper tonight. I would like to keep you waiting a little longer."', "table"),
         c('[Leave the answer as you gave it.]', "business"),
         paragraphs=(
             p('"You threatened to make the payments late. I have brought no bill tonight. You may disappoint me about the rent some other time."', requires=(STAYS,)),
             p('"There was a roof above Tovin\'s shop. Bread, cheese, and far too many buildings to point at. We sat together until he brought the lamp. I wanted another evening even then."', requires=(COURTED,), forbids=(STAYS,)),
             p("\"And a book I promised to lend you, with a whole page about an innkeeper's sauce.\"",
               requires=(COURTED, "arsinoe_first_impression"), forbids=(STAYS,)),
             p("\"And a table in Tovin's shop after closing, where you read the sauce while I watched your face.\"",
               requires=(COURTED, "arsinoe_hours_of_her_own", "arsinoe.next_table"), forbids=(STAYS,)),
             p('"And the doorway with the carved face. I meant to show you the stonework, then caught myself looking at you instead."',
               requires=(COURTED, "arsinoe_hours_of_her_own", "arsinoe.next_walk"), forbids=(STAYS,)),
             p('"The war took too many evenings. I mean to be less accommodating now."',
               requires=(COURTED,), forbids=(STAYS,)),
             p('"I came because I want you. I have spent all day being patient with customers. Come here."'),
         )),
    late("night", '''{n}Arsinoe stood close while the Commander opened her collar, gold eyes fixed on theirs. At the next clasp she caught their hands and kissed them hard.{/n}
"I waited for the campaign to end. These fastenings have had quite enough of my patience."
{n}She undid the rest herself and let the robes fall. Her hair came loose as she pushed the Commander back toward the bed. She drew them down beside her, put their hands on her bare waist, and held them there until their fingers tightened. Then she bent to their mouth, and her composure broke on a breath.{/n}
"Higher. I have wanted your hands there since the roof above Tovin's shop."
{n}The Commander cupped her breasts and she arched into them, nipples hard against their palms, a low curse in a priestess's mouth. She stripped them with the exactness she gave a ledger and none of the patience, kissed down their chest while their hands knotted in her loosened hair, and came back up with her thighs spread wide over them. She was wet against their skin and shaking with the effort of not hurrying. Her hand slid down between them, and her gold eyes did not leave theirs.{/n}''',
         c("Continue", "morning")),
    late("morning", '''{n}In the morning she sat at the Commander's table in her shift, hair loose, drinking from the better cup. The other stood within reach of the bed.{/n}
"Go back to sleep. I mean to open late, and I want company."
{n}She set down the cup and came back before the Commander could oblige. The next appointment was made over breakfast. At the shop, she cleared a place for a second cup without entering it in any account.{/n}''',
         c('[Stay.]')),
    late("table", '''{n}She took the Commander's hand across the table, leaned over, and kissed them hard. When she sat back, she was smiling.{/n}
"Supper tonight. The rest in a month. I can afford four weeks, and I intend to enjoy looking forward to every one of them."
{n}She kept the appointment, and the next. The queue outside her shop learned which morning of the month it would be wise to come later.{/n}''',
         c('[Keep the appointment.]')),
    late("business", '''{n}Arsinoe kept to the answer the Commander had given her before the march. When business brought them together, she was courteous, exact, and quick to return to her customers. The evenings she had once offered went to other company.{/n}
"May Abadar keep you, Commander."''',
         c('[Let her go.]')),
], requires=(LATE_COMMITTED,), forbids=(*LATE_GONE, "sacrifice", "ascended", "swarm", "true_lich"),
   ForbidOverrides={"sacrifice": "trickster.commander_back"}, last=6, Relationship="arsinoe"))

# Ascended: no visit up a stair. She writes, and the page says why there is no night (brief pattern 3).
SCENES.append(scene("arsinoe.trickster.late.ascended", "An invoice to a higher address", "Epilogue", 6, "", [
    late("letter", '''{n}Arsinoe never learned how to send a letter to a Commander who had become something the roads did not reach. She wrote one anyway, the spring after Threshold, on temple vellum, and left it on the altar of Abadar, which was the highest address she had.{/n}
{n}It said that she had meant to come to the Commander's door in her good robes with her hair up, and say that she wanted them, and that she had not priced it. It said that a door was a necessary part of the arrangement. It asked, with perfect courtesy, whether the Commander still had one.{/n}
{n}Nobody knows whether it was answered. The second cup on her shelf was never given to another guest.{/n}''')],
    requires=(LATE_COMMITTED, "ascended"), forbids=LATE_GONE, last=6, Relationship="arsinoe"))

COLLECTOR = p("{n}Asked why she had stayed, Arsinoe said Drezen still required a priestess who could read an account. "
              "Asked by the Commander, she gave a less public answer.{/n}", requires=(STAYS,))


def integrate(payload):
    """Registered-route edit (save-safe: text only): the three kept endings gain the collector paragraph (E14c)
    instead of sibling pages, so the ordinary one-ending-per-history invariant holds unchanged."""
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    payload.setdefault("DerivedForbids", {})["arsinoe.trickster.konomi_not_dismissed"] = ["konomi.dismissed"]
    payload["DerivedForbids"]["arsinoe.trickster.konomi_in_post"] = ["konomi.dead.unreturned"]
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


# --- eng8-q8c / E-Q8-09: interrupted pledges and both negotiated outcomes ---
# Authored lease terms: grace waives renewals, never the initial 500 crowns.
_RENT_GRACE = "arsinoe.trickster.cost.rent_grace"
_nodes["discount"]["EnterSet"] = [_RENT_GRACE]
_nodes["discount"]["Text"] = _nodes["discount"]["Text"].replace(
    "Three seasons' grace.", "The first payment stands. The next three seasonal renewals are waived.")
for _choice in _nodes["rent"]["Choices"]:
    _choice["Forbids"].append(_RENT_GRACE)
for _choice in _nodes["start"]["Choices"]:
    if _choice.get("Next") == "rent":
        _choice["Forbids"].append(_RENT_GRACE)
_nodes["start"]["Choices"].append(c(
    '"The first payment stands. We agreed on three renewals free."', "discount",
    requires=(_RENT_PAID, _RENT_GRACE), forbids=(_RENT_RAISED,)))

_collection = next(s for s in SCENES if s["Id"] == COLLECTION)
_pledge = next(nd for nd in _collection["Nodes"] if nd["Id"] == "pledge")
_collateral = (STILL, WOUND, WORD)
for _choice in _pledge["Choices"]:
    _choice["Forbids"].extend(_collateral)
# Append-only resume answers: no second pledge, including when the still is gone.
for _flag, _target, _text in (
    (STILL, "still", '"The still is already pledged."'),
    (WOUND, "wound", '"You already hold the lien on the Worldwound."'),
    (WORD, "word", '"My word is already in your ledger."'),
):
    _pledge["Choices"].append(c(_text, _target, requires=(_flag,),
        forbids=tuple(f for f in _collateral if f != _flag)))

# end eng8-q8c


# --- eng8-q8c / E-Q8-04: close the collection opener before its next turn ---
_collection["Nodes"][0]["Text"] = _collection["Nodes"][0]["Text"].replace(
    'I do not do that. So.\n', 'I do not do that. So."\n')
# end eng8-q8c


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


# Authored aftermath, on Konomi's existing office list. These are separate
# occasions for the same allocated reactor, with independent completion IDs.
INTIMACY = "arsinoe.trickster.intimacy_seen"
KONOMI_KNOWN = "arsinoe.trickster.after_war.konomi_known"
KONOMI_POST = "arsinoe.trickster.konomi_in_post"
DERIVED[INTIMACY] = [["arsinoe.night_shared"], ["arsinoe.trickster.collection_night_shared"]]
DERIVED[KONOMI_POST] = [["konomi.in_office", "crossroute.konomi.available", "arsinoe.trickster.konomi_serving"]]
# The dismissal device returns her with recessed; the other devices retain
# returned. Consume both landed receipts without granting or repeating a return.
DERIVED["arsinoe.trickster.konomi_serving"] = [["arsinoe.trickster.konomi_not_dismissed"],
    ["konomi.trickster.returned"], ["konomi.trickster.recessed"]]
DERIVED["arsinoe.trickster.konomi_not_dismissed"] = [["trickster.ever"]]

SCENES.append(reaction("Konomi", "arsinoe.trickster.after_hours.react_konomi",
    ("trickster.ever", INTIMACY, "konomi.in_office"),
    '{n}Lady Konomi slides a folded complaint beneath another letter. Her smile makes no attempt at innocence.{/n}\n"A merchant waited an hour for a scroll and demanded that I inform the capital. I shall. Immediately after the dispatch about the demon armies."\n{n}She taps the buried letter.{/n}\n"He also included an account of your whereabouts. Such enterprise. I advised him to pay more attention to his own customers. An audience with the Commander must be requested through the proper office. Arsinoe\'s counter is not a second diplomatic council."',
    answer_list=KONOMI_OFFICER, relationship="arsinoe",
    entry='"Has someone complained about Arsinoe\'s opening hours?"',
    forbids=("konomi.dismissed", "konomi.retained_dead", "konomi.dead.unreturned"),
    ForbidOverrides={"konomi.dismissed": "arsinoe.trickster.konomi_serving"},
    chapter=5, last=5, delay=0, Chapters=[5]))

# The landed ask keeps its ID, nodes and original yes/no answer positions.
# Availability changes only which copy of the same yes witnesses the office
# exchange. The original no-office yes remains fully available.
_ask = next(s for s in SCENES if s["Id"] == "arsinoe.trickster.late.ask")
_ask_start = _ask["Nodes"][0]
_ask_start["Choices"][0]["Forbids"].append(KONOMI_POST)
_ask_start["Choices"].append(c(_ask_start["Choices"][0]["Text"], "yes_known",
    flags=(LATE_ACCEPTED,), requires=(KONOMI_POST,)))
_ask["Nodes"].append(n("yes_known", "Arsinoe", '{n}Arsinoe walks with you as far as the citadel. At Lady Konomi\'s open office door she stops.{/n}\n"If your clerks want me after the campaign, send them before closing. I have made other arrangements for my evenings."\n{n}Konomi\'s glance travels from her to you. She smiles.{/n}\n"How prudent. I shall put temple business first. The Royal Council\'s requests can be discussed during your profitable hours."\n{n}Arsinoe gives her a folded account.{/n}\n"My rates for the Council\'s next order. That business will keep its usual hours."',
    c(flags=(KONOMI_KNOWN,))))

# Read the recorded answer, never readiness as an acceptance. A refusal
# remembers business only on the old target; it creates no route closure.
_late["Requires"] = [LATE_READY]
_late["RequiresAnyGroups"] = [[LATE_ACCEPTED, LATE_DECLINED]]
for _paragraph in _late["Nodes"][0]["Paragraphs"]:
    _paragraph["Requires"].append(LATE_ACCEPTED)
_late["Nodes"][0]["Paragraphs"].append(p('{n}The spring after Threshold, she came to the Commander\'s door in her good robes, hair pinned up, gold eyes steady.{/n}\n"I kept the evening you asked for. I intend to keep rather more of them."', requires=(LATE_ACCEPTED,)))
for _node in _late["Nodes"]:
    if _node["Id"] in ("morning", "table"):
        _node.setdefault("Paragraphs", []).append(p('{n}Lady Konomi\'s next letter to Arsinoe requested letters of credit for Mendevian merchants. Below the figures she asked that the Council\'s orders be filled before Arsinoe\'s private appointments. Arsinoe answered with her rates. Konomi\'s reply arrived promptly: "Let us talk price."{/n}',
            requires=(LATE_ACCEPTED, KONOMI_KNOWN, KONOMI_POST)))


# Round 2 receipts: nights record events, never acceptance or commitment.
DERIVED[INTIMACY].append(["arsinoe.unprofitable_night_shared"])
_prior_integrate = integrate
def integrate(payload):
    _prior_integrate(payload)
    # A settled ordinary future supersedes the earlier invitation for every reader.
    payload.setdefault("DerivedForbids", {})[LATE_COMMITTED] = ["arsinoe.future_spoken"]
    from storylines import arsinoe_rubric2
    arsinoe_rubric2.integrate(payload)

# Business recollections do not stage Konomi in Arsinoe's shop.
_collection = next(s for s in SCENES if s["Id"] == COLLECTION)
_col = {page["Id"]: page for page in _collection["Nodes"]}
_col["stay"]["Choices"][1]["Next"] = "personal_offer"
_collection["Nodes"].append(n("personal_offer", "Arsinoe", '''{n}Arsinoe taps the renewal date, then rests her hand beside yours.{/n}
"The payments will be punctual. Another evening with you is a different offer. I should like it."
{n}She folds the lease and puts it away.{/n}
"Ask me after closing. I am tired of being interrupted at the interesting part."''', c()))
_col["threshold"]["Text"] = _col["threshold"]["Text"].replace('Well? I have had enough of watching you admire the stone.',
    'I have had enough of watching you admire the stone. Look at me.')
_col["threshold"]["Choices"][0]["Next"] = "arsinoe.trickster.cauldron.collection.explicit.1"
# Explicit slot C: secured till, cleared counter, personal invitation; lien unchanged.
_collection["Nodes"].append(n("arsinoe.trickster.cauldron.collection.explicit.1", "Arsinoe", '''{n}Still astride your lap, Arsinoe catches your hand against her waist. The ledger lies where she pushed it; she gives it no further attention.{/n}
"The ledger stays shut tonight."''', c("Continue", "morning")))

# Arrival is established in the existing accepted paragraphs, before any recall.
_offer = _late["Nodes"][0]
_arrival = '{n}The spring after Threshold, Arsinoe came to the Commander\'s door in her good robes, hair pinned up, gold eyes steady. When the door opened, she stepped inside and laid her gloves on the table.{/n}\n'
_offer["Paragraphs"][0]["Text"] = _arrival + _offer["Paragraphs"][0]["Text"]
_offer["Paragraphs"][1]["Text"] = _arrival + '"There was a roof above Tovin\'s shop. Separate chairs, bread, cheese, and far too many buildings to point at. Then I took your hand, and kept it until he brought the lamp. I wanted another evening even then."'
_offer["Paragraphs"][7]["Text"] = '"Tonight is the evening we kept. I intend to keep rather more of them."'
_ln = {page["Id"]: page for page in _late["Nodes"]}
_ln["night"]["Choices"][0]["Next"] = "arsinoe.trickster.late.commit.explicit.1"
_ln["morning"]["Text"] = '''{n}In the morning Arsinoe sat at the Commander's table in her shift, drinking from the better cup. She put it down when the Commander stirred, crossed the room and slid back beside them.{/n}
"I have time for this. Stop looking at the door."
{n}She kissed them, then rested her cheek against their shoulder. When she finally rose, her hair was thoroughly disordered. She pinned it up at the mirror and came back for a last kiss before opening the shop.{/n}
"Supper next time. I shall bring something worth being late for."'''
_table_text = _ln["table"]["Text"]
_ln["table"]["Text"] = '''{n}The next morning Arsinoe returned from opening the shop with bread still warm from the oven. She put it on the table and took the Commander's hand before they could reach for it.{/n}
"The customers have their scrolls. Now I want my breakfast."
{n}She kissed them, sat down beside them and named their next evening. Her shop's queue learned which morning of the month it would be wise to come later.{/n}'''
_offer["Choices"][1]["Next"] = "deferred_evening"
_late["Nodes"].extend([
    # Explicit slot L: impatience with fastenings after an accepted physical arrival.
    late("arsinoe.trickster.late.commit.explicit.1", '''{n}Arsinoe remained over the Commander, her fingers closing around theirs against her waist. The discarded robes lay beside the bed.{/n}
"Tomorrow, you may tell me how patient I was."''', c("Continue", "morning")),
    late("deferred_evening", '''{n}At supper she took the Commander's hand across the table and kissed them firmly before sitting back.{/n}
"Tonight we eat. The rest in a month. I can afford four weeks, and I intend to enjoy looking forward to them."
{n}Four weeks later she came back after closing, carrying the bottle she had promised. She set it beside the supper dishes and began undoing her collar before either cup was filled.{/n}
"I kept the date. Now put that down and come to me."
{n}She caught the Commander's sleeve, kissed them and led them toward the bed. Halfway there she stopped to kiss them again against the wall, her robes already open, her bare breast filling the Commander's palm. She had been composed all day and was composed no longer. She ground against their thigh and bit their lip.{/n}
"Four weeks. I have been insufferable all day. Take your clothes off."
{n}The Commander did, and she watched every inch of it with open appetite. She pushed them down onto the bed, straddled them and let the robes slide off her shoulders, hair falling around both their faces. Her hand went between them to take hold, and she stayed there, poised and flushed and smiling, savouring the moment she had waited a month for.{/n}''', c("Continue", "arsinoe.trickster.late.commit.explicit.2")),
    # Explicit slot D: kept four-week appointment, distinct from immediate arrival.
    late("arsinoe.trickster.late.commit.explicit.2", '''{n}Arsinoe stayed poised over the Commander, flushed and smiling, the unopened bottle beyond either of their reach.{/n}
"You have kept me waiting long enough."''', c("Continue", "table")),
])


# Returning intimacy uses the union of played mornings; no first-night reward repeats.
_col["stay"]["Choices"][0]["Forbids"].append(INTIMACY)
_col["stay"]["Choices"].append(c(_col["stay"]["Choices"][0]["Text"], "threshold_return",
    requires=("arsinoe.campaign_lover", INTIMACY), flags=(STAYS, "arsinoe.started")))
_collection["Nodes"].append(n("threshold_return", "Arsinoe",
    _col["threshold"]["Text"].replace('This is outside the lease. Close the curtains.',
    'I want you here again. Outside the lease, as before. Close the curtains.'),
    c("Continue", "arsinoe.trickster.cauldron.collection.explicit.1")))
_offer["Choices"][0]["Forbids"].append(INTIMACY)
_offer["Choices"].append(c(_offer["Choices"][0]["Text"], "late_return",
    requires=(LATE_ACCEPTED, INTIMACY)))
_late["Nodes"].append(late("late_return", _ln["night"]["Text"].replace(
    'I waited for the campaign to end. These fastenings have had quite enough of my patience.',
    'I remember waking beside you. I have had quite enough patience during the campaign.'),
    c("Continue", "arsinoe.trickster.late.commit.explicit.1")))

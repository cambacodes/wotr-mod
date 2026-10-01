"""Konomi on the Trickster path: recess, not farewell (Writer/handoffs/trickster/konomi.md, families F17 and F03).

Canon: the Commander dismisses the attache of Nerosyan with "you can go to the demons, Lady Konomi. Along with the entire
Royal Council." (Diplomacy_6/Answer_0070 73c5728c) and she answers "So be it. Farewell, Commander... I will make haste for
Nerosyan" (Cue_0075 384cd664). She prices everything: "Very well, let us talk price" (Diplomacy_4/Cue_0034 4652e021, with
"a smug, somewhat predatory smile"), and her people "live everywhere, you are just... not always aware of our existence"
(Diplomacy_Officer/Cue_0038 efe7fee4). Kyado names the Trickster's rule: "your tricks somehow become the truth" (Kyado_main_
dialogue/Cue_0109 509eac82, PlayerIsTrickster only; quoted by nobody in this route). Polish 9b: no word is made true
here. Dismissed: the council minute records her audience as adjourned, a rider carries it to the Chancellor, and her
driver is paid to take the charcoal loop road back to the east gate; she stays of her own accord, because she does not
walk out of an adjourned audience. Dead: her soul is called by her own people's rite, found through a payment in her own
ledger (her canon: her people "live everywhere"), and she consents only on her fee (a raise calls, it does not drag).
Never arrived: a Nerosyan informer in the Drezen chancery, caught on the page and used as a postman. She prices, bills,
refuses, and can walk away.
"""
import copy

from story_format import c, n, p, reaction, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
UNIT = "ca2d58c5c65723945857e04fb85d30ce"              # RankUpOfficer_Diplomacy (her capital actor; hidden, never removed)
HUB = "0dc8b8604bb33c846a63f3eb62443674"               # Crusade/RankUps/Diplomacy/Diplomacy_Officer/AnswersList_0003
LOCATOR = "e6a7de2a-ce6f-4413-b24d-06daf1990e4c"       # her office locator (the one DiplomacyOfficer_InDrezen uses)
REGILL_HUB = "2366a8db6481070439fee222c0c52e45"        # CompanionDialogues/Regill/AnswersList_0002
KYADO_HUB = "33178c26f304abe41949f3fb0fa8ac6e"         # c3/TempleOfDelamere/KyadoDrezen/AnswersList_0003 (Kyado in Drezen)

PRIMED = "konomi.trickster.primed"
RETURNED = "konomi.trickster.returned"
RECESSED = "konomi.trickster.recessed"
DECLINED = "konomi.trickster.declined"
SETTLED = "konomi.trickster.terms_settled"
ENVOY = "konomi.trickster.envoy"
LATE = "konomi.trickster.cost.late"
DEBT = "konomi.trickster.cost.debt_owed"
OUTFOXED = "konomi.trickster.cost.outfoxed"
PAID = "konomi.trickster.debt_paid"
FAVOUR = "konomi.trickster.favour_owed"
RECALLED = "konomi.trickster.cost.recalled"
FEE = "konomi.trickster.cost.consult_fee"
FEE_PAID = "konomi.trickster.fee_paid"
ACCREDITED = "konomi.trickster.cost.accredited"
STEWARD_PAID = "konomi.trickster.cost.steward_paid"       # the informer paid, and left in the chancery
STEWARD_BURNED = "konomi.trickster.cost.steward_burned"   # the informer threatened with the rope, and gone
JOURNEY = "konomi.trickster.journey_paid"
LATE_COMMITTED = "konomi.trickster.late_committed"
DEAD = "konomi.retained_dead"
CONFIRMED = "konomi.retained_return_confirmed"
KYADO_SAID_IT = "konomi.trickster.kyado_said_it"         # he said Cue_0109 to this Commander
DRIVER = "konomi.trickster.cost.driver_paid"             # polish 9b: the loop road bought, and the minute sent
LAMP = "konomi.trickster.cost.her_people"                # polish 9b: her people's rite; their price is silence
TESTED = "konomi.trickster.supper_asked"                 # Sol BEL: a non-lover is asked why, before any commit
ASKED_AGAIN = "konomi.trickster.asked_again"             # Sol INT: the season she asked for, and the second ask
SLIP = "konomi.trickster.slip_read"                      # Sol TRK: the informer's slip, caught on the page
ARRIVED = "konomi.trickster.arrived"                     # Sol r2 INT: she is placed in her office only once she is back
ROAD_BACK = "konomi.trickster.back_from_the_road"        # Sol r5 INT: the dismissal journey's own arrival (not the jug's)
MISSED_LATCH = "konomi.missed_contact.latched"           # PP5 r2: first observation of the missed contact (the 96 hours run from it)
GALFREY_GONE = ("galfrey.dead", "galfrey.killed_by_commander")
REGILL_GONE = ("regill.dead", "regill.kicked_out", "regill.left_plot")
OWN = ("konomi.closed", "konomi.farewell", "inhuman")
DEVICE_OWN = ("konomi.closed", "inhuman")   # Sol r4: a completed ordinary farewell does not bar the dismissal rescue

RELATIONSHIP_PATCH = dict(
    TricksterAccess={
        "konomi.dismissed": dict(detect=["konomi.dismissed", "konomi.office_completed"],
                                 device="konomi.trickster.dismissed.late", returned=RECESSED),
        "konomi.retained_dead": dict(detect=[DEAD], device="konomi.trickster.dead.recalled", returned=CONFIRMED),
        "konomi.missed_contact_available": dict(detect=["konomi.missed_contact_available"],
                                                device="konomi.trickster.never_arrived.accredited", returned=RETURNED),
    })
PRESENCES = {
    # Her capital actor exists hidden whether she was dismissed or never came (KonomiHidden 0b828275); reuse-native
    # unhides it on the office locator the native office etude uses. Derived presence_on (trickster_world) opens it only
    # after the loop on the road (cost.late) or the secretary's error (cost.accredited).
    "konomi.presence": dict(Unit=UNIT, Area=DREZEN, Mode="reuse-native", At=dict(Locator=LOCATOR, Offset=[0.0, 0.0]),
                            Requires=["trickster.ever", "konomi.trickster.presence_on"], Forbids=["konomi.closed", "konomi.private_departed"],
                            MinChapter=3, MaxChapter=5, AnswerLists=[HUB]),
}
SEEN_CUES = {KYADO_SAID_IT: ["509eac8248670664fab0808c3e00fe04"]}   # Kyado_main_dialogue/Cue_0109


def k(id, text, *choices, **kw):
    return n(id, "Konomi", text, *choices, portrait="Konomi", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Konomi", **kw)


def physical(id, title, entry, nodes, requires, forbids, delay, chapters=(5,), own=None, **extra):
    SCENES.append(scene(id, title, "Konomi", min(chapters), entry, nodes, requires=requires, forbids=(*(own or OWN), *forbids),
                        delay=delay, last=max(chapters), optional=True, Relationship="konomi", Areas=[DREZEN],
                        Chapters=list(chapters), ContactUnit=UNIT, AnswerLists=[HUB], **extra))



def letter(id, title, nodes, requires, forbids, delay, chapters=(5,), own=None, **extra):
    SCENES.append(scene(id, title, "Konomi", min(chapters), "", nodes, requires=requires, forbids=(*(own or OWN), *forbids),
                        delay=delay, last=max(chapters), optional=True, Relationship="konomi", Areas=[DREZEN],
                        Chapters=list(chapters), Remote=True, **extra))


# --- State dismissed: recess, not farewell (F17) ------------------------------------------------------------------

# The only setup: the old inline preface cannot return to Diplomacy_6 (Cue_0068 has a Continue), so the joke is said on
# the page, at the gate, after the insult. Its own marker (cost.late) opens the recess, so a Konomi revived earlier on the
# path and dismissed later still has a road to walk.
letter("konomi.trickster.dismissed.late", "Mind the step", [
    nar("start", '''{n}Her carriage is at the east gate in the grey before dawn, Nerosyan's pennant on the roof and the curtains drawn. You are on the wall above it. So, by some coincidence nobody will admit to, is half the watch.{/n}
{n}"So be it," she said, when you told her where she and the Royal Council could go. "Farewell, Commander." She wished you luck with the foreign powers. She said she would make haste for Nerosyan. She did not say she would forgive you, and she did not look back from the door.{/n}
{n}The driver gathers the reins. The curtain on your side does not move.{/n}''',
      c('[Shout it after the carriage] "Farewell, Lady Konomi. ...Mind the step on your way back in."', "minute",
        mythic="Trickster", alignment=("Chaotic", 1)),
      c('[Leave the chair where it is.] "..."', abort=True)),
    nar("minute", '''{n}The watch laughs, because you are the Commander, and then stops, because nothing else happens. The curtain does not move. The carriage goes out under the arch and down the road toward the capital, and grows small, and is gone.{/n}
{n}At the council table that morning the attaché's chair is empty. The clerk has the minute of her dismissal in front of him and his pen raised, waiting for the word.{/n}''',
      c("Continue", "queen", requires=("coronation.seen",), forbids=GALFREY_GONE),
      c("Continue", "record", forbids=("coronation.seen",)),
      c("Continue", "record", requires=("coronation.seen", GALFREY_GONE[0])),
      c("Continue", "record", requires=("coronation.seen", GALFREY_GONE[1]), forbids=(GALFREY_GONE[0],))),
    nar("queen", '''{n}The Queen is in Drezen this week, and sits in on the council this morning out of courtesy, to listen rather than to rule. It was her seal on the scroll Lady Konomi carried into this room on her first day.{/n}
{n}She raises one eyebrow at the empty chair, then at you, and says nothing at all.{/n}''',
      c("Continue", "record")),
    nar("record", '''{n}You tell him what to write. He hesitates a moment, pen above the page: a minute of the war council is a legal record in Mendev, and he will sign under it. Then he writes it exactly as dictated, because the Commander's word at this table is an order and the minute is his only protection from it.{/n}
{n}'Audience with the attaché of Nerosyan: adjourned.'{/n}
{n}He sands it. The word dries, and stays.{/n}''',
      c('[Minute it as a recess] "The record will show the audience was adjourned. Not ended."',
        flags=(PRIMED, LATE, "konomi.started"), forbids=("konomi.dismissed",)),   # retired by gating (index kept)
      c('[Minute it as a recess] "The record will show the audience was adjourned. Not ended."', "driver")),
    nar("driver", '''{n}The minute goes out within the hour by the consulate's fastest rider, under your seal, to the Chancellor in Nerosyan: the Commander's audience with the attaché of Nerosyan stands adjourned, and the Commander awaits her return to conclude it.{/n}
{n}The second errand you run yourself. Her driver waters his horses at the last post-house before the Nerosyan road forks from the old charcoal road, the loop the burners' carts use, which bends west through the hills for two days and comes back to Drezen by the east gate. He is a practical man with a family in the lower town, and he knows exactly who you are.{/n}''',
      c('[Pay the driver to take the loop road, and to swear he never turned the horses] "Two days on the charcoal road. The east gate at noon. And you never turned."',
        crusade=("Finances", -150), flags=(PRIMED, LATE, "konomi.started", DRIVER), forbids=("konomi.dismissed",)),   # retired (PP5)
      c('[Let the carriage go.] "..."', abort=True, forbids=("konomi.dismissed",)),                                   # retired (PP5)
      c('[Pay the driver to take the loop road, and to swear he never turned the horses] "Two days on the charcoal road. The east gate at noon. And you never turned."',
        "gate", crusade=("Finances", -150)),
      c('[Let the carriage go.] "..."', abort=True)),
    # PP5 (tier-A Ch5 budget): the gate sergeant's note is this letter's last page, not a second delivery. The letter waits
    # until the road is behind her (72 hours after the insult), so everything it tells has already happened when it is read.
    nar("gate", '''{n}The account ends with the gate sergeant's note, dated two days after the carriage left, a little after noon, in a hand that has plainly been laughing: the Nerosyan carriage came back in by the east gate, the attaché in it. She asked for her old office. The driver asked for a priest.{/n}''',
      c("Continue", flags=(PRIMED, LATE, "konomi.started", DRIVER, ROAD_BACK))),
], requires=("trickster", "konomi.dismissed", "konomi.office_completed", "konomi.dismissed.latched"),
   forbids=(LATE, RECESSED), delay=72, TricksterDevice=True, TricksterState="konomi.dismissed", own=DEVICE_OWN)

READ_TERMS = '''"Tricks are my people's prerogative, Commander, and they are never free. You have played one on me without asking. Very well, let us talk price."
{n}She opens the fan and looks at you over the top of it.{/n}
"You have kept an attaché from her capital in the middle of a revolt. You dismissed her from a council table and adjourned her from a wall, in front of the watch, and sent the Chancellor a minute that says so. How very public. I could leave again tonight, and the capital would thank me for it. But you have put yourself in Nerosyan's debt in front of your own watch, with a minute that says so in your hand, and a Commander in the Crown's debt is worth more to my Chancellor than one more attaché in a burning capital. So I stay until I have collected. Nerosyan will want to know why I am late, and I shall want something to tell them."'''

# Dorgelinda's audit is read, never required (doc 03 §2.11).
DORGELINDA_PRIMED = "dorgelinda.trickster.primed"
LEDGER_TERMS = '''{n}She lets the fan fall shut against her palm.{/n}
"Your quartermaster tells me a warehouse walked into your personal account. You and she keep books the same way, Commander: one line for the Crusade, and one for what the Crusade does not know it has paid."'''

physical("konomi.trickster.dismissed.recess", "The third morning", '"Lady Konomi."', [
    nar("start", '''{n}Lady Konomi's carriage left Drezen by the east gate at dawn. Two days later, at noon, it came back in by the east gate. The driver swears on his mother and on Erastil that he never turned the horses, and it is perfectly true: the charcoal road did the turning for him.{/n}
{n}The morning after the carriage came back, she is standing in her old office in front of the swept desk, fan closed, travelling cloak still on. On the desk lies the clerk's copy of the minute, where somebody took care that she would find it: 'Audience with the attaché of Nerosyan: adjourned.' When you come in she steps back over the threshold and forward over it again, very deliberately, watching her own feet.{/n}
{n}She does not look pleased about it. She looks, if anything, interested, which is worse.{/n}''',
      c("Continue", "price")),
    k("price", '''"You told me to mind the step on my way back in. I have now minded it, Commander, and the capital is burning without me."
{n}Her smile is smug and faintly predatory, the one she used to save for the Royal Council's opponents.{/n}
"The driver has had a religious experience. The horses have not recovered. I have spent two nights at inns I did not choose and been charged for three, which is the only part of this I understand. You will tell me it was chance."''',
      c('[Chance] "Chance. Drezen\'s roads are notoriously circular."',
        check=dict(Skill="CheckBluff", DC=30, Success="read", Failure="outfoxed", CommanderOnly=True)),
      c('[Tell her the truth] "I told you to mind the step. You didn\'t ask why."', "truth")),
    k("truth", '''"No. I did not."
{n}She closes the fan against her palm, one fold at a time.{/n}
"I heard a Commander being childish from a wall, and I let the curtain stay shut so that you could watch me not hearing it. I heard a jest. I did not hear you buy my driver at the last post-house, or send my dismissal to the Chancellor dressed as an adjournment." {n}Something sharp and pleased moves behind her eyes.{/n} "I shall not make that mistake twice."''',
      c("Continue", "read")),
    k("read", READ_TERMS,
      c('[Hear her terms] "Name them."', flags=(RECESSED, DEBT), forbids=(DORGELINDA_PRIMED,)),
      c("Continue", "read_ledger", requires=(DORGELINDA_PRIMED,))),
    k("outfoxed", '''"Circular."
{n}She lets the word hang in the air a moment longer than it deserves.{/n}
"I saw your road on the second morning, Commander. The hills were on the wrong side of my window, and my driver had a new purse and could not look at me. I stayed on the loop to watch you work. You work very prettily. You also lie to a kitsune about a trick, to her face, in her own office."
{n}She sits, uninvited, behind the desk that is no longer hers.{/n}
"Now the price is mine to set, and I shall set it high."''',
      c("Continue", "read_outfoxed")),
    k("read_outfoxed", READ_TERMS,
      c('[Hear her terms] "Name them."', flags=(RECESSED, DEBT, OUTFOXED), forbids=(DORGELINDA_PRIMED,)),
      c("Continue", "read_outfoxed_ledger", requires=(DORGELINDA_PRIMED,))),
    # Appended: Dorgelinda's audit (dorgelinda_trickster) as a node variant; it never gates the recess.
    k("read_ledger", LEDGER_TERMS,
      c('[Hear her terms] "Name them."', flags=(RECESSED, DEBT))),
    k("read_outfoxed_ledger", LEDGER_TERMS,
      c('[Hear her terms] "Name them."', flags=(RECESSED, DEBT, OUTFOXED))),
], requires=("trickster.ever", "konomi.dismissed", "konomi.office_completed", LATE, ROAD_BACK),
   forbids=(RECESSED,), delay=0, own=DEVICE_OWN)

# Sol r2 INT: her actor is placed only when she is back in Drezen, two days after the road (and the letter says so).
# PP5: kept for saves already on the road (cost.late without back_from_the_road); a new shout sets both in the setup.
letter("konomi.trickster.dismissed.arrival", "The east gate at noon", [
    nar("start", '''{n}A note from the gate sergeant, in a hand that has plainly been laughing: the Nerosyan carriage came back in by the east gate at noon, the attaché in it. She asked for her old office. The driver asked for a priest.{/n}''',
      c("Continue", flags=(ARRIVED,), forbids=("konomi.dismissed",)),   # retired by gating (index kept)
      c("Continue", flags=(ROAD_BACK,))),
], requires=("trickster.ever", "konomi.dismissed", LATE), forbids=(ROAD_BACK, RECESSED), delay=48, own=DEVICE_OWN)

physical("konomi.trickster.dismissed.terms", "Terms", '"You said you would name your terms."', [
    k("price", '''{n}She has had the desk polished. There is a single sheet on it, and her pen, and nothing else.{/n}
"My terms. A letter to Nerosyan in your hand, endorsing the restoration of the Royal Council your nobles arrested. Not an apology. An endorsement. The capital will pay for my three days on your road by reading it aloud in the council chamber, and you will pay by having written it, in front of every lord in Mendev who wanted you to."''',
      c('[Pay her price] "The letter, then. My hand, my seal."', "paid", crusade=("Finances", -500),
        forbids=(OUTFOXED,)),
      c('[Pay her price] "The letter, then. My hand, my seal."', "paid_envoy", crusade=("Finances", -500),
        requires=(OUTFOXED,)),
      c('[Offer a different coin] "Not that letter. Ask me for something else. Anything I can give myself."', "favour"),
      c('[Refuse] "I won\'t pay for a road."', "refused")),
    k("paid", '''{n}She reads it once for the argument and once for the grammar, and corrects the grammar.{/n}
"Your nobles will say you have gone soft on the Crown. The Crown will say you have finally understood your place. Both will stop sending you grain for a season while they decide which of them is right. That is the price, Commander. I did not say it was mine to pay."
{n}She seals it herself.{/n}''',
      c('"Worth it."', flags=(SETTLED, PAID, "konomi.private_future"))),
    k("paid_envoy", '''"...and my name on it, as your envoy. You lied to me about the road. I should like the lie paid for in ink, where I can see it."
{n}She reads the letter once for the argument and once for the grammar, corrects the grammar, and adds a line of her own at the foot before she seals it.{/n}
"You will find I am very hard to dismiss twice."''',
      c('"I don\'t doubt it."', flags=(SETTLED, PAID, "konomi.private_future"))),
    k("favour", '''{n}She taps the pen once against the blank sheet, then lays it down.{/n}
"An unnamed favour, then, to be named at a time of my choosing. Not the crusade's. Yours."
{n}Her smile is small and does not reach any further than it has to.{/n}
"I have a very good memory, Commander, and an excellent sense of timing. You will not like the day I choose. You will pay anyway, because you are the kind of Commander who shouts clauses at carriages, and that kind always pays."''',
      c('"Name the day when you like."', flags=(SETTLED, FAVOUR, "konomi.private_future_open"))),
    k("refused", '''"Then I go to Nerosyan for good."
{n}She rises, and gathers her gloves, and does not hurry.{/n}
"I shall tell them the road was a jest, and that you were very drunk, and that I found it charming. They will believe me. They always do."
{n}At the door she stops, one foot over the threshold, and looks down at it.{/n}
"The road will let me go this time, I think. I shall pay the driver myself. You have made it very clear you do not want me back."''',
      c('[Let her go.]', flags=("konomi.closed",))),
], requires=("trickster.ever", RECESSED, "konomi.dismissed"), forbids=(SETTLED,), delay=48, own=DEVICE_OWN)

physical("konomi.trickster.dismissed.private", "Off the record", '"Business concluded?"', [
    nar("start", '''{n}Evening. The office is lit by one lamp. Her terms are entered in her own ledger, in her own hand, and the ledger is closed. The window is open on the square, where the watch is changing.{/n}''',
      c("Continue", "concluded")),
    k("concluded", '''"Business concluded, Commander. You are still here. So am I. One of us will have to explain that, and I should prefer it were not me."''',
      c('[Ask her to stay, for yourself] "Stay. Not for Nerosyan. For me."', "answer", requires=("konomi.lovers",)),
      c('[Ask her to stay, for yourself] "Stay. Not for Nerosyan. For me."', "courted", requires=(TESTED,),
        forbids=("konomi.lovers",)),
      c('[Ask her to stay as envoy] "Stay as Nerosyan\'s envoy. The chair is yours."', "envoy")),
    k("answer", '''{n}She does not answer at once. She opens the fan, and closes it, and sets it on her closed ledger as if it were a paperweight.{/n}
"Three days on your road, and you wait until the business is sealed to say it. You did the same at the council table: the price first, the thing you actually wanted afterwards, when there was nobody left to bargain with but me."
"I stay. On my own account, not Nerosyan's. I keep my own rooms, my own correspondents and my own opinions, and you shall have all three at breakfast. And you never again dismiss me in front of a council. In private you may try. I shall enjoy watching."''',
      c('[Take her hand] "Then name the next evening."', "threshold", flags=("konomi.committed",)),
      c('[Ask what she wants] "What do you want, Konomi? Not the capital. You."', "wants")),
    k("courted", '''{n}She studies you over the closed fan, as if you had put a clause in front of her in a language she reads well and did not expect to see here.{/n}
"You dismissed me in front of a council. You bought my driver. Then you sat through a supper with no clerk and answered my question like a person, which I did not expect, and I have been annoyed about it since."
"In my trade, the difference between a courtship and an insult is usually the seal. I have had a road and a supper to read yours." {n}The corner of her mouth moves.{/n} "It is both, and I will take it anyway."
"I keep my own rooms, my own correspondents and my own opinions, and I shall give you all three at breakfast. And you never again dismiss me in front of a council. You may dismiss me in private. I shall enjoy watching you try."''',
      c('[Take her hand] "Then name the next evening."', "threshold", flags=("konomi.committed",)),
      c('[Ask what she wants] "What do you want, Konomi? Not the capital. You."', "wants")),
    k("wants", '''"Me. Very well."
{n}She counts them off on the closed fan.{/n}
"My letters go to Nerosyan under my seal and come back under it, and nobody in your chancery opens them. Not your clerks, not your spymaster, not you. I sit at your council in my own right, not as your guest. And the next time you want me gone, you tell me so in a room with a door, not from a wall."''',
      c('[Agree to all of it] "All of it. Your seal, your chair, a door."', "threshold", flags=("konomi.committed",)),
      c('"Your letters go through my chancery like everyone\'s. That one I won\'t give."', "no")),
    k("envoy", '''"Envoy. A chair at your table, with my name on it and Nerosyan's seal under it."
{n}She considers the offer the way she considers a treaty: from the end backwards.{/n}
"That, Commander, I will take. And I will make you regret offering it every single week, in writing, in triplicate, with the capital copied in."''',
      c('[Accept the chair\'s terms] "Envoy, then. My door stays open."', flags=(ENVOY,))),
    k("no", '''{n}She sets the pen down and squares it with the edge of the ledger, exactly, before she answers.{/n}
"Then you want an attaché whose letters you read. I have been that, for the Crown, and I will not be it in your bed." {n}She picks up the fan again. It steadies her hand.{/n} "Give me a season, Commander. Then ask me again, and do not ask as a Trickster. Ask as someone who could be told no."''',
      c('[Let her decide] "Your call."', flags=(DECLINED,))),
    nar("threshold", '''{n}She looks at your hand in hers for a moment, and her thumb moves once across your knuckles.{/n}
"The next evening," she says, "is this one."
{n}The fan closes with a snap. She rises, and the manners she has worn since the day she walked into your council with a scroll under the Queen's seal come off all at once: the ears she keeps so correctly upright at the table tip back, pleased, and the tail she holds in a careful curl through every audience comes loose and sweeps out behind her in the lamplight, slow, russet and pale-tipped, like a banner let down from a wall.{/n}
"I have wanted this since you shouted at my carriage. Take this robe off me. Slowly. I want to watch your hands."
{n}You do it slowly. She lets the outer robe slide from one shoulder, then the other, and stands in the lamplight with nothing on but her rings, and lets you look for exactly as long as she has decided you may. Then she kisses you, hard, her nails light at the back of your neck, her tail curling round the backs of your knees as if it had its own opinion about where you should stand.{/n}
{n}She walks you backwards to the desk. A week of Nerosyan's dispatches goes to the floor in a slither of wax and ribbon. She pushes you down across the place where they lay, climbs over you with her knees either side of your hips, catches both your wrists in one hand and pins them above your head, and settles astride your hips, and reaches down between you with her free hand, watching your face the whole time to see what it costs you.{/n}''',
      c("Continue", "morning")),
    nar("morning", '''{n}Morning. She is at your desk in your shirt, composing a dispatch, tail curled round the leg of the chair. The dispatches are stacked again, in order. One of them has a heel print on it.{/n}
"Nerosyan will hear that I was detained by the Commander on urgent business." {n}She blots the line.{/n} "Entirely accurate."
{n}She does not look up when you come to stand behind her. She does lean back, just enough.{/n}''',
      c('"Leave the one with the heel print. I\'ll answer it myself."')),
], requires=("trickster.ever", SETTLED), forbids=("konomi.committed", DECLINED, ENVOY), delay=72, own=DEVICE_OWN)

physical("konomi.trickster.dismissed.supper", "Supper, unminuted", '"Supper. No clerk."', [
    k("start", '''{n}She has chosen the room: the small one above the chancery, with one table, two chairs and no bell to call a secretary. The dishes are Nerosyan and the wine is not, and she tastes both before you do, out of habit rather than suspicion.{/n}
"No clerk, no minute, no seal. You will find it very uncomfortable, Commander. I intend to watch."''',
      c("Continue", "letter", requires=(PAID,)), c("Continue", "favour", requires=(FAVOUR,), forbids=(PAID,)),
      c("Continue", "ask", forbids=(PAID, FAVOUR))),
    k("letter", '''"You paid for my road with a letter that will cost you your nobles' grain for a season. That was a political price, and I took it as one. Tonight I want to know what you pay when there is nobody to read the receipt."''',
      c("Continue", "ask")),
    k("favour", '''"You paid for my road with a favour I have not yet named. That was a debt, and I took it as one. Tonight I want to know what you pay when there is nobody to hold the note."''',
      c("Continue", "ask")),
    k("ask", '''{n}She folds her hands on the table, the negotiator's posture, and then, deliberately, unfolds them.{/n}
"One question, and I shall know if you answer it as a Commander. Why did you turn the road round? Not for Nerosyan. The capital would have sent you another attaché within the month, and a duller one. Why me?"''',
      c('"Because nobody else at that table ever told me no and made me glad of it."', "glad", flags=(TESTED,)),
      c('"Because I wanted you in the room. Not the chair. You."', "you", flags=(TESTED,)),
      c('"Because Nerosyan\'s envoy is worth more than its attaché."', "politics")),
    k("glad", '''"Glad."
{n}She turns the word over as if checking it for a false bottom, and does not find one.{/n}
"I have been dismissed by better generals and flattered by worse ones. You are the first who cost me a reception and three days of charcoal smoke and made me curious about the bill." {n}She pours for you herself, which she has never once done at the council table.{/n} "Ask me again when my ledger is closed. I may even let you finish the sentence."''',
      c('"When your ledger is closed, then."')),
    k("you", '''"Me."
{n}Her ears tip back, a fraction, before she has them upright again.{/n}
"That is either the most honest thing a Commander has said to me or the best-rehearsed. I find I do not mind which, and that is the part I shall hold against you." {n}She pours for you herself, which she has never once done at the council table.{/n} "Ask me again when my ledger is closed."''',
      c('"When your ledger is closed, then."')),
    k("politics", '''"There. A Commander's answer, and a correct one." {n}She finishes her wine and sets the cup upside down on its saucer.{/n} "I shall take the chair if you offer it, and you shall ask me for nothing else. It is a better bargain for both of us. I shall try to be grateful."''',
      c('"Goodnight, Lady Konomi."')),
], requires=("trickster.ever", SETTLED), forbids=("konomi.lovers", TESTED, "konomi.committed", DECLINED, ENVOY), delay=24, own=DEVICE_OWN)

physical("konomi.trickster.dismissed.a_season", "A season, abridged", '"You asked for a season."', [
    k("start", '''{n}Her ledger is open at a page headed, in her own hand, with nothing but a date. The date is today's.{/n}
"It has not been a season. I have decided I do not need the whole of one; I have seen how you spend time, and I would rather not wait for you to spend mine."
{n}She closes the fan and lays it across the page.{/n}
"You were told to ask as someone who could be told no. So. Ask."''',
      c('"Stay, Konomi. Not the envoy. You. And you may say no."', "price", flags=(ASKED_AGAIN,)),
      c('"Not yet. I haven\'t earned the question."', abort=True)),
    k("price", '''"Then hear what I want. It is small, and you will hate it."
"Once, at the council table, in front of every lord who watched you dismiss me, you will put a recommendation to me, and I will refuse it, and you will take the refusal and move to the next business. No joke. No road. You will sit in your chair and be told no by the woman you dismissed, and everyone will see you bear it."''',
      c('[Agree] "Refuse me in front of all of them. I\'ll bear it."', "yes", flags=("konomi.committed",)),
      c('[Balk] "Not in front of the council."', "no")),
    k("yes", '''{n}She reads your face the way she reads a treaty, from the last line backwards, and finds what she wanted in it.{/n}
"Then we are agreed." {n}Her ears tip back, pleased, and this time she lets them.{/n} "Come here, Commander. I have been told no by nobody tonight, and I intend to keep it that way."
{n}She rises out of the chair and out of the outer robe in the same motion, lets it pool on the ledger, and pulls you down into the chair she has just left. The silk underneath goes over her head; the rings stay on. She strips your shirt off you with none of the patience she spends on treaties, settles bare across your lap with one knee either side of you and her tail sweeping the floor behind her, takes your hands and puts them on her hips, and sinks down against you with a low, satisfied sound.{/n}''',
      c("Continue", "council", forbids=(SETTLED,)),       # retired by gating (index kept): the morning comes first
      c("Continue", "a_season_morning")),
    k("a_season_morning", '''{n}Morning. She has taken the good side of your bed and the better half of your blanket, and she is reading your dispatches over your shoulder before you are awake enough to stop her.{/n}
"You write 'regret' when you mean 'refuse'. I shall correct that." {n}She does not get up. She hooks her ankle over yours instead, so that you cannot either.{/n} "The levy is on the council's list for this morning. Remember what you promised."''',
      c("Continue", "council")),
    k("council", '''{n}At the next council she refuses your recommendation on the winter levy, in full session, in four crisp sentences. You thank her and move to the next business. Three lords stare at you until the session ends. She does not look at you once, and her tail, under the table, is curled round your boot the whole time.{/n}''',
      c('"Next business."')),
    k("no", '''"Then you have asked as a Commander after all."
{n}She takes the fan off the page and closes the ledger over the date.{/n}
"I will be at the council table, Commander, as your envoy. That is all I will be. I do not bargain twice for the same thing."''',
      c('"Understood."', flags=(ENVOY,))),
], requires=("trickster.ever", SETTLED, DECLINED), forbids=("konomi.committed", ASKED_AGAIN, ENVOY), delay=168, own=DEVICE_OWN)


# --- State dead_retained: recalled for consultations (F17) --------------------------------------------------------

# A Recovery scene (existing Revivals entry): her soul refuses the killer's recall, then consents on her own terms. The
# consular rider paid to overtake the dispatch is the only line Arsinoe's ledger bills (ledger row 8; no temple fee).
letter("konomi.trickster.dead.recalled", "For consultations", [
    nar("start", '''{n}They have laid Lady Konomi out in the council chamber, because nobody could decide whose chapel an attaché from Nerosyan belonged in. Her fan is folded on her breast. Someone has closed her eyes and not quite managed her mouth, which still looks as if it has one more objection.{/n}
{n}A clerk is writing her dispatch to the capital at the end of the table: DECEASED AT HER POST. A second copy has already gone out by the east gate with the morning rider.{/n}''',
      c('[Stop the clerk mid-word] "Wait. Tear that up. And send a rider after the other one."', "recall",
        crusade=("Finances", -300), forbids=(RECALLED,), flags=(PRIMED, RECALLED, "konomi.started")),
      c('[Stop the clerk mid-word] "Wait. Tear that up."', "recall", requires=(RECALLED,)),
      c('[Let the clerk finish.] "..."', abort=True)),
    nar("recall", '''{n}The consulate's fastest rider goes out by the same gate at a cost the treasurer reads twice. The clerk tears his copy in half and waits, pen raised, to be told what to write instead.{/n}
{n}You do not speak to him. You speak to her, in the form her office taught her to answer: the form in which one court informs another that its envoy is not lost, only detained.{/n}''',
      c('[Correct the dispatch] "Lady Konomi isn\'t dead. She has been recalled for consultations. With me."', "refusal",
        mythic="Trickster", forbids=(DEAD,)),       # retired by gating (index kept): the rite comes first now
      c('[Let the clerk finish after all.]', abort=True),
      c('[Open her ledger] "Before anyone writes anything else. Where does she spend her money?"', "ledger")),
    nar("ledger", '''{n}Her ledger is on the table beside her, where the clerk laid it, because nobody knew whose it now was. It is exact to the copper and written in a hand that forgives nothing. Most of it is the crusade's business.{/n}
{n}One line is not. Every week, since her first week in Drezen: "To the lamp-seller on the chancery steps, for oil." Konomi's office has never once burned a lamp of its own; she complains about the crusade's oil at every council. She has been paying somebody for something else.{/n}''',
      c('[Go down to the chancery steps yourself]', "lamp")),
    nar("lamp", '''{n}The lamp-seller is an old woman with a tray of cheap oil and very bright eyes, who has sat on the chancery steps every day that you can remember and whom you have never once looked at. She looks at the ledger in your hand, and then at you, and the smile she gives you is Konomi's, older.{/n}
"We live everywhere, Commander. Most people never notice us. She always did." {n}She stands and shoulders her tray.{/n} "We will call her. Our way, with our words and your diamonds. What she says when she hears us is hers. And our price is that you never ask who we are, and never write one of us down."''',
      c('[Pay their price, and the diamonds] "I never saw you. Bring her home."', "rite", flags=(LAMP,),
        crusade=("Finances", -500)),
      c('[Let them be.] "..."', abort=True)),
    nar("rite", '''{n}They come at midnight: the lamp-seller and three others you have walked past a hundred times, a scribe, a laundress and a boy who holds horses at the gate. They send the clerk out. They grind the diamonds you bought them in a bowl of Nerosyan lacquer, and burn the dust in the oil of a lamp from the tray, and then the old woman speaks Konomi's name, and her rank, and the name of her post, the way one court informs another that an envoy is not lost, only detained.{/n}
{n}You speak last, in the same form. They let you.{/n}''',
      c('[Correct the dispatch] "Lady Konomi isn\'t dead. She has been recalled for consultations. With me."', "refusal",
        mythic="Trickster")),
    nar("refusal", '''{n}The hand on the fan does not move. The lamp gutters, as if a door has opened somewhere that is not in this room. Out of the old woman's mouth, faint and very dry, in a voice that is not the old woman's, comes a voice you know:{/n}
"Recalled? Only Nerosyan recalls me, Commander. I died at my post in your war, on your business. I see no reason whatever to consult."''',
      c('[Name the terms] "Consultations at your rate, then. Name it."', "fee", flags=(FEE,)),
      c('[Let her go] "...Then rest, Lady Konomi."', abort=True)),
    nar("fee", '''{n}A silence long enough to be a negotiating position.{/n}
"...Triple the standard rate for consultations. In advance: now, into my drawer, before I open my eyes. And the recall is entered as my decision. Not yours. Mine. I will not be the woman who came back because a Commander with a joke told her to."
{n}The old woman's eyes are closed. The others have not breathed for some time.{/n}''',
      c('[Agree to her fee] "Triple. In advance. Your decision, on the record."', "record", alignment=("Chaotic", 1),
        crusade=("Finances", -300))),
    nar("record", '''{n}The old woman opens her eyes and blows out the lamp. In the dark, a dead woman's hand turns on the folded fan, very slightly, palm-up, the way an attaché receives a sealed dispatch.{/n}
{n}In the morning the clerk crosses out DECEASED. Above it, in his best hand, at the dictation of the Commander, he writes: FOR CONSULTATIONS, AT HER OWN REQUEST. There is nobody on the chancery steps. There never was.{/n}''',
      c('[Let her come back.]', revive="konomi", flags=(CONFIRMED,))),
], requires=("trickster", DEAD), forbids=(CONFIRMED,), delay=0,
   chapters=(3, 5), Recovery="konomi", TricksterDevice=True, TricksterState=DEAD, own=DEVICE_OWN)

physical("konomi.trickster.dead.consultation", "Triple, in advance", '"You asked for consultations."', [
    k("start", '''{n}She is at her desk, alive and very displeased about the manner of it. There is colour in her face and ink on her fingers. The dispatch with the crossed-out word is pinned to the wall behind her, where she can see it and so can everyone who comes in.{/n}
"'Recalled for consultations.' You have committed a diplomatic impertinence on my corpse, Commander, and I accepted it on terms, which you have met. I counted."
{n}She opens the fan. Her hand is not quite steady; she lets you see that, and dares you to mention it.{/n}
"The fee was triple, in advance, and it is in my drawer. Now we consult. I have a great many questions about the afterlife and very few of them are theological."''',
      c('[Consult] "You asked for consultations. I\'m here to consult."', "unpaid", forbids=(CONFIRMED,)),     # retired
      c('[Pay the fee first] "The fee, as agreed. In advance."', "paid", crusade=("Finances", -300), forbids=(CONFIRMED,)),
      c('"The fee was paid before you came back. Ask your questions."', "paid")),
    k("unpaid", '''"Without paying first. Naturally."
{n}She writes a figure in the margin of the dispatch and underlines it twice.{/n}
"It will accrue. Sit down, Commander. We shall begin with why I died at my post, and we shall end, if you are fortunate, with whether I intend to hold it against you. I have not decided. I am enjoying not having decided."
{n}She taps the dispatch on the wall.{/n} "That stays there while I hold this office. Every envoy who sits in that chair will read it and ask. I shall tell each of them the truth."''',
      c('"Then let\'s begin."', flags=(RETURNED,))),
    k("paid", '''{n}She unlocks the drawer, so that you can see the coin is still there, and locks it again.{/n}
"...Paid, before I would open my eyes. How unexpectedly honest of you. I shall have to recalculate you."
"Sit down. We shall begin with why I died at my post in your war. You may take as long as you like; I am billing by the hour."
{n}She taps the dispatch on the wall.{/n} "That stays there while I hold this office. Every envoy who sits in that chair will read it and ask. I shall tell each of them the truth."''',
      c('"Then let\'s begin."', flags=(RETURNED, FEE_PAID))),
], requires=("trickster.ever", PRIMED, CONFIRMED, RECALLED),
   forbids=(DEAD, RETURNED, "konomi.return_first_words", "konomi.missed_letter_sent"), delay=12, chapters=(3, 5), own=DEVICE_OWN)


# --- State never_arrived: credentials deemed presented (F03, the chancery's informer) ------------------------------

letter("konomi.trickster.never_arrived.accredited", "Deemed presented", [
    nar("start", '''{n}The war council sits. At the foot of the table there is a chair for Nerosyan's attaché, because on the day your council first sat you had one set for Nerosyan's attaché, a courtesy to the Crown that cost nothing, and the steward keeps a courtesy the way other men keep saints' days. Nobody has ever come to sit in it. Somebody has put a jug on it.{/n}
{n}The steward sets her place anyway, every session: a cup, a pen, a sheet of the Crown's paper. He is a quiet old man who came with the Queen's household and has never once been asked to leave a room. He stands behind the empty chair through every council, and when the council rises he is the last out of the room.{/n}
{n}Today, on the chancery stair, a slip of paper falls from his sleeve.{/n}''',
      c('[Bow to the empty chair, with the steward behind it] "Lady Konomi\'s credentials are hereby deemed presented. Someone tell her she\'s late for her own audience."',
        "nerosyan", mythic="Trickster", alignment=("Chaotic", 1), forbids=("konomi.missed_contact_available",)),  # retired
      c('[Move the jug and carry on.] "..."', abort=True),
      c('[Put your boot on the slip before he can stoop for it]', "slip")),
    nar("slip", '''{n}He stops. So do you. You pick it up and read it on the stair, in front of him: today's council, in a small Nerosyan court hand, down to who coughed and who argued the levy and which way the Queen's man looked when he lost. It is addressed to nobody. It does not need to be.{/n}
{n}You fold it and give it back to him without a word. He takes it without one. His hands are quite steady; his ears are not.{/n}''',
      c('[Let him go up to his dovecote. Tomorrow, give him something worth sending.]', "bow", flags=(SLIP,))),
    nar("bow", '''{n}The next morning the council sits. The steward is behind the empty chair, laying a cup and a pen and a sheet of the Crown's paper for nobody, as he has every session since your council first sat.{/n}''',
      c('[Bow to the empty chair, with the steward behind it] "Lady Konomi\'s credentials are hereby deemed presented. Someone tell her she\'s late for her own audience."',
        "nerosyan", mythic="Trickster", alignment=("Chaotic", 1))),
    nar("nerosyan", '''{n}The council laughs politely. You bow to the jug anyway, properly, from the waist, and hold the bow long enough to be sure of the one man in the room who did not laugh. Behind the chair the steward has gone very still, the way a fox goes still in long grass.{/n}
{n}You find him that evening in the dovecote above the chancery, with a bird in his hands and a slip already rolled on its leg. He does not pretend to be feeding it. He has been sending your council's business to the Chancellor's office in Nerosyan without your leave or the Queen's, and what a crusade does to a man who sells its council is whatever its Commander says. You both know which Commander he has.{/n}''',
      c('[Pay him to send it word for word] "Add a line to tonight\'s report. The Commander presented Lady Konomi\'s credentials in full council. To a jug. Word for word."',
        "sent_paid", crusade=("Finances", -100),
        flags=(PRIMED, ACCREDITED, "konomi.missed_letter_sent", "konomi.started", STEWARD_PAID)),
      c('[Threaten him with the rope] "Send it word for word. Then pack. If you are in Drezen at dawn, I find out how well you hang."',
        "sent_burned", alignment=("Evil", 1),
        flags=(PRIMED, ACCREDITED, "konomi.missed_letter_sent", "konomi.started", STEWARD_BURNED))),
    nar("sent_paid", '''{n}He names a price exactly one copper higher than you expected and takes it without counting. The bird goes out over the lower town into the dark. In the morning he is at his post behind the chair, laying a cup and a pen for nobody, and every word your council says from now on goes up that ladder with your blessing.{/n}
{n}Two days after your bow, in Nerosyan, the Chancellor's office reads the dovecote's report, as it reads every report from that dovecote, and enters in its register, column four: 'Drezen: credentials presented.' The Commander of the crusade said it in full council, before witnesses. In Nerosyan a thing the Commander says in full council is protocol until someone proves otherwise, and nobody in the Chancellor's office wants the work.{/n}''',
      c("Continue", forbids=(ACCREDITED,)),     # retired (PP5): the clerk's note is this letter's last page
      c("Continue", "clerk")),
    nar("sent_burned", '''{n}He sends it. His hands are steady on the bird and on nothing else. In the morning the place behind the chair is empty. Someone has laid a cup and a pen for the attaché, out of habit, and the chancery spends a week finding out that the only man who knew where every key was kept has gone, and taken none of them with him.{/n}
{n}Two days after your bow, in Nerosyan, the Chancellor's office reads the dovecote's last report and enters in its register, column four: 'Drezen: credentials presented.' The Commander of the crusade said it in full council, before witnesses, and in Nerosyan that is protocol until someone proves otherwise. A second slip comes in on the same bird, in the same hand, smaller. It is the Commander's name.{/n}''',
      c("Continue", forbids=(ACCREDITED,)),     # retired (PP5)
      c("Continue", "clerk")),
    # PP5 (tier-A Ch5 budget): the arrival note folds into the setup instead of riding as a second letter.
    nar("clerk", '''{n}The account ends with a note from the chancery clerk, dated four days after your bow, a little after noon: a kitsune in travelling silks came in by the east gate with Nerosyan's seal on her papers, walked into the attaché's office as if she had the key, and has been there since. She has asked for tea and for you, in that order.{/n}''',
      c("Continue", flags=(ARRIVED,))),
], requires=("trickster", "konomi.missed_contact_available", MISSED_LATCH),
   forbids=("konomi.present", "konomi.dismissed", "konomi.missed_contact_invalidated", RETURNED, ACCREDITED), delay=96,
   chapters=(3, 5), TricksterDevice=True, TricksterState="konomi.missed_contact_available")

physical("konomi.trickster.never_arrived.audience", "Late for her own audience", '[Greet the woman in the attaché\'s office.]', [
    k("start", '''{n}A kitsune in travelling silks is standing in the attaché's office, kept swept for an attaché who never came, with a ledger under her arm and a dovecote's copy of your bow laid open on the desk.{/n}
"Lady Konomi, official attaché of Nerosyan. Here are my credentials." {n}She holds out her credentials. The date on them is the day the Chancellor's clerk entered your bow in his register.{/n} "Though I understand they have already been presented. By you. To a jug."
"I was halfway through a reception in Nerosyan when the Chancellor's clerk showed me his register. Column four: 'credentials presented, Drezen', entered on the strength of a report from our dovecote in your chancery. My people live everywhere, Commander. You are not supposed to be aware of it. One of them has stood behind that chair since your council first sat, and nobody in this city has ever looked at him twice. You looked. Then you used him to send me an invitation by my own post."
"He is either richer or gone. I have not yet decided which of those I shall bill you for."
{n}Her smile is small, sharp and entirely pleased with itself.{/n}
"The journey is on your account, Commander. So is the reception I left. It was a very good reception."
"And one thing more. On the strength of that register, the Chancellor's office has stopped paying my stipend in the capital from the day it was entered, and begun charging it to Drezen. They would like to know why you never reported my arrival. So, frankly, would I."''',
      c('[Receive her] "Welcome to your audience, Lady Konomi. You\'re late."', "received"),
      c('[Pay for her journey] "The journey is on my account. Name the sum."', "journey", crusade=("Finances", -200))),
    k("received", '''"Late. For an appointment I never made, in a city I had never seen, to a Commander I had not met."
{n}She inclines her head exactly as far as protocol requires, and not one finger further.{/n}
"You have an extraordinary way of issuing invitations. I shall find out whether you have an ordinary way as well. I have taken rooms in the lower town while I decide. You may write to me there, and I shall choose whether to answer."''',
      c('"I\'ll write."', flags=(RETURNED, "konomi.missed_appointment"))),
    k("journey", '''{n}She names it. It is exactly what the journey cost, to the copper, with the reception added at a rate that suggests it was a very good reception indeed.{/n}
"How refreshing. Most people in Mendev argue with the second figure."
"I have taken rooms in the lower town while I decide what you are. You may write to me there, and I shall choose whether to answer."''',
      c('"I\'ll write."', flags=(RETURNED, "konomi.missed_appointment", JOURNEY))),
], requires=("trickster.ever", PRIMED, ACCREDITED, "konomi.missed_letter_sent", ARRIVED),
   forbids=("konomi.present", RETURNED, "konomi.missed_contact_invalidated", CONFIRMED, "konomi.presence.failed"), delay=0,
   chapters=(3, 5))

letter("konomi.trickster.never_arrived.audience_letter", "Late for her own audience", [
    nar("start", '''{n}A letter in a Nerosyan court hand, delivered by the chancery boy, who will not meet your eye: Lady Konomi, official attaché of Nerosyan, has taken rooms in the lower town, since the attaché's office in the citadel is, in her words, "occupied by a jug".{/n}
{n}"My credentials were presented, I am told, by you. The journey and the reception I left are on your account. You may write to me here, and I shall choose whether to answer. K."{/n}''',
      c('"I\'ll write."', flags=(RETURNED, "konomi.missed_appointment"))),
], requires=("trickster.ever", PRIMED, ACCREDITED, "konomi.missed_letter_sent", ARRIVED, "konomi.presence.failed"),
   forbids=("konomi.present", RETURNED, "konomi.missed_contact_invalidated", CONFIRMED), delay=0, chapters=(3, 5))


# Q12 (Sol COX/HOW): the never-arrived road rejoins the ordinary missed-contact chain, whose letters alone outrun the shared
# chain budget. This Trickster beat is that road's own short way to an answer: her account for the jug, settled at her desk,
# and a supper she sets the terms of. Her terms accepted, she is eligible for her page (late_committed); "business only"
# makes her the envoy; "not tonight" leaves it open. The ordinary chain stays available alongside it.
ROOMS_KEPT = "konomi.trickster.rooms_kept"
physical("konomi.trickster.never_arrived.rooms", "The account for the jug", '"You sent for me, Lady Konomi?"', [
    k("start", '''{n}She has her ledger open on the desk and a second one, thinner, beside it. The thin one has your name on the cover in her court hand.{/n}
"Your account, Commander. The journey. The reception I left, at the rate of a good reception. Struck through, both, if you have paid them already; I keep honest books when someone is watching. The stipend the capital stopped paying me from the day of the register entry you arranged." {n}She turns it round with one finger.{/n} "And a line at the bottom I have not yet priced: one attaché, invited by her own post, by a Commander she had never met, to a city she had never wished to see. I do not know what that costs. I should like to find out."''',
      c('[Pay it as written] "Every line. Including the one you haven\'t priced."', "paid", crusade=("Finances", -150),
        forbids=(JOURNEY,)),
      c('"Spoken like a true politician. Let\'s talk price."', "haggle", forbids=(JOURNEY,)),
      c('"Not tonight, Lady Konomi."', abort=True),
      # Appended (Sol BEL): the audience already paid the journey and the reception; only the stipend is left.
      c('[Pay what is left] "The stipend, then. And the line you haven\'t priced."', "paid_rest", crusade=("Finances", -50),
        requires=(JOURNEY,)),
      c('"Spoken like a true politician. Let\'s talk price."', "haggle_rest", requires=(JOURNEY,))),
    k("paid_rest", '''"The stipend." {n}She writes PAID beside it in a hand that does not hurry, under the two lines already struck through.{/n} "You paid the first figure at my door and the second here. Nobody in Mendev does that twice. I am beginning to think it is a habit." {n}She taps the last line with her fan.{/n} "That one I still have not priced."''',
      c("Continue", "terms")),
    k("haggle_rest", '''{n}Her ears come up, very slightly.{/n} "That is my line, Commander. You will pay a royalty on it."
{n}There is not much left to fight over: the journey and the reception are struck through, paid at her door. You argue the stipend down to the day the register was entered; she argues it back up to the day she would have been paid, and wins. When the candle is half gone there is one line left, the unpriced one, and she taps it with her fan.{/n}''',
      c("Continue", "terms", crusade=("Finances", -25))),
    k("haggle", '''{n}Her ears come up, very slightly.{/n} "That is my line, Commander. You will pay a royalty on it."
{n}You go through the account line by line. She concedes the reception and wins the stipend back with interest; you win the journey; she wins it back by pointing out that you never asked whether she wanted to come. When the candle is half gone there is one line left, the unpriced one, and she taps it with her fan.{/n}''',
      c("Continue", "terms", crusade=("Finances", -100))),
    k("paid", '''"Every line." {n}She looks at the ink as if it might be forged.{/n} "Nobody in Mendev pays the first figure. You have either a great deal of money or a very poor sense of how to keep it." {n}She taps the last line with her fan.{/n} "That one I still have not priced."''',
      c("Continue", "terms")),
    k("terms", '''"Here are my terms for it." {n}She closes the thin ledger.{/n} "Supper. Here, at this desk, once a week, at your expense, until one of us loses an argument we both care about. You may not bring your advisers. I may not bring my correspondents. Whoever concedes first pays for the wine."
{n}She does not look away while she says the rest, which costs her something.{/n} "Since I came through your gate this city has looked at me as a clerical error with ears. I should like one person in it to look at me across a table as something else." {n}She lets that stand, and does not dress it.{/n} "Those are my terms."''',
      c('[Accept her terms] "Done. I\'ll bring the wine; I expect to pay for it."', "accept", flags=(ROOMS_KEPT,),
        forbids=(ACCREDITED,)),   # retired (PP5 r2): the first supper comes first
      c('"Business only, Lady Konomi. The council table is enough."', "business", flags=(ENVOY,)),
      c('[Accept her terms] "Done. I\'ll bring the wine; I expect to pay for it."', "supper")),
    k("supper", '''"Then the first supper is tonight," she says, "and you are late for it."
{n}She sends the chancery boy for bread, cold fowl and a wine she names without looking at any list, and clears exactly half the desk. The other half keeps her ledger, open.{/n}
{n}She eats the way she argues, neatly and without wasting anything, and lets you talk about the council for the length of one glass. Then she sets her cup down.{/n}
"You could have left the jug in that chair until the war ended. Nobody at your table would have noticed. Why did you want a stranger there, Commander? Not Nerosyan. A stranger."''',
      c('"Everyone at that table agrees with me eventually. I wanted someone who wouldn\'t."', "supper_no"),
      c('"I wanted to know who Nerosyan would send. Now I want to know who you are."', "supper_who"),
      c('"The chair was an excuse. You were the reason, once you walked in."', "supper_you")),
    k("supper_no", '''"Someone who will not." {n}She considers you over the rim of the cup.{/n} "Then you have chosen badly, Commander. I disagree for a living, and I charge for it. Tonight I am disagreeing for nothing, which my Chancellor would call a scandal."
{n}She does not, you notice, ring for the plates to be cleared.{/n}''',
      c("Continue", "stay")),
    k("supper_who", '''"Who I am." {n}Her ears turn, very slightly, toward you.{/n} "That is a longer account than this one, and I do not hand it to people who have only paid for the journey."
{n}She refills your cup without being asked, which in Nerosyan is a concession, and leaves the bottle on your side of the desk.{/n}''',
      c("Continue", "stay")),
    k("supper_you", '''"An excuse." {n}She sets her fan down on the ledger, closed.{/n} "You bowed to a jug in full council as an excuse."
{n}For a moment she looks as though she means to bill you for it. Then she laughs, low, the first unguarded sound you have heard from her.{/n} "Nobody has ever gone to so much trouble to be rude to me."''',
      c("Continue", "stay")),
    k("stay", '''{n}The candle is half gone. The chancery boy comes back for the plates and is sent away again without them.{/n}
"The terms said supper," she says. "They said nothing about when supper ends."''',
      c("[Stay.]", "accept", flags=(ROOMS_KEPT,))),
    nar("accept", '''{n}She comes round the desk, takes the account out of your hand and drops it in the drawer, and then takes you by the front of your coat and walks you back until the edge of her desk is behind your knees. Her rings come off one at a time into the inkwell lid, unhurried, as if she were laying down a hand of cards. The court silks go over her head; she sweeps the ledger off the desk with her tail and sits you down on the cleared wood, and settles across your lap with one knee either side of you, and puts her hands flat on your chest as if she were still deciding the price.{/n}
{n}"I lose this argument," she says against your mouth, "on purpose. Do not get used to it," and pushes you down.{/n}''',
      c("Continue", "morning")),
    k("morning", '''{n}In the morning she is at the desk again, dressed, writing, with your coat over the back of her chair as if she had won it.{/n}
"I have entered last night as a supper," she says, without looking up. "The wine is on your account. The rest is not for sale." {n}Her ears are pink to the tips.{/n} "Same time next week, Commander. Do not be late twice."''',
      c('"Same time next week."', flags=("konomi.lovers",))),
    k("business", '''"Business only." {n}She opens the thin ledger again and writes one line in it, very neatly.{/n} "Then I shall be your envoy, Commander, and Nerosyan shall have my honest opinion of you every week, in cipher. You will not enjoy it."''',
      c('"I\'m sure it will."')),
], requires=("trickster.ever", RETURNED, ACCREDITED, "konomi.missed_appointment"),
   forbids=("konomi.lovers", "konomi.committed", ROOMS_KEPT, ENVOY, DECLINED, "konomi.presence.failed", "konomi.private_departed"),
   delay=72, chapters=(3, 5))

# PP5: kept for saves between the bow and her arrival; the setup now sets ARRIVED itself.
letter("konomi.trickster.never_arrived.arrival", "A stranger in the attaché's office", [
    nar("start", '''{n}A note from the chancery clerk: a kitsune in travelling silks came in by the east gate at noon with Nerosyan's seal on her papers, walked into the attaché's office as if she had the key, and has been there since. She has asked for tea and for you, in that order.{/n}''',
      c("Continue", flags=(ARRIVED,))),
], requires=("trickster.ever", ACCREDITED, "konomi.missed_letter_sent"), forbids=(ARRIVED, RETURNED), delay=48,
   chapters=(3, 5))


# --- Epilogue: paragraphs on her registered endings, and her own pages (R2-6) ---------------------------------------

TRICKSTER_PARAGRAPHS = (
    p("Lady Konomi reached Nerosyan eventually. She never explained the delay, and she billed the crown for three days of "
      "travel that had taken her nowhere.", requires=(RECESSED,), forbids=(OUTFOXED,)),
    p("In Nerosyan they said the new envoy to Drezen had been appointed by the Commander, at her own suggestion, on terms "
      "nobody else was shown.", requires=(RECESSED, OUTFOXED)),
    p("She kept the unnamed favour for years, and mentioned it only when the Commander seemed in danger of forgetting it.",
      requires=(FAVOUR,)),
    p("Nerosyan's archive holds one dispatch with a word crossed out and six words added at a dead woman's request. Lady Konomi had "
      "it framed, and billed the crown for the frame. Every envoy who ever sat across from her read it, and asked, and was "
      "told plainly that she had died at her post and come back on her own fee. None of them ever again quite trusted a "
      "Commander who could afford it.",
      requires=(RETURNED, RECALLED)),
    p("In the Royal Council's register for that year, column four still reads 'credentials presented, Drezen', entered from "
      "a dovecote's report two days before anyone left the capital. Auditors query it every spring. Lady Konomi signs the "
      "query every spring, and sends it back.", requires=(RETURNED, ACCREDITED)),
)

SCENES.append(scene("konomi.trickster.epilogue.commit", "Accepted in advance", "Epilogue", 5, "", [
    nar("offer", '''{n}Lady Konomi came back to Drezen after the war as envoy of a Nerosyan that had learned to read the Commander's letters very carefully.{/n}
{n}She asked the question herself, in a sealed dispatch addressed to the Commander in person, not to the Commander's office. It was two lines long. She did not wait for the courier to leave before adding a postscript: 'Accepted in advance.'{/n}''',
      c('[Ride to Nerosyan and answer it at her door.]', "signed"),
      c('[Send it back with terms of your own.]', "terms"),
      c('[Send it back unsigned, folded round an invitation to dinner.]', "dinner")),
    nar("signed", '''{n}The Commander answered it in person, on the steps of the Nerosyan embassy, overtaking the courier on the road to do it. She heard the answer in her own doorway, in front of her whole staff, and laughed out loud, which nobody in Nerosyan had ever heard her do.{/n}
{n}She kept her rooms, her correspondents and her opinions, and delivered all three at breakfast. The dispatch hung framed above the desk they shared. Visitors assumed it was a treaty. In a sense it was.{/n}''',
      c(), paragraphs=TRICKSTER_PARAGRAPHS),
    nar("terms", '''{n}The Commander sent it back with a single clause added: 'Not to be recalled by anyone. Including me.'{/n}
{n}She arrived the next morning with the dispatch in one hand and her travelling case in the other, and read the clause aloud in the doorway, twice, the way she read treaties. Then she set the case down.{/n}
"That," she said, "is the first sensible thing you have ever written me."
{n}She stayed. She was never recalled by anyone again.{/n}''',
      c(), paragraphs=TRICKSTER_PARAGRAPHS),
    nar("dinner", '''{n}The Commander sent it back unsigned, folded round an invitation to dinner.{/n}
{n}She came to the dinner. She brought the dispatch, still unsigned, and laid it beside her plate, and they argued over it until the candles were out. Every year after there was another dinner, in Drezen or in Nerosyan, and the dispatch came too, a little more creased each time. It was never signed. It was never withdrawn. She said that was the most durable treaty she had ever negotiated, and billed the Commander for the candles.{/n}''',
      c(), paragraphs=TRICKSTER_PARAGRAPHS)],
    requires=("trickster.ever", LATE_COMMITTED), forbids=("konomi.committed", "konomi.closed", DECLINED, ENVOY, "sacrifice"),
    last=99, Relationship="konomi", ForbidOverrides={"sacrifice": "trickster.commander_back"}))

# Sol INT: the envoy she agreed to be, and nothing she did not.
SCENES.append(scene("konomi.trickster.epilogue.envoy", "Envoy, in triplicate", "Epilogue", 5, "", [
    nar("start", '''{n}Lady Konomi sat in the envoy's chair at the Commander's table until the Wound was closed, and after it, until Nerosyan ran out of reasons to recall her and she ran out of patience with its reasons. She regretted nothing in writing. She made the Commander regret the offer every week, in triplicate, with the capital copied in, exactly as promised.{/n}
{n}After the chair was agreed, they never dined alone again. She said it kept the accounts clean. The Commander, reading the weekly triplicate, suspected it kept her amused.{/n}''',
      c(), paragraphs=TRICKSTER_PARAGRAPHS)],
    requires=("trickster.ever", ENVOY), forbids=("konomi.committed", "konomi.closed", "sacrifice"), last=99, Relationship="konomi",
    ForbidOverrides={"sacrifice": "trickster.commander_back"}))

SCENES.append(scene("konomi.trickster.epilogue.refused", "Still negotiating", "Epilogue", 5, "", [
    nar("start", '''{n}Lady Konomi was never recalled by anyone again. She saw to that. Every spring the Commander received one dispatch from Nerosyan, correct in every particular and signed in her own hand, and every spring it ended the same way: 'Still negotiating.'{/n}''',
      c(), paragraphs=TRICKSTER_PARAGRAPHS)],
    requires=("trickster.ever", DECLINED), forbids=("konomi.committed", ENVOY, "sacrifice"), last=99, Relationship="konomi",
    ForbidOverrides={"sacrifice": "trickster.commander_back"}))


# Sol r4 BEL: the Commander's death with no prepared return is her loss, not a living future.
SCENES.append(scene("konomi.trickster.epilogue.sacrifice", "An account left open", "Epilogue", 5, "", [
    nar("start", '''{n}Lady Konomi read the dispatch from the Wound in her own office, standing, and then sat down, which nobody on her staff had seen her do in the middle of a working day.{/n}
{n}She finished the war's paperwork. She closed every account the Commander had left open with Nerosyan, to the copper, and signed each one herself. The last she kept in her desk, unsigned, for the rest of her life: a supper the two of them had agreed on and never eaten.{/n}''',
      c())],
    requires=("konomi.committed", "sacrifice"), forbids=("trickster.commander_back", "konomi.closed", "ascended", "inhuman"), last=99,
    Relationship="konomi"))


# --- Reactions (05 section 3.1: exactly Regill and Kyado) ---------------------------------------------------------

REACTIONS = [
    reaction("Regill", "konomi.trickster.dismissed.react_regill", (RECESSED, "konomi.dismissed"),
             '''{n}Regill's pale yellow eyes settle on you with an expression of polite attention that is not polite at all.{/n}
"You dismissed the attaché of Nerosyan before your own council, and then retained her with a bribed carter and a minute that lies by being accurate. Either decision alone I could respect. Together they are contempt of your own order."
"And you have told every man on the east gate that the Commander's word at the war table can be revised by a carter's purse. My sergeants will need to be told otherwise. I will tell them. You will not like how."''',
             answer_list=REGILL_HUB, forbids=REGILL_GONE, chapter=5, last=5, entry='"About Lady Konomi..."'),
    reaction("Kyado", "konomi.trickster.dismissed.react_kyado", (RECESSED, "kyado.in_drezen", KYADO_SAID_IT),
             '''{n}Kyado has heard. Everyone in the lower town has heard. He does not laugh; he looks at you the way he looked at you once in the temple, as if you were weather.{/n}
"I warned you, Commander. Back at the temple, about your tricks. I thought you'd at least use magic."
"The fox lady's driver came to me for absolution. He took your silver to drive the charcoal loop and swear he never turned the horses. Erastil keeps the roads for honest travellers, I told him, and gave him a penance: to tell her himself." {n}He hesitates.{/n} "I hope she made you pay for it."''',
             answer_list=KYADO_HUB, forbids=("kyado.dead",), chapter=5, last=5, entry='"About Lady Konomi..."'),
    reaction("Regill", "konomi.trickster.dead_retained.react_regill", (CONFIRMED, RECALLED),
             '''{n}Regill does not look up from his report.{/n}
"A death is a record, Commander. You had it amended, and the deceased invoiced you for the correction."
{n}He turns a page.{/n}
"What concerns me is the other matter. Four civilians nobody can name held a rite in your council chamber at midnight, and the clerk was sent out. The chamber was unguarded while they did it. The attaché is alive; I accept that. I do not accept that you will not tell me who they were. Double the watch on that door, or I will."''',
             answer_list=REGILL_HUB, forbids=REGILL_GONE, chapter=3, last=5, entry='"About Lady Konomi..."'),
    reaction("Kyado", "konomi.trickster.dead_retained.react_kyado", (CONFIRMED, RECALLED, "kyado.in_drezen"),
             '''{n}Kyado sets down the ledger he was reading and folds his hands on it, the way a prior folds his hands, though he gave that office up.{/n}
"They say she was dead, and then she was expensive."
"Erastil says the dead should be let rest. He also says a debt is a debt." {n}He frowns at his hands.{/n} "I don't know which of those you kept, Commander. I think she does. Ask her before you ask me."''',
             answer_list=KYADO_HUB, forbids=("kyado.dead",), chapter=3, last=5, entry='"About Lady Konomi..."'),
    reaction("Regill", "konomi.trickster.never_arrived.react_regill", (RETURNED, ACCREDITED, STEWARD_PAID),
             '''"Credentials are presented, or they are not, Commander. 'Deemed' is a word for people who have lost the argument."
{n}Regill's mouth tightens a fraction.{/n}
"And yet here she is, with Nerosyan's register to prove it. You found the Chancellor's informer in your own chancery and, instead of hanging him, made him your postman. A spy you let run is a door you left open, Commander. I shall want to know every other door in that chancery before the week is out."''',
             answer_list=REGILL_HUB, forbids=REGILL_GONE, chapter=3, last=5, entry='"About Lady Konomi..."'),
    reaction("Regill", "konomi.trickster.never_arrived.react_regill_burned", (RETURNED, ACCREDITED, STEWARD_BURNED),
             '''"Credentials are presented, or they are not, Commander. 'Deemed' is a word for people who have lost the argument."
{n}Regill's mouth tightens a fraction.{/n}
"And yet here she is. You found the Chancellor's informer in your own chancery, made him carry your message, and then put the rope in front of him and let him run. Crude. It shuts the door he used and tells his masters we found it. It does not tell me what he carried out with him, or who else Nerosyan keeps on our stairs. He will not tell me now. I shall find out the slow way."''',
             answer_list=REGILL_HUB, forbids=REGILL_GONE, chapter=3, last=5, entry='"About Lady Konomi..."'),
    reaction("Kyado", "konomi.trickster.never_arrived.react_kyado", (RETURNED, ACCREDITED, "kyado.in_drezen"),
             '''{n}Kyado laughs before he can stop himself, then looks guilty about it.{/n}
"You bowed to a jug, and a lady came. The whole lower town is telling it. Half of them think it was a miracle."
"It wasn't a miracle. Erastil doesn't send people to sit in chairs." {n}He sobers.{/n} "Be kind to her, Commander. She came a very long way to find out what you meant, and she didn't have to."''',
             answer_list=KYADO_HUB, forbids=("kyado.dead",), chapter=3, last=5, entry='"About Lady Konomi..."'),
]
SCENES.extend(REACTIONS)


# --- The registered route -----------------------------------------------------------------------------------------

# Superseded on Trickster (the spec's renamed ids; retired by gating, never deleted). A save already past one of them
# keeps its own continuation: fate_reply and the_answer_she_addressed are not gated. retained_attempt (a revive by
# Trickster power alone) is retired as well (polish 9b); dead.recalled no longer forbids its prepared path.
RETIRED = ("konomi.fate_post", "konomi.retained_inquiry", "konomi.the_unintroduced_letter", "konomi.retained_attempt")
ENDINGS = ("konomi.ending_public", "konomi.ending_private", "konomi.ending_changed", "konomi.ending_ascended",
           "konomi.ending_distance", "konomi.ending_distance_open", "konomi.ending_distance_lived",
           "konomi.ending_distance_open_lived")
LIVING_ENDINGS = ("konomi.ending_public", "konomi.ending_private", "konomi.ending_distance", "konomi.ending_distance_open",
                  "konomi.ending_distance_lived", "konomi.ending_distance_open_lived")
BURIED = "iomedae.trickster.buried_alive"
PUBLIC_BURIED_TEXT = (
    "{n}Lady Konomi wore black for the Commander of the Fifth Crusade for the full term the court allowed, and not a day "
    "longer, and wrote the Royal Council a memorandum on the cost of the funeral that is still cited in Nerosyan as a model of "
    "its kind.{/n}\n"
    "{n}She never became a reliable source of agreement with the person she wrote to afterwards, either. Her household knew "
    "there was someone: letters went out every week to a different waystation, sealed in plain wax and addressed to nobody, "
    "and twice a year the envoy took leave and went nowhere for a fortnight, and came back in a temper or in a very good mood, "
    "and was never asked which. Whoever it was argued with her as nobody else in Mendev dared to. She never named them. The few "
    "letters she left unsealed were burned unread when she died, on her own written instruction, by a servant who said "
    "afterwards that there had been a great many of them.{/n}")

AUDIENCE_ANSWER = '"You chose a better room than the attaché\'s office."'
COURTYARD_NODES = [
    k("again_audience", '''"I did. The office has a jug in it now, on a shelf, with a label. The chancery will not let anyone move it."
{n}She settles into her chair and arranges her sleeves.{/n}
"I have been received, Commander. I have presented my credentials twice, which is once more than any court has ever required of me. This afternoon I should like to find out what you are like when you are not bowing to crockery."''',
      c('"Then tell me about the work you chose."', "work"),
      c('"I would like to spend some of it simply enjoying your company."', "company")),
]


def _scene(by_id, id):
    if id not in by_id:
        raise ValueError("Konomi Trickster integration missing scene: " + id)
    return by_id[id]


def _node(scene_, id):
    return next(x for x in scene_["Nodes"] if x["Id"] == id)


def _gate(choice, forbids=(), requires=()):
    choice["Forbids"] = [*choice["Forbids"], *[f for f in forbids if f not in choice["Forbids"]]]
    choice["Requires"] = [*choice["Requires"], *[r for r in requires if r not in choice["Requires"]]]


def integrate(payload):
    """Save-safe edits to the registered route: no id, node or choice is renamed, removed or reordered. New choices are
    appended; the scenes and choices they replace on a Trickster run are gated off."""
    rel = payload["Relationships"]["konomi"]
    rel["TricksterAccess"] = {k_: dict(v) for k_, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, a dismissed Konomi may find the road back to Drezen longer than she "
                        "expected; a Konomi killed at her post may be called back by her own people, on her own terms; "
                        "and one who never came may find her credentials already presented.")
    payload.setdefault("Presences", {}).update({k_: dict(v) for k_, v in PRESENCES.items()})
    for key, cues in SEEN_CUES.items():
        payload.setdefault("SeenCues", {})[key] = list(cues)
    by_id = {s["Id"]: s for s in payload["Scenes"]}

    # The post office, the map and the unintroduced letter are the devices this route replaces on the Trickster path.
    for id in RETIRED:
        _scene(by_id, id)["Forbids"].append("trickster.ever")
    # A primed return is the consultation, not the letter; an accredited Konomi comes in person, not by carrier.
    _scene(by_id, "konomi.return_letter")["Forbids"].append(PRIMED)
    _scene(by_id, "konomi.the_answer_she_addressed")["Forbids"].append(ACCREDITED)

    # The courtyard knows she was received in person, not by an answered letter.
    courtyard = _scene(by_id, "konomi.the_courtyard_introduction")
    start = _node(courtyard, "start")
    _gate(start["Choices"][1], forbids=(ACCREDITED,))
    start["Choices"].append(c(AUDIENCE_ANSWER, "again_audience", requires=(ACCREDITED,)))
    courtyard["Nodes"].extend(COURTYARD_NODES)

    for id in LIVING_ENDINGS:
        s = _scene(by_id, id)
        s["Forbids"].append("sacrifice")
        s.setdefault("ForbidOverrides", {})["sacrifice"] = "trickster.commander_back"
    # R2-6: the late commit is her own page; the registered unfinished ending does not also play.
    _scene(by_id, "konomi.ending_unfinished")["Forbids"].append(LATE_COMMITTED)
    for id in ENDINGS:
        for node in _scene(by_id, id)["Nodes"]:
            if all(ch.get("Next") is None for ch in node["Choices"]):
                node.setdefault("Paragraphs", []).extend(dict(x) for x in TRICKSTER_PARAGRAPHS)


    # R6 (iomedae_trickster): in the world where the Commander walked out of the Wound and stayed buried, a relationship
    # "so well known that visitors arrived" cannot be the Commander's. Appended sibling of ending_public (which Forbids that
    # world); the conditional paragraphs are carried over unchanged.
    public = _scene(by_id, "konomi.ending_public")
    public["Forbids"].append(BURIED)
    buried = copy.deepcopy(public)
    buried["Id"] = "konomi.ending_public_buried"
    buried["Title"] = "Letters to nobody"
    buried["Forbids"] = [f for f in buried["Forbids"] if f != BURIED]
    buried["Requires"].append(BURIED)
    _node(buried, "start")["Text"] = PUBLIC_BURIED_TEXT
    payload["Scenes"].append(buried)

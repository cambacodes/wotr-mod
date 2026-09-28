"""Konomi on the Trickster path: recess, not farewell (Writer/handoffs/trickster/konomi.md, families F17 and F03).

Canon: the Commander dismisses the attache of Nerosyan with "you can go to the demons, Lady Konomi. Along with the entire
Royal Council." (Diplomacy_6/Answer_0070 73c5728c) and she answers "So be it. Farewell, Commander... I will make haste for
Nerosyan" (Cue_0075 384cd664). She prices everything: "Very well, let us talk price" (Diplomacy_4/Cue_0034 4652e021, with
"a smug, somewhat predatory smile"), and her people "live everywhere, you are just... not always aware of our existence"
(Diplomacy_Officer/Cue_0038 efe7fee4). Kyado names the Trickster's rule: "your tricks somehow become the truth" (Kyado_main_
dialogue/Cue_0109 509eac82, PlayerIsTrickster only). Authored, and labelled as authored: the road that takes a farewell at
its word; a soul that refuses a recall from her killer until she names her own fee (Pharasma's rule: only the willing
return); a secretary in Nerosyan who writes the wrong word in the right column. She prices, bills, refuses, and can walk away.
"""
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
JOURNEY = "konomi.trickster.journey_paid"
LATE_COMMITTED = "konomi.trickster.late_committed"
DEAD = "konomi.retained_dead"
CONFIRMED = "konomi.retained_return_confirmed"
KYADO_SAID_IT = "konomi.trickster.kyado_said_it"         # he said Cue_0109 to this Commander
GALFREY_GONE = ("galfrey.dead", "galfrey.killed_by_commander")
REGILL_GONE = ("regill.dead", "regill.kicked_out", "regill.left_plot")
OWN = ("konomi.closed", "konomi.farewell", "inhuman")

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
                            Requires=["trickster.ever", "konomi.trickster.presence_on"], Forbids=["konomi.closed"],
                            MinChapter=3, MaxChapter=5, AnswerLists=[HUB]),
}
SEEN_CUES = {KYADO_SAID_IT: ["509eac8248670664fab0808c3e00fe04"]}   # Kyado_main_dialogue/Cue_0109


def k(id, text, *choices, **kw):
    return n(id, "Konomi", text, *choices, portrait="Konomi", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Konomi", **kw)


def physical(id, title, entry, nodes, requires, forbids, delay, chapters=(5,), **extra):
    SCENES.append(scene(id, title, "Konomi", min(chapters), entry, nodes, requires=requires, forbids=(*OWN, *forbids),
                        delay=delay, last=max(chapters), optional=True, Relationship="konomi", Areas=[DREZEN],
                        Chapters=list(chapters), ContactUnit=UNIT, AnswerLists=[HUB], **extra))


def letter(id, title, nodes, requires, forbids, delay, chapters=(5,), **extra):
    SCENES.append(scene(id, title, "Konomi", min(chapters), "", nodes, requires=requires, forbids=(*OWN, *forbids),
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
{n}Somewhere under the gate a paving stone you have never noticed before sits a finger's width proud of the others.{/n}
{n}At the council table that morning the attaché's chair is empty. The clerk has the minute of her dismissal in front of him and his pen raised, waiting for the word.{/n}''',
      c("Continue", "queen", requires=("coronation.seen",), forbids=GALFREY_GONE),
      c("Continue", "record", forbids=("coronation.seen",)),
      c("Continue", "record", requires=("coronation.seen", GALFREY_GONE[0])),
      c("Continue", "record", requires=("coronation.seen", GALFREY_GONE[1]), forbids=(GALFREY_GONE[0],))),
    nar("queen", '''{n}The Queen is in Drezen this week, and sits in on the council this morning out of courtesy, to listen rather than to rule. It was her seal on the scroll Lady Konomi carried into this room on her first day.{/n}
{n}She raises one eyebrow at the empty chair, then at you, and says nothing at all.{/n}''',
      c("Continue", "record")),
    nar("record", '''{n}You tell him what to write. He writes it without looking up, because clerks who look up at the Commander's jokes are clerks who end up counting arrows in the Abyss.{/n}
{n}'Audience with the attaché of Nerosyan: adjourned.'{/n}
{n}He sands it. The word dries, and stays.{/n}''',
      c('[Minute it as a recess] "The record will show the audience was adjourned. Not ended."',
        flags=(PRIMED, LATE, "konomi.started"))),
], requires=("trickster", "konomi.dismissed", "konomi.office_completed", "konomi.dismissed.latched"),
   forbids=(LATE, RECESSED), delay=24, TricksterDevice=True, TricksterState="konomi.dismissed")

READ_TERMS = '''"Illusions are my people's prerogative, Commander, and they are never free. You have borrowed one without asking. Very well, let us talk price."
{n}She opens the fan and looks at you over the top of it.{/n}
"You have kept an attaché from her capital in the middle of a revolt. You dismissed her from a council table and adjourned her from a wall, in front of the watch. How very public. Nerosyan will want to know why I am late, and I shall want something to tell them."'''

# Dorgelinda's audit is read, never required (doc 03 §2.11).
DORGELINDA_PRIMED = "dorgelinda.trickster.primed"
LEDGER_TERMS = '''{n}She lets the fan fall shut against her palm.{/n}
"Your quartermaster tells me a warehouse walked into your personal account. You and she keep books the same way, Commander: one line for the Crusade, and one for what the Crusade does not know it has paid."'''

physical("konomi.trickster.dismissed.recess", "The third morning", '"Lady Konomi."', [
    nar("start", '''{n}Lady Konomi's carriage left Drezen by the east gate at dawn. At noon it arrived at Drezen by the east gate. The driver swore on his mother and on Erastil that he never turned the horses. At dusk it happened again.{/n}
{n}On the third morning she is standing in her old office in front of the swept desk, fan closed, travelling cloak still on. When you come in she steps back over the threshold and forward over it again, very deliberately, watching her own feet.{/n}
{n}She does not look pleased about it. She looks, if anything, interested, which is worse.{/n}''',
      c("Continue", "price")),
    k("price", '''"You told me to mind the step on my way back in. I have now minded it three times, Commander, and the capital is burning without me."
{n}Her smile is smug and faintly predatory, the one she used to save for the Royal Council's opponents.{/n}
"The driver has had a religious experience. The horses have not recovered. I have spent two nights at the same inn and been charged for three, which is the only part of this I understand. You will tell me it was chance."''',
      c('[Chance] "Chance. Drezen\'s roads are notoriously circular."',
        check=dict(Skill="CheckBluff", DC=30, Success="read", Failure="outfoxed", CommanderOnly=True)),
      c('[Tell her the truth] "I told you to mind the step. You didn\'t ask why."', "truth")),
    k("truth", '''"No. I did not."
{n}She closes the fan against her palm, one fold at a time.{/n}
"I heard a Commander being childish from a wall, and I let the curtain stay shut so that you could watch me not hearing it. I heard a jest. I did not hear a clause." {n}Something sharp and pleased moves behind her eyes.{/n} "I shall not make that mistake twice."''',
      c("Continue", "read")),
    k("read", READ_TERMS,
      c('[Hear her terms] "Name them."', flags=(RECESSED, DEBT), forbids=(DORGELINDA_PRIMED,)),
      c("Continue", "read_ledger", requires=(DORGELINDA_PRIMED,))),
    k("outfoxed", '''"Circular."
{n}She lets the word hang in the air a moment longer than it deserves.{/n}
"I saw the seam in your road on the second morning, Commander. A stone under the gate that was not there when I arrived in this city, and is there only for me. I stayed for the third turn to watch you work. You work very prettily. You also lie to a kitsune about an illusion, to her face, in her own office."
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
], requires=("trickster.ever", "konomi.dismissed", "konomi.office_completed", LATE),
   forbids=(RECESSED,), delay=48)

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
"The step will let me go this time, I think. You have made it very clear you do not want me back."''',
      c('[Let her go.]', flags=("konomi.closed",))),
], requires=("trickster.ever", RECESSED, "konomi.dismissed"), forbids=(SETTLED,), delay=48)

physical("konomi.trickster.dismissed.private", "Off the record", '"Business concluded?"', [
    nar("start", '''{n}Evening. The office is lit by one lamp. Her terms are entered in her own ledger, in her own hand, and the ledger is closed. The window is open on the square, where the watch is changing.{/n}''',
      c("Continue", "concluded")),
    k("concluded", '''"Business concluded, Commander. You are still here. So am I. One of us will have to explain that, and I should prefer it were not me."''',
      c('[Ask her to stay, for yourself] "Stay. Not for Nerosyan. For me."', "answer", requires=("konomi.lovers",)),
      c('[Ask her to stay, for yourself] "Stay. Not for Nerosyan. For me."', "courted", forbids=("konomi.lovers",)),
      c('[Ask her to stay as envoy] "Stay as Nerosyan\'s envoy. The chair is yours."', "envoy")),
    k("answer", '''{n}She does not answer at once. She opens the fan, and closes it, and sets it on her closed ledger as if it were a paperweight.{/n}
"Three days on your road, and you wait until the business is sealed to say it. You did the same at the council table: the price first, the thing you actually wanted afterwards, when there was nobody left to bargain with but me."
"Very well. My terms. I stay. I keep my own rooms, my own correspondents and my own opinions, and I shall give you all three at breakfast. And you never again dismiss me in front of a council. You may dismiss me in private. I shall enjoy watching you try."''',
      c('[Take her hand] "Then name the next evening."', "threshold", flags=("konomi.committed",)),
      c('[Ask what she wants] "What do you want, Konomi? Not the capital. You."', "no")),
    k("courted", '''{n}She looks at you for a long moment over the closed fan, as if you had put a clause in front of her in a language she reads well and did not expect to see here.{/n}
"You have never once asked me to supper, Commander. You dismissed me in front of a council. Then you turned a road round to fetch me back, and paid for it with a letter that will cost you your nobles' grain for a season."
"That is either the most romantic thing anyone has ever done for me or the most insulting. I have had three days on your road to decide which." {n}The corner of her mouth moves.{/n} "I have decided it is both, and that I will take it anyway. So. My terms."
"I keep my own rooms, my own correspondents and my own opinions, and I shall give you all three at breakfast. And you never again dismiss me in front of a council. You may dismiss me in private. I shall enjoy watching you try."''',
      c('[Take her hand] "Then name the next evening."', "threshold", flags=("konomi.committed",)),
      c('[Ask what she wants] "What do you want, Konomi? Not the capital. You."', "no")),
    k("envoy", '''"Envoy. A chair at your table, with my name on it and Nerosyan's seal under it."
{n}She considers the offer the way she considers a treaty: from the end backwards.{/n}
"That, Commander, I will take. And I will make you regret offering it every single week, in writing, in triplicate, with the capital copied in."''',
      c('[Accept the chair\'s terms] "Envoy, then. My door stays open."', flags=(ENVOY,))),
    k("no", '''{n}The question lands somewhere she has not armoured. For a moment she looks tired, and much younger than her office.{/n}
"What I want is not to be recalled by anyone. Not by Nerosyan. Not by you, from a wall, with a joke that turns roads round." {n}She picks up the fan again. It steadies her hand.{/n} "Give me a season, Commander. Then ask me again, and do not ask as a Trickster. Ask as someone who could be told no."''',
      c('[Let her decide] "Your call."', flags=(DECLINED,))),
    nar("threshold", '''{n}She looks at your hand in hers as if it were a clause she had drafted herself and was only now reading in fair copy.{/n}
"The next evening," she says, "is this one."
{n}The fan closes with a snap. She rises, and for the first time since the day she walked into your council with a scroll under the Queen's seal she lets go of her manners all at once: the ears she keeps so correctly upright at the table tip back, pleased, and the tail she holds in a careful curl through every audience comes loose and sweeps out behind her in the lamplight, slow, russet and pale-tipped, like a banner let down from a wall.{/n}
"Agreed. Now take this robe off me, Commander. Slowly. I bill by the minute, and tonight I intend to be very expensive."
{n}You do it slowly. She lets the outer robe slide from one shoulder, then the other, and stands in the lamplight with nothing on but her rings and her smile, and lets you look for exactly as long as she has decided you may. Then she kisses you, with a politician's patience and none of a politician's restraint, her nails light at the back of your neck, her tail curling round the backs of your knees as if it had its own opinion about where you should stand.{/n}
{n}She walks you backwards to the desk. A week of Nerosyan's dispatches goes to the floor in a slither of wax and ribbon. She pushes you down across the place where they lay, climbs over you with her knees either side of your hips, catches both your wrists in one hand and pins them above your head, and settles astride your hips, and reaches down between you with her free hand, watching your face the whole time to see what it costs you.{/n}''',
      c("Continue", "morning")),
    nar("morning", '''{n}Morning. She is at your desk in your shirt, composing a dispatch, tail curled round the leg of the chair. The dispatches are stacked again, in order. One of them has a heel print on it.{/n}
"Nerosyan will hear that I was detained by the Commander on urgent business." {n}She blots the line.{/n} "Entirely accurate."
{n}She does not look up when you come to stand behind her. She does lean back, just enough.{/n}''',
      c('"Leave the one with the heel print. I\'ll answer it myself."')),
], requires=("trickster.ever", SETTLED), forbids=("konomi.committed", DECLINED, ENVOY), delay=72)


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
        mythic="Trickster"),
      c('[Let the clerk finish after all.]', abort=True)),
    nar("refusal", '''{n}The hand on the fan does not move. The candles gutter all at once, as if a door has opened somewhere that is not in this room. Somewhere close, faint and very dry, a voice you know says:{/n}
"Recalled? Only Nerosyan recalls me, Commander. And you killed me. I see no reason whatever to consult."''',
      c('[Name the terms] "Consultations at your rate, then. Name it."', "fee", flags=(FEE,)),
      c('[Let her go] "...Then rest, Lady Konomi."', abort=True)),
    nar("fee", '''{n}A silence long enough to be a negotiating position.{/n}
"...Triple the standard rate for consultations. In advance. And the recall is entered as my decision. Not yours. Mine. I will not be the woman who came back because a Commander with a joke told her to."
{n}The clerk has not breathed for some time.{/n}''',
      c('[Agree to her fee] "Triple. In advance. Your decision, on the record."', "record", alignment=("Chaotic", 1))),
    nar("record", '''{n}A dead woman's hand turns on the folded fan, very slightly, palm-up, the way an attaché receives a sealed dispatch.{/n}
{n}The clerk crosses out DECEASED. Above it, in a neater hand that is not his, someone has added: FOR CONSULTATIONS, AT HER OWN REQUEST.{/n}''',
      c('[Let her come back.]', revive="konomi", flags=(CONFIRMED,))),
], requires=("trickster", DEAD), forbids=(CONFIRMED, "konomi.return_path_prepared"), delay=0,
   chapters=(3, 5), Recovery="konomi", TricksterDevice=True, TricksterState=DEAD)

physical("konomi.trickster.dead.consultation", "Triple, in advance", '"You asked for consultations."', [
    k("start", '''{n}She is at her desk, alive and very displeased about the manner of it. There is colour in her face and ink on her fingers. The dispatch with the crossed-out word is pinned to the wall behind her, where she can see it and so can everyone who comes in.{/n}
"'Recalled for consultations.' You have committed a diplomatic impertinence on my corpse, Commander, and I accepted it on terms, which I shall now enforce."
{n}She opens the fan. Her hand is not quite steady; she lets you see that, and dares you to mention it.{/n}
"The fee is triple. In advance. Then we consult. I have a great many questions about the afterlife and very few of them are theological."''',
      c('[Consult] "You asked for consultations. I\'m here to consult."', "unpaid"),
      c('[Pay the fee first] "The fee, as agreed. In advance."', "paid", crusade=("Finances", -300))),
    k("unpaid", '''"Without paying first. Naturally."
{n}She writes a figure in the margin of the dispatch and underlines it twice.{/n}
"It will accrue. Sit down, Commander. We shall begin with why you killed me, and we shall end, if you are fortunate, with whether I intend to hold it against you. I have not decided. I am enjoying not having decided."''',
      c('"Then let\'s begin."', flags=(RETURNED,))),
    k("paid", '''{n}She counts it. All of it, twice, while you watch.{/n}
"...Paid. How unexpectedly honest of you. I shall have to recalculate you."
{n}She sweeps the coin into a drawer and locks it.{/n}
"Sit down. We shall begin with why you killed me. You may take as long as you like; I am billing by the hour."''',
      c('"Then let\'s begin."', flags=(RETURNED, FEE_PAID))),
], requires=("trickster.ever", PRIMED, CONFIRMED, RECALLED),
   forbids=(DEAD, RETURNED, "konomi.return_first_words", "konomi.missed_letter_sent"), delay=12, chapters=(3, 5))


# --- State never_arrived: credentials deemed presented (F03, the secretary's register) -----------------------------

letter("konomi.trickster.never_arrived.accredited", "Deemed presented", [
    nar("start", '''{n}The war council sits. At the foot of the table there is a chair for Nerosyan's attaché, because the Crown's protocol says a crusade's council has one, and the steward keeps protocol the way other men keep saints' days. Nobody has ever come to sit in it. Somebody has put a jug on it.{/n}''',
      c('[Bow to the empty chair] "Lady Konomi\'s credentials are hereby deemed presented. Someone tell her she\'s late for her own audience."',
        "nerosyan", mythic="Trickster", alignment=("Chaotic", 1)),
      c('[Move the jug and carry on.] "..."', abort=True)),
    nar("nerosyan", '''{n}The council laughs politely. You bow to the jug anyway, properly, from the waist.{/n}
{n}The same hour, in Nerosyan. A junior secretary of the Royal Council is copying the day's dispatches by a bad lamp. He writes 'Drezen: credentials presented' in the column for the attaché's journey, where 'Drezen: pending' should go. He blots it, frowns at it, and decides it was always like that.{/n}
{n}Across the room, at a reception, a kitsune in grey silk is being very charming to a margrave she despises. She has never been to Drezen. She has no idea.{/n}
{n}In Drezen, when the steward lifts the jug, the seat beneath it is warm.{/n}''',
      c("Continue", flags=(PRIMED, ACCREDITED, "konomi.missed_letter_sent", "konomi.started"))),
], requires=("trickster", "konomi.missed_contact_available"),
   forbids=("konomi.present", "konomi.dismissed", "konomi.missed_contact_invalidated", RETURNED, ACCREDITED), delay=0,
   chapters=(3, 5), TricksterDevice=True, TricksterState="konomi.missed_contact_available")

physical("konomi.trickster.never_arrived.audience", "Late for her own audience", '[Greet the woman in the attaché\'s office.]', [
    k("start", '''{n}A kitsune in travelling silks is standing in the attaché's office, empty since Drezen fell, with a ledger under her arm, as if she had been there for an hour. She has.{/n}
"Lady Konomi, official attaché of Nerosyan. Here are my credentials." {n}She holds out her credentials. The ink on the date is two days old.{/n} "Though I understand they have already been presented. By you. To a jug."
"I was halfway through a reception in Nerosyan when a secretary showed me his register. Column four, in his hand: 'credentials presented, Drezen'. He could not say how. Nobody could. I have come to see what I said."
{n}Her smile is small, sharp and entirely pleased with itself.{/n}
"The journey is on your account, Commander. So is the reception I left. It was a very good reception."''',
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
], requires=("trickster.ever", PRIMED, ACCREDITED, "konomi.missed_letter_sent"),
   forbids=("konomi.present", RETURNED, "konomi.missed_contact_invalidated", CONFIRMED), delay=48, chapters=(3, 5))


# --- Epilogue: paragraphs on her registered endings, and her own pages (R2-6) ---------------------------------------

TRICKSTER_PARAGRAPHS = (
    p("Lady Konomi reached Nerosyan eventually. She never explained the delay, and she billed the crown for three days of "
      "travel that had taken her nowhere.", requires=(RECESSED,), forbids=(OUTFOXED,)),
    p("In Nerosyan they said the new envoy to Drezen had been appointed by the Commander, at her own suggestion, on terms "
      "nobody else was shown.", requires=(RECESSED, OUTFOXED)),
    p("She kept the unnamed favour for years, and mentioned it only when the Commander seemed in danger of forgetting it.",
      requires=(FAVOUR,)),
    p("Nerosyan's archive holds one dispatch with a word crossed out and six words added in a neater hand. Lady Konomi had "
      "it framed, and billed the crown for the frame.", requires=(RETURNED, RECALLED)),
    p("In the Royal Council's register for that year, column four still reads 'credentials presented, Drezen', in a junior "
      "secretary's hand, two days before anyone left the capital. Auditors query it every spring. Lady Konomi signs the "
      "query every spring, and sends it back.", requires=(RETURNED, ACCREDITED)),
)

SCENES.append(scene("konomi.trickster.epilogue.commit", "Accepted in advance", "Epilogue", 5, "", [
    nar("offer", '''{n}Lady Konomi came back to Drezen after the war as envoy of a Nerosyan that had learned to read the Commander's letters very carefully.{/n}
{n}She asked the question herself, in a sealed dispatch addressed to the Commander in person, not to the Commander's office. It was two lines long. She did not wait for the courier to leave before adding a postscript: 'Accepted in advance.'{/n}''',
      c('[Write "Countersigned" under the postscript.]', "signed"),
      c('[Send it back with terms of your own.]', "terms")),
    nar("signed", '''{n}She read the countersignature in the doorway of the Commander's rooms, with the courier still standing behind her, and laughed out loud, which nobody in Nerosyan had ever heard her do.{/n}
{n}She kept her rooms, her correspondents and her opinions, and delivered all three at breakfast. The dispatch hung framed above the desk they shared. Visitors assumed it was a treaty. In a sense it was.{/n}''',
      c(), paragraphs=TRICKSTER_PARAGRAPHS),
    nar("terms", '''{n}The Commander sent it back with a single clause added: 'Not to be recalled by anyone. Including me.'{/n}
{n}She arrived the next morning with the dispatch in one hand and her travelling case in the other, and read the clause aloud in the doorway, twice, the way she read treaties. Then she set the case down.{/n}
"That," she said, "is the first sensible thing you have ever written me."
{n}She stayed. She was never recalled by anyone again.{/n}''',
      c(), paragraphs=TRICKSTER_PARAGRAPHS)],
    requires=("trickster.ever", LATE_COMMITTED), forbids=("konomi.committed", "konomi.closed", DECLINED), last=99,
    Relationship="konomi"))

SCENES.append(scene("konomi.trickster.epilogue.refused", "Still negotiating", "Epilogue", 5, "", [
    nar("start", '''{n}Lady Konomi was never recalled by anyone again. She saw to that. Every spring the Commander received one dispatch from Nerosyan, correct in every particular and signed in her own hand, and every spring it ended the same way: 'Still negotiating.'{/n}''',
      c(), paragraphs=TRICKSTER_PARAGRAPHS)],
    requires=("trickster.ever", DECLINED), forbids=("konomi.committed",), last=99, Relationship="konomi"))


# --- Reactions (05 section 3.1: exactly Regill and Kyado) ---------------------------------------------------------

REACTIONS = [
    reaction("Regill", "konomi.trickster.dismissed.react_regill", (RECESSED, "konomi.dismissed"),
             '''{n}Regill's pale yellow eyes settle on you with an expression of polite attention that is not polite at all.{/n}
"You dismissed the attaché of Nerosyan before your own council, and then retained her on a technicality of the road. Either decision alone I could respect. Together they are contempt of your own order."
"I have no statute for a road that disobeys its surveyors. I shall have to write one. It will be long."''',
             answer_list=REGILL_HUB, forbids=REGILL_GONE, chapter=5, last=5, entry='"About Lady Konomi..."'),
    reaction("Kyado", "konomi.trickster.dismissed.react_kyado", (RECESSED, "kyado.in_drezen", KYADO_SAID_IT),
             '''{n}Kyado has heard. Everyone in the lower town has heard. He does not laugh; he looks at you the way he looked at you once in the temple, as if you were weather.{/n}
"I told you, Commander. Back at the temple. You play tricks, and your tricks become the truth. I didn't think it would be roads."
"The fox lady's driver came to me for a blessing. I gave him one. Erastil keeps the roads for honest travellers, I told him, and you were honest; it was the road that wasn't." {n}He hesitates.{/n} "I hope she made you pay for it."''',
             answer_list=KYADO_HUB, forbids=("kyado.dead",), chapter=5, last=5, entry='"About Lady Konomi..."'),
    reaction("Regill", "konomi.trickster.dead_retained.react_regill", (CONFIRMED, RECALLED),
             '''{n}Regill does not look up from his report.{/n}
"A death is a record, Commander. You amended it, and the deceased countersigned. I have no statute for that."
{n}He turns a page.{/n}
"I shall write one. I shall also note, for your file, that she charged you triple, and that you paid. It is the first sign of discipline I have seen in you."''',
             answer_list=REGILL_HUB, forbids=REGILL_GONE, chapter=3, last=5, entry='"About Lady Konomi..."'),
    reaction("Kyado", "konomi.trickster.dead_retained.react_kyado", (CONFIRMED, RECALLED, "kyado.in_drezen"),
             '''{n}Kyado sets down the ledger he was reading and folds his hands on it, the way a prior folds his hands, though he gave that office up.{/n}
"They say she was dead, and then she was expensive."
"Erastil says the dead should be let rest. He also says a debt is a debt." {n}He frowns at his hands.{/n} "I don't know which of those you kept, Commander. I think she does. Ask her before you ask me."''',
             answer_list=KYADO_HUB, forbids=("kyado.dead",), chapter=3, last=5, entry='"About Lady Konomi..."'),
    reaction("Regill", "konomi.trickster.never_arrived.react_regill", (RETURNED, ACCREDITED),
             '''"Credentials are presented, or they are not, Commander. 'Deemed' is a word for people who have lost the argument."
{n}Regill's mouth tightens a fraction.{/n}
"And yet here she is, with Nerosyan's register to prove it, in a secretary's hand that no court could fault. I dislike being out-argued by furniture."''',
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
# keeps its own continuation: fate_reply, retained_attempt and the_answer_she_addressed are not gated.
RETIRED = ("konomi.fate_post", "konomi.retained_inquiry", "konomi.the_unintroduced_letter")
ENDINGS = ("konomi.ending_public", "konomi.ending_private", "konomi.ending_changed", "konomi.ending_ascended",
           "konomi.ending_distance", "konomi.ending_distance_open", "konomi.ending_distance_lived",
           "konomi.ending_distance_open_lived")
AUDIENCE_ANSWER = '"You chose a better room than the attaché\'s office."'
COURTYARD_NODES = [
    k("again_audience", '''"I did. The office has a jug in it now, on a shelf, with a label. The steward will not let anyone move it."
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
                        "expected; a Konomi killed at her post may be recalled on her own terms; and one who never came "
                        "may find her credentials already presented.")
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

    # R2-6: the late commit is her own page; the registered unfinished ending does not also play.
    _scene(by_id, "konomi.ending_unfinished")["Forbids"].append(LATE_COMMITTED)
    for id in ENDINGS:
        for node in _scene(by_id, id)["Nodes"]:
            if all(ch.get("Next") is None for ch in node["Choices"]):
                node.setdefault("Paragraphs", []).extend(dict(x) for x in TRICKSTER_PARAGRAPHS)

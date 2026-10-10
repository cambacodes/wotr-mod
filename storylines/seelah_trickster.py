"""Seelah on the Trickster path: rob the thief (Writer/handoffs/trickster/seelah.md, family F07).

Canon: Seelah became a paladin because she was a thief. As a girl she stole a mithral helm from a knights' camp, and its
owner, Acemi, died of a gnoll's blow to her unprotected head (string 2a34986a: "who was really to blame for her death -
the gnoll attacker or the young thief named Seelah?"). Penta's rule is canon too: "After standing trial before [the
Lady of Graves], a soul can no longer be resurrected" (DLC6 Tavern_Night_Debate/Cue_0001 9e410aac). The Trickster robs
a richer thief (polish b9c: no mythic power does the work). At her bier the chaplain's bowl is short, and nobody knows
how long her soul waits before it is tried (Penta's rule; no deadline is invented). In her purse the Commander finds her list of old thefts (authored), whose last
line names a Drezen relic-seller selling diamonds prised from the Kenabres reliquaries. The Commander lifts his pouch
with the lift she taught (Thievery DC 15 with the lesson, 25 without; caught, the Commander faces him down, and he
knows the face), and the stolen stones fill the bowl before her trial. The cost stays: she wakes to a life bought
with a theft from her own city's dead (the Acemi mirror), a line on her list she cannot cross out. If she was
dismissed instead, the
Commander lifts her transfer papers while taking her hand (CompanionDialogues/Seelah/Cue_0043 -> Cue_0050 "Then good
luck to you on your journey."), so no company can sign her on and she comes back, furious, for them.
"""
import copy

from story_format import c, n, p, reaction, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
HUB = "417fa384f3250634bb71859fbc913453"            # CompanionDialogues/Seelah/AnswersList_0003
DISMISSAL = "64cfedbb85f36a44cb45f568f18152f7"      # CompanionDialogues/Seelah/AnswersList_0046 (after Cue_0043)
FINAL_DECISION = "3a2c9f56a58b5c1478746c3ebc456986"  # Cue_0043 "Is that your final decision?"
GOOD_LUCK = "6b81c330ca8b1324186cb02bdc8d9c54"      # Cue_0050 "Then good luck to you on your journey." (OnStop: Unrecruit)
NPC = "90481a29cc75f424b9891a55c6dcbb53"            # Seelah_NPC_Level1 (non-companion; the presence copy)
FYE = "0f12118177d102f428a3b30b15b132eb"            # Fye_Bartender, the presence anchor
DIAMOND = "6a7cdeb14fc6ef44580cf639c5cdc113"        # Items/Jewelry/Diamond
IRABETH_HUB = "871af36f2ab2b1f40b5de77976c54276"    # NPC_Common/Irabeth/AnswersList_0009
SOSIEL_HUB = "129b55b8b5d50974f84f7c607d894fd0"     # CompanionDialogues/Sosiel/AnswersList_0002

PRIMED = "seelah.trickster.primed"
POCKETS = "seelah.trickster.pockets_picked"         # the spec's alias flag of PRIMED, set with it
RETURNED = "seelah.trickster.returned"
REJOINED = "seelah.trickster.rejoined"              # Derived: returned in the retained-death world (back in the party)
DECLINED = "seelah.trickster.declined"
REVIVED = "seelah.revived"
FINALLY_DEAD = "seelah.finally_dead"                # Derived: her retained unit lies dead (revive.seelah.available)
ROMANCE = "seelah.romance"                          # Derived: the registered route's romance (kissed / lovers)
LESSON = "seelah.trickster.lift_lesson"
HOLDS = "seelah.trickster.cost.holds_her_death"         # (b9c) the Commander holds her list; the flag id is a save ref
BROKER = "seelah.trickster.cost.broker_knows"          # the lift was caught: the relic-seller knows the Commander's face
CHAPLAIN = "seelah.trickster.cost.chaplains_word"
KEEPS = "seelah.trickster.cost.keeps_it"
GIVEN_BACK = "seelah.trickster.death_returned"
WOKE = "seelah.trickster.woke"
CORRESPONDENT = "seelah.trickster.correspondent"
HERDED = "seelah.trickster.cost.herded"
DARED = "seelah.trickster.dared"
LATE = "seelah.trickster.cost.late"
CAUGHT = "seelah.trickster.cost.caught"
STAY = "seelah.trickster.stay_decided"
NEAR = "seelah.trickster.stays_near"
FAR = "seelah.trickster.goes_far"
FRIENDS = "seelah.trickster.friends"
ROBBED = "seelah.trickster.cost.robbed_back"
LATE_COMMITTED = "seelah.trickster.late_committed"  # Derived (trickster_world): trickster.ever + stay_decided
DIAMOND_HELD = "seelah.diamond_held"
COURTED = "seelah.trickster.courted"                # Q10: the market game played on the presence (either answer)
TAVERN_KISSED = "seelah.trickster.tavern_kissed"    # Q10: the alley kiss, a romance earned outside the party
DISPATCHED = "seelah.trickster.stones_sent"          # Q10 r2: the rider rite sent; she is not back yet
REPLIED = "seelah.trickster.cost.rider_days"         # Q10 r2: the field chaplain's note (>= 96 h after the rider)
TAKEN = "seelah.trickster.cost.seller_taken"          # Q10 r2: caught lift, the seller arrested, stones kept by order
PAID = "seelah.trickster.cost.seller_paid"            # Q10 r2: caught lift, the seller paid off from the crusade chest
RECONCILED = "seelah.trickster.reconciled"            # Q10 r2: her no answered by the second ask (declined stays as history)
SELLER_HEARD = "seelah.trickster.seller_heard"         # Q10 r3: her word on the seller heard (tavern or visit twin)
LATE_CODA = "seelah.trickster.late_coda"               # Q10 r3: Derived late commit qualified by romance (Last Call coda)
FAILED = "seelah.presence.failed"                   # runtime: Fye's anchor failed; the visit twins take over
OWN = ("seelah.closed", "inhuman")

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={"seelah_dead": RETURNED, "seelah_gone": RETURNED},
    # ER-2: each device also ignores the other unavailable flag. SeelahNotInParty_Dead needs her in the party, so she
    # cannot also be KickedOut in play; a world that forces both at once (the coexistence model) still reaches a device.
    TricksterAccess={
        "dead": dict(detect=["seelah_dead", FINALLY_DEAD, "seelah_gone"], device="seelah.trickster.dead.pickpocket",
                     returned=RETURNED),
        "dead_no_unit": dict(detect=["seelah_dead", "!" + FINALLY_DEAD, "seelah_gone"],
                             device="seelah.trickster.dead.pickpocket_effects", returned=RETURNED),
        "dismissed": dict(detect=["seelah_gone", "seelah_dead"], device="seelah.trickster.dismissed.setup", returned=RETURNED),
    })
DERIVED = {
    FINALLY_DEAD: [["revive.seelah.available"]],
    ROMANCE: [["seelah.kissed"], ["seelah.roof_kissed"], ["seelah.lovers"], [TAVERN_KISSED]],
    REJOINED: [[RETURNED, REVIVED]],
    LATE_CODA: [[LATE_COMMITTED, ROMANCE]],
}
PRESENCES = {
    # A copy of her non-companion NPC blueprint at Fye's bar (the companion unit would offer recruitment). One presence
    # for both outside-the-party worlds; if Fye has left the capital the anchor fails and the papers letter opens.
    "seelah.presence": dict(Unit=NPC, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=FYE, Side="left", Distance=2.0),
                            Requires=["trickster.ever", "seelah.trickster.in_drezen"], Forbids=["seelah.closed", "seelah.committed"],
                            MinChapter=3, MaxChapter=5, AnswerLists=[], Dialog="hub",
                            Greeting="{n}Seelah has the table nearest the door, her back to the wall like a thief and her "
                                     "boots polished like a paladin. She watches you cross the room without blinking.{/n}"),
}


def s_(id, text, *choices):
    return n(id, "Seelah", text, *choices, portrait="Seelah")


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Seelah", **kw)


def hub(id, title, entry, nodes, requires, forbids, delay, **extra):
    """Physical, on her own companion hub (she is in the party)."""
    SCENES.append(scene(id, title, "Seelah", 3, entry, nodes, requires=requires, forbids=(*OWN, *forbids), delay=delay,
                        last=5, optional=True, Relationship="seelah", AnswerLists=[HUB], **extra))


def tavern(id, title, entry, nodes, requires, forbids, delay, **extra):
    """Physical, on the presence at Fye's bar (she lives outside the party)."""
    SCENES.append(scene(id, title, "Seelah", 3, entry, nodes, requires=requires, forbids=(*OWN, *forbids), delay=delay,
                        last=5, optional=True, Relationship="seelah", Areas=[DREZEN], Chapters=[3, 5], ContactUnit=NPC,
                        InteractionHub="seelah.presence", **extra))


def letter(id, title, nodes, requires, forbids, delay, **extra):
    SCENES.append(scene(id, title, "Seelah", 3, "", nodes, requires=requires, forbids=(*OWN, *forbids), delay=delay,
                        last=5, optional=True, Relationship="seelah", Chapters=[3, 5], Remote=True, **extra))


# --- In the party: the lift she teaches ----------------------------------------------------------------------------

hub("seelah.trickster.in_party.lift_lesson", "One lift, never on anyone who needs it",
    '"You told me you were a thief once. Prove it. Teach me something."', [
    s_("start", '''{n}Seelah looks you up and down, the way she looks at a stranger's hands in a crowded market.{/n}
"A paladin of Iomedae, teaching the Commander to pick pockets. The Inheritor is going to have words with me."
{n}She grins anyway, the same grin she wears on a battlefield.{/n}
"Fine. One lift. And you swear it now, on whatever you swear on: never on anyone who needs what's in the purse. I learned that one too late."''',
      c('[Let her show you] "Show me. Slowly. I want to see where the hand goes."', "lesson")),
    nar("lesson", '''{n}She walks past you, stumbles, catches your arm to steady herself and says she is so sorry, what a clumsy fool, is your shoulder all right? Then she holds up your purse between two fingers.{/n}
{n}You never felt it go.{/n}
"The trick's not the hand," {n}she says, and gives it back.{/n} "It's the apology. Everybody watches your face while you're saying sorry. Nobody watches your fingers."''',
      c('[Practise on her] "Again. On you, this time."',
        check=dict(Skill="SkillThievery", DC=15, Success="caught_it", Failure="caught_you", CommanderOnly=True))),
    nar("caught_it", '''{n}You bump her shoulder and apologise. You mean the apology, a little, which may be the point. You come away with one of her coppers.{/n}
{n}Seelah turns out the purse, counts, and stares at you.{/n}
"...Huh. You're a natural. That isn't a compliment, Commander. Keep it where I can see it."''',
      c('[Keep the coin] "Finders keepers."', flags=(LESSON, "seelah.started"))),
    nar("caught_you", '''{n}She catches your wrist before your fingers are halfway to the strings, and holds it there, not hard.{/n}
"Too slow. And you looked at the purse. Never look at the purse." {n}Her thumb taps your knuckle once.{/n} "Do it like you're sorry. You'll get it. Some other day."''',
      c('[Offer her one of your coppers] "For the lesson. Keep it where I can see it."', flags=(LESSON, "seelah.started"))),
], requires=("trickster",), forbids=("seelah_dead", "seelah_gone", LESSON), delay=0, Chapters=[3, 4, 5])


# --- The richer thief: her list's last line, and the lift she taught -------------------------------------------------
# Shared by the bier and the effects: the relic-seller under the chapel steps, the lift (the lesson lowers the DC), and
# on a failed check the Commander's nerve instead of a clean hand. Both roads fill the bowl; only the cost differs.

LIST_LAST = '''{n}The last line is in fresher ink: "The relic-seller under the chapel steps. Sells 'saints' tears' to pilgrims. I bought one off him for two silver and took it to old Brother Haldis at the chapel, who carried the Kenabres reliquary book out of the ruins. The setting marks match his book, stone for stone. They are off the Kenabres altars. Not mine to take back. I am a paladin now. Tell Irabeth."{/n}'''

STALL = '''{n}The relic-seller's stall is a plank on two barrels under the chapel steps, shuttered for the night. He is still behind it, counting by a shielded lamp: a soft, careful man in pilgrim's grey, with a fat pouch at his belt that he touches every little while, the way a man touches a thing he loves.{/n}'''

LIFTED = '''{n}You stumble into his lamp and catch it before it falls, and you are so sorry, what a clumsy fool, did it burn him? He watches your face the whole time you are apologising. Nobody watches your fingers.{/n}
{n}Round the corner you open the pouch in your palm. Small, cloudy stones, a good many of them, some still with a crumb of gilt where somebody's knife prised them out of a setting.{/n}'''

GRABBED = '''{n}He feels it go. His hand closes on your wrist with the strings still in your fingers, and he draws breath to shout for the watch, and then he sees whose wrist it is.{/n}
"Commander." {n}He does not let go.{/n} "Those are consecrated stones. Bought honestly."
{n}You tell him, quietly, what a Kenabres reliquary looks like with its settings emptied, and whose altars they stood on. He does not let go. He is a careful man, and he has done his sums.{/n}
"Then call the watch, Commander. I'll go quietly. And these go to the Inheritor's court as evidence, under seal, until my trial." {n}His eyes go to your coat, where the paper is.{/n} "How long has your dead paladin got? Longer than a court? Or we part friends: you take the stones, and the Inheritor never hears my name. Not from you, and not from her little list. Your word, in front of the saints."'''

CONCEALED = '''{n}You give it. His hand opens. It is the only thing you have bought tonight that you will have to keep, and it is the one line on her list she asked someone to finish: Tell Irabeth. He knows your face now, and he will tell the story to anyone who buys him a drink, everywhere but the Inheritor's door.{/n}'''

SELLER_TAKEN = '''{n}You shout for the watch yourself. When the sergeant comes running you put the man in his hands and the pouch in your coat, and write the order on the sergeant's own slate: the stones are the crusade's business tonight, by the Commander's word, and the court may have them back as dust. The seller shouts about seals and sacrilege all the way to the cells.{/n}
{n}By morning every clerk of the Inheritor's court knows the Commander broke a sacred-property seizure on a word, and they will remember it the next time the Commander wants a favour. But the man is in a cell.{/n}'''

# r5-S2 (seelah:D01/D02/D05/D06): who hears the report. Her list says "Tell Irabeth"; the choices stay independent of
# Irabeth, and only these read-only paragraphs follow whether she is alive and in Drezen to be told.
IRABETH_DEAD, IRABETH_LEFT, IRABETH_RETURNED = "irabeth_dead", "irabeth_gone", "irabeth.trickster.returned"


def irabeth_told(here, dead, left):
    return (p(here, forbids=(IRABETH_DEAD, IRABETH_LEFT)),
            p(here, requires=(IRABETH_RETURNED,), any_groups=[[IRABETH_DEAD, IRABETH_LEFT]]),
            p(dead, requires=(IRABETH_DEAD,), forbids=(IRABETH_RETURNED,)),
            p(left, requires=(IRABETH_LEFT,), forbids=(IRABETH_RETURNED, IRABETH_DEAD)))


TAKEN_REPORT = irabeth_told(
    '''{n}The sergeant's slate and the seller's name are on Irabeth's desk before breakfast. The last line on her list, Tell Irabeth, is done.{/n}''',
    '''{n}Irabeth is dead, and cannot be told. The sergeant's slate and the seller's name go to the Inheritor's court instead, to be read by clerks who never knew Seelah. Her last line asked for Irabeth. The court is what is left.{/n}''',
    '''{n}Irabeth has left Drezen, and a letter would take weeks to find her. The sergeant's slate and the seller's name go to the Inheritor's court instead. Her last line asked for Irabeth. Tonight the court is who you can tell.{/n}''')

SELLER_PAID = '''{n}"Name it," you say. He does, and it is a jeweller's price for every stone, and a second one for forgetting your face. You pay it out of the crusade's chest with a note the quartermaster will read aloud at the next council.{/n}
{n}He lets go and counts it twice. The stones are yours, honestly bought from a man who stole them from the Kenabres dead, and he walks off whistling. The last line on her list, Tell Irabeth, stays undone, and now you have paid him to keep it that way.{/n}'''


def caught_choices(*conceal):
    """The caught lift: the existing answers (now the concealment, his word) keep their positions; arrest and buy-off are
    appended (Q10 r2), each to its own page."""
    return [*conceal,
            c('[Have him taken, and keep the stones] "Watch! This man robs the Kenabres dead. The stones stay with me, by my order."',
              "taken", flags=(TAKEN,), crusade=("Favors", -50)),
            c('[Buy the stones and his silence] "How much for the lot, and for forgetting my face?"', "paid", flags=(PAID,),
              crusade=("Finances", -500))]


def lift_choices():
    return (c('[Lift his pouch the way she taught you] "Excuse me. So sorry."', requires=(LESSON,),
              check=dict(Skill="SkillThievery", DC=15, Success="lifted", Failure="grabbed", CommanderOnly=True)),
            c('[Lift his pouch off his belt] "Excuse me."', forbids=(LESSON,),
              check=dict(Skill="SkillThievery", DC=25, Success="lifted", Failure="grabbed", CommanderOnly=True)))


# --- State dead_not_raised: the dead thief's list, and a richer thief ------------------------------------------------

letter("seelah.trickster.dead.pickpocket", "The dead thief's purse", [
    nar("bier", '''{n}The chaplain of the Drezen chapel stands over the bier with a bowl of diamond dust that is not full, and a rite he cannot finish with it.{/n}
"Before she stands trial, Commander. A soul that has stood its trial cannot be raised, and nobody on this side of the Boneyard can tell you how long a soul waits before the Lady tries it. An hour. A week. I have never dared find out, and I would not make her wait to learn it."
{n}Seelah's purse lies beside her, its strings tied neatly by somebody who did not know her. She always tied them badly, so she could get them open fast.{/n}''',
      c("Continue", "strings", requires=(LESSON,)), c("Continue", "fumble", forbids=(LESSON,))),
    nar("strings", '''{n}You untie them the way she taught you: while apologising to her. The chaplain watches your face. Nobody watches your fingers.{/n}''',
      c("Continue", "coin")),
    nar("fumble", '''{n}You fumble the strings. They were never meant to be opened by anyone else. The chaplain pretends not to see.{/n}''',
      c("Continue", "coin")),
    nar("coin", '''{n}Her savings go into the chaplain's bowl coin by coin: coppers, a few silver, one gold piece she must have been keeping for something. It is not enough. It was never going to be enough.{/n}
"I will not try the lesser rite on her," {n}the chaplain says.{/n} "It brings the dead back weak, and I have seen it fail twice this month on the crusade's dead. She has a war to go back to. The greater rite gives her back whole, and it wants two stones' worth of diamond dust. The chapel's own stone is promised to the next knight who falls."
{n}At the bottom of the purse is a square of paper folded very small. It is a list, in her hand, of every theft she can remember. Most lines are crossed out, each with a sum beside it and the word "paid". The first line is not: "A mithral helm. Acemi." There is no sum beside it.{/n}
''' + LIST_LAST,
      c('[Pick the dead thief\'s pocket] "Old habits, Seelah. Whatever\'s in the purse is mine. Including that."', "stall",
        mythic="Trickster", alignment=("Chaotic", 1)),
      c('[Leave the purse tied] "Not like this."', abort=True)),
    nar("stall", '''{n}You fold the list into your coat and tell the chaplain to keep his candles lit.{/n}
''' + STALL, *lift_choices()),
    nar("lifted", LIFTED, c("Continue", "pocketed")),
    nar("grabbed", GRABBED, *caught_choices(
        c('[Give him your word] "Your name stays off every report. Let go."', "concealed", flags=(BROKER,)))),
    nar("concealed", CONCEALED, c("Continue", "pocketed")),
    nar("taken", SELLER_TAKEN, c("Continue", "pocketed"), paragraphs=TAKEN_REPORT),
    nar("paid", SELLER_PAID, c("Continue", "pocketed")),
    nar("pocketed", '''{n}The chaplain is still at the bier when you come back. You tip the pouch into his bowl, and the stones rattle down on top of her coppers.{/n}
{n}He picks one out and turns it to the candle. There is gilt on it.{/n}
"These came off the Kenabres altars." {n}He does not ask how you came by them. He looks at the paper in your hand, and at her, and weighs the pouch in his palm.{/n} "They were given to the dead of Kenabres, Commander. One stone's worth, near enough. Half the rite."''',
      c('[Put a diamond from your own coat in with them] "They were taken off the Kenabres dead. Let them buy one back. That\'s both stones. Begin."',
        requires=(DIAMOND_HELD,), revive="seelah", remove_item=DIAMOND, flags=(RETURNED, REVIVED, HOLDS, "seelah.started")),
      c('[Give him your word for the other stone] "They were taken off the Kenabres dead. Let them buy one back. Spend the chapel\'s stone; the crusade will make it good. Begin."',
        forbids=(DIAMOND_HELD,), revive="seelah", crusade=("Favors", -100), flags=(RETURNED, REVIVED, HOLDS, CHAPLAIN, "seelah.started"))),
], requires=("trickster", "trickster.ever", "seelah_dead", "seelah.dead.latched", FINALLY_DEAD), forbids=(RETURNED, "seelah_gone"),
   delay=24, TricksterDevice=True, TricksterState="dead", Recovery="seelah", Areas=[DREZEN])

hub("seelah.trickster.dead.wakes", "Whatever you took", '"Seelah."', [
    s_("start", '''"You robbed my corpse."
{n}She is sitting on the edge of the chapel cot in her shirt, turning her empty purse inside out. She laughs once, badly.{/n}
"The worst part is I'd have done the same. Every copper I had, Commander. Even the gold piece, and I've carried that one since Solku without ever spending it. Did She let me go, or did you buy me?"''',
      c('"The chaplain did the work. The seller\'s stones paid for half the rite, and my diamond for the rest."', "coin", forbids=(CHAPLAIN, PAID)),
      c('"The chaplain did the work. The seller\'s stones paid for half the rite, and his chapel supplied the rest on my word."', "coin_word", requires=(CHAPLAIN,), forbids=(PAID,)),
      c('"The chaplain did the work. Crusade gold bought the seller\'s stones. My diamond paid for the rest."', "coin", requires=(PAID,), forbids=(CHAPLAIN,)),
      c('"The chaplain did the work. Crusade gold bought the seller\'s stones. The chapel supplied the rest on my word."', "coin_word_paid", requires=(PAID, CHAPLAIN,))),
    s_("coin_word", '''"On your word." {n}She closes her eyes.{/n} "You emptied a dead paladin's purse, brought the priests stones off the Kenabres altars, and asked them for credit. Wonderful. I'm going to hear about that at every mass until the Wound shuts."''',
      c("Continue", "coin")),
    s_("coin", '''"He showed me one of the stones. Gilt still on it." {n}She turns the empty purse over again, as if something might have grown in it overnight.{/n} "Kenabres stones. I paid Brother Haldis to check one against his reliquary book. It matched. Now I'm walking round on them."
"And something else is gone. My list." {n}Her hand goes flat under her collarbone, where the purse hangs when she sleeps.{/n} "You read it. Every line. You're the one who took it."
{n}She holds out her palm, and it is steady.{/n}
"Give it back. Now, while I'm still too weak to take it off you."''',
      c('[Put the list in her hand] "Here. It\'s yours. I only borrowed it."', "given", flags=(WOKE, GIVEN_BACK)),
      c('[Keep it] "Not yet."', "kept", flags=(WOKE, KEEPS))),
    s_("given", '''{n}She unfolds the list and reads the last line. Then she borrows the chaplain's pen and writes beneath it: "Kenabres stones. Used for me. Owed."{/n}
{n}She folds it small, puts it in her purse and ties the strings badly.{/n}
"Acemi never got her helm back. I'll put these stones right, if it takes the rest of my life. Thank you, Commander. I'm still angry."''',
      c('"Be angry. You have time for it now."')),
    s_("kept", '''{n}Her hand stays out a moment longer. Then she closes it, slowly, around nothing.{/n}
"Then I'll steal it back." {n}She says it lightly. She does not mean it lightly.{/n} "Fair warning, Commander. I was better at this than you, and I've had a lot of practice being patient."''',
      c('"I\'ll keep my coat buttoned."')),
    s_("coin_word_paid", '''"On your word." {n}She shuts her eyes, then opens them again.{/n} "You paid a grave-robber with crusade gold. For the stones and his silence. Then you asked the chapel for credit. Wonderful. He's richer, the priests are poorer, and I'm alive to shout at you."''',
      c("Continue", "coin")),
], requires=(REVIVED, RETURNED), forbids=(WOKE, "seelah_dead"), delay=0, Areas=[DREZEN], Chapters=[3, 5])


# --- State dead_no_unit: the richer thief, and the stones by post -----------------------------------------------------

letter("seelah.trickster.dead.pickpocket_effects", "Her effects, without her", [
    nar("start", '''{n}Her effects came back to Drezen without her, in a sack with her name chalked on the side. A field chaplain's note is pinned to it: her body is in his keeping, under a sheet, and he does not send the dead down roads where too many carts have arrived with something else inside the sheet.{/n}
{n}A whetstone. A prayer book with a stolen library's stamp inside the cover, the stamp half scraped away and then, it seems, left alone on purpose. And a purse, tied badly.{/n}''',
      c("Continue", "purse")),
    nar("purse", '''{n}At the bottom of the purse is a square of paper folded very small: a list, in her hand, of every theft she can remember, most of them crossed out and marked "paid". The first line is not: "A mithral helm. Acemi."{/n}
''' + LIST_LAST + '''
{n}The chaplain's note goes on. He will not try the lesser rite on her; it brings the dead back weak, and it has failed him on the crusade's dead before. The greater rite wants two stones' worth of diamond dust, and he has a bowl and nothing to put in it, and one rule: a soul that has stood its trial cannot be raised. Nobody can say how long a soul waits before the Lady tries it, he writes; he has never dared find out. A fast rider reaches him in two days.{/n}''',
      c('[Pick the dead thief\'s pocket] "Old habits, Seelah. Whatever\'s in the purse is mine. Including that."', "stall",
        requires=(DIAMOND_HELD,), mythic="Trickster", alignment=("Chaotic", 1)),
      c('[Pick the dead thief\'s pocket] "Old habits, Seelah. Whatever\'s in the purse is mine. Including that."', "stall",
        forbids=(DIAMOND_HELD,), mythic="Trickster", alignment=("Chaotic", 1), flags=(CHAPLAIN,)),
      c('[Leave the purse tied] "Not like this."', abort=True)),
    nar("stall", '''{n}You put the list in your coat and go down to the chapel steps before the lamps are out.{/n}
''' + STALL, *lift_choices()),
    nar("lifted", LIFTED, c("Continue", "rider", forbids=(CHAPLAIN,)), c("Continue", "rider_word", requires=(CHAPLAIN,))),
    nar("grabbed", GRABBED, *caught_choices(
        c('[Give him your word] "Your name stays off every report. Let go."', "concealed_rider", forbids=(CHAPLAIN,), flags=(BROKER,)),
        c('[Give him your word] "Your name stays off every report. Let go."', "concealed_rider_word", requires=(CHAPLAIN,),
          flags=(BROKER,)))),
    nar("concealed_rider", CONCEALED, c("Continue", "rider")),
    nar("concealed_rider_word", CONCEALED, c("Continue", "rider_word")),
    nar("taken", SELLER_TAKEN, c("Continue", "rider", forbids=(CHAPLAIN,)), c("Continue", "rider_word", requires=(CHAPLAIN,)),
        paragraphs=TAKEN_REPORT),
    nar("paid", SELLER_PAID, c("Continue", "rider", forbids=(CHAPLAIN,)), c("Continue", "rider_word", requires=(CHAPLAIN,))),
    nar("rider", '''{n}You send the rider out with her savings, the relic-seller's stones and a diamond from your own coat: two stones' worth. You keep the list. Two days there, the chaplain's rite, two days back: nothing to do now but wait for the rider.{/n}''',
      c('"Ride fast."', requires=(DIAMOND_HELD,), remove_item=DIAMOND, flags=(DISPATCHED, HOLDS))),
    nar("rider_word", '''{n}You send the rider out with her savings, the relic-seller's stones, and your word, sealed, that the crusade will make good the other stone. You keep the list. Two days there, the chaplain's rite, two days back: nothing to do now but wait for the rider.{/n}''',
      c('"Ride fast."', crusade=("Favors", -100), flags=(DISPATCHED, HOLDS))),
], requires=("trickster", "trickster.ever", "seelah_dead", "seelah.dead.latched"), forbids=(FINALLY_DEAD, RETURNED, DISPATCHED),
   delay=24, TricksterDevice=True, TricksterState="dead_no_unit", Areas=[DREZEN])

# Q10 r2: the rider's four days are real. The chaplain's note waits >= 96 h after dispatch; she arrives two days after it,
# and only then is she returned, a correspondent and eligible for the presence.
letter("seelah.trickster.dead.effects_reply", "The chaplain's note", [
    nar("start", '''{n}The rider is back, mud to the saddle-skirts, with a note in the field chaplain's hand.{/n}''',
      c("Continue", "note", forbids=(CHAPLAIN,)), c("Continue", "note_word", requires=(CHAPLAIN,))),
    nar("note", '''"She sat up and asked who had been in her purse. I told her, and I showed her a stone with gilt on it. She said a word I will not write. She will come to Drezen when she can walk that far."''',
      c('"Tell her I\'ll be at Fye\'s."', flags=(REPLIED,))),
    nar("note_word", '''"I know Kenabres gilt when I see it. I ground the stones anyway, and spent my own reserve on your promise for the rest. She sat up and asked who had been in her purse. I told her. She will come to Drezen when she can walk that far. So, I expect, will every priest's opinion of your credit."''',
      c('"Let them talk. Tell her I\'ll be at Fye\'s."', flags=(REPLIED,))),
], requires=("trickster.ever", "seelah_dead", DISPATCHED), forbids=(RETURNED, REPLIED), delay=96,
   TricksterDevice=True, TricksterState="dead_no_unit")

letter("seelah.trickster.dead.effects_arrival", "Badly folded, again", [
    nar("start", '''{n}A note under your door, folded small, in a hand you last read at the bottom of a dead woman's purse.{/n}
"I'm in Drezen. I walked. Fye's, the table by the door. Bring my list, and bring something to drink, because I'm not paying, I haven't a copper to my name. I wonder why. - S."''',
      c('[Go to Fye\'s] "Coming."', flags=(RETURNED, CORRESPONDENT, "seelah.started"))),
], requires=("trickster.ever", "seelah_dead", REPLIED), forbids=(RETURNED,), delay=48,
   TricksterDevice=True, TricksterState="dead_no_unit")


# --- State dismissed: you stole my trick ---------------------------------------------------------------------------

# Inline beside the native "Yes" (Answer_0047) after Cue_0043; the one terminal choice continues into Cue_0050, so the
# native OnStop (Unrecruit, the walk-away cutscene, SeelahNotInParty_KickedOut) still runs.
SCENES.append(scene("seelah.trickster.dismissed.setup", "Check your pockets", "Seelah", 3,
    '"Safe travels. Check your pockets at the gate."', [
    nar("start", '''{n}Seelah hesitates, then offers you her hand, the way soldiers do when they are not sure they are allowed to embrace.{/n}
{n}You take it. You apologise for keeping her waiting. Her transfer papers, folded into her belt, are in your coat before she lets go.{/n}''',
      c("Continue", native_next=GOOD_LUCK, flags=(PRIMED, POCKETS))),
], requires=("trickster",), forbids=(*OWN, PRIMED, "seelah_dead", "seelah_gone"), last=5, optional=True, Relationship="seelah",
   AnswerLists=[DISMISSAL],
   NativeReturnCue=FINAL_DECISION, EntryMythic="PlayerIsTrickster", TricksterDevice=True, TricksterState="dismissed"))

letter("seelah.trickster.dismissed.late", "A transfer on the clerk's desk", [   # Areas: the gate clerk is in Drezen (Sol PP1)
    nar("start", '''{n}You find her transfer among the undelivered dispatches on the gate clerk's desk. No company has signed for her. The clerk pulls it from a stack of old post and lays it beside the letters for the next courier to the Eagle Watch. He is eating his lunch over them. There is a thumbprint of grease on the seal.{/n}''',
      c('[Lift the papers the way she taught you] "Excuse me. So sorry."', requires=(LESSON,), mythic="Trickster",
        check=dict(Skill="SkillThievery", DC=15, Success="lifted", Failure="caught", CommanderOnly=True)),
      c('[Lift the papers off the clerk\'s desk] "Excuse me."', forbids=(LESSON,), mythic="Trickster",
        check=dict(Skill="SkillThievery", DC=25, Success="lifted", Failure="caught", CommanderOnly=True)),
      c('[Let her go] "She said goodbye. I heard her."', "gone", flags=(DECLINED,))),
    nar("lifted", '''{n}You bump his elbow and apologise, and he apologises back, and you walk away with the papers. He never feels them go.{/n}
{n}The trick's not the hand. It's the apology.{/n}''',
      c('[Pocket them] "Come and get them, Seelah."', flags=(PRIMED, LATE))),
    nar("caught", '''{n}He feels it. He shouts. Half the gate turns in time to see the Commander of the crusade walk off with a dismissed paladin's papers under one arm, and nobody quite dares to stop you.{/n}
{n}By evening, wherever she is, she has heard about it.{/n}''',
      c('[Walk off with them anyway] "Crusade business."', alignment=("Chaotic", 1), flags=(PRIMED, LATE, CAUGHT))),
    nar("gone", '''{n}The courier comes at dusk and takes the papers north with the rest of the post. You watch him go from the wall, and you do not move your hands.{/n}''',
      c('"Good luck, Seelah."')),
], requires=("trickster", "seelah_gone", "seelah.gone.latched"), forbids=(PRIMED, RETURNED, DECLINED, "seelah_dead"), delay=48,
   TricksterDevice=True, TricksterState="dismissed", Areas=[DREZEN])

PAPERS_TEXT = '''"My transfer papers. My papers, Commander. No company in Mendev will sign me without them. The clerk at the gate laughed at me for a quarter of an hour, and then he told me who'd had them."
{n}She is furious, and trying very hard not to be impressed, and not managing either one properly.{/n}
"That's my trick. You stole my trick."'''

tavern("seelah.trickster.dismissed.back_for_the_papers", "You stole my trick", '"Seelah."', [
    nar("start", '''{n}She is waiting in the tavern, at the table nearest the door, with her back to the wall like a thief and her boots polished like a paladin. She does not get up.{/n}''',
      c("Continue", "papers", forbids=(CAUGHT,)), c("Continue", "papers_caught", requires=(CAUGHT,))),
    s_("papers_caught", '''"And you got caught. In front of the whole gate. I taught you better than that. No, I didn't. That's the problem, isn't it? I never finished teaching you anything."''',
      c("Continue", "papers")),
    s_("papers", PAPERS_TEXT + '''
"You sent me away. Fine. That was yours to do, and I went. Then you made sure I couldn't go anywhere else." {n}She puts one finger on the table between you.{/n} "Why?"''',
      c('[Hand them over] "They\'re yours. So\'s the door."', "handed",
        flags=(RETURNED, HERDED, CORRESPONDENT, "seelah.started")),
      c('[Make her take them] "Pick my pocket for them. Old habits."', "dared",
        flags=(RETURNED, HERDED, CORRESPONDENT, DARED, "seelah.started"))),
    s_("handed", '''{n}She takes them without looking at them and puts them inside her tunic, flat against her ribs, where nobody is going to get them again.{/n}
"The door. Right." {n}She stays sitting.{/n} "I haven't decided which way I'm going through it. That's mine too."''',
      c('"I know."')),
    nar("dared", '''{n}She stands, walks round the table, stumbles, catches your arm and says she is so sorry, what a clumsy fool. The papers are in her hand before she has finished the apology. So is your purse.{/n}''',
      c("Continue", "dared_2")),
    s_("dared_2", '''{n}She drops the purse back in your lap.{/n}
"There. Now we both know I'm still better at it." {n}She is almost smiling. Almost.{/n} "Don't do that to me again, Commander. I mean it. I'll pick your pocket for fun any day you like. I will not be herded."''',
      c('"Understood."')),
], requires=("trickster.ever", "seelah_gone", PRIMED), forbids=(RETURNED, "seelah_dead"), delay=48,
   TricksterDevice=True, TricksterState="dismissed")

letter("seelah.trickster.dismissed.back_for_the_papers_letter", "A note, badly folded", [
    nar("start", '''{n}A note, folded small enough to slip into a pocket and badly enough that it wants you to know it was folded in a temper.{/n}
"My transfer papers are in your coat. I know it. You know it. The Inheritor knows it. I sat at Fye's two nights like a civilised thief and you never came. Send them, or I come and get them, and you won't like how. - S."''',
      c('[Send them back] "Yours. Come and say thank you in person."', flags=(RETURNED, HERDED, CORRESPONDENT, "seelah.started"))),
], requires=("trickster.ever", "seelah_gone", PRIMED, "seelah.presence.failed"),
   forbids=(RETURNED, "seelah.trickster.dismissed.back_for_the_papers", "seelah_dead"), delay=144,
   TricksterDevice=True, TricksterState="dismissed")


# --- After the return, outside the party: her decision, the commit, her no -----------------------------------------

tavern("seelah.trickster.after.stay_or_go", "Two notices", '"Seelah. What now?"', [
    nar("start", '''{n}She has two recruiting notices on the table in front of her, weighted with her tankard so the draught from the door cannot take them.{/n}''',
      c("Continue", "choice")),
    s_("choice", '''"There's a relief company on the Drezen road that'll take a paladin with no references and a bad reputation. There's another one bound for the Sarkorian border that'll take anyone at all, and pays in turnips."
{n}She turns her tankard a quarter-turn.{/n}
"I haven't decided. You don't get to decide for me. You get to say what you'd like, and then I'll probably do the other thing, because I'm like that."''',
      c('[Say you\'d like her near Drezen] "Stay close. The crusade still needs a sword it trusts. So do I."', "folded",
        flags=(STAY, NEAR)),
      c('[Say she should go where she\'s needed] "Go where you\'re needed. Write."', "folded", flags=(STAY, FAR))),
    nar("folded", '''{n}She folds one notice and puts it in her purse. She does not show you which. The other she leaves on the table, face down, for the next fool.{/n}
"Thank you for saying it," {n}she says.{/n} "Now go away. I want to finish my drink without a Commander watching me decide things."''',
      c('"Finish your drink."')),
], requires=("trickster.ever", RETURNED, CORRESPONDENT), forbids=(STAY,), delay=24)

THRESHOLD = '''{n}She does not answer with words. She drags you up the tavern stairs by the belt, and on the landing you find the belt is in her hand and no longer round your waist.{/n}
"Ha. Got your belt. Old habits." {n}Her breath is hot on your mouth.{/n} "Now hold still. I'm taking the rest, and this time I'm not giving it back."
{n}She kisses you laughing, then not laughing. Her armour is already off; she wriggles out of the gambeson in one practised motion, all freckles and sword-callus, and has your shirt over your head before you have reached the top step. The door of the little room slams behind you. She backs you into it, bare to the waist, fingers already at your laces, and tumbles you down onto the bed under the eaves, palms flat on your chest, hair falling round both your faces. She grins down at you, flushed and triumphant, the way she grins on a wall after a charge that worked.{/n}'''

MORNING_NEAR = '''{n}Morning. She is sitting cross-legged on the bed in your shirt, lacing her boots, and she looks up with a grin.{/n}
"All there. I only wanted to know how much you're worth." {n}She stretches until her shoulders crack.{/n} "The Drezen road company can wait an hour. Iomedae forgive me, I'd do it again. Twice before breakfast, probably."'''

MORNING_FAR = '''{n}Morning. She is sitting cross-legged on the bed in your shirt, lacing her boots, and she looks up with a grin that does not quite hold.{/n}
"All there." {n}She looks at the window, where the road south is.{/n} "The border company leaves at noon. I said I was leaving and I am. But I'm coming back on every leave they give me, and you're going to be here when I do, and that isn't a question."'''

tavern("seelah.trickster.dismissed.commit", "Not as a sword", '"Seelah. Stay a while."', [
    s_("start", '''{n}The same table by the door. She has bought you a drink with money she swore she didn't have, and she pushes it across without looking at it.{/n}
"I stole to eat, in Solku. Then I stole a knight's helm, and she died without it, and I've been paying for that in a paladin's coat ever since. And now you've stolen from me, and I'm sitting here buying you a drink." {n}She spreads her hands.{/n} "Explain that. I've been turning it over ever since I came back."''',
      c("Continue", "near", forbids=(FAR,)), c("Continue", "far", requires=(FAR,))),
    s_("near", '''"I took the Drezen road company, by the way. Close enough to rob you on feast days."''', c("Continue", "ask")),
    s_("far", '''"I took the border company, by the way. So whatever you're going to say, say it like I'm leaving. Because I am."''',
      c("Continue", "ask")),
    nar("ask", '''{n}She waits, chin on her fist, the way she waits out a sermon she has heard before.{/n}''',
      c('[Ask her] "Seelah. Stay. Not as a sword."', "answer")),
    s_("answer", '''{n}She does not look away. She has never been good at looking away.{/n}
"Then say what as. Carefully, Commander. I'm listening with both ears and I've had half a drink."''',
      c('[Kiss her] "Stay. Not as a sword. As you."', "threshold", requires=("seelah.started", ROMANCE),
        forbids=(HOLDS,), flags=("seelah.committed",)),
      c('[Let her choose] "You know where the coat is."', "chooses", requires=(ROMANCE,), forbids=(HOLDS,),
        flags=("seelah.committed",)),
      c('[Be her friend] "Then as a friend. Same coat. Same door."', "friend", forbids=(ROMANCE,), flags=(FRIENDS,)),
      c('[Give her the door] "Go and help people. Write."', "door", flags=(FRIENDS,)),
      c('[Ask what\'s wrong] "You\'re not saying something."', "no", forbids=(HOLDS,)),
      c('[Ask what\'s wrong] "You\'re not saying something."', "no_death", requires=(HOLDS,), forbids=(GIVEN_BACK,)),
      # b9c: while the Commander still holds her list she will not say yes; giving it back first is the way through.
      c('[Put her list on the table first] "Yours. Every line. I only borrowed it."', "list_back",
        requires=(HOLDS, ROMANCE), forbids=(GIVEN_BACK,), flags=(GIVEN_BACK,)),
      # b9c: the list already given back (possession is holds_her_death without death_returned).
      c('[Kiss her] "Stay. Not as a sword. As you."', "threshold", requires=("seelah.started", ROMANCE, HOLDS, GIVEN_BACK),
        flags=("seelah.committed",)),
      c('[Let her choose] "You know where the coat is."', "chooses", requires=(ROMANCE, HOLDS, GIVEN_BACK),
        flags=("seelah.committed",)),
      c('[Ask what\'s wrong] "You\'re not saying something."', "no_stones", requires=(HOLDS, GIVEN_BACK))),
    s_("no_stones", '''{n}She presses her hand over the list inside her tunic.{/n}
"You read every line before you gave it back. The man on the last one had stones off the Kenabres altars. Now those stones have bought me back. I owe the people they were taken from. I don't know yet what I owe you."
{n}She finishes her drink.{/n}
"Ask me again when I've paid the first coin back myself. Not before."''',
      c('[Let her keep it] "Then I\'ll ask again, and I\'ll ask better."', flags=(DECLINED,))),
    s_("list_back", '''{n}She does not touch it at once. Then she unfolds it and reads it from the top, Acemi first, the way you would count the money in a purse somebody had just given back to you. At the last line she stops.{/n}
"You never crossed it out." {n}She borrows the stub of pencil behind the tankards and writes a line under it, and does not cross that out either: "Kenabres stones. Used for me. Owed."{/n}
{n}She folds it small and puts it inside her tunic, flat against her ribs.{/n} "All right. Now it's only you and me at this table. Now ask."''',
      c('[Kiss her] "Stay. Not as a sword. As you."', "threshold", requires=("seelah.started",), flags=("seelah.committed",)),
      c('[Let her choose] "You know where the coat is."', "chooses", flags=("seelah.committed",))),
    s_("chooses", '''{n}She looks at your coat, then at you. Then she laughs, low, and reaches across the table and takes your purse out of it without any apology at all.{/n}
"There. Chosen. Upstairs, Commander. Before someone finds me another cart to lift."''',
      c("Continue", "threshold")),
    nar("threshold", THRESHOLD, c("Continue", "morning_near", forbids=(FAR,)), c("Continue", "morning_far", requires=(FAR,))),
    s_("morning_near", MORNING_NEAR, c('"I\'ll count it again later."')),
    s_("morning_far", MORNING_FAR, c('"I\'ll be here."')),
    s_("friend", '''"As a friend." {n}She tries it out.{/n} "Yes. All right. I've had fewer of those than you'd think, and none who'd rob me for my own good."
{n}She clinks her tankard against yours.{/n}
"Same coat. Same door. Mind I don't take the coat."''',
      c('"I\'ll mind."')),
    s_("door", '''"Go and help people. Write." {n}She repeats it like an order she has decided to obey.{/n} "I will. Both. The letters will be badly spelled and full of complaints about turnips."''',
      c('"I\'ll read every one."')),
    s_("no", '''{n}She is quiet a long time.{/n}
"You took my papers so I'd have to come back. And I came." {n}She taps the table, once.{/n} "That clerk laughed at me for a quarter of an hour. Every company I asked looked at my empty belt before they looked at my face. I'm not sitting here because I chose to, Commander. I'm sitting here because you made sure I couldn't sit anywhere else."
{n}She finishes her drink.{/n}
"Ask me again after I've walked out that door once, on my own feet, and come back through it anyway."''',
      c('[Let her keep it] "Then I\'ll ask again, and I\'ll ask better."', flags=(DECLINED,))),
    s_("no_death", '''{n}Her hand goes to the place under her collarbone where her purse hangs, the way it does when she thinks nobody is watching.{/n}
"You've still got my list. In your coat. You've read every line of it, and you haven't given it back." {n}She is not angry. That is worse.{/n} "I can't say yes to someone who's carrying every theft I ever did. Give it back, or let me take it, and then ask me."''',
      c('[Let her keep it] "Then I\'ll ask again, and I\'ll ask better."', flags=(DECLINED,))),
], requires=("trickster.ever", RETURNED, STAY), forbids=("seelah.committed", DECLINED, FRIENDS), delay=48,
   RequiresAnyGroups=[[ROMANCE, COURTED]])

tavern("seelah.trickster.dismissed.second_ask", "Her way", '"Seelah. I\'m asking again. Better."', [
    s_("price", '''{n}She walked out of Fye's the night you first asked, on her own feet, and took the Sarkorian road. Four days later she walked back in the same way, and nobody sent for her. She is at the table by the door when you come in, and she does not pretend to be surprised.{/n}
"Better. All right." {n}She stands and comes round the table.{/n} "Here's how it goes. You keep your hands at your sides, and I rob you. I take whatever I want out of your coat, and you don't get to know what until I'm gone."
{n}She stops close enough that you can smell the tavern smoke in her hair.{/n}
"That's fair. That's the fairest thing that's happened between us."''',
      c('[Let her pick your pocket] "Go on. Take it back. Whatever you like."', "robbed", requires=(ROMANCE,),
        flags=("seelah.committed", ROBBED, RECONCILED)),
      c('[Keep your hand on your purse] "No."', "closed", flags=("seelah.closed",))),
    nar("robbed", '''{n}You keep your hands at your sides. It is harder than it sounds. She takes her time, and she apologises the whole while, softly, for nothing in particular, and you do not watch her hands.{/n}
{n}When she steps back, your coat is lighter by something. You do not know what, except that if her list was still in it, it is not there now. She is smiling.{/n}
"Now ask me," {n}she says, and does not wait for you to finish.{/n}''',
      c("Continue", "threshold")),
    nar("threshold", THRESHOLD, c("Continue", "morning_near", forbids=(FAR,)), c("Continue", "morning_far", requires=(FAR,))),
    s_("morning_near", MORNING_NEAR, c('"I\'ll count it again later."')),
    s_("morning_far", MORNING_FAR, c('"I\'ll be here."')),
    s_("closed", '''{n}She looks at your hand on your purse. Then at your face. Then at the hand again, as if it might change its mind.{/n}
"Then keep it. All of it." {n}She picks up her notice and her tankard.{/n} "Goodbye, Commander. I mean that one."''',
      c('"Goodbye, Seelah."')),
], requires=("trickster.ever", DECLINED, RETURNED, ROMANCE), forbids=("seelah.committed",), delay=96)


# --- Q10: the courtship outside the party (a fresh return has no kiss behind it), and the failed-anchor visits ------
# A dismissed or no-unit Seelah comes back with no romance from the companion hub. The market game is earned on the
# presence: she lifts the Commander's glove and ring, the Commander steals them back (the lesson lowers the DC) or does
# not, and in the alley the player chooses the kiss (TAVERN_KISSED feeds ROMANCE) or a friend. The commit waits for it.

tavern("seelah.trickster.after.courtship", "Finders keepers", '"Seelah. Walk with me."', [
    s_("start", '''{n}She is on her feet before you reach the table, cloak already round her shoulders, as if she has been waiting all evening for an excuse.{/n}
"Walk with you? Only if you're game. The east market's open till the chapel bell." {n}She grins, the grin of a woman who intends to win.{/n} "A contest, Commander, fair and agreed. Between here and the well I lift one thing off you, and you've got till the bell to lift it back. Off each other and nobody else; nobody in that market who needs their purse loses a copper on our account, or Iomedae hears about it from me. You win, I buy. I win, you buy, and I keep the prize."''',
      c('[Agree to her terms] "You\'re on. One thing, off me, and I take it back."', "market")),
    nar("market", '''{n}The east market at dusk is lamp-smoke, wet wool and pilgrims haggling over candles. She walks at your shoulder and talks the whole way: the Sarkorian company's cook, the price of turnips, a sergeant she would like to punch. Between the candle stall and the well she trips over nothing, catches your arm, and tells you she is so sorry, what a clumsy cow.{/n}
{n}Your left glove is gone. So is the signet you keep in it.{/n}
"Bell's in a quarter of an hour, Commander," {n}she says, without turning round.{/n}''',
      c('[Take it back the way she taught you] "Sorry. Sorry, my fault."', requires=(LESSON,),
        check=dict(Skill="SkillThievery", DC=15, Success="won", Failure="lost", CommanderOnly=True)),
      c('[Take it back] "Hold still a moment."', forbids=(LESSON,),
        check=dict(Skill="SkillThievery", DC=20, Success="won", Failure="lost", CommanderOnly=True)),
      c('[Let her keep it and follow her] "I\'m buying, then."', "lost")),
    nar("won", '''{n}You catch her up at the well and ask her the way to the chapel like a lost pilgrim, and apologise for the onions on your breath, and come away with the glove and the ring inside it. She never feels it go.{/n}
{n}Ten steps on she pats her belt and stops dead in the street, mouth open.{/n}
"You -" {n}She is laughing too hard to finish. She grabs your collar and hauls you into the gap between the cooper's and the chandler's, out of the lamplight, to get her breath back.{/n} "That was my lift. That was my lift exactly. Iomedae forgive me, I've made a monster."''',
      c("Continue", "alley")),
    nar("lost", '''{n}The chapel bell goes. She turns round, walking backwards, pulls your glove on, pushes your ring onto her thumb over it and admires it in the lamplight.{/n}
"Finders keepers. You owe me a drink and a ring." {n}She takes your collar and pulls you into the gap between the cooper's and the chandler's, out of the lamplight, where nobody from the crusade will see the Commander being robbed blind.{/n} "Don't sulk. You were watching my face the whole time. Everybody does."''',
      c("Continue", "alley")),
    s_("alley", '''{n}The gap is so narrow that her back is against the cooper's wall and your shoulder against the chandler's, and there is nowhere at all for your hands. She does not seem to mind. She is warm through the cloak, and she smells of tavern smoke and the oil she uses on her sword.{/n}
"So." {n}Her eyes go to your mouth and stay there.{/n} "I came back to Drezen for something, Commander, and it wasn't Fye's beer."''',
      c('[Kiss her]', "kissed", flags=(TAVERN_KISSED, COURTED)),
      c('[Step back into the street] "For the drinks, Seelah. And a friend."', "friends_walk", flags=(COURTED,))),
    nar("kissed", '''{n}You kiss her, or she kisses you; later neither of you will admit which. She kisses the way she charges, quick and then not quick at all, one fist in your collar and the other hand already inside your coat. When you come up for breath she is holding the glove again.{/n}
"Ha." {n}She is flushed to the ears, freckles and all.{/n} "Keeping this one. Iomedae saw that, and She can take it up with me on Sunday." {n}She kisses you again, hard and fast, as if to make sure the first one happened.{/n} "Drinks are on you. Move, before the cooper comes out and asks what we're doing to his wall."''',
      c('"Moving."')),
    s_("friends_walk", '''{n}She looks at you a breath longer, then laughs and lets go of your collar.{/n}
"Drinks and a friend. Fine. That's more than I walked in with." {n}She tosses you the glove. The ring she turns in the light a while before she slaps it into your palm.{/n} "Next time I keep it."''',
      c('"Next time."')),
], requires=("trickster.ever", RETURNED, STAY), forbids=(ROMANCE, COURTED, "seelah.committed", DECLINED), delay=24)

# When Fye's anchor fails (the tavern shut, Fye gone), the presence cannot stand, so every presence beat after the
# papers has a remote visit twin: she comes to the Commander's quarters in the citadel. Same nodes, choices and flags
# (the shared flags keep the twins exclusive); only the place changes.

VISIT_THRESHOLD = """{n}She does not answer with words. She takes you by the belt and walks you backwards across your own quarters, past the map table and the cold supper, and somewhere on the way the belt comes away in her hand.{/n}
"Ha. Got your belt. Old habits." {n}Her breath is hot on your mouth.{/n} "Now hold still. I'm taking the rest, and this time I'm not giving it back."
{n}She kisses you laughing, then not laughing. She heels the bedchamber door shut, wriggles out of her gambeson in one practised motion, all freckles and sword-callus, and has your shirt over your head before you reach the bed. She backs you into it, bare to the waist, fingers already at your laces, and tumbles you down onto the Commander's own blankets, palms flat on your chest, hair falling round both your faces. She grins down at you, flushed and triumphant, the way she grins on a wall after a charge that worked.{/n}"""


def visit_twin(src_id, new_id, title, swaps):
    src = next(x for x in SCENES if x["Id"] == src_id)
    twin = copy.deepcopy(src)
    for key in ("ContactUnit", "InteractionHub"):   # Sol PP1: keep Areas; the visit is still staged in Drezen
        twin.pop(key, None)
    twin.update(Id=new_id, Title=title, Entry="", Remote=True, Kind="visit")
    twin["Requires"] = twin["Requires"] + [FAILED]
    for old, new in swaps:
        hits = 0
        for node in twin["Nodes"]:
            if old in node["Text"]:
                node["Text"] = node["Text"].replace(old, new.strip())
                hits += 1
        if not hits:
            from authoring.generation_errors import record
            record("overlay.swap_snippet", scene=new_id, detail=old[:70])
    SCENES.append(twin)


QUARTERS = ("{n}She is waiting in your quarters in the citadel when you come off the wall, on your one good chair with her "
            "boots on your map table. She got tired of waiting for you at Fye's; she says the guard let her in for a smile, which is a lie, and "
            "for the latest gossip from Fye's, which probably is not.{/n}\n")

visit_twin("seelah.trickster.after.stay_or_go", "seelah.trickster.after.stay_or_go_visit", "Two notices", [
    ("{n}She has two recruiting notices on the table in front of her, weighted with her tankard so the draught from the door cannot take them.{/n}",
     QUARTERS + "{n}Two recruiting notices lie on the map table in front of her, weighted with your inkwell so the draught from the door cannot take them.{/n}"),
    ("She turns her tankard a quarter-turn.", "She turns your inkwell a quarter-turn."),
    ("I want to finish my drink without a Commander watching me decide things.",
     "I want to finish your wine without a Commander watching me decide things. Yes, in your rooms. Go and inspect something."),
])
visit_twin("seelah.trickster.after.courtship", "seelah.trickster.after.courtship_visit", "Finders keepers", [
    ("{n}She is on her feet before you reach the table, cloak already round her shoulders, as if she has been waiting all evening for an excuse.{/n}",
     "{n}She is at your door when you come off the wall, cloak already round her shoulders, as if she has been waiting all evening for an excuse.{/n}"),
])
visit_twin("seelah.trickster.dismissed.commit", "seelah.trickster.dismissed.commit_visit", "Not as a sword", [
    ("{n}The same table by the door. She has bought you a drink with money she swore she didn't have, and she pushes it across without looking at it.{/n}",
     "{n}Your quarters again, and your one good chair turned to face the door. She has brought a jug of something bought with money she swore she didn't have, and she pours you a cup and pushes it across without looking at it.{/n}"),
    ("She borrows the stub of pencil behind the tankards", "She takes the pen off your desk"),
    ("She clinks her tankard against yours.", "She knocks her cup against yours."),
    (THRESHOLD, VISIT_THRESHOLD),
])
visit_twin("seelah.trickster.dismissed.second_ask", "seelah.trickster.dismissed.second_ask_visit", "Her way", [
    ("{n}She walked out of Fye's the night you first asked, on her own feet, and took the Sarkorian road. Four days later she walked back in the same way, and nobody sent for her. She is at the table by the door when you come in, and she does not pretend to be surprised.{/n}",
     "{n}She walked out of the citadel gate the night you first asked, on her own feet, and took the Sarkorian road. Four days later she walked back in through it, and nobody sent for her. She is in your quarters when you come in, and she does not pretend to be surprised.{/n}"),
    ("smell the tavern smoke in her hair", "smell the road dust in her hair"),
    ("She picks up her notice and her tankard.", "She picks up her notice and her cloak."),
    (THRESHOLD, VISIT_THRESHOLD),
])

# --- Q10 r2: Seelah's word on the relic-seller, after the caught lift (whichever answer the Commander chose) -----------

SELLER_WORD_TOLD = irabeth_told(
    '''"Tell Irabeth. You did it." {n}She crosses the line out, and writes "done" beside it, and then, after a moment, "not by me".{/n}''',
    '''"Irabeth should have been the one to hear it." {n}She looks at the line a long while. Then she crosses it out anyway, writes "done, by the court" beside it, and after a moment, "not by me".{/n} "She'd have had him scrubbing Kenabres altars on his knees till they bled. A cell will have to do."''',
    '''"Irabeth's gone where a letter takes a month to catch her. Fine. A court did the telling." {n}She crosses the line out, writes "done, by the court" beside it, and after a moment, "not by me".{/n} "I'll write to her anyway. She'll want to know some bastard was selling Kenabres off a stone at a time."''')

SELLER_NODES = [
    s_("start", '''{n}She has a scrap of paper out with the last line of her list on it, copied fresh in her own hand, and she is looking at it.{/n}
"Brother Haldis says the relic-seller's stall is empty. I want to know what you did with him, Commander. All of it."''',
      c("Continue", "concealed", requires=(BROKER,)), c("Continue", "taken", requires=(TAKEN,)),
      c("Continue", "paid", requires=(PAID,))),
    s_("concealed", '''"Your word. In front of the saints. To a man who robs the dead." {n}She folds the scrap very small.{/n}
"It's your word, not mine, so I'll let it stand. I'm not going to make a liar of you to feel clean. But every pilgrim he sold a stone to, I'm going to find, and buy it back, a coin at a time. Don't you dare offer me the money."''',
      c('"I won\'t."', flags=(SELLER_HEARD,))),
    n("taken", "Seelah", '''{n}Her grin is slow, and very wide.{/n}''',
      c('"They can hate me. It was your line."', flags=(SELLER_HEARD,)), portrait="Seelah",
      paragraphs=SELLER_WORD_TOLD + (p('''"The court clerks will hate you for a year. Good. Iomedae's courts can stand to be reminded that the dead come first."'''),)),
    s_("paid", '''"You paid him." {n}She says it flatly, the way she would say you had stepped in something.{/n}
"With the crusade's gold. To a man who prised stones off the Kenabres dead." {n}She does not cross the line out. She writes beside it, small: "and the Commander paid him".{/n}
"I know why. I'm alive, so I can't even shout at you properly. I'm going to shout at you a little anyway."''',
      c('"Shout. I earned it."', flags=(SELLER_HEARD,))),
]
SELLER_ANY = [[BROKER, TAKEN, PAID]]

hub("seelah.trickster.dead.seller_word", "The last line", '"Seelah. About the relic-seller."', copy.deepcopy(SELLER_NODES),
    requires=(REVIVED, WOKE), forbids=(), delay=24, Chapters=[3, 4, 5], RequiresAnyGroups=SELLER_ANY)
tavern("seelah.trickster.dead_no_unit.seller_word", "The last line", '"Seelah. About the relic-seller."', copy.deepcopy(SELLER_NODES),
       requires=("trickster.ever", RETURNED, CORRESPONDENT, HOLDS), forbids=(REVIVED, SELLER_HEARD), delay=24,
       RequiresAnyGroups=SELLER_ANY)
# Q10 r3: the failed-anchor twin; SELLER_HEARD keeps the pair exclusive.
visit_twin("seelah.trickster.dead_no_unit.seller_word", "seelah.trickster.dead_no_unit.seller_word_visit", "The last line", [
    ("{n}She has a scrap of paper out with the last line of her list on it, copied fresh in her own hand, and she is looking at it.{/n}",
     "{n}She is waiting in your quarters in the citadel, a scrap of paper on your map table with the last line of her list copied onto it, and she is looking at it.{/n}"),
])

# --- Epilogue ------------------------------------------------------------------------------------------------------

PICKPOCKET_PARAGRAPHS = (
    p("{n}Seelah kept the list in her purse, tied in badly on purpose. Beneath the relic-seller's entry she kept her own "
      "account of what she owed the Kenabres dead, and what she had paid back.{/n}", requires=(GIVEN_BACK,)),
    p("{n}The Commander never did give it back. Seelah never stopped trying to take it. Every year the attempts grew more "
      "elaborate, and every year, at the end, she apologised.{/n}", requires=(KEEPS,), forbids=(ROBBED,)),
    p("{n}The chapel never quite forgave the credit the Commander had asked of it, or the stolen stones it had ground. Seelah "
      "paid back both herself, the chapel and the Kenabres reliquary, a coin at a time, out of a paladin's stipend. It "
      "took her eleven years.{/n}", requires=(CHAPLAIN,)),
    p("{n}The relic-seller told the story of the night the Commander of the crusade robbed him in every tavern in Drezen, "
      "for years, and never told it the same way twice. Nobody bought him a drink for it twice either.{/n}", requires=(BROKER,),
      forbids=(TAKEN, PAID)),
    p("{n}Of the transfer papers she said only that they had come back to her, and that she now kept them somewhere no "
      "Commander would ever look.{/n}", requires=(HERDED,), forbids=(DARED,)),
    p("{n}Of the transfer papers she said only that she had taken them back herself, and the Commander's purse with "
      "them, and returned the purse, which was more than the Commander had done.{/n}", requires=(DARED,)),
    p("{n}Whatever she took from the Commander's coat on the night of her price, she never said. The Commander never "
      "asked. It was, by the terms of the agreement, none of their business.{/n}", requires=(ROBBED,)),
    p("{n}She and the Commander stayed what they had agreed to be over a drink: friends, with a door between "
      "them that neither ever locked.{/n}", requires=(FRIENDS,), forbids=("seelah.committed", "seelah.closed")),
    p("{n}She did not come back after the night she was refused her price. Her letters stopped at the Sarkorian border.{/n}",
      requires=("seelah.closed",)),
    # Q10 r2 (appended; epilogue.papers slices this tuple from index 3): the caught lift's other two answers.
    p("{n}The relic-seller served two years in the Inheritor's cells. Seelah visited him once, with a list of every pilgrim he "
      "had sold a 'saint's tear' to, and made him help her find them all.{/n}", requires=(TAKEN,)),
    p("{n}Crusade gold had bought the relic-seller's stones and his silence. He left Drezen a rich man. Seelah spent the next "
      "three winters tracking down the pilgrims he had sold stones to, and buying back what she could, a coin at a time.{/n}", requires=(PAID,)),
)

PICKPOCKET_OPENERS = (
    p("{n}Seelah remembered the night at her bier: her purse emptied, her list read without asking, and the Kenabres stones "
      "brought to the chaplain's bowl. She gave thanks for her life. She still wanted an account of what had bought it.{/n}", requires=(REVIVED,)),
    p("{n}Seelah remembered her effects opened in Drezen while her body lay in a field chaplain's keeping. Her savings went "
      "by rider with stones off the Kenabres altars. Her list stayed in the Commander's coat. She gave thanks for her life, "
      "then asked for the list.{/n}", forbids=(REVIVED,)),
)

SCENES.append(scene("seelah.trickster.epilogue.pickpocket", "Whatever was in the purse", "Epilogue", 5, "", [
    n("end", "Narrator", '''{n}Of everything the Commander ever took from her, Seelah said, her purse was the one that counted.{/n}''',
      portrait="Seelah", paragraphs=PICKPOCKET_OPENERS + PICKPOCKET_PARAGRAPHS)],
    requires=(RETURNED, HOLDS), last=99, Relationship="seelah"))

SCENES.append(scene("seelah.trickster.epilogue.papers", "Her papers", "Epilogue", 5, "", [
    n("end", "Narrator", '''{n}Seelah kept her transfer papers inside her tunic for the rest of the war, flat against her ribs. She told anyone who asked that a Commander had once stolen them to make her come back, and that it had worked, and that she was still deciding whether to forgive it.{/n}''',
      portrait="Seelah", paragraphs=PICKPOCKET_PARAGRAPHS[3:])],
    requires=(RETURNED, HERDED), forbids=(HOLDS,), last=99, Relationship="seelah"))

SCENES.append(scene("seelah.trickster.epilogue.commit", "Now we're even", "Epilogue", 5, "", [
    n("end", "Narrator", '''{n}On a visit after the war, Seelah left a purse on the Commander's pillow, tied badly, with a note inside: "Ask me properly. - S."{/n}
{n}She was waiting at Fye's. The Commander asked. She caught their belt and pulled them close.{/n}
"There. Took you long enough. Upstairs. I want you, and I've wasted enough of my leave staring across this table."
{n}In the room above, she kicked off her boots and pulled her shirt over her head. Her mouth found the Commander's throat while her callused hands opened their shirt. A buckle caught between them; she swore, laughing, and freed it. Then she drew the Commander down onto the bed with her, bare skin warm against theirs, her breath coming short at their ear.{/n}
"Better. Now kiss me before somebody finds us a job."
{n}By morning she was late for muster. She scrambled into her clothes, found a missing boot under the Commander's coat, and came back from the door for another kiss.{/n}''', portrait="Seelah")],
    requires=("trickster.ever", LATE_COMMITTED, ROMANCE),
    forbids=("seelah.committed", "seelah.closed", DECLINED, FRIENDS), last=99, Relationship="seelah"))

SCENES.append(scene("seelah.trickster.epilogue.refused", "An empty purse, every winter", "Epilogue", 5, "", [
    n("end", "Narrator", '''{n}Seelah ran her relief company for many years. Every winter a parcel came for the Commander with nothing in it but an empty purse, tied badly. Nobody else understood it. The Commander always did.{/n}''',
      portrait="Seelah")],
    requires=("trickster.ever", DECLINED), forbids=("seelah.committed", "seelah.closed"), last=99, Relationship="seelah"))


# --- Reactions (Irabeth, Sosiel), one pair per world ---------------------------------------------------------------

IRABETH_GONE = ("irabeth_dead",)
IRABETH_BACK = {"irabeth_dead": "irabeth.trickster.returned"}
SOSIEL_GONE = ("sosiel.dead", "sosiel.kicked_out")

REACTIONS = [
    reaction("Irabeth", "seelah.trickster.dead.react_irabeth", (RETURNED, REVIVED, WOKE, KEEPS),
             '''{n}Irabeth puts down her pen, which is how you know she means it.{/n}
"You robbed a paladin's corpse, Commander. She got up. And she swore in my hearing, in the chapel, to rob you back for it."
{n}She picks the pen up again.{/n}
"A relic-seller from under the chapel steps boarded up his stall and left by the east gate in a hurry. Seelah asked me why. I told her I didn't know. I'm asking you, and I can see you're not going to tell me. I'm going to pray about this. Then I'm going to buy her a drink and pray about that."''',
             answer_list=IRABETH_HUB, forbids=IRABETH_GONE + (TAKEN,), chapter=3, last=5, entry='"Seelah is back."',
             Chapters=[3, 5], ForbidOverrides=dict(IRABETH_BACK)),
    # Q10 r3: the list given back at her waking; no vow to rob the Commander back (appended sibling).
    reaction("Irabeth", "seelah.trickster.dead.react_irabeth_given", (RETURNED, REVIVED, WOKE, GIVEN_BACK),
             '''{n}Irabeth puts down her pen, which is how you know she means it.{/n}
"You robbed a paladin's corpse, Commander. She got up. And she came to the chapel with a list in her hand and asked me to witness a new line on it, which she will not let me read."
{n}She picks the pen up again.{/n}
"A relic-seller from under the chapel steps boarded up his stall and left by the east gate in a hurry. I'm not going to ask. I'm going to pray about it, and then I'm going to buy her a drink."''',
             answer_list=IRABETH_HUB, forbids=IRABETH_GONE + (TAKEN,), chapter=3, last=5,
             entry='"Seelah is back, and she has her list."', Chapters=[3, 5], ForbidOverrides=dict(IRABETH_BACK)),
    # Q10 r2: the caught lift answered by an arrest; Irabeth has the seller in her cells (appended sibling).
    reaction("Irabeth", "seelah.trickster.dead.react_irabeth_taken", (RETURNED, REVIVED, TAKEN),
             '''{n}Irabeth puts down her pen, which is how you know she means it.{/n}
"You robbed a paladin's corpse, Commander. She got up. And there is a relic-seller in my cells who swears the Commander of the crusade picked his pocket, and then broke the court's seal on the evidence by writing on a sergeant's slate."
{n}She picks the pen up again.{/n}
"The clerks want me to complain to you. Seelah wants me to give you a medal. I'm going to give you neither, and I'm going to hang his stones' settings over the chapel door so every pilgrim sees them."''',
             answer_list=IRABETH_HUB, forbids=IRABETH_GONE, chapter=3, last=5, entry='"Seelah is back. And the relic-seller?"',
             Chapters=[3, 5], ForbidOverrides=dict(IRABETH_BACK)),
    reaction("Sosiel", "seelah.trickster.dead.react_sosiel", (RETURNED, REVIVED, WOKE, GIVEN_BACK),
             '''{n}Sosiel is sketching, and he does not stop.{/n}
"She showed me a list. Old thefts, most of them crossed out, with what she paid back beside each one. The last line isn't crossed out, and it's new." {n}He shades something.{/n} "She said it's the most expensive thing she owns. I believe her. I didn't ask what it cost."''',
             answer_list=SOSIEL_HUB, forbids=SOSIEL_GONE, chapter=3, last=5, entry='"Have you seen Seelah?"'),
    # b9c: the list kept at her waking; Sosiel hears the other half of it.
    reaction("Sosiel", "seelah.trickster.dead.react_sosiel_kept", (RETURNED, REVIVED, WOKE, KEEPS),
             '''{n}Sosiel is sketching, and he does not stop.{/n}
"She asked me whether a paladin who steals something back from her Commander has to confess it. I said it depends on the Commander." {n}He shades something.{/n} "She said it depended on the thing, and that you know which thing. I think you should button your coat."''',
             answer_list=SOSIEL_HUB, forbids=SOSIEL_GONE, chapter=3, last=5, entry='"Have you seen Seelah?"'),
    reaction("Irabeth", "seelah.trickster.dead_no_unit.react_irabeth", (RETURNED, CORRESPONDENT, HOLDS),
             '''"A letter from your paladin came across my desk. First line: 'Tell the Commander I'm counting my coins.' Second line's a list."
{n}She holds it up. It is a long list.{/n}
"You owe her a great many coins, Commander. And something else, she says, that she won't put in writing."''',
             answer_list=IRABETH_HUB, forbids=IRABETH_GONE, chapter=3, last=5, entry='"Any word from Seelah?"',
             Chapters=[3, 5], ForbidOverrides=dict(IRABETH_BACK)),
    reaction("Sosiel", "seelah.trickster.dead_no_unit.react_sosiel", (RETURNED, CORRESPONDENT, HOLDS),
             '''"She wrote to me from the field chapel where they raised her. She asked me to paint her a purse. Just a purse, tied badly."
{n}He shows you the canvas. It is a very good purse.{/n}
"I didn't ask why. I'm finishing it tonight. I think it's a portrait."''',
             answer_list=SOSIEL_HUB, forbids=SOSIEL_GONE, chapter=3, last=5, entry='"Have you heard from Seelah?"'),
    reaction("Irabeth", "seelah.trickster.dismissed.react_irabeth", (RETURNED, HERDED),
             '''"Seelah came through the gate asking after her transfer. I told her the Commander's coat is the worst-kept vault in Drezen."
{n}Irabeth's mouth twitches.{/n}
"She said, 'I know. I used to rob better.' I'm choosing to believe that was about you."''',
             answer_list=IRABETH_HUB, forbids=IRABETH_GONE, chapter=3, last=5, entry='"Seelah is back in Drezen."',
             Chapters=[3, 5], ForbidOverrides=dict(IRABETH_BACK)),
    reaction("Sosiel", "seelah.trickster.dismissed.react_sosiel", (PRIMED, RETURNED, "seelah_gone"),
             '''{n}Sosiel sets down his brush.{/n}
"You took her papers so she'd have to come back." {n}He says it without blame, which is its own kind of blame.{/n} "I've done worse for people I loved. I just never did it with my hands."''',
             answer_list=SOSIEL_HUB, forbids=SOSIEL_GONE, chapter=3, last=5, entry='"Seelah left."'),
]
SCENES.extend(REACTIONS)


# --- The registered route ------------------------------------------------------------------------------------------

# Superseded on Trickster (the spec's renamed ids; retired by gating, never deleted): seelah.fate_life is the old
# Trickster revive and pickpocket replaces it; seelah.fate_return is its waking, replaced by wakes once she has returned.
RETIRED = ("seelah.fate_life",)


def _scene(by_id, id):
    if id not in by_id:
        raise ValueError("Seelah Trickster integration missing scene: " + id)
    return by_id[id]


def integrate(payload):
    """Save-safe edits to the registered route (no id, node or choice renamed, removed or reordered): the relationship
    patch, the presence, the derived keys, the retired Trickster revive, and G6(b) grief overrides. Her companion-hub
    scenes and endings lift her death or dismissal once she has returned; her remote letters, which assume she is back
    in the party, lift them only in the retained-death world (REJOINED)."""
    rel = payload["Relationships"]["seelah"]
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(v) for k, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, a fallen Seelah's purse may name a richer thief to rob for her, and a "
                        "dismissed one may find her papers missing. Look for her at Fye's.")
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    derived = payload.setdefault("Derived", {})
    for key, groups in DERIVED.items():
        derived[key] = [list(g) for g in groups]
    removable = payload.setdefault("RemovableItems", [])
    if DIAMOND not in removable:
        removable.append(DIAMOND)
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    for id in RETIRED:
        _scene(by_id, id)["Forbids"].append("trickster.ever")
    _scene(by_id, "seelah.fate_return")["Forbids"].append(RETURNED)
    ours = {s["Id"] for s in SCENES}
    for s in payload["Scenes"]:
        if s.get("Relationship") != "seelah" or s["Id"] in ours or s["Id"] in RETIRED:
            continue
        value = REJOINED if s.get("Remote") else RETURNED
        for flag in ("seelah_dead", "seelah_gone"):
            if flag in s["Forbids"]:
                s.setdefault("ForbidOverrides", {})[flag] = value
    from storylines import seelah_round2
    seelah_round2.integrate(payload)
    # Irabeth's two Seelah barks sit on Seelah's companion hub; they lift her death or dismissal once she has returned.
    for id in ("irabeth.trickster.dead.react_seelah", "irabeth.trickster.killed.react_seelah"):
        if id in by_id:
            fo = by_id[id].setdefault("ForbidOverrides", {})
            fo["seelah_dead"] = RETURNED
            fo["seelah_gone"] = RETURNED


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'seelah.trickster.dead.effects_arrival',
    'seelah.trickster.dead.effects_reply',
    'seelah.trickster.dismissed.back_for_the_papers',
    'seelah.trickster.dismissed.back_for_the_papers_letter',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]

# Authored round-2 situations, route-local receipts and save-safe slot staging.
from storylines import seelah_round2
seelah_round2.prepare(SCENES, PRESENCES, DERIVED)

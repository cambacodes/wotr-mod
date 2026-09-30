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
    ROMANCE: [["seelah.kissed"], ["seelah.roof_kissed"], ["seelah.lovers"]],
    REJOINED: [[RETURNED, REVIVED]],
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
    s_("start", '''{n}Seelah looks at you for a long moment, the way she looks at a stranger's hands in a crowded market.{/n}
"A paladin of Iomedae, teaching the Commander to pick pockets. The Inheritor is going to have words with me."
{n}She grins anyway, and it is not a paladin's grin.{/n}
"Fine. One lift. And you swear it now, on whatever you swear on: never on anyone who needs what's in the purse. I learned that one too late."''',
      c('[Let her show you] "Show me. Slowly. I want to see where the hand goes."', "lesson")),
    nar("lesson", '''{n}She walks past you, stumbles, catches your arm to steady herself and says she is so sorry, what a clumsy fool, is your shoulder all right? Then she holds up your purse between two fingers.{/n}
{n}You never felt it go.{/n}
"The trick's not the hand," she says, and gives it back. "It's the apology. Everybody watches your face while you're saying sorry. Nobody watches your fingers."''',
      c('[Practise on her] "Again. On you, this time."',
        check=dict(Skill="SkillThievery", DC=15, Success="caught_it", Failure="caught_you", CommanderOnly=True))),
    nar("caught_it", '''{n}You bump her shoulder and apologise. You mean the apology, a little, which may be the point. You come away with one of her coppers.{/n}
{n}Seelah turns out the purse, counts, and stares at you.{/n}
"...Huh. You're a natural. That isn't a compliment, Commander. Keep it where I can see it."''',
      c('[Keep the coin] "Finders keepers."', flags=(LESSON, "seelah.started"))),
    nar("caught_you", '''{n}She catches your wrist before your fingers are halfway to the strings, and holds it there, not hard.{/n}
"Too slow. And you looked at the purse. Never look at the purse." Her thumb taps your knuckle once. "Do it like you're sorry. You'll get it. Some other day."''',
      c('[Give her back her own coin, with one of yours] "Two for one. For the lesson."', flags=(LESSON, "seelah.started"))),
], requires=("trickster",), forbids=("seelah_dead", "seelah_gone", LESSON), delay=0, Chapters=[3, 4, 5])


# --- The richer thief: her list's last line, and the lift she taught -------------------------------------------------
# Shared by the bier and the effects: the relic-seller under the chapel steps, the lift (the lesson lowers the DC), and
# on a failed check the Commander's nerve instead of a clean hand. Both roads fill the bowl; only the cost differs.

LIST_LAST = '''{n}The last line is newer than the rest, the ink hardly a week old; she must have found him since she came to Drezen: "The relic-seller under the chapel steps. Sells 'saints' tears' to pilgrims. They are the Kenabres reliquary diamonds; I would know them anywhere, I used to steal the candles off those altars. Not mine to take back. I am a paladin now. Tell Irabeth."{/n}'''

STALL = '''{n}The relic-seller's stall is a plank on two barrels under the chapel steps, shuttered for the night. He is still behind it, counting by a shielded lamp: a soft, careful man in pilgrim's grey, with a fat pouch at his belt that he touches every little while, the way a man touches a thing he loves.{/n}'''

LIFTED = '''{n}You stumble into his lamp and catch it before it falls, and you are so sorry, what a clumsy fool, did it burn him? He watches your face the whole time you are apologising. Nobody watches your fingers.{/n}
{n}Round the corner you open the pouch in your palm. Small, cloudy stones, a good many of them, some still with a crumb of gilt where somebody's knife prised them out of a setting.{/n}'''

GRABBED = '''{n}He feels it go. His hand closes on your wrist with the strings still in your fingers, and he draws breath to shout for the watch, and then he sees whose wrist it is.{/n}
"Commander." {n}He does not let go.{/n} "Those are consecrated stones. Bought honestly."
{n}You tell him, quietly, what a Kenabres reliquary looks like with its settings emptied, and whose altars they stood on, and what the Inheritor's knights do to a man who robs their dead. He does not let go. He is a careful man, and he has done his sums.{/n}
"Then the Inheritor never hears my name. Not from you, and not from your dead paladin's little list." {n}His eyes go to your coat, where the paper is.{/n} "Your word, Commander, in front of the saints. Or I shout, and we both hang."
{n}You give it. His hand opens. It is the only thing you have bought tonight that you will have to keep, and it is the one line on her list she asked someone to finish: Tell Irabeth. He knows your face now, and he will tell the story to anyone who buys him a drink, everywhere but the Inheritor's door.{/n}'''


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
    nar("coin", '''{n}Her savings go into the chaplain's bowl coin by coin: coppers, a few silver, one gold piece she must have been keeping for something. It is not enough. It was never going to be enough. The rite wants five thousand gold in diamond dust, and a stone from your own coat would not cover a quarter of what is missing.{/n}
{n}At the bottom of the purse is a square of paper folded very small. It is a list, in her hand, of every theft she can remember. Most lines are crossed out, each with a sum beside it and the word "paid". The first line is not: "A mithral helm. Acemi." There is no sum beside it.{/n}
''' + LIST_LAST,
      c('[Pick the dead thief\'s pocket] "Old habits, Seelah. Whatever\'s in the purse is mine. Including that."', "stall",
        mythic="Trickster", alignment=("Chaotic", 1)),
      c('[Leave the purse tied] "Not like this."', abort=True)),
    nar("stall", '''{n}You fold the list into your coat and tell the chaplain to keep his candles lit.{/n}
''' + STALL, *lift_choices()),
    nar("lifted", LIFTED, c("Continue", "pocketed")),
    nar("grabbed", GRABBED, c("Continue", "pocketed", flags=(BROKER,))),
    nar("pocketed", '''{n}The chaplain is still at the bier when you come back. You tip the pouch into his bowl, and the stones rattle down on top of her coppers.{/n}
{n}He picks one out and turns it to the candle. There is gilt on it.{/n}
"These came off the Kenabres altars." {n}He does not ask how you came by them. He looks at the paper in your hand, and at her, and for a while he says nothing at all.{/n} "They were given to the dead of Kenabres, Commander."''',
      c('[Leave a diamond of your own on the relic-seller\'s plank] "Then one goes back to him, so he has nothing to take to the Inheritor. She\'s Kenabres dead. Begin."',
        requires=(DIAMOND_HELD,), revive="seelah", remove_item=DIAMOND, flags=(RETURNED, REVIVED, HOLDS, "seelah.started")),
      c('[Give him your word] "She\'s Kenabres dead. Begin. If anyone asks where they came from, the crusade answers for them."',
        forbids=(DIAMOND_HELD,), revive="seelah", crusade=("Favors", -100), flags=(RETURNED, REVIVED, HOLDS, CHAPLAIN, "seelah.started"))),
], requires=("trickster", "trickster.ever", "seelah_dead", "seelah.dead.latched", FINALLY_DEAD), forbids=(RETURNED, "seelah_gone"),
   delay=24, TricksterDevice=True, TricksterState="dead", Recovery="seelah", Areas=[DREZEN])

hub("seelah.trickster.dead.wakes", "Whatever you took", '"Seelah."', [
    s_("start", '''"You robbed my corpse."
{n}She is sitting on the edge of the chapel cot in her shirt, turning her empty purse inside out. She laughs once, badly.{/n}
"The worst part is I'd have done the same. Every copper I had, Commander. Even the gold piece, and I've carried that one since Solku without ever spending it. Did She let me go, or did you buy me?"''',
      c('"The chaplain did the work. Your purse paid for some of it. A grave-robber paid for the rest."', "coin", forbids=(CHAPLAIN,)),
      c('"The chaplain did the work. A grave-robber paid for it, and the chapel took his stones on my word."', "coin_word", requires=(CHAPLAIN,))),
    s_("coin_word", '''"On your word." She closes her eyes. "So the whole chapel knows the Commander robbed a dead paladin, then robbed a grave-robber, and asked the priests to bless the takings. Wonderful. I'm going to be hearing about that at every mass until the Wound shuts."''',
      c("Continue", "coin")),
    s_("coin", '''"He showed me one of the stones. Gilt still on it." She turns the empty purse over again, as if something might have grown in it overnight. "Kenabres stones. I used to steal the candles off those altars when I was nine. Now I'm walking round on them."
"And something else is gone. My list." {n}Her hand goes flat under her collarbone, where the purse hangs when she sleeps.{/n} "You read it. Every line. You're the one who took it."
{n}She holds out her palm, and it is steady.{/n}
"Give it back. Now, while I'm still too weak to take it off you."''',
      c('[Put the list in her hand] "Here. It\'s yours. I only borrowed it."', "given", flags=(WOKE, GIVEN_BACK)),
      c('[Keep it] "Not yet."', "kept", flags=(WOKE, KEEPS))),
    s_("given", '''{n}She unfolds it and reads the last line. Under it, in your hand, somebody has written "Taken back." She looks at that for a long time.{/n}
{n}Then she borrows the chaplain's pen and writes one more line beneath it, and does not cross it out: "Kenabres stones. Stolen for me. Owed."{/n}
{n}She folds the list very small, puts it in her purse and ties the strings badly, on purpose.{/n}
"Acemi never got her helm back. I'll get this one right, if it takes the rest of my life. Thank you, Commander. I'm still angry."''',
      c('"Be angry. You have time for it now."')),
    s_("kept", '''{n}Her hand stays out a moment longer. Then she closes it, slowly, around nothing.{/n}
"Then I'll steal it back." She says it lightly. She does not mean it lightly. "Fair warning, Commander. I was better at this than you, and I've had a lot of practice being patient."''',
      c('"I\'ll keep my coat buttoned."')),
], requires=(REVIVED, RETURNED), forbids=(WOKE, "seelah_dead"), delay=0, Areas=[DREZEN], Chapters=[3, 5])


# --- State dead_no_unit: the richer thief, and the stones by post -----------------------------------------------------

letter("seelah.trickster.dead.pickpocket_effects", "Her effects, without her", [
    nar("start", '''{n}She fell on the Sarkorian border, and she lies there still, under a sheet, in a row at a field hospital. The road north to Drezen runs through demon country; the hospital does not send its dead along it, because too many carts have arrived with something else inside the sheet. Her effects came back without her, in a sack with her name chalked on the side.{/n}
{n}A whetstone. A prayer book with a stolen library's stamp inside the cover, the stamp half scraped away and then, it seems, left alone on purpose. And a purse, tied badly.{/n}''',
      c("Continue", "purse")),
    nar("purse", '''{n}At the bottom of the purse is a square of paper folded very small: a list, in her hand, of every theft she can remember, most of them crossed out and marked "paid". The first line is not: "A mithral helm. Acemi."{/n}
''' + LIST_LAST + '''
{n}The chaplain at the border hospital has written too. He has a bowl and nothing to put in it, and one rule: a soul that has stood its trial cannot be raised. Nobody can say how long a soul waits before the Lady tries it, he writes; he has never dared find out. A fast rider reaches him in two days.{/n}''',
      c('[Pick the dead thief\'s pocket] "Old habits, Seelah. Whatever\'s in the purse is mine. Including that."', "stall",
        requires=(DIAMOND_HELD,), mythic="Trickster", alignment=("Chaotic", 1), remove_item=DIAMOND,
        flags=(RETURNED, HOLDS, CORRESPONDENT, "seelah.started")),
      c('[Pick the dead thief\'s pocket] "Old habits, Seelah. Whatever\'s in the purse is mine. Including that."', "stall",
        forbids=(DIAMOND_HELD,), mythic="Trickster", alignment=("Chaotic", 1), crusade=("Favors", -100),
        flags=(RETURNED, HOLDS, CORRESPONDENT, CHAPLAIN, "seelah.started")),
      c('[Leave the purse tied] "Not like this."', abort=True)),
    nar("stall", '''{n}You put the list in your coat and go down to the chapel steps before the lamps are out.{/n}
''' + STALL, *lift_choices()),
    nar("lifted", LIFTED, c("Continue", "rider", forbids=(CHAPLAIN,)), c("Continue", "rider_word", requires=(CHAPLAIN,))),
    nar("grabbed", GRABBED, c("Continue", "rider", forbids=(CHAPLAIN,), flags=(BROKER,)),
        c("Continue", "rider_word", requires=(CHAPLAIN,), flags=(BROKER,))),
    nar("rider", '''{n}You send the rider south with her savings and the relic-seller's stones, and leave a diamond of your own on his plank, so that he has nothing left to complain of but his pride. He pockets it without a word. By morning the stall under the chapel steps is boarded up, and he has gone out by the east gate. You keep the list.{/n}
{n}Four days later a note comes back in the chaplain's hand: "She sat up and asked who had been in her purse. I told her, and I showed her a stone with gilt on it. She said a word I will not write. She will come to Drezen when she can walk that far."{/n}''',
      c('"Tell her I\'ll be at Fye\'s."')),
    nar("rider_word", '''{n}You send the rider south with her savings, the relic-seller's stones, and your word, sealed, that the crusade answers for where they came from. You keep the list. The chaplain there knows Kenabres gilt when he sees it; he grinds the stones anyway, on a Commander's promise, and every priest on the border hears of it by the end of the week.{/n}
{n}Four days later a note comes back: "She sat up and asked who had been in her purse. I told her. She will come to Drezen when she can walk that far. So, I expect, will the relic-seller's complaint."{/n}''',
      c('"Let him complain. Tell her I\'ll be at Fye\'s."')),
], requires=("trickster", "trickster.ever", "seelah_dead", "seelah.dead.latched"), forbids=(FINALLY_DEAD, RETURNED), delay=24,
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

letter("seelah.trickster.dismissed.late", "A transfer on the clerk's desk", [
    nar("start", '''{n}Two days on, her transfer is still on the gate clerk's desk, waiting for a courier to the Eagle Watch. The clerk is eating his lunch over it. There is a thumbprint of grease on the seal.{/n}''',
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
   TricksterDevice=True, TricksterState="dismissed")

PAPERS_TEXT = '''"My transfer papers. My papers, Commander. No company in Mendev will sign me without them. The clerk at the gate laughed at me for a quarter of an hour, and then he told me who'd had them."
{n}She is furious, and trying very hard not to be impressed, and not managing either one properly.{/n}
"That's my trick. You stole my trick."'''

tavern("seelah.trickster.dismissed.back_for_the_papers", "You stole my trick", '"Seelah."', [
    nar("start", '''{n}She is waiting in the tavern, at the table nearest the door, with her back to the wall like a thief and her boots polished like a paladin. She does not get up.{/n}''',
      c("Continue", "papers", forbids=(CAUGHT,)), c("Continue", "papers_caught", requires=(CAUGHT,))),
    s_("papers_caught", PAPERS_TEXT + '''
"And you got caught. In front of the whole gate. I taught you better than that. No, I didn't. That's the problem, isn't it? I never finished teaching you anything."''',
      c("Continue", "papers")),
    s_("papers", '''"You sent me away. Fine. That was yours to do, and I went. Then you made sure I couldn't go anywhere else." She puts one finger on the table between you. "Why?"''',
      c('[Hand them over] "They\'re yours. So\'s the door."', "handed",
        flags=(RETURNED, HERDED, CORRESPONDENT, "seelah.started")),
      c('[Make her take them] "Pick my pocket for them. Old habits."', "dared",
        flags=(RETURNED, HERDED, CORRESPONDENT, DARED, "seelah.started"))),
    s_("handed", '''{n}She takes them without looking at them and puts them inside her tunic, flat against her ribs, where nobody is going to get them again.{/n}
"The door. Right." She stays sitting. "I haven't decided which way I'm going through it. That's mine too."''',
      c('"I know."')),
    nar("dared", '''{n}She stands, walks round the table, stumbles, catches your arm and says she is so sorry, what a clumsy fool. The papers are in her hand before she has finished the apology. So is your purse.{/n}''',
      c("Continue", "dared_2")),
    s_("dared_2", '''{n}She drops the purse back in your lap.{/n}
"There. Now we both know I'm still better at it." She is almost smiling. Almost. "Don't do that to me again, Commander. I mean it. I'll pick your pocket for fun any day you like. I will not be herded."''',
      c('"Understood."')),
], requires=("trickster.ever", "seelah_gone", PRIMED), forbids=(RETURNED, "seelah_dead"), delay=48,
   TricksterDevice=True, TricksterState="dismissed")

letter("seelah.trickster.dismissed.back_for_the_papers_letter", "A note, badly folded", [
    nar("start", '''{n}A note, folded small enough to slip into a pocket and badly enough that it wants you to know it was folded in a temper.{/n}
"My transfer papers are in your coat. I know it. You know it. The Inheritor knows it. Fye's is boarded up, so I can't wait for you there like a civilised thief. Send them, or I come and get them, and you won't like how. - S."''',
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
"Thank you for saying it," she says. "Now go away. I want to finish my drink without a Commander watching me decide things."''',
      c('"Finish your drink."')),
], requires=("trickster.ever", RETURNED, CORRESPONDENT), forbids=(STAY,), delay=24)

THRESHOLD = '''{n}She does not answer with words. She drags you up the tavern stairs by the belt, and on the landing you find the belt is in her hand and no longer round your waist.{/n}
"Ha. Got your belt. Old habits." Her breath is hot on your mouth. "Now hold still. I'm taking the rest, and this time I'm not giving it back."
{n}She kisses you laughing, then not laughing. Her armour is already off; she wriggles out of the gambeson in one practised motion, all freckles and sword-callus, and has your shirt over your head before you have reached the top step. The door of the little room slams behind you. She backs you into it, bare to the waist, fingers already at the lacing of your breeches, and tumbles you down onto the narrow bed. Then she swings a knee over your hips and straddles you, palms flat on your chest, hair falling round both your faces, and grins down at you like a thief who has just got away with something.{/n}'''

MORNING_NEAR = '''{n}Morning. She is sitting cross-legged on the bed counting your coins, and she hands the purse back with a grin.{/n}
"All there. I only wanted to know how much you're worth." She stretches until her shoulders crack. "The Drezen road company can wait an hour. Iomedae forgive me, I'd do it again. Twice before breakfast, probably."'''

MORNING_FAR = '''{n}Morning. She is sitting cross-legged on the bed counting your coins, and she hands the purse back with a grin that does not quite hold.{/n}
"All there." She looks at the window, where the road south is. "The border company leaves at noon. I said I was leaving and I am. But I'm coming back on every leave they give me, and you're going to be here when I do, and that isn't a question."'''

tavern("seelah.trickster.dismissed.commit", "Not as a sword", '"Seelah. Stay a while."', [
    s_("start", '''{n}The same table by the door. She has bought you a drink with money she swore she didn't have, and she pushes it across without looking at it.{/n}
"I was a thief because nobody ever gave me anything. I became a paladin because somebody did. And now you've stolen from me, and I'm sitting here buying you a drink." She spreads her hands. "Explain that. I've been trying to all week."''',
      c("Continue", "near", forbids=(FAR,)), c("Continue", "far", requires=(FAR,))),
    s_("near", '''"I took the Drezen road company, by the way. Close enough to rob you on feast days."''', c("Continue", "ask")),
    s_("far", '''"I took the border company, by the way. So whatever you're going to say, say it like I'm leaving. Because I am."''',
      c("Continue", "ask")),
    nar("ask", '''{n}She waits, chin on her fist, the way she waits for a mark to finish talking.{/n}''',
      c('[Ask her] "Seelah. Stay. Not as a sword."', "answer")),
    s_("answer", '''{n}She does not look away. She has never been good at looking away.{/n}
"Then say what as. Carefully, Commander. I'm listening with both ears and I've had half a drink."''',
      c('[Kiss her] "Stay. Not as a sword. As you."', "threshold", requires=("seelah.started", ROMANCE),
        flags=("seelah.committed",)),
      c('[Let her choose] "You know where the coat is."', "chooses", requires=(ROMANCE,), flags=("seelah.committed",)),
      c('[Be her friend] "Then as a friend. Same coat. Same door."', "friend", forbids=(ROMANCE,), flags=(FRIENDS,)),
      c('[Give her the door] "Go and help people. Write."', "door", flags=(FRIENDS,)),
      c('[Ask what\'s wrong] "You\'re not saying something."', "no", forbids=(HOLDS,)),
      c('[Ask what\'s wrong] "You\'re not saying something."', "no_death", requires=(HOLDS,))),
    s_("chooses", '''{n}She looks at your coat, then at you. Then she laughs, low, and reaches across the table and takes your purse out of it without any apology at all.{/n}
"There. Chosen. Upstairs, Commander, before I think about it like a paladin."''',
      c("Continue", "threshold")),
    nar("threshold", THRESHOLD, c("Continue", "morning_near", forbids=(FAR,)), c("Continue", "morning_far", requires=(FAR,))),
    s_("morning_near", MORNING_NEAR, c('"I\'ll count it again later."')),
    s_("morning_far", MORNING_FAR, c('"I\'ll be here."')),
    s_("friend", '''"As a friend." She tries it out. "Yes. All right. I've had fewer of those than you'd think, and none who'd rob me for my own good."
{n}She clinks her tankard against yours.{/n}
"Same coat. Same door. Mind I don't take the coat."''',
      c('"I\'ll mind."')),
    s_("door", '''"Go and help people. Write." She repeats it like an order she has decided to obey. "I will. Both. The letters will be badly spelled and full of complaints about turnips."''',
      c('"I\'ll read every one."')),
    s_("no", '''{n}She is quiet a long time.{/n}
"You took my papers so I'd have to come back. And I came." She taps the table, once. "That clerk laughed at me for a quarter of an hour. Every company I asked this week looked at my empty belt before they looked at my face. I'm not sitting here because I chose to, Commander. I'm sitting here because you made sure I couldn't sit anywhere else."
{n}She finishes her drink.{/n}
"Ask me again after I've walked out that door once, on my own feet, and come back through it anyway."''',
      c('[Let her keep it] "Then I\'ll ask again, and I\'ll ask better."', flags=(DECLINED,))),
    s_("no_death", '''{n}Her hand goes to the place under her collarbone where her purse hangs, the way it does when she thinks nobody is watching.{/n}
"You've still got my list. In your coat. You've read every line of it, and you haven't given it back." She is not angry. That is worse. "I can't say yes to someone who's carrying every theft I ever did. Give it back, or let me take it, and then ask me."''',
      c('[Let her keep it] "Then I\'ll ask again, and I\'ll ask better."', flags=(DECLINED,))),
], requires=("trickster.ever", RETURNED, STAY), forbids=("seelah.committed", DECLINED), delay=48)

tavern("seelah.trickster.dismissed.second_ask", "Her way", '"Seelah. I\'m asking again. Better."', [
    s_("price", '''{n}She walked out of Fye's the night you first asked, on her own feet, and took the Sarkorian road. Four days later she walked back in the same way, and nobody sent for her. She is at the table by the door when you come in, and she does not pretend to be surprised.{/n}
"Better. All right." She stands and comes round the table. "Here's how it goes. You stand still, and I rob you. I take whatever I want out of your coat, and you don't get to know what until I'm gone."
{n}She stops close enough that you can smell the tavern smoke in her hair.{/n}
"That's fair. That's the fairest thing that's happened between us."''',
      c('[Let her pick your pocket] "Go on. Take it back. Whatever you like."', "robbed", requires=(ROMANCE,),
        flags=("seelah.committed", ROBBED)),
      c('[Keep your hand on your purse] "No."', "closed", flags=("seelah.closed",))),
    nar("robbed", '''{n}You stand still. It is harder than it sounds. She takes her time, and she apologises the whole while, softly, for nothing in particular, and you do not watch her hands.{/n}
{n}When she steps back, your coat is lighter by something. You do not know what. She is smiling.{/n}
"Now ask me," she says, and does not wait for you to finish.''',
      c("Continue", "threshold")),
    nar("threshold", THRESHOLD, c("Continue", "morning_near", forbids=(FAR,)), c("Continue", "morning_far", requires=(FAR,))),
    s_("morning_near", MORNING_NEAR, c('"I\'ll count it again later."')),
    s_("morning_far", MORNING_FAR, c('"I\'ll be here."')),
    s_("closed", '''{n}She looks at your hand on your purse for a long moment.{/n}
"Then keep it. All of it." She picks up her notice and her tankard. "Goodbye, Commander. I mean that one."''',
      c('"Goodbye, Seelah."')),
], requires=("trickster.ever", DECLINED, RETURNED, ROMANCE), forbids=("seelah.committed",), delay=48)


# --- Epilogue ------------------------------------------------------------------------------------------------------

PICKPOCKET_PARAGRAPHS = (
    p("She kept the list in her purse for the rest of her life, tied in badly on purpose. The last line was never crossed "
      "out. She showed it to exactly two people, and one of them was the Commander.", requires=(GIVEN_BACK,)),
    p("The Commander never did give it back. Seelah never stopped trying to take it. Every year the attempts grew more "
      "elaborate, and every year, at the end, she apologised.", requires=(KEEPS,)),
    p("The chapel never quite forgave being asked to raise a paladin on stolen stones. Seelah paid the Kenabres "
      "reliquary back herself, a coin at a time, out of a paladin's stipend. It took her eleven years.", requires=(CHAPLAIN,)),
    p("The relic-seller told the story of the night the Commander of the crusade robbed him in every tavern in Drezen, "
      "for years, and never told it the same way twice. Nobody bought him a drink for it twice either.", requires=(BROKER,)),
    p("Of the transfer papers she said only that they had come back to her, and that she now kept them somewhere no "
      "Commander would ever look.", requires=(HERDED,), forbids=(DARED,)),
    p("Of the transfer papers she said only that she had taken them back herself, and the Commander's purse with "
      "them, and returned the purse, which was more than the Commander had done.", requires=(DARED,)),
    p("Whatever she took from the Commander's coat on the night of her price, she never said. The Commander never "
      "asked. It was, by the terms of the agreement, none of their business.", requires=(ROBBED,)),
    p("She and the Commander stayed what they had agreed to be over a tankard at Fye's: friends, with a door between "
      "them that neither ever locked.", requires=(FRIENDS,), forbids=("seelah.committed", "seelah.closed")),
    p("She did not come back after the night she was refused her price. Her letters stopped at the Sarkorian border.",
      requires=("seelah.closed",)),
)

SCENES.append(scene("seelah.trickster.epilogue.pickpocket", "Whatever was in the purse", "Epilogue", 5, "", [
    n("end", "Narrator", '''{n}Seelah never quite forgave the night at the bier: every coin she had, her list read without asking, and a grave-robber robbed in her name. She never said which of the three she minded most.{/n}''',
      portrait="Seelah", paragraphs=PICKPOCKET_PARAGRAPHS)],
    requires=(RETURNED, HOLDS), last=99, Relationship="seelah"))

SCENES.append(scene("seelah.trickster.epilogue.papers", "Her papers", "Epilogue", 5, "", [
    n("end", "Narrator", '''{n}Seelah kept her transfer papers inside her tunic for the rest of the war, flat against her ribs. She told anyone who asked that a Commander had once stolen them to make her come back, and that it had worked, and that she was still deciding whether to forgive it.{/n}''',
      portrait="Seelah", paragraphs=PICKPOCKET_PARAGRAPHS[3:])],
    requires=(RETURNED, HERDED), forbids=(HOLDS,), last=99, Relationship="seelah"))

SCENES.append(scene("seelah.trickster.epilogue.commit", "Now we're even", "Epilogue", 5, "", [
    n("end", "Narrator", '''{n}After the war the Commander found a purse on the pillow one morning, tied badly on purpose, with a note inside in Seelah's hand: "Now we're even. Ask me properly."{/n}
{n}The Commander did.{/n}''', portrait="Seelah")],
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
    reaction("Irabeth", "seelah.trickster.dead.react_irabeth", (RETURNED, REVIVED),
             '''{n}Irabeth puts down her pen, which is how you know she means it.{/n}
"You robbed a paladin's corpse, Commander. She got up. And she swore in my hearing, in the chapel, to rob you back for it."
{n}She picks the pen up again.{/n}
"A relic-seller from under the chapel steps boarded up his stall this week and left by the east gate in a hurry. Seelah asked me why. I told her I didn't know. I'm asking you, and I can see you're not going to tell me. I'm going to pray about this. Then I'm going to buy her a drink and pray about that."''',
             answer_list=IRABETH_HUB, forbids=IRABETH_GONE, chapter=3, last=5, entry='"Seelah is back."',
             Chapters=[3, 5], ForbidOverrides=dict(IRABETH_BACK)),
    reaction("Sosiel", "seelah.trickster.dead.react_sosiel", (RETURNED, REVIVED),
             '''{n}Sosiel is sketching, and he does not stop.{/n}
"She showed me a list. Old thefts, most of them crossed out, with what she paid back beside each one. The last line isn't crossed out, and it's new." He shades something. "She said it's the most expensive thing she owns. I believe her. I didn't ask what it cost."''',
             answer_list=SOSIEL_HUB, forbids=SOSIEL_GONE, chapter=3, last=5, entry='"Have you seen Seelah?"'),
    reaction("Irabeth", "seelah.trickster.dead_no_unit.react_irabeth", (RETURNED, CORRESPONDENT, HOLDS),
             '''"A letter from your paladin came across my desk. First line: 'Tell the Commander I'm counting my coins.' Second line's a list."
{n}She holds it up. It is a long list.{/n}
"You owe her a great many coins, Commander. And something else, she says, that she won't put in writing."''',
             answer_list=IRABETH_HUB, forbids=IRABETH_GONE, chapter=3, last=5, entry='"Any word from Seelah?"',
             Chapters=[3, 5], ForbidOverrides=dict(IRABETH_BACK)),
    reaction("Sosiel", "seelah.trickster.dead_no_unit.react_sosiel", (RETURNED, CORRESPONDENT, HOLDS),
             '''"She wrote to me from the border hospital. She asked me to paint her a purse. Just a purse, tied badly."
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
"You took her papers so she'd have to come back." He says it without blame, which is its own kind of blame. "I've done worse for people I loved. I just never did it with my hands."''',
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
    # Irabeth's two Seelah barks sit on Seelah's companion hub; they lift her death or dismissal once she has returned.
    for id in ("irabeth.trickster.dead.react_seelah", "irabeth.trickster.killed.react_seelah"):
        if id in by_id:
            fo = by_id[id].setdefault("ForbidOverrides", {})
            fo["seelah_dead"] = RETURNED
            fo["seelah_gone"] = RETURNED

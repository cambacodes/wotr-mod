"""Arueshalae, the beats between each Trickster answer and its commit (arueshalae.md F18; §3 states).

- The chaplain (romance failed): the crusade's spoken appointment has to be lived in before the question on the chapel
  steps. Desna is "the Tender of Dreams" and the travellers' goddess; the Desnan travel blessing is authored.
- The returned (dead in the party): the count of days since she ate, and what she ate.
- The fallen (evil, killed at the lair, returned on the queen's credit): at the jeweller's arcade at night before the arrangement,
  still a villain. Canon register, MeetEvilArusha/Cue_0008 ab5e0787: "I believed the lies of a deceitful goddess... For
  mortals? For this blithering meat?"
"""
from story_format import c, n, scene
from storylines.arueshalae_trickster import (AFTERTASTE, CHAPLAIN, CLOSED, COMMITTED, DEAD, DREZEN, EVIL_DEAD, EVIL_UNIT,
                                             FED_ON_PRISONER, FED_ON_YOU, HUB, HUNGRY, P, RECRUITED, RETURNED, REUNITED,
                                             TAVERN_FAILED, DREZEN_PLACES, TAVERN_PRESENCE, UNIT, YARD_PRESENCE, ALLY, IF_ASKED,
                                             EVERY_TIME)
from storylines.arueshalae_treatment import ELYSIUM, INTAKE, KITCHEN, TOUCHED

SCENES = []
CENSER = P + "chaplain.censer"
DYING = P + "chaplain.the_dying"
HELD_HIS_HAND = P + "chaplain.held_his_hand"
COMPLAINT = P + "chaplain.complaint"
STAYS_CHAPLAIN = P + "chaplain.stays"
COUNTING = P + "returned.counting"
SOSIEL_OFFERED = P + "react.sosiel_fed"       # Sosiel's offer, played (a reaction scene id once completed)
LANN_SAID = P + "react.lann_prisoner"         # Lann's word on the prisoner, played
SERGEANT = P + "evil.sergeant"
DAYBOOK = P + "evil.daybook"
GUARD = (CLOSED, DEAD, EVIL_DEAD, RECRUITED)
BACK = dict(ForbidOverrides={DEAD: RETURNED})


def a(id, text, *choices, **kw):
    return n(id, "Arueshalae", text, *choices, portrait="Arueshalae", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Arueshalae", **kw)


def hub(id, title, chapter, entry, nodes, requires, forbids=(), delay=0, last=5, chapters=None, optional=True, **extra):
    SCENES.append(scene(id, title, "Arueshalae", chapter, entry, nodes, requires=("trickster.ever", *requires),
                        forbids=(*GUARD, id, *forbids), delay=delay, last=last, optional=optional,
                        Relationship="arueshalae", AnswerLists=[HUB], ContactUnit=UNIT,
                        Chapters=list(chapters or range(chapter, last + 1)), **{**BACK, **extra}))


def tavern(id, title, entry, nodes, requires, forbids=(), delay=0):
    """At night, at the jeweller's arcade; the tailor's-awning copy when the jeweller is gone (the same beat)."""
    for hub_key, suffix, extra, unit in DREZEN_PLACES:
        SCENES.append(scene(id + suffix, title, "Arueshalae", 5, entry, [dict(nd) for nd in nodes],
                            requires=("trickster.ever", RETURNED, EVIL_DEAD, REUNITED, *requires, *extra),
                            forbids=(CLOSED, COMMITTED, ALLY, id, id + "_yard", *forbids), delay=delay, last=5,
                            optional=True, Relationship="arueshalae", Areas=[DREZEN], Chapters=[5], ContactUnit=unit,
                            InteractionHub=hub_key))


# --- The chaplain ----------------------------------------------------------------------------------------------

hub(CENSER, "Which end of the censer", 3, '"How is the shrine, Chaplain?"', [
    a("start", '''{n}She winces at the title, and then, you notice, straightens a little under it.{/n}
"I set fire to the altar cloth on the first morning. Not badly. The censer. Nobody tells you it has a draught hole, and I held it upside down, and an acolyte of Iomedae put it out with his cloak and then was very polite about it for the rest of the day, which was worse." {n}She rubs soot off her knuckle that has been there for days.{/n}
"The second company don't care. They just want their swords blessed and someone to talk to after. I'm very good at the talking after. I've heard every kind of confession there is. Usually I was the thing being confessed."''',
        c("Continue", "confession")),
    a("confession", '''"A boy came to me. He'd run, at Kenabres. Left his post, hid in a cellar while the demons went past. His whole company died and he didn't, and he's never told anyone." {n}She is looking at her hands.{/n}
"And I understood him. That's the terrible part. I didn't have to pretend. I know exactly what it's like to want the wrong thing so badly you do it before you've decided. I told him so. I didn't tell him why I knew."
"He slept that night. The first whole night in months. He came back to tell me. And I've been wondering ever since whether that's a blessing, or whether I just fed on him in a new way."''',
        c('"It\'s a blessing. You gave him something and took nothing."', "blessing", flags=(CENSER,)),
        c('"Maybe both. Maybe that\'s what chaplains do."', "both", flags=(CENSER,))),
    a("blessing", '''"Gave and took nothing." {n}She turns it over, testing it the way she tests your jokes for the hook.{/n} "He came back smiling. He slept because I spoke to him, and I didn't take anything for it. I keep wondering how that can be enough." {n}She almost smiles.{/n} "Don't tell the Iomedaeans. They'll want me to do the sermons."''', c()),
    a("both", '''{n}She laughs, startled.{/n} "That's what the acolyte said. The one with the cloak. He said all chaplains live on other people's sins; it's only a question of what you do with them afterwards." {n}She looks at the soot on her knuckle.{/n} "I'm going to learn which end of the censer is which. And then I'm going to do this properly."''', c()),
], (CHAPLAIN,), delay=24, chapters=(3, 5))

hub(DYING, "Last rites", 5, '"You weren\'t at the evening blessing."', [
    a("start", '''"I was in the field hospital." {n}Her eyes are dry and very bright.{/n} "A pikeman from Nerosyan. Gut wound, from the siege. The healers had done everything. He asked for the chaplain, and I was the chaplain, so they sent for me."
"He wanted his hand held. He kept reaching for mine. And I stood there with my hands behind my back, Commander, while a dying man reached for me, because if I'd taken it I'd have taken the last of him with it. Even the last of him would have tasted good. That's what I was thinking. With him reaching."''',
        c("Continue", "song")),
    a("song", '''"So I sang to him instead. The Desnan travellers' blessing, the one for the road. 'Go gently where the road goes, and the stars go with you.' I don't have a good voice. He didn't mind. He held the bed-rail, because I wouldn't let him hold me." {n}She swallows.{/n}
"He died at the end of the second verse. The orderly said he looked peaceful. I don't know. I wasn't looking at his face. I was looking at his hand on the rail, and hating myself for being glad it wasn't on mine."''',
        c('"Next time, send for me. I\'ll hold his hand, and you sing."', "together", flags=(DYING, HELD_HIS_HAND)),
        c('"You gave him the song. That\'s what he needed, not your hand."', "enough", flags=(DYING,))),
    a("together", '''{n}She stares at you.{/n} "You'd come. From whatever you were doing. To hold a stranger's hand while a succubus sings." {n}Something in her face gives way.{/n}
"Yes. All right. Next time. The Commander holds the hand and the demon sings." {n}She laughs, cracked.{/n} "It sounds like the start of one of your jokes. It isn't, is it? For once it isn't."''', c()),
    a("enough", '''"That's what the orderly said." {n}She looks down.{/n} "I want to believe it. I think I'll believe it more on the tenth one than on the first." {n}She takes a breath.{/n} "There'll be a tenth. There's a war. I'm the chaplain. You made me the chaplain." {n}No reproach in it. Only a fact she is learning to carry.{/n}''', c()),
], (CHAPLAIN, CENSER), delay=48, chapters=(5,))

hub(COMPLAINT, "A formal complaint", 3, '"I hear you\'ve been sent for."', [
    a("start", '''"By the Iomedaean chapter-master. He's written to you, as well. Did you read it?" {n}She doesn't wait.{/n} "It says a demon of lust has no business blessing the arms of the Inheritor's crusade, and that it is a scandal, and that the Commander's jest has gone too far."
{n}She holds herself very straight.{/n} "He's right. By every rule he knows, he's right. So I've come to resign. You appointed me out loud; you can dismiss me out loud. Say it and I'll hand back the censer."''',
        c('"Tell him you\'re the only chaplain who knows exactly what she\'s blessing them against."', "against",
          flags=(COMPLAINT, STAYS_CHAPLAIN)),
        c('"Hand it back, then. I\'ll find somebody who\'s less trouble."', "choice", flags=(COMPLAINT,))),
    a("against", '''{n}Her mouth falls open. Then she laughs, and it is not the startled laugh; it is something rougher and prouder.{/n}
"The only chaplain who knows exactly what she's blessing them against." {n}She says it again, slowly, to keep it.{/n} "I'm going to write that on the vestry door. He's going to see it every morning." {n}She hesitates.{/n} "You know he'll only write again."
"Let him," {n}you tell her.{/n} "I'll give him a seat in the front pew for your first sermon."''', c()),
    a("choice", '''{n}She stands there, holding the censer she brought to hand back.{/n}
"Less trouble." {n}She sets the censer down on your table, and then, slowly, picks it up again, and her smile has teeth in it.{/n} "You'll find somebody who's less use. Do you know what he's afraid of, your chapter-master? Not me. What I know about the men he blesses." {n}She tucks the censer under her arm.{/n} "I'm keeping it. The second company asked me to bless their swords before the march, and I said yes, and I don't go back on a yes. Tell him I'll pray for him. He'll hate that."''', c(flags=(STAYS_CHAPLAIN,))),
], (CHAPLAIN,), delay=48, chapters=(3, 5))


# --- The returned: counting ------------------------------------------------------------------------------------

hub(COUNTING, "The count", 3, '"How many days?"', [
    a("start", '''{n}She knows what you mean. She always knows. She holds up her hand and counts on it, although she doesn't need to.{/n}
"I've started counting again. Days since I ate. One more every morning." {n}She says it the way a sailor says how long since land.{/n} "Before, I counted the other way. Days since I fed. Now I count days since I was fed, which is different, because I didn't choose it. You chose it. I just swallowed."''',
        c("Continue", "you", requires=(FED_ON_YOU, SOSIEL_OFFERED)),
        c("Continue", "him", requires=(LANN_SAID,), forbids=(FED_ON_YOU,)),
        # Sol r3 (INT): Sosiel's offer and Lann's word are recalled only where those reactions were played.
        c("Continue", "you_alone", requires=(FED_ON_YOU,), forbids=(SOSIEL_OFFERED,)),
        c("Continue", "him_alone", forbids=(FED_ON_YOU, LANN_SAID))),
    a("you_alone", '''"And every day it's you I taste. Not a stranger. You." {n}She rubs her lips with the back of her hand, the gesture of a woman trying to wipe off a kiss, and failing.{/n}
"I keep thinking someone else should have offered. Anyone. It would be easier to want it from someone I didn't care about." {n}Her voice drops.{/n} "Isn't that monstrous? I'm grateful, and I'm already hungry for the same dish."''',
        c("Continue", "ask")),
    a("him_alone", '''"And every day I taste him. The cultist. He's in the east cells, still. He doesn't know his own name. I go and look at him, sometimes, through the grille. I don't know why." {n}She looks at you.{/n}
"Nobody has said a word to me about it. Not one of them. I think they're waiting to see what I do with it. So am I."''',
        c("Continue", "ask")),
    a("you", '''"And every day it's you I taste. Not a stranger. You." {n}She rubs her lips with the back of her hand, the gesture of a woman trying to wipe off a kiss, and failing.{/n}
"Sosiel came to me. He said if I ever need it again, I should come to him first; he has more to spare. He meant it. He's the kindest man in this army." {n}Her voice drops.{/n} "And I don't want his. I want yours. Isn't that monstrous? I've been given two gifts and I'm already choosing between them like dishes."''',
        c("Continue", "ask")),
    a("him", '''"And every day I taste him. The cultist. He's in the east cells, still. He doesn't know his own name. I go and look at him, sometimes, through the grille. I don't know why." {n}She looks at you.{/n}
"Lann says he'd have done the same, fed me a man so I'd live. He said he's not proud of thinking it. I think he's the most honest person in this army. And I think about the man in the east cell, and I'm not honest about how good he was."''',
        c("Continue", "ask")),
    a("ask", '''{n}She lets her hand fall.{/n} "You said..." {n}She glances at you, and away.{/n}''',
        c("Continue", "every", requires=(EVERY_TIME,)),
        c("Continue", "asked", forbids=(EVERY_TIME,))),
    a("every", '''"You said every time. If I die again, you'll do it again, every time. I believed you. That's the problem." {n}She laughs, shakily.{/n} "It means I'm not afraid of dying any more, and I should be. I should be afraid of everything. So I'm going to keep counting. Eleven. Twelve tomorrow. If I get to a hundred without wanting to die just to be fed, you can ask me whatever you like."''',
        c("[Let her count.]", flags=(COUNTING,))),
    a("asked", '''"You said only if I ask. I've thought about it every night. Whether I'd ask." {n}She holds your eyes.{/n} "I wouldn't. I've decided. If I die again, I stay dead, unless there's some reason in the world that isn't me being hungry. And I don't know of one yet." {n}A pause.{/n} "Ask me again at a hundred days. Maybe I'll know one then."''',
        c("[Let her count.]", flags=(COUNTING,))),
], (AFTERTASTE,), delay=48, chapters=(3, 5))


# --- The fallen: at the jeweller's arcade, before the arrangement ---------------------------------------------------------

tavern(SERGEANT, "A patrol sergeant", '"The third company is one man short."', [
    a("start", '''"Is it? How careless of them." {n}She is sitting with her boots on the table and a cup of wine from a bottle she has plainly stolen from the jeweller's back room, and she does not trouble to look innocent.{/n}
"You sent me away hungry, darling. I told you what I'd do." {n}She swirls the wine.{/n} "He was very sweet. He had a sweetheart in Nerosyan, and he told me about her the whole time. I let him."''',
        c("Continue", "choice")),
    a("choice", '''{n}She tips her head, watching you.{/n} "Well? This is where the Commander of the crusade draws a sword on me. I've been looking forward to it. You're so pretty when you're righteous."''',
        c('"He was one of mine. You don\'t get to do that in my city."', "mine", flags=(SERGEANT,)),
        c('[Sit down and take her cup] "Next time, you eat me. Not them."', "me", flags=(SERGEANT,))),
    a("mine", '''"Yours." {n}She laughs, delighted.{/n} "Everything is somebody's, darling. He was yours, and I'm hers, and you're..." {n}She leans in.{/n} "Well. That's what we're here to find out, isn't it."
"I'll be good in your city. For a while. Because it amuses me, and because you asked with that face. Don't mistake it for anything else."''', c()),
    a("me", '''{n}For one moment something crosses her face that is not a smile at all. Then it is gone.{/n}
"You'd do that. You'd put yourself on the menu to keep a sergeant's sweetheart from weeping." {n}She takes the cup back and drinks.{/n} "That's either the most mortal thing I've ever heard, or the stupidest. You were always wasting kindness on me."''', c()),
], (HUNGRY,), delay=24)

tavern(DAYBOOK, "The daybook", '"You kept something of hers?"', [
    a("start", '''"Hers?" {n}She laughs.{/n} "Mine. I'm not someone else, darling. I'm the same succubus with the same memories. I just stopped pretending I didn't like the taste." {n}She reaches into her bodice and takes out a small burnt thing: the charred corner of a clerk's daybook, the kind bought off a Drezen stationer.{/n}''',
        c("Continue", "book", requires=("arueshalae.treatment.rx_watch",)),
        c("Continue", "feather", forbids=("arueshalae.treatment.rx_watch",))),
    a("book", '"\'Watch people eat. Three times a day.\' Your little dare. I burned the book the night I left, page by page, in the Worldwound, and I read every page before it went in. All those careful notes about how mortals pass the bread." {n}She turns the charred corner over.{/n}\n"And I kept this bit back. To burn in front of you." {n}She holds it to the candle and lets it catch, and watches your face, not the flame, while it goes.{/n} "Don\'t look at me like that, as if I\'d lost something. I\'m the one who\'s finally eating."',
        c("Continue", "end")),
    a("feather", '''"No, you're right, it's not a book. It's nothing. A page of prayers to a goddess who lied to me." {n}She holds it to the candle, and lets it catch.{/n}
"I read them sometimes. To laugh. 'And what do you dream of?' She asked me that. As if a demon dreams. As if I'd ever want anything as soft as a dream when I can have what I want, when I want it."''',
        c("Continue", "end")),
    a("end", '''{n}She drops the last burning scrap into your cup and watches the ash go round.{/n} "Drink that. Then buy me another, and don't ask me anything else tonight. You have a way of asking things that makes me answer, and I don't like it." {n}A thin smile.{/n} "Ask me again and I'll find somebody less tedious to drink with."''',
        c("[Buy her another drink.]", flags=(DAYBOOK,))),
], (), delay=24)


# Q11: after the native Elysium ending the returned count of hungry days is not restaged.
for _scene in SCENES:
    if _scene["Id"] in (COUNTING, DYING) and ELYSIUM not in _scene["Forbids"]:
        _scene["Forbids"].append(ELYSIUM)


def integrate(payload):
    """Scenes only; keys bind on demand through trickster_world."""

"""Devarra's watchtower: the courtship around the "Clutch-mother" spine (devarra_trickster).

Every beat is physical on the Storyteller's hub in Drezen (Chapters 3 and 5). host_reason: he is her canon captive and
the one buyer of her tariff who lived (KTC_StorytellerIsBack/Cue_0006, Cue_0019); since the moult he is her messenger,
and for the climbs he is the Commander's guide up the ridge, blind and unafraid of the path. Her only native unit is a
hostile monster (WoundWormsLair_BlackDragon c540d81c, Factions/Mobs, no dialog), so she is never spawned: she speaks in
these scenes under her own name and portrait (E14f) while the Storyteller stands by. The two letters of the spine are the
route's whole letter budget (Chapter 3: 2, Chapter 5: 2), so nothing here is a letter. The one remote beat is the
Chapter 4 memory wrong_sky (PP7), kept on the voyage and told in person at the Abyss vigil.

Authored, and labelled as authored: the watchtower, its bones and its new grey roof; the tax clerk; her questions; the
demon nest; the bites. Her voice is built on her canon lines (StoryTellerAndDragonGoodEnter/Cue_0002 546738b4 "I do
love to play with my food"; BadEnter/Cue_0002 a6793a08 "little parasites"; DLC1 flavour "dragons have excellent
memories" 3b37a8b4). The tax clerk's opening line reuses the retired draft's best beat ("If you came about the tax, it
is eating the third paragraph."), now hers.

Moral weight stays on the spine's pivots (the clutch, the tithe, the terms, Directive 3). The choices here shape how she
reads the Commander, and one of them (claiming her) is answered the way she answers every attempt to own her.
"""
from story_format import c, n, scene
from storylines.devarra_trickster import (
    BITTEN, CLOSED, COMMITTED, COOK_GIVEN, COOK_REFUSED, ENDING_OWED, HUNGRY, HUNTING, HUNTS, KEPT_BACK, LEFT_HUNGRY, MARKED,
    RETURNED, RUTHLESS, SHAME_SOLD, STORY_SOLD, TESTED, UNKNOWN, WITHHELD, XANTHIR, FLATTERED, TRUE,
    FLOWN, PACT, COLLECTED,
    dv, nar, storyteller, teller)

# Option A ("She flies", 2026-10-01): she never died. Every line below that remembers a carcass, a moult, a new hide or the
# three days is a LEGACY line (a save that returned her through the retired moult device): its incoming choice Forbids
# FLOWN, and a flight-world sibling node (suffix _free) is reached by an appended choice that Requires FLOWN. Scenes whose
# whole premise is the moult Forbid FLOWN and have flight-world replacements with new ids. Ids, node order of existing
# nodes and choice positions are unchanged.

SCENES = []
T = "devarra.tower."
HEARD = T + "news_heard"
CLIMBED = T + "climbed"
QUESTIONED = T + "questioned"
TAXED = T + "taxed"
CLUTCH_SPOKEN = T + "clutch_spoken"
TROPHY = T + "trophy_kept"
BITTEN_ONCE = T + "first_bite"
SHE_SAYS = T + "what_she_says_heard"
NEXT_TOLD = T + "next_told"
BANE_SEEN = T + "bane_seen"
# Variants (read by later beats only; nothing gates on them).
APOLOGISED = T + "apologised"
BOASTED = T + "boasted"
WARNED = T + "warned"
LOVED_LIE = T + "answer_loved_lie"
STOLE_FIRST = T + "answer_stole_first"
JOKES_STOP = T + "answer_jokes_stop"
TAX_PAID = T + "tax_paid"
TAX_EXEMPT = T + "tax_levy"
TAX_EATEN = T + "tax_eaten"
LOOKED_AWAY = T + "looked_away"
WATCHED = T + "watched"
VAULT_OPENED = T + "vault_opened"
VAULT_REFUSED = T + "vault_refused"
CH3 = "devarra.chapter_three"               # Chapter03 etude 15e0048c (Playing; completed by ToNexus), bound in devarra_trickster
CLIMBED_CH3 = T + "climbed_before_the_abyss"   # she was back and the tower climbed before the march into the Wound
# PP7 (Chapter 4): the wrong sky, a story kept back for her on the voyage out of Alushinyrra (wrong_sky; read by after_the_abyss).
VOYAGE = "devarra.voyage_begun"             # StartedDialogs AirAdventures_BookEvent a07f6d1f (every captain), bound in integrate
VOYAGE_SEEN = VOYAGE + ".latched"           # its latch: the delay runs from the hour the voyage began (Sol PP7 r1)
SKY = T + "wrong_sky.kept"
SKY_FEAR = T + "wrong_sky.fear"
SKY_VIEW = T + "wrong_sky.view"
SKY_SPENT = T + "wrong_sky.spent"
SKY_CHOICES = (
    c("[Keep the fall for her: the moment the deck dropped away under you, and what your stomach did.]", "fear"),
    c("[Keep the view for her: the whole wrong sky from the rail, every colour of it, the way a dragon would want it.]", "view"),
    c("[Keep nothing back. Tell it to the sailor on watch, the same night, while it is fresh.]", "spent"),
)


def hub(id, title, entry, nodes, requires, forbids=(), delay=0, **extra):
    storyteller(id, title, entry, nodes, requires=requires, forbids=(CLOSED, *forbids), delay=delay, into=SCENES, **extra)


# --- 1. What climbed out (after the return, before the test) --------------------------------------------------------

hub(T + "what_climbed_out", "The sound she makes now", '"You heard her come back. What did she sound like?"', [
    teller("start", '''"I heard her before anyone saw her. Blind men hear dragons the way sighted men see weather." {n}He turns his cup a quarter turn on the table, then another.{/n}
"She used to sound like a forge. Bellows and iron. Now she sounds like paper. Dry, new, rustling when she turns her head. She is lighter on the ground; the stones do not complain under her the way they did in the lair. And she breathes differently. Shorter. Hungrier."''',
        c('"Is she still the same dragon?"', "same"),
        c('"Is she dangerous to Drezen?"', "danger"),
        c('"Does she remember you?"', "remember")),
    teller("same", '''"The dragon who held me in the lair would have eaten you for the story you told about her. That dragon is lying in pieces on a floor somewhere, emptied out like a glove." {n}He considers.{/n} "What came out of the glove listens more. She stopped outside the east gate last night and listened to the city for an hour. I have never heard her listen to anything that was not a story. I cannot tell you what she was counting. I did not ask. I would rather she told me than I guessed."''',
        c("Continue", "end")),
    teller("danger", '''"Two men of the north watch went up the ridge last night with torches, on a wager, to see her." {n}He does not smile.{/n} "She sent their helmets down to the north gate this morning, and nothing else. I did not ask her why. She told me anyway: 'The city may keep its walls. The ridge is mine. Anything that climbs it without being sent for is food.' I am told the watch has stopped making wagers."''',
        c("Continue", "end")),
    teller("remember", '''"She remembers me." {n}His fingers stop on the cup.{/n} "She said my name when she passed me on the road, as though she were reading it off a list. Then she said, 'Not yet, old man. You still owe me the end of a story.' I had forgotten I had not finished it. She had not."''',
        c("Continue", "end")),
    teller("end", '''"She will send for you when she has decided what you are for. Until then, I would not go up the ridge uninvited." {n}He lifts his blind face toward you.{/n} "I say that as a man who once did."''',
        c('"Noted."', flags=(HEARD,))),
], requires=("trickster.ever", RETURNED), forbids=(HEARD, FLOWN), delay=12)


hub(T + "what_came_back", "The sound she makes now", '"You heard her come in over the city. What did she sound like?"', [
    teller("start", '''"I heard her before anyone saw her. Blind men hear dragons the way sighted men see weather." {n}He turns his cup a quarter turn on the table, then another.{/n}
"In the lair she sounded like a forge: bellows and iron. Now there is a catch in the bellows. One wing does not close clean; it whistles on the downstroke, where your people put holes in it. She lands heavy on that side. And she breathes shorter than she did. Hungrier."''',
        c('"Is she still the same dragon?"', "same"),
        c('"Is she dangerous to Drezen?"', "danger"),
        c('"Does she remember you?"', "remember")),
    teller("same", '''"The dragon who held me in the lair went where a stone told her and fought what it pointed at." {n}He considers.{/n} "This one stopped outside the east gate last night and listened to the city for an hour. I have never heard her listen to anything that was not a story. I cannot tell you what she was counting. I did not ask. I would rather she told me than I guessed."''',
        c("Continue", "end")),
    teller("danger", '''"Two men of the north watch went up the ridge last night with torches, on a wager, to see her." {n}He does not smile.{/n} "She sent their helmets down to the north gate this morning, and nothing else. I did not ask her why. She told me anyway: 'The city may keep its walls. The ridge is mine. Anything that climbs it without being sent for is food.' I am told the watch has stopped making wagers."''',
        c("Continue", "end")),
    teller("remember", '''"She remembers me." {n}His fingers stop on the cup.{/n} "She said my name when she passed me on the road, as though she were reading it off a list. Then she said, 'Not yet, old man. You still owe me the end of a story.' I had forgotten I had not finished it. She had not."''',
        c("Continue", "end")),
    teller("end", '''"She will send for you when she has decided what you are for. Until then, I would not go up the ridge uninvited." {n}He lifts his blind face toward you.{/n} "I say that as a man who once did."''',
        c('"Noted."', flags=(HEARD,))),
], requires=("trickster.ever", RETURNED, FLOWN), forbids=(HEARD,), delay=12)


# --- 2. The first climb (after the test): the tower, face to face --------------------------------------------------

hub(T + "first_climb", "The watchtower", '"She\'s sent for me, hasn\'t she?"', [
    teller("path", '''"She has. Come; I know the path. I have walked it four times now, and the fourth time she did not bother to look up." {n}He takes his stick and his useless lantern, and leads you out through the north gate and up the ridge in the last of the light, placing his feet without hesitation on stones you can barely see.{/n}
"One piece of advice. She does not like to be looked at while she is eating. She does not like to be looked away from, either. Nobody has yet found the angle between."''',
        c("Continue", "tower", forbids=(FLOWN,)),
        c("Continue", "tower_free", requires=(FLOWN,))),
    nar("tower", '''{n}The watchtower has lost its upper floor to some older war, and she has made the ruin into a nest: the broken stair is a ramp, the arrow slits are stuffed with fleeces, and a grey wing is folded over the top like a roof. The floor is scattered with bones, sorted by size, smallest at the door.{/n}
{n}She is lying around the base of the stair with her head on the sill. In the dusk her new hide looks like ash that has not yet decided to be cold. There is a pale seam low on her flank, under the wing, where the killing blow went in; the moult grew over it and did not bother to hide it.{/n}''',
        c("Continue", "look")),
    dv("look", '''"You climb loudly." {n}She does not lift her head.{/n} "The old man climbs like a cat. You climb like a crusader, as if the mountain owed you the path."
{n}One eye opens and fixes on you. Up close, it is the size of a shield, and the colour of the inside of a furnace.{/n} "Sit. Not there; that is a bone I have not finished. There."''',
        c("[Sit where she says.]", "dying", forbids=(FLOWN,)),
        c("[Sit where you like.]", "sit_anyway"),
        c("[Sit where she says.]", "flying", requires=(FLOWN,))),
    dv("sit_anyway", '''{n}You sit on the bone. It cracks.{/n} "Hm." {n}She watches you, and something at the corner of her mouth moves that might, in a smaller animal, be amusement.{/n} "The little parasite has manners of its own. Keep them. I will enjoy taking them away later."''',
       c("Continue", "dying", forbids=(FLOWN,)),
       c("Continue", "flying", requires=(FLOWN,))),
    dv("dying", '''"Do you want to know what it was like?" {n}She does not wait for an answer.{/n} "Dark. Not the dark of a cave; I have slept in caves for three hundred years. The dark of a thing with nothing in it. And in that dark I could hear a story. About me. It was the only sound there was, so I listened to it to the end, the way I have listened to every story anyone ever told in my lair to buy a life."
"And then I was hungry. The dead are not hungry. So I knew the new hide had taken, because nobody had cut me open to see what was under the old one; and I knew the story had been good enough, and what I owed the one who told it. I got up, and I did not eat you."''',
       c('"I didn\'t know it would work."', "didnt_know"),
       c('"I\'m sorry it was you."', "sorry", flags=(APOLOGISED,)),
       c('"It was a good joke. Admit it."', "good_joke", flags=(BOASTED,))),
    dv("didnt_know", '''"No. You did not." {n}She sounds pleased, as if you had confessed to a vice she approved of.{/n} "You bet on it anyway, on a guess, with other people's money and other people's swords, over a thing that was dead or nearly. That is the thing about you, crusader. There is a mean streak beneath the laughter. I have been wondering how long you would keep making it apologise."''',
       c("Continue", "claim")),
    dv("sorry", '''{n}The eye narrows to a slit of orange.{/n} "Do not. A thing that apologises for what it did to me is asking me to forgive it, and I have not decided whether to eat it." {n}She breathes out; the fleeces in the arrow slits stir.{/n} "Keep your sorry. Give it to someone who needs it. I would rather have the part of you that told the story."''',
       c("Continue", "claim")),
    dv("good_joke", '''{n}For a heartbeat the whole tower is silent. Then she laughs, a sound like a kiln door opening, and the fleeces blow out of two of the arrow slits and go tumbling down the ridge.{/n}
"It was a very good joke. It was cruel, and it was clever, and it was about me." {n}She shows you all of her teeth, which is not the same as smiling.{/n} "Those are the only three things I have ever liked in a story."''',
       c("Continue", "claim")),
    dv("claim", '''"Now. The garrison left this tower. The city says it still belongs to them. Your crusade says everything within sight of Drezen belongs to you." {n}Her claws flex against the stone, and the stone gives a little.{/n} "Tell me who this tower belongs to."''',
       c('"It\'s yours."', "hers"),
       c('"Everything here is under my protection. You included."', "protect", flags=(WARNED,)),
       c('"It belongs to whoever can hold it."', "hold")),
    dv("hers", '''"Yes." {n}She says it the way a judge passes a sentence.{/n} "Good. You can be taught. So here is how it will be, and I am not asking. Your city is safe while it stays off my mountain. You are safe while you amuse me. Either of those can end the day I am bored."''',
       c("Continue", "leave")),
    nar("protect", '''{n}She moves faster than anything that size should be able to move. One wingbeat, not even a full one, and you are on your back among the small bones with the breath knocked out of you and the grey wing a hand's breadth from your face.{/n}''',
        c("Continue", "protect_2", forbids=(FLOWN,)),
        c("Continue", "protect_2_free", requires=(FLOWN,))),
    dv("protect_2", '''"Once," {n}she says, quite gently.{/n} "I will let you say that once. You kept the knives off my carcass and paid my tariff, and I paid out. That does not make you my keeper. It makes you the one I will eat last."
{n}The wing lifts. The Storyteller, at the door, has not moved at all.{/n}''',
       c("Continue", "leave")),
    dv("hold", '''"Whoever can hold it." {n}She tastes the words.{/n} "A dragon's answer, from a thing with soft hands. I will hold it, then, and you will watch me hold it, and we will both know what you meant."''',
       c("Continue", "leave")),
    dv("leave", '''"Go down now. Come back when I send for you." {n}She breathes out as you turn, once, not at you but past you, and the stone of the doorway beside your head goes red and runs. Your cloak is smoking at the shoulder. The heat stays in your cheek all the way down the ridge, and for a week afterwards the skin there peels.{/n}
"So that your sentries know where you have been," {n}she says behind you,{/n} "and that you came back down because I allowed it."''',
       c("[Go down the mountain.]", flags=(CLIMBED,), forbids=(CH3,)),
       c("[Go down the mountain.]", flags=(CLIMBED, CLIMBED_CH3), requires=(CH3,))),
    nar("tower_free", '''{n}The watchtower has lost its upper floor to some older war, and she has made the ruin into a nest: the broken stair is a ramp, the arrow slits are stuffed with fleeces, and a grey wing is folded over the top like a roof. The floor is scattered with bones, sorted by size, smallest at the door.{/n}
{n}She is lying around the base of the stair with her head on the sill. Up close the lair is still on her: the web of one wing knotted with scar where your blades went through it, and low on her flank, under the wing, a long pale seam where the fight opened her to the ribs and she flew with it open. It has closed. It has not bothered to close neatly.{/n}''',
        c("Continue", "look")),
    dv("flying", '''"Do you want to know what it was like?" {n}She does not wait for an answer.{/n} "Xanthir's charm calls in the bones of the head. Not loud. Like your own name said behind you in a market, again and again, by a voice you have obeyed all season. I lay on a mountain with my side open and the blood going cold on the rocks, and it called, and called, and called, and every time it called I saw the fists."
"Then it stopped. Either you had put your hand in the stone's mouth, or the fists had closed, and I lay there until morning not knowing which. That was the worst night I have had in three hundred years, and you gave it to me."''',
       c('"I didn\'t know it would work."', "didnt_know_free"),
       c('"I\'m sorry it was you."', "sorry", flags=(APOLOGISED,)),
       c('"It was a good joke. Admit it."', "good_joke", flags=(BOASTED,))),
    dv("didnt_know_free", '''"No. You did not." {n}She sounds pleased, as if you had confessed to a vice she approved of.{/n} "You bet on it anyway: on a guess about a stone you had never seen, with my clutch for the stake and your dwarf's fee for the ante. You wagered my clutch, crusader. Do not pretend the laugh made it kind."''',
       c("Continue", "claim")),
    dv("protect_2_free", '''"Once," {n}she says, quite gently.{/n} "I will let you say that once. You walked into Xanthir's house for me and paid my tariff in the same breath, and I paid out. That does not make you my keeper. It makes you the one I will eat last."
{n}The wing lifts. The Storyteller, at the door, has not moved at all.{/n}''',
       c("Continue", "leave")),
], requires=("trickster.ever", RETURNED, TESTED), forbids=(CLIMBED,), delay=24)


# --- 3. Her questions (after the first climb) -----------------------------------------------------------------------

hub(T + "her_questions", "Three questions for a liar", '"Has she sent anything down?"', [
    teller("start", '''"Three questions." {n}He sets them down between you on the table as if they were coins.{/n} "She says a thing that bought her terms with a story owes her an account of itself, and that she will know if you lie to her again, because she has tasted your lies and knows what they are made of."
"I am to carry the answers up word for word. I will. I would add, as the carrier, that I am curious too."''',
        c("Continue", "first")),
    teller("first", '''"The first: what did you steal first? Not the biggest thing. The first."''',
        c('"A boat, at the Kenabres river, the night the city fell. I never gave it back."', "first_boat", flags=(STOLE_FIRST,)),
        c('"A name. The one I use. It belonged to someone else before it was mine."', "first_name", flags=(STOLE_FIRST,)),
        c('"Tell her I don\'t remember."', "first_none")),
    teller("first_boat", '''"A boat." {n}He smiles.{/n} "A stolen boat, off a burning city. I will carry those words exactly. What she makes of them is her business."''',
        c("Continue", "second")),
    teller("first_name", '''{n}The smile goes, for a moment.{/n} "A name. Yes. I will carry that one carefully. She keeps her own name close enough that I have never heard her say it twice the same way."''',
        c("Continue", "second")),
    teller("first_none", '''"I will tell her." {n}He turns his cup.{/n} "She will probably call it a lie. I am to carry your answer, not defend it."''',
        c("Continue", "second")),
    teller("second", '''"The second: who have you lied to that you still love?"''',
        c('"Everyone I love. That\'s how I know I love them. I bother to lie."', "second_all", flags=(LOVED_LIE,)),
        c('"You. I paid for you to get up, before anyone knew you could."', "second_her", flags=(LOVED_LIE,), forbids=(FLOWN,)),
        c('"No one. I don\'t lie to people I love."', "second_none"),
        c('''"You. I told you I could stop Xanthir's stone. I had never even seen it."''', "second_her", flags=(LOVED_LIE,),
          requires=(FLOWN,))),
    teller("second_all", '''"Everyone." {n}He nods slowly.{/n} "I will repeat it exactly. Including the way your voice went on the last word. She will ask, and I do not lie to her; it is bad for my health."''',
        c("Continue", "third")),
    teller("second_her", '''{n}He does not answer at once.{/n} "Commander. You understand that I am to carry this up word for word, to a woundwyrm, who has three hundred years of experience in telling what people mean from how they smell when they say it."
"Very well. It is your neck. Or your forearm."''',
        c("Continue", "third")),
    teller("second_none", '''"No one." {n}He writes nothing down, but you have the sense that he is remembering the exact shape of it.{/n} "She will call that a lie. I cannot promise she will believe the steadiness either."''',
        c("Continue", "third")),
    teller("third", '''"The last: what will you do when the jokes stop working?"''',
        c('"Keep telling them. Somebody has to."', "third_keep", flags=(JOKES_STOP,)),
        c('"Find out what I am without them."', "third_find", flags=(JOKES_STOP,), forbids=(FLOWN,)),
        c('"They won\'t stop."', "third_wont"),
        c('"Find out what I am without them."', "third_find_free", flags=(JOKES_STOP,), requires=(FLOWN,))),
    teller("third_keep", '''"Keep telling them." {n}He turns his cup the last quarter turn, back to where it started.{/n} "She asked the question. She can judge the answer. Dragons go on sitting on gold long after it has stopped being useful; she may think that a compliment, or she may think it a confession."''',
        c("Continue", "end")),
    teller("third_find", '''"Find out what you are." {n}He is quiet.{/n} "She had three days in the dark in a dead body to find out that. I have not asked her what she found. I will carry your answer and not my opinion."''',
        c("Continue", "end")),
    teller("third_wont", '''"I will tell her." {n}He considers you over his cup.{/n} "She likes arrogance. She finds it seasons the meat."''',
        c("Continue", "end")),
    teller("end", '''{n}He climbs the ridge at dusk and comes back after dark, and sits down across from you without a word for a while.{/n}
"She listened to all three without interrupting. Then she said, 'The thing is more interesting than I thought, and less honest than it thinks.' Then she took my lantern out of my hand, and kept it, and told me to find my own way down." {n}He turns his useless eyes toward the window.{/n} "I know how to find a path in the dark, Commander. It was a long way down."''',
        c('"I will get you another lantern."', flags=(QUESTIONED,))),
    teller("third_find_free", '''"Find out what you are." {n}He is quiet.{/n} "She lay a night on a mountain with her side open, listening to Xanthir's charm call her, to find that out about herself. I have not asked her what she found. I will carry your answer and not my opinion."''',
        c("Continue", "end")),
], requires=(CLIMBED,), forbids=(QUESTIONED,), delay=24)


# --- 4. The tax (after the first climb): the Crusade's clerk goes up the ridge --------------------------------------

hub(T + "the_tax", "The assessment", '"Why is there a clerk crying in your corridor?"', [
    teller("start", '''"Because the Treasury sent him to assess the watchtower on the north ridge for its value to the crusade, in anticipation of its reoccupation. He is to go up and measure it." {n}The Storyteller folds his hands.{/n} "He came to me because he heard I know the path. I do. I also know what is at the end of it. He has been crying since I told him, but he insists on going, because his superior insists on the assessment, and he is more afraid of his superior."
"I suggest, Commander, that you go with him. For the good of the Treasury."''',
        c("Continue", "climb")),
    nar("climb", '''{n}The clerk is a thin young man named Oswin with ink up to both wrists and a satchel full of forms. He climbs behind you with the fixed stare of the condemned. At the top he stops dead in the doorway and holds up the Treasury's proclamation, rolled and sealed, in front of him like a holy symbol.{/n}
{n}Devarra looks at the proclamation. Then she leans down, takes it very delicately between her front teeth, and begins, slowly and with every sign of enjoyment, to eat it from the bottom up.{/n}''',
        c("Continue", "tax")),
    dv("tax", '''"If you came about the tax," {n}she says around the parchment,{/n} "it is eating the third paragraph."''',
        c("Continue", "clerk")),
    n("clerk", "Oswin", '''{n}The clerk looks at the dragon, and then at you, and then, with the courage of a man who has already written his own will in the corridor, back at the dragon.{/n} "I came about the tower, madam."
{n}He turns to you.{/n} "And you, Commander, I take it, are the more expensive problem."''',
        c("Continue", "choose")),
    dv("choose", '''{n}She swallows the last of the proclamation, seal and all, and looks at you with great interest.{/n} "Well, crusader? He is your little parasite, not mine. Tell him what my tower is worth."''',
        c('[Pay the assessment from the war chest] "Charge the crusade. Full value. She\'s a garrison."', "paid",
          crusade=("Finances", -100), flags=(TAXED, TAX_PAID)),
        c('[Tell him who she is] "She isn\'t the tower\'s tenant, Oswin. She\'s the tax collector. Every ox on the east road is the crusade\'s levy, and she\'s collecting."', "levy",
          flags=(TAXED, TAX_EXEMPT)),
        c('"Let her finish the forms. All of them."', "eaten", flags=(TAXED, TAX_EATEN))),
    dv("paid", '''"A garrison." {n}She turns the word over like a coin.{/n} "Paid by the crusade. To sit on a mountain and eat whatever comes up it." {n}The eye swings to Oswin, who writes very fast.{/n} "Put down that the garrison is excellent value and has never lost a post."''',
       c("Continue", "end", forbids=(FLOWN,)),
       c("Continue", "end_free", requires=(FLOWN,))),
    dv("levy", '''"The tax collector." {n}She stops chewing. Then the laugh comes, the kiln door flung wide, and the tower shakes with it.{/n} "Yes. Every ox on the east road, collected in full, on the crusade's behalf. I am the most efficient officer your Treasury has ever had."
{n}Her eye swings to Oswin.{/n} "Go down and tell your superior that the assessment is complete, and that the collector will be calling on him next. Personally." {n}Oswin goes down the ridge considerably faster than he came up it.{/n}''',
       c("Continue", "end", forbids=(FLOWN,)),
       c("Continue", "end_free", requires=(FLOWN,))),
    nar("eaten", '''{n}Oswin, to his eternal credit, opens the satchel himself. She eats the forms one at a time, in order, with great ceremony: the assessment, the schedule of improvements, the notice of reoccupation, the receipt for the notice. She saves the blank requisitions for last and eats those as dessert.{/n}
{n}When the satchel is empty she studies Oswin the way she studied the proclamation. Then she breathes on him, very gently, just enough to dry the ink on his wrists.{/n}''',
        c("Continue", "end", forbids=(FLOWN,)),
        c("Continue", "end_free", requires=(FLOWN,))),
    teller("end", '''{n}At the foot of the ridge, the Storyteller is waiting with his lantern.{/n} "He is alive? Good. The Treasury will call it a successful assessment. This clerk survived. His superior should not take that for an invitation." {n}He pats Oswin's shoulder as the young man goes past, shaking.{/n} "She will be telling this one to anything foolish enough to climb the ridge."''',
        c('''"Let the Treasury hear about it."''')),
    teller("end_free", '''{n}At the foot of the ridge, the Storyteller is waiting with his lantern.{/n} "He is alive? Good. The Treasury will call it a successful assessment. This clerk survived. His superior should not take that for an invitation." {n}He pats Oswin's shoulder as the young man goes past, shaking.{/n} "She will be telling this one to anything foolish enough to climb the ridge."''',
        c('''"Let the Treasury hear about it."''')),
], requires=(CLIMBED,), forbids=(TAXED,), delay=48)


# --- 5. The clutch (after the first climb): the one attachment she has ------------------------------------------------

hub(T + "the_clutch", "What she wants from you", '"She asked about the eggs again, didn\'t she?"', [
    teller("start", '''"She never stops asking about the eggs. She asked about them this morning, and when I said I had nothing new, she asked me what I would have said if I had." {n}He rubs his eyes with thumb and finger.{/n} "She wants you up the ridge. Tonight. She said to say it is not about the tower."''',
        c("Continue", "omelet_given", requires=(COOK_GIVEN,)),
        c("Continue", "omelet_refused", requires=(COOK_REFUSED,)),
        c("Continue", "druids_hunting", requires=(HUNTING,)),
        c("Continue", "withheld", requires=(WITHHELD,)),
        c("Continue", "xanthir", requires=(XANTHIR,)),
        c("Continue", "marked", requires=(MARKED,)),
        c("Continue", "unknown", requires=(UNKNOWN,)),
        c("Continue", "unknown", forbids=(COOK_GIVEN, COOK_REFUSED, HUNTING, WITHHELD, XANTHIR, MARKED, UNKNOWN, COLLECTED)),
        c("Continue", "collected", requires=(COLLECTED,))),

    # Omelet, the cook given.
    dv("omelet_given", '''{n}She is lying with her chin on the sill, watching the citadel kitchens' chimneys smoke.{/n} "I was quick with him. I said I would be." {n}Her eye turns to you.{/n} "He wept. He said he did not know what the eggs were when he salted them. That he had been told they were a gift. I believed him. I ate him anyway, because you gave him to me, and because a thing that cooks a mother's children should know, at the end, what it is to be food."''',
       c("Continue", "omelet_given_2")),
    dv("omelet_given_2", '''"Now. What was he to you? A name on a door? A man you passed in a corridor?" {n}She waits.{/n} "I want to know what you paid, crusader. I want to know whether it cost you anything at all."''',
       c('"Nothing. He was a cook. You were owed."', "given_nothing"),
       c('"More than I thought it would."', "given_something")),
    dv("given_nothing", '''"Nothing." {n}She breathes out, long and slow, and the watchtower fills with the smell of the forge.{/n} "Good. Then it was a gift, not a sacrifice. Gifts are better. You do not have to thank anyone for a sacrifice, and I do not intend to thank you for anything, ever."''',
       c("Continue", "end")),
    dv("given_something", '''{n}Smoke threads out of her nostrils and up into the rafters.{/n} "More than you thought. Yes. I could taste that on him, a little. That you had hesitated." {n}Her tongue flickers once, testing the air between you.{/n} "Keep the hesitation, crusader. Never let it stop you. But keep it. It is the only thing in you that tastes of anything but ambition."''',
       c("Continue", "end")),

    # Omelet, the cook refused.
    dv("omelet_refused", '''"I have been patient with your city." {n}She has not moved from the sill in what looks like days. Below, Drezen glows.{/n} "Every night I lie here and look at it. The cook. The quartermaster who bought the eggs. The soldiers who ate them standing up, in the rain, because they were starving and it was hot food. They were starving. You said so. I believe you."
"Tell me one thing, and tell me true. Did you eat any?"''',
       c('"Yes. I was hungry too."', "ate_yes"),
       c('"No."', "ate_no")),
    dv("ate_yes", '''{n}Her jaws open beside your face. She draws a long breath through her teeth.{/n} "You too. Hungry little crusader." {n}Her tongue touches your cheek; then she pushes you down onto the stair with her snout.{/n} "Tell me how you ate them. Look at me while you do it."''',
       c("[Tell her.]", "ate_yes_told")),
    nar("ate_yes_told", '''{n}You give her the account from the stair. Each time your eyes drop, her claw strikes the stone beside your boot. She makes you repeat the part about the shells. Below the ridge, the north watch changes; nobody comes up.{/n}''',
        c("Continue", "ate_yes_end")),
    dv("ate_yes_end", '''"Herbs." {n}She scrapes the stair beside you, leaving a deep white gouge.{/n} "I shall smell them every time you climb. You saved your cook. Do not mistake that for saving yourself."''',
       c("Continue", "end")),
    dv("ate_no", '''"Then you fed them to others." {n}Her snout drives you back against the stair. She looks past you toward the kitchens.{/n} "You stand between me and the cook. I can wait until you move. I can enjoy what you bring me while I wait."''',
       c("Continue", "end")),

    # The druids: she is hunting them.
    dv("druids_hunting", '''{n}She is thinner. There are burrs in the joints of her wings, and a long, clean cut along one foreleg that has not been made by any weapon you know.{/n} "I found their trail again. Three rivers east. I followed it to a hill with a white stone on the top, and on the white stone was one piece of eggshell, and on the eggshell was scratched a word in Draconic." {n}Her eye burns.{/n} "The word was 'safe'. Whoever scratched it knew I would find it. Whoever scratched it has claws."''',
       c("Continue", "druids_hunting_2")),
    dv("druids_hunting_2", '''"Someone scratched that word into the shell. With a claw. And the trail smelled of gold." {n}She lowers her head until her eye is level with yours.{/n} "What did you give my children to?"''',
       c('"I don\'t know. I thought they were druids."', "hunting_dunno"),
       c('"Something that won\'t eat them. That\'s all I know."', "hunting_safe")),
    dv("hunting_dunno", '''"You thought." {n}The word comes out of her like a cinder.{/n} "Well. That is how children are always lost. Someone thought." {n}She lifts her head.{/n} "I will find out what they are. And then I will find out whether 'safe' was a promise or a boast. Go home. I have a hill to go back to."''',
       c("Continue", "end")),
    dv("hunting_safe", '''{n}She lays her chin back on the sill.{/n} "Something that will not eat them." {n}She looks east.{/n} "There are not so many things in the world of which that is true. I am not one of them, crusader. I would not eat my own. But I would not keep them from being eaten by my own, either. That is what I am." {n}She closes her eyes.{/n} "Perhaps they are safer. Do not tell me so again. I will hear it in the dark."''',
       c("Continue", "end")),

    # The clutch withheld (the druids or the vault).
    dv("withheld", '''"You kept them from me." {n}She is lying curled so tightly around the broken stair that you have to climb over her tail to get in.{/n} "You said it to my face, and I let you live. I have thought about that every night since. I have decided you were telling the truth about them, and I have decided that I hate you for it."
"So. You will tell me about them instead. Are they warm? Are they eating? Does anyone sing to them? I sang to them, in the lair. The old man heard me. Ask him."''',
       c("Continue", "withheld_vault", requires=("eggs.project",), forbids=("eggs.druids", "eggs.omelet", "eggs.destroyed")),
       c("Continue", "withheld_told", requires=("eggs.druids",)),
       c("Continue", "withheld_told", forbids=("eggs.project", "eggs.druids")),
       # PP7 (Sol INT): the vault's project finished after the promise; the native outcome comes first.
       c("Continue", "withheld_spent", requires=("eggs.project", "eggs.omelet"), forbids=("eggs.druids",)),
       c("Continue", "withheld_spent", requires=("eggs.project", "eggs.destroyed"), forbids=("eggs.druids", "eggs.omelet"))),
    dv("withheld_told", '''{n}So you tell her what little you are sure of, and nothing you are not. She listens as if every word were a piece of meat, weighing each one before she swallows it.{/n}
"Careful," {n}she repeats.{/n} "Good. Careful is good." {n}She is quiet.{/n} "I will not ask you again for a while. It is too expensive, asking."''',
       c("Continue", "end")),
    dv("withheld_vault", '''"They are in your vault. I lie at the wall every night and listen to them. They are growing. I can hear the difference." {n}Her claws scrape the stone.{/n} "Let me in. Once. Under your guard, with your spears at my throat, with whatever you like. I want to put my face against the shells and let them hear that I am still here."''',
       c('[Let her in, once, under guard] "Tonight. After the city sleeps. My guards, my terms."', "vault_yes", flags=(VAULT_OPENED,)),
       c('"No. Not while they\'re Drezen\'s."', "vault_no", flags=(VAULT_REFUSED,))),
    nar("vault_yes", '''{n}She comes down the ridge at the dead hour, grey against a grey sky, and folds herself through the old siege breach in the vault wall with the care of something ten times smaller. Your guards stand with their spears levelled and their faces white. She does not look at them once.{/n}
{n}She lies down among the eggs and puts her face against them, one after another, and makes a sound too low to hear, that you feel in the shells under your hand and in your back teeth. The guards at the door tighten their grip on their spears and do not know why.{/n}''',
        c("Continue", "vault_yes_2")),
    dv("vault_yes_2", '''{n}At dawn she gets up and leaves the way she came. At the breach she stops.{/n} "You let a woundwyrm into your vault, crusader, and the eggs are all still there." {n}It is almost a question.{/n} "Remember that I could have taken them. Remember that I did not. We will both remember it, and it will be the only kindness either of us ever does the other. Do not spend it."''',
       c("Continue", "end")),
    dv("withheld_spent", '''"You kept them from me, in your vault. I lay at the wall every night and listened to them grow." {n}Her claws are still on the stone.{/n} "Then one night there was nothing to listen to. I know what was done to them. I could smell it from the ridge."
{n}She does not raise her voice. The fleeces in the arrow slits stir anyway.{/n} "You told me they would be warm, crusader. Go down the mountain before I decide what that was worth, and do not come up it again until I send."''',
       c("Continue", "end")),
    dv("vault_no", '''"Drezen's." {n}She says it very softly.{/n} "They are not Drezen's. They are not yours. They are mine, and you are keeping them, and you are keeping them well, and that is the only reason your city is still standing." {n}She turns her head away.{/n} "Say no to me again, crusader, when you are sure. I will still be listening at your wall."''',
       c("Continue", "end")),

    # Destroyed: she went for Xanthir's students.
    dv("xanthir", '''{n}Something has been dropped in the doorway of the tower for you: a satchel, scorched at one end, full of wax tablets covered in close, careful notes about golem obedience. One of the tablets is still warm.{/n}
"His students," {n}she says from the dark.{/n} "Two of them. There are more. You told me they still breathe. Now there are two fewer who do." {n}Her eye opens.{/n} "Read the tablets. They were writing down how to make the next golems obey better. They were proud of the chamber where my eggs were. They had drawn it."''',
       c('"Burn them."', "xanthir_burn"),
       c('"I\'ll keep them. The crusade can use this."', "xanthir_keep")),
    dv("xanthir_burn", '''{n}She breathes on the satchel without lifting her head. It goes up white. The tablets run like tallow.{/n} "Good. Now there is nothing left of the chamber except what is in my head, and yours." {n}She watches the fire.{/n} "I like you better when you are wasteful, crusader. It suits you."''',
       c("Continue", "end")),
    dv("xanthir_keep", '''"Use it." {n}She turns the answer over, and you with it.{/n} "Yes. That is what your kind does. You take the teeth out of a thing and wear them." {n}She does not sound angry. She sounds like someone taking a note.{/n} "Wear them, then. But when you build a golem out of those tablets, and you will, do not let me see it. I have seen enough golems."''',
       c("Continue", "end")),

    # Destroyed and watched: she makes the Commander watch the next thing.
    dv("marked", '''"I have picked it." {n}She is already standing when you reach the top, her wings half open, the whole tower creaking under her.{/n} "The next thing you will watch. Get on." {n}She lowers one shoulder.{/n} "Do not look like that. I will not drop you. If I wanted you dead I would not waste a flight on it."''',
       c("[Climb onto her shoulder.]", "flight")),
    nar("flight", '''{n}She flies north, low, fast, with the ridge dropping away beneath you and the cold tearing at your eyes, until the ground under you turns the colour of old meat and you smell the Worldwound.{/n}
{n}There is a hollow in a burned hillside, and in the hollow a vrock brood: a nest of greasy grey eggs as big as barrels, humming. Three vrocks are guarding it. They look up as her shadow crosses them.{/n}''',
        c("Continue", "nest")),
    dv("nest", '''"Watch," {n}she says.{/n} "You watched once. Watch again."''',
        c("[Watch.]", "watch", flags=(WATCHED,)),
        c("[Look away.]", "look_away", flags=(LOOKED_AWAY,))),
    nar("watch", '''{n}You watch. She crushes one vrock beneath her claw and tears the other two from the air, and then she stands over the nest, and she does not breathe fire on it at once. She looks at the eggs first, head low, exactly as the golems stood over hers.{/n}
{n}Then she burns them. It takes a long time. She watches every moment of it, and so do you.{/n}''',
        c("Continue", "after_nest")),
    nar("look_away", '''{n}You look away, at the horizon, at the sky, at anything. Behind you there is shrieking, and then there is fire, and then there is the smell, and then there is only the sound of something burning very thoroughly.{/n}
{n}When you look back she is watching you, not the ashes.{/n}''',
        c("Continue", "after_nest")),
    dv("after_nest", '''"There." {n}She studies your face before lowering her shoulder.{/n} "Did you want to look away? Remember that when you climb to me. Those ashes are not my children. Nothing you bring me will be."''',
       c("Continue", "end")),

    # Unknown: she wants the Commander to find them.
    dv("unknown", '''"Found them?" {n}She does not even let you reach the top of the stair.{/n} "It has been days. You are the one who walks about in that city and asks people questions."''',
       c('"They were taken out of the Sanctum. Nobody will say where."', "unknown_told"),
       c('"I haven\'t found anything. I\'m still looking."', "unknown_looking")),
    dv("unknown_told", '''"Nobody will say." {n}She lies down again, heavily.{/n} "That is what they told me about the first clutch I ever saw taken, when I was too small to burn anyone for it. Nobody will say. Nobody ever says." {n}Her eye closes.{/n} "Keep asking. Ask the wrong people. You are good at the wrong people."''',
       c("Continue", "end")),
    dv("unknown_looking", '''"Still looking." {n}She smells you, a long, deliberate breath, from your boots to your hair.{/n} "True. You smell of other people's archives and other people's lies. Good." {n}She puts her head down.{/n} "Keep looking. I will know if you stop."''',
       c("Continue", "end")),

    # Option A: she took the clutch home herself.
    dv("collected", '''{n}She is lying curled around the base of the stair, and inside the curl, in a nest of fleeces and stolen cloaks, are her eggs, all she found in the straw, every one of them warm as bread and ticking faintly as it cools and warms. She does not get up.{/n} "I have to hunt," {n}she says.{/n} "I have not hunted since I carried them up here, and I am beginning to look at them the way I look at oxen."
{n}Her eye settles on you.{/n} "Sit with them. Until dawn. If one is missing when I come back, I will eat you, and then I will count again."''',
       c("[Sit with the eggs until dawn.]", "sat"),
       c('"I have a war to run."', "no_sit")),
    nar("sat", '''{n}She goes out over the north wall without a sound. You sit in the curl of warm fleece with your back to the stair and a clutch of woundwyrm eggs against your knees, and every so often one of them moves under your hand, the way a sleeper turns over. Twice in the night something comes up the ridge, smells what is in the tower, and goes away again.{/n}
{n}She comes back before dawn with a stag in her jaws and blood to the eyes, and counts them with her nose, one by one, while you sit very still. Then she lies down around them and around you together, and does not tell you to go.{/n}''',
        c("Continue", "end")),
    dv("no_sit", '''"A war." {n}She looks at you the way she would look at a door she had decided not to eat.{/n} "Yes. You have a war. I have a clutch and a hunger, and you have just told me which of them to trust tonight." {n}She lays her head down across the fleeces.{/n} "Go down. I will hunt hungry and come back hungrier, and if I look at them wrong, crusader, that will be yours too."''',
       c("Continue", "end")),
    teller("end", '''{n}The Storyteller is waiting at the foot of the ridge, as he always is, with the lantern he does not need.{/n} "You were a long time." {n}He falls in beside you.{/n} "I heard a little of it. Not much; I kept back. There are things a messenger should not carry." {n}A pause.{/n} {n}He does not ask what she said. At the gate he stops.{/n} "Whatever she asked you for tonight, Commander, she will ask again. She does not forget a debt, and she has decided that her children are one you owe."''',
        c('"I know."', flags=(CLUTCH_SPOKEN,))),
], requires=(CLIMBED,), forbids=(CLUTCH_SPOKEN,), delay=24)


# --- 6. The bane of the Worldwound (after the first climb, when she has been fed on the enemy) -----------------------

hub(T + "bane", "A trophy for your desk", '"What\'s in the sack, and why is it moving?"', [
    teller("start", '''"A present." {n}He sets the sack on the table with a great deal of care.{/n} "From the ridge. She asked me to say that it is dead, and that it is only moving because of the way she killed it, and that you should not open it near food."
{n}Inside is the head of a demon: a babau, flayed and grinning, its jaw still working slowly on nothing.{/n}''',
        c("Continue", "hunter", requires=(HUNTS,)),
        c("Continue", "cultists", requires=(RUTHLESS,), forbids=(HUNTS,))),
    teller("hunter", '''"She has been hunting the Worldwound's edge since you told her to. She comes back at dawn, most days, with something in her teeth." {n}He tilts his head.{/n} "The scouts have started to follow her flights. Where she hunts, the demons are thin the next week. Your generals have begun to mark her kills on their maps, as if she were a regiment. She knows. She asked me to find out what regiment she is."''',
        c("Continue", "go_up")),
    teller("cultists", '''"The cells are emptier every week. The carts go up full and come down empty and clean; she licks them clean, the drovers say, and then asks for more." {n}He is quiet for a moment.{/n} "She sent this one down because it was the last thing they prayed to. The cultists. She said it came, eventually, when there were very few of them left, and she was so pleased that it had finally come that she killed it slowly."''',
        c("Continue", "go_up")),
    nar("go_up", '''{n}You go up the ridge that night with the head in its sack, and put it down on the tower floor between you.{/n}''',
        c("Continue", "her")),
    dv("her", '''"You brought it back." {n}She sounds amused.{/n} "Most people would have burned it. Your quartermaster would have sold it. You carried it up a mountain to show me you had received it." {n}She noses it over with one claw; the jaw keeps working.{/n} "They have a name for me down there now, did the old man tell you? The demons. It is not a polite name. I have decided I like it better than the one I was hatched with."''',
       c('[Keep the trophy] "It goes on my desk."', "keep", flags=(TROPHY, BANE_SEEN)),
       c('"Burn it. I don\'t need a demon\'s head to know what you are."', "burn", flags=(BANE_SEEN,), forbids=(FLOWN,)),
       c('"Burn it. I don\'t need a demon\'s head to know what you are."', "burn_free", flags=(BANE_SEEN,), requires=(FLOWN,))),
    dv("keep", '''"On your desk." {n}Her claw pushes the writhing sack toward you.{/n} "Where your generals will hear it when they tell you the war is hopeless. Bane of the Worldwound. Let the demons learn why. I want the next one alive long enough to see what I did to this one."''',
       c("Continue", "end")),
    dv("burn", '''{n}The eye narrows, then opens again. She breathes on the sack, and the head inside it finally stops moving.{/n} "You do not need it to know what I am." {n}She lays her chin on her claws.{/n} "No. You watched what I am climb out of what I was. You would know it in the dark. That is a very unpleasant thing to be known by, crusader. I am getting used to it."''',
       c("Continue", "end")),
    teller("end", '''{n}When you come down, the Storyteller is sitting on a rock at the foot of the ridge, listening to the wind.{/n} "She hunted all through my captivity, too, and brought nothing back but bones. She is bringing things back to someone now." {n}He stands.{/n} "That is how a cat brings a mouse to the door. I would not mistake it for anything gentler, and neither, I think, would she."''',
        c('"Good night."')),
    dv("burn_free", '''{n}The eye narrows, then opens again. She breathes on the sack, and the head inside it finally stops moving.{/n} "You do not need it to know what I am." {n}She lays her chin on her claws.{/n} "No. You fought me in my own lair, and let me fly from you bleeding, and then walked into Xanthir's house for my eggs. You would know what I am in the dark. You know too much about me, crusader. I have eaten things for less."''',
       c("Continue", "end")),
], requires=(CLIMBED,), forbids=(BANE_SEEN,), delay=48, RequiresAnyGroups=[[RUTHLESS, HUNTS]])


# --- After the commit: 7. The first bite -----------------------------------------------------------------------------

hub(T + "first_bite", "Once a year, where she chooses", '"She sent for me. Just me."', [
    teller("start", '''"Just you." {n}He does not get up.{/n} "She was very specific. I am to walk you to the foot of the ridge and then walk back, and I am not to listen, and I am to tell the watch on the north gate that if they see fire on the ridge tonight it is not the enemy." {n}He folds his hands on the table.{/n} "I will leave you at the path. I have no wish to hear what follows, and she has made very sure that I will not."''',
        c("Continue", "ridge")),
    nar("ridge", '''{n}He leaves you at the foot of the path. You climb the rest alone, in the dark, with the lamps of Drezen at your back and the tower above you like a black tooth.{/n}
{n}There is fire on the ridge. She has lit it herself: a ring of burning brush around the base of the tower, low and orange, so that the whole ruin glows from inside like a lantern. The heat reaches you halfway up the path.{/n}''',
        c("Continue", "inside", forbids=(FLOWN,)),
        c("Continue", "inside_free", requires=(FLOWN,))),
    dv("inside", '''"You came." {n}She rises from the burning brush, flames sliding off her new grey hide. She crosses to the unlit side of the ruin and lies on the cold stone. You wait at the doorway while the night wind carries the smoke away. When you reach toward her, the scales are warm; you can keep your palm against them.{/n} "Not the sword arm. I remember. Now the gauntlet. And the rest. Your generals can have their iron back in the morning."''',
        c("[Take off the gauntlet, and then the rest.]", "close")),
    nar("close", '''{n}You unbuckle your armor beside the doorway, away from the burning brush. She curls around you on the unlit stone, her tail drawing your legs into the hollow beneath her wing. Her scales press against your skin. Behind her, the fire throws shadows up the wall.{/n}
{n}She lowers her head over your shoulder and runs her tongue along your bared forearm, from elbow to wrist, then returns to the pulse. Her teeth hang beside it.{/n}''',
        c("Continue", "tasting", forbids=(FLOWN,)),
        c("Continue", "tasting_free", requires=(FLOWN,))),
    dv("tasting", '''"There," {n}she says, very low, and the word goes through the coils and through you.{/n} "Iron. Ink. Fear, a little; good. And under it the thing I tasted in the dark while I was dead. The story. You still taste of the story you paid my tariff with."
{n}The coils tighten, just enough.{/n} "Look at me. I want you to watch. And tell me why you climbed up here with your belt already loose."''',
        c('[Look at her] "Because I\'ve wanted you since the first night you called me food."', "bite"),
        c("[Look at her, and let her read the answer off your skin.]", "bite")),
    nar("bite", '''{n}Her eye stays on yours as her teeth close around your forearm. The points break the skin, no deeper than the small bite you promised. She drinks, then releases the arm. You bind it with the fleece beside you.{/n}
{n}She raises her wing, exposing the seam where the killing blow went in. Her tail draws you across the cool stone and against her belly. You put your hand beneath the raised wing; she shifts into the touch, her claws grinding against the floor.{/n}
"Mine," {n}she says against your hair.{/n} "Stay. I did not call you up here for your arm alone."
{n}She draws you closer, and you reach for her.{/n}
{n}Your hands find the buckles of your armor and she watches every one of them open, her eye gone to a coal, her breath coming slow and hot and loud in the dark of the wing. Gauntlet, bracer, belt, the wet leather and the shirt beneath it; you set each piece on the stone and her tail takes each new stretch of bare skin in turn, coiling up your calf, round your thigh, over your hip, drawing the cold out of you with its heat. The scales under your palms run from smooth to ridged to blistering, and where you press, her whole length shudders and her claws grind furrows in the floor.{/n}
"Mine," {n}she says again, lower.{/n} "I have eaten better than you and wanted it less. Tell me what you want, little thing. Say it out loud, so the stone hears it."
{n}You tell her. She listens to every word with her head bent over you, her breath hot on your face, and when you finish she makes a sound in her chest like a forge bellows drawing in air. The wing comes down over the two of you. The tail takes you in a slow, tightening spiral against her belly, your bare skin to her hide, and she holds you there, hot and trembling and entirely hers, while the last of the cold goes out of the stone.{/n}''',
        c("Continue", "morning")),
    nar("morning", '''{n}The brush has burned to a black ring. Dawn reaches the doorway where you left your armor. You lie beneath her wing on the unlit side of the tower. Her scales have pressed red marks into your shoulder and hip. The fleece around your forearm is spotted with blood; the crescent beneath it throbs when you move.{/n}''',
        c("Continue", "after")),
    dv("after", '''"Small." {n}Her eye opens as you inspect the bandage.{/n} "I said it would be small." {n}Her tail catches your ankle when you reach for your armor.{/n} "The bells have not rung. Your generals can wait."''',
       c("[Stay a little longer.]", flags=(BITTEN_ONCE,))),
    dv("inside_free", '''"You came." {n}She rises from the burning brush, flames sliding off her scarred hide. She crosses to the unlit side of the ruin and lies on the cold stone. You wait at the doorway while the night wind carries the smoke away. When you reach toward her, the scales are warm; you can keep your palm against them.{/n} "Not the sword arm. I remember. Now the gauntlet. And the rest. Your generals can have their iron back in the morning."''',
        c("[Take off the gauntlet, and then the rest.]", "close")),
    dv("tasting_free", '''"There," {n}she says, very low, and the word goes through the coils and through you.{/n} "Iron. Ink. Fear, a little; good. And under it the thing I tasted in my lair, from behind the rocks, with a dwarf's knife a yard from my wing. The story. You still taste of the story you paid my tariff with."
{n}The coils tighten, just enough.{/n} "Look at me. I want you to watch. And tell me why you climbed up here with your belt already loose."''',
        c('[Look at her] "Because I\'ve wanted you since the first night you called me food."', "bite_free"),
        c("[Look at her, and let her read the answer off your skin.]", "bite_free")),
    nar("bite_free", '''{n}Her eye stays on yours as her teeth close around your forearm. The points break the skin, no deeper than the small bite you promised. She drinks, then releases the arm. You bind it with the fleece beside you.{/n}
{n}She raises her wing, exposing the scar left by the fight in her lair. Her tail draws you across the cool stone and against her belly. You put your hand beneath the raised wing; she shifts into the touch, her claws grinding against the floor.{/n}
"Mine," {n}she says against your hair.{/n} "Stay. I did not call you up here for your arm alone."
{n}She draws you closer, and you reach for her.{/n}
{n}Your hands find the buckles of your armor and she watches every one of them open, her eye gone to a coal, her breath coming slow and hot and loud in the dark of the wing. Gauntlet, bracer, belt, the wet leather and the shirt beneath it; you set each piece on the stone and her tail takes each new stretch of bare skin in turn, coiling up your calf, round your thigh, over your hip, drawing the cold out of you with its heat. The scales under your palms run from smooth to ridged to blistering, and where you press, her whole length shudders and her claws grind furrows in the floor.{/n}
"Mine," {n}she says again, lower.{/n} "I have eaten better than you and wanted it less. Tell me what you want, little thing. Say it out loud, so the stone hears it."
{n}You tell her. She listens to every word with her head bent over you, her breath hot on your face, and when you finish she makes a sound in her chest like a forge bellows drawing in air. The wing comes down over the two of you. The tail takes you in a slow, tightening spiral against her belly, your bare skin to her hide, and she holds you there, hot and trembling and entirely hers, while the last of the cold goes out of the stone.{/n}''',
        c("Continue", "morning")),
], requires=(COMMITTED, BITTEN, CLIMBED), forbids=(BITTEN_ONCE,), delay=24)   # the tower is climbed before it is lit


# --- 8. What she says when you are not there (the Storyteller's account) --------------------------------------------

hub(T + "what_she_says", "What she says about you", '"Does she talk about me? When I\'m not there?"', [
    teller("start", '''{n}He turns his cup before answering.{/n} "You are asking what she says about you, Commander. She did not forbid me to repeat it. I will tell you what I heard and what I found with my fingers. What you make of it is your trouble."''',
        c("Continue", "says")),
    teller("says", '''"She counts your visits. Not out loud; she scratches them on the stair, one line for each, the way prisoners mark days. I found them with my fingers, the last time I went up." {n}He rubs the bridge of his nose.{/n} "When the wind is from the city she lies with her head out of the tower and listens for your voice among the others. She can pick it out. She told me so as though she were confessing to a disease."''',
        c("Continue", "worst")),
    teller("worst", '''"And she says the worst things about you, all the time, with great enjoyment. That you climb like an ox. That you smell of other people's secrets. That you are the most dishonest creature she has met in three centuries, and that she has met demons." {n}He pauses.{/n} "Then she eats something, slowly, looking at the city, and does not speak again until I have gone. She does not do that after she talks about anyone else. I do not know what it means, Commander. I am only telling you what she does."''',
        c('"Tell her something from me."', "message"),
        c('"Don\'t tell her I asked."', "secret")),
    teller("message", '''"Very well. What shall I carry?"''',
        c('"Tell her I count them too."', "count"),
        c('"Tell her the old man talks too much."', "talks")),
    teller("count", '''{n}He nods slowly.{/n} "I will tell her. If she wants it repeated, she can ask." {n}A dry smile.{/n} "She will ask. She asks for everything twice, to see if the price changes."''',
        c("Continue", "end")),
    teller("talks", '''"She has been saying the same thing about me since the first night you climbed." {n}He chuckles, a dry sound.{/n} "Then I shall have carried a message she cannot dispute. That will be a first."''',
        c("Continue", "end")),
    teller("secret", '''"I will not tell her." {n}A pause.{/n} "She will know anyway. She can smell a question on you from the foot of the ridge, and that one has a very particular smell. But I will not be the one who told her. A messenger has some honour, even to a dragon."''',
        c("Continue", "end")),
    teller("end", '''{n}He picks up his stick and taps it once on the floor.{/n} "There. Now you know what she says when you are not there. If she asks how you learned it, I expect you to have a better answer than my name."''',
        c('"Thank you."', flags=(SHE_SAYS,))),
], requires=(COMMITTED, BITTEN_ONCE), forbids=(SHE_SAYS,), delay=48)


# --- 9. What happened next (the owed ending, collected in pieces) ---------------------------------------------------

hub(T + "what_happened_next", "The next part of the story", '"She wants the next part, doesn\'t she."', [
    teller("start", '''"She does. She says you owe her an ending, and that she has decided to collect it in installments, like rent, because a thing that is still paying cannot leave." {n}He folds his hands.{/n} "Tonight, she wants the part where the crusader goes back into the Abyss. She wants it true. She says she will know."''',
        c("Continue", "owed", requires=(ENDING_OWED,)),
        c("Continue", "sold", requires=(STORY_SOLD,), forbids=(ENDING_OWED,)),
        c("Continue", "climb", forbids=(ENDING_OWED, STORY_SOLD, PACT)),
        c("Continue", "pact_told", requires=(PACT,), forbids=(ENDING_OWED, STORY_SOLD))),
    teller("pact_told", '''"She reminds you that you told her the first part yourself, from behind a rock in her lair, with a dwarf's knife a yard from her wing: a dragon who flew, and a thief who stood before Xanthir's stone. She says that part was very good, and that you have been living on credit since."''',
        c("Continue", "climb")),
    teller("owed", '''"She reminds you that you told her the first part yourself, from behind a rock in her lair, before the blades came out. She says that part was very good, and that you have been living on credit since."''',
        c("Continue", "climb")),
    teller("sold", '''{n}His mouth twists.{/n} "She reminds you, and me, that she already has the first part. I told it to her bones. Kenabres to the night of the sale." {n}A pause.{/n} "She says it was the best meal she ever had, and that it is time for dessert."''',
        c("Continue", "climb")),
    nar("climb", '''{n}She is waiting at the top with her chin on the sill, the tower dark, the city below. She does not greet you. She opens one eye and says, "Begin."{/n}''',
        c("Continue", "tell")),
    dv("tell", '''"From the Abyss. Leave nothing out. If a demon was stupid, say it was stupid. If you were afraid, say so; I will know if you do not."''',
        c("[Tell it plainly, the way it happened.]", "plain"),
        c("[Tell it the way a bard would, with the good parts first.]", "bard"),
        c("[Tell it about her: every time you thought of the ridge.]", "about_her")),
    dv("plain", '''{n}She listens with her eyes shut. When you stop, one opens.{/n} "There. The part where you were afraid. You hurried over it." {n}Her claw rests on the scratched stair.{/n} "Stay there a little longer. Tell me what you heard before you knew you would live."''',
        c("Continue", "end")),
    dv("bard", '''"A fine noise." {n}A little flame licks the sill.{/n} "Now take the ribbons off. Who did you leave alive? What did you want from them?" {n}She lowers her head.{/n} "I have eaten enough singers to know where they hide the meat."''',
        c("Continue", "end")),
    dv("about_her", '''{n}She lets you get a long way into it before she stops you.{/n} "Enough." {n}Her voice is very low.{/n} "You were supposed to tell me about the Abyss." {n}A long silence.{/n} "You did. You told me about the Abyss, and every so often you looked up the ridge. I heard the looking." {n}She closes her eye.{/n} "Do it again and I will come down that ridge and fetch you myself, in front of your generals."''',
        c("Continue", "end")),
    dv("end", '''"Go down. That will do for tonight. There is more you owe me, and I will have it." {n}Her tail shifts across the stair, over the scratched lines, one for each visit.{/n} "You will still be paying when you are old. That was the plan."''',
       c("[Go down the mountain.]", flags=(NEXT_TOLD,))),
], requires=(COMMITTED, BITTEN_ONCE), forbids=(NEXT_TOLD,), delay=72, chapters=(5,))


# --- 10. Back up the mountain (the Commander left her the tower and her memory; one more climb) --------------------

hub(T + "back_up_the_mountain", "She is still hungry", '"Is she still up there?"', [
    teller("start", '''"She is still there. The drovers say she keeps her head on the sill, watching the city." {n}He turns toward the ridge.{/n} "They are pleased that she has left their oxen alone. I would rather hear that she had eaten."''',
        c("Continue", "climb")),
    nar("climb", '''{n}The tower is exactly as you left it: the bones sorted by size, the fleeces in the arrow slits, the grey wing folded over the top. She does not lift her head when you come in. She only says, without looking,{/n}''',
        c("Continue", "her")),
    dv("her", '''"You came back. I said you would." {n}Now she looks.{/n} "Have you come to say yes, or to tell me another story about why not? I warn you, crusader: my tariff has not changed. Once a year. Where I choose. A small bite."''',
        c('[Bare your forearm] "Once a year. Not the sword arm."', "yes", flags=(COMMITTED, BITTEN)),
        c('"Not yet. I just came to see you."', "not_yet", forbids=(FLOWN,)),
        c('"No bites. I came to tell you that."', "no", flags=(CLOSED, "devarra.trickster.refused")),
        c('"Not yet. I just came to see you."', "not_yet_free", requires=(FLOWN,))),
    dv("yes", '''"Not the sword arm." {n}She says it the way a judge says 'so ordered'.{/n} "You kept me waiting, crusader. You will pay interest. I have not yet decided in what." {n}She lays her head back on the sill, facing the city, and at last she closes both eyes.{/n}''',
        c("[Go down the mountain.]")),
    dv("not_yet", '''"To see me." {n}Her face gives you nothing to read at all.{/n} "Then look. Look as long as you like. You kept me whole for three days; you may as well look at what you kept." {n}She turns back to the city.{/n} "And then go, and come back when you have an answer. I am still hungry. I am always hungry now."''',
        c("[Go down the mountain.]", abort=True)),
    dv("no", '''"Then there is nothing in you worth keeping." {n}She does not raise her voice.{/n} "I gave you two chances, crusader. I have never given anyone two. Go down the mountain before I remember the rest of you is edible."''',
        c("[Go.]")),
    dv("not_yet_free", '''"To see me." {n}Her face gives you nothing to read at all.{/n} "Then look. Look as long as you like. You went to Xanthir's stone for me; you may as well look at what you went for." {n}She turns back to the city.{/n} "And then go, and come back when you have an answer. I am still hungry. I am always hungry now."''',
        c("[Go down the mountain.]", abort=True)),
], requires=(LEFT_HUNGRY,), forbids=(COMMITTED,), delay=72)


# --- 11. The first message (after the return): the Commander writes up the ridge -----------------------------------

MESSAGE = T + "message_sent"
HIDE_DEALT = T + "hide_dealt"
HIDE_GIVEN = T + "hide_given"
HIDE_SOLD = T + "hide_sold"
HIDE_BURNED = T + "hide_burned"
DWARF = T + "dwarf_spoken"
GREYBOR_STRUCK = "devarra.greybor_struck"   # SeenCues GoodEnter/Cue_0034 5a083cd2: "Sweet dreams." (bound in devarra_trickster)
SCRAPED = T + "scraped"
RING = T + "ring_finished"
FLOWN_OVER = T + "flown"                    # the flight over Drezen (key unchanged; renamed from FLOWN in Python only)
GENERALS = T + "generals"
ONE_BATTLE = T + "one_battle_sold"
ABYSS_BACK = T + "abyss_return"
FREE_STORY = T + "free_story"
SHELTERED = T + "sheltered"
LAST_NIGHT = T + "last_night"

hub(T + "first_message", "A message up the ridge", '"Can you take a message up the ridge?"', [
    teller("start", '''"I can." {n}He does not reach for paper; he has never needed it.{/n} "I should warn you that she will not take your words on paper. She says a letter is what people send with stories they are afraid to tell out loud. So it will be your words, in my mouth, in front of her teeth. Choose them as if you were saying them yourself."''',
        c('"Tell her: welcome back."', "welcome", forbids=(FLOWN,)),
        c('"Tell her: the oxen on the east road belong to the crusade, and so do the horses."', "oxen"),
        c('"Tell her: I\'m glad it worked."', "glad"),
        c('"Tell her: welcome back."', "welcome_free", requires=(FLOWN,))),
    teller("welcome", '''{n}He goes up at noon and comes back at dusk with soot on his sleeve.{/n} "I said, 'The Commander says: welcome back.' She said, 'Welcome. As if I had been on a journey. As if I had gone to visit relations.'" {n}He brushes the sleeve.{/n} "And then she said, 'Tell the Commander that is the stupidest thing anyone has said to me since I died, and that I will think about it for a week.' She breathed on me a little when she said it. Not enough to hurt. Enough to be understood."''',
        c("Continue", "end")),
    teller("oxen", '''{n}He goes up at noon and comes back at dusk, unharmed and faintly amused.{/n} "I said, 'The Commander says the oxen on the east road belong to the crusade.' She said, 'Everything belongs to something until I am hungry. Then it belongs to me.'" {n}He settles into his chair.{/n} "Then she asked how many oxen the crusade has. I told her I did not know. She said she would count them herself, and that you would like the result less."''',
        c("Continue", "end")),
    teller("glad", '''{n}He goes up at noon and comes back after dark, and sits for a while before he speaks.{/n} "I said, 'The Commander says: I'm glad it worked.' She was quiet until I thought she had fallen asleep, which she does, in the middle of threats." {n}His fingers find the edge of the table.{/n} "Then she said, 'It. The thing the Commander said. It worked. On me. Tell the Commander I am not an it, and I am not glad, and to say it again, slower, the next time it is brave enough to come up here itself.'"''',
        c("Continue", "end")),
    teller("end", '''"She did not send a reply, exactly. She sent a condition." {n}He smiles thinly.{/n} "You may go on sending me up that ridge with messages for as long as you like, she says, because she enjoys watching a blind man climb. But one day soon she will want to hear your voice saying them. When that day comes, I am to tell you, and you are to come."''',
        c('"I\'ll come."', flags=(MESSAGE,))),
    teller("welcome_free", '''{n}He goes up at noon and comes back at dusk with soot on his sleeve.{/n} "I said, 'The Commander says: welcome back.' She said, 'Welcome. As if I had been on a journey. As if I had gone to visit relations, and not lain on a mountain with my side open, listening to Xanthir's charm call me.'" {n}He brushes the sleeve.{/n} "And then she said, 'Tell the Commander that is the stupidest thing anyone has said to me in a hundred years, and that I will think about it for a week.' She breathed on me a little when she said it. Not enough to hurt. Enough to be understood."''',
        c("Continue", "end")),
], requires=("trickster.ever", RETURNED), forbids=(MESSAGE,), delay=24)


# --- 12. The old hide (after the return): what to do with the dead dragon ----------------------------------------------

hub(T + "the_old_hide", "Her old face", '"What happened to the old hide?"', [
    teller("start", '''"It is still where she left it. Nobody will touch it." {n}He tilts his head.{/n} "A merchant from Nerosyan has offered your treasurer a great deal of money for it: dragon hide, three hundred years old, no holes but one. The treasurer came to ask me whether the dragon who used to be in it would mind. I said I would ask you. I prefer not to ask her questions whose answers are fire."''',
        c("Continue", "ride")),
    nar("ride", '''{n}You go to see it. Nobody has moved it. It lies exactly where she fell, split along the spine from horns to tail, dry and dark as an old saddle, with the shape of her still in it. The face is the worst part: the empty eyes, the jaw hanging a little open, as though it had been about to say something when the thing inside it stood up and walked away.{/n}
{n}You are still looking at it when the shadow comes over you, and she lands on the far side of her own body.{/n}''',
        c("Continue", "her")),
    dv("her", '''{n}She does not look at the hide. She looks at you looking at it.{/n} "The old man told me there was a buyer. He told me very politely, from a great distance." {n}Her claws scrape on stone.{/n} "Well, crusader? That was me, for three hundred years. It is not me now. Tell me what you intend to do with what you killed."''',
        c('[Sell it to Nerosyan] "The crusade needs the gold more than you need a keepsake."', "sell",
          crusade=("Finances", 150), flags=(HIDE_DEALT, HIDE_SOLD)),
        c('[Burn it] "Nobody wears you. Not even as a coat."', "burn", flags=(HIDE_DEALT, HIDE_BURNED)),
        c('[Give it to her] "It\'s yours. You decide."', "give", flags=(HIDE_DEALT, HIDE_GIVEN))),
    dv("sell", '''"Gold." {n}She glances at the hide at last, and then back at you, and something like approval moves in her eye.{/n} "Yes. That is what I would have done. Sell the dead thing to the fool who wants it, and eat well on the money." {n}She lifts her head.{/n} "When they make it into a coat, crusader, find out who wears it. I would like to know which of your nobles is walking around inside my old face. I would like to visit."''',
       c("Continue", "end")),
    dv("burn", '''{n}She goes very still.{/n} "Nobody wears me." {n}She repeats it as though tasting a new spice.{/n} "Very well. Stand back."
{n}She breathes on her old body. It takes a long time to catch; dragon hide does not burn easily, even when the dragon wants it to. When it does, she watches it the whole way down, and she does not say anything at all until there is nothing but a black shape on the stones.{/n}''',
       c("Continue", "burn_2")),
    dv("burn_2", '''"There." {n}Her voice is rough with smoke.{/n} "Now I am the only one." {n}She turns her head and looks at you.{/n} "You burned good hide, crusader. A merchant in Nerosyan would have paid you a hoard for it." {n}She licks the ash off her teeth.{/n} "Bring me something worth that fire. I am going to eat something now. Do not watch."''',
       c("Continue", "end")),
    dv("give", '''"Mine." {n}She looks down at it at last, at her own dead face, for a very long time.{/n} "I will keep it, then. I will drag it up the ridge and lay it across the door of the tower, so that anyone who comes to kill me has to walk through the last one who tried."
{n}She takes the hide in her jaws, gently, the way she would lift an egg, and does not look at you again. At the way out she stops.{/n} "You might have sold it. I know what it was worth. Remember that you did not. I will."''',
       c("Continue", "end")),
    teller("end", '''{n}Back in Drezen, the Storyteller listens to your account without interrupting.{/n} "I was in the lair when she was still wearing it. I could not see her face, of course. But I could hear it, when she spoke; the old hide creaked around the jaw. The new one does not."''',
        c('"Maybe not."')),
], requires=("trickster.ever", RETURNED), forbids=(HIDE_DEALT, FLOWN), delay=24)


# --- 13. The dwarf (after the first climb): the blade under the wing ---------------------------------------------------

hub(T + "the_dwarf", "Who set the ambush", '"She asked about Greybor, didn\'t she."', [
    teller("start", '''"She did. She asked me the name of the dwarf who put his blade under her wing. She described the blade. She described the angle." {n}His hands are very still on the table.{/n} "I did not tell her. I am not in the habit of handing names to dragons. But she knows the smell of him, Commander, and I think she knows you know it too. She has asked for you."''',
        c("Continue", "climb")),
    dv("climb", '''"The dwarf." {n}She does not bother with a greeting; she is lying across the doorway with the grey seam under her wing turned toward you, deliberately, so you cannot look anywhere else.{/n} "He found the one soft place on me in three hundred years, and he put steel in it, and he said 'sweet dreams'. I heard him through my own roaring." {n}Her eye narrows.{/n} "I want him."''',
       c('"No. He works for me. He\'s under my protection."', "protect"),
       c('"He was paid to do it. Take it up with whoever paid him. That was me."', "me"),
       c('"He said to tell you repeat work is billed at the full rate."', "rate", requires=("devarra.react.greybor.repeat_work",))),
    dv("protect", '''"Under your protection." {n}The tower goes very quiet.{/n} "You say that word to me a great deal, crusader, for a thing that is soft all the way through." {n}She flexes her claws.{/n} "Very well. I will not eat your dwarf. Not because you told me not to. Because he was good at it. The ones who are good at killing you are the only ones worth remembering. I will remember him instead. It is worse."''',
       c("Continue", "end")),
    dv("me", '''{n}She lowers her head until her eye is level with yours and stays there, breathing.{/n} "You." {n}It is almost fond.{/n} "Yes. It was always you, wasn't it? The dwarf was the blade. You were the hand. And then you were the voice, too, telling the story that paid my tariff, and then the one who kept the saws off me." {n}She pulls back.{/n} "You are very greedy, crusader. You wanted to kill me and name me both. I have never met anyone so greedy. It is nearly dragonish."''',
       c("Continue", "end")),
    dv("rate", '''{n}For a moment she simply stares. Then the laugh comes, the kiln door, and half the fleeces in the arrow slits blow out down the ridge.{/n} "Full rate. The dwarf wants paying twice for the same dragon." {n}She cannot stop; smoke comes out of her in little gusts.{/n} "Tell him yes. Tell him I will pay him, gladly, the day he tries. Tell him I will even let him pick the soft place. I have a new one now."''',
       c("Continue", "end")),
    teller("end", '''{n}At the foot of the ridge, the Storyteller falls into step beside you.{/n} "And?" {n}He listens to your answer and nods.{/n} "Then the dwarf lives. I am glad. He is rude to me, and he smells of other men's blood, but he once told me my story about the ring was 'not bad', which from him is an ode."''',
        c('"From him, it is."', flags=(DWARF,))),
], requires=(CLIMBED, GREYBOR_STRUCK), forbids=(DWARF,), delay=24)   # only where his strike is on record (GoodEnter/Cue_0034)


# --- 14. The itch (after the first climb): the old scales that did not come off ----------------------------------

hub(T + "the_itch", "The places she cannot reach", '"She\'s asked for a spade?"', [
    teller("start", '''"A spade. A long-handled one. And a crusader to hold it." {n}He sounds as if he has been trying not to laugh for some time.{/n} "She says the moult did not finish properly. There are old scales still stuck to her back, between the wings, where she cannot reach with teeth or claws, and they itch. She has been rubbing against the tower until the stones come loose. The garrison on the north wall think it is an earthquake."''',
        c("Continue", "climb")),
    nar("climb", '''{n}She is lying flat on the tower floor when you arrive, wings spread and pinned under their own weight like a tent that has fallen down, and she does not lift her head.{/n}
{n}Between the wings, along her spine, the new grey hide is crusted with patches of the old one: dark, dry scales still clinging on, curling at the edges, some the size of shields. The skin under them is angry and pink.{/n}''',
        c("Continue", "her")),
    dv("her", '''"Do not laugh." {n}Her voice is muffled by the floor.{/n} "If you laugh I will roll over, and then there will be a great deal less of you to laugh with. Climb up. Scrape. Do not stop until I say."''',
       c("[Climb up and start scraping.]", "scrape")),
    nar("scrape", '''{n}You climb up her flank and walk the length of her spine with the spade, and begin. The old scales come away with a sound like bark tearing. Under each one the new grey hide is soft and hot, softer than you would have believed of anything on a dragon, and every time a scale comes free the whole long body under your boots shudders from end to end and she lets out a breath that rattles the fleeces in the windows.{/n}''',
        c("Continue", "halfway")),
    dv("halfway", '''"Left," {n}she says.{/n} "No. My left. Higher." {n}A long, slow exhale.{/n} "There." {n}Another scale. Another shudder.{/n} "You are the first thing that has touched my back in three hundred years that was not trying to put a blade in it. Do not think that means anything. It means you have a spade."''',
       c("[Keep scraping in silence.]", "silent"),
       c('"It means something. You asked me, not the garrison."', "means")),
    nar("silent", '''{n}You keep scraping, and she keeps breathing, and after a while the breathing slows and goes deep and even, and you realise, halfway down her tail, that the woundwyrm beneath your boots has fallen asleep under your spade like a cat in the sun.{/n}
{n}You finish the job anyway, as quietly as you can. When you climb down her eye is open, watching you, and she does not say anything at all.{/n}''',
        c("Continue", "end")),
    dv("means", '''"I asked you because the garrison would have used the spade on my neck." {n}A pause, and another scale comes away, and her whole spine arches under you in a way that makes you grab for a ridge of bone to stay on.{/n} "And because you would not." {n}Her voice drops.{/n} "Do not make me say it twice. Scrape."''',
       c("Continue", "end")),
    teller("end", '''{n}The Storyteller is waiting at the bottom of the ridge with a bucket of water, which he holds out without comment.{/n} "You are covered in dragon." {n}He sniffs.{/n} "She is quiet up there now. Quieter than I have ever heard her. If I did not know better I would say you had done the one thing I thought nobody could do to a woundwyrm." {n}He takes back the bucket.{/n} "You have made her comfortable, and she let you see where she itches. Be careful, Commander. She will want something back for that, and she will choose what."''',
        c('"I know."', flags=(SCRAPED,))),
], requires=(CLIMBED,), forbids=(SCRAPED, FLOWN), delay=48)


hub(T + "the_scabs", "The places she cannot reach", '"She\'s asked for a spade?"', [
    teller("start", '''"A spade. A long-handled one. And a crusader to hold it." {n}He sounds as if he has been trying not to laugh for some time.{/n} "The fight in her lair cracked the scales along her back, she says, between the wings, where a dragon cannot reach with teeth or claws. The dead ones will not drop, the new ones are pushing up under them, and it itches. She has been rubbing against the tower until the stones come loose. The garrison on the north wall think it is an earthquake."''',
        c("Continue", "climb")),
    nar("climb", '''{n}She is lying flat on the tower floor when you arrive, wings spread and pinned under their own weight like a tent that has fallen down, and she does not lift her head.{/n}
{n}Between the wings, along her spine, a broad patch of scales is dead and dull, cracked and curled at the edges like old bark, some of them the size of shields. The skin showing between them is angry and pink, and under the dead plates you can see the edges of new ones coming in.{/n}''',
        c("Continue", "her")),
    dv("her", '''"Do not laugh." {n}Her voice is muffled by the floor.{/n} "If you laugh I will roll over, and then there will be a great deal less of you to laugh with. Climb up. Scrape. Do not stop until I say."''',
       c("[Climb up and start scraping.]", "scrape")),
    nar("scrape", '''{n}You climb up her flank and walk the length of her spine with the spade, and begin. The dead scales come away with a sound like bark tearing. Under each one the new scale is soft and hot, softer than you would have believed of anything on a dragon, and every time a plate comes free the whole long body under your boots shudders from end to end and she lets out a breath that rattles the fleeces in the windows.{/n}''',
        c("Continue", "halfway")),
    dv("halfway", '''"Left," {n}she says.{/n} "No. My left. Higher." {n}A long, slow exhale.{/n} "There." {n}Another plate. Another shudder.{/n} "You are the first thing that has touched my back in three hundred years that was not trying to put a blade in it. Do not think that means anything. It means you have a spade."''',
       c("[Keep scraping in silence.]", "silent"),
       c('"It means something. You asked me, not the garrison."', "means")),
    nar("silent", '''{n}You keep scraping, and she keeps breathing, and after a while the breathing slows and goes deep and even, and you realise, halfway down her tail, that the woundwyrm beneath your boots has fallen asleep under your spade like a cat in the sun.{/n}
{n}You finish the job anyway, as quietly as you can. When you climb down her eye is open, watching you, and she does not say anything at all.{/n}''',
        c("Continue", "end")),
    dv("means", '''"I asked you because the garrison would have used the spade on my neck." {n}A pause, and another plate comes away, and her whole spine arches under you in a way that makes you grab for a ridge of bone to stay on.{/n} "And because you would not." {n}Her voice drops.{/n} "Do not make me say it twice. Scrape."''',
       c("Continue", "end")),
    teller("end", '''{n}The Storyteller is waiting at the bottom of the ridge with a bucket of water, which he holds out without comment.{/n} "You are covered in dragon." {n}He sniffs.{/n} "She is quiet up there now. Quieter than I have ever heard her." {n}He takes back the bucket.{/n} "You have made her comfortable, and she let you see where she itches. Be careful, Commander. She will want something back for that, and she will choose what."''',
        c('"I know."', flags=(SCRAPED,))),
], requires=(CLIMBED, FLOWN), forbids=(SCRAPED,), delay=48)


# --- 15. The ring (after the first climb): the Storyteller finishes the story he started in her lair ----------------

hub(T + "the_ring", "The one about the ring", '"She wants the end of the story about the ring."', [
    teller("start", '''"She does." {n}The Storyteller grips the head of his stick.{/n} "In the lair I told her about a gnome at a party in Restov, and a signet ring with the arms of King Irovetti, and a man who thought himself immune to the knives he had paid for. She asked me what happened next, and then the lair was full of steel and fire, and I never finished." {n}He folds his hands.{/n} "She has decided I owe her the ending. She wants it told in the tower, with you present, so that there is a witness when she decides whether it was worth my life."''',
        c('"I\'ll come."', "tower"),
        c('"I\'ll come, and if she tries to eat you, she\'ll have to go through me."', "guard")),
    teller("guard", '''"How gallant." {n}The discomfort does not leave his face, but something else joins it.{/n} "She would go through you, Commander, and very quickly, and it would be undignified for both of us. But I thank you. It is a better line than most of the ones in my story."''',
        c("Continue", "tower")),
    nar("tower", '''{n}So you climb the ridge together, the blind elf and the Commander, and the old man sits down on a bone the size of a bench in front of a dragon who once kept him prisoner in her lair, and clears his throat.{/n}
{n}She lies with her chin on the floor, her eye level with his face, close enough that her breath stirs his hair. She does not blink.{/n}''',
        c("Continue", "story")),
    teller("story", '''"The gnome's name was Tartuccio," {n}he says, and his voice turns shrill and sneering, the voice of someone else.{/n} "He rode into the Stolen Lands with the ring on his finger and a list of rivals in his pocket, and at the top of the list was an adventurer nobody had heard of. A dark horse." {n}The voice goes back to his own.{/n} "He meant to sell a wooden sword to King Irovetti for the price of a crown. He was very clever. He planned everything except the possibility that the dark horse might be the better story."''',
        c("Continue", "story_2")),
    teller("story_2", '''"He did not come back out of the Stolen Lands. The dark horse did, and became a baron, and then something the songs in Brevoy still disagree about." {n}He spreads his hands.{/n} "And the ring he thought would keep him safe from all the knives? It is in my bag, as it was in your lair, madam. It kept him safe from every knife but the one he was holding."''',
        c("Continue", "verdict")),
    dv("verdict", '''{n}She says nothing, and the old man's hands begin, very slightly, to tremble.{/n} "A clever thing," {n}she says at last,{/n} "that thought itself immune, and was undone by a stranger it did not take seriously." {n}Her eye slides, slowly, from the Storyteller to you.{/n} "I wonder why you chose to tell me that story, old man, in front of this one."''',
       c('"Because it\'s true, and you asked for it."', "true"),
       c('"Because he\'s a better storyteller than he lets on."', "better")),
    dv("true", '''"Because it is true." {n}She lifts her head.{/n} "Yes. It was worth your life, old man. It was worth it the first time, too; I was only waiting to see if you knew it." {n}She turns away, toward the city.{/n} "Your debt is paid. Go down. And take the dark horse with you before I start wondering which of us is the gnome."''',
       c("Continue", "end")),
    dv("better", '''"He is." {n}She says it to you, not to him.{/n} "He told me that story in the lair to keep me from eating him, and he tells it now to warn you about me, and he has made both of those the same story, and he thinks I did not notice." {n}Her lip lifts off one tooth.{/n} "Your debt is paid, old man. It was paid the first time. I only wanted to hear how well you lie when you are frightened. Very well. Go down, both of you."''',
       c("Continue", "end")),
    teller("end", '''{n}He is silent all the way down the ridge, his stick finding the stones one by one. At the bottom he stops.{/n} "Thank you for coming, Commander. I have told that story in the courts of three kingdoms, and I have never been so frightened telling it." {n}A pause.{/n} "Or so pleased with how it went. Do not tell her either of those things."''',
        c('"I won\'t."', flags=(RING,))),
], requires=(CLIMBED, "devarra.lair_story_heard"), forbids=(RING,), delay=48)   # only where the ring story was begun (GoodEnter/Cue_0028)


# --- 16. The flight (after the first climb): she takes the Commander up over Drezen ------------------------------------

hub(T + "the_flight", "Over Drezen at night", '"She wants to fly? With me?"', [
    teller("start", '''"Not with you. On you, she said first, then corrected herself." {n}He smiles.{/n} "She wants to take you up tonight. She says a thing that lies about dragons should find out what the world looks like to one before it says anything else about us. I would dress warmly. I would also not look down, but I am told that is advice for the sighted."''',
        c("Continue", "up")),
    nar("up", '''{n}She lowers one shoulder for you without a word. There is nowhere obvious to hold, so you hold the ridge of bone at the base of her neck, and she launches from the tower in one long, silent push, and the ridge drops away beneath you, and then Drezen does, and then the world.{/n}
{n}It is very cold, and very quiet. Up here the wind is the only sound, and under it, when she tilts her head back toward you, her voice.{/n}''',
        c("Continue", "sky")),
    dv("sky", '''"There. Your city." {n}Below, Drezen is a scatter of small gold lamps on a black cloth.{/n} "You fight for that. All those little lights. From here I could put my claw over it and hide it. From here it looks like the clutch I had before this one, in a cave in the hills, before the ground there broke open." {n}Her wings shift.{/n} "Someone else's crusade came through. They did not eat them. They did not need to. They simply walked on them."''',
       c('"I didn\'t know."', "didnt", forbids=(FLOWN,)),
       c('"Is that why you fight demons?"', "demons"),
       c('"I didn\'t know."', "didnt_free", requires=(FLOWN,))),
    dv("didnt", '''"No. Nobody knows. There is nobody left who was there except me." {n}She banks, slowly, over the dark river.{/n} "I am telling you because you are a thief of stories, and I want this one stolen. When I am dead again, properly this time, somebody should know that Xanthir's toys had my clutch in their fists, and I got up anyway." {n}A pause.{/n} "Do not make it sad. It was not sad. It was hunger."''',
       c("Continue", "down")),
    dv("demons", '''"I fight everything." {n}She sounds almost amused.{/n} "Demons are simply the easiest to find. They are everywhere, and they never learn, and they taste of rot, which is how I like my enemies." {n}She drops a little, and your stomach goes with her.{/n} "And the golems that held my eggs were made by a man who serves them. I am very thorough, crusader. I go back to the beginning of a debt."''',
       c("Continue", "down")),
    nar("down", '''{n}She brings you down on the ridge just before dawn, so gently that you barely feel the landing. Your hands are numb, your face is raw with cold, and Drezen, which was a scatter of lamps under you all night, is only now growing back to its proper size.{/n}''',
        c("Continue", "end_her", forbids=(FLOWN,)),
        c("Continue", "end_her_free", requires=(FLOWN,))),
    dv("end_her", '''"Now you know how small you are." {n}She settles around the tower, folding her wings.{/n} "Remember it the next time you tell someone what they are. You told me I was a clutch-mother. From up there, crusader, you are a lamp. A very small lamp. I could put it out with one breath." {n}She closes her eyes.{/n} "I will not. Go down."''',
       c("[Go down the mountain.]", flags=(T + "flown",))),
    dv("didnt_free", '''"No. Nobody knows about that clutch. There is nobody left who was there except me." {n}She banks, slowly, over the dark river.{/n} "I am telling you because you are a thief of stories, and I want this one stolen. When I finally die, somebody should know that Xanthir's toys had my clutch in their fists, and called, and that one night I did not go." {n}A pause.{/n} "Do not make it sad. It was not sad. It was hunger."''',
       c("Continue", "down")),
    dv("end_her_free", '''"Now you know how small you are." {n}She settles around the tower, folding her wings.{/n} "Remember it the next time you tell a stone what it is to do. From up there, crusader, you are a lamp. A very small lamp. I could put it out with one breath." {n}She closes her eyes.{/n} "I will not. Go down."''',
       c("[Go down the mountain.]", flags=(T + "flown",))),
], requires=(CLIMBED,), forbids=(T + "flown",), delay=72)


# --- 17. The generals (after the first climb): the crusade wants a dragon on its side -------------------------------

hub(T + "the_generals", "A dragon for the war", '"The general staff asked you about her?"', [
    teller("start", '''"The general staff asked me whether the dragon on the north ridge could be persuaded to fight for the crusade." {n}His mouth twists.{/n} "I told them that nobody has ever persuaded her of anything, and that I would advise against the attempt in writing. They have decided that you should ask her instead. Your generals are very brave when the dragon is someone else's conversation."''',
        c("Continue", "climb")),
    dv("climb", '''"Your generals sent you." {n}She already knows; she can smell the staff tent on you, the ink and the map wax.{/n} "They want a dragon on the field. They want to point at a demon and say 'there', and have me go there." {n}Her eye narrows.{/n} "Well? You are the one who tells me what I am. Tell me what I am to your generals."''',
       c('[Order her] "You\'ll fight where the crusade needs you."', "order"),
       c('[Ask her] "Will you? Once. Where you choose."', "ask"),
       c('[Bargain] "One battle. Name your price."', "bargain")),
    dv("order", '''{n}The wing hits you before the sentence ends: not hard, not enough to break anything, just enough to put you flat on your back among the bones.{/n} "No," {n}she says.{/n} "You tell me what I am. You do not tell me where to go. Learn the difference, crusader, before I teach it to you with my teeth."
{n}She lets you get up.{/n} "Tell your generals the dragon said no. Tell them it was very polite about it. Tell them you still have all your fingers, and let them wonder why."''',
       c("Continue", "end")),
    dv("ask", '''"Ask." {n}She considers it the way she considers food.{/n} "You ask me. Not your generals. You." {n}She is silent a long while.{/n} "Once. Where I choose, when I choose, against whatever I choose. And they will not be told in advance, and they will not put me in their dispatches, and when it is over nobody will thank me, because I will not be there to be thanked." {n}Her eye glints.{/n} "Tell them that is my offer. They will hate it. Good."''',
       c("Continue", "end", flags=(ONE_BATTLE,))),
    dv("bargain", '''"A price." {n}Now she is interested.{/n} "Yes. That is how a crusade should talk to a dragon." {n}Her claws tap the floor.{/n} "One battle. For one battle I want the story of it. Not the dispatch; the story. Told by you, here, the night after, every death in it, and I will judge whether the war was worth my wings." {n}She shows her teeth.{/n} "If it was not, I will take the difference out of your generals. Agreed?"''',
       c('"Agreed."', "end", flags=(ONE_BATTLE,))),
    teller("end", '''{n}The Storyteller takes your report to the staff tent himself, and comes back looking pleased.{/n} "The generals are furious. One of them threw an inkwell. I could not see it, of course, but I heard where it landed, and it was not near me." {n}He sits.{/n} "Dragons are wonderful for morale, Commander. Other people's morale. Never one's own."''',
        c('"Good work."', flags=(GENERALS,))),
], requires=(CLIMBED,), forbids=(GENERALS,), delay=72)


# --- 18. After the Abyss (Chapter 5): she waited ---------------------------------------------------------------------

hub(T + "after_the_abyss", "You were gone", '"Was she there, while I was in the Abyss?"', [
    teller("start", '''"She was there. Every day. She did not leave the ridge once, except to eat, and then she ate close." {n}He is quiet a moment.{/n} "She asked me where you were the first morning. I said the Abyss. She said, 'Which part?' I said I did not know. She said, 'Then find out.' I said I was a blind old elf and could not. She said, 'Then sit here with me until you can,' and so I sat. For some time. She is not good company, but she is warm."''',
        c("Continue", "climb")),
    dv("climb", '''{n}She hears you on the path long before you reach the top, and she does not move. When you come through the door she is lying exactly where she was when you left, as if she had not shifted in all those months, and her eye follows you across the floor and does not let go.{/n}
"You went into the Wound." {n}Her voice is flat.{/n} "Without asking me. Without telling me what you would bring back."''',
       c('"I came back."', "back"),
       c('"I brought you the worst hour of it. Nobody else has heard it."', "gift"),
       # PP7: the Chapter 4 sky (wrong_sky), appended; their pages are the last of this scene.
       c('"I flew over the Abyss, on a ship. I kept the part where the deck fell out from under me."', "sky_fear", requires=(SKY_FEAR,)),
       c('"I brought you a sky. The Abyss from a ship\'s rail, all of it."', "sky_view", requires=(SKY_VIEW,)),
       c('"I flew over the Abyss on a ship. The crew has the story already."', "sky_spent", requires=(SKY_SPENT,))),
    dv("back",'''"You came back." {n}She breathes in, a long, slow breath from your boots to your hair, taking stock.{/n} "You smell of the Abyss. Of demon and of rot and of a hundred things I do not have names for." {n}Her tail moves across the stair, over old scratches in the stone, as if checking that they are all still there.{/n} "You came back. Do not do that again without telling me. A thing that owes me something does not go where it cannot pay."''',
       c("Continue", "end")),
    dv("gift", '''{n}You sit down on the bones and tell her the worst hour you had on the other side, the one you have told nobody, not the generals, not the people who were there. She listens with her eyes shut and her nostrils open, as if she could smell it on you while you talk.{/n}
"The worst hour. Kept back. For me." {n}Her eye opens, a slit of furnace.{/n} "That is a better tithe than a forearm, crusader, and you will not get away with paying it only once. Do not look at me like that. Go away. I want to eat something and think about it."''',
       c("Continue", "end")),
    teller("end", '''{n}At the foot of the ridge, the Storyteller is standing where he always stands.{/n} "She is quieter. That is good. The garrison on the north wall have been hearing her all the months you were gone, every night: not roaring. A sound they could not name." {n}He pauses.{/n} "I could name it. I did not tell them. Some stories should not be told to soldiers."''',
        c('"What was it?"', "what")),
    teller("what", '''"She was counting." {n}He smiles.{/n} "Aloud, all night, in Draconic. The scratches on her stair, one for each time you climbed it. One, and one, and one again. As if she might have missed one, and it would be the one that mattered."''',
        c('"..."', flags=(ABYSS_BACK,))),
    dv("sky_fear", '''"On a ship." {n}Her lip lifts off one tooth.{/n} "Planks and rope and a sail, in the air, and you trusted your weight to it." {n}She makes you tell the gust twice: how far the deck fell, what your hands did, whether you made a sound.{/n}
"You were afraid of the sky. Good. It is the only honest thing anyone has ever carried out of the Abyss for me." {n}Her tail drags slowly across the scratched stair.{/n} "Next time you want to be afraid of the sky, crusader, you come up here and ask. I drop much further than a boat."''',
       c("Continue", "end")),
    dv("sky_view", '''{n}She listens with her eyes shut: the wind from underneath, the clouds carrying only colour, the spires below the keel.{/n} "A ship. To cross a sky like that." {n}Her wings shift against the walls.{/n} "I would have flown below those clouds. You brought me a sky I cannot have. I have not decided whether that is a gift or an insult. Keep coming up until I decide."''',
       c("Continue", "end")),
    dv("sky_spent", '''"The crew has it." {n}Her eye narrows to a slit.{/n} "You flew over the Abyss, and you spent it on a sailor the same night, while it was still warm." {n}She breathes out; the fleeces in the arrow slits stir.{/n} "Then I will not have it from you second-hand. Stale bread. Bring me something you kept, or bring me nothing."
{n}She turns her head to the city. After a long while, without looking at you:{/n} "What colour were the clouds?"''',
       c("Continue", "end")),
], requires=("trickster.ever", RETURNED, CLIMBED, CLIMBED_CH3), forbids=(ABYSS_BACK,), delay=0, chapters=(5,))


# --- 18b. The wrong sky (Chapter 4, PP7): a memory on the voyage to Colyphyr --------------------------------------------
# No courier climbs out of the Abyss to her ridge, and she takes no letters. What travels is a story kept back for her tariff
# ("a story buys a life", Cue_0002 546738b4). Native moment: the airship voyage out of Alushinyrra (AirAdventures_BookEvent
# a07f6d1f, every captain; StartAirAdventures cutscene in AlushinyrraMediumCity), bound as StartedDialogs. The crew, the
# gust and the colours are authored and claim no specific day of the voyage. Path: T (her survival is the flight device).
# Read in Chapter 5 by after_the_abyss (climb, appended answers). Gated like that vigil: a tower climbed before the march.

SCENES.append(scene(T + "wrong_sky", "A ship in the wrong sky", "Devarra", 4, "", [
    nar("start", '''{n}The ship lifts off from Alushinyrra and climbs into the Abyss's own sky, and for the first hours you stand at the rail and do not go below.{/n}''',
        c("Continue", "lamps", requires=(FLOWN_OVER,)),
        c("Continue", "planks", forbids=(FLOWN_OVER,))),
    nar("lamps", '''{n}You remember being this high once, when Drezen was a scatter of small gold lamps under a black wing, and a voice in the wind told you how small you were. There is no wing here. There are planks, and rope, and a sail, and wind that comes from underneath.{/n}
{n}A dragon on a ridge above Drezen sells lives for stories. She will want this one, and she will want it whole.{/n}''',
        *SKY_CHOICES),
    nar("planks", '''{n}You have never been this high with nothing under you but planks. The wind comes from underneath. The clouds are the wrong colour, and somewhere below them is a sea, or a pit, or nothing; nobody aboard will say which.{/n}
{n}A dragon on a ridge above Drezen sells lives for stories. She will want this one, and she will want it whole.{/n}''',
        *SKY_CHOICES),
    nar("fear", '''{n}It comes in the first hour: a gust from below, the deck falling a man's height and catching, and your hands shut on the rail before you knew they had moved. Nobody saw. You decide nobody will hear of it either, until a dragon does. She will want the part where the crusader was afraid of the sky.{/n}''',
        c("[Keep it for the ridge.]", flags=(SKY, SKY_FEAR))),
    nar("view", '''{n}You stay at the rail until the light changes, and learn the sky the way a thief learns a house: where the wind comes from, which clouds carry weather and which carry only colour, how the spires of Alushinyrra look from above, like teeth. You tell none of it to anyone aboard.{/n}''',
        c("[Keep it for the ridge.]", flags=(SKY, SKY_VIEW))),
    nar("spent", '''{n}The sailor on watch is glad of the company. You give him all of it, the gust and the colours and the spires like teeth, and by the change of watch the whole crew has it, a little bigger at every telling. It is a good story. It is not hers any more.{/n}''',
        c("[Go below.]", flags=(SKY, SKY_SPENT))),
], requires=("trickster.ever", RETURNED, CLIMBED, CLIMBED_CH3, VOYAGE_SEEN), forbids=(CLOSED, SKY), delay=12, last=4, optional=True,
    Relationship="devarra", Chapters=[4], Remote=True, Kind="memory"))


# --- 19. A story for nothing (after the commit) -----------------------------------------------------------------------

hub(T + "a_story_for_nothing", "Not owed", '"I want to tell her a story. Not one I owe her."', [
    teller("start", '''"Not owed." {n}He sets his cup down.{/n} "In her lair I paid for my life. Now I carry demands down this ridge. A story with nothing asked for in return? I would like to hear what she does with it."''',
        c("Continue", "climb")),
    dv("climb", '''"The old man says you have brought me a story you do not owe me." {n}She sounds suspicious.{/n} "That is not how stories work. Stories are what you pay with. What do you want for it?"''',
       c('"Nothing. Just listen."', "tell")),
    nar("tell", '''{n}So you tell her something small. A story with no dragons in it, and no demons, and no crusade: a market, a dog, a stolen pie, a rainstorm. Whether any of it happened is your business.{/n}
{n}She listens with growing confusion, and then with something else. When you finish she does not speak for a while.{/n}''',
        c("Continue", "her")),
    dv("her", '''"That was terrible." {n}She sounds genuinely offended.{/n} "Nothing happened in it. There was no price and no blood and nobody learned anything. The dog did not even eat anybody." {n}She lays her head down.{/n} "Tell it again."''',
       c("[Tell it again.]", "again")),
    nar("again", '''{n}You tell it again. Halfway through she interrupts to ask what colour the dog was, and whether the pie was meat or fruit, and then she waits, with her chin on the sill, for you to go on.{/n}''',
        c("Continue", "end_her")),
    dv("end_her", '''"Fruit," {n}she says, at the end, with deep disapproval.{/n} "I would have eaten the dog." {n}She closes her eyes.{/n} "Go down. And do not tell anyone you gave me something for nothing. If it gets about, they will all want to try it, and I will have to eat them."''',
       c("Continue", "end")),
    teller("end", '''{n}The Storyteller sits on his rock at the foot of the ridge, smiling. He gets up as you approach.{/n} "I heard her ask for it again. A dog and a stolen pie! In that lair I offered her a signet ring's history, and still had to worry about my legs." {n}He takes his stick.{/n} "I shall have to remember the pie."''',
        c('''"I'll keep that in mind."''', flags=(FREE_STORY,))),
], requires=(COMMITTED,), forbids=(FREE_STORY,), delay=48)


# --- 20. Under the wing (after the first bite): the storm -------------------------------------------------------------

hub(T + "under_the_wing", "The storm", '"There\'s a storm coming. Is she all right up there?"', [
    teller("start", '''"She is a woundwyrm on a mountain, Commander; she is the most all right thing within a hundred miles." {n}He tilts his head toward the window, where the wind is rising.{/n} "But she did send a message, an hour ago, before the rain. It was two words. 'Come up.' I told her it would be a very bad night for climbing. She said that was why."''',
        c("Continue", "climb")),
    nar("climb", '''{n}You make the top soaked to the skin, with the rain coming sideways and the lightning showing you every stone of the path in white, then taking it away. The tower is dark. Then a grey wing lifts from the doorway, just enough, and you duck under it, and it comes down behind you.{/n}
{n}Inside it is warm. Warmer than any hall in Drezen. She has lain down around the whole of the tower floor, and her body is the wall, and her wing is the roof, and the storm is somewhere very far away.{/n}''',
        c("Continue", "her")),
    dv("her", '''"Sit," {n}she says.{/n} "There. Against me." {n}Her flank is hot as a banked hearth through your wet clothes.{/n} "You are cold. Crusaders are always cold. You eat bread and wear iron and wonder why." {n}The wing settles lower, and the dark closes in, warm and close and smelling of forge-smoke and rain.{/n} "Sleep, if you want. I will not bite. It is not the day."''',
       c("[Sleep against her.]", "sleep"),
       c('"Why did you call me up in the storm?"', "why")),
    dv("why", '''{n}The storm answers first, all around the wing.{/n} "Because in the lair, before, there was a storm like this, and I lay alone under the rock and listened to the thunder and was not afraid of it, and it was very dull." {n}Her breath stirs your wet hair.{/n} "And tonight I wanted to find out whether it would still be dull with a thing beside me that I could frighten. It is not. Sleep."
{n}You close your eyes. A claw lifts your chin before you are halfway under, no harder than a fingertip.{/n}
"No." {n}The great head lowers over you.{/n} "I said sleep. I changed my mind. It is mine to change." {n}Her breath is a furnace across your wet shirt, and the heat draws steam out of the cloth.{/n} "Take that off. It is cold and it stinks of rain. You will not be cold under me."
{n}You peel the soaked clothes away piece by piece, and she watches without blinking, one eye, orange, an arm's length from your face. Each time you stop she makes a low sound of impatience in her throat. Her tail is around you before the last of it hits the floor, drawing you across the stone into the hollow beneath the wing, against the roaring heat of her belly. Scales ridged and smooth against your bare skin, her claws shifting on the stone either side of you, her breath all down your back.{/n}
"Frightened?" {n}It rumbles through your ribs.{/n} "Good. Dull would be an insult. Put your hands on me and stay frightened."
{n}You do. She shudders under them, from the throat to the tail. The wing shuts out the storm, and she pulls you in underneath her.{/n}''',
       c("[Sleep against her.]", "sleep")),
    nar("sleep", '''{n}You sleep. Sometime in the night you wake, and the storm is still raging somewhere beyond the wing, and her great head has come around in the dark and is resting on the floor beside you, one eye half-open, orange as a coal, watching you breathe.{/n}
{n}When she sees that you are awake she closes it, deliberately, and pretends to be asleep until the morning.{/n}''',
        c('"..."', flags=(SHELTERED,))),
], requires=(COMMITTED, BITTEN_ONCE), forbids=(SHELTERED,), delay=96)


# --- 21. A visit before the final march (Chapter 5, after the commit) --------------------------------------------------

hub(T + "before_the_end", "What you still owe", '"I\'m going somewhere I might not come back from. I want to see her."', [
    teller("start", '''"I know where you are going. Everyone in Drezen knows; they only pretend not to, so they can sleep." {n}He stands, which he rarely does for anyone.{/n} "I will walk you to the foot of the ridge. I would like you to know, Commander, that whatever happens, the story is a good one. I am not flattering you. I am a professional."''',
        c("Continue", "climb")),
    dv("climb", '''"You are going to the end of the world." {n}She does not ask; she has heard the city.{/n} "To the place where the Wound goes all the way down. And you have come to tell me before you go." {n}Her eye does not leave you.{/n} "Good. You can be taught."''',
       c('"If I don\'t come back, the tower is yours. It always was."', "if"),
       c('"I\'ll come back. I owe you the end."', "owe", forbids=(FLOWN,)),
       c('"I\'ll come back. I owe you the end."', "owe_free", requires=(FLOWN, BITTEN_ONCE,))),
    dv("if", '''{n}The wing comes around you before you finish, not hard, just close, closing you in against her.{/n} "If you do not come back," {n}she says, very quietly,{/n} "I will go down there and find what is left of you and bring it back up this mountain and eat it, so that nothing else can. That is what I do with what is mine." {n}The wing tightens.{/n} "So do not make me. I would not enjoy it. That is the first time I have ever said so about a meal."''',
       c("Continue", "end_her")),
    dv("owe", '''"You owe me the end." {n}The laugh, soft, like a forge drawing breath.{/n} "Yes. You have been paying it in pieces since I got up, and you are not finished, and a thing that is still paying cannot die. I decided that the night you first owed me. I meant it as a threat." {n}She lowers her head until her brow rests against yours, hot as a forge stone.{/n} "It is still a threat. Come back and pay."''',
       c("Continue", "end_her")),
    dv("end_her", '''"Go down. When you leave Drezen, look back." {n}She lifts her head above the broken wall.{/n} "I want you to see how much of the sky I fill."''',
       c("[Go down the mountain. Look back.]", flags=(LAST_NIGHT,))),
    dv("owe_free", '''"You owe me the end." {n}The laugh, soft, like a forge drawing breath.{/n} "Yes. You have been paying it in pieces since I flew from you, and you are not finished, and a thing that is still paying cannot die. I decided that the night you first owed me. I meant it as a threat." {n}She lowers her head until her brow rests against yours, hot as a forge stone.{/n} "It is still a threat. Come back and pay."
{n}The wing comes down over you both, and the dark under it is the dark of a banked furnace. Her breath rolls over your face and throat. Her tail climbs your leg without asking and winds around your thigh, and her great head turns, slowly, so that her jaw drags along your shoulder, the teeth a finger-width from the skin and held there.{/n}
"A creditor collects before the debtor can die," {n}she says.{/n} "Take your clothes off, and let me count what I am owed."
{n}You do, with her eye on every inch of it. She draws you in against her belly, scales ridged and blistering under your bare palms, her whole body shifting to fit you, the claws on the floor grinding as you press your hands to the seam of hide where the heat is worst. She makes a sound you have never heard from anything that lives, and holds you hard against her, and tells you in her low forge-voice exactly whose you are.{/n}''',
       c("Continue", "end_her")),
], requires=(COMMITTED,), forbids=(LAST_NIGHT,), delay=120, chapters=(5,))


NAMED = T + "name_given"
FED = T + "meal_shared"
SEAM = T + "seam_touched"
HUNTED_TOGETHER = T + "hunted_together"
DROVERS = T + "drovers_settled"
BOOK = T + "garrison_book"
TELLER_VIEW = T + "storyteller_view"


# --- 22. The drovers (after the return): the quartermaster's list of oxen ---------------------------------------------

hub(T + "the_drovers", "Four oxen and a list", '"Why is the quartermaster sending the drovers to you?"', [
    teller("start", '''"Because the drovers went to the quartermaster about the oxen, and the quartermaster went up the ridge with a list, and came down again very quickly without the list." {n}The Storyteller sounds as if he is enjoying himself.{/n} "Wilcer Garms is a brave man with a ledger, Commander, but he is not brave enough for a dragon who reads upside down. He has decided the matter is diplomatic, and that diplomacy is my department. I have decided it is yours."''',
        c("Continue", "drovers")),
    nar("drovers", '''{n}The drovers are three brothers from the east road, weathered and furious, with their hats in their hands and their fear in the set of their shoulders. They lost four oxen and a cart to the grey dragon in one morning, and they want paying, and they have heard that the Commander is the one who talks to it.{/n}''',
        c('[Pay them from the war chest] "The crusade will make it good."', "paid", crusade=("Finances", -50)),
        c('"Take it up with her. She\'s on the ridge."', "her"),
        c('[Promise them she\'ll stay off the east road] "It won\'t happen again. I\'ll see to it."', "promise")),
    teller("paid", '''{n}The brothers go away with their purse, bowing, and the Storyteller waits until the door has shut.{/n} "She will hear of it, you know. She hears everything that is said about food." {n}A pause.{/n} "You have paid for her dinner, with the crusade's coin. When I tell her, she will either be insulted or she will order more oxen. I will carry her reply when she gives one."''',
        c("Continue", "end")),
    teller("her", '''{n}The brothers look at each other, and then at you, and then leave without their compensation and without another word.{/n}
"That," {n}the Storyteller says,{/n} "was cruel, and fair, and very like her. She will be delighted when I tell her." {n}He turns his cup, and does not look pleased.{/n} "She says that a thing that walks where she eats has made its choice. I would not have said it to their faces. You did. Three brothers will tell that on the east road for the rest of their lives, and they will not tell it kindly."''',
        c("Continue", "end")),
    teller("promise", '''{n}The brothers go away satisfied, and the Storyteller sighs.{/n} "You promised them she would stay off the east road." {n}He sighs.{/n} "Commander, she will hear that too. She will hear that you promised something about her, to strangers, without asking. I will carry her answer down when she gives it. I do not think it will be about oxen."''',
        c("Continue", "promise_her")),
    teller("promise_her", '''{n}He goes up the next morning and comes back at noon.{/n} "She says: 'The Commander may promise whatever it likes about the east road. I have not eaten on the east road since the first morning. I have been eating on the north road. Tell the Commander I was being polite, and that it has now spoiled it by noticing.'" {n}He does not smile.{/n} "The north-road drovers have not been compensated. I thought you should know whose road it is now."''',
        c("Continue", "end")),
    teller("end", '''"The drovers have their answer." {n}He sets his cup down.{/n} "And all three are still alive. If she sends for them, Commander, I suggest you send soldiers with them."''',
        c('''"I'll remember that."''', flags=(DROVERS,))),
], requires=("trickster.ever", RETURNED), forbids=(DROVERS,), delay=36)


# --- 23. Her name (after her questions): what the Commander may call her -----------------------------------------------

hub(T + "her_name", "What to call her", '"She\'s asked for me again?"', [
    teller("start", '''"She has. She says it is a matter of names, and that I am not to come up with you, and that if I listen from the bottom of the ridge she will know." {n}He shakes his head.{/n} "I will not listen. I have heard her say names before. It is not something one wants to hear twice."''',
        c("Continue", "climb")),
    dv("climb", '''"You answered my three questions." {n}She is sitting upright in the ruin for once, her head level with the broken top of the wall, the city behind her.{/n} "The old man carried them up word for word. You lied in one of them. I will not tell you which; it is more fun if you have to wonder." {n}Her eye settles on you.{/n} "Now. What do you call me, when you talk about me to your people?"''',
        c('"The dragon."', "dragon"),
        c('"Devarra."', "devarra"),
        c('"Mine."', "mine")),
    dv("dragon", '''"The dragon." {n}She sounds disappointed, and a little relieved.{/n} "As if there were only one." {n}She considers it, and decides she likes it.{/n} "Good. When you say 'the dragon' in front of your people, they will think of me, and they will look up at the ridge, and they will be afraid. Call me that. It frightens them properly."''',
       c("Continue", "name")),
    dv("devarra", '''{n}The whole tower goes still.{/n} "Where did you hear that?" {n}She does not wait.{/n} "No. I know where. The crusade writes everything down; somewhere there is a clerk who wrote 'the dragon Devarra' in a book, as if a name were a thing you could own because you had spelled it." {n}Smoke curls from her nostrils.{/n} "You said it to my face. That is different. Say it again, and I will decide whether you may."''',
       c("Continue", "name")),
    nar("mine", '''{n}The wing moves, fast, and stops a finger's breadth from your throat. It hangs there. She does not strike.{/n}''',
        c("Continue", "mine_2", forbids=(FLOWN,)),
        c("Continue", "mine_2_free", requires=(FLOWN,))),
    dv("mine_2", '''"You would say that to me." {n}Her voice is very soft.{/n} "After everything. You, of all things, who kept the saws off my carcass and paid for your life with a story about what I was." {n}The wing withdraws, slowly.{/n} "I will let it pass, because I have decided I like your nerve better than your manners. But understand me: I am not yours. You are mine. You are the thing I have decided to keep. That is not the same, and one day it will matter which of us said it."''',
       c("Continue", "name")),
    dv("name", '''"Here is my name, then. The true one." {n}She says a word in Draconic, low, that goes on and on and seems to have fire in the middle of it, and the stones of the tower hum with it after she stops.{/n} "Nobody living has heard that. I have given it to no one before." {n}She watches you.{/n} "You will not be able to say it. Your mouth is the wrong shape. That is the point. It is not for saying. It is for knowing."''',
       c('"Then I\'ll know it."', "know"),
       c('"Why give it to me?"', "why", forbids=(FLOWN,)),
       c('"Why give it to me?"', "why_free", requires=(FLOWN,))),
    dv("know", '''"Yes." {n}She lowers her head.{/n} "Know it. And when you tell the next lie about me, remember that you know what I am called, and that I did not have to tell you." {n}Her eye closes.{/n} "Go down now. I have said enough for one year."''',
       c("[Go down the mountain.]", flags=(NAMED,))),
    dv("why", '''"Because you named me once already, in a story you told without asking, and I paid for it with your life, which I did not take." {n}Her breath is hot on your face.{/n} "It seemed only fair that you should know what you were naming. Next time, crusader, if there is a next time, you will know what you are doing." {n}She settles.{/n} "Go down. I have said enough for one year."''',
       c("[Go down the mountain.]", flags=(NAMED,))),
    dv("mine_2_free", '''"You would say that to me." {n}Her voice is very soft.{/n} "After everything. You, of all things, who told me a fable from behind a rock and walked into Xanthir's house in my name." {n}The wing withdraws, slowly.{/n} "I will let it pass, because I have decided I like your nerve better than your manners. But understand me: I am not yours. You are mine. You are the thing I have decided to keep. That is not the same, and one day it will matter which of us said it."''',
       c("Continue", "name")),
    dv("why_free", '''"Because you told my story once already, from behind a rock, before you had any right to it, and I paid for it with your life, which I did not take." {n}Her breath is hot on your face.{/n} "It seemed only fair that you should know whose story it was. Next time, crusader, if there is a next time, you will know what you are doing." {n}She settles.{/n} "Go down. I have said enough for one year."''',
       c("[Go down the mountain.]", flags=(NAMED,))),
], requires=(QUESTIONED,), forbids=(NAMED,), delay=48)


# --- 24. The meal (after the first climb): she cooks --------------------------------------------------------------

hub(T + "the_meal", "Dinner on the ridge", '"She\'s invited me to dinner?"', [
    teller("start", '''"She has invited you to dinner. She was very precise: you are to bring nothing, you are to be hungry, and you are not to ask what it is." {n}He clears his throat.{/n} "I asked, on your behalf. She said it had four legs and one head and had never been to Drezen, and that this was all I needed to know, and that I was not invited. I confess I was relieved."''',
        c("Continue", "climb")),
    nar("climb", '''{n}There is a whole stag turning on a spit of broken spear shafts in the middle of the tower floor, and no fire under it. She is lying with her chin on her claws beside it, breathing on it slowly, patiently, in a long thin stream of flame that she moves from end to end as carefully as a cook with a basting brush.{/n}
{n}The smell of roast meat fills the ruin and goes straight past your nose to your stomach.{/n}''',
        c("Continue", "her")),
    dv("her", '''"Sit. Do not touch it." {n}She moves the thin flame along the stag's flank.{/n} "I can smell your kitchens from here. Burned fat and raw meat. Your crusade ruins its cattle before eating them." {n}She turns one eye toward you.{/n} "Tell me what you want. Not the leg. The leg is mine."''',
       c('"Whatever you give me."', "give"),
       c('"The heart."', "heart"),
       c('"I thought you only ate people."', "people")),
    dv("give", '''"Whatever I give you." {n}She is amused.{/n} "That is a dangerous thing to say to a dragon at dinner." {n}She tears off a strip of shoulder with one claw, hot and dripping, and drops it on a flat stone in front of you like a hound bringing back a bird.{/n} "Eat. And then tell me whether it is better than your cooks. I will know if you lie."''',
       c("Continue", "eat")),
    dv("heart", '''{n}She stops breathing on the stag and looks up at you.{/n} "The heart." {n}Something in her eye changes.{/n} "In my lair, the one who takes the heart of the first kill is the one who stands at the mouth of the cave. That is my rule. I made it." {n}She reaches into the stag, very neatly, and takes it out, and puts it down in front of you, steaming.{/n} "I do not suppose you knew that. Eat it anyway. I will not tell you what it means twice."''',
       c("Continue", "eat")),
    dv("people", '''"People are tough, and they talk, and they never season themselves properly." {n}She rolls the stag over with one claw.{/n} "I eat people when people deserve it, or when people are in the way, or when I am bored. Stags I eat because they are delicious. You should know the difference, crusader, since you have been on the list of the first kind and are now, apparently, a guest." {n}She tears off a piece.{/n} "Eat."''',
       c("Continue", "eat")),
    nar("eat", '''{n}It is smoky and tender all the way through, cooked so evenly that there is not one burned edge on it.{/n}
{n}She watches every mouthful go down, the way she watches the east road from the sill: to see what it does next.{/n}''',
        c('"It\'s better than my cooks."', "better")),
    dv("better", '''"It is better than your cooks." {n}She turns back to the stag, satisfied.{/n} "Of course it is. I told you." {n}She tears off the leg, the one that was hers, and eats it in two bites.{/n} "You may come to dinner again. Bring nothing. Be hungry. Do not bring the old man; he talks with his mouth full, and his stories are better cold."''',
       c("[Stay until the stag is bones.]", flags=(FED,))),
], requires=(CLIMBED,), forbids=(FED,), delay=48)


# --- 25. The soft place (after the itch): the seam under the wing -----------------------------------------------------

hub(T + "the_soft_place", "Where the blade went in", '"She sent for me again. Not about food, I suppose."', [
    teller("start", '''"Not about food." {n}He does not smile.{/n} "She said to tell you to come alone, and to come unarmed, and to come in daylight. I asked her why daylight. She said, 'So that the Commander can see exactly what I am showing it.'" {n}He turns his face toward the ridge.{/n} "Leave your sword with me, Commander. I will keep it for you. I have kept worse things for worse people."''',
        c("Continue", "climb", forbids=(FLOWN,)),
        c("Continue", "climb_free", requires=(FLOWN,))),
    nar("climb", '''{n}She is lying on her side in the sun on the tower floor, one wing lifted and held high, like a sail, like a door propped open. Under it, low on her flank where the new grey hide is thinnest, is the seam: a long pale ridge where the killing blow went in and the moult grew over it.{/n}
{n}She does not look at you. She is looking at the sky.{/n}''',
        c("Continue", "her")),
    dv("her", '''"There." {n}Her voice is flat and quiet.{/n} "The one soft place. Steel found it. I have spent three hundred years making certain nobody else ever could, and now it is there again, on a new body, in the same place, because that is where you killed me and the moult remembered." {n}A long breath.{/n} "Put your hand on it."''',
       c("[Put your hand on it.]", "touch"),
       c('"Why are you showing me this?"', "why")),
    dv("why", '''"Because now you know where it is, because I am showing you. If you ever want to kill me again, you will not need to look for it." {n}She still does not look at you.{/n} "So I am showing you, in daylight, with my wing up, and your sword at the bottom of the mountain, and my teeth a length from your neck. Put your hand on it. Then we will see which of us is quicker."''',
       c("[Put your hand on it.]", "touch")),
    nar("touch", '''{n}The seam is hot under your palm, hotter than the rest of her, and softer: soft enough that you can feel her heartbeat through it, huge and slow and very steady, the heartbeat of something that could crush you by rolling over in its sleep.{/n}
{n}Under your hand it speeds up. Only a little. Only for a moment. Then she makes it slow down again, deliberately, and you feel her do it.{/n}''',
        c("Continue", "after")),
    dv("after", '''"There," {n}she says, very quietly, and the teeth come a little closer to your neck.{/n} "Now take your hand away, crusader. Slowly." {n}You do not. The wing comes down, slowly, over your arm, over your shoulder, until you are standing in the grey dark under it with your hand still on her side.{/n} "Do not ever tell anyone about this. Not the old man. Not your generals. Not the other things you love. This one is mine."''',
       c('"I won\'t."', "wont")),
    dv("wont", '''"No. You will not." {n}She lifts the wing again, and the daylight comes back.{/n} "You are a liar and a thief and you have never kept a secret in your life that you could sell. But you will keep this one." {n}Her eye turns to you at last.{/n} "I know, because I am the secret. Go down. Get your sword back from the old man before he starts telling stories about it."''',
       c("[Go down the mountain.]", flags=(SEAM,))),
    nar("climb_free", '''{n}She is lying on her side in the sun on the tower floor, one wing lifted and held high, like a sail, like a door propped open. Under it, low on her flank where the scales are thinnest, is the scar: a long pale ridge where your fight opened her to the ribs, and she flew on it, and it closed the way it pleased.{/n}
{n}She does not look at you. She is looking at the sky.{/n}''',
        c("Continue", "her_free")),
    dv("her_free", '''"There." {n}Her voice is flat and quiet.{/n} "The one soft place. In my lair it was under the wing too, and your people found it. I have spent three hundred years making certain nobody else ever could, and now there is a seam over it, and the seam is thinner than the scale was." {n}A long breath.{/n} "Put your hand on it."''',
       c("[Put your hand on it.]", "touch"),
       c('"Why are you showing me this?"', "why_free")),
    dv("why_free", '''"Because now you know where it is, because I am showing you. If you ever want to finish what your people started in my lair, you will not need to look for it." {n}She still does not look at you.{/n} "So I am showing you, in daylight, with my wing up, and your sword at the bottom of the mountain, and my teeth a length from your neck. Put your hand on it. Then we will see which of us is quicker."''',
       c("[Put your hand on it.]", "touch")),
], requires=(SCRAPED,), forbids=(SEAM,), delay=48)


# --- 26. The hunt (after the commit): she takes the Commander hunting -----------------------------------------------

hub(T + "the_hunt", "Hunting at the edge", '"She wants to take me hunting?"', [
    teller("start", '''"At the edge of the Wound. At dawn. On her back." {n}He has clearly been instructed to say exactly this and nothing else, and it pains him.{/n} "She says that a thing she has decided to keep should know how she eats, since it will be watching her do it for years. She says you may bring a weapon. She says you will not need it, and that she will be offended if you use it."''',
        c("Continue", "flight")),
    nar("flight", '''{n}You fly north in the grey before sunrise, low and fast over the dead ground, until the air starts to taste of copper and ash and the earth below turns cracked and wrong. She lands on a black ridge without a sound, and crouches, and you slide down from her shoulder into the grit beside her.{/n}
{n}Below, in a hollow, a pack of babaus is feeding on something that was a Mendevian outrider this morning, to judge by the boots. There are nine of them. She watches them the way a cat watches a bird that has not yet noticed the cat.{/n}''',
        c("Continue", "wait")),
    dv("wait", '''"Watch," {n}she breathes, and her whisper is still loud enough to lift the dust.{/n} "Not the killing. Anyone can kill. Watch the waiting."
{n}She does not move for a long, long time. The sun comes up behind you and stretches her shadow down the ridge, toward the hollow, a little at a time, and she lets it, until the very tip of it touches the nearest babau's heel.{/n}''',
        c("Continue", "strike")),
    nar("strike", '''{n}Then she goes. It is not a charge; it is a fall, a grey weight dropping out of the dawn onto the hollow, and the first four babaus are dead before the other five understand what the shadow was. The rest do not last much longer. She kills the last one slowly, pinning it with one claw and watching it struggle, and then she stops, and looks up the ridge at you.{/n}''',
        c("Continue", "offer")),
    dv("offer", '''"Come down." {n}Her muzzle is black to the eyes.{/n} "On my mountain, the one I keep is given the first bite of the kill, so that everyone watching knows. My rule." {n}She pushes the dead demon a little toward you with her claw.{/n} "Nobody is watching. Take it anyway. Or do not. I am curious which."''',
       c('[Take the first bite, and hold her eye while you do.]', "bite"),
       c('"I\'ll take the gesture. Not the demon."', "gesture")),
    dv("bite", '''{n}It is foul, and you do it anyway, and you do not look away from her while you do.{/n}
"Hah." {n}The laugh comes out of her with a gust of hot breath that smells of the hunt.{/n} "You would. Of course you would. You would eat a demon at dawn to win an argument with a dragon." {n}She lowers her head until her black muzzle is next to your face.{/n} "Good. Now everyone who is not watching knows."''',
       c("Continue", "home")),
    dv("gesture", '''"The gesture." {n}She considers you, and then the demon, and then you again, and her lip lifts.{/n} "Too delicate for demon meat. Very well. I shall take your share, and you will watch me take it." {n}She eats the demon herself, in three bites, slowly, with her eye on you the whole time.{/n} "Next time I offer you the first bite, crusader, I will not offer twice."''',
       c("Continue", "home")),
    nar("home", '''{n}She flies you home in the full morning light, slow and heavy with the hunt, and brings you down on the ridge above the city just as the bells of Drezen start for the morning service. On the wall the sentries are watching; they have been watching since dawn. She lets them.{/n}''',
        c("[Go down the mountain.]", flags=(HUNTED_TOGETHER,))),
], requires=(COMMITTED,), forbids=(HUNTED_TOGETHER,), delay=72)


# --- 27. The garrison's book (after the first climb): the soldiers are betting -----------------------------------------

hub(T + "the_garrison_book", "The odds", '"Why are the soldiers on the north wall so interested in my health?"', [
    teller("start", '''"Because the soldiers on the north wall have been running a book on you since the first time you climbed the ridge." {n}He says it with a great deal of pleasure.{/n} "The odds on your coming back down alive were eight to one against, when the book opened. They are now level. The man who runs the book asked me whether I had inside information. I said I was blind. He said that was why he asked."''',
        c('"Who\'s betting against me?"', "against"),
        c('"What are the odds on her?"', "on_her")),
    teller("against", '''"Most of the old soldiers, who have seen dragons before. Most of the chaplains, on principle. And one of your generals, very heavily, which I think you should know." {n}He smiles.{/n} "Betting for you: the young soldiers, who have not seen dragons before, and the quartermaster, who says the crusade cannot afford to lose its Commander to a lizard and has bet accordingly, as a point of order."''',
        c("Continue", "tell_her")),
    teller("on_her", '''"There is a separate book on her. The question is not whether she will eat you. The question is whether she will ever come down into the city." {n}He taps his stick once on the floor.{/n} "Nobody has bet that she will. The odds are a hundred to one. I have considered placing a small wager myself. I am a storyteller; I know when a story is heading somewhere."''',
        c("Continue", "tell_her")),
    teller("tell_her", '''"Shall I tell her? About the book?" {n}He tilts his head.{/n} "I warn you: she will want to know the odds, and she will want to know who is betting against you, and she will want their names."''',
        c('"Tell her. Leave out the names."', "tell"),
        c('"Don\'t. Let them have their fun."', "dont")),
    teller("tell", '''{n}He goes up that evening and comes back laughing, silently, his shoulders shaking.{/n} "She wanted to know the odds. I told her. She said, 'Level? Level? After everything?' She was so offended on your behalf that she flew over the north wall at dawn, very low, very slowly, and looked at each of the soldiers in turn." {n}He wipes his eyes.{/n} "The odds are now three to one in your favour. The book on her coming down into the city has been closed, as nobody will take the other side."''',
        c("Continue", "end")),
    teller("dont", '''"Let them have their fun." {n}He nods.{/n} "A garrison that is betting on its Commander's visits to a dragon is not a garrison that is counting the demons beyond the wall." {n}He settles back.{/n} "I will not tell her. She will find out anyway. She always does. But it will not have been me."''',
        c("Continue", "end")),
    teller("end", '''"In any case, I have placed my wager." {n}He folds his hands.{/n} "I will not tell you which book. A storyteller must keep some things back, or nobody will pay for the ending."''',
        c('"Fair."', flags=(BOOK,))),
], requires=(CLIMBED,), forbids=(BOOK,), delay=96)


# --- 28. The Storyteller's view (after the commit): what the messenger thinks -----------------------------------------

hub(T + "the_messenger", "What the messenger thinks", '"You\'ve carried every message between us. What do you think of it?"', [
    teller("start", '''{n}When he answers, he does not look toward the ridge.{/n} "I think that she held me in that lair for days, deciding how I would taste, and that I paid for my life with the best story I had, and that I have not slept well since. I think that you gave her a new body to be hungry in, and I said some stories should be allowed to end, and I meant it."''',
        c("Continue", "but")),
    teller("but", '''"And I think that I have climbed that ridge more times than I can count, carrying her threats down and your jokes up, and that somewhere on the way I stopped being afraid of her." {n}He tilts his head toward the ridge.{/n} "Not because she is less dangerous. She is more. She waits for your footsteps now, and the north watch still counts the men it lost to her. I cannot tell you which of those she will think of first, on the day it matters. Neither can she, I suspect."''',
        c('"Do you forgive her?"', "forgive"),
        c('"Do you forgive me?"', "forgive_me")),
    teller("forgive", '''"Forgive her?" {n}He laughs, a dry, surprised sound.{/n} "No. I am an old man, and she tried to eat me, and I am allowed to hold that for the rest of my life. But I will tell you what she asked me, Commander." {n}He leans forward.{/n} "The last time I went up, she asked me for the end of a story I had never started. I told her I would make one up. She said she would wait. I left before she changed her mind. I am not sure, even now, that waiting was not a threat."''',
        c("Continue", "end")),
    teller("forgive_me", '''"You?" {n}He considers it with great seriousness.{/n} "You told a lie over her body, and she paid for it as if it were a story, because to her there is no difference. She tells it differently every time she tells it, and so, I notice, do you. That is a terrible thing to do to a story." {n}He does not smile.{/n} "And every one of them was a very good story. That does not bring back the two men of the north watch, or whatever she ate on the north road last week. Ask me again when I have heard the ending."''',
        c("Continue", "end")),
    teller("end", '''"I have carried her messages. The climb is yours." {n}He waves you away.{/n} "And when all this is over, however it ends, for you or for her, I would like to hear it. I will pay full price."''',
        c('"You\'ll have it free."', flags=(TELLER_VIEW,))),
], requires=(COMMITTED,), forbids=(TELLER_VIEW, FLOWN), delay=96)


hub(T + "the_messenger_free", "What the messenger thinks", '"You\'ve carried every message between us. What do you think of it?"', [
    teller("start", '''{n}When he answers, he does not turn toward the ridge.{/n} "She held me in that lair for days, deciding how I would taste. I paid for my life with a story. You offered her a bargain, and she flew wounded rather than answer the stone. Now she is above Drezen, hungry, and the north watch counts the men it has lost to her. You ask what I think? I think of the people who have to live below that ridge."''',
        c("Continue", "but")),
    teller("but", '''"And I think that I have climbed that ridge more times than I can count, carrying her threats down and your jokes up, and that somewhere on the way I stopped being afraid of her." {n}He tilts his head toward the ridge.{/n} "Not because she is less dangerous. She is more. She waits for your footsteps now, and the north watch still counts the men it lost to her. I cannot tell you which of those she will think of first, on the day it matters. Neither can she, I suspect."''',
        c('"Do you forgive her?"', "forgive"),
        c('"Do you forgive me?"', "forgive_me")),
    teller("forgive", '''"Forgive her?" {n}He laughs, a dry, surprised sound.{/n} "No. I am an old man, and she tried to eat me, and I am allowed to hold that for the rest of my life. But I will tell you what she asked me, Commander." {n}He leans forward.{/n} "The last time I went up, she asked me for the end of a story I had never started. I told her I would make one up. She said she would wait. I left before she changed her mind. I am not sure, even now, that waiting was not a threat."''',
        c("Continue", "end")),
    teller("forgive_me", '''"You?" {n}He considers it with great seriousness.{/n} "You told a fable over my head to a dragon who had her claw round my ankle, and she paid for it as if it were a story, because to her there is no difference. She tells it differently every time she tells it, and so, I notice, do you. That is a terrible thing to do to a story." {n}He does not smile.{/n} "And every one of them was a very good story. That does not bring back the two men of the north watch, or whatever she ate on the north road last week. Ask me again when I have heard the ending."''',
        c("Continue", "end")),
    teller("end", '''"I have carried her messages. The climb is yours." {n}He waves you away.{/n} "And when all this is over, however it ends, for you or for her, I would like to hear it. I will pay full price."''',
        c('"You\'ll have it free."', flags=(TELLER_VIEW,))),
], requires=(COMMITTED, FLOWN), forbids=(TELLER_VIEW,), delay=96)


HOARD = T + "hoard_moved"
COIN_STOLEN = T + "coin_stolen"
COIN_ASKED = T + "coin_asked"
BONES = T + "bones_counted"
FEAR = T + "fear_spoken"
ROOF = T + "on_the_roof"


# --- 29. The hoard (after the first climb): the old lair and what she left in it ----------------------------------

hub(T + "the_hoard", "What she left in the lair", '"She wants to go back to her old lair?"', [
    teller("start", '''"She wants her hoard." {n}He says it as though announcing a natural disaster.{/n} "It is still in the lair where she held me, under the rockfall at the back. She did not take it when she left the old lair. She wants it brought to the watchtower, all of it, and she wants you to help." {n}He pauses.{/n} "I told her she had never let anyone near her hoard. She said, 'That is why it has to be the Commander. I want to see what it does.'"''',
        c("Continue", "lair")),
    nar("lair", '''{n}She leads you down into the old lair: the broken rock, the old bones, and the flat stone where, the Storyteller says, he sat and told his story with a dragon's claw curled around his ankle. She digs out the rockfall at the back in a few minutes, flinging boulders down the gorge like pebbles.{/n}
{n}Behind it the hoard glows. Coin of four kingdoms, most of them fallen. A crown with the stones prised out. Sarkorian torcs, a dwarven helm, a set of silver spoons, a child's wooden horse with a gold bridle painted on it. It is not as large as the songs say a dragon's hoard should be. It is very carefully arranged.{/n}''',
        c("Continue", "her")),
    dv("her", '''"Three hundred years." {n}She stands over it with her wings half raised, like a hen over a nest.{/n} "Every piece of it taken from something that thought it was stronger than me." {n}Her eye swings to you.{/n} "Now. You will carry it up the ridge, a sack at a time, on your own back, and I will watch you do it, and we will both see how much of it arrives."''',
        c('[Carry it all. Every coin.]', "honest"),
        c('[Carry it all, and palm one coin on the way.]', "steal", flags=(COIN_STOLEN,)),
        c('"Can I have one coin? Ask first, like a person."', "ask", flags=(COIN_ASKED,), forbids=(FLOWN,)),
        c('"Can I have one coin? Ask first, like a person."', "ask_free", flags=(COIN_ASKED,), requires=(FLOWN,))),
    nar("honest", '''{n}She flies the hoard to the foot of the ridge in two loads, the sacks swinging from her claws; the ridge is your part. It takes eleven climbs and the whole of a day. You carry every coin, every spoon, the crown, the torcs, and the wooden horse last of all, and you set each sack down on the tower floor in front of her and go back for the next.{/n}
{n}She counts it all when you have finished, with one claw, very slowly. Then she counts it again.{/n}''',
        c("Continue", "honest_her")),
    dv("honest_her", '''"All of it." {n}She sounds almost offended.{/n} "You carried three hundred years of gold up a mountain on your own back, and you did not take one coin." {n}She looks at you with something close to suspicion.{/n} "Either you are an honest thing, crusader, which I refuse to believe, or you are playing a longer game than I can see. I will find out which. I have time."''',
       c("Continue", "end")),
    nar("steal", '''{n}On the fourth climb you let one coin slip from the sack into your sleeve: a small gold piece from a kingdom that no longer exists, with a queen's head on it. It slides into your sleeve without a sound.{/n}
{n}She counts it all when you have finished, with one claw, very slowly. Then she looks at your sleeve.{/n}''',
        c("Continue", "steal_her")),
    dv("steal_her", '''"One." {n}Her voice is perfectly calm.{/n} "The Queen of Iobaria. I took her from a bandit who took her from a merchant who took her from a tomb. She has been stolen more often than she was ever spent." {n}Her eye does not move from your sleeve.{/n} "Keep her. You earned her; nobody has ever stolen from me and lived to be caught. That was the price of seeing what you would do. Now I know."''',
       c("Continue", "end")),
    dv("ask", '''{n}She stares at you as though you had grown a second head.{/n} "Ask." {n}It comes out of her like a cough of smoke.{/n} "You are a thief. You stole my carcass out from under the hunters. And you ask me, for one coin, like a child at a table." {n}Then she puts one claw into the hoard and slides out a single gold piece with a queen's head on it, and pushes it toward you across the floor.{/n} "Take it. And now carry the rest."''',
       c("Continue", "ask_2")),
    nar("ask_2", '''{n}She flies the hoard to the foot of the ridge in two loads; the ridge is your part. It takes eleven climbs and the whole of a day. She counts it all when you have finished, twice. Then she looks at the gold piece, which you have been carrying in your hand the whole time, turning it over.{/n}''',
        c("Continue", "ask_her")),
    dv("ask_her", '''"Nobody has ever been given anything from my hoard." {n}She lays her head down beside the heap of gold.{/n} "Taken, yes. Every coin there was taken. That one was given. It is the only one I gave." {n}Her eye closes.{/n} "Do not spend it. I will know. And one day I will ask for something out of your hoard, crusader, and before you answer you will remember that coin."''',
       c("Continue", "end")),
    teller("end", '''{n}At the bottom of the ridge that night, the Storyteller asks how it went, and listens without interrupting.{/n} "In the lair," {n}he says at last,{/n} "she told me that her hoard was the only thing in the world she loved. I believed her. I think it was true, then." {n}He turns his face toward the ridge.{/n} "When she lets you carry her hoard up a mountain she is not trusting you, Commander. She is counting it, and you with it."''',
        c('"..."', flags=(HOARD,))),
    dv("ask_free", '''{n}She stares at you as though you had grown a second head.{/n} "Ask." {n}It comes out of her like a cough of smoke.{/n} "You are a thief. You walked into Vang's house and talked to his stone. And you ask me, for one coin, like a child at a table." {n}Then she puts one claw into the hoard and slides out a single gold piece with a queen's head on it, and pushes it toward you across the floor.{/n} "Take it. And now carry the rest."''',
       c("Continue", "ask_2")),
], requires=(CLIMBED,), forbids=(HOARD,), delay=72)


# --- 30. The bones (after the first climb): what each one was ------------------------------------------------------

hub(T + "the_bones", "Sorted by size", '"What does she do up there all day?"', [
    teller("start", '''"She sorts her bones." {n}He is not joking.{/n} "Smallest at the door, largest at the back. Every morning, she moves them. I asked her why once. She said, 'So that I remember which ones I have not finished.' I did not ask what she meant. She has asked for you, today. She says you should know what is on her floor, since you walk across it so carelessly."''',
        c("Continue", "climb")),
    dv("climb", '''"Sit. Pick one." {n}She sweeps her claw across the floor, over the bones laid out in their long neat rows.{/n} "Any one. I will tell you what it was. Every one of them has a story; the old man taught me that, in the lair, while he was trying not to be one of them."''',
        c('[Pick up a small, delicate bone near the door.]', "small", forbids=(FLOWN,)),
        c('[Pick up a huge, blackened thighbone from the back.]', "large", forbids=(FLOWN,)),
        c('[Pick up a bone with a crusader\'s ring still on it.]', "ring"),
        c('[Pick up a small, delicate bone near the door.]', "small_free", requires=(FLOWN,)),
        c('[Pick up a huge, blackened thighbone from the back.]', "large_free", requires=(FLOWN,))),
    dv("small", '''"A bird." {n}She sounds pleased.{/n} "A crow, from where I died. It sat by the carcass all three days, and it was the only thing your guards did not trouble to chase off. I ate it the first morning I was alive again, because it had been waiting to eat me." {n}Her lip lifts.{/n} "I kept the bones to remind me that everything waits for everything else to die. Even the little things. Especially the little things."''',
       c("Continue", "then")),
    dv("large", '''"A vrock." {n}She looks at it with great fondness.{/n} "The first demon I killed after I got up. It was very large and very stupid and it screamed in three languages. I kept its leg because it was the first thing I killed for myself, and not for eggs, or for a lair, or because something had put steel in me." {n}She takes it from you and lays it back very precisely.{/n} "It tasted terrible. I have never been happier."''',
       c("Continue", "then")),
    dv("ring", '''{n}She is quiet for a moment.{/n} "A crusader. Not one of yours. One of the ones from a hundred years ago, who came into the Worldwound on the first crusades and did not come out. I found him in a cave." {n}She hooks the ring off the finger bone with one claw and drops it into your palm.{/n} "I did not kill him. I keep him because he is the only crusader I ever found who went all the way in. I thought you should know that there was one before you."''',
       c("Continue", "then")),
    dv("then", '''"Now your turn." {n}She lies down with her chin among the bones.{/n} "Name something you killed that was worth the trouble. Not a demon; I can smell those on you. Something that cost you."''',
        c('[Tell her about someone you couldn\'t save.]', "lost"),
        c('[Tell her about someone you killed who didn\'t deserve it.]', "killed"),
        c('"My floor isn\'t sorted. I don\'t look at it."', "unsorted")),
    dv("lost", '''{n}She listens without moving. When you finish, she noses the bone in your hand.{/n} "You kept nothing of it?" {n}she says at last.{/n} "No tooth? No bone? Not even a ring?" {n}She sniffs, disgusted.{/n} "Then tell it well, the next time you tell it. That is all you have left of it, and you told it badly."''',
       c("Continue", "end")),
    dv("killed", '''{n}She listens with great interest, which is worse than disapproval.{/n} "And you think about it." {n}She seems genuinely curious.{/n} "I have killed a great many things that did not deserve it. I do not think about them at all. I only keep the bones." {n}She considers you.{/n} "Perhaps that is the difference between us. Perhaps it is only that you have fewer bones. Come back when you have more, and we will see."''',
       c("Continue", "end")),
    dv("unsorted", '''"No." {n}She does not sound surprised.{/n} "You step on everything on your floor as if it were not there. So do cattle." {n}She pushes the crow's bones a little closer to you with her claw.{/n} "Then mind where you put your feet on mine. I keep my dead where I can see them, and I bite things that kick them."''',
       c("Continue", "end")),
    teller("end", '''{n}The Storyteller hears the account in silence.{/n} "She told me, in the lair, that bones were for picking her teeth." {n}He sets the cup aside.{/n} "Now she sorts them and tells you what they were. I would be flattered that she learned it from me, if I did not know what she keeps the stories for. She keeps them the way she keeps the bones: picked clean."''',
        c('"Both."', flags=(BONES,))),
    dv("small_free", '''"A bird." {n}She sounds pleased.{/n} "A crow, from the mountain where I lay the night the charm called. It sat on a rock above me until dawn, waiting for me to be too weak to bite. I ate it in the morning, when the calling stopped." {n}Her lip lifts.{/n} "I kept the bones to remind me that everything waits for everything else to die. Even the little things. Especially the little things."''',
       c("Continue", "then")),
    dv("large_free", '''"A vrock." {n}She looks at it with great fondness.{/n} "The first demon I killed after your bargain. It was very large and very stupid and it screamed in three languages. I kept its leg because it was the first thing I killed in a year that a stone had not pointed me at." {n}She takes it from you and lays it back very precisely.{/n} "It tasted terrible. I have never been happier."''',
       c("Continue", "then")),
], requires=(CLIMBED,), forbids=(BONES,), delay=96)


# --- 31. What she is afraid of (after the commit): the second death --------------------------------------------------

hub(T + "her_fear", "The thing she will not say", '"She\'s quiet. The sentries say she hasn\'t hunted in days."', [
    teller("start", '''"She has not. She lies on the sill and looks at the city and does not eat." {n}He is worried; you can hear it.{/n} "I asked her what was wrong. She said, 'Nothing is wrong. Everything is exactly as it is, and that is the problem.' She would not say any more to me. I think she will say it to you. I think she has been waiting for you to ask, so that it will not be her idea."''',
        c("Continue", "climb")),
    dv("climb", '''{n}She does not lift her head when you come in. Her eye follows you across the floor, dull as a banked coal.{/n} "You have come to ask what is wrong." {n}Her voice is very flat.{/n} "Then ask. I will not tell you unless you ask."''',
        c('"What\'s wrong?"', "wrong", forbids=(FLOWN,)),
        c('"What\'s wrong?"', "wrong_free", requires=(FLOWN,))),
    dv("wrong", '''{n}She lifts the wing. The seam under it has opened along a hand's length, wet and grey at the lips, and the new hide around it is cracked like a dry riverbed.{/n} "It split three nights ago, when I took a vrock at the Wound's edge and it got a claw in. It has not closed. Everything else on me closes." {n}Her eye holds you, dull and furious.{/n} "You gambled that my body knew what it was doing. Perhaps it did once. If the next blade finds this, the stories you paid me in will not stitch it, and I will be a carcass again, and this time nobody will be fool enough to wait three days. Do not tell me it will heal. Tell me what you are going to do."''',
        c('[Send for the crusade\'s best surgeon, and the alchemist who seals siege-armour] "Tomorrow. Both of them, up the ridge, whether they like it or not."', "made"),
        c('"I don\'t know. Nobody\'s ever kept a woundwyrm alive long enough to find out."', "dunno"),
        c('[Draw your knife and cut your own palm] "Then take what you need to close it. You took the rest already."', "keep")),
    dv("made", '''"A surgeon. Up my mountain." {n}She shows you her teeth.{/n} "He will be so frightened his hands will shake, and if they shake on my seam I will eat them, and then I will eat him, and you will have to find another." {n}She lays her head down, watching you.{/n} "Send the alchemist first. Alchemists are used to things that might explode. And tell the surgeon what I said about his hands. I want him careful, not brave."''',
       c("Continue", "end")),
    dv("dunno", '''{n}She does not answer. Then the laugh, small and rusty, like a bellows full of embers.{/n} "Nobody. No. They cut us up for glue and hide and sell our blood by the thimble." {n}She lays her head on your boots, heavily, so that you cannot move without her leave.{/n} "Then stop guessing aloud, crusader, and find me somebody who has cut one up. A renderer, a hide-merchant, a demon who has eaten one. Whoever knows where we come apart knows where we are held together. Bring them up here. I will not eat them until they have talked."''',
       c("Continue", "end")),
    dv("keep", '''{n}She watches the blood run down your wrist, and her nostrils open.{/n} "Blood does not close a hide, crusader. Every hunter who ever came up a mountain after me knew that." {n}Her tongue comes out anyway, and takes it off your palm, slowly, all of it.{/n} "But it was offered, and I do not refuse what is offered." {n}She lays her head down.{/n} "Now send your surgeon. And if he faints at the top of the stair, I keep him."''',
       c("Continue", "end")),
    teller("end", '''{n}The next morning the sentries report that the grey dragon went hunting at dawn, far out over the Wound's edge, and came back with a vrock in each claw, and ate them both on the sill in full view of the north wall, very noisily.{/n}
{n}A week later the people you sent up the ridge come down it grey to the lips, with their pots and needles used up, and refuse to say what they saw. One of them does not come down at all for two days, and when he does he has lost a finger, and will only say that he flinched.{/n}
{n}The Storyteller hears the account without smiling.{/n} "The seam is shut, then. She will be hungry after. Tell the north watch to stay off the walls tonight."''',
        c('"Good."', flags=(FEAR,))),
    dv("wrong_free", '''{n}She lifts the wing. The long scar on her flank, the one your fight opened in the lair and she flew on, has split again along a hand's length, wet and grey at the lips, and the scales around it are cracked like a dry riverbed.{/n} "It opened three nights ago, when I took a vrock at the Wound's edge and it got a claw in. It has not closed. Everything else on me closes." {n}Her eye holds you, dull and furious.{/n} "You put this in me, and then you asked me to lie on a mountain with it open rather than answer the stone. It never healed right. If the next blade finds it, I will be meat on a hillside, and no story will buy that back. Do not tell me it will heal. Tell me what you are going to do."''',
        c('[Send for the crusade\'s best surgeon, and the alchemist who seals siege-armour] "Tomorrow. Both of them, up the ridge, whether they like it or not."', "made"),
        c('"I don\'t know. Nobody\'s ever kept a woundwyrm alive long enough to find out."', "dunno"),
        c('[Draw your knife and cut your own palm] "Then take what you need to close it. You took the rest already."', "keep")),
], requires=(COMMITTED,), forbids=(FEAR,), delay=120)


# --- 32. On the roof (after the commit): she comes down into the city ------------------------------------------------

hub(T + "on_the_roof", "The odds were a hundred to one", '"Why is the whole garrison staring at the citadel roof?"', [
    teller("start", '''"Because there is a dragon on it." {n}He tries to suppress a laugh.{/n} "She landed above your window an hour ago and has not moved. The chaplains are praying. On the north wall they are arguing whether a dragon on the roof is better or worse than one flying over it. Nobody has volunteered to ask her."''',
        c("Continue", "roof")),
    nar("roof", '''{n}You climb out onto the roof in the dark. The whole city is quiet below you, every window lit, every face turned up. She is lying along the ridge of the citadel roof like a grey gargoyle, her chin on the chimney stack, watching the stars.{/n}''',
        c("Continue", "her")),
    dv("her", '''"A hundred to one." {n}She shifts her tail along the tiles. Three slide off and shatter below.{/n} "That is what they put on my coming down here. I thought I would let them see what their hundred looks like from underneath." {n}Her eye turns toward the courtyard.{/n} "I have not eaten anyone tonight. Tell them that. Tell them it is very difficult."''',
        c('"Why did you really come down?"', "why"),
        c('[Sit beside her on the roof.]', "sit")),
    dv("why", '''"To see what you see." {n}She finally turns her head.{/n} "Every night you look up at my ridge from this window. I have watched you do it. I wanted to lie where you stand and look back at it, and see whether it is small from here, the way you are small from there." {n}She looks up at the dark ridge.{/n} "It is. It is very small. I did not like that at all."''',
       c("Continue", "sit")),
    nar("sit", '''{n}You sit on the cold tiles with her flank warm at your back. Her breath rises into the night. Below, faces crowd the lit windows; a few guards still hold crossbows, though none has raised one toward the roof.{/n}''',
        c("Continue", "end_her")),
    dv("end_her", '''"Tomorrow they will say you tamed me." {n}Her voice is very low, and very pleased.{/n} "Let them. It will be the funniest lie anyone has ever told about either of us, and you did not even have to tell it." {n}She lays her head on the chimney stack.{/n} "I will go back up before dawn. Stay a while. It is warmer out here than in your little room. I checked."''',
        c("[Stay.]", flags=(ROOF,))),
], requires=(COMMITTED, BOOK), forbids=(ROOF,), delay=120)

COLD = T + "first_snow"
HIS_STORY = T + "storytellers_story"


# --- 33. The first snow (after the first climb): woundwyrms do not like the cold ------------------------------------

hub(T + "first_snow", "Snow on the ridge", '"It snowed on the ridge last night. Is she...?"', [
    teller("start", '''"Furious." {n}He says it with deep satisfaction.{/n} "She has discovered, it seems, that a new hide is a thin hide. The moult left her grey and fine and very handsome, and not at all suited to a Mendevian winter. She spent the night breathing on the tower walls to keep them warm and has set fire to most of her fleeces. She has asked me to ask you, with a great many threats attached, whether the crusade owns any braziers."''',
        c('[Send up every brazier in the citadel] "All of them. And blankets."', "braziers"),
        c('"Tell her to come down into the city where it\'s warm."', "city")),
    nar("braziers", '''{n}It takes six carts and a great deal of swearing from the teamsters to get the braziers up the ridge. You go up with the last one.{/n}
{n}She has lain down in a ring of them around the tower floor like a cat around a hearth, her wings wrapped tight about herself, her breath coming out in white plumes, glaring at the snow on the sill as though it had insulted her personally. The fleeces you sent are heaped under her chin.{/n}''',
        c("Continue", "braziers_her")),
    dv("braziers_her", '''"Do not say anything." {n}Her teeth are very nearly chattering, which on a dragon is a sound like knives in a drawer.{/n} "Three hundred winters in the mountains of the north, the last hundred of them in the Wound, and I never once felt the cold. The old hide was a hand thick. This one is paper." {n}She pulls a fleece closer with one claw.{/n} "This is your fault. You kept the knives off me for three days while this grew. You did not think to keep me warm."''',
       c('[Sit down inside the ring and lean against her.]', "lean"),
       c('"Next time you die, I\'ll bring braziers."', "both")),
    teller("city", '''{n}He goes up and comes back before noon, looking both shocked and delighted.{/n} "She said: 'Tell the Commander that if I come down into its city to get warm, I will not come back up, and the city will not be warm for very long afterwards.'" {n}He folds his hands.{/n} "And then she said, 'Send the braziers.' I have taken the liberty of ordering them in your name."''',
        c("Continue", "braziers")),
    nar("lean", '''{n}You step between the braziers and sit down with your back against her flank. She is cold, the way a stove is cold in the morning: warmth still deep inside, but none of it reaching the surface. After a moment she shifts, and the grey wing comes down over both of you, and between the braziers and the wing and the two of you it is suddenly, absurdly, warm.{/n}''',
        c("Continue", "lean_her")),
    dv("lean_her", '''"Hm." {n}Her voice rumbles through her ribs into your back.{/n} "You are warmer than you look. Crusaders run hot. It is all that righteousness, burning." {n}She settles.{/n} "Stay until the snow stops. I want your heat, and I am taking it. Get up before I say, and I will lie on you until you learn."''',
       c("Continue", "end")),
    dv("both", '''"Next time." {n}She considers this with narrowed eyes.{/n} "Knives off, and braziers. Yes. Next time you sit up with a dead thing, crusader, be thorough. Think of the winters." {n}She huffs a jet of flame at the snow on the sill, which hisses and vanishes.{/n} "Now go and find more braziers. These are too small. Everything your crusade makes is too small."''',
       c("Continue", "end")),
    teller("end", '''{n}The Storyteller, when you come down, has a cup of hot wine waiting.{/n} "I heard the carts. The whole city heard the carts. There are already three songs about the Commander carrying fire up a mountain to a dragon." {n}He hands you the cup.{/n} "They are all terrible. I am writing a fourth. It will be worse, but it will be true."''',
        c('"Send her a copy."', flags=(COLD,))),
], requires=(CLIMBED,), forbids=(COLD, FLOWN), delay=96, chapters=(5,))


hub(T + "first_snow_free", "Snow on the ridge", '"It snowed on the ridge last night. Is she...?"', [
    teller("start", '''"Furious." {n}He says it with deep satisfaction.{/n} "She has discovered that a wing your people put holes in lets the wind through. The scar stiffens in the cold, she says, and aches like a bad tooth, and locks when she tries to bank. She spent the night breathing on the tower walls to keep them warm and has set fire to most of her fleeces. She has asked me to ask you, with a great many threats attached, whether the crusade owns any braziers."''',
        c('[Send up every brazier in the citadel] "All of them. And blankets."', "braziers"),
        c('"Tell her to come down into the city where it\'s warm."', "city")),
    nar("braziers", '''{n}It takes six carts and a great deal of swearing from the teamsters to get the braziers up the ridge. You go up with the last one.{/n}
{n}She has lain down in a ring of them around the tower floor like a cat around a hearth, her wings wrapped tight about herself, her breath coming out in white plumes, glaring at the snow on the sill as though it had insulted her personally. The fleeces you sent are heaped under her chin.{/n}''',
        c("Continue", "braziers_her")),
    dv("braziers_her", '''"Do not say anything." {n}Her teeth are very nearly chattering, which on a dragon is a sound like knives in a drawer.{/n} "Three hundred winters in the mountains of the north, the last hundred of them in the Wound, and the cold never caught in that wing before. Now the wind goes through it like a sieve." {n}She pulls a fleece closer with one claw.{/n} "This is your fault. Your people put the holes in it. You did not think to keep me warm."''',
       c('[Sit down inside the ring and lean against her.]', "lean"),
       c('"Next time I put holes in you, I\'ll bring braziers."', "both")),
    teller("city", '''{n}He goes up and comes back before noon, looking both shocked and delighted.{/n} "She said: 'Tell the Commander that if I come down into its city to get warm, I will not come back up, and the city will not be warm for very long afterwards.'" {n}He folds his hands.{/n} "And then she said, 'Send the braziers.' I have taken the liberty of ordering them in your name."''',
        c("Continue", "braziers")),
    nar("lean", '''{n}You step between the braziers and sit down with your back against her flank. She is cold, the way a stove is cold in the morning: warmth still deep inside, but none of it reaching the surface. After a moment she shifts, and the grey wing comes down over both of you, and between the braziers and the wing and the two of you it is suddenly, absurdly, warm.{/n}''',
        c("Continue", "lean_her")),
    dv("lean_her", '''"Hm." {n}Her voice rumbles through her ribs into your back.{/n} "You are warmer than you look. Crusaders run hot. It is all that righteousness, burning." {n}She settles.{/n} "Stay until the snow stops. I want your heat, and I am taking it. Get up before I say, and I will lie on you until you learn."''',
       c("Continue", "end")),
    dv("both", '''"Next time." {n}She considers this with narrowed eyes.{/n} "Holes, and braziers. Yes. Next time you set your people on a dragon, crusader, be thorough. Think of the winters." {n}She huffs a jet of flame at the snow on the sill, which hisses and vanishes.{/n} "Now go and find more braziers. These are too small. Everything your crusade makes is too small."''',
       c("Continue", "end")),
    teller("end", '''{n}The Storyteller, when you come down, has a cup of hot wine waiting.{/n} "I heard the carts. The whole city heard the carts. There are already three songs about the Commander carrying fire up a mountain to a dragon." {n}He hands you the cup.{/n} "They are all terrible. I am writing a fourth. It will be worse, but it will be true."''',
        c('"Send her a copy."', flags=(COLD,))),
], requires=(CLIMBED, FLOWN), forbids=(COLD,), delay=96, chapters=(5,))


# --- 34. The Storyteller's story (after the messenger): the one he never started --------------------------------------

hub(T + "his_story", "A story made up for a dragon", '"You said she asked you for a story you\'d never started. Did you finish it?"', [
    teller("start", '''"I finished it." {n}He sounds, for once, uncertain.{/n} "It took me some time. I have not made up a story in a very long while, Commander; I have only collected them. I would like to tell it to her tonight, and I would like you to be there. I am told I am a better storyteller when I am frightened, and I am more frightened of telling this one than of anything I have told in a long while."''',
        c("Continue", "climb")),
    nar("climb", '''{n}So the three of you sit in the tower as the light goes: the dragon with her chin on the floor, the old blind elf on his bone bench, and you between them. Her eye follows the old elf's hands as he begins.{/n}''',
        c("Continue", "story", forbids=(FLOWN,)),
        c("Continue", "story_free", requires=(FLOWN,))),
    teller("story", '''"Once there was a thief," {n}he says,{/n} "who stole a word. It was the most dangerous word in the world: the word for what a thing is. And the thief, being a thief, did not keep it. The thief gave it away, carelessly, to a dead thing on a floor, just to see what would happen."
{n}He turns his blind face toward her.{/n} "And the dead thing got up, and was very angry, and went to live on a mountain, and every night it looked down at the thief's city and planned how it would take the word back."''',
        c("Continue", "story_2")),
    teller("story_2", '''"The thief kept climbing, bringing mostly talk. The dragon learned the sound of the footsteps. On nights when the thief did not come, she watched the path anyway." {n}His hands rest on his knees.{/n} "Then she began to count the visits. The thief never asked what number she was waiting for."''',
        c("Continue", "ending")),
    dv("ending", '''{n}She lifts her head.{/n} "And? What happened next?" {n}The old man's hands go still on his knees. Whatever that line once meant in a lair, he does not say.{/n}''',
        c("Continue", "ending_2")),
    teller("ending_2", '''{n}He smiles.{/n} "The thief is still climbing, madam. I have not heard how it ends." {n}He turns toward you.{/n} "Perhaps tonight we will get a little further."''',
        c("Continue", "her")),
    dv("her", '''{n}She looks from you to the Storyteller.{/n} "You left out the night, old man. The waiting. The dragon listening in the dark." {n}Her claws scrape under her chin.{/n} "You had better teeth in your stories when I kept you in the lair. Put them back."''',
       c("Continue", "end")),
    teller("end", '''{n}He gives her the waiting: the dragon listening in the dark, the thief waiting to learn whether the bargain would hold. She interrupts over the dragon's voice. He tries another voice. This time she lets him finish.{/n}
{n}At the foot of the ridge he stops, his stick planted firmly between the rocks.{/n} "I could have given her a happy ending. She would have heard the lie before I finished it." {n}He starts down again.{/n} "I think I prefer the interruption."''',
        c('''"She let you finish."''', flags=(HIS_STORY,))),
    teller("story_free", '''"Once there was a thief," {n}he says,{/n} "who stole a dragon's leash. It was the most dangerous thing in the world to steal, because a leash is a promise, and the thing that held the other end was stone, and stone does not forget. And the thief, being a thief, did not keep what was stolen. The thief gave it away, carelessly, to a dragon who would have eaten the thief the week before, just to see what would happen."
{n}He turns his blind face toward her.{/n} "And the dragon flew, and was very angry, and went to live on a mountain, and every night it looked down at the thief's city and planned how it would pay the thief back, and in what coin."''',
        c("Continue", "story_2_free")),
    teller("story_2_free", '''"The thief kept climbing, bringing mostly talk. The dragon learned the sound of the footsteps. On nights when the thief did not come, she watched the path anyway." {n}His hands rest on his knees.{/n} "Then she began to count the visits. The thief never asked what number she was waiting for."''',
        c("Continue", "ending")),
], requires=(COMMITTED, TELLER_VIEW), forbids=(HIS_STORY,), delay=72)

CELLS = T + "cells_seen"
TRAIL = T + "trail_followed"
SCAR = T + "scar_seen"


# --- 35. The cells (after the tithe, ruthless): the last cultist ---------------------------------------------------

hub(T + "the_cells", "The last cart", '"The cells under the citadel are nearly empty."', [
    teller("start", '''"Nearly." {n}He does not sound pleased.{/n} "One left. A priest of Deskari, the one who would not talk when your inquisitors asked him nicely or otherwise. She has sent word that she wants him brought up alive, and that you are to come with him." {n}He turns his cup.{/n} "I will not carry this one, Commander. I carried her threats. I will not carry her dinner. Your guards can do that."''',
        c("Continue", "climb")),
    nar("climb", '''{n}The cultist is chained in the cart, a gaunt man with locust sigils cut into his arms, and he spits at the guards and laughs at the ridge all the way up. He stops laughing at the door of the tower.{/n}
{n}She does not move toward him. She lies with her chin on the floor and looks at him as she looked at the Storyteller in the lair, the way a reader looks at the first page of a book.{/n}''',
        c("Continue", "her")),
    dv("her", '''"Your god," {n}she says to him, very pleasantly.{/n} "Tell me about him. Tell me a story about the Locust Lord that impresses me, and perhaps I will not eat you. That is my tariff. The old man down the mountain paid it once." {n}Her eye slides to you.{/n} "Stay, crusader. I want you to hear what a man says when he knows exactly how little he has left to trade."''',
        c('[Stay and listen.]', "listen"),
        c('"I\'ve heard enough from his kind. Do what you want."', "leave")),
    nar("listen", '''{n}The priest talks. At first it is threats, and then scripture, and then, as her breath comes closer and hotter, it is something else: the story of a village in the Worldwound, a boy with a fever, a swarm that came in the night and a voice in the swarm that promised the fever would stop. It is not a good story. It is a true one.{/n}
{n}When he is done she lets the silence go on.{/n}''',
        c("Continue", "verdict")),
    dv("verdict", '''"Not impressive," {n}she says at last, gently.{/n} "True, and small, and sad, and not impressive." {n}She looks at you.{/n} "You see, crusader? That is the difference between his god and me. His god promised him something, and took the price, and never came. I told him my price at the start, and I will keep my word." {n}She opens her jaws.{/n} "Go down the mountain now. You have heard what you came for."''',
       c("[Go down the mountain.]", "end")),
    dv("leave", '''"Do what I want." {n}She sounds faintly disappointed in you.{/n} "Yes. I always do. But I wanted you to watch me give him the chance. That is the only mercy in me, crusader: I tell them the price." {n}She turns back to the priest.{/n} "Go. I will tell you whether he impressed me. He will not."''',
       c("[Go down the mountain.]", "end")),
    teller("end", '''{n}At the bottom of the ridge the Storyteller is not waiting. He has gone home. You find him later, in his room, sitting in the dark.{/n} "The cells are empty," {n}he says, without turning.{/n} "Your inquisitors are pleased. The city is safer." {n}A long pause.{/n} "I was in that lair, Commander. I know what it is to stand in front of her and tell the story of your life to buy the rest of it. I would not wish it on a priest of Deskari. I would not wish it on anyone. Go to bed."''',
        c('"Good night."', flags=(CELLS,))),
], requires=(TESTED, RUTHLESS, CLIMBED), forbids=(CELLS,), delay=72)


# --- 36. The trail (after the first climb, hunting the druids): what she found -----------------------------------------

hub(T + "the_trail", "Tracks that are not druids'", '"She\'s been gone for days. The sentries say she flew east."', [
    teller("start", '''"East, and east again, and back." {n}He sounds tired; he has been sleeping badly, he admits, listening for her.{/n} "She came back last night and has not spoken to anyone. She asked for you this morning, in one word, and the word was your title, and nothing else. I think she has found something. I think she does not know what it means."''',
        c("Continue", "climb")),
    dv("climb", '''{n}There is mud dried grey on her claws and a long scrape across her muzzle where something thorny and deliberate has raked it.{/n} "I found where they nest." {n}She does not greet you.{/n} "Your druids. In a valley with a white stone at the top, three rivers east. They are not druids, crusader. When they saw me coming, one of them stopped being a man, and was gold, and was very nearly as big as I am."''',
        c("Continue", "fight")),
    dv("fight", '''"We did not fight." {n}She touches the scrape on her muzzle; the thorn wall around the valley did that, not the gold one.{/n} "It stood in front of the nest the way a mother stands, and I knew the stance, because it was mine. And behind it, in the valley, I heard them: my children, hatched, calling to each other in a nest that was not mine." {n}Her voice does not change at all.{/n} "The gold one said one word in Draconic. It said 'safe'. The same word as on the eggshell."''',
        c('"What did you do?"', "did")),
    dv("did", '''"I left." {n}She says it as if it were the most shameful word she knows.{/n} "I left my children in the nest of a gold dragon, because they were warm, and they were fed, and they were not afraid, and they did not know my voice." {n}The wind moves through the arrow slits.{/n} "Tell me I was right, crusader. You are a liar. Lie to me well."''',
        c('"You were right."', "right"),
        c('"I won\'t lie to you about this."', "no_lie")),
    dv("right", '''"Yes." {n}She lays her head down.{/n} "That was a very good lie. I almost believed it." {n}Her eye closes.{/n} "Tell it to me again in a year. By then I may believe it. That is how your lies work on me, is it not? You tell them until I decide they are worth paying for."''',
       c("Continue", "end")),
    dv("no_lie", '''{n}Her eye opens and fixes on you, and for a moment you think she will strike.{/n} "You will not lie." {n}Then, slowly, the anger goes out of her, and something older and much tireder takes its place.{/n} "No. Not about this. I asked you to, and you would not. That is worse than any lie you have ever told me." {n}She looks east.{/n} "And better. Go down. I need to not be looked at."''',
       c("Continue", "end")),
    teller("end", '''{n}The Storyteller hears what happened in silence.{/n} "She left them." {n}He shakes his head slowly.{/n} "In the lair, she told me that dragons do not give up what is theirs, ever." {n}He turns his face toward the ridge.{/n} "She left without the young. You should not assume she has finished counting them."''',
        c('"..."', flags=(TRAIL,))),
], requires=(HUNTING, CLIMBED), forbids=(TRAIL,), delay=96)


# --- 37. The scar (after the first bite): the surgeons ask ------------------------------------------------------------

hub(T + "the_scar", "The surgeons have questions", '"The surgeons keep asking about my arm."', [
    teller("start", '''"I imagine they do." {n}He sounds amused.{/n} "A neat grey crescent of punctures, perfectly spaced, healing clean, on the forearm of the Commander of the crusade, who will say only that it was 'a bargain'. Your chief surgeon came to me because he has heard I know dragons. He wanted to know whether the bite would fester." {n}He smiles.{/n} "I told him who made the marks, and that healing them was his trade and not mine, and that he should not expect them to be the last."''',
        c('"What else did he ask?"', "asked"),
        c('"Does she know they\'re asking?"', "knows")),
    teller("asked", '''"He asked whether you were under an enchantment." {n}The smile widens.{/n} "I told him I know of no spell on you, and that if he wished to know what you are under he should ask you, and that he should ask it in daylight, in company." {n}He smiles, very slightly.{/n} "He went away looking very serious. I believe he thinks it is a curse. I did not correct him."''',
        c("Continue", "climb")),
    teller("knows", '''"She knows everything that is said about her, and most of what is said about you." {n}He tilts his head.{/n} "She asked me yesterday whether the mark was healing well. I said I could not see it. She said, 'Then touch it, next time the Commander is careless enough to let you.' I did not. I have my limits."''',
        c("Continue", "climb")),
    dv("climb", '''"Show me." {n}She does not wait for you to reach the top of the stair.{/n} "The arm. Show me." {n}You roll back your sleeve. She brings her head down close and studies the healing marks, her breath hot on your skin, the way a smith looks at a weld.{/n}''',
        c("Continue", "look", forbids=(FLOWN,)),
        c("Continue", "look_free", requires=(FLOWN,))),
    dv("look", '''"Good." {n}She sounds satisfied, and something more than satisfied.{/n} "Clean. Even. It will scar grey, the colour of the new hide. Anyone who sees it will know whose it is." {n}She touches the mark once, very lightly, with the tip of her tongue, and you feel it all the way up your arm.{/n} "Your surgeons may ask all they like. The answer is on your arm. Let them read it."''',
       c('"They will."', flags=(SCAR,))),
    dv("look_free", '''"Good." {n}She sounds satisfied, and something more than satisfied.{/n} "Clean. Even. It will scar pale, the colour of the seam your people left in me. Anyone who sees the two of them will know whose they are." {n}She touches the mark once, very lightly, with the tip of her tongue, and you feel it all the way up your arm.{/n} "Your surgeons may ask all they like. The answer is on your arm. Let them read it."''',
       c('"They will."', flags=(SCAR,))),
], requires=(BITTEN_ONCE,), forbids=(SCAR,), delay=72)

# --- 37b. One short (Nidalynn's route, ledger 05 row 5): custody of the twelfth egg, before the bill --------------------
# Additive (R2, claude/trk-nidalynn). Custody: the clutch is hers and follows its native fate and her own route's flags;
# the one egg the Commander took out of the Sanctum in the ash-bin stays with whoever raises it. She never takes it back
# and never closes Nidalynn's route; Nidalynn never closes hers. What she wants is to know, and later to be paid.

ONE_SHORT = T + "one_short"
TWELFTH_TOLD = T + "twelfth_told"
TWELFTH_LIED = T + "twelfth_lied"
N_PRIMED = "nidalynn.trickster.primed"

hub(ONE_SHORT, "One short", '"She\'s counting again, isn\'t she?"', [
    teller("start", '''"She has never stopped." {n}He turns his cup a quarter turn.{/n} "She has stopped telling me what she is counting. I know anyway."''',
        c("Continue", "count", forbids=("nidalynn.trickster.eggs.vault",)),
        c("Continue", "start_vault", requires=("nidalynn.trickster.eggs.vault",))),
    teller("count", '''"She laid twelve, she says. She has had every account of that chamber out of me that I could give her, and out of anyone else she could frighten, and she makes it eleven. Eleven in the straw when the golems were done with it, whatever became of them after." {n}His blind face turns toward you.{/n} "She says the twelfth went out of that chamber on somebody's back. She says she can smell whose."''',
        c("Continue", "climb", forbids=(FLOWN,)),
        c("Continue", "climb_free", requires=(FLOWN,))),
    teller("start_vault", '''"The twelve came to your vault in straw. She does not dispute it; she counted the cart from the ridge." {n}He folds his hands.{/n} "She has had every account of that vault out of me that I could give her, and she makes it eleven now. She says the twelfth went out of your vault in somebody's coat. She says she can smell whose."''',
        c("Continue", "climb", forbids=(FLOWN,)),
        c("Continue", "climb_free", requires=(FLOWN,))),
    dv("climb", '''{n}She is lying across the top of the broken stair with her chin on her claws, and she does not look at you when you come up.{/n} "Eleven." {n}The word comes out on a long, hot breath.{/n} "I have counted them in the dark of that dead body, and I have counted them since. Eleven. I laid twelve."
{n}Now she looks at you.{/n} "Where is the twelfth, crusader? Do not tell me there never was one. A mother knows the weight of what she carried."''',
       c('"I have it. It was the smallest, and it was cold, and it\'s alive."', "told", flags=(ONE_SHORT, TWELFTH_TOLD)),
       c('[Lie] "There were eleven. You miscounted, dying."', "lied", flags=(ONE_SHORT, TWELFTH_LIED)),
       c('"It\'s safe. That\'s all I\'ll say."', "safe", flags=(ONE_SHORT,))),
    dv("told", '''{n}Something very old moves behind her eyes and goes back into the dark.{/n} "The smallest. It always is." {n}She lays her head back on her claws.{/n} "I will not come down for it. A thing that small, taken out from under Xanthir's toys by a thief who could have smashed it, is warmer where it is than it would be here. I know what I am."
"But I know who took it now. Remember that I know. When I have decided what it cost me, you will hear the price."''',
       c("[Go down the mountain.]")),
    dv("lied", '''"I died counting, and I got up counting, and I have never once in three hundred years miscounted an egg." {n}She does not raise her voice. She does not need to.{/n} "That is the worst lie you have told me, crusader, and the first one I did not enjoy. Keep it. I will keep it too, next to the egg you are lying about, and I will add them together when I send the bill."''',
       c("[Go down the mountain.]")),
    dv("safe", '''"Safe." {n}She tastes the word, as she did once before.{/n} "From me, you mean." {n}A long breath; the fleeces in the arrow slits stir.{/n} "Good. Keep it safe from me, then. I will let you. It is the only thing of mine you will ever keep from me without paying, and you will pay for it anyway, later, when I know the whole of it."''',
       c("[Go down the mountain.]")),
    dv("climb_free", '''{n}She is lying across the top of the broken stair with her chin on her claws, and she does not look at you when you come up.{/n} "Eleven." {n}The word comes out on a long, hot breath.{/n} "I knew how many lay under those fists the night the charm called, and I have counted every word of them since. Eleven. I laid twelve."
{n}Now she looks at you.{/n} "Where is the twelfth, crusader? Do not tell me there never was one. A mother knows the weight of what she carried."''',
       c('"I have it. It was the smallest, and it was cold, and it\'s alive."', "told", flags=(ONE_SHORT, TWELFTH_TOLD)),
       c('[Lie] "There were eleven. You miscounted, bleeding on a mountain."', "lied_free", flags=(ONE_SHORT, TWELFTH_LIED)),
       c('"It\'s safe. That\'s all I\'ll say."', "safe", flags=(ONE_SHORT,))),
    dv("lied_free", '''"I have never once in three hundred years miscounted an egg." {n}She does not raise her voice. She does not need to.{/n} "That is the worst lie you have told me, crusader, and the first one I did not enjoy. Keep it. I will keep it too, next to the egg you are lying about, and I will add them together when I send the bill."''',
       c("[Go down the mountain.]")),
], requires=("trickster.ever", RETURNED, N_PRIMED),
   # PP7 (Sol BEL): once the kiln confession has told her where the twelfth is, she no longer asks.
   forbids=(ONE_SHORT, T + "smallest_egg", "nidalynn.trickster.confessed"), delay=24)


# --- 38. The smallest egg (Nidalynn's route, ledger 05 row 5): the bill for the one the Commander stole lands on the Commander -
# Additive (R2, claude/trk-nidalynn). The Commander confessed at the kiln that the "rock" was her egg; the scream carried to
# the ridge. She does not take the hatchling from the silver who raises it; she bills the thief. Nidalynn's route reads the
# flag in nodes only and never gates on it; this scene gates only on the public confession.

EGG_BILL = "devarra.trickster.cost.egg_withheld"
SMALLEST = T + "smallest_egg"
N_CONFESSED = "nidalynn.trickster.confessed"
N_STRAW = "nidalynn.trickster.egg.straw"   # NM1: the twelfth was left in the druids' straw and kept with a lie on the slate

hub(SMALLEST, "The smallest egg", '''"She heard about the hatchling, didn't she?"''', [
    teller("start", '''"The whole ridge heard the hatchling scream. I heard it from my bed." {n}He does not smile.{/n} "She went down to the east wall and watched the kiln until dawn. She did not go closer. Now she wants you fetched. She did not say your title. She said 'the thief'."''',
        c("Continue", "climb", forbids=(FLOWN,)),
        c("Continue", "climb_free", requires=(FLOWN,))),
    dv("climb", '''{n}She does not lift her head from the sill when you come up the stair. Her eye is on the lower town, on one thin line of smoke under the east wall.{/n} "Twelve." {n}Her voice is very quiet.{/n} "I laid twelve, in the dark under the Sanctum, and I counted them every day that Xanthir's toys stood over them with their fists up. I died counting them. I got up counting them."''',
       c("Continue", "omelet", requires=("eggs.omelet",)),
       c("Continue", "druids", requires=("eggs.druids",), forbids=("eggs.omelet", N_STRAW)),
       c("Continue", "vault", requires=("eggs.project",), forbids=("eggs.druids", "eggs.omelet")),
       c("Continue", "destroyed", requires=("eggs.destroyed",)),
       c("Continue", "eleven", forbids=("eggs.omelet", "eggs.druids", "eggs.project", "eggs.destroyed")),
       c("Continue", "druids_straw", requires=("eggs.druids", N_STRAW), forbids=("eggs.omelet",))),
    dv("climb_free", '''{n}She does not lift her head from the sill when you come up the stair. Her eye is on the lower town, on one thin line of smoke under the east wall.{/n} "Twelve." {n}Her voice is very quiet.{/n} "I laid twelve, in the dark under the Sanctum, and I counted them every day that Xanthir's toys stood over them with their fists up. I knew how many lay under the fists the night the charm called me. I have counted them since."''',
       c("Continue", "omelet", requires=("eggs.omelet",)),
       c("Continue", "druids", requires=("eggs.druids",), forbids=("eggs.omelet", N_STRAW)),
       c("Continue", "vault", requires=("eggs.project",), forbids=("eggs.druids", "eggs.omelet")),
       c("Continue", "destroyed", requires=("eggs.destroyed",)),
       c("Continue", "eleven", forbids=("eggs.omelet", "eggs.druids", "eggs.project", "eggs.destroyed", COLLECTED)),
       c("Continue", "kept_eleven", requires=(COLLECTED,), forbids=("eggs.omelet", "eggs.druids", "eggs.project", "eggs.destroyed")),
       c("Continue", "druids_straw", requires=("eggs.druids", N_STRAW), forbids=("eggs.omelet",))),
    dv("kept_eleven", '''"Eleven on my mountain, in my fleeces, under my own chin." {n}Her claws close on the stone.{/n} "And one in a lime-kiln, screaming loudly enough to carry up here. You had her in your hearth, under ash, and called her a rock."''',
       c("Continue", "stole_lane", forbids=("nidalynn.trickster.lied_at_kiln",)),
       c("Continue", "stole_muster", requires=("nidalynn.trickster.lied_at_kiln",))),
    dv("omelet", '''"Eleven your city ate. I have smelled every one of them on its breath." {n}Her claws close on the stone.{/n} "And one it did not eat, because you had it in your hearth, under a coat of ash, and called it a rock."''',
       c("Continue", "stole_lane", forbids=("nidalynn.trickster.lied_at_kiln",)),
       c("Continue", "stole_muster", requires=("nidalynn.trickster.lied_at_kiln",))),
    dv("druids", '''"Eleven the golden liars carried off in a handcart." {n}Her claws close on the stone.{/n} "And one they never carried, because you had it in your hearth, under a coat of ash, and called it a rock."''',
       c("Continue", "stole_lane", forbids=("nidalynn.trickster.lied_at_kiln",)),
       c("Continue", "stole_muster", requires=("nidalynn.trickster.lied_at_kiln",))),
    dv("vault", '''"Eleven in your vault, in straw, and a clerk who cannot count." {n}Her claws close on the stone.{/n} "And one that is not in the straw any more, because you had it in your hearth, under a coat of ash, and called it a rock."''',
       c("Continue", "stole_lane", forbids=("nidalynn.trickster.lied_at_kiln",)),
       c("Continue", "stole_muster", requires=("nidalynn.trickster.lied_at_kiln",))),
    dv("destroyed", '''"Eleven on the chamber floor, under the fists." {n}Her claws close on the stone.{/n} "And one the fists never touched, because you had it in your pack, under a coat of ash, and called it a rock."''',
       c("Continue", "stole_lane", forbids=("nidalynn.trickster.lied_at_kiln",)),
       c("Continue", "stole_muster", requires=("nidalynn.trickster.lied_at_kiln",))),
    dv("eleven", '''"Eleven I cannot find." {n}Her claws close on the stone.{/n} "And one in a lime-kiln, screaming loudly enough to carry up here. You had her in your hearth, under ash, and called her a rock."''',
       c("Continue", "stole_lane", forbids=("nidalynn.trickster.lied_at_kiln",)),
       c("Continue", "stole_muster", requires=("nidalynn.trickster.lied_at_kiln",))),
    dv("stole", '''{n}Her head turns at last. One burning eye fixes on you.{/n} "In my lair a story buys a life. You took a life out of my clutch and paid me nothing. Not a story. Not a lie. Nothing."''',
       c('''"The silver is raising her."''', "silver"),
       c('"What do you want for her?"', "want"),
       c('[Lie] "It wasn\'t one of yours."', "lie")),
    dv("lie", '''{n}She breathes in, long and slow, through her nose, a sound like a bellows filling.{/n} "You smell of my child's shell. You have smelled of it since the day it went missing." {n}Something in the eye almost approves.{/n} "That was a poor lie, crusader. You are tired. Try again when you have slept, and I will pretend to believe it. Now listen."''',
       c("Continue", "want")),
    dv("silver", '''"I know who keeps her. I went down to your wall and smelled it: old snow, old metal, bread. A silver in a widow's dress." {n}Her lip lifts off one tooth.{/n} "I know who took her, too. They are not the same."''',
       c("Continue", "want")),
    dv("want", '''"I do not want her." {n}It comes out flat and hard.{/n} "I do not take a hatchling out of a nest where something older than me is sitting on it and has not wronged me. I am hungry, crusader, not stupid. And one day that little screamer will be big enough to fly up this ridge by herself and ask me what she is. I would like to be here for that. I will not spoil it by eating the silver."
"So I bill the thief. A life. You took one; you owe one. I will name it when I choose: tomorrow, or when you are old, or at the edge of the world. And when I name it, you will pay it, and you will not send the silver to argue for you."''',
       c("Continue", "tariff", requires=(BITTEN,)),
       c("Continue", "pay", forbids=(BITTEN,))),
    dv("tariff", '''"And do not think to offer me your arm for it. The bite is my tariff; you pay it every year and I take it every year, and that account is square." {n}The eye narrows.{/n} "This is a bill. You will not enjoy paying it. That is how you will know it is paid."''',
       c("Continue", "pay")),
    dv("pay", '''{n}She waits. The whole tower waits with her, and the Storyteller at the door does not breathe.{/n}''',
       c('"Name it when you like. I\'ll pay."', "named", flags=(EGG_BILL,)),
       c('"And if I won\'t?"', "wont", flags=(EGG_BILL,))),
    dv("wont", '''"Then I will collect it anyway, from whatever of yours is nearest when I come, and you will know it was your refusing that chose." {n}She puts her head back on the sill.{/n} "You will pay. Everyone pays me. Even the dead."''',
       c("[Go down the mountain.]")),
    dv("named", '''"Good." {n}She puts her head back on the sill, and looks at the kiln's smoke again.{/n} "Go down. Tell the silver that the grey one knows, and is not coming. Not for the child." {n}A long, hot breath.{/n} "For the thief, one day."''',
       c("[Go down the mountain.]")),
    # NM1: the druids' door (nidalynn eggs.straw): they left the smallest in the straw, and the Commander took it after.
    dv("druids_straw", '''"Eleven the golden liars carried off in a handcart." {n}Her claws close on the stone.{/n} "And one they left behind in the straw for the bedding, and you carried it up under your coat, and put it in your hearth under a coat of ash, and called it a rock."''',
       c("Continue", "stole_lane", forbids=("nidalynn.trickster.lied_at_kiln",)),
       c("Continue", "stole_muster", requires=("nidalynn.trickster.lied_at_kiln",))),
    # Authored recollections: the existing confession history selects the place, never eligibility or payment.
    dv("stole_lane", '"You stood in the kiln lane and told them what you had done. Good. They know which door to knock on when she starts burning their wagons."',
       c("Continue", "stole")),
    dv("stole_muster", '"You lied in the lane. Then you stood before your garrison at morning muster and took the lie back." {n}One claw scrapes the stone.{/n} "Good. Now they know whose debt it is. So do I."',
       c("Continue", "stole")),
], requires=("trickster.ever", RETURNED, N_CONFESSED), forbids=(SMALLEST,), delay=24)


# --- Epilogue: her committed page remembers what the watchtower made of the years -----------------------------------

VAULT_SPENT = "{n}She had lain once among the eggs in the Drezen vault, by the Commander's leave, with spears at her throat. After the vault was emptied the other way, she never again came down the ridge on that night of the year, and the Commander never asked her to.{/n}"

EPILOGUE_PARAGRAPHS = (
    (NAMED, "{n}The Commander never said her true name aloud, not once, in all the years after. The Commander only knew it, as she had said, and she seemed to find that enough.{/n}"),
    (VAULT_OPENED, "{n}The clutch in the Drezen vault hatched in the end, far from her, into other hands. Every one of the young woundwyrms flew over the north ridge once, as if by accident, before going wherever they went. She watched every one of them out of sight.{/n}"),
    (WATCHED, "{n}There was a hollow at the edge of the old Wound where nothing grew for a hundred years. The Commander never went back to it. She did, every year, on the same day, and burned it again.{/n}"),
    (HIDE_GIVEN, "{n}The old hide lay across the tower door until it crumbled. Pilgrims who climbed the ridge to see the grey dragon had to walk through her dead face to reach her. Very few of them did it twice.{/n}"),
    (ONE_BATTLE, "{n}Once, in the last year of the war, a grey dragon came out of the dawn over a battlefield nobody had told her about and broke a demon host in half, and was gone before the crusaders could cheer. The dispatch did not mention her. The Commander told her the story of that battle the night after, every death in it, and she judged it worth her wings.{/n}"),
    (FREE_STORY, "{n}Sometimes, on quiet evenings, the sentries on the north wall heard the Commander's voice up on the ridge, telling something with no demons in it, and heard the dragon interrupt to ask what colour the dog was.{/n}"),
    (HUNTED_TOGETHER, "{n}The demons at the Wound's edge learned to be afraid of the dawn, and of a grey shadow that came before it, and of a smaller shape on its shoulders that did not need a weapon.{/n}"),
    (TROPHY, "{n}A babau's head, dry as leather, stayed on the Commander's desk for the rest of the war. Generals who came to report that the cause was hopeless found it grinning at them, and tended to leave more hopeful than they came.{/n}"),
    (TAX_EXEMPT, "{n}The east road paid its levy in oxen for the rest of the war, and nobody from the Treasury ever climbed the north ridge again to dispute the rate.{/n}"),
    (ROOF, "{n}Drezen never again ran a book on anything to do with the grey dragon. The man who had run the last one kept the ledger, framed, over his fireplace, with the odds on the last page: a hundred to one, and nobody on the other side.{/n}"),
    (COIN_ASKED, '''{n}The Commander kept the coin with the vanished queen's head and never spent it. Devarra counted it whenever the Commander climbed the ridge, as carefully as the gold still in her hoard.{/n}'''),
    (EGG_BILL, "{n}The smallest egg of her clutch grew up in a lime-kiln under the east wall, raised by someone else, and flew up the north ridge the year it was grown to ask her what it was. She told it.{/n}"),
)


def integrate(payload):
    """Give her committed epilogue page the watchtower's consequences (E14c paragraphs)."""
    from story_format import p
    payload.setdefault("StartedDialogs", {})[VOYAGE] = "a07f6d1f93531e048928c5c9de328a92"   # PP7: AirAdventures_BookEvent
    payload.setdefault("Latches", {})[VOYAGE_SEEN] = [VOYAGE]
    page = next(s for s in payload["Scenes"] if s["Id"] == "devarra.trickster.epilogue.woken")["Nodes"][0]
    # PP7 (Sol CAN): the hatchlings only where the vault's clutch was not cooked or destroyed afterwards; otherwise the visit.
    page.setdefault("Paragraphs", []).extend(
        p(text, requires=(flag,), forbids=(("eggs.omelet", "eggs.destroyed") if flag == VAULT_OPENED else ()))
        for flag, text in EPILOGUE_PARAGRAPHS)
    page["Paragraphs"].append(p(VAULT_SPENT, requires=(VAULT_OPENED, "eggs.omelet")))
    page["Paragraphs"].append(p(VAULT_SPENT, requires=(VAULT_OPENED, "eggs.destroyed"), forbids=("eggs.omelet",)))
    from storylines.devarra_round2 import polish_epilogue
    polish_epilogue(page)
    from storylines.devarra_round3 import epilogue as polish_round3_epilogue
    polish_round3_epilogue(page)
    # Calling her at Last Call never negotiated or settled the missing-life claim.
    page["Paragraphs"].extend([
        p("{n}She had never named what she would take for the life missing from her clutch. When the Commander climbed, she spoke of the smallest egg again before turning to the visitor. The annual bite settled only the promise about the arm.{/n}",
          requires=(EGG_BILL, "devarra.lastcall.called")),
        p("{n}She had never named what she would take for the life missing from her clutch. When the Commander climbed, she spoke of the smallest egg again before turning to the visitor. The annual bite settled only the promise about the arm.{/n}",
          requires=(EGG_BILL,), forbids=("devarra.lastcall.called",)),
    ])


# Authored round-2 set pieces; append-only repairs, with no new eligibility mechanics.
from storylines.devarra_round2 import polish_tower
polish_tower(SCENES)


# struct2-08: append a playable climb without changing the four saved approaches.
_hoard = next(s for s in SCENES if s['Id'] == T + 'the_hoard')
_hoard_nodes = {node['Id']: node for node in _hoard['Nodes']}
_hoard_nodes['her']['Choices'].append(c(
    '[Skip the carters\' switchbacks. Take the ridge face with the first sack on your back.]',
    check=dict(Skill='SkillAthletics', DC=25, Success='climb_checked', Failure='climb_noticed')))
_hoard['Nodes'].extend([
    nar('climb_checked', '''{n}You shoulder the first sack and ignore the switchbacks the carters cut. You take the face instead, fingers in the cracks, boots finding the ledges before you look for them, the weight riding high between your shoulders. You top the ridge without once stopping for breath.{/n}
{n}Devarra has watched the whole climb from the gorge rim, wings half open, as a hawk watches a goat on scree.{/n} "Sure-footed." {n}She does not make it sound like praise.{/n} "A thing that climbs like that has climbed into other people's rooms. I will remember it when I count my doors."''',
        c('Continue', 'honest', flags=(T + 'hoard_climb_sure',))),
    nar('climb_noticed', '''{n}You shoulder the first sack and ignore the switchbacks the carters cut. Halfway up the face a ledge crumbles under your boot, and the sack swings you out over the gorge by its straps. You hang by two fingers and a curse until your toe finds rock again. The rest of the climb you do slowly, with your cheek against the stone.{/n}
{n}Devarra has watched all of it from the rim, and has not moved a claw.{/n} "Remember how that felt. There are ten more sacks." {n}Her tongue touches her teeth.{/n} "I wanted to see how you fall. It is useful to know, before I trust you with the rest."''',
        c('Continue', 'honest', flags=(T + 'hoard_climb_noticed',))),
])

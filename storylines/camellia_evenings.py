"""Camellia: the evenings between the beats (camellia_trickster, camellia_masks).

The same three movements, filled in. Before the kill: the puppy she once had, the fencing masters her father hired, and a
game of reading strangers across a tavern table (her girlhood: Camelia/Cue_0089, Cue_0090, Cue_0092; her ear for a lie:
FinalTruth Cue_0029 b5485676). After the return: a second evening at Fye's bar, or among the chaplains who count the raised
dead; the obituary she writes for herself. After her answer: breakfast, a gift, a prisoner, and a mirror. None of it softens
her. Her appetite is the same appetite; what changes is whom she lets watch it.
"""
from story_format import c, scene
from storylines.camellia_trickster import (CLOSED, COMMITTED, DREZEN, DUE, GRAVE, HUB_LIST, KILLED, LESSON, NEW_NAME, OLD_NAME,
                                           OUT_LIED, P, PRESENCE, PRISONER_HERS, PRISONER_SPARED, REL, RET, SCENES, SHELF,
                                           TOUCHED, UNIT, WITNESS_HERS, WITNESS_LIED, cam, met, nar)
from storylines.camellia_masks import MIREYA, TWO_LIES, living

E = P + "evening."
PUPPY = E + "the_puppy"
SALLE = E + "the_salle"
STRANGERS = E + "a_table_for_strangers"
WIDOW = E + "the_widow_at_the_bar"
CENSUS = E + "the_chaplains_census"
OBITUARY = E + "her_own_obituary"
BREAKFAST = E + "breakfast"
GIFT = E + "a_gift_for_a_dead_woman"
PRISONER = E + "the_prisoner"
MIRROR = E + "the_mirror"



# === Before the kill ====================================================================================================

# --- The puppy. -------------------------------------------------------------------------------------------------------

living(PUPPY, "A barking ball of happiness", '"Tell me about the puppy."', [
    cam("open", '''"The puppy?" {n}Camellia is mending a glove, with tiny, perfectly even stitches, and she does not stop.{/n} "Why would you want to hear about the puppy? It's the dullest story I have. Everybody has a puppy."
{n}Stitch. Stitch.{/n} "Oh. The game. You're still thinking about the game. You want to know whether he was the true thing or the lie."''',
        c('"I want to know what happened to him."', "him"),
        c('"I want to know why you smiled when you said his name."', "smile")),
    cam("smile", '''"Did I?" {n}She touches her own mouth with the back of her hand, as if to check.{/n} "How careless of me. You notice a great deal, my friend. It's very flattering, and a little rude." {n}She bites off the thread.{/n} "Very well. You've earned a story. But I shall tell it properly, from the beginning. I hate stories that start in the middle."''',
        c("Continue", "him")),
    cam("him", '''"I was very small. He had curly fur, and he was always warm, and he slept against my feet." {n}Stitch.{/n} "I don't remember his name. Isn't that dreadful? I've tried. I remember the fur, and how warm he was."
"He followed me everywhere. He was the only living thing in that house who was never afraid of me."''',
        c("Continue", "then")),
    cam("then", '''"The servants were afraid of me, you see. Father changed them whenever they started to suspect anything. New maids every season. They would come in rosy and chattering, and by midsummer they would stop chattering, and by autumn they would stop coming into my room at all. And then there would be new ones."
"But the puppy never stopped coming in. He never once looked at me the way the maids did." {n}Stitch. She has picked up the glove again.{/n} "I found that very restful."''',
        c('"What happened to him?"', "end")),
    cam("end", '''{n}She is quiet for so long that you think she will not answer. Then she holds the glove up to the light to inspect her work.{/n}
"I took a knife from the kitchen one afternoon and cut his head off. I don't remember deciding to. I remember holding the head in my hands, and how warm it still was, and the rest of him at my feet."
{n}She lowers the glove.{/n} "My mother found me. That was the beginning of the doctors."''',
        c('"Why?"', "did"),
        c("[Say nothing]", "did")),
    cam("did", '''"Why." {n}She considers it, needle poised.{/n} "Because he looked at me. Right to the very end, he wasn't afraid of me. He just looked puzzled. As if I were playing a game he didn't know the rules to." {n}Her voice does not change at all.{/n}
"I have been trying, ever since, to find another face that looks at me like that. Only the other way round."''',
        c('"Afraid."', "afraid"),
        c('"That\'s the saddest thing you\'ve ever told me."', "sad"),
        c('[Trickster] "Which part of that was the lie?"', "lie")),
    cam("afraid", '''"Yes." {n}She seems pleased that you understood.{/n} "Puzzled was lovely, but it was only the beginning. I wanted to know what comes after puzzled. What comes when they finally understand." {n}She threads the needle again, first time.{/n} "You have listened very attentively, my friend. I trust it hasn't spoiled your appetite."''',
        c("Continue", "close")),
    cam("sad", '''"Is it?" {n}She tilts her head, genuinely curious.{/n} "I always thought it was rather a sweet story. A girl and her dog. He was very warm, you know. Right to the end." {n}She pats your hand.{/n} "You have a kind heart, my friend. I hope nobody ever takes advantage of it."''',
        c("Continue", "close")),
    cam("lie", '''{n}Her needle stops halfway through the leather.{/n}
"The puzzled look," {n}she says, after a moment.{/n} "I don't remember his face at all. I gave him the look afterwards, because the story is so much better with it." {n}She pulls the needle through.{/n} "You are improving, my friend. Most people ask about the head."''',
        c("Continue", "close")),
    cam("close", '''"There. Now you know all about the puppy, and I shall never tell anyone else." {n}She holds up the finished glove, turning it this way and that.{/n} "A pleasing story, was it not? I tell it so seldom. It loses something every time."''',
        c("[Leave her to her mending]")),
], requires=(TWO_LIES,), delay=48)


# --- The salle. -------------------------------------------------------------------------------------------------------

SALLE_LEADS_OUT = '''"You cheated at my game once, with the truth. I'm going to cheat at yours with this."'''
living(SALLE, "Hit me where it counts", '"You\'re holding two swords. Should I be worried?"', [
    cam("open", '''"Foils." {n}She tosses you one, hilt first, and it is only when you catch it that you see the button on the point.{/n} "Practice blades. My father's fencing master would have fainted to see me use such cheap ones, but the quartermaster had nothing better, and I have been fighting demons. Their reach is quite different from yours."
"In battle you have an army watching you. Tonight I shall have a better view."''',
        c("Continue", "rules")),
    cam("rules", '''"First touch to the body. I shall not count your sleeve. I want to know whether you can keep me away from somewhere that matters." {n}She salutes, very correctly, blade to her lips.{/n} "Let us converse."''',
        c("Continue", "out", requires=(OUT_LIED,)),
        c("Continue", "bout", forbids=(OUT_LIED,))),
    cam("out", SALLE_LEADS_OUT, c("Continue", "bout")),
    nar("bout", '''{n}She is good. She is better than good. She does not fight like a crusader or a duellist. She fights close, always coming in, always inside your guard, the point of her foil forever drifting towards the same place, just under the breastbone, as if it knows the way. Twice she could have touched you and does not. She is watching your face.{/n}''',
        c("[Fight her fairly, blade to blade]", "fair"),
        c('[Trickster] Drop your guard on purpose, and when she comes in, step past her.', "trick"),
        c("[Let her touch you]", "let")),
    cam("fair", '''{n}It goes on a long time. At last, sweating, laughing, she slips under your blade and her button taps you precisely under the breastbone, exactly where she has been aiming all along.{/n}
"Conversation," {n}she says, and does not take the point away.{/n} "You fight very honestly. It's quite touching. You fight as if the other person wants what you want." {n}She presses, just a little.{/n} "I never do."''',
        c("Continue", "close")),
    cam("trick", '''{n}You let your point fall and your face go slack, the look of someone tired who has made a mistake. She comes in like a cat on a bird. You are not there. Your button taps her between the shoulder blades as she passes.{/n}
{n}She turns round very slowly.{/n} "You lied with your whole body," {n}she says.{/n} "You made your face into a lie."
{n}Then she laughs, flushed and furious and delighted, and throws her foil across the room.{/n} "Again. Again, and this time I shan't believe a thing you do."''',
        c("Continue", "close", flags=(TOUCHED,))),
    cam("let", '''{n}You see the point coming and you do not move. The button presses gently under your breastbone and stays there. She stands very still at the end of her blade, and her face is doing something you have not seen it do before.{/n}
"You let me," {n}she says, almost accusingly.{/n} "Why did you let me?"
{n}You tell her you wanted to see what she would look like. She takes the foil away, and for once she has nothing clever to say at all.{/n}''',
        c("Continue", "close")),
    cam("close", '''{n}She returns the foils to their rack.{/n} "Again tomorrow, if the muster allows it. You watched my point more carefully after the first touch. I should like to know what else you learned."''',
        c("[Help her with the foils]")),
], requires=(MIREYA,), delay=48)


# --- A table for strangers (Drezen). -----------------------------------------------------------------------------------

living(STRANGERS, "A table for strangers", '"Buy you a drink, Camellia?"', [
    nar("open", '''{n}She lets you take her to the tavern by the gate, the loud one with the bad wine, and chooses the table in the corner herself, with her back to the wall and the whole room in front of her. She orders something she does not drink.{/n}''',
        c("Continue", "game")),
    cam("game", '''"Another game." {n}She leans her chin on her hand.{/n} "I invented this one as a girl, at my father's windows. You look at a stranger for the length of a breath, and then you tell me the lie they are telling. Everybody is telling one. It's the first thing a person puts on in the morning."
"I'll go first." {n}She nods towards a stout man by the fire, laughing with a group of soldiers.{/n} "Him. He is telling everyone he is happy to be home on leave. He is lying. He has not written to his wife. He is afraid of what she'll say when she sees his hands. They shake."''',
        c('"How can you know that?"', "how"),
        c('"My turn."', "yours")),
    cam("how", '''"Look at the cup. He can scarcely lift it without spilling. And he keeps turning his wedding ring." {n}She glances toward the laughing soldiers.{/n} "They have let him pay for every round. I doubt they will go home with him to explain those hands. Your turn."''',
        c("Continue", "yours")),
    cam("yours", '''{n}She waits, bright-eyed, as you look around the room.{/n}''',
        c('"The barmaid. She says she hates the soldiers. She\'s in love with one of them."', "barmaid"),
        c('[Trickster] "You. You\'re telling everyone in this room you\'re harmless."', "you"),
        c('"The priest in the corner. He\'s not a priest."', "priest")),
    cam("barmaid", '''"Oh, well done." {n}She watches the girl go by.{/n} "Three cups for the scarred one, and she charged him once. She has expensive tastes. I wonder whether his pay will cover them."''',
        c("Continue", "last")),
    cam("priest", '''{n}Camellia glances at the man in grey. Her eyes narrow very slightly.{/n}
"No," {n}she says quietly.{/n} "He isn't, is he. Look at his boots. Those boots cost more than mine. I wonder who paid for his charitable work." {n}She turns her glass a quarter turn.{/n} "I shall remember him. I have a very good memory for people who pretend to be something kind."''',
        c("Continue", "last")),
    cam("you", '''{n}Her face lights up.{/n} "Me? In a room full of people you might safely offend?" {n}She leans across the table.{/n} "Yes. I have been very well behaved tonight. What persuaded you not to believe it?"''',
        c('"Someone who is very, very good at waiting."', "waiting"),
        c('"Someone I want to know better."', "better")),
    cam("waiting", '''"Yes." {n}Barely a breath.{/n} "Oh, yes. That's exactly it." {n}She sits back, and she is quiet for a moment, and when she speaks again her voice is lighter.{/n} "You're a dangerous person to have a drink with, my friend. I'm going to have to do it more often."''',
        c("Continue", "last")),
    cam("better", '''"Better?" {n}She considers you over the rim of her glass.{/n} "You know my dresses, my manners, and my father's purse. Which part did you wish to examine next?" {n}She sets the glass down.{/n} "Do be specific. I dislike disappointing an admirer."''',
        c("Continue", "last")),
    cam("last", '''{n}She walks back with her hand in the crook of your arm. At the citadel gate, a sentry straightens and steps aside for her.{/n} "Such a pleasant evening. Did you see him hurry to open the gate?" {n}Her smile sharpens.{/n} "You shall have to escort me again. He has decided I am a lady worth helping."''',
        c("[Say good night]")),
], requires=(TWO_LIES,), delay=48, chapters=(3, 5))


# --- Before the kill: the gloves she was mending. --------------------------------------------------------------------

GLOVES = E + "the_gloves"
living(GLOVES, "A pair of gloves", '"Are those for me?"', [
    cam("open", '''"They are." {n}Camellia holds them out across the camp table: a pair of riding gloves in soft grey kid, the ones she was mending the night she told you about the puppy. Every seam has been re-sewn in the same tiny, perfectly even stitches.{/n} "They were my father's. He never wore them. He had forty pairs. He'll never notice."''',
        c('"Why give them to me?"', "why"),
        c("[Put them on]", "on")),
    cam("why", '''"Because your hands are always cold. I noticed at the fire. You hold them out to it like a beggar, and then you pretend you were only stretching." {n}She tilts her head.{/n} "And because I like to know where my friends' hands are. Grey kid shows everything. Mud, ash, ink." {n}A small smile.{/n} "Blood, of course. It's very hard to get out of grey."''',
        c("[Put them on]", "on")),
    cam("on", '''{n}They fit perfectly, which is impossible, because you have never told her the size of your hands. She watches you flex your fingers with the absorbed satisfaction of a tailor.{/n}
"There. Now I shall always know you by your hands, even in the dark." {n}She reaches out and straightens the cuff of the left one, very precisely.{/n} "I measured them while you slept, one night by the fire. You didn't wake. You never do, when I'm near. I find that very touching, and very foolish."''',
        c('"You measured my hands while I slept?"', "slept"),
        c('[Trickster] "I was awake. I wanted to see what you\'d do."', "awake")),
    cam("slept", '''"With a ribbon. It took no time at all." {n}She says it as though it were the most natural thing in the world.{/n} "Your left hand was hanging out from under the blanket. I measured that one first. You did not even stir." {n}She laughs.{/n} "Oh, your face. I have not measured your throat yet. I should like you awake for that."''',
        c("Continue", "close")),
    cam("awake", '''{n}Her hand stops on your cuff. For the length of a breath she is perfectly still, the way she goes still when she is listening to something nobody else can hear.{/n}
"You were awake." {n}Very softly.{/n} "You lay there and let me measure you with a ribbon in the dark, and you never moved." {n}Then she smiles, slow and radiant.{/n} "That's either brave or insulting. I'll decide later, when it's more convenient for me."''',
        c("Continue", "close")),
    cam("close", '''"Wear them. Always. Especially to battle." {n}She sits back and folds her own bare hands in her lap.{/n} "If anything ever happens to you, I want to be the one who knows which hands they were."''',
        c("[Keep them on]")),
], requires=(PUPPY,), delay=48)


# === After the return ====================================================================================================

# --- The widow at the bar (killed): a second evening at Fye's. --------------------------------------------------------

SCENES.append(scene(WIDOW, "The widow from Nerosyan", "Camellia", 3, '"Mireya. Still here?"', [
    cam("open", '''"Still here. Fye has become very attached to me. I tip in silver and I don't talk and I frighten away the men who try to buy me drinks. He says I'm the best customer he's ever had." {n}She lifts the veil a finger's width and smiles at you under it.{/n} "Sit. I want to show you something."''',
        c("Continue", "room")),
    cam("room", '''{n}She tilts her head at the room: a dozen crusaders, a pair of merchants, a chaplain, two girls from the laundry, all drinking, all talking, all very much alive.{/n}
"Half of the people in this room came to my funeral," {n}she murmurs.{/n} "The one with the eyepatch carried my coffin. The laundry girls cried. The chaplain read the service. And not one of them has looked twice at the widow at the end of the bar."
"The coffin-bearer has seen my veil twice and my face not at all. Keep him talking if he comes over."''',
        c('"Doesn\'t it frighten you, hiding among them?"', "frighten"),
        c('"What are you going to do with it?"', "do")),
    cam("frighten", '''"Frighten me?" {n}She laughs softly into her untouched wine.{/n} "My friend, I spent my whole life being seen. Being watched. Maids who went white when I came into a room, physicians with their little notebooks, priests who crossed themselves over my bed. Father, watching, always watching, to see what I'd do next."
"Now the coffin-bearer is looking straight past me." {n}She lowers the veil.{/n} "He has asked you three times for news from the front. Do keep obliging him."''',
        c("Continue", "do")),
    cam("do", '''"Do?" {n}She turns her glass a quarter turn.{/n} "I haven't decided. That's the lovely thing about being dead. There's no hurry. Nobody's expecting anything of me."
{n}Across the room, the crusader with the eyepatch laughs at something, and she watches him with her head a little on one side.{/n} "I could do anything at all," {n}she says, pleasantly.{/n} "He carried my coffin. I wonder how long it would take him to recognize me without this lace."''',
        c('"But you won\'t."', "wont"),
        c('[Trickster] "You could. But then you\'d have to go back to being alive, to enjoy the credit."', "credit")),
    cam("wont", '''"Won't I?" {n}She looks at you, and under the lace her smile is very fond and not reassuring at all.{/n} "You say that as if you'd decided it for me. That's very sweet. It's also very like you." {n}She pats your hand.{/n} "Don't worry. I'm waiting for you. I'm not in the mood for anyone else just now."''',
        c("Continue", "close")),
    cam("credit", '''{n}She stares at you. Then she laughs, genuinely, too loudly for a widow, and two of the laundry girls look round.{/n}
"Oh, that's true," {n}she whispers, when they've looked away.{/n} "That's horribly true. A widow who laughs too loudly is remembered, and a remembered widow is the first person the watch asks about the next body." {n}She shakes her head.{/n} "You've quite spoiled my evening. I shall have to be very dull in public for a month, and save all my interesting habits for my friends."''',
        c("Continue", "close")),
    cam("close", '''"Go on. You're drawing looks. Commanders don't usually sit with widows." {n}She lowers her veil completely.{/n} "Come back soon. Next time I shall choose a quieter table."''',
        c("[Leave her at the end of the bar]")),
    ], requires=("trickster.ever", RET, KILLED, GRAVE), forbids=(CLOSED,), delay=24, last=5, optional=True, Relationship=REL,
    Chapters=[3, 5], ContactUnit=UNIT, Areas=[DREZEN], InteractionHub=PRESENCE))


# --- The chaplains' census (dead otherwise). --------------------------------------------------------------------------

SCENES.append(scene(CENSUS, "The chaplains' census", "Camellia", 3, '"The chaplains want to talk to you. Should I be worried?"', [
    cam("open", '''"Worried? For me? How sweet." {n}Camellia is sitting on an ammunition crate outside the chapel tent with her ankles crossed, holding a long list in her lap.{/n} "They're taking a census of everyone who has been raised this season. They want to know what I saw on the other side. They have a form."
{n}She turns it round to show you. It is a very long form.{/n} "I've been filling it in. I'm on the second page."''',
        c('"What did you write?"', "wrote")),
    cam("wrote", '''"Question four: 'Did the deceased perceive a light, a presence or a voice?' I wrote: 'Yes, a voice. It was very rude, and told me I was overacting.'" {n}She beams.{/n}
"Question seven: 'Did the deceased wish to return?' I wrote: 'Not particularly.' Question nine: 'Has the deceased experienced any changes of temperament since?'" {n}She taps the page with the pencil.{/n} "I haven't answered that one yet. What do you think I should put?"''',
        c('"Put \'no\'. It\'s true."', "no"),
        c('[Trickster] "Put \'Yes. She\'s become much nicer.\' They\'ll never check."', "nicer"),
        c('"Leave it blank."', "blank")),
    cam("no", '''"'No changes of temperament.'" {n}She writes it, in her beautiful schoolroom hand.{/n} "That is true, isn't it? I'm exactly the same as I was. Isn't that reassuring?" {n}She looks up at you, and waits, and you realise she is waiting to see if you find it reassuring.{/n}''',
        c("Continue", "chaplain")),
    cam("nicer", '''{n}She laughs so hard that she has to put the pencil down.{/n} "'Much nicer.' Oh, they'll put that in a report. They'll send it to Nerosyan. Some bishop will read it and weep for joy." {n}She writes it down, very neatly, and underlines it twice.{/n} "There. Now it's official. I'm nicer. You've made an honest woman of me."''',
        c("Continue", "chaplain")),
    cam("blank", '''"Blank." {n}She considers the empty line.{/n} "Yes. I like that. Let them wonder. They'll read it by candlelight and wonder, for the rest of their lives, what the raised shaman meant by leaving question nine blank." {n}She hands you the pencil.{/n} "You should do it. It should be in your hand. You're the one who raised me."''',
        c("Continue", "chaplain")),
    nar("chaplain", '''{n}The flap of the chapel tent opens and a young chaplain comes out, a thin man with ink on his fingers. He sees Camellia and stops. He sees you, and some of the colour comes back into his face. He holds out his hand for the form, and she gives it to him with a charming smile, and he goes back inside without reading it.{/n}''',
        c("Continue", "after")),
    cam("after", '''"He's afraid of me." {n}She watches the tent flap settle.{/n} "They all are, here. They don't know why. The chaplain folded my answers without reading them. He can pray over those, if he likes." {n}She smooths her skirt.{/n} "It's so much nicer when people are afraid of me for no reason. It's like being loved."''',
        c("[Walk her back to camp]")),
    ], requires=("trickster.ever", RET, DUE), forbids=(CLOSED, KILLED), delay=24, last=5, optional=True, Relationship=REL,
    AnswerLists=[HUB_LIST], ContactUnit=UNIT))


# --- Her own obituary (both branches). --------------------------------------------------------------------------------

met(OBITUARY, "An obituary, corrected", '"What are you writing?"', [
    cam("open", '''"My obituary." {n}She does not look up from the page.{/n} "The one the crusade printed was dreadful. 'A noble daughter of Kenabres, taken before her time.' Taken. As if I were an umbrella someone left in a carriage."
"So I'm writing a better one. For you. Nobody else will ever read it." {n}She blots a line.{/n} "Would you like to hear it?"''',
        c('"Yes."', "read")),
    cam("read", '''{n}She clears her throat and reads, in the clear, carrying voice of a governess reciting to a class.{/n}
"'Camellia Gwerm, illegitimate daughter of a man who kept her behind bars and called it love. Spirit shaman. Liar. Collector of dried flowers and friends. She had many friends. She outlived nearly all of them.'"
{n}She glances up.{/n} "Is that too much? I worried it was too much."''',
        c('"It\'s honest."', "honest"),
        c('"Go on."', "more", requires=(KILLED,)),
        c('"Go on."', "more_d", forbids=(KILLED,))),
    cam("honest", '''"It's honest." {n}She seems pleased, and faintly surprised, as if you had complimented a dress she had not expected anyone to notice.{/n} "I crossed out 'beloved' three times. It kept making the next sentence sound ridiculous." {n}She dips the pen.{/n} "There's more."''',
        c("Continue", "more", requires=(KILLED,)),
        c("Continue", "more_d", forbids=(KILLED,))),
    cam("more_d", '''"'She died once, on a battlefield, of nothing in particular. A friend stood over her body and told it that it was overacting. She got up, out of sheer offence.'"
"'She is survived by that friend, and by her spirit Mireya, of whom the less said the better.'" {n}She stops. The pen hovers.{/n} "I don't know how to end it. They always end with something about peace. 'She is at peace now.' I have never been at peace in my life, not for a single hour. It would be the one lie on the page."''',
        c('[Trickster] "End it with \'To be continued.\'"', "continued"),
        c('"End it with my name."', "name"),
        c('"Leave it unfinished."', "unfinished")),
    cam("more",'''"'She died once, at the word of a friend, who told her to do it convincingly. She did. She was not a woman who did things halfway.'"
"'She is survived by that friend, and by her spirit Mireya, of whom the less said the better.'" {n}She stops. The pen hovers.{/n} "I don't know how to end it. They always end with something about peace. 'She is at peace now.' I have never been at peace in my life, not for a single hour. It would be the one lie on the page."''',
        c('[Trickster] "End it with \'To be continued.\'"', "continued"),
        c('"End it with my name."', "name"),
        c('"Leave it unfinished."', "unfinished")),
    cam("continued", '''"'To be continued.'" {n}She writes it. She sits back and looks at it, and slowly, delightedly, she begins to laugh.{/n} "Oh, that's perfect. That's so perfectly vulgar. Like the end of a chapbook." {n}She blows on the ink.{/n} "The chaplain would hate that ending. I wish he could read this one."''',
        c("Continue", "done")),
    cam("name", '''{n}She holds the pen above the page until a drop of ink falls. Then she writes it, slowly, at the bottom of the page: your name, in her careful hand. She looks at it the way she looks at a knife she means to keep.{/n}
"There," {n}she says softly.{/n} "Now it ends with the only thing I'm sure of." {n}She folds the paper in three.{/n} "That's more romantic than anything I've ever said out loud. You're a very bad influence."''',
        c("Continue", "done")),
    cam("unfinished", '''"Unfinished." {n}She considers it, pen still raised.{/n} "Yes. Like a sentence someone else has to end." {n}She puts the pen down.{/n} "I'll keep it like that. And when I really do die one day, you can finish it. You'll know what to write. You're the only one who will."''',
        c("Continue", "done")),
    cam("done", '''{n}She folds the obituary and gives it to you. It is warm from her hands.{/n}
"Keep it somewhere safe. Somewhere you'll find it again." {n}She stands, and her voice changes; the governess is gone and something harder is in its place.{/n} "And now leave me alone for a while. There are details I have yet to decide. I want to get it exactly right."''',
        c("[Take it and go]")),
], requires=("trickster.ever", RET, LESSON), delay=24, optional=True)


# === After her answer =====================================================================================================

# --- Breakfast. -------------------------------------------------------------------------------------------------------

met(BREAKFAST, "Breakfast", '"You\'re awake early."', [
    cam("open", '''"I never sleep late. Sleep is a waste of the only time nobody is watching me." {n}She is sitting cross-legged at the end of your bed in your shirt, eating bread and honey off a knife, which she licks after every bite.{/n} "I brought breakfast. I've never brought anyone breakfast before. I had to ask the cook how it's done. He was terrified."''',
        c('"What did you tell him?"', "cook")),
    cam("cook", '''"I told him the Commander had a guest, and the guest was very hungry, and very particular, and did not like to be kept waiting." {n}She takes another bite.{/n} "All true. He gave me the good honey. He kept looking at my hands."
{n}She holds out the knife to you, with bread on it.{/n} "Here. Try it. It's lovely. I didn't do anything to it. I promise."''',
        c("[Eat it off the knife]", "ate"),
        c('[Trickster] "You first."', "first"),
        c('"Do you ever say \'I promise\' and mean it?"', "promise")),
    cam("ate", '''{n}You take the bread off the blade with your teeth, carefully. She watches you do it with enormous interest, and when you have swallowed she lets out a long, soft breath, as though she has been holding it.{/n}
"You just did that. You just ate something a murderess held out to you on a knife, first thing in the morning, without even looking at it first." {n}She shakes her head, wondering.{/n} "You are either the bravest person I have ever met or the stupidest. I adore not knowing which."''',
        c("Continue", "close")),
    cam("first", '''"Me first?" {n}She looks offended for exactly one heartbeat, and then enchanted.{/n} "You think I might have poisoned your breakfast. At breakfast. How romantic." {n}She eats the bread off the knife in one bite, chews, swallows, and licks the blade clean.{/n} "There. If I die, you'll know. And if I don't..." {n}She cuts another piece.{/n} "You'll never be quite sure I didn't simply have the antidote."''',
        c("Continue", "close")),
    cam("promise", '''"Sometimes." {n}She considers.{/n} "I promised a priest once I'd be kind to the spirits. I have been." {n}She licks honey off her thumb.{/n} "I've kept every promise I ever meant. There are only a very few of them. It's why I make so many that I don't. It hides the real ones."
{n}She holds out the knife again.{/n} "Eat your breakfast."''',
        c("Continue", "close")),
    cam("close", '''"We should do this every morning. I'll bring the bread, and you'll decide whether to trust me, and neither of us will ever get bored." {n}She settles back against the bedpost, your shirt slipping off one shoulder, the knife held loosely in her lap.{/n} "It's the most domestic thing I've ever done. I'm finding it strangely exciting."''',
        c("[Finish breakfast]")),
], requires=("trickster.ever", COMMITTED, SHELF), delay=24, optional=True, living=())


# --- A gift for a dead woman. -----------------------------------------------------------------------------------------

met(GIFT, "A gift for a dead woman", '"I have something for you."', [
    cam("open", '''"For me?" {n}She sets down whatever she was reading, and folds her hands in her lap, and looks at you exactly like a little girl on her birthday.{/n} "A present? How attentive. Father gave me things. Dresses. Books. A puppy. A present is something someone chooses because it's you. Let us see how well you have observed me."''',
        c("Continue", "choose")),
    cam("choose", '''{n}She waits, her eyes going to your hands, your pockets, your face.{/n} "Well? I'm dying of suspense. Only a little. Only figuratively. I've done the other kind."''',
        c('[Trickster] Hand her a set of papers in a new name, with a Nerosyan address and a forger\'s thumbprint still smudged on the wax.', "papers"),
        c("Give her a charcoal rubbing of her own gravestone, framed.", "stone", requires=(KILLED,)),
        c("Give her a pair of fencing foils with real points.", "foils")),
    cam("papers", '''{n}She breaks the seal, and reads, and her eyebrows go up, and up.{/n}
"'Mireya Voss, widow, of Nerosyan. Born in Taldor. No known relations.'" {n}She looks at you over the top of the paper.{/n} "You've made me a person. You've made me a whole new person, with a street and a widowhood and a dead husband. Who was he?"
{n}You tell her he was a wine merchant who died of a surfeit of eels. She presses the papers to her chest.{/n} "I shall wear her to every party. She'll be much better company than I am."''',
        c("Continue", "close", flags=(NEW_NAME,))),
    cam("stone", '''{n}She unwraps it, slowly, and then she is very quiet for a long time, looking at the charcoal letters of her own name and the date of her own death, pressed off stone onto paper.{/n}
"You went to my grave," {n}she says at last, softly.{/n} "Without me. You knelt in the grass and rubbed charcoal over my name. So that I could keep it."
{n}She traces the letters with one finger.{/n} "My name. You kept it." {n}Her mouth tightens, then smooths.{/n} "How sentimental. I'll allow it, for now."''',
        c("Continue", "close", flags=(OLD_NAME,))),
    cam("foils", '''{n}She draws one from its sheath and tests the point on her thumb. A bead of blood wells up. She looks at it, and then at you, and her smile is slow and radiant.{/n}
"Real points." {n}She sucks the blood off her thumb.{/n} "You want to fence with me with real points. You want to converse with me properly." {n}She salutes you with the naked blade, very correctly.{/n} "Now we'll find out which of us is sentimental."''',
        c("Continue", "close")),
    cam("close", '''"I have nothing for you. I didn't think." {n}She says it with a small, perplexed frown, as if she had forgotten something as basic as her own name.{/n} "I'll think of something. I'm very good at thinking of things. I'll give you something nobody else could possibly give you."
{n}She smiles.{/n} "Don't look so worried. It won't be anyone you know."''',
        c("[Take her hand]")),
], requires=("trickster.ever", COMMITTED, SHELF), delay=48, optional=True)


# --- The prisoner. ----------------------------------------------------------------------------------------------------

met(PRISONER, "The prisoner", '"Camellia. They told me you were in the cells."', [
    nar("open", '''{n}The cells under the citadel are cold and badly lit. In the last one, a demon cultist sits chained to the wall: a man with the horned head of the Lord of Beasts cut into his forearms, captured on the walls three nights ago. He has not said a word to the interrogators. Camellia is sitting on a stool in front of him, very close, with her hands in her lap, looking at his face.{/n}''',
        c("Continue", "her")),
    cam("her", '''"He killed a child on the walls," {n}she says, without turning round.{/n} "A drummer boy. Twelve years old. He cut his throat in front of the boy's sergeant and laughed. The interrogators have told me all about it. They are very angry. They want me to make him talk."
{n}She tilts her head. The cultist stares back at her with dull, hating eyes.{/n} "I don't care whether he talks. I've been sitting here for an hour, looking for the thing I look for. He hasn't got it. He isn't afraid of anything. He's quite, quite empty. Like a room with the furniture taken out."''',
        c("Continue", "ask")),
    cam("ask", '''"But he would be. Afraid. At the end. I know how." {n}Now she turns round. Her face is calm and flushed and very beautiful.{/n}
"He isn't anyone's friend. He isn't on any list. Nobody would ever miss him; nobody in the whole world has ever loved him. The spirits would drink him and thank me." {n}She holds out her hand to you.{/n} "I'm asking you. Can I have him?"''',
        c('"He\'s yours."', "yes"),
        c('"No. He goes to trial."', "no"),
        c('[Trickster] "Only if I can watch your face, not his."', "watch")),
    cam("yes", '''"Thank you." {n}She says it quite simply, the way one thanks a friend for passing the salt. She takes a small, clean knife from her sleeve.{/n} "You should go now, my friend. Or stay. It's up to you. I know it isn't pretty."
{n}You leave. Behind you, as the door closes, you hear her begin to talk to him, softly, pleasantly, as if she were telling him a bedtime story. The guards on the stair do not look at you. Later, the chaplain records that the prisoner died in his chains of a failure of the heart.{/n}''',
        c("[Walk up into the light]", flags=(PRISONER_HERS,))),
    cam("watch", '''{n}Camellia blinks, then smiles.{/n} "My face? How discerning."

{n}You stand against the wall. She watches you over the prisoner's shoulder while she works. His breath catches, breaks into a wet rattle, and stops. Her eyes stay on yours. Afterward she washes her hands in the bucket and dries each finger before approaching you.{/n} "Well, my friend? You had a very good view."''',
        c("[Hold her]", flags=(PRISONER_HERS,))),
    cam("no", '''{n}For a moment you see it: the flash of something bright and furious behind her eyes, gone almost before it is there, the look of a woman who has had her plate taken away.{/n}
"Trial," {n}she says.{/n} "Of course. How very correct of you."
{n}She stands, and straightens her skirt, and walks past you to the door. She stops beside you, close enough that her breath touches your ear.{/n} "One day you'll say yes. I can wait. I'm very, very good at waiting." {n}She kisses your cheek, and goes up the stair.{/n}''',
        c("[Let her go]", flags=(PRISONER_SPARED,))),
], requires=("trickster.ever", COMMITTED), any_groups=[[WITNESS_LIED, WITNESS_HERS]], delay=48, optional=True, living=())


# --- The mirror. ------------------------------------------------------------------------------------------------------

MIRROR_LEADS_NEW = '"Mireya Voss, widow of Nerosyan." {n}She tries a curtsey at the glass, then lifts her chin.{/n} "Too deep. Her husband left her money. She need not be grateful to every fool who opens a door."'
met(MIRROR, "The mirror", '"You\'ve been at that mirror for an hour."', [
    cam("open", '''"Have I?" {n}She is standing in front of the long glass in your room with the black veil in her hands, putting it on and taking it off, putting it on and taking it off, watching her own face appear and disappear.{/n} "I'm practising. I've been three people this year. Camellia, and a dead woman, and whoever I am now. I keep forgetting which face I've got on."''',
        c("Continue", "voss", requires=(NEW_NAME,)),
        c("Continue", "which", forbids=(NEW_NAME,))),
    cam("voss", '''"Mireya Voss, widow of Nerosyan." {n}She tries a curtsey at the glass, then lifts her chin.{/n} "Too deep. Her husband left her money. She need not be grateful to every fool who opens a door."''', c("Continue", "which")),
    cam("which", '''"Father brought healers to the house when I was small, and clerics, and in the end exorcists. I remember their faces better than my own. The clerics had a face for praying over me: very gentle, and a little afraid to touch." {n}She lowers the veil.{/n}
"I used to copy it in the glass, afterwards, so I would know it when I saw it again. Or I tell myself I did. I tell myself a great many things about that house. Some of them are even true. I never once practised my own face. I never knew what it was supposed to look like."''',
        c('"Let me show you."', "show"),
        c('[Trickster] "Try mine."', "mine"),
        c('"Maybe it looks like this. Like now."', "now")),
    cam("show", '''{n}You stand behind her, and put your chin on her shoulder, and look at her in the glass. She looks back at you there, and her face does nothing at all.{/n}
"That's the face you make when you're looking at me," {n}she says slowly.{/n} "I've seen it a hundred times. I was hoping it would tell me something." {n}A small, cold smile.{/n} "It doesn't. It only tells me what you want. You want me to be someone who can be shown things. That's very sweet. It's also the face the clerics had."''',
        c("Continue", "close")),
    cam("mine", '''{n}You make your Commander's face at her: the council-of-war face, the stern one. She copies it in the mirror, perfectly, instantly, down to the line between the eyebrows. Then you make the face you make when you are lying to a demon. She copies that too, and then she stops, and laughs.{/n}
"I know that one," {n}she says.{/n} "That's the face you had when you lied to me best. That's my favourite face in the whole world." {n}She holds it for a moment in the glass, your lie on her mouth, and it fits her far too well.{/n} "May I keep it? I shan't tell you what I'll use it for."''',
        c("Continue", "close")),
    cam("now", '''"Like now." {n}She looks at the woman in the glass, with her hair down and the veil in her hands and no paint on her mouth. Something passes over the reflection's face that does not pass over hers.{/n}
"I don't like her," {n}she says, quite calmly.{/n} "She looks as if she might be about to say something true. Women who say true things in my family end up in the garden, under the roses." {n}She turns the glass to the wall.{/n} "There. Now nobody has to find out what she was going to say."''',
        c("Continue", "close")),
    cam("close", '''{n}She hangs the veil on the corner of the mirror, where it stirs in the draught from the window like something breathing.{/n}
"I'll leave it there," {n}she says.{/n} "In case I need to be dead again. One never knows." {n}She does not look at the glass again that night, and when you wake in the small hours she is standing in front of it in the dark, perfectly still, with the veil in her hands.{/n}''',
        c("[Leave her to it]")),
], requires=("trickster.ever", COMMITTED, SHELF), delay=72, optional=True)

from storylines.camellia_trickster import city  # noqa: E402 (Q8)
city(BREAKFAST, GIFT, PRISONER, MIRROR)
from storylines.camellia_trickster import in_drezen  # noqa: E402 (Q8)
in_drezen(STRANGERS)

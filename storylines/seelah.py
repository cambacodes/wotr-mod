"""Seelah's authored scenes. Stable IDs and choice ordering are save references.

Development draft: the complete campaign and fate branches are still being written.
"""
from story_format import c, n, scene

RELATIONSHIP = dict(
    Title="A place beside the fire",
    Description="Seelah has a talent for finding an evening worth keeping in the middle of a disastrous week. I have begun making excuses to join her.",
    Objective="Make time for Seelah",
    Guidance="Speak to Seelah when she is with the crusade. Give her time between meetings and continue her personal quests. Her friends and convictions remain part of her life.",
    StartedFlag="seelah.started", ClosedFlag="seelah.closed", CommittedFlag="seelah.committed",
    UnavailableFlags=["seelah_dead", "seelah_gone"], FailureFlags=[],
)

SCENES = []


def s(id, title, chapter, entry, nodes, **conditions):
    conditions["forbids"] = tuple(conditions.get("forbids", ())) + ("inhuman",)
    SCENES.append(scene("seelah." + id, title, "Seelah", chapter, entry, nodes,
                        Relationship="seelah", AnswerLists=["417fa384f3250634bb71859fbc913453"], **conditions))


s("boots", "The last dry bench", 1, '"Seelah, are you busy this evening?"', [
    n("start", "Seelah", '''{n}Seelah has claimed a bench near the fire with the determined air of someone defending a breach. Her boots stand upside down beside it. A damp sock hangs from the pommel of her sword.{/n}
"If you need a paladin, give me a moment. If you need this bench, prepare to fight for it."
{n}She shifts her legs before you have answered, making room.{/n}
"Oh, sit down. You're making my feet ache just looking at you."''',
      c('"I came looking for you. The bench is a welcome extra."', "company"),
      c('"I wanted to sit with someone who would not ask me to decide anything."', "rest"),
      c('"You are drying a sock on a sacred weapon."', "sock")),
    n("company", "Seelah", '''"Oh?"
{n}She starts to smile, then looks down at her stockinged feet.{/n}
"Well. You've caught me looking my best. Give me warning next time and I'll have someone sing about the boots."
{n}You sit shoulder to shoulder. Hers is warm through the worn cloth of her sleeve.{/n}
"Was there something you wanted to talk about, or did you come to admire a woman who has finally defeated a buckle?"''',
      c('"I wanted your company for once without a demon trying to kill us."', "meal", flags=("seelah.direct",)),
      c('"The buckle never stood a chance."', "meal", flags=("seelah.playful",))),
    n("rest", "Seelah", '''"I can do that."
{n}She indicates a cloth bundle behind the bench.{/n}
"Except for one decision. There's bread in there, an apple, and a little cheese. If you want more than half the apple, I get more than half the cheese. Looking important won't get you a better share."
{n}For a while she lets the small noises around you fill the conversation. A spoon strikes a bowl. Somewhere beyond the firelight, someone is arguing with a door that will not close.{/n}
"I used to think heroes spent their evenings doing something impressive," {n}she says at last.{/n} "Nobody mentioned the amount of sitting about with wet feet."''',
      c('[Take the apple and settle beside her.]', "meal", flags=("seelah.quiet",))),
    n("sock", "Seelah", '''{n}She looks at the sock with exaggerated alarm.{/n}
"Do you think it will be called upon before it dries? That could be awkward."
{n}Then she laughs and lifts it away, laying it over the edge of the bench instead.{/n}
"It is a good sword. I keep it clean, I keep it sharp, and I try to point it at the right people. I don't think it objects to helping with the laundry."
{n}She nudges the empty place beside her with an elbow.{/n}
"Sit. You can tell me which of us you were worried about."''',
      c('"The sword. It has a reputation to maintain."', "meal", flags=("seelah.playful",)),
      c('"You. I was hoping you had finished work."', "meal", flags=("seelah.direct",))),
    n("meal", "Seelah", '''{n}Seelah unwraps the food and divides the apple in two. She studies the halves, then gives you the larger one without comment.{/n}
"Tell me something," {n}she says.{/n} "When all this is over, what would you do with a whole day that nobody had already claimed?"
{n}She holds up her knife before you can answer.{/n}
"And you are not allowed to say 'rebuild the city.' I mean a day. One ordinary, gloriously wasted day."''',
      c('"Get up late. Find good food. See where the road takes us."', "road", flags=("seelah.day_road",)),
      c('"Stay somewhere familiar with someone I love."', "home", flags=("seelah.day_home",)),
      c('"I have stopped making plans that far ahead."', "plans", flags=("seelah.day_uncertain",))),
    n("road", "Seelah", '''"Us?"
{n}The question arrives quickly enough to surprise her. She takes a bite of her half of the apple while you consider your answer.{/n}
"I am very good company on a road. I know songs, I can carry things, and if we get lost I can look extremely confident until we find someone to ask."
{n}She catches your eye over her half of the apple.{/n}
"That sounds like a day I would like."''',
      c('"Then I am inviting you."', "finish", flags=("seelah.invited",)),
      c('"We should get through tomorrow before choosing a road."', "finish")),
    n("home", "Seelah", '''{n}She turns her half of the apple in her hands, rubbing a bruise in the skin with her thumb.{/n}
"Somewhere with a door that stays closed when you close it. A chair that belongs to you because you bought it, not because you got there first."
{n}Her thumb pauses.{/n}
"I could enjoy that for a day. Perhaps two. After that I would start finding reasons to go out. Whoever loved me would have to put up with a lot of 'I won't be long.'"
{n}She glances sideways at you.{/n}
"Though I might be persuaded to come back before supper."''',
      c('"I would save you a place."', "finish", flags=("seelah.invited",)),
      c('"There would probably be someone worth helping outside."', "finish")),
    n("plans", "Seelah", '''{n}Seelah cuts a blemish out of her half of the apple and drops it into the fire.{/n}
"Then let me make one that isn't very far ahead."
{n}She rests the little knife beside the bread.{/n}
"We finish the food. We sit until our feet stop complaining. And tomorrow, if there's a spare hour, I'm finding you before somebody fills it with work."
{n}She leans back, stretching a tired shoulder.{/n}
"I can manage that much planning. On a good day."''',
      c('"Tomorrow, then."', "finish", flags=("seelah.invited",)),
      c('[Eat the apple and stay a while.]', "finish")),
    n("finish", "Seelah", '''{n}Someone calls Seelah's name. She looks toward the sound, then at the boots waiting beside the fire.{/n}
"If this is a demon attack, tell them I expect a moment's courtesy."
{n}It is a question about a missing blanket. She answers it without getting up. A few minutes later her shoulder settles against yours again, this time with no shortage of room on the bench.{/n}
{n}You stay until the fire needs another log.{/n}''', c('[Bring another log and settle beside her again.]', flags=("seelah.warmth",))),
], Chapters=[1, 2, 3, 5])

s("wager", "A very poor wager", 1, '"Can I tempt you away from work for a while?"', [
    n("start", "Seelah", '''{n}Seelah is balancing an empty cup on the edge of a crate. Three buttons lie in her palm.{/n}
"There you are. I have devised a contest of extraordinary skill."
{n}She tosses a button. It strikes the rim of the cup and disappears beneath the crate.{/n}
"The skill is mostly in retrieving the buttons. But we will come to that."
{n}She offers you the remaining two.{/n}
"Winner chooses what we do with the rest of the evening. If we both miss, we blame the cup."''',
      c('"What did you have in mind if you won?"', "terms"),
      c('"You have invented a game that requires us to sit very close together."', "close"),
      c('"I would rather you simply asked me to spend the evening with you."', "ask")),
    n("terms", "Seelah", '''"There is someone nearby who thinks they can play a lute. I intend to find out whether I can dance well enough to make that true."
{n}She places the cup a little farther from the edge.{/n}
"And if you win? Before you answer, you should know I refuse to polish armor for recreation. Even very important armor."
{n}Her gaze lingers on your face as you consider the question. When you look back, she smiles as though she has been caught doing something she meant to keep doing.{/n}''',
      c('"A dance sounds good. I may need you to teach me."', "dance", flags=("seelah.dance",)),
      c('"A walk. I want a little time when nobody else can hear us."', "walk", flags=("seelah.walk",))),
    n("close", "Seelah", '''"Nonsense. We could sit on opposite sides of the room and shout."
{n}She puts a button in your hand, closing your fingers around it with hers.{/n}
"But then everyone would hear how badly you were losing. I am trying to protect your dignity."
{n}Her hand remains a moment longer than the explanation requires.{/n}
"Or were you hoping to escape me with a walk?"''',
      c('"No. I was admiring your planning."', "dance", flags=("seelah.dance", "seelah.flirted",)),
      c('"I would rather take a walk with you."', "walk", flags=("seelah.walk",))),
    n("ask", "Seelah", '''{n}Seelah looks at the cup, sets it upright, and takes your hand.{/n}
"All right. Will you spend the evening with me?"
{n}She is smiling as she asks, already getting up to leave with you.{/n}
"I had hoped to be impressive for at least three throws before asking. You have saved us both a disappointment. We could dance, if that lute I heard belongs to someone who can play it. Or walk, if it doesn't."''',
      c('"Yes. Show me this dance you were planning."', "dance", flags=("seelah.dance", "seelah.flirted",)),
      c('"Yes. Let us find somewhere to walk."', "walk", flags=("seelah.walk",))),
    n("dance", "Seelah", '''{n}Seelah gathers the remaining buttons and drops them into her pocket.{/n}
"A draw, then. We can both pretend we would have won."
{n}She follows the sound of a lute and persuades its owner to play something you can dance to. The musician is enthusiastic, and occasionally correct. Seelah counts the first steps under her breath. When the tune accelerates without warning, she catches your arm and improvises.{/n}
"That part was intentional," {n}she says, laughing.{/n} "Ask anyone."
{n}Her hand is steady at your back. She moves with the strength you know from battle, made unexpectedly easy by the absence of armor. Once, when the music falters, you both continue for another step rather than let go.{/n}
"I ought to confess something. I never cared who won the game."''',
      c('"You could have asked me to dance at the beginning."', "dance_end"),
      c('[Draw her a little closer for the next turn.]', "dance_end", flags=("seelah.flirted",))),
    n("dance_end", "Seelah", '''{n}She turns under your joined hands and nearly collides with a chair. You catch it. She catches you.{/n}
"The furniture is against us. We shall have to be brave."
{n}The musician, pleased to have inspired such enthusiasm, begins the tune again.{/n}
"One more?" {n}she asks.{/n}
{n}This time, when she takes your hand, she pulls you straight into the turn.{/n}''', c('[Stay for another dance, and arrange another evening together.]', flags=("seelah.evening",))),
    n("walk", "Seelah", '''{n}Seelah collects the two remaining buttons and pockets them.{/n}
"We never finished the game. Well, the cup was cheating anyway."
{n}You do not get far. She stops to return a dropped glove, exchange a few words with a guard, and help lift a stubborn wheel over a rut. At the third interruption she looks apologetically at you.{/n}
"I am making a terrible job of the part where nobody else can hear us."
{n}She leads you away from the busiest path. For several paces you can hear only your own footsteps.{/n}
"There. Nobody to interrupt. I wanted you all to myself for a bit. That's why I keep hunting you down, y'know."''',
      c('"I was beginning to hope that you were."', "walk_end", flags=("seelah.flirted",)),
      c('"I like your company too. The rest, I am not sure of yet."', "walk_end", flags=("seelah.unhurried",))),
    n("walk_end", "Seelah", '''"Good. I didn't want to spend the next week pretending I happened to be everywhere you were. It would have made me look a very poor scout."
{n}Her fingers brush yours as you walk, once, then again. She glances sideways at you with a grin.{/n}
{n}Then she remembers the button under the crate and groans. It came from her only good shirt. You turn back together to look for it.{/n}''',
      c('[Take her hand and arrange another evening together.]', flags=("seelah.evening", "seelah.flirted")),
      c('[Walk beside her and make plans to meet again.]', flags=("seelah.evening",))),
], requires=("seelah.boots",), delay=24, Chapters=[1, 2, 3, 5])

EVENING = [
    n("supper", "Seelah", '''{n}Seelah collects a blanket from her things and spreads it over a patch of dry ground. Her parcel contains bread and two rather flat pastries.{/n}
"They were prettier when I bought them. I had to move a horse. The horse had opinions."
{n}She holds up one of the pastries to inspect the damage.{/n}
"On the bright side, we can eat these without opening our mouths very far."
{n}She takes a bite, sending crumbs down her clean shirt. You share the food, picking at the flattened edges. When you both reach for the same piece, she catches your fingers and keeps them in hers.{/n}
"I was thinking about kissing you," {n}she says.{/n} "Apparently I can't do that and eat at the same time."''',
      c('"Then put the pastry down and kiss me."', "kiss", flags=("seelah.kissed",)),
      c('"I want to kiss you. And tomorrow? Will we still know what to say to each other?"', "worry"),
      c('"I like sitting here with you. The kiss can wait for another evening."', "time", flags=("seelah.unhurried",))),
    n("kiss", "Seelah", '''{n}The distance between you closes. Seelah kisses you, her hand tightening around yours against the blanket.{/n}
{n}When she draws back, her smile has lost its uncertainty.{/n}
"Better than the buttons."
{n}You laugh, and she kisses you again before you can think of a reply.{/n}''',
      c('[Stay with her a little longer.]', flags=("seelah.courting",))),
    n("worry", "Seelah", '''"I've been thinking about tomorrow too."
{n}She picks a loose thread from the blanket, then catches herself and leaves it alone.{/n}
"Well, I can't promise I'll suddenly grow wise and sweet-tempered. You've heard me argue. I'd be caught lying before we finished supper."
{n}She looks back at you.{/n}
"But I want to kiss you. And come hunting for you tomorrow. That's as far as I've got."''',
      c('[Kiss her.]', "kiss", flags=("seelah.kissed",)),
      c('"Then let us start with another evening together."', "time", flags=("seelah.unhurried",))),
    n("time", "Seelah", '''"Then another evening it is."
{n}Her smile droops. She shifts over on the blanket and brushes the crumbs off the patch beside her.{/n}
"Well, at least I've finally said it. I was running out of excuses to sit so close."
{n}She separates the remaining bread into two pieces and gives you one.{/n}
"At least I didn't ruin this. Remember that if anybody asks about my skills as a host."
{n}She eats her share, brushing the crumbs off her shirt with more care this time.{/n}''',
      c('[Make a plan to see her again.]', flags=("seelah.courting",))),
]


s("promise", "An invitation kept", 2, '"I would like another evening with you, Seelah."', [
    n("start", "Seelah", '''{n}Seelah has remembered. That is apparent from the clean shirt, the bread wrapped for two, and the look she gives the person hurrying toward her with a request.{/n}
{n}A young recruit has lost something borrowed from a friend. A little brass clasp, nothing valuable to anyone else. The recruit has already searched alone and is frightened of admitting it is gone.{/n}
"I said I would help if it hadn't turned up," {n}Seelah tells you.{/n} "I also said I would meet you."
{n}She looks from the parcel in her hands to the recruit waiting a few paces away.{/n}
"Two promises, one evening. Wonderful. I can count demons better than that."''',
      c('"Let us help together. We can eat afterward."', "search", flags=("seelah.shared_duty",)),
      c('"Ask someone else to help. I want you to keep this evening for us."', "keep", flags=("seelah.kept_evening",)),
      c('"Go. But choose another time for us."', "later", flags=("seelah.rescheduled",))),
    n("search", "Seelah", '''{n}Relief crosses her face, followed by a small wince.{/n}
"Thanks. I owe you a supper that doesn't start with crawling through the dirt."
{n}The three of you search the ground where the recruit was working. Seelah kneels without worrying about the clean shirt. She finds a nail, a bent spoon, and a coin that the recruit insists cannot be theirs.{/n}
{n}You find the clasp caught in a fold of a discarded sack. The recruit's thanks are so fervent that Seelah has to rescue you from them.{/n}
"Go and return it," {n}she says.{/n} "Before it falls in love with another sack."
{n}When you are alone, she examines the dirt on her knees.{/n}
"This is not quite how I pictured making an impression."''',
      c('"You made one."', "supper"),
      c('"Next time, we leave before anyone can find us."', "supper", flags=("seelah.next_private",))),
    n("keep", "Seelah", '''{n}For a moment she looks disappointed in you. Then her gaze drops to the bread and she lets out a breath.{/n}
"Yes. I did promise."
{n}She finds another willing pair of hands for the search, explains where the recruit has already looked, and returns. As you leave, she glances back at the two figures bent over the ground.{/n}
"They have help," {n}she says as you begin walking.{/n} "So why am I still looking over my shoulder? I promised you this evening. One evening!"
{n}She gives you a rueful smile.{/n}
"If I mention that clasp three more times, you may throw a piece of bread at me."''',
      c('"You wanted this evening too. Come on, before the bread goes stale."', "supper"),
      c('"We can ask whether they found it afterward."', "supper")),
    n("later", "Seelah", '''"I will."
{n}She answers quickly, then frowns and counts on her fingers.{/n}
"Tomorrow, after the evening meal. Come and find me. If somebody tries to grab me for another errand, remind me I already broke one promise to you."
{n}She gives you half the bread before she goes.{/n}
"Thank you," {n}she says, then grimaces.{/n} "Oh, that's a poor substitute for supper together. I'm sorry. I was looking forward to tonight."
{n}She stays long enough to squeeze your hand, then goes to help the recruit.{/n}''',
      c('[Leave her to the search. Meet again another evening.]')),
] + EVENING, requires=("seelah.wager",), delay=24, Chapters=[2, 3, 5])


s("kept", "An evening that belongs to us", 2, '\"Have you kept this evening free?\"', [
    n("start", "Seelah", '''{n}Seelah has a parcel ready when you find her. The brass clasp has been returned, her good shirt has survived the search, and she has found something better than bread for supper.{/n}
"I told everyone I'd be busy tonight. Might have made it sound like a dangerous expedition."
{n}She gives you a conspiratorial smile.{/n}
"It worked. Nobody wants to come along."''',
      c('"You went to all that trouble for me? Thank you."', "supper"),
      c('"Then let us disappear before someone grows brave."', "supper")),
] + EVENING, requires=("seelah.promise", "seelah.rescheduled"), delay=24, Chapters=[2, 3, 5])

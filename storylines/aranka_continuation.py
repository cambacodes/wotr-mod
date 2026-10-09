"""Living-island continuation of earned RanRomance Aranka finales.

New performers and performances are authored dialogue encounters.
Parent romance, compass choices, dream access and Reverie's relationship are read only.
"""
from story_format import c, n, scene
from copy import deepcopy

SCENES = []
ACTOR = "430cba7801b149b4e8494ace6baf4f7c"
AREA = "31bab5549f7ea384186159a238360c8d"
ANSWERS = "5ff8a80442182f84e849b4281f98b9ca"
ETUDES = {
    "aranka.ran_romance": "2e98dbe685f045cdabf88b66e4cde9ff",
    "aranka.ran_reverie_partner": "d4dd8a50613e4d528913d0a24d06fca1",
    "aranka.devil_deception": "0b129925567b68d4fb712b4bee6c0f9a",
    "aranka.devil_contract": "5f72b252bd7fa8d48bd04c27982a4f9c",
}
COMPLETED_QUESTS = {"aranka.ran_quest_complete": "1dacd3dfe1bf47c8a73074814e40b1c8"}
SEEN_CUES = {
    "aranka.ran_keep_final": ["a16f4be6de0a4f35a9b13eca4395d6e5", "61461d05999b46218e7700e6596243b5",
                              "363860bffda1404db6ec996384fe2f26", "43936228f4614272a7c7e25ebaaec2c7"],
    "aranka.ran_wing_dream": ["61461d05999b46218e7700e6596243b5", "363860bffda1404db6ec996384fe2f26",
                             "43936228f4614272a7c7e25ebaaec2c7"],
    "aranka.ran_release_final": ["599e7c0cc51741cda1bc55b787734c57", "fefc9911dde04a76975e9027118c7935",
                                 "f9df40d7d6b346298075b435eee6921c", "e16e5b0b3aea426a888e8bb61c521815"],
    "aranka.ran_failure": ["b18d250fa2fb4fdf9fe4eba04e9d1655"],
}
BLOCKED = ("aranka.extension_closed", "aranka.ran_failure", "aranka.devil_deception",
           "aranka.devil_contract", "devil", "demon", "lich", "swarm")
RELATIONSHIP = dict(
    Title="A song with room to breathe", Description="Aranka has asked me to hear what she is making on the island. Our life together began before these visits.",
    Objective="Visit Aranka between rehearsals", Guidance="After completing her RanRomance story while remaining her lover, speak with the living Aranka on the island in Chapter 5. Allow time between visits.",
    StartedFlag="aranka.extension_started", ClosedFlag="aranka.extension_closed", CommittedFlag="aranka.extension_kept",
    UnavailableFlags=list(BLOCKED[1:]), FailureFlags=[],
)


def s(id, title, entry, nodes, previous=None, delay=24):
    for page in nodes:
        page["Portrait"] = "Aranka"
    SCENES.append(scene("aranka." + id, title, "Aranka", 5, entry, nodes,
        requires=("aranka.ran_romance", "aranka.ran_quest_complete") + ((previous,) if previous else ()),
        forbids=BLOCKED, delay=delay, optional=True, Relationship="aranka", Chapters=[5],
        Areas=[AREA], ContactUnit=ACTOR, AnswerLists=[ANSWERS],
        RequiresAny=["aranka.ran_keep_final", "aranka.ran_release_final"]))


s("the_wrong_refrain", "The wrong refrain", '"What were you singing just now?"', [
    n("start", "Aranka", '''{n}Aranka stops halfway through a phrase. Two people a little farther along the island path finish it for her, loudly and in different keys. She watches them go with the expression of a woman whose joke has been repeated back to her very badly.{/n}
"That is becoming a problem."
{n}She takes your hand, draws you closer, and kisses the corner of your mouth.{/n}
"Hello, my darling! Kiss me again before you go hunting demons in my verses."
"My singing. I taught someone a tune, and now everyone knows it except me. They have improved it. I keep hearing about battles I never put in it. In one version you throw a demon through the moon."
"It was a short verse."
{n}She slips her hand into the crook of your elbow and turns toward a quieter patch of grass. Her pace is easy, but she keeps testing a little run of notes under her breath.{/n}''',
        c('"Tell me what happened to your song."', "history"),
        c('"Save that song for me. I will come back when I can hear it through."', abort=True)),
    n("history", "Aranka", '''{n}She tips her head back to look at the sky, then at you.{/n}
"Have you heard my new tune? Can you sing the last line? And how long can I keep you before the crusade steals you?"
"I have a poor technique. Stay anyway."''',
        c('"How has life been since choosing to be a Dream Warden?"', "keeper", requires=("aranka.ran_keep_final",), forbids=("aranka.ran_release_final",)),
        c('"How does it feel to have given up the compass?"', "traveler", requires=("aranka.ran_release_final",))),
    n("keeper", "Aranka", '''"Larger! I keep remembering colors I cannot name. Then somebody asks whose cup I have stolen."
{n}She checks the cup's base, laughs, and sets it beside the music.{/n}
"Mine, this time. Becoming a Dream Warden has not cured my bad habits. Nor finished this song. Even Elysium can wait for the last verse."
{n}She tugs you close enough to kiss, then turns back to the rehearsal sheet.{/n}
"The crusade can have you later. First, listen."''',
        c('"Have you been thinking about your first flight in the dream?"', "flight", requires=("aranka.ran_wing_dream",)),
        c('"Start with the song."', "song")),
    n("flight", "Aranka", '''"Far too much. Every time I try to describe it, I sound as if I am inventing a more impressive version. The wings, the light, the moment when the ground became somewhere I could choose to leave."
{n}She spreads her hands, searching for the size of the feeling.{/n}
"Then I woke and needed my boots. It was rather difficult to be patient with them."
"I want to fly again. I am not going to solve that by leaping off the island. Please look less alarmed. I have an excellent imagination and occasionally use it before doing something foolish."
{n}She looks up, smiling to herself.{/n}
"I want to sing it! But every verse comes out like a solemn hymn. I was flying, not attending my own funeral."
{n}Her gaze returns to you.{/n}
"Today I shall practice being delighted nearer the ground."''', c('"Let me hear what you are working on now."', "song")),
    n("traveler", "Aranka", '''"I still reach for the compass. Look!" {n}Her fingers close on empty air; she catches your hand instead.{/n}
"I gave it up. I miss Reverie and those impossible roads, but I have songs to finish here. No point searching under my pillow."
{n}She folds a corner of the music to mark a troublesome bar.{/n}
"After the war, somewhere that has never heard your title! I shall find a tune neither of us knows. Today I have this one, and you are going to hear it."''', c('"Tell me what you want to make here."', "song")),
    n("song", "Aranka", '''{n}She sings four quiet lines. The melody seems about to climb into a triumphant finish, then steps down instead.{/n}
"The swallow turns above the road,
The traveler turns below.
Ask at the door who made it home;
Ask at the door who knows."
{n}For a moment you hear the voices from the path fitting their louder ending into the same place.{/n}
"A woman named Sella taught me the first bit. She used to sing while hanging washing between the wagons. A few of the others knew different verses. I thought we could make an evening out of it. People singing what they've carried here. No grand story about how delighted everyone is to be at war."
"There is room beside 'Starward Gaze' for a song that doesn't know where it is going yet. I'd like to hear what happens when we give it some company."
"People changed the ending. I'm not furious about that. That is how songs travel. But now a man has asked me to perform the famous version, with you standing beside me. Apparently the song needs a real Commander to keep the moon in place."
{n}She plucks a stalk of grass and knots it loosely around her finger.{/n}
"I could sing it beautifully. They would cheer. Sella would never get to finish the verse she brought. I would rather try something less certain."''', c('"What are you considering?"', "venues")),
    n("venues", "Aranka", '''"One open circle. Everyone can come, the singers can hear one another, and we might persuade the loudest people that listening is part of an evening. Or we take the songs around in little groups. A handful of listeners at a time. Fewer people, but nobody has to compete with a crowd to be heard."
"I want both. I also want another pair of lungs and a morning in which nobody recognizes me. I can manage one of those things at a time."
{n}She turns the knotted stalk around her finger.{/n}
"Come sing with us! No marching orders. I want a listener who can hear a crooked tune, and a Commander brave enough to sing one."
"And afterwards I want you beside me. I have been thinking about your mouth all afternoon."
{n}The grass ring comes apart as she shows it to you. She laughs and drops it into the grass.{/n}
"There. Already too ambitious."''',
        c('"Try the open circle. I will help you earn their attention."', flags=("aranka.extension_started", "aranka.open_circle", "aranka.rehearsal_agreed")),
        c('"Take the songs around in small groups. Let the listeners come close."', flags=("aranka.extension_started", "aranka.rounds", "aranka.rehearsal_agreed"))),
])

s("where_the_breath_goes", "Where the breath goes", '"Is this a good time to listen to the rehearsal?"', [
    n("start", "Aranka", '''{n}A boot keeps time against the grass. The woman wearing it has a low, warm voice and a habit of closing one eye at a difficult note. Beside her, a bearded man taps two smooth sticks together. Neither pays much attention to your arrival until Aranka makes room for you.{/n}
"Sella, Rovan, this is the person I warned you about."
"You said a brave volunteer," {n}Sella replies.{/n}
"I was giving myself room to be wrong."
{n}Rovan salutes you with a stick. His other hand remains folded close to his chest.{/n}
"I used to sing the upper part," {n}he says.{/n} "Now I sound like a hinge. She's trying to persuade me that percussion is an honorable profession."
"A hinge can be very expressive," {n}Aranka says.{/n} "But I don't want to hear yours hurt itself. Let's try the turn again."
{n}Sella begins. Aranka joins a third above her. The tune goes well until the line about the door, when Sella arrives early and Rovan strikes the sticks after both singers have stopped. All three look in different directions.{/n}''',
        c('[Listen for the point where their timing separates. Perception DC 26.]', check=dict(Skill="SkillPerception", DC=26, Success="heard", Failure="missed", CommanderOnly=True)),
        c('"Could each of you show me your part on its own?"', "separate"),
        c('"My head is full of the war today. Save the next rehearsal for me."', abort=True)),
    n("heard", "Aranka", '''{n}Rovan lifts the sticks when Sella draws breath. Aranka has already begun the next phrase by then. Sella follows her instead of taking the breath she prepared, and the last words hurry out in a cluster.{/n}
{n}Aranka looks surprised, then sings the two lines under her breath. She catches herself at the same place.{/n}
"Oh. I have been filling the gap because I know what comes next."
"I need the gap," {n}Sella says.{/n} "It isn't empty on my side."
{n}They try again. Aranka lets the note end before she breathes. Rovan watches Sella's shoulder and brings the sticks together with her first word. The phrase lands with an ease none of them manages to conceal.{/n}
"There you are," {n}Aranka says, looking at Sella rather than at you.{/n} "Do it once more before I become too pleased with myself."
{n}When the next attempt holds, her knee knocks lightly against yours.{/n}
"You can stay. Apparently you have uses besides being kissed."''', c('[Listen to what Rovan needs from the arrangement.]', "rovan", flags=("aranka.timing_heard",))),
    n("missed", "Aranka", '''{n}You follow the beat with your heel and suggest that Rovan come in sooner. He tries. This time the sticks interrupt Sella's first word. She stops, begins again, then shakes her head.{/n}
"I can't find it now."
{n}Aranka holds up a hand. Rovan lowers the sticks. The little silence feels much larger than the mistake.{/n}
"I followed you straight into that! Rovan, put down the sticks. Sella, give me that phrase again."
{n}Sella rubs her throat. She has been forcing the phrase to fit for longer than you realized.{/n}
"I'll need to stop for today. I don't want to lose my voice proving I can follow an instruction."
{n}Aranka gives her the last water in the flask, then asks her to hum only the beginning. Listening without joining, she finally hears where Sella takes her breath.{/n}
"Tomorrow we begin there. No upper part until yours stands on its own."
{n}Sella promises to return for a short rehearsal. When she has gone, Aranka lets out a sigh and rests her cheek against your shoulder.{/n}
"Next time I look impressed, make sure you deserve it."''', c('[Stay to hear Rovan before ending the shortened rehearsal.]', "rovan", flags=("aranka.timing_missed",))),
    n("separate", "Aranka", '''{n}Sella sings without accompaniment. It is slower than the version Aranka taught you. A breath falls between the question and the door; the pause makes you wait for whoever might answer.{/n}
"Again?" {n}Aranka asks.{/n}
{n}She listens twice. On the third attempt she joins only the final word, and Rovan tries a single tap before the phrase begins.{/n}
"That's where I come in," {n}he says.{/n}
"That's where you might come in," {n}Sella says.{/n} "Let me get used to having a door knocked on while I'm singing about it."
{n}They laugh. Rebuilding the harmony takes most of the rehearsal. You listen for the words while Aranka tries the phrase again, then beams at you when all three parts land together.{/n}
"You have been extraordinarily patient," {n}she says when they stop.{/n}
"Stay for Rovan's part! We have made such progress."''', c('[Ask Rovan which part he wants to keep.]', "rovan", flags=("aranka.timing_patient",))),
    n("rovan", "Aranka", '''{n}Rovan turns the sticks between his fingers.{/n}
"I don't mind keeping time. I mind everyone introducing me as the man who used to sing. They look so sorry that I end up comforting them. Then they ask whether I've tried a priest. Yes. Several. I know what my throat can do today."
"What should I call you?" {n}Aranka asks.{/n}
"Rovan would be a daring experiment."
"Rovan it is."
{n}He demonstrates a roll, catches one stick against the other, and ruins the flourish by dropping it. Aranka laughs. He bows from the waist without standing.{/n}
"That part was intentional."
"Excellent. We need a little suspense."
{n}When he leaves, Aranka picks up the stick he forgot and calls him back. He returns at a theatrical crawl, retrieves it, and leaves with the dignity of a man who knows everyone watched.{/n}
"I had a whole speech ready about courage," {n}she admits to you.{/n} "He would have hated it."
"You receive too many speeches already. I shall tell you something dreadful about your singing instead."''', c('"You are very sure you can improve my singing."', "lesson")),
    n("lesson", "Aranka", '''{n}She gives you three notes. You miss the highest; she bites back a laugh and tries again. Her fingers press your ribs just as you draw breath. This time she misses her own note.{/n}
"Oh! That's your fault. Stand there. Farther. I mean to finish this rehearsal."
{n}She steps back and gives you the phrase again. Beyond her shoulder, Sella is waiting with the open song sheet and Rovan taps an impatient beat.{/n}
"One line for you, or a seat among the listeners? Decide before they sack their splendid conductor."''',
        c('"Give me one line. I will learn it before the performance."', flags=("aranka.sings_line", "aranka.rehearsal_kept")),
        c('"Find me among the listeners. I will be paying attention."', flags=("aranka.listens_close", "aranka.rehearsal_kept"))),
], "aranka.rehearsal_agreed")

s("the_name_missing", "The name missing from the song", '"You said someone wanted to speak to us."', [
    n("start", "Aranka", '''{n}The woman waiting with Aranka has folded her cloak into a narrow bundle. She grips it so tightly that the knuckles of one hand show pale. Aranka's greeting is quiet.{/n}
"This is Neris. She heard a verse I was trying."
"The one about a man who went back for his friends," {n}Neris says.{/n} "He didn't."
{n}Aranka looks down at the grass between them.{/n}
"I didn't use a name."
"You used the red gate and the blue scarf. Everyone who was there knows whose scarf it was."
{n}Neris unfolds the cloak, then folds it again without looking at it.{/n}
"His name was Deren. He was my brother. He left us before the fighting began. I waited at the gate because he told me to. I waited until I could see the smoke coming down the street. I don't know where he went. Don't give him a brave death because it's easier to sing."
{n}The island's ordinary noises continue around the three of you. Aranka has stopped moving entirely.{/n}''',
        c('"Aranka, where did you hear that version?"', "account"),
        c('"I should hear this when I can give it my full attention."', abort=True)),
    n("account", "Aranka", '''"From a man who came north with them. He saw the scarf at the gate. He thought Deren must have turned back. I thought..."
{n}Aranka exhales through her nose.{/n}
"I thought it would make a fine verse. I wanted to sing it."
"I needed him to come back," {n}Neris says.{/n} "That is different."
"Yes."
{n}Neris turns and looks straight at you.{/n}
"I'm not asking you to find him. I have asked enough people who needed me to believe they could. I'm asking her to stop singing that I was rescued by a man who wasn't there."
"I was alone until a woman with a broken cart took me with her. I didn't learn her name. There wasn't time to ask everyone to become part of a song."
{n}Aranka's face changes. She had begun to reach for a thought; she lets it go.{/n}
"I sang it wrong. Deren comes out of the verse."
{n}Neris loosens her grip on the cloak. It takes her a moment to believe that the argument has ended.{/n}''', c('[Stay while Aranka tells her what she will change.]', "correction")),
    n("correction", "Aranka", '''"Some people already heard it," {n}Aranka says.{/n} "Taking it out won't make them forget. I can tell them I got it wrong when we perform. I can also speak to the man who told me, so he stops repeating my version as if I confirmed his."
"Without inviting them to come and ask me?"
"Without giving them your name."
{n}Neris nods once. "I will be nearby until tomorrow if you forget any of it." She gathers her cloak and walks away. Aranka watches her go.{/n}
{n}Aranka watches the empty space where she stood.{/n}
"I liked that verse. I was pleased with it. I could hear people singing it before I'd finished."
"And now I could sing a fine verse about my own mistake and have them clap for that! Oh, no. I have had quite enough of that cleverness."
{n}She rubs both hands over her face, then drops them.{/n}
"Listen. I have two endings, and neither is going to smuggle him back through that door."''', c('[Listen to the two endings she is considering.]', "endings")),
    n("endings", "Aranka", '''{n}The first version ends with the traveler reaching a lighted house. The door opens, but the words do not say who stands behind it. Aranka lets the final chord rest without filling the silence.{/n}
"That is as far as the singer knows," {n}she says.{/n} "We can stop there."
{n}The second gives the last question to the listeners. Each may answer with the name of someone they actually met on the road, or let the question pass. The melody leaves enough room for an awkward answer.{/n}
"A tremendous mess. Somebody will say a horse. Somebody will say your name and expect a speech. But someone might remember the woman with the cart. Or their own person, who did something worth remembering without doing it beautifully."
"I cannot know what they will say. That makes me want to try it. It is also what makes me want to sit under a tree and sing to myself."
{n}She tests the unresolved chord again. You can hear her liking it.{/n}
"Choose what you would want to hear. I need an answer from a listener, not a pardon."''',
        c('"Leave the door open. Let the unfinished question stand."', "door"),
        c('"Give the last question to the listeners. Make room for an answer you cannot rehearse."', "answers")),
    n("door", "Aranka", '''{n}She sings it once without looking at you. The last note hangs for a moment above the grass. No one rushes to finish it.{/n}
"I'll need to teach the others not to tidy that up. Rovan will want one more tap. I will want one more word."
"I shall leave out that last word, with great and visible suffering."
{n}The joke is small, but it brings her back toward you. She takes your hand and folds it between both of hers.{/n}
"You heard that dreadful verse and stayed to hear the better one. I shall have to sing it well enough to deserve such devotion!"
"You missed a compliment there. I keep records."
{n}She touches your fingers to her lips, then releases them before you can ask for evidence.{/n}
"Come back for the performance. I would like at least one person to know why the ending sounds unfinished."''', c('[Promise to hear the song as she now intends it.]', flags=("aranka.ending_door", "aranka.song_revised"))),
    n("answers", "Aranka", '''{n}She sings the question toward you, then waits. You give her the name of someone who once helped you without waiting to be asked. The name fits badly into the tune. Aranka repeats it anyway, changing the rhythm until the person seems to belong there.{/n}
"Like that," {n}she says.{/n} "No polishing the name into something easier."
"I like that part. When it goes well, it feels as if a song has opened a window. When it goes badly, I shall look at you until you rescue me with the name of a horse."
{n}She leans into you, smiling now without losing the weariness around her eyes.{/n}
"They will still be singing the old verse tomorrow, curse it."
"Then I shall sing this one louder. And if a horse saves the evening, I shall give it a solo."
{n}Her mouth brushes your cheek.{/n}
"Come and see which one we manage."''', c('[Promise to hear what the listeners bring.]', flags=("aranka.ending_answers", "aranka.song_revised"))),
], "aranka.rehearsal_kept", delay=48)

s("an_evening_uncommanded", "An evening uncommanded", '"Are we ready to begin?"', [
    n("start", "Aranka", '''{n}Aranka is warming her voice with a tune that sounds suspiciously like the one she used to tease you during rehearsal. Sella answers from several paces away. She has also brought a familiar solo to follow the new piece, and is quietly testing its opening notes. Rovan turns a stick over the back of his hand, catches it, and looks around to make sure somebody saw.{/n}
"You came," {n}Aranka says.{/n}
"And here you are! Oh, I have been saving the best part for you."
{n}She catches your hand and kisses you before Sella can pretend she is not watching. Rovan supplies a single solemn tap.{/n}
"No accompaniment for that part," {n}Aranka tells him.{/n}
"A waste of my training."
{n}She laughs, then looks back at you with a little flutter of nerves she makes no attempt to hide.{/n}''',
        c('[Ask how the final rehearsal went.]', "ready_heard", requires=("aranka.timing_heard",)),
        c('[Ask whether Sella had time to recover her voice.]', "ready_missed", requires=("aranka.timing_missed",)),
        c('[Listen for the space you found by taking the parts separately.]', "ready_patient", requires=("aranka.timing_patient",)),
        c('"I cannot stay today. Please do not hold the beginning for me."', abort=True)),
    n("ready_heard", "Aranka", '''"We used the time to learn Sella's other verse," {n}Aranka says.{/n} "She knew one about a traveler who arrived home with the wrong husband. I am almost certain it was meant to be comic."
"She sings it with great conviction. Rovan says he knows the husband. I no longer trust either of them."
{n}Sella gives you a broad smile. Her first breath falls exactly where you heard it during rehearsal. This time Aranka waits for it, then joins her without needing to look.{/n}''', c('[Take your place for the evening.]', "venue")),
    n("ready_missed", "Aranka", '''"She rested it," {n}Aranka says.{/n} "We had another short rehearsal after that. I let her begin alone, and we kept the upper part lower."
{n}Sella hums the turn for you, then stops before the higher note.{/n}
"Enough to know it's there. I'll save the rest for the people listening."
"We dropped the longest repeat," {n}Aranka adds.{/n} "I wanted it, but I want her voice tomorrow more. If anyone demands an encore, Rovan has offered an extremely long solo."
{n}He raises both sticks with such solemn menace that Sella laughs. Aranka waits until the laughter has loosened her shoulders before giving her the next note.{/n}''', c('[Take your place for the shorter arrangement.]', "venue")),
    n("ready_patient", "Aranka", '''{n}The pause is still there. Sella takes it without looking apologetic, and Rovan waits for her instead of chasing Aranka's faster version.{/n}
"We tried it with someone walking past," {n}Aranka says.{/n} "She stopped long enough to hear the last line. Then she asked for the beginning. I am taking that as encouragement."
"We did. She corrected a word. Apparently her grandmother's traveler carried a basket, not a bag. We have agreed to leave room for regional luggage."
{n}Sella has the air of a woman who has won a very small argument and intends to enjoy it.{/n}''', c('[Take your place for the evening.]', "venue")),
    n("venue", "Aranka", '''{n}Before beginning, Aranka lifts her face into the wind.{/n}
"Lady of Stars, keep us listening. And if you can persuade the wind to wait until after the quiet part, I would be grateful."
{n}She opens one eye and looks at the grass. It continues to move.{/n}
"We shall project."''',
        c('[Help gather the open circle.]', "circle", requires=("aranka.open_circle",)),
        c('[Join the first small group.]', "rounds", requires=("aranka.rounds",))),
    n("circle", "Aranka", '''{n}People gather unevenly. Some sit close, others remain standing behind them, and a few have evidently come because they heard you would be here. A man calls for the song about the moon.{/n}
"Later," {n}someone promises him.{/n}
"No," {n}Aranka says pleasantly.{/n} "But I have brought a song with a door. Much less expensive to replace if we damage it."
{n}A few people laugh. The man folds his arms. Aranka starts with a quick piece whose chorus gives the listeners something harmless to argue about. By the third repeat, Sella's low part is carrying the melody and the loudest people have stopped trying to hurry it.{/n}
{n}Then someone spots you and begins a cheer. Others stand to see what they missed. The tune breaks apart around the rising noise. Aranka holds the last note for as long as she can, then lets it go.{/n}
"Well," {n}she says to you, quietly enough that only the performers hear.{/n} "You are a very difficult instrument to bring into a room."''', c('[Choose how to give the singers back their evening.]', "attention")),
    n("rounds", "Aranka", '''{n}The first listeners are finishing a meal and make room without much ceremony. Rovan begins a rhythm on the sticks. Sella sings while Aranka supplies a harmony so quiet that people lean toward it before they know they have moved.{/n}
{n}The next group is harder. Two people are arguing over a game, a third wants news, and a woman asks whether the singers know something she can dance to. Aranka gives her half a verse, just enough to make Sella laugh, then asks them to listen to the new song.{/n}
{n}Before she can begin, someone recognizes you. More people drift over. What was a small gathering becomes a ring with no clear place for the singers, and the questions turn toward the war.{/n}
"I thought traveling light would help," {n}Aranka murmurs to you.{/n} "Unfortunately we brought the most conspicuous person on the island."
{n}Sella stays beside Rovan instead of beginning over the conversation. Aranka looks at you, waiting to see what you will do.{/n}''', c('[Choose how to make room for the performance.]', "attention")),
    n("attention", "Aranka", '''{n}The listeners turn toward you. Aranka draws breath, then stops as another voice calls your title from the back of the gathering.{/n}
{n}Aranka rolls her shoulders, loosening them. Her eyes meet yours briefly.{/n}
"Rescue my audience, Commander. They are about to make you sing a speech!"''',
        c('[Invite the listeners to give the singers their attention without making a speech. Diplomacy DC 25.]', check=dict(Skill="CheckDiplomacy", DC=25, Success="welcomed", Failure="ceremony", CommanderOnly=True)),
        c('[Move beside the other listeners and wait for Aranka to begin.]', "step_aside")),
    n("welcomed", "Aranka", '''{n}You tell them you have spent enough of the day being heard. There are other voices you came to listen to. Then you sit down before the sentence can become a speech.{/n}
{n}The pause catches. A few people who had been standing follow your example. Aranka looks at you over their heads, and the corner of her mouth lifts.{/n}
"A remarkably short introduction. I might employ you again."
{n}She introduces Sella and Rovan by name. Rovan performs his little roll without dropping either stick, which earns a cheer he accepts as if nothing else could have been expected.{/n}
{n}Aranka lets the pleasure settle before changing the mood. When she explains that she had repeated a story she could not verify, the listeners are quiet enough to hear the correction. She names neither Neris nor the blue scarf. She says plainly that the brave return she sang about was invented.{/n}
"Tonight you will hear the song without it."
{n}Someone shifts uncomfortably. Someone else nods. Aranka takes her first breath without asking either reaction to become applause.{/n}''', c('[Listen as the song begins.]', "part", flags=("aranka.crowd_welcomed",))),
    n("ceremony", "Aranka", '''{n}You begin well, then mention what an evening like this means to the people fighting the war. A listener straightens. Another rises. Before you reach the invitation, someone has started a solemn cheer.{/n}
{n}Aranka closes her eyes for one brief, visible moment.{/n}
"Thank you," {n}she says when the cheer ends.{/n} "We are now going to sing about several people who were late getting home. Nobody needs to stand."
{n}The laughter is uncertain. A few listeners leave, having received the moment they expected from you. You move to the side while Aranka starts a brisk nonsense verse to loosen the remaining crowd. It takes two attempts before Sella joins her.{/n}
{n}The original opening has gone. Aranka asks Sella to leave out her separate solo to keep the evening from running too long. Sella agrees without looking pleased. Then Aranka tells the smaller audience why she has changed the verse they may already know. Her voice is clear, although her hands keep moving against her skirt.{/n}
"I gave it a brave ending I had no right to claim. I have taken that ending out."
{n}She glances toward you once. You stay where she can see you and let her finish.{/n}''', c('[Hear the shorter performance through.]', "part", flags=("aranka.crowd_ceremony",))),
    n("step_aside", "Aranka", '''{n}You move out of the singers' space and sit among the listeners. For a while people keep trying to catch your eye. You return your attention to Aranka until most of them follow it.{/n}
{n}Some leave when no speech arrives. Rovan watches them go. Aranka touches his shoulder, then gives him the beat. He brings the sticks together, and Sella begins so softly that the remaining listeners have to settle to hear her.{/n}
{n}The group is smaller than it might have been. It is listening. Aranka takes that bargain and gives them the whole opening song.{/n}
{n}Before the new piece, she explains the change in the verse. She says she had passed on a story that the person who lived through it did not recognize. She has removed the brave return she invented. She will not identify the woman who corrected her.{/n}
"I swallowed a splendid story whole. Now listen to the song with that false verse cut out."
{n}She finds you in the group. Her smile is brief and grateful, then she looks toward Sella for the breath.{/n}''', c('[Listen with the people who chose to stay.]', "part", flags=("aranka.crowd_listened",))),
    n("part", "Aranka", '''{n}Sella takes the first line. Rovan waits for her breath. The space they found in rehearsal opens between the notes, and Aranka steps into it without crowding her.{/n}''',
        c('[Sing the line you practiced.]', "sing", requires=("aranka.sings_line",)),
        c('[Let Aranka find you listening.]', "listen", requires=("aranka.listens_close",))),
    n("sing", "Aranka", '''{n}Your first note strays. Aranka slips her harmony beneath it and gives you the pitch with a bright glance. You finish the line, and a listener grins.{/n}
{n}When Sella takes over, Aranka's fingers brush your wrist once. Then she is watching the other singer again, entirely occupied by the thing the four of you are making.{/n}''', c('[Hear the ending you chose together.]', "ending")),
    n("listen", "Aranka", '''{n}Aranka catches your eye at the end of the verse. You smile, and she launches into the next phrase with renewed vigor.{/n}
{n}Rovan catches a falling beat, Sella answers his flourish, and Aranka's laugh enters the tune for half a measure before she brings it back. You hear the little accident travel through the listeners as pleasure.{/n}''', c('[Hear the ending you chose together.]', "ending")),
    n("ending", "Aranka", '''{n}The melody reaches the place where the borrowed hero used to return. Aranka leaves his place empty. The song moves on without naming him.{/n}''',
        c('[Let the unanswered door remain.]', "door", requires=("aranka.ending_door",)),
        c('[Listen to the answers from the crowd.]', "answers", requires=("aranka.ending_answers",))),
    n("door", "Aranka", '''{n}The final chord refuses to settle where the listeners expect. One man begins to clap early, stops, and looks embarrassed. Aranka gives him a small nod without filling the silence for him.{/n}
{n}The last note fades. There is a moment when you can hear the wind in the grass. Then the applause begins, uneven and quite real.{/n}
"I wanted someone to open it," {n}a woman says.{/n}
"So did I," {n}Sella replies.{/n}
{n}Nobody offers a speech. Rovan tucks the sticks under his arm. Aranka thanks the listeners and promises a quicker tune for anyone still willing to lend her their feet. The woman who wanted dancing is first to stand.{/n}
{n}As Aranka passes, her hand trails over your shoulder. "Save me a dance, my darling!"{/n}
{n}She returns to Sella just as Rovan gives the next beat.{/n}''', c('[Stay through the music and help bring the evening to its end.]', flags=("aranka.performance_kept",))),
    n("answers", "Aranka", '''{n}At first nobody answers. Then a woman says the name of a carter, so quickly that Aranka has to ask her to repeat it. Sella finds room for the name. Rovan makes the awkward rhythm sound deliberate.{/n}
{n}A man names his sister. Another says, "A mule," and the laughter threatens to swallow the next reply. Aranka repeats the mule's name with such grave musical attention that the group quiets to hear what she will do with it.{/n}
{n}The next answer is a woman whose name the speaker never learned. Sella sings, "The woman at the gate," and leaves it there. You cannot tell whether Neris is among the listeners. Aranka does not look for her.{/n}
{n}The ending grows untidy. It lasts longer than planned. When Aranka finally brings the voices together, her face is flushed with the effort and the delight of having kept them from falling apart.{/n}
"That," {n}she says to you as the applause begins,{/n} "was considerably more work than a solo."
{n}Then she laughs, takes your hand for one breath, and goes to thank the singers.{/n}''', c('[Stay through the music and help bring the evening to its end.]', flags=("aranka.performance_kept",))),
], "aranka.song_revised", delay=48)

s("the_song_afterwards", "The song afterwards", '"How did the evening leave you?"', [
    n("start", "Aranka", '''{n}You find Aranka humming to herself with her boots beside her. She has a shallow scratch on one ankle and is trying to remember where she acquired it.{/n}
"I danced," {n}she tells you.{/n} "This is a much better explanation than whatever heroic story you were preparing. Sit down before I make you hear the whole account."
{n}She pulls you close enough to kiss, then studies your face.{/n}
"I have been wanting to do that since I woke. I tried being industrious first. It was disappointing."
"Sella has been asked to teach her version to two people who had only heard mine. Rovan has acquired a pupil who wants to learn the trick with the sticks. He is pretending the pupil must earn it through years of devotion."
{n}She looks pleased, then rubs her ankle once more.{/n}
"Neris said the correction was clear. She did not applaud. Fair enough, though my vanity suffered dreadfully."
{n}The little smile that follows is more tired than the first.{/n}''',
        c('"And what did you think of my contribution?"', "aftermath"),
        c('"Save me another afternoon. Today I have to go."', abort=True)),
    n("aftermath", "Aranka", '''{n}Aranka stretches her legs out and leans back on her hands.{/n}
"Oh, now you want your applause!"
"I came for the singer. I should probably hear her."''',
        c('[Hear what your short introduction made possible.]', "welcomed", requires=("aranka.crowd_welcomed",)),
        c('[Hear what the misplaced speech cost.]', "ceremony", requires=("aranka.crowd_ceremony",)),
        c('[Hear what happened after you moved aside.]', "listeners", requires=("aranka.crowd_listened",))),
    n("welcomed", "Aranka", '''"You gave us the room, and then you stopped talking. I know how tempting that can be to forget when people are pleased to hear you."
"I noticed. It was distracting in an extremely useful way."
{n}She reaches across your lap for her boot, thinks better of it, and leaves her hand there.{/n}
"The man who wanted the moon song stayed for the last dance. He asked Sella whether she knew something faster. He used her name. That may be my favorite result."
"I enjoyed the applause. I am not so virtuous that I forgot it. But I have heard applause that meant people were glad they had seen someone famous. This felt like they had heard something they might carry away."
{n}She presses your knee lightly.{/n}
"I won't employ you as my permanent announcer. You would become unbearable. But I liked having you there."''', c('"What do you want to do next?"', "plans")),
    n("ceremony", "Aranka", '''"I was angry with you for about half a song. Then I was busy. This morning I discovered I was still a little angry, which was inconvenient because I also wanted to kiss you."
"I cut Sella's solo after your speech. She had been looking forward to it. I promised I would come and hear it another day, without a grand occasion attached."
{n}Aranka turns her hand palm up between you.{/n}
"Next time, sing that speech to me first. I shall cut it down to four lines, and Sella will have her solo back."
"Now kiss me before I put the speech to music!"
{n}The kiss begins with laughter and slows. When she draws back she is still a little cross, and enjoying it.{/n}''', c('"What would you like to make after this?"', "plans")),
    n("listeners", "Aranka", '''"Fewer people stayed than I hoped. I was disappointed. Then Sella started, and I stopped counting them."
"I was. Rovan said it felt like playing for people rather than playing at a wall made of noise. He has become poetic. I fear our influence."
{n}She touches your sleeve, smoothing a crease that returns as soon as she lets it go.{/n}
"I wanted the whole island listening! Then Sella sang, and the little crowd sang back. Oh, we shall have to do that again."
"Some evenings. Other evenings I shall want to be adored by hundreds. I hope you are prepared for this shocking inconsistency."
{n}She tilts her face toward yours.{/n}
"Today one attentive person will do nicely."''', c('"Tell your attentive person what comes next."', "plans")),
    n("plans", "Aranka", '''"There is a traveling singer I used to know who could hear a tune once and make you think he had written it. I envied him horribly. I spent a whole summer trying to learn that trick."
"Enough to become annoying. Not enough to stop working. I want that again. A place where I am the person listening at the back because I don't know the song."
{n}She turns toward you, serious beneath the warmth.{/n}
"When the war allows it, I am taking the road again! I love these people, but there are songs beyond Mendev that I have never heard."
"I shall miss you outrageously. Then you will find me in some strange inn, and I shall demand every story you have saved for me."
{n}She traces a line along your palm, then closes your fingers over her own.{/n}
"And I want more evenings before that happens. I am not saying goodbye while sitting on your hand."''',
        c('"After the war, I shall walk a stretch of that road with you."', "road"),
        c('"My campaign may keep me here. Bring your tales back to me."', "meeting")),
    n("road", "Aranka", '''"A stretch! With you beside me, I might even forgive a road full of hills."
"Hills are worse when I am carrying everything I swore I couldn't live without. You may have to watch me part with a third pair of shoes. It will be very moving."
{n}She rests her cheek against your shoulder.{/n}
"We can choose the road when the war is done. Somewhere warm! Somewhere with a tune I have never heard and an innkeeper who does not know your title."
"Until then I would like one evening with you that does not involve an audience. You can tell me a completely unimportant thing, and I shall pay it far too much attention."
{n}She lifts her head and kisses the place just below your ear.{/n}
"I have been saving some attention."''', c('[Promise to return for an evening alone.]', flags=("aranka.future_road", "aranka.after_song_kept"))),
    n("meeting", "Aranka", '''{n}She turns your hand over and kisses your palm.{/n}
"Then you must endure my letters! I shall describe every splendid place until you become unbearably jealous."
"And I want you! I shall send tales from the road, and you must tell me which ones sound too magnificent to be true."
{n}She smiles, then nudges your shoulder with hers.{/n}
"But today you are right here, and I am tired of talking about roads."
"I am versatile. I can begin something else."
{n}Her kiss is slow enough to make the afternoon feel briefly larger. When she steps back, she keeps your hand.{/n}
"Come for an evening when nobody needs us to sing. I want to find out how long I can keep your attention without saying anything clever."''', c('[Promise another evening together.]', flags=("aranka.future_meetings", "aranka.after_song_kept"))),
], "aranka.performance_kept", delay=48)

s("no_encore_needed", "No encore needed", '"You promised an evening without a performance."', [
    n("start", "Aranka", '''{n}Aranka has a shawl over one shoulder and a pair of shoes in her hand. She looks you over with frank pleasure.{/n}
"You look suspiciously prepared to be useful. Put that expression away. We are going for a walk."
{n}She leads you along a quiet part of the island path, keeping well back from the edge. The light is changing across the grass. For a while she talks about nothing more consequential than a bird that stole something brightly colored and then seemed unable to decide what to do with it.{/n}
"I admired its ambition. Its planning needed work."
"Its mistakes were remarkably like mine."
{n}At a sheltered hollow she puts down the shoes and spreads the shawl beside her. When you sit, she settles close enough that your shoulders touch.{/n}
"There. I have brought you somewhere without a chorus. If you hear one, it is entirely your fault."''',
        c('[Stay with her as the light changes.]', "remember"),
        c('"The war has stolen this evening. Save your walk for my next visit."', abort=True)),
    n("remember", "Aranka", '''{n}She takes your hand and works her fingers between yours, looking out over the grass.{/n}
"I keep thinking about the rehearsal. The part where everyone stopped trying to make the song happen quickly."
"I was dreadfully impatient. I could hear the finished thing in my head. I wanted the others to catch up to it. Then they did something I hadn't imagined, and I liked that better."
{n}She turns toward you.{/n}
"Oh, I have imagined tonight already! You were dazzled by me in every version. A very promising beginning."
"That look you are giving me now? That was in it too."
{n}Her free hand comes to rest against your chest. She waits, enjoying the nearness rather than pretending the touch was accidental.{/n}''',
        c('"And Reverie? We still owe her a visit."', "reverie", requires=("aranka.ran_reverie_partner", "aranka.ran_keep_final"), forbids=("aranka.ran_release_final",)),
        c('"I have been admiring that mouth all evening."', "desire")),
    n("reverie", "Aranka", '''{n}Aranka begins a phrase, then stops with a smile you recognize from the dream.{/n}
"That belongs to Reverie's cocoon. I almost put it in the rehearsal song! She would have wanted the last word. And several encores."
{n}She folds that sheet beneath the others.{/n}
"I still mean to visit her. The compass and those promises are not settled by a kiss here. Tonight I want an evening with you. When we see her again, I shall tell her so myself."''', c('[Return to the woman beside you.]', "desire")),
    n("desire", "Aranka", '''{n}Her fingers tighten in your collar.{/n}
{n}She leans close enough that the next words warm your cheek.{/n}
"I want your hands on me. I want to kiss you until the stars come out and forget every verse I ever wrote!"
{n}You touch her waist. Her breath changes. She tips her face toward yours, then stops just short of the kiss, eyes bright.{/n}
"I rather like suspense when I know who I am waiting for. Don't make me wait long."
{n}The shawl has slipped from beneath one elbow. She retrieves it, laughing at the small interruption, and rests her forehead against yours.{/n}
"There. All the romance in the world, and I still sat on a root."''',
        c('"Stay with me tonight. Somewhere with a roof and a door."', "night_initiation"),
        c('"Kiss me here. I have to leave tonight, but I have time now."', "kiss"),
        c('"I want the quiet evening and your hand in mine. Let us leave the rest for another time."', "quiet")),
    n("night", "Aranka", '''{n}She lies against you, tracing a wandering line along your arm. She hums three notes and stops.{/n}
"That was entirely private."
{n}In the morning she finds one shoe beneath the bedding and accuses it of following the two of you for improper reasons. You leave after a slow goodbye, with the song from rehearsal returning to you in fragments and the warmth of her mouth easier to remember than any finished verse.{/n}''', c('[Stay the night with her.]', flags=("aranka.extension_night", "aranka.extension_kept"))),
    n("kiss", "Aranka", '''{n}She answers with a kiss that makes good use of the time. Her hand settles at your neck; the other draws you nearer until the shawl shifts between you. When she pulls back, she looks pleased enough to make you laugh.{/n}
"What?"
"I am considering a repeat performance."
"An unfortunate choice of words."
{n}She kisses you again, slowly. You stay close as the light fades. She tells you about an innkeeper who charged extra for a painted window, and interrupts your answering story with a delighted laugh.{/n}
{n}When it is time to leave, she folds the shawl and puts on her shoes. She walks back with you until your paths divide.{/n}
"Bring me the news. I'll do the rhyming," {n}she says.{/n} "I want to hear what you have been doing, even if none of it rhymes."
{n}Her goodbye kiss almost begins another conversation. She lets you go with a laugh and a last squeeze of your hand.{/n}''', c('[Leave with another visit wanted.]', flags=("aranka.extension_kiss", "aranka.extension_kept"))),
    n("quiet", "Aranka", '''{n}She kisses your knuckles and settles against your shoulder. The shawl covers your joined hands.{/n}
"Then I shall have to be interesting in other ways. Fortunately I have an opinion about every bird on this island."
{n}She imitates the thief you saw on the path. Something in the grass answers; she laughs so hard she cannot finish. The distant camp bugle draws her eyes toward the tents.{/n}
"They want you back. Stay until the light goes. I haven't finished insulting that bird."
{n}When the air cools, she walks back with you, still holding your hand. At the fork she pulls you close for a last kiss.{/n}''', c('[Stay until the air cools, then walk back with her.]', flags=("aranka.extension_quiet", "aranka.extension_kept"))),
], "aranka.after_song_kept", delay=48)

# The first six visits resolve one island project, not the whole relationship.
# These later conversations let the established lovers disagree about fame,
# authorship and the Commander's power without turning Aranka into an admirer.
s("the_story_that_follows", "The story that follows", '\"I heard a new version of the song.\"', [
    n("start", "Aranka", '''{n}Aranka sits on the island wall with a cup in her hands. Below, two travelers argue over a new verse: the Commander bargained with the moon, and it changed the song's ending.{/n}
"The moon! I spent all that time correcting the refrain, and they have given it a speaking part."
{n}She puts the cup down hard enough to spill it.{/n}
"I like a good boast. I even like your boasts. But Sella brought that song out of Kenabres. I will not have her drowned out again."
{n}She points down the path. The travelers are about to pass out of earshot.{/n}''',
        c('"Let us sing them a moon so ridiculous that even those two cannot mistake it for a history."', "trickster", requires=("trickster",)),
        c('"We can tell the travelers the song is yours and leave the story there."', "correct"),
        c('"Let the rumor go. Sing them something better."', "let_go")),
    n("trickster", "Aranka", '''"Another lie? A moon so vain it won't rise without applause? Oh, I could make it unbearable!"
{n}She starts to laugh, then glances after the travelers.{/n}
"But they will carry the funniest verse down the road. Sella gets forgotten, and I spend another week chasing my own song."
{n}She folds her arms.{/n}
"Mock your own moon. I sing the real refrain afterwards, and I get the last word."''',
        c('"Then you take the last verse. I will sing the ridiculous moon."', "game"),
        c('"Keep your song. I can find another joke."', "correct", flags=("aranka.story_restraint",))),
    n("game", "Aranka", '''"Oh, that moon will be unbearable! Sing your nonsense, and then I shall give them the real refrain."
{n}She reaches for your hand again, and squeezes it hard enough to make the point.{/n}
"I have a magnificent moon to sing and a menace with an excellent speaking voice to kiss."
"First I am going to make that moon sound insufferable."''',
        c('[Hail the travelers.]', "shared")),
    n("correct", "Aranka", '''"Oh, what a dull ending for the moon! Still, my song will sound much better without it."
{n}She jumps down from the wall and brushes her knee against yours.{/n}
"You have left me with an excellent song and nothing to quarrel about. Most inconsiderate! Come closer."
"I have other plans for my mouth."''',
        c('[Stay with Aranka as the travelers walk on.]', "quietly", flags=("aranka.story_restraint",))),
    n("let_go", "Aranka", '''"A new song is not a correction," {n}Aranka says.{/n} "But it might be an answer. I don't want to spend every evening chasing the first people who heard a bad verse."
{n}She leans her shoulder against yours. Her smile returns, small and a little tired.{/n}
"Let it travel. I will write the next one for the people who are willing to listen. You can sit beside me and try not to become the chorus."
"Sing something better than your best, then! But let me finish my verse first."''',
        c('[Stay beside her and leave the travelers undisturbed.]', "quietly", flags=("aranka.story_left_alone",))),
    n("shared", "Aranka", '''{n}You hail the travelers and announce a new song about a moon so vain it refuses to rise without applause. Aranka is already on her feet.{/n}
"The singer gets the last word," {n}she tells them.{/n} "Sit down."
{n}She gives them the version with the moon demanding an encore, and she makes the moon sound insufferable. The younger traveler laughs hard enough to nearly drop her pack.{/n}
"That was fun," {n}the older one says.{/n} "What actually happened?"
{n}Aranka answers before you can. She sings the refrain as she wrote it, including the place where she chose to stop rather than give the crowd a heroic finish. She lets the final note settle without adding a word.{/n}
"And that is the refrain I wrote! Carry it down the road. I shall be furious if you improve it before I do."''',
        c('[Let Aranka keep the last word, then walk back together.]', "desire", flags=("aranka.story_game", "aranka.story_conversation_done"))),
    n("quietly", "Aranka", '''{n}The travelers continue down the path. Aranka watches until the bend hides them, then turns toward you.{/n}
"Oh, I could have chased them down the path and sung until their ears rang! I shall save the verse for a better audience."
{n}She catches your face between her hands and kisses you, smiling against your mouth.{/n}
"You can still be a menace. Just don't sing over the quiet ones."''',
        c('[Tell her what you want from the woman who keeps challenging you.]', "desire", flags=("aranka.story_conversation_done",))),
    n("desire", "Aranka", '''"Keep surprising me! And let me finish my verse before you steal the moon."
{n}She catches your collar between two fingers and draws you closer. Her thumb brushes the skin at your throat.{/n}
"Now. Was that another road you wanted, or have I talked long enough for one evening?"''',
        c('"I meant I want you. Here, with no audience."', "private"),
        c('"I meant I want you beside me when the next impossible thing happens."', "road"),
        c('"I meant both."', "both")),
    n("private", "Aranka", '''"Good," {n}she says.{/n} "I have been listened to all evening. I would like to be touched now."
{n}Her hand settles at the back of your neck and she kisses you as if she had rehearsed it, which, knowing her, she has. Then she draws you off the path into the sheltered hollow behind the wall, unpins her cloak and lets it fall on the grass.{/n}
{n}She guides your mouth to the hollow of her throat so you can feel the song she is not singing, and her fingers are already busy with your buckles.{/n}
"Not one anyone else gets to hear," {n}she says against your mouth, and drags your shirt up over your head.{/n}''',
        c('[Draw her close as she strips off your shirt.]', "hollow_morning"),
        c('[Catch her hands, laughing. "Another night."]', flags=("aranka.story_conversation_done",))),
    n("hollow_morning", "Aranka", '''{n}You wake in the hollow with dew on the cloak and her humming against your shoulder: the moon verse, slowed down and made thoroughly indecent. She has written two lines of it on the back of your hand in charcoal.{/n}
"Don't wash that," {n}she says.{/n} "I haven't copied it out yet."''',
        c('[Keep the verse on your hand.]', flags=("aranka.story_conversation_done",))),
    n("road", "Aranka", '''"That sounds lovely," {n}she says.{/n} "It also sounds like the sort of plan that eats every afternoon we have left."
"You can make room for me to sing on the way. Loudly. Badly, at dawn. Those are my terms."
{n}She kisses you, warm and unhurried, then rests her forehead against yours.{/n}
"Come and find me when the impossible thing is over. I'll have written a verse about it, and you will hate how flattering it is."''',
        c('[Promise to find her when your work is done.]', flags=("aranka.story_conversation_done",))),
    n("both", "Aranka", '''"Both! Nights when I can distract you from the song, and roads full of tunes we have never heard."
{n}She kisses you, one hand fisted in your collar, and walks backwards towards the wall without letting go.{/n}
"Tonight, the first. The road can wait until I've slept."''',
        c('[Go with her to the sheltered hollow.]', "private"),
        c('[Kiss her, and promise her the road some other night.]', flags=("aranka.story_conversation_done",))),
], "aranka.extension_kept", delay=48)

s("the_next_verse", "The next verse", '\"I wanted to ask how the story traveled.\"', [
    n("start", "Aranka", '''{n}The travelers have gone. Aranka waits by the island wall, a folded sheet of music tucked into her belt. She waves you over before you can call her name.{/n}
"Look! I have written a new verse. This one has no moon in it, so you must admire the singer instead."
{n}She gives you her hand, and a kiss, and then the sheet of music, which is plainly the real business of the afternoon.{/n}''',
        c('[Ask what happened after the moon verse was introduced as fiction.]', "game_checkin", requires=("aranka.story_game",)),
        c('[Ask what she wrote after the travelers left.]', "restraint_checkin", requires=("aranka.story_restraint",)),
        c('[Ask to hear her new verse.]', "left_alone_checkin", requires=("aranka.story_left_alone",))),
    n("game_checkin", "Aranka", '''"They laughed at the moon and asked me what really happened," {n}she says.{/n} "One of them remembered the last line, the real one. I could have kissed her. I very nearly did."
{n}She taps the folded sheet at her belt.{/n}
"They remembered the joke, and then my verse! I shall have to write a finer one to outdo it."''',
        c('[Ask about the next song.]', "boundary")),
    n("restraint_checkin", "Aranka", '''"It was murder not to follow them," {n}she says.{/n} "I had a better explanation ready for every bend in the road. So I wrote down a line instead, and it was a better line than the explanation."
{n}She pulls the folded sheet free, then slides it back under her belt.{/n}
"Now this one must carry my name. I will not have another verse marched off under your banner."''',
        c('[Ask what she wants.]', "boundary")),
    n("left_alone_checkin", "Aranka", '''"I wrote a verse about that open door. Nobody has heard it yet. The ending is dreadful, and I refuse to sing it until I have a better one."
{n}She looks at you with the same bright directness she brings to a new melody.{/n}
"You will have to wait for the last line. Unless you can sing me a better one?"''',
        c('[Ask what she wants.]', "boundary")),
    n("boundary", "Aranka", '''"Every soldier stands when you walk past! How am I to sing over all that clattering armor? I want them hearing my verses, not waiting for your speech."
{n}She taps the folded sheet at her belt.{/n}
"My name at the top! Sella and Rovan beside their parts. If a herald puts your name on this song, I shall sing the correction outside his window until he begs for mercy."
{n}She thrusts the folded sheet into your hands and points to the empty heading.{/n}''',
        c('"I will write your name above it. Then I shall hear your new verse."', "listen"),
        c('"Give me the sheet. I can spare an afternoon for your song."', "life"),
        c('"Then take the song on the road. It will find an audience."', "empty")),
    n("listen", "Aranka", '''"Good! Start with the heading. Write it large enough for your heralds to read."
{n}She unfolds the sheet and shows you the title line. Her name is written above the song; beneath it are blank spaces for the voices that helped shape it.{/n}''',
        c('[Write the heading and make Sella and Rovan a copy each.]', "specific"),
        c('[Set the sheet down. The work must wait until your next visit.]', "defer")),
    n("life", "Aranka", '''"An afternoon? Splendid! Here is the heading. Try not to give me a title longer than the song."
{n}She unfolds the sheet and shows you the title line. Her name is written above the song; beneath it are blank spaces for the voices that helped shape it.{/n}''',
        c('[Write the heading and make Sella and Rovan a copy each.]', "specific"),
        c('[Set the sheet down. The work must wait until your next visit.]', "defer")),
    n("empty", "Aranka", '''"Of course I shall travel! But I asked for your help with this copy, not a proclamation that I may leave."
{n}She folds the sheet away and steps back.{/n}
"Then I shall finish it myself. Come back in three days, when you can sit still long enough to write more than your signature!"''',
        c('[Leave her to the song and promise to return.]', flags=("aranka.after_story_deferred",))),
    n("defer", "Aranka", '''"Fair," {n}she says.{/n} "Better a late verse than a bad one."
{n}She folds the page and flicks it against your sleeve before putting it away.{/n}
"Give me three days. I shall have a verse worth copying by then, and you had better bring a steady hand."''',
        c('[Promise to return after three days.]', flags=("aranka.after_story_deferred",))),
    n("specific", "Aranka", '''"Three copies! One for Sella, one for Rovan, one for my satchel. Let them carry the song as far as they like, so long as they remember who wrote it."
"Ten days on the road! I know three Desnan camps along the traders' route, and their singers owe me a verse each. I shall catch you on the way if your campaign lets you escape."
{n}She smiles like a woman who has just been handed a well-tuned lute.{/n}
"Help me finish the copies this afternoon. In two days I set out for the first camp!"''',
        c('[Copy the parts with her, writing Sella and Rovan above their verses.]', flags=("aranka.relationship_plan",))),
], "aranka.story_conversation_done", delay=48)

s("the_song_and_the_road", "The song and the road", '\"You said you chose the first road.\"', [
    n("start", "Aranka", '''{n}When you return, Aranka has three finished copies beside her on the wall. Sella and Rovan are named above their parts. The original is folded in her satchel.{/n}
"The first copy goes to Sella. The second to Rovan. The third stays with me until I have heard what the camps want to add."
"Three camps along the traders' route, and ten days of songs! I know their singers. They will have a new verse for me, or I shall make them dance until they invent one."
{n}She pushes a blank margin and the pen across the wall at you.{/n}''',
        c('[Write the singers\' names in the margins.]', "copies", requires=("aranka.relationship_plan",))),
    n("copies", "Aranka", '''{n}She checks the names, makes a small, savage correction to Rovan's rhythm note, then seals each sheet in its own fold.{/n}
"Today I leave for the first camp. Expect outrageous boasts! Ten days, three camps, and a satchel that will come back heavier."
{n}She shoulders the satchel, then puts it down again to catch your collar.{/n}
"I nearly forgot something."''',
        c('[Kiss her goodbye and wish her a splendid audience.]')),
], "aranka.relationship_plan", delay=48)

s("the_deferred_answer", "The deferred answer", '\"I came back to the question.\"', [
    n("start", "Aranka", '''{n}When you return, Aranka has her travel bag beside her and a sheet of music spread across the wall. She lifts the pen in greeting.{/n}
"At last! I have a verse and a pen. What have you brought me?"
{n}She taps the blank heading with the pen.{/n}''',
        c('"Give me the pen. Your name goes above the song, and I shall carry your verses without turning them into a marching tune."', "plan"),
        c('"I have brought no answer. My head is still full of the campaign."', "not_yet")),
    n("plan", "Aranka", '''"Much better! Start with my name, and make the letters magnificent."
{n}She takes your hand, and then the rest of you, and kisses you hard enough to knock the bag over.{/n}
"We shall finish the copies, and then I have three camps to visit along the traders' route. Ten days! I know their singers, and I mean to come back with a satchel full of verses."
"Now I get to miss you, which is excellent for the writing."''',
        c('[Write the credits and help make the copies before kissing her goodbye.]', flags=("aranka.relationship_plan",))),
    n("not_yet", "Aranka", '''"Oh, that campaign! It swallows every tune I try to teach you. I shall finish this one before it swallows mine."
{n}She kisses your cheek, quick and fond and a little cross.{/n}
"Let me work. When I have a verse worth hearing, I shall sing it loudly enough to drag you out of your campaign maps."''',
        c('[Let her go.]')),
], "aranka.after_story_deferred", delay=72)

def _finish_branches(id, branches, shared):
    """Give the two musical trials terminal outcomes, including interrupted replay.

    Each trial shares its closing prose but records its result only at the end.
    These duplicate graph pages contribute no extra distinct prose volume.
    """
    item = next(item for item in SCENES if item["Id"] == "aranka." + id)
    original = {page["Id"]: page for page in item["Nodes"]}
    item["Nodes"] = [page for page in item["Nodes"] if page["Id"] not in shared]
    for branch in branches:
        entry = original[branch]["Choices"][0]
        outcome = entry["Set"]
        entry["Set"] = []
        entry["Next"] += "_" + branch
        for name in shared:
            page = deepcopy(original[name])
            page["Id"] += "_" + branch
            for choice in page["Choices"]:
                if choice["Next"] is not None:
                    choice["Next"] += "_" + branch
                elif not choice["Abort"]:
                    choice["Set"] = outcome + choice["Set"]
            item["Nodes"].append(page)


_finish_branches("where_the_breath_goes", ("heard", "missed", "separate"), ("rovan", "lesson"))
_finish_branches("an_evening_uncommanded", ("welcomed", "ceremony", "step_aside"),
                 ("part", "sing", "listen", "ending", "door", "answers"))


# Round-2 slots are state-free; all original terminal receipts stay in place.
next(s for s in SCENES if s["Id"] == "aranka.no_encore_needed")["Nodes"].extend([
    n("night_initiation", "Aranka", '''"A brilliant proposal. I knew there was a reason to bring you."
{n}She kisses you, then gathers her shoes and gets to her feet. You have not let go of her hand, and she bends for another kiss. The second kiss lasts long enough for the shoes to fall from under her arm.{/n}
"Those have become inconvenient," {n}she says.{/n}
"I have been reminded of another inconvenience."
{n}You retrieve the shoes while she folds the shawl. She walks beside you rather than pulling you along, letting the anticipation survive the distance. Once you reach the private shelter she has arranged for the evening, she takes you through the curtain by your belt.{/n}
{n}Inside she kicks the shoes into a corner and laughs into your mouth when the shawl tangles round both of you. She does not stop to untangle it.{/n}
"Hold still. I am composing." {n}Her fingers are at your collar, her breath is warm on your throat, and she hums the first phrase of the rehearsal song against your skin and loses the tune halfway through.{/n}''', c("Continue", "aranka.no_encore_needed.explicit.1"), portrait="Aranka"),
    # User-supplied established-lovers insertion, followed by the old night aftermath.
    n("aranka.no_encore_needed.explicit.1", "Narrator", "{n}The song does not get finished. The laces of her dress give way one after another under your fingers, her skin is hot against your hands, and her breath turns to a laugh and then to something that is not a laugh at all. Time loses its count between one kiss and the next, and the shawl is never untangled.{/n}", c("Continue", "night"), portrait="Aranka"),
])

_hollow = next(s for s in SCENES if s["Id"] == "aranka.the_story_that_follows")
next(node for node in _hollow["Nodes"] if node["Id"] == "private")["Choices"][0]["Next"] = "aranka.the_story_that_follows.explicit.1"
# User-supplied hollow insertion; the existing deferral never traverses this slot.
_hollow["Nodes"].append(n("aranka.the_story_that_follows.explicit.1", "Narrator",
    "{n}You go down together onto the wool. Her skin is warm under your hands, her laugh turns to a breath against your throat, and the buckles and laces give up one after another. Beyond the cloak the grass is wet with dew, and neither of you notices until much later.{/n}",
    c("Continue", "hollow_morning"), portrait="Aranka"))


# Round 3: the real living Thall answers at his native island hub.
# No spawned actor or relationship stance for an unrequited interest.
SCENES.append(scene("aranka.thall.answer", "The low part", "Aranka", 5,
    '\"Thall, Aranka and I are together. I wanted you to hear it from us.\"', [
    n("start", "Aranka", '''"Wallflower, stop hiding behind that scroll."
{n}She takes your hand.{/n} "I still want to hear you sing. But I want you to hear this first. I love you as a friend. I am going to keep coming back to this dreadful distraction."''',
      c("Continue", "answer"), speaker_unit=ACTOR),
    n("answer", "Thall", '''"Oh. I... yes. I had hoped, but... Thank you for telling me."
{n}Thall lowers the scroll.{/n} "Please don't ask me to sing about it. I would rather listen."
"I have found the hymn you wanted. We could try it. Without an audience. Another day."
{n}Aranka accepts the sheet without pulling him closer. He unrolls the scroll again, leaving the hymn between them.{/n}''',
      c("Continue", flags=("aranka.thall.parting_spoken",)), speaker_unit="8fb65bd79574771429526eaef26762a9"),
], requires=("aranka.ran_romance", "aranka.ran_quest_complete", "aranka.present_now"),
    forbids=(*BLOCKED, "aranka.thall.dead", "aranka.thall.parting_spoken"), last=5, optional=True,
    Relationship="aranka", Chapters=[5], Areas=[AREA], AnswerLists=[ANSWERS],
    ContactUnit="8fb65bd79574771429526eaef26762a9", AdditionalContactUnits=[ACTOR]))

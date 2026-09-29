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
"Hello. You are not the problem. I thought I should get that settled before you offered to defeat anything."
"The singing?"
"My singing. I taught someone a tune, and now everyone knows it except me. They have improved it. I keep hearing about battles I never put in it. In one version you throw a demon through the moon."
"Only one?"
"It was a short verse."
{n}She slips her hand into the crook of your elbow and turns toward a quieter patch of grass. Her pace is easy, but she keeps testing a little run of notes under her breath.{/n}''',
        c('"Tell me what happened to your song."', "history"),
        c('"I want to hear this properly. May I come back when I can stay?"', abort=True)),
    n("history", "Aranka", '''{n}She tips her head back to look at the sky, then at you.{/n}
"I wanted a little time with you in the same weather. There are things I can't tell from a grand adventure. Whether you've eaten. Whether that crease between your eyes disappears when nobody asks you a question."
"You're asking several."
"I have a poor technique. Stay anyway."''',
        c('"How has life been since choosing to be a Dream Warden?"', "keeper", requires=("aranka.ran_keep_final",), forbids=("aranka.ran_release_final",)),
        c('"How does it feel to have given up the compass?"', "traveler", requires=("aranka.ran_release_final",))),
    n("keeper", "Aranka", '''"Larger. Occasionally larger than I know what to do with. I can be halfway through a perfectly ordinary afternoon and remember a color I don't have a name for. Then somebody wants to know whose cup I've taken."
{n}She lifts the cup in her free hand and examines its base.{/n}
"This one is mine. I checked."
"Do you regret becoming a Dream Warden?"
"No. I regret thinking that choosing it would make all my other choices arrange themselves neatly. Reverie told me about a place she wants to show me. I want to see it. I also want to finish something here before I go wandering again."
{n}She gives your arm a small squeeze.{/n}
"And I want afternoons when being together doesn't require either of us to save anyone. I am very fond of your face without a crisis behind it."
"I brought the same face."
"Good. I have been practicing what to do with it."''',
        c('"Have you been thinking about your first flight in the dream?"', "flight", requires=("aranka.ran_wing_dream",)),
        c('"Start with the song."', "song")),
    n("flight", "Aranka", '''"Far too much. Every time I try to describe it, I sound as if I am inventing a more impressive version. The wings, the light, the moment when the ground became somewhere I could choose to leave."
{n}She spreads her hands, searching for the size of the feeling.{/n}
"Then I woke and needed my boots. It was rather difficult to be patient with them."
"You did wonder how long the wings would take outside the dream."
"I did. I am not going to solve that by leaping off the island. Please look less alarmed. I have an excellent imagination and occasionally use it before doing something foolish."
{n}She looks up, smiling to herself.{/n}
"I would like to sing about it eventually. Not yet. I keep reaching for enormous words and losing the moment when I was simply delighted. I want to get that part right."
{n}Her gaze returns to you.{/n}
"Today I shall practice being delighted nearer the ground."''', c('"Let me hear what you are working on now."', "song")),
    n("traveler", "Aranka", '''"I still reach for it sometimes. That's embarrassing. You would think handing something over in person would persuade my hand that it was gone."
{n}She spreads her fingers against the sunlight, then curls them around yours.{/n}
"I chose to stop. I haven't secretly changed my mind because a few ordinary mornings were difficult. But I miss things I didn't expect to miss. Reverie telling a story so enthusiastically that I barely recognized being in it. The possibility that I could turn a corner and find somewhere impossible."
"You can miss it."
"I know. I am trying to do that without composing a song in which every road I didn't take was perfect. Those songs are extremely popular and mostly nonsense."
{n}She swings your joined hands once.{/n}
"I am here. There is work I want to do here. When we can travel again, I intend to get lost somewhere that has never heard your title. You can come if you promise to be interesting when nobody bows."
"A difficult demand."
"I believe in you."''', c('"Tell me what you want to make here."', "song")),
    n("song", "Aranka", '''{n}She sings four quiet lines. The melody seems about to climb into a triumphant finish, then steps down instead.{/n}
"The swallow turns above the road,
The traveler turns below.
Ask at the door who made it home;
Ask at the door who knows."
{n}For a moment you hear the voices from the path fitting their louder ending into the same place.{/n}
"A woman named Sella taught me the first bit. She used to sing while hanging washing between the wagons. A few of the others knew different verses. I thought we could make an evening out of it. People singing what they've carried here. No grand story about how delighted everyone is to be at war."
"There is room beside 'Starward Gaze' for a song that doesn't know where it is going yet. I'd like to hear what happens when we give it some company."
"And someone changed the ending."
"Several someones. I'm not furious that they changed it. That is how songs travel. But now a man has asked me to perform the famous version, with you standing beside me. Apparently the song needs a real Commander to keep the moon in place."
{n}She plucks a stalk of grass and knots it loosely around her finger.{/n}
"I could sing it beautifully. They would cheer. Sella would never get to finish the verse she brought. I would rather try something less certain."''', c('"What are you considering?"', "venues")),
    n("venues", "Aranka", '''"One open circle. Everyone can come, the singers can hear one another, and we might persuade the loudest people that listening is part of an evening. Or we take the songs around in little groups. A handful of listeners at a time. Fewer people, but nobody has to compete with a crowd to be heard."
"Which do you want?"
"Both, obviously. I also want another pair of lungs and a morning in which nobody recognizes me. I can manage one of those things at a time."
{n}She turns the knotted stalk around her finger.{/n}
"Will you help? I don't need you to order attendance. I need someone who will tell me when the tune stops making sense, and possibly carry a tune very badly so the others become less afraid."
"You make an attractive offer."
"I haven't reached the attractive part. Afterwards I shall monopolize you for an entirely unreasonable length of time."
{n}The grass ring comes apart as she shows it to you. She laughs and drops it into the grass.{/n}
"There. Already too ambitious."''',
        c('"Try the open circle. I will help you earn their attention."', flags=("aranka.extension_started", "aranka.open_circle", "aranka.rehearsal_agreed")),
        c('"Take the songs around in small groups. Let the listeners come close."', flags=("aranka.extension_started", "aranka.rounds", "aranka.rehearsal_agreed"))),
])

s("where_the_breath_goes", "Where the breath goes", '"Is this a good time to listen to the rehearsal?"', [
    n("start", "Aranka", '''{n}A boot keeps time against the grass. The woman wearing it has a low, warm voice and a habit of closing one eye at a difficult note. Beside her, a bearded man taps two smooth sticks together. Neither pays much attention to your arrival until Aranka makes room for you.{/n}
"Sella, Rovan, this is the person I warned you about."
"You said a brave volunteer," Sella replies.
"I was giving myself room to be wrong."
{n}Rovan salutes you with a stick. His other hand remains folded close to his chest.{/n}
"I used to sing the upper part," he says. "Now I sound like a hinge. She's trying to persuade me that percussion is an honorable profession."
"A hinge can be very expressive," Aranka says. "But I don't want to hear yours hurt itself. Let's try the turn again."
{n}Sella begins. Aranka joins a third above her. The tune goes well until the line about the door, when Sella arrives early and Rovan strikes the sticks after both singers have stopped. All three look in different directions.{/n}''',
        c('[Listen for the point where their timing separates. Perception DC 26.]', check=dict(Skill="SkillPerception", DC=26, Success="heard", Failure="missed", CommanderOnly=True)),
        c('"Could each of you show me your part on its own?"', "separate"),
        c('"I am distracted. You deserve a better listener. I will return."', abort=True)),
    n("heard", "Aranka", '''{n}Rovan lifts the sticks when Sella draws breath. Aranka has already begun the next phrase by then. Sella follows her instead of taking the breath she prepared, and the last words hurry out in a cluster.{/n}
"Aranka. You're giving her less time than she takes when she sings alone."
{n}Aranka looks surprised, then sings the two lines under her breath. She catches herself at the same place.{/n}
"Oh. I have been filling the gap because I know what comes next."
"I need the gap," Sella says. "It isn't empty on my side."
{n}They try again. Aranka lets the note end before she breathes. Rovan watches Sella's shoulder and brings the sticks together with her first word. The phrase lands with an ease none of them manages to conceal.{/n}
"There you are," Aranka says, looking at Sella rather than at you. "Do it once more before I become too pleased with myself."
{n}When the next attempt holds, her knee knocks lightly against yours.{/n}
"You can stay. Apparently you have uses besides being kissed."''', c('[Listen to what Rovan needs from the arrangement.]', "rovan", flags=("aranka.timing_heard",))),
    n("missed", "Aranka", '''{n}You follow the beat with your heel and suggest that Rovan come in sooner. He tries. This time the sticks interrupt Sella's first word. She stops, begins again, then shakes her head.{/n}
"I can't find it now."
{n}Aranka holds up a hand. Rovan lowers the sticks. The little silence feels much larger than the mistake.{/n}
"That was mine," you say.
"Yes," Aranka answers. "And I agreed with you before I tried singing it. Let us both endure being wrong for a moment."
{n}Sella rubs her throat. She has been forcing the phrase to fit for longer than you realized.{/n}
"I'll need to stop for today. I don't want to lose my voice proving I can follow an instruction."
{n}Aranka gives her the last water in the flask, then asks her to hum only the beginning. Listening without joining, she finally hears where Sella takes her breath.{/n}
"Tomorrow we begin there. No upper part until yours stands on its own."
{n}Sella agrees to another short rehearsal. The full run will have to wait. When she has gone, Aranka leans against you for a moment, weary and still affectionate.{/n}
"Next time I look impressed, make sure you deserve it."''', c('[Stay to hear Rovan before ending the shortened rehearsal.]', "rovan", flags=("aranka.timing_missed",))),
    n("separate", "Aranka", '''{n}Sella sings without accompaniment. It is slower than the version Aranka taught you. A breath falls between the question and the door; the pause makes you wait for whoever might answer.{/n}
"Again?" Aranka asks.
{n}She listens twice. On the third attempt she joins only the final word, and Rovan tries a single tap before the phrase begins.{/n}
"That's where I come in," he says.
"That's where you might come in," Sella says. "Let me get used to having a door knocked on while I'm singing about it."
{n}They laugh. It takes most of the rehearsal to build the harmony back around that space. You do very little except sit still and occasionally say whether you can hear the words. Aranka keeps glancing toward you, as if surprised to find you content with the task.{/n}
"You have been extraordinarily patient," she says when they stop.
"Should I demand a solo?"
"Absolutely not. We have made such progress."''', c('[Ask Rovan which part he wants to keep.]', "rovan", flags=("aranka.timing_patient",))),
    n("rovan", "Aranka", '''{n}Rovan turns the sticks between his fingers.{/n}
"I don't mind keeping time. I mind everyone introducing me as the man who used to sing. They look so sorry that I end up comforting them. Then they ask whether I've tried a priest. Yes. Several. I know what my throat can do today."
"What should I call you?" Aranka asks.
"Rovan would be a daring experiment."
"Rovan it is."
{n}He demonstrates a roll, catches one stick against the other, and ruins the flourish by dropping it. Aranka laughs. He bows from the waist without standing.{/n}
"That part was intentional."
"Excellent. We need a little suspense."
{n}When he leaves, Aranka picks up the stick he forgot and calls him back. He returns at a theatrical crawl, retrieves it, and leaves with the dignity of a man who knows everyone watched.{/n}
"I had a whole speech ready about courage," she admits to you. "He would have hated it."
"You could use it on me."
"No. You receive too many. I shall tell you something dreadful about your singing instead."''', c('"You have not heard me sing."', "lesson")),
    n("lesson", "Aranka", '''"An omission I intend to correct."
{n}She stands in front of you and gives you the first three notes. The third is higher than you expect. Your attempt makes her eyes brighten with a pleasure she is trying very hard to disguise.{/n}
"Again. And stop watching my mouth as if it might provide the answer."
"It is distracting."
"Then imagine how difficult this is for me."
{n}She comes closer and places two fingers against your side, asking you to breathe into the space beneath them. You follow the movement. For a few seconds neither of you sings.{/n}
"There," she says softly. "That was better."
"Was it?"
"I was listening to a different thing."
{n}Her fingers lift. She steps back far enough to give the lesson a chance, then offers the notes once more. This time she lets your imperfect version finish before answering it.{/n}
"Would you rather sing one line with us, or stay among the listeners? Either would help. I will be nervous. Having you where I can find you would be nice."
{n}She catches your collar between finger and thumb and straightens it with unnecessary care.{/n}
"This is the part of the rehearsal I have prepared best."''',
        c('"Give me one line. I will learn it before the performance."', flags=("aranka.sings_line", "aranka.rehearsal_kept")),
        c('"Find me among the listeners. I will be paying attention."', flags=("aranka.listens_close", "aranka.rehearsal_kept"))),
], "aranka.rehearsal_agreed")

s("the_name_missing", "The name missing from the song", '"You said someone wanted to speak to us."', [
    n("start", "Aranka", '''{n}The woman waiting with Aranka has folded her cloak into a narrow bundle. She grips it so tightly that the knuckles of one hand show pale. Aranka's greeting is quiet.{/n}
"This is Neris. She heard a verse I was trying."
"The one about a man who went back for his friends," Neris says. "He didn't."
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
"I thought it sounded like a story people needed."
"I needed him to come back," Neris says. "That is different."
"Yes."
{n}Neris turns and looks straight at you.{/n}
"I'm not asking you to find him. I have asked enough people who needed me to believe they could. I'm asking her to stop singing that I was rescued by a man who wasn't there."
"Were you alone at the gate?"
"For a while. A woman with a broken cart took me with her. I didn't learn her name. There wasn't time to ask everyone to become part of a song."
{n}Aranka's face changes. She had begun to reach for a thought; she lets it go.{/n}
"I won't ask you to give me a better ending," she says. "The verse comes out."
{n}Neris loosens her grip on the cloak. It takes her a moment to believe that the argument has ended.{/n}''', c('[Stay while Aranka tells her what she will change.]', "correction")),
    n("correction", "Aranka", '''"Some people already heard it," Aranka says. "Taking it out won't make them forget. I can tell them I got it wrong when we perform. I can also speak to the man who told me, so he stops repeating my version as if I confirmed his."
"Without inviting them to come and ask me?"
"Without giving them your name."
{n}Neris nods, once. She does not thank Aranka for the promise. She says she will be nearby for a little while if Aranka needs to ask what can be said, then walks away before either of you can offer her a seat.{/n}
{n}Aranka watches the empty space where she stood.{/n}
"I liked that verse. I was pleased with it. I could hear people singing it before I'd finished."
"You can still write something else."
"I know. That is the particularly unpleasant part. I could turn this into a song about learning a lesson and have everyone applaud me by sunset."
{n}She rubs both hands over her face, then drops them.{/n}
"I don't want to be applauded for that. Help me hear the ending without rushing to replace him."''', c('[Listen to the two endings she is considering.]', "endings")),
    n("endings", "Aranka", '''{n}The first version ends with the traveler reaching a lighted house. The door opens, but the words do not say who stands behind it. Aranka lets the final chord rest without filling the silence.{/n}
"That is as far as the singer knows," she says. "We can stop there."
{n}The second gives the last question to the listeners. Each may answer with the name of someone they actually met on the road, or let the question pass. The melody leaves enough room for an awkward answer.{/n}
"That could become a mess," you say.
"A tremendous mess. Somebody will say a horse. Somebody will say your name and expect a speech. But someone might remember the woman with the cart. Or their own person, who did something worth remembering without doing it beautifully."
"You cannot know what they will say."
"That is what makes me want to try it. It is also what makes me want to sit under a tree and sing to myself."
{n}She tests the unresolved chord again. You can hear her liking it.{/n}
"Choose what you would want to hear. I need an answer from a listener, not a pardon."''',
        c('"Leave the door open. Let the unfinished question stand."', "door"),
        c('"Give the last question to the listeners. Make room for an answer you cannot rehearse."', "answers")),
    n("door", "Aranka", '''{n}She sings it once without looking at you. The last note hangs for a moment above the grass. No one rushes to finish it.{/n}
"I'll need to teach the others not to tidy that up. Rovan will want one more tap. I will want one more word."
"Will you resist?"
"With great and visible suffering."
{n}The joke is small, but it brings her back toward you. She takes your hand and folds it between both of hers.{/n}
"Thank you for staying through that. I wanted to charm my way out of being embarrassed. You looked as if you would notice."
"I notice when you charm me."
"Not always. I keep records."
{n}She touches your fingers to her lips, then releases them before you can ask for evidence.{/n}
"Come back for the performance. I would like at least one person to know why the ending sounds unfinished."''', c('[Promise to hear the song as she now intends it.]', flags=("aranka.ending_door", "aranka.song_revised"))),
    n("answers", "Aranka", '''{n}She sings the question toward you, then waits. You give her the name of someone who once helped you without waiting to be asked. The name fits badly into the tune. Aranka repeats it anyway, changing the rhythm until the person seems to belong there.{/n}
"Like that," she says. "No polishing the name into something easier."
"You will have to work quickly."
"I like that part. When it goes well, it feels as if a song has opened a window. When it goes badly, I shall look at you until you rescue me with the name of a horse."
{n}She leans into you, smiling now without losing the weariness around her eyes.{/n}
"You know this won't make what I sang before disappear."
"I know."
"Good. I didn't want you to think I was offering a miracle. I was hoping to offer a very good evening, with one thoroughly earned awkward bit."
{n}Her mouth brushes your cheek.{/n}
"Come and see which one we manage."''', c('[Promise to hear what the listeners bring.]', flags=("aranka.ending_answers", "aranka.song_revised"))),
], "aranka.rehearsal_kept", delay=48)

s("an_evening_uncommanded", "An evening uncommanded", '"Are we ready to begin?"', [
    n("start", "Aranka", '''{n}Aranka is warming her voice with a tune that sounds suspiciously like the one she used to tease you during rehearsal. Sella answers from several paces away. She has also brought a familiar solo to follow the new piece, and is quietly testing its opening notes. Rovan turns a stick over the back of his hand, catches it, and looks around to make sure somebody saw.{/n}
"You came," Aranka says.
"I said I would."
"I know. I enjoy it when a good thing happens twice, once in the promise and once when you actually walk toward me."
{n}She catches your hand and kisses you before Sella can pretend she is not watching. Rovan supplies a single solemn tap.{/n}
"No accompaniment for that part," Aranka tells him.
"A waste of my training."
{n}She laughs, then looks back at you with a little flutter of nerves she makes no attempt to hide.{/n}''',
        c('[Ask how the final rehearsal went.]', "ready_heard", requires=("aranka.timing_heard",)),
        c('[Ask whether Sella had time to recover her voice.]', "ready_missed", requires=("aranka.timing_missed",)),
        c('[Listen for the space you found by taking the parts separately.]', "ready_patient", requires=("aranka.timing_patient",)),
        c('"I cannot stay today. Please do not hold the beginning for me."', abort=True)),
    n("ready_heard", "Aranka", '''"We used the time to learn Sella's other verse," Aranka says. "She knew one about a traveler who arrived home with the wrong husband. I am almost certain it was meant to be comic."
"Almost?"
"She sings it with great conviction. Rovan says he knows the husband. I no longer trust either of them."
{n}Sella gives you a broad smile. Her first breath falls exactly where you heard it during rehearsal. This time Aranka waits for it, then joins her without needing to look.{/n}''', c('[Take your place for the evening.]', "venue")),
    n("ready_missed", "Aranka", '''"She rested it," Aranka says. "We had another short rehearsal after that. I let her begin alone, and we kept the upper part lower."
{n}Sella hums the turn for you, then stops before the higher note.{/n}
"Enough to know it's there. I'll save the rest for the people listening."
"We dropped the longest repeat," Aranka adds. "I wanted it, but I want her voice tomorrow more. If anyone demands an encore, Rovan has offered an extremely long solo."
{n}He raises both sticks with such solemn menace that Sella laughs. Aranka waits until the laughter has loosened her shoulders before giving her the next note.{/n}''', c('[Take your place for the shorter arrangement.]', "venue")),
    n("ready_patient", "Aranka", '''{n}The pause is still there. Sella takes it without looking apologetic, and Rovan waits for her instead of chasing Aranka's faster version.{/n}
"We tried it with someone walking past," Aranka says. "She stopped long enough to hear the last line. Then she asked for the beginning. I am taking that as encouragement."
"Did you sing it for her?"
"We did. She corrected a word. Apparently her grandmother's traveler carried a basket, not a bag. We have agreed to leave room for regional luggage."
{n}Sella has the air of a woman who has won a very small argument and intends to enjoy it.{/n}''', c('[Take your place for the evening.]', "venue")),
    n("venue", "Aranka", '''{n}Before beginning, Aranka lifts her face into the wind.{/n}
"Lady of Stars, keep us listening. And if you can persuade the wind to wait until after the quiet part, I would be grateful."
{n}She opens one eye and looks at the grass. It continues to move.{/n}
"We shall project."''',
        c('[Help gather the open circle.]', "circle", requires=("aranka.open_circle",)),
        c('[Join the first small group.]', "rounds", requires=("aranka.rounds",))),
    n("circle", "Aranka", '''{n}People gather unevenly. Some sit close, others remain standing behind them, and a few have evidently come because they heard you would be here. A man calls for the song about the moon.{/n}
"Later," someone promises him.
"No," Aranka says pleasantly. "But I have brought a song with a door. Much less expensive to replace if we damage it."
{n}A few people laugh. The man folds his arms. Aranka starts with a quick piece whose chorus gives the listeners something harmless to argue about. By the third repeat, Sella's low part is carrying the melody and the loudest people have stopped trying to hurry it.{/n}
{n}Then someone spots you and begins a cheer. Others stand to see what they missed. The tune breaks apart around the rising noise. Aranka holds the last note for as long as she can, then lets it go.{/n}
"Well," she says to you, quietly enough that only the performers hear. "You are a very difficult instrument to bring into a room."''', c('[Choose how to give the singers back their evening.]', "attention")),
    n("rounds", "Aranka", '''{n}The first listeners are finishing a meal and make room without much ceremony. Rovan begins a rhythm on the sticks. Sella sings while Aranka supplies a harmony so quiet that people lean toward it before they know they have moved.{/n}
{n}The next group is harder. Two people are arguing over a game, a third wants news, and a woman asks whether the singers know something she can dance to. Aranka gives her half a verse, just enough to make Sella laugh, then asks them to listen to the new song.{/n}
{n}Before she can begin, someone recognizes you. More people drift over. What was a small gathering becomes a ring with no clear place for the singers, and the questions turn toward the war.{/n}
"I thought traveling light would help," Aranka murmurs to you. "Unfortunately we brought the most conspicuous person on the island."
{n}Sella stays beside Rovan instead of beginning over the conversation. Aranka looks at you, waiting to see what you will do.{/n}''', c('[Choose how to make room for the performance.]', "attention")),
    n("attention", "Aranka", '''{n}You could address them. Many are already waiting for it, and a good word might turn their attention where Aranka wants it. You could also leave the center of the gathering and give them time to realize that you are here to listen.{/n}
{n}Aranka rolls her shoulders, loosening them. Her eyes meet yours briefly.{/n}
"I will follow what you try," she says. "For a little while. Then I would very much like to sing."''',
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
"Thank you," she says when the cheer ends. "We are now going to sing about several people who were late getting home. Nobody needs to stand."
{n}The laughter is uncertain. A few listeners leave, having received the moment they expected from you. You move to the side while Aranka starts a brisk nonsense verse to loosen the remaining crowd. It takes two attempts before Sella joins her.{/n}
{n}The original opening has gone. Aranka asks Sella to leave out her separate solo to keep the evening from running too long. Sella agrees without looking pleased. Then Aranka tells the smaller audience why she has changed the verse they may already know. Her voice is clear, although her hands keep moving against her skirt.{/n}
"I gave it a brave ending I had no right to claim. I have taken that ending out."
{n}She glances toward you once. You stay where she can see you and let her finish.{/n}''', c('[Hear the shorter performance through.]', "part", flags=("aranka.crowd_ceremony",))),
    n("step_aside", "Aranka", '''{n}You move out of the singers' space and sit among the listeners. For a while people keep trying to catch your eye. You return your attention to Aranka until most of them follow it.{/n}
{n}Some leave when no speech arrives. Rovan watches them go. Aranka touches his shoulder, then gives him the beat. He brings the sticks together, and Sella begins so softly that the remaining listeners have to settle to hear her.{/n}
{n}The group is smaller than it might have been. It is listening. Aranka takes that bargain and gives them the whole opening song.{/n}
{n}Before the new piece, she explains the change in the verse. She says she had passed on a story that the person who lived through it did not recognize. She has removed the brave return she invented. She will not identify the woman who corrected her.{/n}
"You can ask me why I believed it so quickly. I have been asking myself. But first I would like you to hear what remains."
{n}She finds you in the group. Her smile is brief and grateful, then she looks toward Sella for the breath.{/n}''', c('[Listen with the people who chose to stay.]', "part", flags=("aranka.crowd_listened",))),
    n("part", "Aranka", '''{n}Sella takes the first line. Rovan waits for her breath. The space they found in rehearsal opens between the notes, and Aranka steps into it without crowding her.{/n}''',
        c('[Sing the line you practiced.]', "sing", requires=("aranka.sings_line",)),
        c('[Let Aranka find you listening.]', "listen", requires=("aranka.listens_close",))),
    n("sing", "Aranka", '''{n}Your first note is not quite where you intended. Aranka moves her harmony beneath it, gives you the pitch with a glance, and lets you finish the line yourself. A listener smiles. You survive being heard imperfectly.{/n}
{n}When Sella takes over, Aranka's fingers brush your wrist once. Then she is watching the other singer again, entirely occupied by the thing the four of you are making.{/n}''', c('[Hear the ending you chose together.]', "ending")),
    n("listen", "Aranka", '''{n}Aranka finds you at the end of the first verse. You do not have to do anything elaborate. You are there, and you are listening. Her next breath comes more easily.{/n}
{n}Rovan catches a falling beat, Sella answers his flourish, and Aranka's laugh enters the tune for half a measure before she brings it back. You hear the little accident travel through the listeners as pleasure.{/n}''', c('[Hear the ending you chose together.]', "ending")),
    n("ending", "Aranka", '''{n}The melody reaches the place where the borrowed hero used to return. Aranka leaves his place empty. The song moves on without naming him.{/n}''',
        c('[Let the unanswered door remain.]', "door", requires=("aranka.ending_door",)),
        c('[Listen to the answers from the crowd.]', "answers", requires=("aranka.ending_answers",))),
    n("door", "Aranka", '''{n}The final chord refuses to settle where the listeners expect. One man begins to clap early, stops, and looks embarrassed. Aranka gives him a small nod without filling the silence for him.{/n}
{n}The last note fades. There is a moment when you can hear the wind in the grass. Then the applause begins, uneven and quite real.{/n}
"I wanted someone to open it," a woman says.
"So did I," Sella replies.
{n}Nobody offers a speech. Rovan tucks the sticks under his arm. Aranka thanks the listeners and promises a quicker tune for anyone still willing to lend her their feet. The woman who wanted dancing is first to stand.{/n}
{n}When Aranka passes you, she says only, "Stay until we're finished?"
You nod. Her hand trails across your shoulder as she goes.{/n}''', c('[Stay through the music and help bring the evening to its end.]', flags=("aranka.performance_kept",))),
    n("answers", "Aranka", '''{n}At first nobody answers. Then a woman says the name of a carter, so quickly that Aranka has to ask her to repeat it. Sella finds room for the name. Rovan makes the awkward rhythm sound deliberate.{/n}
{n}A man names his sister. Another says, "A mule," and the laughter threatens to swallow the next reply. Aranka repeats the mule's name with such grave musical attention that the group quiets to hear what she will do with it.{/n}
{n}The next answer is a woman whose name the speaker never learned. Sella sings, "The woman at the gate," and leaves it there. You cannot tell whether Neris is among the listeners. Aranka does not look for her.{/n}
{n}The ending grows untidy. It lasts longer than planned. When Aranka finally brings the voices together, her face is flushed with the effort and the delight of having kept them from falling apart.{/n}
"That," she says to you as the applause begins, "was considerably more work than a solo."
{n}Then she laughs, takes your hand for one breath, and goes to thank the singers.{/n}''', c('[Stay through the music and help bring the evening to its end.]', flags=("aranka.performance_kept",))),
], "aranka.song_revised", delay=48)

s("the_song_afterwards", "The song afterwards", '"How did the evening leave you?"', [
    n("start", "Aranka", '''{n}You find Aranka humming to herself with her boots beside her. She has a shallow scratch on one ankle and is trying to remember where she acquired it.{/n}
"I danced," she tells you. "This is a much better explanation than whatever heroic story you were preparing. Sit down before I make you hear the whole account."
{n}She pulls you close enough to kiss, then studies your face.{/n}
"I have been wanting to do that since I woke. I tried being industrious first. It was disappointing."
"What became of the singers?"
"Sella has been asked to teach her version to two people who had only heard mine. Rovan has acquired a pupil who wants to learn the trick with the sticks. He is pretending the pupil must earn it through years of devotion."
{n}She looks pleased, then rubs her ankle once more.{/n}
"Neris spoke to me. She said the correction was clear. She didn't say she liked the song. I managed not to ask."
{n}The little smile that follows is more tired than the first.{/n}''',
        c('"And what did you think of my contribution?"', "aftermath"),
        c('"I want more time with you than I have today. Can we postpone?"', abort=True)),
    n("aftermath", "Aranka", '''{n}Aranka stretches her legs out and leans back on her hands.{/n}
"You want the honest answer?"
"I came for the singer. I should probably hear her."''',
        c('[Hear what your short introduction made possible.]', "welcomed", requires=("aranka.crowd_welcomed",)),
        c('[Hear what the misplaced speech cost.]', "ceremony", requires=("aranka.crowd_ceremony",)),
        c('[Hear what happened after you moved aside.]', "listeners", requires=("aranka.crowd_listened",))),
    n("welcomed", "Aranka", '''"You gave us the room, and then you stopped talking. I know how tempting that can be to forget when people are pleased to hear you."
"I was looking forward to hearing you."
"I noticed. It was distracting in an extremely useful way."
{n}She reaches across your lap for her boot, thinks better of it, and leaves her hand there.{/n}
"The man who wanted the moon song stayed for the last dance. He asked Sella whether she knew something faster. He used her name. That may be my favorite result."
"Not the applause?"
"I enjoyed the applause. I am not so virtuous that I forgot it. But I have heard applause that meant people were glad they had seen someone famous. This felt like they had heard something they might carry away."
{n}She presses your knee lightly.{/n}
"I won't employ you as my permanent announcer. You would become unbearable. But I liked having you there."''', c('"What do you want to do next?"', "plans")),
    n("ceremony", "Aranka", '''"I was angry with you for about half a song. Then I was busy. This morning I discovered I was still a little angry, which was inconvenient because I also wanted to kiss you."
"You cut a piece because of my speech."
"Yes. Sella's solo. She had been looking forward to it. I promised I would come and hear it another day, without a grand occasion attached."
{n}Aranka turns her hand palm up between you.{/n}
"I know you meant to help. Next time we should agree on what you will actually say before you start. You have a talent for making every room remember there is a war. It is not always the talent I want beside me."
"Then I will ask before using it."
"Good. Now kiss me again. I have finished that part of the argument and would like to enjoy the rest of being here."
{n}The kiss begins with laughter and slows. When she draws back, the displeasure has not become a joke, but neither has it taken possession of the afternoon.{/n}''', c('"What would you like to make after this?"', "plans")),
    n("listeners", "Aranka", '''"Fewer people stayed than I hoped. I was disappointed. Then Sella started, and I stopped counting them."
"You sounded as if you were enjoying yourself."
"I was. Rovan said it felt like playing for people rather than playing at a wall made of noise. He has become poetic. I fear our influence."
{n}She touches your sleeve, smoothing a crease that returns as soon as she lets it go.{/n}
"I liked knowing where you were. There were moments when I wanted the whole island to hear us. Then I looked at the people who had stayed, and I didn't want to miss them by wishing for everyone else."
"Would you choose the smaller audience again?"
"Some evenings. Other evenings I shall want to be adored by hundreds. I hope you are prepared for this shocking inconsistency."
{n}She tilts her face toward yours.{/n}
"Today one attentive person will do nicely."''', c('"Tell your attentive person what comes next."', "plans")),
    n("plans", "Aranka", '''"There is a traveling singer I used to know who could hear a tune once and make you think he had written it. I envied him horribly. I spent a whole summer trying to learn that trick."
"Did you?"
"Enough to become annoying. Not enough to stop working. I want that again. A place where I am the person listening at the back because I don't know the song."
{n}She turns toward you, serious beneath the warmth.{/n}
"When the war allows it, I want to travel. I have said that before, and I mean it more now. There are people here I love. There are things I can do for them. I don't want to discover, years later, that I stayed because leaving would have disappointed everyone."
"Including me."
"Yes. Including you. I want to miss you sometimes and be very pleased when I find you again. I want you to have things to tell me that I wasn't standing beside you for."
{n}She traces a line along your palm, then closes your fingers over her own.{/n}
"And I want more evenings before that happens. I am not saying goodbye while sitting on your hand."''',
        c('"We can make plans for a stretch of road together, when we are free to take it."', "road"),
        c('"I cannot promise to travel. I want us to keep finding each other anyway."', "meeting")),
    n("road", "Aranka", '''"A stretch," she repeats, smiling. "Good. If we promise to walk every road together, one of us will eventually have to admit that the other keeps choosing hills."
"You have objections to hills?"
"Only when I am carrying everything I swore I couldn't live without. You may have to watch me part with a third pair of shoes. It will be very moving."
{n}She rests her cheek against your shoulder.{/n}
"We won't choose the route today. I want to hear what you want when there isn't a campaign map between us. Perhaps somewhere warm. Perhaps somewhere nobody expects me to improve their dreams. Somewhere with a song I cannot guess the ending of."
"And until then?"
"Until then I would like one evening with you that does not involve an audience. You can tell me a completely unimportant thing, and I shall pay it far too much attention."
{n}She lifts her head and kisses the place just below your ear.{/n}
"I have been saving some attention."''', c('[Arrange another private visit without fixing the future road.]', flags=("aranka.future_road", "aranka.after_song_kept"))),
    n("meeting", "Aranka", '''{n}She turns your hand over and kisses your palm.{/n}
"Thank you for saying it now. I might have enjoyed a very pretty promise for several days before I started hearing the hesitation beneath it."
"I do want you."
"I know. I don't think all wanting has to look like following someone down a road. There will be visits. There will be missed visits. I will write dreadful descriptions of places you should have seen, and you can tell me which parts I exaggerated."
{n}She smiles, then nudges your shoulder with hers.{/n}
"Those are plans for when we can make them happen. Today you are close enough that I am becoming impatient with discussing distances."
"You began it."
"I am versatile. I can begin something else."
{n}Her kiss is slow enough to make the afternoon feel briefly larger. When she steps back, she keeps your hand.{/n}
"Come for an evening when nobody needs us to sing. I want to find out how long I can keep your attention without saying anything clever."''', c('[Arrange another private visit without promising constant travel.]', flags=("aranka.future_meetings", "aranka.after_song_kept"))),
], "aranka.performance_kept", delay=48)

s("no_encore_needed", "No encore needed", '"You promised an evening without a performance."', [
    n("start", "Aranka", '''{n}Aranka has a shawl over one shoulder and a pair of shoes in her hand. She looks you over with frank pleasure.{/n}
"You look suspiciously prepared to be useful. Put that expression away. We are going for a walk."
{n}She leads you along a quiet part of the island path, keeping well back from the edge. The light is changing across the grass. For a while she talks about nothing more consequential than a bird that stole something brightly colored and then seemed unable to decide what to do with it.{/n}
"I admired its ambition. Its planning needed work."
"An artist you recognize."
"Cruel. Accurate, but cruel."
{n}At a sheltered hollow she puts down the shoes and spreads the shawl beside her. When you sit, she settles close enough that your shoulders touch.{/n}
"There. I have brought you somewhere without a chorus. If you hear one, it is entirely your fault."''',
        c('[Stay with her as the light changes.]', "remember"),
        c('"I want this evening, but I cannot give it the time today. Another visit?"', abort=True)),
    n("remember", "Aranka", '''{n}She takes your hand and works her fingers between yours, looking out over the grass.{/n}
"I keep thinking about the rehearsal. The part where everyone stopped trying to make the song happen quickly."
"You were impatient."
"Dreadfully. I could hear the finished thing in my head. I wanted the others to catch up to it. Then they did something I hadn't imagined, and I liked that better."
{n}She turns toward you.{/n}
"I do that with us sometimes. Imagine an evening so thoroughly that I forget you might arrive with a different one in mind. I have imagined several versions of tonight. Some of them were extremely flattering to me."
"Should I ask what happened?"
"You looked at me much as you are doing now. That part was promising."
{n}Her free hand comes to rest against your chest. She waits, enjoying the nearness rather than pretending the touch was accidental.{/n}''',
        c('"And Reverie? I want our time with her to keep its place too."', "reverie", requires=("aranka.ran_reverie_partner", "aranka.ran_keep_final"), forbids=("aranka.ran_release_final",)),
        c('"Tell me which part of tonight you want to try first."', "desire")),
    n("reverie", "Aranka", '''{n}Aranka smiles before answering.{/n}
"So do I. She asked me once whether people in the waking world really manage to be in love while doing so many other things. I told her we do our best, with occasional unfortunate scheduling."
"That sounds like you."
"She was not impressed. She thought we should arrange a much better calendar. I would like to hear her plan when we see her again. It will probably involve abolishing mornings."
{n}Aranka's thumb moves over your knuckles.{/n}
"We can ask her for time together. I want that to be something the three of us choose when we are there. I also wanted this walk with you. Both wishes seem to fit quite comfortably inside me."
{n}She looks toward the deepening sky, then back at you with a quick, mischievous smile.{/n}
"And when I tell her I spent the evening being kissed, I hope to have a very good account."
"You haven't yet."
"A terrible flaw in the story. We should attend to it."''', c('[Return to the woman beside you.]', "desire")),
    n("desire", "Aranka", '''{n}She leans close enough that the next words warm your cheek.{/n}
"I want to kiss you until I stop thinking about whether it is time to go somewhere else. I want your hands on me. And I would like to hear what you want before I become unbearably pleased with my own ideas."
{n}You touch her waist. Her breath changes. She tips her face toward yours, then stops just short of the kiss, eyes bright.{/n}
"You can tell me to slow down. I will complain about the suspense, but I rather like suspense when I know who I am waiting for."
{n}The shawl has slipped from beneath one elbow. She retrieves it, laughing at the small interruption, and rests her forehead against yours.{/n}
"There. All the romance in the world, and I still sat on a root."''',
        c('"I want to stay with you tonight. Somewhere we can both be comfortable."', "night"),
        c('"Kiss me here. I have to leave tonight, but I have time now."', "kiss"),
        c('"I want the quiet evening and your hand in mine. Let us leave the rest for another time."', "quiet")),
    n("night", "Aranka", '''"A brilliant proposal. I knew there was a reason to bring you."
{n}She kisses you, then gathers her shoes and gets to her feet. You have not let go of her hand, and she bends for another kiss. The second kiss lasts long enough for the shoes to fall from under her arm.{/n}
"Those have become inconvenient," she says.
"You need them for the walk."
"I have been reminded of another inconvenience."
{n}You retrieve the shoes while she folds the shawl. She walks beside you rather than pulling you along, letting the anticipation survive the distance. Once you reach the private shelter she has arranged for the evening, she pauses at the entrance and looks back at you.{/n}
"Still the evening you wanted?"
{n}You answer by drawing her close. She meets you eagerly, hands warm at the back of your neck. Inside, the world narrows to the sound of her laughter when you have to untangle the shawl, then to a silence neither of you is in any hurry to break.{/n}
{n}Later she lies against you, tracing a wandering line along your arm. She hums three notes and stops.{/n}
"No encore," you remind her.
"That was entirely private."
{n}In the morning she finds one shoe beneath the bedding and accuses it of following the two of you for improper reasons. You leave after a slow goodbye, with the song from rehearsal returning to you in fragments and the warmth of her mouth easier to remember than any finished verse.{/n}''', c('[Keep the evening as part of the life you are already choosing together.]', flags=("aranka.extension_night", "aranka.extension_kept"))),
    n("kiss", "Aranka", '''{n}She answers with a kiss that makes good use of the time. Her hand settles at your neck; the other draws you nearer until the shawl shifts between you. When she pulls back, she looks pleased enough to make you laugh.{/n}
"What?"
"You seem to approve."
"I am considering a repeat performance."
"You promised there would be none."
"An unfortunate choice of words."
{n}The next kiss is slower. Afterwards you remain close while the light fades, talking in broken little pieces about things that do not need to become plans. She tells you a ridiculous story about an innkeeper who charged extra for a room with a view of a painted window. You tell her something equally unimportant, and she laughs as if she has been waiting all day to hear it.{/n}
{n}When it is time to leave, she folds the shawl and puts on her shoes. She walks back with you until your paths divide.{/n}
"Come and find me when you can," she says. "I want to hear what you have been doing, even if none of it rhymes."
{n}Her goodbye kiss almost begins another conversation. She lets you go with a laugh and a last squeeze of your hand.{/n}''', c('[Leave with another visit wanted.]', flags=("aranka.extension_kiss", "aranka.extension_kept"))),
    n("quiet", "Aranka", '''{n}She kisses your knuckles instead and settles against your shoulder.{/n}
"Then I shall have to be interesting in other ways. Fortunately I have prepared a number of opinions about birds."
"All admiring?"
"One extremely critical. You will know when we reach it."
{n}You spend a while discovering that she has, in fact, noticed a remarkable amount about the small thefts taking place around the camp. Her imitation of an outraged bird is so exact that something in the grass answers it. She breaks into delighted laughter and refuses to try again.{/n}
{n}Later the talk grows slower. She keeps your hand under the fold of the shawl, turning it now and then as if getting used to the shape. When you tell her an ordinary thing you have missed, she listens without turning it into an invitation to fix your life.{/n}
"I would like to be there when you have that again," she says.
"I would like that too."
{n}You stay until the air cools, then walk back together. There is a little reluctance in the way she releases your hand, and pleasure in the way she looks at you before turning away.{/n}
"That was a good evening," she says. "I had not imagined the bird."''', c('[Keep the quiet evening without changing the relationship already earned.]', flags=("aranka.extension_quiet", "aranka.extension_kept"))),
], "aranka.after_song_kept", delay=48)

# The first six visits resolve one island project, not the whole relationship.
# These later conversations let the established lovers disagree about fame,
# authorship and the Commander's power without turning Aranka into an admirer.
s("the_story_that_follows", "The story that follows", '\"I heard a new version of the song.\"', [
    n("start", "Aranka", '''{n}Aranka sits on a low stone wall with one boot planted beside her. She turns a cup in her hands while two travelers cross the island path below. One tells the other that the Commander persuaded a song to change its own ending. The moon has apparently testified.{/n}
"I thought I had corrected that verse," she says.
"You did. This is a new verse. It has me bargaining with the moon. I did not know it could be so easily persuaded."
"Perhaps it heard you sing."
{n}She smiles, but does not laugh.{/n}
"I know how this happens. A tale leaves its maker and comes back with a brighter coat. I like a bright coat. I don't like people deciding the woman who wrote the song is only there to make the Commander more interesting."
{n}She takes your hand. Her thumb circles once over your knuckles. The affection is plain; the question in her face is not an invitation to agree automatically.{/n}''',
        c('"We could offer them a ridiculous version, if we tell them first that we made it up."', "trickster", requires=("trickster",)),
        c('"We can tell the travelers the song is yours and leave the story there."', "correct"),
        c('"Let the story travel. You can write another song that changes what it means."', "let_go")),
    n("trickster", "Aranka", '''"You want to add another lie to the pile." She studies you. "A very clever one, I expect."
"A fiction that knows its own name. We say it is made up before anyone hears it. Then you tell them what really happened."
"And if they only remember the moon?"
"Then we tell them again."
{n}She slips her hand free. The distance is small, but she has made it on purpose.{/n}
"I love a good trick. I have watched you turn a room inside out and make everyone glad they were there. But these people aren't a room you can reset. They have names, and they will tell your version after you leave."
"I can take the blame."
"You can take the blame for what you do. You cannot take the part of the story that belongs to me. Ask me before you turn my song into bait."
{n}She waits. There is no practiced smile to make the answer easier.{/n}''',
        c('"Then we do it together, if you want the game. You decide what stays true."', "game"),
        c('"You are right. I will not make you the punchline or the lure."', "correct", flags=("aranka.story_restraint",))),
    n("game", "Aranka", '''"Together, then. The travelers hear a ridiculous fabrication, clearly introduced as ours, and I get the last word. If they don't want to hear it, we stop."
{n}She reaches for your hand again. The terms have not erased her objection; they have given her a choice in what follows.{/n}
"You look pleased," you say.
"I am deciding whether to kiss you for listening or for being a menace with an excellent speaking voice."
"Can it be both?"
"It can. But first we ask whether they want to hear a made-up verse."''',
        c('[Ask the travelers whether they want the openly fictional moon verse.]', "shared")),
    n("correct", "Aranka", '''"That is less entertaining than I wanted it to be," she says. "Which is usually how I know it was wise."
{n}She stands and comes close enough for her knee to brush yours. She does not ask you to apologize twice.{/n}
"You let me tell the truth in my own voice. I want to thank you properly, but I also want to be annoyed that you are good at this."
"You could start with annoyed."
"No. I have other plans for my mouth."''',
        c('[Leave the travelers their story and let Aranka decide what she sings next.]', "quietly", flags=("aranka.story_restraint",))),
    n("let_go", "Aranka", '''"A new song is not a correction," Aranka says. "But it might be an answer. I don't want to spend every evening chasing the first people who heard a bad verse."
{n}She leans her shoulder against yours. Her smile returns, small and a little tired.{/n}
"Let it travel. I will write the next one for the people who are willing to listen. You can sit beside me and try not to become the chorus."
"I will do my best."
"Do something better than your best. Be quiet when I need the room."''',
        c('[Stay beside her and leave the travelers undisturbed.]', "quietly", flags=("aranka.story_left_alone",))),
    n("shared", "Aranka", '''{n}Before singing, you tell the travelers that you and Aranka invented the moon verse together as a joke. Aranka watches their faces to be sure they understand it is fiction.{/n}
"We like a good joke," the older traveler says, "if the singer gets the last word."
"I do," Aranka answers. "Would you like to hear it?"
"Yes," says the younger traveler. The older one nods. "Go on."
{n}Only after both travelers agree does Aranka give them the version with the moon demanding an encore. She makes the moon sound insufferable. The younger traveler laughs hard enough to nearly drop her pack.{/n}
"That was fun," the older one says. "What actually happened?"
{n}Aranka answers before you can. She sings the refrain as she wrote it, including the place where she chose to stop rather than give the crowd a heroic finish. She lets the final note settle without adding a word.{/n}
"There," she says. "That is mine. The joke was ours; the song is mine."''',
        c('[Let Aranka keep the last word, then walk back together.]', "desire", flags=("aranka.story_game", "aranka.story_conversation_done"))),
    n("quietly", "Aranka", '''{n}The travelers continue down the path. Aranka watches until the bend hides them, then turns toward you.{/n}
"I could have gone after them," she says. "I wanted to. I had the next verse ready in my mouth, and you let me swallow it."
{n}She kisses you slowly, as if she has the whole evening to decide what it means.{/n}
"You can still be a menace. Just don't sing over the quiet ones."''',
        c('[Tell her what you want from the woman who keeps challenging you.]', "desire", flags=("aranka.story_conversation_done",))),
    n("desire", "Aranka", '''"Keep surprising me," she says. "But the night the moon verse went round, you had the whole path laughing before the older one could finish her question, and she never did finish it. When I say stop, stop there. Put the joke down and let the other voice come in."
"I can do both."
"You can try both. Start with the second one. It's the harder tune."
{n}She catches your collar between two fingers and draws you closer. This time the smile is unmistakably inviting.{/n}
"Now, what did you mean about making another mess together?"''',
        c('"I meant I want you. Here, with no audience and no story to perform."', "private"),
        c('"I meant I want you beside me when the next impossible thing happens."', "road"),
        c('"I meant both, if you want both."', "both")),
    n("private", "Aranka", '''"Good," she says. "I have spent enough time being listened to tonight. I would like to be touched now."
{n}Her hand settles at the back of your neck. She waits until you meet her eyes, then kisses you with a confidence that leaves no doubt about what she wants. When you answer, she draws you off the path toward the sheltered hollow behind the wall.{/n}
"No performance?" you ask.
"Not one anyone else gets to hear."''',
        c('[Take the private evening she is offering.]', flags=("aranka.story_conversation_done",)),
        c('[Kiss her here, then leave the rest for another night.]', flags=("aranka.story_conversation_done",))),
    n("road", "Aranka", '''"That sounds lovely," she says. "It also sounds like a plan that might swallow every afternoon we have left."
"I can make room for the quiet ones."
"Make room for me to change my mind, too. I want to see where your road goes. I don't want to be the song you hum so you never notice you're walking alone."
{n}She kisses you, warm and unhurried, then rests her forehead against yours.{/n}
"Come find me when the impossible thing is over. I will decide whether I want to follow it with you."''',
        c('[Keep the invitation open and let her set the next journey.]', flags=("aranka.story_conversation_done",))),
    n("both", "Aranka", '''"I do," she says. "I want nights when the only danger is that you will distract me from the song. I want roads where neither of us has to pretend that love means staying in one place."
{n}She kisses you and lets the contact deepen at her pace, one hand firm at your shoulder. Then she steps back just enough to look at you.{/n}
"Tonight I would rather have the first. The road can wait until I have slept."''',
        c('[Go with her to the sheltered hollow for a private evening.]', flags=("aranka.story_conversation_done",)),
        c('[Choose a kiss now and agree to speak about the road later.]', flags=("aranka.story_conversation_done",))),
], "aranka.extension_kept", delay=48)

s("the_next_verse", "The next verse", '\"I wanted to ask how the story traveled.\"', [
    n("start", "Aranka", '''{n}Several days have passed since the travelers left. Aranka has asked you to meet on the island path where the song's singers can come and go without turning the afternoon into an audience. She leans against the low wall, a folded sheet of music tucked into her belt.{/n}
"This is not the morning after anything," she says, reading your smile. "It has been long enough for me to change my mind twice and write down neither version."
{n}She offers you her hand. The kiss she gives you is warm and unhurried, but she does not use it to answer the question she has brought you here to ask.{/n}''',
        c('[Ask what happened after the moon verse was introduced as fiction.]', "game_checkin", requires=("aranka.story_game",)),
        c('[Ask how it felt to let the rumor pass without chasing it.]', "restraint_checkin", requires=("aranka.story_restraint",)),
        c('[Ask what she has written since choosing to let the tale travel.]', "left_alone_checkin", requires=("aranka.story_left_alone",))),
    n("game_checkin", "Aranka", '''"They laughed at the moon and asked me what really happened," she says. "One of them remembered the last line. I liked that. They didn't carry away a false confession from us."
{n}She taps the folded sheet at her belt.{/n}
"The joke made a door. It was still my choice whether I walked through it. I am glad you asked first."''',
        c('[Listen as she explains what she wants from the next song.]', "boundary")),
    n("restraint_checkin", "Aranka", '''"It was difficult not to follow them," she says. "I kept thinking of a better explanation for the next bend in the road. Then I wrote down a line instead. The song can answer them if I want it to. I don't have to chase every version."
{n}She pulls the folded sheet free, then slides it back under her belt.{/n}
"I liked that you left the choice with me. I want to know what you will do with that kind of trust when the answer costs you a little."''',
        c('[Ask what practical promise would answer her question.]', "boundary")),
    n("left_alone_checkin", "Aranka", '''"I wrote a verse about leaving a door open without standing in it," she says. "I have not decided if anyone else will hear it. I am allowed to keep a song unfinished."
{n}She looks at you with the same bright directness she brings to a new melody.{/n}
"And you? Are you willing to let me leave a story unfinished when it would be more convenient for you to have an ending?"''',
        c('[Ask what practical promise would answer her question.]', "boundary")),
    n("boundary", "Aranka", '''"You listen beautifully. You also make the world rearrange itself around you, and I adore the nerve of it. But I have watched what happens to a song that stands too near a legend. People stop singing it and start singing about it."
{n}She taps the folded sheet at her belt.{/n}
"So. My name goes above this one. I decide where it travels and who sings it next. If I ever hear it in a hall I never chose, with your name ahead of mine, I will stop singing it, and I will not tell you why. Can you live beside that?"
{n}She waits for you to answer instead of softening the question with a kiss.{/n}''',
        c('"If you object, I will stop and listen before defending myself."', "listen"),
        c('"I want a life with you. I will make room for your work and your road."', "life"),
        c('"You are free to leave whenever you like. I will not hold you here."', "empty")),
    n("listen", "Aranka", '''"That is a start," she says. "What would you actually do?"
{n}She unfolds the sheet and shows you the title line. Her name is written above the song; beneath it are blank spaces for the voices that helped shape it.{/n}''',
        c('[Make a named working copy with Sella and Rovan, and let Aranka choose where it travels.]', "specific"),
        c('[Tell her you need time to think through a specific promise, and ask to return to the question.]', "defer")),
    n("life", "Aranka", '''"That is a beautiful sentence," she says. "Tell me what it changes before I agree that it is a plan."
{n}She unfolds the sheet and shows you the title line. Her name is written above the song; beneath it are blank spaces for the voices that helped shape it.{/n}''',
        c('[Make a named working copy with Sella and Rovan, and let Aranka choose where it travels.]', "specific"),
        c('[Tell her you need time to think through a specific promise, and ask to return to the question.]', "defer")),
    n("empty", "Aranka", '''"That tells me I may leave," she says. "I know. It puts the whole decision on me after I have asked what you will do with your power. I don't want reassurance that costs you nothing."
{n}She takes a breath and steps back. The affection remains, but she is done trying to pull a concrete answer out of you today.{/n}
"I am going to travel for a while, and I want the space to decide what I want to share. Do not arrange an escort or turn the trip into a story. If you want to continue this conversation, meet me here after three days with an answer you have actually considered."''',
        c('[Accept the pause and leave the question with her.]', flags=("aranka.after_story_deferred",))),
    n("defer", "Aranka", '''"That is fair," she says. "I don't want to invent a promise just to keep this conversation pleasant."
{n}She folds the page and puts it away. She does not kiss you to make the pause feel smaller.{/n}
"I am going to take three days for my own work. If you still want to answer, meet me here then. If you do not, the song and my road still belong to me."''',
        c('[Accept the pause and let her decide whether to invite you back.]', flags=("aranka.after_story_deferred",))),
    n("specific", "Aranka", '''"That I can understand," she says. "I keep the original. Sella and Rovan each get a copy with their part named. I decide if and when the copies travel beyond the people who made them."
"And your road?"
"I take the song to three Desnan camps over the next ten days and ask for verses people want to share. I go alone unless I invite you to meet me on the way."
{n}She smiles, pleased by the shape of it but not waiting for praise.{/n}
"You can help me make the copies this afternoon. In two days, I choose my first road."''',
        c('[Agree to the concrete plan and help her prepare the named copies.]', flags=("aranka.relationship_plan",))),
], "aranka.story_conversation_done", delay=48)

s("the_song_and_the_road", "The song and the road", '\"You said you chose the first road.\"', [
    n("start", "Aranka", '''{n}Two days later, Aranka sits at the wall with three finished copies beside her. Each names the voice that shaped its verse. She has kept the original folded in her own satchel.{/n}
"The first copy goes to Sella. The second to Rovan. The third stays with me until I have heard what the camps want to add."
"And the ten days?"
"I will visit three camps and ask if they want to trade songs. If I find a new verse, I bring it home in my own hand. If I don't, I still get ten days of road."
{n}She offers you one of the blank margins. The invitation is practical, and it belongs to her.{/n}''',
        c('[Help write the credits, then let her choose when to send the first copy.]', "copies", requires=("aranka.relationship_plan",))),
    n("copies", "Aranka", '''"You have not put your name on it," she says, checking the margin.
"It is your song."
"And the little lie?"
"Ours, and only because you agreed to tell them it was made up."
{n}She reads the credits once more, makes a small correction to Rovan's rhythm note, then seals each sheet in its own fold. The work is modest, specific, and hers to carry.{/n}
"Tomorrow I leave for the first camp. I may send you a letter. I may be too busy singing to remember. Either way, I will come back with my own account of the road."''',
        c('[Kiss her goodbye and let the ten days belong to her.]')),
], "aranka.relationship_plan", delay=48)

s("the_deferred_answer", "The deferred answer", '\"I came back to the question.\"', [
    n("start", "Aranka", '''{n}Three days have passed. Aranka has returned from a short walk with her travel bag beside her. She has not gone far; she wanted the time to think without the audience of your expectations.{/n}
"You said you would come back with an answer you had considered. I am listening."
{n}She does not reach for your hand yet.{/n}''',
        c('"I will protect your byline, keep your original yours, and ask before I join or announce your road."', "plan"),
        c('"I still have no answer. You were right to ask me to think before I promised."', "not_yet")),
    n("plan", "Aranka", '''"That is specific," she says. "I can decide whether to trust it by watching what you do."
{n}She takes your hand, not to seal a vow but because she wants to. Her kiss is brief and warm.{/n}
"I will write the credits, make the copies, and take the song to three camps over ten days. I am going alone. If I want you beside me, I will say so."
"I will wait for your invitation."
"Good. That lets me look forward to seeing you without having to promise when."''',
        c('[Agree to wait for her letter and leave the road hers.]', flags=("aranka.relationship_plan",))),
    n("not_yet", "Aranka", '''"Thank you for not disguising that as an answer," she says. "I will take the road anyway. I don't need you to solve the question before I can choose where to go."
{n}She kisses your cheek, affectionate but unhurried.{/n}
"I don't know when I will want to speak about this again, if I do. Don't send anyone after me or arrange another meeting. I will write only if I want you to know where I am."''',
        c('[Let her travel without turning the pause into a test.]')),
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

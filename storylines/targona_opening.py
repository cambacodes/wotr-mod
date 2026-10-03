"""Correspondence extending installed RanRomance's completed Targona finale."""
from story_format import c, n, scene

SCENES = []
RELATIONSHIP = dict(
    Title="What she carries out", Description="Targona has begun sending me pages she wants someone to read with her. Our earlier choices remain our own.",
    Objective="Read Targona's correspondence", Guidance="After completing RanRomance's Angelic Treatment finale, read the correspondence in Drezen. Allow time for replies.",
    StartedFlag="targona.started", ClosedFlag="targona.closed", CommittedFlag="targona.committed",
    UnavailableFlags=["targona.dead_lab", "targona.dead_lair", "targona.condemned", "swarm", "demon", "lich", "devil"], FailureFlags=[],
)
ETUDES = {
    "targona.free": "720af1f72f413354db3f4d41f76d5af6",
    "targona.dead_lab": "3b8bd37108050a94b9be14e22501e090",
    "targona.dead_lair": "bc65b234df544a718afc4856eb7f33fc",
    "targona.condemned": "1aaee57d670b0494e9d8662bffbf4f6a",
    "targona.ran_none": "4774e38b267c47f2b5f6c0975ec486f0",
    "targona.ran_angel": "e1837a6b241f4095a4312e0115988721",
    "targona.ran_azata": "2660c0d29eaf4dce9de52b3994462df1",
    "targona.ran_aeon": "383cc2c9ea3f47c4a71982cb06535118",
    "targona.ran_trickster": "64e2b82829694b8fac652ea06f4dc8a7",
    "targona.ran_romance": "80cb9c6f466b4eaaaa9561ca56c5f348",
    "targona.ran_lich": "480fead956f24022930a83d4457a377c",
    "targona.ran_demon": "6ba14669a2a74dfbb308f66fecda8f6e",
    "targona.ran_devil": "df70df5cb6824ff5a9776a2478eee6c6",
    "targona.ran_legend": "94bc04d1ed474feaab54af2f77a94574",
    "targona.ran_dragon": "ecdddd77ad964561b38ad1848cb4553f",
    "targona.ran_late_change": "2edcb6e5a1c3439fa9b9e0b3b96a49fb",
}
COMPLETED_QUESTS = {"targona.ran_treatment_completed": "6ec03ce2f763460c8ac89f4c2064c5ad"}
SEEN_CUES = {"targona.ran_final_seen": [
    "ad655c40be31401386b85287483b3841", "cfc5f3cb2cf94672a96cab742e62225d",
    "62c24328ae744ee98fabd219dbe74c92", "ec76729da60441a1b2028f340743c0a8",
]}
ALLOWED = ["targona.ran_none", "targona.ran_angel", "targona.ran_azata", "targona.ran_aeon", "targona.ran_trickster"]
MET = "targona.trickster.met"   # r5: the Trickster ward's angel lives in Drezen; her letters come from the ward, not the wayhouse
BLOCKED = ("targona.closed", "targona.dead_lab", "targona.dead_lair", "targona.condemned", "swarm", "demon", "lich", "devil",
           "legend", "dragon", "targona.ran_lich", "targona.ran_demon", "targona.ran_devil", "targona.ran_legend", "targona.ran_dragon")


def s(id, title, nodes, previous=None, delay=24, requires=(), forbids=()):
    for page in nodes:
        page["Portrait"] = "TargonaCorrespondence"
    SCENES.append(scene("targona." + id, title, "Targona", 5, "Read Targona's correspondence", nodes,
                        requires=("targona.free", "targona.ran_treatment_completed", "targona.ran_final_seen") + ((previous,) if previous else ()) + tuple(requires),
                        forbids=BLOCKED + tuple(forbids), delay=delay, optional=True, Relationship="targona",
                        Remote=True, ManualOnly=True, Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[5], RequiresAny=ALLOWED))


s("unasked_question", "The house of the enemy", [
    n("start", "Narrator", '''{n}The packet waiting among your personal correspondence holds a letter and a folded drawing. Targona has written your name on the outside, not your title.{/n}
"Commander. I have begun an account of Areelu's refuge, for my comrades in the host. Know the house of your enemy better than she knows it herself: I learned that before I learned the sword, and I have never had cause to doubt it.
"So I have been drawing her laboratory. The chains. The ring of purple fire. I keep drawing a door, though I could not swear there was one, and every time I set it down I put the lock on the outside. I know very well I am free. I give thanks for it at morning prayers. Then at night I sit down with a pen and lock myself in again.
"I can give a report of a battle. This I cannot seem to give. I am asking you. You have been into the Abyss and walked out of it. Look at it as a soldier would, and tell me what you see."''',
      c("Unfold the drawing.", "drawing"), c("Put the drawing aside until you can give it an unhurried hour.", abort=True)),
    n("drawing", "Narrator", '''{n}A square room. A ring on the floor where the purple fire burned. A door whose hinges she has drawn twice, once on each side, and a neat arrow pointing out through it. The lock lies across the arrow like a bar across a gate.{/n}
Beneath it she has written, in a smaller hand:
"I do not ask you to go back there. I would not go back for anything. Some of the distances will be wrong. I spent very little time looking at it from above."
The last sentence is underlined once, as though she has decided you may laugh at that much.
"There are hours I cannot account for, and I will not invent them for my account. Areelu Vorlesh is incapable of contrition, even for a heartbeat; she would like nothing better than an angel who misremembers her prison. I will not give her that.
"Tell me the first thing you see. Do not soften it."''',
      c('Write: "You drew the way out before you drew the bar across it."', "exit"),
      c('Write: "You drew the hinges twice. You didn\'t trust your own memory."', "hinges")),
    n("exit", "Narrator", '''{n}You mark the place where the arrow begins. Its first stroke is darker than the line laid over it.{/n}
"You drew the way out first," you write. "The bar came afterwards, in a thinner line. Scouts do the same with a ford they were nearly drowned in: the crossing goes down first, and the current after, when they remember it. Your hand knew the way out before it knew the lock.
"Keep your account as you remember it. Bar and all. Then send me a copy, and I'll mark where a sapper would have gone through that wall if anyone had been fool enough to send one."
{n}There is room left beneath your answer for something that is not about the room at all.{/n}''',
      c("Continue the letter.", "personal")),
    n("hinges", "Narrator", '''{n}You copy both sets of hinges onto a scrap. One door swings in, into the room. The other swings out, flat against the corridor wall.{/n}
"You drew both," you write. "You could have rubbed one out and sent me a clean drawing. You sent me the one where you weren't sure. I'd trust that over any map a scout ever handed me with a straight face.
"Put it in the account that way: two hinges, and the angel who drew them didn't know which. Then send me a copy. I'd like to know which way that door swung, because whoever built it meant something by it."
{n}You set the scrap beside the letter and leave space beneath it.{/n}''',
      c("Continue the letter.", "personal")),
    n("personal", "Narrator", '''{n}The folded room is small enough to cover with one hand. You leave it open while you finish.{/n}''',
      c('Write: "I miss you. Send me the hard letters too. I\'d rather have those than none."', "romance", requires=("targona.correspondence_romanced",)),
      c('Write: "You don\'t have to make it easy to read. I\'ll read it anyway."', "friend", forbids=("targona.correspondence_romanced", MET)),
      c('Write: "You don\'t have to make it easy to read. I\'ll read it anyway."', "friend_ward", requires=(MET,), forbids=("targona.correspondence_romanced",))),
    n("romance", "Narrator", '''{n}You write down the way she looks when she has decided to say a thing before she has found the words for it, and how you once leaned in to hear her though her voice was perfectly clear.{/n}
"I want another evening with you. An ordinary one, with nothing in it that needs binding or praying over. And I'll take the hard letters as well. You needn't pay for one with the other."
The last line comes out less polished.
"I've cleared a corner of my desk for whatever you send next. The quartermaster's reports are sulking about it."
{n}You seal the letter and keep the drawing out of the official dispatches.{/n}''', c("Send your reply with the next personal correspondence.", flags=("targona.correspondence_opened",))),
    n("friend", "Narrator", '''{n}You write that you want to hear what the wayhouse is like: who comes in off the eastern road, what the chaplain burns in the stove, whether the soup is as bad as Drezen's. You start a list of questions and cross it out before it turns into orders.{/n}
"If you tire of this, say so and we'll quarrel about something else. I'd rather have a blunt friend than a polite one."
You leave a clean strip at the bottom of the page and label it ROOM FOR A COMPLAINT ABOUT ANYTHING BUT THE WAR.
{n}Her drawing goes back with the letter, uncertain hinges and first arrow intact.{/n}''', c("Send your reply with the next personal correspondence.", flags=("targona.correspondence_opened",))),
    n("friend_ward", "Narrator", '''{n}Her ward behind Wilcer's stores is a hundred paces from your door, and still the two of you are writing to each other: you are never in it when she is awake, and she is never out of it. You write that you want to hear about it anyway: who came in off the walls today, what the chaplain burns in the stove, whether the soup is as bad as the barracks'. You start a list of questions and cross it out before it turns into orders.{/n}
"If you tire of this, say so and we'll quarrel about something else. I'd rather have a blunt friend than a polite one."
You leave a clean strip at the bottom of the page and label it ROOM FOR A COMPLAINT ABOUT ANYTHING BUT THE WAR.
{n}Her drawing goes back with the letter, uncertain hinges and first arrow intact. A runner carries it the hundred paces.{/n}''', c("Send your reply with the next personal correspondence.", flags=("targona.correspondence_opened",))),
], delay=0)


s("second_margin", "An uplifting account", [
    n("start", "Narrator", '''{n}Targona sends back your letter with a new sheet. She has filled the strip for complaints.{/n}
"The brother who packed these pages used enough string to truss a sheep. I spent longer freeing the paper than drawing on it. That is my complaint. I enjoyed writing it more than is fitting.
"Yes, send me the copy. I will keep one drawing with my account and one with your letter.
"I looked at the bar again. I remember drawing it. I was angry, because the door looked too easy to open, and it was never easy. Not once. You saw it before I did, and I am a little vexed that you did."
{n}Below this, her hand grows smaller.{/n}
"There is a man in Drezen gathering crusaders' accounts for a book. He has asked me for the laboratory. Something short, he says, and uplifting. I said yes before I had thought, because he asked kindly, and an angel is not in the habit of refusing a kind request. Now I cannot get past his word. Uplifting."''',
      c("Read the additional note.", "anograt", requires=("targona.ran_trickster",)),
      c("Read the additional note.", "anograt", requires=("targona.ran_aeon",), forbids=("targona.ran_trickster",)),
      c("Read Targona's proposed account.", "account", forbids=("targona.ran_trickster", "targona.ran_aeon"))),
    n("anograt", "Anograt", '''{n}A different hand has occupied most of the margin.{/n}
"Silver asked me to help. I offered to write the account from the lock's point of view. It would be a short career followed by a deserved retirement. She did not laugh, which in Silver means she wanted to.
"We have been sharing a table. Silver gets the chair with the good cushion; I get the edge of the paper she hasn't written on yet. You can see how much she values my contribution.
"She keeps crossing out the parts where she is angry. I keep writing them back in the margin. We are at eleven each.
"My proposal is that we give the collector the most uplifting account imaginable: a door rising off its hinges and striking the woman who built it. Silver says that is not what happened. I said the word was uplifting, not accurate."
{n}Targona has written beneath this: "This is why I still need your answer."{/n}''', c("Read Targona's proposed account.", "account")),
    n("account", "Narrator", '''{n}Her draft begins with the prisoners who sheltered near her barrier because her light kept the demons off them. She does not name them. She does not pretend to know what became of them. Then the sentences go cold, the way a sermon goes cold when the preacher has stopped believing it.{/n}
"The captive angel remained a source of protection. Her suffering was therefore not without purpose."
The lines are struck through so hard that the nib has torn the sheet.
"I wrote that," Targona says underneath. "No collector put it in my mouth. I wanted the reader to have something to hold, and I found I had written him a reason to leave me in the barrier.
"Men lived because I was there. I thank Iomedae for every one of them. I would have sheltered them awake, with a sword in my hand, if anyone had let me. Areelu chained an angel, and the prisoners near her were safer for it, and I will not print a sentence that makes the second thing pay for the first."
The page ends with a question. Should she write it for him now, or tell him no?''',
      c('Tell her to write it short, in her own name, with the anger left in.', "publish"),
      c('Tell her to refuse him plainly and keep the pages for herself.', "private")),
    n("publish", "Narrator", '''{n}You write a first line for her to throw away if she likes: "Men lived because I was there. That is not why I was there."{/n}
The rest of your answer is short. She need not account for every hour or end on a lesson. She can write what she remembers, say plainly what others told her afterwards, and leave the lost hours lost.
You tell her the cost as well, because she would find it for herself anyway. Once it is printed men will quote it badly, and sooner or later somebody will write the tidy sentence back in for her.
"Write it the way you'd give a report to your comrades," you finish. "Send it if you want to. Don't put an amen at the end of it."''', c("Send your advice to publish.", flags=("targona.account_public",))),
    n("private", "Narrator", '''{n}You tell her to refuse him plainly, without promising him a later date to sweeten it.{/n}
"Your comrades can have the true account. He can get his uplifting paragraph from a man who wasn't there."
You tell her the price too. Other men will tell her story with less of her in it, and her silence won't make them truthful. You put that down plainly, because she would despise you for hiding it.
"If you change your mind, write and say so. Until then I'd like to read what you struck out."
{n}You fold his proposed heading behind the reply without correcting it.{/n}''', c("Send your advice to refuse him.", flags=("targona.account_private",))),
], "targona.correspondence_opened")


s("the_folded_room", "Which way the door swung", [
    n("start", "Narrator", '''{n}The next packet holds two copies of the room and a strip of paper broad enough to cut a small door from. She has kept the first drawing with her account.{/n}
"I did as we said about the collector. I will tell you what came of it when something has.
"Now the door. You asked which way it swung, and I cannot tell you, and it galls me. I remember everything else about that place that I would rather forget, and not this.
"I have drawn the hinges both ways on this copy. Work it out however a soldier works out a wall: by looking, by cleverness, or by cutting through it. I suspect you are qualified in at least two of those."
{n}The copied lines almost meet at one corner. Beneath them she has written: "Send it back even if you fail. A scout who comes back from a bad road has still mapped it."{/n}''',
      c("Study the fold and the two sets of hinges.", "study"),
      c("Cut a simple paper door and leave the disputed hinges visible.", "cut")),
    n("study", "Narrator", '''{n}Folded along one line, the sheet traps the door beneath a flap. Folded along the other, it opens but carries part of the room outside. There may be a way to use both creases, provided you can tell a turning edge from the mark of the lock.{/n}
Targona has numbered the corners so you can report what you tried. The smallest number has nearly disappeared into a fold. Beside it she has written an indignant replacement, twice the size of the others.
You test a corner without pressing it flat. The inner lines are faint beneath the new ink. You could study them closely, or stop treating the drawing as a puzzle with one hidden answer and simply go through the wall.''',
      c("[Perception] Follow the faint inner line and find a fold that opens outward.", check=dict(Skill="SkillPerception", DC=25, Success="found", Failure="creased", CommanderOnly=True)),
      c("Make a new opening instead of solving the old arrangement.", "cut")),
    n("found", "Narrator", '''{n}The faint line ends just short of the apparent corner. You fold there, reverse the inner flap, and find it: a small door that opens outward, into the corridor, without carrying the room with it.{/n}
You mark the sequence in Targona's numbering. The construction is awkward rather than elegant, which is how real doors in real fortresses usually turn out.
"It opens outward, on paper at least," you write. "It took three folds, and the first two made it worse; I've marked those as well. Whether her real door did, only she knows, and I'd rather not ask her."
You return the worked copy with a blank one beside it. Before sealing the packet you open the little door again. It catches on your thumbnail. You add an arrow where she should lift it.''', c("Return the construction and its instructions.", flags=("targona.fold_found",))),
    n("creased", "Narrator", '''{n}The inner line disappears beneath your first crease. When you fold the flap back, the door catches and tears at its top corner. Another attempt only enlarges the tear.{/n}
You put the damaged copy beside the untouched one. For a moment it is tempting to begin again and send only the better result. Her line about scouts stops you.
"I couldn't make the two hinges agree," you write. "I tore the paper trying. The door opens now, but only because its corner is ripped, and I won't pretend that was the plan."
You set down your attempts in order and leave the spare copy blank.
"Your account will have to make do with a torn map and an honest report. I've given worse to Irabeth and lived."
{n}Both copies go into the packet. The failed one remains on top.{/n}''', c("Return the failed attempt honestly.", flags=("targona.fold_failed",))),
    n("cut", "Narrator", '''{n}You cut three sides of a rectangle in the clear part of the copied wall. The fourth becomes a hinge. You trim a narrow strip from the flap's free edge so it opens without catching. When you lift it, the drawing opens onto the surface of your desk.{/n}
It is an almost insolently simple answer to a careful diagram. You keep the discarded strip and write down exactly what you did.
"I didn't find her door. I made one. Every sapper in the crusade will tell you that's the quicker way through a wall."
At the bottom you add a practical improvement: the new door wants a small handle so it can be opened without tearing its corner.
{n}The uncertain original hinges remain visible. The new door does not need them to be correct.{/n}''', c("Return the new opening and the strip you cut away.", flags=("targona.fold_cut",))),
], "targona.second_margin")


s("an_unpromised_future", "A tale for the fever ward", [
    n("start", "Narrator", '''{n}Targona's reply includes the paper door. She has added a handle shaped like a very small wing, and written OPEN HERE beside it in unnecessarily large letters.{/n}
"The chaplain asked what the handle was for. I told him it was for opening the door, and then heard myself say it the way I would say it to a recruit, and laughed at myself.
"He carried it to the man whose fever keeps him awake. The man opened it six times before he would give it back. I am glad I made the handle."
{n}Her account of what happened to the drawing follows.{/n}''',
      c("Read how she used the successful fold.", "found", requires=("targona.fold_found",)),
      c("Read what she did with the torn copy.", "failed", requires=("targona.fold_failed",)),
      c("Read what she made of the new door.", "cut", requires=("targona.fold_cut",))),
    n("found", "Narrator", '''"Outward. Your folds work; I did them twice.
"I did your folds twice. The third time I did them in the wrong order and shut the little lock inside the room. I kept that one too; it is the only version of that room I have ever enjoyed.
"I still do not know how her door was truly made. But I know how to make one that opens, and I gave thanks for that at dawn prayers."
{n}The letter moves on to the collector. Her hand is firmer here than it was round the copied hinges.{/n}''', c("Read about her account.", "account")),
    n("failed", "Narrator", '''"Thank you for sending the torn one on top. Irabeth was right to let you live.
"I tried the spare. My door caught too. So I cut a new hinge at the torn corner, which would be a poor repair on any door that has to keep out the weather. For a map of a ruin, it serves.
"I have kept both copies, yours and mine, with a note in my hand saying neither of us knows which way the door swung. An honest gap in a report has saved more soldiers than a confident lie.
"I tried your torn copy again before dawn, and thanked Iomedae for smaller mercies."
{n}She turns to the collector without apologising for how little the paper did.{/n}''', c("Read about her account.", "account")),
    n("cut", "Narrator", '''"I laughed when I saw the hole. Then I rebuked myself for laughing. Then I opened it again.
"I gave your door a handle. You will see its shape is grander than the carpentry deserves. I chose it because it pleased me. At compline I caught myself giving thanks for a paper door, and smiling before the prayer was done.
"I have pinned your strip of cut wall beside the drawing with a note: 'The way through, as found by the Commander.'
"I did that before dawn prayers, and was early to them for once."
{n}Below this she has written about the collector.{/n}''', c("Read about her account.", "account")),
    n("account", "Narrator", '''{n}A second sheet records her reply to the collector, in her own words rather than a copy of yours.{/n}''',
      c("Read the consequences of publication.", "public", requires=("targona.account_public",)),
      c("Read the consequences of refusing publication.", "private", requires=("targona.account_private",))),
    n("public", "Narrator", '''"I sent him the short account. I wrote that I am glad men lived near me, that I was a prisoner, and that the one does not explain the other. I left the lost hours lost.
"He wrote back asking me to take out the line where I say I hated the room. He said it took something from the courage of the survivors. I told him the line was about the room and not about them, and that if he struck it I would come to his shop and read it to him aloud. He has kept it.
"A sergeant of the Mendevian line wrote to me afterwards. He said it made him less ashamed of how angry he still is about the Worldwound. I answered him the same day. Another reader asked why an angel needs so many words. I have not answered him. I prayed for patience instead, and that prayer has not been answered either.
"I am glad I sent it. I am gladder that I do not have to send another."
{n}At the bottom she has begun a question meant only for you.{/n}''', c("Read the private question.", "question", forbids=(MET,)),
      c("Read the private question.", "question_ward", requires=(MET,))),
    n("private", "Narrator", '''"I refused him. He was courteous and disappointed, and then he printed another man's account in the place mine would have gone. It gives me one paragraph. It says that the angel Targona gave herself to the Architect's barrier of her own will, so that her light might shelter the camps, and that her sacrifice was accepted in Heaven. It is beautifully written. Every word of it is a gift to Areelu.
"I was so angry I broke a basin. One of the good ones. The sister who keeps the linen made me sweep it up myself, which was just.
"There are men in the Mendevian camps who will read it and believe that what was done to them near that laboratory was an angel's holy choice. It was not. It was Areelu's, and she chose it for all of us. When my duties next allow, I will go to his shop and ask him, before Iomedae, to print a correction. I will not shout. I will not need to.
"I still will not give him my pages. But I will not let him give her mine."
{n}She has left the next question on a line of its own.{/n}''', c("Read the private question.", "question", forbids=(MET,)),
      c("Read the private question.", "question_ward", requires=(MET,))),
    n("question", "Narrator", '''"I meant to put the drawing away and finish my account. Then the men asked whether the little door had a room behind it. I had made a handle fit for a fortress gate and furnished nothing at all. They were right to ask.
"So: a task, and I want your help with it. The men in the wayhouse ask me for stories at night, when the fever is bad and nobody can sleep. They do not want the lives of the saints; they have heard those. They want a soldier who wakes in the enemy's house and gets out. I mean to write them one. Awake, with a sword by the door, and Iomedae's name in her mouth.
"Tell me how she gets out, or whom she lets in, if she would rather hold the room. You have got out of worse places than I have; your reports say so, in a very modest voice."
{n}There is a lightly drawn rectangle below the words, waiting for something to be put inside it.{/n}''',
      c('Suggest a scene in which she chooses to leave.', flags=("targona.story_leaving",)),
      c('Suggest a scene in which she chooses who may enter.', flags=("targona.story_receiving",))),
    n("question_ward", "Narrator", '''"I meant to put the drawing away and finish my account. Then the men asked whether the little door had a room behind it. I had made a handle fit for a fortress gate and furnished nothing at all. They were right to ask.
"So: a task, and I want your help with it. The men in the ward ask me for stories at night, when the fever is bad and nobody can sleep. They do not want the lives of the saints; they have heard those. They want a soldier who wakes in the enemy's house and gets out. I mean to write them one. Awake, with a sword by the door, and Iomedae's name in her mouth.
"Tell me how she gets out, or whom she lets in, if she would rather hold the room. You have got out of worse places than I have; your reports say so, in a very modest voice."
{n}There is a lightly drawn rectangle below the words, waiting for something to be put inside it.{/n}''',
      c('Suggest a scene in which she chooses to leave.', flags=("targona.story_leaving",)),
      c('Suggest a scene in which she chooses who may enter.', flags=("targona.story_receiving",))),
], "targona.the_folded_room")


s("the_unscheduled_door", "Meret of the host", [
    n("start", "Narrator", '''{n}The tale Targona sends is short, and written in a hand meant to be read aloud by lamplight. She has given its soldier a name that is not her own.{/n}
"I have called her Meret. A sergeant from Kenabres says he knew a Meret, and that she would have liked this. I chose to believe him.
{n}Meret, a sergeant of the host, wakes in a room with a chair, a closed door, and a parcel tied with a thoroughly unreasonable quantity of string. The parcel gets three lines. The demon who built the room gets none.{/n}
"I read it to the fever ward last night," Targona writes. "They argued about the string for an hour. Nobody died before morning. I am not saying the two are connected. I am not saying they are not."
{n}You read the ending your suggestion gave her.{/n}''',
      c("Read Meret's departure.", "leaving", requires=("targona.story_leaving",)),
      c("Read Meret's invitation.", "receiving", requires=("targona.story_receiving",))),
    n("leaving", "Narrator", '''{n}Meret takes the chair to the door, breaks the lock with its leg, and walks out into a street she does not recognize. A watchman asks whether she is expected somewhere. She says that she is, at the nearest muster, and asks him the way.{/n}
She carries the parcel with her, because it is hers. On a bench by the muster gate she unpicks the knots. Inside is a cup she has never liked. She trades it at the first stall for a chipped blue one and spends the difference on something sweet enough to make the vendor warn her.
"The men wanted her to kill the demon on the way out," Targona writes. "I told them the demon was not in the story, because the demon does not deserve a line. They accepted this. One of them cried, which he has asked me not to tell you."
{n}The last line says only that Meret reaches the muster before roll call. A little ink has spread beneath the word 'reaches'.{/n}''', c("Consider what you might add.", "method")),
    n("receiving", "Narrator", '''{n}Meret does not leave. She sets the chair against the door, draws her sword, and holds the room. Then she opens the parcel and finds a cup she has never liked, and puts it on the table anyway, because a garrison should be able to offer a guest something.{/n}
She chalks a notice on the door: KNOCK. THE CUP IS NOT FOR LENDING.
The first to knock is a crusader who has lost his company and wants to borrow a spoon. Meret nearly runs him through, then decides an honest request deserves an honest answer. She lends him the spoon, refuses him the cup, and asks whether he knows anywhere selling better ones. He directs her to a stall at the corner. She chooses a chipped blue cup, leaves the old one for guests, and makes him swear by Iomedae to return her spoon.
"The ward liked her," Targona writes. "She is less gracious than I meant her to be. The man with the spoon is a corporal from the third cot, and he has demanded to be in the next one."
{n}The tale ends with the door held at an angle Meret chose herself.{/n}''', c("Consider what you might add.", "method")),
    n("method", "Narrator", '''{n}Targona has left the other side of the sheet blank for your part. She has written one condition at its top, in a soldier's capitals: THE MEN HAVE VOTED. SHE DOES NOT DIE.{/n}
You can add another street to the tale, a reply from the corporal with the spoon, or simply tell her which line made the ward laugh. You copy out her ending first. By the time you reach the parcel, you have developed a strong dislike of its string.''',
      c("[Trickster] Give the copied page a folded ending that refuses to stay last.", "trick", requires=("trickster",)),
      c("Write a second ordinary scene, leaving her first ending intact.", "ordinary")),
    n("trick", "Narrator", '''{n}You copy the little door onto both faces of a spare sheet, measuring each from the same corner, and fold the sheet into a narrow concertina. THE END goes on the last panel. A corridor goes on the panel tucked beneath it.{/n}
Open the door and the corridor unfolds past the supposed ending. Turn the strip over and the second door opens onto the same folds. It is a sapper's joke, the kind men make in a trench about walls that were meant to be the last one.
Your first attempt tears at the hinge. You keep it beside the sound one and copy the folding instructions onto the back, step by step, the way you would write orders for a man who has to do it in the dark.
"A sapper's objection to the word last," you write. "There is usually another wall."
{n}You enclose both attempts with her unchanged original. The torn one gets a warning in the margin: "Do not pull this one too hard."{/n}''', c("Send the altered copy alongside the unchanged original.", flags=("targona.extra_ending",))),
    n("ordinary", "Narrator", '''{n}You leave Meret's ending where Targona put it. On the next page you give her a soldier's inconvenience: the chipped blue cup will not fit in a pack, and a sergeant of the host cannot be seen carrying crockery through the muster.{/n}
The trouble is small enough to be funny. Meret makes an unnecessarily elaborate plan involving her helmet, abandons it, and carries the cup in her hand through the whole muster with her chin up. You sketch the helmet plan and discover halfway through that you cannot make it work either.
"The third cot can have his spoon back in the next one," you add. "Tell him I said so."
{n}You return the two scenes together, including the failed sketch.{/n}''', c("Send the second scene with her original.", flags=("targona.ordinary_ending",))),
], "targona.an_unpromised_future")


s("what_she_keeps", "A letter she wanted to write", [
    n("start", "Narrator", '''{n}Targona's latest letter is less carefully arranged than the others. The first paragraph has been moved with an arrow, a second thought has been squeezed above the date, and a faint ring marks where a cup stood too near the edge.{/n}
"I began this before I knew what it was about. I do not recommend it."
{n}Her answer to your page occupies the first sheet.{/n}''',
      c("Read her response to the Trickster page.", "trick", requires=("targona.extra_ending",)),
      c("Read her response to the ordinary continuation.", "ordinary", requires=("targona.ordinary_ending",))),
    n("trick", "Narrator", '''"I opened your door and found your corridor, and followed your instructions, and my first corridor came out upside down. I have kept it. I kept the torn one too, and did not pull it too hard.
"For a moment I wished there had been such a fold in her laboratory. There was not. I will not draw one into my account; an account that lies about the walls gets soldiers killed.
"But I can put one in Meret's story. The corporal from the third cot insists she should take the corridor, and carry her cup carefully. He has tried your torn hinge and made it worse, and is very proud of himself.
"Send me another street when you have time. I have promised him no more than that."
{n}She has drawn Meret opening the door from its unexpected side. The figure carries a cup.{/n}''', c("Read the next page.", "voices")),
    n("ordinary", "Narrator", '''"The ward laughed at the helmet plan until the chaplain came to see whether we were all dying. Then I improved the plan in the margin, which I believe was exactly the trap you laid for me.
"I gave Meret a companion for the next street: the corporal from the third cot, who talks too much about his mother's pottery. She discovers she does not mind. He has his spoon back. The ward voted on that as well.
"I still wake with the old room in my thoughts sometimes. I have no triumphant ending to attach to that sentence. But there are other things on the table now. A cup I like, a tale the men ask for, and letters I am glad to receive.
"I did not expect a cup to do so much. I suppose that is what cups are for."
{n}She has enclosed the beginning of the new street, stopping before the corporal can explain a second glaze.{/n}''', c("Read the next page.", "voices")),
    n("voices", "Narrator", '''{n}The next sheet is folded separately from the tale.{/n}''',
      c("Read the two notes inside.", "two", requires=("targona.ran_trickster",)),
      c("Read the two notes inside.", "two", requires=("targona.ran_aeon",), forbids=("targona.ran_trickster",)),
      c("Read Targona's private note.", "personal", forbids=("targona.ran_trickster", "targona.ran_aeon"))),
    n("two", "Anograt", '''"Silver says I may write this part myself. An extraordinary concession, considering that I have been writing in the margins from the beginning.
"You sent your page back. Good. When we disagree about a story you get two letters, not one sensible compromise. Nobody has ever made a sensible compromise with a wing.
"My opinion is that Meret should keep the bad cup and use it to hold the collector's rejected adjectives. Eventually she could sell them. There is clearly a market."
{n}Targona's reply sits immediately below.{/n}
"I prefer the chipped blue cup. I also prefer Anograt saying what she thinks under her own name, rather than in my margins pretending to be me.
"Keep addressing the letters to me. Add a page for her if you wish. She will read over my shoulder either way; I would rather she did it openly. An enemy in the open is half beaten, and she is not even an enemy, most days."''', c("Read Targona's final lines.", "personal")),
    n("personal", "Narrator", '''"There is something else. Every letter I have sent you has had the laboratory in it somewhere. That is not what I think about when I think about you."
{n}The sentence ends at the fold. You open the lower half of the sheet.{/n}''',
      c("Read what your lover chose to write.", "lover", requires=("targona.correspondence_romanced",)),
      c("Read what your friend chose to write.", "friend", forbids=("targona.correspondence_romanced",))),
    n("lover", "Narrator", '''"I miss kissing you. There. I have written it without first telling you how useful your last letter was, and I am not sorry.
"I miss the pause before you decide whether to say something outrageous, and the times you decide against it and I can tell anyway. I want an evening with you when neither of us has a page to finish or a man to sit with."
{n}The next line has been crossed out and replaced.{/n}
"I nearly promised to be easier company. That would be a lie, and I do not tell those. I can promise to be glad when you come.
"Until then, write me something you have wanted to tell me. It may be foolish. I have grown fond of the parts of your letters no clerk would copy."
{n}She signs her name below the invitation. You read the first line again before reaching for a fresh sheet.{/n}''',
      c('Reply with affection and a private joke for the next letter.', flags=("targona.extension_opening_kept", "targona.private_letters",)),
      c('Reply that you want that quiet time too, and will arrange it when you can.', flags=("targona.extension_opening_kept",))),
    n("friend", "Narrator", '''"Tell me about something you enjoyed. It need not serve the crusade. I find I like news that nobody thought important enough to send.
"Bad stories. Quarrels about cups. Whatever the quartermaster said this week that he should not have. Send me those too, between the hard pages."
{n}She has enclosed another blank strip beneath the signature.{/n}
"For your complaint. I promise not to make it uplifting."
{n}You leave the strip beside your unfinished reply. It is too narrow for the complaint you have in mind. You fetch a larger sheet and begin with that.{/n}''',
      c("Send a personal reply and keep the correspondence open.", flags=("targona.extension_opening_kept",))),
], "targona.the_unscheduled_door")


s("the_open_threshold", "A door that opens both ways", [
    n("start", "Narrator", '''{n}Targona's letter carries the impression of a page opened and closed many times. She has drawn a small door beside the seal.{/n}
"I am tending the wounded at a wayhouse on Drezen's eastern road. The courier who brought this can carry your reply back there. It is on Golarion, and the road between it and the city is ordinary.
"I do want to see you. I have wanted it since the last packet, and I have been ashamed of how often I reread it.
"But I know you, a little. If there is a trick in your answer, tell me what it is before you ask me to walk through it. I spent a long time behind Areelu's barrier. I will not step through another door I have not seen tested, not even yours. If the road is all we have, the road will do."
{n}The invitation names the Drezen courtyard as the meeting point. The courier's dispatch slip carries the same wayhouse address as Targona's letter.{/n}
{n}You read the last line twice, and then go and find out how long the eastern road is on foot.{/n}''',
      c("[Trickster] Give her a door she can test before she walks through it.", "paper_setup", requires=("trickster", "targona.extra_ending")),
      c("[Trickster] Use the ordinary courier route and a fortunate change of dispatch.", "courier_setup", requires=("trickster", "targona.ordinary_ending")),
      c("Decline the meeting tonight and keep the correspondence open.", "declined"),
      c("Answer that you will leave the letter in the courier's hands.", "ordinary", forbids=("trickster",))),
    n("paper_setup", "Narrator", '''{n}Your folded corridor is still on your desk, the torn hinge beside it. She has told you what she thinks of doors she has not seen tested. Then give her one she can test.{/n}
In the citadel's east wall there is a postern the demons bricked up and warded while they held Drezen. The engineers have chalked it unsafe and left it alone. Beyond it a goat track runs down to the eastern road below the gate, out of sight of every sentry on the wall. Unbrick it, kill the old ward, fit a new lock, and an angel walking in from the wayhouse could reach the courtyard without being stared at by a single watchman.
The ward has to be truly dead first. If it is not, there is no invitation.''',
      c("[Knowledge (Arcana)] Unpick the demons' ward and test the postern before inviting her.", check=dict(Skill="SkillKnowledgeArcana", DC=30, Success="steady", Failure="falter", CommanderOnly=True)),
      c("Do not risk a passage. Send an ordinary invitation by the known courier road.", "road")),
    n("courier_setup", "Narrator", '''{n}The ordinary page hid no door, and you do not pretend it did. What you have is a named wayhouse, a courier who runs the eastern road twice a week, and a woman who wrote that she wants to see you.{/n}
You buy the dispatch clerk a bottle and a quiet hour, and your sealed invitation goes into the returns bag on top instead of at the bottom. The courier who was meant to carry a packet of requisitions reaches the wayhouse before her evening duty with your letter in his hand, and he never learns why the clerk was so cheerful.
She writes back in her own hand, on the back of yours. She will walk the public road to Drezen, if you still want her to come.''',
      c("Send the courier back with your invitation.", "road"),
      c("Do not send it. Keep the correspondence open.", "declined")),
    n("ordinary", "Narrator", '''{n}You do not make a magical route. You write that the invitation will wait with the courier, and that the road from her wayhouse is an ordinary one.{/n}
She replies that she will not come this week: there is fever on the eastern road, and eleven men in the wayhouse who need an angel more than you do. You answer with an ordinary account of your day, including one detail too small for any dispatch.
She sends back one from hers. The wayhouse cat has taken the chaplain's chair, and nobody in the house has the courage to move it.''',
      c("Send your answer and leave a later invitation to her.", flags=("targona.visit_correspondence",))),
    n("declined", "Narrator", '''{n}You send no key and no courier. You write that you want to see her, and that you would rather see her on a night when the road and the war both allow it.{/n}
Targona's answer is warm, if brief.
"You took me at my word. Few people do; they think an angel's no is only a yes that has not been prayed over long enough. I still want you. Keep writing to me, and one evening I will write back and name the night."
You answer with the smallest news you have, and ask for hers.''',
      c("Write back.", flags=("targona.visit_correspondence",))),
    n("steady", "Narrator", '''{n}It takes two nights. The last thread of the ward parts with a smell like singed hair. You push an empty dispatch pouch through the gap from outside and from within, at dusk and again at midnight, and nothing answers it. A locksmith from the lower town fits a new lock with two keys and is paid not to wonder why.{/n}
{n}The courier carries Targona a written account of the work, the way the goat track runs, and one of the keys. She reads every line of it. Her reply is one sentence: "I will inspect it myself."{/n}
{n}She comes up the track after dark and examines the postern slowly, frame and hinges and the scorched stones where the ward was, the way a healer examines a wound someone else has dressed, and then puts the key in her own pocket.{/n}
"It is well made," she says. "For a trick."''',
      c("Walk the wall with her.", "walk"),
      c("Tell her the wounded on the eastern road will want her at first light.", "close_passage")),
    n("falter", "Narrator", '''{n}The ward does not die. When you push the empty dispatch pouch through the gap, it comes back scorched, its seams turned inside out. You have the gap bricked up again before the courier ever sees it.{/n}
{n}You send an ordinary letter instead, and tell her exactly what failed. Targona answers by the same courier.{/n}
"Thank you for not sending me the key. I would have used it, and you know that, which is why I am glad you did not.
"Write to me tonight instead. Tell me something from your day too small for a dispatch. When there is a road worth trusting, I will walk it."''',
      c("Answer her and keep the correspondence open.", flags=("targona.visit_correspondence",))),
    n("road", "Narrator", '''{n}The courier carries your invitation to the wayhouse. Targona comes by the public eastern road, on foot, stopping twice on the way at the dressing station by the ford because there were men there.{/n}
No spell moves her and no unstable gate closes behind her. She reaches the Drezen courtyard before the appointed hour and waits until you arrive.
"I walked," she says. "It was a long road, and nobody on it looked at the wing. I liked that. Walk beside me the rest of the way."''',
      c("Walk the wall with her.", "walk"),
      c("Tell her the wounded on the eastern road will want her at first light.", "close_road")),
    n("walk", "Narrator", '''{n}You take the path around the courtyard and up onto the wall, where the city noise thins and the evening air reaches the open edge of her wing.{/n}
You ask if the wing hurts today. She answers without apology: sometimes, and not now. Then she asks what you would have done if she had not come.
"Waited," you say. "Possibly complained to the nearest statue."
"Pray for patience instead. It works on commanders too, I am told, though slowly." {n}Her mouth curves.{/n} "I prayed for it all day. It did not take."
The joke has reached its mark, but not its end.
"Everyone looks at me as a sign," she says. "Heaven's healers look at the wing and see Areelu's work. The soldiers look at the other one and see a promise. In that laboratory I was proof of something." {n}She stops walking.{/n} "You look at me the way you did before the last letter, before the kiss I wrote to you about and the one I did not. I have missed being looked at like that more than I will ever admit to a chaplain. Three days on the eastern road, with eleven men to change dressings for, and every one of them I thought: the Commander would be doing this badly, and would ask me to show how, and would not listen."
{n}She turns to face you and leaves her fingers in your sleeve.{/n}
"Commander. You have looked at me like that the whole length of the wall. Are you going to do anything about it?"''',
      c("Ask her again, and wait for her answer.", "kiss"),
      c("Tell her you would rather continue the walk.", "continue")),
    n("close_passage", "Narrator", '''{n}She looks east, where the watchfires are, and then locks the postern herself and tries the bolt twice.{/n}
"You are right, and I hate it. If I stay, I will stay too long, and tomorrow there are wounded on the eastern road who deserve an angel who slept." {n}She smiles, a little ruefully, and offers you her arm.{/n} "Walk me to the gate, at least. I will go out by it like an honest woman; I will not use your trick twice in one night."''',
      c("Walk with her to the road and say goodnight.", "departed")),
    n("close_road", "Narrator", '''{n}She looks east, where the watchfires are.{/n}
"You are right, and I hate it. If I stay, I will stay too long, and tomorrow there are wounded on the eastern road who deserve an angel who slept." {n}She smiles, a little ruefully, and offers you her arm.{/n} "Walk me to the gate, then. Slowly."''',
      c("Walk with her to the road and say goodnight.", "departed")),
    n("departed", "Narrator", '''{n}You walk her as far as the eastern gate. The sentries there have been told nothing, and they look at the wing, and then at you, and then very hard at the road.{/n}
She squeezes your hand before letting go.
"I am glad I came. Do not ask me for the next evening here, at a gate, in front of sentries. Ask me in a letter, where I can say yes slowly."
Two days later the courier brings a note. She reached the wayhouse before midnight, the cat has kept the chaplain's chair, and she prayed for you at compline, which she says you are not to make anything of.''',
      c("Reply with affection and leave the next invitation open.", flags=("targona.visit_pause",))),
    n("kiss", "Narrator", '''{n}Targona does not wait for you to ask twice. She takes the front of your coat in her fist and kisses you, hard and certain, the way she once told Areelu's barrier that she would bear whatever came.{/n}
{n}Her thumb rests beneath your jaw. When she lets you breathe she keeps her brow against yours, her fist still closed on your coat.{/n}
"I have missed that," she says. "Iomedae forgive me, I have missed that more than I missed the wing."
{n}Your hand finds the edge of the wing. She goes very still, and then she does not pull away.{/n}
"Everyone is so careful with it. You are not being careful." {n}Her palm slides to your chest and finds your heart going like a drum.{/n} "There. That is the truest thing anyone has said to me since the laboratory."
{n}She kisses you once more, slower, and then looks past you at the lit windows of the barracks, and at the dark stair beside them, and back at you.{/n}
"Well. Talk, or kisses, or finding out how many buckles there are on this armour. Choose, Commander. I will tell you if you chose wrong."''',
      c("Choose talk, and another kiss.", flags=("targona.visit_tender",)),
      c("Find out how many buckles there are.", "buckles", flags=("targona.visit_desire",)),
      c("Tell her that kiss was enough for one night.", flags=("targona.visit_pause",))),
    n("buckles", "Narrator", '''{n}She counts them aloud on the dark stair, one at each step, and loses count at six because you have stopped on the step below her and she is, for once, the taller.{/n}
{n}In your rooms she does not light the lamp. She sets her back against the door and has your coat off your shoulders before the latch has finished falling, and then the buckles, quick and certain, a healer's hands that have unfastened a thousand wounded men's harness and never once with this much hurry.{/n}
"Eleven," she says against your mouth. "Eleven, Commander. Who arms you? I will have words with him."
{n}She draws her plain wayhouse habit over her head and lets it fall, and a wing opens behind her in the dark and brushes the wall. She pushes you back onto the bed and follows you down, her knees either side of you, her hair falling round both your faces, and takes your hands and puts them where she wants them.{/n}
{n}Long before light she is dressing again by the window. The wounded on the eastern road will want her at the first bell, she says, and she will not let them want her in vain on your account. She kisses you once more at the door, hard, and does not say when.{/n}''',
      c("Let her go back to her road.")),
    n("continue", "Narrator", '''{n}You tell her that a walk is enough. Targona leaves her fingers in your sleeve and chooses the battlements, where the city opens below and the watchfires on the eastern road show where the wounded are coming in.{/n}
"There," she says, pointing. "That fire is the ford. They brought eleven across it this morning. I counted." {n}She is quiet for a moment.{/n} "I have spent my whole life being useful. I am not sure I know how to be idle beside someone."
"Walk until I am tired. Then eat something sweet enough to be imprudent. Then decide whether I want another kiss. That is my plan, and I will not be argued out of it."
{n}She tells you which of the city lights she can see from the terrace, and which she has mistaken for stars, and which is the lamp in the infirmary where a boy with a fever is waiting for morning.{/n}''',
      c("End the evening with affection and leave the next choice open.", flags=("targona.visit_tender",)),
      c("Ask if she would like that second kiss now.", "kiss")),
], "targona.what_she_keeps", delay=0, requires=("targona.correspondence_romanced",), forbids=(MET,))


s("the_key_remains_hers", "The key remains hers", [
    n("start", "Narrator", '''{n}Targona's next letter comes back by the eastern courier, sealed with a thumbprint of candle wax because she has no seal of her own any more.{/n}''',
      c("Read her answer after the intimate evening.", "desire", requires=("targona.visit_desire",)),
      c("Read her answer after the tender evening.", "tender", requires=("targona.visit_tender",)),
      c("Read her answer after you chose to pause.", "pause", requires=("targona.visit_pause",)),
      c("Read her answer to your letter.", "correspondence", requires=("targona.visit_correspondence",))),
    n("desire", "Narrator", '''{n}A small brass key is tied to the page with red thread: the key to the wayhouse's side gate, which the porter locks at compline.{/n}
"I had it copied in the village. A blade of Iomedae, bribing a locksmith. I confessed it the same evening and did the penance, and I would do it again.
"I have been thinking about your stair. I want you. I want the warmth of you against me, and the sound you make when you stop trying to be clever. I have written that sentence three times and burned two of them, and I am sending the third before I lose my nerve.
"Next time I will come on a night when the road is quiet, and I will not be dressing by the window before light."
{n}She has left the last line blank, as if it belongs to the answer.{/n}''',
      c("Write back that you want her, and that the key had better not rust.", flags=("targona.key_reciprocal",)),
      c("Write back that you want to see her, whatever the night turns into.", flags=("targona.key_unpressured",))),
    n("tender", "Narrator", '''{n}A small brass key is folded into the letter. On its tag, in Targona's unmistakable hand, is written: ONLY IF I ASK.{/n}
"I have not stopped thinking about the evening. I want another one. I want to arrive late, with my sleeves still wet from the basins, and kiss you before either of us says anything clever. After that I do not know. I find I like not knowing."
The line beneath her note is left open for an answer.''',
      c("Reply that you want her, and that you will be waiting.", flags=("targona.key_reciprocal",)),
      c("Reply that you want her company, and leave the rest for another day.", flags=("targona.key_unpressured",))),
    n("pause", "Narrator", '''{n}The letter contains no key. Targona writes that she was pleased you let the evening end without asking her to turn it into a promise.{/n}
"I still want you. I was glad you did not hurry me; the wayhouse had fever in it that week, and I would have come to you smelling of vinegar and gone back before the bell. I would like another evening. Come when the wounded let you."
She has added a small sketch of the courtyard, with the way in and out marked in equal-sized arrows.''',
      c("Tell her you want another evening, whenever the wounded can spare her.", flags=("targona.key_unpressured",)),
      c("Tell her you want to kiss her again when she asks.", flags=("targona.key_reciprocal",))),
    n("correspondence", "Narrator", '''{n}Targona's letter contains a short account of an uneventful afternoon and a question about a story you once sent her.{/n}
"We did not meet that evening. I am not sorry. I think I needed one more letter first. Tell me the ending of the story you started last time; you stopped just when the bridge was about to fall, and I have been worrying about the bridge."
She sends a recipe for a sweet she has recently learned to make. The measurements are exact. The instruction to wait before adding the last ingredient has been underlined twice.''',
      c("Reply with an ordinary detail and keep the conversation open.", flags=("targona.key_unpressured",))),
], "targona.the_open_threshold", requires=("targona.correspondence_romanced",))


# r5: the visit's ward variant. The angel of the Trickster ward lives a hundred paces from the Commander's door; what the
# two of them lack is not a road but an hour. Append-only: a new scene after what_she_keeps, for ward histories only.
s("ward_evening", "An hour off the rows", [
    n("start", "Narrator", '''{n}This letter has come a hundred paces, from the ward behind Wilcer's stores, folded small enough to pass through a runner's fist.{/n}
"Commander. The chaplain says I have not had an evening off the rows since I came to Drezen. He is right, and he said it in front of the men, which was unkind of him and accurate.
"I would like one. With you. Not in the loft, where I can hear the third cot coughing through the floor. Somewhere the ward cannot find me for an hour.
"But I will not leave the rows uncovered, and I will not ask the chaplain, because he will say yes and then look at me all week. If you can find a way, find it. If you cannot, I will see you at the cots, and that is not nothing either."''',
      c("[Trickster] Find her rows a keeper she cannot argue with.", "cover", requires=("trickster",)),
      c("Pay the chaplain's two novices to sit the rows, and tell her exactly what it cost.", "paid"),
      c("Put the letter aside until you can answer it properly.", abort=True)),
    n("cover", "Narrator", '''{n}By supper the whole of Drezen knows that the Queen's chaplains will inspect the infirmary at dawn. Nobody can say who said so. By the first bell there are more volunteers scrubbing the floor behind Wilcer's stores than there are wounded in it, and every one of them is watching the cots so as to be seen watching them.{/n}
"There is no inspection," Targona says, when she finds you at the foot of the wall stair. It is not a question. "You lied to the chaplain."
"I lied to Drezen. The chaplain happened to hear it."
{n}She looks back at the lit canvas, at the scrubbing, at the men sitting up in their cots to watch the show, and something in her face gives way.{/n} "Every cot is watched better tonight than any night since I came. I will have to confess it. I will not be sorry."''',
      c("Continue", "wall")),
    n("paid", "Narrator", '''{n}You pay the chaplain's two novices a week's wages to sit the rows until the second bell, and you write it down for her: their names, the sum, the hour they stop. She reads it at the foot of the wall stair.{/n}
"You paid them more than they are worth," she says. "They will be insufferable." {n}She folds the paper into her sleeve.{/n} "Thank you for telling me the price."''',
      c("Continue", "wall")),
    n("wall", "Narrator", '''{n}The wall walk above the stores is empty at this hour. Below, the ward's canvas glows like a lantern, and from up here you cannot hear the coughing.{/n}
"An hour," she says. "I have not had an hour that was not somebody's since the laboratory." {n}She stands at the parapet with her hands on the stone, and then they are not on the stone; they are on your coat, and she is kissing you as if the hour were already half spent.{/n}
{n}There is a watchtower door at the end of the walk, and a guardroom behind it with a brazier nobody has lit. She lights it. Then she pulls her plain habit over her head and lets it fall, and her wings open in the small room and brush the rafters, and she pulls you down with her onto the bench beside the brazier, her mouth at your throat, her hands already at your belt.{/n}''',
      c("[Let the hour run.]", "bell")),
    n("bell", "Narrator", '''{n}At the second bell she is dressed and on the stair before you have found your other boot. At the foot she stops, turns back, and kisses you once more, hard.{/n}
"Next time I will ask for two hours," she says, "and I will not need a lie or a purse to get them. I will simply take them." {n}Then she goes back to the rows.{/n}''',
      c("Go back to your war.", flags=("targona.ward_evening_kept",))),
], "targona.what_she_keeps", requires=("targona.correspondence_romanced", MET))

"""Correspondence extending installed RanRomance's completed Targona finale."""
from story_format import c, n, scene

# Named, unconditional text paragraph: production slot ID, no runtime schema
# extension. The existing buckles node and exit retain identity and mechanics.
EXPLICIT_PARAGRAPHS = {
    "targona.the_open_threshold.explicit.1":
        "{n}She holds you there, her brow against yours, her breath ragged. The last buckle lies beside the door.{/n}",
}

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
"Commander. I have begun an account of Areelu's refuge, for my comrades in the host. I want them to know what held me there. I can describe the chains and the ring of fire. The rest is harder to set down.
"So I have been drawing her laboratory. The chains. The ring of purple fire. I keep drawing a door, though I could not swear there was one, and every time I set it down I put the lock on the outside. I know very well I am free. I give thanks for it at morning prayers. Then at night I sit down with a pen and lock myself in again.
"I can give a report of a battle. This I cannot seem to give. I am asking you. You have been into the Abyss and walked out of it. Look at it as a soldier would, and tell me what you see."''',
      c("Unfold the drawing.", "drawing"), c("Put the drawing aside until you can give it an unhurried hour.", abort=True)),
    n("drawing", "Narrator", '''{n}A square room. A ring on the floor where the purple fire burned. A door whose hinges she has drawn twice, once on each side, and a neat arrow pointing out through it. The lock lies across the arrow like a bar across a gate.{/n}
{n}Beneath it she has written, in a smaller hand:{/n}
"I do not ask you to go back there. I would not go back for anything. Some of the distances will be wrong. I spent very little time looking at it from above."
{n}The last sentence is underlined once.{/n}
"There are hours I cannot account for, and I will not invent them for my account. Areelu Vorlesh is incapable of contrition, even for a heartbeat; she would like nothing better than an angel who misremembers her prison. I will not give her that.
"Tell me the first thing you see. Do not soften it."''',
      c('{n}Write:{/n} "You drew the way out before you drew the bar across it."', "exit"),
      c('{n}Write:{/n} "You drew the hinges twice. You didn\'t trust your own memory."', "hinges")),
    n("exit", "Narrator", '''{n}You mark the place where the arrow begins. Its first stroke is darker than the line laid over it.{/n}
"You drew the way out first," {n}you write.{/n} "The bar came afterwards, in a thinner line. The arrow is still visible beneath it. I have marked both strokes on the copy.
"Keep your account as you remember it. Bar and all. Then send me a copy, and I'll mark where a sapper would have gone through that wall if anyone had been fool enough to send one."
{n}There is room left beneath your answer for something that is not about the room at all.{/n}''',
      c("Continue the letter.", "personal")),
    n("hinges", "Narrator", '''{n}You copy both sets of hinges onto a scrap. One door swings in, into the room. The other swings out, flat against the corridor wall.{/n}
"You drew both," {n}you write.{/n} "You could have rubbed one out and sent me a clean drawing. You sent me the one where you weren't sure. I'd trust that over any map a scout ever handed me with a straight face.
"Put it in the account that way: two hinges, and the angel who drew them didn't know which. Then send me a copy. I'd like to know which way that door swung, because whoever built it meant something by it."
{n}You set the scrap beside the letter and leave space beneath it.{/n}''',
      c("Continue the letter.", "personal")),
    n("personal", "Narrator", '''{n}The folded room is small enough to cover with one hand. You leave it open while you finish. Beneath your answer you mark a clean strip: ROOM FOR A COMPLAINT ABOUT ANYTHING BUT THE WAR.{/n}''',
      c('{n}Write:{/n} "I miss you. Send me the hard letters too. I\'d rather have those than none."', "romance", requires=("targona.correspondence_romanced",)),
      c('{n}Write:{/n} "You don\'t have to make it easy to read. I\'ll read it anyway."', "friend", forbids=("targona.correspondence_romanced", MET)),
      c('{n}Write:{/n} "You don\'t have to make it easy to read. I\'ll read it anyway."', "friend_ward", requires=(MET,), forbids=("targona.correspondence_romanced",))),
    n("romance", "Narrator", '''{n}You write down the way she looks when she has decided to say a thing before she has found the words for it, and how you once leaned in to hear her though her voice was perfectly clear.{/n}
"I want another evening with you. An ordinary one, with nothing in it that needs binding or praying over. And I'll take the hard letters as well. You needn't pay for one with the other."
{n}You dip the pen again.{/n}
"I've cleared a corner of my desk for whatever you send next. The quartermaster's reports are sulking about it."
{n}You seal the letter and keep the drawing out of the official dispatches.{/n}''', c("Send your reply with the next personal correspondence.", flags=("targona.correspondence_opened",))),
    n("friend", "Narrator", '''{n}You write that you want to hear what the wayhouse is like: who comes in off the eastern road, what the chaplain burns in the stove, whether the soup is as bad as Drezen's. You start a list of questions and cross it out before it turns into orders.{/n}
"If you tire of this, say so and we'll quarrel about something else. I'd rather have a blunt friend than a polite one."
{n}Her drawing goes back with the letter, uncertain hinges and first arrow intact.{/n}''', c("Send your reply with the next personal correspondence.", flags=("targona.correspondence_opened",))),
    n("friend_ward", "Narrator", '''{n}Her ward behind Wilcer's stores is a hundred paces from your door, and still the two of you are writing to each other: the casualty rows and your dispatches seldom leave you an unhurried hour together. You write that you want to hear about it anyway: who came in off the walls today, what the chaplain burns in the stove, whether the soup is as bad as the barracks'. You start a list of questions and cross it out before it turns into orders.{/n}
"If you tire of this, say so and we'll quarrel about something else. I'd rather have a blunt friend than a polite one."
{n}Her drawing goes back with the letter, uncertain hinges and first arrow intact. A runner carries it the hundred paces.{/n}''', c("Send your reply with the next personal correspondence.", flags=("targona.correspondence_opened",))),
], delay=0)


s("second_margin", "An uplifting account", [
    n("start", "Narrator", '''{n}Targona sends back your letter with a new sheet. She has filled the strip for complaints.{/n}
"The brother who packed these pages used enough string to truss a sheep. I spent longer freeing the paper than drawing on it. That is my complaint. I enjoyed writing it. He can use less string next time.
"Yes, I will send you the copies you asked for. I have kept the first drawing with my account, and copied both uncertain hinges. Do not tidy them for me.
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
    n("account", "Narrator", '''{n}Her draft begins with the prisoners who sheltered near her barrier because her light kept the demons off them. She does not name them. She does not pretend to know what became of them. Beneath the opening she has written:{/n}
"The captive angel remained a source of protection. Her suffering was therefore not without purpose."
{n}The lines are struck through so hard that the nib has torn the sheet.{/n}
"I wrote that," {n}Targona says underneath.{/n} "No collector put it in my mouth. I wanted the reader to have something to hold, and I found I had written him a reason to leave me in the barrier.
"Men lived because I was there. I thank Iomedae for every one of them. I would have sheltered them awake, with a sword in my hand, if anyone had let me. Areelu chained an angel, and the prisoners near her were safer for it, and I will not print a sentence that makes the second thing pay for the first."
{n}The page ends with a question. Should she write it for him now, or tell him no?{/n}''',
      c('Tell her to write it short, in her own name, with the anger left in.', "publish"),
      c('Tell her to refuse him plainly and keep the pages for herself.', "private")),
    n("publish", "Narrator", '''{n}You write a first line for her to throw away if she likes: "Men lived because I was there. That is not why I was there."{/n}
{n}The rest of your answer is short. She need not account for every hour or end on a lesson. She can write what she remembers, say plainly what others told her afterwards, and leave the lost hours lost.{/n}
{n}You tell her the cost as well, because she would find it for herself anyway. Once it is printed men will quote it badly, and sooner or later somebody will write the tidy sentence back in for her.{/n}
"Write it the way you'd give a report to your comrades," {n}you finish.{/n} "Send it if you want to. Don't put an amen at the end of it."''', c("Send your advice to publish.", flags=("targona.account_public",))),
    n("private", "Narrator", '''{n}You tell her to refuse him plainly, without promising him a later date to sweeten it.{/n}
"Your comrades can have the true account. He can get his uplifting paragraph from a man who wasn't there."
{n}You tell her the price too. Other men will tell her story with less of her in it, and her silence won't make them truthful. You put that down plainly, because she would despise you for hiding it.{/n}
"If you change your mind, write and say so. Until then I'd like to read what you struck out."
{n}You fold his proposed heading behind the reply without correcting it.{/n}''', c("Send your advice to refuse him.", flags=("targona.account_private",))),
], "targona.correspondence_opened")


s("the_folded_room", "Which way the door swung", [
    n("start", "Narrator", '''{n}The next packet holds two copies of the room and a strip of paper broad enough to cut a small door from. She has kept the first drawing with her account.{/n}
"I did as we said about the collector. I will tell you what came of it when something has.
"Now the door. You asked which way it swung, and I cannot tell you, and it galls me. I remember everything else about that place that I would rather forget, and not this.
"I have drawn the hinges both ways on this copy. Work it out however a soldier works out a wall: by looking, by cleverness, or by cutting through it. I suspect you are qualified in at least two of those."
{n}The copied lines almost meet at one corner. Beneath them she has written: "Send it back even if you fail. Mark where it caught; I want to try that fold myself."{/n}''',
      c("Study the fold and the two sets of hinges.", "study"),
      c("Cut a simple paper door and leave the disputed hinges visible.", "cut")),
    n("study", "Narrator", '''{n}Folded along one line, the sheet traps the door beneath a flap. Folded along the other, it opens but carries part of the room outside. There may be a way to use both creases, provided you can tell a turning edge from the mark of the lock.{/n}
{n}Targona has numbered the corners so you can report what you tried. The smallest number has nearly disappeared into a fold. Beside it she has written an indignant replacement, twice the size of the others.{/n}
{n}You test a corner without pressing it flat. The inner lines are faint beneath the new ink. You could study them closely, or stop treating the drawing as a puzzle with one hidden answer and simply go through the wall.{/n}''',
      c("[Perception] Follow the faint inner line and find a fold that opens outward.", check=dict(Skill="SkillPerception", DC=25, Success="found", Failure="creased", CommanderOnly=True)),
      c("Make a new opening instead of solving the old arrangement.", "cut")),
    n("found", "Narrator", '''{n}The faint line ends just short of the apparent corner. You fold there, reverse the inner flap, and find it: a small door that opens outward, into the corridor, without carrying the room with it.{/n}
{n}You mark the sequence in Targona's numbering. Three arrows mark the folds; a fourth points along the corridor.{/n}
"It opens outward, on paper at least," {n}you write.{/n} "It took three folds, and the first two made it worse; I've marked those as well. Whether her real door did, only she knows, and I'd rather not ask her."
{n}You return the worked copy with a blank one beside it. Before sealing the packet you open the little door again. It catches on your thumbnail. You add an arrow where she should lift it.{/n}''', c("Return the construction and its instructions.", flags=("targona.fold_found",))),
    n("creased", "Narrator", '''{n}The inner line disappears beneath your first crease. When you fold the flap back, the door catches and tears at its top corner. Another attempt only enlarges the tear.{/n}
{n}You put the damaged copy beside the untouched one. For a moment it is tempting to begin again and send only the better result. You leave the tear visible and take up your pen.{/n}
"I couldn't make the two hinges agree," {n}you write.{/n} "I tore the paper trying. The door opens now, but only because its corner is ripped, and I won't pretend that was the plan."
{n}You set down your attempts in order and leave the spare copy blank.{/n}
"Your account will have to make do with a torn map and an honest report. I've given worse to Irabeth and lived."
{n}Both copies go into the packet. The failed one remains on top.{/n}''', c("Return the failed attempt honestly.", flags=("targona.fold_failed",))),
    n("cut", "Narrator", '''{n}You cut three sides of a rectangle in the clear part of the copied wall. The fourth becomes a hinge. You trim a narrow strip from the flap's free edge so it opens without catching. When you lift it, the drawing opens onto the surface of your desk.{/n}
{n}You keep the discarded strip and write down exactly what you did.{/n}
"I didn't find her door. I made one. The old hinges are still visible beside it."
{n}At the bottom you add a practical improvement: the new door wants a small handle so it can be opened without tearing its corner.{/n}
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
"The third time I did them in the wrong order and shut the little lock inside the room. I kept that one too; it is the only version of that room I have ever enjoyed.
"I still do not know how her door was truly made. But I know how to make one that opens, and I gave thanks for that at dawn prayers."
{n}The letter moves on to the collector. Her hand is firmer here than it was round the copied hinges.{/n}''', c("Read about her account.", "account")),
    n("failed", "Narrator", '''"Thank you for sending the torn one on top. Irabeth was right to let you live.
"I tried the spare. My door caught too. So I cut a new hinge at the torn corner, which would be a poor repair on any door that has to keep out the weather. For a map of a ruin, it serves.
"I have kept both copies, yours and mine, with a note in my hand saying neither of us knows which way the door swung. I have left that part of the account blank. Anyone who reads it will know what I could not remember.
"I tried your torn copy again before dawn, and thanked Iomedae for smaller mercies."
{n}The next sheet bears the collector's name and the date of her reply.{/n}''', c("Read about her account.", "account")),
    n("cut", "Narrator", '''"I laughed when I saw the hole. Then I opened it again, to show the chaplain why.
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


s("the_unscheduled_door", "Merovan of the host", [
    n("start", "Narrator", '''{n}The tale Targona sends is short, and written in a hand meant to be read aloud by lamplight. She has given its soldier a name that is not her own.{/n}
"I have called her Merovan. A sergeant from Kenabres says he knew a Merovan, and that she would have liked this. I chose to believe him."
{n}Merovan, a sergeant of the host, wakes in a room with a chair, a closed door, and a parcel tied with a thoroughly unreasonable quantity of string. Merovan sets the parcel on the chair and reaches for the door.{/n}
"I read it to the fever ward last night," {n}Targona writes.{/n} "They argued about the string for an hour. Nobody died before morning. I am not saying the two are connected. I am not saying they are not."
{n}You read the ending your suggestion gave her.{/n}''',
      c("Read Merovan's departure.", "leaving", requires=("targona.story_leaving",)),
      c("Read Merovan's invitation.", "receiving", requires=("targona.story_receiving",))),
    n("leaving", "Narrator", '''{n}Merovan takes the chair to the door, breaks the lock with its leg, and walks out into a street she does not recognize. A watchman asks whether she is expected somewhere. She says that she is, at the nearest muster, and asks him the way.{/n}
{n}She carries the parcel with her, because it is hers. On a bench by the muster gate she unpicks the knots. Inside is a cup she has never liked. She trades it at the first stall for a chipped blue one and spends the difference on something sweet enough to make the vendor warn her.{/n}
"The men wanted her to kill the demon on the way out," {n}Targona writes.{/n} "I told them the demon was not in the story, because the demon does not deserve a line. They accepted this. One of them cried, which he has asked me not to tell you."
{n}The last line says only that Merovan reaches the muster before roll call. A little ink has spread beneath the word 'reaches'.{/n}''', c("Consider what you might add.", "method")),
    n("receiving", "Narrator", '''{n}Merovan does not leave. She sets the chair against the door, draws her sword, and holds the room. Then she opens the parcel and finds a cup she has never liked, and puts it on the table anyway, because a garrison should be able to offer a guest something.{/n}
{n}She chalks a notice on the door: KNOCK. THE CUP IS NOT FOR LENDING.{/n}
{n}The first to knock is a crusader who has lost his company and wants to borrow a spoon. Merovan nearly runs him through, then decides an honest request deserves an honest answer. She lends him the spoon, refuses him the cup, and asks whether he knows anywhere selling better ones. He directs her to a stall at the corner. She chooses a chipped blue cup, leaves the old one for guests, and makes him swear by Iomedae to return her spoon.{/n}
"The ward liked her," {n}Targona writes.{/n} "She is less gracious than I meant her to be. The man with the spoon is a corporal from the third cot, and he has demanded to be in the next one."
{n}Merovan props the door open with the chair.{/n}''', c("Consider what you might add.", "method")),
    n("method", "Narrator", '''{n}Targona has left the other side of the sheet blank for your part. She has written one condition at its top, in a soldier's capitals: THE MEN HAVE VOTED. SHE DOES NOT DIE.{/n}
{n}You can add another street to the tale, a reply from the corporal with the spoon, or simply tell her which line made the ward laugh. You copy out her ending first. By the time you reach the parcel, you have developed a strong dislike of its string.{/n}''',
      c("[Trickster] Give the copied page a folded ending that refuses to stay last.", "trick", requires=("trickster",)),
      c("Write a second ordinary scene, leaving her first ending intact.", "ordinary")),
    n("trick", "Narrator", '''{n}You copy the little door onto both faces of a spare sheet, measuring each from the same corner, and fold the sheet into a narrow concertina. THE END goes on the last panel. A corridor goes on the panel tucked beneath it.{/n}
{n}Open the door and the corridor unfolds past the supposed ending. Turn the strip over and the second door opens onto the same folds. A crease runs through both drawings of the door.{/n}
{n}Your first attempt tears at the hinge. You keep it beside the sound one and copy the folding instructions onto the back, step by step, the way you would write orders for a man who has to do it in the dark.{/n}
"There is another corridor under THE END," {n}you write.{/n} "Lift the hinge and unfold it."
{n}You enclose both attempts with her unchanged original. The torn one gets a warning in the margin: "Do not pull this one too hard."{/n}''', c("Send the altered copy alongside the unchanged original.", flags=("targona.extra_ending",))),
    n("ordinary", "Narrator", '''{n}You leave Merovan's ending where Targona put it. On the next page you give her a soldier's inconvenience: the chipped blue cup will not fit in a pack, and a sergeant of the host cannot be seen carrying crockery through the muster.{/n}
{n}Merovan tries to pack the cup between her spare shirt and her whetstone. Merovan makes an unnecessarily elaborate plan involving her helmet, abandons it, and carries the cup in her hand through the whole muster with her chin up. You sketch the helmet plan and discover halfway through that you cannot make it work either.{/n}
"The third cot can have his spoon back in the next one," {n}you add.{/n} "Tell him I said so."
{n}You return the two scenes together, including the failed sketch.{/n}''', c("Send the second scene with her original.", flags=("targona.ordinary_ending",))),
], "targona.an_unpromised_future")


s("what_she_keeps", "A letter she wanted to write", [
    n("start", "Narrator", '''{n}Targona's latest letter is less carefully arranged than the others. The first paragraph has been moved with an arrow, a second thought has been squeezed above the date, and a faint ring marks where a cup stood too near the edge.{/n}
"I began this before I knew what it was about. I do not recommend it."
{n}Her answer to your page occupies the first sheet.{/n}''',
      c("Read her response to the Trickster page.", "trick", requires=("targona.extra_ending",)),
      c("Read her response to the ordinary continuation.", "ordinary", requires=("targona.ordinary_ending",))),
    n("trick", "Narrator", '''"I opened your door and found your corridor, and followed your instructions, and my first corridor came out upside down. I have kept it. I kept the torn one too, and did not pull it too hard.
"For a moment I wished there had been such a fold in her laboratory. There was not. I will not draw one into my account; my comrades must not look for a passage that was never there.
"But I can put one in Merovan's story. The corporal from the third cot insists she should take the corridor, and carry her cup carefully. He has tried your torn hinge and made it worse, and is very proud of himself.
"Send me another street when you have time. I have promised him no more than that."
{n}She has drawn Merovan opening the door from its unexpected side. The figure carries a cup.{/n}''', c("Read the next page.", "voices")),
    n("ordinary", "Narrator", '''"The ward laughed at the helmet plan until the chaplain came to see whether we were all dying. Then I improved the plan in the margin, which I believe was exactly the trap you laid for me.
"I gave Merovan a companion for the next street: the corporal from the third cot, who talks too much about his mother's pottery. She discovers she does not mind. He has his spoon back. The ward voted on that as well.
"I still wake with the old room in my thoughts sometimes. I have no triumphant ending to attach to that sentence. But there are other things on the table now. A cup I like, a tale the men ask for, and letters I am glad to receive.
"I did not expect a cup to do so much. I suppose that is what cups are for."
{n}She has enclosed the beginning of the new street, stopping before the corporal can explain a second glaze.{/n}''', c("Read the next page.", "voices")),
    n("voices", "Narrator", '''{n}The next sheet is folded separately from the tale.{/n}''',
      c("Read the two notes inside.", "two", requires=("targona.ran_trickster",)),
      c("Read the two notes inside.", "two", requires=("targona.ran_aeon",), forbids=("targona.ran_trickster",)),
      c("Read Targona's private note.", "personal", forbids=("targona.ran_trickster", "targona.ran_aeon"))),
    n("two", "Anograt", '''"Silver says I may write this part myself. An extraordinary concession, considering that I have been writing in the margins from the beginning.
"You sent your page back. Good. When we disagree about a story you get two letters, not one sensible compromise. Nobody has ever made a sensible compromise with a wing.
"My opinion is that Merovan should keep the bad cup and use it to hold the collector's rejected adjectives. Eventually she could sell them. There is clearly a market." {n}Targona's reply sits immediately below.{/n}
"I prefer the chipped blue cup. I also prefer Anograt saying what she thinks under her own name, rather than in my margins pretending to be me.
"Keep addressing the letters to me. Add a page for her if you wish. She will read over my shoulder either way; I would rather she did it openly. Yesterday she rewrote my last sentence while I was fetching ink. At least now I know which words are hers."''', c("Read Targona's final lines.", "personal")),
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


# R4 D11-D13: authored citadel repair/watch; ordinary unpaid dispatch and repair duty.
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
{n}In the citadel's east wall there is a postern the demons bricked up and warded while they held Drezen. The engineers have chalked it unsafe and left it alone. Beyond it a goat track runs down to the eastern road below the gate. The engineers will brace the opening and inspect the stonework once the ward is dead. The watch captain agrees to station a sentry inside, with orders to admit Targona and keep the door barred behind her. She can reach the courtyard without crossing the crowded gate.{/n}
{n}The ward has to be truly dead first. If it is not, there is no invitation.{/n}''',
      c("[Knowledge (Arcana)] Unpick the demons' ward and test the postern before inviting her.", check=dict(Skill="SkillKnowledgeArcana", DC=30, Success="steady", Failure="falter", CommanderOnly=True)),
      c("Do not risk a passage. Send an ordinary invitation by the known courier road.", "road")),
    n("courier_setup", "Narrator", '''{n}The ordinary page hid no door, and you do not pretend it did. What you have is a named wayhouse, a courier who runs the eastern road twice a week, and a woman who wrote that she wants to see you.{/n}
{n}The dispatch clerk reaches for the last letter just as you set yours down. Your invitation slips neatly into the returns bag before he ties it shut. The courier takes it with the requisitions on his usual round; you have gained a place in this packet, not a faster journey. By the time he reaches the wayhouse, her evening duty has begun.{/n}
{n}She writes back in her own hand, on the back of yours. She will walk the public road to Drezen, if you still want her to come.{/n}''',
      c("Send the courier back with your invitation.", "road"),
      c("Do not send it. Keep the correspondence open.", "declined")),
    n("ordinary", "Narrator", '''{n}You do not make a magical route. You write that the invitation will wait with the courier, and that the road from her wayhouse is an ordinary one.{/n}
{n}She replies that she will not come this week: there is fever on the eastern road, and eleven men in the wayhouse who need an angel more than you do. You answer with an ordinary account of your day, including one detail too small for any dispatch.{/n}
{n}She sends back one from hers. The wayhouse cat has taken the chaplain's chair, and nobody in the house has the courage to move it.{/n}''',
      c("Send your answer and leave a later invitation to her.", flags=("targona.visit_correspondence",))),
    n("declined", "Narrator", '''{n}You send no key and no courier. You write that you want to see her, and that you would rather see her on a night when the road and the war both allow it.{/n}
{n}Targona's answer is warm, if brief.{/n}
"You took me at my word. Few people do; they think an angel's no is only a yes that has not been prayed over long enough. I still want you. Keep writing to me, and one evening I will write back and name the night."
{n}You answer with the smallest news you have, and ask for hers.{/n}''',
      c("Write back.", flags=("targona.visit_correspondence",))),
    n("steady", "Narrator", '''{n}It takes two nights. The last thread of the ward parts with a smell like singed hair. You push an empty dispatch pouch through the gap from outside and from within, at dusk and again at midnight, and nothing answers it. The engineers brace the opening, check the lintel and scrape away their warning. The citadel locksmith fits a lock from the repair stores, with two keys. The sentry takes one and bars the door from within.{/n}
{n}The courier carries Targona a written account of the work, the way the goat track runs, and one of the keys. She reads every line of it. Her reply is one sentence: "I will inspect it myself."{/n}
{n}She comes up the track after dark. The sentry checks her name, admits her and drops the bar behind her. She examines the postern slowly, frame and hinges and the scorched stones where the ward was, the way a healer examines a wound someone else has dressed, and then puts the key in her own pocket.{/n}
"It is well made," {n}she says.{/n} "For a trick."''',
      c("Walk the wall with her.", "walk"),
      c("Tell her the wounded on the eastern road will want her at first light.", "close_passage")),
    n("falter", "Narrator", '''{n}The ward does not die. When you push the empty dispatch pouch through the gap, it comes back scorched, its seams turned inside out. You have the gap bricked up again before the courier ever sees it.{/n}
{n}You send an ordinary letter instead, and tell her exactly what failed. Targona answers by the same courier.{/n}
"Thank you for not sending me the key. I would have used it, and you know that, which is why I am glad you did not.
"Write to me tonight instead. Tell me something from your day too small for a dispatch. When there is a road worth trusting, I will walk it."''',
      c("Answer her and keep the correspondence open.", flags=("targona.visit_correspondence",))),
    n("road", "Narrator", '''{n}The courier carries your invitation to the wayhouse. Targona comes by the public eastern road, on foot, stopping twice on the way at the dressing station by the ford because there were men there.{/n}
{n}No spell moves her and no unstable gate closes behind her. She reaches the Drezen courtyard before the appointed hour and waits until you arrive.{/n}
"I walked," {n}she says.{/n} "It was a long road, and nobody on it looked at the wing. I liked that. Walk beside me the rest of the way."''',
      c("Walk the wall with her.", "walk"),
      c("Tell her the wounded on the eastern road will want her at first light.", "close_road")),
    n("walk", "Narrator", '''{n}You take the path around the courtyard and up onto the wall, where the city noise thins and the evening air reaches the open edge of her wing.{/n}
{n}You ask if the wing hurts today. Sometimes, she says. Not now. She studies your face, then smiles.{/n}
"I tried to finish my evening prayers before I came. I kept thinking of you."
"Everyone looks at me as a sign," {n}she says.{/n} "Heaven's healers look at the wing and see Areelu's work. The soldiers look at the other one and see a promise. In that laboratory I was proof of something." {n}She stops walking.{/n} "You look at me the way you did before the last letter, before the kiss I wrote to you about and the one I did not. I have missed being looked at like that more than I will ever admit to a chaplain. Three days on the eastern road, with eleven men to change dressings for, and every one of them I thought: the Commander would be doing this badly, and would ask me to show how, and would not listen."
{n}She turns to face you and leaves her fingers in your sleeve.{/n}
"Commander. You have looked at me like that the whole length of the wall. Are you going to do anything about it?"''',
      c("Ask her again, and wait for her answer.", "kiss"),
      c("Tell her you would rather continue the walk.", "continue")),
    n("close_passage", "Narrator", '''{n}She looks east, where the watchfires are, and then locks the postern herself and tries the bolt twice. The sentry takes his place beside it.{/n}
"You are right, and I hate it. If I stay, I will stay too long, and tomorrow there are wounded on the eastern road who deserve an angel who slept." {n}She smiles, a little ruefully, and offers you her arm.{/n} "Walk me to the gate, at least. I will go out by it like an honest woman; I will not use your trick twice in one night."''',
      c("Walk with her to the road and say goodnight.", "departed")),
    n("close_road", "Narrator", '''{n}She looks east, where the watchfires are.{/n}
"You are right, and I hate it. If I stay, I will stay too long, and tomorrow there are wounded on the eastern road who deserve an angel who slept." {n}She smiles, a little ruefully, and offers you her arm.{/n} "Walk me to the gate, then. Slowly."''',
      c("Walk with her to the road and say goodnight.", "departed")),
    n("departed", "Narrator", '''{n}You walk her as far as the eastern gate. The sentries there have been told nothing, and they look at the wing, and then at you, and then very hard at the road.{/n}
{n}She squeezes your hand before letting go.{/n}
"I am glad I came. Do not ask me for the next evening here, at a gate, in front of sentries. Ask me in a letter, where I can say yes slowly."
{n}Two days later the courier brings a note. She reached the wayhouse before midnight, the cat has kept the chaplain's chair, and she prayed for you at compline, which she says you are not to make anything of.{/n}''',
      c("Reply with affection and leave the next invitation open.", flags=("targona.visit_pause",))),
    n("kiss", "Narrator", '''{n}Targona steps into your arms and kisses you, hard and certain. Your back meets the cold stone of the wall; she presses close enough for you to feel her trembling.{/n}
{n}Her thumb rests beneath your jaw. When she lets you breathe, she keeps her brow against yours and her other hand open against your chest.{/n}
"I have missed that," {n}she says, smiling against your mouth.{/n} "More than I could put in a letter."
{n}Your hand brushes the edge of her wing. She flinches, catches your wrist and draws it to her waist instead.{/n}
"Here." {n}She presses closer. Her other palm rests on your chest, over the pounding heart.{/n} "And stay there. I have had enough people looking at the wing tonight."
{n}She kisses you once more, slower, and then looks past you at the lit windows of the barracks, and at the dark stair beside them, and back at you.{/n}
"Well. Talk, or kisses, or finding out how many buckles there are on this armour. Choose, Commander. I will tell you if you chose wrong."''',
      c("Choose talk, and another kiss.", flags=("targona.visit_tender",)),
      c("Find out how many buckles there are.", "buckles", flags=("targona.visit_desire",)),
      c("Tell her that kiss was enough for one night.", flags=("targona.visit_pause",))),
    n("buckles", "Narrator", '''{n}She counts them aloud on the dark stair, one at each step, and loses count at six because you have stopped on the step below her and she is, for once, the taller.{/n}
{n}In your rooms she does not light the lamp. She sets her back against the door and has your coat off your shoulders before the latch has finished falling, and then the buckles, quick and certain, a healer's hands that have unfastened a thousand wounded men's harness and never once with this much hurry.{/n}
"Eleven," {n}she says against your mouth.{/n} "Eleven, Commander. Who arms you? I will have words with him."
{n}She draws her plain wayhouse habit over her head and lets it fall, and a wing opens behind her in the dark and brushes the wall. She pushes you back onto the bed and follows you down, her knees either side of you, her hair falling round both your faces, and takes your hands and puts them where she wants them.{/n}
{n}Her mouth leaves yours only to go down your throat, your collarbone, the middle of your chest, and the wing folds close around the pair of you without touching anything it should not. Her hands are unembarrassed now. She finds your belt in the dark, laughs low when the last buckle fights her, wins, and strips the rest of you with a soldier's economy. Her breasts are warm against your ribs, her skin tastes of salt and road, and when your mouth closes on her she gasps your name and arches into it. It is nothing like the voice that tells wounded men to be brave.{/n}
"Do not be careful with me. I have been careful with other people's bodies for weeks." {n}She settles over your hips, thighs open around you, wet already against your skin, puts your hand back on her hip, and reaches down between you to guide the two of you together.{/n}
''' + EXPLICIT_PARAGRAPHS["targona.the_open_threshold.explicit.1"] + '''
{n}Long before light she is dressing again by the window. The wounded on the eastern road will want her at the first bell, she says, and she will not let them want her in vain on your account. She kisses you once more at the door, hard, and does not say when.{/n}''',
      c("Let her go back to her road.")),
    n("continue", "Narrator", '''{n}You tell her that a walk is enough. Targona leaves her fingers in your sleeve and chooses the battlements, where the city opens below and the watchfires on the eastern road show where the wounded are coming in.{/n}
"There," {n}she says, pointing.{/n} "That fire is the ford. They brought eleven across it this morning. I counted." {n}She is quiet for a moment.{/n} "I have spent my whole life being useful. I am not sure I know how to be idle beside someone."
"Walk until I am tired. Then eat something sweet enough to be imprudent. Then decide whether I want another kiss. That is my plan, and I will not be argued out of it."
{n}She tells you which of the city lights she can see from the terrace, and which she has mistaken for stars, and which is the lamp in the infirmary where a boy with a fever is waiting for morning.{/n}''',
      c("End the evening with affection and leave the next choice open.", flags=("targona.visit_tender",)),
      c("Ask if she would like that second kiss now.", "kiss")),
], "targona.what_she_keeps", delay=0, requires=("targona.correspondence_romanced",), forbids=(MET,))


s("the_key_remains_hers", "The key remains hers", [
    n("start", "Narrator", '''{n}Targona's next letter is sealed with a thumbprint of candle wax because she has no seal of her own any more.{/n}''',
      c("Read her answer after the intimate evening.", "desire", requires=("targona.visit_desire",), forbids=(MET,)),
      c("Read her answer after the tender evening.", "tender", requires=("targona.visit_tender",), forbids=(MET,)),
      c("Read her answer after you chose to pause.", "pause", requires=("targona.visit_pause",), forbids=(MET,)),
      c("Read her answer to your letter.", "correspondence", requires=("targona.visit_correspondence",), forbids=(MET,)),
      c("Read her letter from the ward.", "start_ward", requires=(MET,))),
    n("desire", "Narrator", '''{n}A small brass key is tied to the page with red thread: the key to the wayhouse's side gate, which the porter locks at compline.{/n}
"I had it copied in the village, then told the porter. He wanted to know who would be using it. I told him your name. Now he sweeps the side path whenever a dispatch arrives.
"I have been thinking about your stair. I want you. I want the warmth of you against me, and the sound you make when you stop trying to be clever. I have written that sentence three times and burned two of them, and I am sending the third before I lose my nerve.
"Next time I will come on a night when the road is quiet, and I will not be dressing by the window before light."
{n}She has left the last line blank, as if it belongs to the answer.{/n}''',
      c("Write back that you want her, and that the key had better not rust.", flags=("targona.key_reciprocal",)),
      c("Write back that you want to see her, whatever the night turns into.", flags=("targona.key_unpressured",))),
    n("tender", "Narrator", '''{n}A small brass key is folded into the letter. On its tag, in Targona's unmistakable hand, is written: ONLY IF I ASK.{/n}
"I have not stopped thinking about the evening. I want another one. I want to arrive late, with my sleeves still wet from the basins, and kiss you before either of us says anything clever. After that I do not know. I find I like not knowing."
{n}The line beneath her note is left open for an answer.{/n}''',
      c("Reply that you want her, and that you will be waiting.", flags=("targona.key_reciprocal",)),
      c("Reply that you want her company, and leave the rest for another day.", flags=("targona.key_unpressured",))),
    n("pause", "Narrator", '''{n}The letter contains no key. Targona writes that she was pleased you let the evening end without asking her to turn it into a promise.{/n}
"I still want you. I was glad you did not hurry me; the wayhouse had fever in it that week, and I would have come to you smelling of vinegar and gone back before the bell. I would like another evening. Come when the wounded let you."
{n}She has added a small sketch of the courtyard, with the way in and out marked in equal-sized arrows.{/n}''',
      c("Tell her you want another evening, whenever the wounded can spare her.", flags=("targona.key_unpressured",)),
      c("Tell her you want to kiss her again when she asks.", flags=("targona.key_reciprocal",))),
    n("correspondence", "Narrator", '''{n}Targona's letter contains a short account of an uneventful afternoon and a question about a story you once sent her.{/n}
"We did not meet that evening. I am not sorry. I think I needed one more letter first. Tell me the ending of the story you started last time; you stopped just when the bridge was about to fall, and I have been worrying about the bridge."
{n}She sends a recipe for a sweet she has recently learned to make. The measurements are exact. The instruction to wait before adding the last ingredient has been underlined twice.{/n}''',
      c("Reply with an ordinary detail and keep the conversation open.", flags=("targona.key_unpressured",))),
    # Authored: a pending wand-night arrival can move her to the existing Drezen ward after the wayhouse visit.
    n("start_ward", "Narrator", '''{n}A runner has brought it from the infirmary behind Wilcer's stores. The wax is still soft. Targona has crossed out the wayhouse address and written DREZEN beneath it.{/n}''',
      c("Read her answer after the intimate evening.", "desire_ward", requires=("targona.visit_desire",)),
      c("Read her answer after the tender evening.", "tender_ward", requires=("targona.visit_tender",)),
      c("Read her answer after you chose to pause.", "pause_ward", requires=("targona.visit_pause",)),
      c("Read her answer to your letter.", "correspondence_ward", requires=("targona.visit_correspondence",))),
    n("desire_ward", "Narrator", '''{n}A small brass key is tied to the page with red thread. Beneath it she has written: THE DRYING LOFT, ABOVE THE WARD.{/n}
"The wayhouse key would do you little good now. Wilcer had a lock fitted to the loft hatch. I had this copy made in the lower town, and confessed it the same evening. I would do it again.
"I have been thinking about your stair. I want you. I want the warmth of you against me, and the sound you make when you stop trying to be clever. I have written that sentence three times and burned two of them, and I am sending the third before I lose my nerve.
"I remember dressing by your window before light, with the eastern road still ahead of me. Now I can see your window from the cots. Come up when the chaplain takes the rows. I want to wake beside you and have only a ladder to climb down."
{n}She has left the last line blank.{/n}''',
      c("Write back that you want her, and that the key had better not rust.", flags=("targona.key_reciprocal",)),
      c("Write back that you want to see her, whatever the night turns into.", flags=("targona.key_unpressured",))),
    n("tender_ward", "Narrator", '''{n}A small brass key is folded into the letter, with a tag naming the drying loft above Drezen's ward. Beneath it, in Targona's hand, is written: ONLY IF I ASK.{/n}
"I have not stopped thinking about our evening on the wall. I want another one. This time you can find me behind Wilcer's stores, with my sleeves still wet from the basins. I want to kiss you before either of us says anything clever.
"When the chaplain takes the rows, come up to the loft with me. After that I do not know. I find I like not knowing."
{n}The line beneath her note is left open.{/n}''',
      c("Reply that you want her, and that you will be waiting.", flags=("targona.key_reciprocal",)),
      c("Reply that you want her company, and leave the rest for another day.", flags=("targona.key_unpressured",))),
    n("pause_ward", "Narrator", '''{n}The letter contains no key. Targona writes that she was pleased you let the wayhouse evening end without asking her to turn it into a promise.{/n}
"I still want you. I was glad you did not hurry me. There was fever at the wayhouse that week, and I would have gone back before the bell. Now the fever is here in Drezen, and so am I. Come to the cots when you can. When the chaplain takes my place, I would like another walk with you."
{n}She has sketched the way from Wilcer's stores to the courtyard.{/n}''',
      c("Tell her you want another evening, whenever the wounded can spare her.", flags=("targona.key_unpressured",)),
      c("Tell her you want to kiss her again when she asks.", flags=("targona.key_reciprocal",))),
    n("correspondence_ward", "Narrator", '''{n}Targona's letter describes an afternoon in Drezen's infirmary. She ran out of clean linen before she ran out of patients.{/n}
"We did not meet that evening. I am not sorry. I think I needed one more letter first. You can bring the next one to the cots yourself, now. Tell me the ending of the story you started last time; you stopped just when the bridge was about to fall, and I have been worrying about the bridge."
{n}She sends a recipe for a sweet she learned at the wayhouse. She has asked the infirmary cook to try it, if he can find the honey.{/n}''',
      c("Reply with an ordinary detail and keep the conversation open.", flags=("targona.key_unpressured",))),
], "targona.the_open_threshold", requires=("targona.correspondence_romanced",))

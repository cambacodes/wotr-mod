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
BLOCKED = ("targona.closed", "targona.dead_lab", "targona.dead_lair", "targona.condemned", "swarm", "demon", "lich", "devil",
           "legend", "dragon", "targona.ran_lich", "targona.ran_demon", "targona.ran_devil", "targona.ran_legend", "targona.ran_dragon")


def s(id, title, nodes, previous=None, delay=24, requires=()):
    for page in nodes:
        page["Portrait"] = "TargonaCorrespondence"
    SCENES.append(scene("targona." + id, title, "Targona", 5, "Read Targona's correspondence", nodes,
                        requires=("targona.free", "targona.ran_treatment_completed", "targona.ran_final_seen") + ((previous,) if previous else ()) + tuple(requires),
                        forbids=BLOCKED, delay=delay, optional=True, Relationship="targona",
                        Remote=True, ManualOnly=True, Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[5], RequiresAny=ALLOWED))


s("unasked_question", "A page without a diagnosis", [
    n("start", "Narrator", '''{n}The packet waiting among your personal correspondence holds a letter and a folded drawing. Targona has written your name on the outside, not your title. For once she does not ask to be treated for anything.{/n}
"I began this letter three times with 'I am well', and I struck it out three times. My sisters in Heaven taught me to report a wound the way a sentry reports the wall: plainly, and first. So, plainly. I dream of the laboratory.
"I have been drawing one of its rooms. I remember the door better than anything in it, and still, every time I set it down, I put the lock on the outside, where Areelu kept it. I know I am free. I give thanks for it at morning prayers. Then at night I sit down with a pen and lock myself in again.
"Will you look at it? You walked out of that place as well. The healers here look at my drawing and tell me what an angel ought to be able to bear. I would rather hear what a soldier sees."''',
      c("Unfold the drawing.", "drawing"), c("Put the drawing aside until you can give it an unhurried hour.", abort=True)),
    n("drawing", "Narrator", '''{n}A square room. A narrow table with straps at the corners. A door whose hinges she has drawn twice, once on each side, and a neat arrow pointing out through it. The lock lies across the arrow like a bar across a gate.{/n}
Beneath it she has written, in a smaller hand:
"I am not asking you to find the room. It lies under the ruin, and I thank Iomedae for every stone on top of it. Some of the distances may be wrong. I spent very little time looking at it from above."
The last sentence is underlined once, as though she has decided you may laugh at that much.
"There are hours I cannot account for, and I will not invent them to make a better story. But Areelu still keeps the only clear part of this one. She knew what she wanted, and I was the table she worked on. I want some of it back.
"Tell me the first thing you see. Do not stop to decide what would comfort me."''',
      c('Write: "You drew the way out before you drew the bar across it."', "exit"),
      c('Write: "You drew the hinges twice. You didn\'t trust your own memory."', "hinges")),
    n("exit", "Narrator", '''{n}You mark the place where the arrow begins. Its first stroke is darker than the line laid over it.{/n}
"You drew the way out first," you write. "The bar came afterwards, in a thinner line, as if you had to go back and remember to be afraid. I can't tell you which is the true room. I can tell you which one you put down first."
You nearly add that it will not trouble her now. You cross that out. She would know it for a lie before she reached the full stop.
"Send me a copy and I'll mark that. Keep the first one clean. It's yours. I don't get to draw on it."
{n}There is room left beneath the question for something that is not about the room at all.{/n}''',
      c("Continue the letter.", "personal")),
    n("hinges", "Narrator", '''{n}You copy both sets of hinges onto a scrap. One door swings in, into the room. The other swings out, flat against the corridor wall.{/n}
"You left both," you write. "You could have rubbed one out and sent me a clean drawing. You sent me the one where you weren't sure. I trust that more than any map a scout ever handed me with a straight face."
"Let me work on a copy. I won't pretend to know what the room looked like. I'd like to see what you can make it do now."
{n}You set the scrap beside the letter and leave space beneath it.{/n}''',
      c("Continue the letter.", "personal")),
    n("personal", "Narrator", '''{n}The folded room is small enough to cover with one hand. You leave it open while you finish.{/n}''',
      c('Write: "I miss you. Send me the hard letters too. I\'d rather have those than none."', "romance", requires=("targona.ran_romance",)),
      c('Write: "You don\'t have to make it easy to read. I\'ll read it anyway."', "friend")),
    n("romance", "Narrator", '''{n}You write down the way she looks when she has decided to say a thing before she has found the right words for it, and how you once leaned in to hear her though her voice was perfectly clear.{/n}
"I want another evening with you. An ordinary one, with nothing in it that needs healing. And I want the rest of it too, the dreams and the room. You don't have to pay for one with the other."
The last line comes out less polished.
"I've cleared a corner of my desk for whatever you send next. The quartermaster's reports are sulking about it."
{n}You seal the letter and keep the drawing out of the official dispatches.{/n}''', c("Send your reply with the next personal correspondence.", flags=("targona.correspondence_opened",))),
    n("friend", "Narrator", '''{n}You write that you want to hear what she notices now, the small things that would never survive into a report. You start a list of examples, and cross it out before it turns into orders.{/n}
"If you tire of this, say so and we'll quarrel about something else. I'd rather have an awkward friend than a polite one."
You leave a clean strip at the bottom of the page and label it ROOM FOR AN UNRELATED COMPLAINT.
{n}Her drawing goes back with the letter, uncertain hinges and first arrow intact.{/n}''', c("Send your reply with the next personal correspondence.", flags=("targona.correspondence_opened",))),
], delay=0)


s("second_margin", "Who holds the pencil", [
    n("start", "Narrator", '''{n}Targona sends back your letter with a new sheet. She has filled the strip for complaints, whether or not you meant it seriously.{/n}
"The brother who packed these pages used enough string to truss a sheep. I spent longer freeing the paper than drawing on it. I offer this as my complaint, and I confess I enjoyed writing it.
"Yes, make a copy. Keep the first as it is. I do not want to mend it until I have forgotten why I sent it.
"I looked at the bar again. I remember drawing it. I was angry, because the door looked too easy to open, and it was not easy. It was never easy. Forgive me if that sounds foolish. I noticed it before you did, and I would like the credit."
{n}Below this, her hand grows smaller.{/n}
"A man is gathering crusaders' accounts for a book. He has asked me for the laboratory. Something short, he says, and uplifting. I said yes before I had thought, because he asked kindly and I was made to be useful. Now I cannot get past his word. Uplifting."''',
      c("Read the additional note.", "anograt", requires=("targona.ran_trickster",)),
      c("Read the additional note.", "anograt", requires=("targona.ran_aeon",), forbids=("targona.ran_trickster",)),
      c("Read Targona's proposed account.", "account", forbids=("targona.ran_trickster", "targona.ran_aeon"))),
    n("anograt", "Anograt", '''{n}A different hand has occupied most of the margin.{/n}
"Silver asked me to help. I offered to write the account from the lock's point of view. It would be a short career followed by a deserved retirement. She smiled, so the suggestion was not entirely wasted.
"We have been sharing a table. Silver gets the chair with the good cushion; I get the edge of the paper she hasn't written on yet. You can see how much she values my contribution.
"She keeps crossing out the parts where she is angry. I keep writing them back in the margin. We are at eleven each.
"My proposal is that we give the collector the most uplifting account imaginable: a door rising off its hinges and striking the person who built it. Silver says that is not what happened. I said the word was uplifting, not accurate."
{n}Targona has written beneath this: "This is why I still need your answer."{/n}''', c("Read Targona's proposed account.", "account")),
    n("account", "Narrator", '''{n}Her draft begins with the people who lived near her prison because her light was there. She does not name them. She does not pretend to know what became of them. Then the sentences go cold, the way a sermon goes cold when the preacher has stopped believing it.{/n}
"The captive angel remained a source of protection. Her suffering was therefore not without purpose."
The lines are struck through so hard that the nib has torn the sheet.
"I wrote that," Targona says underneath. "No collector put it in my mouth. I was trying to give the reader something to hold, and I found I had written him a reason to leave me in the barrier.
"Men lived because I was there. I thank Iomedae for every one of them. I would have sheltered them awake, with a sword in my hand, if anyone had let me. I cannot make the second thing small enough to fit under the first, and I will not print a sentence that pretends I can."
The page ends with a question. Should she write it for him now, or tell him no?''',
      c('Tell her to write it short, in her own name, with the anger left in.', "publish"),
      c('Tell her to refuse him plainly and keep the pages for herself.', "private")),
    n("publish", "Narrator", '''{n}You write a first line for her to throw away if she likes: "Men lived because I was there. That is not why I was there."{/n}
The rest of your answer is short. She need not account for every hour or end on a lesson. She can write what she remembers, say plainly what others told her afterwards, and leave the lost hours lost.
You tell her the cost as well, because she would find it for herself anyway. Once it is printed men will quote it badly, and sooner or later somebody will write the tidy sentence back in for her.
"I'll read what you actually mean," you finish. "Send it if you want to. Don't put an amen at the end of it."''', c("Send your advice to publish.", flags=("targona.account_public",))),
    n("private", "Narrator", '''{n}You tell her to refuse him plainly, without promising him a later date to sweeten it.{/n}
"Write it if the writing helps. Write it to somebody you chose. He can get his uplifting paragraph from a man who wasn't there."
You tell her the price too. Other men will tell her story with less of her in it, and her silence won't make them truthful. You put that down before you offer to keep her pages, so she knows you are not selling her a door with no cost on it.
"If you change your mind, write and say so. Until then I'd like to read what you struck out. Nobody else will see it."
{n}You fold his proposed heading behind the reply without correcting it.{/n}''', c("Send your advice to refuse him.", flags=("targona.account_private",))),
], "targona.correspondence_opened")


s("the_folded_room", "An exit on the page", [
    n("start", "Narrator", '''{n}The next packet holds two copies of the room and a strip of paper broad enough to cut a small door from. She has kept the first drawing back.{/n}
"I did as we said about the collector. I will tell you what came of it when something has.
"Today I want to try your other idea. This copy you may spoil; keep the first one safe. I want a door on this page that I open myself.
"I have drawn the hinges both ways. Settle it however you like: by looking, by cleverness, or by arguing with the paper. I suspect you are qualified in at least two of those."
{n}The copied lines almost meet at one corner. Beneath them she has written: "Send it back even if it fails. Areelu only ever told me about the experiments that worked."{/n}''',
      c("Study the fold and the two sets of hinges.", "study"),
      c("Cut a simple paper door and leave the disputed hinges visible.", "cut")),
    n("study", "Narrator", '''{n}Folded along one line, the sheet traps the door beneath a flap. Folded along the other, it opens but carries part of the room outside. There may be a way to use both creases, provided you distinguish a turning edge from the mark of the lock.{/n}
Targona has numbered the corners so you can explain what you tried. The smallest number has nearly disappeared into a fold. Beside it she has written an indignant replacement, twice the size of the others.
You test a corner without pressing it flat. The inner lines are faint beneath the new ink. You could study them closely, or stop treating the drawing as a puzzle that must conceal one correct solution.''',
      c("[Perception] Follow the faint inner line and find a fold that opens outward.", check=dict(Skill="SkillPerception", DC=25, Success="found", Failure="creased", CommanderOnly=True)),
      c("Make a new opening instead of solving the old arrangement.", "cut")),
    n("found", "Narrator", '''{n}The faint line ends just short of the apparent corner. You fold there, reverse the inner flap, and discover a small door that opens without carrying the room through it. Its lock remains on the outside, where it can no longer hold the paper shut.{/n}
You mark the sequence in Targona's numbering. The construction is awkward rather than elegant; that seems a virtue in something she should be able to reproduce without taking your word for it.
"It took three folds," you write. "The first two made the obstruction worse. I have marked those as well."
You return the worked copy with a blank one beside it. Before sealing the packet, you open the little door again. It catches on your thumbnail. You add an arrow where she should lift it, and ask whether she finds the result worth the trouble.''', c("Return the construction and its instructions.", flags=("targona.fold_found",))),
    n("creased", "Narrator", '''{n}The inner line disappears beneath your first crease. When you fold the flap back, the door catches and tears at its top corner. Another attempt only enlarges the tear.{/n}
You put the damaged copy beside the untouched one. For a moment it is tempting to begin again and send only the better result. Her request beneath the drawing stops you.
"I could not make the two hinges agree," you write. "I damaged the paper while trying. The door does open now, but only because its upper corner is torn. I do not propose pretending that this was my intention."
You describe the attempts in order and leave the spare copy blank.
"If you want to finish this construction yourself, I would like to see it. If you would rather use the paper for something else, I would like to know that too."
{n}Both copies go into the packet. The failed one remains on top.{/n}''', c("Return the failed attempt honestly.", flags=("targona.fold_failed",))),
    n("cut", "Narrator", '''{n}You cut three sides of a rectangle in the clear part of the copied wall. The fourth becomes a hinge. You trim a narrow strip from the flap's free edge so it opens without catching. When you lift it, the drawing opens onto the surface of your desk.{/n}
It is an almost offensively simple answer to a careful diagram. You keep the discarded strip rather than tidying it away, and write down precisely what you did.
"I made another opening. Your careful numbering now leads directly to a hole. I hope you will forgive the untidiness; I did at least manage to cut straight."
At the bottom you add a practical improvement: the new door wants a small handle so it can be opened without tearing its corner. You leave Targona to choose what shape that handle should take.
{n}The uncertain original hinges remain visible. The new door does not need them to become correct.{/n}''', c("Return the new opening and the strip you cut away.", flags=("targona.fold_cut",))),
], "targona.second_margin")


s("an_unpromised_future", "The part no one commissioned", [
    n("start", "Narrator", '''{n}Targona's reply includes the paper door. She has added a handle shaped like a very small wing, and written OPEN HERE beside it in unnecessarily large letters.{/n}
"I wanted one line on this page that nobody could preach a sermon over."
{n}Her account of what happened to the drawing follows.{/n}''',
      c("Read how she used the successful fold.", "found", requires=("targona.fold_found",)),
      c("Read what she did with the torn copy.", "failed", requires=("targona.fold_failed",)),
      c("Read what she made of the new door.", "cut", requires=("targona.fold_cut",))),
    n("found", "Narrator", '''"I did your folds twice. The third time I did them in the wrong order and shut the little lock inside the room. I liked it so much I kept it.
"You were right to mark the folds that failed. Without them I would have believed your hand went straight to the right line, the way I believe everyone's hand does except my own.
"I have opened the door more often than is seemly for a blade of Iomedae. The dream has not changed, and I will not tell you it has to make you feel clever. But at dawn prayers I gave thanks for a paper door, and I did not feel foolish, and I have not been able to say that about a prayer since the laboratory."
{n}The letter moves on to the collector. Her hand is firmer here than it was round the copied hinges.{/n}''', c("Read about her account.", "account")),
    n("failed", "Narrator", '''"Thank you for sending the torn one on top. I knew the temptation you meant.
"I tried the spare. My door caught too. So I cut a new hinge at the torn corner, which would be a poor repair on any door that has to keep out the weather. For a door that only has to open, it serves.
"I keep your attempt beside mine. Two badly made things, and nobody standing over them calling it a miracle. I have had miracles announced over my head before, in that laboratory, in a voice I still hear when the lamps go out.
"The dream is the same. The paper has not cured it. It has given my hands something to finish after I wake, and I have thanked Iomedae for smaller mercies."
{n}She turns to the collector without apologising for how little the paper did.{/n}''', c("Read about her account.", "account")),
    n("cut", "Narrator", '''"I laughed when I saw the hole. Then I scolded myself for laughing. Then I opened it again.
"I gave the door a handle. You will see its shape is grander than the carpentry deserves. I chose it because I liked it, for no better reason, and I have not done that since before Areelu.
"I am keeping the strip you cut away. If anyone asks why my drawing has a hole in it, I can show them exactly where the wall went.
"The dream has not changed. Some foolish part of me hoped it would. What changed was the hour after I woke. I had work for my hands that was not holding them still."
{n}Below this she has written about the collector.{/n}''', c("Read about her account.", "account")),
    n("account", "Narrator", '''{n}A second sheet records her reply to the collector, in her own words rather than a copy of yours.{/n}''',
      c("Read the consequences of publication.", "public", requires=("targona.account_public",)),
      c("Read the consequences of refusing publication.", "private", requires=("targona.account_private",))),
    n("public", "Narrator", '''"I sent him the short account. I wrote that I am glad men lived near me, that I was a prisoner, and that the one does not explain the other. I left the lost hours lost.
"He wrote back asking me to take out the line where I say I hated the room. He said it took something from the courage of the survivors. I told him the line was about the room and not about them, and that if he struck it I would come to his shop and read it to him aloud. He has kept it.
"A sergeant of the Mendevian line wrote to me afterwards. He said it made him less ashamed of how angry he still is about the Worldwound. I answered him the same day. Another reader asked why an angel needs so many words. I have not answered him. I prayed for patience instead, and that prayer has not been answered either.
"I am glad I sent it. I am gladder that I do not have to send another."
{n}At the bottom she has begun a question meant only for you.{/n}''', c("Read the private question.", "question")),
    n("private", "Narrator", '''"I refused him. He was courteous and disappointed, and then he printed another man's account in the place mine would have gone. It gives me one paragraph. It says that the angel Targona gave herself to the Architect's barrier of her own will, so that her light might shelter the camps, and that her sacrifice was accepted in Heaven. It is beautifully written. Every word of it is a gift to Areelu.
"I was so angry I broke a basin. One of the good ones. The sister who keeps the linen made me sweep it up myself, which was just.
"There are men in the Mendevian camps who will read it and believe that what was done to them near that laboratory was an angel's holy choice. It was not. It was Areelu's, and she chose it for all of us. When my duties next take me into the city, I will go to his shop and ask him, before Iomedae, to print a correction. I will not shout. I will not need to.
"I still will not give him my pages. But I will not let him give her mine."
{n}She has left the next question on a line of its own.{/n}''', c("Read the private question.", "question")),
    n("question", "Narrator", '''"May I ask you something that has no place in any account? What should I want, when nobody needs me for an hour?"
{n}She has struck the question out and left it legible. Beneath it is another.{/n}
"That was unfair. I began by asking you to choose for me, which is what everyone has done since the laboratory. Here is a better one. Will you help me with something useless? I want to write a woman in that room who knows what she wants before anyone comes to open the door.
"It will not change what happened. I want to see what it does to the page."
{n}There is a lightly drawn rectangle below the words, waiting for something to be put inside it.{/n}''',
      c('Suggest a scene in which she chooses to leave.', flags=("targona.story_leaving",)),
      c('Suggest a scene in which she chooses who may enter.', flags=("targona.story_receiving",))),
], "targona.the_folded_room")


s("the_unscheduled_door", "Permission to surprise the page", [
    n("start", "Narrator", '''{n}The scene Targona sends is brief. She has given its woman a name that is neither her own nor a title bestowed by people who needed protection.{/n}
"I have called her Meret. I know no Meret who is likely to object. If you do, please do not tell me until I have finished this draft."
{n}Meret wakes in a room containing a chair, a closed door, and a parcel tied with a thoroughly unreasonable quantity of string. The parcel is important enough to occupy three lines. The room's creator receives none.{/n}
"I found I wanted to write about what she would take with her," Targona explains. "Then whether she would share it with anyone. I have enjoyed this more than anything since I woke in that barrier. I prayed about whether that was permitted, and nothing struck me down."
{n}You read the ending shaped by your suggestion.{/n}''',
      c("Read Meret's departure.", "leaving", requires=("targona.story_leaving",)),
      c("Read Meret's invitation.", "receiving", requires=("targona.story_receiving",))),
    n("leaving", "Narrator", '''{n}Meret opens the door, discovers a street she does not recognize, and is immediately asked whether she is expected somewhere. She says that she is, having just made the appointment with herself.{/n}
She takes the parcel to a bench where she can undo its knots in good light. Inside is a cup she has never liked. She exchanges it for a chipped blue one and spends the difference on something sweet enough to make the vendor warn her.
"I could not decide where she should go next," Targona writes. "For once, that did not feel like a failure in the story. I wanted her to have more street than she could use in a paragraph."
{n}The final line says only that Meret finishes her purchase before anyone can turn it into a lesson. A little ink has spread beneath the word 'finishes.'{/n}''', c("Consider what you might add.", "method")),
    n("receiving", "Narrator", '''{n}Meret opens the parcel and finds a cup she has never liked. She places it on the table anyway, because it will do for a guest until she obtains another.{/n}
Then she puts a chair beside the door and writes a notice: KNOCK IF YOU HAVE SOMETHING TO SAY THAT IS NOT ABOUT MY USEFULNESS.
The first visitor asks to borrow a spoon. Meret almost shuts the door, then decides that this is at least an honest request. She lends it, refuses to lend the cup, and asks whether the visitor knows a place selling better ones. He directs her to a stall at the corner. She chooses a chipped blue cup, leaves the old one on the table for guests, and makes him promise to return her spoon.
"I like her," Targona writes. "She is less gracious than I meant her to be. I would enjoy visiting her, provided I brought my own spoon."
{n}The story ends with the door left at an angle Meret chose herself.{/n}''', c("Consider what you might add.", "method")),
    n("method", "Narrator", '''{n}Targona has left the opposite side of the sheet blank for your contribution. She has written one condition at its top: NO REWRITING WHAT SHE ALREADY CHOSE.{/n}
You can add another ordinary street to the fiction, a reply from the visitor, or simply tell her which sentence made you smile. You copy out her ending first. By the time you reach the parcel, you have developed a strong dislike of its string.''',
      c("[Trickster] Give the copied page an extra ending that refuses to stay last.", "trick", requires=("trickster",)),
      c("Write a second ordinary scene, leaving her first ending intact.", "ordinary")),
    n("trick", "Narrator", '''{n}You write THE END beneath your copy, then draw a door below it. When you turn the paper over, the little door is above the words. Turn it again, and the end has acquired a corridor. For a moment the ink refuses to agree on which side of the sheet it belongs to.{/n}
You keep one hand on the unchanged original while the copy quarrels with its own conclusion. The little corridor turns left where the edge of the sheet ought to stop it.
The corridor's last line curls into a question mark. You flatten the sheet, and it behaves like paper again, except that the little door now appears on both faces without the ink having bled through.
{n}You describe the oddity in your reply, then attempt to label the two sides. Both insist on being the front. You leave Targona a warning in the margin: "Do not let it give you directions."{/n}''', c("Send the altered copy alongside the unchanged original.", flags=("targona.extra_ending",))),
    n("ordinary", "Narrator", '''{n}You leave Meret's chosen ending where Targona put it. On the next page you give her a minor inconvenience: the chipped blue cup is a very awkward shape to carry. She must either hold it in her hand or ask someone for wrapping.{/n}
The trouble is small enough to be funny. Meret makes an unnecessarily elaborate plan, abandons it, and carries the cup. You sketch her proposed arrangement of string and discover halfway through that you cannot make it work either.
"I like the person you wrote," you add. "I wanted to find out what she would do with a problem she was allowed to consider beneath her dignity."
{n}You return the two scenes together, including the unsuccessful sketch. You would like to see what she writes beside it.{/n}''', c("Send the second scene with her original.", flags=("targona.ordinary_ending",))),
], "targona.an_unpromised_future")


s("what_she_keeps", "A letter she wanted to write", [
    n("start", "Narrator", '''{n}Targona's latest letter is less carefully arranged than the others. The first paragraph has been moved with an arrow, a second thought has been squeezed above the date, and a faint ring marks where a cup stood too near the edge.{/n}
"I began this before deciding what it was about. I recommend the experience in moderation."
{n}Her answer to your contribution occupies the first page.{/n}''',
      c("Read her response to the Trickster page.", "trick", requires=("targona.extra_ending",)),
      c("Read her response to the ordinary continuation.", "ordinary", requires=("targona.ordinary_ending",))),
    n("trick", "Narrator", '''"I turned the sheet over six times. The door remained on both faces. I held it to the light because I suspected you had simply pressed too hard with the pen. You had not.
"I liked the trick. And then I wanted to ask whether you could do the same to the room I remember: turn it over until the door was on the outside. I did not ask. I am telling you I wanted to, because a temptation hidden is a temptation half obeyed, and I was taught that in Heaven before I was taught to hold a sword.
"I have put your impossible page beside my very possible account. I can tell them apart. I thank Iomedae that I still can.
"Leave the room as it was. Send me more pages like this one, that argue with me. I have enjoyed the argument."
{n}She has drawn Meret opening the door from its unexpected side. The figure carries a cup.{/n}''', c("Read the next page.", "voices")),
    n("ordinary", "Narrator", '''"I laughed at her plan for carrying the cup. Then I improved the plan in the margin, which I believe was exactly the trap you laid for me.
"I gave Meret a companion for the next street. He talks too much about ceramics, and she discovers that she does not mind. I have not decided whether he will remain in the story. I am enjoying being able to decide that without a prophecy, an experiment, or someone announcing what sort of creature she must become.
"I still wake with the old room in my thoughts sometimes. I have no triumphant ending to attach to that sentence. But there are other things waiting on the table now. A cup I like, a story I may change, and letters I am glad to receive.
"I did not expect a cup to do so much. I suppose that is what cups are for."
{n}She has enclosed the beginning of the new street, stopping before the talkative visitor can explain a second glaze.{/n}''', c("Read the next page.", "voices")),
    n("voices", "Narrator", '''{n}The next sheet is folded separately from the story.{/n}''',
      c("Read the two notes inside.", "two", requires=("targona.ran_trickster",)),
      c("Read the two notes inside.", "two", requires=("targona.ran_aeon",), forbids=("targona.ran_trickster",)),
      c("Read Targona's private note.", "personal", forbids=("targona.ran_trickster", "targona.ran_aeon"))),
    n("two", "Anograt", '''"Silver says I may write this part myself. An extraordinary concession, considering that I have been writing in the margins from the beginning.
"You sent both endings back. Good. When we disagree about a story you get two letters, not one sensible compromise. Nobody has ever made a sensible compromise with a wing.
"My opinion is that Meret should keep the bad cup and use it to hold the collector's rejected adjectives. Eventually she could sell them. There is clearly a market."
{n}Targona's reply sits immediately below.{/n}
"I prefer the chipped blue cup. I also prefer Anograt saying what she thinks in her own name. We disagree about how much room the cup requires in the next chapter.
"Please continue addressing the letters to me. Add a page for her if you wish. She will still read over my shoulder, but I have found that asking is an improvement over discovering her conclusions already in the margin."''', c("Read Targona's final lines.", "personal")),
    n("personal", "Narrator", '''"There is something else. Every letter I have sent you has had the laboratory in it somewhere. That is not what I think about when I think about you."
{n}The sentence ends at the fold. You open the lower half of the sheet.{/n}''',
      c("Read what your lover chose to write.", "lover", requires=("targona.ran_romance",)),
      c("Read what your friend chose to write.", "friend", forbids=("targona.ran_romance",))),
    n("lover", "Narrator", '''"I miss kissing you. There. I have written it without first telling you how useful your last letter was.
"I miss the pause before you decide whether to say something outrageous, and the occasions when you decide against it and I can tell anyway. I would like a little time with you when neither of us has a page to finish."
{n}The next line has been crossed out and replaced.{/n}
"I almost promised to be less complicated company. That would be a poor promise. I can offer to be glad when you arrive.
"Until we can arrange it, send me something you have wanted to tell me. It may be foolish. I have become fond of the parts of your letters that would be omitted from an official copy."
{n}She signs her name below the invitation. You read the first line again before reaching for a fresh sheet.{/n}''',
      c('Reply with affection and a private joke for the next letter.', flags=("targona.extension_opening_kept", "targona.private_letters",)),
      c('Reply that you want that quiet time too, and will arrange it when you can.', flags=("targona.extension_opening_kept",))),
    n("friend", "Narrator", '''"Tell me about something you enjoyed. It need not serve the crusade. I find I like news that nobody thought important enough to send before.
"Bad stories. Quarrels about cups. The kind of complaint that shrinks when somebody else reads it. Send me those too, between the hard pages."
{n}She has enclosed another blank strip beneath the signature.{/n}
"For your unrelated complaint. I will do my best not to turn it into an uplifting account."
{n}You leave the strip beside your unfinished reply. It is too narrow for the complaint you have in mind. You fetch a larger sheet and begin with that.{/n}''',
      c("Send a personal reply and keep the correspondence open.", flags=("targona.extension_opening_kept",))),
], "targona.the_unscheduled_door")


s("the_open_threshold", "A door that opens both ways", [
    n("start", "Narrator", '''{n}Targona's letter carries the impression of a page opened and closed many times. She has drawn a small door beside the seal.{/n}
"My current post has put me at the Celestial Order's wayhouse just beyond Drezen's eastern road. The courier who brought this can carry your reply back there. It is on Golarion, and the road between it and the city is ordinary.
"I do want to see you. I have wanted it since the last packet, and I have been ashamed of how often I reread it.
"But I know you, a little. If there is a trick in your answer, tell me what it is before you ask me to walk through it. I spent a long time behind a barrier that someone else built for my own good. I will not step through another door I have not seen tested, not even yours. If the road is all we have, the road will do."
{n}The invitation names the Drezen courtyard as the meeting point. The courier's dispatch slip carries the same wayhouse address as Targona's letter.{/n}
{n}Anograt's earlier note is still in the packet. It says nothing about this evening, and you leave it that way.{/n}''',
      c("[Trickster] Continue from the impossible extra door you drew on her page.", "paper_setup", requires=("trickster", "targona.extra_ending")),
      c("[Trickster] Use the ordinary courier route and a fortunate change of dispatch.", "courier_setup", requires=("trickster", "targona.ordinary_ending")),
      c("Decline the meeting tonight and keep the correspondence open.", "declined"),
      c("Answer that you will leave the letter in the courier's hands.", "ordinary", forbids=("trickster",))),
    n("paper_setup", "Narrator", '''{n}The impossible page is still with you. On its copy the door appears on both faces, and the short corridor refuses to end at the edge of the paper.{/n}
It is not a portal yet. It is only a pattern your Trickster power has already made strange, and she has told you what she thinks of doors she has not seen tested. You can try to use that contradiction to join two real, named places on the same plane: her wayhouse and the courtyard where you would meet.
First you must test the opening without sending anyone through it. If its ends will not stay where you put them, it does not become an invitation.''',
      c("[Knowledge (Arcana)] Test and stabilize both ends before inviting her.", check=dict(Skill="SkillKnowledgeArcana", DC=30, Success="steady", Failure="falter", CommanderOnly=True)),
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
    n("steady", "Narrator", '''{n}The two anchors hold when you test the opening with an empty dispatch pouch, first from the wayhouse side and then from Drezen. The path returns to the same two places every time. It will stay open for the evening.{/n}
{n}The courier carries Targona a written account of the test, the way to close the passage, and the key. She reads every line of it. Her reply is one sentence: "I will inspect it myself."{/n}
{n}When she arrives in the Drezen courtyard she examines both anchors, slowly, the way a healer examines a wound someone else has dressed, and then puts the key in her own pocket.{/n}
"It is well made," she says. "For a trick."''',
      c("Walk the wall with her.", "walk"),
      c("Tell her the wounded on the eastern road will want her at first light.", "close_passage")),
    n("falter", "Narrator", '''{n}The first end shifts when you test it with the dispatch pouch. The pouch comes back with its seams turned inside out. You close the opening before the courier ever sees it.{/n}
{n}You send an ordinary letter instead, and tell her exactly what failed. Targona answers by the same courier.{/n}
"Thank you for not sending me the key. I would have used it, and you know that, which is why I am glad you did not.
"Write to me tonight instead. Tell me something from your day too small for a dispatch. When there is a road worth trusting, I will walk it."''',
      c("Answer her and keep the correspondence open.", flags=("targona.visit_correspondence",))),
    n("road", "Narrator", '''{n}The courier carries your invitation to the Celestial Order's wayhouse. Targona comes by the public eastern road, on foot, stopping twice on the way at the dressing station by the ford because there were men there.{/n}
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
{n}She turns to face you. The black wing lifts a little, the way it does when she is startled, and she does not fold it down.{/n}
"Commander. You have looked at me like that the whole length of the wall. Are you going to do anything about it?"''',
      c("Ask her again, and wait for her answer.", "kiss"),
      c("Tell her you would rather continue the walk.", "continue")),
    n("close_passage", "Narrator", '''{n}She looks east, where the watchfires are, and then turns the key herself; the opening folds shut at the Drezen end.{/n}
"You are right, and I hate it. If I stay, I will stay too long, and tomorrow there are wounded on the eastern road who deserve an angel who slept." {n}She smiles, a little ruefully, and offers you her arm.{/n} "Walk me to the road, at least. I will not use your trick twice in one night."''',
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
{n}Her thumb rests beneath your jaw. When she lets you breathe she keeps her brow against yours, and the black wing has come half open behind her without her noticing.{/n}
"I have missed that," she says. "I have missed wanting something that nobody will write down afterwards as a symptom."
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
{n}She draws her plain wayhouse habit over her head and lets it fall, and the black wing opens behind her in the dark and brushes the wall. She pushes you back onto the bed and follows you down, her knees either side of you, her hair falling round both your faces, and takes your hands and puts them where she wants them.{/n}
{n}Long before light she is dressing again by the window. The wounded on the eastern road will want her at the first bell, she says, and she will not let them want her in vain on your account. She kisses you once more at the door, hard, and does not say when.{/n}''',
      c("Let her go back to her road.")),
    n("continue", "Narrator", '''{n}You tell her that a walk is enough. Targona leaves her fingers in your sleeve and chooses the battlements, where the city opens below and the watchfires on the eastern road show where the wounded are coming in.{/n}
"There," she says, pointing. "That fire is the ford. They brought eleven across it this morning. I counted." {n}She is quiet for a moment.{/n} "I have spent my whole life being useful. I am not sure I know how to be idle beside someone."
"Walk until I am tired. Then eat something sweet enough to be imprudent. Then decide whether I want another kiss. That is my plan, and I will not be argued out of it."
{n}She tells you which of the city lights she can see from the terrace, and which she has mistaken for stars, and which is the lamp in the infirmary where a boy with a fever is waiting for morning.{/n}''',
      c("End the evening with affection and leave the next choice open.", flags=("targona.visit_tender",)),
      c("Ask if she would like that second kiss now.", "kiss")),
], "targona.what_she_keeps", delay=0, requires=("targona.ran_romance",))


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
"I still want you. I was glad you did not hurry me. I have been hurried by Areelu, and by Heaven's healers, and by my own fear, and you were the first thing in a long time that simply waited. I would like another evening. Come when the wounded let you."
She has added a small sketch of the courtyard, with the way in and out marked in equal-sized arrows.''',
      c("Tell her you want another evening, whenever the wounded can spare her.", flags=("targona.key_unpressured",)),
      c("Tell her you want to kiss her again when she asks.", flags=("targona.key_reciprocal",))),
    n("correspondence", "Narrator", '''{n}Targona's letter contains a short account of an uneventful afternoon and a question about a story you once sent her.{/n}
"We did not meet that evening. I am not sorry. I think I needed one more letter first. Tell me the ending of the story you started last time; you stopped just when the bridge was about to fall, and I have been worrying about the bridge."
She sends a recipe for a sweet she has recently learned to make. The measurements are exact. The instruction to wait before adding the last ingredient has been underlined twice.''',
      c("Reply with an ordinary detail and keep the conversation open.", flags=("targona.key_unpressured",))),
], "targona.the_open_threshold", requires=("targona.ran_romance",))

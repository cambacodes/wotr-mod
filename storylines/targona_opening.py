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
    n("start", "Narrator", '''{n}The packet waiting among your personal correspondence contains a letter and a folded drawing. Targona has written your name rather than your title on the outside. There is no request for another treatment.{/n}
"I tried saying this aloud and kept beginning with an assurance that I was well. That is a poor beginning when one wishes to ask a difficult question. Please do not mistake the question for a change in what we already decided together.
"I have been drawing a room from the laboratory. I remember its door particularly clearly. When I put it on paper, however, I keep drawing the lock on the wrong side. I know perfectly well that I am free. I can even laugh at the drawing in daylight. Then I make it again.
"Will you look at it? I would like an answer from someone who has walked out of that place, rather than another explanation of what an angel ought to endure."''',
      c("Unfold the drawing.", "drawing"), c("Put the unopened drawing aside until you have time to read carefully.", abort=True)),
    n("drawing", "Narrator", '''{n}The paper shows a square room, a narrow table, and a door whose hinges have been drawn twice. A neat arrow points outward. The lock lies across that arrow like a correction.{/n}
Targona has added three notes beneath it.
"This is a recollection, not a plan for returning. I am not asking you to find the room again. Some of the distances may be wrong. I spent very little time looking at it from above."
The last sentence is underlined once, as though she has decided you may laugh at that much.
"There are hours I cannot account for. I will not fill them with whatever makes the best story. But I would like to stop giving Areelu the only intelligible part of this one: she had a purpose, and I was what she acted upon.
"What did you first notice when you looked at the page? Please answer before thinking of what would comfort me."''',
      c('Write: "You drew an exit before you drew its obstruction."', "exit"),
      c('Write: "The second set of hinges. You checked your own memory."', "hinges")),
    n("exit", "Narrator", '''{n}You mark the point where the arrow begins. Its first stroke is darker than the line across it.{/n}
"I cannot tell you which line belongs to the actual room," you write. "I can tell you which you put down first. You began by showing me a way out. The obstruction came afterward. I would like to know whether you remember making that correction."
You resist an easy promise that the drawing will cease troubling her now that someone has noticed it. A second question takes longer to phrase.
"Would you like me to return this with my marks on it, or make a separate copy? I do not want my explanation to become another line you must draw around."
{n}There is room for a personal sentence below the question. The page no longer looks like an examination, but neither does it pretend to be an answer.{/n}''',
      c("Continue the letter.", "personal")),
    n("hinges", "Narrator", '''{n}You copy the two sets of hinges onto a separate scrap. One would allow the door to open inward; the other would keep it pressed against the corridor wall.{/n}
"You have left the disagreement visible," you write. "You could have rubbed one version out and given me a much tidier memory. Instead you showed me where you were uncertain. I trust that more than a perfect plan."
"May I work on a copy? We could try another arrangement without deciding that the original must have been different. I would rather learn what you can do with the page now than force it to testify about everything that happened then."
{n}You put the scrap beside the letter, leaving space beneath the practical questions.{/n}''',
      c("Continue the letter.", "personal")),
    n("personal", "Narrator", '''{n}The folded room is small enough to cover with one hand. You leave it open while finishing your reply.{/n}''',
      c('Write: "I miss you. I would rather have this difficult letter than only the reassuring ones."', "romance", requires=("targona.ran_romance",)),
      c('Write: "You do not have to make this easy for me to remain your friend."', "friend")),
    n("romance", "Narrator", '''{n}You add a memory of the way she looks at you when she has decided to risk saying something before finding the perfect words. You remember leaning closer to hear her, though her voice had been perfectly clear.{/n}
"I would like another ordinary evening with you. I would also like to understand this part of the days between our evenings. You need not earn one by explaining the other."
The final sentence is less polished.
"And I am keeping enough of my desk clear to unfold whatever you send next."
{n}You seal the letter, keeping the drawing out of the official dispatches. Clearing the promised space takes longer. Several urgent reports must learn to share a corner.{/n}''', c("Send your reply with the next personal correspondence.", flags=("targona.correspondence_opened",))),
    n("friend", "Narrator", '''{n}You write that you would be glad to hear about the things she notices now, including anything too small to justify a report. You begin a list of examples, then cross it out before your invitation acquires instructions.{/n}
"If you tire of this experiment, tell me. We can argue about something else. I would prefer an inconvenient friendship to an exchange of assurances that leaves us knowing no more about each other."
You consider adding a joke about your own difficult correspondence and decide that this would invite questions about military paperwork. Instead you leave a clean strip at the bottom of the page and label it ROOM FOR AN UNRELATED COMPLAINT.
{n}The letter joins the personal correspondence. Her drawing stays separate from the official dispatches, with its uncertain hinges and its first, hopeful arrow intact.{/n}''', c("Send your reply with the next personal correspondence.", flags=("targona.correspondence_opened",))),
], delay=0)


s("second_margin", "Who holds the pencil", [
    n("start", "Narrator", '''{n}Targona returns your letter with a new sheet. She has filled the space for unrelated remarks whether or not you formally provided one.{/n}
"The person who packed these sheets used far too much string. I have now spent longer freeing the paper than drawing on it. I believe that qualifies as a complaint.
"Yes, make a copy. Keep the first drawing as it is. I do not want to improve it until I no longer recognize why I sent it.
"I have been looking at the correction again. I remember putting the lock across the arrow. I was annoyed because the door appeared too easy to leave. I realize how that sounds. Please allow me the dignity of having noticed it before you did."
{n}Below this, her handwriting becomes smaller.{/n}
"Someone has asked me to describe the laboratory for a collection of crusader accounts. A short, uplifting description. I thought I wanted to do it. Now I cannot get past the adjective."''',
      c("Read the additional note.", "anograt", requires=("targona.ran_trickster",)),
      c("Read the additional note.", "anograt", requires=("targona.ran_aeon",), forbids=("targona.ran_trickster",)),
      c("Read Targona's proposed account.", "account", forbids=("targona.ran_trickster", "targona.ran_aeon"))),
    n("anograt", "Anograt", '''{n}A different hand has occupied most of the margin.{/n}
"Silver asked me to help. I offered to write the account from the lock's point of view. It would be a short career followed by a deserved retirement. She smiled, so the suggestion was not entirely wasted.
"We have been sharing a table. Silver gets the chair with the good cushion; I get the edge of the paper she hasn't written on yet. You can see how much she values my contribution.
"She wants to write it herself. I want her to stop crossing out the parts where she is angry. Apparently these are different problems.
"My proposal is that we give the collector the most uplifting account imaginable: a door rising off its hinges and striking the person who built it. Silver says that is not what happened. I said the word was uplifting, not accurate."
{n}Targona has written beneath this: "This is why I still need your answer."{/n}''', c("Read Targona's proposed account.", "account")),
    n("account", "Narrator", '''{n}The draft begins with the people who survived near her imprisoned presence. It does not name them or claim to know what has become of each of them since. After that the sentences grow impersonal.{/n}
"The captive angel remained a source of protection. Her suffering was therefore not without purpose."
Those lines have been crossed out so firmly that the nib tore a small hole in the sheet.
"I wrote that," Targona explains. "No collector put those words in my mouth. I was trying to give the reader something useful and found myself making an argument for leaving me there.
"People lived because I could protect them. I am glad of it. I would have protected them awake and free if I had been allowed. I cannot make the second fact small enough to fit underneath the first."
The page ends with a question: should she attempt the public account now, or tell the collector that she is not ready?''',
      c('Recommend a short account in her own name, including the anger and uncertainty.', "publish"),
      c('Recommend a private account for now, with an explicit refusal of publication.', "private")),
    n("publish", "Narrator", '''{n}You write a proposed first sentence: "I protected people while I was imprisoned; my imprisonment was not what made their lives worth protecting." You mark it as a suggestion, leaving Targona room to reject the wording.{/n}
The rest of your reply is practical. A short account need not explain every hour or end in a lesson. She can say what she remembers, identify what others later told her, and refuse to let an editor supply a fortunate conclusion to the missing parts.
You also name the cost. Once circulated, her words may be quoted badly. The crossed-out sentence may be replaced by something equally tidy in someone else's summary. You cannot prevent every reader from wanting a simpler angel.
"I would still read what you actually mean," you conclude. "If you choose to send it, let the account have an end without pretending the matter is ended."''', c("Send the suggestion to publish on those terms.", flags=("targona.account_public",))),
    n("private", "Narrator", '''{n}You recommend that she refuse the request plainly, without promising a publication date to soften the refusal.{/n}
"Keep the account if writing it helps you. Let it be addressed to a person you chose. The collector can ask someone else for an uplifting paragraph. You do not owe the collection a version of yourself that fits its heading."
That decision has a cost too. Other people will continue telling the story with less of her voice in it. Silence will not make them accurate. You say this before offering to keep her pages, so that privacy is not presented as a way of escaping every consequence.
"If you later want to publish it, we can return to that decision. For now, I would like to read what you stopped yourself from writing. I will not forward it."
{n}You leave the proposed public heading uncorrected and fold it behind the reply.{/n}''', c("Send the suggestion to keep the account private.", flags=("targona.account_private",))),
], "targona.correspondence_opened")


s("the_folded_room", "An exit on the page", [
    n("start", "Narrator", '''{n}The next packet contains two copies of the room and a strip of paper broad enough to make a little door. Targona has left the original out of this experiment.{/n}
"I have acted on the decision about the account. I will tell you what followed when there is something to tell.
"For today I would like to try your other suggestion. This copy may be changed; keep the original safe. I want to put something on this page that I can choose to open.
"I have drawn the hinges both ways. You may settle the matter by observation, ingenuity, or an argument with the paper. I suspect you have qualifications in at least two of those."
{n}The copied lines almost meet at one corner. Beneath them she has written: "Please return your attempt even if it fails. I am tired of hearing only about successful experiments."{/n}''',
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
"I wanted one instruction on this page that did not require interpretation."
{n}Her account of what happened to the drawing follows.{/n}''',
      c("Read how she used the successful fold.", "found", requires=("targona.fold_found",)),
      c("Read what she did with the torn copy.", "failed", requires=("targona.fold_failed",)),
      c("Read what she made of the new door.", "cut", requires=("targona.fold_cut",))),
    n("found", "Narrator", '''"I reproduced your folds twice. On the third attempt I did them in the wrong order and shut the little lock inside the room. I liked that version enough to keep it.
"You were right to mark the unsuccessful folds. Without them I would have assumed your hand went straight to the correct line. I find that I am very willing to imagine everybody else's certainty.
"The door pleases me. I have opened it an unreasonable number of times. It has not changed the dream into a pleasant one, and I will not give you a false report to make the experiment look better. But I have something from the waking part of the day to put beside it."
{n}The letter moves on to the matter of the collector. Her handwriting here is firmer than it was around the copied hinges.{/n}''', c("Read about her account.", "account")),
    n("failed", "Narrator", '''"Thank you for leaving the failed copy on top. I recognized the temptation you described.
"I tried the spare sheet. My door also caught. I then cut a new hinge at the torn corner, which would be a poor repair for any door required to keep out the weather. For a door whose only purpose is to open, it is quite satisfactory.
"I have kept your first attempt beside mine. There is something comforting about two badly made objects that nobody has called a breakthrough. I do not mean that unkindly. I have had enough of breakthroughs announced over my head.
"The dream is still unpleasant. The paper has not cured it. It has given me a small task I can finish afterward, and I am glad of that."
{n}She turns to the collector's request without apologizing for the limited result.{/n}''', c("Read about her account.", "account")),
    n("cut", "Narrator", '''"I laughed when I saw the hole. Then I was annoyed with myself for laughing. Then I opened it again.
"I gave the door a handle. You will see that its shape is more elaborate than its engineering deserves. I wanted to choose something merely because I liked it.
"I am keeping the strip you cut away. If anybody asks why the drawing has a hole, I can show them exactly how it happened. I like that better than pretending the wall was never there.
"The dream has not changed. I did not expect a piece of paper to accomplish that, though some hopeful part of me apparently did. What changed was the hour after I woke. I had something to do with my hands besides trying to be composed."
{n}Below this she has written about the account and the decision you helped her make.{/n}''', c("Read about her account.", "account")),
    n("account", "Narrator", '''{n}A second sheet records her reply to the collector, in her own words rather than a copy of yours.{/n}''',
      c("Read the consequences of publication.", "public", requires=("targona.account_public",)),
      c("Read the consequences of refusing publication.", "private", requires=("targona.account_private",))),
    n("public", "Narrator", '''"I sent the short account. I wrote that I am glad people survived near me, that I was imprisoned, and that these facts do not explain each other. I left the missing hours missing.
"The collector asked whether I would remove the sentence in which I said I hated the room. He thought it distracted from the courage of the survivors. I told him that the sentence concerned the room, not a defect in their courage. He has agreed to keep it.
"One reader wrote to say that the account made him less ashamed of remembering a battle with anger. Another asked why an angel required so much explanation. I have answered the first letter. I have not answered the second.
"I am glad I sent it. I am also glad I do not have to send something every day merely because someone found it useful."
{n}At the bottom she has begun a question addressed only to you.{/n}''', c("Read the private question.", "question")),
    n("private", "Narrator", '''"I refused the request. The collector was courteous and disappointed. He has printed another account in its place, which describes my captivity in one sentence. It is not false. It is so small that I scarcely recognize anything in it.
"I was angry when I saw it. Then I remembered that I had chosen to keep my own pages. The anger does not prove the decision was wrong. It does mean that privacy has not given me control over every story told about me.
"I have written more than I intended. Some of it concerns the room. Some concerns what I wanted to eat on the first morning when nobody else decided whether I would wake. I may send you that part. It is less instructive and more opinionated.
"I still prefer this arrangement for now."
{n}She has left the next question on a separate line.{/n}''', c("Read the private question.", "question")),
    n("question", "Narrator", '''"May I ask something that has no place in the account? What do you think I should want when nobody needs me for an hour?"
{n}The question has been crossed out, but left legible. Beneath it is a replacement.{/n}
"That was unfair. I began by asking you to choose for me. Here is the better question: will you help me try something unnecessary? I want to write a scene in which the woman in the room knows what she wants before anyone arrives to free her.
"I know it will not alter the past. I want to see what it does to the page."
{n}There is a lightly drawn rectangle below the words, waiting for something to be put inside it.{/n}''',
      c('Suggest a scene in which she chooses to leave.', flags=("targona.story_leaving",)),
      c('Suggest a scene in which she chooses who may enter.', flags=("targona.story_receiving",))),
], "targona.the_folded_room")


s("the_unscheduled_door", "Permission to surprise the page", [
    n("start", "Narrator", '''{n}The scene Targona sends is brief. She has given its woman a name that is neither her own nor a title bestowed by people who needed protection.{/n}
"I have called her Meret. I know no Meret who is likely to object. If you do, please do not tell me until I have finished this draft."
{n}Meret wakes in a room containing a chair, a closed door, and a parcel tied with a thoroughly unreasonable quantity of string. The parcel is important enough to occupy three lines. The room's creator receives none.{/n}
"I found that I wanted to write about what she would take with her," Targona explains. "Then I wanted to know whether she would invite anyone to share it. These turned out to be questions I enjoyed. I had not expected to enjoy writing any of this."
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
"I like the trick. I also found myself wanting to ask whether you could do something similar with the room I remember. I did not ask. I wanted to tell you that the temptation was there, rather than praise your restraint as though I had never wished for more.
"For now I have put your impossible page beside my very possible account. I can distinguish them. That matters to me.
"I know what your power has already changed in my life. I do not need every new use of it to be another change made to me. This one gave me a thing to argue with, and I have enjoyed the argument."
{n}She has drawn Meret opening the door from its unexpected side. The figure carries a cup.{/n}''', c("Read the next page.", "voices")),
    n("ordinary", "Narrator", '''"I laughed at her plan for carrying the cup. Then I improved the plan in the margin, which I believe was exactly the trap you laid for me.
"I gave Meret a companion for the next street. He talks too much about ceramics, and she discovers that she does not mind. I have not decided whether he will remain in the story. I am enjoying being able to decide that without a prophecy, an experiment, or someone announcing what sort of creature she must become.
"I still wake with the old room in my thoughts sometimes. I have no triumphant ending to attach to that sentence. But there are other things waiting on the table now. A cup I like, a story I may change, and letters I am glad to receive.
"I wanted you to know the difference your ordinary page made."
{n}She has enclosed the beginning of the new street, stopping before the talkative visitor can explain a second glaze.{/n}''', c("Read the next page.", "voices")),
    n("voices", "Narrator", '''{n}The next sheet is folded separately from the story.{/n}''',
      c("Read the two notes inside.", "two", requires=("targona.ran_trickster",)),
      c("Read the two notes inside.", "two", requires=("targona.ran_aeon",), forbids=("targona.ran_trickster",)),
      c("Read Targona's private note.", "personal", forbids=("targona.ran_trickster", "targona.ran_aeon"))),
    n("two", "Anograt", '''"Silver says I may write this part myself. An extraordinary concession, considering that I have been writing in the margins from the beginning.
"I like that you sent both versions back. I do not want to be the improved version of her either. If we disagree about a story, you are allowed to hear two opinions. You need not find the one that explains us both.
"My opinion is that Meret should keep the bad cup and use it to hold the collector's rejected adjectives. Eventually she could sell them. There is clearly a market."
{n}Targona's reply sits immediately below.{/n}
"I prefer the chipped blue cup. I also prefer Anograt saying what she thinks in her own name. We disagree about how much room the cup requires in the next chapter.
"Please continue addressing the letters to me. Add a page for her if you wish. She will still read over my shoulder, but I have found that asking is an improvement over discovering her conclusions already in the margin."''', c("Read Targona's final lines.", "personal")),
    n("personal", "Narrator", '''"There is something else I have wanted to say. I have spent a great deal of this correspondence asking you to look at difficult things. I do not want you to mistake that for the whole of what I want from you."
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
    n("friend", "Narrator", '''"I want to hear about something you enjoyed. It need not justify itself by improving the crusade. I have discovered that I like receiving news which nobody thought important enough to send before.
"I am glad our friendship has room for the difficult pages. I would also like to make room for bad stories, disagreements over cups, and the sort of complaint that becomes less serious when someone else reads it."
{n}She has enclosed another blank strip beneath the signature.{/n}
"For your unrelated complaint. I will do my best not to turn it into an uplifting account."
{n}You leave the strip beside your unfinished reply. It is too narrow for the complaint you have in mind. You fetch a larger sheet and begin with that.{/n}''',
      c("Send a personal reply and keep the correspondence open.", flags=("targona.extension_opening_kept",))),
], "targona.the_unscheduled_door")


s("the_open_threshold", "A door that opens both ways", [
    n("start", "Narrator", '''{n}Targona's letter carries the impression of a page opened and closed many times. She has drawn a small door beside the seal.{/n}
"My current post has put me at the Celestial Order's wayhouse just beyond Drezen's eastern road. The courier who brought this can carry your reply back there. It is on Golarion, and the road between it and the city is ordinary.
"I do want to see you. Before you answer, there is one risk you must state plainly if your Trickster idea involves more than the road. A newly made passage might shift, close, or fail to return someone to its other end. I will not cross an untested opening, and I will not be asked to accept a risk I have not heard. If we cannot make a safe route, I will stay here. Our letters continue, and neither of us owes the other an apology for that.
"If you would rather let the courier carry a simple invitation, say so. If you would rather decline the visit altogether, say that too. I mean what I wrote about wanting you. I do not mean that I have already agreed to every way of getting there."
{n}The invitation names the Drezen courtyard as the meeting point. The courier's dispatch slip carries the same wayhouse address as Targona's letter.{/n}
{n}Anograt's earlier note remains in the packet, but says nothing about this evening. You do not treat her silence as an invitation or a refusal; any shared invitation would need to reach her separately, with room for her own answer.{/n}''',
      c("[Trickster] Continue from the impossible extra door you drew on her page.", "paper_setup", requires=("trickster", "targona.extra_ending")),
      c("[Trickster] Use the ordinary courier route and a fortunate change of dispatch.", "courier_setup", requires=("trickster", "targona.ordinary_ending")),
      c("Decline the meeting tonight and keep the correspondence open.", "declined"),
      c("Answer that you will leave the letter in the courier's hands.", "ordinary", forbids=("trickster",))),
    n("paper_setup", "Narrator", '''{n}The impossible page is still with you. On its copy the door appears on both faces, and the short corridor refuses to end at the edge of the paper.{/n}
You do not treat this as a proven portal or as permission to reach into Targona's room. It is only a pattern your Trickster power has already made strange. You can try to use that contradiction to join two real, named places on the same plane: her wayhouse and the courtyard where you would meet.
First you must test the opening without sending anyone through it. If its ends will not stay where you put them, it does not become an invitation.''',
      c("[Knowledge (Arcana)] Test and stabilize both ends before inviting her.", check=dict(Skill="SkillKnowledgeArcana", DC=30, Success="steady", Failure="falter", CommanderOnly=True)),
      c("Do not risk a passage. Send an ordinary invitation by the known courier road.", "road")),
    n("courier_setup", "Narrator", '''{n}The ordinary page remains ordinary. You cannot claim it hid a door or that Targona's story has changed the world.{/n}
Instead, you use what the letters actually give you: a named wayhouse, a regular courier, and Targona's explicit wish to meet. Your Trickster intervention is a small, absurd correction in the dispatch chain. The courier who was meant to deliver a routine packet takes the wrong turn, finds your sealed invitation among the returns, and reaches Targona before her evening duty begins.
She writes back herself. She will walk the public road from the wayhouse to Drezen if you still want the meeting. No spell transports her; no fate trick makes her say yes. You can send that invitation, or keep the exchange in letters.''',
      c("Send the courier's invitation and let Targona choose the walk.", "road"),
      c("Do not send it. Keep the correspondence open.", "declined")),
    n("ordinary", "Narrator", '''{n}You do not make a magical route. You write that you will leave the invitation with the courier and let Targona decide whether to walk the road from her wayhouse.{/n}
She replies that she is not ready to make the visit. She is glad you asked without trying to turn her hesitation into a puzzle. You answer with an ordinary account of the day, including one detail too trivial for a military dispatch.
She sends back an equally small detail from hers. The romance and the letters remain as they were; tonight simply does not become a meeting.''',
      c("Send your answer and leave a later invitation to her.", flags=("targona.visit_correspondence",))),
    n("declined", "Narrator", '''{n}You send no portal and no courier invitation. Your reply says that you wanted to see her and are glad she told you what she does not want tonight.{/n}
Targona's answer is warm, if brief.
"Thank you for believing the answer. I still want you. I would like us to keep writing, and I may ask for another evening when I know what kind of one I want."
You send a private reply. Nothing in the letter changes the parent romance or withdraws the invitation to continue corresponding.''',
      c("Reply with affection and leave the next decision open.", flags=("targona.visit_correspondence",))),
    n("steady", "Narrator", '''{n}The two real anchors hold when you test the opening with an empty dispatch pouch, first from the wayhouse side and then from Drezen. The path returns to the same two places. It cannot wander into another room or plane, and your test shows it will remain open for the evening.{/n}
The known courier carries Targona a written account of the test, the way to close the passage, and the key. She reads the risk before she chooses. Her reply gives no promise that she must come; it only says she is willing to inspect the threshold herself.
When she arrives at the Drezen courtyard, she examines both anchors and keeps the key. The passage stays open behind her, an ordinary route home made briefly shorter. She has chosen to cross and may leave by the same tested way whenever she wants.''',
      c("Offer to walk beside her and let her choose where to begin.", "walk"),
      c("Ask whether she would rather close the passage and take the road home now.", "close_passage")),
    n("falter", "Narrator", '''{n}The first end shifts when you test it with the dispatch pouch. You close the opening before sending the courier, and before Targona is anywhere near it.{/n}
You send an ordinary letter explaining exactly what failed. You do not send the key, invite her to cross, or make her risk your mistake. Targona remains at the wayhouse and answers by the same reliable courier.
"That was the right choice. I still want you; I do not want to be the test of whether a dangerous passage works. Let us write tonight. We can speak of meeting again when there is a route worth trusting."
You reply with affection and a small report from your day. The failed attempt changes tonight's plan, not the relationship.''',
      c("Answer her and keep the correspondence open.", flags=("targona.visit_correspondence",))),
    n("road", "Narrator", '''{n}The courier carries your invitation to the Celestial Order's wayhouse. Targona reads the terms there and chooses to come by the public eastern road, on foot and at her own pace.{/n}
No spell moves her and no unstable gate closes behind her. She reaches the Drezen courtyard before the appointed hour and waits until you arrive.
"I wanted to see whether you would let the road be enough," she says. "It is. I would still like you to walk beside me."''',
      c("Walk with her and let her choose where to begin.", "walk"),
      c("Ask whether she would rather return to the wayhouse tonight.", "close_road")),
    n("walk", "Narrator", '''{n}You take the path around the courtyard rather than leading her through it. Targona chooses the slower walk along the wall, where the city noise thins and the evening air reaches the open edge of her wing.{/n}
You ask if the wing hurts today. She answers without apology: sometimes, and not now. Then she asks what you would have done if she had declined.
"Waited," you say. "Possibly complained to the nearest statue."
"Good. I would have disliked becoming responsible for your disappointment."
Her mouth curves. The joke has reached its mark, but not its end.
She tells you that she has spent too many years being looked at as a sign: proof of protection, proof of corruption, proof that some power can do what it claims. She likes that you look at her as a woman you desire. She dislikes when desire becomes another argument that she ought to be grateful.
"Then let me be precise," you say. "I want to kiss you. I do not think you owe me one."
She turns to face you. "That is precise enough. Ask me again when you are closer."
{n}You take one step. The rest belongs to her.{/n}''',
      c("Ask her again, and wait for her answer.", "kiss"),
      c("Tell her you would rather continue the walk.", "continue")),
    n("close_passage", "Narrator", '''{n}You ask whether she would rather close the tested passage and take the public road home now. Targona turns the key herself; the opening folds shut at the Drezen end.{/n}
"Yes. I would like to walk back while the evening is still quiet. I am glad we met, and I do not want to make staying longer a test of how much I want you."
You tell her you are glad she came, and do not ask her to reconsider. She offers you her arm for the walk to the eastern road.''',
      c("Walk with her to the road and say goodnight.", "departed")),
    n("close_road", "Narrator", '''{n}You ask whether she would rather return to the wayhouse tonight. Targona says yes; she would like to walk back while the evening is still quiet.{/n}
"I am glad we met. I do not want to make staying longer a test of how much I want you."
You tell her you are glad she came, and do not ask her to reconsider. She offers you her arm for the walk to the eastern road.''',
      c("Walk with her to the road and say goodnight.", "departed")),
    n("departed", "Narrator", '''{n}You walk her to the passage or to the road, according to the route she chose. Targona decides to return to the wayhouse before the evening is over.{/n}
She squeezes your hand before letting go.
"That is all I want tonight. I am glad we met. Please do not make the ending of an evening carry a promise for the next one."
You tell her you will not. Her return is uneventful; the route works exactly as agreed, and the familiar courier carries her note that she reached the wayhouse safely.''',
      c("Reply with affection and leave the next invitation open.", flags=("targona.visit_pause",))),
    n("kiss", "Narrator", '''{n}You ask her again. Targona's reply is to draw you close by the front of your coat and kiss you with a certainty that makes the careful question worth asking.{/n}
The kiss is warm, unhurried, and unmistakably hers. Her thumb rests beneath your jaw. When she lets you breathe, she keeps her brow against yours.
"I have missed that," she says. "I have missed wanting it without having to turn the want into evidence that I am well."
You tell her that you want her, including the wing she once wished she could regard without fear. You do not call it beautiful on her behalf. She searches your expression for the compliment you are trying not to force.
"You may desire me without making a sermon of it," she says. "And I may enjoy being desired without promising you that I have made peace with everything I see in the mirror."
Her palm slides to your chest, feeling the quickened beat beneath your clothes. She smiles at the proof of her effect.
"There. That is a much more useful response than another assurance."
She kisses you once more, then rests her forehead against your shoulder. For a little while neither of you has to explain what the evening means.
When she draws back, she asks whether you will spend the night talking, kissing, or finding out how much of that armor she is willing to unfasten. She makes clear that any answer can change when either of you wants it to.''',
      c("Choose the quiet of conversation and another kiss.", flags=("targona.visit_tender",)),
      c("Tell her you want to explore the desire between you, at her pace.", flags=("targona.visit_desire",)),
      c("Say that the invitation itself was enough for tonight.", flags=("targona.visit_pause",))),
    n("continue", "Narrator", '''{n}You tell her that a walk is enough. Targona leaves her fingers in your sleeve and chooses a path along the battlements, where the view opens over the city.{/n}
"I am glad you did not treat the invitation as a contract," she says. "I have spent enough of my life watching a decision become something other people believe they can collect from me."
You ask what she would like to do with the remaining hours.
"Walk until I am tired. Then eat something sweet enough to be imprudent. Then decide whether I want another kiss."
"That sounds like a plan."
"It is a proposal. Plans are what people make when they have already forgotten to ask me."
Her smile makes the correction gentler, not less serious. She tells you which of the city lights she can see from the terrace, and which she has mistaken for stars. You listen as the night deepens around the places she chooses to name.''',
      c("End the evening with affection and leave the next choice open.", flags=("targona.visit_tender",)),
      c("Ask if she would like that second kiss now.", "kiss")),
], "targona.what_she_keeps", delay=0, requires=("targona.ran_romance",))


s("the_key_remains_hers", "The key remains hers", [
    n("start", "Narrator", '''{n}Targona's next letter answers the choice you made about seeing her. One version contains a small brass key tied to the page with red thread; another is a page of ordinary news. Whatever form it takes, the decision about another meeting is hers to make.{/n}''',
      c("Read her answer after the intimate evening.", "desire", requires=("targona.visit_desire",)),
      c("Read her answer after the tender evening.", "tender", requires=("targona.visit_tender",)),
      c("Read her answer after you chose to pause.", "pause", requires=("targona.visit_pause",)),
      c("Read her answer to your letter.", "correspondence", requires=("targona.visit_correspondence",))),
    n("desire", "Narrator", '''{n}A small brass key is tied to the page with red thread. It is not a key to a lock you recognize; the note says it belongs to the path you opened.{/n}
"I kept it. I want the option of coming back without needing to ask you to make the first move every time.
"I have also been thinking about your question. I do want you. I want the warmth of you close to me, the sound you make when you stop trying to be clever, and the knowledge that you will hear me when I tell you to slow down. I am not embarrassed to write that. I am not promising that every night will feel as easy as the one we began.
"If you open the way again, do it because I said yes to this visit. I will tell you if I want something different next time. I expect you to do the same."
{n}She has left the last line blank, as if it belongs to the answer.{/n}''',
      c("Reply that her desire is welcome, and your answer will remain honest.", flags=("targona.key_reciprocal",)),
      c("Reply that you want to meet again, with no expectation of what happens.", flags=("targona.key_unpressured",))),
    n("tender", "Narrator", '''{n}A small brass key is folded into the letter. On its tag, in Targona's unmistakable hand, is written: ONLY IF I ASK.{/n}
"I have not forgotten that you let me choose the shape of the evening. I want another one. I also want to be able to arrive, kiss you, and then decide that is all I want. I am trying to write that without making it sound like a warning. It is not a warning. It is part of what makes the choice mine."
The line beneath her note is left open for an answer.''',
      c("Reply that you want her and will accept a changed answer without resentment.", flags=("targona.key_reciprocal",)),
      c("Reply that you want her company, and leave the rest for another day.", flags=("targona.key_unpressured",))),
    n("pause", "Narrator", '''{n}The letter contains no key. Targona writes that she was pleased you let the evening end without asking her to turn it into a promise.{/n}
"I still want you. I also want to be able to stop at a kiss, or to spend the whole time talking, without either of us treating that as an unfinished answer. If you are still willing to see me on those terms, I would like another evening."
She has added a small sketch of the courtyard, with the way in and out marked in equal-sized arrows.''',
      c("Tell her you want another evening and will let her set its pace.", flags=("targona.key_unpressured",)),
      c("Tell her you want to kiss her again when she asks.", flags=("targona.key_reciprocal",))),
    n("correspondence", "Narrator", '''{n}Targona's letter contains a short account of an uneventful afternoon and a question about a story you once sent her.{/n}
"We did not meet that evening. I was glad to receive a question I could answer freely, and I am glad you did not make my reply carry more than it said. I still want to continue our letters. I may ask about another visit when I know what I want from it."
She sends a recipe for a sweet she has recently learned to make. The measurements are exact. The instruction to wait before adding the last ingredient has been underlined twice.''',
      c("Reply with an ordinary detail and keep the conversation open.", flags=("targona.key_unpressured",))),
], "targona.the_open_threshold", requires=("targona.ran_romance",))

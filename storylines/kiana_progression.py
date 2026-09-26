"""Opt-in continuation of old farewells and a decision after the developed route."""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, nodes, requires, forbids=(), delay=48, **extra):
    for page in nodes:
        page["Portrait"] = "Kiana"
    SCENES.append(scene("kiana." + id, title, "Kiana", 5, "", nodes,
                        Relationship="kiana", Remote=True, Chapters=[5], Areas=[DREZEN],
                        requires=("seelah.souls_returned", "kiana.lovers", "kiana.morning", *requires),
                        forbids=("kiana.closed", "inhuman", *forbids), delay=delay, optional=True, **extra))


s("another_page", "There is still time to answer", [
    n("start", "Narrator", '''{n}Kiana's folded farewell page is still among the things you have kept. There is room on it for an invitation of your own.{/n}
{n}You could write to ask for another ordinary evening in Drezen. The things you have already said would remain said. There would simply be time for more.{/n}''',
      c('[Write to ask whether she would like to continue your evenings together.]', "reply"),
      c('[Keep the page as it is. You can write another time.]', abort=True)),
    n("reply", "Narrator", '''{n}Her answer arrives on a scrap cut from a larger sheet.{/n}
"Yes. I have been finding things to do, some of them badly. I would enjoy having you here for a few of the attempts."
{n}Beneath that, in smaller writing:{/n}
"You needn't bring the farewell back. I meant it when I gave it to you. I also mean this invitation. It is very inconvenient to be limited to one kind of evening."''',
      c('[Keep the invitation and make time for her next letter.]', flags=("kiana.catchup_requested",))),
], requires=("kiana.farewell",), forbids=("kiana.future_settled",), delay=0, ManualOnly=True)


s("a_place_afterward", "The promise after the evenings", [
    n("start", "Kiana", '''{n}Kiana has written two lists on opposite sides of the same page. One concerns the next month. The other has only a heading: Afterward.{/n}
"I tried putting everything on one side. It looked very impressive until I realized I had promised the baker an afternoon sometime after the defeat of evil. She prefers a day of the week."
{n}She turns the page toward you.{/n}
"We have managed some actual evenings. There is a room I can work in, and people who ask what I am writing. I want to decide where you belong in what comes next. I would rather ask than keep an empty place and resent you for not guessing its size."''',
      c('"Then let us talk about what we want now."', "history"),
      c('[Ask to return when you can give the question your attention.]', abort=True)),
    n("history", "Narrator", '''{n}She puts the list down. This is something she wants to say without arranging it first into neat lines.{/n}''',
      c('[Listen as she speaks about the life she is making after the separation.]', "separated", requires=("kiana.separated",), forbids=("kiana.bereaved", "seelah.elan_dead")),
      c('[Listen as she speaks about the life she is making after Elan.]', "bereaved", requires=("kiana.bereaved", "seelah.elan_dead"), forbids=("kiana.separated",))),
    n("separated", "Kiana", '''"When Elan and I separated, I could tell you what I couldn't promise him. It took longer to find things I wanted to do after saying it."
{n}She looks toward the picture she kept.{/n}
"I have not finished being sad about parts of that life. I don't wish I had never loved him. I also don't want you waiting outside every memory until I decide it is safe to let you in."
"I haven't asked you to put the picture away."
"I know. You have been here while I was busy with other things. I wanted to notice that, for once, without turning it into a test you had passed."
{n}She turns back toward the page.{/n}''', c('[Ask what she wants to put beside your name.]', "promise")),
    n("bereaved", "Kiana", '''"There are still mornings when I want to tell Elan something before I remember. I expect there will be more."
{n}Her hands rest flat on the page.{/n}
"There are mornings when I wonder whether you will enjoy the ridiculous thing I wrote. They can be the same morning. I don't want to keep waiting for one of those thoughts to disappear before I make a plan."
"What would you like to plan?"
"Something that contains you because I want you there. I am tired of introducing every wish with an explanation of why I am allowed to have it."
{n}She picks up the pen, considers it, and puts it down again.{/n}
"I shall need to hear your answer before I write anything."''', c('[Tell her you are listening.]', "promise")),
    n("promise", "Kiana", '''"I want more evenings. I would like to make plans far enough ahead that I occasionally have to change them. I don't want a place in your life that exists only when nothing more important has asked for the time."
{n}She smiles briefly.{/n}
"I am aware that the world has been making extravagant demands. I mean afterward too."
{n}She leaves the pen alone.{/n}''',
      c('"I meant the promise I made. I want to keep building this life with you."', "renew", requires=("kiana.committed",)),
      c('"I could not promise it before. I can now. I want you in my life after the war."', "choose", forbids=("kiana.committed",)),
      c('"I want this relationship to continue. I still cannot promise a whole life after the war."', "open", forbids=("kiana.committed",)),
      c('"I have cared about these evenings. I do not want to promise a relationship I cannot continue."', "part")),
    n("renew", "Kiana", '''"Good. I wanted to hear it after we had discovered how much of a life is made of arrangements that refuse to stay arranged."
{n}She turns the page over and writes your name below the heading.{/n}
"Not an appointment. I shall put those on the sensible side. This is to remind me whom I meant to ask when I have decided where I want to go."
"And if I cannot come?"
"Then tell me. We will choose another time, or I shall go without you and bring back an unreasonable account of what you missed."
{n}She leaves room beneath your name for something she has not decided yet.{/n}''', c('[Reaffirm the promise without surrendering either of your other relationships.]', "end", flags=("kiana.committed",))),
    n("choose", "Kiana", '''{n}She starts to answer, then takes a breath and tries again.{/n}
"Yes. That is what I wanted."
{n}She reaches for your hand before she reaches for the pen.{/n}
"I liked having you here while the answer was smaller. I don't wish those evenings away because you can say something more now."
"Neither do I."
"Then we shall keep them. And make more. I reserve the right to remind you that I was very patient about your handwriting."
{n}She writes your name beneath Afterward, smiling at the space she has left around it.{/n}''', c('[Make the promise now that you know what you have been choosing together.]', "end", flags=("kiana.committed",))),
    n("open", "Kiana", '''{n}Kiana draws the page back toward herself. For a while she looks at the empty heading.{/n}
"I would have liked the larger answer. I won't pretend otherwise."
"I know."
"But I want to keep seeing you. I can make that choice without calling it a rehearsal for a promise you haven't made."
{n}She turns to the first side and puts your name beside an evening.{/n}
"Tell me when that changes. I will tell you if this stops being enough for me. We needn't stop enjoying it in advance."
{n}She taps the date with the end of the pen.{/n}
"This one is real. I expect you to be hungry. I have been advised that not every supper needs to become a discussion."''', c('[Choose to continue the relationship without a lasting promise.]', "end", flags=("kiana.future_open",))),
    n("part", "Kiana", '''{n}Kiana folds the page with its blank side inward.{/n}
"Then I am glad I asked before I put your name there."
{n}She stays where she is. The pen lies between you, unused.{/n}
"I liked those evenings. Tonight I don't want to make them into something that proves either of us should stay. Please go. I will decide what to do with the next one myself."''', c('[Leave the relationship, keeping its history intact.]', flags=("kiana.closed", "kiana.future_settled"))),
    n("end", "Kiana", '''{n}She puts the page away and brings out a loaf wrapped in a clean cloth.{/n}
"I bought enough for two possible answers. One of them would have left me eating a great deal of bread."
"You could have invited someone else."
"I could. Tonight I wanted you. Sit down."
{n}You help set the table. The list stays folded while she tells you something that happened on the stairs, and gets annoyed when you guess the ending before she has finished.{/n}''', c('[Stay for the evening you have chosen.]', flags=("kiana.future_settled",))),
], requires=("kiana.followthrough_kept",), forbids=("kiana.farewell",),
   ForbidOverrides={"kiana.farewell": "kiana.catchup_requested"})


def ending(id, text, requires=(), forbids=(), owner="Epilogue"):
    SCENES.append(scene("kiana.ending_" + id, "The princess writes her own part", owner, 5, "", [
        n("start", "Narrator", text, c(), portrait="Kiana"),
    ], Relationship="kiana", last=99, requires=requires, forbids=forbids))


ending("open", '''{n}Kiana and the Commander continued to arrange evenings rather than promise a shared lifetime. Sometimes the arrangement was difficult to keep. They learned to send an answer before an empty chair became an argument.{/n}
{n}Her writing had readers and a place among the other things she wanted to do. She did not wait for the Commander to be free before making every plan. When they were together, she had things to tell and occasionally a part to offer in whatever she was trying next.{/n}
{n}Neither called the relationship unfinished merely because its future was not promised. They kept asking, and for as long as they both wanted it, they kept coming back.{/n}''',
       requires=("kiana.future_settled", "kiana.future_open"), forbids=("kiana.closed", "kiana.committed", "ascended"))

ending("open_ascended", '''{n}Kiana and the Commander had chosen to continue without promising a shared lifetime. When divinity intervened, she did not pretend it had supplied the promise they had left unmade.{/n}
{n}She kept writing. Some letters concerned a reading; others asked whether their next conversation might occur before she had forgotten what she intended to say. She also had evenings for which she invited people who could reliably reach her door.{/n}
{n}The relationship continued through the invitations they actually answered. Kiana had enough work maintaining a fictional princess to attempt building a religion around her own private life.{/n}''',
       requires=("kiana.future_settled", "kiana.future_open", "ascended"), forbids=("kiana.closed", "kiana.committed"))

ending("promised", '''{n}The Commander had promised Kiana a place in the life after the war. The promise had been made sincerely; there was still much they had not learned about keeping it.{/n}
{n}Kiana returned to her pages and to the people she knew in Drezen. She sent invitations when she wanted company. She would not spend every evening waiting beside an unwritten answer.{/n}
{n}What they had begun remained a promise to be tried, rather than a life the two had already built.{/n}''',
       requires=("kiana.committed",), forbids=("kiana.closed", "kiana.future_settled"))

ending("open_aeon", '''{n}The evenings Kiana and the Commander had chosen together belonged to a history that no longer held the world in place. They had made no promise that could require the new world to restore them.{/n}
{n}Kiana had other choices ahead of her. Somewhere in that unwritten life there might still be a woman impatient to finish a page and go out for the evening.{/n}''',
       requires=("kiana.future_settled", "kiana.future_open"), forbids=("kiana.closed", "kiana.committed"), owner="AeonEpilogue")

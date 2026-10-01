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
{n}There is still room beneath Kiana's farewell for an invitation to supper.{/n}''',
      c('[Write to ask whether she would like to continue your evenings together.]', "reply"),
      c('[Keep the page as it is. You can write another time.]', abort=True)),
    n("reply", "Narrator", '''{n}Her answer arrives on a scrap cut from a larger sheet.{/n}
"Yes. I have been finding things to do, some of them badly. I would enjoy having you here for a few of the attempts."
{n}Beneath that, in smaller writing:{/n}
"Leave the farewell at home. I want another evening, and I have several much less solemn lines prepared."''',
      c('[Keep the invitation and make time for her next letter.]', flags=("kiana.catchup_requested",))),
], requires=("kiana.farewell",), forbids=("kiana.future_settled",), delay=0, ManualOnly=True)


s("a_place_afterward", "The promise after the evenings", [
    n("start", "Kiana", '''{n}Kiana has written two lists on opposite sides of the same page. One concerns the next month. The other has only a heading: Afterward.{/n}
"I tried putting everything on one side. It looked very impressive until I realized I had promised the baker an afternoon sometime after the defeat of evil. She prefers a day of the week."
{n}She turns the page toward you.{/n}
"I have a room and readers now. I want you beside me after the war. Must I steal another moon to make you answer?"''',
      c('"Ask me, Kiana."', "history"),
      c('[Ask to return when you can give the question your attention.]', abort=True)),
    n("history", "Narrator", '''{n}She sets down the list and meets your eyes.{/n}''',
      c('[Listen as she speaks about the life she is making after the separation.]', "separated", requires=("kiana.separated",), forbids=("kiana.bereaved", "seelah.elan_dead")),
      c('[Listen as she speaks about the life she is making after Elan.]', "bereaved", requires=("kiana.bereaved", "seelah.elan_dead"), forbids=("kiana.separated",))),
    n("separated", "Kiana", '''"After I left Elan, I spent a week staring at this wall. Then I remembered I had a princess to ruin."
{n}She looks toward the picture she kept.{/n}
"I still miss things about that marriage. Come in anyway; there is room beside the picture."
"I haven't asked you to put the picture away."
"I know. You even endured the princess's dreadful third speech. I have not forgotten."
{n}She turns back toward the page.{/n}''', c('[Ask what she wants to put beside your name.]', "promise")),
    n("bereaved", "Kiana", '''"There are still mornings when I want to tell Elan something before I remember. I expect there will be more."
{n}Her hands rest flat on the page.{/n}
"Some mornings I remember Elan and want to laugh with you. An inconveniently crowded morning, but mine."
"What would you like to plan?"
"I want you there. I refuse to spend another sheet explaining why."
{n}She picks up the pen, considers it, and puts it down again.{/n}
"I shall need to hear your answer before I write anything."''', c('[Tell her you are listening.]', "promise")),
    n("promise", "Kiana", '''"I want you after the war too. More suppers, more scandal, and fewer excuses about a general's schedule."
{n}She smiles briefly.{/n}
"I am aware that the world has been making extravagant demands. I mean afterward too."
{n}She leaves the pen alone.{/n}''',
      c('"I promised to come back. I meant it."', "renew", requires=("kiana.committed",)),
      c('"I could not promise it before. I can now. I want you in my life after the war."', "choose", forbids=("kiana.committed",)),
      c('"I want more evenings with you. I cannot promise you the rest of my life."', "open", forbids=("kiana.committed",)),
      c('"I have loved these evenings. I cannot stay with you."', "part")),
    n("renew", "Kiana", '''"Good. I wanted to hear it after we had discovered how much of a life is made of arrangements that refuse to stay arranged."
{n}She turns the page over and writes your name below the heading.{/n}
"Not an appointment. I shall put those on the sensible side. This is to remind me whom I meant to ask when I have decided where I want to go."
"And if I cannot come?"
"Then tell me. We will choose another time, or I shall go without you and bring back an unreasonable account of what you missed."
{n}She leaves room beneath your name for something she has not decided yet.{/n}''', c('[Take her hand and promise to keep the evening.]', "end", flags=("kiana.committed",))),
    n("choose", "Kiana", '''{n}She starts to answer, then takes a breath and tries again.{/n}
"Yes. That is what I wanted."
{n}She reaches for your hand before she reaches for the pen.{/n}
"I enjoyed every stolen evening. This is an excellent excuse to steal more."
"Neither do I."
"Then we shall keep them. And make more. I reserve the right to remind you that I was very patient about your handwriting."
{n}She writes your name beneath Afterward, smiling at the space she has left around it.{/n}''', c('[Promise to return after the war.]', "end", flags=("kiana.committed",))),
    n("open", "Kiana", '''{n}Kiana draws the page back toward herself. For a while she looks at the empty heading.{/n}
"I would have liked the larger answer. I won't pretend otherwise."
"I know."
"Then come again. I shall buy another pair of offensively long candles."
{n}She turns to the first side and puts your name beside an evening.{/n}
"Come for supper. If I want more, you will hear of it; subtlety has never served me well."
{n}She taps the date with the end of the pen.{/n}
"This one is real. I expect you to be hungry. I have been advised that not every supper needs to become a discussion."''', c('[Promise her another evening.]', "end", flags=("kiana.future_open",))),
    n("part", "Kiana", '''{n}Kiana folds the page with its blank side inward.{/n}
"Then I am glad I asked before I put your name there."
{n}She stays where she is. The pen lies between you, unused.{/n}
"I liked those evenings. Tonight I want you to go before I begin begging, and hate us both for it."''', c('[Say goodbye and leave.]', flags=("kiana.closed", "kiana.future_settled"))),
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
{n}Kiana kept buying long candles and writing invitations the Commander found impossible to ignore.{/n}''',
       requires=("kiana.future_settled", "kiana.future_open"), forbids=("kiana.closed", "kiana.committed", "ascended"))

ending("open_ascended", '''{n}Even divinity failed to cure the Commander's habit of answering Kiana's invitations late.{/n}
{n}She kept writing. Some letters concerned a reading; others asked whether their next conversation might occur before she had forgotten what she intended to say. She also had evenings for which she invited people who could reliably reach her door.{/n}
{n}The relationship continued through the invitations they actually answered. Kiana had enough work maintaining a fictional princess to attempt building a religion around her own private life.{/n}''',
       requires=("kiana.future_settled", "kiana.future_open", "ascended"), forbids=("kiana.closed", "kiana.committed"))

ending("promised", '''{n}The Commander had promised to return after the war; Kiana furnished the spare chair and complained about the delay.{/n}
{n}Kiana returned to her pages and to the people she knew in Drezen. She sent invitations when she wanted company. She would not spend every evening waiting beside an unwritten answer.{/n}
{n}She still kept that chair, though she threatened to give it to somebody with better manners.{/n}''',
       requires=("kiana.committed",), forbids=("kiana.closed", "kiana.future_settled"))

ending("open_aeon", '''{n}The rewritten world held no trace of those suppers or of the absurd princess who had summoned the Commander to them.{/n}
{n}Kiana had other choices ahead of her. Somewhere in that unwritten life there might still be a woman impatient to finish a page and go out for the evening.{/n}''',
       requires=("kiana.future_settled", "kiana.future_open"), forbids=("kiana.closed", "kiana.committed"), owner="AeonEpilogue")

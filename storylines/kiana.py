"""Kiana after the native soul-quest aftermath.

New book events stage her invitations; native one-shot conversations stay intact.
Pre-wedding courtship and restoration of inaccessible outcomes remain separate work.
"""
from story_format import c, n, scene

RELATIONSHIP = dict(
    Title="The princess writes her own part",
    Description="Kiana has sent me a page from an unfinished play. She has left the last line blank and asked me not to be sensible about it.",
    Objective="Answer Kiana's invitations",
    Guidance="After the soul quest and your conversation with Kiana, her invitations arrive during quiet rests in Drezen. Give her time between meetings. Her marriage or bereavement remains part of her story.",
    StartedFlag="kiana.started", ClosedFlag="kiana.closed", CommittedFlag="kiana.committed",
    UnavailableFlags=[], FailureFlags=[],
)
SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, nodes, requires=(), forbids=(), delay=48, optional=False, **extra):
    for page in nodes:
        if not page["Portrait"]:
            page["Portrait"] = "Seelah" if page["Speaker"] == "Seelah" else "Kiana"
    SCENES.append(scene("kiana." + id, title, "Kiana", 5, "", nodes,
                        Relationship="kiana", Remote=True, Chapters=[5], Areas=[DREZEN],
                        requires=("seelah.souls_returned",) + requires,
                        forbids=forbids, delay=delay, optional=optional, **extra))


s("invitation", "One unfinished sentence", [
    n("start", "Narrator", '''{n}A folded page waits among your letters. Its first line announces that the vampire princess has dismissed her entire court for being insufficiently mysterious. Its last line is blank.{/n}
{n}Kiana has added a note: I am trying to finish something pleasant. Give me an ending. No speeches about duty, please. I hear enough of those.{/n}''',
      c('[Write: The princess stole the moon and discovered she had nowhere to put it.]', "reply", flags=("kiana.moon",)),
      c('[Write: She locked the doors and asked one guest to stay.]', "reply", flags=("kiana.guest",)),
      c('[Put the page aside to answer another day.]', abort=True)),
    n("reply", "Narrator", '''{n}You send the page back. Several lines of military correspondence await your attention, all considerably less concerned with the difficulties of being a vampire princess.{/n}''',
      c('[Leave room in your schedule for her reply.]', flags=("kiana.started",))),
], requires=("kiana.aftermath_seen",), delay=0)

s("rehearsal", "A very unsuitable castle", [
    n("start", "Kiana", '''{n}Kiana's invitation brings you to a borrowed room in Drezen. Someone has pinned dark fabric over a shelf. The candles beside it are unlit.{/n}
"My castle. It was a storeroom this morning. Please admire the transformation before you notice the onions."
{n}She holds your returned page by its corners.{/n}''',
      c('"How does a princess store a stolen moon?"', "moon", requires=("kiana.moon",)),
      c('"Did the guest stay?"', "guest", requires=("kiana.guest",))),
    n("moon", "Kiana", '''"Badly. Her subjects keep asking why the soup glows."
{n}Her smile comes easily, then falters as she looks at the empty chairs.{/n}
"I wanted to invite people. I got as far as arranging the room. Then I couldn't bear the thought of everybody trying to have a good time for my benefit."''', c('"We can leave the chairs empty tonight."', "company")),
    n("guest", "Kiana", '''"I haven't decided. The princess is an excellent hostess, but the castle has dreadful plumbing."
{n}She sets the page down beside the unlit candles.{/n}
"I meant to invite a few people. Somehow asking one person was easier."''', c('"Then one person will have to supply the applause."', "company")),
    n("company", "Kiana", '''"You may applaud the onions. They have been very patient."
{n}She pulls a chair up to the table. The grand performance becomes two people reading a ridiculous story aloud, stopping whenever one of them loses the thread.{/n}''',
      c('[Stay until she is ready to finish.]', flags=("kiana.company",))),
], requires=("kiana.invitation",))

s("stagecraft", "The trouble with an entrance", [
    n("start", "Kiana", '''{n}The door to Kiana's borrowed castle stands open. A strip of cloth lies across the threshold. On the table, a paper moon rests beneath a bowl of onions.{/n}
"Stop there. That is a cliff."
{n}Kiana peers at you over her script.{/n}
"I told the porter, and he stepped over it without a word. You would think people encountered cliffs in storerooms every day. Now, you have come to demand the return of the moon. Try to sound as though the journey was inconvenient."
{n}She waits, plainly enjoying the prospect of giving you instructions.{/n}''',
      c('"I have climbed seven mountains, crossed a desert, and been directed to the wrong staircase twice."', "play"),
      c('"Would you like the Commander, or someone who has never commanded anything?"', "ordinary"),
      c('"I came to see you. Must I audition first?"', "complaint"),
      c('[Tell her you cannot stay, and arrange another time.]', abort=True)),
    n("play", "Kiana", '''"The east staircase? Everyone does that. The skeleton at the bottom gives dreadful directions."
{n}She adopts a lofty expression, but a laugh escapes before she can finish her next line.{/n}
"No, wait. I can do this. I practiced while the porter was here. He was a very respectful audience, considering I was standing on the sack he wanted."
{n}She starts again, one hand extended toward the stolen moon.{/n}
"You have found my castle. What makes you think you may leave it?"''', c('"Your skeleton gave me directions back as well."', "laugh")),
    n("ordinary", "Kiana", '''"A roof mender, then. Someone who has never commanded anything. I know what the Commander sounds like."
{n}She considers you, then turns a page backward.{/n}
"You mend roofs. Without the moon, you can't find your tools when you drop them in the dark. That is your complaint. You don't know whether I can turn you into a bat, and you rather suspect I can."
{n}She puts down the script.{/n}
"There. Now I have to frighten somebody who isn't impressed by a title."''', c('"My lady, if you turn me into a bat, you will have to mend your own roof."', "laugh")),
    n("complaint", "Kiana", '''"Yes. I am extremely difficult to visit. First the cliff, then the audition, then you have to say something complimentary about the scenery."
{n}She lowers the pages enough for you to see her smile.{/n}
"You may sit down and watch, if you'd rather. But I want to try this aloud. It keeps sounding magnificent in my head and rather silly when I say it."''',
      c('"Then let us find out which lines survive."', "ordinary"),
      c('[Sit down and listen to her perform the entrance.]', "listen")),
    n("laugh", "Kiana", '''{n}Kiana loses the princess completely. She braces a hand on the table and laughs, while the moon slides out from beneath its bowl.{/n}
"Don't make that face. You knew exactly what you were doing."
{n}She catches the paper before it reaches the floor and studies the crease running through it.{/n}
"The trouble is, I like your line better. Mine was supposed to make the room go quiet."
{n}She tries her threat again. Without your interruption, its last few words linger in the little room.{/n}
"Well?"''',
      c('"Keep the threat. I will stop trying to win the scene."', "threat"),
      c('"Let her be funny. She can still be dangerous."', "comedy")),
    n("listen", "Kiana", '''{n}She makes her entrance from behind the hanging cloth. The first attempt catches a sleeve on the shelf. On the second she forgets the line. On the third, she speaks so quietly that you lean forward to hear the threat.{/n}
{n}Kiana holds the silence a moment longer, then looks at you expectantly.{/n}
"That one? Or are you simply being polite because you hope I'll let you go home?"''',
      c('"That one. Leave them waiting for the next word."', "threat"),
      c('"I liked the sleeve. The princess has a terrible castle and refuses to admit it."', "comedy")),
    n("threat", "Kiana", '''"Good. I wanted to keep it."
{n}She writes a note beside the line, then gives you a suspicious look.{/n}
"You are allowed to disagree, you know. But if you make me laugh halfway through this next attempt, I'm starting again."
{n}The next time she makes her entrance, you let her finish. She watches you watching her, and this time she remembers every word.{/n}''',
      c('[Help her rehearse the rest of the scene.]', "end", flags=("kiana.quiet_entrance",))),
    n("comedy", "Kiana", '''"Perhaps she bought the castle without visiting it first."
{n}Kiana looks around the storeroom with renewed interest.{/n}
"A thousand years of darkness. Rising damp. No one mentions the rising damp when they promise you a thousand years of darkness."
{n}She tries the entrance again, letting her sleeve catch on the shelf and then rescuing it without a glance. You laugh. This time she is ready, and waits for you to finish before delivering the threat.{/n}''',
      c('[Help her rehearse the rest of the scene.]', "end", flags=("kiana.comic_entrance",))),
    n("end", "Kiana", '''{n}Eventually she marks a place in the script and sets it down. You help her fold the hanging cloth. The castle becomes a storeroom again, though she leaves the paper moon on the table.{/n}
"Next time, you can choose the part. I reserve the right to complain about your direction."
{n}At the door she glances down at the strip of cloth, then steps over it with exaggerated care.{/n}
"Mind the cliff on your way out. I'd hate to have to find another audience."''',
      c('[Step carefully over the cliff.]', flags=("kiana.rehearsed",))),
], requires=("kiana.company",), forbids=("kiana.farewell_kept",), optional=True)

s("marriage", "The person in the room", [
    n("start", "Kiana", '''"Elan asked what I was writing. I told him about the princess and your terrible ending. He laughed."
{n}Kiana folds the page once, then smooths it flat again.{/n}
"I liked telling him. I also left out how often I've been hoping you would answer. That bothered me afterward."''',
      c('"I have been hoping for your letters too."', "attraction"),
      c('"Then let us keep this a friendship you can speak about freely."', "friends")),
    n("attraction", "Kiana", '''"There. Now we've said something we can't pretend was about the play."
{n}She looks directly at you.{/n}
"He is a good man. He has not earned an unfaithful wife by being away, and I haven't stopped loving him because I like the way you look at me. I need to work out what that means before I make promises to anyone."''',
      c('"Speak to him first. I want you, but I can wait."', "wait", flags=("kiana.waited",)),
      c('[If she wants it, offer one kiss before you part.]', "kiss", forbids=("inhuman",)),
      c('"I would rather stop here than ask you to make that choice."', "friends")),
    n("kiss", "Kiana", '''{n}Kiana comes closer. She pauses within reach, watches your face, then kisses you. Her fingers close briefly around your sleeve.{/n}
{n}When she steps away, she does not smile.{/n}
"I wanted that. I won't tell him it simply happened to me."
{n}She collects her pages, leaving yours until last.{/n}
"No second secret. I need to speak to him."''', c('[Let her go.]', flags=("kiana.attracted", "kiana.affair",))),
    n("wait", "Kiana", '''"Please do. And let me be the one who tells him. He deserves to hear it from his wife."
{n}She picks up the pages without offering you another to take home.{/n}''', c('[Give her time.]', flags=("kiana.attracted",))),
    n("friends", "Kiana", '''{n}She lets out a breath.{/n}
"All right. We can still give the princess a scandalous life. She has fewer people to hurt."
{n}She turns the page and asks what you think should happen next.{/n}''', c('[Keep the friendship.]', flags=("kiana.closed",))),
], requires=("kiana.company",), forbids=("seelah.elan_dead",))

s("widow", "An evening she chose", [
    n("start", "Kiana", '''{n}When Kiana next asks you back, she has lit one candle in the borrowed castle.{/n}
"I laughed at something yesterday and wanted to tell Elan. I had almost turned around before I remembered."
{n}She straightens the candle, though it was already standing evenly.{/n}
"I don't want every evening to be about him. I don't want people to decide that means he mattered less, either."''',
      c('"You can tell me about him when you want to."', "room"),
      c('"What would you like this evening to be about?"', "room")),
    n("room", "Kiana", '''"A woman with an unfinished play and a guest she is beginning to look forward to seeing."
{n}Her gaze stays on you.{/n}
"I think I might want more than company. Slowly. I am allowed to be uncertain about it, aren't I?"''',
      c('"So am I. We can find out together."', "try"),
      c('"I would like to stay your friend."', "friend")),
    n("try", "Kiana", '''{n}She pushes a page toward you.{/n}
"Then read this part. The guest is supposed to be irresistible. I want to hear how you manage it without sounding terribly pleased with yourself."
{n}Her next laugh surprises her. She lets it finish.{/n}''', c('[Read with her.]', flags=("kiana.attracted", "kiana.available", "kiana.bereaved",))),
    n("friend", "Kiana", '''"I'd like that. Stay for the reading, then. I still need someone willing to say the embarrassing lines."''', c('[Stay as her friend.]', flags=("kiana.closed",))),
], requires=("kiana.company", "seelah.elan_dead"), delay=168)

s("answer", "No second secret", [
    n("start", "Kiana", '''{n}Kiana sends for you without enclosing a page of the play. When you arrive, she has a small travel case by her chair.{/n}
"I've spoken to Elan. I'm staying with a friend for a while."
{n}She touches the case with her foot, as if checking that it is still there.{/n}
"He asked whether I wanted him to stop fighting. I told him this wasn't a punishment for leaving to do his duty. That would have been an easier conversation, I think."''',
      c('"Did you tell him about the kiss?"', "truth", requires=("kiana.affair",)),
      c('"What did you tell him you wanted?"', "apart", forbids=("kiana.affair",))),
    n("truth", "Kiana", '''"Yes. He asked me twice. I answered twice."
{n}She presses her lips together.{/n}
"He said he wished I'd spoken before I kissed you. I could hardly argue. I don't want you to call him small-minded for being hurt."''',
      c('"He is right about that. I chose it too."', "apart", flags=("kiana.owned_hurt",)),
      c('"I will not ask you to defend me to him."', "apart", flags=("kiana.owned_hurt",))),
    n("apart", "Kiana", '''"I told him I couldn't keep promising the marriage we had planned. He wants a wife who can make that promise. I want to find out what I can choose without making it for somebody else's sake."
{n}She looks tired. There is relief in her voice, but no triumph.{/n}
"We are separating. There will be practical things to settle. I haven't asked you here to move my case into your room."''',
      c('"Tell me where you want it taken. Then take the time you need."', "later")),
    n("later", "Kiana", '''"My friend has already arranged that. Tonight, I wanted you to know why I haven't written."
{n}She rests her hands in her lap.{/n}
"When I invite you again, it will be because I want to see you. That is all I can promise yet."''',
      c('[Leave the next invitation to her.]', flags=("kiana.available", "kiana.separated",))),
], requires=("kiana.marriage", "kiana.attracted"), forbids=("seelah.elan_dead",), delay=120)

s("date", "The guest stays", [
    n("start", "Kiana", '''{n}The next invitation is written in Kiana's most elaborate hand: One guest. No court. Bring no speeches.{/n}
{n}She meets you in her borrowed castle, wearing a dark dress with a ribbon at the throat. The onions have been removed.{/n}
"I thought we could manage an evening without deciding the whole future. I have been rather bad at those lately."''',
      c('"Have you decided what the princess wants?"', "want", forbids=("inhuman",)),
      c('"You look beautiful."', "dress", forbids=("inhuman",)),
      c('"I hardly resemble the guest you first imagined."', "changed", requires=("inhuman",))),
    n("changed", "Kiana", '''"No. And I can't make this easy by pretending you are wearing a costume."
{n}Kiana leaves space between you. Her hands are steady, though she has stopped playing with the ribbon at her throat.{/n}
"I used to laugh at things that frightened me. Sometimes that helped. Sometimes I was simply frightened and laughing."
{n}She draws a chair to the other side of the table.{/n}
"Tonight I want to hear you. We stay here and talk. If the scene needs a wider stage, the leading lady will move her chair, and the audience will pretend not to notice. I have performed brave for half of Drezen. You get the rehearsal, lines fluffed and all."''',
      c('"Then we begin with your voice, and mine."', "want")),
    n("dress", "Kiana", '''"Thank you. I tried on three dresses before choosing the first. You are getting a very carefully arranged appearance of spontaneity."
{n}She turns once so you can admire the result, then comes back to you.{/n}''', c('"What happens when the guest is thoroughly impressed?"', "want")),
    n("want", "Kiana", '''"Here is what I want."
{n}Kiana waits until she has your attention before continuing.{/n}
"I want this evening with you. And the next one, if you have it. I am asking you to answer my letters, and to turn up when you say you will. An actress can forgive anything but an empty seat she was promised."''',
      c('"I can promise that."', "close"),
      c('"I cannot promise a relationship. I should have said so sooner."', "stop")),
    n("close", "Kiana", '''"Good. Then you may be charming again. I was beginning to miss it."
{n}Her smile is a little unsteady now that the evening is no longer make-believe.{/n}''',
      c('[Kiss her.]', "kiss", forbids=("inhuman",)),
      c('"Stay beside me. I want to hear the rest in your own voice."', "read", forbids=("inhuman",)),
      c('"I want to hear the rest in your own voice. Stay where you are comfortable."', "distance", requires=("inhuman",))),
    n("kiss", "Kiana", '''{n}She meets you halfway. This kiss lasts until she begins to smile against your mouth.{/n}
"I had a much better line prepared. I can't remember it now."
{n}She does not go looking for the script.{/n}''', c('[Spend the evening together.]', flags=("kiana.lovers", "kiana.kissed",))),
    n("read", "Kiana", '''{n}She settles beside you, leaving the page on the table.{/n}
"The guest stayed. The princess forgot to be mysterious. It was an improvement."
{n}There is no audience to please. She tells you about her day, and asks about yours.{/n}''', c('[Spend the evening together.]', flags=("kiana.lovers",))),
    n("distance", "Kiana", '''{n}Kiana stays in the chair she chose across the table. After a while, she stops glancing at the space between you.{/n}
"I want to change the ending. The guest doesn't have to sweep her off her feet. Perhaps the princess has had enough of being swept anywhere."
{n}She turns the page toward you and reads. Her voice grows less careful as the evening passes.{/n}''', c('[Listen, and spend the evening with her.]', flags=("kiana.lovers",))),
    n("stop", "Kiana", '''"Yes. You should have."
{n}She takes a moment before she answers the rest.{/n}
"Thank you for saying it now. I would like the evening to myself."''', c('[Respect her decision.]', flags=("kiana.closed",))),
], requires=("kiana.available",), delay=168)

s("morning", "An ordinary difficulty", [
    n("start", "Kiana", '''{n}Kiana has put the play aside. There is something else she wants to tell you before you begin reading.{/n}''',
      c('[Listen.]', "bereaved", requires=("kiana.bereaved",)),
      c('[Listen.]', "settling", requires=("kiana.separated",))),
    n("bereaved", "Kiana", '''"I found an old letter from Elan. I had forgotten how bad his handwriting could be when he was in a hurry. He used to blame the horse."
{n}She smiles, rubbing a thumb along the edge of the folded paper.{/n}
"I wanted to read it again. I also wanted to see you tonight. I am getting better at letting both things be true."''',
      c('"Keep it somewhere you can find it again."', "work")),
    n("settling", "Kiana", '''"Elan and I have been sorting out what belongs to whom. We agreed about the furniture. Then neither of us wanted to be the first to take down a little picture we bought together."
{n}She looks toward the wall, where the picture now hangs.{/n}
"He told me to keep it. We were kind to each other for a few minutes. I was glad of that."''',
      c('"I am glad you could have that conversation."', "work")),
    n("work", "Kiana", '''{n}Kiana takes up the play. She has crossed out most of its final page.{/n}
"Everyone keeps congratulating me on being brave. I was trying to write a woman who wants a pleasant evening. Apparently that is a heroic undertaking now."
{n}She shows you the one surviving sentence.{/n}
"Help me make her a little selfish. Something small enough that she has to admit she simply wants it."''',
      c('"She keeps the best seat by the fire."', "seat"),
      c('"She asks her lover to leave the paperwork until morning."', "papers")),
    n("seat", "Kiana", '''"Excellent. And she refuses to apologize for having cold feet."
{n}Kiana writes it down and settles herself more comfortably.{/n}
"You may choose the next scene. I have decided to be generous."''', c('[Let her claim the best place by the fire.]', "promise")),
    n("papers", "Kiana", '''"An outrageous demand. I approve."
{n}She puts her own pages aside first.{/n}
"There. I have saved you from having to point out the hypocrisy."''', c('[Put your work aside too.]', "promise")),
    n("promise", "Kiana", '''"When all this is over, I would like to keep seeing you. In rooms that don't have to be borrowed, perhaps. But I won't wait until the war is over to have a life."
{n}Her voice is quiet, with none of the princess in it.{/n}
"Will you make room for that?"''',
      c('"Yes. Let us keep choosing the time, even when it is difficult."', "yes"),
      c('"I want you, but I cannot promise what happens after the war."', "uncertain")),
    n("yes", "Kiana", '''"Then I will hold you to the next evening first. I know how generals can be about distant plans."
{n}She names a day. You make the arrangement together.{/n}''', c('[Keep making a life with her.]', flags=("kiana.committed",))),
    n("uncertain", "Kiana", '''"Then don't promise it. Keep the evening you have offered. We can talk again when we know more."
{n}She draws her chair closer.{/n}''', c('[Stay without making a lasting promise.]', flags=("kiana.uncertain",))),
], requires=("kiana.lovers",))

s("seelah", "What she has heard", [
    n("start", "Seelah", '''"Kiana told me you have been seeing each other. I wanted to hear it from you too."
{n}Seelah keeps her voice low.{/n}''',
      c('"We kissed before she spoke to Elan. I should have waited."', "hurt", requires=("kiana.affair",)),
      c('"We waited until she had spoken to Elan."', "waited", requires=("kiana.waited",)),
      c('"She wanted time and company. We found something more."', "grief", requires=("kiana.bereaved",))),
    n("hurt", "Seelah", '''"Yes. You should have."
{n}For a moment she looks as if she might leave it there.{/n}
"Elan is my friend. So is Kiana. I'm not going to make one of them a villain so the rest of us can enjoy ourselves. If somebody starts telling that version around you, put a stop to it."''',
      c('"I will. He deserves that much from me."', "end", flags=("kiana.defend_elan",))),
    n("waited", "Seelah", '''"I'm glad you waited. That doesn't mean he won't be hurt."
{n}She rubs a hand over her face.{/n}
"I used to think getting everyone through the fighting would be the hard part. Then we'd all know how to be happy. Rather a lot to ask of winning a war, isn't it?"''', c('"It was a good thing to hope for."', "end")),
    n("grief", "Seelah", '''"She laughed when she told me about your play. Then she cried a little. I wasn't sure what to do, so I stayed."
{n}Seelah gives you a small, tired smile.{/n}
"That seemed to help. You don't have to fix every evening."''', c('"I am learning that."', "end")),
    n("end", "Seelah", '''"All right. I wanted to say it. Now I have to work out how to attend a play without becoming part of it. Kiana has threatened to give me a crown."
{n}She sounds considerably more alarmed by this than by most military assignments.{/n}''', c('[Promise nothing about the crown.]', flags=("kiana.seelah_spoke",))),
], requires=("kiana.lovers",), forbids=("seelah_dead", "seelah_gone"), optional=True)

s("farewell", "The next page", [
    n("start", "Kiana", '''{n}Kiana has brought you a clean page, folded small enough to carry.{/n}
"For the next part. I thought about writing you a magnificent farewell. Then I imagined having to live with it if you came back and quoted it at me."
{n}She presses the fold flat with her thumb.{/n}
"Come back. I would like to be embarrassed by something much less solemn."''',
      c('"Keep a part for me."', "part"),
      c('"I would like to hear what you plan to do while I am gone."', "plans")),
    n("plans", "Kiana", '''"Work on the play. Arrange a reading of the next draft. Discover which of my improvements people preferred before I improved them."
{n}Her smile comes and goes.{/n}
"There are people I'd like to invite who need an evening out. I was going to ask Arsinoe whether she knew anyone who might enjoy it. I thought an invitation would be better than deciding they ought to be cheered up."''',
      c('"I would like to speak with her too. Save me a seat when the play is ready."', "part", flags=("arsinoe.introduced",)),
      c('"Save me a seat."', "part")),
    n("part", "Kiana", '''"I will. You must be there to complain about the ending."
{n}She gives you the folded page. For once she lets the plain request stand, without adding a joke to make it easier to hear.{/n}''', c('[Keep the page.]', flags=("kiana.farewell_kept",))),
], requires=("kiana.morning",), RequiresAny=("kiana.future_settled", "inhuman"))

s("parting", "The words outside the play", [
    n("start", "Kiana", '''"Tell me. You have been looking at me as if you're trying to remember a line."''',
      c('"I want to end our relationship."', "end"),
      c('"I wanted to ask for another evening together."', "stay")),
    n("end", "Kiana", '''{n}Kiana sits very still.{/n}
"I see. I would like to ask you a dozen questions, and I'm not sure I want any of the answers tonight."
{n}She reaches for her pages.{/n}
"Please go. I'll write if I want to talk."''', c('[End the relationship.]', flags=("kiana.closed",))),
    n("stay", "Kiana", '''"Then ask. I have wasted an excellent expression of concern on a perfectly pleasant invitation."''', c('[Arrange the evening.]', abort=True)),
], requires=("kiana.lovers",), optional=True, ManualOnly=True)


def ending(id, text, requires=(), forbids=(), owner="Epilogue"):
    SCENES.append(scene("kiana.ending_" + id, RELATIONSHIP["Title"], owner, 5, "", [
        n("start", "Narrator", text, c(), portrait="Kiana"),
    ], Relationship="kiana", last=99, requires=requires, forbids=forbids))


ending("together", '''{n}Kiana took the play beyond readings to a production with scenery, borrowed costumes and more practical difficulties than she had budgeted for. One performance was interrupted when a guest asked why the vampire princess's castle smelled of onions. She considered this a promising response.{/n}
{n}The small picture she had kept after separating from Elan hung in the room where she wrote. She did not take it down to make a visitor comfortable. Her marriage had been real, and so had its ending.{/n}
{n}She and the Commander kept finding evenings for one another. Some were grand enough to satisfy the vampire princess. The ones Kiana spoke of most fondly involved unfinished work and someone who stayed to hear how her day had gone.{/n}''', requires=("kiana.committed", "kiana.separated", "kiana.future_settled"), forbids=("kiana.closed", "ascended"))
ending("bereaved", '''{n}Kiana took the play beyond readings to a production with scenery and costumes. The scenery proved less reliable than the actors. She laughed through a disastrous rehearsal and insisted on inviting an audience anyway.{/n}
{n}Elan's letters stayed in a drawer she opened when she wanted to hear his voice in the words. Some days she spoke about him. The Commander learned to listen without trying to bring those stories to a comforting conclusion.{/n}
{n}There were new letters too, and evenings worth dressing for. Kiana made plans with the person who had learned her ridiculous lines and stayed for the conversations that followed.{/n}''', requires=("kiana.committed", "kiana.bereaved", "kiana.future_settled"), forbids=("kiana.closed", "ascended"))
ending("ascended", '''{n}Kiana discovered that loving someone who had become divine did not make waiting for an answer less irritating. Her letters said so, with increasingly elaborate illustrations.{/n}
{n}When an answer came, she read it in private. Then she returned to the play, where the princess had acquired a guest with an inconveniently celestial schedule. The guest's best line was still a simple promise to stay for the evening.{/n}''', requires=("kiana.committed", "ascended", "kiana.future_settled"), forbids=("kiana.closed",))
ending("apart", '''{n}Kiana kept the pages they had written together, though she put them away for a time. When she returned to the play, she changed the ending.{/n}
{n}She did not offer their private conversations as an explanation for the changes. Whatever an audience made of the princess and her guest, Kiana chose how much of her own story she would tell.{/n}''', requires=("kiana.lovers", "kiana.closed"))
ending("unfinished", '''{n}Their evenings never quite became the life Kiana had begun to imagine. For a while, she left room in her invitations. Eventually she made other plans.{/n}
{n}She finished the play. The princess's guest had several excellent lines, but no longer appeared in the final scene.{/n}''', requires=("kiana.attracted",), forbids=("kiana.committed", "kiana.closed", "kiana.future_settled"))
ending("aeon", '''{n}In the history the Commander left behind, there was no borrowed castle and no folded page carried into the last battle. Kiana had other evenings to live.{/n}
{n}Whether a fragment of that other story survived in memory or only in a sudden wish to write, it could no longer require the ending two people had once planned for it.{/n}''', requires=("kiana.committed",), forbids=("kiana.closed",), owner="AeonEpilogue")

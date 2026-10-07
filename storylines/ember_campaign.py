"""Ember's friendship campaign: authored lives alongside native companion quests.

No romance, age transformation, quest completion, or cure is supplied here.
"""
from copy import deepcopy
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
CONTACT = "2779754eecffd044fbd4842dba55312c"
ANSWERS = "f2a35965e9bc601449498bd022b04d9d"
CARE_ANSWERS = "fd8276a6302f4d44583eba3f0b9663bf"
ETUDES = {
    "ember.native_good": "b981026a5be6a9a49bf1f7ab57f9e1bb",
    "ember.native_law": "f55fcc7bf5fd0c14384cb15dce345c8e",
    "ember.native_devastated": "b1d0c45e438c2ae458466ed56de99a9d",
}
COMPLETED_QUESTS = {
    "ember.native_q1_complete": "1fdf404b17d464a489267f69d58b846d",
    "ember.native_q2_complete": "a3f445a64ee130f4396c20a07c30ece0",
    "ember.native_q3_complete": "49b7496143daed149ab4557a9684dd53",
}


def s(id, title, entry, nodes, requires=(), delay=24, chapters=(3, 5), care=False, forbids=()):
    for node in nodes:
        node["Portrait"] = "Ember" if node["Speaker"] in ("Ember", "Narrator") else ""
    SCENES.append(scene("ember." + id, title, "Ember", min(chapters), entry, nodes,
        Relationship="ember", Chapters=list(chapters), last=max(chapters), Areas=[DREZEN],
        ContactUnit=CONTACT, AnswerLists=[CARE_ANSWERS if care else ANSWERS],
        requires=("ember.present", *requires), delay=delay, optional=True,
        forbids=("ember.closed", "ember_dead", "ember_gone", "ember.absent",
                 *(("ember.native_devastated",) if not care else ()), *forbids)))


s("something_you_cannot_do", "The Commander's other talents",
  '"I thought of something I am bad at. Would you like to try it with me?"', [
    n("start", "Ember", '''"Yes. Unless it is being bad at having an afternoon. We have already practiced that enough."
{n}Ember has put the puppets away. Soot sits above her on the edge of a low roof, turning her head whenever a sparrow ventures near the crumbs below.{/n}
"She thinks I don't know what she is doing. I put the crumbs there for everybody."
{n}Ember looks up at the crow. Soot looks somewhere else.{/n}
"There. Now she is too busy to answer. What did you think of?"
{n}She has left a space beside her on the low wall. The paving in front of it is clear, and for once nobody seems to be waiting to ask her a question. She pats the stone once, an invitation to begin.{/n}''',
      c('"Whistling. I know a tune, but it disappears when I try to whistle it."', "whistle"),
      c('"A little game with stones. I can never remember whose turn it is."', "stones"),
      c('"Unfortunately, I must practice having the afternoon another day."', abort=True)),
    n("whistle", "Ember", '''{n}Your first attempt produces mostly breath. The second has a note in it, unexpectedly loud. A sparrow abandons the crumbs. Soot remains where she is, but draws herself up as though the roof has become a place requiring dignity.{/n}
"You have frightened someone," {n}Ember whispers.{/n} "Try a smaller tune."
{n}You explain that the tune is already very small. She listens while you hum it, then tries to whistle the first few notes. Her breath makes a thin, uncertain sound. She stops and laughs.{/n}
"I think mine has escaped too. Perhaps they have gone to find each other."
{n}The next attempt goes better. You supply a few notes; she waits for a place to answer. It takes several tries before either of you remembers to stop at the same time.{/n}
"We could use that when we want someone to know we are coming," {n}she says.{/n} "Only they might think we are two very poorly birds."
{n}Soot descends to the crumbs. Apparently the danger has passed.{/n}''',
      c('"Keep practicing until you can answer each other."', "whistle_personal")),
    n("whistle_personal", "Ember", '''"Who showed you the tune?"
{n}The question is ordinary enough that you nearly answer without thinking. Then you remember a person, or a place, or the embarrassment of learning it alone. Ember waits while you decide what you want to tell.{/n}
"You don't have to make it a good story," {n}she says.{/n} "I wanted to know what you were remembering when you stopped."
{n}You tell her something of that earlier day. When she asks another question, it concerns the part you almost left out: whether you liked the company, whether you wanted to go home, whether anybody else knew you were trying.{/n}
{n}She tries the tune again after you finish. This time she leaves a pause for your answer.{/n}
"There. It can have this afternoon in it too. It doesn't have to stop belonging to the other one."
{n}The last note collapses into laughter. You cannot quite imitate it, which makes her laugh harder.{/n}''',
      c('"Keep the uneven tune between you."', flags=("ember.started", "ember.campaign_started", "ember.shared_whistle"))),
    n("stones", "Ember", '''{n}You collect a few smooth stones and mark a circle in the dust. The game begins with moving them across the circle in pairs. By the fourth turn, Ember has three stones on one side, you have one on the other, and neither of you can explain where the last pair went.{/n}
"I think we have been too helpful," {n}she says.{/n} "I moved one of yours because it was alone."
{n}You start again. This time she keeps her hands in her lap when it is your turn. You make a mistake, notice it too late, and look up to find her smiling with alarming patience.{/n}
"May I move that one now?"
"It will let you win."
"Yes. That is why I asked."
{n}She moves it and looks so pleased that you demand another round. Halfway through she forgets which stones are hers. You return the same patient smile.{/n}
"Oh. It isn't as nice from this side."
{n}The sparrows return to the crumbs. Soot watches from the roof while you agree on a way to mark the two sets.{/n}''',
      c('"Play another round, with one set of stones turned pale side up."', "stones_personal")),
    n("stones_personal", "Ember", '''"Did somebody teach you this? Or did you make it because you needed something to do?"
{n}You tell her what you remember of learning the game. She asks whether the person who taught you let you win. When you say what you think, she considers it seriously.{/n}
"I like winning. But I think I would want to know if somebody was giving it to me. I might be proud of the wrong thing."
{n}The next round takes longer. You both stop to check whose turn it is, which greatly improves the fairness and does nothing for the speed. Ember wins by a move you both notice a moment after she makes it.{/n}
"That one was mine," {n}she says, delighted.{/n}
{n}You collect the stones together. She asks whether you will show her another game sometime, then changes her mind.{/n}
"This one first. I want to remember it without being reminded every time. You can tell me if I move the lonely stones again."
{n}She gives you half of them to keep until the next afternoon.{/n}''',
      c('"Keep your half of the stones."', flags=("ember.started", "ember.campaign_started", "ember.shared_stones"))),
], requires=("ember.puppet_afternoons_kept", "ember.second_ending"))

# A late friendship plays the same activity without claiming the eight earlier visits.
late_nodes = deepcopy(SCENES[-1]["Nodes"])
late_nodes[0]["Text"] = '''"I would like that. What are you bad at?"
{n}Ember moves along the low wall to make room. Soot sits above her on the edge of a roof, turning her head whenever a sparrow ventures near the crumbs below.{/n}
"She thinks I don't know what she is doing. I put the crumbs there for everybody."
{n}Ember looks up at the crow. Soot looks somewhere else.{/n}
"There. Now she is too busy to answer. We can do something without her."
{n}You have shared the demands of the crusade, but there have been fewer visits simply to keep each other company. Ember seems pleased by the invitation. She leaves you room to explain what you had in mind.{/n}'''
s("a_late_afternoon", "An afternoon still worth having",
  '"We have not had enough time just to be friends. May I show you something?"',
  late_nodes, chapters=(5,), delay=0,
  forbids=("ember.puppet_afternoons_kept", "ember.campaign_started"))


s("the_empty_basket", "Things somebody might still want",
  '"What are you looking for?"', [
    n("start", "Ember", '''"The person who lost this."
{n}Ember holds up a wooden comb with three teeth missing. A blue thread is tied through a hole at one end. Beside her is a shallow basket containing a buckle, a folded scrap of cloth, and a little wooden handle without the tool it once belonged to.{/n}
"They were clearing a room for people to sleep in. Some of these things were under the boards. The man said they were rubbish. But the comb has a string. Somebody wanted to hang it up where they could find it."
{n}She runs a finger along the unbroken teeth.{/n}
"I don't know whether they are still here. They might have gone a long way. I thought I could ask before everything went into the fire."
{n}Soot lands on the wall. She is carrying nothing, although Ember examines her beak with hopeful interest before returning to the basket.{/n}
"Will you help me? You know more people than I do. I think. You certainly have more people telling you what to do."''',
      c('"Show me where the things came from."', "room"),
      c('"We can look when I have more time."', abort=True)),
    n("room", "Narrator", '''{n}The room stands behind a storehouse. An adult woman named Vessa is sweeping it while a man lifts broken boards through the doorway. She has kept two sound sleeping platforms and a table that needs a wedge beneath one leg.{/n}
"For people coming in from the roads," {n}Vessa explains.{/n} "One night, perhaps two. They need somewhere before they know who to ask for work."
{n}The man with the boards introduces himself as Dervan. He has a flattened nose, broad hands, and the habit of looking toward the door whenever someone speaks sharply outside.{/n}
"The comb was beneath that platform," {n}he tells Ember.{/n} "Before you ask, I didn't put it there. I have been here three days."
"I wasn't going to ask that."
{n}He looks embarrassed, then shrugs.{/n}
"People usually do."
{n}Vessa rests her broom against the table. The room belonged to a family before it became storage. She knows where one of their former neighbors sells vegetables, though she cannot promise the woman remembers a comb.{/n}''',
      c('"Ask the neighbor about the family."', "neighbor"),
      c('"Dervan, why did you expect to be blamed?"', "deren")),
    n("deren", "Ember", '''"Because I used to take things," {n}Dervan says.{/n} "Sometimes from people who had less than I did. Vessa knows. I told her before she found out from someone else."
{n}Ember looks at the basket, then back at him.{/n}
"Did you give them back?"
"Some. I couldn't find everyone. I couldn't remember everyone."
{n}He says the last part with difficulty. Ember does not tell him that it makes no difference.{/n}
"Perhaps you can help us find this person. You remember where it was."
"That won't return what I took."
"No. It might return a comb."
{n}Dervan looks toward Vessa. She gives him a small nod, then points at the stack of boards he still has to move.{/n}
"After those. I will be the one tripping over them while you do a good deed."
{n}He finishes the work. Ember waits with the basket, turning the blue thread between her fingers.{/n}''',
      c('"Go to the neighbor when the doorway is clear."', "neighbor")),
    n("neighbor", "Narrator", '''{n}The vegetable seller remembers the family. Her name is Heda. She has news of the youngest daughter, now an adult, who works carrying water to a kitchen several streets away. She does not know whether the comb belonged to her.{/n}
"Take it to her if you like. But don't arrive telling her you've brought back her home. People have been bringing her broken pieces of it for years."
{n}Ember holds the basket closer.{/n}
"I was going to ask if she wanted it."
"Then ask. And let her say no."
{n}Heda writes the kitchen's location on the back of a discarded price notice. Dervan reads it, then points out a shorter way. He knows the streets where the stores are, he says, with a smile that does not quite survive the explanation.{/n}
{n}At the kitchen, the woman is carrying two empty buckets. She introduces herself as Mara, listens to Ember, and studies the comb without taking it.{/n}
"That was my mother's. I don't want it."''',
      c('"Then we will take it away. Thank you for looking."', "declined"),
      c('"Would you like us to leave it somewhere you could collect it later?"', "later")),
    n("declined", "Ember", '''{n}Ember lowers the basket at once.{/n}
"All right. Do you want the other things?"
{n}Mara looks through them. She takes the wooden handle, surprising both of you.{/n}
"My father made this. The tool broke every time he repaired it. He kept making better handles for a worse and worse blade."
{n}For a moment she smiles. Then she asks where the room is being used now. When Vessa's work is explained, she nods and picks up her buckets.{/n}
"I hope they sleep well. The floor is cold by the door."
{n}Ember thanks her and moves aside. You walk away with a lighter basket and the comb still lying on top.{/n}
"I thought she would want that most," {n}Ember says.{/n} "She knew something about it I didn't know."
{n}Dervan carries the basket back while Ember walks beside you.{/n}''',
      c('"Return the unclaimed things to Vessa without reserving them for Mara."', flags=("ember.keepsake_declined", "ember.room_known"))),
    n("later", "Ember", '''"No," {n}Mara says.{/n} "I don't want to know it is waiting for me. You can give it to someone who needs a comb."
{n}Ember nods. She holds the basket while Mara looks through the rest. The woman takes the wooden handle, which her father made, and tells a short story about the troublesome tool it once belonged to.{/n}
{n}Before returning to work, Mara asks what has become of the room. When she hears about the sleeping platforms, she tells Ember that the floor is cold by the door.{/n}
"Perhaps that will be useful. More useful than keeping a comb for me."
{n}On the way back, Ember looks at the blue thread.{/n}
"I wanted to leave it where she could change her mind. But she didn't want another thing she had to decide about."
{n}She turns to Dervan, who has offered to carry the basket.{/n}
"We should tell Vessa about the cold floor. Mara wanted us to know that."
{n}Dervan says he has some sacks he can clean and lay under a mat. It is the first suggestion he has made without looking as though he expects to be refused.{/n}''',
      c('"Carry back Mara\'s useful warning and her refusal."', flags=("ember.keepsake_questioned", "ember.room_known"))),
], requires=("ember.campaign_started",))


s("the_cold_side", "A place by the door",
  '"Did Vessa make the room ready?"', [
    n("start", "Ember", '''"Almost. The door won't stay where she puts it. Dervan says the wood has opinions."
{n}Ember has a bundle of washed sacks under one arm. You walk with her to the room, where Vessa is testing the threshold with the flat of her foot. The door closes if pushed firmly, but springs open again when someone crosses the boards.{/n}
"It didn't do that yesterday," {n}she says.{/n}
"Yesterday we were holding it open with a bucket," {n}Dervan reminds her.{/n}
"Then it was more polite yesterday."
{n}The sleeping platforms have clean coverings. Mara's warning has been remembered: a woven mat lies near the door, waiting for something beneath it to keep the cold from coming through.{/n}
{n}Ember gives Vessa the sacks and asks whether anyone has come yet. Two people are expected tonight. One is an older traveler with a painful leg; the other has been sleeping outside the kitchen where he hopes to work.{/n}
"Neither needs another night with a door that changes its mind," {n}Vessa says.{/n}''',
      c('"Look at how the door moves when the floor is stepped on."', "inspect"),
      c('"Ask a carpenter to examine it. We can finish the mat while we wait."', "carpenter")),
    n("inspect", "Narrator", '''{n}Dervan opens and closes the door while Vessa crosses the threshold. Its lower edge catches, then lifts away from the latch. The boards seem to move together, but the scrape on the floor is uneven.{/n}
{n}Ember waits with the mat rolled beside her. She watches your face rather than offering an answer she does not have.{/n}''',
      c('[Perception] Follow the scrape and identify what lifts the door clear of its latch.',
        check=dict(Skill="SkillPerception", DC=24, CommanderOnly=True, Success="wedge", Failure="uncertain")),
      c('"I would rather ask the carpenter than guess."', "carpenter")),
    n("wedge", "Narrator", '''{n}A loose chip has worked beneath the door's lower hinge. Each time the threshold flexes, the chip pushes the door slightly upward. You point it out. Dervan holds the door while Vessa works the chip free with the end of a spoon.{/n}
{n}The latch catches properly. Vessa crosses the boards again, then asks Dervan to try. The door stays shut.{/n}
"We should still replace the loose screw," {n}she says.{/n} "But now I can do it tomorrow in daylight."
{n}Ember tests the handle gently, pleased by the unremarkable click.{/n}
"That is a good sound. I don't think I noticed it before."
{n}The time saved leaves you free to make the cold corner more comfortable. Vessa finds a spare covering, and Dervan offers to carry the older traveler's bundle from the place where she is waiting.{/n}''',
      c('"Finish the mat and help meet the arriving traveler."', "early")),
    n("uncertain", "Ember", '''{n}The scrape does not tell you enough. You test the threshold once more, then step aside rather than make the hinge bear an experiment. Vessa nods when you say you cannot identify the cause.{/n}
"I can ask the carpenter. He will come after his present work. It means we will be late opening."
{n}Ember looks at the sleeping platforms.{/n}
"We should tell the people who are coming. They won't know where to go if they find the door shut."
{n}Dervan takes the message to the kitchen. You remain to help Vessa arrange the mat. The carpenter arrives near dusk, discovers a chip beneath the loose hinge, and repairs the fastening. He charges for the visit. Vessa pays without looking particularly happy about it.{/n}
"I had hoped to buy another covering," {n}she says.{/n} "That will wait. A closed door will help more tonight."
{n}Ember gathers the unused sacks. There are enough to make a smaller pad for the cold corner, though it will be less comfortable than the covering.{/n}''',
      c('"Make the pad and wait for the guests to return."', "late")),
    n("carpenter", "Ember", '''{n}Vessa asks Dervan to fetch the carpenter. While he is gone, you help Ember lay the cleaned sacks beneath the mat. She tries the corner herself, sitting for a moment before deciding one part needs folding twice.{/n}
"Mara was right. You can feel it through the floor."
{n}The carpenter arrives with Dervan and a small bag of tools. He finds a chip beneath the loose hinge, works it free, and replaces the screw that allowed it to move. The charge leaves Vessa with less money for another covering, but the door stays closed while you test the threshold.{/n}
{n}You finish in time to receive the guests. Dervan goes to help the older traveler with her bundle, while Ember asks Vessa whether the remaining sacks can make another pad.{/n}
"Yes. We can make do with that tonight."
{n}Ember holds one end while you fold the other. The result is inelegant and usefully thick.{/n}''',
      c('"Put the extra pad where the traveler can reach it."', "on_time")),
    n("early", "Narrator", '''{n}The older traveler introduces herself as Tesvara. She is grateful for help with her bundle and less grateful for suggestions about where to put her painful leg. Ember stops giving those when Tesvara asks, then holds the cushion where she points.{/n}
{n}The other guest arrives while Vessa is still explaining the room. His name is Oren. He takes the place near the door before Tesvara can apologize for wanting the warmer one.{/n}
"I'm used to outside," {n}he says.{/n}
"You can be used to this instead," {n}Ember answers.{/n}
{n}Dervan puts the spare covering on the table for them to decide how to share. Vessa records where it belongs before she leaves.{/n}''',
      c('"Leave them with a working door and the extra covering."', flags=("ember.door_found", "ember.room_opened"))),
    n("late", "Narrator", '''{n}The guests return after Dervan finds them shelter beside the kitchen for the delay. Tesvara is tired and cross, although she thanks him for carrying her bundle. Oren says very little until he sees the clean place prepared for him.{/n}
{n}Ember apologizes that they had to wait. Tesvara asks for a drink rather than an explanation. Ember brings one and sits nearby only after asking whether company would help.{/n}
{n}The door holds when Vessa closes it. The extra pad is smaller than the covering she meant to buy, but Tesvara puts it under her leg and sighs with relief.{/n}
"That will do. Thank you."
{n}Ember leaves with you, carrying the empty water jug back to the kitchen.{/n}''',
      c('"Help put things away after the delayed opening."', flags=("ember.door_uncertain", "ember.room_opened"))),
    n("on_time", "Narrator", '''{n}Tesvara arrives with her bundle in Dervan's arms. Oren follows, looking so cautiously at the clean sleeping place that Vessa has to tell him twice that it is the one he may use.{/n}
{n}Ember offers the extra pad. Tesvara accepts it and explains where it will help her leg. When Ember begins to suggest something else, Tesvara asks her to wait until she has tried sitting down.{/n}
"Oh. Yes. I can wait."
{n}She does. Outside, Vessa shuts the door and tests it one final time. The room has opened when promised, though another covering will have to wait until she can afford it.{/n}
{n}Ember walks back beside you, pleased and tired enough to leave some of the walk quiet.{/n}''',
      c('"Keep her company on the way back."', flags=("ember.door_helped", "ember.room_opened"))),
], requires=("ember.room_known", "ember.the_empty_basket"))


s("the_missing_covering", "Who has to answer",
  '"You said you wanted help at Vessa\'s room."', [
    n("start", "Ember", '''"I want you to listen. You can help with that, can't you?"
{n}Ember walks beside you quickly, then slows when she notices. She has a piece of folded cloth in her hand. One edge is marked with dark blue stitches.{/n}
"Vessa has lost a covering. Dervan thinks she means he took it. She says she hasn't said that. But she keeps asking where he went yesterday."
{n}She unfolds the corner enough to show the stitches.{/n}
"This is how she marks the things that belong in the room. She gave me this bit so I would know what to look for. I haven't found it."
{n}At the doorway, Dervan is putting his few belongings into a bag. Vessa stands beside the table, visibly trying to choose each word before it leaves her mouth.{/n}
"I need to ask everyone who had the key," {n}she says.{/n} "You had it. That is why I am asking."
"And if it was someone who looked more respectable? Would he be packing?"
"I didn't tell you to pack."
"You haven't told me to stay either."''',
      c('"Ask what Ember would like to say before joining the argument."', "ember"),
      c('"Vessa, tell me what is missing and when you last saw it."', "facts")),
    n("ember", "Ember", '''"I don't know whether he took it. I don't want to say I know when I don't."
{n}Dervan looks away. Ember notices and turns toward him.{/n}
"I wanted you to stay while we looked. Going away won't help Vessa find it. And it won't tell us what happened."
"Staying while everybody looks at me won't either."
"Then perhaps we can look at the room."
{n}She puts the marked scrap on the table. Vessa sits, as though the suggestion has given her permission to stop standing guard over a bag she never meant to search.{/n}
"That would help," {n}she says.{/n} "I would like to explain what I actually know."
{n}Dervan does not unpack. He sets the bag beside the door and remains to listen.{/n}''',
      c('"Hear Vessa\'s account."', "facts")),
    n("facts", "Narrator", '''{n}Vessa laid a donated covering on the table yesterday. It had the blue corner mark, and a patched stripe down one side. She left the room to help at the kitchen. When she returned, it was gone.{/n}
{n}Tesvara has moved on with a cart going toward her relatives. Oren has begun working at the kitchen and still sleeps here. Dervan was cleaning the platform nearest the door. Two other people came to ask about a bed. Vessa knows only one of their names.{/n}
"I should have stayed," {n}she says.{/n}
"You can't stay here all day," {n}Ember answers.{/n} "You have to eat too."
{n}Dervan says he saw someone take a rolled bundle through the door. He thought it was Tesvara's. He did not ask. Now he is angry that Vessa seems to consider this less satisfactory than a confession.{/n}
"I haven't asked you to confess," {n}she says.{/n}
"You've asked me four times."
{n}Ember looks from one to the other, then at you. She wants the covering found. She also wants the two people in front of her to stop hurting each other while they try.{/n}''',
      c('"Ask Oren what he saw. Keep the question about the covering."', "oren"),
      c('"Search the room with Vessa first. It may have been put away."', "search"),
      c('"Dervan should show us his bag and end the suspicion."', "bag")),
    n("bag", "Ember", '''"That would show us his bag," {n}Ember says.{/n} "It wouldn't show us yesterday."
{n}Dervan puts a hand on the fastening. He looks ready to open it, though nothing in his expression suggests that he wants to.{/n}
"Do you want to?" {n}Ember asks him.{/n}
"I want to stop being looked at."
{n}She turns back to you.{/n}
"That isn't the same answer. Can we ask Oren first? He was here too."
{n}Vessa presses her lips together, then nods.{/n}
"Yes. I have let the room become a place where only one person is being asked to explain himself. That wasn't what I meant to do."
{n}Dervan takes his hand off the bag. He does not thank anyone. Ember does not appear to expect him to.{/n}''',
      c('"Leave the bag closed and ask Oren."', "oren")),
    n("search", "Narrator", '''{n}Vessa opens the cupboard and lifts the coverings from the platforms. Dervan holds the table steady while you look beneath it. Ember checks the clean sacks without unfolding the ones already arranged for Oren.{/n}
{n}You find a wooden button and a spoon nobody admits owning. The missing covering is not in the room. Vessa checks her written list again, then puts it down.{/n}
"I wanted to discover I had miscounted."
"You still might have forgotten something," {n}Ember says.{/n} "Oren was here. He could remember a different bit."
{n}Dervan picks up the spoon and places it beside the cupboard. He leaves his bag where it is, but no longer holds its fastening.{/n}
"I'll come," {n}he says.{/n} "I want to hear the question the first time someone asks it."''',
      c('"Go to the kitchen together."', "oren")),
    n("oren", "Ember", '''{n}Oren is scraping a pot when you arrive. He sees Vessa's face and puts the scraper down before she speaks.{/n}
"The striped covering? I lent it to the woman with the cart. Her little brother was shivering. She said she would bring it back."
"You did not ask me," {n}Vessa says.{/n}
"You weren't there. I thought helping was what the room was for."
{n}Dervan laughs once, without amusement. Ember waits until Oren has finished explaining where the cart went.{/n}
"You wanted him to be warm," {n}she says.{/n} "Now somebody else might be cold. We have to look for it."
"I didn't take it for myself."
"I know. Where did they say they were staying?"
{n}Oren gives a description of a yard near the city entrance. Vessa knows it. She asks him to come after his work and help her see whether the cart is still there.{/n}
{n}Dervan looks ready to leave. Before he does, Vessa says his name.{/n}''',
      c('"Let Vessa answer Dervan for herself."', "apology")),
    n("apology", "Ember", '''"I should have asked him as carefully as I asked you," {n}Vessa says.{/n} "I'm sorry."
{n}Dervan looks at her for a long moment.{/n}
"You knew where I was sleeping. It was easier to keep asking me."
"Yes."
{n}Ember waits beside the table while Dervan rubs a thumb along his bag's fastening.{/n}
"I want my bag somewhere I can shut a door," {n}he says at last.{/n} "A different door. I can finish the work I promised. I don't want to sleep there tonight."
{n}Vessa says she understands. Ember asks whether he wants help finding somewhere else. He considers the offer, then nods.{/n}
"You can ask at the yard with the cart. One question while you're there. Not a speech about me."
"I can ask one question," {n}Ember says.{/n} "I might need two if they don't understand the first."
{n}That earns a reluctant smile. Dervan picks up his tools and returns to finish the platform.{/n}''',
      c('"Offer to go with Ember and look for the missing covering."', flags=("ember.covering_misgiven", "ember.deren_distance"))),
], requires=("ember.room_opened", "ember.the_cold_side"))


s("a_question_at_the_yard", "The promise someone else made",
  '"Shall we look for the cart?"', [
    n("start", "Narrator", '''{n}Ember has brought Vessa's marked scrap. Vessa and Oren meet you near the yard after the kitchen work is done. The carts stand in uneven rows, their owners speaking over one another about food, repairs, and the next safe road.{/n}
{n}The woman Oren describes is there. Her name is Selvi. Her younger brother, still a child, sits in the cart wrapped in the striped covering. He is awake and eating. The blue corner mark hangs over one wheel.{/n}
"We came to ask for that back," {n}Vessa says.{/n}
{n}Selvi looks from her to Oren. Her hand closes around the side of the cart.{/n}
"He said we could use it."
"I said you could borrow it," {n}Oren replies.{/n} "You said you would return it."
"We haven't left."
{n}Ember stops a little way from the wheel, where the boy can see her without being surrounded. She asks whether he feels warmer. He nods, looking anxiously at the adults.{/n}''',
      c('"Tell Selvi why the covering is needed back at the room."', "need"),
      c('"Ask whether she has anything else to keep him warm tonight."', "other")),
    n("need", "Ember", '''{n}Vessa explains the room and the people expected to use it. Selvi's grip on the cart loosens a little, though her face remains closed.{/n}
"I thought a room would have more. We have what fits here."
"It doesn't have much more," {n}Ember says.{/n} "It has people who need to sleep too."
{n}The boy begins to unwrap himself. Ember holds up a hand, stopping him without touching the covering.{/n}
"We are still talking. You don't have to get cold while we do it."
{n}Vessa looks away for a moment, then asks Selvi what she has for him. There is another cloth in the cart, thin and too short to cover him well. It has been folded beneath the food to keep it clean.{/n}
"We can use that," {n}Selvi says, too quickly.{/n}
{n}Ember looks at Vessa. Nobody has found an extra covering merely by explaining who needs this one.{/n}''',
      c('"Consider what can be arranged for tonight."', "choices")),
    n("other", "Ember", '''{n}Selvi takes a thin cloth from beneath the food. She shakes it open, showing that it will cover her brother if he stays curled up.{/n}
"We can manage."
{n}Ember looks at the boy's feet, which are already sticking out from the striped covering.{/n}
"He might want to move while he is asleep."
{n}Selvi's expression falters. She tells Vessa that she had hoped to find something to trade before the cart left. The delay is not wholly a plan; it is also a day spent hoping another answer would appear.{/n}
"I should have said that," {n}she admits.{/n}
"Yes," {n}Vessa says.{/n} "I cannot lend what I don't know is missing."
{n}Oren starts to apologize. Vessa asks him to wait until the covering is settled. Ember remains beside the wheel, keeping the conversation from closing around the boy.{/n}''',
      c('"Work out a smaller promise everyone can actually keep."', "choices")),
    n("choices", "Narrator", '''{n}Vessa considers the room's expected guests. There is space for Selvi and her brother tonight if the cart stays in the yard and she is willing to walk back. The covering can return with them; they can leave in the morning after asking at the kitchen about spare cloth.{/n}
{n}Or Vessa can extend the loan until morning and ask Oren to sleep at the kitchen where he works. His covering can serve a new guest for one night. He dislikes the arrangement, but accepts that he gave away something he had no right to promise.{/n}
{n}Selvi can manage either choice. She looks at the cart before saying so. She does not like leaving it, even in a guarded yard.{/n}
"We can help you carry the food," {n}Ember offers.{/n} "If you come."
{n}Vessa asks which arrangement seems less likely to fail. Neither is comfortable for everyone. Oren is waiting for a chance to repair some of the trouble he caused.{/n}''',
      c('"Invite them to the room tonight. Help carry what Selvi cannot leave."', "room"),
      c('"Let the covering stay until morning. Oren can take the less comfortable night."', "cart")),
    n("room", "Ember", '''{n}Selvi locks the cart and checks the fastening twice. You carry the food while Oren helps her brother down. Ember takes the thin cloth, which folds into a very small bundle in her arms.{/n}
"It isn't nothing," {n}she says when Selvi looks at it.{/n} "He can use it over his shoulders when he wakes."
{n}The walk is slow. Vessa goes ahead to prepare the extra place. By the time you reach the room, the boy is yawning so widely that Ember begins to yawn too.{/n}
{n}Selvi settles him with the striped covering, then thanks Vessa in a voice that still sounds tired and defensive. Vessa nods and points out where the water is kept.{/n}
{n}Outside, Ember remembers Dervan's request. You go back to the yard and ask about a place for an adult worker to sleep. There is one in a shared loft. The owner wants to meet him before agreeing. Ember carries that answer back exactly as it was given.{/n}''',
      c('"Finish the evening by taking Dervan the offer to meet."', flags=("ember.covering_room", "ember.covering_settled"))),
    n("cart", "Ember", '''{n}Vessa names the time she will return in the morning. Selvi repeats it back. Oren promises to meet her there before going to work, and this time asks whether Vessa wants him to promise anything else.{/n}
"Only what we've just said."
{n}Ember asks the yard owner about Dervan. There is a place in a shared loft, but the owner wants to meet him first. She thanks the man and does not add a recommendation that Dervan asked her not to make.{/n}
{n}On the walk back, Oren complains about the kitchen floor. Ember listens, then asks which part is least cold. He laughs despite himself.{/n}
"You aren't going to tell me it's my own fault?"
"You know what you did. I wanted to know where you were going to sleep."
{n}At the corner, she gives him the extra sack pad you helped carry from the room. Vessa has agreed it can go with him for the night. Oren checks that he heard this correctly before taking it.{/n}''',
      c('"Take Dervan the invitation to meet the yard owner."', flags=("ember.covering_cart", "ember.covering_settled"))),
], requires=("ember.covering_misgiven", "ember.the_missing_covering"))


s("what_did_not_mend", "Dervan's other door",
  '"Did Dervan find somewhere to sleep?"', [
    n("start", "Ember", '''"Yes. The loft has a window. He told me that first."
{n}Ember has brought two small rolls from the kitchen. She gives you one after explaining that the cook said they were for the people helping Vessa. Her own roll has already lost a corner.{/n}
"He doesn't have to keep his bag by his feet now. The man at the yard gave him a place on a shelf. Dervan said it is a very good shelf."
{n}She considers this while chewing.{/n}
"I think he meant it. I used to know which places stayed dry when it rained. Sometimes a dry place is the first thing you want to tell somebody about."
{n}Vessa passes on her way back from the room. She stops to tell you how the arrangement with Selvi ended.{/n}''',
      c('"Ask about the family who stayed in the room."', "room", requires=("ember.covering_room",)),
      c('"Ask whether the covering came back from the cart."', "cart", requires=("ember.covering_cart",))),
    n("room", "Narrator", '''{n}Selvi and her brother left after breakfast. The kitchen found a second cloth, worn but large enough to fold around the boy. Selvi cleaned the place where they slept before returning to the cart. She left the striped covering on the table, carefully folded to show the blue mark.{/n}
"She asked whether she could bring something if she came this way again," {n}Vessa says.{/n} "I said to ask what we needed when she arrived. She looked relieved not to be given a list to carry away."
{n}Oren has helped wash the used cloths. He now asks before lending even a spoon, which Vessa expects will become less irritating once he trusts himself to distinguish a spoon from a bed covering.{/n}
{n}Ember asks whether Selvi's brother slept well. He did. That answer makes her smile before she asks anything else.{/n}''',
      c('"Ask whether Dervan has returned to help."', "distance")),
    n("cart", "Narrator", '''{n}Oren met Vessa at the yard before work. Selvi had the covering folded and ready. Her brother was wrapped in two thinner cloths, one newly traded from another traveler. Oren carried the striped covering back, then washed it before going to the kitchen.{/n}
"He complained about the floor," {n}Vessa says.{/n} "Then he asked where to put the clean covering. I consider that an improvement."
{n}Selvi's cart left later that morning. She promised nothing more before going. Vessa seems content with the object actually returned.{/n}
{n}Ember has finished her roll. She rubs the crumbs from her fingers over a bare patch of paving where the sparrows can find them.{/n}
"I'm glad they found the other cloth. I kept thinking about his feet sticking out."
{n}Vessa tells her that the boy was asleep when they came for the covering. Ember smiles at that.{/n}''',
      c('"Ask whether Dervan has returned to help."', "distance")),
    n("distance", "Ember", '''"He finished the platform," {n}Vessa says.{/n} "He said he would. He hasn't come back since."
{n}She looks tired, and more hurt than she seems to think she has a right to be.{/n}
"I apologized. I meant it. I know he doesn't owe me a friendly answer, but I would still like one."
{n}Ember looks toward the road to the yard.{/n}
"I can ask whether he wants to see you. I don't want to tell him that he does."
"Don't ask today. Let him settle."
{n}Vessa goes back to her work. Ember remains on the wall beside you, turning the empty paper from the rolls over in her lap.{/n}
"I wanted everyone to stay friends. Now the covering is back and Dervan has a room, but I didn't get the thing I was wishing for."
{n}She looks at you.{/n}
"I know those are good things. I can know that and still wish the other one."''',
      c('"Tell me what you miss about having them together."', "miss"),
      c('"Would you like company while you feel disappointed? We do not have to fix it."', "company")),
    n("miss", "Ember", '''"They made each other laugh. When they were carrying the table, Dervan said its short leg was trying to go home. Vessa told him to ask where it lived and take the rest with it."
{n}Ember smiles at the memory, then looks down.{/n}
"I don't know whether they will do that again. I keep wanting to remind them, as though they have forgotten. But they remember. They were there."
{n}She folds the paper into a crooked square.{/n}
"Sometimes I think if I find the right words, everything will stop hurting. Then somebody asks me a question and I want the words even more."
"What would you like from me?"
"You could tell me when you don't have them either. I don't want to be the only person who is trying to think of an answer."
{n}You sit with her. After a while she begins watching the sparrows, and the fold in the paper relaxes beneath her hands.{/n}''',
      c('"Admit that you do not know whether they will be friends again."', flags=("ember.disappointment_named", "ember.afternoon_without_answer"))),
    n("company", "Ember", '''"Yes. Only I might talk about it again."
{n}You say that is all right. Ember leans her shoulder against the wall behind her and watches a sparrow try to carry a crumb too large for its beak.{/n}
"He should break it."
{n}The bird drops it, hops backward, and tries again from a different side.{/n}
"I suppose I can let him work it out."
{n}She laughs quietly. A little later she asks whether you have ever apologized and still wanted the other person to stop being cross sooner than they did. You tell her what you are willing to remember.{/n}
"Oh," {n}she says.{/n} "I thought you might have. But people are so quick to agree with you that I wasn't sure."
{n}She listens without deciding what the other person ought to have done. When you finish, the sparrow has finally managed its crumb.{/n}
"We missed it," {n}Ember says.{/n} "He didn't need us to watch after all."''',
      c('"Stay beside her until you both feel ready to leave."', flags=("ember.disappointment_shared", "ember.afternoon_without_answer"))),
], requires=("ember.covering_settled", "ember.a_question_at_the_yard"), delay=48)


s("the_person_in_the_title", "What the Commander would like",
  '"You asked to see me?"', [
    n("start", "Ember", '''"Yes. You looked tired before. I thought you might still be tired."
{n}Ember has found a quiet place beside the courtyard wall. There is a cup of water on the ledge and a folded cloth to sit on. She notices you examining the arrangement.{/n}
"I asked before borrowing them. Pella wants the cup back. You may be tired, but you still have to return things."
{n}She sits, then moves the cloth so you can choose the less dusty part.{/n}
"I thought we could do something you like. Only I started thinking of things I like. That might not be the same."
{n}She waits until you sit or stand where you are comfortable.{/n}
"Do you want to talk? Or do you want me to talk? Or do you want nobody to talk for a while? I can try that last one. I might forget."''',
      c('"I am afraid of disappointing people who trust me."', "fear"),
      c('"Distract me. Tell me something unimportant."', "distraction"),
      c('"Quiet company would help."', "quiet"),
      c('"I cannot stay now. Thank you for thinking of me."', abort=True)),
    n("fear", "Ember", '''"Is it something you did, or something you are afraid you might do?"
{n}You explain as much as you choose. Ember listens, her attention occasionally drawn to a sound in the street before returning to you. She does not look as though she is preparing an answer large enough to cover everything.{/n}
"I think I would be afraid too," {n}she says.{/n}
{n}For a moment that is all. Then she asks which part can be done today. The question is practical, almost disappointing after the size of what you have told her.{/n}
"You don't have to do it now. I wanted to know whether we were sitting beside something that would get worse while we waited."
{n}You name one thing that can wait and one that cannot. She nods.{/n}
"Then perhaps we can have the time before you need to do the second one. I won't tell you it will all be right. I would like it to be. I don't know how to promise it."
{n}She passes the cup when you reach for it. The water is cool enough to be pleasant.{/n}''',
      c('"Thank her for listening without promising."', "fear_end")),
    n("fear_end", "Ember", '''"Will you tell me later? How the thing went?"
{n}You say you will tell her what you can. She smiles, then hastily explains.{/n}
"Not because I need you to come back with a good answer. I wanted to know whether you would still want company if it went badly."
{n}The question catches you more sharply than the earlier ones. You tell her whether you usually seek people out or hide when you are disappointed in yourself.{/n}
"I could ask," {n}she says.{/n} "And you could say no if you didn't want me there. That might be easier than deciding I already know."
{n}When it is time to go, she takes the cup back to Pella. She does not call after you with a last piece of advice. The promise she has made is small enough to remember.{/n}''',
      c('"Agree that she can ask how you are doing."', flags=("ember.commander_confided", "ember.care_received"))),
    n("distraction", "Ember", '''"Soot stole a string."
{n}She says it with the satisfaction of someone who has found exactly the right subject.{/n}
"She did. I know because she brought it to me, and then the woman who owned it came looking. She wanted me to admire it. I told her it was a very good string and she had to give it back."
{n}The crow is not present to defend herself. Ember explains that she placed it just out of her reach, then pretended to become interested in a beetle.{/n}
"I can forgive her and still move the string. She doesn't like that part."
{n}You ask whether she returned it. She did, after asking the woman to describe the color. It was the correct string, although Soot seemed to consider the inquiry an insult to her taste.{/n}
{n}The story becomes a discussion of things the crow might be collecting in places Ember has not found. You suggest a particularly improbable object. She laughs, then looks genuinely worried that she might manage it.{/n}
"Don't tell her. I want to go on being welcome in that street."''',
      c('"Stay for another small story."', "distraction_end")),
    n("distraction_end", "Ember", '''{n}The next story is about Ember herself. She mistook a folded apron for a sleeping cat and spent several minutes keeping people from putting things on it. The apron was eventually claimed by a woman who wished somebody had been as careful with the real cat, which had stolen her supper.{/n}
{n}Ember laughs before the end. You have to ask her to repeat part of it. She does, badly imitating the woman's voice, then apologizes to an absent person for making her sound like a goose.{/n}
"Are you still tired?"
{n}You tell her the truth. She nods without looking defeated.{/n}
"I didn't think the apron would fix everything. I just thought you might like it."
{n}When you rise, she asks whether she may tell you the next foolish thing that happens. You say yes. She seems pleased enough with that answer.{/n}''',
      c('"Thank her for the distraction."', flags=("ember.commander_distracted", "ember.care_received"))),
    n("quiet", "Narrator", '''{n}Ember folds her hands loosely and watches the street. For a few moments the effort of not speaking is almost audible. Then something catches her attention beyond the courtyard, and she relaxes into looking at it.{/n}
{n}You sit together. A cart passes. Someone argues with a shutter. Pella comes to the doorway, sees the two of you, and returns to her work without asking a question.{/n}
{n}After a while Ember moves the cup closer to your hand. She does not insist that you drink. When you do, she smiles and returns to watching a patch of light move across the wall.{/n}
{n}The quiet lasts until you decide it has been enough. Ember looks up when you stand.{/n}
"I nearly told you three things. I can keep them for another time."
{n}You thank her. She begins to shake the dust from the cloth, then stops when she realizes she is sending it toward your clothes. Her apologetic expression makes you both laugh.{/n}''',
      c('"Help her return the borrowed things."', flags=("ember.commander_quiet", "ember.care_received"))),
], requires=("ember.afternoon_without_answer", "ember.what_did_not_mend"))


s("the_words_people_keep", "A story told without its owner",
  '"Is something troubling you?"', [
    n("start", "Ember", '''"Someone told a story about me. I was in it, but I don't think I was there."
{n}Ember sits with a loose thread wound around one finger. She unwinds it when she notices you looking.{/n}
"The woman said I had told a man exactly what to do, and then everything became good. I told her I didn't remember saying it. She said perhaps I hadn't known I was wise."
{n}Ember frowns.{/n}
"I didn't know how to answer that. If I say I don't know, she thinks it proves the story."
{n}She lays the thread on the wall rather than winding it again.{/n}
"I like it when something I say helps somebody. I don't like it when they put words in my mouth and then ask me to say them properly. I have enough trouble with the words that are really mine."
{n}Soot lands nearby and inspects the thread. Ember moves it out of reach without interrupting the conversation.{/n}''',
      c('"What did you want the woman to understand?"', "woman"),
      c('"Has this happened with stories about your captivity?"', "captivity", requires=("ember.native_q1_complete",)),
      c('"People have told stories about your meeting with Nocticula too."', "nocticula", requires=("ember.native_q2_complete",))),
    n("captivity", "Ember", '''"Sometimes. They make it sound as though I went there because I knew what would happen. I didn't know."
{n}She looks down at her hands.{/n}
"When people are frightened, they want somebody else to know. I wanted you to know where I was. That is different from knowing how everything would end."
{n}She is quiet for a moment. You wait rather than supply a description of her courage.{/n}
"I can be glad I met someone and still wish they hadn't hurt people. I don't want the story to need the hurting."
{n}Soot nudges the thread. Ember gives her a smaller loose piece from the end, after checking that nothing remains tied to it.{/n}
"There. She can have that one. It won't become a lesson unless she swallows it."
{n}Her smile returns briefly before she thinks of the woman again.{/n}''',
      c('"What did you want to tell her?"', "woman")),
    n("nocticula", "Ember", '''"They like that one because she is important. I think she would like them saying that part."
{n}Ember's smile fades into thought.{/n}
"I wanted her to be less unhappy. People ask whether I made her good. I don't know how to make somebody be good. I can talk to them. They have to live when I stop talking."
{n}She looks at you.{/n}
"You were there. You know I wasn't giving her orders. If someone tells it that way, will you say so? You don't have to make another story where I knew everything."
{n}You agree. Ember seems relieved, though she does not expect the agreement to stop every account of the meeting from changing as it travels.{/n}
"I hope she has someone to talk to when she doesn't feel important. It would be lonely never to be allowed to be anything smaller."
{n}Soot nudges the loose thread. She moves it aside again.{/n}''',
      c('"Ask what she wanted the woman here to understand."', "woman")),
    n("woman", "Ember", '''"That I can remember not knowing what to do. And that the man in her story helped himself too. He had to get up the next morning and do something when I wasn't watching."
{n}She scratches a mark in the dust with a small stone, then rubs it away.{/n}
"If I say that, do you think she will hear it?"
"She might."
"Yes. That is what I think. I wanted you to say she would."
{n}Ember smiles ruefully. She asks whether you will come with her if the woman is still at the kitchen. You agree, and she takes the thread to return it to Pella before you leave.{/n}
{n}The woman is there. Her name is Leth. She listens while Ember explains that she does not recognize the instruction in the story. Leth begins to say something about wisdom, then stops when Ember asks her to let the sentence finish.{/n}
"I would like you to tell the part he did," {n}Ember says.{/n} "He was there when I wasn't."''',
      c('"Let the woman ask Ember her own question."', "listen"),
      c('"Support Ember\'s correction with a short account of what you have seen."', "support")),
    n("listen", "Ember", '''"Then what should I tell my sister?" {n}Leth asks.{/n} "She won't leave a bad situation. I thought if it came from you..."
{n}Ember's expression changes. The borrowed story has finally reached the person it was meant to move.{/n}
"Tell her you want her to be safe. Ask what would make leaving possible. If you need somewhere for her to go, we can ask. I don't want you to tell her I already know what she has to do. I haven't met her."
{n}Leth sits. She begins explaining the difficulty in a less certain voice. Ember listens for a while, then asks whether the sister wants to speak to anyone here herself.{/n}
{n}When you leave, nothing has been decided for the absent woman. Leth has agreed to ask before bringing her, and Ember has agreed to listen if she wants to come.{/n}
"That was harder than saying something wise," {n}Ember tells you.{/n} "I think it was more useful."''',
      c('"Walk back with her after the real conversation."', flags=("ember.story_listened", "ember.words_owned"))),
    n("support", "Ember", '''{n}You tell Leth that you have seen Ember ask questions and change her mind. The woman looks disappointed at first, then asks what use the story is if it cannot tell her sister what to do.{/n}
{n}Ember asks about the sister. She listens to the account of a bad situation, then says she would rather meet the woman than lend an instruction to someone who has not asked her for one.{/n}
"She might not come," {n}Leth says.{/n}
"Then ask what else she would like. I can help you ask about a safe place. I can't make her want to tell me things."
{n}Leth agrees to speak to her sister. As you leave, Ember thanks you, then adds something more quietly.{/n}
"She listened when you said you had seen it. I wanted her to hear me too. I think she did in the end."
"If I get stuck next time, could you give me a moment before helping? I might need a little longer to find the words."''',
      c('"Agree to notice, and let her tell you when you miss it."', flags=("ember.story_supported", "ember.words_owned"))),
], requires=("ember.care_received", "ember.the_person_in_the_title"))


s("a_letter_with_no_road", "Where an invitation can go",
  '"You have been looking at that paper for a long time."', [
    n("start", "Ember", '''"I know what I want to say. I don't know where to send it."
{n}Ember shows you a short letter. The writing is uneven, with one word crossed out so thoroughly that it has become a small dark window. At the bottom she has drawn a bird with a very clear, ordinary number of legs.{/n}
"It is for a woman I knew in Kenabres. She used to mend things near the place where I slept. Once she gave me a whole spool of thread because she said I would lose anything smaller."
{n}She touches the dark crossed-out word.{/n}
"I wrote that I remembered her. Then I thought it sounded as though I only remembered her now. I remembered before. I just didn't write."
{n}The last place Ember heard of the woman was a roadside shelter. The traveler who brought that news has already gone. Nobody has a current address.{/n}
"Her name is Anet. She might not want a letter. I would like her to be able to say so."''',
      c('"Ask the travelers who use Vessa\'s room. Someone may know the shelter."', "travelers"),
      c('"Leave a copy with a carrier who agrees to ask along that road."', "carrier"),
      c('[Trickster] "We could ask a lost road whether it remembers her footsteps."', "road", requires=("trickster",))),
    n("travelers", "Narrator", '''{n}Vessa lets Ember place a notice beside the cupboard, provided it does not ask travelers for money or promise that someone is waiting to receive them. Ember writes Anet's name and the last shelter she heard of. She asks people to leave word if they know where the woman went.{/n}
{n}For several days the notice acquires no answer. Then a traveler recognizes the shelter. It closed after its roof became unsafe. People moved to different places, and he does not remember Anet.{/n}
{n}Ember copies the names of two later stopping places. She leaves the original letter unsent and thanks him for telling her what he actually knows.{/n}
"That is farther than we got before," {n}she says.{/n} "It doesn't feel farther. I thought there might be an answer with her in it."
{n}You help her make a second notice, leaving room for another traveler to add something useful.{/n}''',
      c('"Keep asking without promising that the search will find her."', flags=("ember.letter_inquiries", "ember.letter_started"))),
    n("carrier", "Ember", '''{n}A carrier who regularly uses the road agrees to ask at the shelter and leave a copy of the letter where someone might recognize the name. Ember reads it over before handing it to him.{/n}
"If you find her, will you ask whether she wants it? You don't have to tell her she must answer because I waited."
"I can ask," {n}he says.{/n} "I can't promise I'll find her."
"I know. I wanted to say the other part too."
{n}The carrier takes the copy. Ember keeps the original, including the dark crossed-out word. She folds it carefully and asks you whether the bird looks recognizably like a bird.{/n}
{n}You say what you think. She laughs at the crooked beak, then folds that corner inside where it will not catch against anything.{/n}
"I hope she laughs at it. If she gets it. I can hope that part now."''',
      c('"Leave the copy with the willing carrier."', flags=("ember.letter_carrier", "ember.letter_started"))),
    n("road", "Ember", '''"Would it bring her here? What if she was busy?"
{n}You explain that you mean to ask for a direction, not to pull a person along it. Ember considers the distinction, then puts the letter flat between you.{/n}
"Can it say it doesn't know?"
"It might."
"Then we can ask. I don't want a road that makes up an answer because you are the Commander."
{n}You fold the paper until the line naming the old shelter rests along its crease. For a moment the crease continues beyond the page, a thin road drawn across the paving. Tiny footprints travel its length. They stop at a branching, turn back, then choose another way.{/n}
{n}Ember watches without stepping on it. The road reaches a small square shadow that belongs to no building nearby. Letters appear along its edge, naming a place farther from Kenabres than the original shelter.{/n}
{n}Then the page lifts in an ordinary breeze. The road is gone. Ember catches the paper before it blows away.{/n}''',
      c('"Copy the place name and ask a real traveler whether the road exists."', "road_checked")),
    n("road_checked", "Narrator", '''{n}The carrier recognizes the name. There is a waystation there, used by people traveling between smaller settlements. He will ask about Anet when he passes, if Ember wants him to take a copy of the letter.{/n}
"Yes," {n}she says.{/n} "If she is there, ask whether she wants it."
{n}The man takes the copy. Ember keeps the original, which now has an extra crease through the bird.{/n}
"I liked the little footprints," {n}she tells you.{/n} "I wanted to follow them. But they weren't her. They were a way to ask somebody where she might be."
{n}She opens the page once more, looking for any mark the impossible road left behind. There is only the crease.{/n}
"Could we do something like that just for fun another day? A road that goes around a cup and comes home again. It wouldn't have to find anybody."
{n}She turns the cup upside down to show you where the little road might go.{/n}''',
      c('"Promise to try a small, harmless road another afternoon."', flags=("ember.letter_trickster", "ember.letter_started"))),
], requires=("ember.words_owned", "ember.the_words_people_keep"), delay=48)


s("an_answer_from_elsewhere", "The life at the other end",
  '"Has there been any news of Anet?"', [
    n("start", "Ember", '''{n}Ember brings out the folded original of her letter. Its edges have softened from being opened and put away.{/n}
"There has been news. I wanted to tell you before I decided what to do next."
{n}She sits beside you. The bird on the page has acquired a small stain across one wing, which she touches with the tip of a finger before unfolding the rest.{/n}''',
      c('"Ask what the travelers learned from the notices."', "inquiries", requires=("ember.letter_inquiries",)),
      c('"Ask what the carrier found."', "carrier", requires=("ember.letter_carrier",)),
      c('"Ask about the waystation at the end of the impossible road."', "trickster", requires=("ember.letter_trickster",))),
    n("inquiries", "Ember", '''"Someone knew her at the second place. She had gone before he arrived again. He said she was traveling with a woman who sold buttons."
{n}Ember points to a new name written beneath the old shelter's.{/n}
"I don't know whether that is where she went or where the other woman came from. He didn't know either. I asked twice before I remembered that asking again would not make him remember something he hadn't heard."
{n}She folds the letter halfway, then opens it again.{/n}
"I would like to keep asking. But I don't want every afternoon to be waiting for someone who knows the next bit. I can leave the notice and do other things."
{n}She looks at you, worried that this might sound like abandoning the woman.{/n}
"If she is having a good day somewhere, I don't have to stop having one here. Do I?"
{n}You say that you do not think so. Ember lets out a breath and smooths the paper.{/n}''',
      c('"Keep the notice available without making the search her whole day."', "unanswered")),
    n("carrier", "Ember", '''"The shelter was shut. He found the people who had taken its cooking pots away, and one of them remembered her. She went with a trader. They didn't know which road."
{n}Ember shows you the carrier's short note. He has left the copy of her letter with a woman who agreed to pass it on if Anet returns.{/n}
"He said he could try again next time he passes. I told him to ask if it was easy to ask. I don't want him to spend all his work looking."
{n}She turns the original over. There is no address on the back, only a little mark where she tested the ink.{/n}
"I hope she knows someone is pleased to see her when she arrives. Even if she doesn't know I wrote."
{n}She asks whether you think it is foolish to keep a letter that may never be delivered. You tell her what you think, and she listens before choosing to keep it anyway.{/n}
"I wrote things I meant. I would like to remember how I said them."''',
      c('"Leave the copy with the willing keeper and retain the original."', "unanswered")),
    n("trickster", "Ember", '''"She was there. The carrier found her."
{n}Ember has a reply, shorter than the letter she sent. Anet remembers her and is glad to hear she is alive. She is working at the waystation for now. She asks Ember not to travel to find her; the roads are difficult, and she may move again before anybody arrives.{/n}
"She said I can write if I want. She might not answer quickly. Her hands get sore after work."
{n}Ember reads that part again, then carefully folds the reply.{/n}
"I wanted her to say she was coming. I didn't write that in mine. I think she knew I might want it."
{n}She looks at you with a smile that holds both pleasure and disappointment.{/n}
"The road helped us ask. It couldn't decide what she would say. I'm glad it didn't. This sounds like her. She used to tell people when they were making too much work for her hands."
{n}There is one more line in the reply. Anet likes the bird. She wants to know why it looks as though it is waiting for an argument.{/n}''',
      c('"Help Ember write an answer that does not promise a visit."', "reply")),
    n("unanswered", "Ember", '''{n}Ember puts the original away. She leaves the notice or the held copy where it can still do some good, then asks whether you have time for a walk that is not a search.{/n}
"We can look at things without asking whether they know her. I nearly asked a woman because she had the same color shawl. That wouldn't have helped either of us."
{n}You walk toward the quieter streets. Ember points out a window where someone has hung strips of cloth to keep the sun out. The colors change as the wind moves them.{/n}
"I would like Anet to see that. I can tell her if I find her. I can also show you now."
{n}You stand together until the wind drops. Ember begins describing which colors she would choose if the window were hers. She chooses too many, notices, and starts arguing with herself about which one to leave out.{/n}''',
      c('"Enjoy the window with her today."', flags=("ember.letter_still_open", "ember.answer_kept"))),
    n("reply", "Ember", '''{n}Ember explains that the bird has spent too much time listening to Soot. She tells Anet about the room for travelers and asks whether there is anything she would like to hear next. Then she stops before adding a question about every detail of the waystation.{/n}
"She said her hands hurt. I don't want to give her a whole book to answer."
{n}The new letter is short enough to fit on one page. Ember asks the carrier when he expects to go that way again and accepts that he does not yet know.{/n}
"It can wait here. The waiting doesn't have to be unhappy every minute."
{n}Later she asks about the little road around a cup. She has found a clean scrap of paper and placed the cup in its center.{/n}''',
      c('"Make a road with folded paper and let Ember supply its traveler."', "paper_road"),
      c('[Trickster] "Let a tiny impossible road wander around the cup."', "another_road", requires=("trickster",))),
    n("paper_road", "Ember", '''{n}You fold the paper into a narrow path around the cup. Ember moves a pebble along it, stopping at each corner to invent a reason why the traveler has forgotten what she meant to do.{/n}
"Perhaps she wanted to come home," {n}she says when the pebble returns to its starting place.{/n} "That can be a reason too."
{n}The folded road remains on the table until the cup is needed. Ember unfolds it and puts the paper away for another afternoon. Her letter waits separately for the next willing carrier.{/n}''',
      c('"Keep her reply ready to send."', flags=("ember.anet_answered", "ember.answer_kept"))),
    n("another_road", "Ember", '''{n}The tiny road wanders around the rim, takes a completely unnecessary turn, and returns to where it began. Ember supplies a traveler who has forgotten why she went out.{/n}
"Perhaps she wanted to come home," {n}she says.{/n} "That can be a reason too."
{n}She moves one finger alongside the little path, careful not to touch it before asking. When the road fades, she checks the cup and laughs to find it still quite ordinary.{/n}
"Good. We can still drink from it."
{n}The letter waits separately for the next willing carrier.{/n}''',
      c('"Keep her reply ready to send."', flags=("ember.anet_answered", "ember.answer_kept"))),
], requires=("ember.letter_started", "ember.a_letter_with_no_road"), delay=96)


s("where_she_is_needed", "Someone who can say no",
  '"Have you decided where to spend the afternoon?"', [
    n("start", "Ember", '''"I was going to ask you. Then I thought I should decide what I wanted before asking."
{n}Ember has a little bag beside her. It contains a clean cloth, the original letter to Anet, and a few things she has found worth keeping. She has taken them out and put them back with more attention than packing requires.{/n}
"Dervan asked whether I wanted to see the window in his loft. Vessa asked whether I could come to the room. Pella wants her basket back, which isn't really an invitation. I should do that first."
{n}She looks toward the street.{/n}
"There are other people asking too. I used to think being wanted always meant I should go. Now I think it means somebody wants me to go. I still have to answer."
{n}She gives you a small, uncertain smile.{/n}''',
      c('"How do you feel about what the Redeemed might want from you now?"', "good", requires=("ember.native_q3_complete", "ember.native_good")),
      c('"Are you worried that people might be afraid of you?"', "law", requires=("ember.native_q3_complete", "ember.native_law")),
      c('"What would you like to do today?"', "today")),
    n("good", "Ember", '''"I want them to help each other. I don't want to be the answer to everything they have to do next."
{n}She sets the cloth inside the bag.{/n}
"They helped each other when they thought I wasn't there to help them. They can remember that. I would like to see them sometimes. I would like to hear what they did when nobody was waiting for me to tell them."
{n}Ember looks at you.{/n}
"If you visit somebody because you want to see them, they might tell you something they like. If you visit because everybody has stopped until you arrive, you spend all your time trying to make them begin again."
{n}She smiles at the bag, remembering something.{/n}
"Dervan wanted me to see a shelf. It was a very ordinary thing to want from me. I liked being asked."
{n}She closes the bag and leaves it beside her rather than getting up at once.{/n}''',
      c('"Ask which ordinary invitation she wants to accept."', "today")),
    n("law", "Ember", '''"I am. I don't want to learn to like it when someone is afraid of me."
{n}She looks at her hands. The pause is longer than the words that follow.{/n}
"I wanted the fighting to stop. It stopped. I can be glad people lived and still wish I had not frightened them. If someone says I should do it again every time they won't listen, I don't want that to become easy to hear."
{n}You sit with her while she finds the next thought.{/n}
"Dervan knows I can do things he can't. He still told me not to make a speech about him. I was glad he could say that. I would be sad if all my friends started thanking me before they knew what I was going to do."
{n}She turns the bag's fastening between her fingers.{/n}
"You can tell me if I make you afraid. I might not like hearing it. I would still want to know."
{n}There is no new spell in the room, and no request for her to prove what the old one accomplished.{/n}''',
      c('"Agree to speak honestly, then ask what she wants today."', "today")),
    n("today", "Ember", '''"I want to see the window. He asked because he wanted to show me something, not because he thought I could make the room better."
{n}She picks up Pella's basket, which has been waiting at her feet.{/n}
"And then I want a little time with you. We can do the two things without making Dervan come to Vessa's room first."
{n}You return the basket, then walk to the yard. Dervan meets you below the loft and asks you to wait while he checks that the other lodger is willing to receive visitors. She is, provided nobody touches the boots drying by the window.{/n}
{n}The window looks over a low wall and several yards. There is nothing magnificent about it. Dervan has put a small jar on the sill with a green cutting in it.{/n}
"Mara gave me that," {n}he says.{/n} "I carried water for the kitchen. She said it might take root."
{n}Ember bends to look at the cutting. A fine pale root has begun to reach down through the water.{/n}''',
      c('"Ask Dervan what he likes about the view."', "view"),
      c('"Let Ember and Dervan talk while you look out."', "listen")),
    n("view", "Ember", '''"I can see the gate before someone knocks," {n}Dervan says.{/n} "That sounds suspicious, doesn't it?"
"It sounds useful," {n}Ember answers.{/n}
{n}He shows her the shelf, the place where the roof stays dry, and the awkward nail that caught his shirt on the first night. She laughs at his imitation of the shirt refusing to let him go to work.{/n}
{n}The visit is short. Dervan has things to do, and the other lodger wants to close the window before the evening cools. At the door he tells Ember that she may come again, though not every day. He is enjoying having somewhere he does not have to explain himself.{/n}
"Then I will ask first," {n}she says.{/n}
{n}Outside, she seems pleased by the qualification rather than rejected by it.{/n}
"He can say when he wants company. That is a good thing about having a door."''',
      c('"Walk back together."', flags=("ember.deren_visited", "ember.wishes_answered"))),
    n("listen", "Narrator", '''{n}Dervan asks about the missing covering. Ember tells him what happened without turning the account into a reason to visit Vessa. He listens, nods, and says he is glad the room is working.{/n}
{n}Then he shows Ember how the window catches the afternoon light. The cutting's shadow makes a shape on the wall much larger than the plant itself. She moves one leaf to see whether the shadow changes as she expects.{/n}
"It is very tall over there," {n}she says.{/n}
"Cheaper than growing a tree."
{n}They laugh. When the visit ends, Dervan says she may come again if she asks when he is free. Ember agrees without adding an expectation that he become easier to visit somewhere else.{/n}
{n}You leave the loft as it was, with a cutting in a jar and two people who might enjoy another ordinary conversation.{/n}''',
      c('"Return with Ember, without carrying another request for Dervan."', flags=("ember.deren_visited", "ember.wishes_answered"))),
], requires=("ember.answer_kept", "ember.an_answer_from_elsewhere"), chapters=(5,), delay=48)


s("the_afternoon_not_promised", "Something you can ask for",
  '"We kept the time you asked for."', [
    n("start", "Ember", '''"We did. I nearly filled it with another thing before we got here."
{n}Ember settles beside you in the sheltered courtyard. She has brought nothing that needs finishing and nobody who needs an answer. Soot has found a place above the door from which she can watch both of you.{/n}
"I wanted to say thank you. Then I started thinking about how to say it properly, and it began to sound like I was thanking the Commander for helping a great many people."
{n}She makes a face at the invisible speech.{/n}
"I am glad you helped. But I wanted to thank my friend for coming when I wanted company. That is a smaller thing to say, and I like it better."
{n}She looks at you directly.{/n}
"I hope you still want me to ask. You can ask me too. I might be busy. I would still like to be asked."''',
      c('"I want to keep being your friend, even when neither of us has an answer."', "promise"),
      c('"I care about you. I cannot promise how often I will be here, but I will answer honestly."', "honest")),
    n("promise", "Ember", '''"Good. I have been wrong about quite a lot of things lately. It would be inconvenient if I had to stop having friends until I got them all right."
{n}She smiles, then considers the promise more seriously.{/n}
"If I want to be alone, I will try to tell you. If I say something that hurts you, I would like you to tell me. I don't want everybody to be kind to me by pretending I never hurt anybody."
{n}You agree. She does not ask for a vow that neither of you will die, disappear, or change. She asks whether you have time for the small thing you began together.{/n}''',
      c('"Try the uneven tune again."', "whistle", requires=("ember.shared_whistle",)),
      c('"Set out the two sets of stones."', "stones", requires=("ember.shared_stones",))),
    n("honest", "Ember", '''"That is a good promise. It has something you can actually do in it."
{n}She looks up at Soot, who has begun examining a crack above the door.{/n}
"Sometimes I want someone to promise they won't go away. Then I remember all the places I want to go. I don't want being my friend to mean staying on the same piece of paving forever."
{n}She returns her attention to you.{/n}
"Tell me when you can. If I don't know where you are, I will miss you. That doesn't mean I will have stopped being glad we met."
{n}For this afternoon, you are both here. She asks whether you would like to try the small thing you began together before there are any more promises to discuss.{/n}''',
      c('"Try the uneven tune again."', "whistle", requires=("ember.shared_whistle",)),
      c('"Set out the two sets of stones."', "stones", requires=("ember.shared_stones",))),
    n("whistle", "Ember", '''{n}You begin the tune. Ember supplies the answer, misses a note, and starts laughing before you can finish your part. Soot turns her head sharply toward the sound.{/n}
"We have not become more impressive," {n}she says.{/n}
{n}The next attempt is better. You leave the pause where she expects it. She changes the last note deliberately, just to see whether you will follow. You do, badly enough that both of you have to stop again.{/n}
{n}Later she asks how you have been since the afternoon when you were tired. You tell her what you choose to tell. She listens, then asks whether you want to talk more or try the tune again.{/n}
{n}The question remains yours to answer. When the day grows late, you walk together to return a borrowed cup, and Ember hums the tune until she forgets one of the turns.{/n}
"You remember that bit," {n}she says.{/n} "I can ask you next time."''',
      c('"Keep the next invitation possible."', flags=("ember.trusted_friend", "ember.campaign_developed"))),
    n("stones", "Ember", '''{n}You set the stones in their circle. Ember turns her set pale side up, pauses, and asks whether you kept yours together. She seems pleased that you did.{/n}
{n}The first round goes quickly. She remembers the turns this time, but makes a move that lets you win. She studies the position until she sees it, then demands another round in a voice that is only half joking.{/n}
"I know what I did. I want to try not doing it."
{n}The second round lasts longer. Between moves, she asks how you have been since the afternoon she found you tired. You tell her what you choose. She listens without forgetting whose turn it is, a success she points out with considerable pride.{/n}
{n}When it is time to leave, you divide the stones again. Ember puts her half in the little bag with the things she intends to keep.{/n}
"We don't have to finish everything today," {n}she says.{/n} "I would like there to be another game."''',
      c('"Keep your half until the next afternoon."', flags=("ember.trusted_friend", "ember.campaign_developed"))),
], requires=("ember.wishes_answered", "ember.where_she_is_needed"), chapters=(5,), delay=48)


s("a_place_to_sit", "A visit after the crying",
  '"May I sit here for a little while?"', [
    n("start", "Narrator", '''{n}Ember sits near the wall with Soot beside her. Her eyes are swollen from crying. She looks up when you speak, then toward the empty place you indicated, as though making certain you mean that particular piece of ground.{/n}
"There?"
{n}You nod. She draws her knees closer and leaves room. Soot turns her head toward you but stays beside her.{/n}
{n}For a little while, neither of you speaks. Ember picks at a loose thread, stops, and rubs her cheek with the back of her hand. Her breathing catches before she can settle it again.{/n}
"I don't know what to say."
{n}She sounds frightened of what will happen if there is no answer. You remain where she allowed you to sit.{/n}''',
      c('"You do not have to tell me anything. I can stay quietly."', "quiet"),
      c('"I have said cruel things. I will not ask you to comfort me about them."', "responsibility"),
      c('"Would you like me to fetch some water?"', "water")),
    n("responsibility", "Ember", '''{n}Ember looks at you, then away. She does not answer the apology with forgiveness. Her fingers close around the loose thread until she notices it pulling at her dress.{/n}
"Are you angry?"
"No."
{n}She listens to the answer for a moment before looking at the place beside her again.{/n}
"You can sit."
{n}You sit without explaining how much the permission means to you. Soot shifts closer to her arm. Ember watches her until she can follow her movements without looking back at your face.{/n}
{n}After a while she asks whether anyone else is coming. You tell her that you have invited nobody. If someone approaches, you will ask what she wants before making the visit larger.{/n}''',
      c('"Remain quietly where she permitted you to sit."', "quiet")),
    n("water", "Narrator", '''{n}Ember nods. You tell her where you are going and return with a cup of water. She takes it in both hands, carefully, and drinks only a little before lowering it to her lap.{/n}
"Thank you."
{n}She looks toward the street. A distant shout makes her shoulders draw inward. You wait until she looks at you before asking whether she would rather move somewhere quieter.{/n}
"Not far."
{n}You find a more sheltered place around the corner, close enough for her to recognize the way back. Soot follows. Ember carries the cup herself and sits before trying another sip.{/n}
{n}When the street becomes quiet again, she loosens her grip on the cup. You remain beside her without asking whether she feels better now.{/n}''',
      c('"Let her decide when she has had enough company."', "leave")),
    n("quiet", "Narrator", '''{n}The afternoon moves slowly. Ember watches Soot work a little piece of grit loose from the wall. Once she starts to say something and stops. You do not ask her to begin again.{/n}
{n}A passerby looks toward her. You stay where you are, leaving Ember room to see who is approaching. The person moves on. She follows the footsteps with her eyes until they are gone.{/n}
"He didn't need anything."
{n}The observation seems to surprise her. Soot returns to her side, and Ember strokes the crow's feathers with a familiar, careful movement.{/n}
{n}You ask whether she wants you to remain. She nods this time without first checking the space beside her. You stay until she begins looking toward the place where she rests.{/n}''',
      c('"Ask whether she would like the visit to end."', "leave")),
    n("leave", "Ember", '''"I think I want to sleep."
{n}She says it uncertainly, as though the wish might require a better reason. You tell her that you will go. If she wants another short visit, she can say so when you ask.{/n}
"You can ask."
{n}Soot climbs onto her shoulder. Ember stands slowly, finding her balance before taking a step. You do not reach for her unless she asks. When she pauses, you wait with her.{/n}
{n}At the end of the visit she looks back once. There is no promise that the next day will hurt less. There is a place where you sat because she allowed it, and a question she has said you may ask again.{/n}''',
      c('"Leave when she asks to rest."', flags=("ember.started", "ember.care_visits_allowed"))),
], requires=("ember.native_q3_complete", "ember.native_devastated"), chapters=(5,), care=True, delay=24)


s("the_small_choice", "The cloth beside her",
  '"Would you like a little company today?"', [
    n("start", "Narrator", '''{n}Ember is sitting where the light reaches the wall. Soot rests nearby. She notices you before you speak, and her expression shifts between recognition and uncertainty.{/n}
"A little."
{n}You sit in the place she indicates. Someone has left a clean cloth beside her, folded into a square. She turns it once, then puts it back as though she has forgotten what she meant to do with it.{/n}
"It keeps coming undone."
{n}One folded edge opens as she puts it down, then another. Ember lets the cloth lie unfolded beside her, her fingers resting at its edge.{/n}''',
      c('"Would you like me to fold it with you?"', "fold"),
      c('"We can leave it as it is. Would you rather watch Soot?"', "soot"),
      c('"I can come another time if you would rather be alone."', "alone")),
    n("alone", "Ember", '''"Not yet."
{n}She moves the cloth aside, clearing a place for your hand if you want to rest it on the wall. She does not take it. Soot makes a quiet sound, and she turns toward her.{/n}
"She's here."
{n}You answer that she is. Ember watches the crow until the effort of deciding what to do with the cloth has passed. When you ask again whether she wants help, she shakes her head.{/n}
"Just that."
{n}She means the sitting, and you remain. The cloth stays unfolded beside her.{/n}''',
      c('"Watch the crow with her."', "soot")),
    n("fold", "Narrator", '''{n}Ember lets you take one corner. You ask which way she wants it folded and wait for her to show you. Her first gesture is uncertain. Then she brings her corner toward yours.{/n}
{n}The edges do not meet evenly. She notices and starts to pull them apart. You keep your hand still until she decides whether to try again.{/n}
"It can be like that."
{n}You set the folded cloth beside her. She smooths it once, then leaves it.{/n}
{n}A little later she asks where the water cup is. You show her, and she takes it herself. The cloth remains folded while she drinks.{/n}''',
      c('"Stay until she has finished her drink."', "fold_end")),
    n("fold_end", "Ember", '''"Will it stay?"
{n}She is looking at the cloth. You say it will probably stay folded unless somebody moves it. Ember considers that, then lays a small stone on one corner.{/n}
"There."
{n}It is an ordinary solution to an ordinary problem. Her attention wanders away from it before she can decide whether she is pleased. She rubs her cheek and asks whether you will be angry if she cries again.{/n}
{n}You say no. When the tears come, you remain where she asked you to sit. There is no unfinished explanation you need her to hear first.{/n}
{n}Later, when she wants to rest, she leaves the cloth beneath its little stone. You say goodbye and let the visit end.{/n}''',
      c('"Leave the cloth as she arranged it."', flags=("ember.care_folded", "ember.care_choice_kept"))),
    n("soot", "Narrator", '''{n}Soot investigates the edge of the wall, walking with careful steps. Ember watches her stop beside a pale pebble and turn it with her beak. When it proves uninteresting, she moves on.{/n}
{n}She makes a small sound that might have become a laugh on another afternoon. It does not become one now. The crow returns to her shoulder, and she strokes the feathers beneath her beak.{/n}
"She knows me."
{n}You stay quiet while she repeats the movement. After a while she asks whether you can move the cloth farther from the edge so it will not fall. You do, and show her where you put it.{/n}
{n}When she asks to rest, you leave the crow with her. The cloth is safe beside the wall, still unfolded.{/n}''',
      c('"Say goodbye when she has had enough company."', flags=("ember.care_watched", "ember.care_choice_kept"))),
], requires=("ember.native_q3_complete", "ember.native_devastated", "ember.care_visits_allowed", "ember.a_place_to_sit"), chapters=(5,), care=True, delay=48)


s("the_visits_she_can_end", "A familiar question",
  '"May I sit with you again?"', [
    n("start", "Ember", '''"For a little while."
{n}Ember makes room beside her. She knows where you usually sit now. The cup is within reach, and the clean cloth rests nearby. Soot watches from the wall.{/n}
{n}She looks toward the street before asking whether anyone has sent you. You say that you came to ask whether she wanted company. She waits, then nods as though she has found the part of the answer she needed.{/n}
"No questions about them?"
{n}You tell her you have not come to ask her to explain the people who died. She draws a breath that catches before it settles.{/n}''',
      c('"Ask whether she wants the cloth left where she put it."', "cloth", requires=("ember.care_folded",)),
      c('"Watch Soot with her, as she chose before."', "bird", requires=("ember.care_watched",))),
    n("cloth", "Narrator", '''{n}The little stone remains on the folded corner. Ember checks beneath it, then places it back. She does not begin folding the cloth again.{/n}
"It stayed."
{n}You agree. She looks at the cup and asks whether it is the one she used before. It is the one set here for her now; you do not pretend to know every hand that moved it between your visits. She seems content with being shown where it is.{/n}
{n}For a while you sit together. Ember asks whether there will be more people coming through the street. You say there probably will, and ask whether she wants a quieter place. She shakes her head.{/n}
"I know this one."
{n}You remain in the familiar place.{/n}''',
      c('"Let the familiar afternoon continue."', "end")),
    n("bird", "Narrator", '''{n}Soot has found a small seed and is deciding whether it deserves attention. Ember follows her movements, sometimes losing the seed and waiting for Soot to show her where it went.{/n}
{n}When Soot drops it, Ember points. The crow looks at the indicated place, finds it, and carries it to the other end of the wall. Ember watches until she comes back.{/n}
"She found it."
{n}You agree. She moves the clean cloth away from the edge again, though it was already safe. Then she rests her hands and looks down the street.{/n}
{n}Soot settles beside the cloth. Ember watches her feathers lift and settle in the breeze.{/n}''',
      c('"Remain beside her."', "end")),
    n("end", "Ember", '''"You can ask another day."
{n}She says it before you ask whether she is tired. Then she adds, more quietly:{/n}
"Not every day. Sometimes I don't want people."
{n}You tell her that she can refuse. The answer will not make you demand a reason or ask her to prove she still cares. She watches your face, then looks toward the place where she rests.{/n}
"I want to stop now."
{n}You stand and say goodbye. Ember remains seated for a moment with Soot beside her. She has asked for the visit to end, and it ends.{/n}
{n}There may be other afternoons when she wants company. You will have to ask her on those days too.{/n}''',
      c('"Respect the end of today\'s visit."', flags=("ember.care_continues",))),
], requires=("ember.native_q3_complete", "ember.native_devastated", "ember.care_choice_kept", "ember.the_small_choice"), chapters=(5,), care=True, delay=48)


def ending(id, title, text, requires, forbids=(), owner="Epilogue"):
    SCENES.append(scene("ember." + id, title, owner, 1, "",
        [n("end", "Narrator", text, portrait="Ember")],
        requires=requires, forbids=forbids, last=6, Relationship="ember"))


ORDINARY = ("ember.closed", "ember_dead", "ember_gone", "ember.absent", "sacrifice", "ascended", "ember.native_devastated")
ending("ending_good_friend", "The visits she chose", '''{n}The Commander remained someone Ember could ask for an afternoon without first finding a reason to make it useful. Sometimes they talked about people she had helped. Sometimes she wanted to complain that Soot had stolen something, or show the Commander a small discovery that would mean very little to anybody else.{/n}
{n}The Redeemed continued to make choices of their own. Ember was glad when she heard good news of them, worried when the news was difficult, and unwilling to become the person whose instructions replaced their own judgment. The Commander had seen her practice saying what she wanted even when somebody hoped for a different answer.{/n}
{n}Dervan kept his distance from Vessa for a time. The room still gave travelers somewhere to sleep. Ember visited where she was invited, asked before bringing other people, and occasionally forgot to do either as carefully as she meant to. Her friends could tell her. She did not always find it pleasant, but she listened.{/n}
{n}There were days when the Commander wanted company and days when Ember did. They learned to ask. The invitations became a familiar part of lives that contained much more than their conversations.{/n}''',
    ("ember.campaign_developed", "ember.native_q3_complete", "ember.native_good"), ORDINARY)
ending("ending_law_friend", "A friend who could disagree", '''{n}Ember did not grow comfortable with people being afraid of her. She remembered the fighting that had stopped and the lives preserved, but she also remembered how quickly fear could make someone agree before they had decided what they believed.{/n}
{n}The Commander became one of the people she could ask about that uneasiness. Their friendship had room for ordinary mistakes and inconvenient answers. Ember could lose a game, admit that she wanted the missing covering found for more than one reason, or say that she did not want a visitor today. The Commander could answer honestly in return.{/n}
{n}She continued to care about the people around her without accepting every invitation to frighten them into doing right. Sometimes the work was smaller: a cup carried, a letter kept, a visit to a man pleased with his new shelf. The Commander knew why those things mattered to her.{/n}
{n}When she wanted another afternoon, she asked. She was particularly glad when the answer included an ordinary disagreement about what to do with it.{/n}''',
    ("ember.campaign_developed", "ember.native_q3_complete", "ember.native_law"), (*ORDINARY, "ember.native_good"))
ending("ending_friend", "An ordinary reason to return", '''{n}Ember and the Commander had made room for a friendship that did not depend on her having an answer for everyone who came to ask. Their afternoons held discoveries, disappointments, and small pleasures they learned to recognize in each other.{/n}
{n}The room behind the storehouse continued to require work. People arrived, left, returned borrowed things late, and sometimes found a better place to stay. Ember did not mistake every departure for a failure. She could still miss the company.{/n}
{n}The Commander remained someone she wanted to tell when a day had gone well, and someone she could ask to sit beside her when it had not. She offered the same company when it was wanted. Sometimes she guessed badly and had to ask again.{/n}
{n}There were more important histories being made around them. Their friendship also contained the particular pleasure of hearing a familiar voice ask whether there was time for something small.{/n}''',
    ("ember.campaign_developed",), (*ORDINARY, "ember.native_good", "ember.native_law"))
ending("ending_unfinished", "The next afternoon not yet arranged", '''{n}Ember and the Commander had begun keeping time for each other beyond the work of the crusade. There were still conversations unfinished and invitations postponed. She sometimes thought of something she meant to ask the next time they could sit together.{/n}
{n}She did not know what all those later afternoons would become. The ones already shared had given her reasons to want another. She remembered the Commander trying something small, being imperfect at it, and remaining good company anyway.{/n}
{n}When she had a chance, Ember asked whether they could make time again. The question was simple enough to answer honestly, even when the answer had to be later.{/n}''',
    ("ember.campaign_started",), (*ORDINARY, "ember.campaign_developed"))
ending("ending_care", "The visits she could refuse", '''{n}Ember's pain did not disappear because the Commander learned to sit quietly beside her. Some days she wanted company. On others she could not bear another person waiting for her to answer. The Commander asked and accepted the answer given.{/n}
{n}There were familiar places, a cup within reach, and small choices nobody hurried into demonstrations of recovery. Soot remained a companion whose movements could hold her attention when other things became difficult. A folded cloth could stay where she had put it until she wanted it moved.{/n}
{n}The Commander could remember earlier words and feel regret without asking Ember to make that regret easier. Care required returning to the person who was there, with the needs and wishes she could express that day.{/n}
{n}Sometimes a visit ended quickly. Sometimes she permitted it to last. When she said she wanted to stop, it stopped. That was one thing the Commander could do reliably enough for the next question to remain possible.{/n}''',
    ("ember.native_q3_complete", "ember.native_devastated", "ember.care_continues"),
    ("ember.closed", "ember_dead", "ember_gone", "ember.absent", "sacrifice", "ascended"))
ending("ending_care_unfinished", "Company not yet made familiar", '''{n}What had happened to Ember could not be put aside by remembering the afternoons the Commander had once wanted to share with her. Her distress remained part of the life in front of them. Earlier affection did not provide permission for whatever comfort the Commander wished to give.{/n}
{n}There were small questions to ask, and answers that needed to be heard without being improved. A visit might be welcome, or it might not. The Commander had not yet made those visits a familiar, dependable part of Ember's days.{/n}
{n}Whatever kindness followed would have to begin with her present wishes. There was no speech that could do that work in advance.{/n}''',
    ("ember.started", "ember.native_q3_complete", "ember.native_devastated"),
    ("ember.closed", "ember_dead", "ember_gone", "ember.absent", "ember.care_continues", "sacrifice", "ascended"))
ending("ending_departed", "A friend beyond the familiar street", '''{n}Ember was no longer with the Commander. The old places where they might have sat did not reveal where she now slept, what company she wanted, or whether another invitation could reach her.{/n}
{n}There had been time shared before the departure. The Commander could remember it without treating those memories as an address or an answer from the absent girl. She had a life beyond what the Commander could presently see.{/n}
{n}If they met again, there would be things to ask before assuming that an earlier afternoon had promised all the later ones. For now the Commander had the history that had actually happened, and the distance that had actually followed.{/n}''',
    ("ember.started", "ember_gone"), ("ember_dead", "sacrifice", "ascended"))
ending("ending_absent", "The place left unoccupied", '''{n}Ember's absence left the Commander without the ordinary means of asking how she was. A familiar place could remain empty for many reasons. The Commander would not learn which one applied merely by remembering the last time she had sat there.{/n}
{n}The afternoons already shared still mattered. They gave the uncertainty a particular face and voice. They could not supply news that had not arrived, or turn an absence into a death.{/n}
{n}Another conversation would require finding Ember as she actually was, and hearing what she wanted then.{/n}''',
    ("ember.started", "ember.absent"), ("ember_dead", "ember_gone", "sacrifice", "ascended"))
ending("ending_dead", "The questions she would have asked", '''{n}Ember's death left small, unfinished things in the Commander's memory. A question she had asked too plainly to avoid answering. A laugh that began before the funny part of a story. The particular way she could want company without knowing what to do with the afternoon once it arrived.{/n}
{n}The Commander sometimes encountered something she would have wanted to see and felt the old impulse to tell her. For a moment, the invitation seemed as ordinary as it once had. Then the absence returned.{/n}
{n}The time they had actually shared remained part of her life. It did not make her death easier to call by its name.{/n}''',
    ("ember.started", "ember_dead"), ())
ending("ending_sacrifice", "An afternoon she could not ask for", '''{n}The Commander's sacrifice left Ember with questions no next visit could answer. She had known that people died. Knowing had never kept the death of someone she cared about from hurting.{/n}
{n}There were things she wished she had said and ordinary things she wished they had done once more. Other people might describe the victory. Ember could hear them and still want the person who had sat beside her.{/n}
{n}She continued among the people who remained, accepting company when she could and missing the particular company she could no longer ask for. No one afternoon settled the grief.{/n}''',
    ("ember.started", "sacrifice"), ("ember_dead", "ember_gone", "ember.absent", "ascended"))
ending("ending_ascended", "The size of a friend's question", '''{n}Ascension changed the scale on which the Commander's choices could reach the world. It did not make every question between friends simpler. Ember had wanted company, answers she could believe, and the freedom to say what she wished to do with an ordinary day.{/n}
{n}Whatever powers and responsibilities followed, their earlier friendship had taught the Commander something about asking before helping. A person might want a covering returned, a visit ended, or a small story heard without being made into an instruction for everyone else.{/n}
{n}Those wishes did not become unimportant because greater things had become possible. If another conversation could be kept, the Commander would still have to listen to the friend who actually answered.{/n}''',
    ("ember.started", "ascended"), ("ember_dead", "ember_gone", "ember.absent"))
ending("ending_aeon", "An afternoon outside the rewritten world", '''{n}The rewritten world did not preserve the circumstances of Ember's friendship with the Commander simply because the afternoons had mattered. The particular questions, small games, and difficult silences belonged to the lives in which they had happened.{/n}
{n}Ember's life beyond that history was not a place held open for the return of someone she had never known there. Whatever safety or happiness the changed world allowed her would belong to that life.{/n}
{n}An invitation could begin something new if there were people able and willing to make it. It could not demand that she remember an answer from another world.{/n}''',
    ("ember.started",), (), owner="AeonEpilogue")

"""Played settlement consequences and additive migration for Jerribeth's charm route."""
from story_format import c, n, scene

SCENES = []


def s(id, title, nodes, requires=(), forbids=(), delay=24, manual=False):
    for page in nodes:
        if not page["Portrait"]:
            page["Portrait"] = "Jerribeth"
    SCENES.append(scene(
        "jerribeth." + id, title, "Jerribeth", 5, "", nodes,
        Relationship="jerribeth", Remote=True, Chapters=[5],
        Areas=["2570015799edf594daf2f076f2f975d8", "7847c3e3537104f4694167af0b9fcd0e"],
        requires=("jerribeth.commission", "jerribeth.terms", "jerribeth.lovers", *requires),
        forbids=("jerribeth.farewell", *forbids), delay=delay,
        ForbidOverrides={"jerribeth.farewell": "jerribeth.catchup_requested"},
        ManualOnly=manual))


s("settlement_visit", "The visitor who looks underneath", [
    n("start", "Jerribeth", '''{n}Jerribeth is working when she answers. Her image contains a flight of little stairs and a silver basin wide enough to drown the whole model. She moves the basin away from the steps.{/n}
"A precaution. The last time somebody brought work to my table, I eventually broke a chair. This is more expensive."
{n}She moves the frame until it faces the table, then turns it slightly back toward herself.{/n}
"I have invited someone to see it. You may watch if you wish. I shall repeat anything worth hearing. I am beginning to enjoy having a second opinion that the visitor cannot interrupt."''',
      c('"The patron who asked to have your work inspected?"', "inspection", requires=("jerribeth.counter_public_account",)),
      c('"The patron who wanted the impossible staircase?"', "buyer", requires=("jerribeth.counter_private_archive",), forbids=("jerribeth.counter_public_account",)),
      c('[Arrange to return when you can stay for the visit.]', abort=True)),
    n("inspection", "Jerribeth", '''"Her inspector. She prefers to discover whether I am dangerous before spending an evening with me. An order of events you neglected entirely."
{n}She raises the basin. A small window forms above its rim. In it, a figure climbs the stairs while its reflection reaches the upper landing first.{/n}
"This part is mine. Serit made the moving supports for a backdrop. I am testing how much scenery they can carry before someone mistakes a collapsed street for an artistic decision."
{n}The little figure steps out of sight. Its reflection takes another step before disappearing.{/n}
"The basin holds an image briefly while I move the scenery. Otherwise you would see the supports. Do not look pleased. You have not discovered Vardess's room in miniature. It is a little water and a great deal of work."
{n}She sets it down. An adult dwarf with a shaved scalp enters the image carrying a narrow roll of tools. Jerribeth indicates the frame and speaks aloud. The dwarf gives you a brief, professional nod.{/n}
"Hessa. She says she has been paid to examine the construction, and would like me to stop improving it until she has finished."''', c('"Let her begin."', "underneath")),
    n("underneath", "Narrator", '''{n}Hessa starts with the back. Jerribeth follows her hands with such fierce attention that the stair climber loses its head. She restores it without comment.{/n}
{n}The dwarf removes one section of scenery. Behind it, a thin brass arm moves a screen across the basin. She stops the arm. The picture above the water freezes. The figure remains there with its head bent to pass beneath an arch.{/n}
"It will fade," {n}Jerribeth says.{/n} "Unless she intends to hold that all evening."
{n}Hessa points to the image, then to the frame. Jerribeth's hands draw together.{/n}
"She asks whether a guest would know their image was being held. I said that a guest who could see it would notice. She says that was not her question."
{n}The figure in the basin still appears to be trying to get through the door.{/n}
"I offered inspection because I have no hidden recorder in my work. I have not made one. This was meant to hide a join. She wants to mention it in her report."''',
      c('"A stopped image is something her patron should know about. Show it beside the stairs, where nobody has to take your word for it."', "visible", flags=("jerribeth.inspection_visible",)),
      c('"Take the basin out of the paid design. Keep the difficult version for your own experiments."', "removed", flags=("jerribeth.inspection_removed",)),
      c('"Let her report it. You can refuse the commission without denying what she found."', "refused", flags=("jerribeth.inspection_refused",))),
    n("visible", "Jerribeth", '''"Then everyone watches the join instead of the stairs."
"Show me."
{n}She looks as though she might refuse on principle. Then she turns the basin until its bright surface faces the frame. Hessa releases the arm. The tiny figure jerks forward and vanishes.{/n}
{n}Jerribeth begins again. This time there are two climbers. One crosses the model while the other waits in plain sight above the silver rim. When they change places, the substitution is easy to see.{/n}
"A magician obligingly pointing at the sleeve."
{n}Hessa says something. Jerribeth's antennae lift, then draw back.{/n}
"She asks what happens if they refuse to exchange places. I told her that was not the design. She has asked whether it could be."
{n}Jerribeth holds the first figure where it is. The second reaches the landing and turns to stare at its absent partner. For a moment the pair appear to be arguing about who has arrived.{/n}
"That would require another sequence," {n}she says.{/n}
{n}Hessa folds her arms and waits. Jerribeth notices you watching and makes a sharp sound of annoyance.{/n}
"I did not say it was impossible."''', c('"Ask what her patron would pay for that sequence before you make the whole thing."', "inspection_result")),
    n("removed", "Narrator", '''{n}Jerribeth lifts the basin away. Without it, the model shows its moving screens. The tiny climber goes behind one and comes out halfway up the wrong staircase.{/n}
"There. Entirely honest and thoroughly stupid."
{n}She repeats the movement more slowly. The figure notices the wrong landing, looks down, and retreats behind the screen. Hessa makes a small sound. Jerribeth looks at her.{/n}
"She laughed. At the error."
"Can you use it?"
"I can make an entertaining mistake deliberately. I was attempting something else."
{n}She sets the basin well away from Hessa's tools. The little figure tries a third staircase and reaches the place where it began. Its increasingly furious haste makes even the visible screens seem part of the joke.{/n}
"This version will take less time. It will also pay less. I should like that remembered before everybody begins congratulating me."
{n}Hessa points to the supports. Jerribeth answers aloud, then relays the explanation to you.{/n}
"Serit's mechanism remains. The moving picture does not. She may describe exactly that."''', c('"Keep the basin for the work you meant to make."', "inspection_result")),
    n("refused", "Jerribeth", '''"You are remarkably free with someone else's fee."
{n}She keeps her attention on you long enough to make the complaint unpleasant. Then she turns to Hessa and gives a short answer.{/n}
"I have withdrawn the offer. She may report what she saw. I will not turn the whole room into a demonstration of how it fails to deceive people."
{n}Hessa asks a question. Jerribeth points to the dwarf's tools, then makes a dismissive gesture.{/n}
"Her fee is between her and the patron. I invited an inspection. She performed one. I will not pretend she was unwelcome because she looked in an inconvenient place."
{n}Hessa begins replacing the screen. Jerribeth reaches to help and stops when the dwarf holds out a palm. They finish the task separately.{/n}
"I want the room," {n}Jerribeth tells you.{/n} "I should like you to remember that when this becomes an amusing story about my temperament."
{n}The frozen figure fades from the water. The basin is empty before Hessa finishes putting away her tools.{/n}''', c('"I will remember. What do you want to make when she has gone?"', "inspection_result")),
    n("inspection_result", "Jerribeth", '''{n}Hessa writes at the cleared end of the table. Before folding the sheet she points to the frame and asks another question.{/n}
"Whether the Commander approves the construction. She would like to put your name beside her findings."
{n}Jerribeth's voice loses its irritation. She studies you with fresh interest.{/n}
"A useful line. Neither of us has to buy it."''',
      c('"You may say I attended through the charm. I cannot certify what I have only been shown."', "report", flags=("jerribeth.inspection_witness_only",)),
      c('"Leave my name out. This is your work and her examination."', "report", flags=("jerribeth.inspection_unnamed",))),
    n("report", "Narrator", '''{n}Jerribeth repeats your answer aloud. Hessa changes a line and shows her the revision. The two bend over it together, equally unwilling to make room.{/n}
"She has put down what she actually examined," {n}Jerribeth tells you.{/n} "Including the part I would have preferred her not to admire so closely. She will take it to her employer."
{n}Hessa leaves with her report. Jerribeth waits until the door beyond the image closes, then puts one of the little figures on top of the basin.{/n}
"I was tempted to give it her face."
"Were you?"
"I still am. She cannot inspect every petty pleasure I have."
{n}She leaves the figure faceless. Her hand remains over it for a moment before she turns back to you.{/n}
"Stay while I put this away. I have spent quite enough time having people look underneath things tonight."''', c('[Stay while she clears the table.]', "after")),
    n("buyer", "Jerribeth", '''"The very one. Lady Cevra. She has sent specifications, most of them concerning the people who should look foolish."
{n}Jerribeth lifts the basin. An image of two figures forms above it. Both climb a stair, yet the follower arrives first and looks back at the other with elaborate pity.{/n}
"I made this to try the sequence before installing it among Serit's moving screens. The staircase can be absurd without making any particular person ridiculous. She appears to consider that an unnecessary limitation."
{n}An adult woman enters the image in a dark gown sewn with little mirrors. Jerribeth names the frame's audience aloud. The woman adjusts her shoulders and gives you a smile that arrives fully prepared.{/n}
"She says she has heard how diverting my private company is."
{n}Jerribeth waits through another sentence.{/n}
"She has been less well informed about what it costs. I shall correct that."''', c('"Show her the staircase."', "specification")),
    n("specification", "Narrator", '''{n}Cevra watches the figures climb. At the first reversal she laughs. At the second she points to the figure arriving late and begins a long explanation, punctuating it by touching individual mirrors on her sleeve.{/n}
"Her guests," {n}Jerribeth says.{/n} "She would like me to give that figure the face of whichever one is watching. She has had a dispute about precedence. Several disputes."
{n}Jerribeth answers aloud. Cevra stops smiling.{/n}
"I told her the price was for an impossible staircase. She says Vardess included likenesses. And retained them for later entertainments."
{n}Cevra takes a folded invitation from her sleeve. Jerribeth reads it without bringing it close enough for you to see the names.{/n}
"He has announced a new room. We returned what he needed to finish it. I cannot tell from a card whether he has succeeded. She wants the same advantage here, for less money."
{n}The catalogue lies open beside the model. Jerribeth puts a hand on it.{/n}
"We bought the means to approach his clients. There is one. She has not become a different client because I asked her here."''',
      c('"Sell the likeness as a part a guest chooses to play. Give them a way to turn the joke on the hostess."', "player", flags=("jerribeth.catalogue_play",)),
      c('"Sell her a fixed comedy about invented rivals. Charge for the better show, not the same trap."', "comedy", flags=("jerribeth.catalogue_comedy",)),
      c('"Refuse the commission. Keep the names and look for a less tedious use of them."', "decline", flags=("jerribeth.catalogue_declined",))),
    n("player", "Jerribeth", '''"She will be delighted to pay for that suggestion."
{n}Despite the dry answer, Jerribeth gives Cevra the proposal. The woman's reply is immediate. Jerribeth listens, then places a third figure at the top of the stair.{/n}
"She says guests will decline to be mocked. I have suggested that she play first."
{n}Cevra studies the third figure. Jerribeth waits. Finally the woman points to herself, then to the landing.{/n}
"She agrees to show us how it ought to look. Try not to reward the effort before she has made it."
{n}An image of Cevra's mirrored gown forms around the third figure. Jerribeth offers her two small cards and explains them aloud. Cevra chooses one. The little hostess sweeps down the stairs to greet her guests, passes behind a screen and reappears on the landing she has just left.{/n}
{n}The visitors look up at her. She descends again, faster. This time they reach the top before she can greet them.{/n}
"She chose to insist on meeting them personally," {n}Jerribeth tells you.{/n} "The other card lets them find their own way."
{n}Cevra snatches the second card. Her figure sits down. The other two immediately become lost. After a silence, the real Cevra laughs.{/n}
"She wants both endings. And her figure must have a better chair."''', c('"Put both choices into the demonstration her guests see before they agree to play."', "bargain")),
    n("comedy", "Narrator", '''{n}Jerribeth folds the catalogue shut and makes the climbers quarrel. One wears a crown too large for the archway. The other keeps offering to carry it, then placing it on its own head.{/n}
{n}Cevra gestures impatiently. Jerribeth answers without stopping the figures. The crown becomes stuck. Both climbers abandon it and begin racing to the landing, where a second, larger crown waits.{/n}
"She says her guests will miss the point if they cannot recognize each other. I told her she could explain it to them."
"Will they enjoy that?"
"Almost as much as she will enjoy being asked which crown belongs to her."
{n}Cevra speaks sharply. Jerribeth turns to her. Their exchange grows brisk enough that you receive no translation until both figures have reached the top and discovered the larger crown will not fit either of them.{/n}
"She wants the first crown turned into a hat. I have agreed. She wants me to explain privately which figure stands for which guest. I declined. She can invent insults without my assistance."
{n}The little figures exchange their useless prize. Cevra watches them, then puts one finger against the table and begins discussing a price.{/n}''', c('"What does the simpler commission leave you to make for yourself?"', "bargain")),
    n("decline", "Jerribeth", '''"Less tedious may take some finding."
{n}She closes the catalogue. Cevra reaches for it, and Jerribeth puts a delicate hand over hers. The visitor withdraws first.{/n}
"I have declined the work. She would like to know what use I expect to make of a client list if I intend to be so particular about the clients."
"What did you tell her?"
"That a list is useful because it contains more than one name."
{n}Cevra leaves the invitation on the table. Her farewell takes longer than the greeting. Jerribeth answers it aloud with immaculate courtesy and waits until the woman has passed out of the image.{/n}
"She says she will tell Vardess how disappointing I was. He may find that comforting."
{n}Jerribeth moves the card away from the basin. Its corner has become damp.{/n}
"There was money there. Enough for part of a room. I am going to be unpleasant about losing it for a little while. You may remain if you can bear to let me."
{n}She does not ask you to replace the fee. She opens the catalogue and turns to the next name, then stops before you can mistake the movement for an end to the evening.{/n}''', c('"I can stay. Tell me about the room."', "private_cost")),
    n("bargain", "Jerribeth", '''{n}Cevra examines the miniature from each side. Jerribeth turns the basin so she can see the picture above the water stop and fade. They argue over the number of performances and how much of the mechanism Cevra is buying.{/n}
"She has agreed to the demonstration we just gave her," {n}Jerribeth tells you.{/n} "No store of guest likenesses for future use. I will have to remain to work the sequence. She would prefer to own something that could be made to repeat itself indefinitely."
{n}Cevra produces a small purse. Jerribeth does not open it until the visitor has read the revised description beside the model. Then she counts the advance in plain view and writes a receipt.{/n}
"Serit will be pleased. It pays for the next section. The rest buys some time to look at rooms."
{n}Cevra departs with the receipt and leaves Vardess's invitation behind. Jerribeth picks it up by a corner.{/n}
"His room remains his problem to finish. Its guests will have a problem of their own if he succeeds. We did not purchase the right to forget that."''', c('"And you have not promised me that this commission will cure his clients."', "private_cost")),
    n("private_cost", "Jerribeth", '''"The room will have to wait. Tonight I have had enough of selling admission to it."
{n}She folds Vardess's invitation around itself until none of the writing shows. It goes into the catalogue as a marker.{/n}
"I could send you a heroic account of my evening. The cruel patron, the artist who discovered a conscience at exactly the moment an audience would admire it. You would know where I had shortened the bargaining."
"You did let me watch it."
"Yes. I kept wanting to know which part you were looking at. That was distracting."
{n}She turns the basin until it shows only the dark ceiling above her table.{/n}
"The next invitation will be for you. I want to show you where this is going without somebody else asking how much of it can be purchased."''', c('[Stay until she has put the work away.]', "after")),
    n("after", "Narrator", '''{n}She takes the model apart carefully. It is slow work. Once, when a support catches, she holds it still and waits until the urge to pull has passed.{/n}
"Say something," {n}she tells you.{/n} "I have nearly finished being interesting."
{n}You ask how she makes the little climbers turn so sharply. She demonstrates with two fingers, then has to start fitting the support again. The interruption earns an irritated laugh.{/n}
{n}When the last screen is laid flat, she leaves the charm open. The conversation continues without an exhibit between you.{/n}''', c('[Keep the next invitation.]', flags=("jerribeth.settlement_visited",))),
], requires=("jerribeth.counteroffer_kept",), delay=48)


s("room_measure", "A room before its walls", [
    n("start", "Jerribeth", '''{n}The impossible city has acquired a floor. Most of it consists of bare planks laid across open darkness. Jerribeth stands at their edge and regards them with distaste.{/n}
"Measurements. Serit wanted to know how wide the moving backdrop must be. I thought you might enjoy seeing what an ambition looks like when somebody asks where the screws go."
{n}She steps aside. A single finished section of scenery rises behind her, real wood among the chosen images. Its painted arch turns on a brass support.{/n}
"That part is paid for. He made it, brought it, and left. He wants more for a second section. I considered reminding him who first asked for his name to be put on his work. I expect he would have reminded me that it was his name already."''',
      c('"What happened after the inspection?"', "public_result", requires=("jerribeth.counter_public_account",)),
      c('"What did the catalogue buy you in the end?"', "private_result", requires=("jerribeth.counter_private_archive",), forbids=("jerribeth.counter_public_account",)),
      c('[Return when you have time to see her plans.]', abort=True)),
    n("public_result", "Jerribeth", '''"The patron received the report. She asked whether I intended to dispute it. I said that if she wished to employ Hessa and then disregard her findings, she should pay her twice."
{n}Jerribeth lets you enjoy that answer before showing you a fresh sheet of measurements.{/n}''',
      c('"And the visible basin?"', "public_visible", requires=("jerribeth.inspection_visible",)),
      c('"And the version without it?"', "public_removed", requires=("jerribeth.inspection_removed",)),
      c('"Did she accept that you had withdrawn?"', "public_refused", requires=("jerribeth.inspection_refused",))),
    n("public_visible", "Jerribeth", '''"She wants the quarrelling reflections. She also wants the basin in a different metal. Apparently silver belongs to somebody else's drawing room."
{n}Jerribeth shows you the two figures again. This time the one inside the basin sits down and refuses to leave. Its partner grows old waiting on the staircase. The change happens so abruptly that the extravagantly long beard catches on a step.{/n}
"That was my addition. She will have to pay for it. The ordinary exchange remains in the design, and the held image remains where an audience can see it."
"Hessa's question improved the piece."
"Hessa's question made me work. Those are not identical observations."
{n}She removes the beard with a vicious little flick, then restores it a little longer.{/n}
"I kept her name. If I must endure another examination, I prefer somebody who notices the interesting part."''', c('[Ask where the paid section belongs.]', "floor")),
    n("public_removed", "Jerribeth", '''"A smaller fee. The patron accepted the comedy with the visible screens. I have kept the basin."
{n}She shows you the climber trying to escape its endless staircase. At the last landing it stops, takes off its tiny boots, and flings them at the audience. The boots disappear before reaching the edge of the image.{/n}
"She wanted a more gracious conclusion. I gave her one in which it bows while throwing them."
{n}Jerribeth repeats the bow. It makes the insult unmistakable.{/n}
"The fee will cover another section if I make that section narrower. I have not decided whether to do it. I like the wide street. People always begin improving a room by asking you to need less of it."
{n}She leaves the basin out of the paid design. In her imagined city, its reflected window remains large enough to contain a whole second street.{/n}''', c('"Show me the wide street before you decide."', "floor")),
    n("public_refused", "Jerribeth", '''"She sent a reply explaining that she had anticipated a more accommodating artist. I have saved it. Should I ever need to impersonate one, I know what she expects."
{n}The first support stands alone against a great deal of dark, empty space.{/n}
"There is no second advance. Serit will make no second section until I pay for it. A tiresomely symmetrical arrangement."
"Will you offer the piece elsewhere?"
"When it looks the way I want. Someone may dislike it for a more interesting reason."
{n}She moves the finished arch and discovers that it casts a broad shadow across the proposed street. She turns it again, more slowly.{/n}
"I wanted to show you the whole thing tonight. You will have to endure a drawing with one obstinate piece of wood standing in it."''', c('"Then put it where you want it. I came to see your room."', "floor")),
    n("private_result", "Jerribeth", '''{n}She brings the catalogue into view, opens it to the folded invitation and closes it again without showing you a name.{/n}
"A way to reach people who already spend money on illusions. Some of them wish to spend less. Some wish to own the person making them. I am becoming quick at recognizing the second inquiry."
{n}She rests one hand on the real wooden arch.{/n}''',
      c('"Has Cevra kept both choices in the game?"', "private_play", requires=("jerribeth.catalogue_play",)),
      c('"Has Cevra accepted the comedy?"', "private_comedy", requires=("jerribeth.catalogue_comedy",)),
      c('"Have you found someone after refusing Cevra?"', "private_declined", requires=("jerribeth.catalogue_declined",))),
    n("private_play", "Jerribeth", '''"She tried to buy a third card. One that let the hostess win whichever choice her guest made. I offered to sell her a crown instead."
{n}Jerribeth shows you two little cards, then turns them over. The same symbols appear on both sides.{/n}
"These are easier to distinguish across a room. I will explain them before anybody takes a part. She has accepted the design. Whether she finds a way to be unbearable about it is beyond my contract."
{n}Her antennae incline toward you.{/n}
"She also asked whether you would appear for the opening. I said she had purchased stairs. Should she wish to invite a Commander, she would have to discover how to do that herself."
"Thank you."
"I enjoyed disappointing her. You need not deprive me of the less admirable reason."''', c('[Ask where the next section will go.]', "floor")),
    n("private_comedy", "Jerribeth", '''"She wanted one of the rivals made unmistakably smaller than the other. I asked whether she meant in stature or importance. It took her three letters to answer."
{n}Two figures appear. The small one lifts the large hat over its entire body and walks away unseen. The taller one bows to the empty staircase.{/n}
"She accepted that. I have charged for the letters as revisions. Her guests will probably find themselves in it whether I put them there or not. At least I have made something worth looking at while they argue."
{n}She makes the hat walk back and bow. Beneath it, the little figure sticks out its tongue.{/n}
"There. I have been entertaining people who annoy me. I am in danger of becoming respectable. You will have to look offended on my behalf."''', c('"I might have to laugh first."', "floor")),
    n("private_declined", "Jerribeth", '''"Someone has asked for a price. That is not yet someone paying it."
{n}She sets the catalogue down with more care than it deserves.{/n}
"I thought knowing what they had paid Vardess would make this easier. It tells me how much they possess, not how much they will surrender to me. They have enjoyed explaining the difference."
"Would you take Cevra's work now?"
"I might take a different offer. I do not have to become poor to prove that I meant my refusal."
{n}She moves the completed arch with both hands. It is heavier than the image suggested.{/n}
"For tonight, this is the room I can afford. Do not tell me how much more important my company is. I know you did not come to admire an invoice. I would still like another wall."''', c('"Show me where you would put it."', "floor")),
    n("floor", "Narrator", '''{n}Jerribeth moves the real arch while the city changes around it. A street curls upward, trying to meet the arch's far side. She widens the street. The room beyond the image has no corresponding space, so the final stretch remains a drawing in the air.{/n}
"It will need a room of its own. I have looked at descriptions. I have not bought one."
{n}The street has two possible ends. At one, a terrace overlooks the impossible city. At the other, a door opens onto the place where the walk began.{/n}
"This is the part I cannot decide. The visitor can discover that they have travelled nowhere, or discover somewhere worth staying. I am inclined to promise the second and give them the first."
{n}She watches your expression.{/n}
"You may disagree without commissioning an inspection."''',
      c('"Let them return to the beginning and notice what changed while they were walking."', "loop", flags=("jerribeth.room_loop",)),
      c('"Give them the terrace. Make them want to turn back and try a different street afterward."', "terrace", flags=("jerribeth.room_terrace",))),
    n("loop", "Narrator", '''{n}She sends the small figure through the arch. The street bends out of sight. When it returns, its own footprints are already waiting on the planks.{/n}
"Too obvious."
{n}The footprints vanish. A window opens over the doorway instead. Someone inside has set out a lamp. The climber stops beneath it.{/n}
"Who lives there?" {n}you ask.{/n}
"Someone who has seen it pass before."
"Will they open the door?"
{n}Jerribeth considers that. The window closes, but the light remains behind it. The little figure sits on the step and takes off its boots.{/n}
"Perhaps they will argue about whose doorstep it is. I can make a longer version."
{n}She writes something down outside the image. When she returns, the lamp has grown brighter.{/n}
"Do not grow impatient and give it a happy ending while I am occupied. I should like to discover what it wants first."''', c('"I will leave it on the step. Come back here."', "private")),
    n("terrace", "Narrator", '''{n}The little figure reaches the terrace. Below it, streets exchange places like impatient people trying to see past one another. It watches until one rises toward a narrow door, then runs to find the way down.{/n}
"Greedy," {n}Jerribeth says with approval.{/n}
{n}She sends the figure back. It takes the wrong turning and emerges at the arch. This time it begins again without being prompted.{/n}
"I would need more streets."
"You could begin with these."
"You sound like Serit. He has an excellent grasp of what I cannot afford."
{n}She watches the climber disappear down a new passage, makes the passage a little longer and records something outside the frame.{/n}
"That one will remain unfinished for a while. Someone may enjoy standing at its end and making suggestions I did not solicit."
"Would you?"
"I have been enduring it all evening."''', c('"Then let me make one more. Leave the streets and stay with me."', "private")),
    n("private", "Jerribeth", '''{n}She leaves the unfinished room visible, but brings her own form nearer the frame. The delicate hands that moved the heavy arch rest together. A fine tremor passes through one antenna and stops.{/n}
"I wanted a place where I could choose who entered. That was the whole ambition at first. A door, and the pleasure of leaving someone outside it."
{n}She glances back at the model.{/n}
"Now I keep making another street because I think you will ask what is around its corner. I have allowed your questions to become expensive."
"I like the unfinished one."
"I noticed. You would."
{n}Her voice softens without losing its high, vibrating edge.{/n}
"There is still no door from that room to yours. I cannot turn a drawing into a passage by wanting you on the other side. Tonight I can offer you what I have."''',
      c('"Describe where you would stand if I were there. I want to imagine coming to you."', "desire", flags=("jerribeth.room_desire",)),
      c('"Stay close to the frame. I want your company here while the city keeps moving."', "quiet", flags=("jerribeth.room_quiet",))),
    n("desire", "Jerribeth", '''"Here. Close enough that you would have to decide whether to stop admiring the scenery."
{n}She gives you time to picture it. The imagined lamplight follows the edge of a wing. You tell her how you would approach, and she corrects one detail with a low, pleased sound.{/n}
"Slower. I have spent a long time waiting to discover whether you meant to come nearer. I would like to enjoy being certain."
{n}Your hands remain on your side of the charm. Hers rest within the chosen image. What passes between you is a description, then an answer she has waited to hear, then her voice asking you to say it again.{/n}
{n}When the conversation grows quiet, she leaves the image close. The city behind her has lost most of its lights. Neither of you asks her to restore them.{/n}''', c('[Keep the quiet evening together.]', "end")),
    n("quiet", "Jerribeth", '''"You have watched enough work for one evening?"
"I have watched you keep finding one more thing to change."
"An objectionable habit. I have cultivated it carefully."
{n}She moves the image nearer. You can still see the unfinished street. She dims its far end until you can no longer follow the little figure.{/n}
{n}Jerribeth adds a lamp beside the nearest arch and asks where you would put it. You tell her. She moves it, dislikes the effect and moves it back. Then she laughs at herself before you can answer.{/n}
"Leave it there. Tell me something I cannot improve."
{n}The conversation leaves the room and its measurements. Her voice stays with you as the image darkens. When she decides you have grown tired, she tells you so, and is right, and is insufferable about it.{/n}''', c('[Stay a little longer.]', "end")),
    n("end", "Jerribeth", '''"I will keep working on it."
{n}She means the room. She leaves the rest for you to answer another evening.{/n}
"Come back when you can. I should like to hear what you intend to do after you have finished being inconvenient to the world."''', c('[Keep her invitation to speak about what comes next.]', flags=("jerribeth.settlement_kept",))),
], requires=("jerribeth.settlement_visited",), delay=48)


s("short_invitation", "An evening before the promises", [
    n("start", "Jerribeth", '''"You have been turning the frame toward you as though there is something you mean to ask."
{n}She leaves her work where it is.{/n}
"If it concerns how little time you have, I have already counted it. Make your offer. I dislike learning that somebody has vanished from my books by reading it in theirs."''',
      c('"I want to keep seeing you after the war, even if we cannot make time for the longer visits before it ends."', "short"),
      c('"I want to make that time. Let us return to what you wanted to show me."', abort=True)),
    n("short", "Jerribeth", '''"Then ask me for that, properly, and I shall name what it costs. We have had evenings I want repeated. I have not yet had the ones I want most."
{n}Her hands unlink.{/n}
"The work will keep. If you come back to it before you leave, so much the better for you. If you do not, I shall remember, and charge the difference later."''', c('[Arrange a conversation about continuing the shorter courtship.]', flags=("jerribeth.short_future_requested",))),
], forbids=("jerribeth.future", "jerribeth.settlement_kept"), delay=0, manual=True)

s("promise_revisited", "The promise with days inside it", [
    n("start", "Jerribeth", '''"You promised to keep answering. You have answered through several evenings that would have been easier to miss."
{n}She brings the unfinished city into the frame. The visible street ends well before the edge of the image.{/n}
"So I am raising the price. There is something here now besides my talent for making an invitation attractive, and a thing that exists is worth more than a thing promised. The work has not made me easy company. I do not intend to improve."''',
      c('"I want to keep choosing this. Your work, our evenings, and the arguments we will still have."', "chosen"),
      c('"I mean the promise I made. I am not ready to promise more tonight."', "held"),
      c('"I no longer want this relationship."', "close"),
      c('[Find another evening for this conversation.]', abort=True)),
    n("chosen", "Jerribeth", '''"I want you to see the room when it exists. If it takes longer than I expect, you may hear me complain while I find another fee."
{n}Her antennae lift toward the frame.{/n}
"Bring me your complaints too. I am excellent at finding out whom to blame, and very reasonable about what it costs to ruin them."
"I only want you to hear them."
"You will get both. I do not do half-measures. Rather inconveniently, I want more of this than I have paid for."''', c('[Renew the promise with the life you have begun to share.]', flags=("jerribeth.developed_future", "jerribeth.future_settled"))),
    n("held", "Jerribeth", '''"Then I shall keep the promise I actually heard."
{n}She looks back at the unfinished street and leaves it unfinished.{/n}
"You may still come and argue about the next corner. I have not sold the right to complain about your suggestions."''', c('[Keep the existing promise without enlarging it.]', flags=("jerribeth.future_settled", "jerribeth.promise_held"))),
    n("close", "Jerribeth", '''{n}For a moment the city remains behind her, much brighter than her face.{/n}
"I had hoped to show you more."
{n}She removes the image herself.{/n}
"I heard you. I will stop waiting for an invitation."''', c('[End the relationship.]', flags=("jerribeth.closed",))),
], requires=("jerribeth.future", "jerribeth.committed", "jerribeth.settlement_kept"), forbids=("jerribeth.developed_future",))

s("old_promise", "What the earlier promise meant", [
    n("start", "Jerribeth", '''"We made a promise. I have no intention of pretending it did not happen because there are evenings we have not found time for."
{n}She watches you across the charm.{/n}
"If you are leaving soon, say so now. I keep a place open for a debtor. I do not keep it open for a rumour."''',
      c('"Keep the promise as we made it. I cannot offer the longer visits before I leave."', "keep"),
      c('"I want to make those visits before we say our farewells."', abort=True)),
    n("keep", "Jerribeth", '''"Then I will expect your answer when you can give it. If you mistake my patience for forgetting, I shall show you what I remember, all at once, at a moment of my choosing."
{n}Her voice brightens slightly.{/n}
"Come back and I shall not have to. I would enjoy either."''', c('[Keep the earlier promise and arrange a farewell before the unfinished visits.]', flags=("jerribeth.future_settled", "jerribeth.short_future_chosen", "jerribeth.short_farewell_requested"))),
], requires=("jerribeth.future", "jerribeth.committed"), forbids=("jerribeth.future_settled", "jerribeth.settlement_kept"), delay=0, manual=True)

s("farewell_review", "Before the unfinished evenings", [
    n("start", "Jerribeth", '''"Are you leaving soon?"
{n}She puts down the work she was about to show you.{/n}
"We can say our farewells if you must. I do not waste good work on an audience that has already left."
{n}She looks back at the table.{/n}
"Or you can stay for what comes next. I made it to see your face when you understand it. Do not cheat me of that."''',
      c('"I need to say farewell before we finish those evenings. Keep our promise as it stands."', "leave"),
      c('"There is still time. Show me what you have been preparing."', abort=True)),
    n("leave", "Jerribeth", '''"Then give me one more evening before you go. I shall try to think of something you have not already heard."
{n}Her hands meet over the unfinished work.{/n}
"If you find there is more time after all, come back to this. A farewell is not a contract. I have broken better ones."''',
      c('[Arrange the farewell, leaving the remaining work for an invitation you can explicitly renew.]', flags=("jerribeth.short_farewell_requested",))),
], requires=("jerribeth.ordinary", "jerribeth.committed", "jerribeth.future_settled"),
   forbids=("jerribeth.developed_future", "jerribeth.short_farewell_requested", "jerribeth.catchup_requested"), delay=0, manual=True)

# This invitation must remain manually selected, so declining it cannot occupy the rest queue.
SCENES.append(scene("jerribeth.another_evening", "An invitation after farewell", "Jerribeth", 5, "", [
    n("start", "Jerribeth", '''"You said there might be no more convenient evenings. I see you have found an inconvenient one."
{n}She draws her hands apart as the image steadies.{/n}
"Did you want to return to the work we left, or only to make certain I would answer?"''',
      c('"I want to return to it. There is time for more than the farewell we already said."', flags=("jerribeth.catchup_requested",)),
      c('"Only to hear you. Keep the farewell as it stands for now."', abort=True), portrait="Jerribeth"),
], Relationship="jerribeth", Remote=True, Chapters=[5], ManualOnly=True,
    Areas=["2570015799edf594daf2f076f2f975d8", "7847c3e3537104f4694167af0b9fcd0e"],
    requires=("jerribeth.farewell", "jerribeth.committed"), forbids=("jerribeth.catchup_requested",)))

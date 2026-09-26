"""Authored Chapter 3 friendship afternoons; no native quest or romance mutations."""
from story_format import c, n, scene

SCENES = []


def s(id, title, nodes, requires, delay=24):
    for node in nodes:
        node["Portrait"] = "Ember" if node["Speaker"] == "Ember" else ""
    SCENES.append(scene("ember." + id, title, "Ember", 3, "", nodes,
                        Relationship="ember", Remote=True, Chapters=[3], last=3,
                        Areas=["2570015799edf594daf2f076f2f975d8"],
                        requires=("ember.present",) + requires,
                        forbids=("ember.closed", "ember_dead", "ember_gone", "ember.absent"),
                        delay=delay))


s("paper_bird", "A bird with a speaking part", [
    n("start", "Narrator", '''{n}A woman sorting laundry in a narrow Drezen courtyard has put a shallow basket beside her work. It contains scraps of cloth, short lengths of thread, and several bent wooden pegs. Ember is choosing among them with considerable care.{/n}
{n}"Those are the ones you may have," the woman tells her. "The basket by my elbow is mending. Anything in there still belongs to somebody, however hopeless it looks."
Ember moves her hand away from a spectacularly torn sleeve.{/n}
"Even that?"
"Especially that. Its owner keeps telling me how much he likes it."
{n}Ember notices you.{/n}''',
      c('"What are you making?"', "project"),
      c('"I see you have found a more difficult bird than Soot."', "project"),
      c('[Return when you can stay for the afternoon.]', abort=True)),
    n("project", "Ember", '''"Our bird. Only this time he can move."
{n}She shows you a flat wooden offcut with a paper beak attached. Loose pieces of cloth dangle below it.{/n}
"Pella gave me the broken pegs. I thought they could be legs, but they were too heavy. He kept falling on his face."
"You kept putting him down beak first," says the woman.
"That too."
{n}Ember holds the bird sideways. Its beak opens when she pulls a thread.{/n}
"I wanted to make him say something. But now that he can, I don't know what he ought to say first."''',
      c('"Something about the terrible burden of command."', "general", requires=("ember.manyboots",)),
      c('"A complaint about the weather."', "inspector", requires=("ember.rain_inspector",))),
    n("general", "Ember", '''{n}She makes the beak open and shut twice.{/n}
"I have inspected all the boots, and none of them contain breakfast."
{n}Pella laughs into a piece of folded linen.{/n}
"That is a burden, certainly."
"He can go looking for it," Ember says. "Only somebody will have to tell him where to go. If I make him walk and talk and meet everybody myself, I will run out of hands."''', c('"You want another performer."', "invite")),
    n("inspector", "Ember", '''{n}She lifts the bird until its beak faces the cloudless sky.{/n}
"The rain is very late. I shall have to inspect something else."
"My washing is grateful," says Pella.
"He could inspect breakfast. But somebody will have to tell him where it is. If I make him walk and talk and meet everybody myself, I will run out of hands."''', c('"You want another performer."', "invite")),
    n("invite", "Ember", '''"Would you like to?"
{n}She lays the bird across the top of the scrap basket.{/n}
"Pella says we can use her courtyard when the washing has gone in. Just for a little while. She wants to see whether he can walk without losing anything."
"I want to sit down without someone handing me another shirt," Pella says. "A bird is a welcome change."
{n}Ember brings out a second wooden shape. This one has a long nose and a tail made from an old ribbon.{/n}
"This is a fox. I thought he might know where breakfast was. Foxes usually do."''',
      c('"I will be the fox. I reserve the right to give terrible directions."', "fox", flags=("ember.player_fox",)),
      c('"I would rather tell the story. You can give them their voices."', "narrator", flags=("ember.player_narrates",))),
    n("fox", "Ember", '''"Then I must make him get lost somewhere interesting."
{n}She holds the fox out by its flat handle. Its ribbon tail has a knot in the middle.{/n}
"Don't undo that. It keeps slipping off. I think he must have caught it in a gate."
"Or a laundry basket," Pella says.
"He won't admit it."
{n}You try a solemn greeting. Ember's bird answers by opening its beak so far that the thread catches. She has to free it before either creature can speak again.{/n}
"We should practice. He might get stuck halfway through a secret."''', c('[Agree to rehearse before inviting anyone.]', "cloth")),
    n("narrator", "Ember", '''"Then you can tell me when they have been talking for too long."
{n}She gives the fox a deep, solemn voice, then answers it with the bird. The second voice is almost exactly the same. Pella raises an eyebrow.{/n}
"They're related," Ember says quickly.
"A fox and a bird?"
"They don't like to talk about it."
{n}She laughs at her own explanation and tries again. This time the fox speaks so slowly that the bird interrupts before he reaches the end of his greeting.{/n}
"We should practice. You might have to tell me which one I am."''', c('[Agree to rehearse before inviting anyone.]', "cloth")),
    n("cloth", "Narrator", '''{n}Pella takes a clean, patched blue cloth from a shelf and spreads it over a low worktable. The patches look like islands.{/n}
"You can stand the figures here. My own cloth, not a customer's. Bring it back to the shelf when you've finished."
{n}She smooths one corner.{/n}
"If my brother needs it for his delivery cart, his work comes first. He's lent me that cart often enough."
"We can still have the bird," Ember says. "He belongs to us."
"Yes. And the courtyard is yours for one afternoon after we agree the day. No preaching to draw a crowd, and no blocking the door."
"I wanted to do the fox," Ember says, sounding faintly affronted.
{n}Pella lifts both hands in surrender. Ember arranges a scrap of yellow cloth beside the bird, then removes it and folds it into a small parcel.{/n}''', c('"What is that?"', "boots")),
    n("boots", "Ember", '''"His boots. All of them. He takes them off to eat breakfast, and the fox carries them away."
"Why?"
"I haven't decided. Perhaps he has cold feet."
{n}She sets the little parcel beside the fox.{/n}
"I want the bird to get them back. But I don't want the fox to be chased away forever. We shall have to think of something."
{n}Pella returns to the torn sleeve. Ember gathers the puppets, leaving the borrowed cloth folded on its shelf.{/n}
"I will keep these safe. Next time, you can tell me if the story makes sense."''', c('[Arrange another afternoon to rehearse.]', flags=("ember.puppet_project",))),
], requires=("ember.shared_afternoon",))

s("missing_cloth", "The sea has gone to work", [
    n("start", "Narrator", '''{n}The shelf is empty. Ember looks underneath it, then at the table, although a blue cloth large enough to cover the table could hardly have hidden beneath a spool of thread.{/n}
"He needed it," Pella says. "I told you his cart came first. A crate had broken, and he needed something to keep the little parcels together."
{n}Ember nods. She puts the bird on the bare wood.{/n}
"I remember."
"He'll bring it back when he's done. I don't know when that will be."
{n}Pella steps into the house with an armful of shirts. The bird tips over. Without the cloth beneath its handle, it slides whenever Ember tries to make it walk.{/n}
"I had made the islands go all the way to the bowl of breakfast. Now he can't get there."''',
      c('"We could find another piece of cloth."', "another"),
      c('"I think you are disappointed."', "disappointed"),
      c('[Return when you have time to rehearse.]', abort=True)),
    n("another", "Ember", '''"Pella might have another. But she might need that one too."
{n}She picks up the bird and examines its wooden handle.{/n}
"I don't want her to have to give us everything because I look sad. I am sad about it. A little."
{n}Her thumb follows a splinter in the wood.{/n}
"I thought knowing she might need it would mean I wouldn't mind when she did. It hasn't worked very well."''', c('"We can mind and still let her use her own cloth."', "choices")),
    n("disappointed", "Ember", '''"I liked the sea. I liked knowing where all the islands were."
{n}She points to an empty place on the tabletop.{/n}
"There was a yellow patch here. The fox was going to say it was cheese. He was lying, but perhaps the bird could have a little rest on it."
{n}Ember rests the bird in her lap.{/n}
"Pella didn't do anything wrong. I don't know why that doesn't make me feel better."''', c('"You can be disappointed without anybody having to be wrong."', "choices")),
    n("choices", "Ember", '''"Then I am."
{n}She says it firmly, as though someone has questioned her right to the feeling. Then she looks at the long grain of the wood.{/n}
"We could make these into roads. Only there aren't any places to stop."
{n}Pella returns for the empty basket and hears the end of this.{/n}
"No chalk on my table. It gets in the grain. You may put something on it that comes off again. Or wait for the cloth."
"Could we have the courtyard another afternoon?"
"Yes. I'll tell the two people I invited. Don't promise a day until we've got one."''',
      c('"Let us make a road with loose scraps. The bird can travel overland."', "road", flags=("ember.stage_road",)),
      c('"Let us wait for the cloth. We can practice the voices today."', "wait", flags=("ember.stage_waited",))),
    n("road", "Narrator", '''{n}You and Ember choose three broad scraps from the permitted basket. Pella gives you a small board to put under them so their ragged edges will not snag on the table. With the handles held just above the cloth, both figures can cross it.{/n}
"That one is an inn," Ember says, indicating a brown square.
"A very small inn."
"It only has one room. The fox has promised it to everybody."
{n}She stops. The fox looks behind itself.{/n}
"That might be why he needs to leave in a hurry."
{n}The bird attempts to enter the inn and catches its beak on the edge of the board. Ember frees it without dislodging the road.{/n}
"We can keep the afternoon we chose. Pella won't have to go and tell people we've stopped."''', c('[Help fasten a rest for the bird behind the board.]', "role")),
    n("wait", "Narrator", '''{n}Pella takes a shawl down from its peg. She is going to see one of her guests before the evening meal anyway, but the other lives in the opposite direction.{/n}
"I'll do that door tomorrow," she says. "There won't be anybody waiting here for a performance that isn't happening."
{n}Ember watches her go.{/n}
"Waiting makes work too. I hadn't thought about that."
{n}You practice at the bare table. The puppets stay in their operators' hands, well above the wood. The fox is given a sneeze that interrupts its most important lies. By the fourth attempt, you both manage to keep the figures upright through it.{/n}
"When the sea comes back, he will be ready for it."''', c('[Practice the scene in which the bird asks for its boots.]', "role")),
    n("role", "Narrator", '''{n}The rehearsal reaches the theft. The fox's ribbon tail lies across the little yellow bundle. Ember pauses before the bird discovers that its boots are gone.{/n}''',
      c('[As the fox, try to conceal the bundle behind its nose.]', "fox", requires=("ember.player_fox",)),
      c('[Describe how the fox hides the bundle while Ember moves the figures.]', "narrator", requires=("ember.player_narrates",))),
    n("fox", "Ember", '''"Your nose is much too small. I can see the boots."
{n}The bird peers around the fox. You move the fox again, keeping it between bird and bundle, until the two figures are circling the same patch of table.{/n}
"He must get tired of doing that eventually."
{n}You make the fox sit on the boots. Ember laughs, then tries to make the bird laugh too. Its beak sticks open.{/n}
"Oh, he really liked that."''', c('[Untangle the thread.]', "ending")),
    n("narrator", "Ember", '''{n}At your description, Ember conceals the bundle beneath the fox's tail. Then the bird demands that the fox turn around. She tries to lift the tail and keep the boots hidden with the same hand.{/n}
"I know where he put them. It ought to be easier."
{n}You give the bird a sudden interest in the sky. While it looks away, Ember gets the bundle clear of the ribbon.{/n}
"Thank you. I think he was looking at a cloud shaped like breakfast."''', c('[Bring the bird back to its missing boots.]', "ending")),
    n("ending", "Ember", '''"I thought the fox could give them back, and then they could share the breakfast. But the bird hasn't got any breakfast yet. And the fox still wanted something to keep his feet warm."
{n}She unties the yellow bundle and looks at the scrap inside.{/n}
"Perhaps there could be another parcel. Or perhaps he could ask before he takes this one. Only then there wouldn't be a story."
{n}She puts the bundle back together.{/n}
"I want him to have done it. I want him to be able to do something else afterward."''',
      c('"He could return them, then help the bird find breakfast. Let the bird decide about sharing."', "returned", flags=("ember.play_restitution",)),
      c('"Let him explain why he took them. They can make another pair together after breakfast."', "explained", flags=("ember.play_explanation",))),
    n("returned", "Ember", '''"The bird can be cross for a while. He had to walk without his boots."
{n}She moves the bird a few stiff steps, then catches herself.{/n}
"Only he was flying. We must give him something to carry. Something too heavy to fly with."
{n}The yellow bundle becomes luggage until the boots are needed. Ember puts a loose thread beside it to remind herself of the extra job.{/n}
"The fox can carry that. And the bird can stop being cross when he wants to."''', c('[Keep that ending for the performance.]', flags=("ember.puppet_rehearsed",))),
    n("explained", "Ember", '''"Then the fox must ask. He can't just say he needs them and keep sitting on them."
{n}The fox steps off the bundle.{/n}
"Please may I have some boots? Mine have holes in."
{n}The bird considers. Then it picks up the bundle and takes it with him toward an imaginary breakfast.{/n}
"First give mine back. Then I'll see what I can do."
{n}Ember lowers the bird, still watching the fox.{/n}
"That sounds better. He is going to help, but he wants his own feet warm too."''', c('[Keep that ending for the performance.]', flags=("ember.puppet_rehearsed",))),
], requires=("ember.puppet_project",))

s("courtyard_play", "Breakfast for a troublesome bird", [
    n("start", "Narrator", '''{n}Pella has cleared the courtyard. Three stools face the low table, with enough room beside them for anyone who would rather stand. A woman carrying an empty market basket has taken the stool nearest the door. Pella introduces her as Ilva, then sits beside her.{/n}
{n}Ember peers over the table. Ilva wants to know whether she will be able to hear from the back.{/n}
"There isn't a back," Ember says. "But you can tell us if we're too quiet."''',
      c('[Help set out the road.]', "road", requires=("ember.stage_road",)),
      c('[Help unfold the returned sea.]', "sea", requires=("ember.stage_waited",)),
      c('[Ask for a little time before taking your place.]', abort=True)),
    n("road", "Narrator", '''{n}The little road occupies the middle of the table. The blue cloth has come back, but Ember leaves it on its shelf.{/n}
"We know where everything goes now."
{n}Pella's brother has apologized for the small tear near a corner of the cloth. Pella says she will mend it when she has finished the work she is paid for. She examines the road instead and approves the unmarked tabletop beneath it.{/n}
"I told them you had a traveling show. I seem to have been right."
{n}Ember makes the bird take an experimental step behind the board.{/n}
"He has a very long way to go for breakfast."''', c('[Take your place.]', "role")),
    n("sea", "Narrator", '''{n}The cloth has come back with a small tear near one corner. Pella's brother has apologized, and Pella has folded that edge underneath so it cannot catch on the bird's handle.{/n}
"Nessa couldn't come on the first afternoon," she tells you. "So the new day worked out for somebody."
{n}Nessa arrives with a cup with a chipped rim. She sets it well away from the performers and takes the last stool.{/n}
"I was told there would be a sea. Is that it?"
"It has had a busy week," Ember says.
"So have I. I'll try not to spill anything into it."
{n}Ember smooths the yellow island. It is a little farther from the edge than she remembers.{/n}
"The sea has got smaller. We can move breakfast."
{n}You put the empty wooden bowl near the far end. The bird will have to cross two islands to reach it, but its handle no longer catches on a loose thread.{/n}''', c('[Take your place.]', "role")),
    n("role", "Narrator", '''{n}Pella sits down. The fox waits behind the table with the little parcel of boots. Ember checks the thread inside the bird's beak one last time.{/n}''',
      c('[Make the fox greet its audience with extravagant dignity.]', "fox", requires=("ember.player_fox",)),
      c('[Begin the story while Ember raises the bird.]', "narrator", requires=("ember.player_narrates",))),
    n("fox", "Narrator", '''{n}You introduce the fox as a creature who knows absolutely everything, provided nobody asks for particulars. Ilva settles back on her stool.{/n}
"I know a man like that."
{n}Ember nearly answers her in her own voice. She catches herself and makes the bird interrupt the fox's account of its splendid travels.{/n}
"But do you know where breakfast is?"
{n}The fox points in two directions at once. Pella laughs, and Ember gives you a quick, pleased glance before steering the bird toward the wrong end of the table.{/n}''', c('[Continue to the missing boots.]', "theft")),
    n("narrator", "Narrator", '''{n}You announce that the bird has left home without breakfast and has found a creature very willing to offer advice. Ember gives the fox its slow, solemn voice. The bird interrupts it before it has said where it is going.{/n}
"Is there food there?"
"There is an excellent view."
"Can I eat it?"
{n}Pella laughs. The fox sneezes so violently that its tail slips off the edge of the table. Ember retrieves it while you explain that this is a customary fox greeting, seldom understood by outsiders.{/n}
"Ah," Pella says. "That explains a good deal."''', c('[Continue to the missing boots.]', "theft")),
    n("theft", "Narrator", '''{n}The bird puts down its boots to count them. The fox offers to help, then hides the little bundle beneath its tail. When the bird turns back, the parcel has vanished.{/n}
"You were standing here," says the bird.
"I stand in many places," says the fox.
"But this was one of them."
{n}The fox begins to back away. Its tail drags the parcel into sight.{/n}
"That wasn't very clever," Ilva says.
{n}Ember gives the bird a long look at the exposed boots. This time she remembers to close its beak before speaking.{/n}''',
      c('[Give the fox the work of making amends.]', "restitution", requires=("ember.play_restitution",)),
      c('[Let the fox ask for help with its own cold feet.]', "explanation", requires=("ember.play_explanation",))),
    n("restitution", "Narrator", '''{n}The fox returns the boots and offers to carry the bird's luggage. The bird accepts the help, but makes the fox walk where it can see the bundle. Together they arrive at the empty bowl.{/n}
"There isn't any breakfast," says the bird.
{n}The fox searches beneath the bowl. The yellow scrap, now unpacked, becomes a pancake. It is folded into two unequal pieces. The bird studies both before offering the larger one to the fox.{/n}
"You did carry everything."
{n}Pella applauds. Ilva claps too, then says she hopes the fox doesn't take the boots again tomorrow.{/n}
"He might think it was worth it, for half a pancake."
{n}Ember keeps hold of the bird. Pella looks toward her, waiting for the performance to finish.{/n}''', c('[Let Ember answer.]', "answer")),
    n("explanation", "Narrator", '''{n}The fox returns the bundle. Then it shows the bird the holes in its own imaginary boots, pointing with its ribbon tail since it has no other convenient limb.{/n}
"I thought you had so many that you wouldn't miss a few."
"I have so many feet."
{n}The bird considers, then leads the fox to breakfast. A scrap becomes a pancake, shared between them. Afterward they roll the remaining yellow cloth into a new pair of boots for the fox.{/n}
"Ask first next time," says the bird.
{n}Pella applauds. Ilva claps more slowly.{/n}
"And if he says he's cold again? Does the bird have to keep making him things?"
{n}Ember looks at the tiny boots. Pella waits instead of answering for her.{/n}''', c('[Let Ember answer.]', "answer")),
    n("answer", "Ember", '''"I don't know what he does tomorrow. We haven't made tomorrow yet."
{n}She lowers the bird a little.{/n}
"I wanted him to be able to come back."
"I liked him," Pella says. "I don't want him driven out."
"Neither do I," Ilva says. "I'd put my boots somewhere else, though."
{n}Ember puts the bird down. The wooden handle makes a little clack against the table.{/n}
"It is finished for today. Thank you for coming."
{n}The audience thanks her. Ilva asks whether there will be another. Ember says she would like to think about it. Pella gets up to move the stools, giving you a moment beside the table.{/n}''',
      c('"I liked doing it with you. We can talk about the ending when you want."', "together", flags=("ember.play_company",)),
      c('"The ending left them with different answers. Would you like to hear mine later?"', "opinion", flags=("ember.play_opinion",))),
    n("together", "Ember", '''"I liked it too."
{n}She picks up the fox and looks at the knot in its tail.{/n}
"I liked the part before they asked what happened next. But they were listening. I wanted them to listen."
{n}Her expression brightens a little.{/n}
"Pella sat down the whole time. She didn't mend anything. I think that part worked."''', c('[Help put the courtyard back in order.]', flags=("ember.puppet_performed",))),
    n("opinion", "Ember", '''"Yes. Later, though. I still have everybody else's in my head."
{n}She separates the little boots from the pancake and puts them beside the figures.{/n}
"Tell me the parts you liked too. I might want to keep them."
{n}Pella calls for someone to hold the door while she carries the stools inside. Ember gathers the puppets before they can be buried beneath the returned washing.{/n}''', c('[Help put the courtyard back in order.]', flags=("ember.puppet_performed",))),
], requires=("ember.puppet_rehearsed",), delay=48)

s("after_applause", "The morning after the fox", [
    n("start", "Narrator", '''{n}Ember is sitting near Pella's doorway with the puppet handles laid across her knees. Pella is inside, arguing with a customer about a missing button. The customer believes that five buttons became four in the wash. Pella remembers sewing the fourth one on last week.{/n}
"I don't think the fox took it," Ember says quietly.
{n}She turns one of the handles over.{/n}
"Ilva came by. She brought us a piece of ribbon for the next one. She said she liked the play. Then she said the same thing about the boots."
{n}The new ribbon is green and much too long for a tail.{/n}
"I thought she'd forgotten the other parts. But she remembered the sneezing, and the pancake. She liked those too."''',
      c('[Return to the question you offered to discuss.]', "opinion", requires=("ember.play_opinion",)),
      c('"Would you like to talk about the ending now?"', "company", requires=("ember.play_company",)),
      c('[Arrange to talk when you can give her your attention.]', abort=True)),
    n("opinion", "Ember", '''"You said you'd tell me what you thought. I think I can listen now."
{n}She folds the green ribbon over her finger.{/n}
"I kept thinking that if she didn't like the ending, she hadn't understood it. But she knew the fox was cold. She told me that."
{n}Ember studies the fox.{/n}
"Perhaps she understood, and still didn't like it."''', c('"That happens. I can tell you what I saw."', "discuss")),
    n("company", "Ember", '''"Yes. I didn't want to yesterday. I wanted you to say the bird was funny."
{n}She opens its beak, then lets it fall shut.{/n}
"I still want that. But you can say something else too."
{n}Inside, Pella finds the missing button caught in a cuff. The customer gives an embarrassed little cough. Ember listens until the door has closed behind her.{/n}
"She said sorry. Pella said she'd sew it on again. I don't think they like each other very much."''', c('"People can put something right without becoming friends."', "discuss")),
    n("discuss", "Ember", '''"The bird doesn't have to be his friend. I know."
{n}Her answer comes quickly. She rubs a frayed edge on the fox's ear.{/n}
"But I want him to want to. Otherwise the fox is by himself again."
{n}She looks at the two figures lying apart on her knees.{/n}
"I can move them wherever I want. That makes it easy to give him a friend. I don't know how to make it look as though the bird chose."''',
      c('"Give the bird something it enjoys about the fox. We only saw what the fox needed."', "enjoy", flags=("ember.revision_laughter",)),
      c('"Let them part for a while. The bird can decide to seek him out later."', "part", flags=("ember.revision_distance",))),
    n("enjoy", "Ember", '''"The fox is funny. Only we knew that before we started."
{n}She makes the bird look at the fox.{/n}
"Perhaps the fox knows a song. A very bad one. The bird could teach him how it goes."
{n}She tries a tuneless hum, stops, and tries a worse one. Pella looks out of the doorway.{/n}
"Is that a new animal?"
"The fox singing."
"Ah. Keep him away from my customers."
{n}Ember laughs. Then she moves the bird closer, as though it has come to investigate the noise.{/n}
"He might come back because he wants to finish the song. It doesn't have to mean he thinks taking the boots was all right."''', c('"Try that. Keep the bird cross about the boots while they sing."', "remember")),
    n("part", "Ember", '''"Where does the fox go?"
{n}She asks as though the answer might take him out of reach.{/n}
"We could give him somewhere. A house with a gate. That might be where he caught his tail."
{n}She draws the green ribbon into a loop on her knee and places the fox inside it.{/n}
"Then the bird knows where he is. He can go past without going in."
{n}The bird makes a circuit of the little house. On the second pass, Ember stops it beside the gate.{/n}
"He might ask whether the fox has breakfast today. And the fox could say yes. He could have something to offer this time."''', c('"Let the fox offer it. Then the bird has a reason to stay."', "remember")),
    n("remember", "Narrator", '''{n}Ember holds both figures still. The ribbon hangs between them, waiting to become a gate or a new bit of costume.{/n}''',
      c('"Keep the journey where the fox carries the luggage. That work still matters."', "work", requires=("ember.play_restitution",)),
      c('"Keep the part where the fox returns the boots before asking for help."', "request", requires=("ember.play_explanation",))),
    n("work", "Ember", '''"Yes. He did that. I don't want him to have to start over every time somebody remembers he took them."
{n}She puts the parcel beside him.{/n}
"But carrying it doesn't mean he gets to choose what the bird does next. He'll have to put it down and wait."
{n}The fox sets down the luggage. Ember gives it a sneeze to fill the silence, then shakes her head.{/n}
"Perhaps he can wait without making everybody laugh. Just for a little while."''', c('[Leave a quiet pause in the new ending.]', "private")),
    n("request", "Ember", '''"Yes. The bird can help with new boots and still go home afterward."
{n}She unrolls the scrap into two small pieces.{/n}
"The fox doesn't have to lose these because the bird leaves. They're his now."
{n}She places them beside the fox, then moves the bird away. For a moment she lets them stay apart.{/n}
"I think I was making the breakfast do too much. They can have breakfast, and then something else can happen."''', c('[Leave room for another day in the story.]', "private")),
    n("private", "Ember", '''"Could we try it with just us first?"
{n}She gathers the figures against her patched dress.{/n}
"Pella has work, and Ilva will ask whether it is finished. I don't want to say yes before I've heard it."
{n}The green ribbon slips. You catch it before it reaches the dusty step.{/n}
"There. We have already saved one piece of the story."''', c('[Agree to a private rehearsal.]', flags=("ember.puppet_revision",))),
], requires=("ember.puppet_performed",))

s("second_ending", "A visitor at the fox's gate", [
    n("start", "Narrator", '''{n}Ember has borrowed a small tray from Pella, who made her promise to return it before supper. The courtyard table is covered in clean laundry today. You settle on the broad step with the tray between you and the puppets laid beside it.{/n}
"Only the end," Ember says. "We know how the beginning goes."
{n}She has mended the bird's beak. The thread now passes through a smooth loop, and the jaw closes when she lets it go.{/n}
"It doesn't laugh unless I want it to. That's useful. Sometimes I don't want it to."''',
      c('[Take the fox, as before.]', "fox", requires=("ember.player_fox",)),
      c('[Ask where she would like the narration to begin.]', "narrator", requires=("ember.player_narrates",)),
      c('[Ask to try the ending another afternoon.]', abort=True)),
    n("fox", "Ember", '''"You can say something I haven't thought of. Only don't have him take the boots again. I don't want that today."
{n}You make the fox inspect the bird's boots from a respectful distance. It announces that it has retired from collecting other people's footwear.{/n}
"Good," says the bird. "Then we can talk about something else."
{n}Ember looks up from the tray.{/n}
"I like that. We haven't let them talk about much else."''', c('[Begin the new ending.]', "version")),
    n("narrator", "Ember", '''"Say the bird has finished breakfast. He doesn't have to go anywhere yet."
{n}You describe an afternoon with no urgent journey. Ember moves the bird to the tray's rim, where it can look over the edge without falling.{/n}
"And the fox is there. He isn't asking for anything."
{n}The fox looks up. Ember tries its solemn voice, then clears her throat and makes it a little less grand.{/n}
"I had a good breakfast. Thank you."
{n}She glances at you.{/n}
"I forgot to have him say that before."''', c('[Begin the new ending.]', "version")),
    n("version", "Narrator", '''{n}The returned boots stand beside the bird. The fox has its own place on the tray, with enough space between them for a pause.{/n}''',
      c('[Let the fox attempt its terrible song.]', "song", requires=("ember.revision_laughter",)),
      c('[Follow the bird past the fox\'s gate.]', "gate", requires=("ember.revision_distance",))),
    n("song", "Narrator", '''{n}The fox begins with a verse about a splendid tail. It loses the tune halfway through, starts again, and ends on a note that causes the bird to turn its head.{/n}
"You have left part of it out," the bird says.
"The dull part."
"The part that makes it a song."
{n}The bird supplies three clear notes. The fox copies two and misses the third. Ember repeats the passage until both figures can get through it together.{/n}
"Tomorrow," says the bird, "I might show you the next bit."
{n}The fox asks whether the next bit mentions its tail. The bird says no, but they can probably fit it in.{/n}
{n}Ember puts the bird down. This time the silence at the end has nothing caught inside it.{/n}
"He wants to come back. We let him say it himself."''', c('"And the fox has something to practice while he waits."', "heard")),
    n("gate", "Narrator", '''{n}The green ribbon makes a gate across the tray. The fox has gone home. The bird passes once, carrying its boots. On the next pass it slows beside the gate.{/n}
"Have you had breakfast?"
"Yes," says the fox. "There is a little left."
{n}The bird studies the gate. The fox waits on the other side without dragging it open.{/n}
"May I bring my boots in?"
"You may keep them on."
{n}The bird enters. For a little while, the two figures sit beside an imaginary bowl. Then the bird says it must go. The fox says it can come another time, if it likes.{/n}
{n}Ember brings the bird out through the gate and lowers it beside the tray.{/n}
"It doesn't have to be forever. He came in today."''', c('"That is an ending we can show without promising tomorrow."', "heard")),
    n("heard", "Ember", '''"I want to keep this one."
{n}She coils the green ribbon around the fox's handle.{/n}
"Ilva might still ask about tomorrow. That's all right. I think I can say I don't know without feeling as though I forgot to finish."
{n}A cart rattles past the courtyard. Ember waits until the noise has gone.{/n}
"Did you like doing this? You have done a lot of afternoons now. You don't have to keep saying yes because I asked the first time."''',
      c('"I like our afternoons. I would like more of them."', "more", flags=("ember.puppet_more",)),
      c('"I liked making this with you. Next time, could we do something without an audience?"', "quiet", flags=("ember.puppet_quiet",))),
    n("more", "Ember", '''"Then we can think of another. Later."
{n}She gives the bird one last opening and closing of its beak.{/n}
"I don't want every afternoon to be getting ready for the next one. Sometimes we can just have it."
{n}She leaves the figures on the step while she checks the tray for loose thread. There is a tiny yellow scrap caught under its rim. She puts it in the bag with the boots.{/n}
"And sometimes I might want to make something by myself. I'll tell you when I do."''', c('"Tell me. I will do the same."', "end")),
    n("quiet", "Ember", '''"Yes. We can do that."
{n}She looks toward the empty stools stacked inside Pella's doorway.{/n}
"I wanted people to like the story. I still do. But I don't want to spend all my time waiting to find out."
{n}She puts the bird beside the fox in their little bag.{/n}
"You could show me something you like. It doesn't have to be something you're good at. I think we have done very well without that."''', c('"I can think of several things I am bad at."', "end")),
    n("end", "Narrator", '''{n}Ember laughs and takes the tray back to Pella. You hear her ask whether the mended blue cloth needs carrying upstairs. Pella says it does, then gives precise directions about which shelf is clear.{/n}
{n}When Ember returns, she sits beside the bag of puppets and looks out through the courtyard doorway. Neither figure needs moving. For a while, you stay with her and watch the street.{/n}''', c('[Keep her company until it is time to go.]', flags=("ember.puppet_afternoons_kept",))),
], requires=("ember.puppet_revision",))

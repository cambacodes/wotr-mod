"""Authored consequences of making room for a civilian life during the crusade.

Ista's stolen book, Nell's lanterns and the gathering are alternate developments.
They change no native military, inventory, marriage or morale state.
"""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, owner, entry, nodes, requires=(), delay=48):
    SCENES.append(scene(id, title, owner, 3, entry, nodes,
                        requires=("three_small_journeys.kept", "kept_terms", *requires),
                        forbids=("closed", "loss", "inhuman", "irabeth_away",
                                 "anevia_away", "last_watch"),
                        delay=delay, optional=True, Relationship="tirabade",
                        Areas=[DREZEN], Chapters=[3, 5],
                        ForbidOverrides={"last_watch": "three_progression.catchup_requested"}))


s("three_stolen_roads", "Someone else's journey", "Together",
  '\"Shall we find something for that map of ours?\"', [
    n("start", "Anevia", '''{n}Anevia has a paper packet tucked beneath her arm. A corner of yellow cloth protrudes from it. Irabeth notices you noticing it and gives a small, solemn shake of her head.{/n}
"She has refused to tell me."
"You don't have to sound so wounded. It's a surprise, not a conspiracy."
{n}At the next stall Anevia stops. Among the combs and travel cups lies a small book with a blue leather cover. One corner has been stitched with red thread.{/n}
"That's Ista's."
{n}The woman behind the stall looks up.{/n}
"It belongs to the person who buys it."
"Does Ista know that?" {n}Anevia asks.{/n}''',
      c('[Look at the book.]', "book"),
      c('[Ask to visit the stalls another time.]', abort=True)),
    n("book", "Narrator", '''{n}The book contains hand-drawn roads, sketches of bridges, and cramped notes about places to sleep. A folded page at the back shows a garden behind a mill. Anevia keeps her hands off it.{/n}
{n}"Ista repairs wagon covers," she tells you. "Beth bought our map from her. She showed me this when I asked about the market town. Sewed that corner herself. Said it held together better than the journey."{/n}
{n}"Then she should not have sold it," the stallkeeper says.{/n}
{n}"Did she sell it to you?" Irabeth asks.{/n}
{n}"A man left it on commission. Vald. Tall, split front tooth. Said it was his wife's. I am Gresa, if we are having introductions."{/n}
{n}Anevia looks toward the neighboring stalls.{/n}
{n}"Ista's wife is shorter than me. Better teeth, too."{/n}
{n}Gresa draws the book back from the edge.{/n}
{n}"That does sound like a difficulty."{/n}''', c('"Where is Ista?"', "owner")),
    n("owner", "Irabeth", '''"At the wagon yard. We passed her sign."
{n}Gresa puts a scrap of cloth over the book.{/n}
"Go and ask. I will not sell it until you come back. Nor will I hand it to you because someone knows the stitching."
"Good," {n}Irabeth says.{/n}
{n}Anevia raises an eyebrow, but follows her away from the stall.{/n}
{n}Ista is mending a cover beside her cart. When you describe the book, she drops the needle into her lap.{/n}
"The blue one? I thought my wife had packed it."
{n}She opens a small chest. Its lock hangs loose. Inside, a rectangular space interrupts the neatly stacked cloth.{/n}
"And the letters. The delivery acknowledgments. All in a tied bundle."
{n}Irabeth examines the hasp without touching it.{/n}
"Who has been here?"
"Customers. Half a dozen. A man asking about a cover he never ordered. I cannot tell you which of them opened it."
{n}Ista closes the lid very gently.{/n}''', c('[Ask what the missing papers mean for her.]', "stakes")),
    n("stakes", "Ista", '''"People paid me to bring things. Now I have to write and ask them to say I did. Some will. Some will have better uses for their time."
{n}She folds her hands over the needle in her lap.{/n}
"The book is mine. Years of it. Places I went before I met my wife. Places we argued about after. There is a page with a very good fish supper and three different accounts of whose idea it was to stop."
{n}Anevia crouches beside the chest.{/n}
"Vald may have the bundle nearby. He'll need to come back for his money. We could watch where he goes."
"We should secure the book first," {n}Irabeth says.{/n} "If he notices anything wrong, he may run with what remains."
"If we take it now, Gresa has to tell him why she can't sell it. We get the book and a description we've already got."
{n}Ista turns the needle over.{/n}
"I want both. I know that is not an answer you can use."''', c('[Return to Gresa and discuss the possibilities.]', "decision")),
    n("decision", "Narrator", '''{n}Ista accompanies you. Gresa asks her about the folded garden drawing without opening it. Ista describes the broken mill wheel on its reverse. Gresa checks, then sets the book within Ista's reach.{/n}
{n}"Yours. What do you want to do?"{/n}
{n}Anevia explains her idea. Gresa can tell Vald that somebody is considering the price and ask him to return later. Nobody will buy stolen goods or pay to make the deception work.{/n}
{n}"He may go back to wherever he put the bundle," Anevia says. "Or he may go drinkin'. We don't know."{/n}
{n}"And if he asks for the book back?" Irabeth asks.{/n}
{n}Gresa shrugs. "I cannot keep a thief here by talking forever."{/n}
{n}Ista touches the blue cover, then withdraws her hand.{/n}
{n}"I will risk waiting for the papers. But if you think we should take this and stop, say so. I do not want you promising a chase through the whole city."{/n}
{n}"Only while we can keep him in sight," Anevia says. "No heroic guessing."{/n}
{n}Irabeth nods reluctantly.{/n}''',
      c('"Take the book now. We can help Ista replace the acknowledgments without risking this."', "secure", flags=("three_stolen_roads.book_safe",)),
      c('"Watch for Vald. We will follow while we can see him, then stop."', "watch", flags=("three_stolen_roads.followed",))),
    n("secure", "Narrator", '''{n}Ista wraps the book in a cloth. Gresa supplies a description of Vald's coat and the time he left it. Irabeth writes them down for Ista's report.{/n}
{n}"If he comes back?" Gresa asks.{/n}
{n}"Tell him the owner collected her property," Irabeth says. "Do not try to hold him alone."{/n}
{n}Anevia studies the openings between the stalls. By the time Ista has read the note, the market is growing busy. There are too many backs in brown coats.{/n}
{n}"He could have seen us from any of those gaps," she says. "Or he hasn't come back at all."{/n}
{n}Ista opens the book to its folded page. Her thumb pauses over the mill.{/n}
{n}"This much is home, anyway."{/n}
{n}Anevia looks at her, then helps tie the cloth securely. The missing bundle remains missing.{/n}''', c('[Walk Ista back to her cart.]', "after")),
    n("watch", "Narrator", '''{n}You wait at separate stalls. Irabeth stays where she can see Gresa's counter. Anevia chooses a place beside a rack of pans, with a view of both ends of the lane.{/n}
{n}Vald returns before the lamps are lit. Gresa speaks to him, pointing at the covered book. He listens, looks around, and takes it back despite her attempt to keep him talking.{/n}
{n}He walks toward the wagon yard. Anevia follows at a distance. You and Irabeth keep her in sight.{/n}
{n}At a narrow service passage, Vald whistles. A second man steps out with a tied bundle under his arm. Vald opens the book and shows him a page. The other man shakes his head.{/n}
{n}Then a cart turns into the passage. Its driver calls for room. Vald looks back and sees Irabeth.{/n}
{n}"Leave it," she calls. "Both of you."{/n}''', c('[Move to stop them.]', "flight")),
    n("flight", "Narrator", '''{n}The man with the bundle drops it beneath the cart and bolts through a side door. Vald flings the book after it and runs the other way. Anevia catches his coat, but the seam tears. He leaves her holding a strip of brown cloth.{/n}
{n}You stop the cart before its rear wheel reaches the bundle. Irabeth retrieves the papers. The front wheel has already passed over the book, crushing its spine against the stones.{/n}
{n}Anevia takes two steps toward Vald, then stops at the crowded lane. She looks back at the open side door. Neither man is visible.{/n}
{n}"That's as far as we said," she says. She sounds furious.{/n}
{n}Irabeth gathers the loose pages. Anevia kneels to help her. Between them they find every sheet they can see, including the mill drawing, now split along an old fold.{/n}
{n}Ista is waiting with Gresa. When Irabeth gives her the bundle, she checks the knots before looking at the ruined binding.{/n}
{n}"These are mine," she says. Then, more quietly, "So is that."{/n}''', c('[Help Ista carry what was recovered.]', "after")),
    n("after", "Anevia", '''{n}Ista returns to her cart to examine what she has. You leave her the account you have written. Anevia folds the note after Ista has read it.{/n}
"Wanted us to buy something useless," {n}she says.{/n} "Managed another report."
{n}Irabeth looks at the yellow corner still protruding from her wife's packet.{/n}
"You did buy something."
"Before the evening took a turn. It's a sash. There were supposed to be lanterns, too. Music. You looking surprised."
{n}Irabeth stops walking.{/n}
"I am surprised."
"Later, Beth. I'm too cross to appreciate it properly."
{n}Irabeth waits until Anevia looks at her.{/n}
"Then later. I will choose the music, if you still want the evening."
{n}Anevia exhales.{/n}
"I do. I want both of you there."''', c('[Arrange another evening together.]', flags=("three_stolen_roads.settled",))),
])


s("three_lantern_debt", "What she had arranged", "Anevia",
  '"Shall we fetch those lanterns?"', [
    n("start", "Anevia", '''"Beth's coming when she's done. We can get a head start."
{n}Anevia has brought a folded sack with two carrying straps. She hands you one end before testing the other.{/n}
"Nell lent me four. She paints the shades herself. Said she'd trust me with the lamps if I promised not to make jokes about the birds."
{n}You turn the corner beside a narrow workshop. Four paper shades hang in the window. Their painted birds have round bodies and legs at improbable angles.{/n}
"Been rehearsin' my silence," {n}Anevia tells you.{/n} "Hardest part of the arrangement."''',
      c('[Go into the workshop with her.]', "nell"),
      c('[Offer to help another time.]', abort=True)),
    n("nell", "Narrator", '''{n}Nell is an older woman with paint on her cuffs and a thick bandage around one thumb. She points to the shades before Anevia can speak.{/n}
{n}"Plovers."{/n}
{n}"Wouldn't dream of disagreein'."{/n}
{n}"You did last time."{/n}
{n}"Learned somethin'."{/n}
{n}Nell takes a lamp from the shelf. A narrow metal cup sits beneath the shade, well clear of the paper.{/n}
{n}"Carry the frames separately. You can fit them at the yard. Keep the paper away from the flame, keep them out of the rain, and put them out before anybody starts being interesting."{/n}
{n}Anevia opens the sack. Nell does not hand over the lamp.{/n}
{n}"You said you would sit for me."{/n}
{n}"I said you could try drawin' me. Didn't realize you meant today."{/n}
{n}"I did not realize you meant never."{/n}''', c('"A portrait?"', "portrait")),
    n("portrait", "Anevia", '''"A sketch. She needs faces to practice on. I needed lanterns. Thought she might forget."
{n}Nell retrieves a board with paper pinned to it.{/n}
"I remembered. There is a chair."
{n}Anevia sits, but turns the chair until she can see the door. Nell lifts her pencil, lowers it again, then moves her own stool.{/n}
"You could simply have asked me to sit on this side."
"Could've. We're here now."
{n}Nell begins with the shape of Anevia's face. Anevia watches the pencil for a while, then looks at you.{/n}
"Well? You're not obliged to help her. But if you've got somethin' entertaining to say, this would be a fine time."''',
      c('"Tell me how you found a painter who lends lanterns."', "meeting"),
      c('"I rather like having time to look at you."', "look", flags=("three_lantern_debt.looked",))),
    n("meeting", "Anevia", '''"Saw the window. Came in to ask what sort of birds they were. Nell told me. Very firmly."
"She wanted a lamp that made people look handsome," {n}Nell says.{/n}
"I said warm."
"You asked whether yellow light was kinder than white."
{n}Anevia gives you a warning look which has very little force behind it.{/n}
"Certain people make a terrible fuss about their own faces. Thought I could spare myself the argument."
{n}Nell pauses.{/n}
"And your wife? Does she know you say that?"
"Usually say it to her. She knows what I think of her face."
{n}The pencil moves again. Anevia sits still for longer this time.{/n}
"Wanted her to catch herself lookin' beautiful without first decidin' whether she was allowed to enjoy it. The light won't do all that. I know. But I can arrange a lamp."''', c('[Remain with her while Nell draws.]', "waiting")),
    n("look", "Anevia", '''"Careful. I might get accustomed to it."
{n}Nell asks her to turn her chin a little. Anevia obeys, then steals a glance back at you.{/n}
"Suppose this is fair. I've spent enough time watchin' you when you thought nobody was interested."
"Did I?"
"Some days. Other days you were quite pleased with yourself. Liked those too."
{n}Nell makes a small impatient sound. Anevia stops talking long enough for the line of her mouth to be drawn.{/n}
"There," {n}Nell says.{/n} "Now you may misbehave again."
{n}Anevia laughs. The painter makes two quick marks before the expression is gone.{/n}
"That's cheating," {n}Anevia says.{/n}
"You would know."''', c('[Remain with her while Nell draws.]', "waiting")),
    n("waiting", "Anevia", '''{n}Nell goes to find a softer pencil. Anevia stretches her fingers over her knees.{/n}
"I keep thinkin' about that stall. All those people walkin' past. One of them might have bought Ista's book, taken it home and thought they'd found somethin' lovely."
{n}She looks at the lamps waiting on the shelf.{/n}
"I know how to get somebody to turn their head. Ask the right question, drop something by the wrong foot. Used to think I was very clever."
{n}She rubs at a fleck of yellow paint on the chair arm.{/n}
"Was clever. That wasn't the problem."
{n}Nell returns, hears the last words, and sensibly asks nothing.{/n}''',
      c('"You wanted to follow him because you knew the trick."', "followed", requires=("three_stolen_roads.followed",)),
      c('"You still wish we had followed him."', "secured", requires=("three_stolen_roads.book_safe",))),
    n("followed", "Anevia", '''"Thought I did. Then he looked back, and I had a fistful of coat."
{n}She closes her empty hand.{/n}
"Ista got the acknowledgments. That matters. I'm allowed to be pleased about that. Keep tellin' myself."
"And the book?"
"I can still hear the wheel."
{n}Nell lowers her pencil. Anevia waves for her to continue.{/n}
"Beth didn't say she told us so. Made it worse, somehow. I was ready for that argument. Had all my answers. Instead she asked whether I'd cut my hand on the stones."
{n}She looks down at her uninjured palm.{/n}
"I wanted to catch him. Not just get the papers. Wanted her to see me do it."''', c('[Stay with her while she finds the next words.]', "admission")),
    n("secured", "Anevia", '''"Yes."
{n}She says it before Nell has settled on her stool.{/n}
"Ista got the book. I know why we stopped. But I've been through the lane twice since, lookin' at the doors. As though they'll tell me where he went if I stare hard enough."
"Have you found anything?"
"A woman who wanted to know why I was blockin' her delivery. Fair question."
{n}She settles back, giving Nell the angle she wants.{/n}
"Beth offered to come next time. Didn't ask if there ought to be a next time. I almost wished she had. Could've told her she didn't understand."
{n}Anevia lets out an irritated little laugh.{/n}
"She understands quite a lot. Inconvenient woman."''', c('[Stay with her while she finds the next words.]', "admission")),
    n("admission", "Anevia", '''"I used to think knowing the bad little tricks made me the useful one when respectable people got lost. There I was, with Beth beside me, and I wanted to be right in front of her."
{n}Nell pauses to sharpen her pencil. Anevia turns toward you while she can.{/n}
"Wanted you watching too. That's the embarrassing part. Could have picked a less expensive performance."
{n}Her gaze holds yours.{/n}
"Don't tell me you only like me when I'm sensible. I'd have to assume you've been confused for quite some time."''',
      c('"I like your nerve. I also want to hear when you are guessing."', "nerve", flags=("three_lantern_debt.nerve",)),
      c('"I wanted to be in that adventure with you. I am still thinking about what it cost Ista."', "cost", flags=("three_lantern_debt.cost",))),
    n("nerve", "Anevia", '''"Most of the time. I can tell you when I've got something better."
{n}Nell asks her to face forward. Anevia obeys.{/n}
"Beth said she liked me before I learned to make my bad ideas sound official. I asked whether that was a compliment. She told me to work it out."
{n}The smile returns slowly.{/n}
"Suppose I deserved that one."
{n}She glances back at you.{/n}
"I've arranged four lamps and a yellow sash. Can guarantee the sash. Everything after that, we're taking our chances."''', c('[Wait while Nell finishes the sketch.]', "arrival")),
    n("cost", "Anevia", '''"Me too. Doesn't stop me wishing you'd seen me catch him."
{n}She gives Nell her profile again.{/n}
"I told Beth that. She said she would have liked to see it. Then she asked whether I could stop turning our walk into a trial of my worth as a wife."
{n}Nell's pencil stills. Anevia looks at her.{/n}
"You may draw the face I made. Would save me doing it again."
{n}The painter resumes. Anevia rests her hands in her lap.{/n}
"I'm still cross. But I want that dance. Want both of you looking at me for reasons that have nothing to do with Vald."''', c('[Wait while Nell finishes the sketch.]', "arrival")),
    n("arrival", "Narrator", '''{n}Irabeth arrives as Nell unpins the paper. She stops just inside the door.{/n}
{n}"You did not mention this."{/n}
{n}"Neither did Nell. Until she had the lamps where I couldn't reach them."{/n}
{n}Nell holds up the drawing. Anevia is caught looking sideways, her mouth beginning a smile which has not yet become a joke.{/n}
{n}Irabeth comes closer. She looks at the paper for so long that Anevia shifts in her chair.{/n}
{n}"It's a sketch, Beth. You don't have to approve a fortification."{/n}
{n}"May I buy it?" Irabeth asks Nell.{/n}
{n}"It is hers. She gave me the practice."{/n}
{n}Anevia looks from one woman to the other, then takes the paper.{/n}
{n}"You can have it," she tells Irabeth. "But I get to complain about the place you hang it."{/n}''',
      c('"Keep it somewhere you can enjoy it together."', "private", flags=("three_lantern_debt.private_sketch",)),
      c('"Show it to me again when the lanterns are lit. I want to compare."', "compare", flags=("three_lantern_debt.shared_sketch",))),
    n("private", "Irabeth", '''"Beside the bed, perhaps."
{n}Anevia looks suddenly pleased, then makes an attempt to conceal it by inspecting the edge of the paper.{/n}
"Where I can catch you lookin' at it. Sensible."
{n}Irabeth takes the drawing by its dry corners.{/n}
"I shall be looking at you. This is for when you get up before I do."
{n}Nell begins packing the lamp cups, humming to herself with conspicuous determination.{/n}''', c('[Help carry the lamps.]', "carrying")),
    n("compare", "Anevia", '''"Well, now she has to bring me. Can't send the drawing and say I'm busy."
{n}Irabeth holds the paper beside her wife's face.{/n}
"It is a good likeness. But it does not keep interrupting me."
"You'll get bored."
"Very quickly."
{n}Anevia catches her wife's wrist and kisses the inside of it before letting her roll up the drawing. Nell pretends to count the four lamp cups twice.{/n}''', c('[Help carry the lamps.]', "carrying")),
    n("carrying", "Narrator", '''{n}The shades ride in their own box. You carry them while the wives take opposite ends of the sack. Irabeth has wrapped the drawing in a clean scrap of canvas and tucked it inside her coat.{/n}
{n}"You could have asked me to sit for you," Anevia says as you leave.{/n}
{n}"I cannot draw."{/n}
{n}"Didn't say you had to draw."{/n}
{n}Irabeth misses half a step. Anevia keeps the lamps level, smiling straight ahead. At the next turn, Irabeth deliberately takes the longer way, where the street is quieter.{/n}
{n}When you catch up, she asks you whether you have chosen what to wear. Anevia listens with an interest which makes the question rather less innocent.{/n}''', c('[Tell them what you have in mind.]', flags=("three_lantern_debt.kept",))),
], requires=("three_stolen_roads.settled",), delay=24)


s("three_beth_steps", "An unfamiliar step", "Irabeth",
  '"You said you wanted my help with the music."', [
    n("start", "Irabeth", '''"I wanted your help with what happens during it. The music is arranged."
{n}Irabeth has moved a bench away from the wall. A folded coat lies over its back. She picks it up, considers putting it on, and lays it down again.{/n}
"Tessa knows a fiddler. The daughter of one of her regular players. Her name is Veska. She will play a few dances in exchange for supper."
{n}Irabeth looks at the space she has cleared.{/n}
"I told Anevia I would choose one. Then I remembered that choosing it and doing it were different difficulties."''',
      c('"Show me what you remember."', "lesson"),
      c('[Arrange to practice later.]', abort=True)),
    n("lesson", "Irabeth", '''{n}She offers you her hand, keeping her other hand carefully at her side.{/n}
"It is a turning dance. Walk together, change places, turn. I know the count."
{n}She demonstrates the first steps without you, counting under her breath. On the turn she comes too close to the bench and stops.{/n}
"Usually there would be more room."
{n}You move the bench farther back. She watches, then laughs at herself.{/n}
"Yes. That was an available solution."
{n}This time she asks you to join her. The first change of places works. The second leaves you facing the wrong direction.{/n}
"I think that was mine," {n}she says.{/n} "I tried to correct you before you had finished moving."''',
      c('"Let me lead this time. You can find out where I am going."', "follow", flags=("three_beth_steps.followed",)),
      c('"Keep leading. Give me time to follow the step you actually take."', "lead", flags=("three_beth_steps.led",))),
    n("follow", "Narrator", '''{n}Irabeth places her hand against your shoulder. You count softly and begin. She starts a turn too soon, catches herself and waits, her mouth pressed into a line of concentration.{/n}
{n}You finish the change of places. She follows the turn cleanly. Her face brightens, then she notices you watching.{/n}
{n}"Do not look so surprised."{/n}
{n}"I was enjoying it."{/n}
{n}"Then you may look a little."{/n}
{n}On the next turn, you almost collide with the bench yourself. She stops you with a firm hand and a less restrained laugh.{/n}
{n}"Shall I move it again?"{/n}''', c('[Try again, keeping clear of the bench.]', "coat")),
    n("lead", "Narrator", '''{n}Irabeth returns to the first position. This time she gives you the whole beat before turning. You move together, change places, and arrive facing one another.{/n}
{n}"Oh," she says.{/n}
{n}The next attempt is less successful. She forgets her feet while checking yours and brushes your boot with her own. You recover before either of you can apologize.{/n}
{n}"I thought I was past that part," she says.{/n}
{n}"We managed the turn."{/n}
{n}"We did. I would like to do it again while still standing on my own feet."{/n}
{n}She offers her hand with considerably less ceremony.{/n}''', c('[Practice until you can make the turn together.]', "coat")),
    n("coat", "Irabeth", '''{n}After several attempts, Irabeth puts on the coat. It is dark blue, with plain fastenings and sleeves she has had shortened. She rolls her shoulders, testing the fit.{/n}
"I thought the old one might do. Then I tried it, and the lining tore. I have asked a tailor to mend it for ordinary wear. This is borrowed from her stock until I decide whether I want it."
{n}She smooths the front once.{/n}
"I do want it. I am trying to stop finding more respectable reasons to say so."
"Is wanting to wear it not enough?"
"For the tailor, certainly. She grew tired of my explanations before I did."
{n}Irabeth turns slightly, looking for a reflection in the dark window.{/n}
"What do you think?"''',
      c('"Leave it open. I like seeing the shape of you beneath it."', "open", flags=("three_beth_steps.open_coat",)),
      c('"Fasten it, then try the turn. I want to see you move in it."', "fastened", flags=("three_beth_steps.fastened_coat",))),
    n("open", "Irabeth", '''{n}She stills with her fingers on the second fastening.{/n}
"That is a direct answer."
{n}She undoes the first and lets the coat fall open. The flush in her cheeks deepens when you continue looking.{/n}
"Anevia will say something dreadful if she sees me standing like this."
"Will you mind?"
{n}Irabeth considers the question with a seriousness which does not last.{/n}
"I may encourage her."
{n}She comes back to the cleared space. When she offers her hand, she stands closer than she did before.{/n}''', c('[Take another turn with her.]', "tessa")),
    n("fastened", "Narrator", '''{n}Irabeth closes the coat and takes her place. The hem swings away from her legs as she turns. She notices it in the window and tries the movement again, this time without counting.{/n}
{n}"The tailor said it would do that. I thought she was trying to sell me something."{/n}
{n}"She was."{/n}
{n}"Successfully, it seems."{/n}
{n}Irabeth looks over her shoulder at the falling cloth, smiling. Then she catches you looking at her instead of the coat and returns to you without adjusting a thing.{/n}''', c('[Take another turn with her.]', "tessa")),
    n("tessa", "Irabeth", '''{n}You pause when the room becomes too warm. Irabeth opens the window a little.{/n}
"Anevia told me she wanted to catch Vald while I watched. I was so surprised that I answered badly."
"What did you say?"
"That I would have enjoyed watching him caught. Which was true, and not what she was trying to tell me."
{n}Irabeth leans one shoulder against the wall.{/n}
"I know she is capable. I think I forget how little use that knowledge is if I never say anything until she has been hurt."
{n}From outside comes the scrape of a cart wheel. She listens until it has passed.{/n}''',
      c('"What do you think of our decision now?"', "followed", requires=("three_stolen_roads.followed",)),
      c('"What do you think of our decision now?"', "secured", requires=("three_stolen_roads.book_safe",))),
    n("followed", "Irabeth", '''"We recovered the papers. I did not think we would."
{n}She rubs her thumb along the edge of the windowsill.{/n}
"When the book went under the wheel, I wanted to tell Anevia that this was why I had objected. Then I picked up the bundle."
{n}She looks back at you.{/n}
"I had wanted a clean answer as much as she had. Secure the book, write the report, leave knowing we had done something properly. Ista would still have needed those acknowledgments."
"Do you wish we had stopped?"
"I wish Vald had not stolen them. That is the only answer I have managed without changing it ten minutes later."''', c('[Sit with her for a moment.]', "uneasy")),
    n("secured", "Irabeth", '''"I am glad Ista has her book. I saw her holding it when we left."
{n}She rubs her thumb along the edge of the windowsill.{/n}
"Then she started listing everyone she had to write to. I could have helped her spell the names. I could not make them answer."
{n}She looks back at you.{/n}
"I wanted securing the book to be enough. It was the part I could be certain about. Anevia was looking at the rest of the problem."
"Would you choose differently?"
"Perhaps. Then I remember that he could have taken the book away too, and I change my mind again. I have very little patience with myself this week."''', c('[Sit with her for a moment.]', "uneasy")),
    n("uneasy", "Irabeth", '''{n}Irabeth sits on the end of the bench, leaving room for you.{/n}
"I can bear people disagreeing with me. I have had practice. It is harder when I want to go home with them afterward and I am still composing the argument."
{n}She looks down at the blue cloth across her knees.{/n}
"Anevia asked me to dance. I nearly explained why this was a poor time. Then I realized I was going to give her a report instead of an answer."
{n}She reaches for your hand.{/n}
"I do not want that to be all I bring either of you."''',
      c('"I can disagree with you and still want you. You can be annoyed with me too."', "argument", flags=("three_beth_steps.argument",)),
      c('"I want an evening when we are allowed to forget the argument for a while."', "respite", flags=("three_beth_steps.respite",))),
    n("argument", "Irabeth", '''"I shall try to remember that before delivering my next explanation."
{n}She squeezes your hand, then lets it rest against her knee.{/n}
"Anevia said something similar. With more threats about confiscating my papers."
{n}Her smile grows.{/n}
"I love her when she is difficult. I should be less surprised that she returns the favor."
{n}She rises and offers you her hand again.{/n}
"One more turn. I am buying this coat. We may as well find out whether it survives my enthusiasm."''', c('[Return to the practice space together.]', "ending")),
    n("respite", "Irabeth", '''"So do I. I keep thinking that I have to settle it before I can enjoy anything."
{n}She looks toward the window, then back at you.{/n}
"We could spend the whole evening on that bench and still have the same missing answers. I would rather find out whether Anevia likes this coat."
"I suspect she will tell you."
"At length, if I am fortunate."
{n}Irabeth stands and offers her hand.{/n}
"One more turn. Before I find another reason to sit down."''', c('[Return to the practice space together.]', "ending")),
    n("ending", "Irabeth", '''{n}Irabeth closes the window before you try again. The last turn works without either of you counting aloud. Irabeth remains close when it ends. Her thumb moves against the back of your hand.{/n}
"Thank you. I was making rather a large obstacle out of four steps."
{n}She looks down at your joined hands, then meets your eyes.{/n}
"I would like to kiss you. Before we put the bench back. I may lose my courage while moving furniture."
{n}The joke does not quite hide how much she wants the answer.{/n}''',
      c('[Kiss her and stay close for a while.]', "kiss", flags=("three_beth_steps.kissed",)),
      c('"Hold me for a moment. That is what I want tonight."', "hold", flags=("three_beth_steps.held",))),
    n("kiss", "Narrator", '''{n}Irabeth bends toward you. The first kiss is careful. When you draw her closer, she makes a quiet, pleased sound and lets the next one last.{/n}
{n}Her new coat is warm beneath your hand. She catches its edge as you shift, then laughs against your cheek.{/n}
{n}"Still borrowed. I ought to buy it before we become careless."{/n}
{n}You step apart eventually. She looks at the bench as though she has only just remembered that furniture exists.{/n}''', c('[Help put the room back in order.]', flags=("three_beth_steps.learned",))),
    n("hold", "Narrator", '''{n}Irabeth puts her arms around you. She adjusts her stance so you can rest comfortably, then grows still.{/n}
{n}For a while you hear only the street beyond the closed window. When she lets you go, her hand remains at your shoulder.{/n}
{n}"I would like another dance with you. When Veska is there to keep us in time."{/n}
{n}She gives the empty floor a satisfied look before reaching for the bench.{/n}''', c('[Help put the room back in order.]', flags=("three_beth_steps.learned",))),
], requires=("three_stolen_roads.settled",), delay=24)


s("three_ista_departure", "The road she was taking", "Together",
  '\"Ista sent word that she wanted to see us.\"', [
    n("start", "Irabeth", '''"She is at the wagon yard. She asked us to come before the afternoon deliveries."
{n}Anevia has brought the descriptions you wrote down. She checks the folded sheet, then puts it away without explaining why she checked.{/n}
"Could've come herself," {n}she says.{/n}
"She has a cart to watch."
"Yes. I know."
{n}Irabeth touches her wife's elbow. Anevia does not move away, but she does not answer the touch until you have reached the corner. Then her hand closes briefly over Irabeth's.{/n}''',
      c('[Go to see Ista.]', "arrival"),
      c('[Send word that you need to arrange another time.]', abort=True)),
    n("arrival", "Narrator", '''{n}Ista stands beside a pile of folded covers. Another woman is tightening the strap around them. She introduces herself as Ista's wife, Wenna, then asks you to hold the strap while she moves its buckle.{/n}
{n}"I heard about the book," she says. "And the men."{/n}
{n}Anevia watches her work.{/n}
{n}"No sign of them since. We've given the descriptions to Ista."{/n}
{n}"She showed me. I do not know either of them."{/n}
{n}Wenna pulls the strap tight. You let go when she nods.{/n}
{n}Ista takes a small packet from the seat of the cart.{/n}
{n}"I wanted you to hear how things stand. Before you started imagining a better ending than the one I have."{/n}''',
      c('[Listen.]', "receipts", requires=("three_stolen_roads.followed",)),
      c('[Listen.]', "letters", requires=("three_stolen_roads.book_safe",))),
    n("receipts", "Ista", '''"The acknowledgments are all there. I can settle the deliveries and take my next load. We shall leave when the cart is ready."
{n}She opens the packet. Blue leather lies between two boards, its split spine stitched loosely enough to show the damage beneath.{/n}
"The book will never close properly. Wenna has put the loose pages in order. Most can be read. There are a few lines I cannot make out."
{n}Anevia starts to speak. Ista lifts a finger.{/n}
"I agreed to leave it at the stall. I remember. That does not make me like looking at it."
{n}She opens to the mill drawing. A strip of plain paper holds the halves together. On the reverse, a sentence ends where the wheel tore through it.{/n}
"That was an argument about a fish supper," {n}she says.{/n} "I remember the supper. I cannot remember what we thought was so funny afterward."
{n}Wenna reaches across and closes the book gently.{/n}
"We may remember on the road."''', c('[Give them a moment.]', "offer")),
    n("letters", "Ista", '''"Two customers have already answered. One sent a boy back with my letter and said he had no time for accounts. I will go myself. Perhaps he will find some time if I stand in his doorway."
{n}She opens the packet. The blue book rests inside, its red stitches bright against the worn corner.{/n}
"We should have been ready to leave. Instead we are taking small jobs here until I can settle enough deliveries to pay for the next load."
{n}Irabeth's eyes go to the stacked covers.{/n}
"How many acknowledgments remain?"
"Enough that you would start offering to write them. They are my customers. Some of them would mistake your attention for a threat."
{n}Irabeth closes her mouth, then nods.{/n}
{n}Wenna turns the book to its folded drawing.{/n}
"We have this. I am glad of it. I would also like to be leaving. Those facts have been sharing the same conversation for days."''', c('[Give them a moment.]', "offer")),
    n("offer", "Ista", '''{n}Ista draws a second sheet from the packet. It is a copy of the road between the garden and the market town on your own map.{/n}
"You asked about these places before the theft. I had started this for you. I finished it yesterday."
{n}Anevia looks at the little bridges marked across the river.{/n}
"You didn't have to."
"I know. You paid for the first map. This is something I wanted to give you."
{n}Ista taps a dotted turn beside the mill.{/n}
"That track has steep ground. Wenna likes to say I put it there to make her appreciate the other road."
"She took the turn without asking me," {n}Wenna says.{/n} "Then claimed the view was worth it."
{n}Irabeth studies the two routes.{/n}
"Was it?"
{n}Wenna's mouth twitches.{/n}
"Eventually."''',
      c('"Mark the steep way as well. We can decide when we get there."', "both", flags=("three_ista_departure.both_roads",)),
      c('"Show us the easier way. We have enough difficult ground behind us."', "easy", flags=("three_ista_departure.easy_road",))),
    n("both", "Narrator", '''{n}Wenna takes the pencil from Ista and adds a small mark beside the turn.{/n}
{n}"A place to rest before the steep part. Decide there. It becomes harder to admit a mistake once you have carried the basket halfway up."{/n}
{n}"We did enjoy ourselves," Ista says.{/n}
{n}"Yes. After I stopped being hungry."{/n}
{n}Anevia leans close to Irabeth.{/n}
{n}"I'm bringin' the bread. You can settle the geography."{/n}
{n}"You will have opinions about the geography."{/n}
{n}"Several. Thought I'd warn you now."{/n}''', c('[Thank them for the map.]', "leave")),
    n("easy", "Narrator", '''{n}Wenna draws a firm line along the river road, then dots the smaller track so it remains visible.{/n}
{n}"You can see the mill from below. Anyone who says you must climb to appreciate it can carry their own basket."{/n}
{n}Irabeth studies the little line.{/n}
{n}"I would like to try a day with no steep part."{/n}
{n}"Could manage that," Anevia says. "Might complain about the lack of excitement."{/n}
{n}"You would complain about the basket."{/n}
{n}"Only if you put something sensible in it."{/n}''', c('[Thank them for the map.]', "leave")),
    n("leave", "Anevia", '''{n}Wenna returns to the covers. Ista puts her book away, then hands Anevia the new sheet.{/n}
"When you can go. There is no date on it."
{n}Anevia accepts it with both hands.{/n}
"I'll try not to improve the route without askin'."
"Ask your companions," {n}Ista says.{/n} "I shall be somewhere else, having a different argument."
{n}On the way back, Irabeth asks to carry the map. Anevia passes it over. For several streets nobody mentions Vald.{/n}
{n}Then Anevia stops at a turning and looks down it. Irabeth waits beside her.{/n}
"Not today," {n}Anevia says at last. She turns back toward you.{/n}
"We've got somewhere we meant to go."''', c('[Walk back with them.]', flags=("three_ista_departure.heard",))),
], requires=("three_lantern_debt.kept", "three_beth_steps.learned"))


s("three_lantern_turn", "The evening she wanted", "Together",
  '\"Are the lanterns ready?\"', [
    n("start", "Anevia", '''"Four lamps. Four birds. No casualties."
{n}Anevia stands beside the yard gate with the yellow sash tied at her waist. Tessa has closed the lane for the evening. The pins are stacked beyond the fence, and the fee board has been turned to its blank side.{/n}
{n}Veska, a gray-haired woman with a fiddle case beneath her arm, is arguing cheerfully with Tessa about how much supper counts as payment. Irabeth has gone to fetch a jug of water.{/n}
"Don't look at the birds too long," {n}Anevia tells you.{/n} "Nell has spies everywhere."
{n}She takes your offered arm before calling for her wife.{/n}''',
      c('[Join them for the evening.]', "coat"),
      c('[Ask to keep the gathering for another evening.]', abort=True)),
    n("coat", "Irabeth", '''{n}Irabeth returns wearing the blue coat. Anevia stops in the middle of untangling a lamp cord.{/n}
"Well."
{n}Irabeth sets down the jug.{/n}
"I bought it."
"Good. Saves me an argument with the owner when I refuse to give it back."
{n}Irabeth comes close enough for Anevia to straighten the collar. Her wife's hands linger against the cloth.{/n}
"You look handsome," {n}Anevia says.{/n} "There. No joke. Very expensive service."
{n}Irabeth kisses her forehead, then the corner of her mouth. Anevia catches her by the lapel before she can draw away.{/n}
"Do that properly."
{n}Irabeth does. Veska examines her fiddle strings with the air of a woman accustomed to waiting for lovers.{/n}''',
      c('[Help Irabeth settle the coat open as you practiced.]', "open", requires=("three_beth_steps.open_coat",)),
      c('[Ask Irabeth to show Anevia how the coat moves.]', "turn", requires=("three_beth_steps.fastened_coat",))),
    n("open", "Narrator", '''{n}You ease the coat clear of its fastening. Irabeth turns toward you, smiling before your hand has left the cloth.{/n}
{n}"Still to your taste?"{/n}
{n}"Very much."{/n}
{n}Anevia looks from her wife to you.{/n}
{n}"Been practicin' that too?"{/n}
{n}"Only the dancing," Irabeth says, then glances at you. "Mostly."{/n}
{n}Anevia laughs and draws you both toward the lamps.{/n}''', c('[Take your places by the cleared lane.]', "first")),
    n("turn", "Narrator", '''{n}Irabeth makes the turn you practiced. The hem of the coat swings neatly around her. Anevia's eyes follow it, then rise to her wife's face.{/n}
{n}"Again."{/n}
{n}"You could join me."{/n}
{n}"I intend to. Wanted a good look first."{/n}
{n}She gives you a sideways smile before taking Irabeth's hand. Irabeth reaches for yours as well, making you part of her satisfaction without rushing her wife past the moment.{/n}''', c('[Take your places by the cleared lane.]', "first")),
    n("first", "Narrator", '''{n}Veska plays a few bars and asks Irabeth if that is the tune she wanted. Irabeth hums a different ending. Veska tries again, quicker this time, and gets an eager nod.{/n}
{n}"I thought we might begin together," Irabeth tells Anevia.{/n}
{n}Anevia looks at the hand offered to her, then puts her own into it.{/n}
{n}"You arranged this."{/n}
{n}"I said I would."{/n}
{n}They walk the first steps. Irabeth gives Anevia time to turn. Her wife comes back into her arms laughing, the yellow sash bright between the dark folds of the coat.{/n}
{n}For the second turn Anevia draws closer. Irabeth misses a beat. Veska repeats the phrase without comment.{/n}
{n}"That was deliberate," Irabeth murmurs.{/n}
{n}"Can't prove it."{/n}
{n}Tessa offers you a cup. From beside the counter you watch Irabeth stop counting and begin smiling at her wife.{/n}''', c('[Enjoy watching them finish their dance.]', "you")),
    n("you", "Anevia", '''{n}The tune ends with Anevia leaning against Irabeth, both of them laughing over a turn neither is willing to claim. Anevia comes to fetch you while Irabeth catches her breath.{/n}
"Your turn. I've been very patient."
{n}She takes the cup from you and places it safely on the counter.{/n}
"Walk with me. Then turn when I give you my hand. If it goes wrong, we blame the music. Veska's already been paid in supper."
"I can hear you," {n}Veska says.{/n}
"Good. Saves explainin' afterward."
{n}The first phrase begins. Anevia keeps her eyes on you rather than the boards, waiting to see how you will move.{/n}''',
      c('[Dance close, keeping the turn small.]', "close", flags=("three_lantern_turn.close",)),
      c('[Give her room for a quick turn and follow her back.]', "quick", flags=("three_lantern_turn.quick",))),
    n("close", "Narrator", '''{n}You stay near enough that Anevia's sleeve brushes yours. She changes her step to match, her teasing expression softening as you turn together.{/n}
{n}"Like this?" she asks.{/n}
{n}You answer by drawing her close on the next phrase. She rests a hand against your shoulder and stops talking.{/n}
{n}Across the lane, Irabeth watches with her cup held forgotten at her waist. Anevia notices and gives her a slow smile before returning her attention to you.{/n}
{n}When the music stops, she remains against you for another breath.{/n}''', c('[Bring her back to Irabeth.]', "beth")),
    n("quick", "Narrator", '''{n}Anevia turns beneath your joined hands. The end of her sash brushes your wrist, and she catches it before it can tangle around your fingers.{/n}
{n}"Didn't think of that complication."{/n}
{n}She tucks the loose end into her belt and tries again. This time the turn brings her neatly back to you. Irabeth applauds from beside the counter.{/n}
{n}Anevia bows to her wife, then pulls you into the next step before Veska can finish the phrase. You recover together, laughing.{/n}
{n}"Could get fond of this," Anevia says. She does not look toward the fiddle.{/n}''', c('[Bring her back to Irabeth.]', "beth")),
    n("beth", "Irabeth", '''{n}Irabeth puts down her cup as you approach.{/n}
"I believe I was promised a turn."
"Several," {n}Anevia says.{/n} "Some of them almost graceful."
{n}She takes her wife's cup and goes to speak to Veska. Irabeth offers you her hand with the confidence of having done it before.{/n}''',
      c('[Lead her as you did in practice.]', "follow", requires=("three_beth_steps.followed",)),
      c('[Follow the step she has learned to give you.]', "lead", requires=("three_beth_steps.led",))),
    n("follow", "Narrator", '''{n}You begin the dance. Irabeth waits for your turn and follows it without correcting either of you. When you change places, she glances toward the edge of the lane.{/n}
{n}"No bench," she says.{/n}
{n}"A considerable advantage."{/n}
{n}Her laugh carries into the next phrase. Anevia leans against the fence watching you both, her hands folded over the yellow sash.{/n}
{n}Irabeth catches her eye, then looks back at you. Her hand tightens briefly around yours before you begin the last turn.{/n}''', c('[Finish the dance with her.]', "supper")),
    n("lead", "Narrator", '''{n}Irabeth begins with a clear, unhurried step. You follow her through the change of places. When the turn ends, she is smiling directly at you.{/n}
{n}"Still on our own feet," she says.{/n}
{n}Anevia calls from beside the fence that this is a modest ambition. Irabeth turns her head just long enough to tell her that she may demonstrate a more difficult one next time.{/n}
{n}Then she draws you back into the dance, watching your face instead of your boots.{/n}''', c('[Finish the dance with her.]', "supper")),
    n("supper", "Narrator", '''{n}Veska sets down the fiddle and demands the rest of her payment. Tessa brings the food from the covered counter: cold meat, pickled roots, and bread bought from Dalia. Anevia admits the last detail before anyone can praise her baking.{/n}
{n}"I arranged an evening," she says. "Didn't attempt a second career."{/n}
{n}Veska describes a wedding where the bride's father kept requesting the same song because he had forgotten its name and refused to admit it. Irabeth laughs with her mouth full and has to turn away. Anevia watches her with open delight.{/n}
{n}When the plates are cleared, Veska plays a slow tune she likes herself. Tessa sits beside her rather than finding something to clean.{/n}
{n}You stand between the wives by the fence. Anevia leans against you; Irabeth's arm rests along the rail behind both of you.{/n}''',
      c('[Ask to see Nell\'s sketch under the lamps.]', "sketch", requires=("three_lantern_debt.shared_sketch",)),
      c('[Stay with them while Veska plays.]', "quiet", forbids=("three_lantern_debt.shared_sketch",))),
    n("sketch", "Anevia", '''"Beth brought it. Wouldn't let me carry it near the pickles."
{n}Irabeth retrieves the rolled paper from its cloth wrapping. Beneath the yellow light, the drawn Anevia watches the living one with the same unfinished smile.{/n}
"What do you think?" {n}Irabeth asks you.{/n}
"You chose the right lamps."
{n}Anevia laughs, then grows quiet as Irabeth holds the sketch beside her face. Her wife's expression makes the next joke unnecessary.{/n}
"Keep it safe," {n}she says.{/n} "I'll do my best with the original."
{n}Irabeth rolls the paper again before kissing her.{/n}''', c('[Stay close while the tune ends.]', "leaving")),
    n("quiet", "Narrator", '''{n}Anevia takes Irabeth's free hand and draws it around her own waist. Irabeth steps closer, bringing you with her. None of you quite faces the same direction, and Anevia has to move her foot to give everyone room.{/n}
{n}"There," she murmurs.{/n}
{n}Irabeth bends her head beside yours. You can feel her smile when Anevia begins humming, gets the tune wrong, and continues with confidence.{/n}
{n}Veska finishes the piece her own way.{/n}''', c('[Thank Veska and Tessa for the evening.]', "leaving")),
    n("leaving", "Irabeth", '''{n}You help extinguish the lamps before taking down the shades. Tessa checks the gate while Veska packs her fiddle. Anevia folds the yellow sash over one arm so it will not trail in the street.{/n}
"Come back to ours," {n}Irabeth says.{/n} "If you have time. I do not want to stop looking at you both yet."
{n}Anevia turns toward her wife, visibly pleased by the directness.{/n}
"Neither do I."
{n}She looks at you before offering her hand.{/n}''',
      c('"I would like that. Let us take the lamps back first."', flags=("three_lantern_turn.home", "three_lantern_turn.kept")),
      c('"I have to leave tonight. Keep another evening for me."', flags=("three_lantern_turn.later", "three_lantern_turn.kept"))),
], requires=("three_ista_departure.heard",))


s("three_open_road", "Where the evening went", "Together",
  '\"I wanted to spend more time with you both.\"', [
    n("start", "Irabeth", '''{n}Irabeth opens the door wearing the blue coat. The room behind her is warm, and the table has been cleared except for the two maps and a small bowl of walnuts.{/n}
"Anevia asked me to wear it again. I did not require much persuasion."
{n}Anevia looks up from the rug beside the hearth.{/n}
"Good coat. Excellent contents. Come in before she starts explainin' the lining."
{n}Irabeth waits for you to enter before closing the door.{/n}''',
      c('[Join them.]', "after_home", requires=("three_lantern_turn.home",)),
      c('[Join them.]', "after_later", requires=("three_lantern_turn.later",)),
      c('[Arrange to return when you can stay.]', abort=True)),
    n("after_home", "Anevia", '''"Last time we had to return the lamps before we could sit down together. Tonight we can begin with the pleasant part."
{n}She moves the bowl within your reach.{/n}
"Nell got everything back. Asked whether the birds had been admired. I said everyone behaved beautifully. Nearly true."
{n}Irabeth sits beside her wife and takes a walnut.{/n}
"I did admire the lamps."
"I was watchin' you admire other things."
{n}Irabeth does not deny it. She offers you the first half of the nut after cracking it.{/n}''', c('[Settle beside them.]', "maps")),
    n("after_later", "Anevia", '''"We kept the evening. As requested. Beth has been complainin' that I wouldn't tell her what else I had planned."
"You said walnuts."
"Accurate so far."
{n}Irabeth sits beside her wife and takes one from the bowl. After cracking it, she offers you the first half.{/n}
"I am willing to discover the rest as we go."
{n}Anevia looks pleased by that answer. She shifts to make room for you on the rug.{/n}''', c('[Settle beside them.]', "maps")),
    n("maps", "Narrator", '''{n}Irabeth unfolds Ista's new sheet beside the first map. Your penciled additions are still where you left them. Anevia smooths a crease with the side of her hand.{/n}
{n}"She began this before we went looking for her book. Kept thinkin' she was thanking us. She was finishing something she already meant to give us."{/n}
{n}"She can be grateful and angry," Irabeth says.{/n}
{n}"I know. Wish she could be grateful and delighted. Would suit my vanity better."{/n}
{n}Irabeth gives her a sidelong look.{/n}
{n}"I believe I married you with that vanity already attached."{/n}
{n}"Read the terms, did you?"{/n}
{n}"Several times. They were unusually entertaining."{/n}''',
      c('[Trace the stopping place before the steep path.]', "steep", requires=("three_ista_departure.both_roads",)),
      c('[Trace the easier road beside the river.]', "river", requires=("three_ista_departure.easy_road",))),
    n("steep", "Irabeth", '''"We decide here. Before carrying the basket uphill."
{n}Anevia taps the rest mark with one finger.{/n}
"Could eat the contents. Reduce the burden."
"Then we would be carrying an empty basket to the view."
"Very practical."
{n}Irabeth puts her hand over Anevia's, leaving both resting beside the little mark.{/n}
"I want to find out which of us changes our mind."
{n}Anevia's smile softens.{/n}
"Might surprise you."''', c('[Leave the choice for that future day.]', "desire")),
    n("river", "Anevia", '''"You chose the easy road. I'm puttin' that in writing before either of us finds a reason to make it difficult."
{n}Irabeth takes the pencil and draws a tiny basket beside the river.{/n}
"There. We have committed ourselves to a scandalous lack of ambition."
"Could be good at it. With practice."
{n}Irabeth sets down the pencil and takes Anevia's hand.{/n}
"I would like the practice."
{n}Anevia turns her hand beneath her wife's until their fingers fit together.{/n}''', c('[Leave the map open for another future day.]', "desire")),
    n("desire", "Irabeth", '''{n}Irabeth moves the walnuts out of the way and turns toward Anevia.{/n}
"I liked dancing with you. I liked seeing you dance with our guest. I have been trying to find a less awkward way to say that."
"That way was fine," {n}Anevia says.{/n}
{n}Her wife touches the yellow sash, laid across the back of the nearby chair.{/n}
"I wanted to bring you home. Both of you. I kept thinking about it while Veska played."
{n}Anevia rises onto her knees and kisses her. Irabeth's arms close around her wife before Anevia draws back far enough to speak.{/n}
"Could have told me on the way. Would've walked faster."
{n}She turns toward you, one hand still resting against Irabeth's chest.{/n}
"What do you want tonight?"''',
      c('[Kiss them both and stay together for the night.]', "night", flags=("three_open_road.night",)),
      c('[Ask for kisses and an unhurried evening, then your own bed.]', "evening", flags=("three_open_road.evening",)),
      c('"I want to stay close and hear you talk. I do not want more tonight."', "company", flags=("three_open_road.company",))),
    n("night", "Narrator", '''{n}You join them on the rug. Anevia meets your kiss eagerly, then draws Irabeth close enough that your hands find the same warm folds of her coat. Irabeth laughs, breathless, when Anevia begins undoing the fastenings with exaggerated care.{/n}
{n}"Bought it, remember?" she says.{/n}
{n}"Doesn't mean I intend to ruin it."{/n}
{n}Irabeth catches her wife's hand and kisses it, then turns toward you. The next kiss leaves very little room for conversation. Anevia rests against both of you, waiting for the moment when Irabeth reaches for her again.{/n}
{n}Later, the coat hangs safely over a chair. The fire is banked and the maps lie folded together. You follow the wives to bed, where Anevia's next joke is lost against Irabeth's mouth.{/n}
{n}In the morning, Irabeth wakes to find you and Anevia watching her. She looks from one to the other, then pulls you both closer before either can explain.{/n}''', c('[Stay until it is time to begin the day.]', flags=("three_open_road.kept",))),
    n("evening", "Narrator", '''{n}Anevia draws you close and kisses you without hurrying. Irabeth brushes a hand along your shoulder, waiting until you turn toward her. Her kiss is warm, and her smile when you part is warmer still.{/n}
{n}You settle together with the wives on either side. Anevia loosens her sash and lays it out of reach of the fire. Irabeth keeps the coat on because her wife asks, rather shamelessly, for the pleasure of looking at her.{/n}
{n}When you rise to leave, Anevia fetches your things. Irabeth walks you to the door and asks when she will see you again. You choose a time before saying goodnight.{/n}
{n}The last thing you see as the door closes is Anevia taking her wife's hand and drawing her back toward the hearth.{/n}''', c('[Keep the next meeting in mind as you leave.]', flags=("three_open_road.kept",))),
    n("company", "Narrator", '''{n}"Then stay here," Irabeth says, making room against her shoulder.{/n}
{n}Anevia sits on her other side with the bowl of walnuts. She insists on returning to Veska's story about the wedding and invents three increasingly implausible names for the song the bride's father wanted.{/n}
{n}Irabeth supplies a fourth. Anevia laughs so hard that she drops a shell and has to fish it out from under the rug. You take the bowl while she searches.{/n}
{n}The fire settles. Irabeth's hand rests over yours; Anevia leans back against her wife when the missing shell has been found. You remain together until the room grows cooler and one of you finally offers to fetch another blanket.{/n}''', c('[Enjoy the rest of the evening together.]', flags=("three_open_road.kept",))),
], requires=("three_lantern_turn.kept",), delay=24)

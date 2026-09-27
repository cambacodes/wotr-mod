"""Authored continuation of Ista's stolen-records story, before the last watch.

All commercial documents, supporting adults and meetings are book-event fiction.
No native quest, currency, inventory, marriage or morale state is changed.
"""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, owner, entry, nodes, requires=(), delay=48):
    SCENES.append(scene(id, title, owner, 3, entry, nodes,
                        requires=("three_open_road.kept", "kept_terms", *requires),
                        forbids=("closed", "loss", "inhuman", "irabeth_away",
                                 "anevia_away", "last_watch"),
                        delay=delay, optional=True, Relationship="tirabade",
                        Areas=[DREZEN], Chapters=[3, 5],
                        ForbidOverrides={"last_watch": "three_progression.catchup_requested"}))


s("three_borrowed_names", "The price of your name", "Together",
  '"You wanted to show me a letter."', [
    n("start", "Anevia", '''"Apparently we're in the carrying trade. Thought you ought to know."
{n}Anevia holds up a folded paper. Irabeth has cleared a place for it, but has not removed the bowl in which the wives keep their loose buttons. Ista and Wenna sit opposite her. Wenna's coat is still fastened. She looks ready to leave before anyone has begun.{/n}
"We asked them to bring this here," Irabeth says. "It concerns our names as well as yours."
{n}Ista pushes the paper across the table.{/n}
"It concerns my wagon. Yours are the names at the bottom."
{n}Beneath a list of goods and charges, someone has written that the Commander's household will guarantee payment. Anevia and Irabeth are named as the people who arranged it. The handwriting is unfamiliar. The impression in the wax resembles an ordinary merchant's mark, a hooked staff within a circle.{/n}
"I didn't sign it," Ista says. "I didn't ask you to promise anything. I want that understood before someone begins offering to pay."''',
      c('"Show me what happened."', "history"),
      c('[Arrange another time to hear them without interruption.]', abort=True)),
    n("history", "Narrator", '''{n}The claim comes from Malven, a freight broker who takes deposits on space in other people's wagons. Ista paid him to reserve such space for a customer. Now he says she also accepted a much larger consignment on credit. The disputed sheet describes deliveries with an unnerving familiarity.{/n}
{n}"He says he bought the undertaking from a collector," Wenna tells you. "He won't name the collector. He is quite willing to mention you."{/n}
{n}Ista points to a small fee in the margin.{/n}
{n}"This part is real. He has my deposit. Everything below it is a different bargain."{/n}
{n}"Can he take your wagon?" Irabeth asks.{/n}
{n}"He can frighten people away from hiring it. He's started. One customer wants their payment back until this is settled. That doesn't require a judge, does it?"{/n}
{n}Anevia reads the description of the first delivery a second time, her thumb still on the line when she looks at you.{/n}''',
      c('[Compare the claim with the records recovered from the thieves.]', "recovered", requires=("three_stolen_roads.followed",)),
      c('[Ask which details could have come from the missing bundle.]', "missing", requires=("three_stolen_roads.book_safe",))),
    n("recovered", "Ista", '''"There. I have the acknowledgment. The customer paid for that load already."
{n}Ista unwraps the recovered bundle. The sheets have been flattened beneath a weight; one bears a wheel's dirty edge. She finds a signature and places it beside the claim. A genuine delivery has been copied into a debt that never existed.{/n}
"So somebody read these before we got them back," Anevia says.
"Or knew the customer. Or worked where I delivered it. I'm tired of finding new people to suspect."
{n}Ista opens her travel book to hold the papers down. The damaged corner catches on her sleeve. She frees it with a care which interrupts the conversation more effectively than a rebuke.{/n}
"I left with the load I planned," she says. "I came back expecting another. Now I'm answering this instead. Getting my papers back helped. It didn't stop whoever copied them."
{n}Irabeth asks permission before lifting the acknowledgment. Ista gives it and sits back, watching all three of you.{/n}''', c('[Keep the original and the false account separate.]', "names")),
    n("missing", "Ista", '''"Two addresses. The cloth weight. A repair I charged for. All in the bundle we didn't get back."
{n}She puts her intact travel book on the table, then closes it again without opening a page.{/n}
"I've spent days asking people to confirm things they already signed once. Some are away. Some think I ought to have kept their first answer. Wenna took the smaller jobs while I went knocking."
"And now," Wenna says, "someone has found a profitable use for our missing paperwork."
{n}Anevia starts to speak. Ista raises a hand.{/n}
"I wanted the book safe too. We chose that. I won't pretend we knew everything that would follow, but you needn't explain the choice to me again. Help me find the people who actually did this."
{n}Irabeth draws a blank sheet toward her.{/n}
"Which customer can we reach without sending anyone out of Drezen? Start there."''', c('[Write down the reachable witnesses.]', "names")),
    n("names", "Anevia", '''"He picked the household business carefully. Nobody has to believe the Commander personally buys wagon covers. Just that somebody close enough might be makin' a little money on the side."
{n}She looks at Irabeth.{/n}
"He's heard we've been helping Ista. Seen us together. That's enough to give the story legs."
"Helping her recover stolen property," Irabeth says.
"I know what we did. I'm tellin' you what he's selling."
{n}Wenna unfastens her coat at last.{/n}
"There is more. He offered to settle privately. Said he understood why you might prefer that. I asked what he meant. He smiled."
{n}Anevia's expression loses its humor.{/n}
"Lazy bastard. Doesn't even have to decide what the secret is. Lets us do the work."
{n}Irabeth rests her hand beside Anevia's on the table, close enough for her wife to take if she wishes. Anevia does, without looking away from Wenna.{/n}''',
      c('"He will not turn our private life into proof of a debt."', "private"),
      c('"The fastest answer is a clear denial from everyone named."', "denial")),
    n("private", "Irabeth", '''"Then we deny the guarantee. Each name, each supposed signature."
{n}Irabeth turns the sheet toward you.{/n}
"I won't deny wanting you at our table to save him explaining this."
{n}Anevia's thumb moves across her wife's knuckles.{/n}
"Make him talk about the money. He'd much rather talk about us."
"And don't pay him to stop," Wenna says. "He'll tell everyone we bought his kindness. I want my wife's account cleared."''', c('[Return to the false guarantee.]', "plan")),
    n("denial", "Anevia", '''"Might be. Though if you shout it from the walls, half the city will ask what they're supposed to have heard."
{n}She lets the sheet fall flat.{/n}
"Let's have something to put beside the denial. Otherwise it's four respectable people and me saying a merchant's a liar."
"Five people," Irabeth says. "You do not have to make his argument for him."
"I'm making ours. He'll do a worse job with mine."
{n}Ista gives a short laugh despite herself.{/n}
"I want him to withdraw the claim in front of the people he told. That would do more good than a speech to people who have never hired me."
{n}You draw those names onto Irabeth's sheet. The list is smaller than the city and therefore something you can actually begin.{/n}''', c('[Work out what each witness can establish.]', "plan")),
    n("plan", "Narrator", '''{n}Irabeth puts the disputed entries on a separate sheet. Ressa, the copyist who has worked for Ista before, may recognize how the list was prepared. Anevia wants Gresa's commission scrap preserved before anyone tells her which mark they hope to find.{/n}
{n}"I am coming to the meeting," Ista says. "You can't settle my account while I wait outside."{/n}
{n}"Bring your customers' names," Irabeth replies. "He will have to correct his story to each of them."{/n}
{n}Wenna takes the original guarantee. Irabeth keeps the copy Ista permits her to make. Anevia has already found her coat by the time they reach the door.{/n}
{n}"Copyist for you, scrap for me?" she asks her wife.{/n}
{n}"And no warning Malven which questions we are bringing."{/n}
{n}"There she is." Anevia brushes a kiss against Irabeth's mouth, then looks at you. "Choose where you want to start."{/n}''', c('[Arrange to follow the two leads.]', flags=("three_borrowed_names.heard",))),
])


s("three_back_of_seal", "The scrap she kept", "Anevia",
  '"Shall we speak to Gresa?"', [
    n("start", "Anevia", '''"She kept it. Under a jar of buttons. Might start using one myself."
{n}Anevia walks beside you toward Gresa's stall, a short pencil tucked behind one ear.{/n}
"She won't lend it. We can look while she's there."
{n}Gresa has cleared half her counter. The rest holds buckles and combs; she goes on selling them while Anevia explains the claim. A customer compares two identical buckles until Anevia turns to you in silent appeal.{/n}
"Not even spies are that careful," she murmurs. "Most pick the expensive one and blame their superiors."''',
      c('[Wait until Gresa can give you her attention.]', "scrap"),
      c('[Ask to return when the stall is less busy.]', abort=True)),
    n("scrap", "Narrator", '''{n}Gresa unwraps a scrap of stout paper. On the front Vald recorded his commission price for the stolen travel book. On the back, beneath an old wax stain, are a few cramped letters. The scrap was cut from a larger commercial form.{/n}
{n}"He didn't get paid," she says. "Before you ask. I don't owe him for carrying stolen things to my counter."{/n}
{n}Anevia recognizes the handwriting from the claim's description of the goods, but will not call it proof. The words are short; the same person might have copied the list for an honest purpose before somebody else forged the guarantee.{/n}
{n}"What about the back?" you ask.{/n}
{n}"Wax hid it when he gave it to me. Flaked off in the jar. I thought it was dirt."{/n}
{n}The old pressure marks cross several newer creases. Gresa permits you to examine the original under the awning's slanting light. Anevia lays a clean sheet nearby for notes, keeping her pencil away from the fragile scrap.{/n}''', c('[Look over the available ways to compare it.]', "method")),
    n("method", "Anevia", '''"Could be another guarantee. See the ruled edge? We need a name, or a complete form somebody can identify."
{n}Gresa has a drawer of purchase notes from the same traders. Sorting it will take most of her remaining afternoon. She will have to close while the papers cover her counter.{/n}
"I'd rather lose an afternoon than have Vald call me his partner," she says. "Still, it is an afternoon."
{n}Anevia turns the scrap. The light catches an indentation, then loses it.{/n}
"Your eyes might do it faster. Don't rub it. I'd like the paper to survive whichever way we try."''',
      c('[Inspect the faint impression beneath the old seal.]', check=dict(Skill="SkillPerception", DC=25, Success="impression", Failure="unreadable", CommanderOnly=True)),
      c('[Help Gresa sort her purchase notes for a complete example.]', "catalogue")),
    n("impression", "Narrator", '''{n}You move the paper closer to the awning's edge. A downstroke emerges beneath the crack in the wax, followed by the shallow curve of a name. The front's ink does not follow those grooves. They belong to the form which was cut apart.{/n}
{n}"Malven," you read. "Received against carriage."{/n}
{n}Anevia bends beside you. Her shoulder rests against yours while she follows the strokes with the blunt end of the pencil, never touching the paper.{/n}
{n}"And the hook in the staff."{/n}
{n}She asks Gresa to look before either of you reads the rest aloud. The stallkeeper recognizes the mark from a receipt she kept. Together you compare the broken rim of the impression. It matches the defect on Malven's receipt.{/n}
{n}This does not explain who forged the household guarantee. It does place a piece of Malven's own paperwork in the hands of the man who sold Ista's stolen book.{/n}
{n}Gresa wraps both papers separately. She agrees to bring them to the meeting herself. Anevia's smile, when she turns back to you, is sharp with pleasure.{/n}''', c('[Record what all three of you saw.]', "after", flags=("three_back_of_seal.impression",))),
    n("unreadable", "Narrator", '''{n}The groove seems to make a letter until you turn the scrap. Then the crease becomes its downstroke and a stain supplies the rest. You try the light from the other side. Whatever was written there will not separate itself from the damage.{/n}
{n}Anevia waits while you make one last attempt, then covers the pencil with her hand.{/n}
{n}"Leave it. We could invent a very convincing name if we keep looking."{/n}
{n}Gresa's next customer arrives. There is no room to spread her whole drawer now; she cannot give you both the examination and the afternoon's sorting. She offers to make a statement about receiving the scrap from Vald, which proves less but is something she actually knows.{/n}
{n}You return the paper without a name to put on its reverse. Anevia asks Gresa to preserve it anyway. Perhaps somebody else can read it later. For the coming meeting, you will have a witness and a suspicion, without the link you hoped to find.{/n}''', c('[Accept Gresa\'s statement without adding a guessed name.]', "after", flags=("three_back_of_seal.unreadable",))),
    n("catalogue", "Narrator", '''{n}Gresa turns her sign and brings out the drawer. You separate paid purchases from offers; Anevia flattens curled corners beneath a row of buckles. Once, a customer rattles the shutter and leaves when Gresa calls that she is closed.{/n}
{n}Near the bottom you find a complete form with the same ruling and stock phrases as the scrap. Malven's name is written on it. So are two other brokers' names on similar forms. They buy their paper from the same supplier.{/n}
{n}"Useful," Anevia says. "Less useful than I'd hoped."{/n}
{n}It establishes how easily an ordinary receipt could have been cut into a commission note. It does not establish whose receipt Vald used. Gresa gives you a copy of the blank form and agrees to explain that distinction at the meeting.{/n}
{n}When you put the drawer back, she counts the afternoon's takings without trying to hide it. Anevia waits until she is done before thanking her. Gresa accepts the thanks, then asks you both to leave the counter clear. She still has an hour in which to sell something.{/n}''', c('[Help return the stock to its place.]', "after", flags=("three_back_of_seal.catalogue",))),
    n("after", "Anevia", '''{n}Outside, Anevia pulls the pencil from behind her ear. It has left a dark mark. You point; she rubs the wrong place, then hands you her handkerchief.{/n}
"Beth usually gets it on the first try. Don't give her anything to boast about."
{n}She stands still while you wipe it away, watching you from very close.{/n}
"I liked having you beside me. Usually I give you a list and watch you leave to do the dangerous part."
{n}A wagon passes. She draws you against the wall with her.{/n}
"We should try this again. Preferably without a merchant's hand in Ista's purse."''',
      c('"I liked watching you work."', "watching"),
      c('"Next time, give me a job before we arrive."', "job")),
    n("watching", "Anevia", '''"I could see you in the glass of the button jar."
{n}Anevia smiles at your expression.{/n}
"Fine view. Very difficult to count lines on a scrap with that going on beside me."
{n}Her gaze moves to your mouth. She takes her time looking up again.{/n}
"Beth would've caught me watching the reflection. Then I'd have had two problems."
{n}She smooths the collar which the wall has turned up, leaving her fingers there until the wagon has passed.{/n}''', c('[Walk with her into the quieter lane.]', "old_work")),
    n("job", "Anevia", '''"Keep track of the question I haven't asked. I get a promising answer and start pulling at it. Beth's usually the one who remembers we came for something else."
"And what will you do?"
"The interesting bits."
{n}She nudges your elbow.{/n}
"Until you catch something I miss. Then I'll try very hard to be gracious."
{n}At the corner she leaves you room to choose the quieter lane toward home.{/n}''', c('[Ask whether she thinks Vald is still in Drezen.]', "old_work")),
    n("old_work", "Anevia", '''"Vald might still be in Drezen. Or he could be congratulatin' himself somewhere else. We know he stole a book. We don't know that he wrote this guarantee."
{n}Her expression tightens.{/n}
"I don't like him. That makes it easy to let him explain everything. Then you stop looking."
{n}She studies the shuttered upper window of a house ahead, then looks away.{/n}
"I could get into Malven's rooms. Find out what he keeps. That's the sort of thing I used to offer Beth before she'd finished telling me what was wrong."
"Are you offering now?"
"Thinking about it. Different thing. He's expecting a meeting about a debt. If he catches me in his room, he gets to talk about that instead."
{n}Anevia turns the pencil between her fingers.{/n}
"Hate giving a fool a good answer. Makes him unbearable."''',
      c('"Keep the meeting. We have witnesses he has to answer."', "return"),
      c('"Save the clever entrance for a door that needs opening."', "door")),
    n("door", "Anevia", '''"Ours sticks when it rains."
{n}She laughs at your expression.{/n}
"What? You offered. Come round with a plane and a few spare hours. Beth will fall in love with you all over again."
{n}Her laughter settles into a smile as you approach the lodging.{/n}
"Actually, don't. She has opinions about who ought to repair it. Says she put the hinge on and she'll put it right. I keep telling her I married her for other qualities."
"Does she believe you?"
"Usually. I can be quite convincing."''', c('[Let her tell Irabeth what you found.]', "return")),
    n("return", "Narrator", '''{n}Irabeth is not home when you arrive. Anevia leaves a short note about Gresa's evidence, then begins a second line, smiles, and folds the page before you can read it.{/n}
{n}"For her," she says, without apology.{/n}
{n}She catches your hand before you turn away.{/n}
{n}"And this is for you."{/n}
{n}Her kiss is quick at first. Then she draws you back, giving the second one more time. When she releases you, the pencil has fallen from her sleeve onto the floor.{/n}
{n}You both look down at it.{/n}
{n}"Pocket," she says. "Don't tell Beth."{/n}''',
      c('[Pick up the pencil and give it back.]', flags=("three_back_of_seal.kept",))),
], requires=("three_borrowed_names.heard",), delay=24)


s("three_beth_account", "Her own account", "Irabeth",
  '"I can come with you to the copyist."', [
    n("start", "Irabeth", '''"Thank you. There is something I would like you to do when we arrive."
{n}Irabeth has changed into the blue coat. Its fastening catches for a moment; she frees it before you can reach to help.{/n}
"Let Ressa finish before we answer. I have been told I can make a question sound like a verdict."
"By Anevia?"
"By several people. Anevia illustrated her complaint. At length."
{n}She gives you a brief imitation of her wife's indignant posture, then straightens with a look of surprise at having done it in the street.{/n}
"You are not to improve that when you tell her."
{n}Ressa's workroom is reached through a repair shop. The copyist, a broad-shouldered woman with silver rings on her ink-stained fingers, offers stools without offering refreshments. She has laid two pages face down on her desk.{/n}''',
      c('[Sit where Ressa indicates.]', "copyist"),
      c('[Ask to return when you can give this your full attention.]', abort=True)),
    n("copyist", "Narrator", '''{n}"I wrote part of it," Ressa says before Irabeth can ask a question. "The descriptions. Malven brought me Ista's delivery details. Said she wanted another copy. I do that work for her sometimes."{/n}
{n}She turns over the first page. It is her work record, listing what she copied and the fee she charged. The second is a practice sheet on which she tried a heading.{/n}
{n}"There was no household guarantee when it left this room. No promise from the Commander. Look at the space beneath the total. I left it for the customer's acknowledgment."{/n}
{n}Irabeth sits very still. Ressa watches her hands.{/n}
{n}"I should have asked Ista. She has sent work through other people before. I believed him because it was ordinary and paid the ordinary rate. That's the extent of my cleverness."{/n}
{n}"May I look?" Irabeth asks.{/n}
{n}The copyist nods. Irabeth draws the work record toward her, leaving Ressa's hands resting on the edge of her own desk.{/n}''', c('[Compare the dates without interrupting her account.]', "history")),
    n("history", "Irabeth", '''"Malven supplied the details. You copied them. The guarantee was added afterward."
"That's what I can swear to. He'll say I'm saving my business."
"Can you show the entry for his payment?"
{n}Ressa taps the open record.{/n}
"Here. But I'm not lending the book. My other customers haven't accused me of anything."
{n}She offers to bring it and show the relevant page herself. Alternatively, she will sign an account for the meeting.{/n}
"I won't have you promise no one will blame me. People who can't tell a bad copy from a good one can still stop buying either."
{n}Irabeth studies the payment mark.{/n}
"I can't promise that. We will begin with his payment. He can hardly claim you invented his money."''',
      c('"Bring the work record. Let him answer the original entries."', "record", flags=("three_beth_account.record",)),
      c('"The signed account is enough. Keep your other customers out of this."', "statement", flags=("three_beth_account.statement",))),
    n("record", "Narrator", '''{n}Ressa binds the unrelated pages with a strip of cloth. She will hold the book and open only the section concerning Ista. Irabeth adds that limit to the invitation and returns it for her signature.{/n}
{n}"When he asks about somebody else's money?" Ressa says.{/n}
{n}"I shall bring him back to his own."{/n}
{n}Ressa signs. As you rise, she asks whether the meeting requires her best coat.{/n}
{n}"The one you can sit in comfortably," Irabeth says. "We may have to listen to a great deal of explanation."{/n}''', c('[Walk back with Irabeth.]', "walk")),
    n("statement", "Narrator", '''{n}Ressa writes while you wait. Irabeth asks her to strike out a sentence claiming Malven planned the forgery from the beginning.{/n}
{n}"You suspect that. So do I. You did not see it."{/n}
{n}"It would sound better."{/n}
{n}"Until he asks how you know."{/n}
{n}Ressa starts a clean sheet. Irabeth reads it aloud when she finishes; Ressa corrects a date, then signs.{/n}
{n}"If he disputes it, you can ask me to come," she says.{/n}
{n}"We will ask."{/n}
{n}Irabeth puts the account into a dry cover before they shake hands.{/n}''', c('[Walk back with Irabeth.]', "walk")),
    n("walk", "Irabeth", '''{n}Anevia is waiting below the copyist's stairs. She hears Irabeth's account, then looks up at the window.{/n}
"Don't lead with her account. Let him tell us where he got the list before he sees what she kept. Otherwise he'll build his collector around her dates."
"I won't have Ressa treated as an accomplice to get him talking," Irabeth says.
"Neither will I. Keep her out of his reach. Just don't feed him her answers."
{n}Irabeth considers it, then nods.{/n}
"Ista's account first. His explanation. Then we show Ressa's evidence. I will stop him wandering into her other work."
"There. Between us we might get him to finish a sentence that means something."
{n}Anevia has a message to collect. She squeezes her wife's hand before going, leaving you to walk back with Irabeth.{/n}
"She used to watch me hesitate at locked doors," Irabeth says. "Then she would open one and ask whether I meant to spend all night admiring the hinges. I would be furious that she had made me laugh."''',
      c('"What did you do when she made you laugh?"', "laugh"),
      c('"She still likes getting past your guard."', "guard")),
    n("laugh", "Irabeth", '''"Tried to look stern. Poorly, by all accounts."
{n}She turns down a quieter passage, waiting for you to follow.{/n}
"Once I told her I would discuss her methods after we were out of danger. She asked whether that was a standing invitation to supper. I had no answer prepared. I think she took that as encouragement."
{n}Irabeth's ears darken.{/n}
"You are smiling in much the same way."
"It sounds like encouragement."
"It was. Eventually I stopped pretending otherwise."
{n}She offers you her free hand. Her grip is warm and a little too firm until she notices and eases it.{/n}
"There. That is an invitation I have managed without a tactical pretext."''', c('[Take the invitation.]', "want")),
    n("guard", "Irabeth", '''"I do leave openings. Occasionally on purpose."
{n}She glances at you to see whether that surprises you.{/n}
"She likes believing she has caught me. Sometimes I let her finish the joke before I tell her I know. Sometimes I want her to finish it."
"And does she know that?"
"Of course. That is what makes it enjoyable."
{n}Irabeth stops beneath a projecting roof, out of the traffic, and offers you her hand.{/n}
"You needn't always wait for her to arrange the surprise."
{n}For a moment the woman looking at you seems very pleased with the difficulty she has caused. Then she laughs at herself and draws you closer.{/n}''', c('[Take her hand.]', "want")),
    n("want", "Irabeth", '''"I asked Tessa about a room for the three of us. Before this business arrived."
{n}Irabeth rests her shoulder against the wall.{/n}
"She lets the upstairs room to visiting relatives. There is a window over the yard. I want an evening there with you both."
"Does Anevia know?"
"That I am planning something. She has been insufferable. I have rather enjoyed making her wait."
{n}Irabeth takes your hand.{/n}
"Will you come and see it?"''',
      c('"Show us the room. I want to see what you chose."', "room", flags=("three_beth_account.room",)),
      c('"An evening away sounds good. Keep the sleeping arrangements for later."', "evening", flags=("three_beth_account.evening",))),
    n("room", "Irabeth", '''{n}Her smile broadens before she can hide it.{/n}
"I have only seen the stairs. Tessa assures me the room is better than the stairs."
"A promising endorsement."
"She also said the bed does not creak. Then asked whether I needed a demonstration."
{n}Irabeth covers her face briefly with her free hand.{/n}
"I told her no so quickly that she laughed all the way to the gate. Anevia will hear about it. I cannot prevent that."
{n}You move closer and kiss the hand when she lowers it. She looks at you, the embarrassment slowly giving way to something warmer.{/n}
"I am still going to ask you both. Even if the bed proves a disappointment."''', c('[Tell her you will keep the evening free.]', "home")),
    n("evening", "Irabeth", '''"Yes. I want the evening either way."
{n}She gives your hand a brief squeeze.{/n}
"There is a window over the yard. I imagined hearing the last players leave and having no reason to go down with them. Perhaps that was the part I wanted most."
"You can still tell Anevia that you planned a great seduction."
{n}Irabeth laughs, startled.{/n}
"She would ask for details. Then improve them."
"Would that be terrible?"
"No," she says after a moment. "It would be rather distracting. I may tell her anyway."''', c('[Keep the evening free.]', "home")),
    n("home", "Narrator", '''{n}At the lodging, Anevia opens the door with a question about the copyist already forming. It stops when she sees the way Irabeth is holding your hand.{/n}
{n}"Well?"{/n}
{n}"Ressa has given us an account," Irabeth says.{/n}
{n}"I meant the other thing."{/n}
{n}"You may be patient about the other thing."{/n}
{n}Anevia steps aside, then catches her wife by the open edge of the blue coat. Irabeth bends willingly to meet her kiss. When they part, Anevia keeps her hand there.{/n}
{n}"How patient?"{/n}
{n}Irabeth looks at you before answering.{/n}
{n}"Until we have dealt with Malven. Then I would like your attention elsewhere."{/n}
{n}"Oh, you'll have it." Anevia lets her in, smiling. "Both of you, by the look of things."{/n}''', c('[Go inside with them.]', flags=("three_beth_account.kept",))),
], requires=("three_borrowed_names.heard",), delay=24)


s("three_counterclaim", "What he can afford to say", "Together",
  '"It is time to meet Malven."', [
    n("start", "Narrator", '''{n}Malven has agreed to meet at Gresa's stall after she closes. He arrives early, a square-faced man with a carefully brushed collar, and begins by asking where the Commander would prefer to sit.{/n}
{n}Ista answers before you do.{/n}
{n}"Where there is a chair. You are discussing my account."{/n}
{n}Wenna sets the disputed guarantee on the counter. Malven gives it a glance and begins an explanation about the difficulty of doing honest business in a city at war. Anevia waits until he takes a breath.{/n}
{n}"Who sold you this undertaking?"{/n}
{n}"A collector. He brought several accounts."{/n}
{n}"Name?"{/n}
{n}"I would have to consult my papers."{/n}
{n}Gresa places a chair at the far end of the counter, forcing him to turn toward Ista if he wants to sit down.{/n}
{n}"You can consult them after we have asked the questions," she says. "I have already moved my stock for you."{/n}''',
      c('[Sit beside the wives and let Ista begin.]', "accounts"),
      c('[Postpone until you can stay for the whole meeting.]', abort=True)),
    n("accounts", "Ista", '''"I paid a deposit for space. I did not buy these goods. I did not promise anyone that the Commander would cover my debts."
"You have influential friends," Malven says. "I could hardly know the limits of the arrangement."
"Then you should have asked."
{n}He turns toward Irabeth.{/n}
"Surely you understand how a misunderstanding might arise. Your position, the assistance you have given her..."
"I am here as a person whose name you used," Irabeth answers. "I did not authorize the guarantee. Neither did my wife. Neither did the Commander. You have our answer."
{n}Anevia folds her hands in her lap. It makes her look almost relaxed, except that you know how still she becomes when she is listening for a lie.{/n}
"Now tell us where the delivery list came from," she says.''',
      c('[Let Ista produce the recovered acknowledgments.]', "paid", requires=("three_stolen_roads.followed",)),
      c('[Let Ista present the confirmations she has gathered.]', "confirmations", requires=("three_stolen_roads.book_safe",))),
    n("paid", "Narrator", '''{n}Ista lays the original paid acknowledgments beside the claim. Malven studies them longer than their short entries require. When he suggests a second delivery, she asks him to name its driver.{/n}
{n}He cannot.{/n}
{n}"You have copied the loads I already carried," she says. "There was no second wagon. You have even copied the repair to the first one."{/n}
{n}Wenna taps the entry for that repair. She did the work; she can describe the torn cover, the thread she used, and the customer who complained about the color before paying.{/n}
{n}Malven stops calling the matter a misunderstanding. He calls it an error made somewhere before the account reached him.{/n}
{n}Anevia glances at you. She has heard the change too.{/n}''', c('[Bring in the copyist\'s account.]', "copyist")),
    n("confirmations", "Narrator", '''{n}Ista has confirmations for two of the deliveries. A third customer is away. She will not pretend the new pages replace every acknowledgment in the stolen bundle.{/n}
{n}Malven reaches for that gap at once. Perhaps the third delivery explains the total, he suggests.{/n}
{n}"Then name the goods," Wenna says.{/n}
{n}He reads the claim back to her.{/n}
{n}"Those are the covers I repaired. You charged them twice. If you think there was another load, describe one thing about it that isn't written on a page stolen from my wife."{/n}
{n}He has nothing to add. It does not recover the missing records or the days Ista spent collecting replacements. It does prevent him from turning their absence into agreement.{/n}
{n}Anevia slides the disputed list back to the middle of the counter.{/n}
{n}"Now the writing," she says.{/n}''', c('[Bring in the copyist\'s account.]', "copyist")),
    n("copyist", "Irabeth", '''"Ressa copied these delivery details at your request. She recorded the payment. There was no household guarantee on the page when she finished."
{n}Malven's eyes move toward the door.{/n}
"A copyist may forget which client brought which work."
"She remembers this one."
{n}Anevia leans forward.{/n}
"You told us a collector brought you the account. Ressa says you brought her the details before that guarantee existed. Maybe there's an explanation that fits both. We'd like to hear it."
{n}Malven smooths a crease in his cuff. His hands remain on the counter afterward, spread flat.{/n}''',
      c('[Let Ressa show the entry she agreed to bring.]', "book", requires=("three_beth_account.record",)),
      c('[Read the signed account Ressa authorized.]', "signed", requires=("three_beth_account.statement",))),
    n("book", "Narrator", '''{n}Ressa opens the cloth binding around her work record. She shows Malven his entry and keeps a hand over the unrelated work beneath it. He recognizes his own payment mark, then asks how often she makes errors.{/n}
{n}"Often enough to write down what I charge," she says. "You counted the fee twice before you gave it to me. I remember that too."{/n}
{n}He begins a question about another customer. Irabeth interrupts.{/n}
{n}"That is outside the account she agreed to show. Ask about your entry."{/n}
{n}Ressa closes the book when he has no such question. She stays on her stool, with the volume in her lap. Malven can dispute her motive, but he cannot make her into a distant name whose answer he supplies himself.{/n}''', c('[Ask Gresa for the evidence she agreed to preserve.]', "evidence")),
    n("signed", "Narrator", '''{n}You read the statement aloud, including the limit Ressa put on what she knows. Malven calls attention to that limit as if he discovered it.{/n}
{n}"She cannot say who wrote the guarantee."{/n}
{n}"Neither can you, apparently," Anevia says. "Yet you were willing to collect on it."{/n}
{n}He asks to question Ressa. Irabeth says the copyist can be approached again if necessary; she will not turn an absent woman into a promise to appear whenever he wishes.{/n}
{n}"Then we cannot settle everything today," he says.{/n}
{n}"We can settle whether you continue claiming that we signed it," Irabeth answers.{/n}
{n}Gresa draws her wrapped scrap from beneath the counter while Malven considers a reply.{/n}''', c('[Ask Gresa for the evidence she agreed to preserve.]', "evidence")),
    n("evidence", "Narrator", '''{n}Gresa describes Vald bringing the stolen book to her stall. She does not claim Malven was with him. She describes the commission note, the paper she kept, and what she allowed you to examine.{/n}
{n}Malven asks whether a stall selling secondhand goods is the best place to establish anyone's honesty. Gresa looks at the chair she lent him.{/n}
{n}"You were quite happy to sit down here."{/n}
{n}Anevia gives him no time to improve the insult.{/n}
{n}"Look at the paper."{/n}''',
      c('[Show the matching damaged seal and the legible name.]', "linked", requires=("three_back_of_seal.impression",)),
      c('[Describe what the damaged scrap could not establish.]', "weak", requires=("three_back_of_seal.unreadable",)),
      c('[Show the complete commercial form without overstating its origin.]', "forms", requires=("three_back_of_seal.catalogue",))),
    n("linked", "Anevia", '''"Your name. Your damaged seal. On the back of a note written by a man selling a stolen book."
{n}She keeps a finger beside the scrap, leaving Malven room to look without touching it.{/n}
"Could be he stole your receipt too. Could be you gave him one. Those are different stories. Which would you like to tell?"
{n}Malven looks at Gresa, then at the complete receipt she has laid beside the scrap. He no longer asks whether she is an honest woman.{/n}
"I have dealt with many couriers."
"Then you won't mind putting this one in writing."
{n}For the first time he offers to return Ista's whole booking deposit as well as withdraw the false claim. Ista does not reach for the offered paper. She looks at Wenna, who gives a small nod, then waits to hear the rest.{/n}
"No admission of fraud," Malven says quickly.
"No silence bought with her money," Irabeth answers.''', c('[Hear Ista\'s terms.]', "terms")),
    n("weak", "Narrator", '''{n}The reverse cannot be read with confidence. You say so. Malven relaxes enough to look almost pleased, until Gresa reminds him that the front was written by the man who brought the stolen book.{/n}
{n}There is still no demonstrated link between Malven's seal and that scrap. He uses the gap to refuse a full refund of Ista's deposit. He offers half, calling the rest payment for booking work already done.{/n}
{n}Anevia asks him to show the work. He promises to produce it later.{/n}
{n}"Of course you will," she says.{/n}
{n}Ista keeps her temper with visible effort. She can challenge the remaining charge, but it will mean another argument with another set of people while she needs to earn a living. The unreadable mark has left him somewhere to stand.{/n}''', c('[Hear Ista\'s terms.]', "terms")),
    n("forms", "Narrator", '''{n}The complete form explains the ruling and stock phrases. Several brokers use it. You say that before Malven can discover it for himself.{/n}
{n}He denies knowing which broker supplied the scrap. Without a legible name or matching impression, you cannot prove otherwise. He offers to return half Ista's deposit while insisting that the rest paid for booking work.{/n}
{n}Gresa folds the form away. An afternoon's sorting has produced a useful limit on the story, but it has not produced the stronger evidence you wanted.{/n}
{n}"You may yet have to account for that fee," Irabeth says.{/n}
{n}"I am always happy to explain my charges."{/n}
{n}Wenna gives a short, humorless laugh. Everyone at the counter has now spent long enough with him to understand it.{/n}''', c('[Hear Ista\'s terms.]', "terms")),
    n("terms", "Ista", '''"You withdraw the debt," Ista says. "You correct it with every customer you approached. By name. We will ask them."
{n}Malven begins to qualify the correction. She taps the list. He agrees.{/n}
"I can take the money he has offered and keep pursuing the rest. Or circulate this through the brokers I know and wait for the deposit while they argue. Neither puts Vald in front of us."
"Circulate it," Anevia says. "Let his next customer ask about the collector before handing over a deposit. He'll keep using that story while it only costs him one awkward meeting."
"And Ista loses another booking," Irabeth says. "Take the refund and the signed withdrawal. Put the money back to work. We can still demand his collector's name."
"We can demand plenty. Doesn't make him answer."
{n}Ista looks from one wife to the other.{/n}
"I know what waiting costs. I can bear it if we take that course. I haven't promised him silence if we take the money, either."
{n}She turns the false guarantee toward you.{/n}
"If I circulate it, your names go with it. Which course will you stand behind?"''',
      c('"Take the offered refund. Keep the withdrawal and the right to pursue the rest."', "settlement", flags=("three_counterclaim.settlement",)),
      c('"Circulate the evidence with our signed denial. We will answer for our names."', "circulate", flags=("three_counterclaim.circulated",))),
    n("settlement", "Narrator", '''{n}Wenna reads the withdrawal twice. She strikes out a line which would have forbidden Ista to discuss the agreement. Malven objects; Ista pushes the pen back toward him and waits.{/n}
{n}He signs without the line.{/n}
{n}Gresa witnesses the correction and keeps a copy because her stall was used in the sale. Malven counts out the refund he offered. No money passes through your hands. Ista gives a receipt naming the deposit, making no admission about the false debt.{/n}
{n}"That leaves the collector," Anevia says.{/n}
{n}"I will consult my papers."{/n}
{n}"You do that."{/n}
{n}She does not block the door when he leaves. She watches him all the way to the turning.{/n}''',
      c('[Let Ista count the full returned deposit.]', "full", requires=("three_back_of_seal.impression",)),
      c('[Let Ista record the unpaid half beside the refund.]', "partial", requires=("three_back_of_seal.unreadable",)),
      c('[Let Ista record the unpaid half beside the refund.]', "partial", requires=("three_back_of_seal.catalogue",))),
    n("full", "Ista", '''"All of it."
{n}She pushes the coins into her purse without smiling.{/n}
"I would rather have had the booking I paid for. But I can book elsewhere now."
{n}Wenna folds the withdrawal and puts it beside the purse.{/n}
"Keep that where you can find it."
"I will."
{n}Their hands meet briefly over the fastening. Anevia turns back from the door in time to see it.{/n}''', c('[Help them collect their papers.]', "leave", flags=("three_counterclaim.refunded",))),
    n("partial", "Ista", '''"Half. I can hear him congratulating himself from here."
{n}She counts it again, then writes the unpaid amount on her own account.{/n}
"Wenna has work. We can manage the next booking, but it will be smaller. If I pursue him for the rest, I lose more time. If I don't, he keeps it."
{n}Wenna puts a hand on the back of her chair.{/n}
"We can decide tomorrow. Tonight we know which account is ours."{/n}
{n}Ista folds the withdrawal slowly, pressing each crease with her thumb.{/n}''', c('[Help them collect their papers.]', "leave", flags=("three_counterclaim.partial",))),
    n("circulate", "Narrator", '''{n}Malven withdraws his offer of immediate repayment. Ista looks at Wenna before accepting that cost. They will have to postpone a booking while the deposit remains in dispute.{/n}
{n}He still signs the denial of the household guarantee. You keep your own statement narrow: you did not authorize it, promise payment, or offer favors to customers. Irabeth and Anevia sign separately beneath their own denials.{/n}
{n}Ista will send copies through the brokers she already knows. She will include the witness accounts their authors authorized, without claiming an arrest, a judgment, or proof of who forged the final lines.{/n}
{n}Malven leaves before the copying begins. Anevia watches him go, then sits down beside Irabeth and asks for a clean sheet.{/n}
{n}"We ought to make it legible," she says. "Wouldn't want to give Ressa more work fixing our spelling."{/n}''', c('[Sign your own account of the meeting.]', "leave", flags=("three_counterclaim.unpaid",))),
    n("leave", "Narrator", '''{n}Outside, Irabeth follows Anevia's gaze down the lane.{/n}
{n}"Are you going after him?"{/n}
{n}"He'll expect it. Let him keep looking over his shoulder tonight."{/n}
{n}Anevia waits until Malven disappears around the turning.{/n}
{n}"Tomorrow, I want to know who else he's offered that collector story to."{/n}
{n}"Ask before he has time to prepare them," Irabeth says.{/n}
{n}They take the lane toward home. Anevia is still watching the turning when her wife reaches for her hand. She catches it without looking, then reaches back for yours.{/n}''', c('[Go back with them.]', flags=("three_counterclaim.kept",))),
], requires=("three_back_of_seal.kept", "three_beth_account.kept"))


s("three_unposted_notice", "Who gets to hear it", "Together",
  '"Have Ista and Wenna heard anything since the meeting?"', [
    n("start", "Irabeth", '''"Enough to tell us themselves. They asked to stop here before returning to work."
{n}Ista is standing by the table with a cup she has not drunk from. Wenna sits with one boot off, examining a stone that has worked its way through a split in the sole.{/n}
"I was going to mend that," Ista says.
"You were going to do several things. This one I can do sitting down."
{n}Anevia slides a scrap of leather across the table. Wenna accepts it with a nod and turns her attention to the boot.{/n}
"The customers?" Irabeth asks.
"He spoke to them. Two have told me so. One asked whether we were all friends again."
{n}Ista finally drinks.{/n}
"I said we were discussing carriage, which seems to be a subject everyone is determined to forget."''',
      c('[Ask how the settlement has affected their next work.]', "outcome"),
      c('[Arrange a better time for the visit.]', abort=True)),
    n("outcome", "Narrator", '''{n}The written withdrawal has helped with the people Malven approached. It has not made them forget the dispute. Ista has had to show the page more than once, and Wenna has begun carrying a copy so that answering questions does not consume both their days.{/n}
{n}Anevia asks whether Vald has been seen. Neither woman has heard anything she trusts.{/n}
{n}"If someone tells me he has a brown coat," Ista says, "I ask what else. Drezen has quite a few brown coats."{/n}
{n}"Split tooth," Anevia murmurs.{/n}
{n}"Yes. I remembered."{/n}
{n}Anevia looks down at her cup and lets Ista continue.{/n}''',
      c('[Hear what the returned deposit made possible.]', "refund", requires=("three_counterclaim.refunded",)),
      c('[Hear how they are working around the unpaid half.]', "half", requires=("three_counterclaim.partial",)),
      c('[Hear what circulating the accounts has cost and changed.]', "public", requires=("three_counterclaim.unpaid",))),
    n("refund", "Ista", '''"We booked with someone else. Smaller fee, worse departure hour. Wenna says she can survive getting up early if it keeps Malven out of the room."
"I said I could survive it once."
{n}Ista smiles at her wife.{/n}
"The deposit is back in work. I won't call that justice, but it is useful. One customer asked why Malven returned the whole amount if he had done nothing wrong. I told her to ask him."
{n}Anevia laughs into her cup.{/n}
"Good answer."
"I thought so."
{n}Wenna pulls the boot on and stamps once, testing the patch. The sound has the satisfying finality which the larger business still lacks.{/n}''', c('[Ask about the next journey.]', "records")),
    n("half", "Ista", '''"A smaller load. Wenna has two repairs to finish before we can pay for the rest of the space. We're still asking for the unpaid half."
{n}Anevia begins to answer. Ista stops her.{/n}
"Tomorrow. Please. I want to finish this tea without him in it."
{n}Anevia pushes the jug closer.{/n}
"One customer came back," Ista continues. "The one who wanted their payment returned. They saw the withdrawal."
"I would still have preferred the money," Wenna says, testing her repaired boot.
"So would I."
{n}Ista brushes a fleck of leather from her wife's sleeve.{/n}''', c('[Ask about the next journey.]', "records")),
    n("public", "Ista", '''"Two brokers answered. One wants to see the originals before dealing with him again. The other asked whether I could carry a smaller load. We have not been repaid."
{n}She sets down the cup.{/n}
"The warning is doing something. The lost booking did something too. Wenna has taken repairs while we wait. I knew that was the choice. I still dislike living through it."
{n}Irabeth nods without trying to make the result sound larger.{/n}
"Has anyone challenged the accounts?"
"Malven says we arranged the whole thing to ruin him. A merchant who read your denial asked him whether that explained his using your names before anyone complained. I wish I'd been there."
{n}Anevia's smile returns.{/n}
"So do I."
"Don't smile too much. He has my deposit."''', c('[Ask about the next journey.]', "records")),
    n("records", "Narrator", '''{n}Ista takes out the list for her next load. She has added a second copy, kept separately, and gives Wenna the duplicate before putting her own away.{/n}''',
      c('[Ask whether the recovered bundle is safely stored.]', "saved", requires=("three_stolen_roads.followed",)),
      c('[Ask whether the last missing acknowledgment has been replaced.]', "lost", requires=("three_stolen_roads.book_safe",))),
    n("saved", "Ista", '''"Yes. In a different box from the travel book. I should have done that before."
{n}Her fingers rest for a moment on the damaged book's cover.{/n}
"I tried to write the missing line again. It wasn't the same. Wenna remembered another part of the day, so I put that beside the gap."
"I remembered that we were hungry," Wenna says.
"You remember that about most days."
"You keep planning walks across them."
{n}Ista laughs, then closes the book carefully. The gap remains. It now has a second account beside it, in Wenna's heavier handwriting.{/n}''', c('[Wish them a better journey.]', "names")),
    n("lost", "Ista", '''"Not yet. The customer is still away. I have to explain the gap every time somebody asks."
{n}Ista touches the intact travel book through its wrapping, then checks the fastening of her bag.{/n}
"At least this one can come on the journey."
{n}Wenna puts the duplicate load list inside her own coat.{/n}
"Separate copies. Separate pockets. Very dull people to rob."
"I hope so. I have other uses for excitement."
{n}Ista looks at her wife. Wenna answers with a smile she has not offered anyone else in the room.{/n}''', c('[Wish them a better journey.]', "names")),
    n("names", "Anevia", '''{n}After Ista and Wenna leave, Anevia picks up a scrap which has fallen beneath their chairs. It is only the paper wrapped around Wenna's boot patch. She checks both sides anyway.{/n}
"We're going to be looking at the back of every shopping list for a month."
{n}Irabeth gathers the cups.{/n}
"Tessa asked whether we still wanted to see the room. I said yes."
"Good."
"She also asked who was coming. I said the three of us. Then she asked whether to put out the narrow bed as well."
{n}Anevia's smile turns slow.{/n}
"What did you say?"
"That we would tell her after we had seen it. She knows us well enough to ask. I would like her to know why I am bringing you both. If you want that too."
{n}Anevia lays the scrap down.{/n}
"I'd like one person to hear it because we chose to say it. Someone who isn't trying to put a price on the answer."''',
      c('"Tell Tessa we are lovers. She can hear it from all three of us."', "named", flags=("three_unposted_notice.named",)),
      c('"Let us keep the explanation between ourselves. She can still welcome all three."', "private", flags=("three_unposted_notice.private",))),
    n("named", "Irabeth", '''"Then I will."
{n}She sets the last cup down before looking at Anevia.{/n}
"I am likely to make it sound like a formal announcement."
"I'll put my hand somewhere distracting."
"That may not improve it."
"Depends what we're improving."
{n}Irabeth laughs, and Anevia reaches for her as promised, though only to take her hand.{/n}
"You say it," Anevia tells her. "I want to hear you."
{n}The request leaves Irabeth quiet. She looks from her wife to you and then down at their joined hands.{/n}
"I have been looking forward to this," she admits. "I thought I was looking forward to the room."
"Could be both," Anevia says. "Tessa will charge us either way."''', c('[Keep the appointment with Tessa.]', "arrange")),
    n("private", "Anevia", '''"All right. We can enjoy her room without handing over an account of what we'll do in it."
{n}Irabeth nods, then gives a rueful smile.{/n}
"I had begun composing a sentence. It was becoming rather elaborate."
"Save it for us. I want to hear it."
{n}Anevia takes her wife's hand and waits. Irabeth looks at you, then back at her.{/n}
"I wanted to say that I am happy you are coming with me. Both of you."
"Much better than elaborate."
{n}She kisses Irabeth's fingers. Her wife bends to kiss her mouth, and Anevia makes a pleased sound before drawing you close enough to share the warmth between them.{/n}
"There," she says. "Tessa can put that on the bill as three troublesome guests."''', c('[Keep the appointment with Tessa.]', "arrange")),
    n("arrange", "Narrator", '''{n}You choose an evening after the wives' work is done. Anevia insists that Irabeth leave her papers at home, then admits she will need somewhere to put her own. Irabeth points at the drawer without comment.{/n}
{n}"Cruel woman," Anevia says.{/n}
{n}The words are accompanied by a kiss beneath her wife's ear. Irabeth catches Anevia's hand against her waist and keeps it there while she speaks to you.{/n}
{n}"Come a little early. I want to walk there together."{/n}
{n}"Before she finds a reason to inspect the hinges," Anevia adds.{/n}
{n}Irabeth turns her head enough to answer her wife directly.{/n}
{n}"You have been waiting to discover what I planned. You can spend another hour wondering."{/n}
{n}Anevia looks delighted.{/n}''', c('[Arrange to arrive early.]', flags=("three_unposted_notice.kept",))),
], requires=("three_counterclaim.kept",))


s("three_rooms_unlocked", "The room she chose", "Together",
  '"Shall we go to Tessa\'s?"', [
    n("start", "Narrator", '''{n}Anevia is waiting outside when you arrive. Her yellow sash is folded over her arm. She tells you she has left her notes in the drawer, then looks back toward the door to make sure Irabeth is close enough to hear.{/n}
{n}Irabeth emerges without a bundle beneath either arm. She locks the door, tests it once, and puts the key away.{/n}
{n}"Ready?"{/n}
{n}Anevia slips her hand through her wife's arm. Irabeth offers the other to you. For the first few steps you have to adjust to the width of the lane; then you find a way to walk together without continually apologizing to passersby.{/n}
{n}At Tessa's yard the last players are putting the pins away. She leads you upstairs carrying a lamp and pauses beside the landing window.{/n}
{n}"Before I show you the extravagant accommodations," she says, "there are two things to know. The roof is sound. The washstand leans if you put a boot on it."{/n}''',
      c('[Follow her upstairs.]', "welcome"),
      c('[Arrange to visit on another evening.]', abort=True)),
    n("welcome", "Narrator", '''{n}Tessa opens the room. There is a wide bed, a narrow one beneath a folded cover, and three chairs which have plainly come from different rooms. A small table stands by the window overlooking the now-empty yard.{/n}
{n}Irabeth looks at the beds and then at Tessa. Anevia looks at Irabeth, enjoying herself immensely.{/n}
{n}"I thought you might prefer to decide without me standing over you," Tessa says. "The narrow one can stay where it is. Nobody charges by how many beds you fail to use."{/n}
{n}She sets the lamp on the table.{/n}''',
      c('[Stand beside Irabeth while she tells Tessa.]', "told", requires=("three_unposted_notice.named",)),
      c('[Thank Tessa for making room for all three guests.]', "untold", requires=("three_unposted_notice.private",))),
    n("told", "Irabeth", '''"We are here together. As lovers. I wanted you to hear it from us."
{n}Anevia's teasing expression stills. She puts her hand into her wife's, openly, and reaches for yours.{/n}
"Yes," she says.
{n}Tessa looks at each of you. Then she nods toward the mismatched chairs.{/n}
"Well, I hope you like one another enough to decide who gets the comfortable one."
{n}Irabeth laughs with a relief that makes Anevia squeeze her hand.{/n}
"And nobody gets to ask you for favors on my stairs," Tessa adds. "I won't have people loitering there because they think they can catch a guest on the way to bed."
"I may never leave," Anevia says.
"Then you'll be paying by the week."
{n}Tessa wishes you a good evening and leaves. Irabeth continues looking at the closed door until her wife turns her gently away from it.{/n}''', c('[Let the three of you have the room.]', "chosen")),
    n("untold", "Narrator", '''{n}Tessa takes the thanks as it is offered. She shows you where the clean water is and which window fastening needs a firm hand. Irabeth listens with the concentration she gives useful instructions.{/n}
{n}"I won't have people waiting on the stairs to ask favors," Tessa says. "If someone wants the Commander, they can use the ordinary arrangements."{/n}
{n}"And if someone wants us?" Anevia asks.{/n}
{n}"Same stairs."{/n}
{n}Anevia grins. Tessa leaves the lamp and closes the door behind her, without asking what relationship the chairs, beds, or guests have to one another.{/n}
{n}Irabeth tries the window fastening exactly as instructed. It opens. She looks so pleased that Anevia crosses the room to kiss her before she can report the success.{/n}''', c('[Let the three of you have the room.]', "chosen")),
    n("chosen", "Anevia", '''"You chose well."
{n}Irabeth looks around as if she might have missed some grave defect.{/n}
"You have hardly seen it."
"I've seen you in it. Promising start."
{n}Anevia lays the yellow sash across the narrow bed. Then she takes her wife's hands and draws her close.{/n}
"Were you nervous?"
"Yes."
"Good. I'd hate to think I was losing my touch."
{n}Irabeth kisses her before the next joke can arrive. Anevia's hands rise to the blue coat, pulling her closer. For a little while you can hear someone stacking bowls downstairs and the scrape of the last gate fastening outside.{/n}
{n}When the wives part, Irabeth looks at you over Anevia's shoulder.{/n}
"Come here. I have been imagining this part all day."''',
      c('[Join them and kiss Irabeth, then Anevia.]', "kisses"),
      c('[Join them, taking a hand from each woman.]', "hands")),
    n("kisses", "Narrator", '''{n}Irabeth meets you halfway. Her kiss is eager, almost impatient, and Anevia laughs softly against her shoulder before turning your face toward her own.{/n}
{n}"My turn."{/n}
{n}You kiss her with Irabeth's arm still warm around you. Anevia's hand slides to the back of your neck. When she releases you, she keeps her forehead against yours long enough to catch her breath.{/n}
{n}"We ought to sit down before Beth starts worrying about the furniture."{/n}
{n}"I am not worrying about the furniture."{/n}
{n}"Then stop looking at the chairs."{/n}
{n}"I was deciding where I wanted you."{/n}
{n}Anevia's delighted silence lasts just long enough for Irabeth to enjoy it.{/n}''', c('[Let Irabeth choose a seat beside the window.]', "sitting")),
    n("hands", "Narrator", '''{n}Irabeth's hand closes around yours. Anevia leans against her wife, drawing you with her until the three of you stand close enough that the blue coat brushes your arm.{/n}
{n}"We should sit," Irabeth says.{/n}
{n}"You only brought us here to demonstrate the chairs."{/n}
{n}"I brought you here because I wanted an evening with you."{/n}
{n}Anevia lifts her wife's hand and kisses it. The teasing leaves her expression for a moment.{/n}
{n}"You've got one."{/n}
{n}You help move the chairs toward the window. The comfortable one turns out to be too low for Irabeth, who chooses another with a look which dares Anevia to make that an argument.{/n}
{n}Anevia sits down smiling.{/n}''', c('[Settle beside the window.]', "sitting")),
    n("sitting", "Irabeth", '''{n}Irabeth settles beside the window and rests a hand on Anevia's knee.{/n}
"Stay there."
"Wasn't goin' anywhere. Unless you've forgotten supper."
"A covered tray downstairs. We can fetch it when we want it."
"A woman of foresight. I should marry you."
{n}Irabeth gives her a long look.{/n}
"I have quite enough difficulty getting the wife I have to sit still while I admire her."
{n}Anevia stops moving. She tilts her head, playful at first, then quieter as Irabeth continues looking.{/n}
"Better?"
"Very."''',
      c('[Stay with Anevia while Irabeth fetches the tray she arranged.]', "anevia"),
      c('[Help Irabeth carry the tray upstairs.]', "beth")),
    n("anevia", "Anevia", '''{n}When Irabeth has gone, Anevia draws her feet beneath her chair and looks after her.{/n}
"She's enjoying herself."
"So are you."
"Was it obvious?"
{n}Her smile makes the question absurd.{/n}
"I like being wanted by her. After all this time, I still like catching her at it. And I like what happens to her face when she sees you looking back."
{n}She turns toward you fully.{/n}
"That used to frighten me more than I let on. Not tonight. Tonight I'm wondering how long she's going to spend arranging the tray."
{n}From the stairs comes Irabeth's careful warning that one bowl is hot. Anevia rises at once to open the door.{/n}
"There she is. Don't tell her I missed her. Very bad for discipline."''', c('[Help make room for the tray.]', "meal")),
    n("beth", "Irabeth", '''{n}On the stairs, Irabeth gives you the cups and carries the tray herself. She pauses on the landing, listening to Anevia humming through the open door.{/n}
"I hoped she would do that."
"Hum?"
"Forget to listen for everyone else. Just for a little while."
{n}She looks at you, then gives a small, self-conscious laugh.{/n}
"I also hoped you would look at me the way you did when we arrived. That part was entirely for myself."
{n}You tell her you have not stopped. The flush which follows is worth the delay on the stairs.{/n}
"Good," she says, very quietly.
{n}Then the hot bowl shifts on the tray and both of you have to pay attention to something less pleasant. Anevia reaches the doorway in time to rescue the cups and laugh at your account of the danger.{/n}''', c('[Set the tray where all three can reach.]', "meal")),
    n("meal", "Narrator", '''{n}The food is simple and still warm. Anevia claims the crispiest piece from the edge of the dish; Irabeth admits that she asked Tessa to leave that part uncovered. Her wife looks at her as though she has made a much grander declaration.{/n}
{n}For a while the talk wanders. Anevia describes Gresa's patient buckle buyer. Irabeth repeats Ressa's advice about keeping payment records, then catches herself and changes the subject before the commercial dispute can reclaim the room.{/n}
{n}"Tell me somewhere you want to go," she asks you. "An actual place. Something you would be disappointed to miss."{/n}
{n}You name one. The wives ask questions, disagree about the best season, and begin arguing over whether Anevia would pack enough dry clothes. She defends herself with several examples which fail to convince Irabeth.{/n}
{n}Eventually the dishes are empty. You carry them downstairs together. When you return, the lamp has burned lower and the wide bed's cover catches a little light from the window.{/n}''', c('[Close the door behind you.]', "late")),
    n("late", "Irabeth", '''{n}Irabeth closes the window and turns toward you both.{/n}
"I don't want to rush the end."
"Then don't," Anevia says.
{n}She loosens the yellow sash where she has retied it at her waist and lays it over a chair. Irabeth watches the movement, then looks toward you with no attempt to conceal what she wants.{/n}
"We can stay here. Or walk back slowly. I have had the evening I wanted."
{n}Anevia goes to her wife, resting a hand against the blue coat.{/n}
"I'm inclined to stay. But I can be tempted by a walk if the company is good."
{n}They wait for your answer together.{/n}''',
      c('[Stay for a night of shared intimacy.]', "night", flags=("three_rooms_unlocked.night",)),
      c('[Stay close together and sleep, without taking the evening further.]', "rest", flags=("three_rooms_unlocked.rest",)),
      c('[Ask for a walk home together before returning to your own bed.]', "walk", flags=("three_rooms_unlocked.walk",))),
    n("night", "Narrator", '''{n}You come close enough to answer with a kiss. Irabeth's arm draws you in; Anevia presses against her other side, her smile warm against her wife's cheek.{/n}
{n}This time Irabeth removes the blue coat herself. She hangs it over the back of a chair and turns to find you both watching. For once she makes no attempt to disguise how much she enjoys the attention.{/n}
{n}"Come here," she says again.{/n}
{n}Anevia does. You follow, and the next little while belongs to hands finding familiar warmth, interrupted kisses, and laughter when the bed gives one unmistakable complaint.{/n}
{n}"Subtle," Anevia whispers.{/n}
{n}Irabeth kisses the rest of her objection away. The lamp is lowered before you join them beneath the cover.{/n}
{n}Morning finds the blue coat beneath Anevia's hand where it hangs from the chair. Half asleep, she had reached for Irabeth and caught a sleeve instead. Her wife frees the cloth, takes Anevia's hand, and settles closer to you both.{/n}''', c('[Stay until all three are ready to rise.]', "morning")),
    n("rest", "Narrator", '''{n}Anevia retrieves the extra blanket from the narrow bed. Irabeth moves the chairs out of the way, then realizes she is still arranging the room and sits down with a laugh at herself.{/n}
{n}"Come to bed," her wife tells her. "You've done enough commanding for one evening."{/n}
{n}You settle together beneath the blankets. At first the unfamiliar mattress keeps everyone awake; then Anevia complains about a cold foot and Irabeth admits ownership with such solemnity that you all begin laughing again.{/n}
{n}The talk dwindles. There is a question about breakfast, a half-finished answer, and Anevia's hand finding yours in the dark.{/n}
{n}You wake before either wife. Irabeth lies facing Anevia, who has tucked her nose into the warm hollow beneath her wife's chin. When you move, Irabeth opens her eyes and smiles at you without lifting her head. There is nowhere any of you must hurry for the next few minutes.{/n}''', c('[Enjoy the quiet before rising.]', "morning")),
    n("walk", "Narrator", '''{n}Irabeth straightens the blue coat and leaves it open because Anevia asks. You return the key to Tessa, who accepts it without inspecting anyone's expression for an explanation.{/n}
{n}Outside, the cooler air makes Anevia tuck her hand firmly into her wife's arm. She offers you the other side. You take a longer lane toward their lodging, passing windows whose lamps have already been put out.{/n}
{n}At the door, Irabeth kisses you goodnight if you lean toward her. Anevia waits for her own turn, then steals one more kiss from her wife before letting her find the key.{/n}
{n}"We should do that again," Irabeth says.{/n}
{n}"You can ask us properly tomorrow," Anevia tells her. "Give yourself something to look forward to."{/n}
{n}They wait until you have turned toward your own quarters before going inside together. The door closes easily. Irabeth has finally repaired the hinge.{/n}''', c('[Return to your own bed with the evening to remember.]', flags=("three_rooms_unlocked.kept",))),
    n("morning", "Narrator", '''{n}You leave the room as you found it, apart from the beds and a chair which Anevia insists was crooked before she touched it. Irabeth takes the key downstairs. Tessa asks whether the washstand survived and receives a reassuring report.{/n}
{n}On the way back, Anevia puts her hand into yours while Irabeth walks at her other side. The city has begun work. A cart needs the lane; you separate to let it pass and find each other again beyond it.{/n}
{n}"Again?" Irabeth asks.{/n}
{n}Anevia looks up at her.{/n}
{n}"You haven't even taken us home yet."{/n}
{n}"I would like to know."{/n}
{n}You answer her together. Irabeth looks pleased all the way to the door, which opens without sticking. She admits, under Anevia's persistent questioning, that she repaired the hinge before you left the previous evening.{/n}
{n}"Show-off," Anevia says, and kisses her.{/n}''', c('[Begin the day after an evening you chose together.]', flags=("three_rooms_unlocked.kept",))),
], requires=("three_unposted_notice.kept",), delay=24)

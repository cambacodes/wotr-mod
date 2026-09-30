"""Authored Chapter 3 courtship after the native Wintersun resolution.

Local contact only. No cure, resurrection, native quest mutation or placed props.
"""
from story_format import c, n, scene

UNIT = "3ba3a0ff8575be8419159221177c1411"
AREA = "0a5654e7dc18f074d9356009d55eb51b"
ANSWER_LIST = "2063ee21356b772408f5c9cfb3ed5bd0"
ETUDES = {
    "gesmerha.dead": "49839ba15f34bee469c4f093dace0811",
    "gesmerha.truth": "1fd9e6e1b5440ac469d5466a9b3d6814",
    "gesmerha.illusions": "23a7a6020a500004daa8e2c2f47b75a2",
    "gesmerha.marhevok_rules": "baa4820ac052d664bbaa261d17ce9b08",
}
COMPLETED_QUESTS = {"gesmerha.wintersun_resolved": "c0d0b565f4b725241b96c148000f1910"}
RELATIONSHIP = dict(
    Title="What the wood will bear",
    Description="Gesmerha has work of her own in mind. She has invited me to return to her bench in Wintersun.",
    Objective="Visit Gesmerha in Wintersun",
    Guidance="After resolving Wintersun and reporting to Irabeth, speak to Gesmerha at her native trading dialogue. Return between visits while she remains available in Chapter 3.",
    StartedFlag="gesmerha.started", ClosedFlag="gesmerha.closed", CommittedFlag="gesmerha.committed",
    UnavailableFlags=["gesmerha.dead"], FailureFlags=[],
)
SCENES = []


def s(id, title, entry, nodes, requires=(), delay=24):
    for page in nodes:
        page["Portrait"] = "Gesmerha"
    SCENES.append(scene(
        "gesmerha." + id, title, "Gesmerha", 3, entry, nodes,
        Relationship="gesmerha", Chapters=[3], last=3, Areas=[AREA],
        AnswerLists=[ANSWER_LIST], ContactUnit=UNIT,
        RequiresAny=["gesmerha.truth", "gesmerha.illusions"],
        requires=("gesmerha.wintersun_resolved", *requires),
        forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil"),
        delay=delay, optional=True))


s("unbought_work", "Something you have not ordered", '"Are you working on something of your own?"', [
    n("start", "Gesmerha", '''{n}Gesmerha has tucked a coil of dark hair into the back of her collar. One strand has escaped. She blows it away from her mouth without taking either hand from the piece of wood before her.{/n}
"Yes. And if you tell me what it ought to be, it will cease to be mine."
{n}The block has no recognizable shape yet. Two shallow channels follow a pale line through its middle. Beside it lie a folded cloth, a knife, and a cup with a broken handle. Each has its place within easy reach of her hand.{/n}
"You are allowed to ask," she adds. "I have had three people tell me today that it would make an excellent box. A fourth wanted a box and thought that amounted to the same thing."
"Would it?"
"Possibly. I have not forgiven the fourth person yet."
{n}She sets the knife down with its handle toward her. Only then does she turn to you.{/n}''',
      c('"Then I will ask. What do you want to make?"', "history"),
      c('"Another time. I will leave you your afternoon."', abort=True)),
    n("history", "Gesmerha", '''"Something people will hold before they ask what it means. I am tired of meanings arriving first."
{n}Her thumb rests in one of the unfinished channels. From the village comes the hard, irregular sound of someone chopping kindling. She waits for the blows to stop before continuing.{/n}''',
      c('"Has it been difficult to find time since the truth came out?"', "truth", requires=("gesmerha.truth",)),
      c('"And with the enchantment still over the village?"', "illusion", requires=("gesmerha.illusions",), forbids=("gesmerha.truth",))),
    n("truth", "Gesmerha", '''"Time is not the worst of it. Someone brings me a bowl and remembers who sat beside them while they ate. Another brings a stool and cannot bear the sound it makes on the floor. They ask whether I can change those things."
"Can you?"
"A bowl, sometimes. A stool, certainly. What they remember, no."
{n}She runs a nail along the end grain, dislodging a pale fleck.{/n}
"I have not taken every commission. A woman wanted her father's drinking cup reduced to shavings. I told her to put it away for a week. If she still wants shavings, any hatchet will serve. She need not pay for mine."
"And your own work waits?"
"My own work is here. I have become very good at defending this little piece of bench."
{n}She taps it once, claiming the space with a dry smile.{/n}''', c('[Ask about the demands on that space.]', "office")),
    n("illusion", "Gesmerha", '''"The enchantment has made certainty cheap. A visitor arrives, everyone sees what they expect, and a warning sounds like bad manners. I know what we agreed to preserve. I still have to live with it."
"Do you regret it?"
"Ask me on a different morning and you may receive a different answer. People sleep. People laugh. Those things matter to me. So does what they would say if they knew."
{n}She draws her hand away from the unfinished channels.{/n}
"I can tell you which side of this block is rough. I cannot give you so simple an account of the village. Do not commission one."
"I came to ask about the carving."
"Then you have chosen a better subject than most of my visitors."
{n}The chopping starts again. She waits until the next blow has fallen before lifting her voice.{/n}''', c('[Ask about the demands on her time.]', "office")),
    n("office", "Gesmerha", '''"There are also questions people bring because they want someone else to carry them home. A boundary. A debt. A quarrel over a tool that was borrowed before either disputant was born."
{n}She smooths the cloth beside the carving with the side of her hand.{/n}''',
      c('"Do they still bring those questions to you while Marhevok rules?"', "carver", requires=("gesmerha.marhevok_rules",)),
      c('"Does being their chief leave you any room to refuse?"', "chief", forbids=("gesmerha.marhevok_rules",))),
    n("carver", "Gesmerha", '''"Some do. Some lower their voices first. I would prefer them to stop looking over their shoulders, but I will not pretend that asking them to be brave makes the asking harmless."
"Would you prefer I spoke to him?"
"About a borrowed chisel? No. About my afternoons? Still no. You have made your decision about Marhevok. I have to judge which of my neighbors I can help under it."
{n}Her answer is firm, without invitation to bargain.{/n}
"If you want to do something here, let it be something you can finish with your own hands."
"I am not a woodshaper."
"Then you can begin by holding the other end of a plank. Most people survive their first lesson."
{n}She turns the block toward the open side of the bench.{/n}''', c('[Sit where she has made room.]', "offer")),
    n("chief", "Gesmerha", '''"A chief who cannot refuse will soon have nothing left worth asking for. I am learning. The lesson is not popular with everyone."
"I recognize that lesson."
"Then perhaps you can spare me advice and help me practice. There is room on this bench for a visitor. There is not room for a second chief."
{n}She shifts her cup toward herself and touches the clear place with two fingers.{/n}
"You can sit there. You can tell me if the shavings blow toward the knife. You can leave the knife where I put it. These are modest powers, but they are yours."
"I will try not to abuse them."
"Most people make that promise before they move my cup."
{n}You sit. Her cup stays where it is.{/n}''', c('[Ask what help she actually wants.]', "offer")),
    n("offer", "Gesmerha", '''"I have a length of wood put aside. I want to make a game board that folds around its pieces. A game for two people, with no army to carry and no god to flatter."
"Do you have rules?"
"Half of them. The other half have been winning arguments with me for years."
{n}She feels the shallow channels again.{/n}
"I used to make grander things. I still intend to. But I would like this one to be handled badly by someone enjoying it. I would like to hear the pieces dropped and complaints about the rules."
"That sounds more demanding than a statue."
"A statue seldom admits when it is losing."
{n}She smiles, then reaches for the cup and finds its broken handle with her thumb.{/n}
"Come back if you want to help examine the wood. Afterwards you may discover whether I am a fair opponent. I should warn you that nobody has given me a satisfactory answer to that question."
{n}The invitation is for an afternoon's work and a game. She has named no price and asked for no favor from the crusade.{/n}''',
      c('"I will return for the work and the game."', flags=("gesmerha.invited",)),
      c('"I cannot promise the game, but I would like to help with the wood."', flags=("gesmerha.invited", "gesmerha.work_first"))),
], delay=0)

s("along_the_grain", "A fault in the board", '"Shall we examine that wood?"', [
    n("start", "Gesmerha", '''{n}The length of wood lies on low supports. Gesmerha has brushed its surface clean. A line of chalk marks the proposed hinge; two smaller marks indicate where her hands should meet yours when you lift it.{/n}
"Tell me before you turn it. I would rather not learn your intentions from my fingers."
{n}Together you bring the pale underside uppermost. Near one end a dark seam curves out of sight.{/n}
"There," she says when you describe it. "I can follow it at the edge, but I cannot reach where it goes without cutting. It may be no more than a stain. It may spoil the whole length."
"What would you do without me?"
"Sacrifice a strip along that side. I have enough wood. I would prefer not to waste it."
{n}The piece is hers. She waits while you examine the seam, keeping her hands clear of the supported edge.{/n}''',
      c('[Examine the grain and the dark seam.]', check=dict(Skill="SkillLoreNature", DC=23, Success="sound", Failure="missed", CommanderOnly=True)),
      c('"Take the narrow strip. I would rather work from a cut we can both examine."', "strip"),
      c('"I cannot give this the time it needs today."', abort=True)),
    n("sound", "Gesmerha", '''{n}The seam narrows where the grain turns around an old branch. Beneath it, a second line runs almost parallel, too fine to notice until you turn the wood into the light. The two lines meet at the far edge.{/n}
"There is a split around the knot. If the hinge goes here, the screws will pull against it."
{n}You guide her finger to the edge you mean, with her hand resting lightly on yours. She feels the faint change in the surface, then asks you to turn the board again.{/n}
"Yes. Now that I know where to press, I can feel it move."
{n}She sets a small wedge into the seam. Under gentle pressure, the unsound corner comes away in one piece.{/n}
"That would have broken after I carved it. You have saved me a very bitter afternoon."
"Can you still make the board?"
"Narrower. The pieces will have less room to hide."
{n}She redraws the hinge line, measuring with a strip of cord. The block she has removed goes into a basket of offcuts, not into the fire.{/n}''', c('[Help her measure the narrower board.]', "narrow")),
    n("missed", "Gesmerha", '''{n}You trace the dark line as far as you can and find no open split. Gesmerha asks you to describe it again. At your answer she marks the hinge and begins a shallow cut.{/n}
{n}Halfway along, the blade catches. A thin crack runs toward the knot with a sound like a dry twig snapping.{/n}
"Stop holding it there. Put it down."
{n}You lower the board together. She tests the crack with a fingernail, then pushes a wedge into it. The corner parts too readily.{/n}
"It was split inside. Neither of us found the way in."
"I thought the line was only a stain."
"I know. That is why I began the cut."
{n}For a while she says nothing. The unfinished hinge groove now runs too close to the new edge. She measures it twice before setting the cord down.{/n}
"This cannot be the folding board I wanted. We can make two trays that sit together, or start again with another length. I do not want to start again today."
"Then show me the trays."
{n}She turns the damaged edge away from the hinge line and begins marking a shallower recess.{/n}''', c('[Help make the pair of trays.]', "trays")),
    n("strip", "Gesmerha", '''"The cautious answer. Hand me the little saw. Wooden handle, broad at the end."
{n}You place it against her open palm. She checks the blade with the back of a nail and tells you how to brace the wood. The saw follows the grain reluctantly. It takes longer than your first estimate and produces a heap of pale dust.{/n}
{n}When the strip comes free, she bends it over her knee. It breaks at the knot.{/n}
"Well. We have paid for certainty."
"Too much?"
"Ask me when I need a strip exactly this wide. For today, no."
{n}The remaining board is sound and a little narrower than she planned. She makes two quick calculations under her breath, then replaces the cord along the proposed hinge.{/n}
"We shall have to stop pretending the pieces need their own estates. A close game, then."
{n}You brush away the dust as she marks the new rows. Her fingers pause where your hand rests near the edge.{/n}
"Leave that side clear. I need to reach it. Thank you."''', c('[Clear the edge and help with the new measurements.]', "safe")),
    n("narrow", "Gesmerha", '''{n}The new rows fit. Gesmerha rubs her thumb over the last chalk mark, satisfied.{/n}
"There is a pleasure in finding the fault before it becomes everyone's problem. I had almost forgotten that part of the work."
"You have not forgotten how to use it."
"No. I have had less practice believing a good afternoon will remain good."
{n}She turns the removed corner in her hand.{/n}
"I shall keep this. A very small monument to an argument we did not have."
"Between us?"
"Between me and a broken hinge. I would have lost."
{n}She puts the offcut aside. When you leave, the space for the hinge is still uncut, but its position is right.{/n}''', c('"Let me know when you are ready for the next part."', flags=("gesmerha.wood_kept", "gesmerha.grain_found"))),
    n("trays", "Gesmerha", '''{n}The trays take shape slowly. You hold each one while Gesmerha tests the depth of the recess. They will need a cloth wrapped around them for carrying.{/n}
"I wanted one thing," she says. "Now I shall have two things that must be kept together. There is probably a proverb about that. Do not tell me."
"I do not know one."
"A quality I appreciate in a visitor."
{n}She asks you to find the offcut you first examined. It is not where you thought you left it. After a search you discover it beneath the supports and put it in her hand.{/n}
"Next time, leave the evidence where we can find it. Being wrong is tiresome enough without kneeling in the dust afterwards."
{n}She puts it beside her cord. The game will still be made, though she does not pretend it is the game she originally planned.{/n}''', c('"I will help with the wrapping when the trays are finished."', flags=("gesmerha.wood_kept", "gesmerha.grain_missed"))),
    n("safe", "Gesmerha", '''{n}You finish the measuring before she lets you sweep the bench. The sacrificed strip yields two small blanks for playing pieces and little else.{/n}
"You look as though you expect a verdict," she says.
"Was it the right choice?"
"It was a choice I offered. I knew what it would cost. You need not turn it into a trial."
{n}She places one of the blanks in your hand. It is smooth on one side and raw on the other.{/n}
"Here. Tomorrow this will be something worth arguing over. Today it can remind you how much work we have left."
{n}She asks for the blank back before you go. You surrender it, and she laughs.{/n}
"I said it could remind you. I did not say you could steal my pieces before we have a game."''', c('"I will return to lose them honestly."', flags=("gesmerha.wood_kept", "gesmerha.grain_cut"))),
], requires=("gesmerha.invited",))

s("whose_mark", "A name on the underside", '"How is the game coming along?"', [
    n("start", "Gesmerha", '''{n}The playing pieces wait in a shallow bowl. Some are short cylinders with a groove around the middle; the others have two grooves. Gesmerha lets you handle one of each.{/n}
"You can tell them apart without looking. And if someone insists on playing in the dark, we shall not have to invent a second set of rules."
{n}A scrap of parchment lies beneath the bowl. On it someone has sketched a shield and a suggestion for an inscription honoring the crusade.{/n}
"A traveler saw me working. He thinks people in Drezen would buy these if your name were on them. He offered to take an example and ask."
"Would they?"
"You tell me. It is your name."
{n}She picks up the parchment and holds it out. You describe the sketch, including the space left beneath the shield.{/n}
"He left that for my mark. Generous of him. He said my work deserved a patron."
"What did you say?"
"That my work deserved a customer. He did not seem to understand the difference."''',
      c('"Would selling them let you make more things you want?"', "price"),
      c('"I cannot discuss this properly now. Keep the example here."', abort=True)),
    n("price", "Gesmerha", '''"Perhaps. I would like better hinges. A sharp little plane of the kind your people carry. There are tools I have heard described and never held. I would enjoy making something that required them."
{n}She brings the corners of the parchment together and presses the fold flat with her thumb.{/n}
"I would also enjoy finishing this game before someone orders twelve. The traveler wanted a date. He wanted me to explain how many people could copy my design. By the time he left, I had apparently become a workshop."
"You could refuse the order."
"I have not received an order. I have received a man explaining how fortunate I would be to receive one."
{n}Her mouth tightens in a smile that is almost a grimace.{/n}
"I was angry with him. Then I was angry with myself for wanting the plane. I am still deciding which anger is useful."
"What would you put on the game?"
"My maker's mark. Whoever buys it may add their own name to the wrapping. They need not carve it into my work."''',
      c('"Let the work travel under your mark. I can give an honest account if anyone asks."', "own"),
      c('"Would you accept my name on a separate letter introducing the work, with yours on the piece?"', "letter")),
    n("own", "Gesmerha", '''"And if they ask whether buying it will please you?"
"Tell them to play it. If they dislike the game, they should buy something else."
"You make a poor patron."
"You asked for customers."
{n}She unfolds the parchment, turns it over, and asks you to write a short reply. One example may be shown. No delivery date has been promised. No copies have been ordered. Interested buyers may ask Gesmerha herself about the next piece.{/n}
{n}When you have read the words back, she changes 'copies' to 'further boards'.{/n}
"They will not be identical. The wood will differ, and I may think of a better way."
"The traveler will dislike that."
"He may put his disappointment on a shield."
{n}She lays the reply beneath the bowl. Her fingers linger on the topmost piece before she lets you take it.{/n}
"A warning. I am going to charge more than he suggested. If he refuses, I may have to be unpleasant company for a while."
"I have met unpleasant company."
"You have not met me after someone undervalues three days of carving."''', c('"I will stand by the answer we wrote."', flags=("gesmerha.mark_kept", "gesmerha.own_mark"))),
    n("letter", "Gesmerha", '''"That is a small distinction for someone accustomed to large banners. Explain it."
"The letter would say where the work came from and how to reach you. It would promise no crusade purchase, no protection, and no favor for whoever buys it."
"Would you put that last part in the letter?"
"If you want it there."
"I do. I want to hear how uncomfortable it sounds."
{n}You write it. Read aloud, the disclaimer occupies nearly as much space as the introduction. Gesmerha begins to laugh before you finish.{/n}
"Nobody will frame that. Good."
{n}She asks you to remove a sentence praising her endurance. You replace it with an account of the grooved pieces and the portable board. That she allows to stand.{/n}
"If this produces twelve orders, we shall answer that I have two hands. I will not train them to move faster because someone likes your seal."
"Agreed."
{n}She folds the letter herself, finding the edges with her fingertips. Then she puts it beside her own reply, which names a price and promises no date.{/n}''', c('"The letter introduces your work. You decide what comes next."', flags=("gesmerha.mark_kept", "gesmerha.introduced"))),
], requires=("gesmerha.wood_kept",))

s("the_first_game", "A rule she dislikes", '"Is it time to learn your game?"', [
    n("start", "Gesmerha", '''{n}Gesmerha has cleared the bench. The pieces sit in two groups, each within easy reach of one player.{/n}
"The reply came back," she says. "We should dispose of business before you discover how ruthless I am at leisure."''',
      c('"What did he say about selling it under your mark?"', "own_reply", requires=("gesmerha.own_mark",)),
      c('"Did the letter help?"', "letter_reply", requires=("gesmerha.introduced",))),
    n("own_reply", "Gesmerha", '''"He says buyers would want a discount if there is no special connection to the crusade. I told him the connection was that its Commander had helped me measure the wood. He did not find that special enough."
"So he refused?"
"He refused to carry it at my price. I have refused to lower the price. We are very efficient correspondents."
{n}She sets the returned scrap beneath her cup.{/n}
"I was bad company, as promised. Then I sharpened the tools I already own. I would still like the plane."
"We could try someone else."
"Later. I want to find out whether the game is any good before I spend another afternoon defending its price."
{n}She pushes the one-grooved pieces toward you. Her answer has cost her a possible sale. She does not ask you to pretend the cost was imaginary.{/n}''', c('[Sit down to play.]', "board")),
    n("letter_reply", "Gesmerha", '''"He knows a merchant willing to look at one example. The merchant asks whether I can make a simpler version, without the grooves, for less money."
"Would you?"
"No. I mean to play the things I make. I am not going to save a stranger a handful of coins by making that impossible."
{n}She puts one of the double-grooved pieces in your palm.{/n}
"I offered to leave the outside plain. That would save time. The parts a player touches will stay as they are. If that is too dear, he can purchase dice."
"Has he answered?"
"Not yet. Your name got the work considered. It did not make the consideration pleasant."
{n}She takes the piece back and places it with its fellows.{/n}
"I am glad we tried. I shall be gladder when somebody wants to play instead of simplify."''', c('[Sit down to play.]', "board")),
    n("board", "Gesmerha", '''{n}She asks you to describe the arrangement once, then checks it with her hands. Each row has a small notch at its edge. She names a row and moves a piece along it, feeling for the shallow stopping points.{/n}''',
      c('[Set the paired trays firmly together.]', "trays", requires=("gesmerha.grain_missed",)),
      c('[Open the narrow board and check its hinge.]', "hinge", forbids=("gesmerha.grain_missed",))),
    n("trays", "Gesmerha", '''{n}The trays slide apart when you push the first piece across their join. Gesmerha catches the nearer one and sighs.{/n}
"There is the fault we bought. Fetch the wrapping cloth."
{n}Folded twice beneath the trays, it holds them steady. You try the move again, slowly. This time the piece reaches the opposite row without disturbing the board.{/n}
"An extra thing to remember," she says. "Put the cloth away with them when we finish."
"I will."
"And you may move that piece back. Fixing the table did not entitle you to take my corner."
{n}Her finger is already on the occupied corner. You return your piece to its starting place.{/n}''', c('[Begin the game again.]', "play")),
    n("hinge", "Gesmerha", '''{n}The hinge holds. The narrow rows place your fingers close to hers when you make the first move. She waits until you withdraw your hand before feeling the new arrangement.{/n}
"Name the row before you move. I shall do the same. Then if either of us knocks a piece, we will know where it belonged."
"Does knocking your opponent's piece count as a strategy?"
"Only if you wish your opponent to become tedious about the rules. I assure you I can."
{n}You name a row. She checks the piece and answers with a move of her own, too quickly for you to guess whether it was prepared or improvised.{/n}''', c('[Study her reply.]', "play")),
    n("play", "Gesmerha", '''{n}You learn the game by losing the first round. In the second, you discover that a piece against the outer edge can block two of hers. She tests the position, moves a finger to the empty center, and withdraws it.{/n}
"That rule has always irritated me."
"Because it works?"
"Because a dull player can defend a corner forever."
"You put it there."
"I inherited it from the person who taught me. That is a different kind of foolishness."
{n}She folds her hands beside the board, leaving the position intact.{/n}
"We could alter it. Once a piece reaches the outer row, it must move back inward on its next turn. But we would have to begin again."
"You are proposing to change a rule while I am winning."
"I am proposing to change a rule while you are taking an intolerable time to win. There is a distinction."
{n}Her smile is open now, almost challenging. She is perfectly prepared to play the dull position out if you insist.{/n}''',
      c('"Finish this game under the old rule. Then we will try yours."', "finish"),
      c('"Let us start again with the change. I want to see what it does."', "change")),
    n("finish", "Gesmerha", '''{n}It takes longer than either of you expects. She makes you name every move and finds two ways to postpone the loss. When the last is exhausted, she touches the final position and concedes with a small bow.{/n}
"There. A complete victory. I hope it keeps you warm on the road."
"You could have conceded earlier."
"I could have carved a box."
{n}She resets the pieces. The altered rule produces a quicker game, and this time you lose a piece by forgetting the new restriction. Gesmerha catches the mistake before you take your hand away.{/n}
"Back inward. I want to beat you under the rules we agreed to."
{n}By the end she has won, but neither of you mistakes that for proof the change was fair. She asks you to play it again another day.{/n}''', c('"Keep both sets of rules. We can quarrel over which to use."', flags=("gesmerha.game_kept", "gesmerha.finished_rule"))),
    n("change", "Gesmerha", '''{n}You reset the pieces. The new rule makes the outer rows dangerous; two of your early moves turn out to trap you instead of her. Then she makes the same mistake and sits very still, touching the piece she can no longer save.{/n}
"I had imagined this being more elegant."
"It may be. We may simply be bad at it."
{n}She laughs loudly enough to turn a passerby's head. At your next move she stops you and asks to feel the whole position again.{/n}
"No. Leave that piece there. I think we have found something."
{n}The next exchange opens the center and gives both of you a chance. She forgets her cup until the drink is cold. When you finally stop, the question of who won the abandoned game remains unresolved and seems less interesting than it did before.{/n}''', c('"I want another game under the new rule."', flags=("gesmerha.game_kept", "gesmerha.changed_rule"))),
], requires=("gesmerha.mark_kept",))

s("the_unclaimed_hour", "When the tools are put away", '"Would you like company when the work is finished?"', [
    n("start", "Gesmerha", '''{n}Gesmerha wipes the blade of her knife, checks that it is dry, and folds it into its cloth. She has finished before you ask. Your arrival has not brought the working day to an end.{/n}
"Company doing what? People are very fond of offering company with an errand hidden in it."
"Sitting. Talking. Perhaps something to drink."
"I have a drink. It is not a very good one. You may have some if you promise not to praise it."
{n}She leads the way to a sheltered seat near her work. The ground is familiar to her; she taps the seat once before sitting and tells you which end catches the wind.{/n}
"That end is yours. You may take it as a compliment to your cloak."
{n}The drink tastes of smoke and something sour. When you pause over it, she turns toward you expectantly.{/n}''',
      c('"I see why you demanded the promise."', "laugh"),
      c('"It is warm. I will confine my praise to that."', "warm"),
      c('"I cannot stay after all. Keep the cup for another evening."', abort=True)),
    n("laugh", "Gesmerha", '''"The woman who made it called it invigorating. She was right. I have been thinking of little else since the first mouthful."
"Why keep drinking it?"
"She gave me a whole jar. I dislike defeat."
{n}She takes another sip, considers it, then puts the cup down decisively.{/n}
"There. I have lost. I feel younger already."
{n}Her laughter catches on the last word. She clears her throat and asks you to describe something ordinary you have enjoyed recently, something that did not require a battle to obtain.{/n}''', c('[Tell her about a meal that lasted longer than expected because the conversation was good.]', "ordinary")),
    n("warm", "Gesmerha", '''"A restrained tribute. I shall pass it on if she asks."
{n}She sets her own cup down after another doubtful sip.{/n}
"I wanted to like it. She was so pleased to give me something I had not asked for. There has been a great deal of asking lately."
"You can appreciate the gift without finishing the jar."
"Can I? What a convenient custom. We should adopt it at once."
{n}She moves the jar away from both cups and leans back against the wall.{/n}
"Tell me something you enjoyed without having to convince yourself. No victory speeches. I have heard enough of those to know where the pauses go."''', c('[Tell her about a meal that lasted longer than expected because the conversation was good.]', "ordinary")),
    n("ordinary", "Gesmerha", '''{n}She listens to your account, asking what was served and who forgot to clear the dishes. When you describe the last scraps being divided, she asks who took the piece everybody had been politely avoiding.{/n}
"That is the person I would like to meet," she says. "Someone willing to end an argument by eating it."
"What would you do with an evening that nobody could interrupt?"
"I would invite somebody to interrupt it. At a time of my choosing."
"You have managed that much."
"Yes. I am deciding what to do with the rest."
{n}For a moment she falls silent. You hear movement farther down the path, a bucket set down, two people calling to each other. The sounds pass without becoming a demand on her.{/n}
"I miss being asked foolish things," she says. "Not careless things. Foolish ones. Whether I would rather be a bird or a fish. Whether a song would sound better with all the verses in the wrong order. People think every conversation with me ought to repair something."
"Bird or fish?"
"Bird. I do not trust water enough to live in it. You?"''',
      c('"Bird. We could argue about where to land."', "bird"),
      c('"Fish. I could finally escape requests delivered by messenger."', "fish")),
    n("bird", "Gesmerha", '''"I should choose the highest roof and you would choose the one with the best view. We would both complain about the wind."
"You have settled the argument without having it."
"I am conserving my strength. We would still have to find supper."
{n}She shifts a little closer, her shoulder almost touching yours. The warmth of her body reaches you through the narrow space between your sleeves.{/n}
"Do you always answer questions as though they might become orders?"
"Not always."
"Good. I have no intention of growing feathers for you."
{n}The teasing is gentle now. She leaves the space between you as it is, small enough to notice and large enough to choose what comes next.{/n}''', c('[Stay beside her.]', "ask")),
    n("fish", "Gesmerha", '''"A messenger would learn to swim. Then you would have to listen to every request twice because the first copy was wet."
"You have made the river sound worse than a council meeting."
"I have attended some very bad meetings. It is an informed comparison."
{n}She shifts a little closer, her shoulder almost touching yours. You can smell the clean wood dust caught in her sleeve beneath the smoke from the cups.{/n}
"Stay on land," she says. "You have only just learned the rules of my game. I do not want to start again with somebody else."
{n}It is an invitation to another visit, spoken without the protection of a joke. She lets it stand.{/n}''', c('[Stay beside her.]', "ask")),
    n("ask", "Gesmerha", '''"There is something I should ask while neither of us is pretending to work. Why do you keep coming back?"
{n}She turns her face toward your voice. The old scars are visible in the sheltered light. Her expression is attentive, a little wary, and more interested than she intends to disguise.{/n}
"I like your company," you say.
"That is a pleasant answer. It has room to hide several others."
{n}Her hand rests on the seat between you. She has not reached for yours.{/n}
"I find myself listening for your arrival. Sometimes I am annoyed when somebody else's boots make the right sound. I would rather know whether I am being foolish before I begin resenting innocent footwear."
{n}The words cost her a moment's hesitation. Once spoken, they make her smile at herself.{/n}
"Answer me plainly. I have survived worse than a wrong guess."''',
      c('"I want you. I would like to come back courting, not visiting."', "court"),
      c('"There may be more here. Give me time to find out."', "slow"),
      c('"Your friendship is what I want. Plainly."', "friend")),
    n("court", "Gesmerha", '''"I do want it. I had begun preparing a very dignified way of pretending otherwise. You have spared us both."
{n}She offers her hand palm upward. When you take it, her fingers close around yours, warm and a little rough from the day's work.{/n}
"I will not begin calling you by your title over supper. And I will still tell you when you are losing at the game."
"Those are your conditions?"
"Those are the ones I thought of while being dignified. More may occur to me."
{n}She draws your joined hands onto her knee and stays there, neither hurrying the moment nor making a ceremony of it. After a while she asks you to return when the wind has dropped. She has a small thing she wants to show you.{/n}''', c('"I would like that."', flags=("gesmerha.hour_kept", "gesmerha.courting"))),
    n("slow", "Gesmerha", '''"Then I shall resent no boots yet."
{n}She lets out a breath and leans back. The space between your shoulders remains small.{/n}
"A doubt said aloud I can live with. It is the unspoken ones that rot the wood from inside. Keep coming, and we will see what the grain does."
"I will."
"Good. Come back when the wind drops. I have something to show you, and it will not require an answer about the rest of your life."
{n}She picks up her cup, remembers what is in it, and sets it down again.{/n}
"We shall also obtain a better drink. I am prepared to make that decision without further reflection."''', c('"We have another afternoon, then."', flags=("gesmerha.hour_kept", "gesmerha.slow"))),
    n("friend", "Gesmerha", '''"Thank you."
{n}She withdraws her hand from the space between you and folds it over the other in her lap. For a little while she listens to the village.{/n}
"I am disappointed. It will pass. You need not become excessively kind until it does. That would be more difficult to endure."
"Would you prefer I left?"
"I would prefer you told me why defending that outer row pleased you so much. I am still deciding whether to forgive you."
{n}You defend your tactics. She considers your argument and rejects your best excuse. By the time the cups are empty enough to abandon, the conversation has found its old ease, though you both leave a few subjects alone.{/n}
"Come back when the wind drops," she says as you rise. "I have something to show you. A friend is permitted to be impressed."''', c('"I will come as your friend."', flags=("gesmerha.hour_kept", "gesmerha.friendship"))),
], requires=("gesmerha.game_kept",))

s("against_the_current", "A boat for no customer", '"You had something to show me."', [
    n("start", "Gesmerha", '''{n}A little wooden boat rests in Gesmerha's palm. Its hull is no longer than your finger, and a narrow shaving curls above it in place of a sail.{/n}
"From the offcuts. I was meant to be testing a tool. Then I wanted to see whether it would float."
{n}A shallow basin stands beside the bench. She asks you to set it level, then places the boat on the water. It leans so far to one side that the sail touches the surface.{/n}
"You are allowed to laugh," she says. "I know what it is doing."
"How?"
"The sail grows wet when I lift it. There are ways to learn what a boat has done besides watching it."
{n}She retrieves it, feels the wet shaving, and rests the hull in her palm again.{/n}
"It needs weight. Or a smaller sail. I would prefer to keep the sail. I like the way it catches against my finger."''',
      c('"Let us try a small weight low in the hull."', "weight"),
      c('[Offer a little Trickster nonsense: persuade the basin to lend the boat its center for a moment.]', "trick", requires=("trickster",)),
      c('"Keep it out of the water until I can stay longer."', abort=True)),
    n("weight", "Gesmerha", '''{n}You try a small pebble, then a smaller one. The first puts the hull so low in the water that a ripple swamps it. Gesmerha turns it over to drain and accuses you of confusing a boat with an anchor.{/n}
{n}The second keeps it upright. She follows its rim with one finger, barely touching, while you describe the sail above it.{/n}
"And if I take the stone out?"
"It will lean again."
"Good. I would hate to learn that it had only been contrary."
{n}She pushes water toward the hull with the side of her hand. The boat turns, bumps the basin, and circles back.{/n}
"I have made a vessel fit to cross a washing bowl. My ancestors will be astonished."
"You wanted it to float."
"I wanted to enjoy making it. Floating is a pleasant addition."
{n}She lets it complete another slow circle before lifting it out.{/n}''', c('[Dry the basin rim while she dries the boat.]', "history")),
    n("trick", "Gesmerha", '''"Explain what you mean before you do anything."
"For a moment, the boat can borrow the basin's balance. It will think it is too broad to tip. Nothing about you or the village has to change."
"A foolish little bargain."
"Very little."
{n}She turns the boat in her hand, then places it back on the water.{/n}
"One moment. And describe it honestly. If it sinks, I want to know."
{n}You address the basin with the gravity due a difficult official. The tilted hull slowly rights itself. A drop climbs the inside of the bowl, thinks better of the journey, and falls back.{/n}
{n}At Gesmerha's request you guide her finger to the upright rim. She touches it, laughs once in surprise, then takes her hand away.{/n}
"Enough. Let it have its own troubles again."
{n}The borrowed balance goes. The boat leans, and she catches it before the sail becomes soaked.{/n}
"Now find us a small stone. I want it to float when you are somewhere else."
{n}You ballast the hull and try it again. This time its balance belongs to the pebble. She tests it with a ripple and seems more satisfied with the second result.{/n}''', c('[Help her dry the boat after its voyage.]', "history")),
    n("history", "Gesmerha", '''{n}She rubs the hull with a corner of cloth and sets it where she can find it again.{/n}
"No customer. No inscription. No debate about what the clan ought to be. I wanted you to see that I can still waste an afternoon very agreeably."
"I would not call it wasted."
"I would. It was mine to waste."
{n}She sits beside the empty basin. A trace of water darkens her cuff. She finds it with her other hand and rolls the sleeve back.{/n}
"I have been thinking about what you told me."''',
      c('[Sit close enough for your sleeves to touch.]', "court", requires=("gesmerha.courting",)),
      c('[Give her time to continue.]', "slow", requires=("gesmerha.slow",)),
      c('[Sit beside her as a friend.]', "friend", requires=("gesmerha.friendship",))),
    n("court", "Gesmerha", '''"I wanted to kiss you the other evening. Then I began wondering whether I should wait until we had a less ridiculous drink. By that measure we might have waited all winter."
{n}She turns toward you, close enough that her knee brushes yours.{/n}
"I will need you to tell me where you are. Then I should like to stop talking for a little while."
{n}Her hand rises, waiting for you to meet it. Her smile is nervous at the edges and quite certain at its center.{/n}''',
      c('"Here." [Take her hand and guide it to your cheek.]', "kiss"),
      c('"I would like to hold you today. The kiss can wait."', "hold")),
    n("kiss", "Gesmerha", '''{n}Her fingertips brush your cheek and settle beside your mouth. She moves closer at your quiet answer, her other hand resting on your shoulder.{/n}
{n}The first kiss is brief. She draws back enough to breathe, laughs softly at something she does not explain, and kisses you again. This time you feel the care in her movements give way to pleasure.{/n}
{n}When you part, she keeps her hand against your cheek.{/n}
"There. I have been wanting to do that while asking you very sensible questions about wood."
"Were they genuine questions?"
"Entirely. I contain more than one thought. Occasionally they interfere with each other."
{n}You stay close until she leans back, comfortable enough to ask you to move the basin before somebody catches it with a foot. The little boat remains on its cloth, drying in the air.{/n}
"Next time," she says, "come with a story that has nothing to do with me. I want to find out who visits all these other places and then comes here."''', c('"I will bring one worth your afternoon."', flags=("gesmerha.opening_kept", "gesmerha.first_kiss"))),
    n("hold", "Gesmerha", '''"Then sit nearer. Your cloak is doing most of the holding from there."
{n}She leans into your arm, adjusting until the seam of your sleeve no longer presses against her cheek. One hand settles on your wrist.{/n}
"That is better."
{n}You listen to the village for a while. She identifies one approaching step, then admits she cannot place the next. The unknown visitor passes without stopping, and she relaxes against you again.{/n}
"Next time, bring a story from somewhere else. Not a report. Something you would tell a person you wanted to stay beside after you finished telling it."
"That may take thought."
"You have until your next visit. I expect a reasonable effort."
{n}Her fingers close briefly around your wrist. When she sits up, she asks you to help put the basin away, and leaves the boat where she can touch it on returning to the bench.{/n}''', c('"I want another afternoon with you."', flags=("gesmerha.opening_kept", "gesmerha.held_close"))),
    n("slow", "Gesmerha", '''"Slow suits wood. It may suit us. I can want another afternoon without reading omens into every silence."
{n}She touches the little boat with one finger, checking its place on the cloth.{/n}
"That does not mean I have stopped being curious. Next time I want a story from somewhere you have been. One you choose because you enjoyed being there. I have heard enough accounts of where the Commander was needed."
"And if I choose badly?"
"Then I shall ask questions until we reach the interesting part."
{n}She leaves room beside her while you put the basin away. When you return to the seat, she begins an account of a carving she once disliked so much that she turned it upside down and began again. She refuses to tell you what it originally depicted.{/n}
"Another afternoon," she says. "I have to keep something back."''', c('"Another afternoon, without hurrying it."', flags=("gesmerha.opening_kept",))),
    n("friend", "Gesmerha", '''"You have been good company. I wanted to say so, without you wondering whether I was asking you the other thing again."
"You have been good company too."
"Even over the drink?"
"Especially after you surrendered to it."
{n}She laughs and reaches for the boat. For a moment she seems about to offer it to you; then she puts it back on its cloth.{/n}
"I am keeping this one. I give away too many things simply because someone was present when I finished them."
"I have a game to return to."
"You do. And a story to bring. Next time, tell me something about a place I have never been. I will interrupt with questions, so choose a place you actually remember."
{n}You help put the basin away. She has already begun setting out the pieces by the time you return, leaving your side of the bench clear.{/n}''', c('"I will bring a story, and try to remember the rules."', flags=("gesmerha.opening_kept",))),
], requires=("gesmerha.hour_kept",))

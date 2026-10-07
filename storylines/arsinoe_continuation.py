"""Arsinoe's authored private hours and courtyard venture, after the opening."""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
CONTACT = "a609ed9b2205d034bb3bb04d2a255681"


def s(id, title, entry, nodes, previous, delay=24):
    SCENES.append(scene(id, title, "Arsinoe", 3, entry, nodes,
                        requires=tuple(dict.fromkeys(("arsinoe.capital", "arsinoe.opening_kept", previous))),
                        forbids=("arsinoe.closed",), delay=delay, optional=True,
                        Relationship="arsinoe", Areas=[DREZEN], Chapters=[3, 5],
                        ContactUnit=CONTACT,
                        AnswerLists=["ecaf5cfe8087a4f45a2269974f4885c9"]))


s("arsinoe_your_hours", "The Commander's questionable taste",
  '"You wanted to know what interests me. I have something to show you."', [
    n("start", "Arsinoe", '''{n}Arsinoe finishes writing a price on a narrow strip of paper. She gives it to her customer, answers a final question about the scroll, and waits until the man has left before turning toward you.{/n}
"The army has had its scrolls, and the temple has had my morning. Show me what you choose when nobody is demanding it."
{n}She takes her outdoor cloak from its peg. A thread has caught around the fastening; she frees it with a practiced turn of one fingernail.{/n}
"I can spare the next hour. If your interest requires a week in the saddle, you must give me a little more notice. If it requires my professional opinion, I reserve the right to be disappointed."
{n}Her smile takes the sting from the qualification.{/n}''',
      c('"A game. One that is over before anyone starts calling it a campaign."', "game"),
      c('"An outrageously bad adventure story. I want someone to enjoy it with."', "story"),
      c('"I need to postpone our hour."', abort=True)),
    n("game", "Arsinoe", '''{n}You find an unoccupied table and mark a small board on the back of a discarded notice. Pebbles serve for pieces; a broken tile marks the gate. Arsinoe turns the paper around until the notice is no longer upside down to her.{/n}
"I cannot concentrate while being ordered to deliver six sacks of oats by yesterday."
{n}You explain the game. One side tries to pass the gate; the other tries to surround it. Pieces cannot retreat. Arsinoe listens without touching the board, then asks three questions about draws that you had hoped would not arise.{/n}
{n}The first round goes quickly. You take an opening she appears to have missed, and discover why she left it. Your leading piece is now incapable of moving anywhere useful.{/n}
"That was a very fine advance," {n}she observes.{/n} "Do you require a commemorative notice? We have paper."
{n}The second round lasts longer. Neither of you mentions the war.{/n}''',
      c('"You enjoyed that far too much. Again."', "game_again"),
      c('"Let me show you the variation where the gate can move."', "game_change")),
    n("game_again", "Arsinoe", '''{n}This time Arsinoe loses her best piece while arranging the rest into a shape she finds pleasing. She studies the empty place with real annoyance.{/n}
"I had an excellent plan for that corner."
"You can still admire it."
"Thank you. Your generosity in victory is memorable."
{n}She gives you the captured pebble, then stops your hand as you begin to clear the board.{/n}
"Leave it a moment. I want to see where I did it."
{n}You trace the earlier moves together. It is a small pleasure to argue about something whose worst possible result is another lost pebble. When she finally sees the mistake, she laughs at herself without asking you to soften the account.{/n}
"I have a game among my traveling things. More elaborate than this. I bought it because the board was beautiful, and have never had a satisfactory explanation of the rules. Will you help me remedy that disgrace?"''',
      c('"Bring it next time."', flags=("arsinoe.interest_games",))),
    n("game_change", "Arsinoe", '''{n}Arsinoe protests the moving gate until she sees an opportunity to use it against you. After that she defends the variation with considerable energy.{/n}
"The gate was always an underused piece."
"You called it an architectural impossibility."
"I was speaking as a disappointed visitor. My position has improved."
{n}The board fills with possibilities that neither of you can quite calculate. You make a desperate move; she answers it too quickly and discovers a trap you had not meant to set. Both of you claim credit for understanding it first.{/n}
{n}At the end she gathers the pebbles into a neat pile, keeping the broken tile separate.{/n}
"I have a traveling board you might enjoy. The seller explained its rules to me while packing three other purchases. I suspect I have been playing it incorrectly ever since. That seems an excellent reason to bring it."''',
      c('"Then our next game should be a revelation."', flags=("arsinoe.interest_games",))),
    n("story", "Arsinoe", '''{n}The little borrowed booklet has a cracked cover and an extravagant title. Its hero enters a forbidden palace in the opening paragraph, loses his disguise in the second, and spends most of the third explaining why the palace's entire guard should trust him.{/n}
{n}Arsinoe listens until the princess reveals that she has been disguised as her own aunt.{/n}
"Does the aunt know?"
"The author does not say."
"Then I choose to believe that she does, and has gone on holiday with the household silver."
{n}You continue. Arsinoe begins supplying the aunt's movements in the pauses. By the time the hero reaches a window with no ledge beneath it, the missing woman has acquired a boat, an accomplice, and a much more convincing escape plan.{/n}
"I concede the attraction," {n}Arsinoe says.{/n} "Though I do not think we are enjoying quite the book its author intended."''',
      c('"Read the princess. I will do the hero."', "story_roles"),
      c('"Let us give the aunt the ending she deserves."', "story_aunt")),
    n("story_roles", "Arsinoe", '''{n}Arsinoe gives the princess the measured voice of a woman assessing a very expensive mistake. Your hero's declaration of eternal devotion draws a long silence.{/n}
"There are six guards on the stairs," {n}she reads.{/n} "Perhaps begin with something achievable."
"That is not the next line."
"It ought to be."
{n}She does return to the printed words, although the princess now sounds increasingly doubtful about them. The scene ends in an improbable leap. Arsinoe closes the booklet before the author can explain where everyone landed.{/n}
"I want to remember them in the air. The ground will only disappoint us."
{n}Her thumb rests on the worn cover.{/n}
"I had forgotten how enjoyable it is to read aloud without teaching anybody anything. Bring this again. I can contribute a tale of my own, although it has regrettably little intrigue. It concerns an expensive game and a woman who did not ask enough questions before buying it."''',
      c('"I already like your heroine."', flags=("arsinoe.interest_stories",))),
    n("story_aunt", "Arsinoe", '''{n}You begin with the boat. Arsinoe insists on establishing who owns it. You propose that the aunt stole it; she counters that an accomplice with a boat is a much better investment than one with romantic intentions and no practical skills.{/n}
{n}Between you, the aunt acquires a new name and a destination neither of you has visited. She sells only enough silver to reach it. The rest she keeps, because the story has not yet provided a reason for her to become sensible.{/n}
"And there we should leave her," {n}Arsinoe says.{/n} "Before we spend her stolen silver on an inn. I like her better in the boat."
{n}She returns the booklet reluctantly.{/n}
"Next time I will bring something. It has a beautiful board, a set of rules that appear to contradict one another, and a history I may have paid too much to hear. You can decide whether the seller belongs in our next story."''',
      c('"I look forward to meeting him at a safe distance."', flags=("arsinoe.interest_stories",))),
], "arsinoe.opening_kept", delay=24)


s("arsinoe_borrowed_court", "The seven merchants",
  '"Did you find the game you promised?"', [
    n("start", "Arsinoe", '''{n}Arsinoe has wrapped the board in a length of faded green cloth. She lifts one corner to show you inlaid streets, seven little brass merchants, and a square of pale wood at the center.{/n}
"It has survived considerably more journeys than its instructions. I have arranged somewhere we can spread it out."
{n}The place is a locksmith's courtyard a few streets away. Its owner, Neral, is a broad-shouldered woman with a burn scar on her wrist and a habit of shutting drawers with her hip. She shows you a table beneath a patched awning.{/n}
{n}A repaired lock lies beside Neral's tools, its case scored where someone tried to force it during the occupation.{/n}
"Two hours," {n}Neral says.{/n} "If you want more chairs, fetch them yourselves. I am not closing the workshop."
"Nor would I ask you to."
{n}Arsinoe has paid for the table. She accepts your offer to carry the board, but declines to let you reimburse her. It is her turn to bring something.{/n}''',
      c('"Let us meet your merchants."', "board")),
    n("board", "Arsinoe", '''{n}The brass figures carry bags, baskets, and little folded cloths. Each has a different mark on its base. Two marks also appear in the margin of the brittle instruction sheet.{/n}
"The seller told me that everyone must reach the square before the gates close. Then he demonstrated a move that made this impossible. When I asked why, he said that was the lesson."
{n}She sets a figure on one of the inlaid roads.{/n}
"I have since wondered whether the lesson was to find another seller."
{n}The sheet names tolls, shelters, and a privileged route, but its last fold has worn through the sentence explaining who can use that route. One brass merchant carries a tiny key. It could be a useful clue, or an especially attractive distraction.{/n}
{n}From her doorway, Neral looks at the board.{/n}
"If you cannot agree on the rules, write down the ones you do agree on. Otherwise the loudest player wins."''',
      c('"May I compare the marks with the wording?"', "method"),
      c('"We could follow Neral\'s advice and make our own version."', "house")),
    n("method", "Arsinoe", '''{n}Arsinoe moves her cup beyond the reach of the old paper and holds the sheet flat with two clean stones. The difficulty is not magical: its writer assumed that everyone knew which kinds of merchant paid which tolls. The marks may preserve that distinction.{/n}
"If you can make sense of it, I will be grateful. If you cannot, I will survive the loss of my reputation as an informed purchaser."
{n}She turns the keyed merchant in her fingers.{/n}
"Do not let the charming little key persuade you before the words do. It persuaded me for several years."
{n}The workshop hammer falls twice, stops, and starts again. You have time to study the damaged instructions, or to leave their missing rule unsettled and begin a game that belongs to the people at this table.{/n}''',
      c("[Knowledge (World)] Reconstruct the toll rule from the marks and surviving instructions.",
        check=dict(Skill="SkillKnowledgeWorld", DC=24, Success="original", Failure="uncertain", CommanderOnly=True)),
      c('"I would rather invent a version with you."', "house")),
    n("original", "Arsinoe", '''{n}The repeated mark means a covered stall, not a locked gate. The privileged route belongs to the merchant carrying cloth: the rules shelter goods that would spoil in rain. The little key merely identifies its owner's trade.{/n}
{n}Once you place the cloth seller correctly, the impossible demonstration resolves into a contest over the remaining dry roads. Arsinoe tests your reading against the other instructions, then presses her lips together.{/n}
"I have been granting a locksmith the privileges of a cloth merchant. Neral, you may wish to reconsider your occupation."
"I will wait until the cloth merchants can open my drawers."
{n}The game is sharp and brief. Arsinoe sacrifices a profitable route to block yours, and discovers that you have left yourself another. Afterward she copies the reconstructed rule onto a fresh slip, crediting the two of you with the repair rather than claiming a recovered original sheet.{/n}
"This deserves another table of players. I should like to watch someone else make my mistakes."''',
      c('"I would enjoy that too."', flags=("arsinoe.game_reconstructed",))),
    n("uncertain", "Arsinoe", '''{n}You can make either reading fit part of the sentence. Neither accounts for the second mark. After a patient attempt, you have two plausible rules and no honest reason to call one the original.{/n}
{n}Arsinoe takes the key-bearing merchant off the disputed road.{/n}
"Then we do not know. I would rather say so now than explain an invented certainty to the next person."
{n}You play with the privileged route closed. The merchants crowd the remaining streets; the round takes longer than either of you expected. Neral reminds you of the hour before you finish. You record the unfinished positions on a scrap so that no one has to claim a victory.{/n}
"A rather expensive draw," {n}Arsinoe says as you pack.{/n} "But I still want to finish it."
{n}She puts the sketch inside the green cloth.{/n}
"Next time we shall allow longer, and tell people exactly what is missing. There is room for an uncertain rule at a table, provided nobody pretends otherwise."''',
      c('"Keep the positions. We will finish our game."', flags=("arsinoe.game_unresolved",))),
    n("house", "Arsinoe", '''{n}You set aside the damaged instruction sheet. Each merchant may use the short road once, but only after giving another player a turn there. Arsinoe writes the rule down, then catches you attempting to apply it to yourself twice.{/n}
"The ink is barely dry."
"I was testing the wording."
"It has survived its first adversary."
{n}Neral supplies two buttons when you need more counters. Your version produces a ridiculous traffic jam in the central square and one surprisingly elegant escape. Neither of you can remember which of you suggested the move that caused the jam. Both remember who found the way out.{/n}
{n}Arsinoe labels the new slip COURTYARD RULES and places it beside the old sheet, leaving the damaged original untouched.{/n}
"I would like to try this with more people. Three minds have already improved it. Or at least made its faults more entertaining."
{n}Neral holds out her hand for the borrowed buttons. You return them before the game can acquire another creditor.{/n}''',
      c('"Let us find another table of willing merchants."', flags=("arsinoe.game_house",))),
], "arsinoe_your_hours")


s("arsinoe_price_of_an_evening", "A place at the table",
  '"You mentioned inviting more people to the courtyard."', [
    n("start", "Arsinoe", '''{n}Arsinoe has Neral's offer written on half a sheet: the courtyard, two extra tables, lamps, and an evening without hammering. Beneath it she has calculated the cost of six places.{/n}
"She is willing to open after work. I have asked her to hold one evening until we answer. I have paid nothing yet."
{n}She places a finger beside the smaller sum.{/n}
"If we charge this, the evening pays for itself. Not much more than a drink, and less likely to produce a headache. I thought we could begin with the game, then read something."
{n}Her proposed notice includes a line announcing the Commander's participation. It is written in the same careful hand as the prices.{/n}
"A modest undertaking," {n}she says.{/n} "Though I admit I have enjoyed arranging it. What do you think?"''',
      c('"You have turned our afternoon into an advertised attraction."', "attraction"),
      c('"I like the idea. But my name will change who comes."', "name"),
      c('"Why charge at all? Invite a few people and let it remain an evening."', "charge")),
    n("attraction", "Arsinoe", '''{n}Arsinoe looks down at the notice. She does not immediately apologize.{/n}
"I thought you enjoyed it."
"I did. That does not mean I want to perform it for a room of customers."
{n}She puts the sheet flat on the table.{/n}
"No. But I also enjoyed it, and I would like a place where I can do this again without borrowing space every time. I cannot make that happen merely by liking the idea."
{n}There is more heat in her answer than in the original proposal. She notices it, draws a breath, and leaves the notice where both of you can see it.{/n}
"I should have asked before putting your title here. I can remove it. I am less persuaded that asking people to help pay for a pleasant evening will spoil it. Tell me which part you object to. I would rather argue with your actual objection."''',
      c('"The public role. I want some hours when I am not what brings people through the door."', "private_objection"),
      c('"The price. A person without spare coin may enjoy a game as much as we do."', "price_objection")),
    n("name", "Arsinoe", '''{n}She reads the line again, this time as if it belonged to someone else's notice.{/n}
"Yes. Some will come to look at you. Some will want something from you. And some will assume that the invitation is an order, however attractively we print it."
{n}She crosses out the line. No replacement goes above it.{/n}
"I was thinking of a full courtyard. You were thinking of the people in it. We can still have the gathering without advertising your presence."
{n}She turns the cost calculation toward you.{/n}
"There remains this less flattering part. Neral must be paid. I can pay her myself for one evening, or we can ask those who come to contribute. I will not obtain a cheaper room by explaining whose companion I am."
{n}She says it firmly, looking at her own handwriting.{/n}''',
      c('"A small charge could work if people know exactly what they are buying."', "terms"),
      c('"I would prefer a small private invitation this time."', "terms")),
    n("charge", "Arsinoe", '''"Because Neral is spending her evening here instead of upstairs with her supper. Because the lamps burn oil. Because I would like this to happen again without requiring a generous person's purse every time."
{n}Arsinoe taps the total, not hard, but with unmistakable conviction.{/n}
"Neral repairs locks for people trying to keep a roof over their heads in a demon war. I will not ask her to lose an evening's wages for my amusement. Some people will stay away because they cannot pay. I have not solved that part."
{n}For a moment she looks tired of the calculation. Then she draws the paper back.{/n}
"We could have a private evening instead. Invite only as many as we can comfortably host. I would enjoy it, although it would not become the little establishment I was imagining. I want you to understand that I was imagining one. It was not merely a device to give you a pleasant surprise."''',
      c('"Then let us discuss what we can actually offer."', "terms")),
    n("private_objection", "Arsinoe", '''"That I can understand. I came here to be useful. You cannot cross a courtyard without someone deciding how to make use of you."
{n}She strikes your title from the notice.{/n}
"I still want other company sometimes. People who are neither buying a scroll nor asking me to officiate. I am quite capable of being lonely in a place where everyone knows where to find me."
{n}She says it the way she would report a leak: a fact, to be dealt with.{/n}
"Will you come to an evening where you are one of the players, and I am one of the people who arranged it? Or would you prefer that we keep this first gathering small enough to know everyone we invite? Either is possible. I would rather choose one honestly than spend the evening regretting the other."''',
      c('"Let us settle the size and the price together."', "terms")),
    n("price_objection", "Arsinoe", '''"They may. And I do not want to pretend that a low price is no price."
{n}She looks toward the street before continuing.{/n}
"But I will not tell Neral to work for our good intentions. If we choose a public evening, I can pay for two unclaimed places as well as yours and mine. No names on those places. No announcement about who needed them. That is what I can afford to promise tonight."
{n}Two places would be sold at the stated price; Arsinoe would cover the other four, including yours and hers, making six in all.{/n}
"Or I invite a small group and pay Neral for the whole evening myself. You can help me carry the chairs. It will be a pleasant private evening, and we can stop asking it to solve the question of every evening after it."''',
      c('"Show me both versions."', "terms")),
    n("terms", "Arsinoe", '''{n}You work through the two arrangements. For the public gathering, Neral will collect two modest fees from guests; Arsinoe will pay for two places available without explanation to anyone who asks. Arsinoe will also pay for your place and hers, making six. The notice will promise a game and a reading, with no mention of your attendance. People will be free to leave before paying if the prospect does not suit them.{/n}
{n}For the private gathering, Arsinoe will invite Neral and three acquaintances from her ordinary business, making six with the two of you. Arsinoe will pay Neral for the room herself. Nobody will be expected to buy anything afterward.{/n}
"Whichever we choose, I will tell Neral tomorrow," {n}Arsinoe says.{/n} "And I will leave the next hour we spend alone entirely unprofitable. You may hold me to that."
{n}Arsinoe checks the draft for any remaining mention of your attendance and strikes it out. The corrections remain visible; she does not replace the sheet with a tidier one.{/n}''',
      c('"Try the public evening, with the two places you described."', flags=("arsinoe.evening_public",)),
      c('"Let us host the smaller private gathering."', flags=("arsinoe.evening_private",))),
], "arsinoe_borrowed_court")


s("arsinoe_courtyard_company", "Company after closing",
  '"Is everything ready for the courtyard evening?"', [
    n("start", "Arsinoe", '''{n}Neral has hung a lamp at each end of the awning. The workshop is shut, though the courtyard still smells faintly of hot metal. Arsinoe stands on a low stool to straighten a wick, and hands you the chimney before you can offer advice from the ground.{/n}
"There. Now we shall be able to see our terrible decisions."
{n}Neral pockets the coins Arsinoe has brought for the agreed arrangement, then sets out the last chair. The game waits on one table; a small stack of reading material lies on the other. Cups and a jug occupy the least level surface, which Neral has corrected with a folded scrap of leather.{/n}
{n}A patrol passes the courtyard without stopping. Arsinoe climbs down from the stool and checks the six places once more.{/n}
"We should begin before I think of another improvement."''',
      c("Welcome the arriving customers.", "public", requires=("arsinoe.evening_public",)),
      c("Welcome the invited company.", "private", requires=("arsinoe.evening_private",))),
    n("public", "Arsinoe", '''{n}The two paid guest places fill. One guest is a wheelwright, who pauses to admire the workshop's door hinge before sitting down. One of the two places Arsinoe has covered goes to a quiet older laundress; the other goes to a young courier who asks twice whether he needs to give his employer's name. Neral tells him he needs only a chair.{/n}
{n}A paying guest recognizes you and begins,{/n} "Since I have the opportunity..."
"You have the opportunity to choose a brass merchant," {n}Arsinoe says, offering him the board.{/n} "Official business keeps different hours."
{n}He considers arguing, notices the other guests watching, and selects the locksmith instead.{/n}
{n}The courier leaves his satchel beneath his feet. The laundress chooses the cloth merchant without asking what it does. Arsinoe looks to you for the rules you agreed to use.{/n}''',
      c("Explain the reconstructed toll rule.", "original_game", requires=("arsinoe.game_reconstructed",)),
      c("Explain the missing rule and resume the recorded position.", "uncertain_game", requires=("arsinoe.game_unresolved",)),
      c("Explain the courtyard version.", "house_game", requires=("arsinoe.game_house",))),
    n("private", "Arsinoe", '''{n}Arsinoe's acquaintances arrive separately: an older laundress who sometimes brings her mending, a courier who delivers purchases, and a wheelwright who once spent most of an afternoon explaining the disadvantages of three kinds of axle. Neral brings her own cup and takes the sixth place.{/n}
"I was promised no professional questions," {n}she tells the wheelwright.{/n}
"I have brought none."
{n}"You are looking at the hinge," Neral says.{/n}
{n}"It is a handsome hinge," the wheelwright replies.{/n}
{n}The small company laughs. There is less distance between the chairs than you expected, and no easy way to remain a guest of honor. Arsinoe gives you the cloth merchant and asks whether you remember where it belongs.{/n}
{n}The courier settles his satchel beneath his feet. Neral turns the board so that nobody has to read its streets upside down. It is time to explain which rules this company will inherit.{/n}''',
      c("Explain the reconstructed toll rule.", "original_game", requires=("arsinoe.game_reconstructed",)),
      c("Explain the missing rule and resume the recorded position.", "uncertain_game", requires=("arsinoe.game_unresolved",)),
      c("Explain the courtyard version.", "house_game", requires=("arsinoe.game_house",))),
    n("original_game", "Arsinoe", '''{n}The recovered distinction between the cloth seller and the locksmith produces immediate objections from everyone who has chosen neither. Arsinoe shows them the surviving marks and your copied explanation.{/n}
"You may dislike the toll. You must at least dislike the correct toll."
{n}The laundress proves exceptionally good at making other people's routes inconvenient. A guest suggests that her trade gives her an unfair advantage; she replies that he is welcome to spend tomorrow washing shirts and test the theory.{/n}
{n}Your earlier discovery saves the company a lengthy argument. It does not save Arsinoe from losing two merchants in succession. She leans back, inspecting the board as if it has broken a private agreement with her.{/n}
"I wanted witnesses to other people's mistakes. This is a discouraging start."
{n}There is time for a second round before the reading. The company chooses its pieces with considerably more care.{/n}''',
      c("Play on until the reading.", "reading")),
    n("uncertain_game", "Arsinoe", '''{n}You set up the unfinished position from your sketch and explain that the original privilege remains unknown. The company will keep the disputed route closed.{/n}
{n}The resulting game takes most of the available time. Three people offer to improve it, and two of their suggestions would immediately favor their own pieces. Arsinoe insists that any change wait until the next round.{/n}
"We may be ignorant. We need not be so obliging about it."
{n}At last the courier finds a way to clear the central square. You finish the old game with a narrow loss and an entirely disproportionate sense of relief. Arsinoe folds the sketch, writes FINISHED across its back, and keeps it.{/n}
{n}The extra play has eaten into the reading time. She tells the company so and makes them choose one piece rather than gallop through three.{/n}''',
      c("Choose the evening's reading.", "reading")),
    n("house_game", "Arsinoe", '''{n}The rule granting each merchant one use of the short road sounds simple until six people begin remembering whose turn came before whose. Neral finds a shallow dish. Used tokens go into it, and the first dispute ends before anyone raises a voice.{/n}
{n}Arsinoe writes this addition beneath COURTYARD RULES.{/n}
"We now owe Neral credit as well as rent."
{n}The courier wins by allowing two rivals to block each other while he takes the long road. He appears almost apologetic about it, until the laundress tells him to enjoy his victory while he has one.{/n}
{n}Your improvised game belongs comfortably to this table now. Someone asks whether the rules may be copied. Arsinoe agrees, then hands the request to you to answer as well.{/n}
{n}You leave the board set up for anyone who wants another round after the reading.{/n}''',
      c("Begin the reading.", "reading")),
    n("reading", "Arsinoe", '''{n}The guests move their chairs. Arsinoe gives the lamplight to whoever holds the page, then sits beside the table with her own cup between both hands.{/n}''',
      c("Read the ridiculous adventure you shared with Arsinoe.", "story_reading", requires=("arsinoe.interest_stories",)),
      c("Let Arsinoe read while you follow the game's last disputed move.", "game_reading", requires=("arsinoe.interest_games",))),
    n("story_reading", "Arsinoe", '''{n}The princess reaches her impossible window. Arsinoe takes over her lines without being asked. Her delivery is solemn enough that it takes the company a moment to understand how little she believes the hero.{/n}
{n}Neral asks about the aunt. You and Arsinoe exchange a look, then give her the version with the boat. The laundress objects to selling the silver too cheaply. The wheelwright wants to know how the boat was maintained.{/n}
"We have found our audience," {n}Arsinoe murmurs.{/n}
{n}For a few minutes you are not presenting anything to Drezen. You are trying to keep a preposterous story alive while six sensible people make it more preposterous.{/n}
{n}Then the courier sees the hour and stands abruptly. His satchel catches a chair leg; his cup falls. Nothing breaks, but the reading stops while he apologizes and gathers his things. He has a delivery he cannot postpone, and has stayed longer than he meant to.{/n}''',
      c("Help him free the satchel.", "leaving")),
    n("game_reading", "Arsinoe", '''{n}Arsinoe reads a passage from her travel book about a host who boasted of the quiet in his establishment while his poultry fought beneath the guests' window. Her voice grows increasingly dignified as the account grows less so.{/n}
{n}You turn a brass merchant in your fingers. The courier leans over to show you the move he thinks you missed. Arsinoe notices both of you studying the board and stops at the exact moment the host begins explaining the noise.{/n}
"Shall I leave him defending his chickens until you have finished?"
{n}You put the merchant down. The company laughs, and you give her the attention you would have wanted for your own interest. She continues without another rebuke.{/n}
{n}Before the passage ends, the courier sees the hour and rises in a hurry. His satchel catches a chair; his cup spills. He has a delivery still to make. The little gathering rearranges itself around his apologies.{/n}''',
      c("Help him free the satchel.", "leaving")),
    n("leaving", "Arsinoe", '''{n}The courier insists on wiping the table before leaving. Arsinoe finds a cloth and lets him help.{/n}
"Come again if you can," {n}she says.{/n}
"If it is earlier. I thought I could stay for both."
{n}After he has gone, the question remains. Neral could open the courtyard an hour earlier on another evening, but only if the gathering used the smaller side table while she finished working. The hammer would occasionally interrupt. Keeping this hour would preserve the quiet and exclude the courier from part of it.{/n}
{n}Arsinoe looks at the remaining company.{/n}
"I like the quiet. I also asked people to come together. I should like to hear what you think before I choose for everyone."
{n}Neral, from her doorway, makes it plain she does not care which, so long as somebody decides before her supper goes cold.{/n}''',
      c('"Try the earlier hour next time. We can stop speaking while Neral works."', "earlier"),
      c('"Keep this hour. Give the courier a shorter game before his delivery when we can."', "quiet")),
    n("earlier", "Arsinoe", '''{n}Neral agrees to the earlier trial. The wheelwright cannot promise to attend it. The laundress prefers it.{/n}
{n}Arsinoe writes the new time on the back of the notice.{/n}
"One trial. Then we ask again."
{n}The reading resumes. Twice someone glances toward the empty chair, but nobody leaves it ceremonially untouched. Neral moves it out of the way so that the remaining company can sit closer.{/n}
{n}When the lamps are put out, Arsinoe checks the courtyard for dropped pieces. You find the key-bearing merchant under the leg of a table.{/n}
"An independent trader," {n}she says, holding out the cloth.{/n} "He has been evading every arrangement we made."
{n}You wrap the board together. She knots the green cloth twice, as if the merchants might otherwise escape before the next meeting.{/n}''',
      c("Walk back with Arsinoe.", flags=("arsinoe.company_earlier",))),
    n("quiet", "Arsinoe", '''{n}Neral keeps the later hour. The laundress would have preferred an earlier one, and says so. Arsinoe writes her complaint on the back of the notice, beneath the chairs.{/n}
"I will offer him a short game before his route when I can spare the time. I cannot promise it every evening."
{n}The reading resumes in the quiet courtyard. There is room to hear the small changes in Arsinoe's voice, and enough time afterward for the company to disagree about the story's ending.{/n}
{n}When the last guest leaves, she checks beneath each table for missing pieces. You find the key-bearing merchant by a chair leg.{/n}
"At least one of us has found a private evening," {n}she says.{/n}
{n}She wraps the board carefully, then puts the courier's unused cup back on the shelf. Neral waits by the courtyard gate with the keys.{/n}''',
      c("Walk back with Arsinoe.", flags=("arsinoe.company_quiet",))),
], "arsinoe_price_of_an_evening", delay=24)


s("arsinoe_another_hour", "What the evening cost",
  '"How did the next courtyard gathering go?"', [
    n("start", "Arsinoe", '''{n}Arsinoe has put the green-wrapped board beneath her table. A fresh slip of paper protrudes from the cloth. She follows your glance and takes it out.{/n}
"A record. Not a bill for you."
{n}One side lists the courtyard's costs. The other contains changes to the game, three suggestions for readings, and a complaint about the height of the chairs.{/n}
"Neral says the chairs are exactly the height they were when we accepted them. I fear her case is strong."
{n}She makes space beside the paper. Her manner is easy, but she has plainly been considering more than chair legs.{/n}
"Neral was paid, and we managed an evening while Drezen still needed defending. I count that as a useful trial."''',
      c('"Did the earlier hour help?"', "earlier", requires=("arsinoe.company_earlier",)),
      c('"Did keeping the quiet hour work?"', "quiet", requires=("arsinoe.company_quiet",))),
    n("earlier", "Arsinoe", '''"The courier finished a complete game. He was delighted, except that he lost. The wheelwright could not come. Neral interrupted a particularly fine sentence with a hammer, and I had to begin it three times."
{n}Arsinoe taps the list of readings.{/n}
"I enjoyed the game. I did not enjoy reading over the workshop. I had expected to be more generous about the noise. It turns out that I like people to hear the sentences I have chosen."
{n}She has told Neral that the earlier hour suits games better than readings. Neral considers this a promising discovery, having never offered to conduct her work silently.{/n}
"I am willing to keep an occasional early game. I want the readings later. That means some people will miss them. I have stopped expecting one invitation to fit every life in the courtyard. It was a rather grand expectation for six chairs."''',
      c('"And the arrangement for paying?"', "accounts")),
    n("quiet", "Arsinoe", '''"The reading went well. The laundress told a story of her own, and Neral stayed after putting out the workshop lights. I liked it very much."
{n}Arsinoe folds one corner of the paper, then smooths it again.{/n}
"I offered the courier a game before his route. He could spare a few minutes; I could not finish a round in them. We left the board set up behind my table, and completed it on his next visit. He won. He has been extremely courteous about reminding me."
{n}She looks at the wrapped board.{/n}
"That is company too. But it does not replace sitting with everyone else. I asked whether he wanted us to change the reading hour. He said he would rather we kept playing when we could. I believe him. I still mean to ask again if his work changes."
{n}She sounds pleased with the evening, and faintly annoyed about the courier, and does not try to reconcile the two.{/n}''',
      c('"And the arrangement for paying?"', "accounts")),
    n("accounts", "Arsinoe", '''{n}She turns the paper over. The sums are small enough to fit in a few lines, and substantial enough to matter to the people who paid them.{/n}''',
      c("Examine the public gathering's account.", "public", requires=("arsinoe.evening_public",)),
      c("Ask about the cost of the private gathering.", "private", requires=("arsinoe.evening_private",))),
    n("public", "Arsinoe", '''"The two paying guests covered their places. I paid for yours, mine, and the two unclaimed chairs as agreed. Neral received her full price. Nobody made a profit, and nobody had to explain why they took an available chair."
{n}Arsinoe points to a second, smaller figure.{/n}
"For the next evening, one of the original guests offered to cover a place. I accepted, on the same condition. No names announced, no gratitude collected at the door. It means I can afford to try this occasionally. It does not mean we have founded an institution."
{n}The guest who wanted official business has not returned. Arsinoe heard that he found the evening disappointing.{/n}
"He probably did. We sold him a game and gave him one. I will not improve that bargain by giving him access to you."
{n}She puts the account aside.{/n}
"There is one other expense I did not write down. I spent most of the first evening watching whether everyone else enjoyed it. I scarcely played with you."''',
      c('"I missed that too."', "alone"),
      c('"I enjoyed seeing you with your guests. But I would like another hour of our own."', "alone")),
    n("private", "Arsinoe", '''"I paid Neral for the evening. I can afford to do that occasionally, as I promised. I cannot afford to make every idle evening a gathering."
{n}She taps the list of names on the other side.{/n}
"The wheelwright has offered his own room for a future reading. It is smaller, and we must not knock anything into the glue pot. I accepted an invitation to look at it. One evening. I will not promise his room to half the market."
{n}She smiles, a little ruefully.{/n}
"You were right that a private evening could be enough. I still like the idea of something more regular. For now, I would rather have the company than exhaust myself arranging its ideal future."
{n}She folds the account.{/n}
"And I owe you the hour I said I would leave unprofitable. I spent most of that first evening being a host. I enjoyed it, but I missed sitting beside you without listening for an empty cup."''',
      c('"I would like that hour."', "alone"),
      c('"You need not owe it to me. Invite me because you want it."', "invitation")),
    n("alone", "Arsinoe", '''"Good. Then let us choose something before I decide it needs three lamps and a printed announcement."
{n}She puts the account away and rests her hands on the table.{/n}
"I want to hear you disagree with a story. Or watch you make a clever move and pretend not to be pleased with yourself. I have learned that I enjoy both."
{n}She says it lightly, and then does not smile, so that you will know she meant it.{/n}
"I have spent all day arranging chairs for people who may not come. I would rather spend the next evening with you. So: come back on an ordinary day, Commander, and let me have you to myself."
{n}She names an evening when her business can close at its usual hour.{/n}''',
      c('"Then I will come for that evening."', flags=("arsinoe.private_hour_invited",))),
    n("invitation", "Arsinoe", '''{n}Arsinoe considers the distinction, then inclines her head.{/n}
"Very well. I want another evening with you. I want to stop being responsible for whether everybody in the room has a good time. Two people, one table, and neither of us a host."
{n}A customer passes outside. She lets him continue toward the market without turning the invitation into business.{/n}
"I also want to finish a story without being interrupted by a hammer. Or a courier. Or my own excellent ideas. I am willing to tolerate some interruption from you."
{n}Her smile returns, warmer now.{/n}
"Come when I close on the evening we choose. Bring yourself. Anything else should be small enough to fit on a table."
{n}You settle on a day. She writes your arrangement on a separate scrap and keeps it apart from the courtyard's accounts.{/n}''',
      c('"I will be there."', flags=("arsinoe.private_hour_invited",))),
], "arsinoe_courtyard_company")


s("arsinoe_the_unprofitable_hour", "No notice on the door",
  '"I have come for our evening."', [
    n("start", "Arsinoe", '''{n}Arsinoe closes at the hour you agreed. She checks the fastening once, then takes you to a small room behind her working space. A clean cloth covers the table. There are two cups, something cold to drink, and no account waiting beneath either plate.{/n}
"I have been very restrained. You may admire it."
{n}She has removed the outer layer of her formal robes. The simpler garment beneath is no less carefully kept, but she sits in it without attending to every fold. Her hair catches on a small fastening; she frees it and leaves the clasp beside the lamp.{/n}
"If the alarm bell rings, I shall answer it. Until then, I am off duty."
{n}Outside, someone calls a price across the street. Arsinoe pours your drink and lets the call pass unanswered.{/n}''',
      c("Set out a game.", "game", requires=("arsinoe.interest_games",)),
      c("Open the adventure story.", "story", requires=("arsinoe.interest_stories",))),
    n("game", "Arsinoe", '''{n}You choose the simple paper board from your first afternoon, or as close to it as either of you remembers. Arsinoe insists on a fixed gate. You agree, after extracting a promise that she will not call the moving one visionary when it favors her.{/n}
{n}The first round is quick. The second develops an awkward middle in which both of you would prefer the other to make a mistake. Arsinoe reaches for a piece, stops, and looks up at you.{/n}
"I had a plan to spend this evening being effortlessly charming. I now discover that I would rather win."
{n}She makes the move. It is a good one. You spend a comfortable stretch of silence trying to undo its consequences, while she drinks and makes no effort to rescue you from them.{/n}
{n}When the round ends, she leaves the pieces where they fell and turns her chair toward yours.{/n}''',
      c('"Your confidence is touching. Was the evening what you wanted?"', "answer")),
    n("story", "Arsinoe", '''{n}You find the hero at the window and read on. He leaps for a roof much too far away, then survives by means of a hanging banner that neither of you remembers being mentioned. Arsinoe examines the earlier page to make certain the author has not earned this escape by stealth.{/n}
"No banner. I am inclined to leave him on the pavement."
"The princess has endured worse disappointments. She has listened to him speak."
{n}You trade parts. Your princess demands an explanation; Arsinoe's hero offers one so magnificently inadequate that you both have to stop. The room feels smaller in the pleasant way a room does when laughter no longer needs to carry to anyone outside it.{/n}
{n}Eventually she marks the page with a clean slip and closes the booklet.{/n}
"We must leave them something to be foolish about next time."
{n}She sets it beyond the reach of your cups and turns her chair toward yours.{/n}''',
      c('"Was the evening what you wanted?"', "answer")),
    n("answer", "Arsinoe", '''"Yes. Although I expected to be better company. Over these evenings I have argued over rules, complained about an author, and made you wait while I thought."
{n}She watches your expression, then smiles at the answer she finds there.{/n}
"You need not list these as virtues. I enjoyed myself. I hope you did too."
{n}The lamp has burned lower. Arsinoe adjusts it, bringing the light back without making it brighter than the little room needs.{/n}
"I do not want to leave Drezen merely because I have managed to make myself useful here. That has often been the moment when I began looking elsewhere. There was always somewhere I could do more."
{n}Her fingers rest beside the abandoned clasp.{/n}
"I am beginning to dislike what I would have to pack away. The board. The unfinished book. A room I have learned to arrange for someone else's comfort as well as my own. That is a new difficulty. I am not asking you to solve it tonight."''',
      c('"You can keep a life here as well as a purpose."', "pace"),
      c('"I cannot promise where the war will take me. I am glad we have this evening."', "uncertain")),
    n("uncertain", "Arsinoe", '''"So am I. I would not thank you for promising me a road you cannot yet see."
{n}She draws the cups closer to the center of the table, making room between you.{/n}
"When I spoke of staying, I did not mean that you must remain in this room to make it worthwhile. I have my work, and Neral will continue to overcharge me for uneven chairs. I am forming opinions about people who are perfectly capable of disappointing me in your absence."
{n}Her tone is dry, but there is no retreat from the affection in what she has said.{/n}
"I would like you to return when you can. I would like to have something to tell you when you do. That is as far as I need to look tonight."
{n}Outside, the market's last voices have thinned to footsteps. Neither of you rises at once.{/n}''',
      c("Stay beside her a little longer.", "pace")),
    n("pace", "Arsinoe", '''{n}Arsinoe lets the quiet settle. For once she has no plan for the next hour, and seems to enjoy the novelty.{/n}''',
      c('[Kiss her.]', "kiss", requires=("arsinoe.courting",)),
      c("Offer her your hand and remain beside her.", "hand", requires=("arsinoe.courting",)),
      c('"I like finding our way slowly."', "slow", requires=("arsinoe.slow",)),
      c('"I am glad we made time for this, my friend."', "friend", requires=("arsinoe.friendship",))),
    n("kiss", "Arsinoe", '''{n}She sees it coming and does not look away. When you lean toward her, she meets you with one hand against your cheek. The kiss is unhurried, warm with the pleasure of an evening already shared. She draws back only far enough to look at you, then kisses you again of her own accord.{/n}
"I am pleased we kept this hour for ourselves."
{n}Her hand slips from your cheek to your shoulder. You stay close, discovering the comfortable angle of two chairs that were never designed for this use. She laughs softly when one complains beneath you and pulls you toward the sturdier one.{/n}
{n}The rest of the hour needs little conversation. When it is time to leave, she retrieves her clasp but does not put it on until she has walked you to the door.{/n}
"Come back with something else you like," {n}she says.{/n} "I have begun to trust your questionable taste."''',
      c("Kiss her good night and leave her to rest.", flags=("arsinoe.continuation_kept", "arsinoe.continuation_kiss"))),
    n("hand", "Arsinoe", '''{n}Her fingers close around yours. She shifts her chair until neither of you has to reach, and rests your joined hands on the edge of the table.{/n}
"This is comfortable," {n}she says.{/n} "I recommend remembering it before we buy better furniture."
{n}You remain there while the lamp burns lower, talking when something occurs to you and leaving the pauses alone. Arsinoe tells you which reading she wants to try with the courtyard company, then catches herself preparing a whole evening and laughs.{/n}
"Tomorrow. They can have tomorrow's excellent ideas."
{n}She gives your hand a small squeeze. When you begin to rise, she holds it a moment longer and finishes the story she was telling.{/n}
{n}At the door she keeps your hand for a moment longer.{/n}
"Bring me another interest next time. I intend to develop a much better informed opinion of you."''',
      c("Wish her good night.", flags=("arsinoe.continuation_kept",))),
    n("slow", "Arsinoe", '''"So do I. I have had enough journeys in which I saw very little because I was so pleased with my progress."
{n}She does not reach across the remaining space. Instead she picks up the clasp, turns it once in her fingers, and sets it down again.{/n}
"Stay until we finish our drinks. We need not decide what the next evening will be while this one is still happening."
{n}You talk about the game, the courtyard, and the things you would like to do if an afternoon ever becomes unexpectedly free. Some are impractical. Arsinoe refuses to discard them merely for that reason.{/n}
{n}When you finally rise, she asks what you might bring next time. Neither of you settles on an answer before reaching the door.{/n}
"Choose something we can disagree about for longer," {n}she says.{/n} "I seem to enjoy that rather more than I expected."''',
      c("Agree to another evening, without hurrying it.", flags=("arsinoe.continuation_kept",))),
    n("friend", "Arsinoe", '''"As am I. I have missed this sort of company more than I realized."
{n}She divides the last of the drink between your cups, giving you the fuller one with the absent fairness of someone who has stopped keeping a formal account of hospitality.{/n}
"You have given me an unfortunate appetite for bad literature and small victories. I shall have to explain to Neral why a priest of Abadar spent so long disputing a toll owed by a brass merchant."
"She would believe that. We must be more honest with her."
{n}The laughter lasts into the tidying. Arsinoe lets you help with the cups and does not turn the offer into a debt. At the door, she reminds you that the next courtyard invitation will be an invitation, not a duty.{/n}
"And this room is available for quieter company. Come when you have a story, or when you would rather listen to one."''',
      c("Thank her for the evening and say good night.", flags=("arsinoe.continuation_kept",))),
], "arsinoe_another_hour")


# Authored round-2 situation: her private expenditure precedes her invitation.
_another = next(s for s in SCENES if s["Id"] == "arsinoe_another_hour")
_a = {page["Id"]: page for page in _another["Nodes"]}
_a["accounts"]["Text"] = '''{n}Arsinoe turns the paper over. Neral's receipt is pinned to it. Beneath the workshop charge, someone has written TEMPLE MONEY? in a different hand.{/n}
"A guest thought the temple had paid for our company. Another thought we charged him twice. Neral showed him his one receipt. I showed him mine. He preferred his first account of the evening."
{n}She draws a line beneath her own expenditure.{/n}
"The temple pays for healing and worship. My share pays for my pleasures. Neral has received every coin we promised her."'''
_a["alone"]["Text"] = '''{n}She puts away Neral's paid account, then takes out a wrapped bottle and a strip of fine cloth. The cloth gleams gold against her wrist.{/n}
"Good drink. Silk I certainly did not need. I bought both with my own money, after paying my share. I have decided to spend the rest badly."
{n}Her eyes move from the silk to you.{/n}
"The others can arrange tomorrow's reading. Neral will keep them from borrowing her good tools as props. I want you alone, without somebody trying to buy an audience between two moves."
{n}She names an evening when she can close at the usual hour.{/n}
"Come then. I intend to enjoy what I bought."'''
_a["invitation"]["Text"] = '''{n}Arsinoe folds the receipt and tucks it away. A parcel of silk and a bottle wait beneath it.{/n}
"Then I invite you because I want you. Neral has her money, and the guests can choose their own reading next time. I have bought myself something beautiful to wear and something good to drink. Neither appears in the temple's accounts."
{n}She holds the silk against her throat, watching you.{/n}
"Come when I close. I would like your attention for rather more than my choice of chairs."'''

_hour = next(s for s in SCENES if s["Id"] == "arsinoe_the_unprofitable_hour")
_h = {page["Id"]: page for page in _hour["Nodes"]}
_h["start"]["Text"] = '''{n}Arsinoe shuts the shop at the agreed hour. Behind it, the table holds two cups, the bottle she showed you and a game beside an open book. The window sticks when she tries to open it. She leaves it for tomorrow.{/n}
"If the alarm sounds, I shall answer. Until then, somebody else can watch Drezen's walls."
{n}The silk at her throat is the cloth she bought. She notices you looking, and takes her time removing the outer robes. A clasp catches her hair; she frees it and puts it beside the lamp.{/n}
"Well chosen, I think. I mean to enjoy your opinion of it."'''
_h["answer"]["Text"] = '''"Yes. I wanted an evening I did not have to arrange for everyone else."
{n}She pushes the cups aside and turns toward you. Her knee brushes yours beneath the table.{/n}
"I spent half the reading waiting to be alone with you. That was discourteous to the author. Fortunately, he was not there."
{n}She leaves the clasp where it lies.{/n}
"I shall have to decide what to pack when I next travel. Tonight I would rather stay here."'''
_h["uncertain"]["Text"] = '''"Then we have tonight. I would rather have that than a grand promise you cannot keep."
{n}She moves her chair closer. Outside, a patrol's boots pass the shutter; she listens until they turn toward the wall, then gives you her attention again.{/n}
"I have work tomorrow. So have you. I expect we can survive wasting the rest of this evening."'''
_h["kiss"]["Text"] = '''{n}Arsinoe meets your kiss with her hand against your cheek. The second is hers; she holds you close until the chair creaks beneath you. She laughs against your mouth and gets to her feet, drawing you up with her.{/n}
"This furniture is intolerable. I should have spent more on it."
{n}She kisses you again beside the table. The book lies open, the drinks unfinished. Her fingers catch in your collar.{/n}
"You could stay. I have no intention of reading another page tonight."'''
# The old kiss-and-leave exit keeps its position and effects. Overnight is optional.
_h["kiss"]["Choices"].append(c('"Then I will stay."', "arsinoe_the_unprofitable_hour.explicit.1"))
# Explicit slot U: her chosen finery, unfinished drink, initiative; no future promise.
_hour["Nodes"].extend([
    n("arsinoe_the_unprofitable_hour.explicit.1", "Arsinoe", '''{n}Arsinoe leaves the book open and draws you to the bed. She loosens the silk at her throat, then catches your hand before you can help.{/n}
"I chose it for you to admire. You have barely looked."
{n}She takes her time with the last clasp, watching your face. When you kiss her she forgets the cloth, lets it fall, and pulls you down beside her. Her hand stays at your collar; the next kiss is hers.{/n}
"The shop can wait until morning."''', c("Continue", "private_morning")),
    n("private_morning", "Arsinoe", '''{n}In the morning, Arsinoe searches beneath the bed for her clasp. You find it caught in your discarded collar. She takes it, then bends to kiss you before pinning up her hair.{/n}
"I chose it carefully. Next time I shall choose something harder to lose."
{n}A customer knocks at the shutter. She looks toward the sound, then gives you one more kiss.{/n}
"Yes, I heard him. Come back when there is no queue. I want to finish our argument."
{n}She opens the shop herself. The bottle remains half full upstairs.{/n}''',
      c('[Leave her to her customers.]', flags=("arsinoe.continuation_kept", "arsinoe.continuation_kiss", "arsinoe.unprofitable_night_shared"))),
])

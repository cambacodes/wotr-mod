"""Unexported Arsinoe courtship opening; native bindings require integration review."""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
RELATIONSHIP = dict(
    Title="A city worth staying in",
    Description="Arsinoe has invited me to see more of Drezen with her. There is more to her company than the business that first brought us together.",
    Objective="Make time for Arsinoe",
    Guidance="Speak to Arsinoe in Drezen when she is free of her ceremonial duties. Allow time between visits.",
    StartedFlag="arsinoe.started", ClosedFlag="arsinoe.closed", CommittedFlag="arsinoe.committed",
    UnavailableFlags=["arsinoe.victims_revived", "swarm", "true_lich"], FailureFlags=[],
)
ETUDES = {
    "arsinoe.capital": "3f3fbb973a4ffee47956b4c7714c939a",
    "arsinoe.victims_revived": "6d3fb96f9b60c0449a01add4be5c4a49",
}
INTEGRATION_REQUIREMENTS = {
    "Implemented": False,
    "Unit": "a609ed9b2205d034bb3bb04d2a255681",
    "VendorDialogue": "d5adc0bbbad5f054098b527cf9cc64f1",
    "CapitalEtude": "3f3fbb973a4ffee47956b4c7714c939a",
    "NativeDialogueConditions": "c4fa13c72fc350d4bae7431242eb095a",
    "Pending": [
        "Verify staged relationship registration, capital actor and VictimsRevived guards with native bindings and managed construction.",
        "Verify live contact, interruption and native quest/cutscene ownership in game.",
        "Bind actual Lann ceremony and Seelah/Arueshalae history for optional contextual responses.",
        "Implement character-specific mythic access, refusal and attainable Trickster restoration.",
        "Review real engine skill-check construction, outcomes and save persistence before export.",
    ],
}


def s(id, title, entry, nodes, requires=(), delay=24):
    if id == "arsinoe_city_on_paper":
        for page in nodes:
            page["Portrait"] = "ArsinoeShop"
    SCENES.append(scene(id, title, "Arsinoe", 3, entry, nodes,
                        requires=("arsinoe.capital", *requires), forbids=("arsinoe.closed",),
                        delay=delay, optional=True, Relationship="arsinoe",
                        Areas=[DREZEN], Chapters=[3, 5],
                        ContactUnit="a609ed9b2205d034bb3bb04d2a255681",
                        AnswerLists=["ecaf5cfe8087a4f45a2269974f4885c9"]))


s("arsinoe_city_on_paper", "A handsome city", '"What is that picture?"', [
    n("start", "Arsinoe", '''{n}Arsinoe holds a sheet by its corners, keeping it well clear of the edge of her table. Beneath a grandly lettered DREZEN, little figures stroll past an uninterrupted row of handsome houses. Every shutter hangs straight. Every roof is whole.{/n}
"An achievement. Someone has repaired the damage of a demon occupation without troubling a single mason."
{n}She tilts the sheet toward you. Its colors catch the light.{/n}
"A printer brought samples for sale. I bought this one. I was going to return it, but I find that I rather like looking at it. This puts me in an embarrassing position."
{n}A small handwritten note is tucked beneath the picture.{/n}
"He wants to know whether I will recommend it to travelers. I sell useful things to travelers. Apparently that makes me an authority on anything they might carry away."''',
      c('"May I look more closely?"', "picture"),
      c('"Another time. I cannot stay."', abort=True)),
    n("picture", "Arsinoe", '''{n}She lays the sheet on a clean cloth. A harbor fills one corner. Above it, the artist has placed a distant sweep of hills and a particularly ambitious cathedral.{/n}
"The houses are improved, the streets are widened, and the wagons have obligingly become carriages. I can allow an artist a certain latitude. But there is a difference between flattering a city and inventing it."
{n}Her finger stops short of touching the ink.{/n}
"What do you make of it? I have an opinion already. I am trying, with some difficulty, to keep it to myself until you have one."''',
      c('[Knowledge: World] Examine the harbor and architecture for the source of the borrowed view.',
        check=dict(Skill="SkillKnowledgeWorld", DC=24, Success="recognized", Failure="uncertain", CommanderOnly=True)),
      c('"Ask the printer where the picture came from. He should have to answer for it."', "ask"),
      c('"I would rather hear your opinion."', "her_eye")),
    n("recognized", "Narrator", '''{n}The harbor was drawn for a coastal city. The same tide marks appear on every mooring post; the vessels are sea-going, and the broad steps belong to a quay built for a considerable rise and fall of water. A new title has done little to conceal the old composition.{/n}
{n}You point out the marks. Arsinoe bends closer, then looks up at you.{/n}
"Yes. I noticed the ships, but not that. He has been more economical with his engraving than with his praise."
{n}She writes your observation beneath her own on the back of the printer's note.{/n}
"Now I shall ask him about that harbor before he has time to begin talking about artistic freedom."''', c('[Hand the picture back.]', "invitation", flags=("arsinoe.print_source_found",))),
    n("uncertain", "Narrator", '''{n}You compare the towers and try to place the sweep of the shore. Several cities come to mind; none fits well enough to name. The little buildings are too simplified to bear the weight of a confident answer.{/n}
{n}Arsinoe waits until you set the sheet down.{/n}
"Then we shall ask. I will be interested to discover whether the man knows which city he has sold me."
{n}She adds a question beneath her note instead of a place name.{/n}
"I have bought things on a convincing description before. I have also sold scrolls to people who were certain they knew how to use them. I would rather ask him than buy another false view."''', c('[Return the picture.]', "invitation", flags=("arsinoe.print_source_uncertain",))),
    n("ask", "Arsinoe", '''"He shall. Without a regiment at his back, if we can manage it."
{n}She folds the note once.{/n}
"I dislike being taken for a fool. That is a private grievance. Your arrival at his counter would be a public event unless we take care. I want an answer, not a confession obtained by frightening a man who has never spoken to you."
{n}She looks at the flawless roofs again.{/n}
"Besides, I should like to know whether he can make something better."''', c('"We can ask as customers."', "invitation", flags=("arsinoe.print_asked",))),
    n("her_eye", "Arsinoe", '''"I think I paid for the title."
{n}She says it with enough irritation to make it clear that the price still matters to her.{/n}
"I saw a fine city called Drezen, and for a moment I wanted it without examining it. I do that less often than I did when I was young. Less often is an inconvenient distance from never."
{n}She smooths the cloth beneath the paper.{/n}
"The printer has a skill. I should prefer to encourage him to use it here, instead of merely exchanging his lettering. It would be a shame to have a local view made only by people who intend never to look at us."''', c('"Then let us see what he can do."', "invitation", flags=("arsinoe.print_listened",))),
    n("invitation", "Arsinoe", '''"I intend to visit him when I have finished here. His name is Tovin. He has a press behind the shop with the blue lintel."
{n}She rolls the picture around a wooden tube, slowly enough that the paper does not buckle.{/n}
"You could come with me. There will be no healing, no blessings, and no reason for you to stand while I work. I shall even attempt to discuss something other than the needs of the crusade."
{n}Her smile warms.{/n}
"I will not promise to avoid the needs of the city. I enjoy those."''',
      c('"I would enjoy an evening with you."', "warm", flags=("arsinoe.open_interest",)),
      c('"I would like to see what he makes of the real city."', "city")),
    n("warm", "Arsinoe", '''"Would you?"
{n}For the first time she seems to consider the invitation without the printer in it.{/n}
"Then I should choose a better beginning than an argument over a purchase. Still, you have seen the picture. I suspect you would notice if I suddenly lost interest in the matter."
{n}She ties the roll with a narrow ribbon.{/n}
"Come when we can both leave our work behind for a little while. I have not forgotten how to enjoy company."''', c('[Agree to visit when you are both free.]', flags=("arsinoe.picture_invitation", "arsinoe.started"))),
    n("city", "Arsinoe", '''"So would I. There are things worth drawing here even now."
{n}She lifts the rolled picture and measures its extravagant title with her eye.{/n}
"He has made us remarkably prosperous. Perhaps we can persuade him to make us recognizable."
{n}Before you leave, she writes the location on the back of a scrap of paper and gives it to you.{/n}
"For the shop. I have learned not to describe a street by the building that used to stand at its corner."''', c('[Agree to visit when you are both free.]', flags=("arsinoe.picture_invitation", "arsinoe.started"))),
], delay=0)


s("arsinoe_printers_view", "The view he can sell", '"Shall we visit your printer?"', [
    n("start", "Arsinoe", '''{n}Arsinoe has the picture under one arm. She adjusts the fastening at her wrist, notices you watching, and offers the roll for you to carry.{/n}
"Thank you. I have brought the receipt as well. One should not arrive with an argument and forget the evidence."
{n}Outside the shop, a broad-shouldered man is lifting a drying frame through a doorway scarcely wider than the frame. He sees Arsinoe and attempts a bow without putting it down.{/n}
"Please finish that first," {n}she says.{/n}
{n}He does. The frame settles safely inside, and the man wipes his hands on an apron before introducing himself as Tovin.{/n}
"You liked the view?"
"I liked it enough to examine it. May we come in?"''',
      c('[Enter the shop.]', "counter"),
      c('"I must postpone our visit. I am sorry."', abort=True)),
    n("counter", "Narrator", '''{n}Tovin spreads the view beside a stack of uncolored sheets. Arsinoe places her receipt beside it. The sight of both together makes him glance toward the door.{/n}
{n}"Then I am very glad to see you, Commander."{/n}
{n}He says it so quickly that Arsinoe almost smiles.{/n}''',
      c('"Tell us about the coastal engraving beneath this new title."', "source", requires=("arsinoe.print_source_found",)),
      c('"Where did this view come from?"', "explanation", forbids=("arsinoe.print_source_found",))),
    n("source", "Arsinoe", '''{n}Tovin looks at the harbor, then at the mooring posts you indicate.{/n}
"An old plate. Came with the press. I don't know which port it was. The name had already been cut away when I bought it."
"But you knew it was not this city."
"Yes."
{n}Arsinoe lets the answer stand for a moment.{/n}
"Thank you. Now we can discuss what to do with it. Can you draw a view of your own?"''', c('[Hear his proposal.]', "proposal")),
    n("explanation", "Arsinoe", '''"An old plate," {n}Tovin says.{/n} "It came with the press. The name was gone. I added a title and had the sheets colored."
{n}"Did you mean it as a proposal for what Drezen might become?" Arsinoe asks.{/n}
"I meant to sell pictures. Crusaders send them home. Some want their families to believe they have reached somewhere worth defending."
{n}Arsinoe turns the sheet toward him. "Then it matters where they have been. You sold this to me without saying it was an invented view."{/n}
"I can return the money."
{n}"You can. But first I should like to hear whether you can draw." Arsinoe waits for his answer.{/n}''', c('[Wait for his answer.]', "proposal")),
    n("proposal", "Tovin", '''"Buildings. Well enough. Faces give me trouble."
{n}He takes a board from behind the counter. On it is a rough study of his own street. A leaning chimney has been drawn twice, once as it stands and once corrected to the vertical.{/n}
"I was going to make this straight."
"I would begin with the chimney itself," {n}Arsinoe says.{/n}
{n}He laughs, then notices that she is looking seriously at the drawing.{/n}
"I could cut a small plate. This corner, a bit of the next house. Nothing like the big one. A proper view would take longer."
"And these?"
{n}He touches the stack of old prints.{/n}
"If I destroy them, I lose the paper, the color, and the work. If I put another title on, people will think I am making a joke of the city."''', c('"What would you propose, Arsinoe?"', "terms")),
    n("terms", "Arsinoe", '''"He can keep the fantastic city. Label it as such, remove any suggestion that it is an accurate view, and show purchasers the correction before taking their money."
{n}Tovin rubs a finger along the edge of the counter.{/n}
"That will make them harder to sell."
"Yes."
"Or I stop selling these and cut the street. Use the money I set aside for the next batch of paper. I can print fewer copies."
{n}Arsinoe turns to you.{/n}
"He has asked me to recommend his work. I could recommend a plainly described fancy while he learns the real view. I could also ask him to finish an honest local picture first. I would rather see the latter. But the cost is his, and he has offered both."
{n}Tovin nods reluctantly.{/n}
"Either is possible. I want to keep the shop. I also want her to send customers, if they will come."''',
      c('"Recommend the corrected fantasy now. People can decide whether they want it."', "fantasy", flags=("arsinoe.print_fantasy",), forbids=("arsinoe.print_street",)),
      c('"Wait for the street view. Let your recommendation mean you have seen his own work."', "street", flags=("arsinoe.print_street",), forbids=("arsinoe.print_fantasy",))),
    n("fantasy", "Arsinoe", '''"Then show me the corrected title before you offer another copy. And tell your earlier customers what they bought if they return."
{n}Tovin finds a blank strip and tries a few words with his pen. After two attempts, he writes A CITY IMAGINED.{/n}
"Drezen can still be the place where you imagined it," {n}Arsinoe says.{/n}
"I wish someone had suggested that before I paid for the lettering."
{n}Arsinoe examines the strip, then sets it across the false title.{/n}
"This I can recommend as a curiosity. Not as a view."
{n}Tovin thanks her. He keeps the money for the next supply of paper; the little street plate will have to wait until he has spare hours for it.{/n}''', c('[Step outside with Arsinoe.]', "outside")),
    n("street", "Arsinoe", '''"Bring me a proof when it is ready. If I like it, I shall say so. If I do not, I shall tell you why before I tell anyone else."
{n}Tovin counts the sheets on the counter, then covers the old stack with a cloth.{/n}
"Smaller edition, then. I can manage that."
"Keep the money you owe me until you have the proof. We can settle my purchase then."
{n}He looks relieved, although the covered stack still troubles him.{/n}
"I had hoped this would be quicker."
"So had I," {n}she says.{/n} "I came to buy a picture."
{n}Tovin's rueful laugh follows you to the door.{/n}''', c('[Step outside with Arsinoe.]', "outside")),
    n("outside", "Arsinoe", '''{n}Outside, she stops to look back along the street. It is considerably narrower than its imagined counterpart. A basket hangs from an upper window on a rope, and someone below is arguing that its owner has sent down the wrong coins.{/n}
"There. He ought to draw that. The basket, I mean. Perhaps not the argument."
{n}She watches until the coins are exchanged and the basket rises.{/n}
"I am aware that I have taken you to a shop and discussed its goods at length. It is possible that you expected more from my invitation."''',
      c('"I expected to spend time with you. I have."', "pleased"),
      c('"I would enjoy hearing something you have not prepared for a customer."', "traveler")),
    n("pleased", "Arsinoe", '''{n}She looks directly at you.{/n}
"You make it difficult to dismiss that as courtesy."
"Would you prefer to?"
"No. I would prefer to enjoy it."
{n}She shifts the rolled picture to her other hand and offers you her arm for the walk back.{/n}
"There is a roof above the shop. Tovin said we could use the stair if we wanted to see the buildings he is drawing. I should like to go when the light falls along the street. Another evening, if you are willing."''', c('"Another evening."', flags=("arsinoe.printer_met",))),
    n("traveler", "Arsinoe", '''"I once went to a city because I admired its bridges. When I arrived, one was closed, one had collapsed, and the third charged a toll so high that I took a ferry."
{n}She waits until you laugh.{/n}
"I stayed long enough to see the first repaired. It was very fine. I had been ready to leave in disgust, and would have missed it."
{n}She begins walking beside you.{/n}
"Come to the roof above Tovin's shop with me another evening. He has offered us the stair. I can show you something I like about a city without first having to sell it."''', c('"I would like that."', flags=("arsinoe.printer_met",))),
], requires=("arsinoe.picture_invitation",))


s("arsinoe_roofs", "An evening above the street", '"You offered to show me the view."', [
    n("start", "Arsinoe", '''{n}Arsinoe waits at the blue lintel with a covered basket. She is watching the light on the opposite wall. When you approach, she looks from it to your face.{/n}
"We have time. I was beginning to wonder whether I should climb up and admire it all on your behalf."
{n}She lifts the basket a little.{/n}
"Bread, cheese, and something to drink. I discovered that my arrangements for the evening had omitted supper. A rather basic failure for a devotee of civilized living."''',
      c('[Take the basket and climb with her.]', "roof"),
      c('"I cannot stay tonight. I am sorry."', abort=True)),
    n("roof", "Narrator", '''{n}The stair leads to a flat section of roof enclosed by a low parapet. Tovin has brought up two chairs. One has been repaired with a crosspiece of noticeably newer wood.{/n}
{n}Arsinoe tests it before sitting, then places her basket on the broad parapet beside her. She unfolds a small cloth. The cups she takes from it are plain, thin pottery, carefully wrapped to protect their rims.{/n}
{n}"I dislike drinking from a cup that could serve as a bucket," she says when she catches your glance. "You may consider me delicate in this one respect."{/n}
{n}The roofs descend unevenly toward the street. Here and there, a repaired patch catches the light differently from the older tiles.{/n}''',
      c('"Which part would you have him draw?"', "view"),
      c('"You have gone to some trouble for this."', "trouble")),
    n("view", "Arsinoe", '''"That window."
{n}A woman below has wedged a board across her sill and arranged several pots along it. The pots do not match. One holds a plant that has grown tall enough to need a supporting stick.{/n}
"She has very little room. She has made some."
{n}Arsinoe pours for you, then for herself.{/n}
"I like the great buildings too. I will not pretend to prefer a cracked flowerpot to a good colonnade. With demons beyond the walls, she has still planted something she expects to see grow. I should like Tovin to draw that."''', c('[Look along the roofs with her.]', "leaving")),
    n("trouble", "Arsinoe", '''"A reasonable amount. I wanted a pleasant evening, so I arranged one."
{n}She passes you a cup.{/n}
"I have attended celebrations with magnificent vows and nothing fit to drink. I have also seen people make a feast with almost no money because they thought about what their guests would actually enjoy."
{n}Her gaze moves over you, slower than her practical tone would suggest.{/n}
"I thought about what you might enjoy. That part was more difficult. I know a great deal more about what people ask of you."''',
      c('"This will do very well."', "leaving"),
      c('"Ask me. I would rather you knew than guessed."', "likes")),
    n("likes", "Arsinoe", '''"Company or quiet?"
{n}She asks it without hesitation, then raises a hand before you answer.{/n}
"I realize that sounds as though I am offering to leave. I mean, would you rather talk or look at the city for a while? I can enjoy either."
{n}She settles into her chair, cup resting loosely between her hands.{/n}''',
      c('"Tell me something about yourself."', "leaving"),
      c('"Let us look for a while."', "quiet", flags=("arsinoe.roof_quiet",))),
    n("quiet", "Narrator", '''{n}For a while, you eat and watch the light move. A distant call is answered from a window. Somewhere below, a shutter refuses to close until its owner lifts it off its sagging hinge.{/n}
{n}Arsinoe smiles into her cup at the sound of the eventual success. When the bread is nearly gone, she breaks the last piece and offers you half.{/n}
{n}"That was a good answer," she says. "I nearly filled the whole evening before you could give it."{/n}''', c('[Accept the bread.]', "leaving")),
    n("leaving", "Arsinoe", '''"I spent a long time in the Stolen Lands. Long enough to watch a small barony become a place that did not need me in quite the same way."
{n}She turns the cup slowly between her fingers.{/n}
"People ask whether I miss it. Of course I do. I left people I liked, rooms I knew, habits I had grown fond of. But I had wanted the place to prosper. It would have been very strange to resent it for succeeding."
"And when Drezen prospers?"
"I shall have to decide what to do next."
{n}She glances at you.{/n}
"I have not made that decision. I am still learning which streets here remain passable after rain."''',
      c('"I would want to know if you were thinking of leaving."', "tell"),
      c('"I understand the wish to see what lies farther on."', "farther"),
      c('"Must a city need you for you to make a life in it?"', "need")),
    n("tell", "Arsinoe", '''"Then I would tell you."
{n}She sets down her cup before continuing.{/n}
"I do not slip away from people because speaking to them would be uncomfortable. At least, I hope I do not. There are a few farewells I might have handled better."
{n}Her mouth quirks.{/n}
"One woman spoke at such length about everything I ought to pack that I left a day early. I have since regretted both the discourtesy and the spare boots I forgot."''', c('[Stay beside her as the light fades.]', "interest")),
    n("farther", "Arsinoe", '''"Do you? Then you will understand how thoroughly I can enjoy a familiar room and still look up when someone mentions a road I have not taken."
{n}She points beyond the roofs, where the light has begun to leave the walls.{/n}
"I do not require every journey to be dangerous. A safe road, a good inn, and a city worth seeing at the end would please me immensely. I should like to make that kind of journey again."''', c('[Stay beside her as the light fades.]', "interest")),
    n("need", "Arsinoe", '''"No. But it is one of the reasons I choose where to go."
{n}She answers without offense, although she does not soften the point.{/n}
"My calling has taken me to places I would never have chosen for comfort. I am glad it did. I have enjoyed a better life than I would have had by remaining where my work was easiest."
{n}She reaches for the folded cloth beneath the cups.{/n}
"I would not wish to find myself staying somewhere merely because leaving had become troublesome. Nor would I wish to leave a happy life merely to prove that I could. Fortunately, neither choice is required of me tonight."''', c('[Stay beside her as the light fades.]', "interest")),
    n("interest", "Arsinoe", '''{n}The air cools. Arsinoe draws the cloth over the empty basket, then leaves her hand resting beside it.{/n}
"I would like another evening with you. I can make that decision now."
{n}She looks at you with the composed attention she gives a serious answer, but her smile is quite different from the one she offers across her table.{/n}
"There is a rather attractive person sitting next to me, and I have spent much of the evening pointing out buildings. I hope that has not made my interest difficult to detect."''',
      c('"I noticed. I hoped it was personal."', "touch"),
      c('"I would like to take this slowly."', "slow"),
      c('"I enjoy your company as a friend."', "friend")),
    n("touch", "Arsinoe", '''"Very personal."
{n}She turns her hand palm upward beside the basket. She grips your hand firmly, then looks from it to your face with undisguised satisfaction.{/n}
"I am pleased you came."
{n}A shout rises from the stair below. Tovin wants to know whether you need a lamp to come down.{/n}
{n}Arsinoe closes her eyes for a moment, amused rather than embarrassed.{/n}
"Yes, please. The city's celebrated order has not yet reached your stairs."
{n}She keeps your hand until the light appears at the door.{/n}''', c('[Walk down with her.]', flags=("arsinoe.roof_shared", "arsinoe.courting"))),
    n("slow", "Arsinoe", '''"So would I. There is a great deal I would enjoy learning before either of us begins making promises."
{n}She leaves her hand where it is and begins to wrap the cups with the other.{/n}
"Another evening, then. You may choose it. I am aware that I have selected the subject, the location, and the refreshments so far."
{n}Her smile invites an answer without requiring one before you stand.{/n}''', c('[Help her pack the basket.]', flags=("arsinoe.roof_shared", "arsinoe.slow"))),
    n("friend", "Arsinoe", '''{n}She takes a breath, then nods.{/n}
"Then I shall enjoy that. I am a little disappointed, but I have had a good evening. You need not make a poorer one of it by worrying over my expression."
{n}She begins wrapping the cups.{/n}
"I should still like your opinion of Tovin's next attempt. Friends may be put to work on matters of taste, I believe."''', c('[Help her pack the basket.]', flags=("arsinoe.roof_shared", "arsinoe.friendship"))),
], requires=("arsinoe.printer_met",), delay=24)


s("arsinoe_first_impression", "What the picture leaves out", '"Has Tovin brought his new work?"', [
    n("start", "Arsinoe", '''{n}Arsinoe has cleared a place for a sheet of paper. Beside it stands Tovin, looking more anxious than he did when he sold her something demonstrably false.{/n}
"He has. I thought you should see it before I answered him."
{n}The printer inclines his head to you and removes the cloth covering the sheet.{/n}''',
      c('[Look at the print.]', "fantasy_result", requires=("arsinoe.print_fantasy",)),
      c('[Look at the print.]', "street_result", requires=("arsinoe.print_street",)),
      c('"I cannot stop now. Please do not wait for my opinion."', abort=True)),
    n("fantasy_result", "Tovin", '''"Three sold. With the correction shown to each buyer. One laughed and asked whether we would ever be so fortunate. Another wanted the old title, so I lost that sale."
{n}A CITY IMAGINED now fills the space above the improbable harbor. Beneath it, smaller letters name Tovin and Drezen as the place of printing.{/n}
"I have the paper for another batch. I have not cut the street yet."
{n}He sets a pencil drawing beside the print. The leaning chimney has remained leaning.{/n}
"I worked on this when the shop was quiet. There was less quiet than I expected."
{n}Arsinoe examines both.{/n}
"I am glad the correction did not ruin you. I should still like to see this other one finished."
"So should I. But I won't tell you it will be tomorrow."''', c('[Study the street drawing.]', "omission")),
    n("street_result", "Tovin", '''"Four copies. One spoiled when I pulled it. Three fit to sell."
{n}The printed view is smaller than the old one. Its lines are uneven in places, but the basket hangs from its window and the leaning chimney would be difficult to mistake for any other.{/n}
"I could not afford the next batch of paper. I have enough for small jobs. This will have to sell before I do much more."
{n}Arsinoe studies it, then places her old receipt on the table.{/n}
"I would like to exchange my purchase for this one, if the price is the same."
"It is."
{n}His shoulders ease when she says that she will recommend it. The covered stack of old pictures remains his loss; a single pleased customer has not made that disappear.{/n}''', c('[Study the street view.]', "omission")),
    n("omission", "Arsinoe", '''{n}Arsinoe points to a gap between two houses.{/n}
"You have left this empty. There is a covered stall there."
"It hides half the doorway."
"People stand there."
"People stand everywhere. I can't put all of them in."
{n}He looks at you, hoping for help.{/n}
"It is a picture. I have to choose something."
{n}Arsinoe looks at the empty space again.{/n}
"Yes. You do. I was pleased that you had stopped inventing buildings. Perhaps I have become greedy and want every person accounted for as well."''',
      c('"Keep the open space. He has chosen a view, and he has shown what he changed."', "open", flags=("arsinoe.picture_open_space",)),
      c('"Try a second drawing with the stall. Let us see the choice before deciding."', "stall", flags=("arsinoe.picture_stall",))),
    n("open", "Arsinoe", '''"Then keep it. I shall refrain from inspecting your next picture for every omitted barrel."
{n}Tovin looks relieved enough to make her laugh.{/n}
"That was a joke. Mostly."
{n}He gathers the work, leaving Arsinoe the view she has purchased. When he has gone, she looks toward the real street.{/n}
"I had imagined that I would be very easy to please once he drew what was actually there. Apparently I require practice."''', c('"What would you draw?"', "hers")),
    n("stall", "Narrator", '''{n}Tovin puts a thin sheet over his street view and sketches the awning. Its edge cuts across the doorway. He darkens the underside, adds the suggestion of a figure, then holds the two versions apart.{/n}
{n}The busy version is less graceful. It also looks more like the place you walked through.{/n}
{n}"I prefer it," Arsinoe says.{/n}
{n}"I prefer the doorway," Tovin replies. "But I'll keep the drawing. It might work from farther along the street."{/n}
{n}He gathers the work, leaving Arsinoe her purchase. No new plate is promised. When he has gone, she is still looking at the place where he held the two versions.{/n}
{n}"I should have liked him to agree. At least I know what he disagrees with."{/n}''', c('"What would you draw?"', "hers")),
    n("hers", "Arsinoe", '''"Badly? Almost anything. Well? I have never learned."
{n}She finds an unused corner of a sheet and draws a rectangle, then another. A street begins to emerge, suspiciously regular.{/n}
"Room for two carts. Drains that work. A place to rest that does not charge for beer. We have soldiers coming back wounded and people living in half a house; I should like to build something for them besides another barricade."
{n}She pauses over the little drawing.{/n}
"I would enjoy seeing this built. I would also enjoy sitting beneath one of those trees with a book while someone else admired the drainage."
{n}She adds a small bench. It takes three attempts to make its legs stop resembling a ladder.{/n}''',
      c('"May I sit beside you in this magnificent future?"', "future", forbids=("arsinoe.friendship",)),
      c('"What would you be reading?"', "book")),
    n("future", "Arsinoe", '''"You may. But you will have to tolerate my pointing out the drains at least once."
{n}She adds a second mark to the bench, then studies it with comic dissatisfaction.{/n}
"I have done neither of us justice. You should be much closer."
{n}She lays down the pen and moves her chair toward yours instead.{/n}
"That is more within my abilities."''', c('"And what will we be reading on our bench?"', "book")),
    n("book", "Arsinoe", '''"A travel account. Preferably written by someone who can describe a meal without treating it as an interruption to the important part of the journey."
{n}She adds a tiny square to the figure on the bench.{/n}
"I have one with an entire page about an innkeeper's sauce. The next chapter concerns a governor, and is much less persuasive. I have never decided whether the author liked the sauce too much or the governor too little."
{n}She sets down the pen.{/n}
"You may borrow it. I would like another opinion."''', c('"Bring it when we next meet."', "invitation")),
    n("invitation", "Arsinoe", '''"I will. Where shall that be?"
{n}She folds her little street carefully enough to suggest that she intends to keep it.{/n}
"I promised you a choice. There is a table in the shop after Tovin closes, and he is willing to lend it. Or we could walk while there is still light. I should enjoy either, although I warn you that I may have opinions about anything you point out."''',
      c('"Bring the book. I will meet you at the table."', flags=("arsinoe.next_table", "arsinoe.first_impression_kept")),
      c('"A walk. Show me the things you would keep as they are."', flags=("arsinoe.next_walk", "arsinoe.first_impression_kept"))),
], requires=("arsinoe.roof_shared",), delay=24)


s("arsinoe_hours_of_her_own", "When her work is finished", '"Have you time for our evening?"', [
    n("start", "Arsinoe", '''{n}Arsinoe puts away the last of her work before turning to you. She has brought a book with a repaired spine, its place marked by a narrow strip of blue cloth.{/n}
"Yes. And I have remembered that you were to choose where we spent it."
{n}Her gaze rests on you for a moment before she picks up the book.{/n}
"Shall we?"''',
      c('[Go to the table with her.]', "table", requires=("arsinoe.next_table",)),
      c('[Walk with her.]', "walk", requires=("arsinoe.next_walk",)),
      c('"I must ask you to keep the evening for another time."', abort=True)),
    n("table", "Narrator", '''{n}Tovin has swept the shop and left a lamp on the table. He wishes you both a good evening, retrieves a forgotten apron, and finally leaves you alone.{/n}
{n}Arsinoe puts the book between you and opens it at the marker.{/n}
{n}"Here. The sauce. Tell me whether you think a page is excessive."{/n}
{n}You read while she watches your face. The traveler describes the meal with such concentration that the inn, the road, and the purpose of the journey all disappear for several paragraphs.{/n}
{n}"I want to taste it," Arsinoe admits. "That is the difficulty with calling it excessive."{/n}''',
      c('"He should have asked for the recipe."', "recipe"),
      c('"A person ought to be allowed a page for something they enjoyed."', "page")),
    n("recipe", "Arsinoe", '''"He did. She refused."
{n}Arsinoe turns a page and shows you the short, injured paragraph that follows.{/n}
"He describes her as unreasonable. I suspect she had already listened to him discussing her supper for longer than she wished."
{n}She laughs when you find his attempt to guess the ingredients in a note at the bottom.{/n}
"I should have liked to meet her. I believe we might have got on."''', c('[Read a little farther together.]', "evening")),
    n("page", "Arsinoe", '''"Then you must allow me several on the subject of a properly built city."
{n}She rests her chin on her hand.{/n}
"No, do not look resigned. I can be entertaining. I have just demonstrated that I know where to find the good passages in someone else's book."
{n}She turns the page to the governor, reads the first sentence, and promptly turns back.{/n}
"That will not improve our evening."''', c('[Read a little farther together.]', "evening")),
    n("walk", "Narrator", '''{n}Arsinoe takes you along a street whose houses are patched, crowded, and determinedly occupied. She stops beneath a stone lintel carved with leaves. Several have broken away, but the surviving ones curl around a small, solemn face.{/n}
{n}"That," she says. "I would keep that."{/n}
{n}She steps aside so you can see it without looking straight into the lowering sun.{/n}
{n}"Someone could have made a plain lintel and finished sooner. Instead, someone wanted people passing beneath it to look up."{/n}
{n}She opens her book at a folded scrap showing another carved doorway, then holds it beside the real one. They are nothing alike.{/n}
{n}"The traveler disliked this one. Too elaborate. I have occasionally wondered whether I would have enjoyed his company at all."{/n}''',
      c('"You could have argued about every doorway."', "argument"),
      c('"I am enjoying yours."', "company")),
    n("argument", "Arsinoe", '''"For the first three days, certainly. After that I should require him to admire something without qualifying the compliment."
{n}She closes the book and slips her finger beneath the blue marker to keep its place.{/n}
"I have no objection to a discerning companion. I do object to one who makes enjoyment feel like a lapse in judgment."
{n}She looks back at the carved face before walking on.{/n}
"There are worse faults in a doorway than giving someone a little too much to look at."''', c('[Walk on beside her.]', "evening")),
    n("company", "Arsinoe", '''"I am glad. I had begun to suspect that I was taking you on a very slow inspection."
{n}She closes the book and turns away from the lintel.{/n}
"There. I shall look at you for a while."
{n}She does, with an attention that makes the rest of her sentence unnecessary. Then she smiles and resumes walking at your side.{/n}''', c('[Walk on beside her.]', "evening")),
    n("evening", "Arsinoe", '''{n}When the hour grows late, Arsinoe accompanies you to the place where your ways part. She has tucked the book securely beneath her arm.{/n}
"I have enjoyed this. Even the parts that had nothing to do with pictures."
{n}She glances back along the street, then returns her attention to you.{/n}''',
      c('"I would like to see you again."', "romance", requires=("arsinoe.courting",)),
      c('"I would like to see you again."', "slow_end", requires=("arsinoe.slow",)),
      c('"Thank you for the evening."', "friend_end", requires=("arsinoe.friendship",))),
    n("romance", "Arsinoe", '''"Yes."
{n}She answers before you have quite finished speaking, then laughs at herself.{/n}
"I have been sufficiently composed for one evening. You may know that I was hoping you would ask."
{n}She takes a step nearer. The book presses lightly against her side as she lifts her free hand toward yours.{/n}
"Come closer. I have been thinking about your mouth instead of listening to my own good advice."''',
      c('[Kiss her.]', "kiss"),
      c('"Hold my hand a moment. I would like that tonight."', "hand")),
    n("kiss", "Narrator", '''{n}She comes close enough that you feel the warmth of her before her lips touch yours. The first kiss is brief. When you stay near, she grips your sleeve and kisses you again, firmly enough to make you forget the book.{/n}
{n}The book slips against her arm. You catch its lower edge, and she laughs softly against your cheek.{/n}
{n}"Thank you. I should hate to discover that the governor was useful only as a weight."{/n}
{n}She settles the book securely, then keeps her hand in yours a little longer.{/n}''', c('[Walk the last few steps with her.]', "parting", flags=("arsinoe.first_kiss",))),
    n("hand", "Arsinoe", '''"Then that is what we shall do."
{n}She gives you her hand and stands beside you. Her thumb moves once over your knuckles. A pair of passersby recognizes her, receives a nod, and continues on without requiring either of you to explain the evening.{/n}
"I am very pleased with tonight," {n}she says.{/n} "I hope that is clear."''', c('[Walk the last few steps with her.]', "parting")),
    n("slow_end", "Arsinoe", '''"So would I."
{n}She offers you the book.{/n}
"Take this until then. Begin with the inn. You may skip the governor with my blessing, although I cannot claim divine authority for that advice."
{n}When you accept it, her fingers rest briefly against yours.{/n}
"I would enjoy another walk. Or something you would like to show me. I know rather more about your patience with my interests than I do about your own."''', c('[Promise another conversation.]', flags=("arsinoe.opening_kept",))),
    n("friend_end", "Arsinoe", '''"And thank you for coming."
{n}She offers you the book, opened to the place where the traveler finally leaves the inn.{/n}
"Borrow it. I shall ask whether you agreed with him about the next city. Disagree if you like. I usually do."
{n}She waits while you find a safe place for it, then wishes you a good night and turns toward her own door.{/n}''', c('[Leave with the borrowed book.]', flags=("arsinoe.opening_kept",))),
    n("parting", "Arsinoe", '''"Next time, something of yours. A place, a story, an argument you have been saving. I should like to know what occupies you when nobody has come to ask for a decision."
{n}She releases your hand reluctantly enough for you to notice.{/n}
"Good night."
{n}After a few steps she looks back. Finding you still there, she smiles without trying to disguise it.{/n}''', c('[Wish her a good night.]', flags=("arsinoe.opening_kept",))),
], requires=("arsinoe.first_impression_kept",), delay=24)


# Round 2: an interrupted observation/selection remains the same on return.
_city = next(s for s in SCENES if s["Id"] == "arsinoe_city_on_paper")
_pages = {page["Id"]: page for page in _city["Nodes"]}
_results = ("arsinoe.print_source_found", "arsinoe.print_source_uncertain")
_pages["picture"]["Choices"][0]["Forbids"].extend(_results)
for _flag, _target in zip(_results, ("recognized", "uncertain")):
    _pages["picture"]["Choices"].append(c('[Recall the view you already examined.]', _target,
        requires=(_flag,), forbids=tuple(f for f in _results if f != _flag)))
_impression = next(s for s in SCENES if s["Id"] == "arsinoe_first_impression")
_omission = next(page for page in _impression["Nodes"] if page["Id"] == "omission")
_selections = ("arsinoe.picture_open_space", "arsinoe.picture_stall")
for _choice in _omission["Choices"]:
    _choice["Forbids"].extend(_selections)
for _flag, _target in zip(_selections, ("open", "stall")):
    _omission["Choices"].append(c('[Keep the decision you made.]', _target,
        requires=(_flag,), forbids=tuple(f for f in _selections if f != _flag)))

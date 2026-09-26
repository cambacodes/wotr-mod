"""Authored negotiations and private consequences through the existing invited charm.

No native outcome, actor, patron, possession, inventory or quest state is changed.
"""
from story_format import c, n, scene

SCENES = []


def s(id, title, nodes, requires=(), delay=24):
    for page in nodes:
        if not page["Portrait"]:
            page["Portrait"] = "Jerribeth"
    SCENES.append(scene(
        "jerribeth." + id, title, "Jerribeth", 3, "", nodes,
        Relationship="jerribeth", Remote=True, Chapters=[3, 4, 5],
        Areas=["2570015799edf594daf2f076f2f975d8", "7847c3e3537104f4694167af0b9fcd0e"],
        requires=("jerribeth.commission", "jerribeth.terms", *requires),
        forbids=("jerribeth.farewell",), delay=delay, optional=True,
        ForbidOverrides={"jerribeth.farewell": "jerribeth.catchup_requested"}))


s("offered_signature", "The purchaser of an evening", [
    n("start", "Narrator", '''{n}Jerribeth is already attending to her side when you invite the connection. She has arranged three folded papers beside her hands. Each bears the same red impression, carefully kept too small for you to read.{/n}
"A purchaser has made me an offer. A wealthy widow with grown daughters who have learned to leave before she begins describing her collections. She collects entertainments and sometimes remembers to pay their makers."
{n}Jerribeth taps the first paper.{/n}
"She wants an evening like the one I made for you. That would be flattering if she had not spent most of her letter describing you."''',
      c('"Show me what she is actually buying."', "offer"),
      c('[Leave the business for another evening.]', abort=True)),
    n("offer", "Jerribeth", '''{n}The writing enlarges inside the charm. It remains on her side of the connection; you read the portion she holds up.{/n}
{n}The purchaser offers payment for a performance and permission to describe it as an entertainment enjoyed in the Commander's private company. A further line requests a likeness, an imitation of your voice and an account of what you asked Jerribeth to change.{/n}
"No memories, no opening into your thoughts. Merely my own observations. You see how diligently people learn the rules before finding something useful outside them."
{n}Her voice is amused. She is watching whether yours will be.{/n}''',
      c('"You would be selling somebody the impression that I invited her into our room."', "impression"),
      c('"And how much is my supposed hospitality worth?"', "price")),
    n("impression", "Jerribeth", '''"Precisely. She is less interested in the room than in being seen emerging from it."
{n}Jerribeth turns the paper so the seal faces her.{/n}
"I have not agreed. I wanted to hear what you would object to first: the lie, the presumption or the possibility that I might enjoy making money from something you thought belonged to us."
{n}She waits, delighted with the question she has made you answer.{/n}''', c('"The presumption. You have brought me a decision somebody hoped I would never see."', "ownership")),
    n("price", "Jerribeth", '''"Enough to be insulting when compared with what she thinks the association will purchase afterward."
{n}A dry little chitter follows.{/n}
"She has offered to introduce my work to people who supposedly matter. The useful names are absent. The compliments are abundant. I have served masters who used the same accounting."
"You sound tempted."
"I am tempted by the payment. I am offended by the expectation that I should be grateful for the rest. Both deserve your attention."''', c('"Then let us separate your work from what she thinks she can buy through me."', "ownership")),
    n("ownership", "Jerribeth", '''"The work is mine. The evening was ours. Those are different claims, although you may discover how inconvenient it is to draw the line."
{n}She unfolds the second paper. It contains her reply, unfinished after the salutation.{/n}
"I can offer a new entertainment without your likeness, words or endorsement. She would have to pay for what I make instead of whom she hopes to resemble."
"Or?"
"I can refuse the performance and sell her a design she must assemble herself. An unpleasant amount of work. Her own guests would discover whether she has any taste."
{n}Jerribeth lifts her gaze.{/n}
"I prefer the first. I would enjoy watching her discover what she has purchased. But I asked you here because I wanted something more useful than an audience that nods."''',
      c('"Offer a new performance. Keep our likenesses and our private conversations out of the sale."', "performance", flags=("jerribeth.offer_performance",)),
      c('"Sell the design. Let her put her own reputation in front of the guests."', "design", flags=("jerribeth.offer_design",))),
    n("performance", "Jerribeth", '''{n}She writes, slowly enough for you to read the words she chooses. The offer describes a new work. It grants no right to your name, likeness, speech or private correspondence. Jerribeth adds her own name beneath yours in the restriction.{/n}
"There. She may purchase what I choose to show. She may not fill the room with copies of either of us afterward."
"You had not mentioned that possibility."
"I have now. I would dislike discovering myself at a party I had declined to attend."
{n}She pauses over the price, doubles it, then leaves the pen still long enough for you to notice.{/n}''', c('"You expect her to bargain."', "send")),
    n("design", "Jerribeth", '''{n}Her antennae draw back.{/n}
"You have chosen the version in which I must explain my work to somebody with more money than patience. An imaginative cruelty."
{n}Nevertheless, she writes the offer. The purchaser will receive instructions for one invented scene, without either of your likenesses or the private conversation that inspired it. The purchaser must name herself as its presenter.{/n}
"I shall insist on an advance. If she cannot endure reading the instructions, she can at least pay for my having written them."
{n}She adds a price that makes you look at her.{/n}''', c('"You expect her to bargain."', "send")),
    n("send", "Jerribeth", '''"I expect her to call me difficult. It will be pleasant to deserve it for a reason I selected."
{n}She folds the reply but does not seal it yet.{/n}
"Do not mistake this for your having forbidden me a profitable vice. I have accepted the restriction because I want this correspondence to continue. I reserve the pleasure of making the remaining arrangement expensive."
"Then make it expensive."
{n}She presses her seal into the wax.{/n}
"You say the most encouraging things when you stop trying to improve me."''', c('[Ask to see the purchaser\'s answer when it comes.]', flags=("jerribeth.counteroffer_sent",))),
])


s("borrowed_sun", "The figure she leaves unfinished", [
    n("start", "Jerribeth", '''{n}The room Jerribeth projects tonight contains a small unfinished landscape on a table. A pale disc hangs above it, casting light without warming the painted roofs.{/n}
"A study. I have not offered it to the purchaser."
{n}As you look, a doorway acquires a standing figure. Its face is blank.{/n}
"You recognize the problem already. I can hear how carefully you are waiting."''',
      c('"You told me what your illusion made the people of Wintersun see. Why bring that shape into this room?"', "shape"),
      c('[Ask her to leave the study covered until you have time to discuss it.]', abort=True)),
    n("shape", "Jerribeth", '''"Because it worked. Because I remember the light. Because refusing to name a thing does not prevent me from remembering how to make it."
{n}Her hand rests beside the little roofs.{/n}
"No villagers are inside this model. No one is looking through it. It is a construction I am showing you, and I am asking whether there is anything in it you would choose to keep."
"You are also asking me to turn what happened into a question of taste."
"Yes. I thought you might notice."
{n}She does not cover the model. She waits beside it.{/n}''',
      c('"Remove the inhabited village. Make a place that does not borrow its meaning from people you deceived."', "empty", flags=("jerribeth.sun_uninhabited",)),
      c('"Keep the construction unfinished. Show me where you would have made an audience stop questioning it."', "expose", flags=("jerribeth.sun_exposed",)),
      c('"You made people defend the world you invented for them. I want to understand how. Turn it around and show me the construction."', "expose", flags=("jerribeth.sun_exposed", "jerribeth.sun_studies_power"))),
    n("empty", "Jerribeth", '''{n}The doorway disappears. Then the roofs lift away, leaving the pale disc over a bare slope.{/n}
"There. An admirable absence."
"You can do better than making my answer look foolish."
{n}Her hands stop.{/n}
"I can. It requires deciding what to put in the space."
"That is the work."
{n}She gives you a look whose meaning requires no translation. Then she draws a black line through the slope. It opens into a ravine, and light catches on a narrow crossing. There is no village at either end.{/n}
"Now there is somewhere to go. I could put a storm behind it."
"Leave the far end visible."
"You are determined to make me show my audience where the path ends. Very well. They may still dislike the journey."''', c('[Watch her finish the crossing.]', "account")),
    n("expose", "Jerribeth", '''{n}She turns the model around. From behind, the roofs are shallow shells. The doorway opens onto nothing.{/n}
"A familiar face here. A welcome at the gate. The visitor supplies most of the rest. People work astonishingly hard to make a comforting explanation complete."
"And when it does not fit?"
"They ask somebody they trust. Or they stop asking because the answer would make the next hour unbearable."
{n}The blank figure turns its head. Before it can acquire features, you point to it.{/n}
"Leave that one blank while you show me what you are changing."
{n}Jerribeth's hand closes, and the figure stills.{/n}
"You would display the machinery. Some guests would be offended by the suggestion that they need it explained."
"Those guests can leave."
"They might. I would enjoy seeing which ones first pretended they had understood all along."''', c('[Ask her to leave the back of the model visible.]', "account")),
    n("account", "Jerribeth", '''{n}Jerribeth moves away from the study. When she speaks, the high voice has lost its teasing rhythm.{/n}
"I am not returning anything to Wintersun by changing this model. Do not later offer me that account of what we did."
"I know."
"And I am not going to tell you that I remember my deception only with regret."
"You told me what happened to travelers who believed they had found safety. I remember which part was real."
{n}Her antennae quiver once.{/n}
"Then why remain?"''',
      c('"Because I can want you and still refuse this use of your work. You do not get to combine those answers for me."', "remain", flags=("jerribeth.sun_judgment_kept",)),
      c('"Because I wanted to see what you would make after I objected. I have not decided what that means beyond tonight."', "remain", flags=("jerribeth.sun_judgment_reserved",)),
      c('"I have discovered that I cannot keep doing this."', "part"),
      c('"I recognize the attraction of that power. I wanted to study it with you, not pretend the people who suffered were inventions too."', "power_reply", flags=("jerribeth.sun_power_interest",), requires=("jerribeth.sun_studies_power",))),
    n("remain", "Jerribeth", '''{n}For several breaths she offers neither an excuse nor a new display. Then she brings the altered model closer to the charm.{/n}
"Look at it once more. This version. Tell me whether the light reaches the far side."
{n}You lean toward the frame. She follows your gaze, moving the pale disc by a small amount until its light reveals the changes you requested.{/n}
"There," she says. "I dislike some of your company. I have apparently decided to keep asking for it."
{n}She leaves the model where you can both see it for the rest of the conversation.{/n}''', c('[Continue looking with her.]', flags=("jerribeth.sun_reworked",))),
    n("part", "Jerribeth", '''"Then this is the last thing I show you."
{n}She moves the study beyond the frame. Her own face remains until you reach for the charm.{/n}
"You need not pretend the evening was wasted. I learned where you would leave."
{n}The connection ends under your hand. Nothing in Wintersun changes with it.{/n}''', c('[End the private relationship.]', flags=("jerribeth.closed",))),
    n("power_reply", "Jerribeth", '''{n}Her attention sharpens. She turns the model so that the blank figure faces you again.{/n}
"That is a question I could spend an evening answering. You might dislike how much of the answer you recognize."
"I have not offered you my mind as a place to demonstrate it."
"No. You have offered your attention. I have accepted the distinction, inconvenient though you sometimes make it."
{n}She taps the empty doorway.{/n}
"We can examine this without supplying it with a victim. I have already shown you how the face is withheld. Watch what happens when I change what stands behind it."''', c('[Study the construction without pretending it excuses its maker.]', "remain")),
], requires=("jerribeth.offered_signature", "jerribeth.wintersun_known"))


s("small_print", "The part she expected you to miss", [
    n("start", "Jerribeth", '''{n}The purchaser's answer has arrived. Jerribeth holds it by one corner as if the paper has been badly washed.{/n}
"She accepts the price."
"You sound disappointed."
"I had prepared an excellent answer to an objection she neglected to make. Fortunately, she supplied another."
{n}She turns the page toward the charm.{/n}
"Read the line beneath the acceptance."''',
      c('[Read the added condition.]', "condition"),
      c('[Postpone the discussion before agreeing to anything.]', abort=True)),
    n("condition", "Narrator", '''{n}The line permits the purchaser to advertise that Jerribeth developed the work during private consultations with an unnamed victorious commander. It then lists enough accomplishments to make the omitted name useless as a disguise.{/n}
"She has removed the likeness and kept the implication," Jerribeth says. "A competent piece of impudence."
{n}A second sheet lies underneath. You ask to see it.{/n}
"My draft answer."
{n}She has crossed out the accomplishments. The phrase private consultations remains.{/n}''',
      c('"That phrase still sells our evening. Why have you kept it?"', "kept"),
      c('"You knew I would ask for the second sheet."', "test")),
    n("kept", "Jerribeth", '''"Because a little uncertainty makes people curious. Because I did not agree to hide the fact that I have somebody worth entertaining."
"You agreed not to sell our private conversations."
"I agreed not to reproduce them. There is a difference."
{n}You leave the sentence unanswered long enough for her to hear herself defending it.{/n}
"Yes," she says. "An ugly little difference when placed beside the invitation that made the conversations possible. I had hoped it would look more attractive with a fee attached."''', c('"What are you offering now?"', "choice")),
    n("test", "Jerribeth", '''"I thought you probably would. I also thought you might enjoy the implication enough to let it remain."
"Then you were asking after all. You chose an irritating way to do it."
"I wanted you to choose the indulgent answer without making me request indulgence."
{n}Her linked hands tighten.{/n}
"There. A confession sufficiently small that I can bear to make it. Do something useful with it before I decide it was a mistake."''', c('"Give me an offer you actually mean to keep."', "choice")),
    n("choice", "Jerribeth", '''"I can strike the phrase and require her to announce that the work carries no endorsement from you. She may withdraw. She may pay and resent us. I could enjoy either result."
"Or?"
"I can withdraw myself. Keep the work and the advance unsigned. Make her explain to her guests why the entertainment she has been hinting about never existed."
{n}Jerribeth draws the letter back toward her.{/n}
"I am asking what you want. I have not offered to become pleasant about it."''',
      c('"Keep the sale if she accepts the explicit correction. No hints that I endorse her."', "correct", flags=("jerribeth.sale_corrected",)),
      c('"Withdraw. I would rather the work remain yours than spend another evening bargaining over my absence from it."', "withdraw", flags=("jerribeth.sale_withdrawn",))),
    n("correct", "Jerribeth", '''{n}She writes the correction where you can read it. The purchaser may describe the work and its maker. She may not describe a relationship with you, invite guests on your supposed behalf or display either your name or a recognizable substitute for it.{/n}
"Now she can decide whether she wanted the work at all."
{n}Jerribeth adds a demand for written acceptance before delivery.{/n}
"You have cost me the pleasure of pretending I misunderstood her. I shall seek compensation in the quality of her irritation."
"And the phrase in your own draft?"
{n}She draws a line through it, then tears that sheet in half.{/n}''', c('[Watch her seal the corrected offer.]', "after")),
    n("withdraw", "Jerribeth", '''{n}She stares at the unsigned agreement, then takes a clean sheet.{/n}
"I decline the proposed terms. The commission is not accepted. Any announcement made before acceptance was your invention."
{n}She reads the three sentences aloud. A chitter of pleasure accompanies the third.{/n}
"A little blunt. It will improve in the retelling."
"Are you keeping a copy?"
"Two. One for anyone who asks me whether she has purchased my services. One for when I am tempted to remember this as your forbidding me something instead of my choosing the answer."
{n}She looks up as though she regrets having said the last part.{/n}''', c('[Let that admission stand without congratulating her.]', "after")),
    n("after", "Jerribeth", '''"You could be more gracious about winning an argument."
"Would you prefer applause?"
"I would prefer an invitation. I have spent enough time tonight being useful to a person I do not particularly like."
{n}She leaves the sealed letter on the table. Her attention settles on you with a directness she had kept out of the negotiation.{/n}
"Another evening. No purchaser. You can decide whether I have earned the opportunity to be difficult in a different way."
"You can ask without earning it. I can answer without owing it."
{n}Her amusement returns, quieter.{/n}
"Then I am asking."''', c('[Agree to an evening without the correspondence on the table.]', flags=("jerribeth.sale_terms_set",))),
], requires=("jerribeth.counteroffer_sent",), delay=48)


s("unsold_evening", "An audience she cannot purchase", [
    n("start", "Jerribeth", '''{n}There are no papers in the projected room. Jerribeth has made that absence conspicuous by leaving the table entirely bare.{/n}
"I considered putting a vase there. Then I imagined you asking who owned the flowers."
"I would have asked why you chose them."
"An even more dangerous question."
{n}She reaches toward the empty space beside her, then stops short of furnishing it.{/n}
"I can show you the room while we talk. Or we can dispense with the scenery. Either way, you remain where you are. I have not secretly improved the furniture."''',
      c('[Ask her to show the room she prepared.]', "room"),
      c('[Keep the frame between you and spend the evening talking.]', "frame", flags=("jerribeth.unsold_frame",)),
      c('[Ask to keep the evening for another time.]', abort=True)),
    n("room", "Narrator", '''{n}The room becomes clear inside the frame. Jerribeth moves her image to a chair near its edge. You draw your own chair closer to the charm; the distance between your bodies remains unchanged.{/n}
{n}She does not borrow anyone you recognize. A narrow strip of darkness marks where her invented room ends.{/n}
"I could make the table disappear too," she says. "But I suspect we would only find another object to put between us."''',
      c('"Show yourself in your own form. I want to look at you."', "true", flags=("jerribeth.unsold_true_form",)),
      c('"Choose a guise you enjoy wearing. Tell me what you like about it."', "guise", flags=("jerribeth.unsold_guise",))),
    n("guise", "Jerribeth", '''{n}The change takes place in full view. The woman inside the frame has a broad mouth, fine lines beside her eyes and an expression that remains Jerribeth's. She turns one hand, watching how the lamplight lies on its ordinary knuckles.{/n}
"This one smiles very well. People expect a creature with this mouth to have something enjoyable to say. I sometimes disappoint them deliberately."
"Did you invent her?"
"Yes. I could have improved the symmetry. I liked this better."
{n}She smiles to demonstrate. It is a good reason.{/n}''', c('[Ask her to bring the image nearer.]', "near")),
    n("true", "Jerribeth", '''{n}She lets the scenery dim around her own narrow silhouette. The antennae move as she watches you; a little light remains along the edges of her wings.{/n}
"You are allowed to look pleased. I did not ask you to examine a specimen."
{n}You tell her which expression prompted your smile. Her hands separate, and she brings one toward the edge of the image.{/n}''', c('[Keep your attention on her.]', "near")),
    n("near", "Jerribeth", '''{n}She watches you with unembarrassed interest, her image close to the border it cannot cross.{/n}
"I wanted you to ask. It is an inconvenient pleasure. I cannot obtain it by predicting what you would say."
"You could pretend."
"I have been very good at pretending. Tonight I would notice."
{n}Her hand turns palm upward inside the frame.{/n}''',
      c('"Tell me how you would kiss me if we were in the same room. I want to hear you say it."', "kiss", flags=("jerribeth.unsold_kiss_chosen",)),
      c('[Set your hand beside the frame and ask what she has wanted to tell you.]', "story", flags=("jerribeth.unsold_quiet",))),
    n("kiss", "Jerribeth", '''"Yes."
"I would put my hand here."
{n}She touches her own collar, then looks toward yours.{/n}
"I would ask you to come closer. I would like you to be sufficiently impatient that I could hear it in your answer. Then I would kiss you, and discover whether you become quiet or find more things to say."
{n}You tell her. Her hands come together slowly, and she asks you to be more specific. You oblige. The room's invented light shifts across her face. She seems to forget it until one lamp gutters absurdly, and then her laughter interrupts your answer.{/n}
"An unforgivable lapse in presentation."
"I was occupied."
"So was I. That is my defense."
{n}She leaves the lamp as it is.{/n}''',
      c('[Keep sharing the private imaginings you both invited, then remain at the charm afterward.]', "after", flags=("jerribeth.unsold_intimate",)),
      c('[Tell her you enjoyed that, and ask for quieter conversation now.]', "story", flags=("jerribeth.unsold_quiet",))),
    n("frame", "Jerribeth", '''{n}She lets the prepared room fall away. Her own silhouette remains inside the lacquered border.{/n}
"You have chosen the form of entertainment in which I cannot distract you with excellent lighting."
"You can try saying something interesting."
"A severe restriction. I shall survive it."
{n}Her hands come to rest where you can see them.{/n}
"I have been deciding what I wanted to tell you when I could no longer pretend it was necessary business."''', c('"Tell me."', "story")),
    n("story", "Jerribeth", '''"Before our first private evening, I rehearsed what I would say when you opened the connection. Four versions. In the third I was pleased to see you and concealed it so effectively that there was no reason for you to remain."
{n}She gives the faintest irritated buzz.{/n}
"The fourth was much better. I cannot remember a word of it. You opened the frame, and I became occupied with finding out whether you had come because you wanted to."
"You could have asked."
"And waste four perfectly good rehearsals?"
{n}You laugh. She waits for you to stop, pleased and annoyed in nearly equal measure.{/n}
"I have induced people to wait for a word from me as though it would determine whether the sun rose. Then I found myself disliking the small delay before this charm answered. I did not enjoy the comparison."
"Do you rehearse now?"
"Sometimes. Tonight I intended to remark upon your pauses. I offer you an evening, and you consider the answer as though somewhere a council has demanded to know who will pay for enjoying it."
{n}Her antennae incline toward you.{/n}
"Perhaps I should send a second letter authorizing a little waste. No useful intelligence. No improving conclusion. Just me, being very pleased to have interrupted you."''',
      c('"Send it. I will return it with several unreasonable demands for your company."', "after"),
      c('"I like hearing how closely you have been watching for my answer."', "joke_enjoyed"),
      c('"Sometimes I am simply busy. You are not on trial every time I take a moment to answer."', "joke_disputed")),
    n("after", "Jerribeth", '''{n}For a while neither of you mentions the purchaser. You watch her turn an answer over before giving it, then decide to say what you like about that pause.{/n}
"You enjoy finding the remark that will make me look at you again. I like seeing you choose it."
"You could save us both the effort by continuing to look."
"Then you would have to find out whether I stayed without the remark."
{n}She begins an answer, stops, and leaves you an unusually long silence. Her hands have become still in the frame.{/n}
"I thought you would eventually ask what useful thing I had brought," she says. "Something worth the time."
"Tonight I wanted this."
"Then I have brought it. I expect you to be extravagantly pleased."
{n}Her next laugh is softer than the remark deserves.{/n}
{n}When another obligation draws near, you tell her how much time remains.{/n}
"Spend it here, then. I will not ask you to steal it from somebody else so that I can admire the theft."
{n}She stays until you choose to close the connection, without turning the ending into a test.{/n}''', c('[Keep the pleasure of this evening without promising away the next.]', flags=("jerribeth.unsold_evening_kept",))),
    n("joke_enjoyed", "Jerribeth", '''"Of course you do. I have foolishly allowed you to discover how much trouble I take."
{n}She lifts one hand toward the edge of the frame, then lowers it.{/n}
"Enjoy it. I intend to be very difficult when it is your turn to wait."
"Will you keep me waiting on purpose?"
"I shall try. You have every reason to hope I will become impatient first."''', c('[Tell her what you enjoy watching in return.]', "after")),
    n("joke_disputed", "Jerribeth", '''{n}The amusement thins. She studies your expression.{/n}
"Then tell me when you are occupied. I would rather resent the actual interruption than invent an elaborate explanation for an empty frame."
"I can do that. I cannot promise an immediate answer."
"I heard you. I am making my complaint smaller, which is a disagreeable amount of work for a joke that was perfectly good."
{n}Her antennae move again.{/n}
"I can wait. I would prefer to know that I am waiting."''', c('[Let the correction stand, then tell her what you enjoy about her company.]', "after")),
], requires=("jerribeth.sale_terms_set", "jerribeth.lovers"))


s("purchaser_answer", "What she did when nobody watched", [
    n("start", "Jerribeth", '''{n}Jerribeth holds up the purchaser's final answer. The seal is broken, but the sheet has not been smoothed. She has read it more than once.{/n}
"I promised you the result. I am beginning to appreciate why people make fewer promises when they expect to be believed."
{n}She opens the paper.{/n}''',
      c('[Ask what became of the corrected sale.]', "sale", requires=("jerribeth.sale_corrected",)),
      c('[Ask how the purchaser received her withdrawal.]', "withdrawn", requires=("jerribeth.sale_withdrawn",)),
      c('[Ask to hear the result another evening.]', abort=True)),
    n("sale", "Jerribeth", '''"She accepted the correction. In writing. Then she asked whether I would attend a private supper afterward, so that her guests could discover the association for themselves."
"And you?"
"I quoted a separate price for my company. It was not a serious price. She understood that."
{n}Jerribeth unfolds a smaller note tucked inside the first.{/n}
"The payment is arranged between us. It buys only the work we specified. She has asked me never to negotiate in this fashion again. I have invited her to seek a more tractable artist."
"You sound pleased."
"I am. I intend to make the work good enough that she remembers this conversation when she wants another."''',
      c('[Ask about the new performance.]', "performance", requires=("jerribeth.offer_performance",)),
      c('[Ask about the design she must assemble herself.]', "design", requires=("jerribeth.offer_design",))),
    n("performance", "Jerribeth", '''"A banquet at which the dishes continually accuse one another of being in poor taste. No guest is copied, named or required to participate. They may simply sit there and suspect the vegetables of having better conversation."
"You made the food quarrel?"
"An invented meal. I have not taught anyone's supper to plead. The distinction seemed likely to concern you."
{n}A silver bowl appears in her image. Its lid rises, hesitates, and withdraws from the platter beside it with unmistakable disdain.{/n}
"The bowl thinks the platter is beneath it. I have not yet decided which is right."
{n}You ask to see the platter's answer. She supplies it with obvious satisfaction.{/n}''', c('[Let her enjoy showing what she made.]', "temptation")),
    n("design", "Jerribeth", '''"She receives a room in which every painted exit returns an imagined visitor to the seat she began in. The instructions require the real entrance to remain plainly visible. The actual guests may leave whenever they wish."
"And if she conceals the real entrance?"
"Then she has changed the design. I have written that she must not. I cannot promise you every purchaser will obey instructions merely because I write them beautifully."
{n}Jerribeth indicates the sample. A little painted door opens onto a second image of the same room, while the unpainted gap beside it remains unmistakable.{/n}
"I can make the distinction part of what I deliver. She can spoil it. That is one disadvantage of giving other people anything."''', c('[Ask her to keep the visible exit in the final instructions.]', "temptation")),
    n("withdrawn", "Jerribeth", '''"She called me unreliable. Then she asked whether I would reconsider. In the same letter."
{n}Jerribeth shows you the two paragraphs, savoring their proximity.{/n}
"I answered the first and ignored the second. She has no accepted commission and no permission to advertise one. I retain the work."
"And the payment?"
"There is none. You may admire my restraint at its actual price."
"You agreed to withdraw."
"I remember. I am allowing myself the complaint. Do not take that away as well."
{n}She folds the answer and puts it beneath her own copy of the refusal.{/n}''', c('"What will you do with the work?"', "kept")),
    n("kept", "Jerribeth", '''"Keep making it until it pleases me. Show it to someone who interests me. Eventually sell it to somebody who asks for the thing itself."
{n}She tilts her head.{/n}
"Those intentions may occur in an inconvenient order. I refuse to wait for a worthy buyer before enjoying what I have made."
"Then show me a part you like."''',
      c('[Ask to see part of the performance she kept.]', "kept_performance", requires=("jerribeth.offer_performance",)),
      c('[Ask to see part of the design she kept.]', "kept_design", requires=("jerribeth.offer_design",))),
    n("kept_performance", "Jerribeth", '''"A banquet with exceptionally ill-mannered dishes. I am still deciding whether any of them deserve to be invited again."
{n}She conjures a silver bowl whose lid rises to inspect an empty platter. The lid closes with an air of appalled judgment. You laugh before she explains it.{/n}
"Good," she says. "The platter has not yet given its defense. I have been saving that."''', c('[Ask what she almost did instead.]', "temptation")),
    n("kept_design", "Jerribeth", '''{n}She shows you a little room whose painted doors open onto further pictures of the same room. An unpainted gap beside the first door remains clearly visible.{/n}
"Every invented escape returns an imagined visitor to her seat. The actual guests can leave through that gap. I was rather pleased with the contrast."
"Would your purchaser have left it visible?"
"I required it. I cannot tell you whether she would have obeyed. Now I need not discover whether she can follow an instruction without considering herself diminished by it."
{n}Jerribeth turns the model, showing you the clear opening from the other side. The painted doors all face away from it.{/n}''', c('[Ask what she almost did instead.]', "temptation")),
    n("temptation", "Jerribeth", '''{n}The little display disappears.{/n}
"I considered sending her a beautiful imitation of your handwriting. No words of yours. Nothing that would command anyone. Merely a sheet she could spend a very uncomfortable evening explaining."
"Did you?"
"No. I had agreed not to use you in the dispute. I would have enjoyed it, and then you would have asked a question to which I disliked giving the true answer."
{n}Her gaze does not move from yours.{/n}
"I am telling you the version in which I remained tempted. If you require me to report that the temptation vanished, we can begin lying to each other now."''',
      c('"I care that you kept the agreement when breaking it would have entertained you."', "credit", flags=("jerribeth.consequence_values_action",)),
      c('"I am glad you told me. I will still ask the question next time."', "questions", flags=("jerribeth.consequence_keeps_questions",))),
    n("credit", "Jerribeth", '''"Then say that. It is an accomplishment I recognize."
{n}She listens while you do. There is nothing modest in the way she receives it.{/n}
"I could become accustomed to being praised accurately. Other people should be warned."
"Warn them yourself."
"I shall. They will assume it is a threat. In several cases they will be correct."''', c('[Stay while she puts the papers away.]', "end")),
    n("questions", "Jerribeth", '''"You would disappoint me if you stopped. I would also find it temporarily convenient. I contain multitudes of disagreeable preferences."
{n}She begins stacking the papers, then leaves the final answer facing you until you finish reading it.{/n}
"Ask while I am here to answer. I have no desire to compete with the version of me you invent when I am absent. She will either be tiresomely innocent or much too efficient."''', c('[Finish reading, then let the business end.]', "end")),
    n("end", "Jerribeth", '''{n}Jerribeth puts the last paper away and clears a space where the little display had stood.{/n}
"Enough about the purchaser. You haven't asked me which part was the most difficult."''',
      c('[Ask about the quarrelling dishes.]', "end_performance", requires=("jerribeth.offer_performance",)),
      c('[Ask about the painted doorways.]', "end_design", requires=("jerribeth.offer_design",))),
    n("end_performance", "Jerribeth", '''{n}Jerribeth restores the bowl and platter. This time the platter tips just enough to send the bowl's reflection sliding out of sight.{/n}
{n}The affront is so precise that you ask her to do it again. She obliges, then makes a small improvement she insists you notice.{/n}
"There. That is what I wanted to spend the evening showing you."
{n}She leaves the display running while you speak. The work has consequences outside your company; your company has changed one of the decisions she made about it. Neither of you claims more than that.{/n}''', c('[Ask her to save the next improvement for you.]', flags=("jerribeth.consequences_kept",))),
    n("end_design", "Jerribeth", '''{n}Jerribeth restores the model. One painted door opens a moment before the little room beyond it appears. She closes it, adjusts something too small for you to see, and tries again.{/n}
"There. You should have the pleasure of choosing the wrong door before discovering that it was wrong."
{n}This time the movement is smooth. The actual opening remains clear beside it. You ask her to repeat the change so that you can follow what she did.{/n}
"Watch the hinge," she says, pleased by the attention. "Everyone watches the room."
{n}She leaves the model between you while you talk. You keep noticing details, and she keeps admitting that she put them there deliberately.{/n}''', c('[Ask her to save the next improvement for you.]', flags=("jerribeth.consequences_kept",))),
], requires=("jerribeth.unsold_evening_kept",), delay=48)

"""Optional Kiana continuation after morning, before farewell.

Lenna, Odrin, their households, and these events are authored fiction.
The native marriage/death predicates are read, never changed.
"""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, nodes, after, delay=48):
    for page in nodes:
        page["Portrait"] = "Kiana"
    SCENES.append(scene("kiana." + id, title, "Kiana", 5, "", nodes,
                        Relationship="kiana", Remote=True, Chapters=[5], Areas=[DREZEN],
                        requires=("seelah.souls_returned", "kiana.lovers", "kiana.morning", after),
                        forbids=("kiana.closed", "kiana.farewell", "inhuman"),
                        ForbidOverrides={"kiana.farewell": "kiana.catchup_requested"},
                        delay=delay, optional=True))


s("guest_table", "Enough bowls for everyone", [
    n("start", "Kiana", '''{n}Kiana has borrowed a table rather than a castle. It is too wide for the room; anyone taking the chair by the wall will have to remain there until everyone else has finished eating.{/n}
"That place is Odrin's. He always tries to wash up before the rest of us have put down our spoons. Tonight he will have to endure our company."
{n}She sets down a fourth bowl and examines the arrangement. The lamplight catches the pale crystals above her brow.{/n}
"Lenna will be here too. She mends shoes. Odrin repairs carts. You are allowed to have supper without recruiting either of them."
{n}Kiana looks at the door, then back at you.{/n}
"I told them I wanted them to meet someone I enjoy being with. Lenna asked whether that meant you. Apparently my descriptions have been extremely subtle."''',
      c('"What did you tell her?"', "told"),
      c('[Explain that duty will keep you away tonight, and ask to arrange another supper.]', abort=True)),
    n("told", "Kiana", '''"Yes. Then she asked what she ought to wear. That took considerably longer."
{n}Kiana straightens one of the spoons, sees you watching, and leaves the other crooked.{/n}
"Lenna knows about Elan. If she watches my face through the whole soup course, I shall put an onion up her nose."
"Will the soup survive that much attention?"
"It will become insufferable. It's already rather pleased with itself."
{n}There is a knock. Kiana opens the door to a broad woman carrying a jar beneath one arm and a thin, gray-bearded man holding a bundle of spoons.{/n}
{n}"You said you had bowls," Odrin explains.{/n}
{n}"An excellent distinction. Come in." Kiana takes the spoons. "Commander, Lenna. Lenna, you have been standing on Odrin's foot for some time."{/n}''',
      c('[Make room for them at the table.]', "supper")),
    n("supper", "Narrator", '''{n}Lenna's jar contains pickled onions. She warns you about them after you have taken one. Odrin watches your face with the interest of a man who has already suffered.{/n}
{n}"She says she followed her mother's instructions," he tells you. "Her mother lives a comfortable distance away."{/n}
{n}"A woman who raised six children ought to be allowed a little revenge," Lenna says. "Kiana likes them."{/n}
{n}"Kiana has not committed herself," Kiana replies, and puts one into her bowl.{/n}
{n}The conversation becomes an argument about whether Odrin's lodger truly owns the enormous dog he feeds, or merely pays its expenses. Kiana wants to know whether the dog signed anything. Odrin says the dog has excellent references from all the butchers.{/n}
{n}When Kiana laughs, Lenna leans back in her chair. Relief makes her careless.{/n}
{n}"There she is. I was beginning to think we'd lost you to all that sadness. Good to see someone has brought you back." She nods toward you.{/n}
{n}Kiana sets down her spoon. Odrin suddenly finds the jar's lid difficult to open.{/n}''',
      c('"Give the cook the credit, Lenna. She has armed herself with onions."', "speak", flags=("kiana.guest_table.spoke",)),
      c('[Let Kiana answer, keeping your attention on her.]', "listen", flags=("kiana.guest_table.listened",))),
    n("speak", "Kiana", '''"And the blame for trapping Odrin against the wall."
{n}She smiles at him before turning to Lenna.{/n}
"The Commander brought neither the soup nor a cure, Lenna. Eat before you flatter it into going cold."
{n}Lenna's face reddens.{/n}
"I only meant you look happy."
"Then say that. I won't make you prove it."
{n}Beneath the table, Kiana finds your knee with hers. The touch lasts only a moment. Lenna looks from one of you to the other, then down at her bowl.{/n}''',
      c('[Take another spoonful of soup.]', "history")),
    n("listen", "Kiana", '''"I had to make the soup myself, Lenna. My rescuer was late."
{n}Lenna begins to laugh, then sees that Kiana has not picked up her spoon.{/n}
"I invited you to supper, Lenna, not to inspect how well I have mended."
{n}Lenna holds her cup with both hands.{/n}
"I didn't mean it that way."
"Then give me something better to hear. Odrin, what did that dog steal?"
{n}Kiana looks toward you. You stay with her gaze, and her shoulders ease a little.{/n}''',
      c('[Stay with the conversation.]', "history")),
    n("history", "Narrator", '''{n}Odrin places the opened jar in the middle of the table. Nobody reaches for it.{/n}
{n}Kiana sets down her spoon and looks directly at Lenna.{/n}''',
      c('[Listen.]', "widowed", requires=("kiana.bereaved", "seelah.elan_dead"), forbids=("kiana.separated",)),
      c('[Listen.]', "separated", requires=("kiana.separated",), forbids=("seelah.elan_dead", "kiana.bereaved"))),
    n("widowed", "Kiana", '''"Elan would have laughed at that. So am I. Stop looking relieved and tell us what the dog did next."
{n}Her voice catches on the last word. She takes a drink before anyone can offer her one.{/n}
"Some jokes are worth enjoying. Odrin's story about the dog has been getting better for years."
"The dog has been getting more expensive," he says.
{n}Kiana laughs through the breath she had been holding. Lenna manages a small smile, but does not yet look up.{/n}''',
      c('[Ask Odrin how the dog acquired its excellent references.]', "end")),
    n("separated", "Kiana", '''"Elan gave an excellent supper. He also burnt the bread once. Must I suppress one story to tell the other?"
{n}She puts both hands around her bowl.{/n}
"I left him myself, Lenna. No handsome general carried me off over a saddle."
{n}Lenna nods too quickly, then stops herself.{/n}
"All right. I am sorry."
"Thank you. Now, Odrin, tell me what the butcher actually wrote. Did he recommend the dog for employment?"''',
      c('[Listen to the remainder of the story.]', "end")),
    n("end", "Kiana", '''{n}The story becomes less believable as Odrin tells it. By the time the butcher has offered to stand as the dog's guarantor, Kiana is arguing that the dog ought to rent the room itself.{/n}
{n}Lenna eats, answers when spoken to, and leaves earlier than Odrin. She forgets her empty jar. Kiana follows her to the door, but their low conversation does not detain her.{/n}
{n}After Odrin has finally been allowed to wash the bowls, you and Kiana put the table back against the wall.{/n}
"Well. Nobody choked. I had hoped to set my standards a little higher."
{n}She turns Lenna's jar in her hands.{/n}
"I'm glad you came. Next time I may feed Lenna before she begins improving my life."
{n}She puts the jar aside and takes your hand.{/n}
"Walk me downstairs. We can be two people who ate too much soup for a few minutes."''',
      c('[Walk downstairs with her.]', flags=("kiana.guest_table.kept",))),
], after="kiana.morning")


s("market_weather", "The color in daylight", [
    n("start", "Kiana", '''{n}You find Kiana beneath a cloth seller's awning, holding a length of deep blue fabric beside her face. Rain runs from one corner of the canvas into a carefully positioned bucket.{/n}
"Be honest. Does this make me look magnificent, or like an expensive bruise?"
{n}She lowers it before you can answer.{/n}
"The light inside was yellow. I was magnificent there. Outside I became a bruise. The seller has been very patient about it."
{n}The seller folds another piece of cloth without looking up. "The green was better."{/n}
"The green was beyond my purse. It had every advantage."
{n}Kiana smiles when she sees the empty jar you have brought at her request.{/n}
"Good. We can return that on our way. Lenna hasn't answered my note. She may be busy. She may also be hiding behind a great many shoes."''',
      c('"Show me the blue in proper light."', "color"),
      c('[Apologize for being unable to keep the outing, and arrange another day.]', abort=True)),
    n("color", "Kiana", '''{n}She steps to the edge of the awning. Beneath the gray sky, the cloth is darker than her blue skin and makes the white crystalline points above her brow seem brighter.{/n}
"There. You may admire me, but try to have an opinion about the fabric as well."
"Is that a difficult distinction?"
"People have failed at easier tasks while looking at a pretty woman."
{n}A drop runs down her wrist. She retreats beneath the awning, shaking it off.{/n}
"I want to look splendid in daylight. Candles have been taking far too much credit."
{n}She lays the cloth down and counts out her own coins. After a brief discussion of lengths, the seller begins cutting.{/n}''',
      c('"The blue suits you. I would like to see you wear it somewhere crowded."', "public", flags=("kiana.market_weather.public",)),
      c('"The blue suits you. I am imagining a walk where we can hear each other."', "quiet", flags=("kiana.market_weather.quiet",))),
    n("public", "Kiana", '''"Somewhere crowded? How scandalous. People might discover I buy cloth and eat supper."
{n}Her amusement softens as she follows your glance toward the market.{/n}
"Take me through the market. Let them discover that the vampire princess buys onions."
{n}She accepts the wrapped cloth from the seller.{/n}
"If anyone mentions Elan, I shall answer. You can hold the jar and look magnificent."
"I won't ask you to."
"Good. You may be seen carrying my jar. It is a position of considerable distinction."''',
      c('[Take the jar and walk beside her.]', "recognition")),
    n("quiet", "Kiana", '''"Somewhere with fewer people explaining how pleased they are for me? Tempting."
{n}She accepts the wrapped cloth, then studies you over it.{/n}
"A quiet walk, then. Choose an alley that smells of bread; I refuse to be mysterious beside a drain."
"We can begin with one that doesn't."
"Ambitious. I approve."
{n}She gestures toward the open market.{/n}
"Lenna first. If she's hiding, I shall have to be braver than an empty jar."''',
      c('[Carry the jar as you leave the awning.]', "recognition")),
    n("recognition", "Narrator", '''{n}A woman carrying a covered basket recognizes Kiana and stops. Kiana introduces her as Edris, who lives beside Lenna's workshop. Edris gives you a startled nod and nearly dislodges the cloth covering her basket.{/n}
{n}"Eggs," she explains, though nobody has asked. "I ought to get them home. Kiana, are you coming to the supper on Lenna's roof? She said she hadn't asked you yet."{/n}
{n}Kiana's smile becomes still.{/n}
{n}"I hadn't heard about it."{/n}
{n}"Oh. Well, it's only a few of us. Odrin will be there. I thought you knew." Edris shifts the basket. "I'd better go before I turn these into something that needs cooking immediately."{/n}
{n}She leaves. Rain splashes into a gutter beside your feet. Kiana watches the water for a moment, then takes the jar back.{/n}''',
      c('"She invited Odrin and forgot you?"', "hurt"),
      c('"Do you want to ask Lenna about it?"', "ask")),
    n("hurt", "Kiana", '''"Yes. How inconvenient. I had prepared several excellent reasons not to be upset about an unanswered note."
{n}She hooks a finger through the jar's handle.{/n}
"Perhaps she thought I wouldn't enjoy it. Perhaps she's cross with me. Perhaps Edris was supposed to keep quiet and we have just witnessed a complete failure of neighborhood intrigue."
{n}Kiana looks toward the lane leading to Lenna's shop.{/n}
"I could spend the whole afternoon inventing explanations. I'd like to hear hers."''',
      c('"Then let us go."', "past")),
    n("ask", "Kiana", '''"Yes. Though I would prefer her to appear here, looking ashamed and carrying a very persuasive cake."
{n}She looks down at the jar.{/n}
"One sharp word and Lenna has banished me from her roof. What a delicate little tyrant."
{n}She turns toward the lane.{/n}
"Come along. If she has hidden behind a shoe, you can help me drag her out."''',
      c('[Walk with her toward the workshop.]', "past")),
    n("past", "Narrator", '''{n}The rain eases. You stop beneath an arch while Kiana tucks the cloth more securely under her arm. She looks at you as though she is deciding whether to say something.{/n}''',
      c('[Give her time.]', "waited", requires=("kiana.waited", "kiana.separated"), forbids=("seelah.elan_dead", "kiana.bereaved")),
      c('[Give her time.]', "affair", requires=("kiana.affair", "kiana.separated"), forbids=("seelah.elan_dead", "kiana.bereaved")),
      c('[Give her time.]', "widow", requires=("kiana.bereaved", "seelah.elan_dead"), forbids=("kiana.separated",))),
    n("waited", "Kiana", '''"You waited while I spoke to Elan. I was glad of it. I still am."
{n}She watches a droplet slide down the jar.{/n}
"Sometimes I catch myself wanting that to make everything afterward simple. We did one difficult thing carefully. Surely we ought to be rewarded with several easy ones."
"How many?"
"At least six. I am prepared to negotiate."
{n}She smiles and steps out from beneath the arch.{/n}
"Lenna didn't promise us an easy afternoon. Neither did I. Come along."''', c('[Continue with her.]', "shut")),
    n("affair", "Kiana", '''"At supper I said I made choices. I meant the kiss too. I haven't forgotten it because there are nicer things to say now."
{n}She shifts the cloth against her side.{/n}
"If Lenna wants to scold me about the kiss, she can do it to my face. You will not be blamed for carrying me off."
"I was there. I won't give her that story."
"Thank you. You may still sweep me away on some occasion that doesn't require anyone else to be lied to. Preferably in dry weather."
{n}She steps from beneath the arch and waits for you.{/n}''', c('[Continue with her.]', "shut")),
    n("widow", "Kiana", '''"They tiptoe round me until I want to shout. Then I shout, and they tiptoe harder. Desna preserve me."
{n}She watches the rain beyond the arch.{/n}
"Elan would have liked Lenna's roof. You can see quite a long way from it. I don't know whether I would have said that aloud if she had invited me. Perhaps I would."
"You can say it to me."
"I want to see that roof with you. Elan had a good eye for a view, the wretch."
{n}She turns the jar so its chipped side faces inward.{/n}
"Let's find out whether we're invited before I spend the whole afternoon worrying about attending."''', c('[Continue with her.]', "shut")),
    n("shut", "Kiana", '''{n}Lenna's door is locked. A note asks customers to return tomorrow. Kiana reads it, tests the latch once, and puts the jar back into your hands.{/n}
"Well. That was a very stirring journey to a closed door."
{n}She takes a scrap of paper from the cloth's wrapping and writes against the wall, using the little pencil tied beside the customer notice.{/n}
"I shall come tomorrow. I would like to see you. There. No accusations she can read six times before I arrive."
{n}She slips the note beneath the door.{/n}
"Keep me company then, if you can. For now, I would like to get this cloth somewhere dry before the color becomes everybody else's problem."''',
      c('[Arrange to meet her tomorrow, and take the jar with you.]', flags=("kiana.market_weather.walked",))),
], after="kiana.guest_table", delay=24)


s("lenna_door", "The unasked invitation", [
    n("start", "Kiana", '''{n}This time Lenna's door stands open. Kiana is waiting outside it, wearing her old cloak. She takes the jar from you with a conspiratorial glance.{/n}
"If we are here all afternoon, I intend to leave this behind. I refuse to become emotionally attached to a pickle jar."
{n}Inside, Lenna sits on a low stool with a boot between her knees. A young man with a full beard stands on one bare foot beside her, holding his other boot and looking miserable.{/n}
{n}"He dried them beside the fire," Lenna says by way of greeting. "Then complained they were stiff."{/n}
{n}"They were wet," the man protests.{/n}
{n}"You have certainly cured that."{/n}
{n}Kiana gives him a sympathetic look and places the jar on the counter. Lenna glances at the note lying beside her tools, then at you.{/n}''',
      c('[Wait until Lenna has finished with her customer.]', "finished"),
      c('[Ask Kiana to arrange another visit when you have time to stay.]', abort=True)),
    n("finished", "Narrator", '''{n}The customer pays for a repair that will take until morning and leaves in borrowed shoes too large for him. Lenna watches his careful progress past the window.{/n}
{n}"I'll have to get those back before Odrin notices," she says.{/n}
{n}"Did Odrin lend them?" Kiana asks.{/n}
{n}"He left them here. He knows what I am like." Lenna puts down her tools. "I got your note."{/n}
{n}"I hoped you had. I was beginning to feel rather foolish about the jar."{/n}
{n}Lenna looks at it as though she might hide inside.{/n}
{n}"You heard about the supper."{/n}
{n}"Yes."{/n}
{n}"I thought you wouldn't want to come. After I made such a mess of the last one."{/n}
{n}Kiana pulls up two chairs, sits in one and pats the other for you.{/n}''',
      c('[Stay beside Kiana.]', "earlier")),
    n("earlier", "Narrator", '''{n}Lenna rubs at a spot of polish on her thumb. Her eyes keep returning to you.{/n}''',
      c('[Hear what she wants to say.]', "commander_spoke", requires=("kiana.guest_table.spoke",)),
      c('[Hear what she wants to say.]', "kiana_spoke", requires=("kiana.guest_table.listened",))),
    n("commander_spoke", "Kiana", '''{n}"I didn't fancy being corrected by the Commander in front of everyone," Lenna says. "I know that isn't a generous thing to admit."{/n}
"There were four of us, Lenna. One was trapped behind a table."
"It felt like everyone."
{n}Kiana lets the joke fall.{/n}
"All right. It felt like everyone. But you don't get to leave me out of the next supper so you won't have to feel it again. You could have asked whether I wanted to come alone."
{n}Lenna turns toward you.{/n}
"I thought you were angry."
{n}Kiana does not answer for you.{/n}''',
      c('"I disliked what you said. I came today because Kiana wanted to see her friend."', "plain"),
      c('"I meant what I said. Now, have you saved any plum wine for us?"', "rank")),
    n("kiana_spoke", "Kiana", '''{n}"You looked at me as though you didn't know me," Lenna says.{/n}
"I was trying to decide how much to say. If I had been speaking to a stranger, I probably would have let it pass."
{n}Lenna bends over the boot, then sets it aside without doing anything to it.{/n}
"And the Commander didn't say a word. I couldn't tell what that meant."
"It meant I was speaking."
{n}Kiana looks at you, her mouth twitching.{/n}
"But I imagine there was some thinking involved as well."''',
      c('"I disliked what you said. I came today because Kiana wanted to see her friend."', "plain"),
      c('"Kiana had the floor. I was enjoying the view."', "listen")),
    n("plain", "Kiana", '''{n}Lenna nods, slowly this time.{/n}
"I was afraid you hated me. It seemed safer to hide behind a boot."
"I still brought the jar back," Kiana says. "If I hated you, I would have kept it and sent Odrin to explain why."
{n}Lenna laughs before she can prevent it. Kiana waits for her to finish.{/n}
"I want to see you. But you have to invite me. I can't keep finding out about my own absence from Edris."''',
      c('[Give Lenna room to answer.]', "invitation", flags=("kiana.lenna_door.plain",))),
    n("rank", "Kiana", '''{n}"It did," Lenna says. "People usually come to me when their shoes hurt. They don't bring the person in charge of the city."{/n}
"I brought someone I wanted you to like," Kiana says. "I may have been rather hopeful about how easy that would be."
{n}She glances at you.{/n}
"Yes, the Commander commands things. At supper I expect that to be confined to passing the bread."
{n}Lenna exhales.{/n}
"I was embarrassed. There. A complete absence of mystery."
"Much better. I would have needed another jar to carry all the explanations I was inventing."''',
      c('[Let the conversation continue.]', "invitation", flags=("kiana.lenna_door.rank",))),
    n("listen", "Kiana", '''{n}"You could have said that," Lenna tells you, then hears herself and looks at Kiana. "No. You couldn't very well interrupt to announce that you weren't interrupting."{/n}
"It would have been a magnificent speech," Kiana says. "Brief, but memorable."
{n}Lenna laughs and leans back on her stool.{/n}
"I am making this worse."
"You are talking to us. That's already an improvement on deciding we wouldn't want to come."
{n}Kiana rests her hands on her knees. She has stopped watching the door.{/n}''',
      c('[Let Lenna finish.]', "invitation", flags=("kiana.lenna_door.listened",))),
    n("invitation", "Narrator", '''{n}"Would you come?" Lenna asks Kiana. "Both of you. Odrin has been making an awful drink with plums in it. He needs a wider audience to tell him how awful it is."{/n}
{n}"Is he aware that's the reason?"{/n}
{n}"He thinks we want the recipe."{/n}
{n}Kiana looks toward you, then back to Lenna.{/n}
"Yes, both of us. Cross or not, you can ask me yourself next time."
{n}"I'm sorry," Lenna says. "I spoke like an idiot over your own soup."{/n}
{n}"No. I might still need you telling me about the dog."{/n}
{n}Lenna begins to smile, then groans. "He's acquired a collar. Odrin claims it was a gift."{/n}''',
      c('[Ask when the supper begins.]', "outside")),
    n("outside", "Kiana", '''{n}You leave with an evening arranged and the jar finally returned. Kiana walks several steps before stopping to examine the heel of her shoe.{/n}
"I should have asked her about this. I was too busy being dignified."
{n}She looks back at the shop. Lenna raises a hand through the window. Kiana raises hers in return.{/n}
"I'll come back tomorrow. For the shoe. I think I can manage to be a customer again."
{n}She turns toward you.{/n}
"Thank you for coming. I should have thrown the jar if I had been left alone with it."
{n}She reaches for your hand and tugs you gently into step.{/n}
"Now take me somewhere for a drink that doesn't have plums in it. I must save my courage."''',
      c('[Walk with her to find a drink.]', flags=("kiana.lenna_door.invited",))),
], after="kiana.market_weather", delay=24)


s("blue_room", "What she takes with her", [
    n("start", "Kiana", '''{n}Kiana has asked you to meet her before Lenna's supper. The new blue cloth lies across a chair, now hemmed into a shawl. She holds two fastening pins against it and studies their effect in a small mirror.{/n}
"If you say you prefer the one I have just put down, I shall suspect you of doing it deliberately."
{n}She catches your reflection and smiles. Her blue-green eyes are brighter than the cloth. The pins are plain brass, one round and one shaped like a leaf.{/n}
"Come in. Mind the box. I was looking for these and found considerably more of my life than I meant to."''',
      c('[Join her, leaving the box undisturbed.]', "box"),
      c('[Explain that you need to leave, and ask to meet before another supper.]', abort=True)),
    n("box", "Kiana", '''{n}The box holds folded clothes, a cracked comb and several ribbons wound around pieces of card. Kiana puts the pins down and lifts a dark length of fabric from the top.{/n}
"Part of an old costume. I used to be able to pack a whole kingdom into this box. Now it won't hold two shawls without an argument."
{n}She drapes the fabric over her arm, then returns it to the box.{/n}
"Tonight the princess stays in her box. I am going to drink Lenna's wine and complain if it is dreadful."
{n}She bends to move the box beneath the table, then pauses with her hand on its lid.{/n}''',
      c('[Stay while she decides what to say.]', "bereaved", requires=("kiana.bereaved", "seelah.elan_dead"), forbids=("kiana.separated",)),
      c('[Stay while she decides what to say.]', "separated", requires=("kiana.separated",), forbids=("seelah.elan_dead", "kiana.bereaved"))),
    n("bereaved", "Kiana", '''"I nearly put Elan's letter in here. Imagine sharing a drawer with that comb for eternity."
{n}She closes the lid without adding anything.{/n}
"The letter is where I can find it. I read it again this morning. It made me cry. Then I was cross because I wanted my eyes to look nice tonight."
{n}She touches the corner of one eye, checking for the damp that is no longer there.{/n}
"There. A very small and selfish complaint. I almost didn't tell you."
"Your eyes look like yours."
"How fortunate. I had nothing suitable to replace them with."
{n}Her laugh comes unevenly, but it comes.{/n}
"I still want to go. These eyes have survived crying; now let Lenna admire them."''',
      c('"Lenna can wait while you choose the pin."', "pin"),
      c('"Would you like to tell me what you read?"', "letter")),
    n("letter", "Kiana", '''"Not the words. I would like to keep those today."
{n}She pulls the chair closer and sits, leaving the shawl over its back.{/n}
"But I can tell you how I read them. Slowly at first. Then all at once, as though something might have changed at the bottom since last time."
{n}She looks at her empty hands.{/n}
"It hadn't. I knew it wouldn't. I still looked."
{n}For a while you sit with her. Outside, somebody calls up the stairwell for a missing basket. A door opens, an answer comes, and the building settles again.{/n}
{n}Kiana takes a breath and reaches behind her for the shawl.{/n}
"All right. Help me choose before I turn this into the greatest fastening dispute in Mendev."''',
      c('[Look at the two pins with her.]', "pin", flags=("kiana.blue_room.letter",))),
    n("separated", "Kiana", '''"I wondered whether I ought to put the picture in here. Just while you were visiting."
{n}She looks toward the little picture she kept after separating from Elan. It still hangs where you saw it before.{/n}
"Then I imagined explaining why the wall had developed a pale rectangle, and felt ridiculous. You have already seen it."
{n}She shuts the box.{/n}
"The picture stays. If I hide it, I shall have to invent a splendid explanation for the mark on the wall."
"You told me why you kept it."
"Yes. I was braver about it that evening. People ought to be more consistent. It would save a great deal of time."
{n}She looks at you, waiting for an answer she has not supplied herself.{/n}''',
      c('"Leave it there. I want to know the woman who lives in this room."', "picture"),
      c('"Leave it there. Your shawl is winning my attention anyway."', "learning")),
    n("picture", "Kiana", '''"You will have to endure the comb too, then. It has broken two teeth and I keep expecting it to improve."
{n}She pushes the box beneath the table with her foot.{/n}
"Good. I refuse to have the picture interrogated every time you visit."
{n}She picks up the shawl, then lets it hang between her hands.{/n}
"I do want you here. In case I have made that sound like a discussion about storage."''',
      c('"You haven\'t. Show me the pins."', "pin", flags=("kiana.blue_room.picture",))),
    n("learning", "Kiana", '''"I tried moving everything twice. Apparently furniture is no substitute for a good entrance."
{n}She glances at the wall.{/n}
"If that wall offends you, say so. I can put a dreadful portrait of the princess there instead."
"It is a perfectly agreeable wall."
"Good. I shall let it know."
{n}She picks up the shawl. Her smile is warmer now.{/n}
"I want you here. Come and admire something that can blush back."''',
      c('[Turn your attention to the pins.]', "pin", flags=("kiana.blue_room.learning",))),
    n("pin", "Kiana", '''{n}Kiana puts on the shawl. The dark blue falls below her shoulders, leaving the pale crystalline shape of her head uncovered. She holds the round pin against the fold, then the leaf.{/n}
"One opinion. I reserve the right to ignore it."
"Naturally."
"You say that very readily. It suggests experience."''',
      c('"The leaf. I like the way it catches the light when you move."', "leaf", flags=("kiana.blue_room.leaf",)),
      c('"The round one. It leaves my attention on your face."', "round", flags=("kiana.blue_room.round",))),
    n("leaf", "Kiana", '''"An answer with a compliment attached. You have been paying attention."
{n}She fastens the leaf through the fold and turns toward the lamp. The brass flashes once.{/n}
"There. If Odrin asks, I shall tell him you chose it after a bitter struggle."
{n}She comes close enough for you to see the tiny scratches on the pin.{/n}
"Would you like to admire the rest before we go? I have put a great deal of effort into appearing casually dressed."''', c('[Look at her.]', "want")),
    n("round", "Kiana", '''"A shameless answer. Unfortunately it worked."
{n}She fastens the round pin through the fold, checks the result and leaves the mirror alone.{/n}
"There. You must defend your choice if Lenna has opinions. She usually does."
{n}She steps closer and tilts her face toward you.{/n}
"You may begin by making good on your promise to pay attention."''', c('[Look at her.]', "want")),
    n("want", "Kiana", '''{n}For a moment Kiana stays still under your gaze. Then her pleased expression grows less composed.{/n}
"I wanted this part of the evening too. The part before anyone else arrives. I almost wore something absurdly elaborate so you'd have to notice."
{n}She reaches for your hand.{/n}
"I am glad I didn't. I would still be fastening it when Lenna began serving supper."''',
      c('[Kiss her before you leave.]', "kiss", flags=("kiana.blue_room.kissed",)),
      c('[Take her hand and tell her you are glad to be going with her.]', "hand")),
    n("kiss", "Kiana", '''{n}Kiana meets you with a smile that does not survive the kiss. Her hand closes around yours; when you draw apart, she keeps it there.{/n}
"We ought to leave."
{n}She does not move immediately. Then she laughs at herself, retrieves her small purse, and leads you toward the door.{/n}
"Before I begin arguing with my own excellent advice."''', c('[Go with her.]', flags=("kiana.blue_room.ready",))),
    n("hand", "Kiana", '''"So am I. Even if the drink is dreadful."
{n}She squeezes your hand, then takes her purse from the table.{/n}
"Come along. If we arrive late, Odrin will have explained how he made it before we can stop him."''', c('[Go with her.]', flags=("kiana.blue_room.ready",))),
], after="kiana.lenna_door", delay=48)


s("roof_supper", "A place among the guests", [
    n("start", "Narrator", '''{n}Lenna meets you at the top of the stairs, carrying a jug in one hand and a folded towel in the other. A drop of purple liquid lands on her shoe.{/n}
{n}"Before anyone asks, it was an accident," she says. "I have not begun pouring it away."{/n}
{n}"I heard that," Odrin calls from the roof.{/n}
{n}The table is made from two doors laid across trestles. There are stools enough for everyone, though several appear to have been borrowed from people of quite different heights. Edris sits on the tallest, shelling peas into a bowl. Beyond her, the late sun lights the broken edges of Drezen's roofs.{/n}
{n}Kiana takes the towel before the stain can spread. Lenna notices her new shawl.{/n}''',
      c('[Join them.]', "leaf", requires=("kiana.blue_room.leaf",)),
      c('[Join them.]', "round", requires=("kiana.blue_room.round",)),
      c('[Send an apology and ask to join them another evening.]', abort=True)),
    n("leaf", "Narrator", '''{n}"That suits you," Lenna says. "Especially the leaf."{/n}
{n}"The Commander insisted," Kiana tells her. "It was a bitter struggle."{/n}
{n}She catches your eye over Lenna's shoulder. The tiny brass leaf flashes as she bends to wipe the spilled drink.{/n}
{n}"One opinion," you remind her.{/n}
{n}"An exceedingly forceful opinion. Fortunately, you were right."{/n}
{n}Lenna looks puzzled for a moment, then leaves you your private joke and offers to hang up the shawl. Kiana shakes her head and settles it more securely.{/n}''',
      c('[Help carry the jug to the table.]', "cups")),
    n("round", "Narrator", '''{n}"A leaf would have looked nice," Lenna says, considering the round pin.{/n}
{n}"There was a leaf," Kiana replies. "I brought an advocate for the opposition."{/n}
{n}She turns toward you, plainly expecting you to defend yourself.{/n}
{n}"She asked for my opinion. I gave it."{/n}
{n}"You gave it very prettily." Kiana wipes Lenna's shoe, then straightens. "I may ask again. Don't let that alarm you."{/n}
{n}Lenna offers to hang up the shawl. Kiana keeps it on, smoothing the fold around the round pin before following you to the table.{/n}''',
      c('[Make room beside you.]', "cups")),
    n("cups", "Kiana", '''{n}Odrin pours a little of his drink into each cup. He begins explaining before anyone has tasted it.{/n}
"Plums," Kiana says. "We had guessed that much."
{n}"There's more to it than plums."{/n}
"I am afraid there may be."
{n}She tastes it. Her eyebrows rise.{/n}
"Oh. That's rather good."
{n}Lenna looks betrayed. Edris takes a cautious sip and agrees with Kiana.{/n}
{n}"It had better be," Odrin says. "I poured yesterday's away."{/n}
"You made us practice on the first attempt?"
{n}"I needed opinions."{/n}
"Then ask the Commander next time. I can recommend the service."
{n}The meal begins while Odrin is still defending his methods. Nobody raises a toast to Kiana's recovery. Edris asks whether she would like more bread, and receives a cheerful request for the piece with the most crust.{/n}''',
      c('[Stay with the table conversation.]', "public", requires=("kiana.market_weather.public",)),
      c('[Share the meal, then find a moment with Kiana.]', "quiet", requires=("kiana.market_weather.quiet",))),
    n("public", "Kiana", '''{n}Edris wants to know what Kiana has been writing. Kiana begins with the princess and the stolen moon, then stops herself.{/n}
"I am explaining it badly. You ought to hear a little. Commander, would you?"
{n}She turns toward you with an expression you recognize from the borrowed castle.{/n}
"You wanted somewhere crowded. I have found four people and an audience that can't escape without passing the pudding."
{n}"Three," Lenna says. "You're counting yourself."{/n}
"I am very interested in my own work."
{n}She leans closer to you.{/n}
"Take the guest's part, or I shall give it to Odrin and make you listen to him."''',
      c('"Give me a part. Something with a short speech."', "perform"),
      c('"Tell it. I want to hear which parts you like best."', "tell")),
    n("perform", "Narrator", '''{n}Kiana appoints you keeper of the castle doors, charged with explaining why nobody has brought the princess supper. Your explanation involves a stolen moon, a missing cook and a staircase that has changed its mind about where it leads.{/n}
{n}She rejects every excuse until you suggest that the princess could fetch her own supper. Then she rises with great dignity, takes the bread basket and announces that the keeper is dismissed for excessive wisdom.{/n}
{n}Lenna laughs with her mouth full. Odrin objects that a good staircase would never behave so badly. He gives Kiana three better excuses, of which she immediately steals two.{/n}
{n}"You should do this properly," Edris says. "With the rest of it written down."{/n}
{n}"Finish it? Certainly. Advertise me without warning and I shall give you the villain's part, Edris."{/n}
{n}Lenna raises her cup. "A villain who brings pudding, I hope."{/n}
{n}"A pudding would still be acceptable."{/n}''',
      c('[Ask Kiana to read you the next version when it is ready.]', "later", flags=("kiana.roof_supper.performed",))),
    n("tell", "Narrator", '''{n}Kiana begins again, this time with the princess attempting to hide the moon in a cupboard. She tells it with her hands, moving cups and the bread basket to stand for the court. Odrin's cup becomes a particularly foolish chamberlain.{/n}
{n}"I need that," he protests.{/n}
{n}"The chamberlain has duties."{/n}
{n}By the time he recovers his drink, Lenna is asking how the princess means to put the moon back. Kiana tries two endings aloud. Neither pleases her, but she writes down a suggestion from Edris on the clean corner of a paper bag.{/n}
{n}You have heard her read in a room where every laugh belonged to you. Here she has to wait for Odrin to understand a joke and defend a line Lenna finds too solemn. She looks annoyed once, then interested. The princess survives both.{/n}
{n}"I shall tell you when it's finished," she says. "And I shall expect you to remember which suggestions were yours."{/n}''',
      c('[Offer to listen to the next version.]', "later", flags=("kiana.roof_supper.told",))),
    n("quiet", "Kiana", '''{n}After the bowls have been passed around a second time, Kiana takes her cup to the low wall overlooking the lane. She leaves space beside her. Behind you, Odrin and Edris disagree about the amount of sugar a plum ought to require.{/n}
"You wanted a walk where we could hear each other. Will this do for a beginning?"
{n}She looks over the roof rather than down into the lane.{/n}
"I thought I would spend all evening waiting for Lenna to say something dreadful. She has mostly been concerned with the food. I find I am quite hungry."
"There is more bread."
"I know. I have been keeping track."
{n}She puts her shoulder beside yours against the wall.{/n}
"I'm glad we came. Now I have stolen you from the table, and I intend to enjoy the theft."
{n}For a while you watch a woman below trying to close her shutters around an obstinate flowerpot. She finally takes it inside. Kiana raises her cup in silent approval.{/n}
"There. A satisfactory ending. I should borrow it."
{n}Lenna calls over to ask whether you want pudding. Kiana answers for herself at once.{/n}
"Yes. But save it. We're talking."''',
      c('[Stay with her a little longer, then return to the table.]', "later", flags=("kiana.roof_supper.quiet",))),
    n("later", "Narrator", '''{n}When the plates are empty, Edris remembers a question about somebody called Meral and another supper. He has asked her to find out whether Kiana is free next week.{/n}
{n}"He's taken over the room above the bakery," she explains. "He says you know which one."{/n}
{n}"I know the stairs. I once climbed them in a dress that wasn't made for climbing anything." Kiana smiles, then waits for Edris to finish.{/n}''',
      c('[Let Kiana answer.]', "separated", requires=("kiana.separated",), forbids=("kiana.bereaved", "seelah.elan_dead")),
      c('[Let Kiana answer.]', "widow", requires=("kiana.bereaved", "seelah.elan_dead"), forbids=("kiana.separated",))),
    n("separated", "Kiana", '''{n}"He'll have asked Elan too," Edris adds. "I don't know whether you knew."{/n}
"I didn't. Thank you for telling me. I will ask Meral what he has arranged."
{n}Edris glances at you. Kiana follows the glance, then turns back to her.{/n}
"I shall write to Meral. If Elan is coming, I want to know before I trip over him on the stairs."
{n}"Of course," Edris says.{/n}
{n}Kiana reaches for the last piece of crust and breaks it in half, offering you one piece.{/n}
"You are invited to this bread crust. Meral's supper must wait until he answers my letter."
{n}Her voice is low enough to keep the explanation between you.{/n}''',
      c('"Send me word after Meral answers."', "stairs")),
    n("widow", "Narrator", '''{n}"Nothing elaborate," Edris says. "He wants to show off the room."{/n}
{n}Kiana looks down at her plate. "Elan helped him move the table. They got it stuck halfway up. Meral was so sure that taking the legs off would be more trouble."{/n}
{n}"Did they get it loose?" Lenna asks.{/n}
{n}"Eventually. Elan was at the bottom. He said that gave him an interest in the outcome." Her smile falters. She rubs at the edge of her plate, then looks up. "Please tell Meral I'd like to hear from him."{/n}
{n}Odrin moves the bread basket within her reach. Kiana takes the last piece and tears off a corner.{/n}
{n}Lenna asks Edris which door leads to the room. When Edris cannot remember, Kiana supplies it. She stays at the table until the cups are empty.{/n}''',
      c('[Keep her company as the evening ends.]', "stairs")),
    n("stairs", "Kiana", '''{n}You carry the empty jug downstairs while Kiana holds the lamp. At the bottom she sets it beside Lenna's workbench and looks back up toward the voices on the roof.{/n}
"I didn't know how much I wanted to be asked about the next supper until someone did it."
{n}She rubs a thumb across the pin at her shoulder.{/n}
"Take me home before I begin accusing a perfectly good evening of misconduct."
{n}She takes your arm as you step into the lane. There is nobody waiting there to congratulate either of you.{/n}
"Walk with me? We needn't be interesting. I am quite prepared to admire a wall or complain about my shoes."''',
      c('[Walk her home.]', flags=("kiana.roof_supper.kept", "kiana.consequences_ready"))),
], after="kiana.blue_room", delay=0)

# Getting ready and supper are one evening. A separate remote scene would wait
# for another rest even with zero delay, so continue within the same book.
supper = SCENES.pop()
preparation = SCENES[-1]
assert supper["Id"] == "kiana.roof_supper" and preparation["Id"] == "kiana.blue_room"
for page in preparation["Nodes"]:
    for choice in page["Choices"]:
        if choice["Next"] is None and "kiana.blue_room.ready" in choice["Set"]:
            choice["Next"] = "supper_start"
for page in supper["Nodes"]:
    page["Id"] = "supper_" + page["Id"]
    page["Choices"] = [choice for choice in page["Choices"] if not choice["Abort"]]
    for choice in page["Choices"]:
        if choice["Next"] is not None:
            choice["Next"] = "supper_" + choice["Next"]
preparation["Nodes"].extend(supper["Nodes"])

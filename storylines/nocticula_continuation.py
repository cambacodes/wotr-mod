"""Living, gifted Chapter 5 continuation of the accepted RanRomance dream bargain.

New incidents and named agents are authored fiction. All participants are adults.
Dreams carry the sleeping Commander into her real court (user decision 2026-10-07).
This module does not implement acquisition, resurrection, gift replacement, or a triad.
"""
from copy import deepcopy
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
ETUDES = {
    "noct.parent_active": "18affced672d4c56a52bf6ffc00601b9",
    "noct.parent_initial": "8a28bbd82568486bb757d00a2087a6cf",
    "noct.parent_rejected": "761ca3572c1145ebb755032d613bff46",
    "noct.parent_laulieh": "9591c34df22b4d518a059cf608255458",
    "noct.parent_laulieh_departure": "19e5d6f04b9b4483b2e2979baf8736e4",
    "noct.gift": "0c1695f4a362f0243a4afcfd1957eb0d",
    "noct.dead": "e581f609dc0f44a481e7e88824ac39da",
}
# enGB 43ca3072: Nocticula states the native Aeon trial conditions.
SEEN_CUES = {
    "noct.native_trials_seen": ["a5472a3492d23c542b5f77cb6e591ca3"],
    "noct.parent_agreement_seen": ["631bf0ede36742559cee476f34dcb5de", "cb13766be07b448f8cacb477be32e13c", "5388a7d7a1da48deb333d34abab1a6d0"],
    "noct.parent_ambition_heard": ["b3a4ce99bc30440fa9ebcbfce2776176"],
    "noct.parent_feelings_uncertain": ["1110f2b6304549999fb546e7ecc4c8a1"],
    "noct.socoth_plan_exposed": ["bb552fe4e21cb874fa3c98c2cc328186"],
}
RELATIONSHIP = dict(
    Title="Under her black flower", Description="Someone sold passage under Nocticula's black flower. She wants me watching while she collects.",
    Objective="Sleep, and see what she has caught", Guidance="After accepting RanRomance's Chapter 5 dream relationship, rest in Drezen while Nocticula lives and her Profane Gift remains. While the Gift holds, her dreams carry you into her court; what you decide there happens. These meetings do not recover a missed or rejected relationship.",
    StartedFlag="noct.started", ClosedFlag="noct.closed", CommittedFlag="noct.complete",
    UnavailableFlags=["noct.dead", "inhuman", "legend", "dragon"], FailureFlags=[])
SCENES = []


def f(*names):
    return tuple("noct." + name for name in names)


def s(id, title, nodes, previous=None, delay=12):
    if previous is not None:
        late = id in ("counterseal", "no_applause", "what_she_keeps", "second_door")
        answer = ('"The harbor business is settled. I do not want these private meetings to continue."' if late
                  else '"I am leaving the harbor undertaking. Find someone else to finish it."')
        response = '''{n}She looks away from you. When she speaks, her voice has lost its teasing edge.{/n}
"I invited you because the business was settled. You need not explain the distinction to me."
"Then you understand what I am declining."
"Perfectly. It is an unpleasant advantage of listening."
{n}You wait. She lets the silence grow uncomfortable before she answers.{/n}
"The work stands. So does the answer you have just given. There will be no further invitations to these meetings."
"Our earlier bargain still stands too."
"I did not confuse it with an evening's company. Do me the courtesy of remembering that."
{n}She lifts two fingers. The dream fades around her, and you wake without a new promise.{/n}''' if late else '''{n}For a moment she watches you without answering.{/n}
"You could have told me before I arranged the evening."
"I am telling you before I promise another."
{n}Her gaze sharpens.{/n} "So you are. Do not mistake my willingness to hear an answer for pleasure in receiving it."
{n}She turns one palm upward. The objects of the evening lose their edges, but she remains distinct against the darkness.{/n}
"I shall choose my next adviser more carefully. What you have already done is done. You will receive no further invitations concerning this harbor."
"And our earlier bargain?"
"Was not about a harbor. I have not forgotten its terms because you have tired of these."
{n}She lowers her hand. The dream ends before you can decide whether she meant to dismiss you or spare herself another word.{/n}'''
        nodes[0]["Choices"].append(c(answer, "withdraw_undertaking"))
        nodes.append(n("withdraw_undertaking", "Nocticula", response,
            c('[Leave this undertaking. The earlier bargain remains unchanged.]', flags=f("closed", "undertaking_withdrawn"))))
    for page in nodes:
        page["Portrait"] = "Nocticula"
    SCENES.append(scene("noct." + id, title, "Memory", 5, title, nodes,
        requires=("noct.parent_active", "noct.parent_agreement_seen", "noct.gift") + (("noct." + previous,) if previous else ()),
        forbids=("noct.dead", "noct.parent_rejected", "noct.closed", "inhuman", "legend", "dragon"),
        delay=delay, optional=True, Relationship="nocticula", Remote=True, Areas=[DREZEN], Chapters=[5]))


s("unlit_quay", "The unlit quay", [
    n("start", "Narrator", '''{n}Sleep brings you to a quay without a sea. The mooring ropes hang into darkness, pulled taut by something the dream has not bothered to supply. Nocticula sits on a bollard with one knee crossed over the other. Her dress is black, its hem quite dry despite the rain that falls several yards away.
She watches you notice the missing water. Then she uncrosses her legs and stands.{/n}
"Before you ask: no, you have not drowned. And this is not an improvement to the accommodation I promised you. I require your opinion."
"About a harbor?"
"About a man who has been selling passage through one. He claims to act with my permission. Three of his passengers have disappeared, two have returned richer, and the sixth has offered to sell me his account of the journey."
{n}She passes you a scrap of sailcloth. A black flower has been worked into its edge with exceptionally fine thread. When you turn it over, the reverse is unfinished.{/n}
"My memory of it. The original is in my vault, and my memory is the only one of my rooms you are invited into. Ask me what I did not notice and I shall charge you for the insult."
"You could simply seize him."
"I could seize everyone on the quay. Then I would possess a quay full of frightened liars and no explanation for the two profitable journeys. I want the route. I also want to know who believes I am too distracted to notice it."''',
      c('"You already have servants. What do you want from me?"', "offer"),
      c('"You noticed what I did with your brother\'s plan. Is this related?"', "council", requires=f("socoth_plan_exposed"))),
    n("council", "Nocticula", '''"Related in the sense that I have recently been reminded how entertaining it is when someone brings me the part of a scheme its author meant to conceal."
{n}She takes back the cloth and lets it trail between her fingers.{/n}
"Do not turn that into a general pardon for everything a member of your Council might attempt. I have not forgotten whose spells brought you into my palace. Nor do I intend to reward every intrusion merely because one proved useful."
"But you remember the useful one."
"I remember useful things. It is among the habits that have kept me alive."
{n}The rain moves closer to the edge of the quay. Nocticula glances at it and the shower stops, leaving a line of silver drops suspended in the air.{/n}
"Your brother's enemy can still want something from you that your brother would approve of."
"Precisely. You are beginning to understand the difficulty of finding agreeable company."
{n}Her smile turns more personal as she comes to stand beside you.{/n}
"I want to see which question you ask when a problem does not come with a crusader already pointing at the correct villain. After that, we may discuss rewards."''', c('"Then give me the problem, without choosing my answer for me."', "offer")),
    n("offer", "Nocticula", '''"An independent appetite. Most of my agents know what answer would please me. You have occasionally demonstrated the irritating ability to want a different answer."
"And our existing arrangement?"
"Continues. This is not a new price secretly added to it. The Worldwound remains the price we discussed, and you are still quite capable of disappointing me about that."
{n}She turns the cloth over again. The unfinished flower exposes the knots beneath its beautiful surface.{/n}
"This undertaking is smaller. You help me understand a private trade route. You learn something I would otherwise keep to myself. If we enjoy the work, there may be other reasons to keep meeting. I am not proposing an oath."
"You are withholding the passenger's name."
"Until you decide whether you want to hear him. He is a mortal thief, by his own account an exceptional one, and he has already tried to sell my agent the same story twice at two prices. I have not brought you an orphan to weep over. I have brought you a liar, and I want to watch what you make of him."
{n}She lifts your hand and sets the cloth in it. Her fingers remain for a moment after she could have released it.{/n}
"You may also decline. I shall find another use for the evening. Probably one you would have enjoyed."
{n}The dark waterless space below the quay gives a slow, hollow creak. Somewhere a ship is moving against its ropes.{/n}''',
      c('"I will hear him. No promise to like what either of you wants."', flags=f("started", "invitation_accepted")),
      c('"Another evening. I want you tonight, without a new undertaking."', "later"),
      c('"No. I will not take on this undertaking. Do not bring it to me again."', "decline_undertaking")),
    n("decline_undertaking", "Nocticula", '''{n}She takes back the embroidered cloth.{/n}
"I had expected curiosity to win. How disappointing to discover you can ration it."
"You offered me a choice."
"Yes. I reserve the right to dislike your use of it."
{n}She folds the unfinished flower inward. The ropes beneath the quay slacken, and the unseen ship drifts away.{/n}
"I will take this elsewhere. Our earlier agreement remains precisely what it was. You have declined an invitation, not renegotiated the Worldwound."
{n}You wake without accepting her undertaking. No further harbor invitation follows.{/n}''',
      c('[Decline the harbor undertaking permanently.]', flags=f("closed", "undertaking_declined"))),
    n("later", "Nocticula", '''"A dangerous preference to confess. I might begin expecting you to distinguish my company from my opportunities."
{n}She closes her hand over yours, hiding the flower between your palms. The quay becomes a narrow balcony. Beyond its rail the city is made of lights you cannot quite count. Nocticula places the cloth on the balustrade and turns her attention to you.
For the rest of the dream she supplies no passenger, route, or price. She supplies herself. The black dress comes open one hook at a time while she watches you watch her do it; the rail is cold against your back when she pins you to it with one hand flat on your chest, and her mouth finds your throat as if she were looking for the pulse to bite. When she has had enough of your standing, she pushes you down onto the cushions heaped along the balcony and follows you down, a knee on either side of you, her hair falling round both your faces, and the city of lights goes on burning beyond the rail.
Later, the flower is still where she put it on the balustrade: a question she has no intention of letting you forget.{/n}
"Tell me when you have finished being sensible," {n}she says, as the dream begins to thin.{/n} "I have work for you when you are."
{n}You wake with the memory of her laugh and no new obligation. The proposed undertaking can wait for another sleep.{/n}''', c('[Leave the invitation unanswered for now.]', abort=True)),
], delay=0)

s("sixth_passenger", "The sixth passenger", [
    n("start", "Narrator", '''{n}The next dream supplies the sea. It is shallow enough for you to see broken pottery below the quay, each shard moving with a current that does not disturb the surface. A chair stands in the water. A broad-shouldered man in a travel-stained red coat occupies it, his boots braced against its front legs.
He looks real until he raises his hand and repeats the same small motion twice. Nocticula stops the image with a gesture.{/n}
"Orren Vale. My agent questioned him this morning. This is a reconstruction from her account, with his recorded replies. It can tell us what he said. It cannot answer questions nobody asked."
"You have made him rather uncomfortable."
"That was the actual chair. He complained about it with admirable persistence."
{n}She releases the image. Orren rubs his knee, looks past you toward the place where his interviewer must have stood, and begins his story.
He bought a passage under the Black Flower's protection. The ship did not cross the open sea. Its captain brought it against a cliff, and a door appeared in the rock where the waves struck. Beyond lay a dry harbor with six lamps. He unloaded sealed cases, received a purse of silver, and returned by the same way.
On his second voyage, there were five lamps. He asks whether this difference might be valuable enough to pay for a better chair.{/n}''',
      c('"Let me hear the times and cargo weights together."', "measure"),
      c('"What did he steal? He has not mentioned that part."', "theft"),
      c('"What happened to the missing passengers?"', "missing")),
    n("measure", "Nocticula", '''{n}Nocticula moves her hand. The account resumes at a later question. Orren says the first journey took an hour by his sandglass, though a day had passed at the quay. The second consumed most of a day aboard and less than an hour outside. He regarded both as advantages, depending on who expected him home.
The cargo weights were recorded before loading, not after delivery. The ship returned lighter than the declared cargo accounted for.{/n}
"There," {n}you say.{/n} "They are paying for something they do not call cargo."
"Or the weights were invented."
"Then we need a passenger who did not profit from inventing them."
"One of the missing three would be inconveniently persuasive."
{n}You ask her to repeat the times. This time she watches you rather than the speaker.{/n}
"I have had merchants explain to me that irregular time is merely another form of storage. The less successful ones generally leave out the problem of collecting a debt before the debtor has incurred it."
"Does this harbor belong to you?"
"Not yet."
{n}The answer is almost affectionate. She has allowed you to reach the question she most wanted asked, and enjoys how little reassurance it provides.{/n}''', c('"Find out what comes back lighter. Keep the two voyages separate."', "terms", flags=f("asked_weights"))),
    n("theft", "Nocticula", '''"An astute objection."
{n}The image changes. Orren now holds a small brass object which he tries to present as a navigational instrument. Under questioning he admits that he took it from the captain's cabin. It contains six hollow pins and a lens that shows the reflected room without its occupants.
He sold the object before approaching Nocticula's agent. He refuses to name the buyer without immunity from both theft and the consequences of selling stolen property.{/n}
"He is selling you the recovery of what he sold someone else."
"A common business model."
"You admire him."
"I admire a man who can count his enemies and still ask for a better chair. His judgment about which enemies to make is less impressive."
{n}She lets the image repeat its demand. Orren's voice has an ambitious little lift on the word immunity.{/n}
"The buyer will want the instrument more than the story. He may have sold the only thing that can get him safely through that door."
"Then I suggest he begin appreciating the value of my protection."
"Protection against your buyer or his?"
{n}Nocticula's mouth curves.{/n}
"You are not going to let this become an agreeable conversation, are you? Good. I was afraid the chair would provide all the entertainment."''', c('"Get the buyer\'s name. A missing instrument is something we can trace."', "terms", flags=f("asked_instrument"))),
    n("missing", "Nocticula", '''"The captain says they disembarked. Their families say they did not return. Both statements can be true."
{n}The recorded man stops being amusing when the interviewer supplies the names. He knows two. A woman who ran a repair yard, and a pilot who had taught him to recognize a false harbor light. Orren insists that neither sailed on his second voyage.
He remembers a scrap of blue cloth caught in the fifth lamp. He had thought it a charm against storms. Now he wants to know which of the missing passengers wore blue.{/n}
"Your witness is frightened."
"He was frightened when he arrived. He is becoming frightened about something useful."
"Is the difference important to you?"
"Very. Fear that produces only shouting is expensive to accommodate."
{n}She stops the image before it can ask another question.{/n}
"We will not learn their fate by encouraging him to supply a better tragedy. I can send someone to the repair yard. There will be records, tools, people who know what the woman took with her."
"And someone to the pilot's family."
"You may dictate the questions. You may not promise my money before we decide who has earned it."
{n}She draws the purse out of your reach and sets it behind the stopped witness.{/n}''', c('"Ask for descriptions and dates. Do not tell them we have found anyone."', "terms", flags=f("asked_missing"))),
    n("terms", "Nocticula", '''"My agent can continue. There is one condition you should know before you begin choosing subjects for her kindness. Orren asked for protection. I offered it if he surrendered every profit from the voyages."
"Did he?"
"He offered half. We are enjoying the negotiation."
{n}You look at the man in the wet chair. The image is silent now, its face caught between defiance and calculation.{/n}
"I want the route intact," {n}Nocticula says.{/n} "Someone has put my emblem on a very clever theft. I am willing to pay to discover how it works. I am not willing to be thanked for a rescue I have not undertaken."
{n}She steps between you and the reconstruction. Her hand rests against your chest, the tips of her nails just touching the cloth, until you look at her instead of at him.{/n}
"Tell me what you want from this. An adventure? A weapon? An opportunity to improve my morals?"
"Would you believe the last one?"
"I would believe you wanted it. I would advise you to bring better equipment."
{n}The dream holds her warmth as accurately as it holds the cold water. She knows you notice both.{/n}''',
      c('"I want the missing people found, even if that makes the route less valuable."', flags=f("witness_heard", "purpose_rescue")),
      c('"I want whoever stole your emblem working for us, or unable to work for anyone."', flags=f("witness_heard", "purpose_power")),
      c('"I want to know what you do when the answer is not the one you wanted."', flags=f("witness_heard", "purpose_curiosity"))),
], "invitation_accepted")

s("lamp_measure", "The measure of a lamp", [
    n("start", "Narrator", '''{n}Nocticula meets you in a room with a low ceiling and no furniture except an enormous balance. Six lamps hang from one side. The other holds a brass instrument, enlarged until you can see the fine scratches around its lens.
She has acquired a copy of the ship's loading book. Here it appears as floating columns, the numbers turning whenever you walk around them.{/n}
"The captain owns two sets of weights. A tolerably familiar fraud. Unfortunately, the discrepancy survives comparison with both."
{n}One column names the passengers. Another lists timber, salt, copper, and six sealed cases described as devotional supplies. The same six cases appear on three voyages, always under different owners. No passenger appears twice except Orren.{/n}
"We have not bought his instrument back," {n}she says.{/n} "This is a drawing made by the craftsman who repaired its hinge. He could describe everything except the contents of the pins. He had the sense not to open them."
"A rare quality in a craftsman?"
"In anyone asked to mend something valuable without being told what it does."
{n}Nocticula stands close behind you as you study the columns. Her presence is an agreeable distraction and, you suspect, an intentional one.{/n}
"If I were trying to make this easy," {n}she murmurs,{/n} "I would have asked somebody less interesting to read it."''',
      c('[Compare loading intervals, declared weights, and the repeated cases. Knowledge: World, DC 30.]', check=dict(Skill="SkillKnowledgeWorld", DC=30, Success="read", Failure="miss", CommanderOnly=True)),
      c('"Let us bait the captain with a shipment that is weighed honestly."', "bait"),
      c('"Offer him two profitable lies that cannot both be true."', "trick", requires=("trickster",))),
    n("read", "Nocticula", '''{n}You stop following the weights and compare the owners. Each repeated case changes hands after the ship returns, never before it leaves. The devotional goods are being sold retrospectively. Whatever enters the harbor can acquire a new owner while it is already inside.
You draw a line through the six names. Then you put the missing passengers beneath them.{/n}
"He does not transport the same cargo three times. He sells a claim to what has already arrived. The weights are an excuse for the payments."
{n}Nocticula looks at your arrangement, then at the lamps. Only now does she move away from your shoulder.{/n}
"That would explain why the fifth lamp changed without another passenger boarding. Someone purchased an old arrival."
"And why a stolen navigational instrument matters. It might identify what he is actually selling."
"Or allow the buyer to collect it."
{n}She turns the balance. Its beam cuts across the floating columns, separating the supposed cargo from the names.{/n}
"You have made this considerably less amusing."
"Because it may be worse than smuggling?"
"Because I should have seen it first."
{n}She kisses you without warning, brief and exact, then steps away before you can mistake it for a distraction from the answer.{/n}
"There. I can be generous about a defeat when it is useful."''', c('"We follow the ownership transfers. Keep the captain unaware."', flags=f("method_chosen", "ledger_read"))),
    n("miss", "Narrator", '''{n}The figures almost agree. You find a pattern in the salt shipments and spend long enough defending it that Nocticula stops teasing you. She produces a second page. It contains the same payments with no salt aboard.
For a moment the room is uncomfortably quiet.{/n}
"A plausible answer," {n}she says.{/n} "I have killed people for supplying worse ones with greater confidence."
"Shall I apologize for surviving?"
"Only if you insist on continuing the argument."
{n}You erase the connection you made. The floating columns separate again. Nocticula does not conceal the correction beneath a compliment.
The lost time has a consequence. Her agent has held Orren in protection long enough that the captain's men have begun looking for him. A quiet comparison of accounts will now be difficult. Nocticula can still send a deliberately conspicuous shipment and see what the captain offers to conceal.{/n}
"It costs me a merchant who can be trusted to act surprised," {n}she says.{/n} "They are rarer than merchants who can be trusted with money."
"Use one who dislikes the captain. Surprise will be easier when he is enjoying himself."
{n}That wins a small smile.{/n}
"Perhaps you have not entirely wasted my evening. Choose what he is to offer."''', c('"A shipment with an owner too prominent to disappear quietly."', "bait", flags=f("ledger_missed"))),
    n("bait", "Nocticula", '''"Prominent enough to be noticed. Not so prominent that he refuses the business."
{n}She chooses a broker named Meret, a middle-aged tiefling whose warehouses depend on the harbor trade. You have not met her. Nocticula describes her as honest about the occasions on which she intends to cheat.
The proposed cargo is copper stamped with Meret's own mark. Every ingot will have been weighed twice before loading. If the captain invents a discrepancy, Meret will demand to know whose scales he proposes to use.{/n}
"It warns him," {n}you say.{/n}
"Yes. You wanted an experiment rather than an elegant guess. The subject may notice he is being experimented upon."
"And Meret?"
"She owes me eleven thousand in salt and sulphur. She will carry the copper to have a third of it forgiven. If the captain makes her disappear, I lose a debtor and he loses a great deal more than copper, and Meret knows that arithmetic better than anyone. It is why she still sleeps at night."
{n}Nocticula holds out her hand. You give her the imaginary loading book. She closes it, and the room's columns vanish.{/n}
"The captain will tighten his operation. We lose surprise, gain a controlled shipment, and owe Meret something. I hope you enjoy accounting. It becomes intimate surprisingly quickly."''', c('[Authorize the conspicuous shipment within this undertaking.]', flags=f("method_chosen", "bait_sent"))),
    n("trick", "Nocticula", '''"Explain before you attempt to amuse me."
"He profits from being the only man who can satisfy a buyer. Give him two buyers. One wants a passage kept secret. The other will pay more if the same passage is publicly guaranteed by you."
"He could simply refuse the second."
"Unless the second has purchased the first buyer's debt. Then he must explain which obligation owns the voyage."
{n}Nocticula studies you. The smile comes slowly, with real interest behind it.{/n}
"You want him to choose a lie in front of someone who can collect on either answer."
"I want him to ask his supplier how to answer. We follow the question."
"No transformation of the universe? No demand that I admire a pun?"
"Will you pay more if I add one?"
"Less."
{n}She chooses two agents who have never openly worked together. Their offers will be carried through rival intermediaries. One is to complain about the price where the captain's clerk can hear him. The other will arrive carrying the disputed debt in a case too expensive for its contents.
Nocticula places the two offers on opposite sides of the balance.{/n}
"If he flees, he takes the route with him. If he answers, we learn who corrects his mistakes. I accept the risk. Do not become dull now that I have encouraged you."''', c('[Commit the contradictory offers and follow the captain\'s inquiry.]', flags=f("method_chosen", "double_offer"))),
], "witness_heard")

s("captains_reply", "The captain's reply", [
    n("start", "Narrator", '''{n}A ship's cabin waits on the other side of sleep. Nothing rocks. The bottles in their leather rack remain perfectly level, though the sound of waves comes through the floor.
Nocticula has arranged three objects on the captain's desk: a length of blue cloth, a copper coin cut in half, and a narrow knife. She lifts the cloth to show you a stitch in the shape of a hook. The knife has a wooden handle polished by ordinary use.{/n}
"Do not look so concerned. I have not murdered the captain with cutlery. He has a servant who keeps his accounts and dislikes the way he refers to her. My agents have made her an offer."
"A better employer?"
"A passage out, a payment, and the pleasure of seeing him discover how much of his business he did not understand. She asked for the pleasure first. I approved her priorities."
{n}The servant is named Dessa. Nocticula says she is a human woman the city swallowed a decade ago, who survived by making herself indispensable, and has now decided that indispensability is a poor substitute for a door she can open.
Her testimony comes as a written account, not another speaking image. Some phrases are crossed out. Nocticula has kept the corrections.{/n}
"She changed 'master' to 'captain' every time. It made the account slower to write. She insisted."
"You let her."
"I wanted it legible. Anger is useful; a trembling hand is less so."''',
      c('"Did the ownership transfers lead her to the supplier?"', "ledger", requires=f("ledger_read")),
      c('"What did he do with the conspicuous shipment?"', "bait", requires=f("bait_sent")),
      c('"Which buyer did he try to betray first?"', "double", requires=f("double_offer"))),
    n("ledger", "Nocticula", '''"Neither. They led us to the woman who collects the supplier's payment."
{n}Dessa copied the transfers before the captain knew they mattered. Each sale names a different owner, but the receipts carry the same small error: a seventh line where the harbor is supposed to have six berths. The person writing them expects room for something the ship never brings.
Nocticula taps the seventh line with a nail.{/n}
"Your reading bought us this. The captain still believes his accounts are merely dishonest. He does not know which dishonesty we have found."
"What is the collector's name?"
"Ilvara. No title. No explanation of whom she represents. Dessa says the captain always meets her on the quay, never aboard."
"Because she dislikes ships?"
"Because he would have an advantage aboard his own. She knows where to stand."
{n}Dessa has included a description of Ilvara's shoes: white leather, unmarked by the harbor mud. Nocticula approves of the detail. People recall beautiful faces unreliably, she says. They remember when someone can afford to walk through filth without looking down.
The supplier remains hidden, but a quiet meeting can still be watched. Your successful reading has preserved that opportunity.{/n}''', c('"Let her collect once more. We need the destination, not merely the collector."', "dessa", flags=f("collector_unwarned"))),
    n("bait", "Nocticula", '''"He refused it. Politely, at first. Meret demanded an explanation loudly enough to make politeness expensive."
{n}The captain then offered to accept the copper if its marks were removed. Meret declined to supply anonymous metal at the price of recognizable goods. Their argument drew the collector out of a nearby warehouse.
Ilvara ordered the captain to end the discussion. She offered Meret compensation from a purse whose coins had been cut cleanly in half. When Meret objected, Ilvara supplied an equal weight of whole silver instead.{/n}
"A mistake?" {n}you ask.{/n}
"A habit. She reached for the money she uses among her own people. Dessa noticed."
"Meret has lost the voyage."
"And earned the reduction I promised. You have cost me something definite. It is refreshing. Most people insist I should be grateful before they reveal the amount."
{n}Ilvara now knows that the captain has attracted attention. The next collection will be guarded. Nocticula's agents can still watch the warehouse, but Dessa must leave before her employer discovers who copied his book.
Nocticula folds the account. She seems less pleased with the warning than interested in what the half-coins mean.{/n}
"There is an exchange we have not understood. I would like to understand it before she decides to change currencies."''', c('"Get Dessa out before watching the next collection."', "dessa", flags=f("collector_warned"))),
    n("double", "Nocticula", '''"Both. I would have been disappointed by anything less."
{n}The captain accepted the private buyer's deposit, promised the public buyer a charter, then wrote to someone named Ilvara asking whether ownership of a passenger could be transferred before the passenger arrived. He disguised the question as a dispute about storage fees.
Dessa copied both his letter and Ilvara's answer. Nocticula allows you a moment to appreciate the result before supplying the price.{/n}
"The answer was delivered by a messenger who recognized one of my intermediaries. Ilvara suspects my interest. She does not know how much we learned."
"Enough to know the cargo can be a person."
"Enough to know that arrival matters more than distance. She refused the advance transfer. Whatever she sells must first have crossed the threshold."
{n}Nocticula brings the two forged offers together. Their wax seals touch, then melt into a single dark bead.{/n}
"You made a captain afraid of disappointing two buyers. He asked the one question he would never have answered for us. I enjoyed that."
"Even though she suspects you?"
"Especially because she must now wonder which of her answers I possess. Uncertainty can be a costly guest."
{n}She places the bead in your palm. It is only dream wax, but she closes your fingers around it as though she has given you a prize.{/n}''', c('"Keep her uncertain. Bring Dessa out while they are deciding whom to blame."', "dessa", flags=f("collector_warned", "transfer_rule_known"))),
    n("dessa", "Nocticula", '''"Dessa has one additional condition. Her sister owns a room above a dye shop. She wants the room's lease purchased before she leaves, so the captain cannot take it in payment for her disappearance."
"A reasonable fear."
"A shrewd last-minute addition. The room is worth more to him as a threat than it is to any tenant."
{n}Nocticula puts the knife beside the cloth. Dessa has asked to keep it. It was her mother's, and the captain told her a servant could not own anything used in his kitchen.
There is no great magical secret in the knife. Its importance is smaller and harder to bargain down.{/n}
"I can buy the lease. I can also tell the captain that harming the sister will result in an unpleasant personal visit. One costs money, the other makes my involvement unmistakable. Neither conceals Dessa's departure forever."
"Which do you prefer?"
"The threat. It has the advantage of being true."
{n}She watches you choose. Her amusement has sharpened into something more attentive. The question is no longer whether you can read a ledger. It is what sort of power you prefer when both methods would work.{/n}''',
      c('"Buy the lease quietly. She asked for a home he cannot take, not a new patron he fears."', "lease"),
      c('"Threaten him. Let him understand exactly whose attention he has earned."', "threat")),
    n("lease", "Nocticula", '''"Very well. The lease becomes the sister's property. Not mine, not yours. I will have the transfer checked before Dessa leaves."
{n}She calculates what the quiet purchase allows: another day before the captain connects his servant's departure to the collector's trouble.
Then she sets the knife beside the door.{/n}
"Dessa may keep this too. If she intends to begin a new life with a kitchen knife and an excellent memory, I would advise future employers to pay her on time."
"Will you?"
"If I employ her. She has not asked."
{n}Nocticula leans across the desk and kisses the corner of your mouth. The edge of the lease catches beneath her hand and tears.{/n}
"You make expensive distinctions. I may eventually acquire a taste for watching you defend them."
"Eventually?"
"Do not haggle over an adverb. It makes you look needy."''', c('[Keep the quiet purchase and Dessa\'s independence.]', flags=f("dessa_safe", "lease_bought"))),
    n("threat", "Nocticula", '''"At last, an answer which does not require a clerk."
{n}She composes the warning aloud. It is short. The captain may consider the sister's room beyond his reach. If he disagrees, he may present his reasoning to the Lady in Shadow in person, without weapons or the expectation of returning home. As a postscript she adds the name of the captain's mother, and the street in Shatterstone where the old woman keeps her songbirds.
Nocticula stops before the final sentence and looks at you.{/n}
"You understand what this buys. He will leave the sister alone because he believes she is mine. She will be mine, in the way a coin with my face on it is mine: nobody else spends it. If Dessa wanted to belong to nobody, you have chosen the wrong kindness for her."
"It keeps him away from her."
"It does. It also tells every captain on that quay whose property she is. I find I like that half better."
{n}She reads the warning back, lowering her voice for the sentence about an audience without weapons. Then she adds that the captain may bring his accountant.
She sends the knife with the warning, enclosed in a separate case for Dessa. The captain is not permitted to keep either the blade or the last word.{/n}''', c('[Make the protection public and accept the attention it draws.]', flags=f("dessa_safe", "threat_sent"))),
], "method_chosen")

s("her_own_face", "Her own face", [
    n("start", "Narrator", '''{n}This time there is no harbor. You find Nocticula in a chamber whose ceiling disappears into darkness. A single lamp illuminates a wide couch and a bowl of pale fruit. She sits with a book open on her knee, though she closes it before you can read the title.
The face she turns toward you is her own.{/n}
"You look as though you expected an invoice."
"You have been keeping accounts."
"So have you. I thought we should discover whether we can endure an evening without comparing them."
{n}She offers a piece of fruit between two fingers. If you take it, the flavor is cool and faintly bitter. She eats the next piece herself rather than watching for your reaction.{/n}
"You have used dreams to offer me things I wanted," {n}you say.{/n} "Does this room mean you know what I want tonight?"
"It means I know what I want tonight. You may supply the other half of the information."
{n}She moves the book from her knee, opening a place beside her.
She lays one hand beside the book. You glance from it to her face.{/n}
"You could make the invitation rather difficult to refuse. Your gift has not gone away."
"No," {n}she says.{/n} "It has not."
{n}She makes no movement. The lamp gutters once, and you become uncomfortably aware of how closely you were watching her fingers.{/n}
"Should I find that reassuring?"
"You should remember it. Particularly if you begin imagining that a pleasant evening has altered our older bargain."
"Then why ask what I want?"
"Because I want to hear the answer. I know what obedience sounds like. It has very poor conversational range."
{n}She takes the book up again, holding your place beside her open with its spine.{/n}
"Tonight I am asking. You may disappoint me. I would advise against being dull about it."
{n}You let the silence last a little longer. Her mouth curves, but she waits.{/n}''',
      c('"I wanted to see you without another face between us."', "face"),
      c('"I enjoy your inventions. I would also like to know which amuse you."', "invention"),
      c('"Tonight I would rather talk. You can keep the fruit."', "talk")),
    n("face", "Nocticula", '''"That is either a very good compliment or a remarkably provincial objection to variety."
"You may choose the interpretation you like."
"I usually do. It saves time."
{n}You sit beside her. At this distance her expression is less easily reduced to a smile. There is calculation in it, but also the small, unguarded adjustment of someone settling into company she chose.
She turns your hand palm upward and traces one line with a fingertip.{/n}
"You have been looking at my hands when I work. Most people look elsewhere."
"They move before the dream changes."
"A habit, not a necessity."
"Then I have learned a habit."
{n}Her finger stops. She looks up at you, and for a moment the answer she intended seems less interesting than the one she could give.{/n}
"Yes. You have."
{n}When she kisses you, she does not change her shape. The kiss lasts long enough for you to answer, then she draws back with a pleased, almost challenging glance.{/n}
"There are disadvantages to recognizing me. You will have fewer excuses when I disappoint you."
"I was not collecting excuses."
"Then perhaps you are better company than I thought."''', c('[Stay with the woman who chose this room.]', "night", flags=f("own_face_chosen"))),
    n("invention", "Nocticula", '''"At last, a question about craft."
{n}She lifts the empty bowl. Its pale interior becomes a summer sky. A cloud crosses it slowly enough that you can see rain falling over a distant hill.{/n}
"I dislike perfection. Not because it offends me, but because it makes people suspicious. A room with no dust persuades nobody that they have arrived somewhere private. One misplaced object does more work than a thousand accurate tiles."
"What did you misplace here?"
{n}She glances at the book, then realizes she has answered you. Her laugh is brief and genuine.{/n}
"Careless of me."
"What is it?"
"A history of a minor mortal dynasty. They spent two hundred years fighting over a ford and then a flood moved the river. The final chronicler blamed a rival family's manners."
"You find that amusing."
"I find their persistence impressive. I have known demons who abandoned a feud over much less."
{n}She lets you hold the bowl. The cloud follows your thumb, though the rain continues to fall on the hill.{/n}
"I could make it follow every gesture," {n}she says.{/n} "But then there would be nothing for you to watch except yourself."
{n}She leans against your shoulder. The room remains imperfect, and she seems content to leave it that way.{/n}''', c('[Let the cloud take its own course and turn toward her.]', "night", flags=f("craft_shared"))),
    n("talk", "Nocticula", '''"A devastating refusal. I shall have to eat two pieces."
{n}She does exactly that, then moves the bowl between you. She does not argue. She has eaten a great many refusals in her time, and she lets you watch her enjoy the taste of this one.
You ask why she kept the old chronicle. She tells you about its final historian, who tried to conceal a queen's disastrous affair by devoting seven chapters to drainage. Nocticula remembers the affair only vaguely. She can recite the drainage disputes with surprising precision.{/n}
"You think that is the more revealing part?"
"It tells me what the historian was afraid someone might compare. I have spent a great deal of my life reading around what people insist is important."
"And me?"
"You are less accommodating. You occasionally say the troublesome thing outright."
{n}She asks about a place you remember badly: not a battlefield, but a room you could draw only until someone asked where its second window stood. You describe it. She builds the window in the wrong wall, listens to your correction, and leaves one detail uncertain.
The conversation goes on. The lamp burns down. She lets you see her decide not to hurry you, and lets you understand that it is a decision.{/n}''', c('[Keep the evening as conversation.]', "morning", flags=f("quiet_evening"))),
    n("night", "Narrator", '''{n}Nocticula puts the bowl aside, and the book after it, and stops pretending the couch is for sitting. She takes your hand by the wrist and lays it at her throat, over the single fastening of the black gown, and holds it there until you open it. When you catch her other hand before it can alter the room, she laughs low in her throat and leaves the lamp exactly where it is, so that you can see what you have uncovered.
She has no patience for being undressed slowly. Your belt, your collar, the rest of it goes wherever she flicks it, and she looks at you in the lamplight the way she looks at a map of a city she has decided to take. Then she puts one hand flat on your chest and pushes, and you go down among the cushions, and she comes down after you, a knee on either side of your hips, her hair falling round both your faces like a drawn curtain.
"Look at me," she says. "My own face. Remember which one it was."
Her mouth closes on yours. She catches your wrists and presses them into the cushions, smiling when you pull against her hold. "My own face," she repeats, close enough for you to feel the words. The lamplight narrows to the bright edge of her hair, then vanishes.
Later she lies beside you, one hand resting loosely over yours. The book has fallen open on the floor. Neither of you reaches for it.{/n}
"That book," {n}she says,{/n} "ends with a flood. Two hundred years of ingenious murder, and the river decides the succession."
{n}You remark on her disappointment.{/n}
"I was becoming fond of the losing side. They had just hired an excellent poisoner."
{n}You laugh. Nocticula closes her eyes and allows herself a smile she does not bother to aim at you.{/n}''', c('[Stay through the unhurried quiet afterward.]', "morning", flags=f("private_night"))),
    n("morning", "Nocticula", '''"I have one question before you wake."
{n}She is sitting up now, the closed book between her hands. The room has not begun to dissolve, but you can feel morning waiting beyond it.{/n}
"Ilvara is using my flower to sell people. When I take her road, somebody will call it a rescue. Somebody will call it theft. I intend to keep the road."
{n}She closes the book under your hand and draws you back against her.{/n}
"Will you still come here when she starts screaming?"
{n}You keep your hand on hers. Her grip tightens.{/n}
"Good. I would hate to waste the lamp."
{n}The window brightens. You have time to notice that she has kept your hand on the book before the weight of it disappears. Your own pillow is colder than the cushion she made for you.{/n}''', c('[Wake and keep the evening in its own right.]', flags=f("evening_kept"))),
], "dessa_safe")

s("white_shoes", "White shoes on a black shore", [
    n("start", "Narrator", '''{n}Ilvara arrives in the dream as a portrait drawn from three reports. Nocticula marks the uncertain details with deliberate flaws: one sleeve changes color, the ring on her hand has no stone, and her face remains indistinct around the eyes.
The shoes are perfectly clear. White leather, thin soles, expensive stitching. They stand on a strip of black sand that never sticks to them.{/n}
"My agents agree on those," {n}Nocticula says.{/n} "I thought you would prefer an honest uncertainty to a convincing face."
{n}Ilvara has sent a message after noticing the pressure around the captain. She addresses Nocticula by a private title used in older contracts. She offers a demonstration of the harbor's value in exchange for a meeting under a temporary truce.
The message describes the harbor as a place where journeys can be held unfinished. A passenger's arrival may be delayed, divided, or sold. It says nothing about lamps.{/n}
"A mortal magician," {n}Nocticula says.{/n} "Older than her face suggests, younger than her confidence. I have found three previous names. Under one she sold routes through dreams. Under another she arranged escapes from besieged cities. Under the third she was executed."
"Successfully?"
"The record is enthusiastic but imprecise. I have learned to distrust that combination."
{n}She places the offered truce beside Ilvara's portrait. Its seal is another half-coin.{/n}''',
      c('"What did she overlook while we kept the collector unwarned?"', "unwarned", requires=f("collector_unwarned")),
      c('"She knows you are interested. What is she trying to hide now?"', "warned", requires=f("collector_warned"))),
    n("unwarned", "Nocticula", '''"Her messenger carried two letters. He delivered mine and took the second to a buyer near the upper market. He did not know he was followed."
{n}The buyer wants the harbor emptied before Nocticula can claim it. His name is unimportant to her; his payment is not. He offered Ilvara a place aboard a departing vessel and enough power to establish herself elsewhere.
Nocticula produces a copy of the second letter. It asks whether the remaining lamps can be extinguished without damaging the instrument.{/n}
"They are considering abandoning whatever is inside."
"Or whatever sustains it. We still need the distinction."
"Can your agents stop the buyer?"
"Yes. But stopping him tells Ilvara we read the letter. I would rather make the escape less attractive before she knows it is in danger."
{n}She suggests purchasing the vessel's next berth through a third party, delaying its departure by an apparently unrelated dispute. It will buy one meeting, no more.
She counts out the berth money and adds the agent's fee. The shipowner has demanded both before holding the vessel. She pushes the coins through the dream's image of the receipt; when her hand comes back, it is empty.{/n}''', c('"Delay the vessel. We use the meeting to learn what the lamps hold."', "meeting", flags=f("escape_delayed"))),
    n("warned", "Nocticula", '''"Her escape. She has become very interested in the departure times of ships she cannot ordinarily afford."
{n}Ilvara has placed two guards at the warehouse. Neither is impressive enough to keep Nocticula out. They are impressive enough to kill a witness while their employer runs.
Nocticula does not propose testing the difference.{/n}
"I could close the harbor quarter. She would know before my order reached the final street. She might destroy what I want merely to punish me for making the attempt."
"Then offer her a reason to stay."
"She has already named one. A private audience and the possibility of becoming useful."
{n}You look at the temporary truce. Nocticula watches you read its narrow promise: no attack by either party during the meeting, no claim beyond its duration, no protection for anyone not named.{/n}
"It excludes the people in the harbor."
"Deliberately. She wants to learn how much they matter to us."
"Will she learn?"
"That depends on whether you let her choose the question."
{n}Nocticula smiles. She has begun to enjoy Ilvara's nerve, which is not the same as forgiving her use of the Black Flower.{/n}''', c('"Meet her, but decide our demand before she starts pricing it."', "meeting", flags=f("escape_open"))),
    n("meeting", "Nocticula", '''"The truce is for a real meeting in my city. You will not be there in the flesh. I can take your questions and return with her answers."
"You invited me into the investigation."
"Yes. I did not offer to carry your sleeping body into a room with an ambitious extortionist. You are my adviser, not my bait. I do not leave my possessions lying where other people can put a price on them."
{n}She draws two chairs in the sand, then erases one. The remaining chair faces the sea. Beside it she lays Dessa's final copy of the accounts. There are six numbered berths, then a seventh line with no passenger assigned to it.{/n}
"There is also this. Our diligent clerk copied the reservations. Ilvara has left one place blank on every voyage. I should like to know whom she expects."
"You can advise me. You can also ask me to make a promise in your name. I suggest you decide how much of your name you wish her to possess."
"She knows I work with you?"
"She suspects you are interested. I have not told her whether you are a patron, a lover, or an inconvenient voice I enjoy hearing."
"Which would she fear?"
"A patron would compete with her. A lover might be distracted. An inconvenient voice would ask questions she has not prepared for."
{n}Nocticula touches the indistinct face of the portrait, making it turn toward the empty second chair.{/n}
"I prefer the third. It costs us no false declaration and leaves her uncertain how far you will follow an answer."''',
      c('"Require the release of one missing passenger as proof that she can do it."', "release"),
      c('"Require a demonstration with something she owns. No borrowed victim."', "property"),
      c('"Offer her a false buyer for the seventh berth. See whether she corrects you."', "seventh", requires=("trickster",))),
    n("release", "Nocticula", '''"A clear demand. She will hear that you value the passengers."
"She will also hear that I want proof, not a performance."
"Those are not mutually exclusive. I shall require a name we can verify and a person my agents can question afterward. If she sends a convincing duplicate, I will count that as an insult to both of us."
{n}She studies you for a moment before setting the terms aside.{/n}
"You realize she may choose the least valuable captive."
"Then we learn she ranks them."
{n}Nocticula's eyes narrow with pleasure.{/n}
"There. A humane demand with a useful second edge. Keep doing that and I may begin to suspect you of enjoying the work."
{n}The portrait folds into the message. Nocticula carries it toward the water, already rehearsing how little eagerness she intends to show.{/n}''', c('[Ask for a verifiable release.]', flags=f("meeting_planned", "demand_release"))),
    n("property", "Nocticula", '''"She owns her shoes. I have developed an unreasonable interest in watching them get wet."
"Something more difficult to replace."
"Her chief assistant, perhaps. No, do not look at me like that. You said something she owns; I am demonstrating why the wording matters."
{n}You settle on the instrument itself. Ilvara may send it through the harbor and bring it back while Nocticula's agent records the interval. No captive is to be spent to make the demonstration convincing; Nocticula means to own every one of them before this is finished, and she dislikes watching her inventory wasted before she has counted it.
Nocticula corrects your proposed wording twice. The first correction prevents Ilvara from substituting a second instrument. The second prevents the demonstration from being presented as a completed sale.{/n}
"I would have asked for her signet," {n}she says.{/n} "But you have chosen something she needs enough to be frightened of losing. I approve."
{n}Her fingertips brush your wrist as she takes the terms. Her nails catch the paper beside your fingers. She folds it with the instrument's demand facing outward.{/n}''', c('[Demand the instrument\'s passage and verified return.]', flags=f("meeting_planned", "demand_instrument"))),
    n("seventh", "Nocticula", '''"There are six lamps."
"There is a seventh line in the accounts. Offer to reserve it for a passenger who has not yet agreed to travel. If she refuses, ask what would make the reservation valid."
"And if she accepts?"
"We learn whether she sells empty promises. Supply no name and pay no deposit. The offer must remain a question."
{n}Nocticula considers the shape of the trap. A false buyer could be exposed; an unanswered commercial inquiry is harder to punish without admitting why it was dangerous.{/n}
"You want to make her teach me the boundary of her own power."
"She wants you to believe it has none. She may overcorrect."
"Or attempt to sell me a boundary she does not possess."
"Then ask for the instrument as security."
{n}Nocticula laughs softly.{/n}
"I am beginning to understand why your friends keep inviting you to councils. It cannot be the brevity of the meetings."
{n}She accepts the inquiry, with one change: the hypothetical passenger must be powerful enough that an empty promise would be dangerous to collect. She leaves the name unspecified, allowing Ilvara's own ambition to furnish it.{/n}''', c('[Send the unnamed reservation and demand that she define its limits.]', flags=f("meeting_planned", "demand_seventh"))),
], "evening_kept")

s("demonstration", "What the harbor keeps", [
    n("start", "Narrator", '''{n}Nocticula is angry when the dream begins. She has made no attempt to disguise it with a more agreeable setting. You stand in an empty room while she removes a white glove finger by finger. A narrow cut crosses its palm.
She sees you looking and holds up her uninjured hand.{/n}
"The glove. Not me. Ilvara wanted to demonstrate that arrival and possession need not occur at the same time. I allowed her to attempt it with something I could afford to lose."
"You let her take a glove from your hand?"
"I let her discover that removing it did not entitle her to keep it. That was the cut. She tried to sever the claim when I pulled it back."
{n}She drops the glove. It lands heavily enough to sound like a stone.{/n}
"Her instrument does not create a harbor. It opens a surviving piece of somebody else's crossing. She has been feeding it the unfinished journeys of passengers. Their intentions hold the place together. Their bodies remain inside until she sells the right to finish arriving."
"And the lamps?"
"Each marks a person whose journey she can still use. The flame is not a soul. Do not let the appearance tempt you into making a more convenient mistake."
{n}She turns toward you fully. Her anger has acquired a precise object.{/n}
"The flower on the cloth is not her attempt to imitate my authority. She is using scraps from an old shipment which once traveled under my protection. It is an actual remnant of my passage. She has made a door out of a permission I gave someone else."''',
      c('"Did she release the passenger we demanded?"', "release", requires=f("demand_release")),
      c('"What happened when her instrument crossed?"', "instrument", requires=f("demand_instrument")),
      c('"What did she say about the seventh berth?"', "seventh", requires=f("demand_seventh"))),
    n("release", "Nocticula", '''"A pilot named Halren. He is alive. My agent verified the scar his wife described and asked him about a voyage that was never entered in the captain's book."
{n}Halren remembered stepping off the ship into a dry harbor. He had been told he could rest while the cargo was counted. He sat beside a lamp and began repairing a strap on his boot. When Ilvara released him, the strap remained unfinished and his hands ached as though he had worked on it for days.
He could not say how long he had been there. He could name two other people: the woman from the repair yard, Vessa, and a young sailor called Tomar who had tried to walk through the harbor wall.{/n}
"The wall led him back to his own footprints," {n}Nocticula says.{/n} "Halren tried to follow. He reached the same place without ever finding Tomar."
"Can Halren go home?"
"He has gone to a room my agent controls. He wants to see his wife. She wants him examined before she comes near anything that escaped an impossible harbor. I consider her the more sensible member of the household."
{n}Nocticula has kept Ilvara's released lamp. It is an ordinary object now, blackened around an empty wick. The release was real and cost Ilvara something she had wanted to keep.{/n}''', c('"Use Halren\'s account. Do not send him back to demonstrate it again."', "price", flags=f("halren_returned"))),
    n("instrument", "Nocticula", '''"For a moment she could not bring it back."
{n}Ilvara set the instrument on a strip of sailcloth and spoke a destination. The brass vanished. Her hand stayed open above the empty cloth while the room grew very quiet.
Nocticula counted three breaths before asking whether the demonstration had ended. Ilvara answered too quickly. Then she took a half-coin from her purse and snapped it in two. The instrument returned with a thread of blue fabric trapped beneath its lens.{/n}
"She used a passenger's unfinished arrival as payment. I did not know that until afterward. Your condition prevented her from supplying a new victim; it did not stop her spending one she already held."
"Did it kill someone?"
"She says no. I would not accept her assurance as a complete account. The lamp corresponding to the blue thread grew dimmer."
{n}Nocticula spreads her fingers. The cut glove appears between them, followed by the half-coin.{/n}
"But she revealed the mechanism. The instrument cannot simply fetch itself. Something inside must be surrendered to finish the passage. She has made every journey depend upon another unfinished one."
"A business that consumes its inventory."
"A business that intends never to run out of passengers."
{n}Her voice is cold with professional contempt, made worse by the theft of her emblem.{/n}''', c('"Then the recovery plan must account for the people already inside."', "price", flags=f("instrument_rule_known"))),
    n("seventh", "Nocticula", '''"That there is no seventh berth. Then, when I looked disappointed, that there might be one for a patron of sufficient importance."
{n}Nocticula lets you enjoy the contradiction before explaining the correction. The seventh line is a claim on the harbor itself. Ilvara has been pretending to sell ownership shares in a place she does not fully control. A sufficiently powerful arrival might stabilize it, or destroy it, or become trapped as its permanent anchor.
Ilvara did not know which. She had prepared an expensive answer for all three possibilities.{/n}
"She thought I might volunteer."
"Did you let her think so?"
"For almost an entire minute. You would have admired my restraint."
{n}The offered reservation became a threat without your needing to invent a victim. Nocticula asked Ilvara to warrant that the passenger could leave. Ilvara refused, first politely, then with an impressive display of technical vocabulary.
The refusal established the limit you needed.{/n}
"She cannot guarantee departure once the harbor has a powerful enough claim on its visitor," {n}Nocticula says.{/n} "And she cannot sell that guarantee without becoming answerable for it herself."
"There is our price."
"There is our lever. I have not yet decided what we should make her lift."
{n}She hands you the imaginary cut glove as though awarding a share of the discovery.{/n}''', c('"Make her stand behind a departure with something she cannot abandon."', "price", flags=f("anchor_rule_known"))),
    n("price", "Nocticula", '''"Ilvara wants a recognized commission. She will surrender the instrument and the people presently held if I give her protection and a place among my useful servants."
"Will she?"
"She would like me to believe that she can. The demonstration has made me less certain."
{n}Nocticula picks up the glove again. The cut opens into a line of darkness. She closes her fist around it, and the line disappears.{/n}
"I can break the old protection woven into the cloth. That will close the door she has stolen. It may also leave the passengers wherever she has put them. I do not know otherwise, and I dislike not knowing a great deal more than you dislike hearing it."
"So you need her alive."
"For the moment. You need not sound so pleased about it."
{n}She opens her hand. The glove has vanished; a scorch marks the skin of her palm. It remains while she looks at it, then fades.{/n}
"She wore my protection while selling something she would not dare offer me honestly. I could put her on that quay and break every lamp in front of her."
"Including the passengers' lamps."
"Yes. You see why I have come to consult somebody who will insist on mentioning them."
{n}She steps close enough that your shoulders touch. You can smell scorched leather, though there is nothing left to burn.{/n}
"Give me something I want more."
"Her method. Her buyers. A door she can no longer sell."
"A beginning. You have my attention."''',
      c('"We need a living witness inside who can choose to finish the journey."', "witness"),
      c('"We need to discover what Ilvara cannot afford to lose."', "leverage")),
    n("witness", "Nocticula", '''"Someone who can describe the harbor without being entirely shaped by her instructions."
{n}She has an account from Vessa's repair yard: a list of fittings the woman took aboard, including a small brass bell used to test whether a mast's seams carried sound evenly. Nocticula has copied the yard's drawing, down to a dent beside the handle.
If Vessa still has it, she may be able to signal across the harbor's broken acoustics. If she does not, the account will at least tell your agent which passenger knows how to test a structure before trusting it.{/n}
"You will not reach her by shouting encouragement from your bed," {n}Nocticula says.{/n} "We need a way to pass a question through the real door."
"Ilvara offered a second demonstration."
"Then she can demonstrate that her passengers can answer. I will ask for the bell by description. If she produces one before she has had time to reach Vessa, we learn how much of the show is prepared."
{n}Nocticula opens her empty hand. The torn glove forms across her palm again, its cut precisely where you remember it. She examines the edge, then tucks it into her sleeve.{/n}''', c('[Prepare a question only the passenger can answer.]', flags=f("next_measure", "witness_plan"))),
    n("leverage", "Nocticula", '''"Her life, obviously. But obvious threats make people imagine obvious escapes."
{n}You ask about the third name under which Ilvara was executed. Nocticula supplies the record. She died owing a debt to a mortal patron who had purchased passage for himself and his companions. The debt survives in the hands of his daughter, now older than Ilvara appears.
The daughter kept the signed promise. Two survivors witnessed it; both have refused Ilvara's agents money to forget her name.{/n}
"Find the daughter," {n}you say.{/n} "Offer her a chance to ask where her father went."
"She may demand revenge."
"Then we learn what it would cost to buy her patience."
{n}Nocticula looks pleased in a way that makes the room seem smaller.{/n}
"You would bring an old creditor to a new bargain. I like it. I like it rather more because you have remembered that the creditor may want something inconvenient."
{n}She agrees to seek the woman. On the message to her agent she writes the original debt before Ilvara's current name, then underlines the older figure.{/n}''', c('[Locate the surviving creditor and hear her own demand.]', flags=f("next_measure", "creditor_plan"))),
], "meeting_planned")

s("voices_in_glass", "Voices in the glass", [
    n("start", "Narrator", '''{n}A long table stands on the quay. At one end rests Vessa's bell. At the other, a glass of water trembles whenever the bell moves. Nocticula has recreated the arrangement exactly as her agent described it, including a crack in the glass.
She tells you the real bell rang twice during Ilvara's second demonstration. The first sound reached the room. The second appeared only as a ripple in the water.{/n}
"Vessa understood the question. She tested the boundary instead of begging us to believe she was alive."
"What did she say?"
"Not much. Words came through in the wrong order. Names arrived more clearly than sentences. I have not allowed my agent to improve them into an explanation."
{n}The dream repeats the fragments. Vessa's voice is rough and impatient. Six lamps. A door without a wall. Tomar following a wake in dry sand. A woman waiting for someone who had already died outside.
Then a phrase which Nocticula repeats without alteration: the harbor keeps the part of the journey you cannot finish alone.{/n}
"There is a rule there," {n}she says.{/n} "It may be a rule of the original passage, or something Ilvara has made her captives believe. We need to distinguish those before we give it more power by obeying it."''',
      c('"We planned around Vessa. What did she make of our question?"', "witness", requires=f("witness_plan")),
      c('"Did the surviving creditor answer you?"', "creditor", requires=f("creditor_plan"))),
    n("witness", "Nocticula", '''"She asked whether the person who sent it knew anything about ships. I have decided to take that as a compliment to its practicality."
{n}Your question had asked which part of the harbor remained unchanged when Vessa walked away from it. She answered: the names painted beneath the lamps. She had scratched out her own. By the time she reached the door, it was there again.
Then she changed the spelling. The wrong letter remained until somebody called her by the right name.{/n}
"An error persisted until corrected by a witness," {n}Nocticula says.{/n} "That is more interesting than a wall which leads you back to your footprints."
"She can affect it."
"A little. Enough to annoy Ilvara, who ended the demonstration immediately after that answer."
{n}Nocticula places a finger against the cracked glass. Its reflection shows the letter Vessa had changed, although the air above it remains empty.{/n}
"We will need someone to carry an answer through. Someone who knows which name to say and who can come back without letting the harbor borrow the journey."
"Ilvara."
"Perhaps. I am increasingly interested in making her experience the convenience she has sold to others."''', c('"Make her explain why she can leave when her passengers cannot."', "choice", flags=f("name_rule_known"))),
    n("creditor", "Nocticula", '''"She answered in person. Her name is Sere. She is sixty-two, has outlived two husbands, and informed my agent that she will not be hurried by a woman who has had centuries to make inquiries."
{n}Sere brought a letter written by her father before he took Ilvara's passage. It promised that he would meet her at a harbor whose lamps she could see from their old home. The home has been demolished. The harbor was renamed. Sere says she waited until she understood waiting was becoming her entire life, then stopped.
She does not want her father returned as a stranger expecting a child who no longer exists.{/n}
"What does she want?"
"An account. If he died, she wants to know. If he did not, she wants him told what happened while he was absent. She will not hand us her grief to beat Ilvara with."
"Does that disappoint you?"
"Enormously. Grief is the cheapest weapon in any city, and she has locked hers in a drawer. I have had to pay her instead."
{n}Nocticula has paid Sere for copies of the letter and travel records. Sere insisted on naming the price herself. She will speak to Ilvara only after someone gives her a credible answer about the passengers now inside.
Sere has kept the original. Nocticula taps the purchased copy against her palm. "An expensive woman. I had hoped to enjoy her anger. Instead I have bought her handwriting."{/n}''', c('"Honor her terms. The letter may explain what the harbor believes is unfinished."', "choice", flags=f("sere_heard"))),
    n("choice", "Nocticula", '''"Ilvara carries a return token. One half of a coin stays with her; the other is held outside by a person who expects her back. She has never entered without arranging that expectation."
{n}The half-coin rises from the table and turns in the air. Its severed edge is irregular, too distinctive to confuse with another.{/n}
"Not a soul bond," {n}Nocticula says.{/n} "Not love. A specific appointment, witnessed and paid for. She made a practical precaution into a privilege she could deny her passengers."
"We can give them return tokens."
"If someone can carry the matched halves through. The harbor will recognize the old passengers as cargo until somebody disputes that claim from inside."
"And you cannot simply order it to change."
{n}She gives you a look of magnificent displeasure.{/n}
"I can order anything. The distinction is what happens afterward. If I break the passage, we may lose everyone in it. If I take Ilvara's place without understanding her claim, I may purchase a very elaborate prison."
{n}Nocticula lowers the coin onto the table between you.{/n}
"So. We force her to carry the tokens, with a guarantee she cannot discard. Or we send a volunteer under my protection and trust Ilvara to keep the doorway open while we work. You may imagine how much I enjoy the second proposition."''',
      c('"Use Ilvara. She made this trap, and she should take the risk of opening it."', "ilvara"),
      c('"Ask for a volunteer who understands the danger. Keep Ilvara where we can watch her."', "volunteer")),
    n("ilvara", "Nocticula", '''"I thought you might reach that conclusion eventually."
{n}She does not offer to disguise the coercion. Ilvara will enter because the alternative is losing the instrument and Nocticula's protection against the people she has cheated. She will carry the tokens because her own return half will remain outside until the passengers have been accounted for.
There are limits. She may sabotage the rescue to make herself necessary. She may choose a captive whose return creates another problem. She will certainly insist that her cooperation entitles her to more than survival.{/n}
"I will give her a written answer," {n}Nocticula says.{/n} "Cooperation buys a hearing. Nothing more."
"And if she succeeds?"
"Then we decide what to do with a useful criminal who has performed one useful act. It is a category with which I have extensive experience."
{n}She lifts the coin and presses it into your palm. The dream metal is cold, though her hand is warm around yours.{/n}
"I enjoy it when you choose a sharp tool without asking me to blunt its name. Remember that when you dislike what I do with one."''', c('[Make Ilvara carry the return tokens.]', flags=f("crossing_planned", "ilvara_sent"))),
    n("volunteer", "Nocticula", '''"You are volunteering someone you have not met. That is admirably efficient of you."
"I said ask. If nobody agrees, we use another plan."
{n}She waits long enough to make certain you mean the distinction. Then she names Teren, a tiefling pilot whose work has taken him through unstable passages before. He has no special immunity to this harbor. What he has is a reputation for returning with his passengers and for refusing jobs he considers stupid.
Nocticula will buy him the way she buys anything she means to keep using: payment, a matched return token held by a witness of his choosing, and every account she has, because a pilot who has read the charts drowns less expensively than one who has not.{/n}
"He may ask me why I do not go myself."
"What will you tell him?"
"That the harbor would gain far more by holding me than by holding him. He will find that insulting. It will still be true."
{n}She studies the space where the second chair stood in the earlier dream.{/n}
"You will receive his answer before I send him. I dislike waste, and a resentful pilot is particularly wasteful. Do not begin praising me for asking. You insisted on a condition; I have accepted it."
{n}Her gaze softens just enough to make the last sentence sound less like a reprimand.{/n}''', c('[Let Teren examine the risk and choose.]', flags=f("crossing_planned", "volunteer_requested"))),
], "next_measure")

s("cost_of_return", "The price of coming back", [
    n("start", "Narrator", '''{n}You arrive in a dream of a narrow bridge. On one side is the dry harbor; on the other, a kitchen with a kettle just beginning to boil. Nocticula stands between them, holding the two halves of a coin apart.
She glances toward the kitchen, faintly offended by how ordinary it is.{/n}
"I had a pilot named Teren examine the return arrangements. He has crossed unstable passages before. He showed my agent this kitchen, which belongs to his sister. Whenever he takes a dangerous commission, he tells her when to expect him for supper."
"That is his precaution?"
"One of them. He says an appointment he wants to keep is harder for a passage to misunderstand. No ceremony, no invocation. He insists the soup matters."
"Can wanting be measured?"
"Ilvara has built a business on pretending it can. I would rather test the claim with someone who notices when he is being cheated."
{n}The kettle whistles. Nocticula silences it without removing it from the flame. You reach past her and move it anyway. She watches the gesture with an expression you cannot immediately read.{/n}
"It was only a sound," {n}she says.{/n}
"It had a reason."
{n}She looks from the kettle to the empty kitchen chair. Then she lets the room become still on its own.{/n}''',
      c('"What terms did Ilvara accept?"', "ilvara", requires=f("ilvara_sent")),
      c('"Did Teren agree?"', "teren", requires=f("volunteer_requested"))),
    n("ilvara", "Nocticula", '''"Fewer than she asked for. More than I enjoyed granting."
{n}Ilvara will carry six matched tokens and return with a count of every person she can reach. Her own return half remains with Nocticula's agent. She demanded that no one destroy the instrument while she was inside. Nocticula agreed, since destroying it would defeat the purpose of sending her.
Then Ilvara asked to retain one lamp as payment.
Nocticula refused before the agent had finished reading the request.{/n}
"I have not begun charging you for people," {n}she says.{/n} "I see no reason to let her begin charging me."
"You want the whole harbor."
"Of course. That does not make her offer less offensive."
{n}Ilvara has written the passengers' names in a hand that deteriorates as the list continues. The final name is incomplete. She says its owner entered before she took possession of the instrument and may no longer know how to answer.
Nocticula believes this much, because it is an admission which reduces the value of the thing Ilvara hopes to sell.{/n}
"We may be buying an older crime along with hers," {n}she says.{/n} "Do not let her use that to persuade you that the newer one is less real."''', c('"Keep the older passenger in the count. Unknown is not absent."', "risk")),
    n("teren", "Nocticula", '''"He called the plan stupid, then explained how he would improve it. I take that as a professional form of affection."
{n}Teren refused a sword. He asked for a length of knotted cord, the return tokens, and written descriptions of the missing passengers. He will not carry Nocticula's emblem. It would make the harbor more interested in him and might persuade the captives that they had merely acquired a new owner.
Nocticula accepted this refusal with rather less grace than she now gives it in the telling.{/n}
"He also requested a witness who does not work for me. His sister. She will hold his coin and receive the payment if he does not return."
"You agreed?"
"Yes. I would like the man concentrating on the harbor rather than on whether I intend to cheat his family."
{n}Teren's final condition is that he may turn back after inspecting the first lamp. He will not be required to finish the rescue merely to justify the cost of beginning it.
Nocticula lays out his route. He has supplied an exact signal for retreat: three pulls on the cord, followed by a pause long enough to hear the response.{/n}
"He has agreed," {n}she says.{/n} "He has also made certain we cannot honestly say he agreed to everything. I suspect you will like him."''', c('"Keep the retreat signal. If he uses it, he comes back."', "risk")),
    n("risk", "Nocticula", '''"Before we proceed, there is the matter of the door."
{n}She brings the halves of the coin together. They do not join. A narrow line of darkness remains between them.{/n}
"The stolen cloth contains the remnant of my protection. I can lend the crossing enough of that old claim to keep it open while the tokens are carried through. I cannot do that without revealing the shape of the permission. Ilvara will learn something about how my agents travel."
"A real price."
"Yes. Try not to sound delighted."
{n}The alternative is to use the instrument without reinforcement. It may hold long enough; it may not. If it fails, the person inside must choose between abandoning the captives and losing their own way back.
Nocticula has not yet chosen. She wants the harbor, wants to punish the theft, and dislikes giving an enemy knowledge she may later have to kill to contain.{/n}
"You asked for a plan worth the delay," {n}you remind her.{/n}
"And you have helped make one. Now we decide whether the plan is worth its cost."
{n}She touches your cheek, surprisingly gently, while considering an act that has nothing gentle about it.{/n}
"Ilvara gets one look at my road. You get your passengers. I shall remember who asked."''',
      c('"Reinforce it. We accepted responsibility for sending someone through."', "open"),
      c('"Keep the secret. A rescue that gives her another weapon may cost more lives later."', "closed"),
      c('"Reveal a limited permission that expires when the last token returns."', "limited", requires=("trickster",))),
    n("open", "Nocticula", '''{n}She gives you a long, cool look, then turns back toward the harbor.{/n}
"You have an expensive understanding of responsibility."
"You knew that when you asked."
"I wanted to hear whether you still possessed it when I supplied the amount."
{n}She will reinforce the old claim. Ilvara will see how it is done. The knowledge cannot be removed afterward by declaring the rescue a success.
Nocticula orders her agent to record everyone present at the demonstration, including the guards and the woman who brings the water. Nobody is arrested for watching. Every name goes into a book she keeps for people who have seen more than they should, and one day, when it suits her, each of them will be asked what they remember.{/n}
"I will need to change the permissions on three other routes," {n}she says.{/n} "People I employ will curse my name while they learn the new forms. You may take some private satisfaction in having made their work more difficult."
"I would rather take satisfaction in the passengers coming out."
"Then let us arrange for you to have something to enjoy."
{n}She kisses you once before releasing the dream, her impatience now directed toward the work instead of your answer.{/n}''', c('[Accept the disclosed secret and the stronger crossing.]', flags=f("crossing_ready", "door_reinforced"))),
    n("closed", "Nocticula", '''"That is the answer I expected from a ruler. I was less certain whether you would give it while imagining the person inside."
{n}The crossing will proceed with a shorter limit. Her agent will pull the return line at the first sign that the harbor is borrowing its visitor's destination.
The passengers may have to come out in more than one attempt. Some may be left beyond reach when the instrument exhausts itself.{/n}
"Tell whoever goes in," {n}you say.{/n}
"Already part of the instructions. I have no use for a heroic surprise halfway through an extraction."
{n}She sets the halves of the coin on opposite sides of the bridge. The darkness between them remains.
She draws the return line between them, stopping short of the far coin. Her nail leaves a white score in the stone.{/n}
"When we hear the account," {n}she says,{/n} "do not ask me to tell it more kindly because you were prudent. I dislike prudence that cannot bear to recognize its own casualties."''', c('[Keep the route secret and require an early withdrawal if it fails.]', flags=f("crossing_ready", "door_unreinforced"))),
    n("limited", "Nocticula", '''"An expiring permission is still a permission she can study."
"Give it a condition she cannot reproduce. The matched tokens are numbered. Let the opening depend on the numbers still owed a return. When none remain, it ends."
"You are assuming we can identify every token the harbor accepts."
"Then count them together before entry. Leave no blank place she can fill later."
{n}Nocticula examines the proposal. It requires a new pattern drawn around the old cloth, two witnesses keeping the count, and a separate return line for the carrier. Ilvara can still observe the pattern. What she cannot keep is the exact unfinished obligation that powers this use of it.
The arrangement will be weaker than lending Nocticula's full protection, stronger than trusting the instrument alone.{/n}
"It also prevents me from keeping the door open after the last passenger leaves," {n}she says.{/n}
"You wanted the harbor. You may have to choose what remains of it."
{n}Her smile is slow and dangerous.{/n}
"There you are. I wondered when your clever solution would begin charging me rent."
{n}She sends for her agent's notes and begins drawing the pattern around the six names. Twice she stops to ask you to repeat the proposed limit. The second time, she catches an ambiguity and makes you choose exactly what the last token must finish.{/n}''', c('[Prepare the counted, limited reinforcement.]', flags=f("crossing_ready", "door_limited"))),
], "crossing_planned")

s("return_count", "The count at the door", [
    n("start", "Narrator", '''{n}For several nights the harbor has been an image supplied for your consideration. Tonight it is an account of something that has happened without you.
Nocticula tells you this before she gives the dream its shape. Her agents have completed the crossing. She will show you the sequence as they recorded it. Nothing you say to an image can go back and alter a decision already made at the door.{/n}
"You could simply tell me whether they came back."
"They came back. Now you should know how."
{n}The relief does not entirely survive her tone.
The room forms around you: bare boards, a trough of seawater, the strip of sailcloth fixed between two iron uprights. Ilvara's instrument rests above it. The half-coins have been laid in a row, each beside a name and a description. Nocticula's agent, a sharp-faced woman called Rhez, checks the names aloud.
The doorway opens without a flash. Beyond it, dry sand shifts as if something has just walked out of sight. You hear Vessa's bell before any figure appears.{/n}
"The sound reached us before the movement," {n}Nocticula says.{/n} "Rhez used it to keep the count when the doorway stopped showing the same instant on both sides. She is asking for a considerable increase in her fee. I am inclined to grant it."''',
      c('"Show me what Ilvara did."', "ilvara", requires=f("ilvara_sent")),
      c('"Show me Teren\'s crossing."', "teren", requires=f("volunteer_requested"))),
    n("ilvara", "Narrator", '''{n}Ilvara enters reluctantly and remains near the threshold long enough to be told twice that the tokens will not carry themselves. Her white shoes acquire a thin line of black sand.
At the first lamp she speaks a name, breaks a half-coin against its mate, and steps aside. A woman appears where the flame had been. Vessa is holding the bell so tightly that her knuckles have whitened.
Ilvara tells her to walk through the doorway. Vessa refuses until she sees the return token held outside. Rhez raises it. Only then does the woman move.
At the second lamp, Ilvara tries to conceal one of the brass pins in her sleeve.{/n}
"She intended to keep a claim on the crossing," {n}Nocticula says.{/n} "Rhez saw the sleeve change shape. Your prisoner was useful, not converted."
{n}Ilvara protests that removing the pin is part of the release. Rhez asks which name belongs to it. Ilvara cannot answer without looking back at the lamp she has already emptied.
The stolen pin goes into the trough outside. Ilvara's own return half remains where she can see it and cannot reach it.
She continues.
At the next lamp her hands shake badly enough that she drops the token. She crouches to retrieve it, keeping her face turned toward her own return half. Rhez lifts it higher.{/n}''', c('"And when the crossing began to strain?"', "strain", flags=f("ilvara_pin_taken"))),
    n("teren", "Narrator", '''{n}Teren enters carrying the knotted cord and no weapon. He kneels beside the first lamp before speaking. His sister's return token is visible in the room outside, held by Rhez on her behalf while the sister waits beyond the door.
Vessa appears when he matches her coin. She does not trust him. He tells her what he knows about the bell, then lets her inspect the token. When she decides to leave, he moves out of her way rather than taking her arm.
At the second lamp, the cord pulls itself tight.
Teren gives the retreat signal: three pulls, then a pause. Rhez answers. He comes back far enough to put one foot on the boards outside and reports that the harbor is trying to supply a destination he has not named.{/n}
"He used the right you gave him," {n}Nocticula says.{/n} "Ilvara called it cowardice. Rhez told her she was welcome to replace him."
{n}Teren examines the remaining names, adjusts the order of the tokens, and chooses to go back. This time he asks each passenger to describe where they mean to arrive before he breaks the coin. The harbor must accommodate an answer it did not dictate.
He is not fearless. His hand shakes when the doorway turns briefly into a wall. He waits for Rhez's signal instead of pretending he can see through it.
The practical caution is what keeps the count from becoming a list of guesses.{/n}''', c('"And when the crossing began to strain?"', "strain", flags=f("teren_returned_once"))),
    n("strain", "Nocticula", '''"The final lamp had two names. One old, one recently written over it. Ilvara had sold the same unfinished arrival twice."
{n}The older passenger is a man named Ren. He speaks a daughter's name as though she is still young enough to wait at a window for him. The newer passenger, Tomar, cannot remember agreeing to carry anyone else's journey. He only knows that every attempt to leave has brought him to the old man's lamp.
For a moment both figures occupy the same narrow space. Ren reaches for the lamp; his hand passes behind Tomar's shoulder. Tomar tries to move aside and finds himself facing the same flame again.
Vessa rings her bell from outside. Ren turns toward the sound. Tomar follows, and the instrument bends under a pressure its brass was never meant to bear.{/n}
"This is where our precaution mattered," {n}Nocticula says.{/n} "Ilvara had not told us there were two claims. Whether she knew how they would behave is a question I intend to ask at length."
{n}She stops the account with the two men standing in the doorway. Her face remains controlled, but she has drawn close enough that your hands nearly meet.{/n}''',
      c('"Your protection held the door."', "reinforced", requires=f("door_reinforced")),
      c('"We kept the secret and used the narrower opening."', "unreinforced", requires=f("door_unreinforced")),
      c('"The counted permission had to recognize both claims."', "limited", requires=f("door_limited"))),
    n("reinforced", "Nocticula", '''"It held. Ilvara saw precisely which part of the old protection I used. I watched her stop looking at the passengers."
{n}Rhez calls both names. The men stumble onto the boards separately. Tomar falls hard enough to break his nose; Ren reaches for a railing which is not there. Vessa catches his coat and swears at him until he stops trying to return for a bag left beside the lamp.
The instrument survives. So does a readable impression of the route. Rhez covers it before Ilvara can see which parts remained intact.{/n}
"Every passenger we could identify came through alive," {n}Nocticula says.{/n} "There may have been others before Ilvara began keeping names. We found no remaining occupied lamp. I will not turn that into certainty about every earlier journey."
"And the secret?"
"Learned. I have changed two permissions already. The third cannot be altered until a ship returns. For several days I will possess an inconvenience you helped purchase."
{n}She takes your hand. There is no reproach in the gesture, but no invitation to forget the price either.{/n}
"You wanted the stronger door. It was strong enough. That is an answer worth having."''', c('[Keep the successful return and the exposed route secret in the same account.]', flags=f("crossing_finished", "chart_intact"))),
    n("unreinforced", "Narrator", '''{n}The doorway begins to close between the two men. Vessa puts the bell through it sideways, jamming the gap. Brass flattens. Her hand remains around the handle when the metal grows hot.
Rhez pulls Tomar clear. Ren follows the sound of his own name, spoken by a stranger who refuses to stop repeating it. The instrument breaks before the last heel reaches the boards.
Vessa does not release the bell until Rhez tells her three times that both men are out.{/n}
"Her hand is injured," {n}Nocticula says.{/n} "The healer expects her to keep the fingers. He will not promise their old strength. She has asked whether the payment includes the months in which she cannot work."
"Does it?"
"It will. A woman who jams her own hand into a closing door to save my inventory is an asset, and I do not let assets starve. The earlier decision still cost exactly what it cost."
{n}The harbor's chart is lost with the broken instrument. Ilvara's account and the passengers remain, but the route cannot be claimed in its present form.
Nocticula stops the image as Rhez wraps a clean cloth around Vessa's hand. A thin wisp rises from the bell.{/n}
"Vessa wants the crushed bell back," {n}Nocticula adds.{/n} "I told Rhez to give it to her. I have no use for a trophy she earned with her hand."''', c('[Remember Vessa\'s injury and the route that was lost.]', flags=f("crossing_finished", "vessa_injured", "chart_lost"))),
    n("limited", "Nocticula", '''"Rhez refused to count two people as one merely because the lamp did. That gave the pattern its answer."
{n}The two names are spoken separately. The final token fractures into three pieces, one for each passenger and one which remains inside. The men reach the boards as the limited permission exhausts itself.
The door closes. The sailcloth falls apart along the old embroidery. There is no longer an opening for Nocticula to claim.
The instrument survives, but its lens shows only the room it occupies.{/n}
"We kept the promise small enough that the harbor could not demand more," {n}she says.{/n} "We also kept it too small for me to retain the passage afterward."
"You knew that was the limit."
"Knowing a price does not oblige me to enjoy paying it."
{n}She turns the now-ordinary lens between her fingers. For a moment you think she may break it out of irritation. Instead she sets it down carefully.{/n}
"It was good work. The kind that makes an opponent realize the victory was never offered on the terms she thought she accepted. I recognize the experience."
{n}Her glance makes certain you know she includes herself among the opponents.
She turns the lens through a full circle. It shows the quay behind you, then the wall, then your face. When she angles it toward the vanished entrance, the glass reflects only her own hand.{/n}''', c('[Keep the successful limited intervention and the closed harbor.]', flags=f("crossing_finished", "chart_limited"))),
], "crossing_ready")

s("after_the_lamps", "After the lamps go out", [
    n("start", "Narrator", '''{n}Nocticula brings no image of the harbor to the next dream. She brings a list of requests.
Tomar wants his wages for the voyage. Vessa wants the bell and an explanation of what happened to the fittings she carried. Ren wants to know why everyone insists his daughter is an old woman. Orren wants immunity again, apparently encouraged by the survival of people who might testify against him.
Nocticula reads the last request twice, enjoying it more the second time.{/n}
"It is almost admirable. He has mistaken the absence of immediate execution for an invitation to improve his terms."
"Will you execute him?"
"For stealing a navigational instrument from a slaver? I should have to reorganize half my city if I began punishing theft according to its victim's complaint. He will surrender the profit he concealed. Then he may attempt to become somebody else's difficulty."
{n}She sits on the edge of a low fountain. The water reflects a sky which the room does not possess.{/n}
"You wanted people returned. Here they are, making claims on the world. It would be easier if gratitude made them obedient."
"Would you prefer them obedient?"
"Often. You may notice I do not always receive my preference."''',
      c('"How is Vessa\'s hand?"', "injury", requires=f("vessa_injured")),
      c('"What does Vessa want to do next?"', "yard", forbids=f("vessa_injured"))),
    n("injury", "Nocticula", '''"Better than the healer feared. Worse than she would like. She can hold a cup. She cannot yet hold a hammer."
{n}Nocticula has paid for treatment and an assistant at the repair yard. Vessa chose the assistant. She rejected the first person offered because he kept telling her how fortunate she was.
The second asked where she wanted the tools. He remains employed.{/n}
"She sent a message for you," {n}Nocticula says.{/n} "Rhez told her someone outside the city had helped choose the plan. Vessa says that if you ever commission a ship, you should pay the carpenter before praising the voyage."
"That seems fair."
"It seems pointed. Fairness was not among the qualities she mentioned."
{n}A second account lies beneath the healer's bill. It charges for a hammer with a wider handle. Nocticula has marked it for payment.
You ask whether the message displeased her.{/n}
"A little. I have paid for that woman's survival, her treatment, and now the tools with which she intends to overcharge my captains. I expect something magnificent from her first ship."
{n}She lets the water run over her fingers, then flicks the drops away.{/n}''', c('"Keep her account with ours. Do not let the successful return erase it."', "ren")),
    n("yard", "Nocticula", '''"Open her yard. Charge higher prices to captains she distrusts. Replace the fittings Ilvara lost. In that order."
{n}Vessa has refused an invitation to tell her story at a merchant's gathering. She suspects the audience would remember the miraculous rescue and forget to pay their invoices. Nocticula seems to consider this a sound assessment of merchants.
She has accepted payment for a technical account of the harbor. Her drawings show the places where sound moved differently from light, where footsteps repeated, and where the lamps' names could be changed. She has written a warning across the first sheet: tested once, under threat of death, do not call this a reliable method.{/n}
"You bought the account?"
"Yes. She knew its value. I would have been disappointed if she had given it away."
"And what will you do with it?"
"Read it. Then decide whether anybody else should be allowed to."
{n}Nocticula folds the drawings inward, hiding the measurements before you can finish reading them. Her thumb rests on Vessa's price at the bottom of the page.{/n}''', c('"What happened when Ren learned how long he had been gone?"', "ren")),
    n("ren", "Nocticula", '''"He accused Rhez of lying. Then asked her to repeat the date. Then became very quiet."
{n}Ren is Sere's father. Nocticula's agents found enough records to verify it. She did not trouble the daughter for a childhood password; a woman who has buried two husbands does not open like a chest, and Nocticula does not waste a lever she may need later.
Sere agreed to receive a letter before deciding whether to meet him. Ren wrote three. He destroyed the first because it addressed her as a child. The second contained so many explanations that he could not find a greeting. The third asked what name she preferred to be called now.{/n}
"She answered that one," {n}Nocticula says.{/n}
"Will they meet?"
"She has proposed a place. He has agreed. That is as far as the account goes."
{n}The fountain changes. Its reflection briefly shows a harbor window, then a demolished wall, then only the room again. Nocticula has forgotten to close the image.{/n}
"I could have given him the dream of the daughter he remembered," {n}she says.{/n} "It would have been considerably less painful."
"For whom?"
{n}She looks at you and does not answer quickly.{/n}
"An irritating question. You have acquired a talent for them."''',
      c('"You let them have the difficult answer. That matters to me."', "matter"),
      c('"A comforting illusion would have been another way to keep him."', "keep")),
    n("matter", "Nocticula", '''"Be careful. You are approaching gratitude on someone else's behalf."
"I said it matters to me."
{n}She considers the correction, then inclines her head a fraction.{/n}
"Accepted."
{n}You sit beside her. The fountain is narrow enough that your knees touch. She does not move away, but she does not let the closeness become evidence in the argument either.{/n}
"I have done worse things than Ilvara," {n}she says.{/n} "Do not build an understanding of me out of one rescue that served my interests."
"I am trying to understand this choice."
"Then understand that it pleased me to deny her the final explanation. She wanted to be the only person who could tell her passengers what had happened. Now they have one another, and she has lost something she valued."
{n}She catches a floating scrap of Ilvara's advertisement from the fountain. The ink runs between her fingers. The list of promised destinations comes apart last.
When she wipes her hand on your sleeve, she is smiling.{/n}
"You could have made the water vanish."
"I could have. You were sitting so conveniently near."''', c('[Stay beside her while the last of the ink dissolves.]', "ilvara_next", flags=f("motive_heard"))),
    n("keep", "Nocticula", '''"Yes. It would."
{n}She turns toward you, her expression suddenly sharper.{/n}
"You say that as though you have discovered the secret of my entire existence. I know what an illusion can keep. I also know what people willingly return to. You have done both: accepted what I offered, and asked me to change it."
"And you have sometimes agreed."
"Sometimes. Do not become sentimental about the frequency."
{n}For a moment the conversation stands close to a quarrel. Then she looks down at your hand resting on the fountain's edge and lays hers beside it, without closing the space.{/n}
"I let him write because I wanted to know whether he could bear an answer from someone who no longer needed the man he remembered being. It is not a question I often hear asked honestly."
"Is that why you told me?"
"Perhaps. Perhaps I wanted to see whether you could avoid making the story entirely about yourself."
{n}Her glance is a challenge, and her hand stays where it is, the nails resting lightly on your knuckles like a promise of what they could do.{/n}''', c('[Take her hand without claiming the last word.]', "ilvara_next", flags=f("illusion_challenged"))),
    n("ilvara_next", "Nocticula", '''"We still have Ilvara."
{n}The name returns the evening to its unfinished business. Nocticula has not promised the magician freedom. She has promised a hearing after the passengers were accounted for.
Ilvara has requested your presence by name. She believes you are the source of the limits Nocticula placed upon the rescue, and hopes to turn those limits into protection for herself.{/n}
"I will hear her before I decide what becomes of her," {n}Nocticula says.{/n} "You can hear the account here afterward and tell me what you think. If you want to propose a condition before the hearing, now is the time."
{n}You point out that she has already decided something.{/n}
"That she will not leave with my old permission intact. Beyond that, I am prepared to be persuaded. Not cheaply."
{n}She rises from the fountain and offers you her hand. Her other hand keeps Ilvara's petition folded against her hip.{/n}
"I hope you have enjoyed learning what happens after a successful rescue. People become remarkably demanding when they are allowed to continue living."''', c('"Hear her. Then we decide what she can still be trusted to do."', flags=f("aftermath_heard"))),
], "crossing_finished")

s("another_place", "A place not promised", [
    n("start", "Narrator", '''{n}Nocticula catches you looking for the harbor before the dream has finished taking shape.
She closes the door behind you. Music comes from the far side, low strings and a voice singing in a language you cannot quite place. There is room to dance between the dressing table and the window. No desk appears.
She holds out her hand.{/n}
"One dance."
"You have no work for me?"
"I have an inexhaustible supply. At present I would like you to stop looking for it."
{n}A folded blue note lies beside her comb. Your eyes pass over it, and she takes it up before you can read the exposed line.{/n}
"You were about to ask."
"You put it where I could see it."
"I live here. Occasionally an object is present for reasons other than instructing you."
{n}She puts the note inside a shallow drawer. The music grows clearer, though the door remains shut.{/n}''',
      c('[Take her hand and leave the note where she put it.]', "dance"),
      c('"I would rather hear what happened. I will not be very good company while I wonder."', "refused_dance")),
    n("dance", "Nocticula", '''"There. A decision made without consulting a witness."
{n}She draws you into the narrow space. At first she leads, turning before the music seems ready for it. You follow once, then hold your place at the next turn. Her hand presses harder against yours.{/n}
"You are anticipating me."
"You keep changing the measure."
"The singer is quite certain of it."
{n}You listen. The phrase repeats. This time you turn on its last note and leave her a choice between following and stopping. She follows, her skirt brushing your knee, and laughs close to your ear.{/n}
"I could change the song."
"Then I would know you needed to."
{n}For several steps she gives you nothing but the weight of her hand. Then she turns you toward the window, leaving very little room to recover the next step. You catch yourself on its sill. Her palm settles beside yours.{/n}
"You see," {n}she says,{/n} "I do not need to."
{n}You could argue about whether the window had been so close before. Instead you kiss her. She lets you finish before moving away from the sill.
The song ends while you are still holding her hand. She draws her fingers slowly free, opens the drawer, and takes out the note.{/n}
"Now you may ask. I advise against beginning with an accusation about the architecture."''', c('[Follow her back to the dressing table.]', "note")),
    n("refused_dance", "Nocticula", '''{n}Her hand drops. The music continues on the other side of the door.{/n}
"Then wonder."
{n}She sits at the dressing table and picks up the comb. Its teeth catch in a strand of hair. She works them free, looking at you in the mirror, and resumes.
You remain beside the window. From here the drawer would be easy to reach if you leaned past her.{/n}
"You could have put it away before I arrived," {n}you say.{/n}
"Yes. I could also have made a dream in which you wanted precisely what I intended. I find I have acquired expensive tastes."
"You wanted the dance."
"I asked for one. You may recall the exchange. It was brief."
{n}You let the next phrase of the song pass. She separates another strand of hair and draws the comb through it with infuriating care.
When the singer begins again, you sit on the end of the couch. Nocticula watches your reflection settle.{/n}
"I am staying," {n}you say.{/n}
"I can see that."
{n}She finishes with her hair before opening the drawer. By then the song has ended. She puts the comb down and unfolds the note; the place where she offered her hand remains empty between you.{/n}''', c('[Listen when she chooses to speak.]', "note")),
    n("note", "Narrator", '''{n}Nocticula stands at the dressing table, removing an earring. She leaves the other in place while she examines the note written on blue paper.
She looks at you in the mirror.{/n}
"Ilvara has discovered that I have other people in my life. She considers this a weakness she may be able to purchase."
"Which people?"
"She is not yet particular. Servants, lovers, useful acquaintances. She has asked whether any of them would prefer to negotiate without me."
{n}Nocticula sets down the earring. The note curls at one corner but does not burn.{/n}
"An entirely reasonable question. I have asked it about my enemies often enough. What interests me is whether she understands the difference between another person's desire and a price she can name on their behalf."
"You sometimes make that mistake."
{n}She turns from the mirror with an expression that might become dangerous if either of you pretended the remark was accidental.{/n}
"Yes. I sometimes do. I prefer discovering it before the person concerned becomes useful to somebody else."
{n}She offers you the note. Its wording assumes that everyone who shares Nocticula's bed is either paid for it or waiting for revenge. It has not occurred to Ilvara that anyone might go back to it for the teeth.{/n}''',
      c('"Has she approached Laulieh?"', "laulieh", requires=f("parent_laulieh")),
      c('"Has she approached Laulieh about leaving with you?"', "departure", requires=f("parent_laulieh_departure")),
      c('"Who has actually received an offer?"', "courier")),
    n("laulieh", "Nocticula", '''"Indirectly. Through a servant who was paid far too little to risk delivering it discreetly."
{n}Laulieh returned the offer. She added a note of her own, informing Ilvara that if she wanted to know what Laulieh desired, she could begin by learning to address her rather than discussing her as an accessory to a bargain.
Nocticula permits herself a pleased smile.{/n}
"She has been paying attention. I should probably be concerned."
"Did you ask whether she wanted anything the offer contained?"
"She asked me first why I had allowed someone to believe she could be purchased so easily. It was a spirited conversation."
{n}Laulieh has made a demand of her own: no talk of harbors the next night she joins you. She means to have that evening on her own terms from beginning to end, and she said so to Nocticula's face.
Nocticula has granted it the way she grants a clever courtier a jewel she was already tired of, and tells you so with visible pleasure in the girl's nerve.{/n}
"You may answer her yourself when you next meet," {n}she says.{/n} "I am not going to put an agreeable sentence in your mouth merely because it would make scheduling easier."
"That has not always stopped you."
"I am displaying restraint. Try to appreciate it before it becomes tedious."''', c('"Then her invitation gets its own answer, outside this undertaking."', "others", flags=f("laulieh_request_heard"))),
    n("departure", "Nocticula", '''"She has heard that Laulieh hopes for a future beyond the Abyss. She believes hope is a form of unpaid debt."
{n}Nocticula places a second sheet beside the first. Laulieh has written only a few lines. She wants any promised opportunity to leave judged by what she does, not by whether she can remain useful to the Commander's negotiations.
Her handwriting presses hard enough to mark the sheet beneath.{/n}
"You asked me to give her a chance," {n}Nocticula says.{/n} "You did not acquire the right to decide what she should be grateful for. Neither did Ilvara."
"And neither did you."
{n}Nocticula's glance is cool.{/n}
"I acquired several rights by employing her. Gratitude was not one of the dependable ones."
{n}She lets the joke stand for a moment, then becomes more exact. The promise she made Laulieh stands in exactly its original words, and not one syllable wider. Nocticula has never in her existence widened a promise because somebody wept at it.
What she will not permit is Ilvara selling the girl a cheaper escape out of the gap.{/n}
"Laulieh is mine to disappoint," {n}she says.{/n} "Not Ilvara's. If anyone is going to sell that girl a lie about her future, it will be someone who can afford to make it true."''', c('"Keep the promise in its actual terms. No invented certainty."', "others", flags=f("laulieh_request_heard"))),
    n("courier", "Nocticula", '''"A courier called Senet. He carries private letters between houses whose owners dislike being seen speaking. Ilvara offered him a route which would let him deliver before he departed."
"After what happened to her passengers?"
"She omitted that part. Senet supplied it, having a better memory than she expected."
{n}He brought the offer to Nocticula and asked whether she intended to confiscate his correspondence while investigating it. She told him that depended on whether the letters concerned her. He replied that all private correspondence concerns someone, which did not answer the question.
Nocticula seems almost fond of the exchange.{/n}
"He has lovers in two houses which would both pay to learn about the other. He has managed not to sell either address. Ilvara assumed that meant he had not been offered enough."
"What does he want from you?"
"A public warning that her promised route has not been verified, and a private assurance that he can decline my employment without being counted among her allies."
"Will he get them?"
"Yes. I have plenty of couriers. I would like to keep having ones who bring me an interesting offer before accepting it. The last one who accepted first is decorating a gate in the Lower City, and the gate does not carry letters."
{n}She folds the note. Senet has crossed out the offered sum so thoroughly that the paper has torn. Nocticula holds it up to the mirror and peers through the hole.{/n}''', c('"That is a better reason to bring you an offer than fear alone."', "others", flags=f("courier_request_heard"))),
    n("others", "Nocticula", '''"And you?"
{n}She comes around the dressing table. Only one earring remains, giving her appearance an unfinished intimacy more convincing than any deliberately careless gown.{/n}
"If somebody offered you an evening I could not supply, would you come and confess it to me, like a boy who has broken a window?"
"You have asked me that before."
"I asked whether I minded your other lovers. I do not. I am a Demon Lord, not a farmer's wife. I am asking whether you would enjoy them less if I did."
{n}She has watched a great many mortals sharpen their pleasures on the idea of her jealousy. She has no intention of supplying it to you for free.
She takes the remaining earring off and sets it beside its mate.{/n}
"Keep your lovers. Keep their secrets too. A man who brings me other people's confidences as love-gifts will one day carry mine to somebody else, and I have killed people for that, slowly, in front of the person they carried it to."
"And if our interests collide?"
"Then we shall have a war. A small, private one. I shall enjoy it enormously; it is so much better than sulking over a kiss."''',
      c('"I can want you and keep other promises. I will tell you when they conflict."', "promise"),
      c('"I intend to keep my private life private. You receive what I choose to share."', "private")),
    n("promise", "Nocticula", '''"A useful answer. I expect it to become inconvenient."
{n}She takes a fistful of your collar and draws you against her, and kisses you with none of the ceremony she gives a courtly audience.
Afterward her thumb holds your chin where she wants it for a moment longer.{/n}
"If a conflict comes, I may ask you to choose against me. I may also argue very persuasively that you should not. I am not promising to be pleasant merely because you have been honest."
"I would have suspected a forgery if you had."
{n}That makes her laugh. She keeps your hand as she turns back toward the mirror, examining the two of you without changing either reflection.
She raises your joined hands until their reflection covers the folded note, then presses a kiss to your knuckles.{/n}''', c('[Keep the promise to name actual conflicts.]', flags=f("others_discussed", "conflicts_named"))),
    n("private", "Nocticula", '''"Then you must be prepared for me to keep mine."
"I am."
{n}She studies you long enough that a less certain answer might begin to defend itself. You let it stand.
At last she nods.{/n}
"Good. I have no desire to spend eternity explaining every closed door to someone who imagines a lover's interest is the same thing as a ruler's warrant."
"You might remember that yourself."
"I might. You may have the pleasure of reminding me when I do not."
{n}She kisses you, then draws back.{/n}
"If one of your private correspondents plans to kill me, I expect a warning."
"The same applies to yours."
"Mine plan it so frequently that you would soon stop opening the letters. I will warn you when one becomes competent."
{n}She picks up an earring and offers it to you, turning her head so you can fasten it.{/n}''', c('[Keep the private lives beyond this room.]', flags=f("others_discussed", "privacy_named"))),
], "aftermath_heard")

s("hearing", "A hearing without absolution", [
    n("start", "Narrator", '''{n}Ilvara's hearing takes place in a chamber with no audience. Nocticula brings you the account afterward, reproducing the testimony and marking every interruption her recorder noted.
The magician stands beside a table on which the instrument has been dismantled. Her shoes are still white. She keeps them together while her fingers move against the table's edge, counting something her testimony has not yet named.
She begins by reminding Nocticula that the passengers survived.{/n}
"I reminded her that they would not have needed rescuing if she had not sold their arrivals," {n}Nocticula says.{/n} "We proceeded more efficiently after that."
{n}Ilvara claims to have found the harbor abandoned. Its original maker had used it to conceal refugees from a pursuit. The first passengers left return witnesses outside. Later passengers were brought without understanding the precaution. When nobody arrived to claim them, their unfinished journeys became the structure that kept the harbor intact.
Ilvara discovered how to sell access to it. She did not discover how to make it safe.{/n}
"She calls that a distinction in culpability," {n}Nocticula says.{/n} "I call it a useful technical history. We are both listening very carefully to different parts of her account."
{n}The testimony pauses where Ilvara insists that she never intended permanent captivity. Nocticula lets you read the sentence twice.{/n}
"Your question," {n}she says.{/n} "What would you have asked at this point?"''',
      c('[Compare her account with the transfers and return-token rules. Knowledge: World, DC 32.]', check=dict(Skill="SkillKnowledgeWorld", DC=32, Success="contradiction", Failure="incomplete", CommanderOnly=True)),
      c('"When did she first learn a passenger could not leave?"', "date"),
      c('"Ask which part of her business would fail if every customer understood it."', "business", requires=("trickster",))),
    n("contradiction", "Nocticula", '''{n}You return to the third transfer. Ilvara sold a claim after the original passenger had failed to return, then recorded the profit as storage rather than passage. She already knew the journey could not finish on its own.
The dates do not establish when she learned every rule. They establish when she began earning money from somebody else's failure to leave.{/n}
"That is the contradiction," {n}you say.{/n} "Not that she intended every captive to remain forever. That she had begun charging for the condition she claims was an accident."
{n}Nocticula moves the testimony aside and reproduces a later question from her own hearing. It asks why the storage fee increased when relatives stopped inquiring.
Ilvara's answer is evasive. She says uncertainty raises costs.{/n}
"We arrived by different routes," {n}Nocticula says.{/n} "At much the same unpleasant place."
"You already asked it."
"I wanted to see whether you would find it without being invited to admire me."
{n}She smiles when you look at her.{/n}
"You may admire me now, if it would improve the evening."
{n}Your reading gives the account a firmer point. Any future bargain must begin with Ilvara admitting what she knew when she charged the fee, not with the convenient claim that she merely inherited somebody else's mistake.{/n}''', c('"Keep that admission as a condition of any employment."', "terms", flags=f("hearing_proof"))),
    n("incomplete", "Narrator", '''{n}You find a transfer that seems to precede Ilvara's ownership, but the dates were recorded under different harbor calendars. Nocticula supplies the correction before you finish accusing her witness of an impossible sale.
The error does not make Ilvara innocent. It means this particular accusation will not hold.{/n}
"I dislike an enemy who can win an argument by pointing at my arithmetic," {n}Nocticula says.{/n} "We will not give her that pleasure."
{n}She asks the question another way: when did Ilvara first refuse a relative's request to bring someone home?
The answer is less exact than the contradiction you hoped to find. Ilvara admits refusing, but says she believed the relative could not safely serve as a return witness. She will not name the supposed danger. Nocticula's recorder notes a long silence.{/n}
"We have enough to restrain her," {n}Nocticula says.{/n} "Not enough to claim that every defense has been answered. If we employ her, someone will have to watch the part she refuses to explain."
"That is another cost."
"Yes. An uncertain answer is not a cheaper answer merely because you have stopped asking."
{n}She crosses out your failed comparison rather than preserving it among the evidence. The hearing continues with its limits visible.{/n}''', c('"Record the uncertainty. Do not turn a failed argument into proof."', "terms", flags=f("hearing_uncertain"))),
    n("date", "Nocticula", '''"A good question. My recorder asked it while I was deciding whether to remove the table."
{n}Ilvara says she learned during her second season operating the harbor. A passenger's return witness had died. She tried to substitute a paid clerk, but the harbor rejected an appointment neither person believed had been made. She then kept the passenger inside while searching for another method.
She did not stop selling journeys.{/n}
"She describes that as keeping the harbor funded until a solution could be found."
"Did she spend the money on a solution?"
"Some. Not all. I have heard more elaborate versions of the same defense from governors with excellent reputations."
{n}In the margin of the testimony Nocticula has copied a phrase from the advertisement: improvements included at no further charge. She taps it with her nail.{/n}
"You may decide she has nothing worth buying," {n}Nocticula says.{/n} "But if you decide to buy, you should know which of her habits the price does not include changing."''', c('"Any future experiment needs a return condition before it begins."', "terms", flags=f("hearing_limits"))),
    n("business", "Nocticula", '''{n}She repeats your question slowly, enjoying the shape of it.{/n}
"Which part would fail if every customer understood it. Yes. That is more difficult to decorate than an accusation."
{n}The account resumes at the end of the hearing. Nocticula asked Ilvara to describe a voyage she could sell while disclosing every known hazard. Ilvara proposed cargo without passengers. Nocticula asked who would unload it. Ilvara proposed remote handling. Nocticula asked what power would pay for the harbor's continued existence after the last unfinished journey ended.
There was no answer ready.{/n}
"She needed somebody not to know," {n}you say.{/n}
"Precisely. Not because ignorance is a universal requirement of her magic, but because it was the cheapest material in her business."
{n}Nocticula turns the dismantled instrument so that its empty pins face upward.{/n}
"A new method might work. It would cost research, failures, and power she could no longer borrow from missing people. She wanted my patronage because I could afford all three."
"Then make her sell you the problem honestly."
{n}Nocticula leans back in her chair, studying you. Then she takes Ilvara's proposed fee and strikes through it.{/n}
"You do have a gift for making a clever thief discover she has applied for an ordinary job."''', c('"Let the price reflect work not yet done, not power she stole."', "terms", flags=f("hearing_business"))),
    n("terms", "Nocticula", '''"I have three choices worth considering."
{n}She sets the half-coins in a line, one for each proposed outcome.
Ilvara can remain in confinement while independent researchers examine her account. It is the safest way to keep her from repeating the trade and the slowest way to learn anything useful.
She can work under a restricted commission, unable to conduct a live crossing without witnesses and a verified return. That retains her skill and requires Nocticula to keep paying attention to a woman who has earned distrust.
Or she can be expelled after surrendering the instrument and the names of her buyers. That ends Nocticula's immediate responsibility while leaving an ambitious magician elsewhere in the worlds.{/n}
"You have not listed execution."
"I have not forgotten it. I have decided her surviving knowledge may be more valuable than the satisfaction. If she attempts another sale of a person under my name, that calculation changes."
{n}She looks toward the place where Ilvara stood, then turns the coin under her thumb. The rim has bitten into the table.{/n}
"What do you advise? You will not be the person who has to employ her. I will remember that when weighing your answer."''',
      c('"Confine her and separate the research from her control."', "confine"),
      c('"Give her the restricted commission. Use her talent without buying her excuses."', "commission"),
      c('"Take the information, break her claim here, and expel her."', "exile")),
    n("confine", "Nocticula", '''"Prudent. Inconvenient. Expensive."
{n}Nocticula chooses a place where Ilvara can write and be questioned without access to the instrument. She does not promise comfort. Her instruction to the jailers is brief: they may take anything from the prisoner that does not hold a pen or answer a question. Several of them are disappointed by how little that leaves.
The commission goes to other researchers. Every claim in Ilvara's account must be reproduced before anyone is allowed to risk a living traveler.
This will take longer. Nocticula refuses to give a date she does not possess.{/n}
"You have denied me the quickest way to keep the thing I wanted."
"You asked for my advice."
"And I have taken it. You need not become defensive merely because I intend to complain."
{n}She touches the first coin with a nail. It turns black.
Ilvara will remain alive and unavailable to her former buyers. The unfinished work survives without the woman who profited from it directing the next attempt.{/n}''', c('[Accept the slow, guarded research.]', flags=f("hearing_finished", "ilvara_confined"))),
    n("commission", "Nocticula", '''"You are willing to keep a dangerous person useful. I wondered how long that would remain an abstract opinion."
{n}The commission is narrow. Ilvara must disclose every remaining claim on the harbor, surrender her private return tokens, and work with an observer she cannot dismiss. No living traveler enters a new experiment until an independent return has been demonstrated.
Nocticula keeps the right to end the work, and the magician, whenever it stops amusing her. Ilvara may refuse the commission and take the cell instead. Neither of them calls the arrangement trust.{/n}
"She will try to become indispensable," {n}Nocticula says.{/n}
"Then make sure more than one person understands what she does."
"I intend to. She will find teaching considerably more exhausting than extortion."
{n}There is pleasure in her voice. She has retained a skilled enemy and made that enemy share the source of her advantage. Whether it lasts will depend upon the attention she actually gives it.
The second coin acquires a narrow inscription, too small to read until you hold it close.{/n}
"The terms," {n}Nocticula says.{/n} "I thought she might appreciate a contract with less empty space."''', c('[Accept the dangerous, supervised commission.]', flags=f("hearing_finished", "ilvara_commissioned"))),
    n("exile", "Nocticula", '''"You would rather send the difficulty beyond your sight. There are worse instincts. There are also more flattering ways to describe that one."
{n}Ilvara will surrender the instrument, the remnants of the protected cloth, and a verified list of buyers. Rhez will escort her to a departure whose destination Nocticula knows. No promise is made that other rulers will welcome her.
The expulsion is not freedom from every consequence. It is the end of this bargain in this city. The people she cheated retain their own claims, and Nocticula will not furnish a false recommendation to make the exile comfortable.{/n}
"She may begin again," {n}you say.{/n}
"Yes. Without this door, without my mark, and with several people better informed about her methods. If you wanted certainty, you should have chosen a prison and accepted the work of keeping it."
{n}The third coin slides across the table until it falls out of the dream.
Nocticula watches it go. Then she dictates a second letter, identifying Ilvara to the authorities at the first port her ship must reach.{/n}''', c('[Accept the expulsion and its unresolved future risk.]', flags=f("hearing_finished", "ilvara_exiled"))),
], "others_discussed")

s("last_buyer", "The last buyer", [
    n("start", "Narrator", '''{n}The buyer who planned Ilvara's escape has finally introduced himself. His name is Ossin. He represents a small consortium of merchants whose success depends upon knowing which borders can be crossed before their owners notice.
Nocticula presents his letter as though serving a dish whose smell offends her.{/n}
"He believes I have taken possession of the harbor. He wishes to buy exclusive access. In the event that I refuse, he proposes to inform several interested parties that I have been maintaining a private prison beneath my own protection."
"An accusation made out of part of the truth."
"The most economical kind."
{n}Ossin knows the Black Flower was real. He knows passengers disappeared. He does not know which parts of the instrument survived, what happened at the final lamp, or what Ilvara told during her hearing.
He assumes the missing information can be purchased from somebody who resents Nocticula enough to sell it.{/n}
"I could kill him," {n}she says.{/n} "Then his partners would sell the accusation at a memorial dinner and congratulate themselves on having discovered my vulnerability. I would prefer they learn a more useful lesson first. I can always kill him afterward; he is not going anywhere I cannot reach."
{n}She spreads the letter beside three intercepted invoices. The papers differ in age and handwriting. Each names a storage facility that has already changed owners twice.{/n}
"If we answer the wrong person, we merely improve somebody else's understanding of my affairs. I would like the people who will profit from this threat to hear the answer together."''',
      c('[Identify the common guarantor hidden in the invoices. Knowledge: World, DC 33.]', check=dict(Skill="SkillKnowledgeWorld", DC=33, Success="guarantor", Failure="false_lead", CommanderOnly=True)),
      c('"Publish the passengers\' accounts and the limits of what you claimed."', "public"),
      c('"Sell them the exclusive right to a route whose limits you describe exactly."', "auction", requires=("trickster",))),
    n("guarantor", "Nocticula", '''{n}The companies do not share an owner. They share a guarantor, a woman whose signature appears only when a debt changes hands. She has promised to cover losses from an interrupted voyage. If the harbor is exposed as a fraud, she owes money to every buyer at once.
You place the three signatures beneath Ossin's threat.{/n}
"He is not simply trying to acquire your route. He needs you to acknowledge it exists so his guarantor can deny the claims."
{n}Nocticula reads the arrangement and begins to smile.{/n}
"A threatened scandal which protects the person threatening it. Yes. I should have expected a more interesting motive than greed."
"Greed remains involved."
"As it should. One must not neglect the fundamentals."
{n}She can now send the answer to every insured buyer as well as the guarantor. The letter will state exactly what survived and which journeys were sold without a reliable return. Ossin must either contradict his own contracts or admit that his consortium helped finance Ilvara's operation.
You have not made his accusation disappear. You have made it expensive for him to tell only the profitable half.{/n}
"A very good afternoon's reading," {n}Nocticula says.{/n} "I am beginning to resent how much of our private time is improved by your ability to recognize a bad contract."''', c('"Send the complete account to everyone whose money depends on it."', "cost", flags=f("buyers_exposed"))),
    n("false_lead", "Narrator", '''{n}One repeated name appears to be the owner you need. Nocticula recognizes it as a dead merchant whose identity has been used to conceal three different debts. Your comparison has found a mask, not the face behind it.
The error costs the opportunity to answer quietly. By the time her agent verifies the name, Ossin has sent copies of the accusation to two buyers who have begun asking public questions.{/n}
"We can still tell the truth," {n}Nocticula says.{/n} "We will now be doing it after someone else has supplied the first version."
"Or buy the letters back."
"No. I will pay to learn a secret. I will not pay a man to repeat a threat he has already demonstrated he cannot keep exclusive."
{n}She destroys the dead merchant's false address and keeps the copies of the accusation. The investigation has lost surprise rather than acquired a fabricated culprit.
The passengers' accounts can answer much of the claim. They will also reveal that Nocticula did not discover the stolen use of her protection immediately. She dislikes that part enough that you know the decision to include it is real.{/n}''', c('"Then publish the complete account, including the delay."', "public", flags=f("buyer_read_failed"))),
    n("public", "Nocticula", '''"A public account will travel farther than your qualifications. Someone will say I sold the passengers. Someone else will say I rescued them out of love for mortals. I find both versions irritating."
"The witnesses can describe what happened."
"They can. They may also discover that people prefer the more flattering lie."
{n}She releases the records and keeps the passengers' private histories back, because they are hers now and she does not give away what she owns for nothing. Vessa's drawings go out at Vessa's price. Sere's letters stay in Nocticula's cabinet. Tomar collects his wages and is told, very pleasantly, that the first time he sells the story in a tavern will be the last time he sells anything.
The statement includes the use of the old protection, Ilvara's sales, the return, and the remaining uncertainties. It does not claim Nocticula had always intended the outcome.{/n}
"Ossin will dislike the loss of his private audience," {n}she says.{/n} "He wanted me alone in a room with the accusation. Now he can explain it to everyone whose money he proposed to collect."
{n}Nocticula sets the statement beside the threat. She has chosen to surrender some control over her reputation rather than purchase a fragile silence.
It is not an act she intends to repeat every time somebody says something unkind.{/n}''', c('[Release the bounded account and protect the witnesses\' private details.]', "cost", flags=f("account_public"))),
    n("auction", "Nocticula", '''"That sounds remarkably close to the business we have just dismantled."
"Only if we sell what we do not possess. Offer exclusive access to the records, not the harbor. Let him explain to his investors why the difference disappoints him."
"He may notice before paying."
"Then he has learned to read. Either outcome improves the conversation."
{n}You draft an invitation to bid on the technical account, with every absence listed plainly: no guaranteed passage, no ownership of travelers, no claim on Nocticula's future protection. The price includes a public acknowledgment of which voyages the buyer previously financed.
Ossin can refuse. He can also accept and surrender the secrecy that made his accusation profitable. His competitors receive the same terms at the same time.{/n}
"You have turned his threat into a question about whether he wants his rivals to know more than he does," {n}Nocticula says.{/n} "That is much better than pretending he will become honest because we caught him lying."
{n}She makes one change. The proceeds will pay the outstanding claims from the voyages before the consortium receives a single page. If there is nothing left afterward, she will accept the pleasure of watching them calculate the loss.
Nocticula seals the offers one at a time. Each bears the same closing hour. She saves Ossin's for last and puts his name inside, where the next clerk to open it will see what their principal has been buying.{/n}''', c('[Offer the exact, limited auction to every interested buyer.]', "cost", flags=f("records_auctioned"))),
    n("cost", "Nocticula", '''"There is one more matter. Ilvara's disposition will become part of the answer whether we publish it or not."
{n}She draws the three half-coins from the hearing out of the letter's shadow. Only the one you chose remains solid.{/n}
"If I have confined her, Ossin will accuse me of hiding the witness. If I have employed her, he will say I have inherited the trade. If I have expelled her, he will try to buy her account. None is an argument for pretending we chose differently."
"What will you say?"
"What I did. With sufficient detail to make the useful questions possible and the useless ones expensive."
{n}Nocticula's hand closes around the surviving coin. She looks tired of the affair without being tired of you, a distinction she has not previously made much effort to show.{/n}
"You may take your share of the credit. You may also leave your name out. I do not need the Commander printed beneath my account as a certificate of good behavior."
"How generous."
"It is not generosity. I am deciding how much of you to spend in public, and I should like your opinion before I spend it. Do not waste the question by asking which answer would please me."''',
      c('"Name my part accurately. I helped make the decisions."', "named"),
      c('"Keep my name private. The witnesses do not need another famous person in their account."', "unnamed")),
    n("named", "Nocticula", '''"Then they will know you helped me. Some will stop listening before the rest of the sentence."
"They already do that when they hear your name."
"Yes. It is occasionally convenient."
{n}The final account names your questions and advice without crediting you for work Rhez, Vessa, or the carrier performed. Nocticula refuses a sentence praising your moral leadership. She replaces it with the particular decision for which you were responsible.
One of Ossin's buyers has returned the notice with your name circled. He wants his passage money back from the crusade. Nocticula lays his demand beneath the signed account. "He has stopped asking me. How quickly a grateful merchant learns a new address."
Nocticula studies the finished wording, then touches your signature with a finger.{/n}
"There. You are in dangerous company again. I hope you continue to find it worth the trouble."''', c('[Stand by the part you actually played.]', flags=f("buyer_answered", "work_named"))),
    n("unnamed", "Nocticula", '''"Very well. I will not invent a mysterious adviser merely to make the omission seem important."
{n}The account credits the people who performed the work and the authority under which Nocticula commissioned it. Your private involvement remains between those who already know it. She warns that silence is not a lock; Ilvara and Ossin may still guess, and guessers are cheap to kill but tiresome to count.
You accept the distinction.
Nocticula folds the final statement and puts it aside. Then she steps close enough to straighten a crease in your collar which the dream did not need to supply.{/n}
"I know what you did," {n}she says.{/n} "Do not imagine I will require a public document to remember an inconvenient answer."
"Or a useful one."
"Especially an answer which managed to be both."
{n}She kisses you before allowing the room to fade. For a moment the seal on her letter remains visible in the darkness, a black flower pressed into red wax.{/n}''', c('[Keep the work private without denying it.]', flags=f("buyer_answered", "work_private"))),
], "hearing_finished")

s("empty_chair", "The guest who was not invited", [
    n("start", "Narrator", '''{n}Tonight the dream contains a dining table set for three. One chair lies on its side. Nocticula stands over it, holding a small mask by its ribbon.
The mask is smiling. Its mouth has been cut too wide for the face, and the white paint around it is chipped.{/n}
"If you intend to ask whom I have killed, begin with the more useful question of who sent this."
"Whom have you not killed yet?"
"A hostess. She is relying upon my remembering the difference."
{n}She places the mask on the overturned chair. It is a dream copy of an object delivered to Rhez, who has declined its accompanying invitation.
The sender is Istrava, a lamia who keeps a hunting lodge above one of Alushinyrra's older pleasure gardens. Her guests pay to be introduced to people who cannot refuse the introduction. Sometimes she supplies prisoners. More often she supplies frightened debtors and calls their appearance voluntary.
After the harbor account reached her, Istrava announced an evening honoring the people who had deprived several of her patrons of their investments. Rhez is to receive a prize. The invitation does not say what must happen before she can collect it.{/n}
"Ossin's partners?"
"Some of them. He did not invent resentment. He has merely supplied it with a place to dine."
"And the third chair?"
"Mine. The fallen one belongs to the hostess. I was deciding whether to put it back."
{n}You look at the two upright chairs. Neither bears your name. Nocticula notices where your attention stops.{/n}
"I have not invited you into her house. This is my reconstruction from Rhez's report. If you propose an entrance, someone who can actually reach that entrance will have to make it."
"You could forbid the gathering."
"I could. Istrava would then become a woman who had frightened me into forbidding dinner. I would prefer a less generous obituary for her evening."''',
      c('"First decide whether this threatens the witnesses or merely insults you."', "threat"),
      c('"If she wants you angry enough to arrive without questions, disappoint her."', "temper")),
    n("threat", "Nocticula", '''"It threatens the people who accepted my protection. Whether it threatens me remains to be seen."
{n}She sets a second object beside the mask: a strip of yellow cloth, torn from a servant's sleeve. A woman named Edris delivered it with a sketch of the lodge's lower gallery. She used to tend the rooms there. Istrava dismissed her after an injured guest noticed how often the servants disappeared before the hunting horn sounded.
Edris says three attendants have been ordered to impersonate the returned passengers. Istrava has their descriptions from gossip, not their persons. She intends a performance in which an imitation rescue ends with the rescuers devoured by the guests.
Nocticula has already moved Rhez's next meeting away from its advertised location. She has not dragged the former passengers back out to be looked at. They are hers now, and she does not show her property to people she intends to kill.{/n}
"They are mocking the rescue with substitutes," {n}you say.{/n}
"They are teaching my agents what accepting my protection looks like when I am not in the room. The mockery is the part they hope I will answer."
"And the attendants?"
"At present, available for instruction. Istrava is not famous for telling them which part of the performance is real."
{n}She rights the chair with one foot. The gesture is careful rather than angry.{/n}
"We should decide what happens to the performers before choosing where to put the audience."''', c('"Tell me what Edris can actually show us."', "edris", flags=f("lodge_people_first"))),
    n("temper", "Nocticula", '''"You think I am angry."
"You have furnished a room in which to overturn one chair."
{n}She looks down at it, and a short sound escapes her that might be a laugh. There is no warmth in it, but some of the deliberation leaves her face.{/n}
"You may be useful this evening."
"An encouraging beginning."
"Do not become encouraged too quickly. Istrava wants the city to see me punish a joke because its subject embarrassed me. Several patrons would happily purchase that story with her life."
{n}Nocticula brings a strip of yellow cloth from beneath the mask. A former attendant named Edris sent it with a drawing of the lower gallery. Three servants have been assigned to portray the rescued passengers. The guests will enact a hunt. Edris does not believe the servants will be allowed to stop acting when they become afraid.
Rhez is already away from the meeting place named in the invitation. Nobody has sent for the real passengers. Nocticula does not parade what she owns for a lamia's benefit.{/n}
"Then arrive with something she did not prepare to answer," {n}you say.{/n}
"Her own servants would be persuasive."
"Provided they are still alive to speak."
"Yes. A tiresome limitation of the best witnesses."
{n}She rights the chair. Its legs scrape the floor loudly enough to end the joke.{/n}''', c('"Tell me what Edris can actually show us."', "edris", flags=f("lodge_pride_named"))),
    n("edris", "Nocticula", '''{n}The table becomes a model of the lodge. Its windows are dark; the lower gallery is represented by three narrow strips of pale wood. Nocticula leaves gaps where Edris could not remember a measurement.
Edris has offered to guide one person through the service entrance. She will not go upstairs. Her last employer made her carry a guest's severed antler through that doorway while the guest begged for it back. She does not know what manner of creature he was. She remembers how lightly it weighed.
Nocticula repeats the account without supplying the missing spectacle.{/n}
"She asked whether I could promise Istrava would never find her. I said no. She nearly left."
"Why did she stay?"
"Her sister still works there. I could have lied about the promise. I thought a woman who had already escaped one extravagant hostess might notice."
{n}Edris wants passage for herself and her sister to a place beyond Istrava's ordinary reach. Nocticula has offered transport on a known route after the operation, nothing grander: not the damaged harbor, and not a cure for every pursuit. If the sister would rather stay and be eaten, that is the sister's affair.
She also wants her sister's shoes. They belonged to their mother. Istrava keeps them in a cabinet with other possessions she permits her attendants to borrow for special evenings.{/n}
"We are not reopening Ilvara's door for a pair of shoes," {n}Nocticula says.{/n}
"I was going to suggest opening the cabinet."
"I know. I wanted to hear you say it. There is a particular expression people acquire just before asking me to improve the laws of existence because they dislike a lock."
{n}She watches you study the model. The gallery leads to a bell chamber, and the bell chamber has two stairways. One descends to the service yard. The other climbs toward the dining room. Edris has marked the second with a crooked cross.{/n}
"The bell announces the hunt. Until it rings, every servant must remain where the guests can see them. Afterward, the guests may follow anyone wearing one of these masks."
"Then whoever controls the bell decides when the house changes its rules."
"Perhaps. Edris cleaned the chamber. She did not design it. I would rather discover the difference before giving her a heroic instruction."
{n}Nocticula takes your hand and sets it beside the model, aligning your fingers with the two stairways. The contact lasts just long enough to become intentional.{/n}
"Choose what you want from this," {n}she says.{/n} "Do not leave me to guess whether you mean to save servants, humble a hostess or impress me."
"Those ambitions may cooperate."
"For an evening. Then one generally sends the others an unexpected bill."''',
      c('"The attendants leave alive. We can be inventive about her humiliation afterward."', "purpose", flags=f("lodge_rescue")),
      c('"Take her house from her. Give every frightened servant a better reason to obey us."', "purpose", flags=f("lodge_conquest"))),
    n("purpose", "Nocticula", '''"Then we have an object. We still need a way into a house whose owner expects my temper to arrive ahead of me."
{n}She removes the mask from the chair and offers it to you by its unbroken edge. The paint is cool against your thumb. Nothing behind its eyeholes resembles a face.
You turn it over. On the reverse, a little hook has been sewn into the ribbon. It is meant to catch when the wearer tries to pull the mask away.{/n}
"An economical hostess," {n}you say.{/n}
"And an unimaginative one. She has mistaken difficulty in leaving for a reason to stay."
"You sound personally offended."
"I have spent a great deal of effort learning the difference."
{n}She holds out her hand. You return the mask; she places it on the table, facedown. Tonight, at last, she sits beside you rather than behind the arrangement.
Together you examine Edris's sketch until you can describe both stairways without looking. Nocticula corrects the width of a landing, then admits the correction is her guess and removes it. The missing measurement remains missing.
Before she lets you wake, she asks you to name the one thing she should not promise on your behalf.{/n}''',
      c('"Don\'t put a living person at risk and tell them I agreed to it."', "vow_guard", flags=f("lodge_proposed")),
      c('"Promise what you like in my name. I want to approve which lives you spend."', "vow_ledger", flags=f("lodge_proposed"))),
    n("vow_guard", "Nocticula", '''{n}She considers that longer than you expected.{/n}
"A conscience with a clause in it. How lawyerly of you." {n}Her mouth curves.{/n} "Very well. Then return with a plan before I grow fond of my own. I have had a head start."
"I noticed the furniture."
{n}This time her laugh is real.{/n}''', c('[Prepare a plan for the lodge from the information actually available.]')),
    n("vow_ledger", "Nocticula", '''{n}Her eyes go very bright.{/n}
"You want the list. Who goes down the stairs first, who holds the door, who is left in the gallery if the bell rings early." {n}She leans closer.{/n} "Most of my generals want to be told afterwards, so they can mourn with a clear heart. You want to sign it." {n}A slow smile.{/n} "I shall send you the list, then. Every name. You will learn how heavy paper can be."''', c('[Prepare a plan for the lodge from the information actually available.]')),
], "buyer_answered")

s("mask_and_bell", "A mask with its mouth shut", [
    n("start", "Narrator", '''{n}The model has acquired a bell. Nocticula suspends it over the dining table by a thread, with an ordinary spoon inside for a clapper.
You touch the rim. It makes a small, disagreeable sound.{/n}
"Edris says the real one is silver. I considered supplying the proper material, but this noise has already improved my opinion of silence."
{n}Rhez has visited the lodge's supplier under a borrowed name. The hunting masks are ordinary objects. The bell is not. Its enchantment marks the people counted as quarry when the host names them, and the house's hunters can then follow those marks through its galleries. The marks end when the bell is rung again by the person holding the host's baton.
The supplier knew the arrangement because Istrava once refused to pay for a repair after an evening ended too soon. He kept her complaint.
Nocticula has not bought the bell or copied its enchantment into the dream. She has copied the complaint.{/n}
"A second ringing ends the hunt," {n}you say.{/n}
"If we possess the baton. If the bell has not been altered since that repair. Rhez answers to me for both, and if either fails I shall want to know whose idea wasted my agent."
{n}The baton usually remains beside Istrava's chair. Her chamberlain, Vhal, carries it when she leaves the room. He is a cambion with a talent for making guests believe every inconvenience was arranged especially for them.
Edris remembers that he has never accepted a mask himself.{/n}''',
      c('[Read the repair complaint for a way to stop the first marking. Use Magic Device, DC 34.]', check=dict(Skill="SkillUseMagicDevice", DC=34, Success="silence", Failure="fracture", CommanderOnly=True)),
      c('"Send an irresistible guest. Let Istrava surrender the baton to welcome you."', "guest"),
      c('"A hostess must greet her guests. Send her an invitation addressed to herself."', "trick", requires=("trickster",))),
    n("silence", "Nocticula", '''{n}The disputed repair replaced the bell's suspension, not its clapper. Istrava complained that the bell rang when a guest struck the outside. The supplier answered that a hunt could only begin when the baton touched the bell's inner lip.
You turn the copied complaint toward Nocticula and set the spoon against the rim from within.{/n}
"Make the first blow miss. Vhal can announce the hunt, but he cannot mark anyone with an empty gesture."
"The supplier may have improved it."
"Then we verify the inner rim before depending on it. Edris knows the cleaner who polishes it."
{n}Nocticula unfolds a second report. Rhez has already questioned the cleaner through Edris: the inner lip still carries the inscription, and old wax has lodged beneath it. The supplier's complaint now makes that observation useful. A thin packing of the same wax can absorb one touch of the baton without appearing new.
The cleaner has offered to help if she can leave before the gathering. She will not wait inside to see whether a plan works. Nocticula adds an instruction for Rhez to meet her outside before any signal is given.{/n}
"One quiet bell," {n}she says.{/n} "Afterward, everybody will know somebody has been touching it."
"Then we should already be doing something they cannot ignore."
{n}She leaves the spoon lying across the model. The first advantage is small, bought from somebody whose name the guests have never bothered to learn.{/n}''', c('[Use the verified packing to prevent the first marking.]', "limits", flags=f("lodge_silent_bell"))),
    n("fracture", "Nocticula", '''{n}You find the damaged mounting and suggest loosening its pins. Nocticula lets you finish before turning over the supplier's sketch. A second brace is fixed inside the housing. Without removing it, the bell would tilt rather than fall, leaving its inner lip directly beneath the baton.
You have nearly devised a way to make the hunt easier to begin.{/n}
"I prefer that you do your dangerous guessing here," {n}she says.{/n}
"You could have stopped me sooner."
"You were about to discover whether I enjoyed being right more than I enjoyed keeping an agent alive. I thought the discovery might be useful."
{n}She removes the pin from the dream model. The spoon strikes its exposed rim. Both of you endure the noise until you put the pin back.
The failed reading leaves you without a reliable way to silence the bell. The supplier has closed his shop for the gathering, and Rhez cannot obtain a fresh inspection without advertising the interest. There is still a direct entrance: Nocticula can attend as a guest, making Istrava stand to receive her. Vhal will then carry the baton, and Rhez can watch him from the service stair.
The bell may ring before she reaches him. Every attendant must be warned to run when it does, whether the guests believe the performance has begun or not.{/n}
"No pretending the plan is quieter than it is," {n}Nocticula says.{/n} "Tell me what you want the people downstairs to do when subtlety fails."''', c('[Use the guest entrance and warn the attendants about the first ringing.]', "limits", flags=f("lodge_bell_read_failed", "lodge_guest_entry"))),
    n("guest", "Nocticula", '''"She would enjoy that. She would also spend the evening wondering whether enjoyment was the mistake."
{n}Nocticula asks what you propose she wear. When you answer that it should give Istrava a reason to leave her chair, she looks at you as if you had moved a piece she had not seen.{/n}
"That is a remarkably indirect compliment."
"I was trying to keep it useful."
"Try less hard."
{n}The plan is simple enough to survive a frightened messenger. Nocticula will enter through the front. Istrava must either receive her or publicly refuse a guest she has spent days pretending to invite. Vhal will take the baton when his mistress rises. Rhez will approach him from the service stair while the room is watching somebody else.
Nocticula will use her own form. No double will hold a room full of demons through the first unexpected question. You will not be transported there by wanting to attend.
There is no promise that the bell remains silent. The attendants will be warned to run at its first sound, and Rhez will know that taking the baton matters more than keeping her cover.{/n}
"I shall have to trust someone else to enjoy the clever part," {n}Nocticula says.{/n}
"You can enjoy being impossible to ignore."
"I generally do. It is the occasions on which I need to be ignored that require better company."''', c('[Draw the audience toward Nocticula while Rhez follows the baton.]', "limits", flags=f("lodge_guest_entry"))),
    n("trick", "Nocticula", '''"Istrava will recognize her own address."
"Good. We need her to recognize her invitation too. Every guest was promised an honored quarry. Tell her the honor has been reserved for the only person qualified to preside over it."
"She will recognize a threat."
"A threat with excellent manners. Let her deny it before the other guests arrive. They will ask why she finds her own hospitality alarming."
{n}Nocticula considers the announcement. It forces Istrava to decide which part of her performance she is willing to defend in public.
Rhez can deliver the announcement through the lodge's musicians, who have been ordered to celebrate every guest's arrival. If they rehearse Istrava's arrival as well, the chamberlain must either interrupt the music or carry the baton out to conduct it.
The interruption will make him visible from the service stair. It does not make him helpless.{/n}
"She might laugh," {n}Nocticula says.{/n}
"Then she has bought herself time by admitting the joke. We still know who carries the baton."
"And if she orders the musicians punished?"
"Your entrance interrupts the order. We do not leave them waiting to discover whether our timing was amusing."
{n}Nocticula draws a small black flower beside the final line of the announcement.{/n}
"A joke which makes its author provide the rescue. You are becoming expensive company."''', c('[Use the public announcement to expose the chamberlain and protect its performers.]', "limits", flags=f("lodge_self_invitation"))),
    n("limits", "Nocticula", '''{n}The plan still has a lower floor. Nocticula turns the model so that the service yard faces you.
Edris can open one door. Beyond it, her sister and the others must run on their own legs. Rhez has two hands and a stair to hold, and anyone who stops at the door to argue will be left for the guests.
Nor can she remain indefinitely. Once the hunt begins, the gallery will become a corridor through which armed guests expect to pursue something.{/n}
"I want Vhal alive," {n}Nocticula says.{/n} "He knows which guests bought the performance before they were invited. If Rhez must choose between carrying him and keeping her own hands free, however, she drops him."
"That is unusually practical advice from someone who can make the whole room stop moving."
"I will be in a different room. Power does not make an agent less dead if I notice too late where I should have been looking."
{n}She says it with such irritation that you suspect the lesson once belonged to somebody whose name she has not offered. You do not ask for it as the price of believing her.
Instead you move the little figure representing Rhez from the upper stair to the yard. Nocticula moves it back. The baton must be taken before the second ringing can end the mark. You repeat the order until both movements fit without placing Rhez in two rooms at once.
The bell above you turns on its thread. Its spoon has come loose. You catch it before it hits the table.{/n}
"There," {n}Nocticula says.{/n} "A feat worthy of the Commander."
"I expect a song."
"You may have a silence. I have just learned to appreciate them."
{n}She takes the spoon from you and lays it aside. Then her fingers return to your empty hand, briefly, without a plan to illustrate.
She gives the instructions to her real agents after the dream. Their answers will belong to the next meeting; no gesture over this model can complete the operation tonight.{/n}''', c('[Let the agents prepare the agreed entrance and the service-yard withdrawal.]', flags=f("lodge_method_ready"))),
], "lodge_proposed")

s("uninvited_guest", "The entertainment answers back", [
    n("start", "Narrator", '''{n}You fall asleep in Drezen and wake standing up, in a mask, on a stair you have only seen in charcoal.
The lodge is louder than Edris's sketch. Below you lies Istrava's dining hall: long couches in a horseshoe, bowls of something that is still moving, a hundred candles burning in a smell of musk and spilled wine. Above the far end of the hall hangs the bell chamber, open on one side like a box at the theater, and in it the little brass bell on its hook, and beside it a narrow man in grey holding a baton across his palms like a priest holding a relic. Vhal. Below the hall, behind a railing, runs the lower gallery, where three attendants stand very still in white masks with their mouths cut too wide.
Nocticula is beside you. She wears black, and a mask of plain black silk that hides nothing; every person in this house knows who she is, and the mask is there so that they must pretend not to.{/n}
"Don't wake up," {n}she says without turning her head.{/n} "I went to a great deal of trouble to bring you, and you look lovely in that."
{n}On the highest couch lies the hostess. From the waist down Istrava is serpent, a long coil of dark green and gold that runs off the couch and across the floor and back again; from the waist up she is a handsome woman with a heavy jaw, and her black hair is threaded with tiny gold cages, each one holding a live moth. The moths beat against the bars whenever she laughs. She is laughing now. Around her the guests recline in their own masks, demons and worse and a few rich mortals with the shine of terror on them that they mistake for excitement. Three of them are Ossin's friends. Ossin is not among them. Nocticula knows exactly where Ossin is.
Istrava sees the black mask on the stair and raises her glass.{/n}
"Lady in Shadow. We had begun to fear you would take offense."
"At being invited so late? I assumed you had difficulty finding a chair you could afford to lose."
{n}The laugh goes round the horseshoe a beat too late. Nocticula smiles at it the way one smiles at a dog that has learned to sit.{/n}
"Stay here, at the rail," {n}she tells you, low.{/n} "Nobody in this house can touch you. The Gift sees to that, and so do I, and every one of them can smell it on you. You won't fight tonight, darling. You'll watch. And when I look up at you, you'll choose a name for the bell."
"Whose name?"
"Whoever you like. That's the joke." {n}She takes her hand off the rail.{/n} "She rings it, and her guests chase whoever it names. She does it under my protection, in my city, on my people. Hunting is a privilege, and in Alushinyrra the privilege is mine. Let's go and remind her."''',
      c('[Watch Vhal strike the bell you silenced.]', "silent", requires=f("lodge_silent_bell")),
      c('[Watch Rhez go for the baton.]', "guest", requires=f("lodge_guest_entry")),
      c('[Let the musicians read out her invitation.]', "announcement", requires=f("lodge_self_invitation"))),
    n("silent", "Nocticula", '''{n}Istrava claps twice. The musicians stop. Vhal steps to the bell with the baton raised, and the whole horseshoe leans toward him the way a crowd leans toward a gallows.
He strikes.
Nothing. Brass on brass, a dull little tap like a spoon on a cup, and then silence. The attendants in the gallery do not move. No light comes. Vhal strikes again, harder, and the bell swings on its hook and taps the wall, and someone at the end of the horseshoe giggles.{/n}
"Is that the entertainment?" {n}Nocticula asks the room, pleasantly.{/n} "A man discovering silence? I've seen it done better in my cells. They usually scream first."
{n}Istrava's coils tighten on the couch. She says something sharp to Vhal. Vhal, sweating, lifts the baton for a third try, and finds Nocticula standing beside him in the bell chamber, though nobody saw her climb the stair. She takes the baton out of his hand the way one takes a toy from a child.{/n}
"You won't need this. It doesn't work. I had it seen to." {n}She glances up at your rail, and her eyes in the black silk are laughing.{/n} "By someone with very clever thumbs."
{n}Vhal reaches for the baton. She lets him get his fingers on it and then breaks two of them, without looking, and he folds down onto his knees and stays there.{/n}
"Listen to me, all of you." {n}She does not raise her voice. She has never had to.{/n} "The bell has no working left in it. It's only a bell. But you all know what it means when it rings in this house. That was the only magic it ever had: you, doing as you're told." {n}She taps the brass with the baton, very lightly. It gives a small, clear note.{/n} "So it still works. It simply works for me."''',
      c('"Now the gallery."', "gallery", flags=f("lodge_unmarked"))),
    n("guest", "Nocticula", '''{n}Rhez comes in on Nocticula's arm, masked, in the green coat, looking bored. She has been invited as the guest of honor and she walks like it, straight down the middle of the horseshoe toward the bell chamber, and Vhal comes down from the chamber to bow to her with the baton across his palms, as the house rules say he must.
He is still bowing when she takes it.
It is very neat. It would have been perfect, except that a guest on the nearest couch, a bull-necked thing with a jeweled snout who has been drinking since before the candles were lit, sees the baton change hands and does not like it, and puts a knife into Rhez's arm.
Rhez does not drop the baton. She cannot stop it ringing, either: it strikes the bell as she twists away, once, and a line of pale fire runs across the masks in the lower gallery, and below you the three attendants scream together. The guests applaud. They think it has begun.
Rhez hits the bell again on purpose, harder, the second stroke that ends the marks, and the fire goes out. Then she sits down on the floor with her back to the bell chamber wall, holding her arm, and bleeds.
Nocticula has the snouted guest by the collar. She lifts him off his couch, walks him across the hall with his feet kicking, and drops him into Istrava's own seat, which Istrava has just vacated in a hurry.{/n}
"You wanted service," {n}she tells him.{/n} "Begin by keeping it warm."
{n}She picks the baton up off the floor where Rhez has let it roll, and looks at the blood on it, and at Rhez.{/n}
"That arm cost me twenty years and three dead masters," {n}she says, to the whole room.{/n} "I'll remember who opened it." {n}The snouted guest, in Istrava's chair, begins very quietly to cry.{/n} "Rhez. Don't die. It would be so inconvenient." {n}Rhez, white to the lips, tells her lady where she can put the inconvenience. Nocticula laughs, delighted, and looks up at your rail.{/n}''',
      c('"Rhez is cut. Make someone pay for it."', "gallery", flags=f("lodge_mark_ended", "lodge_rhez_hurt"))),
    n("announcement", "Nocticula", '''{n}Istrava rises on her coils to make her welcome. Before she can open her mouth the musicians strike up, and a thin tenor steps forward with a card in his hand, and reads it out in a voice that fills the hall.
It is Istrava's own invitation. You know, because you wrote it. It is in her hand, and her seal is on it, and it announces, in her own flowery phrases, that this evening's most honored quarry will be the lady of the house.
Nobody moves. Then somebody laughs, high and nervous, and stops.
Vhal comes down out of the bell chamber with the baton raised to strike the tenor, and Rhez, who has been standing behind the musicians in her green coat all evening holding a tray, steps into his way and asks him whether he means to hit a guest with the instrument of welcome. He hits her with his other hand instead. She lets the blow turn her, catches the baton against her shoulder, and puts him on the floor. The tenor, bless his spite, reads the card to the end.{/n}
"Her rules," {n}Nocticula says, with enormous pleasure.{/n} "The house has rules, and she wrote them, and she signed them. I adore people who write their own sentences. It saves me the effort." {n}She takes the baton from Rhez, who gives it up with a bow.{/n}
{n}Istrava is still standing on her coils at the head of the horseshoe. Her guests are looking at her. They are looking at her the way they looked at the attendants in the gallery when they came in: measuring, appetite stirring under the masks. She sees it. She sits down very slowly, and the moths in her hair throw themselves against their cages.{/n}
"Look at their faces, darling," {n}Nocticula says up to your rail.{/n} "They're doing sums. Which is more dangerous: the hostess, or the house rule? They've never had to ask before."''',
      c('"Let them keep doing sums. The gallery."', "gallery", flags=f("lodge_unmarked", "lodge_host_exposed"))),
    n("gallery", "Narrator", '''{n}The lower gallery is a long room behind a railing, lined with cabinets, lit low so that the guests above can see down into it and the people in it cannot easily see up. The three attendants are dressed as Nocticula's returned passengers: sea-stained clothes, a fake brass bell for Vessa, a boot for Halren. Their masks have hooks sewn into the ribbons. One of them is crying behind hers and cannot stop.
The service door at the far end opens a crack. Edris slips through it, in her yellow sleeve, and goes straight to the smallest of the three and takes her by the shoulders. That is Mera. She is wearing her mother's shoes, which are red, and a size too small, and she will not leave the cabinet where Istrava keeps the rest of the trophies: a comb, three rings, a child's wooden whistle that a grown servant kept from her girlhood. Edris cuts her mask's ribbon instead of pulling it, and hisses at her to come, and Mera shakes her head.
A guest has come down into the gallery to watch them. Not one of the drunk ones. He is lean and plain-dressed, with a collector's iron chain of office round his neck and a tally-stick in his belt, and he leans on the railing and smiles at the sisters as though they were a debt he had been waiting a long time to collect.{/n}
"That one," {n}Edris says, loud enough to carry, pointing up at him with the knife.{/n} "That's Suth. He buys the ones who run, and he collects on the ones who don't. He's got paper on both of us."
{n}Suth touches his brow to her, courteously.
Up in the bell chamber, Nocticula stands with the baton held loosely under the little brass bell. The hall below her has gone quiet. Istrava is watching her. The guests are watching her. Suth, in the gallery, has stopped smiling and is watching her too.
Then she lifts her eyes, past all of them, to your rail.{/n}''',
      c("[Meet her eyes across the hall.]", "held")),
    n("held", "Nocticula", '''{n}Afterwards the hall is a mess. Couches overturned, wine and worse on the tiles, a mask lying face up in a puddle and smiling at the ceiling. The musicians have hidden under their own platform. Somewhere in the gardens a guest is still screaming, more and more faintly, as though walking away.
Istrava lies on the floor of her own dining hall with her long tail tangled round a broken couch and Nocticula's bare foot on the back of her neck. Half the moth cages in her hair are crushed. The moths that got out are crawling on her face.
Nocticula has taken the hostess's chair. She sits with one leg crossed over the other and the baton across her knee, and you stand at her right, where she has put you, still masked.{/n}
"There," {n}she says.{/n} "Now we can talk like civilized people."
{n}Istrava talks. It pours out of her, the way it does when people realize the floor they are lying on is the last floor they will own. Her patrons; the names of the people who paid for every hunt this season and the last; the house, the gardens, the gold in her strongbox, the list of every servant she ever rented and to whom. She will give all of it. She will give anything. She knows things about other houses. She knows things about the Ten Thousand Delights. She has a cousin—{/n}
"Names, sweetheart," {n}Nocticula says.{/n} "All of them. Sing it like you mean it."
{n}She reaches down without looking and picks a moth off Istrava's cheek, and eats it, slowly, in front of everyone who is left. Istrava stops talking. Nocticula licks the powder off her fingers.{/n}
"You hunted under my protection," {n}she says, to Istrava, gently.{/n} "You took my name off the door and used it to make your guests feel safe while they ate people I'd never been asked about. That's a kind of theft I don't have a word for, because nobody ever tried it often enough to need one." {n}She lifts her foot. Istrava does not dare move.{/n} "And now you want to sell me my own city back, a piece at a time, and keep your skin."
{n}She looks up at you. Behind the black silk her eyes are bright and hungry and perfectly calm.{/n}
"What do I give her for it, darling?"''',
      c('"Take the list from her mouth. Promise nothing."', flags=f("lodge_hunt_ended"))),
], "lodge_method_ready")

s("closed_gallery", "The price of keeping a door shut", [
    n("start", "Narrator", '''{n}Rhez's account is short. She wants the name of the guest who followed Mera, enough guards to make his first retaliation expensive, and a replacement for the coat she tore at the stair. She has declined an invitation to dine with Nocticula while the household is still looking for people to blame.
Nocticula reads that last sentence twice.{/n}
"She suspects dinner would become another report."
"Would it?"
"Probably. I shall buy the coat."
{n}The guests have begun telling different versions of the evening. In one, Nocticula rescued servants out of sudden tenderness. In another, she staged the entire performance to take Istrava's house. The guest who pursued Mera calls himself an injured spectator.
His name is Suth. He maintains a small company of collectors who recover people as readily as objects. Nocticula has forbidden him to approach the escaped attendants while she examines the complaint. He has obeyed so far.
Istrava's remaining servants have closed the gallery. They will not clear the trophies from the floor until they know whom the possessions will belong to afterward. Their mistress has threatened to replace them. There are not enough willing replacements waiting at her door.{/n}
"They have found an inconvenience she cannot eat," {n}you say.{/n}
"She can eat the servants. She cannot make the others mistake that for a recommendation. For the moment, she still wants a functioning house."
{n}Nocticula sets three objects between you: the copied mask, a key sent by the service-yard guard and a strip torn from Rhez's coat.
She asks which of them you think Istrava most regrets losing.{/n}''',
      c('[Find the threat Istrava cannot dismiss without losing her guests. Diplomacy, DC 35.]', check=dict(Skill="CheckDiplomacy", DC=35, Success="audience", Failure="misjudge", CommanderOnly=True)),
      c('"Let the servants name their possessions before another owner claims the house."', "owners", requires=f("lodge_rescue")),
      c('"Take her remaining guests as the audience for her surrender."', "seizure", requires=f("lodge_conquest"))),
    n("audience", "Nocticula", '''{n}You choose the mask. Not because it frightened the attendants, but because it allowed the guests to pretend that somebody else had decided whom they might hurt.
Istrava sold them that permission. When the marking failed to protect their entertainment, she asked them to rely on her version of events instead. Suth's complaint is therefore a test: will she still supply the story they paid to inhabit?{/n}
"Let her answer it before the people who purchased the same promise," {n}you say.{/n} "If she declares that a fleeing servant attacked a spectator, every patron learns that her house cannot distinguish the hunter from the quarry."
"And if she admits the hunt?"
"She must say whose protection she expected the guests to disregard."
{n}Nocticula turns the mask over. Its broken ribbon falls across her wrist.{/n}
"You have made her audience useful to me. I had been considering how much of it I could afford to remove."
"You can still dislike them."
"I shall make an effort."
{n}She sends the summons as a hearing about the hostess's hospitality, with the escaped attendants spoken for by Edris from another room; Nocticula has no intention of letting Istrava look at her property again. Edris accepts that role from another room, through a messenger she knows. The trap uses Istrava's promises against her and gives the servants time to empty the gallery before the guests understand what is being decided.{/n}''', c('[Make the invited audience hear what its hostess actually promised.]', "offer", flags=f("lodge_audience_turned"))),
    n("misjudge", "Nocticula", '''{n}You choose the key and argue that Istrava cannot afford to lose the house. Nocticula asks what you would do if the lamia burned it.
You begin answering that her guests would resent losing their possessions, then stop. Their resentment would fall on the people accused of making the house unsafe. Istrava could preserve the story by destroying the place where it might be contradicted.{/n}
"She is capable of preferring a splendid loss to a visible surrender," {n}Nocticula says.{/n} "I find that annoying chiefly because I understand it."
{n}Nocticula produces the last report received before this meeting. Istrava has already ordered two wagons brought to the gallery. She may intend to remove its contents; she may intend to destroy them. Your argument supplies no quiet pressure she can be trusted to accept before the wagons leave.
Nocticula therefore chooses an overt order for guards to stop them in the yard. The servants are to remain outside the locked gallery while their possessions are counted under guard. It is a rougher intervention, and it will tell Istrava exactly which door Nocticula is prepared to seize.{/n}
"We can recover what remains," {n}she says.{/n} "We have lost the pleasure of letting her discover why she should surrender it."
"Then claim the interference. Do not let her blame the attendants for your soldiers."
{n}Nocticula writes her own name beneath the order. She does not invite you to share the signature merely to make the correction less embarrassing.{/n}''', c('[Own the overt intervention and guard the possessions still in the yard.]', "offer", flags=f("lodge_pressure_failed"))),
    n("owners", "Nocticula", '''"Some of them will claim things which never belonged to them."
"Then ask what they can describe before you open the cabinet."
{n}You set the strip from Rhez's coat beside the key. Istrava knows the value of the trophies. Their owners know the repairs, the stains, the contents of folded letters. The distinction will not settle every claim, but it makes a useful first question.
Nocticula sends a clerk and enough guards to keep the clerk from becoming another possession. The attendants can describe an object privately before it is brought out. Objects whose ownership remains disputed go into a sealed chest, not into the clerk's pocket.
Nocticula keeps the cabinet itself. It is lacquered and old and it was Istrava's, and she likes the idea of the lamia knowing exactly where it stands.{/n}
"You have made a remarkably small conquest," {n}Nocticula says.{/n}
"Small enough that the people concerned may recognize it."
"And large enough that Istrava will resent every missing comb. There is a certain precision to it."
{n}Edris agrees to identify what she remembers. Mera will not return. Nocticula shrugs at that: a witness who will not come is a witness nobody else can buy either.
She sends the clerk without her.{/n}''', c('[Return identified possessions and keep disputed claims out of the hostess\'s hands.]', "offer", flags=f("lodge_possessions_returned"))),
    n("seizure", "Nocticula", '''"You would like them to know whose company now makes a room dangerous."
"I would like them to stop mistaking your patience for an invitation."
{n}She accepts the distinction with a slight inclination of her head, though you can see she has not surrendered the less flattering interpretation.
The summons offers Istrava a choice. She can surrender the hunting apparatus, its guest list and the lower gallery under Nocticula's authority, or face an inspection of every person presently confined in her house. The second choice would expose obligations she has concealed from several patrons.
You have chosen pressure rather than a purchased apology. It may secure the gallery quickly. It also gives Nocticula a foothold in a house she did not own yesterday.{/n}
"The attendants should hear that before they celebrate," {n}you say.{/n}
"I am not concealing my name above the door."
"A new name can look like an exit until someone tries to use it."
{n}Nocticula's expression cools. She studies you as though deciding whether the warning was meant for her or for the person you would become beside her.{/n}
"Then they may leave. I want the position, the guest list and the example. I do not need frightened cleaners to complete the triumph."
"Put that in the order."
"You are becoming less decorative with practice."
{n}She adds the sentence. The joke does not soften how carefully she watches you read it.{/n}''', c('[Take the gallery and its political advantage while allowing the attendants to depart.]', "offer", flags=f("lodge_gallery_seized"))),
    n("offer", "Nocticula", '''{n}Istrava sends a private answer before the next public move. She offers Suth as the author of the hunt. She will testify that he demanded the attendants, provided she keeps her house and the matter ends with him.
She also offers one of the gold cages from her hair. Inside it is a moth whose wings have been painted with a map. The map allegedly leads to a hidden store belonging to a former patron.
Nocticula places the cage on the table. The moth remains still.{/n}
"A gift for me," {n}she says.{/n} "A culprit for you. She has been listening poorly to whichever story she heard about us."
"Is the map real?"
"Possibly. She has not said whether its owner still visits the store. I admire an apology which finds room for an ambush."
{n}You ask whether Nocticula intends to accept the cage. She answers that accepting an object is not the same as accepting its explanation. She has already ordered the moth fed and the paint examined without unfolding its wings by force.
There is something unexpectedly intimate about watching her refuse a beautiful thing's advertised use. Then she asks how much Istrava would pay to learn whether it worked, and the moment becomes recognizably hers again.{/n}
"Suth did pursue Mera," {n}you say.{/n} "He is not innocent because he is convenient."
"Nor is Istrava absolved because her guest was enthusiastic. We may take the evidence without purchasing the conclusion."
{n}She slides the offer to you. The final line asks that the Commander be told who supplied the decisive information.
Nocticula has not disclosed your identity as her adviser if you kept it private. Istrava is speculating about a famous ally whose involvement she hopes to provoke. If you claimed public credit, she is appealing to the name you already chose to give the affair. Either way, the invitation remains unanswered.
The choice now is how much access an enemy can buy by delivering a worse one.{/n}''',
      c('"Take her evidence. Give her no private access to either of us."', "end", flags=f("lodge_offer_bounded")),
      c('"Let her think the offer interested us. Make her name the other patrons before we answer."', "end", flags=f("lodge_offer_bait"))),
    n("end", "Nocticula", '''"I will send the answer in my own name. Your choice about public credit has not become permission to write every new threat beneath it."
{n}She closes the cage's small door and places it beyond the papers. The moth begins to move. Its painted wings make the supposed treasure flicker in and out of existence.
She takes three replies from beneath the cage. Edris has asked when she can leave. Rhez's coat is ruined. Istrava wants Suth's name printed above her own.
Nocticula signs Edris's passage order, adds a coat to Rhez's payment, and holds Istrava's reply to the lamp.{/n}
"She may keep her scapegoat. I am keeping the guest list."
{n}The burning paper lights her mouth. She catches your hand before you can gather the scattered reports.{/n}
"Leave them. The next threat can wait until I wake you."''', c('[Let the chosen pressure and the reply to Istrava take effect.]', flags=f("lodge_answer_sent"))),
], "lodge_hunt_ended")

s("unborrowed_evening", "An evening she did not borrow", [
    n("start", "Narrator", '''{n}This time she does not bother with a stair or a mask. You close your eyes in Drezen and open them in a high room in her palace, at a window, with the whole of Alushinyrra lying below you on fire.
It is not burning. It only looks that way at night: the Middle City in its terraces of red lamps, the Fleshmarkets glowing like a brazier, the black canals between them catching the light and throwing it back. Somewhere down there is a hunting lodge with its doors kicked in. From here you cannot tell which light it is.
Nocticula is sitting in the window. She has not changed since the hunt. There is still dried blood at the hem of her black gown that is not hers, and a smear of moth powder, gold and grey, along one cheekbone. She is cutting a pear on the sill with a plain kitchen knife, and she is eating the slices off the blade.{/n}
"I'm hungry," {n}she says, without looking round.{/n} "A hunt does that. It always has. Mortals think it's the blood. It's the running. Everyone running at once, in the dark, and only one of them going to be caught, and none of them knowing which."
{n}She holds the pear and the knife out to you, one in each hand.{/n}
"Peel it. I want to watch your hands do something careful after tonight."
{n}You take them. The pear is cold, as if it has come out of a well, and the knife is sharper than it looks. She watches your hands the whole time, the way she watched the bell chamber, and when the peel comes away in one long curl she takes it from your fingers and eats that too.{/n}
{n}Below the window a procession is crossing the nearest bridge: lanterns, a curtained litter, a line of slaves on a chain shuffling behind it. She points at it with her chin.{/n}
"One of Istrava's guests. Going home. He thinks he got out of that garden because he's clever." {n}She bites a slice off the blade.{/n} "He got out because I left a gate open for him, so that he'd go home and tell everyone on his street what he saw. By morning the whole Middle City will know whose garden it was. Dead guests don't gossip. Frightened ones never stop."
"And Istrava?"
"In her own cellar, with Rhez sitting on the door eating an apple. I'll go and look at her tomorrow night. I want her to have one whole day to think about what I'm going to do to her, and I haven't decided, and she knows that too." {n}She licks pear juice from her thumb.{/n} "Most of them break on the thinking, darling. The chains are only for decoration."
"You found her," {n}she says.{/n} "Or you chose who'd be found, which is better. Do you know how long it has been since anybody gave me a name for a bell? Nobody gives me anything. They pay me. It's not the same." {n}She leans back against the window frame and puts her bare feet up in your lap, as if you were furniture she had bought for the purpose.{/n} "Sit. No, closer. The knife stays on the sill. I like to see it there while I decide."
"Decide what?"
"Whether I'm going to be patient." {n}She smiles. It is not a reassuring smile.{/n} "I was patient all evening. I let her talk. I'm tired of it."''',
      c('[Sit beside her. Let her have the night.]', "close", flags=f("lodge_evening_close")),
      c('"Talk to me first. Tell me what you see from this window."', "talk", flags=f("lodge_evening_talk")),
      c('"Not tonight. Send me back to Drezen."', "leave")),
    n("close", "Nocticula", '''{n}You sit where she has decided you will sit, with her feet in your lap and the city burning at your back. She takes the pear out of your hand and bites it, and then she takes your jaw in the same sticky hand and kisses you, and her mouth tastes of pear and of something under it, metallic, from the gardens.
She does not let the kiss end when you would end it. She ends it when she likes, and pulls back an inch, and looks at you from very close.{/n}
"There," {n}she says.{/n} "That's what I wanted in her hall, with my foot on her neck. I thought about it the whole time she was begging." {n}Her thumb moves along your lower lip, wiping off the juice, not gently.{/n} "Don't look shocked. You were watching through my eyes. You know exactly what I was thinking."
{n}You do. That is the uncomfortable part.
The knife lies on the sill beside her hip, where she can reach it and you cannot. She sees you notice, and is pleased.{/n}
"Now," {n}she says.{/n} "You can ask me what I was hoping you'd ask. Or you can stop talking."''',
      c('"Why here? Why this window, and not your bed?"', "want")),
    n("talk", "Nocticula", '''{n}She looks at you for a long moment, as if deciding whether to be insulted. Then she takes her feet out of your lap, turns on the sill, and looks out.{/n}
"Everything," {n}she says.{/n} "I see everything from this window. That's why I took it."
{n}She points with the knife. The tower you are in, she tells you, belonged to somebody else once, a long time ago. A demon of some importance, who liked the view, and liked her, and had her brought up here to look at it with him. She does not remember his name. She remembers that he talked through the whole evening about what he owned, pointing at it, and that she let him, and that when he finally took her to bed she killed him in it, and then she came back to this window, alone, and looked at the city, and decided she wanted all of it.{/n}
"It took longer than the evening," {n}she says.{/n} "Not much longer. Most of the people who owned those lights died in beds. The rest died in worse places. I built the islands on what was left of them." {n}She looks at you sideways.{/n} "Don't make that face. You asked what I see. I see everything I took."
"And tonight?"
"Tonight I took one more house, and watched a hostess learn whose hunt it was in a garden she thought was hers, and someone I like stood at a rail and decided it." {n}She cuts the last of the pear in two and gives you half.{/n} "That's a good night, in Alushinyrra. You should be flattered I shared it."''',
      c('"Why bring me up here, then?"', "want")),
    n("leave", "Nocticula", '''{n}She stops chewing. For a moment the only sound in the room is the noise of the city coming up through the window, music and screaming and bells, the ordinary noise of Alushinyrra at night.
Then she takes her feet out of your lap and puts them back on the floor, one at a time, very deliberately.{/n}
"Not tonight," {n}she repeats.{/n} "After a hunt. After I gave you my eyes. You stood in my city and chose who'd be torn apart, and you enjoyed it; I know you did, I was inside your head. And now you'd like to go home to your cot." {n}She laughs, and it is genuinely amused, which is worse than if it were angry.{/n} "Oh, darling. The work isn't the part you're afraid of, is it? It never is, with your sort."
{n}She leans close, close enough that you can smell the gardens on her: crushed leaves, spilled wine, a stranger's blood gone brown at her hem.{/n} "You're afraid of the part where you lie here afterwards and know you liked both. The hunt and me. The same night, with the same hands." {n}She taps the flat of the knife against your knuckles, once, not quite hard enough to cut.{/n} "Get used to it. I did, a very long time ago, and look how well I've done."
"The work goes on. I'm not walking away from the lodge."
"I know you're not. I'd have you brought back if you tried." {n}She picks the knife up off the sill and cleans it on the hem of her gown, slowly, both sides.{/n} "I keep a list of nights owed. It's a very short list; most people don't live long enough to be on it. You're on it now. I'll collect when it suits me, and you won't be asked." {n}She sets the knife down.{/n} "Go on, then. I'll send for Laulieh. She's never once told me not tonight."
{n}She lifts two fingers. Your cot in Drezen is suddenly very hard, and very cold, and you can still taste the pear.{/n}''',
      c('[Wake in Drezen. The work goes on; the night is owed.]', flags=f("lodge_evening_finished", "lodge_evening_declined"))),
    n("want", "Nocticula", '''"Because up here nobody in that city knows what I'll do next. Not Shamira, not my brother, not the dealers in the Fleshmarket who bet on my moods." {n}She turns the knife on the sill so that the lamplight runs along it.{/n} "Everything down there I took from somebody. You I only borrow, a night at a time, out of your cot. I want to see what you do with the nights."
{n}She sits up. Her eyes, without the black silk, are the eyes you looked out of in the garden: very bright, very patient, entirely without pity.{/n}
"You asked me nothing all night. You chose. Now I'm going to ask." {n}She points the knife at you, lightly, the tip just touching your breastbone.{/n} "What do you want, Commander? When there's no crusade watching and nobody kneeling. Not what you're owed. What you want. And which of your wants do you ruin for yourself, because you're afraid of what it would make you?"''',
      c('"I keep looking for the next danger. Sometimes I bring it into rooms where it was not invited."', "honest", flags=f("lodge_vigilance_admitted")),
      c('"I enjoy being necessary. I have called it duty when appetite would have been more honest."', "honest", flags=f("lodge_appetite_admitted")),
      c('"Small things. A meal while it is still hot. A voice without a report behind it. Enough sleep that waking is not an argument."', "want_small", flags=f("lodge_vigilance_admitted")),
      c('"Power. More of it than I have, and yours to measure it against."', "want_power", flags=f("lodge_appetite_admitted")),
      c('"The moment before the knife comes out. I have never found anything to match it."', "want_danger", flags=f("lodge_appetite_admitted")),
      c('"You. Here. With the knife put down."', "want_pleasure", flags=f("lodge_appetite_admitted"))),
    n("want_small", "Nocticula", '''"How very mortal." {n}She says it the way another woman might say how very rare, and eats the slice she has cut.{/n} "A hot meal. I've had kings poisoned in the middle of theirs, and you want one. I could give you every one of those things tonight in a dream, finished, never cold." {n}She does not. She watches you understand that she has chosen not to.{/n} "No. You'd stop wanting them, and then what would I hold over you?"''',
      c("Continue", "honest")),
    n("want_power", "Nocticula", '''{n}Her eyes brighten, the way a cat's do at a movement in the grass.{/n} "At last, an appetite with teeth. Measure it against mine, then, and discover how short your ruler is." {n}She taps the flat of the knife against your knee, once.{/n} "Most mortals who want power want the chair. The clever ones want the person who gives the chairs away. I haven't decided which you are. Either way, I'll enjoy watching you try."''',
      c("Continue", "honest")),
    n("want_danger", "Nocticula", '''{n}She turns the knife so the lamplight runs along the edge, and lays it on the sill between you, point toward your hand.{/n} "Then you've come to the right window." {n}She does not pick it up again.{/n} "I've killed people for sitting where you're sitting. I may yet kill you for it. And you're enjoying this more than the pear." {n}Her smile is slow.{/n} "So am I. How inconvenient for us both."''',
      c("Continue", "honest")),
    n("want_pleasure", "Nocticula", '''"Put down?" {n}She looks at the knife on the sill beside her hip, and back at you.{/n} "It's on the sill, where I can reach it. That's as down as it goes." {n}Her foot finds your thigh and stays there.{/n} "You ask for so little, for a Commander. I'll have to teach you to be greedier. Not all at once. I want to see how long you can bear to want it."''',
      c("Continue", "honest")),
    n("honest", "Nocticula", '''{n}She cuts the last slice of pear and holds it against your lower lip. When you reach for it with your mouth she draws it back and eats it herself.{/n}
"That's a better confession than most," {n}she says.{/n} "It hasn't cost you anything yet, which is why you could say it. I'll make it cost something later. I'm good at that."
{n}She turns back to the window. Below, the city goes on burning. A bell is ringing somewhere toward the Fleshmarkets, a big one, for a sale.{/n}
"Istrava asked me tonight, while she was begging, why I care what one lamia does in one garden. It's a reasonable question. I have a thousand Istravas." {n}She is quiet for a while.{/n} "The answer is that she did it with my name. She made her guests feel safe by telling them I was watching over the house. I was. I was watching her steal from me, and enjoying it, and waiting for the right evening." {n}She glances at you.{/n} "And then you came, and it was the right evening."
{n}It is the nearest she has come to saying anything kind. She leaves it there, at the window, with her face turned away from you so that you only see the side of it, gold with moth powder. Then she turns back, and it is gone, and she is smiling.{/n}
"Don't make anything of that," {n}she says.{/n} "Go home. I'll send for you when the house is ready."''',
      c('[Watch the city burn with her until the dream lets go.]', flags=f("lodge_evening_finished"))),
], "lodge_answer_sent")

s("bell_without_master", "A bell without a master", [
    n("start", "Narrator", '''{n}The next night she takes you back to the lodge.
It is empty now, or nearly. The candles are out. The couches in the dining hall have been righted and stripped, and someone has scrubbed the tiles, not well; in the light of the lamp Nocticula carries you can see where the scrubbing gave up. The garden doors are boarded. The smell of musk is still in the walls.
She walks it the way a woman walks a house she has just bought: slowly, touching things, opening cupboards to see how deep they go. She runs a finger along the back of Istrava's couch and looks at the dust on it and wipes it on the wall. She tries the bell chamber stair and finds the third step creaks, and goes up and down it twice to be sure.
The bell itself lies on the floor of the hall, where it fell. A little brass thing, no bigger than a fist, dented on one side. Nocticula nudges it with her bare toe, and it rolls, and gives a small flat note.{/n}
"What does one do with a hunting lodge?" {n}she asks you.{/n} "Hunt, darling. Obviously. The question is who."
{n}Below your feet, through the floor, something knocks: slow, heavy, irregular, like a tail striking stone.
Istrava is in her own cellar. Rhez put her there last night and has been sitting on the cellar door since, with her coat over her shoulders, eating an apple. When Nocticula comes past she gets up and opens it without being told, and the smell that comes up is wine and damp and lamia. In the dark at the bottom of the stair the hostess of the house lies chained to her own racks by the throat and the wrists and the root of the tail, and her hair is full of empty cages.{/n}
"She hasn't stopped talking," {n}Rhez says.{/n} "I put a cork in her for an hour. She talked round it."
"She'll stop when I'm finished with her," {n}Nocticula says.{/n} "And the guests?"
"The ones who are left? Upstairs. In the long room. Still drinking." {n}Rhez shrugs.{/n} "They think they're your guests now. Nobody told them otherwise."
{n}Nocticula smiles at that, and closes the cellar door on the knocking, and turns to you with the lamp held up so that she can see your face.{/n}''',
      c('"What did her list give you?"', "bounded", requires=f("lodge_offer_bounded")),
      c('"Did she sing every name before she understood she\'d bought nothing?"', "bait", requires=f("lodge_offer_bait"))),
    n("bounded", "Nocticula", '''"Everything she had," {n}Nocticula says.{/n} "Which is what one gets, promising nothing. People give much more when they're not sure of the price."
{n}She tells you what the list was worth, ticking it off on her fingers like a girl counting presents. Eleven patrons who paid for this season's hunts, and where they sleep. Four other houses that run the same game under her protection, smaller and quieter, in the Ten Thousand Delights. A Fleshmarket dealer who rented Istrava her quarry by the night and took them back afterwards in whatever condition they were in.{/n}
"I've visited two of the patrons already, this afternoon," {n}she says.{/n} "One of them is in the cellar now, beside her; I thought she'd like the company. The other wasn't at home, so I took his house instead. I'm going to have so many houses." {n}She sounds delighted.{/n} "The dealer I'm saving. He'll keep. Dealers always think they can sell their way out, and I want to hear what he offers."
"And Istrava? What does she think she bought?"
"Nothing. I told her nothing, and she believed me, which is the only clever thing she's done all year." {n}She swings the lamp toward the cellar door.{/n} "She keeps asking me what I'm going to do with her. I keep telling her I haven't decided. It's true. I like to watch her hope."''',
      c('"Then decide what the house is for."', "judgment")),
    n("bait", "Nocticula", '''"Every one," {n}Nocticula says, with enormous satisfaction.{/n} "Every patron, every house, every dealer who ever rented her a body for the night. She sang it like a canary. She thought each name was buying her another hour, and so it was, in a way. She just didn't know how few hours there were."
{n}She tells you about the moment Istrava understood. It was near the end, after the last name. Istrava had stopped, and waited, and looked up from the floor at the Lady in Shadow sitting in her chair, and asked what she had bought. And Nocticula had told her: you, darling, have bought the right to know that you told me everything. Nobody else in the city will ever be able to say that.{/n}
"Her face," {n}Nocticula says. She closes her eyes, remembering it, and smiles.{/n} "You gave me that. You said: let her think she's buying her life. I'll keep that face in my collection forever."
"Has the story got out?"
"Of course it has. Half the Middle City knows Istrava tried to buy herself from me and was robbed in the process. Several of them have written to say how shocked they are that I'd bargain with such a creature." {n}She laughs.{/n} "They're terrified I'll bargain with them. Good. Let them write. Let them wonder what I'd charge."''',
      c('"Then decide what the house is for."', "judgment")),
    n("judgment", "Nocticula", '''{n}She sets the lamp down on Istrava's couch and walks out into the middle of the hall, where the bell lies, and turns round slowly, looking up at the bell chamber, the gallery, the boarded garden doors.{/n}
"I can think of three things to do with it," {n}she says.{/n} "I can burn it. Tonight, with the guests upstairs, still drunk, still thinking they're mine. Leave the doors open; it'll draw better. The whole Middle City will see it from the canals, and everyone who ever paid to hunt in a house under my protection will know exactly what the smoke means."
{n}She nudges the bell with her toe again. It rolls.{/n}
"Or I can keep it. Hunt here myself. It's a good house for it; she was a fool but she had taste. I'd keep her in the cellar for the season and let her out on the first night, and see how well she knows her own gardens when she's the one running." {n}Her eyes glitter.{/n} "Or I give it to Rhez. On a leash. Rhez has never been given anything in her life. I want to see whether she bites."
{n}Rhez, in the doorway with her apple, says nothing at all. She has stopped chewing.{/n}
"You decide," {n}Nocticula says to you.{/n} "I'll enjoy any of them. That's the luxury of owning things."''',
      c('"Burn it. Guests inside."', "close", flags=f("lodge_closed_house")),
      c('"Keep it. Hunt here yourself."', "keep", flags=f("lodge_kept_house"))),
    n("close", "Nocticula", '''"Oh, good," {n}she says, softly.{/n}
{n}She does it herself. She goes up the stair to the long room, where you can hear the guests laughing, and opens the door and says something, and the laughing gets louder. Then she comes back down and locks the door behind her with Istrava's own key, and drops the key into the bell's mouth, and touches the wall.
The fire starts in the walls, not on them. It comes up through the plaster like a blush. In a few breaths the whole upper floor is roaring, and the laughing has turned into something else, and fists are hammering on the locked door, and then not.
At the last moment she goes down into the cellar, alone, and comes back up the stair dragging Istrava by the chain round her throat. The hostess is coughing, sooty, her tail thrashing on the steps. Nocticula hauls her out into the yard like a sack and drops her on the gravel.{/n}
"For the collection," {n}she says to you, a little breathless, delighted.{/n} "I couldn't let her miss it. Look, Istrava. Look at your house."
{n}Istrava looks. Behind you the lodge burns, all of it, the gallery and the cabinets and the bell chamber, and the light of it goes up over the old pleasure garden and out across the canals, and down in the Middle City people come out onto their roofs to watch.
Nocticula stands in the yard with the fire on her face and her hand wound in the chain, and laughs, long and hard, the way she laughed in the throne hall when the court laughed with her. There is nobody here to laugh with her now except Rhez. Rhez does.{/n}''',
      c('[Watch it burn.]', "last", flags=f("lodge_payment_advanced"))),
    n("keep", "Nocticula", '''"Yes," {n}she says, and you can hear that it is the answer she wanted.{/n}
{n}She goes down into the cellar, and you go with her, and she crouches in front of Istrava in the wet dark and takes her chin in one hand and turns her face up to the lamp.{/n}
"You're staying," {n}she tells her.{/n} "Isn't that nice? It's your house. You know every hedge in that garden, every dry fountain, every hole in the wall. I'm going to open the house again at the end of the month, with new guests, and on the first night of the season I'm going to take the chains off you and ring that little bell, and they're going to find out how well you know it." {n}She pats Istrava's cheek.{/n} "If you're very clever, you'll last till dawn. If you last till dawn, I'll put you back down here, and we'll do it again next season."
{n}Istrava says nothing. She has finally stopped talking.
Upstairs, Nocticula gives her orders. The guests in the long room are to be woken and thanked and sent home, all of them, with a gift each: an invitation to the opening of the season, in Istrava's hand, under Nocticula's seal. They will all come. Nobody refuses the Lady in Shadow's invitations, and it will be an excellent opportunity to see which of them were Istrava's friends.{/n}
"I'll keep the bell," {n}she says, picking it up off the floor and turning it in her fingers.{/n} "Dented. I like it dented. It'll remind her."''',
      c('[Leave Istrava in her cellar for the season.]', "last", flags=f("lodge_information_post"))),
    n("last", "Nocticula", '''{n}When you come out into the yard there is a man waiting there under guard.
It is Suth, the collector from the gallery. He has been kept somewhere overnight, and it shows: his plain coat is torn, there is blood dried in his beard, and both his hands are bound up in rags, because Rhez spent part of the night asking him questions about them. But he has his chain of office round his neck still, and his tally-stick in his belt, and when he sees Nocticula he goes down on one knee on the gravel, carefully, like a man who has knelt to a great many important people and knows exactly how low to go.{/n}
"Lady," {n}he says.{/n} "With respect. I'm a collector. Lawful. I've a hall in the Middle City and forty men and my paper's good in every court on the islands." {n}He nods toward the gate, where Edris and Mera stand with Rhez.{/n} "Those two cunts owe me forty silver apiece. Their mother sold them to Istrava's house on my credit. They carry my marks. Lawful debts, Lady. I'm only asking what's mine."
{n}Nocticula looks at him for a long moment. Then she looks at Rhez.{/n}
"Rhez," {n}she says,{/n} "he said 'owe'. In my house."
"I heard him, Lady."
"Lawful." {n}She tastes the word.{/n} "In my city. Say it again, Suth. Slowly. I want Rhez to hear it properly."
{n}Suth does not say it again. He has gone very pale above the beard. He is looking at you now, because you are the only one in the yard who has not yet said anything, and he has seen in the gallery who chose the name for the bell.{/n}
"Well, darling?" {n}Nocticula says.{/n} "What do I do with a man who collects in my city on paper I never signed?"''',
      c('"Send his hands to his collectors\' hall."', flags=f("lodge_judgment_finished"))),
], "lodge_evening_finished")

s("counterseal", "The name beneath the debt", [
    n("start", "Narrator", '''{n}The quay has acquired a desk with one short leg. Nocticula has folded a petition beneath it. Each time she sets down her pen, the desk rocks just enough to make her glance at the offending corner.
A letter lies open before her. Its seal shows a hand holding another hand by the wrist.{/n}
"You have received an appeal," {n}you say.{/n}
"I have received an invoice which has learned to plead. The distinction becomes clearer near the bottom."
{n}She turns the letter toward you. A broker named Tazren financed purchases for Istrava's household. He claims the departure of her attendants has deprived his clients of the labor against which those purchases were secured. Since Nocticula arranged the departure, he suggests the obligation has passed to her.
His list includes Mera. Beside her name is a charge for the shoes she recovered from the cabinet. He describes them as an advance made for her benefit.{/n}
"Her mother's shoes," {n}you say.{/n}
"An unusually personal loan."
"He knows what they were."
"Probably. He would like me to correct the description while accepting the debt. Then we may argue about the price of an object he never owned."
{n}The letter does not disclose the sisters' destination. It names their former rooms in the lodge, information any supplier might have obtained. Nocticula's messengers have been told to bring further correspondence to her clerk, without confirming where the women went.{/n}
"You could kill him."
"Certainly. His clients would auction the claim before his chair cooled. I want to know whose signature makes them believe it is worth bidding on."
{n}She lifts the desk with one hand and takes out the folded petition. The wobble stops while she holds it. With the other hand she offers you the damaged paper.{/n}
"He sent that yesterday. Read what he wanted before he learned to call it a debt."''', c('[Read the earlier petition against the invoice.]', "petition")),
    n("petition", "Narrator", '''{n}Yesterday Tazren requested permission to announce that his clients supplied Nocticula's new household. He offered favorable terms on furnishings and credit. The invitation was addressed to the household whether or not the lodge remained open.
At the bottom, in smaller writing, he promised to settle outstanding obligations attached to any persons entering her protection. A courteous service, the sentence calls it. Nocticula has drawn a line beneath those words.{/n}
"He offered to collect their debts for you."
"He offered to decide which debts existed. An industrious man."
"And when you did not answer?"
"He supplied a debt with my name on it. If I pay, he has a transaction to show the next frightened person. If I simply tell him I owe nothing, he can announce that I have abandoned the people whose escape produced the bill."
{n}You compare the dates. The invoice predates the letter offering to arrange the obligations. Tazren has altered one figure, but the impression of the old ink remains visible in the copy she supplies.
Nocticula waits while you notice it.{/n}
"You already saw that."
"Yes. I wanted to discover whether you would propose burning the letter before reading the useful part."
"I am fond of making a creditor explain himself before the fire."
"Then we may yet have a pleasant evening."
{n}The broker has enclosed a summary, not the original agreements. His own fees form the largest part of the supposed debt. A smaller sum was guaranteed by an unnamed patron of the lodge. That signature could identify someone who paid for the hunt and has not appeared in Istrava's account.
Nocticula wants the original. She has not sent for Mera to obtain it. The woman's denial would establish what she remembers; it would not reveal what the patron signed elsewhere.{/n}''', c('"He has given us a reason to demand the papers. Has he given us a way to get them?"', "price")),
    n("price", "Nocticula", '''"He will sell. He makes his living by arriving before the collector and leaving before the argument. When this is finished, I shall find him somewhere to arrive that he cannot leave."
{n}She puts two blank sheets on the desk. One is narrow enough for a public notice. The other has the broad margin of a purchase agreement.{/n}
"We can reject the transfer openly. Name the false charge, refuse to acknowledge his authority over my household, and warn anyone buying the claim that I intend to dispute it. He may keep the original. He will have fewer people eager to finance his interpretation."
"Or you can buy it."
"Buy the original schedule and the guarantor's obligation. Cancel the entries against the attendants. Keep the claim against the person who paid to make them quarry."
"He receives money for inventing part of the bill."
"Less than he hoped. More than you would enjoy. I would be purchasing evidence as well as an obligation."
{n}She touches the wide margin with her pen, leaving a dot of ink where a signature might begin.{/n}
"I would like to collect from that patron. I would also like Tazren to discover that separating his fees from the principal makes him much poorer. Those pleasures do not prove the purchase wise. They do make it attractive."
"And the people on his list?"
"Receive the canceled originals if I obtain them. Receive a warning and my public refusal if I do not. Neither answer requires them to return here and earn my interest by telling the story again."
{n}You look at the desk's short leg. Nocticula follows your glance and restores the folded petition beneath it.{/n}
"I know," {n}she says.{/n} "A ruler of my resources should possess better furniture."
"I was thinking you could fix it."
"I could. For the moment I enjoy knowing precisely which petition is supporting my work."
{n}She waits for your answer with the pen still in her hand. This time she has told you what she wants before offering the choice.{/n}''',
      c('"Deny it publicly. Make selling this claim dangerous. I will not help him establish a price for releasing people he never owned."', "deny", flags=f("lodge_debt_denied")),
      c('"Buy the original and strip out his inventions. Cancel the servants\' entries. Then let his patron discover who now holds the honest part of his debt."', "purchase", flags=f("lodge_debt_purchased"))),
    n("deny", "Nocticula", '''"You are leaving me with a useful suspicion and no signature."
"I am leaving him with a claim you have publicly challenged. He wanted your name to make it valuable. Give him your name."
{n}She looks at the narrow sheet again. Her pen moves before she answers.{/n}
"I can make that an unpleasant gift."
{n}The notice names the altered date and the false charge for the shoes. It does not print the sisters' present whereabouts or invite other creditors to send their accounts. It states that leaving Istrava's service transferred no obligation to Nocticula and grants no collector permission to seize the former attendants under her authority.
She stops before adding a threat against anyone who buys the paper.{/n}
"An extravagant threat is cheap to repeat. It becomes expensive the first time someone tests whether I can find him."
"Then promise the part you will do."
"I will publish the objections with every attempted sale brought to my attention. I will pay for the names of the buyers. That will make Tazren calculate the value of keeping his original."
{n}She signs. Her irritation has become concentration, without becoming agreement that this was her preferred use of the evening.{/n}
"If this costs me the patron's name, I shall remind you."
"If buying it would have taught him to send another invoice, I shall be unable to prove it."
"How refreshing. An argument which admits where its victory cannot be counted."''', c('[Send the public challenge and watch who still tries to buy the claim.]', "end")),
    n("purchase", "Nocticula", '''"At last. Someone who can dislike a practice without becoming incurious about its records."
"Read the price before you congratulate me. I want the canceled entries delivered to the people named in them. Not a promise that you will never collect."
{n}Her smile narrows. She draws the broad sheet toward herself.{/n}
"You think I would keep the option."
"You have explained several times how much you enjoy options."
"I have been unusually instructive."
{n}She writes the cancellation into the purchase. No attendant's obligation can be sold on or held as security. The patron's guarantee must be produced in its original form; an assertion that such a document once existed will earn Tazren nothing. A clerk is to compare the dates before payment, and another is to witness the canceled entries being separated from the remaining account.
The price is lower than the summary demands. Nocticula explains which invented fees she has removed with the pleased precision of someone describing a rival's failed entrance.{/n}
"He can refuse," {n}you say.{/n}
"Yes. Then I have the letter in which he offered to sell an original he now refuses to produce. We begin again from there."
{n}She leaves room beneath the offer for his answer. The purchase has not occurred merely because she wants its result.{/n}
"When I collect from the guarantor, you may find him quite pitiful."
"I will read what he agreed to buy."
"Do. I should dislike discovering that you found my appetite attractive only while I was discussing it."''', c('[Offer the limited purchase, conditional on verified originals and canceled servant claims.]', "end")),
    n("end", "Nocticula", '''{n}The copied seal remains on the desk after she puts away the papers. One hand holds another by the wrist, and the tiny cut between them has filled with dark wax.
You turn it toward her.{/n}
"An unfortunate emblem for a man hoping to conduct business with you."
"He believes it depicts assistance."
"Does he?"
"He believes his clients enjoy calling it that. The distinction has fed him for years."
{n}Nocticula takes the seal between finger and thumb. For a moment you expect her to crush it. Instead she puts it beside the order she will send when this meeting ends.
You have seen enough of her correspondence to recognize the gesture. She keeps the things she may want to contradict precisely.{/n}
"You made me state the part I intended to keep," {n}she says.{/n}
"You had already stated the part you wanted."
"Do not grow complacent. There are evenings when the distinction will matter more than this one."
{n}You tell her you expect to notice. She gives you a look in which pleasure and skepticism are equally evident.
When the desk disappears, its short leg leaves a crooked impression in the dust. She removes that too. The papers go last.{/n}''', c('[Await the broker\'s answer and the survivors\' departure report.]', flags=f("lodge_debt_answered"))),
], "lodge_judgment_finished")

s("no_applause", "No applause at the departure", [
    n("start", "Narrator", '''{n}Dawn, in so far as Alushinyrra has one: a thinning of the red over the Middle City, and a grey light coming up off the canals.
She has brought you to a gate. It is one of the old landward gates of the Middle City, a high black arch with the docks beyond it and the long road down to the water, and the night's traffic is coming in through it: carts of meat, a coffle of slaves on a chain, a drunk incubus singing. Just inside the arch there is a stone bench, and Nocticula is sitting on it with her legs crossed, eating cherries out of a paper twist and spitting the stones into the gutter.
Across the road, against the wall of a cookshop, stand Edris and Mera. They have a trunk between them, a small cheap one with a broken strap, and Mera is wearing her mother's red shoes. They are holding hands. They look the way people look when they have been told something very good and have not yet worked out what is wrong with it.{/n}
"I took my flower off them this morning," {n}Nocticula says.{/n} "Both of them. Stood them in front of me and took it off, like a collar. They're free." {n}She spits a stone.{/n} "Do you know what free means, in my city?"
"Tell me."
"It means nobody's. It means that anyone who catches them may keep them." {n}She holds out the twist of cherries to you.{/n} "Every dealer in the Fleshmarket knows their faces by now. Every collector. Every bored thing on the docks that likes the look of red shoes. I've given them the road, and the morning, and nothing else. Let's see how far a bird gets without a cage in Alushinyrra."
{n}Mera has noticed you. She is looking across the road at the Lady on the bench with an expression you cannot read: fear, certainly, and something sharper than fear.{/n}''',
      c('"There\'s still smoke on the hill."', "closed_account", requires=f("lodge_closed_house")),
      c('"And your new house? Did the season open?"', "kept_account", requires=f("lodge_kept_house"))),
    n("closed_account", "Nocticula", '''{n}She follows your look. Up on the hill above the old pleasure garden a thin column of smoke still stands against the grey, going straight up in the windless air.{/n}
"It burned all night," {n}she says, pleased.{/n} "I sat up and watched. The Middle City sat up with me; I could see them on the roofs. Three other houses closed their doors before morning without being asked. One of them sent me its bell in a box, with a very frightened letter." {n}She smiles.{/n} "I'm going to have a shelf of bells. Istrava's I keep by my bed. She has a cage in my gallery now, and every night I ring it once, and she flinches. It's a lovely sound."''',
      c('"And the collector?"', "debt_report")),
    n("kept_account", "Nocticula", '''"Last night." {n}She looks satisfied enough to purr.{/n} "New guests, new masks, the same old gardens. They all came; nobody refuses my invitations. I took the chains off her myself at midnight and rang her own little dented bell, and you should have seen her go."
"Did she last till dawn?"
"She lasted till the second fountain. They brought her back with a guest's teeth still in her tail, and I put her back in the cellar to heal for next time." {n}She eats a cherry.{/n} "Whoever holds the keys to that house, it's mine. That's the point of it. Every guest who came last night knows now what happens to a house that hunts on my name, and every one of them was too frightened to leave early." {n}She spits the stone.{/n} "Good business. Better sport."''',
      c('"And the collector?"', "debt_report")),
    n("debt_report", "Narrator", '''{n}At the name, Edris looks up sharply from across the road. Mera's hand tightens on her sister's. Nocticula sees both and is amused, and does not lower her voice at all when she answers.{/n}''',
      c('"Did his hands reach his hall?"', "debt_refused", requires=f("lodge_debt_denied")),
      c('"Is he collecting for you yet?"', "debt_bought", requires=f("lodge_debt_purchased"))),
    n("debt_refused", "Nocticula", '''"In a box. Rhez took them herself, and set them on his table in front of his forty men, and asked who was in charge now." {n}Nocticula spits a cherry stone into the gutter.{/n} "Nobody was. They've closed the hall. They're selling his paper in the Fleshmarket by the bale, very cheaply, and nobody is buying it, because nobody wants to be the next collector to say 'owe' in my city."
{n}Across the road Mera has heard every word. She is staring at Nocticula. Edris has one hand pressed flat over her own mouth.{/n}
"So there's no paper on them anywhere now," {n}Nocticula says.{/n} "Nobody's chasing them for a debt. They're simply free." {n}She smiles at the sisters, and waves her fingers at them.{/n} "Which is a different thing entirely."''',
      c('"How is Rhez\'s arm?"', "wound", requires=f("lodge_rhez_hurt")),
      c('"What does Rhez want next?"', "agent", requires=f("lodge_unmarked", "lodge_silent_bell")),
      c('"What does Rhez want next?"', "agent_announcement", requires=f("lodge_unmarked", "lodge_self_invitation"), forbids=f("lodge_silent_bell"))),
    n("debt_bought", "Nocticula", '''"He started this morning." {n}Nocticula tilts her head toward the far end of the road, where it goes down between the warehouses to the docks.{/n}
{n}You look. Down there, under a cookshop awning, a lean man in a plain coat is standing with half a dozen others round him, and his hands are bandaged, and he has a new chain of office round his neck. Even from here you can see that the badge on it is a black flower.{/n}
"He collects for me now," {n}she says.{/n} "His hall, his forty men, his lovely paper; all mine. I bought him for the price of his hands, and gave him the hands back. He's very grateful. You'd be surprised how hard a grateful man works." {n}She spits a stone.{/n} "And he does know those two. Their faces. Their mother. The street their aunt lives on. He knows them better than anyone in Alushinyrra."
{n}Across the road Edris has seen him too. She has gone very still.{/n}''',
      c('"How is Rhez\'s arm?"', "wound", requires=f("lodge_rhez_hurt")),
      c('"What does Rhez want next?"', "agent", requires=f("lodge_unmarked", "lodge_silent_bell")),
      c('"What does Rhez want next?"', "agent_announcement", requires=f("lodge_unmarked", "lodge_self_invitation"), forbids=f("lodge_silent_bell"))),
    n("wound", "Nocticula", '''"Healing. She can use the hand. She can't yet fasten the coat without swearing, which she does beautifully." {n}Nocticula looks pleased with Rhez, the way one is pleased with a good horse.{/n} "She came to me yesterday and asked for the man with the jeweled snout. The one who opened her arm. I'd kept him for her."
"What did she do with him?"
"Nothing yet. She's making him wait in a cell beside the one where Vhal is giving his evidence. Vhal gives it standing up, by the way, for as long as it takes; I thought that was fair, for a man who used to make the servants stand all night." {n}She eats a cherry.{/n} "When they've both finished, Rhez may decide which hand each of them leaves my city with. I thought she'd like to choose. You see, darling, I can be generous with the people who bleed for me."''',
      c('"Let Rhez collect. Then let\'s see your wager."', "credit")),
    n("agent", "Nocticula", '''"The next job." {n}Nocticula smiles.{/n} "She always wants the next job. She came to me last night with her coat on and asked what was after Istrava, and I told her nothing, yet, and she looked so disappointed that I almost found her someone to kill on the spot."
"Will you?"
"Of course. Something worthy of her. There's a dealer in the Fleshmarket who rented Istrava her quarry by the night. I've been saving him." {n}She spits a stone into the gutter.{/n} "Rhez is a knife I spent years sharpening. A knife you don't use goes dull, or goes looking for another hand. I don't let my knives go looking." {n}She glances at you.{/n} "Remember that, the next time you feel restless."''',
      c('"Give her the dealer. Then let\'s see your wager."', "credit")),
    n("credit", "Nocticula", '''{n}She settles back on the bench and wipes cherry juice off her fingers on your sleeve.{/n}
"You bet against your own hand, or with it, and you didn't even notice." {n}She sounds delighted with you.{/n} "Two nights ago, in that yard, you decided what Suth was. That decided everything. I knew how this morning would end the moment you said it. I only asked you to bet on yourself."
{n}She pulls a little iron key out of her bodice and drops it in your lap. It is warm.{/n}
"Istrava's strongbox. I had it carried up from her cellar before I burned or kept anything. If that was a win, it'll be in Drezen before you wake, and you can buy your crusade something shiny with a lamia's money." {n}She leans close.{/n} "If it wasn't, you owe me. Not gold. I don't want your gold. I'll collect at a time of my choosing, and you won't like the time."
{n}She kisses the corner of your mouth, quickly, and sits back to look at you.{/n}
"So. You've watched me hunt, and burn, and set two birds loose to see how far they get. You've helped with all of it. And you're still sitting on this bench." {n}Her eyes are very bright.{/n} "Tell me why."''',
      c('"I dislike what you can make sound reasonable. I also want you. I will have to keep answering both facts."', "answer", flags=f("lodge_desire_contested")),
      c('"I liked watching you take the house from her. I will not pretend that attraction belongs to someone less ambitious than I am."', "answer", flags=f("lodge_danger_desired"))),
    n("answer", "Nocticula", '''"Then don't tell me later that I hid which woman you were choosing."
{n}She stands. She does not sit back down beside you; she stands over you with the dawn wind pulling at her skirts and looks down at you as though you were a city she had been told she could not have. Then she sets one knee on the bench beside your thigh, takes your jaw in her hand, and turns your face up to hers.{/n}
"Both," {n}she says.{/n} "Good. Either one alone would have bored me by spring."
{n}She kisses you hard, in the open gate, in front of the meat carts and the coffle and the singing incubus, and lets you go only when she has decided to. A carter stares. She looks at him, once, and he finds something urgent to do with his mule.
Then she sits down beside you as if nothing had happened, and picks up the cherries again, and looks out through the arch at the road going down to the docks, where it is quite empty now.{/n}
"I'm going to show you my collection next," {n}she says.{/n} "Everything we've taken. You've earned a look at it."
"Our collection?"
{n}She turns her head and considers you, with a cherry halfway to her mouth.{/n}
"We'll see," {n}she says.{/n} "That depends on whether you can stand being seen holding it."''',
      c('[Let the gate and the morning go. Keep the woman on the bench.]', flags=f("lodge_consequences_finished"))),
], "lodge_debt_answered")
# Append after s() adds the existing withdrawal node; its saved position must survive.
SCENES[-1]["Nodes"].append(n("agent_announcement", "Nocticula", '''"The next job." {n}Nocticula smiles.{/n} "She always wants the next job. She came to me last night with her coat on and asked what was after Istrava. And the musicians who read out Istrava's own invitation in her own hall have come to me as well, all six of them, asking to be taken into my service, because they say nobody else in the Middle City will ever hire them again."
"Will you take them?"
"The tenor. He has a lovely voice and no sense at all of when to stop, which is exactly what I want in a herald. The rest I've sold." {n}She spits a cherry stone.{/n} "And Rhez gets a dealer in the Fleshmarket who rented Istrava her quarry by the night. I've been saving him for her. A knife you don't use goes dull, or goes looking for another hand. I don't let my knives go looking." {n}She glances at you.{/n} "Remember that, the next time you feel restless."''', c('"Give her the dealer. Then let\'s see your wager."', "credit"), portrait="Nocticula"))

s("what_she_keeps", "What she keeps", [
    n("start", "Narrator", '''{n}Her gallery is above the Harem of Ardent Dreams, in a long room under the roof with slatted floors, so that the music and the heat and the smell of the Harem come up through the boards. You can look down through the slats and see the couches below, and the bodies on them, and the succubi going between them with trays. Nobody below looks up. It is not done.
The gallery itself is lined with what she keeps.
She walks you through it the way a girl shows off a dollhouse, holding your hand, pulling you from one thing to the next before you have finished looking at the last. Here is a crown she took off a king who is still alive, somewhere, without it. Here is a jar with something in it that blinks. Here is a whole wall of masks, every one of them a face somebody once wore to her court and then could not take off. Here, newer, a row of little gold cages, each with a moth in it, beating against the bars. The moths are fresh. She has them changed every night.
Laulieh is lounging on a couch at the far end of the gallery where she is certainly not supposed to be, eating sugared almonds and admiring her own reflection in a polished shield. She waggles her fingers at you as you pass, and Nocticula ignores her magnificently.{/n}
"This," {n}Nocticula says, stopping at last in the middle of the gallery and spreading her arms,{/n} "is what I keep. Everything here was somebody's, once. Now it's mine." {n}She turns to you.{/n} "And this end of the room is what you helped me take. The harbor, the court, the lodge. Come and look."
{n}At the near end of the gallery, on a table of black wood, lies the brass lens from the cliff door.{/n}''',
      c('"The lens. Is the road still yours?"', "chart", requires=f("chart_intact")),
      c('"The lens is cracked."', "broken", requires=f("chart_lost")),
      c('"The door is shut. What did you keep of it?"', "limited", requires=f("chart_limited"))),
    n("chart", "Nocticula", '''"Of course it is." {n}She picks up the lens and holds it to her eye and looks at you through it, and laughs.{/n} "Whole. Not a scratch. And out on the coast there's a door in the cliff with my flower burning in it, and every captain who sails past at night can see it."
{n}She sets the lens down.{/n}
"Two of them have already come to me, asking to buy passage. One of them was the man who used to buy from Ilvara. He didn't recognize me. He thought I'd be grateful for the custom." {n}She smiles.{/n} "He's in the cells. His ship is mine. The other I let through, at three times what Ilvara charged, because she was polite, and I wanted to see whether the door would hold for a stranger." {n}Her eyes go to the window, toward the coast you cannot see.{/n} "It held. My road. Built on my old permission, opened by your stolen magician, and now it opens for whoever I like. A share of what comes through it is yours, darling. If you can stand being seen holding it."''',
      c('"Show me what became of Ilvara."', "disposition")),
    n("broken", "Nocticula", '''"Cracked right across." {n}She turns it in the light so that the crack throws a thin bright line onto the wall.{/n} "Rhez had it in her hand when the door shut. It's never worked since. The road's gone; the cliff is only a cliff."
{n}She does not sound sorry. She sounds interested, as if the crack were a new kind of jewel.{/n}
"Vessa is downstairs," {n}she says.{/n} "In the Harem. Her hand is splinted, and she'll never hold a bell with it again, and she knows exactly whose door it went into. She wears my flower on her collar now. The girls down there are terrified of her." {n}She sets the lens down with the crack facing you.{/n} "I lost a road. I gained a woman who put her own hand in a closing rock to save my property. I've made worse trades." {n}She glances at you.{/n} "You told me to hold the door narrow. I'll remember that it was you, every time I look at that crack. Don't worry; I don't mind remembering it."''',
      c('"Show me what became of Ilvara."', "disposition")),
    n("limited", "Nocticula", '''{n}She does not pick up the lens. Beside it on the table there is a shallow glass dish, and in the dish a little heap of black threads, brittle and coming apart, that was once a flower worked into an old sail.{/n}
"It fell to pieces in Rhez's pack when the door shut," {n}Nocticula says.{/n} "My old permission. Centuries old. Ilvara cut it off some ship I'd let pass and sewed it into her harbor, and when your count ran out, it simply gave up." {n}She touches the threads with one fingernail, and one of them breaks.{/n} "Nobody will ever open that door again. Including me. You made the price so small I couldn't keep the door afterwards."
"You agreed to it."
"I agreed to it. I didn't agree to like it." {n}She looks at you sideways.{/n} "I keep this dish to remind me that I paid. I always remember what I paid, and to whom. Most people find that alarming."''',
      c('"Show me what became of Ilvara."', "disposition")),
    n("disposition", "Narrator", '''{n}Beyond the lens there is an alcove in the gallery wall, lined with black velvet, the kind of alcove in which a better-run house would keep a statue. Nocticula leads you to it by the hand and stops in front of it.{/n}
"And the magician," {n}she says.{/n} "You haven't asked about her. You've been very good. I can see you wanting to."''',
      c('"Is she still burning?"', "confined", requires=f("ilvara_confined")),
      c('"Is she still working the door?"', "commissioned", requires=f("ilvara_commissioned")),
      c('"Who bought her?"', "exiled", requires=f("ilvara_exiled"))),
    n("confined", "Nocticula", '''"Every night." {n}The alcove is empty. Nocticula points down instead, through the slatted floor, to the far end of the Harem below.{/n}
{n}You look. Over the great bed at the end of the Harem, the one with the black silk hangings, a small brass lamp hangs on a chain, and in the lamp there is a light that is not quite a flame. If you look at it long enough, the light has a shape. The shape is a woman, very small, standing in the glass with her palms pressed against it, watching the bed.{/n}
"She's been watching for weeks," {n}Nocticula says.{/n} "Everything that happens on that bed. Everything. She can't close her eyes; lamps don't have eyelids. I've been down there twice myself, just to give her something to look at." {n}She sounds pleased.{/n} "The Harem thinks she's the most beautiful lamp in the islands. Two people have tried to buy her. One of them was a magician."
"Did you sell?"
"Darling. I never sell anything that's still suffering usefully."''',
      c('"And what do you believe we learned about each other?"', "ambition")),
    n("commissioned", "Nocticula", '''"Day and night." {n}The alcove is not empty. In it, on a black velvet cushion, lies a length of iron chain with a broken link at one end, as if somebody had kept a souvenir.{/n}
"She's on the coast," {n}Nocticula says.{/n} "Collared to the rock, beside her door, with my flower burned on the collar. She opens it when I want it open and shuts it when I'm bored, and every time it bites, it bites her first." {n}She lifts the chain and lets it run through her fingers.{/n} "The guards send me word when it bites. It's bitten her four times. She's lost two fingers and most of an ear, and she's still the best door-warden I've ever had, because she knows that the day she stops being useful, I'll stop feeding her."
{n}She drops the chain back on the cushion.{/n}
"She sends me messages. She has things she'd like to say about the conditions of her work."''',
      c('"Does she still say it, the thing she admitted in the hall?"', "fee_admission", requires=f("hearing_proof")),
      c('"Is she still hiding the danger she would not name?"', "extra_observer", requires=f("hearing_uncertain")),
      c('"Does she still swear she never sold anyone who couldn\'t leave?"', "return_condition", requires=f("hearing_limits")),
      c('"Have her old buyers come looking for her?"', "new_price", requires=f("hearing_business"))),
    n("fee_admission", "Nocticula", '''"Every time she tries to complain. She starts to say the passengers were never prisoners, and the guard reminds her what she admitted in front of my whole court, and she stops." {n}Nocticula smiles.{/n} "You broke her in the hall. She stays broken. I find that very restful."''',
      c('"And what do you believe we learned about each other?"', "ambition")),
    n("extra_observer", "Nocticula", '''"Yes. She held out on you in the hall, and she holds out still. There's something about that door she won't tell me." {n}Nocticula's eyes glitter.{/n} "So I've put a second guard on her, whose only work is to watch her face whenever the door bites, and tell me what she flinches at. Sooner or later she'll flinch at the right thing. I can wait. I'm very good at waiting."''',
      c('"And what do you believe we learned about each other?"', "ambition")),
    n("return_condition", "Nocticula", '''"She swore it in the hall. She swears it to the guards. She swore it to the door, the last time it bit her, at the top of her voice." {n}Nocticula laughs.{/n} "Now she's the one who can't leave. I don't think she's noticed the joke. I've stopped explaining it. Some jokes are better when only the audience gets them."''',
      c('"And what do you believe we learned about each other?"', "ambition")),
    n("new_price", "Nocticula", '''"Three of them, so far. Courtiers from my own steps, the ones who went somewhere else to stand when you asked the hall who'd bought from her." {n}She examines her nails.{/n} "They came to the coast to make sure she wasn't talking. I had them collared beside her. She has company now. They don't get on."''',
      c('"And what do you believe we learned about each other?"', "ambition")),
    n("exiled", "Nocticula", '''"A tanner." {n}The alcove is empty, except for a little card propped on the velvet, the kind they hang round a slave's neck on the Fleshmarket block. It has a number on it.{/n}
"That's what she fetched," {n}Nocticula says, tapping the card.{/n} "Less than her shoes, which I sold separately, to a dancer in the Ten Thousand Delights who wears them on stage. Ilvara's at the tannery on the eastern canal now, scraping hides. They say she still tells the other slaves she was a great magician once, and they don't believe her, and beat her for putting on airs." {n}She props the card straight.{/n} "I go and look at her sometimes, from a carriage. She never sees me. I like that best of all."''',
      c('"And what do you believe we learned about each other?"', "ambition")),
    n("ambition", "Nocticula", '''"That you'll help me take things," {n}she says.{/n} "Willingly. With your own hands, and your own voice, and sometimes with an appetite you'd rather I didn't notice. I noticed."
{n}She walks to the end of the gallery, past Laulieh, who sits up very straight, and stops at the window, which looks out over the Midnight Isles toward the open sea.{/n}
"And that you'll sometimes refuse me, and mean it, and stand there afterwards waiting to find out what it costs. Most people who refuse me run. You wait." {n}She turns.{/n} "I find that more interesting than anything in this room."
"Is that what you wanted to show me?"
"I wanted to show you what I'm going to do with it." {n}She spreads her hand against the glass, over the islands.{/n} "All this. And more than this. I didn't build the Midnight Isles out of dead lords so that I could sit on them and be content. I want more than a harbor and a house and a magician in a lamp. I want things I haven't thought of yet." {n}She looks back at you over her shoulder.{/n} "And I want to know what you want from me, darling, while I take them. Say it carefully. I'll hold you to it."''',
      c('"You told me why you want to leave the Abyss. This work has not made that ambition smaller."', "known", requires=f("parent_ambition_heard")),
      c('"I want to stand beside someone who can hear a rival answer. I do not need you harmless."', "rival"),
      c('"I want power with you. I will argue over its use, not pretend I have no appetite for it."', "power")),
    n("known", "Nocticula", '''"No. It hasn't." {n}She does not turn from the window.{/n} "I told you once what I want past the Abyss, and why I can't walk away from it empty-handed. Every lord I ever killed has friends with long memories. A harbor doesn't change that. A hunting lodge doesn't change it. I don't intend to leave with a small life and a nice view."
{n}She turns then, and comes back down the gallery to you, and takes your face in both hands.{/n}
"So don't imagine, because you've seen me pleased with a lamp and a pair of shoes, that I'll ever be content with a small, manageable future. I'm capable of enjoying small things. I'm not capable of settling for them."
"I wouldn't believe you if you promised."
"Good. Save your disbelief for when it's useful." {n}Her grip tightens.{/n} "When we meet at the Worldwound, remember this room before you decide what I can afford to lose."
"Remember it before you decide what I can afford to give."
{n}She laughs, low, and lets you go.{/n} "Yes. That'll be the troublesome part."''',
      c('"Then let us decide what we are willing to build between those ambitions."', flags=f("ambition_discussed", "future_rivals"))),
    n("rival", "Nocticula", '''"A rival answer," {n}she repeats, delighted.{/n} "From a mortal. In my own gallery, with my servant listening." {n}Behind her Laulieh says "Fie!" under her breath, scandalized and thrilled.{/n} "Oh, I'll hear it. I'll hear every one you have. And then I'll do as I like, and you'll have to stand there and watch me, and come up with a better one for next time."
"And if I never do?"
"Then I'll be bored, and you'll be dead. One of those comes first." {n}She crosses to you and takes the back of your neck in her hand and kisses you, hard, in front of Laulieh and the moths and every mask on the wall, a kiss that is not a question.{/n}
"Come back with an argument I haven't already thought of," {n}she says against your mouth.{/n} "And sometimes with no argument at all. I don't want to find out that the only thing we enjoy together is winning."''',
      c('[Take her hand.] "Then come back with a better argument."', flags=f("ambition_discussed", "future_rivals"))),
    n("power", "Nocticula", '''"There." {n}She looks at you as if you had just handed her something heavy and gold.{/n} "An appetite you haven't dressed up as a sacrifice. I was beginning to think you'd never show me one."
{n}She comes close. Behind her, very quietly, Laulieh stops eating almonds.{/n}
"Then understand mine. Try to tame me, Commander, and you'll find out which of us leaves the cage. I'll want things that ruin your plans, and I'll take them first and tell you afterwards, if I remember. And if you do the same to me—" {n}she smiles{/n} "—I'll admire it, and then I'll make you pay for it, and then I'll admire that too."
{n}She takes your hand and presses it flat against the black velvet of the empty alcove beside her, where a trophy would go.{/n}
"Remember what we agreed about Shamira. My bed hasn't given her my throne. Yours hasn't given you mine. Sell a word from this room and I'll come and collect it from your tongue."
{n}She kisses you, and bites your lower lip when she is finished, not quite hard enough to bleed.{/n}''',
      c('"Then let us see what we can take together."', flags=f("ambition_discussed", "future_power"))),
], "lodge_consequences_finished")

s("second_door", "The second door", [
    n("start", "Narrator", '''{n}She does not take you to her gallery this time. She takes you down into the Harem itself, by the front stair, in front of everyone.
The Harem of Ardent Dreams is full tonight. Couches in tiers under a dome painted with things that move when you are not looking at them; incense; music from somewhere you cannot see; succubi and incubi and their guests tangled on the cushions, and slaves with trays, and courtiers in jewels doing business in low voices in the alcoves. Everyone who matters in the Middle City comes here to buy the Lady's favor from the Ardent Dream's court. They are buying it now. They stop when she comes down the stair.
They stop because she is holding your hand.
She walks you the whole length of the Harem. She does not hurry. She lets them look: at her, at you, at your hand in hers, and the whole vast room goes quiet tier by tier as you pass, the way a crowd goes quiet at an execution when the prisoner is brought out. A courtier with a lapful of contracts lets them slide to the floor. A succubus on the nearest couch stops in the middle of something and stays stopped. The highest couch, the Ardent Dream's, stands empty tonight. That is better. A court tells everything to the one who is not in the room.
Behind the dais at the far end there is a door. It is small and black and has no handle on the outside, and every person in the Harem knows what is behind it, because every person in the Harem has at some time wished to be invited through it.
Nocticula stops in front of it and turns round to face the room.{/n}
"This door is mine," {n}she says. She does not raise her voice; the dome carries it.{/n} "Nobody opens it unbidden. Nobody ever has." {n}She lifts your hand in hers, so that they can all see it.{/n} "Except the Commander, now. Look at the Commander's face, all of you. You'll be seeing it."
{n}Nobody breathes. Then, very quietly, somewhere up in the tiers, someone begins to applaud, and is hushed, and stops.
Nocticula turns her back on them. She looks at you, close, under the dome, with the whole Harem watching and listening, and she is smiling the way she smiled in the bell chamber.{/n}
"There," {n}she says, for you alone.{/n} "Now they know. Everything we did together, and now this. Say something, darling. They're all waiting to hear what the Lady's favorite sounds like."''',
      c('"I would have liked to see them step ashore."', "rescue", requires=f("purpose_rescue")),
      c('"You\'ve shown them your hand. What are you buying with it?"', "advantage", requires=f("purpose_power")),
      c('"You wanted them to see this. What are you still deciding?"', "curiosity", requires=f("purpose_curiosity"))),
    n("rescue", "Nocticula", '''"They did," {n}she says.{/n} "Into my city."
{n}She laughs at your face, softly, so that only the first tier can hear it.{/n}
"You wanted the passengers found. I found them. You stood on my rock and watched them come out of the cliff, wet and blinking, and then you decided where they went. That was you, darling. Not me. I only held the lantern." {n}She brushes something from your collar that is not there.{/n} "Whatever you told yourself in that cell about rescuing people, you've seen now what rescue means in Alushinyrra. It means changing hands."
"You could have let them go."
"I did what you told me. I always do what you tell me, in the end, if it amuses me." {n}She glances out over the silent tiers.{/n} "And it always amuses me to see what you'll choose. That's why they're all looking at you. They've never seen me take orders. They're trying to work out what you cost."''',
      c('"Then let them wonder. Ask me what you brought me here to ask."', "future")),
    n("advantage", "Nocticula", '''"Everything." {n}She is pleased you asked.{/n} "Every one of these people sells my favor for a living. Now they know whose favor is worth more than theirs. By morning half of them will be trying to buy you a drink, and the other half will be trying to have you killed, and all of them will be telling me which is which, to curry favor." {n}She smiles.{/n} "I'll learn more about my own court in a week than I have in a century. You're the best bait I've ever owned."
"Bait?"
"Don't be offended. Bait is the most important part of the hook." {n}She lifts your hand to her mouth and bites the knuckle, lightly, in front of everyone.{/n} "And the most expensive. I don't put just anything on the end of my line."
{n}Up in the tiers someone drops a glass.{/n}''',
      c('"Then let them bite. Ask me what you brought me here to ask."', "future")),
    n("curiosity", "Nocticula", '''"What you'll do," {n}she says.{/n} "With the door. With them watching. I've given you something nobody else in my city has, in front of everybody who could ever take it from you, and I want to know whether you'll walk through it, or stand here and make a speech, or turn round and leave me holding your hand in front of my own court like a fool." {n}Her eyes are very bright.{/n} "I genuinely don't know. Do you understand how rare that is? I always know."
"And if I leave?"
"Then they'll have seen the Lady in Shadow refused, and I'll have to do something very memorable to make them forget it." {n}She smiles.{/n} "So you see, there's no wrong answer. Only interesting ones."''',
      c('"Then let me give you an interesting one. Ask."', "future")),
    n("future", "Nocticula", '''{n}She lets go of your hand. The door stands at her back, black and closed. Behind you, the whole Harem waits.{/n}
"Our old bargain stands," {n}she says.{/n} "The Worldwound. What you'll do when you reach its heart. Nothing in this room changes that, and I'd think less of you if you imagined it did." {n}She tilts her head.{/n} "But this is not the Worldwound. This is my house, and my door, and my court watching. So I'll ask you here, where they can hear the answer."
{n}She leans back against the black door.{/n}
"Will you come back? Not because I've caught you, though I have, or because I've marked you, though I may have. Because you want to stand in my city and choose who runs. Because you want to open this door with your own hand and have all of them hear the latch." {n}Her smile is slow.{/n} "Or will you keep what we already have, and no more, and walk back up that stair in front of everyone with your hands empty? Either way, darling, I'll remember. I remember everything."''',
      c('"Yes. More private evenings and more arguments worth having."', "yes", requires=f("future_rivals")),
      c('"Yes. I want the company and the dangerous work we may choose together."', "power", requires=f("future_power")),
      c('"I want to keep what we already agreed, without making this undertaking a larger promise."', "limited")),
    n("yes", "Nocticula", '''"Then open it."
{n}She steps aside.
The door has no handle. You put your palm flat against the black wood instead, where a handle would be, and for a moment nothing happens, and somewhere behind you somebody laughs nervously. Then you feel it: the Gift, under your skin, answering something in the wood. The latch lifts on the inside with a sound like a key turning in a lock, very loud in the silent Harem, and the door swings inward on darkness and the smell of her.
Behind you, a whole room full of people lets out its breath.{/n}
"There," {n}Nocticula says, at your shoulder, very softly.{/n} "They heard it. Every one of them. They'll be telling that story in the Fleshmarkets for a hundred years." {n}Her mouth is at your ear.{/n} "I've wanted to do this in front of them since the first night. Get in."
{n}She puts her hand flat on your back and pushes you through, not gently, and follows, and kicks the door shut behind her without looking. Inside it is dark and warm, and she has you against the closed door before your eyes have adjusted, her mouth on your throat, her hands already busy. Much later, the room comes back. You are lying on something soft in the dark, with her weight on you and her hair over both your faces, and from very far away, through the door, the Harem has started talking again: one voice, then many, the sound of a whole court beginning to sell what it saw.{/n}
"Listen to them," {n}she says against your neck.{/n} "Every one of them is going to remember tonight. So am I."
{n}You reach to push the hair out of your eyes. She catches your wrist and pins it.{/n}
"Leave it. I want to look at you without your face arranged."''',
      c('[Keep the door. Keep the invitation.]', "end", flags=f("chosen_company"))),
    n("power", "Nocticula", '''"Company and dangerous work." {n}She tastes it, and laughs, low, and the front tier of the Harem shivers.{/n} "Oh, you greedy thing. Yes."
{n}She does not open the door yet. She turns to the room instead, and takes your arm, and walks you along the front of the dais, past the first tier of couches, where the most important of her court sit.{/n}
"You'll want no oath from me, and you won't get one; sworn allies bore me within a year. Every scheme we make, we bargain for fresh. When you refuse me, I'll be furious, and then I'll have you anyway, the same night, in the same bed. And one rule." {n}She stops in front of a courtier in green, a soft man with clever eyes who has been, until tonight, one of the people who sell her favor.{/n} "Nothing said behind that door is ever sold. The first of us who sells a pillow confidence may expect the other to come and collect it in person." {n}She smiles down at the courtier.{/n} "With tongs."
{n}The courtier, who has sold a great many things in his time, goes grey.{/n}
"This one," {n}she tells you, not lowering her voice,{/n} "has been selling introductions to me. He thinks I don't know. I was going to deal with him tonight. I'll do it later. Much later. He can spend tonight imagining what I'll do." {n}She pats the courtier's cheek, twice.{/n} "Don't leave the Harem, sweetheart. I'll want you where I can find you."
{n}Then she takes you back to the black door and opens it herself, with one hand, and the latch sounds through the whole room like a blow, and she pulls you through by the front of your shirt. A long while afterwards she asks what you would have proposed for the courtier. You are lying in the dark with your head on her stomach, and through the door the Harem is still very quiet, as though nobody out there dares to move.
Your answer is brief: send him an introduction to his creditors.{/n}
{n}She lifts her head.{/n}
"I knew there was a reason I kept you."''',
      c('[Keep the alliance, and the door inside it.]', "end", flags=f("chosen_alliance"))),
    n("limited", "Nocticula", '''{n}She is still for a moment. Behind you, the Harem has heard. You can feel it hear: a long, slow shifting along every tier, couches creaking, silk, a whisper starting somewhere high up and being smothered.
Nocticula does not look at them. She looks at you, and her face does not change at all.{/n}
"No," {n}she says.{/n} "In front of all of them."
"I'll keep what we agreed. I won't promise more than that."
"I heard." {n}She reaches past you and lays her palm on the black door, and you hear the latch move inside it, for her, and stop, and not open.{/n} "Then it stays shut. It will stay shut for you until I decide otherwise, and I'll decide it when it suits me, not when you change your mind." {n}She smiles, quite pleasantly.{/n} "I collect my debts, Commander. And I'm in no hurry. Hurry is for mortals."
{n}She takes your arm, as she took it coming in, and turns you round to face the room, and walks you back the whole length of the Harem toward the stair, slowly, with every eye on you. Nobody laughs. Nobody would dare. But they all see your empty hands, and they all see her face, which is smiling, and they all know what it means when the Lady in Shadow smiles like that at someone who has refused her.
At the foot of the stair she lets go.{/n}
"You'll come when I send for you," {n}she says.{/n} "That's what we agreed, and I always keep what I agree. And one night, darling, I'll send for you to collect. You won't know which night until you're standing in it."''',
      c('[Keep the earlier bargain. Leave the door shut.]', "end", flags=f("chosen_limit"))),
    n("end", "Narrator", '''{n}At the last she catches your sleeve, the way she always does, and pulls you back for one more look at you.{/n}
"Wake up," {n}she says.{/n} "I'm finished with you for tonight. Tell your crusaders whatever you like about where you were. Half of them will believe you, and the other half will be right."
{n}You wake in Drezen with the smell of incense in your hair. The room is cold, the lamp gone out. Someone in the corridor is knocking: the morning dispatch, late as usual. You lie still for a moment with your eyes closed, listening, half expecting to hear a latch.{/n}''', c('[Return to the waking world.]', flags=f("complete"))),
], "ambition_discussed")


def ending(id, title, text, requires=(), forbids=(), owner="Epilogue"):
    SCENES.append(scene("noct.ending_" + id, title, owner, 0, "", [n("end", "Narrator", text, portrait="Nocticula")],
        requires=f("complete") + tuple(requires), forbids=tuple(forbids), last=99,
        optional=True, Relationship="nocticula", Remote=True))


# Supplementary recollections of this undertaking, not replacements for native
# or parent political/romantic endings. Root must review epilogue delivery/order.
ORDINARY_BAD = ("noct.dead", "inhuman", "ascended", "sacrifice")
ending("company", "The door she keeps", '''{n}The door behind the dais in the Harem of Ardent Dreams stayed the Commander's to open unbidden. Nobody else ever did. The Ardent Dream's court counted the visits, and sold the count, and Nocticula bought it back from them now and then for the pleasure of reading how often she had been seen to want something.
She did not soften. She still sat in judgment in her throne hall and carried out the sentences herself; she still let her court bet on how long the condemned would last, and still won. She still read the Commander's thoughts whenever the Gift held, and laughed out loud at the parts the Commander had meant to keep, sometimes in company. When the Commander pronounced a sentence at her trials, she carried it out. When the sentence bored her, she said so, and chose a better one.
The harbor and the lodge became stories in the Middle City, and then songs, and the songs got the details wrong, which she preferred. The bell from Istrava's house hung somewhere she could reach it.
She never once said she loved anyone. Once, at a window over the burning city, she told the Commander: "You are mine to disappoint." It was the closest she came, and it was close enough.{/n}''', requires=f("chosen_company"), forbids=ORDINARY_BAD)
ending("alliance", "The chosen instrument", '''{n}The harbor and the lodge were the first things the Commander helped Nocticula take. They were not the last.
She called the Commander "the chosen instrument of my will" in front of her court, and meant it as the highest praise she had, and the court understood it exactly. Instruments are used. This one was used often, and well, and argued about every use, and was kept anyway, because nothing else in her city could surprise her twice.
The courtier who had sold introductions to her waited in the Harem for nine days, as he had been told to, and on the tenth she remembered him. She had his creditors introduced to him one at a time, in a locked room, and the Middle City talked about the result for a season. She told the Commander about it in bed, in detail, and laughed until she cried.
Her rule spread. Houses that had hunted under her protection closed, or burned, or were taken and hunted in by her. Captains who sold passage under borrowed flowers learned to stop. Each of these things she called ours when she was pleased, and mine the rest of the time, and both were true.{/n}''', requires=f("chosen_alliance"), forbids=ORDINARY_BAD)
ending("limit", "An undertaking completed", '''{n}At the end of the harbor undertaking Nocticula offered the Commander her door, in front of her whole court, and the Commander refused it and walked back up the Harem stair with empty hands.
She did not forgive it. She did not punish it, either, not then. She kept the bargain they had made, exactly, to the letter, the way she kept everything she agreed to. She sent for the Commander when the Gift allowed and the Commander came. The door behind the dais stayed shut.
She remembered. The Midnight Isles learned, over that time, that the Lady in Shadow had been refused by a mortal and had smiled about it, and the smile frightened them more than any punishment would have.
Long afterwards, on a night of her own choosing, she sent for the Commander and collected. What she collected, and how, the Commander never told anyone. It was not gold. It was exactly as unpleasant as she had promised, and she enjoyed every moment of it, and at the end of it she laid her hand on the Commander's cheek and said, "There. Paid. I'll think of something else you owe me."{/n}''', requires=f("chosen_limit"), forbids=ORDINARY_BAD)
ending("death", "The unused question", '''{n}After Nocticula's death, the room beside the quay could only be remembered. The dream which once supplied its light no longer brought an invitation from her.
During the harbor affair she had made an entire sea because the Commander noticed its absence. She had kept a damaged lens and an old bollard long after each had ceased to be useful to the conversation. None explained what she might have wanted from another evening.
The passengers had come out of their borrowed harbor before she died. Their names remained in the account, beside the fees she disputed and the questions she had sent back for a better answer. Between two of those reports there had been a private meeting. She had rested her hand beside the Commander's, close enough to touch, and waited.
The next movement belonged to a time when both were still there.{/n}''', requires=("noct.dead",))
ending("sacrifice", "An answer no longer possible", '''{n}After the Commander's sacrifice, the harbor account still contained the questions asked before the crossing. A reader could follow them through amended instructions, the names called at the door, and the reports delivered afterward. The person who had asked them would never read another reply.
Nocticula had once completed a room while deciding how to invite that person back. She had kept a useless bollard beside its hearth and made a window overlooking water that had not been there at first.
On their final visit of the undertaking she had asked whether there should be more evenings. The Commander had given an answer. Now the unfinished invitations belonged to her alone, and even a perfectly chosen question would receive no new answer from the one she had intended to ask.{/n}''', requires=("sacrifice",), forbids=("noct.dead", "inhuman", "ascended"))
ending("ascent", "Her champion comes home", '''{n}When Pharasma summoned the Commander to her court, another summons drowned her out: the Lady in Shadow, calling her champion home. The Commander went.
Nocticula met them in the throne hall in front of everyone, on the dais where she had once sat the Commander at her right hand to let her court wonder what the crusader cost her. Now there was no need to wonder. The Commander came up the steps in true demonic form, and the court went down on its faces, and she laughed, long and hard, and the hall laughed with her because it had learned to.
"I bet on you," she said. "Everyone told me not to. I so rarely lose."
The harbor had been the first thing they took together, and the lodge the second, and they were small things, a door in a cliff and a house in a garden. She kept the bell from Istrava's lodge by her throne anyway, and rang it sometimes when the Commander was away, to see who in her court would flinch. The conquests that followed were not small. They were only beginning.{/n}''', requires=("ascended",), forbids=("noct.dead", "inhuman"))
ending("changed", "The earlier company", '''{n}The Commander of the harbor affair belonged to an earlier time. Nocticula had asked that person for advice, resented some of it, and finished the undertaking with an invitation beside a window overlooking dark water.
Then the Commander changed, and the old invitation ceased to describe the being who might answer it. Nocticula knew the danger of trusting a familiar name after its owner had become something else.
The earlier account still held the missing passengers' names. It held the magician's evasions, the cost of a crossing, and the questions that had exposed an awkward truth. Its final private evening was harder to record. Nocticula had caught a fold of the Commander's sleeve, nearly made a joke, and chosen to speak plainly instead.
That hesitation belonged to the person she had met then.{/n}''', requires=("inhuman",), forbids=("noct.dead",))
ending("aeon", "A harbor without that witness", '''{n}In the remade history, the Commander never arrived at the quay without a sea. Nocticula had no occasion to build its water, move a lamp nearer a couch, or discover which unwelcome question that particular guest would ask.
The two doors, the copied lens, and the bollard beside the hearth belonged to meetings erased with the history that had allowed them. No passenger in the remade world owed a return to the lost investigation. No letter carried an answer from it.
There was no empty place in Nocticula's chamber where the room ought to have been. It had been made for somebody she had not met in that way, during evenings the new world had never contained.{/n}''', owner="AeonEpilogue")


from storylines.nocticula_n1 import scaffold
scaffold(SCENES)


def integrate(payload):
    """Register only verified read-only bindings; root owns export registration."""
    for name, bindings in (("Etudes", ETUDES), ("SeenCues", SEEN_CUES)):
        target = payload.setdefault(name, {})
        for key, value in bindings.items():
            if key in target and target[key] != value:
                raise ValueError("Conflicting Nocticula parent binding: " + key)
            target[key] = deepcopy(value)
    # Native Epilogues/Cue_0294 (enGB 13a9b9dc) requires this flag,
    # the Wound closed, and Nocticula alive. Read only; no authored producer.
    payload.setdefault("UnlockableFlags", {})["noct.native_redeemed"] = "48909f9355f52e14ab3a8748fa3e81a0"
    payload.setdefault("Derived", {})["noct.redeemed_epilogue"] = [["noct.native_redeemed", "ending.wound_closed"]]
    payload.setdefault("DerivedForbids", {})["noct.redeemed_epilogue"] = ["noct.dead"]
    # Existing reserved-key registry: known to validation, never produced.
    pending = payload.setdefault("PendingHooks", [])
    if "noct.retired" not in pending:
        pending.append("noct.retired")
    relationships = payload.setdefault("Relationships", {})
    if "nocticula" in relationships and relationships["nocticula"] != RELATIONSHIP:
        raise ValueError("Conflicting Nocticula relationship registration")
    relationships["nocticula"] = deepcopy(RELATIONSHIP)

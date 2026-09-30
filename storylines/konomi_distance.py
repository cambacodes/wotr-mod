"""Authored correspondence and a temporary return after the private departure."""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, nodes, requires=(), delay=168):
    for node in nodes:
        node["Portrait"] = "Konomi"
    SCENES.append(scene("konomi." + id, title, "Konomi", 3, "", nodes,
                        Relationship="konomi", Remote=True, Areas=[DREZEN], Chapters=[3, 5],
                        requires=("konomi.dismissed", "konomi.office_completed", "konomi.private_departed",
                                  "konomi.private_address", *requires),
                        forbids=("konomi.present", "inhuman", "konomi.farewell"),
                        delay=delay, optional=True))


s("capital_letter", "The first ordinary post", [
    n("start", "Narrator", '''{n}A letter from Nerosyan waits among the messages delivered to your quarters. It bears Konomi's name and a forwarding address crossed out in favor of a new one. The receiving agent has added a short note confirming that future letters can go directly to her lodging.{/n}
{n}Inside, Konomi has dated the pages separately. The last was written several days after the first.{/n}''',
      c('[Read her letter.]', "arrival"),
      c('[Set aside time to read and answer it later.]', abort=True)),
    n("arrival", "Konomi", '''"We arrived with two wagons, all six horses and considerably fewer opinions about how quickly we ought to have arrived. Selis gave the receiving agent her list. Vanna asked to be present while it was checked. Neither looked offended. I shall refrain from announcing that I have cured them.
"The room I have taken faces a wall. The woman who lets it assured me that this makes it quiet. Her daughter practices a stringed instrument on the other side of the wall. I have learned the first half of one tune very well.
"You asked me to write about the work. I have the first replies."''',
      c('[Read about the woman who challenged her arguments.]', "arguments", requires=("konomi.departure_arguments",)),
      c('[Read the account she promised, including the refusals.]', "refusal", forbids=("konomi.departure_arguments",))),
    n("refusal", "Konomi", '''"The first woman cannot offer me a post. She explained this over a very good lunch, during which she asked how I would settle a disagreement between two of her clients. I answered the first question before realizing what I was doing. At the second, I put down my fork.
"She asked whether I had become too proud to help an old acquaintance. I asked where I should send the fee. The rest of lunch was less pleasant.
"I had dressed carefully. I had prepared an excellent account of my experience. I returned to my room with enough compliments to fill a drawer and no work. You wanted the refusals. There is one."
{n}A new paragraph begins beneath a small ink stain.{/n}
"I have stopped composing the letter in which I explain why she will regret it. It was becoming longer than the conversation deserved.
"The woman who used to read all my arguments has offered paid work. I have her written terms beside me. They are considerably more useful than the compliments."''', c('[Turn to the next page.]', "second")),
    n("arguments", "Konomi", '''"The woman whose old letter I brought on the wagon remembered it. She did not remember the sentence I found most insulting. I was obliged to find it for her, which diminished the dignity of my complaint.
"She read it, winced and said she would write that part differently now. I had no answer ready for that. We spent the rest of the afternoon discussing the argument instead.
"She has work that needs doing. It is smaller than I hoped. She told me precisely why she will not offer me more yet. I disliked hearing it, and I shall probably take the work.
"You may enjoy knowing that I carried an old grievance all the way to Nerosyan only to find its author more reasonable than I remembered."''', c('[Read what the work involves.]', "second")),
    n("second", "Konomi", '''"The work concerns an agreement between a workshop and the women who sell its goods. They have written down the price of almost everything except the work they keep asking each other to do. I thought of our wagon yard."
{n}The next lines return to your part in that afternoon.{/n}''',
      c('[Read what she remembers of measuring the cargo.]', "measured", requires=("konomi.carriers_measured",)),
      c('[Read what she remembers of asking about the customers.]', "asked", forbids=("konomi.carriers_measured",))),
    n("measured", "Konomi", '''"I remembered you holding the cord while Vanna checked the figures. I had been asking two women to be precise while letting them speak as if the third wagon stood beside us. You helped put something measurable in front of them.
"I asked to see the workshop before I proposed any terms. There were three unfinished orders stacked beneath the bench. None had appeared in the account I was given. I thought you would appreciate that."''', c('[Read the last page.]', "personal")),
    n("asked", "Konomi", '''"I remembered your question about the customers. The smallest line in Selis's list turned out to be the one she was most afraid to change.
"This time I asked the sellers which customer they would least like to disappoint. I learned more from the pause before the answer than from the account I had been sent. I should have asked sooner. You may claim some credit for that question."''', c('[Read the last page.]', "personal")),
    n("personal", "Konomi", '''"I have also bought a pear. The woman selling them gave me detailed instructions about when it would be ripe. I followed them and obtained an excellent pear. It was the least troublesome advice I have received since arriving.
"I wanted to tell you while I was eating it. There was nobody in the room, so I began this last page. That is the sort of absence I did not anticipate. I had prepared for difficult evenings and important news. I had not prepared for fruit.
"Tell me something small. I want to know what I am missing while I am busy imagining the things you might be facing."''',
      c('[Tell her about a quiet meal you made time to enjoy. Ask her to keep some of that pear-buying luck for your next visit.]', "answer", flags=("konomi.capital_reply_quiet",)),
      c('[Describe how long you spent looking for this very letter after placing it beneath another report. Admit you were distracted by seeing her name.]', "answer", flags=("konomi.capital_reply_distraction",))),
    n("answer", "Narrator", '''{n}You write on an unmarked sheet. Her account of the capital lies beside you while you work; once, you turn back to the paragraph about the room and its unfinished tune.{/n}
{n}There is enough room at the bottom for an invitation. You tell her you want to see her again, when she can arrange the journey, and ask her to write before making plans. Then you copy the new address carefully onto the outside.{/n}''',
      c('[Send the answer with the ordinary outgoing post.]', flags=("konomi.capital_answer_sent",))),
], requires=("konomi.private_letters",), delay=336)

s("return_offer", "A journey with two purposes", [
    n("start", "Narrator", '''{n}Konomi's next envelope contains a letter and a small sheet folded inside it. On the smaller sheet she has copied the tune that comes through her wall, as far as she has learned it. A note below the last phrase reads: "Here she begins again. I have no further intelligence."{/n}''',
      c('[Read her answer.]', "reply"),
      c('[Wait until you can give the letter your attention.]', abort=True)),
    n("reply", "Konomi", '''"The workshop agreement is finished. They asked me to stay for the first payment under it. I said I would. Then I wondered whether I had volunteered for another afternoon of unpaid work and asked what they intended to pay me for attending. They answered without offense. I could have saved myself a remarkable amount of indignation by asking sooner."
{n}She has underlined the next sentence once.{/n}
"I liked your letter."''',
      c('[Read her answer about the quiet meal.]', "quiet", requires=("konomi.capital_reply_quiet",)),
      c('[Read her answer about your misplaced post.]', "distraction", forbids=("konomi.capital_reply_quiet",))),
    n("quiet", "Konomi", '''"I read the part about your meal while eating something I had allowed to go cold. It was an effective rebuke, though I suspect you did not intend one. I put the letter down, asked for something warm and finished eating before I picked it up again.
"The pear seller says I ask too many questions. I have bought two for the woman whose advice I resented. I considered sending you one. Selis explained what a pear would look like after the journey. You must wait."''', c('[Read her proposed visit.]', "work")),
    n("distraction", "Konomi", '''"I would like to pretend I received your admission with composure. In fact, I was reading it on the stairs and had to move when somebody asked to pass. I had stopped between floors without noticing.
"Keep your papers in better order. I shall endeavor to stop obstructing the household. Between us, we may eventually make correspondence safe for the people around us."''', c('[Read her proposed visit.]', "work")),
    n("work", "Konomi", '''"There is work in Drezen. Selis has recommended me to a woman who wants someone to examine the terms of a storage lease before she signs it. I have received a written offer, including the fee. You may congratulate me on this advance.
"I would like to accept it. I would also like to accept your invitation. I have allowed time for both, so you need not pretend to have a lease in need of examination.
"If you can see me, send your answer through Selis's agent. I shall wait for it before booking the journey. If this is a poor time, tell me. The work can be arranged separately."''',
      c('[Confirm the visit and set aside a private evening.]', "confirm", flags=("konomi.return_private_evening",)),
      c('[Confirm the visit and suggest a walk together before dinner.]', "confirm", flags=("konomi.return_walk",)),
      c('[Write that you cannot make plans yet. Reconsider the invitation later.]', abort=True)),
    n("confirm", "Narrator", '''{n}You confirm that you want her to come and tell her how to reach you when she arrives. You give the answer to the outgoing post before another report can cover it.{/n}
{n}Her proposed visit will take more than a wish and a free evening. There is a journey to arrange, work to finish in Nerosyan and the road itself. This time, you have both agreed what you are waiting for.{/n}''',
      c('[Send the confirmation.]', flags=("konomi.return_expected",))),
], requires=("konomi.capital_answer_sent",), delay=168)

s("private_reunion", "What the letters left out", [
    n("start", "Narrator", '''{n}A note reaches you after Konomi arrives in Drezen. She has taken a room for the visit and asks you to meet her in the courtyard below it. When you enter, she is standing beside a travel case with a paper parcel in her hands.{/n}
{n}For a moment she looks as if she is about to greet a delegation. Then she sees your face and laughs under her breath.{/n}
"I have written several pages to you since we last stood in the same place. Apparently none of them has taught me how to begin this conversation."''',
      c('"You could tell me what is in the parcel."', "parcel"),
      c('[Offer her a welcoming embrace.]', "embrace"),
      c('[Explain that you need to postpone the meeting.]', abort=True)),
    n("embrace", "Konomi", '''{n}She puts the parcel carefully on top of the case and comes to you. Her arms close around you; for a few breaths she seems content to let the greeting take care of itself.{/n}
"That helps."
{n}When she steps back, she looks you over once, with less concealment than she might have attempted before the journey.{/n}
"I was going to ask whether you have been well. I think I would rather hear the long answer when we sit down."''', c('"First, tell me what you brought."', "parcel")),
    n("parcel", "Konomi", '''{n}With the parcel resting on the case, Konomi unfolds the paper.{/n}
"Supper. And pears bought here, after I arrived. I have accepted the limitations of transporting ripe fruit."
{n}She opens one corner of the paper to inspect the contents, then closes it again.{/n}
"The lease can wait until tomorrow. I told the woman who hired me that I had a previous appointment. She asked whether she should dress formally when she eventually met you. I explained that you would not be attending."
{n}She picks up the parcel.{/n}
"Shall we keep our appointment?"''',
      c('[Take the walk you suggested.]', "walk", requires=("konomi.return_walk",)),
      c('[Join her for the private evening you arranged.]', "room", forbids=("konomi.return_walk",))),
    n("walk", "Narrator", '''{n}Konomi leaves the case in her room before joining you outside. You carry the parcel while she finds a street that is quieter than the one she remembers. At the first turning she confidently chooses a passage that ends at a locked yard.{/n}
{n}She studies the gate, then turns around.{/n}
"It used to go through. Or I used to be considerably better at remembering where I was going."
{n}When you offer to lead, she hands you responsibility for the route with exaggerated relief. You find a place to sit before the food grows cold. Konomi settles beside you and unpacks it on the paper between you.{/n}''', c('[Ask what the visit will mean for her work in Nerosyan.]', "visit")),
    n("room", "Narrator", '''{n}She carries the parcel upstairs while you bring the case. You leave it against the wall and help her lay out supper on the little table. While she unwraps the bread, she begins to hum. The tune stops abruptly.{/n}
"Now I am doing it."
{n}She sees you listening and gives an irritated little smile.{/n}
"The tune from the other side of my wall. I asked how it ends. She told me she was not ready to play that part yet. I have caught myself listening at the door in case she changes her mind."
{n}Konomi tries the last phrase once more, then gives up and passes you the bread.{/n}
"I used to have more imposing reasons for wanting to return to the capital."''', c('[Ask what the visit will mean for her work in Nerosyan.]', "visit")),
    n("visit", "Konomi", '''"I have kept the room there. The instrument has acquired an entire second tune. I could hardly leave permanently at such a promising moment."
{n}She breaks a piece of bread and considers the answer more seriously.{/n}
"There is work worth returning to. This lease will keep me here for several days, perhaps longer if the parties disagree about the revisions. After that I intend to go back. I wanted you to know before we start enjoying ourselves and become tempted to avoid the subject."
{n}She tastes the bread.{/n}
"I also want more of this than letters. I found that out by writing them."''',
      c('"So did I. I want us to keep making these visits possible."', "want", flags=("konomi.distance_wants_visits", "konomi.private_interest", "konomi.attracted")),
      c('"I want to spend this visit with you. Let us see how it goes before we plan the next one."', "visit_only", flags=("konomi.distance_taking_time",))),
    n("want", "Konomi", '''"Good. I had a much longer explanation ready, and I am pleased not to need it."
{n}She reaches across the paper and takes your hand as if it had been on her list of purchases.{/n}
"I missed you. There were occasions when I missed the idea of you and suspected the real person might have been more difficult. It is a relief to have the real person here."''',
      c('[Take her hand and kiss her.]', "kiss", flags=("konomi.reunion_kissed",)),
      c('[Take her hand and stay beside her.]', "partners")),
    n("visit_only", "Konomi", '''"Yes. I can leave the next journey unarranged for one evening."
{n}She puts another piece of bread on your plate before taking one for herself.{/n}
"Tell me something that did not fit in your letters. I have had far too much time to supply my own version of your days."''', c('[Continue over supper.]', "partners")),
    n("kiss", "Konomi", '''{n}She sets down the bread before she meets you. The care of that small movement almost makes you smile; then her hand is at your cheek and the distance between you is gone.{/n}
{n}When she draws back, she stays close enough to speak quietly.{/n}
"You make it difficult to stop."
{n}She kisses you once more, then takes a breath and glances at the abandoned meal.{/n}
"Eat something. I did not carry that parcel here merely to give us an excuse to ignore it."''', c('[Return to supper, keeping close.]', "partners")),
    n("partners", "Konomi", '''{n}Konomi turns one of the pears in her hand, testing it gently with her thumb.{/n}
"What did you leave out of your letters? Something you wanted to tell me in person, perhaps."
{n}She sets the pear between you.{/n}
"I kept putting the best explanation on the page. In person, my answers have been less impressive. I let an old contact extract advice from me over lunch. I had given her far too much before I thought to ask for a fee."
{n}She looks at you over the tableware.{/n}
"Your turn, if you like."''',
      c('"I have been sleeping badly. I keep rehearsing conversations I cannot change."', "sleepless"),
      c('"I had an evening when nobody needed an answer from me. I wished you could have been there."', "good_evening"),
      c('"Nothing I want to explain tonight. I am happy being here."', "content")),
    n("sleepless", "Konomi", '''"Do you win them on the second attempt?"
{n}At your expression, she puts down her knife.{/n}
"I am asking because I generally do. I have never been defeated by somebody who is not there to answer. Then I wake up cross with the person who spoke to me, as though she ought to have heard my improved argument."
{n}She reaches for her cup and holds it between her hands.{/n}
"Or is it something you wish you had not said at all?"''',
      c('"I keep wondering whether a kinder answer would have changed anything."', "kinder"),
      c('"Mostly I wish I had found the right words sooner."', "sooner")),
    n("kinder", "Konomi", '''"Sometimes it would. I cannot tell you otherwise merely because I am pleased to see you."
{n}She looks down into her cup before continuing.{/n}
"I have written apologies that did not recover what I hoped they would. I was angry about that for a while. I thought the work of writing one ought to purchase a better reception."
{n}A wry smile touches her mouth.{/n}
"There is a woman in Nerosyan who still will not dine with me. She does answer my letters now. I have had to be satisfied with that."
{n}She looks back at you.{/n}
"If you have something left to say to her, send it by an ordinary post while she can still read it. Not tonight. Tonight I have paid for the journey, and I intend to have the whole of your attention for the fare."''', c('[Thank her, and return to the meal.]', "schedule")),
    n("sooner", "Konomi", '''"Then tell me the version you have been rehearsing. I reserve the right to defend the absent party if you have made her conveniently foolish."
{n}You give her the argument. She stops you once to ask what the other person actually said, rather than what you now suspect she meant. By the time you answer, you are smiling despite yourself.{/n}
"There. A more formidable opponent. If you are going to lose sleep, you may as well earn a respectable victory."
{n}She takes a drink, her gaze still on you.{/n}
"For tonight, may I suggest postponing the next round? I have traveled a long way to be the person you are talking to."''', c('[Agree, and return to the meal.]', "schedule")),
    n("good_evening", "Konomi", '''"What would I have done with myself?"
{n}You describe the idle part of the evening, after the plates had been cleared, when somebody began a story and everybody kept interrupting to improve it. You think she would have objected to at least two of the improvements.{/n}
"Almost certainly. I should like to hear it without your corrections first."
{n}You begin. By the second interruption she has caught herself doing precisely what you predicted.{/n}
"Very well. Finish it. I shall make a list."
{n}She does not. She keeps trying to guess the end, and when you finally reach it, she laughs loudly enough to surprise you both.{/n}''', c('[Enjoy the meal together.]', "schedule")),
    n("content", "Konomi", '''"Then stay. I will not make you produce a confidence before I let you have supper."
{n}She cuts the pear and offers you the first piece, then tastes one herself.{/n}
"Good. I was beginning to suspect I had praised these beyond anything a piece of fruit could reasonably accomplish."
{n}For a while you eat without supplying another subject. When she looks up, you find that she has been smiling to herself.{/n}''', c('[Stay with her.]', "schedule")),
    n("schedule", "Narrator", '''{n}The food dwindles, and the stiffness of the first greeting disappears.{/n}''',
      c('[Tell her how you have made room for this visit among your other relationships.]', "others", requires=("konomi.private_other_promises",)),
      c('[Ask what she most wants to do while she is here.]', "plans", forbids=("konomi.private_other_promises",))),
    n("others", "Konomi", '''{n}She listens, asking once when you need to be elsewhere. When you answer, she nods.{/n}
"Then we know how many hours I have bought. I shall spend them, not audit them."
{n}She brushes a crumb from the edge of her plate.{/n}
"Keep your other appointments. Only do not come to my door next time worn thin from making excuses at everyone else's. I want you at full value."''', c('[Ask what she most wants to do while she is here.]', "plans")),
    n("plans", "Konomi", '''"I want to finish the lease without it occupying every hour until I leave. I want to find the woman who sold me those pears and discover whether choosing good ones was skill or luck. And I want another evening with you."
{n}She smiles at the last admission without trying to take it back.{/n}
"We can arrange that before I go. Have the last pear. I want to know whether you think I chose well."''',
      c('[Share the pear and stay with her.]', flags=("konomi.private_returned", "konomi.reunion_kept",))),
], requires=("konomi.return_expected",), delay=336)

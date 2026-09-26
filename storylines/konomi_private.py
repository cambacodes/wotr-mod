"""Authored private visits after dismissal; no native actor or trade-state changes."""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, nodes, requires=(), delay=24):
    for node in nodes:
        node["Portrait"] = "KonomiPrivateEvening" if id == "before_road" and node["Id"] == "start" else "Konomi"
    SCENES.append(scene("konomi." + id, title, "Konomi", 3, "", nodes,
                        Relationship="konomi", Remote=True, Areas=[DREZEN], Chapters=[3, 5],
                        requires=("konomi.dismissed", "konomi.office_completed", "konomi.reconnection_open", *requires),
                        forbids=("konomi.present", "inhuman", "konomi.farewell", "konomi.private_departed"),
                        delay=delay, optional=True))


s("carriers", "What the wagons can carry", [
    n("start", "Konomi", '''{n}Konomi's note asks you to meet her at a wagon yard. When you arrive, she is standing beneath the raised tailboard of a cart, holding a measuring cord away from a patch of axle grease.{/n}
"Both women agreed to let you attend. They would prefer you as my guest rather than as somebody empowered to settle their argument by announcing its conclusion."
{n}She steps clear of the tailboard.{/n}
"I said I would explain the distinction. Please justify my confidence."''',
      c('"I came to see how you work."', "women"),
      c('"I cannot stay today. Finish the inspection without me."', abort=True)),
    n("women", "Narrator", '''{n}Konomi introduces Vanna, the stocky woman scraping mud from a wheel, and Selis, who has been checking the fastenings on a stack of empty chests. Both are well into middle age. Neither looks pleased with the other's diligence.{/n}
{n}"Two wagons," Vanna says. "Mine. Six horses, also mine. We can carry what she has promised."{/n}
{n}"I promised space on three wagons," Selis replies. "The third will join us before departure."{/n}
"Whose third wagon?" Konomi asks.
{n}Selis names a woman who has not yet answered her offer. Vanna stops scraping the wheel.{/n}
{n}"You told me it was arranged."{/n}
{n}"I told you I knew where to obtain it."{/n}
{n}Konomi stretches the measuring cord along the bed of the cart.{/n}
"Then let us discover how much of your agreement exists outside the future tense."''',
      c('[Help measure the space already available.]', "measure", flags=("konomi.carriers_measured",)),
      c('[Ask Selis what she has promised the customers.]', "customers", flags=("konomi.carriers_asked",))),
    n("measure", "Narrator", '''{n}Vanna holds one end of the cord while you take the other. Konomi records the usable space, then asks about weight. Vanna answers immediately. When Selis begins to add the third wagon, Konomi points to the two beside you.{/n}
"These first."
{n}The empty chests fit. The sacks Selis has described would leave too little room for the rest of the promised cargo. Vanna checks the figures herself and nods reluctantly.{/n}
{n}"We could take the first two customers. The third would have to wait."{/n}
{n}Selis looks at her list.{/n}
{n}"The third introduced me to the other two."{/n}''', c('[Let Konomi follow that admission.]', "obligation")),
    n("customers", "Narrator", '''{n}Selis has promised one customer a departure date she could meet with two wagons. The other two have been offered the same date. When you ask which agreement came first, she points to the shortest entry.{/n}
{n}"That one introduced me to the others. If I leave her cargo behind after using her name, she will remember it."{/n}
{n}Konomi sets down the cord.{/n}
"You have spent a favor before knowing what it will cost to repay."
{n}Selis flushes. Vanna's expression changes, losing some of its anger.{/n}
{n}"Why did you not tell me?"{/n}
{n}"Because you would have said exactly that."{/n}''', c('[Give the women room to answer one another.]', "obligation")),
    n("obligation", "Konomi", '''{n}Konomi turns to Vanna.{/n}
"You wanted this partnership before we counted a single chest. Why?"
{n}Vanna picks a flake of dried mud from her sleeve.{/n}
{n}"She kept my drivers paid when I broke my leg last winter. It would have taken me another year to begin again if she had not."{/n}
"And you wanted to repay her by accepting a promise you had not checked?"
{n}"I wanted to repay her by being the person she could ask."{/n}
{n}Konomi looks at Selis. Selis closes the cargo list.{/n}
{n}"I did not want to ask her for another favor. I wanted to bring her business."{/n}
{n}For a moment the two women look equally miserable.{/n}
"You have brought business," Konomi says. "More than the wagons can carry. We can work with that once you stop offering each other gratitude disguised as arithmetic."''', c('[Listen to her proposed next step.]', "terms")),
    n("terms", "Narrator", '''{n}Konomi has Selis write to the customer who made the introductions. The letter explains the missing wagon and offers a later date for part of the load. Vanna checks that the offered date is possible before Selis signs it.{/n}
{n}Their agreement will cover one journey with two wagons. They will divide its proceeds according to the wagons, labor and customers each provides, then decide whether to continue. Konomi makes them state who will pay if another promise exceeds the space available.{/n}
{n}Selis dislikes that question. Vanna dislikes how long she takes to answer it. Neither leaves.{/n}
{n}The last disagreement concerns who will approach the third wagon's owner. This time Selis says she will ask and return with an answer, rather than announcing that the wagon is practically theirs.{/n}''',
      c('"A smaller agreement than they hoped for."', "smaller"),
      c('"They still want to travel together."', "together")),
    n("smaller", "Konomi", '''"Yes. They may decide after one journey that they dislike doing business together. It would be useful to discover that before one of them owns half the other's livelihood."
{n}She winds the measuring cord around her hand.{/n}
"I would have preferred them to tell me about the missing wagon yesterday. I spent a perfectly good afternoon comparing promises about an object nobody here owned."''', c('[Walk back toward her lodging with her.]', "walk")),
    n("together", "Konomi", '''"They do. I was beginning to wonder whether either would admit it before the horses grew old."
{n}She winds the cord around her hand.{/n}
"I cannot make that wish profitable. I can make it harder to conceal a bad promise inside a grateful one. That should keep me occupied until their customer answers."''', c('[Walk back toward her lodging with her.]', "walk")),
    n("walk", "Konomi", '''{n}At the gate, she checks her sleeve for grease. Finding none, she looks almost disappointed that the precaution was necessary.{/n}
"They have work to do before I can finish mine. I have told them I will collect the answer later."
{n}She stops where the street divides, one way toward headquarters and the other toward her temporary rooms.{/n}''',
      c('"Then may I claim an evening while you are waiting?"', "evening", requires=("konomi.private_interest",)),
      c('"I would like to see you again before you leave."', "evening", forbids=("konomi.private_interest",))),
    n("evening", "Konomi", '''"Yes. Send me a time."
{n}She shifts the cord into her other hand before touching your arm.{/n}
"You listened today. It was pleasant having you there without wondering when I would have to disagree with you in front of somebody else."
{n}Her smile becomes more mischievous.{/n}
"I may disagree with you privately, of course. It would be a shame to waste all the practice."''', c('[Arrange the private evening.]', flags=("konomi.carriers_inspected",))),
], requires=("konomi.private_meeting", "konomi.private_history_ready"))

s("before_road", "An evening before the road", [
    n("start", "Konomi", '''{n}Konomi has moved a traveling case away from the place where you will sit. Its straps lie loose across the lid. A length of cloth caught beneath one buckle suggests that she gave up packing when she heard your step.{/n}
"Their customer has accepted the later date for part of the cargo. With several remarks about the value of being informed before she had arranged her own business around a promise."
{n}She shuts the door behind you.{/n}
"Selis read those aloud. Vanna listened. I think they have a chance."''',
      c('"So you can leave for Nerosyan."', "departure"),
      c('"I am glad the work ended well. I came to see you."', "company"),
      c('[Explain that you must postpone the evening.]', abort=True)),
    n("departure", "Konomi", '''"When they have loaded the wagons. There is a place for my case and, I am assured, for me. I have checked both claims."
{n}She sits, leaving the chair nearest the case for you.{/n}
"I wanted to leave this city with a dignified explanation for everything that happened. I now have a seat on a wagon and a professional interest in whether two stubborn women can get through the next journey without lying to spare each other's feelings."
{n}Her attention returns to you.{/n}
"And this evening. I wanted it before I knew what I would say."''', c('[Sit beside her.]', "histories")),
    n("company", "Konomi", '''"Then I shall give you an account that contains less information about freight."
{n}She sits, leaving the chair nearest the case for you.{/n}
"I was pleased when your note arrived. I then spent too long deciding whether to move that case out of sight. I decided it would be foolish to have you trip over it in the passage merely to improve the appearance of the room."
{n}She glances at the open straps.{/n}
"It can stay. So can you."''', c('[Sit beside her.]', "histories")),
    n("histories", "Narrator", '''{n}The room is quieter than the courtyard. Konomi has left the window open a little; you can hear someone sweeping the passage below it.{/n}''',
      c('"I have wanted another evening like this with you."', "lovers", requires=("konomi.lovers",)),
      c('"I am glad you asked me here."', "new", forbids=("konomi.lovers",))),
    n("lovers", "Konomi", '''"I kept remembering the things I had planned to tell you. Very small things, mostly. I would think that you would be amused, then remember why I had not sent the note."
{n}She looks at your hand resting beside the chair arm.{/n}
"I am still angry about some of it. I did not want to discover that being right to feel angry required me to stop wanting your company."
{n}She lays her hand beside yours.{/n}
"I wanted it."''',
      c('[Take her hand.]', "near", flags=("konomi.before_road_hand",)),
      c('"You can have my company without having to settle every feeling tonight."', "talk")),
    n("new", "Konomi", '''"I nearly asked you to come earlier so that I could pretend this was an ordinary afternoon."
{n}She gives a short laugh at herself.{/n}
"I have become very accomplished at choosing what an invitation appears to mean. I would like to be less accomplished at it for a while."
{n}She turns toward you.{/n}
"I am attracted to you. I am leaving Drezen. I have not managed to make either fact conveniently smaller."''',
      c('"I am attracted to you too. May I come closer?"', "near", flags=("konomi.before_road_hand", "konomi.private_interest", "konomi.attracted")),
      c('"I would like us to take our time, even with the journey ahead."', "talk")),
    n("near", "Konomi", '''{n}She closes the space between your hands and draws her chair nearer. One of its legs catches on the edge of the rug. She looks down at it with such frank annoyance that you both laugh.{/n}
"A useful interruption. I was in danger of making this unbearably solemn."
{n}This time she moves the chair carefully. Her knee rests against yours.{/n}
"There."''',
      c('[Kiss her.]', "kiss"),
      c('[Stay close and keep talking.]', "talk")),
    n("kiss", "Konomi", '''{n}She meets you before you have quite closed the distance. Her hand slips to the back of your neck, holding you close for a moment after the kiss would otherwise have ended.{/n}
{n}When she draws back, she does not release you at once.{/n}
"I cannot think of a useful remark."
{n}Her thumb brushes the edge of your collar.{/n}
"You may make that difficult for me again."''',
      c('[Kiss her again, then stay close.]', "talk", flags=("konomi.before_road_kissed",)),
      c('"I would rather know what you are thinking now."', "talk", flags=("konomi.before_road_kissed",))),
    n("talk", "Konomi", '''{n}She leaves the traveling case where it is. Beyond the window, the sweeping stops; for a little while neither of you supplies another sound.{/n}
"I will not ask you to make the road disappear," she says at last. "I have things to do in Nerosyan. I would like to know what we intend to do about the distance."''',
      c('"Keep writing. Tell me when you expect to return, and I will tell you when I can meet you."', "letters", flags=("konomi.private_letters",)),
      c('"I care for other people too. I want to keep a place for you without offering a promise that erases them."', "others", flags=("konomi.private_letters", "konomi.private_other_promises"))),
    n("letters", "Konomi", '''"I can do that. I may write too much when I am irritated. You may tell me which pages you enjoyed most."
{n}She looks at the case.{/n}
"Do not leave every invitation for the day when there is nothing inconvenient about it. We will become very dignified correspondents and never see one another."
{n}Her hand rests near yours again.{/n}
"Ask when you want me there. I will answer when I can."''', c('[Agree to keep asking honestly.]', "finish")),
    n("others", "Konomi", '''"Then make the invitation you can keep."
{n}She considers you for a moment.{/n}
"I have never had exclusive possession of your time. I would like the part you offer me to be real. If you must change a plan, tell me before I have spent an evening inventing explanations for an empty chair."
{n}She touches your hand lightly.{/n}
"I am choosing this with you. I am not asking you to make somebody else's affection disappear to improve the description."''', c('"You will have an honest answer from me."', "finish")),
    n("finish", "Konomi", '''{n}The conversation lasts until the lamp needs tending. Konomi gets up to trim it, then returns to her chair.{/n}
"I would like you here for a little longer."
{n}The traveling case waits with its straps unfastened. She leaves it that way while you stay.{/n}''', c('[Stay for the rest of the evening.]', flags=("konomi.before_road_kept",))),
], requires=("konomi.carriers_inspected",))

s("private_departure", "A place on the wagon", [
    n("start", "Narrator", '''{n}The two wagons are loaded when you reach the yard. Selis stands beside the nearer one, reading a list while Vanna touches each fastening in turn. At the end of every line, Selis waits for a nod before reading the next.{/n}
{n}Konomi's case is secured behind the driver's bench. She stands beneath it with a smaller bag over her shoulder. When she sees you, she steps away from the wheel.{/n}
"You found us. I have discovered that departures are announced several times before anybody actually leaves."
{n}A horse stamps behind her. She moves another pace, bringing you with her by a light touch on your sleeve.{/n}
"That one appears to share my impatience."''',
      c('"You sound ready."', "ready"),
      c('"I wish we had another evening."', "evening"),
      c('[Explain that you cannot stay for the departure.]', abort=True)),
    n("ready", "Konomi", '''"I am. It is possible to want to leave a city and dislike leaving somebody in it. I have had ample opportunity to establish that distinction."
{n}She checks the fastening on her bag, finds it secure, and takes her hand away.{/n}
"The capital will be less impressed by my arrival than I once imagined. That may be useful. I can find out who wants my judgment when I am no longer carrying an appointment from the council."''', c('"Whom will you approach first?"', "capital")),
    n("evening", "Konomi", '''"So do I. I am trying to avoid turning that into a reason to delay the wagon. Selis has already had to apologize for one impossible date."
{n}She looks toward the driver's bench, then back at you.{/n}
"I enjoyed the one we had. I would rather leave wanting another than stay until I resent the things I have put off to obtain it."''', c('"What are you hoping to do when you arrive?"', "capital")),
    n("capital", "Konomi", '''"I shall send three letters. One to a woman who used to ask for my advice and then present it at meetings as her own. One to a woman who disagreed with nearly everything I said but always read it. The third will depend on how those two answer."
{n}She notices your expression.{/n}
"Yes, the first may be pleased to hear from me. No, I have not forgotten. There is a difference between making use of a contact and mistaking her for a friend."
{n}Behind her, Vanna tests the step beneath the bench with her boot.{/n}
"I want work that requires me to be good at it. I do not yet know who will offer that. I would prefer you to hear the uncertainty from me before I learn how to describe it more elegantly."''',
      c('"Write about the refusals too. You do not have to impress me in every letter."', "refusals", flags=("konomi.departure_plain_letters",)),
      c('"I want to hear what you make of them. Especially the woman who always read your arguments."', "arguments", flags=("konomi.departure_arguments",))),
    n("refusals", "Konomi", '''"I should like to impress you in some of them. Allow me that much vanity."
{n}Her smile softens.{/n}
"But yes. If the first reply is a refusal, you will receive an account of it. I may spend a page demonstrating that it was a foolish refusal before I admit it stung."''', c('[Ask where to send your answer.]', "address")),
    n("arguments", "Konomi", '''"She once returned six pages with a seventh explaining the question I should have answered. I was furious. I kept the letter."
{n}She lifts her bag slightly.{/n}
"It is in here. I thought I might read it on the road, when I cannot immediately write something ill-considered in reply. You shall hear whether the intervening years have improved either of us."''', c('[Ask where to send your answer.]', "address")),
    n("address", "Konomi", '''{n}She gives you a folded sheet with your name on the outside.{/n}
"The address is Selis's receiving agent in Nerosyan. She has agreed to hold my letters until I have rooms and can send you a better one. Nothing addressed to the council, please. I would like the woman who opens it to be me."
{n}The driver calls her name. Konomi raises a hand to show she heard, but stays with you.{/n}
"I will write after I arrive. If the journey takes longer than we hope, an empty postbag will mean exactly that. You need not construct an entire quarrel out of it."
{n}Her mouth quirks.{/n}
"That warning is partly for my own benefit."''',
      c('[Ask for a farewell kiss.]', "kiss", requires=("konomi.before_road_hand",)),
      c('[Offer your hand and wish her a good journey.]', "hand")),
    n("kiss", "Konomi", '''"Yes. Before they begin a third inspection of the harness."
{n}She puts her bag down and steps close. Her kiss is brief at first; then she catches your sleeve and returns for another, less easily mistaken for a polite goodbye.{/n}
{n}When she bends to pick up the bag, Selis becomes conspicuously interested in the cargo list. Konomi sees her and lifts one eyebrow.{/n}
"I believe we have delayed the inspection sufficiently."''', c('[Walk with her to the wagon.]', "leave", flags=("konomi.departure_kissed",))),
    n("hand", "Konomi", '''{n}She takes your hand in both of hers.{/n}
"And you. Whatever happens before I write, I hope there will be something in your answer that you enjoyed living through."
{n}She holds on for a moment longer, then releases you to settle the bag on her shoulder.{/n}
"Come. I would like to reach the step before Vanna decides to test it again."''', c('[Walk with her to the wagon.]', "leave")),
    n("leave", "Narrator", '''{n}Konomi climbs onto the bench and settles her bag between her feet. Selis checks the list once more, folds it, and climbs up beside her. Vanna takes the second wagon.{/n}
{n}The first wheel jolts across the rut by the gate. Konomi catches the side of the bench with one hand, then looks back to see whether you noticed. You did. She shakes her head at your expression and raises her free hand.{/n}
{n}You watch until the wagons turn out of sight. The folded address remains in your hand. For once, the next message has somewhere ordinary to go.{/n}''',
      c('[Keep the address for your reply.]', flags=("konomi.private_departed", "konomi.private_address"))),
], requires=("konomi.before_road_kept", "konomi.private_letters"), delay=24)

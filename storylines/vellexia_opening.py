"""Optional living-manor interlude before the native Battlebliss invitation.

The native three dates, departures, victims and rewards remain untouched.
"""
from story_format import c, n, scene

UNIT = "a32a07903e428d34cb0e98a804d40569"
AREA = "8217b05e37078414981d994151f0ffb1"
ANSWER_LIST = "7f394dd6cd32c44408a59bd08eb1512a"
ETUDES = {
    "vellexia.dead": "72e423c719ed9d44fa432a6b9629babd",
    "vellexia.early_fight": "eef93f5400704a0fa3e4820cc62282b3",
    "vellexia.final_fight": "b5ed357e0f654a6bbd45ef9f74b10f00",
}
SEEN_CUES = {
    "vellexia.greeted": ["3850d7abe56fba24fb5acb4b8e0767a6"],
    "vellexia.arena_invited": ["746af280c4d1daa47afbb44c7f8b2eea"],
}
COMPLETED_QUESTS = {"vellexia.native_finished": "820f28d6776755d47a2169e2851e15ca"}
RELATIONSHIP = dict(
    Title="The unfinished likeness",
    Description="Vellexia has offered me a private wager about a portrait. Her interest is flattering, expensive, and unlikely to stay still.",
    Objective="Return to Vellexia's gallery",
    Guidance="Speak to Vellexia in her manor before accepting her Battlebliss invitation. These optional visits need her living original manor actor during her initial manor window. The six parts have no required wait and can be played in one extended visit. Accepting Battlebliss pauses this interlude pending a later continuation; it does not erase progress. Her native dates remain separate.",
    StartedFlag="vellexia.started", ClosedFlag="vellexia.closed", CommittedFlag="vellexia.committed",
    UnavailableFlags=["vellexia.dead", "vellexia.early_fight", "vellexia.final_fight"], FailureFlags=[],
)
SCENES = []


def s(id, title, entry, nodes, requires=(), delay=0):
    for page in nodes:
        page["Portrait"] = page["Portrait"] or "Vellexia"
    SCENES.append(scene("vellexia." + id, title, "Vellexia", 4, entry, nodes,
        Relationship="vellexia", ContactUnit=UNIT, Chapters=[4], last=4,
        Areas=[AREA], AnswerLists=[ANSWER_LIST],
        requires=("vellexia.greeted", *requires),
        forbids=("vellexia.dead", "vellexia.early_fight", "vellexia.final_fight", "vellexia.closed", "inhuman", "vellexia.arena_invited", "vellexia.native_finished"),
        optional=True, delay=delay))


s("unfinished_likeness", "The portrait that arrived early", '"What has caught your interest today?"', [
    n("start", "Vellexia", '''{n}Vellexia turns a narrow silver bracelet around her wrist. Its clasp clicks once, then again. At your question her fingers stop.{/n}
"A hopeful opening. Most people begin by telling me what ought to interest me."
{n}She leads your gaze toward a picture standing backward against a low table. Its frame is dark, plain wood, conspicuously severe among the room's ornaments.{/n}
"That arrived this morning. An artist promises that it will reveal a part of me I have never seen. A modest undertaking. I believe he allowed himself three days."
"Have you looked?"
"Of course. I saw an extremely handsome woman looking as though somebody had promised her a revelation. So far, the picture is admirably accurate."
{n}She studies you over the bracelet.{/n}
"Would you like to be useful, or would that ruin your entrance?"''',
        c('"I would like to see what disappointed you."', "warning"),
        c('"I would rather return when I have time to disappoint you properly."', abort=True), portrait="VellexiaManorSpeaker"),
    n("warning", "Narrator", '''{n}She puts the bracelet down beside the picture. The movement is unhurried. A small space on the table has already been cleared for your hands.{/n}''',
        c('"Jerribeth warned me that pleasing you yesterday might not help today."', "jerribeth", requires=("vellexia.introduced",)),
        c('"What exactly did the artist promise?"', "terms", forbids=("vellexia.introduced",))),
    n("jerribeth", "Vellexia", '''"Did she? How considerate. I hope she made me sound considerably more dangerous than a dissatisfied purchaser."
"She did."
"Then she has not wasted your time."
{n}Vellexia's smile sharpens.{/n}
"Jerribeth has excellent taste in dangerous company. Do try to justify her recommendation. I should hate to tell her she wasted a warning on someone who bores me."
"I can answer for myself."
"A claim worth testing. Let us begin with something small enough to survive the test."
{n}She rests one finger on the back of the frame.{/n}''', c('"Tell me about the promise."', "terms"), portrait="VellexiaManorSpeaker"),
    n("terms", "Vellexia", '''"He said it would surprise me. I asked whether he meant once or whenever I looked. He said whenever. Such a lovely, ruinous word."
"And you paid him?"
"Half. The rest depends on my satisfaction. He also insisted the workings were his secret. I agreed to leave them alone until he returned."
"You want me to break that agreement for you."
{n}She laughs, delighted by how quickly you have reached the possibility.{/n}
"I want to discover whether you would. But no. Today I want you to look. You have had fewer centuries to practice being disappointed. Perhaps you will notice what I am overlooking."
"What happens to him if I don't?"
"He will leave without the second half of his fee. I have other uses for my temper. If he is wise, he will not try to collect those instead."
{n}She turns the frame toward you.{/n}''', c('[Examine the picture without opening the frame.]', "picture"), portrait="VellexiaManorSpeaker"),
    n("picture", "Narrator", '''{n}Vellexia's painted likeness stands in a room you do not recognize. Her dress is white; one sleeve has slipped to the elbow. The expression is so openly pleased that for a moment the portrait seems more intimate than a naked figure would have been.{/n}
{n}Then you notice the room. Its window shows a sky that could belong to Golarion. The table holds a cup with a chipped rim. Nothing in it is magnificent enough for the woman standing there.{/n}
"Well?" {n}asks the actual Vellexia.{/n}
"The room is very ordinary."
"To you, perhaps. To me it resembles an industrious attempt at an insult."''',
        c('[Look back at the picture.]', "picture_changed"), portrait="VellexiaPaintingDay"),
    n("picture_changed", "Narrator", '''{n}You look back. The cup is whole. The sky has darkened. The woman now wears an expression of faint impatience.{/n}
"It changed."
"Yes. It is very good at agreeing that something ought to change. I am less convinced it knows what."''',
        c('"It may be showing what the person looking expects to see."', "expectation"),
        c('"Then make a wager with me. Let us find something it cannot flatter."', "wager"), portrait="VellexiaPaintingChanged"),
    n("expectation", "Vellexia", '''"Then it has made the same mistake as half the people who visit me. It has confused attention with service."
"You asked it for a surprise."
"I did. It has offered me my own impatience in a new dress. I already have mirrors, darling. Excellent ones."
{n}She looks at the picture again. The painted woman folds her arms a moment before Vellexia does.{/n}
"There. That is new. It has begun taking liberties with the order of events."
"Or you followed it."
{n}She lowers her arms. The painted woman does not.{/n}
"You may be worth an afternoon. He is waiting nearby. Give me a moment to ask what he thinks he has sold me, then join me by the picture."
"Will he have a chance to answer?"
"A generous one. I want to hear him invent the explanation."
{n}She turns the picture away before it can imitate her smile.{/n}''', c('"I will return to hear it too."', flags=("vellexia.gallery_invited", "vellexia.noticed_expectation")), portrait="VellexiaManorSpeaker"),
    n("wager", "Vellexia", '''"You offer to defeat a picture. How refreshing. Most warriors require a larger audience."
"You would be the audience."
"Flattery already? We have barely begun."
{n}She takes the bracelet from the table, then thinks better of putting it on.{/n}
"Very well. Find the flaw, and I shall answer one question plainly. Fail, and I shall ask mine, and you will answer it. Do make it an interesting failure."
"And if I would rather lose than answer?"
"Then you will have lost twice, darling, and I shall know which question frightened you. Keep a little courage."
"That is my wager."
{n}Her gaze holds yours long enough for the smile to become a decision.{/n}
"Accepted. I shall ask the artist to explain his triumph. He is waiting nearby. Join me again when he has finished, if I have not ceased believing he has one."
{n}She turns the picture toward the wall.{/n}''', c('"Leave the back closed until we can examine it together."', flags=("vellexia.gallery_invited", "vellexia.question_wager")), portrait="VellexiaManorSpeaker"),
], delay=0)


s("second_painter", "A seam in the surprise", '"Has your artist explained the portrait?"', [
    n("start", "Vellexia", '''{n}The artist has withdrawn to the entrance hall after his explanation. Vellexia occupies his empty chair with the air of someone who has found a better use for it.{/n}
"He explained everything. It took a considerable time. I learned that only a vulgar mind would ask how the work was made, and that a sophisticated purchaser would be content to pay the balance."
"What did you say?"
"That I was considering a vulgar mind's opinion. Yours, specifically. He became much more accommodating."
{n}The picture lies face down. A small brass key rests across its back.{/n}
"He surrendered the key. I found that much wiser than his explanation. He will return for the balance or the picture. Astonishingly, he left with all his fingers; I considered mentioning it in his receipt."
"You sound disappointed."
"I am waiting to discover whether his picture is more ingenious than his excuses."''',
        c('[Open the back and examine the enchantment.]', "work"),
        c('"Keep the key. I cannot stay long enough to do this carefully."', abort=True)),
    n("work", "Narrator", '''{n}The key releases four tiny catches. Inside the frame, silver wire surrounds a pale stone no larger than a fingernail. Beneath the stone lies an older panel, its edges shaved down to fit. The newer paint has seeped through a narrow crack and dried against the wood.{/n}
{n}Vellexia leans beside you, close enough that the loose end of her hair touches your sleeve.{/n}
"A picture inside a picture. How economical."
"You think he copied someone."
"Everyone copies someone. I object when they charge me for having invented the ancestor."
{n}The wire carries a fine vibration. Looking too closely at the stone gives you the uneasy impression that someone is looking back from the wrong direction.{/n}''',
        c('[Knowledge: Arcana] Trace how the newer enchantment uses the older panel.', check=dict(Skill="SkillKnowledgeArcana", DC=28, Success="found", Failure="missed", CommanderOnly=True)),
        c('"Ask the artist to name the older work and open it himself. We need not guess."', "ask")),
    n("found", "Vellexia", '''{n}The older panel holds the receptive charm. The newer wire does not create its images. It suppresses some of them and brightens others, directing what the viewer notices. You point out two junctions where the newer work crosses the old.{/n}
"He has taught it to flatter."
"More precisely, he has taught it which answers to hide."
{n}Vellexia's amusement vanishes for a moment.{/n}
"How diligent of him. I buy a surprise, and he kindly spares me the shock of receiving one."
{n}She examines the junctions without touching them. You follow the wire to an adjustment hidden beside the catch. There are three small notches. It has been set to the last.{/n}
"Can it be changed?"
"Yes. I would begin with the middle notch. The original might be overwhelming without any restraint."
"Such a sober recommendation. I wonder how long it will survive my curiosity."
{n}For now, she accepts it. You move the catch once. The painted surface gives a soft crackle, then settles.{/n}''', c('[Close the frame at the tested setting.]', "found_end")),
    n("missed", "Narrator", '''{n}You follow a loop of wire toward the pale stone and mistake a binding for an adjustment. The moment you touch it, white light spills from beneath the face-down picture across the table.{/n}
{n}Vellexia catches your wrist before you move the wire farther.{/n}
"Enough. If we want a blank wall, I own several."
{n}You take your hand away. With her help, you lift the open frame upright and look around its edge. The light across the painted surface recedes slowly. The older panel has become visible through the newer painting, overlapping a mouth with a window and a hand with an empty chair.{/n}
"I thought that controlled the image."
"It did. You controlled it very badly."
{n}She releases your wrist and watches the next movement of your fingers with undisguised suspicion.{/n}
"We will ask him to separate the workings. In front of us. Your mistake has made his economy rather conspicuous. That may prove useful even if your expertise does not."''', c('[Replace the back without touching another wire.]', "missed_end")),
    n("ask", "Vellexia", '''"You decline to be impressive?"
"I decline to damage something merely to avoid asking a question. He knows how he assembled it. Let him show us."
"He may lie."
"Then we can compare what he says with what he does."
{n}She watches your hand leave the wire alone.{/n}
"A disappointingly durable answer. Very well. He will demonstrate the joining when he returns. I shall ask him to bring the price of the old panel as well."
"Why?"
"Because he will expect an argument about beauty. I would like to hear him explain a bill."
{n}She gives you the back of the frame to hold while she checks that nothing has shifted.{/n}
"You have deprived me of an accident. Try to provide a worthwhile conversation in compensation."''', c('[Help close the frame for the demonstration.]', "asked_end")),
    n("found_end", "Vellexia", '''{n}When you turn the closed frame toward you, the picture shows a woman looking toward an open door. Beyond it there is another room, almost bare. She has one foot on either side of the threshold.{/n}
"Better," {n}Vellexia says.{/n}
"Do you recognize it?"
"I recognize the impulse. I have left more interesting rooms than that one."
{n}She reaches past you to turn the frame, then stops with her arm close against yours.{/n}
"Leave it. I would like to discover whether it changes before he arrives. Give him a little time to prepare his account. Then we shall decide what to tell him he has made."
"You know what he made."
"Yes. I have not yet decided how much he should regret telling me otherwise."''', c('"I will return for that conversation."', flags=("vellexia.panel_examined", "vellexia.panel_found"))),
    n("missed_end", "Vellexia", '''{n}The double image remains. Vellexia tilts her head to study the misplaced mouth.{/n}
"It is almost good. How irritating for him if your accident proves the most original part of his work."
"You could tell him that."
"I certainly shall. The question is whether to do so before or after I ask him to mend it."
{n}She hands you the key.{/n}
"Put it beside the frame. He will be ready shortly. Stay for the answer if you can. I want someone present who remembers which mistake was his."
"And which was mine?"
"Darling, I will remember yours."''', c('[Set the key down and accept the appointment.]', flags=("vellexia.panel_examined", "vellexia.panel_missed"))),
    n("asked_end", "Vellexia", '''{n}Vellexia closes the catches herself. She leaves the key in the last one, projecting from the frame like an accusation.{/n}
"There. He cannot complain that we failed to invite him to explain himself."
"You might let him finish a sentence."
"I might let him finish several. That will depend on the sentences."
{n}She rises and smooths her dress. For a moment her attention rests on you instead of the picture.{/n}
"We shall hear him shortly. I want to know whether your caution was judgment or merely a fortunate lack of nerve."
"Would you accept that it might be both?"
"From you, perhaps. From him, I intend to demand a price reduction."''', c('"Leave him a chance to answer, then."', flags=("vellexia.panel_examined", "vellexia.panel_asked"))),
], requires=("vellexia.gallery_invited",))


s("price_of_novelty", "The artist's second account", '"What did the artist admit?"', [
    n("start", "Vellexia", '''{n}A thin stack of papers lies beside the portrait. Vellexia holds the uppermost sheet by its corners, keeping it away from her drink.{/n}
"He brought a history of the work. It is wonderfully detailed. The first page says that purchasing a discarded experiment and changing its frame can be understood as a creative act."
"Can it?"
"Certainly. Claiming to have invented the experiment was less creative. He has apologized for the confusion. I have assured him that I was never confused."
{n}She lowers the paper.{/n}
"He is waiting for my answer in the entrance hall. Alive, unpaid, and at present untransformed. You may stop counting the furniture."
"I was counting the exits."
"Then we have both been attentive."''', c('[Ask about the demonstration.]', "history"), c('"I cannot stay for the decision. Make no bargain in my name."', abort=True)),
    n("history", "Narrator", '''{n}She has left the frame open so you can compare its present state with what you saw before.{/n}''',
        c('[Examine the adjustment you identified.]', "found", requires=("vellexia.panel_found",)),
        c('[Look for the repair to the doubled image.]', "missed", requires=("vellexia.panel_missed",)),
        c('[Ask what he demonstrated when he opened it.]', "asked", requires=("vellexia.panel_asked",))),
    n("found", "Vellexia", '''"You were right about the suppressing charm. He admitted that much before I finished pointing at it. A pity. I had prepared an excellent expression for his denial."
{n}She sets one fingernail beside the middle notch.{/n}
"The earlier maker wanted a portrait that could contradict its subject. Our enterprising guest improved it by hiding the contradictions he thought I would dislike."
"He was afraid of you."
"And dishonest about what his fear had produced. I pay for good work, not for the honor of reassuring somebody while he sells me bad work."
{n}The image behind her shifts. She lets it change without turning.{/n}''', c('"What is your answer to him?"', "answer")),
    n("missed", "Vellexia", '''"He repaired the binding you loosened. Then he discovered that the image beneath it was more difficult to explain than the damage."
"Did you tell him who damaged it?"
"Yes. I wanted his embarrassment properly distributed. He cannot blame your fingers for the age of the lower panel."
{n}She turns the frame enough for you to see that the doubled mouth is gone.{/n}
"He has left the suppressing charm loose enough to admit some of the older images. I am almost sorry. The mouth in the window was more disturbing than he intended."
"You could have asked him to keep it."
"I did. He looked so offended that I became fond of the idea. Perhaps another day."''', c('[Hear the decision she is considering.]', "answer")),
    n("asked", "Vellexia", '''"He demonstrated that the upper charm filters the lower one. Then he demonstrated that he could talk very quickly while doing it. I preferred the first performance."
"Did he name the earlier maker?"
"An abandoned workshop, a dead creditor, several inconvenient changes of ownership. He may even have been truthful. His bill certainly looked old enough to resent being disturbed."
{n}She taps one line on the paper.{/n}
"He will write that history down without the compliments to his own ingenuity. If he wishes to charge for his alterations, he may describe them as alterations. A terrible burden."
"You have already chosen."
"I have chosen what I believe. What I do with it is still available for discussion."''', c('"Then tell me the choices."', "answer")),
    n("answer", "Vellexia", '''"I could keep it at a lower price. He would receive enough to dislike the bargain and too much to complain honestly. Or I could send it back and let him explain to his next purchaser why I refused it."
"You make both sound unpleasant."
"They are unpleasant. He attempted to sell me my own vanity as a discovery. I do not intend to thank him."
{n}She studies the picture, then you.{/n}
"But you have been entertaining, and I would like your preference before I give mine. Keep the disappointing object and learn what it can do, or enjoy the cleaner pleasure of sending it away?"
"Will my answer decide his safety?"
"No. He is worth considerably more alive, to hear what I tell his next patron about him. How fortunate for him."
{n}Her tone makes his survival sound like a whim she has not yet tired of.{/n}''',
        c('"Keep it, with the account corrected. I want to see what the older work was trying to do."', "keep"),
        c('"Return it. If he wants you as a patron, let him bring something he can describe honestly."', "return")),
    n("keep", "Vellexia", '''"Curiosity defeats indignation. I approve, though I would have enjoyed a little more indignation first."
{n}She writes a figure on the bottom of the paper and pushes it away.{/n}
"The remainder of his fee. Reduced, as promised. If he accepts, the picture stays. If he refuses, he takes it away and we find a better occupation."
{n}She carries the paper to the entrance herself. You hear a short conversation, an objection cut off by laughter, and finally the sound of the outer door.{/n}
{n}When she returns, she carries only the key.{/n}
"He accepted. I have purchased a flawed invention with an accurate label. My reputation may never recover."
"You could keep the label on the back."
"And deprive myself of hearing visitors misunderstand it? You are not always as imaginative as you appear."
{n}She puts the key beside your hand.{/n}
"Next time we shall try looking together. I suspect it will find that much less comfortable."''', c('"Keep the key here. I will return."', flags=("vellexia.price_settled", "vellexia.kept_picture"))),
    n("return", "Vellexia", '''"A remarkably expensive way to preserve a standard. I like it better when somebody else proposes it."
{n}She rises and calls the artist to collect the frame. You remain where you can see the doorway. He enters, wraps the picture, and leaves with the papers tucked beneath it. His complaint about the unpaid balance ends when Vellexia asks him to read the original promise aloud.{/n}
{n}After the outer door closes, she returns to the empty table.{/n}
"Gone. I find that I wanted the picture more once I had decided to refuse it. An irritating discovery. You owe me another."
"I did not make the promise on the receipt."
"No. You made yourself interesting while I was reading it. That is less enforceable, and far more dangerous to you."
{n}She draws a chair toward the cleared space.{/n}
"Come back. We shall attempt a portrait without purchasing another artist's disappointment."''', c('"I will come back to see what you mean."', flags=("vellexia.price_settled", "vellexia.returned_picture"))),
], requires=("vellexia.panel_examined",))


s("two_observers", "The view from the other chair", '"What do you intend to try today?"', [
    n("start", "Vellexia", '''{n}Vellexia has placed two chairs opposite one another. Between them stands the low table, cleared of drinks and ornaments.{/n}
"Sit. No, whichever chair you prefer. I have not concealed a moral lesson beneath either cushion."
"That leaves a great many other possibilities."
"It does. How pleasant to be understood."
{n}She waits until you choose before taking the other place. Her dress is a deep red today, simple enough to draw attention to the precision of its fit.{/n}
"We have spent a considerable time describing somebody else's failure. I am becoming curious about what you would call a success."
"A picture that surprises you?"
"For a beginning. After that I might become more demanding."''', c('[Look at what she has prepared.]', "object"), c('"Then save the demands until I can stay."', abort=True)),
    n("object", "Narrator", '''{n}She has arranged the afternoon according to the decision you made together.{/n}''',
        c('[Turn the retained picture so both of you can see it.]', "kept", requires=("vellexia.kept_picture",)),
        c('[Ask how she intends to make a likeness without the returned picture.]', "returned", requires=("vellexia.returned_picture",))),
    n("kept", "Vellexia", '''{n}The picture shows Vellexia seated alone. As you move it, another chair appears at the painted table. Its occupant is a blur. You cannot tell whether the uncertainty belongs to the work or to the people looking.{/n}
"It is hesitating," {n}she says.{/n} "Apparently we disagree."
"About what?"
"How close the chairs ought to be, for one thing. Watch."
{n}She moves her own chair nearer. In the picture the distance widens.{/n}
"Now that is rude."
"Perhaps it expects you to leave."
{n}Her gaze turns from the picture to you.{/n}
"Do you?"
"Eventually. I am interested in what you do before then."
"An answer with a modest ambition. I might even be able to meet it."
{n}She turns the frame away, leaving you with the actual distance between the chairs.{/n}''', c('[Let her ask her next question.]', "question")),
    n("returned", "Vellexia", '''"You will describe me. I will tell you which parts sound like a person you have met and which sound like a story somebody sold you."
"You would know which parts you wanted to deny."
"Of course. A portrait sitting requires a little resistance from the subject. Otherwise we might as well commission a tax record."
{n}She settles into her chair, then changes the position of one hand.{/n}
"There. Begin."
"You moved your hand because you saw me notice it."
"A promising accusation. Go on."
"You want to be observed without becoming predictable."
{n}Her fingers stop moving.{/n}
"That sounds like someone who has visited. I dislike it considerably less than I expected. Now let me try you."
{n}She draws her chair nearer, watching whether your attention follows her or stays on the door.{/n}''', c('[Wait for her account of you.]', "question")),
    n("question", "Vellexia", '''"You watch the door. You watch my hands. You also keep coming back. I could flatter myself that the third observation explains the first two, but I would rather hear your version."
"I know you are dangerous."
"Everyone knows that. Most people make a career of pretending they discovered it in private."
"You asked why I return."
"I am allowing you an elaborate approach to the answer. It seems important to your dignity."
{n}She smiles, but does not reach across the table.{/n}
"Tell me something you want, without first explaining why a good person might be permitted to want it. I will attempt to resist correcting your taste."''',
        c('"I want an evening in which I am neither a commander nor an exhibit. I want to find out whether you can offer one."', "ordinary"),
        c('"I want someone who can surprise me without expecting me to surrender my judgment."', "danger")),
    n("ordinary", "Vellexia", '''"An evening without an audience. You propose depriving half the city of an opportunity to envy you. Cruel."
"Would you miss them?"
{n}She begins a ready answer, then stops. The pause is small enough that you might have missed it if she had not been so quick before.{/n}
"Sometimes. I enjoy being seen to enjoy myself. There are pleasures an audience improves."
"This one?"
"I have not decided what this one is."
{n}She moves the table a few inches to one side. The space between the chairs is now unobstructed.{/n}
"We could spend an hour finding out. If it fails, you will have a very exclusive disappointment."
"And you?"
"I shall blame you. Briefly. Then I shall decide whether to invite you again."
{n}She smiles as though the hour is already hers.{/n}''', c('"An hour, then. No audience."', flags=("vellexia.observers_kept", "vellexia.private_hour"))),
    n("danger", "Vellexia", '''"How greedy. You want the edge of the knife and the privilege of examining the handle."
"I prefer knowing who is holding it."
"And if I put it down?"
"I might pay more attention to your hands."
{n}Her laugh is low and sudden.{/n}
"There you are. I had begun to think you would spend the entire afternoon explaining the conditions under which you might enjoy yourself."
{n}She lays one hand palm upward on her knee.{/n}
"I can offer an hour without a performance. You may tell me a story I have not heard. I may tell you something true and quite unsuitable for polite company. Nobody need mistake the exchange for a cure."
"A cure for whom?"
"Whichever of us is foolish enough to want one."
{n}Her open hand remains where it is.{/n}''', c('"I will bring a story, and keep my judgment."', flags=("vellexia.observers_kept", "vellexia.candid_hour"))),
], requires=("vellexia.price_settled",))


s("unadvertised_hour", "An hour with no witnesses", '"You offered an hour without a performance."', [
    n("start", "Vellexia", '''{n}Vellexia receives you beside the open door of a small sitting room. She closes a book as you approach, keeping one finger between its pages.{/n}
"I did. You have arrived almost exactly when I expected you. I shall try not to hold that against you."
"Should I have been late?"
"No. Then I would have resented the waiting. You see what a difficult undertaking you have chosen."
{n}There are two cups on a narrow table. She pours into her own and drinks before offering you the other.{/n}
"Drink, or spend the hour wondering what you refused. I should enjoy either expression."
{n}She takes the chair farthest from the door, which leaves you the one with your back to it.{/n}''', c('[Sit and give her the hour you promised.]', "opening"), c('"I need to postpone. I will ask again when I can keep the appointment."', abort=True)),
    n("opening", "Narrator", '''{n}For a moment neither of you speaks. From elsewhere in the manor comes the distant sound of a door closing. Vellexia glances toward it, then deliberately turns back to you.{/n}''',
        c('"No audience. Are you already missing them?"', "private", requires=("vellexia.private_hour",)),
        c('"I have brought a story. It may disappoint your expectations."', "candid", requires=("vellexia.candid_hour",))),
    n("private", "Vellexia", '''"I was wondering what they would invent about us. I do hope it is something worth denying."
"The door is open."
"A detail that will trouble nobody determined to gossip."
{n}She places the book on the table. You can see writing crowded into the margins, some lines crossed out so fiercely that the paper has torn.{/n}
"My own notes. On an entertainment I found magnificent once and insufferable the second time. I was attempting to discover whether the entertainment changed."
"Did it?"
"Not enough to excuse me. There. A confession. You may embroider it for your diary."
"What was it?"
"A play. Extremely long. Its author survived my first enthusiasm and has been wisely unavailable since my second opinion."''', c('"Tell me what you liked the first time."', "play")),
    n("candid", "Vellexia", '''"Begin. I shall interrupt when I require assistance being impressed."
{n}You tell her about an argument over a seat at supper. By the time everyone had explained why they did not mind where they sat, the food had gone cold and the person who had caused the difficulty was eating comfortably in the kitchen.{/n}
{n}Vellexia asks who owned the house. Then she asks who had been invited twice. Her third question is about the person who left for the kitchen.{/n}
"That one understood the evening. Did they enjoy the meal?"
"More than the people discussing the chairs."
"Then you have brought me a useful tragedy. Its heroes were defeated by soup."
{n}She takes the book from her lap and sets it down.{/n}
"I once adored a play that took considerably longer to make the same point. On the second viewing I wanted to tear the stage apart."''', c('"What changed between the two viewings?"', "play")),
    n("play", "Vellexia", '''"I knew where the clever parts were. I could feel them approaching. I began resenting the audience for laughing a breath later than I did."
"You could have watched them instead."
"I did. That made it worse."
{n}Her smile fades without becoming gentle.{/n}
"Do not offer me patience as though nobody has thought to put it in a cup before. I have practiced patience longer than your oldest monastery has had a roof. Sometimes it works. Then I become aware of practicing it."
"I wasn't going to offer a cure."
"Good. I should hate to discover you had spent all this time preparing a sermon."
{n}She lifts the book, finds the place she marked and reads one line aloud. Without its surrounding scene it is merely an insult, beautifully timed. She laughs at it, surprised by her own amusement.{/n}
"There. That still works. I had forgotten it was there."''',
        c('"Read the next part. I would like to hear you enjoy something."', "read"),
        c('"Leave it there. Let one good line be enough for today."', "leave")),
    n("read", "Vellexia", '''{n}She reads until the insult finds its victim and is returned with interest. She gives the second character a painfully earnest voice, then stops to tell you the actor was even worse.{/n}
{n}You laugh. Vellexia watches you over the top of the page instead of reaching for the next line.{/n}
"You enjoyed that."
"So did you."
"For an instant."
"We have an hour. It can hold more than one kind of instant."
{n}She shuts the book with a finger still inside it.{/n}
"A dangerously persuasive little sentence. I shall remember that you said it when you become tedious."
"I would expect nothing less."
{n}She rests the book on the table and rises, bringing her cup to the chair beside yours.{/n}''', c('[Make room for her.]', "intent")),
    n("leave", "Vellexia", '''"You would dismiss an author after one good line? I may have underestimated your ruthlessness."
"You can read another tomorrow."
"And spoil a perfectly good anticipation?"
{n}She closes the book, this time allowing the marker to remain between the pages.{/n}
"Very well. One line. I dislike how little has happened and how reluctant I am to dismiss it. You may consider that a compliment if you need one."
"I was considering asking you to sit nearer."
{n}Her gaze moves from your face to the empty space beside you.{/n}
"An improvement on explaining why you ought not to ask."
{n}She brings her cup with her and sits within reach.{/n}''', c('[Turn toward her.]', "intent")),
    n("intent", "Vellexia", '''"You have been watching my mouth," {n}she says.{/n}
"You have been watching me notice it."
"Yes. I prefer to know whether my company is attentive."
{n}Her knee touches yours. She leaves it there, then waits.{/n}
"You keep looking at my mouth. Shall I flatter myself, or have you discovered something more amusing to say? I could invent a splendid declaration for you from very little evidence."
"Since when has that stopped you?"
"Since I became curious what you would say before I put the words in your mouth. Do not make me regret the experiment."''',
        c('"I want you. And I intend to make you want another evening."', "court"),
        c('"Another hour. You have not quite tempted me into the rest."', "slow"),
        c('"I enjoy your company. I want to keep this as conversation."', "company")),
    n("court", "Vellexia", '''"How very direct. What an earnest thing to bring into this house."
{n}Two fingers settle on the back of your hand; her smile sharpens as she feels your pulse jump under them.{/n}
"Another hour, then. We shall see whether you can make me begrudge its ending. I have begrudged very few."
"I asked for another."
"And you shall have it. Come back soon. I have begun wondering what I shall do with you, and I dislike wondering for long."
{n}Her fingers slip between yours for a moment before she withdraws them.{/n}
"The answer is probably no. How indiscreet of me to admit it."''', c('"I would rather spend the time with you than outside the door."', flags=("vellexia.hour_kept", "vellexia.courting"))),
    n("slow", "Vellexia", '''"You have an admirable talent for approaching a precipice and asking whether there is a bench."
"Is there?"
{n}She withdraws her knee with a little laugh, as though she has thought of a better temptation.{/n}
"For another hour, yes. I am curious enough to allow an unfinished answer. Do not mistake that for limitless patience."
"I don't."
"Good. Bring that admirable nerve back with you. You used it to disappoint me politely; I have other uses for it."
{n}She picks up her cup. The conversation returns to the play, but she leaves the marked page closed.{/n}''', c('"Another hour. Surprise me."', flags=("vellexia.hour_kept", "vellexia.slow"))),
    n("company", "Vellexia", '''{n}Her expression stills. Then she draws back just far enough to make the new distance unmistakable.{/n}
"A less flattering answer than I had prepared for. How economical of you to surprise me without purchasing anything."
"I would rather be clear."
"Yes, you have made that preference abundantly apparent."
{n}She looks at the book on the table and begins to smile again.{/n}
"Stay a little longer when you can, then. We have an argument about an artist to finish, and I may yet enjoy your company without requiring you to admire mine in quite the way I intended."
"You may?"
"Allow me the dignity of an experiment. You have been granted several."''', c('"I will return for the conversation."', flags=("vellexia.hour_kept", "vellexia.company"))),
], requires=("vellexia.observers_kept",))


s("a_question_kept", "The question she chooses", '"You had another hour for me."', [
    n("start", "Vellexia", '''{n}The sitting room looks almost unchanged. Vellexia has moved the marked book to a shelf and placed a small bowl of dark fruit where it stood.{/n}
"I did. I have spent part of it deciding what to ask you. An inefficient pleasure. I recommend it to anyone with too much time and an inconveniently interesting guest."
"Have you chosen?"
"Nearly. First, we should settle the picture. It would be tiresome to leave a debt wandering about between us, pretending to be mystery."
{n}She indicates the chair you used before. This time her own stands beside it rather than opposite.{/n}''', c('[Sit and settle the old question.]', "wager"), c('"Keep the question until I can stay for the answer."', abort=True)),
    n("wager", "Narrator", '''{n}She remembers the terms on which you first agreed to return.{/n}''',
        c('"We wagered an answer. What do you consider the result?"', "result", requires=("vellexia.question_wager",)),
        c('"We discovered what the artist had hidden. You did not promise me a reward."', "unowed", forbids=("vellexia.question_wager",))),
    n("result", "Vellexia", '''"We discovered that he had suppressed the answers he thought I would dislike. That explains the disappointment rather neatly. You may have the question."
"Even if you helped find the answer?"
"Especially then. I prefer my wagers to produce something worth having. I have had your company and an unusually competent disagreement."
{n}She leans back, apparently at ease.{/n}
"Ask. I should like to discover which question you think worth making me lose. Careful: I remember every question anyone has ever been foolish enough to ask me."
"What would you most enjoy taking from me?"
{n}Her ease changes. Her eyes stay on you, and something behind them has started to count.{/n}
"That is a much better question than whether I have ever loved someone. I had prepared a beautiful lie for that one."''', c('[Wait for the answer she owes.]', "answer")),
    n("unowed", "Vellexia", '''"No. You came back without an enforceable return on your time. That was either generosity or a failure to read the market."
"Perhaps I enjoyed the company."
"An extravagant possibility."
{n}She chooses a piece of fruit, considers it, then puts it back.{/n}
"I have begun wondering what you expect from me. I suspect I could make you regret almost any answer, and I find I would rather hear it first."
"Then let me ask first. What would you most enjoy taking from me?"
{n}She looks at you with a stillness that briefly makes the room seem smaller.{/n}
"You do have a talent for making a modest afternoon expensive."''', c('[Let her decide how plainly to answer.]', "answer")),
    n("answer", "Vellexia", '''"Your attention, darling. Especially the part you meant to spend elsewhere. Your insults, when I bore you, sharp enough to make me consider them. And one surprise you have been foolish enough to keep from me, which I intend to take."
"And when that stops being new?"
"Then I may become unpleasant. I have been unpleasant before."
{n}She does not soften the admission with laughter.{/n}
"I am not offering you a harmless woman who happens to possess an alarming history. You have seen a small part of my house. You should believe what it tells you."
"I do."
"Good. Your attention would be worth less if I had purchased it by pretending otherwise."
{n}She moves the fruit bowl aside, clearing the space near your hand.{/n}
"What would you like from this hour?"''',
        c('"A kiss, if you still want to discover how that earnest word sounds."', "kiss_offer", requires=("vellexia.courting",)),
        c('"Your company close enough that neither of us needs an audience."', "close", requires=("vellexia.courting",)),
        c('"A conversation that leaves the next answer open."', "slow", requires=("vellexia.slow",)),
        c('"A story you would tell someone whose company you want again."', "company", requires=("vellexia.company",))),
    n("kiss_offer", "Vellexia", '''"I do."
{n}The answer comes without ornament. Her hand catches your collar and draws you into a deliberate, possessive kiss.{/n}
{n}Her kiss is warm and deliberate. The pause afterward is more unsettling: she watches your face without speaking, close enough that you can feel her breath when she laughs softly.{/n}
"There. You have made me curious about a second one. An excellent beginning, and a dangerous one for you."
"I noticed the kiss."
"Then I chose well."
{n}She kisses you again before drawing back. Her hand stays at your collar, holding, as though she has decided you are hers to keep there.{/n}
"Stay for the hour. We need not spend it predicting what I shall want tomorrow."
{n}You remain beside her. The next conversation begins slowly, with the fruit she had been too distracted to taste.{/n}''', c('[Stay close and steal another kiss.]', flags=("vellexia.opening_kept", "vellexia.first_kiss"))),
    n("close", "Vellexia", '''"Then come closer. You have been negotiating from a very respectful distance."
{n}She makes room beside her. When you sit, her shoulder rests against yours and her fingers settle lightly around your wrist.{/n}
"This is an unusual way to spend an afternoon here."
"Quietly?"
"Without explaining it to anyone."
{n}She listens to a sound beyond the door, then returns her attention to you. This time she does not tell you what she imagines the rest of the house might think.{/n}
"Tell me about someone who escaped an exhausting celebration. Someone sensible enough to know when to leave. I would like to hear what happened after the victory."
"I can tell you about an argument that ended over food."
"Begin there. I promise nothing about my patience, but you have my attention."
{n}She stays close while you speak, interrupting only when a detail interests her.{/n}''', c('[Tell her the story and enjoy her interruptions.]', flags=("vellexia.opening_kept", "vellexia.held_close"))),
    n("slow", "Vellexia", '''"An unfinished answer. You are becoming consistent, which ought to annoy me more than it does."
{n}She offers you the fruit bowl and takes a piece herself.{/n}
"Very well. Tell me something you changed your mind about. Something small. I do not want an account of how a great battle taught you humility. I have heard enough generals attempt that story."
"Would an opinion about a person do?"
"If the person is me, choose a better disguise."
{n}You begin with an argument you once thought worth winning. She asks what losing would have cost. The question takes the conversation somewhere you had not intended, and she follows with evident interest.{/n}
{n}When the hour ends, she keeps the best part of her own story back for your next visit, and tells you so.{/n}
"You may return," {n}she says.{/n} "With another unfinished thought, if necessary. I reserve the right to finish an argument."''', c('[Promise another visit.]', flags=("vellexia.opening_kept",))),
    n("company", "Vellexia", '''"A story for someone whose company I want again. You make conversation sound like a dangerous commission."
{n}She considers, then begins an account of a noble who paid to have his enemy's name removed from every program at a celebration. The enemy purchased all the empty spaces and left them blank. By midnight, nobody was talking about anyone else.{/n}
"Which one were you helping?"
"At different points, both. I was younger. I considered that an efficient use of an evening."
"And now?"
"Now I would purchase the whole program and let them quarrel over the scraps. Every blank space, and my name in none of them. Nobody would talk of anything else for a year."
{n}She looks toward the cleared table and smiles at a thought she does not share.{/n}
"Come back if you have a better example. I dislike surrendering the last word, but I will occasionally lend it to someone who knows what to do with it."''', c('"I will try to make good use of the loan."', flags=("vellexia.opening_kept",))),
], requires=("vellexia.hour_kept",))

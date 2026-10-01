"""A living Vellexia correspondence campaign after her native peaceful dismissal.

The early token and later rivalry are authored fiction, not native actor recovery.
Remote scenes do not place Vellexia physically in the Commander's camp or capital.
"""
from story_format import c, n, p, scene
from storylines.vellexia_opening import UNIT, AREA, ANSWER_LIST

NEXUS = "7847c3e3537104f4694167af0b9fcd0e"
DREZEN = "2570015799edf594daf2f076f2f975d8"
SEEN_CUES = {
    "vellexia.dismissed_native": ["fa6db1b41f5394f4f8a23f09fc7061f7"],
    "vellexia.coin_given": ["ff7f743740d221b46860f3137299c3d2"],
    "vellexia.mirrored": ["42429350764f92140b293b24039b89ef"],
}
SELECTED_ANSWERS = {"vellexia.native_coercion": "3aa48f68198afe14cb6de752ce80cc8f"}
BLOCKERS = ("vellexia.dead", "vellexia.early_fight", "vellexia.final_fight",
            "vellexia.closed", "vellexia.mirrored", "vellexia.native_coercion", "inhuman")
SCENES = []


# Q11: every native ending of the affair opens the correspondence, not only the bored dismissal (Cue_0076): the mercy
# (Cue_0098, vellexia.spared) and the passionate farewell (Cue_0106, vellexia.farewell). The spared world's final_fight
# lifts through vellexia.fight_survived (spared OR returned), as on the endings.
ENDED = ["vellexia.dismissed_native", "vellexia.spared", "vellexia.farewell"]
SPARED_FO = {"vellexia.final_fight": "vellexia.fight_survived"}


def s(id, title, entry, nodes, previous, chapter=4, local=False, delay=24, chapters=None):
    """chapters (remote only): the Chapters list when it is not just [chapter]. Q11: of the shell calls only the second
    invitation is a Chapter 4 delivery (the R2-5 allowance); the account and the wager follow in Chapter 5, in Drezen."""
    for page in nodes:
        page["Portrait"] = "Vellexia"
    chapters = list(chapters or [chapter])
    extra = dict(Relationship="vellexia", Chapters=chapters, last=max(chapters), optional=True)
    if local:
        extra.update(ContactUnit=UNIT, Areas=[AREA], AnswerLists=[ANSWER_LIST])
        required = ("vellexia.greeted", previous)
        forbidden = (*BLOCKERS, "vellexia.arena_invited", "vellexia.native_finished")
    else:
        extra.update(Remote=True, Areas=[NEXUS if ch == 4 else DREZEN for ch in chapters],
                     RequiresAnyGroups=[list(ENDED)], ForbidOverrides=dict(SPARED_FO))
        required = ("vellexia.native_finished", previous)
        forbidden = BLOCKERS
    SCENES.append(scene("vellexia." + id, title, "Vellexia" if local else "Memory", min(chapters),
        entry, nodes, requires=required, forbids=forbidden, delay=0 if local else delay, **extra))


s("the_unused_reply", "A reply she has not written", '"You said I might return. What if I am somewhere you cannot hear me knock?"', [
    n("start", "Vellexia", '''{n}Vellexia has been selecting rings from a shallow tray. At your question she places two beside each other, studies the effect, and returns one to its compartment.{/n}
"You could write. People do. Some even improve in writing, though the delay deprives me of watching them discover that I disagree."
"Would you answer?"
"What a demanding question to ask before composing a sentence."
{n}She lifts a ring to the light. Its dark stone contains a moving thread of color, which twists when her finger passes over it.{/n}
"There are ways to send a voice," she says. "I own a pair of echo shells. Far less tedious than letters. One can shut them while the admirer is still composing his compliment, and watch his little light go on begging in the dark."
"Your admirers put up with that?"
"My admirers put up with a great deal more. Then they wonder why I grow tired of hearing them."
{n}She closes the ring tray and rests both hands on its lid.{/n}
"You have thought of leaving already. How very mortal. You stand in an interesting room and begin calculating how long it will take to reach another."''',
      c('"Give me a way to call you. I will risk the answer."', "asking"),
      c('"I am curious what you would send when you had time to invent your entrance."', "entrance"),
      c('"We can discuss it another time."', abort=True)),
    n("asking", "Vellexia", '''"Risk. What a delicious word to bring to a woman's ring tray. I have punished people for using it carelessly."
"And when someone keeps you waiting?"
{n}She looks up from the tray.{/n}
"I understand waiting perfectly. It makes me vindictive."
"Then we have something in common."
{n}Her smile appears slowly.{/n}
"A gentleman sends me his likeness whenever he invents a compliment. I have broken three of his messengers, one of them quite thoroughly. He still believes himself irresistible, and considers the broken ones evidence of my passion."
"Did you tell him otherwise?"
"With admirable clarity. He continues to have a poor ear."
{n}She rises and crosses to a cabinet. Its doors stand open; inside are cases too small to hold the grand curiosities displayed elsewhere in the house.{/n}
"Wait there. I have something considerably less tiresome than his likeness, and I want to watch your face when you see what it costs."''', c('[Wait while she chooses something from the cabinet.]', "shell")),
    n("entrance", "Vellexia", '''"Naturally. A letter is an entrance one can rehearse without admitting it."
"You would admit it?"
"To the right audience. A little visible artifice makes the rest easier to overlook."
{n}She leans back, studying you with renewed amusement.{/n}
"I might send a line from that play and discover whether you had the patience to find the insult. Or a description of an evening whose most interesting guest never arrived. You would spend a pleasant moment wondering whether I meant you."
"Then I might ask."
"And spoil all that excellent uncertainty? You are determined to be an expensive correspondent."
{n}She rises and crosses to a cabinet of small cases. Her fingers hover over one, then choose another.{/n}
"I insist upon being able to silence it. Even your voice may become tedious, sweetheart, and I should hate to have to break you the way I broke his messengers."''', c('[Watch what she takes from the cabinet.]', "shell")),
    n("shell", "Vellexia", '''{n}She returns with two palm-sized shells set in silver rims. Each has a hinged cover of cloudy glass. When she opens one, its hollow gives back the quiet sound of her fingernail against the table.{/n}
"An echo pair. Made for a collector who wanted to hear the sea without visiting it. A mistake. The sea is enormously repetitive."
"Who made them?"
"An expensive craftswoman. She understood exactly what I wanted, which was a delightful novelty in a craftswoman. Before you ask: no, nobody is inside them. Shells, silver, and a fee she still boasts about."
{n}She opens the other cover. Her next word sounds beside your hand as well as across the table. When she closes your shell, the second voice stops.{/n}
"Open the cover when it glows. If I am inclined to hear you, you will hear me. If I am not, you may watch the little light and wonder what I am doing instead."
"And when I close it?"
"You become unavailable. An accomplishment some of my guests have spent centuries failing to achieve."
{n}She turns your shell so its hinge lies away from you.{/n}
"We would have to bind the pair to our voices. I cannot promise every plane or every obstruction would permit an answer. Nor shall you assume that a closed shell means a broken one. I may simply have better company."''',
      c('"Then let us test it before we decide."', "test"),
      c('"Keep it for now. I want to think before accepting."', abort=True)),
    n("test", "Narrator", '''{n}You each speak a short phrase into one shell. Vellexia chooses your name with a small, deliberate change in emphasis. You choose hers. She watches your mouth while you say it, then lowers her gaze to the light gathering under the cloudy glass.{/n}
{n}She goes to the far side of the sitting room and closes her cover. Your first request produces no answering voice. A moment later the light in your shell dims. She has declined it.{/n}
"Cruel already?" you call across the room.
"Thorough. Try again."
{n}This time she opens the cover. The glass clears to show a small image of her face. Her voice sounds close, but her body remains across the room, one hand resting on the cabinet. You ask her to close it while you are speaking. The sound stops in the middle of a word and the glass clouds again.{/n}
{n}She waits with visible impatience for your cover to open, then finishes the insult you interrupted.{/n}
"I was about to tell you which word I disliked. You may have saved yourself a considerable explanation."
{n}You shut your cover. Her real laughter crosses the room without assistance.{/n}''', c('[Open it once more and finish the test.]', "choice")),
    n("choice", "Vellexia", '''"It works," she says. "Now we may decide whether that was a sensible discovery."
{n}She puts your shell into a narrow case and slides it toward you, watching your hand rather than your face.{/n}
"Take it. I should like to discover whether your voice can amuse me without the rest of you to distract me. If it cannot, I shall know very quickly, and so will you."
"And what do you want now?"
"To discover whether you can interest me without the advantage of standing where I can touch you."
{n}The words are teasing; the attention behind them is not casual.{/n}
"There is also an opinion I may want. An old acquaintance has begun selling predictions about other people's tastes. He claims he can tell a patron what will delight them before they have chosen it. His own conversation is exquisitely predictable. I am considering whether to make that public."
"You want a collaborator."
"Possibly. I have not yet decided whether he is worth the inconvenience. You will be disappointed to learn that my gifts occasionally precede my schemes."
{n}She slides the case within reach.{/n}''',
      c('"I will take it. Ask when you have something you want me to hear."', "accepted"),
      c('"I would rather leave it here today."', abort=True)),
    n("accepted", "Vellexia", '''{n}You take the case. Vellexia watches you close it, then puts her own shell beside the ring tray.{/n}
"No speech?"
"Would you like one?"
"I was preparing to dislike it. You have left me an unexpected interval."
{n}She draws you close enough to take a pale thread from your shoulder. Once it is gone, her hand remains there for a moment.{/n}
"Our next meeting can still be somewhere with other people. I have not renounced the pleasure of being seen with an interesting guest."
"And if you cease finding me interesting?"
"Then I may leave the cover closed. You should believe that answer even when you enjoy the voice giving it."
{n}She lets her hand fall.{/n}
"Before you go, look at what that prediction seller sent me. I require a second audience for my disgust, and I have decided it will be you."''',
      c('[Keep the echo shell and accept another look at the seller\'s claim.]', flags=("vellexia.seal_agreed",))),
], "vellexia.opening_kept", local=True)

s("the_price_of_tomorrow", "A taste for being wrong", '"Show me what the seller thinks he knows about you."', [
    n("start", "Vellexia", '''{n}Vellexia has spread a narrow strip of silk on the table. Along it, a fine hand has written the names of entertainments, some with dates beside them. Two have been crossed out in a darker ink.{/n}
"Ilveris," she says. "He would prefer a title, but he changes it whenever the old one becomes associated with a debt. At present he calls himself an assessor of future pleasure."
"What did he assess?"
"Me. Without the courtesy of asking how expensive that might prove."
{n}She taps the first crossed-out line.{/n}
"A quartet. He predicted I would tire of it before the third movement. I did. The second prediction concerned a perfume. I sent it away unopened. He claims that counts as tiring of it before the first use."
"A generous standard for himself."
"He has always been his most devoted patron."
{n}The third entry mentions a portrait. Vellexia leaves it for you to read.{/n}''',
      c('[Read what he predicted about the picture she kept.]', "kept", requires=("vellexia.kept_picture",)),
      c('[Read what he predicted about the picture she returned.]', "returned", requires=("vellexia.returned_picture",)),
      c('"I cannot give this proper attention yet."', abort=True)),
    n("kept", "Vellexia", '''"He says I kept it because the flaws gave me something to punish. He has not seen the work. He has seen an invoice describing the reduction in price."
"Would you have kept it without the reduction?"
"No. That does not give him the rest of the answer."
{n}She turns the picture toward you. The painted woman sits with a hand suspended over a closed book. While you look, the hand lowers and the book opens. Vellexia turns the frame away before you can see what is written there.{/n}
"I do enjoy an accurate accusation," she says. "It saves a great deal of explanation. This is a poor accusation wearing the clothes of a clever one."
"You want to prove him wrong."
"I want him to be wrong where people can enjoy it. Those are distinct pleasures. The second is worth dressing for."
{n}She lays the silk beside the key to the frame.{/n}
"Our artist apparently sold his revised bill as a sample. I shall not purchase his next apology. He may keep it for a more hopeful collector."''', c('[Read the offer beneath the prediction.]', "offer")),
    n("returned", "Vellexia", '''"He says I sent it back because indignation was cheaper than admitting curiosity. He has purchased the artist's account of my refusal. A wonderfully affordable authority on my character."
"You did say you wanted the picture more after refusing it."
"To you. In this room. I did not publish the observation for him to sell by the yard."
{n}She smooths the edge of the silk with one finger.{/n}
"And wanting the picture was not the same as wanting to reward the claim attached to it. He has chosen the part that fits his little trade and discarded the rest."
"Will you buy it back to contradict him?"
"No. That would give him two sales from one bad account. Do not make my enemies' work easier merely because you have understood their method."
{n}She looks toward the empty place the frame once occupied.{/n}
"I dislike how much time I have given a man who has not yet managed to enter the room. We shall have to charge him for it somehow."''', c('[Read the offer beneath the prediction.]', "offer")),
    n("offer", "Narrator", '''{n}Ilveris offers a private demonstration. He will name what a guest most wants, select an amusement and predict the moment the guest ceases to enjoy it. Patrons may pay for access to the predictions before inviting that guest elsewhere.{/n}
{n}A second hand has added a brief note beneath the flourishing signature. The demonstration requires three questions answered in advance. The names of any companions and their proposed parts in the evening must also be supplied.{/n}
"His clerk," Vellexia says. "Tessar. A precise woman with a regrettable habit of finishing the sentences he leaves useful only to himself."
"Does she make the predictions?"
"I do not know. I should enjoy asking him in front of her."
{n}You read the three questions. What would you refuse? What would you pay to avoid? What would you be ashamed to want twice?{/n}
"He could use those answers to arrange the result," you say.
"Certainly. I object to his calling the arrangement a discovery."
{n}She rests her chin on one hand, watching you read the last question again.{/n}
"That one interests you. Have you found an answer?"''',
      c('"An easy victory. I enjoy them more than I like to admit."', "victory"),
      c('"An evening with someone who has already told me I ought to know better."', "evening")),
    n("victory", "Vellexia", '''"Of course you do. Difficulty improves a story afterward. It is frequently a nuisance while one is having it."
"You would prefer an easy victory over Ilveris?"
"I would prefer a victory that leaves him alive to hear the account repeated. Ease would be a welcome addition."
{n}She reads the question aloud once more, testing its rhythm.{/n}
"But I see why he asks. A person ashamed of wanting something will pay to be persuaded that the wanting was beyond their control. Fate makes an excellent accomplice. It rarely comes to collect its share."
"You sound as though you have used that explanation."
"I have used nearly every explanation worth hearing. I have also been bored by people who used them badly."
{n}She lays the silk down.{/n}
"Keep that answer for yourself. I have no intention of sending it to him merely because he left a space for it."''', c('[Ask what she will send instead.]', "reply")),
    n("evening", "Vellexia", '''{n}Vellexia's smile is slow and unpleasantly perceptive.{/n}
"That sounds like an accusation delivered as a compliment. You have learned something in this house."
"Would you send him that answer?"
"I would charge him for being allowed to read it. Then I would send something less useful."
{n}She touches the silk's lowest edge, careful not to smear the fresh note.{/n}
"There is a pleasure in returning to something one was warned against. Do not confuse it with liking the thing itself. Some of my admirers have loved the warning so much that they scarcely noticed me."
"You noticed."
"Immediately. It is a tedious form of neglect, all the more insulting because they believe themselves daring."
{n}She looks back at you.{/n}
"Come back for me, darling, not for the warning. I should hate to discover that the danger interested you more than the woman. I have eaten men for less."''', c('[Ask what she intends to send.]', "reply")),
    n("reply", "Vellexia", '''"Nothing yet. Let him wait until he begins predicting whether I will answer."
{n}She folds the silk with the writing inward.{/n}
"I may visit. I may invite him here and find another use for the time. There is no need to make him important merely because he has asked to be."
"And the picture?"
"The artist has spent one piece of information. I have learned what he considers his customers' privacy worth. That is useful enough to keep."
{n}She reaches toward your case, then stops short of touching it.{/n}
"If I pursue this, I shall call you. Do invent a better occupation than waiting for me; I find devotion very dull to watch."
"What if I decline?"
"Then I shall have to find another way to amuse myself. I have managed before."
{n}Her palm turns upward beside your hand, her eyes bright with an expectation she has no intention of disguising.{/n}''',
      c('[Take her hand before leaving.]', "touch", requires=("vellexia.courting",)),
      c('"Ask when you decide. I will answer then."', "part")),
    n("touch", "Vellexia", '''{n}Her fingers close around yours and draw you nearer, as if your hand had been hers to collect all along.{/n}
"An encouragingly direct answer to a question I had not quite asked."
"You left room for it."
"So I did."
{n}She leaves your joined hands between you.{/n}
"Come here. I want a better farewell than a hand."''',
      c('"Yes. I would."', "kiss"),
      c('"Only your hand, this time."', "hand")),
    n("hand", "Vellexia", '''"Only my hand? What remarkable economy. I shall have to make the next visit more tempting, and you will regret your thrift."
{n}She releases your fingers slowly, amused by the temptation she has left unfinished, and wishes you an interesting evening elsewhere in the city in a tone that promises it will not be.{/n}''', c('[Leave her to her schemes.]', flags=("vellexia.prediction_known",))),
    n("kiss", "Vellexia", '''{n}You come nearer. She touches your cheek and kisses you, taking her time over the parting.{/n}
"There. No prediction improved that," she says.
{n}When you step back, she releases your hand. The silk remains folded on the table, and her shell remains closed beside it.{/n}
"Try to find something more delightful in the city tonight. I shall enjoy hearing you explain why you failed."''',
      c('[Leave her to her schemes.]', flags=("vellexia.prediction_known",))),
    n("part", "Vellexia", '''"An admirably unprofitable promise. I cannot even sell it to Ilveris as evidence of what you will do."
{n}She closes her hand and rises. At the door she pauses to turn back toward the folded silk.{/n}
"He has given me something to think about," she admits. "I dislike that more than the invoice. I had intended to choose my own occupation today."
"You still can."
"Yes. I am deciding how much of it to spend disliking him."
{n}Her laughter follows you to the threshold. By the time you reach it she has already turned back to the silk, and to the man she means to ruin.{/n}''',
      c('[Leave her to her schemes.]', flags=("vellexia.prediction_known",))),
], "vellexia.seal_agreed", local=True)

s("the_second_invitation", "The invitation after the dismissal", "[Consider the light beneath the echo shell's cover.]", [
    n("start", "Narrator", '''{n}A dim light moves beneath the closed cover of the echo shell. You have heard nothing from it since your affair in the Upper City ended, and it ended the way everything ends in her house: on her terms, or very nearly.{/n}
{n}The shell glows, and goes on glowing, with the patience of someone who expects to be obeyed. When you open it, one dark eye fills the cloudy glass.{/n}
"Ah. Too near."
{n}Vellexia moves her shell farther away. Her face comes into view. She wears an expression of annoyance that becomes amusement as soon as she sees you noticing it.{/n}
"I have discovered a disadvantage in a conversation one must arrange one's own flattering distance for. You may enjoy that before I begin."''',
      c('"You said you did not intend for us to meet again."', "dismissed", requires=("vellexia.dismissed_native",)),
      c('[Close the cover. Decide whether to hear her another time.]', abort=True),
      c('"The last time we met, you were beaten, and I let you live."', "spared",
        requires=("vellexia.spared",), forbids=("vellexia.dismissed_native",)),
      c('"You sent me away yourself. You said you could not allow me to leave you."', "farewell",
        requires=("vellexia.farewell",), forbids=("vellexia.dismissed_native", "vellexia.spared"))),
    n("dismissed", "Vellexia", '''"I meant every word. You had become tedious. Fortunately for you, Ilveris has done something even more irritating, and I find I need someone to be irritated at him with."
"Then what has changed?"
"Ilveris has made himself useful. I expect to punish him for it."
{n}She brings the folded silk into view, then lowers it when it hides her face.{/n}
"He has distributed a prediction about our dates. He says he knew precisely how long they would hold my interest. That much is cheap enough. Half the city expected a short entertainment. The part I dislike is his claim to have arranged it."
"Did he?"
"Not to my knowledge. I dislike having to add that qualification."
{n}Her mouth tightens.{/n}
"He says every answer I heard was one he had prepared for me to reject. He says I performed his demonstration without knowing I had agreed to appear in it."
"And you want me to contradict him."
"If he is lying. If he is not, I want to know how he accomplished it before I decide which part of him should regret the ingenuity."
{n}She watches your expression in her glass.{/n}
"I intend to make him regret using my name. Yours was in the same little performance, darling, so you may help or you may watch."''',
      c('"I will hear the evidence. I will not pretend our dates ended differently to improve your position."', "evidence"),
      c('"I will hear your quarrel. Spare me the flirtation tonight."', "evidence"),
      c('"I do not want another arrangement with you."', "refuse")),
    n("spared", "Vellexia", '''{n}For a moment her face does nothing at all. Then she smiles, slowly, and it is not a pleasant smile.{/n}
"You did. You surprised me, one last time before the end of our brief affair, and I said so. I have not forgiven you for it. Being spared is a debt, and I loathe owing." {n}She turns a ring on her finger, slowly, the way another woman might test the edge of a knife.{/n}
"Then Ilveris made himself useful. I expect to punish him for it, and I find I would rather have a witness who has already seen me lose."
"What has he done?"
"He has sold a prediction about our affair. He says he knew to the hour how long it would hold my interest, and he says he arranged its ending. Every answer you gave me, he claims, was one he had prepared for me to despise. I should like to know whether he is lying before I decide which part of him to keep."''',
      c('"I will hear the evidence. I will not pretend our dates ended differently to improve your position."', "evidence"),
      c('"I will hear your quarrel. Spare me the flirtation tonight."', "evidence"),
      c('"I do not want another arrangement with you."', "refuse")),
    n("farewell", "Vellexia", '''"I did. I could not allow you to leave me; it would have been intolerable. So I sent you away first, with my best wishes and my wounded pride, and I meant both." {n}Her mouth curves.{/n} "You will notice I did not say I would never call."
"And now you are calling."
"Ilveris has made himself useful. I expect to punish him for it. He has sold a prediction about our affair: he says he knew to the hour how long it would hold my interest, and that he arranged its ending. Every answer you gave me, he claims, was one he had prepared for me to despise." {n}Her eyes narrow.{/n} "If he arranged my farewell, I want to know how, before I decide which part of him should regret the ingenuity."''',
      c('"I will hear the evidence. I will not pretend our dates ended differently to improve your position."', "evidence"),
      c('"I will hear your quarrel. Spare me the flirtation tonight."', "evidence"),
      c('"I do not want another arrangement with you."', "refuse")),
    n("evidence", "Vellexia", '''"Good. A witness who changes the past to please me would be almost as useless as Ilveris. Less amusing, because I would have no reason to be surprised."
{n}She holds a paper close enough for you to make out a few lines. The writing is a transcription of questions from her reception. Beneath them are several possible answers. Some resemble things you might have said. Others turn you into a pompous caricature.{/n}
"He had it printed," she says. "Before the evening, he claims."
"The list could have been written afterward."
"Certainly. Or copied from someone who had heard me ask the same questions of another guest. I am ancient, darling, not inexhaustible. Even my admirers have occasionally heard a question twice."
{n}She lowers the page.{/n}
"Tessar has asked me to pay for the original account rather than the advertisement. That is the first interesting thing to come out of his house. He either has a clerk who dislikes being underpaid, or he has decided to sell the explanation of his fraud as a second service."
"You have not bought it?"
"Not yet. Tessar has offered to sell me the truth. I should like you to hear how expensive it proves. And if you mean to charge me for your help, name your fee now, before I become fond of the work and stop paying attention to prices."''',
      c('"Buy the account, not the clerk. I want a witness with a reason to tell us the truth."', "clerk"),
      c('"Give me a copy of whatever we learn. I want to know how he used my name."', "copy")),
    n("clerk", "Vellexia", '''"She is employed, darling, not chained. Ilveris has at least understood that much, or she would be a chair by now."
"A single account. She is worth more to us as an independent witness than as your newest piece of furniture."
{n}Vellexia regards you for a moment, then laughs.{/n}
"Very well. One account. I want her accurate enough to embarrass him in front of his next patron, and frightened enough of me to stay accurate."
"And afterward?"
"Afterward I expect her to repeat the story wherever it will do him the most harm. That is what I am really buying."
{n}She reaches for a fresh sheet and writes while keeping you in view.{/n}
"There. Enough silver to make truth profitable. Let us see how ingeniously she earns it."
{n}Vellexia reads the offer back, lingering over the sum as if it were a compliment to herself.{/n}''', c('[Accept that limited commission.]', "terms_clerk")),
    n("copy", "Vellexia", '''"A witness with an appetite for the account. How much more interesting than a witness who merely wants to be thanked."
"I want to know what he sold."
"So do I. We may yet quarrel over what to do with the knowledge, but at least we shall begin by wanting the same packet."
{n}She dictates a demand for the predictions and the dates they were prepared, naming the sums she will pay for useful originals and, in a smaller hand, what she will do to a clerk who sells her a forgery.{/n}
"You shall have a copy," Vellexia says. "Try to use it more ingeniously than Ilveris used your name. If you use it to flatter yourself at my expense, I shall know."
"You would dislike it if I flattered you instead."
"Immensely. Flattery from a witness is worth nothing. I collect the other kind."
{n}She sets the sheet aside.{/n}
"If she accepts, we shall examine it together. You may accuse me of selective reading where I can hear you."''', c('[Accept access to the same account.]', "terms_copy")),
    *[n(id, "Vellexia", '''"One more matter. You will not go into his house on the strength of my amusement. I am quite capable of deciding I dislike a person while they are still useful. You should know where the doors are without relying on my mood."
"We can work through the shell."
"For now. We shall examine it through the shell. I want to watch the clerk discover which part has offended me, and I want you watching me watch her."
{n}She moves her own shell enough to show you the empty part of the table around it, then returns the glass to her face.{/n}
"I have missed a certain quality of your disagreement," she says. "Do not become sentimental about the admission. It does not mean I have decided what else I miss."
"Then we can leave that undecided."
"Excellent. Keep that little uncertainty. It suits you far better than an apology, and I intend to take it from you slowly."
{n}She closes the cover with the satisfied air of a woman who has found tomorrow's amusement. The light goes out, leaving you with an ordinary quiet and the inconvenience of being interested.{/n}''',
      c('[Agree to examine the account when it arrives.]', flags=("vellexia.case_opened", flag)))
      for id, flag in (("terms_clerk", "vellexia.clerk_terms"), ("terms_copy", "vellexia.shared_account"))],
    n("refuse", "Vellexia", '''{n}Her expression stills. For a moment you can see her deciding which unpleasant answer would please her most.{/n}
"Very well," she says at last. "I asked. You answered. I shall seek a different audience."
"You do not sound pleased."
"No, I am not pleased. Did you expect me to applaud the loss of an interesting accomplice? I shall find another, and I shall tell him all about you."
{n}She reaches toward her cover, then pauses.{/n}
"Keep the account of our dates accurate if anyone asks. I have no intention of improving it for your reputation either."
{n}The glass clouds as she closes the shell. No second request follows. Whatever becomes of Ilveris, it will not be a commission you accepted.{/n}''',
      c('[Close the shell and end this private correspondence.]', flags=("vellexia.closed",))),
], "vellexia.prediction_known")

s("the_claim_before_the_event", "What the account can prove", "[Open the echo shell to examine Tessar's account.]", [
    n("start", "Vellexia", '''"You went somewhere my shell could not follow," Vellexia says as the glass clears, "and came back, which I shall count in your favour. Tessar did not wait for you. She accepted while you were gone. I find a promptly answered offer almost suspicious. Fortunately, the account is irritating enough to restore my faith in the enterprise."
{n}Three sheets lie on her table. She brings them into view one at a time, giving you time to read before moving the shell again.{/n}
"These are her copies. She says the originals remain where Ilveris's creditors can inspect them. He requires patrons to deposit a stake before he will guarantee a prediction. The stake is returned when they accept his account of the result."
"And if they disagree?"
"He retains it while they prove him wrong. Such a beautiful little arrangement. I almost regret not having invented it."
{n}The first sheet lists dates and sealed packets. The second gives the predictions. The third records what happened and how Ilveris chose to describe it afterward.{/n}
"Tessar says the seals on the first page are genuine. She refuses to tell me that this makes the third page honest. I begin to appreciate her precision."''',
      c('[Compare the dated predictions with the later descriptions of the results.]', check=dict(Skill="SkillKnowledgeWorld", DC=29, CommanderOnly=True, Success="found", Failure="missed")),
      c('"Have Tessar choose one disputed entry and explain how it was recorded."', "ask"),
      c('[Close the shell until you can study the account.]', abort=True)),
    n("found", "Vellexia", '''{n}The date on one prediction belongs to the sealed packet, not to every line inside it. Tessar's copy records an addition made after the packet was opened. Ilveris's later account prints that addition beneath the earlier date without distinguishing it.{/n}
{n}You point out the change. Vellexia turns the sheet toward herself, reads it twice and gives a soft, delighted laugh.{/n}
"A prediction of yesterday, guaranteed by an envelope from last week. How very efficient."
"It proves he altered this entry. It does not prove every prediction is false."
"No. We shall have to inconvenience him with the precise accusation."
{n}You find a second alteration in the account of the perfume. The unbroken seal covers his prediction that she would reject an unfamiliar scent. The words 'without opening it' were added later.{/n}
"That one is mine," she says. "I shall keep the original where he can see me keeping it."
{n}The account concerning your dates has no such addition. Vellexia's smile thins.{/n}
"Now we reach the part I was hoping would be equally simple."
{n}She calls Tessar into the room. A composed voice answers from just outside the glass: "I have the purchaser's extract here, my lady. Shall I read it beside the original?" Vellexia tells her to remain while you compare them.{/n}''', c('[Read the sealed prediction about the Commander.]', "yours")),
    n("missed", "Narrator", '''{n}You mistake the repeated date for evidence that two packets were opened at once. Vellexia calls Tessar into the room and asks her to compare the entries with your explanation.{/n}
{n}A composed voice answers from outside the glass.{/n}
"That is the date of settlement. The prediction is on the previous line. I used different columns because the same date would have been misleading."
{n}There is a pause in which Vellexia appears to enjoy several possible remarks before selecting one.{/n}
"Our witness has demonstrated the usefulness of your columns. Continue."
{n}You acknowledge the mistake. Tessar reads the disputed entry in full. Your attempted shortcut has consumed the time she reserved for making another copy; Vellexia must buy a second appointment if she wants the remaining papers delivered promptly.{/n}
"I shall pay," Vellexia says. "You may repay me by making your next certainty more expensive to obtain."
{n}Tessar identifies the later additions herself. The account concerning your dates, however, appears to have been sealed before the first meeting at the arena.{/n}''', c('[Ask to hear that particular entry in full.]', "yours")),
    n("ask", "Vellexia", '''"You would rather hear the person who wrote it. A habit I should find less disappointing by now."
{n}She calls Tessar into the room. The clerk remains outside the glass and introduces herself before speaking. Her voice is low and careful, with no apparent effort to resemble Vellexia's polished hospitality.{/n}
"I can explain the perfume entry. That is the smallest dispute. The later description includes a phrase that was not in the sealed prediction. I marked its addition in my copy."
{n}She takes you through the columns without being hurried. Vellexia attempts to interrupt once. Tessar asks whether she should stop accounting for the work she has been paid to do. Vellexia laughs and lets her finish.{/n}
{n}The explanation uses the time Tessar had reserved for preparing a second set of papers. Vellexia buys another appointment on the spot; an account this damaging is worth keeping its author eager, and well paid enough to be afraid of losing the work.{/n}
"I have acquired a very expensive appreciation of neat columns," she says when the clerk pauses. "Now tell us about the Commander."
"That prediction was sealed earlier," Tessar replies. "The changes are in the account of what it means."''', c('[Listen to the prediction about you.]', "yours")),
    n("yours", "Vellexia", '''{n}The prediction lists five answers a visitor might give about coming to the Abyss. Duty, revenge, pleasure, uncertainty and ambition. Beside each, Ilveris has written a possible reason Vellexia would eventually dislike hearing it.{/n}
"He sold the entire list," she says. "He only needs one answer to fit."
"Does the account say which one he predicted I would give?"
"No. It says the packet contained the answer. A claim generously assisted by containing several others."
{n}Tessar adds, from beyond the glass, that Ilveris charged each purchaser for a different extract. Those whose extracts proved unhelpful received a credit toward another demonstration. They had an interest in continuing rather than announcing what they had lost.{/n}
"So he did not arrange what I said," you observe.
"He arranged what people would pay to believe about it," Vellexia answers. "I dislike that more. If he had controlled you, at least there would have been a spell worth examining."
{n}She lowers the papers. For a moment her irritation is bare.{/n}
"I was predictable enough to make his lie convenient. That is the part he will expect me to deny. We should find a better answer."''',
      c('"Expose how he changes the account after the event. Leave your tastes out of it."', "method"),
      c('"Offer him one prediction that must name a result before either of us chooses it."', "challenge")),
    n("method", "Vellexia", '''"A clean accusation. Almost irritatingly clean. He loses his claim to honest accounting, and I lose the pleasure of watching him attempt to read me."
"You would still win something."
"Yes. That is why I am considering it."
{n}She asks Tessar whether the later additions can be certified without exposing the names of every purchaser. Tessar says they can, but someone must pay for a second clerk to compare the originals.{/n}
"Send me the cost," Vellexia says. "And do not find the cheapest clerk merely because you think I will enjoy having paid less. I want Ilveris unable to buy the answer back."
{n}Tessar leaves to prepare it. Vellexia waits until you hear the door close.{/n}
"You have offered me a result with fewer opportunities to become magnificent. I shall remember that when you next ask why I prefer your company to an obedient audience. Sometimes I do not."
{n}Her smile returns, sharper than before.{/n}
"We shall compare the price with the more extravagant possibility before deciding."''',
      c('[Keep the accounting approach available.]', flags=("vellexia.account_read", "vellexia.method_first"))),
    n("challenge", "Vellexia", '''"There. You do understand the expensive part."
{n}She asks Tessar to remain long enough to hear the proposed rule. One question. One declared result. No substitution after the choice has been made, and no losing purchaser required to buy another chance merely to recover the first stake.{/n}
"He will ask what he gains by accepting," Tessar says.
"My name attached to the result if he is right. An admission in public. He has been selling a counterfeit of it; let him try to obtain the original."
"And if you refuse to make the admission?"
{n}Vellexia looks toward the unseen clerk.{/n}
"Then I lose the stake as well as giving him a better story. Put it in the account. I will not pay you to pretend that I am an easy person to collect from."
{n}Tessar leaves to calculate the terms. Vellexia watches you through the glass.{/n}
"This could be unpleasant," she says. "I find I have missed being uncertain about which unpleasantness I will prefer."''',
      c('[Keep the public challenge available.]', flags=("vellexia.account_read", "vellexia.challenge_first"))),
], "vellexia.case_opened", chapter=5)

s("the_clerks_own_price", "The woman who kept the accounts", "[Hear Tessar's terms through the echo shell.]", [
    n("start", "Vellexia", '''"Tessar is here," Vellexia says when you answer. "She has asked to speak before I begin improving the proposal. I find that impertinent enough to be promising."
{n}She moves the shell to show a woman standing beside the table. Tessar has short dark horns and a mouth that looks accustomed to being held still while somebody else speaks. A leather case rests beneath one hand.{/n}
"I have agreed to discuss the accounts," Tessar says. "Not to be introduced as the conscience of Ilveris's establishment. You should know that before we begin."
"I had not mistaken you for it," Vellexia answers.
"Some of your guests may. They will want an admirable reason for my changing patrons. I would prefer an accurate one."
{n}She looks toward the glass, waiting for you to speak.{/n}''',
      c('"Then tell me why you are willing to sell the account."', "reason"),
      c('[Postpone until you can hear her without interruption.]', abort=True)),
    n("reason", "Tessar", '''"I prepared the settlements. Ilveris took the fee for each successful prediction and deducted the cost of the unsuccessful ones from mine. He called the first his insight and the second my poor selection of clients."
"You agreed to that?"
"For one season. I thought I could learn enough to leave with clients of my own. I learned that he intended to sell those introductions separately."
{n}Vellexia leans back, visibly pleased by a story with room for more than one appetite.{/n}
"And now?" you ask.
"Now I want three things. Payment for the work I have done. A record that I did not alter the sealed predictions. And the right to show prospective employers what I can prepare without asking Ilveris to recommend me."
"Whose names must you use?"
"From the people whose names are in it. I can conceal purchasers. I cannot conceal Lady Vellexia and the Commander while making this particular account intelligible."
{n}She opens her case and lays down a prepared sample. Most names have been replaced by marks. Yours and Vellexia's remain, along with the questions used to describe your dates.{/n}''', c('[Examine the sample she wants to use.]', "sample")),
    n("sample", "Vellexia", '''"She wants to make a career from the account of my having been misrepresented. An enterprising choice."
"I want to make a career from a correct account," Tessar says. "It is more difficult to sell than you might imagine."
"I can imagine several prices."
{n}Vellexia studies the sample. The record includes her own refusal to examine the perfume before rejecting it. It also includes the fact that she declined to give a reason afterward.{/n}
"That is accurate," she says. "I dislike the order in which it makes me appear unreasonable."
"The order is chronological."
{n}For a moment the room on the other side of the glass becomes very quiet.{/n}
"I noticed," Vellexia says at last. "Do not cultivate insolence merely because it worked once."
{n}Tessar lowers her eyes but does not take the sample away.{/n}
"The Commander must decide about the questions attributed to them," she says. "I cannot claim that every possible answer was spoken. I have made that distinction. I need them to tell me whether it is clear."''',
      c('"It is clear. You may use this account, including my name, once the alterations are independently checked."', "named"),
      c('"Use the method, but remove my name and the private questions. I will attest that your accounting was clear."', "limited")),
    n("named", "Tessar", '''"That gives me something I can show without asking a listener to trust an anonymous example. Thank you."
"Do not thank too soon," Vellexia says. "You still require my answer."
{n}Tessar waits. Vellexia reads the sample again, stopping at the unfavorable line she has already objected to.{/n}
"You may use it," she says. "Once it is checked. Keep the part in which Ilveris claimed my rejection was his invention. If I am to appear unreasonable, I want the neighboring folly represented at full size."
"It is already there."
"Then we have saved each other a correction."
{n}Tessar records both answers and closes her case, well aware of the powerful resentment her sample may attract. She does not ask Vellexia to promise it will never arrive; nobody who has spent an afternoon in this house would.{/n}
"I can afford one carefully documented enemy," she says. "I could not afford another year of paying for his unsuccessful predictions."''', c('[Let her finish the arrangement before she leaves.]', "named_end")),
    n("limited", "Tessar", '''{n}Tessar considers the restriction, then sets the named sample aside.{/n}
"I can prepare an anonymous version. Your attestation will help, though it will not demonstrate as much. Some employers will assume the interesting names were invented."
"They were not," you say.
"No. But I am asking them to distinguish my accurate account from Ilveris's advertising. I should expect the question."
{n}Vellexia watches her select the pages that will need alteration.{/n}
"I will permit my name in the part concerning the perfume," she says. "The Commander has their own appetite for being discussed. I have mine."
"That will make the sample uneven."
"Then explain the reason. You are very good at explaining reasons when I would prefer you had overlooked them."
{n}Tessar nods. She will have to do more work, and the sample will be harder to sell. In return, she has a narrower piece of the Commander's life to account for when the questions begin.{/n}''', c('[Let her finish the arrangement before she leaves.]', "limited_end")),
    *[n(id, "Vellexia", '''{n}Tessar takes the silver and leaves. You hear the clasp click as she checks her case twice, then the door opens and shuts. Vellexia brings the shell nearer.{/n}
"I wanted to frighten her when she corrected me," she says. "You noticed."
"Yes."
"I wanted her to remain accurate too. A tiresome interference between pleasures."
"You chose the account."
"Today. Do not turn a practical decision into a discovery of my hidden goodness. If you do, I shall have to demonstrate the alternative on somebody, and it will probably be someone you like."
{n}She looks toward the door Tessar used.{/n}
"She may earn herself better patrons by embarrassing Ilveris. I should enjoy hearing him complain. Or she may use my name badly, in which case I shall have a new occupation, and she will have a very short career."
"You agreed to the sample you read."
"I did. I intend to remember exactly how much I gave her. So should she."
{n}Vellexia turns back to you.{/n}
"You gave her an answer worth selling. How refreshing. Most of my guests would have offered her advice, and I would have had to watch."
"Useful?"
"Do not hurry me. I am rationing the compliments. You have had two this month."''',
      c('[Await Ilveris\'s answer.]', flags=("vellexia.witness_heard", flag)))
      for id, flag in (("named_end", "vellexia.named_sample"), ("limited_end", "vellexia.limited_sample"))],
], "vellexia.account_read", chapter=5)

s("the_wager_with_an_edge", "The cost of a certain answer", "[Hear Ilveris's response to the proposed challenge.]", [
    n("start", "Vellexia", '''{n}Vellexia has opened her ring tray again. Through the glass you see her lift a narrow circlet from it and place it beside Tessar's revised account.{/n}
"Ilveris accepted the possibility of a demonstration. He has declined the possibility of being paid merely to admit that his descriptions were dishonest. A severe limitation in his understanding of entertainment."
"What does he want?"
"This. A piece I made when I was less easily offended by excellent work belonging to someone else. I won it back from its third purchaser after deciding I disliked seeing it worn badly."
"Is it alive?"
"No. Enchanted silver. My own work, my own property, and sufficiently valuable that losing it would annoy me. He chose well."
{n}She puts one finger through the circlet and turns it without sliding it onto her hand.{/n}
"He will risk the original packets, the deposits attached to this series of predictions and a public correction. He wants me to risk the circlet and an admission that he understood something I could not bear to hear."
"Even if what he understood was how to arrange the result?"
"Precisely. He wishes to sell that distinction afterward. We must decide whether to let him try."''',
      c('[Ask about exposing the altered accounts without taking his wager.]', "account"),
      c('[Ask what one result he proposes to predict.]', "question"),
      c('[Leave the decision until you can consider it carefully.]', abort=True)),
    n("account", "Vellexia", '''"The second clerk has confirmed the additions. We can publish that much now. It will cost the fee already spent, and Ilveris will lose some confidence among his purchasers."
"Some?"
"Some of them buy him because they like what he lets them believe about themselves. A careful explanation will not impoverish that trade overnight."
{n}She lifts the circlet, then sets it back in its compartment.{/n}
"It would end our particular work cleanly. He did not control your answers. He changed his claims afterward. We could say so, let Tessar use the agreed sample and find a different occupation."
"You sound disappointed."
"I am. I also like this piece of silver. Both deserve consideration."
{n}Her gaze returns to yours through the glass.{/n}
"Publish it, if you prefer. I shall have to imagine his face when the purchasers begin asking for their silver back, and I shall tell you at length how much better it would have looked in person."''',
      c('"Publish the checked account. Keep the circlet and let this be enough."', "publish"),
      c('"Tell me the proposed prediction before I decide."', "question")),
    n("question", "Vellexia", '''"He will prepare two sealed descriptions. One contains an amusement he claims I will prefer; the other contains an account of why I will choose against it when I know he expects the preference."
"That still allows him both answers."
"Yes. I told him so in words Tessar has declined to preserve in her formal record."
{n}Vellexia smiles.{/n}
"The revised version has one sealed prediction and three offers. A repeat of an entertainment I once praised, a new work I have not examined, and an hour left entirely for my own use. He must name the one I will choose. I must actually spend the hour on it."
"He could make one of them unbearable."
"We choose who supplies the offers. He sees their descriptions in advance, as do I. He must state his answer before we see the finished works."
{n}She lifts the circlet again.{/n}
"He proposes that you choose the order in which I receive them. I believe he wants to make my decision look like a decision about you. We could refuse that part. Or leave him the temptation to mistake my appetite for something simpler."''',
      c('"Take the wager, but let Tessar draw the order. I will witness it."', "draw"),
      c('"I will choose the order. He can risk his claim on understanding both of us."', "order"),
      c('"No. Publish the checked account instead."', "publish")),
    n("publish", "Vellexia", '''{n}She closes the ring tray with the circlet inside it.{/n}
"Very well. I shall have to enjoy being correct without making an entire room watch me discover it."
"You can make the room read."
"A cruel suggestion. Some of them would prefer a more immediate punishment."
{n}She calls Tessar and gives the instruction. The corrected account will go to every purchaser of the affected predictions, with an invitation to compare their copies and a list of the deposits Ilveris has kept. The perfume entry carries the proof; the Commander's private questions stay out of the copies, as ordered.{/n}
"I am paying," Vellexia says. "Keep the accusation exact. I want him unable to wriggle out of it, and I want him to know whose silver paid for the nail."
{n}When the clerk leaves, Vellexia looks almost satisfied.{/n}
"He will receive questions he has not written for himself. That may be worth imagining even without a seat in the room."
"And the demonstration?"
"Canceled. I will not leave him expecting a stake I have decided to keep."''',
      c('[Let the checked account stand without a wager.]', flags=("vellexia.wager_chosen", "vellexia.published_accounts"))),
    n("draw", "Vellexia", '''"You deprive him of a convenient romance. I imagine he will manufacture another."
"He must predict the choice, not the explanation he will sell afterward."
"Yes. Let us make that expensive to forget."
{n}She calls Tessar into view. The clerk reads the revised terms and records her own responsibility for drawing the order. Ilveris will seal one named result before the draw, and copies of the seal will be witnessed by purchasers who have deposits at risk.{/n}
"I will not promise he loses," Tessar says.
"I would not pay you to," Vellexia answers. "You would be selling the same service with less attractive handwriting."
{n}Vellexia lifts the circlet toward the shell, letting you see its fine joined edges.{/n}
"If I lose, I want you to remember that this was excellent work. Do not soothe me by saying the loss was nothing."
"I will remember."
"Good. We have begun agreeing on the difficult parts."''',
      c('[Accept a witnessed draw and the real risk of losing.]', flags=("vellexia.wager_chosen", "vellexia.drawn_order"))),
    n("order", "Vellexia", '''"You are certain you want to stand where his explanation will point?"
"I want to see whether your choice needs his explanation."
{n}She studies you for a moment, then calls Tessar forward. The clerk records that you will choose the order after the prediction is sealed. The offers themselves will be checked by the same witnesses who hold copies of the seal.{/n}
"If you arrange the order to make her lose," Tessar says, "the loss remains a loss. I will not be asked to rewrite it because the reason was intimate."
"You will not," Vellexia says. "And if I choose merely to thwart the Commander, record that too. I should hate to deprive our assessor of something else to be wrong about."
{n}After Tessar has written, Vellexia moves the shell nearer.{/n}
"I might surprise you unpleasantly," she says.
"You have done so before."
"And you have opened the cover again. An interesting fact. I shall avoid explaining it too quickly."''',
      c('[Accept responsibility for choosing the order.]', flags=("vellexia.wager_chosen", "vellexia.commander_order"))),
], "vellexia.witness_heard", chapter=5)

s("an_hour_that_counts", "The result he must keep", "[Answer Vellexia's request on the evening of the decision.]", [
    n("start", "Narrator", '''{n}The light beneath the shell's cover burns steadily. When you answer, Vellexia has already placed her own shell where both hands are free. You see the edge of a table and her face beyond it.{/n}
"You are in time," she says. "I have been deciding how much of this evening I want you to witness. The unflattering parts seem determined to occur first."''',
      c('[Ask about the published account.]', "published", requires=("vellexia.published_accounts",)),
      c('[Ask whether the prediction is sealed.]', "sealed", forbids=("vellexia.published_accounts",)),
      c('[Close the cover and postpone the conversation.]', abort=True)),
    n("published", "Vellexia", '''"Ilveris has answered. He says the altered descriptions were interpretive notes, never intended to be confused with predictions. Then he objects that Tessar disclosed his method to people incapable of appreciating it."
"Did they believe him?"
"Some. Others have asked for deposits he assured them they would recover after another purchase. He is attempting to decide which question to answer first."
{n}She lifts an opened letter into view.{/n}
"This purchaser thanks me for helping him discover that three of his most perceptive remarks about his lover came from the same sealed packet. He proposes that I help him recover the price."
"Will you?"
"No. I did not undertake to make everybody who enjoyed Ilveris's flattery wealthy again. I have given him a correct account. He may use whatever intelligence survives the disappointment."
{n}She sets the letter down with evident pleasure.{/n}
"Tessar has two offers for work. I advised her to demand enough silver to make Ilveris jealous, and to make the second employer bid against the first. She looked at me as though I had handed her a knife. I had."
"And you?"
"I have my circlet and an enemy whose explanation requires longer every time he gives it. I find the result more satisfying than I expected."''', c('[Ask what she intends to do with the rest of the evening.]', "unspent")),
    n("unspent", "Vellexia", '''"I have an hour I had reserved for being vindicated in public. It has become available for a less improving occupation."
{n}She takes a small book from beside the shell. You recognize the marked page from the sitting room, though the edge has acquired another impatient crease.{/n}
"I thought of inviting people to hear the account. Then I imagined the third person congratulating me on my insight, and the pleasure began to curdle. I wanted to have been right. I did not want to hear everybody describe the accomplishment."
"What would you rather hear?"
"Your opinion of a line I have been attempting not to enjoy again. I suspect repetition has been unfairly blamed for several deficiencies in my guests."
{n}She reads the insult from the play. Her delivery is slower than you remember; she holds the final word until you have almost supplied it yourself. You laugh, and she looks up with an expression too pleased to conceal quickly.{/n}
"There. He would have sold that as a prediction too."
{n}She reads the reply, then shuts the book before the next scene can demand its turn.{/n}''', c('[Stay for the conversation after the account.]', "published_end")),
    n("sealed", "Vellexia", '''"Sealed, copied and witnessed. Ilveris has written that I will choose the unused hour. He has supplied an explanation, but it will be opened afterward. I refuse to have the evening spoiled by being told what I must think about it in advance."
"You know his answer?"
"We agreed I would. The wager is that he can predict my choice even when I have an excellent reason to make another. He considers pride a predictable inconvenience. I am about to give that opinion a costly audience."
{n}She turns the shell to show Tessar at the far end of the table. Beside her stand three witnesses holding their copies. Ilveris has sent his signed acceptance; he has declined to attend in person.{/n}
"A sensible man on a rare occasion," Vellexia says.
{n}The first offer is the old play, performed by two hired actors who look as though they have heard what became of the last ones in this house. The second is a new mechanical theater whose silver figures dismantle an emperor's triumphal procession to build a privy. The third is the empty hour.{/n}
"The mechanism is silver and springs," Tessar says before you ask. "Its maker has brought it himself. Lady Vellexia asked that nobody look at the actors as though they were furniture. It made them more nervous."
{n}Vellexia smiles at the irritation in the clerk's exact repetition.{/n}''',
      c('[Let Tessar draw the order as agreed.]', "draw", requires=("vellexia.drawn_order",)),
      c('"Begin with the new theater. Let her discover whether it deserves her time."', "new", requires=("vellexia.commander_order",)),
      c('"Begin with the empty hour. I will not conceal what he expects her to want."', "quiet", requires=("vellexia.commander_order",)),
      c('[Trickster] "The coin you gave me opened the way through your arch. Would you like to try giving this hour an unexpected ending?"', "fate_offer", requires=("vellexia.commander_order", "trickster", "vellexia.coin_given"))),
    n("draw", "Narrator", '''{n}Tessar draws the new theater first. The mechanism begins with a tiny fanfare so overconfident that Vellexia laughs before any figure has moved. The emperor lifts a silver arm. His servants begin dismantling the arch above him.{/n}
{n}The transformation takes longer than good taste would advise. Vellexia leans forward, impatient, just as a workman returns to measure the emperor himself for the door. The little ruler is too wide. The workman removes the imperial crown and tries again.{/n}
"Oh, that is ugly," Vellexia says delightedly. "Leave it running."
{n}Tessar reminds her that the other offers remain to be sampled. Vellexia permits the old play's opening and hears its familiar insult without smiling. Then she dismisses both samples and asks the mechanism's maker whether the emperor fits through the door by the end.{/n}
"That would tell you the last joke," the maker answers from beyond the glass.
"Then remain alive to receive a compliment if it is good. I choose the theater."
{n}Tessar records the choice. The prediction has failed, but the hour must still be spent as agreed.{/n}''', c('[Watch the hour she chose.]', "won")),
    n("new", "Narrator", '''{n}You choose the new theater first. Its maker starts the mechanism where the shell can show you the moving figures. A silver emperor raises his arm to accept the adoration of a procession whose servants have begun dismantling his triumphal arch.{/n}
{n}Vellexia laughs when the first column becomes a privy door. By the time the workmen discover the emperor is too wide to enter, she has asked the maker two questions and been refused the answer to both.{/n}
"You understand how to sell an ending," she says. "That is more than can be said for our absent assessor."
{n}She hears the sample of the old play, then spends several silent moments considering the empty hour. You do not fill them for her.{/n}
"The theater," she decides. "I want to know whether the little tyrant ever becomes useful. The question may occupy me longer than the answer."
{n}Tessar records the choice. Vellexia glances toward your image.{/n}
"You chose well," she says. "Do not assume that will make you better at it tomorrow."
{n}She turns back to the figures before you can offer a reply.{/n}''', c('[Watch the hour she chose.]', "won")),
    n("quiet", "Vellexia", '''{n}She looks at you through the glass, then at the witnesses.{/n}
"The honest temptation first. Very well."
{n}She samples the old play. She watches the mechanical emperor begin to lose his triumphal arch. The joke makes her laugh, but when the maker reaches to continue it, she raises a hand.{/n}
"No. I choose the empty hour."
{n}Tessar pauses with her pen above the account.{/n}
"You understand that this is the sealed prediction."
"I heard it. I also heard the beginning of two entertainments I have no particular wish to finish tonight. I will not spend an hour displeased merely to rescue my reputation for being difficult to understand."
{n}She picks up the circlet and places it beside the witnesses' copies.{/n}
"Send it. Record that he was right about this choice. Keep the corrections to his earlier accounts where people can read them. One accurate prediction does not mend the others."
{n}The decision has made her angry. It has not made her ask you to find a false way around it.{/n}''', c('[Accept the loss without calling it meaningless.]', "lost")),
    n("fate_offer", "Vellexia", '''"Explain it before you entertain yourself at my expense."
"The shell already carries an echo. Let it keep this hour, and give it back to you once, in the space of a breath, when it is over. You would know what was coming, and you could watch for the moment the little tyrant gives the joke away. Nobody else would lose a moment of it."
"Would that make him wrong?"
"Not by the terms you agreed. It would be a fourth offer. You would forfeit the stake if you took it."
{n}She becomes very still. Then she smiles.{/n}
"An expensive trick that admits its price. Tessar, record the forfeit. I would like to be the person who knows why I paid it."
"You may still choose one of the three offers," the clerk says.
"I know. That is what makes spending the silver interesting."
{n}Vellexia speaks her agreement into the shell. You ask the echo to keep the hour between its first note and its last. A second light appears beneath the glass, following the first a heartbeat behind. Vellexia studies the doubled gleam, then deliberately holds her hand before it.{/n}
"One encore," she says. "Do not teach the shell to mistake my curiosity for patience."
{n}You promise one turn, and she makes you say it twice, as if she expects to be cheated.{/n}''', c('[Give her the one encore she has bought.]', "fate")),
    n("fate", "Narrator", '''{n}The hour passes. Vellexia chooses the old play and dismisses it after the familiar insult. She watches the mechanical emperor fail to fit through his new door. Then she spends the remainder talking to the maker about an earlier, less successful machine.{/n}
{n}At the last note of the shell, Vellexia closes her eyes. The stored hour passes through her awareness again, from the first insult to the maker's final explanation. She knows each word before it arrives and listens this time for the moment his pride gives way to embarrassment. Across the room a witness finishes drawing breath. To everyone else, only that breath has passed. The second light goes out.{/n}
"Enough," she says.
{n}The glass remains dark until she opens her eyes; no second recollection follows.{/n}
{n}She sits without speaking for several breaths.{/n}
"I knew which parts were coming. I still wanted to hear one of them. How extraordinarily inconvenient."
{n}Tessar asks whether the forfeit stands. Vellexia hands her the circlet.{/n}
"Of course. He may tell people he won an object. He will have to ask me what I bought with it."
{n}The witnesses leave with the recorded result. No prediction has been rewritten, and no earlier choice has been removed from the account.{/n}''', c('[Remain while she dismisses the last spectators.]', "fate_end")),
    n("won", "Vellexia", '''{n}She stays for the promised hour. By the end, the emperor has become the privy's door handle and the procession has begun praising his accessibility. Vellexia laughs so suddenly that one of the witnesses forgets to be discreet about staring.{/n}
"Yes, I enjoyed it," she tells him. "You may report the astonishing event without inventing a more flattering cause."
{n}Tessar records the completed hour, returns the circlet to its owner and prepares the correction Ilveris must circulate. His deposits will go back to the purchasers named in the agreement. He will keep whatever business does not depend on this wager.{/n}
"Not ruined," Vellexia observes. "Merely inconvenienced in public. I shall have to make the most of it."
{n}She asks the maker for a price for another performance, then rejects the first figure offered with such enthusiasm that the negotiation becomes an entertainment of its own. By the end he has agreed to build her a second emperor, smaller, with a face she will describe to him later.{/n}
{n}When the room empties, she moves the shell close again.{/n}
"You stayed. Even through the parts in which I had almost nothing to say to you. I find that more pleasant than I expected."''',
      c('[Keep the finished result and the unexpected pleasure.]', flags=("vellexia.verdict_kept", "vellexia.wager_won"))),
    n("lost", "Vellexia", '''{n}She dismisses the performers and gives the witnesses leave to go. The empty compartment in the ring tray remains within the glass's view until she notices it and moves the tray aside.{/n}
"I wanted that piece," she says. "I can make another. I wanted that one."
"You chose the hour knowing the cost."
"Yes. I have been attempting to resent you for presenting it first. You may be pleased to hear the attempt is going badly."
{n}She sits back and looks at your image without smiling.{/n}
"Stay. I require an audience with the sense not to congratulate me on losing gracefully. I have not decided to be graceful, and if you call me that I shall show you what I do instead."
{n}You stay. She tells you how she recovered the circlet from its third purchaser, and the story is vain, vindictive and funny enough that you understand why she wanted the object back. When you laugh, she reaches toward the shell before remembering the distance.{/n}
"There," she says, drawing her hand back. "Something worth the price of a poor temper."''',
      c('[Spend the rest of the empty hour with her.]', flags=("vellexia.verdict_kept", "vellexia.wager_lost"))),
    n("fate_end", "Vellexia", '''"Do not tell me you have cured my boredom," she says when you are alone. "I shall become bored with the sentence before you finish it."
"You wanted to try one unexpected ending."
"I did. I obtained it. I also lost something I liked, which will prevent me becoming unbearably grateful."
{n}She touches the closed ring tray and pushes it out of view.{/n}
"The encore was mine. Nobody else in that room got a second hour, and they will spend years wondering why I smiled at the wrong moment. Ilveris can keep the circlet and invent a reason why I enjoyed losing it."
"Would you do it again?"
"Not tonight. Tonight I would like to find out what happens after it."
{n}She brings the shell nearer and asks you about the moment you knew her answer would cost her the circlet. She listens closely, especially where your account differs from the one she expected.{/n}''',
      c('[Finish the evening without another turn of the trick.]', flags=("vellexia.verdict_kept", "vellexia.fate_hour"))),
    n("published_end", "Vellexia", '''"I expected to spend tonight humiliating a man in front of people whose opinions I would dislike by morning. Instead I have humiliated him in writing and found a better use for the remaining time."
"You have no regrets?"
"Several. I would have enjoyed his face when he lost. I would also have disliked hearing him describe the loss as part of his plan. You have deprived me of both."
{n}She rests the book beside the shell.{/n}
"Tessar will send the final receipts. Once I have paid them, this is finished. Ilveris may continue to be irritating, but I refuse to let that become an obligation to correspond with him."
"And with me?"
{n}Her attention settles on your face.{/n}
"A different question. Ask it when I can answer without pretending we are still discussing an invoice."''',
      c('[Let the work end with the account actually settled.]', flags=("vellexia.verdict_kept", "vellexia.account_published"))),
], "vellexia.wager_chosen", chapter=5)

s("the_question_after_business", "What she asks without a fee", "[Open the shell for a conversation without an account to settle.]", [
    n("start", "Vellexia", '''{n}When the glass clears, Vellexia is fastening an earring. She finishes before speaking, then turns her face slightly as though she expects an opinion and has not decided whether to request it.{/n}
"Tessar has been paid. The receipts have been copied. Ilveris has discovered that describing a disappointment at greater length does not always increase its sale price. I have decided we may cease discussing him."
"A generous decision."
"For us. I intend to let him wonder which of his latest explanations I have read."
{n}She leans toward the shell.{/n}
"I asked for this conversation because I wanted it. I have no difficult packet to put in your hands first. You may find the change alarming."
"What would you like to talk about?"
"The fact that you kept opening this little door after I had given you an excellent reason to leave it shut."''',
      c('"I wanted the work settled. I also wanted to hear you."', "want"),
      c('[Leave the request unanswered until you can give it time.]', abort=True)),
    n("want", "Vellexia", '''"Yes. That second part has become inconveniently important to me."
{n}She moves her hand away from the earring.{/n}
"I wanted you gone, at the end. I said so, and I meant it, and I do not take back things I meant. Now I find that your voice has become an exceedingly inconvenient pleasure, and I resent it."
"You could ask for one."
"I am approaching the indignity with suitable care."
{n}Her smile returns, but she does not let it finish the conversation for her.{/n}
"You let me be wrong without pretending I had become a helpless creature who needed your good influence. You disagreed, sometimes at exactly the moment I wanted obedience. You also found things to enjoy that I had not selected to impress you."
"That sounds like another assessment."
"It is. There is no invoice left to examine, and still I want you to open the shell. How irritating. I have had men flayed for being less inconvenient."
{n}She looks directly into the glass.{/n}
"I want you as my lover. Imagine how delighted I am to discover that you may have something to say about it. Say it quickly, darling, before I decide to be offended by the delay."''',
      c('"I want you. Let us see how long we can keep each other interested."', "terms"),
      c('"You have tempted me. You have not quite won me."', "slow"),
      c('"I want your company. I do not want a romance with you."', "company")),
    n("terms", "Vellexia", '''"Then hear what you are getting, before you become fond of imagining me in your rooms."
"Go on."
"I am not becoming harmless for you. My quarrels are a considerable pleasure to me, and I shall go on having them. If I invite you into one, try to be worth the invitation."
{n}She watches you take that in, and seems to enjoy it.{/n}
"Contradict me when you must. I shall enjoy discovering how cleverly you do it, and I shall punish you when you do it badly. I may punish you anyway. You may decide I am not worth it."
"That is more honest than a promise you would resent."
"It is less flattering. I find I do not care."
{n}She draws the shell a little nearer.{/n}
"Keep your other amusements, darling. I keep mine. But when you come to me, I expect to be the one you cannot stop thinking about, and if I ever find I am not, I shall take it very personally."
"Then make me want to come back."
"Oh, I intend to. And I intend to make you resent every interruption."''',
      c('"I know the woman I am asking for. I want her."', "near"),
      c('"Another evening first. I have not finished making up my mind."', "slow")),
    n("near", "Vellexia", '''"Come a little nearer the glass," she says. "I would like to see your face when I stop explaining myself."
{n}You lift the shell. Her image grows clearer as she adjusts her own. For a moment the practical business of finding a comfortable position makes you both laugh.{/n}
"We have selected an inconvenient distance for this conversation," you say.
"An exquisite inconvenience. I can imagine what I would do if you were here without being distracted by whether my earring has caught in your collar."
"What would you do?"
"Ask you to put the shell down. Then discover whether you come to me before I have finished asking."
{n}Her voice lowers. She describes the kiss she would like to give you, the pause afterward and the pleasure of finding you still close. Nothing reaches through the glass. Your own breath catches anyway.{/n}
"Tell me what you want," she says. "I have spent enough of this evening listening to myself be brave."''',
      c('[Tell her how you would welcome her, and keep the private conversation between you.]', "desire"),
      c('"Tonight I want your voice and an unhurried conversation. The rest can wait."', "gentle")),
    n("desire", "Vellexia", '''{n}You tell her. She listens without the interruption you expected, then makes you repeat one part more slowly, twice. Her answer is a low laugh and a promise to make the next kiss worth resenting the glass between you.{/n}
{n}The conversation grows intimate without pretending the distance has disappeared. You learn which pauses she enjoys and which make her ask whether you have begun composing something too polished to say. She learns that you can make her lose her place in a sentence without being in the room.{/n}
"I was saying something excellent," she complains.
"You can begin again."
"I would rather hear what you were about to say. A shameful failure of discipline."
{n}Later, when the eagerness has quieted, neither of you closes the cover immediately. She asks you a small question about where you are sitting, and you answer without trying to make the place worthy of her.{/n}
"I would like to know that room," she says. "Not tonight. Tonight this has been enough to make tomorrow inconvenient."''',
      c('[Tell her you want another evening as her lover.]', flags=("vellexia.departure_kept", "vellexia.renewed_lovers", "vellexia.committed"))),
    n("gentle", "Vellexia", '''"Then give me something unpolished to listen to. I refuse to spend a quiet evening hearing a visitor become solemn because nobody is touching them."
{n}You tell her about a small irritation from your day. She offers a solution so excessive that you begin laughing before she finishes. She looks pleased, then asks what you actually did.{/n}
"That worked?"
"Well enough."
"How disappointing. I had almost enjoyed my version."
{n}You keep talking. At one point she rests her cheek against her hand, listening, and the familiar expression becomes unexpectedly intimate when you realize she is making no attempt to improve it for you.{/n}
"There," she says after a long silence she clearly enjoyed. "I shall remember this when you are close enough to kiss. Do try to survive the anticipation; I intend to make it as unpleasant for you as possible."
"I was going to ask whether you wanted another evening."
"An excellent substitution. Yes."''',
      c('[Tell her you want another evening as her lover, and let her make you wait for it.]', flags=("vellexia.departure_kept", "vellexia.renewed_lovers", "vellexia.committed"))),
    n("slow", "Vellexia", '''{n}She leans back. The disappointment in her face is plain enough that she does not bother denying it.{/n}
"You make an unfinished answer sound very deliberate. I shall have to believe you mean it."
"I do."
"You are determined to remain unfinished. Very well. I shall choose a more tempting occupation for the next evening, and you will regret every one of tonight's scruples."
{n}She turns the shell slightly, adjusting a reflection that has crossed the glass.{/n}
"Spare me an apology. Tell me something worth hearing while I decide how offended I wish to be. I have not decided yet; it depends on the story."
{n}You ask about the earring. She tells you why its maker hates the woman who owns the matching piece, and the conversation wanders into a feud ridiculous enough to please her without needing to become yours.{/n}
"Come back with something more interesting than an apology," she says before the cover closes. "I may yet decide to make you regret this answer. I may enjoy it."''',
      c('[Keep calling her.]', flags=("vellexia.departure_kept", "vellexia.renewed_slow"))),
    n("company", "Vellexia", '''"An unequivocal answer. I had hoped for a more flattering one."
{n}She turns her head away, then back.{/n}
"I can enjoy a person who does not want to kiss me. I have managed it before, though I prefer being wanted."
"I would like our conversations to continue."
"Then allow me the pleasure of being offended. I was expecting a considerably more flattering answer, and I had already decided what to wear for it."
{n}You let her be offended. After a while she tells you that Tessar demanded her last payment before letting Ilveris hear the corrected account, and held the door shut on his man until the silver was counted; the clerk, it seems, has learned something in her house worth keeping.{/n}
"I considered correcting the omission," Vellexia says. "Then I decided I preferred having one person leave my house surprised."
{n}The conversation finds its way back to ease gradually. Before closing the cover, she orders you to return with a better story, and does not wait to hear whether you will.{/n}''',
      c('[Accept another conversation as company, not courtship.]', flags=("vellexia.departure_kept", "vellexia.renewed_company"))),
], "vellexia.verdict_kept", chapter=5)

s("the_voice_after_the_abyss", "A different room for the same voice", "[Answer the echo shell in Drezen.]", [
    n("start", "Narrator", '''{n}A pale thread moves beneath the cover of the shell while the sounds of Drezen pass outside your room. For days it has shown no light at all; your war has been loud, and she has been, by her own later account, busy elsewhere.{/n}
{n}When you answer, Vellexia is looking away. She turns sharply at the sound of your voice, then composes her expression with enough care to reveal what she is concealing.{/n}
"You have become inconveniently difficult to reach," she says. "I considered taking offense. Then I discovered I preferred hearing whether you were still capable of offending me yourself."
"I am here."
"So I hear. I would like to see it without the glare from whatever lamp you have placed behind you."
{n}You turn the shell until the image clears. She leans nearer, and for a moment says nothing.{/n}''',
      c('"I wanted to hear you again."', "lovers", requires=("vellexia.renewed_lovers",)),
      c('"We left a question open. I have not forgotten it."', "slow", requires=("vellexia.renewed_slow",)),
      c('"I have missed our conversations."', "company", requires=("vellexia.renewed_company",)),
      c('[Close the cover until you can speak without interruption.]', abort=True)),
    n("lovers", "Vellexia", '''"Yes. So did I. I had an excellent complaint prepared, but it required you to have been careless rather than absent. I may save it for a more suitable occasion."
{n}Her fingers rise toward the edge of the glass. She lowers them again with a small, impatient laugh.{/n}
"I dislike this part of the arrangement. I want to touch your face and discover whether you look as tired as the shell insists."
"I could tell you I am perfectly rested."
"You could. I would enjoy the lie for approximately as long as it took you to finish it."
{n}You tell her something true about the last days. She interrupts only to demand the detail you had tried to make less unpleasant, and then asks whether you have had a quiet hour since, in a tone that implies you had better say no.{/n}
"This one may have to do," you say.
"Then put the shell somewhere your arm will not ache. I refuse to be remembered as an inconvenient weight when I have gone to considerable trouble to be a voice."''', c('[Settle in and ask what became of her own business.]', "result")),
    n("slow", "Vellexia", '''"Good. I would have resented being the only one who remembered leaving it there."
{n}She watches your face for a moment before sitting back.{/n}
"You are back. Excellent. Tell me what has made that room so unworthy of my attention. I have spent enough time imagining it to distrust the picture."
{n}You describe the room without improving it. She asks which sounds come through the door, then whether the chair is comfortable.{/n}
"That is the room in which you are choosing to hear me?"
"At present."
"I shall attempt not to compete with the chair. It has had a considerable advantage in becoming familiar."
{n}Her smile returns as she finds a new detail to mock.{/n}
"You may ask about my days too. Some of them contained things besides waiting to see whether this expensive shell was broken."''', c('[Ask what became of Ilveris and the account.]', "result")),
    n("company", "Vellexia", '''"You should. I have been obliged to have several without you. In one of them a man explained a joke to me after I had laughed at it. I wanted to preserve the experience for someone capable of sharing my disgust."
"You could have closed the conversation."
"He was in the room. I had neglected to put a lid on him."
{n}She looks amused by the possibility, then turns her attention back to you.{/n}
"I am pleased you returned. There. A remarkably plain sentence. You may receive it without requiring me to repeat the accomplishment."
{n}You tell her a small thing about Drezen. She asks a question sharp enough to turn the account into a story, and for a while the interruption feels wonderfully familiar.{/n}
"Now," she says, "you may inquire after the consequences of our enterprise. I have been waiting to tell someone who remembers which parts I chose badly."''', c('[Ask for the actual outcome.]', "result")),
    n("result", "Narrator", '''{n}Vellexia has put the final account into the same narrow case that once held Ilveris's silk. She opens it where you can see the papers arranged inside.{/n}''',
      c('[Ask about the published corrections and the circlet she kept.]', "papers", requires=("vellexia.account_published",)),
      c('[Ask whether Ilveris paid after losing his wager.]', "won", requires=("vellexia.wager_won",)),
      c('[Ask what became of the circlet she lost.]', "lost", requires=("vellexia.wager_lost",)),
      c('[Ask whether Ilveris managed to describe the hour she bought with the forfeit.]', "fate", requires=("vellexia.fate_hour",))),
    n("papers", "Vellexia", '''"The corrections circulated. One purchaser obtained a repayment. Another bought a new prediction because he believed Ilveris would be especially careful after being caught. I cannot prevent people from investing in their own foolishness."
{n}She lifts the circlet, lets the light pass along its edge, and returns it to the case.{/n}
"The man who thanked me for the account sent a second letter asking whether I might advise him about his lover. I declined. Our accuracy seems to have given him an inflated opinion of my generosity."
"Does Ilveris still sell predictions?"
"Under another title. Fewer guarantees, more language about possibility. He is learning to charge for the part no one can disprove."
{n}Her smile sharpens.{/n}
"We did not make him honest. We made that particular dishonest account expensive. I am content to have accomplished something with an ending."''', c('[Ask about Tessar.]', "tessar")),
    n("won", "Vellexia", '''"He paid. Reluctantly, which improved the pleasure. The witnesses were purchasers with deposits of their own; they had no interest in admiring his explanation instead of collecting."
{n}She lifts the circlet, then slides it onto one finger.{/n}
"He sent a private letter suggesting that my having known his answer invalidated the prediction. Tessar returned a copy of the terms he signed. He complained that her handwriting had become insolent since she left his employment."
"Had it?"
"I like to think so."
{n}She turns her hand to consider the silver.{/n}
"The theater's maker has acquired several commissions. I have refused two invitations to hear patrons explain how much better they understand the joke than everyone else. The little emperor deserved a less tiresome triumph."
"Would you watch it again?"
"Perhaps. I should like the maker to spend a little longer wondering whether he has pleased me. It improves his work."''', c('[Ask what Tessar chose next.]', "tessar")),
    n("lost", "Vellexia", '''"Ilveris sold it. That offended me more than winning it. He had no intention of wearing the thing; he wanted to turn the account of my loss into a price."
"Will you buy it back?"
"Not at the price he has taught its new owner to request. I made the piece. I know exactly which of its virtues he has misunderstood in the advertisement."
{n}She shows you the empty space in the case, then closes it.{/n}
"I have begun another design. It is not a replacement, and if you soothe me by pretending the loss improved my work I shall break the shell. I liked the old piece. I shall enjoy making its new owner discover precisely how much."
"You bought an excellent hour. You can still resent the bill."
"I intend to. For centuries, if necessary."
{n}She tells you Ilveris has had less success selling his one accurate prediction than he expected. Too many listeners ask why a woman who knew she would lose chose the hour anyway.{/n}
"His answer becomes duller each time. Mine remains mine."''', c('[Ask about Tessar\'s work.]', "tessar")),
    n("fate", "Vellexia", '''"He has described it in three incompatible ways. A concealed trick, a confession that he had won, and an entertainment he generously permitted me to purchase. I expect a fourth as soon as he finds a new audience."
"He did receive the circlet."
"Yes. I have not disputed the forfeit. It ruins his more indignant explanations when someone points that out."
{n}She taps the edge of the closed case.{/n}
"I remember the repeated hour. I have not discovered a secret by which everything becomes new again. I am still capable of hearing a familiar line and wanting its speaker silenced. You may retain your opinion of my character."
"I had no intention of revising it without asking you."
"How prudent."
{n}Her expression softens into amusement.{/n}
"I also remember wanting one part again. I find that worth keeping. It requires less explanation than Ilveris would prefer."''', c('[Ask what Tessar made of the finished account.]', "tessar")),
    n("tessar", "Vellexia", '''"Tessar chose her next work herself. I offered another commission. She declined it, politely enough to make it difficult to enjoy being insulted."
"Why?"
"She wants two patrons who cannot agree on a reason to dismiss her. I understood the calculation. I disliked being included in it."
{n}Vellexia checks the clasp of the case while you speak.{/n}''',
      c('[Ask about the sample carrying both your names.]', "named", requires=("vellexia.named_sample",)),
      c('[Ask about the limited sample and your attestation.]', "limited", requires=("vellexia.limited_sample",))),
    n("named", "Vellexia", '''"It found her work quickly. It also found her a man who assumed she could provide an introduction to you. She sent him your permission to use the account and asked him to point to the part promising your company."
"What did he say?"
"Nothing worth preserving, apparently. She took a different commission."
{n}Vellexia sounds pleased with a reply she has not been permitted to claim as her own.{/n}
"Your name was useful. It was also troublesome. She has begun charging for the trouble rather than pretending it is an honor. I suspect she will do well enough to become irritating in a new way."''', c('[Let the completed work remain completed.]', "end")),
    n("limited", "Vellexia", '''"It took her longer. One employer declined to consider an anonymous example, despite your attestation. Another asked to see a second, smaller account, and hired her after she corrected his estimate of the work."
"Was she disappointed?"
"Certainly. She preferred obtaining work quickly. She found a patron who wanted an account, not an introduction she could not sell. How fortunate for his purse."
{n}Vellexia rests her hand on the case.{/n}
"I would have chosen differently. She knows. She sends the account; I send the silver; our opinions of one another remain exquisitely overpriced."''', c('[Let the completed work remain completed.]', "end")),
    n("end", "Vellexia", '''"Enough of Ilveris. I refuse to let him occupy another evening I could spend being admired."
"What occupation would you prefer?"
"An evening with no use in it at all. Do something in that room you would do if I were not watching, and let me watch anyway."
"And you?"
"I shall choose something here. We will discover whether the two pleasures tolerate being interrupted by conversation."
{n}She looks past the shell toward her own room, apparently considering several possibilities.{/n}
"No witnesses, no wager. I intend to discover whether you can amuse me without either. If you cannot, I shall tell you so, at length, and you will enjoy it less than I do."''',
      c('[Agree to another private call.]', flags=("vellexia.return_kept",))),
], "vellexia.departure_kept", chapter=5)

s("two_unremarkable_pleasures", "What she does with an unclaimed evening", "[Open the shell for the evening you agreed to share.]", [
    n("start", "Narrator", '''{n}You have set aside one small occupation you would ordinarily attempt alone: sorting the loose pages that have accumulated among your personal things. Some deserve to be kept. Others have survived because deciding what to do with them seemed less urgent than putting them down.{/n}
{n}Vellexia answers beside a table crowded with tiny stoppered bottles. She is holding one beneath her nose, looking profoundly dissatisfied.{/n}
"Awful," she says. "I had almost forgotten how much I disliked it. A useful beginning."
"Perfume?"
"Old perfume. Mine. I am deciding which scent I was foolish enough to associate with a marvelous evening. I suspect the evening did most of the work."
{n}She looks at the papers beside your shell.{/n}
"You have brought your own small excavation. Excellent. We can be disappointed at separate tables."''',
      c('[Tell her about a page you have been reluctant to throw away.]', "page"),
      c('[Postpone until you can keep the evening clear.]', abort=True)),
    n("page", "Vellexia", '''{n}You show her a rough drawing of an inn's roofline. It is poor work, made during an idle moment, and you have kept it longer than several more useful records.{/n}
"Did you like the place?" she asks.
"For a while."
"A remarkably sufficient reason to keep a poor drawing. I approve."
"You would have thrown it away?"
"I would have commissioned a better one and resented finding that it reminded me of the artist instead. I have made that mistake before."
{n}She uncorks another bottle, considers it and sets it to one side.{/n}
"That one is tolerable. It reminds me of a man who tried to flatter me by claiming he had never enjoyed anything so much as my company. I asked him what he had compared it with. He answered 'everything.' We had almost nothing to discuss afterward."
"You kept the scent."
"Yes. It has outlived the conversation. Not an exacting achievement."
{n}She waits while you decide where to put the drawing.{/n}''',
      c('[Keep the drawing, imperfect and familiar.]', "keep"),
      c('[Set it aside to discard. Tell her what you will remember without it.]', "discard")),
    n("keep", "Vellexia", '''"There. A choice no purchaser can make more flattering by paying for it."
{n}You put the drawing among the things you intend to keep. Vellexia takes the first, disliked bottle and sets it beside the tolerable one.{/n}
"I am keeping this too," she says. "For the pleasure of discovering that I was right to dislike it. A meaner attachment than yours, perhaps, but it is mine."
"Would you wear it?"
"Certainly not. Possessing a mistake does not oblige me to repeat it on my skin."
{n}She looks up, smiling at your expression.{/n}
"You hoped I would throw it away and become easier to understand. I could see the beginning of the hope."
"I was wondering how many bottles you keep for that reason."
"An excellent question. We may need another evening to answer it."''', c('[Ask which scent she actually wants tonight.]', "chosen")),
    n("discard", "Vellexia", '''{n}You set the drawing aside and describe the sound of rain above the inn's window, the smell of a meal from downstairs and the idle time in which you made it. Vellexia listens without asking you to turn the recollection into an occasion worthy of a better artist.{/n}
"I understand keeping that," she says. "Though I would probably keep the paper too and complain that it occupied space."
"You could commission a cabinet for the complaint."
"I have several. You are beginning to understand my household."
{n}She removes one bottle from the table and puts it out of reach.{/n}
"That one will go. It reminds me of an evening I have described so often that I am tired of hearing the account in my own head. If I miss it, I can be annoyed about having discarded it. A new subject, at least."''', c('[Ask which scent she actually wants tonight.]', "chosen")),
    n("chosen", "Vellexia", '''{n}She opens a small bottle with no label, tests it and touches one drop behind her ear.{/n}
"This one. I cannot remember who gave it to me. That leaves the scent with an unusual amount of freedom."
"Describe it."
"Bitter at first. Something warmer beneath it. Your world has a fruit whose peel does almost the same thing when one presses it between the fingers. I never remember the name until someone says the wrong one."
{n}You offer possibilities. She rejects several, laughs at another and finally accepts one with the satisfaction of having made you do the remembering.{/n}
"There. Now tell me something from your room I cannot smell through this troublesome glass."
{n}You tell her about ink, paper and the air coming through the window. The exchange is intimate in its small inaccuracies. Each of you asks questions the other would not have thought to answer.{/n}
"I would like to be able to get that wrong in person," she says. "To tell you the room smells of something you have stopped noticing."
{n}She pauses before adding anything to the wish.{/n}''',
      c('"Come to Drezen. I want considerably less glass between us."', "meeting", requires=("vellexia.renewed_lovers",)),
      c('"For tonight, tell me what you would say if you were here."', "voice"),
      c('"Stay on the shell tonight. Tell me what you would do if you were here."', "voice", requires=("vellexia.renewed_slow",))),
    n("meeting", "Vellexia", '''"Yes. You have a city full of people who would reasonably dislike my arrival. I have a city full of people who would enjoy mistaking yours for an announcement. I can imagine several entertaining mistakes and very few convenient introductions."
"The shell does not carry people."
"I noticed. I have had considerable reason to resent the limitation."
{n}She leans nearer the glass.{/n}
"An invitation. Into a crusader city, into a crusader's bed. How deliciously improper." {n}Her eyes narrow with pleasure.{/n} "Say it properly, then, so that I can hold you to it. I want to see the face you make when I finally put this shell down."
"Come to Drezen. Come to me."
"How inconvenient. You have made me want a room that is not mine. I shall come when it suits me, and you will not know the night."
{n}She touches her finger to her mouth, then rests it beside the shell.{/n}
"For tonight, stay where I can hear you. I have been thinking about the last time you were close enough to interrupt me without speaking."''', c('[Stay on the shell with her until the lamp burns down.]', flags=("vellexia.private_kept", "vellexia.invited"))),
    n("voice", "Vellexia", '''"I would probably complain about the chair first. Then I would want to know why you kept one of those pages and discarded another. At some point you would ask whether I had come merely to criticize your room."
"Had you?"
"No. I would have come because I wanted you, and I take what I want. I would hope you had noticed before making me admit it so inelegantly."
{n}She closes the bottle she chose and puts the others away one by one. The little clinks accompany your conversation until the table is almost clear.{/n}
"I am here for the same reason now," she says. "You may imagine the complaint about the chair if it makes the admission easier to believe."''',
      c('[Enjoy the quiet affection between lovers.]', "lovers", requires=("vellexia.renewed_lovers",)),
      c('[Stay for her company.]', "company_end", forbids=("vellexia.renewed_lovers",))),
    n("lovers", "Vellexia", '''{n}You talk until the pages beside you have been sorted or abandoned. Vellexia asks you to leave the shell open while she unfastens the earring that has begun to catch in her hair. She complains about its maker with an inventiveness that makes it difficult to answer soberly.{/n}
"Do not laugh too much," she says. "I may remember you fondly whenever it annoys me. An association you might regret."
"I can think of worse."
"So can I. I prefer this one."
{n}After a while her voice grows quiet. She asks what kind of kiss you would want if the distance were less considerable. You tell her, and the silence after your answer has nothing vacant in it.{/n}
"I would like that," she says. "Keep the rest. I want something to take from you that you have not described perfectly in advance."
{n}She names the hour of the next call as if it were a summons, and closes the cover before you can agree.{/n}''',
      c('[Keep the evening and promise another call.]', flags=("vellexia.private_kept",))),
    n("company_end", "Vellexia", '''{n}The conversation lasts longer than the sorting. Vellexia asks which discarded page was easiest to release, and you tell her. Her answer is an account of something extravagant she kept solely because an enemy had offered to buy it.{/n}
"Did you want it?"
"Less than he did. That was sufficient at the time."
{n}She sounds amused by the comparison rather than chastened. Before the evening ends, she asks whether you have room for another conversation soon.{/n}
"I have enjoyed this one," she says. "There is no invoice to explain the remark. Do not make me regret having said it aloud."
{n}She closes the shell while you are still laughing at her last insult, which she clearly considers a victory.{/n}''',
      c('[Keep the evening and promise another call.]', flags=("vellexia.private_kept",))),
], "vellexia.return_kept", chapter=5)

s("the_cover_before_the_battle", "Before the next silence", '"I want to speak before I leave again."', [
    n("start", "Vellexia", '''{n}When Vellexia answers, a servant is removing a vase from the table behind her. She stops him at the door.{/n}
"The flowers may go. The vase stays. I disliked the giver, not the workmanship."
{n}He returns the empty vase and leaves. She waits until the door has closed before bringing the shell nearer.{/n}
"You have the look of someone who has been saying important things all day. I had hoped to provide an interruption."
"You still can. I wanted to tell you that I am preparing to leave again. The next part may be difficult to come back from."
"Yes. People seldom arrange a war around the convenience of my correspondence."
{n}The remark costs her more effort than usual. She rests her fingers on the rim without touching the cover.{/n}
"How much time do you have now?"
"Enough for you to waste on me."
"A useful answer. I dislike being given a farewell so complete that nothing I say can change its shape."
{n}She moves the empty vase out of the glass's view.{/n}
"Tell me what you came to ask. Then I shall tell you whether it is the thing I wanted to hear."''',
      c('"I want another evening with you when I return. I cannot say when that will be."', "absence"),
      c('"Before I go, tell me whether you still want me."', "meaning"),
      c('"I want this to be our last call. I cannot keep offering what you want."', "ending"),
      c('[Explain that you must go now and ask to return to the conversation.]', abort=True)),
    n("absence", "Vellexia", '''"I would rather know that than sit here interpreting every quiet evening as an insult. I can invent sufficiently unpleasant explanations without your assistance."
"You might have reasons of your own not to answer."
"I have many. Some are even respectable. I will not leave the cover open as a demonstration that I deserve your return."
{n}She glances toward the door, then back at you.{/n}
"There is a performance next week. A singer I have dismissed twice intends to sing the same piece again, apparently because she believes I missed its finer qualities while objecting to the middle. I intend to go and find out whether she has acquired better reasons or merely greater confidence."
"You sound pleased."
"I am looking forward to being difficult about something familiar. I had not intended to admit that today."
"Then tell me about it if I come back."
"I might. You may have to hear me complain about it first."
{n}Her fingers relax against the rim.{/n}
"I want you to return. I shall continue doing exactly as I please while you are away, and some of it would make your chaplains faint. Both are true, however poorly they flatter a dramatic farewell."''', c('[Tell her what you want the next answer to mean.]', "meaning")),
    n("meaning", "Vellexia", '''"You are not my whole life," she says. "Do not flatter yourself. But you have become a part of it I would notice losing, and I do not lose things. I have them taken from me, and then I take them back."
{n}She looks at the shell's silver edge with a brief, dissatisfied smile.{/n}
"I made this so that I could shut out a tiresome visitor. Now I notice when it stays dark. I find that sufficiently irritating without having to call it an improvement in my character."
"Then admit you miss me."
"I have never in my life been ashamed of wanting. It is the part where the person has an answer of their own that makes such trouble. Love is a game in which somebody bares their throat, darling. I have simply never before been unsure which of us it would be."
{n}She meets your eyes again.{/n}
"What do you want that answer to be, if we have another evening?"''',
      c('"I want to remain your lover. I have not finished tempting fate."', "lovers", requires=("vellexia.renewed_lovers",)),
      c('"I want you as my lover. Tell me you still want me."', "new_terms", requires=("vellexia.renewed_slow",)),
      c('"I want this friendship. I do not want to turn it into a romance."', "friends", forbids=("vellexia.renewed_lovers",)),
      c('"Another evening first. I have not settled that question."', "slow", requires=("vellexia.renewed_slow",)),
      c('"I want to end this. I will close the shell."', "ending", requires=("vellexia.renewed_lovers",))),
    n("new_terms", "Vellexia", '''{n}Her smile comes before the answer.{/n}
"Yes. I dislike the timing, but I want you. You have managed to make both statements rather urgent."
"Tell me what you want."
"You, darling. Your mouth, your insolence, and the delightful belief that I shall still want them tomorrow. You will spend the rest of your life wondering whether I do. That is the game. Do you remember what I told you about it? You must deceive yourself, a little, or it is no fun at all."
{n}She pauses, watching your face, and her smile has teeth in it.{/n}
"I am not becoming harmless. I shall keep my house and my quarrels and my appetites, and you will not ask me to put any of them down. Do not praise me tonight and hope to wake beside a better woman. I should find your disappointment delicious."
"I know who I am asking."
"Then ask me again when there is less glass between us. For now, I would like to hear that you mean it."''',
      c('"I remember. I want you anyway. Come to Drezen before I march, and I will say it with no glass at all."', "new_lovers"),
      c('"Not yet. Keep tempting me."', "slow")),
    n("lovers", "Vellexia", '''"Good. I wanted to hear it before discovering how extravagantly I might resent a different answer."
{n}She brings the glass closer and studies your face with frank proprietary interest, as if checking a possession for damage.{/n}
"You look tired. How vexing. I had intended to monopolize every remaining scrap of your attention, and now I find I want to hear you speak even when the words are not impressive. That has never happened to me before, and I blame you for it."
"I want to come back. I want to hear you complain about the singer."
"There. Appalling flattery. Almost nothing in it for anyone but me."
{n}Her laughter is brief and warm.{/n}
"I want another kiss," she says. "The fact that I cannot have it now has not made the wish more dignified. Tell me how you would leave if you were standing here."''',
      c('[Describe a lingering kiss and let her answer in her own words.]', "warm"),
      c('"I would hold your hand a while. Then I would go when I had to."', "quiet"),
      c('[Invite her] "I would not leave. You would come here. Drezen, before I march, and no glass at all."', "invite")),
    n("invite", "Vellexia", '''{n}For a moment she says nothing. Then she laughs, low, delighted and not at all kind.{/n}
"Into a crusader city. Into a crusader's bed, on the eve of a battle, with the whole garrison listening at the shutters." {n}She draws the shell so close that her mouth fills the glass.{/n} "Yes. I shall come when it suits me, and you will not know the night, and you will spend every evening until then wondering whether this is the one. Consider it your first payment."
{n}The glass clouds while she is still smiling.{/n}''',
      c('[Leave the shutters unlatched.]', flags=("vellexia.farewell_kept", "vellexia.farewell_lovers", "vellexia.invited"))),
    n("new_lovers", "Vellexia", '''"An invitation. Very well, I accept, and you will not know the night. Come nearer. I have waited through enough careful answers to enjoy this one without pretending I was indifferent to it."
{n}You lift the shell. She tells you where she would put her mouth if the glass were gone, and in what order, and your answer makes her close her eyes for a moment.{/n}
"An inconvenient thing to hear just before you leave. I intend to remember it."
{n}You talk until the impending departure becomes something you can mention without allowing it every sentence. She asks for one ordinary detail of your morning and laughs at the answer.{/n}
"Keep yourself alive if you can," she says at last. "I want more of this particular person. I have no use for a monument that cannot answer back."
{n}You say goodbye as lovers. The cover closes after she has said it too.{/n}''',
      c('[Promise to come back to her.]', flags=("vellexia.farewell_kept", "vellexia.farewell_lovers", "vellexia.committed", "vellexia.invited"))),
    n("warm", "Vellexia", '''{n}You tell her. She answers with a soft correction to the way you imagined her hands, then asks you to begin again. This time she lets the description finish.{/n}
"Yes," she says. "That is a departure I would resent properly."
"Properly?"
"With enough pleasure to make the next arrival worth anticipating."
{n}For a while you speak quietly about what you want from that arrival. Neither room changes. Her voice is enough to make the distance feel personal, something between two bodies rather than a line on a map.{/n}
"Go when you must," she says. "I dislike rehearsing it."
{n}You tell her you have to leave. She asks for another breath, and you give it before saying goodbye. Her answer is unadorned. She keeps looking at you until you close the cover.{/n}''',
      c('[Keep the affection and the farewell you gave each other.]', flags=("vellexia.farewell_kept", "vellexia.farewell_lovers"))),
    n("quiet", "Vellexia", '''"Only my hand? You are determined to leave me hungry. How fortunate for you that I have a long memory, and a longer appetite, and that you are coming back."
{n}She rests her hand beside the shell. You put yours where she can see it. There is silver under your fingers, no borrowed sensation passing between them.{/n}
"There," she says. "A poor substitute. I am glad you suggested it."
{n}You sit together until it is time to go. She asks what you will wear when you return, as though she has already appointed herself its most demanding critic, and then describes in detail what she will do to it.{/n}
"I want the next answer," she says when you stand. "I shall not pretend I have it already."
{n}You tell her goodbye. She answers before the glass clouds.{/n}''',
      c('[Keep the quiet affection and the farewell.]', flags=("vellexia.farewell_kept", "vellexia.farewell_lovers"))),
    n("friends", "Vellexia", '''"Friendship, then. Bring me someone worth insulting. I refuse to spend it being congratulated on my restraint, and I warn you that I have none."
{n}She settles back and angles the shell toward her, bringing the empty vase into the edge of the image again.{/n}
"I have enjoyed your company. I expect to find you irritating again, if you return with enough energy to have opinions. I would rather risk that than have you agree with me as a farewell gift."
"I was not planning to."
"Good. There is an improvement to the singer's middle passage I would like to propose, and you may be just unreasonable enough to tell me why she would refuse it."
{n}You discuss the proposal. It is lavish, insulting and almost certainly calculated to make Vellexia the subject of the performance. She defends it with increasing pleasure as you object.{/n}
{n}When you leave, the last sound before the cover closes is her laughter at something you said. You find yourself smiling after the room has gone quiet.{/n}''',
      c('[Keep her friendship.]', flags=("vellexia.farewell_kept", "vellexia.farewell_friends"))),
    n("slow", "Vellexia", '''"You have made patience an unexpectedly demanding entertainment."
"I am not asking you to wait for a different answer."
"Very well. Remain mysterious a little longer. You will have to compensate me with a better story, and I shall decide what it costs."
{n}She turns the shell slightly, removing the lamp's reflection from its glass.{/n}
"There are things I would like to ask you that have nothing to do with persuading you into my bed. Some of them are even about you. You may find the novelty irresistible."
"You could try one now."
{n}She does. The question concerns a place you miss, and she listens long enough to ask a better second question. Her own answer is less tender: she misses the view from a balcony because she once enjoyed watching a rival discover that his procession had taken the wrong street.{/n}
{n}The departure arrives during an argument about whether she arranged that mistake. She refuses to improve the story by answering too soon.{/n}
"Ask another time," she says. "I may still refuse."
{n}You say goodbye without turning the uncertainty into a pledge. She sends you away with a smile.{/n}''',
      c('[Keep calling her, without promising romance.]', flags=("vellexia.farewell_kept", "vellexia.farewell_slow"))),
    n("ending", "Vellexia", '''{n}Her hand leaves the rim.{/n}
"How disappointing. I had begun making rather extravagant plans for you, and now I shall have to make them for somebody duller."
"I meant what I offered before."
"At least you cannot give the pleasure back. I shall keep that much, as I keep everything."
{n}She studies you for a moment longer.{/n}
"Close your shell. I find that I would rather resent you without interruptions. If I ever open mine again, it will be because I have thought of something unforgivable to say, not because you have found a more elegant explanation."
"I will not call."
"You will want to. That will be my pleasure, not yours."
{n}She draws the cover toward her. Before it closes, she looks back once.{/n}
"I enjoyed the part you cannot give back. Remember that whenever you are tempted to become noble about having spared me something. You spared me nothing. I took it."
{n}The glass clouds. No light follows it.{/n}''',
      c('[Let the glass go dark.]', flags=("vellexia.farewell_kept", "vellexia.closed"))),
], "vellexia.private_kept", chapter=5)


def ending(id, title, text, requires=(), forbids=(), owner="Epilogue", paragraphs=()):
    SCENES.append(scene("vellexia.ending_" + id, title, owner, 0, "", [
        n("start", "Narrator", text, portrait="Vellexia", paragraphs=paragraphs)], Relationship="vellexia", last=99,
        requires=("vellexia.prediction_known", *requires), forbids=forbids))


BAD_END = ("vellexia.dead", "vellexia.mirrored", "vellexia.native_coercion", "vellexia.early_fight", "vellexia.final_fight")
ORDINARY_BLOCK = (*BAD_END, "vellexia.closed", "inhuman", "ascended", "sacrifice")
ending("lovers", "A light beneath the cover", '''{n}Vellexia remained a difficult lover. She called at inconvenient hours and took offense when kept waiting, then neglected the shell herself for a week while a more promising guest amused her, and described the guest afterwards in more detail than was kind. The Commander learned to give as good as that, which she considered the finest compliment the Commander ever paid her.{/n}
{n}The echo shell carried affection as well as complaints. Vellexia discovered that the Commander remembered details she had included carelessly: an earring that caught in her hair, a singer's disputed passage, the name of someone she had hoped would feel suitably insulted. She pretended to regret having supplied such material and continued supplying it.{/n}
{n}Vellexia did not become gentle toward the world to enjoy any of it.{/n}''', requires=("vellexia.farewell_lovers",), forbids=ORDINARY_BLOCK,
    # Q11: the lovers' ending follows what actually happened in the flesh (vellexia_trickster: after.visit, after.night).
    paragraphs=(
        p('''{n}For a long time they were lovers across an inconvenient distance, and she made the distance into a weapon: a voice at the wrong hour, a description of her evening that left out exactly the part the Commander wanted, a promise to come to Drezen that she renewed and broke with equal pleasure.{/n}''',
          forbids=("vellexia.trickster.visited", "vellexia.trickster.night_kept")),
        p('''{n}She had come to Drezen once already, in person, to look the Commander over like a purchase, and she made a habit of reminding the Commander that she could do it again whenever she liked, and of not doing it.{/n}''',
          requires=("vellexia.trickster.visited",), forbids=("vellexia.trickster.night_kept",)),
        p('''{n}She came through the Commander's door when she pleased after that first night before the march, never on the night she was expected, and always left before morning with something of the Commander's she had decided to keep: a glove, a seal, a bruise.{/n}''',
          requires=("vellexia.trickster.night_kept",)),
    ))
ending("friends", "An argument worth continuing", '''{n}The Commander and Vellexia continued their friendship through the echo shell. Some invitations concerned performances, some an insult too elaborate to enjoy without an audience, and some no subject she cared to admit had been an excuse to call.{/n}
{n}She did not become a kinder patron through having acquired a friend. Disagreement sometimes delighted her and sometimes earned the Commander a week of exquisitely pointed silence, broken by a better question and an insistence that nobody call it an apology.{/n}
{n}There was pleasure in being remembered accurately. When she misquoted the old play to improve an insult, the Commander corrected her. Her delighted indignation kept the conversation alive long after either had intended to retire.{/n}''', requires=("vellexia.farewell_friends",), forbids=ORDINARY_BLOCK)
ending("slow", "An answer still open", '''{n}Vellexia kept calling when the Commander interested her, and spent the unanswered evenings upon whatever newer amusement presented itself. She never once waited faithfully for anything, and said so, often, in a tone that suggested she was waiting.{/n}
{n}There were other evenings in both their lives. The ones they spent speaking through the shell acquired jokes too old to explain to another listener and disagreements they returned to with suspicious enthusiasm. When Vellexia finally explained the procession and the wrong street, the Commander accused her of having delayed the best detail deliberately. She denied only that it had been the best.{/n}''', requires=("vellexia.farewell_slow",), forbids=ORDINARY_BLOCK)
ending("interrupted", "The last conversation", '''{n}No further call came. Vellexia had found other amusements, or decided that the Commander should wonder whether she had; the shell offered no explanation either way.{/n}
{n}The silver cover kept its small, familiar weight. One remembered laugh could not make it glow again.{/n}''', forbids=(*ORDINARY_BLOCK, "vellexia.farewell_kept"))
ending("closed", "A cover left closed", '''{n}Their correspondence ended. Vellexia did not send a gentler version of her last answer; she had never sent a gentle version of anything.{/n}
{n}She had enjoyed the Commander while she wanted the Commander, and she did not pretend otherwise. When a line from the old play reminded her, she laughed at the recollection, told the story to whichever guest was nearest, and did not open the shell.{/n}''', requires=("vellexia.closed",), forbids=(*BAD_END, "inhuman"))
ending("dead", "The unanswered request", '''{n}Vellexia died. The shell could carry no answer from her. It had never contained the woman whose voice had used it.{/n}
{n}The Commander remembered her appetite for novelty, her cruelty, and the rare pleasure of having genuinely surprised her. Death did not make her harmless in retrospect, and nobody who had been her guest pretended that it did.{/n}''', requires=("vellexia.dead",), forbids=("vellexia.mirrored",))
ending("mirror", "No voice borrowed from glass", '''{n}Vellexia remained imprisoned in the mirror, by the Commander's hand and with her own spell. The shell carried no answering voice.{/n}
{n}There was nothing to make the silence comfortable. The Commander could remember the woman who had offered the shell, and could guess, with some precision, what she would say if she were ever let out.{/n}''', requires=("vellexia.mirrored",))
ending("coercion", "The invitation cannot answer", '''{n}The Commander's demonic rage had frightened Vellexia into surrender. Her old invitations could not disguise what followed as affection, and she never pretended that they could.{/n}
{n}The shell stayed dark. Domination had ended the courtship, and the woman who had once laughed at the Commander across a ring tray kept her laughter for people she did not fear.{/n}''', requires=("vellexia.native_coercion",), forbids=("vellexia.dead", "vellexia.mirrored"))
ending("hostility", "The invitation overtaken", '''{n}Violence overtook the invitation Vellexia had made. The shell did not preserve a safe, unchanged hostess somewhere beyond the quarrel. An earlier pleasant hour was no guarantee that either could resume the conversation that followed it.{/n}
{n}There was no new agreement between them. The recollection of her laughter remained exact and insufficient.{/n}''', requires=(), forbids=("vellexia.dead", "vellexia.mirrored", "vellexia.native_coercion"))
SCENES[-1]["RequiresAny"] = ["vellexia.early_fight", "vellexia.final_fight"]
ending("changed", "Another kind of silence", '''{n}The Commander changed beyond the life in which the echo pair had first been offered. The old arrangement did not furnish a new one for that altered existence. No familiar signal appeared merely because the shell still had its cover.{/n}
{n}The voice she had pursued was gone. Vellexia kept the shell as one more expensive curiosity whose amusement had ended, and showed it to guests as a warning about wanting things.{/n}''', requires=("inhuman",), forbids=BAD_END)
ending("ascent", "A god is not an answer", '''{n}When the Commander ascended, Vellexia wanted to hear the account twice. Then she asked a question the messenger could not answer and dismissed him before he attempted to invent something flattering.{/n}
{n}A god might have other ways to call than a small silver shell. She waited to see whether this one would bother, and pretended to everyone, loudly, that she was not waiting.{/n}
{n}She kept the shell. Sometimes she resented its silence. Sometimes she was entertained by the thought of how much she would enjoy criticizing a divine entrance. No answer from the new power was recorded in the glass.{/n}''', requires=("ascended",), forbids=(*BAD_END, "inhuman", "vellexia.closed"))
ending("sacrifice", "What she wanted back", '''{n}The Commander's sacrifice left Vellexia with news she could neither bargain against nor improve by refusing to hear. She dismissed a visitor who began praising the magnificence of the loss. Later she sent for him to finish the factual part of his account.{/n}
{n}She wanted the Commander back, and resented every flattering account of the loss. Admiration was an intolerably poor substitute, and she said so to everyone who offered it, until they stopped.{/n}
{n}The shell stayed closed for a long time. When she finally opened it, she heard only the small sound of her nail against its rim. She closed it again before anyone entered the room.{/n}''', requires=("sacrifice",), forbids=(*BAD_END, "inhuman", "ascended", "vellexia.closed"))
ending("aeon", "An invitation not made", '''{n}In the history remade without the Worldwound, the Commander did not travel the same road to Vellexia's rooms. The offered shell, the dispute over predictions and the private answers that might have followed had no unchanged place in that world.{/n}
{n}Vellexia's appetites belonged to her own life. No memory of an erased visitor arrived to turn them into a promise she had never made.{/n}''', owner="AeonEpilogue")


def integrate(payload):
    payload.setdefault("SeenCues", {}).update(SEEN_CUES)
    payload.setdefault("SelectedAnswers", {}).update(SELECTED_ANSWERS)

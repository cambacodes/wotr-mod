"""A living Vellexia correspondence campaign after her native peaceful dismissal.

The early token and later rivalry are authored fiction, not native actor recovery.
Remote scenes do not place Vellexia physically in the Commander's camp or capital.
"""
from story_format import c, n, scene
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


def s(id, title, entry, nodes, previous, chapter=4, local=False, delay=24):
    for page in nodes:
        page["Portrait"] = "Vellexia"
    extra = dict(Relationship="vellexia", Chapters=[chapter], last=chapter, optional=True)
    if local:
        extra.update(ContactUnit=UNIT, Areas=[AREA], AnswerLists=[ANSWER_LIST])
        required = ("vellexia.greeted", previous)
        forbidden = (*BLOCKERS, "vellexia.arena_invited", "vellexia.native_finished")
    else:
        extra.update(Remote=True, Areas=[NEXUS if chapter == 4 else DREZEN])
        required = ("vellexia.dismissed_native", "vellexia.native_finished", previous)
        forbidden = BLOCKERS
    SCENES.append(scene("vellexia." + id, title, "Vellexia" if local else "Memory", chapter,
        entry, nodes, requires=required, forbids=forbidden, delay=0 if local else delay, **extra))


s("the_unused_reply", "A reply she has not written", '"You said I might return. What if I am somewhere you cannot hear me knock?"', [
    n("start", "Vellexia", '''{n}Vellexia has been selecting rings from a shallow tray. At your question she places two beside each other, studies the effect, and returns one to its compartment.{/n}
"You could write. People do. Some even improve in writing, though the delay deprives me of watching them discover that I disagree."
"Would you answer?"
"What a demanding question to ask before composing a sentence."
{n}She lifts a ring to the light. Its dark stone contains a moving thread of color, which twists when her finger passes over it.{/n}
"There are ways to send a voice," she says. "A few of them permit the recipient to decide whether to listen. I find those receive better answers, though fewer admirers request them."
"The others prefer certainty?"
"The others prefer access. Then they wonder why I grow tired of hearing them."
{n}She closes the ring tray and rests both hands on its lid.{/n}
"You have thought of leaving already. How very mortal. You stand in an interesting room and begin calculating how long it will take to reach another."''',
      c('"I want a way to ask for another conversation. You would still choose whether to have it."', "asking"),
      c('"I am curious what you would send when you had time to invent your entrance."', "entrance"),
      c('"We can discuss it another time."', abort=True)),
    n("asking", "Vellexia", '''"A surprisingly expensive distinction. I have punished people for failing to understand it."
"And do you understand it when someone is asking you to wait?"
{n}She looks up from the tray.{/n}
"Yes. Understanding a thing does not oblige me to enjoy it."
"Then we have something in common."
{n}Her smile appears slowly.{/n}
"You are asking for a door that can remain closed. I begin to see why I might want one too. There is a particular gentleman who sends an illusion of himself whenever he has composed a compliment. I have broken three of his messengers. He considers that evidence of my passion."
"Did you tell him otherwise?"
"With admirable clarity. He continues to have a poor ear."
{n}She rises and crosses to a cabinet. Its doors stand open; inside are cases too small to hold the grand curiosities displayed elsewhere in the house.{/n}
"Wait there. If I return with anything that speaks before it is opened, you may accuse me of failing to understand my own complaint."''', c('[Wait while she chooses something from the cabinet.]', "shell")),
    n("entrance", "Vellexia", '''"Naturally. A letter is an entrance one can rehearse without admitting it."
"You would admit it?"
"To the right audience. A little visible artifice makes the rest easier to overlook."
{n}She leans back, studying you with renewed amusement.{/n}
"I might send a line from that play and discover whether you had the patience to find the insult. Or a description of an evening whose most interesting guest never arrived. You would spend a pleasant moment wondering whether I meant you."
"Then I might ask."
"And spoil all that excellent uncertainty? You are determined to be an expensive correspondent."
{n}She rises and crosses to a cabinet of small cases. Her fingers hover over one, then choose another.{/n}
"We should give the recipient a way to decline the performance. I dislike a captive audience when I am one of its members. You may enjoy that observation without pretending it has altered the rest of my opinions."''', c('[Watch what she takes from the cabinet.]', "shell")),
    n("shell", "Vellexia", '''{n}She returns with two palm-sized shells set in silver rims. Each has a hinged cover of cloudy glass. When she opens one, its hollow gives back the quiet sound of her fingernail against the table.{/n}
"An echo pair. Made for a collector who wanted to hear the sea without visiting it. A mistake. The sea is enormously repetitive."
"Who made them?"
"A craftswoman who understood the difference between a shell and a person. Before you ask, these have never been either lovers or servants. They were mineral, silver and a considerable fee."
{n}She opens the other cover. Her next word sounds beside your hand as well as across the table. When she closes your shell, the second voice stops.{/n}
"A sound can ask to be heard. Both covers must be open before conversation begins. The little light is the request. It cannot make your hand move."
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
{n}She returns and waits for you to open yours again. Only then does she speak into her shell.{/n}
"I was about to tell you which word I disliked. You may have saved yourself a considerable explanation."
{n}You shut your cover. Her real laughter crosses the room without assistance.{/n}''', c('[Open it once more and finish the test.]', "choice")),
    n("choice", "Vellexia", '''"It works," she says. "Now we may decide whether that was a sensible discovery."
{n}She puts your shell into a narrow case. There is no ribbon to untie and no inscription claiming you before you have answered.{/n}
"I offer conversation. No command hidden in the sound, no claim on the person who opens it. If I want something more, I can ask while you are listening."
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
"Before you go, I would like to show you something the prediction seller sent. Not today if you are occupied. I can endure being the only person in the room who has read it. For a while."''',
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
"When you want another evening, ask for the evening. I would like to know whether the person inviting me has found anything beyond the danger to enjoy."''', c('[Ask what she intends to send.]', "reply")),
    n("reply", "Vellexia", '''"Nothing yet. Let him wait until he begins predicting whether I will answer."
{n}She folds the silk with the writing inward.{/n}
"I may visit. I may invite him here and find another use for the time. There is no need to make him important merely because he has asked to be."
"And the picture?"
"The artist has spent one piece of information. I have learned what he considers his customers' privacy worth. That is useful enough to keep."
{n}She reaches toward your case, then stops short of touching it.{/n}
"If I decide to pursue this, I may ask for your opinion through the shell. It will be a new request. Do not spend the interval considering yourself employed."
"What if I decline?"
"Then I shall have to find another way to amuse myself. I have managed before."
{n}Her fingers settle on the table beside yours. She turns her hand palm upward, an invitation small enough to ignore without turning it into an argument.{/n}''',
      c('[Take her hand before leaving.]', "touch", requires=("vellexia.courting",)),
      c('"Ask when you decide. I will answer then."', "part")),
    n("touch", "Vellexia", '''{n}Her fingers close around yours. She draws your hand toward her, then gives you time to choose whether to follow it.{/n}
"An encouragingly direct answer to a question I had not quite asked."
"You left room for it."
"So I did."
{n}She leaves your joined hands between you.{/n}
"Would you like a kiss before you go?"''',
      c('"Yes. I would."', "kiss"),
      c('"Only your hand, this time."', "hand")),
    n("hand", "Vellexia", '''"Then only my hand. You may tell me when the answer changes. I am capable of remembering a question."
{n}Her fingers tighten briefly around yours. When you step back she releases them and wishes you an interesting evening elsewhere in the city.{/n}''', c('[Leave the next invitation for another choice.]', flags=("vellexia.prediction_known",))),
    n("kiss", "Vellexia", '''{n}You come nearer. She touches your cheek and kisses you, taking her time over the parting.{/n}
"There. No prediction improved that," she says.
{n}When you step back, she releases your hand. The silk remains folded on the table, and her shell remains closed beside it.{/n}
"Enjoy the rest of the city. I should hate to be blamed for having left you nothing to discover elsewhere."''',
      c('[Leave the next invitation for another choice.]', flags=("vellexia.prediction_known",))),
    n("part", "Vellexia", '''"An admirably unprofitable promise. I cannot even sell it to Ilveris as evidence of what you will do."
{n}She closes her hand and rises. At the door she pauses to turn back toward the folded silk.{/n}
"He has given me something to think about," she admits. "I dislike that more than the invoice. I had intended to choose my own occupation today."
"You still can."
"Yes. I am deciding how much of it to spend disliking him."
{n}Her laughter follows you to the threshold. She does not ask you to remain, and does not make a promise about the next time you will see her.{/n}''',
      c('[Leave the next invitation for another choice.]', flags=("vellexia.prediction_known",))),
], "vellexia.seal_agreed", local=True)

s("the_second_invitation", "The invitation after the dismissal", "[Consider the light beneath the echo shell's cover.]", [
    n("start", "Narrator", '''{n}A dim light moves beneath the closed cover of the echo shell. You have heard nothing from it since Vellexia asked you to leave her reception. Her parting was clear enough: whatever pleasure she had found in your dates, she did not intend another.{/n}
{n}The light waits. There is no voice insisting that you misunderstood her, no message already playing over whatever you meant to do with the evening. When you open the cover, its cloudy glass shows the close, bright image of one dark eye.{/n}
"Ah. Too near."
{n}Vellexia moves her shell farther away. Her face comes into view. She wears an expression of annoyance that becomes amusement as soon as she sees you noticing it.{/n}
"I have discovered a disadvantage in a conversation one must arrange one's own flattering distance for. You may enjoy that before I begin."''',
      c('"You said you did not intend for us to meet again."', "dismissed"),
      c('[Close the cover. Decide whether to hear her another time.]', abort=True)),
    n("dismissed", "Vellexia", '''"I did. I had become tired of the performance we were giving each other. I was not speaking in a secret language that meant you should pursue me more vigorously."
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
"That is the new request. The old dismissal was real."''',
      c('"I will hear the evidence. I will not pretend our dates ended differently to improve your position."', "evidence"),
      c('"Your quarrel interests me. That is not an agreement to resume courting you."', "evidence"),
      c('"I do not want another arrangement with you."', "refuse")),
    n("evidence", "Vellexia", '''"Good. A witness who changes the past to please me would be almost as useless as Ilveris. Less amusing, because I would have no reason to be surprised."
{n}She holds a paper close enough for you to make out a few lines. The writing is a transcription of questions from her reception. Beneath them are several possible answers. Some resemble things you might have said. Others turn you into a pompous caricature.{/n}
"He had it printed," she says. "Before the evening, he claims."
"The list could have been written afterward."
"Certainly. Or copied from someone who had heard me ask the same questions of another guest. I am ancient, darling, not inexhaustible. Even my admirers have occasionally heard a question twice."
{n}She lowers the page.{/n}
"Tessar has asked me to pay for the original account rather than the advertisement. That is the first interesting thing to come out of his house. He either has a clerk who dislikes being underpaid, or he has decided to sell the explanation of his fraud as a second service."
"You have not bought it?"
"Not yet. I am offering you a share in choosing what we ask for. No souls. No part of your crusade. If you are determined to charge a fee, name it before I become fond of the work."''',
      c('"Pay the clerk for her time and let her leave when the work is finished. That is my price."', "clerk"),
      c('"Give me a copy of whatever we learn. I want to know how he used my name."', "copy")),
    n("clerk", "Vellexia", '''"Tessar is employed, not chained. I can pay a woman without congratulating myself on having freed her."
"Then put the limit of the work in your offer. I do not want her discovering she has sold a lifetime when she named a price for an account."
{n}Vellexia regards you for a moment, then nods.{/n}
"A dull clause. Useful, perhaps, if she is deciding whom she dares disappoint. I shall include it. I want an answer from someone who expects to remain capable of giving another."
"And afterward?"
"Afterward she may take her cleverness elsewhere. You are purchasing a particular arrangement, not my admiration for every principle behind it."
{n}She reaches for a fresh sheet and writes while keeping you in view.{/n}
"There. A defined task, a fee, and no continuing service owed to my house. She may decline. You may witness her acceptance through the shell if she chooses to speak to you."
{n}Vellexia reads the offer back without making it prettier than you asked.{/n}''', c('[Accept that limited commission.]', "terms_clerk")),
    n("copy", "Vellexia", '''"A witness with an appetite for the account. How much more interesting than a witness who merely wants to be thanked."
"I want to know what he sold."
"So do I. We may yet quarrel over what to do with the knowledge, but at least we shall begin by wanting the same packet."
{n}She writes a short offer to Tessar, then reads it aloud. It buys a copy of the predictions and the account of when they were prepared. Tessar may withhold names unrelated to the sale, but she must say what has been withheld.{/n}
"I will give you the same papers I keep," Vellexia says. "You may use the part concerning your own name. I will not ask you to swear that your use of it will flatter mine."
"You would dislike it if it did not."
"Immensely. That is not a reason to purchase an agreement I cannot expect you to keep."
{n}She sets the sheet aside.{/n}
"If she accepts, we shall examine it together. You may accuse me of selective reading where I can hear you."''', c('[Accept access to the same account.]', "terms_copy")),
    *[n(id, "Vellexia", '''"One more matter. You will not go into his house on the strength of my amusement. I am quite capable of deciding I dislike a person while they are still useful. You should know where the doors are without relying on my mood."
"We can work through the shell."
"For now. I shall arrange the papers here. If I invite anyone to speak, you will know who is in the room before I open our conversation to them."
{n}She moves her own shell enough to show you the empty part of the table around it, then returns the glass to her face.{/n}
"I have missed a certain quality of your disagreement," she says. "Do not become sentimental about the admission. It does not mean I have decided what else I miss."
"Then we can leave that undecided."
"Yes. At last, something I am being allowed not to predict."
{n}She waits for your answer before closing the cover. The light goes out, leaving you with an ordinary quiet and the inconvenience of being interested.{/n}''',
      c('[Agree to examine the account when it arrives.]', flags=("vellexia.case_opened", flag)))
      for id, flag in (("terms_clerk", "vellexia.clerk_terms"), ("terms_copy", "vellexia.shared_account"))],
    n("refuse", "Vellexia", '''{n}Her expression stills. For a moment you can see her deciding which unpleasant answer would please her most.{/n}
"Very well," she says at last. "I asked. You answered. I shall seek a different audience."
"You do not sound pleased."
"I am not. You were permitted to refuse, not promised that I would enjoy the refusal."
{n}She reaches toward her cover, then pauses.{/n}
"Keep the account of our dates accurate if anyone asks. I have no intention of improving it for your reputation either."
{n}The glass clouds as she closes the shell. No second request follows. Whatever becomes of Ilveris, it will not be a commission you accepted.{/n}''',
      c('[Close the shell and end this private correspondence.]', flags=("vellexia.closed",))),
], "vellexia.prediction_known")

s("the_claim_before_the_event", "What the account can prove", "[Open the echo shell to examine Tessar's account.]", [
    n("start", "Vellexia", '''"She accepted," Vellexia says as the glass clears. "I find a promptly answered offer almost suspicious. Fortunately, the account is irritating enough to restore my faith in the enterprise."
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
{n}The explanation uses the time Tessar had reserved for preparing a second set of papers. Vellexia purchases another appointment rather than asking her to remain indefinitely.{/n}
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
], "vellexia.case_opened")

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
"Now I want three things. Payment for the work I have done. A record that I did not alter the sealed predictions. And permission to show prospective employers what I can prepare without asking Ilveris to recommend me."
"Permission from whom?"
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
{n}Tessar closes her case with both permissions recorded. Her sample will carry recognizable names and the possibility of attracting powerful resentment. She does not ask Vellexia to promise that resentment will never arrive.{/n}
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
    *[n(id, "Vellexia", '''{n}Tessar leaves after reading back the limits of the work. You hear the clasp click as she checks her case, then the door opens and shuts. Vellexia brings the shell nearer.{/n}
"I wanted to frighten her when she corrected me," she says. "You noticed."
"Yes."
"I wanted her to remain accurate too. A tiresome interference between pleasures."
"You chose the account."
"Today. Do not turn a practical decision into a discovery of my hidden goodness. I would like to be able to enjoy it without having to disprove your conclusion."
{n}She looks toward the door Tessar used.{/n}
"She may leave with a better position than either of us intended to give her. That would be a pleasing result. Or she may use my name badly, in which case I shall have a new occupation."
"You agreed to the sample you read."
"I did. I intend to remember exactly how much I agreed to. So should she."
{n}Vellexia turns back to you.{/n}
"I also noticed that you answered the question she asked, rather than explaining what sort of grateful person she ought to become. I find that quality increasingly useful in you."
"Useful?"
"Do not hurry me. I am choosing the compliments myself."''',
      c('[Keep the agreed limits and await the final offer.]', flags=("vellexia.witness_heard", flag)))
      for id, flag in (("named_end", "vellexia.named_sample"), ("limited_end", "vellexia.limited_sample"))],
], "vellexia.account_read")

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
"If you choose the account, I will not pretend it was cowardice merely because I wanted a spectacle. I may complain that the spectacle would have been better. You are already acquainted with the distinction."''',
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
{n}She calls Tessar and gives the instruction. The corrected account will go to the purchasers of the affected predictions, with an invitation to compare their copies. Tessar applies the permissions you gave to both documents: if you withheld your name and private questions, neither version will contain them. The alterations can be demonstrated through the perfume entry without identifying you. The wider account names Ilveris and Vellexia only with her separate agreement.{/n}
"The fee is mine," Vellexia says. "The part concerning the Commander is theirs to keep. No admission that the list of possible answers was a prediction of a single answer. Put that plainly."
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
"You will not," Vellexia says. "And if I choose merely to thwart the Commander, he will not be permitted to call that my having chosen freely while every other answer would have been manipulation. Record the choice. Leave him to argue about his own cleverness."
{n}After Tessar has written, Vellexia moves the shell nearer.{/n}
"I might surprise you unpleasantly," she says.
"You have done so before."
"And you have opened the cover again. An interesting fact. I shall avoid explaining it too quickly."''',
      c('[Accept responsibility for choosing the order.]', flags=("vellexia.wager_chosen", "vellexia.commander_order"))),
], "vellexia.witness_heard")

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
"Tessar has two offers for work. She has asked whether either employer is likely to expect gratitude in place of a wage. I advised her to ask them in writing. It is a question that deserves to be preserved."
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
{n}The first offer is the old play, performed by two paid actors who have agreed to one hour and know when they may leave. The second is a new mechanical theater whose silver figures dismantle an emperor's triumphal procession to build a privy. The third is the empty hour.{/n}
"No souls in the figures," Tessar says before you ask. "I checked the maker's bill and the workings. Lady Vellexia requested that the point not become the entire discussion."
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
{n}Tessar records the choice. The prediction has failed, but the hour must still be spent as agreed.{/n}''', c('[Watch the hour she chose, without asking her to change the decision.]', "won")),
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
"The shell already carries an echo. Perhaps it could keep the experience of this hour for you, then let you live through that memory once more in the space of a breath. You would know what was coming. Nobody else would repeat a word or lose a moment. You would choose what to notice the second time."
"Would that make him wrong?"
"Not by the terms you agreed. It would be a fourth offer. You would forfeit the stake if you took it."
{n}She becomes very still. Then she smiles.{/n}
"An expensive trick that admits its price. Tessar, record the forfeit. I would like to be the person who knows why I paid it."
"You may still choose one of the three offers," the clerk says.
"I know. That is what makes spending the silver interesting."
{n}Vellexia speaks her agreement into the shell. You ask the echo to keep the hour between its first note and its last. A second light appears beneath the glass, following the first a heartbeat behind. Vellexia studies the doubled gleam, then deliberately holds her hand before it.{/n}
"Once," she says. "Not until you tire of watching me."
{n}You promise one turn and leave her to choose what she does with it.{/n}''', c('[Keep the echo to the single recollection she accepted.]', "fate")),
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
{n}She asks the maker for a price for another performance, then rejects the first figure offered with such enthusiasm that the negotiation becomes an entertainment of its own. She does not buy the mechanism or claim its maker's future work.{/n}
{n}When the room empties, she moves the shell close again.{/n}
"You stayed. Even through the parts in which I had almost nothing to say to you. I find that more pleasant than I expected."''',
      c('[Keep the finished result and the unexpected pleasure.]', flags=("vellexia.verdict_kept", "vellexia.wager_won"))),
    n("lost", "Vellexia", '''{n}She dismisses the performers and gives the witnesses leave to go. The empty compartment in the ring tray remains within the glass's view until she notices it and moves the tray aside.{/n}
"I wanted that piece," she says. "I can make another. I wanted that one."
"You chose the hour knowing the cost."
"Yes. I have been attempting to resent you for presenting it first. You may be pleased to hear the attempt is going badly."
{n}She sits back and looks at your image without smiling.{/n}
"Stay if you want to. Do not congratulate me for losing gracefully. I have not decided to be graceful, and you would spoil the occupation."
{n}You stay. She tells you how she recovered the circlet from its third purchaser, and the story is vain, vindictive and funny enough that you understand why she wanted the object back. When you laugh, she reaches toward the shell before remembering the distance.{/n}
"There," she says, drawing her hand back. "Something worth the price of a poor temper."''',
      c('[Spend the rest of the empty hour with her.]', flags=("vellexia.verdict_kept", "vellexia.wager_lost"))),
    n("fate_end", "Vellexia", '''"Do not tell me you have cured my boredom," she says when you are alone. "I shall become bored with the sentence before you finish it."
"You wanted to try one unexpected ending."
"I did. I obtained it. I also lost something I liked, which will prevent me becoming unbearably grateful."
{n}She touches the closed ring tray and pushes it out of view.{/n}
"The memory is mine. The room did not become another room. Nobody spent the hour again because I wanted to hear a joke twice. That was the part I needed to know before agreeing."
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
], "vellexia.wager_chosen")

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
"I disliked your company at the end of our dates. I wanted you to go. I would not improve either of those facts merely because I now find myself wanting a different answer."
"You could ask for one."
"I am approaching the indignity with suitable care."
{n}Her smile returns, but she does not let it finish the conversation for her.{/n}
"You let me be wrong without pretending I had become a helpless creature who needed your good influence. You disagreed, sometimes at exactly the moment I wanted obedience. You also found things to enjoy that I had not selected to impress you."
"That sounds like another assessment."
"It is. I have been attempting to understand why I want your voice when the matter giving me an excuse to hear it is finished. I do not intend to sell the answer to anyone else."
{n}She looks directly into the glass.{/n}
"I want to be your lover. A new invitation, not a correction written over the old dismissal. I would like to know whether you want it."''',
      c('"I do. I want to find out what we choose after the first excitement has passed."', "terms"),
      c('"I want to keep exploring this, but I am not ready to call us lovers."', "slow"),
      c('"I want your company. I do not want a romance with you."', "company")),
    n("terms", "Vellexia", '''"Then there are some things I will say before you become fond of imagining me in your rooms."
"Go on."
"I am not offering to become harmless. I will not account for every person I dislike as though you had been appointed to correct my temper. Nor will I send my quarrels into your house and call your having a lover permission to make them yours."
{n}She watches you absorb the distinction.{/n}
"If I ask for help, you may refuse. If you ask me to refrain from something, I will answer. I may answer badly. You may decide the answer means you do not want me."
"That is more honest than a promise you would resent."
"It is less flattering. I am attempting to tolerate the discovery."
{n}She draws the shell a little nearer.{/n}
"I will have other pleasures, and I expect you to have a life that continues when this cover is closed. Do not offer me somebody else's consent. Do not promise another person's time to make yours appear more available. I have had enough admiration built from things the admirer did not own."
"And we choose our own time together."
"Yes. As much of it as we actually want. I may become greedy. You should say so where I can hear you."''',
      c('"I accept those terms. I want the affection we can choose honestly."', "near"),
      c('"I cannot promise that without more thought. Let us slow down."', "slow")),
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
    n("desire", "Vellexia", '''{n}You tell her. She listens without the interruption you expected, then asks you to repeat one part more slowly. Her answer is a quiet laugh and a promise concerning the next kiss, if you both choose the meeting that would make it possible.{/n}
{n}The conversation grows intimate without pretending the distance has disappeared. You learn which pauses she enjoys and which make her ask whether you have begun composing something too polished to say. She learns that you can make her lose her place in a sentence without being in the room.{/n}
"I was saying something excellent," she complains.
"You can begin again."
"I would rather hear what you were about to say. A shameful failure of discipline."
{n}Later, when the eagerness has quieted, neither of you closes the cover immediately. She asks you a small question about where you are sitting, and you answer without trying to make the place worthy of her.{/n}
"I would like to know that room," she says. "Not tonight. Tonight this has been enough to make tomorrow inconvenient."''',
      c('[End the call as lovers, with another conversation freely chosen.]', flags=("vellexia.departure_kept", "vellexia.renewed_lovers", "vellexia.committed"))),
    n("gentle", "Vellexia", '''"Then give me something unpolished to listen to. I refuse to spend a quiet evening hearing a visitor become solemn because nobody is touching them."
{n}You tell her about a small irritation from your day. She offers a solution so excessive that you begin laughing before she finishes. She looks pleased, then asks what you actually did.{/n}
"That worked?"
"Well enough."
"How disappointing. I had almost enjoyed my version."
{n}You keep talking. At one point she rests her cheek against her hand, listening, and the familiar expression becomes unexpectedly intimate when you realize she is making no attempt to improve it for you.{/n}
"There," she says after a comfortable silence. "I have managed to want the next kiss without requiring this conversation to hurry toward it. I hope you will not reward the achievement with a lecture about patience."
"I was going to ask whether you wanted another evening."
"An excellent substitution. Yes."''',
      c('[End the call as lovers who have chosen this pace.]', flags=("vellexia.departure_kept", "vellexia.renewed_lovers", "vellexia.committed"))),
    n("slow", "Vellexia", '''{n}She leans back. The disappointment in her face is plain enough that she does not bother denying it.{/n}
"You make an unfinished answer sound very deliberate. I shall have to believe you mean it."
"I do."
"Then I will decide how much patience I want to spend, rather than telling myself yours is a promise in disguise."
{n}She turns the shell slightly, adjusting a reflection that has crossed the glass.{/n}
"We can still speak. I would prefer that you bring me something besides an apology for not wanting exactly what I wanted tonight. I have received the answer. Let us find another use for the time."
{n}You ask about the earring. She tells you why its maker hates the woman who owns the matching piece, and the conversation wanders into a feud ridiculous enough to please her without needing to become yours.{/n}
"Ask again if your answer changes," she says before the cover closes. "I may have a different one too. We shall discover whether the timing is merciful."''',
      c('[Keep the relationship question open without promising an answer.]', flags=("vellexia.departure_kept", "vellexia.renewed_slow"))),
    n("company", "Vellexia", '''"An unequivocal answer. I had hoped for a more flattering one."
{n}She turns her head away, then back.{/n}
"I can enjoy a person who does not want to kiss me. I have managed it before, though I prefer being wanted."
"I would like our conversations to continue."
"So would I. For the moment, let me be disappointed without inviting me to demonstrate how reasonably I bear it."
{n}You give her the silence she asks for. After a while she tells you something Tessar said when the final payment arrived: that it was the first time a patron had paid the agreed amount without attempting to make a better price part of the celebration.{/n}
"I considered correcting the omission," Vellexia says. "Then I decided I preferred having one person leave my house surprised."
{n}The conversation finds its way back to ease gradually. When it ends, she asks you to open the cover another time. The invitation carries no further question hidden inside it.{/n}''',
      c('[Accept another conversation as company, not courtship.]', flags=("vellexia.departure_kept", "vellexia.renewed_company"))),
], "vellexia.verdict_kept")

s("the_voice_after_the_abyss", "A different room for the same voice", "[Answer the echo shell in Drezen.]", [
    n("start", "Narrator", '''{n}The shell has survived the journey back to Golarion. For a time its closed glass showed no light at all. Now a pale thread moves beneath the cover while the sounds of Drezen pass outside your room.{/n}
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
{n}You tell her something true about the return. She does not demand the whole account. When you stop, she asks whether you have had a quiet hour since arriving.{/n}
"This one may have to do," you say.
"Then put the shell somewhere your arm will not ache. I refuse to be remembered as an inconvenient weight when I have gone to considerable trouble to be a voice."''', c('[Settle in and ask what became of her own business.]', "result")),
    n("slow", "Vellexia", '''"Good. I would have resented being the only one who remembered leaving it there."
{n}She watches your face for a moment before sitting back.{/n}
"I am not asking you to answer it in your first breath from another world. Tell me something about where you are. I have spent enough time imagining it to distrust the picture."
{n}You describe the room without improving it. She asks which sounds come through the door, then whether the chair is comfortable.{/n}
"That is the room in which you are choosing to hear me?"
"At present."
"I shall attempt not to compete with the chair. It has had a considerable advantage in becoming familiar."
{n}Her smile returns without demanding a declaration from you.{/n}
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
"Perhaps. I am enjoying being allowed not to decide yet."''', c('[Ask what Tessar chose next.]', "tessar")),
    n("lost", "Vellexia", '''"Ilveris sold it. That offended me more than winning it. He had no intention of wearing the thing; he wanted to turn the account of my loss into a price."
"Will you buy it back?"
"Not at the price he has taught its new owner to request. I made the piece. I know exactly which of its virtues he has misunderstood in the advertisement."
{n}She shows you the empty space in the case, then closes it.{/n}
"I have begun another design. It is not a replacement, and I am not asking you to soothe me by pretending the loss improved my work. I liked the old piece. I also liked the hour I bought by letting it go."
"Both can remain true."
"An inconvenient arrangement. I have made room for it."
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
"Certainly. She preferred obtaining work quickly. She also discovered that people who accepted her limits were less likely to ask her to sell them an introduction she did not possess."
{n}Vellexia rests her hand on the case.{/n}
"I would have chosen differently. She knows. We have reached the civilized arrangement of not requiring each other's admiration before collecting our fees."''', c('[Let the completed work remain completed.]', "end")),
    n("end", "Vellexia", '''"There. An account with a last page. We should be careful not to make another occupation from rereading it until we cease liking one another."
"What occupation would you prefer?"
"I would like to see whether we can share an evening that neither of us has to improve into a useful event. Choose something you would want to do in that room if you were not trying to make it impressive enough for me."
"And you?"
"I shall choose something here. We will discover whether the two pleasures tolerate being interrupted by conversation."
{n}She looks past the shell toward her own room, apparently considering several possibilities.{/n}
"No audience. No wager. If it disappoints, we may say so and find another way to spend the time. I have lately acquired an appreciation of giving an evening a recognizable end."''',
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
      c('"I want a meeting too. We would have to choose where it could actually happen."', "meeting", requires=("vellexia.renewed_lovers",)),
      c('"For tonight, tell me what you would say if you were here."', "voice"),
      c('"I want to keep the closeness we can have now, without making a larger promise."', "voice", requires=("vellexia.renewed_slow",))),
    n("meeting", "Vellexia", '''"Yes. You have a city full of people who would reasonably dislike my arrival. I have a city full of people who would enjoy mistaking yours for an announcement. I can imagine several entertaining mistakes and very few convenient introductions."
"The shell does not carry people."
"I noticed. I have had considerable reason to resent the limitation."
{n}She leans nearer the glass.{/n}
"I would not arrive in your room without being asked. You may enjoy hearing that without mistaking it for a promise to become agreeable to everyone outside the door. If we arrange a meeting, we will choose it in words other people cannot make for us."
"That is what I want."
"Then we share a difficult wish. I find it more interesting than a convenient lie."
{n}She touches her finger to her mouth, then rests it beside the shell.{/n}
"For tonight, stay where I can hear you. I have been thinking about the last time you were close enough to interrupt me without speaking."''', c('[Stay for the private conversation.]', "lovers")),
    n("voice", "Vellexia", '''"I would probably complain about the chair first. Then I would want to know why you kept one of those pages and discarded another. At some point you would ask whether I had come merely to criticize your room."
"Had you?"
"No. I would have come because I wanted your company. I would hope you had noticed before making me admit it so inelegantly."
{n}She closes the bottle she chose and puts the others away one by one. The little clinks accompany your conversation until the table is almost clear.{/n}
"I am here for the same reason now," she says. "You may imagine the complaint about the chair if it makes the admission easier to believe."''',
      c('[Enjoy the quiet affection between lovers.]', "lovers", requires=("vellexia.renewed_lovers",)),
      c('[Stay with the company you have chosen without changing its terms.]', "company_end", forbids=("vellexia.renewed_lovers",))),
    n("lovers", "Vellexia", '''{n}You talk until the pages beside you have been sorted or abandoned. Vellexia asks you to leave the shell open while she unfastens the earring that has begun to catch in her hair. She complains about its maker with an inventiveness that makes it difficult to answer soberly.{/n}
"Do not laugh too much," she says. "I may remember you fondly whenever it annoys me. An association you might regret."
"I can think of worse."
"So can I. I prefer this one."
{n}After a while her voice grows quiet. She asks what kind of kiss you would want if the distance were less considerable. You tell her, and the silence after your answer has nothing vacant in it.{/n}
"I would like that," she says. "Keep the rest for another conversation. I want something to anticipate that you have not described perfectly in advance."
{n}You arrange another call, and she closes the cover only after hearing your answer.{/n}''',
      c('[Keep the evening and the next chosen call.]', flags=("vellexia.private_kept",))),
    n("company_end", "Vellexia", '''{n}The conversation lasts longer than the sorting. Vellexia asks which discarded page was easiest to release, and you tell her. Her answer is an account of something extravagant she kept solely because an enemy had offered to buy it.{/n}
"Did you want it?"
"Less than he did. That was sufficient at the time."
{n}She sounds amused by the comparison rather than chastened. Before the evening ends, she asks whether you have room for another conversation soon.{/n}
"I have enjoyed this one," she says. "There is no invoice to explain the remark. You may have to believe I mean it."
{n}You agree on another call. The glass clouds only after both of you have said what you meant to say.{/n}''',
      c('[Keep the evening and the next chosen call.]', flags=("vellexia.private_kept",))),
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
"Enough to choose how we spend it."
"A useful answer. I dislike being given a farewell so complete that nothing I say can change its shape."
{n}She moves the empty vase out of the glass's view.{/n}
"Tell me what you came to ask. Then I shall tell you whether it is the thing I wanted to hear."''',
      c('"I want to keep what we chose. I cannot promise when I will answer again."', "absence"),
      c('"I want to settle what we mean to each other before I go."', "meaning"),
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
"I want you to return. I shall continue doing things I want while you are away. Those are two true statements, however poorly they flatter a dramatic farewell."''', c('[Tell her what you want the next answer to mean.]', "meaning")),
    n("meaning", "Vellexia", '''"I have not mistaken the shell for your whole life," she says. "You should not mistake it for mine. But it has become a part I would notice losing."
{n}She looks at its silver edge with a brief, dissatisfied smile.{/n}
"I chose this because it let me decline a tiresome visitor. Now I notice when it remains dark. I find that sufficiently irritating without being required to call it an improvement in my character."
"You are allowed to want someone."
"I have never needed permission for wanting. It is the part where the person has an answer of their own that makes such trouble."
{n}She meets your eyes again.{/n}
"What do you want that answer to be, if we have another evening?"''',
      c('"I want to remain your lover, with the freedom and care we agreed."', "lovers", requires=("vellexia.renewed_lovers",)),
      c('"I am ready to choose you as a lover, if you still want that."', "new_terms", requires=("vellexia.renewed_slow",)),
      c('"I want this friendship. I do not want to turn it into a romance."', "friends", forbids=("vellexia.renewed_lovers",)),
      c('"I still need a slower answer. I want to keep knowing you without promising romance."', "slow", requires=("vellexia.renewed_slow",)),
      c('"I want to stop being lovers. If you need distance after that, I understand."', "ending", requires=("vellexia.renewed_lovers",))),
    n("new_terms", "Vellexia", '''{n}Her smile comes before the answer.{/n}
"Yes. I dislike the timing, but I want you. You have managed to make both statements rather urgent."
"Then we should say what we are offering."
"Affection. Desire. Time we actually choose. I will have other pleasures, and I expect you to have other people whose claims on your time matter. Neither of us can give away their answers."
{n}She pauses, watching your face.{/n}
"I am not becoming harmless. You may refuse to help me, and I may refuse something you ask. If an answer changes what you want, say so. I will do the same. I do not want a lover who praises me in the evening and hopes to discover a different woman in the morning."
"I know who I am asking."
"Then ask me again when there is less glass between us. For now, I would like to hear that you mean it."''',
      c('"I mean it. I choose those terms, and I want you."', "new_lovers"),
      c('"I cannot accept that yet. Let us keep the slower answer."', "slow")),
    n("lovers", "Vellexia", '''"Good. I wanted to hear it before discovering how extravagantly I might resent a different answer."
{n}She moves closer. The small image cannot conceal the care with which she studies your face.{/n}
"You look tired. I had several excellent suggestions for how to occupy the time, and now I find myself wanting to hear you speak without spending another ounce of effort making the words impressive."
"I want to come back. I want to hear you complain about the singer."
"There. Appalling flattery. Almost nothing in it for anyone but me."
{n}Her laughter is brief and warm.{/n}
"I want another kiss," she says. "The fact that I cannot have it now has not made the wish more dignified. Tell me how you would leave if you were standing here."''',
      c('[Describe a lingering kiss and let her answer in her own words.]', "warm"),
      c('"I would hold your hand a while. Then I would go when I had to."', "quiet")),
    n("new_lovers", "Vellexia", '''"Then I accept. Come nearer. I have waited through enough careful answers to enjoy this one without pretending I was indifferent to it."
{n}You lift the shell. She tells you how she would greet you if you could step into the room, stopping after the first kiss to ask what you would want next. Your answer makes her close her eyes for a moment.{/n}
"An inconvenient thing to hear just before you leave. I intend to remember it."
{n}You talk until the impending departure becomes something you can mention without allowing it every sentence. She asks for one ordinary detail of your morning and laughs at the answer.{/n}
"Keep yourself alive if you can," she says at last. "I want more of this particular person. I have no use for a monument that cannot answer back."
{n}You say goodbye as lovers. The cover closes after she has said it too.{/n}''',
      c('[Keep the freely chosen relationship and the farewell.]', flags=("vellexia.farewell_kept", "vellexia.farewell_lovers", "vellexia.committed"))),
    n("warm", "Vellexia", '''{n}You tell her. She answers with a soft correction to the way you imagined her hands, then asks you to begin again. This time she lets the description finish.{/n}
"Yes," she says. "That is a departure I would resent properly."
"Properly?"
"With enough pleasure to make the next arrival worth anticipating."
{n}For a while you speak quietly about what you want from that arrival. Neither room changes. Her voice is enough to make the distance feel personal, something between two bodies rather than a line on a map.{/n}
"Go when you must," she says. "I dislike rehearsing it."
{n}You tell her you have to leave. She asks for another breath, and you give it before saying goodbye. Her answer is unadorned. She keeps looking at you until you close the cover.{/n}''',
      c('[Keep the affection and the farewell you gave each other.]', flags=("vellexia.farewell_kept", "vellexia.farewell_lovers"))),
    n("quiet", "Vellexia", '''"Then I would keep your hand until you told me. I am capable of wanting a thing without making every moment an attempt to obtain more. Do not look so relieved. It is a selective talent."
{n}She rests her hand beside the shell. You put yours where she can see it. There is silver under your fingers, no borrowed sensation passing between them.{/n}
"There," she says. "A poor substitute. I am glad you suggested it."
{n}You sit together until it is time to go. Once she asks whether you have remembered something you need to take. Her next remark is extravagant enough to make you laugh, as though she has grown suspicious of her own practical concern.{/n}
"I want the next answer," she says when you stand. "I shall not pretend I have it already."
{n}You tell her goodbye. She answers before the glass clouds.{/n}''',
      c('[Keep the quiet affection and the farewell.]', flags=("vellexia.farewell_kept", "vellexia.farewell_lovers"))),
    n("friends", "Vellexia", '''"Then friendship. I am not going to spend every conversation treating the word as a puzzle you must eventually solve in my favor."
{n}She settles back and angles the shell toward her, bringing the empty vase into the edge of the image again.{/n}
"I have enjoyed your company. I expect to find you irritating again, if you return with enough energy to have opinions. I would rather risk that than have you agree with me as a farewell gift."
"I was not planning to."
"Good. There is an improvement to the singer's middle passage I would like to propose, and you may be just unreasonable enough to tell me why she would refuse it."
{n}You discuss the proposal. It is lavish, insulting and almost certainly calculated to make Vellexia the subject of the performance. She defends it with increasing pleasure as you object.{/n}
{n}When you leave, the last sound before the cover closes is her laughter at something you said. You find yourself smiling after the room has gone quiet.{/n}''',
      c('[Keep the friendship you both named.]', flags=("vellexia.farewell_kept", "vellexia.farewell_friends"))),
    n("slow", "Vellexia", '''"You have made patience an unexpectedly demanding entertainment."
"I am not asking you to wait for a different answer."
"I know. I can decide whether I want the conversation you are offering. I do."
{n}She turns the shell slightly, removing the lamp's reflection from its glass.{/n}
"There are things I would like to ask you that have nothing to do with persuading you into my bed. Some of them are even about you. You may find the novelty irresistible."
"You could try one now."
{n}She does. The question concerns a place you miss, and she listens long enough to ask a better second question. Her own answer is less tender: she misses the view from a balcony because she once enjoyed watching a rival discover that his procession had taken the wrong street.{/n}
{n}The departure arrives during an argument about whether she arranged that mistake. She refuses to improve the story by answering too soon.{/n}
"Ask another time," she says. "I may still refuse."
{n}You say goodbye without turning the uncertainty into a pledge. She sends you away with a smile.{/n}''',
      c('[Keep the slower, unpromised relationship.]', flags=("vellexia.farewell_kept", "vellexia.farewell_slow"))),
    n("ending", "Vellexia", '''{n}Her hand leaves the rim.{/n}
"I would prefer a different answer. I am not going to persuade you to give it merely because I would enjoy hearing it."
"I meant what I offered before."
"Then leave it true. We need not make every pleasant evening a mistake in order to stop having them."
{n}She studies you for a moment longer.{/n}
"I do not want another call while I discover how much I resent this one. Keep your shell closed. If that changes, it will not change because you have found a more elegant explanation to send me."
"I will respect that."
"I expect you to."
{n}She draws the cover toward her. Before it closes, she looks back once.{/n}
"I enjoyed the part you cannot give back. Remember that if you are tempted to become noble about having spared me something."
{n}The glass clouds. No light follows it.{/n}''',
      c('[Respect her answer and end the correspondence.]', flags=("vellexia.farewell_kept", "vellexia.closed"))),
], "vellexia.private_kept", chapter=5)


def ending(id, title, text, requires=(), forbids=(), owner="Epilogue"):
    SCENES.append(scene("vellexia.ending_" + id, title, owner, 0, "", [
        n("start", "Narrator", text, portrait="Vellexia")], Relationship="vellexia", last=99,
        requires=("vellexia.prediction_known", *requires), forbids=forbids))


BAD_END = ("vellexia.dead", "vellexia.mirrored", "vellexia.native_coercion", "vellexia.early_fight", "vellexia.final_fight")
ORDINARY_BLOCK = (*BAD_END, "vellexia.closed", "inhuman", "ascended", "sacrifice")
ending("lovers", "A light beneath the cover", '''{n}Vellexia remained a difficult correspondent. She sent invitations at inconvenient hours, complained when her own answer had been kept waiting, and sometimes declined a call because she preferred the company already in her room. The Commander could do the same. There were silences they chose and others that annoyed them enough to be discussed at the next meeting of their voices.{/n}
{n}The echo shell carried affection as well as complaints. Vellexia discovered that the Commander remembered details she had included carelessly: an earring that caught in her hair, a singer's disputed passage, the name of someone she had hoped would feel suitably insulted. She pretended to regret having supplied such material and continued supplying it.{/n}
{n}They remained lovers across an inconvenient distance. No body stepped through the little glass. The prospect of a physical visit still required a place, an invitation and an arrangement both would actually choose. In the meantime, there were evenings worth answering for. Vellexia did not become gentle toward the world to enjoy them.{/n}''', requires=("vellexia.farewell_lovers",), forbids=ORDINARY_BLOCK)
ending("friends", "An argument worth continuing", '''{n}The Commander and Vellexia continued their friendship through the echo shell. Some invitations concerned performances, some an insult too elaborate to enjoy without an audience, and some no subject she cared to admit had been an excuse to call.{/n}
{n}She did not become a kinder patron through having acquired a friend. The Commander could disagree, refuse a request or close the cover. Sometimes Vellexia resented the answer. Sometimes she returned with a better question and an insistence that nobody call it an apology.{/n}
{n}There was pleasure in being remembered accurately. When she misquoted the old play to improve an insult, the Commander corrected her. Her delighted indignation kept the conversation alive long after either had intended to retire.{/n}''', requires=("vellexia.farewell_friends",), forbids=ORDINARY_BLOCK)
ending("slow", "An answer still open", '''{n}Vellexia kept calling when she wanted the Commander's company. The slower answer remained what they had actually chosen. She was not entitled to turn it into a promise of romance, and the Commander did not ask her to wait faithfully for a desire that might never arrive.{/n}
{n}There were other evenings in both their lives. The ones they spent speaking through the shell acquired jokes too old to explain to another listener and disagreements they returned to with suspicious enthusiasm. When Vellexia finally explained the procession and the wrong street, the Commander accused her of having delayed the best detail deliberately. She denied only that it had been the best.{/n}''', requires=("vellexia.farewell_slow",), forbids=ORDINARY_BLOCK)
ending("interrupted", "The last conversation", '''{n}The correspondence did not reach another settled farewell. Vellexia had offered a way to ask for her attention, and the Commander had learned how to use it. Neither could supply a later answer simply by remembering the earlier invitation.{/n}
{n}The silver cover kept its small, familiar weight. What they had said before the silence remained part of their history, including any affection and promises they had actually chosen. No later meeting arrived to decide what should follow them.{/n}''', forbids=(*ORDINARY_BLOCK, "vellexia.farewell_kept"))
ending("closed", "A cover left closed", '''{n}Their correspondence ended. Vellexia did not send a gentler version of her last answer, and the Commander did not keep requesting one. The shell remained a thing that could be closed.{/n}
{n}She had enjoyed the company while she wanted it. The ending did not persuade her to despise every earlier pleasure. When a line from the old play reminded her of the Commander, she could laugh at the recollection and still decline to reopen the conversation.{/n}''', requires=("vellexia.closed",), forbids=(*BAD_END, "inhuman"))
ending("dead", "The unanswered request", '''{n}Vellexia died. The shell could carry no answer from her. It had never contained the woman whose voice had used it.{/n}
{n}The Commander remembered a presence larger and more troublesome than the little object: her appetite for novelty, the sudden pleasure of a remark that reached her, the cruelty she did not hide. Death did not make her harmless in retrospect. Nor did it erase the occasions on which she had freely wanted that particular company.{/n}''', requires=("vellexia.dead",), forbids=("vellexia.mirrored",))
ending("mirror", "No voice borrowed from glass", '''{n}Vellexia had been transformed into a mirror. The echo shell did not release her from that fate, and the earlier invitation did not turn her transformation into something she had chosen.{/n}
{n}There was no answering voice to make the silence comfortable. The Commander could remember the woman who had offered the shell. What it would take to restore her, and what she would say afterward, remained unanswered.{/n}''', requires=("vellexia.mirrored",))
ending("coercion", "The invitation cannot answer", '''{n}The Commander's demonic domination of Vellexia changed the meaning of any later claim to her willingness. The earlier freely offered shell could not speak for the woman placed under that power.{/n}
{n}The correspondence did not continue on the strength of frightened surrender. No account of their earlier pleasure supplied the answer that would have to be given without that threat. Whatever happened next remained outside the invitation they had once made.{/n}''', requires=("vellexia.native_coercion",), forbids=("vellexia.dead", "vellexia.mirrored"))
ending("hostility", "The invitation overtaken", '''{n}Violence overtook the invitation Vellexia had made. The shell did not preserve a safe, unchanged hostess somewhere beyond the quarrel. An earlier pleasant hour was no guarantee that either could resume the conversation that followed it.{/n}
{n}There was no new agreement between them. The recollection of her laughter remained exact and insufficient.{/n}''', requires=(), forbids=("vellexia.dead", "vellexia.mirrored", "vellexia.native_coercion"))
SCENES[-1]["RequiresAny"] = ["vellexia.early_fight", "vellexia.final_fight"]
ending("changed", "Another kind of silence", '''{n}The Commander changed beyond the life in which the echo pair had first been offered. The old arrangement did not furnish a new one for that altered existence. No familiar signal appeared merely because the shell still had its cover.{/n}
{n}Vellexia had chosen particular conversations with a particular person. The memory could remain without claiming she had accepted every possible being that might follow them.{/n}''', requires=("inhuman",), forbids=BAD_END)
ending("ascent", "A god is not an answer", '''{n}When the Commander ascended, Vellexia wanted to hear the account twice. Then she asked a question the messenger could not answer and dismissed him before he attempted to invent something flattering.{/n}
{n}She had known a voice that could request her attention through a small silver shell. A god might have other ways to call. That possibility did not make the next invitation hers to assume, or make an old agreement sufficient for an altered existence.{/n}
{n}She kept the shell. Sometimes she resented its silence. Sometimes she was entertained by the thought of how much she would enjoy criticizing a divine entrance. No answer from the new power was recorded in the glass.{/n}''', requires=("ascended",), forbids=(*BAD_END, "inhuman", "vellexia.closed"))
ending("sacrifice", "What she wanted back", '''{n}The Commander's sacrifice left Vellexia with news she could neither bargain against nor improve by refusing to hear. She dismissed a visitor who began praising the magnificence of the loss. Later she sent for him to finish the factual part of his account.{/n}
{n}She wanted the person back. She was vain enough to resent having acquired a want that admiration could not satisfy, and honest enough in private to know what she missed. Any words they had actually spoken remained theirs. She added no unmade promise to them.{/n}
{n}The shell stayed closed for a long time. When she finally opened it, she heard only the small sound of her nail against its rim. She closed it again before anyone entered the room.{/n}''', requires=("sacrifice",), forbids=(*BAD_END, "inhuman", "ascended", "vellexia.closed"))
ending("aeon", "An invitation not made", '''{n}In the history remade without the Worldwound, the Commander did not travel the same road to Vellexia's rooms. The offered shell, the dispute over predictions and the private answers that might have followed had no unchanged place in that world.{/n}
{n}Vellexia's appetites belonged to her own life. No memory of an erased visitor arrived to turn them into a promise she had never made.{/n}''', owner="AeonEpilogue")


def integrate(payload):
    payload.setdefault("SeenCues", {}).update(SEEN_CUES)
    payload.setdefault("SelectedAnswers", {}).update(SELECTED_ANSWERS)

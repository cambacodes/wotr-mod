"""Kiana's work and relationship encounter an audience outside her circle."""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, nodes, after, delay=48, **extra):
    for page in nodes:
        page["Portrait"] = "Kiana"
    SCENES.append(scene("kiana." + id, title, "Kiana", 5, "", nodes,
        Relationship="kiana", Remote=True, Chapters=[5], Areas=[DREZEN],
        requires=("seelah.souls_returned", "kiana.lovers", "kiana.followthrough_kept", *after),
        forbids=("kiana.closed", "inhuman", "kiana.farewell", "kiana.future_settled"),
        ForbidOverrides={"kiana.farewell": "kiana.catchup_requested", "kiana.future_settled": "kiana.further_requested"},
        delay=delay, optional=True, **extra))


# An older completed capstone stays completed. This letter alone opts into later work.
SCENES.append(scene("kiana.later_incident", "A less private audience", "Kiana", 5, "", [
    n("start", "Narrator", '''{n}A note from Kiana asks whether you have time for something awkward. Someone outside her circle has taken an interest in the princess. Unfortunately, that person also appears to have taken an interest in advertising the Commander.{/n}
"We have already had our conversation about what we want. I have no intention of making you sit it again. This is a new inconvenience. I would appreciate your company while I find out how large it is."
{n}There is room to send an answer. The evenings you have already kept remain yours.{/n}''',
      c('[Answer that you will come and hear what happened.]', flags=("kiana.further_requested", "kiana.catchup_requested")),
      c('[Keep the note until you can give her the time.]', abort=True), portrait="Kiana"),
], Relationship="kiana", Remote=True, ManualOnly=True, Chapters=[5], Areas=[DREZEN],
    requires=("seelah.souls_returned", "kiana.lovers", "kiana.followthrough_kept", "kiana.future_settled"),
    forbids=("kiana.closed", "inhuman", "kiana.further_kept"), optional=True))


s("borrowed_name", "The name above the title", [
    n("start", "Kiana", '''{n}Kiana meets you with a board tucked beneath one arm. The writing on it is too large to be a private invitation.{/n}
"I have made an unfortunate discovery. It is possible to become famous in one courtyard without anyone asking whether you wanted to be."
{n}She turns the board toward you. Beneath a painted moon, a crooked line announces an entertainment requested by the Knight Commander. The vampire princess will receive her guest after the wagoners have finished their work.{/n}
"I lent a page to Rovan. He carries messages for people at the wagon yard. He wanted to read something ridiculous to his friends. I said he could read that page."
{n}Her finger stops beneath your title.{/n}
"That was not on it."''',
      c('"Show me who wrote the notice."', "yard"),
      c('[Ask to return when you can give the matter your attention.]', abort=True)),
    n("yard", "Narrator", '''{n}The yard is busy with civilian carters replacing a broken wheel. A lean man in a patched coat looks up when Kiana calls his name. His smile survives seeing her board, but not seeing you behind it.{/n}
"I was going to ask you," Rovan says.
"About the performance or the request I apparently made on the Commander's behalf?"
"I only meant people would like to know. You read together. I thought..."
"You thought the name would make them come."
{n}He looks at the board again.{/n}
"Yes."
{n}Two of the carters stop working. Rovan begins to hold himself as though he has been called before an officer.{/n}''',
      c('[Diplomacy] "Nobody is in trouble for wanting an evening off. Tell us what you actually promised."', check=dict(Skill="CheckDiplomacy", DC=24, Success="plain", Failure="stiff", CommanderOnly=True), forbids=("kiana.further_plain", "kiana.further_stiff", "kiana.further_private")),
      c('"Kiana lent you the page. Ask her to walk through the notice with you. I will wait here."', "private", flags=("kiana.further_private",), forbids=("kiana.further_plain", "kiana.further_stiff")),
      c('[Return to the explanation Rovan gave openly.]', "plain", requires=("kiana.further_plain",)),
      c('[Return to the explanation Kiana had to draw out of him.]', "stiff", requires=("kiana.further_stiff",))),
    n("plain", "Rovan", '''"I said she would come. I should have asked first. I said the Commander liked it, and someone asked whether it was an order to attend. I made a joke instead of answering."
{n}One of the carters gives him a look of such concentrated disgust that he stops attempting to smile.{/n}
"I said we could all benefit from refinement. It sounded funnier yesterday."
"Most commands do," Kiana says.
{n}Rovan takes a rag from his pocket and rubs at your title. The paint has dried. He only spreads a dark smear over the word requested.{/n}
"I'll change it."
"You will tell them too. They cannot attend a correction you leave in your pocket."''', c('[Ask to see the page he intended to read.]', "page", flags=("kiana.further_plain",))),
    n("stiff", "Narrator", '''{n}Rovan nods too quickly. Every answer begins with your title. When you ask what he promised, he says he intended no disrespect. When you ask whether people believe they must attend, he says he has always supported the crusade.{/n}
{n}Kiana puts the board on the ground between you.{/n}
"Rovan. Look at me. You borrowed something I wrote. I want to know what you told people about it."
{n}He answers her. He promised she would come. When someone asked whether the Commander's request meant attendance was compulsory, he made a joke about refinement and let the question stand.{/n}
"You must answer it now," she says. "Plainly. And show me what you intended to read."
{n}You step back. The carters resume their work, slowly enough to hear the rest.{/n}''', c('[Give him room to fetch the page.]', "page", flags=("kiana.further_stiff",))),
    n("private", "Narrator", '''{n}Kiana and Rovan move to the far side of the wheel. You wait by the open gate. One carter asks whether you need the road cleared, and seems relieved when you say no.{/n}
{n}You cannot hear the conversation. You can see Kiana point to the notice, wait while Rovan answers, and shake her head at something he tries to add.{/n}
{n}When they return, he carries a folded page.{/n}
"I promised she would come," he tells you. "And I let people believe your request meant more than it did."
"There was no request," Kiana says.
"No. There wasn't. I will tell them."
{n}He hands her the page with less ceremony than he tried to give you.{/n}''', c('[Look at the page with her permission.]', "page")),
    n("page", "Kiana", '''{n}The beginning is hers. Halfway down, the guest has become a weary captain who wins the princess by explaining that other people have difficult lives too. The princess thanks him for correcting her and promises to be less troublesome.{/n}
{n}Kiana reads that passage twice.{/n}
"Did you write this?"
"The ending was missing. I thought it needed a lesson."
"It needed the rest of the play."
"People like a lesson. I read my ending to Orvenna while she was working. She liked it."
"Then they can learn to ask before completing someone else's work."
{n}She smooths the fold with a thumbnail. A pale crystal at her temple catches the light when she bends closer.{/n}
"You may tell your own story about a captain. You may not tell people I wrote this one, or that the Commander ordered them to hear it."''',
      c('"Correct the notice and offer the real scene, if you still want an audience. Everyone can choose whether to stay."', "offer", flags=("kiana.further_offer",), forbids=("kiana.further_withdraw",)),
      c('"Take your page back. He can arrange a different entertainment without borrowing either of our names."', "withdraw", flags=("kiana.further_withdraw",), forbids=("kiana.further_offer",))),
    n("offer", "Kiana", '''"I want them to hear a woman being troublesome without a captain arriving to repair her. Apparently that has become an educational undertaking."
{n}She turns to Rovan.{/n}
"I will come once. You will say that before anyone loses an evening they intended to spend elsewhere. There is no order, no inspection, and no reward for laughing."
"I can say that."
"Say it now to the people who heard you yesterday. Then find someone willing to read the guest. Ask them. That part is important."
{n}Rovan turns toward the carters. His correction is awkward and audible. One tells him he should have made the whole thing a lesson in wheel repair.{/n}
{n}Kiana almost smiles.{/n}''', c('[Leave him to make the remaining corrections.]', "end")),
    n("withdraw", "Kiana", '''{n}Kiana folds her page and puts it away.{/n}
"No performance of mine at this gathering. You have other people to ask, and you can begin by asking whether they want an entertainment."
{n}Rovan looks at the blank space left in his hands.{/n}
"They'll be disappointed."
"I am disappointed now. You will survive sharing the experience."
{n}He starts to lift the board, then stops.{/n}
"Will you come when I tell them? They'll think the Commander stopped it."
{n}Kiana looks at you, then at the carters listening from the wheel.{/n}
"I will come to say I stopped lending you my page. It may be a very short evening."
"All right."
"And you will not advertise that as a performance."''', c('[Leave him to correct what he promised.]', "end")),
    n("end", "Kiana", '''{n}Outside the yard, Kiana walks several paces before speaking.{/n}
"I wanted strangers to enjoy something I made. I was not prepared for enjoying it to include replacing the woman at its center with a grateful cushion."
"You were clear about what you wanted."
"Eventually. There was a moment when I wanted you to frighten him so I would not have to explain anything."
{n}She looks at you sidelong.{/n}
"I am not particularly proud of that moment. I am telling you because it was there."
{n}She takes your arm for the walk back, still angry enough to make her steps quick.{/n}''', c('[Keep the next evening free to finish what was begun.]', flags=("kiana.further_name_kept",))),
], after=())


s("yard_evening", "People who may leave", [
    n("start", "Narrator", '''{n}Rovan meets you at the yard gate. The notice now says there is no requirement to attend and no official sponsorship. The correction occupies more space than the original title.{/n}
"I thought I should make it difficult to miss," he says.
{n}Kiana reads it, then hands him the board.{/n}
"Sensible. A rare but welcome direction for the evening."
{n}Several carters sit along the low wall. Kiana folds her scarf and leaves it beside a clear place to sit. A broad-shouldered woman is trimming a damaged strap. She does not put her work down when you enter.{/n}''',
      c('[Join the voluntary reading.]', "reading", requires=("kiana.further_offer",)),
      c('[Join Kiana while she corrects the promised entertainment.]', "withdrawn", requires=("kiana.further_withdraw",))),
    n("reading", "Narrator", '''{n}Rovan introduces Kiana by name, without appending yours. He says anyone who has better plans should take them. A man near the gate immediately leaves. Rovan looks wounded until Kiana nudges him with her elbow.{/n}
{n}The woman with the strap agrees to read the guest. Her name is Orvenna. She holds the page in one broad hand and gives the princess a skeptical look before delivering a line.{/n}
"Your castle has mice."
"They are hereditary mice," Kiana answers. "One cannot dismiss old retainers merely because they eat the curtains."
{n}Orvenna glances toward a heap of chewed sacking. The yard laughs. Kiana waits for it, then continues without explaining the joke.{/n}
{n}The scene is short. The princess offers an invitation; the guest asks whether the mice will be at supper. No captain appears to settle either question.{/n}''', c('[Let the applause belong to the people who chose to give it.]', "complaint")),
    n("withdrawn", "Kiana", '''"I lent Rovan a page. I did not agree to the changes he made or promise to perform it. He has corrected the notice. I have come because I would rather tell you that myself than have you blame the Commander for withdrawing it."
{n}She does not look at you while she says it.{/n}
{n}The woman with the strap snorts.{/n}
"He's been arranging our leisure all week. Perhaps he'll ask next time."
"Orvenna," Rovan begins.
"Yes. That remains my name when I'm annoyed."
{n}Someone offers to tell a story about a mule that refused a bridge. Orvenna says everyone has heard it, but settles her strap in her lap to listen anyway.{/n}
{n}Kiana sits on the wall beside you. She has recovered her page and given up the chance to have this audience hear it. She listens to the mule story without attempting to turn it into her own evening.{/n}''', c('[Stay until the story has finished.]', "complaint")),
    n("complaint", "Orvenna", '''"I liked the captain better," Orvenna says when the talk pauses.
{n}Rovan makes an unhappy noise. Kiana turns toward her.{/n}
"He knew when someone had been selfish."
"He knew the answer before he arrived," Kiana says. "That is a convenient kind of wisdom."
"Sometimes people leave good men and call it finding themselves. Sometimes the rest of us are expected to clap."
{n}Her eyes move from Kiana to you. There is no mistaking what she is asking now.{/n}
{n}Kiana puts both feet on the ground. She has not yet decided whether she will stand.{/n}''',
      c('"You may dislike a story. That does not give you our private lives to finish for us."', "answer", flags=("kiana.further_spoke",), forbids=("kiana.further_listened",)),
      c('[Stay beside Kiana and let her choose her answer.]', "listen", flags=("kiana.further_listened",), forbids=("kiana.further_spoke",))),
    n("answer", "Kiana", '''"I can answer," Kiana says.
{n}Her voice is quiet enough that you hear the correction before the rest of the yard does.{/n}
"I know."
"Then let me decide how much."
{n}You stop. She turns back toward Orvenna, leaving your hand where it rests beside her on the wall.{/n}''', c('[Let her finish in her own words.]', "history")),
    n("listen", "Narrator", '''{n}You remain beside her. Orvenna looks as if she expected a rebuke from you, and for a moment that expectation occupies the silence.{/n}
{n}Kiana takes a breath. She does not reach for the page or turn toward the gate.{/n}''', c('[Listen.]', "history")),
    n("history", "Narrator", '''{n}Kiana looks directly at Orvenna.{/n}''',
      c('[Hear the answer she chooses about her separation.]', "separated", requires=("kiana.separated",), forbids=("kiana.bereaved", "seelah.elan_dead")),
      c('[Hear the answer she chooses about her bereavement.]', "widow", requires=("kiana.bereaved", "seelah.elan_dead"), forbids=("kiana.separated",))),
    n("separated", "Kiana", '''"Elan is a good man. That is true whether you approve of me or not. I will not tell you that I left a villain so that you can feel comfortable about sharing a wall with me."
{n}She keeps her voice level with effort.{/n}
"He and I have spoken. There are things he has a right to ask me. You are not asking for him."
{n}Orvenna opens her mouth, then closes it.{/n}
"I don't know him," she admits.
"No. You don't. You may dislike what you do know of me. I have no power to make you like it. I came here to settle what was done with my page."
{n}The carter looks down at the strap in her hands.{/n}
"I shouldn't have said it like that."
"No," Kiana says. "You shouldn't."
{n}She rises and turns toward the gate. You leave with her.{/n}''', c('[Leave the exchange there.]', "after")),
    n("widow", "Kiana", '''"My husband died. I did not leave him."
{n}The words stop Orvenna's next breath.{/n}
"I am sorry. I didn't know."
"You knew enough to decide what kind of woman was sitting beside you."
{n}Kiana's voice shakes. She waits until she can continue without raising it.{/n}
"I am not going to tell you about him so that you can revise your opinion of my evenings. I loved him. I miss him. That is what I will say here."
{n}Orvenna sets the strap down.{/n}
"I was thinking of someone else."
"Then you should have spoken to someone else."
{n}Kiana stands. You stand with her.{/n}''', c('[Leave the yard together.]', "after")),
    n("after", "Narrator", '''{n}Outside the gate, Rovan catches up long enough to return a scarf Kiana left on the wall. She takes it without stopping.{/n}
"I'm sorry," he says.
"So am I. Please leave us now."
{n}He does. Kiana walks until the voices from the yard have become part of the general noise of Drezen.{/n}
"I had an excellent answer about the captain," she says. "It involved his being eaten by the mice. I wish I had got to use it."
{n}She tries to smile and fails. When you offer your arm, she takes it, holding more firmly than she usually does.{/n}
"I don't want to be told it went well."
"I won't."
"Thank you. That is the only useful thing anyone has said for several minutes."''', c('[Walk with her until she is ready to go home.]', flags=("kiana.further_yard_kept",))),
], after=("kiana.further_name_kept",))


s("unborrowed_evening", "What she asks of you", [
    n("start", "Kiana", '''{n}Kiana opens the door herself. She has a clean page in one hand and a knife for trimming quills in the other.{/n}
"Come in. The knife is for the pen. I thought I should make that clear before discussing our last outing."
{n}She puts both objects on the table and brings your chair nearer hers.{/n}''',
      c('"How have you been since the yard?"', "notice"),
      c('[Ask to return when you can stay and listen.]', abort=True)),
    n("notice", "Kiana", '''"Cross. Then busy. Then cross because I had nearly enjoyed being busy and remembered I meant to be cross. I am becoming a difficult person to organize."
{n}She takes a short note from beneath the clean page.{/n}
"Rovan has written to apologize. No audience, no notice, no request for you to approve the apology. It is an improvement."
"And Orvenna?"
"Nothing. I do not intend to go looking for her so that we can achieve a pleasing conclusion."
{n}She lays the note down.{/n}''',
      c('[Ask about the page she chose to share.]', "offered", requires=("kiana.further_offer",)),
      c('[Ask about the page she took back.]', "withdrawn", requires=("kiana.further_withdraw",))),
    n("offered", "Kiana", '''"One of the carters asked Rovan for a copy of the scene as I wrote it. He passed the request to me. He did not supply a new ending first."
{n}She touches the clean sheet.{/n}
"I said yes. I am copying it here. Orvenna does not own everyone who sat in that yard, and I liked hearing them laugh at the mice."
"Will you go back?"
"Perhaps. Not because I must prove I am brave, and certainly not because someone has decided I owe them entertainment. I may want to hear another person read that guest."
{n}She moves the blank sheet away from the edge of the table.{/n}
"I will send this first. Then I can decide."''', c('[Ask what she wants to say about your part in the evening.]', "commander")),
    n("withdrawn", "Kiana", '''"It is still mine. That sounds rather grand for a page with a blot in the corner."
{n}She takes it from between two other sheets and lays it flat.{/n}
"I keep imagining how it might have sounded in the yard. Then I remember how much I disliked being promised as if I were part of the refreshments. Both thoughts remain inconveniently persuasive."
"Would you make the same choice?"
"That evening? Yes. Another evening might be different. I do not have to punish every future invitation for Rovan's first one."
{n}She smooths the crease without trying to erase it.{/n}
"For now, I am writing something else. A woman who refuses to attend her own very flattering portrait unveiling. I am enjoying her enormously."''', c('[Ask what she wants to say about your part in the evening.]', "commander")),
    n("commander", "Kiana", '''"There is one part I have been putting off."
{n}She pulls the chair a little closer, then appears annoyed with herself for doing it.{/n}''',
      c('[Hear what she thought of your intervention.]', "spoke", requires=("kiana.further_spoke",)),
      c('[Hear what she thought of your silence.]', "listened", requires=("kiana.further_listened",))),
    n("spoke", "Kiana", '''"I know why you answered Orvenna. For a moment I was glad someone had. Then I heard the Commander telling a carter which questions were permitted, and I wondered whether anyone would hear my answer after yours."
"I did stop when you asked."
"You did. I noticed that too. I am not asking you to accept a version in which you shouted and I was very patient. Neither happened."
{n}She draws one finger along the chair's arm.{/n}
"I want to be able to be angry with somebody in your presence without everyone waiting for your verdict. I do not know how often that will be possible. I want us to try."''', c('[Tell her what you can actually offer.]', "position")),
    n("listened", "Kiana", '''"I saw you decide to wait. I was grateful. I was also furious that I had to find the words while you were sitting right there."
{n}She shakes her head before you can answer.{/n}
"You did what I needed. That does not mean I enjoyed needing it. I thought I should tell you both parts before the second one escaped during some quite unrelated argument."
"What would you want next time?"
"Stay. Listen. If I ask you to speak, speak. It sounds straightforward when I say it here, with no carter deciding she knows my marriage better than I do."
{n}She looks toward the empty doorway.{/n}
"I expect I shall still be cross."''', c('[Tell her what you can actually offer.]', "position")),
    n("position", "Kiana", '''{n}She waits without reaching for her pages. This conversation has no other character she can put between you.{/n}''',
      c('"I can wait for you to ask, even when I dislike what I am hearing."', "wait", flags=("kiana.further_wait_voice",), forbids=("kiana.further_answer_abuse",)),
      c('"I will not answer questions about your life for you. I may still object when someone tries to humiliate you."', "object", flags=("kiana.further_answer_abuse",), forbids=("kiana.further_wait_voice",))),
    n("wait", "Kiana", '''"Thank you. I am not asking you to enjoy it."
"I doubt I will."
"Good. I would find that extremely irritating."
{n}The corner of her mouth lifts. She rests a hand over yours, keeping it there while the silence loses some of its weight.{/n}
"I may ask badly. I may say your name as though you should have guessed ten minutes earlier. You are allowed to remind me that I requested the chance to be difficult for myself."
"I will try to find a tactful moment."
"Please do. Immediately afterward may be unwise."''', c('[Stay with the agreement you have actually made.]', "history")),
    n("object", "Kiana", '''{n}She considers that longer than you expect.{/n}
"Then say you object. Do not tell them what I feel. And if I ask you to stop, stop."
"I can do that."
"I believe you. You have listened to me here. That matters more than devising a perfect answer for someone we may not see again."
{n}Her hand finds yours on the arm of the chair.{/n}
"I will try not to make being loved require your becoming invisible."''', c('[Keep the distinction between defending her and speaking for her.]', "history")),
    n("history", "Narrator", '''{n}She looks at your joined hands before speaking again.{/n}''',
      c('[Stay with the history that began by waiting.]', "waited", requires=("kiana.separated", "kiana.waited"), forbids=("kiana.affair", "kiana.bereaved", "seelah.elan_dead")),
      c('[Stay with the history that includes the undisclosed kiss.]', "affair", requires=("kiana.separated", "kiana.affair"), forbids=("kiana.bereaved", "seelah.elan_dead")),
      c('[Stay with her grief without asking it to explain the whole evening.]', "bereaved", requires=("kiana.bereaved", "seelah.elan_dead"), forbids=("kiana.separated",))),
    n("waited", "Kiana", '''"We waited before we began this. It mattered to me. It did not arrange the rest of the world into people who would understand."
{n}She turns your hand over, tracing the crease beneath your thumb.{/n}
"I am glad we waited. I am also glad we did not decide that waiting had to last until nobody could be hurt. I would still be sending you pages and pretending not to watch the door."
"You watched the door?"
"You were unusually slow with some of the pages. I had to occupy myself somehow."''', c('[Move nearer.]', "desire")),
    n("affair", "Kiana", '''"What we did before I told Elan remains what we did. Orvenna being cruel does not make it suddenly considerate."
"No."
"I have told him the truth. I will not tell every stranger the same thing so that they can decide whether I have been sorry enough to enjoy an evening."
{n}She squeezes your hand.{/n}
"And I will not turn you into a punishment I keep choosing because I am ashamed of wanting you. I do want you. I wanted to say that somewhere no one could mistake it for an argument addressed to them."''', c('[Let her see that you heard her.]', "desire")),
    n("bereaved", "Kiana", '''"I kept thinking of something Elan would have said about that captain. Something very earnest. Then he would have realized the princess was making fun of him and become magnificently embarrassed."
{n}Her smile hurts a little. She lets it remain.{/n}
"That is the memory I wanted to have. Not the one someone demanded because she had already invented a worse story."
"You can tell me more."
"Another evening. Tonight I want this hand and the person attached to it. I would like to discover whether you can be magnificently embarrassed as well."''', c('[Draw her a little closer.]', "desire")),
    n("desire", "Kiana", '''{n}Kiana rises from her chair without letting go of your hand. She stands between your knees, near enough that the cool ends of her hair brush your cheek when she leans down.{/n}
"I have no intention of thanking you for rescuing me from my own temperament."
"I hadn't requested thanks."
"Good. I have something less instructive in mind."
{n}She kisses the corner of your mouth, pauses to see your answer, then smiles.{/n}''',
      c('[Kiss her and stay for the private evening.]', "kiss"),
      c('"Come outside with me. I want some time with you that no one has advertised."', "walk")),
    n("kiss", "Narrator", '''{n}She meets your kiss with none of the composure she maintained in the yard. Her hand slides to the back of your neck. When you stand, she comes with you, laughing softly as the chair catches against your heel.{/n}
"Our scenery remains unreliable."
{n}You move it aside. She closes the door, returns to you, and leaves the pages where they are.{/n}
{n}Later, when the room has grown quiet, she rests her head against your shoulder. She has not become less troublesome. She seems pleased that you have noticed.{/n}''', c('[Keep the evening without making it an answer to the whole city.]', flags=("kiana.further_kept", "kiana.further_private_evening"))),
    n("walk", "Kiana", '''"An unadvertised walk. We shall be a great disappointment to the public."
{n}She takes her scarf from the chair and puts it on without arranging it for effect. At the door she catches your hand again.{/n}
"If anyone asks, we are investigating the quality of the evening air. It is a very serious commission."
{n}You find a quieter street and let the conversation stray. She tells you a dreadful rhyme about the captain, tries a better one, and objects when you prefer the first.{/n}
{n}When you turn back, she draws you close enough to kiss before releasing your hand to open her door.{/n}
"There. Something they may not put on a board."''', c('[Leave her with a real evening to remember and the next one still welcome.]', flags=("kiana.further_kept", "kiana.further_private_walk"))),
], after=("kiana.further_yard_kept",))


def integrate(payload):
    """Gate only an unplayed capstone; never invalidate completed older promises."""
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    required = {s["Id"] for s in SCENES} | {"kiana.a_place_afterward"}
    missing = required - by_id.keys()
    if missing:
        raise ValueError("Missing Kiana further scenes: " + ", ".join(sorted(missing)))
    gate = by_id["kiana.a_place_afterward"]["Requires"]
    if "kiana.further_kept" not in gate:
        gate.append("kiana.further_kept")

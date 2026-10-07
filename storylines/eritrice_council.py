"""Eritrice: the Council, the war and the chair's private life, sitting by sitting (the standing debate, continued).

Every scene is in the Council hall, on her own private list (Council_Eritrice/AnswersList_0002), after the standing
debate has opened (eritrice_minutes). Canon anchors:
- "celestials and beasts are sitting at this table peacefully" (Council_1/Cue_0014 56e90037); Socothbenoth bringing
  the Commander in (Council_1/Cue_0007 b5aa61e8); Chadali's "lucky charm" (Council_1/Cue_0025 866558d6);
- the Commander's motion for material aid, "A sound proposition... we will put it to a vote" (Council_2/Answer_0021
  6801f9cd, Cue_0030 6cc3a4f0); Alichino's wardstones and demon taxes (Council_2/Cue_0014 fe89e404, Cue_0016 76e375a7);
  Cobblehoof's purse (Council_2/Cue_0035 95a29494);
- the notes compared "with something I saw in a certain book" (Council_3/Cue_0014 07c13d2e); Shyka's "dull version of
  the future" (Council_Lexicon2/Cue_0054 1d1c4855);
- the magical orange and the bag (Council_5-1/Cue_0001 dfd57a47, Cue_0002 5e4fabec, Cue_0022 ecbf22d2);
- the dagger at her belt (Council_Eritrice/Cue_0018 3b128644) and the claws (Council_5-2/Cue_0035 b138a1a4);
- Socothbenoth "undressing you with his eyes" (Council_2/Cue_0011 cd1ca02d);
- "Just imagine... a forum for inter-planar debate" (Council_5-2/Cue_0001 3d07c9e5).
"""
from story_format import c, scene
from storylines.eritrice_trickster import CLOSED, COMMITTED, LIST, LOST, e, nar
from storylines.eritrice_minutes import (CONVENING, ESSENCE, POINT_ONE, QUILL, RECORD, SOCOTH_COVERED, SOCOTH_EXPOSED,
                                         WROTE)

SCENES = []
K = "eritrice.council."

AID_MOVED = "eritrice.aid_moved"          # Council_2/Cue_0030: the Commander's motion for material aid, put on her agenda
ORANGE = "council.orange_called"          # Council_5-1/Cue_0020 "An orange! An orange! I knew it!" (bound by trickster_world)
BOOK_SAID = "eritrice.certain_book_said"     # Council_3/Cue_0014: "...compare them with something I saw in a certain book"
THREAT_HEARD = "eritrice.threatened_by_force"  # Council_5-2/Cue_0035: "if you don't offer it up willingly, I'll take it by force!"
DULL_FUTURE = "eritrice.shyka_dull_future"  # Council_Lexicon2/Cue_0054 (c4 folder): Shyka will not read the hidden pages out
SEEN_CUES = {AID_MOVED: ["6cc3a4f0d7dc4c949b62a80dc81cabc0"], DULL_FUTURE: ["1d1c4855bacf5a94fb1e84b7ae8424a3"],
             THREAT_HEARD: ["b138a1a41f4128e43822bb8f3bdc1b4c"], BOOK_SAID: ["07c13d2efd8a90b45824a79873b62108"]}
CIPHER_TAUGHT = "eritrice.minutes.exercise_promised"  # her own sitting "What the truth could not read" (Chapter 5)

FIRST = K + "celestials_and_beasts"
AID = K + "a_sound_proposition"
PROOF = K + "a_proof"
LUCK = K + "luck_is_not_a_position"
ELDEST = K + "the_eldests_version"
BOOK = K + "a_certain_book"
LISTS = K + "the_casualty_lists"
DAGGER = K + "the_dagger"
JEALOUS = K + "his_eyes"
ACCURATE = K + "accurate_minutes"
GIFT = K + "the_six_hundred_and_thirteenth"
EVE = K + "just_imagine"
TWICE = K + "twice_nightly"

NAMED = K + "named_the_dead"
TOLD_PLAN = K + "told_her_the_plan"
KEPT_PLAN = K + "kept_the_plan"
NEW_QUILL = K + "gave_a_quill"


def sitting(id, title, entry, nodes, requires, forbids=(), delay=24, chapters=(3, 5)):
    """A physical sitting on her own private list in the Council hall (while it is open)."""
    SCENES.append(scene(id, title, "Eritrice", min(chapters), entry, nodes, requires=("trickster.ever", *requires),
                        forbids=(CLOSED, LOST, *forbids), delay=delay, last=max(chapters), optional=True,
                        Relationship="eritrice", Chapters=list(chapters), AnswerLists=[LIST]))


# --- Celestials and beasts: the Council, as she sees it. -------------------------------------------------------------

sitting(FIRST, "Celestials and beasts", '"Tell me about the Council. As you see it."', [
    nar("open", '''{n}She is not at the head of the table tonight. She is walking its length slowly, from chair to empty chair, resting her claws on the back of each one as she passes, the way a general walks a line of sentries who cannot see her.{/n}''',
        c("Continue", "start")),
    e("start", '''"As I see it." {n}She considers the phrase, as if it were an amendment she might accept.{/n}
"When Socothbenoth brought you in, you saw a table. By now you have seen all of it: a demon lord with tattoos, a devil in spectacles, a hippogriff with a purse, an azata who thinks luck is a policy, and an Eldest who cannot keep one face for the length of a sentence. You saw a farce." {n}Her claws rest on the table's edge.{/n}
"I see celestials and beasts sitting at one table in peace. Do you know how long it has been since that happened anywhere? I do not. Nobody has kept the minutes."''',
      c('"It is a farce. A useful one."', "farce"),
      c('"I saw you, holding it together by your fingernails."', "holding")),
    e("farce", '''"A useful farce." {n}She repeats it without offence, which surprises you.{/n}
"Yes. That is fair. They are ridiculous, every one of them, and so am I, for thinking they could be otherwise. But the Worldwound is not ridiculous, and every other remedy has been tried with swords." {n}She taps the table.{/n}
"If the only table in the multiverse where Hell and Elysium sit down together is a farce, then I will chair the farce. Somebody must. It will not chair itself; you have seen what happens when I look away."''',
      c("Continue", "members")),
    e("holding", '''{n}She is silent for a moment. Then, with great dignity:{/n} "Claws. Not fingernails."
{n}But her ears have gone back, and something in her shoulders gives, very slightly.{/n} "Yes. I hold it together. Every session. Alichino skips, Socothbenoth flirts, Shyka laughs at jokes nobody has told yet, Cobblehoof snorts at everything, and Chadali claps. And at the end of it, someone has to write down what was decided, even when it was nothing." {n}She looks at the empty chairs.{/n} "Especially when it was nothing."''',
      c("Continue", "members")),
    e("members", '''"You want to know which of them I trust." {n}She does not wait.{/n} "None of them. That is not the purpose of a Council. The purpose of a Council is that I do not need to trust them. I need them in the room, arguing, and I need the minutes to be true."
{n}She folds her hands.{/n} "Trust is for allies. This is a Council. We sit at this table because each of us is certain the others are wrong, and the truth is what is still standing when the arguing is done. That is the whole of my method. Trust comes after, if it comes, and it is earned here by people who could have lied and did not."''',
      c('"And me? Am I Council, or ally?"', "which"),
      c('"You trust Chadali. I\'ve watched you."', "chadali")),
    e("which", '''{n}The quill stops over the scroll.{/n}
"The chair declines to answer that question in session." {n}A long pause.{/n} "This is not a session. It is a private audience. The chair notes the distinction and remains silent anyway."
{n}She writes nothing. Her eyes stay on you until you look away first, and then, very quietly, she makes a sound in her chest that is not a growl.{/n}''',
      c("[Leave the question on the table.]")),
    e("chadali", '''"I do not trust Chadali. I do not need to. Chadali has never once in her existence concealed anything; she would not know how." {n}A faint twitch of the whiskers.{/n}
"She thinks my Council is a wonderful party. She thinks the Worldwound can be fixed by believing in it hard enough. She is wrong about everything and she has never once lied to me." {n}She sighs.{/n} "It is exhausting. I would not change it."''',
      c("[Leave her to her minutes.]")),
], requires=(POINT_ONE,), forbids=(FIRST,))


# --- A sound proposition: the Commander's own motion for material aid. ---------------------------------------------

AID_CHOICES = (
    c('"Then vote on it. The crusade is starving while this Council debates."', "starving"),
    c('"Forget the aid. What I needed, I got: a table where they listen to me."', "forget"),
)

sitting(AID, "A sound proposition", '"About my motion for material aid..."', [
    nar("open", '''{n}She has the old scroll out already, the one from the session when Alichino first took his seat. An item for material aid is on it, in her upright hand, with a note in the margin: "Sound. Debate. Vote." Beneath the note, a blank space awaits the result.{/n}''',
        c("Continue", "moved", requires=(AID_MOVED,)),
        c("Continue", "unmoved", forbids=(AID_MOVED,))),
    e("moved", '''"\'I move that since my army is the only force doing anything practical to close the Worldwound, the Council should consider providing us with some material aid.\'" {n}She reads it aloud, exactly.{/n}
"I called it a sound proposition. I said I would try to fit it on a later agenda." {n}Her claw rests beside the note.{/n} "The motion is still here. The aid is not."''', *AID_CHOICES),
    e("unmoved", '''"You never moved it in session. Everyone else at this table did, in one way or another: Alichino wants the Wardstones sold, Socothbenoth wants something, Chadali wants everyone to be lucky. You asked for nothing." {n}She taps the margin.{/n}
"So I wrote it down for you, as a motion the Commander would have moved had the Commander been less proud. It is not true that you moved it. It is true that you should have. I have marked it as such."''', *AID_CHOICES),
    e("starving", '''"Starving." {n}She sets down the quill. Her claws press into the old scroll.{/n}
"Alichino calls every request from a mortal army begging for charity, and says it is typical of mortals. I have let him say it. I should not have." {n}She writes, quickly.{/n}
"The chair rules that the Commander\'s motion is placed first on the agenda of the next session, above the demon taxes, above the Wardstones, above everything. If anyone walks out before it is voted, the chair will vote it alone, and minute that she did so, and why."''',
      c("[Thank her.]", "close", flags=(K + "aid_first",))),
    e("forget", '''{n}Her ears flick forward.{/n} "You can withdraw the request. You cannot make the soldiers less hungry."
{n}She writes beneath the proposal: "The Commander declines to press the motion. No aid granted."{/n}
"There. An accurate record of a very poor result. If anyone calls this Council generous, I shall read it to them."''',
      c("[Let the record stand.]", "close")),
    e("close", '''"The war does not wait for the agenda. I know that. I have always known it." {n}She rolls the old scroll.{/n}
"I have had members at this table whose cities were burning. I have not had one who made me feel it while I found the right wording. It concentrates the mind." {n}A pause.{/n} "It is unpleasant. Do not stop."''',
      c("[Leave her with the agenda.]")),
], requires=(POINT_ONE,), forbids=(AID,))


# --- A proof: Cobblehoof. ---------------------------------------------------------------------------------------------

sitting(PROOF, "Phrr", '"What does Cobblehoof actually say?"', [
    nar("open", '''{n}A single grey feather lies on the Council table in front of Cobblehoof's chair, shed in some argument you did not attend. She is turning it between two claws, holding it up to the lamp, as though it might yet be entered into evidence.{/n}''',
        c("Continue", "start")),
    e("start", '''"'Phrr.'" {n}She says it perfectly, down to the rattle in the back of the beak, and then looks faintly embarrassed at having done it.{/n}
"He is from Axis. He believes that everything true can be proven, and everything that cannot be proven is noise. When he snorts, it means the argument has not yet been proven. When he snorts twice, it means it cannot be. When he bangs his foreleg on the table, it means he agrees, and would like it written down." {n}She sniffs.{/n} "He is the only member who understands what the minutes are for."''',
      c('"And the purse?"', "purse"),
      c('"You speak hippogriff?"', "speak")),
    e("speak", '''"I speak truth. It sounds different in every mouth, but it is always the same language." {n}She says it with great solemnity, and then her whiskers twitch.{/n}
"Also, we have been at the same table for a very long time. After enough sessions of 'phrr', one begins to hear the tenses."''',
      c('"And the purse?"', "purse")),
    e("purse", '''"He keeps a paw over that purse whenever a mortal sits at the table, as if you were a pickpocket." {n}She allows herself a short, satisfied sound.{/n}
"He fears a mortal might reach for it. He would rather hide the purse than answer the request for aid." {n}Her whiskers lift.{/n} "That is his contribution to the debate."''',
      c("Continue", "orange", requires=(ORANGE,)),
      c("Continue", "close", forbids=(ORANGE,))),
    e("orange", '''"Back in that session, you told Chadali there was a magical orange in his bag." {n}Her voice drops.{/n} "There are no magical orange trees in Axis. I said so. In session. On the record."
"Back in that session, Chadali believed you, and clapped, and Cobblehoof looked as though his entire plane had been insulted." {n}A long pause.{/n} "It was the most undignified session of this Council's existence. I laughed. I had to minute that I laughed."''',
      c('"You laughed?"', "laughed")),
    e("laughed", '''"Once. Briefly. In front of Alichino." {n}Her ears are flat with mortification.{/n}
"Cobblehoof has not forgiven me. He snorts twice whenever I call the session to order now. Twice, Commander. That means it cannot be proven that I am fit to chair."''',
      c("Continue", "close")),
    e("close", '''"He will come back with his proof. He always does. Axis is slow, but it arrives." {n}She writes a note in the margin, in her small private hand.{/n}
"When he does, I would like you to be at the table. He listens to you. So, it appears, do I."''',
      c("[Leave her to her margin.]")),
], requires=(POINT_ONE,), forbids=(PROOF,))


# --- Luck is not a position: Chadali. --------------------------------------------------------------------------------

sitting(LUCK, "Luck is not a position", '"You and Chadali..."', [
    nar("open", '''{n}There is a flower in her inkwell. It was bright once, and it has died, the way everything alive dies in this hall; she has not thrown it out. She is looking at it when you come in, and moves her hand as if to hide it, and then, being who she is, does not.{/n}''',
        c("Continue", "start")),
    e("start", '''"Chadali and I." {n}She sets the quill down, which means she is going to be honest about something she would rather not be.{/n}
"She is from Elysium. She believes in luck, and freedom, and good wishes sent across the planes. She calls you our lucky charm. She calls me 'dear chair' and brings me flowers that die in the hall because nothing grows here." {n}The corner of her mouth draws back from one long tooth.{/n}
"Luck is not a position, Commander. I have told her so in every session since the first. She claps. It is like debating a sunrise."''',
      c('"You\'re fond of her."', "fond"),
      c('"She\'d say the Council exists because you got lucky with Socothbenoth."', "lucky")),
    e("fond", '''"I am..." {n}The word she is looking for does not come. She tries another.{/n} "I am accustomed to her."
{n}And then, because she does not lie:{/n} "Yes. Fond. She is the only member of this Council who has never wanted anything from it except that everyone should have a nice time. It is useless, and it is the kindest thing at this table, and I do not know what to do with it except write it down."''',
      c("Continue", "rival")),
    e("lucky", '''{n}The growl starts and stops.{/n} "She has said so. In session." {n}A pause.{/n} "And she is not entirely wrong, which is the worst thing about her. Socothbenoth suggested the Council. I did not plan it. It fell into my lap, like one of her flowers."
"I have spent a long time pretending my Council was the product of reason. It was the product of a demon's boredom and an azata's optimism. Do not tell her I said so. She would be unbearable."''',
      c("Continue", "rival")),
    e("rival", '''{n}She picks up the quill again, and does not write with it.{/n}
"She likes you. You know that. She has told me, at length, and asked what I thought of you, and I told her I had not yet formed a conclusion." {n}The quill turns.{/n}
"I knew that was untrue. I have not corrected it." {n}The quill stops turning.{/n} "I am telling you instead. This is a private audience, Commander."''',
      c('"Would it bother you? If she and I..."', "bother"),
      c('"I\'m not going anywhere, Madam Chair."', "staying")),
    e("bother", '''"Yes." {n}Immediately. Then, with enormous effort:{/n} "It would bother me. It would not be a reason to object. A Council is not a household. I do not require that my allies have no other allies."
"I would require the minutes to be accurate. And I would growl. You would have to allow me the growl." {n}Her ears are very flat.{/n} "That is the most undignified sentence I have ever spoken. Leave now, before I say something else I will have to live with for the next thousand years."''',
      c("[Leave, smiling.]")),
    e("staying", '''"You do not know that. You are mortal; you do not even know if you are going anywhere tomorrow." {n}But her voice has gone soft around the edges.{/n}
"Still. It is the kind of thing Chadali would say. I find I do not mind it as much from you." {n}She writes, in the small hand: "The floor claims to be staying. Unproven. Hoped."{/n}''',
      c("[Leave her with the note.]")),
], requires=(POINT_ONE,), forbids=(LUCK,))


# --- The Eldest's version: Shyka. ------------------------------------------------------------------------------------

sitting(ELDEST, "The Eldest's version", '"Does Shyka ever tell you the truth?"', [
    nar("open", '''{n}She is speaking when you come in, low and formal, and there is no one in the hall. She is addressing Shyka's empty chair. She stops mid-sentence when she sees you, and does not explain, and the chair, which should look empty, somehow does not.{/n}''',
        c("Continue", "start")),
    e("start", '''"Shyka tells me many truths. That is the difficulty." {n}She rubs the bridge of her nose, where the fur is shortest.{/n}
"They are an Eldest of the First World, and they walk the ways between what was and what may be. Every sentence they speak is true of some future. The trouble is that they choose which future to live in according to which one amuses them most." {n}She looks at Shyka's empty chair, which, of all the chairs, is somehow the one that looks occupied.{/n}
"They laughed at your idea of the crossroads for a very long time. Then they said that moment alone was worth all our endless debates. I have not decided whether that was a compliment to you or an insult to me."''',
      c('"Both. That\'s the kind of thing Shyka means."', "both", requires=(CIPHER_TAUGHT,)),
      c('"You don\'t like them."', "like", requires=(DULL_FUTURE,)),
      c('"Both. That\'s the kind of thing Shyka means."', "both_early", forbids=(CIPHER_TAUGHT,)),
      c('"You don\'t like them."', "like_early", forbids=(DULL_FUTURE,))),
    e("like_early", '''"Fondness is not a qualification for the chair. I am fond of Chadali; that does not settle a disputed motion." {n}A pause.{/n}
"But Shyka frightens me, and I do not say that of anyone. Ask them a plain question and they answer the one you ought to have asked, in a future you have not reached yet, and then they laugh at your face while you work out which." {n}Her claws dig into the table.{/n}
"Every other member of this Council wants something, and a want can be debated. Shyka wants to be entertained. That is the only position at this table I cannot debate, because it does not care whether it is right."''',
      c("Continue", "you")),
    e("both_early", '''"Both. That saves them the trouble of choosing."
{n}She eyes the empty chair.{/n} "It does not save me the trouble of asking. The Council\'s work matters even when Shyka finds it dull."''',
      c("Continue", "you")),
    e("like", '''"Fondness is not a qualification for the chair. I am fond of Chadali; that does not settle a disputed motion." {n}A pause.{/n}
"But Shyka frightens me, and I do not say that of anyone. When you showed us the Lexicon's hidden pages, they read them, and refused to read them out. They said it would lead to a dull future. Not the worst one. Only dull." {n}Her claws dig into the table.{/n}
"They would rather let a true thing stay hidden than let the future be boring. That is the only position at this table I cannot debate, because it does not care whether it is right."''',
      c("Continue", "you")),
    e("both", '''"Both. Yes. A compliment with teeth in it."
{n}She sets the quill down across Shyka\'s empty place.{/n} "I dispute the insult. The debates mattered before they became amusing. I will ask them which they meant, and they will probably offer me a third answer."''',
      c("Continue", "you")),
    e("you", '''"Here is my point, and it is not about Shyka." {n}She turns the quill in her fingers.{/n}
"You are a trickster. Shyka walks between futures and picks the amusing ones. You walk between truths and lies and pick the useful ones. I have been sitting across the table from you for a long while now, and I have not yet decided whether you are more like them, or more like me." {n}She waits.{/n}''',
      c('"Like you. I just lie better."', "me"),
      c('"Like them. But I\'d never choose a dull future for you."', "them"),
      c('"Neither. I\'m the one who makes you both argue."', "neither")),
    e("me", '''"You do lie better. Anyone would." {n}Something like a smile.{/n} "I will accept the comparison. A liar at least knows which side of the truth they are standing on. Most of this Council does not."''',
      c("[Leave her to her finding.]")),
    e("them", '''{n}She is quiet for a moment, and then she laughs, low and surprised, as if the sound had got out before the chair could rule on it.{/n}
"A trickster who would not choose a dull future for me. That is the most frightening thing anyone has said to me since the Council was convened." {n}She writes it down, in full, and underlines "for me".{/n}''',
      c("[Leave her to her underlining.]")),
    e("neither", '''"The floor." {n}She nods slowly.{/n} "Yes. The one who makes the Council argue instead of posture. That is what a floor is for." {n}She writes: "Motion from the floor: that the floor is neither the Eldest nor the chair. Carried, with the chair's grudging concurrence."{/n}''',
      c("[Leave her to her concurrence.]")),
], requires=(CONVENING,), forbids=(ELDEST,))


# --- A certain book: the Lexicon, Chapter 3. -------------------------------------------------------------------------

sitting(BOOK, "A certain book", '"You said you\'d compare the Lexicon with a certain book."', [
    e("start", '''"I did say that." {n}She does not reach for any book. She reaches for the scroll of that session, and finds the line: "I have taken notes as necessary, and later I will have to compare them with something I saw in a certain book."{/n}
"I compared them. I will not tell you which book." {n}She raises one claw before you can object.{/n} "Not because it is a secret. Because I was wrong about it. I believed, for a very long time, that it contained the truth about the Worldwound. It contained a truth. Areelu's notes contain a different one. They cannot both be the whole truth, and I trusted the wrong one for longer than your crusades have had numbers."''',
      c('"What did the Lexicon tell you?"', "lexicon"),
      c('"Being wrong isn\'t lying."', "wrong")),
    e("wrong", '''"No. It is worse. A liar knows where the truth is. I did not." {n}Her ears go back.{/n}
"Rule three: a point conceded stays conceded. I concede that I was wrong for a very long time. It is minuted. Do not make me read it aloud."''',
      c('"What did the Lexicon tell you?"', "lexicon")),
    e("lexicon", '''"That the Worldwound is not a mistake of the world order. It was made, on purpose, by a mortal who wanted a door." {n}She says it the way one might announce a death.{/n}
"I have called it a mistake in every session. An aberration. Something that could be refuted, if only the right truth were found and made public. It was not an aberration. It was a design. You cannot refute a design. You can only take it apart, or finish it differently." {n}She looks at you.{/n} "Which is what you proposed. A crossroads. Areelu's door, finished differently."''',
      c('"Does that frighten you?"', "fear"),
      c('"Then help me finish it."', "finish")),
    e("fear", '''"Yes." {n}At once.{/n} "Because it means that everything this Council has done until you arrived has been debating the wrong question, very politely, with minutes."
{n}She sets the quill down.{/n} "And because it means that the person who will finish the door is a mortal with a Trickster's heart, sitting across the table from me, asking whether I am afraid. I am, Commander. I am also, I find, extremely pleased that it is you."''',
      c("[Leave her with the truth.]")),
    e("finish", '''"I have been helping you. That is what this Council is now, whether its members know it or not." {n}She taps the scroll.{/n}
"Every vote since you arrived has been a vote on your door. I have minuted them as votes on the Worldwound. That is not a lie. It is the same thing, seen from a better angle." {n}Something eases in her shoulders.{/n} "You have taught me angles. I resent it."''',
      c("[Leave her with her angles.]")),
], requires=(CONVENING, "council.session_minuted", BOOK_SAID), forbids=(BOOK,), chapters=(3,))


# --- The casualty lists: the war in the room. -------------------------------------------------------------------------

sitting(LISTS, "The casualty lists", '"You\'re reading the lists again."', [
    nar("open", '''{n}The crusade's casualty lists are spread over half the long table: the latest from Drezen, older ones from the Worldwound's edge, a few in hands you do not recognise. She has weighted them with inkwells and read every one. Some names have a small mark beside them, in her private hand.{/n}''',
        c("Continue", "start")),
    e("start", '''"Your clerks send these to Nerosyan. I read them before Nerosyan does." {n}She does not ask whether that is permitted.{/n}
"I mark the ones who died in ways the report does not explain. 'Lost in action.' 'Missing, presumed.' 'Accident on the march.' Every one of those phrases is somebody declining to keep the minutes." {n}She looks at you.{/n} "You know some of these names. I would like you to tell me one of them. Truly. Who they were, and how they died. Not as the report says. As it was."''',
      c("[Tell her about someone you lost, truthfully.]", "told"),
      c('"I can\'t. Not tonight."', "cannot"),
      c('"They died so this Council could keep debating."', "bitter")),
    e("told", '''{n}You tell her. She does not write while you speak. When you have finished, she takes the list the name is on, finds it, and writes beside it in her upright hand, the hand the Council reads: what happened, in your words, in full.{/n}
"There. Now it is true." {n}Her claws are trembling very slightly.{/n}
"I cannot do this for all of them. I do it for the ones someone will tell me. That is one more than yesterday."''',
      c("[Stay while the ink dries.]", flags=(NAMED,))),
    e("cannot", '''"No. Of course not." {n}She puts the list down, gently.{/n}
"I should not have asked it as if it were a point. It is not a point. It is a debt, and it is not yours to pay tonight." {n}She folds the lists, one by one, and stacks them at her elbow.{/n}
"When you can, come and tell me. I will keep the space beside the name empty until then. I am good at keeping spaces."''',
      c("[Leave her with the lists.]")),
    e("bitter", '''{n}The growl is immediate and real, and her claws come out and go into the table. For a moment she is exactly the thing the Council fears when it walks out on her.{/n}
"Do not." {n}Very quietly.{/n} "Do not say that to me as if I had not read every one of these." {n}She draws the claws back, slowly.{/n}
"...But I have read them. And I have debated. And they are still dying. You are right, and I hate that you are right, and I will not strike it from the record."''',
      c("[Leave the point standing.]")),
], requires=(POINT_ONE,), forbids=(LISTS,))


# --- The dagger: her temper, in her own telling. ---------------------------------------------------------------------

sitting(DAGGER, "The dagger", '"You wear a dagger to a debate."', [
    nar("open", '''{n}The dagger is out of its sheath. You have never seen it out before. It lies on a square of oiled cloth in front of her, and she is cleaning a blade that has no mark on it, slowly, with the absorbed care of someone who has done this a great many times and has never once needed to.{/n}''',
        c("Continue", "start")),
    e("start", '''{n}She does not stop. She turns the blade to the lamp, and then, deliberately, lays it down between you with her hand still on the hilt, as though to prove she is not ashamed of it.{/n}
"I do. I have never drawn it at this table. That is a fact, and you may check the minutes." {n}She looks at you steadily.{/n}
"You want to know whether I have drawn it elsewhere. Everyone does, eventually. Socothbenoth asked on his first day, and I told him the truth, and he stopped flirting with me for almost a week."''',
      c('"Have you?"', "have"),
      c('"You don\'t have to tell me."', "dont")),
    e("dont", '''"I do not have to. I will anyway. That is the difference between a truth and a confession: a confession is dragged out of you."''',
      c("Continue", "have")),
    e("have", '''"Yes." {n}She says it the way she says everything, plainly.{/n}
"There are liars who cannot be refuted. They are not wrong; they know exactly where the truth is, and they stand in front of it, and they will not move. I have debated such creatures for a very long time. And once, in my own telling, which is the only one there is, I stopped debating." {n}Her thumb moves on the hilt.{/n}
"I will not tell you who. I will tell you that I minuted it afterwards, in full, and that it is the only entry in all my records I have never reread."''',
      c('"Would you do it again?"', "again"),
      c('[Put your hand over hers, on the hilt.]', "hand")),
    e("again", '''"Yes." {n}No hesitation.{/n} "If there were a liar standing in front of a truth that people were dying for want of, and the liar would not move. Yes."
"That is why I wear it to a debate, Commander. Not because I expect to use it. Because I want everyone at this table to know that I know I could. It keeps the debate honest." {n}She lets go of the hilt.{/n} "It frightens you. Good. It frightens me."''',
      c("[Let it frighten you.]", flags=(K + "dagger_feared",))),
    e("hand", '''{n}Her fingers are warm and very still under yours. Neither of you moves.{/n}
{n}At last she speaks.{/n} "If I ever draw it at this table, I want your hand to be there. Exactly there. Not to stop me. So that I have to feel it, and decide."
{n}She lifts her hand from the hilt, and leaves yours there a moment longer, and then takes it and holds it, hard, as if it might be called to order.{/n}''',
      c("[Hold on.]", flags=(K + "dagger_held",))),
], requires=(CONVENING,), forbids=(DAGGER,))


# --- His eyes: jealousy, after the commit. ---------------------------------------------------------------------------

JEALOUS_OPEN = (
    c("Continue", "exposed", requires=(SOCOTH_EXPOSED,)),
    c("Continue", "covered", requires=(SOCOTH_COVERED,), forbids=(SOCOTH_EXPOSED,)),
    c("Continue", "plain", forbids=(SOCOTH_EXPOSED, SOCOTH_COVERED)),
)

sitting(JEALOUS, "Undressing you with his eyes", '"Something wrong, Madam Chair?"', [
    nar("open", '''{n}She stands behind Socothbenoth\'s chair, both hands on its back. Fresh claw marks score the wood beneath her fingers.{/n}''', *JEALOUS_OPEN),
    e("exposed", '''"He did it again. At the session. He looked at you the way he looks at everything he wants to take apart and put back together wearing different clothes." {n}Her claws are in the chair's back.{/n} "And now I know why he wanted this Council. Now I know what he wants from everyone. And he still looks at you like that, at my table."''',
      c("Continue", "confess")),
    e("covered", '''"He did it again. At the session. You told me he was bored, and a bored demon looks at a mortal like that for the entertainment." {n}Her claws are in the chair's back.{/n} "I have watched Socothbenoth undress you with his eyes across my own table. I minuted nothing. It was accurate. It still is."''',
      c("Continue", "confess")),
    e("plain", '''"He did it again. At the session. He looks at you as if he were undressing you with his eyes, and I have not rebuked him, because it is accurate." {n}Her claws are in the chair's back.{/n} "It is still accurate. It is accurate at every session. I have minuted it as 'Socothbenoth attended'."''',
      c("Continue", "confess")),
    e("confess", '''{n}She lets go of the chair, and looks at the marks her claws have left, and seems for a moment genuinely shocked by them.{/n}
"The chair is jealous." {n}She says it like the reading of a verdict.{/n} "It is a very stupid feeling, and I resent having it about a demon lord with scented sleeves. It argues with itself and loses both sides."''',
      c('"You\'ve got nothing to be jealous of."', "nothing"),
      c('[Flirt] "I like it on you."', "like"),
      c('"Then minute it. Accurately."', "minute")),
    e("nothing", '''"That is not true. Socothbenoth is beautiful and old and powerful, and wants you, and does not keep minutes." {n}She says each item as if entering it.{/n}
"But it is true that you are here, after the session, and he is not." {n}Something eases in her face.{/n} "The chair concedes that the evidence favours the floor. The chair does not concede the feeling. Feelings are not subject to evidence. I have just learned that, and I dislike it."''',
      c("[Go to her.]")),
    e("like", '''{n}The growl is low, and long, and at the end of it there is something else entirely.{/n}
"You would." {n}She comes around the chair, slowly.{/n} "You like everything that makes me less dignified. The growling. The laughing. The chair taken out of my hands." {n}She is very close now.{/n} "Very well. The chair is jealous, and the floor likes it. Minuted. Now come here and give me a reason to stop."''',
      c("[Give her one.]")),
    e("minute", '''"Accurately." {n}She sits, and pulls the scroll toward her, and writes, and reads it aloud as she goes:{/n} "'Socothbenoth attended. He looked at the Commander. The chair wished to remove his eyes. The chair refrained.'"
{n}She sands it.{/n} "There. It is true, and it is terrible, and it is on the record. I feel much better. That is also terrible."''',
      c("[Kiss the top of her head.]")),
], requires=(COMMITTED,), forbids=(JEALOUS, "socot.gone", "council.walked_out"), delay=48)


# --- Accurate minutes: the other lovers, after the commit. ---------------------------------------------------------

sitting(ACCURATE, "Accurate minutes", '"You wanted to discuss... other matters?"', [
    e("start", '''"Other members." {n}She has a fresh scroll, and she has written at its head, in her private hand: "Matters of the heart. Not for the Council."{/n}
"I am told that the Commander does not sit only at this table. I am told this by Chadali, who thinks it is lovely, and by Socothbenoth, who thinks it is hilarious, and by Alichino, who thinks it is leverage." {n}She looks up.{/n}
"I would like to hear it from you. Accurately. I do not want anyone's minutes of my own life but my own."''',
      c("[Tell her the truth: every name.]", "truth"),
      c('"There are others. I won\'t name them. They\'re not yours to minute."', "private"),
      c('"There\'s no one else."', "lie")),
    e("truth", '''{n}You tell her. She listens, and does not write, and when you are finished she is quiet until the lamp wants trimming.{/n}
"Thank you." {n}She means it; you can hear that it has cost her.{/n} "A Council is not a household. I have never required that my allies have no other allies. I do not require it now." {n}Her ears go back, very slightly.{/n}
"I require that you do not lie to me about it. You have not. That is all the chair asks. The lion asks more, and the lion will be growled at until it stops."''',
      c("Continue", "rule")),
    e("private", '''"Not mine to minute." {n}She weighs it.{/n} "That is fair. Their records are their own. I would not want mine read aloud at another's table."
"But you have told me they exist, and you have not pretended otherwise, and that is the point." {n}She writes nothing on the scroll.{/n} "The chair accepts a sealed record. The chair has sealed a few of her own."''',
      c("Continue", "rule")),
    e("lie", '''{n}She does not write. Her face grows formal, and she leaves the quill poised above the empty line.{/n}
{n}Very quietly:{/n} "Rule two. A point is answered honestly or not at all." {n}She waits.{/n}
"Three members of this Council have told me otherwise, and they agree on nothing else. They may all be wrong; it would not be the first time. If they are, say it again, plainly, and I will minute it and believe it. If they are not, I did not ask so that you could protect me. Try again."''',
      c("[Tell her the truth: every name.]", "truth"),
      c('"...There are others. I won\'t name them."', "private"),
      c('"They\'re wrong. There is no one else."', "only")),
    e("only", '''{n}She looks at you for a long time, the way she reads a motion twice before she votes. Then she writes, in the private hand: "The Commander sits at one table."{/n}
"Then the Council is wrong, which it frequently is. Chadali will be disappointed; she had hoped for a crowd." {n}Her ears tilt.{/n} "If that changes, I expect to be told before Chadali is."''',
      c("Continue", "rule")),
    e("rule", '''"I will make one rule, and I will write it down, so that neither of us can pretend later that it was otherwise." {n}She dips the quill.{/n}
"Nobody at this table is asked to give anyone up. Not now, not later. If one day it comes to a vote, I will vote against making you choose." {n}She writes it, and raises her own hand, and waits for yours.{/n} "I dislike sharing your attention. I will not pretend that gives me authority over another woman."''',
      c("[Raise your hand. Aye.]", flags=(K + "no_one_given_up",))),
], requires=(RECORD,), forbids=(ACCURATE,), delay=48)


# --- The six hundred and thirteenth: a quill. ------------------------------------------------------------------------

sitting(GIFT, "The six hundred and thirteenth", '[Give her a new quill.] "For the record."', [
    e("start", '''{n}She looks at the quill in your hand and does not take it. It is white, and long, and very plain, cut the way she cuts her own.{/n}
"Where did you get this." {n}Not quite a question.{/n}
"I cut them myself. Always. From the same bird, which I will not name, because Chadali would want to visit it." {n}She takes it, turns it to the lamp, and her ears go forward.{/n} "This is cut as I cut them. Exactly." {n}She turns the feather once more.{/n} "You went to some trouble."''',
      c("Continue", "wrote", requires=(WROTE,)),
      c("Continue", "plain", forbids=(WROTE,))),
    e("wrote", '''"The cut matches mine." {n}She sets it against the quill you once held, comparing their tips.{/n} "You chose something I can use. I intend to. Give me the ink."''',
      c("Continue", "use")),
    e("plain", '''{n}She tests the quill on a scrap of parchment. The line comes cleanly; she writes your name again beneath it.{/n}
"It suits my hand. I shall keep it. Come and see what I write with it."''',
      c("Continue", "use")),
    e("use", '''"It is the six hundred and thirteenth." {n}She sets the old one down, the six hundred and twelfth, very carefully, beside the scroll.{/n}
"I will use it for the Council's minutes. All of them. From tonight." {n}She dips it, and writes the date, and then, beneath it, before anything else: "The chair's quill was cut by the Commander."{/n}
"There. Now every session this Council ever holds begins with you. Nobody else will know why. I will."''',
      c("[Watch her write the first line.]", flags=(NEW_QUILL,))),
], requires=(QUILL, COMMITTED), forbids=(GIFT,), delay=72)


# --- Just imagine: the eve of the last session (Chapter 5). -----------------------------------------------------------

sitting(EVE, "Just imagine", '''"The next session..."''', [
    e("start", '''"Just imagine." {n}She is standing at the far end of the hall, where the lamplight hardly reaches, looking at nothing, as though the thing she is describing were already there in the dark.{/n}
"The Worldwound, transformed into a forum for debate between the planes. Neutral ground for angels and demons, azatas and devils, the fey, the qlippoths, things from beyond the edge of everything. All of them resolving their disagreements with facts and logic instead of blades and spells." {n}She turns.{/n} "At the next session we shall have to decide what to do with the cauldron. The essences. Everything we have argued for, while the crusade waits for us to stop talking."''',
      c("Continue", "ask")),
    e("ask", '''"You have said very little about that session." {n}She sits and folds her hands over the scroll.{/n} "What will you do when they ask for the other essences? Not what you would like. What you mean to do."''',
      c('[Tell her the truth: it may end in blood.] "They\'ll turn on you. When they do, I won\'t stand between you and them. I\'ll stand where I have to."', "truth", flags=(TOLD_PLAN,)),
      c('[Lie] "I\'ll vote with you. Whatever comes."', "lie", flags=(KEPT_PLAN,)),
      c('"I don\'t know yet. I\'ll know when I see their faces."', "unknown")),
    e("truth", '''{n}She does not answer at once. Her claws are flat on the scroll.{/n}
"You think it will come to a fight." {n}Not a question.{/n} "And if it does, you do not know whose side you will be on. Because it may not be mine."
{n}She writes the warning in full.{/n} "Thank you. I would rather hear it here than learn it on the floor of my own hall."''',
      c("[Stay with her tonight.]")),
    e("lie", '''{n}She believes you. Her shoulders loosen, and she reaches for the quill.{/n}
"Whatever comes." {n}She writes it down, and underlines it, and blots it with great care.{/n}
"Then I have your vote at the next session." {n}She reaches for your hand.{/n}''',
      c("[Take her hand.]")),
    e("unknown", '''"That is an honest answer, and a terrible one." {n}She sets down the quill.{/n}
"I have chaired a very long time, Commander. I know what it means when the floor will not say how it will vote. It means the floor is afraid of the chair\'s face when it hears." {n}Her hand rests beside the quill.{/n}
"Whatever you do at that session, it will be minuted truly." {n}She touches your cheek with the back of one claw.{/n} "That much I can promise."''',
      c("[Stay with her tonight.]")),
], requires=(CONVENING, ESSENCE), forbids=(EVE, "eritrice.essence_given", "council.walked_out"), chapters=(5,))


# --- Twice nightly: the standing debate, in private. ----------------------------------------------------------------

sitting(TWICE, "Twice nightly", '"Is the chair in session?"', [
    nar("open", '''{n}Late. The hall is dark but for the lamp at the head of the table, and she is not at the head of the table. She is sitting on it, at the far end, with her feet on the seat of Alichino's chair, reading the evening's minutes by the light of a single candle she has brought down from somewhere.{/n}''',
        c("Continue", "start")),
    e("start", '''"The chair is still in session." {n}Her feet rest on Alichino\'s empty chair. The public minutes are finished, but she has not gone home.{/n}
"I was waiting for you. Sit here." {n}She pats the table beside her, then looks at the casualty list folded beneath the scroll.{/n} "We have heard enough bad news tonight."''',
      c('"Is that a complaint?"', "complaint"),
      c('[Sit beside her on the table.]', "beside")),
    e("complaint", '''"No. An invitation." {n}She puts the scroll aside and reaches for your sleeve.{/n} "Must I chair that too? Come closer."''',
      c("Continue", "beside")),
    e("beside", '''{n}The table creaks under both of you. She lets her shoulder rest against yours, and after a moment her hand, claws drawn in, settles on your knee as deliberately as if she were placing a weight on a scroll to keep it flat.{/n}
"What happens afterwards is that the one who lost wants to debate again. Immediately. On any subject. At length." {n}Her voice has gone low and warm.{/n} "I have drafted a motion. I would like to move it now, while the Council is not here to be scandalised."''',
      c('"Move it."', "move")),
    e("move", '''"I move that the debate be held twice nightly." {n}She says it with perfect solemnity, and then ruins it by purring at the end.{/n}
"Seconded?" {n}She turns her head, and her whiskers brush your jaw, and her breath is warm on your throat.{/n} "The floor is taking a very long time to second a simple motion. I want you, and I am not a patient lion. I will count to three. One."''',
      c("[Second it before she reaches two.]", "carried")),
    e("carried", '''"Carried." {n}She pushes the scroll off her knees, swings one leg across you, and settles astride your lap on the edge of the Council\'s table, with a creak of old wood and a rumble in her chest that is very nearly a purr. She takes your hands and sets them on the belt at her waist, and holds them there until you pull it loose. Only then, with her mouth already on yours and her gown sliding off one shoulder, does she reach back and pinch out the candle.{/n}
{n}The minutes slide from the table. This time she leaves them where they fall. "I shall write it down in the morning," she murmurs against your mouth. "Give me something worth the ink."{/n}''',
      c("[Give her a great deal to write.]", flags=(K + "twice_nightly_carried",))),
], requires=(RECORD,), forbids=(TWICE,), delay=24)


# --- A point of personal privilege: the chair's feelings, before the second reading. -----------------------------------

FEELINGS = K + "personal_privilege"

sitting(FEELINGS, "A point of personal privilege", '"You look like you have a point to raise."', [
    nar("open", '''{n}She is not writing. The scroll is open in front of her, the quill is inked, and she is sitting with both hands flat on the table on either side of it, like someone bracing against a ship's roll. When you come in she does not look up, and then, all at once, she does.{/n}''',
        c("Continue", "start")),
    e("start", '''"A point of personal privilege." {n}She says it very fast.{/n} "It is a procedure. I am instituting it now, for this table and this debate: a member may interrupt any business to raise a matter affecting their own conduct or condition, and it takes precedence over everything else on the agenda. I have just raised one."
{n}Her claws tap the table: once, twice, and then do not stop.{/n}
"I have never used it. In all the time this Council has sat, I have never once had a matter affecting my own condition that I considered worth the Council's time."''',
      c('"And now you do."', "now"),
      c('"The floor yields to the chair."', "yields")),
    e("yields", '''"The floor is very gracious." {n}It comes out almost as a growl, and she stops it, visibly.{/n} "The floor is being gracious on purpose, because the floor knows exactly what the chair is about to say and wants to watch her say it."''',
      c("Continue", "now")),
    e("now", '''"The matter is this." {n}She takes a breath.{/n}
"The chair has found that she cannot chair a session at which the Commander is present with the same attention she gives to sessions at which the Commander is absent. She has checked. She has compared the minutes. When you are at the table, the minutes are shorter, and the chair's hand is worse, and on two occasions the chair has written the Commander's name where she meant to write 'Worldwound'." {n}She turns the scroll so that you can see the two crossed-out lines.{/n}
"That is a matter affecting the chair's conduct. It is also a matter affecting her condition. I do not know which is worse."''',
      c('[Flirt] "Both, I hope."', "both"),
      c('"You could have just told me."', "told"),
      c('[Reach across and still her tapping claws.]', "still")),
    e("both", '''"You hope." {n}Her ears flatten and lift and flatten again.{/n} "You come into my hall, dispute my motions, and then sit there hoping I cannot write the word \'Worldwound\' without thinking of you." {n}A breath.{/n}
"It is working. Minute that. No. I will minute it myself. It is my privilege, and I am exercising it."''',
      c("Continue", "close")),
    e("told", '''"I have just told you. This is how I tell things. In order, with a procedure, on the record, so that I cannot pretend afterwards that I said something else." {n}Her breath has gone short.{/n}
"You would have preferred that I say it in a corridor, perhaps, with my back to you, and then deny it at the next session. That is how mortals do it. I have read your plays. I did not care for them."''',
      c("Continue", "close")),
    e("still", '''{n}Your hand closes over hers. The tapping stops. Under your fingers the claws are drawn in, but the whole hand is humming with something, like a harp string a moment after it has been plucked.{/n}
{n}Quite quietly:{/n} "That is not a procedure." {n}She does not take her hand away.{/n}
"The chair notes that the floor has responded to a point of personal privilege with an irregular physical intervention. The chair does not object. The chair would like that very clearly understood."''',
      c("Continue", "close")),
    e("close", '''"The point is raised. It is not a motion. There is nothing to vote on." {n}She writes, and her hand is not very good.{/n}
"When there is something to vote on, it will be put to you properly, at a reading. Not in a hurry, not in a corridor, not by a trick. That is what I can give you that no one else at this table can. Everything I feel, in order, minuted, with a vote at the end." {n}She blots the line.{/n} "It is not very romantic. It is what I have."''',
      c('"It\'s the most romantic thing anyone\'s ever said to me."', "romantic"),
      c("[Leave her to her minutes.]")),
    e("romantic", '''{n}She stares at you. Then she looks down at the scroll, and writes something very small in the margin, and covers it with her hand before you can read it.{/n}
{n}Without conviction:{/n} "That is a lie. I will check. I will find out. I have the rest of the war to find out."''',
      c("[Leave her to find out.]")),
], requires=(CONVENING,), forbids=(FEELINGS, COMMITTED))


# --- Where the chair goes home: Nirvana, in her own telling. ---------------------------------------------------------

HOME = K + "where_the_chair_goes_home"

sitting(HOME, "Where the chair goes home", '"Where do you go, when the Council adjourns?"', [
    nar("open", '''{n}She is standing at the far end of the hall with her eyes closed and her head a little on one side, as if listening to something a very long way off. When she opens her eyes, it takes her a moment to come back from wherever it was.{/n}''',
        c("Continue", "start")),
    e("start", '''"Home." {n}She says it as if the word were slightly improper.{/n}
"Nirvana. You have heard the name. Your priests say it as if it were a reward, and your poets as if it were a silence. It is neither. It is the plane where goodness does not need to be argued for, because everyone already agrees." {n}She taps the quill against the scroll.{/n}
"I find it very difficult to be there for long. Nobody disagrees with me. Do you know what that is like, for someone like me? It is like being a sword in a world without anything to cut."''',
      c('"So you built a Council to have someone to argue with."', "built"),
      c('"What\'s it like? Tell me, in your own words."', "like")),
    e("like", '''"In my own words. Everything I tell you about it is in my own words; there are no others that would be accurate." {n}She closes her eyes, and for a moment the chair is gone from her face.{/n}
"There are the records I keep at home, every true thing I have heard said in honest debate, written down, and I seldom need to consult them, because nobody who comes to my home lies to me twice. There is a garden where the lions lie down in the evening and nobody asks why. There is my study, with every scroll I have ever written, in order, from the first to this one, and a window that looks out on a light that never goes down." {n}She opens her eyes.{/n}
"It is very beautiful. I have spent most of my existence somewhere else."''',
      c("Continue", "built")),
    e("built", '''"I convened the Council because the Worldwound needed another answer. I also wanted an argument worth having. Both are in my private papers."
{n}She turns your chair toward hers.{/n} "You dispute my conclusions and still come back. Tonight I am pleased about the second part. The first remains contested."''',
      c('"Would you show me? Nirvana. After the war."', "show"),
      c('"You\'d be bored with me there too, eventually."', "bored")),
    e("show", '''{n}She is quiet.{/n}
"I do not know how a living mortal would make that journey, or what it would cost you to make it, and I will not pretend to know." {n}Her voice is careful.{/n} "I will not tell you that I can bring you there safely. I do not know if it is true. But I will tell you this, and it is true: the window in my study has room for two chairs, and I have only ever set one."
{n}She writes nothing. She only looks at you, in the lamplight, as if memorising a record she does not intend to keep on paper.{/n}''',
      c("[Hold her gaze.]", flags=(K + "second_chair",))),
    e("bored", '''"Possibly. You might grow tired of arguing with me first."
{n}She moves your chair a little nearer the lamp.{/n} "Tonight you have surprised me. Tomorrow I have work, and so have you. Come back after it. We shall find out how long this lasts."''',
      c("[Leave her to her fury.]")),
], requires=(POINT_ONE,), forbids=(HOME,))


# --- A lie for the chair (Chapter 5): the one thing she cannot do herself. -----------------------------------------

LIE = K + "a_lie_for_the_chair"
LIED_FOR_HER = K + "lied_for_her"
REFUSED_TO_LIE = K + "refused_to_lie_for_her"

sitting(LIE, "A lie for the chair", '"You sent for me. Alone."', [
    e("start", '''"I have a request. I do not want it minuted." {n}The scroll is still rolled. She keeps glancing at the quill.{/n}
"The Council\'s plan will need Elysium as well as Nirvana. They will look to Chadali for it. She brings flowers to this table. They will ask her to bleed into the cauldron."
{n}Her claws catch in the wood.{/n} "I can see Alichino counting the samples already. Hers will be another useful thing to him. I do not want it to happen."''',
      c('"What do you want me to do?"', "want")),
    e("want", '''"I want you to lie." {n}Her claws dig into the table.{/n}
"When the Council discusses the other essences, tell them that an azata\'s would spoil the mixture. Say the Lexicon warns against it. You brought us the book. They may believe you."
{n}She looks at the unused quill.{/n} "I cannot say it and then pretend I merely kept the minutes. Nor can I ask you and pretend the lie is yours alone. I am asking anyway. For Chadali."''',
      c('[Agree] "I\'ll tell them. They\'ll believe it."', "agree", flags=(LIED_FOR_HER,)),
      c('"No. If you want her protected, protect her yourself. Honestly."', "refuse", flags=(REFUSED_TO_LIE,)),
      c('"Why don\'t you just tell them the truth? That you won\'t let them hurt her."', "truth", flags=(K + "truth_for_chadali",))),
    e("agree", '''{n}Her shoulders drop, and for a moment she looks enormously tired.{/n}
"Thank you." {n}And then, almost at once:{/n} "No. That is not the whole truth. The whole truth is that I asked a trickster to lie on my behalf so that I could keep my own hands clean, which is exactly what I have despised Alichino for, at this table, for as long as he has sat at it."
{n}She takes the quill out of its stand, and turns it over, and puts it back without writing.{/n} "I said I did not want it minuted. I have changed my mind. It will be. In my own hand. Tonight."''',
      c("[Let her write it.]", "close")),
    e("refuse", '''{n}The growl starts, and she chokes it off.{/n}
"You are right. I knew you would say it, and I asked anyway, because I hoped you would not." {n}She sits back.{/n}
"The honest way is to stand in front of the Council and say that I will not allow it, and to be told that I am the chair, not a guardian, and to lose the vote, and to have it on the record that I lost." {n}Her claws draw in, slowly.{/n} "Very well. I will lose honestly. It is the only way I know how to lose. You taught me that it can be done."''',
      c("[Stay while she drafts it.]", "close")),
    e("truth", '''"Because it is a preference, not an argument." {n}She stops.{/n} "It is also true. I do not want Chadali hurt."
{n}She draws the scroll toward her.{/n} "Then I shall say it when the Council raises the other essences. My preference, in my own name. Alichino will enjoy that."''',
      c("[Stay with her.]", "close")),
    e("close", '''"The request belongs in my private record. Chadali\'s answer will belong in the Council\'s." {n}She touches the rolled scroll, then takes up the quill.{/n} "I would rather she never read this page. That is a wish, Commander. Not a ruling."
{n}Her eyes stray to the quill.{/n} "When this war is over, Commander, I intend to spend a very long time working out how much of what I have become at this table is your fault. I suspect the answer will be: most of it."''',
      c("[Leave her to her reckoning.]")),
], requires=(POINT_ONE, "council.cauldron_given"), forbids=(LIE,), chapters=(5,))


# --- The mortal clock: after the commit. ----------------------------------------------------------------------------

CLOCK = K + "the_mortal_clock"

sitting(CLOCK, "The mortal clock", '"You\'re counting something."', [
    e("start", '''"Years." {n}She does not pretend otherwise. There is a sheet of figures at her elbow, in the small private hand, with some of the numbers struck out and rewritten.{/n}
"I have been calculating. It is a habit. I calculate how long a debate will last, how long a Council will hold, how long before the truth comes out." {n}She turns the sheet face down.{/n} "I have been calculating how long I will have you. I did not want to. I did it anyway. It is a very small number."''',
      c('"The Worldwound might make it smaller."', "smaller", requires=("eritrice.proposed_key",)),
      c('"Then don\'t waste any of it counting."', "waste"),
      c('[Turn the sheet back over and read it.]', "read"),
      c('"The Worldwound might make it smaller."', "smaller_early", forbids=("eritrice.proposed_key",))),
    e("smaller_early", '''"Yes. I included it." {n}Very quietly.{/n} "I have read every report you have sent this Council, and some you did not send. I know what the war does to the ones who go nearest the Wound. I put that in the figures. And then I put in the chance that you do something no one has predicted, which with you is very high." {n}A breath.{/n}
"The figures do not agree with each other. I am considering disciplining them."''',
      c("Continue", "close")),
    e("smaller", '''"Yes. I included it." {n}Very quietly.{/n} "I have read the Lexicon. I know what the wound does to the one who carries it. I put that in the figures too. And then I put in the crossroads, and the chance that it heals you, and the chance that it does not, and the chance that you do something no one has predicted, which with you is very high." {n}A breath.{/n}
"The figures do not agree with each other. My own arithmetic has never before refused to come to a conclusion."''',
      c("Continue", "close")),
    e("waste", '''"Counting is not waste. Counting is how I know what a thing is worth." {n}But she does not turn the sheet back over.{/n}
"You will die, Commander. Soon, as I measure things. I will not. Every one of your crusades has been a single breath to me. I have watched four of them draw in and let out." {n}Her claws rest on the back of the sheet.{/n} "I mind this one."''',
      c("Continue", "close")),
    e("read", '''{n}She lets you. Down the left side, in her small hand, a column of numbers, each one smaller than the last, each one struck out. At the bottom, not a number at all but a single line, underlined, and then struck out, and then written again beneath: "Not enough."{/n}
"I wrote that as a finding. Then I struck it out, because it is a feeling, not a finding. Then I wrote it again, because it is also true."''',
      c("Continue", "close")),
    e("close", '''"Here is my ruling, and I have thought about it a long time." {n}She takes the sheet and tears it, carefully, in half, and then in half again.{/n}
"I will not count any more. I will keep the minutes instead. Every sitting, every point, every night. If the number is small, the record will be long. When you are gone, I will have all of it, true, in order, and I will read it, and argue with it, and it will not always win." {n}Her voice does not break, because she will not let it.{/n}
"That is the only defence against time I know of. It is the one I have used against everything else. I am going to use it against losing you."''',
      c("[Take her hand.]", flags=(K + "counting_stopped",))),
], requires=(RECORD,), forbids=(CLOCK,), delay=72)


# --- Gah: the walk-out branch (Chapter 5): Socothbenoth leaves, and the hall stays open. ----------------------------

GONE = K + "so_many_years"

sitting(GONE, "So many years of preparation", '"Socothbenoth\'s gone."', [
    nar("open", '''{n}His chair is empty, and it will stay empty; she has already turned it to face the wall. The Council met, and waited for something that did not come, and Socothbenoth slumped in disappointment and left, and nobody fought, and nobody was bled. The hall is still open. She is still here.{/n}''',
        c("Continue", "start")),
    e("start", '''"'So many years of preparation, wasted.'" {n}She quotes him, precisely.{/n} "He said that. At my table. As if my Council had been a trap he had been baiting for years, and the quarry had simply not come."
"I suppose that is exactly what it was. You told me, or I should have seen it. He wanted his sister, and he wanted this table to catch her with, and when she did not come, he had no further use for us." {n}Her claws are sheathed. She seems almost too tired to draw them.{/n}''',
      c("Continue", "exposed", requires=(SOCOTH_EXPOSED,)),
      c("Continue", "covered", requires=(SOCOTH_COVERED,), forbids=(SOCOTH_EXPOSED,)),
      c("Continue", "plain", forbids=(SOCOTH_EXPOSED, SOCOTH_COVERED))),
    e("exposed", '''"You told me the truth about him, the night I asked. I said I would never again mistake his reasons for mine. I did not. I watched him wait for her all session, and I knew what he was waiting for, and I chaired anyway." {n}She looks at the turned chair.{/n} "That is the one comfort in this. I was not fooled at the end. Only at the beginning."''',
      c("Continue", "now")),
    e("covered", '''"You told me he was bored." {n}She says it without heat, which is worse.{/n}
"I believed you. I stepped onto it like ice. I have been reading back through my minutes tonight, and the line is there: 'The Commander holds that Socothbenoth is bored.' I underlined nothing." {n}She looks at you.{/n} "I do not ask why you lied. I think you did it to spare me. I think it did not spare me. It only moved the sparing to tonight."''',
      c('"I\'m sorry. I should have told you."', "now"),
      c('"You were happier not knowing."', "happier")),
    e("happier", '''"Yes. I was." {n}She does not argue it.{/n} "That is the most dangerous sentence a mortal has ever said to me, and it is true, and I am going to write it down so that I never believe it again."''',
      c("Continue", "now")),
    e("plain", '''"I did not see it. I suspected, at the end. I did not see it." {n}She looks at the turned chair.{/n} "He brought me the idea of a Council. He brought me you. He waited at my table for someone who never came, and I thought, all that while, that he was debating."''',
      c("Continue", "now")),
    e("now", '''"And yet." {n}She straightens, visibly, the way she does before calling a session to order.{/n}
"And yet the Council did not fight. Nobody drew anything. Nobody was bled. Shyka is still laughing somewhere and Cobblehoof is still snorting and Chadali is still clapping, and Alichino will turn up at the next session as if he had never missed one." {n}Her whiskers lift, very slightly.{/n}
"The table stands. He left it, and it stands. Do you know how rare that is? A table that survives the one who set it up for a trap?"''',
      c('"You set it, Madam Chair. He only suggested it."', "set"),
      c('"Then call the next session."', "next")),
    e("set", '''{n}She stares at you. Then she looks down the length of the long table, at every chair, at the one turned to the wall.{/n}
"I did set it." {n}Slowly.{/n} "He suggested. I convened. I chose the chairs and the rules and the minutes. He brought a trap. I brought a table. Only one of us is still here." {n}She takes up the quill.{/n}
{n}She does not write it down at once. She sits with her hand flat over the scroll, and her shoulders, which you have only ever seen squared, are not.{/n}
"You comforted me. It worked. I do not know how, and I am not going to minute it. Stay until I do."''',
      c("[Stay while she writes.]", flags=(K + "table_stands",))),
    e("next", '''"Yes." {n}She reaches for a fresh scroll.{/n} "The Council will reconvene. Without him. The first item on the agenda will be the Worldwound, as it always has been. The second item will be the Commander's crossroads, as it has been since you arrived."
{n}She stops writing. She looks at the turned chair for a long while, and then at you, and when she speaks again there is no agenda in it at all.{/n}
"I was not wasted. Was I? Tell me I was not. I will believe you. You are the only one here I would believe."''',
      c('"You weren\'t wasted. You were the only one of them who meant it."', flags=(K + "table_stands",))),
], requires=(POINT_ONE, "council.walked_out"), forbids=(GONE,), delay=0, chapters=(5,))


# --- The Fool King: the Trickster's lie that came true. ---------------------------------------------------------------

FOOL = K + "the_fool_king"

sitting(FOOL, "The Fool King", '"You\'ve heard about Thaberdine."', [
    e("start", '''"Everyone has heard about Thaberdine. Chadali has heard about him three times, and told me four." {n}Her claws are flat on the table.{/n}
"A drunkard in a Drezen tavern who claims to be the rightful king of Sarkoris. A crown from nowhere. A pig at his feet. And the Commander of the Fifth Crusade, in front of the whole tavern, set the crown on his head and pronounced him king." {n}She says "pronounced" as if it were an obscenity.{/n}
"I would like to know, for the record, whether you believed a word of it."''',
      c("Continue", "tablet", requires=("fool_king.tablet_true",)),
      c("Continue", "ask", forbids=("fool_king.tablet_true",))),
    e("tablet", '''"And then you went to Pulura's Fall, and brought back a stone, and the letters on it repeated his words." {n}Her voice has dropped very low.{/n}
"His family tree. Carved in stone, in a place he has never been, saying exactly what a drunkard said in a tavern after you told him it was all true." {n}She looks at you, and there is something in her face you have not seen before, and it takes you a moment to recognise it as fear.{/n}
"Answer me carefully, Commander. Did the stone say it before you believed him, or after?"''',
      c('"I don\'t know. That\'s the honest answer. I don\'t know."', "dont_know"),
      c('"After. It usually is, with me."', "after")),
    e("ask", '''"Did you believe him?"''',
      c('"No. But he deserved a crown more than most kings I\'ve met."', "deserved"),
      c('"I trusted my intuition. It said: it\'s all true."', "intuition")),
    e("deserved", '''"That is not a reason to crown a man. That is a reason to buy him a drink." {n}But the tip of her quill taps the table, once, which in her is almost a laugh.{/n}
"He means to defend this city, I am told, should it come to that. With a tankard, and his friends, and a great deal of singing. The reports are not clear, because the men who wrote them were also drunk." {n}She sighs.{/n} "I cannot refute it. I have tried. I have minuted it as 'unverified, regrettably plausible'."''',
      c("Continue", "close")),
    e("intuition", '''"Your intuition." {n}The growl is very soft.{/n} "I have spent my existence arguing that truth is found through honest debate. You found it by feeling it in a tavern and saying it out loud until it was so." {n}Her claws curl.{/n}
"That is not how it works. That cannot be how it works. If it is how it works, then my Council is a very elaborate way of doing slowly what you do in an evening with a crown and a pig."''',
      c("Continue", "close")),
    e("dont_know", '''{n}Her whiskers settle, slowly.{/n} "That is the correct answer. It is the only answer that does not terrify me." {n}She writes it down.{/n}
"If you had said \'before\', I would have had to believe that you found a buried truth, which is what I do. If you had said \'after\', I would have had to believe that you make them, which is what I fear. \'I do not know\' leaves room for both. I can minute that answer without inventing the rest."''',
      c("Continue", "close")),
    e("after", '''{n}Her claws come out, and go into the table, and stay there.{/n}
"Then you are the most dangerous creature I have ever sat across from, and I have sat across from Socothbenoth." {n}Very quietly.{/n}
"A liar lies, and the truth is still there, underneath, waiting to be found. A thing that makes its lies true leaves nothing underneath. Nothing to find. Nothing to debate." {n}She draws the claws back, one at a time, with visible effort.{/n} "And yet here you are, debating me. Point by point. Why would a creature like that bother?"''',
      c('"Because you\'re the one thing I can\'t make true by saying it."', "cant"),
      c('"Because it only works on fools and kings. You\'re neither."', "cant")),
    e("cant", '''{n}She stares at you. Then something in her face gives, like a knot coming loose.{/n}
"Yes. That is right. You cannot say 'the chair agrees' and make it so. You have to argue. You have to win the vote." {n}She takes up the quill.{/n} "That is why you come here. It is the only table in your life where your tricks do not work. I have been flattering myself that it was my conversation."''',
      c("Continue", "close")),
    e("close", '''"Thaberdine is king of Sarkoris, then. Or of a tavern. The record will show whichever proves true, when it proves true." {n}She writes, in the upright hand:{/n} "The Commander crowned a king. The chair reserves judgement on the king. The chair has formed her judgement on the Commander, and declines to minute it."
{n}Without looking up, she adds:{/n} "It is not unfavourable. That is all you are getting."''',
      c("[Leave her with her reservations.]")),
], requires=(POINT_ONE, "fool_king.crowned"), forbids=(FOOL,))


# --- The Lady in Shadow (Chapter 5): Nocticula, and the Commander's other dealings. ---------------------------------

NOCTA = K + "the_lady_in_shadow"
NOCTA_NAMED = "eritrice.nocticula_named"    # Council_5-1/Cue_0063 "even if, by some miracle, we manage to outwit Nocticula"
SEEN_CUES[NOCTA_NAMED] = ["f2022cc8f6117df4c9418824428c592a"]

sitting(NOCTA, "The Lady in Shadow", '"You mentioned Nocticula in session."', [
    e("start", '''"I said that even if, by some miracle, we managed to outwit Nocticula and collect her essence, it would do us no good. Hers is from the Abyss, like her brother's, and the Worldwound is already connected to the Abyss." {n}She recites it exactly.{/n}
"That was an argument about essences. This is not. This is about the fact that when I said her name, you did not look at the Council. You looked at the door." {n}Her amethyst eyes do not move from you.{/n}
"I keep the minutes, Commander. I notice where people look."''',
      c('"I have dealings with her. They\'re not the Council\'s business."', "dealings"),
      c('"You notice too much."', "notice"),
      c('[Lie] "I was looking at Socothbenoth."', "lie")),
    e("lie", '''"No, you were not. Socothbenoth was looking at the door. You were looking at it with him." {n}She does not raise her voice.{/n}
"You may keep your dealings from me. You may not tell me they do not exist. Rule two." {n}She waits.{/n}''',
      c('"...I have dealings with her. They\'re not the Council\'s business."', "dealings")),
    e("notice", '''"It is my element. I cannot stop noticing any more than you can stop playing tricks." {n}A pause.{/n} "And I notice that you have not denied anything."''',
      c('"I have dealings with her. They\'re not the Council\'s business."', "dealings")),
    e("dealings", '''"They are not." {n}She agrees at once, which surprises you.{/n}
"A demon lord of the Abyss. Our Lady in Shadow, as her worshippers say. Her brother sits at my table and hates her, and her essence cannot help us. Whatever you do with her, it is not on my agenda." {n}Her claws tap, once.{/n}
"But you are on my agenda. I would rather hear what you want than guess. I am not asking you to give her up. I do not require that my allies have no other allies. Even in the Abyss." {n}Her claws tap the wood.{/n} "I would like to know what you see in her."''',
      c('"Would it bother you? If it were more than dealings?"', "more"),
      c('"You\'d really sit at a table with her?"', "table")),
    e("more", '''"Yes." {n}Immediately, and then, carefully:{/n} "It would bother the lion. The chair would note that the Commander keeps company with a demon lord who tells the truth when it serves her and lies when it serves her better, and that the Commander keeps company with the chair, who has staked everything on the truth being worth more than either. The chair would find that very interesting, and would want to understand it."
{n}The fur along her jaw rises and settles.{/n} "Understanding things is how I stop them from bothering me. It has never failed yet. I suspect Nocticula will be the first."''',
      c("Continue", "close")),
    e("table", '''"I sit at a table with her brother. I sat at one with Alichino for a very long time before I noticed what he was." {n}She considers.{/n}
"I would sit at a table with Nocticula, yes, if she would sit and argue instead of seducing the chairs. I doubt she would. But the offer would be minuted. Every plane is welcome at my table. That was always the point, and I will not make an exception because the Commander looks at doors."''',
      c("Continue", "close")),
    e("close", '''"The chair's ruling." {n}She writes as she speaks.{/n} "The Commander's dealings with the Lady in Shadow are not the Council's business. The chair notes that they exist. The chair does not object. The chair will growl."
{n}She sands the line.{/n} "There. It is true, and it is fair, and it is minuted. You may go and look at doors."''',
      c("[Go.]")),
], requires=(POINT_ONE, NOCTA_NAMED), forbids=(NOCTA,), chapters=(5,))


# --- The fair copy: a record for a mortal. ----------------------------------------------------------------------------

FAIR = K + "the_fair_copy"

sitting(FAIR, "The fair copy", '"What\'s that?"', [
    e("start", '''{n}It is a scroll, but not one of the Council's. It is shorter, bound with a ribbon of amethyst silk, and it has been written in the upright hand from end to end, without a single correction.{/n}
"A fair copy. Of our debate. Every sitting, every point, from our first private debate to last night." {n}She holds it out, and then does not quite let go of it.{/n}
"I made it for you. You are mortal, and you forget things, and your clerks lose your papers, and you are going into a war I cannot follow you into. I want you to have a true record. Of this. Of me."''',
      c("[Take it.]", "take"),
      c('"Keep it. You\'ll remember it better than I will."', "keep")),
    e("keep", '''"That is true. It is not the point." {n}She presses it into your hands, and this time lets go.{/n}
"The minutes are not for the one who keeps them. They are for the one who needs to know, later, what was really said. That is you, Commander. On some bad night at the edge of the Worldwound, you will need to know that someone argued with you as an equal and lost, gladly, and wrote it down."''',
      c("Continue", "read")),
    e("take", '''{n}It is heavier than it looks. She watches you hold it with an expression you have seen on her only when a vote is being counted.{/n}
"Read the first line. Not now. When I am not watching. I could not bear to watch you read it."''',
      c("Continue", "read")),
    e("read", '''"There is one thing in it that is not in the Council's minutes." {n}She is not looking at you.{/n}
"At the end, after the last sitting, I have added a line. It is not a record of anything that was said. It is a record of something that is true, which I have never said aloud, and which I will not say now, because I would growl, or worse." {n}Her ears are flat.{/n}
"It is written down. That is how I say things. You will have to read it."''',
      c('[Unroll it to the end, in front of her.]', "unroll"),
      c("[Put it away, for later.]", "later")),
    e("unroll", '''{n}Under the last date, in her upright hand: "I love you. This is not a motion before the Council." She reaches for the ribbon, then leaves your hands alone.{/n}
"Well? Refute it."
{n}Her voice is stern. Her ears are forward, and she has stopped breathing quite evenly.{/n}''',
      c('"I can\'t. Carried."', "carried", flags=(K + "fair_copy_read",))),
    e("later", '''"Later." {n}She nods, too quickly.{/n} "Yes. That is better. When I am not here." {n}She busies herself with the Council's scroll, and her hand is not steady.{/n}
"If you are ever in doubt of anything, Commander, read it. I have never written anything that was not true. I have never written anything truer than that."''',
      c("[Keep it close.]", flags=(K + "fair_copy_kept",))),
    e("carried", '''"Carried." {n}Her voice is not quite steady.{/n}
"The chair has now said it. In writing. Which counts. It is minuted in two places now, and you are holding one of them." {n}She reaches over and rolls the scroll closed in your hands, gently, and ties the ribbon.{/n} "Take care of it. It is the only fair copy. I could make another. I will not."''',
      c("[Keep it close.]")),
], requires=(RECORD,), forbids=(FAIR,), delay=48)


# --- A motion to expel: Alichino moves against the mortal member. ---------------------------------------------------

EXPEL = K + "a_motion_to_expel"
AUDACITY = "eritrice.alichino_remembers"    # Council_2/Cue_0034 "What rash audacity... I will remember this..."
SEEN_CUES[AUDACITY] = ["784db62832f3c0743a9250b2382052c1"]

sitting(EXPEL, "A motion to expel", '"You look like you\'ve had a letter from Hell."', [
    e("start", '''"From Erebus. Alichino does not attend sessions, but he writes." {n}She lays the letter on the table between you, face up. The hand is small and very neat, and the seal is black.{/n}
"He moves that the mortal member be expelled from the Council. The grounds are that the Commander \'brings the petty concerns of a single crusade to a body concerned with the multiverse\', that the Commander \'is unreliable in procedure\', and that the Commander \'adjourns meetings without the authority of the chair\'." {n}She pauses.{/n} "Those are his grounds." {n}She turns the page.{/n} "He supports the second ground by quoting, in full, the chair\'s own censure of you, for the motion you carried in a room with no floor. He has copied it out of my minutes in a very small, very neat hand. He has copied my own words."''',
      c("Continue", "remembers", requires=(AUDACITY,)),
      c("Continue", "rule", forbids=(AUDACITY,))),
    e("remembers", '''"He said, the day you met him, that he would remember your audacity. He does. Devils always do. It is the most reliable thing about them." {n}Her claws tap the black seal, once.{/n}''',
      c("Continue", "rule")),
    e("rule", '''"Here is my difficulty, and I want you to understand it before you say anything clever." {n}She folds her hands.{/n}
"The motion is properly made. It is in writing, it states its grounds, it was submitted before the session. By the rules I wrote, I must put it on the agenda. If I refuse because the chair is fond of the mortal member, then the chair's minutes are worth exactly as much as Alichino's contracts." {n}Her ears go back.{/n}
"So it will be debated. And the Council will vote. And I do not know how the Council will vote. Shyka will do whatever is funniest."''',
      c('[Trickster] "Let me handle Alichino. By the next session, he\'ll withdraw it himself."', "trick"),
      c('"Put it on the agenda. I\'ll argue my own case."', "argue"),
      c('"Recuse yourself. You can\'t chair a vote on me."', "recuse")),
    e("trick", '''"I do not want to know how." {n}At once.{/n} "If you tell me how, I will have to minute it, and if it is what I suspect, I will have to minute it with a very specific word."
{n}She weighs you, the way she weighs an amendment.{/n} "If Alichino withdraws his own motion, freely, in writing, the chair will accept the withdrawal. The chair will not inquire into his reasons. The chair notes that she is declining to inquire, and that she will enjoy not knowing." {n}She looks, for a moment, almost smug.{/n} "Go. Before I change my mind."''',
      c("[Go and find a devil's weak spot.]", "close", flags=(K + "alichino_handled",))),
    e("argue", '''{n}She looks at you with an expression very close to pride.{/n}
"Yes. That is what I hoped you would say, and I did not dare suggest it." {n}She draws the agenda toward her and writes it in, first item, above the Worldwound.{/n}
"You will stand at my table and argue your own place at it, and I will chair the debate as if I did not care how it ended. I will care very much. No one will know. That is what it is to be the chair." {n}She blots the line.{/n} "Prepare. His submission quotes my censure word for word. He will make you answer it."''',
      c("[Prepare your case.]", "close", flags=(K + "argued_own_case",))),
    e("recuse", '''"Recuse myself." {n}Her claws stop tapping.{/n}
"Hand the chair to someone else. For one vote. Because I cannot be impartial about you." {n}A long silence.{/n} "That is correct procedure. It is also an insult to the chair, and a true one, which is the worst kind."
{n}She writes: "The chair recuses herself from the motion to expel the Commander, on grounds of partiality, which she declares." She signs it hard enough to tear the scroll.{/n}
"Cobblehoof will chair it. He will snort at everything. It will be the longest session in the history of the multiverse."''',
      c("[Thank her.]", "close", flags=(K + "chair_recused",))),
    e("close", '''{n}As you turn to go:{/n} "Whatever happens at that session, it will be minuted truly. If they expel you, I will write it down. And then I will write a dissent, in my own name, as the chair, and I will enjoy every line of it." {n}She looks at the black seal.{/n}
"It will be very long. It will be the best thing I have ever written. Alichino will have to read all of it, because the rules require it."''',
      c("[Leave her drafting the dissent in advance.]")),
], requires=(POINT_ONE,), forbids=(EXPEL,))


# --- The motion to expel, resolved (Sol r2 BEL): each approach the Commander chose, and what came of it. ---------------

sitting(K + "the_motion_to_expel_voted", "The motion to expel", '"About Alichino\'s motion..."', [
    nar("start", '''{n}The black-sealed letter lies on the Council table, answered. Beside it the agenda of the last session is open at its first item.{/n}''',
        c("Continue", "handled", requires=(K + "alichino_handled",)),
        c("Continue", "argued", requires=(K + "argued_own_case",)),
        c("Continue", "recused", requires=(K + "chair_recused",))),
    e("handled", '''"Alichino withdrew his motion." {n}She says it to the agenda.{/n} "In writing, freely, the day before the session. His letter of withdrawal is three lines long and gives no reason. The chair did not inquire. The chair notes that the devil's handwriting was, for the first time in the history of this Council, not quite neat."
{n}She strikes the item through, once, precisely.{/n} "Whatever you did, Commander, he will remember it. So will I. I am not asking."''',
      c("[Say nothing.]")),
    e("argued", '''"The motion failed." {n}She lets herself say it plainly, once, before she says it properly.{/n} "His written case was read in full. You answered the censure, then the charge that one crusade had no place at this table. Shyka laughed at exactly the moment that did him the most harm. Cobblehoof abstained, loudly. Chadali voted twice and was ruled out of order once."
"Minuted: the motion to expel the mortal member fails. The chair\'s dissent, drafted in advance, was not required." {n}Her claws rest on a thick roll of paper at her elbow.{/n} "The chair has kept it anyway."''',
      c("[Ask to read the dissent.]")),
    e("recused", '''"Cobblehoof chaired it." {n}Her ears go back at the memory.{/n} "It was the longest session in the history of the multiverse, as I said it would be. He snorted at every speaker. The motion failed on a tie, broken by the chair, who was, for one vote, a hippogriff who dislikes devils rather more than he dislikes mortals."
"I was not permitted to vote. I sat at the side of my own hall with my hands in my lap and watched my Council decide about you without me." {n}She looks at her hands.{/n} "It was correct procedure. I will not do it again."''',
      c("[Take her hands.]")),
], requires=(EXPEL,), forbids=(K + "the_motion_to_expel_voted",), delay=48)
SCENES[-1]["RequiresAnyGroups"] = [[K + "alichino_handled", K + "argued_own_case", K + "chair_recused"]]   # one approach was chosen


# --- The rules of the Crossroads (Chapter 5): the forum she dreamed of, drafted with the Commander. -----------------

RULES = K + "rules_of_the_crossroads"

sitting(RULES, "The rules of the Crossroads", '"You\'re drafting something."', [
    e("start", '''"Standing orders. For the Crossroads." {n}There are six scrolls on the table, overlapping, each one covered in her upright hand and each one heavily struck through.{/n}
"If the Worldwound becomes what you proposed, a place where every plane meets, then someone will have to write the rules of debate. Who speaks first. How long. What counts as an argument and what counts as a sword with a sentence attached." {n}She pushes the scrolls toward you.{/n}
"I have been trying for a week. Every draft assumes that everyone will be honest. You have taught me that this is not a safe assumption."''',
      c('"Rule one: everyone keeps their own minutes."', "minutes"),
      c('"Rule one: nobody may carry a weapon into the hall. Not even the chair."', "weapon"),
      c('"Rule one: any member may move a motion from the floor. Even a mortal."', "floor")),
    e("minutes", '''"Everyone keeps their own minutes." {n}She turns the idea over.{/n} "So that nobody can claim the record was falsified, because there are a hundred records, and they must all be reconciled. It would take forever."
{n}Her whiskers lift.{/n} "It would take forever. It would also make lying at the Crossroads almost impossible, because a hundred planes would have to tell the same lie." {n}She writes it at the top of a fresh scroll.{/n} "Rule one. Carried. Next."''',
      c("Continue", "two")),
    e("weapon", '''{n}Her hand goes to the dagger at her belt, and stays there.{/n}
"Not even the chair." {n}A long pause.{/n} "You are asking me to walk into my own forum unarmed, with demons on one side and devils on the other, and trust that the rules will hold." {n}She unbuckles the dagger and lays it on the table between you.{/n}
"Yes. That is the only rule that proves the forum means it. Force proves nothing; I have said so for longer than you have been alive. If I say it at the Crossroads, I must say it with empty hands." {n}She writes it.{/n} "Rule one. Carried. I hate it. Next."''',
      c("Continue", "two", flags=(K + "dagger_laid_down",))),
    e("floor", '''"Even a mortal." {n}She repeats it, and her ears go forward.{/n}
"You want there to be a floor. Not only lords and powers with chairs, but a floor, from which anyone may rise and move a motion that no one expected." {n}She taps the scroll.{/n} "That is what you were, at my table. The floor. The only member who ever surprised the Council."
{n}She writes it at the top.{/n} "Rule one. Carried. The chair notes that this rule gives a public floor to mortals without a seat, not only to this Commander."''',
      c("Continue", "two")),
    e("two", '''"Rule two is harder." {n}She sets the quill down.{/n}
"Who chairs? Not me. I want to, more than I have wanted anything except one other thing, and that is exactly why it must not be me. A forum where the one who dreamed it also chairs it is a forum that belongs to its chair." {n}Her claws curl.{/n}
"You will say it should be me anyway. You will be kind. Do not be kind. Tell me the truth."''',
      c('"It should be you. Not because you dreamed it. Because you\'re the only one who\'d let it outvote you."', "you"),
      c('"Rotate it. Every plane chairs in turn. Even the Abyss."', "rotate")),
    e("you", '''{n}She looks at you, and keeps looking.{/n}
"That is not kindness." {n}Slowly.{/n} "That is an argument. It is a good one. The chair should be the one who will accept losing. And I have lost to you so often now that I have practised." {n}Her voice is not quite level.{/n}
"I will put it to the Crossroads. They will vote. If they vote for me, I will chair. If they do not, I will sit on the floor, next to wherever you are sitting, and move motions until they regret it."''',
      c("[Help her write it.]", "close")),
    e("rotate", '''"Even the Abyss." {n}She winces, visibly.{/n} "A demon lord chairing a session of the Crossroads. Deskari's heralds calling the planes to order."
"...It is correct. If the forum means what it says, every plane must be able to hold the chair, and every plane must be able to lose it. Otherwise it is only my Council with a larger table." {n}She writes it.{/n} "I will be the first chair. You will allow me that. Then I will hand it on. And I will keep the minutes of whoever follows, because somebody must."''',
      c("[Help her write it.]", "close")),
    e("close", '''{n}You work on the standing orders until the lamp needs trimming, and then past it. She writes; you argue; she strikes out; you laugh; she growls and writes it anyway. At the end there are nine rules on a clean scroll, and at the foot of it she has left a space for two signatures.{/n}
"The war is not won. The Worldwound is not a crossroads. Nothing on this scroll is true yet." {n}She signs.{/n} "But it is written down, in two hands, and I have never yet abandoned a thing I wrote down in my own. Sign, Commander."''',
      c("[Sign.]", flags=(K + "crossroads_drafted",))),
], requires=(COMMITTED, CONVENING), forbids=(RULES,), delay=48, chapters=(5,))


# --- Epilogue paragraphs on the committed page (eritrice.trickster.epilogue.we_did_meet). ---------------------------

EPILOGUE_PARAGRAPHS = [
    (NEW_QUILL, "{n}Every volume of her minutes after the war begins with the same line, in the same hand, before the date: \"The chair's quill was cut by the Commander.\" She cut all the later ones herself, and never once got them quite as right.{/n}"),
    (NAMED, "{n}Beside a name on an old casualty list from the Fifth Crusade, in the chair's upright hand, is an account of how a soldier really died. It is the only such note on the list. It was the first of a great many she wrote in later years, at the Commander's dictation, for the dead nobody else had kept minutes for.{/n}"),
    (TOLD_PLAN, '''{n}Before the Council\'s confrontation over the essences, the Commander told Eritrice that it might end in blood. She recorded the warning, word for word. Whatever followed, she had been told.{/n}'''),
    (KEPT_PLAN, '''{n}In Eritrice\'s private minutes, "Whatever comes" is underlined twice. It remains a record of the Commander\'s promise. She did not enter it as proof of what happened afterwards.{/n}'''),
    (K + "crossroads_drafted", "{n}The standing orders of the Crossroads were nine rules long, and the forum they were written for never sat. The first copy, the one with two signatures at its foot, hung in the chair's study anyway, beside the window with room for two chairs.{/n}", dict(forbids=("ending.trickster_full", "ending.trickster_allplanes", "ending.trickster_allplanes_fw"))),
    (K + "dagger_laid_down", "{n}The Crossroads she had drafted rules for never sat. She kept the dagger on a shelf in her study anyway, where the Commander had seen her lay it down, as the rules would have required.{/n}", dict(forbids=("ending.trickster_full", "ending.trickster_allplanes", "ending.trickster_allplanes_fw"))),
    (K + "crossroads_drafted", "{n}The standing orders of the Crossroads of Worlds were nine rules long, and the first copy, the one with two signatures at its foot, was never filed with any archive. It hung in the chair's study, beside the window with room for two chairs.{/n}", dict(any_groups=[["ending.trickster_full", "ending.trickster_allplanes", "ending.trickster_allplanes_fw"]])),
    (K + "dagger_laid_down", "{n}She walked into the first session at the Crossroads unarmed, as the rules required. The dagger stayed on a shelf in her study, where the Commander had seen her lay it down, and she did not take it up again.{/n}", dict(any_groups=[["ending.trickster_full", "ending.trickster_allplanes", "ending.trickster_allplanes_fw"]])),
    (K + "fair_copy_read", "{n}The Commander kept a short scroll bound in amethyst silk for the rest of their life, and read its last line more often than anyone knew.{/n}"),
    (LIED_FOR_HER, '''{n}Eritrice\'s private minutes recorded a request that the Commander lie for Chadali. The promise was there; a public statement was not. She kept the two entries distinct, even after the opportunity had passed.{/n}''', dict(forbids=(K + "lie_for_chadali_spoken", K + "lie_for_chadali_withdrawn"))),
    (K + "counting_stopped", "{n}She never again calculated how long she would have the Commander. She kept the minutes instead, every night, and when the time came, the record was very long.{/n}"),
    (K + "no_one_given_up", "{n}One rule in her private minutes was never amended, not once, in all the years after: nobody at her table would ever be asked to give anyone up.{/n}"),
]


def integrate(payload):
    """Bind this module's own reads, and extend her committed page with the sittings' consequences."""
    from story_format import p
    for key, cues in SEEN_CUES.items():
        have = payload.setdefault("SeenCues", {}).get(key)
        if have is not None and have != cues:
            raise ValueError("Conflicting binding: " + key)
        payload["SeenCues"][key] = list(cues)
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    page = by_id["eritrice.trickster.epilogue.we_did_meet"]["Nodes"][0]
    for flag, text, *extra in EPILOGUE_PARAGRAPHS:
        kw = extra[0] if extra else {}
        page.setdefault("Paragraphs", []).append(p(text, requires=(flag,), forbids=kw.get("forbids", ()), any_groups=kw.get("any_groups", ())))


# AUTHORED: one interjection at Council_5-2/AnswersList_0021, before native extraction.
# STAGED, not exported: E14b must append this entry after all four native answers.
# src/Main.cs currently inserts before the last answer. The coordinator enables
# integrate_public(payload) only after supplying that shared placement contract.
# This adds a record, not an exemption, an extraction, or Chadali's answer.
PUBLIC = K + "chadalis_essence"
TRUTH_FOR_CHADALI = K + "truth_for_chadali"
LIE_SPOKEN = K + "lie_for_chadali_spoken"
LIE_WITHDRAWN = K + "lie_for_chadali_withdrawn"
TRUTH_SPOKEN = K + "truth_for_chadali_spoken"
PROTECTION_SPOKEN = K + "protection_for_chadali_spoken"
PROTECTION_REQUESTED = K + "refused_to_lie_for_her"
FINAL_LIST = "2e2e6dd9c2bf7d748972de8d5a65b8ad"


def _public_e(id, text, *choices):
    # E14f: portrait/name alone does not bind the native speaker.
    return e(id, text, *choices, speaker_unit="4a47d14a45ce264408a1c6a33345dd89")


PUBLIC_SCENES = [scene(PUBLIC, "Chadali's essence", "Eritrice", 5,
    '"Before anyone uses the cauldron: Chadali."', [
    _public_e("start", '''{n}Eritrice's quill stops. Chadali glances from her to the cauldron.{/n}
"The floor has raised Elysium's contribution. Let us hear it before we decide who is to bleed."''',
        c("[Address the Council.]", "promise", requires=(LIED_FOR_HER,)),
        c("[Yield the floor to Eritrice.]", "protect", requires=(PROTECTION_REQUESTED,), forbids=(LIED_FOR_HER,)),
        c("[Let her say it plainly.]", "truth", requires=(TRUTH_FOR_CHADALI,), forbids=(LIED_FOR_HER, PROTECTION_REQUESTED))),
    _public_e("promise", '''"You asked for the floor, Commander." {n}She looks at the Lexicon, then at you. The quill remains still.{/n}''',
        c('[Lie] "The Lexicon warns against an azata\'s essence. It would spoil the mixture."', "lie_response", flags=(LIE_SPOKEN,)),
        c('"I will not claim the Lexicon forbids it. The book says no such thing."', "withdraw_response", flags=(LIE_WITHDRAWN,))),
    nar("lie_response", '''{n}Alichino adjusts his spectacles. "Which passage? I should hate to reject a perfectly usable sample on hearsay."
Chadali leans away from the cauldron. "Oh! Then we mustn't use mine. We wouldn't want to spoil all that hard work!"
Eritrice waits for a passage that is not there. At last she writes: "Claim unsupported." Her claws nearly pierce the scroll.{/n}''',
        c("[Hear the ruling.]", "lie_ruling")),
    _public_e("lie_ruling", '''"There is no such passage." {n}She keeps her eyes on the record.{/n} "I asked you to make that claim. Minute that too."
{n}Chadali's smile fades. Eritrice draws the scroll back from her claws.{/n} "We still need Elysium. Chadali, the chair has not answered for you."''',
        c("[Return to the debate.]")),
    _public_e("withdraw_response", '''{n}Eritrice lets out the breath she was holding.{/n} "Withdrawn."
{n}Chadali looks from the book to the cauldron. "So we do still need Elysium? Oh, I wish there were another way."{/n}
"So do I." {n}Eritrice writes beneath her private request.{/n} "The Commander withdrew the false claim. At least that line can go into the minutes unchanged."''',
        c("[Return to the debate.]")),
    _public_e("protect", '''"I move that Chadali be excused from extraction, and that Elysium's sample be sought elsewhere." {n}Eritrice lays down the quill.{/n}
{n}Alichino folds his hands. "And who will fetch it? Our industrious mortal, I presume."
Chadali looks hopefully at you. "You found Nirvana's essence! Couldn't you find some more? Then nobody would need to be poked."{/n}
"I am asking for a vote, Chadali. Not another wish. All those in favor?" {n}Eritrice raises her hand. Chadali hesitates; no other hand rises. Eritrice lowers hers slowly. Her claws score the table.{/n} "Not carried. The chair's objection is to be entered in full."''',
        c("[Let her enter the result.]", "protect_record", flags=(PROTECTION_SPOKEN,))),
    _public_e("protect_record", '''"Moved by Eritrice. Not carried." {n}She writes it and sands the line.{/n} "There. I have not asked for Chadali's answer to be written in my hand."''',
        c("[Return to the debate.]")),
    _public_e("truth", '''"I do not want Chadali hurt." {n}The quill lies flat beside her hand.{/n} "No, I have no passage from the Lexicon to support that. It is my preference. Put my name beside it."
{n}Alichino's smile thins. "A sentiment contributes no sample."{/n}
"I did not offer it as one."
{n}Chadali reaches across the table and touches Eritrice's sleeve. "Oh, kitty cat. I don't want anyone hurt! Maybe {name} will find another sample. Things have worked out so wonderfully so far!"{/n}''',
        c("[Let her record her words.]", "truth_record", flags=(TRUTH_SPOKEN,))),
    _public_e("truth_record", '''{n}She writes in her own upright hand.{/n} "Eritrice stated her preference. No exemption was voted." {n}Her ears flatten.{/n} "The question of Elysium remains before the Council."''',
        c("[Return to the debate.]")),
    ], requires=("trickster", K + "a_lie_for_the_chair"),
    forbids=(CLOSED, LOST, PUBLIC, "council.walked_out", "eritrice.essence_given"),
    last=5, delay=0, optional=True, Relationship="eritrice", Chapters=[5],
    RequiresAnyGroups=[[LIED_FOR_HER, PROTECTION_REQUESTED, TRUTH_FOR_CHADALI]],
    AnswerLists=[FINAL_LIST], Remote=False, ReturnToList=True,
    ReturnText="{n}Eritrice takes up the minutes. The debate resumes.{/n}")]

# Pending drafts and the intimate morning are truthful in the currently exported
# route too. Append paragraph slots; do not shift any existing consequence.
EPILOGUE_PARAGRAPHS.extend([
    (TRUTH_FOR_CHADALI, "{n}Eritrice drafted a plain statement about Chadali for the Council. Her private record kept the draft separate from the public minutes. It was never entered there as spoken.{/n}", dict(forbids=(TRUTH_SPOKEN,))),
    (PROTECTION_REQUESTED, "{n}Eritrice drafted an objection to Chadali's extraction. No public ruling followed it. She filed the draft among her private papers, without an aye beside it.{/n}", dict(forbids=(PROTECTION_SPOKEN,))),
    (K + "twice_nightly_carried", "{n}The next morning Eritrice retrieved the fallen scroll and set it flat beneath the inkwell. On a fresh page she entered: \"A second private session. Carried.\" She read it to the Commander while gathering the scattered clothing, and purred through the last word.{/n}"),
])

PUBLIC_EPILOGUE_PARAGRAPHS = [
    (LIE_SPOKEN, "{n}The Council's record contained an unsupported claim about Elysium's essence. Beneath it, in Eritrice's hand: \"The chair requested this falsehood.\" She never struck out either line.{/n}"),
    (LIE_WITHDRAWN, "{n}The Commander withdrew the lie before the Council. Eritrice recorded the withdrawal beside her own request, and kept both. She could read that page without being proud of it.{/n}"),
    (TRUTH_SPOKEN, "{n}At the Council's sitting on planar essences, Eritrice stated that she did not want Chadali hurt. She recorded that preference under her own name. It carried no vote and concealed no lie.{/n}"),
    (PROTECTION_SPOKEN, "{n}Eritrice moved that Chadali be excused and Elysium's sample found elsewhere. The motion did not carry. She kept it in the minutes under her own name, with the result beside it.{/n}"),
]


def integrate_public(payload):
    """Coordinator hook after E14b append placement, before engine guard passes."""
    import copy
    from story_format import p
    payload["Scenes"].extend(copy.deepcopy(PUBLIC_SCENES))
    page = next(s for s in payload["Scenes"] if s["Id"] == "eritrice.trickster.epilogue.we_did_meet")["Nodes"][0]
    for flag, text in PUBLIC_EPILOGUE_PARAGRAPHS:
        page.setdefault("Paragraphs", []).append(p(text, requires=(flag,)))

# ROUND 2 AUTHORED: all three approaches meet at one performed hearing.
from storylines.eritrice_minutes import EXTRACTED
from storylines.eritrice_trickster import CAUGHT
HEARING = K + "expulsion_hearing"
PENDING = K + "expulsion_pending"
for _s in SCENES:
    if _s["Id"] in (EVE, K + "a_lie_for_the_chair"):
        _s["Forbids"].extend((EXTRACTED, "council.debrief_motion", "council.walked_out", "eritrice.essence_given"))
    if _s["Id"] == EXPEL:
        _by = {x["Id"]: x for x in _s["Nodes"]}
        for _node, _intent in (("trick", "withdrawal_planned"), ("argue", "defense_planned"), ("recuse", "recusal_planned")):
            _by[_node]["Choices"][0]["Set"] = [K + _intent]
        _by["trick"]["Text"] = '"Then give him a reason he can sign. No secret price binding this chair." {n}She lays the censure beside his submission.{/n} "He wants a place in the Crossroads before it exists. Offer a hearing, Commander. If you offer my approval, I shall contradict you in front of him."'
        _by["argue"]["Text"] = '"Answer my censure. It is true. Then answer his claim that the Worldwound is too small a concern for this table." {n}She pins both papers to the agenda.{/n} "I will testify to my own invitation. I will not pretend it appointed you chair."'
        _by["recuse"]["Text"] = '"Correct. I can yield the chair without yielding my voice as a member." {n}She writes the request beside the motion.{/n} "Cobblehoof must accept the sitting first. No vote has been taken."'
    if _s["Id"] == K + "the_motion_to_expel_voted":
        _s["Requires"].append(HEARING)
        _by = {x["Id"]: x for x in _s["Nodes"]}
        _by["start"]["Choices"].append(c("Continue", "pending", requires=(PENDING,)))
        _s["RequiresAnyGroups"][0].append(PENDING)
        _by["handled"]["Text"] = '"His signed withdrawal is here. A hearing for his profit proposal, if the Crossroads is built. No approval promised." {n}She taps his signature.{/n} "He tried to buy a vote. He came away with the right to argue. That is the whole agreement. My censure stays in the record."'
        _by["argued"]["Text"] = '"Your answer to the censure is entered beside it. So is my testimony: I chose the private invitation. You did not acquire my obedience." {n}She closes the agenda.{/n} "Alichino still presses his motion. It stands deferred while the Worldwound is our business. Your case was heard; no victory has been minuted."'
        _by["recused"]["Text"] = '"Cobblehoof took the chair. He deferred the motion. I spoke as a member, and I made no claim that fondness cancels procedure." {n}She draws the scroll back.{/n} "You heard my objection to expelling you. That remains mine, whichever chair eventually calls the vote."'
        _s["Nodes"].append(e("pending", '"No withdrawal, no judgment. The motion remains pending." {n}She rolls the unanswered submission into the agenda.{/n} "I will not report a bargain you declined as a victory."', c("[Leave the item pending.]")))

sitting(HEARING, "The devil's objection", '"Call the hearing on Alichino\'s motion."', [
    nar("open", '{n}Alichino has come to defend the objection he sent in writing. His notebook lies beside Eritrice\'s public scroll; beyond them are the crusade\'s casualty lists. Cobblehoof waits at the other end of the table.{/n}', c("[Hear the charge.]", "charge")),
    nar("charge", '{n}Alichino reads the censure aloud. "The mortal declares a private acclamation unanimous. The chair then grants a private audience. Admirable impartiality!" He marks the two dates with a fingernail.{/n}', c("[Let Eritrice answer for herself.]", "witness")),
    e("witness", '"Those are my words. I censured the unauthorized chair. I also chose the invitation. The dates prove both; they do not prove that my vote belongs to the Commander." {n}Her quill stops over the public record.{/n} "Now hear the answer."',
      c('"Withdraw it. You will have a hearing for a profit proposal if we build the Crossroads."', "offer", requires=(K + "withdrawal_planned",)),
      c('"I acted without appointment. Your chair admitted debate. The Worldwound is here, and our soldiers are dying."', "defense", requires=(K + "defense_planned",)),
      c('"Cobblehoof, will you take the chair for this motion?"', "recusal", requires=(K + "recusal_planned",)),
      c("[Leave the motion pending.]", "unfinished")),
    nar("offer", '{n}Alichino smiles. "A hearing is worth very little without a guaranteed result. I should prefer approval." Eritrice draws a line under the word in his notebook.{/n}\n"No member may sell the forum\'s future vote," {n}she says. The devil changes the wording: "A guaranteed hearing. No approval promised."{/n}',
      c('"That wording. Read the censure with it."', "signed"),
      c('"Then leave your motion pending."', "unfinished")),
    nar("signed", '{n}Alichino reads the censure once more, taking his time. Then he signs: "Motion withdrawn in exchange for a hearing, should the Crossroads be established." He keeps the counter-proposal. Eritrice keeps his withdrawal.{/n}\n"I shall bring a most profitable argument," {n}he says. Eritrice sands the signature without smiling.{/n}',
      c("[Let her enter the withdrawal.]", flags=(K + "alichino_handled",))),
    nar("defense", '{n}Alichino taps the casualty list. "Precisely. A mortal emergency dressed as universal business." Eritrice turns the scroll toward him.{/n}\n"The Wound connects planes. Its victims are not a defect in the motion. The Commander has answered the censure without asking me to erase it."\n{n}The devil refuses withdrawal. Eritrice enters both arguments and defers the disputed motion while the Council attends to the Wound.{/n}',
      c("[Accept that the case remains disputed.]", flags=(K + "argued_own_case",))),
    nar("recusal", '{n}Cobblehoof snorts, then takes the head of the table. Eritrice moves to a member\'s seat, bringing the censure with her. Alichino opens his notebook again.{/n}\n"We have the Wound to consider," {n}Cobblehoof says. "Expelling our mortal can wait."{/n}\n"Enter the deferral," {n}Eritrice says. "And my dissent from the motion. I recused myself from the chair, not from this Council."{/n}',
      c("[Let the acting chair adjourn the hearing.]", flags=(K + "chair_recused",))),
    e("unfinished", '"The motion remains pending. No agreement has been reached." {n}She keeps the censure on the table.{/n} "My invitation remains mine. Alichino may dispute that too, if he has more ink to waste."',
      c("[Return to the war business.]", flags=(PENDING,))),
], requires=(EXPEL,), forbids=(HEARING, "council.debrief_motion", "council.walked_out"), delay=0)

# Resolve the aid promise at an existing open opportunity; it creates no supplies.
sitting(K + "aid_heard", "The army's motion", '"The first item: aid for the army."', [
    nar("open", '{n}Eritrice reads the army\'s motion before the Council\'s other business. Alichino offers another profitable proposal instead of provisions. Cobblehoof shuts his purse.{/n}', c("[Hear the ruling.]", "ruling")),
    e("ruling", '"No aid granted. The chair votes for the motion; the chair cannot turn that vote into food." {n}She enters the refusal beneath the casualty figures.{/n} "I promised a hearing. Here is its result. It stays in the minutes."', c("[Take the answer back to the army.]")),
], requires=(K + "aid_first",), forbids=(K + "aid_heard", K + "aid_cancelled", "council.debrief_motion", "council.walked_out"), delay=0)
SCENES.append(scene(K + "aid_cancelled", "Unfinished business", "Eritrice", 5, "", [
    e("cancelled", '"The Council no longer offers another sitting for your army\'s motion. No aid was granted. I have marked the pending hearing cancelled, not carried."\n{n}Her letter encloses the unchanged request, with its casualty figures.{/n}', c("[File the unanswered request.]")),
], requires=("trickster.ever", K + "aid_first"), forbids=(CLOSED, K + "aid_heard", K + "aid_cancelled"),
    RequiresAnyGroups=[["council.debrief_motion", "council.walked_out", "council.fought", "council.fought_nocta_allied"]],
    Remote=True, Relationship="eritrice", last=5))

for _s in SCENES:
    if _s["Id"] == TWICE:
        _carried = next(x for x in _s["Nodes"] if x["Id"] == "carried")
        # S2: user's fill process supplies the return to an established lover.
        _carried["Choices"][0]["Next"] = TWICE + ".explicit.1"
        _s["Nodes"].append(nar(TWICE + ".explicit.1",
            '{n}Her gown falls across the abandoned scroll. She brings you down with her, still kissing; the candle has gone out before either of you reaches the table. The fallen scroll waits beneath the table until morning.{/n}', c("[...]")))

sitting(K + "second_morning", "Worth the ink", '"You promised another record."', [
    e("morning", '{n}She retrieves the scroll from under Alichino\'s chair, then your shirt. Her gown is tied crookedly; she catches you looking and pulls you into a brief, hungry kiss.{/n}\n"I did. A second private session. Carried."\n{n}She writes the line on a fresh sheet and reads it aloud while fastening your collar.{/n} "I have a sitting to chair. Tonight I intend to come back. Leave the lamp where it is."', c("[Help her gather the scattered clothing.]")),
], requires=(K + "twice_nightly_carried",), forbids=(K + "second_morning",), delay=6)

for _s in SCENES:
    if _s["Id"] == ELDEST:
        _both = next(x for x in _s["Nodes"] if x["Id"] == "both")
        _both["Text"] += '\n"You promised another exercise. Here it is: two meanings in one remark. Neither cancels the other. Now give me an objection. I still cannot read the cipher."'
    if _s["Id"] == K + "so_many_years":
        _s["Nodes"][0]["Text"] += '\n"Socothbenoth\'s departure tells me that his purposes and mine were not the same. It does not tell me every reason he had. Any promise to investigate remains open; I will not invent its answer."'
    if _s["Id"] == JEALOUS:
        for _name in ("nothing", "like"):
            next(x for x in _s["Nodes"] if x["Id"] == _name)["Text"] += '\n{n}She takes your face between her hands and kisses you hard, then draws back, breathing through her nose. Her claws stay sheathed.{/n} "There. My wish, not a ruling."'

# ERI-02: her question is answered from the conduct this hearing actually recorded.
_hearing = next(x for x in SCENES if x["Id"] == HEARING)
for _n in _hearing["Nodes"]:
    if _n["Id"] in ("signed", "defense", "recusal", "unfinished"):
        _n["Choices"][0]["Next"] = "personal"
_hearing["Nodes"].extend([
    e("personal", '"You let him read the censure in full. You could have tried to make my invitation an excuse to hide it. Why?" {n}She rolls the public record closed.{/n} "Answer for what you did here, Commander. I can read the rest."',
      c('"I tried to cheat your vote before. That is already in the record. I want your judgment this time."', "caught_answer", requires=(CAUGHT,)),
      c('"I asked you to yield the chair. I still wanted you to speak for yourself."', "recused_answer", requires=(K + "chair_recused",), forbids=(CAUGHT,)),
      c('"Your invitation was yours. It did not erase my censure."', "plain_answer", forbids=(CAUGHT, K + "chair_recused"))),
    e("caught_answer", '"Yes. I remember the false acclamation. Today you heard my testimony without putting another aye in my mouth." {n}She sets the public scroll beside Alichino\'s submission.{/n} "That is the distinction I shall keep. Now my private invitation can remain private."', c("[Leave her judgment intact.]")),
    e("recused_answer", '"I disliked yielding it. You heard that too." {n}She takes her own chair again.{/n} "I spoke as a member. It was my decision. Alichino may put the dates in his notebook; he cannot put words in my mouth."', c("[Leave her to the next item.]")),
    e("plain_answer", '"Correct. The chair may want you and still censure you." {n}She pulls a blank sheet from beneath the public minutes.{/n} "The devil has his record. Mine has room for another question. I shall ask it when I am ready."', c("[Let her choose the time.]")),
])

# The native event can close an unplayed public intervention; no draft becomes a rescue.
SCENES.append(scene(K + "protection_cancelled", "The unspoken objection", "Eritrice", 5, "", [
    e("cancelled", '"The opportunity to raise Chadali\'s contribution has passed. My private request was not spoken before the Council. I have marked it cancelled."\n{n}The enclosed draft has a ruled line through its proposed hearing date; the words remain legible.{/n} "Do not write that we won an exemption. There was no such vote."', c("[Keep the cancelled draft with its date.]")),
], requires=("trickster.ever", K + "a_lie_for_the_chair"),
    RequiresAnyGroups=[[LIED_FOR_HER, PROTECTION_REQUESTED, TRUTH_FOR_CHADALI],
        [EXTRACTED, "council.debrief_motion", "council.walked_out", "council.fought", "council.fought_nocta_allied"]],
    forbids=(CLOSED, PUBLIC, K + "protection_cancelled", LIE_SPOKEN, LIE_WITHDRAWN, TRUTH_SPOKEN, PROTECTION_SPOKEN),
    Remote=True, Relationship="eritrice", last=5))

# Mandatory extraction also closes the staged interjection before its shared hook is enabled.
for _s in PUBLIC_SCENES:
    _s["Forbids"].extend((EXTRACTED, "council.debrief_motion"))

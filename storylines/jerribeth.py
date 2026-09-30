"""Jerribeth draft: explicitly invited magical correspondence, not restored native encounters."""
from story_format import c, n, scene

RELATIONSHIP = dict(
    Title="The guest who knocked",
    Description="Jerribeth has offered a private means of correspondence. For once, she has asked before entering somebody's thoughts. I suspect she expects to be admired for it.",
    Objective="Consider Jerribeth's invitation",
    Guidance="After meeting Jerribeth, look for her invitation during a quiet rest in Drezen or at the Nexus. Meetings use an explicitly invited magical projection. Her native life, allegiances, and victims are not rewritten by accepting it.",
    StartedFlag="jerribeth.started", ClosedFlag="jerribeth.closed", CommittedFlag="jerribeth.committed",
    UnavailableFlags=["jerribeth.unavailable"], FailureFlags=[],
)
SCENES = []


def s(id, title, nodes, requires=(), forbids=(), delay=24, chapter=3, optional=False, **extra):
    for page in nodes:
        if not page["Portrait"]:
            page["Portrait"] = "Jerribeth"
    SCENES.append(scene("jerribeth." + id, title, "Jerribeth", chapter, "", nodes,
                        Relationship="jerribeth", Remote=True, Chapters=[ch for ch in (3, 4, 5) if ch >= chapter],
                        Areas=["2570015799edf594daf2f076f2f975d8", "7847c3e3537104f4694167af0b9fcd0e"],
                        requires=requires, forbids=forbids, delay=delay, optional=optional, **extra))


s("invitation", "A message that waits", [
    n("start", "Narrator", '''{n}Among the messages waiting for you is a small lacquered frame wrapped in paper. Where a portrait should be, a dark surface reflects nothing. A note lies against it.{/n}
{n}The handwriting is fine and rather impatient: I have acquired a correspondence charm. You attend to this side; I attend to the other. It conveys a chosen image and spoken thoughts, not everything either of us would prefer to keep private. Turn it over to end the conversation. Even mortals should be capable of that.{/n}
{n}Below the instructions is a name: Jerribeth.{/n}''',
      c('[Examine the charm, then deliberately invite a conversation.]', "voice"),
      c('[Leave it wrapped until you choose to consider it.]', abort=True),
      c('[Reject the invitation.]', "reject")),
    n("voice", "Jerribeth", '''{n}A narrow, insectile silhouette appears inside the frame. The voice that reaches your thoughts is familiar, high and lightly buzzing.{/n}
"At last. I began to suspect you were waiting for somebody to explain whether accepting a letter was a heroic act."
{n}One delicate hand lifts inside the image.{/n}
"Try the cloth if you like. I would rather you knew the door works. A captive audience fidgets, and I do not waste my evenings on fidgeting."''',
      c('[Turn the frame over, wait, then invite her again.]', "test"),
      c('"Why seek my company?"', "why")),
    n("test", "Jerribeth", '''{n}The image and voice cease. When you turn the charm back and invite her again, Jerribeth is waiting with her hands linked together.{/n}
"Satisfied? Good. I have provided a useful device and endured an inspection. You might now reward me by being interesting."''', c('"Why seek my company?"', "why", flags=("jerribeth.tested_channel",))),
    n("why", "Jerribeth", '''"Because you have a talent for changing arrangements that other people consider permanent. Because I would like to know what you want before somebody else learns how to offer it."
{n}The outline of an antenna trembles.{/n}
"And because I have been wondering whether you are as difficult to entertain as you are to predict. That part is personal."''',
      c('"Then entertain me. I will decide whether to invite you back."', "return", flags=("jerribeth.challenge",)),
      c('"I am interested in you. Begin there."', "return", flags=("jerribeth.direct",))),
    n("return", "Jerribeth", '''"A little patience. I have spent this evening demonstrating a piece of furniture. I refuse to let that become your account of my hospitality."
{n}Her voice lowers, still inside your thoughts.{/n}
"Another evening. Bring one question you would not ask with an audience. I shall do the same."''', c('[Agree to another conversation.]', flags=("jerribeth.invited",))),
    n("reject", "Narrator", '''{n}You return the charm without opening a connection. Whatever Jerribeth hoped to learn, she will have to learn elsewhere.{/n}''', c('[Decline further private invitations.]', flags=("jerribeth.closed",))),
], requires=("jerribeth.met",), delay=0)

s("question", "What the audience never hears", [
    n("start", "Jerribeth", '''{n}Jerribeth answers the invitation in her own form. The charm preserves the fine movements of her hands more clearly than the shadows of her face.{/n}
"You remembered. How flattering. Or how inconvenient for whatever worthy pursuit you have neglected."
{n}A chittering note of amusement accompanies the words.{/n}
"My question first. Would you rather be admired for what you are, or desired for something you could become?"''',
      c('"I would rather know which person someone is looking at when they desire me."', "known", flags=("jerribeth.wants_recognition",)),
      c('"There are pleasures in being able to surprise someone who thought they knew me."', "surprise", flags=("jerribeth.wants_surprise",))),
    n("known", "Jerribeth", '''"How demanding. Most people are delighted to be mistaken for somebody magnificent."
{n}She studies you, or the image of you the charm permits her to see.{/n}
"You would deprive an admirer of half the work and then complain that they had not understood the remainder. I begin to see the attraction."''', c('"And what would you prefer?"', "answer")),
    n("surprise", "Jerribeth", '''"Yes. Especially the instant before they decide whether they approve."
{n}Her hands separate in a small, pleased gesture.{/n}
"You know that instant. I thought you might. There is an audience that spends it reaching for a weapon, but one must not let poor taste dictate every performance."''', c('"And when there is no audience to deceive?"', "answer")),
    n("answer", "Jerribeth", '''{n}For several moments she does not answer.{/n}
"I dislike being predictable. I dislike it more when someone is right about me."
{n}Her voice takes on an airy lightness.{/n}
"You may consider that a confidence. I have not decided whether you deserve a second one."''',
      c('"I would like to see the face you choose when you are trying to please me."', "next", flags=("jerribeth.asked_guise",)),
      c('"You need not become something else to hold my attention."', "next", flags=("jerribeth.asked_true_form",))),
    n("next", "Jerribeth", '''"Wouldn't that be a curious experience. Trying to please one person who knew it was being done deliberately."
{n}Her amusement returns, but she does not dismiss the thought.{/n}
"I shall consider an appropriate setting. The frame is capable of more than displaying my hands."''', c('[Look forward to her next invitation.]', flags=("jerribeth.attracted",))),
], requires=("jerribeth.invitation",))

s("guise", "A room with visible seams", [
    n("start", "Jerribeth", '''{n}The frame shows a furnished room, bright with reflected lamplight. Jerribeth waits within it. A slim elven figure stands where her insectile shape appeared before, but a deliberate shimmer along the edges reveals the projection.{/n}
"A setting for a conversation. You remain exactly where you are; I remain where I am. I thought I should mention that before you tried to rescue the furniture from a demon."
{n}The elven image smiles.{/n}
"The face is also deliberate. Does knowing spoil it?"''',
      c('"No. A costume can be beautiful when I know who is wearing it."', "guise", flags=("jerribeth.chosen_guise",)),
      c('"I would rather look at you in your own form."', "true", flags=("jerribeth.chosen_true_form",))),
    n("guise", "Jerribeth", '''"Then I shall keep it for tonight."
{n}The image moves closer without pretending to cross the boundary of the frame.{/n}
"Tell me what you find beautiful. Be specific. I have heard enough praise addressed to a pair of pointed ears."''',
      c('"The expression of someone enjoying being watched."', "seen"),
      c('"The care you took after pretending this would be effortless."', "seen")),
    n("true", "Jerribeth", '''{n}The elven outline falls away. In its place, Jerribeth's narrow head tilts toward you. Light catches the edges of her wings.{/n}
"If you tell me that appearances do not matter, I shall be offended. This one has taken me considerably longer to acquire."
{n}The delicate movements of her hands remain the same as they were beneath the illusion.{/n}''',
      c('"They matter. I like seeing which small movements belong to you."', "seen"),
      c('"You are watching for my reaction. I enjoy knowing I can unsettle you too."', "seen")),
    n("seen", "Jerribeth", '''{n}Her answer arrives as a soft, amused vibration.{/n}
"So attentive. I could grow accustomed to being examined with that much care."
{n}The room beyond her shifts slightly. For a moment the illusion has a corner that does not meet its wall. She corrects it, then notices that you noticed.{/n}
"You have distracted me. I trust you are pleased with yourself."''',
      c('"Very. I would like to do it again."', "end"),
      c('"Leave the seam. I would rather keep your attention."', "end", flags=("jerribeth.kept_seam",))),
    n("end", "Jerribeth", '''"Another evening, then. I will see whether I can distract you as successfully."
{n}She lets the room dissolve before she ends the connection. Her own silhouette remains for a moment in the dark frame, as though she has thought of one more thing to say and decided to save it.{/n}''', c('[Invite her again another evening.]', flags=("jerribeth.courting",))),
], requires=("jerribeth.question",))

s("price", "The question she hoped to postpone", [
    n("start", "Jerribeth", '''"You have been preparing a serious question. I can tell by the way you wait for me to stop enjoying myself."
{n}Jerribeth folds her hands in the image.{/n}
"Ask it. I make no promise that the answer will improve the evening."''',
      c('"What happened in Wintersun was more than a clever performance."', "wintersun", requires=("jerribeth.wintersun_known",)),
      c('"Why should I trust the interest you show me?"', "trust")),
    n("wintersun", "Jerribeth", '''"Of course it was. An illusion that changes nothing is decoration."
{n}There is pride in the answer, and impatience with what she expects you to say next.{/n}
"The people believed they understood their world. They loved and fought and made their choices inside it. I supplied the part they would have found inconvenient to question."''',
      c('"You made them kill people they would otherwise have welcomed. I will not admire that."', "refuse", flags=("jerribeth.condemned_wintersun",)),
      c('"I understand the appeal. Plant nothing in me. Whatever happens between us will be my own bad idea."', "limit", flags=("jerribeth.claimed_limit",))),
    n("trust", "Jerribeth", '''"You shouldn't trust every part of it. I enjoy power. I enjoy discovering where somebody keeps a weakness. I have made those preferences remarkably clear."
{n}Her antennae incline toward the image of you.{/n}
"But I have also returned to a conversation I cannot force you to continue. You might ask why I keep doing that."''',
      c('"Because an answer you chose for me would tell you nothing about what I want."', "limit", flags=("jerribeth.claimed_limit",)),
      c('"You keep what interests you. On a needle, usually. Tell me what stops you doing that to me."', "refuse", flags=("jerribeth.asked_possession",))),
    n("refuse", "Jerribeth", '''{n}The silence lasts long enough for the projected room to fade at its edges.{/n}
"You want a confession. You will not get one. I would only perform it, and you would know, and then we should both be bored."
{n}Her next words are colder.{/n}
"I will sell you something instead. Your head stays yours. The charm shows what you invite, and nothing else. In exchange, you keep inviting me. Stop, and the terms lapse, and you have seen what I do in Wintersun when I have nothing better to amuse me. Do not mistake any of this for a sudden discovery that I have spent my life being wicked."''',
      c('"Then keep that agreement. I will judge what you do next."', "terms"),
      c('"That is not enough for me to continue this."', "end")),
    n("limit", "Jerribeth", '''"Possession is so much less trouble. It is why everyone in the Abyss prefers it."
{n}She says it as though restraint were an expensive indulgence she has decided, this once, to charge to somebody else's account.{/n}
"Very well. Terms. Your head stays yours, and I will not use you as a door into anyone else's. That is what I give. What I receive: you keep answering. If you want a miracle that turns me into somebody you can introduce at a feast without an explanation, find another demon."''', c('"Keep the terms. Speeches are cheap."', "terms")),
    n("terms", "Jerribeth", '''"A demon and a crusader with terms and no witnesses. The Abyss would laugh. I intend to laugh first."
{n}Some of the chill leaves her voice.{/n}
"Will you invite me again? Answer before you invent a noble reason for it. I dislike noble reasons. They are always renegotiated."''', c('"Yes. I still want to see you."', flags=("jerribeth.terms",))),
    n("end", "Jerribeth", '''"Then close the frame."
{n}She watches you without the courtesy of a farewell. The charm falls silent when you turn it over, exactly as promised.{/n}''', c('[End the private relationship.]', flags=("jerribeth.closed",))),
], requires=("jerribeth.guise",))

s("evening", "An invitation without witnesses", [
    n("start", "Jerribeth", '''{n}There is no grand room inside the frame tonight. Jerribeth has chosen a close circle of lamplight and a background of darkness.{/n}
"I considered arranging something magnificent. Then I remembered how pleased you were when I stopped attending to the walls."
{n}Her voice seems quieter, though it still reaches you through the charm.{/n}
"I would like your attention for a while. The part you do not distribute to supplicants."''',
      c('"You have it."', "want"),
      c('"I have other lovers. I will not make you a promise of exclusivity."', "others")),
    n("others", "Jerribeth", '''"Good. Otherwise I should have had to find out how you were lying."
{n}An amused chitter brushes the words.{/n}
"I am not buying all of you, Commander. Only tonight. I have never once cared who else has handled a thing I mean to have for an evening. It is the evening I collect."''', c('"Then this evening is yours."', "want", flags=("jerribeth.open_terms",))),
    n("want", "Jerribeth", '''"Tell me what you wanted when you opened the frame. You have been quite brave about my answers. I should like to see how you manage your own."
{n}She waits. For once, she does not supply an interpretation for you.{/n}''',
      c('"I wanted to hear that you had been waiting for me."', "waiting"),
      c('"I wanted to see what you do when you stop performing. And I wanted you to know I was watching."', "private"),
      c('"I want your company. Let us go slowly."', "slow")),
    n("waiting", "Jerribeth", '''"I was."
{n}The answer comes too quickly for her to make it sound like a concession.{/n}
"I had prepared a less flattering description of how I spent the hour. You have made it inconvenient to use."''', c('"Then let us make the waiting worth it."', "private")),
    n("private", "Jerribeth", '''{n}Jerribeth draws the projected light close, leaving the rest of the image in shadow.{/n}
"My own form, or the face I made for you? I would like to hear you choose."''',
      c('"Your own form. I want to see you."', "private_true"),
      c('"The elven guise, tonight. I know who is wearing it."', "private_guise")),
    n("private_true", "Jerribeth", '''{n}She lets you see the small movements of her antennae and the way her hands become still when she listens closely.{/n}
"You have become quiet. Have I disappointed you?"
{n}The question has an edge. She is accustomed to recognizing fear, and dislikes having to ask what she is seeing instead.{/n}''',
      c('"I was watching you forget to perform. I like it."', "close"),
      c('"No. I am trying to find a way to say that I want you closer without spoiling this."', "close")),
    n("private_guise", "Jerribeth", '''{n}The elven image returns, with the same deliberate shimmer at its edges. Its expression changes as Jerribeth discovers how closely you are watching.{/n}
"I know what people usually want from this face. You make me less certain. It is becoming a rather distracting habit."
{n}The image leans nearer, then stops at the edge of the frame.{/n}
"I would like to kiss you. How inconvenient that I sent furniture."''',
      c('"The woman behind the face is the one I want closer."', "close"),
      c('"Then stay with me tonight, and we can be dissatisfied with the furniture together."', "close"), portrait="Jerribeth-Guise"),
    n("close", "Jerribeth", '''{n}The image gives way to darkness, but her voice remains, closer than the frame should allow.{/n}
"I have been wanted before. By cultists, mostly, who wanted whatever I could make them see. It is a cheap thing to be wanted for, and they paid cheap prices."
{n}A low, amused vibration follows.{/n}
"You keep asking for the thing that makes the pictures. I have not decided whether that is flattery or a threat to my business. Say it again, and I will decide."''',
      c('"I want you, Jerribeth. I would like you to remember hearing me say it."', "late"),
      c('"I have been waiting all evening to hear you admit it. Stay."', "late")),
    n("late", "Jerribeth", '''"I remember everything, Commander. It is my worst habit and my best stock in trade."
{n}She stays. There is no image to admire now, and neither of you asks for one. She asks you questions she already knows the answers to, only to hear how you answer them, and she laughs, high and abrasive, each time you notice.{/n}
{n}When you finally part, she names the evening she wants next, and the hour, as though it were already entered in a book and only your signature was missing.{/n}''', c('[Choose another evening together.]', flags=("jerribeth.lovers", "jerribeth.private_evening"))),
    n("slow", "Jerribeth", '''"Then I shall have to be good company. You do enjoy setting difficult tasks."
{n}She tells you about a patron who commissioned an illusion of his own victory and objected because the defeated rival looked insufficiently devastated. By the third revision, the rival's grief had become so elaborate that nobody noticed the victor at all.{/n}
{n}Her delight in the story is infectious. When the conversation ends, she informs you that she had been saving it, and that you now owe her one of equal quality.{/n}''', c('[Ask her to save another story.]', flags=("jerribeth.lovers", "jerribeth.slow_evening"))),
], requires=("jerribeth.price",))

s("commission", "An audience of one", [
    n("start", "Jerribeth", '''{n}The frame opens on an unfinished illusion. Several painted-looking doors hang in darkness, each with a different landscape beyond it.{/n}
"A commission. My client wants to be pursued through a place where every escape leads somewhere worse. The pursuers and the danger are inventions. The client's taste is, regrettably, genuine."
{n}Jerribeth makes one of the doors vanish.{/n}
"I have solved the terror. It is the ending that refuses to behave."''',
      c('"What did the client ask to feel when it was over?"', "ask"),
      c('"Let them escape somewhere unexpectedly beautiful."', "beauty")),
    n("ask", "Jerribeth", '''"Triumphant. Exhausted. Desperate to try it again. The usual modest ambitions."
{n}A door opens on an extravagant throne room. She dismisses it almost immediately.{/n}
"I could praise them until they became insufferable. I would prefer to be paid before that happens."''', c('"Give them a moment they did not know they wanted."', "beauty")),
    n("beauty", "Jerribeth", '''{n}The doors disappear. Beyond the last one is a quiet terrace under a sky that has never existed. Jerribeth adjusts the light, then leaves a narrow seam visible along the horizon.{/n}
"They will complain that it looks unfinished."
{n}She watches the image for a moment.{/n}
"I find I don't care. I may keep this ending for somebody with better taste."''',
      c('"I would like to see it with you."', "keep"),
      c('"Do not fix the seam on my account."', "keep", requires=("jerribeth.kept_seam",))),
    n("keep", "Jerribeth", '''"Then look. There is no pursuer, no audience waiting to discover whether you are brave, and nothing you need to conquer before the light changes."
{n}She joins her image to the terrace and lets the illusion remain still.{/n}
"You may tell me it is beautiful. I will make a reasonable effort not to become insufferable."''', c('"It is beautiful. Stay there with me a little longer."', flags=("jerribeth.shared_work",))),
], requires=("jerribeth.evening",))

s("patron", "A name offered carefully", [
    n("start", "Jerribeth", '''"You should understand something about the people who appreciate my work. Appreciation is not a promise that they will continue to find its creator useful."
{n}Jerribeth's projected hands are still.{/n}
"Vellexia understands entertainments that would exhaust a lesser imagination. Her curiosity is also capable of exhausting the people expected to satisfy it. If you seek her attention, prepare to keep earning it."''',
      c('"Would you help me understand her?"', "introduce", flags=("vellexia.introduced",)),
      c('"Are you warning me about her, or asking me to watch out for you?"', "personal")),
    n("introduce", "Jerribeth", '''"I will tell you what I know. It will not make her safe."
{n}Her voice sharpens.{/n}
"Do not confuse a refined manner with restraint. Do not assume that yesterday's delight will please her tomorrow. And do not arrive believing that somebody has already arranged her answer to you."
{n}After a pause, she adds:{/n}
"I have arranged no such thing."''', c('"I understand. Tell me what you want from this."', "personal")),
    n("personal", "Jerribeth", '''"I would like you alive. I would like not to have made a foolish investment in somebody who mistakes a warning for an invitation to boast."
{n}She appears to consider leaving it there.{/n}
"And I would dislike ending these conversations because you had become somebody else's diverting catastrophe."''',
      c('"Then keep telling me when you see danger. I will do the same."', "end"),
      c('"You could have said that you would miss me."', "end")),
    n("end", "Jerribeth", '''"I would dislike losing an investment this far along. You may take that as tenderly as you like; I shall deny it in any company."
{n}The irritation in her voice is almost affectionate.{/n}
"Now listen carefully. I am going to tell you something useful, and I expect you to remember it when being foolish would make a better story."''', c('[Listen to her warning.]', flags=("jerribeth.warned",))),
], requires=("jerribeth.commission", "jerribeth.refuge_known"), forbids=("jerribeth.patron_lost",), chapter=4, optional=True)

s("collection", "The amusement she remembers", [
    n("start", "Jerribeth", '''"You are looking at me as though you have remembered something unpleasant."
{n}Her projected hands draw together.{/n}
"Xanthir, perhaps. I wondered when you would bring him into one of our evenings."''',
      c('"I saw how much you enjoyed tormenting him."', "answer"),
      c('"Does everyone who interests you eventually become a specimen?"', "answer")),
    n("answer", "Jerribeth", '''"He took my chambers and my authority, and expected me to be grateful for what remained. He was also an extraordinary creature. I found a way to satisfy more than one interest."
{n}There is no apology in the answer.{/n}
"You saw it yourself. I would prefer you not to discover it anew whenever we have had a pleasant evening."''',
      c('"A pleasant evening does not make me forget it. I am asking what keeps this from ending the same way."', "difference"),
      c('"I will not spend my evenings making excuses for what you did to him."', "leave")),
    n("difference", "Jerribeth", '''{n}Her antennae incline, then hold still.{/n}
"Nothing keeps it from ending the same way, except that it would bore me. Xanthir on a pin said only what I arranged for him to say. I heard every word of it before he did."
{n}Her next words come more slowly, priced one at a time.{/n}
"You say things I did not arrange. I have not yet found a needle that would keep that. When I find one, I shall tell you, and you may decide whether to run."''',
      c('"Then never ask me to admire what you did to him."', "end", flags=("jerribeth.remembered_cruelty", "jerribeth.judges_actions")),
      c('"You have found something more difficult to collect. I intend to keep it that way."', "end", flags=("jerribeth.remembered_cruelty", "jerribeth.contests_possession"))),
    n("end", "Jerribeth", '''"I had hoped for an easier conversation tonight."
{n}She considers the frame, then remains within it.{/n}
"I am still here. You may decide what to make of that without my assistance."''', c('[Continue the evening without pretending the argument settled everything.]')),
    n("leave", "Jerribeth", '''"Then don't."
{n}For a moment you hear only the faint hum of the charm.{/n}
"I will not tell you that you have misunderstood me. I think you understand quite enough."''', c('[Close the private relationship.]', flags=("jerribeth.closed",))),
], requires=("jerribeth.price", "jerribeth.xanthir_known"), optional=True)

s("refuge", "The house she left behind", [
    n("start", "Jerribeth", '''{n}Jerribeth answers from an image of bare darkness. She has made no effort to hide her irritation.{/n}
"Vellexia's protection has become a story people tell when deciding how much danger I am worth."
{n}Her voice buzzes harshly.{/n}
"I left the manor. I am looking for another patron. You may spare me an expression of surprise that losing a powerful protector is inconvenient."''',
      c('"What do you need from me?"', "need"),
      c('"Are you angry with me?"', "anger")),
    n("anger", "Jerribeth", '''"Among other things. I am capable of more than one thought, even when every thought is unpleasant."
{n}She moves one hand away from the other, making herself uncurl it.{/n}
"I chose refuge among dangerous people. I knew what could happen. That does not oblige me to enjoy discovering which possibility has occurred."''', c('"Then tell me what you need now."', "need")),
    n("need", "Jerribeth", '''"Names. Introductions, if you have them. Information I can use without discovering that it has been sold to somebody else first."
{n}She stops, and does the sum in front of you.{/n}
"And an evening with the one creature in two planes who is not working out what I am worth tonight. I find that refreshing. I am also deeply suspicious of it."''',
      c('"I can offer the conversation tonight. We can consider the rest carefully."', "stay"),
      c('"I will listen. I will not pretend to have a safe patron waiting for you."', "stay")),
    n("stay", "Jerribeth", '''"Good. I have had enough reassuring inventions for one day."
{n}She begins with the practical problems, grows angry again in the middle of an explanation, and allows you to hear it without correcting herself into a more attractive performance.{/n}
{n}Before you part, she admits that she opened her side of the charm before the agreed hour.{/n}
"I thought you might be there," she says. "You may be pleased about that after I have gone."''', c('[Arrange another conversation.]', flags=("jerribeth.refuge_acknowledged",))),
], requires=("jerribeth.evening", "jerribeth.refuge_known", "jerribeth.patron_lost"), chapter=4, optional=True)

s("future", "A future she has not rehearsed", [
    n("future_entry", "Jerribeth", '''"You wanted to speak about what happens after this war."
{n}She puts aside the scenery before turning her whole attention to the frame.{/n}''',
      c('"We have made time for the work and what followed it. I want to keep making that time."', "start", requires=("jerribeth.settlement_kept",)),
      c('"We have not had those longer evenings. I still want this courtship to continue."', "short_future", requires=("jerribeth.short_future_requested",), forbids=("jerribeth.settlement_kept",))),
    n("short_future", "Jerribeth", '''"Then continue it. Invite me when you can, and come when I ask. I do not ask twice; I send something that asks for me."
{n}Her hands remain loosely linked.{/n}
"There are things I want badly enough to be unpleasant about. You have not seen them yet. You will, and I am curious whether you will still be at the frame afterwards."
{n}A small vibration of amusement enters her voice.{/n}
"An evening at a time, then. I have made worse bargains than that, all of them with princes."''',
      c('"I want those evenings. Keep expecting me."', "short_end", flags=("jerribeth.committed", "jerribeth.short_future_chosen")),
      c('"I cannot make that promise."', "part")),
    n("short_end", "Jerribeth", '''"I will. I have acquired an inconvenient preference for your answers."
{n}The imperfect horizon returns behind her. It is something you have already made together, with room still left beyond it.{/n}
"Come back when you can. You may yet discover what I have been trying to show you."''', c('[Keep the shorter courtship open.]', flags=("jerribeth.chosen_future", "jerribeth.future_settled"))),
    n("start", "Jerribeth", '''{n}Jerribeth answers without preparing a setting. The frame holds only her own form and the darkness around it.{/n}
"An arrangement like this ends so easily. A missed invitation. A changed allegiance. A crusader who decides, one morning, that a demon's voice in the evenings would look very bad before an inquisitor."
{n}Her antennae move once, then settle.{/n}
"I served Lord Baphomet for exactly as long as it benefited me more than it cost me. I am told that is a vice. I call it bookkeeping. So: what does this pay, and for how long?"''',
      c('"I want this to continue. More evenings, and more of me in them. That is the offer."', "promise"),
      c('"Fate may object. As a Trickster, I would enjoy proving it wrong."', "fate", requires=("trickster",)),
      c('"I cannot promise you a future together."', "part")),
    n("fate", "Jerribeth", '''"Find a loophole large enough for two, then. I refuse to spend eternity applauding you from the wrong side of a closed door."
{n}Her amusement is bright and eager.{/n}
"I would enjoy helping. Imagine the indignity of being an inevitable ending and discovering that somebody has read the smaller print."
{n}She pauses.{/n}
"Tell me before you sign anything on my behalf. I prefer to choose which impossible arrangements I enter."''', c('"Then we will examine the arrangement together."', "promise", flags=("jerribeth.fate_terms",))),
    n("promise", "Jerribeth", '''"Then here is what I want, since you so rarely ask. More than evenings. When I decide how much more, you will discover the price, and you will pay it, because by then you will already have had the goods."
{n}A faint vibration of amusement returns.{/n}
"This is the part where a mortal says that the other matters. I will not say it. I will tell you that I turned away two commissions this month to keep the frame free on your evenings, and that I do not turn away money. Draw your own conclusion. I already have."''',
      c('"You matter to me. Write that into whatever you are drafting, and read it as closely as you like."', "end", flags=("jerribeth.committed",)),
      c('"I want you in my life. Needles, small print and all."', "end", flags=("jerribeth.committed",))),
    n("end", "Jerribeth", '''{n}She lets the answer stand without testing it, which for her is a considerable concession, and then tests it anyway.{/n}
"I shall hold you to every word. You should know that I have kept a copy. Tomorrow, then. If the world is still ending, it can spare us another conversation."
{n}Before the image fades, the seam of the invented horizon appears behind her. She has kept it.{/n}''', c('[Keep the next evening for her.]', "future_conclusion", flags=("jerribeth.chosen_future",))),
    n("future_conclusion", "Jerribeth", '''"I shall expect you."
{n}She leaves the frame open until you are ready to put it down.{/n}''',
      c('[Keep the promise with the work and evenings you have shared.]', flags=("jerribeth.developed_future", "jerribeth.future_settled"), requires=("jerribeth.settlement_kept",)),
      c('[Keep the earlier promise, with the longer visits still ahead.]', flags=("jerribeth.short_future_chosen", "jerribeth.future_settled"), forbids=("jerribeth.settlement_kept",))),
    n("part", "Jerribeth", '''"Then I am glad I asked."
{n}Her voice is perfectly controlled. She has made an effort to achieve that.{/n}
"Keep the frame or destroy it. I shall no longer attend to the other side."''', c('[End the relationship.]', flags=("jerribeth.closed",))),
], requires=("jerribeth.commission",), chapter=5,
   RequiresAny=["jerribeth.settlement_kept", "jerribeth.short_future_requested"])

s("ordinary", "A performance she abandoned", [
    n("start", "Jerribeth", '''{n}Jerribeth has prepared three different backgrounds and appears to dislike all of them. One vanishes as soon as you open the connection.{/n}
"I have been working. You have arrived at a moment when I am no longer capable of being impressed by myself."
{n}A second background dissolves.{/n}
"It will pass. In the meantime, you may find me unusually tolerable."''',
      c('"Show me the part you are pleased with."', "work"),
      c('"I asked you for something I could admire. Show me what you made."', "work", requires=("jerribeth.judges_actions",)),
      c('"I have decided you may enjoy my company without adding me to a collection."', "contest", requires=("jerribeth.contests_possession",)),
      c('"You need not perform for me tonight."', "rest")),
    n("contest", "Jerribeth", '''"How generous. I shall endeavor to resist labeling the frame."
{n}Her amusement sharpens, then softens into something less practiced.{/n}
"I remember the argument. I also remember that you came back after it. You need not keep proving that you could have left."''', c('"Then enjoy the fact that I am here."', "rest")),
    n("work", "Jerribeth", '''{n}She shows you a bird made of shifting light. Its wings move incorrectly, then beautifully, then incorrectly again.{/n}
"It should be impossible and convincing. At present it is merely irritating."
{n}When you point out the moment that worked, she makes it happen again. Her pleasure in being understood lasts longer than the illusion.{/n}''', c('"Keep that version. Leave the rest until tomorrow."', "rest")),
    n("rest", "Jerribeth", '''"An evening without improving anything. How extravagant."
{n}The backgrounds disappear. Her own form remains, and she settles into the conversation without turning it into a spectacle.{/n}
"Tell me something you have not said to anybody else today. It need not be useful."''',
      c('"I wanted to see you like this, without wondering how much was meant to impress me."', "known", requires=("jerribeth.wants_recognition",)),
      c('"I did not expect to enjoy discovering what you are like when you stop trying to surprise me."', "surprise", requires=("jerribeth.wants_surprise",)),
      c('"I was looking forward to this conversation."', "end")),
    n("known", "Jerribeth", '''"Most of it usually is. I have chosen an exacting audience."
{n}A faint chitter accompanies the admission.{/n}
"Tonight you may have the part that has run out of good ideas."''', c('"That is the part I asked for."', "end")),
    n("surprise", "Jerribeth", '''"Then I have managed it again by accident. How economical."
{n}She lets the joke rest without trying to improve it.{/n}''', c('[Stay with her.]', "end")),
    n("end", "Jerribeth", '''{n}The conversation wanders. At one point she forgets to keep the imagined lamplight steady, and you discover that neither of you particularly minds.{/n}
"Come again tomorrow," she says at last. "I might still be short of good ideas."''', c('[Keep another evening for her.]', flags=("jerribeth.at_ease",))),
], requires=("jerribeth.future", "jerribeth.committed"), chapter=5)

s("farewell", "The frame she leaves open", [
    n("start", "Jerribeth", '''{n}The charm answers almost immediately. Jerribeth appears without a prepared setting.{/n}
"I know. There are important things you must do, and this may be our last convenient opportunity to say something foolish."
{n}Her hands are linked tightly together.{/n}
"I would prefer you to survive. I find I have become rather particular about whose attention I want."''',
      c('"Keep an evening for me. I intend to return."', "return"),
      c('"Tell me what you would like when I do."', "want")),
    n("want", "Jerribeth", '''"An account of what happened. The interesting version first, and then the one you have edited to make yourself sound less frightened."
{n}Her voice softens into a low vibration.{/n}
"And another evening on that terrace. I have not found a better audience for an imperfect horizon."''', c('"Then keep it for us."', "return")),
    n("return", "Jerribeth", '''"I will."
{n}For once, she does not attach a clever qualification.{/n}
"When you return, invite me. I will know what you mean."
{n}She waits for you to end the connection. Her own side remains open until you do.{/n}''', c('[Carry the promise into what comes next.]', flags=("jerribeth.farewell_kept",))),
], requires=("jerribeth.ordinary", "jerribeth.future_settled"), chapter=5,
   RequiresAny=["jerribeth.developed_future", "jerribeth.short_farewell_requested"])

s("parting", "A connection you may close", [
    n("start", "Jerribeth", '''"You have something to say. I would prefer to hear it before I begin inventing possibilities."''',
      c('"I want to end the relationship."', "end"),
      c('"I want to make more time for you."', "stay")),
    n("end", "Jerribeth", '''{n}Her hands remain still.{/n}
"Then I will stop waiting for your invitations."
{n}There is anger in her voice, but she does not disguise it as a threat.{/n}
"I dislike the answer. I prefer having heard it to discovering that the charm had become a piece of furniture you no longer remembered owning."''', c('[End the relationship.]', flags=("jerribeth.closed",))),
    n("stay", "Jerribeth", '''"Then choose an evening. I have an excellent imagination, but it does not benefit from doing all our arrangements by itself."''', c('[Arrange another meeting and keep the relationship.]', abort=True)),
], requires=("jerribeth.lovers",), optional=True, ManualOnly=True)


def ending(id, text, requires=(), forbids=(), owner="Epilogue"):
    nodes = [n("start", "Narrator", text, c(), portrait="Jerribeth")]
    if id in ("together", "ascended"):
        nodes[0]["Choices"][0]["Next"] = "settlement"
        nodes[0]["Choices"][0]["Requires"] = ["jerribeth.developed_future"]
        nodes[0]["Choices"].append(c(forbids=("jerribeth.developed_future",)))
        nodes.insert(0, n("history", "Narrator", "{n}The correspondence charm had carried a promise beyond the war.{/n}",
            c('[Remember the life begun through it.]', "start", requires=("jerribeth.developed_future",)),
            c('[Remember the promise and the invitations still unanswered.]', "earlier", forbids=("jerribeth.developed_future",)), portrait="Jerribeth"))
        nodes.extend([
            n("earlier", "Narrator", '''{n}The promise was real, though much of the life it invited remained to be discovered. Jerribeth still wanted another evening, and made no attempt to disguise her impatience when arranging one became difficult.{/n}
{n}She kept working on her illusions, and kept an account, in a hand nobody else could read, of every evening the Commander had promised and every evening the Commander had come. She never said what she meant to do with the difference. She enjoyed not saying.{/n}''', c(), portrait="Jerribeth"),
            n("settlement", "Narrator", "{n}The room Jerribeth wanted had begun with a bargain whose costs neither of them could forget.{/n}",
                c('[Remember the account and the inspection.]', "account", requires=("jerribeth.counter_public_account",)),
                c('[Remember the catalogue and its clients.]', "catalogue", requires=("jerribeth.counter_private_archive",), forbids=("jerribeth.counter_public_account",)), portrait="Jerribeth"),
            n("account", "Narrator", '''{n}Vardess's signed account had made some invitations harder to obtain. When an inspector looked beneath Jerribeth's own scenery, the Commander had seen what it cost her to let another person describe the work.{/n}
{n}Hessa had taken the report to her employer. Jerribeth could argue with its judgment and refuse a commission; she could not make the stopped image something the inspector had never seen. She remembered that irritation whenever somebody asked her to put another promise in writing.{/n}''', c('Continue', "room"), portrait="Jerribeth"),
            n("catalogue", "Narrator", '''{n}The catalogue had bought introductions, and left Vardess the means to finish his concealed recorder. A new client had soon asked Jerribeth for the same advantage. The Commander remembered the bargaining that followed, including what she wanted badly enough to resent losing.{/n}
{n}Useful names remained useful. She had begun judging their owners with a more exact knowledge of what a fee could cost her, and occasionally enjoyed explaining that knowledge to someone who had expected her to be grateful.{/n}''', c('Continue', "room"), portrait="Jerribeth"),
            n("room", "Narrator", '''{n}Serit's finished section carried his name. Further work required further payment. Jerribeth found this deeply irritating whenever ambition ran ahead of her means, and found her chosen correspondent an excellent person to complain to.{/n}
{n}Their charm remained a means of speaking, not a passage between worlds. Even so, the unfinished city acquired streets she wanted to show one particular visitor. She kept making room for an answer she could not supply herself.{/n}''', c(), portrait="Jerribeth"),
        ])
    SCENES.append(scene("jerribeth.ending_" + id, "The guest who knocked", owner, 5, "", nodes,
                        Relationship="jerribeth", last=99, requires=requires, forbids=forbids))


ending("together", '''{n}Jerribeth remained a difficult person to describe to anyone who expected the Commander to keep reassuring company. She did little to make the explanation easier.{/n}
{n}The private conversations continued. Sometimes she arrived with an elaborate illusion, sometimes with an ugly truth she had considered withholding. She kept the visible seam in one impossible horizon, and returned to it with the person who had watched her create it.{/n}''', requires=("jerribeth.committed",), forbids=("jerribeth.closed", "jerribeth.unavailable", "ascended"))
ending("ascended", '''{n}Jerribeth found several advantages to knowing a god personally, and admitted to most of them. The advantage she discussed least was still being able to ask for an evening and receive an answer meant for her alone.{/n}
{n}Her entertainments remained inventive. Her private invitations became simpler. It pleased her more than she expected when magnificence proved unnecessary.{/n}''', requires=("jerribeth.committed", "ascended"), forbids=("jerribeth.closed", "jerribeth.unavailable"))
ending("apart", '''{n}The charm eventually ceased to show anything but its own dark surface. Jerribeth had other patrons to cultivate and other arrangements to consider.{/n}
{n}Once, while preparing an illusion, she left a narrow seam along a painted horizon. When somebody asked whether it was intentional, she gave an answer sharp enough to discourage a second question.{/n}''', requires=("jerribeth.lovers", "jerribeth.closed"), forbids=("jerribeth.unavailable",))
ending("unfinished", '''{n}For a time, Jerribeth continued to attend to the far side of the correspondence charm. The invitations grew less frequent, and eventually she stopped arranging her evenings around the possibility of one.{/n}
{n}She never quite decided whether the unfinished conversation irritated her more than a disappointing answer would have done.{/n}''', requires=("jerribeth.attracted",), forbids=("jerribeth.committed", "jerribeth.closed", "jerribeth.unavailable"))
ending("aeon", '''{n}The history that might have joined Jerribeth and the Commander had no place in the world's new account of itself. Somewhere in the Abyss, an illusion acquired a narrow seam along its horizon.{/n}
{n}Whether its creator remembered an audience, or merely imagined one, she left the imperfection where it was.{/n}''', requires=("jerribeth.committed",), forbids=("jerribeth.closed",), owner="AeonEpilogue")

"""Authored book-event incidents, not changes to native Alushinyrra quests."""
from story_format import c, n, scene

SCENES = []
NEXUS = "7847c3e3537104f4694167af0b9fcd0e"


def s(id, title, nodes, requires):
    for node in nodes:
        node["Portrait"] = "Seelah"
    SCENES.append(scene("seelah." + id, title, "Seelah", 4, "", nodes,
                        Relationship="seelah", Remote=True, Areas=[NEXUS],
                        Chapters=[4], last=4, requires=requires, forbids=("inhuman",), delay=24, optional=True))


s("letter", "An audience for cruelty", [
    n("start", "Seelah", '''{n}Seelah finds you at the Nexus with a strip of red cloth wound around her wrist.{/n}
"I'm going back into the city. I said I'd meet someone by a stall with a red awning, and she gave me this because apparently there are six."
{n}She unwinds the cloth.{/n}
"A copyist. Her employer sold a bundle of her papers when she left his service. There was a letter in it that she wants back. She asked for someone to stand beside her while she asks for it."
{n}Seelah looks toward the way out.{/n}
"I'd like you with me."''',
      c('[Accompany her.]', "stall"),
      c('[Explain that you cannot go now.]', abort=True)),
    n("stall", "Narrator", '''{n}The awning is the color of the cloth. Beneath it, a performer entertains a small crowd by reading letters in exaggerated voices. The copyist, a tiefling woman with ink ground into the creases of her fingers, waits at the edge.{/n}
{n}"He has my sister's letter," she says. "The one with the blue thread. Please don't tell him it's mine."{/n}
{n}Seelah nods. Beneath the counter, a brazier spits sparks as the performer drops a discarded page into it. He takes up a folded sheet with a blue thread hanging from it and begins a plaintive imitation of a woman asking whether her sister has enough to eat.{/n}
{n}A laugh goes through the crowd. Seelah moves forward. The copyist catches her sleeve, but Seelah has already opened her mouth.{/n}''',
      c('[Step beside Seelah and demand that the reading stop.]', "direct"),
      c('[Draw the audience away with a performance of your own, risking what he does with the unwanted page.]', "divert")),
    n("direct", "Narrator", '''{n}Your interruption cuts through the laughter. Seelah plants herself in front of the stall.{/n}
{n}"Put it down." She speaks quietly enough that the nearest spectators stop talking to hear.{/n}
{n}The performer looks from her sword to you. He drops the page on the counter and steps back, spreading empty hands with an injured expression.{/n}
{n}"Such an important letter. Who could it belong to?"{/n}
{n}The copyist reaches between you to take it. A spectator recognizes her from another stall and calls out her trade. Others turn to look. She folds the letter without checking it and walks away so quickly that Seelah has to hurry to catch up.{/n}''',
      c('[Follow them out of the crowd.]', "public", flags=("seelah.letter_public",))),
    n("divert", "Narrator", '''{n}You catch Seelah's eye and address the spectators with the solemn importance of a herald announcing a war. Your subject is the disgraceful quality of the performer's awning. It sags. It fades. Its tassels have deserted their posts.{/n}
{n}Seelah stares at you. Then she follows your glance to the copyist and moves beside the woman instead of the counter.{/n}
{n}The copyist points toward the counter. Seelah helps her slip along the edge of the crowd as a spectator shouts a suggestion about punishing the tassels. Before they can reach the stall, the performer tries to resume reading, loses his place, and reaches for a more promising sheet. He crumples the sister's letter and throws it into the brazier.{/n}
{n}The copyist makes a small sound. Seelah starts toward the fire, but flame has already climbed the dry paper. She stops when the woman catches her sleeve again.{/n}
{n}"Leave it. Please."{/n}''',
      c('[Leave with them while the audience is distracted.]', "burned", flags=("seelah.letter_burned",))),
    n("public", "Seelah", '''{n}In a narrow passage away from the stall, the copyist finally opens the letter. It is intact.{/n}
"We got it," Seelah says.
{n}"Yes," the woman answers. "And tomorrow they can ask whether my sister thinks I'm starving. At every stall where I look for work."{/n}
{n}Seelah's hand falls from the woman's shoulder.{/n}
"I thought if we stopped him quickly..."
{n}"I wanted that too. I just wish I didn't have to go back there tomorrow."{/n}
{n}She puts the letter inside her coat. Before leaving, she thanks you for returning it. She keeps one hand pressed against the fold as she walks away.{/n}''', c('[Give her room to leave.]', "return")),
    n("burned", "Seelah", '''{n}You stop in a narrow passage away from the stall. Seelah still has one hand closed around the strip of red cloth.{/n}
"I'm sorry. I thought we could reach it while he was looking at you."
{n}The copyist shakes her head. "He didn't get to the end. That matters."{/n}
{n}She looks down at her empty hands.{/n}
{n}"My sister draws a little house beside her name. Every time. As if I could forget where she lives."{/n}
{n}Seelah offers her the cloth. The woman takes it absently, winds it around her fingers, and leaves before either of you can find something else to say.{/n}''', c('[Let her go.]', "return")),
    n("return", "Seelah", '''{n}Back at the Nexus, Seelah unbuckles her sword belt and lays it down with unnecessary care.{/n}
"I thought standing beside her would be the easy part."
{n}You begin to answer. She raises a hand, then lowers it again.{/n}
"No. Sorry. I do want to hear you. Just not while I'm still trying to make the afternoon come out differently."
{n}She looks at you directly.{/n}
"Tomorrow. Will you let me be angry tonight without deciding I've stopped wanting you here?"''',
      c('"Yes. We will talk tomorrow."', flags=("seelah.letter_unsettled",))),
], requires=("seelah.abyss_together",))


s("letter_after", "What we meant to do", [
    n("start", "Seelah", '''{n}Seelah comes to find you. She has brought neither an apology disguised as a joke nor something for you to eat.{/n}
"I've been rehearsing this conversation. In every version I get to sound more sensible than I was yesterday."
{n}She sits on a low stone, leaving the conversation between you instead of trying to fold you into an embrace.{/n}
"I heard someone laughing at a hungry woman, and I stopped looking at the woman standing beside me."''',
      c('"I thought stopping him was worth the attention it would draw."', "public", requires=("seelah.letter_public",)),
      c('"I did not expect anyone to recognize her. I was trying to get the letter back."', "public", requires=("seelah.letter_public",)),
      c('"We kept her identity out of his performance. We still lost something she wanted."', "burned", requires=("seelah.letter_burned",))),
    n("public", "Seelah", '''"I thought I knew what getting it back would cost. A threat, perhaps an argument. Then we could leave. She was the one who had to go back."
{n}She rubs her palms together, impatient with herself.{/n}
"I am glad she has the letter. I'm not going to pretend that doesn't count. But I keep remembering how pleased I was when he stepped back. Before I looked at her."
{n}Her eyes meet yours.{/n}
"Did you see her sooner than I did?"''',
      c('"No. I was watching him too."', "admit"),
      c('"I saw her hesitate. I thought she would be grateful afterward."', "assumed")),
    n("burned", "Seelah", '''"Yes. And I nearly made you stop before I understood what you were doing."
{n}She gives a short, unhappy laugh.{/n}
"You were insulting an awning. I was furious with you for about three heartbeats."
{n}She looks down at the stone beneath her hands.{/n}
"I wish we'd got the letter. I also know he might have read the rest while we were trying to be cleverer. I can't find a version that lets me be pleased with everything."''',
      c('"We should have agreed on a signal before we went in."', "signal"),
      c('"I need you to give me time to act, even when my plan looks foolish."', "trust")),
    n("admit", "Seelah", '''"Then next time one of us watches the person we're there for. Even when the other is making a very satisfying speech."
{n}Her mouth twists.{/n}
"Especially then."
{n}She does not look relieved. But she has stopped searching your face for an answer that will make her feel better.{/n}''', c('[Agree to check with each other.]', "end", flags=("seelah.check_person",))),
    n("assumed", "Seelah", '''"That sounds ugly when you say it. I've done it too."
{n}She takes a moment before continuing.{/n}
"I want us to catch it before somebody has to explain the harm we didn't bother to notice. Even if it means interrupting each other in front of people."
{n}She looks at you without softening the request.{/n}
"I won't enjoy that. I'm asking anyway."''', c('[Agree to let her interrupt, and to do the same for her.]', "end", flags=("seelah.check_person",))),
    n("signal", "Seelah", '''"Something better than looking at me while I am already marching past you."
{n}She offers her wrist.{/n}
"Here. Two taps. I stop and look. It won't solve the whole city, but I might hear the next sentence someone says to me."
{n}You try the signal. She holds still, deliberately, until you finish.{/n}''', c('[Agree on the signal.]', "end", flags=("seelah.check_signal",))),
    n("trust", "Seelah", '''"Give me something to recognize. I can trust you and still misunderstand you."
{n}She holds out her wrist.{/n}
"Two taps when we can reach each other. Say my name when we can't. I'll look before I start arguing."
{n}A trace of humor returns.{/n}
"I am making no promises about what happens after I look."''', c('[Agree on the signal.]', "end", flags=("seelah.check_signal",))),
    n("end", "Seelah", '''{n}For a while neither of you speaks. Then Seelah shifts closer on the stone.{/n}
"I don't want to get good at leaving these conversations unfinished. Yesterday needed a night. It didn't need a week."
{n}She rests her hand beside yours, close enough to invite an answer.{/n}
"Will you walk with me? Just here. I have had quite enough of awnings for now."''',
      c('[Take her hand and walk beside her.]', flags=("seelah.letter_discussed",)),
      c('[Walk beside her, still thinking over the conversation.]', flags=("seelah.letter_discussed",))),
], requires=("seelah.letter_unsettled",))


s("letter_work", "The price she names", [
    n("start", "Seelah", '''{n}Seelah has news of the copyist. She found her again while passing through the city, bent over a page outside a shop that sells ink.{/n}
"She wants someone to walk with her to a prospective customer. Carry the samples, look respectable, and keep quiet. She was very particular about that last part."
{n}Seelah gives you a rueful look.{/n}
"I said I could manage two of those without practice."''',
      c('[Go with her to meet the copyist.]', "meeting"),
      c('[Tell her you cannot come this time.]', abort=True)),
    n("meeting", "Narrator", '''{n}The copyist has wrapped her samples in a scrap of oilcloth. She hands the bundle to Seelah but keeps one page to check for smudges.{/n}
{n}"You came," she says, looking at you. "Good. I have enough to think about without watching both ends of every alley."{/n}''',
      c('"How have things been since the stall?"', "public", requires=("seelah.letter_public",)),
      c('"How have things been since the stall?"', "burned", requires=("seelah.letter_burned",))),
    n("public", "Narrator", '''{n}"Two people asked about my sister. One thought it was funny. I didn't get much work from him anyway."{/n}
{n}She rubs at a spot on the oilcloth.{/n}
{n}"I read the letter again last night. Properly, this time. I am glad I can do that."{/n}
{n}Seelah nods, but does not offer the answer she seems to have prepared. The copyist points toward a narrow street.{/n}
{n}"Come on. If we're late, she'll charge me for waiting."{/n}''', c('[Follow her.]', "customer")),
    n("burned", "Narrator", '''{n}"No one has said anything. I think we managed that much."{/n}
{n}She folds the edge of the oilcloth inward.{/n}
{n}"I wrote down the parts I remembered. There was a bit about a neighbor's dog that I can't get right. My sister made it sound as though she was trying very hard not to laugh."{/n}
{n}Seelah starts to speak, then lets the pause remain.{/n}
{n}"I still have work to do," the copyist says. "It helps. This way."{/n}''', c('[Follow her.]', "customer")),
    n("customer", "Narrator", '''{n}The customer receives you in a cramped room lined with narrow drawers. She is a tiefling with a silver ring on each horn and a habit of tapping her nails while other people speak.{/n}
{n}She examines the samples, pauses over a line, and turns the page toward the copyist.{/n}
{n}"You missed a letter here. I'll pay half."{/n}
{n}"I'll correct the sample. The price for the finished pages stays the same."{/n}
{n}"Does it? I hear you need work."{/n}
{n}Seelah draws breath. Beside her, the copyist reaches for the faulty sample. Her hand is steady.{/n}''',
      c('[Tap Seelah\'s wrist twice, as agreed.]', "signal_used", requires=("seelah.check_signal",)),
      c('"Seelah. Look at her."', "person_seen", requires=("seelah.check_person",)),
      c('[Keep quiet and let Seelah decide whether to intervene.]', "her_choice")),
    n("signal_used", "Seelah", '''{n}Seelah turns toward you. For an instant she looks annoyed. Then she closes her mouth and watches the copyist take a pen from her sleeve.{/n}
{n}She shifts the samples to her other arm, freeing the wrist you touched. Her hand brushes yours once before she lets it fall.{/n}''', c('[Wait for the copyist to answer.]', "bargain", flags=("seelah.signal_used",))),
    n("person_seen", "Seelah", '''{n}Seelah looks at you first. You glance toward the copyist, who has taken a pen from her sleeve without asking either of you for help.{/n}
{n}Seelah shifts her weight back onto both feet. When the customer looks toward her, she holds out the remaining samples instead of answering for their owner.{/n}''', c('[Let the copyist negotiate.]', "bargain", flags=("seelah.person_seen",))),
    n("her_choice", "Seelah", '''{n}"There is more work here," Seelah begins, lifting the bundle. "You can see..."{/n}
{n}The copyist holds out her hand without turning. Seelah stops. After a moment, she puts the bundle into it.{/n}
{n}The customer drums her nails on the table. The copyist waits until she finishes.{/n}''', c('[Wait beside Seelah.]', "bargain", flags=("seelah.stopped_herself",))),
    n("bargain", "Narrator", '''{n}"Here is the correction," the copyist says. "And here is the price. If you want cheaper work, I won't keep you."{/n}
{n}She places the repaired page on the table. The customer studies it longer than the change requires.{/n}
{n}"Six pages. You'll bring them tomorrow."{/n}
{n}"At the price I named."{/n}
{n}The customer's nails stop moving. At last she nods.{/n}
{n}Outside, Seelah helps the copyist wrap the samples in their oilcloth again.{/n}
{n}"Six pages aren't a living. But they're six pages." She looks at the two of you. "Thank you for carrying them."{/n}
{n}She leaves you at the next turning. This time she is already thinking about her work when she goes.{/n}''', c('[Walk back with Seelah.]', "return")),
    n("return", "Seelah", '''"I was going to tell that woman exactly what I thought of her offer."
{n}Seelah watches the copyist disappear into the street.{/n}
"She probably knew. I have been told I am very easy to read when somebody is being a bastard."
{n}She turns back to you.{/n}
"It would have been a good speech."''',
      c('"Save it. I am sure the city will give you another opportunity."', "tease"),
      c('"I liked watching you decide what to do with it."', "warm")),
    n("tease", "Seelah", '''"I'll polish it on the way back. You can tell me where to put the swearing."
{n}Her laugh comes more easily than it did during your last conversation. She takes your arm, then stops short at a turning and draws you out of the way of a passing cart.{/n}
"There. I remain extremely useful company."''', c('[Continue the walk with her.]', flags=("seelah.copyist_followed",))),
    n("warm", "Seelah", '''{n}She studies your face, suspicious of praise that arrives too neatly. Then she smiles.{/n}
"I liked having you there. Even when I didn't particularly like what I needed to hear."
{n}She reaches for your hand.{/n}
"Don't expect me to admit that every time. You'd become impossible."''', c('[Walk beside her.]', flags=("seelah.copyist_followed",))),
], requires=("seelah.letter_discussed",))

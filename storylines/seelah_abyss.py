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
{n}She puts the letter inside her coat. Before leaving, she thanks you for returning it. She keeps one hand pressed against the fold as she walks away.{/n}''', c('[Watch her go.]', "return")),
    n("burned", "Seelah", '''{n}You stop in a narrow passage away from the stall. Seelah still has one hand closed around the strip of red cloth.{/n}
"I'm sorry. I thought we could reach it while he was looking at you."
{n}The copyist shakes her head. "He didn't get to the end. That matters."{/n}
{n}She looks down at her empty hands.{/n}
{n}"My sister draws a little house beside her name. Every time. As if I could forget where she lives."{/n}
{n}Seelah offers her the cloth. The woman takes it absently, winds it around her fingers, and leaves before either of you can find something else to say.{/n}''', c('[Let her go.]', "return")),
    n("return", "Seelah", '''{n}Back at the Nexus, Seelah unbuckles her sword belt and lays it down with unnecessary care.{/n}
"Stand beside her. Get the letter. How did we make such a mess of that?"
{n}You begin to answer. She raises a hand, then lowers it again.{/n}
"No. Sorry. I'll listen tomorrow. Tonight I'll just argue, and you've had enough of that from me."
{n}She looks at you directly.{/n}
"Come back tomorrow, will you? I'm angry. That doesn't mean I've suddenly gone off you."''',
      c('"Yes. We will talk tomorrow."', flags=("seelah.letter_unsettled",))),
], requires=("seelah.abyss_together",))


s("letter_after", "What we meant to do", [
    n("start", "Seelah", '''{n}Seelah comes to find you empty-handed. She opens her mouth, shuts it, then plants her hands on her hips.{/n}
"I had a fine speech ready. Made me sound very wise. Pity about yesterday."
{n}She sits on a low stone and scuffs the ground with her heel.{/n}
"I was so busy wanting to knock his teeth out that I forgot to look at the woman holding my sleeve."''',
      c('"I thought stopping him was worth the attention it would draw."', "public", requires=("seelah.letter_public",)),
      c('"I did not expect anyone to recognize her. I was trying to get the letter back."', "public", requires=("seelah.letter_public",)),
      c('"He never got her name. But we lost her letter."', "burned", requires=("seelah.letter_burned",))),
    n("public", "Seelah", '''"I thought I'd scare him, she'd take the letter, and we'd be done. Except she has to go back to those stalls and ask for work. We don't."
{n}She rubs her palms together, impatient with herself.{/n}
"She has her letter. Good. I'm glad of that. But when he backed off, I thought we'd won. Then I saw her face."
{n}Her eyes meet yours.{/n}
"Did you see her sooner than I did?"''',
      c('"No. I was watching him too."', "admit"),
      c('"I saw her hesitate. I thought she would be grateful afterward."', "assumed")),
    n("burned", "Seelah", '''"Yes. And I nearly made you stop before I understood what you were doing."
{n}She gives a short, unhappy laugh.{/n}
"You were insulting an awning. I was furious with you for about three heartbeats."
{n}She looks down at the stone beneath her hands.{/n}
"Damn it, I wish we'd got the letter. But if we'd waited for a better trick, he might have read it all. Either way, she walks off clutching that scrap of cloth."''',
      c('"We should have agreed on a signal before we went in."', "signal"),
      c('"Let me finish the trick before you charge in, even if I look like a fool."', "trust")),
    n("admit", "Seelah", '''"Next time, one of us keeps an eye on whoever asked for help. The other can make the grand speech."
{n}Her mouth twists.{/n}
"And give the speech-maker a good jab if they're getting carried away."
{n}Seelah rubs a hand over her face. Her shoulders are still hunched, but she looks you in the eye again.{/n}''', c('[Agree to watch each other as well as the person you are helping.]', "end", flags=("seelah.check_person",))),
    n("assumed", "Seelah", '''"Ugh. 'She'll thank me afterward.' I've said that too."
{n}She grimaces and presses her palms against the stone.{/n}
"If I start doing that again, stop me. In front of everyone, if you have to. I'll do the same for you. Better a red face than another mess like yesterday."
{n}She points a finger at you.{/n}
"And if I grumble, remind me whose bright idea it was."''', c('[Agree to stop each other when you get carried away.]', "end", flags=("seelah.check_person",))),
    n("signal", "Seelah", '''"Something better than looking at me while I am already marching past you."
{n}She offers her wrist.{/n}
"Here. Two taps. I'll stop and look. Try it before I get my sword out, eh?"
{n}You tap her wrist twice. She turns her head toward you, eyebrows raised.{/n}''', c('[Agree on the signal.]', "end", flags=("seelah.check_signal",))),
    n("trust", "Seelah", '''"Then give me a signal! I saw you mocking an awning. I didn't see a plan."
{n}She holds out her wrist.{/n}
"Two taps when we can reach each other. Say my name when we can't. I'll look before I start arguing."
{n}A trace of humor returns.{/n}
"I am making no promises about what happens after I look."''', c('[Agree on the signal.]', "end", flags=("seelah.check_signal",))),
    n("end", "Seelah", '''{n}For a while neither of you speaks. Then Seelah shifts closer on the stone.{/n}
"There. If I'd put that off another week, I'd have worn a trench pacing around camp. One night was bad enough."
{n}She lays her hand beside yours, her little finger brushing your knuckle.{/n}
"Will you walk with me? Just here. I have had quite enough of awnings for now."''',
      c('[Take her hand and walk beside her.]', flags=("seelah.letter_discussed",)),
      c('[Walk beside her and think over what she said.]', flags=("seelah.letter_discussed",))),
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
{n}Seelah nods and tightens her grip on the samples. The copyist points toward a narrow street.{/n}
{n}"Come on. If we're late, she'll charge me for waiting."{/n}''', c('[Follow her.]', "customer")),
    n("burned", "Narrator", '''{n}"No one has said anything. I think we managed that much."{/n}
{n}She folds the edge of the oilcloth inward.{/n}
{n}"I wrote down the parts I remembered. There was a bit about a neighbor's dog that I can't get right. My sister made it sound as though she was trying very hard not to laugh."{/n}
{n}Seelah draws breath, then bites her lip.{/n}
{n}"I still have work to do," the copyist says. "It helps. This way."{/n}''', c('[Follow her.]', "customer")),
    n("customer", "Narrator", '''{n}The customer receives you in a cramped room lined with narrow drawers. She is a tiefling with a silver ring on each horn and a habit of tapping her nails while other people speak.{/n}
{n}She examines the samples, pauses over a line, and turns the page toward the copyist.{/n}
{n}"You missed a letter here. I'll pay half."{/n}
{n}"I'll correct the sample. The price for the finished pages stays the same."{/n}
{n}"Does it? I hear you need work."{/n}
{n}Seelah draws breath. Beside her, the copyist reaches for the faulty sample. Her hand is steady.{/n}''',
      c('[Tap Seelah\'s wrist twice, as agreed.]', "signal_used", requires=("seelah.check_signal",)),
      c('"Seelah. Look at her."', "person_seen", requires=("seelah.check_person",)),
      c('[Keep quiet and watch Seelah.]', "her_choice")),
    n("signal_used", "Seelah", '''{n}Seelah turns toward you. For an instant she looks annoyed. Then she closes her mouth and watches the copyist take a pen from her sleeve.{/n}
{n}She shifts the samples to her other arm, freeing the wrist you touched. Her hand brushes yours once before she lets it fall.{/n}''', c('[Wait for the copyist to answer.]', "bargain", flags=("seelah.signal_used",))),
    n("person_seen", "Seelah", '''{n}Seelah looks at you first. You glance toward the copyist. A pen is already in the woman's hand.{/n}
{n}Seelah shifts her weight back onto both feet. The customer looks toward her. Seelah holds out the remaining samples, her lips pressed together.{/n}''', c('[Let the copyist negotiate.]', "bargain", flags=("seelah.person_seen",))),
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
{n}She leaves you at the next turning, counting the six pages on her ink-stained fingers.{/n}''', c('[Walk back with Seelah.]', "return")),
    n("return", "Seelah", '''"I was going to tell that woman exactly what I thought of her offer."
{n}Seelah watches the copyist disappear into the street.{/n}
"She probably knew. I have been told I am very easy to read when somebody is being a bastard."
{n}She turns back to you.{/n}
"It would have been a good speech."''',
      c('"Save it. I am sure the city will give you another opportunity."', "tease"),
      c('"You swallowed a fine speech. I liked that."', "warm")),
    n("tease", "Seelah", '''"I'll polish it on the way back. You can tell me where to put the swearing."
{n}Her laugh comes more easily than it did during your last conversation. She takes your arm, then stops short at a turning and draws you out of the way of a passing cart.{/n}
"There. I remain extremely useful company."''', c('[Continue the walk with her.]', flags=("seelah.copyist_followed",))),
    n("warm", "Seelah", '''{n}She narrows her eyes at you, then breaks into a smile.{/n}
"I'm glad you came. Even if you did catch me about to put my foot in it again."
{n}She reaches for your hand.{/n}
"Don't expect me to admit that every time. You'd become impossible."''', c('[Walk beside her.]', flags=("seelah.copyist_followed",))),
], requires=("seelah.letter_discussed",))

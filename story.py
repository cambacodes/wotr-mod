"""Authoring source for Three at the Table. Build with python story.py.

Scene and node IDs are save references. Keep them stable when revising prose.
"""
import json
from pathlib import Path
from story_format import c, n, scene

ROOT = Path(__file__).parent
scenes = []


def s(id, title, owner, chapter, entry, nodes, requires=(), forbids=(), delay=0, last=5, optional=False):
    scenes.append(scene(id, title, owner, chapter, entry, nodes, requires, forbids, delay, last, optional))


s("a_cup", "A cup that has gone cold", "Anevia", 1,
  '"Have you had a moment to yourself, Anevia?"', [
    n("start", "Anevia", '''{n}Anevia looks at your hands before she looks at your face. No orders, no report, no object requiring an explanation. Her mouth quirks.{/n}
"Careful. Keep comin' up empty-handed and I'll start thinkin' you enjoy my company."
{n}She moves a stack of papers off the adjoining chair with one hand. The other guards a cup that long ago stopped steaming.{/n}
"Sit, if you're sittin'. Standin' over people makes the guards nervous. They think somebody's about to be promoted."''',
      c('"How is the leg?"', "leg", requires=("chapter_one",)),
      c('"I thought we could talk without discussing the crusade."', "work"),
      c('"I do enjoy your company."', "company")),
    n("leg", "Anevia", '''"Good as the other one. Been testing it on the stairs. The stairs lost."
{n}She gets up, steps lightly around the chair and returns to her seat without favoring either leg.{/n}
"The healers did their job. Now everybody else has to catch up. You should see the looks when I climb onto something."
{n}Her amusement softens as she looks at you.{/n}
"I'm glad you were there under Kenabres. But if we're going to be friends, don't make every visit a check on the woman who needed gettin' out. I've got other talents. Some of 'em are even respectable."''',
      c('"Then tell me something I haven\'t rescued you from."', "bread"),
      c('"You don\'t owe me anything."', "company")),
    n("work", "Anevia", '''"That's a nasty trick to play on a woman. Take away her occupation and expect her to make conversation."
{n}Her smile remains, but she turns the papers facedown. The gesture gives you her attention more honestly than the words.{/n}
"I know which cook waters the stew, which guards can't keep their mouths shut, who's missin' somebody and who's hopin' somebody stays missing. Ask what I've been doing, I can talk till sunrise. Ask how I am..."
{n}She lifts the cold cup.{/n}
"Well. This was hot when I poured it."''', c('"We can start with a fresh cup."', "bread")),
    n("company", "Anevia", '''{n}For a moment she seems about to return the compliment. Instead she tips her cup toward you.{/n}
"You and my wife. Very peculiar taste, the pair of you."
{n}Irabeth's name changes her face. Affection, immediate and unguarded, slips through the practiced levity.{/n}
"She'll ask if I've eaten. I'll ask if she's slept. We'll both lie, then spend ten minutes tryin' to catch each other out. That's married life in the Eagle Watch."
{n}Anevia looks back at you rather than toward the door.{/n}
"You can stay a bit. No interrogation required."''', c('"What would you do with a whole day off?"', "bread")),
    n("bread", "Anevia", '''"Bake somethin'."
{n}The answer comes so promptly that she laughs at herself.{/n}
"Don't look so impressed. I didn't say it'd be edible. I like the idea of it. You put things together, leave 'em alone awhile, and they turn into something people are glad to see. My usual line of work runs the other way."
{n}She rubs a circle in a ring of spilled tea.{/n}
"Irabeth would eat every bite. Even if it could stop an arrow. That's the trouble with asking someone who loves you whether you've made good bread."
{n}You remain together while the noise of headquarters rises and falls around the little space she has cleared. Nothing urgent happens. Anevia seems almost suspicious of how pleasant that is.{/n}''',
      c('"When you try, I\'ll give you an honest opinion."', "end"),
      c('[Flirt] "I\'d come for the company. The bread can defend itself."', "flirt")),
    n("flirt", "Anevia", '''"That sounded dangerously like a line."
{n}She gives you time to retreat from it. When you do not, her smile grows quieter.{/n}
"I'm married. Happily. You know that, don't you?"
{n}There is no rebuke in the question, but she waits for your acknowledgment before setting down her cup.{/n}
"All right. Then we know where we stand."
{n}She turns back to her papers. A moment later she moves them off your chair again, although you have not yet risen.{/n}''',
      c('"I know. Thank you for the tea."', flags=("a_interest",))),
    n("end", "Anevia", '''"An honest opinion? In headquarters? They'll throw us both out."
{n}When you rise, she catches your sleeve lightly between two fingers.{/n}
"Thanks. For askin' something I didn't have to make a report out of."
{n}She lets go before you need to answer. The chair remains empty beside her, cleared of papers.{/n}''', c('"Another time, then."')),
])

s("i_watch", "Off duty", "Irabeth", 1,
  '"Irabeth, may I speak to you as a person rather than an officer?"', [
    n("start", "Irabeth", '''{n}Irabeth straightens as you approach. You can almost see her assemble the list of matters awaiting your attention. Your question interrupts the process.{/n}
"I... yes. Of course. Is something wrong?"
{n}When you tell her that nothing is wrong, her expression becomes more uncertain. She sets aside a report with unnecessary care.{/n}
"Then I am afraid you have caught me unprepared. I had answers for several kinds of emergency."''',
      c('"Does every conversation have to be an emergency?"', "habit"),
      c('"You look tired."', "tired"),
      c('"I wanted to thank you for trusting me."', "trust")),
    n("habit", "Irabeth", '''"No. Anevia has explained this to me. More than once."
{n}A reluctant smile reveals the small tips of her tusks.{/n}
"When I have nothing to do, I remember something I have forgotten. When I have done everything I remember, I worry about what I have failed to notice. It is an efficient system for avoiding leisure."
{n}She glances toward her abandoned report, catches herself, and turns it facedown.{/n}
"There. An act of tremendous courage."''', c('"What does Anevia do when she catches you at it?"', "wife")),
    n("tired", "Irabeth", '''{n}Irabeth reaches for the familiar assurance that she is fit for duty. You watch her decide not to give it.{/n}
"I am."
{n}Her hands rest against the edge of the table. The leather at the fingers of her gloves has been repaired several times.{/n}
"There are people who need the rest more. That is what I keep telling myself. It is also what every exhausted soldier says when I order them away from their post."
{n}She exhales through her nose.{/n}
"Apparently the advice becomes less convincing when addressed to me."''', c('"Who is allowed to tell you that?"', "wife")),
    n("trust", "Irabeth", '''"You earned it. Do not let anyone tell you otherwise."
{n}She delivers the answer with the certainty that deserts her whenever she speaks about herself.{/n}
"I have seen brave people. I have seen people who were certain that they were brave. The difference is often visible only when things go wrong. You kept helping people when you had every reason to think of your own survival."
{n}She grows a little embarrassed by the force of her praise.{/n}
"I did not mean to turn this into an inspection. Old habits."''', c('"Tell me about something outside the Eagle Watch."', "wife")),
    n("wife", "Irabeth", '''"Anevia has never mistaken my rank for an argument. It is one of her more inconvenient qualities."
{n}The warmth in her voice makes the complaint absurd.{/n}
"She will steal the pen from my hand. Then she will deny having it while it is plainly visible behind her ear. I can order soldiers into a breach, but I cannot make that woman surrender a pen."
{n}Her smile fades only a little.{/n}
"She should not have to steal time from me. I know that. It is easy to give everything to a cause and imagine that the people closest to you can live on what remains."
{n}For a while she studies the patched gloves rather than your face.{/n}''',
      c('"You\'re allowed to want something for yourself."', "want"),
      c('[Flirt] "For what it\'s worth, I wanted your company too."', "flirt")),
    n("flirt", "Irabeth", '''{n}Irabeth looks up sharply. The flush that follows is easier to see in the tips of her ears than in her cheeks.{/n}
"I am married."
{n}It is a statement, without accusation. She searches your expression and finds no surprise there.{/n}
"You know. Yes. I suppose you would."
{n}She folds her hands, unfolds them, and finally lets them lie still.{/n}
"I will not pretend I am offended by kindness. But I would rather we understood each other. Anevia is dearer to me than I can explain in an idle conversation."
{n}Even after saying it, she does not reach for the report.{/n}''', c('"I understand. I\'m glad we talked."', flags=("i_interest",))),
    n("want", "Irabeth", '''"I wanted a useful life. I have one. I wanted someone to share it with. I have her. It feels ungrateful to find anything missing."
{n}She hears what she has said and shakes her head.{/n}
"No. That is unfair to Anevia. I am responsible for finding room to live the life I asked for."
{n}A runner appears in the doorway. Irabeth lifts a hand, asking for a moment, and lets you finish speaking before she accepts the message.{/n}''', c('"We should do this again."')),
])

s("a_errand", "An unprofitable errand", "Anevia", 2,
  '"You promised me an honest assessment of your baking."', [
    n("start", "Anevia", '''"I promised you nothin' of the sort. You volunteered to risk your teeth."
{n}Anevia produces a small cloth parcel. Inside lies a piece of bread with a blackened crust and a surprisingly respectable middle.{/n}
"Before you ask, I paid for the flour. This operation's ruined my reputation as a thief."
{n}She divides the bread with a knife that has plainly served less domestic purposes. When a messenger approaches, she redirects him with a tilt of her head, then waits until he is out of earshot.{/n}
"There. The entire crusade can manage without us for ten minutes."''', c('[Taste the bread.]', "taste")),
    n("taste", "Anevia", '''{n}The crust is bitter. The bread beneath is dense but warm, with a little salt and a fragrance that belongs in a kitchen far from the Worldwound.{/n}
"Don't make that face. I've seen people swallow worse to impress a woman."
{n}The remark lands between you before she can dress it as a joke. She busies herself gathering crumbs.{/n}
"Irabeth took the worst bit. Said she liked it crisp. I married a terrible liar."
{n}She laughs, then stops smiling without looking unhappy.{/n}
"I wanted you to try it too. That's all."''',
      c('"The middle is good. You were right about the crust."', "home"),
      c('[Flirt] "I am trying to impress a woman. I hope honesty helps."', "honesty")),
    n("honesty", "Anevia", '''"Depends on the woman."
{n}She looks directly at you now. The distance between you is entirely ordinary. You are both suddenly aware of it.{/n}
"You keep sayin' things that'd be easier to laugh off if you didn't mean 'em."
{n}Her fingers brush a crumb from your sleeve, then retreat.{/n}
"Don't make a game of me. I'm good at games. I don't always know when to stop."''', c('"I\'m not making a game of you."', "home", flags=("a_interest",))),
    n("home", "Anevia", '''"We had a little place in Kenabres. You know. Small enough that if one of us was cross, there wasn't anywhere for the other to pretend not to notice."
{n}She folds the empty cloth along an old crease.{/n}
"I used to complain about it. Wanted a real kitchen. A window that didn't stick. Now I think about the way she'd take off her sword before she kissed me hello, so the scabbard wouldn't knock my knees."
{n}For once, she lets the silence last.{/n}
"I miss being somebody who expected the same door to be there tomorrow. It's a funny thing to miss."
{n}She offers you the last piece. It is the better one.{/n}''',
      c('"You can miss her and still enjoy being here."', "end"),
      c('"You should have had this time with Irabeth."', "wife")),
    n("wife", "Anevia", '''"I did."
{n}The answer is gentle, but the look accompanying it is sharp.{/n}
"You don't have to send me back to my wife every time I enjoy myself. She isn't my keeper. And I haven't forgotten her."
{n}Anevia draws a breath and looks down at the cloth.{/n}
"Sorry. You weren't sayin' that. I suppose I've been arguing with myself and you've wandered into the wrong side of it."''', c('"Then I\'ll listen before I argue."', "end")),
    n("end", "Anevia", '''{n}The ten minutes become twenty. You talk about ordinary things badly remembered: a meal, an unremarkable street, a season when rain was merely inconvenient. Anevia gives you fewer practiced answers as the conversation goes on.{/n}
"Next time, I might even manage not to burn it."
{n}She says next time with an ease that makes you both glance away. When she returns to work, she takes the cloth with her rather than leaving it for a servant to clear.{/n}''', c('"I\'ll hold you to that."')),
], requires=("a_cup",), delay=12)

s("i_hands", "The work of hands", "Irabeth", 2,
  '"May I sit with you while you mend that?"', [
    n("start", "Irabeth", '''{n}Irabeth is repairing a glove. With her sword she is decisive; with the needle she is methodical and faintly irritated. A small red bead on one finger suggests the needle has been winning.{/n}
"It is only a seam. I used to be better at this."
{n}She moves to make room. Without her gauntlets, the old marks on her hands are easier to see: a healed cut, a burn, pale lines at the knuckles. She notices you looking and curls her fingers.{/n}
"They are not very elegant."''',
      c('"They look like hands that have done useful things."', "useful"),
      c('[Flirt] "I wasn\'t thinking about elegance."', "look"),
      c('"Would you like help with the needle?"', "help")),
    n("help", "Irabeth", '''"If you can find the hole without stabbing either of us."
{n}She gives you the needle. The thread has frayed at the end; you trim it, feed it through, and return it. A tiny service, scarcely worth mentioning. Her thanks are oddly serious.{/n}
"Thank you. Now let me finish it. I have a company to inspect, and I refuse to do it with my thumb sticking out."''', c('"I understand."', "ordinary")),
    n("useful", "Irabeth", '''"They have. Though I have just managed to sew the thumb shut."
{n}She shows you the offending stitch, then cuts it. Her embarrassment gives way to a small, stubborn smile.{/n}
"A sword hilt, a frightened horse, an opponent's wrist. I generally know what to do with my hands. This needle is making a poor witness for me."
{n}She holds the glove open between her fingers, inspecting the repaired thumb.{/n}
"I had hoped to make a better impression than a woman defeated by her own clothing."''', c('"You can be more than one thing."', "ordinary")),
    n("look", "Irabeth", '''{n}Irabeth holds still. Her thumb rests against the place where the needle pricked her.{/n}
"Then perhaps you should not look at me like that."
{n}The words are firmer than her voice. Her needle stops halfway through the stitch. She looks at your mouth, then down at her hand.{/n}
"No. I snapped because I liked it. Give me the glove before I say anything worse."
{n}She reaches for the glove again, but leaves her bare hand on the table between you.{/n}''', c('"I can give you space."', "ordinary", flags=("i_interest",))),
    n("ordinary", "Irabeth", '''"Anevia would have drawn a face on the thumb by now. Given it a name. Addressed all further complaints to it."
{n}Irabeth looks at the glove and laughs despite herself.{/n}
"She knows how badly I want to win an argument with an inanimate object. She finds it endearing. I am still deciding whether to forgive her."
{n}She draws the next stitch through neatly. This time she lets you watch.{/n}
"I nearly put it away when you arrived. I wanted you to find me doing something well. That has become a rather inconvenient ambition."
{n}Her eyes meet yours.{/n}
"Anevia would notice that, too."''',
      c('"I don\'t need you to be impressive every moment."', "end"),
      c('"Tell her what you just told me."', "tell")),
    n("tell", "Irabeth", '''"Yes. I can already hear her asking whether I mended the glove or spent the evening looking at you."
{n}Irabeth draws the final stitch through, then stops with the thread between her fingers.{/n}
"I would rather she heard it from me than had to make a joke to get an answer."
{n}She cuts the thread.{/n}
"As for the glove, I shall insist on receiving some credit."
{n}She looks down at the cut thread.{/n}
"But I keep waiting for Anevia to ask before I tell her anything difficult."''', c('"It sounds like something you can change."', "end")),
    n("end", "Irabeth", '''{n}Irabeth pulls the glove on and closes her fist. The seam holds. She turns her hand for you to see, plainly pleased.{/n}
"There. I retain command of at least one thumb."
{n}A runner calls her name. She rises, but pauses beside your chair instead of answering at once.{/n}
"Next time, I shall choose something at which I have a chance of impressing you. You may choose how severely to judge it. Would you like that?"
{n}Her gloved fingers rest briefly against your forearm. She is smiling when she goes to the door.{/n}''', c('"I would."')),
], requires=("i_watch",), delay=12)

s("a_roof", "What she does not report", "Anevia", 3,
  '"You said there was a quiet place above the stores."', [
    n("start", "Anevia", '''{n}The little landing above the stores smells of old timber and rain. Anevia checks the stairs, then the narrow window behind you.{/n}
"Habit. Don't take it personally. If I ever stop lookin' at doors, check whether I've been replaced by a demon."
{n}She holds up a copper between finger and thumb.{/n}
"Nothing to sign tonight. You can try to catch me cheating instead."
{n}The copper disappears. You follow her empty hand; she opens the other, equally empty, then lets the coin fall from a fold in her scarf. At your look she laughs and starts to repeat the trick. Halfway through, she catches you watching her smile instead of her fingers. The coin strikes the floor.{/n}
"Oh, that's dirty."
{n}She retrieves it, still grinning.{/n}
"Just me, then. Apparently that's enough to keep you occupied."''', c('"That was what I came for."', "want")),
    n("want", "Anevia", '''"I noticed. Nearly cost me a copper."
{n}She slips it into her pocket and leans against the wall, facing you.{/n}
"Had that trick since I was a girl. Guards used to pat me down and send me on my way while their mates laughed. I've done it with a knife pointed at me. You stand there looking pleased with yourself, and suddenly I've got butter fingers."
{n}She shakes her head, enjoying the complaint.{/n}
"I've been thinking of things to show you. Places I'd like to take you. Then Beth comes through the door and I want to pull her down for a kiss, same as ever."
{n}Her smile lingers, but her voice grows quieter.{/n}
"I know what I want when she's there. Turns out I know what I want when you're here, too."''',
      c('"I feel it too."', "danger", flags=("a_interest",)),
      c('"We could keep this a friendship."', "friend"),
      c('"What do you want from me?"', "danger")),
    n("danger", "Anevia", '''"I want to try that again and see if you can make me drop it twice."
{n}Anevia takes out the copper. This time she sets it on the sill, where neither of you needs to watch it.{/n}
"I like the way you wait for me to do something outrageous. Makes me want to oblige. And I've been wondering what it'd take to get that look off your face."
{n}She steps closer, studying your mouth. Her fingers catch a loose thread at her shoulder and wind it tight.{/n}
"A kiss, maybe. Or maybe you'd look even more pleased. That's been keeping me awake."
{n}Below you, a latch clicks. She glances toward the stairs, then back.{/n}
"Beth doesn't know we're up here. She's never made me ask leave to enjoy myself. I know the difference between that and what I'm thinking about."''',
      c('"We should stop before this becomes something we have to hide."', "friend"),
      c('"I want you. I won\'t pretend that makes it harmless."', "end", flags=("a_interest",))),
    n("friend", "Anevia", '''{n}Anevia's face closes for a moment. When she speaks, the disappointment has not made her unkind.{/n}
"We could. It'd be a good thing to keep."
{n}She moves aside so that the stairs are no longer behind you.{/n}
"Thanks for saying it before we had to make a great miserable ceremony of it."
{n}You descend together. She tells a deliberately dreadful joke on the way down, and you both make a little too much of laughing at it.{/n}''',
      c('[End the romance route. Remain friends.]', flags=("closed",))),
    n("end", "Anevia", '''{n}For one unguarded instant, her expression is simply pleased. Then the cost of being pleased catches up with her.{/n}
"I ought to send you downstairs."
{n}She does not. You remain close, neither touching nor moving away, while a dozen small sounds come up from below. Nothing happens that would explain the speed of your breathing to anyone who found you there.{/n}
"Go on. I've got work."
{n}She gives the excuse an affectionate little grimace. She knows you no longer believe it. You leave her at the landing, looking after you.{/n}''', c('[Leave her with time to think.]')),
], requires=("a_errand",), delay=24)

s("i_respite", "The woman beneath the title", "Irabeth", 3,
  '"Can we speak after your duties are finished?"', [
    n("start", "Irabeth", '''{n}Irabeth arrives without her sword belt, carrying a small board with a worn grid scratched into it. She sets a pouch of wooden counters beside it.{/n}
"You asked to speak after my duties. I thought I should bring something that could not become a report."
{n}She empties the pouch. Several counters have been replaced with buttons.{/n}
"The rules are simple. Cross the board before your opponent blocks you. It gets less simple when someone begins losing. Anevia keeps proposing amendments."
{n}Her smile falters as she looks from the board to you.{/n}
"I do not know if this was what you had in mind. I wanted a reason to stay longer than a greeting."''',
      c('"You don\'t have to solve anything here."', "still"),
      c('"We can talk about what happened to you, if you want."', "wounds", requires=("broken",)),
      c('"You seem surer of yourself lately."', "strength", requires=("encouraged",))),
    n("wounds", "Irabeth", '''{n}She looks toward the door, then back at you.{/n}
"Not tonight."
{n}The refusal is quiet. It costs her something to make it.{/n}
"I am grateful when people listen. I am. But I do not want every private kindness to begin with an account of what was done to me. I have other things to say, even when I cannot think of them immediately."
{n}She draws a slower breath.{/n}
"And I do not want gratitude to answer a question neither of us has asked aloud."''', c('"Then we can leave it alone."', "still")),
    n("strength", "Irabeth", '''"Some days. I try not to make a proclamation of the good ones. It makes the bad ones feel like broken promises."
{n}She sits beside you with a care that has little to do with the furniture.{/n}
"Anevia has been patient. More patient than I have been with myself. She would hate hearing me call it patience. She says a marriage is not an extended charitable assignment."
{n}Irabeth laughs softly.{/n}
"I find that I believe her more often now."''', c('"I\'m glad."', "still")),
    n("still", "Irabeth", '''{n}You sit over the little board while Irabeth explains the moves. She sets two counters side by side, leaving what appears to be an inviting gap. When you reach toward it, her smile gives the trap away.{/n}
"I would never offer such helpful advice to a recruit. You have been warned."
{n}She waits while you reconsider. The pleasure she takes in your concentration is quite undisguised. Then your eyes meet across the board, and she leaves her own next move unfinished.{/n}
"I should have invited Anevia. She would enjoy watching me forget my own lesson."
{n}She turns a counter between her fingers.{/n}
"But I wanted you to myself this evening. That is why I did not."''',
      c('"You want to be here. So do I."', "admit", flags=("i_interest",)),
      c('"Then go to her. We should remain friends."', "friend")),
    n("admit", "Irabeth", '''"Yes. And I had intended to be a little less obvious about it."
{n}She sets down the counter. A faint flush reaches the tips of her ears.{/n}
"I wanted to beat you. Then I wanted to find out whether you would lean across the board and demand another game. I have been imagining that rather vividly."
{n}Her gaze travels to your mouth. This time she lets you catch her.{/n}
"In council I can argue with you and keep my mind on the argument. Here, with nothing at stake, I keep thinking about putting my hand on your neck."
{n}She draws her hand back from the board.{/n}
"I have not said any of this to Anevia. I came here intending to play a game. I should have asked myself why I cared so much whether you would enjoy it."''',
      c('"I won\'t ask you to decide tonight."', "end"),
      c('"You can still choose to leave."', "end")),
    n("friend", "Irabeth", '''{n}Irabeth nods. Relief and disappointment cross her face together.{/n}
"Thank you for being clear. It would be dishonest of me to pretend that I feel only relief. But I value your friendship. I would like to keep it."
{n}She takes up her gloves. This time, leaving is a decision rather than an excuse.{/n}''', c('[End the romance route. Remain friends.]', flags=("closed",))),
    n("end", "Irabeth", '''{n}When she rises, she stands close enough that you must lift your eyes to keep looking at her. Neither of you mistakes the moment for an accident.{/n}
"I should go."
{n}She makes herself say it before stepping away. At the door she looks back, then seems annoyed with herself for doing so.{/n}
"Good night."
{n}Long after she has left, you remember how much effort it took her to leave. You also remember that she did.{/n}''', c('[Let her go.]')),
], requires=("i_hands",), delay=24)

s("a_crossing", "A door left unlatched", "Anevia", 3,
  '"I have been thinking about what you said above the stores."', [
    n("start", "Anevia", '''{n}Anevia gives you a long look, then asks you to meet her after the evening reports. When you arrive, the room is empty except for her. She has put away the papers. Her scarf lies across the back of a chair.{/n}
"I've been trying to think of something clever to say. It's annoying. Usually you can't stop me."
{n}She walks to the door and rests her hand on the latch without lowering it.{/n}
"If you leave now, we can still call this a conversation."''',
      c('"Is that what you want?"', "choice"),
      c('[Leave. End the romance route.]', "leave")),
    n("choice", "Anevia", '''"No."
{n}She faces you. Without the scarf and the joke she was preparing, she looks no less capable, only less protected.{/n}
"That's the honest answer. I'd like a different honest answer. One where I get to feel this and nobody gets hurt. Haven't found it."
{n}She looks briefly toward the closed door.{/n}
"Irabeth thinks I'm finishing work. I was. Then I waited for you instead."
{n}The admission has no glamour. It makes the little room feel smaller.{/n}
"I'm telling you because I won't have you think this is an arrangement she's agreed to. It isn't."''',
      c('"I understand. I still want to stay."', "kiss"),
      c('"Then I should go."', "leave")),
    n("kiss", "Anevia", '''{n}Anevia comes to you slowly enough that you could step aside. When you do not, she puts a hand against your cheek and studies your face with the same unsettling concentration she gives a locked door.{/n}
"Last chance to ask for a report instead."
{n}You answer by drawing closer. Her first kiss is brief. She breaks it herself, searching your expression, then kisses you again with the hesitation gone. For a little while the only thing either of you says is the other's name.{/n}
{n}A sound in the corridor makes her stiffen. She turns toward it before she can stop herself. Footsteps pass. No one knocks.{/n}
"That's going to happen every time, isn't it?"
{n}She is not asking about the footsteps.{/n}''',
      c('"We can stop."', "stop"),
      c('[Stay with her. Let the evening pass in private.]', "night")),
    n("night", "Anevia", '''{n}She goes back to the door. Her hand rests on the wood, not the latch, and she leaves it unbarred: anybody could walk in, and she wants you to know she knows it. When she turns round, whatever she was arguing with herself about has been settled.{/n}
"No speeches. Not tonight. Just don't lie to me while we're doin' this."
{n}She crosses the room in four steps and pulls the scarf from the chair to drop it on the floor, as though clearing the last piece of evidence. Her fingers are quick and not quite steady on your buckles; she swears at one, gives up on it and drags your shirt over your head instead. Her own laces she undoes herself, watching your face the whole time, and lets the dress fall.{/n}
{n}She walks you backwards until the edge of the bed catches your knees, pushes you down onto it and follows, one knee either side of your hips. Her hands flatten on your chest. For a heartbeat she holds there, breathing hard, as if memorizing the moment for a report she will never file. Then she leans down, her hair falling around both your faces, and drags you up against her.{/n}
{n}Later, she dresses in silence. She puts her scarf on twice before she is satisfied with how it sits. At the door she presses her forehead briefly to yours.{/n}
"I wanted that. Whatever happens, I won't make you carry the lie that I didn't."
{n}Then she leaves to go home to the woman who trusts her.{/n}''', c('[Let her leave.]', flags=("a_affair",))),
    n("stop", "Anevia", '''{n}She keeps her hand against your face for a moment longer, then lowers it.{/n}
"We should've said that ten minutes ago."
{n}Her voice is soft, without blame. You have crossed a boundary even if you refuse to cross the next one. She does not ask you to pretend otherwise.{/n}
"I'll see you tomorrow. I don't know what I'll say. But I'll see you."''', c('[Leave for tonight.]', flags=("a_affair",))),
    n("leave", "Anevia", '''{n}Anevia steps aside. Her hand drops from the latch.{/n}
"All right."
{n}She makes no joke to spare either of you the embarrassment. You are grateful for that much honesty.{/n}''', c('[End the romance route.]', flags=("closed",))),
], requires=("a_roof",), delay=24)

s("i_crossing", "No order given", "Irabeth", 3,
  '"Irabeth, I don\'t want to keep pretending I came only to talk."', [
    n("start", "Irabeth", '''{n}Irabeth closes her eyes for a moment. When she opens them, she looks at you with a steadiness that makes retreat more difficult.{/n}
"Neither do I."
{n}She has chosen a room where she can leave without passing through yours. You understand the care behind the choice when she draws attention to it herself.{/n}
"Before anything else: I must be able to say no to you. Tomorrow, in council, in front of your officers. I will not become agreeable because I am afraid of losing this."
{n}Her hands are clasped tightly enough to blanch the knuckles.{/n}
"And you must be able to hear it without making me pay."''',
      c('"Your judgment remains your own. I would want it no other way."', "wife"),
      c('"I expect loyalty from everyone close to me."', "refuse"),
      c('"This is a mistake. We should stop."', "leave")),
    n("wife", "Irabeth", '''"I have not told Anevia."
{n}Irabeth does not soften the admission.{/n}
"There is no argument that makes that honorable. I have rehearsed several and disliked myself more with each one."
{n}She takes a step toward you, then stops.{/n}
"I love her. I need you to understand that before you let yourself imagine anything else. I am not waiting for someone better to release me from a poor choice. Marrying her was the best choice I ever made."
{n}Her voice catches, and she waits until it is under control.{/n}
"And still I have been thinking about touching you all day. There. That is what I have made of my certainty."''',
      c('"I want you too. That doesn\'t excuse either of us."', "kiss"),
      c('"Then let us stop here."', "leave")),
    n("kiss", "Irabeth", '''{n}You hold out your hand. Irabeth looks at it for long enough that you nearly withdraw it. Then she takes it, her fingers warm and firm around yours.{/n}
"Iomedae forgive me. I have wanted to do this since you walked in."
{n}She bends toward you. The first kiss is careful, almost solemn. When you rest your hand against the back of her neck, she makes a small, startled sound and draws you closer. Her strength is familiar; the tenderness with which she contains it is not.{/n}
{n}When you part, she keeps her forehead against yours. Her breath is unsteady.{/n}
"I had forgotten that wanting could make me feel so... foolish."
{n}For a moment, despite everything, she smiles.{/n}''',
      c('[Stay. Let the night continue in private.]', "night"),
      c('"This is enough for tonight."', "gentle")),
    n("night", "Irabeth", '''{n}Irabeth takes off her gloves and sets them carefully together. Then she laughs at the absurdity of being orderly at such a moment. The laughter loosens something in both of you.{/n}
"Come here."
{n}You go to her. She kisses you again, harder, and her hands go to her own buckles: the sword belt onto the chair, the breastplate onto the floor with a noise that makes her wince and then laugh. She hauls her shirt over her head, catches you by the collar and pulls you down onto the bed with her, her weight rolling over yours and her knee sliding between your thighs.{/n}
{n}Later, before she leaves, she sits beside you in the darkness. Her hand finds yours without searching.{/n}
"It mattered to me. I do not know what I am going to do with that. But it mattered."
{n}She does not ask for absolution, and you do not offer it.{/n}''', c('[Say good night.]', flags=("i_affair",))),
    n("gentle", "Irabeth", '''{n}She nods and lets her arms loosen around you. There is disappointment in her face, but no wounded pride.{/n}
"Yes. Stay a moment, though. I am not quite ready to let go."
{n}She kisses your hand before releasing it. The gesture is so unguarded that it stays with you after she has gone.{/n}''', c('[Say good night.]', flags=("i_affair",))),
    n("refuse", "Irabeth", '''{n}Irabeth's expression clears. Whatever uncertainty brought her here has found an answer.{/n}
"Then you should seek it from someone else. I will serve the crusade. I will not purchase affection with my obedience."
{n}She picks up her gloves and walks out. This time she does not look back.{/n}''', c('[End the romance route.]', flags=("closed",))),
    n("leave", "Irabeth", '''"Yes."
{n}The answer comes with visible effort. She steps away before either of you can find another reason to remain.{/n}
"I am sorry. That does not mean I wish you had never been kind to me."
{n}She returns to her duties. The next time she speaks to you, her courtesy is precise and painful.{/n}''', c('[End the romance route.]', flags=("closed",))),
], requires=("i_respite",), delay=24)

s("a_morning", "The cost of an easy lie", "Anevia", 3,
  '"How have you been since we were alone?"', [
    n("start", "Anevia", '''"Efficient."
{n}Anevia smiles without showing her teeth.{/n}
"Got through the reports, caught a man stealing lamp oil, remembered to eat. Very successful day."
{n}When you do not accept the answer, she turns away from the open doorway.{/n}
"Irabeth asked if I'd been working late. I said yes. Easy as breathing. That's what I can't stop thinking about. It ought to have caught in my throat."
{n}She grips her own wrist and rubs it once.{/n}
"I've lied to worse people about bigger things. That doesn't help as much as I thought it would."''',
      c('"We need to tell her."', "tell"),
      c('"I don\'t regret being with you."', "regret"),
      c('"Then be more careful."', "careful")),
    n("careful", "Anevia", '''{n}Anevia's gaze sharpens.{/n}
"If I wanted advice on not gettin' caught, you'd be the last person I'd ask. I know how to keep a secret. I'm trying to decide whether I can stand keeping this one."
{n}She looks tired rather than angry.{/n}
"Don't turn what happened into a little operation. Please. I've got enough of those."''', c('"You\'re right. I was avoiding what you meant."', "tell")),
    n("regret", "Anevia", '''"Neither do I. Not the way I ought to."
{n}She looks at you, and for a moment the room you shared seems close enough to step back into.{/n}
"I regret the lie. I don't regret your hands on mine. Try making those fit together without cutting yourself on an edge."
{n}Her fingers uncurl.{/n}
"It'd be easier if I hated you a little. You've been very inconsiderate about that."''', c('"Wanting each other doesn\'t make the lie disappear."', "tell")),
    n("tell", "Anevia", '''"Yes. We do."
{n}She says it as if agreeing to a difficult task whose dimensions she has already measured.{/n}
"Let me speak to her with you. Not a confession dumped on her before she has to inspect a garrison. Not some awful gift you hand over to prove how honest you can be. Give her a room where she can be angry. Give her time."
{n}Anevia reaches toward you, stops, then deliberately takes your hand.{/n}
"I still want to see you. That's the part I can't offer to fix just by saying sorry. But I don't want her living inside a story everyone understands except her."''',
      c('"We will tell her together."', flags=("a_will_tell",)),
      c('"There is something else you need to know. Irabeth and I have been involved too."', "both", requires=("i_affair",))),
    n("both", "Anevia", '''{n}Her hand goes slack in yours.{/n}
"Say that again. Slowly."
{n}You do. Anevia listens without interruption. When you finish, she withdraws her hand, lays it flat on the table, and looks down at it.{/n}
"She didn't tell me."
{n}The words are almost inaudible. A moment later Anevia gives a short, ugly laugh.{/n}
"Listen to me. As if I've earned the right to be surprised."
{n}She looks up.{/n}
"No more private explanations. The next time we talk about this, she's in the room."''', c('"Agreed."', flags=("a_will_tell", "disclosed_a"))),
], requires=("a_crossing", "a_affair"), delay=12)

s("i_morning", "What an oath cannot answer", "Irabeth", 3,
  '"You have been avoiding being alone with me."', [
    n("start", "Irabeth", '''"Yes."
{n}Irabeth's willingness to admit it leaves you without the argument you had prepared.{/n}
"I thought that distance would help me think clearly. It has mostly helped me think about the distance."
{n}She stands near the window. You can hear a drill being called somewhere outside. She has corrected that same drill often enough that her lips almost shape the next order.{/n}
"I have prayed. Not for permission. I know better than to ask a goddess to make an exception simply because I would enjoy it."
{n}She looks back at you.{/n}
"I asked for the courage to stop hiding behind words I respect."''',
      c('"What do you mean?"', "oath"),
      c('"Do you wish we had never been together?"', "regret")),
    n("oath", "Irabeth", '''"Duty. Sacrifice. Restraint. I have used all of them to avoid telling my wife that I am frightened or tired or that I need her. Now I am tempted to use them to avoid telling her something worse."
{n}Her expression hardens, but the anger is directed inward.{/n}
"I could make a magnificent speech about giving you up for the sake of my marriage. If I never told her why, it would still leave her living with a lie. A very noble lie, perhaps. I doubt she would enjoy the distinction."
{n}She rubs a thumb over the ring on her hand.{/n}
"I do not want to become a person who calls cowardice consideration."''', c('"Then we need to speak with her."', "tell")),
    n("regret", "Irabeth", '''"No. I wish I had spoken to Anevia before I came to you. That is a different wish."
{n}She watches your face, with none of the haste that made her turn away before.{/n}
"I remember reaching for you. How readily you came closer. I had spent so long wondering what you would do that, for a moment, I could think of nothing else."
{n}Her fingers tighten on the windowsill.{/n}
"I would like to reach for you now. Instead I am standing here trying to rehearse an answer for my wife. She deserves to hear it before I find a prettier version."''', c('"What happens now?"', "tell")),
    n("tell", "Irabeth", '''"We tell her. Together, if you are willing. I am not asking you to speak for me. I am asking you not to leave her wondering which of us is telling the part that makes us look better."
{n}She studies you with a frankness that allows neither consolation nor evasion.{/n}
"Until then, no stolen evenings. I have to look Nevi in the face. I will not kiss her with another lie in my mouth."''',
      c('"I will be there, and I will tell the truth."', flags=("i_will_tell",)),
      c('"Before that, you should know that Anevia and I have also been involved."', "both", requires=("a_affair",))),
    n("both", "Irabeth", '''{n}Irabeth draws a breath and cannot quite finish it. Her eyes remain fixed on yours.{/n}
"Anevia."
{n}You tell her without offering details she has not asked for. She listens, then turns toward the window. The drill outside has stopped.{/n}
"I thought I was the only one who had betrayed something. That is a shameful thing to find comforting."
{n}She does not turn back immediately.{/n}
"Please leave me for a little while. I will speak to her. Then the three of us will speak. I do not want another version of this that she has not heard."''', c('"I will give you that time."', flags=("i_will_tell", "disclosed_i"))),
], requires=("i_crossing", "i_affair"), delay=12)

s("reckoning", "Three accounts of the same evening", "Together", 3,
  '"It is time the three of us spoke in private."', [
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("start", "Narrator", '''{n}Anevia has chosen a small room with a table and three chairs. Irabeth has brought no armor beyond the habits of her posture. Neither woman sits beside you. They sit facing each other, leaving the third place between them empty until you take it.{/n}
{n}Anevia checks the latch. Irabeth watches her do it.{/n}
"We don't need guarding," {n}Irabeth says.{/n}
"I know." {n}Anevia takes her hand off the door.{/n} "That's not why I checked."
{n}The silence after that is more painful than an accusation.{/n}''',
      c('"I have been involved with both of you. I knew each of you was keeping it from the other."', "truth", flags=("reckoning_honest",)),
      c('"We all wanted this. Perhaps there is less to apologize for than we think."', "excuse"),
      c('"I should not be part of your marriage any longer."', "withdraw")),
    # end eng7-f2
    n("excuse", "Irabeth", '''"No."
{n}Irabeth does not raise her voice.{/n}
"I wanted you. I did not agree to be deceived by my wife. She did not agree to be deceived by me. Do not use what we wanted to erase what we did."
{n}Anevia studies the grain of the table.{/n}
"And don't try to sell me my own tricks. I know what a convenient summary sounds like."''',
      c('"You are right. I knew, and I helped keep you both in the dark."', "truth", flags=("reckoning_honest",)),
      c('"I will not apologize for giving you what you wanted."', "end_bad", flags=("closed",))),
    n("truth", "Anevia", '''"Right. Now we can stop guessing which bits we're still missing."
{n}Anevia looks at Irabeth. The confidence in her voice lasts exactly that long.{/n}
"I kept saying it was one little thing of my own. An hour nobody else got to fill. Then I came home and let you think I was tired from work."
{n}Irabeth's jaw tightens.{/n}
"I thought you had stopped asking how I was because you were exhausted. I was relieved. It meant I did not have to tell you where I had been."
{n}Anevia shuts her eyes.{/n}
"Desna. We were helping each other hide it."
{n}For a while you hear nothing but the lamp and someone walking in the passage outside.{/n}''', c('[Listen.]', "hurt"), portrait="TogetherReckoning"),
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("hurt", "Irabeth", '''"Were you unhappy with me?"
{n}The question costs Irabeth more than anger would have. Anevia answers at once.{/n}
"I was happy to come home to you. I was happy up there on that landing, too. I thought if I kept the two apart, I could keep both."
"You could have told me."
"So could you."
{n}Anevia presses her lips together, then looks directly at her wife.{/n}
"Sorry. That was cheap. I'm answering for me."
{n}Irabeth lays her hands flat on the table.{/n}
"I liked being bold. Making the Commander wait for my next move. I kept wanting to see how far I could go."
{n}She looks at you before turning back to Anevia.{/n}
"Then you asked about my evening, and I let you believe I had spent it alone. I found that much easier than looking you in the face now."
"You took the choice," {n}Anevia says.{/n} "So did I."''',
      c('"You don\'t have to decide tonight whether you can forgive anyone."', "space"),
      c('"Could we find a way for all three of us to be together?"', "too_soon")),
    # end eng7-f2
    n("too_soon", "Anevia", '''"Maybe. I don't know."
{n}Anevia's uncertainty is more honest than a refusal would have been.{/n}
"But if you turn this into a clever solution before I've finished being hurt, I'll walk out. And I won't be walking toward your room."
{n}Irabeth nods slowly.{/n}
"There may be something worth keeping here. We cannot use it to hurry past this conversation."''', c('"Then I will stop asking for an answer tonight."', "space")),
    n("space", "Narrator", '''{n}They ask questions. Some are about dates. Some are about words you said and whether you meant them. You answer what concerns you and leave each woman to answer for herself. Neither asks for an account of private intimacies. Neither mistakes restraint for a lack of imagination.{/n}
{n}At last Irabeth pushes back her chair.{/n}
"We need time together. Anevia and I. Not to decide what you deserve. To find out what we still know how to say to each other."
{n}Anevia stands beside her, leaving a little space between them.{/n}
"We'll speak again. Separately first, I think. And nobody's borrowing work as an excuse in the meantime."
{n}They leave together. Neither reaches for the other's hand. Neither moves far enough away to make reaching impossible.{/n}''', c('[Give them time.]')),
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("withdraw", "Narrator", '''{n}Neither woman tries to stop you. That is harder than you expected.{/n}
"Then say it plainly," {n}Irabeth says.{/n}
{n}You do. You tell them that the affairs are over and that you will not ask either to leave the other. Anevia listens with her arms folded, but when you finish she lets them fall to her sides.{/n}
"All right. We'll have enough to talk about without guessing whether you're waiting outside the door."
{n}You leave them together. Repairing their marriage is theirs to attempt, and no longer yours to direct.{/n}''', c('[End the romance route.]', flags=("closed", "parted_honestly"))),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("end_bad", "Narrator", '''{n}Irabeth rises. Anevia does not look at you again.{/n}
"Then there is nothing further to discuss," {n}Irabeth says.{/n} "You will receive the same service and the same honest counsel as before. Nothing more."
{n}The meeting ends. There is no dramatic dismissal, only a door opened and held until you leave.{/n}''', c('[Leave.]')),
    # end eng7-f2
], requires=("a_morning", "i_morning", "a_affair", "i_affair"), delay=24)

s("a_truth", "What she keeps", "Anevia", 3,
  '"You said you wanted to speak to me alone."', [
    n("start", "Anevia", '''"I did. Irabeth knows we're talking. Before you wonder."
{n}Anevia pulls out a chair without offering you the easy smile that used to accompany the gesture.{/n}
"We talked half the night. Had a very dignified argument about who'd been protecting whom from knowing what. At one point I told her she ought to have trusted me to be angry. Then I remembered I'd done exactly the same thing."
{n}Her mouth twists.{/n}
"Hard to win an argument when your wife can hand you your own evidence."''', c('"How is she?"', "her"), c('"How are you?"', "self")),
    n("her", "Anevia", '''"Ask her."
{n}The reply is immediate, then gentler.{/n}
"That's something we're trying. I don't do her talking for her. She doesn't decide what I can bear to hear. You don't carry messages between us like a poor fool sent across a battlefield."
{n}Anevia folds her hands around a cup.{/n}
"I can tell you she stayed. So did I. That felt like something."''', c('"Then how are you?"', "self")),
    n("self", "Anevia", '''"Angry. Embarrassed. Still stupid enough to be glad when I see you."
{n}She lifts her eyes to yours.{/n}
"I keep catching myself measuring it. Did you look at her that way? Did you say that to her too? It's a foul little habit. Doesn't matter that I know better."
{n}She lets out a breath, slow and deliberate.{/n}
"I don't want to become an investigator in my own home. I know where that ends. You search long enough, you start thinking the search itself is proof."
{n}Her cup remains untouched.{/n}
"If there is anything after this, I need a life that belongs to me as well as a marriage that matters. That's work I should've done before I found an excuse to make it exciting."''',
      c('"What can I do that would help?"', "need"),
      c('"You matter to me separately from Irabeth."', "separate")),
    n("separate", "Anevia", '''"Good. Keep meaning that when I'm inconvenient."
{n}A flicker of her old humor returns, then settles into something more serious.{/n}
"I'm not the easier wife. People think that because I laugh more. There are things I won't give you just because you ask nicely. My whole past, for one. Every private thing I've ever told her, for another."
{n}She watches your response before continuing.{/n}
"What I choose to tell you is a gift. It isn't a toll I owe for being wanted."''', c('"You decide what you share."', "need")),
    n("need", "Anevia", '''"Be where you say you'll be. If something changes, tell me. Don't send me a jewel when what I need is an answer. And don't tell me I'm silly for having a bad day after I agreed to try."
{n}Her shoulders loosen a little as she speaks.{/n}
"I can imagine wanting this. The three of us. That's new, and it scares me more than the part I already did. Sneaking around was something I knew how to do."
{n}She finally drinks from the cup and makes a face.{/n}
"Cold again. Must be a curse."''',
      c('"I can promise honesty. I can\'t promise never to disappoint you."', "end", flags=("a_heard",)),
      c('"I think we should stop trying to turn this into a relationship."', "stop")),
    n("end", "Anevia", '''"That's an answer I might believe."
{n}She does not touch you when you leave. But she tells you a small, ridiculous thing that happened in the kitchen that morning. You recognize the effort in offering something that is neither a secret nor a confession.{/n}
{n}You laugh. After a moment, so does she.{/n}''', c('[Leave her to her day.]')),
    n("stop", "Anevia", '''{n}Anevia nods, once.{/n}
"Then we stop. I'd rather hear it now than spend a month trying to make you comfortable enough to stay."
{n}She opens the door. The conversation has hurt her, but she does not use that hurt to keep you there.{/n}''', c('[End the romance route.]', flags=("closed", "parted_honestly"))),
], requires=("reckoning",), delay=24)

s("i_truth", "Without a penance", "Irabeth", 3,
  '"I would like to hear what you want, Irabeth."', [
    n("start", "Irabeth", '''"I have a list of things I ought to want. You have probably heard most of it."
{n}Irabeth looks tired, but her attention is steady.{/n}
"Anevia told me last night that if I apologized once more without saying anything new, she would start charging a copper each time. I nearly apologized for that."
{n}She allows herself a brief smile.{/n}
"She was right. I was making her reassure me. It is a selfish way to appear remorseful."''', c('"What would you say instead?"', "want")),
    n("want", "Irabeth", '''"I want to keep my wife. I want to keep caring for you. I want those wishes to stop requiring someone else's ignorance."
{n}The words come slowly, without the shelter of a prepared speech.{/n}
"I want to be able to enjoy an evening without proving I have earned it. I want to be touched when I am neither wounded nor being congratulated. I want to stop treating happiness as a thing I must first justify to every person who has suffered more than I have."
{n}She looks down, then makes herself look up again.{/n}
"And I want to remain someone I can respect in the morning. I do not yet know how to put all of that into one life."''',
      c('"We can find out slowly."', "slow"),
      c('"You don\'t have to atone by giving up everything you want."', "penance")),
    n("penance", "Irabeth", '''"No. But wanting to avoid punishment is not proof that a choice is right."
{n}She considers you with sober affection.{/n}
"I need you to disagree with me sometimes. If every difficult thought can be answered by telling me that I am too hard on myself, I will learn nothing except how pleasant it is to be forgiven."
{n}Her hand rests flat on the table.{/n}
"Anevia says that loving me does not require finding me blameless. I think I am beginning to understand what a generous thing that is."''', c('"Then we can care for you and still ask you to do better."', "slow")),
    n("slow", "Irabeth", '''"Slowly, then."
{n}She says it with the determination of someone accepting a demanding assignment, catches herself, and laughs softly.{/n}
"You see the difficulty. Even now I am tempted to turn this into a campaign I can win by diligence."
{n}Her expression becomes serious again.{/n}
"There are terms I will not negotiate. My duties must remain separate. No gifts from crusade stores, no favors for anyone who knows about us. And Anevia is not to feel that she must agree because losing you might break me."
{n}She leans forward.{/n}
"I will be hurt if this ends. I will survive it. She needs to know that. So do you."''',
      c('"I hear you. Neither of you owes me a relationship."', "end", flags=("i_heard",)),
      c('"I cannot offer what you are asking for."', "stop")),
    n("end", "Irabeth", '''{n}Irabeth extends her hand, palm upward. You take it. This time there is no secrecy in the gesture, but she still looks at your joined hands as if they were something she must learn to trust.{/n}
"Thank you for listening to the parts that were not flattering."
{n}You sit together for a while. When she leaves, she tells you where she is going. It is such a small courtesy that its absence until now suddenly seems enormous.{/n}''', c('[Let the conversation rest.]')),
    n("stop", "Irabeth", '''"Then I am glad you have told me."
{n}She is not glad, and neither of you asks her to make the words convincing.{/n}
"I hope, in time, we can remember the kindness without making an excuse of it. For now I would prefer some distance."''', c('[End the romance route.]', flags=("closed", "parted_honestly"))),
], requires=("reckoning",), delay=24)

s("table", "A place for the third chair", "Together", 3,
  '"Shall we talk about what we could build together?"', [
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("start", "Narrator", '''{n}This time there is food on the table. Anevia has bought it rather than attempting to bake. She catches you looking at the loaf.{/n}
"Thought we'd suffered enough for one week."
{n}Irabeth gives her a look that is half affection and half warning. Anevia shrugs, but her smile is genuine.{/n}
"We have spoken," {n}Irabeth says.{/n} "A great deal. We do not agree about everything."
"Which is how we knew we hadn't been replaced by unusually polite demons."
{n}Irabeth reaches for her wife's hand. Anevia lets her take it.{/n}''', c('[Sit with them.]', "proposal")),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("proposal", "Irabeth", '''"We would like to try. The three of us."
{n}Irabeth says it plainly, then looks to Anevia rather than continuing on her behalf.{/n}
"Not 'you can borrow my wife on certain evenings'," {n}Anevia says.{/n} "I know that sounds obvious. I want it said anyway. You're not something we're dividing up, and neither are we."
{n}She pulls the bread apart with her fingers.{/n}
"We keep our marriage. We make room for you as yourself. And if one of us isn't happy, we don't decide the other two get to outvote her. Or you."
{n}Irabeth nods.{/n}
"We cannot promise that it will be easy. We can promise to stop pretending that difficulty is a reason to lie."''',
      c('"I want that too."', "terms"),
      c('"Would I always be a guest in your marriage?"', "guest"),
      c('"I care about you both, but I cannot do this."', "stop")),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("guest", "Anevia", '''"That's what I was afraid you'd ask. Because I don't have a tidy answer."
{n}She looks to Irabeth, who answers without defensiveness.{/n}
"We have years together. A history we cannot and should not erase. But history is not authority over you. You must have a say in the life we share. A real say, including the right to dislike our habits."
"Especially her habits," {n}Anevia adds.{/n} "Mine are charming."
{n}Irabeth squeezes her hand.{/n}
"And there must be time for each of us alone with you. We are not offering you admission to a room where the two of us have already made every decision."''', c('"Then let us decide the first things together."', "terms")),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("terms", "Narrator", '''{n}The discussion is less graceful than the proposal. You speak about nights together and nights apart. About what may be said in public, and what belongs only to the person who confided it. About the difference between privacy and an alibi.{/n}
"If I ask for an evening with my wife," {n}Irabeth says,{/n} "it cannot become a test of whether I love you enough. And if you ask for time with her, I must not treat that as a trespass."
"Same goes for you and me," {n}Anevia tells her.{/n} "We don't make our marriage the place nobody's allowed to need anything."
{n}When other attachments come up, neither woman assumes your answer.{/n}''',
      c('"I have other people in my life. I will not hide them from you or ask you to compete."', "open", flags=("other_loves",)),
      c('"For now, I want to see what the three of us can become. If that changes, I will say so."', "room")),
    # end eng7-f2
    n("open", "Anevia", '''"Then we talk about time. Actual time. An evening you've promised somebody can't also be an evening you've promised me."
{n}She holds up a hand before Irabeth can speak.{/n}
"And no, you don't get to say you're used to sharing people with the crusade, so whatever's left will do. That's exactly the sort of nonsense we're trying to stop."
{n}Irabeth looks caught, then amused.{/n}
"I was not going to say that."
"You were thinking it very loudly."
{n}They agree that affection elsewhere is not itself a betrayal. Broken promises still will be. No one asks you to end another relationship, and no one pretends that every possible difficulty has been settled.{/n}''', c('"I can agree to that."', "room")),
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("room", "Irabeth", '''"One more thing. I do not want this evening to end with all of us proving how comfortable we are."
{n}Irabeth's ears redden. Anevia's expression softens.{/n}
"You mean we can eat the bread without anyone having to take their shirt off."
"I was attempting to put it more delicately."
"You were doing very well."
{n}The laughter that follows is a little embarrassed and entirely welcome. You eat together. Some of the conversation is awkward; some of it is wonderfully ordinary. When you leave, each woman kisses you goodbye in the other's presence. Anevia watches Irabeth do it, then looks away, then deliberately looks back.{/n}
"All right," {n}she says.{/n} "We can learn."''', c('[Begin trying, without demanding certainty.]', flags=("trying",))),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("stop", "Narrator", '''{n}The two women hear you out. Neither asks you to make your refusal sound like a lesser affection.{/n}
"Then thank you for coming far enough to say it honestly," {n}Irabeth says.{/n}
{n}Anevia folds the cloth around the remaining bread.{/n}
"Take this. We bought too much."
{n}It is a small kindness, offered without a claim on you. You accept it and leave them together.{/n}''', c('[End the romance route.]', flags=("closed", "parted_honestly"))),
    # end eng7-f2
], requires=("a_truth", "i_truth", "a_heard", "i_heard"), delay=24)

s("ordinary", "The first ordinary quarrel", "Together", 3,
  '"We missed the evening we planned. I would like to talk about it."', [
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("start", "Narrator", '''{n}The evening was meant to be simple. Supper, no reports, no attempt to settle the future. Then duties ran late. A message failed to arrive. Someone waited longer than she would like to admit.{/n}
"I am not angry that you were needed," {n}Irabeth says.{/n} "I am angry that I sat there inventing reasons not to feel disappointed."
{n}Anevia folds her arms.{/n}
"And I'm angry that I knew you were doing that and tried to make a joke out of it instead of saying I was disappointed too."
{n}Neither looks at you as if you alone are responsible. That does not make the conversation comfortable.{/n}''',
      c('"We need a better way to send word when plans change."', "practical"),
      c('"This is what loving the Commander means. You knew that."', "rank"),
      c('"I need to know when your plans change too. I can be the one left waiting."', "waiting")),
    # end eng7-f2
    n("waiting", "Irabeth", '''"Of course. I did not mean..."
{n}Anevia looks at her. Irabeth stops, then begins again.{/n}
"I suppose I thought you would always have something else to do."
"Beth."
"I can hear it now that I have said it."
{n}Irabeth turns back to you, visibly resisting the urge to explain herself further.{/n}
"Tell me what you wanted us to do."''',
      c('"Come and find me afterward. Even a shorter evening together matters to me."', "find_me", flags=("ordinary.find_after",)),
      c('"Tell me not to wait. I would rather make another plan than keep watching the door."', "release_wait", flags=("ordinary.release_wait",))),
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("find_me", "Anevia", '''"Even if I can't explain what's kept me?"
{n}She asks without making it a joke.{/n}
"I can come home with a head full of things I can't tell you. Sometimes I go quiet because I'd rather that than spend the evening sayin' what I can't say."
{n}Irabeth's expression shifts at something familiar in the description.{/n}
"You could tell us you wanted to stay," {n}she says.{/n}
"Yes. Could've done that."
{n}Anevia turns back to you.{/n}
"I can look for you. If you've gone to bed, I'll leave you to sleep. But I won't decide you wouldn't want me there just because the good part of the evening got away."''',
      c('"That is what I am asking. We can eat before we have anything clever to say."', "practical")),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("release_wait", "Irabeth", '''{n}Irabeth looks down at the unused place setting.{/n}
"I would have found that difficult to hear tonight."
"Better than not hearin' anything," {n}Anevia says.{/n}
"Yes. Better than that."
{n}Irabeth draws the plate toward her and begins to cut the bread.{/n}
"I don't want us all sitting in different rooms because each of us is trying not to be a burden. If I cannot come, I will say so. If I still want you to find me later, I will say that too."
{n}She puts the bread where all three of you can reach it.{/n}
"And if you have already made another plan, I will try not to treat that as a verdict on how much you wanted to see me."''',
      c('"We can miss one evening without losing the next one."', "practical")),
    # end eng7-f2
    n("rank", "Irabeth", '''"I know what serving the Commander means. We were discussing something else."
{n}Irabeth's voice is level. Anevia's is not.{/n}
"If being disappointed is disloyalty now, we should've stuck to sneaking around. At least then I knew what the rules were."
{n}She immediately regrets the last sentence, but does not withdraw the first.{/n}
"That was cruel. I'm sorry. The rest of it stands."''',
      c('"You are right. I used my title to avoid answering you."', "practical"),
      c('"My duties will always come first. I cannot offer more."', "stop")),
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("practical", "Narrator", '''{n}Anevia finds a scrap of paper and writes: under the candle by the door.{/n}
"The aides move that whenever they leave reports," {n}Irabeth says.{/n}
{n}She takes an empty tea tin from the sideboard and sets it where all three of you can see it.{/n}
"Here. A note inside, the lid on."
"I'll try not to order more tea for it," {n}Anevia says.{/n}
{n}You agree to check the tin before leaving for an evening together. No confidential names on the note, and no one needs to wait for the others before eating.{/n}
"And we reschedule," {n}Anevia says.{/n} "Actually reschedule. Not 'soon', which in military language means sometime after the next catastrophe."
{n}Irabeth nods.{/n}
"If it is always the same person's evening that disappears, we speak about that too."
{n}Once the practical matters are settled, an awkward silence remains.{/n}''', c('"Are we still angry?"', "angry")),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("angry", "Anevia", '''"A little."
{n}Anevia looks almost relieved to admit it.{/n}
"I don't want to have to stop being angry the instant we find a sensible answer. Makes the whole thing feel like a performance review."
"Nor do I," {n}Irabeth says.{/n} "But I would still like supper."
{n}You eat what is available. It is not the meal anyone had planned. Halfway through it, Anevia steals a particularly good piece from Irabeth's plate. Irabeth catches her wrist, removes the morsel, and gives it to you. Anevia's offended expression makes both of you laugh.{/n}''', c('[Keep the new arrangement.]', flags=("kept_terms",))),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("stop", "Narrator", '''{n}Irabeth nods slowly. Anevia pushes her plate away.{/n}
"Then that is the answer," {n}Irabeth says.{/n} "We will not keep asking for a life you have told us you cannot share."
{n}They do not punish your honesty. They do not agree to live on it, either.{/n}''', c('[End the romance route.]', flags=("closed", "parted_honestly"))),
    # end eng7-f2
], requires=("table", "trying"), delay=48)

s("a_self", "The things that are hers", "Anevia", 3,
  '"What would you like us to do with an evening that is only ours?"', [
    n("start", "Anevia", '''"Walk. Somewhere I don't have to look like I'm following anyone."
{n}You do not go far. Drezen is still Drezen, and Anevia never entirely stops reading the people around her. But she takes your arm when you offer it and lets you choose the first turning.{/n}
"Used to think freedom meant never needing anybody to know where I was. Turns out it can also mean telling someone and trusting they won't use it to keep you there."
{n}She glances at your joined arms.{/n}
"Don't get smug. You picked the street with the worst paving."''', c('"You could have warned me."', "ordinary")),
    n("ordinary", "Anevia", '''"And miss the chance to complain?"
{n}She moves closer as someone passes, then stays close after the street is clear. You stop beneath a narrow strip of sky between the buildings.{/n}
"I've spent a lot of time thinking about what I'm allowed to keep to myself. When you're good at finding secrets, people think you ought to hand over all your own as a matter of fairness."
{n}Her expression is thoughtful rather than guarded.{/n}
"I don't want us keeping the sort that takes somebody else's choice away. I do want to remain a person with a door I can close."''',
      c('"Then I will knock."', "privacy"),
      c('"Is there something you want to tell me?"', "history")),
    n("history", "Anevia", '''{n}Anevia considers the question. She makes you wait while she does.{/n}
"Maybe another night. There are things Irabeth helped me through. Things that belong to me, even though she was there. Some of them are good things. Don't give me that face like you've found a wound you need to bandage."
{n}She touches your cheek, briefly and affectionately.{/n}
"When I tell you, I want it to be because I want you to know me. Not because we've reached some point where I'm expected to unlock the last drawer."
{n}Her hand returns to your arm.{/n}
"Can that be enough?"''', c('"Yes. You don\'t have to earn your privacy."', "privacy", flags=("a_privacy",))),
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("privacy", "Anevia", '''"Good."
{n}You walk again. After a while she begins telling you about a bakery she once passed every morning. She remembers the smell more clearly than the street. She never bought anything there, and admits she used to linger outside until the proprietor chased her away.{/n}
"One day," {n}she says,{/n} "I'd like to be the sort of woman who goes in because she can. Buys the ridiculous expensive thing with the honey. Eats it before anyone can tell her she ought to save it."
{n}She looks up at you with a smile that owes nothing to concealment.{/n}
"There. A scandalous confession. Try not to spread it around."''',
      c('"I want to be there when you do."', "end"),
      c('"I could buy you a whole bakery."', "bakery")),
    # end eng7-f2
    n("bakery", "Anevia", '''"You could buy yourself a very expensive argument."
{n}She laughs and nudges your side.{/n}
"I don't want a bakery bestowed on me. I want to learn what I like doing when nobody's paying me to be useful. If I end up wanting a bakery, I'll tell you. You'll hear about flour prices until you beg for a cultist interrogation instead."''', c('"Then I\'ll start with one honey cake."', "end")),
    n("end", "Anevia", '''{n}At the end of the walk she kisses you in a doorway without first checking whether she has an alibi. She does check whether you are standing in anyone's way. Some habits, she tells you, are merely good manners.{/n}
"I had a nice evening."
{n}It is almost comically plain after everything you have said to one another. She seems pleased with the plainness.{/n}
"Let's have another."''', c('[Promise another walk.]', flags=("a_privacy",))),
], requires=("ordinary",), delay=24)

s("power", "No exception for power", "Together", 5,
  '"We should talk about what my power means for us."', [
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("start", "Irabeth", '''"Yes. We should."
{n}Irabeth does not look toward the door or lower her voice as if disagreeing with you required secrecy. Anevia notices, and seems quietly pleased.{/n}
"I have followed you through things I could scarcely have imagined when we met. That does not mean I will call every choice you make a good one."
"And if you ever start reading my mind to save yourself an awkward question," {n}Anevia adds,{/n} "we're going to have a much more awkward conversation."
{n}There is humor in it, but no uncertainty.{/n}''',
      c('"Heaven has given me power. It has not made every private choice of mine righteous."', "angel", requires=("angel",)),
      c('"Freedom matters to me. So does the freedom to refuse me."', "azata", requires=("azata",)),
      c('"I need to know you would still speak against me if judgment demanded it."', "aeon", requires=("aeon",)),
      c('"I will not use demonic power to make either of you want something."', "demon", requires=("demon",)),
      c('"There will be no bargains for your affection."', "devil", requires=("devil",)),
      c('"I am learning to live without the power I had."', "legend", requires=("legend",)),
      c('"A longer life will not make your years less important than mine."', "dragon", requires=("dragon",)),
      c('"I promise not to make your feelings the subject of a cosmic joke."', "trickster", requires=("trickster",)),
      c('"There are choices on my path that would cost me the life we are discussing."', "lich", requires=("lich",)),
      c('"Whatever power I wield, your choices remain yours."', "terms")),
    # end eng7-f2
    n("angel", "Irabeth", '''"Thank you for saying so."
{n}Irabeth touches the symbol at her breast, then lowers her hand.{/n}
"It is tempting to mistake a miracle for an answer to every question that follows it. I know that temptation well. But my faith is not a way to avoid knowing my own conduct. Nor should it become a way to excuse yours."
{n}Anevia glances between you.{/n}
"Good. Nobody gets to win an argument by glowing."''', c('[Continue.]', "terms")),
    n("azata", "Anevia", '''"Then remember that staying can be a free choice too."
{n}Anevia looks at her wife before looking back at you.{/n}
"I used freedom as a very pretty word for doing something I was afraid to discuss. Desna didn't make me do that. I did it."
{n}Her smile returns, faint but unashamed.{/n}
"I still want adventures. I also want to know who's coming home for supper. I don't think the goddess is going to be offended by supper."''', c('[Continue.]', "terms")),
    n("aeon", "Irabeth", '''"I would. I hope I would have the courage to do it even if I feared the cost."
{n}Irabeth holds your gaze.{/n}
"But I will not be evidence of your impartiality. Do not make an example of someone you love simply to prove that love has not touched your judgment. That, too, would be a kind of dishonesty."
{n}Anevia rests a hand on the table between you.{/n}
"And if your path takes you somewhere we can't follow, tell us while we're still here to hear it."''', c('[Continue.]', "terms")),
    n("demon", "Irabeth", '''"That is the beginning of the promise. It cannot be the end."
{n}Irabeth's expression is stern without becoming distant.{/n}
"I will not overlook cruelty because you have been tender to me. If the person I love harms the people I have sworn to protect, loving them will make opposing them more painful. It will not make it unnecessary."
{n}Anevia's voice is quieter.{/n}
"I grew up where powerful people found reasons for other people to suffer. Don't bring that into my home and give it a kinder name."
{n}Neither woman asks you for a performance of remorse. They ask whether you have heard them.{/n}''', c('"I have. You are not promising to excuse my actions."', "terms")),
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("devil", "Anevia", '''"No bargains means no clever wording either."
{n}Anevia leans forward.{/n}
"If you find yourself explaining why something technically wasn't a lie, stop and imagine me having a very large knife and very little patience."
"Anevia."
"A metaphorical knife."
{n}Irabeth does not look reassured.{/n}
"We are choosing a relationship," {n}she says.{/n} "Not an obligation enforceable by power. Nothing we say tonight gives you a claim upon either of us."''', c('"Agreed."', "terms")),
    # end eng7-f2
    n("legend", "Irabeth", '''"You do not have to replace it by being indispensable every hour of the day."
{n}The warning comes with a rueful smile.{/n}
"That may be advice I am particularly poorly qualified to give. I would still like you to hear it."
{n}Anevia takes your hand and turns it palm upward.{/n}
"Still yours. Still warm. I can think of things worth doing with an ordinary life."''', c('[Continue.]', "terms")),
    n("dragon", "Anevia", '''"Good. Because I'm not spendin' a year waiting for you to decide whether it's a convenient afternoon."
{n}She says it lightly, then squeezes your hand.{/n}
"I mean it. Don't start mourning me early. I intend to be a nuisance for a respectable while yet."
{n}Irabeth nods.{/n}
"And do not promise to change us so that you need never grieve. Ask us what life we want before you offer us a longer one."''', c('[Continue.]', "terms")),
    n("trickster", "Anevia", '''"Now that's a promise I'll be checking."
{n}Anevia grins, but Irabeth's expression remains serious.{/n}
"I can bear being laughed with. I have learned to bear being laughed at. I will not live with someone who cannot tell the difference when I ask them to stop."
{n}Anevia's smile gentles.{/n}
"There are enough people who deserve a ridiculous hat. You don't have to put one on every honest feeling."''', c('[Continue.]', "terms")),
    n("lich", "Irabeth", '''"Then do not ask us to wait until after you have made them to discover what they mean."
{n}Irabeth's face is pale beneath its green undertone.{/n}
"I will not call an empty imitation of tenderness enough simply because I remember the person who once offered it. I will not accept another's suffering as the price of keeping you."
{n}Anevia looks at your hands rather than your face.{/n}
"If the road takes you away from being able to want this, we don't get dragged along by a promise made before you changed. Neither do you."''', c('"I understand what I stand to lose."', "terms")),
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("terms", "Narrator", '''{n}Power has not made the conversation easy. It has merely made avoiding it more dangerous. You answer their concerns without requiring admiration in return.{/n}
"We are not promising never to be afraid," {n}Irabeth says.{/n} "We are promising to speak when we are."
"And you're promising to listen before you decide we just don't understand," {n}Anevia adds.{/n}
{n}When you agree, neither woman treats the matter as settled forever. They do, however, move their chairs closer. For tonight, being able to have the conversation is enough.{/n}''',
      c('"Hold me to that."', flags=("power_terms",)),
      c('"I cannot accept those limits."', "stop")),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("stop", "Irabeth", '''"Then we cannot offer you this relationship."
{n}There is sorrow in Irabeth's voice. There is no invitation to negotiate. Anevia stands beside her, close enough that their shoulders touch.{/n}
"We meant what we said," {n}Anevia tells you.{/n} "It wasn't a way of asking you to make us feel better."''', c('[End the romance route.]', flags=("closed",))),
    # end eng7-f2
], requires=("return",), delay=24)

s("future", "A door worth coming home through", "Together", 5,
  '"When the war is over, what would you want our life to look like?"', [
    n("start", "Anevia", '''"A window that opens."
{n}Anevia answers before you have finished asking. Irabeth gives her an affectionate, exasperated look.{/n}
"That is not the entirety of our plans."
"It was going to be my opening demand. We can negotiate up from there."
{n}They have brought a sheet of paper. No map of enemy positions, no requisitions. Just a few untidy lines about places they might like to see and things they might like to have.{/n}
{n}There is room left for your handwriting.{/n}''', c('[Add something you would like.]', "room")),
    n("room", "Irabeth", '''"I would like a room where taking off my armor means I am finished for the day. Usually, at least."
{n}She smiles at her own qualification.{/n}
"I would like work that matters without pretending every other thing must wait until it is done. And I would like to learn how to be present when nothing is wrong."
{n}Anevia lays a hand over hers.{/n}
"I'd like you to stop saying that as if you're applying for a post."
"I am aware that I require practice."
"Good. We'll be very demanding employers."''', c('"And what do you want, Anevia?"', "own")),
    n("own", "Anevia", '''"A kitchen I know how to use. Friends who don't have to begin every visit by asking whether this is a bad time. A bit of money that isn't already promised to somebody's armor repairs."
{n}She looks at Irabeth with such obvious affection that the complaint becomes an old familiar joke.{/n}
"And days when I can be away from both of you without somebody deciding it means I've stopped loving you. I don't want to have to choose between belonging and being able to breathe."
{n}Irabeth nods.{/n}
"I would like that for all of us."''',
      c('"A home, with room for each of us to leave and return."', "choice"),
      c('"I may still have other people and duties in my life."', "others")),
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("others", "Irabeth", '''"So will we."
{n}Irabeth's answer is gentle.{/n}
"I do not mean that those attachments will be identical. Only that none of us is arriving without a life. We cannot ask you to have no claims upon your time except ours while keeping all of our own."
"We can ask you to remember we exist when we're not in the room," {n}Anevia says.{/n} "And we can do the same for whoever else matters to you. That's a start."''', c('"Then let us plan honestly around the lives we have."', "choice", flags=("other_loves",))),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("choice", "Narrator", '''{n}You discuss where you might live and discover that all three of you have strong opinions about stairs. You discuss money without allowing your rank to end the conversation. You discuss whether a public announcement would be courage or merely an efficient way to make other people unbearable.{/n}
"We can tell the people who need to know," {n}Anevia says.{/n} "Everybody else can survive wondering."
{n}Irabeth agrees, then looks at you with a seriousness that quiets the room.{/n}
"We would like you in that life. I would. Anevia would. We have had time to find out whether that is only gratitude, or fear, or the wish to make what happened less shameful. It is more than those things."
{n}Anevia meets your eyes.{/n}
"We want you. With us. Do you want that too?"''',
      c('"Yes. I choose a life with you both."', "yes", flags=("committed",)),
      c('"I love you, but I cannot promise that life."', "no")),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("yes", "Narrator", '''{n}Anevia lets out a breath she had been pretending not to hold. Irabeth reaches for you, then for her wife, drawing the three of you close enough that the table becomes an inconvenience.{/n}
"We should move that," {n}Anevia murmurs.{/n}
"The table?"
"Eventually. I was having a moment."
{n}You laugh, all three of you. When the laughter passes, no one immediately lets go.{/n}
{n}There is no new oath before a temple, no witness empowered to make the choice permanent. There are three people who have learned something of the harm they can do, and who are choosing to attempt something kinder. For tonight, they trust each other enough to begin.{/n}''', c('[Stay with them.]')),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("no", "Narrator", '''{n}Irabeth's hand pauses before reaching yours. Anevia looks at the space you have left on the paper.{/n}
"Then it is better that we know," {n}Irabeth says.{/n}
{n}You speak for a while longer, without trying to make the ending painless. When you leave, the paper remains on the table. They still have a future to write upon it.{/n}''', c('[End the romance route.]', flags=("closed", "parted_honestly"))),
    # end eng7-f2
], requires=("power", "a_self", "i_self", "power_terms"), delay=48)

s("shared_night", "No one at the door", "Together", 5,
  '"I would like an evening with you both. No promises beyond tonight."', [
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("start", "Narrator", '''{n}Anevia opens the door before you knock a second time. For an instant the old habit returns: a quick glance down the passage, a check of who might have seen you arrive. Then she catches herself and steps aside with a smile.{/n}
"Come in. We were arguing about the wine."
"I said it was quite good," {n}Irabeth explains.{/n}
"She's trying to spare its feelings."
{n}The room is warm. There are three cups, a small plate of food, and no convincing attempt to disguise the evening as anything else.{/n}''', c('[Join them.]', "near")),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("near", "Anevia", '''"Before anybody gets impressive," {n}Anevia says,{/n} "we can have a nice evening and leave it at that."
{n}She looks at Irabeth as she says it, then at you.{/n}
"I know we all agreed. I want to know we still mean it when we're here, and somebody's looking hopeful."
{n}Irabeth sets her cup down.{/n}
"I mean it. I am also looking hopeful. Both can be true."
{n}Anevia's laughter is soft. She leans over and kisses her wife. When they part, she reaches for your hand rather than assuming you will move closer.{/n}''',
      c('[Take her hand and kiss each woman in turn.]', "close"),
      c('"Tonight I would rather just be close to you."', "quiet")),
    # end eng7-f2
    n("close", "Narrator", '''{n}At first the unfamiliarity makes all three of you careful. Then Anevia says something irreverent against Irabeth's cheek, Irabeth laughs, and the carefulness goes out of the room like a draught when a door shuts.{/n}
{n}Anevia gets to your buttons first. She has spy's fingers and no patience, and she kisses you while she works, hard, tasting of the wine she said was only quite good. Behind you Irabeth's hands settle on your hips, big and warm, and her mouth finds the back of your neck.{/n}
"Still all right?" Irabeth asks, low, against your skin.
"Beth," Anevia says, "if you ask that one more time I'm puttin' you on report."
{n}You answer her with your mouth on Anevia's. Irabeth's laugh shakes through both of you. Then the three of you are down on the cushions in a tangle of half-shed clothes, Anevia pulling you over her by the collar, Irabeth's weight settling warm along your back, and Anevia's heel hooks round your leg to keep you exactly where she wants you.{/n}''', c('[Let the night remain private.]', "morning")),
    n("quiet", "Narrator", '''{n}Irabeth draws you close. Anevia settles against her other side, then complains that someone has arranged the cushions with military efficiency and no concern for comfort.{/n}
{n}The three of you spend several minutes correcting this injustice. By the time you are satisfied, Anevia is laughing and Irabeth has abandoned any claim to dignity. You talk until conversation gives way to drowsiness.{/n}
{n}No one asks whether you are certain about what you declined. The warmth offered afterward is no less generous for it.{/n}''', c('[Stay until morning.]', "morning")),
    n("morning", "Narrator", '''{n}Morning brings a familiar problem. Irabeth is trying to rise without waking anyone. Anevia catches her wrist without opening her eyes.{/n}
"If the city isn't on fire, five minutes."
"I was going to fetch water."
"A dangerously convincing excuse."
{n}You make room, and Irabeth stays. Light creeps across the floor. Somewhere outside, the ordinary machinery of Drezen begins another day.{/n}
{n}Anevia opens one eye and looks toward the door. Then she closes it again. There is no one she needs to deceive about where she has spent the night.{/n}''', c('[Enjoy the five minutes.]', flags=("shared_evening",))),
], requires=("future", "committed"), delay=24)

s("last_watch", "Until the last watch ends", "Together", 5,
  '"Before the final battles, there are things I want to say."', [
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("start", "Narrator", '''{n}You have all become skilled at pretending that practical preparations are enough. There is always another report, another strap to mend, another person who needs an answer. Tonight you leave those things unfinished long enough to sit together.{/n}
"I don't want a farewell speech," {n}Anevia says.{/n} "I've heard officers make 'em. They always sound as if they've already decided who gets to be brave and who gets to grieve."
{n}Irabeth's hand tightens around hers.{/n}
"Then let us speak as people who would prefer to come home."''',
      c('"I want the life we planned. I will fight for the chance to live it."', "life"),
      c('"If I do not return, I want you to keep living."', "after")),
    # end eng7-f2
    n("after", "Anevia", '''"We will. Badly, some days, if it comes to that."
{n}Anevia's voice catches, but she does not look away.{/n}
"Don't ask us to promise we'll do it beautifully. I might be very unreasonable for a while."
{n}Irabeth rests her forehead briefly against her wife's temple, then turns to you.{/n}
"We understand what you mean. I would ask the same of you. Remember us as people who wanted to live, not as instructions to spend the rest of your life mourning correctly."''', c('"I will remember."', "life")),
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("life", "Irabeth", '''"Then there is something I should admit."
{n}Irabeth looks almost embarrassed.{/n}
"I have been adding places to the list. For afterward. More than we could visit in a year."
"More than we could visit in five," {n}Anevia says.{/n} "She has opinions about lakes now."
{n}Irabeth smiles through the fear neither woman is hiding very well.{/n}
"I would like the chance to be disappointed by at least one of them. To arrive and discover that the poet exaggerated, and complain about the road, and be happy anyway."
{n}She takes your hand.{/n}
"I have never wanted an ordinary disappointment so much."''', c('"Keep the list. We will need it."', "end")),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("end", "Narrator", '''{n}There are kisses, and a laugh that breaks in the middle, and a long silence in which none of you pretends to have become fearless. You remain together until the next necessary thing can no longer wait.{/n}
{n}At the door, Anevia turns back.{/n}
"A window that opens," {n}she reminds you.{/n} "Don't let her replace it with a defensible arrow slit."
"I have made no such proposal."
"Yet."
{n}You leave them laughing quietly together. You carry the sound with you into the preparations that remain.{/n}''', c('[Return to the crusade.]', flags=("last_words",))),
    # end eng7-f2
], requires=("future",), delay=24)

s("ending_together", "Three at the table", "Epilogue", 0, "", [
    n("end", "Narrator", '''{n}When the war released its hold upon them, Anevia and Irabeth discovered that peace required skills for which the Eagle Watch had provided remarkably little training. Irabeth could still turn a visit to the market into a supply inspection. Anevia could still learn an entire street's secrets before remembering what she had gone there to buy.{/n}
{n}The Commander found a place in their life by returning to it, again and again. Their home acquired a third chair that was nobody's guest chair. It also acquired arguments about time, money, wet boots, and whether an unanswered question counted as an answer. The old betrayals were not forgotten. They became things the three could name without allowing them to name everything else.{/n}
{n}They kept private evenings as carefully as shared ones. Other duties and attachments were discussed rather than concealed. Irabeth learned to set down her work before exhaustion made the decision for her. Anevia learned to bake bread which even an honest person could praise. The Commander learned which promises mattered most when no one was watching.{/n}
{n}Visitors sometimes arrived hoping for a scandalous account of the arrangement. They usually left with a full stomach, several opinions about window repairs, and the disconcerting impression that three people had made an ordinary happiness out of something they had once handled very badly.{/n}'''),
], requires=("committed",), forbids=("closed", "irabeth_dead", "anevia_dead", "irabeth_gone", "anevia_gone", "swarm", "true_lich", "sacrifice", "ascend_all", "ascend_alone", "ascend_areelu", "ascend_companions"), last=99)

s("ending_apart", "What they chose to keep", "Epilogue", 0, "", [
    n("end", "Narrator", '''{n}The life the Commander, Anevia, and Irabeth had imagined together did not become the life they lived. Affection had been real. So had the harm. Neither truth proved sufficient to erase the other.{/n}
{n}Anevia and Irabeth kept the work of their marriage between themselves. They had learned the cost of assuming that love made honesty unnecessary, and the equal cost of using honesty only when there was nothing left to hide. Some conversations remained difficult long after the war ended. They had more of them anyway.{/n}
{n}In time, the Commander's name could be spoken without every room growing quiet. There were things to remember kindly, and things neither woman excused. Their memories made room for both.{/n}'''),
], requires=("reckoning", "closed"), forbids=("irabeth_dead", "anevia_dead", "irabeth_gone", "anevia_gone", "swarm", "true_lich", "sacrifice", "ascend_all", "ascend_alone", "ascend_areelu", "ascend_companions"), last=99)

s("ending_unfinished", "Words left unfinished", "Epilogue", 0, "", [
    n("end", "Narrator", '''{n}The war ended before the Commander and the two women had made a shared life of what passed between them. There had been tenderness, hesitation, and promises whose meaning remained unsettled. Peace did not settle them by decree.{/n}
{n}Anevia and Irabeth returned to the life they had built together. Whatever place the Commander might once have taken in it remained a question rather than a claim. Neither woman mistook an unfinished possibility for an obligation to wait forever.{/n}
{n}Some evenings were remembered with warmth. Others with regret. No single account of the crusade contained all of either.{/n}'''),
], requires=("a_affair", "i_affair"), forbids=("committed", "closed", "irabeth_dead", "anevia_dead", "irabeth_gone", "anevia_gone", "swarm", "true_lich", "sacrifice", "ascend_all", "ascend_alone", "ascend_areelu", "ascend_companions"), last=99)

s("ending_loss", "An empty place", "Epilogue", 0, "", [
    n("end", "Narrator", '''{n}War had taken from the three a future they had scarcely learned to imagine. The private hopes they had once spoken aloud survived only in fragments: an ordinary room, a book left open, a cup set out before its owner remembered.{/n}
{n}No promise made in tenderness overruled the loss. No intimacy changed the choices that had brought them to it. Those who remained were left with the difficult freedom of deciding what to do with love that could no longer be returned in the way they had wished.{/n}
{n}The crusade's histories preserved victories and sacrifices. They had little room for the smaller things that made the sacrifices unbearable.{/n}'''),
], requires=("a_affair", "i_affair", "loss"), forbids=("swarm", "true_lich", "ascend_all", "ascend_alone", "ascend_areelu", "ascend_companions"), last=99)

s("ending_ascend", "Beyond the promised years", "Epilogue", 0, "", [
    n("end", "Narrator", '''{n}The Commander's ascent made ordinary plans seem very small. It did not make them meaningless. Anevia regarded eternity as a poor excuse for missing supper. Irabeth was less amused by the prospect of every disagreement acquiring a congregation.{/n}
{n}Neither mistook divinity for agreement. Whatever reach the Commander's new existence permitted, affection could not be commanded into permanence. The women kept their own choices, their own work, and the right to welcome or refuse a presence that the world had begun to treat as beyond refusal.{/n}
{n}Among the grand claims later made about the Commander's nature, there was a quieter story. It concerned someone who had once learned, with considerable difficulty, to arrive when expected and speak honestly at a table meant for three. Whether told as a memory or a hope, it was a story neither woman allowed the worshipers to improve.{/n}'''),
], requires=("committed", "ascended"), forbids=("closed", "irabeth_dead", "anevia_dead", "irabeth_gone", "anevia_gone"), last=99)

s("ending_monster", "The person they had known", "Epilogue", 0, "", [
    n("end", "Narrator", '''{n}The life once imagined at a small table in Drezen did not survive what the Commander became. Its failure could not be blamed on insufficient devotion. Some choices destroy the conditions in which affection can remain a choice at all.{/n}
{n}There had been moments when Anevia and Irabeth saw someone they could want without fear. Those moments belonged to the past. They did not grant the present a claim upon either woman, and no remembered tenderness absolved the power that outlived it.{/n}'''),
], requires=("a_affair", "i_affair", "inhuman"), last=99)

s("ending_aeon", "A life not remembered", "AeonEpilogue", 0, "", [
    n("end", "Narrator", '''{n}In a world from which the wound had been removed, the Commander's private history with Anevia and Irabeth had no place to have happened. There was no affair to confess, no room where three frightened people learned to speak plainly, no promise whose keeping could restore what time itself had undone.{/n}
{n}Whatever lives the women lived in that altered world belonged to them. The erased Commander could claim neither their memory nor their love as a reward for making it possible.{/n}
{n}If some trace of the old world remained beyond the reach of recollection, it was not a summons. It was the shape of an empty chair in a room that had never existed.{/n}'''),
], requires=("a_affair", "i_affair"), last=99)


def make_story():
    etudes = json.loads((ROOT / "data/etudes.json").read_text(encoding="utf-8"))
    aliases = {
        "anevia_dead": "AneviaDead", "irabeth_dead": "IrabethDead",
        "anevia_gone": "AneviaGone", "irabeth_gone": "IrabethGone",
        "irabeth_away": "IrabethNotInDrezenCh5_WithGalfrey", "anevia_away": "AneviaNotInDrezen",
        "broken": "IrabethBroken_Chapter03", "encouraged": "IrabethEncouraged_Chapter03",
        "angel": "PlayerIsAngel", "azata": "PlayerIsAzata", "aeon": "PlayerIsAeon",
        "demon": "PlayerIsDemon", "devil": "PlayerIsDevil", "dragon": "PlayerIsDragon",
        "legend": "PlayerIsLegend", "trickster": "PlayerIsTrickster", "lich": "PlayerIsLich",
        "true_lich": "MythicLich_TrueLich", "swarm": "PlayerIsLocust",
    }
    refs = {key: etudes[name] for key, name in aliases.items()}
    refs.update(sacrifice="381a296094804761af0893d2e70dc2df",
                ascend_all="07ad18ffb08145b69522f8eee0230857", ascend_alone="08e47548e25945e286fe77b896884b32",
                ascend_areelu="63279a971792474ba0439b9f75795a7a", ascend_companions="9fc5161813f1497f8eaad1563ac54211")
    return dict(Scenes=scenes, Etudes=refs)


def build():
    payload = make_story()
    (ROOT / "package/Story.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    words = sum(len(node['Text'].split()) + sum(len(c['Text'].split()) for c in node['Choices']) for scene in scenes for node in scene['Nodes'])
    print(f"{len(scenes)} scenes, {sum(len(s['Nodes']) for s in scenes)} pages, {words:,} words")


s("i_self", "A strength she can set down", "Irabeth", 3,
  '"Would you spend this evening with me, without finding work for us?"', [
    n("start", "Irabeth", '''{n}Irabeth arrives carrying a book. She looks at it, then at you, and laughs in embarrassment.{/n}
"It is not a tactical manual. I thought I should establish that immediately."
{n}It is a battered collection of travelers' accounts. Several pages have come loose. She has marked a description of a lake with a strip of spare cloth.{/n}
"I used to imagine visiting places like this. Then I acquired a very impressive list of reasons not to. Some were even good reasons."''', c('"Read it to me."', "lake")),
    n("lake", "Irabeth", '''{n}Her reading is careful at first. She gives every sentence the weight of testimony. When the writer grows extravagantly sentimental about the moon on the water, she stops and looks at you.{/n}
"I had forgotten how bad this part was."
{n}You laugh together. She tries the passage again in the grand voice it appears to require and makes herself laugh so hard that she loses her place.{/n}
"Anevia must never hear that."
{n}Then she considers.{/n}
"No. She should. She will be unbearable about it, but she should."
{n}She puts the book aside and sits nearer to you.{/n}''', c('"I like hearing you laugh."', "seen")),
    n("seen", "Irabeth", '''"I like not wondering whether I look foolish when I do."
{n}She runs a finger along the loose binding.{/n}
"People have decided many things about me before I spoke. That I would be violent. That I would be stupid. Sometimes, after I proved them wrong, that I ought to be endlessly grateful for the opportunity."
{n}She speaks matter-of-factly, but her shoulders have tightened.{/n}
"I learned to be very careful about what I showed. Even kindness can become another examination. Am I gentle enough? Noble enough? A sufficiently reassuring exception?"
{n}She looks at you directly.{/n}
"I do not want to be an exception here. I would like to be a woman having a rather pleasant evening."''',
      c('"Then come closer. The evening isn\'t over."', "touch"),
      c('"You don\'t have to make yourself smaller with me."', "touch")),
    n("touch", "Irabeth", '''{n}She takes your hand and brings it to her cheek. It is a request, unmistakable and unhurried. You trace the edge of her jaw lightly, and she closes her eyes.{/n}
"Anevia tells me that I sometimes accept tenderness as if it were medical treatment. Something necessary which I should endure without complaint."
{n}Her smile returns beneath your hand.{/n}
"I am attempting to improve."
{n}She catches your sleeve when you draw back, kisses you again, and leaves her hand warm against your neck.{/n}''',
      c('[Spend the rest of the evening close to her.]', "end"),
      c('"Read me another terrible passage first."', "read")),
    n("read", "Irabeth", '''"You have a cruel streak."
{n}She retrieves the book without moving away from you. The next passage compares a sunrise to a maiden's blush. Irabeth gives you a flat look and turns the page.{/n}
"We will spare each other that one."
{n}By the time the lamp needs trimming, you have learned very little about the lake and rather more about her sense of humor.{/n}''', c('[Enjoy the evening.]', "end")),
    n("end", "Irabeth", '''{n}Later, she leaves the book in your keeping, with the cloth marker still between its pages.{/n}
"I should like us to go somewhere after all this. Somewhere whose strategic importance nobody has explained to me."
{n}She considers the request, then adds with unexpected firmness:{/n}
"And I should like to choose some of the places."
{n}You promise her that much. Her expression suggests that, of all the assurances you have given her, this small one has found a particularly tender place.{/n}''', c('"We will make the list together."', flags=("i_seen",))),
], requires=("ordinary",), delay=24)

s("departure", "Before the descent", "Together", 3,
  '"Before the next campaign takes me away, I want an evening with you both."', [
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("start", "Narrator", '''{n}Drezen is full of preparations. Orders travel faster than rumors for once, though the rumors are doing their best. You find Anevia and Irabeth arguing over how much can reasonably be fitted into a travel pouch.{/n}
"It is a sensible precaution," {n}Irabeth says.{/n}
"It's a second cupboard with a strap."
{n}They stop when they see you. Anevia holds up the pouch.{/n}
"We've been making ourselves useful. You should probably intervene before we add a chair."''', c('"What have you put in it?"', "gifts")),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("gifts", "Narrator", '''{n}A small sewing kit. A clean cloth. Something edible wrapped with considerably more care than its appearance warrants. A whetstone that Irabeth insists is better than the one you have been using. None of it comes from crusade stores.{/n}
"There is no charm in it," {n}Irabeth says.{/n} "No blessing I can promise will keep you safe."
"Just things that'll annoy you into remembering us," {n}Anevia adds.{/n}
{n}Her voice is light until she looks at the pouch in your hands.{/n}
"We're bad at this part. The waiting. You'll have noticed."''', c('"I cannot promise when I will return."', "promise")),
    # end eng7-f2
    n("promise", "Irabeth", '''"Then do not."
{n}Irabeth reaches for Anevia's hand before she takes yours.{/n}
"Promise that when you can tell us the truth, you will. We can endure uncertainty better than an assurance we know you cannot keep."
{n}Anevia nods, though her eyes are bright.{/n}
"And if I leave a letter in your things, don't read it in front of the entire camp. I have a professional reputation."
"It is a very affectionate letter."
"Irabeth."
{n}The laughter breaks before it becomes entirely convincing. You hold them both until no one feels obliged to make it sound better.{/n}''',
      c('"I will carry you with me."', "end"),
      c('[Kiss them each goodbye.]', "end")),
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("end", "Narrator", '''{n}You spend the evening together. There are things left unsaid, but none of them is a deliberate deception. At the door Anevia straightens your collar, then immediately complains that Irabeth has taught her to fuss.{/n}
"Take care of yourself," {n}she says.{/n} "Not just the useful bits. All of you."
{n}Irabeth's farewell is quieter.{/n}
"Come back if you can. We will still be people while you are gone. I hope you remember that as a comfort."
{n}You take the pouch. It is heavier than it looks.{/n}''', c('[Prepare to leave.]', flags=("farewell",))),
    # end eng7-f2
], requires=("table",), delay=24, last=3)

s("abyss_letter", "A letter with no messenger", "Memory", 4, "", [
    n("start", "Narrator", '''{n}Even at rest, the Abyss refuses to be quiet in a familiar way. A distant cry might be laughter, pain, or a merchant advertising something best left unnamed. You turn a scrap of paper over in your hands. There is no reliable messenger to whom you would entrust it.{/n}
{n}You begin a letter anyway.{/n}
{n}Anevia's name comes first. Then Irabeth's. You stare at the two names together. At home, saying them in the same breath has become complicated. Here, the simple fact that both women exist somewhere beyond this place feels almost unbearably precious.{/n}''',
      c('[Write about something ordinary you miss.]', "ordinary"),
      c('[Write what you failed to say before leaving.]', "unfinished")),
    n("ordinary", "Narrator", '''{n}You write about cold tea. A glove repaired badly, then repaired again. The way Anevia notices a joke approaching and tries not to help it along. Irabeth pretending she does not know that her wife has stolen something from her plate.{/n}
{n}It is a ridiculous letter from the Abyss. Nothing about the strength of the enemy, the strange geometry of the streets, or how easily cruelty becomes entertainment here. You have reports enough for those things.{/n}
{n}For this page, you want to remember what you are trying to return to.{/n}''', c('[Continue writing.]', "truth")),
    n("unfinished", "Narrator", '''{n}At first you write an apology. Then you cross out the part that asks them to reassure you. You try again, describing something you did rather than something you hope they will believe about you.{/n}
{n}The words become less impressive and more difficult to write. You discover how often a declaration of affection can be used to avoid a plain account of conduct.{/n}
{n}You keep the plain account. There is no one here to reward you for it. Perhaps that is why it feels worth keeping.{/n}''', c('[Continue writing.]', "truth")),
    n("truth", "Narrator", '''{n}You cannot know how things stand between them tonight. You cannot write their answer for them. Beyond the walls of your refuge, the Abyss offers a thousand ways to confuse appetite with entitlement. On this little page, you try to keep the distinction clear.{/n}
{n}You fold the letter instead of burning it. If you return, there may be a time to read it aloud. If you do not, at least this much of the truth exists somewhere outside your thoughts.{/n}''', c('[Keep the unsent letter.]', flags=("wrote_letter",))),
], requires=("a_affair", "i_affair"), last=4)

s("abyss_dream", "The empty chair", "Memory", 4, "", [
    n("start", "Narrator", '''{n}Sleep brings you a room with three chairs. It is not quite any room you remember. The light is wrong, and the window looks onto a street that should not be visible from Drezen. Dreams have never respected a map.{/n}
{n}Anevia is speaking, but you cannot hear the words. Irabeth has a book open across her knees. There is a place for you. When you move toward it, the floor lengthens like one of Alushinyrra's treacherous streets.{/n}
{n}You wake before you reach them.{/n}''', c('[Sit with the memory.]', "awake")),
    n("awake", "Narrator", '''{n}For a moment you are angry with the dream for promising something it could not give. Then you remember that no promise was made. A chair was empty. You supplied the rest.{/n}
{n}You take out the letter and add a line: "I miss you. I know that does not tell me what you need from me."{/n}
{n}You consider writing more. Instead you put the paper away and do something practical for the person who must eventually carry it home. Eat. Mend a strap. Rest another hour if you can.{/n}
{n}For once, taking care of yourself feels less like an interruption to the crusade than a promise you are capable of keeping.{/n}''', c('[Rest.]', flags=("kept_letter",))),
], requires=("abyss_letter",), delay=48, last=4)

s("a_waiting", "The place beside her", "Anevia", 5,
  '"You keep looking toward the door. Are you thinking about Irabeth?"', [
    n("start", "Anevia", '''"That's an easy guess."
{n}Anevia looks toward the door once more, catches herself, and gives you a tired smile.{/n}
"I'm glad you're here. I am. But some of what I want to say needs her in the room. I won't make you her substitute just because you're the person I can reach."
{n}Her fingers tap against the table, a quick uneven rhythm.{/n}
"You'd think being good at finding people would make waiting for one easier. It doesn't."''', c('"We can wait without pretending it is easy."', "end")),
    n("end", "Anevia", '''{n}You stay awhile. Anevia speaks about the practical business of keeping people fed, informed, and alive. Eventually she stops turning every sentence into evidence that she has been coping well.{/n}
"I don't need you to promise me she'll be all right. Just don't talk about the future as if she's already safely in it."
{n}You agree. When you leave, she thanks you for the company without apologizing for what she could not offer.{/n}''', c('[Let the reunion wait until everyone is present.]')),
], requires=("a_affair", "irabeth_away"))

s("return", "People who kept living", "Together", 5,
  '"Can we make time for one another again?"', [
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("start", "Narrator", '''{n}The three of you sit together with the door closed. It ought to be a familiar arrangement by now. Instead you find yourselves looking carefully at one another, as if a careless assumption might undo the effort that brought you here.{/n}
"I had a speech," {n}Anevia says.{/n} "Very good one. You'd have been impressed."
"What happened to it?" {n}Irabeth asks.{/n}
"People kept turning out to be more complicated than I'd allowed for. Inconsiderate of them."
{n}She looks at you, then at her wife, and her smile softens.{/n}''',
      c('[Show them the letter you wrote in the Abyss.]', "letter", requires=("wrote_letter",)),
      c('"Tell me how you are now, not how you think I need you to be."', "now")),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("letter", "Narrator", '''{n}You put the folded page on the table. Anevia recognizes neither the paper nor the handwriting's hurried slant, but she understands its condition. She handles it as carefully as she would a report that cost someone's life to carry.{/n}
{n}Irabeth reads it slowly, smoothing a crease with her thumb. She stops before the last line and looks at you.{/n}
"You kept this all that time?"
{n}Anevia finishes first, then returns to the beginning.{/n}
"This is a very bad military report," {n}she says.{/n} "No useful intelligence at all."
{n}She keeps the paper between her palms until she is ready to hand it to her wife.{/n}''', c('"It was not written for the officers."', "now")),
    # end eng7-f2
    n("now", "Irabeth", '''"Some things are better. Some are not. I would rather tell you which than make you guess."
{n}Irabeth does. Anevia corrects one detail and supplies another. They disagree briefly, listen, and continue. You realize that their ability to do so is something they have practiced when you were not there.{/n}
"We didn't spend every evening discussing you," Anevia says. "That'd have been a miserable way to stay married."
{n}The remark is affectionate, but the point beneath it is serious.{/n}
"We have been learning to ask each other for things," Irabeth adds. "Without first explaining why the request is reasonable enough to deserve an answer."''',
      c('"I want to know the people you are becoming."', "future"),
      c('"I hoped things could go back to how they were."', "back")),
    n("back", "Anevia", '''"Some of it can. The good bits."
{n}Anevia leans toward you.{/n}
"But don't ask us to stand exactly where you left us. I wouldn't ask that of you. Even if I miss somebody you used to be."
{n}Irabeth takes your hand.{/n}
"There is room to be glad of what remains and curious about what has changed."''', c('"Then tell me what you want next."', "future")),
    n("future", "Narrator", '''{n}The answer is not a grand one. Time together that is actually kept. A conversation about what your power means now. A chance to make a plan that reaches beyond the next military report without pretending the war will respect it.{/n}
{n}Before you leave, Anevia asks whether she may kiss you. You are surprised by the question until you see that she wants the pleasure of an answer freely given, without relying on what was once understood.{/n}
{n}You answer. Irabeth watches with a tenderness that still contains effort, then draws you close in her turn. Nobody is being left outside the room.{/n}''', c('[Begin again from where you actually are.]')),
], requires=("ordinary",), delay=24)


s("parting", "An answer that can change", "Together", 3,
  '"I need to talk about whether I can remain in this relationship."', [
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("start", "Narrator", '''{n}They listen without interrupting. Anevia's hand has gone still on the table. Irabeth sits a little straighter, then deliberately lets her shoulders relax.{/n}
"Is this something you need us to hear," {n}Irabeth asks,{/n} "or something you have already decided?"
{n}Anevia looks at you steadily.{/n}
"Either way, say it. We didn't promise to keep you by making it impossible to leave."''',
      c('"I have decided. I want to end our romantic relationship."', "confirm"),
      c('"I am overwhelmed, but I still want to be with you. I needed to be able to say it."', "stay")),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("confirm", "Irabeth", '''"Then we accept your decision."
{n}Her voice is careful. Beside her, Anevia draws a slow breath.{/n}
"Give us a little distance," {n}Anevia says.{/n} "I don't want to promise we'll all be easy friends tomorrow just to make the ending nicer. But I don't want you punished for telling us, either."
{n}You say goodbye to the part of your lives you had hoped to share. The work of the crusade remains, as do the things you have learned about one another. Neither is a reason to pretend that nothing has ended.{/n}''',
      c('[End the romance route.]', flags=("closed", "parted_honestly"))),
    # end eng7-f2
    # eng7-f2: narration markup; wording, answers and effects retained.
    n("stay", "Anevia", '''"All right. Then we can talk about being overwhelmed."
{n}Anevia's shoulders loosen. Irabeth reaches for your hand and waits for you to decide whether to take it.{/n}
"You do not have to threaten to leave in order to ask for something to change," {n}Irabeth says.{/n} "But you must also be able to tell us when you are considering it."
{n}The conversation is difficult and useful. You leave with the relationship still intact, and with a little less fear of saying something inconvenient inside it.{/n}''', c('[Continue the relationship.]', abort=True)),
    # end eng7-f2
], requires=("trying",), optional=True)


if __name__ == "__main__":
    build()

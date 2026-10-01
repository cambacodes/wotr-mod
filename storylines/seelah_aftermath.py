"""Authored Chapter 5 incidents and faith conversations; no native quest mutation."""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, entry, nodes, requires=(), delay=24):
    for node in nodes:
        node["Portrait"] = "Seelah"
    SCENES.append(scene("seelah." + id, title, "Seelah", 5, entry, nodes,
                        Relationship="seelah", AnswerLists=["417fa384f3250634bb71859fbc913453"],
                        Areas=[DREZEN], Chapters=[5], requires=("seelah.courting", "seelah.weight", *requires),
                        forbids=("inhuman", "seelah.farewell", "seelah_dead", "seelah_gone"),
                        ForbidOverrides={"seelah.farewell": "seelah.catchup_requested"},
                        optional=True, delay=delay))


s("borrowed_saw", "The missing teeth", '"You said you wanted a second pair of hands."', [
    n("start", "Seelah", '''{n}Seelah has a strip of wood tucked under one arm. Someone has drawn a wavering line along it, then crossed it out and drawn another.{/n}
"Preferably hands that know which end of a saw to hold. I offered to fix a washing platform. Splitting wood? Easy. Cutting two boards the same length? Apparently that's a whole other profession."
{n}She turns the strip over.{/n}
"Mera is teaching me. She's the carpenter. Orsa does the washing. They've both said you can come, provided you don't mind being told where to stand."''',
      c('[Go with her to the washing yard.]', "yard"),
      c('"I cannot help today. Do not wait for me."', abort=True)),
    n("yard", "Narrator", '''{n}Water runs through a stone gutter beside the washing yard. The platform over it has been lifted away, leaving the supports exposed. Two women stand on opposite sides of the opening. Mera, broad-shouldered and gray at the temples, has her tool roll open. Orsa has rolled her sleeves above weathered elbows, though her hands are dry.{/n}
{n}"The saw," Mera says. "That was the agreement. Borrow it yesterday, return it before I start today."{/n}
{n}"I know." Orsa looks at Seelah. "I was going to explain."{/n}
{n}Seelah draws breath to speak, then looks at Orsa's empty hands.{/n}''',
      c('[Touch Seelah\'s wrist twice, as you agreed.]', "signal", requires=("seelah.check_signal",), flags=("seelah.saw_listened",)),
      c('[Watch the women with her before either of you intervenes.]', "person", requires=("seelah.check_person",), forbids=("seelah.check_signal",), flags=("seelah.saw_listened",)),
      c('[Wait for Seelah to ask Orsa what happened.]', "need", requires=("seelah.knows_need",), forbids=("seelah.check_signal", "seelah.check_person"), flags=("seelah.saw_listened",)),
      c('[Listen as Seelah steps into the conversation.]', "hasty_start", forbids=("seelah.check_signal", "seelah.check_person", "seelah.knows_need"))),
    n("signal", "Seelah", '''{n}At the second tap she stops and turns toward you. Then she looks at Mera, taking in the open tool roll.{/n}
"Right. Frightened voice, sword out. Except nobody's drawn a sword, and I haven't even asked about the saw."
{n}She sets down the strip of wood and turns to Orsa.{/n}''', c('[Let Mera explain the loan.]', "listened")),
    n("person", "Seelah", '''{n}Seelah follows your attention from Orsa to the carpenter. Mera has left a space in the tool roll for the missing saw. She keeps touching it as though the tool might appear there.{/n}
"We should hear what happened before I start making offers," Seelah says. "Mera?"
{n}Orsa lets out a breath. Seelah glances from her to the empty slot in Mera's tool roll.{/n}''', c('[Ask Mera about the borrowed saw.]', "listened")),
    n("need", "Seelah", '''"Orsa, what's happened? Want me to help you tell it?"
{n}The washer shakes her head, then looks toward the washhouse.{/n}
{n}"I need to fetch it. I was hoping I wouldn't have to show everyone."{/n}
"Then we'll wait. Mera, tell me what you agreed."
{n}Seelah puts the wood down and settles on her heels beside the drain.{/n}''', c('[Wait with her.]', "listened")),
    n("listened", "Narrator", '''{n}"I lent it for a shelf," Mera says. "She was to bring it back before I began this platform. It isn't a shared tool. I earn my living with it."{/n}
{n}Seelah nods, then turns to Orsa. "We won't know what to do until we see it."{/n}
{n}Orsa looks at Mera. "All right."{/n}''', c('[Wait while Orsa fetches the saw.]', "broken")),
    n("hasty_start", "Seelah", '''"Oh, let her get a word out," Seelah says. "You'll frighten the truth clean out of her."
{n}Mera looks down at the gap between herself and Orsa.{/n}
{n}"I am standing on the other side of a drain. I would like my saw back."{/n}
{n}Seelah's mouth closes. She glances at you.{/n}''',
      c('[Ask Orsa where the saw is.]', "broken"),
      c('"Seelah, let Mera finish explaining the agreement."', "agreement")),
    n("agreement", "Seelah", '''"Right. Yes."
{n}She sets the strip of wood beside the wall and steps back.{/n}
{n}"I lent it to her for a shelf," Mera says. "Not for this job. This morning I asked whether she had brought it. She said she'd fetch it. That was before you arrived."{/n}
{n}Orsa twists the hem of her apron.{/n}
"That is the part I hadn't heard," Seelah says.
{n}Mera turns to Orsa again, still waiting for her answer.{/n}''', c('[Wait for Orsa to answer.]', "broken")),
    n("broken", "Narrator", '''{n}Orsa goes into the washhouse and returns with a saw wrapped in a towel. Several teeth are broken. One end of the blade has bent away from the handle.{/n}
{n}"There was a nail in the shelf board. I pulled harder when it caught. I thought if I could straighten it before you saw..."{/n}
{n}"You'd have given me a straight broken saw," Mera says.{/n}
{n}Seelah reaches toward the blade, then stops before touching it.{/n}
"Can it be repaired?"
{n}"By someone who knows what she's doing. Not by bending it against a doorstep." Mera wraps the sharp edge again. "The smith near my lodgings can tell me. Until then this platform waits."{/n}
{n}Orsa looks at the uncovered drain. "The evening washing won't."{/n}''', c('"What can we do safely with the tools that remain?"', "work")),
    n("work", "Seelah", '''{n}Seelah crouches by the nearest support, keeping her feet on the paving.{/n}
"Carry the loose boards out of the way, for a start. Nobody should try jumping over this with wet sheets."
{n}Mera kneels opposite her. Together they test the remaining support without putting their weight on it.{/n}
{n}"We can lay the uncut boards across this half and secure them," Mera says. "One person at a time. The rest stays closed until I can cut the replacements."{/n}
"Tell me where you want them."
{n}You carry boards while Mera checks each one. Seelah braces the first in place. Orsa brings dry wedges and kneels to pass them to the carpenter.{/n}
{n}By the time the narrow crossing is firm, Seelah's forearms are trembling. Mera tests it herself, then lets her release the board.{/n}
"I like a job where being stubborn is briefly the right answer," Seelah says, flexing her fingers.''', c('[Return to the question of the saw.]', "repayment")),
    n("repayment", "Narrator", '''{n}Mera puts her remaining tools away. Orsa stands beside her rather than across the drain.{/n}
{n}"I'll pay to repair it. Not all at once. I don't have it."{/n}
{n}"I need the saw for work. I can't wait until you have it."{/n}
"I'll pay the smith," Seelah says. "Orsa, how about you pay me back a few coins at a time?"
{n}Orsa looks relieved, then wary. "I don't want to spend every washing day wondering when you'll come to collect."{/n}
{n}Seelah rubs her hands on her trousers.{/n}
"Fair enough. Let's count the coins before I start throwing them about."
{n}Mera places the wrapped saw on her tool roll. "And whether this is a loan at all. I won't pretend nobody has to pay because a paladin arrived."{/n}''',
      c('"Pay for it outright. Orsa, tell Mera the truth next time, and take better care of her tools. Keep your coins."', "gift", flags=("seelah.saw_gift",)),
      c('"Orsa, how much can you spare after food and rent? Make that the payment."', "loan", flags=("seelah.saw_loan",))),
    n("gift", "Seelah", '''"I can afford the repair. Or a replacement if that is what Mera needs."
{n}She looks at Orsa.{/n}
"A gift, Orsa. No debt, no favors to collect later. Shall I take it to the smith?"
{n}Orsa untwists her apron. "Yes. Thank you."{/n}
{n}Mera lifts the tool roll. "Thank her by telling me when you break something. I might have lent you the other blade before I promised it elsewhere."{/n}
{n}Orsa nods, her eyes fixed on the towel around the saw. Seelah opens her mouth, catches herself, and picks up her strip of wood.{/n}''', c('[Walk to the smith with Mera and Seelah.]', "walk")),
    n("loan", "Narrator", '''{n}Orsa names a small amount after each week's washing. "And after you've paid for supper?" Seelah asks. Orsa studies her apron.{/n}
{n}After a pause, Orsa names a smaller one.{/n}
"That one," Seelah says. "If the work stops, you tell me. No extra charge for needing longer."
{n}Mera asks what happens if Seelah leaves Drezen.{/n}
{n}Seelah scratches her chin. "Then Orsa and I settle it before I pack. I'm not handing her debt to some stranger with a big stick."{/n}
{n}Orsa agrees. She repeats the amount herself, then says she is sorry for hiding the saw. Mera keeps her eyes on Orsa until the washer finishes, then nods.{/n}''', c('[Walk to the smith with Mera and Seelah.]', "walk")),
    n("walk", "Narrator", '''{n}Mera walks ahead to check whether the smith is still working. Seelah hangs back with you for a few steps.{/n}''',
      c('[Ask about the moment when she stopped to listen.]', "practice", requires=("seelah.saw_listened",)),
      c('[Ask why she cut Mera off.]', "hasty", forbids=("seelah.saw_listened",))),
    n("practice", "Seelah", '''"I nearly gave Mera a fine scolding. Very righteous. Very loud. All without seeing the saw."
{n}She looks toward the smith's door.{/n}
"Keeping my mouth shut was harder than holding that board. Orsa looked miserable, and I wanted to jump in. But then out came the saw. Broken teeth. Bent blade. Finally, something we could fix."
{n}She gives you a crooked smile.{/n}
"Next time I forget, wave a broken saw at me. Apparently that helps."''',
      c('"Mera needed help too. That saw earns her bread."', "thanks"),
      c('"You said I might have to remind you to let someone answer. I did not need to today."', "remember_frank", requires=("seelah.frank_terms",)),
      c('"You heard Mera out. Just as I asked you to hear me."', "remember_heard", requires=("seelah.hear_terms",)),
      c('"I once asked you to take my side before hearing the rest. I am glad you refused."', "remember_demand", requires=("seelah.corrected_demand",))),
    n("remember_frank", "Seelah", '''"Don't sound too impressed. I was biting the inside of my cheek."
{n}She nudges your arm with hers.{/n}
"Give me a nudge next time. Before the end of the speech, preferably. I hate wasting a good ending."
{n}Ahead of you, Mera catches the smith's door before it swings shut.{/n}
"There. Another chance to let her do the talking."''', c('[Catch up with Mera.]', "thanks")),
    n("remember_heard", "Seelah", '''"She had quite a lot to say. I nearly supplied both halves of the argument for her."
{n}Seelah looks down at the strip of wood she is still carrying.{/n}
"And I still need her to teach me how to cut this straight. Imagine having to go back and ask after telling her how to do everything else."
"You might have managed it."
"Oh, I'd have asked. She might have enjoyed the answer rather more."''', c('[Join the carpenter at the smith\'s door.]', "thanks")),
    n("remember_demand", "Seelah", '''"You took it back. I remember that part too."
{n}She gives your hand a brief squeeze before letting you go.{/n}
"Come on. If we leave Mera waiting much longer, she'll decide the real problem with paladins is that we spend all day talking outside workshops."
"Would she be wrong?"
"Today? I'd rather not give her more evidence."''', c('[Follow her to the door.]', "thanks")),
    n("thanks", "Seelah", '''{n}Seelah catches up with the carpenter before she goes inside.{/n}
"Thank you for showing us the crossing would hold. I'll come back when you're ready to finish it."
{n}"If you can follow instructions," Mera says.{/n}
"I've had some practice today."
{n}Mera smiles and takes the saw inside. Seelah waits while she explains to the smith what she needs for her next job.{/n}''', c('[Stay until they have agreed on the repair.]', flags=("seelah.saw_arranged",))),
    n("hasty", "Seelah", '''"Orsa sounded frightened, so I charged in. Poor washer, wicked carpenter, Seelah to the rescue! Gods, what an ass I made of myself."
{n}She glances toward Mera.{/n}
"I owe her an apology. I still haven't said that I was unfair to her."''',
      c('"Tell her you were wrong. She heard the accusation. She should hear the apology."', "plain", requires=("seelah.frank_terms",)),
      c('"You asked me to hear your reasons. Mera deserved that too."', "heard", requires=("seelah.hear_terms",)),
      c('"I wanted you to take my side without hearing the rest. You just did the same to Mera."', "demand", requires=("seelah.corrected_demand",))),
    n("plain", "Seelah", '''"Yes. You told me to speak plainly. Seems I heard 'Seelah, talk over everyone.' That's a rotten excuse."
{n}She catches up with Mera and asks for a moment before they go inside.{/n}''', c('[Wait nearby while Seelah apologizes.]', "apology")),
    n("heard", "Seelah", '''"She did. I don't much enjoy hearing my own promise quoted back at me, but she did."
{n}She catches up with Mera and asks for a moment before they go inside.{/n}''', c('[Wait nearby while Seelah apologizes.]', "apology")),
    n("demand", "Seelah", '''"I remember telling you off for it, too. Now I've gone and done it myself. Mera deserves an apology, courting me or not."
{n}She catches up with Mera and asks for a moment before they go inside.{/n}''', c('[Wait nearby while Seelah apologizes.]', "apology")),
    n("apology", "Narrator", '''{n}"I spoke as though you were bullying her," Seelah says. "You weren't. I'm sorry."{/n}
{n}Mera considers her. "If you want to come tomorrow, come. But when I tell you where to put your hands, don't decide I'm insulting you."{/n}
{n}"That may be the easiest promise I've made today."{/n}
{n}Mera goes in first. The smith unwraps the blade on her bench. As the two tradeswomen discuss it, Seelah props her strip of wood against the wall and waits.{/n}''', c('[Stay until they have agreed on the repair.]', flags=("seelah.saw_arranged",))),
])


s("platform_finished", "One person at a time", '"How did the repair go?"', [
    n("start", "Seelah", '''{n}Seelah has a fresh scrape across one knuckle and a look of satisfaction which suggests the two are related.{/n}
"New blade. Old handle. Mera says that makes it the same saw, and the smith says that makes her a sentimental fool. They've apparently been having that argument for years."
{n}She opens and closes her hand.{/n}
"The platform is finished. I paid what we agreed. I would like you to see it before I start telling everyone I built a bridge."''',
      c('[Return to the washing yard with her.]', "yard"),
      c('[Arrange to visit another time.]', abort=True)),
    n("yard", "Narrator", '''{n}Wet cloth hangs above the yard. Orsa carries a basket across the new boards, keeping to the side Mera has marked with chalk. Seelah steps forward to take the basket, but Orsa turns her shoulder.{/n}
{n}"I've got it. You can move that empty tub."{/n}
{n}Seelah moves the tub. Orsa sets the basket down exactly where she intended.{/n}
{n}"She asked me first today," Orsa tells you, nodding toward Seelah. "Yesterday I thought she'd carry me across as well as the washing."{/n}
"Only if you'd asked."
{n}Orsa raises an eyebrow.{/n}
"All right. I was thinking about it."
{n}The washer laughs and beckons a customer toward the repaired crossing. Seelah leaves her to work.{/n}''',
      c('"Any regrets about paying for the saw?"', "gift", requires=("seelah.saw_gift",)),
      c('"Have you settled how Orsa will repay you?"', "loan", requires=("seelah.saw_loan",))),
    n("gift", "Seelah", '''"The saw cuts. The platform holds. Good use of my coins. So why was I waiting for Orsa to thank me a second time? Oh, don't answer that. I know."
{n}She watches Orsa disagree with her customer about the basket's weight.{/n}
"I bought a saw blade, not a sweet temper. Listen to her! Five minutes after a good deed, and she's already arguing over the bill."
{n}Seelah grins.{/n}
"Though if she wins that argument, I may ask her to come shopping with me."''',
      c('"Would you make the same offer again?"', "same"),
      c('"You hoped paying for the blade would settle everything."', "unfinished")),
    n("loan", "Seelah", '''"Yes. First payment's already in my purse. I asked if the washing had paid as well as she'd hoped. It had, so I took the coins."
{n}She pats the small purse at her belt.{/n}
"Nearly shoved them straight back at her, too. 'Look how generous I am!' We'd agreed on a loan. She kept her word. I can manage to keep mine without making a spectacle of it."
{n}She grimaces.{/n}
"Whatever's left when I leave Drezen, I'll strike out. Told her so today. She said, 'Until then, take the money and stop fussing.' Fair enough."''',
      c('"Take the coins she promised. You would have helped her with an empty purse, too."', "same"),
      c('"She wants to pay her share, not stand there with her cap in her hands."', "unfinished")),
    n("same", "Seelah", '''"Of course I'd help. But next time I'll ask where the nail is before I swing the hammer."
{n}Mera calls from the washhouse door. Seelah turns, expecting another board to carry, and receives a small paper packet instead.{/n}
{n}"For your hand. Put it on before you get the cut filthy again."{/n}
"Yes, Mera."
{n}The carpenter looks delighted by the unqualified answer.{/n}''', c('[Walk out with Seelah.]', "outside")),
    n("unfinished", "Seelah", '''"Yes. One generous sweep of the hand, and everything's fixed! Except Orsa still has washing to do, and Mera still has to teach me how to saw."
{n}Mera calls from the washhouse door and gives her a little paper packet.{/n}
{n}"For the cut. I'll leave you to tie it. Unless you want me to carry you across the yard as well?"{/n}
{n}Seelah laughs. "I had that coming."{/n}''', c('[Walk out with Seelah.]', "outside")),
    n("outside", "Seelah", '''{n}Outside the yard, she opens the packet and wraps the clean strip of cloth around her knuckle. You hold the end while she ties it.{/n}
"Tomorrow I'm finding a quiet corner. Before I start boasting about my magnificent bridge over three feet of drain."
{n}She studies the finished knot.{/n}
"I want to pray. Come along? I promise the speech will be for Iomedae. Lucky you."''',
      c('"I would like to be there."', "invited", flags=("seelah.prayer_company",)),
      c('"Go pray. I\'ll see you afterward. You can tell me how it went then."', "later", flags=("seelah.prayer_private",))),
    n("invited", "Seelah", '''"Then come find me tomorrow. I know a quiet corner."
{n}She catches your fingers before you let go of the bandage.{/n}
"Thank you for today. All of it. Even the parts where you were rather inconvenient company."''', c('[Make time to meet her.]', flags=("seelah.platform_kept",))),
    n("later", "Seelah", '''"I will. And afterward I'd like to see you."
{n}She catches your fingers before you let go of the bandage.{/n}
"Tomorrow? We'll find something to do. I've issued enough marching orders for one day."''', c('[Arrange to see her afterward.]', flags=("seelah.platform_kept",))),
], requires=("seelah.saw_arranged",))


s("inheritors_corner", "Words she has said before", '"You asked me to find you today."', [
    n("start", "Narrator", '''{n}Seelah is waiting beside a sheltered alcove in Drezen. Someone has set a small image of Iomedae on the stone ledge. There is room for two people to stand without blocking the passage.{/n}''',
      c('[Join her for the prayer you discussed.]', "prayer", requires=("seelah.prayer_company",)),
      c('[Ask whether she has finished praying.]', "after", requires=("seelah.prayer_private",)),
      c('[Arrange another time.]', abort=True)),
    n("prayer", "Seelah", '''"I'm going to kneel. Mind that stone if you join me. It's got a vicious corner."
{n}She kneels, then shifts her weight off a sharp corner of the paving. After a moment she bows her head.{/n}
"Inheritor, help me do better than yesterday. And remember the good I did, even when I'm busy kicking myself for the rest."
{n}Her lips move without sound. You hear someone pass behind you, then the scrape of a bucket carried away. Seelah remains where she is.{/n}
{n}When she rises, she rubs her knee, notices you watching, and smiles.{/n}
"Ow. Faith's willing. Knees are complaining."''',
      c('"I would like to pray beside you, in my own words."', "own"),
      c('"I\'m glad I came. Though I don\'t know whether any god would listen to me."', "doubt"),
      c('"May I ask what you were saying quietly?"', "quiet_words")),
    n("own", "Seelah", '''"Of course."
{n}She steps aside, giving you the place before the image. You say what you came to say. Seelah waits until you turn back to her.{/n}
"There. You, me, and no sermon. We should do this more often."''', c('[Walk with her out of the passage.]', "outcomes")),
    n("doubt", "Seelah", '''"I trust her. Some mornings I kneel down and can't get a word out anyway. 'Why did that happen? Why was I there?' Round and round, like a dog after its tail."
{n}She looks toward the little image.{/n}
"Don't go inventing a prayer to impress me. You came. That was what I wanted."''', c('[Walk with her out of the passage.]', "outcomes")),
    n("quiet_words", "Seelah", '''"Names. After a while I just kept saying them."
{n}She rests her bandaged hand against her other palm.{/n}
"The rest is between me and her for now. I've still got words stuck in my throat. They'll come out when they're ready."''', c('"Then I\'ll leave the rest to her. I\'m glad you brought me."', "outcomes")),
    n("after", "Seelah", '''"Yes. I've finished. Or stopped, anyway."
{n}She steps out of the alcove, leaving the space free for a woman carrying a covered bowl.{/n}
"I thanked her. I've been forgetting that part. Then came the questions. Still no answers, but at least I didn't swallow the last half of the prayer and rush out grinning."
{n}She gives you a small smile.{/n}
"I am glad you're here too."''', c('[Walk with her.]', "outcomes")),
    n("outcomes", "Seelah", '''{n}You reach a low wall overlooking a narrow garden. Seelah puts her elbows on it and watches a sparrow turn a fallen leaf over with its beak.{/n}
"Boards are easy. Count them, hammer them down, watch Orsa walk across without breaking her neck. There. Something put right. I wish the rest were that simple."''',
      c('[Let her talk about what returning the souls did not repair.]', "bad", requires=("seelah.souls_returned", "seelah.ending_bad")),
      c('[Ask what she is still trying to understand.]', "moderate", requires=("seelah.souls_returned", "seelah.ending_moderate"), forbids=("seelah.ending_bad",)),
      c('[Ask what has stayed with her since the rescue.]', "rescued", requires=("seelah.souls_returned",), forbids=("seelah.ending_bad", "seelah.ending_moderate")),
      c('[Ask what she still hopes to put right.]', "unfinished", forbids=("seelah.souls_returned",))),
    n("bad", "Seelah", '''"I can't count the people who came back and call it a victory. Not with the others still gone."
{n}She presses her palms against the wall.{/n}
"I'm glad we brought them back. Of course I am. But if someone tells me to smile and forget the rest, I'll bite their head off. Sometimes I start sharpening my teeth before anyone's said a word."
{n}She looks at you.{/n}
"Some days I'll want to saddle a horse and ride out alone. When I do, I'll tell you myself. You won't wake up to an empty chair and a scrap of paper."''', c('"Tell me before you ride. I won\'t ask when you\'ll stop missing them."', "friends", flags=("seelah.aftermath_grief",))),
    n("moderate", "Seelah", '''"How I can come out the other side and still know so little. 'Have faith,' I tell people. Nice and easy from me. Then they ask why, and suddenly I've got a mouth full of turnips."
{n}She turns so that she can see you properly.{/n}
"When there's a chance, I might take the road alone for a while. Hear what people say when they haven't already decided what Seelah the paladin ought to tell them. I want you. That hasn't changed. But I can't promise I'll always be waiting at your door."
{n}She smiles without much amusement.{/n}
"Listen to that. 'Come here, I might be elsewhere!' A magnificent bit of courting."''', c('"An honest one. We\'ll talk again when you know where you\'re riding."', "friends", flags=("seelah.aftermath_questions",))),
    n("rescued", "Seelah", '''"I still want to charge ahead shouting, 'This time it'll be better!' You'd think I'd have bitten my tongue off by now."
{n}The sparrow flies away. Seelah follows it with her eyes.{/n}
"I'll keep hoping. But I can't drag my friends along by the collar and tell them to cheer up. We got them back. That doesn't wipe out what happened, or make all my mistakes come right. They can tell me themselves what they're glad about."
{n}She glances at you.{/n}
"Same goes for you. If I try dragging you into my glorious future by the collar, kick me."''', c('[Ask what she wants to remember about her friends.]', "friends", flags=("seelah.aftermath_hope",))),
    n("unfinished", "Seelah", '''"I've still got things to put right. Some I can reach. Others... I don't know. But I won't cross them off just because you and I have started making plans."
{n}She turns away from the wall.{/n}
"We can have supper. We can kiss. Gods, if I waited until I'd mended the whole world, I'd never get either. But when there's work to do, I'll go. And I'm still going to ask why, even when I don't like the answers."
{n}She gives a small, tired laugh.{/n}
"Oh, stop looking at me like that. I haven't brought you a shovel."''', c('"Then we\'ll make our plans and keep doing the work."', "plans", flags=("seelah.aftermath_unfinished",))),
    n("friends", "Seelah", '''"Elan is part of it."''',
      c('[Listen to her memory of him.]', "elan", requires=("seelah.elan_dead",)),
      c('[Ask about Elan.]', "elan_living", forbids=("seelah.elan_dead",))),
    n("elan", "Seelah", '''"I remember him sounding so sure of himself. Made me want to shake him. Then five minutes later I'd be wishing I could believe as firmly as he did."
{n}She looks down at her hands.{/n}
"Now I catch myself thinking, 'Elan would agree with me.' Convenient, isn't it? He can't argue back. I miss him. I won't make him my pet sermon."
{n}After a moment she exhales.{/n}
"Next time I'll just tell you about him. Try to get through it without preaching."''', c('"I would like to hear it when you want to tell it."', "plans")),
    n("elan_living", "Seelah", '''"I keep starting to tell people how glad he must be. Then I remember he has a perfectly good mouth of his own."
{n}She brushes grit from her sleeve.{/n}
"I'll ask him myself one of these days. Just him and me. I won't lure him to supper with us and start cross-examining him over the bread."
{n}Her smile returns.{/n}
"So you're stuck with me tonight. Hope you brought enough patience."''', c('"I came to see you."', "plans")),
    n("plans", "Seelah", '''"Speaking of tonight, I've got a better idea than standing here talking your ears off."
{n}She points toward the rooftops beyond the garden.{/n}
"Mera knows a place above her workshop where you can see the evening sky. She offered it when I said I kept going out to look up and finding a wall in the way. She says the stairs are sound and I am not to demonstrate how much weight the railing will hold."
{n}Seelah waits for your answer with an eagerness she makes little effort to hide.{/n}
"Tomorrow? I'll bring supper. You bring an appetite."''', c('[Arrange the evening on the roof.]', flags=("seelah.faith_spoken",))),
], requires=("seelah.platform_kept",))


s("roof_evening", "Enough sky for an evening", '"You promised me a view."', [
    n("start", "Narrator", '''{n}Mera lets you through her workshop and points to the stairs. Seelah follows carrying a covered basket. At the top, the roof opens into a small terrace with two low seats set well back from the railing.{/n}
{n}"The view is included," Mera calls. "The furniture is not to be tested to destruction."{/n}
"There goes my plan for the evening," Seelah calls back.
{n}Mera's laugh follows you up. Seelah spreads the cloth on a low crate between the seats, sets out the food, and puts the basket at her feet.{/n}
"Cold chicken, flatbread, and something the woman swore was a pickle. She had my coins before I could argue."''',
      c('[Try the pickle.]', "pickle"),
      c('[Ask Seelah to try it first.]', "first"),
      c('[Explain that you need to return another evening.]', abort=True)),
    n("pickle", "Seelah", '''{n}You bite into something crisp, sour, and startlingly hot. Seelah watches your expression with undisguised interest.{/n}
"That bad?"
{n}You offer her the untouched second piece. She tries it, stops chewing, then finishes with great determination.{/n}
"I see. We have bought an argument."
{n}She pushes the bread toward you and reaches for a cup of water herself.{/n}''', c('[Recover together over the rest of the food.]', "sky")),
    n("first", "Seelah", '''"Coward."
{n}She bites into a piece, clearly expecting to enjoy your caution. Her expression changes.{/n}
"Sensible coward."
{n}She swallows, drinks some water, and points firmly at the chicken.{/n}
"I have carried out the dangerous part. You can begin there."
{n}She moves the pickles to the far end of the cloth, where they can offend nobody by accident.{/n}''', c('[Share the safer part of supper.]', "sky")),
    n("sky", "Narrator", '''{n}From the terrace you can see above the nearest roofs. A scrap of pale cloud catches the evening light. Seelah watches it while she folds a piece of chicken into the flatbread.{/n}
"There. I wanted you to see that. It looked like nothing at all a moment ago."
{n}You watch until the color changes again. Below you, Mera shutters the workshop window. Seelah raises her hand in thanks when the carpenter looks up.{/n}''',
      c('"This is the kind of home evening I hoped for."', "home", requires=("seelah.day_home",)),
      c('"We did not have to travel far to find a view worth stopping for."', "road", requires=("seelah.day_road",)),
      c('"I couldn\'t give you an answer before. But this? Yes."', "try", requires=("seelah.day_uncertain",)),
      c('"I am glad you chose this."', "try", forbids=("seelah.day_home", "seelah.day_road", "seelah.day_uncertain"))),
    n("home", "Seelah", '''"You said supper at home. I remembered. Wasn't sure a borrowed roof would count."
{n}She tears the last flatbread in two and offers you half.{/n}
"I like the road. But coming home to you, finding my boots where I left them, knowing what we're doing tomorrow... I could get used to that."
{n}She laughs at your expression.{/n}
"One of them, then. I won't demand miracles."''', c('[Stay and watch the light change.]', "future")),
    n("road", "Seelah", '''"A journey with stairs. We should count it."
{n}She tears the last flatbread in two and offers you half.{/n}
"I would still like the longer ones. But if I wait for the perfect road before I invite you anywhere, I could miss rather a lot of evenings."
{n}She points at the remaining pickle.{/n}
"We even encountered a danger unknown to either of us. A proper expedition."''', c('[Stay and watch the light change.]', "future")),
    n("try", "Seelah", '''"So am I. I nearly wore a hole in my boots looking for something grand enough. Then I thought, 'Seelah, you idiot. You want supper with this person. Go buy supper.'"
{n}She tears the last flatbread in two and offers you half.{/n}
"Good sky. Good company. Jury's still out on the pickle."''', c('[Stay and watch the light change.]', "future")),
    n("future", "Seelah", '''{n}As the light fades, Seelah moves the empty basket beneath her seat. She looks at you instead of the sky.{/n}
"I've still got questions. And there's still work waiting downstairs. But right now I'm looking at your mouth, and I'd rather you were sitting here."
{n}She rests her hand on the seat beside her, palm up.{/n}
"Come closer. Tomorrow we'll talk about the promises. Tonight I want you against me."''',
      c('[Take her hand. "Kiss me."]', "kiss"),
      c('[Take her hand and sit quietly together.]', "quiet"),
      c('"There are others I love. I want evenings with you, too, and I won\'t leave any of you waiting on a broken promise."', "others")),
    n("others", "Seelah", '''"Then don't leave them watching the door. Tell them you're here. And if you've got to go, tell me before I pour another cup."
{n}She leaves her hand where it is.{/n}
"I won't demand every evening you have. But come because you want me, and keep your word to them, too. I don't fancy kissing you while someone else waits over a cold supper."
{n}She smiles.{/n}
"Half an hour? I'll take it. Seems a waste to spend all thirty minutes arguing for the rest of the night."''',
      c('[Take her hand. "Kiss me."]', "kiss", flags=("seelah.aftermath_otherpartners",)),
      c('[Take her hand and stay close for the time you have.]', "quiet", flags=("seelah.aftermath_otherpartners",))),
    n("kiss", "Seelah", '''"Yes."
{n}She meets you halfway. Her free hand rests against your shoulder, then slides to the back of your neck as she kisses you again. You can feel her smiling before she draws back.{/n}
"I'm glad we didn't wait for a better evening."
{n}She stays beside you while the remaining light leaves the cloud. Neither of you mentions the view for a while.{/n}''', c('[Stay until it is time to go down.]', "leave", flags=("seelah.roof_kissed",))),
    n("quiet", "Seelah", '''{n}She shifts closer and leans against you. After a while her thumb moves across your knuckles, slowly enough that you notice each pass.{/n}
"This is good too."
{n}She says nothing else for a time. From somewhere below comes the sound of a bucket being emptied and a woman telling someone that tomorrow will do. Seelah closes her eyes and lets tomorrow wait.{/n}''', c('[Stay until it is time to go down.]', "leave", flags=("seelah.roof_quiet",))),
    n("leave", "Narrator", '''{n}You pack the cups and the remaining food into the basket. Seelah folds the cloth over them and checks that neither of you has left anything behind.{/n}
{n}At the stairs she offers you her free hand, then laughs when you point out how little space there is to walk side by side. She goes first and waits at the bottom.{/n}
{n}She takes your hand again before you leave the workshop together.{/n}''',
      c('[Ask how her journeys will fit the life you have promised each other.]', "promised", requires=("seelah.committed",)),
      c('[Arrange to talk again about your future.]', "consider", forbids=("seelah.committed",))),
    n("promised", "Seelah", '''"I still mean it. There'll be journeys, and questions, and days when I come back in a foul temper. You ought to hear that from me before we start picking curtains."
{n}She gives your hand a small squeeze.{/n}
"And if I get so busy chasing answers that I forget supper with you, remind me of this roof. Preferably without serving that pickle again."''', c('[Keep your promise, with her journeys and doubts still ahead.]', flags=("seelah.aftermath_ready",))),
    n("consider", "Seelah", '''"Tomorrow, then. We'll tackle the hard part. I'm not ducking it."
{n}She gives your hand a small squeeze.{/n}
"For tonight, I'm glad we came."''', c('[Walk home with her and keep tomorrow free for the talk.]', flags=("seelah.aftermath_ready",))),
], requires=("seelah.faith_spoken",))






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
"A pair with better judgment than these would be useful. I offered to help repair a washing platform. Then I discovered that I can split wood very impressively and still be absolutely useless at making two pieces the same length."
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
      c('[Give her time to ask what help is actually wanted.]', "need", requires=("seelah.knows_need",), forbids=("seelah.check_signal", "seelah.check_person"), flags=("seelah.saw_listened",)),
      c('[Listen as Seelah steps into the conversation.]', "hasty_start", forbids=("seelah.check_signal", "seelah.check_person", "seelah.knows_need"))),
    n("signal", "Seelah", '''{n}At the second tap she stops and turns toward you. Then she looks at Mera, taking in the open tool roll.{/n}
"I heard her sound frightened. I hadn't heard what happened."
{n}She sets down the strip of wood and leaves room for Orsa to answer.{/n}''', c('[Let Mera explain the loan.]', "listened")),
    n("person", "Seelah", '''{n}Seelah follows your attention from Orsa to the carpenter. Mera has left a space in the tool roll for the missing saw. She keeps touching it as though the tool might appear there.{/n}
"We should hear what happened before I start making offers," Seelah says. "Mera?"
{n}Orsa exhales. Seelah waits rather than deciding what that means.{/n}''', c('[Hear the agreement before proposing a solution.]', "listened")),
    n("need", "Seelah", '''"Orsa, do you want help explaining something?"
{n}The washer shakes her head, then looks toward the washhouse.{/n}
{n}"I need to fetch it. I was hoping I wouldn't have to show everyone."{/n}
"Then we'll wait. Mera, tell me what you agreed."
{n}Seelah puts the wood down without offering to fetch the saw herself.{/n}''', c('[Wait with her.]', "listened")),
    n("listened", "Narrator", '''{n}"I lent it for a shelf," Mera says. "She was to bring it back before I began this platform. It isn't a shared tool. I earn my living with it."{/n}
{n}Seelah nods, then turns to Orsa. "We won't know what to do until we see it."{/n}
{n}Orsa looks at Mera. "All right."{/n}''', c('[Give Orsa room to fetch the saw.]', "broken")),
    n("hasty_start", "Seelah", '''"Then let's hear her," Seelah says. "Nobody gets more honest because you stand over them."
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
"I'll pay the smith," Seelah says. "You can repay me a little at a time. If that is what you want, Orsa."
{n}Orsa looks relieved, then wary. "I don't want to spend every washing day wondering when you'll come to collect."{/n}
{n}Seelah rubs her hands on her trousers.{/n}
"Fair. We should say what we're agreeing to before I go rushing off feeling generous."
{n}Mera places the wrapped saw on her tool roll. "And whether this is a loan at all. I won't pretend nobody has to pay because a paladin arrived."{/n}''',
      c('"Make it a gift. Orsa owes Mera an honest account and care with borrowed tools, not a debt to us."', "gift", flags=("seelah.saw_gift",)),
      c('"Ask what Orsa can repay without losing meals or rent. Agree on that amount and no more."', "loan", flags=("seelah.saw_loan",))),
    n("gift", "Seelah", '''"I can afford the repair. Or a replacement if that is what Mera needs."
{n}She looks at Orsa.{/n}
"You can say no. But if you say yes, I won't turn it into a favor you owe me later."
{n}Orsa untwists her apron. "Yes. Thank you."{/n}
{n}Mera lifts the tool roll. "Thank her by telling me when you break something. I might have lent you the other blade before I promised it elsewhere."{/n}
{n}Orsa nods. She looks more ashamed than she did while the two women were arguing. Seelah begins to speak, then leaves the apology to her.{/n}''', c('[Walk to the smith with Mera and Seelah.]', "walk")),
    n("loan", "Narrator", '''{n}Orsa names a small amount after each week's washing. Seelah asks whether that is the amount she can spare or the amount she thinks a paladin wants to hear.{/n}
{n}After a pause, Orsa names a smaller one.{/n}
"That one," Seelah says. "If the work stops, you tell me. No extra charge for needing longer."
{n}Mera asks what happens if Seelah leaves Drezen.{/n}
{n}Seelah thinks before answering. "We settle what remains before I go. I won't leave someone else to collect a promise I made."{/n}
{n}Orsa agrees. She repeats the amount herself, then says she is sorry for hiding the saw. Mera listens without telling her that the concealment did not matter.{/n}''', c('[Walk to the smith with Mera and Seelah.]', "walk")),
    n("walk", "Narrator", '''{n}Mera walks ahead to check whether the smith is still working. Seelah hangs back with you for a few steps.{/n}''',
      c('[Ask about the moment when she stopped to listen.]', "practice", requires=("seelah.saw_listened",)),
      c('[Give her room to speak about the interruption.]', "hasty", forbids=("seelah.saw_listened",))),
    n("practice", "Seelah", '''"I was ready to tell Mera off. I had a whole picture of what happened, and I hadn't even seen the saw."
{n}She looks toward the smith's door.{/n}
"This time I waited. It didn't make me feel clever. I stood there wondering whether I was leaving Orsa to struggle. Then she showed us the blade, and we could do something about the actual problem."
{n}She gives you a crooked smile.{/n}
"Apparently remembering is something you do with your mouth shut occasionally. Who knew?"''',
      c('"Mera got to be a person who needed help too."', "thanks"),
      c('"You said I might have to remind you to let someone answer. I did not need to today."', "remember_frank", requires=("seelah.frank_terms",)),
      c('"That was the kind of hearing I asked you for. Mera got it too."', "remember_heard", requires=("seelah.hear_terms",)),
      c('"I once asked you to take my side before hearing the rest. I am glad you refused."', "remember_demand", requires=("seelah.corrected_demand",))),
    n("remember_frank", "Seelah", '''"Don't sound too impressed. I was biting the inside of my cheek."
{n}She nudges your arm with hers.{/n}
"You can still remind me next time. Preferably before I've delivered the entire speech. I get attached to a good ending."
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
    n("hasty", "Seelah", '''"I heard a frightened voice and decided I knew the rest. I don't like discovering how quickly I can turn somebody into a villain so I can be helpful."
{n}She glances toward Mera.{/n}
"I owe her an apology. I still haven't said that I was unfair to her."''',
      c('"Tell her plainly. She should not have to guess whether you still think she was cruel."', "plain", requires=("seelah.frank_terms",)),
      c('"You asked me to hear your reasons. Mera deserved that too."', "heard", requires=("seelah.hear_terms",)),
      c('"We both know wanting reassurance can turn into an unfair demand."', "demand", requires=("seelah.corrected_demand",))),
    n("plain", "Seelah", '''"Yes. You gave me permission to speak plainly to you. That wasn't permission to stop listening to everyone else."
{n}She catches up with Mera and asks for a moment before they go inside.{/n}''', c('[Wait nearby while Seelah apologizes.]', "apology")),
    n("heard", "Seelah", '''"She did. I don't much enjoy hearing my own promise quoted back at me, but she did."
{n}She catches up with Mera and asks for a moment before they go inside.{/n}''', c('[Wait nearby while Seelah apologizes.]', "apology")),
    n("demand", "Seelah", '''"I remember. I was very clear about what you owed me. I should manage to give some of it to someone who isn't trying to court me."
{n}She catches up with Mera and asks for a moment before they go inside.{/n}''', c('[Wait nearby while Seelah apologizes.]', "apology")),
    n("apology", "Narrator", '''{n}"I spoke as though you were bullying her," Seelah says. "You weren't. I'm sorry."{/n}
{n}Mera considers her. "If you want to come tomorrow, come. But when I tell you where to put your hands, don't decide I'm insulting you."{/n}
{n}"That may be the easiest promise I've made today."{/n}
{n}Mera goes in first. The smith unwraps the blade on her bench and asks questions which Seelah allows its owner to answer.{/n}''', c('[Stay until they have agreed on the repair.]', flags=("seelah.saw_arranged",))),
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
      c('"How do you feel about giving the money?"', "gift", requires=("seelah.saw_gift",)),
      c('"Have you settled how Orsa will repay you?"', "loan", requires=("seelah.saw_loan",))),
    n("gift", "Seelah", '''"Pleased. And annoyed with myself, because part of me wants her to be so grateful that I'll know I did the right thing."
{n}She watches Orsa disagree with her customer about the basket's weight.{/n}
"She doesn't have to become somebody easier to help because I spent money. She can take the gift and have a perfectly ordinary argument five minutes later."
{n}Seelah grins.{/n}
"Though if she wins that argument, I may ask her to come shopping with me."''',
      c('"Would you make the same offer again?"', "same"),
      c('"I think you wanted the gift to finish the whole problem."', "unfinished")),
    n("loan", "Seelah", '''"Yes. She brought the first payment before I asked. I made certain she still had the work she expected. Then I accepted it."
{n}She pats the small purse at her belt.{/n}
"I nearly handed it straight back. That would have felt generous too. It would also have meant our agreement lasted exactly as long as it took me to want a different feeling about myself."
{n}She grimaces.{/n}
"When I leave, I'll forgive whatever is left. I told her that today. She says until then she intends to pay what she promised, and I should let her."''',
      c('"You can accept her choice without making her prove she deserves help."', "same"),
      c('"It sounds as though she wants this to be an agreement between equals."', "unfinished")),
    n("same", "Seelah", '''"I would still help. I would ask more questions before I decided what helping looked like."
{n}Mera calls from the washhouse door. Seelah turns, expecting another board to carry, and receives a small paper packet instead.{/n}
{n}"For your hand. Put it on before you get the cut filthy again."{/n}
"Yes, Mera."
{n}The carpenter looks delighted by the unqualified answer.{/n}''', c('[Walk out with Seelah.]', "outside")),
    n("unfinished", "Seelah", '''"And I wanted to be the person who made it simple. That's not always a job anyone needs doing."
{n}Mera calls from the washhouse door and gives her a little paper packet.{/n}
{n}"For the cut. You can open it yourself. I thought you might appreciate being asked to do something you already know how to do."{/n}
{n}Seelah laughs. "I had that coming."{/n}''', c('[Walk out with Seelah.]', "outside")),
    n("outside", "Seelah", '''{n}Outside the yard, she opens the packet and wraps the clean strip of cloth around her knuckle. You hold the end while she ties it.{/n}
"I'd like to go somewhere quiet tomorrow. Somewhere I won't be tempted to announce that I've had a useful afternoon."
{n}She studies the finished knot.{/n}
"I want to pray. You can come if you want. I don't have a speech ready about it."''',
      c('"I would like to be there."', "invited", flags=("seelah.prayer_company",)),
      c('"Take the time you need. Tell me afterward, if you want to."', "later", flags=("seelah.prayer_private",))),
    n("invited", "Seelah", '''"Then come find me tomorrow. I know a quiet corner."
{n}She catches your fingers before you let go of the bandage.{/n}
"Thank you for today. All of it. Even the parts where you were rather inconvenient company."''', c('[Make time to meet her.]', flags=("seelah.platform_kept",))),
    n("later", "Seelah", '''"I will. And afterward I'd like to see you."
{n}She catches your fingers before you let go of the bandage.{/n}
"Tomorrow? We can decide what to do when we get there. I've made enough plans for other people today."''', c('[Arrange to see her afterward.]', flags=("seelah.platform_kept",))),
], requires=("seelah.saw_arranged",))


s("inheritors_corner", "Words she has said before", '"You asked me to find you today."', [
    n("start", "Narrator", '''{n}Seelah is waiting beside a sheltered alcove in Drezen. Someone has set a small image of Iomedae on the stone ledge. There is room for two people to stand without blocking the passage.{/n}''',
      c('[Join her for the prayer you discussed.]', "prayer", requires=("seelah.prayer_company",)),
      c('[Ask whether this is still a good time to meet.]', "after", requires=("seelah.prayer_private",)),
      c('[Arrange another time.]', abort=True)),
    n("prayer", "Seelah", '''"You don't have to kneel because I do. Or say anything."
{n}She kneels, then shifts her weight off a sharp corner of the paving. After a moment she bows her head.{/n}
"Inheritor. Help me do better than yesterday. And help me notice when yesterday wasn't entirely wasted."
{n}Her lips move without sound. You hear someone pass behind you, then the scrape of a bucket carried away. Seelah remains where she is.{/n}
{n}When she rises, she rubs her knee, notices you watching, and smiles.{/n}
"No sacred meaning to that part. It's a very hard floor."''',
      c('"I would like to pray beside you, in my own words."', "own"),
      c('"I am glad you let me be here. I do not know what I believe about being heard."', "doubt"),
      c('"May I ask what you were saying quietly?"', "quiet_words")),
    n("own", "Seelah", '''"Of course."
{n}She steps aside, giving you the place before the image. You say what you came to say. Seelah waits until you turn back to her.{/n}
"I won't ask you to explain it. I wanted you here, not giving an account of yourself."''', c('[Walk with her out of the passage.]', "outcomes")),
    n("doubt", "Seelah", '''"Some days I know exactly what I believe and still don't know what to say. I have faith in her. That doesn't mean I understand what has happened, or why I was there to see it."
{n}She looks toward the little image.{/n}
"I don't want you pretending for my sake. You stayed. I noticed."''', c('[Walk with her out of the passage.]', "outcomes")),
    n("quiet_words", "Seelah", '''"Names. Then I stopped trying to make a sentence out of them."
{n}She rests her bandaged hand against her other palm.{/n}
"I can tell you that much. I'd like to keep the rest. Not because you're forbidden to hear it. Because I haven't finished saying it, even to myself."''', c('"Then keep it. I am glad you invited me."', "outcomes")),
    n("after", "Seelah", '''"Yes. I've finished. Or stopped, anyway."
{n}She steps out of the alcove, leaving the space free for a woman carrying a covered bowl.{/n}
"I thanked her for the things I keep forgetting to be grateful for. Then I asked some questions I don't expect to settle today. I'm glad I didn't try to make it shorter so I could arrive looking cheerful."
{n}She gives you a small smile.{/n}
"I am glad you're here too."''', c('[Walk with her.]', "outcomes")),
    n("outcomes", "Seelah", '''{n}You reach a low wall overlooking a narrow garden. Seelah puts her elbows on it and watches a sparrow turn a fallen leaf over with its beak.{/n}
"I keep thinking about what comes after helping someone. Yesterday we could count the boards. There was a place to stand that hadn't been safe before. I liked knowing what we'd done."''',
      c('[Let her talk about what returning the souls did not repair.]', "bad", requires=("seelah.souls_returned", "seelah.ending_bad")),
      c('[Ask what she is still trying to understand.]', "moderate", requires=("seelah.souls_returned", "seelah.ending_moderate"), forbids=("seelah.ending_bad",)),
      c('[Ask what has stayed with her since the rescue.]', "rescued", requires=("seelah.souls_returned",), forbids=("seelah.ending_bad", "seelah.ending_moderate")),
      c('[Give her room to speak about unfinished work.]', "unfinished", forbids=("seelah.souls_returned",))),
    n("bad", "Seelah", '''"I can't do that with the people we lost. Count everyone who came back and arrive at a number that makes it all right."
{n}She presses her palms against the wall.{/n}
"I know the rescue mattered. I get angry when I think someone is asking me to be happy enough to stop talking about what it couldn't change. Sometimes nobody has asked. I've prepared the argument anyway."
{n}She looks at you.{/n}
"There may be days when I need to go somewhere without you. I don't mean that as a threat. I don't want you waking up one morning and finding a note where an explanation should have been."''', c('"Tell me what you can. I will not demand a date when grief ends."', "friends", flags=("seelah.aftermath_grief",))),
    n("moderate", "Seelah", '''"Whether I have mistaken getting through something for understanding it. I can tell somebody else to have faith. Then I get halfway through explaining what I mean and hear how easy I've made it sound."
{n}She turns so that she can see you properly.{/n}
"I may need to travel on my own when I can. Listen to people who don't already know what answer they expect from me. I still want you in my life. I haven't worked out how often I can promise to be in the same room."
{n}She smiles without much amusement.{/n}
"A magnificent invitation from someone trying to court you."''', c('"An honest one. We should keep talking about what we can promise."', "friends", flags=("seelah.aftermath_questions",))),
    n("rescued", "Seelah", '''"That I still want to run ahead of everybody and promise the next thing will be better. I thought I'd have learned enough to stop wanting that."
{n}The sparrow flies away. Seelah follows it with her eyes.{/n}
"I don't want to stop hoping. I want to stop handing people my hope as though they agreed to carry it. What happened to my friends isn't proof that my own life has worked out. I don't get to decide what the rescue ought to mean to everyone else."
{n}She glances at you.{/n}
"And neither do I get to do that with us."''', c('[Ask what she wants to remember about her friends.]', "friends", flags=("seelah.aftermath_hope",))),
    n("unfinished", "Seelah", '''"There are things I haven't put right. Some may still be possible. Some may already be beyond anything I can do. I don't want a conversation about our future to sound as though we decided none of them mattered."
{n}She turns away from the wall.{/n}
"I am not asking you to refuse every good thing until the world is repaired. I couldn't keep that promise myself. I am asking that we leave room for the work and for the questions."
{n}She gives a small, tired laugh.{/n}
"I didn't bring a list. You can stop looking as though I'm going to assign you something."''', c('"We can want a future without pretending everything is finished."', "plans", flags=("seelah.aftermath_unfinished",))),
    n("friends", "Seelah", '''"Elan is part of it."''',
      c('[Listen to her memory of him.]', "elan", requires=("seelah.elan_dead",)),
      c('[Let her explain without deciding for him.]', "elan_living", forbids=("seelah.elan_dead",))),
    n("elan", "Seelah", '''"I remember how certain he could sound. Sometimes I wanted to shake him. Sometimes I wanted to borrow it for an hour."
{n}She looks down at her hands.{/n}
"Now I can imagine him agreeing with any argument I want. He isn't here to tell me I've got him wrong. I don't want to start doing that. I miss a person. Not an answer I can put in his mouth."
{n}After a moment she exhales.{/n}
"I can tell a story about him without making it a lesson. I'm going to try."''', c('"I would like to hear it when you want to tell it."', "plans")),
    n("elan_living", "Seelah", '''"He gets to answer for himself. That sounds obvious until I catch myself explaining what the rescue must have meant to him."
{n}She brushes grit from her sleeve.{/n}
"I would like to ask him sometime. I won't invite him to one of our evenings and then spring the question on him. If he wants to talk to me, we can arrange our own conversation."
{n}Her smile returns.{/n}
"That leaves you with me. I hope you had allowed for that."''', c('"I came to see you."', "plans")),
    n("plans", "Seelah", '''"Then there's something I'd like to do with you. No lesson attached."
{n}She points toward the rooftops beyond the garden.{/n}
"Mera knows a place above her workshop where you can see the evening sky. She offered it when I said I kept going out to look up and finding a wall in the way. She says the stairs are sound and I am not to demonstrate how much weight the railing will hold."
{n}Seelah waits for your answer with an eagerness she makes little effort to hide.{/n}
"Tomorrow? I'll bring food that doesn't require anyone to be grateful for it."''', c('[Arrange the evening on the roof.]', flags=("seelah.faith_spoken",))),
], requires=("seelah.platform_kept",))


s("roof_evening", "Enough sky for an evening", '"You promised me a view."', [
    n("start", "Narrator", '''{n}Mera lets you through her workshop and points to the stairs. Seelah follows carrying a covered basket. At the top, the roof opens into a small terrace with two low seats set well back from the railing.{/n}
{n}"The view is included," Mera calls. "The furniture is not to be tested to destruction."{/n}
"There goes my plan for the evening," Seelah calls back.
{n}Mera's laugh follows you up. Seelah spreads the cloth on a low crate between the seats, sets out the food, and puts the basket at her feet.{/n}
"Cold chicken, flatbread, and something the woman selling it described as a pickle before I had an opportunity to disagree."''',
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
      c('"I did not know what I wanted when you first asked. I am glad we tried this."', "try", requires=("seelah.day_uncertain",)),
      c('"I am glad you chose this."', "try", forbids=("seelah.day_home", "seelah.day_road", "seelah.day_uncertain"))),
    n("home", "Seelah", '''"I remembered. I didn't know if it would still be what you wanted."
{n}She tears the last flatbread in two and offers you half.{/n}
"I like going out. I like coming back too. Perhaps I could become a woman who knows both where she left her things and what she means to do tomorrow."
{n}She laughs at your expression.{/n}
"One of them, then. I won't demand miracles."''', c('[Stay and watch the light change.]', "future")),
    n("road", "Seelah", '''"A journey with stairs. We should count it."
{n}She tears the last flatbread in two and offers you half.{/n}
"I would still like the longer ones. But if I wait for the perfect road before I invite you anywhere, I could miss rather a lot of evenings."
{n}She points at the remaining pickle.{/n}
"We even encountered a danger unknown to either of us. A proper expedition."''', c('[Stay and watch the light change.]', "future")),
    n("try", "Seelah", '''"So am I. I kept trying to think of something impressive, then remembered that I wanted to spend the time with you, not explain afterward why it ought to have been enjoyable."
{n}She tears the last flatbread in two and offers you half.{/n}
"I am prepared to call the sky a success. The pickle requires more thought."''', c('[Stay and watch the light change.]', "future")),
    n("future", "Seelah", '''{n}As the light fades, Seelah moves the empty basket beneath her seat. She looks at you instead of the sky.{/n}
"I meant what I said about needing room for the questions. I also want evenings like this. I don't want to make you guess which one I mean whenever I ask to see you."
{n}She rests her hand on the seat beside her, palm up.{/n}
"Tonight, I mean that I want you close. Tomorrow, we can talk about the promises we know how to keep."''',
      c('[Take her hand and ask to kiss her.]', "kiss"),
      c('[Take her hand and sit quietly together.]', "quiet"),
      c('"I care for other people too. I want to make these evenings possible without treating them carelessly."', "others")),
    n("others", "Seelah", '''"Then tell them when you're here, if they've been waiting for you. And tell me when you need to go."
{n}She leaves her hand where it is.{/n}
"I don't need to be the only person who makes you happy. I do want to know that you wanted this evening, and that nobody is sitting somewhere believing you forgot them."
{n}She smiles.{/n}
"If we have half an hour, I'd rather enjoy half an hour than spend it proving somebody owes me the whole night."''',
      c('[Take her hand and ask to kiss her.]', "kiss", flags=("seelah.aftermath_otherpartners",)),
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
      c('[Talk about what this means for the life you have already promised each other.]', "promised", requires=("seelah.committed",)),
      c('[Agree to talk about the future with what you now know.]', "consider", forbids=("seelah.committed",))),
    n("promised", "Seelah", '''"I still mean it. I wanted you to hear the difficult part before either of us starts mistaking a promise for knowing exactly how our lives will go."
{n}She gives your hand a small squeeze.{/n}
"And now you've heard it. You can remind me of the evening on the roof when I forget to ask for another one."''', c('[Keep making room for what you have learned about one another.]', flags=("seelah.aftermath_ready",))),
    n("consider", "Seelah", '''"Tomorrow, then. The harder conversation. I still want it."
{n}She gives your hand a small squeeze.{/n}
"For tonight, I'm glad we came."''', c('[Keep the evening and make time for the conversation.]', flags=("seelah.aftermath_ready",))),
], requires=("seelah.faith_spoken",))






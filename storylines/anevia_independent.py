"""Anevia's independent, adult, graphic and explicit campaign.

The native marriage, actors and dispatchers are preserved.
Scenes and all civilian events below are authored alternate developments.
"""
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
ANEVIA = "b5e867e13503c6f41bb1316705efb4a2"
IRABETH = "280d4712dceb37f4a88e98f1f4c6e64f"
A_ANSWERS = "33960c7f7af40cd43b7f801a76c87a0b"
I_ANSWERS = "871af36f2ab2b1f40b5de77976c54276"
RELATIONSHIP = dict(
    Title="Anevia: A life of her choosing",
    Description="Anevia has time for a conversation that is neither a report nor an invitation for somebody else. What she chooses to share is hers to decide.",
    Objective="Make time for Anevia",
    Guidance="Speak with Anevia in Drezen. Private invitations and decisions about her marriage develop through actual conversations. Other relationships remain your own.",
    StartedFlag="anevia.started", ClosedFlag="anevia.closed", CommittedFlag="anevia.committed",
    UnavailableFlags=["anevia_dead", "anevia_gone", "swarm", "true_lich"],
    FailureFlags=["anevia_dead", "anevia_gone", "inhuman"])
ETUDES = {"anevia.irabeth_killed_by_commander": "c0f261c4a259da741ab0052f0100c2a0"}
SCENES = []


def s(identity, title, nodes, *, requires=(), forbids=(), delay=24, owner="Anevia", chapters=(3, 5), any_of=(), remote=False):
    item = scene("anevia." + identity, title, owner, min(chapters),
        '"There was something I wanted to speak with you about."', nodes,
        requires=requires, forbids=("closed", "anevia.closed", "inhuman", *forbids),
        delay=delay, last=max(chapters), optional=True, Relationship="anevia",
        Chapters=list(chapters), RequiresAny=list(any_of), Remote=remote)
    if not remote:
        item.update(Areas=[DREZEN], AnswerLists=[I_ANSWERS if owner == "Irabeth" else A_ANSWERS],
                    ContactUnit=IRABETH if owner == "Irabeth" else ANEVIA)
        item["Forbids"].append("irabeth_away" if owner == "Irabeth" else "anevia_away")
    for page in item["Nodes"]:
        page["Portrait"] = "Irabeth" if page["Speaker"] == "Irabeth" else "Anevia"
    SCENES.append(item)
    return item


s("unborrowed_hour", "An hour she had not promised", [
    n("start", "Anevia", '''{n}Anevia is trying to repair a small wicker handle with a length of string. A basket rests on the chair beside her, empty except for a folded cloth and a knife in a wooden sheath. She looks up when you approach, then follows your glance to the knife.{/n}
"Bread knife. Before you ask who needs persuadin'."
{n}She draws the string tight. The handle slips sideways.{/n}
"Might be the basket."
{n}You offer to hold it still. Anevia makes room on the table, gives you the basket and starts the knot again. A runner appears at the door. She hears the woman's message, gives a short answer and waits until the footsteps have receded before looking back at you.{/n}
"That was the last thing I promised anybody for an hour. Beth's got her own plans. So have I, if this object can be convinced it used to carry things."
{n}The knot holds. She tests it twice, takes the basket from you and reaches for her coat.{/n}
"Want to come? Nothing to inspect. If somebody asks you to inspect something, you're allowed to disappoint 'em."''',
      c('"I would like an hour with you."', "street"),
      c('"What have you planned? I would enjoy being surprised."', "plan"),
      c('[Leave her to enjoy the hour. Ask another day.]', abort=True)),
    n("plan", "Anevia", '''"A woman sellin' pears told me they're too soft to sell tomorrow. I intend to find out whether she says that every day."
{n}She settles the basket over her elbow.{/n}
"There's also a bit of wall that gets the sun. No roof, no decent view, and people keep forgettin' to call it strategically important. I've been saving it."
"For what?"
"Apparently for this afternoon. You coming, or do I need to make the pears sound endangered?"
{n}She is already smiling when you take your place beside her. At the door she pauses to put back a report she has almost carried out by habit. She weighs the basket in its place, as though remembering what she wanted her hands to be full of.{/n}''', c('[Go with her.]', "street")),
    n("street", "Narrator", '''{n}Anevia takes the longer way to the market. She does not disguise the fact. At the first turning she points out the shorter route and leads you away from it, past a woman painting a repaired shutter and two children arguing over the ownership of an entirely uninterested cat.{/n}
{n}At the fruit stall she buys four pears. The seller adds a fifth with a split in its skin. Anevia asks whether the split makes it less respectable. The seller tells her to leave before the entire basket becomes a gift.{/n}
{n}The strip of wall is just as unremarkable as promised. A little sun remains on the stones. Anevia lays out the cloth, cuts the damaged pear into pieces and offers you the least bruised one.{/n}
"Don't look grateful. I'm givin' you the bit I don't have to explain."
{n}For several minutes there is the small business of eating fruit without losing it through your fingers. Anevia tries to catch a drop of juice with the cloth and succeeds in making the stain larger. She laughs at it, without checking whether you have laughed too.{/n}''',
      c('"I like that you wanted this enough to plan it."', "wanted"),
      c('"Do you always know a place to disappear?"', "disappear"),
      c('"I have a place I save for myself too."', "yours")),
    n("wanted", "Anevia", '''"Wasn't difficult. Wanted a pear. Wanted to sit down. Surprising how much of my life those two ambitions failed to occupy."
{n}She gives you another piece, then keeps one for herself.{/n}
"I do plan things that aren't useful. Not always very well. Beth once found a list of excuses I'd been makin' for not asking her out. Thought it was a surveillance schedule."
"Was it?"
"Only in the sense that I knew where she'd be."
{n}Her smile changes when she speaks of her wife. It becomes less guarded and more particular, as if she can see the expression she is describing.{/n}
"Took her to a place with terrible soup. We argued about the soup for weeks. Good evening, all things considered."
{n}She rests her elbow on the basket.{/n}
"This one hasn't got soup. Promising start."''', c('"Then let us give it something else worth remembering."', "watching")),
    n("disappear", "Anevia", '''"Most places, yes. I don't always want to use 'em."
{n}She looks along the street. A woman carrying a rolled carpet struggles through a doorway; a neighbor comes out to lift the far end. Anevia waits until the carpet is safely inside before continuing.{/n}
"Sometimes I want to sit somewhere everybody can see me and have nobody decide that means I'm available. There's a difference."
"You could have told me you wanted to be alone."
"Could've. Didn't."
{n}She lets the answer remain small. Then she nudges the basket toward your foot so a passing cart will not catch it.{/n}
"If I take you somewhere private, I'd like it to be because I wanted you there. Not because you worked out where I'd hide. I know you're good at finding things. You needn't demonstrate it every time."''', c('"Then I will wait to be invited."', "watching")),
    n("yours", "Anevia", '''"Tell me what you like about it. You can keep the directions."
{n}She shifts on the wall, giving you her attention without the alert stillness she brings to a report.{/n}
"Is it quiet? Or is it the sort of noise nobody expects you to answer?"
{n}You consider the question. The difference matters more than you expected.{/n}''',
      c('"Quiet. Sometimes I need a little time without being needed."', "quiet", flags=("anevia.commander_quiet",)),
      c('"People living around me. I like remembering they do that when I am elsewhere."', "noise", flags=("anevia.commander_company",)),
      c('"It is somewhere I can be bad at something without it becoming important."', "clumsy", flags=("anevia.commander_practice",))),
    n("quiet", "Anevia", '''"Then don't apologize when you want it. I might be disappointed if I came looking for you. I can survive a disappointing afternoon."
{n}She turns a pear in her hand, choosing where to cut.{/n}
"Would rather know you wanted quiet than spend the whole time wonderin' what clever thing I'm meant to say. I can make a terrible nuisance of myself when I think somebody needs cheering up."
"You?"
"I've been told. By reliable sources."
{n}She gives you an unhurried minute in which neither of you supplies another word. The street carries on. When she speaks again, she offers you another thin slice of pear.{/n}''', c('[Share a slice.]', "watching")),
    n("noise", "Anevia", '''"Then you'd have liked that soup place. Everybody had an opinion, and none of 'em involved us until Beth tried to defend the cook."
{n}She laughs at the memory.{/n}
"I like hearin' somebody complain about a roof, sometimes. Means they expect to be under it next month. We spend so much time listening for bad news that an ordinary complaint can sound almost indecent."
{n}The woman with the carpet reappears to argue with her neighbor about which way it should face. Anevia listens until they go inside again.{/n}
"There. Both wrong. Excellent argument."
{n}She looks at you rather than the doorway when she adds:{/n}
"I'd like more afternoons when that's the most urgent opinion either of us has."''', c('"So would I."', "watching")),
    n("clumsy", "Anevia", '''"That sounds dangerous. I might enjoy watchin'."
{n}She sees your expression and raises a hand.{/n}
"Not like that. Well, a little like that. But I could bring something I'm no good at too. Give you ammunition."
"A terrible bargain."
"Only if one of us starts keeping score."
{n}She tells you about a loaf she once attempted without asking anybody how much water went in. The account becomes less plausible as she describes it, until she admits that the part about breaking a knife belongs to somebody else's bread.{/n}
"Mine just sat there. Refused to become anything useful. Had to admire the conviction."
{n}Her laughter makes the afternoon feel longer, as though you have found a small use for time neither of you had put aside.{/n}''', c('[Tell her which part you would like to try together.]', "watching")),
    n("watching", "Anevia", '''{n}Anevia has stopped cutting the fruit. Her attention rests on you with an openness that makes the question unnecessary for a moment.{/n}
"I keep enjoying the part where you look pleased to see me."
{n}She folds the cloth around the knife, taking care with the edge.{/n}
"Could make a joke about your standards. Been thinking of several. None of 'em would answer the question."
"What question?"
"Whether I'd like another afternoon because you're good company, or because I want you looking at me like that again."
{n}She glances at the place where your hands almost meet on the wall.{/n}
"Both, I think. That's more of an answer than I meant to give before supper."''',
      c('"I am attracted to you. I want us to be honest about what that would mean."', "honest"),
      c('"I would like the company, without a romance."', "friend"),
      c('"We do not have to decide today. I would like another afternoon."', "wait")),
    n("honest", "Anevia", '''"Yes. We do."
{n}She does not take your hand. She rubs a nick in the basket handle with her thumb.{/n}
"I love my wife. That isn't a warning I'm obliged to give before pretending it doesn't matter. It's part of the answer."
"I heard you."
"Good. Because I haven't finished workin' out the rest. I won't bring Beth a decision and call it a question. And I won't bring you something she's agreed to and act as if that settles whether you want it."
{n}Anevia picks up the basket. This time the repaired handle holds without complaint.{/n}
"I'd like to talk again. Somewhere with fewer pears to hide behind. You can think about whether you meant it while I think about whether I know what I'm asking."
{n}On the way back she remains beside you. She does not pretend that the afternoon has become a mistake.{/n}''', c('[Agree to another honest conversation.]', flags=("anevia.courtship_requested",))),
    n("wait", "Anevia", '''"Another afternoon, then. With a question in it this time."
{n}She gathers the cloth and the empty fruit stems. A pear remains at the bottom of the basket, spared by all the talking.{/n}
"Taking this home. Beth will ask whether I enjoyed myself. I intend to say yes."
{n}Her look is direct.{/n}
"I did. I don't want the next conversation to make us ashamed of that part."
{n}You walk back at an easy pace. At headquarters she leaves you with the invitation still open, and enough time to decide whether you want to accept it.{/n}''', c('[Keep the invitation open.]', flags=("anevia.courtship_requested",))),
    n("friend", "Anevia", '''"All right. That answers it."
{n}She looks down briefly, then reaches for the basket.{/n}
"Might need to feel foolish about saying it for a day. You needn't help. I'm experienced."
"I liked the afternoon."
"So did I. We can keep that."
{n}She gives you the remaining pear and takes the knife herself. On the walk back, she finds something ordinary to complain about. You let the complaint be ordinary.{/n}''',
      c('[Keep the friendship. Decline romance with Anevia only.]', flags=("anevia.closed", "anevia.local_declined"))),
], forbids=("a_affair", "trying", "committed", "anevia.courtship_requested", "irabeth_dead", "irabeth_gone"), delay=0)


s("a_question_at_home", "The question before the answer", [
    n("start", "Anevia", '''{n}Anevia meets you with two mugs and no report. She puts one within your reach, tests the other and makes a face.{/n}
"Too hot. Been waiting long enough to ask you this that I thought I'd at least get the tea right."
{n}She sits opposite you.{/n}
"I told Beth there was somebody I'd begun wanting to see for reasons I couldn't file under work. Told her it was you. Didn't tell her we'd agreed to anything."
{n}She waits for you to answer.{/n}
"She asked whether I wanted to leave her. I said no. She asked whether I was asking her to be pleased. That took longer."
"What did you say?"
"That I'd like her to be pleased eventually. But I couldn't require it before she was allowed an opinion."
{n}Anevia cups her hands around the mug without drinking.{/n}
"I think that was the first useful thing either of us said."''',
      c('"What does she want from me?"', "wife"),
      c('"What do you want, now that you have said it aloud?"', "desire"),
      c('[Ask to leave this conversation for another day.]', abort=True)),
    n("wife", "Anevia", '''"An answer from you. Not one I've tidied up on the way across the room."
{n}She rubs at a mark on the mug with her thumb.{/n}
"She'll speak with you alone. About what you think you're asking for, and what happens if she says something you don't like. She's not arrangin' an interview for the position of my lover. I wouldn't put either of you through that."
"And if she cannot agree?"
"Then we find out what I meant when I said I wouldn't bring her a finished decision."
{n}Anevia looks up.{/n}
"I get to choose what I do. So does she. Doesn't mean nobody gets hurt. I'd rather we find out where it hurts now, over tea, than later, in a doorway."''', c('"Before I speak with her, tell me what you want."', "desire")),
    n("desire", "Anevia", '''"You. Separately. That's the bit I'm tryin' not to lose while we discuss arrangements."
{n}The directness leaves her briefly amused at herself.{/n}
"I'd like to find out whether you argue when you're comfortable. Whether you know how to leave an evening alone when it doesn't need improving. I'd like another walk, and to kiss you at the end without spending the walk inventing a reason I happened to be there."
"And at home?"
"I'd like to keep bein' Beth's wife. The woman who knows which boots hurt her and which sermon she's about to argue with. I don't want to start describing that life as inadequate just because I've found something else I want."
{n}She takes a cautious drink. The tea is finally cool enough.{/n}
"There. Doesn't fit in one sentence. I've been warned that makes a poor request."''',
      c('"I want a relationship with you. I am not asking Irabeth to become my lover."', "separate", flags=("anevia.wants_separate",), forbids=("irabeth.lover",)),
      c('"I could imagine caring for you both, but I have only earned this conversation with you."', "possible", flags=("anevia.group_possible",), forbids=("irabeth.lover",)),
      c('"I have other loves. I want to tell you what time and affection I can actually offer."', "other", flags=("anevia.other_loves_known",)),
      c('"Irabeth and I have a relationship. I want to hear your own answer without treating it as part of hers."', "her_marriage", requires=("irabeth.lover",), forbids=("irabeth.closed",)),
      c('"My romance with Irabeth ended. I will not use this invitation to reopen it through you."', "past_marriage", requires=("irabeth.lover", "irabeth.closed"))),
    n("past_marriage", "Anevia", '''"Then we'll need to be particularly clear about what we're asking. I don't intend to carry messages between you under the cover of having an evening with somebody I want."
{n}She considers you before continuing.{/n}
"Beth gets to say how she feels about this. You get to hear an answer that isn't arranged to make your earlier ending more comfortable. And I get to decide what I want after I've heard you both."
"I can accept that."
"Good. It won't make the conversations simple. I'd rather have the actual ones than a prettier account that leaves somebody out."''', c('[Keep the new question separate from the ended romance.]', "time")),
    n("her_marriage", "Anevia", '''"Good. I was hoping I wouldn't have to make that distinction sound more dignified than it is."
{n}She looks at you with a small, nervous smile.{/n}
"I know what you and Beth chose. That doesn't mean I know what you and I would be like. I'd like to find out because I want you, not because it would make our evenings easier to arrange."
"And if we eventually want time together?"
"Then we ask for it. All of us. Not tonight by implication while we're busy answering something else."
{n}Anevia rests her hand around the warm mug.{/n}
"I can be glad my wife has somebody she likes and still want an invitation with my own name on it. This is me asking for one."''', c('[Answer Anevia for herself.]', "time")),
    n("separate", "Anevia", '''"Tell her that. Clearly. She can hear a request for everybody else's sake in almost anything if she tries hard enough."
{n}Anevia leans back, considering you.{/n}
"I'd like you two to be able to sit in a room without either one thinkin' the other has come to collect me. I'd like you to disagree occasionally. About something as small as the way I carry a basket, preferably."
"You would take her side."
"Depends whether she's right. Also whether you've just dropped the basket."
{n}The humor leaves room for the practical concern beneath it.{/n}
"She doesn't have to want what I want. Neither do you. If this works, it'll be because we stopped making that the price of being in the room."''', c('[Ask what would make the arrangement worthwhile to her.]', "time")),
    n("possible", "Anevia", '''"Good. Keep the word 'could' where it belongs."
{n}She says it gently, then gives you a sharper smile.{/n}
"My wife isn't the second half of a bargain. She might fancy you. She might think you look better across a council table. I haven't asked her to decide for my convenience."
"I would not want that."
"Then don't arrive with a plan for three people when one of 'em agreed to a conversation. If something grows there, you'll have to grow it with her. I can't lend you the years I've spent lovin' her and have that count."
{n}She rests her hands beside the mug.{/n}
"I am asking what the two of us want. I'm enjoying that question more than I expected. Let me finish asking it."''', c('[Keep this conversation about Anevia.]', "time")),
    n("other", "Anevia", '''"Then tell me which promises already have somebody's name on them. You needn't tell me their private business."
{n}She listens while you describe what you can offer. Once she stops you when an answer becomes more impressive than precise.{/n}
"One evening you keep is a better offer than all the time you don't have."
{n}She thinks for a moment.{/n}
"I'd like to be told if a plan changes. I'd like not to be the person who always gets moved because she knows enough about the crusade to understand. I can understand and still mind."
"You may have to change plans too."
"I will. Then you'll be allowed to mind. We can be inconvenient to each other without making somebody else's existence the offense."''', c('"Then let us speak about the time we can keep."', "time")),
    n("time", "Anevia", '''"I want evenings at home that aren't the empty places between your visits. For Beth and me. I want evenings with you that aren't all spent apologizing for going home."
{n}She reaches for the teapot, finds it empty and laughs under her breath.{/n}
"And apparently I want to learn how much tea two people drink while they talk about this."
{n}You fetch more water together. She lets you carry the pot and takes the mugs, declining your attempt to balance all three. The small division of work makes the conversation easier to continue.{/n}
"I'd like to see you doing something you chose," she says. "Not just the things I figured you'd like. Kenabres, the year before the Heart: I spent a month bein' exactly the barmaid a cultist wanted to talk to. Laughed at his jokes. Liked his wine. Got so good at it I forgot I hated his wine. Took me weeks after to remember what I did like."
{n}She sets the mugs down in their old places.{/n}
"If you see me doing that, you can ask. Don't congratulate yourself on catching me. Just ask."''',
      c('"I will ask what you wanted before I assume you are offering what I want."', "finish"),
      c('"I do it too. Sometimes it is easier to be useful than to say what I want."', "useful"),
      c('"I have thought about it. Friendship is what I can offer."', "stop")),
    n("useful", "Anevia", '''"I know. Was trying not to make a speech about it."
{n}She gives you a rueful look.{/n}
"You showed up with empty hands. I handed you a basket to fix. We could be magnificent at this for years and never notice."
{n}She places the pot where neither of you needs to tend it.{/n}
"Then here's something I want. When you come to see me next, don't bring a reason I have to admire. Bring whatever mood you're in. I'll try to have one that hasn't been prepared for visitors."
"That may go badly."
"Could be a very informative evening."
{n}For a moment her hand almost reaches across the table. She catches the movement, considers it, and leaves her palm open beside the mug instead.{/n}
"Soon, if we decide we can. I am not patient by nature. I'm making an effort."''', c('[Tell her you want to make the effort too.]', "finish")),
    n("finish", "Anevia", '''"I'll tell Beth you're willing to speak with her. You can find her when she has time; this doesn't have to become the most urgent matter in headquarters."
{n}She rises with you, then pauses beside the door.{/n}
"Whatever she says, don't explain my marriage to me afterward. You can tell me how you felt. I might disagree with your interpretation. I'd still like to hear it."
{n}You agree. She smiles, relieved and still a little nervous.{/n}
"Good. That's one invitation made honestly. I knew we'd get something done if we sat here long enough."''',
      c('[Arrange the conversation with Irabeth.]', flags=("anevia.spousal_conversation_requested",))),
    n("stop", "Anevia", '''{n}Anevia lets the silence last before answering.{/n}
"I am disappointed. I don't think you'd thank me for pretending otherwise."
{n}She moves your mug away from the edge of the table, an absent practical kindness.{/n}
"But I'm glad you said it here. I'll tell Beth the question has changed. You needn't go make a case for declining me."
"I did want the afternoons."
"So did I. Give me a little time before we arrange another. I intend to be very mature about this after I've had a chance not to be."''',
      c('[End only Anevia\'s romantic courtship.]', flags=("anevia.closed", "anevia.local_declined"))),
], requires=("anevia.courtship_requested",), forbids=("a_affair", "trying", "committed", "irabeth_dead", "irabeth_gone"))


s("one_truth", "The person who was not told", [
    n("start", "Anevia", '''{n}Anevia shuts the door, then moves away from it before speaking. She does not ask you to sit.{/n}
"We said we'd tell her. I've been hearing that sentence whenever somebody asks me how my day's been."
{n}She looks tired, and impatient with her own tiredness.{/n}
"I told Beth there was something she needed to hear from both of us. She asked if you and I had been together. I said yes. I didn't leave her guessing so we could arrange a better scene."
{n}The room is quiet enough that you can hear a cart being unloaded outside.{/n}
"She wants to speak with you. Alone. I've told her what I did. She wants to hear what you thought you were doing."
"How did she take it?"
"Badly. How would you like me to describe it?"
{n}Anevia rubs her hands together once, then stops.{/n}
"Sorry. That was an answer meant for me."''',
      c('"I will tell her the truth. I will not ask you to make it easier for me."', "account"),
      c('"Do you still want me?"', "want"),
      c('"Then perhaps we should keep our distance and let this disappear."', "disappear"),
      c('[Postpone the conversation without changing the history.]', abort=True)),
    n("want", "Anevia", '''"Yes. That's part of why I owe her a better answer than saying it didn't matter."
{n}She meets your eyes.{/n}
"I won't tell her you meant nothing to make what I did smaller. I won't tell you she means less to make you feel secure. Both of you would know I was lyin'."
"I was afraid you regretted all of it."
"I regret deciding she didn't get to know. I have other feelings about you. They haven't arranged themselves neatly for the occasion."
{n}Her mouth twists, almost a smile.{/n}
"I wanted to see you this morning. Then I was angry that I wanted it. Then I came anyway, because avoiding you wasn't going to make the conversation honest. That's as clear an account as I have."''', c('"Then let us give her an honest one too."', "account")),
    n("disappear", "Anevia", '''"It won't disappear for her. It'll just become something she's expected to know without asking about."
{n}Anevia's voice is low.{/n}
"You can decide you don't want a relationship with me. You can't decide that makes the truth unnecessary. I'll speak with her whether you come or not."
{n}She waits, giving you the unpleasant space in which to choose your answer.{/n}''',
      c('"You are right. I meant to avoid being present for the harm."', "account"),
      c('"I will not continue the romance. Tell her that too."', "stop")),
    n("account", "Anevia", '''"Don't make it a speech about how complicated love is. She knows. Been married to me for years."
{n}For the first time a trace of humor reaches her face, then passes.{/n}
"Tell her what happened. Answer what she asks. If there's something that belongs to my private life, say so without using that as an excuse to conceal what you did. You can be honest without handing over every touch like an inventory."
{n}She walks to the window and opens it far enough to hear the street.{/n}
"I asked whether she'd rather I slept somewhere else tonight. She said she'd rather I stopped deciding what she wanted before she'd said it. So I'm going home. We'll probably argue. Might sit in different rooms for an hour. That's still going home."
"And us?"
{n}Anevia turns back toward you.{/n}
"We stop arranging secret evenings. We find out what remains when everybody gets an answer. I don't know what that is yet."
{n}She picks up her coat, which has been lying over the back of a chair.{/n}
"I would like to find out. You should know that much before you go."''',
      c('[Agree to speak with Irabeth about this actual affair.]', flags=("anevia.spousal_conversation_requested", "anevia.single_affair_disclosed"))),
    n("stop", "Anevia", '''{n}Anevia closes her eyes for a moment.{/n}
"All right. I'll tell her."
{n}When she opens them, she looks at you steadily.{/n}
"I am not going to call it a kindness. It may be the right answer. It still hurts. Give me room to discover both things without trying to arrange my expression for me."
{n}You leave her with the conversation she has chosen to have at home. The history does not become innocent because the romance has ended.{/n}''',
      c('[End only Anevia\'s romance, retaining the actual affair history.]', flags=("anevia.closed", "anevia.local_declined"))),
], requires=("a_affair", "a_morning", "a_will_tell"), forbids=("i_affair", "trying", "committed", "anevia.spousal_conversation_requested", "irabeth_dead", "irabeth_gone"), delay=0)


s("beths_question", "An answer that is hers", [
    n("start", "Irabeth", '''{n}Irabeth has chosen a small room without a council table. Two chairs stand beside a window. She has removed her gloves, but folded them so precisely that their fingers lie one over the other.{/n}
"Thank you for coming. Anevia is not waiting outside. I asked for this conversation without an audience."
{n}She gestures to the other chair and waits until you sit.{/n}
"I have spent much of the morning deciding what a reasonable person would say. It has not been a useful exercise. I would rather tell you what I mean, even if I need to begin a sentence twice."
{n}Her hands rest on her knees.{/n}
"This is not a matter on which your rank gives you an answer. I need to know that you understand it before we discuss anything else."''',
      c('"You are free to disagree with me. It will not affect your command."', "history"),
      c('"Of course. I expect you to remain loyal despite this."', "rank"),
      c('[Ask to speak when you can give the conversation your full attention.]', abort=True)),
    n("rank", "Irabeth", '''"Then we have not understood each other."
{n}She rises. The motion is controlled, but there is nothing uncertain about it.{/n}
"I will continue to do my duty. You do not obtain a claim on my wife by reminding me of it."
{n}She picks up the gloves.{/n}
"If that is what you meant, this conversation is over. If it is not, explain without telling me what I am expected to feel."''',
      c('"I used the wrong language because I was uncomfortable. Your answer is yours."', "history"),
      c('"I meant it. This should not interfere with your obligations."', "refused")),
    n("history", "Irabeth", '''{n}Irabeth draws her chair a little closer to the window and settles with her hands in her lap, giving herself a moment before she continues.{/n}
"Anevia has told me what brought us here. I want your account of your part in it."
{n}She does not ask you to begin with an assurance that nobody intended to hurt anybody. Her expression suggests she has already considered how little that assurance would tell her.{/n}''',
      c('"We want to court one another. We have waited to speak with you before beginning a romantic relationship."', "before", forbids=("a_affair",)),
      c('"We crossed a boundary while you did not know. I knew she was keeping it from you, and I took part."', "after", requires=("a_affair", "anevia.single_affair_disclosed"))),
    n("before", "Irabeth", '''"I appreciate being told before I have to discover it. I am not yet certain what to do with the information."
{n}She looks toward the window, where the light catches a worn place in the frame.{/n}
"I keep trying to decide whether my first feeling is the correct one. That is apparently another way to avoid telling you what it is."
"What is it?"
"Fear. Followed by irritation that I am frightened. I know she loves me. I know that wanting something else does not automatically make a person dissatisfied with everything she has. I can explain all of that quite convincingly."
{n}A brief, rueful smile appears.{/n}
"I can still picture being the person who understands so well that nobody remembers to ask whether she is lonely. I dislike that picture. I would rather say so now than become silently admirable about it."''', c('"What would you need us to understand?"', "needs")),
    n("after", "Irabeth", '''{n}Irabeth looks down at her hands. When she speaks, her voice is careful enough to make each word distinct.{/n}
"Thank you for not beginning with what I failed to provide."
"That was not the reason."
"I know. I have been trying to remember it without asking Anevia to comfort me for what she did. She has offered. I am not always ready to accept."
{n}She turns one hand palm upward, then lets it rest.{/n}
"I was making plans while the two of you knew something that would have changed them. Small plans. An evening. Whether I should wait for her before eating. I do not need a catalogue of your intimacy. I need you to understand that I was present in the life around it."
{n}Her gaze returns to yours.{/n}
"I love her. I am angry with her. You do not need to help me choose which feeling is more dignified."
"I will not."
"And I do not know yet whether I can welcome a relationship that began by excluding me from a decision about my own marriage. I am willing to ask the question. That is what I can offer today."''', c('"Tell me what you need me to hear before you decide."', "needs")),
    n("needs", "Irabeth", '''"I need my home to remain somewhere I am expected, not somewhere I arrive at the wrong time. I need an evening with my wife that does not become available to somebody else because I was slow to claim it."
{n}She pauses, then shakes her head at her own wording.{/n}
"That sounds as though we were dividing supplies. I do not want to live by a ledger. I want to be considered before a plan is settled. There is a difference."
{n}Outside, somebody calls to a friend in the yard. Irabeth listens until the answer comes, using the interruption to gather her next thought.{/n}
"I also need to be able to change my mind about what is comfortable without making every difficult evening a threat to the whole arrangement. And I need Anevia to speak for herself, rather than the two of us negotiating what she ought to want."
"She asked the same of me."
"Yes. She has become rather particular about it. I cannot say I disapprove."''',
      c('"I am asking for a relationship with her. You owe me neither romance nor cheerful approval."', "not_courtship", forbids=("irabeth.lover",)),
      c('"What would happen if you decided you could not live with it?"', "refusal"),
      c('"Would you like to know what time I can honestly offer, including my other commitments?"', "practical"),
      c('"You and I have chosen a relationship too. That does not answer this question for you."', "already_lovers", requires=("irabeth.lover",), forbids=("irabeth.closed",)),
      c('"Our romance ended. I am not asking Anevia to carry a request to begin it again."', "past_lovers", requires=("irabeth.lover", "irabeth.closed"))),
    n("past_lovers", "Irabeth", '''"I needed to hear that. I would rather not discover I was expected to understand it from everybody's good intentions."
{n}She allows herself a moment before continuing.{/n}
"Our ending may affect how some of this feels. I will not pretend otherwise. It does not decide what Anevia wants, and I will not ask her to choose my answer simply because she is my wife."
"What should I do?"
"Be clear. Do not use an invitation from her as a reason to arrive in my private life without asking. And hear what I actually say, rather than deciding that every difficulty is the old argument in disguise."
{n}She looks toward the gloves, then back at you.{/n}
"We have a new question to consider. We can at least consider it honestly."''', c('[Discuss the present request and its actual terms.]', "practical")),
    n("already_lovers", "Irabeth", '''"No. It does not. I am glad you understand that."
{n}She looks at you with familiar affection, without allowing it to finish the conversation for her.{/n}
"I want our time together. I want my marriage. Now Anevia is asking for something with you that is hers to choose. I can imagine enjoying what grows between all of us, but imagination is not an agreement about every evening or every room."
"We can keep the questions separate."
"We should. I would not like to discover that I had promised a shared household because I was pleased to see you with my wife. Let us decide what we are actually being asked, and leave the larger invitation until somebody chooses to make it."
{n}Her hand briefly covers yours, then returns to her lap.{/n}
"I would like to answer as both the woman you know and Anevia's wife. Neither has to disappear while the other speaks."''', c('[Discuss the actual plans without presuming a triad.]', "practical")),
    n("not_courtship", "Irabeth", '''"Good. Because I have been wondering whether I would eventually be expected to be grateful for an invitation."
{n}She gives you a level look, allowing the awkwardness to belong to both of you.{/n}
"I can like you without wishing to court you. I can care for Anevia without turning everything she wants into something I must want too. I would like those possibilities to remain ordinary."
"They will."
"Then I would also like you to remain somebody I can disagree with about things that have nothing to do with this. If every argument over a patrol becomes a private message, we will all become unbearable."
{n}The smile that follows is brief, but real.{/n}
"I have enough experience of our household to make that prediction with some confidence."''', c('[Discuss the actual visits and promises.]', "practical")),
    n("refusal", "Irabeth", '''"Then I would tell her. She would decide what she could offer me, and I would decide whether I could live with it. Neither answer would be yours to overrule."
{n}She does not make the possibility sound easy.{/n}
"I do not want to leave her. I am not threatening to do it so that somebody will hurry to reassure me. But if I pretend there is no possible answer I could refuse, this is not a conversation. It is an announcement with better manners."
"And if the answer is no?"
"I would rather you heard it than found a flattering description of yes. I am asking for time because I have not reached it yet."
{n}She unfolds her gloves, then folds them differently.{/n}
"I hope you understand that wanting time is not an invitation to make a more persuasive speech."''', c('"Then let us discuss what you need to consider, and leave you that time."', "practical")),
    n("practical", "Irabeth", '''{n}You describe the visits you could keep. Irabeth asks what happens when duties intervene, and whether either of you intends to use her knowledge of those duties as a reason she must never object. You describe where you could leave word and ask how she prefers to be reached.{/n}
{n}She tells you about an evening Anevia had meant to spend teaching her a card game. Work interrupted it three times. By the end Irabeth knew every rule and had enjoyed none of the game. Anevia finally took away the cards and asked when she intended to stop pretending she had been present.{/n}
"She was right. I have my own habits to change. I do not want to discover that a new arrangement only gives us more elegant reasons to keep them."
{n}You talk until the light has moved across the window frame. There are no signatures to put on the result. Irabeth has written down one proposed evening, then crossed it out when you remember a prior obligation. The correction seems to reassure her more than your first answer did.{/n}
"Thank you for remembering before it became somebody else's fault."
{n}She leaves the page unfinished.{/n}
"I will speak with Anevia. Give us a little time. Then I will tell you what I can agree to. I would rather you heard it from me."''',
      c('[Give them time, with no promised romantic outcome.]', flags=("anevia.spouse_heard",))),
    n("refused", "Irabeth", '''"Then I will tell Anevia precisely what you said."
{n}Irabeth opens the door. Her posture has the formality of a military dismissal, though she has used no title.{/n}
"She asked me to hear you. I have. Do not mistake my willingness to continue the work of the crusade for agreement about our private lives."
{n}The proposed courtship ends here. It does not become an instruction to alter her command or punish either woman.{/n}''',
      c('[Accept the end of Anevia\'s independent courtship.]', flags=("anevia.closed", "anevia.authority_refused"))),
], requires=("anevia.spousal_conversation_requested",), forbids=("irabeth_dead", "irabeth_gone"), owner="Irabeth")


s("beths_answer", "What she can agree to", [
    n("start", "Irabeth", '''{n}This time Irabeth meets you at the end of an ordinary working day. She puts away the last paper before speaking. The deliberate pause keeps the two conversations separate.{/n}
"Anevia and I have talked. Several times. On the second evening she asked whether we could spend an hour doing something else, and I discovered that I had mistaken continuing to speak for making progress."
{n}She smiles faintly.{/n}
"We played the card game. She won. I believe she would have found losing under the circumstances intolerable."
{n}Her expression becomes serious again.{/n}
"I can agree to her courting you. With an understanding about our home and our time together. She can invite you to a room of her own without making our room something I must avoid. Our plans remain plans, not the time she has left over. Yours should receive the same consideration."
{n}She waits for you to hear the whole answer.{/n}
"I have not promised to enjoy every part of learning this. I have promised to say what I mean instead of expecting her to discover it from my silence."''',
      c('"Are you agreeing because you want to try, or because you fear losing her?"', "choice"),
      c('"I can keep those terms. I want your home to remain yours."', "history"),
      c('"I have reconsidered. I should not begin this relationship."', "decline"),
      c('[Leave the decision unrecorded and continue another day.]', abort=True)),
    n("choice", "Irabeth", '''"Both were part of the question. I would distrust an answer that pretended fear had never entered the room."
{n}She considers how to continue.{/n}
"Anevia asked what I would choose if I knew she would not leave me for saying no. I was angry with her for asking a question I could not answer immediately. Then she told me she was willing to wait while I tried."
"And now?"
"Now I want to try this. I want a marriage in which we tell each other what we want while there is still time to decide what to do. I want to keep the woman who tells me those things, rather than a version of her who has learned which desires make me comfortable."
{n}Irabeth looks directly at you.{/n}
"That does not mean I would accept every arrangement she proposed. I refused the first idea about moving our evenings around at the last moment. She thought about it and agreed. I have not lost the ability to say no."''', c('"Then I will take the answer you have chosen to give."', "history")),
    n("history", "Irabeth", '''{n}Irabeth rests one hand on the back of her chair.{/n}
"There is one more thing I want said plainly before we leave this conversation."''',
      c('[Hear what remains after the affair.]', "hurt", requires=("a_affair",)),
      c('[Hear what remains uncertain about the new arrangement.]', "uncertain", forbids=("a_affair",))),
    n("hurt", "Irabeth", '''"This agreement does not make the earlier secrecy something I agreed to. I am still angry about it. Anevia knows that."
{n}Her voice remains steady.{/n}
"Some evenings I can accept her hand without remembering the question I did not know to ask. Some evenings I remember. We have agreed not to call either kind of evening the final verdict on our marriage."
"What do you need from me?"
"To keep your word now. To answer honestly if something changes. And not to ask me to perform forgiveness so that the two of you can feel certain it has happened."
{n}She straightens the back of the chair, which was already straight.{/n}
"I can wish you a good evening with her and still have a difficult one myself. I would like to be trusted with that complexity."''', c('"I will not ask you to make the past easier to describe."', "finish")),
    n("uncertain", "Irabeth", '''"I do not know whether this will be easy. I suspect it will be easier on some days than others."
{n}She gives you a small, wry smile.{/n}
"Anevia says that is also her experience of being married to me. She did not say it gently enough to be entirely reassuring."
"Did you object?"
"Yes. Then I remembered the argument I had begun about the proper place for a wet cloak."
{n}The smile lingers.{/n}
"I do not need the three of us to become an example of anything. I would like our promises to become ordinary enough that we keep them without discussing what remarkable people we are for having made them."
{n}She leaves the chair alone.{/n}
"You may tell me if I start making a speech. I would prefer a discreet warning."''', c('"I can promise discretion about speeches."', "finish")),
    n("finish", "Irabeth", '''"Then speak with her. She will have an answer of her own."
{n}Irabeth picks up the last of her papers, then puts it down again.{/n}
"And Commander? This need not be the only thing we ever speak about privately. I am still capable of an opinion about a book or a badly repaired gate. You may bring either subject without fearing that I intend to examine your conduct."
{n}You suggest an afternoon. Irabeth checks it against her duties, then asks whether the weather is likely to hold.{/n}
"Good," she says. "The gate really is badly repaired. I have been trying not to sound like myself about it all afternoon."''',
      c('[Respect her chosen agreement and speak with Anevia.]', flags=("anevia.marital_terms_agreed",))),
    n("decline", "Irabeth", '''"Then tell Anevia. Kindly, and without telling her it was my decision."
{n}She pauses before adding:{/n}
"You are allowed to change your mind. She is allowed to be hurt by the answer. I would rather neither of you used me to avoid that conversation."
{n}You agree to speak with Anevia yourself. Irabeth does not turn your refusal into a favor for which she must thank you.{/n}''',
      c('[End only the proposed romance with Anevia.]', flags=("anevia.closed", "anevia.local_declined"))),
], requires=("anevia.spouse_heard",), forbids=("irabeth_dead", "irabeth_gone"), delay=72, owner="Irabeth")


s("her_own_answer", "The invitation she kept", [
    n("start", "Anevia", '''{n}Anevia has borrowed a room with a table too large for it and a window that refuses to close completely. She demonstrates the second defect as soon as you arrive.{/n}
"In case you were expecting a seduction conducted in perfect comfort."
{n}A folded cloth on the sill keeps the frame from rattling. Two cups and a plate of sliced fruit occupy one end of the table. At the other lies a shallow wooden box, empty except for a scrap of sandpaper.{/n}
"Beth said she'd spoken with you. I told her I intended to ask you here. She said she hoped I'd remember to eat something before becoming eloquent."
{n}Anevia indicates the plate.{/n}
"Precautions."
{n}She waits while you put aside your things, watching you with a smile that becomes quieter when you return her attention.{/n}
"I still want this. That seemed worth saying before I found something clever to do with my hands."''',
      c('"I want you too. What were you planning for the box?"', "box"),
      c('"I have been thinking about kissing you all the way here."', "want"),
      c('[Ask to postpone the evening without changing the agreement.]', abort=True)),
    n("box", "Anevia", '''"Growing something. Probably killing it first, then asking somebody what I did wrong."
{n}She lifts the box, turning its rough edge toward the light.{/n}
"A woman at the market has cuttings of a herb she uses in soup. Smells better than our cook's entire cupboard. She said I could have one when I found somewhere for it."
"A garden?"
"A box. Let's not promote it before it's survived me."
{n}She rubs the edge with the sandpaper, then stops to brush a few pale grains off her sleeve.{/n}
"I like the idea of something that needs doing every day and doesn't involve keeping a list of who might die if I forget. Though she did say not to drown it. There are apparently limits to its patience."
{n}She sets the box down.{/n}
"You can help with the edge. Or you can sit there and keep me company while I do it badly. Neither answer is an examination."''',
      c('[Hold the box while she smooths the edge.]', "working", flags=("anevia.box_helped",)),
      c('"I would like to watch you make something for yourself."', "watching", flags=("anevia.box_watched",))),
    n("working", "Narrator", '''{n}You brace the box while Anevia works along the rough edge. She is patient with the wood and less patient with your suggestions. After the third one she raises her eyes to yours.{/n}
"You can hold it very expertly without tellin' me where every splinter is. I'm becoming acquainted with them."
{n}You apologize. She gives the box a little tug to make sure you have not interpreted that as a request to let go.{/n}
"There. Useful disagreement. Nobody resigned."
{n}When the edge is smooth, she runs her thumb over it, looks pleased and immediately finds another rough place. This time she points it out herself before you can mention it. By the time she is satisfied, a little heap of dust has gathered on the cloth beneath your hands.{/n}
{n}She folds the dust into the cloth and sets the box on the sill. It fits imperfectly. She turns it around, discovers that the other way is worse, and returns it to the first position.{/n}
"A home," she says. "With faults. That ought to keep it from getting above itself."''', c('[Sit with her when she has finished.]', "want")),
    n("watching", "Anevia", '''"Then I'll try not to start performing competence for you. Could take all evening."
{n}She works while you talk. Once she stops to tell you about a lock whose owner had insisted it could not be opened, then catches herself turning the story into proof that she knows how to use her hands.{/n}
"Listen to me. Nobody asked."
"I liked the story."
"So did I. That's how I get away with it."
{n}She finishes the edge without supplying another credential. When she lifts the box toward you, her expression asks whether you like it rather than whether you are impressed. You tell her which small unevenness you like. She argues that you have chosen the worst part, then leaves it as it is.{/n}
"Fine. It can remind me somebody was there while I made it."
{n}She places the box on the sill and returns to the table.{/n}''', c('[Make room beside you.]', "want")),
    n("want", "Anevia", '''{n}Anevia comes nearer, leaving enough space that you can answer without moving away.{/n}
"I had plans for how to ask this. None of them survived you arriving."
{n}Her fingers brush the back of your hand.{/n}
"May I kiss you?"
{n}She asks without making light of the question. The careful preparations, the badly fitting window and the unfinished box are forgotten while she waits for your answer.{/n}''',
      c('"Yes. I would like that."', "kiss"),
      c('"Come sit close. I would like to begin there."', "near"),
      c('"I cannot offer the relationship we have been discussing."', "stop")),
    n("kiss", "Narrator", '''{n}She kisses you with the confidence of someone who has been patient long enough to know what she wants. Her hand settles at the side of your neck. When you move closer, she makes a small pleased sound and lets the kiss last until both of you are smiling against it.{/n}
"That's going to make the rest of my eloquence difficult."
{n}You tell her she can attempt it later. She kisses you again before agreeing. When she draws back, she keeps her forehead near yours for a moment, looking at you from a distance that makes her usual quick deflections seem unnecessary.{/n}
"I wanted that."
"I noticed."
"Good. Wasn't aiming for subtle."
{n}She sits beside you, her knee resting against yours. Outside, the wind rattles the frame until the folded cloth catches it. Anevia glances toward the window, then turns back without getting up to improve anything.{/n}''', c('[Stay close and ask what she would like from this evening.]', "evening", flags=("anevia.first_evening_kissed",))),
    n("near", "Anevia", '''"Then there. I can manage that without a speech."
{n}She takes the place beside you. At first your shoulders touch only when one of you moves. Then she settles more comfortably against you, and the contact becomes deliberate.{/n}
"If you change your mind about the kiss, ask. If you don't, I can still have a very agreeable evening."
{n}You ask whether the box is likely to survive the plant. She tells you that the woman supplying the cutting has expressed more concern about the plant surviving the box. The account becomes an argument about which of them has less faith in Anevia's talents, and Anevia supplies both sides with considerable enjoyment.{/n}
{n}She remains close while she speaks. Nothing in her manner treats your choice as an interval she must endure before you offer something better.{/n}''', c('[Enjoy the closeness she chose.]', "evening")),
    n("evening", "Anevia", '''"I'd like you to tell me something you thought today and didn't say because it wasn't important enough."
{n}She considers the request, then adds:{/n}
"Not a confession. A thing. Something that irritated you, or made you laugh, or had you wishing you'd taken the other street."
{n}You find an example. She asks a question you did not expect, and the answer becomes a story rather than the brief explanation you had prepared. When your account ends, she offers one of her own. It concerns a woman who wanted to sell her an extremely conspicuous coat for discreet work.{/n}
"Apparently nobody would suspect a spy of having such poor judgment."
{n}You ask whether she bought it.{/n}
"Couldn't afford to be that inconspicuous."
{n}Later she touches your hand and asks when you would like to see her again. You choose a day you can actually keep. She checks her own promises before agreeing, and neither of you treats the pause as a retreat.{/n}
"Good," she says. "I'd like to have something to look forward to that isn't an intercepted letter."''',
      c('[Choose this relationship with Anevia, with her marriage and other lives intact.]', flags=("anevia.lover", "anevia.personal_ready"))),
    n("stop", "Anevia", '''{n}Anevia withdraws her hand and sits in the other chair.{/n}
"Then tell me now. Before I begin remembering this evening as something it wasn't."
{n}You explain as well as you can. She listens, asks one question, and accepts the answer without making it pleasant for either of you.{/n}
"You should go. I'll be all right. That doesn't mean I want company while I discover how disappointed I am."
{n}You leave. Inside, she pushes the other chair back beneath the table.{/n}''',
      c('[End only Anevia\'s romance.]', flags=("anevia.closed", "anevia.local_declined"))),
], requires=("anevia.marital_terms_agreed",), forbids=("anevia.personal_ready", "irabeth_dead", "irabeth_gone"))


s("a_place_of_our_own", "A date that belongs to two people", [
    n("start", "Anevia", '''{n}Anevia catches you at the end of a conversation about a future that includes more people than fit comfortably around most tables.{/n}
"I'd like an evening with you. Just you. Not because anything's wrong with the other sort. Because this is a thing I want too."
{n}She rests a hand on the back of an empty chair.{/n}
"We've spent enough time asking what the three of us can manage. I don't want to find out I've stopped asking whether you and I have a good time when nobody else is there to keep the conversation moving."
{n}Her smile softens.{/n}
"I think we do. I'd like to give myself some evidence."''',
      c('"I would like that. We do not have to start our courtship over."', "history"),
      c('"Does Irabeth know you are asking?"', "wife"),
      c('[Leave the invitation for another evening.]', abort=True)),
    n("wife", "Anevia", '''"Yes. She looked at me as if I'd asked permission to have a favorite kind of weather."
{n}Anevia's imitation of her wife's solemn expression is affectionate and not quite fair.{/n}
"We agreed we'd have time separately. I'd like to use some of it. Beth can ask for the same thing without either of us standing outside counting the minutes."
"I did not mean to suggest otherwise."
"I know. It's worth saying. I can turn an invitation into a committee meeting if I try hard enough."
{n}She slides the empty chair back toward the table.{/n}
"No committee tonight. Two people, something to eat, and an opportunity to discover whether you tell the same stories when there's only one person to interrupt."''', c('[Accept the individual invitation within the actual existing relationship.]', "history")),
    n("history", "Anevia", '''"We don't have to pretend the difficult parts happened to somebody else, either."
{n}She considers you for a moment, then adds:{/n}
"I'm not asking you here to do penance. I'd like to have a pleasant evening without insisting it proves everything has always been simple. We can manage both."
{n}When you meet later, she has found a room with a table too large for it and a window that will not quite close. A shallow wooden box stands on the sill. She tells you she intends to grow a herb in it, then immediately lowers that ambition to keeping a herb alive long enough to learn its name.{/n}
"You can laugh. I have been assured it's a very patient plant."
{n}You sit together. Anevia puts aside the scrap of sandpaper she has been using on the box and gives you her attention.{/n}
"Tell me what you'd like from an evening that's ours."''',
      c('"Something quiet, where we do not have to fill every pause."', "quiet", flags=("anevia.commander_quiet",)),
      c('"Something ordinary. I like seeing you choose what you enjoy."', "ordinary", flags=("anevia.commander_company",)),
      c('"Something we have not learned to do. I want a reason to laugh at myself with you."', "ordinary", flags=("anevia.commander_practice",))),
    n("quiet", "Narrator", '''{n}She moves her chair close enough that your shoulders touch and leaves the next silence alone. The room has its own small sounds: wind at the window, footsteps below, the occasional tap of the box as it shifts on the uneven sill.{/n}
{n}After a while you tell her something that had seemed too small to mention during the day. She asks about it without turning it into a problem to solve. Her reply wanders into a memory of a room she once disliked, then into the particular noise that made her remember it fondly years later.{/n}
"There. A whole account with nothing useful in it. You bring out terrible habits."
{n}She kisses your cheek, then settles against you again.{/n}''', c('[Keep the quiet evening with her.]', "end")),
    n("ordinary", "Anevia", '''"Then you may help me decide whether that box is crooked or the sill is."
{n}You investigate together. Turning the box changes which corner lifts; moving it along the sill improves nothing. Anevia finally folds a scrap of cloth beneath one edge and declares the matter settled.{/n}
"A triumph of practical knowledge over architecture."
{n}You ask whether she intends to put that in her report.{/n}
"Only if I can blame you for the delay."
{n}She sits close afterward, her hand resting openly on yours. You talk about things neither of you needs to remember accurately tomorrow. Anevia allows herself to lose an argument about a song, then hums the disputed part incorrectly until you begin laughing again.{/n}''', c('[Stay close when the argument has become a joke.]', "end")),
    n("end", "Anevia", '''"Another evening, then. When we can keep it."
{n}She says it before either of you rises. You choose a day, check the promises already occupying it, and agree on a time that belongs to neither an apology nor an emergency.{/n}
{n}At the door she kisses you with unhurried affection.{/n}
"I like you when there's nobody else here. Thought you should have that in writing, but this seemed better."
{n}The shared relationship remains what you actually chose. This evening has given the two of you something of your own inside it, without rewriting how you arrived.{/n}''',
      c('[Continue the earned personal relationship with Anevia.]', flags=("anevia.lover", "anevia.personal_ready"))),
], any_of=("trying", "committed"), forbids=("anevia.personal_ready", "irabeth_dead", "irabeth_gone", "tirabade.group_closed"), delay=0)


s("an_invitation_afterward", "The question she asked separately", [
    n("start", "Anevia", '''{n}Anevia asked you to come after the three of you had finished the conversation about a shared arrangement. She meets you alone, in a room she has chosen for this different question.{/n}
"I'm glad you came. Was trying not to turn an invitation into a test of whether you understood it."
{n}She indicates the chair beside hers.{/n}
"I'd like us to say what we're asking now. Without pretending the earlier conversation didn't happen, and without making it decide an answer we haven't given."''',
      c('[Acknowledge the shared relationship that has ended.]', "ended", requires=("trying",)),
      c('[Acknowledge the shared arrangement you did not begin.]', "declined", forbids=("trying",)),
      c('[Leave the invitation for another day.]', abort=True)),
    n("ended", "Anevia", '''"We chose something together. Then we decided we couldn't keep that arrangement. Those are both part of what happened."
{n}She looks at you directly.{/n}
"I don't want to make our evenings into proof that the three-person arrangement secretly survived. I want to ask whether you and I can keep a relationship of our own, under the terms we actually discussed."
"And Beth?"
"Has given her own answer. I'm not bringing you a kinder version of it, or asking you to finish that conversation through me. I'm asking for mine."
{n}Anevia lets the distinction rest between you before moving closer.{/n}''', c('[Hear what Anevia wants for herself.]', "own")),
    n("declined", "Anevia", '''"We didn't begin the shared life we were discussing. That doesn't make everything before it an experiment we can pretend not to have tried."
{n}She waits while you meet her gaze.{/n}
"There was secrecy. There were conversations afterward that I needed to have whether or not anybody agreed to a future. I don't intend to call those things harmless because we've found a different invitation."
"Nor do I."
"Good. Then we can ask the new question without using it to escape the old one. Beth knows I asked you here. We have spoken about what it would mean. You heard her own answer."
{n}Anevia rests her hand beside the empty chair.{/n}
"This one comes from me."''', c('[Hear her separate invitation.]', "own")),
    n("own", "Anevia", '''"I want to see you. Sometimes for a walk, sometimes to tell you something that annoyed me, sometimes because I'd like to kiss you and not have the evening end immediately afterward."
{n}She gives you a small, nervous smile.{/n}
"I want the part of my life with Beth to remain real too. We haven't stopped being married because a proposed shape for everybody's evenings didn't work. I won't give you a prettier explanation at her expense."
"What would you like to begin with?"
"An evening. A date we can keep. Something we chose because we wanted it, rather than because it seemed the least painful answer in a difficult room."
{n}She waits. The affection between you has a history. The next answer is still yours to give.{/n}''',
      c('"I want that relationship with you. Let us choose the evening."', "date"),
      c('"I care for you, but I cannot continue the romance."', "stop")),
    n("date", "Narrator", '''{n}You choose an evening and remain for part of this one. Anevia tells you about a shallow wooden box she has been making fit a badly made sill. She wants to grow a herb in it, and has already encountered several opinions about her chances.{/n}
{n}She demonstrates the crooked edge with her hands and argues when you suggest cutting it shorter. After a while she takes your hand, then asks whether you would like her to kiss you.{/n}
{n}You answer. She listens to the answer you actually give, and the evening continues at the pace the two of you choose. When you leave, the next invitation has a time attached to it. Neither of you has to pretend you met tonight to look forward to it.{/n}''',
      c('[Keep the evening you have arranged with Anevia.]', flags=("anevia.lover", "anevia.personal_ready"))),
    n("stop", "Anevia", '''"Then I am glad I asked instead of deciding what your coming here must mean."
{n}She withdraws her hand from the chair and folds it with the other in her lap.{/n}
"I am hurt. I don't want to make you fix that by giving me an answer you don't want to live with. Give me a little distance. We can find out later what being kind to each other looks like."
{n}You leave when she asks, with the scope of the goodbye clear between you.{/n}''',
      c('[End only Anevia\'s romantic relationship.]', flags=("anevia.closed", "anevia.parted"))),
], requires=("tirabade.group_closed", "tirabade.anevia_continuation_invited"),
   forbids=("anevia.personal_ready", "irabeth_dead", "irabeth_gone"), delay=0)


s("borrowed_signature", "A name used without asking", [
    n("start", "Anevia", '''{n}Anevia is waiting with a woman you have not met. The stranger has a red wool scarf wrapped twice around her neck, though the day is warm. She holds a folded paper by its edges, avoiding the ink.{/n}
"This is Ressa," Anevia says. "She repairs harnesses. Somebody has decided that makes her a useful source of names."
{n}Ressa hands you the paper. It requests the names and addresses of people renting rooms near a damaged warehouse, together with a payment for an inspection. At the bottom is a mark intended to look official.{/n}
"It isn't ours," Anevia says. "Not quite. Somebody remembered the shape and got ambitious with the rest."
{n}Ressa keeps watching your hands.{/n}
"My neighbor paid. Then they asked which of the other women lived alone. That was when I stopped believing it was about the roof."
{n}Anevia offers her a chair. Ressa refuses it, then changes her mind before anybody comments.{/n}
"I didn't come here to be the woman who accused half the street. I came because I don't know where the names go."''',
      c('"You have brought a specific concern. We can investigate it without calling everyone guilty."', "paper"),
      c('"Who delivered the paper?"', "courier"),
      c('[Postpone the interview without recording its outcome.]', abort=True)),
    n("courier", "Ressa", '''"A woman in a brown coat. She came with a little board to write on. Asked whether my landlord had mentioned the inspection. When I said no, she said landlords always forget the things tenants have to pay for."
{n}Ressa's mouth tightens.{/n}
"I laughed. I knew exactly what she meant. That made her seem more real than the paper did."
"Did she give a name?" Anevia asks.
"Cale. Perhaps. I didn't write it down."
"Then we don't build a whole person out of the part you're least sure of. What did she ask next?"
{n}Ressa describes the questions in their order. Anevia listens without completing the account for her. When Ressa contradicts herself about the day, Anevia asks what else happened that morning. The answer fixes the delivery after a broken cart had blocked the street, without requiring either of you to pretend the witness began certain.{/n}''', c('[Examine the actual paper.]', "paper")),
    n("paper", "Anevia", '''"We can send somebody through the neighborhood announcing that the inspection is false. That stops some payments. It also tells whoever arranged this that we're looking."
{n}Anevia smooths the paper on the table.{/n}
"Or we find out where the replies go first. There'll be another collection. They wouldn't have asked for addresses if they meant to disappear after the first handful of coins."
"My neighbor gave them her sister's name," Ressa says. "She thought it would help get her roof looked at."
{n}Anevia's expression changes.{/n}
"Then the warning can't wait for a clever plan to finish. We can keep the investigation quiet without keeping the people at risk ignorant."
{n}She asks Ressa whether she knows somebody who can carry a plain warning without turning it into a story about who first doubted the notice. Ressa thinks, then nods.{/n}
"Dema. She collects washing. Everybody talks to her while they're giving her things they don't want the neighbors to see."
"Would she agree to help?"
"Ask her. She objects to being volunteered."''',
      c('"We will ask. Start with the warning and keep Ressa\'s name out of it."', "warning", flags=("anevia.source_protected",)),
      c('"The warning should be official, but it need not identify who brought the paper."', "notice", flags=("anevia.public_warning",))),
    n("warning", "Anevia", '''"Good. Ressa, don't tell Dema she has to pretend she thought of it herself. Tell her what she needs to know and let her choose how to say it."
{n}Ressa looks relieved by the distinction.{/n}
"She'll ask why you haven't arrested somebody."
"So would I. We haven't found the right somebody yet."
{n}Anevia writes a short account of what is false about the notice, leaving out the witness's name. She reads it aloud, changes a phrase Ressa says her neighbors will misunderstand, and folds it without sealing it.{/n}
"If she wants to know more, she can ask me. If she doesn't want to be involved, we find another way."
{n}Ressa takes the warning. Before leaving, she asks whether she may keep a copy of the false paper. Anevia makes one herself, marking plainly that it is a copy. She gives it to Ressa with an instruction to tell anyone collecting money that she has already asked headquarters about it.{/n}''', c('[Let the witness leave with an answer she can use.]', "alone")),
    n("notice", "Anevia", '''"Then make it about the demand, not about a brave witness who'll have to live beside the people you praised her for reporting."
{n}She writes a plain warning that no such inspection fee is authorized. You read it together, removing a sentence that would make every person who paid sound foolish. Ressa objects to one other phrase.{/n}
"Don't say to bring suspicious strangers here. Somebody will decide that means the woman from the next street who doesn't greet them properly."
{n}Anevia crosses it out.{/n}
"Bring the paper. Keep the description. Don't bring a prisoner. Better?"
{n}Ressa nods. The warning is copied for the neighborhood, and somebody will know by evening that the false office has attracted real attention.{/n}
"They may stop using this notice," Anevia says after Ressa leaves. "That protects the next woman they would have asked. It may also mean they change the place where the replies are collected. We work with the choice we made."''', c('[Discuss what can still be traced.]', "alone")),
    n("alone", "Anevia", '''{n}Anevia turns the false notice over. There is a faint impression on the back, made by something written on a sheet above it.{/n}
"Tomorrow. I know a woman who sells paper without asking where every scrap came from. Sometimes that's a kindness. Sometimes it gives somebody like this a cheap supply."
{n}She looks up at you, then at the door Ressa used.{/n}
"This was meant to be the beginning of our afternoon. I should have sent word. She arrived frightened, and I thought I'd hear her first. Then I heard enough that I didn't want her going away with nothing."
"I understand."
"I know you do. I'd still like to ask whether you want to spend what's left of it with me, rather than decide that understanding means you don't mind."''',
      c('"I want the afternoon. Put the paper away until tomorrow."', "kept", flags=("anevia.case_evening_kept",)),
      c('"I need to return to my own plans. Choose another time with me now."', "rescheduled", flags=("anevia.case_evening_rescheduled",))),
    n("kept", "Narrator", '''{n}She places the notice beneath a weight, tells the nearest aide where to find her if Ressa returns, and takes your hand only when you are outside the working room.{/n}
"There. I may tell you three other things I should be doing before we reach the street. You can remind me I chose this one."
{n}You find something to eat and a place to sit. Anevia begins to describe the paper seller, catches herself, and asks you a question about your morning instead. The change takes an effort. You can see her making it.{/n}
{n}Later she kisses you goodbye, with no apology attached to the pleasure of it. The unresolved paper remains where she left it. She has not solved the case by giving herself an afternoon, or betrayed it by wanting one.{/n}''', c('[Keep the afternoon and the appointment to investigate.]', flags=("anevia.case_open",))),
    n("rescheduled", "Anevia", '''"Fair. I'd be annoyed if you'd assumed I could simply wait."
{n}She chooses another time and asks you to check it before she writes it down. When you agree, she leaves the note where she will see it before taking another appointment.{/n}
"I would have liked you to stay. That isn't an argument. Just an answer."
{n}You kiss her briefly before leaving. She holds your hand for a moment afterward, then lets you go without trying to make the departing minute compensate for the afternoon.{/n}
"Tomorrow for the paper," she says. "And the evening we just chose for us. Different promises. I'll try keeping both."''', c('[Leave with two distinct appointments.]', flags=("anevia.case_open",))),
], requires=("anevia.personal_ready", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"))


s("the_paper_seller", "What the impression leaves out", [
    n("start", "Narrator", '''{n}The paper seller occupies the front room of a house whose rear wall has been rebuilt in three different kinds of stone. Shelves hold packets sorted by size. None is quite the same color as its neighbors. A woman with ink on the side of her hand watches Anevia enter and immediately puts away a receipt.{/n}
"That looks guilty," Anevia says.
"That looks private," the woman replies. "You can ask which it is before making a habit of my doorway."
{n}Anevia smiles.{/n}
"Tovra. The Commander. We'd like to ask about paper."
"People who want paper generally buy it."
{n}You place the false notice on a clear part of the counter. Tovra looks at the printed mark, then at the edge where the sheet has been cut unevenly.{/n}
"Mine. Or it was. I sold a packet cut from those leaves. It came out of an office somebody was clearing. Half used, half not. I don't ask paper whether it has led a blameless life."
"Do you ask the person selling it?"
"When I think the answer will matter. Apparently I should have thought so."''',
      c('"We need to know who bought it, not punish you for selling scraps."', "customer"),
      c('"There is an impression on the back. May we use the window to examine it?"', "customer"),
      c('[Leave the investigation for another day.]', abort=True)),
    n("customer", "Tovra", '''"Use the window if you like. I can tell you who bought it, too. A woman called Cale. That was the name she gave. She wanted cheap sheets that would look as though they'd passed through several hands. I assumed she was sending invoices nobody intended to pay."
{n}Tovra rubs at the ink on her hand and spreads it a little farther.{/n}
"She paid. She didn't threaten me. She didn't tell me she was collecting the names of women who live alone. I would remember a thing like that."
"I believe you," Anevia says. "What did you notice that she didn't ask you to notice?"
{n}Tovra considers the question with visible irritation, then answers it.{/n}
"Wet cuffs. Not from rain. We'd had none. And blue marks on two fingers. She told me she'd been carrying a sack of dye for her sister. That may even be true. People occasionally tell the truth when they don't need to."
{n}Anevia turns the paper over.{/n}
"Let's see whether the sheet has anything to add."''', c('[Examine the reverse.]', "method")),
    n("method", "Anevia", '''{n}The impression is easier to see with the paper held sideways to the light. A curved mark crosses two faint lines. Something above them may be a letter, or a crease made by a folded corner.{/n}
"Could be an address," Anevia says. "Could be somebody's shopping. I'd like to know before we start knocking on doors."
{n}Tovra points to a drawer beneath the counter.{/n}
"I kept a few of the sheets that were written on. For wrapping. You can go through them. It will take time, and I'd like someone to mind the room while I pull the packets apart."
{n}Anevia looks to you.{/n}
"Or you can try the light. Better eyes than mine, some days. If it doesn't give us a whole answer, we can still ask the woman who moves washing through this neighborhood. Blue dye and wet cuffs may mean more to her than an imagined letter."''',
      c('[Perception DC 24] Read the shallow impression without filling in what is missing.', check=dict(Skill="SkillPerception", DC=24, Success="read", Failure="blurred", CommanderOnly=True)),
      c('[Help Tovra sort the used sheets and mind her shop while she searches.]', "sorted"),
      c('[Keep the uncertain paper and ask Dema about the practical details.]', "uncertain")),
    n("read", "Narrator", '''{n}You turn the sheet until the curve resolves into the lower loop of a written figure. The first apparent letter is a crease. Beneath it, the words "blue cistern, second bell" cross the impression of a narrow receipt line.{/n}
{n}Anevia repeats the words exactly, without adding a name to them. Tovra asks to look. She recognizes the ruled line as one used in packets sold to the dye yard near an old cistern.{/n}
"Not proof she works there," Tovra says. "People can write directions to a place they don't own."
"Useful distinction," Anevia replies. "We'll keep it."
{n}You have a meeting place and an approximate time. You do not have the identities of everyone expected there, or permission to treat everybody carrying blue dye as part of the scheme.{/n}''',
      c('[Record the actual place and time.]', "cost", flags=("anevia.trace_read", "anevia.trace_cistern"))),
    n("blurred", "Narrator", '''{n}The angle changes the mark, but does not make it reliable. You think you can see a name until a slight movement turns the first letter into the edge of a receipt line. Anevia watches your expression, then lowers the paper.{/n}
"Leave it uncertain. We can make a perfectly good mistake without giving it a convincing address."
{n}Tovra looks relieved that you have not asked her to confirm what you hoped to see.{/n}
"Dema uses the dye yard when she has cloth that needs more than washing. If somebody is carrying wet bundles around, she might know where they began."
{n}Anevia folds the notice along its existing crease.{/n}
"Then we ask. The paper didn't answer. That doesn't mean the next person has to."''',
      c('[Keep the limits of the failed reading in the record.]', "cost", flags=("anevia.trace_failed",))),
    n("sorted", "Narrator", '''{n}You spend the next hour learning how many shades of almost-white paper can occupy a small shop. Anevia minds the front room while you and Tovra separate packets. Twice she calls you to identify a size a customer has described entirely by hand gestures. The second customer buys the wrong one anyway and blames the weather.{/n}
{n}At the bottom of a tied bundle, Tovra finds a receipt for a packet delivered to the dye yard. Part of its line matches the impression on the false notice. There is no time written on it, and nothing that names Cale as the owner of the yard.{/n}
"The same stack," Tovra says. "Not necessarily the same person."
{n}Anevia writes down the distinction. The work has given you a place to begin, at the cost of an hour during which the next collection may have moved. It has also left Tovra with half her stock spread across the table.{/n}''',
      c('[Help restore the packets and keep the narrower evidence.]', "cost", flags=("anevia.trace_sorted", "anevia.trace_cistern"))),
    n("uncertain", "Anevia", '''"Then we don't need to turn every crease into a clue."
{n}She puts the paper away, careful not to make another mark on the back.{/n}
"I'd rather ask somebody who works here than invent an answer because the page looks interesting."
{n}Tovra gives you directions to Dema's collection place. She also tells you which woman at the dye yard will answer a question directly and which will insist on telling you the history of the whole street first.{/n}
"Either may know something useful," she adds. "I am merely warning you about the time."
{n}Anevia thanks her. This approach leaves the impression unread and the meeting time unknown. It gives you a willing local introduction instead.{/n}''',
      c('[Use the introduction without claiming a result from the paper.]', "cost", flags=("anevia.trace_asked",))),
    n("cost", "Tovra", '''"Are you going to put my name in the warning?"
{n}The question arrives after the practical work, when it is harder to pretend she has asked it only for somebody else's sake.{/n}
"People will hear the paper came from here. I'd rather they heard that I helped. I'd also rather they didn't break my window first and ask which order it happened in later."
{n}Anevia rests her hand on the counter.{/n}
"I can say the seller cooperated. I won't publish your address as the place to bring everybody's anger. But I can't promise nobody will recognize the paper."
"No. You can't."
{n}Tovra takes the false notice and examines the mark one more time before returning it.{/n}
"Then stop whoever is using my stock to look respectable. I have enough difficulty with ordinary customers."''',
      c('"We will describe your cooperation without making you the public face of the case."', "outside"),
      c('"If someone threatens you, report the actual threat. Do not wait for it to become impressive."', "outside")),
    n("outside", "Anevia", '''{n}Outside, Anevia takes your arm for a few steps, then lets it go when the passage narrows.{/n}
"Liked that. The part where we didn't ask her to be fearless before we believed her."
{n}She looks back at the shop.{/n}
"I can get impatient when somebody knows a thing and won't tell me. Start thinking how much easier everybody's life would be if they'd simply cooperate. Usually means I've stopped asking what it'll cost them after I leave."
"You remembered."
"This time. You can tell me if I stop. Preferably before I've made a magnificent argument for being an ass."
{n}She checks the position of the sun, then turns toward the street where Dema collects the washing.{/n}
"Come on. We have somebody to ask, and I have been warned that she objects to being volunteered. I think I may like her."''',
      c('[Go on with what the evidence actually supports.]', flags=("anevia.paper_examined",))),
], requires=("anevia.case_open", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"))


s("the_woman_with_the_basket", "What Dema chooses to carry", [
    n("start", "Narrator", '''{n}Dema's collection place is a shed with a roof that leaks at one corner. She has dealt with the leak by moving a tub beneath it and hanging an emphatic notice above the dry baskets. Nothing on the notice invites a customer to comment on the arrangement.{/n}
{n}Dema herself is an adult woman with rolled sleeves and a streak of blue beneath one thumbnail. She looks from Anevia to you, then sets down the bundle she was tying.{/n}
"Ressa said you might come. She also said I could refuse. I assume that part survived the journey."
"It did," Anevia says.
"Good. Then tell me what you want before telling me how helpful I'd be if I supplied it."
{n}Anevia describes the false notices. Dema listens, asks to see the paper and points to the mark at the bottom.{/n}
"I've seen a woman carrying those. Cale. That name at least is hers. She's been using the old counting room by the dye yard. I thought she was collecting rents. Several people have been doing that since the original owners stopped coming."''',
      c('[Describe the exact meeting place and time read from the impression.]', "time", requires=("anevia.trace_read",)),
      c('[Explain the narrower link to the dye yard, with no known meeting time.]', "place", requires=("anevia.trace_sorted",)),
      c('[Describe the wet cuffs and ask how she knows Cale.]', "work", forbids=("anevia.trace_read", "anevia.trace_sorted")),
      c('[Arrange to continue when Dema is willing.]', abort=True)),
    n("time", "Dema", '''"Second bell. That would be when she comes for the bundles."
{n}Dema points toward the yard beyond the shed.{/n}
"She puts her papers in a covered basket so they stay dry. Looks like washing unless you lift the cloth. I did once. There was a list of names underneath. She told me they belonged to people who owed her employer money."
"Did you believe her?" Anevia asks.
"Enough to put the cloth back. Not enough to forget the list."
{n}Dema looks at the paper again.{/n}
"If you know the time, you could wait without me. She might change it if she sees soldiers. She won't change it just because I have washing to carry."''', c('[Ask whether she wants any part in the plan.]', "choice")),
    n("place", "Dema", '''"The counting room, then. I know which door. I don't know when she'll be there next. She comes at different times when she thinks somebody is paying attention."
{n}Dema picks a thread off her sleeve.{/n}
"There was a bundle due today. If you've spent the morning looking through paper, she may have collected it already. That doesn't mean she won't return. It means you'll have to wait, or ask somebody who is already there."
"You?" Anevia asks.
"Perhaps. I haven't offered yet."
{n}Anevia nods, accepting the correction without making Dema repeat it.{/n}''', c('[Ask what she would be willing to do.]', "choice")),
    n("work", "Dema", '''"She pays me to carry cloth. Some of it has dye in it, some of it smells as though it ought to. She has a basket she doesn't want washed. I found papers beneath its cover once."
{n}Dema glances toward a shelf of folded sheets.{/n}
"I didn't steal them. I put the cloth back. If that disappoints you, consider how much I knew at the time."
"It doesn't," Anevia says. "What did you read?"
"Names. Not enough to make a list for you. Enough that I remembered Ressa's street when she told me what happened."
{n}Dema considers the door.{/n}
"I could carry the next bundle and see whether the basket is still there. I could also tell you to stand outside until Cale comes out. The second option would give me a quieter evening."
"Then let's discuss both," Anevia says.''', c('[Hear the choices without treating her help as owed.]', "choice")),
    n("choice", "Dema", '''"If I help, I want to know what happens when she notices. I work here. I cannot go back to headquarters and become somebody with a door guard."
{n}Anevia takes a slow breath before answering.{/n}
"You could tell us whether the basket is there and leave. No taking it, no keeping her talking. If she asks why you've come, you deliver the washing you were going to deliver anyway. We watch the door, not you pretending to be an agent."
"And afterward?"
"We don't name you in the public account. Ressa can keep the warning moving. If Cale threatens you, we act on the threat. I can't promise she won't guess somebody spoke."
{n}Dema studies her.{/n}
"That is less reassuring than the speech I expected."
"I know."
"I think I prefer it."
{n}She picks up the waiting bundle and sets it down again.{/n}
"I will tell you whether the basket is there. I won't wear a signal, and I won't go back a second time because the first answer wasn't enough. If you need more than that, choose the other plan."''',
      c('"Accept her limited help. One ordinary delivery, then she leaves."', "help", flags=("anevia.dema_helped",)),
      c('"We can watch the door ourselves. She has already given us enough."', "watch", flags=("anevia.dema_spared",))),
    n("help", "Narrator", '''{n}Dema goes about the delivery with an air of irritation that needs no rehearsal. Anevia keeps you at the corner rather than close to the counting-room door. You can see the entrance and a narrow side passage. Neither view reveals what happens inside.{/n}
{n}When Dema returns, she does not stop beside you. She passes, sets down her empty basket at the shed and waits until Anevia comes to her.{/n}
"Basket on the stool. Blue cloth over it. Cale and another woman inside. The other one said they should finish collecting before more people hear about the warning."
{n}Anevia asks whether Dema saw a weapon. She says no, then corrects herself: she saw none; that is not the same thing.{/n}
"Go on, then. That's the answer I agreed to give."
{n}Anevia thanks her once. Dema returns to the washing. She does not remain as a convenient witness for the confrontation that follows.{/n}''',
      c('[Approach with knowledge of the basket and two occupants.]', "approach", flags=("anevia.basket_located",))),
    n("watch", "Narrator", '''{n}You and Anevia wait where you can see the entrance. A woman carries a basket into the counting room, but the angle gives you no view beneath its cover. Dema does not approach the building again.{/n}
{n}The wait gives the occupants time to move things. Once Anevia points to a thin drift of smoke from a side window. Someone has lit a brazier inside. It may be for warmth or dye work. It may not.{/n}
"We know enough to question the false collection," she says. "If we wait for the room to explain itself from here, we may lose the papers."
{n}You have chosen not to place another task on Dema. That choice protects her involvement and leaves you less certain about the evidence inside.{/n}''',
      c('[Proceed with the false notice as the basis for the questions.]', "approach", flags=("anevia.basket_unconfirmed",))),
    n("approach", "Anevia", '''{n}Anevia stops before you turn into the passage.{/n}
"I want the names back. I also want to know who expected to buy them. If I start chasing the second answer while somebody burns the first, remind me what Ressa asked us for."
"What will you do?"
"Talk. Look where they don't want me looking. Try not to get clever enough to forget there's another door."
{n}She studies your face.{/n}
"You don't have to agree with every way I do this because you like me. I'd rather hear it while it might change what happens."
{n}She squeezes your hand once, quickly, before letting it go.{/n}
"And don't call me fearless afterward. Dema made a sensible request. I'm trying to be the sort of person she wasn't foolish to trust."''',
      c('[Agree on the immediate priority and prepare to act.]', flags=("anevia.dema_terms_kept",))),
], requires=("anevia.paper_examined", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"), delay=0)


s("the_counting_room", "The names and the person leaving", [
    n("start", "Narrator", '''{n}The counting-room door is unlatched. Anevia knocks anyway. A woman inside answers sharply, and you enter before she can decide whether to withdraw the invitation.{/n}
{n}Cale stands beside a desk with a cloth-covered basket at her feet. Another woman is fastening a narrow case. A small brazier smolders beneath the window. There is no obvious weapon in either woman's hand.{/n}
"We are here about the inspection notices," Anevia says.
"Then you want the office," Cale replies.
"This one will do."
{n}Anevia places the false inspection notice on the desk. Cale recognizes it before she remembers to look puzzled.{/n}
"The fee is for a private assessment. Nobody said it came from headquarters."
"Then you'll have no difficulty explaining why your mark imitates ours. Or why a roof inspection needs to know which women live alone."
{n}The woman with the case stops fastening it. Her attention shifts to the side door.{/n}''',
      c('[Keep the woman with the case in view while Anevia questions Cale.]', "account"),
      c('[Ask Cale to put the basket on the desk.]', "basket"),
      c('[Withdraw before beginning the confrontation and resume later.]', abort=True)),
    n("basket", "Anevia", '''"The covered one. You know which."
{n}Cale hesitates, then lifts it by the handle. A corner of paper shows beneath the cloth. The woman with the case looks at it once, too quickly, then returns her attention to the door.{/n}
"Customer records," Cale says.
"Good. Then your customers can have them back when we establish what they agreed to."
{n}Anevia does not reach across Cale to uncover the basket. She moves instead, putting herself where she can see both its contents and the brazier.{/n}
"Who is your colleague?"
"A buyer."
"Of roof assessments?"
{n}Nobody answers that question immediately.{/n}''', c('[Hear the account before choosing the next move.]', "account")),
    n("account", "Cale", '''"People sell information. Your friend knows that."
{n}She looks at Anevia rather than you when she says it.{/n}
"Names of people looking for work. Empty rooms. Who has a relative outside the city. There are merchants who pay for that. Not everything you don't like is a cult."
"Oh, I've sold information," Anevia says. "Never had to pretend I was repairing somebody's roof."
{n}Her smile has gone flat.{/n}
"Call it trade again. Go on. Then tell me which of those women agreed to be on your list."
{n}The buyer lifts the case from the table.{/n}
"I came to examine a list. I have made no purchase. If she obtained it improperly, that is between her and the people who supplied it."
"Put the case down," you say.
{n}She hesitates. Cale seizes the basket handle.{/n}
"You don't know what I paid for those names," Cale says. "You can't just take them."
{n}Anevia sees the movement toward the brazier as Cale swings the basket toward it. She catches its rim, but the cloth comes away in Cale's hand. Loose sheets scatter toward the heat. At the same moment the buyer steps through the side doorway.{/n}
"Papers or door," Anevia says. There is no time to discuss both.''',
      c('[Help Anevia save the names and receipts before they burn.]', "papers", flags=("anevia.saved_papers",)),
      c('[Stop the buyer while Anevia deals with Cale and the brazier.]', "buyer", flags=("anevia.stopped_buyer",))),
    n("papers", "Narrator", '''{n}You pull the falling sheets away from the brazier while Anevia pushes the basket flat against the desk, trapping Cale's hand beneath its rim until she lets go. A corner of one receipt blackens. The lists themselves stay clear of the coals.{/n}
{n}The buyer is gone through the side passage. You hear a door strike a wall somewhere beyond it, then the confused protests of a person whose way she has blocked. Anevia looks after the sound but remains beside the papers.{/n}
"Let her go. We know where these names are now."
{n}Cale begins explaining that she would never have burned them. Anevia places the scorched receipt in front of her.{/n}
"Then you should be relieved."
{n}You secure the records and keep Cale in the room until help arrives. The buyer's identity remains an open question. The women whose names fill the lists will not have to wait for that question to be solved before hearing what was taken.{/n}''', c('[Record the preserved evidence and the escaped buyer honestly.]', "limits", flags=("anevia.records_intact",))),
    n("buyer", "Narrator", '''{n}You reach the side doorway before the buyer can close it. She stops when she sees that leaving now will require more than a brisk explanation. You direct her back into the room and keep the passage behind you.{/n}
{n}Anevia has Cale against the desk, one hand held clear of the brazier. With the other she drags the basket away from the coals. Smoke rises from several loose sheets before she can reach them.{/n}
"Names survived," she says. "Some receipts didn't."
{n}The buyer sets her case down. Inside are several packets of ordinary commercial papers, a purse and two letters of introduction. None establishes a demonic conspiracy. One establishes that she has bought address lists in another district.{/n}
"Helve," Anevia reads. "Then we can stop calling you a customer."
{n}Helve asks whether she is being accused of purchasing this list. Anevia looks at the unsigned receipt, then at the papers damaged by the fire.{/n}
"You are being asked what you came to buy. We will not improve the evidence to make the answer easier."''', c('[Keep the buyer for questioning and record the damaged receipts.]', "limits", flags=("anevia.records_partial",))),
    n("limits", "Anevia", '''{n}Once the immediate danger is past, Anevia uncovers the lists one page at a time. She finds Ressa's street, then the neighbor's sister. She does not read the names aloud for everybody in the room.{/n}
"Who else has copies?"
{n}Cale looks at the door, then at the brazier, as though considering which answer might have been available a minute earlier.{/n}
"I sent a sample. Five names. No addresses."
"To whom?"
"I don't know the woman's name. She left a place to send it."
{n}Anevia asks for the address and writes it separately from the recovered list.{/n}
"We follow that too. We don't tell people we've recovered every copy when we haven't."
{n}There is anger in her voice now, less theatrical than Cale seems to expect.{/n}
"You had women asking their neighbors for private details because they thought a roof might be made safe. That's the part I keep coming back to. You used them to do the collecting for you."
"You use informants."
"They know they're telling me something. They get to ask what happens next. You took that question away."''',
      c('"The public account should state the deception and the limits of what we recovered."', "record"),
      c('"First tell the people on the list. They should not hear their own names in a public announcement."', "record")),
    n("record", "Narrator", '''{n}Cale is taken for ordinary questioning about the false collection. The recovered papers go into a sealed packet whose outside identifies the case, not its witnesses. Anevia keeps a separate list of the people who need warning, and asks for messages to be delivered privately.{/n}
{n}The counting room is quieter after the others leave. The brazier still smells of scorched paper. Anevia opens the window, then stands beside it with her hands resting on the sill.{/n}
"We made a choice fast. I want to talk about it when I've stopped hearing the paper hit the coals."
"Do you think it was wrong?"
"I think I could give you a splendid explanation either way while I'm still relieved we got anything. I'd rather find out what I think after the relief has stopped doing all the talking."
{n}She turns toward you.{/n}
"Come see me in a day or two. Not for a report. I can give you that at headquarters. I want the other conversation."''',
      c('[Agree to hear her judgment after the immediate relief.]', flags=("anevia.counting_room_settled",))),
], requires=("anevia.dema_terms_kept", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"), delay=0)


s("what_the_warning_cost", "After the names were returned", [
    n("start", "Anevia", '''{n}Anevia brings a letter to the borrowed room, then asks before putting it on the table.{/n}
"Ressa. She said I could read you the part about her. Not the list of people who came to her door."
{n}You agree. Anevia unfolds the sheet.{/n}
"She says the warning reached her neighbor before anybody came for another payment. The neighbor is angry that she believed the notice. Ressa told her the notice was made to be believed. They argued about that, then went together to tell the sister."
{n}Anevia folds the bottom of the page under her thumb, keeping the private names out of sight.{/n}
"Dema's still working. Cale knows somebody spoke, but she doesn't know who. That doesn't make Dema invisible forever. It means we haven't made her more visible for the sake of a satisfying account."
{n}She puts the letter down.{/n}
"The payments were another matter."''',
      c('[Hear what the intact receipts made possible.]', "receipts", requires=("anevia.records_intact",)),
      c('[Hear what could be established after some receipts burned.]', "burned", requires=("anevia.records_partial",)),
      c('[Leave the conversation for another evening.]', abort=True)),
    n("receipts", "Anevia", '''"Most of the receipts survived. We can match the amounts to the names and return what remained in Cale's box. Not everything she collected was still there. Some had already been spent."
{n}She taps the edge of the folded letter.{/n}
"We know who is still owed money. That's better than telling everybody to prove they paid while holding the only proof in a pile of ash."
"And the buyer?"
"We have descriptions, an address for the sample, and no convenient person who can be made to answer for every unknown. I don't like losing her. I liked knowing where Ressa's neighbor's name was when we walked out. Both are true."
{n}Anevia looks at you steadily.{/n}
"I wanted to chase. You saw it. Thank you for keeping your hands on the thing we said we came for."''', c('"Would you choose the papers again?"', "papers_answer")),
    n("papers_answer", "Anevia", '''"Yes. Ask me tomorrow when I get another useless description of the buyer and I may swear before I answer. It'll still be yes."
{n}She smiles briefly, without pretending the frustration has disappeared.{/n}
"I don't want to become the sort of woman who can't stop pursuing a secret because she has forgotten what she wanted it for. Easy habit to acquire. People praise you for it right up to the point where somebody else pays."
{n}She lifts the letter again, then folds it along the worn crease.{/n}
"Ressa did not ask us for a magnificent investigation. She asked where the names went. We answered a good part of that. I am trying to let it be a good answer while the rest remains unfinished."''', c('[Ask what remains for Dema.]', "dema")),
    n("burned", "Anevia", '''"Some amounts can be matched. Others can't. We have people who remember paying and no surviving receipt that tells us exactly how much. Cale has become remarkably uncertain about arithmetic."
{n}Her mouth tightens.{/n}
"Helve's papers gave us another district to warn. We found a woman there who had received a similar request. She hadn't answered yet. That mattered."
"And the money here?"
"What remains will be divided against the claims that can be supported. The rest will need testimony, and some people will wait longer because the receipts burned. I don't intend to call that an incidental detail."
{n}Anevia rests her hands on the table.{/n}
"Stopping Helve wasn't a foolish choice. It had a cost. I'd like us to be able to speak about the cost without either of us hearing that the other has begun an accusation."''',
      c('"I would still stop her. Warning another district mattered."', "defend"),
      c('"I would choose the papers if we faced it again."', "reconsider")),
    n("defend", "Anevia", '''"I can understand that. I think I might choose the papers. We may not get to discover which answer makes us feel better afterward."
{n}She leans back, considering the disagreement rather than trying to shorten it.{/n}
"You saw a person who could leave and do the same thing elsewhere. I saw the names starting to burn. Neither of us saw everything. That's why I wanted you there."
"Even if we disagree now?"
"Especially if you can tell me why without reminding me which of us commands the army."
{n}Her smile returns, faint and unmistakably affectionate.{/n}
"Don't make that face. You haven't. I'm allowed to appreciate the absence of a terrible argument."''', c('[Let the disagreement stand without ending the evening.]', "dema")),
    n("reconsider", "Anevia", '''"Then keep that in mind. Don't turn it into a confession you have to repeat every time we discuss the case."
{n}She reaches across the table and touches your fingers.{/n}
"I made a choice too. I could have stopped talking sooner. I could have moved the brazier before Cale reached for it. I have been making a list of all the ways the scene could have been simpler if I'd known its ending in advance."
"A long list?"
"Exceptionally competent. Everybody does exactly what I need. Very unlike people."
{n}She squeezes your hand once before withdrawing it.{/n}
"We learn something. We don't pretend learning it repairs a burned receipt. Then we go on being useful to the people who still need an answer."''', c('[Ask what remains for Dema.]', "dema")),
    n("dema", "Anevia", '''"She sent word. Wanted to know whether I'd tell the next person she helped that she was reliable. I said I wouldn't send the next person without asking her."
{n}Anevia looks amused and a little abashed.{/n}
"I had already thought of another question she might answer. Had it ready. Then I heard myself about to ask and remembered she'd agreed to one thing."
"Did you ask?"
"No. I thanked her. She said that was unusually brief of me."
{n}Anevia folds Ressa's letter carefully.{/n}
"I think she may speak with me again. I'd like that. I also like knowing she could have a life in which I never ask her to carry another dangerous basket."
{n}She puts the letter away rather than turning it into another task for the evening.{/n}
"There. That's what I wanted to tell you. Now I'd like to hear something that isn't about the case."''',
      c('"I enjoyed watching you do work you cared about. I also missed having you to myself."', "missed"),
      c('"I am glad you trusted me with the disagreement afterward."', "trusted")),
    n("missed", "Anevia", '''"Good. I was hoping you'd say the second part before I had to become unbearably charming about it."
{n}She gets up, comes around the table and offers you her hand.{/n}
"There's a whole room here that isn't occupied by that letter. We could try sitting in some of it."
{n}You follow her to the wider chair by the window. She settles close, turns toward you and kisses you before either of you can find another practical subject.{/n}
"There. I missed that too."
{n}She waits for your answer, smiling when you give it with another kiss. For a while the only unfinished business she attends to is the small distance between you.{/n}''', c('[Keep the rest of the evening for one another.]', "end")),
    n("trusted", "Anevia", '''"I was nervous about it. You can know that without congratulating me for being brave."
{n}She moves her chair around the corner of the table so she can sit nearer.{/n}
"I like you. Makes it temptin' to bring you the version of my judgment that sounds most impressive. I'd rather you knew what I was still arguing with myself about. You might have something worth saying."
"I might not."
"Then I'll enjoy the company while I ignore your advice. A sound basis for affection."
{n}She kisses your cheek, then the corner of your mouth, taking obvious pleasure in making the teasing difficult to answer.{/n}
"Come closer. I have finished being professionally interesting for the evening."''', c('[Accept the invitation.]', "end")),
    n("end", "Narrator", '''{n}The lamp burns lower while you talk. Anevia has planted the cutting in the box by the window. When you ask about it, she tells you the woman at the market supplied soil as well, having little faith in the contents of a military yard.{/n}
{n}The plant has produced one new leaf. Anevia points it out with pride disproportionate to its size, then laughs when you notice. You ask whether she intends to put that achievement in a report.{/n}
"No. This one's mine."
{n}She rests against you after saying it. The case has consequences still being worked out. Her evening has something growing on the sill and somebody she wanted to show it to. Neither makes the other less real.{/n}''',
      c('[Remember the work, its cost and the evening afterward.]', flags=("anevia.case_consequence_kept",))),
], requires=("anevia.counting_room_settled", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"), delay=48)


s("the_evening_without_a_case", "Something she did not have to solve", [
    n("start", "Anevia", '''{n}Anevia arrives at the borrowed room carrying a parcel that rattles. She places it on the table with unnecessary care, then unwraps six little wooden pieces and a folded board.{/n}
"Found a game neither of us has a professional advantage at. Unless you've been hiding a career in moving wooden goats up imaginary mountains."
{n}She lays out the pieces. One has a horn painted on the wrong side of its head.{/n}
"That one's mine. Looks like it's had to improvise."
{n}The rules are written on the back of the board. Anevia reads them aloud, objects to the rule about crossing the same bridge twice, and agrees to observe it only after you point out that the goats have no other legal argument.{/n}
"Fine. But if mine gets trapped, I'm calling it a failure of government."
{n}She sits opposite you with an expression of determined enjoyment. There is no report under the board. When footsteps pass outside, she lets them pass.{/n}''',
      c('[Play seriously. She brought a game she wants to win.]', "serious", flags=("anevia.goats_competed",)),
      c('[Try an ambitious move and invite her to explain why it will fail.]', "reckless", flags=("anevia.goats_experimented",)),
      c('[Ask to postpone the evening before beginning.]', abort=True)),
    n("serious", "Narrator", '''{n}The first game is close enough that Anevia stops talking for several turns. She watches your hand approach one piece, makes a small hopeful noise when you change your mind, and looks offended when you change it back.{/n}
"Unkind."
{n}You tell her she would have done the same.{/n}
"Yes, but I'd have looked more innocent."
{n}She finds a route you overlooked and reaches the far side with the crooked goat. Her satisfaction is immediate and thoroughly undignified. She taps the board twice, then notices the look on your face.{/n}
"You may admire my victory. I have arranged a short interval for it."
{n}The next game goes differently. You trap her at the disputed bridge and win while she is explaining why the rule should be reconsidered. Anevia studies the board, then pushes the winning piece toward you with a reluctant smile.{/n}
"All right. That was good. Annoying, but good."''', c('[Ask whether she wants a deciding game.]', "deciding")),
    n("reckless", "Narrator", '''{n}Your ambitious move leaves two goats on a ledge with no legal way down. Anevia looks at them, then at you.{/n}
"Are we rescuing them or establishing a settlement?"
{n}You defend the experiment. She hears the defense with exaggerated respect, then wins in three moves. Instead of resetting the board immediately, she asks what you hoped the move would accomplish. The explanation gives her an idea, and for the next several minutes you both forget whose turn it was.{/n}
{n}The borrowed rules become the subject of an argument about whether a goat can turn around on a bridge. Anevia insists that any real goat could, then admits she has not consulted one. You agree on a house rule and discover that it makes the game worse.{/n}
"Good," she says, crossing it out. "We have learned something at very little cost to the goats."''', c('[Restore the old rule and offer another game.]', "deciding")),
    n("deciding", "Anevia", '''"In a moment. I wanted to tell you something before I find another excuse to keep my eyes on the board."
{n}She sets the crooked goat upright beside the lamp.{/n}
"I like how I feel after you leave. Not every time. Sometimes I'm disappointed the evening's over. Sometimes I think of something I should have said differently. But mostly I find myself remembering a thing you did and wanting to tell you I liked it."
{n}Her fingers remain beside the little wooden piece.{/n}
"That surprised me. I expected the wanting-you-here part. Hadn't thought much about being pleased after you'd gone."
"What did I do?"
"Lost a game without explaining why the game didn't matter. Asked what I wanted when I got distracted. Looked at me while I was being ridiculous and didn't seem to wish I'd recover my dignity."
{n}She glances up, smiling.{/n}
"There's a list. I'm not giving you the whole thing. You'd become impossible."''',
      c('"I remember the way you look pleased before you decide what to say about it."', "seen"),
      c('"I like being someone you can disagree with and still want nearby."', "different"),
      c('"I want another kind of closeness tonight, if you do."', "desire")),
    n("seen", "Anevia", '''"Then I'll have to stop being pleased so predictably."
{n}The threat is undermined by her expression. She comes around the table, takes the chair beside you and looks at the game from your side.{/n}
"You could see that move coming the whole time."
"Yes."
"And still sat there looking fond. Disgraceful."
{n}She turns toward you, close enough that the teasing quiets without needing to stop.{/n}
"I like being seen when I haven't chosen the best angle. You make it difficult to pretend I was merely being charming on purpose."
{n}Her hand rests against your cheek for a moment. The touch is warm and unhurried.{/n}''', c('[Ask what closeness she would like tonight.]', "desire")),
    n("different", "Anevia", '''"You'd be disappointed if you wanted somebody who agreed with you all the time. I'd get bored trying."
{n}She comes around the table and sits beside you.{/n}
"I have caught myself saving arguments because I thought you'd enjoy them. That's either affection or a very elaborate way of making trouble."
"Does it have to be one?"
"No. That's one of the things I like about you."
{n}She leans against you, taking a moment to find a comfortable place for her shoulder.{/n}
"I don't want us to become so considerate that we never surprise each other. Tell me when you want something I haven't guessed. I'll try doing the same before I've prepared an explanation that makes it sound sensible."''', c('"Then tell me what you want now."', "desire")),
    n("desire", "Anevia", '''{n}Anevia pushes back her chair and reaches for you. You draw close beside the table. Her hand settles at the back of your neck while she speaks.{/n}
"I would like you to stay. I made the room ready because I hoped you'd want to. That isn't a debt you acquired by coming through the door."
{n}She smiles, the confidence in it warmed by a visible trace of nerves.{/n}
"I can put the goats away either way. They've had a demanding evening."
{n}You kiss her. She answers readily, drawing closer until the chair becomes a poor arrangement for the distance both of you want. When you pause, she rests her forehead near yours.{/n}
"Tell me what you'd like."''',
      c('[Stay the night with her, letting the evening become private.]', "night"),
      c('[Stay close for a while, then keep your promise to return elsewhere.]', "leave"),
      c('[Ask for a quiet night of sleep and company.]', "sleep")),
    n("night", "Narrator", '''{n}She puts the little pieces into their parcel without caring which way they face. The crooked goat remains beside the lamp until she notices it watching, laughs and turns it toward the wall.{/n}
{n}Then her attention is wholly yours. She kisses you at the edge of the bed, lingering when your hand finds her waist. There is a buckle she cannot undo while you keep making her laugh. She catches your wrist, presses a kiss to your knuckles and asks you to be helpful for once.{/n}
{n}You are helpful. The buckle gives, and the belt, and she steps out of the rest herself, quick and unembarrassed, like a woman shedding a disguise she has worn too long. "Your turn," she says, and does not wait for you to manage it; she has your shirt over your head before you can make a joke of it.{/n}
"There," she murmurs against your mouth. "That's what I'd like."
{n}She pulls you down onto the bed after her by a fistful of whatever you are still wearing, laughing once, low, and then not laughing at all. Her knee draws up along your hip; her hand spreads flat between your shoulders and holds you there, exactly where she wants you.{/n}
{n}In the morning Anevia wakes with one arm across you and a complaint about the window already forming. She abandons it when you turn toward her. For a while neither of you gets up to discover whether the complaint was justified.{/n}''',
      c('[Keep the morning as part of the invitation.]', "morning", flags=("anevia.private_night",))),
    n("sleep", "Anevia", '''"I would like that. I am very good at being quiet once somebody has persuaded me to stop talking."
{n}She puts the game away, finds another blanket and asks which side of the bed you prefer. The practical questions make her smile; she had apparently imagined needing a much more impressive answer.{/n}
{n}You settle together while the room cools. Anevia tells you one last thing she meant to say, then another, then apologizes into your shoulder for her inaccurate description of her own talents. You laugh, and she finally grows quiet.{/n}
{n}In the morning she wakes before you and lies still long enough to enjoy having no immediate obligation to rise. When you open your eyes, she is watching the light rather than the door.{/n}
"I could become accustomed to this. Not every morning. Enough to miss it when we don't."''',
      c('[Enjoy the unhurried beginning of the day.]', "morning", flags=("anevia.quiet_night",))),
    n("leave", "Anevia", '''"Then keep it. I liked knowing you would come when you said you would. Somebody else is allowed to like that too."
{n}She kisses you once more, without making the goodbye brief in order to prove she accepts it. At the door she straightens a fold in your clothing, notices what she is doing and smiles at herself.{/n}
"Apparently I've learned a habit. Don't make a report of it."
{n}You choose another evening before leaving. Anevia puts the game away afterward and keeps the crooked goat beside the lamp. She taps it on the head before blowing out the lamp.{/n}''',
      c('[Keep both the goodbye and the next invitation.]', flags=("anevia.ordinary_life_kept",))),
    n("morning", "Anevia", '''"We should eat something before I start finding reasons not to leave."
{n}She gets up reluctantly, returns to kiss you and then gets up again with more determination. There is bread, a little cheese and fruit that has survived your earlier appetite. She distributes it without turning breakfast into a new test of domestic competence.{/n}
"I have work. You have work. I also have an evening at home I intend to keep."
{n}She takes your hand across the table.{/n}
"And I want another one here. Those can all be true without any of them sounding like an apology."
{n}You agree on the next visit. She leaves pleased, with the folded game under her arm and the little crooked goat still beside your lamp.{/n}''',
      c('[Choose another evening without claiming all her time.]', flags=("anevia.ordinary_life_kept",))),
], requires=("anevia.case_consequence_kept", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"), delay=48)


s("departure_note", "The part of the page she left blank", [
    n("start", "Anevia", '''{n}Anevia has folded a sheet of paper small enough to fit inside an ordinary pouch. She gives it to you without ceremony, then looks annoyed when the fold opens before you can put it away.{/n}
"Was meant to look more composed than that."
{n}The page contains a few lines in her hand. Nothing useful about the road, no warning disguised as a farewell. She has written that she enjoyed the last evening she spent with you, and named one small thing that made her laugh.{/n}
"Left the bottom empty," she says. "In case you think of something you'd have told me if I was there. You don't have to make it worth the paper."
{n}Her fingers remain on the edge for a moment before she lets go.{/n}
"I'd like an answer when you can give one. I know that may not be soon. Don't turn a lack of news into a promise you can't keep just because you know I'll want it."''',
      c('"What will you do while I am gone?"', "days"),
      c('"I am afraid of what the silence will do to us."', "fear"),
      c('[Leave the farewell for a day when you can finish it.]', abort=True)),
    n("days", "Anevia", '''"Work. Complain about work. Find somebody who'll let me ruin a batch of bread without charging for the damage."
{n}She smiles, then grows more serious.{/n}
"Have evenings at home. Think of something you would have said and be irritated that I can't ask whether I'm right. Go somewhere you haven't been with me. I'd like to have things to tell you that aren't all about waiting."
"I would like to hear them."
"Good. Then remember that's part of what you're coming back to, if you can. People who kept living. Not a room carefully preserved so you won't have to learn anything new."
{n}She touches your cheek.{/n}
"You can change too. I may complain about the inconvenience. I'll still want to know you."''', c('[Tell her something you will want to ask when you return.]', "end")),
    n("fear", "Anevia", '''"So am I. I'd rather know we both said it than spend the time imagining I was the only one who minded."
{n}She looks at the folded page in your hand.{/n}
"I can't promise to be brave in an attractive way. I might be cross with somebody who has done nothing except ask a question at the wrong moment. I'll apologize afterward. Probably after being cross about having to apologize."
"That sounds like you."
"Let's hope I don't become too impressive while you're away. You'd hardly recognize me."
{n}Her humor breaks for a moment. She takes a breath and lets you see the effort.{/n}
"Keep the paper. Not as something you owe me. As a thing I chose to give you when I knew I couldn't go along."''', c('[Keep her gift and stay close.]', "end")),
    n("end", "Narrator", '''{n}She embraces you without pretending it will be enough. You remain together until one of you needs to move, then kiss once more at the door. Anevia does not fill the last silence with instructions.{/n}
"Come back if you can," she says. "I would like to argue about something ordinary with you again."
{n}You put the page where you will be able to find it. It is light enough to forget you are carrying it, until you remember why it is there.{/n}''',
      c('[Keep her page and say goodbye.]', flags=("anevia.departed_together",))),
], requires=("anevia.lover", "anevia.personal_ready"), forbids=("irabeth_dead", "irabeth_gone"), chapters=(3,), delay=0)


s("the_blank_half", "A page with room for an answer", [
    n("start", "Narrator", '''{n}Among your belongings you find the page Anevia gave you before you left. The creases have softened. Her account of one small, pleasant thing occupies less of the sheet than the blank space beneath it.{/n}
{n}There is no reliable way to send an ordinary letter from here to Drezen. For a while you read what she wrote without adding anything.{/n}
{n}The memory that returns is not heroic. It is the way she watched you decide whether a joke was meant kindly, then laughed when you answered it. It is her hand on the table after she had finished speaking. You smooth the crease with your thumb and begin looking for something to write with.{/n}''',
      c('[Write about a moment you wanted to share with her.]', "moment"),
      c('[Write about what you fear may have changed.]', "changed"),
      c('[Keep the answer in memory rather than on a page.]', "memory"),
      c('[Put the page away for another quiet rest.]', abort=True)),
    n("moment", "Narrator", '''{n}You begin with a detail you would have told her while it was still fresh: something absurd, something unexpectedly beautiful, something that angered you before you knew how to explain why. The first version sounds like a report. You cross out the unnecessary explanation and begin again.{/n}
{n}You tell her what you wanted her to notice. Then you admit you also wanted to watch her noticing it. You can imagine her reading that line twice and finding something unbearable to say about it.{/n}
{n}The page fills slowly. You do not turn the ending into an assurance that you will certainly return. Instead you ask about something ordinary in her life, something whose answer will belong to days you did not see.{/n}
{n}You leave a little room beside the question, though she will not be here to answer it tonight.{/n}''',
      c('[Keep the written answer for a possible return.]', flags=("anevia.absence_account", "anevia.absence_shared_moment"))),
    n("changed", "Narrator", '''{n}You write that you are afraid she will have grown accustomed to your absence. Then you read the sentence and discover the unfair wish beneath it: that missing you should have prevented her from growing accustomed to anything.{/n}
{n}You do not erase the fear. You write the second thought beneath it. If you return, you will want a place in the life she has actually lived, not proof that she left all of it waiting for you.{/n}
{n}That is easier to write than to feel. You tell her so. The admission makes the page less dignified and more like a conversation she might recognize.{/n}
{n}You finish by asking what she has wanted that you do not yet know about. The question feels less secure than a promise, and more useful.{/n}''',
      c('[Keep the fear and its more honest answer together.]', flags=("anevia.absence_account", "anevia.absence_changed"))),
    n("memory", "Narrator", '''{n}You fold the page without writing. There are things you want to tell her that will not settle into a useful order tonight. You try the opening aloud, dislike it, and stop.{/n}
{n}You think of her making an ordinary plan in Drezen. Not waiting at a window, not saying something brave for an audience you have invented. Perhaps she is losing a game, or arguing about a wet cloak, or burning something she had intended to eat.{/n}
{n}You would like to hear which of those guesses is wrong. You would like to tell her what it was like to make them here.{/n}
{n}You tuck the page back into its fold. It can wait until you have something worth telling her.{/n}''',
      c('[Keep the page. Tell her in person if you return.]', flags=("anevia.absence_account", "anevia.absence_unwritten"))),
], requires=("anevia.departed_together", "anevia.lover"), chapters=(4,), remote=True, delay=0)


s("the_life_she_lived", "The answer you could not guess", [
    n("start", "Anevia", '''{n}Anevia has moved the little plant to a larger pot. The wooden box now holds pieces of paper, a needle case and a key she tells you opens nothing she currently owns.{/n}
"Kept it because I liked the shape. Apparently that's allowed. I checked."
{n}She clears a place beside it for your things, then sits near enough that you can reach her hand without making a ceremony of it.{/n}
"I've been thinking about the way we tell each other what's happened. I can give you a very good account and leave out every part that mattered to me. You may have noticed the technique."
{n}Her smile invites recognition rather than reassurance.{/n}
"I'd like a different conversation tonight."''',
      c('"There are days we missed. I want to hear about yours."', "absence", requires=("anevia.departed_together",)),
      c('"Tell me about a day I have not heard about. I want to know more than the evenings we spend together."', "new_days", forbids=("anevia.departed_together",)),
      c('[Ask to keep this conversation for another day.]', abort=True)),
    n("absence", "Anevia", '''"Some were awful. Some were ordinary. I don't want to turn the ordinary ones into evidence that I wasn't missing you."
{n}She draws her feet beneath the chair.{/n}
"I went to the market with Beth. Had an argument about whether we needed another blanket. Bought it, then discovered she'd already ordered one. We were very well supplied for an evening spent being annoyed with each other."
{n}The memory makes her smile before the sadness returns.{/n}
"Another day I nearly told a runner to come back when she had something worth hearing. She had brought exactly what I'd asked for. I was angry because it wasn't news of you. Had to go find her afterward and explain whose fault that was."
"Yours?"
"Mine. Didn't make the wanting less real. Did make it something I had to stop throwing at people."
{n}She reaches for your hand.{/n}
"What did you keep for me? If you kept anything. You don't owe me a page for every day."''',
      c('[Give her the written account of a moment you wanted to share.]', "moment", requires=("anevia.absence_shared_moment",)),
      c('[Give her the page about fearing what might change.]', "changed", requires=("anevia.absence_changed",)),
      c('[Tell her the account you kept without writing.]', "unwritten", requires=("anevia.absence_unwritten",)),
      c('"I kept your page. I have no finished answer, but I would like to begin one here."', "unwritten", forbids=("anevia.absence_account",))),
    n("moment", "Anevia", '''{n}Anevia reads without speaking. At one point her thumb stops against the edge of the page, and she goes back over a sentence before continuing.{/n}
"I'd have liked being there for that."
{n}She looks up.{/n}
"I'd have liked seeing what you looked like while it happened. That's the bit a letter can't supply. You would have turned toward me, and I'd have known you wanted me to notice."
{n}She folds the page carefully, leaving your addition inside.{/n}
"Thank you for keeping the moment. Tell me the part you crossed out. I can see you've argued with it. I'd like to hear the argument too."
{n}You explain the sentence you removed. Anevia listens, disagrees with your first explanation and asks a better question. Soon the letter has become what you wanted it to be when you wrote it: something the other person can answer.{/n}''', c('[Let the remembered moment become a conversation.]', "her_days")),
    n("changed", "Anevia", '''"I did get accustomed to some of it."
{n}She gives you the difficult answer while her hand remains on yours.{/n}
"Not having you there. Having to decide what to do with an evening instead of thinking that wanting you was a plan. I didn't stop wanting you. I stopped expecting that to tell me how to spend every hour."
{n}She reads the second thought again, the one you wrote beneath the fear.{/n}
"I'm glad you left this in. The unfair part and the part that knew it was unfair. I have thoughts like that too. Usually I try them out on a wall before inflicting them on anybody."
"A patient wall?"
"Exceptionally. Terrible advice, though."
{n}She kisses your fingers before setting the page down.{/n}
"Ask about the person who's here. I think you'll still like her. She may have acquired an opinion you haven't prepared for."''', c('[Ask what she wants you to know about her days.]', "her_days")),
    n("unwritten", "Narrator", '''{n}You begin with a small detail. Anevia asks where you were standing, then what happened immediately before the part you chose to tell. The questions change the account. Something you had meant as an aside becomes the reason you remembered the day.{/n}
{n}She listens without insisting that every silence must be filled. When you lose the order of events, she waits while you find it. At the end she tells you which detail she will remember, and it is not the one you expected.{/n}
"There. Didn't need to be a letter. I like being able to ask questions while you're still here to look offended by them."
{n}You ask whether she has anything you should be prepared to hear. She considers the invitation rather than answering with a joke.{/n}''', c('[Give her the same room to answer.]', "her_days")),
    n("new_days", "Anevia", '''"A whole day? Dangerous. You might find out how much of it I spend looking for something I put down a minute earlier."
{n}She smiles, then grows thoughtful.{/n}
"There are things I keep meaning to tell you about. Small things. Places I went, arguments I had, a woman who taught me something while pretending she was merely complaining."
"You can tell me."
"I know. I'm learning that knowing doesn't always make me remember to do it. I can spend a whole evening with you and talk about nothing except the part of my life you already saw."
{n}She leans nearer.{/n}
"So ask. Not as an investigation. As somebody who would like to know what I do when I haven't arranged the room for company."''', c('[Ask about an ordinary day she has not described.]', "her_days")),
    n("her_days", "Anevia", '''"I went back to the woman with the cuttings. Asked whether I could help with the boxes on her sill. She said I could begin by carrying them without explaining how I'd carry a person through a dangerous passage."
{n}She looks at you, amused.{/n}
"Apparently I had been making the plants sound like an assignment."
"Did you stay?"
"Yes. Got dirt under my nails. Learned which roots shouldn't be pulled apart. She asked whether I wanted another cutting when it was ready. I said yes before thinking of a reason I'd be too busy."
{n}Anevia rests her hand on the wooden box.{/n}
"I'd like more of that. Having somewhere to go because I want to be there, and somebody expecting me who doesn't need information. I don't mean instead of you. I mean a life I have something to bring you from."
{n}She waits, giving you the answer without making it smaller.{/n}''',
      c('"I would like to hear about it. You do not have to invite me into every part."', "end"),
      c('"I may be disappointed when you choose an afternoon elsewhere. I still want you to have it."', "end")),
    n("end", "Anevia", '''"Then I'll tell you when I'm going. You can tell me you miss me without making it sound like a complaint I have to solve."
{n}She moves close enough to kiss you, then rests against you while the light changes at the window. Outside, someone drops a bucket. She laughs at the succession of increasingly elaborate curses.{/n}
"What are you going to do tomorrow," she says, "that I haven't already guessed?"
{n}You answer. She looks pleased by the part that surprises her.{/n}''',
      c('[Keep making room for the people you are now.]', flags=("anevia.return_ready",))),
], requires=("anevia.ordinary_life_kept", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"), chapters=(5,))


s("a_key_that_is_hers", "What she wants to keep", [
    n("start", "Anevia", '''{n}Anevia brings you a key attached to a short length of green cord. She keeps it in her own hand while explaining it.{/n}
"The woman who rents me the room offered a longer arrangement. Not a promise that the building will survive every catastrophe. Just that she won't give it to somebody else whenever I'm away for a week."
{n}She turns the key once between her fingers.{/n}
"I'd like to keep it. A place where I can leave the box on the sill and find it where I put it. Somewhere you could come because we agreed to meet, not because I found an empty room before anybody else did."
"And your home?"
"Still my home. Beth and I have talked about it. This isn't me packing quietly and hoping nobody asks what the key means."
{n}She sits beside you, her expression open and nervous.{/n}
"I want a life with you in it. I don't need that to become the only life either of us has. I do need to know whether you want to keep choosing it after the next convenient evening."''',
      c('"Yes. I want a lasting relationship with you, with room for the lives we both have."', "yes"),
      c('"I love the time we have. I cannot promise that future."', "open"),
      c('"I need to end the romance. You deserve an answer I mean."', "part"),
      c('[Ask for time before giving a final answer.]', abort=True)),
    n("yes", "Anevia", '''{n}Anevia closes her hand around the key, then puts it on the table so she can take yours.{/n}
"Good. I had several very dignified replies ready in case you made that harder to hear."
{n}She kisses you before you can ask to hear them. When she draws back, she is smiling with a relief she does not try to hide.{/n}
"You may have a key if you want one. After we decide what using it means. I don't want us discovering that in a doorway while somebody's tired."
"What would you like?"
"Ask before arriving if we haven't made a plan. Come in if we have. Leave a note if something changes. Don't treat finding me alone as proof I had no reason to want an afternoon alone."
{n}Her thumb moves over your knuckles.{/n}
"And tell me where I stand with you. I don't mean an announcement to the city. I mean not having to infer it from which invitation you remembered."''',
      c('"I want the key, and I can keep those terms."', "key", flags=("anevia.shared_key",)),
      c('"Keep the only key for now. I would like to keep asking and being invited."', "invited", flags=("anevia.kept_invitations",))),
    n("key", "Anevia", '''"Then I'll have another made. This one remains mine."
{n}She loops the cord around her finger, pleased by the small distinction.{/n}
"I like knowing I can give you a way in without giving up the idea that the room belongs to me. Sounds obvious when I say it. Didn't always feel obvious."
{n}You discuss where you will leave a message and which neighbor will accept a note without reading it. Anevia objects when you propose paying for every repair, and you agree to ask before turning a leaking shutter into a gift she must appreciate.{/n}
"You can hold the ladder," she says. "I have great confidence in your ability to stand still while I complain."
{n}She points out where the ladder slipped last time. The mark is still visible on the plaster.{/n}''', c('[Ask what she hopes will happen in the room.]', "room")),
    n("invited", "Anevia", '''"I can like that too. We don't have to choose the most impressive version of trusting each other."
{n}She lays the key beside the lamp.{/n}
"I enjoy asking you. I enjoy knowing you came because you wanted to, not because the room had become one of the places you check on your way past."
"You may still ask for a different arrangement later."
"So may you. Preferably before one of us has composed a very convincing complaint about something the other never agreed to."
{n}She smiles and leans against you.{/n}
"There. A lasting relationship with some questions still in it. I find that more believable than the version where we become infallible after a pleasant speech."''', c('[Ask what she hopes will happen in the room.]', "room")),
    n("room", "Anevia", '''"Breakfast. Though if I try cooking it here, that window'll have to open all the way."
{n}She studies the cramped hearth, then shakes her head.{/n}
"Still want my proper oven. Stone, big enough for a loaf I haven't had to bully into the pan. Beth says I should learn to make the loaf before choosing the oven. Typical paladin. Very concerned with doing things in order."
"Would it fit here?"
"No. And I won't put it here. That's for home. For the morning she comes downstairs because she can smell what I've made."
{n}Anevia turns the key on its cord.{/n}
"There was a kitchen in the temple where I grew up. Desna's people, singing while they worked. I could smell breakfast before I was properly awake. Sometimes that's what I remember when somebody asks why I keep doing this miserable bloody job. A morning where the noise outside the door is somebody being happy."
{n}She gives the key a little swing and catches it.{/n}
"Doesn't have to be a temple. Doesn't even need a competent baker, at first. Just has to be somewhere a person can stop listening for whoever's coming to drag her out."
"You want that with Irabeth."
"Yes. And I want you coming to breakfast because I asked you. Beth grumbling that I've fed you the burnt bit. You defending it badly. Several people I love, all wrong about my bread."
{n}She laughs, then lays the key down.{/n}
"This room's smaller. I can start with an evening. Though I'd like several very good nights too. Don't let the breakfast plan give you a false impression."
{n}Her smile is warm and deliberately wicked. She catches the front of your clothing lightly and draws you closer, giving you time to answer the invitation.{/n}
"We could begin investigating the second possibility."''',
      c('[Kiss her and stay for the evening she has chosen.]', "end"),
      c('[Hold her close and enjoy the future taking an ordinary shape.]', "end"),
      c('"I would like to help with the bread. Tell me which part you want company for."', "bread"),
      c('"I would rather share the table than pretend I know how to bake."', "table")),
    n("bread", "Anevia", '''"Measuring. Apparently guessing is a privilege you earn after you know what you're doing."
{n}She draws a rough circle in a patch of dust on the table, then divides it badly.{/n}
"One loaf. No buying me a bakery while I'm asleep. If I burn it, you'll have to be there for the second attempt."
"What if I burn it?"
"Then we'll have discovered a useful division of blame."
{n}She wipes away the drawing before the cup can spread it across her sleeve.{/n}
"All right. I'll ask the cook when the oven's free. And I'll do the asking. She's entitled to say no without finding the Commander in her kitchen looking hopeful."''',
      c('[Agree to a first attempt when she has arranged it.]', "end", flags=("anevia.bread_company",))),
    n("table", "Anevia", '''"Good. An honest appetite. I know what to do with one of those."
{n}She takes your hand and draws you back toward her.{/n}
"You can tell me if it's awful. I'd rather hear it from you than watch Beth construct an elaborate lie about the crust."
"Would she?"
"She'd try. Wouldn't get far. Her ears give her away."
{n}Anevia smiles at the thought, then kisses you.{/n}
"Come hungry. Whatever else goes wrong, we ought to manage that."''',
      c('[Look forward to the meal she wants to offer.]', "end", flags=("anevia.bread_guest",))),
    n("end", "Narrator", '''{n}You remain together while the room darkens. The key lies where she put it. When Anevia reaches for it, the cord catches beneath a cup. She rescues both with a muttered complaint.{/n}
{n}Anevia tells you another thing she wants, and you tell her one she had not guessed. She objects to the first day you suggest, naming an errand she has already promised Beth. You find another and write it on the scrap beside the lamp.{/n}''',
      c('[Choose a lasting relationship with Anevia.]', flags=("anevia.committed", "anevia.future_chosen"))),
    n("open", "Anevia", '''{n}Anevia listens, then puts the key in her pocket.{/n}
"I would have liked the other answer. I can still hear this one."
{n}She asks what you can offer without dressing it up as permanence. You tell her. She thinks about it long enough that you stop preparing a reply and wait.{/n}
"I want to keep seeing you. I won't make plans that depend on a promise you haven't given. If that stops being enough, I'll tell you instead of hoping you'll notice that every invitation has become an argument."
"I can agree to that."
"Then agree because you want it. Not because I've made it easy to avoid hurting me. It does hurt a little. I am choosing it anyway."
{n}She takes your hand. The affection is real, and the future remains unpromised.{/n}''',
      c('[Continue openly without claiming a settled lifelong commitment.]', flags=("anevia.open_future", "anevia.future_chosen"))),
    n("part", "Anevia", '''{n}She closes her hand around the key and keeps it there.{/n}
"All right. Then we don't have to argue about whether the answer was clear enough."
{n}The attempt at humor fails. She does not repeat it.{/n}
"I'd like some distance. I don't mean you must disappear from headquarters. I mean I don't want to have an easy little conversation tomorrow so you can know I'm taking it well."
"I understand."
"You might not. Give me the distance anyway."
{n}You leave her with the key and the room she wanted to keep. She is still holding the key when you look back from the doorway.{/n}''',
      c('[End Anevia\'s romance without closing Irabeth\'s or changing their marriage.]', flags=("anevia.closed", "anevia.parted"))),
], requires=("anevia.return_ready", "anevia.case_consequence_kept", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"), chapters=(5,), delay=48)


s("the_last_ordinary_thing", "Before the next road", [
    n("start", "Anevia", '''{n}Anevia has repaired the loose fastening on the borrowed window. She demonstrates the improvement twice, then opens it again to let the evening air into the room.{/n}
"There. I can close it when I want. Having the choice seems to have made me less interested in using it."
{n}She turns toward you with a smile that does not quite conceal the reason she asked you here.{/n}
"You'll be leaving again. For whatever comes next. I have been trying to decide which sensible thing I could give you that wouldn't look like I thought you were incapable of packing."
{n}On the table lies the crooked wooden goat from the game. Anevia picks it up.{/n}
"Settled on something entirely useless. Difficult to misunderstand the intention."''',
      c('[Take the little goat and ask what she would like you to remember.]', "remember"),
      c('"Keep it here. I would like a reason to come back and finish the game."', "here"),
      c('[Leave this farewell for another evening.]', abort=True)),
    n("remember", "Anevia", '''"That I won the first game. Important historical fact."
{n}She places it in your hand and closes your fingers around it.{/n}
"Also that I wanted to see you when there was nothing useful to ask. That we could disagree and still have a good evening. That you don't have to become a better story before you're allowed to miss somebody."
{n}She looks at your closed hand.{/n}
"It's small. Should fit somewhere without making you choose between affection and another bandage. I have no desire to win that argument."
{n}You put it away. Anevia watches until it is safe, then comes closer.{/n}''', c('[Hold her close.]', "future")),
    n("here", "Anevia", '''"Then it stays by the lamp. No moving it to make the room look more respectable while you're away."
{n}She sets it down facing the board, as though giving it something to consider.{/n}
"I may practice. You should know that before you promise to return victorious."
"You would practice against yourself?"
"An irritating opponent. Knows all my tricks."
{n}The joke leaves her smiling and visibly close to tears. She lets you see both, then steps nearer instead of finding another object to arrange.{/n}''', c('[Make room for the feeling she has not hidden.]', "future")),
    n("future", "Anevia", '''"I don't want to spend this evening saying everything as though I'll never get another chance. Makes ordinary words sound like somebody else's speech."
{n}She takes your hand.{/n}
"I love you. That's an ordinary thing I would like to say more than once. I'd like to say it while I'm annoyed with you, and when you've arrived earlier than I expected, and when nothing at all has happened worth explaining."
{n}You answer her. Her thumb stops moving over your hand. When you have finished, she smiles.{/n}
"Good. We can begin with this evening."
{n}You stay together while the room darkens. There are kisses, a complaint about the cooling tea and a disagreement about where the game ought to be kept. Anevia insists that the disagreement counts as keeping her promise to speak ordinarily. You tell her she is making suspiciously good progress.{/n}
{n}When it is time to leave, she comes to the door with you. She does not ask the road to guarantee what it cannot.{/n}
"Come back if you can. I'll have things to tell you."''',
      c('[Keep the farewell and the life that gives it meaning.]', flags=("anevia.developed",))),
], requires=("anevia.future_chosen", "anevia.case_consequence_kept", "anevia.ordinary_life_kept", "anevia.lover"),
   forbids=("irabeth_dead", "irabeth_gone"), chapters=(5,), delay=24)


s("a_grief_with_a_name", "The person she is missing", [
    n("start", "Anevia", '''{n}Anevia is holding a folded cloth she has not decided where to put. She sets it on the table when you approach, then picks it up again before speaking.{/n}
"Beth's. Not important. I keep finding things that aren't important and discovering I can't decide what to do with them."
{n}She looks at you, tired and fully aware of the care with which you have entered the room.{/n}
"You can say her name. I'd rather hear it than watch everybody working around the empty space."
{n}You say Irabeth's name. Anevia closes her eyes for a moment, then sits.{/n}
"Thank you."
{n}There is no useful question waiting behind the word. She has not asked you here to arrange what her grief ought to become.{/n}''',
      c('[Sit with her and let her choose what to say.]', "cloth"),
      c('"Would you rather be alone? I can come another day."', "company"),
      c('[Leave the conversation unfinished for now.]', abort=True)),
    n("company", "Anevia", '''"Not tonight. I might ask you to go later. I'd like to know I can do that without having to comfort you about it."
"You can."
{n}She nods and moves a chair closer with her foot.{/n}
"Then sit. You don't have to find a thing to fix. I know you're good at it. I am not presently a suitable occupation."
{n}The familiar dryness almost becomes a smile. She turns her face aside and rubs at one eye.{/n}''', c('[Sit beside her.]', "cloth")),
    n("cloth", "Anevia", '''"She used to fold these differently. I told her it didn't matter which edge went on the outside. She said it mattered to her. We had an entire argument about whether that was an answer."
{n}Anevia turns the cloth in her hands.{/n}
"It was, of course. A very irritating answer. I miss having it available to argue with."
{n}For a while she says nothing. You remain beside her. Someone passes the door without stopping.{/n}
"People tell me she knew I loved her. I know she did. I still think of things I wanted to say. Knowing a person was loved doesn't finish every conversation you were going to have."
"No."
"I'd like to keep some of them. Even the stupid ones. Especially those, some days. Everybody remembers the brave woman with the sword. I remember her trying not to laugh while I explained why the soup was an insult."
{n}She folds the cloth her wife's way and leaves it in her lap.{/n}''',
      c('"Tell me something about her that you want somebody else to remember."', "memory"),
      c('"We can keep the silence too. You do not have to turn this into a story for me."', "silence")),
    n("memory", "Anevia", '''"She once tried to mend a chair because I said it leaned. Refused to admit she'd never done it before. Came back with a chair that leaned in the opposite direction and a splinter she wouldn't let me remove until she'd explained the improvement."
{n}Anevia laughs, abruptly, and the laugh becomes a sob before she can decide which sound she intended. She puts a hand over her mouth, then lowers it when you remain where you are.{/n}
"Both happened. That's allowed. I know it's allowed. I keep explaining it to myself as if I'd disagree."
{n}You ask what became of the chair.{/n}
"We kept it. Put a folded scrap beneath one leg. She said she was going to fix it properly. I said I was becoming fond of its opinions."
{n}The memory leaves her quiet again. Then she looks toward the cold hearth.{/n}
"I had this picture of her coming into the kitchen. I'd have bread ready. She'd burn her fingers because she wouldn't wait, and pretend she hadn't."
{n}Anevia presses the heel of her hand against one eye.{/n}
"Can't bear people tellin' me I can still learn to bake. I know I can. That's not what I lost."
{n}You wait. She takes her hand away and looks at you.{/n}
"Don't put yourself in that doorway to make the picture come right. Sit here. I asked you here."''', c('[Let the memory remain hers.]', "us")),
    n("silence", "Narrator", '''{n}She leans back and lets the cloth lie still. There are sounds from the corridor, ordinary work continuing without permission from the room. Once Anevia seems about to complain about a raised voice outside, then shakes her head and remains quiet.{/n}
{n}After a while she places her hand beside yours. You ask before taking it. She nods, and her fingers close around yours.{/n}
{n}Eventually she turns toward you. Her expression has not become less sad. It has become less occupied with being watched.{/n}''', c('[Stay while she finds the words she wants.]', "us")),
    n("us", "Anevia", '''"I still care for you. I don't know what evenings with me will be like for a while."
{n}She says it carefully, without offering either statement as a consolation for the other.{/n}
"I may want you near and then discover I can't bear anybody touching me. I may enjoy an afternoon and feel guilty before I've got home. I don't want to pretend those things mean nothing. I also don't want every one of them to decide the rest of my life."
"What would help?"
"Ask what I want that day. Believe me if I know. Don't act as though the place beside me has become easier to obtain because she's gone. It hasn't. It's a different place, in a life I didn't choose to have changed this way."
{n}Her hand remains near yours.{/n}
"You were already someone I wanted. I'd like not to lose that by making you her substitute."''',
      c('"I want to remain part of your life without taking her place. We can decide each visit honestly."', "remain"),
      c('"I care for you, but I cannot continue a romantic relationship. I will not make that your fault."', "part")),
    n("remain", "Anevia", '''"Then come again. Ask first. I will try to answer instead of deciding that whatever hurts least for you must be what I want."
{n}She puts the cloth beside the chair, within reach but no longer held so tightly.{/n}
"Not every visit has to be about this. Some will be. I'd like the choice."
{n}You stay until she asks for the room to herself. She stands first, tired enough to lean against the table. You collect your things while she folds the cloth.{/n}
{n}At the door she remembers your cloak and passes it to you. Her hands are steadier now.{/n}''',
      c('[Stay with her until she asks for the evening to herself.]', flags=("anevia.bereavement_heard", "anevia.survivor_continues"))),
    n("part", "Anevia", '''{n}Anevia listens without looking away.{/n}
"I wish the answer were different. I am glad you haven't called it something I made you do."
{n}She draws the cloth back into her lap.{/n}
"Then give me some distance. I have people I can ask to come. You don't have to remain in a relationship you don't want so I won't be alone tonight."
{n}You leave when she asks. The sound of a chair moving follows you into the passage.{/n}''',
      c('[End only Anevia\'s romance.]', flags=("anevia.closed", "anevia.parted"))),
], requires=("anevia.lover", "irabeth_dead"), forbids=("anevia.irabeth_killed_by_commander",), chapters=(5,), delay=0)


def ending(identity, title, text, *, requires=(), forbids=(), owner="Epilogue"):
    local_close = () if identity == "ending_parted" else ("anevia.closed",)
    SCENES.append(scene("anevia." + identity, title, owner, 1, "",
        [n("end", "Narrator", text, portrait="Anevia")],
        requires=requires, forbids=tuple(dict.fromkeys(("closed", "trying", "committed", *local_close, *forbids))), last=6,
        Relationship="anevia", ForbidOverrides={"trying": "tirabade.group_closed", "committed": "tirabade.group_closed"}))


LIVING_END = ("anevia.closed", "anevia_dead", "anevia_gone", "irabeth_dead", "irabeth_gone", "inhuman", "sacrifice", "ascended")
ending("ending_kept", "The room with the repaired window", '''{n}Anevia kept the room. The window acquired a second repair, and the plant outgrew another pot before she admitted that she had become the sort of woman who asked neighbors for advice about roots.{/n}
{n}The Commander remained part of that life through visits that were actually arranged, messages that sometimes arrived late, and the work of saying when either of them minded. Anevia did not become easier to surprise, or less inclined to argue with an explanation she thought too convenient. She did become more willing to bring an unfinished thought to somebody she trusted to hear it.{/n}
{n}Her marriage to Irabeth remained a life with its own rooms, promises and disagreements. An invitation to one woman was not treated as an instruction to the other. Where affection overlapped, the people involved asked what they wanted instead of assuming that every shared evening had already been promised.{/n}
{n}Ressa's street remembered the false inspection. Some payments took longer to recover than anybody liked. Anevia kept asking after the women affected without turning Dema's help into a permanent obligation. The Commander knew enough of that work to admire it and enough of Anevia to disagree with her about it.{/n}
{n}There were evenings when nothing went well. There were nights neither wished to end. Sometimes Anevia looked up from a book or a troublesome seedling and seemed freshly pleased to find the Commander there. She usually made a joke before admitting it. The admission came more easily with practice.{/n}''',
       requires=("anevia.committed", "anevia.developed"), forbids=LIVING_END)
ending("ending_open", "An invitation without a final promise", '''{n}Anevia and the Commander kept seeing one another without calling their future settled. There were invitations accepted, others postponed and a few honest refusals that neither enjoyed. They learned which promises they could keep and stopped improving the sound of the ones they could not.{/n}
{n}Anevia's home with Irabeth remained her home. Her work remained demanding, and her private life contained more than the portions the Commander witnessed. The affection between them did not require her to apologize for those facts. Nor did affection make every absence easy.{/n}
{n}The room with the troublesome window continued to hold evenings of its own. On some visits the little game came out. On others it stayed folded while the two of them talked, or found a quieter use for the time. Anevia liked being asked. She also liked knowing she could give an answer that had not been prepared to preserve somebody else's expectations.{/n}
{n}On leaving, the Commander would sometimes find a goat in a pocket, a challenge to return it and try again.{/n}''',
       requires=("anevia.open_future", "anevia.developed"), forbids=(*LIVING_END, "anevia.committed"))
ending("ending_unfinished", "A question they had not finished", '''{n}Anevia and the Commander had begun a relationship with more questions than they had time to answer. They had kept evenings together, and there were still things Anevia wanted to ask when the next opportunity came.{/n}
{n}Anevia continued to make a life around the demands of the crusade and her marriage. She remembered the particular pleasure of being wanted without immediately being asked for a report. Some evenings she still thought of something she would have liked to say to the Commander, and considered whether to send an invitation.{/n}
{n}Whatever followed would require an answer from both of them. She disliked leaving the question to guesswork. Once, in the middle of another letter, she turned the page over and began a note of her own.{/n}''',
       requires=("anevia.lover",), forbids=(*LIVING_END, "anevia.developed", "anevia.committed"))
ending("ending_promised", "The next visit they had chosen", '''{n}Before the last campaign ended, Anevia and the Commander had chosen to keep a lasting relationship. The promise had been spoken plainly. They had not yet found all the days in which to learn how well they could keep it.{/n}
{n}Anevia kept the key on its green cord. Sometimes she wound it around a finger while composing a note, crossed out a perfectly good opening and began with the thing she actually wanted to ask. She had no intention of making every invitation sound like a test.{/n}
{n}Her home with Irabeth remained her home. The room she had chosen for herself still needed repairs. Neither fact surprised the Commander, who had been there when she explained what she wanted. There would be missed evenings and awkward conversations, but they had agreed to return to them.{/n}
{n}She looked forward to the next visit with an impatience she found faintly embarrassing. The embarrassment did not stop her sending the note.{/n}''',
       requires=("anevia.lover", "anevia.committed", "anevia.future_chosen"), forbids=(*LIVING_END, "anevia.developed"))
ending("ending_parted", "What remained after the goodbye", '''{n}Anevia did not describe the relationship as a mistake merely because it ended. There had been things she wanted, things she chose and things she would have done differently with the knowledge she gained afterward. The Commander was part of that history, without retaining a claim on what she would choose next.{/n}
{n}They gave each other distance where they could. Work sometimes brought them into the same room, and courtesy was possible before ease returned. Anevia did not promise that the two would arrive together, or perform a cheerful friendship to make the separation more flattering.{/n}
{n}Her life continued beyond the goodbye. She still had people to visit and work she meant to finish. Some evenings she left early, tired of being asked whether she was quite herself.{/n}''',
       requires=("anevia.parted", "anevia.closed"), forbids=("anevia_dead", "anevia_gone", "inhuman", "sacrifice", "ascended"))
ending("ending_survivor", "The life she did not stop living", '''{n}Irabeth's death remained part of Anevia's life. Grief did not become smaller because the Commander stayed, and the Commander did not become a replacement for the woman she had lost.{/n}
{n}There were visits Anevia asked for and others she could not bear. She learned to say which kind of day it was, imperfectly and sometimes too late. The Commander learned that accepting the answer mattered more than finding a reassuring interpretation of it.{/n}
{n}Their affection continued through that uncertainty. They spoke Irabeth's name, remembered ordinary things about her and sometimes spent an entire evening on another subject. A good day was allowed to be good without serving as evidence that the mourning had ended.{/n}
{n}Anevia kept choosing what to do with the life that remained hers. Some choices included the Commander. None required her to surrender the years she had loved her wife in order to deserve another evening of warmth.{/n}''',
       requires=("anevia.lover", "anevia.survivor_continues", "irabeth_dead"),
       forbids=("anevia.closed", "anevia_dead", "anevia_gone", "inhuman", "sacrifice", "ascended", "anevia.irabeth_killed_by_commander"))

# Native Coronation can remove Anevia before the conditional contact chapter.
# These endings remember earned romance without fabricating that visit or her consent to resume it.
ending("ending_grief_unanswered", "The invitation not yet renewed", '''{n}Irabeth died before Anevia and the Commander had spoken about what their relationship might become after that loss. Their earlier affection had been real. So had the life Anevia expected to keep with her wife.{/n}
{n}The Commander remembered her delight when a conversation went somewhere she had not expected, and the abruptness with which she could turn away from a question she disliked. There were questions now that no old invitation answered. Messages were considered, rewritten and sometimes put aside.{/n}
{n}Anevia had not promised another visit. The Commander could miss her without calling that silence an agreement. Whatever she chose next would come from a life whose center had changed.{/n}''',
       requires=("anevia.lover", "irabeth_dead"),
       forbids=("anevia_dead", "anevia_gone", "anevia.survivor_continues", "anevia.irabeth_killed_by_commander", "inhuman", "sacrifice", "ascended"))
ending("ending_wife_absent", "News that did not arrive", '''{n}Irabeth was no longer in the life the Commander had known in Drezen. That absence did not tell the Commander where she had gone, or settle what Anevia intended to do.{/n}
{n}There had been affection between Anevia and the Commander, and plans made while they could speak face to face. Now the questions that mattered could not be answered by remembering a pleasant evening. Anevia's marriage had never been an empty place waiting for somebody else to occupy it.{/n}
{n}The Commander kept the memory of her laughter. No message arrived that could turn the uncertainty into a renewed invitation, or into a reason to mourn a woman whose death had not been established.{/n}''',
       requires=("anevia.lover", "irabeth_gone"),
       forbids=("irabeth_dead", "anevia_dead", "anevia_gone", "anevia.irabeth_killed_by_commander", "inhuman", "sacrifice", "ascended"))
ending("ending_wife_killed", "The answer affection could not change", '''{n}The Commander had killed Irabeth. Whatever tenderness Anevia had once offered could not make that fact into a loss the two of them would simply share.{/n}
{n}There were memories of earlier visits, of Anevia reaching for a hand or stopping in the middle of a joke because she had begun to laugh herself. The Commander could remember them. They could not supply the forgiveness she had never given.{/n}
{n}No further romantic invitation came from Anevia. Her anger belonged to the woman who had loved Irabeth, and the Commander had no right to shorten it into a misunderstanding. The life that might once have included another evening together was gone.{/n}''',
       requires=("anevia.lover", "irabeth_dead", "anevia.irabeth_killed_by_commander"),
       forbids=("anevia_dead", "inhuman", "ascended"))

ending("ending_death", "The afternoons that had happened", '''{n}Anevia's death left no finished version of the life she and the Commander had been making. There were actual evenings to remember, actual disagreements, a particular way she looked pleased before deciding whether to admit it. Anevia had a way of making even a short visit leave something unfinished to laugh about next time.{/n}
{n}The Commander remembered her work as well as her warmth. She had wanted answers for people whose names were easy to treat as information. She had also wanted an ordinary room, an afternoon nobody improved into a duty and the chance to be ridiculous without becoming less loved.{/n}
{n}For a long time the Commander still turned at a familiar laugh in a crowded room.{/n}''',
       requires=("anevia.lover", "anevia_dead"), forbids=("inhuman", "ascended"))
ending("ending_gone", "Beyond the invitations that remained", '''{n}Anevia was no longer available to the Commander in the life they had known. An old invitation could not establish where she was now, whether she wished to answer, or what contact would require.{/n}
{n}The Commander had memories of real affection, and sometimes a question that would once have found its way to her. Those things gave the absence weight. They did not provide an address or justify treating a departure as a death.{/n}
{n}If another conversation became possible, it would have to begin with the woman who was actually there, and the choices that had brought her to it. For now, no reply came.{/n}''',
       requires=("anevia.lover", "anevia_gone"), forbids=("anevia_dead", "inhuman", "ascended", "sacrifice", "anevia.irabeth_killed_by_commander"))
ending("ending_sacrifice", "The answer she could not receive", '''{n}The Commander's sacrifice left Anevia with things she had intended to say on an ordinary evening. Some were affectionate. Some were arguments she could no longer finish. She resented how often people expected gratitude for the victory to settle what the loss felt like.{/n}
{n}She had known that no road promised a return. Knowing did not make an empty place easy to pass without looking. Nor did it make the evenings they had kept less real than the future they could not have.{/n}
{n}Anevia continued living among the people and obligations that remained. She did not have to become an emblem of somebody else's noble ending before she was allowed to miss the person she had wanted beside her.{/n}''',
       requires=("anevia.lover", "sacrifice"), forbids=("anevia_dead", "anevia_gone", "inhuman", "ascended", "anevia.irabeth_killed_by_commander"))
ending("ending_changed_power", "An answer power could not supply", '''{n}The Commander's transformation did not turn Anevia's earlier affection into an obligation to accept whatever followed. The life in which they had made their invitations had changed beyond the terms she chose.{/n}
{n}Nothing in a remembered kiss authorized possession, and nothing in a promise of future visits gave the Commander a right to rewrite her answer. Whatever remained of the history belonged to the people who had lived it, not to the power that could now claim so much else.{/n}
{n}The ordinary relationship did not continue merely because its old words could still be repeated.{/n}''',
       requires=("anevia.lover", "inhuman"), forbids=())
ending("ending_ascended", "The scale of an ordinary invitation", '''{n}Ascension changed what the Commander could become. It did not retroactively decide what Anevia had agreed to, or carry her into a divine household without an answer of her own.{/n}
{n}There had been a woman who liked an ordinary invitation, who found something to tease the Commander about even when she had meant to be solemn. The Commander had known her at that scale. Remembering it mattered more than giving the old relationship a grander title.{/n}
{n}Whatever contact might follow would have to respect the lives and choices that actually remained. Power could make remarkable things possible. It could not substitute for being asked, or make a person's silence into the answer the Commander wanted.{/n}''',
       requires=("anevia.lover", "ascended"), forbids=("inhuman",))
ending("ending_aeon", "An invitation outside the rewritten world", '''{n}In the rewritten world, the Commander's private history with Anevia no longer had the circumstances that made it happen. The particular room, the unfinished questions and the evenings she had chosen could not be restored by pretending that a different life owed the same answer.{/n}
{n}The woman who lived beyond that erased history belonged to herself. Whatever she loved or wanted there was not a reward held in reserve for the Commander who had changed the world.{/n}
{n}If any trace of their time together remained beyond ordinary memory, it was not a command to remember. It was the shape of an invitation nobody in that world had yet made.{/n}''',
       requires=("anevia.lover",), forbids=(), owner="AeonEpilogue")

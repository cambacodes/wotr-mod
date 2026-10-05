"""Anevia's independent, adult, graphic and explicit campaign.

The native marriage, actors and dispatchers are preserved.
Scenes and all civilian events below are authored alternate developments.
"""
from story_format import c, n, p, scene

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
    n("wanted", "Anevia", '''"Wasn't difficult. Wanted a pear. Wanted to sit down. You'd be amazed how rarely I manage both."
{n}She gives you another piece, then keeps one for herself.{/n}
"I plan useless things all the time. Badly, mostly. Beth once found a list of excuses I'd been makin' for not askin' her out. Thought it was a surveillance schedule."
"Was it?"
"Only in the sense that I knew where she'd be every hour of the day."
{n}Her grin goes crooked and soft at once, the way it only does for her wife.{/n}
"Took her to a place with terrible soup. We argued about that soup for three weeks. Best three weeks of my life, and I've robbed a cult treasurer."
{n}She rests her elbow on the basket.{/n}
"No soup here. Promisin' start."''', c('"Then let us give it something else worth remembering."', "watching")),
    n("disappear", "Anevia", '''"Most places, sure. Don't always want to use 'em."
{n}She looks along the street. A woman carrying a rolled carpet struggles through a doorway; a neighbor comes out to lift the far end. Anevia watches until the carpet is safely inside, the way she watches everything.{/n}
"Sometimes I want to sit on a wall in plain sight and eat a pear and have nobody come up to me with a dispatch. Wall's for that."
"You could have told me you wanted to be alone."
"Could've. Didn't. You're here, ain't you?"
{n}She nudges the basket toward your foot so a passing cart will not catch it.{/n}
"And don't go findin' my hidey-holes to prove you can. I know you can. If I want you somewhere private, I'll drag you there myself."''', c('"Then I will wait to be invited."', "watching")),
    n("yours", "Anevia", '''"Keep the directions. Tell me what it's like."
{n}She shifts on the wall and gives you her whole attention, which on Anevia feels a little like being picked out of a crowd by a pickpocket.{/n}
"Is it quiet? Or the kind of noise nobody expects you to answer?"''',
      c('"Quiet. Sometimes I want a little time when nobody\'s calling."', "quiet", flags=("anevia.commander_quiet",)),
      c('"People living around me. I like remembering they do that when I am elsewhere."', "noise", flags=("anevia.commander_company",)),
      c('"It is somewhere I can be bad at something without it becoming important."', "clumsy", flags=("anevia.commander_practice",))),
    n("quiet", "Anevia", '''"Then take it and don't say sorry. If I come lookin' and you're off being quiet somewhere, I'll sulk. I'm good at sulking. Nobody's died of it yet."
{n}She turns a pear in her hand, choosing where to cut.{/n}
"Only warnin' you, I'm terrible with quiet people. Start tellin' jokes at 'em like they're a sick relative."
"You?"
"Ask Beth. She's got a list."
{n}For a whole minute neither of you says anything. The street carries on without you. Then she hands you a thin slice of pear, as if that settles an argument.{/n}''', c('[Share a slice.]', "watching")),
    n("noise", "Anevia", '''"Then you'd have loved the soup place. Everybody had an opinion and none of 'em were about us, till Beth tried to defend the cook."
{n}She laughs at the memory.{/n}
"I like hearin' somebody gripe about a roof. Means they expect to be under it next month. Spend all day listenin' for bad news, a good ordinary complaint sounds downright filthy."
{n}The woman with the carpet reappears to argue with her neighbor about which way it should face. Anevia listens until they go inside again.{/n}
"There. Both wrong. Lovely."
{n}She looks at you, not the doorway.{/n}
"More afternoons like this, where that's the worst thing anybody's shoutin' about. That's what I'd take, if somebody was handin' 'em out."''', c('"So would I."', "watching")),
    n("clumsy", "Anevia", '''"Oh, that sounds dangerous. I'd pay to watch."
{n}She sees your expression and raises a hand.{/n}
"Not like that. Well. A bit like that. Fine, I'll bring somethin' I'm rubbish at too. Fair's fair."
"A terrible bargain."
"Only if somebody keeps score. I'll keep score."
{n}She tells you about a loaf she once attempted without asking anybody how much water went in. The story grows less plausible as she goes, until she admits the part about the broken knife happened to somebody else's bread.{/n}
"Mine just sat there. Refused to become anythin'. Had to admire the conviction, honestly."
{n}She laughs hard enough that she has to put the knife down.{/n}''', c('[Tell her which part you would like to try together.]', "watching")),
    n("watching", "Anevia", '''{n}Anevia has stopped cutting the fruit. She is looking at you the way she looks at a door she has already decided to open.{/n}
"You keep lookin' pleased to see me. I keep likin' it. That's gettin' to be a problem."
{n}She folds the cloth around the knife, taking care with the edge.{/n}
"Had three jokes ready about your taste in company. None of 'em get me out of this."
"Out of what?"
"Wantin' another afternoon. And not for the pears."
{n}Her hand lies on the wall a finger's width from yours. She does not move it closer, and she does not move it away.{/n}
"There. Said it before supper. Beth'd be proud. Then she'd want a word."''',
      c('"I am attracted to you. I want to be plain about what I\'d do about it."', "honest"),
      c('"I\'d like the company. Just the company."', "friend"),
      c('"We do not have to decide today. I would like another afternoon."', "wait")),
    n("honest", "Anevia", '''"Yeah. We would."
{n}She does not take your hand. She rubs a nick in the basket handle with her thumb.{/n}
"I love Beth. You make her miserable, you'll have two Tirabades to answer to, and she's the nice one."
"I heard you."
"Good. And I ain't sneakin' about behind her back. I tell her. Me. Tonight, probably, while she's got her boots off and can't storm out proper."
{n}Anevia picks up the basket. This time the repaired handle holds.{/n}
"So. Another talk, somewhere with fewer pears. You think about whether you meant that. I'll think about how to say it to Beth without her reachin' for her sword out of sheer habit."
{n}On the way back she walks close enough that your sleeves brush, and she does not make a joke about it.{/n}''', c('[Agree to another straight conversation.]', flags=("anevia.courtship_requested",))),
    n("wait", "Anevia", '''"Another afternoon, then. With a question in it this time. I'll bring the question. You bring your nerve."
{n}She gathers the cloth and the fruit stems. One pear has survived at the bottom of the basket.{/n}
"This one's goin' home. Beth'll ask if I had a good time. I'm gonna say yes, and I'm gonna watch her ears."
{n}Her look is direct.{/n}
"I did have a good time. Don't you dare make me sorry for it next time."
{n}You walk back slowly. At headquarters she leaves you at the door with a two-fingered salute that no officer would recognize and every thief in Kenabres would.{/n}''', c('[Keep the invitation open.]', flags=("anevia.courtship_requested",))),
    n("friend", "Anevia", '''"Right. That's an answer."
{n}She looks down at the basket for a moment, then picks it up.{/n}
"Gonna feel like an idiot for a day. Don't help. I've had practice."
"I liked the afternoon."
"So did I. We'll keep that bit."
{n}She gives you the last pear and keeps the knife. On the walk back she finds something to complain about, a loose cobble, a rude pigeon. You let her have it.{/n}''',
      c('[Shake your head.] "Friends, Anevia. Nothing more."', flags=("anevia.closed", "anevia.local_declined"))),
], forbids=("a_affair", "trying", "committed", "anevia.courtship_requested", "irabeth_dead", "irabeth_gone"), delay=0)


s("a_question_at_home", "The question before the answer", [
    n("start", "Anevia", '''{n}Anevia meets you with two mugs and no report. She pushes one across to you, tests the other and makes a face.{/n}
"Too hot. Been waitin' so long to ask you this I figured I could at least get the tea right. Missed that too."
{n}She sits opposite you.{/n}
"I told Beth. That there's somebody I've started wantin' to see for reasons I can't file under work. Told her it was you. Told her nothin's happened."
{n}She blows on the tea.{/n}
"She asked if I was leavin' her. I said don't be daft. Then she asked if I wanted her to be happy about it. That one took the rest of the night."
"What did you tell her?"
"That I'd like her happy. That I wasn't gonna wait for happy before askin'. She threw a boot at me. Missed on purpose. Then we talked till the candle went."''',
      c('"What does she want from me?"', "wife"),
      c('"What do you want, now that you have said it aloud?"', "desire"),
      c('[Ask to leave this conversation for another day.]', abort=True)),
    n("wife", "Anevia", '''"To look at you. Beth likes to see a person's face when they say a thing. Paladin habit. Or orc habit. She won't tell me which."
{n}She rubs at a mark on the mug with her thumb.{/n}
"She'll want you alone. Don't go in there rehearsed. She's questioned cultists, she knows what rehearsed sounds like. And she ain't interviewin' you for a post, so don't bring references."
"And if she says no?"
"Then she says no, and I find out what I'm made of. Might be somethin' ugly. Rather find out over tea than on some doorstep at midnight."''', c('"Before I go near Beth, what do you want out of this?"', "desire")),
    n("desire", "Anevia", '''"You. On your own account. Not as a thing I've arranged around Beth."
{n}She laughs at herself, short and embarrassed.{/n}
"I want to know if you argue when you're comfortable. I want a walk that ends with me kissin' you, without spendin' the whole walk makin' up a reason I happened to be goin' that way."
"And at home?"
"Home's Beth. The woman who knows which boots pinch her and which sermon she's about to pick a fight with. That's mine and it stays mine. You'd be somethin' extra, not somethin' instead."
{n}She takes a cautious drink. The tea has finally cooled.{/n}
"There. Didn't fit in one sentence. Spies are meant to be brief. I'm a disgrace."''',
      c('"I want you. Not Irabeth. You."', "separate", flags=("anevia.wants_separate",), forbids=("irabeth.lover",)),
      c('"I could want you both. Tonight I\'m only talking to you."', "possible", flags=("anevia.group_possible",), forbids=("irabeth.lover",)),
      c('"There are others. I\'ll tell you straight how many nights I\'ve got."', "other", flags=("anevia.other_loves_known",)),
      c('"Irabeth and I are together already. I want your answer, not hers."', "her_marriage", requires=("irabeth.lover",), forbids=("irabeth.closed",)),
      c('"Irabeth and I are finished. I won\'t use you to get back to her."', "past_marriage", requires=("irabeth.lover", "irabeth.closed"))),
    n("past_marriage", "Anevia", '''"Then I'm not your messenger. You want somethin' said to Beth about the two of you, walk up and say it yourself."
{n}She looks at you over the mug.{/n}
"This here's about you and me. If it goes near whatever you had with her, she'll tell you so. Loudly. Probably in front of the guard."
"I can live with that."
"You'll have to. Didn't marry a quiet woman."''', c('"That was then. Ask me what you came to ask."', "time")),
    n("her_marriage", "Anevia", '''"Good. Saves me makin' a speech about it."
{n}Her smile is small and a little nervous, which on Anevia is a rare thing to see.{/n}
"I know what you and Beth have got. Don't mean I know what you and I would be. I want my own go at findin' out. My own evenings. With my name on 'em."
"And if all three of us want an evening?"
"Then somebody buys a bigger table. Not tonight."
{n}She wraps both hands around the mug.{/n}
"I'm glad she's got you. Doesn't stop me bein' greedy."''', c('"I am answering you, Anevia. Not her."', "time")),
    n("separate", "Anevia", '''"Then tell her exactly that. Beth'll hear 'he wants all of us' in a weather report if she's nervous enough."
{n}Anevia leans back, considering you.{/n}
"I'd like you two in one room arguin' about somethin' stupid. The way I carry a basket. My bread. Somethin' like that."
"You would take her side."
"Depends if she's right. And whether you just dropped the basket."
{n}She grins, then lets it go.{/n}
"And if you two ever gang up on me about the bread, I'm leavin' the pair of you for the baker."''', c('"And what do you get out of it?"', "time")),
    n("possible", "Anevia", '''"Keep that 'could' where it is. Don't polish it."
{n}She says it kindly, then gives you a sharper look.{/n}
"My wife ain't the second half of a bargain. Might be she fancies you. Might be she'd rather see you across a council table. I haven't asked her, and I won't ask for her."
"I would not want that."
"Then don't turn up with a plan for three over one cup of tea. You want Beth, you go stand in front of her like a recruit and see what happens. I'd pay to watch."
{n}She taps the table.{/n}
"Right now it's you and me. I'm enjoyin' that more than I figured. Let me have it."''', c('"Then let us talk about you."', "time")),
    n("other", "Anevia", '''"Then tell me which of your nights have already got somebody's name on 'em. I don't need the gossip. Just the dates."
{n}She listens while you describe what you can offer. Once she cuts you off when the answer starts sounding grander than it is.{/n}
"One evenin' you actually turn up for beats a month you promise and don't."
{n}She thinks for a moment.{/n}
"You change a plan, you tell me. Don't make me the one who always gets bumped 'cause she understands about the war. I understand fine. I'll still throw somethin'."
"You may have to change plans too."
"I will. Then you get to throw somethin'. Mind the good jug."''', c('"Then let us speak about the time we can keep."', "time")),
    n("time", "Anevia", '''"I want evenin's at home that ain't just the gaps between your visits. And evenin's with you that ain't all spent apologizin' for goin' home. Both. Greedy, told you."
{n}She reaches for the teapot, finds it empty and laughs under her breath.{/n}
"Also I want to know how much tea two people drink talkin' about this. Answer's apparently all of it."
{n}You fetch more water together. She lets you carry the pot and takes the mugs herself, refusing to let you balance all three.{/n}
"I want to see what you'd do if you picked," {n}she says.{/n} "Not what you think I'd like. Kenabres, the year before the Heart, I spent a month bein' exactly the barmaid a cultist wanted to talk to. Laughed at his jokes. Drank his wine. Got so good at it I forgot I hated his wine. Took me weeks after to remember what I did like."
{n}She sets the mugs down in their old places.{/n}
"You catch me laughin' at a joke of yours I don't find funny, pour your drink down my back. I'll know what it's for."''',
      c('"Name the night. I\'ll be there before you are."', "finish"),
      c('"I do it too. Easier to fix a thing than ask for one."', "useful"),
      c('"I have thought about it. Friendship is what I can offer."', "stop")),
    n("useful", "Anevia", '''"I know. That's why I asked."
{n}She gives you a rueful look.{/n}
"You turned up empty-handed and I gave you a basket to fix. We could go on like that for years. Two people bein' useful at each other."
{n}She puts the pot where neither of you has to tend it.{/n}
"So next time, don't bring me a reason. Bring whatever mood you're in. Foul one, if that's what you've got. I'll try not to tidy mine up for company."
"That may go badly."
"Might be the best evenin' we've had."
{n}Her hand starts across the table toward yours. She stops it halfway and leaves it there, palm up, which is almost worse.{/n}
"Soon. I ain't patient. I'm doin' an impression of patient. It's slippin'."''', c('"I\'ll do my share of the talking."', "finish")),
    n("finish", "Anevia", '''"I'll tell Beth you'll see her. Find her when she's got a free hour. Not in the middle of drill, she'll bite your head off out of reflex."
{n}She rises with you, then stops by the door.{/n}
"And after, don't come back and explain my marriage to me. Tell me what she said to your face and what you thought of it. I'll tell you where you've got it wrong."
{n}You agree. She grins, still nervous under it.{/n}
"Good. That's the hard bit done. Knew we'd get somethin' done if we sat here long enough."''',
      c('"Then we talk to Irabeth. Together."', flags=("anevia.spousal_conversation_requested",))),
    n("stop", "Anevia", '''{n}Anevia does not answer at once.{/n}
"That stings. Not gonna pretend it doesn't."
{n}She moves your mug back from the edge of the table without looking at it.{/n}
"Glad you said it here, though, and not after I'd made a fool of myself somewhere public. I'll tell Beth the question's off. Don't go explainin' yourself to her, she'll only feel sorry for you."
"I did want the afternoons."
"Me too. Give me a week before the next one. I'm gonna be very grown-up about this, right after I've been childish for a bit."''',
      c('"I cannot, Anevia. Not like this."', flags=("anevia.closed", "anevia.local_declined"))),
], requires=("anevia.courtship_requested",), forbids=("a_affair", "trying", "committed", "irabeth_dead", "irabeth_gone"))


s("one_truth", "The person who was not told", [
    n("start", "Anevia", '''{n}Anevia shuts the door and walks away from it before she speaks. She does not ask you to sit.{/n}
"We said we'd tell her. I've heard that sentence every time somebody's asked me how my day's goin'."
{n}She looks tired, and angry at being tired.{/n}
"I told Beth there was somethin' she had to hear from both of us. She asked if you and I had been together. I said yes. Didn't make her guess so we could stage it nicer."
{n}Outside, a cart is being unloaded, crate by crate.{/n}
"She wants to see you. Alone. I've told her what I did. She wants to hear what you thought you were doin'."
"How did she take it?"
"How d'you think? She took it like a paladin who married a spy and thought she'd got the only honest one."
{n}Anevia rubs her hands together once, hard, then stops.{/n}
"Sorry. That one was meant for me."''',
      c('"I\'ll tell her. Don\'t soften it for me."', "account"),
      c('"Do you still want me?"', "want"),
      c('"Then maybe we just stop, and let it go quiet."', "disappear"),
      c('"Not today. Ask me again."', abort=True)),
    n("want", "Anevia", '''"Yes. That's the whole bloody problem."
{n}She meets your eyes.{/n}
"I ain't gonna tell her you meant nothin' so I look better. And I ain't gonna tell you she matters less so you feel safe. You'd both smell it on me."
"I was afraid you regretted all of it."
"I regret not tellin' her. The rest of it..."
{n}Her mouth twists.{/n}
"I wanted to see you this mornin'. Then I was furious I wanted to. Then I came anyway. That's as straight as I can give it you."''', c('"Then let\'s give her a true one too."', "account")),
    n("disappear", "Anevia", '''"It won't disappear for her. It'll just turn into somethin' she's meant to know and never mention."
{n}Anevia's voice goes low and flat.{/n}
"Walk away from me if you want. Can't walk away from what we did. I'm goin' home to tell her, with you or without you."
{n}She waits, and does not make it easier.{/n}''',
      c('"You\'re right. I wanted you to face her without me. That was cowardly."', "account"),
      c('"It\'s over between us. Tell her that too."', "stop")),
    n("account", "Anevia", '''"Don't give her a speech about how love's complicated. She knows. She married me."
{n}For a moment something like humor touches her face, then goes.{/n}
"Tell her what happened. Answer what she asks. She'll ask the nasty ones first; she questions cultists for a livin'."
{n}She pushes the window open far enough to hear the street.{/n}
"I asked if she wanted me to sleep somewhere else tonight. She said she wanted me to stop decidin' what she wants before she's opened her mouth. So I'm goin' home. We'll fight. Might sit in separate rooms for an hour. Still home."
"And us?"
{n}Anevia turns back toward you.{/n}
"No more sneakin'. After that, we see what's left standin'. Don't know yet."
{n}She picks up her coat from the back of the chair.{/n}
"I want there to be somethin'. Thought you ought to know that before you go in there."''',
      c('"We tell Irabeth. All of it."', flags=("anevia.spousal_conversation_requested", "anevia.single_affair_disclosed"))),
    n("stop", "Anevia", '''{n}Anevia shuts her eyes for a moment.{/n}
"Right. I'll tell her."
{n}When she opens them, she looks at you straight.{/n}
"Don't call it a kindness. Might be right. Still hurts like a kick. And don't stand there tryin' to work out what face I ought to be makin'."
{n}You leave her to go home and have the conversation alone. What happened between you is not undone because it has ended.{/n}''',
      c('"It happened. It ends here."', flags=("anevia.closed", "anevia.local_declined"))),
], requires=("a_affair", "a_morning", "a_will_tell"), forbids=("i_affair", "trying", "committed", "anevia.spousal_conversation_requested", "irabeth_dead", "irabeth_gone"), delay=0)


s("beths_question", "An answer that is hers", [
    n("start", "Irabeth", '''{n}Irabeth has picked a small room with no council table in it. Two chairs by a window. Her gloves lie folded on the sill, fingers squared one over the other, as if they were due for inspection.{/n}
"Commander. Anevia is not outside the door. I checked. Twice."
{n}She points you to the other chair and does not sit until you have.{/n}
"I spent the morning drafting what a sensible woman would say to you. I burned the draft. It was very sensible. None of it was true."
{n}Her hands settle on her knees.{/n}
"Before anything else. You outrank me in the field, in council and on every piece of paper in Drezen. You do not outrank me in my own marriage. Tell me you know that, or we stop here."''',
      c('"Tell me I\'m wrong if I\'m wrong. I\'ll still sign your orders."', "history"),
      c('"Of course. I expect you to remain loyal despite this."', "rank"),
      c('"Not now. When I can hear you properly."', abort=True)),
    n("rank", "Irabeth", '''"Then I heard you wrong. Or I heard you right."
{n}She stands. It is a controlled movement, and there is nothing uncertain in it.{/n}
"I will do my duty until the Wound is shut. That duty does not come with my wife attached to it."
{n}She takes the gloves off the sill.{/n}
"If that is what you meant, we are done. If it is not, say what you did mean. Plainly. I have no patience left today for anything else."''',
      c('"I used the wrong words because I was nervous. Your answer is yours."', "history"),
      c('"I meant it. This shouldn\'t get in the way of your duty."', "refused")),
    n("history", "Irabeth", '''{n}Irabeth sits again and pulls her chair a little nearer the window, where the light is worse for her and better for seeing your face.{/n}
"Anevia has told me her side. Now yours."
{n}She does not ask you to start by swearing nobody meant any harm. Her expression says she has already heard that one and filed it under useless.{/n}''',
      c('"We want each other. We came to you first, before anything started."', "before", forbids=("a_affair",)),
      c('"We crossed a line while you did not know. I knew she was keeping it from you, and I took part."', "after", requires=("a_affair", "anevia.single_affair_disclosed"))),
    n("before", "Irabeth", '''"You came to me first. Good. That is how it should be done, and it is rarer than it ought to be."
{n}She looks at the window frame, where the paint has worn through.{/n}
"I have been sitting here trying to decide what I feel so I can report it properly. That is a coward's way of not saying it."
"Then say it."
"I am afraid. And I am angry that I am afraid. I know she loves me. I know wanting something is not the same as being unhappy. I could preach it to a hall of recruits."
{n}The corner of her mouth moves.{/n}
"And still I can see myself being very gracious about all of this, and very alone at the kitchen table. I will not be that woman. I would sooner shout at you now."''', c('"What do you want us to understand?"', "needs")),
    n("after", "Irabeth", '''{n}Irabeth looks at her hands. When she speaks, she spaces her words the way she spaces an order that must not be misheard.{/n}
"You did not start by telling me what I failed to give her. Good. I would have thrown you out."
"That was not the reason."
"I know. Anevia keeps trying to comfort me for what she did. I keep refusing. We are both very tired."
{n}She turns one hand palm up, then lays it flat.{/n}
"I was keeping supper for her. Small things. Whether to wait for her before I ate. You two knew something that made all of it foolish, and I went on keeping supper. I do not want to hear what you did. I want you to know I was in the next room of it."
{n}Her gaze comes back to you.{/n}
"I love her. I am furious with her. I will carry both. I did not ask you to help me pick one."
"I will not."
"And I do not know if I can stomach a thing that started behind my back. I am willing to ask the question. That is all I have for you today."''', c('"Tell me what I have to hear before you decide."', "needs")),
    n("needs", "Irabeth", '''"My home stays my home. I do not come back to it and find I have walked in at a bad hour. Our evenings stay ours. They are not what is left over when you have had yours."
{n}She stops and scowls at her own words.{/n}
"That sounds like the quartermaster dividing rations. Fine. I have been a soldier longer than I have been anything else."
{n}Outside, somebody in the yard shouts for a friend. Irabeth waits for the answer before she goes on.{/n}
"And Anevia speaks for Anevia. I will not sit in a room with you haggling over what my wife ought to want. She would skin us both."
"She told me much the same."
"Of course she did. She is always one step ahead of me and pretends she is not. It is her most annoying virtue."''',
      c('"I\'m asking for her. You don\'t have to like it, and you don\'t have to want me."', "not_courtship", forbids=("irabeth.lover",)),
      c('"What would happen if you decided you could not live with it?"', "refusal"),
      c('"Do you want to know how much time I can really give, other commitments and all?"', "practical"),
      c('"You and I are together too. That doesn\'t mean you have to say yes to this."', "already_lovers", requires=("irabeth.lover",), forbids=("irabeth.closed",)),
      c('"We\'re finished, you and I. I\'m not using Anevia to get back to you."', "past_lovers", requires=("irabeth.lover", "irabeth.closed"))),
    n("past_lovers", "Irabeth", '''"Good. I wanted that said aloud, not left for me to work out from everybody's good manners."
{n}She takes a breath.{/n}
"What we had and ended will colour some of this. I will not pretend otherwise. It does not decide what Anevia wants, and I will not make her choose my way because she wears my ring."
"What should I do?"
"Be clear. Do not use her door to walk back through mine. And when I object to something, do not decide it is the old quarrel in a new coat. Sometimes I will simply be right."
{n}She glances at the gloves.{/n}
"New question. We will answer it straight, or not at all."''', c('"Then ask it straight."', "practical")),
    n("already_lovers", "Irabeth", '''"No. It does not."
{n}The look she gives you is warm and does not let you off anything.{/n}
"I want our time. I want my marriage. And now Anevia wants something with you that is hers. Fine. I can picture the three of us at one table, some night. Picturing it is not the same as promising it."
"We can keep the questions apart."
"We will. I will not wake up one morning to find I promised a shared house because I liked seeing you make my wife laugh. When somebody wants the bigger thing, they ask for it. Out loud."
{n}Her hand covers yours for a moment, rough and warm, then goes back to her knee.{/n}
"I am answering as your lover and as her wife. I can do both. I have done harder drills."''', c('"Then tell me what you will and won\'t have."', "practical")),
    n("not_courtship", "Irabeth", '''"Good. I was beginning to wonder if I would be expected to be grateful for being left out."
{n}She gives you a level look and lets the awkwardness sit there for both of you.{/n}
"I can like you without courting you. I can love Anevia without wanting everything she wants. I would like all of it to be very, very dull."
"It will be."
"Then keep arguing with me about patrols. If every quarrel over a watch rota turns into a private message about my wife, I will resign my commission and take up goats."
{n}The smile is short, and real.{/n}
"I know this household. That is not a joke. It is a forecast."''', c('"Then let us talk evenings, not forecasts."', "practical")),
    n("refusal", "Irabeth", '''"Then I would tell her no. She would decide what she could live with, and I would decide what I could. You would not get a vote."
{n}She does not make it sound easy.{/n}
"I do not want to leave her. I am not saying it so someone will run to reassure me. But if there is no answer I could refuse, you have not come to ask. You have come to inform me, and politely."
"And if the answer is no?"
"Then you hear no, and not some pretty word for yes. I have not got there yet. I want time."
{n}She unfolds the gloves and folds them the other way.{/n}
"And time is not an invitation to come back with a better speech. I have heard your speeches. They are good. That is the trouble with them."''', c('"Then think on what you have to consider, and take that time."', "practical")),
    n("practical", "Irabeth", '''{n}You go through the visits you could keep. Irabeth asks what happens when a battle moves them, and whether anyone means to use her knowledge of the war as a reason she may never complain. You tell her where you could leave word. She tells you how she wants to be reached: in writing, not through a runner who will repeat it in the mess.{/n}
{n}She tells you about an evening Anevia meant to teach her a card game. Work interrupted it three times. By the end Irabeth knew every rule and had enjoyed none of it. Anevia took the cards away and asked when she intended to actually turn up.{/n}
"She was right. I hate that. I have my own bad habits, and I do not want this to give me better excuses for them."
{n}You talk until the light has crawled across the window frame. Irabeth writes one proposed evening on a scrap, then crosses it out when you remember a prior duty. The crossing-out seems to settle her more than anything you have said.{/n}
"You caught it before it was somebody else's problem. Good."
{n}She leaves the scrap on the sill.{/n}
"I will speak with Anevia. Give us some days. Then I will tell you my answer, myself."''',
      c('[Stand.] "Take your time, both of you."', flags=("anevia.spouse_heard",))),
    n("refused", "Irabeth", '''"Then I will tell Anevia exactly what you said. Word for word. I have a very good memory for words."
{n}Irabeth opens the door and holds it, as for an officer leaving a court-martial.{/n}
"She asked me to hear you. I have. I will keep serving the crusade. Do not mistake that for anything else."
{n}She does not punish either of you with her command. She does not have to.{/n}''',
      c('[Nod.] "Understood, Knight-Captain."', flags=("anevia.closed", "anevia.authority_refused"))),
], requires=("anevia.spousal_conversation_requested",), forbids=("irabeth_dead", "irabeth_gone"), owner="Irabeth")


s("beths_answer", "What she can agree to", [
    n("start", "Irabeth", '''{n}This time Irabeth sees you at the end of an ordinary working day. She puts the last report into its box and closes the lid before she speaks, so that the one business does not touch the other.{/n}
"Anevia and I have talked. Several nights. On the second she asked if we could stop for an hour and do something else, and I found out I had been mistaking talking for getting anywhere."
{n}A faint smile.{/n}
"We played the card game. She won. I do not think she would have survived losing it that night."
{n}Then she is serious again.{/n}
"She may court you. Our house stays ours. She can ask you into a room of her own; that does not make our room somewhere I must avoid. Our nights are nights, not whatever she has left. Yours will be treated the same."
{n}She waits until she is sure you have heard all of it.{/n}
"I have not promised to like every part of this. I have promised to say it when I do not, instead of sulking until she guesses. That was the hardest thing I have signed this year."''',
      c('"Is that a yes, or are you scared of losing her?"', "choice"),
      c('"I can keep those terms. Your house stays yours."', "history"),
      c('"I\'ve thought again. I shouldn\'t start this."', "decline"),
      c('"Sleep on it. Both of you."', abort=True)),
    n("choice", "Irabeth", '''"Both. I would not trust a woman who told you fear had nothing to do with it."
{n}She considers how to go on.{/n}
"Anevia asked what I would say if I knew she would stay whatever I said. I was angry she asked me something I could not answer on the spot. Then she said she would wait while I tried."
"And now?"
"Now I want to try. I want a wife who tells me what she wants while there is still time to do something about it. Not one who has learned which wants I can bear to hear."
{n}Irabeth looks straight at you.{/n}
"And I can still refuse. I refused her first idea, moving our evenings about at the last moment. She thought about it and agreed. I have not handed in my right to say no."''', c('"Then I\'ll take your answer as you gave it."', "history")),
    n("history", "Irabeth", '''{n}Irabeth rests one hand on the back of her chair.{/n}
"One more thing. I want it said before we are done."''',
      c('"Say the rest of it."', "hurt", requires=("a_affair",)),
      c('"What are you still unsure of?"', "uncertain", forbids=("a_affair",))),
    n("hurt", "Irabeth", '''"I said yes to this. I never said yes to the lying. I am still angry about it. Anevia knows; I threw a boot."
{n}Her voice stays level.{/n}
"Some nights I can take her hand and think of nothing. Some nights I lie there doing the arithmetic of every evening she said she was at the Heart. Both kinds of night are still my marriage, and she is still in it."
"What do you want from me?"
"Keep your word now. Tell me if something changes. And do not come round expecting me to forgive you on schedule so the two of you can sleep better."
{n}She straightens the back of the chair, which was already straight.{/n}
"I can wish you a good night with her and have a bad one myself. I am a grown woman. I have had worse nights in trenches."''', c('"Say it however it comes out."', "finish")),
    n("uncertain", "Irabeth", '''"I do not know if it will be easy. I expect some days worse than others."
{n}A wry look.{/n}
"Anevia says that is also what being married to me is like. She did not say it kindly enough to be comforting."
"Did you object?"
"Yes. Then I remembered I had started a fight that morning about where a wet cloak belongs."
{n}The smile stays.{/n}
"I do not need the three of us to be an example to anyone. I want our promises to become boring. Kept, and never talked about."
{n}She leaves the chair alone.{/n}
"If I start making a speech, cough. Discreetly."''', c('"I can promise discretion about speeches."', "finish")),
    n("finish", "Irabeth", '''"Then go and speak with her. She has her own answer, and it is none of my business what it is."
{n}Irabeth picks up the last paper, then puts it down again.{/n}
"And Commander. This need not be the only thing you and I ever talk about behind a closed door. I still have opinions about books. And about that gate by the stables, which is a disgrace."
{n}You suggest an afternoon. Irabeth checks it against her duties, then asks whether the weather will hold.{/n}
"Good. The gate really is a disgrace. I have been trying all afternoon not to sound like myself about it."''',
      c('[Take her at her word and speak with Anevia.]', flags=("anevia.marital_terms_agreed",))),
    n("decline", "Irabeth", '''"Then tell Anevia. Yourself. And do not tell her it was my doing."
{n}She pauses.{/n}
"You may change your mind. She may be hurt by it. Do not either of you hide behind me."
{n}You agree to tell Anevia yourself. Irabeth does not thank you for it.{/n}''',
      c('"Then I won\'t ask it of either of you."', flags=("anevia.closed", "anevia.local_declined"))),
], requires=("anevia.spouse_heard",), forbids=("irabeth_dead", "irabeth_gone"), delay=72, owner="Irabeth")


s("her_own_answer", "The invitation she kept", [
    n("start", "Anevia", '''{n}Anevia has borrowed a room with a table too big for it and a window that will not quite shut. She shows you the second fault the moment you walk in.{/n}
"In case you were expectin' a seduction in perfect comfort. You're not gettin' one."
{n}A folded cloth on the sill stops the frame rattling. Two cups and a plate of sliced fruit sit at one end of the table. At the other lies a shallow wooden box, empty but for a scrap of sandpaper.{/n}
"Beth says she talked to you. I told her I was bringin' you here. She said eat somethin' before you get eloquent."
{n}Anevia points at the plate.{/n}
"Precautions."
{n}She watches you put your things down, and the grin goes quieter when you look back at her.{/n}
"Still want you. Figured I'd say so before I found somethin' clever to do with my hands."''',
      c('"I want you too. What were you planning for the box?"', "box"),
      c('"I have been thinking about kissing you all the way here."', "want"),
      c('"Another evening. I will keep it."', abort=True)),
    n("box", "Anevia", '''"Growin' somethin'. Killin' it first, probably. Then askin' somebody what I did wrong."
{n}She turns the box so its rough edge catches the light.{/n}
"Woman at the market's got cuttin's of a herb she puts in soup. Smells better than our cook's whole cupboard. Said I could have one once I had somewhere for it."
"A garden?"
"A box. Don't promote it till it's survived me."
{n}She rubs the edge with the sandpaper and brushes the pale dust off her sleeve.{/n}
"Somethin' that needs doin' every day and nobody dies if I forget. Mostly. She said don't drown it. Apparently it's got limits."
{n}She sets the box down.{/n}
"You can hold it steady. Or sit there and watch me botch it. Either's fine."''',
      c('[Hold the box while she smooths the edge.]', "working", flags=("anevia.box_helped",)),
      c('"I would like to watch you make something for yourself."', "watching", flags=("anevia.box_watched",))),
    n("working", "Narrator", '''{n}You brace the box while Anevia works along the rough edge. She is patient with the wood and less patient with your advice. After the third suggestion she looks up.{/n}
"You're holdin' it beautifully. Now stop tellin' me where the splinters are. We've been introduced."
{n}You apologize. She tugs the box a little, in case you were thinking of letting go.{/n}
"There. A row. Nobody resigned."
{n}When the edge is smooth she runs her thumb along it, looks pleased, and finds another rough place at once. This time she points it out herself before you can. By the end, a little heap of dust has gathered on the cloth under your hands.{/n}
{n}She folds the dust into the cloth and sets the box on the sill. It sits crooked. She turns it round, finds the other way worse, and turns it back.{/n}
"A home," {n}she says.{/n} "With faults. Keeps it humble."''', c('[Sit with her when she has finished.]', "want")),
    n("watching", "Anevia", '''"Then I'll try not to show off for you. Might take all night."
{n}She works while you talk. Once she starts telling you about a lock whose owner swore it could not be opened, and catches herself halfway through turning it into a boast.{/n}
"Listen to me. Nobody asked."
"I liked the story."
"So did I. That's how I get away with it."
{n}She finishes the edge and lifts the box toward you, and the question on her face is whether you like it, not whether you are impressed. You point to the one small unevenness you like. She says you have picked the worst bit, and leaves it.{/n}
"Fine. It can remind me somebody was sittin' there."
{n}She sets the box on the sill and comes back to the table.{/n}''', c('[Make room beside you.]', "want")),
    n("want", "Anevia", '''{n}Anevia comes round the table and stops close, close enough that you can smell sawdust and pear on her.{/n}
"Had a whole plan for this bit. Lines and everythin'. Lost 'em when you walked in."
{n}Her fingers brush the back of your hand.{/n}
"So I'm just gonna kiss you. Unless you'd rather I kept talkin'. I can. For hours."
{n}The window rattles against its cloth, the box sits crooked on the sill, and she does not look at either of them.{/n}''',
      c('"Yes. I would like that."', "kiss"),
      c('"Come sit close. I would like to begin there."', "near"),
      c('"I can\'t give you what we\'ve been talking about."', "stop")),
    n("kiss", "Narrator", '''{n}She kisses you like she has been planning it for a month, which she has. Her hand settles at the side of your neck. When you lean into it she makes a small pleased sound in her throat and does not let go until you are both grinning against each other's mouths.{/n}
"There goes the rest of my eloquence."
{n}You tell her she can try again later. She kisses you once more before she agrees. When she draws back she stays with her forehead near yours, close enough that none of her usual quick deflections would have anywhere to go.{/n}
"Wanted that."
"I noticed."
"Good. Wasn't bein' subtle."
{n}She drops onto the bench beside you, knee against yours. The wind shoves at the window until the cloth catches it. Anevia glances at it and, for once, does not get up to fix anything.{/n}''', c('[Stay close and ask what she would like from this evening.]', "evening", flags=("anevia.first_evening_kissed",))),
    n("near", "Anevia", '''"Right there, then. I can do that without makin' a speech."
{n}She takes the place beside you. At first your shoulders touch only when somebody moves. Then she leans in properly and leaves her weight there.{/n}
"You want the kiss later, you know where I am. I'll be right here, bein' charmin'."
{n}You ask whether the box will survive the plant. She says the woman with the cuttings is more worried about the plant surviving the box, and the account turns into a long argument about which of them has less faith in Anevia, with Anevia arguing both sides and enjoying herself enormously.{/n}
{n}She stays pressed against your side the whole time.{/n}''', c('[Lean into her.]', "evening")),
    n("evening", "Anevia", '''"Tell me somethin' you thought today and didn't say 'cause it wasn't important."
{n}She props her chin on her fist.{/n}
"Not a confession. Somethin' that got up your nose. Or made you laugh. Or made you wish you'd gone down the other street."
{n}You find one. She asks a question you did not expect, and the small thing turns into a story. When you finish, she gives you one of hers: a woman who once tried to sell her an extremely loud coat for discreet work.{/n}
"Said nobody'd ever suspect a spy of such bad taste."
{n}You ask if she bought it.{/n}
"Couldn't afford to be that inconspicuous."
{n}Later she taps the back of your hand and asks when she gets you again. You name a day you can actually keep. She checks it against her own promises, and nods.{/n}
"Good. Somethin' to look forward to that ain't an intercepted letter."''',
      c('[Kiss her.] "Yes. You, and everything you come with."', flags=("anevia.lover", "anevia.personal_ready"))),
    n("stop", "Anevia", '''{n}Anevia takes her hand back and sits down in the other chair.{/n}
"Then say it now. Before I start rememberin' tonight as somethin' it wasn't."
{n}You tell her as well as you can. She listens, asks one question, and takes the answer without making it easy for either of you.{/n}
"Go on. I'll be fine. Just don't want company while I work out how disappointed I am."
{n}You go. Behind you, she shoves the other chair back under the table.{/n}''',
      c('"I can\'t, Nevi. I\'m sorry."', flags=("anevia.closed", "anevia.local_declined"))),
], requires=("anevia.marital_terms_agreed",), forbids=("anevia.personal_ready", "irabeth_dead", "irabeth_gone"))


s("a_place_of_our_own", "A date that belongs to two people", [
    n("start", "Anevia", '''{n}Anevia catches you on the way out of a long talk about a future with more people in it than most tables will seat.{/n}
"I want a night with you. Just you. Nothin' wrong with the other sort. I just want this sort too."
{n}She leans on the back of an empty chair.{/n}
"We've spent weeks workin' out what the three of us can manage. I don't want to wake up one day and find I've forgot whether you and me are any fun without Beth there to keep the conversation goin'."
{n}She grins.{/n}
"I reckon we are. Want proof."''',
      c('"I\'d like that. We don\'t have to start from scratch."', "history"),
      c('"Does Irabeth know you are asking?"', "wife"),
      c('[Leave the invitation for another evening.]', abort=True)),
    n("wife", "Anevia", '''"Course she does. Looked at me like I'd asked permission to like rain."
{n}Anevia's impression of her wife's solemn face is loving and not quite fair.{/n}
"We said we'd each have time on our own. I'm usin' mine. She can have hers without me hangin' about outside countin' minutes."
"I did not mean to suggest otherwise."
"I know. I can turn a night out into a council meetin' if nobody stops me. Stop me."
{n}She pushes the empty chair back under the table.{/n}
"No council tonight. Two people, some food, and I find out if you tell the same stories when there's only one person interruptin'."''', c('[Take her hand.] "Then tonight is ours."', "history")),
    n("history", "Anevia", '''"And we don't pretend the bad bits happened to somebody else, neither."
{n}She looks you over, then shrugs.{/n}
"Not askin' you for penance. Just a good night. Don't need it to prove everythin' was always easy."
{n}When you meet later she has found a room with a table too big for it and a window that will not shut. A shallow wooden box sits on the sill. She tells you she means to grow a herb in it, then downgrades the plan at once to keeping a herb alive long enough to learn its name.{/n}
"Laugh. I'm told it's a very patient plant."
{n}You sit together. She puts down the sandpaper and gives you all her attention, which is a lot.{/n}
"So. What's a night that's ours look like, to you?"''',
      c('"Something quiet, where we do not have to fill every pause."', "quiet", flags=("anevia.commander_quiet",)),
      c('"Something ordinary. I like watching you enjoy yourself."', "ordinary", flags=("anevia.commander_company",)),
      c('"Something we have not learned to do. I want a reason to laugh at myself with you."', "ordinary", flags=("anevia.commander_practice",))),
    n("quiet", "Narrator", '''{n}She pulls her chair in until your shoulders touch and leaves the next silence alone. The room has its own small noises: wind at the window, feet on the floor below, the box knocking on the uneven sill.{/n}
{n}After a while you tell her something too small to have mentioned in daylight. She asks about it without trying to fix it. Her answer wanders into a room she once hated, and the one noise that made her fond of it years later.{/n}
"There. Whole story, not a scrap of use in it. You're a terrible influence."
{n}She kisses your cheek and settles against you again.{/n}''', c('[Stay where you are.]', "end")),
    n("ordinary", "Anevia", '''"Then help me work out if that box is crooked or the sill is."
{n}You investigate together. Turning the box changes which corner lifts; sliding it along the sill fixes nothing. Anevia finally wedges a scrap of cloth under one edge and declares victory.{/n}
"Practical knowledge beats architecture. Again."
{n}You ask if she means to put that in her report.{/n}
"Only if I can blame you for the delay."
{n}Afterwards she sits close with her hand on yours in plain sight. You talk about things neither of you will remember properly tomorrow. She loses an argument about a song on purpose, then hums the disputed bit wrong until you are laughing again.{/n}''', c('[Stay close when the argument has become a joke.]', "end")),
    n("end", "Anevia", '''"Another one of these. Soon as we can."
{n}She says it before either of you stands. You pick a day, check it against the promises already sitting on it, and settle on an hour that is nobody's apology and nobody's emergency.{/n}
{n}At the door she kisses you, slow, like she has all the time in the world and means to spend it here.{/n}
"I like you when there's nobody else about. Was gonna put that in writin'. This was better."''',
      c('"Same time next week. I\'ll bring the wine."', flags=("anevia.lover", "anevia.personal_ready"))),
], any_of=("trying", "committed"), forbids=("anevia.personal_ready", "irabeth_dead", "irabeth_gone", "tirabade.group_closed"), delay=0)


s("an_invitation_afterward", "The question she asked separately", [
    n("start", "Anevia", '''{n}Anevia asked you to come after the three of you were done talking about a shared life. She meets you alone, in a room she picked for this.{/n}
"You came. Good. Was tryin' not to make the invitation a test."
{n}She nods at the chair beside hers.{/n}
"Let's say what we're after now. Without pretendin' that last talk never happened, and without lettin' it answer for us."''',
      c('"The three of us is over. I know."', "ended", requires=("trying",)),
      c('"The three of us never started. I know."', "declined", forbids=("trying",)),
      c('[Leave the invitation for another day.]', abort=True)),
    n("ended", "Anevia", '''"We tried the three of us. Then we couldn't keep it. Both of those happened. I ain't sweepin' either one under the rug."
{n}She looks at you straight.{/n}
"And I don't want our nights to be proof the three-way thing's secretly still alive. I want to know if you and me can keep somethin' of our own. On the terms we actually said out loud."
"And Beth?"
"Beth's said her piece. I'm not bringin' you a softer version of it, and I'm not carryin' messages. This is me askin' for me."
{n}She lets that sit, then shifts closer.{/n}''', c('[Hear what Anevia wants for herself.]', "own")),
    n("declined", "Anevia", '''"We never started the life we talked about. Doesn't mean everythin' before it was a game we can forget we played."
{n}She waits until you meet her eyes.{/n}
"There was sneakin'. There were nights I lied to Beth's face and she let me. I ain't callin' any of that harmless 'cause we've found a new door."
"Nor do I."
"Good. Beth knows I asked you here. She told you so herself, with that face she does. If you'd heard it from me you'd've thought I was lyin' again."
{n}She rests her hand on the empty chair beside her.{/n}
"This one's from me."''', c('"Go on, then."', "own")),
    n("own", "Anevia", '''"I want to see you. For a walk. To moan at you about somethin'. To kiss you without the night endin' right after."
{n}Her grin is small and nervous.{/n}
"And Beth and me stay real. We ain't stopped bein' married 'cause a plan for everybody's evenin's fell over. I won't make it sound nicer for you at her cost."
"What would you like to begin with?"
"One night. One we can keep. Picked 'cause we want it, not 'cause it's the least painful thing to do."
{n}She waits. You have a history with her, and none of it answers for you now.{/n}''',
      c('"I want you. Pick the evening."', "date"),
      c('"I care for you. But I can\'t go on with this."', "stop")),
    n("date", "Narrator", '''{n}You pick an evening and stay for part of this one. Anevia tells you about a wooden box she has been forcing to fit a badly made sill. She wants to grow a herb in it and has already collected several rude opinions about her chances.{/n}
{n}She shows you the crooked edge with her hands and argues when you suggest cutting it shorter. Then she stops arguing, takes your face in both hands and kisses you like she has been waiting all evening to shut you up.{/n}
{n}When you leave, the next night has an hour attached to it. She makes you repeat the hour back to her, like a password.{/n}''',
      c('"Oathday, then. Yours."', flags=("anevia.lover", "anevia.personal_ready"))),
    n("stop", "Anevia", '''"Then I'm glad I asked, and didn't just assume."
{n}She takes her hand off the chair and folds it with the other in her lap.{/n}
"It hurts. Don't go fixin' it by sayin' somethin' you don't mean. Give me some room. We'll work out later how to be decent to each other."
{n}You go when she asks. You both know exactly what has ended, and what has not.{/n}''',
      c('"I can\'t keep it, Nevi."', flags=("anevia.closed", "anevia.parted"))),
], requires=("tirabade.group_closed", "tirabade.anevia_continuation_invited"),
   forbids=("anevia.personal_ready", "irabeth_dead", "irabeth_gone"), delay=0)


s("borrowed_signature", "A name used without asking", [
    n("start", "Anevia", '''{n}Anevia is waiting with a woman you have not met. The stranger has a red wool scarf wrapped twice around her neck, though the day is warm. She holds a folded paper by its edges, avoiding the ink.{/n}
"This is Ressa," {n}Anevia says.{/n} "She repairs harnesses. Somebody has decided that makes her a useful source of names."
{n}Ressa hands you the paper. It requests the names and addresses of people renting rooms near a damaged warehouse, together with a payment for an inspection. At the bottom is a mark intended to look official.{/n}
"It isn't ours," {n}Anevia says.{/n} "Not quite. Somebody remembered the shape and got ambitious with the rest."
{n}Ressa keeps watching your hands.{/n}
"My neighbor paid. Then they asked which of the other women lived alone. That was when I stopped believing it was about the roof."
{n}Anevia offers her a chair. Ressa refuses it, then changes her mind before anybody comments.{/n}
"I didn't come here to be the woman who accused half the street. I came because I don't know where the names go."''',
      c('"You\'ve brought one name and one paper. We chase that, not the whole street."', "paper"),
      c('"Who delivered the paper?"', "courier"),
      c('"Let her come back when she\'s ready."', abort=True)),
    n("courier", "Ressa", '''"A woman in a brown coat. She came with a little board to write on. Asked whether my landlord had mentioned the inspection. When I said no, she said landlords always forget the things tenants have to pay for."
{n}Ressa's mouth tightens.{/n}
"I laughed. I knew exactly what she meant. That made her seem more real than the paper did."
"Did she give a name?" {n}Anevia asks.{/n}
"Cale. Perhaps. I didn't write it down."
"Then 'Cale, perhaps' goes down in pencil. What'd she ask next?"
{n}Ressa describes the questions in their order. Anevia lets her talk and keeps her own mouth shut, which visibly costs her. When Ressa contradicts herself about the day, Anevia asks what else happened that morning. The answer fixes the delivery after a broken cart had blocked the street. Ressa was not sure before. She is now.{/n}''', c('[Examine the actual paper.]', "paper")),
    n("paper", "Anevia", '''"We could send a crier round shoutin' that the inspection's fake. Stops some payments. Also tells whoever's behind it we're sniffin'."
{n}Anevia smooths the paper flat on the table.{/n}
"Or we find where the replies go first. There'll be another collection. Nobody asks for addresses if they mean to vanish after one handful of coin."
"My neighbor gave them her sister's name," {n}Ressa says.{/n} "She thought it'd get her roof seen to."
{n}Anevia's face changes.{/n}
"Then the warnin' goes out today. Clever can wait. I ain't leavin' women in the dark so I can have a neater trap."
{n}She asks Ressa who on the street can carry a plain warning and keep her mouth shut about where it came from. Ressa thinks, then nods.{/n}
"Dema. Collects washin'. Everybody talks to her while they're handin' over things they don't want the neighbors seein'."
"Would she help?"
"Ask her. She hates bein' volunteered."''',
      c('"We will ask. Start with the warning and keep Ressa\'s name out of it."', "warning", flags=("anevia.source_protected",)),
      c('"Post the warning under my seal. Nobody needs to know who brought it."', "notice", flags=("anevia.public_warning",))),
    n("warning", "Anevia", '''"Good. Tell Dema straight what it's for. You lie worse than she does, and it'd show."
{n}Ressa looks relieved.{/n}
"She'll ask why you haven't arrested anybody."
"So would I. Haven't found the right anybody yet."
{n}Anevia writes a short account of what is false about the notice, leaving the witness's name out. She reads it aloud, changes a phrase Ressa says the street will get wrong, and folds it without sealing it.{/n}
"She wants more, she knows where I drink."
{n}Ressa takes the warning. Before she goes, she asks to keep a copy of the false paper. Anevia makes one herself, marks it plainly COPY, and tells her to say to anyone collecting money that she has already asked headquarters about it.{/n}''', c('[Send Ressa home with something she can tell her neighbours.]', "alone")),
    n("notice", "Anevia", '''"Then it's about the demand. Not about some brave witness who's got to live next door to whoever we hang."
{n}She writes a plain warning that no such inspection fee exists. You read it over together and strike a sentence that would make everyone who paid sound like a fool. Ressa objects to one more phrase.{/n}
"Don't say bring suspicious strangers here. Somebody'll decide that means the woman two streets over who doesn't say good mornin'."
{n}Anevia crosses it out.{/n}
"Bring the paper. Remember the face. Don't bring me a prisoner. Better?"
{n}Ressa nods. The warning is copied for the neighborhood, and by evening somebody will know the false office has drawn real attention.{/n}
"They'll drop this notice now," {n}Anevia says when Ressa has gone.{/n} "Then they'll move where they collect. Then we find where."''', c('[Discuss what can still be traced.]', "alone")),
    n("alone", "Anevia", '''{n}Anevia turns the false notice over. There is a faint dent on the back, pressed through from something written on a sheet above it.{/n}
"Tomorrow. I know a woman sells paper without askin' where every scrap came from. Sometimes that's kind. Sometimes it's how scum like this get cheap stationery."
{n}She looks at you, then at the door Ressa used.{/n}
"This was meant to be our afternoon. Ressa turned up shakin' and I clean forgot I had one."
"I noticed."
"'Course you did. There's an hour left in it. You want it, or you want to go sulk somewhere dignified?"''',
      c('"I want the afternoon. Put the paper away until tomorrow."', "kept", flags=("anevia.case_evening_kept",)),
      c('"I\'ve got to go. Pick another night now, before either of us forgets."', "rescheduled", flags=("anevia.case_evening_rescheduled",))),
    n("kept", "Narrator", '''{n}She slides the notice under a weight, tells the nearest aide where to find her if Ressa comes back, and waits until you are both outside the working rooms before she takes your hand.{/n}
"There. I'm gonna remember three other things I ought to be doin' before we hit the street. When I do, you remind me I picked this."
{n}You find something to eat and a place to sit. Anevia starts describing the paper seller, catches herself, and asks about your morning instead. You can see what it costs her.{/n}
{n}When you part she kisses you, and does not apologize for enjoying it. The paper waits where she left it.{/n}''', c('"Tomorrow, the paper. Tonight was ours."', flags=("anevia.case_open",))),
    n("rescheduled", "Anevia", '''"Go on, then. Crusade won't run itself. Worse luck."
{n}She picks another time and makes you check it before she writes it down. When you agree, she pins the note where she will see it before she can promise the hour to anyone else.{/n}
"Wanted you to stay. Go, before I start askin' nicely. It ain't pretty."
{n}You kiss her quickly before you go. She keeps hold of your hand a moment longer, then lets go.{/n}
"Tomorrow for the paper. And the night we just picked, for us. Two different promises. Watch me keep both."''', c('"Two promises. I\'ll keep both."', flags=("anevia.case_open",))),
], requires=("anevia.personal_ready", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"))


s("the_paper_seller", "What the impression leaves out", [
    n("start", "Narrator", '''{n}The paper seller occupies the front room of a house whose rear wall has been rebuilt in three different kinds of stone. Shelves hold packets sorted by size. None is quite the same color as its neighbors. A woman with ink on the side of her hand watches Anevia enter and immediately puts away a receipt.{/n}
"That looks guilty," {n}Anevia says.{/n}
"That looks private," {n}the woman replies.{/n} "You can ask which it is before making a habit of my doorway."
{n}Anevia smiles.{/n}
"Tovra. The Commander. We'd like to ask about paper."
"People who want paper generally buy it."
{n}You place the false notice on a clear part of the counter. Tovra looks at the printed mark, then at the edge where the sheet has been cut unevenly.{/n}
"Mine. Or it was. I sold a packet cut from those leaves. It came out of an office somebody was clearing. Half used, half not. I don't ask paper whether it has led a blameless life."
"Do you ask the person selling it?"
"When I think the answer will matter. Apparently I should have thought so."''',
      c('"We want the buyer. Nobody is punishing you for selling scraps."', "customer"),
      c('"There is an impression on the back. May we use the window to examine it?"', "customer"),
      c('[Leave the investigation for another day.]', abort=True)),
    n("customer", "Tovra", '''"Use the window if you like. I can tell you who bought it, too. A woman called Cale. That was the name she gave. She wanted cheap sheets that would look as though they'd passed through several hands. I assumed she was sending invoices nobody intended to pay."
{n}Tovra rubs at the ink on her hand and spreads it a little farther.{/n}
"She paid. She didn't threaten me. She didn't tell me she was collecting the names of women who live alone. I would remember a thing like that."
"I believe you," {n}Anevia says.{/n} "What did you notice that she didn't ask you to notice?"
{n}Tovra considers the question with visible irritation, then answers it.{/n}
"Wet cuffs. Not from rain. We'd had none. And blue marks on two fingers. She told me she'd been carrying a sack of dye for her sister. That may even be true. People occasionally tell the truth when they don't need to."
{n}Anevia turns the paper over.{/n}
"Let's see whether the sheet has anything to add."''', c('[Examine the reverse.]', "method")),
    n("method", "Anevia", '''{n}The impression is easier to see with the paper held sideways to the light. A curved mark crosses two faint lines. Something above them may be a letter, or a crease made by a folded corner.{/n}
"Could be an address," {n}Anevia says.{/n} "Could be somebody's shopping. I'd like to know before we start knocking on doors."
{n}Tovra points to a drawer beneath the counter.{/n}
"I kept a few of the sheets that were written on. For wrapping. You can go through them. It will take time, and I'd like someone to mind the room while I pull the packets apart."
{n}Anevia looks to you.{/n}
"Or you can try the light. Better eyes than mine, some days. If it doesn't give us a whole answer, we can still ask the woman who moves washing through this neighborhood. Blue dye and wet cuffs may mean more to her than an imagined letter."''',
      c('[Perception DC 24] Read the shallow impression, and only what is really there.', check=dict(Skill="SkillPerception", DC=24, Success="read", Failure="blurred", CommanderOnly=True)),
      c('[Help Tovra sort the used sheets and mind her shop while she searches.]', "sorted"),
      c('[Keep the uncertain paper and ask Dema about the practical details.]', "uncertain")),
    n("read", "Narrator", '''{n}You turn the sheet until the curve resolves into the lower loop of a written figure. The first apparent letter is a crease. Beneath it, the words "blue cistern, second bell" cross the impression of a narrow receipt line.{/n}
{n}Anevia repeats the words exactly, without adding a name to them. Tovra asks to look. She recognizes the ruled line as one used in packets sold to the dye yard near an old cistern.{/n}
"Not proof she works there," {n}Tovra says.{/n} "People can write directions to a place they don't own."
"Useful distinction," {n}Anevia replies.{/n} "We'll keep it."
{n}You have a meeting place and an approximate time. It does not say who will be there, and half the district has blue dye under its nails.{/n}''',
      c('[Record the actual place and time.]', "cost", flags=("anevia.trace_read", "anevia.trace_cistern"))),
    n("blurred", "Narrator", '''{n}The angle changes the mark, but does not make it reliable. You think you can see a name until a slight movement turns the first letter into the edge of a receipt line. Anevia watches your expression, then lowers the paper.{/n}
"Leave it. I ain't kickin' in a door on a smudge."
{n}Tovra shrugs, as if smudges were a common complaint in her trade.{/n}
"Dema uses the dye yard when she has cloth that needs more than washing. If somebody is carrying wet bundles around, she might know where they began."
{n}Anevia folds the notice along its existing crease.{/n}
"Then we ask Dema. Paper's said all it's gonna."''',
      c('[Write down that you couldn\'t read it.]', "cost", flags=("anevia.trace_failed",))),
    n("sorted", "Narrator", '''{n}You spend the next hour learning how many shades of almost-white paper can occupy a small shop. Anevia minds the front room while you and Tovra separate packets. Twice she calls you to identify a size a customer has described entirely by hand gestures. The second customer buys the wrong one anyway and blames the weather.{/n}
{n}At the bottom of a tied bundle, Tovra finds a receipt for a packet delivered to the dye yard. Part of its line matches the impression on the false notice. There is no time written on it, and nothing that names Cale as the owner of the yard.{/n}
"The same stack," {n}Tovra says.{/n} "Not necessarily the same person."
{n}Anevia writes down the distinction. The work has given you a place to begin, at the cost of an hour during which the next collection may have moved. It has also left Tovra with half her stock spread across the table.{/n}''',
      c('[Help her put the packets back. Keep the one sheet that matters.]', "cost", flags=("anevia.trace_sorted", "anevia.trace_cistern"))),
    n("uncertain", "Anevia", '''"A crease is a crease."
{n}She puts the paper away, careful not to make another mark on the back.{/n}
"Let's go ask somebody with a mouth."
{n}Tovra gives you directions to Dema's collection place. She also tells you which woman at the dye yard will answer a question directly and which will insist on telling you the history of the whole street first.{/n}
"Either may know something useful," {n}she adds.{/n} "I am merely warning you about the time."
{n}Anevia thanks her. This approach leaves the impression unread and the meeting time unknown. It gets you Dema's name instead, and Tovra's word that Dema will talk.{/n}''',
      c('[Take Tovra\'s name for Dema and go.]', "cost", flags=("anevia.trace_asked",))),
    n("cost", "Tovra", '''"You gonna put my name on the warnin'?"
{n}Tovra asks it with her back to you, squaring packets that are already square.{/n}
"People will hear the paper came from here. I'd like 'em to hear I helped. I'd also like 'em not to put a brick through my window before they work out which way round it was."
{n}Anevia rests her hand on the counter.{/n}
"I can say the seller cooperated. I won't hand out your address as the place to bring everybody's temper. Can't promise nobody'll know the paper, though."
"No. You can't."
{n}Tovra takes the false notice and looks at the mark one more time before handing it back.{/n}
"Then stop whoever's usin' my stock to look respectable. My honest customers are trouble enough."''',
      c('"Your name stays off the notice. Nobody pins this on your shop."', "outside"),
      c('"Anyone threatens you, send word the same day. Don\'t wait for it to get worse."', "outside")),
    n("outside", "Anevia", '''{n}Outside, Anevia takes your arm for a few steps and lets go when the passage narrows.{/n}
"Blue dye, wet cuffs, and a name that's probably false. I've seen folk hanged on less. I've been wrong on less, too."
{n}She looks back at the shop.{/n}
"Tovra'll have a brick through that window inside a month if we're sloppy. Send a lad to sit on her step tonight. Tell him it's for the view."
"Done."
"Good. Now I owe her, and she knows it. Best kind of friend."
{n}She checks the sun and turns toward the street where Dema collects the washing.{/n}
"Come on. Somebody to ask, and I'm told she bites if you volunteer her. Think I'm gonna like her."''',
      c('"Then we go where the paper points."', flags=("anevia.paper_examined",))),
], requires=("anevia.case_open", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"))


s("the_woman_with_the_basket", "What Dema chooses to carry", [
    n("start", "Narrator", '''{n}Dema's collection place is a shed with a roof that leaks at one corner. She has dealt with the leak by moving a tub beneath it and hanging an emphatic notice above the dry baskets. Nothing on the notice invites a customer to comment on the arrangement.{/n}
{n}Dema herself is an adult woman with rolled sleeves and a streak of blue beneath one thumbnail. She looks from Anevia to you, then sets down the bundle she was tying.{/n}
"Ressa said you'd come. She said you'd be polite about it. I've got three tubs soaking, so skip that part."
"Done," {n}Anevia says.{/n}
{n}Anevia describes the false notices. Dema listens, asks to see the paper and points to the mark at the bottom.{/n}
"I've seen a woman carrying those. Cale. That name at least is hers. She's been using the old counting room by the dye yard. I thought she was collecting rents. Several people have been doing that since the original owners stopped coming."''',
      c('[Describe the exact meeting place and time read from the impression.]', "time", requires=("anevia.trace_read",)),
      c('[Tell her it points at the dye yard, and that\'s all you know.]', "place", requires=("anevia.trace_sorted",)),
      c('[Describe the wet cuffs and ask how she knows Cale.]', "work", forbids=("anevia.trace_read", "anevia.trace_sorted")),
      c('[Arrange to continue when Dema is willing.]', abort=True)),
    n("time", "Dema", '''"Second bell. That would be when she comes for the bundles."
{n}Dema points toward the yard beyond the shed.{/n}
"She puts her papers in a covered basket so they stay dry. Looks like washing unless you lift the cloth. I did once. There was a list of names underneath. She told me they belonged to people who owed her employer money."
"Did you believe her?" {n}Anevia asks.{/n}
"Enough to put the cloth back. Not enough to forget the list."
{n}Dema looks at the paper again.{/n}
"If you know the time, you could wait without me. She might change it if she sees soldiers. She won't change it just because I have washing to carry."''', c('[Ask if she wants in.]', "choice")),
    n("place", "Dema", '''"The counting room, then. I know which door. I don't know when she'll be there next. She comes at different times when she thinks somebody is paying attention."
{n}Dema picks a thread off her sleeve.{/n}
"There was a bundle due today. If you've spent the morning looking through paper, she may have collected it already. That doesn't mean she won't return. It means you'll have to wait, or ask somebody who is already there."
"You?" {n}Anevia asks.{/n}
"Perhaps. I haven't offered yet."
{n}Anevia nods once and lets it go.{/n}''', c('[Ask how far she\'ll go.]', "choice")),
    n("work", "Dema", '''"She pays me to carry cloth. Some of it has dye in it, some of it smells as though it ought to. She has a basket she doesn't want washed. I found papers beneath its cover once."
{n}Dema glances toward a shelf of folded sheets.{/n}
"I didn't steal them. I put the cloth back. I had washing to deliver and no reason yet to be a hero."
"It doesn't," {n}Anevia says.{/n} "What did you read?"
"Names. Not enough to make a list for you. Enough that I remembered Ressa's street when she told me what happened."
{n}Dema considers the door.{/n}
"I could carry the next bundle and see whether the basket is still there. I could also tell you to stand outside until Cale comes out. The second option would give me a quieter evening."
"Tell me the quiet one first," {n}Anevia says.{/n}''', c('"Tell us what you\'ll do, and what you won\'t."', "choice")),
    n("choice", "Dema", '''"If I help, I want to know what happens when she notices. I work here. I can't run back to headquarters and get a man on my door."
{n}Anevia takes a slow breath before answering.{/n}
"You tell us if the basket's there, and you leave. You don't take it, you don't keep her talkin'. She asks why you came, you're deliverin' the washin' you were gonna deliver anyway. We watch the door. Not you playin' spy."
"And after?"
"You ain't in the public account. Ressa keeps the warnin' movin'. Cale threatens you, we come down on her like a wall. Can't swear she won't guess somebody talked."
{n}Dema studies her.{/n}
"You're a terrible liar, for a spy."
"I save it for people I don't like."
{n}She picks up the waiting bundle and sets it down again.{/n}
"I'll tell you if the basket's there. I won't wear a signal, and I won't go back a second time because the first answer wasn't enough. Need more than that, pick the other plan."''',
      c('"One delivery, then she walks away. That\'s enough."', "help", flags=("anevia.dema_helped",)),
      c('"We watch the door ourselves. She\'s done enough."', "watch", flags=("anevia.dema_spared",))),
    n("help", "Narrator", '''{n}Dema goes about the delivery with an air of irritation that needs no rehearsal. Anevia keeps you at the corner rather than close to the counting-room door. You can see the entrance and a narrow side passage. Neither view reveals what happens inside.{/n}
{n}When Dema returns, she does not stop beside you. She passes, sets down her empty basket at the shed and waits until Anevia comes to her.{/n}
"Basket on the stool. Blue cloth over it. Cale and another woman inside. The other one said they should finish collecting before more people hear about the warning."
{n}Anevia asks whether Dema saw a weapon. She says no, then corrects herself: she saw none; that is not the same thing.{/n}
"Go on, then. That's all you're getting."
{n}Anevia thanks her once. Dema goes back to her washing and does not look up again.{/n}''',
      c('[Go in knowing there are two of them and a basket.]', "approach", flags=("anevia.basket_located",))),
    n("watch", "Narrator", '''{n}You and Anevia wait where you can see the entrance. A woman carries a basket into the counting room, but the angle gives you no view beneath its cover. Dema does not approach the building again.{/n}
{n}The wait gives the occupants time to move things. Once Anevia points to a thin drift of smoke from a side window. Someone has lit a brazier inside. It may be for warmth or dye work. It may not.{/n}
"We know enough to question the false collection," {n}she says.{/n} "If we wait for the room to explain itself from here, we may lose the papers."
{n}Dema stays at her tubs. You go in not knowing what is on the other side of the door.{/n}''',
      c('[Go in with the false notice in your hand.]', "approach", flags=("anevia.basket_unconfirmed",))),
    n("approach", "Anevia", '''{n}Anevia stops you before you turn into the passage.{/n}
"I want the names back. I want to know who was buyin'. If I start chasin' the buyer while somebody's burnin' the names, grab my collar."
"What will you do?"
"Talk. Look where they don't want me lookin'. Try not to get so clever I forget there's a back door."
{n}She squints at you.{/n}
"Side door's on the left. Anybody bolts, it's through there, and I can't run in these boots."
{n}She squeezes your hand once, hard, and lets it go.{/n}
"Right. I knock first. It confuses people."''',
      c('"Names first. Then the buyer."', flags=("anevia.dema_terms_kept",))),
], requires=("anevia.paper_examined", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"), delay=0)


s("the_counting_room", "The names and the person leaving", [
    n("start", "Narrator", '''{n}The counting-room door is unlatched. Anevia knocks anyway. A woman inside answers sharply, and you enter before she can decide whether to withdraw the invitation.{/n}
{n}Cale stands beside a desk with a cloth-covered basket at her feet. Another woman is fastening a narrow case. A small brazier smolders beneath the window. There is no obvious weapon in either woman's hand.{/n}
"We are here about the inspection notices," {n}Anevia says.{/n}
"Then you want the office," {n}Cale replies.{/n}
"This one will do."
{n}Anevia places the false inspection notice on the desk. Cale recognizes it before she remembers to look puzzled.{/n}
"The fee is for a private assessment. Nobody said it came from headquarters."
"Then you'll have no difficulty explaining why your mark imitates ours. Or why a roof inspection needs to know which women live alone."
{n}The woman with the case stops fastening it. Her attention shifts to the side door.{/n}''',
      c('[Keep the woman with the case in view while Anevia questions Cale.]', "account"),
      c('[Ask Cale to put the basket on the desk.]', "basket"),
      c('[Back off. Come back later.]', abort=True)),
    n("basket", "Anevia", '''"The covered one. You know which."
{n}Cale hesitates, then lifts it by the handle. A corner of paper shows beneath the cloth. The woman with the case looks at it once, too quickly, then returns her attention to the door.{/n}
"Customer records," {n}Cale says.{/n}
"Good. Then your customers can have 'em back once we find out what they signed and why."
{n}Anevia does not reach across Cale to uncover the basket. She moves instead, putting herself where she can see both its contents and the brazier.{/n}
"Who is your colleague?"
"A buyer."
"Of roof assessments?"
{n}Nobody answers that question immediately.{/n}''', c('"Talk, Cale."', "account")),
    n("account", "Cale", '''"People sell information. Your friend knows that."
{n}She looks at Anevia rather than you when she says it.{/n}
"Names of people looking for work. Empty rooms. Who has a relative outside the city. There are merchants who pay for that. Not everything you don't like is a cult."
"Oh, I've sold information," {n}Anevia says.{/n} "Never had to pretend I was repairing somebody's roof."
{n}Her smile has gone flat.{/n}
"Call it trade again. Go on. Then tell me which of those women put her own name on your list."
{n}The buyer lifts the case from the table.{/n}
"I came to examine a list. I have made no purchase. If she obtained it improperly, that is between her and the people who supplied it."
"Put the case down," {n}you say.{/n}
{n}She hesitates. Cale seizes the basket handle.{/n}
"You don't know what I paid for those names," {n}Cale says.{/n} "You can't just take them."
{n}Anevia sees the movement toward the brazier as Cale swings the basket toward it. She catches its rim, but the cloth comes away in Cale's hand. Loose sheets scatter toward the heat. At the same moment the buyer steps through the side doorway.{/n}
"Papers or door," {n}Anevia says. There is no time to discuss both.{/n}''',
      c('[Help Anevia save the names and receipts before they burn.]', "papers", flags=("anevia.saved_papers",)),
      c('[Stop the buyer while Anevia deals with Cale and the brazier.]', "buyer", flags=("anevia.stopped_buyer",))),
    n("papers", "Narrator", '''{n}You pull the falling sheets away from the brazier while Anevia pushes the basket flat against the desk, trapping Cale's hand beneath its rim until she lets go. A corner of one receipt blackens. The lists themselves stay clear of the coals.{/n}
{n}The buyer is gone through the side passage. You hear a door strike a wall somewhere beyond it, then the confused protests of a person whose way she has blocked. Anevia looks after the sound but remains beside the papers.{/n}
"Let her go. We know where these names are now."
{n}Cale begins explaining that she would never have burned them. Anevia places the scorched receipt in front of her.{/n}
"Then you should be relieved."
{n}You secure the records and keep Cale in the room until help arrives. The buyer's identity remains an open question. The women whose names fill the lists will not have to wait for that question to be solved before hearing what was taken.{/n}''', c('[Write it down straight: what you saved, and who got away.]', "limits", flags=("anevia.records_intact",))),
    n("buyer", "Narrator", '''{n}You reach the side doorway before the buyer can close it. She stops when she sees that leaving now will require more than a brisk explanation. You direct her back into the room and keep the passage behind you.{/n}
{n}Anevia has Cale against the desk, one hand held clear of the brazier. With the other she drags the basket away from the coals. Smoke rises from several loose sheets before she can reach them.{/n}
"Names survived," {n}she says.{/n} "Some receipts didn't."
{n}The buyer sets her case down. Inside are several packets of ordinary commercial papers, a purse and two letters of introduction. None establishes a demonic conspiracy. One establishes that she has bought address lists in another district.{/n}
"Helve," {n}Anevia reads.{/n} "Then we can stop calling you a customer."
{n}Helve asks whether she is being accused of purchasing this list. Anevia looks at the unsigned receipt, then at the papers damaged by the fire.{/n}
"You are being asked what you came to buy. We will not improve the evidence to make the answer easier."''', c('[Keep the buyer for questioning and record the damaged receipts.]', "limits", flags=("anevia.records_partial",))),
    n("limits", "Anevia", '''{n}Once the immediate danger is past, Anevia uncovers the lists one page at a time. She finds Ressa's street, then the neighbor's sister. She does not read the names aloud for everybody in the room.{/n}
"Who else has copies?"
{n}Cale looks at the door, then at the brazier, as though considering which answer might have been available a minute earlier.{/n}
"I sent a sample. Five names. No addresses."
"To whom?"
"I don't know the woman's name. She left a place to send it."
{n}Anevia asks for the address and writes it separately from the recovered list.{/n}
"Then there's five names still out there, and we're goin' after 'em."
{n}There is anger in her voice now, less theatrical than Cale seems to expect.{/n}
"You had women asking their neighbors for private details because they thought a roof might be made safe. That's the part I keep coming back to. You used them to do the collecting for you."
"You use informants."
"Mine know who they're talkin' to, and they get paid. You had grandmothers doin' your legwork for the price of a roof."''',
      c('"Post the truth: it was a swindle, and we didn\'t get all of it back."', "record"),
      c('"Tell the people on the list first. Nobody should hear their own name read out in the square."', "record")),
    n("record", "Narrator", '''{n}Cale is taken off for ordinary questioning about the false collection. The recovered papers go into a sealed packet marked with the case, not the witnesses. Anevia keeps a separate list of the people who need warning and asks for the messages to go by hand, privately.{/n}
{n}The counting room is quieter once the others are gone. The brazier still stinks of scorched paper. Anevia opens the window and stands with her hands on the sill.{/n}
"Stinks. I'll smell burnt paper for a week."
"Was it the right door?"
"Ask me when I've slept. Right now I'd hang Cale out that window and call it justice, so I'm the wrong one to ask."
{n}She turns to you.{/n}
"Come find me in a day or two. Bring wine. I'll have the sums by then, and I'll be in a mood."''',
      c('"Tell me later. Breathe first."', flags=("anevia.counting_room_settled",))),
], requires=("anevia.dema_terms_kept", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"), delay=0)


s("what_the_warning_cost", "After the names were returned", [
    n("start", "Anevia", '''{n}Anevia brings a letter to the borrowed room and holds it up before she puts it down.{/n}
"Ressa. Said I could read you the bit about her. Not the names of who came knockin'."
{n}You nod. Anevia unfolds the sheet.{/n}
"Warnin' got to her neighbor before anybody came back for more coin. Neighbor's furious she fell for it. Ressa told her it was made to be fallen for. They had a row about that, then went off together to tell the sister."
{n}Anevia folds the bottom of the page under her thumb so the private names stay hidden.{/n}
"Dema's still workin'. Cale knows somebody squealed, don't know who. Won't stay that way forever. But we didn't hang a lantern on her for the sake of a tidy story."
{n}She puts the letter down.{/n}
"Then there's the money."''',
      c('[Hear what the intact receipts made possible.]', "receipts", requires=("anevia.records_intact",)),
      c('[Hear what could be established after some receipts burned.]', "burned", requires=("anevia.records_partial",)),
      c('[Leave the conversation for another evening.]', abort=True)),
    n("receipts", "Anevia", '''"Most of the receipts made it. We can match amounts to names and hand back what was left in Cale's box. Not all of it. Some was already spent."
{n}She taps the edge of the letter.{/n}
"But we know who's still owed. Better than tellin' folk to prove they paid while the only proof's a pile of ash."
"And the buyer?"
"Descriptions. An address for the sample. And nobody handy to hang for the whole lot. Hate losin' her. Loved knowin' exactly where Ressa's neighbor's name was when we walked out. Both at once."
{n}She looks at you steadily.{/n}
"I wanted to chase. You saw it. You kept your hands on what we came for. Thanks."''', c('"Would you choose the papers again?"', "papers_answer")),
    n("papers_answer", "Anevia", '''"Yeah. Ask me tomorrow, after somebody's brought me another useless description of the buyer, and I'll swear first. Still yes."
{n}She grins briefly and does not pretend the itch has gone.{/n}
"I've seen agents go that way. Chasin' a secret so long they forget who they wanted it for. Everybody claps 'em on the back right up till somebody else pays the bill."
{n}She picks the letter up again and folds it along the worn crease.{/n}
"Ressa didn't ask for a grand investigation. She asked where the names went. We found most of 'em. The rest I'm gonna find, and then I'm gonna be unbearable about it."''', c('[Ask what remains for Dema.]', "dema")),
    n("burned", "Anevia", '''"Some amounts we can match. Some we can't. We've got people who remember payin' and no receipt sayin' how much. Cale's gone very vague about sums."
{n}Her mouth tightens.{/n}
"Helve's papers gave us another district. Found a woman there with the same letter. Hadn't answered yet. That counts."
"And the money here?"
"What's left gets split against the claims we can prove. Rest'll need witnesses, and some folk'll wait longer 'cause the receipts burned. That ain't a detail. That's somebody's rent."
{n}She puts both hands flat on the table.{/n}
"Wanted those receipts. Still do. But you caught a slippery sod, and I'm gonna find out what she knows before I start yellin' at you."''',
      c('"I would still stop her. Warning another district mattered."', "defend"),
      c('"I would choose the papers if we faced it again."', "reconsider")),
    n("defend", "Anevia", '''"I'd have gone for the papers. And Helve's sittin' in a cell eatin' our bread, and she's the only one of the lot who's talked, so now I've got to be grateful to you. Hate it."
{n}She leans back and props her boots on the other chair.{/n}
"Next time I grab the papers and you grab the door. We get both, and I get to be smug."''', c('"We disagree. Pour me another."', "dema")),
    n("reconsider", "Anevia", '''"Then remember it. Just don't turn it into a hair shirt you pull on every time the case comes up."
{n}She reaches across and touches your fingers.{/n}
"I made calls too. Could've shut up sooner. Could've kicked that brazier over before Cale got to it. I've got a whole list of ways that room could've gone smoother if I'd known the endin'."
"A long list?"
"Magnificent list. Everybody does exactly what I want. Nothin' like real people."
{n}She squeezes your hand once and lets go.{/n}
"Anyway. Twelve claims with no receipt behind 'em. You're good with angry widows, apparently. You're takin' four."''', c('[Ask what remains for Dema.]', "dema")),
    n("dema", "Anevia", '''"Dema sent word. Her shed roof leaks, and since I owe her, I'm fixin' it."
{n}Anevia looks amused and faintly alarmed.{/n}
"I've never fixed a roof in my life. Beth has. I'm gonna volunteer Beth and see how she likes bein' volunteered."
"Did you have more questions for Dema?"
"Six. Didn't ask one. Next thing she carries for me, I'm payin' for, and she knows it."
{n}Anevia folds Ressa's letter carefully.{/n}
{n}She puts the letter away rather than making it the evening's next job.{/n}
"There. That's the report. Now tell me somethin' that ain't about the case, before I start again."''',
      c('"I enjoyed watching you do work you cared about. I also missed having you to myself."', "missed"),
      c('"I\'m glad you came and argued it out with me after."', "trusted")),
    n("missed", "Anevia", '''"Good. Hopin' you'd get to the second bit before I had to start bein' unbearably charmin'."
{n}She gets up, comes round the table and holds out her hand.{/n}
"There's a whole room here not bein' used by that letter. Let's go sit in some of it."
{n}You follow her to the wide chair by the window. She drops into it, pulls you down half on top of her and kisses you before either of you can find another practical subject.{/n}
"There. Missed that too."
{n}She waits for your answer and grins when you give it with another kiss. For a while the only unfinished business she cares about is the gap between you, and she closes it.{/n}''', c('[Stay. Let the letter keep.]', "end")),
    n("trusted", "Anevia", '''"'Course I did. Who else am I gonna argue with? Beth agrees with me when she's tired, and that's no sport at all."
{n}She drags her chair round the corner of the table so she can sit nearer.{/n}
"Besides, you had the right of it about Helve. Once. Don't let it go to your head."
"I might not."
"Then I'll enjoy the company and ignore you. Solid foundation for romance, that."
{n}She kisses your cheek, then the corner of your mouth, plainly enjoying how hard she is making it for you to answer.{/n}
"Come here. I'm done bein' professionally interestin' for tonight."''', c('[Accept the invitation.]', "end")),
    n("end", "Narrator", '''{n}The lamp burns lower while you talk. Anevia has planted the cutting in the box by the window. When you ask about it, she tells you the market woman sent soil as well, having no faith at all in anything dug out of a military yard.{/n}
{n}The plant has put out one new leaf. Anevia points at it with pride out of all proportion to its size, then laughs when she sees you noticing. You ask if it is going in a report.{/n}
"No. This one's mine."
{n}She leans back against you when she says it. Out in the city the case is still making trouble for people. On the sill, the leaf is doing fine.{/n}''',
      c('[Kiss her goodnight.]', flags=("anevia.case_consequence_kept",))),
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
"Good," {n}she says, crossing it out.{/n} "We have learned something at very little cost to the goats."''', c('[Restore the old rule and offer another game.]', "deciding")),
    n("deciding", "Anevia", '''"In a minute."
{n}She stands the crooked goat up by the lamp.{/n}
"Told Beth about last week. How you lost at cards and didn't explain why it didn't count. She said you sounded unnatural. Then she laughed for a good minute, which she don't do for just anybody."
{n}Her finger stays on the little wooden goat.{/n}
"What else did I do?"
"Watched me bein' ridiculous about a goat and didn't look like you wanted me to stop."
{n}She glances up, grinning.{/n}
"There's a list. Not showin' you. You'd get a big head."''',
      c('"I remember the way you look pleased before you decide what to say about it."', "seen"),
      c('"I like that you can tell me I\'m wrong and still want me here."', "different"),
      c('"I want you tonight. If you want me."', "desire")),
    n("seen", "Anevia", '''"Then I'll have to stop bein' so predictable."
{n}The threat is ruined by her face. She comes round the table, drops into the chair beside you and looks at the board from your side.{/n}
"You saw that move comin' the whole time."
"Yes."
"And sat there lookin' fond. Disgraceful."
{n}She turns toward you, close enough that the teasing goes quiet without stopping.{/n}
"Nobody catches me when I ain't picked my best angle. You keep doin' it. It's very rude."
{n}Her palm rests against your cheek, warm, in no hurry to leave.{/n}''', c('"What do you want tonight?"', "desire")),
    n("different", "Anevia", '''"You'd be bored stiff with somebody who agreed with you. I'd be bored tryin'."
{n}She comes round the table and sits next to you.{/n}
"Caught myself savin' up arguments 'cause I thought you'd enjoy 'em. Either that's love or it's a very long con."
"Does it have to be one?"
"No. That's one of the things I like about you."
{n}She leans into you, shifting until her shoulder finds a comfortable place.{/n}
"So surprise me. I've got a whole evenin' and a board full of goats."''', c('"Then what are we doing tonight?"', "desire")),
    n("desire", "Anevia", '''{n}Anevia pushes her chair back and reaches for you. You come to her beside the table. Her hand hooks round the back of your neck and stays there.{/n}
"Made the bed this mornin'. First time in a week. Spent the whole day tellin' myself it was for the look of the place."
{n}She grins, and under the grin her pulse is going like a rabbit's where your fingers rest on her wrist.{/n}
"It wasn't. Settin' up this room was easy. Waitin' for you to walk through that door nearly killed me."
{n}You kiss her. She answers hard and eager, pulling you in until the chair is in the way of everything either of you wants. When you break for breath she keeps her forehead against yours and laughs, low.{/n}
"The goats can see us. Say somethin' before I shock 'em."''',
      c('[Stay the night.]', "night"),
      c('[Stay a while, then go. You promised someone else the night.]', "leave"),
      c('[Ask to just sleep beside her.]', "sleep")),
    n("night", "Narrator", '''{n}She puts the little pieces into their parcel without caring which way they face. The crooked goat remains beside the lamp until she notices it watching, laughs and turns it toward the wall.{/n}
{n}Then her attention is wholly yours. She kisses you at the edge of the bed, lingering when your hand finds her waist. There is a buckle she cannot undo while you keep making her laugh. She catches your wrist, presses a kiss to your knuckles and asks you to be helpful for once.{/n}
{n}You are helpful. The buckle gives, and the belt, and she steps out of the rest herself, quick and unembarrassed, like a woman shedding a disguise she has worn too long. "Your turn," she says, and does not wait for you to manage it; she has your shirt over your head before you can make a joke of it.{/n}
"There," {n}she murmurs against your mouth.{/n} "That's what I'd like."
{n}She pulls you down onto the bed after her by a fistful of whatever you are still wearing, laughing once, low, and then not laughing at all. Her knee draws up along your hip; her hand spreads flat between your shoulders and holds you there, exactly where she wants you.{/n}
{n}In the morning Anevia wakes with one arm across you and a complaint about the window already forming. She abandons it when you turn toward her. For a while neither of you gets up to discover whether the complaint was justified.{/n}''',
      c('[Stay for breakfast.]', "morning", flags=("anevia.private_night",))),
    n("sleep", "Anevia", '''"I'd like that. I'm very quiet once somebody's shut me up."
{n}She puts the game away, digs out another blanket and asks which side of the bed you want. The plain little questions make her smile; she had clearly imagined needing something much grander to say.{/n}
{n}You settle together while the room cools. Anevia tells you one last thing, then another, then apologizes into your shoulder for having lied about her talent for silence. You laugh, and she finally goes still.{/n}
{n}In the morning she wakes first and lies there enjoying having nowhere to be. When you open your eyes she is watching the light on the ceiling, not the door.{/n}
"Could get used to this. Not every mornin'. Enough to miss it when I don't get it."''',
      c('[Stay for breakfast.]', "morning", flags=("anevia.quiet_night",))),
    n("leave", "Anevia", '''"Then go keep it. Somebody's waitin'. I know the feelin'."
{n}She kisses you again, and takes her time about it. At the door she straightens a fold in your collar, notices she is doing it and snorts at herself.{/n}
"Look at me. Domesticated. Don't you dare put that in a report."
{n}You pick another night before you go. Afterwards she packs the game away and leaves the crooked goat by the lamp. She taps it on the head before she blows the lamp out.{/n}''',
      c('[Kiss her goodbye and promise the next night.]', flags=("anevia.ordinary_life_kept",))),
    n("morning", "Anevia", '''"We should eat before I start findin' reasons not to leave."
{n}She gets up, comes back to kiss you, gets up again with more conviction. There is bread, a heel of cheese and what fruit survived your appetites. She hands it round and steals the best of the cheese.{/n}
"I've got work. You've got work. And I've got a night at home with Beth I mean to keep."
{n}She takes your hand across the table.{/n}
"And I want another one here. All of it at once. Greedy woman, you knew that."
{n}You settle on the next visit. She goes off pleased, the folded game under her arm, the crooked goat still standing by your lamp.{/n}''',
      c('"Fireday? If Beth hasn\'t got it."', flags=("anevia.ordinary_life_kept",))),
], requires=("anevia.case_consequence_kept", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"), delay=48)


s("departure_note", "The part of the page she left blank", [
    n("start", "Anevia", '''{n}Anevia has folded a sheet of paper small enough to fit in a belt pouch. She hands it over without ceremony, then scowls when the fold springs open before you can put it away.{/n}
"Was meant to look more dignified than that."
{n}A few lines in her hand. Nothing about the road, no warning dressed up as a goodbye. She has written that she liked the last night you spent together, and named one small thing that made her laugh.{/n}
"Left the bottom empty," {n}she says.{/n} "Case you think of somethin' you'd have told me if I'd been there. Doesn't have to be clever."
{n}Her fingers stay on the edge a moment before she lets go.{/n}
"And don't go promisin' letters you can't send. I'll wait for 'em like an idiot. I know me."''',
      c('"What will you do while I am gone?"', "days"),
      c('"I\'m afraid of what months without a word will do to us."', "fear"),
      c('[Leave the farewell for a day when you can finish it.]', abort=True)),
    n("days", "Anevia", '''"Work. Moan about work. Find somebody who'll let me ruin a loaf without chargin' me for the flour."
{n}She grins, then sobers.{/n}
"Nights at home with Beth. Think of somethin' to say to you and be furious I can't. Go places you've never been with me, so I've got stories for when you're back. I ain't sittin' in a window like a widow in a ballad."
"I would like to hear them."
"Good. So come back to a woman who kept livin', not a room with dust sheets on it. And if you come back changed, fine. I'll complain. I'll still want you."
{n}She touches your cheek, rough-fingered and quick.{/n}''', c('[Tell her something you will want to ask when you return.]', "end")),
    n("fear", "Anevia", '''"So am I. Bloody terrified. There. Both said it."
{n}She looks at the folded page in your hand.{/n}
"I won't be brave pretty. I'll bite some poor runner's head off for knockin' at the wrong minute. Say sorry after. Probably be cross about sayin' sorry."
"That sounds like you."
"Let's hope I don't turn into a saint while you're off. You'd never recognize me."
{n}The joke cracks down the middle. She takes a breath and lets you see her do it.{/n}
"Keep the paper. It ain't a bill. I gave it you 'cause I can't come along."''', c('[Keep her gift and stay close.]', "end")),
    n("end", "Narrator", '''{n}She holds you hard, knowing it will not be enough. You stay like that until one of you has to move, then kiss once more at the door. Anevia does not fill the last quiet with instructions, which for her is a small miracle.{/n}
"Come back if you can," {n}she says.{/n} "I want to argue with you about somethin' stupid again."
{n}You put the page where you will find it. It weighs nothing, until you remember why you are carrying it.{/n}''',
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
    n("changed", "Narrator", '''{n}You write that you are afraid she will have got used to your absence. It takes three tries. The first sounds like a report, the second like a sulk, and the third you cannot read back without wincing, so you leave it.{/n}
{n}Under it you write about the Abyss instead: the heat, the colour of the sky, a demon that tried to sell your party a hat. It is easier than the other thing. Then you go back to the other thing and write one more line of it.{/n}
{n}The page ends up blotted and crooked, and more like something she would recognize.{/n}
{n}You finish by asking what she has wanted that you do not know about yet.{/n}''',
      c('[Keep the fear and the plainer answer together.]', flags=("anevia.absence_account", "anevia.absence_changed"))),
    n("memory", "Narrator", '''{n}You fold the page without writing. There are things you want to tell her that will not settle into a useful order tonight. You try the opening aloud, dislike it, and stop.{/n}
{n}You think of her making an ordinary plan in Drezen. Not waiting at a window, not saying something brave for an audience you have invented. Perhaps she is losing a game, or arguing about a wet cloak, or burning something she had intended to eat.{/n}
{n}You would like to hear which of those guesses is wrong. You would like to tell her what it was like to make them here.{/n}
{n}You tuck the page back into its fold. It can wait until you have something worth telling her.{/n}''',
      c('[Keep the page. Tell her in person if you return.]', flags=("anevia.absence_account", "anevia.absence_unwritten"))),
], requires=("anevia.departed_together", "anevia.lover"), chapters=(4,), remote=True, delay=0)


s("the_life_she_lived", "The answer you could not guess", [
    n("start", "Anevia", '''{n}Anevia has moved the little plant into a bigger pot. The wooden box now holds scraps of paper, a needle case and a key she says opens nothing she currently owns.{/n}
"Kept it 'cause I liked the shape. That's allowed. I checked."
{n}She clears a place beside it for your things and sits close enough that you can reach her hand without anyone making a ceremony of it.{/n}
"Been thinkin'. I can give you a lovely report of my week and leave out every bit that mattered. You might've noticed. It's a professional skill."
{n}She raises an eyebrow, daring you to say you had.{/n}
"Not tonight. Tonight you get the bits I'd cut."''',
      c('"There are days we missed. I want to hear about yours."', "absence", requires=("anevia.departed_together",)),
      c('"Tell me about a day I missed. Not the evenings. The rest."', "new_days", forbids=("anevia.departed_together",)),
      c('[Ask to keep this conversation for another day.]', abort=True)),
    n("absence", "Anevia", '''"Some were awful. The plain ones were worse."
{n}She pulls her feet up under her on the chair.{/n}
"Went to market with Beth. Fought about whether we needed another blanket. Bought one, got home, found she'd already ordered one. Very well-blanketed evenin', spent bein' cross with each other."
{n}The memory makes her smile before the other thing comes back into her face.{/n}
"Another day I nearly bit a runner's head off. She'd brought exactly what I asked for. I was livid 'cause it wasn't news of you. Had to go find her after and say whose fault that was."
"Yours?"
"Mine. Didn't make me miss you less. Did stop me chuckin' it at people."
{n}She reaches for your hand.{/n}
"What'd you keep for me? If you kept anythin'. Don't owe me a page a day."''',
      c('[Give her the written account of a moment you wanted to share.]', "moment", requires=("anevia.absence_shared_moment",)),
      c('[Give her the page about fearing what might change.]', "changed", requires=("anevia.absence_changed",)),
      c('[Tell her the account you kept without writing.]', "unwritten", requires=("anevia.absence_unwritten",)),
      c('"I kept your page. I haven\'t finished my answer. I\'ll start it here."', "unwritten", forbids=("anevia.absence_account",))),
    n("moment", "Anevia", '''{n}Anevia reads without a word. Once her thumb stops against the edge of the page, and she goes back over a line before she carries on.{/n}
"Wish I'd been there for that."
{n}She looks up.{/n}
"Wish I'd seen your face while it happened. Letter can't give me that. You'd have turned round to me, and I'd have known you wanted me to look."
{n}She folds the page carefully with your writing inside.{/n}
"Now tell me the bit you crossed out. I can see you fought with it. I want the fight."
{n}You explain the sentence you took out. Anevia disagrees with your first reason and asks a sharper question, and soon the letter has turned into what you wanted when you wrote it: something she can answer back.{/n}''', c('[Let the remembered moment become a conversation.]', "her_days")),
    n("changed", "Anevia", '''"I did get used to some of it."
{n}She gives you the hard answer with her hand still on yours.{/n}
"Not havin' you about. Havin' to decide what to do with a night instead of just wantin' you and callin' that a plan. Didn't stop wantin' you. Stopped lettin' it run my whole week."
{n}She reads the second thought again, the one under the fear.{/n}
"Glad you left the blots in. Tells me which lines you fought. I'd have burned the page and written you a nice lie."
"A patient wall?"
"Saintly. Terrible advice, though."
{n}She kisses your fingers before she puts the page down.{/n}
"Now ask about the woman that's actually here. You'll still like her. She's got a few new opinions you ain't ready for."''', c('[Ask what she wants you to know about her days.]', "her_days")),
    n("unwritten", "Narrator", '''{n}You start with a small detail. Anevia asks where you were standing, then what happened just before the part you chose to tell. The questions change the story. Something you meant as an aside turns out to be why you remembered the day at all.{/n}
{n}When you lose the thread she waits while you find it. At the end she tells you which detail she will keep, and it is not the one you expected.{/n}
"There. Didn't need a letter. Better like this. I can ask questions while you're here to look offended by 'em."
{n}You ask whether she has anything you should brace for. For once she does not answer with a joke.{/n}''', c('[Give her the same room to answer.]', "her_days")),
    n("new_days", "Anevia", '''"A whole day? Dangerous. You'll find out how much of it I spend lookin' for somethin' I put down a minute ago."
{n}She grins, then thinks about it.{/n}
"There's stuff I keep meanin' to tell you. Little stuff. Places I went, rows I had, a woman who taught me somethin' while pretendin' she was only complainin'."
"You can tell me."
"I know. Knowin' don't make me remember to. I can spend a whole night with you talkin' about nothin' but the bits of my life you already saw."
{n}She leans in.{/n}
"So ask. And not like you're takin' a deposition."''', c('[Ask about an ordinary day she has not described.]', "her_days")),
    n("her_days", "Anevia", '''"Went back to the woman with the cuttin's. Asked if I could help with the boxes on her sill. She said I could start by carryin' 'em without tellin' her how I'd carry a wounded man through a sewer."
{n}She looks at you, amused.{/n}
"Apparently I'd been talkin' about the plants like they were a mission."
"Did you stay?"
"Yeah. Dirt under my nails. Learned which roots you don't pull apart. She asked if I wanted another cuttin' when it's ready. Said yes before I could invent a reason I was too busy."
{n}Anevia rests her hand on the wooden box.{/n}
"Want more of that. Dirt, and an old woman who don't want a single secret off me. I'm goin' back Toilday."
{n}She waits to see what you make of Toilday.{/n}''',
      c('"Tell me about it. You don\'t have to take me along to all of it."', "end"),
      c('"I\'ll sulk when you spend an afternoon somewhere else. Go anyway."', "end")),
    n("end", "Anevia", '''"Toildays I'm in the dirt, then. Come and hold a pot. Badly. She'll love you."
{n}She moves in close enough to kiss you, then leans against you while the light changes in the window. Outside someone drops a bucket. She laughs at the string of curses that follows, each fouler than the last.{/n}
"So what're you doin' tomorrow," {n}she says,{/n} "that I ain't already guessed?"
{n}You tell her. She looks delighted by the part she didn't see coming.{/n}''',
      c('"Then let\'s meet the new ones."', flags=("anevia.return_ready",))),
], requires=("anevia.ordinary_life_kept", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"), chapters=(5,))


s("a_key_that_is_hers", "What she wants to keep", [
    n("start", "Anevia", '''{n}Anevia brings you a key on a short length of green cord. She keeps it in her own hand while she explains.{/n}
"Landlady offered me a longer lease. Not a promise the building survives the next siege. Just that she won't let it to somebody else every time I'm gone a week."
{n}She turns the key once between her fingers.{/n}
"I want it. Somewhere the box stays where I put it. Somewhere you come 'cause we said we'd meet, not 'cause I grabbed an empty room before anybody else did."
"And your home?"
"Still my home. Beth and me talked it through. This ain't me packin' a bag quiet and hopin' nobody asks what the key's for."
{n}She sits down beside you, and for once her face is not hiding anything.{/n}
"I want you in my life. Not the whole of it. But I want to know you'll keep turnin' up after the next easy night. Are you in, or are you visitin'?"''',
      c('"Yes. For keeps. Your life, mine, and whatever room we can make between them."', "yes"),
      c('"I love the time we have. I cannot promise that future."', "open"),
      c('"I have to end this. You deserve an answer I mean."', "part"),
      c('[Ask for time before giving a final answer.]', abort=True)),
    n("yes", "Anevia", '''{n}Anevia closes her fist round the key, then sets it on the table so she can take your hand instead.{/n}
"Good. Had some very dignified replies ready in case you made that hard."
{n}She kisses you before you can ask to hear them. When she pulls back she is grinning with a relief she does not bother to hide.{/n}
"You can have a key, if you want one. Once we've settled what usin' it means. Don't want to find out in a doorway at midnight with both of us knackered."
"What would you like?"
"No plan, you knock. Plan, you walk in. Somethin' changes, leave a note. And if you find me alone in there, I'm alone on purpose. Don't take it personal."
{n}Her thumb moves over your knuckles.{/n}
"And don't make me guess where I stand. Don't need a proclamation in the square. Just don't make me work it out from which invites you remembered."''',
      c('"I want the key, and I can keep those terms."', "key", flags=("anevia.shared_key",)),
      c('"Keep the key. I\'d rather keep knocking."', "invited", flags=("anevia.kept_invitations",))),
    n("key", "Anevia", '''"Then I'll get a copy cut. This one stays mine."
{n}She loops the cord round her finger, pleased with herself.{/n}
"Like that. You get a way in, room's still mine. Sounds obvious said out loud. Wasn't, always."
{n}You settle where to leave messages and which neighbor will take a note without reading it. She bristles when you offer to pay for every repair, and you agree to ask before turning a leaky shutter into a present she has to be grateful for.{/n}
"You can hold the ladder," {n}she says.{/n} "You're very good at standin' there while I swear."
{n}She points out where the ladder slipped last time. The scrape is still on the plaster.{/n}''', c('[Ask what she hopes will happen in the room.]', "room")),
    n("invited", "Anevia", '''"I can like that too. Don't have to go for the grandest version."
{n}She lays the key by the lamp.{/n}
"I like askin' you. Like knowin' you came 'cause you wanted to, not 'cause the room's on your way past."
"You may still ask for a different arrangement later."
"So can you. Preferably before one of us throws a boot."
{n}She grins and leans against you.{/n}
"There. For keeps, with a few questions left in it. Believe that more than any vow."''', c('[Ask what she hopes will happen in the room.]', "room")),
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
{n}Her smile is warm and deliberately wicked. She catches the front of your shirt and draws you closer, and waits, not very long, to see what you'll do about it.{/n}
"We could begin investigating the second possibility."''',
      c('[Kiss her and stay for the evening she has chosen.]', "night"),
      c('[Hold her and listen to the street.]', "end"),
      c('"Let me help with the bread. Tell me which part you\'ll trust me with."', "bread"),
      c('"I would rather share the table than pretend I know how to bake."', "table")),
    n("night", "Anevia", '''{n}You kiss her. She makes a pleased, impatient sound against your mouth and walks you backwards the two steps to the bed, which is as far as the room goes. The key's cord is still round her finger; she flicks it onto the hook by the door without looking.{/n}
"Landlady's deaf in one ear. Let's find out about the other."
{n}She has your shirt open before you have her laces loose, and then she has to help with those as well, swearing at the knots she tied that morning. The dress goes over her head and onto the chair. She pushes you down onto the lumpy mattress, climbs astride you with one knee braced against the frame, and pulls your hands to her hips.{/n}''',
      c("Continue", "key_morning")),
    n("key_morning", "Anevia", '''{n}Grey light through a shutter that does not close. The key is still on its hook by the door, swinging a little every time a cart goes past below. Anevia is sitting on the edge of the bed lacing her boots, with your shirt on and her own dress over the chair.{/n}
"Landlady's other ear works fine. She knocked on the wall twice. I knocked back."
{n}She finishes one boot and starts on the other, and does not hurry.{/n}
"I promised Beth breakfast. Proper breakfast, at the house, with the burnt bit on her plate so she can complain about it. I'm keepin' that promise. Then I'm comin' back here tonight, and you're gonna be on the right side of that door when I do."
{n}She takes the key off its hook, looks at it, and hangs it back.{/n}
"Stays there. That's where it lives now."''',
      c('[Choose a lasting relationship with Anevia.]', flags=("anevia.committed", "anevia.future_chosen"))),
    n("bread", "Anevia", '''"Measuring. Apparently guessing is a privilege you earn after you know what you're doing."
{n}She draws a rough circle in a patch of dust on the table, then divides it badly.{/n}
"One loaf. No buying me a bakery while I'm asleep. If I burn it, you'll have to be there for the second attempt."
"What if I burn it?"
"Then we'll have discovered a useful division of blame."
{n}She wipes away the drawing before the cup can spread it across her sleeve.{/n}
"All right. I'll ask the cook when the oven's free. And I'll do the asking. And she can tell me no without the Commander standin' in her kitchen lookin' hopeful."''',
      c('[Agree to a first attempt when she has arranged it.]', "end", flags=("anevia.bread_company",))),
    n("table", "Anevia", '''"Good. An honest appetite. I know what to do with one of those."
{n}She takes your hand and draws you back toward her.{/n}
"You can tell me if it's awful. I'd rather hear it from you than watch Beth construct an elaborate lie about the crust."
"Would she?"
"She'd try. Wouldn't get far. Her ears give her away."
{n}Anevia smiles at the thought, then kisses you.{/n}
"Come hungry. Whatever else goes wrong, we ought to manage that."''',
      c('[Look forward to the meal she wants to offer.]', "end", flags=("anevia.bread_guest",))),
    n("end", "Narrator", '''{n}You stay together while the room goes dark. The key lies where she put it. When she reaches for it the cord snags under a cup, and she rescues both with a muttered curse.{/n}
{n}Anevia tells you one more thing she wants, and you tell her one she hadn't guessed. She knocks back the first day you suggest, because she's promised it to Beth for an errand. You find another and scratch it on the scrap of paper by the lamp.{/n}''',
      c('[Choose a lasting relationship with Anevia.]', flags=("anevia.committed", "anevia.future_chosen"))),
    n("open", "Anevia", '''{n}Anevia listens, then puts the key in her pocket.{/n}
"Wanted the other answer. I can still hear this one."
{n}She asks what you can offer without dressing it up as forever. You tell her. She thinks about it long enough that you stop getting a reply ready and just wait.{/n}
"I want to keep seein' you. I just ain't buildin' shelves in a house you might not live in. It stops bein' enough, you'll hear it before breakfast, with the pan in my hand."
"Understood."
"Don't you 'understood' me like a quartermaster. It stings. I'm takin' it anyway."
{n}She takes your hand and squeezes it hard enough to hurt, which is the closest she comes to saying the rest.{/n}''',
      c('"Keep askin\' me. I\'ll keep comin\'."', flags=("anevia.open_future", "anevia.future_chosen"))),
    n("part", "Anevia", '''{n}She closes her hand round the key and keeps it there.{/n}
"Right. Can't argue it wasn't clear."
{n}The joke falls flat. She does not try another.{/n}
"Keep away a while. Not out of headquarters. Just don't come find me tomorrow for a nice little chat so you can see I'm takin' it well. I won't be."
"I understand."
"You don't. Keep away anyway."
{n}You leave her with the key and the room she wanted. She is still gripping the key when you look back from the doorway.{/n}''',
      c('"This is where I stop, Nevi."', flags=("anevia.closed", "anevia.parted"))),
], requires=("anevia.return_ready", "anevia.case_consequence_kept", "anevia.lover"), forbids=("irabeth_dead", "irabeth_gone"), chapters=(5,), delay=48)


s("the_last_ordinary_thing", "Before the next road", [
    n("start", "Anevia", '''{n}Anevia has fixed the loose catch on the borrowed window. She shows you twice, then opens it again to let the evening in.{/n}
"There. Can shut it when I like. Now I can, I don't much want to."
{n}She turns to you with a smile that does not quite hide why she asked you here.{/n}
"You're off again. Whatever's next. Been tryin' to think what sensible thing I could give you that doesn't say I think you can't pack."
{n}On the table stands the crooked wooden goat from the game. Anevia picks it up.{/n}
"Settled on somethin' completely useless. Hard to get the wrong idea."''',
      c('[Take the little goat and ask what she wants you to remember.]', "remember"),
      c('"Keep it here. I would like a reason to come back and finish the game."', "here"),
      c('[Leave this farewell for another evening.]', abort=True)),
    n("remember", "Anevia", '''"That I won the first game. Historical fact. Very important."
{n}She puts it in your palm and closes your fingers over it.{/n}
"And that I wanted to see you when there was nothin' to ask. That we could fight and still have a good night. That you don't have to go and do somethin' heroic before you get to miss somebody. Write that on your arm if you have to."
{n}She looks at your closed hand.{/n}
"It's small. Fits somewhere without you havin' to leave a bandage behind. Wouldn't want to win that argument."
{n}You put it away. Anevia watches until it is safe, then steps in close.{/n}''', c('[Hold her close.]', "future")),
    n("here", "Anevia", '''"Then it stays by the lamp. And nobody tidies it away while you're gone."
{n}She stands it facing the board, as if giving it something to think about.{/n}
"I might practise. Fair warnin', before you promise to come back and win."
"You would practise against yourself?"
"Horrible opponent. Knows all my tricks."
{n}The joke leaves her smiling and very close to tears. She lets you see both, and steps nearer instead of finding something else to straighten.{/n}''', c('[Leave room for what she has not hidden.]', "future")),
    n("future", "Anevia", '''"I'm not doin' tonight like it's my last chance to say anythin'. Makes plain words sound like somebody else's speech."
{n}She takes your hand.{/n}
"I love you. There. Plain. I want to say it lots. When I'm narked with you. When you turn up early. When nothin's happened at all."
{n}You answer her. Her thumb goes still on your hand. When you finish, she grins.{/n}
"Good. Start with tonight, then."
{n}You stay together while the room darkens. There are kisses, a complaint about the tea going cold and a fight about where the game should be kept. Anevia insists the fight counts toward her promise to say things plainly. You tell her she is making suspiciously good progress.{/n}
{n}When it is time, she walks you to the door. She does not ask the road to promise anything.{/n}
"Come back if you can. I'll have stuff to tell you."''',
      c('[Kiss her goodbye.]', flags=("anevia.developed",))),
], requires=("anevia.future_chosen", "anevia.case_consequence_kept", "anevia.ordinary_life_kept", "anevia.lover"),
   forbids=("irabeth_dead", "irabeth_gone"), chapters=(5,), delay=24)


s("a_grief_with_a_name", "The person she is missing", [
    n("start", "Anevia", '''{n}Anevia is holding a folded cloth and cannot decide where to put it. She sets it on the table when you come in, then picks it up again before she speaks.{/n}
"Beth's. Nothin' important. I keep findin' nothin' important and I can't put any of it down."
{n}She looks at you, worn out, and she has clocked exactly how carefully you came through the door.{/n}
"Say her name. Everybody's tiptoein' round it like it's a hole in the floor."
{n}You say Irabeth's name. Anevia shuts her eyes, then sits.{/n}
"Thanks."''',
      c('[Sit with her and wait.]', "cloth"),
      c('"Would you rather be alone? I can come another day."', "company"),
      c('[Leave the conversation unfinished for now.]', abort=True)),
    n("company", "Anevia", '''"Not tonight. Might tell you to go later. When I do, just go. Don't make me cheer you up about it."
"You can."
{n}She hooks a chair closer with her foot.{/n}
"Sit, then. And don't look for somethin' to fix. I know you're good at it. I ain't a job."
{n}The old dryness almost makes it to a smile. She turns her face away and rubs one eye with the heel of her hand.{/n}''', c('[Sit beside her.]', "cloth")),
    n("cloth", "Anevia", '''"She folded these different. I told her it didn't matter which edge went outside. She said it mattered to her. We had a whole row about whether that counted as an answer."
{n}Anevia turns the cloth over in her hands.{/n}
"It did. Bloody irritatin' answer. I'd give anythin' to have it to argue with."
{n}For a while she says nothing. Somebody walks past the door without stopping.{/n}
"Everybody tells me she knew I loved her. Course she did. I've still got things to say to her. Knowin' don't finish the conversation."
"No."
"Everybody remembers the brave paladin with the sword. I remember her tryin' not to laugh while I explained why that soup was a personal insult."
{n}She folds the cloth her wife's way and leaves it in her lap.{/n}''',
      c('"Tell me something about her. I\'ll remember it too."', "memory"),
      c('"Or say nothing. I\'m not going anywhere."', "silence")),
    n("memory", "Anevia", '''"She tried to mend a chair once 'cause I said it leaned. Wouldn't admit she'd never done it. Came back with a chair leanin' the other way and a splinter she wouldn't let me dig out till she'd explained the improvement."
{n}Anevia laughs, suddenly, and the laugh turns into a sob before she can pick which one she meant. She claps a hand over her mouth, then drops it when you do not move.{/n}
"Both. Fine. Both."
{n}You ask what happened to the chair.{/n}
"Kept it. Folded rag under one leg. She was gonna fix it proper. I said I'd got fond of its opinions."
{n}Then she looks at the cold hearth.{/n}
"Had this picture of her comin' into the kitchen. Me with bread ready. Her burnin' her fingers 'cause she won't wait, pretendin' she didn't."
{n}Anevia presses the heel of her hand into one eye.{/n}
"If one more person tells me I can still learn to bake, I'll put 'em through a wall. I know I can. That ain't what I lost."
{n}You wait. She lowers her hand and looks at you.{/n}
"And don't you go standin' in that kitchen doorway to finish the picture for me. Sit here. I asked you here."''', c('[Stay quiet and let her have it.]', "us")),
    n("silence", "Narrator", '''{n}She leans back and lets the cloth lie still. Out in the corridor the work of the citadel goes on without asking her leave. Once she seems about to snap at a raised voice outside, then shakes her head and lets it go.{/n}
{n}After a while her hand comes to rest beside yours. Then, without looking, she takes it and holds on hard.{/n}
{n}Eventually she turns toward you. She is no less sad. She has stopped minding being watched.{/n}''', c('[Stay while she finds the words.]', "us")),
    n("us", "Anevia", '''"I still want you. I dunno what I'll be like for a while."
{n}She says it flat, not offering either half to soften the other.{/n}
"Some nights I'll want you close and then I won't be able to stand anybody touchin' me. Some days I'll have a good afternoon and hate myself for it before I'm home. That's comin'. I ain't gonna let every bad hour decide the rest of my life, neither."
"What can I do?"
"Ask what kind of day it is. If I throw somethin', it's a bad one. And don't you ever think you got her side of the bed. You didn't. That's hers. You've got the draughty side, same as always."
{n}Her hand stays by yours.{/n}
"You were somebody I wanted before. Stay that. You try bein' Beth and I'll know in a minute, 'cause you'll fold the socks wrong."''',
      c('"I want to stay. Not in her place. Beside it. One visit at a time."', "remain"),
      c('"I care for you. But I can\'t go on with this, and it\'s not your fault."', "part")),
    n("remain", "Anevia", '''"Then come back. Knock first. I'll try to tell you straight, not just say whatever'll make you feel better."
{n}She sets the cloth by the chair, close, but no longer clenched in her fists.{/n}
"Not every visit's gotta be about her. Some will. My pick."
{n}You stay until she asks for the room to herself. She stands first, tired enough to lean on the table. At the door she remembers your cloak and hands it over. Her hands are steadier now.{/n}''',
      c('[Stay until she sends you home.]', flags=("anevia.bereavement_heard", "anevia.survivor_continues"))),
    n("part", "Anevia", '''{n}Anevia listens without looking away.{/n}
"Wish it was different. Glad you didn't make out it was my doin'."
{n}She pulls the cloth back into her lap.{/n}
"Go on, then. Keep your distance a bit. I've got people I can send for. Don't stay with me out of pity so I ain't alone tonight. I'd know."
{n}You leave when she asks. Behind you, a chair scrapes.{/n}''',
      c('"I can\'t, Nevi. I\'m sorry."', flags=("anevia.closed", "anevia.parted"))),
], requires=("anevia.lover", "irabeth_dead"), forbids=("anevia.irabeth_killed_by_commander",), chapters=(5,), delay=0)


def ending(identity, title, text, *, requires=(), forbids=(), owner="Epilogue"):
    local_close = () if identity == "ending_parted" else ("anevia.closed",)
    SCENES.append(scene("anevia." + identity, title, owner, 1, "",
        [n("end", "Narrator", text, portrait="Anevia")],
        requires=requires, forbids=tuple(dict.fromkeys(("closed", "trying", "committed", *local_close, *forbids))), last=6,
        Relationship="anevia", ForbidOverrides={"trying": "tirabade.group_closed", "committed": "tirabade.group_closed"}))


LIVING_END = ("anevia.closed", "anevia_dead", "anevia_gone", "irabeth_dead", "irabeth_gone", "inhuman", "sacrifice", "ascended")
ending("ending_kept", "The room with the repaired window", '''{n}Anevia kept the room. The window needed a second repair, and the plant outgrew another pot before she admitted she had become the kind of woman who asks the neighbors about roots.{/n}
{n}The Commander stayed part of that life: visits actually kept, notes that sometimes came late, and a long habit of saying so when either of them minded something. Anevia never got easier to surprise, and never stopped picking fights with explanations she found too convenient. She did start bringing her half-finished thoughts to the Commander before they were polished.{/n}
{n}Irabeth stayed Irabeth: she still folded her socks in threes, still read the Commander's notes to Anevia aloud in a flat voice at breakfast to embarrass everyone, and once, memorably, came up the stairs to the room with the bad window to deliver a pie and a lecture on fire hazards, and stayed for the pie.{/n}
{n}Ressa's street remembered the false inspection. Some of the money took years to come back. Anevia kept asking after the women on the list without ever sending Dema another basket. The Commander knew enough of that work to admire it and enough of Anevia to argue with her about it.{/n}
{n}Some evenings went badly. Some nights neither of them wanted to end. Now and then Anevia would look up from a book or a sulking seedling and seem freshly delighted to find the Commander still there. She always made a joke first. The admission came after, and quicker every year.{/n}''',
       requires=("anevia.committed", "anevia.developed"), forbids=LIVING_END)
ending("ending_open", "An invitation without a final promise", '''{n}Anevia and the Commander kept seeing each other without calling it settled. Some invitations were taken, some put off, and a few refused to their faces. They learned which promises they could keep and stopped dressing up the ones they couldn't.{/n}
{n}Her home with Irabeth stayed her home. Her work stayed hard, and most of her life went on in rooms the Commander never saw. She never apologized for that, and she never pretended the gaps were easy.{/n}
{n}The room with the bad window kept its own evenings. Some nights the goat game came out. Some nights it stayed folded while the two of them talked, or found a better use for the bed. Anevia liked being asked. She liked even more saying "not tonight, I'm busy" and watching the Commander try not to look put out.{/n}
{n}Leaving, the Commander would sometimes find a crooked wooden goat in a pocket, and a note daring them to come back and lose again.{/n}''',
       requires=("anevia.open_future", "anevia.developed"), forbids=(*LIVING_END, "anevia.committed"))
ending("ending_unfinished", "A question they had not finished", '''{n}Anevia and the Commander had started something with more questions in it than they had nights to answer. The nights they had kept were good ones. Anevia still had things to ask.{/n}
{n}She went on living around the crusade and her marriage. She remembered what it was like to be wanted by somebody who didn't want a report. Some evenings she thought of a thing she'd have said to the Commander and wondered whether to send for them.{/n}
{n}She hated leaving a question to guesswork. Once, halfway through another letter, she turned the page over and started a note of her own.{/n}''',
       requires=("anevia.lover",), forbids=(*LIVING_END, "anevia.developed", "anevia.committed"))
ending("ending_promised", "The next visit they had chosen", '''{n}Before the last campaign was over, Anevia and the Commander had said out loud that this was for keeps. What they had not yet had was the years to find out if they could keep it.{/n}
{n}Anevia kept the key on its green cord. Sometimes she wound it round a finger while she wrote a note, scratched out a perfectly good opening and started instead with the thing she actually wanted.{/n}
{n}Her home with Irabeth stayed her home. The room she'd taken for herself still needed fixing. Neither surprised the Commander. There would be missed nights and bad rows. The first time the Commander stood her up, she sent the note back with the spelling corrected and one word underneath: Toilday.{/n}
{n}She waited for the next visit with an impatience that embarrassed her. It never stopped her sending the note.{/n}''',
       requires=("anevia.lover", "anevia.committed", "anevia.future_chosen"), forbids=(*LIVING_END, "anevia.developed"))
ending("ending_parted", "What remained after the goodbye", '''{n}Anevia never called it a mistake just because it ended. There were things she had wanted and got, and things she would have done differently knowing what she knew after. The Commander was part of that, and had no say in what she chose next.{/n}
{n}They kept out of each other's way where they could. Work put them in the same room sometimes, and they managed courtesy long before they managed ease. Anevia did not put on a cheerful friendship to make the parting look better.{/n}
{n}Her life went on past the goodbye. She had people to see and work to finish. Some evenings she left early, sick of being asked whether she was quite herself.{/n}''',
       requires=("anevia.parted", "anevia.closed"), forbids=("anevia_dead", "anevia_gone", "inhuman", "sacrifice", "ascended"))
ending("ending_survivor", "The life she did not stop living", '''{n}Irabeth's death stayed in Anevia's life. Her boots stayed under the bed for a year, toes to the wall, and the Commander learned to step round them in the dark.{/n}
{n}Some visits Anevia asked for. Some she met at the door with "Not today," and shut it. Some days she threw things; the Commander learned which cups were safe to have given her.{/n}
{n}They said Irabeth's name. They remembered her burned fingers and her bad chair, and some nights they talked about something else entirely and laughed, and Anevia did not apologize for it the next morning.{/n}
{n}On the anniversary of Iz she went up to the wall alone, every year, and came down again, every year, and knocked on the Commander's door on the way back.{/n}''',
       requires=("anevia.lover", "anevia.survivor_continues", "irabeth_dead"),
       forbids=("anevia.closed", "anevia_dead", "anevia_gone", "inhuman", "sacrifice", "ascended", "anevia.irabeth_killed_by_commander"))

# Native Coronation can remove Anevia before the conditional contact chapter.
# These endings remember earned romance without fabricating that visit or her consent to resume it.
ending("ending_grief_unanswered", "The invitation not yet renewed", '''{n}Irabeth died before Anevia and the Commander had talked about what they would be to each other afterward. What they had before was real. So was the life Anevia had meant to go on living with her wife.{/n}
{n}The Commander remembered her delight when a conversation went somewhere she hadn't planned, and how fast she could turn her back on a question she didn't like. There were questions now that no old invitation could answer. Letters were started, torn up, started again.{/n}
{n}Anevia had not promised another visit. The Commander could miss her without pretending the silence was a yes. Whatever she chose next would come out of a life that had lost its center.{/n}''',
       requires=("anevia.lover", "irabeth_dead"),
       forbids=("anevia_dead", "anevia_gone", "anevia.survivor_continues", "anevia.irabeth_killed_by_commander", "inhuman", "sacrifice", "ascended"))
ending("ending_wife_absent", "News that did not arrive", '''{n}Irabeth was gone from the Drezen the Commander knew. Where she had gone, and what Anevia meant to do about it, nobody said.{/n}
{n}There had been something real between Anevia and the Commander, and plans made face to face. None of the questions that mattered now could be answered by remembering a good night. Anevia's marriage had never been an empty house waiting for a new tenant.{/n}
{n}The Commander kept the sound of her laugh. No letter came to turn the silence into an invitation, or into a reason to mourn a woman nobody had seen die.{/n}''',
       requires=("anevia.lover", "irabeth_gone"),
       forbids=("irabeth_dead", "anevia_dead", "anevia_gone", "anevia.irabeth_killed_by_commander", "inhuman", "sacrifice", "ascended"))
ending("ending_wife_killed", "The answer affection could not change", '''{n}The Commander had killed Irabeth. Nothing Anevia had once felt could turn that into a grief the two of them might share.{/n}
{n}There were memories of earlier nights: Anevia reaching for a hand, or stopping mid-joke because she had started laughing at it herself. The Commander kept them. They did not add up to a forgiveness she had never given.{/n}''',
       requires=("anevia.lover", "irabeth_dead", "anevia.irabeth_killed_by_commander"),
       forbids=("anevia_dead", "inhuman", "ascended"))
# Sol pol INT: the permanent closure is true only of an Anevia who never came back; a returned one left a door ajar at
# the gate ("Come back when you can knock"), so her variants are appended by anevia_trickster.integrate instead.
SCENES[-1]["Nodes"][-1]["Paragraphs"] = [p(
    "{n}No further invitation came from Anevia. Her anger belonged to the woman who had loved Irabeth, and the Commander "
    "had no right to shrink it into a misunderstanding. Whatever other night they might once have had was gone.{/n}",
    forbids=("anevia.trickster.returned",))]

ending("ending_death", "The afternoons that had happened", '''{n}Anevia's death left no finished version of the life she and the Commander had been building. There were real nights to remember, real fights, and a particular way she looked pleased a heartbeat before she decided whether to admit it. She had a gift for leaving even a short visit with something unfinished to laugh about next time.{/n}
{n}The Commander remembered her work as well as her warmth. She had wanted answers for people other folk treated as names on a list. She had also wanted a room of her own, an afternoon nobody turned into a duty, and the right to be ridiculous without being loved less for it.{/n}
{n}For years afterward the Commander still turned at a certain laugh in a crowded room.{/n}''',
       requires=("anevia.lover", "anevia_dead"), forbids=("inhuman", "ascended"))
ending("ending_gone", "Beyond the invitations that remained", '''{n}Anevia had gone out of the life the Commander knew her in. An old invitation could not say where she was now, whether she wanted to answer, or what reaching her would take.{/n}
{n}The Commander had real memories, and now and then a question that would once have gone straight to her. They made the absence heavy. They did not give anyone an address, or the right to mourn a woman who had only left.{/n}
{n}If there was ever another conversation, it would start with the woman who was actually there, and whatever roads had brought her to it. For now, nothing came back.{/n}''',
       requires=("anevia.lover", "anevia_gone"), forbids=("anevia_dead", "inhuman", "ascended", "sacrifice", "anevia.irabeth_killed_by_commander"))
ending("ending_sacrifice", "The answer she could not receive", '''{n}The Commander's sacrifice left Anevia holding things she'd meant to say on some ordinary night. Some were soft. Some were fights she would never get to finish. She came to hate how often people expected the victory to make up for it.{/n}
{n}She had always known no road promised a way home. Knowing did not make it easier to walk past the empty chair. It did not make the nights they'd had any less real than the ones they didn't get.{/n}
{n}Anevia went on living among the people and the work that were left. She refused to become anybody's noble widow before she was allowed to just miss the one she'd wanted beside her.{/n}''',
       requires=("anevia.lover", "sacrifice"), forbids=("anevia_dead", "anevia_gone", "inhuman", "ascended", "anevia.irabeth_killed_by_commander"))
ending("ending_changed_power", "An answer power could not supply", '''{n}Whatever the Commander became, Anevia took one look at it and packed a bag. She left the key on its green cord hanging from the doorknob, where the thing that had been the Commander would find it.{/n}
{n}It sent for her once. She sent the messenger back with his boots tied together.{/n}
{n}She kept the goat game. She played it with Beth, badly, on Toildays, and she did not say who had taught her the house rule.{/n}''',
       requires=("anevia.lover", "inhuman"), forbids=())
ending("ending_ascended", "The scale of an ordinary invitation", '''{n}Ascension changed what the Commander could become. Anevia, told about it by a very nervous herald, asked whether it was catching and whether the herald wanted tea.{/n}
{n}There had been a woman who liked an ordinary invitation and could find something to tease the Commander about even at a funeral. The Commander had known her at that size. Remembering her that way mattered more than giving what they'd had a grander name.{/n}
{n}Whatever came after would have to knock. She was very clear with the herald on that point, and she made him repeat it back.{/n}''',
       requires=("anevia.lover", "ascended"), forbids=("inhuman",))
ending("ending_aeon", "An invitation outside the rewritten world", '''{n}In the rewritten world, nothing that had put Anevia and the Commander in the same room had happened. The borrowed room, the goat game, the nights she had picked: all of it was gone.{/n}
{n}Somewhere in that world a woman with sharp eyes and a Kenabres accent ran a tavern, cheated at a game with wooden goats, and had a wife who snored like a siege engine.{/n}
{n}The Commander went there once, bought a drink, and lost a game to her. She said "Come back and lose again," the way she said it to everybody. It was not nothing.{/n}''',
       requires=("anevia.lover",), forbids=(), owner="AeonEpilogue")

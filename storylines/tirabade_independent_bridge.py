"""Authored joins between independent courtship and the existing shared campaign.

This contribution is staged for assembled review, not registered by expansion.py.
Existing answer arrays remain prefixes, preserving saved answer identities.
"""
from copy import deepcopy
from story_format import c, n, scene

ANEVIA = "b5e867e13503c6f41bb1316705efb4a2"
IRABETH = "280d4712dceb37f4a88e98f1f4c6e64f"
DREZEN = "2570015799edf594daf2f076f2f975d8"
ANSWERS = ["33960c7f7af40cd43b7f801a76c87a0b", "871af36f2ab2b1f40b5de77976c54276"]
GROUP_CLOSED = "tirabade.group_closed"


def separation_nodes():
    return [
        n("separate_question", "Irabeth", '''"Then let us be precise about what you are asking."
{n}Irabeth moves her chair back a little. She is still within reach of her wife, but you can see both their faces without leaning around the table.{/n}
"If you do not want a relationship with me, I need to hear that. If you want one without the expectation that every important evening belongs to all three of us, I need to hear that too. They would be different answers."
"And if you're hoping Beth will tell me what I ought to want," Anevia adds, "you'll have a long evening. She tried that once about a coat. I still own it."
{n}The joke gives Irabeth something familiar to smile at. It does not turn the question into a joke.{/n}
"Our marriage isn't the part you're being asked to settle," Anevia says. "What you want with each of us is. Say that first. We can answer for ourselves."''',
          c('"Anevia, I want to continue with you. Irabeth, I am ending our romantic relationship."', "separate_anevia", forbids=("anevia.closed", "irabeth.closed")),
          c('"Irabeth, I want to continue with you. Anevia, I am ending our romantic relationship."', "separate_irabeth", forbids=("anevia.closed", "irabeth.closed")),
          c('"I want a relationship with each of you, without a shared household or an expectation that we meet as three."', "separate_both", forbids=("anevia.closed", "irabeth.closed")),
          c('"Anevia and I have parted. Irabeth, I would like to continue with you."', "separate_irabeth", requires=("anevia.closed",), forbids=("irabeth.closed",)),
          c('"Irabeth and I have parted. Anevia, I would like to continue with you."', "separate_anevia", requires=("irabeth.closed",), forbids=("anevia.closed",)),
          c('"I need more time to understand what I am asking. I have not decided tonight."', "separate_wait")),
        n("separate_anevia", "Irabeth", '''{n}Irabeth looks down at her hands. When she raises her eyes again, she speaks to you first.{/n}
"I understand. I would rather you had wanted a different answer. That does not make this one unclear."
{n}Anevia does not reach across her wife to take your hand. She waits until Irabeth turns toward her.{/n}
"I still want to see you," Anevia says. "Alone. That's my answer, not something Beth has to say for me. But I won't turn her hurt into the price of a pleasant evening."
"I can live with you continuing to see each other," Irabeth says. "I may have an unhappy face when you leave. I would prefer not to be required to improve it before either of you can go."
"You won't be."
{n}Anevia's answer is quiet. She rests her hand on the table between them, leaving Irabeth room to take it or leave it there.{/n}
"Come and speak to me another day," she tells you. "We need to work out what we're actually offering each other. Don't arrive with an account of what Beth must have meant. I'll ask her myself."
{n}Irabeth nods. No one offers a farewell kiss to make the room look kinder than it feels.{/n}''',
          c('[Accept Anevia\'s individual invitation.]',
            flags=(GROUP_CLOSED, "irabeth.closed", "tirabade.anevia_continuation_invited"))),
        n("separate_irabeth", "Anevia", '''"Right."
{n}Anevia folds the edge of the cloth once, then smooths it flat again.{/n}
"I heard you. You needn't find a version that sounds like you're doing me a favor."
{n}Irabeth starts to speak. Anevia looks at her, tired rather than angry.{/n}
"And you don't have to give the same answer as me. I know that face."
"I was going to ask whether you wanted me to stay afterward."
"Yes. I would."
"I'm not asking you to stop seeing each other," Anevia adds. "I want our marriage. I can make room for this relationship without pretending I'm pleased about how my own has ended."
{n}Irabeth nods before turning to you.{/n}
"I still want a relationship with you. I cannot tell you tonight exactly what it will look like. There are things Anevia and I need to say without making you our audience. There are things you and I need to say without asking her to bear witness."
"That would be a considerable improvement," Anevia says. "Being brave in front of an audience gets exhausting."
{n}Irabeth gives her a small, pained smile.{/n}
"Come and speak with me another day," she tells you. "If we continue, I want it to be because we have chosen something we can live with. Not because neither of us could bear another ending tonight."
{n}When you leave, Irabeth stays as her wife asked. Their evening belongs to them.{/n}''',
          c('[Accept Irabeth\'s individual invitation.]',
            flags=(GROUP_CLOSED, "anevia.closed", "tirabade.irabeth_continuation_invited"))),
        n("separate_both", "Anevia", '''"That I can understand. I don't want every supper to become a vote on what all three of us are."
{n}Anevia looks at her wife.{/n}
"Beth?"
"I want time with each of you. I also wanted something the three of us might make together. I need to admit that I will miss the possibility."
"You can miss it. I might too."
{n}Irabeth turns back to you.{/n}
"I am willing to continue seeing you separately. I am not agreeing that our difficulties will disappear because we have fewer people at supper. I will still be married. I will still care how you treat my wife."
"And I'll still care how you treat her," Anevia says. "I won't conduct her conversations for her. Those are different things."
"Then we are agreed about the marriage too," Irabeth says. "Each of us can keep seeing you. We are not asking one another to give that up."
"Agreed," Anevia says.
{n}You discuss visits, private confidences and evenings that have already been promised elsewhere. Irabeth stops herself when she begins answering a question meant for Anevia. Anevia lets her start again without making the correction into a performance.{/n}
"Speak with each of us," Irabeth says. "A proper conversation. We have each said that we want to continue. We have not decided every detail of how."
"And when Beth and I go home together," Anevia adds, "you don't have to come along to prove you're all right. You're allowed an evening of your own. We'll try to survive the suspense."
{n}Irabeth's laugh is brief, but it is real. The decision has left them with something to do besides persuade one another not to be disappointed.{/n}''',
          c('[Accept separate conversations, without a shared relationship.]',
            flags=(GROUP_CLOSED, "tirabade.anevia_continuation_invited", "tirabade.irabeth_continuation_invited"))),
        n("separate_wait", "Irabeth", '''"Then we stop here for tonight."
{n}Irabeth draws a slow breath. Anevia puts the cloth back where it was.{/n}
"Don't make me guess which answer you're going to give," Anevia says. "When you know, tell me. Until then, I can live with 'I don't know.'"
{n}You leave the question open. Nobody calls the conversation a promise to continue, or a decision to part.{/n}''',
          c('[Leave the decision open. Speak again later.]', abort=True)),
    ]


SCENES = [scene(
    "tirabade.negotiated_table", "A supper nobody had promised", "Together", 3,
    '"I would like an evening with you both. Would you?"', [
        n("start", "Anevia", '''{n}Anevia asks you to wait until Irabeth has finished at the watch. When you meet them later, they have taken a small table in a side room at headquarters. Three mismatched cups stand beside a covered dish. Nobody has brought a report.{/n}
"Beth said we should be clear about the invitation. I said supper was a fairly clear invitation. Apparently I have been inviting people to complicated things for years."
"You once invited me to inspect a loose window fastening," Irabeth says.
"It was loose."
"I found out afterward that you had already repaired it."
{n}Anevia looks at you with conspicuous innocence.{/n}
"Good evening, though."
{n}Irabeth smiles. Then she takes her place beside the table, waiting for you to sit rather than choosing where you must go.{/n}
"We each have a relationship with you," she says. "We have not yet asked what we might want when the three of us are together. I would like to ask."
"And eat," Anevia adds. "The two ambitions can coexist."''',
          c('"I would like to find out."', "wanted"),
          c('"I am happy seeing you separately. I do not want to begin a shared relationship."', "separate"),
          c('"This deserves an evening when I can stay. May I ask another day?"', "later")),
        n("wanted", "Irabeth", '''"I wanted you to see us when we are enjoying ourselves."
{n}Irabeth glances at Anevia, whose fingers have paused on the cover of the dish.{/n}
"I have spoken about my marriage as something that must be considered. It is. But it is also the person who knows when I am trying not to laugh. The person I want to show a ridiculous thing because it will become more ridiculous when she sees it."
"I provide an essential service," Anevia says.
"You do."
{n}Irabeth says it without changing her expression. Anevia looks briefly at the dish, then reaches over to straighten a fold in her wife's sleeve. It takes longer than the fold deserves.{/n}
"I like you watching her," Anevia tells you. "Sometimes. Sometimes I find myself watching you instead. I wanted to find out what an evening would be like if I didn't have to pretend I was merely waiting for the two of you to finish speaking."
"You would not wait in any case," Irabeth says.
"No. But now I've said why."
{n}Anevia removes the cover. There are roasted roots, dark bread and a portion of cheese she warns both of you to divide fairly.{/n}''',
          c('"I like seeing the two of you together. I would like to be wanted here too."', "place"),
          c('"What would change between us?"', "change"),
          c('"I want you both. I do not want to assume that settles the evening."', "change")),
        n("place", "Anevia", '''"You are. I didn't buy enough cheese for a diplomatic observer."
{n}She passes you the plate, then lets the joke rest.{/n}
"I know Beth in ways you don't. She knows me in ways you don't. You know things about each of us the other hasn't been there to see. I'd rather be curious about that than keep score."
"There will be moments when we fall into an old habit," Irabeth says. "A look that means something to us and nothing to you. You can ask. You can also dislike being left outside it."
"You don't have to enjoy every story about our marriage. Some of them aren't very good."
{n}Irabeth looks wounded enough to make Anevia laugh.{/n}
"Especially the window one."
"That was your story."
"And I know when to retire it."
{n}They make room for your answer. The space is awkward for a moment, then easier when you speak without trying to match their years together.{/n}''',
          c('"Then let us make a few stories of our own."', "change")),
        n("change", "Irabeth", '''"We would be choosing evenings together. We would not be surrendering the evenings we spend separately."
{n}Irabeth breaks a piece of bread in two and gives half to Anevia.{/n}
"I would still ask you out without first arranging an outing for everyone. I would still want time alone with my wife. If either of you needed to speak to me privately, I would listen privately."
"And if one of us wants an evening to herself, we don't appoint the other two to find out what's wrong," Anevia says. "Sometimes I want to put my feet up and complain to nobody. It's a talent."
"You have rarely demonstrated it."
"Private talent."
{n}You discuss the simpler matters first: how to send word, who might be waiting, what can be said in front of the aides. Irabeth wants no false explanation that makes another person responsible for covering your whereabouts. Anevia wants no public announcement made on her behalf merely because it would save an awkward question.{/n}
"If someone asks me directly, I will answer for myself," she says. "I'd like the chance to do that before hearing which version has reached the kitchens."''',
          c('"Other people may also matter to me. I will keep the promises I make to them."', "others", flags=("other_loves",)),
          c('"I want to give this time without promising what the rest of my life will look like."', "time")),
        n("others", "Anevia", '''"Good. Then don't promise us their evenings."
{n}Anevia pushes the cheese toward Irabeth, who has been politely leaving the last piece alone.{/n}
"I don't need a list of every private thing you say to somebody else. I do need to know whether you're coming when you've told me you're coming. And they deserve the same."
"We should tell you when our own plans change," Irabeth says. "Neither of us has a spotless record there."
"Speak for yourself."
{n}Irabeth raises an eyebrow. Anevia considers it, then gives in.{/n}
"All right. Speak for both of us on that particular point."
{n}There is no demand to abandon another lover, and no attempt to turn this meal into permission for promises nobody has asked you to make.{/n}''',
          c('"Then we begin with the time we can actually give."', "time")),
        n("time", "Irabeth", '''"I would like another evening. After we have had time to think about this one."
"Supper again?" Anevia asks.
"Perhaps. Something ordinary."
"You say that as though we've been spectacularly unusual tonight. I have eaten too much and you have defended a window fastening."
{n}Irabeth laughs, surprised into it. Anevia watches her with an expression you have seen when her wife enters a room she was not expected to enter. Then she catches you watching and does not turn away.{/n}
"I could get used to this," she says.
{n}Irabeth sets down her cup.{/n}
"I want to try. With both of you. I do not need to decide tonight where we will live after the war. I do want you to know that I am here because I wanted to come."
"So am I," Anevia says. "And I want to hear your answer before I invent something clever to make it easier to say."''',
          c('"Yes. Let us try this together."', "goodnight"),
          c('"I care for you both, but I want to keep our relationships separate."', "separate"),
          c('"I need another day to think."', "later")),
        n("goodnight", "Narrator", '''{n}At the door, Anevia catches Irabeth's sleeve and draws her down for a kiss. Irabeth's hand settles at her wife's waist. It is a familiar gesture, offered without a glance to see whether you approve.{/n}
{n}When Anevia turns to you, there is a question in the way she holds out her hand. You take it and kiss her. Irabeth waits until you turn toward her before leaning close enough for you to meet her.{/n}
"Another evening," she says.
"With a less charitable division of the cheese," Anevia adds.
{n}You leave them arguing about who ate the last piece. The argument follows you down the corridor, affectionate and entirely unnecessary. For once you have no reason to wonder whether your departure has made the room easier to bear.{/n}''',
          c('[Choose the shared relationship you have discussed.]', flags=("trying",))),
        n("separate", "Anevia", '''"Then that's what we keep."
{n}Anevia lets out a breath, disappointed enough that she does not immediately dress it up as a joke.{/n}
"I liked the idea. I still like you. Both facts can fit in the same evening."
"I would rather know," Irabeth says. "The relationships we have chosen do not disappear because we choose against this possibility."
{n}You finish supper. You speak about another visit with each of them, separately. No one calls it a lesser answer, or pretends it was the answer she had hoped for.{/n}''',
          c('[Keep the independent relationships and decline the shared arrangement.]', flags=(GROUP_CLOSED,))),
        n("later", "Irabeth", '''"Then take it."
{n}Irabeth stands, and Anevia begins collecting the cups.{/n}
"Ask us when you're ready," Anevia says. "We'll see what evening we can find. You needn't decide because the food's already on the table."
{n}You leave without making a new promise. The relationships you brought to this conversation remain as they were.{/n}''',
          c('[Consider the invitation. Speak again another day.]', abort=True)),
    ],
    requires=("anevia.lover", "irabeth.lover", "anevia.marital_terms_agreed", "irabeth.marital_terms_agreed"),
    forbids=("closed", "anevia.closed", "irabeth.closed", "irabeth.future_friends", GROUP_CLOSED, "trying", "committed", "inhuman", "anevia_away", "irabeth_away"),
    optional=True, delay=24, Chapters=[3, 5], Areas=[DREZEN], AnswerLists=ANSWERS,
    ContactUnit=ANEVIA, AdditionalContactUnits=[IRABETH], Relationship="tirabade")]

SCENES.append(scene(
    "tirabade.after_local_parting", "A question left for the other woman", "Together", 3,
    '"One relationship has ended. I would like to speak about what that means for the other."', [
        n("start", "Narrator", '''{n}You ask whether both women are willing to speak with you. Anevia arranges a time after their duties; Irabeth asks you to meet them in a side room at headquarters. When you arrive, neither has brought anything to make the conversation look like a social call.{/n}
"We have already heard one answer," Irabeth says. "I do not want to argue you out of it."
"Neither do I," Anevia says. "But we haven't said what happens to the other relationship. I'd rather ask than find out we've all been assuming different things."
{n}They wait for you to sit. The conversation has room for an answer; it offers no way to take back the refusal already given.{/n}''',
          c('[Speak about the relationship that remains undecided.]', "separate_question")),
        *separation_nodes(),
    ], requires=("reckoning",), forbids=("closed", GROUP_CLOSED, "inhuman", "anevia_away", "irabeth_away"),
    RequiresAny=["anevia.local_declined", "irabeth.local_declined"], optional=True, delay=24,
    Chapters=[3, 5], Areas=[DREZEN], AnswerLists=ANSWERS,
    ContactUnit=ANEVIA, AdditionalContactUnits=[IRABETH], Relationship="tirabade"))

SCENES.append(scene(
    "tirabade.negotiated_letter", "The supper you would ask for", "Memory", 4, "", [
        n("start", "Narrator", '''{n}The paper has a stain near one edge. You turn it over, hoping the other side will look more suitable for a letter, and discover that the stain has had the same idea.{/n}
{n}Outside, Alushinyrra conducts another evening of business you would rather not describe to the people you miss. You write Anevia's name. Irabeth's follows beside it, leaving too little space for the sentence you had planned.{/n}
{n}You remember the covered dish at headquarters, Anevia insisting that Irabeth take the last piece of cheese, and the way Irabeth waited for your answer without trying to supply it. The recollection has an ordinary weight that nothing in this city quite possesses.{/n}''',
          c('[Write about the next evening you would ask them to share.]', "supper"),
          c('[Write about the question you cannot answer from here.]', "question")),
        n("supper", "Narrator", '''{n}You describe a supper without anyone eating hurriedly because the next summons is already overdue. You make no heroic promise to provide it. Instead you ask what each of them would bring, and find yourself smiling at the argument the question might provoke.{/n}
{n}It occurs to you that they might have an evening planned already. An evening together, or apart, which has nothing to do with you. The thought hurts a little before it comforts you. You wanted them to keep having a life. Distance has made it harder to enjoy being unable to supervise your own place in it.{/n}
{n}You leave room beneath the question, though no answer can arrive on this page tonight.{/n}''', c('[Continue the letter.]', "keep")),
        n("question", "Narrator", '''{n}You begin by asking whether they miss you. Then you stop. The question would be easy to answer in ways that told you very little about their days.{/n}
{n}You ask instead what Anevia has found funny lately, and whether Irabeth has had an evening she did not spend preparing for the next morning. There would be questions for you too. You try answering one before imagining how graciously they might receive it.{/n}
{n}The page becomes less polished. It also becomes something you could place on a table without having to explain which parts were written to make you look worth waiting for.{/n}''', c('[Keep the questions you actually wanted to ask.]', "keep")),
        n("keep", "Narrator", '''{n}There is no messenger you trust with the letter. You fold it and place it among the things you intend to carry home. The words record what you wanted tonight. They cannot reserve the future for you.{/n}
{n}Before putting it away, you add one small account of your own day. Anevia would complain about a letter made entirely of questions. Irabeth would notice what you had left out.{/n}
{n}You can almost hear them disagreeing about who should read it first. You let yourself enjoy the imagined voices, then return to the work of reaching the people who have the real ones.{/n}''',
          c('[Keep the unsent letter.]')),
    ], requires=("tirabade.negotiated_table", "trying"), forbids=("closed", GROUP_CLOSED, "anevia.closed", "irabeth.closed", "abyss_letter"),
    last=4, Remote=True, Relationship="tirabade"))


def history_variant(book, page_id, text):
    """Keep legacy answer IDs and prose; append choices for the new entry history."""
    original = next(page for page in book["Nodes"] if page["Id"] == page_id)
    alternate = deepcopy(original)
    alternate["Id"] = page_id + "_negotiated"
    alternate["Text"] = text.strip()
    for page in book["Nodes"]:
        for choice in list(page["Choices"]):
            if choice.get("Next") != page_id:
                continue
            newer = deepcopy(choice)
            newer["Next"] = alternate["Id"]
            newer["Requires"].append("tirabade.negotiated_table")
            page["Choices"].append(newer)
            choice["Forbids"].append("tirabade.negotiated_table")
    book["Nodes"].append(alternate)


def integrate(payload):
    books = {item["Id"]: item for item in payload["Scenes"]}
    if "tirabade.negotiated_table" in books:
        raise ValueError("Tirabade independent bridge applied twice")
    payload["Scenes"].extend(deepcopy(SCENES))

    # Ending either romance also ends the shared romance, without deciding the other's answer.
    for book in books.values():
        if book.get("Relationship") not in ("anevia", "irabeth"):
            continue
        for page in book["Nodes"]:
            friendship_answers = []
            for choice in page["Choices"]:
                if {"anevia.closed", "irabeth.closed", "irabeth.future_friends"}.intersection(choice["Set"]):
                    choice["Set"] = [*choice["Set"], GROUP_CLOSED]
                    choice["Text"] += " [Any shared romance between the three of you also ends.]"
                if book.get("Relationship") == "anevia" and "irabeth.lover" in choice["Requires"]:
                    if "irabeth.closed" in choice["Requires"]:
                        friendship = deepcopy(choice)
                        friendship["Requires"] = [flag for flag in choice["Requires"] if flag != "irabeth.closed"] + ["irabeth.future_friends"]
                        friendship["Forbids"] = [*choice["Forbids"], "irabeth.closed"]
                        friendship_answers.append(friendship)
                    elif "irabeth.closed" in choice["Forbids"]:
                        choice["Forbids"] = [*choice["Forbids"], "irabeth.future_friends"]
            page["Choices"].extend(friendship_answers)

    for who, ids in (
        ("anevia", ("a_cup", "a_errand", "a_roof", "a_crossing", "a_morning")),
        ("irabeth", ("i_watch", "i_hands", "i_respite", "i_crossing", "i_morning")),
    ):
        for sid in ids:
            books[sid]["Forbids"].append(who + ".closed")
            # A spoken request begins the new honest approach, not an unplayed affair.
            if sid not in ("a_morning", "i_morning"):
                books[sid]["Forbids"].extend([who + ".courtship_requested", who + ".lover"])

    for sid, page, who in (("a_roof", "friend", "anevia"), ("i_respite", "friend", "irabeth"),
                           ("a_crossing", "leave", "anevia"), ("i_crossing", "leave", "irabeth"),
                           ("a_truth", "stop", "anevia"), ("i_truth", "stop", "irabeth")):
        book = books[sid]
        source = next(item for item in book["Nodes"] if item["Id"] == page)
        source["Choices"].append(c('[End only this relationship. Speak for yourself about the other.]', "local_goodbye"))
        speaker = "Anevia" if who == "anevia" else "Irabeth"
        text = '''"Then that's what we've decided. You and me."
{n}Anevia rests her hand against the doorframe.{/n}
"I won't tell Beth what she ought to want. And I won't make you a promise about what she'll say. If there's something between you, you'll have to speak to her."
{n}Her voice softens a little.{/n}
"Give me time. I meant it about keeping the friendship. I'd like to manage that without making it look easy for your benefit."''' if who == "anevia" else '''"Then we have answered the question between us."
{n}Irabeth draws on her gloves, taking care with a fastening she could ordinarily manage without looking.{/n}
"Anevia is entitled to her own answer. I will not provide it for her. Nor can I promise what she will want because I have chosen to hear you without anger."
{n}She looks up.{/n}
"I would like some time before we attempt an easy conversation. That is all I am asking now."'''
        book["Nodes"].append(n("local_goodbye", speaker, text,
            c('[Respect her answer.]', flags=(who + ".closed", who + ".local_declined"))))

    for sid, page, who in (("a_roof", "danger", "anevia"), ("a_crossing", "choice", "anevia"),
                           ("i_respite", "admit", "irabeth"), ("i_crossing", "wife", "irabeth")):
        book = books[sid]
        source = next(item for item in book["Nodes"] if item["Id"] == page)
        source["Choices"].append(c('"I want to ask honestly before we cross that line. Speak with your wife, and then with me."', "honest_request"))
        text = '''"You make that sound almost possible."
{n}Anevia steps back, leaving the space between you empty.{/n}
"I'll speak to her. About what I want, not about some irresistible thing that happened to me while I was minding my own business. She deserves better than that story. So do I."
{n}She smiles briefly, without trying to recover the moment you have interrupted.{/n}
"And then we'll talk. You and me. Don't spend the meantime deciding which answer would be kindest for Beth to give. I married her. I know when she's saying something because she thinks she ought to."
{n}Anevia lets you leave without a kiss. The decision has not made her want you less; it has given her something to do about wanting you that she can explain in daylight.{/n}''' if who == "anevia" else '''"Yes. I can ask."
{n}Irabeth lowers her hand to her side. The movement is deliberate.{/n}
"I have been behaving as though the only choices were to betray her or pretend I felt nothing. Neither is a conversation I have actually allowed her to answer."
{n}She takes a breath.{/n}
"I will speak with Anevia. I am not promising what she will say, or asking you to wait as though she owed us a favorable answer. But I want to make the request honestly."
{n}At the door, she turns back.{/n}
"Come and speak with me again. There are things I need to ask you as well. We should know what we are asking before we decide how brave it is to ask."
{n}She leaves without touching you. You have no reason to mistake the care for indifference.{/n}'''
        book["Nodes"].append(n("honest_request", "Anevia" if who == "anevia" else "Irabeth", text,
            c('[Return for an honest conversation.]', flags=(who + ".courtship_requested",))))

    for sid, page in (("table", "proposal"), ("future", "choice"), ("parting", "start")):
        book = books[sid]
        source = next(item for item in book["Nodes"] if item["Id"] == page)
        source["Choices"].append(c('"Could we talk about separate relationships instead of a shared life?"', "separate_question"))
        book["Nodes"].extend(separation_nodes())
        # The book narrates meeting in the room after the invitation; both native actors must be available.
        book.update(ContactUnit=ANEVIA, AdditionalContactUnits=[IRABETH], Areas=[DREZEN], Chapters=[3, 5] if sid != "future" else [5])
        book["Forbids"].extend(["anevia_away", "irabeth_away"])
        book["Nodes"][0]["Text"] = '{n}The two women arrange to meet you after their duties. You join them in a side room at headquarters, where the conversation can belong to the people taking part in it.{/n}\n' + book["Nodes"][0]["Text"]

    personal_legacy = {"a_cup", "a_errand", "a_roof", "a_crossing", "a_morning", "i_watch", "i_hands", "i_respite", "i_crossing", "i_morning"}
    for book in books.values():
        if book.get("Relationship", "tirabade") == "tirabade" and book["Id"] not in personal_legacy:
            book["Forbids"].append(GROUP_CLOSED)
            if book["Id"] not in ("a_truth", "i_truth"):
                book["Forbids"].extend(["anevia.closed", "irabeth.closed", "irabeth.future_friends"])
    for sid in ("ordinary", "departure"):
        book = books[sid]
        book["Requires"] = list(dict.fromkeys(flag for flag in book["Requires"] if flag != "table"))
        if "trying" not in book["Requires"]:
            book["Requires"].append("trying")
        book["RequiresAny"] = ["table", "tirabade.negotiated_table"]

    history_variant(books["ordinary"], "rank", '''"I know what serving the Commander means. We were discussing something else."
{n}Irabeth's voice is level. Anevia sets her cup down harder than she intended.{/n}
"We asked for an evening. If you'd told me you couldn't keep it, I'd have been disappointed and eaten. I don't need to be reminded which of us has the more impressive title before I'm allowed to say I waited."
{n}She looks at the cup, then moves it away from the table's edge.{/n}
"I know you've got duties. So have we. That's why we were trying to make a plan."''')
    history_variant(books["return"], "back", '''"I miss how easy some of it felt, too."
{n}Anevia leans toward you.{/n}
"The part where seeing you was simply a good thing in the middle of the day. I still want that. I don't want to need a special occasion every time I ask you to sit down."
{n}Irabeth takes your hand.{/n}
"Nor do I. But I would like to hear what has changed for you, even when the answer complicates the evening we hoped to have. We have time to enjoy ourselves and time to learn something we did not expect."''')
    history_variant(books["power"], "azata", '''"Then keep choosing," Anevia says. "When the choice is interesting, and when it's whether to send word that you'll be late."
{n}She smiles a little, then rests her hand beside yours.{/n}
"I like that you want a life you haven't already been assigned. So do I. I asked Beth for something I wanted, and then I asked you. It mattered that you could each answer. I'd hate to find out we'd made all that effort just to start calling somebody else's answer an obstacle to our freedom."
"We will have promises to keep," Irabeth says. "We chose those too."
"Exactly. Desna doesn't have to remind me where I said I'd be for supper. I can remember that myself."''')
    history_variant(books["future"], "choice", '''{n}You discuss where you might live and discover that all three of you have strong opinions about stairs. You discuss money without allowing your rank to end the conversation. You discuss whether a public announcement would be courage or merely an efficient way to make other people unbearable.{/n}
"We can tell the people who need to know," Anevia says. "Everybody else can survive wondering."
{n}Irabeth agrees, then looks at you with a seriousness that quiets the room.{/n}
"We would like you in that life. I would. Anevia would. We have learned more about what we want than we knew when we first asked you to supper. I do not want to keep calling it an experiment because a promise makes me nervous."
{n}Anevia meets your eyes.{/n}
"We want you. With us. Do you want that too?"''')
    history_variant(books["future"], "yes", '''{n}Anevia lets out a breath she had been pretending not to hold. Irabeth reaches for you, then for her wife, drawing the three of you close enough that the table becomes an inconvenience.{/n}
"We should move that," Anevia murmurs.
"The table?"
"Eventually. I was having a moment."
{n}You laugh, all three of you. When the laughter passes, no one immediately lets go.{/n}
{n}There is no new oath before a temple, no witness empowered to make the choice permanent. You have said what you want and heard two answers. Keeping them will involve days far less graceful than this evening. Tonight, each of you is willing to begin.{/n}''')

    books["abyss_letter"]["Forbids"].append("tirabade.negotiated_table")
    books["abyss_dream"]["Requires"].remove("abyss_letter")
    books["abyss_dream"]["RequiresAny"] = ["abyss_letter", "tirabade.negotiated_letter"]
    return_start = next(page for page in books["return"]["Nodes"] if page["Id"] == "start")
    return_start["Choices"].append(c('[Show them the letter about the supper you hoped to share.]', "negotiated_letter", requires=("tirabade.negotiated_letter",)))
    books["return"]["Nodes"].append(n("negotiated_letter", "Narrator", '''{n}Anevia reads the letter first, then passes it to her wife without folding it. Irabeth smooths the crease with the side of her hand.{/n}
"I would have answered," she says.
"So would I," Anevia says. "Probably on worse paper."
{n}She touches the stain at the edge of the page. There are things both women might ask about the days in which you carried it. For now, Irabeth places the letter between you where no one has to reach across someone else to take it.{/n}
"We can tell you about our days now," she says. "You can tell us which part of yours belongs in a conversation instead of a report."''',
        c('"Then let us begin there."', "now")))

    for old_id in ("ending_together", "ending_apart", "ending_unfinished", "ending_loss", "ending_monster", "ending_aeon"):
        old = books[old_id]
        revised = deepcopy(old)
        revised["Id"] = "tirabade.negotiated_" + old_id
        revised["Requires"] = [flag for flag in revised["Requires"] if flag not in ("a_affair", "i_affair", "reckoning")]
        revised["Requires"].append("tirabade.negotiated_table")
        if old_id == "ending_together":
            revised["Nodes"][0]["Text"] = '''{n}When the war released its hold upon them, Anevia and Irabeth discovered that peace required skills for which the Eagle Watch had provided remarkably little training. Irabeth could still turn a visit to the market into a supply inspection. Anevia could still learn an entire street's secrets before remembering what she had gone there to buy.{/n}
{n}The Commander found a place in their life by returning to it, again and again. Their home acquired a third chair that was nobody's guest chair. It also acquired arguments about time, money, wet boots, and whether an unanswered question counted as an answer. Being able to ask for what they wanted did not make every answer easy to hear. They learned which quarrels improved with a night's sleep and which survived because somebody still needed to finish speaking.{/n}
{n}They kept private evenings as carefully as shared ones. Other duties and attachments were discussed rather than concealed. Irabeth learned to set down her work before exhaustion made the decision for her. Anevia learned to bake bread which even an honest person could praise. The Commander learned which promises mattered most when no one was watching.{/n}
{n}Visitors sometimes arrived hoping for a scandalous account of the arrangement. They usually left with a full stomach and several opinions about window repairs. Anevia complained that this was what became of a promising scandal when people insisted on enjoying their lives.{/n}'''
        if old_id == "ending_apart":
            revised["Nodes"][0]["Text"] = '''{n}The Commander, Anevia and Irabeth did not keep the shared future they once imagined. Ending it required conversations none of them enjoyed. It did not make the days they had wanted one another an elaborate mistake.{/n}
{n}Anevia and Irabeth kept their marriage. Some habits acquired during the Commander's visits remained; others became things they chose to put away. They did not agree about every memory. They learned which differences needed speaking of, and which could be allowed to belong to the person remembering.{/n}
{n}In time there were evenings when a familiar joke was funny without first becoming painful. Nobody had been able to promise when that would happen.{/n}'''
        if old_id == "ending_aeon":
            revised["Nodes"][0]["Text"] = '''{n}In a world from which the wound had been removed, the Commander's evenings with Anevia and Irabeth had no place to have happened. No letter waited to be carried home. No invitation had brought three people to the table where they first chose a life together.{/n}
{n}Whatever lives the women lived in that altered world belonged to them. The erased Commander could claim neither their memory nor their love as a reward for making it possible.{/n}
{n}The absence of a remembered promise was not another promise, waiting to be collected. The women were free to live the days that now existed.{/n}'''
        old["Forbids"].append("tirabade.negotiated_table")
        payload["Scenes"].append(revised)

"""Soana / Corven, round 2a: route-owned stance and continuity.

Canon: SoanaAfterQuest/Cue_0012, c6789b662ea5c404f957d9a20b68f5c7,
a verified memory of marriage and children;
Cue_0032, 1c27dcef5249a3f48b1a8d76b90332f6, her refusal to flee to Gundrun.
Neither establishes Corven's fate. The dispatch, journey and conversations below
are authored additions under CANON-PARTNERS-DESIGN.md's 2026-10-05 revision.
Corven's new dialogue is an authored voice, not a quotation of a native speaker.
The Commander exploits a cult courier's literal delivery obligation; ordinary
travel and a paid escort bring an elderly dwarf back, never a resurrection.
"""
from copy import deepcopy

from story_format import c, n, p, scene

K = "soana.partner."
SHARE = "soana.partner_stance.share"
EXCLUSIVE = "soana.partner_stance.exclusive"
SECRET = "soana.partner_stance.secret"
DECIDED = K + "agreed"
PURSUED = K + "pursued"
HELD = K + "held"
BURIED = K + "buried"
CONFIRMED = K + "corven_known_alive"
TOGETHER = K + "corven_together"
SEPARATED = K + "corven_separated"
DISTANT = K + "corven_distant"
EXPOSED = K + "affair_exposed"
BROKEN = K + "romance_ended"
CHOSEN = K + "exclusive_chosen"
CAREFUL = K + "bundle_hidden"
QUIET_RETURN = K + "quiet_homecoming"
RETURNED = "soana.trickster.returned"
LOSS = ("soana.dead", "soana.killed_by_camellia", "soana.forest_dead")
ACTOR = "64805abb52739e44280a758f850b300c"
WINTERSUN = "0a5654e7dc18f074d9356009d55eb51b"


def commitments(scenes):
    """Append stance branches; retain each old committing answer and its target.

    Original effects, including the knot and second asking's prices, occur only
    on acceptance. An exclusivity demand neither cuts the knot nor buys a die.
    No scene eligibility, presence or payoff guard changes here.
    """
    for event in scenes:
        for page in list(event["Nodes"]):
            old = [deepcopy(a) for a in page["Choices"] if "soana.committed" in a["Set"]]
            if not old:
                continue
            for answer in page["Choices"]:
                if "soana.committed" in answer["Set"]:
                    answer["Requires"].append(DECIDED)
            suffix = page["Id"]
            share, exclusive, secret = ("partner_" + x + "_" + suffix for x in ("share", "exclusive", "secret"))
            page["Choices"].extend((
                c('"Keep Corven\'s place. If he comes home, we tell him what we are to each other."', share,
                  forbids=(DECIDED,)),
                c('"If I stay, you end your marriage to Corven. I will not share you."', exclusive,
                  forbids=(DECIDED,)),
                c('"I want you. Let Corven and everyone else believe I only come for your counsel."', secret,
                  forbids=(DECIDED,)),
            ))
            share_answers, secret_answers = [], []
            for original in old:
                for stance, destination in ((SHARE, share_answers), (SECRET, secret_answers)):
                    answer = deepcopy(original)
                    answer["Set"].extend((stance, DECIDED))
                    destination.append(answer)
            if event["Id"] == "soana.the_days_she_counted":
                parting = next(x for x in event["Nodes"] if x["Id"] == "part_as_friends")
                refusal = deepcopy(parting["Choices"][0])
                refusal["Text"] = '[Leave the place beside her blanket. Remain her friend.]'
                refusal["Set"].append(EXCLUSIVE)
            elif event["Id"] == "soana.trickster.returned.terms":
                refusal = c('[Accept her refusal. Remain a friend.]', "partner_exclusive_end_" + suffix)
            elif event["Id"] == "soana.trickster.missed.bowl":
                refusal = c('[Accept her refusal. Leave the die, and the bed.]', "partner_exclusive_end_" + suffix)
            else:
                refusal = c('[Leave. She has refused your demand.]',
                            flags=(EXCLUSIVE, "soana.closed", "soana.trickster.refused"))
            event["Nodes"].extend((
                n(share, "Soana", '''{n}Soana keeps hold of your wrist. Her thumb stops moving.{/n}
"Corven is my husband. I have no news of him. If he comes home, he comes home to his house, and he hears it from me. You will stand there too, hunter. No slipping out while I answer for both of us."
{n}She draws your hand against her throat.{/n}
"He may want neither of us afterwards. I will hear him. Until then, you have a place here. You have not taken his."''',
                  *share_answers, portrait="Soana"),
                n(exclusive, "Soana", '''{n}She releases your wrist. Her hand closes on the old clasp at her throat.{/n}
"End it with whom? A man whose road I do not know? Shall I shout into the trees and call myself unmarried when nothing answers?"
{n}She pushes your bundle away from the blanket.{/n}
"He gave me flowers. We had children. You do not buy that out of me with a promise to stay. I wanted your mouth, bloody hunter. I did not ask you to pull his name out by the roots."
{n}She pushes the bundle farther from the blanket.{/n} "No. You shall have no lover here on those terms."''',
                  refusal, portrait="Soana"),
                n(secret, "Soana", '''{n}Her fingers tighten on your belt, then loosen. She looks past you at the bark bearing her husband's name.{/n}
"Counsel. Is that what you will call it when you leave my blanket with a bite on your neck?"
{n}She pulls you nearer anyway.{/n}
"I want you. Enough to do this foolish thing. No boasts at the soldiers' fire. And if Corven asks me, I shall have to look him in the face. You will not answer for me."
{n}Her mouth brushes yours, impatient and bitter.{/n} "Put that fine lying tongue to another use while I can bear it."''',
                  *secret_answers, portrait="Soana"),
            ))
            if refusal.get("Next"):
                friend = deepcopy(next(x for x in event["Nodes"] if x["Id"] == "friend"))
                friend["Id"] = refusal["Next"]
                for answer in friend["Choices"]:
                    answer["Set"].extend((EXCLUSIVE, "soana.trickster.friends"))
                event["Nodes"].append(friend)

    # Two existing postwar invitations also narrate a commitment, without
    # writing COMMITTED. Keep their eligibility and payoff flags intact; ask
    # about Corven before their existing romantic continuation is shown.
    late = {"soana.trickster.epilogue.commit", "soana.trickster.epilogue.luck_late"}
    responses = {}
    for event in scenes:
        for page in event["Nodes"]:
            for stance in ("share", "exclusive", "secret"):
                if page["Id"].startswith("partner_" + stance + "_"):
                    responses.setdefault(stance, deepcopy(page))
    for event in scenes:
        if event["Id"] not in late:
            continue
        page = event["Nodes"][0]
        original = deepcopy(page["Choices"][0])
        # Accounting and paid debts remain visible before the answer. Only
        # the final new cord / bed invitation waits for an accepted stance.
        future = []
        if event["Id"] == "soana.trickster.epilogue.commit":
            future = [deepcopy(page["Paragraphs"][4])]
            page["Paragraphs"][4]["Requires"].append(DECIDED)
            page["Paragraphs"][4]["Forbids"].append(EXCLUSIVE)
        # The saved exit leaves without settling any relationship terms.
        page["Choices"][0]["Id"] = "continue"  # saves reference the legacy .continue epilogue answer
        for name, stance, text in (
            ("share", SHARE, '"Keep Corven\'s place. If he comes home, we tell him what we are to each other."'),
            ("exclusive", EXCLUSIVE, '"If I stay, you end your marriage to Corven. I will not share you."'),
            ("secret", SECRET, '"I want you. Let Corven believe I only come for your counsel."'),
        ):
            response = deepcopy(responses[name])
            response["Id"] = "partner_" + name + "_start"
            continuation = deepcopy(original)
            if stance == EXCLUSIVE:
                continuation["Text"] = '[Leave. She has refused your demand.]'
                continuation["Set"].extend(("soana.closed", "soana.trickster.refused"))
            else:
                response["Paragraphs"] = deepcopy(future)
                continuation["Set"].extend((stance, DECIDED))
                continuation["Id"] = "continue"
            response["Choices"] = [continuation]
            page["Choices"].append(c(text, response["Id"], flags=() if stance == EXCLUSIVE else (stance, DECIDED), forbids=(DECIDED,)))
            event["Nodes"].append(response)

    # Authored choice to end her vows, never proof that the absent husband died
    # or accepted them. The existing work earns her willingness to choose again.
    for event in scenes:
        pages = {page["Id"]: page for page in event["Nodes"]}
        for refusal in list(event["Nodes"]):
            if not refusal["Id"].startswith("partner_exclusive_") or "_end_" in refusal["Id"]:
                continue
            key = refusal["Id"]
            share = key.replace("exclusive", "share", 1)
            secret = key.replace("exclusive", "secret", 1)
            if share not in pages or secret not in pages:
                continue
            refusal["Choices"][0]["Set"] = list(dict.fromkeys((*refusal["Choices"][0]["Set"], EXCLUSIVE, DECIDED)))
            for page in list(event["Nodes"]):
                for answer in page["Choices"]:
                    if answer.get("Next") == key:
                        answer["Next"] = key + "_answer"
            refusal["Choices"].extend((
                c('"Then I withdraw it. Keep his place, and mine if you still want me."', share),
                c('"Keep our nights secret instead."', secret)))
            refusal["Text"] += '\n{n}She waits, still holding your bundle.{/n} "Back down, and I shall still pull you under the blanket. His clasp stays on my throat. You will feel it."'
            proof, other = "soana.late_thorn_tested", "soana.trickster.accounting_invited"
            event["Nodes"].append(n(key + "_answer", "Soana", '''{n}Soana lays her hand over the old clasp. Outside the cave, the watch calls that the demon tracks lead north.{/n}
"You want an answer about the years before you. Let me think."''',
                c('[Wait for her answer.]', key + "_chosen", requires=(proof, "trickster.now")),
                c('[Wait for her answer.]', key + "_chosen", requires=(other, "trickster.now"), forbids=(proof,)),
                c('[Wait for her answer.]', key, forbids=(proof, other)),
                c('[Wait for her answer.]', key, requires=(proof,), forbids=("trickster.now",)),
                c('[Wait for her answer.]', key, requires=(other,), forbids=(proof, "trickster.now",)), portrait="Soana"))
            accepted = deepcopy(pages[share]["Choices"])
            for answer in accepted:
                answer["Set"] = [flag for flag in answer["Set"] if flag != SHARE]
                answer["Set"].extend((EXCLUSIVE, DECIDED, CHOSEN))
            event["Nodes"].append(n(key + "_chosen", "Soana", '''"You stayed to do the work when the forest had nothing pretty to give you. I wanted you back after it. That was my doing."
{n}She unfastens the clasp and sets it beside the bark bearing Corven's name.{/n}
"I shall write that I have chosen another lover, and ended my vows. Send it south with the scouts. No pretending the silence is his answer. I don't know whether he can hear it."
{n}She presses your hand to the bare place at her throat.{/n}
"Our children will hear my words too. You stay when they curse me. If Corven comes, I answer him myself. I will not hide behind your fine coat."''', *accepted, portrait="Soana", paragraphs=deepcopy(pages[share].get("Paragraphs", []))))

    # The safe affair carries no discarded shirt for the returning family to find.
    for event in scenes:
        for page in event["Nodes"]:
            if not page["Id"].startswith("partner_secret_"):
                continue
            if event["Id"].startswith("soana.trickster.") and not event["Owner"].endswith("Epilogue"):
                page["Choices"].append(c("[Leave.]", forbids=("trickster.now",), abort=True))
            page["Text"] += '\n"Take your bundle when you go. No second bed laid out for the whole forest to see. I shall have to wait until you return to smell you again."'
            for answer in list(page["Choices"]):
                if answer.get("Abort"):
                    continue
                private = deepcopy(answer)
                private.pop("Id", None)
                private["Text"] = '[Take your bundle after every visit. Leave no second bed.]'
                private["Set"].append(CAREFUL)
                page["Choices"].append(private)


def cave(id, title, entry, nodes, requires, *, any_groups=(), delay=0, forbids=()):
    return scene(K + id, title, "Soana", 3, entry, nodes, Relationship="soana",
                 Chapters=[3, 5], last=5, ContactUnit=ACTOR, Areas=[WINTERSUN],
                 AnswerLists=["2b1776f3e398685479ff6b16290b4cc2"],
                 requires=(*requires, "soana.after_quest"),
                 forbids=(*LOSS, RETURNED, "soana.closed", "inhuman", *forbids), delay=delay, optional=True,
                 RequiresAnyGroups=[list(g) for g in any_groups])


SCENES = [
    cave("dispatch", "A name on the southern road", '"A captive courier has a letter addressed to you."', [
        n("start", "Narrator", '''{n}The courier taken on the Wintersun road carried cult orders and a sack of ordinary letters. His oath forbade him to leave a message undelivered. You gave him Soana's address and made him carry this one ahead of his master's orders. The crusade's scouts followed him back to his relay.{/n}
{n}The letter came through a relay near Gundrun. An old dwarf asks after a shaman, her children, and a meadow where they were married. He signs himself Corven. The hand is cramped, the ink fresh. The scouts have not seen its writer.{/n}''',
          c('[Give Soana the letter.]', "read"),
          c('[Keep the letter with your dispatches until after the fighting.]', flags=(HELD,)),
          c('[Burn the letter. Leave Corven looking for an answer.]', "burn")),
        n("read", "Soana", '''{n}She reads it standing. Then she sits, still holding it above her knees.{/n}
"That fool used to make his letters so small I needed the sun to read them. This could be his hand. It could be something that has seen his hand."
{n}She touches a crooked word.{/n}
"Ask about the flowers. Not their color. Ask what he called me when I threw the wreath at him. If he knows, bring him a road he can walk. The demons have had enough of my people."''',
          c('[Send her question south and pay for an escort if the answer is his.]', "sent",
            crusade=("Finances", -75), flags=(PURSUED,)),
          c('"I will keep it safe. The southern roads must wait."', flags=(HELD,))),
        n("sent", "Soana", '''{n}Soana writes her question under his cramped lines. She gives the messenger dried fish and stands watching until he has passed the bend.{/n}
"If it is him, do not bring him here thinking he owes you his wife. I have words for him. He will have words for me."''',
          c('[Tell him about your arrangement with Soana in the same dispatch.]', "sent_share", requires=(SHARE,)),
          c('[Send only the question. Conceal the affair.]', requires=(SECRET,)),
          c('[Send her separation with the question. He hears her choice before he comes.]', "sent_exclusive", requires=(EXCLUSIVE, CHOSEN))),
        n("sent_share", "Soana", '''{n}She takes the sheet back and writes beneath the question. Her hand presses hard enough to score the bark.{/n}
"There. My words. You have a lover waiting here, and I have a husband waiting south. Neither is going to hear about the other from a fool on the road."
{n}She folds it over both messages and gives it to the messenger herself.{/n}''', c()),
        n("burn", "Narrator", '''{n}The cramped letters curl into ash. Beneath the address is a smaller line asking that undelivered letters be returned to the southern relay. The courier's oath still holds; he saw where this one went.{/n}
{n}You scatter the ash. Soana's unanswered bark lies beside her blanket.{/n}''',
          c('[Leave the ash cold.]', flags=(BURIED,))),
        n("sent_exclusive", "Soana", '''{n}She copies the separation beneath her question about the flowers.{/n}
"Both sheets. No making him walk north expecting a wife who has taken off his clasp."
{n}She gives the messenger the folded letter herself.{/n} "If he wants to come and curse me, he has a road. I will hear him."''', c(), portrait="Soana"),
    ], ("trickster.now", "trickster.ever", "soana.committed"),
       any_groups=((SHARE, SECRET, EXCLUSIVE),), forbids=(PURSUED, HELD, BURIED)),
    cave("homecoming", "At his own door", '"The southern messenger has returned with your answer."', [
        n("start", "Soana", '''{n}An elderly dwarf stands at the cave mouth with a walking staff. Behind him, a dwarf with gray in his beard sets down his father's pack. Soana looks from Corven to their son. Below the bend, the escort keeps watch for demons.{/n}
"Well? What did you call me?"
{n}Corven's mouth twists.{/n} "A thorn bush in a wedding wreath. You threw it again."
{n}She crosses the last steps herself. He catches her, awkwardly; neither lets go quickly.{/n}
"You found the road," {n}she says against his coat.{/n} "Bloody fool."
"Your answer found me. I had stopped expecting one."
{n}He looks toward the blanket. Soana turns in his arms to face you.{/n}''',
          c('[Stay to hear Corven\'s answer to your arrangement.]', "share", requires=(SHARE,)),
          c('[The affair has reached his own door.]', "discovery", requires=(SECRET,), forbids=(CAREFUL,)),
          c('[Leave them alone. Your bundle is packed; no second bed is laid out.]', "hidden", requires=(SECRET, CAREFUL)),
          c('[Put your bundle beside her blanket. Stay at her door tonight.]', "discovery", requires=(SECRET, CAREFUL)),
          c('[Hear his answer to the separation she sent.]', "exclusive", requires=(EXCLUSIVE, CHOSEN))),
        n("share", "Corven", '''"Her letter told me. A hunter at her fire, and in her bed. You had better have heard the same words I did."
{n}He puts his staff down. His fingers shake as he works the strap of his pack.{/n}
"I have spent years wondering whether she had a fire at all. Now I find it warm, and somebody else's boots beside it. I will not thank you for that."
"I will stay if she still wants her husband. I will not lie beside you while you take her. And no child of ours carries messages between your beds. Tell me yourselves."
{n}Their son folds his arms.{/n} "I brought Father through the Wound. I am not carrying either of you to the other's blanket. Write your own damned letters."''',
          c('"You hear it from us. Your marriage and your bed remain yours."', "together"),
          c('"I cannot live by those terms."', "leave")),
        n("together", "Soana", '''"I want you here, Corven. Put the pack down before you shake the pot off its stone."
{n}She takes it from him. He catches her free hand.{/n}
"And you still want the hunter?" {n}Corven asks.{/n}
{n}Soana meets his gaze.{/n} "Yes."
{n}He closes his eyes, then nods once.{/n}
"Then I shall curse both of you when I need to. My door is not a barracks door. Knock."
"You may start with me," {n}Soana says.{/n} "I have kept you outside it long enough."
{n}She sets out three cups. Corven takes the one nearest his pack. His hand has not stopped shaking.{/n}''',
          c('[Leave them the evening together. Return by the terms you accepted.]', flags=(TOGETHER,))),
        n("leave", "Soana", '''{n}She puts your bundle in your arms.{/n}
"Then take your things. You asked to hear him. You have heard him."
{n}Corven makes room at the entrance. He gives you no farewell. Soana goes back to the pot, rubbing the old clasp between her fingers.{/n}''',
          c('[Leave her with her husband.]', flags=(TOGETHER, BROKEN, "soana.closed", "soana.trickster.refused"))),
        n("discovery", "Corven", '''{n}Corven lifts your bundle. Your shirt unfolds across his hands. Soana reaches for it; he holds it away.{/n}
"Your counsel? That was the word on the road. Does counsel need a place in my wife's bed?"
{n}He looks at the place kept beside her blanket. She does not move your bundle away.{/n}
"I took the hunter for my lover, Corven. I wanted it. I let you go on writing to a wife who would not answer."
{n}Their son turns toward her.{/n} "You answered neither of us. I thought the forest had taken you."
{n}Corven's grip tightens on the shirt.{/n} "And you let me walk all this way to find the answer in my own house."
{n}He drops the shirt at your feet.{/n}
"I would have heard you. Do not tell me now what I might have said. You never asked."''',
          c('"It was an affair. I knew whose place I was taking."', "separated"),
          c('[Lie] "She is only my teacher."', "lie")),
        n("lie", "Soana", '''"No."
{n}Soana picks up your shirt and pushes it into your hands.{/n}
"I will not hear that filthy little word again. You are my lover. I pulled you here. Corven heard it from my mouth."
{n}Her husband takes his staff. His knuckles are white against the wood.{/n}''', c('[Hear what follows.]', "separated")),
        n("separated", "Corven", '''"I am going south. There is still a place for me there. You will hear where. Our children will hear why."
{n}Soana takes a step after him. He stops her with an open hand.{/n}
"I came for my wife. Keep the wreath, if you kept it. I have no use for it now."
{n}Their son takes his father's pack and goes with him to the escort. He does not look at you. Soana stays at the bend until Corven's staff can no longer be heard. When she turns back, she points at your bundle.{/n}
"You too. I will write him a proper answer. I cannot do it with your smell in my blanket."
{n}She folds the blanket away. Her hands fumble at the corners.{/n}''',
          c('[Take your things. Neither marriage nor romance survives the lie.]',
            flags=(SEPARATED, EXPOSED, BROKEN, "soana.closed", "soana.trickster.refused"))),
        n("hidden", "Soana", '''{n}Corven sets his pack beside the one blanket. His son goes down to the escort. Soana waits until he is out of earshot.{/n}
"A hunter helped on the roads," {n}she tells her husband.{/n}
"So I heard. I shall thank the hunter when I've had some sleep."
{n}She keeps her hands on the pot. She gives you no kiss at the door.{/n} "Go. We have years to talk about."
{n}Outside, you pick up the bundle you never left beside her bed.{/n}''',
          c('[Leave her with Corven. Keep future visits away from his house.]', flags=(CONFIRMED, QUIET_RETURN)), portrait="Soana"),
        n("exclusive", "Corven", '''"I read your letter. You ended your vows. I thought I should hear you say it."
{n}Soana lays the clasp on the stone.{/n} "I chose the hunter. I have ended them."
"Years looking for a road home. And this is what's at the end of it."
{n}Their son takes his father's pack. He turns on Soana.{/n} "You could have told us before he started walking."
"I have told you now," {n}she says. Her hand stays on the stone.{/n}
{n}Corven picks up the clasp.{/n} "Then I am no longer your husband. Keep your hunter. I shall hear any news of you from the children. No more letters calling me home."
{n}Soana waits until he has gone down to the escort. Then she turns to you.{/n} "You heard them. No telling me it will all come right. Stay, if you meant it."''',
          c('[Stay beside her after the family leaves.]', flags=(SEPARATED, CONFIRMED)), portrait="Soana"),
    ], ("trickster.ever", "soana.committed", PURSUED),
       any_groups=((SHARE, SECRET, EXCLUSIVE),), delay=168, forbids=(CONFIRMED,)),
    cave("returned_letter", "The undelivered answer", '"The courier came back to your cave?"', [
        n("start", "Soana", '''{n}Soana holds two letters. One bears the courier's mark; the other is cramped with small writing. She points at the bundle of demon reports under your arm.{/n}
"Your army can wait until you have heard this."
{n}She holds up the courier's sheet.{/n} "He had to return an undelivered letter. His oath, hunter. Your joke. He went south with word that mine had reached your hand and come no farther."
{n}She holds up the smaller sheet.{/n}
"Corven wrote about the flowers. He called me a thorn bush in a wedding wreath. Nobody else heard that quarrel. It is him. Alive, south of the Wound, still writing."
"And you burned the road he sent me."''', c('[Hear the rest of Corven\'s letter.]', "corven")),
        n("corven", "Narrator", '''{n}She reads the cramped words aloud.{/n}
"'The courier says your hunter burned my letter. So you have a fire, a hunter, and someone to decide who reaches you. Is that what you wanted? Tell me yourself, Soana. I have waited long enough for other people's news.'"
{n}She lowers the letter. Her face has gone stiff.{/n}''',
          c('"I burned it to keep you for myself."', "verdict"),
          c('[Lie] "The courier burned it."', "caught")),
        n("caught", "Soana", '''"He watched you do it. He carried the ash back with his report."
{n}She drops the courier's letter beside your boots.{/n}
"Read it. Then take your things. I shall not have you sorting my husband's words into the fire."''', c('[Take your things.]', "verdict")),
        n("verdict", "Soana", '''{n}Soana puts your bundle outside the cave. The clasp at her throat has turned backward; she does not notice.{/n}
"I wanted your hands on me. I did not give you his letters to burn. He is alive. He will know what I did with you, from me. Our children will hear from me too."
{n}She points toward the path.{/n} "Whatever he answers, I have answered you."
{n}She sits by the pot with Corven's letter on her knees. She writes her reply, folds it, and holds it out.{/n}
"Carry this one. Bring back what he says. No burning."''',
          c('[Carry her answer south and bring Corven\'s reply back.]', "answer_share", requires=(SHARE,)),
          c('[Carry her confession south and bring Corven\'s reply back.]', "answer_secret", requires=(SECRET,)),
          c('[Carry the separation south. Let him answer the burned letter too.]', "answer_exclusive", requires=(EXCLUSIVE, CHOSEN))),
        n("answer_share", "Narrator", '''{n}At the southern relay you put Soana's reply in Corven's hands. He reads the account of her lover, then the admission that his first letter was burned. His answer is short. You carry it back unopened. Soana reads it by the cave mouth.{/n}
"'I will speak to you, wife. I will not send another word through the hunter who burned the last ones. The relay knows where to find me. Come yourself, or write by another hand.'"
{n}She puts it inside her shawl, then points at your bundle, still outside.{/n}
"Your last delivery. Take that and go."''',
          c('[Leave. Her marriage awaits his answer; your romance has ended.]',
            flags=(DISTANT, BROKEN, "soana.closed", "soana.trickster.refused"))),
        n("answer_secret", "Narrator", '''{n}At the southern relay you give Corven his wife's confession. He reads it twice. He does not offer you a seat.{/n}
"Tell her I have heard. The hunter in her bed and my words in the fire. Both of you knew whose name she kept. Neither of you troubled to tell me."
{n}He writes his answer while you stand.{/n}
"I am no longer her husband. She can tell the children what she wants. They will hear from me. Carry that too."
{n}At the cave Soana reads his answer. She folds it carefully. Then she picks up your bundle and pushes it into your hands.{/n}
"You have finished here. Go."''',
          c('[Leave with Corven\'s answer delivered. Both bonds have broken.]',
            flags=(SEPARATED, EXPOSED, BROKEN, "soana.closed", "soana.trickster.refused"))),
        n("answer_exclusive", "Narrator", '''{n}At the southern relay Corven reads Soana's separation. His answer fills only half a sheet.{/n}
"Then she has chosen. I am no longer her husband. Tell her I would have heard her without the hunter burning my words first. The children will hear about that too."
{n}Soana reads it at the cave mouth. She holds the answer in one hand, and pushes your bundle into your arms with the other.{/n}
"I took off his clasp. I did not put you in charge of who could write to me. Take your things."
{n}She goes inside without waiting for your answer.{/n}''',
          c('[Leave. The marriage has ended; burning his letter cost you the romance.]', flags=(SEPARATED, BROKEN, "soana.closed", "soana.trickster.refused"))),
    ], ("trickster.ever", "soana.committed", BURIED),
       any_groups=((SHARE, SECRET, EXCLUSIVE),), delay=72, forbids=(CONFIRMED,)),
]

# Record identity and disposition together. An interrupted conversation must
# neither retire its own continuation nor leave CONFIRMED without an ending state.
for event in SCENES:
    for page in event["Nodes"]:
        for answer in page["Choices"]:
            if set(answer["Set"]) & {TOGETHER, SEPARATED, DISTANT}:
                answer["Set"].append(CONFIRMED)

# A native living Soana and her earned return have different dialogue hosts.
# The returned unit uses her existing authored presence, never the dead native list.
for native in list(SCENES):
    returned = deepcopy(native)
    returned["Id"] += ".returned"
    returned["AnswerLists"] = []
    returned["InteractionHub"] = "soana.presence"
    returned["Requires"].remove("soana.after_quest")
    returned["Requires"].append(RETURNED)
    returned["Forbids"].remove(RETURNED)
    returned["ForbidOverrides"] = {f: RETURNED for f in LOSS}
    SCENES.append(returned)


def paragraphs(*, lost=False, aeon=False):
    if aeon:
        # These are receipts from the erased history, never a new-world return.
        return (
            p("{n}In the vanished history, Corven's fate had remained unknown. His unanswered bark and their children's "
              "names had stayed beside Soana's blanket. No word of that marriage reached the vanished traveler.{/n}",
              forbids=(CONFIRMED,)),
            p("{n}Corven had come home and agreed to keep his marriage, with his own bed and no messages carried by their "
              "children. That answer belonged to the erased history; no news of him came from the world without the Wound.{/n}",
              requires=(TOGETHER,)),
            p("{n}Corven had ended the marriage after hearing about the affair and gone south. Their children had heard "
              "both accounts. The erased world's separation told the vanished traveler nothing of this world's marriage.{/n}",
              requires=(SEPARATED,)),
            p("{n}Before the history vanished, Corven had been alive in the south, waiting to hear from Soana herself. "
              "That unanswered marriage left no message for the traveler who had erased the Wound.{/n}", requires=(DISTANT,)),
            p("{n}The promise to face Corven together and tell the truth belonged to the Commander and Soana. "
              "It was erased with their visits.{/n}", requires=(SHARE,)),
            p("{n}Soana's answer to the Commander's demand to end her marriage belonged to the vanished history. "
              "Neither that answer nor her desire told the traveler what she had chosen in this world.{/n}", requires=(EXCLUSIVE,)),
            p("{n}Corven's return to a house without evidence of the affair belonged to the erased history. It told the traveler nothing of this world's marriage.{/n}", requires=(QUIET_RETURN,)),
            p("{n}The Commander had chosen an affair hidden behind a shaman's counsel. Its secrecy belonged to the "
              "vanished visits; there was no account of their consequences in the new history.{/n}", requires=(SECRET,)),
            p("{n}No arrangement with the Commander had been settled before the history vanished. "
              "Corven's marriage had not been surrendered to the vanished traveler.{/n}",
              forbids=(SHARE, EXCLUSIVE, SECRET)),
        )
    unknown = p("{n}The bark addressed to Corven remained among Soana's possessions. No answer had reached it. "
                "Corven's fate was still unknown; the names of their children stayed inside the fold.{/n}",
                forbids=(CONFIRMED,))
    together = p("{n}Corven had come home and heard the truth. He had agreed to keep their marriage, with his own bed "
                 "and no messages passed through their children. Those terms had never been withdrawn.{/n}",
                 requires=(TOGETHER,))
    if lost:
        together = p("{n}Corven had come home and kept their marriage after hearing about the Commander. Now his wife was dead. "
                     "He took the bark bearing his name south, with the news for their children.{/n}", requires=(TOGETHER,))
    separated = p("{n}Corven had ended the marriage after hearing that Soana had chosen the Commander. He was living in the south; "
                  "their children heard his account as well as Soana's. His letters no longer called her wife.{/n}", requires=(SEPARATED,))
    distant = p("{n}Corven was alive in the south. After the burned letter came to light, Soana had written him the truth. "
                "No answer accepting it had come back. He remained her husband, far from her fire.{/n}", requires=(DISTANT,))
    if lost:
        distant = p("{n}Corven was last known alive in the south. Soana's reply about the burned letter had gone there; "
                    "now another message carried the news of her death. There was no answer to either.{/n}", requires=(DISTANT,))
    return (unknown, together, separated, distant,
            p("{n}Corven had come home to one blanket. The Commander had taken the second bundle away after every visit; nothing at the door had betrayed the affair. Soana had kept her husband home and sent her hunter away from the house. She had not told Corven the truth.{/n}", requires=(QUIET_RETURN,)),
            p("{n}The Commander had agreed to speak openly if Corven returned. While there was no news, his place was kept, "
              "and the arrangement could promise no answer on his behalf.{/n}", requires=(SHARE,), forbids=(CONFIRMED,)),
            p("{n}The Commander had demanded Soana end her marriage. She had refused. Corven's name stayed; "
              "the demand had bought no claim on his wife.{/n}", requires=(EXCLUSIVE,), forbids=(CHOSEN,)),
            p("{n}Soana had taken off Corven's clasp and sent her separation south with the scouts. She held the Commander to the promise to hear any answer beside her. Her choice had bought no blessing from her family.{/n}", requires=(EXCLUSIVE, CHOSEN)),
            p("{n}The visits had been an affair, hidden behind talk of a shaman's counsel. Corven had not known, "
              "and the bark addressed to him had stayed under its weight through every secret visit.{/n}", requires=(SECRET,), forbids=(EXPOSED,)),
            p("{n}The affair had been exposed. Soana had sent the Commander away; the second blanket was folded out of reach.{/n}",
              requires=(SECRET, EXPOSED)),
            p("{n}A letter signed Corven had been kept among the Commander's dispatches. Its writer had never been verified, "
              "and Soana had heard nothing of it.{/n}", requires=(HELD,), forbids=(CONFIRMED,)),
            p("{n}A letter signed Corven had been burned before Soana could read it. The courier's unanswered report remained "
              "on the southern road; no proof of its writer's fate had reached her.{/n}", requires=(BURIED,), forbids=(CONFIRMED,)),
            p("{n}No arrangement with the Commander had been settled. Corven remained her husband; "
              "nothing had been agreed on his behalf.{/n}", forbids=(SHARE, EXCLUSIVE, SECRET)))


LOSS_ENDINGS = {"soana.ending_native_loss", "soana.ending_unfinished_loss",
                "soana.trickster.epilogue.luck_lost", "soana.trickster.epilogue.by_your_hand"}


def endings(scenes):
    for event in scenes:
        if event.get("Relationship") != "soana" or not event["Owner"].endswith("Epilogue"):
            continue
        for page in event["Nodes"]:
            page.setdefault("Paragraphs", []).extend(deepcopy(paragraphs(
                lost=event["Id"] in LOSS_ENDINGS, aeon=event["Owner"] == "AeonEpilogue")))


def finish_normal_endings(scenes):
    """Keep registered ending paragraphs ahead of the new continuity tail.

    The Trickster integrator adds the existing winter debts after the normal
    route loads. Only our appended paragraphs move; their old slots stay intact.
    """
    for event in scenes:
        if not event["Id"].startswith("soana.ending_"):
            continue
        tail = paragraphs(lost=event["Id"] in LOSS_ENDINGS,
                          aeon=event["Owner"] == "AeonEpilogue")
        for page in event["Nodes"]:
            current = page.get("Paragraphs", [])
            appended = [entry for entry in current if entry in tail]
            page["Paragraphs"] = [entry for entry in current if entry not in tail] + appended


BROKEN_EPILOGUE = scene(K + "epilogue.broken", "The bundle outside", "Epilogue", 0, "", [
    n("start", "Narrator", '''{n}Soana had sent the Commander away. When visitors asked after the second bundle at her fire, she pointed them down the path. Her letters went south instead of to Drezen.{/n}''',
      paragraphs=paragraphs())], requires=(BROKEN,), forbids=(*LOSS,),
    ForbidOverrides={f: RETURNED for f in LOSS}, Relationship="soana", last=99)


def lastcall():
    """Amend only Soana's route-owned entry before the shared emitter copies it."""
    from storylines import lastcall_partners
    record = next(x for x in lastcall_partners.PARTNERS if x["key"] == "soana")
    # Idempotent across test builds; do not accumulate paragraphs in module state.
    tail = paragraphs()
    if not any(x.get("Text") == tail[0]["Text"] for x in record["paragraphs"]):
        record["paragraphs"] = (*record["paragraphs"], *deepcopy(tail))

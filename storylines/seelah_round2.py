"""Authored Seelah situations from the round-2 sheets, not native romance.

Reservation: act_before_confession / Drezen list reckoning and borrowed room.
The list and first-coin receipts collect her existing terms, never buy desire.
No echo, partner invention, new price, attraction score or mandatory outing.
"""
import copy

from story_format import c, n, p, scene

HUB = "417fa384f3250634bb71859fbc913453"
DREZEN = "2570015799edf594daf2f076f2f975d8"
NPC = "90481a29cc75f424b9891a55c6dcbb53"
FYE = "0f12118177d102f428a3b30b15b132eb"
FYE_HUB = "9b15b09c244076047b02f317e55ef5e3"  # BartenderFye/AnswersList_0021
LOCATOR = "e077da41-372d-4b63-a6cb-b4aed6099291"
PREFIX = "seelah.trickster."
HOLDS = PREFIX + "cost.holds_her_death"
KEEPS = PREFIX + "cost.keeps_it"
GIVEN = PREFIX + "death_returned"
ROBBED = PREFIX + "cost.robbed_back"
SETTLED = PREFIX + "list_settled"
GAME = PREFIX + "list_game"
COIN_NO = PREFIX + "stones_declined"
COIN_PAID = PREFIX + "first_coin_paid"
FREEDOM_NO = PREFIX + "freedom_declined"
LIST_NO = PREFIX + "list_declined"
PRICE_NO = PREFIX + "price_refused"
CUSTODY = PREFIX + "custody_clear"


def node(s, id):
    return next(n for n in s["Nodes"] if n["Id"] == id)


def add_flag(answer, flag):
    if flag not in answer["Set"]:
        answer["Set"].append(flag)


def add_cut(s, old_id, before, cut, after):
    """Append staging/slot nodes; preserve old node, answers and terminal effects.

    Old saves inside the legacy node still have their original exits. Incoming
    edges now stage the encounter before that same aftermath/exit node.
    """
    sid = s["Id"] + ".explicit.1"
    staging = sid + ".approach"
    for page in s["Nodes"]:
        for answer in page["Choices"]:
            if answer.get("Next") == old_id:
                answer["Next"] = staging
    node(s, old_id)["Text"] = after
    # Explicit brief: see tools/route_packs/explicit_slots/seelah/<sid>.json.
    s["Nodes"].extend([
        n(staging, "Seelah", before, c('[Draw her close.]', sid), portrait="Seelah"),
        n(sid, "Narrator", cut, c('[Stay with her.]', old_id), portrait="Seelah"),
    ])


def custody_gate(s):
    s.setdefault("Requires", []).append(CUSTODY)


def prepare(scenes, presences, derived):
    """Apply to this route's source scenes before the expansion copies them."""
    by = {s["Id"]: s for s in scenes}
    derived[CUSTODY] = [["availability.observed"]]
    derived[PREFIX + "no_romance"] = [["availability.observed"]]
    # Verified EtudeBracketSetCompanionPosition locator in both native Drezen
    # LeadershipSeelahRankUpPosition / MilitarySeelahRankUpPosition blueprints.
    presences["seelah.presence"]["At"] = dict(Locator=LOCATOR, Offset=[0.0, 0.0])
    presences["seelah.presence"]["Forbids"] = ["seelah.closed", "seelah.revived", "seelah.plot_departed"]
    presences["seelah.presence"]["Greeting"] = (
        '{n}Seelah waits by the crusade notices, her pack at her feet.{/n} '
        '"There you are. Walk with me. Fye still owes me a decent drink."')
    # A living carrier waits at Fye's existing native dialogue. She is authored
    # staging in that conversation, not a Seelah spawn awaiting its own return.
    # No new presence type or exception to Seelah's death guard is needed.
    for suffix in ("reply", "arrival"):
        s = by["seelah.trickster.dead.effects_" + suffix]
        s.pop("Remote", None)
        s.update(ContactUnit=FYE, AnswerLists=[FYE_HUB],
                 Areas=[DREZEN], Entry='"Fye, did the courier come back?"')
        s.pop("Kind", None)
    node(by[PREFIX + "dead.effects_reply"], "start")["Text"] = (
        '{n}Fye points to the courier waiting beside the door. She holds out a note, '
        'its seal protected beneath a fold of oilcloth. '
        'Mud has dried on her boots all the way to the knees.{/n} '
        '{n}"Four days in the saddle. The chaplain put this in my hand himself."{/n}')
    node(by[PREFIX + "dead.effects_arrival"], "start")["Text"] = (
        '{n}When you next find the courier, she points across the yard. '
        'Seelah stands beside the crusade notices, leaning on her sword. She lifts '
        'one hand when she sees you, palm open.{/n}\n'
        '{n}"She walked the last stretch," the courier says. "Wouldn\'t ride behind me."{/n}\n'
        '"My list, Commander. And a drink. In that order."')
    # The dependable physical locator replaces the extra mailbag chain. Keep all
    # fallback IDs and nodes, including their old answer destinations.
    for s in scenes:
        if s["Id"].endswith("_visit") or s["Id"] == PREFIX + "dismissed.back_for_the_papers_letter":
            s["Forbids"].append(PREFIX + "in_drezen")
    node(by[PREFIX + "dismissed.back_for_the_papers"], "start")["Text"] = (
        '{n}Seelah catches you by the crusade notices. She holds out her hand before '
        'you can greet her. Only after you stop does she lead you to Fye\'s table by the door.{/n}')
    caught = by[PREFIX + "dismissed.back_for_the_papers"]
    node(caught, "start")["Choices"][1]["Requires"].append(PREFIX + "lift_lesson")
    node(caught, "start")["Choices"].append(c("Continue", "papers_caught_untaught",
        requires=(PREFIX + "cost.caught",), forbids=(PREFIX + "lift_lesson",)))
    node(caught, "papers_caught")["Text"] = (
        '"And you got caught. At the gate! I showed you where to look, Commander. '
        'Perhaps I should have spent more time on what to leave alone."')
    caught["Nodes"].append(n("papers_caught_untaught", "Seelah",
        '"You tried a pocket lift in front of the whole gate without a lesson? '
        'Wonderful. Next time ask the clerk. Better yet, leave my things alone."',
        c("Continue", "papers"), portrait="Seelah"))
    # V1 intent: a misguided invitation back, answered by her property demand.
    node(by[PREFIX + "dismissed.setup"], "start")["Text"] += (
        '\n{n}One last conversation at the gate, before she takes the road north. '
        'That is what you mean to steal. The papers weigh unpleasantly in your coat.{/n}')
    for suffix in ("commit", "commit_visit"):
        s = by[PREFIX + "dismissed." + suffix]
        for nid, receipt in (("no_stones", COIN_NO), ("no", FREEDOM_NO), ("no_death", LIST_NO)):
            add_flag(node(s, nid)["Choices"][0], receipt)
        node(s, "list_back")["Choices"].extend([
            c('"What is still troubling you?"', "no_stones"),
            c('"Keep it. We can talk about us another evening."', abort=True),
            c('"Keep it. Let us remain friends."', "friend", flags=(PREFIX + "friends",)),
        ])
        # Existing terminal exits stay exactly where they were.
        threshold = node(s, "threshold")["Text"]
        threshold = threshold.replace('"Ha. Got your belt. Old habits."',
            '"Ha! Your belt. Didn\'t even need to apologize."')
        add_cut(s, "threshold", threshold,
            '{n}She pulls you against her, still laughing, then buries the laugh in '
            'a hungry kiss. Her skin is hot under your hands and scarred where the gambeson '
            'rubs it raw, and her breath comes ragged in your ear, saying your name like a thing she '
            'has finally stolen clean. The door stays shut; the next call to muster is hours away.{/n}\n'
            + ('{n}At dawn, Seelah sits beside you and reaches for her boots.{/n}' if suffix == "commit" else
               '{n}Dawn catches Seelah reaching beneath the bed for one of her boots.{/n}'),
            '{n}A soldier knocks on the door: '
            'the road company is mustering. She calls back that she heard, then '
            'kisses you again before answering properly.{/n}' if suffix == "commit" else
            '{n}A soldier '
            'knocks with the muster call. "Heard you!" she shouts, then turns back '
            'for one more kiss.{/n}')
    for suffix in ("second_ask", "second_ask_visit"):
        s = by[PREFIX + "dismissed." + suffix]
        s["Forbids"].append(COIN_NO)
        s.setdefault("ForbidOverrides", {})[COIN_NO] = COIN_PAID
        # Her free return and her custody demand are different refusals. The
        # existing delay is retained; a playable return gives it its receipt.
        price = node(s, "price")
        price["Text"] = ('{n}Seelah stands when you approach. Her pack is by her chair; '
            'nobody has brought her here under orders.{/n}\n'
            '"I came back to hear you ask. My choice. Before you do, there\'s something to settle."')
        old_choices = price["Choices"]
        price["Choices"] = old_choices
        for answer in old_choices:
            answer["Requires"].append(PREFIX + "refusal_answered")
        price["Choices"].extend([
            c('[Hear why she came back.]', "free_return", requires=(FREEDOM_NO,)),
            c('[Give her the list.]', "list_return", requires=(LIST_NO,), forbids=(GIVEN, ROBBED)),
            c('[Acknowledge the returned list.]', "list_acknowledged", requires=(LIST_NO, GIVEN)),
            c('[Acknowledge her reclaimed list.]', "list_acknowledged", requires=(LIST_NO, ROBBED), forbids=(GIVEN,)),
            c('[Leave the question for another evening.]', abort=True),
            c('[Ask her after her first payment.]', "coin_answer", requires=(COIN_NO, COIN_PAID)),
        ])
        node(s, "price")["Choices"][1]["Set"].append(PRICE_NO)
        s["Nodes"].extend([
            n("coin_answer", "Seelah", '{n}She pats the receipt tucked inside her list.{/n}\n'
              '"My first coin is paid. My list is here. I still owe the dead, '
              'but I don\'t owe you a yes. You\'re getting one because I want '
              'another night with you." {n}She gets up, grinning.{/n} '
              '"First, let\'s see what you\'ve got in that coat."',
              c('[Hear her offer.]', "offer", flags=(PREFIX + "refusal_answered",)), portrait="Seelah"),
            n("free_return", "Seelah", '{n}She drops her travel-stained gloves on the table.{/n}\n'
              '"I took my papers north, signed for the posting myself, and came back on leave. '
              'You didn\'t send for me. I wanted to see you. Now you can stop looking so damned relieved."',
              c('[Ask her again.]', "offer", flags=(PREFIX + "refusal_answered",)), portrait="Seelah"),
            n("list_return", "Seelah", '{n}She takes her list, reads it, and puts it inside her tunic.{/n}\n'
              '"Mine. At last. Don\'t make me ask twice for it again. Now, what was it you wanted to say?"',
              c('[Ask her again.]', "offer", flags=(GIVEN, SETTLED, PREFIX + "refusal_answered")), portrait="Seelah"),
            n("list_acknowledged", "Seelah", '{n}She pats the folded list against her ribs.{/n}\n'
              '"Here. Where it belongs. You can ask about us without keeping this between us."',
              c('[Ask her again.]', "offer", flags=(SETTLED, PREFIX + "refusal_answered")), portrait="Seelah"),
        ])
        # Successful pocket game is offered after settlement, in her own terms.
        node(s, "robbed")["Text"] = (
            '{n}She takes your purse, counts its contents, and puts every coin back. '
            'Then she sets it on the table where you can reach it.{/n}\n'
            '"There. No secrets held hostage. Next time I rob you, it\'s for fun." '
            '{n}She catches your collar and kisses you.{/n} "And this is because I want you."')
        add_flag(node(s, "price")["Choices"][0], SETTLED)
        threshold = node(s, "threshold")["Text"]
        add_cut(s, "threshold", threshold,
            '{n}She tosses the belt from her hand and draws you down '
            'into a kiss that leaves no room for another speech. Her heartbeat knocks against your palm, '
            'her breath goes short, and what she says next is not a word anyone could write in a ledger.{/n}\n'
            + ('{n}In the pale light from the window, Seelah begins lacing her boots.{/n}' if suffix == "second_ask" else
               '{n}By dawn, Seelah has found your shirt and is looking for her boots.{/n}'),
            '{n}'
            'The soldier outside knocks twice before she admits to being awake.{/n}'
            if suffix == "second_ask" else
            '{n}'
            'A soldier calls her to muster. She answers with a curse, a laugh, '
            'and a promise to be down in a moment.{/n}')
        # Receipt -> her offer -> embrace. Keep the saved price page and all
        # its choices, but do not send a newly answered refusal back to it.
        offer = n("offer", "Seelah",
            '{n}She comes close and taps your coat.{/n}\n'
            '"Hands at your sides. I take your purse, you try to look surprised, '
            'and every coin goes back. Then upstairs, if you still want me."',
            portrait="Seelah")
        offer["Choices"] = copy.deepcopy(old_choices[:2])
        s["Nodes"].append(offer)
    # Conditional prose stays on epilogue pages; ordinary encounters branch.
    pick = by[PREFIX + "epilogue.pickpocket"]
    # The pickpocket page has two openers before the legacy paragraph tuple;
    # the papers page slices that tuple. Detach both and target by history.
    for ending in (pick, by[PREFIX + "epilogue.papers"]):
        node(ending, "end")["Paragraphs"] = copy.deepcopy(node(ending, "end")["Paragraphs"])
    blocks = node(pick, "end")["Paragraphs"]
    given = next(b for b in blocks if GIVEN in b["Requires"])
    given["Text"] = given["Text"].replace('tied in badly on purpose', 'tied securely')
    unresolved = next(b for b in blocks if KEEPS in b["Requires"])
    unresolved.update(Text='{n}Seelah recovered '
        'her list. The Commander felt the folded paper leave their coat and found '
        'her watching them, hand closed around it. "Warned you," she said. She '
        'kept her account of the Kenabres stones herself.{/n}',
        Requires=[HOLDS],
        Forbids=[GIVEN, ROBBED, SETTLED, "seelah.lastcall.list_returned"])
    reclaimed = next(b for b in blocks if ROBBED in b["Requires"])
    reclaimed.update(Text='{n}Her list stayed against her ribs after she took it '
        'back. The Commander knew where it was. Seelah no longer had to ask.{/n}',
        Forbids=[GIVEN, "seelah.lastcall.list_returned"])
    next(b for b in blocks if "seelah.closed" in b["Requires"])["Requires"].append(PRICE_NO)
    blocks.append(p('{n}The Commander ended their courtship. Seelah left for her '
        'posting with her papers and her own plans. When they met again on crusade '
        'business, she spoke plainly and kept their private evenings to herself.{/n}',
        requires=("seelah.closed", PREFIX + "stay_decided"), forbids=(PRICE_NO,)))
    blocks.append(p('{n}The Commander ended their courtship. Seelah kept her '
        'place among the companions, but no longer sought out their room after '
        'the watch. In battle she still guarded their flank.{/n}',
        requires=("seelah.closed",), forbids=(PRICE_NO, PREFIX + "stay_decided")))
    # The papers ending has its own copies of the sliced legacy paragraphs.
    paper_blocks = node(by[PREFIX + "epilogue.papers"], "end")["Paragraphs"]
    if PRICE_NO not in paper_blocks[5]["Requires"]:
        paper_blocks[5]["Requires"].append(PRICE_NO)
    paper_blocks.extend(copy.deepcopy(blocks[-2:]))
    paper_reclaimed = next(b for b in paper_blocks if ROBBED in b["Requires"])
    paper_reclaimed.update(Text='{n}When she came back to hear the Commander ask '
        'again, Seelah lifted their purse and returned every coin. They went '
        'upstairs together. She took her papers with her when she left.{/n}')
    game = p('{n}Once her own list was safe, Seelah sometimes lifted the '
        'Commander\'s purse on a visit and made them win it back. She returned '
        'every coin; the game belonged to them both.{/n}', requires=(GAME,))
    blocks.append(game)
    refused = by[PREFIX + "epilogue.refused"]
    node(refused, "end")["Text"] = (
        '{n}Seelah had refused the Commander\'s request. She kept the posting '
        'she had chosen and took her sword north. The road companies '
        'continued to hear her laugh over their fires.{/n}')
    node(refused, "end")["Paragraphs"] = [
        p('{n}On leave she returned to Drezen and shared a drink with the Commander. '
          'She had not taken back her no. She had told them what to put right '
          'before asking again. When the company '
          'mustered, she shouldered her pack and went back to it.{/n}',
          requires=(PREFIX + "returned", "seelah.romance")),
        p('{n}Her papers traveled north after her. She had said goodbye; the '
          'Commander had let her go. No private parcel followed.{/n}',
          forbids=(PREFIX + "returned",)),
    ]
    late = by[PREFIX + "epilogue.commit"]
    custody_gate(late)
    text = node(late, "end")["Text"]
    split = text.index('{n}By morning')
    node(late, "end")["Text"] = text[:split].replace(
        'In the room above, she kicked off her boots',
        'In the room above, she closed the door with her heel, kicked off her boots')
    # Explicit brief: postwar leave; this paragraph has its reserved identifier.
    block = p('{n}She drew the Commander closer, her laughter giving way to '
        'another hungry kiss. The old scars on her hands were rough against bare skin, her breath came '
        'ragged, and for a long while the leave she had counted so carefully stopped being counted.{/n}')
    block["Id"] = late["Id"] + ".explicit.1"
    node(late, "end")["Paragraphs"] = [block, p(text[split:])]
    # A custody disagreement cannot disappear inside an alley kiss.
    for suffix in ("courtship", "courtship_visit"):
        custody_gate(by[PREFIX + "after." + suffix])
    for suffix in ("commit", "commit_visit"):
        answer = node(by[PREFIX + "dismissed." + suffix], "answer")
        # Reclamation has the same settled meaning as handing it back. Existing
        # indices retain their effects and destinations; new alternatives append.
        for index in (5, 6):
            answer["Choices"][index]["Forbids"].append(ROBBED)
        for index in (7, 8):
            fresh = copy.deepcopy(answer["Choices"][index])
            fresh["Requires"] = [x for x in fresh["Requires"] if x != GIVEN] + [ROBBED]
            fresh["Forbids"].append(GIVEN)
            answer["Choices"].append(fresh)
    additions = new_scenes(by)
    for addition in additions:
        # Same current-body observation used by every existing physical route
        # scene; dispatch and historical return alone cannot supply a meeting.
        addition["Requires"].append("seelah.present_now")
    scenes.extend(additions)


def new_scenes(by):
    common = dict(Relationship="seelah", Areas=[DREZEN], Chapters=[3, 5],
                  optional=True, forbids=("seelah.closed", "seelah.plot_departed"))
    reclaimed = scene(PREFIX + "dead.list_reclaimed", "The hand you did not watch", "Seelah", 3,
        '"Seelah, about your list..."', [
        n("start", "Seelah", '{n}Seelah bumps your shoulder as you stop by the crusade '
          'notices. Her apology is excellent. Her hand, when she steps away, holds '
          'the folded list you kept.{/n}\n"Warned you. I wanted to wait until I could '
          'do that standing up."\n{n}She checks the first line, then the last. Her '
          'smile goes.{/n}\n"Acemi. The Kenabres stones. Mine to put right. You '
          'don\'t get to carry them for me just because you brought me back."',
          c('"It belongs with you. I should have returned it."', "private", flags=(ROBBED, SETTLED)),
          c('"You have it. What happens between us now?"', "offer", flags=(ROBBED, SETTLED),
            requires=("seelah.romance",)),
          c('"You have it. What happens between us now?"', "offer", flags=(ROBBED, SETTLED),
            requires=(PREFIX + "courted",), forbids=("seelah.romance",)),
          c('"You have it. What happens between us now?"', "offer_first", flags=(ROBBED, SETTLED),
            forbids=("seelah.romance", PREFIX + "courted")),
          portrait="Seelah"),
        n("private", "Seelah", '{n}She puts the list against her ribs and ties her purse properly.{/n}\n'
          '"Yes. You should. I\'m keeping it now. As for us... come and ask me '
          'without a dead woman\'s purse in your hand."', c('[Let her keep it.]'), portrait="Seelah"),
        n("offer", "Seelah", '"I decide whether I want another evening. I still do, '
          'damn you." {n}She taps your coat.{/n} "And if you want a pocket game, '
          'we play with your purse. My list stays with me. Nobody keeps what '
          'the other needs back."',
          c('"Your rules. Show me how badly I can lose."', flags=(GAME,)),
          c('"Keep the list private. I would rather have your company."'), portrait="Seelah"),
        # Authored first invitation: a returned body/list is not a past date.
        # The familiar offer and its saved answers remain at their old IDs.
        n("offer_first", "Seelah", '"An evening with you? Yes, damn you. Fye\'s, '
          'before the next muster." {n}She taps your coat.{/n} "And if you want '
          'a pocket game, we play with your purse. My list stays with me. '
          'Button your coat. I need a challenge."',
          c('"Your rules. Show me how badly I can lose."', flags=(GAME,)),
          c('"Keep the list private. I would rather have your company."'), portrait="Seelah"),
    ], requires=("trickster.ever", PREFIX + "returned", HOLDS, CUSTODY + ".unsettled"),
       AnswerLists=[HUB], **common)
    # Outside-party copy uses the same reclamation, not an extra device.
    reclaim_copy = copy.deepcopy(reclaimed)
    reclaim_copy.update(Id=PREFIX + "after.list_reclaimed", ContactUnit=NPC,
                        InteractionHub="seelah.presence")
    reclaim_copy.pop("AnswerLists")
    reclaimed["Requires"].extend(["seelah.revived", PREFIX + "woke", KEEPS])
    reclaim_copy["Forbids"].append("seelah.revived")
    paid = scene(PREFIX + "dismissed.second_ask_paid", "Her first coin", "Seelah", 3,
        '"Seelah. I wanted to ask you again."', [
        n("start", "Seelah", '{n}Seelah places a chapel receipt beside her drink. '
          'One silver, from her company wages, entered toward the Kenabres reliquary.{/n}\n'
          '"Mine. Earned it standing in the rain with the road company. Haldis '
          'wanted to round it up when he heard what it was for. I made him write '
          'the damned coin I paid."\n{n}She folds the receipt into her list.{/n}\n'
          '"First one. There will be plenty more. Now ask about me, Commander. '
          'You\'re allowed to want me while I still owe them."',
          c('"I still want another evening with you. As lovers."', "yes", flags=(COIN_PAID,)),
          c('"I came to see you. We can leave the question for now."', "later", flags=(COIN_PAID,)),
          c('"I cannot promise you that. Let us be friends."', "friend", flags=(COIN_PAID, PREFIX + "friends")),
          portrait="Seelah"),
        n("yes", "Seelah", '{n}She takes your hand across the table.{/n}\n'
          '"Good. I wanted you to see that coin first. When you ask me again, '
          'we can talk about us instead of Haldis\'s bowl."\n'
          '{n}She lifts her tankard, grinning.{/n} "Finish your drink. '
          'I\'m still thinking what to take out of that coat."',
          c('[Finish the drink before asking her on her terms.]'), portrait="Seelah"),
        n("later", "Seelah", '"Then drink with me. I have a story about the '
          'sergeant\'s horse. No stolen saints in it. A very stupid sergeant, though."',
          c('[Share the evening.]', abort=True), portrait="Seelah"),
        n("friend", "Seelah", '{n}She looks down at your joined hands, then lets go.{/n}\n'
          '"Friends, then. I wanted more. But I\'m glad you came."', c('[Finish the drink.]'), portrait="Seelah"),
    ], requires=("trickster.ever", PREFIX + "returned", PREFIX + "declined", COIN_NO,
                 "seelah.romance", CUSTODY), delay=96,
       ContactUnit=NPC, InteractionHub="seelah.presence", **common)
    # This is the refusal-specific payment beat, not a second first-night scene.
    # The existing second ask reads her paid receipt and retains its reserved slot.
    paid["Forbids"].extend(["seelah.committed", PREFIX + "friends", COIN_PAID])
    return [reclaimed, reclaim_copy, paid, *early_situations()]


def early_situations():
    """One native-party invitation and its optional, sober morning consequence."""
    party = scene("seelah.early.cart_evening", "The people who brought the beer", "Seelah", 1,
        '"You saved a cart under the demons\' noses. That deserves a drink."', [
        n("start", "Seelah", '{n}Curl is guarding the mugs while Jannah tries '
          'to coax a tune out of the room. Elan watches the door. Seelah pushes '
          'a cup toward you and makes space on the bench.{/n}\n'
          '"They brought that cart through Kenabres while the demons were '
          'burning it. Nobody\'s writing a hymn about them. So we drink '
          'their beer and give them a bloody good evening."\n'
          '{n}She catches you looking at her and grins.{/n}\n'
          '"I wanted you here too. Before you start thanking the barrel."',
          c('"Then dance with me."', "dance"),
          c('"Walk with me when you have finished the drink."', "walk"),
          c('"I will stay for a cup. The company is good."', "cup"), portrait="Seelah"),
        n("dance", "Seelah", '{n}She leaves her cup with Curl and takes your '
          'hand. Jannah claps the beat; Elan moves a stool out of the way '
          'without quite admitting to helping. Seelah\'s palm is firm at '
          'your back. By the second turn she is laughing, warm and sweating, '
          'and looking straight at you.{/n}\n"There. No demons between us '
          'for once. Another turn?"', c('[Stay for the dance.]', "cup"), portrait="Seelah"),
        n("walk", "Seelah", '{n}Seelah leaves her beer unfinished. You make '
          'a circuit of the Heart\'s crowded hall, past defenders sleeping '
          'with weapons in reach. She lowers her voice beside a bandaged '
          'soldier, then finds a quiet patch by the stairs.{/n}\n'
          '"I wanted to get you away from the table. That\'s all the '
          'cunning I\'ve got tonight." {n}She takes your hand.{/n}',
          c('[Stay beside her a while.]', "cup"), portrait="Seelah"),
        n("cup", "Seelah", '{n}Back at the table, Jannah asks Seelah to help '
          'shift bedding from the drafty passage in the morning. Seelah '
          'agrees, reaches for another cup, and catches your eye over it.{/n}\n'
          '"One more. Then bed. I\'m excellent at sensible plans."',
          c('[Leave her to her friends.]', flags=("seelah.early.bad_cup_setup",)),
          c('"Leave that cup. We have enough wounded needing us at dawn."', "stop"), portrait="Seelah"),
        n("stop", "Seelah", '{n}She looks into the cup, then puts it down.{/n}\n'
          '"Spoilsport. Right, Jannah, dawn. If I\'m not up, pull my boots '
          'off the bench. You\'ll hear about it."', c('[Say goodnight.]'), portrait="Seelah"),
    ], Relationship="seelah", AnswerLists=["f1e7b7a6740caaa44a3762033c5f0a5a"],
       Chapters=[1], last=1, optional=True,
       forbids=("seelah.closed", "seelah_dead", "seelah_gone", "inhuman"))
    # Jannah's actual contact, not a Drezen cameo or a inferred later return.
    morning = scene("seelah.early.bad_cup", "A mouth full of ashes", "Seelah", 1,
        '"Jannah, are you waiting for Seelah?"', [
        n("start", "Seelah", '{n}Seelah sits on the bench with her face in '
          'her hands. Jannah waits beside a pile of bedding. Beyond the '
          'Heart\'s shutters, Kenabres is still burning.{/n}\n'
          '"Gods. My mouth tastes like the street. Did I promise her dawn? '
          'Yes. I did. Stop looking at me like that, Jannah, I remember." '
          '{n}She gets to her feet herself, wincing.{/n}',
          c('"I can tell her I kept you busy."', "cover"),
          c('"We will move it together. You can explain while we work."', "help"),
          c('"You promised. Go and face her."', "alone"), portrait="Seelah"),
        n("cover", "Seelah", '"No. Don\'t get yourself into it." '
          '{n}She turns to Jannah.{/n} "I drank too much. I\'m late. You '
          'shouldn\'t have had to wait."\n{n}Jannah snorts. "I\'m still '
          'waiting. Grab that end." Seelah takes the bundle without '
          'another excuse.{/n}', c('[Leave them to the work.]'), portrait="Seelah"),
        n("help", "Seelah", '{n}Seelah takes the heaviest roll herself. '
          'You clear a sleeping place while she tells Jannah what happened.{/n}\n'
          '{n}"Next time, finish with water," Jannah says. "I wanted '
          'help, not a paladin groaning over my blankets."{/n}\n'
          '"Water. Yes. Don\'t say it so loud." {n}Seelah shakes out '
          'the roll and goes back for another.{/n}', c('[Finish the missed work together.]'), portrait="Seelah"),
        n("alone", "Seelah", '"Going." {n}She shoulders a roll of bedding '
          'and catches Jannah\'s eye.{/n} "I got drunk. I\'m sorry. Where '
          'does this go?"\n{n}Jannah points into the hall and picks up '
          'the other bundle. Seelah follows her. Her headache goes with her.{/n}',
          c('[Leave her to keep her promise.]'), portrait="Seelah"),
    ], Relationship="seelah", ContactUnit="588418cb0dfd7cb45b6e6d370ef42bea",
       AnswerLists=["f1e7b7a6740caaa44a3762033c5f0a5a"],
       Chapters=[1], last=1, optional=True, delay=24,
       requires=("seelah.early.cart_evening", "seelah.early.bad_cup_setup"),
       forbids=("seelah.closed", "seelah_dead", "seelah_gone", "inhuman"))
    return [party, morning]


def integrate(payload):
    by = {s["Id"]: s for s in payload["Scenes"]}
    derived = payload.setdefault("Derived", {})
    forbids = payload.setdefault("DerivedForbids", {})
    derived[CUSTODY + ".unsettled"] = [[HOLDS]]
    forbids[CUSTODY + ".unsettled"] = [GIVEN, ROBBED, SETTLED]
    forbids[CUSTODY] = [CUSTODY + ".unsettled"]
    forbids[PREFIX + "no_romance"] = ["seelah.romance", "seelah.committed"]
    # Downstream engine contract preserves extra revokers. A company notice by
    # itself has never been an affirmative romantic answer.
    forbids.setdefault(PREFIX + "late_committed", []).append(PREFIX + "no_romance")
    # Direct native FlagUnlocked on Epilogues/Cue_0040; no invented Aeon memory.
    payload.setdefault("UnlockableFlags", {})["seelah.aeon_remembers"] = "a8b030ebca6c9744bac633cff609b698"
    payload.setdefault("Etudes", {})["seelah.plot_departed"] = "3b8ccafc1be912a4187350ac473cdc0e"
    unavailable = payload["Relationships"]["seelah"]["UnavailableFlags"]
    if "seelah.plot_departed" not in unavailable:
        unavailable.append("seelah.plot_departed")
    # Native Q3 ktc_ElanCalls/Answer_0029: actual selected harsh treatment,
    # never inferred from his death or from a lover's disagreement.
    payload.setdefault("SelectedAnswers", {})["seelah.elan_called_useless"] = "d6e68640b972e8e4e9ea460235fcc914"
    for s in payload["Scenes"]:
        if s.get("Relationship") == "seelah" and not s.get("TricksterDevice"):
            if "seelah.plot_departed" not in s["Forbids"]:
                s["Forbids"].append("seelah.plot_departed")
    for id in ("seelah.door", "seelah.road", "seelah.late_afterglow"):
        custody_gate(by[id])
    ordinary_situations(by)
    # Existing terminal payment indices and native costs remain unchanged.
    fix_transactions(by)


def ordinary_situations(by):
    for id in ("seelah.weight", "seelah.souls"):
        s = by[id]
        node(s, "start")["Choices"].append(c('"You heard what I said to Elan."', "elan_conduct",
            requires=("seelah.elan_called_useless",)))
        s["Nodes"].append(n("elan_conduct", "Seelah",
            '"I heard. His wife\'s soul had been stolen, and you told him a '
            'soldier with a troubled heart was no use to anyone." '
            '{n}Seelah puts her shield down. She looks at you instead of its rim.{/n}\n'
            '"You want people to trust you with their lives. Don\'t sneer '
            'when they care about someone else\'s. I care about you. I '
            'wouldn\'t want to hear that in your mouth if it were me asking '
            'for help."',
            c('"I spoke harshly. He needed help, and I will remember that."', "end",
                flags=("seelah.corrected_demand",)),
            c('"You expect too much from me. We should stop being lovers."', "elan_part"),
            portrait="Seelah"))
        s["Nodes"].append(n("elan_part", "Seelah",
            '{n}She retrieves her shield, checking the fastening with her thumb.{/n}\n'
            '"Then we stop. I won\'t stop asking you to do better as Commander. '
            'But I won\'t come to your room and pretend this doesn\'t matter."',
            c('[End the romance.]', flags=("seelah.closed", "seelah.parted")), portrait="Seelah"))
    # The repaired appointment ends in appetite, not another pastry performance.
    for id in ("seelah.promise", "seelah.kept"):
        # Their source EVENING list shares objects. Detach both situations before
        # changing any page, so kept's uninterrupted supper cannot overwrite promise.
        by[id]["Nodes"] = copy.deepcopy(by[id]["Nodes"])
        node(by[id], "supper")["Text"] = (
            '{n}Seelah spreads the blanket and drops the food between you. '
            'Her clean shirt is creased where her armor pressed it. '
            'Beyond the camp, the watch is changing.{/n}\n'
            '"There. The recruit has had help, we have supper, and I finally have you '
            'to myself." {n}She catches your hand before you reach for the '
            'bread. Her thumb passes over your knuckles.{/n}\n'
            '"I\'ve been wanting to kiss you all damned day. Supper can wait a moment."'
            if id == "seelah.promise" else
            '{n}Seelah spreads the blanket and puts down supper. This time '
            'nobody is waiting for a clasp, a horse, or a paladin. She '
            'catches your hand before you can reach for the food.{/n}\n'
            '"Kept it. The whole evening. Now come here before the next '
            'watch finds something else for us to do."')
        node(by[id], "supper")["Choices"][0]["Text"] = '"Then come here and kiss me."'
        node(by[id], "kiss")["Text"] = (
            '{n}She kisses you with her hand tight around yours. When you '
            'draw back, she follows, impatient for another kiss. Your '
            'shoulder meets the blanket; she braces beside you, grinning.{/n}\n'
            '"Worth the wait. Damn the clasp."\n{n}She stays close enough '
            'to feel her laugh against your mouth.{/n}')
    node(by["seelah.wager"], "dance_end")["Text"] = (
        '{n}She turns under your joined hands and comes back into your '
        'arms without missing the beat. The musician starts again; '
        'she stays where she is for the first two notes.{/n}\n'
        '"One more. I wanted this before I invented that stupid game." '
        '{n}She takes your hand and pulls you into the next turn.{/n}')
    door = by["seelah.door"]
    node(door, "start")["Text"] = (
        '"A door. Finally." {n}Seelah ushers you into the borrowed room, '
        'unhooks her sword belt and hangs it beside the bed. Boots and orders '
        'have followed her through Drezen all day; she leaves both outside.{/n}\n'
        '"I had a speech ready on the stairs. Come in before I remember it."')
    night = node(door, "night")["Text"]
    split = night.index('{n}The lamp survives.')
    approach = night[:split].replace(
        'She unbuckles her sword belt and hangs it on the bedpost as if it has earned a rest, then pulls',
        'She pulls')
    add_cut(door, "night", approach,
        '{n}She catches your mouth again and draws you down against her, '
        'the impatient tug of her hand giving way to a grip she keeps. Her skin is '
        'warm and freckled under your palms, her breath comes short against your throat, '
        'and the narrow bed, the borrowed room and the whole of Drezen stop mattering. The lamp '
        'survives, though neither of you reaches to put it out for a long while.{/n}',
        '{n}When the room is quiet, Seelah finds your hand beneath the blanket '
        'and holds it as she falls asleep, one foot hooked over yours.{/n}\n'
        '"For the record," {n}she mumbles into your shoulder,{/n} "I am not sorry. '
        'Not even a little. Iomedae can take it up with me in the morning."')
    morning = by["seelah.morning"]
    start = node(morning, "start")
    # Ordinary quiet/changed histories still lead to their original bread day.
    start["Text"] = ('{n}Seelah carries four loaves in a cloth bag. One slips '
        'out; she catches it against her damp sleeve.{/n}\n'
        '"The woman behind the storehouse said she was hungry. I charged '
        'straight at the baker. He looked so pleased to see my coin that '
        'I bought fresh bread for half the bloody watch."\n'
        '{n}She lowers the bag.{/n} "Now I have to carry it. Fine victory."')
    start["Choices"].append(c('[Catch her hand before she leaves.]', "night_remembered",
        requires=("seelah.private_night",)))
    morning["Nodes"].append(n("night_remembered", "Seelah",
        '{n}She comes willingly, pressing you against the warm stone beside '
        'the door. Her mouth finds yours before she has put down the bread.{/n}\n'
        '"Been thinking about that room all the way back. And I have to go '
        'put on armor. Rotten arrangement."\n{n}She kisses you once more, '
        'then pushes a loaf into your hand.{/n}\n"Tonight. Find me before '
        'somebody else does."', c('[Walk with her.]', "end"), portrait="Seelah"))
    node(by["seelah.souls"], "survived")["Text"] = (
        '"We nearly lost them. I keep thinking, one wrong turn, a few more minutes..."\n'
        '{n}Seelah blows out a breath and grips the edge of the table.{/n}\n'
        '"They\'re here. I\'d rather ask them how they are than sit here '
        'imagining another funeral."')
    node(by["seelah.parting"], "stay")["Text"] = (
        '"Then choose a time with me. Out loud, with a day in it." '
        '{n}She pulls up the chair you were about to leave.{/n}\n'
        '"I want an evening with you before the next march. And if somebody '
        'sets the world on fire again, tell me we have to change it. '
        'I\'ll swear at the demons and find another day."')
    afterglow = by["seelah.late_afterglow"]
    text = node(afterglow, "night")["Text"]
    split = text.index('{n}In the morning')
    add_cut(afterglow, "night", text[:split],
        '{n}She lets go of your wrists to pull you closer, kissing you until '
        'neither can spare breath for the song. From the workshop below, '
        'a hammer begins to strike.{/n}',
        '{n}Seelah wakes with her arm heavy across you. Hearing the hammer, '
        'she pulls you closer instead of rising.{/n}\n"Morning. Try getting '
        'me out of this bed. Go on. I dare you."')
    aeon = by["seelah.ending_aeon"]
    old = node(aeon, "start")
    # Keep the original page and its terminal choice identity and mechanics.
    text = old["Text"]
    old["Text"] = '{n}In a world spared the Worldwound, Seelah still took the road with her sword and pack.{/n}'
    old["Paragraphs"] = [
        p(text, forbids=("seelah.aeon_remembers",)),
        p('{n}She remembered the demon attack, the crusade, and the comrade '
          'who had erased them. At quiet fires she spoke of the Commander '
          'without expecting the other travelers to recognize the name. '
          'She kept their private evenings to herself, and carried those '
          'memories when she went on to the next village that needed her.{/n}',
          requires=("seelah.aeon_remembers",)),
    ]
    # Avoid a pillow invitation in a history that only chose a posting.
    node(by["seelah.ending_sacrifice"], "start")["Paragraphs"][0]["Requires"].append("seelah.romance")
    # Each living coda has an actual return; her quests and travel still differ.
    for id, visit in {
        "together": '{n}One evening she came home soaked, left her shield at the '
            'door and pulled the Commander up from the table for a kiss. '
            '"Missed you. Complaints after supper." Their plans for the '
            'next journey lay beneath her dripping gloves.{/n}',
        "unsettled": '{n}On one leave she arrived without warning and knocked '
            'until the Commander opened the door. "Still full of questions," '
            'she said. "Still wanted to see you." She stayed for the evening, '
            'then took up her pack and the road again.{/n}',
        "grieving": '{n}On a rare return she sat beside the Commander without '
            'taking off her coat. They held her hand until she was ready to '
            'speak. At the door next morning she turned back for a kiss; '
            'then she went to the people still waiting for her help.{/n}',
        "unfinished_work": '{n}She returned to Drezen with a failed lead and '
            'boots split at the seams. "No luck," she told the Commander. '
            '"But I wanted to come home before trying again." They shared '
            'supper and the fire. She left with repaired boots and another '
            'letter promised.{/n}',
    }.items():
        node(by["seelah.ending_" + id], "start")["Text"] += "\n" + visit


def fix_transactions(by):
    """Persist seller acquisition, then resume payment instead of rerolling."""
    acquired = PREFIX + "seller_resolved"
    for sid in (PREFIX + "dead.pickpocket", PREFIX + "dead.pickpocket_effects"):
        s = by[sid]
        effects = sid.endswith("_effects")
        entry = node(s, "start" if effects else "bier")
        for answer in entry["Choices"]:
            answer["Forbids"].append(acquired)
        entry["Choices"].append(c('[Finish paying for the rite.]', "payment_resume", requires=(acquired,)))
        for nid in (("lifted", "concealed_rider", "concealed_rider_word", "taken", "paid") if effects
                    else ("lifted", "concealed", "taken", "paid")):
            for answer in node(s, nid)["Choices"]:
                add_flag(answer, acquired)
        if not effects:
            s["Nodes"].append(n("payment_resume", "Narrator",
                '{n}The seller\'s stones are already in the chapel bowl. The '
                'chaplain has kept the candles lit. He waits for the other half '
                'of the rite, not another visit to the stall.{/n}',
                c('[Bring the remaining payment.]', "pocketed"), portrait="Seelah"))
            continue
        chaplain = PREFIX + "cost.chaplains_word"
        # Funding intent is not a credit receipt. Availability now selects the
        # component at the actual debit, including a diamond acquired on retry.
        for answer in node(s, "purse")["Choices"]:
            answer["Set"] = [f for f in answer["Set"] if f != chaplain]
        for nid in ("lifted", "taken", "paid"):
            answers = node(s, nid)["Choices"]
            answers[0]["Forbids"] = []
            answers[0]["Requires"] = ["seelah.diamond_held"]
            answers[1]["Requires"] = []
            answers[1]["Forbids"] = ["seelah.diamond_held"]
        grabbed = node(s, "grabbed")["Choices"]
        grabbed[0]["Forbids"] = []
        grabbed[0]["Requires"] = ["seelah.diamond_held"]
        grabbed[1]["Requires"] = []
        grabbed[1]["Forbids"] = ["seelah.diamond_held"]
        add_flag(node(s, "rider_word")["Choices"][0], chaplain)
        s["Nodes"].append(n("payment_resume", "Narrator",
            '{n}The stones and Seelah\'s savings are sealed for the rider. '
            'The seller\'s business is finished. Only the second stone, '
            'or the chapel credit that buys it, is still missing.{/n}',
            c('[Add your diamond.]', "rider", requires=("seelah.diamond_held",)),
            c('[Arrange the chapel credit.]', "rider_word", forbids=("seelah.diamond_held",)),
            portrait="Seelah"))

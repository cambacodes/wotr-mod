"""Authored round-2 situations; native facts are cited in kiana-setpieces.md.

Apply after the partner appender. Only Kiana surfaces are changed. Append saved
nodes/answers; keep legacy exits and their effects. No new price or romance gate.
The native public reunion cannot host the planned bedroom interruption: its
brief is retained for the coordinator, without inventing a private arrival.
"""
import copy

from story_format import c, n, p
from storylines import kiana_partner as kp, kiana_trickster as kt


def page(id, text, *answers, speaker="Kiana"):
    return n(id, speaker, text, *answers, portrait="Kiana")


def integrate(payload):
    books = {book["Id"]: book for book in payload["Scenes"]}

    def nodes(sid):
        return {node["Id"]: node for node in books[sid]["Nodes"]}

    # SP1 / F1 6–8: costume casting precedes the ceremony. A cancelled wedding
    # has the same ribbon/breadstick/wine, without a soul-taking cup.
    if "kiana.trickster.ward_rounds" in books:
        ward = books["kiana.trickster.ward_rounds"]
        pages = nodes(ward["Id"])
        recalls = {
            "court_captive": '''{n}Kiana catches the list against her knee.{/n}
"The ribbon! Elan's knights brought a cake knife to rescue you. I had to sit down before they could begin."
{n}She laughs, then straightens the crumpled sheet.{/n}
"We never got as far as the vows. The princess still had a prisoner, though. Left side. Your escape can wait until everyone has water."''',
            "court_hunter": '''"Keep the breadstick. I have retired from dying on benches."
{n}She touches the spot where the breadstick broke against her dress.{/n}
"My finest swoon, and no wedding afterward. Elan still complains that the hunter got more applause than the groom."
{n}She gives you half the list.{/n}
"Left side. The sergeant wants a crossbow in the next version. Don't encourage him."''',
            "court_guest": '''"Water. We are in a temple, and Arsinoe knows where I hide the wine."
{n}Kiana holds out half the list.{/n}
"You drank to us before anyone stamped POSTPONED across the licence. A perfectly good toast. I still intend to make use of it."
{n}A patient calls for the jug. She lifts it.{/n}
"Left side, guest. Our audience is thirsty."''',
        }
        for nid, text in recalls.items():
            if nid not in pages:
                continue
            old = next(a for a in pages["start"]["Choices"] if a["Next"] == nid)
            old["Forbids"].append(kt.H_BETROTHED)
            twin = copy.deepcopy(old)
            twin["Forbids"].remove(kt.H_BETROTHED)
            twin["Requires"].append(kt.H_BETROTHED)
            twin["Next"] = nid + "_postponed"
            pages["start"]["Choices"].append(twin)
            ward["Nodes"].append(page(twin["Next"], text,
                c('[Do the left side.]', "rounds_no_wedding")))
        pages["rounds"]["Text"] = '''{n}The wedding guests answer their names. One complains about the blankets; another tells a worse joke than yours. Kiana ticks each name only after its owner speaks.{/n}
"The whole court. Even the one who bites."
{n}The dog catches the corner of her list. She pulls it free and tucks your half into your belt.{/n}
"No, you don't get a tick. You haven't learned your lines."
{n}From the counter, Arsinoe points to the empty jug. Kiana takes it, sighing.{/n}
"And the princess gets another round."'''

    # SP2: her rehearsal is interrupted by a real answer, never a permission
    # inferred from the kiss. The deferred arm acknowledges the unanswered debt.
    if "kiana.answer" in books:
        book = books["kiana.answer"]
        pages = nodes(book["Id"])
        pages["start"]["Text"] = '''{n}Kiana has hung the dark cloth again. She begins with the princess's outstretched hand, then sees Elan's letter beneath the script. Her hand drops.{/n}
"The princess was going to dismiss the guards. A very convenient scene."
{n}She pulls the letter free and lays it on top. Beyond the window, a patrol marches toward the gates.{/n}
"Elan wrote. Before I invite you here again, you should hear him. Or hear what I still haven't answered."'''
        pages["apart"]["Text"] = '''"I still love him. I also began looking forward to the evenings when he would be away. He asked me that, and I answered."
{n}She presses the travel case shut with her heel.{/n}
"He wanted to come home to the marriage we made. I kept asking for a different one and hoping he wouldn't notice the difference. I won't keep doing that to him."
{n}She takes the letter from the script.{/n}
"I told him I was leaving. Not because he went to fight. Because I was no longer waiting for the same life."'''
        pages["partner_wait"]["Text"] = '''{n}Kiana starts to tuck Elan's reply under the script, then leaves it on top.{/n}
"He asked whether I still want our marriage. I do. I haven't answered the rest."
{n}She sits on the closed case.{/n}
"I said I would tell him what I wanted. I haven't. I still asked you here. Don't call that patience on my behalf."
{n}She puts the princess's pages aside.{/n}
"Come again if you want me. Before you promise a life, we settle this. He will get an answer in my hand."'''
        # Honest waiting gets the existing confession/reply before courtship.
        # The same terms remain required at commitment; this adds no condition.
        old = next(a for a in pages["start"]["Choices"] if a["Next"] == "partner_wait")
        old["Forbids"].append("kiana.waited")
        book["Nodes"].extend([
            page("reply_waited", '''{n}Kiana gives you Elan's reply. The patrol's boots fade below the window.{/n}
"I wrote before asking you back. He gets to say what this costs him. Read it. I'll wait."''',
                c('[Read his answer.]', "reply_elan")),
            page("reply_elan", '''"Kiana, I want our marriage. I also want to come home to you, not to another careful explanation of why you are unhappy.
"You asked me before going further. That matters. It doesn't make this easy. If the Commander is to keep visiting, I want you home when I return. No officers sent for you. No quarrels in my orders.
"Tell me whether you want that too. Just you, Kiana."''',
                c('[Let her answer him.]', "reply_kiana"), speaker="Elan"),
            page("reply_kiana", '''{n}She writes beneath his question, shielding nothing from you. Then she folds the answer into a fresh sheet addressed to Elan alone.{/n}
"Yes. I want him home. I want you to come again. The princess would have had a magnificent excuse for all this. I haven't."
{n}She leaves the letter beside the door for the courier.{/n}
"His terms come with the invitation. If you cannot bear them, leave me my marriage."''',
                c('[Accept the terms and her next invitation.]',
                    flags=(kp.OPEN, "kiana.available")),
                c('"Then I should remain your friend."',
                    flags=("kiana.closed", "kiana.stayed_married"))),
        ])
        pages["start"]["Choices"].append(c('[Hear the answer to the letter she promised to send.]',
            "reply_waited", requires=("trickster.now", "kiana.waited"),
            forbids=(kp.DEAD, "kiana.bereaved")))
        # A letter must intervene on the unresolved arm too, without claiming
        # that it settles the affair. Its wording is deliberately not a blessing.
        pages["start"]["Choices"].append(c('[Read what Elan asked her, before deciding to wait.]',
            "reply_unanswered", requires=("trickster.now",),
            forbids=(kp.DEAD, "kiana.bereaved", "kiana.waited")))
        book["Nodes"].append(page("reply_unanswered", '''{n}There is a crease through Elan's question.{/n}
"Kiana, I want to come home to you. Do you still want our marriage? Tell me what has happened. I can't answer a letter you haven't sent."
{n}Kiana draws the paper back before beginning the princess's line. She does not begin it.{/n}''',
            c('[Hear what she wants now.]', "partner_wait"), speaker="Elan"))
        # Retire only the current deferred shortcut; its identity/target survive.
        old["Forbids"].append("trickster.now")

    if "kiana.betrothal" in books:
        book = books["kiana.betrothal"]
        pages = nodes(book["Id"])
        # F1 12: the old wording offered coexistence but mechanically broke up.
        pages["start"]["Choices"][1]["Forbids"].append("trickster.now")
        pages["start"]["Choices"].append(c('"I want you. If you have decided to end the engagement, tell me."',
            "truth", requires=("trickster.now",)))
        pages["partner_wait"]["Text"] = '''{n}Elan's letter lies over the postponed licence. Kiana has stopped rehearsing the princess's greeting.{/n}
"He asked whether I still mean to marry him. A stamp cannot answer that. Neither can you."
{n}She folds the licence into the script.{/n}
"I haven't told him about wanting you. I know what I promised. Before the guest swears to stay, Elan gets my answer."'''

    # SP3: preserve threshold/morning_after and their old outgoing answer.
    # Append slot access, retiring only the shortcut on current Trickster.
    if "kiana.date" in books and "threshold" in nodes("kiana.date"):
        book = books["kiana.date"]
        pages = nodes(book["Id"])
        pages["start"]["Text"] = '''{n}One guest. No court. Bring no speeches. Kiana has underlined the last instruction. She opens the door before the next patrol passes her window.{/n}
"Wine, candles, and a dress that has defeated two ribbons. I was going to make you admire it from the doorway."
{n}She stands aside. The script waits on the table, well clear of the wine.{/n}
"Come in. I have enough paper kingdoms to keep the crusade busy all night."'''
        pages["want"]["Text"] = '''"This evening. And the next one, when you can come."
{n}She puts the wine down and looks straight at you.{/n}
"Answer my letters. Turn up when you say you will. I can spend an evening alone; I don't want to spend it dressed for somebody who forgot me."
{n}Her fingers return to the ribbon at her throat.{/n}
"Now. Can you promise me another knock at that door?"'''
        pages["kiss"]["Text"] = '''{n}Kiana meets your kiss, then pulls you back when you begin to draw away. Her fingers tighten in your collar.{/n}
"I had a line for this."
{n}She looks toward the script, laughs breathlessly, and kisses you again.{/n}
"Damn the line."'''
        pages["threshold"]["Text"] = '''{n}She breaks the kiss just far enough to speak.{/n}
"The princess dismisses the guards. Come here. I am tired of rehearsing."
{n}She shuts the door with her heel. A horn sounds from Drezen's wall; she listens until it stops, then turns back to you. She unlaces the dress herself, watching your face over her shoulder. When you reach for the last hook, she catches your wrists and kisses you.{/n}
"That one is mine."
{n}She lets the dress fall, takes you by the hand and draws you to the bed. For a moment she seems ready to give another royal command. Instead she pulls you close.{/n}
"No speeches. I want you."'''
        pages["threshold"]["Choices"][0]["Forbids"].append("trickster.now")
        pages["threshold"]["Choices"].append(c('[Go to her.]', "kiana.date.explicit.1", requires=("trickster.now",)))
        # Explicit brief: first mutually chosen night; preserve unresolved account.
        book["Nodes"].append(page("kiana.date.explicit.1", '''{n}Kiana draws you down beside her. Her hand leaves yours to loosen the ribbon at her throat.{/n}
"Stay. I haven't finished with you."
{n}The candle burns beside the abandoned dress.{/n}''', c('[Stay with her.]', "morning_after")))
        pages["morning_after"]["Text"] = '''{n}Kiana sits up in bed with ink on her fingers. She has straightened the sheet, then pulled it crooked again to reach the playbill beside your pillow.{/n}
"I meant to write a splendid morning-after speech. You have slept through the composition."
{n}She puts the pen down and kisses your shoulder.{/n}
"Come again. I want another night before the war eats it."'''
        old = pages["morning_after"]["Choices"][0]
        old["Forbids"].append(kp.OPEN)
        pages["morning_after"]["Choices"].append(c('[Hear what she has not settled.]',
            "morning_account", requires=(kp.OPEN,), forbids=(kp.DEAD,)))
        pages["morning_after"]["Choices"].append(c('[Hear what she still keeps.]',
            "morning_remembrance", requires=(kp.OPEN, kp.DEAD)))
        book["Nodes"].append(page("morning_account", '''{n}Elan's letter has slipped from beneath the script. Kiana picks it up before reaching for your hand.{/n}
"He doesn't become a worse husband because I enjoyed last night. I still have to answer him."
{n}She lays it on top of the playbill.{/n}
"And the ward opens this morning. Our missing guests haven't come home because I finally got a night I wanted. Help me find my dress."''',
            c('[Spend the morning together.]', flags=tuple(old["Set"]))))
        book["Nodes"].append(page("morning_remembrance", '''{n}Elan's letter has slipped from beneath the script. Kiana picks it up and folds it along its worn crease.{/n}
"I cannot answer this one now. I can keep it."
{n}She lays it on the table before reaching for your hand.{/n}
"I wanted last night. I want you here again. Let me find a pen before the princess starts explaining it for me."''',
            c('[Spend the morning together.]', flags=tuple(old["Set"]))))

    # SP5 / H4: all physical, postal and ending stance clones use the same
    # counter-move. A demand never changes her decision by itself.
    for sid in ("kiana.morning", "kiana.trickster.late_question",
                "kiana.trickster.late_question_letter", "kiana.trickster.epilogue.commit"):
        if sid not in books:
            continue
        pages = nodes(sid)
        if "partner_breakup" in pages:
            pages["partner_breakup"]["Text"] = '''{n}Her next letter encloses Elan's reply. Her own account begins beneath a crossed-out greeting from the princess.{/n}
"I still love him. I told him that, and he asked why I was leaving. I told him I had started counting the evenings until you would come. I don't want to go home pretending that hasn't happened."
{n}She has copied her final answer.{/n}
"Elan, I am ending our life together. I won't ask you to wait while I make another one. I am sorry."
{n}His reply follows on a separate sheet.{/n}'''
        if "partner_morning" in pages:
            pages["partner_morning"]["Text"] = '''"I wanted you here again. Then I reached for Elan's letter. A crowded table, isn't it?"
{n}She takes it out and puts it beside the script.{/n}
"Before you offer to stay, he gets his place on it. I won't tuck him underneath the princess again."'''

    # SP4: native reunion already places Elan in a crowd, not on private stairs.
    # Keep that encounter, proof, and the wife's unrescinded closure intact.
    if "kiana.partner_discovery" in books:
        pages = nodes("kiana.partner_discovery")
        pages["start"]["Text"] = '''{n}Kiana's hand is still on Elan's sleeve. She had kissed him in front of everyone; now he unfolds a sheet from her play. Your name is beneath its last line.{/n}
"I asked her about it. Twice. The second time she answered."
{n}Kiana lets go of his sleeve. He lowers his voice.{/n}
"I thought I was coming home. Was I interrupting?"'''

    if "kiana.lastcall.call" in books:
        pages = nodes("kiana.lastcall.call")
        pages["letter"]["Text"] += '''
{n}Kiana's note was folded into the account before the march:{/n}
"I asked to be there when he called it in. He has chosen a fine time to hide behind his apprentice. Don't let him call a pardon an apology. I want to know exactly what he gets for it."
{n}Below it, she has copied the ward's list of names.{/n}'''

    # SP6 / F1 21–25: collect the victim's objection in the paying scene.
    if "kiana.trickster.pouch.second_offer" in books:
        book = books["kiana.trickster.pouch.second_offer"]
        pages = nodes(book["Id"])
        pages["paid"]["Text"] = '''{n}You repeat Sunhammer's words. The apprentice checks each against his sheet, counts the gold and empties the pouch. Arsinoe breaks the stones. Behind the curtain, somebody demands water.{/n}
"'What I could not take.'" {n}Kiana's grip hurts.{/n} "I'll give that to the villain. He can say it before somebody spits in his wine."
{n}A cooper sits up, listening. Kiana reaches for her script to show him; he pushes it away.{/n}
"Leave my name out. I've been shut in his bloody stone. I won't have strangers laughing at me as well."
{n}Kiana crosses out the name while he watches.{/n}
"Gone. He gets the speech. You get the water."
{n}She puts the script down and fetches the jug herself.{/n}'''

    # Canon class F1 9/50: Elan never lost his soul. The conscious bride can
    # volunteer in the ward; no paid history invents her discharge from a coma.
    repairs = {
        "kiana.native.aftermath_home": '''{n}Elan and Kiana wait at the front of the crowd. The guests have been awake since the stones were broken in the ward. Kiana catches his arm and pulls him close, heedless of everyone around them.{/n}''',
        "kiana.native.aftermath_6_home": '''"It feels good to be married." {n}Kiana smiles.{/n} "I've been helping at the ward. Arsinoe says my stories are no substitute for clean water. Elan still goes off fighting, of course. Somebody has to keep those damned demons away from us."''',
        "kiana.native.aftermath_8_home": '''"Kiana, my love!" {n}Elan blushes.{/n} "The Commander brought our friends home. That doesn't mean we owe every detail!"''',
    }
    for sid, text in repairs.items():
        if sid in books:
            books[sid]["Nodes"][0]["Text"] = text

    # Real attendance pays her promised chair. These are already living ending
    # hosts; mortality/ascension/presence contracts continue to gate them.
    if "kiana.ending_promised" in books:
        ending = books["kiana.ending_promised"]["Nodes"][0]
        ending["Text"] = '''{n}Kiana kept her own plans after the war. The spare chair waited beside her writing table; the guest's exit still waited on the last page.{/n}'''
        ending.setdefault("Paragraphs", []).extend([
            p('''{n}The Commander returned to Drezen and knocked at Kiana's door. She opened it with the princess's greeting ready, saw who stood there, and forgot the line.{/n}
{n}She caught the Commander by the collar and kissed them. The spare chair scraped behind the door; she kicked it clear without letting go.{/n}
"You can admire the furniture later."
{n}After supper she brought out the last page and crossed out the guest's exit. There was still enough ink to complain about the delay.{/n}''', forbids=("ascended",)),
            p('''{n}The Commander's answer came from beyond Golarion. Kiana read it twice, then wrote back: the chair was furnished, the door was hers, and godhood was a dreadful excuse for missing supper. She left the guest's entrance for an evening they could actually keep.{/n}''', requires=("ascended",)),
        ])

    if "kiana.lastcall.page" in books:
        coda = books["kiana.lastcall.page"]["Nodes"][0]
        welcome = p('''{n}When the Commander knocked at the room above the baker's, Kiana opened the door with flour on her cuff. She caught the Commander's hand, pulled them inside and kissed them before asking how long they could stay.{/n}
"The chair is yours this evening. I have other plans tomorrow; you may help me spoil them."
{n}She took down the play. Elan's letters and the ward's list stayed beside it.{/n}''',
                    forbids=("sacrifice", "ascended"))
        welcome["ForbidOverrides"] = {"sacrifice": "trickster.commander_back"}
        coda.setdefault("Paragraphs", []).append(welcome)

    # F1 23–25 siblings: one feast is history; future enforcement belongs only
    # to the living creditor. Keep existing paragraph positions, append variants.
    for book in payload["Scenes"]:
        if book.get("Relationship") != "kiana" and book["Id"] != "kiana.lastcall.page":
            continue
        if book["Owner"] not in ("Epilogue", "AeonEpilogue"):
            continue
        for node in book["Nodes"]:
            for para in node.get("Paragraphs", []):
                if "His apprentice recited it at the jewellers' feast" in para["Text"]:
                    para["Text"] = '''{n}The remaining guests came home for a thousand crowns, a favor and the Commander's apology. At the ward, the recovered cooper refused to have his name in Kiana's play. She crossed it out before fetching his water. Sunhammer's words stayed, in the villain's mouth.{/n}'''
                    node["Paragraphs"].extend([
                        p("{n}While Sunhammer lived, his apprentice kept the apology for the guild's annual feast. Kiana kept a copy too; she had not forgiven its author for the price of the stones.{/n}",
                          requires=(kt.MET, kt.BOUGHT), forbids=(kt.SUNHAMMER_DEAD,)),
                        p("{n}After Sunhammer's death, his annual demand died with him. Kiana kept the apology in the play, with the cooper's name still struck out.{/n}",
                          requires=(kt.MET, kt.BOUGHT, kt.SUNHAMMER_DEAD)),
                    ])
                    break

    # H5/H6 continuations: no second first night, no expansion of their gates.
    for sid, last_line, aftermath, flags in (
        ("kiana.ink_after", "Her ink-stained hand leaves a mark on your collar.",
         '''{n}Later, Kiana finds the ink on your collar and presses her marked finger beside it.{/n}
"Two blots. An improvement. Meral can copy the princess tomorrow; tonight she has lost her desk."''',
         ("kiana.ink_evening_kept",)),
        ("kiana.unborrowed_evening", "The key stays in the locked door.",
         '''{n}Later, she rests her head against your shoulder. The quarrel in the yard has not vanished; her pages still wait by the door.{/n}
"Tomorrow I'll decide what to do with them. Stay a little longer. I wanted this evening too."''',
         ("kiana.further_kept", "kiana.further_private_evening")),
    ):
        if sid not in books:
            continue
        book = books[sid]
        pages = nodes(sid)
        pages["kiss"]["Text"] = (
            '''{n}Kiana rises into your kiss. She closes the ink, lets the shawl fall onto the chair and catches your collar with the stained hand.{/n}
"That will mark. Oh, never mind. Come here."
{n}She backs you against the desk, moves the script and pulls you close again, impatient with the buttons beneath her fingers.{/n}'''
            if sid == "kiana.ink_after" else
            '''{n}Kiana meets your kiss, laughing when the chair catches against your heel. She moves it aside and pulls the pins from her hair.{/n}
"The yard can have its audience. I wanted you."
{n}She draws you to the edge of the bed, still kissing you, then reaches past your shoulder to lock the door.{/n}''')
        old = pages["kiss"]["Choices"][0]
        slot = sid + ".explicit.1"
        # Explicit brief: a return to desire, with the existing consequence join.
        pages["kiss"]["Choices"].append(c('[Stay with her.]', slot))
        book["Nodes"].append(page(slot, "{n}" + last_line + "{/n}", c('[Stay.]', "round2_after")))
        book["Nodes"].append(page("round2_after", aftermath, c('[Keep the evening.]', flags=flags)))

    # H2/H7 are contact, not additional sexual encounters. Keep the quiet
    # alternative and existing departure/attendance effects.
    if "kiana.widow" in books:
        nodes("kiana.widow")["room"]["Text"] = '''"A woman with an unfinished play and a guest she keeps watching instead of the page."
{n}Kiana draws the second chair beside hers. Her knee touches yours; she leaves it there.{/n}
"I want you closer. Sit here before I invent a speech to spoil it."
{n}Elan's old letter lies beside the candle. She moves the script, leaving the letter where it is.{/n}'''
    if "kiana.kept_evening" in books:
        nodes("kiana.kept_evening")["kiss"]["Text"] = '''{n}Kiana catches the back of your neck and kisses you. When the shawl slips, she tosses it onto the chair and pulls you close again.{/n}
"It will survive. I have been looking at your mouth through half of supper."
{n}A watch bell sounds in the street. She curses it softly, then walks you to the door with her fingers caught in your collar.{/n}
"Come back tomorrow. I'll have finished the page. Or I'll have thrown it into the fire. Either way, I want you here."
{n}She kisses you once more before opening the door.{/n}'''

    if "kiana.blue_room" in books:
        pages = nodes("kiana.blue_room")
        changes = {
            "start": '''{n}Kiana stands before the mirror with the blue shawl over one arm. Two brass pins lie beside it. She watches you enter in the glass, then turns from her reflection.{/n}
"Lenna has supper waiting. I invited you early. Those are separate arrangements."
{n}She lifts the shawl, letting its edge brush your hand.{/n}
"Mind the box. I found half my old kingdom looking for a pin. Tonight I would rather be wearing this than sorting it."''',
            "pin": '''{n}Kiana drapes the blue shawl below her shoulders, leaving the pale crystalline shape of her head uncovered. She holds the round brass pin against its fold, then the leaf.{/n}
"One opinion. You may come closer to give it."
{n}She turns her shoulder toward you. The loose fold slips; she catches it against her chest, laughing.{/n}
"Quickly. Before I arrive at Lenna's wearing neither."''',
            "round": '''"Shameless. Unfortunately it worked."
{n}Kiana puts the round pin into your hand and holds the fold in place. She watches your face as you fasten it, scarcely glancing at the mirror.{/n}
"There. Lenna can criticize your choice. I shall defend the assistance."
{n}She catches your wrist before you step away.{/n}''',
            "want": '''{n}Kiana keeps your hand against the newly fastened shawl.{/n}
"This is why I asked you early. I wanted a few minutes before the supper and the questions."
{n}She looks at your mouth. The pin is crooked; she leaves it alone.{/n}
"The princess could have invented a magnificent reason. I wanted you here while I dressed."''',
            "kiss": '''{n}She rises into your kiss and catches the back of your neck. The brass pin presses against your chest; she laughs into your mouth, then draws you close again.{/n}
"Lenna is going to blame the pin. I shall let her."
{n}She kisses you once more, retrieves her purse and opens the door herself.{/n}
"Come. Before I decide supper is somebody else's problem."''',
            "hand": '''{n}Kiana squeezes your hand and pulls you beside her to look in the mirror.{/n}
"Yes. I like going with you. Even to Odrin's dreadful wine."
{n}She straightens the shawl, takes her purse and keeps your hand as she turns toward the door.{/n}
"We can walk slowly. He'll explain how he made it whether we're early or late."''',
        }
        for nid, text in changes.items():
            pages[nid]["Text"] = text
        for nid in ("supper_public", "supper_stairs"):
            if nid in pages:
                pages[nid]["Text"] += '''
{n}Under cover of the voices from the table, Kiana brushes your hand and smiles at you before turning back to her friends.{/n}'''

    from storylines import kiana_round3
    kiana_round3.integrate(payload)

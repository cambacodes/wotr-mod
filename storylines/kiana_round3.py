"""Authored round-3 continuity repairs, after Kiana's round-2 appender.

No new romance requirements or recovery devices. Earlier visiting terms are
history, not a lifetime commitment. Native-service classification belongs to
the shared crossroute_presence pass and is escalated rather than overridden.
"""
import copy

from story_format import c, n, p
from storylines import kiana_partner as kp, kiana_trickster as kt

INFORMED = "kiana.partner_visits_agreed"


def page(id, text, *answers):
    return n(id, "Kiana", text, *answers, portrait="Kiana")


def retire(answer):
    # Preserve the legacy target and effects, but leave one complete sequence.
    answer["Requires"].append("trickster.now")
    answer["Forbids"].append("trickster.now")


def replace_edge(node, answer, target, **gates):
    twin = copy.deepcopy(answer)
    twin["Next"] = target
    for field, values in gates.items():
        twin.setdefault(field, []).extend(values)
    node["Choices"].append(twin)
    return twin


def integrate(payload):
    books = {s["Id"]: s for s in payload["Scenes"]}

    def pages(sid):
        return {n["Id"]: n for n in books[sid]["Nodes"]}

    if "kiana.answer" in books:
        reply = pages("kiana.answer")["reply_kiana"]
        reply["Choices"][0]["Set"].append(INFORMED)

    # Knowledge survives into discovery too: the lie may concern a new
    # lifetime promise rather than the visits Elan had already agreed to.
    if "kiana.partner_discovery" in books:
        book, ns = books["kiana.partner_discovery"], pages("kiana.partner_discovery")
        informed = copy.deepcopy(ns["kiana"])
        informed["Id"] = "kiana_informed"
        informed["Text"] = '''"You knew about our evenings. I answered your letter. I meant it."
{n}Kiana reaches for the page. Elan keeps it.{/n}
"Then I promised something else. A life after the war. I kept that from you because I wanted you home too."
{n}She looks up at him.{/n}
"You weren't away too long. You weren't unkind. I changed what I was asking for and let you keep believing my first answer."'''
        edge = ns["start"]["Choices"][0]
        replace_edge(ns["start"], edge, informed["Id"], Requires=[INFORMED])
        edge["Forbids"].append(INFORMED)
        book["Nodes"].append(informed)
    if "kiana.seelah" in books:
        book, ns = books["kiana.seelah"], pages("kiana.seelah")
        for answer in ns["start"]["Choices"]:
            if answer["Next"] == "partner_discovery":
                answer["Text"] = '"Our promise is still hidden from Elan. What has Kiana told you?"'
        if "partner_elan_letter" in ns:
            elan = copy.deepcopy(ns["partner_elan_letter"])
            elan["Id"] = "partner_elan_letter_informed"
            elan["Text"] = '''"Commander, I agreed to visits. Kiana answered me. Then the two of you promised a life I was not told about.
"I am going to speak to her. Whatever is left between us, you will not stand beside us while we decide. Don't send orders, gifts or apologies through my fellow knights. Keep away."'''
            kiana = copy.deepcopy(ns["partner_kiana_letter"])
            kiana["Id"] = "partner_kiana_letter_informed"
            kiana["Text"] = '''"He asked what I had promised you. I showed him the page. Then he asked what had become of the answer I sent him. I couldn't give him another one that didn't make it worse.
"No more invitations, Commander. I am going to speak to Elan. Keep your pages. I don't want them brought to his door."
{n}Her name is written without its customary flourish.{/n}'''
            elan["Choices"][0]["Next"] = kiana["Id"]
            edge = ns["partner_discovery"]["Choices"][0]
            replace_edge(ns["partner_discovery"], edge, elan["Id"], Requires=[INFORMED])
            edge["Forbids"].append(INFORMED)
            book["Nodes"].extend((elan, kiana))

    # The first answer is already dispatched in the informed history. The
    # morning then reads the actual guest outcome independently of that debt.
    if "kiana.date" in books and "morning_account" in pages("kiana.date"):
        book = books["kiana.date"]
        ns = pages(book["Id"])
        account = ns["morning_account"]
        account["Text"] = '''{n}Elan's letter has slipped from beneath the script. Kiana picks it up before reaching for your hand.{/n}
"He doesn't become a worse husband because I enjoyed last night. I still have to answer him."
{n}She lays it on top of the playbill.{/n}'''
        for answer in ns["morning_after"]["Choices"]:
            if answer["Next"] == "morning_account":
                replace_edge(ns["morning_after"], answer, "morning_account_informed", Requires=[INFORMED])
                answer["Forbids"].append(INFORMED)
                break
        book["Nodes"].append(page("morning_account_informed", '''{n}Kiana retrieves Elan's letter from beneath the script.{/n}
"My answer should be with him by now. I meant it. I want him home, and I want you here again. Last night hasn't changed his terms."
{n}She lays the letter on top of the playbill.{/n}'''))
        effects = tuple(account["Choices"][0]["Set"])
        for nid in ("morning_account", "morning_account_informed"):
            node = next(n for n in book["Nodes"] if n["Id"] == nid)
            if node["Choices"]:
                retire(node["Choices"][0])
            node["Choices"].extend([
                c('[Help her find her dress.]', "morning_guests_uncaptured", requires=(kt.H_BETROTHED,)),
                c('[Help her find her dress.]', "morning_guests_home", requires=(kt.WARD_GUESTS_HOME,), forbids=(kt.H_BETROTHED,)),
                c('[Help her find her dress.]', "morning_guests_captive", forbids=(kt.WARD_GUESTS_HOME, kt.H_BETROTHED)),
            ])
        for nid, text in (
            ("morning_guests_uncaptured", '''"The ward opens this morning. Our wedding never happened, but the war has found plenty of other people for those beds. Help me find my dress."'''),
            ("morning_guests_home", '''"The guests are home. One of them has already complained about the blankets. I promised to read to them this morning; help me find my dress before Arsinoe comes looking."'''),
            ("morning_guests_captive", '''"And the ward opens this morning. Our missing guests haven't come home because I finally got a night I wanted. Help me find my dress."'''),
        ):
            book["Nodes"].append(page(nid, text, c('[Spend the morning together.]', flags=effects)))

    for sid in ("kiana.morning", "kiana.trickster.late_question", "kiana.trickster.late_question_letter", "kiana.trickster.epilogue.commit"):
        if sid not in books:
            continue
        book, ns = books[sid], pages(sid)
        if "partner_terms" not in ns:
            continue
        postal = sid == "kiana.trickster.late_question_letter"
        # Retain the old account for an undisclosed affair. Append a variant
        # before the stance decision, without inferring a stance from visits.
        informed = copy.deepcopy(ns["partner_terms"])
        informed["Id"] = "partner_terms_informed"
        informed["Paragraphs"] = []  # negotiation, never a copied ending slide
        informed["Text"] = ('''{n}Kiana's next letter includes a copy of Elan's earlier answer.{/n}
"He knows about our evenings. I answered him before asking you back. Now you are asking for the rest of our lives. That wasn't in his letter.
"I still want him home when he returns. Tell me what you mean to change."''' if postal else '''{n}Kiana lays Elan's earlier answer beside the unsigned page.{/n}
"He knows about our evenings. I answered him before asking you back. Now you are asking for the rest of our lives. That wasn't in his letter."
{n}She rests her hand on his answer.{/n}
"I still want him home when he returns. Tell me what you mean to change."''')
        informed["Choices"][0]["Text"] = '"Ask Elan about the new promise. I will keep his visiting terms."'
        informed["Choices"][2]["Text"] = '"Keep this new promise between us. Let him think we still mean only visits."'
        for node in list(book["Nodes"]):
            for answer in list(node["Choices"]):
                if answer["Next"] == "partner_terms":
                    replace_edge(node, answer, informed["Id"], Requires=[INFORMED])
                    answer["Forbids"].append(INFORMED)
        book["Nodes"].append(informed)

        # In an absent-placement fallback all staging is exchanged letters.
        if postal:
            letter_text = {
                "partner_terms": '''{n}Kiana returns your page unsigned. She has added a letter.{/n}
"Before we call it settled: Elan. My knight, with his duties and his dreadful handwriting. He is still in my life.
"I wanted to tell him. Then I kept waiting for your invitations instead. Write what you are asking for."''',
                "partner_share": '''"Then he gets a letter without a princess in it. Desna help me, that will be the difficult part."
{n}Her next packet contains the letter she sent Elan: what she wants, what she has done, and the promise still awaiting your signature. One excuse is crossed out. His reply follows on another sheet.{/n}''',
                "partner_share_yes": '''"He asked me to write again. Just to him. I have.
I am still in his life. He still hates part of this. If you expect me to turn him into the villain so that our evenings feel prettier, you will be disappointed."
{n}Elan's reply and her own answer are enclosed separately. Your unsigned page is beneath them.{/n}
"There. Now send your promise."''',
                "partner_demand": '''"For yourself. You write it beautifully.
"I can leave Elan. I cannot be awarded to you afterward. He hasn't failed some test because the crusade kept him away. If I end this, he hears it from me, and you wait until I have finished."''',
                "partner_exclusive_yes": '''"He brought the things himself. I wanted to make him laugh before he left. What a rotten little coward I can be.
"I opened the case after he went. The script was on top. I couldn't read a word of it.
"I chose this. Now ask me to keep a chair for you. Ask properly."''',
                "partner_refuse": '''"Then you can expect an empty chair. Elan never ordered me to love him. I am damned if I shall leave him for someone who does.
"Withdraw it, and you can still have the evenings I offered. On his terms. I have a letter to write."
{n}Your unsigned page comes back folded inside her answer.{/n}''',
                "partner_secret": '''"The evenings he cannot give me. Don't make that sound like his fault.
"I told myself there would be no second secret. Look at what I am writing now. I want you badly enough to make a liar of myself.
"Letters to me. No officers, no gifts arriving at our door. And if he asks, I am the one who answers. You don't get to lie for me.
"If you want him to find nothing, you give the pages back. No little keepsakes under the script. I shall miss rereading them after you go."''',
                "partner_dead": '''"No. And I won't have Elan made into a convenient absence.
"His old letter is beside the script. Keep the chair. Leave his letter where I can find it."''',
                "partner_stop": '''"Then I shall need another page. I have made quite enough people wait for an honest answer."
{n}Kiana returns the unsigned promise. No invitation follows it.{/n}''',
                "partner_answer": '''"Wait for my answer, then. No speech for me to repeat."
{n}The next letter arrives in Kiana's hand.{/n}''',
                "partner_not_yet": '''"No. You have seen me with the wine and the ribbon loose. That isn't a life together yet.
"I read Elan's letter again before writing this. He waited through the crusade and the nightmare in that damned ring. I haven't decided I want to leave him. I will not send him away because you want an answer tonight."''',
            }
            for nid, text in letter_text.items():
                ns[nid]["Text"] = text

        # The yes page is the celebration. Unsettled entrants negotiate first.
        if sid in ("kiana.trickster.late_question", "kiana.trickster.late_question_letter"):
            start = ns["start"]
            yes_edge = next(a for a in start["Choices"] if a["Next"] == "yes")
            yes_edge["Forbids"].append(kp.OPEN)
            start["Choices"].extend([
                c('[Discuss the promise before signing.]', "partner_terms", requires=(kp.OPEN,), forbids=(INFORMED, "kiana.separated")),
                c('[Discuss the new promise before signing.]', informed["Id"], requires=(kp.OPEN, INFORMED), forbids=("kiana.separated",)),
                c('[Sign after the separation she chose.]', "yes", requires=(kp.OPEN, "kiana.separated")),
            ])
            for nid in ("partner_share_yes", "partner_exclusive_yes", "partner_secret", "partner_dead"):
                node = ns[nid]
                for answer in list(node["Choices"]):
                    if kt.LATE_YES in answer["Set"]:
                        replace_edge(node, answer, "promise_accepted")
                        retire(answer)
            book["Nodes"].append(page("promise_accepted", ('''{n}Only then do you sign and dispatch the page. Her answer arrives with the guest's exit crossed out.{/n}
"Then the guest stays. Come home when they let you. I've kept the chair."''' if postal else '''{n}You sign the page. Kiana reads it, folds it into her bodice and kisses you across the counter. Arsinoe puts down her pen.{/n}
"Then the guest stays. Come home when they let you. I've kept the chair."'''), c('[Keep the promise.]')))

    # Every ending producer reads the actual disclosure. Keep paragraph slots
    # stable for the shared positional contracts; append disjoint variants.
    for book in books.values():
        if book.get("Relationship") != "kiana" and book["Id"] != "kiana.lastcall.page":
            continue
        if book["Owner"] not in ("Epilogue", "AeonEpilogue"):
            continue
        for node in book["Nodes"]:
            for para in node.get("Paragraphs", []):
                text = para["Text"]
                if "Kiana kept evenings for Elan as well as the Commander" in text:
                    if book["Id"] == "kiana.ending_apart":
                        para["Text"] = "{n}Elan had agreed to the visits, though they hurt him. The Commander's courtship ended; Kiana no longer kept evenings for that guest. Elan's letter remained hers to answer.{/n}"
                    elif book["Id"] == "kiana.ending_sacrifice":
                        para["Text"] = "{n}Elan had agreed to the visits. After the Commander's death, Kiana kept Elan's letter beside the play. She went home to Elan; he held her while she cried for someone else.{/n}"
                    elif book["Id"] == "kiana.lastcall.page":
                        para["Text"] = "{n}Elan had agreed to the Commander's visits. Kiana kept his terms beside the play: she came home when he did, and military orders stayed out of their beds.{/n}"
                if "believing Kiana's private invitations concerned her play" in text:
                    para["Text"] = "{n}Elan was still in Drezen. Kiana kept the Commander's letters hidden, and the promise of a life together out of what she told her husband. Before opening the letters, she listened for Elan's step.{/n}"
                elif "Until Elan knew, every invitation" in text:
                    para["Text"] = "{n}The Commander had chosen secrecy. The promise of a life together was missing from the letters Kiana sent Elan.{/n}"
                elif "Elan died before the hidden affair could be confessed" in text:
                    para["Text"] = "{n}Elan died without hearing about the hidden promise. Kiana kept the unsent letter; she could no longer ask him to answer it.{/n}"
            node.setdefault("Paragraphs", []).append(p(
                "{n}Before the promise of a life after the war, Elan had agreed to the Commander's visits. Kiana had answered in her own hand: she wanted him home, and accepted his terms. That earlier letter said nothing about a lifetime promise.{/n}",
                requires=(INFORMED,)))
            if book["Id"] == "kiana.lastcall.page":
                node["Paragraphs"].append(p(
                    "{n}With no returned Commander to fill it, Kiana left the guest's chair empty. She kept the last page of the play without writing another entrance.{/n}",
                    requires=("engine.l12.commander_unreturned",)))

    # A commitment conversation gets its partner summary once, after the
    # selected answer has recorded its outcome. Keep legacy paragraph indices.
    sid = "kiana.trickster.epilogue.commit"
    if sid in books:
        book, ns = books[sid], pages(sid)
        for node in book["Nodes"]:
            if node["Id"] in ("margin", "stage", "blank"):
                continue
            for para in node.get("Paragraphs", []):
                para["Forbids"].append("trickster.ever")
        for nid in ("partner_share_yes", "partner_exclusive_yes", "partner_secret", "partner_dead", "partner_refuse", "partner_stop"):
            if nid not in ns:
                continue
            node = ns[nid]
            eligible = [a for a in node["Choices"] if not a.get("Next") and not a.get("Abort")]
            for answer in eligible:
                # Preserve old exits; appended complete sequence owns the slide.
                if "trickster.now" in answer["Requires"] and "trickster.now" in answer["Forbids"]:
                    continue
                replace_edge(node, answer, "partner_resolved_" + nid.removeprefix("partner_"))
                retire(answer)
            summary_text = {
                "partner_share_yes": "{n}Kiana kept Elan's new answer beside the Commander's signed promise. His terms stayed in his own hand, including the lines that had hurt to read.{/n}",
                "partner_exclusive_yes": "{n}Kiana kept the separation she had chosen. Elan had brought her things himself; his name remained in the letters she would not throw away.{/n}",
                "partner_secret": "{n}Kiana kept the Commander's promise out of her letters to Elan. The guest's place was written into the play; she hid the page before her husband came home.{/n}",
                "partner_dead": "{n}Kiana kept Elan's old letter beside the play. The Commander's promise did not fill the place it held.{/n}",
                "partner_refuse": "{n}The demand ended at Kiana's refusal. The Commander's promise remained unsigned; she sent no further invitation.{/n}",
                "partner_stop": "{n}The courtship ended with the page returned unsigned. Kiana kept her play; the guest's exit stayed on its last page.{/n}",
            }[nid]
            # The incoming choice has recorded the stance; these native
            # partner-state paragraphs need no duplicate stance selector.
            summaries = [
                p("{n}Elan was dead. Kiana kept his badly written letters, and refused to let anyone tidy them away.{/n}", requires=(kp.DEAD,)),
                p("{n}Elan was still in Drezen, attending to his duties.{/n}", requires=(kp.LIVE,), forbids=(kp.DEAD,)),
                p("{n}No certain later news of Elan reached Kiana. She asked messengers where they had last seen him.{/n}", forbids=(kp.LIVE, kp.DEAD)),
                p("{n}Elan had already agreed to the earlier visits. The new lifetime promise had not been part of that answer.{/n}", requires=(INFORMED,)),
            ]
            book["Nodes"].append(n("partner_resolved_" + nid.removeprefix("partner_"), "Narrator", summary_text, c(), paragraphs=summaries))

    # Complete the existing slot paths, including ordinary non-Trickster
    # intimacy. The legacy exits retain their targets and recorded effects.
    if "kiana.date" in books and "kiana.date.explicit.1" in pages("kiana.date"):
        book, ns = books["kiana.date"], pages("kiana.date")
        # Explicit brief: the existing first-night slot, at the initiating
        # motion; the dropped dress and promise precede this cut.
        ns["kiana.date.explicit.1"]["Text"] = '''{n}Kiana stays over you, her bare knees on either side of your hips, her fingers tight in your collar.{/n}
"Stay. I haven't finished with you."
{n}The candle burns beside the abandoned dress.{/n}'''
        old = ns["kiss"]["Choices"][0]
        if old["Next"] is None:
            twin = replace_edge(ns["kiss"], old, "kiana.date.explicit.2")
            # Lovers are recorded in the same place, after the cut.
            effects = tuple(twin["Set"])
            twin["Set"] = []
            retire(old)
            book["Nodes"].append(page("kiana.date.explicit.2", '''{n}Kiana stays over you, hot and flushed, her fingers tight in your collar.{/n}
"Damn the line. Stay."
{n}The candle burns beside the abandoned dress.{/n}''', c('[Spend the evening together.]', flags=effects)))
    for sid in ("kiana.ink_after", "kiana.unborrowed_evening"):
        if sid not in books:
            continue
        ns = pages(sid)
        slot = sid + ".explicit.1"
        if slot not in ns:
            continue
        retire(ns["kiss"]["Choices"][0])
        # Explicit brief: renewed intimacy on the desk / private bed, never
        # another first night. Default cuts at her initiating movement.
        ns[slot]["Text"] = ('''{n}Kiana holds you against her on the cleared desk, her bare knees locked round your hips. Her ink-stained hand leaves a mark on your collar.{/n}''' if sid == "kiana.ink_after" else '''{n}Kiana stays over you, catching your hand against her bare waist. The key stays in the locked door.{/n}''')

    from storylines import kiana_round4
    kiana_round4.integrate(payload)

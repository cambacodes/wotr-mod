"""Authored human marriage branches for CANON-PARTNERS-DESIGN, revision 2026-10-05.

No new fate device, affection requirement, or presence/ending eligibility rule.
The talks are letters carried between the existing invitations; Elan does not
teleport from his crusade duties. Discovery rides his native Q3 reconciliation.
Elan's Drezen placement cannot prove postwar survival: unavailable observations
are reported as uncertainty, never as a resurrection or an invented funeral.
"""
import copy

from story_format import c, n, p, scene

OPEN = "kiana.partner_unsettled"
SHARE = "kiana.partner_stance.share"
EXCLUSIVE = "kiana.partner_stance.exclusive"
SECRET = "kiana.partner_stance.secret"
EXPOSED = "kiana.partner_secret_exposed"
CAREFUL = "kiana.partner.careful_letters"
TRAIL = "kiana.partner.kept_private_page"
DISCREET = "kiana.partner.no_letter_trail"
DEAD = "kiana.elan.death_known"
LIVE = "kiana.elan.present"
DEATH_CUES = ["5736cff83ea67644bb11346947b1eb2f", "10eb3a708933ebc4c865ed9ae6e72805",
              "aebbc1845e827dd4da4e28014e7b4162"]
AFTERMATH_LIST = "a237e3aaab7c937468829bba3578770d"


def page(id, speaker, text, *answers):
    return n(id, speaker, text, *answers, portrait="Kiana")


def stance_nodes(flags):
    """Append one commitment conversation to each existing commitment host."""
    nodes = [
        page("partner_terms", "Kiana", '''"A splendid promise. Before we call it settled: Elan. My knight, with his duties and his dreadful handwriting. He is still in my life."
{n}She keeps the pen between her fingers.{/n}
"I wanted to tell him. Then I kept waiting for your invitations instead. Now tell me what you are asking for."''',
             c('"Tell Elan. I want you, and I will hear his terms."', "partner_share", forbids=(DEAD,)),
             c('"End it with Elan. I want you for myself."', "partner_demand", forbids=(DEAD,)),
             c('"Keep us secret. I want the evenings he cannot give you."', "partner_secret", forbids=(DEAD,)),
             c('"Elan is dead. There is nobody to deceive or dismiss."', "partner_dead", requires=(DEAD,)),
             c('"I cannot promise you this. We should stop."', "partner_stop")),
        page("partner_share", "Kiana", '''"Then he gets a letter without a princess in it. Desna help me, that will be the difficult part."
{n}Kiana writes beside you. She tells Elan what she wants, what she has done and the promise you have not yet made. She crosses out an excuse and leaves the ugly space visible. His answer arrives before her next invitation.{/n}''',
             c('[Read Elan\'s answer with her.]', "partner_elan_terms")),
        page("partner_elan_terms", "Elan", '''{n}Elan's hand has pressed through the paper.{/n}
"Kiana, I want a life with you. I won't say this doesn't hurt. It does. But I won't spend the crusade ordering you to sit alone until I return.
"Commander: she comes home when I do. Don't send an officer for her. Don't put your quarrels in my orders. And don't thank me as though I had given you something. I haven't."''',
             c('"Agreed. My rank stays out of this."', "partner_share_yes"),
             c('"I will not accept those terms."', "partner_stop")),
        page("partner_share_yes", "Kiana", '''"He asked me to write again. Just to him. I have."
{n}She folds Elan's letter into her own, carefully keeping the pages apart.{/n}
"I am still in his life. He still hates part of this. If you expect me to turn him into the villain so that our evenings feel prettier, you will be disappointed."
{n}She slides her letter across the table toward you.{/n}
"There. Now make your promise."''',
             c('[Promise her the next evening, and the life after the war.]', flags=(*flags, SHARE, "kiana.partner_elan_terms_kept"))),
        page("partner_demand", "Kiana", '''"For yourself. You say it beautifully."
{n}She puts the pen down.{/n}
"I can leave Elan. I cannot be awarded to you afterward. He hasn't failed some test because the crusade kept him away. If I end this, he hears it from me, and you wait until I have finished."''',
             c('"Then choose, Kiana. I will wait for your answer."', "partner_breakup"),
             c('"I expect you to do as I say."', "partner_refuse"),
             c('"Tell him instead. Let him answer us."', "partner_share")),
        page("partner_breakup", "Kiana", '''{n}Her next invitation contains two letters. Elan's is folded inside hers.{/n}
"I told him I wanted you. I told him I was ending it. Then I tried to explain how he could still be dear to me, and made it worse."
{n}She has copied the sentence she sent him.{/n}
"Elan, I am not coming home as your wife. Or waiting to become one. I am sorry. That is the answer, however much paper I waste around it."''',
             c('[Read his reply.]', "partner_elan_breakup")),
        page("partner_elan_breakup", "Elan", '''"I thought we were waiting for the same thing. I see we weren't. Keep the dress, Kiana. I don't want it sent back to the barracks.
"Commander, I will finish my duty. You will not mistake that for my blessing. When I leave her things at her door, I expect you to be elsewhere."''',
             c('[Leave them that last meeting. Then answer her invitation.]', "partner_exclusive_yes")),
        page("partner_exclusive_yes", "Kiana", '''"He brought the things himself. I wanted to make him laugh before he left. What a rotten little coward I can be."
{n}She opens the case, takes out her script and sets it on the table.{/n}
"I chose this. Now ask me to keep a chair for you. Ask properly."''',
             c('"Keep a chair for me. I will come back."', flags=(*flags, EXCLUSIVE, "kiana.separated", "kiana.partner_breakup_spoken"))),
        page("partner_refuse", "Kiana", '''"Then you can expect an empty chair. Elan never ordered me to love him. I am damned if I shall leave him for someone who does."
{n}She folds the page before you can sign it.{/n}
"Withdraw it, and you can still have the evenings I offered. On his terms. I have a letter to write."''',
             c('[Leave her.]', flags=(EXCLUSIVE, "kiana.closed", "kiana.stayed_married"))),
        page("partner_secret", "Kiana", '''"The evenings he cannot give me. Don't make that sound like his fault."
{n}She turns her ring inward, then turns it back.{/n}
"I told myself there would be no second secret. Listen to me now. I want you badly enough to make a liar of myself."
{n}She loosens the ribbon at her throat. It falls onto the folded letter.{/n}
"Letters to me. No officers, no gifts arriving at our door. And if he asks, I am the one who answers. You don't get to lie for me."''',
             c('[Keep the promise between you.]', flags=(*flags, SECRET, "kiana.affair")),
             c('"Tell him. I will face his answer."', "partner_share")),
        page("partner_dead", "Kiana", '''"No. And I won't have Elan made into a convenient absence."
{n}She lays his old letter beside the script.{/n}
"Keep the chair. Leave his letter where I can find it."''', c('[Promise to return.]', flags=flags)),
        page("partner_stop", "Kiana", '''"Then leave the pen. I shall need it."
{n}She takes the page back.{/n}
"I have made quite enough people wait for an honest answer."''', c('[End the courtship.]', flags=("kiana.closed",))),
    ]
    demand = next(node for node in nodes if node["Id"] == "partner_demand")
    demand["Choices"][0]["Next"] = "partner_answer"
    nodes.extend([
        page("partner_answer", "Kiana", '''{n}Kiana looks at the script, then at the case by her chair.{/n}
"Wait for my answer, then. No speech for me to repeat."''',
             c('[Hear her choice.]', "partner_breakup", requires=("kiana.company", "kiana.rehearsed")),
             c('[Hear her choice.]', "partner_breakup", requires=("kiana.trickster.met", "kiana.rehearsed"), forbids=("kiana.company",)),
             c('[Hear her choice.]', "partner_not_yet", forbids=("kiana.rehearsed",)),
             c('[Hear her choice.]', "partner_not_yet", requires=("kiana.rehearsed",), forbids=("kiana.company", "kiana.trickster.met"))),
        page("partner_not_yet", "Kiana", '''"No. You have seen me with the wine and the ribbon loose. That isn't a life together yet."
{n}She draws Elan's letter from beneath the script.{/n}
"He waited through the crusade, and through the wedding those demons ruined. I haven't decided I want to leave him. I will not send him away because you want an answer tonight."''',
             c('"Then tell him. I will share, on his terms."', "partner_share"),
             c('"Keep our evenings quiet instead."', "partner_secret"),
             c('"I will not share you. We end it."', "partner_stop", flags=(EXCLUSIVE, "kiana.stayed_married"))),
    ])
    secret = next(node for node in nodes if node["Id"] == "partner_secret")
    refusal = next(node for node in nodes if node["Id"] == "partner_refuse")
    if "kiana.trickster.late_yes" in flags and "kiana.committed" in flags:
        secret["Choices"].append(c("[Leave.]", forbids=("trickster.now",), abort=True))
        refusal["Choices"].append(c("[Leave.]", forbids=("trickster.now",), abort=True))
    refusal["Choices"].extend((
        c('"I withdraw it. Tell him, and let him answer us."', "partner_share"),
        c('"Keep the evenings secret instead."', "partner_secret")))
    secret["Choices"].append(c('[Return every private page. No letters or gifts left in the house.]',
        flags=(*flags, SECRET, "kiana.affair", CAREFUL)))
    secret["Text"] += '\n"If you want him to find nothing, you give the pages back. No little keepsakes under the script. I shall miss rereading them after you go."'
    return nodes


def partner_paragraphs():
    # Positive native presence and witnessed death are distinct from old grief
    # and wedding flags. The unknown branch covers absent Drezen observations.
    return [
        p("{n}Elan was dead. Kiana kept his badly written letters beside the play, and refused to let anyone tidy them away.{/n}", requires=(DEAD,)),
        p("{n}Elan was still in Drezen, attending to his duties. Elan and Kiana had separated. He left her belongings at her door. The Commander received no further welcome from Elan.{/n}", requires=(LIVE, "kiana.separated"), forbids=(DEAD,)),
        p("{n}Elan was still in Drezen. Kiana kept evenings for Elan as well as the Commander. His terms remained in his own hand: she would come home when he did, and military orders stayed out of their beds.{/n}", requires=(LIVE, SHARE), forbids=(DEAD, "kiana.separated")),
        p("{n}Elan was still in Drezen, believing Kiana's private invitations concerned her play. She hid the Commander's letters. Before opening them, she listened for Elan's step.{/n}", requires=(LIVE, SECRET), forbids=(DEAD, EXPOSED, "kiana.separated")),
        p("{n}Elan was still in Drezen. After discovering the affair, Elan asked to speak to Kiana without the Commander. She went to Elan. The Commander's chair was put away.{/n}", requires=(LIVE, EXPOSED), forbids=(DEAD,)),
        p("{n}Elan was still in Drezen, attending to his duties. Kiana kept his letters and answered when she had news. She did not ask the Commander to speak for her.{/n}", requires=(LIVE,), forbids=(DEAD, "kiana.separated", SHARE, SECRET, EXPOSED)),
        p("{n}No certain later news of Elan reached Kiana from the crusade. She kept the address for his letters and asked messengers where they had last seen him.{/n}", forbids=(DEAD, LIVE)),
        p("{n}The Commander had asked for exclusivity. Kiana kept the separation she had chosen, and told the Commander to keep Elan's name out of any boasting.{/n}", requires=(EXCLUSIVE, "kiana.separated")),
        p("{n}The Commander had demanded exclusivity; Kiana refused to exchange Elan for an order. The courtship ended with the unsigned page.{/n}", requires=(EXCLUSIVE, "kiana.stayed_married"), forbids=("kiana.separated",)),
        p("{n}Their shared arrangement remained written in Elan's letter. Kiana kept Elan's terms beside the Commander's promise, even when there was no new message to place beside either.{/n}", requires=(SHARE,), forbids=(DEAD,)),
        p("{n}After Elan's death, Kiana kept the letter in which he had agreed to their shared arrangement, including the lines that had hurt to read.{/n}", requires=(SHARE, DEAD)),
        p("{n}The Commander had chosen secrecy. Until Elan knew, every invitation was also a lie Kiana had to take home.{/n}", requires=(SECRET,), forbids=(EXPOSED, DEAD)),
        p("{n}Elan died before the hidden affair could be confessed to him. Kiana kept the unsent confession; she could no longer ask him to answer it.{/n}", requires=(SECRET, DEAD), forbids=(EXPOSED,)),
        p("{n}Elan had discovered the affair. Kiana ended the Commander's welcome and went to answer Elan herself; no later invitation undid that choice.{/n}", requires=(EXPOSED,)),
        p("{n}Kiana and Elan had parted before the news became uncertain. She asked after him as someone she had loved; she did not call the silence a reconciliation.{/n}", requires=("kiana.separated",), forbids=(DEAD, LIVE)),
    ]


def integrate(payload):
    """Called after the existing late-acceptance appender, including Last Call.

    Only Kiana entries are changed. Existing answers retain their Set and Next,
    preserving generated identities; replacements append after their siblings.
    """
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    # The containing generator isolates scene graphs and Derived. Native
    # binding maps can still be shared with authoring constants: detach them.
    payload["SeenCues"] = {**payload.get("SeenCues", {}), "kiana.elan.death_seen": DEATH_CUES[:]}
    payload["Etudes"] = {**payload.get("Etudes", {}), LIVE: "e5e3765b11eec1244a2137c2999f00d1"}
    payload.setdefault("Derived", {})[DEAD] = [["kiana.elan.death_seen"]]
    payload["Derived"][DISCREET] = [[CAREFUL]]
    payload.setdefault("DerivedForbids", {})[DISCREET] = [TRAIL]

    answer = by_id["kiana.answer"]
    start = answer["Nodes"][0]
    start["Choices"].append(c('"I still want you. Leave the decision about Elan until we speak of our future."',
        "partner_wait", requires=("trickster.now",), forbids=(DEAD, "kiana.bereaved")))
    answer["Nodes"].append(page("partner_wait", "Kiana", '''{n}Kiana leaves the case closed.{/n}
"I wrote the speech for leaving him. I couldn't send it. I wrote one for staying, and couldn't send that either. He has enough demons to fight without my dreadful compositions."
{n}She leaves her hand on the closed case.{/n}
"Come again. Before you promise to stay for good, we settle this. No magnificent promise with Elan hidden underneath it."''',
        c('[Answer her next invitation.]', flags=(OPEN, "kiana.available"))))
    # The old start reported a completed separation; deferred histories have not
    # done that. Keep the native report for the old branches, append a new entrance.
    for old in start["Choices"][:-1]:
        old["Forbids"].append(OPEN)
    start["Text"] = '''{n}Kiana sends for you without enclosing a page of the play. A small travel case stands by her chair.{/n}
"Elan. My husband. I keep rehearsing how to explain what I want, and every version sounds worse aloud."
{n}She rests her foot against the case.{/n}
"The crusade has him half the time. That does not make the other half mine to give away without a word."'''

    # Preserve the existing earned separation, but show his answer rather than
    # relying entirely on Kiana's account of their off-page conversation.
    later = next(x for x in answer["Nodes"] if x["Id"] == "later")
    old = later["Choices"][0]
    old["Forbids"].append("trickster.now")
    later["Choices"].append(c('[Read Elan\'s answer before leaving.]', "partner_old_breakup", requires=("trickster.now",)))
    answer["Nodes"].append(page("partner_old_breakup", "Elan", '''{n}Kiana hands you his reply.{/n}
"I asked you to wait while I fought. I did not think I was asking you to wait for someone else. If you cannot say you want our marriage, don't say it out of pity.
"Keep the picture. I will bring the rest of your things. Commander, give us that evening without you."''',
        c('[Leave them that evening.]', flags=tuple(old["Set"]) + ("kiana.partner_breakup_spoken",))))

    betrothal = by_id["kiana.betrothal"]
    betrothal["Nodes"][0]["Choices"].append(c('"I want you. We must speak of Elan before I promise you a life together."',
        "partner_wait", requires=("trickster.now",), forbids=(DEAD,)))
    betrothal["Nodes"].append(page("partner_wait", "Kiana", '''"My betrothed gets a voice in this too. I haven't forgotten him because somebody stamped a licence."
{n}She folds it into her script.{/n}
"Write to me. Before the guest swears to stay, we decide what I am going to tell Elan."''',
        c('[Write her an invitation.]', flags=(OPEN, "kiana.available", "kiana.attracted"))))
    truth = next(x for x in betrothal["Nodes"] if x["Id"] == "truth")
    old = truth["Choices"][0]
    old["Forbids"].append("trickster.now")
    truth["Choices"].append(c('[Read the answer Elan sent her.]', "partner_betrothal_ended", requires=("trickster.now",)))
    betrothal["Nodes"].append(page("partner_betrothal_ended", "Elan", '''"Six months for that ring. I thought I was buying something for our whole life. I threw it, then picked it up. I expect you know that already.
"Keep the dress. I won't stand in front of Abadar and wait for a vow you don't want to give. But don't ask me to laugh at the postponement again. It stopped being funny."
{n}Kiana folds his answer and puts it with the cancelled licence.{/n}''',
        c('[Leave her the choice she made. Write her an invitation.]', flags=tuple(old["Set"]) + ("kiana.partner_breakup_spoken",))))

    morning = by_id["kiana.morning"]
    morning["Nodes"][0]["Choices"].append(c('[Hear what she has left unsaid.]', "partner_morning", requires=(OPEN,), forbids=("kiana.separated", "kiana.bereaved")))
    morning["Nodes"].append(page("partner_morning", "Kiana", '''"I woke wanting you here again. Then I reached for Elan's letter. There is your splendid morning after."
{n}She rubs a dried spot of ink from her finger.{/n}
"Before you offer to stay, he comes out of the drawer."''', c('[Stay and hear her.]', "work")))

    for sid in ("kiana.morning", "kiana.trickster.late_question", "kiana.trickster.late_question_letter"):
        host = by_id[sid]
        yes = next(x for x in host["Nodes"] if x["Id"] == "yes")
        old = yes["Choices"][0]
        flags = tuple(old["Set"])
        if sid != "kiana.morning":
            # earned_outcomes adds these two baseline answers after this hook.
            # Materialize its existing guard/exit first, keeping exit index 1;
            # the proof then sees the guard and needs no extra old-page exit.
            old["Requires"].append("trickster.now")
            yes["Choices"].append(c('[Leave.]', forbids=("trickster.now",), abort=True))
        old["Forbids"].extend((OPEN, "kiana.separated"))
        yes["Choices"].append(c('[Keep her chair, and the separation she chose.]', flags=(*flags, EXCLUSIVE),
            requires=("kiana.separated",) + (() if sid == "kiana.morning" else ("trickster.now",))))
        yes["Choices"].append(c('[Settle what this promise means for Elan.]', "partner_terms", requires=(OPEN,), forbids=("kiana.separated",)))
        host["Nodes"].extend(stance_nodes(flags))

    # The older capstone can make the first promise after an already-earned
    # separation. It cannot introduce a live-marriage stance: its history gate
    # admits only separated/bereaved histories and remains unchanged.
    capstone = by_id["kiana.a_place_afterward"]
    choose = next(x for x in capstone["Nodes"] if x["Id"] == "choose")
    old = choose["Choices"][0]
    old["Forbids"].append("kiana.separated")
    choose["Choices"].append(c(old["Text"], old["Next"], flags=(*old["Set"], EXCLUSIVE),
        requires=("kiana.separated",)))

    ep = by_id["kiana.trickster.epilogue.commit"]
    start = ep["Nodes"][0]
    for old in list(start["Choices"]):
        if "kiana.trickster.late_yes" in old["Set"]:
            old["Forbids"].extend((OPEN, "kiana.separated"))
            start["Choices"].append(c(old["Text"], old["Next"], flags=(*old["Set"], EXCLUSIVE),
                requires=("kiana.separated",), forbids=("kiana.trickster.late_yes", "kiana.trickster.late_no")))
    start["Choices"].append(c('[Answer her question with Elan named between you.]', "partner_terms", requires=(OPEN,),
        forbids=("kiana.separated", "kiana.trickster.late_yes", "kiana.trickster.late_no")))
    ep["Nodes"].extend(stance_nodes(("kiana.trickster.late_yes",)))

    # Q3's surviving-couple dialog supplies Elan's native presence and timing.
    # Selecting this appended answer discovers the affair; it is not a new
    # mandatory quest or a new scene that manufactures his presence.
    discovery = scene("kiana.partner_discovery", "The letter under the script", "Kiana", 5,
        '"Elan, there is something else you should hear."', [
            page("start", "Elan", '''{n}Elan has a sheet from Kiana's play. Your name appears beneath the last line, in her hand.{/n}
"I asked her about it. Twice. The second time she answered."
{n}He looks past you, to Kiana.{/n}
"I thought I was coming home. Was I interrupting?"''', c('[Let Kiana answer.]', "kiana")),
            page("kiana", "Kiana", '''"No. Elan... no."
{n}She reaches for the page. He keeps it.{/n}
"I wanted you both. I told myself I would tell you before it became a lie. Then I kept finding another evening."
{n}Her voice breaks on the last word. She takes a breath and looks at him again.{/n}
"I lied to you. You weren't away too long. You weren't unkind. I wanted it and I lied."''', c('[Hear him.]', "elan")),
            page("elan", "Elan", '''"Don't make me listen to how much you wanted it. I've had enough of that page."
{n}He folds it once, badly.{/n}
"Come home, Kiana. Speak to me there. If there is anything left for us to say, the Commander won't be in the room."
{n}He turns to you.{/n}
"My duty is still my duty. Keep your gratitude, and keep away from my door."''', c('[Step aside.]', "end")),
            page("end", "Kiana", '''{n}Kiana passes you without looking at you.{/n}
"No more invitations. Don't send somebody to ask whether I meant it. I did."
{n}She follows Elan. The page stays in his fist.{/n}''',
                c('[Let her go.]', flags=(EXPOSED, "kiana.closed", "kiana.stayed_married"))),
        ], Relationship="kiana", AnswerLists=[AFTERMATH_LIST], ReturnToList=True,
        requires=("trickster.now", SECRET), forbids=(EXPOSED, DISCREET, "kiana.closed", DEAD, "kiana.separated", "sacrifice"), optional=True)
    payload["Scenes"].append(discovery)

    # The ordinary Q3 entry courts her after that reunion. Its existing Seelah
    # conversation supplies a second opportunity; no new rest or actor return.
    seelah = by_id["kiana.seelah"]
    seelah["Nodes"][0]["Choices"][1]["Forbids"].append(SECRET)
    seelah["Nodes"][0]["Choices"].append(c('"Elan still does not know. What has Kiana told you?"',
        "partner_discovery", requires=(SECRET,), forbids=(EXPOSED, DEAD, DISCREET)))
    quiet = copy.deepcopy(seelah["Nodes"][0]["Choices"][1])
    quiet["Forbids"].remove(SECRET)
    quiet["Requires"].extend((SECRET, DISCREET))
    seelah["Nodes"][0]["Choices"].append(quiet)
    seelah["Nodes"].extend([
        n("partner_discovery", "Seelah", '''"Less than Elan did. He found one of your letters tucked into the play. He asked me whether I knew what it meant."
{n}Seelah's face is hard.{/n}
"I didn't lie to him. He sent this for you. Kiana sent the other one. Don't ask me to carry your answer."''',
            c('[Read Elan\'s letter.]', "partner_elan_letter"), portrait="Seelah"),
        page("partner_elan_letter", "Elan", '''"Commander, I have read enough of your evenings with Kiana. She told me the rest when I asked her.
"I am going to speak to her. Whatever is left between us, you will not be standing beside us while we decide. Don't send orders, gifts or apologies through my fellow knights. Keep away."''',
            c('[Read Kiana\'s answer.]', "partner_kiana_letter")),
        page("partner_kiana_letter", "Kiana", '''"I told him I wanted you both. He asked when wanting had become lying. I couldn't give him an answer that didn't make it worse.
"No more invitations, Commander. I am going to speak to Elan. You may keep your pages. I don't want them brought to his door."
{n}Her name is written without its customary flourish.{/n}''',
            c('[Put away the letters. Let her go.]', flags=(EXPOSED, "kiana.closed", "kiana.stayed_married"))),
    ])
    # Keeping the existing farewell page abandons the no-keepsakes precaution.
    # The old answer and index remain for histories without the hidden affair.
    for host in payload["Scenes"]:
        if host.get("Relationship") != "kiana":
            continue
        for node in host["Nodes"]:
            for answer in list(node["Choices"]):
                if "kiana.farewell_kept" not in answer.get("Set", ()):
                    continue
                souvenir = copy.deepcopy(answer)
                answer["Forbids"].append(SECRET)
                souvenir["Requires"].append(SECRET)
                souvenir["Set"].append(TRAIL)
                node["Choices"].append(souvenir)

    for host in payload["Scenes"]:
        if host.get("Relationship") != "kiana" and host["Id"] != "kiana.lastcall.page":
            continue
        if host["Owner"] not in ("Epilogue", "AeonEpilogue"):
            continue
        for node in host["Nodes"]:
            # History alone cannot assert a continuing friendship. Keep the
            # paragraph's position for the existing surface inventory.
            node.setdefault("Paragraphs", [])
            for para in node["Paragraphs"]:
                if "Elan and Kiana stayed friends" in para["Text"]:
                    para["Text"] = "{n}Kiana remembered Elan laughing at the princess before the wedding. She kept that laugh in the play, even when its ending changed.{/n}"
                if "Kiana framed the licence anyway, the cancelled one" in para["Text"]:
                    # Sharing/secrecy can now keep the engagement. The old
                    # licence remains a keepsake without asserting a breakup.
                    para["Text"] = "{n}Kiana framed the licence with POSTPONED still stamped across it in red. It hung over her writing table; she told guests it was the only review of her wedding she intended to display.{/n}"
            if host["Owner"] == "AeonEpilogue":
                node["Paragraphs"].append(p("{n}The marriage to Elan, the separation and the Commander's promises belonged to the history that had been erased. In the rewritten world no letter from that courtship told Kiana what her knight's life would become.{/n}"))
                node["Paragraphs"].extend([
                    p("{n}In the lost history, Elan had written an answer to the Commander's request to share Kiana's evenings. That letter did not cross into the new world.{/n}", requires=(SHARE,)),
                    p("{n}The Commander's demand for exclusivity, and Kiana's answer concerning Elan, remained in the history that had been erased.{/n}", requires=(EXCLUSIVE,)),
                    p("{n}The secret affair and the lies Kiana had carried home to Elan left no letters in the rewritten world.{/n}", requires=(SECRET,)),
                ])
            else:
                node["Paragraphs"].extend(copy.deepcopy(partner_paragraphs()))

    # These slides previously performed a wedding even if later reports killed
    # the groom. Keep eligibility and IDs; move the act under positive presence.
    for sid in ("kiana.trickster.epilogue.debt_licence", "kiana.trickster.epilogue.betrothed_kept"):
        node = by_id[sid]["Nodes"][0]
        wedding = node["Text"]
        node["Text"] = "{n}After the war, the hold on Kiana's wedding licence ended. She unfolded it herself, without asking the Commander what to do.{/n}"
        node["Paragraphs"].insert(0, p(wedding, requires=(LIVE,), forbids=(DEAD,)))
    sacrifice = by_id["kiana.ending_sacrifice"]["Nodes"][0]
    for para in sacrifice["Paragraphs"]:
        if "kiana.widowed" in para["Requires"]:
            para["Requires"] = [DEAD]

    from storylines import kiana_round2
    kiana_round2.integrate(payload)

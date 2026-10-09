"""Authored Wenduag/Lann stance beats for CANON-PARTNERS-DESIGN, revision 2026-10-05.

Canon: AfterSex/Cue_0043 (2779fd335c035b74999afe9cd48bb2d4) names Lann
and other hunters as casual lovers; Cue_0044 (d6ea5be19a16c1e40ad4e28e82de16a7)
establishes Hosilla's coercion. Lann's four current-state etudes are read through
the existing lann.* bindings. Nothing here changes native romance or party state.

Authored additions: the claim discussion, Lann's answer, and the concealed claim
exposed by the existing morning scent event. His response follows his loyalty to
the Commander and his distrust of Wenduag; no fate device or new reconciliation.
Only Wenduag's entries in later-emitted Last Call templates are amended.
"""
import copy
import itertools

from story_format import c, p, reaction
from storylines.wenduag_trickster import (
    COMMITTED, CLOSED, LANN_GONE, LANN_HUB, LANN_IN, LANN_PAID, LANN_PAID_LATE,
    LANN_OWED, LANN_LIED_AGAIN, RETURNED, W, lann, wd,
)

ROOT = "wenduag.partner_stance."
SHARE, EXCLUSIVE, SECRET = (ROOT + suffix for suffix in ("share", "exclusive", "secret"))
STANCES = (SHARE, EXCLUSIVE, SECRET)
HERE = "wenduag.partner.lann_here"
KNOWN = "wenduag.partner.lann_knows"
SHARED = "wenduag.partner.share_answered"
SEPARATED = "wenduag.partner.separated"
DISCOVERED = "wenduag.partner.secret_discovered"
ACK = "wenduag.partner.acknowledged"
EARNED = "wenduag.partner.exclusive_earned"
REFUSED = "wenduag.partner.exclusive_refused"
CAREFUL = "wenduag.partner.scent_hidden"
E = W + "echo.abyss."


def _attendance(present, absent):
    return (c("Continue", present, requires=(HERE,)),
            c("Continue", absent, forbids=(HERE,)))


def _claim_nodes():
    nodes = [
        wd("partner_intro", '''{n}Wenduag hooks a finger into your collar, but stops short of pulling.{/n} "Lann used to share my bed in Neathholm. Other hunters, too, when I liked the look of them. He was never my husband." {n}She glances at Brask squirming on the floor.{/n} "Lann always wanted someone worth following. I knew how to make him jealous. Now you want a claim on me. How much of one?"''',
           c('"Keep Lann, if he wants you. He hears it from us."', "partner_share_call", forbids=("lann.dead",)),
           c('"End it with Lann. I want you for myself."', "partner_exclusive_offer", forbids=("lann.dead",)),
           c('"Lann need not know about us."', "partner_secret", forbids=("lann.dead",)),
           c('"Lann is dead. I will not ask you to forget him."', "partner_memory", requires=("lann.dead",))),
        wd("partner_memory", '''{n}She lets your collar go.{/n} "Dead. Yes. He could be a fool, but he was a good hunter." {n}She looks at Brask on the floor.{/n} "I chose him when I wanted him. Now I'm choosing you. Don't make a ghost stand between us."''',
           c("Continue", "want", flags=(ACK,))),
        wd("partner_share_call", '''"So I get to keep both? Greedy Commander." {n}Her thumb presses against your lower lip.{/n} "Lann may not like it. He likes being chosen. Let's hear him say it."''',
           *_attendance("partner_share_arrival", "partner_share_away")),
        wd("partner_share_arrival", '''{n}She opens the door and sends the sentry for Lann. When he arrives, she plants herself beside you, her hand still in your collar.{/n} "I chose the winner, Lann. I'm taking the Commander to bed. You can still come to mine, if you stop scowling."''',
           c("Continue", "partner_share_shock", requires=(RETURNED,),
             forbids=(LANN_PAID, LANN_PAID_LATE, LANN_OWED, LANN_LIED_AGAIN, E + "returned", W + "orchard_return")),
           c("Continue", "partner_share_lann", forbids=(RETURNED,)),
           *[c("Continue", "partner_share_lann", requires=(RETURNED, receipt))
             for receipt in (LANN_PAID, LANN_PAID_LATE, LANN_OWED, LANN_LIED_AGAIN, E + "returned", W + "orchard_return")]),
        lann("partner_share_shock", '''{n}Lann stops in the doorway. His eyes move from her face to yours.{/n} "She's alive. And this is how you tell me?" {n}His hand tightens on the doorpost.{/n} "We'll talk about that, Commander. All of it. You owe me more than a look at her teeth." {n}Wenduag bares them anyway.{/n}''',
             c("Continue", "partner_share_lann")),
        lann("partner_share_lann", '''"Convenient, choosing the winner after the fight. You always did know how to make a man feel welcome, Wendu." {n}He looks past her at the blood on Brask's shirt, then at you.{/n} "I'm not claiming her. Never did. But I'm not crawling into a bed to prove I'm braver than you, either. If I come, it's because I want her." {n}His crooked smile returns, briefly.{/n} "And if she sells you to a demon, don't expect me to help her count the money."''',
             c('"No contests over her bed. That goes for all of us."', "partner_share_reply")),
        wd("partner_share_reply", '''"Hear that, Lann? You can still come hunting. Try not to shoot the Commander." {n}Lann gives her a flat look.{/n} "Try not to give me a reason." {n}He leaves. She watches him go, then pulls your collar taut.{/n} "He'll come when he wants to. Now tell me what you want done with this one."''',
           c("Continue", "want", flags=(SHARE, SHARED, KNOWN, ACK))),
        wd("partner_share_away", '''"Lann isn't here to answer. I'm not going to wag his head for him." {n}She releases your collar.{/n} "If he comes back, I'll tell him. He can want me or walk away. Until then, you get no promise from him." {n}She nudges Brask with her boot.{/n} "This one is here. Decide."''',
           c("Continue", "want", flags=(SHARE, ACK))),
        wd("partner_exclusive_offer", '''{n}Her grip tightens. She smiles against your mouth without kissing it.{/n} "All for yourself. I like hearing you say it." {n}Her teeth catch your lip, briefly.{/n} "I'll stop taking Lann to bed. But don't start sleeping soundly because I said yes. I still want to see you throw me off that table."''',
           c('"Then tell him. I will stand beside you."', "partner_exclusive_call"),
           c('"Keep him, if he agrees. I withdraw the demand."', "partner_share_call")),
        wd("partner_exclusive_call", '''"Beside me. Good." {n}She lets go of your collar and looks toward the door.{/n}''',
           *_attendance("partner_exclusive_arrival", "partner_exclusive_away")),
        wd("partner_exclusive_arrival", '''{n}She sends the sentry for Lann. When he arrives, she takes your hand and lays it on her hip.{/n} "I chose the winner, Lann. No more nights with me. Don't come knocking after the watch."''',
           c("Continue", "partner_exclusive_shock", requires=(RETURNED,),
             forbids=(LANN_PAID, LANN_PAID_LATE, LANN_OWED, LANN_LIED_AGAIN, E + "returned", W + "orchard_return")),
           c("Continue", "partner_exclusive_lann", forbids=(RETURNED,)),
           *[c("Continue", "partner_exclusive_lann", requires=(RETURNED, receipt))
             for receipt in (LANN_PAID, LANN_PAID_LATE, LANN_OWED, LANN_LIED_AGAIN, E + "returned", W + "orchard_return")]),
        lann("partner_exclusive_shock", '''"Alive." {n}Lann says it once, looking at her, then turns on you.{/n} "You let me believe she was dead. And now you've brought me here to tell me whose bed she's in." {n}He draws a breath through his nose.{/n} "I'm going to hear the rest, Commander. Don't think this settles it."''',
             c("Continue", "partner_exclusive_lann")),
        lann("partner_exclusive_lann", '''{n}Lann's jaw works. He looks at her hand over yours.{/n} "The winner. You waited until after the fight to choose. Right. No knocking. I can manage that." {n}He turns to you.{/n} "I follow you into battles I know we shouldn't survive. Now you're asking me to step aside for you here, too. Fine. She said it herself. But you'd better be able to stay when she makes it hard. That's the part she never thinks anyone can do."''',
             c('"I heard you, Lann."', "partner_exclusive_reply")),
        wd("partner_exclusive_reply", '''{n}Lann shuts the door. Wenduag listens to his footsteps until they fade.{/n} "He didn't ask me twice. Good." {n}She turns back and presses your hand harder against her hip.{/n} "I chose. Now you choose. Your sergeant's getting blood on the floor."''',
           c("Continue", "want", flags=(EXCLUSIVE, SEPARATED, KNOWN, ACK))),
        wd("partner_exclusive_away", '''"He's not here. I can't tell him to his face." {n}She takes your hand and puts it on her hip.{/n} "I'm done bedding him. If he returns, I'll say it with you standing there. Until then, he hasn't heard it. Don't boast that he stepped aside for you."''',
           c("Continue", "want", flags=(EXCLUSIVE, ACK))),
        wd("partner_secret", '''"You want me, but you don't want his eyes on you." {n}She laughs into your neck.{/n} "I never promised Lann I'd keep to his bed. You're hiding your claim, not stealing a wife." {n}Her teeth press against your neck, then release.{/n} "If he gets close enough, he'll smell me on you. Then you get to answer him. And if he won't touch me afterwards, I won't beg him to. Still want it?"''',
           c('"Yes. Let him find out for himself."', "want", flags=(SECRET, ACK)),
           c('"No. We tell him."', "partner_share_call")),
    ]
    next(node for node in nodes if node["Id"] == "partner_intro")["Choices"][1]["Next"] = "partner_exclusive_answer"
    nodes.extend([
        wd("partner_exclusive_answer", '''{n}Wenduag studies your face, her hand still in your collar.{/n} "You've seen what I do when somebody offers me more. Do you think you've given me a reason to stay?"''',
           c("Continue", "partner_exclusive_offer", requires=(EARNED,)),
           c("Continue", "partner_exclusive_refused", forbids=(EARNED,))),
        wd("partner_exclusive_refused", '''"No. Lann's a good hunter. I won't send him away because you've decided that keeping me alive bought you every night."
{n}Her thumb presses your throat.{/n} "Take the nights I give you. He may still knock on my door after you leave. Or walk out. Brask will keep bleeding while you decide."''',
           c('"I withdraw it. Tell Lann I will share."', "partner_share_call"),
           c('"Keep our nights secret instead."', "partner_secret"),
           c('"Then you get no claim on me. We end it."', flags=(EXCLUSIVE, REFUSED, CLOSED))),
    ])
    secret = next(node for node in nodes if node["Id"] == "partner_secret")
    secret["Choices"].append(c('[Wash and change before returning to Lann. Keep her scent out of the barracks.]', "want",
                               flags=(SECRET, ACK, CAREFUL)))
    secret["Text"] += '\n"Cold water before dawn, then. No wearing my smell like a trophy. I liked the thought of him catching it."'
    return nodes


def ending_paragraphs():
    """Current state wins over remembered presence; stance never invents his answer."""
    return [
        p("{n}Lann remained in the Commander's company. His old nights with Wenduag in Neathholm had bound neither of them to one bed.{/n}",
          requires=(LANN_IN,), forbids=LANN_GONE),
        p("{n}Lann was dead. Whatever claims had been made over Wenduag's bed, there would be no answer from the hunter who had shared it in Neathholm.{/n}", requires=("lann.dead",)),
        p("{n}The Commander had dismissed Lann. He was outside the company now; his old place beside Wenduag bought him no invitation back.{/n}",
          requires=("lann.kicked_out",), forbids=("lann.dead",)),
        p("{n}Lann was away from the company. His place in Wenduag's old cave life remained, but nobody could answer for his present wishes.{/n}",
          requires=("lann.plot_absent",), forbids=("lann.dead", "lann.kicked_out")),
        p("{n}There was no word of Lann. Wenduag had named him as a lover in Neathholm; nothing proved where he was now.{/n}",
          forbids=(LANN_IN, *LANN_GONE)),
        # Native companion reads can overlap in retained histories. Departure
        # wins physical presence, but each live native read still has coverage.
        p("{n}Lann lived, but was outside the Commander's company. His old nights with Wenduag in Neathholm had never bought either lover a promise to return.{/n}",
          requires=(LANN_IN,), forbids=("lann.dead",), any_groups=(("lann.kicked_out", "lann.plot_absent"),)),
        p("{n}Lann was outside the company. Even the reports of his absence offered no news of the hunter who had once shared Wenduag's bed.{/n}",
          requires=("lann.plot_absent", "lann.kicked_out"), forbids=("lann.dead",)),
        p("{n}The Commander had accepted sharing Wenduag. Lann had heard the invitation and refused a contest over her bed. His bow stayed with the crusade; his nights were still his to choose. Wenduag kept inviting him to hunt.{/n}",
          requires=(COMMITTED, SHARE, SHARED, LANN_IN), forbids=LANN_GONE),
        p("{n}The Commander had accepted sharing Wenduag, but Lann had been absent from that bargain. His answer was still his to give.{/n}",
          requires=(COMMITTED, SHARE), forbids=(SHARED, "lann.dead")),
        p("{n}At the Commander's demand, Wenduag had ended her nights with Lann. Lann had heard it from her own mouth. Lann still followed the Commander. He never knocked at her door after the watch.{/n}",
          requires=(EXCLUSIVE, SEPARATED, LANN_IN), forbids=LANN_GONE),
        p("{n}The Commander had demanded Wenduag alone. Her answer had bought no word from him; none was put in his mouth.{/n}",
          requires=(EXCLUSIVE,), forbids=(SEPARATED, "lann.dead")),
        p("{n}Wenduag had refused the exclusive claim. The Commander insisted and lost her bed. Lann's place remained his to accept; she had promised him no new loyalty.{/n}", requires=(EXCLUSIVE, REFUSED)),
        p("{n}The Commander had hidden the claim on Wenduag from Lann. He caught her scent after their night together and ended his own nights with her. Lann still fought beside the Commander, but would share no private jokes with either lover.{/n}",
          requires=(COMMITTED, SECRET, DISCOVERED, LANN_IN), forbids=LANN_GONE),
        p("{n}The Commander's claim on Wenduag was still concealed from Lann. No accusation had reached the lovers; no pardon had been asked or given.{/n}",
          requires=(COMMITTED, SECRET), forbids=(DISCOVERED, "lann.dead")),
        p("{n}Lann had discovered the concealed claim and refused Wenduag's bed. His later absence did not undo that parting.{/n}",
          requires=(COMMITTED, SECRET, DISCOVERED), forbids=("lann.dead",), any_groups=(("lann.kicked_out", "lann.plot_absent"),)),
        p("{n}Lann had heard Wenduag end their nights together. Wenduag kept to the Commander's exclusive claim after Lann left.{/n}",
          requires=(EXCLUSIVE, SEPARATED), forbids=("lann.dead",), any_groups=(("lann.kicked_out", "lann.plot_absent"),)),
        p("{n}Lann had answered the offer to share Wenduag while he was still with the company. With no word of him now, neither lover could say whether he would seek her out again.{/n}",
          requires=(COMMITTED, SHARE, SHARED), forbids=(LANN_IN, *LANN_GONE)),
        p("{n}Lann had heard Wenduag end their nights together. There was no word of Lann now. Wenduag kept to the Commander's exclusive claim.{/n}",
          requires=(EXCLUSIVE, SEPARATED), forbids=(LANN_IN, *LANN_GONE)),
        p("{n}Lann had discovered the concealed claim and refused Wenduag's bed. There was no word of him now, and no reconciliation.{/n}",
          requires=(COMMITTED, SECRET, DISCOVERED), forbids=(LANN_IN, *LANN_GONE)),
        p("{n}Lann had answered the offer to share Wenduag. After he left the company, there was no news of another visit to her bed.{/n}",
          requires=(COMMITTED, SHARE, SHARED), forbids=("lann.dead",), any_groups=(("lann.kicked_out", "lann.plot_absent"),)),
        p("{n}With Lann dead, the Commander's offer to share Wenduag could remain only an offer. Their nights in Neathholm were over.{/n}", requires=(COMMITTED, SHARE, "lann.dead")),
        p("{n}Lann was dead now. Wenduag had answered the exclusive demand herself; no new answer could come from her former lover.{/n}", requires=(EXCLUSIVE, "lann.dead")),
        p("{n}The Commander had concealed the claim on Wenduag. Lann was dead now; neither lover had received a pardon from him.{/n}", requires=(COMMITTED, SECRET, "lann.dead")),
        p("{n}The Commander made no new bargain about Lann. Wenduag's old cave lovers had never promised each other exclusivity.{/n}", forbids=STANCES),
        p("{n}They had spoken of Lann, but the Commander had never accepted Wenduag's claim. There were no nights with the Commander to share or conceal.{/n}",
          forbids=(COMMITTED,), any_groups=(STANCES,)),
        p("{n}Lann had heard the proposed arrangement and answered for himself. The Commander then refused Wenduag's gift; the invitation to share her bed went no further.{/n}",
          requires=(SHARE, SHARED), forbids=(COMMITTED,)),
    ]


def _native_variants(payload, scenes):
    """E14d renders Text only. Compile the same conditions into text variants.

    The variants partition existing eligibility; none grants a new ending.
    Preserve the original replacement IDs and the order of existing variants.
    Retained overlapping companion reads are explicit in each text's guards.
    """
    current = (LANN_IN, *LANN_GONE)
    states = [("dead", {"lann.dead"}, set())]
    for bits in itertools.product((False, True), repeat=3):
        live = (LANN_IN, "lann.kicked_out", "lann.plot_absent")
        positive = {flag for flag, bit in zip(live, bits) if bit}
        negative = {"lann.dead", *(flag for flag, bit in zip(live, bits) if not bit)}
        name = "_".join(label for label, bit in zip(("in_party", "dismissed", "absent"), bits) if bit) or "unknown"
        states.append((name, positive, negative))
    positions = [
        ("unchosen", set(), set(STANCES)),
        ("share_pending", {SHARE}, {EXCLUSIVE, SECRET, SHARED}),
        ("share_answered", {SHARE, SHARED}, {EXCLUSIVE, SECRET}),
        ("exclusive_pending", {EXCLUSIVE}, {SHARE, SECRET, SEPARATED}),
        ("exclusive_answered", {EXCLUSIVE, SEPARATED}, {SHARE, SECRET}),
        ("secret_kept", {SECRET}, {SHARE, EXCLUSIVE, DISCOVERED}),
        ("secret_exposed", {SECRET, DISCOVERED}, {SHARE, EXCLUSIVE}),
    ]

    def visible(para, flags):
        return (set(para["Requires"]) <= flags and not set(para["Forbids"]) & flags
                and all(set(group) & flags for group in para["AnyGroups"]))

    paragraphs = ending_paragraphs()
    # The existing ending inventory aligns these native texts to these exact
    # authored outcomes at finalization. Copy that eligibility before splitting
    # the texts; the route's contract rows keep each split aligned afterwards.
    outcomes = {
        W + "epilogue.native_pack": W + "epilogue.pack",
        W + "epilogue.native_greybor": W + "epilogue.pack",
        W + "epilogue.native_ember": W + "epilogue.pack",
        W + "epilogue.native_greybor_back": W + "epilogue.native_commander_back",
    }
    originals = {id: copy.deepcopy(scenes[id]) for id in set(outcomes.values())}
    for edit in payload.get("NativeEpilogueEdits", {}).values():
        if any(".partner." in variant["Replacement"] for variant in edit.get("Variants", [])):
            continue
        additions = []
        for variant in [edit, *edit.get("Variants", [])]:
            original = scenes.get(variant["Replacement"])
            if original is None or original.get("Relationship") != "wenduag":
                continue
            source = copy.deepcopy(original)
            if source["Id"] in outcomes:
                outcome = originals[outcomes[source["Id"]]]
                for field in ("Requires", "RequiresAny", "RequiresAnyGroups", "Forbids", "ForbidOverrides"):
                    source[field] = copy.deepcopy(outcome.get(field, {} if field == "ForbidOverrides" else []))
                source["Requires"] = list(dict.fromkeys([*source["Requires"], "trickster.now"]))
                for field in ("Requires", "RequiresAny", "RequiresAnyGroups", "Forbids", "ForbidOverrides"):
                    original[field] = copy.deepcopy(source[field])
            when = copy.deepcopy(variant["When"])
            # The existing ID keeps the unchosen/unknown case. No conditional
            # paragraph ever reaches the native replacement renderer.
            original["Forbids"].extend([*current, *STANCES])
            native_only_greybor = source["Id"] == W + "epilogue.native_greybor_back"
            if native_only_greybor:
                # The preceding kept-pack variant already owns every committed
                # history. Preserve that ordering instead of declaring a second
                # selectable replacement for the same history.
                original["Forbids"].append(COMMITTED)
            original["Nodes"][0]["Text"] += "\n" + "\n".join(
                para["Text"] for para in paragraphs if visible(para, set(source["Requires"])))
            variant["When"] = [list(dict.fromkeys([*group, *("!" + flag for flag in (*current, *STANCES)),
                                                    *( ["!" + COMMITTED] if native_only_greybor else [])])) for group in when]
            for (state, positive, negative), (position, chosen, unchosen) in itertools.product(states, positions):
                if state == "unknown" and position == "unchosen":
                    continue
                # Native Commander-return slides also serve the original game
                # romance. An unchosen stance has identical text with or without
                # RRT commitment; chosen stances must preserve that distinction.
                commitments = (True,) if COMMITTED in source["Requires"] else ((None,) if position == "unchosen" else (False, True))
                if native_only_greybor and position != "unchosen":
                    commitments = (False,)
                for committed in commitments:
                    required, forbidden = positive | chosen, negative | unchosen
                    flags = set(source["Requires"]) | required
                    if native_only_greybor:
                        forbidden = forbidden | {COMMITTED}
                    if committed is True:
                        required = required | {COMMITTED}
                        flags.add(COMMITTED)
                    elif committed is False:
                        forbidden = forbidden | {COMMITTED}
                        flags.discard(COMMITTED)
                    text = "\n".join(para["Text"] for para in paragraphs if visible(para, flags))
                    item = copy.deepcopy(source)
                    item["Id"] = source["Id"] + ".partner." + state + "." + position + (".uncommitted" if committed is False else "")
                    item["Requires"] = list(dict.fromkeys([*source["Requires"], *sorted(required)]))
                    item["Forbids"] = list(dict.fromkeys([*source["Forbids"], *sorted(forbidden)]))
                    item["Nodes"][0]["Text"] += "\n" + text
                    item["Nodes"][0].pop("Paragraphs", None)
                    payload["Scenes"].append(item)
                    signed = [*sorted(required), *("!" + flag for flag in sorted(forbidden))]
                    additions.append(dict(Replacement=item["Id"], KeepNativeImage=False,
                                          When=[list(dict.fromkeys([*group, *signed])) for group in when]))
        if additions:
            edit.setdefault("Variants", []).extend(additions)


def integrate(payload):
    payload.setdefault("Derived", {})[EARNED] = [["trickster.now", flag] for flag in
        ("wenduag.romance_finished.latched", W + "cairn.water")]
    payload.setdefault("Derived", {})[HERE] = [[LANN_IN]]
    payload.setdefault("DerivedForbids", {})[HERE] = list(LANN_GONE)
    scenes = {item["Id"]: item for item in payload["Scenes"]}
    for suffix in ("court.claim", "court.claim_in_person"):
        claim = scenes[W + suffix]
        next(node for node in claim["Nodes"] if node["Id"] == "why")["Choices"][0]["Next"] = "partner_intro"
        claim["Nodes"].extend(_claim_nodes())

    # struct2-09: exclusivity refusal is a distinct closure. It never records
    # the old claim_refused receipt, whose page says Brask was released.
    refused = copy.deepcopy(scenes[W + "epilogue.refused"])
    refused["Id"] = W + "epilogue.exclusive_refused"
    refused["Requires"] = [REFUSED if flag == W + "court.claim_refused" else flag
                           for flag in refused["Requires"]]
    refused["Nodes"][0]["Text"] = (
        '{n}Wenduag brought the Commander the best thing she had caught, once, and the Commander wanted all of her for it. She would not send Lann away because a gift had been taken, and she said so, and when the Commander would not take less she pulled her hood up and walked out over the sergeant on the floor. She did not ask again. She had never asked anybody before; she said afterwards that now she knew what it cost.{/n}\n'
        '{n}What became of Brask once the door shut behind her was never told in the cellars, and the neathers learned not to ask. She fought the rest of the war where the fighting was worst, because she was not stupid, and she kept to the dark between battles, and nobody said the Commander\'s name in her hearing. When the war ended she was gone before the banners came down, with a band of her own, east, toward the edge of the Wound, where there was still something worth hunting.{/n}')
    payload["Scenes"].append(refused)

    # Keep the saved original morning reaction for openly chosen / unchosen bonds.
    # The concealed claim uses the same scent event, host, chapter and presence guard.
    morning = scenes[W + "react.lann_morning"]
    morning["Forbids"].append(SECRET)
    discovery = reaction("Lann", W + "react.lann_secret", tuple(morning["Requires"]) + (SECRET,),
        '''{n}Lann waits at the cellar stair. He draws a breath as you approach.{/n} "You smell like her. Every neather down there knows. Did you think I wouldn't?" {n}He looks toward the dark below.{/n} "She never promised me one bed. But you let me stand beside you like a fool while you hid this. I thought we were past that." {n}His voice hardens.{/n} "Tell Wendu I'm not coming tonight. Or any other night. I'll fight your war, Commander. Find someone else to laugh with after it."''',
        answer_list=LANN_HUB, relationship="wenduag", entry='"You have something to say, Lann?"',
        chapter=5, last=5, portrait="Lann", forbids=LANN_GONE + (CLOSED, DISCOVERED, CAREFUL),
        flags=(DISCOVERED, SEPARATED, KNOWN), Chapters=[5])

    # Supported hub dialogue: Lann hears an answer before making his own parting.
    discovery["Reaction"] = False
    first = discovery["Nodes"][0]["Choices"][0]
    first.update(Text='"I hid the claim. You deserved to hear it from me."', Next="fallout")
    discovery["Nodes"][0]["Choices"].append(c(
        '"She never promised you one bed. I should still have told you."', "fallout",
        flags=(DISCOVERED, SEPARATED, KNOWN)))
    discovery["Nodes"].append(lann("fallout",
        '{n}Wenduag comes up the stair with a hare over her shoulder. Lann steps out of her way.{/n} '
        '"No more knocking, Wendu. And no more jokes about what you hide from me." '
        '{n}He leaves for the muster. She watches him go.{/n}', c("Continue", "wenduag_reply")))
    discovery["Nodes"].append(wd("wenduag_reply",
        '"He can keep his nights. I have supper here." '
        '{n}She thrusts the hare into your hands, harder than she needs to.{/n}', c("Continue")))
    payload["Scenes"].append(discovery)
    quiet = copy.deepcopy(discovery)
    quiet["Id"] = W + "react.lann_secret_quiet"
    # Two pages make this a hub conversation, not an E6 one-page reaction.
    quiet["Reaction"] = False
    quiet["Requires"].append(CAREFUL)
    quiet["Forbids"].remove(CAREFUL)
    quiet["Entry"] = '"The night watch was quiet, Lann?"'
    quiet["Nodes"][0]["Text"] = '''{n}Lann waits by the cellar stair with his bow. Your hair is wet; the clean shirt clings coldly to your back.{/n}
"Nothing to report. Wendu's hunters came in before dawn. Tell her to stop leaving bloody arrows in the wash trough."
{n}He shoulders the bow and goes to the muster. Wenduag watches from the stair below. She bares her teeth when you fail to come back down.{/n}'''
    # Preserve the careful-secret exit at index 0 and unwashed return at index 1.
    quiet["Nodes"][0]["Choices"] = [quiet["Nodes"][0]["Choices"][0]]
    quiet["Nodes"][0]["Choices"][0].update(Text="Continue", Next=None, Set=[])
    caught = copy.deepcopy(discovery["Nodes"][0])
    caught["Id"] = "caught"
    quiet["Nodes"][0]["Choices"].append(c('[Go back down to Wenduag. Return to Lann without washing again.]', "caught"))
    # Preserve quiet/start and caught before appending the new aftermath node.
    quiet["Nodes"] = [quiet["Nodes"][0], caught, *copy.deepcopy(discovery["Nodes"][1:])]
    payload["Scenes"].append(quiet)

    # A claim disclosure reveals survival but does not pay the old cairn debt.
    # Keep those conversations and all their answer indices, with a new entrance
    # for Lann who has already seen her during the stance discussion.
    truth = scenes[W + "lann.truth"]
    truth["Entry"] = '"Walk with me, Lann. I owe you the truth about Wenduag."'
    why = next(node for node in truth["Nodes"] if node["Id"] == "why")
    why["Text"] = why["Text"].replace("And you're telling me now. Before I found out. Why?", "And you're telling me how you did it. From your own mouth. Why?")
    start = truth["Nodes"][0]
    start["Choices"][0]["Forbids"].append(KNOWN)
    start["Choices"].append(c('"You saw Wenduag. I owe you the rest."', "how", requires=(KNOWN,)))
    found = scenes[W + "lann.found_out"]
    start = found["Nodes"][0]
    start["Text"] = '''{n}Lann is sitting on the wall with his bow across his knees. He runs his thumb along it, then looks up at you.{/n} "Wendu. There's something we haven't settled, Commander."'''
    for answer in start["Choices"]:
        answer["Forbids"].append(KNOWN)
    start["Choices"].append(c("Continue", "partner_already_seen", requires=(KNOWN,)))
    found["Nodes"].append(lann("partner_already_seen", '''"I know she's alive. You didn't tell me how she got out of that grave." {n}He stands.{/n} "I'm listening now. And I want the whole thing."''', c("Continue", "price")))

    # Old trust receipts describe the cairn, not the stance. They still cost exactly
    # what they did before; an explicit disclosure must not coexist with "never knew".
    native_ids = {variant["Replacement"] for edit in payload.get("NativeEpilogueEdits", {}).values()
                  for variant in [edit, *edit.get("Variants", [])]}
    for item in payload["Scenes"]:
        if item.get("Relationship") != "wenduag" or not item["Owner"].endswith("Epilogue"):
            continue
        if item["Id"] in native_ids:
            continue
        for node in item["Nodes"]:
            for para in node.get("Paragraphs", []):
                if "Lann" in para["Text"] and not any(flag in para["Requires"] for flag in LANN_GONE):
                    if LANN_IN not in para["Requires"]:
                        para["Requires"].append(LANN_IN)
                if para["Text"].startswith("{n}Lann never learned"):
                    para["Forbids"].append(KNOWN)
            node.setdefault("Paragraphs", []).extend(ending_paragraphs())

    for item in payload["Scenes"]:
        if item.get("Relationship") == "wenduag" and item["Owner"].endswith("Epilogue") and item["Id"] not in native_ids:
            item["Nodes"][0]["Paragraphs"].append(p(
                '{n}Savamelekh was dead. The Commander had never brought Savamelekh\'s stinger down the stair, '
                'or answered Wenduag\'s demand to do the killing herself.{/n}',
                requires=(W + "death_promised", "savamelekh.dead"), forbids=(W + "court.stinger",)))

    _native_variants(payload, scenes)

    from storylines import lastcall_partners
    part = next(part for part in lastcall_partners.PARTNERS if part["key"] == "wenduag")
    if any(SHARE in para["Requires"] for para in part["paragraphs"]):
        return
    part["paragraphs"] = copy.deepcopy(list(part["paragraphs"]))
    for para in part["paragraphs"]:
        if "wenduag.romance_finished.latched" in para["Requires"] and COMMITTED in para["Forbids"]:
            para["Text"] = ("{n}Wenduag had stayed beside the Commander through Savamelekh's lair and past it. "
                            "She had never been buried. She needed no cairn stone to find her way back to that bed.{/n}")
        if "Lann" in para["Text"] and not any(flag in para["Requires"] for flag in LANN_GONE):
            para["Requires"].append(LANN_IN)
            para["Forbids"].extend(flag for flag in LANN_GONE if flag not in para["Forbids"])
            if "They waited together" in para["Text"]:
                para["Forbids"].append(DISCOVERED)

    for para in part["paragraphs"]:
        if "dead_on_record" in " ".join(para["Requires"]):
            para["Text"] = para["Text"].replace("The world buried the Commander with an empty coffin and a great deal of singing.",
                "At the Commander's funeral, Wenduag kept to the shadow of the cellar stair.")
            para["Text"] = para["Text"].replace("The world buried the Commander, with an empty coffin and a great deal of singing.",
                "At the Commander's funeral, Wenduag kept to the shadow of the cellar stair.")
        if "wenduag.romance_finished.latched" in para["Requires"] and COMMITTED in para["Forbids"]:
            para["Text"] = ('{n}Wenduag had stayed beside the Commander through Savamelekh\'s lair and past it. '
                'After the war she came back from hunting, shoved the maps aside and ate at the Commander\'s table. '
                'When she finished, she pulled the Commander away from it.{/n}')
    for para in part["paragraphs"]:
        para["Text"] = para["Text"].replace("Lann, who had never once gone down the cellar stair, came down it at dawn and found her sitting on the cairn",
            "Lann, who had kept away from the cellar stair, came down at dawn and found her waiting at its foot")
    part["paragraphs"].extend(ending_paragraphs())
    part["paragraphs"].extend([
        p('{n}Savamelekh was dead. She had not forgotten the killing promised to her, or the stinger nobody had brought down the stair.{/n}',
          requires=(W + "death_promised", "savamelekh.dead"), forbids=(W + "court.stinger",)),
        p('{n}She still carried the deep stroke in her side. Her finger found the seam once while she waited. '
          'She had not forgotten whose hand made it, or her promise to pay it back.{/n}', requires=(W + "cost.stroke_deep",)),
        p('{n}The promised killing was still owed. Savamelekh\'s severed stinger had not paid it. '
          'Wenduag kept her spear beside the stair and her next choice of prey to herself.{/n}', requires=(W + "promise.owed",)),
    ])

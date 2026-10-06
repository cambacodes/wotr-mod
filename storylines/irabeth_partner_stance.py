"""Authored marriage choices, not native marriage or presence changes.

Canon: HorgusAnevia/Cue_0024 (377de2648a0f24d42864709080f850b9),
IrabethDies/Cue_0013 (1f6f05c729cf7274390fa5c640436dcc).
The secret history withdraws the negotiated arrangement under a false pretext;
the existing pre-battle audience exposes it. No new return, payment or pardon.
"""
import copy
from story_format import c, n, p, scene

SHARE = "irabeth.partner_stance.share"
EXCLUSIVE = "irabeth.partner_stance.exclusive"
SECRET = "irabeth.partner_stance.secret"
EXPOSED = "irabeth.partner_stance.discovered"
RETURNED = "anevia.trickster.returned"


def ending_paragraphs():
    """Current wife state; a return never substitutes for an unearned body."""
    return [
        p('{n}Anevia and Irabeth remained wives. Anevia still expected Beth home when she said she would be, and still had plenty to say when she was late.{/n}',
          forbids=("anevia_dead", "anevia_gone", RETURNED, "irabeth_dead", "irabeth_gone")),
        p('{n}Anevia lived, and Irabeth had come back from Iz to their marriage. Nevi still expected Beth to come home when she said she would.{/n}',
          requires=("irabeth.trickster.returned", "irabeth_dead"), forbids=("anevia_dead", "anevia_gone", RETURNED)),
        p("{n}Anevia was alive, but Irabeth had not returned from death. She kept Beth's name out of the Commander's invitations; mourning her wife was her own business.{/n}",
          requires=("irabeth_dead",), forbids=("irabeth.trickster.returned", "anevia_dead", "anevia_gone", RETURNED)),
        p("{n}Anevia lived. Irabeth had left the Commander's service; her marriage had not become vacant because her post had.{/n}",
          requires=("irabeth_gone",), forbids=("irabeth_dead", "anevia_dead", "anevia_gone", RETURNED)),
        p('''{n}Anevia had come back on her own terms. "Back this far," she had said. "Don't start makin' plans for me." Coming back to the gate did not mean forgiving Drezen, or surrendering her right to leave it.{/n}''',
          requires=(RETURNED,), forbids=("anevia_dead",)),
        p("{n}Anevia had gone south and remained away. Irabeth kept sending word south, but never called silence her wife's agreement.{/n}",
          requires=("anevia_gone",), forbids=("anevia_dead", RETURNED, "irabeth.trickster.nevi_answered")),
        p('''{n}Anevia had gone south and remained away. Her answer had come back by the south-road courier: "Keeping it. Ask me to my face next time, Beth." The marriage continued at a distance; her reply did not promise a return to Drezen.{/n}''',
          requires=("anevia_gone", "irabeth.trickster.nevi_answered"), forbids=("anevia_dead", RETURNED)),
        p("{n}Anevia was dead. Irabeth's wedding ring remained a reminder of their marriage; nothing promised to the Commander replaced her.{/n}",
          requires=("anevia_dead",)),
        p('{n}The Commander had agreed to share Irabeth\'s life with her marriage. Her wife\'s answer had been plain: "The nights she promised me stay mine. Don\'t make me come lookin\' for her."{/n}',
          requires=(SHARE,), forbids=(SECRET, EXCLUSIVE)),
        p('{n}The demand that Irabeth leave her wife had met a flat refusal. She kept her marriage; the Commander lost the invitation to her bed.{/n}',
          requires=(EXCLUSIVE,)),
        p('{n}Her wife had been told the courtship was over. The promise made behind her back remained an affair, not an arrangement she had accepted.{/n}',
          requires=(SECRET,), forbids=(EXPOSED,)),
        p('{n}When her wife uncovered the affair, Irabeth chose her marriage. Their marriage survived a bitter quarrel; the Commander\'s welcome did not.{/n}',
          requires=(SECRET, EXPOSED)),
        p('{n}Irabeth had sent her confession south. No answer had arrived. She had stopped visiting the Commander. Her wife had yet to hear the truth from her own mouth.{/n}',
          requires=("irabeth.partner_stance.confession_sent",)),
        p('{n}The affair ended with the lie still untold. Irabeth would not put forgiveness into her dead wife\'s mouth, or return to the Commander\'s bed.{/n}',
          requires=("irabeth.partner_stance.unconfessed",)),
        p('{n}Irabeth had refused the request for secret visits. After her wife had heard she was dead, she would not send her another lie for the Commander\'s sake. The courtship ended there.{/n}',
          requires=("irabeth.partner_stance.secret_refused",)),
        p("{n}No arrangement with the Commander had been settled. Irabeth's wedding ring "
          "remained hers; her wife had made no new promise.{/n}", forbids=(SHARE, EXCLUSIVE, SECRET)),
    ]


def cover_endings(scenes):
    for book in scenes:
        if book.get("Relationship") != "irabeth" or not book["Owner"].endswith("Epilogue"):
            continue
        if ".epilogue.native_" in book["Id"] or ".native." in book["Id"]:
            continue
        # Aeon's canon rewrite keeps its native dead/unmarried account.
        # Stance describes only the erased courtship, never a new marriage.
        if book["Owner"] == "AeonEpilogue":
            for page in book["Nodes"]:
                page["Text"] = page["Text"].replace("The spy she might have married", "Anevia")
                paragraphs = page.setdefault("Paragraphs", [])
                if not any(SHARE in p.get("Requires", []) for p in paragraphs):
                    paragraphs.extend((
                        p('{n}Before the rewriting, the Commander had accepted Irabeth and Anevia\'s marriage. That agreement vanished with the evenings in Drezen.{/n}', requires=(SHARE,)),
                        p('{n}Before the rewriting, Irabeth had refused to leave her wife for the Commander. In the new history she never met either of them.{/n}', requires=(EXCLUSIVE,)),
                        p('{n}The affair, and the lie told to Irabeth\'s wife, belonged to the history that had been erased. Anevia died without ever meeting the paladin.{/n}', requires=(SECRET,)),
                        p("{n}Before the rewriting, no arrangement with the Commander had been settled. "
                          "Nothing of that courtship passed into the new history.{/n}", forbids=(SHARE, EXCLUSIVE, SECRET)),
                    ))
            continue
        for page in book["Nodes"]:
            paragraphs = page.setdefault("Paragraphs", [])
            if not any(SHARE in x.get("Requires", []) for x in paragraphs):
                if book["Id"] == "irabeth.ending_lasting" and page["Id"] in {"living", "returned"}:
                    paragraphs.append(p(page["Text"], forbids=(SECRET,)))
                    page["Text"] = '{n}Irabeth kept her wedding ring. What the Commander had promised did not undo her marriage.{/n}'
                paragraphs.extend(ending_paragraphs())
    # Round-2 receipts follow the existing employment and wife-state inventory;
    # their addition must not move a published conditional paragraph address.
    from storylines import irabeth_round2
    irabeth_round2.ending_additions(scenes)


def cover_native(payload):
    """E14d permits only plain single-node native replacements, not paragraphs.

    Append guarded variants of Irabeth's existing replacements. Their original
    native selector, earned return and finale conditions remain conjuncts.
    """
    from storylines.earned_presence import COMMANDER_ABSENT
    sources = {s["Id"]: s for s in payload["Scenes"] if s.get("Relationship") == "irabeth"
               and (".epilogue.native_" in s["Id"] or ".native." in s["Id"])
               and ".partner." not in s["Id"]
               and s["Id"] != "anevia.trickster.native.bread_returned"}
    wife_states = (
        ("together", (), ("anevia_dead", "anevia_gone", RETURNED),
         '{n}Anevia was alive, and their marriage remained. "Beth comes home when she says she will," she had told the Commander. "That part stays."{/n}'),
        ("returned", (RETURNED,), ("anevia_dead",),
         '{n}Anevia had returned on her own terms. She still chose how far to come into Drezen, and expected her wife to meet her on her side of the gate.{/n}'),
        ("away", ("anevia_gone",), ("anevia_dead", RETURNED),
         '{n}Anevia had gone south and remained away. News of Irabeth went south with the couriers. Her absence did not dissolve their marriage or promise forgiveness.{/n}'),
        ("dead", ("anevia_dead",), (),
         '{n}Anevia was dead. The wedding ring Irabeth had worn remained a reminder of their marriage, not a vacant place for the Commander.{/n}'),
    )
    stance_states = [
        ("share", (SHARE,), (SECRET, EXCLUSIVE),
         '{n}The Commander had accepted the marriage as part of loving Irabeth. Her wife had set the terms herself: promised evenings stayed theirs.{/n}'),
        ("exclusive", (EXCLUSIVE,), (),
         '{n}Irabeth had refused the demand to leave her wife. She kept her marriage and ended the courtship.{/n}'),
        ("secret", (SECRET,), (EXPOSED,),
         '{n}Irabeth had told her wife the courtship was over, then kept seeing the Commander behind her back. It was an affair, never an agreed arrangement.{/n}'),
        ("discovered", (SECRET, EXPOSED), (),
         "{n}Her wife had uncovered the affair. Their marriage survived a bitter quarrel; the Commander lost the invitation to Irabeth's bed.{/n}"),
    ]
    for edit in payload.get("NativeEpilogueEdits", {}).values():
        for variant in [edit, *list(edit.get("Variants", []))]:
            identity = variant.get("Replacement")
            if identity not in sources or any(v.get("Replacement", "").startswith(identity + ".partner.")
                                              for v in edit.get("Variants", [])):
                continue
            source = sources[identity]
            page = source["Nodes"][0]
            page.pop("Paragraphs", None)
            # These three native leads describe a specific absent-wife history.
            # Its state now lives in the selected variant, not in an ungated lead.
            lead = page["Text"]
            if identity.endswith("native_tirabade_south"):
                lead = '{n}Irabeth came back from Iz. Her name returned to the roster, but the Coronation had left its mark on the Tirabades.{/n}'
            elif identity.endswith("native_tirabade_survived_away"):
                lead = '{n}Irabeth survived Iz but never reconciled with the Commander.{/n}'
            elif identity.endswith("native_tirabade_survived_bereavement"):
                lead = '{n}Irabeth survived Iz. The Commander later died closing the Worldwound, with no reconciliation between them.{/n}'
            for wife, wife_requires, wife_forbids, wife_text in wife_states:
                # Old saves have no stance. Keep the published original for
                # its native wife state; append the other current-state readers.
                original_wife = "together" if ".native.eng7_f6c." in identity else "away"
                branches = stance_states + ([("unset", (), (SHARE, EXCLUSIVE, SECRET), '')]
                                            if wife != original_wife else [])
                for name, requires, forbids, text in branches:
                    live_forbids = ("swarm", "true_lich") if wife in {"together", "returned"} else ()
                    guards = [*wife_requires, *requires,
                              *("!" + f for f in live_forbids),
                              *("!" + f for f in (*wife_forbids, *forbids))]
                    groups = []
                    for old in variant["When"]:
                        group = list(dict.fromkeys([*old, *guards]))
                        context = [*group, *source["Requires"], *("!" + f for f in source["Forbids"])]
                        positive = {f for f in context if not f.startswith("!")}
                        negative = {f[1:] for f in context if f.startswith("!")}
                        if not positive & negative:
                            groups.append(group)
                    if not groups:
                        continue
                    clone = copy.deepcopy(source)
                    clone["Id"] = identity + ".partner." + wife + "." + name
                    # One native narration block. The shared ending assembler
                    # splits separate guest blocks into conditional paragraphs,
                    # which E14d cannot deliver. The whole variant is state-gated.
                    parts = [lead, wife_text, text] if text else [lead, wife_text]
                    clone["Nodes"][0]["Text"] = '{n}' + '\n'.join(
                        part.replace('{n}', '').replace('{/n}', '') for part in parts) + '{/n}'
                    clone["Requires"].extend((*wife_requires, *requires))
                    clone["Forbids"].extend((*wife_forbids, *forbids, *live_forbids))
                    payload["Scenes"].append(clone)
                    edit.setdefault("Variants", []).append({"Replacement": clone["Id"],
                        "When": groups,
                        "KeepNativeImage": variant.get("KeepNativeImage", False)})
                    if identity in COMMANDER_ABSENT:
                        # These native careers already continue after the
                        # Commander's unreturned sacrifice. An explicit mourning
                        # twin preserves that eligibility without claiming a
                        # living Commander or extending the shared allowlist.
                        mourning = copy.deepcopy(clone)
                        mourning["Id"] += ".mourning"
                        mourning["Requires"].append("sacrifice")
                        mourning["Forbids"].extend(("trickster.commander_back", "lastcall.active"))
                        payload["Scenes"].append(mourning)
                        edit["Variants"].append({"Replacement": mourning["Id"],
                            "When": [list(dict.fromkeys([*group, "sacrifice", "!trickster.commander_back", "!lastcall.active"]))
                                     for group in groups],
                            "KeepNativeImage": variant.get("KeepNativeImage", False)})
            # Saved selector positions survive. New stance histories pass them
            # to the appended variants; no-stance native histories stay native.
            source["Forbids"].extend((SHARE, SECRET, EXCLUSIVE, "anevia_dead", RETURNED))
            if ".native.eng7_f6c." in identity:
                source["Forbids"].append("anevia_gone")
                page["Text"] = '{n}' + page["Text"].replace('{n}', '').replace('{/n}', '') + (
                    '\nAnevia lived. They remained wives; Beth still owed her the evenings she had promised.{/n}')
            else:
                # The published south-road lead belongs only to an absent wife.
                # The appended unset/together reader carries other old histories.
                source["Requires"].append("anevia_gone")
            # Both native selector paths must see the same retirement guards.
            # Mutate only after cloning, so new readers inherit the published
            # eligibility and their own disjoint current-state conditions.
            base_guards = [*("!" + f for f in (SHARE, SECRET, EXCLUSIVE, "anevia_dead", RETURNED)),
                           "!anevia_gone" if ".native.eng7_f6c." in identity else "anevia_gone"]
            variant["When"] = [list(dict.fromkeys([*group, *base_guards])) for group in variant["When"]]


def commitments(scenes):
    """Keep every saved answer and destination; append demands at its page."""
    for book in scenes:
        if book.get("Relationship") != "irabeth" or book["Owner"].endswith("Epilogue"):
            continue
        if any(page["Id"].startswith("partner_") for page in book["Nodes"]):
            continue
        additions = []
        for page in list(book["Nodes"]):
            # These answers were appended by the existing outcome assembler.
            # Reserve their published indices before appending stance choices.
            if (book["Id"], page["Id"]) in {
                    ("irabeth.trickster.commit", "answer"), ("irabeth.trickster.commit", "decides"),
                    ("irabeth.trickster.second_ask", "yes"), ("irabeth.trickster.nevi_reply", "yes")}:
                # Retire this reserved save slot; the assembler appends its
                # active equivalent after the new answers.
                page["Choices"].append(c('[Leave.]', requires=("trickster.now",),
                                         forbids=("trickster.now",), abort=True))
            for index, answer in enumerate(list(page["Choices"])):
                if "irabeth.committed" not in answer["Set"] or SHARE in answer["Set"]:
                    continue
                # Retired answers remain byte-position compatible and inert.
                if set(answer["Forbids"]) & set(book["Requires"]):
                    continue
                if book["Id"].startswith("irabeth.trickster.") and set(answer["Forbids"]) & {
                        "anevia.trickster.shares_beth", "irabeth.trickster.pen_sent"}:
                    continue
                original = copy.deepcopy(answer)
                answer["Set"].append(SHARE)
                answer["Forbids"].append("anevia_dead")
                widow = copy.deepcopy(original)
                widow["Requires"].append("anevia_dead")
                page["Choices"].append(widow)
                stem = "partner_" + page["Id"] + "_" + str(index)
                for demand, text in (("exclusive", '"Leave Anevia. I want you for myself."'),
                                     ("secret", '"Tell Anevia it is over. Keep coming to me in secret."')):
                    move = c(text, stem + "_" + demand,
                             requires=original["Requires"],
                             forbids=(*original["Forbids"], "anevia_dead"))
                    page["Choices"].append(move)
                back = copy.deepcopy(answer)
                back["Text"] = '"Then we keep the arrangement Anevia agreed to."'
                # This choice is reached through the original earned guards.
                back["Requires"] = []
                back["Forbids"] = []
                stop = c('[Accept her refusal. End the courtship.]',
                         flags=(EXCLUSIVE, "irabeth.closed"))
                additions.append(n(stem + "_exclusive", "Irabeth",
                    '''{n}Irabeth pulls her hand out of yours.{/n}
"No. Anevia is my wife. I love her. You knew that before you asked me for anything."
{n}Her jaw sets.{/n}
"I swore to Anevia. I won't break that oath for you. Take what I offered, or leave it. You don't give orders in my marriage."''',
                    back, stop, portrait="Irabeth"))
                if book["Id"] == "irabeth.a_road_she_would_choose":
                    additions.extend(secret_nodes(stem, original))
                else:
                    additions.append(n(stem + "_secret", "Irabeth",
                        '''"No. Nevi has already had to hear that I was dead. I'm not sending her another lie so you can have me in your bed."
{n}She steps back.{/n} "Ask for what she and I offered. Or stop asking."''',
                        copy.deepcopy(back),
                        c('[End the courtship.]', flags=("irabeth.closed", "irabeth.partner_stance.secret_refused")),
                        portrait="Irabeth"))
        book["Nodes"].extend(additions)


def secret_nodes(stem, original):
    accept = copy.deepcopy(original)
    accept.update(Text='[Keep the promise behind Anevia\'s back.]', Next=stem + "_end")
    accept["Set"].extend((SECRET,))
    accept["Requires"] = []
    accept["Forbids"] = []
    return [
        n(stem + "_secret", "Irabeth", '''{n}Irabeth looks down at her ring. Her breath comes hard.{/n}
"She agreed to an honest arrangement. Not this."
{n}Her hand closes on yours anyway.{/n}
"I'd have to tell her we've stopped. Then go home after seeing you and let her believe me. I know exactly what you're asking. Damn you, I still want to stay."''',
          c('"Tell her. Then come back to me."', stem + "_lie", forbids=("anevia_dead", "anevia_gone")),
          c('"No. Keep it honest."', original["Next"], flags=(*original["Set"], SHARE)),
          c('[Leave before she lies to her wife.]', flags=("irabeth.closed",)), portrait="Irabeth"),
        n(stem + "_lie", "Narrator", '''{n}Irabeth goes home. That evening she brings you Anevia's answer, word for word.{/n}
{n}"Over? You sure that's what you want, Beth?"{/n}
{n}Irabeth said yes.{/n}
{n}"Then come home tonight. I've had enough empty chairs while you two make up your minds."{/n}
{n}Irabeth stands beside your door, one hand covering her ring.{/n}
{n}"She believed me. Don't tell me that makes it easier."{/n}''',
          c('[Draw her inside.]', stem + "_night"),
          c('"Go home. Tell her what you almost did."', flags=("irabeth.closed",)), portrait="Irabeth"),
        n(stem + "_night", "Irabeth", '''{n}She shuts the door and catches your mouth with hers. Her tusk grazes your lip; she presses closer instead of apologizing. Your hands find the warm skin beneath her collar. She unbuckles her sword belt and lays it on the table, then pulls you toward the bed by your coat.{/n}
"I ought to go home."
{n}She stays. Her fingers work at your belt.{/n}''',
          c('Continue', stem + "_morning"), portrait="Irabeth"),
        n(stem + "_morning", "Irabeth", '''{n}Before the dawn muster she fastens her belt with shaking fingers.{/n}
"I'll tell her the watch ran late. She'll ask which watch. I'll have to give her a name."
{n}She looks at you without smiling.{/n}
"I wanted you. I chose it. Don't dress it up for me."''', accept, portrait="Irabeth"),
        n(stem + "_end", "Narrator", '''{n}Later that morning Irabeth returns Sella's exercise herself. The drawing of the lake stays in her notebook. At the muster she gives her report without looking at you; when the officers disperse, she looks once.{/n}''',
          c('[Keep the journey, and the lie, between you.]', flags=("irabeth.future_chosen",)), portrait="Irabeth"),
    ]


def discovery(book):
    start = book["Nodes"][0]
    for answer in start["Choices"]:
        answer["Forbids"].append(SECRET)
    start["Choices"].extend((
        c('[Face Anevia.]', "partner_discovery", requires=(SECRET,),
          forbids=("anevia_dead", "anevia_gone", "swarm", "true_lich")),
        c('[Face Anevia at the gate.]', "partner_discovery_returned", requires=(SECRET, RETURNED),
          forbids=("anevia_dead", "swarm", "true_lich")),
        c('[Hear what remains unsaid.]', "partner_absent", requires=(SECRET, "anevia_gone"),
          forbids=("anevia_dead", RETURNED)),
        c('[Remember what she never learned.]', "partner_dead", requires=(SECRET, "anevia_dead")),
    ))
    book["Nodes"].extend((
        n("partner_discovery", "Anevia", '''{n}Anevia is waiting beside the window. She has brought the watch roster.{/n}
"That watch you kept Beth on? Wrong names. Wrong bell. I've caught cultists with better stories."
{n}Irabeth goes pale. Anevia looks at her.{/n}
"You told me it was over. Came home and kissed me after tellin' me that. How long were you going to keep doing it?"
"Nevi—" {n}Irabeth begins.{/n}
"Don't. I said you could love somebody else. I didn't say you could make a fool of me in my own house."''',
          c('"We both lied to you."', "partner_fallout"),
          c('"This is between you and your wife."', "partner_fallout"), portrait="Anevia"),
        n("partner_fallout", "Irabeth", '''"I chose it. I'm not blaming the Commander."
{n}Irabeth takes off a gauntlet. Her ring is bare between them.{/n}
"I want to come home. I want to try to mend what I did."
"Then come," {n}Anevia says.{/n} "And don't expect me to stop being angry at breakfast."
{n}Irabeth turns to you.{/n}
"We're finished. I'll do my duty against the demons. You won't touch me again."
{n}Anevia opens the door for her wife. She waits for you to move away from it.{/n}''',
          c('[Let them leave together.]', flags=(SECRET, EXPOSED, "irabeth.closed")), portrait="Irabeth"),
        n("partner_absent", "Irabeth", '''{n}Anevia had gone south and remained away. Irabeth has a letter folded beneath the drawing.{/n}
"I lied to my wife. She hasn't even had a chance to answer."
"I wrote what we did. I don't know whether it'll reach her. I don't get to decide her answer, either. Until I hear it, there's no more of this."''',
          c('[Accept the end of the affair.]', flags=("irabeth.closed", "irabeth.partner_stance.confession_sent")), portrait="Irabeth"),
        n("partner_dead", "Irabeth", '''"She died believing I'd told her the truth."
{n}Irabeth covers her ring with her other hand.{/n}
"Don't tell me she'd forgive it. You didn't ask her. Neither did I. I can't go on sharing your bed with that between us."''',
          c('[Accept the end of the affair.]', flags=("irabeth.closed", "irabeth.partner_stance.unconfessed")), portrait="Irabeth"),
    ))
    # Keep the living-in-Drezen and earned-return paths separate. The shared
    # presence proof conservatively intersects incoming conditions; merging
    # these paths would discard both valid wife-state guards.
    for original, identity in (("partner_discovery", "partner_discovery_returned"),
                               ("partner_fallout", "partner_fallout_returned")):
        page = copy.deepcopy(next(n for n in book["Nodes"] if n["Id"] == original))
        page["Id"] = identity
        if original == "partner_discovery":
            page["Text"] = page["Text"].replace("Anevia is waiting beside the window. She has brought the watch roster.",
                "You follow Irabeth out to the gate. Anevia waits on the road side of it, holding the watch roster.")
            for answer in page["Choices"]:
                answer["Next"] = "partner_fallout_returned"
        else:
            page["Text"] = page["Text"].replace("Anevia opens the door for her wife. She waits for you to move away from it.",
                "Anevia takes her wife's hand and turns toward the road. She waits for you to step aside.")
        book["Nodes"].append(page)


def integrate(payload):
    commitments(payload["Scenes"])
    for book in payload["Scenes"]:
        if book["Id"] in {"irabeth.the_hour_before_battle", "irabeth.trickster.back_on_duty"}:
            if not any(n["Id"] == "partner_discovery" for n in book["Nodes"]):
                discovery(book)
    if any(s["Id"] == "irabeth.partner_ending" for s in payload["Scenes"]):
        return
    payload["Scenes"].append(scene("irabeth.partner_ending", "The door she closed", "Epilogue", 0, "", [
        n("end", "Narrator", '{n}Irabeth had ended the courtship. She had kept her wedding ring.{/n}',
          paragraphs=ending_paragraphs(), portrait="Irabeth")],
        requires=("irabeth.closed",), RequiresAny=[EXCLUSIVE, EXPOSED,
            "irabeth.partner_stance.confession_sent", "irabeth.partner_stance.unconfessed",
            "irabeth.partner_stance.secret_refused"],
        last=99, Relationship="irabeth"))

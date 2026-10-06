"""Authored Anevia/Irabeth commitment amendments (CANON-PARTNERS-DESIGN, revision).

No native marriage is dissolved. Canon anchors: HorgusAnevia/Cue_0024
377de2648a0f24d42864709080f850b9; Irabeth/Cue_0048
069eeb42997738d40a0db4667eafe44d. IrabethDead b14e13f9 and
IrabethGone 395aad04 remain read-only. Paid survival is distinct from
reconciliation: dug_out/raised_on_record do not grant returned.
The secret is a renewed breach of the previously negotiated nights, exposed
at the existing farewell (ordinary route) or dawn (gate route).
"""
import copy

from story_format import c, n, p

SHARE = "anevia.partner_stance.share"
EXCLUSIVE = "anevia.partner_stance.exclusive"
SECRET = "anevia.partner_stance.secret"
EXPOSED = "anevia.partner_lie_exposed"
CAREFUL = "anevia.partner.absence_kept"
RETURN = "irabeth.trickster.returned"
DUG = "irabeth.trickster.cost.dug_out"
RAISED = "irabeth.trickster.raised_on_record"
SURVIVAL = (RETURN, DUG, RAISED)


def live_answers(text, target, *, flags=(), requires=(), forbids=()):
    """Disjoint living histories; no dependency on Irabeth's romance choice."""
    answers = []
    for req, no in (
        ((RETURN,), ()), ((DUG,), (RETURN,)), ((RAISED,), (RETURN, DUG)),
        ((), ("irabeth_dead", *SURVIVAL))):
        needed = tuple(dict.fromkeys((*requires, *req)))
        blocked = tuple(dict.fromkeys((*forbids, *no)))
        if not set(needed) & set(blocked):
            answers.append(c(text, target, flags=flags, requires=needed, forbids=blocked))
    return answers


REFUSAL = '''"Leave my wife? No. The house is ours, and you don't get to buy her out of it with a key."
{n}Anevia puts a hand between you and her belt.{/n}
"I want you. Been makin' that embarrassingly clear. I remember Beth beside me before there was a bloody Commander to impress. She stays. You decide whether you do."
{n}The watch bell sounds beyond the window. She leaves her hand where it is.{/n}'''

SECRET_OFFER = '''"We told her we'd keep our nights straight. Now you want me tellin' her I'm workin' while I'm in your bed."
{n}Anevia's thumb catches in your belt. She looks at it, then at you.{/n}
"I ought to go home. She'll have supper waitin'."
{n}She draws you closer instead.{/n}
"Damn you. And damn me for wantin' this. Don't dress it up when she asks. We both know what we're doin'."'''

SECRET_NIGHT = '''{n}Anevia bolts the door. Her fingers shake once against the iron; she swears and turns back to you. She catches your collar, kisses you hard, and pulls until you stumble against the bed.{/n}
"No reports. No bloody speeches. Get this off."
{n}Your coat drops beside her boots. She loosens her laces with a thief's speed, leaves the dress over the chair, and pushes you onto the mattress. Her mouth finds your neck as she draws your hands to her bare waist.{/n}'''

DISCOVERY = '''{n}A note lies open on the table. Irabeth's handwriting has scored the paper.{/n}
"Commander. Nevi told me she was sorting dispatches. The dispatches were on my desk. I kept her supper warm until the watch changed."
{n}The next line is darker.{/n}
"Do not come to our house. My wife and I have things to settle. You will get your patrol reports, and that is all you will get from me. I gave you my word. You gave me an excuse."'''

FALLOUT = '''"She asked me how long. I tried tellin' her how it started. She asked again."
{n}Anevia folds her wife's note, keeping the torn edge inside.{/n}
"Told her. All of it. Then she asked if I was comin' home. Not if I'd behave. If I was comin' home."
{n}She puts on her coat, missing a fastening and leaving it.{/n}
"I am. We'll have some filthy rows. She's still my wife. You and me are finished. Don't send flowers, don't send orders, and don't come round lookin' wounded. I won't be there to patch you up."'''


def refusal_nodes(prefix, back):
    return [n(prefix + "exclusive", "Anevia", REFUSAL + '\n"Back down, and you keep the nights I offered. You get no key to our bedroom. Don\'t come knockin\' on a night I kept for my wife."',
              c('"Then I withdraw the demand. Keep your marriage."', back),
              c('"Then we end it here."', flags=(EXCLUSIVE, "anevia.closed", "anevia.parted")),
              portrait="Anevia")]


def discovery_nodes(prefix):
    return [n(prefix + "discovered", "Narrator", DISCOVERY,
              c("Continue", prefix + "over", forbids=("irabeth.present_now",)),
              c('[Face Irabeth with Anevia.]', prefix + "two_reports", requires=("irabeth.present_now",)), portrait="Irabeth"),
            n(prefix + "over", "Anevia", FALLOUT,
              c('[Let her go home.]', flags=(EXPOSED, "anevia.closed", "anevia.parted")), portrait="Anevia"),
            n(prefix + "two_reports", "Irabeth", '''{n}Irabeth puts two sheets on the table. The patrol dispatch bears the watch captain's receipt. Beside it lies Anevia's account of an evening spent sorting those same dispatches.{/n}
"They were delivered before supper. You were very precise about when you finished, Nevi. Too precise."
{n}Anevia reaches for the second sheet. Irabeth keeps her hand on it.{/n}
"I will not change a watch list to cover this. I will not make a spectacle of our marriage in court, either. Which of you decided I would be easiest to manage?"''',
              c('"I knew she was lying to you. I stayed anyway."', prefix + "how_long"),
              c('[Lie] "We needed privacy for crusade business."', prefix + "no_alibi"), portrait="Irabeth"),
            n(prefix + "no_alibi", "Irabeth", '''"Then name the business. Put it in the report. Sign it."
{n}Anevia pushes the private sheet back toward her wife.{/n}
"Beth. There wasn't any. I wanted to stay with the Commander. Don't let us turn it into work."
{n}Irabeth looks at you once, then turns to her wife.{/n}''',
              c('[Let Anevia answer for herself.]', prefix + "how_long"), portrait="Irabeth"),
            n(prefix + "how_long", "Irabeth", '''"How long?"
"The reports were done. I stayed. I kept thinkin' I could get home before you started wonderin'—" {n}Anevia stops when her wife lifts a hand.{/n}
"How long, Nevi?" {n}Irabeth asks.{/n}
{n}Anevia gives her the evenings, one by one. Irabeth listens without looking at the Commander.{/n}
"Wanted it," {n}Anevia says.{/n} "Still do. That ain't an excuse."
{n}Irabeth folds the private account and leaves the patrol report on the table.{/n}
"The patrols go out as ordered. Commander, you will receive their reports. Stay away from our house."
{n}She looks at Anevia.{/n}
"Are you coming home?"
"Yeah. With you."''',
              c('[Let them leave together.]', prefix + "over"), portrait="Irabeth")]


def ordinary_commit(book):
    nodes = {page["Id"]: page for page in book["Nodes"]}
    for page in book["Nodes"]:
        for answer in page["Choices"]:
            if "anevia.committed" in answer.get("Set", ()):
                answer["Set"].append(SHARE)
    # The existing yes is sharing the arrangement Irabeth already negotiated.
    nodes["start"]["Choices"].extend([
        c('"For keeps means only us. Leave your wife."', "partner_exclusive"),
        c('[Lie] "Tell your wife you are sorting dispatches. Stay with me instead."', "partner_secret_offer")])
    book["Nodes"].extend(refusal_nodes("partner_", "yes"))
    book["Nodes"].extend([
        n("partner_secret_offer", "Anevia", SECRET_OFFER,
          c('[Pull her close.] "Stay."', "partner_secret_night"),
          c('"Go home tonight. We keep the terms we agreed."', "yes"), portrait="Anevia"),
        n("partner_secret_night", "Anevia", SECRET_NIGHT,
          c("Continue", "partner_secret_morning"), portrait="Anevia"),
        n("partner_secret_morning", "Anevia", '''{n}Anevia dresses in the grey before the muster bell. She looks at the key, then leaves it beside your cup.{/n}
"Told her I was workin'. She packed me supper. It's in my bag."
{n}Her mouth twists. She takes your hand anyway.{/n}
"I want another night. That's the nasty bit. Don't ask me to be proud of it."''',
          c('[Keep the key and the affair.]', flags=("anevia.committed", "anevia.future_chosen", SECRET)), portrait="Anevia")])
    nodes["start"]["Choices"].append(c('[Keep the affair to Irabeth\'s absence with the Queen. No false dispatches, no missed supper.]',
        "partner_absent_night", requires=("irabeth_away",), forbids=("irabeth_gone", "irabeth_dead", *SURVIVAL)))
    book["Nodes"].append(n("partner_absent_night", "Anevia", '''"Beth's with the Queen. I still owe her a straight letter. You know I ain't writin' one tonight."
{n}Anevia leaves the scout reports on your desk and bolts the door. She opens your coat with both hands and pushes it from your shoulders.{/n}
"No messengers. No little gifts for her to find when she comes home. I want you, and I'm already lyin' enough."
{n}Her mouth catches yours. She pulls you toward the bed, her wedding ring cold against your bare chest.{/n}''',
        c('[Keep the nights quiet while Irabeth is away.]', flags=("anevia.committed", "anevia.future_chosen", SECRET, CAREFUL)), portrait="Anevia"))


def gate_commit(book):
    """Keep old committing answers for widows; append living-wife alternatives."""
    additions = []
    for page in book["Nodes"]:
        originals = [ch for ch in page["Choices"] if "anevia.committed" in ch.get("Set", ())]
        if originals:
            # earned_outcomes appends this existing lost-path exit later.
            # Reserve its shipped index before adding stance answers; the
            # later duplicate has the same guard and grants nothing.
            page["Choices"].append(c("[Leave.]", forbids=("trickster.now",), abort=True))
        for index, answer in enumerate(originals):
            # Permanently retired answers (the old pre-muster promises) stay retired.
            if "anevia.irabeth_killed_by_commander" in book.get("Requires", ()):
                continue
            prefix = "partner_%s_%s_" % (page["Id"], index)
            old = copy.deepcopy(answer)
            answer["Requires"] = list(dict.fromkeys([*answer.get("Requires", []), "irabeth_dead"]))
            answer["Forbids"] = list(dict.fromkeys([*answer.get("Forbids", []), *SURVIVAL]))
            original_flags = tuple(old["Set"])
            other_flags = tuple(f for f in original_flags if f != "anevia.committed")
            # Share reads a letter, so neither wife is silently placed at the gate.
            page["Choices"].extend(live_answers(old["Text"], prefix + "share",
                flags=other_flags, requires=old["Requires"], forbids=old["Forbids"]))
            additions.extend([
                n(prefix + "share", "Anevia", '''"I told Beth what I'm askin'. She sent you this. Read it before you start unbucklin' things."
{n}Anevia holds the lantern close enough to read Irabeth's handwriting.{/n}
"Commander. I want my wife home on the nights we chose. No summons dragging her away from supper unless the Wound itself is opening under the table. She may invite you elsewhere. Our bedroom stays ours."
{n}Below the signature is another line.{/n}
"You have heard me give orders. This is a promise I expect you to keep."
{n}Anevia watches you finish.{/n}
"Told her yes. Your turn."''',
                  c('"Your house stays yours. I will keep those nights."', old.get("Next"),
                    flags=(*original_flags, SHARE)), portrait="Anevia")])
            # Kiss/hand openings retain their separate share actions. Demand
            # and affair use the broader hand-taking terms once per page.
            if index != len(originals) - 1:
                continue
            page["Choices"].extend(live_answers('"Only us. Leave your wife."', prefix + "exclusive",
                requires=old["Requires"], forbids=old["Forbids"]))
            page["Choices"].extend(live_answers('[Lie] "Tell your wife you are sorting dispatches. Stay with me instead."',
                prefix + "secret_offer", requires=old["Requires"], forbids=old["Forbids"]))
            additions.extend(refusal_nodes(prefix, prefix + "share"))
            # Backing down still pays the original key/terms cost.
            additions[-1]["Choices"][0]["Set"] = list(other_flags)
            additions.extend([
                n(prefix + "secret_offer", "Anevia", SECRET_OFFER,
                  c('[Stay together behind the bolted door.]', prefix + "secret_night",
                    flags=(*original_flags, SECRET)),
                  c('"Go home tonight. We tell her the truth."', prefix + "share", flags=other_flags), portrait="Anevia"),
                n(prefix + "secret_night", "Anevia", SECRET_NIGHT,
                  c("Continue", prefix + "discovered"), portrait="Anevia")])
            if "anevia.trickster.cost.her_key" in original_flags:
                additions[-2]["Text"] = ("{n}You lean in and tell her the secret she demanded. She listens without a smile, "
                    "then closes her empty hand as if she were pocketing something valuable.{/n}\n" + additions[-2]["Text"])
            additions.extend(discovery_nodes(prefix))
            discovered = next(page for page in additions if page["Id"] == prefix + "discovered")
            discovered["Text"] = "{n}At dawn Anevia comes back from the road with a folded note. She lays it between you and stands away from the bed.{/n}\n" + DISCOVERY
            # Reserve the second legacy lost-power exit emitted by earned_outcomes.
            page["Choices"].append(c("[Leave.]", forbids=("trickster.now",), abort=True))
            quiet = live_answers('[Keep the affair to Irabeth\'s absence with the Queen. Leave no false dispatches.]',
                prefix + "absent_night", requires=(*old["Requires"], "irabeth_away"), forbids=(*old["Forbids"], "irabeth_gone", "irabeth_dead", *SURVIVAL))
            if not quiet or set(book.get("Requires", ())) & set(quiet[0]["Forbids"]):
                continue
            page["Choices"].extend(quiet)
            additions.append(n(prefix + "absent_night", "Anevia", '''"Beth's away with the Queen. I'm still makin' a liar of myself. Don't send a damned invitation to the house."
{n}Anevia catches your belt and draws you through the doorway. Her mouth opens against yours; she unlaces her dress without letting you go.{/n}
"These nights. While she's away. When she comes back, I go home."
{n}She presses you against the bed, the ring on her hand bright in the lantern light.{/n}''',
                c('[Keep her company quietly while Irabeth is away.]', flags=(*original_flags, SECRET, CAREFUL)), portrait="Anevia"))
            if "anevia.trickster.cost.her_key" in original_flags:
                additions[-1]["Text"] = ("{n}You tell her the secret she demanded. She listens without a smile, "
                    "then closes her empty hand as if she were pocketing something valuable.{/n}\n" + additions[-1]["Text"])
    book["Nodes"].extend(additions)


def farewell_discovery(book):
    start = book["Nodes"][0]
    quiet = []
    for answer in start["Choices"]:
        if not answer.get("Abort"):
            private = copy.deepcopy(answer)
            private["Requires"].extend((SECRET, CAREFUL))
            quiet.append(private)
            answer.setdefault("Forbids", []).append(SECRET)
    start["Choices"].append(c('[Read the note Anevia lays beside the little goat.]', "partner_discovered", requires=(SECRET,), forbids=(CAREFUL,)))
    start["Choices"].extend(quiet)
    start["Choices"].extend(live_answers('[Ask her to stay another night after Beth comes home. Let supper wait.]',
        "partner_discovered", requires=(SECRET, CAREFUL, "irabeth.presence.route_open"), forbids=("irabeth_away",)))
    book["Nodes"].extend(discovery_nodes("partner_"))


def partner_states():
    """A later departure beats historical survival; survival beats native death."""
    gone = "{n}Irabeth is gone from Drezen. Anevia still called her wife, and kept Beth's old letters. No new invitation came from that house.{/n}"
    away = "{n}Irabeth's absence from Drezen left Anevia with letters to answer. They were still married; the Commander had never been promised all her nights.{/n}"
    state = [
        p("{n}Irabeth had returned from Iz. Anevia kept her wedding ring. Beth's old letters lay folded beside the scout reports, with the private lines turned inward.{/n}", requires=(RETURN,), forbids=("irabeth_gone", "irabeth_away")),
        p("{n}Irabeth survived Iz. She had not reconciled with the Commander. Anevia still signed her letters as her wife; no invitation to the Commander went with them.{/n}", requires=(DUG,), forbids=(RETURN, "irabeth_gone", "irabeth_away")),
        p("{n}Irabeth came back from Iz after the chaplain raised her, but had not reconciled with the Commander. Anevia remained her wife. Beth's old letters went into Anevia's coat, where the Commander could not read them.{/n}", requires=(RAISED,), forbids=(RETURN, DUG, "irabeth_gone", "irabeth_away")),
        p("{n}Irabeth was dead. Anevia's marriage ended at that grave, not at any demand the Commander had made. Beth's name stayed with her.{/n}", requires=("irabeth_dead",), forbids=SURVIVAL),
        p(gone, requires=("irabeth_gone",), forbids=("irabeth_dead", *SURVIVAL)),
        p(away, requires=("irabeth_away",), forbids=("irabeth_dead", "irabeth_gone", *SURVIVAL)),
        p("{n}Irabeth remained Anevia's wife, alive in Drezen. Anevia kept her spare boots beside her wife's at the door; on patrol nights the house was locked.{/n}", forbids=("irabeth_dead", "irabeth_gone", "irabeth_away", *SURVIVAL))]
    for flag, previous in ((RETURN, ()), (DUG, (RETURN,)), (RAISED, (RETURN, DUG))):
        state.append(p(gone, requires=("irabeth_gone", flag), forbids=previous))
        state.append(p(away, requires=("irabeth_away", flag), forbids=("irabeth_gone", *previous)))
    return state


def ending_paragraphs(*, aeon=False):
    """Current native state first, historical stance second. No bodily reunion."""
    state = ([p("{n}Irabeth's marriage to Anevia belonged to the history that was erased. Neither woman owed the Commander its promises in the world that replaced it.{/n}")]
             if aeon else partner_states())
    return state + [
        p("{n}The Commander had accepted the nights the Tirabades kept for themselves. Irabeth had told the Commander plainly: \"Our house stays ours.\" Anevia had kept those nights, and left the Commander to find supper elsewhere.{/n}", requires=(SHARE,)),
        p("{n}The Commander had demanded an end to Anevia's marriage. Anevia had refused, and the romance had ended there.{/n}", requires=(EXCLUSIVE,), forbids=(SHARE, SECRET)),
        p("{n}Anevia had lied about the nights she spent with the Commander. She remembered Irabeth keeping supper warm while she spent the night in someone else's bed.{/n}", requires=(SECRET,), forbids=(EXPOSED, CAREFUL)),
        p("{n}Anevia remembered Irabeth asking how long the affair had lasted, and asking again when she tried to tell her how it had started. She had gone home to face her wife. Their marriage had survived the rows. The Commander's welcome had not.{/n}", requires=(SECRET, EXPOSED)),
        p("{n}The affair had begun during Irabeth's absence with the Queen. No invitation had gone to the Tirabade house; no dispatch had been falsified. Anevia had hidden those visits from her wife. She had offered the nights of that absence, and no claim on their marriage.{/n}", requires=(SECRET, CAREFUL), forbids=(EXPOSED,))]


def cover_endings(scenes, native_replacements=()):
    for book in scenes:
        if (book.get("Relationship") != "anevia" or not book.get("Owner", "").endswith("Epilogue")
                or book["Id"] in native_replacements):
            continue
        for page in book["Nodes"]:
            page.setdefault("Paragraphs", []).extend(copy.deepcopy(ending_paragraphs(aeon=book["Owner"] == "AeonEpilogue")))


def native_stance_variants(payload):
    """E14d needs plain text: append variants without changing old identities.

    Old variants remain the no-stance histories. Each new variant reads the
    same earned return/commitment plus the recorded stance and current wife
    state. No new native target, return, presence or eligibility is created.
    Later shared native corrections need the same treatment by their owner.
    """
    books = {book["Id"]: book for book in payload["Scenes"]}
    # Last Call inserts its page after the last existing route epilogue.
    # Keep that anchor last: inserting new native scenes before it preserves
    # every old scene's relative order, including Anevia's coda and reactions.
    anchor = max(i for i, book in enumerate(payload["Scenes"])
                 if book.get("Relationship") == "anevia" and book.get("Owner", "").endswith("Epilogue")
                 and book.get("EpilogueSequence") is None and book.get("Owner") != "AeonEpilogue")
    new_books = []
    states = partner_states()
    stances = ending_paragraphs()[len(states):]
    for edit in payload.get("NativeEpilogueEdits", {}).values():
        additions = []
        for variant in (edit, *edit.get("Variants", [])):
            original = books.get(variant["Replacement"])
            if not original or original.get("Relationship") != "anevia":
                continue
            old_when = copy.deepcopy(variant["When"])
            # The existing Q7-28 widow correction is applied later. Preserve
            # its proof guards on these copies as well, not just the originals.
            if original["Id"].endswith(("native_tirabade_widow", "native_tirabade_widow_committed")):
                old_when = [[*group, *("!" + flag for flag in SURVIVAL)] for group in old_when]
            for group in variant["When"]:
                group.extend(("!" + SHARE, "!" + EXCLUSIVE, "!" + SECRET))
            for state_index, state in enumerate(states):
                for stance_index, arrangement in enumerate(stances):
                    clauses = [*state["Requires"], *arrangement["Requires"],
                               *("!" + flag for flag in (*state["Forbids"], *arrangement["Forbids"]))]
                    groups = [list(dict.fromkeys([*group, *clauses])) for group in old_when]
                    groups = [group for group in groups if not any("!" + flag in group for flag in group if not flag.startswith("!"))]
                    if not groups:
                        continue
                    book = copy.deepcopy(original)
                    book["Id"] += ".partner_%s_%s" % (state_index, stance_index)
                    book["Requires"] = list(dict.fromkeys([*book["Requires"], *state["Requires"], *arrangement["Requires"]]))
                    book["Forbids"] = list(dict.fromkeys([*book["Forbids"], *state["Forbids"], *arrangement["Forbids"]]))
                    book["Nodes"][0]["Text"] = ("{n}Anevia had returned as far as the Drezen gate, on her own terms. "
                        "The Commander had learned to knock on a real door. "
                        + state["Text"].removeprefix("{n}").removesuffix("{/n}") + " "
                        + arrangement["Text"].removeprefix("{n}").removesuffix("{/n}") + "{/n}")
                    book["Nodes"][0].pop("Paragraphs", None)
                    new_books.append(book)
                    additions.append(dict(Replacement=book["Id"], When=groups, KeepNativeImage=variant.get("KeepNativeImage", False)))
        edit.setdefault("Variants", []).extend(additions)
    payload["Scenes"][anchor:anchor] = new_books


def integrate(payload):
    for book in payload["Scenes"]:
        if book["Id"] == "anevia.a_key_that_is_hers":
            ordinary_commit(book)
        elif book["Id"] == "anevia.the_last_ordinary_thing":
            farewell_discovery(book)
        elif book["Id"] in ("anevia.trickster.gone.commit", "anevia.trickster.gone.second_ask",
                            "anevia.trickster.gone.fetched_commit", "anevia.trickster.gone.fetched_second_ask"):
            gate_commit(book)
    native_replacements = {variant["Replacement"] for edit in payload.get("NativeEpilogueEdits", {}).values()
                           for variant in (edit, *edit.get("Variants", []))}
    cover_endings(payload["Scenes"], native_replacements)
    native_stance_variants(payload)
    # Route-owned contribution to the named Anevia coda; shared Last Call files
    # and every other partner's data remain untouched. This precedes pages().
    from storylines.lastcall_partners import PARTNERS
    part = next(part for part in PARTNERS if part["key"] == "anevia")
    if not any(SHARE in paragraph.get("Requires", ()) for paragraph in part["paragraphs"]):
        part["paragraphs"] = (*part["paragraphs"], *ending_paragraphs())

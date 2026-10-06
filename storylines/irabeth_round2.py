"""Authored round-2 situations at Irabeth's existing hosts.

The wife's dispatch is the registered turn. No new obedience quest or price.
Native anchors: Irabeth Cue_0047/0048 (marriage), Cue_0027 (command before
knighthood), Cue_0192 (bad equipment); Irabeth_C3_Intro Cue_0124 (judgment).
Explicit slots contain heated cuts only; their companion JSONs are fill briefs.
"""
import copy
import json
from pathlib import Path

from story_format import c, n, p

SLOTS = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/irabeth"
RETURNED = "irabeth.trickster.returned"


def cut(book, page, number, split=None):
    """Append the cut without changing an old answer's index or destination."""
    identity = book["Id"] + ".explicit." + str(number)
    brief = json.loads((SLOTS / (identity + ".json")).read_text(encoding="utf-8"))
    after = ""
    if split:
        before, after = page["Text"].split(split, 1)
        page["Text"] = before.rstrip()
        after = split + after
    # Brief: reciprocal desire at the established threshold, then the branch's
    # existing aftermath. No explicit prose, new flags, or inferred affection.
    if after:
        aftermath_id = book["Id"] + ".after_explicit." + str(number)
        # A later fill replaces only the dedicated cut; it cannot erase the
        # missed signature, muster, conversation or their existing receipts.
        if book["Id"] == "irabeth.without_an_account":
            bridge = '{n}Later, the bell for the night watch is ringing across the rooftops when she lifts her head. '
            after = after.replace(bridge, '{n}', 1)
        elif book["Id"] == "i_crossing":
            after = after.replace('{n}Later, before she leaves, she sits beside you in the darkness. ', '{n}', 1)
        elif book["Id"] == "irabeth.the_hour_before_battle":
            after = after.replace('{n}At dawn she buckles', '{n}She buckles', 1)
        aftermath = n(aftermath_id, page["Speaker"], after,
                      *copy.deepcopy(page["Choices"]), portrait="Irabeth")
        slot = n(identity, "Narrator", brief["default_text"], c("Continue", aftermath_id), portrait="Irabeth")
    else:
        aftermath = None
        slot = n(identity, "Narrator", brief["default_text"],
                 *copy.deepcopy(page["Choices"]), portrait="Irabeth")
    active = []
    for answer in page["Choices"]:
        new = copy.deepcopy(answer)
        new["Next"] = identity
        new["Text"] = '[Stay with her.]'
        # Effects stay at the existing exit after the cut, once.
        new["Set"] = []
        new["Abort"] = False
        active.append(new)
        answer["Requires"].append("trickster.now")
        answer["Forbids"].append("trickster.now")
    page["Choices"].extend(active)
    book["Nodes"].append(slot)
    if aftermath:
        book["Nodes"].append(aftermath)


def integrate(payload):
    books = {b["Id"]: b for b in payload["Scenes"]}
    if any(page["Id"] == "i_crossing.explicit.1" for page in books["i_crossing"]["Nodes"]):
        return

    def page(sid, nid):
        return next(x for x in books[sid]["Nodes"] if x["Id"] == nid)

    # IRA-01: her operational correction is part of the existing bad-iron case.
    wagon = page("irabeth.the_seized_wagon", "start")
    wagon["Text"] = wagon["Text"].replace(
        '{n}"Then begin there."{/n}',
        '{n}"Then begin there." Irabeth lays a split shield grip on the wagon. Hadran looks at it before answering.{/n}\n'
        '{n}"Your patrol was ordered to hold the road," she says. "I withdrew it. Two grips broke in the first clash. '
        'The men could hold spears or shields, not both. My correction goes in the report. Now we find out whose iron they carried."{/n}')
    # IRA-02: one mundane interruption, followed by her initiative.
    kiss = page("irabeth.the_evening_she_chose", "kiss")
    kiss["Text"] += ('\n{n}A fist knocks against the door. "Knight-Captain? The shield rack?"{/n}\n'
        '{n}"West wall. Not across the escape stair!" Irabeth shuts her eyes, then laughs against your mouth. '
        'Her hand catches your collar before you can draw away. "I am off duty. Someone should tell my voice." She kisses you again.{/n}')

    # IRA-03: the military endorsement is earned by work, not a lover's favour.
    endorsement = page("irabeth.when_the_instruction_is_used", "endorsement")
    endorsement["Text"] = '''"Your signature got them to read it. Vela's review got Pella her goods back. That is the part I can defend."
{n}Irabeth taps the corrected form.{/n}
"One officer suggested I had found an unusual way to obtain your support. I asked him which paragraph was wrong. He had no answer."
{n}Her mouth tightens.{/n}
"If he finds one tomorrow, I'll hear it. So will you. I am not putting my work beyond criticism because you kiss me."'''

    # Her own offer follows the wife's answered dispatch; military paper is
    # physically set aside before she answers the personal request.
    for sid in ("irabeth.trickster.second_ask", "irabeth.trickster.nevi_reply"):
        own = page(sid, "her_answer")
        own["Text"] = '''{n}Irabeth lays the company's report on the finished stack. Anevia's answer stays beneath her bare hand.{/n}
"Nevi's evening stays hers. She wants me home before I make another invitation. I want that too."
{n}She stands, leaving both papers on the desk.{/n}
"That was her answer. Now ask me."'''
        page(sid, "yes")["Text"] = '''"Yes. I want you here."
{n}She comes round the company desk, takes your face between her hands and kisses you hard. The report slips to the floor. She lets it lie.{/n}'''
    page("irabeth.trickster.commit", "decides")["Text"] = '''"Not an order."
{n}She comes round the desk. Her hand stops just short of your cheek.{/n}'''
    page("irabeth.trickster.commit", "reckon")["Text"] = '''{n}Irabeth catches your hand before the kiss, then pulls you close herself.{/n}
"Yes. But hear me. I came back to a vow I cannot set down and a wife who had already buried me. I love her. That stays."
{n}She kisses you, then rests her forehead against yours.{/n}
"This isn't thanks. Don't you dare take it for thanks."'''
    # The kiss request cannot grant a yes before she has answered. Retain the
    # published producers and their effects as retired save slots; replacement
    # requests reach her answer, whose continuations record that answer.
    for nid in ("answer", "decides"):
        requests = page("irabeth.trickster.commit", nid)
        replacements = []
        for answer in requests["Choices"]:
            if answer.get("Next") == "reckon" and "irabeth.committed" in answer["Set"]:
                replacement = copy.deepcopy(answer)
                replacement["Set"].remove("irabeth.committed")
                replacements.append(replacement)
                answer["Requires"].append("trickster.now")
                answer["Forbids"].append("trickster.now")
        requests["Choices"].extend(replacements)
    for answer in page("irabeth.trickster.commit", "reckon")["Choices"]:
        answer["Set"].append("irabeth.committed")

    # Dawn is actually played; Hadran's amusement is no longer a prediction.
    private = page("irabeth.without_an_account", "private")
    private["Text"] = private["Text"].replace("Every night for two years, I've signed it.", "Every night, I sign it.")
    private["Text"] += '''
{n}At dawn Hadran catches you at the foot of the tack-store stair. He holds out the roll, with his signature under the night watch and an empty space for hers.{/n}
{n}"Your confirmation, ma'am. The west patrol returned six men short. Wounded, all accounted for."{/n}
{n}Irabeth reads the names before signing. Hadran's eyes flick to the blanket under her arm.{/n}
{n}"The report, Lieutenant. If you have something else to say, find a better hour." She hands it back, then brushes her fingers against yours before crossing the yard.{/n}'''
    battle = page("irabeth.the_hour_before_battle", "night")
    old = '{n}Later she arms you strap by strap'
    before, _ = battle["Text"].split(old, 1)
    battle["Text"] = before + '''{n}At dawn she buckles her own armor, then helps with any fastenings you cannot reach. At the duty board she writes her name beside yours.{/n}
{n}The officer assembling the muster looks from the landing to the chalk. "Both here, Knight-Captain?"{/n}
{n}"Both here. Count the west company again. Their wounded arrived after the bell."{/n}
{n}She stands beside you while the names are called. When the missing count is settled, she turns to you, briefly, and presses your hand. Then she goes to her company.{/n}'''

    # Near discovery is a lived interruption, never a new discoverability gate.
    secret_morning = page("irabeth.a_road_she_would_choose", "partner_lasting_0_morning")
    secret_morning["Text"] += '''
{n}A runner calls from the landing for the countersignature on the dawn patrol.{/n}
"I was on the west watch—" {n}Irabeth stops. She opens the door only far enough to take the paper.{/n}
"This is the east patrol. Give it to Hadran."
{n}She shuts the door and looks at the name she will have to give Anevia.{/n}'''
    for sid in ("irabeth.the_hour_before_battle", "irabeth.trickster.back_on_duty"):
        for suffix in ("", "_returned"):
            discovery = page(sid, "partner_discovery" + suffix)
            discovery["Text"] = discovery["Text"].replace(
                '"Don\'t. I said you could love somebody else.',
                '{n}Anevia cuts her off.{/n}\n"Don\'t. I said you could love somebody else.')
            discovery["Text"] += '''
{n}Irabeth lays a second sheet beside the roster: her own account of the night, with no military heading.{/n}
"The watch record is right. I was not there. I went to the Commander. Then I came home and lied to you."
{n}She turns the roster back toward Anevia.{/n}
"This one goes back to the company. The other is yours. I won't put soldiers' names into our lie."'''
            fallout = page(sid, "partner_fallout" + suffix)
            fallout["Text"] = fallout["Text"].replace(
                '"I chose it. I\'m not blaming the Commander."',
                '"I chose the night. I chose the lie. Nevi, I should have told you before you had to find it."')
            discovery["Choices"][1]["Text"] = '"The watch was needed. You are making too much of this."'
            # Keep the old evasion destination; append its response to that
            # shared fallout rather than changing the saved answer route.
            fallout["Text"] = fallout["Text"].replace('"We\'re finished.', '"Do not call it a watch. We\'re finished.')

    # Current wife location determines disclosure, not a prediction of pardon.
    for sid in ("irabeth.trickster.commit", "irabeth.trickster.second_ask", "irabeth.trickster.nevi_reply"):
        for node in books[sid]["Nodes"]:
            if node["Id"].startswith("morning"):
                node["Text"] = node["Text"].replace(
                    '{n}At dawn the watch changes under the window. ', '{n}', 1)
            if node["Id"] == "morning_home":
                node["Text"] = '''{n}Irabeth fastens the last gauntlet and lifts her sword from the desk.{/n}
"I am going to the gate. Nevi has waited outside these walls long enough. You can find your own breakfast."
{n}She kisses you once, with the gauntlet cold against your cheek, then goes out to the road.{/n}'''

    # Insert ten alternative/continuing cuts, each followed by its own paid
    # aftermath. Saved exits stay where they were, with their original effects.
    cut(books["i_crossing"], page("i_crossing", "night"), 1,
        '{n}Later, before she leaves')
    cut(books["irabeth.without_an_account"], private, 1,
        '{n}Later, the bell')
    cut(books["irabeth.the_hour_before_battle"], battle, 1, '{n}At dawn she buckles')
    cut(books["irabeth.a_road_she_would_choose"],
        page("irabeth.a_road_she_would_choose", "partner_lasting_0_night"), 1)
    for sid in ("irabeth.trickster.commit", "irabeth.trickster.second_ask", "irabeth.trickster.nevi_reply"):
        cut(books[sid], page(sid, "threshold"), 1)
        cut(books[sid], page(sid, "threshold_blow"), 2)

    # Loss remembers correspondence without declaring either a reconciliation
    # or a return to her military post. Paragraphs exist only on epilogues.
    gone = page("irabeth.ending_loss", "gone")
    gone["Text"] = '{n}Irabeth remained away from Drezen. The Commander kept the date of their first evening, and wrote no ending beneath it.{/n}'
    gone.setdefault("_IrabethRound2Paragraphs", []).extend((
        p('{n}No reply came from the road. No report named her among the dead.{/n}', forbids=("irabeth.return_reply",)),
        p('{n}Her reply came, precise and guarded. The Commander knew where to send a letter, but had no invitation to follow it.{/n}', requires=("irabeth.return_reply",), forbids=("irabeth.return_private_hour_kept",)),
        p('{n}She had come for the promised hour, corrected the account, and left again. That meeting did not put her back on the roster or undo the Coronation.{/n}', requires=("irabeth.return_private_hour_kept",)),
    ))
    lasting = page("irabeth.ending_lasting", "start")
    lasting["Text"] += '\n{n}At the end of the leave she came home dusty, furious with an innkeeper, and hungry. '
    lasting["Text"] += 'She caught the Commander by the sleeve at the door and kissed away the first question. Before the next journey she returned to the company desk to settle her unfinished reports. That evening she came back again.{/n}'
    page("irabeth.ending_open", "end")["Text"] += '\n{n}One autumn she returned to the same posting house and found the Commander waiting. '
    page("irabeth.ending_open", "end")["Text"] += 'She dropped her pack, caught a familiar collar in her fist, and insisted they settle the argument about the road upstairs.{/n}'
    # Service continues after a fatal sacrifice; no unanswered kitchen
    # invitation can address a living Commander in that history.
    service = page("irabeth.trickster.epilogue.under_orders", "end")
    service.setdefault("_IrabethRound2Paragraphs", []).append(p(
        "{n}After the Commander's memorial Irabeth completed the final roll without omitting a name. "
        'She kept the unanswered personal question to herself, and took the discharge to her wife, if the road still reached her.{/n}',
        requires=("sacrifice",), forbids=("trickster.commander_back",)))
    # The registered returned-lover page carries divinity without inventing
    # another payoff surface. Its saved inert exit retains identity/mechanics.
    record = page("irabeth.trickster.epilogue.off_the_record", "end")
    survival = record["Text"].replace(
        "until the Worldwound was closed", "until the fighting at Threshold ended")
    record["Text"] = '{n}Irabeth kept her own counsel after the war, and her own faith.{/n}'
    record.setdefault("_IrabethRound2Paragraphs", []).extend((
        p(survival, forbids=("ascended",)),
        p('''{n}When the Commander ascended, Irabeth refused to address a dispatch to a temple. She wrote the name she had spoken in the roster room, folded the company report inside, and left it on the cleared desk.{/n}
{n}At the next muster she corrected an officer who called the Commander's judgment infallible. "I argued with it before. I can argue with it now."{/n}''', requires=("ascended",)),
    ))
    # A previous lover's existing ascent owns that history, rather than also
    # playing this page. New returned lovers retain the distinct report above.
    payload.setdefault("Derived", {})["irabeth.round2.legacy_ascent"] = [["ascended", "irabeth.lover"]]
    books["irabeth.trickster.epilogue.off_the_record"]["Forbids"].append("irabeth.round2.legacy_ascent")


def ending_additions(scenes):
    """Append after shared employment/stance paragraphs keep their indices."""
    for book in scenes:
        if book.get("Relationship") != "irabeth":
            continue
        for page in book["Nodes"]:
            pending = page.pop("_IrabethRound2Paragraphs", [])
            if pending:
                page.setdefault("Paragraphs", []).extend(pending)

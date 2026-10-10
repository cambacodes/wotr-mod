"""Authored Minagho round-2 situations; the pair's saved surfaces stay in place.

Native evidence and the authored boundary are in minagho-setpieces.md. This
module changes only this relationship, after its existing stance integration.
No echo, extra seal power, resource price or reconciliation test is introduced.
"""
import copy
import json
from pathlib import Path

from story_format import c, n, p

P = "minagho_chivarro.trickster."
REL = "minagho_chivarro"
DEMAND = P + "rings_asked"
RINGS = P + "cost.rings_buried"
RECEIPT = P + "rings_receipt"


def _nodes(page):
    return {node["Id"]: node for node in page["Nodes"]}


def _situations(pages):
    # SP1: an offer is useful to an enemy, never a prematurely successful cure.
    for suffix in ("setup_c4", "setup_c3"):
        page = pages[P + "minagho_dead." + suffix]
        node = _nodes(page)["grin"]
        node["Text"] = ('{n}Minagho stops laughing. Blood runs from the mark down her eyeless face.{/n}\n'
            '"You volunteer? For his ledger? Look at what he did to me, Golarian. He will take considerably longer with you."\n'
            '{n}She wipes her brow and holds the blood toward you.{/n} "I could sell him your name. '
            'I could let him collect it himself. Yes. Put it down. I want to see which amuses me more."')
    # Keep the saved primer available when its native brand recital is observed.

    # SP2: proof belongs to the actual transfer, not the earlier promise.
    for suffix in ("minagho_dead.brand", "minagho_dead.brand_letter", "minagho_dead.collateral",
                   "spared.brand", "spared.brand_letter"):
        page = pages[P + suffix]
        for node in page["Nodes"]:
            if any(P + "minagho_in" in a["Set"] for a in node["Choices"]):
                node["Text"] += ('\n{n}Minagho wipes the mark. Her fingers come away dry. She digs a nail into '
                    'your open palm; the blood wells again. She presses her brow once more, harder.{/n} '
                    '"Still there. Still his. But he has the wrong hand." {n}She keeps your wrist until '
                    'she has felt the next pulse.{/n} "Do not congratulate yourself. I have not answered you yet."')
    for suffix in ("debt.collectors", "debt.collectors_spared"):
        node = _nodes(pages[P + suffix]).get("stamp")
        if node:
            node["Text"] += ('\n"He ordered me to kill you," {n}Minagho says, holding your wrist within reach '
                'of her knife.{/n} "I could finish the hunt now. I will not."\n'
                '{n}She lets the hand fall. At the next dawn the cut opens again; the collector takes '
                'the stained receipt. Her brow stays dry.{/n}')

    # SP3: their quarrel is hers to interrupt; keeping the debtor is self-interest.
    page = pages[P + "reunion.wardrobe"]
    for key in ("which", "which_debt"):
        node = _nodes(page).get(key)
        if node:
            node["Text"] += ('\n{n}Chivarro draws a dagger.{/n} "One throat, honey. Then we can stop discussing '
                'what this bastard has cost us."\n{n}Minagho catches her wrist before the point reaches '
                'you, turns it aside and keeps it.{/n} "And send the Goat his prize? No. I want this '
                'one breathing."\n"You always did keep expensive rubbish." {n}Chivarro puts the knife '
                'away, catches Minagho by the neck and kisses her. Minagho bites the answering insult short.{/n}')
    # Departure responds to the rejection, not before the player selects it.
    for node in list(page["Nodes"]):
        for answer in node["Choices"]:
            if P + "chivarro_sent_back" in answer["Set"]:
                answer["Next"] = "departure_answer" if node["Id"] in {"which", "which_debt"} else "departure_alone"
    page["Nodes"].extend([
        n("departure_answer", "Minagho", '"Your room, honey. Keep it." {n}Chivarro takes her cloak. '
          'Minagho stands to kiss her before she leaves.{/n}\n"You sent her away from you. Not from '
          'me. I will see her where she chooses. Do not start celebrating."'),
        n("departure_alone", "Chivarro", '"Then send word, honey. Do not come through my cupboards '
          'again." {n}Chivarro takes her cloak and leaves through the door.{/n}')])

    # SP4: lowest point -> public reckoning -> her claim. Three accounts, one cost.
    page = pages[P + "after.the_price_of_her_name"]
    node = _nodes(page)["verdict"]
    node["Text"] = ('{n}Three empty purses lie beside your hand: the one you opened for the bargain, '
        'the one Chivarro says the house swallowed, the one Minagho calls her spoils. Chivarro pushes '
        'them aside and makes you hold the palm open. Blood stains Wilcer\'s inventory.{/n}\n'
        '"Bought by richer. Rescued by better. Neither made such a fucking spectacle of it, honey."\n'
        '{n}Minagho takes your wrist. She presses her thumb into the cut until your fingers jerk.{/n}\n'
        '"Kenabres. Drezen. His cells. Every bastard with a claim wanted me kneeling. You have put '
        'your hand on the table instead."\n"It stays there until I finish," {n}Chivarro says.{/n}\n'
        '{n}Minagho leaves it open for her. When Chivarro folds the fingers shut, Minagho keeps the wrist.{/n}\n'
        '"Tonight you answer to me, Golarian. Ask properly."')
    # Letter counterpart pays the same public reckoning in person, not by a blot.
    page = pages[P + "after.the_price_of_her_name_letter"]
    node = _nodes(page)["start"]
    node["Text"] += ('\n{n}The returned sheet bears three totals, each crossed out by the other woman. '
        'Below them: "Bring the hand to the stores. Wilcer can keep the account."{/n}')
    for answer in node["Choices"]:
        if P + "cost.palm_on_table" in answer["Set"]:
            answer["Next"] = "reckoning_receipt"
    page["Nodes"].append(n("reckoning_receipt", "Minagho", _nodes(pages[P + "after.the_price_of_her_name"])["verdict"]["Text"]))
    page = pages[P + "after.before_the_last_road"]
    _nodes(page)["terms"]["Text"] = ('"Our house. Our names. You come when we ask, and we ask rarely," '
        '{n}Chivarro says. Minagho pulls your hand away from the drying ledger and into her lap.{/n}\n'
        '"I want you there. That is my answer. When the Goat calls, you do not bargain for me again. '
        'I will stand where I choose."\n{n}Chivarro closes a hand on Minagho\'s thigh.{/n} '
        '"And I want her there, honey. You heard both of us. Answer."')
    page = pages[P + "after.before_the_last_road_letter"]
    _nodes(page)["start"]["Text"] += ('\n{n}Minagho has written beneath the terms:{/n} '
        '"I want you. I kept the hand, did I not? Come when we call. Do not make me fetch you."')
    _nodes(pages[P + "after.who_keeps_the_house"])["start"]["Text"] += ('\n"The door faces the street," '
        '{n}Chivarro writes.{/n} "No closets. Let his servants knock where I can hear them."')

    # SP6: the seal collects daily; affection grants only the actual shared dawn.
    for page in pages.values():
        for node in page["Nodes"]:
            node["Text"] = node["Text"].replace("Minagho says you own her debt.",
                "Minagho says her seal bleeds on you.").replace("a mortal who owns my debt",
                "a mortal carrying my debt")
            node["Text"] = node["Text"].replace(
                "I will hear it every dawn now, lying next to you, because of me.",
                "On mornings you spend with us, I will hear it open. Because of me.")
            for para in node.get("Paragraphs", []):
                para["Text"] = para["Text"].replace("and every morning one of them was there to bind it.",
                    "and on mornings they spent together one of them bound it.")
                para["Text"] = para["Text"].replace("Every dawn, for the rest of the Commander's life, Minagho bound the palm herself",
                    "On the mornings they spent together, Minagho bound the palm herself")


def _rings(payload, pages):
    """F21--24: one paying situation, distinct from the scar and brand debts.

    Herrax's asking price is left unquantified, as in her native rings sale.
    This is an authored courier transaction, not a fictional inventory binding.
    """
    derived = payload.setdefault("Derived", {})
    derived[RECEIPT + ".not_killed"] = [["chapter_later"]]
    payload.setdefault("DerivedForbids", {})[RECEIPT + ".not_killed"] = ["chivarro.dead_confirmed"]
    derived[RECEIPT] = [[RECEIPT + ".not_killed"], [P + "chivarro_deposit"],
                        [P + "returned_chivarro"], [RINGS]]
    for page in pages.values():
        if not page["Id"].startswith(P + "alone.minagho") or page["Id"].endswith("morning"):
            continue
        for node in page["Nodes"]:
            for answer in node["Choices"]:
                if "minachiv.complete" in answer["Set"]:
                    answer["Requires"].append(RECEIPT)
            if node["Id"] in {"killer", "killer_start", "killer_decline", "killer_min"}:
                node["Text"] += ('\n{n}Minagho adds:{/n} "Herrax stripped her rings. Fetch them. Pay the bitch what she asks. '
                    'I will put them in the ground myself. Not in your trophy chest."')
        entry = page["Nodes"][0]
        entry["Choices"].append(c('[Ask what she wants done for Chivarro.]', "rings_demand",
            requires=("chivarro.dead_confirmed",), forbids=(P + "chivarro_deposit", P + "returned_chivarro", RINGS)))
        page["Nodes"].append(n("rings_demand", "Minagho",
            '"Her rings. Herrax keeps them. Pay her and bring them to me. I will bury them. '
            'You will stand there while I do it, Golarian. Then I decide whether I want you back."',
            c('[Arrange the purchase.]', "rings_purchase", flags=(DEMAND,)),
            c('[Leave the debt unpaid.]', abort=True)))
    paying_nodes = [
        n("rings_purchase", "Narrator", '{n}You send the descriptions and an order for the rings. '
          'When the courier returns, he lays Herrax\'s parcel on Wilcer\'s counter. Inside are '
          'the rings Minagho described, still scored where the house cut them away. Herrax has enclosed '
          'her price and a note: "No fingers this time, lover. Your bitch can supply her own." '
          'Minagho holds one ring against her knuckle. She sets it down without cleaning it.{/n}',
          c('[Pay the asking price and put the rings in Minagho\'s hand.]', "rings_burial"),
          c('[Return the parcel. Leave the debt unpaid.]', abort=True)),
        n("rings_burial", "Minagho", '{n}The courier counts the payment and leaves a receipt. Minagho takes '
          'you outside the wall, where the siege tore up the earth. She digs with her dagger. '
          'Each ring goes in separately; she covers them with her bare hand.{/n}\n'
          '"She tried to kill me in bed once. You succeeded where she did not. Remember that '
          'when you start feeling pleased with yourself."\n{n}She presses the receipt against your '
          'chest, leaving earth on your clothes.{/n} "Paid. Buried. I will answer you when I choose. '
          'Go. I am staying here a while."', c('[Return when she calls for you.]', "start", flags=(RINGS,)))]
    for page in pages.values():
        if page["Id"].startswith(P + "alone.minagho") and not page["Id"].endswith("morning"):
            page["Nodes"].extend(copy.deepcopy(paying_nodes))
    # An ending cannot turn the uncollected demand into a completed purchase.
    page = pages[P + "epilogue.minagho"]
    page["Requires"].append(RECEIPT)
    page["Nodes"][0].setdefault("Paragraphs", []).extend([
        p('{n}Minagho returned to the patch of earth outside Drezen where she had buried Chivarro\'s '
          'rings. She never took the Commander there again.{/n}', requires=(RINGS,)),
        p('{n}Herrax still held Chivarro\'s rings. Minagho had asked for them. The Commander had '
          'not brought them; she kept that account open.{/n}', requires=(DEMAND,), forbids=(RINGS,))])


def _heat(pages):
    for page in pages.values():
        for node in page["Nodes"]:
            node["Text"] = node["Text"].replace(
                'I will not call silence permission. If Chivarro can answer, she will. Until then, you have what I offer tonight. Nothing of hers.',
                'No word from Chivarro. Do not look so pleased, Golarian. I have not given you her place. Tonight you have mine.')
    page = pages["minachiv.the_unhired_evening"]
    _nodes(page)["want"]["Text"] = ('"Come here." {n}Chivarro pushes the tray out of reach and lets '
        'one shoulder slip from her dress. Minagho catches the exposed skin with her mouth; Chivarro '
        'takes a fistful of her hair and holds her there.{/n}\n"I have spent the evening watching '
        'your mouth, honey. You can stop making me work for it."\n{n}Minagho lifts her head.{/n} '
        '"I noticed first. Sit down before she invents a fee."')
    _nodes(page)["together"]["Text"] = ('{n}Chivarro draws you between their chairs. Minagho catches '
        'your open hand and puts it on Chivarro\'s waist, then pulls Chivarro toward her by the loosened '
        'sleeve.{/n}\n"Still pricing the mouth?"\n"I intend to try it, honey." {n}Chivarro turns '
        'back to you without releasing Minagho.{/n} "Both of us. You heard her. Now answer me."')
    _nodes(page)["slow"]["Text"] = ('"Then lose another round, honey." {n}Chivarro pulls her dress '
        'back over her shoulder and brings the tray between you. Minagho steals the remaining plum.{/n}\n'
        '"You had better be worth waiting for. Deal."')
    _nodes(page)["minagho"]["Text"] = _nodes(page)["minagho"]["Text"].replace(
        'I have waited for this through two cities and a demon lord\'s patience, and I am not going to spend it watching you think.',
        'The Goat can keep his patience. I am not spending our hour watching you think.')
    _nodes(pages["minachiv.minaghos_unfinished_sentence"])["hand"]["Text"] = (
        '{n}Minagho pulls your hand into her lap and turns the palm upward. Her thumb presses the scar; '
        'her other hand catches your jaw. She kisses you before you can ask what she found.{/n}\n'
        '"You keep coming back. His hunters have better excuses. Stay until the watch changes."')
    # Correct the robe before every later night removes it.
    page = pages["minachiv.after_the_last_lamp"]
    for node in page["Nodes"]:
        if node["Id"] == "start":
            node["Text"] += '''
{n}She wears a plain robe, fastened at the shoulder with a pin.{/n}'''
    # Invitations are a return, not another initiation or another arrival.
    for sid in ("minachiv.a_room_she_likes", "minachiv.after_the_last_lamp"):
        for node in pages[sid]["Nodes"]:
            if node["Id"] in {"later", "night"}:
                node["Text"] = node["Text"].replace('The part I have not rehearsed.',
                    'You know the way. Come closer.')


def _receipts(pages):
    # P27--33: preserve the physical lead, then the intended 96-hour fallback.
    for suffix in ("minagho_dead.brand_letter", "spared.brand_letter", "chivarro_dead.the_bill_letter",
                   "after.the_price_of_her_name_letter", "after.before_the_last_road_letter"):
        pages[P + suffix]["DelayHours"] = 120
    for suffix in ("alone.minagho_letter", "alone.chivarro_letter"):
        pages[P + suffix]["DelayHours"] = 192
    # P17--19/F33--35: identical existing rent on physical/letter histories.
    page = pages[P + "alone.chivarro_letter"]
    for node in page["Nodes"]:
        if node["Id"] == "came" or "_night_chivarro" in node["Id"]:
            for answer in node["Choices"]:
                if P + "night.chivarro" in answer["Set"]:
                    answer["Crusade"] = dict(Resource="Finances", Amount=-100)
    page = pages[P + "alone.chivarro_when_it_scars"]
    _nodes(page)["start"]["Text"] = ('{n}You wait five days, as she told you to. On the fifth, '
        'a runner stands beside your desk. The purse lies before you: a year\'s rent, in advance. '
        'He has not touched it. You have written no note.{/n}')
    _nodes(page)["chv"]["Text"] = ('{n}You send the purse. The runner returns with it still sealed '
        'and a message he has been made to learn by heart.{/n}\n"A year in advance. Nobody pays '
        'a madam in advance, honey; it is terribly bad business. It means you intend to come back. '
        'Come and ask me to my face. Bring the purse."')
    _nodes(page)["chv"]["Choices"][1]["Crusade"] = dict(Resource="Finances", Amount=200)
    for node in page["Nodes"]:
        if "_exclusive_" in node["Id"]:
            for answer in node["Choices"]:
                if "minachiv.closed" in answer["Set"]:
                    answer["Crusade"] = dict(Resource="Finances", Amount=200)
    # F52: the player chooses how to answer her proposed intimidation.
    page = pages["minachiv.the_paper_she_kept"]
    for key in ("fear", "service"):
        node = _nodes(page).get(key)
        if not node:
            continue
        node["Text"] = ('"Fear has an excellent memory." {n}Minagho tests the glove\'s torn seam.{/n}\n'
            '"The packet came with us. The false buyer\'s name will be withdrawn. I will not pretend '
            'I failed because the efficient answer was ugly."\n{n}She puts the needle through '
            'the leather.{/n} "Next time the accusation may be true. Decide whether you intend '
            'to stop me before I rely on you to stand in the doorway."')
        node["Choices"][0]["Text"] = '"I will not help you frighten a true account out of existence."'
        node["Choices"][0]["Next"] = "answer_principled"
        # Original reply keeps its index; only the new alternatives append.
        node["Choices"].extend([
            c('"Next time, take the papers first. We need the buyer alive."', "answer_pragmatic"),
            c('"Make the next reader afraid to print your name again."', "answer_complicit")])
    page["Nodes"].extend([
        n("answer_principled", "Minagho", '"You are going to make this tedious, aren\'t you?" '
          '{n}She takes up the needle.{/n} "Bring the lamp closer. I have heard you."', c("Continue", "door")),
        n("answer_pragmatic", "Minagho", '"Alive long enough to name the next bastard. Yes. '
          'I can work with that." {n}She tests the knife inside her sleeve, then reaches for the needle.{/n}', c("Continue", "door")),
        n("answer_complicit", "Minagho", '"There. You can be useful without bleeding." '
          '{n}She pulls your hand toward the torn glove, smiling.{/n} "Hold that. I need the light."', c("Continue", "door"))])

    # The ordinary journey survives on its actual history; an earned Trickster
    # reunion gets a local variant via appended routing, never new arrival flags.
    for sid, key in (("minachiv.two_answers", "start"), ("minachiv.her_own_arrival", "start")):
        page = pages[sid]
        node = _nodes(page)[key]
        old = copy.deepcopy(node["Choices"])
        native_text = node["Text"]
        if sid.endswith("two_answers"):
            native_text = native_text.replace('''"Chivarro?"
''', '').replace(
                '"She has answered. We have arranged',
                '{n}Minagho taps the other signature.{/n} "She has answered. We have arranged')
        else:
            native_text = native_text.replace('''"You came."
"An extraordinary deduction."''',
                '{n}Minagho catches Chivarro\'s wrist.{/n} "You came."\n'
                '{n}Chivarro smiles.{/n} "An extraordinary deduction."')
        node["Text"] = ('{n}You reach the shuttered gaming house at the appointed hour. '
                        'The door opens onto a room Minagho has kept away from the street.{/n}')
        for answer in node["Choices"]:
            answer["Forbids"].append(P + "reunited")
            if not answer["Abort"]:
                answer["Text"] = "Continue"
                answer["Next"] = "native_meeting"
        node["Choices"].append(c("Continue", "local_meeting", requires=(P + "reunited",)))
        text = ('{n}Minagho has sent an address across Drezen, above a shuttered gaming house. '
            'Chivarro has crossed out the little skull on the invitation and written the hour twice. '
            'When you arrive, Minagho takes the sheet from you.{/n}\n"She knows the road. It is '
            'three streets from her room. This time she insists on meeting you with her clothes '
            'and her temper undisturbed."' if sid.endswith("two_answers") else
            '{n}Chivarro has walked from her lodging below the citadel. Her damp cloak hangs '
            'behind the door. She catches Minagho by the neck and kisses her before turning to you.{/n}\n'
            '"A door, honey. My own feet. No cupboard, no delivery note. I am beginning to enjoy '
            'your city."\n"You were less complimentary yesterday," {n}Minagho says.{/n}\n'
            '"Yesterday you kept me waiting."')
        page["Nodes"].append(n("native_meeting", "Narrator", native_text, *copy.deepcopy(old)))
        page["Nodes"].append(n("local_meeting", "Minagho" if sid.endswith("two_answers") else "Chivarro", text, *old))
    # The subsequent account must match that local entry as well.
    page = pages["minachiv.her_own_arrival"]
    _nodes(page)["account"]["Text"] = _nodes(page)["account"]["Text"].replace(
        'I paid my own passage. Do not waste the evening trying to collect gratitude.',
        'I came here to talk. Do not waste the evening trying to collect gratitude.')

    # The engine already arbitrates earned outcomes. Preserve its selectors and
    # all terminal effect inventories; prohibit a second final arrangement.
    pages["minachiv.before_the_last_road"]["Forbids"].append(P + "committed")
    # Minagho's local coda, not the shared source file, names an actual return.
    from storylines import lastcall_partners
    part = next(x for x in lastcall_partners.PARTNERS if x["rel"] == REL)
    for para in part["paragraphs"]:
        if para["Requires"] == ["minachiv.future_minagho"]:
            para["Requires"].append(RECEIPT)
            para["Text"] = ('{n}Minagho returned from her own errands and left a dagger beside the '
                'door. On the mornings she invited the Commander to stay, she bound the bleeding '
                'palm herself. Chivarro\'s letters remained in her drawer; the Commander\'s key '
                'opened nothing of theirs.{/n}')
        if para["Requires"] == ["minachiv.future_two"]:
            para["AnyGroups"] = [["minachiv.future_two", "minachiv.future_together"]]
            para["Requires"] = []


def _slots(pages):
    """Append each approved node; keep every original node and exit effect.

    Epilogue exits are immutable. Their incoming paths visit the slot before
    reaching the old aftermath node. Elsewhere the old answer pays its original
    effects and the added slot returns to its original target.
    """
    root = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/minagho"
    for path in sorted(root.glob("*.json")):
        brief = json.loads(path.read_text(encoding="utf-8"))
        sid, nid = brief["source"]["scene"], brief["source"]["node"]
        page = pages[sid]
        nodes = _nodes(page)
        original = nodes[nid]
        slotid = brief["slot_id"]
        # A dedicated heated-cut default, filled only by the user's later batch.
        # Brief: willing participants/voice/act/continuity are in the matching JSON.
        body = original["Text"]
        split = next((body.index(mark) for mark in ('''

{n}Later''', '''

{n}Near dawn''',
            '''

{n}At dawn''', '''

{n}In the morning''') if mark in body), len(body))
        lead, after = body[:split], body[split:]
        if page["Owner"].endswith("Epilogue"):
            # Original saved terminal choices keep Next/Abort/Set and costs.
            for node in page["Nodes"]:
                for answer in node["Choices"]:
                    if answer["Next"] == nid:
                        answer["Next"] = slotid
            original["Text"] = after.strip() or '{n}The invitation has been answered.{/n}'
            page["Nodes"].append(n(slotid, original["Speaker"], brief["default_text"],
                                   c("Continue", nid), portrait=original.get("Portrait", "")))
        else:
            targets = copy.deepcopy(original["Choices"])
            original["Text"] = lead
            for answer in original["Choices"]:
                answer["Next"] = slotid
            # Threshold nodes in the manifest have one unconditional continuation.
            # Retain its original effects on the old answer, once only.
            continuation = [c("Continue", a["Next"], requires=tuple(a["Requires"]),
                              forbids=tuple(a["Forbids"]), abort=a["Abort"]) for a in targets]
            page["Nodes"].append(n(slotid, original["Speaker"], brief["default_text"],
                                   *continuation, portrait=original.get("Portrait", "")))


def integrate(payload):
    pages = {s["Id"]: s for s in payload["Scenes"] if s.get("Relationship") == REL}
    _situations(pages)
    _rings(payload, pages)
    _heat(pages)
    _receipts(pages)
    _slots(pages)

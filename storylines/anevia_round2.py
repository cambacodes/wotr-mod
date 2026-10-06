"""Authored round-two situations, not new prices or romantic entitlements.

Canon: Anevia/Cue_0071 (8e206818968aa9f4c828fd668b2a64c1),
Kaylessa_main/Cue_0093 (ea4d827995a68b24381d590724973965),
HorgusAnevia/Cue_0024 (377de2648a0f24d42864709080f850b9).
The fixed turn is she_pursues, at the smith side of Drezen's outer gate.
All rooms, watch evidence and romantic encounters are authored additions.
Slot prose stops at the act boundary; supplied briefs belong to the later pass.
"""
import copy
import json
from pathlib import Path

from story_format import c, n, p

SLOTS = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/anevia"
SURVIVAL = ("irabeth.trickster.returned", "irabeth.trickster.cost.dug_out",
            "irabeth.trickster.raised_on_record")


def insert_slot(book, brief):
    """Append a bridge before the saved aftermath page, keeping its answers.

    The old page and answer indices remain; only incoming links take the new
    act-boundary bridge. In-flight saves at that old page resume its aftermath.
    Terminal effects, including commitment receipts, stay on the old answers.
    """
    nodes = {page["Id"]: page for page in book["Nodes"]}
    page = nodes[brief["source_node"]]
    text = page["Text"]
    boundary = {
        "a_crossing": "{n}Later, she dresses",
        "anevia.the_evening_without_a_case": "{n}In the morning Anevia wakes",
    }.get(book["Id"])
    if boundary:
        build, after = text.split(boundary, 1)
        page["Text"] = boundary + after
    else:
        build = text
        # Existing outgoing choices keep their destinations, guards and effects.
        page["Text"] = {
            "threshold": "{n}The lantern has burned low beside the cloak. Anevia wakes at the sound of the relief watch outside.{/n}",
            "night": "{n}The room is quiet when Anevia reaches for you again. Beyond the shutter, a ration cart rattles over the stones.{/n}",
        }.get(page["Id"], "{n}Before the muster bell, Anevia sits up and reaches for her boots. Her ring catches the last of the lantern light.{/n}")
    buildup_id = "round2.buildup." + page["Id"]
    for old in book["Nodes"]:
        for answer in old["Choices"]:
            if answer.get("Next") == page["Id"]:
                answer["Next"] = buildup_id
    # Brief: her initiating motion, practical detail and marriage consequence;
    # no choice, return, forgiveness or quest state is supplied by the slot.
    book["Nodes"].extend([
        n(buildup_id, page["Speaker"], build,
          c("Continue", brief["slot_id"]), portrait=page.get("Portrait", "")),
        n(brief["slot_id"], "Narrator", brief["default_text"],
          c("Continue", page["Id"]), portrait=page.get("Portrait", ""))])


def integrate(payload):
    books = {book["Id"]: book for book in payload["Scenes"]}
    # Presence follows the promised journey, not the Kenabres conversation.
    # ContactWindows ignore flags absent from the history, so fetched and
    # magical clocks remain distinct; the physical crate gets both road legs.
    windows = [dict(Flag="anevia.trickster.gone.wardrobe", MinAgeHours=48),
               dict(Flag="anevia.trickster.gone.fetched", MinAgeHours=12),
               dict(Flag="anevia.trickster.gone.confession", MinAgeHours=48),
               dict(Flag="anevia.trickster.cost.crated", MinAgeHours=144)]
    payload["Presences"]["anevia.presence"]["ContactWindows"] = copy.deepcopy(windows)
    wardrobe = books["anevia.trickster.gone.wardrobe"]
    wardrobe["ContactWindows"] = [dict(Flag="anevia.trickster.cost.crated", MinAgeHours=72)]
    for suffix in ("gate", "fetched_gate"):
        books["anevia.trickster.gone." + suffix]["ContactWindows"] = copy.deepcopy(windows)
    nodes = {page["Id"]: page for page in wardrobe["Nodes"]}
    nodes["nail_crate"]["Text"] = '''{n}You climb back into the crate. Anevia drives one nail through the lid, then stops.{/n}
"Three days south in a box. Bet your council loved that. You ain't doin' three more north."
{n}She pulls the nail out and points you toward the quartermaster's stable.{/n}
"Ride back with the escort. Three days. I'll be at the gate when you get there. And don't follow me."'''
    nodes["named"]["Text"] = '''{n}The candle burns down. Anevia talks about the room's price and the ale below, keeping the knife in her hand. At the first call of the night watch she stands.{/n}
"That's your visit. Mine's at the Drezen gate. Ask the watch for my message when you get back. I'm not comin' in. You come out."'''
    nodes["nail"]["Text"] += '\n"Two nights," {n}Anevia calls through the door.{/n} "At the gate. Come out when I send word."'
    for suffix in ("commit", "fetched_commit"):
        book = books["anevia.trickster.gone." + suffix]
        for page in book["Nodes"]:
            if page["Id"] == "morning":
                # Survival without reconciliation never acquires a grave.
                page["Choices"][0].setdefault("Forbids", []).extend(SURVIVAL)
                page["Choices"].extend(c("Continue", "surviving_wife", requires=(flag,)) for flag in SURVIVAL)
        book["Nodes"].append(n("surviving_wife", "Anevia", '''"My wife ain't a grave you can talk over. What happened at Iz stays in the account."
{n}Anevia pulls on her boots and picks up her ring from the cloak.{/n}
"She hasn't made her peace with you. I ain't makin' it for her. I'm goin' home on the night I promised."
{n}She taps the door twice on her way out.{/n}''', c('"I will knock."'), portrait="Anevia"))
    fetched_retry = books["anevia.trickster.gone.fetched_second_ask"]
    for page in fetched_retry["Nodes"]:
        if page["Id"] == "start":
            page["Text"] = '''{n}At the next change of watch you knock on the guardhouse door. Anevia steps out before the sentry can answer. Her lantern is still burning.{/n}
"Heard you the first time. Had six hours to think about it. Come round here."'''
        elif page["Id"] == "price":
            page["Text"] = page["Text"].replace(
                "You know where I go when I don't want you near me. Now I get somethin' you can't take back, too.",
                "Beth brought me back to hear you. I heard you. This time you leave somethin' with me, too.")
    # Shared generation removed questions embedded in her speech. Keep these
    # statements complete before that scrub, across all copied gate histories.
    for suffix in ("gate", "fetched_gate"):
        for page in books["anevia.trickster.gone." + suffix]["Nodes"]:
            if page["Id"] in ("told", "told_left"):
                page["Text"] += ('\n"Next watch. Six hours. If you come, come out here."' if suffix.startswith("fetched")
                                 else '\n"Four nights. Same place. I\'ll be here first."')
    # Ending props require their played introductions; early lovers retain
    # the original breakup outcome without receiving a lease or goat game.
    changed = books["anevia.ending_changed_power"]["Nodes"][0]
    changed["Text"] = '''{n}Whatever the Commander became, Anevia wanted no part of it. She sent its messenger back with his boots tied together. That was the last answer she sent.{/n}'''
    changed.setdefault("Paragraphs", []).extend([
        p("{n}She left the green-cord key on the doorknob. The room she had offered the Commander would remain hers.{/n}", requires=("anevia.a_key_that_is_hers",)),
        p("{n}She kept the goat game, and the crooked little piece she had turned to face the wall. It went home with her.{/n}", requires=("anevia.ordinary_life_kept",))])
    aeon = books["anevia.ending_aeon"]["Nodes"][0]
    aeon["Text"] = aeon["Text"].replace("The borrowed room, the goat game, the nights she had picked: all of it was gone.",
                                        "The conversations they had kept were gone with that history.")
    for identity in ("anevia.ending_open", "anevia.ending_kept", "anevia.ending_promised"):
        books[identity]["Nodes"][0]["Text"] += '''
{n}On the first evening they had chosen after the campaign, Anevia returned with mud on her boots. She left her bag by the door, caught the Commander's collar and kissed away the greeting she had already guessed.{/n}
"There. Now tell me the bit I don't know."'''
    farewell = books["anevia.the_last_ordinary_thing"]
    farewell["Nodes"][0]["Choices"].append(c('"Supper at home before your watch? I will come back for the game."',
        "supper_before_watch", requires=("anevia.partner_stance.share", "irabeth.present_now"),
        forbids=("anevia.partner_lie_exposed",)))
    farewell["Nodes"].extend([
        n("supper_before_watch", "Irabeth", '''{n}At the Tirabades' table, Irabeth has moved a patrol map away from the bowls. Anevia steals the crust from the Commander's plate before sitting down.{/n}
"Eat something that belongs to you, Nevi."
"Can't. It's all Beth's cooking," {n}Anevia says.{/n}
{n}Irabeth pushes the basket toward her wife. When the watch bell sounds, Anevia puts down the crust and picks up her coat.{/n}
"Scout's late at the north post. I'm goin' to hear what he saw before someone cleans it up for a report."
"You said you would be home after the next watch," {n}Irabeth says.{/n}
{n}Anevia leans over her wife's chair and kisses her.{/n}
"I said it. I'll keep it. Leave the burnt bit for me."''',
          c('[Stay for the next watch.]', "back_from_watch"),
          c('[Say goodbye before taking the road.]', "future"), portrait="Irabeth"),
        n("back_from_watch", "Anevia", '''{n}Irabeth hears the latch before you do. Anevia comes in with mud up to her knees and sets a folded account beside the patrol map.{/n}
"Two cultists watchin' the supply road. Scout got the numbers right. Got scared when somebody asked him twice."
{n}Irabeth takes the account. Anevia stays long enough to answer her first question, then reaches for the cold bread.{/n}
"That's for the morning briefing," {n}Irabeth says.{/n} "Sit down."
{n}Anevia sits between you. She breaks off the burnt crust and puts half on your plate.{/n}
"Came back, didn't I? Now you can both stop listenin' for boots."''',
          c('[Finish supper before the farewell.]', "future"), portrait="Anevia")])
    return_text = '''{n}At the next visit they had chosen, Anevia came back and knocked twice before lifting the latch herself. She put a heel of bread beside the Commander's cup.{/n}
"Probably," {n}she said, and caught the Commander by the shirt before another question could spoil it.{/n}'''
    for book in payload["Scenes"]:
        if not book["Id"].startswith("anevia.") or not book["Owner"].endswith("Epilogue"):
            continue
        if book["Owner"] == "AeonEpilogue":
            continue
        for page in book["Nodes"]:
            if any("anevia.trickster.cost.her_key" in paragraph.get("Requires", ())
                   for paragraph in page.get("Paragraphs", ())):
                page["Paragraphs"].extend([
                    p(return_text, requires=("anevia.trickster.cost.her_key", "anevia.committed", "anevia.present_now"),
                      forbids=("sacrifice",)),
                    p(return_text, requires=("anevia.trickster.cost.her_key", "anevia.committed", "anevia.present_now",
                                             "sacrifice", "trickster.commander_back"))])
    # The case carries evidence, not an automatic intimate reward. She catches
    # a real watch discrepancy and keeps her evening rather than inventing work.
    evening = books["anevia.the_evening_without_a_case"]
    start = evening["Nodes"][0]
    start["Text"] += '''
{n}A runner calls the dispatch hour from the passage. Anevia glances toward him, then shuts the door.{/n}
"Already sent. I ain't borrowin' another hour off a case. This one's mine."
{n}She moves her chair beside yours and taps the crooked goat against your knuckles.{/n}'''
    # Split at the act boundary only. Refused kisses, sleep and grief get no slot.
    for path in sorted(SLOTS.glob("*.json")):
        brief = json.loads(path.read_text(encoding="utf-8"))
        identity = brief["slot_id"].rsplit(".explicit.", 1)[0]
        if identity not in books or identity.startswith("three_"):
            continue  # Joint nights belong to their shared owner.
        insert_slot(books[identity], brief)

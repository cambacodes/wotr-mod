"""Authored round-2 situations; canon anchors are in jerribeth-setpieces.md.

The collector/cache is an extension of the existing market appointment, not a
quest, affection test, or return device. Mental scenes stay inside the leased
imagining. Marhevok's native fate is never rewritten. All answers and pages
already in the route keep their positions and identities.
"""
import copy
import hashlib
import json
import re
from pathlib import Path

from story_format import c, n, p
from storylines import jerribeth_partner as partner

RETURNED = partner.RETURNED
VISITED = "jerribeth.trickster.visited"
DEFERRED = "jerribeth.trickster.visit_deferred"
SCALE = "jerribeth.scale_kept"
SCALE_BACK = "jerribeth.scale_returned"
SCALE_PAID = "jerribeth.scale_hour_collected"
LOST = "jerribeth.collection_refuge_lost"
MIND_LOST = "jerribeth.mental_refuge_lost"
GRUDGE = "jerribeth.trickster.cost.toast_grudge"
PAID = "jerribeth.trickster.cost.toast_interest"
LEVY = "jerribeth.trickster.toast_levy"


def page(id, text, *answers):
    return n(id, "Jerribeth", text, *answers, portrait="Jerribeth")


def node(event, id):
    return next(x for x in event["Nodes"] if x["Id"] == id)


def replace_path(answer, target, marker="trickster.ever"):
    """Retire only in the relevant history; caller appends the replacement.

    Old Next/Set/Abort and answer identity are untouched, including exits.
    """
    twin = copy.deepcopy(answer)
    answer["Forbids"].append(marker)
    twin["Requires"].append(marker)
    twin["Next"] = target
    return twin


# Each number names a Commander quote in the original text, not an alternating
# speaker heuristic. In particular, puppet imitations and relayed guests stay
# Jerribeth's speech. Splitting is done before the situation rewrites below.
PLAYER_QUOTES = {
    "offered_signature": {"price": [2], "ownership": [2], "performance": [1], "send": [2]},
    "borrowed_sun": {"shape": [2], "empty": [1, 3, 5], "expose": [1, 3, 5], "account": [1, 3], "power_reply": [1]},
    "small_print": {"start": [1], "kept": [1], "test": [1], "choice": [1], "correct": [2], "withdraw": [2], "after": [1, 4]},
    "unsold_evening": {"start": [1], "guise": [1], "near": [1], "frame": [1], "story": [2, 5], "after": [0, 2, 5], "joke_enjoyed": [2], "joke_disputed": [1]},
    "purchaser_answer": {"sale": [1, 4], "performance": [1], "design": [1], "withdrawn": [2, 4], "kept": [2], "kept_design": [1], "temptation": [1], "credit": [2]},
    "counterfeit_guest": {"previous_buyer": [2], "maker": [2], "return": [2], "appetite": [2], "square": [2], "judgment": [2], "keep": [1]},
    "counterfeit_hinge": {"patient": [1], "result": [2], "clerk": [2]},
    "counterfeit_clerk": {"payment": [2], "witness": [1], "drawings": [1], "release": [2], "end": [2]},
    "counterfeit_audience": {"leverage": [3], "archive": [0], "departure": [2]},
    "counterfeit_spoil": {"circles": [3], "work": [1], "account": [1, 4], "catalogue": [1], "price": [1], "object": [2], "interest": [1, 3, 5], "complicit": [1], "end": [1, 4]},
    "counterfeit_after": {"wanted": [2, 5], "own": [1], "guise": [1, 4], "attention": [1], "quiet": [2], "after": [1], "promised": [2], "next": [2], "fate": [2], "end": [2]},
    "settlement_visit": {"visible": [1], "removed": [2], "report": [3], "comedy": [1], "decline": [2], "private_cost": [2]},
    "room_measure": {"public_visible": [2], "public_refused": [2], "private_play": [3], "private_declined": [2], "loop": [1, 3], "terrace": [2, 5], "private": [2], "quiet": [1]},
    "promise_revisited": {"chosen": [2]},
    "fate_envelope": {"start": [2], "test": [2, 5], "purpose": [1], "work": [3], "company": [1]},
}


def split_player_speech(event, targets):
    for id, indices in targets.items():
        old = node(event, id)
        matches = list(re.finditer(r'"[^\"]*"', old["Text"]))
        text, tail, pages = old["Text"], old["Choices"], []
        # A Commander attribution immediately after the quote is part of that
        # speech. Narration belonging to her response remains on its page.
        previous = 0
        for k, index in enumerate(indices):
            match = matches[index]
            end = match.end()
            attribution = re.match(r'\s*\{n\}you (?:ask|say|tell her)\.\{/n\}', text[end:])
            if attribution:
                end += attribution.end()
            next_id = id + ".reply." + str(k + 1)
            current = old if k == 0 else pages[-1]
            current["Text"] = text[previous:match.start()].strip() or '{n}She waits for your answer.{/n}'
            if k == 0:
                # All old choices stay at their old indices. They become saved
                # continuations; the appended answer enters the missing reply.
                marker = event["Requires"][0]
                for answer in tail:
                    answer["Requires"].append(marker)
                    answer["Forbids"].append(marker)
                current["Choices"] = tail + [c(match.group(), next_id)]
            else:
                current["Choices"] = [c(match.group(), next_id)]
            pages.append(page(next_id, ""))
            previous = end
        pages[-1]["Text"] = text[previous:].strip() or '{n}She waits for your answer.{/n}'
        # Effects belong to the same final answer, after the same information.
        pages[-1]["Choices"] = copy.deepcopy(tail)
        marker = event["Requires"][0]
        for answer in pages[-1]["Choices"]:
            answer["Requires"].remove(marker)
            answer["Forbids"].remove(marker)
        event["Nodes"].extend(pages)


def disclosure(event, target):
    old = node(event, target)
    saved = copy.deepcopy(old["Choices"])
    marker = "jerribeth.marhevok_disclosed." + event["Id"]
    for answer in old["Choices"]:
        answer["Requires"].append(marker)
    old["Choices"].extend(c('"And Marhevok?"', "marhevok_early_" + fate, **guard)
                          for fate, guard in partner.fate_guards().items())
    texts = {
        "plant": '{n}She turns the image toward a pot. Human eyes stare from its fleshy bud; a vine pulls taut against the rim.{/n}\n"Marhevok. My lover. I found him a shape I could keep. He still watches me. You wanted to know what I do with devotion."',
        "chief": '"Marhevok went back to Wintersun to make amends to his people. He called me his sun even as he left. I keep his letters. You need not expect him to congratulate you."',
        "dead": '"Marhevok is dead. He loved me. Do not look so relieved: you have heard how I kept him, not a promise that I shall keep you differently."',
        "distant": '"Marhevok was in his pot when I lost my body. My lover, left in the Sanctum. Your skull has no room for his roots, and I have no news to tell you."',
        "unknown": '"Marhevok, the Wintersun chief. He loved me. I have no news of his fate. I shall not sell you his silence as an empty place beside me."',
    }
    for fate, text in texts.items():
        answers = copy.deepcopy(saved)
        for answer in answers:
            answer["Set"].append(marker)
        event["Nodes"].append(page("marhevok_early_" + fate, text, *answers))


def install_slots(events):
    root = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/jerribeth"
    for path in sorted(root.glob("*.json")):
        brief = json.loads(path.read_text(encoding="utf-8"))
        placement = brief["placement"]
        event = events[placement["scene"]]
        threshold = node(event, placement["after_node"])
        old_choices = copy.deepcopy(threshold["Choices"])
        # Keep the original destination and effects at the saved answer index.
        marker = event["Requires"][0]
        for answer in threshold["Choices"]:
            answer["Requires"].append(marker)
            answer["Forbids"].append(marker)
        threshold["Choices"].append(c("Continue", brief["slot_id"]))
        # EXPLICIT SLOT: continuation brief in the JSON named by slot_id;
        # default is the heated cut. No explicit prose is authored here.
        event["Nodes"].append(n(brief["slot_id"], "Narrator", brief["default_text"],
                                 *old_choices, portrait="Jerribeth"))


def debt_and_presence(events):
    letter = events["jerribeth.trickster.visit_letter"]
    letter["DelayHours"] = 108
    old = node(letter, "start")["Choices"][0]
    old["Forbids"].append("jerribeth.trickster.visit_due")
    node(letter, "start")["Choices"].append(c(old["Text"], flags=(DEFERRED,)))
    # The physical visit and presence keep VISITED as their completion reader;
    # DEFERRED has no consumer that could suppress another attempt.
    reaction = events["jerribeth.trickster.reaction.woljif_visitor"]
    reaction["Entry"] = '"About Jerribeth\'s visit..."'
    node(reaction, "start")["Text"] = '''"Chief. That demon who visited you. People buy things in the market, then go home and lock the door. You brought the buyer home."
{n}Woljif scratches the base of one horn.{/n}
"One memory, her pick? I've sold plenty I didn't own. I never let the buyer choose which. Give her a boring one. A queue. The weather. Something she won't come back for."'''
    for id in ("jerribeth.refuge", "jerribeth.patron", "jerribeth.fate_envelope"):
        event = events[id]
        event["Forbids"] = [f for f in event["Forbids"] if f != "crossroute.vellexia.unavailable"]
        for item in event["Nodes"]:
            for answer in item["Choices"]:
                answer["Forbids"] = [f for f in answer["Forbids"] if f != "crossroute.vellexia.unavailable"]
    future = events["jerribeth.future"]
    for id in ("interest", "interest_short"):
        old = node(future, id)
        destination = old["Choices"][0]["Next"]
        old["Text"] = '{n}The memories tear loose: faces across raised cups, celebrations, wakes. You remember drinking. You cannot remember whom you honoured.{/n}'
        old["Choices"][0]["Forbids"].append("jerribeth.trickster.cost.toast_grudge")
        old["Choices"].extend((c("Continue", id + "_king", forbids=(LEVY,)), c("Continue", id + "_levy", requires=(LEVY,))))
        for carrier, text in (
            ("king", '{n}One toast remains: the deserter lowering his cup at the Fool King\'s bench, her voice coming from his mouth.{/n}'),
            ("levy", '{n}One toast remains: the Wintersun sergeant pouring your cup among the levy, her voice coming from his mouth.{/n}')):
            future["Nodes"].append(page(id + "_" + carrier, text + '\n"Interest received. Now we may talk about promises."', c("Continue", destination)))
    unfinished = events["jerribeth.ending_unfinished"]
    unfinished["Forbids"].append("sacrifice")
    unfinished.setdefault("ForbidOverrides", {})["sacrifice"] = "trickster.commander_back"


def scale_decision(event):
    old = node(event, "morning_free")
    old["Text"] = '''{n}She has left before the watch changes. On your pillow lies the glossy sliver you pulled from her wing. Beside it, the frame wakes.{/n}
"My scale. A loan. Each night you keep it buys me an hour of your attention. Give it back, and we are square."
{n}Her antennae incline toward your hand.{/n}
"Well?"'''
    saved = copy.deepcopy(old["Choices"])
    for answer in old["Choices"]:
        answer["Requires"].append(SCALE_BACK)
    old["Choices"].extend((c('[Keep the scale.]', "scale_keep", flags=(SCALE,)),
                           c('[Return it when she next opens the frame.]', "scale_return", flags=(SCALE_BACK,))))
    event["Nodes"].append(page("scale_keep", '"I take the first hour now. Your quartermasters can wait."\n{n}She watches you put the scale beside the frame. When the next watch is called, she is still telling you which of Drezen\'s locks she dislikes. You have heard a great deal about the one on your door.{/n}',
                               c('[Stay for the hour she collects, then keep the scale.]', "scale_kept_receipt", flags=(SCALE_PAID,))))
    event["Nodes"].append(page("scale_kept_receipt", '"One hour received. Keep it another night and I shall come looking for the next."', *copy.deepcopy(saved)))
    event["Nodes"].append(page("scale_return", '{n}You place the sliver against the frame. She holds up its bare edge on her side, studies your expression, and laughs.{/n}\n"Square. How disappointing. I had plans for your next hour. I shall have to make you want them."\n{n}The scale stays beside the frame until she can reclaim it in person.{/n}', *copy.deepcopy(saved)))


def integrate(payload):
    events = {s["Id"]: s for s in payload["Scenes"] if s["Id"].startswith("jerribeth.")}
    for suffix, targets in PLAYER_QUOTES.items():
        split_player_speech(events["jerribeth." + suffix], targets)
    # Alternatives where the old embedded line assigned a moral judgment or a
    # restriction. They change the spoken position, not the earned outcome.
    for suffix, id, text, reply in (
        ("borrowed_sun", "shape", '"You want to see whether I still admire the work."', None),
        ("counterfeit_guest", "previous_buyer", '"You kept the agreement. That matters more than their gossip."', None),
        ("counterfeit_spoil", "complicit", '"You enjoyed yourself. I was watching you."',
         '"I did. He meant to make me kneel. Instead he waited while I repeated your words. I shall remember the expression you brought for that."'),
        ("promise_revisited", "chosen", '"Then I will bring you a name when I want someone ruined."',
         '"And I shall bring you the price. You have become an expensive preference, Commander. I would like you to make yourself useful."'),
    ):
        event = events["jerribeth." + suffix]
        old = node(event, id)
        continuation = id + ".reply.1"
        if reply:
            alternative = copy.deepcopy(node(event, continuation))
            alternative["Id"] = id + ".other_reply"
            alternative["Text"] = reply
            event["Nodes"].append(alternative)
            continuation = alternative["Id"]
        old["Choices"].append(c(text, continuation))
    for item in events["jerribeth.small_print"]["Nodes"]:
        for answer in item["Choices"]:
            answer["Text"] = answer["Text"].replace('"You can ask without earning it. I can answer without owing it."',
                '"Ask me again when there is no purchaser waiting."')
    for event in events.values():
        for item in event["Nodes"]:
            item["Text"] = (item["Text"].replace("An adult tiefling", "A tiefling")
                            .replace("an adult elven face", "an elven face")
                            .replace("An adult dwarf", "A dwarf")
                            .replace("An adult woman", "A woman"))
    debt_and_presence(events)
    for id, target in (("price", "terms"), ("evening", "start"), ("patron", "start"), ("refuge", "start")):
        disclosure(events["jerribeth." + id], target)
    evening = events["jerribeth.evening"]
    node(evening, "start")["Text"] = '''"Tonight I want your attention. Not a report from the Sanctum, not a promise that the war will leave you time. Yours."
{n}The dark frame holds her image. She waits for an answer.{/n}'''
    # Both attention answers take the tenant ladder; jealousy dialogue remains
    # intact for living correspondence. Her own lover has now been disclosed.
    for item in evening["Nodes"]:
        if item["Id"] != "start" and not item["Id"].startswith("marhevok_early_"):
            continue
        for other in list(item["Choices"]):
            if other.get("Next") not in ("want", "others"):
                continue
            # The disclosure continuations copied both attention answers.
            # Sweep those copies as well as the original opening.
            if "jerribeth.trickster.cost.tenant" in other["Forbids"]:
                continue
            twin = copy.deepcopy(other)
            other["Forbids"].append(RETURNED)
            twin["Requires"].append(RETURNED)
            twin["Next"] = "tenant_evening"
            item["Choices"].append(twin)
    x = node(events["jerribeth.price"], "x_start")
    x["Text"] = x["Text"].replace('{n}Her projected hands draw together.{/n}', '', 1)
    write_situations(events)
    # These are reports of patronage, not a living Vellexia cameo. Establish
    # that in the prose so the shared presence classifier can preserve this
    # correspondence even after her death or an unrelated romance refusal.
    for event in (events["jerribeth.refuge"], events["jerribeth.patron"], events["jerribeth.fate_envelope"]):
        for item in event["Nodes"]:
            item["Text"] = (item["Text"]
                .replace("Vellexia's protection has become a story people tell when deciding how much danger I am worth.",
                         "Vellexia gave me protection. People have been pricing me by what they think remains of it.")
                .replace("Vellexia still has her house. Whether I care to remain useful there is another question.",
                         "Her house still stands. Whether I care to remain useful there is another question.")
                .replace("Vellexia understands entertainments that would exhaust a lesser imagination. Her curiosity is also capable of exhausting the people expected to satisfy it. If you seek her attention, prepare to keep earning it.",
                         "Vellexia offered me a place in her house. I earned it by keeping her curious. She expected new amusements, not gratitude. If you seek that kind of protection, find something worth selling first.")
                .replace("Vellexia's affairs", "Vellexia's secrets"))
    install_slots(events)
    late_debts(events["jerribeth.trickster.epilogue.commit"])
    localize_late_choices(events["jerribeth.trickster.epilogue.commit"])
    # Claude voice layer (edge job 10): text of existing nodes, before the
    # scaffolding copies host answers onto its companion pages.
    from storylines import jerribeth_voice
    jerribeth_voice.revoice(payload)
    from storylines import jerribeth_scaffolding
    jerribeth_scaffolding.integrate(payload)
    # Cloud voice-owner layer (villain-route-jerribeth): last text over existing pages,
    # after the scaffolding so its saved-prose contract stays a Codex-side guarantee.
    from storylines import jerribeth_cloud
    jerribeth_cloud.apply(payload)


def write_situations(events):
    # Three remote nights have different failures of her control. The charm
    # carries descriptions/images: the intimate approach is jointly imagined.
    rewrites = {
        ("unsold_evening", "kiss"): '''{n}Her image draws close enough to cut off the ruined lamp. She hooks a claw beneath her collar and bares the narrow line beneath it.{/n}
"Here. Imagine your hand here. Mine would already be inside that aggravating collar of yours."
{n}She follows your gaze, catches it, and holds it. The charm stands between your separate rooms; in the scene you describe together there is no table left between you.{/n}
"Now come closer. I want to hear what that does to your voice."''',
        ("counterfeit_after", "desire"): '''{n}The window fills with a city folded impossibly over itself. Jerribeth turns her back on the expensive view. A light behind her begins repeating its course.{/n}
"Let it. You were looking at me."
{n}In the room you imagine together she draws you against the sill. Her mouth interrupts the answer she has been waiting for; her claw catches the fastening she has described at your throat.{/n}
"There. Much better than applause. Tell me where you want my hand next."''',
        ("room_measure", "desire"): '''{n}She leaves the heavy arch unfinished. Her image comes close; the street behind it dwindles to bare planks.{/n}
"You can look at the screws tomorrow. Tonight I have something else for those hands."
{n}She describes taking them, placing them against her own shape. In your shared imagining you feel the ridge beneath her fingers, the cold hinge of her wing. She follows every pause in your answer.{/n}
"Slower. I intend to enjoy how badly you want to hurry."''',
    }
    for (suffix, id), text in rewrites.items():
        node(events["jerribeth." + suffix], id)["Text"] = text
    after = events["jerribeth.unsold_evening"]
    # The rest of this page is now selectable dialogue, including the attitude
    # formerly narrated as the Commander's own philosophy.
    for item in after["Nodes"]:
        item["Text"] = item["Text"].replace(
            "Spend it here, then. I will not ask you to steal it from somebody else so that I can admire the theft.",
            "Spend it here. I have ruined a perfectly good lamp for you. Your officers may have the next watch.")
    node(after, "after")["Text"] = '{n}She lets the room stay dark. Her hands are still in the frame; the ruined lamp remains where she left it.{/n}'
    node(events["jerribeth.counterfeit_after"], "after")["Text"] += '\n{n}She closes the window before calling for Serit. The image she left for you stays out of his drawings.{/n}'
    node(events["jerribeth.room_measure"], "end")["Text"] += '\n{n}She keeps the street dark while the next march is called outside your room. Before you close the frame, her claws touch her collar again.{/n}\n"Come back. I have not finished with you."'

    refuge = events["jerribeth.refuge"]
    start = node(refuge, "start")
    saved = copy.deepcopy(start["Choices"])
    for answer in start["Choices"]:
        answer["Requires"].append("jerribeth.refuge_outcome_reviewed")
    defect = "jerribeth.harem.vellexia_defection_seen"
    for lost, betrayed in ((False, False), (False, True), (True, False), (True, True)):
        id = "refuge_outcome_%s_%s" % (int(lost), int(betrayed))
        req = [f for f, yes in (("jerribeth.patron_lost", lost), (defect, betrayed)) if yes]
        no = [f for f, yes in (("jerribeth.patron_lost", lost), (defect, betrayed)) if not yes]
        start["Choices"].append(c('[Hear what happened at the manor.]', id, requires=req, forbids=no))
        text = ('"Vellexia is gone. Her name opens fewer doors already."' if lost else
                '"Vellexia still has her house. Whether I care to remain useful there is another question."')
        if betrayed:
            text += '\n"You saw which side I chose when the fighting began. I do not intend to spend the rest of my life being thanked for it. I intend to profit."'
        else:
            text += '\n"A patroness has appetites. So have I. I have not confused protection with ownership."'
        # Fate-specific early disclosure follows; no imported actor or patron
        # romance closure changes the facts here.
        answers = copy.deepcopy(saved)
        for answer in answers:
            answer["Set"].append("jerribeth.refuge_outcome_reviewed")
        refuge["Nodes"].append(page(id, text, *answers))

    # Near-discovery rides the existing refuge conversation. It neither sets
    # exposure nor makes the chief travel to the Abyss.
    for item in refuge["Nodes"]:
        if item["Id"] == "marhevok_early_plant":
            item["Text"] += '\n{n}A vine pulls the curtain into view. She tears the hem free and puts it back between the pot and the frame.{/n}\n"He notices where I aim my voice. Cloth will not keep your name out forever."'
        elif item["Id"] == "marhevok_early_chief":
            item["Text"] += '\n{n}She raises a letter bearing his mark.{/n}\n"He asks who occupies my evenings. I have not answered that question yet. He has a village to govern. I have other uses for his jealousy."'

    visit = events["jerribeth.trickster.visit"]
    arrival = node(visit, "arrival")
    arrival["Text"] = '''{n}At the spice stall Jerribeth stands beside two cases. Behind her a horned stranger stops at every stall she has passed, sniffing the latches. The quartermaster's boy keeps counting sacks for the next march.{/n}
"A collector. He wants what I took when I left the laboratories. He has followed the empty outer case beautifully."
{n}She shows you a store doorway beside the stall. Through it you can see a narrow rear passage into the next street.{/n}
"My hiding place. The real collection is already packed. Do try to look at the case and not the door."'''
    saved = copy.deepcopy(arrival["Choices"])
    for answer in arrival["Choices"]:
        answer["Requires"].append(LOST)
    arrival["Choices"].extend((
        c('[Send the collector to the next stall while she moves the cases.]', "collector_cover"),
        c('"He is doubling back. Take the rear passage."', "collector_return")))
    visit["Nodes"].extend([
        page("collector_cover", '''{n}You point the stranger toward a stall piled with empty crates. Jerribeth watches him go, then slips a twitching specimen box beneath one crate's lid.{/n}
"An improvement. But he has no interest in cardamom. Let me give him something worth smelling."
{n}She takes the real case into the store. Outside, the stranger opens the crate and turns sharply toward the doorway.{/n}''', c('"He has found the trail."', "collector_return")),
        page("collector_return", '''{n}The stranger blocks the store's front door. Jerribeth is already beyond the rear passage with her cases. The latch lifts in front of you.{/n}
{n}Then her antennae appear at the rear doorway again. She sets the cases down, comes back, and catches your sleeve.{/n}
"This way. Quickly. I have no intention of listening to him tell me what you fetched."
{n}She draws you through the passage. Behind you the collector forces the front door. He has found the cache; she will not be able to use it again.{/n}''',
             c('[Take her hand and leave with her.]', "collector_after", flags=(LOST,)),
             c('"Go. I will leave separately."', "collector_separate", flags=(LOST,))),
        page("collector_separate", '''{n}She releases your sleeve, waits beyond the rear doorway until you reach the street, then takes up both cases.{/n}
"Separate, then. You still owe me an evening. I choose to have it tonight."''', c("Continue", "collector_after")),
        page("collector_after", '''{n}She shuts the cases at the corner. The collection is intact; her old doorway stands open behind her. She checks the smaller case twice.{/n}
"I could have kept that room. Do not look so pleased. I shall be unpleasant about losing it."
{n}She gives you a long, exact look.{/n}
"Go home. I know the way."
{n}After dark she knocks three times at your quarters. Her own shape fills the doorway; both cases rest beneath her folded wings. Behind you, the reports for Threshold lie unread.{/n}''', *saved),
    ])
    cases = node(visit, "collector_after")
    cases["Text"] += '\n"Two cases. The things I kept, and the things I want near you. Do not call either a gift."'
    cases["Choices"][0]["Text"] = '[Take the cases inside on the terms you agreed.]'
    cases["Choices"].extend((c('"Leave the cases a moment. Tell me plainly why you came back."', "collector_plain"),
                               c('"The affair is what I promised. Keep it that way."', "collector_affair", requires=("jerribeth.short_future_chosen",))))
    visit["Nodes"].extend([
        page("collector_plain", '"Because I wanted you. There. How little pleasure that gives me to say."\n{n}She touches the latch of the specimen case, then leaves it shut.{/n}\n"I still want everything in here. You have become another thing I choose to keep close. Do not expect me to be gracious about it."', *copy.deepcopy(saved)),
        page("collector_affair", '"An evening, then. And another when you can pay attention. I heard the promise you made. I chose it."\n{n}She leaves the cases beside the door instead of unpacking them.{/n}', *copy.deepcopy(saved)),
    ])
    # Marhevok remains in his room until her portable-pot witness/discovery;
    # no extra rescue, disappearance or death is inferred from the cache loss.
    for id in ("morning", "morning_free"):
        node(visit, id)["Text"] += '\n{n}The cases are gone with her. The smaller one left an indentation beside the bed. The frame lights again before the next march; she has returned to finish the evening she claimed.{/n}'
    scale_decision(visit)
    # Physical legacy copies retain their own scale branch and destinations.
    scale_decision(events["jerribeth.future"])
    for event, id, destination in ((visit, "ask", "visit_pause"),
                                   (events["jerribeth.future"], "tenant_body", "tenant_pause")):
        node(event, id)["Choices"].append(c('"Stay. Tonight I only want your company."', destination))
        answers = ([c('[Keep the evening, without going to bed.]', flags=(VISITED,))] if event is visit else
                   [c('[Keep the next evening for her.]', "end", forbids=("jerribeth.short_future_chosen",), flags=("jerribeth.chosen_future",)),
                    c('[Keep the shorter promise.]', "short_end", requires=("jerribeth.short_future_chosen",))])
        event["Nodes"].append(page(destination, '"You make me unpack two cases and then offer me a chair. Very well. Bring it closer."\n{n}She stays for the watch. Her collection remains shut; she wants an audience for herself.{/n}' if event is visit else
                                 '"Then we keep the room lit."\n{n}She sits beside you in the imagining while the real frame stays dark. No marks wait for you at dawn.{/n}', *answers))

    future = events["jerribeth.future"]
    tenant = node(future, "tenant_body")
    tenant["Text"] = tenant["Text"].replace('"I shall not take your hands in here unless you give them. In this house, that is the only rule I keep."',
        '"Well? I have built the room. I want you in it."')
    for id in ("tenant_morning", "tenant_morning_free"):
        old = node(future, id)
        saved = copy.deepcopy(old["Choices"])
        for answer in old["Choices"]:
            answer["Requires"].append(MIND_LOST)
        old["Choices"].append(c('[Leave the imagining together.]', "mental_return", flags=("jerribeth.mental_origin." + id,)))
        # One common continuation, with the original morning destinations.
        future["Nodes"].append(page("mental_receipt_" + id, '"The lease remains. So does the forfeit. You have paid for neither by reaching for me."', *saved))
    future["Nodes"].extend([
        page("mental_return", '''{n}The imagined bedroom narrows to a dark passage. Behind it, the shelves of memories she has collected remain lit; she has withdrawn there. You can feel your own pulse pulling at the room's edges.{/n}
{n}She comes back. Her claws open in front of you, empty.{/n}
"This way. You are tearing the walls apart. I wanted that hiding place."
{n}She leads you out of the shared room, then lets its walls fall. Her collection stays in the space she rented. The private arrangement she built around it is gone.{/n}''',
             c('[Follow her out.]', "mental_after", flags=(MIND_LOST,)),
             c('"I can wake myself. Stay until I do."', "mental_after", flags=(MIND_LOST,))),
        page("mental_after", '"I could have stayed on my side. You would have woken eventually."\n{n}She is quiet behind your left eye. Then the buzzing returns.{/n}\n"Do not make me explain why I came back. Invite me again. I prefer questions I can charge for."',
             *(c("Continue", "mental_receipt_" + id, requires=("jerribeth.mental_origin." + id,)) for id in ("tenant_morning", "tenant_morning_free"))),
    ])
    shelves = node(future, "mental_after")
    shelves["Text"] += '\n{n}Two shelves take shape in her rented space: the memories she keeps for herself, and an empty space facing your imagined chair.{/n}\n"The things I kept. The things I want near you. I have not given up either."'
    answers = copy.deepcopy(shelves["Choices"])
    shelves["Choices"].extend((
        c('"Tell me plainly why you came back."', "mental_plain"),
        c('"Keep the affair we promised. Nothing more."', "mental_affair", requires=("jerribeth.short_future_chosen",))))
    future["Nodes"].extend((
        page("mental_plain", '"Because I wanted you in it. I could have shut the door. I did not."\n{n}The shelves remain on her side of the lease. Her voice comes closer.{/n}\n"That answer belongs to you. My collection does not."', *copy.deepcopy(answers)),
        page("mental_affair", '"The evenings, then. I heard you. I have quite enough shelf space without furnishing it with promises you did not make."\n{n}She leaves the imagined chair where she put it.{/n}', *copy.deepcopy(answers)),
    ))
    # Distinctive payoff is remembered only after her actual chosen return.
    for event in events.values():
        if event["Owner"].endswith("Epilogue") and event["Id"] != "jerribeth.ending_aeon":
            for item in event["Nodes"]:
                if all(a.get("Next") is None for a in item["Choices"]):
                    item.setdefault("Paragraphs", []).extend((
                        p('{n}Her collection survived the Drezen rendezvous. The hiding place did not. She had left with everything she meant to keep, then come back for the Commander. She still complained about the lost room whenever she opened a case.{/n}', requires=(LOST,)),
                        p('{n}The tenant kept her collected memories in the space she rented. The room she had built around them was gone: she had come back into the collapsing imagining to lead the Commander out. She demanded a better room the next time.{/n}', requires=(MIND_LOST,)),
                        p('{n}The scale remained beside the frame. She returned to collect the hours owed for keeping it, and spoke through the next watch, possessive and awake. The forfeit she would take some other time, in some other way.{/n}', requires=(SCALE, SCALE_PAID), forbids=(SCALE_BACK,)),
                        p('{n}The scale was returned. Jerribeth never again charged an hour for it. She found other reasons to claim an evening.{/n}', requires=(SCALE_BACK,)),
                    ))
                    if event["Id"] == "jerribeth.ending_sacrifice":
                        # A remembered price is not a posthumous visit to a
                        # living Commander. Keep this ending wholly historical.
                        item["Paragraphs"][-3]["Text"] = '{n}The tenant had given up her private arrangement to lead the Commander out of their imagining. She never rebuilt that shared room. There was no Commander left to invite into it.{/n}'
                        item["Paragraphs"][-2]["Text"] = '{n}The scale had bought her an hour before the last march. After the Commander\'s death it lay beside the dark frame; there were no further hours to collect.{/n}'
                        item["Paragraphs"][-1]["Text"] = '{n}The scale had been returned before the last march. They were square, which she had found so disappointing. She could claim no further evening from the dead.{/n}'
    late = events["jerribeth.trickster.epilogue.commit"]
    for paragraph in node(late, "offer")["Paragraphs"]:
        paragraph["Text"] = paragraph["Text"].replace(
            "He sat down at the Commander's table without being asked, and her voice came out of him, high and pleased.",
            "The borrowed body sat at the table without being asked; her voice rose from its throat, high and pleased.")
    node(late, "night_after")["Text"] = node(late, "night_after")["Text"].replace("Rent received.", "Evening received.")
    for event, id in ((future, "tenant_morning"), (late, "night_mind_after")):
        item = node(event, id)
        item["Text"] = item["Text"].replace("Rent received.", "The evening was mine. Rent follows the lease.")
    node(late, "torn")["Text"] = '''{n}The Commander kept both hands folded on the table. Jerribeth waited, then shut the smaller case.{/n}
"No forfeit, no promise. I heard you."
{n}She took her cases away. Once she returned for a specimen left beneath the table; she found it herself, without sitting down. The Commander kept the war, including the parts worth losing. There was no promise for her to collect, and she never let the Commander forget it.{/n}'''
    node(late, "torn_mind")["Text"] = '''{n}The Commander finished the tea without answering. The voice behind the left eye thinned.{/n}
"No forfeit, no promise. Only the lease. You pay that already."
{n}She withdrew to the space she had rented. Later she returned to complain about the rent; she did not call it a lover's invitation. The Commander kept the war. She had nothing new to collect, and she said so on the first of every month.{/n}'''
    for item in late["Nodes"]:
        for paragraph in item.get("Paragraphs", ()):
            if paragraph["Text"] == '{n}Nothing about Marhevok was ever settled between them. Jerribeth preferred it that way: an open question is a hook, and she liked the Commander hooked.{/n}':
                paragraph["Text"] = "{n}Marhevok's name stayed between them like a pin left in a cushion. Neither the war nor the Commander's answer ever drew it out, and she never tried.{/n}"
    # Exposure has a consequence in her next on-page invitation, not a claim
    # that a single sentence saying 'not forgiven' settles the broken bargain.
    for event in (visit, future, late):
        resume = node(event, "partner_discovery_resume")
        resume["Text"] = '''{n}She leaves the frame open. Her hands stay on her side of it.{/n}
"You have heard what I kept, or what I lost. You are still here. How troublesome of you."
{n}She leaves her hands at her sides.{/n}
"Come closer, or keep the table between us. I am tired of watching you hover."'''


def late_debts(event):
    # Each incoming signature gets ending-local pay/refuse paths. No payment,
    # partner stance or collection is persisted from an epilogue choice.
    for old in list(event["Nodes"]):
        for index, answer in enumerate(list(old["Choices"])):
            if answer.get("Next") not in ("signed", "signed_mind"):
                continue
            target = answer["Next"]
            id = "late_interest_" + old["Id"] + "_" + str(index)
            twin = copy.deepcopy(answer)
            twin["Next"] = id
            twin["Requires"].append(GRUDGE)
            twin["Forbids"].append(PAID)
            answer["Forbids"].append(GRUDGE)
            paid = copy.deepcopy(answer)
            paid["Forbids"] = [f for f in paid["Forbids"] if f != GRUDGE]
            paid["Requires"].extend((GRUDGE, PAID))
            old["Choices"].extend((paid, twin))
            event["Nodes"].append(page(id, '"First, the toast you drank for free. Every cup before mine. I told you there would be interest. The forfeit buys something else."',
                c('[Pay the interest, then answer her offer.]', id + "_paid"),
                c('[Refuse. Keep your memories, and keep your hand.]', "torn_mind" if target == "signed_mind" else "torn")))
            event["Nodes"].append(page(id + "_paid", '{n}The remembered cups empty. The faces across them vanish. One evening remains, the one when her voice first answered your toast.{/n}\n"Interest received. Now show me your hand. I still choose whether to take it."', c("Continue", target)))


def localize_late_choices(event):
    """Compile existing partner decisions into ending-local destinations.

    Local Set receipts guide the dialogue while it is being authored, and are
    never persisted. Original nodes/answer indices and terminal exits survive.
    New paths converge on those same terminal exits. This does not infer a
    prewar yes, arrival, stance or payment from a kiss or from the late offer.
    """
    # Retain every round-two generated node/answer identity. The revised graph
    # uses a new namespace; the saved late graph remains available to old saves.
    legacy = copy.deepcopy(event)
    original_count = len(legacy["Nodes"])
    for item in legacy["Nodes"]:
        for answer in item["Choices"]:
            if "jerribeth.partner.exclusive_memory_owed" in answer["Set"]:
                answer["Set"] = [f for f in answer["Set"] if f != "jerribeth.partner.exclusive_memory_owed"]
                answer["Set"].extend(("jerribeth.trickster.forfeit_named", "jerribeth.trickster.cost.forfeit"))
    _legacy_localize_late_choices(legacy)
    retained = legacy["Nodes"][original_count:]
    originals = {item["Id"]: copy.deepcopy(item) for item in event["Nodes"]}
    local = {f for item in originals.values() for a in item["Choices"] for f in a["Set"]}
    # Include the slot staging receipts in the compiler: they are local flow,
    # never evidence of a campaign visit or an earlier physical encounter.
    local |= {f for item in originals.values() for a in item["Choices"]
              for f in a["Requires"] if f.startswith("jerribeth.slot_seen.")}
    from storylines import jerribeth_partner as partner
    terms = {partner.SHARE, partner.EXCLUSIVE, partner.SECRET, partner.READY,
             partner.CHOSEN, partner.REFUSED, partner.CAREFUL}
    clones, cache = [], {}

    def resolved(record, state):
        # Campaign arrangements stay live until this graph selects new terms.
        decided = local if partner.READY in state or partner.REFUSED in state else local - terms
        remembered = {partner.EXPOSED, 'jerribeth.partner_exposure.plant',
                      'jerribeth.partner_exposure.chief', 'jerribeth.partner.exclusive_memory_owed'}
        decided = decided - (remembered - state)
        if any(f in decided and f not in state for f in record.get("Requires", ())):
            return None
        if any(f in state for f in record.get("Forbids", ()) if f in decided):
            return None
        out = copy.deepcopy(record)
        for key in ("Requires", "Forbids"):
            out[key] = [f for f in out.get(key, ()) if f not in decided]
        return out

    def visit(id, state):
        original = originals[id]
        if all(a.get("Next") is None for a in original["Choices"]):
            if any(a["Set"] for a in original["Choices"]):
                key = (id, state)
                if key not in cache:
                    label = "job3_local_exit_" + id + "_" + hashlib.sha256("|".join(sorted(state)).encode()).hexdigest()[:10]
                    cache[key] = label
                    notes = [out for para in partner.partner_paragraphs(closed=True)
                             if (out := resolved(para, state))]
                    conclusion = (
                        '{n}After Threshold the Commander gave her the hand, then closed the frame and left her. She kept the promise and the war it would cost. There were no more evenings. She did not ask twice.{/n}'
                        if "__signature" in state else
                        '{n}After Threshold the Commander closed the frame without giving her a hand. She kept what was already owed and took it when it suited her. There were no more evenings.{/n}')
                    notes.append(p(conclusion, requires=("lastcall.active",)))
                    clones.append(n(label, original["Speaker"], original["Text"],
                                    c(), portrait="Jerribeth", paragraphs=notes))
                return cache[key]
            # The original ending exit is the actual exit, with unchanged
            # identity and mechanics. Only newly selected partner aftermath is
            # placed on the preceding page.
            notes = [resolved(para, state) for para in original.get("Paragraphs", ())]
            notes = [para for para in notes if para]
            signed = "__signature" in state
            private = "__private" in state
            if not signed:
                for para in notes:
                    para['Text'] = para['Text'].replace(
                        'She kept the Commander alone as her lover, and the promised memory as her price.',
                        'The promised memory was the price of severing Marhevok\'s claim. The Commander never gave her a hand for the rest, and she took no new lover on credit.')
            if id == 'collected' and not signed:
                key = (id, state)
                if key not in cache:
                    label = 'job3_local_unsigned_' + hashlib.sha256('|'.join(sorted(state)).encode()).hexdigest()[:10]
                    cache[key] = label
                    notes.append(p('{n}After Threshold the lease ran on. Nobody had given her the war, so she did not take it; she took her rent instead, and complained about the difference.{/n}', requires=('lastcall.active',)))
                    clones.append(n(label, 'Narrator', '{n}She closed the frame when the evening ended. The Commander kept the memory of the war.{/n}', c(), portrait='Jerribeth', paragraphs=notes))
                return cache[key]
            aftermath = (
                '{n}After Threshold Jerribeth kept the pin beside the frame, with the Commander\'s blood dried on its point. The war fell due on that promise. Any memory still owed for Marhevok she meant to take separately, on a worse day.{/n}'
                if signed else
                '{n}The last call of the war left the tenant\'s lease intact. The Commander promised her nothing new and gave her no war to take. Their private evening ended in talk, which she pretended to find tedious.{/n}' if private else
                '{n}After Threshold the Commander\'s hand stayed in their lap. Jerribeth took what she was already owed and claimed nothing more. She never forgave the lap.{/n}')
            notes.append(p(aftermath, requires=("lastcall.active",)))
            key = (id, state)
            if key in cache:
                return cache[key]
            label = "job3_local_" + id + "_" + hashlib.sha256("|".join(sorted(state)).encode()).hexdigest()[:10]
            cache[key] = label
            clones.append(n(label, original['Speaker'], original['Text'],
                            c("Continue", id), portrait="Jerribeth", paragraphs=notes))
            return label
        key = (id, state)
        if key in cache:
            return cache[key]
        label = "job3_local_" + id + "_" + hashlib.sha256("|".join(sorted(state)).encode()).hexdigest()[:10]
        cache[key] = label
        item = copy.deepcopy(original)
        item["Id"] = label
        item["Choices"] = []
        item["Paragraphs"] = [out for para in item.get("Paragraphs", ()) if (out := resolved(para, state))]
        # Partner summaries belong to the selected terminal, not each step.
        summaries = {block['Text'] for block in partner.partner_paragraphs()}
        for block in item["Paragraphs"]:
            if block['Text'] in summaries:
                block.setdefault('Forbids', []).append('trickster.ever')
        clones.append(item)
        for answer in original["Choices"]:
            out = resolved(answer, state)
            if out is None:
                continue
            next_state = state | frozenset(answer["Set"])
            if answer.get("Next") in ("signed", "signed_mind"):
                next_state |= {"__signature"}
            if answer.get("Next", "").startswith("partner_private_"):
                next_state |= {"__private"}
            out["Set"] = []
            if out.get("Next"):
                out["Next"] = visit(out["Next"], next_state)
            item["Choices"].append(out)
        return label

    start = node(event, "offer")
    # A new entry choice uses the same text and native-history conditions. The
    # saved offer/answers remain present; their producer effects are retired.
    local_start = visit("offer", frozenset())
    for item in event["Nodes"]:
        terminal = all(a.get("Next") is None for a in item["Choices"])
        if terminal:
            # Existing campaign receipts remain meaningful; late selections
            # have their own paragraph on the preceding page.
            # The selected arrangement is printed on its compiled predecessor.
            # Keep paragraph positions but retire their campaign-only copies;
            # this terminal still has its original exit identity and mechanics.
            for para in item.get("Paragraphs", ()):
                if any(f in local for f in para.get("Requires", ()) + para.get("Forbids", ())):
                    para.setdefault("Forbids", []).append("trickster.ever")
            continue
        for answer in item["Choices"]:
            answer["Set"] = []
            for key in ("Requires", "Forbids"):
                answer[key] = [f for f in answer[key] if f not in local]
            if item is start:
                answer["Forbids"].append("trickster.ever")
    start['Text'] = '{n}Jerribeth opened the frame. It had survived Threshold, as she had. Beside it on the table lay one of her pins, bright, point toward the Commander, waiting for a hand.{/n}'
    # The compiled offer owns the arrival. Retain the original slots dormant.
    for block in start.get('Paragraphs', ()):
        block.setdefault('Forbids', []).append('trickster.ever')
    start["Choices"].append(c('[Hear her offer.]', local_start))
    # Rules.Validate also checks structural reachability of saved pages. Keep
    # the retained graph connected by an appended, retired answer; this scene
    # requires trickster.ever, so a new run cannot enter that earlier graph.
    retained_start = node(legacy, "offer")["Choices"][-1]["Next"]
    start["Choices"].append(c('Continue', retained_start, forbids=("trickster.ever",)))
    event["Nodes"].extend(retained)
    event["Nodes"].extend(clones)


# Frozen round-two graph emitter: identity retention only; new offers enter
# the job3_local graph above. Do not reorder its output or compact its answers.
def _legacy_localize_late_choices(event):
    """Compile existing partner decisions into ending-local destinations.

    Local Set receipts guide the dialogue while it is being authored, and are
    never persisted. Original nodes/answer indices and terminal exits survive.
    New paths converge on those same terminal exits. This does not infer a
    prewar yes, arrival, stance or payment from a kiss or from the late offer.
    """
    originals = {item["Id"]: copy.deepcopy(item) for item in event["Nodes"]}
    local = {f for item in originals.values() for a in item["Choices"] for f in a["Set"]}
    # Include the slot staging receipts in the compiler: they are local flow,
    # never evidence of a campaign visit or an earlier physical encounter.
    local |= {f for item in originals.values() for a in item["Choices"]
              for f in a["Requires"] if f.startswith("jerribeth.slot_seen.")}
    clones, cache = [], {}

    def resolved(record, state):
        if any(f in local and f not in state for f in record.get("Requires", ())):
            return None
        if any(f in state for f in record.get("Forbids", ()) if f in local):
            return None
        out = copy.deepcopy(record)
        for key in ("Requires", "Forbids"):
            out[key] = [f for f in out.get(key, ()) if f not in local]
        return out

    def visit(id, state):
        original = originals[id]
        if all(a.get("Next") is None for a in original["Choices"]):
            if any(a["Set"] for a in original["Choices"]):
                key = (id, state)
                if key not in cache:
                    label = "late_local_exit_" + id
                    cache[key] = label
                    if not any(item["Id"] == label for item in clones):
                        clones.append(n(label, original["Speaker"], original["Text"],
                                        c(), portrait="Jerribeth"))
                return cache[key]
            # The original ending exit is the actual exit, with unchanged
            # identity and mechanics. Only newly selected partner aftermath is
            # placed on the preceding page.
            notes = [resolved(para, state) for para in original.get("Paragraphs", ())
                     if any(f in local for f in para.get("Requires", ()))]
            notes = [para for para in notes if para]
            if not notes:
                return id
            key = (id, state)
            if key in cache:
                return cache[key]
            label = "late_local_" + id + "_" + hashlib.sha256("|".join(sorted(state)).encode()).hexdigest()[:10]
            cache[key] = label
            clones.append(n(label, "Narrator", '{n}She kept the answer the Commander had actually given.{/n}',
                            c("Continue", id), portrait="Jerribeth", paragraphs=notes))
            return label
        key = (id, state)
        if key in cache:
            return cache[key]
        label = "late_local_" + id + "_" + hashlib.sha256("|".join(sorted(state)).encode()).hexdigest()[:10]
        cache[key] = label
        item = copy.deepcopy(original)
        item["Id"] = label
        item["Choices"] = []
        item["Paragraphs"] = [out for para in item.get("Paragraphs", ()) if (out := resolved(para, state))]
        clones.append(item)
        for answer in original["Choices"]:
            out = resolved(answer, state)
            if out is None:
                continue
            next_state = state | frozenset(answer["Set"])
            out["Set"] = []
            if out.get("Next"):
                out["Next"] = visit(out["Next"], next_state)
            item["Choices"].append(out)
        return label

    start = node(event, "offer")
    # A new entry choice uses the same text and native-history conditions. The
    # saved offer/answers remain present; their producer effects are retired.
    local_start = visit("offer", frozenset())
    for item in event["Nodes"]:
        terminal = all(a.get("Next") is None for a in item["Choices"])
        if terminal:
            # Existing campaign receipts remain meaningful; late selections
            # have their own paragraph on the preceding page.
            continue
        for answer in item["Choices"]:
            answer["Set"] = []
            for key in ("Requires", "Forbids"):
                answer[key] = [f for f in answer[key] if f not in local]
            if item is start:
                answer["Forbids"].append("trickster.ever")
    start["Choices"].append(c('[Hear her offer.]', local_start))
    event["Nodes"].extend(clones)

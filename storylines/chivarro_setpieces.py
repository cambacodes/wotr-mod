"""Authored Chivarro round-2 situations, applied after the saved stance surfaces.

The lost madam's counter-offer is the registered bargain, not a new quest.
Canon ledger: tools/route_packs/plans/chivarro-setpieces.md C1-C10.
Neither housing, passage nor a lover's absence earns her invitation.
Minagho-only encounters and shared availability/native adapters stay with their owners.
"""
import json
from copy import deepcopy
from pathlib import Path

from story_format import c, n, p

P = "minagho_chivarro.trickster."
# Single source of truth for every Minagho/Chivarro slot brief (coordinator
# ruling, slot rebuild): the minagho/ copies. The former chivarro/ mirrors are gone.
BRIEFS = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/minagho"


def _nodes(page):
    return {node["Id"]: node for node in page["Nodes"]}


def _text(nodes, key, text):
    nodes[key]["Text"] = text.strip()


def _entry(page):
    nodes = _nodes(page)
    # Keep both passage answers, their alignment shift and their separate debts.
    for key in ("silk", "cellar", "fought"):
        for answer in nodes[key]["Choices"][:2]:
            answer["Text"] = '[Offer the passage] "Drezen is through here. Bring the dagger. I came to get you out."'
    _text(nodes, "press", '''{n}Chivarro tests the opening with the candle. Drezen's watch bell sounds beyond it. She turns the dagger in her hand.{/n}
"Where is Minagho? Answer before I put this through you."
{n}She listens, takes her sack, and steps past you into the press. The dagger stays in her hand. On the other side she turns it toward your bedroom door.{/n}
"A crusader's bedroom. You have a remarkable talent for making an escape look like an insult."''')
    for key in ("which", "which_debt"):
        for answer in nodes[key]["Choices"]:
            if P + "chivarro_sent_back" in answer["Set"]:
                answer["Next"] = "departure_answer" if "departure_answer" in nodes else "chivarro_leaves"
    page["Nodes"].append(n("chivarro_leaves", "Chivarro", '''{n}Chivarro takes her sack. Minagho rises from the bed and catches her wrist.{/n}
"Let go. I will find a room without this idiot in it."
"Send me the address," {n}Minagho says. She kisses Chivarro's knuckles before releasing her.{/n} "And keep the dagger."
{n}Chivarro leaves by the stairs. Minagho turns on you.{/n} "You threw her out of your room, Golarian. Not out of my life."''', c()))
    if "departure_answer" in nodes:
        nodes["departure_answer"]["Text"] = '''"Your room, honey. Keep it," {n}Chivarro says.{/n}
"You sent her away from you. Not from me. I will see her where she chooses. Do not start celebrating," {n}Minagho adds.{/n}'''
        nodes["departure_answer"]["Choices"][0]["Next"] = "chivarro_leaves"
        page["Nodes"][-1]["Text"] = page["Nodes"][-1]["Text"].replace(
            ' Minagho turns on you.{/n} "You threw her out of your room, Golarian. Not out of my life."', '{/n}')


def _business(page):
    nodes = _nodes(page)
    for key in ("start", "receipt"):
        nodes[key]["Text"] += '''
"The sum she wrote. One evening. All six hands flat on the cloth," {n}Chivarro writes.{/n} "I shall choose what we discuss. Herrax can keep the customers who like a chain with their supper. She does not get the ones who came to hear me."
{n}Minagho adds:{/n} "One hand moves, she eats with five."
{n}Chivarro has crossed out the buyer's claim to further visits. The corrected offer waits for your reply.{/n}'''


def _rebuke(page):
    nodes = _nodes(page)
    if page["Id"].endswith("_letter"):
        # The answer keeps its index. The same receipts are earned only after
        # the meeting's paying action, rather than by sending a palm print.
        _text(nodes, "start", '''{n}Chivarro has written across the quartermaster's inventory: "Come to the stores at watch change. Bring the hand. Minagho will be there."
You find them at Wilcer's counter. Chivarro moves his tally board aside; he snatches it back before she can spill anything on it.{/n}
"You carry the Goat's debt for her. Now I want to hear what you think that entitles you to. Your hand, honey. Open on the table until I have finished."
{n}She tells you what she thinks of the escape, your cleverness, and the room you expected her to be pleased with. Minagho adds two insults and disputes a third. Wilcer slams a crate down beside them.{/n}
"This counter is for stores. Take your quarrel outside when you're done."
{n}Chivarro holds out her hand for yours.{/n}''')
        nodes["start"]["Choices"][0]["Text"] = "[Keep your palm open through her verdict; let her close it herself.]"
        # Final paying action belongs on the answer's reached page, not in ink.
        nodes["start"]["Choices"][0]["Next"] = "verdict_paid"
        paid = tuple(nodes["start"]["Choices"][0]["Set"])
        nodes["start"]["Choices"][0]["Set"] = []
        page["Nodes"].append(n("verdict_paid", "Chivarro", '''{n}The old cut opens on the table. You keep the hand there while she finishes. Then Chivarro closes your fingers herself, one at a time.{/n}
"There. Next time you come to ask me something, leave the runner at home."
{n}She takes Minagho's arm and leaves the counter to Wilcer.{/n}''', c(flags=paid)))
        if "reckoning_receipt" in nodes:
            # Both round-two accounts belong to the same meeting. Her lover
            # answers before Chivarro closes the hand and awards the receipt.
            nodes["start"]["Choices"][0]["Next"] = "reckoning_receipt"
            nodes["reckoning_receipt"]["Text"] = '''{n}Minagho takes your wrist. She presses her thumb into the cut until your fingers jerk.{/n}
"Kenabres. Drezen. His cells. Every bastard with a claim wanted me kneeling. You have put your hand on the table instead."
"It stays there until I finish," {n}Chivarro says.{/n}
{n}Minagho leaves it open for her.{/n}
"Tonight you answer to me, Golarian. Ask properly."'''
            nodes["reckoning_receipt"]["Choices"][0]["Next"] = "verdict_paid"
    else:
        nodes["start"]["Text"] = nodes["start"]["Text"].replace(
            "Minagho says you own her debt. Then you and I will discuss the price of her.",
            "You carry the Goat's debt for her. Now you and I will discuss what you think that buys.")
        _text(nodes, "verdict", '''{n}Chivarro pushes a clean board beneath your hand. Wilcer takes his ledger out of reach.{/n}
"Better crusaders than you have offered me a room. Richer fools have offered me a house. None of them got to speak for Minagho."
{n}She takes her time over the escape, your invitation, and everything she dislikes about your city. Minagho disputes Chivarro's account of the rescue, then supplies an insult she missed. The old cut opens. You keep the hand flat.{/n}
"Finished?" {n}Wilcer drops a crate at your feet.{/n} "Then let me issue the damned stores."
{n}Chivarro closes your fingers herself.{/n} "Now come and ask me properly."''')


def _invitation(page):
    nodes = _nodes(page)
    if page["Id"] == P + "after.before_the_last_road":
        _text(nodes, "start", '''{n}Three purses lie on Wilcer's counter. Chivarro draws hers toward her; Minagho claims that all three once belonged to the same idiot.{/n}
"Two," {n}Chivarro says.{/n} "The third was mine before you began improving the story."
"And who distracted him?" {n}Minagho asks.{/n}
"The woman who kept the money," {n}Chivarro says.{/n}
{n}Wilcer pushes a requisition between the purses.{/n} "If you mean to rob one another, do it somewhere I can get at the arrowheads."
{n}Chivarro pockets the surplus, laughs at Minagho, and catches your sleeve as you turn to go.{/n}
"Your war can have the morning, honey. What were you going to ask us tonight?"''')
        _text(nodes, "threshold", '''{n}Chivarro takes your hand and leads you down from the stores to her rented room above the chandler. Minagho follows, carrying the lamp and arguing about who really stole the third purse. Chivarro shuts her up with a kiss, then turns to you.{/n}
"The money stays there." {n}She puts the purse on a shelf and drops your sword belt beside the bed.{/n} "Come here."
{n}Minagho opens your collar. Chivarro takes your hand from the fastening and puts it at her waist; she undoes her gown herself. Minagho draws her close, kisses her bare shoulder, then reaches for you.{/n}
"I am staying," {n}Minagho says.{/n} "Put the lamp down, Chivarro."
{n}Chivarro draws both of you toward her bed.{/n}''')
    elif page["Id"] == P + "after.before_the_last_road_letter":
        _text(nodes, "came", '''{n}The answer comes back with Chivarro's address and an hour. At the chandler's stair she opens the door herself. Minagho has the lamp.{/n}
"You found the front door, honey. I owe her a copper."
{n}Chivarro takes the answered letter from you, reads it, and drops it into the grate.{/n} "The house stays ours. This evening, too."
{n}She puts the purse aside and catches your collar. Minagho kisses Chivarro over your shoulder, then turns your face toward hers. Chivarro drops your belt beside the bed and opens her own gown.{/n}
"I did not bring you here to watch me count." {n}She takes your hand and draws you down with them.{/n}''')
        _text(nodes, "morning", '''{n}A cart rattles beneath the chandler's window. Chivarro drags the cover over all three of you; Minagho pulls it back to bind your hand.{/n}
"You told her you meant to come back?" {n}Chivarro asks you.{/n} "Before you told me?"
"I answered for myself," {n}Minagho says. Chivarro catches your chin.{/n}
"Then let me hear yours, honey. In my bed," {n}Chivarro says.{/n}
{n}She listens, steals one coin from the abandoned purse and kisses you before you can object. Minagho keeps the bandage tight. Chivarro's fingers stay on your collar.{/n}
"Knock next time. Even when she tells you not to."''')
    elif page["Id"] == P + "alone.chivarro":
        _text(nodes, "start", '''{n}Chivarro has spread the rent money across Wilcer's counter. He pushes it back into a purse with the edge of his tally board.{/n}
"Take it upstairs. I've got a garrison to feed."
"So have I, honey. Mine pays better."
{n}She pockets the surplus and steps into your way.{/n} "I have a room below the citadel. I have a bed I chose myself. Minagho's place stays hers. What do you want?"''')
        for key in ("threshold", "threshold_clean"):
            # Preserve the earned hand distinction, remove the sex-as-rent claim.
            nodes[key]["Text"] = nodes[key]["Text"].replace(
                '"Rent,"', '"Your hand,"').replace(
                '"This one is mine, and I am going to collect every copper of it."',
                '"Tonight I want you. Put the damned purse away."').replace(
                '"A room of my own, in a crusader\'s city, and a tenant who pays,"',
                '"A room of my own, and you in it,"').replace(
                '"I have come down in the world. Let us see how far."',
                '"Come closer. I have finished admiring the room."')
    elif page["Id"] == P + "alone.chivarro_letter":
        _text(nodes, "came", '''{n}You go to the address she sent. Chivarro opens the door above the chandler herself. The lease lies folded on the shelf; she sets your purse beside it.{/n}
"That pays for the room. Now look at me."
{n}She takes your collar, loosens it, and draws you close. Her gown slides from her shoulders; she catches your mouth before you can look down. You pull her against you. Chivarro laughs into the kiss and takes you back toward her bed.{/n}
"This evening is mine, honey. I am tired of hearing about everyone else's."''')
        _text(nodes, "morning", '''{n}The watch passes beneath the window. Chivarro has your shirt under her head and no intention of giving it back.{/n}
"Tell them you have been robbed. It will save an explanation."
{n}Beside the bed she has left a receipt for the room's rent. You put the hundred coins down. She reaches past them, catches your wrist, and pulls you back for a kiss.{/n}
"The room will still be here when your war is done. Remember the stair."''')
        nodes["morning"]["Choices"][0]["Crusade"] = {"Resource": "Finances", "Amount": -100}
    elif page["Id"] == P + "alone.chivarro_when_it_scars":
        _text(nodes, "start", '''{n}Five days have passed without a letter or a knock. A runner waits beside a purse on your desk: the year's rent, counted out. Chivarro's address above the chandler lies beneath it. The purse has not left your hand.{/n}''')
        nodes["chv"]["Text"] = '{n}You send the runner. He returns with the purse intact and a message he has learned by heart.{/n}\n' + nodes["chv"]["Text"].split('{/n}', 1)[1].strip()
        nodes["chv"]["Choices"][1]["Crusade"] = {"Resource": "Finances", "Amount": 200}
        _text(nodes, "night", '''{n}Chivarro hears your question before taking the purse. She names the house, her own keys, and Minagho's place, and waits for your reply. Only then does she count the rent and set it aside.{/n}
"Now come here. I sent the runner away so I could have you to myself."
{n}She pulls you down by the collar, kisses you, and lets her gown slip from her shoulders. Your hands catch her waist. She pushes you back onto her bed and follows.{/n}''')


def _mornings(page):
    nodes = _nodes(page)
    if page["Id"] == P + "after.the_morning_after":
        _text(nodes, "start", '''{n}Chivarro arrives at the stores wearing Minagho's cloak. Your shirt is still in her room. She takes your arm before Wilcer can hand you a dispatch.{/n}
"You told Minagho you meant to come back. Then I heard it from her. Why was I the last to know about my own evening?"
"I spoke for myself," {n}Minagho says, still sharpening her dagger. Chivarro tips your face toward hers.{/n}
"Then you can speak to me. And fetch your shirt before someone mistakes it for a souvenir."
{n}She interrupts you with a kiss. Wilcer slaps the dispatch against your shoulder.{/n} "When you're finished. The garrison isn't."''')
        nodes["minagho"]["Text"] = nodes["minagho"]["Text"].replace(
            "I will hear it every dawn now, lying next to you, because of me.",
            "When we spend a night together, I will hear it at dawn. Because of me.")
        nodes["terms"]["Text"] += '\n"Try the wardrobe and I shall charge you for the door as well," {n}Chivarro adds.{/n}'
    elif page["Id"] == P + "alone.chivarro_morning":
        _text(nodes, "start", '''{n}At watch change Chivarro catches you outside Wilcer's stores. She is wearing yesterday's gown; its missing pin is in your pocket. She takes it back and fastens it without haste.{/n}
"You left this beside the bed. I nearly had to come out wearing your shirt."
{n}She reaches into your purse for the rent.{/n} "A hundred for the room. Stop looking so pleased, honey. I chose what happened in it."
{n}She keeps one coin between her fingers while you count the rest.{/n} "Come back when you have something better than dispatches to bring me."''')
        _text(nodes, "haggle", '''{n}She lets you take the coin. Then she catches your wrist, closes your hand around it and pulls you into a kiss, in full view of the stores.{/n}
"Keep it. If I find it on another woman's table, I shall know where to send the knife."''')


def _secret(page):
    # Only Chivarro's secret and the pair's confrontation, not Minagho's solo turn.
    if ".alone.minagho" in page["Id"]:
        return
    service_targets = {answer["Next"] for node in page["Nodes"] for answer in node["Choices"]
                       if "minachiv.future_chivarro_service" in answer["Set"]}
    for node in page["Nodes"]:
        key = node["Id"]
        if key in service_targets:
            continue
        if "_night_chivarro" in key or key in {"late_secret_chivarro", "late_waiting_secret"}:
            # Keep existing branch exits, effects and actual arrival guards.
            node["Text"] = '''{n}Chivarro puts your purse on the shelf and writes a line in her private account. She folds its copy and slips it inside your belt. When you lean to read the book she closes it against your fingers.{/n}
"A consultation, honey. You may tell Minagho how long it took if you feel brave."
{n}She loosens your collar and draws you into a kiss. A footstep creaks on the stair. Chivarro stills, one hand on your mouth, until the watch passes.{/n}
"That pause goes on your bill."
{n}She laughs, opens her gown and catches your hands at her bare waist. You pull her close. She draws you back toward the bed, leaving the closed account on the shelf.{/n}'''
        elif key.startswith("stance_discovery") and "letter" not in key and any(
                a["Next"] == key + "_minagho" for a in node["Choices"]):
            # Either lover's secret can reach this entry. Specific evidence is
            # read below by the woman whose own branch supplied it.
            node["Text"] = ('{n}The arriving woman stops beside her lover. You reach for your belt. She puts her hand on it first and turns toward the woman who has been keeping your company.{/n}'
                            if "return" in key else
                            '{n}The other woman enters before you can put your clothes in order. Her lover is still beside you. She takes the belt from your hand and waits for an explanation.{/n}')
        elif key.startswith("stance_discovery") and key.endswith("_minagho") and "letter" not in key:
            node["Text"] = '''{n}Minagho unfolds the private receipt tucked inside your belt and lays it beside Chivarro's purse. She taps the entry beneath the rent.{/n} "Read that one aloud, Chivarro."
"You can read, honey."
{n}Minagho puts the receipt down, draws a dagger and pins your belt to the door.{/n}
"Chivarro. Tell this idiot whose key that is. Before I cut something that bleeds."
{n}She holds out her free hand for Chivarro's.{/n}'''
        elif key.startswith("stance_discovery") and key.endswith("_chivarro_answers") and "letter" not in key:
            node["Text"] = '''"I liked having something you did not know."
{n}Chivarro takes Minagho's hand, then retrieves your belt from the door and presses it into yours.{/n}
"I wanted the night, honey. I had it. Now I choose her. Get dressed."
{n}Minagho keeps the key. Chivarro opens the door for you herself.{/n}'''
        elif key == "late_secret_chivarro_dawn":
            node["Text"] = '''{n}Minagho lays the private receipt on Chivarro's purse. She reads the entry aloud, then drives her dagger through your discarded belt into the door.{/n}
"Enjoyed the consultation, Chivarro?"
"Very much."
{n}Chivarro takes Minagho's hand, then throws your shirt to you.{/n} "And I choose her, honey. Get dressed."
{n}Minagho keeps the key. No further invitation came. The two women kept their house and each other.{/n}'''


def _continuation(page):
    nodes = _nodes(page)
    if page["Id"] == "minachiv.two_answers":
        # Neutral local wording fits both the native journey and an earned reunion.
        nodes["start"]["Text"] = nodes["start"]["Text"].replace(
            "She has answered. We have arranged how she will reach me. Separately, and with rather more caution than my little drawing suggests.",
            "She has answered. She chose the hour; I chose this room. She will inspect both exits before she lets you sit down.")
    elif page["Id"] == "minachiv.her_own_arrival":
        nodes["start"]["Text"] = nodes["start"]["Text"].replace(
            "She has reached Drezen under a mortal guise and discarded it here, after checking the room herself.",
            "She has checked the room herself and hung her cloak by the exit she intends to use.").replace(
            "Commander. I chose the road here. She chose the room.", "Commander. I chose to come. She chose the room.")
        nodes["account"]["Text"] = nodes["account"]["Text"].replace(
            "I paid my own passage. Do not waste the evening trying to collect gratitude.",
            "I came to conduct my own business. Do not waste the evening trying to collect gratitude.")
    elif page["Id"] == "minachiv.the_unhired_evening":
        _text(nodes, "want", '''"I want that tray out of my way."
{n}Chivarro pushes it aside. Minagho catches her wrist and kisses the inside of it.{/n}
"You could have said so."
"While you were improving the story of the purse you stole? I would still be waiting," {n}Chivarro says.{/n}
{n}Chivarro takes Minagho's chin and kisses her, hard enough to stop the answer. Then she turns toward you, one hand still at Minagho's throat.{/n}
"We have finished the business. Are you staying?"''')
        # Invitations are renewed here; no second "first night" after the chain.
        for key in ("chivarro_kiss", "together_kiss"):
            nodes[key]["Text"] = nodes[key]["Text"].replace(
                "This one is mine.", "Tonight is mine.")
        _text(nodes, "together", '''{n}Chivarro catches your hand before Minagho can reach it.{/n}
"You have been watching my mouth since the game began. Come and give it something to do."
"Greedy," {n}Minagho says, moving beside her.{/n}
"You took the plum."
{n}Minagho kisses Chivarro's bare shoulder, then draws your other hand into her lap. Chivarro loosens the fastening at her throat and turns toward you.{/n}
"Stay, honey. She will complain all night if you leave now."
"I shall complain anyway," {n}Minagho says, catching Chivarro's chin.{/n} "But stay."''')
    elif page["Id"] == "minachiv.a_room_she_likes":
        _text(nodes, "choose", '''"The door closes. The window opens. No one opposite can watch unless I put a ladder out for them."
{n}Chivarro takes two cups from the shelf.{/n} "Minagho wanted to move everything here. I told her she could bring herself. The rest could wait downstairs."
{n}She pours the tea and gives you the cup with the sound handle.{/n} "She complained about the wall. I kissed her until she forgot it. She will be back to finish the complaint."
{n}Chivarro catches your sleeve before you sit.{/n} "Look at the room first, honey. I did not bring you here to admire the teapot."''')
        _text(nodes, "notice", '''{n}Chivarro takes two pins from the ornament box and holds them against the dark cloth above the couch.{/n}
"That one makes the room look pious. Disgusting."
{n}She drops it back into the box, keeps the darker pin and catches you watching her.{/n} "You may object. I shall enjoy hearing how you intend to improve it."
{n}Outside, a cart carries broken spear shafts toward the stores. Chivarro shuts the window.{/n} "Your soldiers have had the street all day. I want the room."''')
        _text(nodes, "close", '''{n}Chivarro pulls you down beside her. One cushion slips; she kicks it to the floor and takes the space it leaves.{/n}
"Finally. I was beginning to think you had come to inspect the furniture."
{n}You kiss her. She catches your collar and holds you there, then loosens it enough to put her hand inside.{/n} "Stay. The rehearsals can go badly without me for one evening."''')
    elif page["Id"] == "minachiv.after_the_last_lamp":
        nodes["start"]["Text"] = nodes["start"]["Text"].replace(
            "She is tired.", "She wears a dressing robe. She is tired.")
        nodes["night"]["Text"] = nodes["night"]["Text"].replace(
            "Now. The part I have not rehearsed.", "Now. Come closer.")
    elif page["Id"] == "minachiv.the_paper_she_kept":
        # The accusation belongs to the player. Keep the old principled exit,
        # append the audit's pragmatic and complicit answers without new flags.
        _text(nodes, "fear", '''{n}Minagho tests the glove's crooked seam between her fingers.{/n}
"They will remember the threat. They brought the packet out of the room, didn't they? The buyer's false name comes off the bill."
{n}She puts the needle down beside the copied names.{/n} "If someone writes a true account next time, I shall still want it gone. Tell me now whether you intend to hold the door or stand in it."
{n}The needle remains on the table. She waits for your answer.{/n}''')
        nodes["fear"]["Choices"][0]["Text"] = '"I will not help you frighten a true account out of existence."'
        nodes["fear"]["Choices"].extend([
            c('"Threaten the liar. A true account gives us something we can use."', "fear_pragmatic"),
            c('"If it brings your enemies to the door, I will help you bury it."', "fear_complicit"),
        ])
        page["Nodes"].extend([
            n("fear_pragmatic", "Minagho", '''{n}Minagho turns the copied list toward you.{/n} "Then find me something useful in this before you ask me to keep it. I have already paid for one correction. I will not pay twice to amuse a stranger."
{n}She takes up the needle and points at the lamp.{/n} "Closer, Golarian. I want to see what you find."''', c(next="door"), portrait="Minagho"),
            n("fear_complicit", "Minagho", '''"You would hold the door for that?"
{n}Minagho bares her teeth, pleased, then puts the copied names inside her coat.{/n} "Good. But I keep this one. You don't get to burn it for me and decide afterward what you saved me from."
{n}She draws the lamp between you and takes up her glove again.{/n}''', c(next="door"), portrait="Minagho"),
        ])
    elif page["Id"] == "minachiv.the_cost_in_daylight":
        # CHI-03 uses the existing after-lamps-close receipt, not guessed intimacy.
        node = nodes["start"]
        old = deepcopy(node["Choices"])
        for answer in node["Choices"]:
            answer["Forbids"].append("minachiv.after_lamps_close")
        node["Choices"].append(c('"Before the accounts — last night."', "chivarro_daylight", requires=("minachiv.after_lamps_close",)))
        page["Nodes"].append(n("chivarro_daylight", "Chivarro", '''"Minagho says you mean to come back. You told her before you told me."
{n}Chivarro pushes the account aside.{/n} "I brought you into my room, honey. Why am I hearing your answer from her?"
{n}Minagho leans in from the doorway.{/n} "I asked what I wanted to know. I didn't answer for you."
"Then you can stop listening at my door."
{n}Minagho laughs and leaves. Chivarro catches your sleeve before you can follow.{/n} "Stay. I have not finished with you."''', *old))


def _returns(page):
    nodes = _nodes(page)
    if page["Id"] == P + "epilogue.pair":
        _text(nodes, "end", '''{n}Minagho and Chivarro kept their house below Drezen's citadel, their names, and the cellar no guest was allowed to inspect. Their invitations came once a year, in two hands.
The Commander returned by the front door. Chivarro opened it herself and held her guest on the step while Minagho retrieved a knife from the couch. Their argument concerned a former customer who had mistaken a year of silence for a forgiven debt. Chivarro finished it before admitting the Commander.
She took the sword belt, dropped it beside the door, and drew her guest toward the room she had chosen. Minagho left the knife where all three could reach it.{/n}''')
    elif page["Id"] == P + "epilogue.chivarro":
        _text(nodes, "end", '''{n}Chivarro kept her own house in Drezen. The lease bore her name; Minagho's chair remained at the table. Former customers still sent offers, and sometimes received answers they regretted opening.
When the Commander returned, Chivarro opened the door herself. She took the rent, left it on the table, and caught her guest by the collar before any talk of the war could begin. She led the way upstairs, leaving the account unfinished.
The rent rose each year. The invitation remained hers to send.{/n}''')
    elif page["Id"] == P + "epilogue.commit":
        nodes["went"]["Text"] = nodes["went"]["Text"].replace(
            "Chivarro takes the Commander's sword belt at the threshold and lets it fall.",
            "Chivarro opens the door herself. She keeps the Commander on the step while Minagho retrieves a knife from the couch, then takes the sword belt and lets it fall.")


def _lastcall_return():
    # Only this relationship's existing coda paragraphs; shared module unchanged.
    from storylines import lastcall_partners
    part = next(row for row in lastcall_partners.PARTNERS if row["rel"] == "minagho_chivarro")
    paragraphs = deepcopy(part["paragraphs"])
    for para in paragraphs:
        if para["Requires"] == ["minachiv.future_two"]:
            para["Text"] = '{n}The Commander returned to their house by the front door. Chivarro opened it, took the sword belt, and waited while Minagho cleared a knife from the couch. Their unfinished quarrel over an old customer resumed after the guest was admitted.{/n}'
        elif para["Requires"] == ["minachiv.future_chivarro"]:
            para["Text"] = '{n}The Commander returned to Chivarro\'s house. She left the rent on the table and led her guest upstairs. Minagho\'s chair remained hers; Chivarro had sold none of her lover\'s place.{/n}'
    part["paragraphs"] = tuple(paragraphs)


def _slots(page):
    # All briefs are copied for the coordinator. Minagho-only inserts are not
    # installed by Chivarro's writer. Shared/pair nights have one slot per scene.
    if ".alone.minagho" in page["Id"]:
        return
    for path in sorted(BRIEFS.glob(page["Id"] + ".explicit.*.json")):
        brief = json.loads(path.read_text(encoding="utf-8"))
        if brief.get("source", {}).get("scene", page["Id"]) != page["Id"]:
            continue
        # minagho/ briefs name one source node; older briefs listed several.
        sources = brief.get("source_nodes") or [brief["source"]["node"]]
        if all("minagho" in key for key in sources):
            continue
        nodes = _nodes(page)
        present = [nodes[key] for key in sources if key in nodes]
        if not present:
            raise ValueError("Unmatched Chivarro slot: " + brief["slot_id"])
        if brief["slot_id"] in nodes:
            # Minagho's round already installed this shared encounter from the
            # same brief, so its default text is already in place. Keep its
            # saved insert IDs and distinct discovery exits. Clean-hand
            # siblings that were not in that manifest still visit an insert.
            for source in present:
                if any(".explicit." in (a["Next"] or "") for a in source["Choices"]):
                    continue
                if page["Owner"].endswith("Epilogue"):
                    continue
                slot_id = brief["slot_id"] + "." + source["Id"]
                exits = deepcopy(source["Choices"])
                for answer in exits:
                    answer["Set"] = []
                    answer.pop("Crusade", None)
                    answer.pop("Alignment", None)
                page["Nodes"].append(n(slot_id, "Narrator", brief["default_text"], *exits))
                for answer in source["Choices"]:
                    if not answer["Abort"]:
                        answer["Next"] = slot_id
            continue
        if page["Owner"].endswith("Epilogue"):
            # Frozen ending exits keep both their continue identity and their
            # terminal mechanics. Epilogue paragraphs support inline inserts.
            for node in present:
                aftermath = ""
                for marker in ("\n\n{n}At dawn", "\n\n{n}In the morning"):
                    if marker in node["Text"]:
                        node["Text"], tail = node["Text"].split(marker, 1)
                        aftermath = marker + tail
                        break
                paragraphs = [dict(p(brief["default_text"]), Id=brief["slot_id"])]
                if aftermath:
                    paragraphs.append(dict(p(aftermath), Id=brief["slot_id"] + ".after"))
                # Existing payoff/departure contracts address paragraph ordinals.
                # New insert paragraphs append, preserving those saved readers.
                node["Paragraphs"] = node.get("Paragraphs", []) + paragraphs
            continue
        # Saved secret variants lead to distinct discovery nodes. Give each
        # distinct exit its own insert rather than adding a branch-memory flag.
        variants = {}
        for node in present:
            destinations = {answer["Next"] for answer in node["Choices"] if not answer["Abort"]}
            if len(destinations) != 1:
                # Late waiting has a distant reply and an unknown-partner exit.
                # Preserve those answers on the slot itself, in original order.
                identity = node["Id"]
            else:
                identity = next(iter(destinations))
            variants.setdefault(identity, []).append(node)
        for index, members in enumerate(variants.values()):
            if index:
                raise ValueError("Distinct saved exits need separate numbered briefs: " + brief["slot_id"])
            slot_id = brief["slot_id"]
            aftermath = ""
            node = members[0]
            for marker in ("\n\n{n}Later", "\n\n{n}Near dawn", "\n\n{n}At dawn", "\n\n{n}In the morning"):
                if marker in node["Text"]:
                    before, tail = node["Text"].split(marker, 1)
                    node["Text"] = before
                    aftermath = marker + tail
                    break
            exits = deepcopy([answer for answer in node["Choices"] if not answer["Abort"]])
            deferred_receipt = all(answer["Next"] is None for answer in exits)
            for answer in exits:
                if not deferred_receipt:
                    answer["Set"] = []
                answer.pop("Crusade", None)
                answer.pop("Alignment", None)
            # Brief scene + source_nodes specify this insert's content.
            slot = n(slot_id, "Narrator", brief["default_text"], *deepcopy(exits))
            for answer in slot["Choices"]:
                answer["Set"] = []
            page["Nodes"].append(slot)
            if deferred_receipt and not aftermath:
                aftermath = ('{n}Chivarro puts the lamp beyond the bed. Minagho keeps your hand between them.{/n}'
                             if "Minagho" in brief["speakers"].values() else
                             '{n}Chivarro leaves your belt on the floor and draws you back when the watch passes.{/n}')
            if aftermath:
                tail_id = slot_id + ".after"
                for answer in slot["Choices"]:
                    answer["Next"] = tail_id
                    if deferred_receipt:
                        answer["Set"] = []
                page["Nodes"].append(n(tail_id, "Narrator", aftermath, *exits))
            for source in members:
                for answer in source["Choices"]:
                    if not answer["Abort"]:
                        answer["Next"] = slot_id
                        if deferred_receipt:
                            # A new cut/aftermath must not award an old terminal
                            # receipt while the expanded encounter is unfinished.
                            answer["Set"] = []


def integrate(payload):
    """Rewrite only the named Chivarro/pair situations; append all new nodes."""
    for page in payload["Scenes"]:
        if page.get("Relationship") != "minagho_chivarro":
            continue
        sid = page["Id"]
        if sid.startswith("minachiv.") and not page["Owner"].endswith("Epilogue"):
            # p1: a completed Trickster arrangement must not restart the
            # continuation and append a conflicting second final arrangement.
            # COMPLETE already locks the reverse order out of Trickster commits.
            if P + "committed" not in page["Forbids"]:
                page["Forbids"].append(P + "committed")
        if sid == P + "reunion.wardrobe":
            _entry(page)
        elif sid == P + "after.what_the_offer_bought":
            _business(page)
        elif sid in {P + "after.the_price_of_her_name", P + "after.the_price_of_her_name_letter"}:
            _rebuke(page)
        _invitation(page)
        _mornings(page)
        if sid in {P + "alone.chivarro_letter", P + "alone.chivarro_morning"}:
            # Discovery pays this same morning's rent, not a free fallback.
            # The existing keepsake branch was already charged before haggle.
            for node in page["Nodes"]:
                if node["Id"] == "haggle":
                    continue
                for answer in node["Choices"]:
                    if P + "cost.morning_after" in answer["Set"]:
                        answer.setdefault("Crusade", {"Resource": "Finances", "Amount": -100})
        _secret(page)
        _continuation(page)
        _returns(page)
        if sid == P + "epilogue.pair":
            for paragraph in page["Nodes"][0].get("Paragraphs", []):
                paragraph["Text"] = paragraph["Text"].replace(
                    "and every morning one of them was there to bind it.",
                    "and on the mornings they spent together one of them bound it.")
        _slots(page)
    _lastcall_return()

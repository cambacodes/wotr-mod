"""Authored round-2 situations, applied after the legacy hosts and aftermath.

Canon anchors and slot briefs: tools/route_packs/plans/camellia-setpieces.md.
This module only touches Camellia's entries. Old nodes and answer positions
remain in place; new branches append. The engine owns death/presence epochs.
"""
import copy
import json
from pathlib import Path

from story_format import c, n, p, scene
from storylines import camellia_trickster as ct

P = ct.P
DISCLOSED = P + "mireya_disclosed"
KNOWN = P + "mireya_known"
PUBLIC = P + "bond.witness_public"
TRUTHS = P + "encounter.all.public_paid"
KNIFE_TAKEN = P + "masks.knife_taken"
SEXTON = P + "cost.sexton_paid"


def node(host, nid):
    return next(x for x in host["Nodes"] if x["Id"] == nid)


def text(host, nid, body):
    node(host, nid)["Text"] = body.strip()


def add(host, nid, body, *answers, speaker="Camellia"):
    host["Nodes"].append(n(nid, speaker, body, *answers, portrait="Camellia"))


def alternative(host, nid, new_id, body, flag):
    """Select an informed variant before displaying a false memory/cover story."""
    old = node(host, nid)
    twin = copy.deepcopy(old)
    twin["Id"], twin["Text"] = new_id, body
    existing = next((page for page in host["Nodes"] if page["Id"] == new_id), None)
    if existing is None:
        host["Nodes"].append(twin)
    else:
        existing["Text"] = body
        existing["Choices"] = twin["Choices"]
    # Snapshot: do not redirect the variant's own outgoing answers.
    for page in [page for page in host["Nodes"] if page["Id"] != new_id]:
        for answer in list(page["Choices"]):
            if answer.get("Next") != nid:
                continue
            alt = copy.deepcopy(answer)
            alt["Next"] = new_id
            alt["Requires"].append(flag)
            answer["Forbids"].append(flag)
            if not any(choice.get("Next") == new_id and flag in choice.get("Requires", [])
                       for choice in page["Choices"]):
                page["Choices"].append(alt)


def _entry(scenes):
    h = scenes[P + "masks.two_lies"]
    text(h, "bored", '"That soldier has been watching my hands since supper. He thinks I have not noticed." '
         '{n}She ties the bag of insects shut and looks up.{/n} "You may sit. I was at the chapel before the watch bell. '
         'Ask the chaplain; he admired my gloves. Now I am here, sorting flowers. A very dull evening, would you not say?"')
    node(h, "bored")["Choices"].append(c('"You left out the walk between the chapel and camp."', "alibi"))
    add(h, "alibi", '{n}The knot stops between her fingers.{/n} "Did I? How careless. The chaplain can tell you where '
        'I was. These flowers can tell you where I am. You are welcome to ask about the rest; I have not promised to answer." '
        '{n}She moves her bedroll aside for you.{/n} "Stay. Let us see how closely you listen when I actually intend to lie."',
        c('"What game?"', "rules"), c('"Do spirits lie?"', "spirits"))
    text(h, "spirits", '"Constantly. That is what my teacher said, whenever a reading displeased her." '
         '{n}She runs a nail down a pressed leaf.{/n} "I watched her mouth instead. She always paused before telling '
         'Father something expensive. Shall we try it?"')
    text(h, "out_lied", '{n}Her finger taps her chin, then stops.{/n} "The cards are a lie. You want your opponent '
         'to think you cheat. The sleep... I have heard your footsteps after the watch changed." {n}She studies you.{/n} '
         '"And the last one? You said it without even looking away. I cannot decide. How irritating."')
    text(h, "fair", '"Absalom. You said it too quickly." {n}She beams.{/n} "One point to me. Do not sulk. '
         'You gave me such a long time to watch you before you answered."')
    h = scenes[P + "evening.a_table_for_strangers"]
    text(h, "how", '"Look at the cup. He needs both hands to keep it still. And he has turned that ring three times '
         'since we sat down." {n}She glances at the soldiers beside him.{/n} "They laugh whenever he pays. '
         'When his purse is empty, I wonder how many will stay. Your turn."')
    text(h, "you", '"Me?" {n}She puts down the untouched glass.{/n} "What have you noticed? My hands are steady. '
         'My sleeves are clean. And I have been perfectly pleasant to you." {n}She leans closer.{/n} '
         '"Tell me which part troubles you. I should hate to repeat a mistake."')
    text(h, "better", '"One gentleman in Kenabres said that while staring at my neckline. He could not remember '
         'a word I had said when I asked him to repeat it." {n}Her eyes move to your mouth.{/n} '
         '"You have been paying rather more attention. I have yet to decide what to do about that."')
    text(h, "last", '{n}At the citadel gate she keeps her hand in your arm while the watch files past.{/n} '
         '"Fye has terrible wine. I wanted my head clear, and you were far more interesting than the glass." '
         '{n}She lets go herself.{/n} "Ask me again. I might even drink next time."')
    h = scenes[P + "masks.a_dance_with_a_knife_in_it"]
    node(h, "lifted")["Choices"][0]["Set"].append(KNIFE_TAKEN)
    text(h, "anticipation", '{n}Boots sound outside: the next watch going to the walls. Camellia keeps her palm '
         'against your chest until the last pair passes.{/n} "Enough. You will be missed, and I dislike an audience '
         'that has not been invited." {n}She steps away and blows out the nearest candle.{/n} '
         '"Three steps and a turn. Remember where you put your hand."')
    h = scenes[P + "masks.the_funeral_i_would_like"]
    text(h, "enjoy", '"Look at the man behind the widow. He was laughing by the gate until she turned round. '
         'Now he has found a handkerchief." {n}Camellia smiles down from the parapet.{/n} '
         '"The chaplain is watching him too. I hope he calls on him to say a few words."')
    text(h, "critic", '"White lilies, and that blue ribbon against the widow\'s coat? Dreadful." '
         '{n}She follows the woman\'s hand along the coffin.{/n} "She keeps touching the lid. '
         'Did you see the bearer move his fingers away? He thought she meant to open it. I wish she would."')
    h = scenes[P + "evening.the_salle"]
    text(h, "open", '"Foils." {n}She tosses you one, hilt first. Its point is buttoned.{/n} '
         '"The quartermaster has nothing better. My father\'s master would have refused to touch them." '
         '{n}She takes her position.{/n} "In battle I am watching what is trying to kill us. Here I can watch '
         'your eyes before you strike. Do not disappoint me."')
    text(h, "rules", '"First touch to the body. Arms do not count." {n}Her point settles opposite your breastbone.{/n} '
         '"There. That is where I intend to touch you."')
    text(h, "fair", '{n}Her button presses beneath your breastbone. She leaves it there through a whole breath.{/n} '
         '"You watched my point and forgot my feet. Shall I show you again?"')
    text(h, "trick", '{n}She looks at the button against her ribs.{/n} "You looked at my shoulder. I followed your '
         'eyes, and you came in underneath." {n}She steps back, flushing.{/n} "Again. I want to see you try that twice."')


def _return(scenes):
    late = scenes[P + "killed.late_curtain"]
    text(late, "start", '{n}The crusade buried Camellia under a plain stone at the edge of Drezen\'s cemetery. '
         'Wedding lilies lie across it. The sexton holds his lantern over a spade. He asks forty gold to open the coffin '
         'and sixty to forget he did it. Beyond the wall, the watch calls the hour.{/n}')
    node(late, "coffin")["Text"] = node(late, "coffin")["Text"].replace('crosses himself', 'grips the lantern with both hands')
    node(late, "choose")["Choices"][0]["Set"].append(SEXTON)
    node(late, "choose")["Choices"].append(c('[Leave the spade for another night.]', abort=True))
    h = scenes[P + "killed.third_night"]
    text(h, "start", '{n}On the third night after Camellia\'s death you stand at her grave. The sexton has left '
         'the lid unnailed, as instructed. Now he holds out his palm: a hundred gold for the burial work and his silence. '
         'The watch bell sounds beyond the cemetery wall.{/n}')
    node(h, "start")["Choices"][0]["Crusade"] = dict(Resource="Finances", Amount=-100)
    node(h, "start")["Choices"][0]["Set"].append(SEXTON)
    node(h, "start")["Choices"].append(c('[Pay him another night.]', abort=True))
    text(h, "breath", '{n}Her voice is a dry whisper from the coffin.{/n} "Your sexton smells of lamp oil. '
         'Get him out of here. Put the lid back; I am dead until I say otherwise." {n}Her eyes turn to you.{/n} '
         '"Go home. I shall find you."')
    for h in (h, late):
        terminal = "home" if h["Id"].endswith("third_night") else "walk"
        node(h, terminal)["Choices"].append(c('[Answer her when she calls you back.]', "eng8.reunion",
                                              requires=("irabeth.chapter_five",)))
        text(h, "eng8.reunion", '{n}The lid lifts again before you leave. She catches your sleeve.{/n} '
             '"Wait. You have given me a very troublesome evening. I intend to make you hear my price before you go."')
        text(h, "eng8.price", '"Camellia Gwerm stays dead. That name, and what I could have claimed with it, '
             'are mine to give up. But the box must be filled. Help me with the stones before dawn." '
             '{n}She holds out her hand, palm up.{/n} "For staying near you: your blood when I ask, or your name '
             'first on my list. Choose. I have not promised you anything else."')
        for answer in node(h, "eng8.price")["Choices"][:2]:
            answer["Next"] = "r2.stones"
        add(h, "r2.stones", '{n}Together you carry loose stones from the cemetery wall. She arranges them '
            'in her coffin while you hold the lid. When the box is full she steps clear, brushes dirt from her '
            'skirt and watches you cover the grave. The watch bell sounds again before you finish.{/n} '
            '"Tomorrow night. Somewhere with a lock. You have agreed; now I want to see you keep your word."',
            c('[Put the spade away.]', flags=(ct.FILLED,)))
    # CAM-A4-02: the prepared fallback retains its saved terminal answers.
    # Retire unpaid exits and append copies that deliver the approved sibling beat.
    prepared = scenes[P + "killed.late_curtain_prepared"]
    stones = copy.deepcopy(node(late, "r2.stones"))
    prepared["Nodes"].append(stones)
    price = node(prepared, "eng8.price")
    for original in list(price["Choices"][:2]):
        paid = copy.deepcopy(original)
        paid["Next"] = "r2.stones"
        original["Requires"].append(ct.FILLED)
        price["Choices"].append(paid)
    h = scenes[ct.PERFORMANCE]
    h["DelayHours"] = 0
    text(h, "late", '"The sexton told me what you paid him, after I woke. He hoped I would pay him again '
         'to keep quiet about you. I told the sexton to ask you himself."')
    text(h, "wrong", '"Your sexton told me about the wedding lilies after I woke. I asked whether the chaplain '
         'had noticed. Apparently he praised them. I should have liked to see his face."')
    text(h, "why", '"You paid the spirits for my body. You did not pay me to come here." '
         '{n}She turns her glass.{/n} "I woke with your blood in my mouth and your sexton staring at me. '
         'You put the lid back when I asked. I wanted to see what else you would do if I asked nicely. '
         'So I chose this table. Sit closer; Fye has been trying to hear us."')
    text(h, "will", '"I still have the will you gave me. Papa acknowledged me at last, and now I would '
         'have to show my living face to claim anything. I read it after I woke. How tiresome of him to '
         'make the one useful gift so inconvenient."')
    text(h, "how", '{n}She removes a glove and turns her hand toward the lamp.{/n} "Your sexton looked '
         'almost as ill as I did when we parted. I sent him lilies. He did not thank me."')
    alternative(h, "how", "r2.clawed", '{n}She peels off a glove. Linen covers the torn fingertips.{/n} '
                '"Nobody gave me a door. By the time your spade reached me I had ruined both my nails and the pine."',
                P + "prepared_clawing")
    # The existing prepared passage alone establishes these injuries.
    node(scenes[P + "killed.third_night"], "dug")["Choices"][0]["Set"].append(P + "prepared_clawing")
    h = scenes[P + "killed.performance_letter"]
    h["DelayHours"] = 96
    # Failure is a delivery observation, not the start of the four-day wait.
    h["Requires"].remove(ct.PRESENCE_FAILED)
    h["RequiresAnyGroups"] = [[ct.PRESENCE_FAILED]]
    text(h, "late_l", '"Your sexton told me about the coins after I woke. He counted them twice. '
         'I shall remember his face much longer than he remembers the sum."')
    h = scenes[P + "beat.her_own_grave"]
    text(h, "order", '"The sexton says Anevia came here with a bottle and sat beside the stone. '
         'He told me after I woke. She did not leave the bottle. How practical of her."')
    if any(x["Id"] == "order" for x in h["Nodes"]):
        # Do not put a currently absent Anevia at a later encounter.
        for page in h["Nodes"]:
            for answer in page["Choices"]:
                if answer.get("Next") == "order":
                    answer["Requires"].append("anevia.present_now")
        # A missing informant callback still has a complete route through the lead.
        for page in h["Nodes"]:
            originals = list(page["Choices"])
            for answer in originals:
                if answer.get("Next") == "order":
                    bypass = copy.deepcopy(answer)
                    bypass["Next"] = "stone"
                    bypass["Requires"].remove("anevia.present_now")
                    bypass["Forbids"].append("anevia.present_now")
                    page["Choices"].append(bypass)
    for family in ("returned.terms", "returned.test"):
        for suffix in ("", "_camp", "_alive"):
            scenes[P + family + suffix]["DelayHours"] = 24
    h = scenes[P + "beat.spirits_due"]
    h["Chapters"] = [3, 5]
    text(h, "open", '"I am well." {n}She sits beside the supply wagons, the silver bowl at her '
         'feet. A teamster gives her a wide berth.{/n} "The chaplain has stopped asking how. I liked him better '
         'when he was frightened. You, however, made a promise. Come here."')
    text(h, "chosen", '"Your blood, from my knife. That is what bought my breath back." {n}She picks up '
         'the bowl.{/n} "We shall pay the first offering now. The spirits can count the new moons afterwards."')
    text(h, "silent", '{n}She takes your offered wrist and sets it over the silver.{/n} '
         '"Keep it there. I have brought the knife."')
    text(h, "unmissed", '{n}She draws the blade across your wrist. Blood strikes silver; then the surface '
         'draws inward without a tilt of the bowl. She watches until the last red bead is gone and binds the cut.{/n} '
         '"There. They have had what you promised. They will ask again."')
    for suffix in ("", "_camp", "_alive"):
        h = scenes[P + "beat.lesson" + suffix]
        alternative(h, "done", "r2.price_known", '"You know my price." {n}She takes back the knife and unlocks '
                    'the door.{/n} "Tomorrow night, then. I want to see whether you meant it."', ct.TERMS)


def _knowledge(scenes, payload):
    payload.setdefault("Derived", {})[KNOWN] = [[ct.UNMASKED], [DISCLOSED], [ct.AMULET_KEPT]]
    payload["Derived"][P + "kills_answered.present_victim"] = [
        ["nurah.present_now", "nurah.dead_camellia"],
        ["soana.present_now", "soana.killed_by_camellia"],
        ["kaylessa.present_now", "kaylessa.camellia_killed"]]
    h = scenes[P + "masks.mireya"]
    alternative(h, "who", "who_known", '"Mireya? We have already disposed of her, have we not?" '
                '{n}She rolls the bone snake between her fingers.{/n} "I can still tell you what I used to '
                'tell the chaplains. You may watch my face this time."', KNOWN)
    alternative(h, "needs", "needs_known", '"Blood. A holy purpose. An explanation for every stained sleeve." '
                '{n}She strokes the snake\'s head.{/n} "You know how useful she was. '
                'I could tell you I wanted to heal the Worldwound and you would have to listen politely."', KNOWN)
    alternative(h, "name", "name_known", '"I gave her a name before I gave her a story. Mireya." '
                '{n}She looks at the amulet.{/n} "A woman in a book, drowning so prettily. '
                'It sounded much better than mine. What would you have called her?"', KNOWN)
    alternative(h, "after", "after_known", '"That is enough of her for tonight." {n}She puts the '
                'snake away and pats the place beside her at the fire.{/n} "Stay a little longer. '
                'I should like some company that can answer."', KNOWN)
    h = scenes[P + "cards.a_bowl_for_mireya"]
    h["Chapters"] = [3, 5]
    alternative(h, "her", "her_known", '"Mireya\'s supper. You need not make that face; I know you know." '
                '{n}She holds out the bowl.{/n} "I used to do this with an audience. Shall we see whether '
                'you can watch without spoiling it?"', KNOWN)
    alternative(h, "after", "after_known", '{n}She fastens the amulet.{/n} "The same amount went in and came out. '
                'You saw. The chaplains never stayed to check." {n}She smiles.{/n} "Thank you for staying. '
                'Do you intend to give them a demonstration? I should enjoy watching."', KNOWN)
    alternative(h, "hold", "hold_known", '{n}The bowl warms your palms. She dips the bone snake '
                'and watches you over its cord.{/n} "There, darling. Drink." {n}Her mouth twitches.{/n} '
                '"You are making this very difficult. I used to get through the whole thing without laughing."', KNOWN)
    alternative(h, "grace", "grace_known", '"Grace? For my poor imaginary friend?" {n}She holds '
                'out the amulet, smiling.{/n} "Do make it improper. I intend to enjoy this prayer."', KNOWN)
    alternative(h, "refuse", "refuse_known", '"Then watch." {n}She balances the bowl herself.{/n} '
                '"I have done this often enough without your hands. I do prefer having your attention."', KNOWN)
    node(h, "bargain")["Text"] = node(h, "bargain")["Text"].replace(
        'if she dies, whatever the hand and whatever the field', 'if she dies at my hand or on my order')
    for suffix in ("", "_camp", "_alive"):
        h = scenes[P + "cards.the_amulet" + suffix]
        for answer in node(h, "open")["Choices"]:
            answer["Requires"] = [KNOWN if k == ct.UNMASKED else k for k in answer["Requires"]]
            answer["Forbids"] = [KNOWN if k == ct.UNMASKED else k for k in answer["Forbids"]]
        text(h, "known", '"You know there is no Mireya. What you have not asked is why I still wear her." '
             '{n}She turns the bone snake over.{/n} "My fingers reach for her when someone asks an awkward question. '
             'It is very useful to have something to look at instead of them."')
        node(h, "tell")["EnterSet"] = [DISCLOSED]
        # The actual confession, rather than accepting her keepsake, records knowledge.


def _turn(scenes):
    for suffix in ("", "_camp", "_alive"):
        h = scenes[P + "returned.terms" + suffix]
        for nid in ("named", "mine"):
            node(h, nid)["Text"] = node(h, nid)["Text"].replace("Three nights.", "Tomorrow night.")
        text(h, "none", '"Then you will not have me in your rooms." {n}She draws her sleeve out of reach.{/n} '
             '"You may issue your crusade orders in the morning. Tonight you have nothing further to ask of me."')
        h = scenes[P + "returned.test" + suffix]
        text(h, "blade", '"Oh, good." {n}She looks down at the point by her ribs, then lifts her knife clear '
             'of your throat and waits for yours to lower.{/n} "I wanted to see your face when you meant it. '
             'Now I have. I shall leave it intact tonight."')
        for nid in ("yes", "yes_a"):
            if not any(x["Id"] == nid for x in h["Nodes"]):
                continue
            text(h, nid, '"Yes. Tonight I am staying." {n}She slides the knife into your belt, hilt ready '
                 'for her hand, and leaves her fingers there.{/n} "I have not forgotten your name. I am '
                 'choosing what to do with it. Keep this where I can find it."')
            node(h, nid)["Choices"][0]["Text"] = '[Leave her knife in your belt, hilt ready for her hand.]'
        h = scenes[P + "bond.not_today" + suffix]
        node(h, "after")["Text"] = node(h, "after")["Text"].replace(
            "Not because I've stopped loving you. Because I will have.",
            "Because I shall love you more, and want to spoil that trusting face more than ever.")
        text(h, "kept", '"Your shelf still has my list. I look at it before I sleep." {n}She glances '
             'toward the paper.{/n} "You can check the names yourself. How tiresome; I used to have my privacy."')
        text(h, "ghost", '"Your witness is still talking. That face in the chapel, those sleeves in the alley: '
             'they have embroidered it considerably. And Fye has started looking at my hands when I laugh." '
             '{n}Her nail scrapes the window frame.{/n} "You have made my evenings very inconvenient."')


def _witness(scenes):
    for suffix in ("", "_camp", "_alive"):
        h = scenes[P + "bond.witness" + suffix]
        if suffix == "":
            text(h, "open", '"Fye asked where he had heard my laugh before." {n}She walks six '
                 'steps to the wall and six back.{/n} "I told him Nerosyan. He accepted that. '
                 'The woman who followed me to the chapel did not."')
        else:
            text(h, "open", '"Someone has been asking about my sleeves at Fye\'s." {n}She walks '
                 'six steps to the wall and six back.{/n} "I should like to know who has been answering."')
        for nid, name in (("alive_w", "Radan"), ("dead_w", "Radan"), ("killed_w", "Lethra")):
            if any(x["Id"] == nid for x in h["Nodes"]):
                body = node(h, nid)["Text"]
                body = body.replace('A lamplighter in the lower city, last week.', 'Radan, a lamplighter in the lower city.')
                body = body.replace('A night-soil man in the lower city.', 'Radan, a night-soil man in the lower city.')
                body = body.replace('A woman at the chapel,', 'Lethra, a candle-seller at the chapel,')
                text(h, nid, body)
        node(h, "choice")["Choices"][0]["Text"] = '[Trickster] "Let me give them a reason to look elsewhere. They stay free."'
        text(h, "lied", '{n}You visit the witness at the infirmary door. They repeat what they saw, angrily, '
             'when you ask whether they might have mistaken the woman. You let them finish. Then you ask Fye '
             'to introduce his veiled Nerosyan customer to the watch by the name she has chosen. The witness '
             'is free to repeat the account; the watch now has two names to ask about. They leave the infirmary '
             'of their own accord, refusing your offer of an escort.{/n}')
        text(h, "lied_after", '"A second name. How industrious of you." {n}She straightens your collar '
             'with a sharp tug.{/n} "And when they ask to see both women together? No, do not tell me. '
             'I want to watch you answer." {n}She lets go.{/n} "You have kept my witness alive. I noticed. '
             'You will be coming with me the next time I visit Fye."')
        node(h, "choice")["Choices"].append(c('"Their account goes to the watch today. Killing them will bury nothing."', "r2.public"))
        add(h, "r2.public", '{n}The witness gives their name to the watch and repeats exactly what they saw. '
            'You have the account read aloud before the tavern empties for muster. They correct one of the '
            'soldiers who tries to add a bloody knife: they saw no knife. When offered an escort, they accept '
            'and ask to go home. Camellia waits by the door until the guard has gone with them.{/n}',
            c("Continue", "r2.public_after"), speaker="Narrator")
        add(h, "r2.public_after", '"You have been very busy with my affairs." {n}She keeps her voice low; '
            'a soldier is still looking toward the door.{/n} "Now if I kill them, every idiot in that room '
            'will remember why. How attentive of you." {n}She pulls the veil straight.{/n} '
            '"Come. You have cost me my table by the window. I intend to see whose company you keep at yours."',
            c('[Walk back with her.]', flags=(ct.WITNESS_LIED, PUBLIC)))
        later = scenes[P + "bond.not_today" + suffix]
        alternative(later, "ghost", "r2.public_callback", '"The watch read your witness\'s account again '
                    'yesterday. Someone remembered my laugh at Fye\'s." {n}Her nail catches in the window '
                    'frame.{/n} "I have been wearing a different veil. You will not be allowed to forget why."', PUBLIC)
        h = scenes[P + "day.a_new_friend" + suffix]
        text(h, "list", '{n}The shelf catches your eye: paper, ash, or an empty space where the list lay. '
             'Ilse has been walking with her in the evenings. Her name may already be among the others.{/n}')
        # Move the existing charge ahead of the irreversible warning; no added fee.
        charge = node(h, "warn")["Choices"][0].pop("Crusade")
        for page in h["Nodes"]:
            for answer in page["Choices"]:
                if answer.get("Next") == "warn":
                    answer["Crusade"] = copy.deepcopy(charge)
        h = scenes[P + "evening.the_prisoner" + suffix]
        text(h, "ask", '"He will never give me that look. He knows we are enemies." {n}She turns from the '
             'cultist to you, flushed.{/n} "I can still make him afraid. That would be pleasant enough '
             'for tonight. May I have him?"')
        text(h, "watch", '"My face? How discerning." {n}She draws the knife. The cultist jerks against '
             'his chains as she leans close and speaks too softly for the stair guard to hear. She looks '
             'back at you over his shoulder. When he stops moving she washes the blade in the bucket '
             'and dries her hands finger by finger.{/n} "Still watching?"')


def _continuity(scenes):
    h = scenes[P + "cards.the_old_womans_deck"]
    node(h, "back")["Text"] = node(h, "back")["Text"].replace(
        'I have always made very sure that somebody else did the turning.',
        'I have always been very careful to read someone else. You made me look at myself.')
    for suffix in ("", "_camp", "_alive"):
        h = scenes[P + "cards.the_deck_again" + suffix]
        text(h, "stacked", '{n}She looks from you to the cards.{/n} "You did not. I watched your hands." '
             '{n}She searches your face and fails to settle on an answer.{/n} "Did you?" '
             '{n}Then she laughs and pulls you down onto the silk.{/n}')
        h = scenes[P + "cards.two_lies_again" + suffix]
        node(h, "open")["Text"] = node(h, "open")["Text"].replace('for months', 'since then')
        text(h, "mine", '"The first is a lie. You are a little afraid. I felt your pulse." '
             '{n}She pulls you down by the collar. Her fingers find the laces while the knife '
             'stays on the pillow beside her ear.{/n} "And the rest? Show me."')
        h = scenes[P + "day.the_second_dance" + suffix]
        text(h, "open", '{n}She has cleared the floor and set candles in the corners. Beyond the window, '
             'the wall patrol passes. She is barefoot, her skirt pinned to the ankle.{/n} '
             '"Three steps and a turn. Come here."')
        text(h, "noticed_d", '"You named the knife, and I laughed. You looked so pleased to have found it." '
             '{n}She puts your hand at her waist.{/n} "It is still there. Tonight I shall let you look properly."')
        alternative(h, "noticed_d", "r2.taken_d", '"You stole my knife and I made you give it back." '
                    '{n}She puts your hand at her waist.{/n} "Tonight you may ask. I want to watch you undo the buckle."', KNIFE_TAKEN)
        h = scenes[P + "evening.breakfast" + suffix]
        text(h, "open", '"The cook was lighting his stove when the first muster bell rang. I went down '
             'before he could give the good honey to the officers." {n}She sits at the foot of your bed in '
             'your shirt, eating bread from a knife.{/n} "He kept looking at my hands. I washed them for him. '
             'He still looked. Here; I brought enough for you."')
        h = scenes.get(P + "evening.a_gift_for_a_dead_woman" + suffix)
        if h:
            text(h, "open", '"For me?" {n}She puts down her book and watches your hands.{/n} '
                 '"Father chose such expensive dresses. I hated the collars. Let us see whether '
                 'you have looked at me more closely than he did."')
            node(h, "foils")["Text"] = node(h, "foils")["Text"].replace(
                'You want to converse with me properly.', 'No button to stop the point this time. How thoughtful.')
        h = scenes.get(P + "evening.the_mirror" + suffix)
        if h:
            text(h, "voss", '"Mireya Voss, widow, of Nerosyan." {n}She raises her chin at the glass.{/n} '
                 '"Too young. I shall put the collar higher. Fye\'s customers have been looking at my throat '
                 'instead of listening to my dreadful account of my husband."')
        h = scenes[P + "cards.the_amulet" + suffix]
        h["Entry"] = '"You have stopped feeding Mireya."'
        text(h, "why", '"You have watched me long enough to know what I want. I am tired of '
             'blaming the snake when you ask." {n}She turns it toward you.{/n} "I liked having '
             'an excuse ready. Now I want to see whether you stay when I put it away."')
    h = scenes[P + "day.the_flower_market"]
    text(h, "open", '"Market day. I want flowers for my grave." {n}She pins the veil and offers her arm.{/n} '
         '"The patrol is changing; we shall reach the square before the soldiers buy everything worth having."')
    text(h, "market", '{n}Below the cathedral the sellers call to the Commander. One bows to the veiled '
         'woman and offers his condolences. She thanks him in a voice you hardly recognise. When he turns '
         'to fetch roses, her fingers tighten on your arm.{/n}')
    text(h, "choose", '"He remembers the widow. He has offered her lilies twice." {n}She examines a rose.{/n} '
         '"When I came here as myself he offered me the expensive ones. I find I resent the difference."')
    text(h, "pay", '{n}The seller warns her about the dark berries. She thanks him and chooses them with '
         'a white rose and a red one. He counts your payment and asks whether the widow will come again '
         'next market day.{/n} "Perhaps. Do keep the red ones for me."')
    text(h, "not", '{n}She turns her veiled face toward you.{/n} "Not to you. No, I had noticed." '
         '{n}Her thumb strokes your arm; then she turns to the seller.{/n} "A red rose. '
         'The Commander is paying. You may show us the expensive ones."')
    for suffix in ("", "_camp"):
        h = scenes[P + "day.the_anniversary" + suffix]
        text(h, "open", '"An early observance. I am not waiting a month for you to forget the date." '
             '{n}She smooths the black silk.{/n} "The crusade may march tomorrow. Tonight I shall have '
             'my wake, my good dress and your company."')
    for h in scenes.values():
        if not h["Id"].startswith(P):
            continue
        for page in h["Nodes"]:
            page["Text"] = page["Text"].replace("They've been praying over me for a week", "They have been praying over me since I came back")
            page["Text"] = page["Text"].replace("priests who crossed themselves over my bed", "clerics who clutched their holy symbols over my bed")
    # Oath readers use present availability; a woman's departure never closes Camellia.
    for suffix in ("", "_camp"):
        h = scenes[P + "kills_answered.oath" + suffix]
        # Derived is OR-of-ANDs; RequiresAnyGroups is AND-of-ORs.
        h["Requires"].append(P + "kills_answered.present_victim")
        for answer in node(h, "start")["Choices"]:
            if answer.get("Next") in ("nurah", "soana", "kaylessa"):
                answer["Requires"].append(answer["Next"] + ".present_now")
        # If the earlier historical victim has left, let the current one answer.
        node(h, "start")["Choices"].extend([
            c("Continue", "soana", requires=("soana.present_now", "soana.killed_by_camellia", "nurah.trickster.returned", "nurah.dead_camellia"), forbids=("nurah.present_now",)),
            c("Continue", "kaylessa", requires=("kaylessa.present_now", "kaylessa.camellia_killed", "camellia.kill_returned.earlier"),
              forbids=("nurah.present_now", "soana.present_now"))])
    h = scenes[P + "cards.the_cutler"]
    text(h, "choose", '{n}She takes down a long serrated blade and checks its balance, then puts '
         'it back.{/n} "Too heavy. I should have to let go of your hand to draw it." '
         '{n}She chooses a smaller one.{/n} "This would fit in my sleeve. Hold out your hand."')
    text(h, "buy", '{n}The dwarf names his price. She watches you lay the coins down.{/n} '
         '"Good. He has been waiting for you to haggle so he can tell you to leave. '
         'I wanted to take it home tonight."')


def _debts(scenes):
    for suffix in ("", "_camp", "_alive"):
        h = scenes[P + "evening.breakfast" + suffix]
        # Append to the existing finish answer; it remains at index zero.
        answer = node(h, "close")["Choices"][0]
        original = copy.deepcopy(answer)
        original["Next"] = "r2.public_request"
        original["Requires"].append(P + "encounter.all")
        original["Forbids"].append(TRUTHS)
        answer["Forbids"].append(P + "encounter.all")
        node(h, "close")["Choices"].append(original)
        paid = copy.deepcopy(answer)
        paid["Forbids"].remove(P + "encounter.all")
        paid["Requires"].extend([P + "encounter.all", TRUTHS])
        node(h, "close")["Choices"].append(paid)
        add(h, "r2.public_request", '{n}She catches your sleeve before you rise.{/n} "Three truths. '
            'You promised me company." {n}She takes the honey pot toward the mess-room door and '
            'waits there, looking back at you.{/n}',
            c('"I love you. I love you. I love you."', "r2.public_paid"),
            c('"Another breakfast. We have orders to give."', "r2.public_unpaid"))
        add(h, "r2.public_paid", '{n}The cook stops with a ladle in his hand. A soldier at the nearest '
            'table coughs into his porridge. Camellia looks from one to the other, then comes back '
            'and kisses the corner of your mouth.{/n} "All three. And not a lowered voice among them. '
            'How obliging." {n}She takes the good honey back from the table.{/n}',
            c('[Go to the muster.]', flags=(TRUTHS,)))
        add(h, "r2.public_unpaid", '"Then I shall choose another audience. I have not forgotten." '
            '{n}She goes back for the knife before she joins you at the door.{/n}', c('[Go to the muster.]'))
    for family in ("epilogue.kept", "epilogue.kept_on_record", "epilogue.commit", "epilogue.commit_on_record"):
        h = scenes[P + family]
        if "trickster.now" not in h["Requires"]:
            h["Requires"].append("trickster.now")
        page = node(h, "page")
        paras = page.setdefault("Paragraphs", [])
        memorial = family.endswith("on_record")
        if memorial:
            paras.append(p('{n}The bowl remained empty after Threshold. The Commander\'s blood could '
                           'no longer answer the battle spirits. Camellia wrapped it and took it away '
                           'herself; nobody saw her make another offering in the Commander\'s name.{/n}',
                           any_groups=[[ct.OWED, ct.BARGAIN_COST]]))
            paras.append(p('{n}She had intended to hear three truths before company. At the memorial '
                           'she listened to the chaplain instead and left before he finished.{/n}',
                           requires=(P + "encounter.all",), forbids=(TRUTHS,)))
        else:
            paras.append(p('{n}At each new moon she brought out the silver bowl. The Commander kept '
                           'a wrist over it while she took the agreed blood. She watched the surface '
                           'empty before she bound the cut. The spirits\' bargain had survived the war.{/n}',
                           any_groups=[[ct.OWED, ct.BARGAIN_COST]]))
            paras.append(p('{n}At the first postwar dinner she called for the three truths still owed '
                           'from their game. The Commander said each one aloud. A guest spilled wine; '
                           'she watched the guest blot a cuff before she answered the Commander '
                           'with a kiss.{/n}', requires=(P + "encounter.all",), forbids=(TRUTHS,)))
            paras.append(p('{n}When she had gone away for a season, the Commander found her at the '
                           'door one night, setting down a travelling bag. She asked who had touched '
                           'her shelf, checked the knife and came back to bed.{/n}', requires=(ct.COMMITTED,)))
            paras.append(p('{n}The witness\'s account remained with the watch. Camellia changed her '
                           'veil and her table at Fye\'s, but not the knife in her sleeve. She made '
                           'the Commander accompany her past the tavern where the testimony had '
                           'been read aloud.{/n}', requires=(PUBLIC,)))
        if family == "epilogue.commit":
            paras.extend([
                p('{n}That spring night she took the promised blood before she chose to stay. '
                  'The Commander held still; she watched their face, bound the cut and put the '
                  'bowl aside. Then she reached for their collar.{/n}', requires=(ct.BLED,)),
                p('{n}That spring night she set the edge beneath the Commander\'s jaw and spoke '
                  'the name she had been offered. After a long look she withdrew it. She chose '
                  'to leave this friend alive, and to stay. The claim remained hers.{/n}', requires=(ct.MARKED,))])
        for para in paras:
            para["Text"] = para["Text"].replace('Nobody on it ever changed.', 'She continued to add names; '
                'the Commander could watch the ink dry and decide what to do.') if ct.LIST_KEPT in para.get("Requires", []) else para["Text"]
            para["Text"] = para["Text"].replace('telling children about the singing ghost with the dog made of mist',
                                                'still insisting on the face they had seen, despite the widow\'s other name')
            para["Text"] = para["Text"].replace('The Gwerm estate went to a cousin the lawyers found.',
                                                'She left her claim on the Gwerm estate unused.')
    # The classified legacy refusal surface covers both life histories. Its
    # exit remains byte-for-byte equivalent; no shared contract entry is added.
    old = scenes[P + "epilogue.refused"]
    old["Requires"] = [k for k in old["Requires"] if k != ct.RET]
    old["Forbids"] = list(dict.fromkeys([*old["Forbids"], "sacrifice"]))
    old.setdefault("ForbidOverrides", {})["sacrifice"] = "trickster.commander_back"
    for para in node(old, "page").get("Paragraphs", []):
        if ct.OWED in para.get("Requires", []):
            para["Text"] = ('{n}Before they parted, the Commander had paid blood into her silver bowl. '
                            'The scars remained. The battle spirits\' claim had been for her return, '
                            'not for her affection; closing the bedroom door did not erase it.{/n}')
    text(old, "page", '{n}The Commander had closed the door on Camellia. '
         'Her name remained among the crusade\'s records.{/n}')
    paragraphs = node(old, "page").setdefault("Paragraphs", [])
    paragraphs.append(p(
        '{n}Until the war ended she answered the Commander\'s orders with exquisite courtesy. '
        'She never mistook those orders for another invitation to their rooms.{/n}',
        requires=("camellia.present_now",), forbids=(ct.RET,)))
    paragraphs.extend((
        p('{n}After the war she went her own way. A pressed camellia arrived without a letter, '
          'in the careful hand the Commander remembered.{/n}', requires=("camellia.present_now",)),
        p('{n}She had been dismissed from the crusade. No further orders went to her; no reply '
          'came from her.{/n}', requires=(ct.KICKED,), forbids=("camellia.present_now", ct.DEAD, ct.KILLED)),
        p('{n}Her death stood. The room was cleared, and no new flowers arrived.{/n}',
          any_groups=((ct.DEAD, ct.KILLED),), forbids=("camellia.present_now", P + "coffin_life")),
        p('{n}She had returned once. Her later death left the room empty again. No new flowers arrived.{/n}',
          requires=("camellia.returned_actor_lost",), forbids=("camellia.present_now",)),
        p('{n}The woman who had returned from the coffin was dismissed from the crusade. '
          'No further orders went to her, and no reply came.{/n}',
          requires=(ct.KICKED, P + "coffin_life", "camellia.epoch_redeparted"),
          forbids=("camellia.present_now", "camellia.returned_actor_lost")),
    ))


def _slots(scenes):
    root = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/camellia"
    for path in sorted(root.glob("*.json")):
        brief = json.loads(path.read_text(encoding="utf-8"))
        spec = brief.get("insertion")
        if not spec:
            continue  # tracker brief (Gemory) still waiting for its structure hook
        if "insertion" not in brief:
            continue  # opportunity brief (no structure hook yet): tracking only, nothing to insert
        spec = brief["insertion"]
        h = scenes[spec["scene_id"]]
        anchor = spec["after_node"]
        if anchor == "end":
            # Route the already selected strap outcome, retaining the old end node.
            anchor = "strap" if "from strap" in spec["branch"] else "leave"
        answer = node(h, anchor)["Choices"][0]
        successor = answer["Next"]
        if anchor in ("strap", "leave"):
            successor = "end"
        answer["Next"] = brief["slot_id"]
        # Explicit slot: adult intimacy in the situation and voice described by
        # this slot's JSON. Default is a heated cut; explicit prose is user-filled.
        add(h, brief["slot_id"], brief["default_text"], c("Continue", successor))
    # Keep initiating motions once. Slots contain the remaining clothing/cut.
    for suffix in ("", "_camp", "_alive"):
        h = scenes[P + "cards.two_lies_again" + suffix]
        text(h, "all", '"Three truths. Cheat." {n}She pulls you close by the collar.{/n} '
             '"You will say them when I ask. Before whoever I choose." {n}She drops the knife '
             'from the pillow and draws you down into a kiss.{/n}')
        h = scenes[P + "bond.not_today" + suffix]
        text(h, "night", '{n}She drives the knife into the window frame, then takes your face '
             'in both hands. She kisses you with her eyes open. Her cold fingers warm against '
             'your neck as she draws you toward the bed.{/n}')
        h = scenes[P + "day.the_second_dance" + suffix]
        text(h, "strap", '{n}The buckle resists your fingers. She watches until it gives, '
             'then lets the warm knife slide into your hand.{/n} "Mind the edge. I have '
             'further use for those fingers."')
        text(h, "end", '{n}Later, the last candle gutters beside the cleared floor. She listens '
             'to the watch changing beyond the shutters and rests her cheek against your shoulder.{/n} '
             '"There. You can stop counting now."')


def integrate(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"] if s.get("Relationship") == "camellia"}
    _entry(scenes)
    _return(scenes)
    _knowledge(scenes, payload)
    _turn(scenes)
    _witness(scenes)
    _continuity(scenes)
    _debts(scenes)
    _slots(scenes)

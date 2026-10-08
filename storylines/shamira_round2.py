"""Shamira's round-two situations, applied after her partner layer.

AUTHORED: the mind refuge, grown shell and nightly tether, optional warning,
thought decoy, courier contacts, patrol and surgeon consequences. Native anchors
are documented in tools/route_packs/plans/shamira-setpieces.md. These additions
do not purchase affection or alter another route. Saved nodes/answers stay put;
dispatch copies and explicit slots append to their existing carrier.
"""
import copy

from story_format import c, n, p, scene

P = "shamira.trickster."
EXTRACTED = P + "essence_taken"
SPENT = P + "essence_spent"
HANDED = "shamira.cauldron_shown.latched"
AUDIENCE = "noct.acq.audience_started"
EDGE = P + "terms.edge"
HID = P + "hid"
ACCEPTED = P + "game_accepted"
SUPPORT = P + "throne.support"
TOLD = P + "barracks.told"
SETTLED = tuple(P + "barracks." + x for x in ("told", "covered", "blamed"))
ARU_PRESENT = "arueshalae.present_now"
ARU_EVIL = "arueshalae.corrupted"
ARU_EARNED = P + "arueshalae_earned"


def variant(s, node, flag, text, suffix, *, yes=True):
    """Preserve every old answer index, appending its opposite history arm.

    The original node remains the negative arm; only incoming edges dispatch.
    New copies retain the outgoing decisions, costs and targets.
    """
    alt = copy.deepcopy(node)
    alt["Id"] = node["Id"] + "_" + suffix
    alt["Text"] = text
    old_id = node["Id"]
    for parent in list(s["Nodes"]):
        for answer in list(parent["Choices"]):
            if answer.get("Next") != old_id:
                continue
            other = copy.deepcopy(answer)
            answer["Forbids" if yes else "Requires"].append(flag)
            other["Requires" if yes else "Forbids"].append(flag)
            other["Next"] = alt["Id"]
            parent["Choices"].append(other)
    s["Nodes"].append(alt)
    return alt


def integrate(payload):
    own = [s for s in payload["Scenes"] if s["Id"].startswith((P, "shamira.early."))]
    by = {s["Id"]: s for s in own}
    payload.setdefault("QuestObjectives", {})[EXTRACTED] = ["62920c1a061578143b4106fc456e6075", "Completed"]
    payload.setdefault("SeenCues", {})[SPENT] = ["2303848f628c04b40b45025ebb06d2b4"]
    payload.setdefault("Derived", {})[ARU_EARNED] = [[key] for key in (
        "arueshalae.recruited_drezen", "arueshalae.recruited_redoubt",
        "arueshalae.evil_recruited", "arueshalae.trickster.returned")]
    # Both evidence readers are native facts, never inferred from killing her.
    payload["Relationships"]["shamira"]["Description"] = (
        "Shamira reads minds and sows dreams. Socothbenoth wants her essence. "
        "A thread in a willing mind might offer her an escape; a stolen body would need warmth. "
        "None of that tells me what the Ardent Dream will choose to do with me.")

    # Sweep the original and all folded copies together. No fold can restore a
    # prior encounter, procurement, confession or body that never occurred.
    for s in own:
        for node in list(s["Nodes"]):
            id = node["Id"]
            text = node["Text"]
            text = text.replace("the door I already knew", "a door you had left open")
            text = text.replace("beside Ziforian", "with his hands over his ears")
            text = text.replace("You threw me out of your head in my own Harem, or you never came, and then tonight", "There was no willing opening for me to follow, and then tonight")
            text = text.replace("Only one mind I had ever been let into.", "One familiar mind in that room, one you had opened to me before.")
            text = text.replace("with the cauldron full and the Council waiting", "with the Council still expecting its prize")
            text = text.replace("Now I only want the chair.", "I still want her. And her chair. Neither desire has made her merciful.")
            text = text.replace("because in a dream there is no reason to", "with her gown folded out of reach")
            text = text.replace("Find me a body, and I'll show you the difference.", "Find me a body. Then I can decide what to do with these hands.")
            text = text.replace("You mean it the way a child means it when it points at a fire.", "You want me even now, with nothing to look at and a knife between us.")
            text = text.replace("Children who point at fires get burned, Golarian. I am going to enjoy watching you learn that.", "Keep wanting, Golarian. I mean to have something worth looking at again.")
            text = text.replace("like a man selling a lame horse to a blind woman", "like a horse-dealer selling a lame mare to a blind buyer")
            node["Text"] = text
            if s["Id"] == P + "react.daeran_sleep":
                node["Text"] = '{n}Daeran watches you over the rim of his cup.{/n} "You talk in your sleep now, my dear. Everyone in the corridor has heard it. In two voices. One of them is very bored, very rude, and extraordinarily pleased with herself." {n}He studies your expression, then smiles.{/n} "The Ardent Dream? Oh, this will be fun. Tell her the walls in this fortress are thin. Or do not. I should hate to lose the entertainment."'
            if "It's in his diamond now." in text:
                node["Text"] = text[:text.index("It's in his diamond now.")] + 'My fire is in the body you killed. I cannot reach it from your skull. I came through your door without it. Do not confuse an escape with being whole."'
                variant(s, node, EXTRACTED, text, "extracted")
            elif "My cauldron has her fire" in text:
                node["Text"] = text.replace("My cauldron has her fire", "My cauldron is still waiting for her fire")
                variant(s, node, EXTRACTED, text, "extracted")
            elif "The cauldron has my spark now." in text:
                node["Text"] = text.replace("The cauldron has my spark now.", "My spark stayed in the corpse. A dead body's fire will not follow a thread into stolen flesh. Your mind is what holds me together now.")
                variant(s, node, EXTRACTED, text, "extracted")
            elif "Socothbenoth wanted my essence for his great joke. He has it" in text:
                node["Text"] = '"Socothbenoth wanted my essence for his great joke. It is still in the corpse. He can wait." {n}She rolls the cup between her palms.{/n}'
                taken = variant(s, node, EXTRACTED, '"The fire you took is in the syphon. You have it; do not start calling it his." {n}Her fingers tighten on the cup.{/n}', "extracted")
                passed = variant(s, taken, HANDED, '"You handed the syphon to his Council. My fire went with it. I shall enjoy collecting the rest of what he owes me."', "handed")
                variant(s, passed, SPENT, '"My fire burned at Threshold. His great joke has used it up. He had better hope I find the story amusing."', "spent")
            if id.endswith("ask") and "You went into her audience chamber" in node["Text"]:
                node["Text"] = '"Tell me what passed between you and my lady. Before the killing, or after. Do not invent an answer to make me easier to live with."'
                silent = next(a for a in node["Choices"] if a.get("Next", "").endswith("silent"))
                silent["Requires"].append(AUDIENCE)
                target = next(x for x in s["Nodes"] if x["Id"] == silent["Next"])
                absent = copy.deepcopy(target)
                absent["Id"] = id + "_never_went"
                absent["Text"] = '"You never spoke to her. Then there is no answer to pick apart." {n}The warmth behind your eyes contracts.{/n} "She will hear from me when I have a mouth again."'
                answer = copy.deepcopy(silent)
                answer["Requires"].remove(AUDIENCE)
                answer["Forbids"].append(AUDIENCE)
                answer["Next"] = absent["Id"]
                node["Choices"].append(answer)
                s["Nodes"].append(absent)
                target["Text"] = '"You spoke to her, but not about me. I heard no verdict. I will not call that mercy." {n}Her voice sharpens.{/n} "Nor will I call it leave to take her place."'
            if id.endswith("want"):
                for a in node["Choices"]:
                    if "You got into my head once, in your Harem" in a["Text"]:
                        a["Requires"].append(P + "let_in")
                        a2 = copy.deepcopy(a)
                        a2["Text"] = '"You. I want to see what you choose when you have a body again."'
                        a2["Requires"].remove(P + "let_in")
                        a2["Forbids"].append(P + "let_in")
                        node["Choices"].append(a2)
                        break
            if id.endswith("choose") and "You know only what she was: tall, on her throne" in text:
                node["Text"] = text.replace("You know only what she was: tall, on her throne, burning, her hand long and white against the red of her hair when she waved you away.", "Socothbenoth described the woman whose body his errand will destroy: tall, red-haired, with long hands. A description is all you have to choose by.")
            if id.endswith("cold") and "Dream as loud as you did in my Harem" in text:
                node["Text"] = text.replace("Dream as loud as you did in my Harem", "Dream loudly enough for me to find you")
            if id.endswith("noct") and "Nocticula never dreams. She never has." in text:
                node["Text"] = '"My lady enjoyed what I brought her: other people\'s dreams, their appetites, what they would kill to possess." {n}The remembered sky darkens.{/n} "I was her chosen lover. I still want her. But a voice behind your eyes cannot climb into her bed, and I will not remain a voice."'
            if id.endswith("look") and "You were thinking of it without knowing" in text:
                node["Text"] = '"My Harem\'s bathing room. I put the memory here." {n}She leans back on her hands; warm water slips from her ankles.{/n} "You are looking at me, Golarian. I have missed being looked at."'
            if id.endswith("put") and "I put nothing there" in text:
                node["Text"] = '"Yes. Mine, this time." {n}She trails her fingers through the water.{/n} "I can remember my own skin. That is a poor substitute for wearing it. Come closer."'
            if id.endswith("without"):
                node["Text"] = '"Less. My fire stayed behind when I fled. I can reach into your mind, but there is no body here to carry it." {n}The voice goes hard.{/n} "Find me flesh. I have spent enough time listening to your sentries piss outside this tent."'
            if id.endswith("barracks") and "That's the thing under the barley" in node["Text"]:
                node["Text"] = node["Text"].replace("That's the thing under the barley", "That is what you chose to give me")

    # SHA-01: a decoy offered in her existing duel, with her own counter-search.
    duel = by[P + "ch4.read"]
    recipes = next(x for x in duel["Nodes"] if x["Id"] == "recipes")
    recipes["Text"] = '{n}You hold an imagined crystal tally at the front of your thoughts, its numbers neatly arranged: a harmless decoy prepared for her search. Behind it, the private memory stays shut. Her attention catches on the neatness.{/n} "You rehearsed that. How considerate." {n}She tests behind the numbers, then encounters the recipes you piled over the closed thought. Her nails bite into the throne\'s arm.{/n} "Something worth hiding. Keep it, for now. I shall remember where you put it."'
    # SHA-02 is optional setup. Her response accepts refuge, never romance.
    setup = by[P + "killed.setup"]
    story = next(x for x in setup["Nodes"] if x["Id"] == "story")
    story["Choices"].append(c('[Warn Shamira through the open thread before entering the boudoir.]', "warning", flags=(P + "warned_before",)))
    setup["Nodes"].append(n("warning", "Shamira", '"His syphon. My fire." {n}Her reply burns along the thread. For a moment she tests the opening hard enough to make your eyes water.{/n} "Leave this open. If his errand succeeds, I shall take the way out you offered. Then you will find me flesh. Empty flesh, not one of your praying soldiers. And I shall decide what to do with it." {n}The pressure withdraws. Socothbenoth studies your expression.{/n}', c('"About the Fleshmarkets..."', "market"), portrait="Shamira"))

    for suffix in ("", "_awning"):
        visit = by[P + "after.visit" + suffix]
        nodes = {x["Id"]: x for x in visit["Nodes"]}
        # Companions are local witnesses; their absence never vetoes courtship.
        visit["Forbids"] = [f for f in visit["Forbids"] if f != "crossroute.arueshalae.unavailable"]
        for a in nodes["arueshalae"]["Choices"]:
            if a.get("Next") in ("aru_redeemed", "aru_evil"):
                a["Requires"].extend((ARU_PRESENT, ARU_EARNED))
                if a["Next"] == "aru_redeemed":
                    a["Forbids"].append(ARU_EVIL)
                else:
                    a["Requires"].append(ARU_EVIL)
        nodes["arueshalae"]["Choices"].append(c("Continue", "aru_evil",
            requires=(ARU_PRESENT, ARU_EARNED, ARU_EVIL),
            forbids=("arueshalae.evil_recruited", "arueshalae.evil_dead")))
        nodes["arueshalae"]["Choices"].append(c('[Return to her invitation.]', "aru_absent"))
        visit["Nodes"].append(n("aru_absent", "Shamira", '"Enough of your companions. I came here for you."', c("Continue", "next"), portrait="Shamira"))
        nodes["watching"]["Text"] = '"I came out of your wardrobe and sat on the bed. You moved toward the warmth before you woke." {n}She rests a finger against your forehead.{/n} "I used to look at sleepers through their dreams. Now I can watch your mouth as well. Much more distracting."'
        variant(visit, nodes["watching"], EDGE, '"I sat on your bed while I kept my back turned at the edge of your dream. I heard you moving in your sleep. I could not see what you made room for." {n}Her finger rests against your forehead.{/n} "I can look at you out here. You did not bar this door."', "edge")
        nodes["body"]["Text"] = '"The body is good. Hungry. Too fond of wine. Cold by dusk." {n}She stretches, drawing the gown tight across her breasts.{/n} "Your coal burns down. Then I come for another. My court has discovered it is dangerous to ask why their mistress visits a besieged city."'
        variant(visit, nodes["body"], EDGE, '"Cold by noon. Just as I told you." {n}She cups her wine between both hands.{/n} "I take my coal from the edge, with my back turned. My courtiers kiss these fingers and pretend not to notice. I know which ones are thinking about knives."', "edge")
        variant(visit, nodes["know"], TOLD, '"Your chaplains know. You told them." {n}She puts down the cup.{/n} "I said nobody would know why. You have made a liar of me. Let them pray over it; they cannot put the dreams back."', "told")
        nodes["barracks"]["Text"] = '"And the barracks." {n}Her eyes brighten.{/n} "They still drill. Still obey. But nothing stirs in them at night. Your surgeon has been following the officers, asking when it started. I wonder how long you will make him wait."'
        nodes["next"]["Text"] = '"Next time, my Harem. No court. One experiment: hide a thought from me, or offer it. If I find myself in it, I shall tell you what I want." {n}She leaves the cup on the wall and rises.{/n} "Will you come?"'
        nodes["kind"]["Text"] = '"One look. If you keep me out, allies. I do not ask twice." {n}She turns toward the alley.{/n} "You have not answered, Golarian. I shall leave the invitation where it is."'
        nodes["come"]["Text"] = '"Good." {n}Her thumb presses your lower lip before she lets you go.{/n} "Come awake. I want the thought you choose to show me."'
        nodes["come"]["Choices"][0]["Set"].append(ACCEPTED)
        # SHA-04: only a demonstrated defence earns the closed-memory callback.
        nodes["did"]["Text"] += '\n"Offer me one memory tonight. I shall see what you choose to leave open."'
        defended = variant(visit, nodes["did"], HID, '"You kept a thought behind those recipes in my Harem." {n}Her finger presses, meets the old resistance, then withdraws.{/n} "Still shut. Offer me another, then. I can take warmth without taking that."', "defended")
        defended["Choices"].append(c('[Offer the memory you shared on the wardrobe floor. Keep the other thought shut.]', "memory_offer"))
        visit["Nodes"].extend([
            n("memory_offer", "Narrator", '{n}You hold the offered memory in front of the thought she failed to take in her Harem. She tests the closed edge again. You hold it.{/n}',
              c("Continue", "memory_home", requires=(P + "last_dream.home",)),
              c("Continue", "memory_peace", requires=(P + "last_dream.peace",)),
              c("Continue", "memory_her", requires=(P + "last_dream.her",)),
              c("Continue", "memory_plain", forbids=(P + "last_dream.home", P + "last_dream.peace", P + "last_dream.her"))),
            n("memory_home", "Shamira", '"That kitchen. You showed me its door on the wardrobe floor." {n}Her attention turns toward the offered warmth.{/n} "I shall take what is in front of me tonight. I remember what you kept behind it."', c("Continue", "memory_answer"), portrait="Shamira"),
            n("memory_peace", "Shamira", '"The war finished. Your soldiers on the road home." {n}She tests the sunlight in the memory.{/n} "I shall warm my hands here tonight. Keep your other thought. You have made me curious about it again."', c("Continue", "memory_answer"), portrait="Shamira"),
            n("memory_her", "Shamira", '"My throne." {n}Her attention settles on the light you offered her on the wardrobe floor.{/n} "You knew what I wanted to see. I shall take this tonight. Your other thought can wait."', c("Continue", "memory_answer"), portrait="Shamira"),
            n("memory_plain", "Shamira", '"This one, then." {n}She leaves the closed thought and settles into the memory you offered.{/n} "I can return for this warmth. You will still have to keep the other door shut yourself."', c("Continue", "memory_answer"), portrait="Shamira"),
            n("memory_answer", "Shamira", '"Tonight, this memory. I have a court to keep waiting until then." {n}She lifts her hand from your forehead and takes up the cup.{/n}',
              c("Continue", "torn", requires=(P + "cost.shell_torn",)),
              c("Continue", "body", forbids=(P + "cost.shell_torn", EDGE)),
              c("Continue", "body_edge", requires=(EDGE,), forbids=(P + "cost.shell_torn",)), portrait="Shamira"),
        ])
        # The new invitation does not renegotiate a recorded nightly border.
        answer = next(x for x in visit["Nodes"] if x["Id"] == "memory_answer")
        variant(visit, answer, EDGE, '"Tonight I sit at its edge, with my back turned. The same poor coal." {n}She takes up the cup.{/n} "I chose to come back. You have not bought the rest of the memory by offering its warmth."', "edge")

        harem = by[P + "harem" + suffix]
        h = {x["Id"]: x for x in harem["Nodes"]}
        h["lost"]["Text"] = '{n}You lower the thoughts you used to hide her. You offer the desire beneath them without disguise.{/n} {n}Her mouth parts. She withdraws from your mind and holds out her hand.{/n} "That was deliberate. Come here, then. I have an answer of my own."'
        h["rise"]["Text"] = '{n}She rises. Her attention leaves your thoughts; the heat behind your eyes subsides. The wanting stays. She comes down to you and takes your mouth hard, pulling you against her until the throne\'s arm catches your hip.{/n} "No more hiding tonight."'
        h["morning"]["Text"] = '{n}Purple light lies across the dais. You wake under her gown. Shamira sits beside you, fastening a pin through her hair; a second pin lies by your shoulder. She retrieves it slowly, her fingers lingering against your bare skin.{/n} {n}Outside, a musician tries a string. She listens, then catches your mouth once more before rising.{/n}'
        h["watch"]["Text"] = '"I stayed. Do not look so pleased; it suited me." {n}She pulls the gown from your shoulder and wraps it around herself.{/n} "You gave me a thought last night. I enjoyed what followed it. That is what you may boast of."'
        variant(harem, h["watch"], EDGE, '"One offered thought. One night on my dais." {n}She fastens the gown over her breasts.{/n} "Your other dreams still have their border. Tonight I shall sit there with my back turned. My hands will be cold by noon. I have not forgotten what you told me."', "edge")
        for id, memory in (("last_home", "home"), ("last_peace", "peace"), ("last_her", "her")):
            h[id]["Text"] = {'home': '"The kitchen you showed me on the wardrobe floor. That door, that bread. I remember what you offered."', 'peace': '"Your war finished. A road without a demon waiting at the end. I remember the warmth, even if your officers have yet to earn the rest."', 'her': '"My throne, as you wanted to see it. I remember that. I mean to have more of it than this borrowed light."'}[memory]
        h["fool"]["Text"] = '{n}You bow low. Shamira lets the court laugh, then looks at the glabrezu behind the musicians.{/n} "My fool. Whoever spills this blood in my Harem will spend the next century wishing I had let them die." {n}The glabrezu lowers his eyes.{/n} {n}In your mind:{/n} "Be funny every visit. I supply the audience, and the threat. Outside these doors, watch your own back."'
        # Slot brief: willing first bodily encounter on the throne steps.
        cut = h["cut"]
        cut["Text"] = cut["Text"].replace("The heat behind your forehead becomes want. She tastes it and smiles.", "You catch her waist and draw her against you. She smiles against your mouth.")
        slot = n("explicit.1", "Narrator", '{n}Shamira draws you against her on the warm steps. Her mouth catches yours again; beyond the dais, the fountains keep running.{/n}', c("Continue", "morning"), portrait="Shamira")
        cut["Choices"][0]["Next"] = "explicit.1"
        harem["Nodes"].append(slot)

        throne = by[P + "after.throne" + suffix]
        t = {x["Id"]: x for x in throne["Nodes"]}
        t["ask"]["Choices"].append(c('"Rebuild your couriers. I will support your reach, while Nocticula keeps her throne."', "support", flags=(P + "throne_told", SUPPORT)))
        throne["Nodes"].append(n("support", "Shamira", '"The couriers who scattered when I died. You would help me find them, without helping me kill my lady." {n}She studies you over the cup.{/n} "Very well. Keep your limit. I shall reclaim the doors they used and make them answer to me again. No borrowed crown, no orders sent in your name." {n}Her smile sharpens.{/n} "My lady will have a useful steward. And an inconvenient one."', c("Continue", "socoth"), portrait="Shamira"))
        t["end"]["Text"] = '"The siege has given you nothing but maps to think about." {n}She finishes your wine and sets the cup down.{/n} "Sleep tonight. I shall come for what we agreed." {n}She turns into the alley.{/n}'

        alone = by[P + "after.night_alone" + suffix]
        a = {x["Id"]: x for x in alone["Nodes"]}
        a["offered"]["Text"] = '"You made my whole court watch you ask, only to give the night back." {n}She pulls you down onto the step beside her.{/n} "I shall use it. Tonight, the memory you offered on the wardrobe floor. I remember it."'
        a["read"]["Text"] = '"My fingers will stay white at the tips." {n}She flexes them slowly.{/n} "Every fool who kisses them will see it. You asked for one night. You took it. Tonight I come back for the coal we agreed. You may look at me while I warm these hands."'
        variant(alone, a["read"], EDGE, '"My fingertips will stay white. Tonight I come back to the edge, with my back turned. The same poor coal." {n}She lets you see the slow movement of her fingers.{/n} "One night alone has not bought you the rest, Golarian. Nor has it bought them for me."', "edge")

    _patrols(by)
    _inquiry(payload, by)
    _endings(by)
    _reactions(payload, by)
    _staging(own)
    _coda()

    for s in own:
        for node in list(s["Nodes"]):
            if node["Id"] == "voice":
                variant(s, node, P + "warned_before", '"You warned me. I tested the thread, and you held it open." {n}Her voice shakes with anger.{/n} "I took that way out. I have not forgotten whose hand killed the body I left. You offered me a refuge. Now make it worth having."', "warned")
            if node["Id"].endswith("mine") and 'Every night, for as long as this body lasts' in node["Text"]:
                node["Text"] += '\n"One missed night chills the flesh. It does not cut the thread. If your soul is held out of death and brought back, I can wait cold while it holds. No sleep, no warmth. If the soul is lost for good, the thread dies with it. Then this flesh empties. Do not test the difference for my amusement."'
            # The existing registered exclusive receipt supplies the current
            # bed decision. Generic whereabouts recount the prior claim,
            # rather than contradicting that receipt with a new present claim.
            for para in list(node.get("Paragraphs", [])):
                para["Text"] = para["Text"].replace("Shamira remained in the Harem of Ardent Dreams, Nocticula's chosen lover and ambitious steward.", "Shamira remained in the Harem of Ardent Dreams. Nocticula had once claimed her bed; her political claim to the ambitious steward survived.")
                para["Text"] = para["Text"].replace("Shamira's tie to her old lover stretched across that absence", "Shamira's political tie to her lady stretched across that absence")
                para["Text"] = para["Text"].replace("Shamira still wanted her old lover, and still wanted her throne", "Shamira still wanted her lady's throne")


def _coda():
    """Only Shamira's registered Last Call entry, before shared assembly."""
    from storylines import lastcall_partners
    part = next(x for x in lastcall_partners.PARTNERS if x["key"] == "shamira")
    updated = []
    for para in part["paragraphs"]:
        para = copy.deepcopy(para)
        if 'For three days after Threshold' in para["Text"]:
            para["Text"] = '{n}For three days the body went cold, but the thread held to the soul kept outside death. Shamira took no dreams from it. When the Commander returned, she came through the wardrobe with white fingertips and caught the living wrist.{/n} "Three days. Do not expect me to find that funny." {n}That night she took warmth under the bargain they had kept before the rift, then returned to her Harem and made the court wait while she warmed her hands.{/n}'
        if "She came to the Commander's funeral" in para["Text"]:
            para["Text"] = '{n}Shamira attended the burial of the empty coffin in a face nobody knew. Afterwards she returned through the wardrobe to the living Commander. She laughed at the priests\' promise of peace, then demanded her cup and an account of what the crusade had cost them.{/n}'
        para["Text"] = para["Text"].replace("Shamira still wanted her old lover, and still wanted her throne", "Shamira still wanted her lady's throne")
        updated.append(para)
    part["paragraphs"] = tuple(updated)


def _patrols(by):
    # Her dangerous inspiration becomes a Commander-owned military order.
    for s in by.values():
        for node in list(s["Nodes"]):
            if node["Id"] != "burn" or s["Id"] != P + "mind.dream":
                continue
            node["Text"] = '{n}You wake with the dream still burning: the road below Drezen, clear under a climbing dragon. On your map that road leads past the templars\' abandoned supply camp. Your officers ask whether to send a patrol.{/n}'
            # Retain the legacy Continue as navigation, with no order imposed.
            node["Choices"][0]["Next"] = "patrol"
            s["Nodes"].extend([
                n("patrol", "Narrator", '{n}The scout points to a ravine beyond the camp. Nobody has checked it since the last templar raid.{/n}',
                  c('[Send the patrol in daylight, with wagons.]', "patrol_day", flags=(P + "patrol.day",), crusade=("Materials", 150)),
                  c('[Send scouts after dark. Take only what they can carry.]', "patrol_night", flags=(P + "patrol.night",), crusade=("Materials", 50)),
                  c('[Reject the order. A dream is no reconnaissance.]', "patrol_refused", flags=(P + "patrol.refused",))),
                n("patrol_day", "Shamira", '"Wagons full, and two scouts dead in the ravine." {n}Her voice savours the report.{/n} "You saw the road I gave you. The templars saw your wagons. I did not promise an empty battlefield."', c("Continue", "morning_burned"), portrait="Shamira"),
                n("patrol_night", "Shamira", '"A few bundles, carried home in the dark. You made my splendid dream crawl on its belly." {n}She sounds offended.{/n} "Your scouts came back. I suppose you will call that a triumph."', c("Continue", "morning_burned"), portrait="Shamira"),
                n("patrol_refused", "Shamira", '"No patrol. No plunder." {n}The heat behind your eyes contracts.{/n} "You can leave a dream unfinished. I cannot make your officers march."', c("Continue", "morning_burned"), portrait="Shamira"),
            ])


def _inquiry(payload, by):
    # One military consequence, independent of romance closure or actor contact.
    primary = by[P + "mind.barracks_after"]
    for suffix in ("", "_awning"):
        s = by[P + "mind.barracks_after" + suffix]
        s["Forbids"] = list(dict.fromkeys(s["Forbids"] + list(SETTLED)))
    nodes = copy.deepcopy(primary["Nodes"])
    nodes[0]["Text"] = '{n}The north barracks\' surgeon intercepts you outside the command tent, with a chaplain behind him.{/n} "Two hundred men stopped dreaming on the same night. A sergeant has hanged himself. I need an answer, Commander."'
    rel = "shamira_barracks"
    payload["Relationships"][rel] = dict(Title="The north barracks", Description="Two hundred soldiers lost their dreams. The surgeon wants an answer.", Objective="Answer the surgeon", Guidance="The surgeon will find the Commander, even if Shamira has left.", StartedFlag=P + "cost.barracks", ClosedFlag=P + "barracks.settled", CommittedFlag=P + "barracks.inquiry_complete", UnavailableFlags=[], FailureFlags=[])
    for s in (primary, by[P + "mind.barracks_after_awning"]):
        for node in s["Nodes"]:
            for answer in node["Choices"]:
                if set(answer.get("Set", ())) & set(SETTLED):
                    answer["Set"].append(P + "barracks.settled")
    for node in nodes:
        node["Text"] = node["Text"].replace("He didn't write anything down, Commander", "The chaplain wrote nothing down, Commander")
        for answer in node["Choices"]:
            if set(answer.get("Set", ())) & set(SETTLED):
                answer["Set"].append(P + "barracks.settled")
    payload["Scenes"].append(scene(P + "mind.barracks_inquiry", "The north barracks", "Surgeon", 5, "", nodes,
        requires=("trickster.ever", P + "cost.barracks"), forbids=SETTLED, last=6,
        Relationship=rel, Chapters=[5, 6], Remote=True, Kind="event", delay=primary["DelayHours"]))


def _endings(by):
    kept = by[P + "epilogue.kept"]["Nodes"][0]
    kept["Text"] = '{n}The chroniclers recorded Shamira\'s death in the Lady in Shadow\'s bedchamber. They did not look behind the Commander\'s eyes. After the war, the Commander returned through the wardrobe and found her on the Harem\'s dais, dismissing petitioners. She kept one place empty beside her.{/n}'
    kept["Paragraphs"].extend([
        p('{n}Her essence burned in the syphon at Threshold. The woman on the throne had survived without that fire.{/n}', requires=(EXTRACTED, SPENT)),
        p('{n}Her celestial fire remained in the syphon; she did not mistake its possession for the life of her stolen body.{/n}', requires=(EXTRACTED,), forbids=(SPENT,)),
        p('{n}The corpse kept the fire she could no longer reach. Her borrowed flesh lived on the warmth she carried from the Commander\'s sleep.{/n}', forbids=(EXTRACTED,)),
        p('{n}The courier doors reopened under Shamira\'s hand. The Commander had offered support, not Nocticula\'s throne. Shamira reclaimed her contacts herself, and sent her lady reports that made it plain whose reach had grown.{/n}', requires=(SUPPORT,)),
        p('{n}One night the Commander had slept alone. Shamira returned the next evening with white fingertips that never quite warmed again. She kept showing them to her court.{/n}', requires=(P + "night_alone.taken",)),
        p('{n}A daylight patrol brought back the templars\' stores. Two scouts stayed in the ravine. Their names remained on Drezen\'s casualty roll.{/n}', requires=(P + "patrol.day",)),
        p('{n}The night scouts returned with what they could carry. Shamira never let the Commander forget how much plunder caution had left behind.{/n}', requires=(P + "patrol.night",)),
        p('{n}The Commander sent no patrol on the strength of her dream. No stores came back from that camp.{/n}', requires=(P + "patrol.refused",)),
    ])
    for para in kept["Paragraphs"]:
        if P + "court.fool" in para.get("Requires", ()):
            para["Text"] = '{n}Every visit to her Harem demanded a new performance from her fool. Shamira supplied the audience and made anyone reaching for a knife meet her eyes. Beyond her doors, the Commander still watched for assassins.{/n}'
        if "Wherever the Commander slept" in para["Text"]:
            para["Text"] = '{n}Shamira returned for the warmth that sustained her body, under the terms the Commander had actually offered. A place on her dais did not give her another door into their dreams.{/n}'
    drowned = by[P + "epilogue.drowned"]["Nodes"][0]
    drowned["Text"] = drowned["Text"].replace("the Abyss swallowed what the syphon had not wanted", "the Abyss swallowed the mind that had lost its hold")
    walked = by[P + "epilogue.walked"]["Nodes"][0]
    walked["Text"] = '{n}Shamira returned to her Harem in the stolen body. After the war she still came through the wardrobe for warmth, then went back to the petitioners and knives waiting in her city. Survival had settled nothing about whose bed the Commander might enter.{/n}'
    walked["Paragraphs"].extend([
        p('{n}She kept to the edge of the dream, with her back turned. By noon the borrowed hands were cold.{/n}', requires=(EDGE,)),
        p('{n}She entered the dreams left open to her, warming her hands before carrying a coal home.{/n}', forbids=(EDGE,)),
    ])
    late = by[P + "epilogue.late"]
    late["Nodes"][0]["Text"] = '{n}After Threshold, Shamira returned to the Commander\'s window. The wager in her Harem had never been played. She held out her hand and waited.{/n}'
    # Engine round 3 keeps this legacy romance page retired. We stage the
    # appended informed choice, but never evade its shared earned-payoff gate.
    late["Nodes"][0]["Choices"][1]["Text"] = '[Accept her wager. Offer her the thought you want her to find.]'
    won = next(x for x in late["Nodes"] if x["Id"] == "partner_late_won")
    won["Text"] = '{n}Afterwards, Shamira retrieved her pins from the steps. She kept one hand on the Commander\'s loosened coat while the musicians gathered outside. Her court would return at the third bell.{/n}'
    # Both saved aftermath exits keep their identity and exact mechanics.
    # The slot precedes this anchor on new affirmative partner paths.
    for node in late["Nodes"]:
        for answer in node["Choices"]:
            if answer.get("Next") == "partner_late_won":
                answer["Next"] = "late_initiation"
    late["Nodes"].append(n("late_initiation", "Narrator", '{n}The Commander offered the thought. Shamira withdrew from it, rose from her throne and caught the Commander\'s mouth. She slipped the pins from her hair and pulled the travelling coat open, then drew her lover down onto the warm steps.{/n}', c("Continue", "explicit.1"), portrait="Shamira"))
    slot = n("explicit.1", "Narrator", '{n}She pulls the loosened coat away and draws you down beside her. The fountains fill the empty Harem; the court has not yet returned.{/n}', c("Continue", "partner_late_won"), portrait="Shamira")
    late["Nodes"].append(slot)
    # Read-only unfinished invitation: asking about a game is never commitment.
    payload_scene = scene(P + "epilogue.invited", "", "ShamiraEpilogue", 6, "", [n("page", "Narrator", '{n}Shamira returned to the window after the war. Her wager had never been played; no thought had been offered for her to answer. She left the invitation open. The warmth that kept her flesh alive bought the Commander no welcome on her dais.{/n}')],
        requires=("trickster.ever", "shamira.present_now", P + "embodied", P + "game_proposed"),
        forbids=("shamira.committed", "shamira.closed", P + "ally", "sacrifice"), last=6, Relationship="shamira",
        ForbidOverrides={"sacrifice": "trickster.commander_back"})
    # Added by the caller below, through the shared list reference.
    by[P + "epilogue.invited"] = payload_scene


def _reactions(payload, by):
    # The companion hub establishes contact; present_now prevents phantom cameos.
    for key in ("inside", "inside_unseen", "walking"):
        old = by[P + "react.arueshalae_" + key]
        old["Forbids"].append(ARU_EVIL)
        evil = copy.deepcopy(old)
        evil["Id"] += "_corrupted"
        evil["AnswerLists"] = ["7d6ad178bd7a1ef4ca737ab167570c79"]
        evil["Requires"].append(ARU_EVIL)
        evil["Requires"].append("shamira.present_now")
        evil["Forbids"].remove(ARU_EVIL)
        evil["Nodes"][0]["Text"] = ('"The Ardent Dream has flesh again." {n}Arueshalae smiles, showing her teeth.{/n} "Tell her I can smell the borrowed warmth. She will know why I find it amusing."' if key == "walking" else
            '"Shamira, inside your head." {n}Arueshalae leans close, then laughs.{/n} "I wondered why you smelled like her Harem. Does she listen when you sleep with someone else? I could give her something to listen to."')
        payload["Scenes"].append(evil)
    payload["Scenes"].append(by[P + "epilogue.invited"])


def _staging(scenes):
    # Drezen has two outdoor contacts. Harem nodes stay on the actual dais.
    for s in scenes:
        if not any(x in s["Id"] for x in ("after.city", "after.visit", "after.throne")):
            continue
        for node in s["Nodes"]:
            for old, new in (
                ("come to her table", "reach her place by the wall"),
                ("pushes the other chair out with her foot", "moves her cup along the wall to make room"),
                ("her corner table", "her place at the tailor's row"),
                ("at her table", "by the wall"), ("across the table", "closer"),
                ("The King has given up pretending not to look.", "The tailor has given up pretending not to look."),
                ("stood in the door with her hand on the frame", "stopped at the end of the row"),
                ("in the King's doorway", "at the end of the row"),
                ("at the end of the street", "at the edge of the smith's yard"),
                ("the King's back door", "the alley beside the tailor's row"),
                ("from the table", "from the wall"), ("onto the chair", "onto the low wall"),
            ):
                node["Text"] = node["Text"].replace(old, new)

"""Authored partner terms, using Marhevok's native fates, not a new rescue.

Canon: JerribethReveal/Cue_0014 (52ada8be) calls his love blind and passionate;
Cue_0044 (7b9443fc) is his judged farewell. MarhevokTransformed/Cue_0001
(410114ed) gives the plant living eyes, never speech. JerribethGreetings/
Cue_0004_NewMarh (d9057361) says she can take him to the Abyss.

Authored additions: the living demon keeps the retained plant in her bedroom;
she shows the correspondence to him, or conceals it until her existing visit.
The returned tenant cannot bring him out of the Sanctum. No plant is restored,
killed or retrieved here. Earned exclusivity severs her lover's claim to the
bed; the living plant remains her possession. A memory pays for that choice.
The judged chief answers by letter and stays with his people. No reunion is
asserted. Unobserved fates remain unknown, including on a tenant history.
"""
import copy

from story_format import c, n, p

PREFIX = "jerribeth.partner_stance."
SHARE, EXCLUSIVE, SECRET = (PREFIX + x for x in ("share", "exclusive", "secret"))
READY = "jerribeth.partner_terms_chosen"
EXPOSED = "jerribeth.partner_secret_exposed"
REFUSED = "jerribeth.partner_exclusive_refused"
EARNED = "jerribeth.partner.exclusive_earned"
CHOSEN = "jerribeth.partner.exclusive_chosen"
CAREFUL = "jerribeth.partner.careful"
RETURNED = "jerribeth.trickster.returned"
PLANT = "jerribeth.marhevok_in_sanctum"
DEAD = "jerribeth.marhevok_dead"
CHIEF = "gesmerha.marhevok_rules"
FATES = (DEAD, CHIEF, PLANT)

# Verified in /wrath/blueprints.zip, not inferred from his absence. These use
# the existing read-only binder; no native etude is started or completed.
ETUDES = {
    PLANT: "4f87458c1e0d21c47b9269cd9dc727be",  # WintersunStory/Marhevok_InSunctum
    DEAD: "fc03aa45c96a1424680c505627db8144",   # WintersunStory/Marhevok_Dead
}


def fate_guards():
    """Death wins over stale plant custody. No false observer proves life."""
    return {
        "dead": dict(requires=(DEAD,)),
        "chief": dict(requires=(CHIEF,), forbids=(DEAD,)),
        "plant": dict(requires=(PLANT,), forbids=(DEAD, CHIEF, RETURNED)),
        "distant": dict(requires=(PLANT, RETURNED), forbids=(DEAD, CHIEF)),
        "unknown": dict(forbids=FATES),
    }


def j(id, text, *choices):
    return n(id, "Jerribeth", text, *choices, portrait="Jerribeth")


def terms_nodes(origins):
    resume = "partner_resume"
    guards = fate_guards()
    nodes = [j("partner_name", '''"One name before we make promises. Marhevok. The chief of Wintersun loved me so blindly that I began to find it interesting."
{n}Her laughter scratches at the inside of your ear.{/n}
"You are wondering whether your war has left room for another lover. I have never needed very much room."''',
        *(c('"And where is Marhevok now?"', "partner_" + fate, **guard)
          for fate, guard in guards.items()))]
    descriptions = {
        "plant": '''{n}Jerribeth turns the frame. Beside her bed stands a pot. A flower bud turns toward you, its pulsing flesh stretched around human eyes.{/n}
"Here. I brought him from the Sanctum. He wanted to be with me forever. I found a convenient shape."
{n}She strokes a leaf; the eyes follow her hand.{/n}
"He cannot speak. He can still look. I like to give him something worth looking at."''',
        "distant": '''"In his pot at the Ivory Sanctum, when I last had a body there. I did not carry him through a sword into your skull."
{n}The buzzing thins.{/n}
"I know what I left. I do not know who has watered it. Do not promise yourself a dead rival merely because he cannot knock on your door."''',
        "chief": '''"In Wintersun, making amends to his people. He said farewell to me under your judgment. Then he called me his sun."
{n}Her antennae incline.{/n}
"He left. His devotion was slower. I still enjoy pulling on it."''',
        "dead": '''"Dead. Whatever you offer me now will not change that."
{n}She examines the frame as if it had developed a flaw.{/n}
"He loved me with very little encouragement. You are considerably more trouble. I have not decided whether that makes you better value."''',
        "unknown": '''"I have no news of him that I shall sell as certainty. Wintersun has had enough of people seeing what they wanted to see."
{n}Her laugh is dry and high.{/n}
"He may still want me. You have heard his name now. You will not be able to call that a surprise."''',
    }
    share_texts = {
        "plant": '''{n}She tilts the frame until Marhevok's eyes catch your image.{/n}
"The Commander will keep coming. You will keep your place here. Look at me, Marhevok."
{n}The bud turns toward her. A vine tightens around the rim of the pot. Jerribeth draws the frame against her bare throat.{/n}
"There. He knows. You have seen his answer. Do not flatter yourself that either of us has made him happy."
{n}She leaves the pot beside her bed, facing the frame.{/n}''',
        "distant": '''"You will share what he still claims, if he lives. I cannot show you his eyes from here."
{n}Her voice presses close behind your own thoughts.{/n}
"Marhevok's silence buys you nothing, Commander. He has not heard this. If I get him back, he hears it before I put him beside a bed. Until then you have an absent rival, and I have an unattended possession."''',
        "chief": '''{n}At Jerribeth's prompting, the frame shows a letter bearing the Wintersun chief's mark. Her message lies beside it, naming you and what she wants from you.{/n}
"I know what you are now, my lady," {n}Marhevok has written.{/n} "Do not ask me to bless another lover. I will not follow you. My people have already paid for that."
{n}Jerribeth taps the last line with a claw.{/n}
"He has learned to refuse me something. How irritating. He stays in Wintersun. You do not get to mistake his farewell for a blessing."''',
        "dead": '''"There is no living Marhevok to agree to anything. You need not pretend you have been generous to him."
{n}Her hands close around the frame.{/n}
"I keep the memory. You get the evenings. Let us see what you do with them."''',
        "unknown": '''"Then if Marhevok is still alive, he is told. You have my promise of that, not his blessing."
{n}Her mouth opens in an insectile smile.{/n}
"I will not swear that he will enjoy hearing it. You may discover that he has better taste than you."''',
    }
    secret_texts = {
        "plant": '''{n}Jerribeth draws a curtain between the frame and the pot. Marhevok's eyes follow it until the cloth shuts him out.{/n}
"He will see me waiting for you. He will not see who comes. For a while."
{n}She holds your image against her mouth, behind the curtain.{/n}
"Do not mistake a flower for a fool. If you come to my bed, you may find it difficult to stay invisible."''',
        "distant": '''"I cannot tell him from here. You would like that to remain convenient."
{n}Her laughter buzzes behind your left eye.{/n}
"If he lives, his ignorance is part of your bargain. It will not become his agreement merely because we keep it long enough."''',
        "chief": '''"He has said farewell. You would still rather he did not know who takes his evenings. How greedy."
{n}She lays a claw across the Wintersun chief's name.{/n}
"Very well. I shall leave your name out. Do not expect me to stay discreet if I find his jealousy more entertaining."''',
        "dead": '''"You cannot deceive a corpse about whose bed I use. I can keep your name from the living, if that is what you want."
{n}Her voice lowers.{/n}
"Marhevok is dead. Do not dress your secrecy up as an affair with his ghost."''',
        "unknown": '''"We keep your name out of anything that might reach Marhevok. That is what you are buying."
{n}She watches your face.{/n}
"If he lives, you have chosen to deceive him. If he is dead, you have chosen to hide from somebody else. Neither choice makes me yours alone."''',
    }
    for fate, text in descriptions.items():
        nodes.append(j("partner_" + fate, text,
            c('"He keeps his place. Tell him about me."', "partner_share_" + fate),
            c('"End it with him. I want you to myself."', "partner_demand_" + fate),
            c('"Keep my name from him. These evenings are ours."', "partner_secret_" + fate)))
        nodes.append(j("partner_share_" + fate, share_texts[fate],
            c('"I know what I am accepting. Continue."', resume, flags=(SHARE, READY))))
        nodes.append(j("partner_secret_" + fate, secret_texts[fate],
            c('"Then keep it quiet."', resume, flags=(SECRET, READY))))
        nodes.append(j("partner_demand_" + fate, '''{n}Jerribeth laughs hard enough to make the image shiver.{/n}
"My possessions are not yours to dispose of. Not even the ones I have lost. You want to give me orders? Baphomet tried that, with rather more to offer."
{n}Her laughter stops.{/n}
"Take the evenings I offered, openly or quietly. Or close the frame. I will not clear my shelves to make room for your pride."''',
            c('"Then we tell him, if he lives. I will share."', "partner_share_" + fate),
            c('"Keep it secret, then."', "partner_secret_" + fate),
            c('"I meant what I said. We are finished."', "partner_refused",
              flags=(EXCLUSIVE, REFUSED))))
    nodes.append(j("partner_refused", '''{n}She turns the frame away. You hear a sharp scrape, then nothing.{/n}
"There. You have all of your evenings back. Spend one of them wondering what you thought you owned."''',
        c('[Close the correspondence.]', flags=("jerribeth.closed", "jerribeth.trickster.parted"))))
    nodes.append(j(resume, '"Now. What were you going to promise me?"',
        *(c('[Return to the offer.]', "partner_continue_" + origin, requires=(receipt, READY))
          for origin, receipt in origins.items())))
    # Authored severance of a lover's claim, not a change to Marhevok's fate.
    for fate in descriptions:
        offer = next(node for node in nodes if node["Id"] == "partner_" + fate)
        offer["Choices"][1]["Next"] = "partner_answer_" + fate
        answer = [c("Continue", "partner_demand_" + fate)]
        if fate in ("plant", "chief", "dead"):
            answer[0]["Forbids"].extend((EARNED,))
            answer.append(c("Continue", "partner_choose_" + fate, requires=(EARNED,)))
            reaction = {
                "plant": '''{n}She lifts the pot. A vine catches her wrist; she cuts it off and lets it fall.{/n}
"You have given me something worth keeping. I can clear a bedroom."
{n}She carries Marhevok beyond the curtain. His eyes follow her; the bud shuts when she leaves him on a shelf.{/n}
"Alive. Mine. But no longer my lover, and no longer beside my bed. Do not mistake that for mercy."
{n}Her claw taps the frame.{/n} "One memory of yours in exchange. I choose when. You have heard how I collect."''',
                "chief": '''"You have given me something I want. I have told Marhevok I shall not ask for his devotion again."
{n}She reads his reply aloud.{/n}
"Then leave my people alone too," {n}he has written.{/n} "I will not answer another summons."
{n}She laughs.{/n} "He thinks he has dismissed me. Let him. You owe me one memory instead. My choice, when I collect."''',
                "dead": '''"Marhevok is dead. I cannot give you his dismissal. I can give you mine: no other lover while our promise holds."
{n}Her laugh scratches inside your ear.{/n} "You have made yourself useful, and rather harder to replace. One memory, Commander. My choice. I shall take it when it hurts."''',
            }[fate]
            nodes.append(j("partner_choose_" + fate, reaction,
                c('"I accept the claim. Keep your promise."', resume,
                  flags=(EXCLUSIVE, READY, CHOSEN, "jerribeth.partner.exclusive_memory_owed")),
                c('"Keep him. I will share instead."', "partner_share_" + fate)))
        nodes.append(j("partner_answer_" + fate, '"Let me consider what you have given me, Commander."', *answer))
        secret = next(node for node in nodes if node["Id"] == "partner_secret_" + fate)
        secret["Choices"].append(c('[Keep to the closed frame. No names in letters, no invitation to your bed.]', resume,
                                   flags=(SECRET, READY, CAREFUL)))
    return nodes


def install_terms(scene, entry_nodes, late=False):
    """Append entry twins; preserve every old answer, effect and destination.

    Entry receipts select an appended copy of the original offer, avoiding a
    dialogue cycle. Mid-scene saves get the same fallback before commitment.
    """
    origins = {}
    continuations = []
    for node in list(scene["Nodes"]):
        commits = [ch for ch in node["Choices"] if "jerribeth.committed" in ch["Set"]]
        if late and node["Id"] == "offer":
            commits += [ch for ch in node["Choices"] if ch.get("Next") in ("signed", "signed_mind")]
        if node["Id"] in entry_nodes or commits:
            receipt = "jerribeth.partner_origin." + scene["Id"].split("jerribeth.")[1] + "." + node["Id"]
            origins[node["Id"]] = receipt
            if node["Id"] in entry_nodes:
                eligible = list(node["Choices"])
            else:
                eligible = commits
            continuation = copy.deepcopy(node)
            continuation["Id"] = "partner_continue_" + node["Id"]
            # The copied offer has a new diagnostic identity. Name the stolen
            # host explicitly; this pronoun never referred to the Commander.
            for paragraph in continuation.get("Paragraphs", []):
                paragraph["Text"] = paragraph["Text"].replace(
                    "He sat down at the Commander's table without being asked, and her voice came out of him, high and pleased.",
                    "The host sat down at the Commander's table without being asked. Jerribeth's voice came from the stolen mouth, high and pleased.")
            continuations.append(continuation)
            for choice in eligible:
                twin = copy.deepcopy(choice)
                choice["Requires"] = [*choice["Requires"], READY]
                twin["Next"] = "partner_name"
                twin["Set"] = [receipt]
                twin["Forbids"] = [*twin["Forbids"], READY]
                twin.pop("Check", None)
                twin["Abort"] = False
                node["Choices"].append(twin)
    scene["Nodes"].extend(terms_nodes(origins))
    scene["Nodes"].extend(continuations)


def install_discovery(scene, node_ids):
    """Existing invitations expose secrecy; no extra delivery or eligibility gate."""
    origins = {}
    continuations = []
    reviewed = "jerribeth.partner_secrecy_reviewed." + scene["Id"]
    for node in list(scene["Nodes"]):
        if node["Id"] not in node_ids:
            continue
        receipt = "jerribeth.partner_discovery_origin." + scene["Id"] + "." + node["Id"]
        origins[node["Id"]] = receipt
        continuation = copy.deepcopy(node)
        continuation["Id"] = "partner_discovery_continue_" + node["Id"]
        continuations.append(continuation)
        for choice in list(node["Choices"]):
            twin = copy.deepcopy(choice)
            # The ordinary answer stays at its old index, with an appended
            # equivalent after discovery. The third twin takes the exposure.
            choice["Forbids"] = [*choice["Forbids"], SECRET]
            exposed = copy.deepcopy(twin)
            exposed["Requires"] = [*exposed["Requires"], SECRET, EXPOSED]
            node["Choices"].append(exposed)
            twin["Next"] = "partner_discovery"
            twin["Set"] = [receipt]
            twin["Requires"] = [*twin["Requires"], SECRET]
            twin["Forbids"] = [*twin["Forbids"], EXPOSED]
            # Accepting the existing bodily invitation breaks frame-only secrecy.
            # A private correspondence continuation is appended below.
            node["Choices"].append(twin)
    if not origins:
        return
    for origin in origins:
        node = next(node for node in scene["Nodes"] if node["Id"] == origin)
        private = copy.deepcopy(continuations[list(origins).index(origin)])
        private["Id"] = "partner_private_" + origin
        private["Text"] = '''"No names in letters, no account of my bed. I shall talk to you and get nothing better for my trouble. How dreary."
{n}Her laugh scratches inside your ear.{/n}
"You may still entertain me, Commander. Tell me which demon your scouts caught lying today. I shall keep the letters unsigned. You keep this evening to conversation."'''
        # A quiet evening ends at this receipt; it cannot run into the bodily visit.
        private["Choices"] = ([c('[Keep the evening to conversation.]', "collected")]
                              if scene.get("Owner", "").endswith("Epilogue") else
                              [c('[Keep the evening to conversation.]', flags=(scene["Id"], "jerribeth.trickster.visited"))])
        scene["Nodes"].append(private)
    nodes = [j("partner_discovery", '"Before you come closer. Something you asked me to keep quiet."',
        *(c('"What have you done?"', "partner_exposed_" + fate, **guard)
          for fate, guard in fate_guards().items()))]
    texts = {
        "plant": '''{n}Jerribeth sets a covered pot on the floor. She has carried it beneath her folded wings. When she pulls the cloth away, human eyes stare at you from a flower bud. A vine strikes the correspondence frame and coils around it.{/n}
"He has been watching me wait. I grew tired of turning him to the wall. I brought him along."
{n}She prises the vine loose. A claw cuts it; dark sap streaks the frame. The bud turns away from her hand.{/n}
"He knows who gets the evenings now. There goes your convenient little secret."''',
        "chief": '''{n}Jerribeth opens a letter across the frame. Your name stands beside the Wintersun chief's mark.{/n}
"Do not send me another account of your bed, my lady. I have work here. Let the Commander answer your summons. I will not."
{n}She folds it slowly.{/n}
"He no longer answers my messages. I put your name in the last one. Your discretion has cost me a very faithful fool."''',
        "distant": '''"Marhevok's pot is still beyond my reach. I have no answer from him. There is nobody here to overhear us."
{n}The voice behind your eye sharpens.{/n}
"That is ignorance, Commander. Keep the word straight. If he lives, this still has not been put to him."''',
        "dead": '''"Marhevok is dead. There will be no jealous knock at this door from him."
{n}She studies you.{/n}
"You can stop pretending our secrecy spares him something. Who else are you hiding from?"''',
        "unknown": '''"No news of Marhevok. No answer to the question of who might learn your name."
{n}Her laugh rasps against the frame.{/n}
"I could tell you he is dead and watch you relax. You would pay handsomely for that lie, I think."''',
    }
    for fate, text in texts.items():
        actual = fate in ("plant", "chief")
        nodes.append(j("partner_exposed_" + fate, text,
            c('"You broke our bargain. I am leaving."', "partner_discovery_part",
              flags=((EXPOSED, "jerribeth.partner_exposure." + fate) if actual else ())),
            c('"Open the frame. I am staying."', "partner_discovery_resume",
              flags=((EXPOSED, "jerribeth.partner_exposure." + fate) if actual else (reviewed,)))))
    nodes.append(j("partner_discovery_part", '"Then go. I will not chase you through a closed frame."',
        c('[Leave her.]', flags=("jerribeth.closed", "jerribeth.trickster.parted"))))
    nodes.append(j("partner_discovery_resume", '"You will not ask me to call this forgiven. Come closer, if you still want me."',
        *(c('[Return to her invitation.]', "partner_discovery_continue_" + origin, requires=(receipt,))
          for origin, receipt in origins.items())))
    # Distant/dead/unknown review cannot make an unseen partner discover an
    # affair. It is a separate receipt allowing the original scene to proceed.
    for node in scene["Nodes"]:
        if node["Id"] in origins:
            for choice in list(node["Choices"]):
                if choice.get("Next") == "partner_discovery":
                    choice["Forbids"].append(reviewed)
                elif EXPOSED in choice["Requires"]:
                    twin = copy.deepcopy(choice)
                    twin["Requires"] = [r for r in twin["Requires"] if r != EXPOSED] + [reviewed]
                    twin["Forbids"].append(EXPOSED)
                    node["Choices"].append(twin)
    scene["Nodes"].extend(nodes)
    scene["Nodes"].extend(continuations)


def install_shared_witness(scene, node_ids):
    """Her existing physical visit brings the portable captive, not a new actor."""
    witnessed = "jerribeth.partner_witness." + scene["Id"]
    guard = fate_guards()["plant"]
    for node in list(scene["Nodes"]):
        if node["Id"] not in node_ids:
            continue
        origin = "jerribeth.partner_witness_origin." + scene["Id"] + "." + node["Id"]
        continuation = copy.deepcopy(node)
        continuation["Id"] = "partner_shared_continue_" + node["Id"]
        # The discovery twins are for a different stance. Shared continuations
        # keep the original invitation's ordinary answers only.
        continuation["Choices"] = [ch for ch in continuation["Choices"]
                                   if SECRET not in ch.get("Requires", ())]
        # A fallback answer covers all histories except the one with a living
        # plant, an open stance, and no witness yet. All twins remain appended.
        for choice in list(node["Choices"]):
            if SECRET in choice.get("Requires", ()):
                continue
            base = copy.deepcopy(choice)
            choice["Forbids"] = [*choice["Forbids"], SHARE]
            for fate, state_guard in fate_guards().items():
                twin = copy.deepcopy(base)
                twin["Requires"] = [*twin["Requires"], SHARE, *state_guard.get("requires", ())]
                twin["Forbids"] = [*twin["Forbids"], *state_guard.get("forbids", ())]
                if fate == "plant":
                    twin["Requires"].append(witnessed)
                node["Choices"].append(twin)
            twin = copy.deepcopy(base)
            twin["Requires"] = [*twin["Requires"], SHARE, *guard["requires"]]
            twin["Forbids"] = [*twin["Forbids"], *guard["forbids"], witnessed]
            twin["Next"] = "partner_witness_" + node["Id"]
            twin["Set"] = [origin]
            node["Choices"].append(twin)
        scene["Nodes"].append(j("partner_witness_" + node["Id"], '''{n}Jerribeth unwraps a pot she carried beneath her wings. The flower's human eyes turn toward you. A vine tightens around the rim.{/n}
"Still with me, Marhevok. You remember the Commander."
{n}She sets him where he can see the bed, then draws you close by the collar. Her claws catch the bare skin at your throat.{/n}
"He keeps his place. You wanted yours. Here it is."''',
            c('[Stay with her.]', continuation["Id"], requires=(origin,), flags=(witnessed,))))
        scene["Nodes"].append(continuation)


def partner_paragraphs(aeon=False, closed=False):
    if aeon:
        return [
            p("{n}The erased correspondence could grant no claim over Marhevok. His devotion to the Lady of the Sun belonged to the history that had been undone; whether either remembered it was unknown.{/n}"),
            p("{n}The promise to share Jerribeth's evenings belonged to the erased history. It could give Marhevok no knowledge of the Commander in the new world.{/n}", requires=(SHARE,)),
            p("{n}The Commander's demand for Jerribeth alone, and her refusal, had been erased with the correspondence. Neither could bind Marhevok in the new world.{/n}", requires=(EXCLUSIVE,)),
            p("{n}The secret evenings were gone with the history that had held them. They could neither betray Marhevok anew nor leave a memory of the Commander.{/n}", requires=(SECRET,)),
        ]
    texts = {
        "dead": "Marhevok remained dead. Jerribeth still named the Wintersun chief when she spoke of things she had lost; none of her later lovers replaced him in that account.",
        "chief": "Marhevok remained chief in Wintersun, apart from Jerribeth by his own farewell. She had not brought him back to her bed or made his people's debts disappear.",
        "plant": "Marhevok remained alive in his pot beside Jerribeth's bed. His human eyes followed her. She had kept her lover; she had not given him back his voice.",
        "distant": "Marhevok's last known place was his pot in the Ivory Sanctum. Jerribeth's lease in the Commander's skull brought no plant with it. No later word established whether he survived there.",
        "unknown": "Marhevok's fate remained unknown. Jerribeth named him without producing news; the silence did not establish his death, his agreement, or a place in anyone's bed.",
    }
    paragraphs = [p("{n}" + text + "{/n}", **guard)
                  for fate, guard in fate_guards().items() for text in (texts[fate],)]
    plant = paragraphs[2]
    plant["Forbids"].append(CHOSEN)
    paragraphs.append(p("{n}Marhevok lived in his pot on a shelf beyond Jerribeth's bedroom curtain. She had cut the vine that caught her wrist when she carried him there. He remained her captive possession; she had ended his place beside her bed.{/n}", requires=(PLANT, CHOSEN), forbids=(DEAD, CHIEF, RETURNED)))
    paragraphs += [
        p("{n}The Commander had chosen to share her evenings. That bargain kept Marhevok's claim in view; it did not make his captivity willing or his farewell an invitation to return.{/n}", requires=(SHARE,)),
        p("{n}The demand for Jerribeth alone had met her refusal. She kept her possessions and her memories; the Commander lost her evenings.{/n}", requires=(EXCLUSIVE, REFUSED)),
        p("{n}Jerribeth had severed Marhevok's claim to her bed, without changing his fate. She kept the Commander alone as her lover, and the promised memory as her price. She named that debt whenever the Commander spoke as though the bargain had made her obedient.{/n}", requires=(EXCLUSIVE, CHOSEN)),
        p("{n}The Commander had chosen secrecy. Jerribeth had kept their name out of her accounts of those evenings; no answer from Marhevok had been received.{/n}", requires=(SECRET,), forbids=(EXPOSED,)),
        p("{n}The secret had been exposed. Marhevok had struck the frame with a vine; Jerribeth had cut it loose. The sap dried on the frame. She never cleaned it off for the Commander.{/n}", requires=(SECRET, EXPOSED, "jerribeth.partner_exposure.plant")),
        p("{n}Jerribeth had exposed the secret in a message to Marhevok. The Wintersun chief refused to receive another account of her bed. She kept Marhevok's letter. No more came. The Commander was left with the lover who had broken their bargain.{/n}", requires=(SECRET, EXPOSED, "jerribeth.partner_exposure.chief")),
        p("{n}No arrangement with Marhevok had been settled. Jerribeth's unfinished correspondence did not settle it in his absence.{/n}", forbids=(SHARE, EXCLUSIVE, SECRET)),
    ]
    if closed:
        for block in paragraphs:
            block['Text'] = block['Text'].replace('The Commander was left with the lover who had broken their bargain.',
                'She had broken their secrecy before the later parting. The letter remained with her; the Commander no longer shared her evenings.')
            block['Text'] = block['Text'].replace('She kept the Commander alone as her lover, and the promised memory as her price.',
                'The Commander had been her sole lover while that promise lasted. The later parting ended that claim; the memory owed for breaking with Marhevok remained its own account.')
            block['Text'] = block['Text'].replace('She named that debt whenever the Commander spoke as though the bargain had made her obedient.',
                'The later parting forgave none of that earlier price.')
    return paragraphs


def integrate(payload):
    payload.setdefault("Etudes", {}).update(ETUDES)
    payload.setdefault("Derived", {})[EARNED] = [["trickster.now", flag] for flag in
        ("jerribeth.shared_work", "jerribeth.counter_spoils_settled", "jerribeth.trickster.cost.forfeit")]
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    install_terms(scenes["jerribeth.future"], {"future_entry"})
    install_terms(scenes["jerribeth.trickster.epilogue.commit"], set(), late=True)
    install_discovery(scenes["jerribeth.trickster.visit"], {"arrival_terms"})
    install_discovery(scenes["jerribeth.future"], {"tenant_room"})
    install_discovery(scenes["jerribeth.trickster.epilogue.commit"], {"signed", "signed_mind"})
    install_shared_witness(scenes["jerribeth.trickster.visit"], {"arrival_terms"})
    install_shared_witness(scenes["jerribeth.trickster.epilogue.commit"], {"signed"})
    # Add precaution answers after the older discovery/witness appenders, keeping
    # every answer they exported in merge-b10 at its original index.
    for event in (scenes["jerribeth.future"], scenes["jerribeth.trickster.visit"], scenes["jerribeth.trickster.epilogue.commit"]):
        pages = {node["Id"]: node for node in event["Nodes"]}
        for key in list(pages):
            if key.startswith("partner_private_"):
                origin = key.removeprefix("partner_private_")
                pages[origin]["Choices"].append(c('[Keep the evening private. No account of your bed reaches Marhevok.]', key,
                                                  requires=(SECRET, CAREFUL), forbids=(EXPOSED,)))
    for scene in payload["Scenes"]:
        if scene.get("Relationship") == "jerribeth" and scene.get("Owner", "").endswith("Epilogue"):
            for node in scene["Nodes"]:
                node.setdefault("Paragraphs", []).extend(partner_paragraphs(scene["Owner"] == "AeonEpilogue", closed=scene["Id"] == "jerribeth.ending_apart"))
    # Last Call builds these pages later. Modify ONLY Jerribeth's named record,
    # in her route integrator; shared Last Call source and gates stay untouched.
    from storylines import lastcall_partners
    part = next(x for x in lastcall_partners.PARTNERS if x["key"] == "jerribeth")
    additions = partner_paragraphs()
    if not any(x.get("Requires") == [EXCLUSIVE, REFUSED] for x in part["paragraphs"]):
        part["paragraphs"] = (*part["paragraphs"], *additions)

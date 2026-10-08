"""Authored Wenduag echo, allocated in 06-ROUTE-REGISTRY, Wenduag's Chapter 4 slot.
Approved pilot-echo-wenduag-v2 and its eight design-review defects govern this unit.
Native evidence: MongrelsDefeated/Cue_0001 and LannQ2_WenduagAttackAndDie.
The hook interrupts a second attack, never resurrects a dead actor or buys affection.
WenduagEcho.cs retains the original UniqueId and supplies observational availability.
Shyka's paid page is required through the public foresight key.
TODO destination: WenduagEcho.TODO_VerifiedCellarPosition needs the navigation check
described in tests/wenduag-echo-acceptance.md before return can become available.
"""
import copy

from story_format import c, n, p, scene
from storylines import foresight

E = "wenduag.trickster.echo.abyss."
W = "wenduag.trickster."
UNIT = "ae766624c03058440a036de90a7f2009"
LANN = "cb29621d99b902e4da6f5d232352fbda"
HUB = "66385ad77fa743e4bb1234078dbd804c"
BACK = "dd70b574d7afd99409b5c664b8c5bfe4"
DREZEN = "2570015799edf594daf2f076f2f975d8"
PAGE = foresight.PAGE_TAKEN
RUNTIME = tuple(E + s for s in (
    "adapter_available", "casualty_available", "return_available", "valid", "unavailable"))
CLOSURES = ("wenduag.killed", "wenduag.kicked_out", "wenduag.closed",
            "wenduag.q3_killed", "wenduag.q3_sent_away", "wenduag.hello_sent_away",
            "wenduag.hello_attacked", W + "native")
LANN_GONE = ("lann.dead", "lann.kicked_out", "lann.plot_absent")


def nar(id, text, *choices):
    return n(id, "Narrator", text, *choices)


def authored(id, title, chapter, entry, nodes, requires=(), forbids=(), **extra):
    return scene(E + id, title, "Wenduag", chapter, entry, nodes,
                 requires=("trickster.now", PAGE) + tuple(requires),
                 forbids=CLOSURES + tuple(forbids), last=chapter,
                 Relationship="wenduag", Remote=False, optional=True, delay=0,
                 EntryMythic=None if extra.get("InteractionHub") else "PlayerIsTrickster", **extra)


SCENES = [authored("prepare", "The second attack", 4,
    '[Follow the scrape that interrupts Lann\'s voice.] "Say that again."', [
    nar("start", '''{n}White steps. Lann's back. Wenduag rushes past a body already wearing her face.
Something catches at her waist. For a blink, you see the underside of her chin.{/n}
{n}"Still standing, cave rat?" Her voice comes through a mouth full of water.
Then Lann is beside you again, alive, impatient, with the noise of Alushinyrra beyond the camp.{/n}''',
        c("[Perception 24] Watch the rush again.", check=dict(Skill="SkillPerception", DC=24, Success="read", Failure="wrong")),
        c('"Forget it."', abort=True)),
    n("read", "conversant", '''"She lost, and went for me anyway? Sounds like Wendu.
She can swallow defeat from somebody stronger. From me, she'd choke on it."''',
        c('"Show me how she would come at you. I\'ll buy something to catch her with."', "practice", flags=(E + "seen",), crusade=("Finances", -150)),
        c('"A guess isn\'t worth your throat."', flags=(E + "seen", E + "abandoned"))),
    nar("wrong", '''{n}You remember the white stair better than the woman.
Somewhere in this city, surely, that stair exists.{/n}''',
        c("[Pay a runner fifty to find it.]", "empty", flags=(E + "seen", E + "misread"), crusade=("Finances", -50)),
        c('"The place may be wrong. Lann, show me the attack."', "practice", flags=(E + "seen",), crusade=("Finances", -150)),
        c("[Dismiss the glimpse.]", flags=(E + "seen", E + "abandoned"))),
    nar("empty", '''{n}The runner returns with white dust and three addresses.
At every stair he describes, the landing is too narrow. He has spent your money already.{/n}
{n}Lann snorts. "Next time pay him to find Wendu's good intentions. He can keep looking forever."{/n}''',
        c('"Enough stairs. Show me how she fights."', "practice", crusade=("Finances", -150)),
        c("[Send him away.]", flags=(E + "abandoned",))),
    n("practice", "conversant", '''{n}The first shaft snaps against Lann's belt.
The seller replaces it with ash, binds the hook in leather, and charges for both.
Lann shows you his guess again. You wait beside him, catch the belt, turn the shaft.
This time his feet leave the ground.{/n}
"If she comes at me, I'm hitting her. And if your clever stick misses, I'm hitting her again.
You want her breathing, you do the catching."''',
        c('"Keep yourself alive. I\'ll take the side of her rush."', flags=(E + "ready",))),
], requires=("lann.in_party", E + "adapter_available"),
    forbids=(E + "seen", "wenduag.abyss_fell", "wenduag.dead_any", W + "returned", W + "fall_agreed") + LANN_GONE,
    AnswerLists=[HUB], NativeReturnCue=BACK),
authored("pickup", "The hooked shaft", 4, "[Kneel beside Wenduag.]", [
    nar("start", '''{n}Her belt has torn halfway through. The shaft still holds her down.
Lann stands beyond her reach, watching the hook as though it has caught something in him too.{/n}''',
        c("Continue", "misread", requires=(E + "misread",)),
        c("Continue", "bind", forbids=(E + "misread",))),
    nar("misread", "{n}No white stair. Fifty gone for nothing.{/n}", c("Continue", "bind")),
    nar("bind", "{n}Blood seeps through her leathers. Her breath catches, then comes again.{/n}",
        c("[Bind the wound. Keep her death as the enemy's story.]", "hidden"),
        c("[Bind the wound openly.]", "open")),
    nar("hidden", '''{n}Lann watches you cover her face from the demon's followers.{/n}
{n}"We rehearsed the catching. Not this funeral. His people can take their story home.
Mine hear the truth from me. I'm not telling Sull she died while you carry her off."{/n}''',
        c("[Finish the dressing.]", "shelter", flags=(E + "cost.used_lann",))),
    nar("open", '''{n}Lann watches you bind her side.{/n}
{n}"Good. Let them see her breathing. I helped you catch her; I know what we agreed.
Keep that knife away from her hand until we're clear. I haven't agreed to a third attack."{/n}''',
        c("[Finish the dressing.]", "shelter", flags=(E + "cost.used_lann",))),
    nar("shelter", '''{n}You work a healing draught between her teeth.
When her breathing steadies, you ease the shaft free. Her hand closes on the broken belt.
You drag her behind fallen masonry, clear space around her face, and cover her with your cloak.{/n}''',
        c("[Arrange food, concealment and passage with your supplies. Bring her back when you leave.]",
          flags=(E + "rescued",), crusade=("Finances", -150)),
        c("[Leave her under the cloak for now.]", abort=True)),
], requires=(E + "ready", E + "casualty_available", "wenduag.abyss_fell"), forbids=(E + "rescued",),
    ContactUnit=UNIT, InteractionHub="wenduag.echo", TricksterDevice=True, TricksterState="echo_abyss"),
authored("return", "The torn belt", 5, "[Approach the hunter at the cellar door.]", [
    n("start", "Wenduag", '''{n}She has hung the torn belt over a nail beside the cellar door. Her knife lies across her knees.
A low bed of loose stones lies beside the stair down. White dust clings to her fingers.{/n}
"You dragged me away from him. I was going to kill Lann.
Don't look pleased with yourself. That hasn't changed."''',
        c('"I wanted you alive. What you do with that is yours."', "stay"),
        c('"You chose Savamelekh. I chose where you fell."', "stay"),
        c('"Leave Drezen."', flags=("wenduag.closed",)), speaker_unit=UNIT),
    n("stay", "Wenduag", '''"A hook. All his promises, all your fine soldiers, and I lost to a hook."
{n}Her teeth show. She takes the belt down and threads it through her fingers.{/n}
"I'll stay. I want to see what you catch next.
And when I come at you, uplander, I'll remember to cut the belt first."''',
        c('"Then keep the knife sharp."', flags=(E + "returned", W + "returned", "wenduag.started", W + "primed")), speaker_unit=UNIT),
], requires=(E + "rescued", E + "return_available"), forbids=(E + "returned",), Areas=[DREZEN],
    ContactUnit=UNIT, InteractionHub="wenduag.echo", TricksterDevice=True, TricksterState="echo_abyss"),
authored("trust", "What Lann gave you", 5, '"About Wenduag."', [
    n("start", "conversant", '''"I showed you how to catch her. I'd do it again.
Now she's in Drezen, armed, with my people sleeping a stair away.
She tried to kill me, Commander. Saving her didn't settle what happens next."''',
        c('"I brought her here. You helped save her; you did not invite her into your home."', "owed"),
        c('"I will answer for bringing her here. Keep your bow beside you."', "owed")),
    n("owed", "conversant", '''"I'll keep it beside me. And I'll tell Sull she's here. No mourning somebody who might walk into the cellar tomorrow.
I'm still fighting beside you. But don't ask me to lower that bow because you like her teeth."''',
        c("[Leave him to his bow.]", flags=(E + "trust_paid",))),
], requires=(E + "returned", E + "cost.used_lann", "lann.in_party"),
    forbids=(E + "trust_paid",) + LANN_GONE, AnswerLists=[HUB], NativeReturnCue=BACK)]


# Register the allocated pilot in the shared budget without injecting a second echo.
foresight.echo("wenduag", SCENES[0]["Id"], "start", SCENES[0]["Entry"],
    foresight.variant(SCENES[0]["Nodes"][0]["Text"]),
    sense="sight + sound", wrong="white stair, water",
    misstep="paid runner searches the wrong place", cost=("Finances", -50), existing=True)
foresight.CONSUMERS.update({item["Id"]: PAGE for item in SCENES})


def _variant(scene, source, target, text, flag=E + "returned"):
    """Keep old answers and targets; append an exclusive authored branch."""
    original = next(node for node in scene["Nodes"] if node["Id"] == source)
    variant = copy.deepcopy(original)
    variant.update(Id=target, Text=text)
    # Primary echo nodes were already serialized; new polish nodes follow them.
    _new = {"which_orchard", "own_orchard", "plain_orchard", "knife_down",
            "reckoning_select", "reckoning_bought", "reckoning"}
    if not scene["Id"].endswith(".native_visit"):
        _at = next((i for i, node in enumerate(scene["Nodes"]) if node["Id"] in _new), len(scene["Nodes"]))
        scene["Nodes"].insert(_at, variant)
    else:
        scene["Nodes"].append(variant)
    orchard_target = {"which_back": "which_orchard", "own_built": "own_orchard", "plain": "plain_orchard"}.get(source)
    for node in scene["Nodes"]:
        for choice in node["Choices"]:
            if orchard_target and choice.get("Next") == orchard_target:
                choice.setdefault("Forbids", []).append(flag)
    for node in scene["Nodes"]:
        if node is variant:
            continue
        for choice in list(node["Choices"]):
            if choice.get("Next") == source:
                alternative = copy.deepcopy(choice)
                choice.setdefault("Forbids", []).append(flag)
                alternative["Next"] = target
                # An echo return overrides an older orchard receipt, without duplicating the selector.
                if source in ("which_back", "own_built", "plain"):
                    alternative["Forbids"] = [f for f in alternative.get("Forbids", []) if f != W + "orchard_return"]
                alternative.setdefault("Requires", []).append(flag)
                if orchard_target and not scene["Id"].endswith(".native_visit"):
                    _at = next((i for i, answer in enumerate(node["Choices"])
                                if answer.get("Next") == orchard_target), len(node["Choices"]))
                    node["Choices"].insert(_at, alternative)
                else:
                    node["Choices"].append(alternative)


def integrate(payload):
    """Registered through wenduag_cairn.integrate; expansion.py is outside this unit's allow list."""
    # eng8-q8a: the departure receipt proves bodily life only; closed still withholds romance.
    payload["Derived"][E + "returned_available"] = [[W + "returned", "trickster.now"], [E + "departed", E + "valid", "trickster.now"]]
    # end eng8-q8a
    payload.setdefault("DerivedForbids", {})[E + "returned_available"] = [E + "unavailable"]
    for key in (W + "with_you", W + "partner", W + "late_committed", "wenduag.harem.voice.pack"):
        # eng8-q8a: a living refusal grants no continuing intimacy or household reward.
        payload["DerivedForbids"][key] = [E + "unavailable", "wenduag.closed"]
        # end eng8-q8a
    relationship = payload["Relationships"]["wenduag"]
    relationship["UnavailableFlags"].append(E + "unavailable")
    relationship["UnavailableOverrides"] = {
        key: E + "returned_available" for key in relationship["UnavailableOverrides"]}
    relationship["TricksterAccess"]["echo_abyss"] = dict(
        detect=["wenduag.dead_any", "!wenduag.kicked_out"], device=E + "pickup", returned=W + "returned")
    for presence in payload.get("Presences", {}).values():
        if presence.get("Unit") == UNIT and presence.get("Mode") == "spawn-copy":
            presence.setdefault("Forbids", []).append(E + "ready")
    scenes = {s["Id"]: s for s in payload["Scenes"] if s.get("Relationship") == "wenduag"}
    for suffix, flag in (("abyss.fall", "ready"), ("abyss.back", "ready"),
                         ("lann.truth", "rescued"), ("lann.found_out", "rescued")):
        scenes[W + suffix].setdefault("Forbids", []).append(E + flag)
    # eng7-l10: E-Q7-30 retire unsupported post-rest casualty actions. Native death has
    # already completed; preparation cannot retroactively earn custody. Keep all saved
    # IDs, nodes, answers and targets. The reviewed immediate echo pickup stays active.
    for suffix in ("abyss.fall", "street.fall"):
        scenes[W + suffix].setdefault("Forbids", []).append("trickster.ever")
    # end eng7-l10
    # Prevent every inherited return device from claiming this interrupted original.
    for item in scenes.values():
        if item.get("TricksterDevice"):
            item.setdefault("Forbids", []).append(E + "ready")
    _knife = next(node for node in scenes[W + "court.cairn"]["Nodes"] if node["Id"] == "knife")
    _knife_echo = copy.deepcopy(_knife["Choices"][0])
    _knife["Choices"][0].setdefault("Forbids", []).append(E + "returned")
    _knife_echo.setdefault("Requires", []).append(E + "returned")
    _knife["Choices"].append(_knife_echo)
    for _twin in ("", ".native_visit"):
        _variant(scenes[W + "court.trial" + _twin], "which_back", "which_echo",
            '''"You caught me by the belt, uplander. There's nothing to catch tonight."
    {n}Her knee bears down on your chest.{/n} "Let's see how quick those hands really are."''')
        _variant(scenes[W + "court.cairn" + _twin], "own_built", "own_echo",
            '''"I built it myself, after you brought me here. I carried every stone down this stair."
    {n}Her hand closes over yours on the rough edge.{/n} "You caught me once.
    Next time I fall, nobody gets to choose where I lie."''')
        _variant(scenes[W + "court.cairn" + _twin], "cut", "cut_echo",
            '''{n}She presses you back against the cold stones, bare skin sliding against yours. Her mouth follows the pulse in your throat. When you pull her nearer, she bites your shoulder and laughs into the mark.{/n} "Still quick, uplander?" {n}You catch her wrist. She twists free, hooks her hands behind your neck and pulls you against her. Her mouth meets yours before she can laugh again.{/n} "Catch me again." {n}The bell above the stair sounds once, then again.{/n}''')
        _variant(scenes[W + "court.stinger" + _twin], "plain", "plain_echo",
            '''"He's dead." {n}She stares at the spike.{/n} "And I was shut up here with a hole in my side.
    It should have been my hand. I'll keep this. There's still plenty of his kind to kill."''')
    # No conditional paragraphs on conversational pages, including the Regill reaction.
    regill = scenes[W + "react.regill_watch"]
    echo_regill = copy.deepcopy(regill)
    echo_regill["Id"] = W + "react.regill_echo"
    echo_regill["Reaction"] = True
    echo_regill["Requires"].extend(["trickster.now", E + "returned"])
    echo_regill["Forbids"] = [f for f in echo_regill["Forbids"] if f != regill["Id"]] + [echo_regill["Id"]]
    # P12: the echo has no legacy burial; retain its original start and exit.
    echo_regill["RequiresAnyGroups"] = [group for group in echo_regill.get("RequiresAnyGroups", [])
        if group != [W + "cairn_built", W + "abyss_cairn", W + "street_cairn"]]
    if not echo_regill["RequiresAnyGroups"]:
        echo_regill.pop("RequiresAnyGroups")
    echo_regill["Nodes"] = [echo_regill["Nodes"][0]]
    _exit = copy.deepcopy(next(node for node in regill["Nodes"] if node["Id"] == "neathholm")["Choices"][0])
    echo_regill["Nodes"][0]["Choices"] = [_exit]
    echo_regill["Nodes"][0]["Text"] = '''{n}Regill closes his ledger.{/n} "A traitor who served Savamelekh has been carried into Drezen with your supplies.
She answers to no muster roll. Your soldiers see her pass the gate and know whose protection she has."
{n}He opens the ledger again.{/n} "Should she resume her former employment, I will act.
Your hook will have to be faster than my axe."'''
    regill["Forbids"].append(E + "returned")
    payload["Scenes"].append(echo_regill)
    scenes[W + "react.lann_morning"]["RequiresAnyGroups"][0].append(E + "trust_paid")
    cost = [
        p("{n}Lann fought beside the Commander to the end. When asked about an old friend, he learned to answer with a question of his own.{/n}",
          requires=(E + "returned", E + "cost.used_lann"), forbids=LANN_GONE),
        p("{n}Lann died before the war ended. Wenduag kept the broken belt; she never spoke of the man who had taught the Commander where to catch it.{/n}",
          requires=(E + "returned", E + "cost.used_lann", "lann.dead")),
        p("{n}Lann left the Commander's service. The question he had learned to ask about an old friend went unanswered.{/n}",
          requires=(E + "returned", E + "cost.used_lann", "lann.kicked_out"), forbids=("lann.dead",)),
        p("{n}Lann was absent when the war ended. Wenduag still kept the broken belt. The Commander could not settle that debt with him.{/n}",
          requires=(E + "returned", E + "cost.used_lann", "lann.plot_absent"), forbids=("lann.dead", "lann.kicked_out")),
    ]
    for suffix in ("epilogue.pack", "epilogue.unclaimed", "epilogue.refused"):
        scenes[W + suffix]["Nodes"][0].setdefault("Paragraphs", []).extend(copy.deepcopy(cost))
    for item in scenes.values():
        if item["Owner"].endswith("Epilogue"):
            item.setdefault("Forbids", []).append(E + "unavailable")
    # eng8-q8a: append the existing departure's receipt; preserve its answer index.
    emitted = copy.deepcopy(SCENES)
    departure = next(s for s in emitted if s["Id"] == E + "return")["Nodes"][0]["Choices"][2]
    departure["Set"].append(E + "departed")
    payload["Scenes"].extend(emitted)
    # Authored aftermath of this paid rescue, not a second return or an invitation.
    payload["Scenes"].append(scene(E + "epilogue.departed", "", "WenduagEpilogue", 6, "", [
        nar("page", "{n}Wenduag left Drezen with her knife and the torn belt. At the south postern she stopped long enough "
            "to cut the belt in two. She took both pieces with her. There was no second invitation.{/n}", c("Continue")),
    ], requires=("trickster.ever", "wenduag.closed", E + "departed", "wenduag.life.available"),
       forbids=("wenduag.committed", E + "unavailable", "sacrifice"),
       ForbidOverrides={"sacrifice": "trickster.commander_back"}, last=6, Relationship="wenduag"))
    # end eng8-q8a
    payload.setdefault("SelectedAnswers", {})[E + "journey"] = "ddbcf384507535043a1ad5ad8ad8ea15"
    payload.setdefault("StartedDialogs", {})[E + "journey_started"] = "09f9a3762723ced47b25f953ddbc9e32"
    _lastcall_variants()


def _lastcall_variants():
    """Amend only Wenduag's later-emitted templates; shared source files stay untouched."""
    from storylines import lastcall_partners, lastcall_ledger
    partner = next(part for part in lastcall_partners.PARTNERS if part["key"] == "wenduag")
    if any(E + "returned" in paragraph["Requires"] for paragraph in partner["paragraphs"]):
        return
    partner["paragraphs"] = list(partner["paragraphs"])
    original = partner["paragraphs"][1]
    original["Forbids"].append(E + "returned")
    # The no-old-cairn account must not duplicate this earned echo funeral.
    partner["paragraphs"][7]["Forbids"].append(E + "returned")
    partner["paragraphs"].append(p(
        "{n}The world buried an empty coffin for the Commander. Wenduag listened from the cellar stair, turning the torn belt in her hands. "
        "Then she packed a niche in the catacombs with loose stones and laid the hooked shaft across it. Nobody was allowed to touch it.{/n}",
        requires=("lastcall.dead_on_record", E + "returned")))
    partner["paragraphs"].extend([
        p("{n}Lann came down the cellar stair after the war. He looked at the hook over her door, then left without asking to come in.{/n}",
          requires=(E + "returned", E + "cost.used_lann"), forbids=LANN_GONE),
        p("{n}Lann was dead. The hook stayed over her door; she never told anyone why she kept it.{/n}",
          requires=(E + "returned", E + "cost.used_lann", "lann.dead")),
        p("{n}Lann had left the Commander's service. The hook stayed over her door, and there was no visit to settle what it had cost him.{/n}",
          requires=(E + "returned", E + "cost.used_lann", "lann.kicked_out"), forbids=("lann.dead",)),
        p("{n}There was no word of Lann after the war. The hook stayed over her door.{/n}",
          requires=(E + "returned", E + "cost.used_lann", "lann.plot_absent"), forbids=("lann.dead", "lann.kicked_out")),
    ])
    lastcall_ledger.EXTRA_ENTRIES.append(dict(
        Id="owed.wenduag.echo", Section="Debts", Portrait="Wenduag", Title="Wenduag: the hooked shaft",
        Text="{n}I caught her belt as Lann struck. She lived. Lann had shown me where to stand; "
             "he knows what I used him for. She keeps the hook over her own cairn now.{/n}",
        Lines=[], Requires=[E + "returned", E + "cost.used_lann"], Forbids=[E + "unavailable"],
        AnyGroups=[], Tooltip="RRT_Debt"))
# eng8-q8h begin: the unsupported legacy bargains cannot promise a retired rescue.
# Keep the complete saved graphs. The allocated immediate echo remains the live device.
LEGACY_RESCUE_OFFERS = tuple(W + suffix for suffix in (
    "traitor.bid", "exile.bid_hub", "exile.bid_traitor", "exile.late_bid",
    "exile.champion", "traitor.nerves"))
_integrate_q8_base = integrate
def integrate(payload):
    _integrate_q8_base(payload)
    for item in payload["Scenes"]:
        if item["Id"] in LEGACY_RESCUE_OFFERS:
            item.setdefault("Requires", []).append("trickster.ever")
            item.setdefault("Forbids", []).append("trickster.ever")
# end eng8-q8h

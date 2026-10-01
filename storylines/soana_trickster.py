"""Soana on the Trickster path (Writer/handoffs/trickster/soana.md; F17 take them at their word, F13 loaded dice).

Canon: Camellia asks at camp to "turn her blood to a good cause" (Camelia/Cue_0136 f505392f) and, in the bear dialog, to
"let her blood serve the spirits of this land one last time" (SoanaAfterBear/Cue_0065 b2e41844, its twin Cue_0069).
Soana made Orso: "I forced the spirit to serve good by linking our lives together" (SoanaAfterBear/Cue_0015 396b1d46);
the brand and the clay knot are one binding (SoanaBear/Cue_0016, Cue_0023). Her creed: "a true protector is the one who
sacrifices themselves" (SoanaAfterBear/Cue_0012 353da9f2); "I serve the forest spirits. I don't serve you." (Cue_0029).
In Chapter 5 the Wintersun beasts fight demons on the roads (KTC_WintersunHelp/Cue_0048 3c616e0b). She is an old dwarf
woman who looks carved from driftwood (SoanaBeforeBear/Cue_0001): proud, bitter, blunt, never grateful, and she names her
own price.

The missed window (polish b9c): no mythic power turns a die. The Commander's die is loaded, lead behind the one, and is
pledged openly as a cheat's luck; her spirits take offerings (the Cue_0015 binding is hers), and Soana, not the die,
feeds that pledge to her beasts at her bowl. They stand on it, paid in the Commander's small misfortunes and salt.

Three states: the handover (Camellia is taken at her word before the kill), killed (the knot read in the other
direction, a guardian's life for hers; the return is tested at her grave and committed on her terms), and the missed
Chapter 3 window (a loaded die pledged in her bowl, paid for in Chapter 5, and a short courtship of its own).
"""
from story_format import c, n, p, reaction, scene

SCENES = []
UNIT = "64805abb52739e44280a758f850b300c"            # Soana_Wintersun (no dialog component; the presence copy)
CAMELLIA = "397b090721c41044ea3220445300e1b8"        # Camelia_Companion (speaks SoanaAfterBear/Cue_0065)
WINTERSUN = "0a5654e7dc18f074d9356009d55eb51b"       # WintersunOutdoor (her cave is in its mechanics scene)
LOCATOR = "cf766aaf-a3a9-490b-ae88-27ebcf6976e6"     # CameliaMove, CutsceneCamellia_killSoana/CommandMoveUnit acc721b8
MEDALLION = "4d78ec5dd1d1d5d41b9f2d8f2c8b5d53"       # SoanaMedallion "Crudely made clay medallion in the shape of a complex knot."
HER_LIST = "2b1776f3e398685479ff6b16290b4cc2"        # SoanaAfterQuest/AnswersList_0002
HER_RETURN = "e9feb6b2946c77641875f2bc731ede1e"      # SoanaAfterQuest/Cue_0017 "Life adapts, and so will we..."
CAMELLIA_HUB = "589d83230bbbfd04bb1220ee4fef1ce1"    # CompanionDialogues/Camelia/AnswersList_0030
EMBER_HUB = "f2a35965e9bc601449498bd022b04d9d"       # CompanionDialogues/Ember/AnswersList_0003
ULBRIG_HUB = "0a50c9c878844ed4a69b8d6131304c5e"      # DLC4_Shifter/Shifter_CompanionDialogue/AnswersList_0001

DEAD = "soana.dead"
KILLED = "soana.killed_by_camellia"
FOREST = "soana.forest_dead"
LOSS = (DEAD, KILLED, FOREST)
BEAR_DEAD = "soana.bear_dead"
GUARDIAN_DEAD = "soana.guardian_dead"               # Derived: Orso dead in combat (bear_dead) or withered when he bit the medallion (Cue_0023)
FRIENDS = "soana.trickster.friends"
CLOSED = "soana.closed"
COMMITTED = "soana.committed"
STARTED = "soana.started"
PRIMED = "soana.trickster.primed"
RETURNED = "soana.trickster.returned"
DECLINED = "soana.trickster.declined"
GRAVE_KEPT = "soana.trickster.graveyard_kept"
DICE = "soana.trickster.primed_dice"
LUCK_KEPT = "soana.trickster.luck_kept"
LUCK_REFUSED = "soana.trickster.luck_refused"
TESTED = "soana.trickster.luck_tested"
REST = "soana.trickster.answered_rest"
ROLL = "soana.trickster.answered_roll"
CHEAT = "soana.trickster.answered_cheat"
LATE_COMMITTED = "soana.trickster.late_committed"
BLOOD = "soana.trickster.cost.blood_given"
GUARDIAN = "soana.trickster.cost.guardian_paid"
SPENT = "soana.trickster.cost.medallion_spent"
LEASH = "soana.trickster.cost.leash_held"
DUG = "soana.trickster.cost.grave_dug"
BOUGHT = "soana.trickster.cost.grave_bought"
LEFT = "soana.trickster.cost.left_the_grave"
BEARER = "soana.trickster.cost.knot_bearer"
SECOND = "soana.trickster.cost.second_ask"
CATCHUP = "soana.trickster.cost.catchup"
LATE = "soana.trickster.cost.late"
DIE_KEPT = "soana.trickster.cost.die_in_her_bowl"
PULVERIZED = "soana.medallion_pulverized"          # SeenCues SoanaBear/Cue_0023 (Orso bit the clay knot to dust)
SAW_CAMELLIA = "soana.saw_camellia"                 # Derived: Camellia spoke in her cave (SoanaAfterBear Cue_0065/0069)
BAITED = "soana.trickster.cost.knot_recut"
CREED = "soana.heard_creed"                          # SeenCues SoanaAfterBear/Cue_0012 (her creed)
BOUND_AGAIN = "soana.trickster.rebind"
REBIND_DECLINED = "soana.trickster.rebind_declined"
HEARD = "soana.heard_link"                            # Derived: SoanaAfterBear Cue_0015 or its twin Cue_0036 seen
SACRIFICE_BACK = {"sacrifice": "trickster.commander_back"}
DEFENDER = ["soana.old_defender", BEAR_DEAD]

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={DEAD: RETURNED, KILLED: RETURNED, FOREST: RETURNED},
    TricksterAccess={
        "killed": dict(detect=list(LOSS), device="soana.trickster.killed.knot", returned=RETURNED),
        "handover": dict(detect=["camellia.asked_for_soana", "camellia.claimed_soana_a", "camellia.claimed_soana_b"],
                         device="soana.trickster.handover.after_quest", returned=None),
        "missed": dict(detect=["chapter_later", "!soana.progression_kept"], device="soana.trickster.missed.crooked_luck",
                       returned=None),
    })
PRESENCES = {
    # Her own blueprint at her own cave, where Camellia stood to kill her. The native unit is dead, so reuse-native cannot
    # apply; the copy has no dialog component, so Dialog "hub" makes it talkable. If the spawn fails, the epilogue page
    # carries the commit (no letter twin: the Chapter 5 letter cap).
    "soana.presence": dict(Unit=UNIT, Area=WINTERSUN, Mode="spawn-copy", At=dict(Locator=LOCATOR, Offset=[0.0, 0.0]),
                           Requires=["trickster.ever", RETURNED], Forbids=[CLOSED], MinChapter=3, MaxChapter=5,
                           AnswerLists=[], Dialog="hub",
                           Greeting="{n}Soana is standing where Camellia stood, in her own cave, with loam still under "
                                    "her nails. She does not look up.{/n} \"Say what you came to say, hunter. "
                                    "The dead have more patience than I do.\""),
}


def s(id, text, *choices):
    return n(id, "Soana", text, *choices, portrait="Soana")


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, **kw)


def inline(id, title, chapter, entry, nodes, requires, forbids, delay=0, last=None, **extra):
    """A scene on her own SoanaAfterQuest list; closes back into the native list (Cue_0017). A new trick passes
    EntryMythic="PlayerIsTrickster"; a payoff or a later beat does not, so a lost path still sees it (ledger 18)."""
    SCENES.append(scene(id, title, "Soana", chapter, entry, nodes, requires=requires, forbids=forbids, delay=delay,
                        last=last or chapter, Relationship="soana", Chapters=[chapter], AnswerLists=[HER_LIST],
                        NativeReturnCue=HER_RETURN, **extra))


def at_cave(id, title, entry, nodes, requires, forbids, delay, **extra):
    """A scene on the returned Soana's presence at her cave (Chapters 3 and 5)."""
    SCENES.append(scene(id, title, "Soana", 3, entry, nodes, requires=requires, forbids=forbids, delay=delay, last=5,
                        Relationship="soana", Chapters=[3, 5], ContactUnit=UNIT, Areas=[WINTERSUN],
                        InteractionHub="soana.presence", **extra))


# --- State 1, the handover: the spirits' portion (F17, Camellia taken at her word) --------------------------------------

def portion(suffix, answer_list, return_cue, joke, requires, any_of, nodes):
    SCENES.append(scene("soana.trickster.handover." + suffix, "The spirits' portion", "Soana", 3,
        '[Play a cruel trick on Camellia] ' + joke, nodes, requires=requires,
        forbids=(DEAD, KILLED, PRIMED), last=3, Relationship="soana", Chapters=[3], AnswerLists=[answer_list],
        NativeReturnCue=return_cue, EntryMythic="PlayerIsTrickster", EntryAlignment=dict(Direction="Chaotic", Value=1),
        TricksterDevice=True, TricksterState="handover", **({"RequiresAnyGroups": [list(any_of)]} if any_of else {})))


# After the quest: Camellia asked at camp; she need not be standing here, so Soana answers the joke alone.
portion("after_quest", HER_LIST, HER_RETURN,
    '"Camellia asked me at camp to turn your blood to a good cause. Your forest is a good cause. Bleed for it first, and she can have what\'s left."',
    ("trickster", "camellia.asked_for_soana"), None, [
    n("start", "Soana", '''{n}The old woman weighs you with her small black eyes, the way she would weigh a snare somebody else had set. Then she laughs, the cracked laugh from your first meeting, and draws her knife across her own palm. Blood runs off her knuckles into the moss. Somewhere in the trees, something answers: not a bird, not a wolf.{/n}
"A good cause. There. The spirits have had their portion, bloody hunter, and a portion is all anyone is owed. Tell your hungry friend she can lick the moss."
{n}She wraps the hand in a rag without looking at it, the way other people tie a bootlace.{/n}''', c("Continue", "cost")),
    n("cost", "Soana", '''"Do not look so pleased with yourself. The spirits ate, so now they know my taste. Every winter from this one they will come to the cave mouth and ask for more, and I will give it to them, because a bargain is a bargain even when a fool strikes it for you."
"Why do it, then?"
"Because your friend would have taken all of it, and the spirits would have had nothing. I serve the forest. I do not serve you, and I certainly do not serve her."''',
        c('[Leave before she changes her mind]', native_next="fef727987297e8d4eb34068688fdac27", flags=(PRIMED, BLOOD)))])

# After the bear: Camellia has just spoken (Cue_0065/0069), so she is on screen and answers in her own voice.
for suffix, lst, nrc, nxt in (("after_bear_a", "001686714a5c2384ba09686b45bd033f", "726e936d05fde7a4798854a917b4b73d",
                               "c6b676fa989a5494cb6ce0c981979907"),
                              ("after_bear_b", "f7b5537dc61ccdc41b0732f0a1b700b2", "396b1d46a2cfb1e48b205468d4360ee9",
                               "74664ddd7bb36744ba825c29aad6f4b3")):
    portion(suffix, lst, nrc, '"You heard her: her blood serves the spirits. So let the spirits have it."',
        ("trickster",), ["camellia.claimed_soana_a", "camellia.claimed_soana_b"], [
        n("start", "Soana", '''{n}The old woman barks a laugh at Camellia, not at you, and draws her knife across her own palm. Blood runs into the moss. Somewhere in the trees, something answers.{/n}
"There, spirit talker. The spirits of this land have had their portion, from my own hand. That is all you get. That is all *anyone* gets."''', c("Continue", "camellia")),
        n("camellia", "Camellia", '''{n}Camellia watches the blood soak into the ground with the fixed attention of a cat at a closed door. Her smile does not move at all.{/n}
"How very generous of her. And of you, my friend. You have taken a death off my plate in front of the one audience I cared about." {n}She wets her lips.{/n} "I do not forget who takes food off my plate. I shall be thinking of you, often, and very carefully."''',
            c('[Leave before either of them decides otherwise]', native_next=nxt, flags=(PRIMED, BLOOD)),
            speaker_unit=CAMELLIA)])


# --- State 2, killed: the knot never checked (F17, her own words read in the other direction) --------------------------

SCENES.append(scene("soana.trickster.killed.knot", "The knot never checked", "Soana", 3, "", [
    nar("start", """{n}You go back to Wintersun alone, on a grey morning, with the crusade's business waiting behind you. The forest died with her: the undergrowth is black, the birds are gone, and something in the black trees has been howling since the night she fell. Soana's cave smells of cold ash and something sweeter under it. Nobody has taken her bones to the ground.{/n}
{n}Something out in the trees stops moving when you step inside.{/n}""",
        c("Continue", "orso", forbids=(GUARDIAN_DEAD,)), c("Continue", "spirit", requires=(GUARDIAN_DEAD,))),
    nar("orso", """{n}Orso comes to the cave mouth and will not come further. He has been circling it for days; the moss is worn down to stone in a ring. The brand on his shoulder is a knot, the same knot she wore in clay at her throat, and it has not faded. Whatever she tied to him has not come untied, by the look of it.{/n}""",
        c("Continue", "read", requires=(HEARD,)), c("Continue", "marks", forbids=(HEARD,))),
    nar("spirit", """{n}Orso lies where he died. The brand on his hide is only a scar on a dead thing now, and nothing in those bones moves.{/n}""",
        c("Continue", "read", requires=(HEARD,), forbids=(GUARDIAN_DEAD,)), c("Continue", "marks", forbids=(HEARD, GUARDIAN_DEAD)),
        c("Continue", "carcass", forbids=(PULVERIZED,)), c("Continue", "pelt", requires=(PULVERIZED,))),
    nar("read", """{n}You remember what she told you, with her arms folded over her chest: she used the medallion to control a spirit of the Abyss after linking it to the sacred bear, and she forced the spirit to serve good by linking our lives together.{/n}
{n}*Our* lives. She may have meant the bear's and the spirit's. She may have meant her own.{/n}
{n}You put two fingers to the brand. It tugs back, once, like a line with a fish on it, and behind you, on the cold floor of the cave, the dead woman's hand closes on nothing.{/n}
{n}So something holds her, and you wager it is the thing in the bear: the spirit of the Abyss she caught and broke to the forest's work. If it is tied to her, it is tied to a corpse, and a thing tied to a corpse can go nowhere and eat nothing; perhaps that is the howling in the trees. Whatever it is, the knot is not cut: when you pull, she answers. A rope that can be pulled one way can be pulled the other.{/n}
{n}It is a gamble, and a Trickster's kind: offer the thing on the far end a living hand to pull on instead of a dead one, and see whether it will drag her back up her own strand to get it.{/n}""",
        c('[Hold her clay medallion to the guardian\'s brand and bargain with what holds the other end] "Whatever you are: give her back, and pull on me instead."',
          "wake_clay", mythic="Trickster", alignment=("Chaotic", 1), requires=("soana.medallion_held",), remove_item=MEDALLION,
          flags=(RETURNED, STARTED, GUARDIAN, SPENT, LEASH)),
        c('[Lay your hand on the brand and bargain with what holds the other end] "Whatever you are: give her back, and pull on me instead."',
          "wake_brand", mythic="Trickster", alignment=("Chaotic", 1), forbids=("soana.medallion_held",),
          flags=(RETURNED, STARTED, GUARDIAN, LEASH)),
        c('[Leave the knot tied] "No. She said she was finished. Let her be finished."', flags=(CLOSED,))),
    nar("marks", """{n}You crouch where she fell. Days dead, and she has not begun to rot: her hands are grey but whole, and the cave smells of ash and dry herbs and nothing worse. On the rock above her pallet the same knot is scratched in charcoal, over and over, the knot of her clay medallion and of the brand on Orso's hide; and beside it, small, the way a trapper keeps a tally, three marks: a bear, a horned thing with too many teeth, and a stooped little figure with a braid.{/n}
{n}A bear, a demon and an old woman, tied in one knot. She never told you so. She wrote it on her wall.{/n}
{n}You put two fingers to the brand. It tugs back, once, like a line with a fish on it, and behind you, on the cold floor of the cave, the dead woman's hand closes on nothing.{/n}
{n}So something holds her, and you wager it is the thing in the bear: the spirit of the Abyss she caught and broke to the forest's work. If it is tied to her, it is tied to a corpse, and a thing tied to a corpse can go nowhere and eat nothing; perhaps that is the howling in the trees. Whatever it is, the knot is not cut: when you pull, she answers. A rope that can be pulled one way can be pulled the other.{/n}
{n}It is a gamble, and a Trickster's kind: offer the thing on the far end a living hand to pull on instead of a dead one, and see whether it will drag her back up her own strand to get it.{/n}""",
        c('[Hold her clay medallion to the guardian\'s brand and bargain with what holds the other end] "Whatever you are: give her back, and pull on me instead."',
          "wake_clay", mythic="Trickster", alignment=("Chaotic", 1), requires=("soana.medallion_held",), remove_item=MEDALLION,
          flags=(RETURNED, STARTED, GUARDIAN, SPENT, LEASH)),
        c('[Lay your hand on the brand and bargain with what holds the other end] "Whatever you are: give her back, and pull on me instead."',
          "wake_brand", mythic="Trickster", alignment=("Chaotic", 1), forbids=("soana.medallion_held",),
          flags=(RETURNED, STARTED, GUARDIAN, LEASH)),
        c('[Leave the knot tied] "No. She said she was finished. Let her be finished."', flags=(CLOSED,))),
    nar("carcass", """{n}Orso lies where he fell, and the carcass has gone soft and black at the edges. The grass has died in a ring around it, the way grass dies around a poisoned well. The brand on his shoulder is a scar on dead hide. Whatever she bound into him, it is not answering: you press two fingers to the brand and feel nothing but cold fur.{/n}
{n}If there is anything left to pull on, you will have to give it something to hold first.{/n}""",
        c('[Cut her knot into the dead hide, bleed into the cuts, and wait for something to come to it] "A knot is a door as well as a rope. Let us see who knocks."',
          "bait", alignment=("Chaotic", 1), flags=(BAITED,)),
        c('[Leave the knot cut] "She said she was finished. Let her be finished."', flags=(CLOSED,))),
    nar("pelt", """{n}Orso is what the medallion left of him: a grey pelt stretched over bones, where he dropped when his teeth ground the clay knot to dust. The brand is still on the pelt, a scar on a dead thing, and the knot that held it is gone. You press two fingers to it and feel nothing but cold fur.{/n}
{n}If there is anything left to pull on, you will have to tie the knot again yourself, and give it something to hold.{/n}""",
        c('[Cut her knot into the dead hide, bleed into the cuts, and wait for something to come to it] "A knot is a door as well as a rope. Let us see who knocks."',
          "bait", alignment=("Chaotic", 1), flags=(BAITED,)),
        c('[Leave the knot cut] "She said she was finished. Let her be finished."', flags=(CLOSED,))),
    nar("bait", """{n}You copy the brand into the hide with your knife, line by line, following the old scar, and then you open your palm and press it into the cuts until the hide is dark with you. It is a gamble, and you know it: that a knot cut in blood is a door as well as a rope, and that something at the Worldwound's edge will come to an open door. Then you sit down beside it in the cold and wait.{/n}
{n}Near dawn the black trees go quiet. Something comes down out of them that you never see, and the cut knot in the hide drinks, and goes on drinking after your blood is gone. Behind you, on the cold floor of the cave, the dead woman's hand closes on nothing.{/n}
{n}So the knot holds again, and she is on it. What is on the far end you cannot say: something of hers come back to its knot, or something new that found the door you cut. The knot is not cut now: when you pull, she answers. A rope that can be pulled one way can be pulled the other.{/n}""",
        c('[Press her clay medallion into the cuts and bargain with what holds the other end] "Whatever you are: give her back, and pull on me instead."',
          "wake_clay", mythic="Trickster", alignment=("Chaotic", 1), requires=("soana.medallion_held",), remove_item=MEDALLION,
          flags=(RETURNED, STARTED, GUARDIAN, SPENT, LEASH)),
        c('[Lay your cut hand on the knot and bargain with what holds the other end] "Whatever you are: give her back, and pull on me instead."',
          "wake_brand", mythic="Trickster", alignment=("Chaotic", 1), forbids=("soana.medallion_held",),
          flags=(RETURNED, STARTED, GUARDIAN, LEASH)),
        c('[Leave it] "No. She said she was finished. Let her be finished."', flags=(CLOSED,))),
    nar("wake_clay", """{n}You press the clay to the brand. Nothing happens, for long enough that you begin to feel foolish. Then the brand darkens, as a rope darkens when it is pulled wet, and something on the far end of the knot pulls back.{/n}
{n}It does not speak. It does not need to. You feel it weigh you, the way it once weighed her: a new hand on the knot, a stranger's, soft with command. It wants what it always wanted, a hand to strain against. It will give her back if it gets yours.{/n}
{n}You close your fist. The medallion cracks down the middle with a sound like a knuckle, and the pull comes up your arm: a weight round your wrist like a leash wound twice about the hand, with something heavy and hungry at the far end of it.{/n}""",
        c("Continue", "wake_orso", forbids=(GUARDIAN_DEAD,)), c("Continue", "wake_spirit", requires=(GUARDIAN_DEAD,))),
    nar("wake_brand", """{n}You lay your palm on the brand and take hold of her end of the knot, as if it were a rope in the dark. Nothing happens, for long enough that you begin to feel foolish. Then the brand darkens under your hand, as a rope darkens when it is pulled wet, and draws tight until your skin burns with cold.{/n}
{n}Something on the far end of the knot pulls back, and weighs you: a stranger's hand, soft with command. It wants what it always wanted, a hand to strain against. It will give her back if it gets yours. You do not let go.{/n}
{n}When you take the hand away, the knot is printed on your palm in white, and the pull does not stop: a weight round your wrist like a leash wound twice about the hand, with something heavy and hungry at the far end of it.{/n}""",
        c("Continue", "wake_orso", forbids=(GUARDIAN_DEAD,)), c("Continue", "wake_spirit", requires=(GUARDIAN_DEAD,))),
    nar("wake_orso", """{n}Out in the ferns Orso staggers, and does not fall. He lies down at the cave mouth, panting, alive. The brand on his shoulder has gone pale. The one on your hand has not. Something inside him strains once against the knot, and you feel it strain.{/n}""",
        c("Continue", "soana")),
    nar("wake_spirit", """{n}The black grass around the bones stirs, though there is no wind. What lies in them strains once against the knot, and you feel it in your wrist, like a dog on a short rope. It does not get loose. You are holding it.{/n}""",
        c("Continue", "soana")),
    s("soana", """{n}Behind you, someone coughs up forest loam.{/n}
"...Bloody hunter. Of course." {n}She spits loam.{/n} "You put your hand on my knot. All those winters I held that demon by the throat, and a hand that holds a thing that long is part of the knot, like it or not. I knew. I told nobody, because I did not think any fool alive would pull on it." {n}She looks at the white print on your hand.{/n} "And it took the trade. Of course it did. A thing from the other side would sooner drag on a young fist than on a dead old woman's. That is worse."
{n}She sits up on the cold floor of her cave, an old dwarf woman in rags, and looks at her hands as if somebody had returned them to her with the fingers in the wrong order. Then she looks at yours.{/n}
"I was finished. I had earned it. And now you are holding my leash in a hand that has never held anything but a sword. It will pull. At night, mostly. Do not let go of it until I take it back, and I have not decided when that will be.\"""",
        c('"You can hate me standing up."')),
    ], requires=("trickster", "trickster.ever"), forbids=(RETURNED, CLOSED), delay=0, last=5, Relationship="soana",
    Chapters=[3, 5], Remote=True, TricksterDevice=True, TricksterState="killed",
    RequiresAnyGroups=[[DEAD, KILLED]]))

at_cave("soana.trickster.returned.graveyard", "What the knot cost", '"Soana."', [
    s("start", """{n}Soana has a spade in one hand. Around the cave mouth are new mounds, a row of them, small and large: a fox, two wolves, a hind with her calf. Beside the last is a hole she has not finished.{/n}
"Two days I have been walking this forest. When I died, the spirits I kept in hand went mad, and the forest died with me. It did not come back when I did. Not a squirrel in it. I bury what I find.\"""",
        c("Continue", "orso", forbids=(GUARDIAN_DEAD,)), c("Continue", "spirit", requires=(GUARDIAN_DEAD,))),
    s("orso", """"Orso lies at my door and will not leave it. He is too tired to hunt. The thing in him pulls at your end of the knot every time he dreams; I can see it in your hand from here. You will learn to sleep through it, or you will not sleep.\"""",
        c("Continue", "dig")),
    s("spirit", """"Orso's bones are in the ground; I put them there myself, the first night, with my hands. What is in them pulls at your end of the knot when it is hungry, and it is always hungry now. You will learn to sleep through it, or you will not sleep.\"""",
        c("Continue", "dig")),
    s("dig", """{n}She holds out the spade, handle first.{/n}
"You were very quick with my knot, bloody hunter. Let us see how quick you are with a grave.\"""",
        c('[Take the spade]', "dug", flags=(GRAVE_KEPT, DUG)),
        c('"I\'ll send to Drezen for diggers."', "bought", crusade=("Finances", -100), flags=(GRAVE_KEPT, BOUGHT)),
        c('[Leave her with her graves]', flags=(CLOSED, LEFT))),
    nar("dug", """{n}The ground is frozen for the first hand's depth and roots all the way down after that. You dig until the light goes, one-handed half the time, because the other hand keeps closing on nothing when the leash pulls. Soana does not help. She sits on a stone and tells you when you are doing it wrong, which is often, and when the hind and her calf finally go in she says something over them in a language that sounds like branches knocking.{/n}""",
        c('[Wipe your hands]', "decide")),
    nar("bought", """{n}The diggers come from Drezen three days later, crusaders with good boots and bad manners. They dig fast and deep and argue about who has to carry the calf. Soana watches them from the cave mouth the whole time with an expression you would not wish on an enemy.{/n}""",
        c('[Pay them off]', "decide")),
    s("decide", """{n}She leans on the spade and looks at you the way she looks at weather.{/n}
"Hear me, hunter, because I will say it once. The dead forest I will bury with you or without you. That is the forest's business, and it does not buy you anything from me. My leash I will take back from your hand whatever you say; I do not leave my work in a stranger's fist. What you want from me is another matter, and I have not decided what I think of it."
"Come back in three days. By then I will know my own mind. I always do, in the end.\"""",
        c('"Three days, then."'),
        c('"I dug your graves. That\'s all I came for."', flags=(CLOSED,))),
    ], requires=("trickster.ever", RETURNED), forbids=(CLOSED, GRAVE_KEPT), delay=48)

TERMS_NIGHT = '''{n}She lays the grey cord across your marked palm and winds it round your wrist, then round her own, and pulls it tight enough to hurt. The fire is low. She does not let go of the cord.{/n}
"Knots listen." {n}Her eyes do not leave yours.{/n} "So do I. So listen."
{n}She pulls. You come. Her hands are as hard as roots and warmer than anything in this forest has a right to be; she finds the buckle of your sword-belt without looking, the way she finds the knife at her own. Her mouth tastes of smoke and of the bitter bark she chews against the cold. She lifts your tied wrist to her teeth and bites the heel of your hand where the print is white, not gently, to see what you will do about it.{/n}
"All those winters I slept with a demon at the door. I am done sleeping."
{n}She draws the cord taut between your wrists and hers and pulls you down into the old furs after her. You catch her against you and drag the last of her rags off her shoulders; she shoves your shirt up with her bound hand, straddles your hips with her knees sunk in the pelts, and leans down over you with her braid falling across your face.{/n}'''
TERMS_NIGHT_CLAY = '''{n}She presses the shards into your palm and ties them there with a strip of gut, round your wrist and then round her own, tight enough to hurt. The fire is low. She does not let go of the strip.{/n}
"Knots listen." {n}Her eyes do not leave yours.{/n} "So do I. So listen."
{n}She pulls. You come. Her hands are as hard as roots and warmer than anything in this forest has a right to be; she finds the buckle of your sword-belt without looking, the way she finds the knife at her own. Her mouth tastes of smoke and of the bitter bark she chews against the cold. She lifts your tied wrist to her teeth and bites the heel of your hand where the knot drew blood, not gently, to see what you will do about it.{/n}
"All those winters I slept with a demon at the door. I am done sleeping."
{n}She draws the gut strip taut between your wrists and hers and pulls you down into the old furs after her. You catch her against you and drag the last of her rags off her shoulders; she shoves your shirt up with her bound hand, straddles your hips with her knees sunk in the pelts, and leans down over you with her braid falling across your face.{/n}'''
TERMS_MORNING = '''{n}The fire has gone to ash and the frost has come in over the cave mouth as far as the furs. Her end of the knot is gone from her wrist; yours is still tied, and underneath it the skin is raised in a red weal the shape of a knot.{/n}
{n}Soana is outside already, feeding the spirits from a bowl. She does not turn around.{/n}
"Your end is sore. Good. It is supposed to be. Now go and fight your war, hunter, and do not die before I do. It would be very inconvenient."'''

at_cave("soana.trickster.returned.terms", "The second strand", '"It has been three days."', [
    s("start", '''{n}The grave is a low mound under the ferns. She has laid stones on it in a pattern you almost recognize.{/n}''',
        c("Continue", "dug", requires=(DUG,)), c("Continue", "bought", requires=(BOUGHT,)),
        c("Continue", "price", forbids=(DUG, BOUGHT, SPENT)), c("Continue", "price_clay", requires=(SPENT,), forbids=(DUG, BOUGHT))),
    s("dug", '''"You dug. Badly, and too shallow at the head end, but you dug, with your own hands, in the cold. That is more than your friends in Drezen would have done. And you came back, which is worse. I find that troublesome."''',
        c("Continue", "price", forbids=(SPENT,)), c("Continue", "price_clay", requires=(SPENT,))),
    s("bought", '''"Your diggers came, dug, ate my last smoked fish and left. Paying is easy for you people. It is the one thing you are good at. Remember that I noticed."''',
        c("Continue", "price", forbids=(SPENT,)), c("Continue", "price_clay", requires=(SPENT,))),
    s("price", '''{n}She opens her hand. In it lies the thing she sat plaiting on her stone by the graves while the digging went on: a cord of grey hair from her own braid, twisted with sinew and tied in the knot that is printed white on your palm. The end of her braid is ragged where the knife went through it.{/n}
"Hear this first, because I will not say it in the furs. I had a husband. Corven. He laid a wreath of the first summer flowers on my head and I became his wife. He is gone, and I do not know where, or whether he lives. I will not dig him a grave to make room for you, and I will not pretend he never was. Take me with him in it, or do not take me."
"I have decided. I want you anyway, hunter, which is a great nuisance, and I am too old to pretend otherwise for the sake of your pride."
"Look at your hand. A knot with one strand is not a knot. It is a piece of string. You are holding my leash in your bare palm, and it will pull you to pieces inside a year. If I am to take it back and keep it, the knot needs a second life at the other end. Mine is spoken for; you saw to that. So: yours. You wear this where the print is. When I die again, and I will, it is your life the knot comes looking for first."
"That is not me haggling. That is what a knot is. I cannot make it sweeter, and I would not if I could."''',
        c('[Hold out your marked hand for the cord]', "bind"),
        c('"Ask me again when the ground thaws."', "no"),
        c('"Find another fool."', "fool"),
        c('"Keep your knot, and keep Corven\'s place. I\'ll be your friend, not your second strand."', "friend", flags=(FRIENDS,))),
    s("bind", '''{n}She does not take your hand yet. She looks at it: the calluses, the scars, the crusade's grime.{/n}
"Say it, then. 'Mine first.' Knots listen."''',
        c('"Mine first."', "night", flags=(COMMITTED, BEARER)),
        c('[Laugh]', "no")),
    s("no", '''{n}She closes her fist over the knot and turns away.{/n}
"No. You laughed at my knot once already, and I woke up in a dead forest. Come back when you can keep your face straight over a thing that matters."''',
        c('[Go]', flags=(DECLINED,))),
    s("fool", '''"I already found one. {mf|He|She} is holding my leash, and {mf|he|she} laughs at knots."
{n}She does not look at you again.{/n}''',
        c('[Go]', flags=(CLOSED,))),
    s("night", TERMS_NIGHT, c("Continue", "morning")),
    s("morning", TERMS_MORNING, c('[Go]')),
    s("friend", '''{n}She looks at you for a long breath, then snorts.{/n}
"A friend. Hm. Then I take my leash back alone, with one strand and my own blood, and you may come and eat my fish and be useless at my graves. Do not look at me like that. Corven had friends too. He never once told them where I kept the mead."''',
        c('[Go]')),
    s("price_clay", '''{n}She opens her hand. The two halves of the clay knot lie in it, the medallion you cracked at the brand; she picked them out of the ash of her own cave.{/n}
"Hear this first, because I will not say it in the furs. I had a husband. Corven. He laid a wreath of the first summer flowers on my head and I became his wife. He is gone, and I do not know where, or whether he lives. I will not dig him a grave to make room for you, and I will not pretend he never was. Take me with him in it, or do not take me."
"I have decided. I want you anyway, hunter, which is a great nuisance, and I am too old to pretend otherwise for the sake of your pride."
"Look at it. A knot with one strand is not a knot. It is a piece of string. You are holding my leash in your bare hand, and it will pull you to pieces inside a year. If I am to take it back and keep it, the knot needs a second life at the other end. Mine is spoken for; you saw to that. So: yours. Carry the pieces. When I die again, and I will, it is your life the knot comes looking for first."
"That is not me haggling. That is what a knot is. I cannot make it sweeter, and I would not if I could."''',
        c('[Hold out your hand for the pieces]', "bind_clay"),
        c('"Ask me again when the ground thaws."', "no"),
        c('"Find another fool."', "fool"),
        c('"Keep your knot, and keep Corven\'s place. I\'ll be your friend, not your second strand."', "friend", flags=(FRIENDS,))),
    s("bind_clay", '''{n}She does not put the pieces in your hand yet. She looks at it: the calluses, the scars, the crusade's grime.{/n}
"Say it, then. 'Mine first.' Knots listen."''',
        c('"Mine first."', "night_clay", flags=(COMMITTED, BEARER)),
        c('[Laugh]', "no")),
    s("night_clay", TERMS_NIGHT_CLAY, c("Continue", "morning")),
    ], requires=("trickster.ever", RETURNED, GRAVE_KEPT), forbids=(CLOSED, COMMITTED, DECLINED), delay=72)

at_cave("soana.trickster.returned.second_ask", "Tied tighter", '"The ground has thawed."', [
    s("start", '''{n}She does not wait for you to reach the cave. She comes down the path to meet you with the knot already in her fist and a strip of fresh gut over her shoulder, and she takes your wrist before you can say anything at all.{/n}
"You made me say it twice. I do not say things twice. So the knot will remember that it had to be asked twice, and so will you."
{n}She sets the edge of her knife against the inside of your wrist, where the pulse is, and waits.{/n}''',
        c("Continue", "price")),
    s("price", '''"Deeper than last time would have been. It will scar white and it will ache every winter you live, and every time it aches you will know whose it is. Hold out your hand or take it back. I will not ask a third time."''',
        c('[Hold out your wrist] "Mine first."', "night", forbids=(SPENT,), flags=(COMMITTED, BEARER, SECOND)),
        c('[Take your hand back] "No. Not like this."', flags=(CLOSED,)),
        c('[Hold out your wrist] "Mine first."', "night_clay", requires=(SPENT,), flags=(COMMITTED, BEARER, SECOND))),
    s("night", TERMS_NIGHT, c("Continue", "morning")),
    s("morning", TERMS_MORNING, c('[Go]')),
    s("night_clay", TERMS_NIGHT_CLAY, c("Continue", "morning")),
    ], requires=("trickster.ever", RETURNED, DECLINED), forbids=(CLOSED, COMMITTED), delay=96)

# Q10 r2: a lover committed before she died (the registered courtship, then the handover or the Commander's own kill)
# still owes the knot its second strand. The terms and the second ask forbid soana.committed, so this is that vow.
at_cave("soana.trickster.returned.rebind", "An old promise, a new knot", '"You said three days."', [
    s("start", '''{n}The grave is a low mound under the ferns. She has laid stones on it in a pattern you almost recognize. She does not get up.{/n}''',
        c("Continue", "camellia", requires=(KILLED,)), c("Continue", "own", forbids=(KILLED,))),
    s("camellia", '''"You courted me. You sat at my fire and ate my fish and called me beloved, and I let you. Then you stood outside my cave while your spirit talker opened my throat, because she asked nicely."
{n}She turns a stone on the mound with one finger, so the pattern comes right.{/n}
"And then you came back and pulled me up out of the dark by my own knot. I have been trying for three days to decide which of those you meant. I think it was all of them. That is the worst thing about you."''',
        c("Continue", "price")),
    s("own", '''"You courted me. You sat at my fire and ate my fish and called me beloved, and I let you. Then you killed me with your own hands, in my own cave."
{n}She turns a stone on the mound with one finger, so the pattern comes right.{/n}
"And then you came back and pulled me up out of the dark by my own knot. I have been trying for three days to decide which of those you meant. I think it was all of them. That is the worst thing about you."''',
        c("Continue", "price")),
    s("price", '''{n}She opens her hand. The knot is in it.{/n}
"What we said before I died was said to a living woman with a whole knot. This one has one strand, and you are holding my leash in your bare hand. If I am to take it back and keep it, the other end needs a life on it. Yours. When I die again, it is your life the knot comes looking for first."
"Old promises do not tie knots, hunter. Say it new or do not say it."''',
        c('[Hold out your hand] "Mine first."', "night", forbids=(SPENT,), flags=(BEARER, BOUND_AGAIN)),
        c('"No. Not this. Not my life on your knot."', "refuse", flags=(REBIND_DECLINED,)),
        c('[Hold out your hand] "Mine first."', "night_clay", requires=(SPENT,), flags=(BEARER, BOUND_AGAIN))),
    s("refuse", '''{n}She closes her fist over the knot.{/n}
"Then I take my leash back alone, with one strand and my own blood, and it may kill me, and that will be your doing too. You may still come to my fire. You may not hold my leash, and you will not hold anything else of mine that matters."''',
        c('[Go]')),
    s("night", TERMS_NIGHT, c("Continue", "morning")),
    s("morning", TERMS_MORNING, c('[Go]')),
    s("night_clay", TERMS_NIGHT_CLAY, c("Continue", "morning")),
    ], requires=("trickster.ever", RETURNED, GRAVE_KEPT, COMMITTED), forbids=(CLOSED, BEARER, REBIND_DECLINED), delay=72)


# The portion comes due (audit: the recurring blood price must be witnessed, not only promised). The first winter after
# the handover, on her own list: the spirits come to the cave mouth, and the Commander can pay it or watch her pay it.
inline("soana.trickster.handover.winter_portion", "The spirits' portion, again", 5, '"The spirits came, didn\'t they?"', [
    n("start", "Soana", '''{n}There is frost on the moss, and a ring of it has melted in front of the cave mouth, the size of a cart wheel, as if something warm had stood there all night. Soana sits on the stone beside it with her knife across her knees. Her left palm is a lattice of old white cuts, and one new one, not yet opened.{/n}
"They came at moonrise, the way I told you they would. They stood there till dawn and did not say a word. They do not need to. I know what they are owed; a fool struck the bargain for me, and a bargain is a bargain."
{n}She turns the knife so the edge catches the light, and looks at you, not at the blade.{/n}
"You may watch. People who make bargains for other people ought to see them paid."''',
        c('[Hold out your own palm] "My joke. My blood. Pay them from me this winter."', "shared",
          flags=("soana.trickster.cost.portion_shared",)),
        c("[Watch her pay it]", "watched", flags=("soana.trickster.portion_watched",))),
    n("shared", "Soana", '''{n}She looks at your hand the way she looks at a snare that has caught the wrong animal. Then she takes your wrist in her root-hard fingers and draws the knife across your palm, not deep, and turns it over the melted ring. The blood goes into the moss and does not stay there. Something in the trees sighs.{/n}
"They know your taste now as well as mine. That was stupid, hunter. They will come to your door as well, some winter, and I will not be there to tell them no."
{n}She binds your hand with the same rag she keeps for her own, without being asked, and without being gentle.{/n}
"Stupid," she says again, more quietly, and does not let go of the rag's end for a while.''',
        c("[Leave her to the frost]")),
    n("watched", "Soana", '''{n}She opens her palm along the old line, without a sound, and holds it over the melted ring until the moss stops drinking. Something in the trees sighs, and the ring begins to freeze over.{/n}
"There. Next winter again, and the winter after. Remember it the next time you are clever on somebody else's behalf."
{n}She wraps the hand the way other people tie a bootlace, and goes back into her cave.{/n}''',
        c("[Leave her to the frost]"))],
    requires=("trickster.ever", BLOOD), forbids=(*LOSS, CLOSED, "soana.trickster.cost.portion_shared", "soana.trickster.portion_watched"),
    delay=72)


# --- State 3, the missed window: crooked luck (F13) ---------------------------------------------------------------------

inline("soana.trickster.missed.dice_bowl", "An offering", 3,
    '[Drop your loaded die into her offering bowl] "For your spirits. It\'s weighted. It only ever lies in my favour."', [
    n("start", "Soana", '''{n}The die rattles in the bone bowl and stops twenty up. She tips the bowl and lets it roll again: twenty. Again: twenty. She fishes it out between two fingers, weighs it, and presses her thumbnail to the face with the single pip, where the lead is.{/n}
"Weighted. A cheat's luck, poured in lead, every throw you ever meant to win." {n}She drops it back into the bowl.{/n} "The spirits like a liar who says so. Spirits take what is offered. They do not say thank you, and neither do I."
{n}After that she does not touch it at all.{/n}''',
        c('[Leave it where it landed]', flags=(DICE,)))],
    requires=("trickster", "soana.after_quest"), forbids=(*LOSS, CLOSED, DICE), RequiresAny=DEFENDER,
    EntryMythic="PlayerIsTrickster")

inline("soana.trickster.missed.crooked_luck", "Crooked luck", 5,
    '[Look at the die in her bowl] "Still twenty up, shaman? I hear your beasts don\'t stay down."', [
    n("start", "Soana", '''{n}A she-bear lies across the cave mouth with her belly opened by a demon's claws. Soana kneels by her head with the bone bowl, and salt, and a smear of her own blood on the rim, and says something to the trees in a language that is mostly breath. The bear gets up, shakes herself and pads into the trees toward the road, bleeding as she goes.{/n}
"That is the third time she has done that. Your die has been in my bowl since the snow, and every night I have fed what is in it to the spirits, because an offering left unspent goes sour. My beasts go out against the demons on the road and they do not stay down. I did not ask for that, bloody hunter."''',
        c("Continue", "price")),
    n("price", "Soana", '''"You pledged your luck, and the spirits took you at your pledge. They have been feeding my beasts on it, and luck is thin fare. They will go on eating it for as long as that die sits in my bowl, and it is your luck they eat, hunter, not mine. Every time a bear of mine gets up on the road, something of yours falls down: a girth snaps, a letter goes astray, a sword turns in your hand at the wrong moment. Small things. Every one of them paid to a beast that is still standing."
"And send a cart of salt, so they have something besides your luck to chew. Leave the die, or take it and let them lie down."''',
        c('[Leave the die in her bowl] "Let them eat my luck."', crusade=("Materials", -50),
          flags=(LUCK_KEPT, CATCHUP, STARTED, "soana.trickster.cost.luck_fed")),
        c('[Take your die back and go]', flags=(LUCK_REFUSED,)))],
    requires=("trickster.ever", "soana.after_quest", DICE),
    forbids=("soana.progression_kept", *LOSS, CLOSED, "inhuman", LUCK_REFUSED, LUCK_KEPT), RequiresAny=DEFENDER,
    TricksterDevice=True, TricksterState="missed")

inline("soana.trickster.missed.late_luck", "Crooked luck, thrown late", 5,
    '[Throw your loaded die at her feet] "Weighted. It never rolls a one. Give it to your spirits."', [
    n("start", "Soana", '''{n}The die skips across the cave floor and stops at her feet, twenty up. She does not pick it up at once. She looks at it, then out at the cave mouth, where a she-bear has been dying all morning, and then at you.{/n}
{n}Then she takes it, weighs it, finds the lead with her thumbnail, and drops it into the bone bowl with salt and a smear of her own blood. She talks to the trees under her breath for a long time. Outside, the she-bear gets up on three legs and limps toward the road.{/n}
"You do not throw a pledge like that in front of my beasts without paying for it, hunter. The spirits heard it land. They will send my beasts out on your luck now whether I want them to or not, and they will come back hungry."''',
        c("Continue", "price")),
    n("price", "Soana", '''"They will eat your luck now, not mine: every time a beast of mine gets up on the road, something of yours falls down. And because you threw it at my feet instead of offering it, they will be hungrier than they would have been. Two carts of salt, so they do not eat you to the bone. The die stays with me. You threw it; you do not get it back."''',
        c('[Leave the die where it fell] "Salt, and the die. Let them eat."', crusade=("Materials", -100),
          flags=(DICE, LATE, LUCK_KEPT, CATCHUP, STARTED, "soana.trickster.cost.luck_fed")),
        c('[Refuse her terms] "No salt, and no die. I\'m not feeding your bears on my luck."', "refused", flags=(LUCK_REFUSED, LATE))),
    n("refused", "Soana", '''{n}She looks at you for a while. Then she puts two fingers into the bone bowl, through the salt and the blood, fishes the die out, spits on it, and says three words to the trees that sound like a door being barred.{/n}
"There. I have taken it off their plate. They had one taste, and they will remember the taste of you, not of me. That is your trouble now."
{n}She flicks the die at your chest. You catch it. Outside, the she-bear that limped toward the road an hour ago lies down in the ferns, and does not get up again.{/n}
"You threw it at my feet and then you would not pay for the throw. Take your lead and get out of my cave, hunter."''',
        c('[Pocket the die and go]'))],
    requires=("trickster", "soana.after_quest"),
    forbids=("soana.progression_kept", *LOSS, CLOSED, "inhuman", LUCK_REFUSED, DICE, LUCK_KEPT), RequiresAny=DEFENDER,
    TricksterDevice=True, TricksterState="missed", EntryMythic="PlayerIsTrickster")

inline("soana.trickster.missed.she_bear", "The she-bear", 5, '"How is your she-bear?"', [
    n("start", "Soana", '''{n}On the road up, your horse throws a shoe it was fitted with two days ago, and the dispatch that should have been waiting for you at the Wintersun camp has gone to Kenabres instead. You have stopped being surprised by that kind of thing.{/n}
{n}Soana is sitting on a stump outside the cave with the she-bear's great head in her lap. Someone has sewn the bear's belly shut with sinew, badly; judging by the old woman's fingers, it was the old woman.{/n}
"She went out again last night. She came back with a demon's hand in her mouth. The hand was still trying to get away."
{n}She scratches the bear behind one ear. The bear sighs like a bellows.{/n}''', c("Continue", "question")),
    n("question", "Soana", '''"Your luck keeps her standing. My spirits keep her walking. When the war ends, hunter, you will be the one holding the dice."
"When this war is done and the luck runs thin, and she lies down, will you let her stay down? Or will you roll again?"''',
        c('"I\'ll let her rest. She\'s earned it."', "rest", requires=(CREED,), flags=(TESTED, REST)),
        c('"I\'ll roll again. As long as it takes."', "roll", requires=(SAW_CAMELLIA,), flags=(TESTED, ROLL)),
        c('[Grin] "I\'ll roll for her. And if it comes up one, I\'ll call it twenty."', "cheat", flags=(TESTED, CHEAT)),
        c('"Why does it matter what I\'d do?"', "why"),
        c('"I\'ll let her rest. She\'s earned it."', "rest_plain", forbids=(CREED,), flags=(TESTED, REST)),
        c('"I\'ll roll again. As long as it takes."', "roll_plain", forbids=(SAW_CAMELLIA,), flags=(TESTED, ROLL))),
    n("why", "Soana", '''{n}She looks at you with those small black eyes, sunk deep in the driftwood.{/n}
"Because I am older than she is, hunter. Answer the question."''',
        c('"I\'ll let her rest. She\'s earned it."', "rest", requires=(CREED,), flags=(TESTED, REST)),
        c('"I\'ll roll again. As long as it takes."', "roll", requires=(SAW_CAMELLIA,), flags=(TESTED, ROLL)),
        c('[Grin] "I\'ll roll for her. And if it comes up one, I\'ll call it twenty."', "cheat", flags=(TESTED, CHEAT)),
        c('"I\'ll let her rest. She\'s earned it."', "rest_plain", forbids=(CREED,), flags=(TESTED, REST)),
        c('"I\'ll roll again. As long as it takes."', "roll_plain", forbids=(SAW_CAMELLIA,), flags=(TESTED, ROLL))),
    n("rest", "Soana", '''"A true protector is the one who sacrifices themselves. You heard me say it once, and you were listening. Hm."
{n}She goes back to scratching the bear's ear, and for a while she says nothing at all, which from her is a speech.{/n}''',
        c('[Leave them in the sun]')),
    n("rest_plain", "Soana", '''"Hm. A true protector is the one who sacrifices themselves. I have said that to better hunters than you, and not one of them listened. You I have not decided about."
{n}She goes back to scratching the bear's ear, and for a while she says nothing at all, which from her is a speech.{/n}''',
        c('[Leave them in the sun]')),
    n("roll", "Soana", '''"That is what a child says. A child with a toy it does not want to put away."
{n}She pulls a burr out of the bear's fur and flicks it at your boots.{/n}
"But it is honest. The last one who lied to me in this cave was your friend with the knife. Go away. I am thinking."''',
        c('[Leave them in the sun]')),
    n("roll_plain", "Soana", '''"That is what a child says. A child with a toy it does not want to put away."
{n}She pulls a burr out of the bear's fur and flicks it at your boots.{/n}
"But it is honest. Most who come up this path lie to me before they have their breath back. Go away. I am thinking."''',
        c('[Leave them in the sun]')),
    n("cheat", "Soana", '''{n}The old woman laughs so suddenly that the bear lifts her head.{/n}
"Of course you would. You would cheat the Abyss out of its teeth and call it a favour to the Abyss. I have met demons with better manners and worse ideas."
{n}She is still laughing, quietly, when you go.{/n}''',
        c('[Leave them in the sun]'))],
    requires=("trickster.ever", LUCK_KEPT), forbids=(*LOSS, CLOSED, TESTED), delay=48, optional=True)

BOWL_NIGHT = '''{n}She takes the bowl off the fire-stone with her bare hands and sets it between you. The die is still in it, twenty up.{/n}
"Then it stays. And so do you, tonight. I am too old to wait for you to guess."
{n}She washes the road off you herself, with water that smells of pine tar and is hotter than you would choose, scrubbing at your neck as if you were a pot. Then she stops scrubbing. She unlaces your shirt with the impatience she keeps for snares, drags it over your head, and reads what the war has written on you, every scar and bruise, with the frank interest of a woman reading tracks in snow.{/n}
"Hm. You heal badly. Good. Things that heal badly remember."'''
BOWL_THRESHOLD = '''{n}She lets you undo her in turn: the belt of knotted cord, the rags one over another, until the old dwarf woman stands in the firelight in nothing but the clay knot at her throat and her grey braid, broad and heavy and unashamed. She takes your hands by the wrists and puts them where she wants them.{/n}
{n}She kisses you with her whole small, heavy body behind it, and bites. When you gasp she laughs, low in her chest.{/n}
"Soft. I thought so." {n}She bites again, harder, where it will show tomorrow.{/n}
{n}Outside, the she-bear lies down across the cave mouth to keep the night off. Soana pushes you back into the furs, climbs over you with her knees sunk in the pelts on either side, and her hand closes on your hip like a root closing on a stone.{/n}'''
BOWL_MORNING = '''{n}Grey light at the cave mouth, and the she-bear's place across it empty. She is sitting up in the furs with her knees drawn up, rolling your die between her fingers. It keeps coming up twenty, because that is what lead does. She keeps frowning at it anyway.{/n}
"The she-bear went out before dawn. She will come back. Your luck is in my bowl, and you are in my bed, and the forest will have to put up with both of you until the war is done. Go on. The demons will not kill themselves."'''

inline("soana.trickster.missed.bowl", "The thing in her bowl", 5, '"You said you had been thinking."', [
    n("start", "Soana", '''{n}The bone bowl is on the fire-stone. Your die sits in it, one face up, as it has since the snow. There is a second blanket on her pallet, which there was not before.{/n}''',
        c("Continue", "rest", requires=(REST,)), c("Continue", "roll", requires=(ROLL,)),
        c("Continue", "cheat", requires=(CHEAT,)), c("Continue", "terms", forbids=(REST, ROLL, CHEAT))),
    n("rest", "Soana", '''"You said you would let her lie down. I have been turning that over like a stone, looking for the worm under it. There is no worm. I find that irritating."''',
        c("Continue", "terms")),
    n("roll", "Soana", '''"You said you would roll again as long as it takes. That is a child's answer. I have been alone with a demon in a bear for more winters than I care to count; I find I have a taste for children's answers."''',
        c("Continue", "terms")),
    n("cheat", "Soana", '''"You said you would call a one a twenty. I laughed. I have not laughed like that since before your crusade was born. I am still angry about it."''',
        c("Continue", "terms")),
    n("terms", "Soana", '''"Hear this first, because I will not say it in the furs. I had a husband. Corven. He laid a wreath of the first summer flowers on my head and I became his wife. He is gone, and I do not know where, or whether he lives. I will not dig him a grave to make room for you, and I will not pretend he never was. Take me with him in it, or do not take me."
"Now listen, hunter, because this is the whole of it. A thing that sits in my bowl is mine. I do not keep things I have not touched. Take your die out now, and everything it has done comes undone with it: the she-bear lies down at the cave mouth and stays there. Or leave it, and it is mine, and you with it, for as long as the luck holds."
"Which is to say, until I decide it does not."''',
        c('[Leave the die in the bowl] "Keep it. And me."', "night", flags=(COMMITTED, DIE_KEPT)),
        c('"Let me think about it."', "no"),
        c('[Take your die out of the bowl]', "taken"),
        c('"Leave the die where it is, and Corven\'s place where it is. I\'ll be your friend."', "friend", flags=(FRIENDS,))),
    n("friend", "Soana", '''{n}She puts the second blanket back on the shelf, without hurry.{/n}
"A friend who leaves a cheat's die in my bowl. Corven would have liked you. He liked fools." {n}She pushes a cup at you.{/n} "Drink. The die stays. So do the bears' bad manners. You may come when you like and leave before I am tired of you."''',
        c('[Go]')),
    n("no", "Soana", '''{n}She shrugs, and puts the second blanket back on the shelf.{/n}
"Think, then. The bowl is patient. I am not. If I have to ask twice, the bowl will want more than one die."''',
        c('[Go]', flags=(DECLINED,))),
    n("taken", "Soana", '''{n}You reach into the bowl. The die is warm. Outside, something large lies down across the cave mouth with a long sigh, and does not get up.{/n}
{n}Soana does not look at the door. She looks at you.{/n}
"There. Now you know what you are. Go."''',
        c('[Go]', flags=(CLOSED,))),
    n("night", "Soana", BOWL_NIGHT, c("Continue", "threshold")),
    n("threshold", "Soana", BOWL_THRESHOLD, c("Continue", "morning")),
    n("morning", "Soana", BOWL_MORNING, c('[Go]'))],
    requires=("trickster.ever", LUCK_KEPT, TESTED), forbids=(*LOSS, CLOSED, COMMITTED, DECLINED), delay=72, optional=True)

inline("soana.trickster.missed.second_ask", "The other die", 5, '"About your bowl."', [
    n("start", "Soana", '''{n}She sets the bowl on the stone between you, and holds out her other hand, palm up.{/n}
"A cheat never carries one die. One sits in my bowl. The other is in your pocket, the one you cheat your soldiers with at the fire. I know it is there. I can hear it when you walk."
"Give me its brother. A liar's pair belongs together, and it belongs with me. You can throw honest bones at your camp fires from now on, hunter, or none at all."''',
        c('[Give her the other die] "Keep them both. And me."', "night",
          flags=(COMMITTED, DIE_KEPT, "soana.trickster.cost.pair_given")),
        c('"No. That one stays with me."', flags=(CLOSED,))),
    n("night", "Soana", BOWL_NIGHT, c("Continue", "threshold")),
    n("threshold", "Soana", BOWL_THRESHOLD, c("Continue", "morning")),
    n("morning", "Soana", BOWL_MORNING, c('[Go]'))],
    requires=("trickster.ever", LUCK_KEPT, DECLINED), forbids=(*LOSS, CLOSED, COMMITTED), delay=96, optional=True)


# --- Epilogue pages (no mythic, alignment or crusade effects) ---------------------------------------------------------

EPILOGUE_PARAGRAPHS = (
    p("She took the Commander's half of the knot back only once, to retie it, and she pulled it tighter.", requires=(SECOND,)),
    p("The Wintersun beasts kept going out against the demons on the roads until the last of them was gone, and they kept "
      "getting up. The scouts stopped reporting it. It had become ordinary.", requires=(CATCHUP,)),
    p("For as long as the die sat in her bowl, the Commander's girths snapped, letters went astray and blades turned at bad "
      "moments. Each time, somewhere on a Wintersun road, a bear that should have stayed down got up again.",
      requires=("soana.trickster.cost.luck_fed",)),
    p("The Commander never threw a loaded die again. The pair sat in Soana's bowl, both twenty up, and nobody who visited "
      "the cave was allowed to touch them.", requires=("soana.trickster.cost.pair_given",)),
)

SCENES.append(scene("soana.trickster.epilogue.knot", "The second strand", "Epilogue", 5, "", [
    nar("start", '''{n}Soana took her leash back from the Commander's hand the night of the vow and tied it into her knot again, with the Commander's life at the other end. The Commander felt it pull on hungry nights for the rest of the war, in the wrist the knot had marked, and the wrist ached in cold weather ever after. When the war was over she began to plant the dead Wintersun woods, and, slowly, to bind the forest's broken things into the few that lived. She never thanked the Commander for anything, and she never let the knot go slack.{/n}''',
        c(), paragraphs=(
            p("The Commander wore the halves of the clay knot on a strip of gut for the rest of their life. When it chafed, "
              "Soana said that was how you knew it was working.", requires=(SPENT,)),
            p("The Commander wore her grey cord round the marked wrist for the rest of their life, and every spring she replaited it "
              "from her own braid, complaining the whole time. When it chafed, she said that was how you knew it was working.",
              forbids=(SPENT,)),
            *EPILOGUE_PARAGRAPHS))],
    requires=(RETURNED, BEARER), forbids=(CLOSED, "sacrifice"), last=99, Relationship="soana", ForbidOverrides=dict(SACRIFICE_BACK)))

SCENES.append(scene("soana.trickster.epilogue.luck", "The die in the bowl", "Epilogue", 5, "", [
    nar("start", '''{n}The die stayed in Soana's bowl after the war, twenty up, and the she-bear who had carried the Commander's luck to the roads grew grey in the muzzle and very fat. The Commander came to Wintersun whenever the world allowed it, and some times when it did not.{/n}
{n}Soana never admitted to missing anyone. She did keep the second blanket on the pallet, and she never once put it back on the shelf.{/n}''',
        c(), paragraphs=EPILOGUE_PARAGRAPHS)],
    requires=(LUCK_KEPT, COMMITTED), forbids=(CLOSED, RETURNED, "soana.late_campaign_kept", "sacrifice"), last=99,
    Relationship="soana", ForbidOverrides=dict(SACRIFICE_BACK)))

SCENES.append(scene("soana.trickster.epilogue.commit", "Your end", "Epilogue", 5, "", [
    nar("start", '''{n}Soana took her leash back from the Commander's hand alone, with one strand and her own blood, and it nearly killed her. She buried the dead forest one grave a day. The year after the Worldwound closed she walked all the way to Drezen with a knot in her fist, found the Commander, and tied it to their wrist without asking.{/n}
"Your end. I held it alone once. I will not do that twice."''',
        c(), paragraphs=EPILOGUE_PARAGRAPHS)],
    requires=(LATE_COMMITTED, RETURNED), forbids=(COMMITTED, CLOSED, DECLINED, FRIENDS, "sacrifice"), last=99, Relationship="soana",
    ForbidOverrides=dict(SACRIFICE_BACK)))

# b9c: the living, missed-window Soana whose luck was paid but whose bowl was never answered gets her own late page (the
# killed branch's leash and dead forest are not hers).
SCENES.append(scene("soana.trickster.epilogue.luck_late", "The rattle in the bowl", "Epilogue", 5, "", [
    nar("start", '''{n}The war ended before Soana finished thinking. She finished afterwards, on her own terms. The year after the Worldwound closed she walked all the way to Drezen with the loaded die in her fist, found the Commander, and put it in their palm.{/n}
"Your luck. It has rattled in my bowl since the snow and I am sick of the noise. Bring it back to Wintersun and keep it where I can hear it, and we will see how much of it is left."''',
        c(), paragraphs=EPILOGUE_PARAGRAPHS)],
    requires=(LATE_COMMITTED, LUCK_KEPT), forbids=(RETURNED, COMMITTED, CLOSED, DECLINED, FRIENDS, "sacrifice"), last=99, Relationship="soana",
    ForbidOverrides=dict(SACRIFICE_BACK)))

UNBOUND = p("She took her leash back from the Commander's hand the day they parted, with a single strand and her own blood. "
             "It held, barely, for as long as she lived. The knot hung in her cave with one strand, and she bound nothing new "
             "into the Wintersun woods again.", requires=(RETURNED,))

SCENES.append(scene("soana.trickster.epilogue.declined", "One strand", "Epilogue", 5, "", [
    nar("start", '''{n}She never asked again. When travellers asked the old woman in the cave about the Commander, she said that she had once met a hunter who could not make up their mind when it mattered, and that was all she said.{/n}''',
        c(), paragraphs=(UNBOUND,))],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED, "sacrifice"), last=99, Relationship="soana",
    ForbidOverrides=dict(SACRIFICE_BACK)))

SCENES.append(scene("soana.trickster.epilogue.unbound", "The leash", "Epilogue", 5, "", [
    nar("start", '''{n}The Commander never went back to Wintersun. Soana came to Drezen once, took her leash back from the Commander's palm with a single strand and most of her own blood, and left without a word. It held.{/n}
{n}The Wintersun woods grew quiet again. Travellers who asked the old woman in the cave about the Commander were told about a hunter who had held a dead woman to her own words. She did not say it kindly.{/n}''',
        c(), paragraphs=(
            p("\"Dug my graves with their own hands,\" she would add. \"Badly. And still walked away.\"", requires=(DUG,)),
            p("\"Paid Drezen to dig my graves,\" she would add, \"and walked away before the diggers had eaten my fish.\"",
              requires=(BOUGHT,)),
            p("\"Would not lift a spade for my dead,\" she would add. \"Turned round at my door and walked away.\"",
              requires=(LEFT,)),
        ))],
    requires=("trickster.ever", RETURNED, CLOSED), forbids=("sacrifice",), last=99, Relationship="soana",
    ForbidOverrides=dict(SACRIFICE_BACK)))

# Q10 r2: a lover from before her death who returned her but never took the knot's second strand.
SCENES.append(scene("soana.trickster.epilogue.unvowed", "One strand, old promises", "Epilogue", 5, "", [
    nar("start", '''{n}Soana took her leash back from the Commander's hand alone, with one strand and her own blood, and it nearly killed her. She lived. She buried the dead forest one grave a day and bound what she could into what was left.{/n}
{n}The Commander still came to her fire when the war allowed. She fed them, scolded them and took them to bed, and never once let them near the knot. "You had your chance at that," she said, and that was the end of it.{/n}''',
        c())],
    requires=("trickster.ever", RETURNED, COMMITTED), forbids=(BEARER, CLOSED, "sacrifice"), last=99, Relationship="soana",
    ForbidOverrides=dict(SACRIFICE_BACK)))

# Q10 r4: the Commander answered her Corven disclosure with friendship.
SCENES.append(scene("soana.trickster.epilogue.friends", "A friend at the fire", "Epilogue", 5, "", [
    nar("start", '''{n}The Commander stayed Soana's friend, which she said was the most tiresome thing anyone had ever been to her, and kept a second cup by the fire for them anyway.{/n}''',
        c(), paragraphs=(
            p("She took her leash back from the Commander's hand alone, with one strand and her own blood. It nearly killed her. "
              "She buried the dead forest one grave a day, and made the Commander dig every third one when they visited.",
              requires=(RETURNED,)),
            p("The loaded die stayed in her bowl, twenty up, and the she-bear who had carried it to the roads grew fat and grey.",
              requires=(LUCK_KEPT,), forbids=(RETURNED,)),
        ))],
    requires=("trickster.ever", FRIENDS), forbids=(COMMITTED, CLOSED, "sacrifice"), last=99, Relationship="soana",
    ForbidOverrides=dict(SACRIFICE_BACK)))

# Q10: the Commander gave their life at the Threshold and stayed dead. Every Trickster page above describes a living
# Commander, so this one page carries the knot, the leash and the die for that world.
SCENES.append(scene("soana.trickster.epilogue.slack", "The slack strand", "Epilogue", 5, "", [
    nar("start", '''{n}The Commander did not come back from the Threshold. Soana did not hear it from the riders. She was out at the cave mouth with a bowl of salt when it happened, and she knew.{/n}''',
        c(), paragraphs=(
            p("The knot on her wrist went slack all at once, the way a line goes slack when the fish is gone. Her end had been "
              "tied to the Commander's life, and that life had gone first, as she had told them it would. She cut the dead strand "
              "off with her knife, tied it round her own throat, and went on binding the Wintersun woods "
              "for twenty years more out of spite. She never said the Commander's name to anyone. She said \"the hunter\", and "
              "everyone knew.", requires=(RETURNED, BEARER)),
            p("The leash came back to her the night the Commander's hand stopped holding it: all of it at once, like a dropped "
              "rope. She caught it, went down on her knees under the weight, and held. It nearly killed her. It did not.",
              requires=(RETURNED,), forbids=(BEARER,)),
            p("Out on the Wintersun road, the she-bear that had stood up on the Commander's luck all winter lay down in the "
              "ferns that night and did not get up. Soana took the die out of the bowl and buried it with her, twenty up.",
              requires=(LUCK_KEPT,), forbids=(RETURNED,)),
        ))],
    requires=("trickster.ever", "sacrifice"), forbids=("trickster.commander_back", "soana.late_campaign_kept"),
    RequiresAnyGroups=[[RETURNED, LUCK_KEPT]], last=99, Relationship="soana"))


# --- Reactions (exactly Camellia, Ember and Ulbrig) ---------------------------------------------------------------------

CAMELLIA_GONE = ("camellia.dead", "camellia.killed", "camellia.kicked_out")
# Her retained death is lifted by her return (Camellia's own integrate does the same). camellia.killed stays closed on
# purpose: the veiled Camellia has no companion hub, and her own route answers Soana's return in person at Fye's
# (camellia_trickster.py, node "soana", gated on camellia.kill_returned.soana).
CAMELLIA_BACK = {"camellia.dead": "camellia.trickster.returned"}
EMBER_GONE = ("ember_dead", "ember_gone")
ULBRIG_GONE = ("ulbrig.dead", "ulbrig.kicked_out")

REACTIONS = [
    reaction("Camellia", "soana.trickster.react.camellia_portion", (BLOOD,),
             '''"You took a death off my plate, my friend. The old woman fed her trees and left me the smell of it." {n}Camellia smooths her skirt with both hands, very slowly.{/n} "Someone will pay me for that meal. I have not decided who. I have decided it will not be quick."''',
             answer_list=CAMELLIA_HUB, forbids=CAMELLIA_GONE, chapter=3, last=5, delay=24, entry='"About Soana..."',
             ForbidOverrides=dict(CAMELLIA_BACK)),
    reaction("Camellia", "soana.trickster.react.camellia_knot", (RETURNED, KILLED),
             '''"The old woman is walking again? I bled her myself. I felt her stop." {n}Camellia smiles, slowly, and does not blink.{/n} "How very interesting you make things. I wonder what else of mine you would take back, if I let you."''',
             answer_list=CAMELLIA_HUB, forbids=CAMELLIA_GONE, chapter=3, last=5, delay=24, entry='"About Soana..."',
             ForbidOverrides=dict(CAMELLIA_BACK)),
    reaction("Ember", "soana.trickster.react.ember_portion", (BLOOD,),
             '''"The old lady cut her own hand so nobody would cut her throat. That's the saddest clever thing I ever saw. You made her do it with a joke. I think she knew it was a joke. I think that's why she did it."''',
             answer_list=EMBER_HUB, forbids=EMBER_GONE, chapter=3, last=5, delay=24, entry='"About the old woman in the woods..."'),
    reaction("Ember", "soana.trickster.react.ember_luck", (CATCHUP,),
             '''"The scouts say the Wintersun bears keep getting up after the demons knock them down. That's your dice, isn't it? They must be so tired. I hope somebody lets them sleep when the fighting's over."''',
             answer_list=EMBER_HUB, forbids=EMBER_GONE, chapter=5, last=5, delay=24, entry='"About the Wintersun bears..."'),
    reaction("Ulbrig", "soana.trickster.react.ulbrig_knot", (LEASH, "ulbrig.talked"),
             '''"I asked you once what these new powers want in return, warchief. Now we know. That one wanted a hand on a demon's leash: yours, by the look of that palm. Every power must have a name, and a price that's fair. I'd call that fair, just about. Mind it doesn't pull you over in your sleep."''',
             answer_list=ULBRIG_HUB, forbids=ULBRIG_GONE, chapter=3, last=5, delay=24, entry='"About Soana..."'),
    reaction("Ulbrig", "soana.trickster.react.ulbrig_luck", (CATCHUP, "ulbrig.talked"),
             '''"The Wintersun crone's beasts are fighting demons on the road again, warchief. A she-bear with her guts hanging out stood up three times, the scouts say. Spirits don't do that for free. What did you give them? And what will they want next?"''',
             answer_list=ULBRIG_HUB, forbids=ULBRIG_GONE, chapter=5, last=5, delay=24, entry='"About the Wintersun beasts..."'),
]
SCENES.extend(REACTIONS)


# --- The registered route -----------------------------------------------------------------------------------------------

# The alive branches end on the registered pages; the portion and the die leave a mark there.
ALIVE_PARAGRAPHS = (
    p("Every winter the spirits came to the cave mouth for their portion, and every winter she cut her palm for them and "
      "cursed the Commander's name while she did it. She never missed a winter.", requires=(BLOOD,)),
    p("Some winters the spirits came to the Commander's door instead, wherever it was, and stood in the frost till dawn. The "
      "Commander learned to keep a knife by the threshold, and a rag, and to expect a letter from Wintersun a week later "
      "calling them stupid.", requires=("soana.trickster.cost.portion_shared",), forbids=("sacrifice",)),
    p("She kept a loaded die in her offering bowl until she died, twenty up. Nobody who visited the cave was allowed to touch it.",
      requires=(DICE,), forbids=(LUCK_REFUSED,)),
)
ALIVE_ENDINGS = ("kept_life", "chosen_visits", "familiar_company", "sacrifice", "beyond_the_forest")
# Q10 r2: the shared portion outlives a Commander who stayed dead; Soana pays both halves. (The living paragraph above
# forbids sacrifice, and the living endings that a returned Commander reaches carry it again with the override below.)
PORTION_ALIVE = ALIVE_PARAGRAPHS[1]
PORTION_DEAD = p("The winter after the Threshold the spirits came to Wintersun twice: once for her portion, and once for the "
                 "Commander's, which nobody alive was left to pay. Soana cut both palms and paid them both, every winter after, "
                 "and cursed the dead for leaving her the bill.", requires=("soana.trickster.cost.portion_shared",))


def _scene(by_id, id):
    if id not in by_id:
        raise ValueError("Soana Trickster integration missing scene: " + id)
    return by_id[id]


def _forbid(scene_, *flags):
    scene_["Forbids"] = [*scene_["Forbids"], *[f for f in flags if f not in scene_["Forbids"]]]


def _paragraphs(scene_, paragraphs):
    for node in scene_["Nodes"]:
        if all(ch.get("Next") is None for ch in node["Choices"]):
            node.setdefault("Paragraphs", []).extend(dict(x) for x in paragraphs)


def integrate(payload):
    """Save-safe edits to the registered route: no id, node or choice is renamed, removed or reordered."""
    rel = payload["Relationships"]["soana"]
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(x) for k, x in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, a Soana handed to Camellia may be taken at Camellia's word instead; a Soana "
                        "who died may be held to her own; and one whose visits were missed may be offered a loaded die for her bowl.")
    payload.setdefault("Presences", {}).update({k: dict(x) for k, x in PRESENCES.items()})
    items = payload.setdefault("RemovableItems", [])
    if MEDALLION not in items:
        items.append(MEDALLION)
    # R2-6: the late commit reads the return (killed branch; also the presence-failure fallback) or the luck paid for.
    payload.setdefault("Derived", {})[LATE_COMMITTED] = [["trickster.ever", RETURNED], ["trickster.ever", LUCK_KEPT]]
    by_id = {x["Id"]: x for x in payload["Scenes"]}

    # SOA-11: the loss pages belong to a Soana who stayed dead.
    for id in ("soana.ending_native_loss", "soana.ending_unfinished_loss"):
        _forbid(_scene(by_id, id), RETURNED)
    for name in ALIVE_ENDINGS:
        _paragraphs(_scene(by_id, "soana.ending_" + name), ALIVE_PARAGRAPHS)
    _paragraphs(_scene(by_id, "soana.ending_sacrifice"), (PORTION_DEAD,))
    # Ledger row 16: a Commander who came back from the sacrifice keeps the living endings (the mourning ones forbid it).
    for name in ("kept_life", "chosen_visits", "familiar_company"):
        scene_ = _scene(by_id, "soana.ending_" + name)
        if "sacrifice" in scene_["Forbids"]:
            scene_.setdefault("ForbidOverrides", {}).update(SACRIFICE_BACK)
            # A Commander who came back holds `sacrifice` too: the living portion paragraph must not drop out for them.
            _paragraphs(scene_, (dict(PORTION_ALIVE, Forbids=[], AnyGroups=[["trickster.commander_back"]]),))

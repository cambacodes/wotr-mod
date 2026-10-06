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
TRK_REFUSED = "soana.trickster.refused"   # NM1: set beside every Trickster-route closure (the Last Call coda cannot read soana.closed, G5)
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
# Polish (Sol INT): the leash is taken back in play (terms friendship, rebinding refused). The latch records the rite; the
# Derived reader also counts a save that finished either scene before the latch existed.
RECLAIMED = "soana.trickster.cost.leash_reclaimed"
RECLAIMED_BEFORE = "soana.trickster.leash_reclaimed_before_threshold"
POSTPONED = "soana.trickster.knot_proposal_postponed"   # Derived: the knot's own "not yet", never answered
# Polish (Sol BEL): the accounting at her graves, between the grave test and any vow. She makes the Commander answer for
# how she died, sets them to work for the dead forest's future, and decides for herself whether to invite more.
ACCOUNTING = "soana.trickster.returned.accounting"
ACC_ANSWERED = "soana.trickster.accounting_answered"
ACC_INVITED = "soana.trickster.accounting_invited"
ACC_FRIEND = "soana.trickster.accounting_friend"
ACC_REFUSED = "soana.trickster.accounting_refused"
STREAM = "soana.trickster.cost.stream_cleared"
NURSERY = "soana.trickster.cost.nursery_guarded"
OWN_KILL = "soana.killed_by_commander"              # Derived over the four native attack answers (SelectedAnswers below)
OWN_KILL_ANSWERS = {
    # [Attack] "I'm sick of your ravings, crone. Die!" (enGB be64dc8f / 7f2adcca)
    "soana.killed_self_before_bear": "4ceb5651b76b5cd4ba4227fb8c905c17",    # SoanaBeforeBear/Answer_0018
    "soana.killed_self_after_quest": "41427b1b6e18d2b46a8710deb79d4266",    # SoanaAfterQuest/Answer_0021
    # [Kill the shaman] "I've had enough of you and this place! To the Abyss with you!" (Shared stringkey da81261d)
    "soana.killed_self_after_bear_a": "fcf85a5f46511764ca2a85481a36cb2e",   # SoanaAfterBear/Answer_0013
    "soana.killed_self_after_bear_b": "7fa80df7d9584c943808aa8a7b9a3120",   # SoanaAfterBear/Answer_0097
    # [Execute the shaman] (enGB cf94657c "...a connection with a spirit from the Abyss can only lead to evil." / 6b7c9f4d
    # "You must answer for your evil deeds."); both cue chains lead to combat with her (audit r2).
    "soana.executed_after_bear_a": "49c746fc3ea9f2f4cb3841eb0eb69ba1",      # SoanaAfterBear/Answer_0030
    "soana.executed_after_bear_b": "91d7e849e995be24ca6f3886a14897e1",      # SoanaAfterBear/Answer_0096
}
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
    n("start", "Soana", '''{n}The old woman weighs you with her small black eyes, the way she would weigh a snare somebody else had set. Then she laughs, a cracked, rasping laugh, and draws her knife across her own palm. Blood runs off her knuckles into the moss. Somewhere in the trees, something answers: not a bird, not a wolf.{/n}
"A good cause. There. The spirits have had their portion, bloody hunter. Tell your hungry friend she can lick the moss."
{n}She wraps the hand in a rag without looking at it, the way other people tie a bootlace.{/n}''', c("Continue", "cost")),
    n("cost", "Soana", '''"Wipe that grin off your face. They know my taste now. Every winter they will come to the cave mouth for more, and I will have to open this hand again."
{n}She pulls the rag tight around her palm.{/n}
"Your friend would have taken my throat. I chose the hand. The forest will have its blood, and she can keep her knife hungry. Go, before you find something else of mine to offer."''',
        c('[Leave before she changes her mind]', native_next="fef727987297e8d4eb34068688fdac27", flags=(PRIMED, BLOOD)))])

# After the bear: Camellia has just spoken (Cue_0065/0069), so she is on screen and answers in her own voice.
for suffix, lst, nrc, nxt in (("after_bear_a", "001686714a5c2384ba09686b45bd033f", "726e936d05fde7a4798854a917b4b73d",
                               "c6b676fa989a5494cb6ce0c981979907"),
                              ("after_bear_b", "f7b5537dc61ccdc41b0732f0a1b700b2", "396b1d46a2cfb1e48b205468d4360ee9",
                               "74664ddd7bb36744ba825c29aad6f4b3")):
    portion(suffix, lst, nrc, '"You heard her: her blood serves the spirits. So let the spirits have it."',
        ("trickster",), ["camellia.claimed_soana_a", "camellia.claimed_soana_b"], [
        n("start", "Soana", '''{n}The old woman barks a laugh at Camellia and draws her knife across her palm. Blood runs into the moss. Something answers from the trees.{/n}
"There, spirit talker. The spirits have had their portion, from my own hand. You can lick what is left."
{n}Soana winds a rag around the cut and pulls it tight with her teeth.{/n}
"They know my taste now. Every winter they will come for more, and I will have to bleed again. Better my hand than my throat. Remember that before you start grinning, bloody hunter."''', c("Continue", "camellia")),
        n("camellia", "Camellia", '''{n}Camellia watches the blood soak into the ground with the fixed attention of a cat at a closed door. Her smile does not move at all.{/n}
"How very generous of her. And of you, my friend. You have taken a death off my plate in front of the one audience I cared about." {n}She wets her lips.{/n} "I do not forget who takes food off my plate. I shall be thinking of you, often, and very carefully."''',
            c('[Leave before either of them decides otherwise]', native_next=nxt, flags=(PRIMED, BLOOD)),
            speaker_unit=CAMELLIA)])


# --- State 2, killed: the knot never checked (F17, her own words read in the other direction) --------------------------

SCENES.append(scene("soana.trickster.killed.knot", "The knot never checked", "Soana", 3, "", [
    nar("start", """{n}You go back to Wintersun alone, on a grey morning, with the crusade's business waiting behind you. The forest died with her: the undergrowth is black, the birds are gone, and something in the black trees howls beyond the cave. Soana's cave smells of cold ash and something sweeter under it. Nobody has taken her bones to the ground.{/n}
{n}Something out in the trees stops moving when you step inside.{/n}""",
        c("Continue", "orso", forbids=(GUARDIAN_DEAD,)), c("Continue", "spirit", requires=(GUARDIAN_DEAD,))),
    nar("orso", """{n}Orso comes to the cave mouth and will not come further. He paces before it, turns at the entrance, and paces back. The brand on his shoulder is a knot, the same knot she wore in clay at her throat, and it has not faded. Whatever she tied to him has not come untied, by the look of it.{/n}""",
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
        c('[Leave the knot tied] "No. She said she was finished. Let her be finished."', flags=(CLOSED, TRK_REFUSED,))),
    nar("marks", """{n}You crouch where she fell. Her hands are grey but whole; the smell of cold ash catches in your throat. On the rock above her pallet the same knot is scratched in charcoal, over and over, the knot of her clay medallion and of the brand on Orso's hide; and beside it, small, the way a trapper keeps a tally, three marks: a bear, a horned thing with too many teeth, and a stooped little figure with a braid.{/n}
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
        c('[Leave the knot tied] "No. She said she was finished. Let her be finished."', flags=(CLOSED, TRK_REFUSED,))),
    nar("carcass", """{n}Orso lies where he fell, and dark fluid stains the fur beneath him. The grass has died in a ring around it, the way grass dies around a poisoned well. The brand on his shoulder is a scar on dead hide. Whatever she bound into him, it is not answering: you press two fingers to the brand and feel nothing but cold fur.{/n}
{n}If there is anything left to pull on, you will have to give it something to hold first.{/n}""",
        c('[Cut her knot into the dead hide, bleed into the cuts, and wait for something to come to it] "A knot is a door as well as a rope. Let us see who knocks."',
          "bait", alignment=("Chaotic", 1), flags=(BAITED,)),
        c('[Leave the knot cut] "She said she was finished. Let her be finished."', flags=(CLOSED, TRK_REFUSED,))),
    nar("pelt", """{n}Orso is what the medallion left of him: a grey pelt stretched over bones, where he dropped when his teeth ground the clay knot to dust. The brand is still on the pelt, a scar on a dead thing, and the knot that held it is gone. You press two fingers to it and feel nothing but cold fur.{/n}
{n}If there is anything left to pull on, you will have to tie the knot again yourself, and give it something to hold.{/n}""",
        c('[Cut her knot into the dead hide, bleed into the cuts, and wait for something to come to it] "A knot is a door as well as a rope. Let us see who knocks."',
          "bait", alignment=("Chaotic", 1), flags=(BAITED,)),
        c('[Leave the knot cut] "She said she was finished. Let her be finished."', flags=(CLOSED, TRK_REFUSED,))),
    nar("bait", """{n}You copy the brand into the hide with your knife, line by line, following the old scar, and then you open your palm and press it into the cuts until the hide is dark with you. It is a gamble, and you know it: that a knot cut in blood is a door as well as a rope, and that something at the Worldwound's edge will come to an open door. Then you sit down beside it in the cold and wait.{/n}
{n}Near dawn the black trees go quiet. Something comes down out of them that you never see, and the cut knot in the hide drinks, and goes on drinking after your blood is gone. Behind you, on the cold floor of the cave, the dead woman's hand closes on nothing.{/n}
{n}So the knot holds again, and she is on it. What is on the far end you cannot say: something of hers come back to its knot, or something new that found the door you cut. The knot is not cut now: when you pull, she answers. A rope that can be pulled one way can be pulled the other.{/n}""",
        c('[Press her clay medallion into the cuts and bargain with what holds the other end] "Whatever you are: give her back, and pull on me instead."',
          "wake_clay", mythic="Trickster", alignment=("Chaotic", 1), requires=("soana.medallion_held",), remove_item=MEDALLION,
          flags=(RETURNED, STARTED, GUARDIAN, SPENT, LEASH)),
        c('[Lay your cut hand on the knot and bargain with what holds the other end] "Whatever you are: give her back, and pull on me instead."',
          "wake_brand", mythic="Trickster", alignment=("Chaotic", 1), forbids=("soana.medallion_held",),
          flags=(RETURNED, STARTED, GUARDIAN, LEASH)),
        c('[Leave it] "No. She said she was finished. Let her be finished."', flags=(CLOSED, TRK_REFUSED,))),
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
    # Polish r4 (coordinator ruling; user rule "a player-chosen kill stands"): a Commander who killed her with their own
    # hands (any of the six native attack/kill/execution answers) gets no return: canon stands and her route closes
    # (epilogue.by_your_hand, with Camellia's and Ulbrig's words on it). The knot answers Camellia's kill or an unattributed death.
    # The own-kill nodes downstream (accounting own/own_lover, rebind own, the clay token) stay for saves that returned her
    # before this ruling; new play cannot reach them.
    ], requires=("trickster", "trickster.ever"), forbids=(RETURNED, CLOSED, OWN_KILL), delay=0, last=5, Relationship="soana",
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
        c('[Leave her with her graves]', flags=(CLOSED, TRK_REFUSED, LEFT))),
    nar("dug", """{n}The ground is frozen for the first hand's depth and roots all the way down after that. You dig until the light goes, one-handed half the time, because the other hand keeps closing on nothing when the leash pulls. Soana does not help. She sits on a stone and tells you when you are doing it wrong, which is often, and when the hind and her calf finally go in she says something over them in a language that sounds like branches knocking.{/n}""",
        c('[Wipe your hands]', "decide")),
    nar("bought", """{n}You write the order on a leaf torn from your dispatch book: diggers from Drezen, as many as will come, paid from the crusade's chest before they set out. Soana watches you press the seal. She does not offer you the spade again. She drives it into the half-dug hole beside the hind, and there it stays.{/n}""",
        c('[Send the order]', "decide")),
    s("decide", """{n}She leans on the spade and looks at you the way she looks at weather.{/n}
"Hear me, hunter, because I will say it once. The dead forest I will bury with you or without you. That is the forest's business, and it does not buy you anything from me. My leash I will take back from your hand whatever you say; I do not leave my work in a stranger's fist. What you want from me is another matter, and I have not decided what I think of it."
"Come back in three days. You will answer me for something then, before you ask me for anything else.\"""",
        c('"Three days, then."'),
        c('"Your graves are seen to. That\'s all I came for."', flags=(CLOSED, TRK_REFUSED,))),
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
    s("bought", '''"Your diggers came, dug, ate my last smoked fish and left. Then you put your own hands in my stream. I saw both, hunter. Do not try to pass one off as the other."''',
        c("Continue", "price", forbids=(SPENT,)), c("Continue", "price_clay", requires=(SPENT,))),
    s("price", '''{n}She opens her hand. In it lies the thing she sat plaiting on her stone by the graves while the digging went on: a cord of grey hair from her own braid, twisted with sinew and tied in the knot that is printed white on your palm. The end of her braid is ragged where the knife went through it.{/n}
"Hear this first, because I will not say it in the furs. I had a husband. Corven. He laid a wreath of the first summer flowers on my head and I became his wife. He is gone, and I do not know where, or whether he lives. I will not dig him a grave to make room for you, and I will not pretend he never was. Take me with him in it, or do not take me."
"I told you to come for me, and you came. I want you here tonight, hunter. Curse you, I have been thinking about it when I should have been counting seed."
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
"Go, then. I will keep my knot. Come back when you can say 'mine first' and mean it."''',
        c('[Go]', flags=(DECLINED,))),
    s("fool", '''"I found one already. {mf|He|She} pulled me back into a dead forest and is still holding my leash. Now {mf|he|she} wants to send me hunting for another."
{n}She shuts her hand over the knot and turns her back.{/n}''',
        c('[Go]', flags=(CLOSED, TRK_REFUSED,))),
    s("night", TERMS_NIGHT, c("Continue", "morning")),
    s("morning", TERMS_MORNING, c('[Go]')),
    s("friend", '''{n}She looks at you for a long breath, then snorts.{/n}
"A friend. Hm. Corven had friends too. He never once told them where I kept the mead."
{n}She takes your marked hand without asking and turns the palm up. Her knife opens her own palm along an old white line; she presses the cut to the print on yours and talks to the knot through her teeth, in the language that sounds like branches knocking. The pull goes out of your wrist. Soana sits down hard on the stone by the grave and keeps hold of your hand until her own stops shaking. Then she pushes it away.{/n}
"Mine again. You may come and eat my fish and be useless at my graves. Do not look at me like that."''',
        c('[Go]', flags=(RECLAIMED,))),
    s("price_clay", '''{n}She opens her hand. The two halves of the clay knot lie in it, the medallion you cracked at the brand; she picked them out of the ash of her own cave.{/n}
"Hear this first, because I will not say it in the furs. I had a husband. Corven. He laid a wreath of the first summer flowers on my head and I became his wife. He is gone, and I do not know where, or whether he lives. I will not dig him a grave to make room for you, and I will not pretend he never was. Take me with him in it, or do not take me."
"I told you to come for me, and you came. I want you here tonight, hunter. Curse you, I have been thinking about it when I should have been counting seed."
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
    # NM1 (Sol INT): a luck-chain "not yet" (missed.bowl) shares soana.trickster.declined; after her return it no longer
    # bars the knot's own first ask (the return lifts it). The knot's own "not yet" is kept out by this scene's completion.
    ], requires=("trickster.ever", RETURNED, GRAVE_KEPT, ACC_INVITED), forbids=(CLOSED, COMMITTED, DECLINED, FRIENDS, "soana.trickster.returned.terms"), delay=72,
    ForbidOverrides={DECLINED: RETURNED})

at_cave("soana.trickster.returned.second_ask", "Tied tighter", '"The ground has thawed."', [
    s("start", '''{n}She does not wait for you to reach the cave. She comes down the path to meet you with the knot already in her fist and a strip of fresh gut over her shoulder, and she takes your wrist before you can say anything at all.{/n}
"You made me say it twice. I do not say things twice. So the knot will remember that it had to be asked twice, and so will you."
{n}She sets the edge of her knife against the inside of your wrist, where the pulse is, and waits.{/n}''',
        c("Continue", "price")),
    s("price", '''"Deeper than last time would have been. It will scar white and it will ache every winter you live, and every time it aches you will know whose it is. Hold out your hand or take it back. I will not ask a third time."''',
        c('[Hold out your wrist] "Mine first."', "cut", forbids=(SPENT,), flags=(COMMITTED, BEARER, SECOND)),
        c('[Take your hand back] "No. Not like this."', flags=(CLOSED, TRK_REFUSED,)),
        c('[Hold out your wrist] "Mine first."', "cut", requires=(SPENT,), flags=(COMMITTED, BEARER, SECOND))),
    s("night", TERMS_NIGHT, c("Continue", "morning")),
    s("morning", '''{n}The fire has gone to ash and the frost has come in over the cave mouth as far as the furs. Her end of the knot is gone from her wrist; yours is still tied, and under it the cut has closed into a hard ridge, already paler than the skin around it.{/n}
{n}Soana is outside already, feeding the spirits from a bowl. She does not turn around.{/n}
"That will scar white. Every winter it aches, you will know whose it is. Now go and fight your war, hunter, and do not die before I do. It would be very inconvenient."''',
        c('[Go]')),
    s("night_clay", TERMS_NIGHT_CLAY, c("Continue", "morning")),
    # Polish (Sol BEL, audit r2): the deeper cut she priced is shown, and it heals as she said it would.
    s("cut", '''{n}She does not hurry. The knife goes in along the inside of your wrist, deeper than any binding needs, and she draws it the length of her thumb while you watch. Blood runs down into your palm and over the white print. She presses the cut shut with her thumb and holds it there until your pulse beats against her hand.{/n}
"Now it is written in you, hunter. Not on you."''',
        c("Continue", "night", forbids=(SPENT,)), c("Continue", "night_clay", requires=(SPENT,))),
    # PP6 (Sol INT): the knot's second ask follows the knot's own first ask; a luck-chain "not yet" (missed.bowl) shares
    # soana.trickster.declined, so the graveyard test and the terms scene are required by name.
    # Polish (Sol INT): a luck "not yet" carried into the knot's friendship is not a postponed knot; the friend's leash is hers.
    ], requires=("trickster.ever", RETURNED, DECLINED, GRAVE_KEPT, "soana.trickster.returned.terms"),
    forbids=(CLOSED, COMMITTED, FRIENDS, RECLAIMED_BEFORE), delay=96)

# Q10 r2: a lover committed before she died (the registered courtship, then the handover or the Commander's own kill)
# still owes the knot its second strand. The terms and the second ask forbid soana.committed, so this is that vow.
at_cave("soana.trickster.returned.rebind", "An old promise, a new knot", '"You said three days."', [
    s("start", '''{n}The grave is a low mound under the ferns. She has laid stones on it in a pattern you almost recognize. She does not get up.{/n}''',
        c("Continue", "camellia", requires=(KILLED,)), c("Continue", "own", requires=(OWN_KILL,), forbids=(KILLED,)),
        c("Continue", "unknown", forbids=(KILLED, OWN_KILL))),
    s("camellia", '''"You courted me. You sat at my fire and ate my fish and called me beloved, and I let you. Then you stood outside my cave while your spirit talker opened my throat, because she asked nicely. You answered me for that by the graves, and I have watched what your hands did afterwards."
{n}She turns a stone on the mound with one finger, so the pattern comes right.{/n}
"You came back when I told you to come for me. I wanted you to. I am still angry about that, and I will be angry a long while yet."''',
        c("Continue", "price")),
    s("own", '''"You courted me. You sat at my fire and ate my fish and called me beloved, and I let you. Then you killed me with your own hands, in my own cave. You answered me for that by the graves, and I have watched what your hands did afterwards."
{n}She turns a stone on the mound with one finger, so the pattern comes right.{/n}
"You came back when I told you to come for me. I wanted you to. I am still angry about that, and I will be angry a long while yet."''',
        c("Continue", "price")),
    s("price", '''{n}She opens her hand. The knot is in it.{/n}
"What we said before I died was said to a living woman with a whole knot. This one has one strand, and you are holding my leash in your bare hand. If I am to take it back and keep it, the other end needs a life on it. Yours. When I die again, it is your life the knot comes looking for first."
"Old promises do not tie knots, hunter. Say it new or do not say it."''',
        c('[Hold out your hand] "Mine first."', "night", forbids=(SPENT,), flags=(BEARER, BOUND_AGAIN)),
        c('"No. Not this. Not my life on your knot."', "refuse", flags=(REBIND_DECLINED,)),
        c('[Hold out your hand] "Mine first."', "night_clay", requires=(SPENT,), flags=(BEARER, BOUND_AGAIN))),
    s("refuse", '''{n}She closes her fist over the knot.{/n}
"Then I hold it alone."
{n}She takes your marked hand and opens her own palm with the knife. Her blood runs between your fingers while she talks to the knot, low and fast, and the pull goes out of your wrist. Her knees give; she sinks onto the edge of the mound and keeps her fist shut until she can stand again.{/n}
"There. That was your doing too, and it did not kill me, so do not flatter yourself. You may still come to my fire. You will keep your hands off my knot, and off anything else of mine that matters."''',
        c('[Go]', flags=(RECLAIMED,))),
    s("night", TERMS_NIGHT, c("Continue", "morning")),
    s("morning", TERMS_MORNING, c('[Go]')),
    s("night_clay", TERMS_NIGHT_CLAY, c("Continue", "morning")),
    # Polish: a death the save cannot attribute (no native attack answer, no Camellia etude) accuses nobody by name.
    s("unknown", '''"What we said before I died was said to a living woman. You answered me by the graves, you stayed for the work, and you came back when I told you to."
{n}She turns a stone on the mound with one finger, so the pattern comes right.{/n}
"I wanted you to. Do not make me say it twice."''',
        c("Continue", "price")),
    ], requires=("trickster.ever", RETURNED, GRAVE_KEPT, COMMITTED, ACC_INVITED), forbids=(CLOSED, BEARER, REBIND_DECLINED, FRIENDS), delay=72)


# Polish (Sol BEL, the Q10 residual): between the grave test and any vow, the accounting. The Commander answers for how
# she died (Camellia, their own hands, or a death the save cannot attribute), works for the dead forest's future under her
# eye, and she decides whether to invite more. Returning her buys nothing; an old lover's vow is no exception.
CLOSE_FLAGS = dict(flags=(CLOSED, TRK_REFUSED, ACC_REFUSED))


def _history_choices():
    return (c("Continue", "camellia", requires=(KILLED,), forbids=(COMMITTED,)),
            c("Continue", "own", requires=(OWN_KILL,), forbids=(KILLED, COMMITTED)),
            c("Continue", "unknown", forbids=(KILLED, OWN_KILL)),
            c("Continue", "camellia_lover", requires=(KILLED, COMMITTED)),
            c("Continue", "own_lover", requires=(OWN_KILL, COMMITTED), forbids=(KILLED,)))


def _answers(admission):
    return (c(admission, "answered", flags=(ACC_ANSWERED,)),
            c('"I brought you back. Isn\'t that answer enough?"', "evasive"),
            c('"I won\'t answer for it. I\'m leaving."', "dismiss", **CLOSE_FLAGS))


ACC_DOWN = """{n}She leads you down to the water under the bare branches. She carries the seed bowl herself.{/n}"""
ACC_DIGGERS = """{n}Your diggers from Drezen are at the far end of the row of graves, crusaders with good boots and bad manners, arguing about who has to carry the calf. Soana sends one back for it without raising her voice and watches until he picks it up. Then she turns her back on them and points you at the water.{/n}"""
ACC_WORK = """{n}The thing in the upper channel is a stag, swollen with water. You get your arms under it and drag it up the bank, and when the leash pulls, your marked hand closes on the wet hide and will not open. Soana waits until it does. Then she points at the next snag.{/n}
{n}The water runs brown, then clear. You drive the stakes into stony ground and weave dead branches between them, and she makes you pull the fence up and set it wider, twice. At last she kneels inside it and presses the seed into the wet earth one at a time, with her thumb.{/n}
"They will need water carried when the stream runs low, and boots kept off them. I will be here.\""""

at_cave(ACCOUNTING, "What you left alive", '"I came back, as you said."', [
    nar("start", """{n}Soana is waiting by the last grave with her walking stick laid across the path at knee height. Behind her, against the rock, lie a bundle of split stakes and a clay bowl of seed. She does not move the stick.{/n}""",
        *_history_choices()),
    s("camellia", '''"You gave me to your spirit talker. Not a stag, not a hide to be split after the hunt. Me. An old woman in her own cave, and you let her have me because she asked."
{n}Her knuckles whiten on the stick.{/n}
"Was she hungry, hunter? Did that make it easy?"''',
        *_answers('"She asked, and I let her kill you. I knew what I was giving her."')),
    s("own", '''"You killed me in my own cave. You found your way back to my door easily enough. Now find your way back to that day."
{n}She taps the frozen earth with the stick.{/n}
"What was I to you, hunter? An old woman who would not do as she was told?"''',
        *_answers('"I chose to kill you. That was my doing, no one else\'s."')),
    s("unknown", '''"I died here. You came afterwards and pulled at my knot and told it what to do with my life. Now you will hear what I mean to do with it."''',
        c('"Then say it. I\'m listening."', "answered", flags=(ACC_ANSWERED,)),
        c('"I brought you back. Isn\'t that answer enough?"', "evasive"),
        c('"Keep your cave. I\'m leaving."', "dismiss", **CLOSE_FLAGS)),
    s("camellia_lover", '''"You came to this cave as my lover. I made room for you at my fire. Then you stood outside it while your spirit talker opened my throat."
{n}She plants the stick between your boots.{/n}
"When she asked you for me, did you remember what you had asked me for? Answer me, hunter."''',
        *_answers('"I remembered. I gave you to her anyway. That was my choice."')),
    s("own_lover", '''"You came to this cave as my lover. I made room for you at my fire. Then you killed me beside it, with your own hands."
{n}She plants the stick between your boots.{/n}
"Did you remember what you had asked me for, when you did it? Answer me, hunter."''',
        *_answers('"I remembered. I killed you anyway. That was my choice."')),
    s("evasive", '''"That answers the knot. I asked you."
{n}She lifts the stick off the path and points it at the graves.{/n}
"A thing can be done twice and mean two different things. Do not expect the second to bury the first."''',
        c('"Bringing you back buys me nothing from you. Ask me again."', "repeat"),
        c('"I\'m not staying to hear this."', "dismiss", **CLOSE_FLAGS)),
    s("repeat", '''{n}Soana lays the stick across the path again, at the same height.{/n}
"Then answer me. Not the knot. Me."''',
        c('"She asked, and I let her kill you. I knew what I was giving her."', "answered", requires=(KILLED,), forbids=(COMMITTED,), flags=(ACC_ANSWERED,)),
        c('"I chose to kill you. That was my doing, no one else\'s."', "answered", requires=(OWN_KILL,), forbids=(KILLED, COMMITTED), flags=(ACC_ANSWERED,)),
        c('"Then say it. I\'m listening."', "answered", forbids=(KILLED, OWN_KILL), flags=(ACC_ANSWERED,)),
        c('"I remembered. I gave you to her anyway. That was my choice."', "answered", requires=(KILLED, COMMITTED), flags=(ACC_ANSWERED,)),
        c('"I remembered. I killed you anyway. That was my choice."', "answered", requires=(OWN_KILL, COMMITTED), forbids=(KILLED,), flags=(ACC_ANSWERED,)),
        c('"I\'m not staying to hear this."', "dismiss", **CLOSE_FLAGS)),
    s("answered", '''"Hm. So your tongue has one honest use."
{n}She moves the stick aside.{/n}
"The stream below the graves still runs. There is something rotting in its upper channel, and I have seed that wants clean water. I carried it in from beyond the dead ground; nothing in this wood is left to give me any."
"Clear the channel. Then fence the bed below it, before your soldiers drag another cart across it. If there is to be a forest here again, it will start with something too small for a bloody hunter to notice."''',
        c('[Take the stakes] "Show me where."', "down"),
        c('"I\'ll do the work as your friend. Nothing more."', "down_friend"),
        c('"You\'ve had enough of my time."', "dismiss", **CLOSE_FLAGS)),
    nar("down", ACC_DOWN, c("Continue", "diggers", requires=(BOUGHT,)), c("Continue", "work", forbids=(BOUGHT,))),
    nar("down_friend", ACC_DOWN, c("Continue", "diggers_friend", requires=(BOUGHT,)), c("Continue", "work_friend", forbids=(BOUGHT,))),
    nar("diggers", ACC_DIGGERS, c("Continue", "work")),
    nar("diggers_friend", ACC_DIGGERS, c("Continue", "work_friend")),
    nar("work", ACC_WORK, c('[Set the last branch]', "judged", flags=(STREAM, NURSERY))),
    nar("work_friend", ACC_WORK, c('[Set the last branch]', "friend", flags=(STREAM, NURSERY))),
    s("judged", '''{n}She tests the fence with the head of her stick. It holds. She looks up at you.{/n}
"You stayed when there was nothing here to conquer. You put your hands where I told you. I wanted to see if you could."
"I have not forgotten what was done to me here, and I will not forget it because the water runs clear."
{n}She tucks the seed bowl under her arm.{/n}
"Come again in three days. Come for me, if that is what you came for. I want to see whether I want you at my fire when the work is done."''',
        c('"I\'ll come for you."', flags=(ACC_INVITED,)),
        c('"Keep the fire for a friend."', "friend"),
        c('"There won\'t be another visit."', "dismiss", **CLOSE_FLAGS)),
    s("friend", '''"A friend, then. I have a use for one who can lift a dead stag without making a speech about it."
{n}She takes your marked hand, turns the palm up and opens her own with the knife. She presses the cut to the print and talks to the knot through her teeth. The pull goes out of your wrist. Her knees go; she catches herself on the stick, waits, and stands straight again.{/n}
"There. My work is in my own hands again. Come when you have something to say. Bring water when you have not."''',
        c('[Leave her by the seed bed]', flags=(FRIENDS, ACC_FRIEND, RECLAIMED))),
    s("dismiss", '''"Go, then. My seed will not wait for your pride to ripen."
{n}She turns to the water with the bowl under her arm.{/n}''',
        c('[Go]')),
    ], requires=("trickster.ever", RETURNED, GRAVE_KEPT),
    forbids=(CLOSED, FRIENDS, BEARER, REBIND_DECLINED, ACC_INVITED, ACCOUNTING, "soana.trickster.returned.terms"), delay=72)


# The portion comes due (audit: the recurring blood price must be witnessed, not only promised). The first winter after
# the handover, on her own list: the spirits come to the cave mouth, and the Commander can pay it or watch her pay it.
inline("soana.trickster.handover.winter_portion", "The spirits' portion, again", 5, '"The spirits came, didn\'t they?"', [
    n("start", "Soana", '''{n}Frost covers the moss. Before the cave mouth a ring has melted, as wide as a cart wheel. Soana sits beside it with her knife across her knees. Old cuts cross her left palm; she runs a thumb along one white scar.{/n}
"They came at moonrise. Stood there till dawn. The blood I gave them left them hungry for more, and now they know the path to my door. Every winter, hunter. This one, and the next."
{n}She turns the knife toward the light and looks at you.{/n}
"Stay and watch. You were quick enough to offer my blood. Let us see how quick you are to look away."''',
        c('[Hold out your own palm] "My joke. My blood. Pay them from me this winter."', "shared",
          flags=("soana.trickster.cost.portion_shared",)),
        c("[Watch her pay it]", "watched", flags=("soana.trickster.portion_watched",))),
    n("shared", "Soana", '''{n}She looks at your hand the way she looks at a snare that has caught the wrong animal. Then she takes your wrist in her root-hard fingers and draws the knife across your palm, not deep, and turns it over the melted ring. The blood goes into the moss and does not stay there. Something in the trees sighs.{/n}
"They know your taste now as well as mine. That was stupid, hunter. They will come to your door as well, some winter, and I will not be there to tell them no."
{n}She binds your hand with the same rag she keeps for her own, without being asked, and without being gentle.{/n}
"Stupid," {n}she says again, more quietly, and does not let go of the rag's end for a while.{/n}''',
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
"That is the third time she has done that. You left your die in my bowl. I fed its luck to the spirits, and now look what they have done with it. My beasts go out against the demons on the road and they do not stay down. I did not ask for that, bloody hunter."''',
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
{n}She flicks the die at your chest. You catch it. Outside, the she-bear that limped toward the road lies down in the ferns, and does not get up again.{/n}
"You threw it at my feet and then you would not pay for the throw. Take your lead and get out of my cave, hunter."''',
        c('[Pocket the die and go]'))],
    requires=("trickster", "soana.after_quest"),
    forbids=("soana.progression_kept", *LOSS, CLOSED, "inhuman", LUCK_REFUSED, DICE, LUCK_KEPT), RequiresAny=DEFENDER,
    TricksterDevice=True, TricksterState="missed", EntryMythic="PlayerIsTrickster")

inline("soana.trickster.missed.she_bear", "The she-bear", 5, '"How is your she-bear?"', [
    n("start", "Soana", '''{n}On the road up, your horse throws a shoe, and the dispatch that should have been waiting for you at the Wintersun camp has gone to Kenabres instead. You have stopped being surprised by that kind of thing.{/n}
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
    n("start", "Soana", '''{n}The bone bowl is on the fire-stone. Your die sits where you left it, twenty up. There is a second blanket on her pallet, which there was not before.{/n}''',
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
        c('[Go]', flags=(CLOSED, TRK_REFUSED,))),
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
        c('"No. That one stays with me."', flags=(CLOSED, TRK_REFUSED,))),
    n("night", "Soana", BOWL_NIGHT, c("Continue", "threshold")),
    n("threshold", "Soana", BOWL_THRESHOLD, c("Continue", "morning")),
    n("morning", "Soana", BOWL_MORNING, c('[Go]'))],
    requires=("trickster.ever", LUCK_KEPT, DECLINED), forbids=(*LOSS, CLOSED, COMMITTED), delay=96, optional=True)


# --- Epilogue pages (no mythic, alignment or crusade effects) ---------------------------------------------------------

EPILOGUE_PARAGRAPHS = (
    p("{n}The cut she made at the second asking healed into a white scar inside the Commander's wrist. It ached every winter, "
      "as she had promised, and she never once asked whether it did.{/n}", requires=(SECOND,)),
    p("{n}The Wintersun beasts kept going out against the demons on the roads until the last of them was gone, and they kept "
      "getting up. The scouts stopped reporting it. It had become ordinary.{/n}", requires=(CATCHUP,)),
    p("{n}For as long as the die sat in her bowl, the Commander's girths snapped, letters went astray and blades turned at bad "
      "moments. Each time, somewhere on a Wintersun road, a bear that should have stayed down got up again.{/n}",
      requires=("soana.trickster.cost.luck_fed",)),
    p("{n}The Commander never threw a loaded die again. The pair sat in Soana's bowl, both twenty up, and nobody who visited "
      "the cave was allowed to touch them.{/n}", requires=("soana.trickster.cost.pair_given",)),
)

SCENES.append(scene("soana.trickster.epilogue.knot", "The second strand", "Epilogue", 5, "", [
    nar("start", '''{n}Soana took her leash back from the Commander's hand the night of the vow and tied it into her knot again, with the Commander's life at the other end. The Commander felt it pull on hungry nights for the rest of the war, in the wrist the knot had marked, and the wrist ached in cold weather ever after. When the war was over she began to plant the dead Wintersun woods, and, slowly, to bind the forest's broken things into the few that lived. She never thanked the Commander for anything, and she never let the knot go slack.{/n}''',
        c(), paragraphs=(
            p("{n}The Commander wore the halves of the clay knot on a strip of gut for the rest of their life. When it chafed, "
              "Soana said that was how you knew it was working.{/n}", requires=(SPENT,)),
            p("{n}The Commander wore her grey cord round the marked wrist for the rest of their life, and every spring she replaited it "
              "from her own braid, complaining the whole time. When it chafed, she said that was how you knew it was working.{/n}",
              forbids=(SPENT,)),
            *EPILOGUE_PARAGRAPHS))],
    requires=(RETURNED, BEARER), forbids=(CLOSED, "sacrifice"), last=99, Relationship="soana", ForbidOverrides=dict(SACRIFICE_BACK)))

SCENES.append(scene("soana.trickster.epilogue.luck", "The die in the bowl", "Epilogue", 5, "", [
    nar("start", '''{n}The die stayed in Soana's bowl after the war, twenty up, and the she-bear who had carried the Commander's luck to the roads grew grey in the muzzle and very fat. The Commander came to Wintersun whenever the world allowed it, and some times when it did not.{/n}
{n}Soana never admitted to missing anyone. She did keep the second blanket on the pallet, and she never once put it back on the shelf.{/n}''',
        c(), paragraphs=EPILOGUE_PARAGRAPHS)],
    requires=(LUCK_KEPT, COMMITTED), forbids=(CLOSED, RETURNED, "soana.late_campaign_kept", "sacrifice", *LOSS), last=99,
    Relationship="soana", ForbidOverrides=dict(SACRIFICE_BACK)))

# Polish (Sol BEL): the late fallback carries the same reckoning as play. Where the accounting was never played it happens
# after the war, and only her own invitation brings the Commander back to her fire.
_RECKON_TAIL = ("The visits after that were spent clearing the stream below the graves and fencing her seed bed while she "
                "watched. She sent the Commander away when the work was done. On the next visit she told them to stay.")
COMMIT_ACCOUNTING = (
    p("{n}" + ("When the Commander came to her cave after the war, she stopped them at the graves and asked why they had given "
      "her to Camellia. They answered for it. She heard them out, then put a bundle of stakes in their hands. " + _RECKON_TAIL) + "{/n}",
      requires=(KILLED,), forbids=(ACC_INVITED,)),
    p("{n}" + ("When the Commander came to her cave after the war, she stopped them at the graves and asked why they had killed "
      "her. They answered for it. She heard them out, then put a bundle of stakes in their hands. " + _RECKON_TAIL) + "{/n}",
      requires=(OWN_KILL,), forbids=(KILLED, ACC_INVITED)),
    p("{n}" + ("When the Commander came to her cave after the war, she stopped them at the graves, and they listened while she "
      "told them what her return had left undone. " + _RECKON_TAIL) + "{/n}",
      forbids=(KILLED, OWN_KILL, ACC_INVITED)),
    p("{n}The Commander had answered her by the graves and worked beside the water. After the war they came back for the "
      "woman who had told them to come for her, and she kept them carrying water through the dry months.{/n}",
      requires=(ACC_INVITED,)),
    p("{n}The year after the war ended she held out a new cord, plaited from her own grey hair. The Commander gave "
      "her the marked wrist. She tied their life to hers and pulled the cord tight.{/n} \"Your end, hunter. You know what "
      "it holds now.\" {n}She kept that wrist in her hand when she led them down into the furs.{/n}"),
)

SCENES.append(scene("soana.trickster.epilogue.commit", "Your end", "Epilogue", 5, "", [
    nar("start", '''{n}Soana took her leash back from the Commander's hand alone, with one strand and her own blood, and it nearly killed her. She buried the dead forest one grave a day, and carried seed from beyond the dead ground to the water below her cave.{/n}''',
        c(), paragraphs=(*COMMIT_ACCOUNTING, *EPILOGUE_PARAGRAPHS))],
    requires=(LATE_COMMITTED, RETURNED), forbids=(COMMITTED, CLOSED, DECLINED, FRIENDS, "sacrifice"), last=99, Relationship="soana",
    ForbidOverrides=dict(SACRIFICE_BACK)))

# b9c: the living, missed-window Soana whose luck was paid but whose bowl was never answered gets her own late page (the
# killed branch's leash and dead forest are not hers).
SCENES.append(scene("soana.trickster.epilogue.luck_late", "The rattle in the bowl", "Epilogue", 5, "", [
    nar("start", '''{n}The war ended before Soana finished thinking. She finished afterwards, on her own terms. The year after the war ended she walked all the way to Drezen with the loaded die in her fist, found the Commander, and put it in their palm.{/n}
"Your luck. It has rattled in my bowl ever since you left it there and I am sick of the noise. Bring it back to Wintersun and keep it where I can hear it, and we will see how much of it is left."''',
        c(), paragraphs=EPILOGUE_PARAGRAPHS)],
    requires=(LATE_COMMITTED, LUCK_KEPT), forbids=(RETURNED, COMMITTED, CLOSED, DECLINED, FRIENDS, "sacrifice", *LOSS), last=99, Relationship="soana",
    ForbidOverrides=dict(SACRIFICE_BACK)))

# Polish (Sol CAN, audit r3): the luck branch's Soana killed later and never returned stays dead; the living pages forbid
# her loss, and this page ends that history (the registered loss pages read the registered chain only).
SCENES.append(scene("soana.trickster.epilogue.luck_lost", "Twenty up, in a cold bowl", "Epilogue", 5, "", [
    nar("start", '''{n}Soana died in her cave at Wintersun, and the forest died with her. When the crusade's people came to see to the body, her bone bowl was still beside the cold hearth with the loaded die in it, twenty up. Nobody had told the spirits the pledge was void.{/n}
{n}The she-bear that had gone out on the Commander's luck came back to the cave mouth once, after the snow, and lay down there, and did not get up again.{/n}''',
        c())],
    requires=("trickster.ever", LUCK_KEPT), forbids=(RETURNED, "soana.late_campaign_kept", "soana.progression_kept", OWN_KILL),
    RequiresAnyGroups=[list(LOSS)], last=99, Relationship="soana"))

UNBOUND = p("{n}She took her leash back from the Commander's hand the day they parted, with a single strand and her own blood. "
             "It held, barely, for as long as she lived. The knot hung in her cave with one strand, and she bound nothing new "
             "into the Wintersun woods again.{/n}", requires=(RETURNED,))

SCENES.append(scene("soana.trickster.epilogue.declined", "One strand", "Epilogue", 5, "", [
    nar("start", '''{n}She never asked again. When travellers asked the old woman in the cave about the Commander, she said that she had once met a hunter who could not make up their mind when it mattered, and that was all she said.{/n}''',
        c(), paragraphs=(UNBOUND,))],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED, FRIENDS, "sacrifice", *LOSS), last=99, Relationship="soana",
    ForbidOverrides={**SACRIFICE_BACK, **{f: RETURNED for f in LOSS}}))

# Polish (Sol BEL, audit r2): a return that never reached her invitation, a friendship, a refusal or a closure is not a late
# romance. The late commit needs her invitation at the accounting (or a failed presence, R2-6); this page covers the rest.
SCENES.append(scene("soana.trickster.epilogue.unfinished", "Left unsaid", "Epilogue", 5, "", [
    nar("start", '''{n}The war ended with Soana's reckoning still unanswered. The following spring she walked to Drezen, took her leash back from the Commander's palm with a single strand and her own blood, and went home the same day.{/n}
{n}She buried the dead forest one grave a day and planted what she could beside the water. When travellers asked about the Commander, she tapped the handle of her spade. "Pulled me back into this," she said. "Still owes me an answer." Then she sent them out of her seed bed.{/n}''',
        c())],
    requires=("trickster.ever", RETURNED),
    forbids=(LATE_COMMITTED, COMMITTED, CLOSED, DECLINED, FRIENDS, BEARER, "sacrifice"), last=99, Relationship="soana",
    ForbidOverrides=dict(SACRIFICE_BACK)))

# Polish r4: the Commander's own kill stands. One closing page for every such history the registered loss pages do not
# already end (they read the registered chain); no trick, no return, no living word from her.
SCENES.append(scene("soana.trickster.epilogue.by_your_hand", "The hunter's kill", "Epilogue", 5, "", [
    nar("start", '''{n}Soana died in her cave at Wintersun by the Commander's own hand, and the forest died with her. Nothing in the trees answered for her afterwards; whatever she had held in her knot went where such things go when the hand on the leash is gone.{/n}
{n}The crusade's report called it a necessary execution. The Sarkorians who passed the dead wood called it the place where the bloody hunter came, and they did not lower their voices when they said it.{/n}''',
        c(), paragraphs=(
            p("{n}Her clay medallion went into the Commander's pack with the rest of the loot, and stayed there.{/n}",
              requires=("soana.medallion_held",)),
            # The two witnesses with a stake (the reactions live here: her relationship is closed by her death).
            p("\"You killed the old woman yourself,\" {n}Camellia said, when the news reached camp, and tilted her head as if "
              "listening for something that had stopped.{/n} \"I asked you so nicely for her, my friend, and you simply took her. "
              "I suppose I ought to admire it. I find I only want to know how it felt.\"",
              forbids=("camellia.dead", "camellia.killed", "camellia.kicked_out")),
            p("{n}Ulbrig looked at the Commander's hands, not their face, when the scouts brought word that the Wintersun wood had "
              "gone grey from the roots up.{/n} \"She bound a demon to a bear and called it keeping, warchief. I'd not have done it "
              "her way. But a forest with nobody left to speak for it is a hungry thing, and it knows whose boots walked out of it.\"",
              requires=("ulbrig.talked",), forbids=("ulbrig.dead", "ulbrig.kicked_out")),
        ))],
    requires=("trickster.ever", OWN_KILL), forbids=(RETURNED, "soana.late_campaign_kept", "soana.progression_kept"),
    RequiresAnyGroups=[list(LOSS)], last=99, Relationship="soana"))

SCENES.append(scene("soana.trickster.epilogue.unbound", "The leash", "Epilogue", 5, "", [
    nar("start", '''{n}The Commander made no further visits to Wintersun. Before the army's last march Soana came to Drezen once, took her leash back from the Commander's palm with a single strand and most of her own blood, and left without a word. It held.{/n}
{n}The Wintersun woods grew quiet again. Travellers who asked the old woman in the cave about the Commander were told about a hunter who had held a dead woman to her own words. She did not say it kindly.{/n}''',
        c(), paragraphs=(
            p("\"Dug my graves with their own hands,\" {n}she would add.{/n} \"Badly. And still walked away.\"", requires=(DUG,)),
            p("\"Paid Drezen to dig my graves,\" {n}she would add.{/n} \"The diggers ate my fish, and the one who paid them walked away all the same.\"",
              requires=(BOUGHT,)),
            p("\"Would not lift a spade for my dead,\" {n}she would add.{/n} \"Turned round at my door and walked away.\"",
              requires=(LEFT,)),
        ))],
    requires=("trickster.ever", RETURNED, CLOSED), forbids=("sacrifice",), last=99, Relationship="soana",
    ForbidOverrides=dict(SACRIFICE_BACK)))

# Q10 r2: a lover from before her death who returned her but never took the knot's second strand.
SCENES.append(scene("soana.trickster.epilogue.unvowed", "One strand, old promises", "Epilogue", 5, "", [
    nar("start", '''{n}Soana held her leash alone, with one strand and her own blood; taking it back nearly killed her. She lived. She buried the dead forest one grave a day and planted what she could beside the water.{/n}''',
        c(), paragraphs=(
            p("{n}The Commander had answered her by the graves and worked where she pointed, and she had called them back "
              "for herself. They still came to her fire when the war allowed. She fed them, scolded them and took them to "
              "bed, and never once let them near the knot.{/n} \"You had your chance at that,\" {n}she said, and that was the end of it.{/n}",
              requires=(ACC_INVITED,)),
            p("{n}Their old promises did not open the cave to them again. When they came after the war she stopped them by "
              "the graves, heard their answer for how she had died, and put the stakes in their hands. They cleared her "
              "stream and fenced her seed bed over the visits that followed. Only when she called them back for herself "
              "did they sit at her fire as her lover again. The knot stayed in her hands.{/n}",
              forbids=(ACC_INVITED,)),
        ))],
    requires=("trickster.ever", RETURNED, COMMITTED), forbids=(BEARER, CLOSED, FRIENDS, "sacrifice"), last=99, Relationship="soana",
    ForbidOverrides=dict(SACRIFICE_BACK)))

# Q10 r4: the Commander answered her Corven disclosure with friendship.
SCENES.append(scene("soana.trickster.epilogue.friends", "A friend at the fire", "Epilogue", 5, "", [
    nar("start", '''{n}Soana kept a second cup by the fire for the Commander. She called them her friend, usually just before asking them to carry something heavy, and when anyone asked whether she liked their visits, she said the water pot did.{/n}''',
        c(), paragraphs=(
            p("{n}She held her leash alone, with one strand and her own blood; taking it back had nearly killed her. "
              "She buried the dead forest one grave a day, and made the Commander dig every third one when they visited.{/n}",
              requires=(RETURNED,)),
            p("{n}The loaded die stayed in her bowl, twenty up, and the she-bear who had carried it to the roads grew fat and grey.{/n}",
              requires=(LUCK_KEPT,), forbids=(RETURNED,)),
        ))],
    requires=("trickster.ever", FRIENDS), forbids=(CLOSED, BEARER, "sacrifice", *LOSS), last=99, Relationship="soana",
    ForbidOverrides={**SACRIFICE_BACK, **{f: RETURNED for f in LOSS}}))

# Q10: the Commander gave their life at the Threshold and stayed dead. Every Trickster page above describes a living
# Commander, so this one page carries the knot, the leash and the die for that world.
SCENES.append(scene("soana.trickster.epilogue.slack", "The slack strand", "Epilogue", 5, "", [
    nar("start", '''{n}The Commander did not come back from the Threshold. The riders brought the word to Wintersun a fortnight later, and Soana made the messenger tell it twice, the second time slower. Then she sent him back down the path and sat by the cold fire.{/n}''',
        c(), paragraphs=(
            p("{n}She had known before the riders came. The knot on her wrist went slack the night it happened, the way a line "
              "goes slack when the fish is gone. Her end had been "
              "tied to the Commander's life, and that life had gone first, as she had told them it would. She cut the dead strand "
              "off with her knife, tied it round her own throat, and went on binding the Wintersun woods "
              "for twenty years more out of spite. She never said the Commander's name to anyone. She said{/n} \"the hunter\"{n}, and "
              "everyone knew.{/n}", requires=(RETURNED, BEARER)),
            p("{n}She had known before the riders came. The leash struck her the night the Commander's hand stopped holding it, "
              "all of its weight at once and nothing at the other end. She went down on her knees, caught it and held. It "
              "nearly killed her. It did not.{/n}",
              requires=(RETURNED,), forbids=(BEARER, RECLAIMED_BEFORE, CLOSED, POSTPONED)),
            p("{n}Out on the Wintersun road, the she-bear that had stood up on the Commander's luck lay down in the "
              "ferns that night and did not get up. Soana took the die out of the bowl and buried it with her, twenty up.{/n}",
              requires=(LUCK_KEPT,), forbids=(RETURNED,)),
            p("{n}She had taken the leash back while the Commander still lived, and no strand of it ran to the Threshold. Nothing "
              "pulled when they died. She sat until the messenger was out of sight, then went out to her graves.{/n}",
              requires=(RETURNED, RECLAIMED_BEFORE), forbids=(BEARER,)),
            p("{n}She had gone to Drezen before the last march and taken the leash back from the Commander's palm herself, with "
              "a single strand and most of her own blood. Nothing pulled when they died. When the messenger asked whether the "
              "Commander had been her friend, she said,{/n} \"The dead do not need you improving them.\"",
              requires=(RETURNED, CLOSED), forbids=(BEARER, RECLAIMED_BEFORE)),
            p("{n}She had tired of waiting for the Commander's answer before the army marched. She went to Drezen, took the "
              "leash back from their palm with her own blood, and walked home. Their death gave her nothing back a second "
              "time. The knot hung in her cave with one strand, and she did not ask again.{/n}",
              requires=(RETURNED, POSTPONED), forbids=(BEARER, CLOSED, FRIENDS, RECLAIMED_BEFORE)),
        ))],
    requires=("trickster.ever", "sacrifice"), forbids=("trickster.commander_back", "soana.late_campaign_kept", *LOSS),
    ForbidOverrides={f: RETURNED for f in LOSS},
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
             answer_list=ULBRIG_HUB, forbids=(*ULBRIG_GONE, RECLAIMED_BEFORE), chapter=3, last=5, delay=24, entry='"About Soana..."'),
    reaction("Ulbrig", "soana.trickster.react.ulbrig_luck", (CATCHUP, "ulbrig.talked"),
             '''"The Wintersun crone's beasts are fighting demons on the road again, warchief. A she-bear with her guts hanging out stood up three times, the scouts say. Spirits don't do that for free. What did you give them? And what will they want next?"''',
             answer_list=ULBRIG_HUB, forbids=ULBRIG_GONE, chapter=5, last=5, delay=24, entry='"About the Wintersun beasts..."'),
]
SCENES.extend(REACTIONS)


# --- The registered route -----------------------------------------------------------------------------------------------

# The alive branches end on the registered pages; the portion and the die leave a mark there.
ALIVE_PARAGRAPHS = (
    p("{n}Every winter the spirits came to the cave mouth for their portion, and every winter she cut her palm for them and "
      "cursed the Commander's name while she did it. She never missed a winter.{/n}", requires=(BLOOD,)),
    p("{n}Some winters the spirits came to the Commander's door instead, wherever it was, and stood in the frost till dawn. The "
      "Commander learned to keep a knife by the threshold, and a rag, and to expect a letter from Wintersun a week later "
      "calling them stupid.{/n}", requires=("soana.trickster.cost.portion_shared",), forbids=("sacrifice",)),
    p("{n}She kept a loaded die in her offering bowl until she died, twenty up. Nobody who visited the cave was allowed to touch it.{/n}",
      requires=(DICE,), forbids=(LUCK_REFUSED,)),
)
ALIVE_ENDINGS = ("kept_life", "chosen_visits", "familiar_company", "sacrifice", "beyond_the_forest")
# Q10 r2: the shared portion outlives a Commander who stayed dead; Soana pays both halves. (The living paragraph above
# forbids sacrifice, and the living endings that a returned Commander reaches carry it again with the override below.)
PORTION_ALIVE = ALIVE_PARAGRAPHS[1]
PORTION_DEAD = p("{n}The winter after the Threshold the spirits came to Wintersun twice: once for her portion, and once for the "
                 "Commander's, which nobody alive was left to pay. Soana cut both palms and paid them both, every winter after, "
                 "and cursed the dead for leaving her the bill.{/n}", requires=("soana.trickster.cost.portion_shared",))


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
    # Polish (Sol BEL, audit r2): the fallback continues a courtship the player chose: her invitation at the accounting, or
    # the luck branch's answered test. A failed presence alone is not courtship (audit r3): the return then ends unfinished.
    payload.setdefault("Derived", {})[LATE_COMMITTED] = [["trickster.ever", RETURNED, ACC_INVITED],
                                                         ["trickster.ever", LUCK_KEPT, TESTED]]
    # Polish (Sol INT): who held the leash when the Commander died. A save that completed the friendship or the refused
    # rebinding before the latch existed counts by those scenes' completion with their outcome flags.
    payload["Derived"][RECLAIMED_BEFORE] = [[RECLAIMED], [RETURNED, FRIENDS, "soana.trickster.returned.terms"],
                                            [RETURNED, REBIND_DECLINED, "soana.trickster.returned.rebind"]]
    payload["Derived"][POSTPONED] = [[RETURNED, DECLINED, "soana.trickster.returned.terms"]]
    # Polish (Sol INT): the Commander's own kill, read from the native attack answers (SelectedAnswers), never inferred.
    answers = payload.setdefault("SelectedAnswers", {})
    for key, guid in OWN_KILL_ANSWERS.items():
        if answers.get(key, guid) != guid:
            raise ValueError("Conflicting binding: " + key)
        answers[key] = guid
    payload["Derived"][OWN_KILL] = [[key] for key in OWN_KILL_ANSWERS]
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

    soana_partner.finish_normal_endings(payload["Scenes"])
    from storylines import soana_round2
    soana_round2.integrate(payload)


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'soana.trickster.missed.crooked_luck',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]

# Round 2a: route-local Corven thread, stance and partner continuity.
from storylines import soana_partner
soana_partner.commitments(SCENES)
soana_partner.endings(SCENES)
SCENES.extend(soana_partner.SCENES)
soana_partner.lastcall()

from storylines import soana_round2
soana_round2.prepare(SCENES)

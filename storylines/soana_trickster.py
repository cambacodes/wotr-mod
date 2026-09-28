"""Soana on the Trickster path (Writer/handoffs/trickster/soana.md; F17 take them at their word, F13 loaded dice).

Canon: Camellia asks at camp to "turn her blood to a good cause" (Camelia/Cue_0136 f505392f) and, in the bear dialog, to
"let her blood serve the spirits of this land one last time" (SoanaAfterBear/Cue_0065 b2e41844, its twin Cue_0069).
Soana made Orso: "I forced the spirit to serve good by linking our lives together" (SoanaAfterBear/Cue_0015 396b1d46);
the brand and the clay knot are one binding (SoanaBear/Cue_0016, Cue_0023). Her creed: "a true protector is the one who
sacrifices themselves" (SoanaAfterBear/Cue_0012 353da9f2); "I serve the forest spirits. I don't serve you." (Cue_0029).
In Chapter 5 the Wintersun beasts fight demons on the roads (KTC_WintersunHelp/Cue_0048 3c616e0b). The Trickster's dice
turn a one into a twenty (TricksterKnowledgeWorldTier2Feature 8b6fe337). She is an old dwarf woman who looks carved from
driftwood (SoanaBeforeBear/Cue_0001): proud, bitter, blunt, never grateful, and she names her own price.

Three states: the handover (Camellia is taken at her word before the kill), killed (the knot read in the other
direction, a guardian's life for hers; the return is tested at her grave and committed on her terms), and the missed
Chapter 3 window (a die planted in her bowl, paid for in Chapter 5, and a short courtship of its own).
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
DUG = "soana.trickster.cost.grave_dug"
BOUGHT = "soana.trickster.cost.grave_bought"
LEFT = "soana.trickster.cost.left_the_grave"
BEARER = "soana.trickster.cost.knot_bearer"
SECOND = "soana.trickster.cost.second_ask"
CATCHUP = "soana.trickster.cost.catchup"
LATE = "soana.trickster.cost.late"
DIE_KEPT = "soana.trickster.cost.die_in_her_bowl"
SEALED = "soana.trickster.cost.woods_sealed"
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
                                    "her nails. She does not look up.{/n} \"Well? Say what you came to say, hunter. "
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
    '"My friend wants your blood turned to a good cause. Your forest is a good cause. Bleed for it first, and she can have what\'s left."',
    ("trickster", "camellia.asked_for_soana"), None, [
    n("start", "Soana", '''{n}The old woman looks at you for a long moment. Then she laughs, the cracked laugh from your first meeting, and draws her knife across her own palm. Blood runs off her knuckles into the moss. Somewhere in the trees, something answers: not a bird, not a wolf.{/n}
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
"How very generous of her. And of you, my friend. You have cheated me out of a perfectly good death in front of the one audience I cared about." {n}She wets her lips.{/n} "I shall have to think of a way to thank you. I think about such things a great deal."''',
            c('[Leave before either of them decides otherwise]', native_next=nxt, flags=(PRIMED, BLOOD)),
            speaker_unit=CAMELLIA)])


# --- State 2, killed: the knot never checked (F17, her own words read in the other direction) --------------------------

SCENES.append(scene("soana.trickster.killed.knot", "The knot never checked", "Soana", 3, "", [
    nar("start", '''{n}You go back to Wintersun alone, on a grey morning, with the crusade's business waiting behind you. Soana's cave smells of cold ash and something sweeter under it. Nobody has taken her bones to the ground; the forest does not have anyone left who would.{/n}
{n}Something out in the trees stops moving when you step inside.{/n}''',
        c("Continue", "orso", forbids=(BEAR_DEAD,)), c("Continue", "spirit", requires=(BEAR_DEAD,))),
    nar("orso", '''{n}Orso comes to the cave mouth and will not come further. He has been circling it for days; the moss is worn down to stone in a ring. The brand on his shoulder is a knot, the same knot she wore in clay at her throat, and it has not faded.{/n}''',
        c("Continue", "read")),
    nar("spirit", '''{n}Orso lies where he fell: a grey pelt stretched over bones. The brand is still on the pelt, darker than a dead thing's brand has any right to be, and the grass around the carcass has gone black in the shape of a knot. Something still lies in those bones: the spirit she bound, with nowhere left to go and nobody left to hold its leash.{/n}''',
        c("Continue", "read")),
    nar("read", '''{n}You remember what she told you, with her arms folded over her chest: she forced the spirit to serve good by linking their lives together.{/n}
{n}She never said whose life went first.{/n}''',
        c('[Hold her clay medallion to the guardian\'s brand] "You linked your lives together. You never said whose goes first. Pay her debt."',
          "wake_clay", mythic="Trickster", alignment=("Chaotic", 1), requires=("soana.medallion_held",), remove_item=MEDALLION,
          flags=(RETURNED, STARTED, GUARDIAN, SPENT)),
        c('[Lay your hand on the brand and read it her own words] "You linked your lives together. You never said whose goes first. Pay her debt."',
          "wake_brand", mythic="Trickster", alignment=("Chaotic", 1), forbids=("soana.medallion_held",),
          flags=(RETURNED, STARTED, GUARDIAN)),
        c('[Leave the knot tied] "No. She said she was finished. Let her be finished."', flags=(CLOSED,))),
    nar("wake_clay", '''{n}The brand darkens, as a rope darkens when it is pulled wet. The clay knot in your hand draws tight, tighter than clay can bear, and cracks down the middle with a sound like a knuckle.{/n}''',
        c("Continue", "wake_orso", forbids=(BEAR_DEAD,)), c("Continue", "wake_spirit", requires=(BEAR_DEAD,))),
    nar("wake_brand", '''{n}The brand darkens under your palm, as a rope darkens when it is pulled wet, and draws tight until the skin of your hand burns with cold. When you take the hand away, the shape of the knot is printed on it in white.{/n}''',
        c("Continue", "wake_orso", forbids=(BEAR_DEAD,)), c("Continue", "wake_spirit", requires=(BEAR_DEAD,))),
    nar("wake_orso", '''{n}The knot does not take a life. It takes the leash. Out in the ferns Orso rears up, and something tears loose from him: a shadow the size of a man, black as burnt grass, that goes into the trees faster than anything that size should move.{/n}
{n}Orso comes down on all fours and shakes himself like a dog out of a river. The brand on his shoulder is grey and cold. He looks at you with a bear's eyes, only a bear's, and does not know you, or the cave, or his own name.{/n}''',
        c("Continue", "soana")),
    nar("wake_spirit", '''{n}The knot does not take a life. It takes the leash. The black grass around the bones turns to plain dead grass, and something leaves the carcass in a rush, low to the ground, like smoke looking for a door. It goes into the trees. Behind it, the bones are only bones.{/n}''',
        c("Continue", "soana")),
    s("soana", '''{n}Behind you, someone coughs up forest loam.{/n}
"...Bloody hunter. Of course. Who else would hold a dead woman to her own words?"
{n}She sits up on the cold floor of her cave, an old dwarf woman in rags, and looks at her hands as if somebody had returned them to her with the fingers in the wrong order.{/n}
"I was finished. I had earned it. And you paid for me with my knot. The thing I bound is loose in my forest, looking for a skin to wear, and there is nobody left to hold its leash but me."''',
        c('"You can hate me standing up."')),
    ], requires=("trickster", "trickster.ever"), forbids=(RETURNED, CLOSED), delay=0, last=5, Relationship="soana",
    Chapters=[3, 5], Remote=True, TricksterDevice=True, TricksterState="killed",
    RequiresAnyGroups=[[DEAD, KILLED]]))

at_cave("soana.trickster.returned.graveyard", "What the knot cost", '"Soana."', [
    s("start", '''{n}Soana has a spade in one hand. Around the cave mouth are new mounds, a row of them, small and large: a fox, two wolves, a hind with her calf. Beside the last is a hole she has not finished.{/n}
"Two days I have been walking this forest behind the thing you let off its leash. It rides whatever it can catch, runs it until its heart bursts, and gets off. I bury what it leaves. The demons on your road would pay well for a rider like that."''',
        c("Continue", "orso", forbids=(BEAR_DEAD,)), c("Continue", "spirit", requires=(BEAR_DEAD,))),
    s("orso", '''"Orso is in the ravine. He will not come when I call. He is only a bear now, and an old one, and the thing that wore him for so long remembers where he sleeps. You used him to pay a debt that was not his, hunter. He was a demon's cage, and he was mine."''',
        c("Continue", "dig")),
    s("spirit", '''"Orso's bones are in the ground; I put them there myself, the first night, with my hands. What was in them is not. It remembers who let it out. It will come looking for you before long, and it will come through my forest to do it."''',
        c("Continue", "dig")),
    s("dig", '''{n}She holds out the spade, handle first.{/n}
"You were very quick with my knot, bloody hunter. Let us see how quick you are with a grave. Then we will talk about catching it."''',
        c('[Take the spade]', "dug", flags=(GRAVE_KEPT, DUG)),
        c('"I\'ll send to Drezen for diggers."', "bought", crusade=("Finances", -100), flags=(GRAVE_KEPT, BOUGHT)),
        c('[Leave her with her graves]', flags=(CLOSED, LEFT))),
    nar("dug", '''{n}The ground is frozen for the first hand's depth and roots all the way down after that. You dig until the light goes. Soana does not help. She sits on a stone and tells you when you are doing it wrong, which is often, and when the hind and her calf finally go in she says something over them in a language that sounds like branches knocking.{/n}''',
        c('[Wipe your hands]', "decide")),
    nar("bought", '''{n}The diggers come from Drezen three days later, crusaders with good boots and bad manners. They dig fast and deep and argue about who has to carry the calf. Soana watches them from the cave mouth the whole time with an expression you would not wish on an enemy.{/n}''',
        c('[Pay them off]', "decide")),
    s("decide", '''{n}She leans on the spade and looks at you the way she looks at weather.{/n}
"Hear me, hunter, because I will say it once. The thing in my woods I will catch with you or without you. That is the forest's business, and it does not buy you anything from me. What you want from me is another matter, and I have not decided what I think of it."
"Come back in three days. By then I will know my own mind. I always do, in the end."''',
        c('"Three days, then."'),
        c('"I dug your graves. That\'s all I came for."', flags=(CLOSED,))),
    ], requires=("trickster.ever", RETURNED), forbids=(CLOSED, GRAVE_KEPT), delay=48)

TERMS_NIGHT = '''{n}She presses the shards into your palm and ties them there with a strip of gut, round your wrist and then round her own, tight enough to hurt. The fire is low. She does not let go of the strip.{/n}
"Knots listen." {n}Her eyes do not leave yours.{/n} "So do I. So listen."
{n}She pulls. You come. Her hands are as hard as roots and warmer than anything in this forest has a right to be; she finds the buckle at your collar without looking, the way she finds the knife at her belt. Her mouth tastes of smoke and of the bitter bark she chews against the cold, and she bites your lower lip where the knot drew blood, not gently, to see what you will do about it.{/n}
"All those winters I slept with a demon at the door. I am done sleeping."
{n}She draws the gut strip taut between your wrists and hers and leans back into the old furs, and you go down with her, because you are tied to her and because you want to.{/n}'''
TERMS_MORNING = '''{n}Morning. Frost on the cave mouth. The strip is gone from her wrist; it is still round yours, and underneath it the skin is raised in a red weal the shape of a knot.{/n}
{n}Soana is outside already, feeding the spirits from a bowl. She does not turn around.{/n}
"Your end is sore. Good. It is supposed to be. Now go and fight your war, hunter, and do not die before I do. It would be very inconvenient."'''

at_cave("soana.trickster.returned.terms", "The second strand", '"You said you had terms."', [
    s("start", '''{n}The grave is a low mound under the ferns. She has laid stones on it in a pattern you almost recognize.{/n}''',
        c("Continue", "dug", requires=(DUG,)), c("Continue", "bought", requires=(BOUGHT,)),
        c("Continue", "price", forbids=(DUG, BOUGHT))),
    s("dug", '''"You dug. Badly, and too shallow at the head end, but you dug, with your own hands, in the cold. That is more than your friends in Drezen would have done. I have been thinking about what it means. I do not like the answer."''',
        c("Continue", "price")),
    s("bought", '''"Your diggers came, dug, ate my last smoked fish and left. Paying is easy for you people. It is the one thing you are good at. Remember that I noticed."''',
        c("Continue", "price")),
    s("price", '''{n}She opens her hand. The two halves of the clay knot lie in it.{/n}
"I have decided. I want you, hunter, which is a great nuisance. So you will have my terms, and you will take them as they are or not at all."
"A knot with one strand is not a knot. It is a piece of string. If I am to catch that thing and bind it again, the knot needs a second life at the other end. Orso's has gone out of it; you saw to that. So: yours. Carry the pieces. When I die again, and I will, it is your life the knot comes looking for first."
"Those are my terms. I will not say them twice, and I will not make them sweeter."''',
        c('[Hold out your hand for the pieces]', "bind"),
        c('"Ask me again when the ground thaws."', "no"),
        c('"Find another fool."', "fool")),
    s("bind", '''{n}She does not take your hand yet. She looks at it: the calluses, the scars, the crusade's grime.{/n}
"Say it, then. 'Mine first.' Knots listen."''',
        c('"Mine first."', "night", flags=(COMMITTED, BEARER)),
        c('[Laugh]', "no")),
    s("no", '''{n}She closes her fist over the shards and turns away.{/n}
"No. You laughed at my knot once already, and it cost me my guardian. Come back when you can hold still for a thing that matters."''',
        c('[Go]', flags=(DECLINED,))),
    s("fool", '''"I already found one. He is in the ravine, and he does not know his own name."
{n}She does not look at you again.{/n}''',
        c('[Go]', flags=(CLOSED,))),
    s("night", TERMS_NIGHT, c("Continue", "morning")),
    s("morning", TERMS_MORNING, c('[Go]')),
    ], requires=("trickster.ever", RETURNED, GRAVE_KEPT), forbids=(CLOSED, COMMITTED, DECLINED), delay=72)

at_cave("soana.trickster.returned.second_ask", "The price goes up", '"About your terms."', [
    s("start", '''"Back. Good. The price has gone up while you were away, hunter."
{n}She points with her chin at the trees behind her. Half of them are grey to the heartwood.{/n}
"The forest needs burying, all of it, and I cannot do it with one spade. Lye, timber, carts. From your stores, not your purse, so that somebody in Drezen goes without. Then the pieces, and the words."''',
        c("Continue", "price")),
    s("price", '''"Well? I will not wait for the ground to thaw twice."''',
        c('[Pay for the lye and the timber] "Mine first."', "night", crusade=("Materials", -150),
          flags=(COMMITTED, BEARER, SECOND)),
        c('"No. Not at that price."', flags=(CLOSED,))),
    s("night", TERMS_NIGHT, c("Continue", "morning")),
    s("morning", TERMS_MORNING, c('[Go]')),
    ], requires=("trickster.ever", RETURNED, DECLINED), forbids=(CLOSED, COMMITTED), delay=96)


# --- State 3, the missed window: crooked luck (F13) ---------------------------------------------------------------------

inline("soana.trickster.missed.dice_bowl", "An offering", 3,
    '[Drop a die into her offering bowl] "For your spirits. They look like they could use the luck."', [
    n("start", "Soana", '''{n}The die rattles in the bone bowl and stops on a one. She looks at it, then at you. When she looks back, it shows a twenty.{/n}
"Spirits take what is offered. They do not say thank you, and neither do I."
{n}She does not take it out of the bowl. She does not touch it at all.{/n}''',
        c('[Leave it where it landed]', flags=(DICE,)))],
    requires=("trickster", "soana.after_quest"), forbids=(*LOSS, CLOSED, DICE), RequiresAny=DEFENDER,
    EntryMythic="PlayerIsTrickster")

inline("soana.trickster.missed.crooked_luck", "Crooked luck", 5,
    '[Look at the die in her bowl] "Still twenty up, shaman? I hear your beasts don\'t stay down."', [
    n("start", "Soana", '''{n}A she-bear lies across the cave mouth with her belly opened by a demon's claws. As you come near she gets up, shakes herself and pads into the trees toward the road, bleeding as she goes.{/n}
"That is the third time she has done that. Your die has been in my bowl since the snow. My beasts go out against the demons on the road and they do not stay down. I did not ask for that, bloody hunter."''',
        c("Continue", "price")),
    n("price", "Soana", '''"The spirits have been feeding my beasts on your luck, and luck is thin fare. If they are to keep standing up, they eat. Salt and meat, a cart of each, every month until this war is done. That is my price for your joke. I will not haggle."''',
        c('[Send the salt and the meat] "Done. That\'s your price."', crusade=("Materials", -100),
          flags=(LUCK_KEPT, CATCHUP, STARTED)),
        c('[Take your die back and go]', flags=(LUCK_REFUSED,)))],
    requires=("trickster.ever", "soana.after_quest", DICE),
    forbids=("soana.progression_kept", *LOSS, CLOSED, "inhuman", LUCK_REFUSED, LUCK_KEPT), RequiresAny=DEFENDER,
    TricksterDevice=True, TricksterState="missed")

inline("soana.trickster.missed.late_luck", "Crooked luck, thrown late", 5,
    '[Throw your special die at her feet] "Rolled a one. Watch it turn into a twenty."', [
    n("start", "Soana", '''{n}The die stops on a one, then shows a twenty. Outside, a she-bear that has been dying across the cave mouth all morning gets up on three legs and limps toward the road.{/n}
"You do not put a thing like that in front of my beasts without paying for it, hunter. They will go out on your luck now whether I send them or not, and they will come back hungry."''',
        c("Continue", "price")),
    n("price", "Soana", '''"Salt and meat, two carts a month, and the die stays with me. You threw it; you do not get it back."''',
        c('[Pay what she asks] "Salt, meat, and the die. Done."', crusade=("Materials", -200),
          flags=(DICE, LATE, LUCK_KEPT, CATCHUP, STARTED)),
        c('[Pick up your die and go]', flags=(LUCK_REFUSED, LATE)))],
    requires=("trickster", "soana.after_quest"),
    forbids=("soana.progression_kept", *LOSS, CLOSED, "inhuman", LUCK_REFUSED, DICE, LUCK_KEPT), RequiresAny=DEFENDER,
    TricksterDevice=True, TricksterState="missed", EntryMythic="PlayerIsTrickster")

inline("soana.trickster.missed.she_bear", "The she-bear", 5, '"How is your she-bear?"', [
    n("start", "Soana", '''{n}Soana is sitting on a stump outside the cave with the she-bear's great head in her lap. Someone has sewn the bear's belly shut with sinew, badly; judging by the old woman's fingers, it was the old woman.{/n}
"She went out again last night. She came back with a demon's hand in her mouth. The hand was still trying to get away."
{n}She scratches the bear behind one ear. The bear sighs like a bellows.{/n}''', c("Continue", "question")),
    n("question", "Soana", '''"Your luck keeps her standing. My spirits keep her walking. Neither of us asked her. So I will ask you instead, since you are the one with the dice."
"When this war is done and the luck runs thin, and she lies down, will you let her stay down? Or will you roll again?"''',
        c('"I\'ll let her rest. She\'s earned it."', "rest", flags=(TESTED, REST)),
        c('"I\'ll roll again. As long as it takes."', "roll", flags=(TESTED, ROLL)),
        c('[Grin] "I\'ll roll for her. And if it comes up one, I\'ll call it twenty."', "cheat", flags=(TESTED, CHEAT)),
        c('"Why does it matter what I\'d do?"', "why")),
    n("why", "Soana", '''{n}She looks at you with those small black eyes, sunk deep in the driftwood.{/n}
"Because I am older than she is, hunter. Answer the question."''',
        c('"I\'ll let her rest. She\'s earned it."', "rest", flags=(TESTED, REST)),
        c('"I\'ll roll again. As long as it takes."', "roll", flags=(TESTED, ROLL)),
        c('[Grin] "I\'ll roll for her. And if it comes up one, I\'ll call it twenty."', "cheat", flags=(TESTED, CHEAT))),
    n("rest", "Soana", '''"A true protector is the one who sacrifices themselves. You heard me say it once, and you were listening. Hm."
{n}She goes back to scratching the bear's ear, and for a while she says nothing at all, which from her is a speech.{/n}''',
        c('[Leave them in the sun]')),
    n("roll", "Soana", '''"That is what a child says. A child with a toy it does not want to put away."
{n}She pulls a burr out of the bear's fur and flicks it at your boots.{/n}
"But it is honest. The last one who lied to me in this cave was your friend with the knife. Go away. I am thinking."''',
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
{n}When she kisses you it is with her whole small, heavy body, the way she does everything, as if the world were a thing to be carried and she had decided to carry you for a while. She bites. She laughs when you gasp, low in her chest, and bites again.{/n}
{n}Outside, the she-bear lies down across the cave mouth to keep the night off. Soana pushes you back into the furs, climbs over you with her knees sunk in the pelts on either side, and her hand closes on your hip like a root closing on a stone.{/n}'''
BOWL_MORNING = '''{n}Morning. She is sitting up in the furs with her knees drawn up, rolling your die between her fingers. It keeps coming up twenty. She keeps frowning at it.{/n}
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
    n("terms", "Soana", '''"Here are my terms, hunter. A thing that sits in my bowl is mine. I do not keep things I have not touched. Take your die out now, and everything it has done comes undone with it: the she-bear lies down at the cave mouth and stays there. Or leave it, and it is mine, and you with it, for as long as the luck holds."
"Which is to say, until I decide it does not."''',
        c('[Leave the die in the bowl] "Keep it. And me."', "night", flags=(COMMITTED, DIE_KEPT)),
        c('"Let me think about it."', "no"),
        c('[Take your die out of the bowl]', "taken")),
    n("no", "Soana", '''{n}She shrugs, and puts the second blanket back on the shelf.{/n}
"Think, then. The bowl is patient. I am not. Do not make me ask the question twice; if I have to, it will cost you."''',
        c('[Go]', flags=(DECLINED,))),
    n("taken", "Soana", '''{n}You reach into the bowl. The die is warm. Outside, something large lies down across the cave mouth with a long sigh, and does not get up.{/n}
{n}Soana does not look at the door. She looks at you.{/n}
"There. Now you know what you are. Go."''',
        c('[Go]', flags=(CLOSED,))),
    n("night", "Soana", BOWL_NIGHT, c("Continue", "threshold")),
    n("threshold", "Soana", BOWL_THRESHOLD, c("Continue", "morning")),
    n("morning", "Soana", BOWL_MORNING, c('[Go]'))],
    requires=("trickster.ever", LUCK_KEPT, TESTED), forbids=(*LOSS, CLOSED, COMMITTED, DECLINED), delay=72, optional=True)

inline("soana.trickster.missed.second_ask", "The bowl's price", 5, '"About your bowl."', [
    n("start", "Soana", '''"I said it would cost you. It does."
{n}She sets the bowl on the stone between you.{/n}
"Your scouts watch my beasts fight on the road, and they report it. Soon your foragers will read the reports too, and come for the meat. Seal an order: no crusader hunts in the Wintersun woods, for any pot, for as long as the war lasts, and whoever does answers to the Commander. Your officers will hate you for it. Then ask me again."''',
        c('[Seal the letter] "Done. Keep the die. And me."', "night", crusade=("Favors", -150),
          flags=(COMMITTED, DIE_KEPT, SEALED)),
        c('"No. Not at that price."', flags=(CLOSED,))),
    n("night", "Soana", BOWL_NIGHT, c("Continue", "threshold")),
    n("threshold", "Soana", BOWL_THRESHOLD, c("Continue", "morning")),
    n("morning", "Soana", BOWL_MORNING, c('[Go]'))],
    requires=("trickster.ever", LUCK_KEPT, DECLINED), forbids=(*LOSS, CLOSED, COMMITTED), delay=96, optional=True)


# --- Epilogue pages (no mythic, alignment or crusade effects) ---------------------------------------------------------

EPILOGUE_PARAGRAPHS = (
    p("She took the Commander's half of the knot back only once, to retie it, and she pulled it tighter.", requires=(SECOND,)),
    p("The Wintersun beasts kept going out against the demons on the roads until the last of them was gone, and they kept "
      "getting up. The scouts stopped reporting it. It had become ordinary.", requires=(CATCHUP,)),
    p("The crusade's quartermasters never forgave the Commander for the Wintersun woods, and not one crusader ever took a hide from them.",
      requires=(SEALED,)),
)

SCENES.append(scene("soana.trickster.epilogue.knot", "The second strand", "Epilogue", 5, "", [
    nar("start", '''{n}Soana caught the thing her knot had let loose in the first thaw after the war, in a gully full of dead deer, and bound it again with the Commander's life at the other end of the clay. Then she began, slowly, to bind the forest's broken things into the few that lived. She never thanked the Commander for anything, and she never let the knot go slack.{/n}
{n}The Commander wore the halves of the clay knot on a strip of gut for the rest of their life. When it chafed, Soana said that was how you knew it was working.{/n}''',
        c(), paragraphs=EPILOGUE_PARAGRAPHS)],
    requires=(RETURNED, COMMITTED), forbids=(CLOSED,), last=99, Relationship="soana"))

SCENES.append(scene("soana.trickster.epilogue.luck", "The die in the bowl", "Epilogue", 5, "", [
    nar("start", '''{n}The die stayed in Soana's bowl after the war, twenty up, and the she-bear who had carried the Commander's luck to the roads grew grey in the muzzle and very fat. The Commander came to Wintersun whenever the world allowed it, and some times when it did not.{/n}
{n}Soana never admitted to missing anyone. She did keep the second blanket on the pallet, and she never once put it back on the shelf.{/n}''',
        c(), paragraphs=EPILOGUE_PARAGRAPHS)],
    requires=(LUCK_KEPT, COMMITTED), forbids=(CLOSED, RETURNED, "soana.late_campaign_kept"), last=99,
    Relationship="soana"))

SCENES.append(scene("soana.trickster.epilogue.commit", "Your end", "Epilogue", 5, "", [
    nar("start", '''{n}Soana buried the Wintersun woods alone, one grave a day, and bound what she could into what was left. The year after the Worldwound closed she walked all the way to Drezen with a broken clay knot in her fist, found the Commander, and tied it to their wrist without asking.{/n}
"Your end. Don't lose it."''',
        c(), paragraphs=EPILOGUE_PARAGRAPHS)],
    requires=(LATE_COMMITTED,), forbids=(COMMITTED, CLOSED, DECLINED), last=99, Relationship="soana"))

SCENES.append(scene("soana.trickster.epilogue.declined", "One strand", "Epilogue", 5, "", [
    nar("start", '''{n}She never asked again. The knot hung in her cave with one strand, and she bound nothing new into the Wintersun woods for as long as she lived. When travellers asked the old woman in the cave about the Commander, she said that she had met a hunter once who could not hold still for a thing that mattered, and that was all she said.{/n}''',
        c())],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED), last=99, Relationship="soana"))


# --- Reactions (exactly Camellia, Ember and Ulbrig) ---------------------------------------------------------------------

CAMELLIA_GONE = ("camellia.dead", "camellia.killed", "camellia.kicked_out")
EMBER_GONE = ("ember_dead", "ember_gone")
ULBRIG_GONE = ("ulbrig.dead", "ulbrig.kicked_out")

REACTIONS = [
    reaction("Camellia", "soana.trickster.react.camellia_portion", (BLOOD,),
             '''"You cheated me out of a perfectly good death, my friend. The old woman fed her trees and left me the smell of it." {n}Camellia smooths her skirt with both hands, very slowly.{/n} "I shall have to think of a way to thank you. I have already thought of several."''',
             answer_list=CAMELLIA_HUB, forbids=CAMELLIA_GONE, chapter=3, last=5, delay=24, entry='"About Soana..."'),
    reaction("Camellia", "soana.trickster.react.camellia_knot", (RETURNED, KILLED),
             '''"The old woman is walking again? I bled her myself. I felt her stop." {n}Camellia smiles, slowly, and does not blink.{/n} "How very interesting you make things. I wonder what else of mine you would take back, if I let you."''',
             answer_list=CAMELLIA_HUB, forbids=CAMELLIA_GONE, chapter=3, last=5, delay=24, entry='"About Soana..."'),
    reaction("Ember", "soana.trickster.react.ember_portion", (BLOOD,),
             '''"The old lady cut her own hand so nobody would cut her throat. That's the saddest clever thing I ever saw. You made her do it with a joke. I think she knew it was a joke. I think that's why she did it."''',
             answer_list=EMBER_HUB, forbids=EMBER_GONE, chapter=3, last=5, delay=24, entry='"About the old woman in the woods..."'),
    reaction("Ember", "soana.trickster.react.ember_luck", (CATCHUP,),
             '''"The scouts say the Wintersun bears keep getting up after the demons knock them down. That's your dice, isn't it? I hope somebody asked the bears first. Somebody should always ask the bears."''',
             answer_list=EMBER_HUB, forbids=EMBER_GONE, chapter=5, last=5, delay=24, entry='"About the Wintersun bears..."'),
    reaction("Ulbrig", "soana.trickster.react.ulbrig_knot", (GUARDIAN, "ulbrig.talked"),
             '''"I asked you once what these new powers want in return, warchief. Now we know. That one wanted the crone's leash: there's a demon loose in the Wintersun woods, riding deer until their hearts burst. Every power must have a name, and a price that's fair. I'd not call that fair. Nor would the crone, I'd wager."''',
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
    p("She kept a die in her offering bowl until she died, twenty up. Nobody who visited the cave was allowed to touch it.",
      requires=(DICE,), forbids=(LUCK_REFUSED,)),
)
ALIVE_ENDINGS = ("kept_life", "chosen_visits", "familiar_company", "sacrifice", "beyond_the_forest")


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
                        "who died may be held to her own; and one whose visits were missed may find a die in her bowl.")
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

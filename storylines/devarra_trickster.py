"""Devarra on the Trickster path: "Clutch-mother" (Writer/handoffs/trickster/devarra.md; family F08, Transformation).
Replaces the unregistered drafts devarra_trickster_opening and devarra_trickster_progression (DEVARRA-01..13 per the
round-2 spec: the DLC1 tower premise, the Hell writ and the tenant arc are cut), kept in reference/retired-drafts/.

Canon: "I am Devarra, bane of the Worldwound" (DLC1 cue ce8e21b7, flavour only); the quest names her "the dragon
Devarra, who attacked your army" (98622d99). She is a woundwyrm (DragonHuntBookEvent3/Cue_0002 05e01257), female,
hunted near Drezen with Greybor. In her lair she sells lives for stories: "I do love to play with my food. What can you
offer me in exchange for your pathetic life? Perhaps I won't kill you if you manage to impress me."
(StoryTellerAndDragonGoodEnter/Cue_0002 546738b4); the Storyteller pays in stories (Cue_0003 6119664e) and she asks "How
interesting. What happened next?" (Cue_0028_EndOfTart 294462fb). Her bad-entry voice: "I will devour you whole, and your
deaths will be slow and agonizing, you parasites!" (StoryTellerAndDragonBadEnter/Cue_0002 a6793a08). Greybor's blade
goes "deep into the dragon's side just beneath [the] wing, where her scaled hide is weakest" (GoodEnter/Cue_0034). Every
live Devarra dies in Chapter 3 (IvorySanctum_MainEtude 977818b7 starts RedDragonKilledInIvorySanctum on her death), where
Xanthir Vang's golems hold her clutch hostage and shout at her carcass (Golems_DragonEggs/Cue_0001 b8dfb42d). The
Storyteller: "For several days she held me prisoner" (KTC_StorytellerIsBack/Cue_0019 6be2fbf6) and "I do not pity her"
(Cue_0021 9fee959d).

Authored, and labelled as authored (polish b9c: no story comes true, no mythic power does the work): the moult is her
own Worldwound biology. A woundwyrm sheds her whole hide as she grows, the new one already grown under the old, and a
wound left behind in a shed hide is a wound healed; her lair is walled with old split hides, one holed through the
chest by a lance. Nobody has ever left a dead woundwyrm whole for three days to see whether a moult begun can finish,
because hunters cut them up for hide and blood. The Commander gambles that it can, and keeps her carcass whole: a
whispered deal with Greybor for the head he would have taken (lair), a con on Xanthir's golems, told she is moulting,
not in breach, so they stand guard over her (Sanctum), or, late, the renderers called off her at a price. The story
told where she can hear it is her canon tariff ("impress me"): it buys a life, the teller's, so she wakes owing the
Commander terms instead of eating the camp. It buys her terms, not her body. The grey new hide; the three days; the
watchtower above Drezen; everything she says after the Sanctum. Her only native unit is a hostile
Mobs-faction monster with no dialog (WoundWormsLair_BlackDragon c540d81c), so the return and the commit are letters, and
every other beat is physical on the Storyteller's hub: he is her canon captive, the one buyer of her tariff who lived,
and her messenger. The courtship around this spine is devarra_tower.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
P = "devarra.trickster."
UNIT = "c540d81c08822c14da75761493427e4c"          # WoundWormsLair_BlackDragon (her name and portrait, E14f; never spawned)
LAIR_LIST = "c8298f1630fd82046986d313ba35f601"     # StoryTellerAndDragonGoodEnter/AnswersList_0030 (after "What happened next?")
LAIR_RETURN = "26650f05010b9ce4cb0202da7e35ce8e"   # GoodEnter/Cue_0029 Greybor: "She's distracted. Attack, now!" (clean)
LAIR_NEXT = "3d5e59ddc658eb947874a1cac31dd6a4"     # GoodEnter/Cue_0012 "What? You again?" (the native fight follows)
GOLEM_LIST = "dd8ac86f25e0f6b4cac75386eb528851"    # IvorySanctum/Golems_DragonEggs/AnswersList_0002
GOLEM_RETURN = "d39b1e850904daa43b7e6dab3a6e7f83"  # Golems_DragonEggs/Cue_0046 "Only a very large creature could lay eggs like these."
GOLEM_NEXT = "9c653a907d8549248bd9d202c1fb8964"    # Golems_DragonEggs/Cue_0045 "These are woundwyrm eggs..."
ST_HUB = "2f5b7e0b76d3c5a42a431e1e33a8db09"        # NPC_Common/StoryTeller_MainDialogue/AnswersList_0004
ST_RETURN = "34a0d078b4ac51547a8f5e0e1c8e1e2c"     # StoryTeller_MainDialogue/Cue_0880 "The Storyteller nods, saying nothing."
GREYBOR_LIST = "174d6c94b6725f44aad1d2a76993a926"  # Companions/Grimbor/AnswersList_0002

STARTED = "devarra.started"
CLOSED = "devarra.closed"
COMMITTED = "devarra.committed"
DEAD_LAIR = "devarra.dead_lair"
DEAD_SANCTUM = "devarra.dead_sanctum"
LATCHED = "devarra.dead.latched"
ESCAPED = "devarra.escaped"
PRIMED = P + "primed"
RETURNED = P + "returned"
DECLINED = P + "declined"
STORY_TOLD = P + "story_told"
ENDING_OWED = P + "cost.ending_owed"
LATE = P + "cost.late"
STORY_SOLD = P + "cost.story_sold"
SHAME_SOLD = P + "cost.shame_sold"
THREATENED = P + "storyteller_threatened"
HUNGRY = P + "cost.woken_hungry"
COOK_GIVEN = P + "cook_given"
COOK_REFUSED = P + "cook_refused"
HUNTING = P + "hunting_druids"
WITHHELD = P + "clutch_withheld"
XANTHIR = P + "pointed_at_xanthir"
MARKED = P + "marked"
UNKNOWN = P + "clutch_unknown"
RUTHLESS = P + "ruthless"
HUNTS = P + "hunts_demons"
TESTED = P + "tested"
TRUE = P + "ending_true"
FLATTERED = P + "ending_flattered"
KEPT_BACK = P + "ending_withheld"
BITTEN = P + "cost.bitten"
KEPT_WHOLE = P + "cost.kept_whole"                  # (b9c) the Commander kept her carcass whole for the moult
LEFT_HUNGRY = P + "left_hungry"
FAILED = "trickster.failed"
ST_DEAD = "storyteller.dead"
EGGS = ("eggs.omelet", "eggs.druids", "eggs.project", "eggs.destroyed")
# --- Option A, "She flies" (Writer/handoffs/trickster/devarra-device-options.md; coordinator-approved 2026-10-01) ---------
# The redesign. Nobody dies and nothing is raised: in canon she breaks off at 10% in her lair (WoundWormLair_Event_Mechanics
# fa1e44ec, "dragon tries to fly away"; the escape cutscene starts RedDragonEscaped 23bea004) and dies only in the Ivory
# Sanctum, where Xanthir's golems hold her clutch under their fists ("Get up and fight... Or else your eggs will be
# destroyed!", Golems_DragonEggs/Cue_0001 b8dfb42d; "the behavioral schematic for controlling the dragon", Cue_0033 234c128b).
# IvorySanctum_MainEtude 977818b7 spawns RedDragon_CR20 in front of the egg chamber on the first entry, so the leash must be
# slipped BEFORE that entry: in the lair she buys the Commander's plan under her own tariff (StoryTellerAndDragonGoodEnter/
# Cue_0002 546738b4 "impress me"), flies at the turn, and does not answer the call. The reviewed native gate (E18,
# src/NativeGate.cs) then takes the Sanctum's own lair-kill branch (the replacement fight; the golems call an absent dragon,
# Cue_0047 ea54d573), and the Commander lowers the fists with the golems' own password (Cue_0008 -> Cue_0016 -> Cue_0028).
# A wrong password is the native Destruction branch: the eggs die, and she knows whom to blame.
# Coordinator ruling (2026-10-01, recorded in the matrix row): the lair-kill, no-hunt and unprepared-escape worlds keep canon
# fate as an entry condition. The moult device (dead.lair_story, dead.setup, dead.storytellers_version, dead.woken) is
# retired by gating; its ids, nodes and choices stay for save safety, and its variant lines stay behind LEGACY gates (a save
# that already returned her through the moult before the redesign).
PACT = P + "flight.pact"                   # the Commander's story from cover, bought on her tariff (lair, before the fight)
STRUCK = P + "flight.struck"               # the stone told she is on an errand, not late (golem master list)
CLUTCH_LEFT = P + "flight.clutch_left"     # the eggs left in the chamber for her (DragonEggs list)
FLOWN = P + "flown"                        # Derived: the pact, and she escaped (latched): the flight world
LEASH = P + "leash_cut"                    # Derived: the flight world, and the golems deactivated (native Cue_0028)
ESCAPE_SEEN = "devarra.escaped.latched"    # Latch of RedDragonEscaped (it reads Playing only, and its parent quest can end)
GOLEMS_MET = "devarra.golems_met.latched"  # Latch of Golems_DragonEggs/Cue_0006 (the fists raised over the eggs, both worlds)
COLLECTED = P + "clutch_collected"         # she took her eggs from the chamber herself
DEBT = P + "debt_claimed"
LEGACY = "devarra.dead.latched"            # a pre-redesign save: she died, and the moult returned her
RETIRED = (P + "dead.lair_story", P + "dead.setup", P + "dead.storytellers_version", P + "dead.woken")
# R2-6: read by Last Call only (epilogue pages set no flags), so it is bound here rather than on demand.
DERIVED = {P + "late_committed": [["trickster.ever", TESTED]],
           FLOWN: [["trickster.ever", PACT, ESCAPE_SEEN], ["trickster.ever", PACT, ESCAPED]],
           LEASH: [[FLOWN, "devarra.golems_deactivated"]]}
LATCHES = {ESCAPE_SEEN: ["devarra.escaped"], GOLEMS_MET: ["devarra.golems_met"]}
SEEN = {"devarra.golems_deactivated": ["450b4a857a418f24c87ca6ae3984e4ff"],    # Golems_DragonEggs/Cue_0028 "Deactivation command received."
        "devarra.golems_met": ["24de2c3ecf95fc640a84a5211d90121d"]}            # Golems_DragonEggs/Cue_0006 (fists over the eggs)
# E18 reviewed native gates: while she has flown on the pact, the Sanctum takes its own absent-dragon branches.
GATE_WHEN = [["trickster.ever", FLOWN]]
NATIVE_GATES = {"ivory_sanctum.red_dragon_spawn": dict(Target="977818b761d048d49a0fe19a1c8fccc4", Relationship="devarra", When=GATE_WHEN),
                "golems_dragon_eggs.over_body": dict(Target="b8dfb42d03fc931409f2b80614cfa9de", Relationship="devarra", When=GATE_WHEN)}

RELATIONSHIP = dict(
    Title="The Woundwyrm's Tariff",
    Description="A woundwyrm who sells lives for stories let the Commander buy two of them, hers and her clutch's. She is keeping count of what she was given, and of what it cost.",
    Objective="Survive Devarra's attention",
    Guidance=("On the Trickster path, in Devarra's lair, speak from cover before Greybor strikes and pay her tariff with a "
              "better story. Then fight her, and when she breaks for the sky at the end, let her fly. In the Ivory Sanctum, "
              "Xanthir's golems will call for her: find the word that makes them listen, and lower their fists before they "
              "decide she is late. Afterwards she comes to you; the Storyteller carries the rest."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[DEAD_LAIR, DEAD_SANCTUM, "inhuman"], FailureFlags=[],
    UnavailableOverrides={DEAD_LAIR: RETURNED, DEAD_SANCTUM: RETURNED},
    TricksterAccess={
        "dead_sanctum": dict(detect=[DEAD_SANCTUM], device=P + "dead.woken", returned=RETURNED),
        "dead_lair": dict(detect=[DEAD_LAIR], device=P + "dead.woken", returned=RETURNED),
    },
)


def dv(id, text, *choices, **kw):
    """Devarra's own voice: her unit's name and portrait (E14f)."""
    return n(id, "Devarra", text, *choices, portrait="Devarra", speaker_unit=UNIT, **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Devarra", **kw)


def teller(id, text, *choices):
    """The Storyteller speaking inline in his own dialog (the native conversant)."""
    return n(id, "conversant", text, *choices)


def storyteller(id, title, entry, nodes, requires, forbids=(), delay=0, into=None, chapters=(3, 5), **extra):
    """A physical scene on the Storyteller's hub in Drezen, returning to his native list (Chapters 3 and 5)."""
    (SCENES if into is None else into).append(scene(id, title, "Devarra", min(chapters), entry, nodes, requires=requires,
                        forbids=(ST_DEAD, *forbids), delay=delay, last=max(chapters), Relationship="devarra",
                        Chapters=list(chapters), AnswerLists=[ST_HUB],
                        NativeReturnCue=ST_RETURN, **extra))


def letter(id, title, nodes, requires, forbids=(), delay=0, **extra):
    """A remote scene (tier B: no friendly unit exists for her anywhere), Chapters 3 and 5 only."""
    SCENES.append(scene(id, title, "Devarra", 3, "", nodes, requires=requires, forbids=forbids, delay=delay, last=5,
                        Relationship="devarra", Chapters=[3, 5], Remote=True, **extra))


# --- LEGACY (retired by gating, Option A; ids kept for save safety). Primer A: the ending of her own story --------------
# Directive 9 foresight on her own tariff. The injected answer is a sibling of native Answer_0032 ("I have an interesting
# story for you, too!") with the same next cue (Cue_0012) and the same Chaotic shift, so the native fight follows.

SCENES.append(scene(P + "dead.lair_story", "What happened next", "Devarra", 3, '[Speak from cover] "I know a better ending."', [
    nar("hides", '''{n}She has heard you, and she waits for the rest; a dragon who sells lives for stories does not interrupt one. Behind the rocks, all the while the old elf was talking, you were looking at the walls. They are hung with hides: black, enormous, dry as old paper, each one split along the spine from the horns to the tail and left where it fell, like a snake's cast skin. There are six that you can count. The oldest is grey with dust. The one nearest the entrance has a hole low in the chest you could put your arm into, the edges ragged where a lance went in.{/n}
{n}Whatever wore that hide took a wound that should have killed it, shed the wound with the skin, and is lying twenty paces away listening to a story. It is a guess, and nobody has ever tested it: that a thing which can shed a mortal wound might shed a death, if nobody cuts it open first.{/n}''',
        c("[One whisper to Greybor first.]", "greybor"),
        c('"Never mind."', abort=True)),
    nar("greybor", '''{n}Greybor does not take his eyes off the soft place under her wing.{/n} "Whisper, then. I'm working." "Hunters' talk. A wyrm killed in her shed dies wrong, they say, slow, like a coal in ash. I never met a man who waited to see. Talk."
{n}You tell him: when she falls, she stays whole. No head, no heart, no hide off her. Nobody cuts her for three days; not him, not the quartermaster's renderers.{/n}
"The head's my proof and half my fee. The rest of her's worth more than the fee." {n}One eye swivels to you, flat and professional.{/n} "You want to pay a dragon's worth to leave a dragon lying in a ditch, that's your coin. Double. From the war chest, not from you; I've seen your purse."''',
        c("Continue", "story")),
    nar("story", '''{n}Your voice carries from behind the rocks. The dragon does not turn yet. The old elf has stopped talking, and she is waiting to hear how a story ends, the way she has waited on every story in this lair: head low, one claw curled around the prisoner's ankle, as if he might get up and leave before the last line.{/n}
{n}Beside you Greybor has gone completely still. He looks at you as though you have started singing in the middle of an ambush. Then he looks at the soft place under her wing, and waits too. You have bought her carcass. Now you pay her tariff, while she can still hear it, for the life she will want to take when she wakes.{/n}''',
        c('[Tell her the end of her own story, and pay Greybor double] "The hunters come. The dragon falls. Everyone swears she\'s a corpse, and they want her hide. But one of the hunters counted the old skins on her wall, and keeps the knives off her for three nights. Whether she gets up is her own business. If she does, the first thing she sees is the one who told her this."',
          mythic="Trickster", alignment=("Chaotic", 1), crusade=("Finances", -200), native_next=LAIR_NEXT,
          flags=(PRIMED, STORY_TOLD, ENDING_OWED, KEPT_WHOLE)),
        c('"Never mind."', abort=True)),
], requires=("trickster",), forbids=(PRIMED, DEAD_LAIR, DEAD_SANCTUM), last=3, Relationship="devarra", Chapters=[3],
    AnswerLists=[LAIR_LIST], NativeReturnCue=LAIR_RETURN, TricksterDevice=True, TricksterState="dead_lair"))


# --- LEGACY (retired by gating, Option A). Primer B: the golems over the carcass -------------------------------------
# Only when the body lies in front of them (Cue_0001); the trick continues into Cue_0045, where the native answers still
# decide the clutch. The payment is her tariff: the story is told over a body minutes dead, while she can still hear it.
# The lair-death world (Cue_0047) gets no golem trick: that carcass is days old, and deaf.

SCENES.append(scene(P + "dead.setup", "No order about clutch-mothers", "Devarra", 3, '"Golem. State the lizard\'s orders."', [
    nar("carcass", '''{n}The woundwyrm lies where she fell, across the chamber floor in front of the golems, one wing half open like a torn tent. Smoke still leaks from her nostrils. Her eyes are open and already clouding, and when your boots scrape on the stone one of them turns a hair's breadth toward the sound. Dragons die slowly. This one has always listened to the end of a story.{/n}
{n}Where the fall split her hide along the spine, what shows through the crack is not meat. It is grey, and dry, and new, like the skin under a snake's in the week before it sheds. It might be a second hide, half grown. It might be the last thing a dying wyrm grows, and nothing under it at all. There is no way to know but to leave her whole and wait, and nobody who ever killed a woundwyrm has waited.{/n}
{n}The nearest golem has not lowered its fist. It stands over the clutch exactly as Xanthir Vang taught it to stand, waiting for the lizard to get up and fight, because nobody ever told it what to do if she did not.{/n}''',
        c("Continue", "orders")),
    n("orders", "Golem", '''{n}The magical mouth works, stops, and works again.{/n} "Orders: fight. Or the eggs are destroyed. The lizard is not fighting. Clarify: is the lizard in breach?"''',
      c('[Tell the golems she is moulting, loud enough for the dying wyrm to hear] "She\'s not a corpse. She\'s a clutch-mother, and she\'s hungry. Not in breach: shedding. Stand over her until she gets up, and let nobody cut her."',
        mythic="Trickster", alignment=("Chaotic", 1), native_next=GOLEM_NEXT, flags=(PRIMED, KEPT_WHOLE)),
      c('"Forget it."', abort=True)),
], requires=("trickster", "devarra.golems_over_body"), forbids=(PRIMED,), last=3, Relationship="devarra", Chapters=[3],
    AnswerLists=[GOLEM_LIST], NativeReturnCue=GOLEM_RETURN, TricksterDevice=True))


# --- LEGACY (retired by gating, Option A). Late fallback: she died unnamed -------------------------------------------
# host_reason: the Storyteller speaks; he is the only living person who bought his life under her tariff
# (KTC_StorytellerIsBack/Cue_0006 "That was what saved me."), and he spent days blind in her lair with his hands on the
# walls, so he knows the hides. He does not fake her ending: he tells the Commander what the walls were, the Commander
# calls the renderers off the carcass at a price, and he climbs to where she fell and pays her tariff ("impress me",
# Cue_0002) with the Commander's story, so she wakes owing terms. The moult is hers; the story buys the teller's life.

storyteller(P + "dead.storytellers_version", "A story for a carcass", '"You were her prisoner. Tell me what she charged."', [
    teller("price", '''{n}His blind eyes do not move.{/n} "She charged what she charges everyone. A story good enough to impress her, or your life. I paid, and I am here."
{n}He folds his hands on the head of his stick.{/n} "You want me to pay her again, for a dead dragon. The tariff still stands; I have no doubt she would honour it, even now. She keeps her bargains longer than most people keep their word. But I will not spend one of my stories on her. Bring me one of yours. The true one, Commander. From Kenabres to tonight."''',
        c('[Pay his price] "Mine, then. Kenabres to tonight. Every trick."', "walls",
          mythic="Trickster", alignment=("Chaotic", 1), flags=(PRIMED, LATE, STORY_SOLD)),
        c('[Intimidate] "You\'ll tell it my way, old man."', "raised", flags=(THREATENED,)),
        c('"Let her stay dead."', flags=(DECLINED,))),
    teller("raised", '''"Threats are a poor story, Commander. She would have eaten you for that one." {n}He does not raise his voice. He does not need to; the room has gone quiet around him the way a room goes quiet around a man who has been somebody's dinner and walked out.{/n}
"Two, then. The one you are proud of, and the one you are ashamed of. I will know if you leave the second one short."''',
        c('[Pay twice] "Both. The one I\'m proud of, and the one I\'m not."', "walls",
          mythic="Trickster", alignment=("Chaotic", 1), flags=(PRIMED, LATE, STORY_SOLD, SHAME_SOLD)),
        c('"Keep your stories."', flags=(DECLINED,))),
    teller("walls", '''"Before you begin, a thing you ought to know, since you are paying." {n}He turns his cup a quarter turn.{/n} "I spent several days in that lair with nothing to do but feel the walls for a way out. They are not stone. They are hides. Her old ones, split down the back and dry as vellum, and one of them has a hole through the chest I could put my head through. She told me, while she was deciding how I would taste, that she had died in a skin before and left it behind. She also told me she had eaten a bishop. I believed one of those."
"Nobody has ever let a dead woundwyrm lie long enough to find out whether she can do it twice. The crusade's renderers have been at her since she fell, a little at a time; your quartermaster has a price list. Her hide has turned their saws, they complain, and her meat has not rotted in all this time, which is a thing about this one carcass that nobody has thought to ask about. The last I heard, they had the teeth and the wing-leather, and had not reached the spine. Whether anything under that hide can still finish what it started, I cannot tell you. Nobody can. Leave her whole three days and find out."''',
        c('[Call the renderers off her] "Every saw off her tonight, and a guard on her till she gets up or rots. Put it on the quartermaster\'s account."', "climb",
          crusade=("Materials", -100), flags=(KEPT_WHOLE,))),
    teller("climb", '''{n}You send the runner, and then you talk until the candle is a stub. He listens without interrupting, the way only a man who has been someone's dinner listens: all of him, and nothing moving but his breath.{/n}
"Good. It is a very impressive story, and most of it is lies. She will like that."
{n}He takes his stick.{/n} "I will go up to where she fell and tell it to her, bones and all. Whether she gets up is her body's business and your saws'. If she does, she will wake owing a life to whoever paid her tariff, and she always pays. Whether you will enjoy what she pays with is not my affair."''',
        c('"Go."')),
], requires=("trickster", LATCHED), forbids=(PRIMED, DECLINED), delay=24, TricksterDevice=True)


# --- LEGACY (retired by gating, Option A). The moult return; reachable only by a pre-redesign save already primed -----

letter(P + "dead.woken", "The hide splits", [
    nar("wake", '''{n}You do not leave it to luck. There is hunters' talk, the kind Greybor repeats and does not believe, that a wyrm caught in her shed dies wrong and slow; there are the old split hides on her lair wall; and nobody has ever waited to see. So you go to the one man in Drezen who has rendered a woundwyrm and will admit it: Ulrich Danz, the quartermaster's hide-man, who keeps a strip of grey new hide in a jar of brine and swears it was still warm a week after the beast that grew it was dead. His brine is not a cure, and he says so: a new hide already grown under the old one holds some life of its own, and his salt keeps that life from going out with the rest of her, for as long as the salt lasts and no longer, and only while the spine is unopened. Nobody has ever tried it on a whole dragon. His price is the coin, the first shed scale for his jar, and your name on his licence when the Treasury asks why the crusade is buying monster pickle. You pay it. You have two barrels worked into the split along her spine by men you pay not to ask why; a guard of your own, paid by the night; and the quartermaster's renderers kept off her, by order where an order will hold and by a lie about plague in the meat where it will not. If the brine fails, or the lie is found out, she rots like any other carcass, and you have spent good silver on a smell.{/n}
{n}For two days the reports from her carcass said what reports from carcasses say: that it stank, that it had not moved, that the quartermaster wished it minuted he had advised against paying good silver to guard meat. On the third day they stopped making sense.{/n}''',
        c("[Go and look at her on the third night]", requires=(DEAD_SANCTUM,), forbids=(LATE, STORY_TOLD), crusade=("Finances", -150),
          check={"Skill": "SkillLoreNature", "DC": 14, "Success": "wake_sanctum", "Failure": "stalled"}),
        c("[Go and look at her on the third night]", forbids=(DEAD_SANCTUM, LATE), crusade=("Finances", -150),
          check={"Skill": "SkillLoreNature", "DC": 14, "Success": "wake_lair", "Failure": "stalled"}),
        c("[Go and look at her on the third night]", requires=(LATE,), crusade=("Finances", -150),
          check={"Skill": "SkillLoreNature", "DC": 14, "Success": "wake_late", "Failure": "stalled"}),
        # b9c: primed in the lair (Greybor's bargain), escaped, and killed in the Sanctum: the bargain held there too.
        c("[Go and look at her on the third night]", requires=(DEAD_SANCTUM, STORY_TOLD), forbids=(LATE,), crusade=("Finances", -150),
          check={"Skill": "SkillLoreNature", "DC": 14, "Success": "wake_sanctum_told", "Failure": "stalled"})),
    nar("stalled", '''{n}The brine has gone grey and soft in the split, and the split has stopped. Under it the new hide is neither growing nor rotting; it is waiting, the way a fever waits, and it will not wait long. Somebody packed the salt too thin along the spine, or too late. The apothecary says, with his hand out, that another barrel might save it and might not.{/n}''',
        c("[Pay for another barrel and another night's guard, and come back]", abort=True)),
    nar("wake_sanctum", '''{n}The golems had their order now: the lizard is shedding, not in breach; stand over her; let nobody cut her. For as long as they stood, they did exactly what they had been told; when Xanthir's last apprentice came back for the heart with a bone-saw, they turned him out. Your own standing order and two pickets in the egg chamber did the rest, and the crusade's renderers left their wagon at the door. On the third night the hide split along the spine, the way a snake's does, from the horns to the tail.{/n}
{n}What came out of it was wet, and grey as eggshell, and smaller in the shoulder than the thing that had died. It stepped over its own old face without looking down. The golems, having no order about that, let it pass.{/n}''',
        c("Continue", "camp")),
    nar("wake_lair", '''{n}Greybor took his double fee and left the head on. For three days two of your own pickets sat at the gorge mouth with orders nobody understood, and turned back the quartermaster's renderers, and a party of Grimwood trappers with a cart, and one very persistent alchemist. The carcass did not rot. The crows would not land on it. On the third night something inside it began to push, slowly, the way a thing pushes that has all the time in the world and knows it.{/n}
{n}By morning there were two dragons in the gorge. One of them was a split, empty hide. The other one was grey as eggshell, and hungry.{/n}''',
        c("Continue", "camp")),
    nar("wake_sanctum_told", '''{n}She fell in the Sanctum, not in her gorge, but Greybor's bargain was for wherever she fell. He took his double fee and left the head on, and two of your pickets sat three days in the egg chamber with orders nobody understood, and turned back Xanthir's last apprentice and the crusade's renderers alike. On the third night the hide split along the spine, the way a snake's does, from the horns to the tail.{/n}
{n}What came out of it was wet, and grey as eggshell, and smaller in the shoulder than the thing that had died. It stepped over its own old face without looking down.{/n}''',
        c("Continue", "camp")),
    nar("wake_late", '''{n}The renderers came down off the carcass with their saws still clean, cursing the Commander and the quartermaster's ledger in that order. A guard sat by what was left of her for three days. She had no teeth to speak of and one wing was bare bone, and on the third night the hide split along the spine anyway, from the horns to the tail.{/n}
{n}What came out of it was wet, and grey as eggshell, and smaller in the shoulder than the thing that had died, and it came out with new teeth, small and white as a hatchling's, and one wing so thin that it would not carry her far for a month. The guard did not stay to see where it went.{/n}''',
        c("Continue", "camp")),
    nar("camp", '''{n}She finds your camp by smell. The sentries find her by the smell of the sentries.{/n}
{n}Nobody is eaten. A picket line of horses is. When you come out of your tent she is lying across the road with her chin on a cart, grey and dry-sounding when she moves, like paper, and her eyes are the same eyes. That is the part the sentries will talk about afterwards: everything else about her had changed, and the eyes had not.{/n}''',
        c("Continue", "threat_told", requires=(STORY_TOLD,)),
        c("Continue", "threat_sold", requires=(STORY_SOLD,), forbids=(STORY_TOLD, SHAME_SOLD)),
        c("Continue", "threat_shame", requires=(SHAME_SOLD,), forbids=(STORY_TOLD,)),
        c("Continue", "threat_escaped", requires=(ESCAPED,), forbids=(STORY_TOLD, STORY_SOLD)),
        c("Continue", "threat", forbids=(STORY_TOLD, STORY_SOLD, ESCAPED))),
    dv("threat_told", '''"You told me my ending from behind a rock, and then the blades came out." {n}The new hide over the old wound is paler than the rest, a grey seam.{/n} "And then you paid him not to cut me. I lay in the dark and listened for the rest of it. A story buys a life in my lair, crusader. I never said whose. It bought yours."''',
       c("Continue", "mother")),
    dv("threat_sold", '''"The blind elf came to where I lay with a lantern he did not need and told your story to my bones. Kenabres. The lies. All of it." {n}Her lip lifts off one tooth; it is new, and very white.{/n} "It was impressive. And your butchers took my teeth. I pay what I charge, crusader, and I remember what I am charged."''',
       c("Continue", "mother")),
    dv("threat_shame", '''"The blind elf came to where I lay with a lantern he did not need and told your story to my bones. Kenabres. The lies. All of it. It was impressive. I pay what I charge."
{n}The lip lifts a little further.{/n} "He told the shameful part twice. I think he enjoyed it."''',
       c("Continue", "mother")),
    dv("threat_escaped", '''"You let me fly once. Xanthir's toys did not." {n}She breathes out through her nose, and the cart under her chin smokes.{/n} "I will remember which of you was polite. And I heard what you told them over my body. It was a good story, and cruel, and about me, and you made them stand guard over me with it. I pay what I charge."''',
       c("Continue", "mother")),
    dv("threat", '''"You. The little parasite who told a room full of stone a story about me while I was still warm." {n}The new hide over the old wound is paler than the rest, a grey seam.{/n} "I was not quite gone. I heard every word, and then I heard the stone keep the saws off me for three days. A story buys a life from me, crusader, if it is good enough. It was. The life is yours. I pay what I charge, even dead."''',
       c("Continue", "mother")),
    dv("mother", '''"I died a dragon and I got up a dragon. The new hide was growing under the old; it does that, slowly, and I was nearly out of it when they killed me. Whether a shed half done can finish in a dead thing, I did not know. The hunters' talk says it can, and hunters lie for a living. You believed the talk, and bought a renderer's brine to keep the new hide alive while the old one was dead, and paid men to stand over meat, with other people's money. I felt your salt in the split like frost. You had no right to be that lucky." {n}She turns her head, and you see how thin the new hide is over the ribs, like vellum.{/n} "I will tell you what I know, because I can feel it: there is nothing growing under this one. Whatever that was, it was the last of it. Kill me again, crusader, and I stay dead." {n}Her eye does not move from you.{/n} "The hide is mine. The terms are yours: you paid for them before you knew whether there would be anyone to collect. I did not ask for either, and I will not thank you for them."''',
       c("Continue", "failed", requires=(FAILED,)),
       c("Continue", "which_eggs", forbids=(FAILED,))),
    dv("failed", '''"Your little tricks have stopped working, I hear. Good. The ones that kept me whole were not tricks. They were coin, and pickets, and a lie told to stone with a straight face, and those still work. So does my tariff."''',
       c("Continue", "which_eggs")),
    dv("which_eggs", '''{n}She lifts her chin off the cart. The whole camp holds its breath with her.{/n} "Now. My clutch."''',
       c("Continue", "said_omelet", requires=("eggs.omelet",)),
       c("Continue", "said_druids", requires=("eggs.druids",), forbids=("eggs.omelet",)),
       c("Continue", "said_project", requires=("eggs.project",), forbids=("eggs.druids", "eggs.omelet")),
       c("Continue", "said_destroyed", requires=("eggs.destroyed",)),
       c("Continue", "said_unknown", forbids=EGGS)),
    dv("said_omelet", '''"Your city ate my children with herbs." {n}She says it very quietly.{/n} "Every citizen had a plate. I can smell it on your city, on its breath and on the stones of its gate. Someone salted them."''',
       c("Continue", "clutch")),
    dv("said_druids", '''"Your druids carried my eggs into the hills. They smelled of gold, and of lies. I followed them for a day and a night and lost them at a river, and I do not lose things."''',
       c("Continue", "clutch")),
    dv("said_project", '''"They are in your vaults. I can hear them." {n}Her head turns, very slowly, toward Drezen, and stays there.{/n} "Keep them warm, crusader. If they are cold when I come for them, Drezen will be warm enough."''',
       c("Continue", "clutch")),
    dv("said_destroyed", '''"Slop on a golem's fist, or under somebody's boot." {n}Nothing in her voice moves at all.{/n} "Nobody in that chamber stopped it."''',
       c("Continue", "clutch")),
    dv("said_unknown", '''"Xanthir's toys had them, the last I knew. Where they are now, nobody alive has told me." {n}Her eye settles on you.{/n} "You know where the demons kept them. You will find out for me."''',
       c("Continue", "clutch")),
    dv("clutch", '''{n}She waits. It is a very particular kind of waiting, and every horse left on the picket line understands it.{/n}''',
       c('[Give her the cook] "Citadel kitchens, second door. He\'s the one who salted them."', "cook_given",
         requires=("eggs.omelet",), alignment=("Evil", 3), flags=(RETURNED, STARTED, HUNGRY, COOK_GIVEN)),
       c('"The city was starving. Eat demons. There are more of them."', "cook_refused",
         requires=("eggs.omelet",), flags=(RETURNED, STARTED, HUNGRY, COOK_REFUSED)),
       c('"Then go and take them back."', "take_back",
         requires=("eggs.druids",), forbids=("eggs.omelet",), flags=(RETURNED, STARTED, HUNGRY, HUNTING)),
       c('"They\'re safer where they are than with you."', "safer",
         requires=("eggs.druids",), forbids=("eggs.omelet",), flags=(RETURNED, STARTED, HUNGRY, WITHHELD)),
       c('"They\'ll be warm."', "warm",
         requires=("eggs.project",), forbids=("eggs.druids", "eggs.omelet"), flags=(RETURNED, STARTED, HUNGRY, WITHHELD)),
       c('[Tell her who gave the order] "Xanthir Vang built the golems. His students still breathe."', "xanthir",
         requires=("eggs.destroyed",), alignment=("Evil", 1), flags=(RETURNED, STARTED, HUNGRY, XANTHIR)),
       c('"I watched. I didn\'t stop them."', "marked",
         requires=("eggs.destroyed",), flags=(RETURNED, STARTED, HUNGRY, MARKED)),
       c('"I don\'t know where they are. I\'ll find out."', "unknown",
         forbids=EGGS, flags=(RETURNED, STARTED, HUNGRY, UNKNOWN))),
    dv("cook_given", '''"Good. I will be quick with him." {n}She stands, and the cart falls over, and the whole road seems to tilt with her.{/n} "I will not be quick with anyone else."''',
       c("[Watch her go.]")),
    dv("cook_refused", '''{n}She considers you as though you were a door she had not decided whether to open.{/n} "Then I will be patient with your city. Dragons are very patient."''',
       c("[Watch her go.]")),
    dv("take_back", '''"Yes." {n}The word comes out of her with smoke on it.{/n} "That is the first sensible thing a crusader has ever said to me. Keep saying sensible things. It will keep you alive."''',
       c("[Watch her go.]")),
    dv("safer", '''{n}Something very old moves behind her eyes and goes back into the dark.{/n} "Safer. You say that to a mother." {n}She considers the word from every side, the way she considers food.{/n} "Say it again when you know me better. I would like to hear whether you still mean it."''',
       c("[Watch her go.]")),
    dv("warm", '''"They will." {n}It is not agreement. It is a sentence being passed.{/n} "Every night, crusader, I will be listening at your walls. If I hear them stop, I will not need you to tell me why."''',
       c("[Watch her go.]")),
    dv("xanthir", '''"Vang." {n}She tastes the name and puts it away somewhere safe, like a bone for later.{/n} "His students. Yes. I remember students; they run in the wrong direction. You have given me something, crusader. I will not forget which of us gave it."''',
       c("[Watch her go.]")),
    dv("marked", '''"Then you will watch the next thing too." {n}She says it almost kindly, which is the worst way she could have said it.{/n} "I have not picked it yet."''',
       c("[Watch her go.]")),
    dv("unknown", '''"You will." {n}She lowers her head until one eye is level with yours, close enough that you can feel the heat of it.{/n} "And when you do, you will tell me before you tell anyone else. That is how this is going to work."''',
       c("[Watch her go.]")),
], requires=("trickster.ever", PRIMED, LATCHED), forbids=(RETURNED, DECLINED), delay=72, TricksterDevice=True)   # the three days


# --- Option A, 1. The pact (physical, Chapter 3): her tariff, paid from cover, before the native fight -----------------
# The injected answer is a sibling of native Answer_0032 ("I have an interesting story for you, too!"), with the same next
# cue (Cue_0012 "What? You again?") and the same Chaotic shift, so the native fight follows unchanged: she still fights, and
# the escape at 10% is the native one. Authored (labelled): the Commander's reading of a wounded dragon who will not leave
# the country where she is hunted (Obj4_FollowDragonblood 891b83e7: "The dragon was deeply wounded"); her own words about
# the stone and the clutch, which repeat what the golems say in canon (Cue_0001, Cue_0047, Cue_0033).

SCENES.append(scene(P + "flight.pact", "A better story", "Devarra", 3, '[Speak from cover, before the dwarf moves] "That story has a better ending. Mine."', [
    nar("cover", '''{n}Greybor's hand closes on your arm: now, while she is thinking. You do not move. Instead you point him along the ledge to the left, where the rock runs out over her flank and the soft place under her wing: strike from there, when I step out. He goes, quiet as a cat, and the old elf's voice and the drip of the cave swallow whatever is said behind him.{/n}
{n}You have had the whole of the old elf's story to look at her from behind the rocks, and you have spent it looking. The wounds of the Grimwood ambush are still open along her flank; she has licked them and not let them close. A woundwyrm this size has the whole Worldwound to heal in and a sky to do it under, and she is lying hurt in a hunted country, within reach of a crusade, with a meal in her claws she cannot be bothered to finish. Dragons do not stay for gold. They can always find more gold. Something of hers is close, and somebody else is holding it.{/n}''',
        c('[Pay her tariff before the dwarf moves] "The old man\'s story is about a crook with a ring. Mine is about you."', "tariff"),
        c('"Never mind."', abort=True)),
    dv("tariff", '''"Another voice from the rocks." {n}She does not turn her head. The claw around the old elf's ankle does not loosen.{/n} "One of the little parasites who bled me in the forest. I know your smell. Come out and I will eat you second, after the storyteller. Or stay where you are and impress me, and I will decide how long you keep your legs."''',
        c('[Tell it as a fable, loud enough for the dwarf to think you are stalling]', "fable"),
        c('"Never mind."', abort=True)),
    nar("fable", '''{n}You tell it the way the old elf tells his, with a voice for every part, pitched to carry to her and no further. Out on the ledge, Greybor will hear a voice from the rocks telling a hungry beast a fable to hold her still. That is what he is waiting for.{/n}
"Once there was a dragon who was hunted, and wounded, and still would not leave the country where they hunted her. The hunters said she was stubborn. One of them said that somebody had something of hers. A dragon does not stay for gold. She stays for the one thing she cannot steal again."
{n}The tail, which has been sweeping slowly across the stones all this while, stops.{/n}''',
        c("Continue", "named")),
    dv("named", '''"Go on." {n}Very quietly. The old elf, who cannot see her face, has stopped breathing.{/n} "No. I will tell this part, since you have been clever enough to earn it. In the house of ivory there is a chamber, and in it two stone things with a man's voice in their mouths, and under their fists there is a clutch that is mine. Xanthir's pupils put a charm on me with their schematics. When it calls, I go, and I fight what the stone points me at, or the fists close."
{n}Her lip lifts off her teeth.{/n} "That is the story so far. Every ending I have found for it has me dead in it, and the eggs under the fists anyway. Tell me a better one, little parasite, or I start the eating with you."''',
        c('[Tell her the ending] "The hunters come. The dragon fights them, because the dwarf is watching and she has to. When she is losing, she flies. When the stone calls her home, she does not go; she lies up where it cannot see her. Stone does not close its fists on a summons. It talks to intruders first. One of the hunters walks into that chamber as the intruder, and puts a hand in the stone\'s mouth while it is still talking."', "terms"),
        c('"Never mind."', abort=True)),
    dv("terms", '''{n}For a long breath she says nothing at all. Then, loudly, for the rocks and for the dwarf behind them:{/n} "A boring story! A crusader's story! I have heard better from my dinner."
{n}And under the noise of her own scorn, low, for you alone:{/n} "Three nights. I can lie still for three nights while it calls. On the fourth I go back to my eggs and fight whatever it points me at, and I will make sure it points me at you. If the fists close, I will come to your city and find the hunter who told me this, and I will not be quick. If they do not..." {n}The claw slides off the old elf's ankle.{/n} "Then you will have impressed me. Nobody has, in a hundred years. Your dwarf is bored. Come out and fight me properly, and make it look true. I will be very surprised to see you."''',
        c('[Step out of cover, and let her play her part] "You heard her. She wants a fight."', mythic="Trickster", alignment=("Chaotic", 1), native_next=LAIR_NEXT,
          flags=(PACT,)),
        c('"Never mind."', abort=True)),
], requires=("trickster",), forbids=(PACT, DEAD_LAIR, DEAD_SANCTUM, ESCAPED, PRIMED), last=3, Relationship="devarra", Chapters=[3],
    AnswerLists=[LAIR_LIST], NativeReturnCue=LAIR_RETURN))


# --- Option A, 2. The leash (physical, Chapter 3): the stone told she is on an errand ---------------------------------
# On the golems' master lists (after the native password, Cue_0016 507a09ca), returning to the list, where the native
# "Deactivation." (Cue_0028) lowers the fists. The wrong password never reaches these lists: it is the native Destruction.

SCENES.append(scene(P + "flight.leash", "The lizard is on an errand", "Devarra", 3, '"First: the lizard. Report."', [
    n("report", "Golem", '''{n}The magical mouth works, stops, and works again.{/n} "Lizard: called. Lizard: did not come. Lizard is late. Protocol when the lizard is late: the eggs are destroyed. Protocol is pending." {n}The fists over the straw do not move.{/n} "Master: confirm?"''',
      c('[Lie to the stone] "Do not confirm. The lizard is on an errand for me. She is exactly where I sent her."', "amended",
        flags=(STRUCK,)),
      c('"Wait."', abort=True)),
    n("amended", "Golem", '''"Amendment received. Lizard: on an errand for master. Lizard: not in breach." {n}The fists stay exactly where they are. Nothing in the amendment says to lower them, and nothing in the golem will do a thing it was not told.{/n} "Protocol: pending. Master: command?"''',
      c("Continue")),
], requires=("trickster.ever", FLOWN, "devarra.golems_calling"), forbids=(STRUCK, "eggs.destroyed"), last=3, Relationship="devarra",
    Chapters=[3], AnswerLists=["04d72f75c1e841747a55b780fccf37fe", "d1f609c764422a24994568d850c99958", "ab4a075bbc5d24048bf892697e75f2e3"],
    ReturnToList=True, ReturnText="{n}The fists hang over the eggs, waiting for a word.{/n}"))


# --- Option A, 3. The clutch left for her (physical, Chapter 3): on the native egg list, returning to it ----------------

SCENES.append(scene(P + "flight.clutch_left", "Their mother is coming", "Devarra", 3, '[Leave the eggs where they lie] "Nobody touches these. Their mother is coming."', [
    nar("left", '''{n}You post nobody; a guard would be dinner. On the way out you wedge the door to the outer hall open with a dead cultist, wide enough for something the size of a house, and you leave the eggs warm in their straw in the shadow of the golems, ticking faintly as they cool and warm again, like a hearth at night.{/n}''',
        c("[Leave them.]", flags=(CLUTCH_LEFT,)),
        c('"Wait."', abort=True)),
], requires=("trickster.ever", LEASH), forbids=(CLUTCH_LEFT, "eggs.destroyed", "eggs.project"),
    last=3, Relationship="devarra", Chapters=[3], AnswerLists=["b265afc1afe5a4241b1d5d42a4148e75"],
    ReturnToList=True, ReturnText="{n}The eggs lie where they are, warm in the straw.{/n}"))


# --- Option A, 4. She comes for her eggs (remote, tier B: her only native unit is a hostile monster) --------------------

letter(P + "flight.eggs", "What a dragon does with a promise", [
    nar("road", '''{n}One night after the Ivory Sanctum the sentries on the east road lose four horses off the picket line, and nobody hears a thing until the last one screams.{/n}
{n}When you come out of your tent she is lying across the road with her chin on an overturned cart, darker than the dark and bigger than she looked in the gorge. The lair is still on her: the torn web of one wing stiff with dried blood, the long gash under it where your party opened her to the ribs, a frost-burn the shape of a spread hand, white across her jaw. She flew on all of it. Her eyes find you before the sentries do.{/n}''',
        c("Continue", "stone")),
    dv("stone", '''"You fought me well. Too well, at the end; one of yours wanted my heart badly enough to forget whose plan it was." {n}Smoke threads from her nostrils.{/n} "Then I flew. And the charm called, the way it has called me all season, and for the first time I did not go. I lay on a mountain with my wounds open for three nights and let it call, and did not go."
{n}The cart under her chin creaks.{/n} "That is the hardest thing I have ever done, and I did it on the word of a parasite who hid behind a rock."''',
        c("Continue", "failed", requires=(FAILED,)),
        c("Continue", "which_eggs", forbids=(FAILED,))),
    dv("failed", '''"Your little tricks have stopped working, I hear. Good. What you did in that house was not a trick. It was a word said to a stone with a straight face, and those still work. So does my tariff."''',
        c("Continue", "which_eggs")),
    dv("which_eggs", '''{n}She lifts her chin off the cart. The whole camp holds its breath with her.{/n} "Now. My clutch."''',
        c("Continue", "said_omelet", requires=("eggs.omelet",)),
        c("Continue", "said_druids", requires=("eggs.druids",), forbids=("eggs.omelet",)),
        c("Continue", "said_project", requires=("eggs.project",), forbids=("eggs.druids", "eggs.omelet")),
        c("Continue", "said_destroyed", requires=("eggs.destroyed",)),
        c("Continue", "said_left", requires=(CLUTCH_LEFT, LEASH), forbids=EGGS),
        c("Continue", "said_collected", requires=(LEASH,), forbids=EGGS + (CLUTCH_LEFT,))),
    dv("said_omelet", '''"Your city ate my children with herbs." {n}She says it very quietly.{/n} "I lay on a mountain and did not answer the stone, so that a crusader could carry my eggs out from under its fists and down to his kitchens. Every citizen had a plate. I can smell it on your city's breath, and on the stones of its gate. Someone salted them."''',
        c("Continue", "clutch")),
    dv("said_druids", '''"You took them out from under the fists. Then you gave them to men who smelled of gold, and of lies." {n}Her claws close on the cart, and it splits.{/n} "I followed them for a day and a night and lost them at a river, and I do not lose things."''',
        c("Continue", "clutch")),
    dv("said_project", '''"They are in your vaults. I can hear them." {n}Her head turns, very slowly, toward Drezen, and stays there.{/n} "You cut the leash, and then you put a lock where the leash had been. Keep them warm, crusader. If they are cold when I come for them, Drezen will be warm enough."''',
        c("Continue", "clutch")),
    dv("said_destroyed", '''"Slop on a golem's fist." {n}Nothing in her voice moves at all.{/n} "You said you would be in that house before the stone knew I was late. You were. I lay on my mountain and did not go, and you were there, and my clutch is slop on the floor of that chamber anyway."''',
        c("Continue", "clutch")),
    dv("said_left", '''"They were where you left them. Warm." {n}Her breath goes out of her, long, and the picket fires lean away from it.{/n} "The stone stood over them with its hands down, like a beggar, and said nothing when I took them. And somebody had wedged the door open for me with a corpse. I noticed that."''',
        c("Continue", "clutch")),
    dv("said_collected", '''"They were where the stone had left them. Warm." {n}Her breath goes out of her, long, and the picket fires lean away from it.{/n} "Nobody had touched them. Nobody had guarded them, either. I took them up the mountain one at a time, in my mouth, and every time I went back I expected to find the fists closed."''',
        c("Continue", "clutch")),
    dv("clutch", '''{n}She waits. It is a very particular kind of waiting, and every horse left on the picket line understands it.{/n}''',
        c('[Give her the cook] "Citadel kitchens, second door. He\'s the one who salted them."', "cook_given",
          requires=("eggs.omelet",), alignment=("Evil", 3), flags=(RETURNED, STARTED, HUNGRY, COOK_GIVEN)),
        c('"The city was starving. Eat demons. There are more of them."', "cook_refused",
          requires=("eggs.omelet",), flags=(RETURNED, STARTED, HUNGRY, COOK_REFUSED)),
        c('"Then go and take them back."', "take_back",
          requires=("eggs.druids",), forbids=("eggs.omelet",), flags=(RETURNED, STARTED, HUNGRY, HUNTING)),
        c('"They\'re safer where they are than with you."', "safer",
          requires=("eggs.druids",), forbids=("eggs.omelet",), flags=(RETURNED, STARTED, HUNGRY, WITHHELD)),
        c('"They\'ll be warm."', "warm",
          requires=("eggs.project",), forbids=("eggs.druids", "eggs.omelet"), flags=(RETURNED, STARTED, HUNGRY, WITHHELD)),
        c('[Tell her who built the fists] "Xanthir Vang made the golems. His students still breathe."', "xanthir",
          requires=("eggs.destroyed",), alignment=("Evil", 1), flags=(RETURNED, STARTED, HUNGRY, XANTHIR)),
        c('"I was there. I didn\'t stop it."', "marked",
          requires=("eggs.destroyed",), flags=(RETURNED, STARTED, HUNGRY, MARKED)),
        c('"Then the tariff is paid."', "paid",
          requires=(LEASH,), forbids=EGGS, flags=(RETURNED, STARTED, HUNGRY, COLLECTED)),
        c('"Then you owe me."', "owe",
          requires=(LEASH,), forbids=EGGS, flags=(RETURNED, STARTED, HUNGRY, COLLECTED, DEBT))),
    dv("cook_given", '''"Good. I will be quick with him." {n}She stands, and the cart falls over, and the whole road seems to tilt with her.{/n} "I will not be quick with anyone else."''',
       c("[Watch her go.]")),
    dv("cook_refused", '''{n}She considers you as though you were a door she had not decided whether to open.{/n} "Then I will be patient with your city. Dragons are very patient."''',
       c("[Watch her go.]")),
    dv("take_back", '''"Yes." {n}The word comes out of her with smoke on it.{/n} "That is the first sensible thing a crusader has ever said to me. Keep saying sensible things. It will keep you alive."''',
       c("[Watch her go.]")),
    dv("safer", '''{n}Something very old moves behind her eyes and goes back into the dark.{/n} "Safer. You say that to a mother." {n}She considers the word from every side, the way she considers food.{/n} "Say it again when you know me better. I would like to hear whether you still mean it."''',
       c("[Watch her go.]")),
    dv("warm", '''"They will." {n}It is not agreement. It is a sentence being passed.{/n} "Every night, crusader, I will be listening at your walls. If I hear them stop, I will not need you to tell me why."''',
       c("[Watch her go.]")),
    dv("xanthir", '''"Vang." {n}She tastes the name and puts it away somewhere safe, like a bone for later.{/n} "His students. Yes. I remember students; they run in the wrong direction. You have given me something, crusader. I will not forget which of us gave it."''',
       c("[Watch her go.]")),
    dv("marked", '''"Then you will watch the next thing too." {n}She says it almost kindly, which is the worst way she could have said it.{/n} "I have not picked it yet."''',
       c("[Watch her go.]")),
    dv("paid", '''"Paid." {n}She lifts her chin off the cart, and the cart rocks back onto its wheels.{/n} "You told me a story and I did not eat you. That was the tariff. Then you stood in front of Xanthir's stone with your hand in its mouth, for a dragon who would have eaten you the week before." {n}Her eye narrows.{/n} "That was not the tariff. That was something else, and I have not decided what it costs."''',
       c("[Watch her go.]")),
    dv("owe", '''"Owe." {n}She tastes the word as if it had gone off.{/n} "Dragons do not owe, crusader. Dragons are owed. A thing that lends to a dragon is a thing that has decided to be eaten later." {n}Smoke curls off her lip.{/n} "But I will remember who stood in that chamber. When I have decided what that is worth, you will be told. You will not like the coin."''',
       c("[Watch her go.]")),
], requires=("trickster.ever", FLOWN, GOLEMS_MET), forbids=(RETURNED, DEAD_LAIR, DEAD_SANCTUM), delay=48,   # two nights after the golems
    RequiresAnyGroups=[[LEASH, "eggs.destroyed", "eggs.project"]])


# --- Option A, reactions: Greybor (his kill given up, his name stained) and the Storyteller (her captive) -----------------

SCENES.append(reaction("Greybor", "devarra.react.greybor.flown", (RETURNED, FLOWN),
    '''{n}Greybor does not look up from the whetstone.{/n} "You sent me out along that ledge to wait for your story to end. I waited. I took it for stalling. I have been thinking about it since." {n}The stone goes down the edge once more, slowly.{/n} "She broke at the turn like a dragon who had been told when to break. Now there is a dragon on the ridge and a stain on my name for a job I did properly." {n}He looks up.{/n} "Lie to a client if you have to, Commander. Never lie to the knife. Next time you want a thing to live, say so before I draw."''',
    answer_list=GREYBOR_LIST, relationship="devarra", forbids=("greybor.dead", "greybor.kicked_out"),
    entry='"The dragon is back."', chapter=3, last=5, portrait="Greybor", Chapters=[3, 5]))
SCENES.append(reaction("Storyteller", "devarra.react.storyteller.flown", (RETURNED, FLOWN),
    '''"I was under her claw while you told it." {n}The blind elf turns his cup a quarter turn on the table.{/n} "A dragon who would not leave a country where she was hunted. I thought you were buying my life with it. You were buying hers, and mine came back as change: when she flew, she forgot to eat me." {n}He turns his face toward the ridge.{/n} "I ought to be grateful. I find I am only careful. Some stories should be allowed to end, Commander. You have never once let one."''',
    answer_list=ST_HUB, relationship="devarra", forbids=(ST_DEAD,), entry='"About the dragon..."', chapter=3, last=5, Chapters=[3, 5]))


# --- The test (physical, Chapters 3-5): her two demands, carried by the one messenger she does not eat --------------
# host_reason: the Storyteller speaks every line; he is the witness who holds the Commander's story (ledger 9).

storyteller(P + "after.tithe", "What a woundwyrm eats", '"You have been up the ridge. Is she asking for me?"', [
    teller("news", '''"She sent me down with two questions, and she let me keep my legs to carry them. Blind men make good messengers to dragons; we do not flinch at the teeth." {n}He smiles thinly.{/n} "She has taken the old watchtower on the ridge above Drezen. The garrison left it. She did not ask them to."''',
        c("Continue", "late", requires=(LATE,)),
        c("Continue", "cook", requires=(COOK_GIVEN,), forbids=(LATE,)),
        c("Continue", "watch", requires=(MARKED,), forbids=(LATE, COOK_GIVEN)),
        c("Continue", "tithe", forbids=(LATE, COOK_GIVEN, MARKED, FLOWN)),
        c("Continue", "tithe_free", requires=(FLOWN,), forbids=(LATE, COOK_GIVEN, MARKED))),
    teller("late", '''"She says you came to her late and through a stranger's mouth. She has added that to the bill." {n}He tilts his head.{/n} "I did not ask what the bill was in. One learns not to."''',
        c("Continue", "tithe")),
    teller("cook", '''"She says the cook was stringy." {n}He lets that sit a moment.{/n} "Your kitchens are short a man, and nobody in them will say why. They know."''',
        c("Continue", "tithe", forbids=(FLOWN,)),
        c("Continue", "tithe_free", requires=(FLOWN,))),
    teller("watch", '''"She says she is still deciding what you will watch next. She said it twice, so that I would remember the exact words."''',
        c("Continue", "tithe", forbids=(FLOWN,)),
        c("Continue", "tithe_free", requires=(FLOWN,))),
    teller("tithe", '''{n}He counts on his fingers.{/n} "The first: what is she to eat, now that she is awake and a mother and very, very hungry? She took four oxen from the east road on the way to ask. The drovers are complaining to your quartermaster. Your quartermaster is complaining to me, which is how I know I am now part of this."''',
        c('[Send her the cultists in the citadel cells] "Deskari\'s faithful. The ones who won\'t talk. And the carts to haul them."', "ending",
          alignment=("Evil", 2), crusade=("Materials", -100), flags=(RUTHLESS,)),
        c('"She\'s the bane of the Worldwound. Let her hunt it. Feed her from the outer farms until she finds her first demon."', "ending",
          crusade=("Materials", -200), flags=(HUNTS,)),
        c('"She\'ll eat when I say so."', "owned", flags=(CLOSED, "devarra.trickster.refused"))),
    teller("owned", '''{n}The Storyteller sets down his cup.{/n} "I will carry that up, because you have asked me to, and because I would like to see her face, and cannot."
{n}He comes back at dusk without his lantern.{/n} "She said: she does not come back to a keeper. The tower is empty. The oxen are safe. I do not think you will see her again, Commander, unless she decides to be the last thing you see."''',
        c('"So be it."')),
    teller("ending", '''"The second question is older." {n}He turns his face toward the ridge.{/n} "You told her an ending once, or paid me to. She says a story that stops at the dragon getting up is not finished. She wants what happens next. She will judge it. I am to carry it up word for word, and I warn you: she has eaten better storytellers than either of us."''',
        c('[Tell it true] "The dragon gets up. The Commander who lied about her has to live with her. Neither of them knows how that ends."',
          flags=(TESTED, TRUE)),
        c('[Flatter her] "The dragon eats the Commander, and it is the best meal of her life."', flags=(TESTED, FLATTERED)),
        c('"Tell her the story isn\'t finished. She\'ll get the end when there is one."', flags=(TESTED, KEPT_BACK))),
    # Option A: the flight world's hunger and second question (she never died; the story she judges is the pact's).
    teller("tithe_free", '''{n}He counts on his fingers.{/n} "The first: what is she to eat, now that she is off the stone's leash and very, very hungry, with the lair's wounds still closing on her? She took four oxen from the east road on the way to ask. The drovers are complaining to your quartermaster. Your quartermaster is complaining to me, which is how I know I am now part of this."''',
        c('[Send her the cultists in the citadel cells] "Deskari\'s faithful. The ones who won\'t talk. And the carts to haul them."', "ending_free",
          alignment=("Evil", 2), crusade=("Materials", -100), flags=(RUTHLESS,)),
        c('"She\'s the bane of the Worldwound. Let her hunt it. Feed her from the outer farms until she finds her first demon."', "ending_free",
          crusade=("Materials", -200), flags=(HUNTS,)),
        c('"She\'ll eat when I say so."', "owned", flags=(CLOSED, "devarra.trickster.refused"))),
    teller("ending_free", '''"The second question is older." {n}He turns his face toward the ridge.{/n} "You told her a story once, from behind a rock in her lair: a dragon who would not leave a hunted country, and a thief who reached the stone before it knew she was late. She says a story that stops at the thief keeping the bargain is not finished. She wants what happens next. She will judge it. I am to carry it up word for word, and I warn you: she has eaten better storytellers than either of us."''',
        c('[Tell it true] "The dragon flew. The thief kept the bargain. Now they have to live within sight of each other, and neither of them knows how that ends."',
          flags=(TESTED, TRUE)),
        c('[Flatter her] "The dragon eats the thief, and it is the best meal of her life."', flags=(TESTED, FLATTERED)),
        c('"Tell her the story isn\'t finished. She\'ll get the end when there is one."', flags=(TESTED, KEPT_BACK))),
], requires=("trickster.ever", RETURNED, HUNGRY), forbids=(CLOSED,), delay=48)


# --- The commit (remote, tier B). Her verdict, her terms, her refusal on every branch ------------------------------

letter(P + "after.lair", "A tower above Drezen", [
    nar("climb", '''{n}The ruined watchtower on the ridge above Drezen has a new roof: a grey wing, folded. You climb because you were sent for: one line burned into the timber of the north gate at the height of a dragon's head, which the gatekeepers have not dared to plane off.{/n}
{n}Inside, the floor is scattered with bones, sorted by size. She is lying around the broken stair with her head on the parapet, watching the city's lamps come on one by one.{/n}''',
        c("Continue", "second_question", requires=(ST_DEAD,), forbids=(TESTED, FLOWN)),
        c("Continue", "verdict", requires=(TESTED,)),
        c("Continue", "second_question_free", requires=(ST_DEAD, FLOWN), forbids=(TESTED,))),
    dv("second_question", '''"There is nobody left to carry messages, so I will ask you myself." {n}She does not turn her head from the lamps.{/n} "You told me an ending once. A story that stops at the dragon getting up is not finished. What happens next? I will judge it. I have eaten better storytellers than you."''',
       c('[Tell it true] "The dragon gets up. The Commander who lied about her has to live with her. Neither of them knows how that ends."', "verdict",
         flags=(TESTED, TRUE)),
       c('[Flatter her] "The dragon eats the Commander, and it is the best meal of her life."', "verdict", flags=(TESTED, FLATTERED)),
       c('"The story isn\'t finished. You\'ll get the end when there is one."', "verdict", flags=(TESTED, KEPT_BACK))),
    dv("verdict", '''{n}She turns her head at last, and the whole tower creaks with it.{/n}''',
       c("Continue", "true", requires=(TRUE,)),
       c("Continue", "flattered", requires=(FLATTERED,)),
       c("Continue", "kept_back", requires=(KEPT_BACK,)),
       c("Continue", "terms", forbids=(TRUE, FLATTERED, KEPT_BACK))),
    dv("true", '''"A true story. You did not know the end, and you said so, knowing it would come to me and that I bite." {n}Her lip lifts.{/n} "That impressed me. Do not make a habit of it."''',
       c("Continue", "hunted", requires=(HUNTS,)), c("Continue", "cultists", requires=(RUTHLESS,), forbids=(HUNTS,)),
       c("Continue", "terms", forbids=(HUNTS, RUTHLESS))),
    dv("flattered", '''"You lied to me about my own ending, and you lied in my favour. The first liar I have met with manners. Keep doing it."''',
       c("Continue", "hunted", requires=(HUNTS,)), c("Continue", "cultists", requires=(RUTHLESS,), forbids=(HUNTS,)),
       c("Continue", "terms", forbids=(HUNTS, RUTHLESS))),
    dv("kept_back", '''"You kept the end back. Clever. A thing that owes me an ending cannot die before it pays, so I will keep you alive to collect."''',
       c("Continue", "hunted", requires=(HUNTS,)), c("Continue", "cultists", requires=(RUTHLESS,), forbids=(HUNTS,)),
       c("Continue", "terms", forbids=(HUNTS, RUTHLESS))),
    dv("hunted", '''"The Worldwound tastes of rot. I eat it anyway. Someone should." {n}A shred of something black and many-jointed hangs from the parapet, drying.{/n} "They called me its bane once, in a language you do not speak. I have decided to deserve it."''',
       c("Continue", "terms")),
    dv("cultists", '''"Your cultists screamed the name of their god. He did not come. They never do." {n}She sounds, if anything, disappointed in him.{/n} "I kept one alive for a day to see whether he would. I am a patient cook."''',
       c("Continue", "terms")),
    dv("terms", '''"My tariff, then; you know I keep one. The tower is mine; nobody climbs it but you. My eggs, wherever they are, are my business before they are yours. And once a year, where I choose, I take one bite. A small one."
{n}Her breath is very hot, and smells of the forge and of the Worldwound.{/n} "I do love to play with my food, crusader, and you have made yourself very interesting food."''',
       c('[Bare your forearm] "Once a year. Not the sword arm."', "bitten", flags=(COMMITTED, BITTEN), forbids=(FLOWN,)),
       c('"No bites."', "no", flags=(CLOSED, "devarra.trickster.refused")),
       c("[Leave her the tower, and her memory.]", "left", flags=(LEFT_HUNGRY,)),
       c('[Bare your forearm] "Once a year. Not the sword arm."', "bitten_free", flags=(COMMITTED, BITTEN), requires=(FLOWN,))),
    dv("bitten", '''"Not the sword arm. I am not a savage." {n}She looks at your bare arm the way a jeweller looks at a stone she has already decided to buy, and then, deliberately, she looks away from it, back at the lamps of Drezen.{/n}
"Not tonight. I have waited three days in a dead thing for this. I can wait a little longer, and so can you. Go down the mountain. Come back when I send for you."''',
       c("[Go down the mountain.]")),
    dv("no", '''"Then there is nothing in you worth keeping." {n}She puts her head back on the parapet.{/n} "Go down the mountain before I remember the rest of you is edible. A woundwyrm does not ask twice. And she does not forget."''',
       c("[Go.]")),
    dv("left", '''"Go, then." {n}Her eyes are already back on the city.{/n} "I will still be hungry when you come back. You will come back."''',
       c("[Go.]")),
    # Option A variants: she never died; the story she asks after is the pact's, and the wait was on a mountain, not in a corpse.
    dv("second_question_free", '''"There is nobody left to carry messages, so I will ask you myself." {n}She does not turn her head from the lamps.{/n} "You told me a story from behind a rock once: a dragon who flew, and a thief who kept a bargain with a stone. A story that stops there is not finished. What happens next? I will judge it. I have eaten better storytellers than you."''',
       c('[Tell it true] "The dragon flew. The thief kept the bargain. Now they have to live within sight of each other, and neither of them knows how that ends."', "verdict",
         flags=(TESTED, TRUE)),
       c('[Flatter her] "The dragon eats the thief, and it is the best meal of her life."', "verdict", flags=(TESTED, FLATTERED)),
       c('"The story isn\'t finished. You\'ll get the end when there is one."', "verdict", flags=(TESTED, KEPT_BACK))),
    dv("bitten_free", '''"Not the sword arm. I am not a savage." {n}She looks at your bare arm the way a jeweller looks at a stone she has already decided to buy, and then, deliberately, she looks away from it, back at the lamps of Drezen.{/n}
"Not tonight. I lay on a mountain with my side open and let Xanthir's charm call me, on your word. I can wait a little longer for this, and so can you. Go down the mountain. Come back when I send for you."''',
       c("[Go down the mountain.]")),
], requires=("trickster.ever", RETURNED), forbids=(CLOSED, DECLINED), delay=48,
    RequiresAnyGroups=[[RUTHLESS, HUNTS, ST_DEAD], [TESTED, ST_DEAD]])


# --- Reactions (doc 05 section 3.1 row 11: exactly Greybor and the Storyteller). LEGACY: the moult world only ---------

SCENES.append(reaction("Greybor", "devarra.react.greybor.repeat_work", (RETURNED,),
    '''{n}Greybor does not look up from the whetstone.{/n} "I was paid for that dragon. Then somebody kept the saws off her for three days and she climbed out of herself." {n}A shrug.{/n} "Repeat work is billed at the full rate. Tell her that, if she asks who set the ambush. She will."''',
    answer_list=GREYBOR_LIST, relationship="devarra", forbids=("greybor.dead", "greybor.kicked_out", FLOWN),
    entry='"The dragon is back."', chapter=3, last=5, portrait="Greybor"))
SCENES.append(reaction("Storyteller", "devarra.react.storyteller.woken", (RETURNED,),
    '''"She held me in that lair for days, deciding how I would taste. I had my hands on those old hides the whole time and never once thought anyone would be fool enough to wait out a dead one." {n}The blind elf turns his face toward the ridge.{/n} "Some stories should be allowed to end, Commander. You have never once let one."''',
    answer_list=ST_HUB, relationship="devarra", forbids=(ST_DEAD, STORY_SOLD, FLOWN), entry='"About the dragon..."', chapter=3, last=5))
SCENES.append(reaction("Storyteller", "devarra.react.storyteller.sold", (RETURNED, STORY_SOLD),
    '''"I told it the way you paid for. I did not promise to enjoy it." {n}The blind elf turns his face toward the ridge.{/n} "She held me in that lair for days, deciding how I would taste. Now she has a new body to be hungry in, and I bought her terms with your life story, and you bought the three days. Some stories should be allowed to end, Commander. You have never once let one."''',
    answer_list=ST_HUB, relationship="devarra", forbids=(ST_DEAD, FLOWN), entry='"About the dragon..."', chapter=3, last=5))


# --- Epilogue pages (R2-6; ordered siblings) -------------------------------------------------------------------------

SCENES.append(scene(P + "epilogue.woken", "", "DevarraEpilogue", 6, "", [
    nar("page", '''{n}The watchtower above Drezen was never re-garrisoned. Once a year the Commander climbed it alone and came down with a bandaged forearm and no explanation. The surgeons stopped asking after the third year. The scar on the Commander's arm grew into a neat grey crescent, like the bite of a very large, very careful animal, and nobody in Drezen ever said so to the Commander's face.{/n}''',
        paragraphs=(
            p("{n}A cook's knife still hangs over the second door of the citadel kitchens. Nobody uses it, and nobody takes it down.{/n}", requires=(COOK_GIVEN,)),
            p("{n}She followed the druids' trail into the hills every spring and came back every autumn, thinner and furious, with nothing. Once she came back with a single shed scale that was not her own, and would not say whose.{/n}", requires=(HUNTING,), forbids=("devarra.tower.trail_followed",)),
            p("{n}Every spring she flew three rivers east to a valley with a white stone at the top, and lay on the ridge above it for a day, listening to children who were hers and had been raised by a gold dragon. She never went down. She came back each time in a temper that lasted a week, and never once said the gold one's name.{/n}", requires=(HUNTING, "devarra.tower.trail_followed")),
            p("{n}Xanthir Vang's students scattered after the war. Some of them were found. The ones who were not found went on looking over their shoulders for the rest of their lives, which was, the Storyteller said, a kind of being found.{/n}", requires=(XANTHIR,)),
            p("{n}The cells under the citadel were never full again. The garrison said it was because the war was over. The garrison had not been up the ridge.{/n}", requires=(RUTHLESS,)),
            p("{n}The Worldwound's edge learned her name before the crusade's archivists did. The demons had a word for the grey dragon that came at dawn, and it was not a polite one. She was proud of it.{/n}", requires=(HUNTS,)),
        ))],
    requires=("trickster.ever", RETURNED, COMMITTED), last=6, Relationship="devarra"))

SCENES.append(scene(P + "epilogue.commit", "", "DevarraEpilogue", 6, "", [
    nar("page", '''{n}The war ended before the woundwyrm finished her judgment. She finished it afterwards, on her own terms. One winter night a grey dragon landed on the Commander's roof, hard enough to crack the tiles, and put her head down into the yard, where the Commander came out barefoot to meet her.{/n}
"The story will do," she said. "It is not finished, and it is not true, and it is yours. That makes it worth a life. Yours, I think, since you keep spending it on me." {n}Her eye took in the house, the lamps, the door that could be locked and would not stop her.{/n} "My tariff stands. Once a year, where I choose. I will choose the spring, and I will choose the arm, and if you are ever not here when I come, I will take the bite out of the house instead."
{n}She took it in the spring, on the ridge, in a ring of fire. The Commander kept the scar, and the appointment, for the rest of their life, and never once locked the door.{/n}''')],
    requires=("trickster.ever", TESTED), forbids=(COMMITTED, CLOSED, DECLINED, LEFT_HUNGRY), last=6, Relationship="devarra"))

SCENES.append(scene(P + "epilogue.refused", "", "DevarraEpilogue", 6, "", [
    nar("page", '''{n}A grey woundwyrm hunted the Worldwound's edge for years. She never came near Drezen again. Dragons have excellent memories, and hers had a Commander in it.{/n}''')],
    requires=("trickster.ever", RETURNED, CLOSED), last=6, Relationship="devarra"))

SCENES.append(scene(P + "epilogue.hungry", "", "DevarraEpilogue", 6, "", [
    nar("page", '''{n}The tower above Drezen kept its grey roof. Nobody knew what she was waiting for. On clear nights the sentries on the city wall could see her eyes up there, two coals in the dark, fixed on one particular window.{/n}''')],
    requires=("trickster.ever", LEFT_HUNGRY), forbids=(COMMITTED,), last=6, Relationship="devarra"))


def integrate(payload):
    """World keys (death etudes, egg fates, the golem and lair cues, the latch, the Storyteller's death) bind on demand in
    trickster_world; the late commit is bound here because no scene reads it yet."""
    for key, groups in DERIVED.items():
        payload.setdefault("Derived", {})[key] = [list(g) for g in groups]
    # Option A: the latches, the golem cues and the reviewed native gates; the moult device is retired by gating.
    for key, sources in LATCHES.items():
        payload.setdefault("Latches", {})[key] = list(sources)
    for key, cues in SEEN.items():
        payload.setdefault("SeenCues", {})[key] = list(cues)
    for key, gate in NATIVE_GATES.items():
        payload.setdefault("NativeGates", {})[key] = dict(gate, When=[list(g) for g in gate["When"]])
    for s in payload["Scenes"]:
        if s["Id"] in RETIRED and "trickster.ever" not in s["Forbids"]:
            s["Forbids"].append("trickster.ever")
    # Q11 history gates (devarra_tower): Greybor's strike is named only where its native cue was seen; the Abyss vigil only
    # where the tower was climbed while the Chapter03 etude was still playing (it completes at ToNexus).
    payload.setdefault("SeenCues", {})["devarra.greybor_struck"] = ["5a083cd26e6c39b46b3eddcf648f87c8"]   # GoodEnter/Cue_0034
    payload.setdefault("Etudes", {})["devarra.chapter_three"] = "15e0048c7daf0ac4999c2313b58df0e3"        # Chapter03

"""Melazmera on the Trickster path: "Salt the hoard" (Writer/handoffs/trickster/melazmera.md for the canon research; the
binding plan is 11-ROSTER-PLAN-2 §2, the Melazmera block and build sheet, rewritten 2026-09-30 in R5. It supersedes the
spec's dead-world pit, the "lapdog" word, the bite price and the Queen's bones clause).

Canon:
- "Melazmera, the umbral dragon of Colyphyr" (achievement 37234663). Her only unit (85c7a3fd) has no dialog; her attacks
  drain life (MelazmeraEnergyDrainOnAttack 2f37af58). She met the Commander's airship over Colyphyr: on one branch she ate the
  crew off the deck (AirAdventures/Cue_0494 04805628, `melazmera.ate_sailors`); on others the ship got away from her, once
  with the captain's harpoon in her hide (Answer_0432 f35d1825 -> Cue_0231 7c50e8a8, `melazmera.harpooned`).
- The Fulsome Queen: "She bragged about eating everything, even dead souls! She giggled and said she'd never had anything
  like me before!" (FulsomeQueen/Cue_0102 d9cf5c5e). She is "always out hunting... the cave just stands there empty"
  (Cue_0046 35fca27d), a big wet cave with a hole in its roof where the rain falls in.
- Her hoard is a trap (Cue_0078 ee90b60e / Cue_0079 87aeec42, shared string 832dc662): touch the treasure and she comes home
  "in the blink of an eye"; the crown and the coins are "silly rocks that have been wrapped in illusions", and "the real
  treasure looks like boring rocks". A true-seeing check in the lair lifts the illusion (UnlockableFlags 47359cb2 /
  3b2bba05).
- She keeps a truce with Hepzamirah (SlavemasterInterrogation/Cue_0030 326fe8ba). Greybor will not take the Queen's contract
  while she lives (Cue_0112 8a7d6895).

Device (11 §2 R5, a gift of theft): while she hunts, the Commander walks into the empty lair and leaves one real thing,
disguised the way she hides hers: the Knight Commander's seal ring, caked in the cave's own clay to pass for one of her
boring rocks, set among the real stones without touching the bait. SkillThievery DC 26 (22 once the illusion has been lifted);
by hand, no mythic power. Failure: the wrist brushes the bait, she is home, her drain greys two fingers of the ring hand, and
she takes the ring herself. No thief has left an unbidden gift among her stones; she hunts this giver out of curiosity, not rage. The kill
stays canon: touch the bait and kill her, and the route closes (§5.1). Leaving Colyphyr before the salt is an entry condition
(coordinator ruling); a salted Commander who leaves before the next Colyphyr rest is found anyway (`ch4.hunt_found`).

Commit: a theft she allows. In her new lair at the Wound's edge (authored) she names the Commander part of her hoard, and the
thief who knows which rocks are real takes one; that is her yes. Player-caused no: the crown (the bait). Recovery is a joint
act, a hunt on the Wound's edge, not a wait. Cost: the seal on her claw for good; two grey fingers on a failed salt; her
tail-lash on a failed hunt. Her Chapter 5 voice comes through Greybor (she hires the one sellsword in Drezen who takes monster
contracts, and pays first) or a stone at the window. melazmera_hoard holds the letters in stone and the night visits.

Path fit (ROUTE-BRIEF-R, v1): every scene is T (the build sheet: v1 all T; v2 N-fit on Demon, Lich and Swarm-That-Walks).
Canon fate stands everywhere: she lives unless the player kills her. No non-Trickster commit or ending is written yet.
"""
import copy

from story_format import c, n, p, reaction, scene
from storylines import household

SCENES = []
REL = "melazmera"
M = "melazmera.trickster."

DREZEN = "2570015799edf594daf2f076f2f975d8"
COLYPHYR = "c876d5303f4a19f4a80b0cc9b313db6f"          # World/Areas/Act_4_MidnightIsles/ColyphyrDungeon (CampingAllowed)
QUEEN_LIST = "5c08af90f48f60b42b9f14ab0e0e3220"        # FulsomeQueen/AnswersList_0037 (the contract list; Cue_0079 returns here)
GREYBOR_LIST = "174d6c94b6725f44aad1d2a76993a926"      # CompanionDialogues/Grimbor/AnswersList_0002
NENIO_HUB = "1ab909cc3a6194840b1475b99547c263"         # CompanionDialogues/Nenio/AnswersList_0015

STARTED = "melazmera.started"
CLOSED = "melazmera.closed"
COMMITTED = "melazmera.committed"

# Native keys. The new ones are bound in integrate(); the merged ones bind on demand in trickster_world.
DEAD_NATIVE = "melazmera_dead"                         # ColyphyrMelazmeraDead: the canon kill; Playing only while on Colyphyr
DEAD = "melazmera.dead.latched"                        # ...so it is latched there, and the kill stands everywhere afterwards
HOARD_TOLD = "melazmera.hoard_told"                    # the Queen's Cue_0078 / Cue_0079: rocks in crowns, real treasure in rocks
LIFTED = "melazmera.illusion_lifted"                   # DragonTreasure_RocksIllusionLifted
LIFTED_B = "melazmera.illusion_lifted_b"               # DragonTreasure_TreasuresIllusionLifted
SEEN_THROUGH = "melazmera.illusion_seen"               # Derived: either illusion lifted in the lair
HOARD_KNOWN = "melazmera.hoard_known"                  # Derived: told by the Queen, or seen through
ATE = "melazmera.ate_sailors"                          # AirAdventures/Cue_0494: she ate the crew off the deck
HARPOONED = "melazmera.harpooned"                      # AirAdventures/Answer_0432: the captain's harpoon
CREVICE = "melazmera.voyage.crevice"
SCREAM = "melazmera.voyage.scream"
CAPTURED = "melazmera.voyage.captured"
CH5 = "melazmera.ch5"                                  # Chapter05 (Playing)
CH5_LATCHED = "melazmera.ch5.latched"                  # the Chapter 5 anchor for the letter's delay
QUEEN_TURNED = "melazmera.queen_gone"                  # merged Derived: the Queen betrayed, attacked, sulked or fled
QUEEN_MET = "melazmera.queen_contract_offered"         # FulsomeQueen/Cue_0024
GREY_IN = "greybor.in_party"
GREY_DECLINED = "greybor.declined_queen"               # FulsomeQueen/Cue_0112: he would not take the Queen's contract
GREY_GONE = ("greybor.dead", "greybor.kicked_out", "greybor.away")
GREY_ABSENT = "melazmera.greybor_gone"                 # merged Derived: [[greybor.dead], [greybor.kicked_out], [greybor.away]]
HEPZ_DEAD = "hepzamirah.dead"
HEPZ_BACK = "hepzamirah.trickster.returned"            # node variants only (build sheet: no Requires/Forbids on hepzamirah.*)
NENIO_GUARD = ("nenio.dead", "nenio.killed_by_commander", "nenio.sent_away", "nenio.kicked_out", "nenio.dissolved")
NENIO_BACK = "nenio.trickster.returned"

# The route.
PLAN = M + "plan"                    # the Commander told the Queen: someone should leave her something
PROMISED = M + "queen_promised"      # ...and promised the Queen the little crown (a lie: the crown is the bait)
POISON_LIE = M + "queen_poison_lie"  # told the Queen it was poison
SALTED = M + "salted"                # the ring is in the hoard
SEAL = M + "cost.seal_given"         # the Knight Commander's seal ring, on her claw for good
GREY_HAND = M + "cost.grey_hand"     # the failed salt: two fingers of the ring hand, drained grey
FIST = M + "fist_closed"             # the failed salt: the Commander kept a fist round it, and she took it anyway
RETURNED = M + "returned"            # she came looking for the giver, and the Commander was worth coming back to
WHY_TAKES = M + "why.everyone_takes"
WHY_MEET = M + "why.to_meet_her"
WHY_QUEEN = M + "why.not_the_queens_knight"
OWED = M + "terms.owed"              # "You owe me" (the crew, the harpoon, the chase)
RENT = M + "terms.rent"              # "Call it rent"
MISTAKE = M + "mistake"              # "It was a mistake": she flies, and the route closes
GREY_CARRIED = M + "greybor_carried" # Greybor carried her stone, paid in advance
MESSAGE = M + "message"              # her Chapter 5 stone read
FED = M + "fed"
FED_CULTISTS = M + "fed.cultists"    # Evil 1: the stockade's cultists (Ledger secret)
FED_DEMONS = M + "fed.demons"
HERD_INCURRED = M + "herd.incurred"
HERD_SETTLED = M + "herd.settled"
HERD_HONEST = M + "herd.honest"
HERD_HIDDEN = M + "herd.hidden"
HERD_PENDING = M + "herd.pending"
FED_HERD = M + "fed.herd"            # forbidden: she took a Mendevian herd (Favors -50)
SECRET_KEY = "melazmera_cultists"
SECRET = "trickster.secret." + SECRET_KEY
DECLINED = M + "declined"            # took the crown: the lie
HUNTED = M + "hunted"                # the shared hunt on the Wound's edge
LASHED = M + "cost.lashed"           # the failed hunt: her tail
STONE_KEPT = M + "stone_kept"        # one of her real stones in the Commander's keeping for good
LEFT_FREE = M + "left_free"          # took nothing: the heap is closed to the Commander (sets ClosedFlag too)
HEAP = M + "heap_seen"
MORNING_STAYED = M + "morning.stayed"
GREY_WARY = M + "greybor_wary"       # Greybor will not take her coin again (read by the together page)

RELATIONSHIP = dict(
    Title="Salt the Hoard",
    Description=("Melazmera, the umbral dragon of Colyphyr, hunts the island while her hoard waits for thieves. "
                 "I could leave something where others come to take. She may follow the scent of the giver. "
                 "I would rather meet her without a drawn sword."),
    Objective="Find out what Melazmera does with a thief who gives",
    Guidance=("On Colyphyr, ask the Fulsome Queen about the hoard and tell her your plan, or see through the lair's illusions. "
              "Rest on the island while Melazmera is hunting to leave the gift among the real treasure. Keep clear of the bait. "
              "She may come looking at a later rest on Colyphyr, in the Nexus, or after your return to Drezen. "
              "A slain dragon will not come looking."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[DEAD, LEFT_FREE], FailureFlags=[], UnavailableOverrides={},
    TricksterAccess={
        "alive": dict(detect=["!" + DEAD], device=M + "ch4.salt", returned=RETURNED),
    },
)

DERIVED = {
    HERD_PENDING: [[HERD_INCURRED, FED_HERD]],
    SEEN_THROUGH: [[LIFTED], [LIFTED_B]],
    HOARD_KNOWN: [[HOARD_TOLD], [LIFTED], [LIFTED_B]],
    # The Queen's six native outcomes, told apart for the harpy's news (beat.queen): the betrayal itself, a fight, a retreat.
    "melazmera.queen_fought": [["melazmera.fq_attacked"], ["melazmera.fq_disobeyed"], ["melazmera.fq_refused"]],
    "melazmera.queen_withdrew": [["melazmera.fq_retreated"], ["melazmera.fq_sulked"]],
    # 05 §2.5 voice note: she joins as a hoarder; what is in her hoard does not leave, and she says so.
    "melazmera.harem.voice.what_is_mine_stays": [[COMMITTED]],
}
SEEN_CUES = {CREVICE: ["789960b4712abbe4b8b221eb8d45f935"],
             SCREAM: ["bc35171dc7a75ff438693c3c1fb8f0e3"],
             CAPTURED: ["cfc0a9dbb896ca04dae1c57fb9952704"], HOARD_TOLD: ["ee90b60ecefa31f44aeb8a58c1e5ebab", "87aeec42d8aa3544093e3ff144a12e06"]}
SELECTED_ANSWERS = {HARPOONED: "f35d182506d00494293206a940bb5229"}
UNLOCKABLE_FLAGS = {LIFTED: "47359cb2a981461db0c138fdc153bc9f", LIFTED_B: "3b2bba05723d42058469f9ecce3c22d0"}
ETUDES = {CH5: "5b01aa690202e584888dfc600a4aac0a"}
LATCHES = {CH5_LATCHED: [CH5], DEAD: [DEAD_NATIVE]}

# Path fit (ROUTE-BRIEF-R 2026-09-29, v1): T = device or Trickster-only; N-all = any path; N-fit = the fitting paths.
PATH_FIT = {}


def tag(scene_id, fit="T"):
    PATH_FIT[scene_id] = fit


def mz(id, text, *choices, **kw):
    """Melazmera, in the woman she wears or in her own shape (her portrait)."""
    return n(id, "Melazmera", text, *choices, portrait="Melazmera", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, **kw)


def queen(id, text, *choices):
    """The Fulsome Queen, inline on her own contract list (the native conversant and portrait)."""
    return n(id, "conversant", text, *choices)


# --- 1. Chapter 4, Colyphyr (T): the plan, on the Fulsome Queen's list. ----------------------------------------------------

SCENES.append(scene(M + "ch4.plan", "Nobody leaves", "Melazmera", 4,
    '"Everyone who walks into that cave takes something. What would she do if someone left her something?"', [
    queen("start", '''{n}The Fulsome Queen stops wobbling. For a moment the borrowed face of the Lady in Shadow goes perfectly blank, the way a puddle goes blank when a stone has sunk in it and the rings have not come yet.{/n}
"Leaves?" {n}Her voice climbs.{/n} "Nobody leaves! Everybody takes! That is what treasure is for! You go in, you take the shiny things, the lizard comes home and bites you. Everybody knows that!" {n}A long, doubtful slurp.{/n} "Why would you give the fat lizard a present? She tried to eat me! She chewed me! Do you know what it is like to be chewed?"''',
        c('"She\'s been robbed by everyone who ever found that cave. I\'d like to meet the one thief she can\'t make sense of."', "sense"),
        c('[Lie] "It won\'t be a present. It\'ll be poison, and she\'ll carry it into her own nest."', "poison",
          flags=(POISON_LIE,)),
        c('"Never mind. Forget I asked."', abort=True)),
    queen("sense", '''{n}The Queen stares at you with her mouth slightly open. A fly walks across her lower lip and she does not notice.{/n}
"You want to meet her." {n}She says it the way someone else might say "you want to lick the floor".{/n} "She will not want to meet you. She will want to eat you. She eats everything. She said so. She giggled."
{n}Then the doubt drains out of her face, and something much worse fills it: an idea.{/n} "Ohhh. Ohhh! But if you leave a thing in her cave, then she will smell you on it. And she will chase you, all over the island, and not me! Not the Queen!" {n}She claps, wetly.{/n} "That is a very cunning plan. It is almost as cunning as one of mine."''',
        c("Continue", "rocks")),
    queen("poison", '''{n}The Queen gasps with delight, a sound like a boot pulled out of a bog.{/n}
"Poison! In her own nest! She will lie on it and roll on it and lick it, because she licks everything, and then her fat belly will swell up and..." {n}She stops, working at it.{/n} "...and then she will be dead forever! Oh, you are almost as clever as me! Almost!"
{n}She leans closer. The smell comes with her.{/n} "And if she does not die, then she will smell you on it, and chase you, and not me. Either way the Queen wins! I always win."''',
        c("Continue", "rocks")),
    queen("rocks", '''"Listen, knight, because I am only going to tell you the secret once, and I am telling you because you are almost as clever as me." {n}She drops her voice to a bubbling whisper that carries across the whole cave.{/n}
"The shiny things are the trap. The stick with the bird, the dress, the coins, the little crown. If you so much as breathe on them she knows, and she comes home in the blink of an eye, and she is very, very cross." {n}Her eyes slide sideways.{/n} "I did not touch the crown. I did not. I only looked at it a lot.
"The real treasure is in the heap at the back where she sleeps. Grey rocks. Boring, lumpy, stupid rocks, all warm from her fat belly. If you want her to think your thing is treasure, knight, you must make it look like nothing."''',
        c("Continue", "crown")),
    queen("crown", '''{n}The Queen wriggles closer, wheedling.{/n} "And while you are in there, being so clever... you could bring me the little crown. The pretty little crown. A queen should have a crown. Nocticula has lots."
{n}She has already forgotten, apparently, that the crown is a rock, and that the crown is the trap.{/n}''',
        c('[Promise her the crown] "If I can reach it, it\'s yours."', flags=(PLAN, PROMISED)),
        c('"The crown stays where it is. Touch it and she comes home. You said so yourself."', "sulk"),
        c('"We\'ll see what\'s there when I\'ve been inside."', flags=(PLAN,))),
    queen("sulk", '''{n}The Queen puffs up, bubbles, and subsides.{/n} "Nobody ever brings the Queen anything," {n}she says to the ceiling, in a small, drowning voice.{/n} "Everybody takes, and nobody brings. Go on, then. Go and put your present in her stupid cave. See if I care. I do not care."''',
        c("[Leave her to sulk.]", flags=(PLAN,)))],
    requires=("trickster", HOARD_KNOWN), forbids=(DEAD, PLAN, CLOSED), last=4, Relationship=REL, Chapters=[4],
    AnswerLists=[QUEEN_LIST], ReturnToList=True, EntryMythic="PlayerIsTrickster",
    ReturnText="{n}The Fulsome Queen settles back into her filth, humming to herself about crowns. The flies settle with her.{/n}"))
tag(M + "ch4.plan")


# --- 2. Chapter 4, Colyphyr (T): the salt. A rest page while she hunts. ------------------------------------------------------

def place(text, success, failure):
    """The Thievery twins: DC 22 once the lair's illusion has been seen through, 26 on the Queen's word alone."""
    return (
        c(text, check=dict(Skill="SkillThievery", DC=22, Success=success, Failure=failure), requires=(SEEN_THROUGH,)),
        c(text, check=dict(Skill="SkillThievery", DC=26, Success=success, Failure=failure), forbids=(SEEN_THROUGH,)),
    )


SCENES.append(scene(M + "ch4.salt", "Salt the hoard", "Melazmera", 4, "", [
    nar("start", '''{n}The camp is asleep when you take off your boots and go. You go alone. Whatever she finds beside the gift must smell of you and nobody else.{/n}
{n}The cave opens in the rock, a great wet mouth with a hole in its roof, and the rain coming through the hole in a grey column, straight down, as if the sky had been poured into a jug. Somewhere far off over the island, something very large is hunting. You can hear it now and then over the rain: a sound like a sail filling, and then nothing. The cave just stands there, empty.{/n}''',
        c("Continue", "seen", requires=(SEEN_THROUGH,)),
        c("Continue", "told", forbids=(SEEN_THROUGH,))),
    nar("seen", '''{n}You have already seen through enough of the cave's disguises to know the trap. The bait lies by the entrance; the real treasure is at the back, where her body has worn a hollow into the floor. You keep your sleeve clear of the ledge and look for a gap in the heap.{/n}''',
        c("Continue", "salt_real", requires=(LIFTED,)),
        c("Continue", "salt_rocks", forbids=(LIFTED,))),
    nar("told", '''{n}The staff, gown, coins and little crown glitter by the mouth. You leave them untouched. Behind them lies the dull heap the Queen described, with a deep hollow where the dragon sleeps. Rain hisses between you and the ledge.{/n}''',
        c("Continue", "salt_rocks")),
    nar("ring", '''{n}You work the seal ring off your finger. It comes hard; it has not been off your hand since the day you were made Knight Commander, and every order that has gone out under your name since has carried its mark. It is the one thing you own that is entirely yours and entirely the Knight Commander's at once.{/n}
{n}A dragon would know gold. A dragon would smell it from the roof. So you kneel at the edge of the hollow and dig your fingers into the cave's own floor, where the rain has made a grey clay of the rock-dust, and you roll the ring in it, and press it, and roll it again, until what sits in your palm is a lump the size of a walnut, grey, pitted, dull, warm from your hand. A boring rock.{/n}''',
        c("Continue", "heap")),
    nar("heap", '''{n}The hollow at the back is chest-high with treasure. Her belly has pressed a smooth dip into it; her tail has worn a groove beside it. You work along its edge, keeping your elbow below the bait's ledge. The warmth reaches through your sleeve.{/n}
{n}One gap lies within reach. You must set the clay-covered seal there without shifting her possessions or touching the ledge behind your wrist.{/n}''',
        *place('[Set it among the real stones] Reach past the bait ledge and put the clay-covered seal in the hollow.', "set", "brush"),
        c("[Not tonight.] Back away and put the ring on again.", abort=True)),
    nar("set", '''{n}You lower the clay lump into the gap and ease your fingers free. Nothing shifts. Your sleeve clears the ledge. Nothing comes down through the roof.{/n}
{n}Rain falls into the cave. Far out over the sea, something enormous is still hunting.{/n}''',
        c("Continue", "out")),
    nar("out", '''{n}You walk back to camp barefoot in the rain with your hand feeling wrong. Your finger keeps looking for the ring and finding skin. In the morning your quartermaster will have to cut a new seal, and the clerks will talk, and you will tell them it was lost in the Abyss, which is true.{/n}
{n}Behind you, in a cave with a hole in its roof, among her real treasure, lies the Knight Commander's seal, looking like nothing. You wonder how long it will take her to notice. You wonder what she does when she finds one thing in her hoard that is not hers.{/n}''',
        c("[Go back to your blankets.]", flags=(SALTED, SEAL))),
    nar("brush", '''{n}It is the ledge: a lip of stone you did not see in the dark, and the back of your wrist grazes it on the way out, the lightest touch, the kind you would not feel on a crowded street.{/n}
{n}For one heartbeat you hear nothing but rain. Then the rain stops. It does not stop falling; it stops reaching you. Something has closed over the hole in the roof.{/n}''',
        c("Continue", "caught")),
    mz("caught", '''{n}She comes down through the roof like a shadow poured through a funnel, and the cave is suddenly full of her: plates the colour of a bruise, a neck that goes on and on, two scarlet eyes as big as shields, lit from inside. Her breath smells of cold iron and old fire. She does not roar. She looks at you, kneeling at her heap with your hand still out over it, and then she looks at the lump of clay under your fingers, and then she giggles.{/n}
"A thief," {n}she says. Her voice fills the cave the way water fills a jug.{/n} "Four hundred thieves in this cave, maybe five hundred. I ate all of them. And every one of them had his hand going out." {n}Her head comes down level with yours.{/n} "Yours is going in."''',
        c("[Hold out the ring.] Scrape the clay off it with your thumb and hold it up to her.", "drain"),
        c("[Close your fist on it.]", "fist")),
    mz("drain", '''{n}She does not take it from your palm. She lays one claw along the back of your hand, delicately, the way a jeweller lays a finger on a stone to feel if it is cold, and the cold goes into you. It goes in at the two last fingers and stays there, and when she lifts the claw away they are grey to the second knuckle and you cannot feel them at all.{/n}
"That is how I taste things," {n}she says, pleasantly.{/n} "You taste like a very long war. Now I know you. I will know you anywhere." {n}She hooks the ring off your grey fingers with the tip of the same claw and holds it up to her eye, turning it.{/n} "Go away, thief. Go to your little fire. I want to think about you, and I cannot think while you are standing so close to my supper."''',
        c("[Go, with your hand held against your chest.]", flags=(SALTED, SEAL, GREY_HAND))),
    mz("fist", '''{n}She lays one claw across your closed fist, delicately, the way a jeweller lays a finger on a stone to feel if it is cold, and the cold goes into you. It goes in at the two last fingers and stays there. You feel them open without asking you, grey to the second knuckle, and you cannot feel them at all.{/n}
"There," {n}she says, pleasantly, and hooks the ring out of your dead fingers with the tip of the same claw.{/n} "You came to give it to me. Then you changed your mind. That is the most thief-like thing you have done yet, and I like you better for it." {n}She holds it up to her eye, turning it.{/n} "Go away. Go to your little fire. I want to think about you, and I cannot think while you are standing so close to my supper."''',
        c("[Go, with your hand held against your chest.]", flags=(SALTED, SEAL, GREY_HAND, FIST)))],
    requires=("trickster",), RequiresAnyGroups=[[PLAN, LIFTED, LIFTED_B]], forbids=(DEAD, SALTED, CLOSED),
    last=4, Relationship=REL, Remote=True, Kind="event", Chapters=[4], Areas=[COLYPHYR],
    TricksterDevice=True, TricksterState="alive"))
tag(M + "ch4.salt")
_salt = SCENES[-1]
_salt["Nodes"].extend([
    nar("salt_real", "{n}Rubies and a blue sapphire shine in the hollow. You have stripped the disguise from her real treasure; the seal must still be hidden in clay. You keep your hands off the gems.{/n}",
        c("Continue", "salt_bare_bait", requires=(LIFTED_B,)), c("Continue", "salt_shiny_bait", forbids=(LIFTED_B,))),
    nar("salt_rocks", "{n}The heap still looks like grey rocks. The shallow hollow and the warmth rising from it mark her bed. You crouch beside it with the seal in your palm.{/n}",
        c("Continue", "salt_bare_bait", requires=(LIFTED_B,)), c("Continue", "salt_shiny_bait", forbids=(LIFTED_B,))),
    nar("salt_bare_bait", "{n}On the bait ledge, the little crown has become a lump of rock. Its spell has been exposed; its alarm has not been disarmed. You keep your sleeve clear.{/n}", c("Continue", "ring")),
    nar("salt_shiny_bait", "{n}The little crown still gleams on its ledge. You look past it to the hollow. Let the glitter catch another thief.{/n}", c("Continue", "ring")),
])



# --- 3. Chapter 4 (T): the hunt. She comes looking for the giver at the next rest. -------------------------------------------

HUNT_BODY = [
    mz("arrive", '''{n}She sits down by your fire without being asked, folding herself onto a rock the way a heron folds onto one leg, and the fire leans away from her. She is tall, and dark, and her gown is the colour of a bruise, and on her head, pressed down into black hair, she wears a rock. A plain grey rock, set there like a crown. Her eyes are scarlet, and lit from inside, and do not blink as often as a woman's.{/n}
{n}Behind her, across the camp and up the rocks beyond it, her shadow goes on and on. It has a neck, and wings folded along its back, and it is as long as a ship. It is the only honest thing about her.{/n}
{n}On the smallest finger of her left hand, so loose it rattles, she wears your seal.{/n}''',
        c("Continue", "speech")),
    mz("speech", '''"Everything on this island that walks, I have eaten." {n}She reaches into your cook-pot with two fingers, fishes out a lump of salt pork, and eats it, still steaming. She does not seem to notice the heat.{/n} "Goats. Harpies. Diggers. Demons, when they are fat enough to be worth the bother. Everything that ever walked into my cave, I ate, and everything that walked into my cave had come to take something."
"No thief ever left a present in my lair." {n}She holds up her hand and lets the ring slide down her finger and back.{/n} "They came for my stones. You brought your own. You brought a ring into my cave and went out without it. I have not decided whether to eat you for it."''',
        c("Continue", "swamp", requires=(PLAN,)),
        c("Continue", "why", forbids=(PLAN,))),
    mz("swamp", '''{n}She sniffs, delicately, in the direction of your boots.{/n} "You have been talking to the thing in the swamp. The one that wears the Lady's face and smells like the bottom of a well. She told you where I sleep." {n}Her lip lifts, a little, over teeth that are too many and too white.{/n} "I chewed her once. She did not taste of anything I could name. I spat her out, and she has been telling everyone I tried to eat her ever since, as if that were an insult to her."''',
        c("Continue", "why")),
    mz("why", '''{n}She leans towards you across the fire. The heat does not seem to trouble her at all; it troubles you, from where you sit, more than she does.{/n}
"So. Why." {n}It is not quite a question. It is the tone of someone turning a strange coin over to see what is stamped on the other side.{/n} "You could have taken my crown. You could have taken my coins, and I would have come home and eaten you, and that would have been the end of it, and I would have understood it. Why did you leave a thing?"''',
        c('"Because everyone takes. I wanted to see what you\'d do with someone who didn\'t."', "takes", flags=(WHY_TAKES,)),
        c('"Because I wanted to meet you, and I didn\'t want to meet you over a corpse."', "meet", flags=(WHY_MEET,)),
        c('"Because the swamp queen wanted me to be her knight and kill you, and I don\'t take orders from puddles."', "queen",
          flags=(WHY_QUEEN,), requires=(QUEEN_MET,))),
    mz("takes", '''"What I would do." {n}She turns the ring on her finger.{/n} "I have it. That part is easy. But you carried it into my cave and left without taking anything. I kept turning that over, and it would not come out even."

{n}She giggles.{/n} "I came to look at the thief who made it difficult. Hold still."''',
        c("Continue", "crew")),
    mz("meet", '''"Over a corpse." {n}The giggle again.{/n} "Most things meet me over a corpse. Theirs, usually." {n}She looks you over, slowly, the way a buyer looks over a horse, and does not seem displeased.{/n}
"You could have met me by touching my crown. Everyone does. I come home, and they meet me, and then they are over. You wanted to meet me and go on." {n}She tilts her head.{/n} "That is either very stupid or very greedy. I cannot tell which yet. I like both."''',
        c("Continue", "crew")),
    mz("queen", '''{n}She laughs out loud, and all along the rocks above the camp her shadow's jaws open with it.{/n} "Puddles! Yes!"
"She has been sending knights at me for years. Mercenaries, a dwarf once, a very stupid paladin. They all took her contract. They all touched my crown. I ate them all, and she sent me more, as if she were feeding a pet." {n}Her eyes narrow, amused.{/n} "You heard her contract, and you came into my cave, and you did not touch my crown. So the puddle has lost her knight. Good. I will tell her so, one day, with my mouth full."''',
        c("Continue", "crew")),
    mz("crew", '''"And then there is your ship." {n}She says it lightly, as if mentioning the weather on the day you met.{/n}''',
        c("Continue", "crew_ate", requires=(ATE,)),
        c("Continue", "crew_harpoon", requires=(HARPOONED,), forbids=(ATE,)),
        c("Continue", "crew_missed", requires=(CREVICE,), forbids=(ATE, HARPOONED)),
        c("Continue", "crew_scream", requires=(SCREAM,), forbids=(ATE, HARPOONED, CREVICE)),
        c("Continue", "crew_captured", requires=(CAPTURED,), forbids=(ATE, HARPOONED, CREVICE, SCREAM)),
        c("Continue", "crew_unknown", forbids=(ATE, HARPOONED, CREVICE, SCREAM, CAPTURED))),
    mz("crew_ate", '''"I was hungry that night. Your little sky-ship came over the cliffs like a goose with a broken wing, and it was full of men who shouted and waved their swords, and their swords bounced." {n}She licks her thumb.{/n} "I ate until I was not hungry any more. Sailors are salty. I did not know then that one of the things in that ship was going to walk into my cave and put something in."
{n}She regards you across the fire without a shred of apology in her face, as a cat regards the bird it has already eaten.{/n} "If you have come to be angry about them, be angry quickly. I get bored."''',
        c("Continue", "truce")),
    mz("crew_harpoon", '''{n}She touches her side, under the ribs of the woman she is wearing. Where she touches, for a heartbeat, the gown is not a gown but torn purple plate with a pink welt in it the length of your forearm.{/n}
"Your captain has a harpoon, and a good arm, and no sense. He put the hook in me and his men pulled, and I went over in the air like a gutted fish in front of the whole island." {n}Her voice is perfectly pleasant.{/n} "I bit through his rope and lost your ship in the cliffs, and I have been thinking about that man every night since. I have decided that I will eat him last."''',
        c("Continue", "truce")),
    mz("crew_missed", '''"Your little sky-ship came over the cliffs like a goose with a broken wing, and I came up to meet it, because a goose is a goose." {n}She shrugs, and her shadow's wings shift along the rocks.{/n} "It got away. It went down among the rocks where I do not fit, and I went home hungry, and I was cross all night."
"I remember every meal that got away from me. There are not many. Now I find out that one of them came back of its own accord, into my cave, to give me presents." {n}She smiles at you with too many teeth.{/n} "The world is very strange this year."''',
        c("Continue", "truce")),
    mz("truce", '''{n}She jerks her chin inland, towards the mines, where the island has shaken all week with picks.{/n}''',
        c("Continue", "truce_dead", requires=(HEPZ_DEAD,)),
        c("Continue", "truce_alive", forbids=(HEPZ_DEAD,))),
    mz("truce_dead", '''"I hunted the horned one's diggers until she came to me, and we made a truce, and I left them alone. I was hungry about it for a long time." {n}She says it the way a cat speaks of a closed door.{/n} "She is dead now. I heard her die; the whole island heard it. So the truce is dead too, and her diggers are running about in the dark with nobody to speak for them." {n}She licks her lips.{/n} "They taste the way they always did. Somebody killed my truce. I suppose that was you. You are an expensive thing to have walking about my island."''',
        c("Continue", "name")),
    mz("truce_alive", '''"I hunted the horned one's diggers until she came to me, and we made a truce. Now I leave them alone. What she said to make me stop is between her and me." {n}She says it the way a cat speaks of a closed door.{/n} "She is digging for something she should not have. That is not my business. My business is what walks into my cave."
"If you have come to kill her, I will not stop you. The truce says I will not eat her diggers. It says nothing at all about her." {n}She smiles.{/n} "And it says nothing about you."''',
        c("Continue", "name")),
    mz("name", '''{n}She stands. The shadow on the rocks stands with her, and goes on standing for some time after she has.{/n}
"Melazmera," {n}she says, as though laying a coin down on the table between you.{/n} "That is my name. Nobody on this island has ever needed it. Everything that heard it was already inside me."
"Do not touch my crown, thief. If you touch it, I will come home, and I will have to eat you, and I have not finished deciding whether I want to." {n}She turns the ring on her finger.{/n} "So. You left a thing with me. Tell me what I owe you for it, or what you owe me, or what it was, and choose well. I will remember whatever you say for a very long time."''',
        c('"You ate my crew off the deck of my ship. Now you owe me."', "owed", requires=(ATE,), flags=(OWED,)),
        c('"You wear our harpoon in your side. Call that even, and this a fresh start."', "owed", requires=(HARPOONED,),
          forbids=(ATE,), flags=(OWED,)),
        c('"You chased my ship and missed. Call that my first gift, and this my second."', "owed", requires=(CREVICE,), forbids=(ATE, HARPOONED),
          flags=(OWED,)),
        c('[Call it rent] "Call it rent, for walking about your island."', "rent", flags=(RENT,)),
        c('"It was a mistake. I should have left you nothing."', "mistake")),
    mz("owed", '''"Owe." {n}She rolls the word round her mouth, then bares her teeth.{/n} "The horned one pays before her diggers go out. You leave a ring and come collecting afterwards. You have put your account the wrong way round, thief."
{n}She bends close enough to smell your throat.{/n} "I will come back. You can try to collect. I want to see what you dare ask for with my mouth this close."''',
        c("[Watch her go.]", "leaves")),
    mz("rent", '''"Rent." {n}Her eyebrows go up, and the rock on her head tilts with them.{/n} "You are paying me rent. For my island. With a ring."
{n}She throws her head back and laughs, and far up the cliffs a flock of something shrieks and scatters.{/n} "The horned one keeps a truce with me. The swamp queen pays me in knights, although she does not know it. And now the crusade pays me in jewellery." {n}She wipes her eyes with one knuckle.{/n} "Very well, tenant. I will come and inspect my tenant. Keep your fire lit. I like to see where things are."''',
        c("[Watch her go.]", "leaves")),
    nar("leaves", '''{n}She walks out of the firelight and does not come into the moonlight on the other side of it. There is a sound like a sail filling, very close, and then the night comes back all at once: the wind, the noise, a sentry sitting down very suddenly on the rock and staying there. Nobody says anything for some time.{/n}
{n}In the morning there is a ring of scorched stone where she sat, and your cook-pot is empty, and the pork was not all she took from it. The ladle is gone too.{/n}''',
        c("Continue", flags=(RETURNED, STARTED))),
    mz("mistake", '''{n}She looks at you for the space of a breath. Then she looks down at the ring on her finger, and something in her face closes, like a hand closing on a coin.{/n}
"A mistake." {n}She says it without heat.{/n} "Then you are only a thief after all, thief, and a stupid one, because you did not even take anything." {n}She pulls the ring off and looks at it, and then puts it back on, deliberately, the way a woman puts on a glove.{/n}
"I will keep your mistake. It is mine now. Things in my hoard do not leave." {n}She walks out of the firelight, and does not come back into it.{/n}''',
        c("Continue", flags=(MISTAKE, STARTED, CLOSED))),
]

# Authored responses to positive native voyage outcomes; no invented escape.
HUNT_BODY.extend([
    mz("crew_scream", '"Your ship screamed at me." {n}Her eyes narrow.{/n} "I heard something in it that I did not want in my mouth. Now I have followed its scent to a ring. You are quieter on the ground, thief."', c("Continue", "truce")),
    mz("crew_captured", '"You arrived tied up in a dead captain\'s hold. I saw his men dragging their catch towards the mines." {n}She turns your seal.{/n} "You came for the stones; you found my ring. I like this voyage better."', c("Continue", "truce")),
    mz("crew_unknown", '"Ships bring diggers to the horned one. Sometimes they bring my dinner." {n}She studies your hand.{/n} "But I found this in my cave. Tell me what you want for it."', c("Continue", "truce")),
])

HUNT_OPEN_COLYPHYR = nar("start", '''{n}You wake because the rain has stopped falling on you. It is still raining; you can hear it hissing on the rocks all round the camp, and beyond the fire it is still coming down in grey sheets. It has stopped only here, over you and the fire and the sentry on the near rock, as if something very large had spread a wing over the camp and was holding it there.{/n}''',
    c("Continue", "known", requires=(GREY_HAND,)),
    c("Continue", "stranger", forbids=(GREY_HAND,)))

KNOWN = nar("known", '''{n}Your hand knows before you do. The two grey fingers, which have felt nothing since the cave, prickle as if they were waking from sleep, and then go cold again.{/n}
{n}A woman walks out of the dark on the far side of the fire.{/n}''',
    c("Continue", "arrive_known", forbids=(FIST,)),
    c("Continue", "arrive_fist", requires=(FIST,)))


def arrive_known(tail):
    """Her memory of the failed salt: the ring held out (grey fingers), or the fist she opened herself (fist_closed)."""
    return [
        mz("arrive_known", '''"You held it out," {n}she says, before she sits down.{/n} "You scraped the clay off with your thumb and offered me the ring. Then I put my claw on your hand, and two fingers went grey. You did not run."
"You paid for nothing. Not passage, not a meal, not your life." {n}She turns the ring against her knuckle.{/n} "I lay on my heap wondering what you wanted. ''' + tail + '"',
            c("Continue", "arrive")),
        mz("arrive_fist", '''"You closed your fist," {n}she says, before she has even sat down.{/n} "In my cave. You came to give me a thing, and then with my claw on you, you would not let go of it, and I had to open your fingers myself, and they went grey while I did it."
"That was the part I understood. Everything I have ever caught held on." {n}She sounds genuinely puzzled.{/n} "It was the rest I could not make come out even: that you came in with it at all. I lay on my heap thinking about it. ''' + tail + '"',
            c("Continue", "arrive")),
    ]


SCENES.append(scene(M + "ch4.hunt", "The thief who gave", "Melazmera", 4, "", [
    HUNT_OPEN_COLYPHYR, KNOWN, *arrive_known("So I came to look at you again."),
    nar("stranger", '''{n}The sentry on the near rock has not moved. His eyes are open, and his hand is on his spear, and he is shaking so hard the butt of it clicks on the stone. He is looking at the far side of the fire.{/n}
{n}A woman walks out of the dark there.{/n}''',
        c("Continue", "arrive")),
    *copy.deepcopy(HUNT_BODY)],
    requires=("trickster.ever", SALTED), forbids=(DEAD, RETURNED, CLOSED), last=4, Relationship=REL, Remote=True,
    Kind="visit", Chapters=[4], Areas=[COLYPHYR]))
tag(M + "ch4.hunt")

# The salted Commander left Colyphyr before resting there again: she follows the scent of the hand, anywhere in the Abyss
# (Chapter 4 goes on after Colyphyr: the Ivory Labyrinth, Alushinyrra). The same meeting; only the place changes.
def _found_body():
    """Off Colyphyr the island's etudes do not read (ColyphyrHepzamirahDead plays only in its area), so the truce is told
    without saying whether the horned one still lives."""
    body = [x for x in copy.deepcopy(HUNT_BODY) if x["Id"] not in ("truce_dead", "truce_alive")]
    truce = next(x for x in body if x["Id"] == "truce")
    truce["Text"] = '''{n}She jerks her chin back the way she came, towards her island and its mines, a whole sea of the Abyss away.{/n}
"The horned one came to me once, and her diggers stopped being my dinner. What she said to make me stop is between her and me." {n}She says it the way a cat speaks of a closed door.{/n} "What becomes of her is not my business. My business is what walks into my cave, and what walks out of it, and where it goes afterwards."'''
    truce["Choices"] = [c("Continue", "name")]
    for node_id, old, new in (("speech", "Everything on this island that walks", "Everything on my island that walks"),
                              ("name", "Nobody on this island has ever needed it.", "Nobody on my island has ever needed it.")):
        node = next(x for x in body if x["Id"] == node_id)
        if node["Text"].count(old) != 1:
            raise ValueError("Off-island restaging must hit exactly once: " + old)
        node["Text"] = node["Text"].replace(old, new)
    return body


SCENES.append(scene(M + "ch4.hunt_found", "The thief who gave", "Melazmera", 4, "", [
    nar("start", '''{n}She finds you under the red sky of the Abyss. You wake because the air over your camp has gone still and heavy, the way it goes before a storm, and because every demon within earshot has stopped screaming at once.{/n}''',
        c("Continue", "known", requires=(GREY_HAND,)),
        c("Continue", "stranger", forbids=(GREY_HAND,))),
    KNOWN, *arrive_known("So I came across half the Abyss to look at you again."),
    nar("stranger", '''{n}There is a fire; somebody has lit one, and it was not you. There is a woman beside it who was not there when you lay down.{/n}''',
        c("Continue", "far")),
    mz("far", '''"You did not wait for me," {n}she says.{/n} "You left your ring with me, and then you went about your war as if I would not be able to smell my own property on your hand." {n}She sounds more amused than offended.{/n} "I can smell a goat across a sea. Did you think I could not find one crusader?"''',
        c("Continue", "arrive")),
    *_found_body()],
    requires=("trickster.ever", SALTED), forbids=(DEAD, RETURNED, CLOSED, M + "ch4.hunt"), delay=36, last=4,
    Relationship=REL, Remote=True, Kind="visit", Chapters=[4]))
tag(M + "ch4.hunt_found")


def _drezen_body():
    """The hunt restaged at the Commander's window in Drezen (Chapter 5): the same meeting, the room instead of the camp."""
    body = _found_body()
    subs = [
        ("arrive", "She sits down by your fire without being asked, folding herself onto a rock the way a heron folds onto one leg, and the fire leans away from her.",
         "She climbs down off the sill without being asked and sits on the stone of your hearth, folding herself onto it the way a heron folds onto one leg, and the fire leans away from her."),
        ("arrive", "Behind her, across the camp and up the rocks beyond it, her shadow goes on and on.",
         "Behind her, up the wall and across the ceiling and out through the open window, her shadow goes on and on."),
        ("why", "{n}She leans towards you across the fire. The heat does not seem to trouble her at all; it troubles you, from where you sit, more than she does.{/n}",
         "{n}She leans towards you across the hearth. The firelight catches the edges of her teeth.{/n}"),
        ("crew_ate", "{n}She regards you across the fire without a shred of apology in her face, as a cat regards the bird it has already eaten.{/n}",
         "{n}She regards you across the hearth without a shred of apology in her face.{/n}"),
        ("speech", "She reaches into your cook-pot with two fingers", "She reaches into the supper tray on your desk with two fingers"),
        ("queen", "all along the rocks above the camp her shadow's jaws open with it", "all along your ceiling her shadow's jaws open with it"),
        ("crew_missed", "her shadow's wings shift along the rocks", "her shadow's wings shift along the ceiling"),
        ("name", "The shadow on the rocks stands with her", "The shadow on the ceiling stands with her"),
        ("rent", "far up the cliffs a flock of something shrieks and scatters", "out on the wall a sentry drops his spear"),
        ("truce", "a whole sea of the Abyss away", "a whole world away, through the hole"),
        ("mistake", "She walks out of the firelight, and does not come back into it.", "She goes out over the sill, and does not come back to it."),
    ]
    for node_id, old, new in subs:
        node = next(x for x in body if x["Id"] == node_id)
        if node["Text"].count(old) != 1:
            raise ValueError("Drezen restaging must hit exactly once: " + old)
        node["Text"] = node["Text"].replace(old, new)
    leaves = next(x for x in body if x["Id"] == "leaves")
    leaves["Text"] = '''{n}She goes out over the sill the way she came, and something enormous drops past the window and does not hit the ground. A moment later every dog in the citadel starts barking at once, and goes on barking until the second bell.{/n}
{n}In the morning there is a scorched ring on the stone of your hearth where she sat, and your supper tray is empty, and the pork was not all she took from it. The spoon is gone too.{/n}'''
    return body


SCENES.append(scene(M + "ch5.hunt_window", "The thief who gave", "Melazmera", 5, "", [
    nar("start", '''{n}Drezen is asleep under its own smoke. You wake in your quarters in the citadel because the shutters have been opened from outside, three storeys up, and the night air is coming in, and something is crouched on your windowsill, blotting out the stars.{/n}''',
        c("Continue", "known", requires=(GREY_HAND,)),
        c("Continue", "stranger", forbids=(GREY_HAND,))),
    nar("known", '''{n}Your hand knows before you do. The two grey fingers, which have felt nothing since the cave, prickle as if they were waking from sleep, and then go cold again.{/n}
{n}The thing on the sill unfolds, and it is a woman.{/n}''',
        c("Continue", "arrive_known", forbids=(FIST,)),
        c("Continue", "arrive_fist", requires=(FIST,))),
    *arrive_known("So I came through the hole in your world to look at you again."),
    nar("stranger", '''{n}The thing on the sill unfolds, and it is a woman, tall and dark, with a rock pressed into her hair like a crown.{/n}''',
        c("Continue", "far")),
    mz("far", '''"You ran away," {n}she says.{/n} "You left your ring with me, and then you ran off, all the way to your own world, as if I would not be able to smell my own property on your hand." {n}She sounds more amused than offended.{/n} "There is a hole in your world, thief. I came up through it after you. It was warm."''',
        c("Continue", "arrive")),
    *_drezen_body()],
    requires=("trickster.ever", SALTED, CH5_LATCHED), forbids=(DEAD, RETURNED, CLOSED, M + "ch4.hunt", M + "ch4.hunt_found"),
    delay=36, last=5, Relationship=REL, Remote=True, Kind="visit", Chapters=[5], Areas=[DREZEN]))
tag(M + "ch5.hunt_window")


# --- 4. Chapter 5 (T): the message. Greybor carries it, paid in advance; or it comes through the window. --------------------

GREY_MESSAGE = '''{n}Greybor sets a flat grey stone on the table between you, wrapped in oilcloth and tied with string, and does not take his hand off it at once.{/n}
"A woman came to the north gate last night after curfew, Commander. Tall. Very tall. She wore a rock on her head, which I noticed, because I am paid to notice things. She asked the watch for the sellsword who takes monster contracts. The watch sent her to me, which I will be discussing with the watch."
"She wanted this carried to you. I told her I do not carry letters; I am not a pigeon. So she paid me." {n}He lays a coin beside the stone: thick, old, square-holed gold from no mint you know.{/n} "In advance, as I require. She knew my terms before I named them, and she did not haggle. Nobody who has not been in the trade a very long time pays a sellsword before the work without haggling. I bit it. It is real."
{n}He taps the lump of clay pressed over the knot. In it, sharp and clean, is your old seal.{/n} "It is sealed with your seal, Commander. The one you lost in the Abyss. '''

SCENES.append(reaction("Greybor", M + "ch5.message", ("trickster.ever", RETURNED, GREY_IN, GREY_DECLINED),
    GREY_MESSAGE + '''I will say this for her: she is a better client than that swamp queen. I told you that one would never pay. This one paid twice."''',
    answer_list=GREYBOR_LIST, relationship=REL, chapter=5, last=5, entry='"You look like a man with something to deliver."',
    portrait="Greybor", flags=(GREY_CARRIED,), forbids=(*GREY_GONE, GREY_CARRIED, MESSAGE, CLOSED)))
tag(M + "ch5.message")

SCENES.append(reaction("Greybor", M + "ch5.message_b", ("trickster.ever", RETURNED, GREY_IN),
    GREY_MESSAGE + '''I did not ask her what she was. At those rates, I never ask. But when she walked away from the gate her shadow went on walking for some time after she had turned the corner."''',
    answer_list=GREYBOR_LIST, relationship=REL, chapter=5, last=5, entry='"You look like a man with something to deliver."',
    portrait="Greybor", flags=(GREY_CARRIED,), forbids=(*GREY_GONE, GREY_DECLINED, GREY_CARRIED, MESSAGE, CLOSED)))
tag(M + "ch5.message_b")

STONE_WORDS = '''"THIEF.
I came through the hole in your world. It is a good hole. Things come up out of it warm, and I eat them.
I have a cave on the edge of it now, north of your city, where the ground smokes. It is not as good as my old cave. There is no rain. I carried the heap across in my mouth. It took nine trips, and I did not drop anything, and I did not swallow anything, and I want you to know how hard that was.
Your ring is on my claw. It does not fit. I do not care.
Your city smells of bread and cooked meat and frightened men, and I am hungry. I will come to your window when the moon is thin. Do not have me shot at. It is rude and it does not work.
M."'''

SCENES.append(scene(M + "ch5.message_read", "A stone with your seal on it", "Melazmera", 5, "", [
    nar("start", '''{n}You cut the string with your knife. The clay seal cracks in two across your own device, and the oilcloth falls open.{/n}
{n}It is a stone: flat, grey, the size of a psalter, and heavy. One face of it is covered, edge to edge, in small square letters. They have not been painted or chiselled. They have been scored into the rock by something very hard and very sharp, one careful stroke at a time, the way a child writes who has been told that the letters must be exactly right.{/n}''',
        c("Continue", "words")),
    mz("words", STONE_WORDS,
        c("[Set it on the windowsill, face out.]", flags=(MESSAGE,)),
        c("[Put it with her other stones.]", flags=(MESSAGE,), requires=(M + "stone.first_read",)),
        c("[Put it under your pillow.]", flags=(MESSAGE,)))],
    requires=("trickster.ever", GREY_CARRIED), forbids=(MESSAGE, CLOSED), last=5, Relationship=REL, Remote=True,
    Kind="letter", Chapters=[5]))
tag(M + "ch5.message_read")

SCENES.append(scene(M + "ch5.message_letter", "A stone through the shutter", "Melazmera", 5, "", [
    nar("start", '''{n}The shutter of your window in the citadel is splintered in the morning, and there is a stone on the floor under it the size of a psalter, flat and grey, lying where it landed. Nobody on the wall saw anything. One sentry says that the stars over the keep went out for a moment, a little after the second bell, as if something had flown across them, and that he did not report it because he did not want to be the one who said so.{/n}
{n}There is a smear of clay on one corner of the stone, and pressed into the clay, sharp and clean, is your old seal. One face of it is covered, edge to edge, in small square letters scored into the rock by something very hard and very sharp.{/n}''',
        c("Continue", "words")),
    mz("words", STONE_WORDS,
        c("[Set it on the windowsill, face out.]", flags=(MESSAGE,)),
        c("[Put it with her other stones.]", flags=(MESSAGE,), requires=(M + "stone.first_read",)),
        c("[Nail the shutter back up.]", flags=(MESSAGE,)))],
    requires=("trickster.ever", RETURNED, CH5_LATCHED), forbids=(MESSAGE, GREY_CARRIED, CLOSED), delay=72, last=5,
    Relationship=REL, Remote=True, Kind="letter", Chapters=[5], Areas=[DREZEN]))
tag(M + "ch5.message_letter")


# --- 5. Chapter 5 (T): her hunger. The evil pivot (Directive 3). ------------------------------------------------------------

SCENES.append(scene(M + "ch5.hunger", "When the moon is thin", "Melazmera", 5, "", [
    nar("start", '''{n}The moon is a paring over Drezen. You are awake when the shutter opens, which is as well, because she does not knock.{/n}
{n}She comes in over the sill the way smoke comes in, in the woman she wears: tall, in the bruise-coloured gown, with the grey rock pressed down into her hair. The room is suddenly too small. Her shadow does not fit in it at all; it goes up the wall and across the ceiling and down the other side, and the candle on your desk bends away from it and stays bent.{/n}
{n}She goes straight to your supper, which is on the desk, and eats it. All of it, bread and meat and the cheese rind and the bone, and then she looks at the plate as if considering it too.{/n}''',
        c("Continue", "sister", requires=(HEPZ_BACK,), forbids=(FED_HERD,)),
        c("Continue", "city", forbids=(HEPZ_BACK, FED_HERD)),
        c("[Answer the cattle owner.]", "forbid_after", requires=(FED_HERD,))),
    mz("sister", '''"The horned one is walking about your city," {n}she says, with her mouth full.{/n} "In a new body. I smelt her from the roof. She smells of a jar and somebody else's blood, and she is eating onions by the smithy as if she had never been dead in her life."
"Tell her I remember our truce." {n}She licks the last grease from her fingers.{/n} "It died when she did. I have a cave on your side now. If she wants another, she can come to it and talk me out of my supper again. It will spoil her onions."''',
        c("Continue", "city")),
    mz("city", '''"Your city is a larder," {n}she says, licking her fingers one at a time.{/n} "Everything in it is fat, and slow, and frightened, and has never been eaten by anything bigger than a plague. I have been walking about your walls, looking in. I have not eaten anybody." {n}She says it as though describing a feat of arms.{/n}
"And I am hungry, thief. My new cave is at the edge of the hole, and the things that come up out of the hole taste of the hole. Ash and flies. I want something fat."''',
        c("Continue", "ask")),
    mz("ask", '''{n}She comes and sits on the edge of your desk, so close that you feel the cold coming off her, a cold like the inside of a well.{/n}
"There is a hole under your castle with men in it," {n}she says.{/n} "Men who pray to the fly. Your priests have finished asking them questions; I listened at the grating, and they have nothing left to say. They are fat, because you feed them. You are feeding them to nothing." {n}Her scarlet eyes are very bright.{/n} "Give them to me. Nobody will miss them. Your priests will be glad of the room."''',
        c('[Give her the cultists] "Take them. Go down quietly, and leave the grating as you found it."', "cultists",
          alignment=("Evil", 1)),
        c('[Point her at the Wound] "There are demons coming up out of that hole every night. Fat ones. Eat those."', "demons"),
        c('[Forbid it] "Nobody in my cells is food. Nobody in my city is food. Hunt somewhere else."', "forbid")),
    mz("cultists", '''{n}She smiles at you, slowly, with every one of her teeth, and for a moment the woman slips and you see what she is pleased with: something with a long jaw, delighted.{/n}
"There. You are not a priest after all." {n}She slides off the desk.{/n} "I will be quiet. I am always quiet when I eat. It is the ones being eaten who make the noise."
{n}She goes out over the sill. Some time later, far below you, in the cellars of the citadel, somebody begins to pray very loudly to Deskari and stops in the middle of a word, and then there is nothing at all but the sound of the river.{/n}''',
        c("Continue", "cultists_after")),
    nar("cultists_after", '''{n}In the morning the gaoler reports seven cells empty, the locks whole, the grating in its place, and a cold in the cellar that will not come out of the stones for a week. He is a sensible man. He writes "escaped" in his book, and looks at you when he says the word, and does not say anything else.{/n}
{n}There is one stone on your windowsill, small and round, with a single word scored into it: FAT.{/n}''',
        c("Continue", flags=(FED, FED_CULTISTS, SECRET))),
    mz("demons", '''"Demons." {n}Her lip curls off her teeth.{/n} "They taste of the Abyss. I have been eating the Abyss for a very long time, thief. I know what it tastes like. It tastes like being bored."
{n}She considers you, and the dark on the ceiling considers you with her.{/n} "This once. I want to see what your face does when a dragon obeys it." {n}She goes to the window.{/n} "If it feels bad, I will come back and eat your priests' prisoners anyway, and tell them it was your idea."''',
        c("Continue", "demons_after")),
    nar("demons_after", '''{n}For three nights afterwards the pickets on the north road report the same thing: a noise out over the Wound's edge like a ship's sail filling, then screaming, then nothing, and in the morning, scattered across the scorched ground where the rifts open, pieces of things that came up out of the earth in the night and did not get any further.{/n}
{n}On the fourth morning there is a stone on your windowsill, small and round, with two words scored into it: STILL BORED.{/n}''',
        c("Continue", flags=(FED, FED_DEMONS))),
    mz("forbid", '''{n}She stares at you. Then she laughs, delighted, the way she laughed at the fire on Colyphyr.{/n}
"Nobody is food!" {n}She holds her stomach.{/n} "Oh, thief. Everybody is food. You are food. The only question is who is holding the spoon." {n}She gets up and goes to the window, still giggling.{/n}
"Not your prisoners, and not your city. I will find something that is not yours." {n}She looks back at you over her shoulder, and her eyes gleam.{/n} "You did not say anything about your friends' cows."''',
        c("Continue", "forbid_after")),
    nar("forbid_after", '''{n}Two days later a Mendevian lord who has lent the crusade two hundred spears writes to the Knight Commander in a hand shaking with fury. His whole herd, driven up from the south to feed his men, is gone from its pen outside the walls in a single night: forty head of cattle, the pen whole, the gate shut, the herdsmen asleep, and nothing left in the morning but a stink of cold iron and the drovers' dogs, who will not stop howling.{/n}
{n}He wants to know what the Knight Commander means to do about it. He wants to know it in writing. His letter lies beside the empty supper plate. From the roof comes a satisfied belch.{/n}''',
        c('[Lie] "Enemy action. The crusade will compensate your loss."', "herd_cover", flags=(FED, FED_HERD, HERD_SETTLED, HERD_HIDDEN), crusade=("Favors", -50)),
        c('"The dragon took your herd. I will compensate you from the crusade chest."', "herd_honest",
          flags=(FED, FED_HERD, HERD_SETTLED, HERD_HONEST), crusade=("Favors", -50)))],
    requires=("trickster.ever", MESSAGE), forbids=(FED, CLOSED), delay=48, last=5, Relationship=REL, Remote=True,
    Kind="visit", Chapters=[5], Areas=[DREZEN], ForbidOverrides={FED: HERD_PENDING}))
tag(M + "ch5.hunger")
_hunger = SCENES[-1]
next(x for x in _hunger["Nodes"] if x["Id"] == "forbid_after")["EnterSet"] = [FED, FED_HERD, HERD_INCURRED]
next(x for x in _hunger["Nodes"] if x["Id"] == "cultists_after")["EnterSet"] = [FED, FED_CULTISTS, SECRET]
_hunger_start = _hunger["Nodes"][0]
_hunger_opening = _hunger_start["Text"]
_hunger_start["Text"] = "{n}The war council has left your table buried in reports. The north road, the cellar stores, hungry mouths. You go upstairs with the last report still in your hand.{/n}"
for _choice in _hunger_start["Choices"][:2]:
    _choice["Next"] = "hunger_arrival"
_hunger["Nodes"].append(nar("hunger_arrival", _hunger_opening,
    c("Continue", "sister", requires=(HEPZ_BACK,)), c("Continue", "city", forbids=(HEPZ_BACK,))))
_hunger["Nodes"].extend([
    nar("herd_cover", '"A loss to enemy action." {n}The quartermaster reads your reply twice. The lord accepts compensation, but demands double pickets for his remaining stores. That night Melazmera drops a horn on your desk.{/n} "Enemy action. I like my new name."', c("Continue")),
    nar("herd_honest", '{n}The lord\'s answer arrives with the receipt: his spears stay, but no more cattle will come within reach of your dragon. Melazmera reads it over your shoulder.{/n} "Forty cows, and he wants to keep all the others. Greedy." {n}She crunches the corner of the letter. You pull the receipt free before she eats that too.{/n}', c("Continue")),
])

household.secret(
    SECRET_KEY, "The empty cells",
    "Seven of Deskari's cultists were in the cells under the citadel, questioned and finished with. I let the dragon Melazmera "
    "go down to them one night, because she was hungry and I wanted her fed and quiet. The gaoler wrote 'escaped'. He is a "
    "sensible man, and he looked at me when he wrote it. The paladins in my household would have another word for what I did.",
    portrait="Melazmera", witnesses=("seelah", "irabeth"), risk="medium")


# --- 6. Chapter 5 (T): the commit. A theft she allows, in her new lair at the Wound's edge. ---------------------------------

SCENES.append(scene(M + "commit.stone", "What a thief takes", "Melazmera", 5, "", [
    nar("start", '''{n}She does not come in by the window this time. She comes over the roof, in her own shape, and you know it because the whole keep goes quiet under you, every horse in the stables and every dog on the wall, all at once, the way birds go quiet when a hawk is up.{/n}
{n}When you climb out onto the leads she is lying along the ridge of the roof like a cat on a wall, purple-black, as long as the keep, with the moon on her plates and your seal glittering on one foreclaw like a flake of mica. She puts her head down beside you. Her eye is as big as a shield.{/n}
"Get on," {n}she says.{/n} "Mind the spines. I want to show you my cave."''',
        c("[Climb up behind her head.]", "flight"),
        c('"I\'ll need my boots."', "boots")),
    mz("boots", '''"You will not need your boots. You will need your hands, and your knees, and not to fall off." {n}The giggle comes out of her as a great warm gust that smells of cold iron.{/n} "If you fall off, I will catch you. Probably. I have never tried to catch anything that I did not mean to eat. It will be interesting for both of us."''',
        c("[Climb up behind her head.]", "flight")),
    nar("flight", '''{n}The spines along her neck are as thick as your wrist and cold as church brass, and when she moves under you it is like sitting on a hill that has decided to walk. Then the hill jumps. Drezen drops away, the whole citadel, a toy on a black cloth, and the wind takes your breath and does not give it back.{/n}
{n}She flies north, low over the road and then lower over the burned country, where nothing grows and the ground is warm to look at. The rifts of the Wound glow in the dark ahead of you like a row of kilns. She goes down towards one of them, a long black split in the ground with steam coming off its lips, and folds herself, and drops into it.{/n}''',
        c("Continue", "cave")),
    nar("cave", '''{n}It is not the cave on Colyphyr. There is no hole in the roof and no rain; there is a crack in the world with a warm floor, and a smell of hot stone, and a red light coming up from very far below. But she has made it into the same thing.{/n}
{n}At the mouth, laid out on a shelf of rock where the light catches them, are the staff with the golden bird, the gown sewn with stones, the fat coins in a careless spill, and on a ledge of its own the little crown. At the back, in a hollow she has already worn smooth, is the heap: grey, lumpy, dull, nine mouthfuls of it, carried across a world.{/n}
{n}She folds herself down, the way she folds herself to come through your window, and it is the woman who walks up the heap and sits on the top of it, with the rock on her head and your ring rattling on her smallest finger.{/n}''',
        c("Continue", "count")),
    mz("count", '''"Forty-one real stones," {n}she says.{/n} "I have counted them every night since I was the size of a horse. Forty-one. Some are rubies, some are the eyes of statues, one is a lump of star that fell into the sea and came up in a net. I ate the net. I ate the fishermen." {n}She lifts her hand.{/n} "And one seal. Forty-two."
{n}She looks down at you from the heap. The red light from the rift is under her chin, and her eyes are two more coals.{/n} "And one Commander. I have put you in my hoard, thief. I decided it on the way here, somewhere over the burned country. I do not know when it happened. Things in my hoard do not leave."''',
        c("Continue", "why_takes", requires=(WHY_TAKES,)),
        c("Continue", "why_meet", requires=(WHY_MEET,), forbids=(WHY_TAKES,)),
        c("Continue", "why_queen", requires=(WHY_QUEEN,), forbids=(WHY_TAKES, WHY_MEET)),
        c("Continue", "open", forbids=(WHY_TAKES, WHY_MEET, WHY_QUEEN))),
    mz("why_takes", '''"You told me the night we met that everyone takes, and that you wanted to see what I would do with someone who did not." {n}She tilts her head, and the rock on it tilts.{/n} "Now I know. I put {mf|him|her} in my hoard. That is what I do with things."''',
        c("Continue", "open")),
    mz("why_meet", '''"You told me the night we met that you wanted to meet me and not over a corpse." {n}She tilts her head, and the rock on it tilts.{/n} "Well. You have met me, and nobody is a corpse, and you are sitting in my cave. That is further than anyone has ever got."''',
        c("Continue", "open")),
    mz("why_queen", '''"You told me the night we met that you do not take orders from puddles." {n}She tilts her head, and the rock on it tilts.{/n} "You do not take orders from me either. I have noticed. I have decided I do not mind."''',
        c("Continue", "open")),
    mz("open", '''{n}She spreads her hands out over the heap, palms down, the way a merchant lays his goods out on a cloth.{/n}
"But you are a thief," {n}she says softly.{/n} "And thieves take. So take something. Anything in this cave: the crown, the coins, a stone, nothing. Whatever you take, that is what you think I am." {n}She settles back on the heap and watches you, and does not move, and does not blink.{/n} "I will not stop you. That is the trick. That is the whole trick, thief. I will not stop you."''',
        c('[Take one real stone] Climb the heap to her and take one warm grey stone from under her hand.', "stone",
          requires=(SALTED,)),
        c("[Take the crown.]", "crown"),
        c("[Take nothing.]", "nothing")),
    nar("stone", '''{n}You climb the heap. The stones shift and clack under your knees, warm as bread, and she does not move. She taps a grey stone beneath her palm. You reach for that one. You put your hand under hers, flat on the heap, and her fingers are cold as a well, and you slide out from under them one grey stone the size of a hen's egg, lumpy and dull and heavy for its size, and close your hand on it.{/n}
{n}She watches it go. Her whole body goes tight, every line of her, the way a hound's does when you take its bone. Her lip comes back off her teeth. You stop with your wrist beneath them. She presses her free hand into the heap, grinding the stones together, and holds still. You draw the sapphire clear.{/n}''',
        c("Continue", "yes")),
    mz("yes", '''{n}She lets out her breath. It comes out of her in a long hiss, and then, astonishingly, in a giggle, high and shaky, as if she had just jumped off something very tall and found she could fly.{/n}
"I let you," {n}she says.{/n} "I let a thief walk off my heap with a piece of it in {mf|his|her} hand. I have never..." {n}She stops. She looks at her own empty hand as if it belonged to somebody else.{/n}
"That one is a sapphire. It came out of the crown of a king of a drowned country. I have slept on it for two hundred years." {n}Her fingers close on your wrist, hard enough to hurt.{/n} "You keep it, and I keep you. That is the bargain. There is no other bargain. Do you understand me, thief?"''',
        c('"I understand you."', "home"),
        c('[Put the stone in your shirt, over your heart.]', "home")),
    mz("home", '''{n}She flies you back before the sky over the Wound has begun to go grey. On the roof of the keep she puts her head down so that you can slide off, and she does not lift it again at once.{/n}
"Come back tomorrow night," {n}she says.{/n} "Come and lie on the heap. I want to see what my hoard looks like with you in it."''',
        c("[Let her see the sapphire in your pocket.]", flags=(COMMITTED, STONE_KEPT), requires=("trickster.now",)),
        c("[Leave.]", abort=True, forbids=("trickster.now",))),
    mz("crown", '''{n}You walk down the cave to the ledge by the mouth and pick up the little crown. It is heavy and cold and bright, and it goes out in your hand like a snuffed candle. It is a rock, grey and ordinary, with a little glitter of mica on one side.{/n}
{n}She does not move from the heap. She does not come home in the blink of an eye; she is home.{/n}
"You took the lie," {n}she says, and she sounds tired, suddenly, and very old.{/n} "Everyone takes the lie. The dwarf took it, and the paladin, and the puddle would have if she could have reached. I thought you knew better. You did know better. You had your hand in my heap on Colyphyr."''',
        c("Continue", "crown2")),
    mz("crown2", '''"Keep it," {n}she says, and turns her face away.{/n} "It is a rock. Take your rock and go home, thief. I will fly you. I am not so angry that I want you to walk back across the burned country and be eaten by something that is not me."''',
        c("[Take your rock and go.]", flags=(DECLINED,)),
        c('"You told me to take anything. I wanted to see what you\'d do if I took the wrong thing."', "crown3",
          flags=(M + "crown_challenge",))),
    mz("crown3", '''{n}She turns back, and looks at you, and the scarlet in her eyes flares and dies down.{/n}
"Then you have seen," {n}she says.{/n} "I am tired, and I want you to go away. That is what I do." {n}She does not smile.{/n} "It is a stupid game, thief. I invented it. I did not expect anybody to play it back at me."''',
        c("[Take your rock and go.]", flags=(DECLINED,))),
    mz("nothing", '''{n}You stand at the foot of the heap with your hands at your sides and take nothing at all.{/n}
{n}She looks at you, and at your empty hands, and something in her face goes out as the crown goes out when you touch it.{/n}
"Nothing," {n}she says.{/n} "You came into my cave the first time and took nothing, and you left a thing. You come into my cave now and take nothing, and you leave nothing." {n}She pulls her knees up on top of her heap and looks at you over them, and her eyes have gone as dull as the stones.{/n} "Then you are not a thief. You were only a guest. Guests go home. Go home, guest."''',
        c("Continue", "nothing2")),
    mz("nothing2", '''"I will fly you back. I am not rude. And I will keep your ring, because it is in my hoard, and things in my hoard do not leave." {n}She turns the ring on her finger.{/n} "But I will not come to your window again. I have a whole hole in the world to eat, and it will keep me busy for a very long time."''',
        c("[Go home.]", flags=(LEFT_FREE, CLOSED)))],
    requires=("trickster.ever", "trickster.now", FED), forbids=(COMMITTED, DECLINED, CLOSED), delay=48, last=5, Relationship=REL,
    Remote=True, Kind="visit", Chapters=[5], Areas=[DREZEN]))
tag(M + "commit.stone")


# --- 7. Chapter 5 (T): the shared hunt. After the crown, a joint act, not a wait. -------------------------------------------

SCENES.append(scene(M + "hunt.shared", "What is real on this side", "Melazmera", 5, "", [
    nar("start", '''{n}The crown sits on your desk for a day, a grey rock with a flake of mica on one side, and everyone who comes in looks at it and nobody asks.{/n}
{n}On the second night she is on the roof again. She does not put her head down for you to climb. She only looks at you, from the ridge of the keep, with the moon on her plates.{/n}''',
        c("Continue", "invite")),
    mz("invite", '''"I am going hunting," {n}she says.{/n} "At the edge of the hole, where things come up. You can come, and see what is real on your side of the world, or you can stay in your castle with your rock." {n}Her tail moves along the roof, slow and heavy, dislodging a slate that goes spinning down into the yard.{/n}
"I do not ask twice, thief. I have never asked once before. Get on, or go to bed."''',
        c("[Climb up behind her head.]", "wound"),
        c('"Go and hunt. I\'m going to bed."', "bed")),
    mz("bed", '''{n}She looks at you a moment more. Then she launches herself off the keep without a word, and the whole roof shakes with it, and you stand on the leads with the wind of her wings in your hair and watch her go north until she is gone.{/n}
{n}She does not come back to your window. On the last night the pickets on the north road hear her screaming out over the Wound's edge, very far off, at something, and then that stops too.{/n}''',
        c("[Go down into the keep.]", flags=(LEFT_FREE, CLOSED))),
    nar("wound", '''{n}She puts you down on a spur of black rock above one of the rifts, where the ground is warm through your boots and smells of struck flint, and folds herself flat beside you until you could not tell her from the rock at all, except for the two red coals of her eyes.{/n}
"Shadow demon," {n}she says, in a voice pitched too low for anything else to hear.{/n} "It has been coming up out of that crack every night and eating your pickets. It thinks it is hard to see. It is not hard to see, if you know what shadow tastes like." {n}Her eye rolls towards you.{/n} "You do not know what shadow tastes like. So look. Tell me where it is before it knows we are here."''',
        c("[Search the rift's mouth for the thing that should not be there.]",
          check=dict(Skill="SkillPerception", DC=24, Success="spotted", Failure="missed"))),
    nar("spotted", '''{n}It takes you a long time. The rift is all shadow, black on black, steam going up in front of it, and nothing moves. Then something doesn't: a patch of dark on the far lip that stays still when the steam goes past it, a stillness with a shape to it, a man's height, bent, waiting. Hungry. You lift your hand and point.{/n}
{n}She goes off the spur beside you like a thrown spear. The patch of dark sees her in the last heartbeat and tries to be somewhere else, and there is a noise like wet cloth tearing, and a scream that goes up and up and stops. She comes back up the rock with something black and smoking between her teeth, and swallows it, and her eyes are blazing.{/n}''',
        c("Continue", "spotted2")),
    mz("spotted2", '''"You saw it." {n}She is almost purring.{/n} "You, with your little mortal eyes. You looked into a hole full of shadow and you found the one bit of it that was lying." {n}She puts her great head down beside you on the rock until her eye is level with your face.{/n}
"That is what you did in my cave. On Colyphyr. You went into my cave carrying a real thing, and you left it with me." {n}The red light goes soft.{/n}''',
        c("Continue", "challenge", requires=(M + "crown_challenge",), flags=(HUNTED,)),
        c("Continue", "not_tired", forbids=(M + "crown_challenge",), flags=(HUNTED,))),
    mz("challenge", '''"And then you took the crown, to see what I would do. You told me so." {n}Her breath goes over you, warm, smelling of cold iron.{/n} "Well. That was what I do when I am tired. Now you have seen what I do when I am not."''',
        c("Continue", "again")),
    mz("not_tired", '''"And then you took the crown, and I was tired, and I sent you home with a rock." {n}Her breath goes over you, warm, smelling of cold iron.{/n} "I am not tired now. A thief who can find the lie in a hole full of shadow does not take my crown by mistake twice. I am going to give you the chance to show me."''',
        c("Continue", "again")),
    nar("missed", '''{n}You look until your eyes water. The rift is all shadow, black on black, steam going up in front of it, and nothing in it moves, and then everything does at once: something tears loose from the dark on the near lip, not the far one, right below you, and comes up the rock at you faster than anything that size should move.{/n}
{n}She is faster. Her tail comes round in a flat sweep that takes the thing off the rock in mid-leap, and takes you too, the last yard of it, across the back and the shoulder. You go down on the warm stone with the breath gone out of you and your coat laid open, and hear the thing scream in her jaws somewhere above you, and stop.{/n}''',
        c("Continue", "missed2")),
    mz("missed2", '''{n}When you can breathe again she is crouched over you, looking down, with something black still smoking at the corner of her mouth. Your back is wet and hot and does not yet hurt, which means it will.{/n}
"You did not see it," {n}she says.{/n} "It was under your feet the whole time, and you were looking at the far side, because the far side is where you would have hidden." {n}She considers the long bleeding line across your back.{/n} "I hit you. I was aiming at it. You were in the way. You will have a mark there as long as your arm for the rest of your life, and every time somebody asks you about it you will have to say a dragon, and they will think you are lying."
{n}She sounds pleased about that.{/n}''',
        c("Continue", "again", flags=(HUNTED, LASHED))),
    mz("again", '''{n}She flies you to her cave afterwards, not home. She walks up the heap in the woman she wears and sits down on the top of it, and spreads her hands out over it again, palms down, as she did before.{/n}
"Once more," {n}she says.{/n} "I do not do things twice. I am doing this twice. Do not make me sorry, thief." {n}She is very still.{/n} "Take something."''',
        c('[Take one real stone] Climb the heap to her and take one warm grey stone from under her hand.', "stone"),
        c("[Leave the heap alone.]", "leave")),
    nar("stone", '''{n}You climb the heap, and the stones clack and shift under your knees, warm as bread. You put your hand under hers, flat on the stones, and her fingers are cold as a well, and you slide out from under them one grey stone the size of a hen's egg, heavy for its size, and close your hand on it.{/n}
{n}She lets you. Her whole body goes tight as a drawn bow while you do it, and then it lets go, and she laughs, high and shaky, with her face turned up to the roof of the cave.{/n}''',
        c("Continue", "stone2")),
    mz("stone2", '''"That one is a sapphire," {n}she says.{/n} "It came out of the crown of a king of a drowned country, and I have slept on it for two hundred years. You keep it, and I keep you. That is the bargain." {n}Her fingers close on your wrist.{/n} "There is no other bargain. Come back tomorrow night and lie on the heap. I want to see what my hoard looks like with you in it."''',
        c("[Close your hand on the stone.]", flags=(COMMITTED, STONE_KEPT), requires=("trickster.now",)),
        c("[Leave.]", abort=True, forbids=("trickster.now",))),
    mz("leave", '''{n}She looks at you, and at your empty hands, and the light in her eyes goes down to embers.{/n}
"Then you are not a thief," {n}she says.{/n} "You were only a guest. Guests go home." {n}She flies you back without another word, and puts you down on the roof of the keep, and is gone north before you have your feet under you. She does not come to your window again.{/n}''',
        c("[Go down into the keep.]", flags=(LEFT_FREE, CLOSED)))],
    requires=("trickster.ever", "trickster.now", DECLINED), forbids=(COMMITTED, CLOSED), delay=24, last=5, Relationship=REL,
    Remote=True, Kind="visit", Chapters=[5], Areas=[DREZEN]))
tag(M + "hunt.shared")


# --- 8. Chapter 5 (T): the heap. The intimacy, and the morning. ---------------------------------------------------------------

SCENES.append(scene(M + "visit.heap", "On the heap", "Melazmera", 5, "", [
    nar("start", '''{n}She is on the roof at the second bell, as she said, and she flies you north without a word, low over the burned country, and drops into the black split in the ground with her wings half-closed so that your stomach stays somewhere up above the Wound.{/n}
{n}The cave is warm. The red light comes up from the deep of the rift and lies along the ceiling like the underside of a banked fire. At the mouth the false treasure glitters on its shelf. At the back the heap waits, grey and dull, forty stones now, with the hollow in it where she sleeps and a smaller hollow near the top where the sapphire lay for two hundred years.{/n}''',
        c("Continue", "lie")),
    mz("lie", '''{n}She goes up the heap in the woman she wears and turns round at the top and holds out her hand to you, and you climb. The stones shift under your knees. They are warm all the way through, as if something had lain on them for two hundred years, which something has.{/n}
"Lie down," {n}she says.{/n} "Here. In the hollow. I want to see what it looks like."
{n}You lie down in the hollow of a dragon's bed. It is shaped for something very much bigger than you, and the stones fit themselves to your back in a way that is not quite comfortable and not quite not. She stands over you with the rift's light behind her, and looks, with her head on one side.{/n}
"Yes," {n}she says, very softly.{/n} "That is better. That is much better than a ring."''',
        c("Continue", "her")),
    mz("her", '''{n}The woman she wears is tall and dark and wears a rock for a crown, and she comes down onto the heap on her knees beside your hip and puts one hand flat on your chest, and watches your breath lift it. She is smiling. It is not a nice smile, and it is not meant to be.{/n}
"I have eaten everything that ever stayed in my reach," {n}she says.{/n} "Everything. It stays, and I eat it. That is what reach is for." {n}Her fingers spread over your heart.{/n} "You keep staying."''',
        c("[Touch her throat.]", "throat"),
        c("[Take her hand and put the sapphire in it.]", "sapphire")),
    nar("throat", '''{n}You put your hand up to her throat, and the woman slips where you touch her. It is skin under your fingers, warm, with a pulse going in it, and then it is scale, cold and smooth and hard as a church bell, a patch of purple-black plate the size of your palm, and then as you move your hand it is skin again, as if you had put your fingers through the surface of a pool and found the bottom.{/n}
{n}She lets you. She holds very still and lets you, the way she held still on the heap when you took the stone, and her eyes half close.{/n}''',
        c("Continue", "throat_grey", requires=(GREY_HAND,)),
        c("Continue", "threshold", forbids=(GREY_HAND,))),
    mz("throat_grey", '''"Not that hand." {n}She catches your wrist, the ring hand, and turns it over, and looks at the two grey fingers she made.{/n} "You cannot feel me with those. I took the feeling out of them myself; I know exactly where it went."
{n}Then she puts them to her mouth anyway, one and then the other, and you cannot feel it, and you watch her do it, and that is worse, and better.{/n} "There," {n}she says.{/n} "Now they have had something."''',
        c("Continue", "threshold")),
    mz("sapphire", '''{n}You take the grey stone out of your shirt, where it has been since she let you take it, and put it into her palm and close her fingers on it.{/n}
{n}She looks at her closed hand. Then she opens it and looks at the stone, lumpy and grey and warm from your body, and something goes over her face that you have never seen on it, and that she does not know what to do with.{/n}
"It is warm," {n}she says.{/n} "It was never warm from anything but me." {n}She puts it back into your shirt, very carefully, and pats it flat over your heart.{/n} "Keep it. That is the bargain. Do not ever give me back anything, thief. I will not know what to do and I will eat something."''',
        c("Continue", "threshold")),
    nar("threshold", '''{n}She bends down and kisses you the way she eats, as though she has been hungry for a very long time and does not care who knows it. Her teeth find the corner of your jaw, and then your throat, and then your shoulder, through the shirt, not gently, hard enough that you will find the marks of every one of them in the morning, too many and too even.{/n}
{n}With claws that are fingers again she has your shirt open and then off, over your head, and flung somewhere down the heap among the rubies. Her gown does not come off. It goes out, like a snuffed candle, all at once, and what is under it is a woman, long and dark and bare, with a sheen of purple along her flanks where the plates of her show through like the grain in a board, and her skin hot under your hands everywhere except where it is suddenly cold.{/n}''',
        c("Continue", "harpoon", requires=(HARPOONED,)),
        c("Continue", "cut", forbids=(HARPOONED,))),
    nar("harpoon", '''{n}Under her ribs on the left side there is a welt the length of your forearm, pink and raised and newer than the rest of her. She sees you find it.{/n}
"Your captain," {n}she says against your mouth.{/n} "Touch it. I want you to know I let you."''',
        c("Continue", "cut")),
    nar("cut", '''{n}She pushes you back down into the stones with one hand flat on your chest, and her hair comes down round your face like a tent, with the rock still in it, knocking against your brow. Behind her, all along the roof of the cave, her shadow spreads its wings.{/n}
{n}She is heavy and hot and bare against you, and she does not hold herself still. She makes a small greedy sound in her throat, the sound she makes at a good kill, and where the cold plate runs under the skin of her belly it chills you and the heat of her swallows the chill. She laughs, the giggle, low and delighted. She puts her mouth at your ear and her teeth in the lobe and bites, not hard enough to cut, just hard enough to count.{/n}
"Mine," {n}she says. Her other hand is already at your belt, pulling it open.{/n} "Say it, thief."''',
        c('"Yours."', M + "visit.heap.explicit.1"),
        c("[Pull her down to you.]", M + "visit.heap.explicit.1")),
    nar("morning", '''{n}The light from the rift goes from red to grey when the sun comes up over the Wound, as if the fire down there were going to sleep. You wake in the hollow of the heap with a ruby pressing into your spine and every other stone in the place printed on your back, and a warm, enormous flank against your side that rises and falls like the sea.{/n}
{n}She has taken off the woman in her sleep. She is curled round the whole heap in her own shape, with you in the middle of it, and her head on her forefeet, and your seal on her claw by your hand, glittering. One scarlet eye is open, watching you, and has been for some time.{/n}''',
        c("Continue", "count")),
    mz("count", '''"Forty on the heap," {n}she says, without lifting her head. Her voice comes up through the stones and through your back.{/n} "One in your pocket, and you are mine, so that is forty-one. And one seal. And one Commander." {n}The eye closes and opens again.{/n} "I counted you twice in the night. You were still there both times. I thought you would go."
"Your war is going to eat you. I can smell it on you: the fly, and the hole, and whatever is at the bottom of it." {n}Her breath goes over you, warm, smelling of cold iron.{/n} "I do not fight in anybody's war. I do not stand in lines. But if your war eats you, thief, I will come and find what is left and bring it here and put it on the heap anyway. Things in my hoard do not leave. Not even for that."''',
        c('"Then I\'d better come back in one piece."', "go"),
        c("[Lie still until she sleeps again.]", "stay")),
    mz("stay", '''{n}You lie still. It takes a long time. The eye watches you, and watches you, and then very slowly it closes, and the great flank against you settles, and her breathing goes long and deep and slow as a bellows in a forge that has been banked for the night.{/n}
{n}You stay until the rift has gone grey all the way down. When you finally climb out of the hollow she opens the eye again, and does not say anything, and does not need to.{/n}''',
        c("Continue", "home", flags=(MORNING_STAYED,))),
    mz("go", '''"In one piece," {n}she agrees.{/n} "I do not want the pieces. I want the whole thing, with the talking still in it." {n}She lifts her head at last, and yawns, and it is like looking into a furnace full of knives.{/n} "Get on. I will take you back before your castle notices you are gone. Your castle notices everything. It is the most frightened building I have ever seen."''',
        c("Continue", "home")),
    nar("home", '''{n}She puts you down on the roof of the keep with the sun barely up. Before you can go, she hooks your belt round your waist and pulls you back against her. "You left this. I am keeping the seal. Take your belt." She bites your shoulder through the shirt, then lets go. You go down the stairs with your shirt on inside out and a stone in the pocket of it, a lumpy grey stone the size of a hen's egg, warm from lying against you all night, and it stays warm all morning, long after it should have cooled.{/n}
{n}There is another stone on your windowsill when you get there, small and round, the clay on its corner still wet, the old seal pressed into it very carefully and very straight: FORTY ON THE HEAP. ONE IN YOUR POCKET. ONE SEAL. ONE COMMANDER. I HAVE MY SEAL. YOU HAVE YOUR BELT. DO NOT LOSE MY STONE.{/n}''',
        c("Continue", "dogs", requires=(GREY_ABSENT,)),
        c("[Go about your day.]", flags=(HEAP,), forbids=(GREY_ABSENT,))),
    nar("dogs", '''{n}When you cross the stable yard, every dog in it gets up and goes somewhere else. The old wolfhound that sleeps by the forge, who has never moved for anyone, crawls under the feed trough on his belly and will not come out, and whines, and the grooms look from him to you and back again and say nothing at all.{/n}''',
        c("[Go about your day.]", flags=(HEAP,)))],
    requires=("trickster.ever", COMMITTED), forbids=(HEAP, CLOSED), delay=24, last=5, Relationship=REL, Remote=True,
    Kind="visit", Chapters=[5], Areas=[DREZEN]))
tag(M + "visit.heap")
# Intimacy insert: her chosen predatory first night on her own hoard; preserve belt and morning continuity.
SCENES[-1]["Nodes"].append(nar(M + "visit.heap.explicit.1",
    "{n}She catches your belt before it slides down the heap. Your answer draws her close; her teeth brush your jaw, and the shadow of her wings covers the stones. The heap shifts and clatters beneath you, a ruby skitters away down the slope, and she takes you the way she takes everything that stays within her reach: greedily, noisily, with her teeth, and without once letting go.{/n}",
    c("Continue", "morning")))


# --- 9. Reactions (named companions with a stake: Greybor, who would not take the contract on her and then carried her
# stone; Nenio, who keeps specimens, and has met a predator that keeps her own).

GREY_GUARD = dict(forbids=GREY_GONE)

SCENES.append(reaction("Greybor", M + "react.greybor_colyphyr", ("trickster.ever", RETURNED, GREY_IN, GREY_DECLINED),
    '''{n}Greybor draws a whetstone along his axe.{/n} "I declined the swamp queen's contract. I still doubt she would pay. Then you left your ring in the dragon's cave, and she came looking for you."

{n}He tests the edge with his thumb.{/n} "If you wanted her attention, you got it. I charge more for clients who have a dragon following them."''',
    answer_list=GREYBOR_LIST, relationship=REL, chapter=4, last=4, Chapters=[4], entry='"What do you make of the dragon following me?"',
    portrait="Greybor", **GREY_GUARD))
tag(M + "react.greybor_colyphyr")

SCENES.append(reaction("Greybor", M + "react.greybor_after", ("trickster.ever", HEAP, GREY_IN),
    '''{n}Greybor sniffs as you come in, once, the way a dog does at a gate, and puts down his whetstone.{/n}
"You came back smelling of her lair, Commander. Hot stone and cold iron. I know that smell. I have been in caves with worse things in them, though not many, and I did not come out of any of them smiling." {n}He looks at you with no expression at all.{/n}
"She came to the gate last night with a stone for you and a coin for me. The coin was good. I sent her away with both." {n}He takes up the whetstone.{/n} "The watch can hang for letting a dragon through after curfew. I won't put my name in that book. Keep her out of my contracts, Commander."''',
    answer_list=GREYBOR_LIST, relationship=REL, chapter=5, last=5, Chapters=[5], entry='"Something on your mind, Greybor?"',
    portrait="Greybor", flags=(GREY_WARY,), **GREY_GUARD))
tag(M + "react.greybor_after")

SCENES.append(reaction("Nenio", M + "react.nenio_specimen", ("trickster.ever", FED),
    '''{n}Nenio is standing at her window with a spyglass to her eye, pointed north at the Wound, and a folio open on the sill with a great many crossings-out in it.{/n}
"An umbral dragon," {n}she says, without turning round.{/n} "In the city. Wearing a woman. For hours. Do you know what that costs? Illusions do not eat, as a rule. Hers ate the measuring rope I left on your windowsill; I found the knot on the roof." {n}She lowers the spyglass.{/n}
"I have catalogued a great many specimens. She is the first that has catalogued me back: she looked at me over your wall for some time, and I am fairly sure she was estimating my weight." {n}Her ears go up.{/n}
"So. An experiment. You will hold the end of a new rope, and I will hold the other end from the far side of the yard, and when she next wears the woman you will put your end round her waist. Distance is the control. You are the variable. Please do not be eaten before I have recorded the circumference."''',
    answer_list=NENIO_HUB, relationship=REL, chapter=5, last=5, Chapters=[5], entry='"You\'re watching the Wound."',
    portrait="Nenio", forbids=NENIO_GUARD,
    ForbidOverrides={"nenio.dead": NENIO_BACK, "nenio.killed_by_commander": NENIO_BACK, "nenio.sent_away": NENIO_BACK,
                     "nenio.kicked_out": NENIO_BACK}))
tag(M + "react.nenio_specimen")


# --- 10. Epilogue pages (Owner MelazmeraEpilogue, Chapter 6; no effects, no page Requires another). -------------------------

EP = dict(last=6, Relationship=REL)
SAC = dict(ForbidOverrides={"sacrifice": "trickster.commander_back"})   # H2 (Last Call's bottle) as well as the native endings
COMMON = (
    # Before round two, FED_HERD was produced only by the successful -50 payment.
    p("{n}A Mendevian lord was paid for his cattle out of the crusade's own chest, eventually, and grudgingly, and never found out where they had gone. His drovers' dogs never went north of the Drezen road again.{/n}", requires=(FED_HERD,), forbids=(HERD_INCURRED,)),
    p("{n}The inquisitor's report named the Commander as the one who gave seven prisoners to Melazmera. The acolyte carried the confession with the measurements of the untouched locks.{/n}", requires=(M + "beat.inquisitor_admitted",)),
    p("{n}The inquisitor sent the measurements and the Commander's refusal to answer up the chain. A second copy stayed in the chapter room. The seven names remained in it.{/n}", requires=(M + "beat.inquisitor_refused",)),
    p("{n}Compensation kept the cattle owner's spears in the crusade. The owner's letter named Melazmera. No more cattle came near Drezen until the war ended.{/n}", requires=(HERD_SETTLED, HERD_HONEST)),
    p("{n}Forty cattle remained missing from the Mendevian lord's stores. The demand for compensation stayed on the war council's table, unanswered.{/n}", requires=(HERD_INCURRED,), forbids=(HERD_SETTLED,)),
    p("{n}The Knight Commander's orders went out under a new seal. Melazmera kept the old one on her claw. She had taken it on Colyphyr, and she did not give it back.{/n}", requires=(SEAL,)),
    p("{n}Two fingers of the Commander's ring hand stayed grey to the second knuckle for the rest of a long life, cold in summer and colder in winter, and never felt anything again. Healers looked at them and went away. The Commander said they had been tasted, and let people decide whether that was a joke.{/n}", requires=(GREY_HAND,)),
    p("{n}Across the Commander's back, from the shoulder nearly to the hip, ran a long pale scar, and when anyone asked, the Commander told them it was a dragon's tail, and they thought it was a lie, which pleased Melazmera very much.{/n}", requires=(LASHED,)),
    p("{n}In the cellars under the citadel of Drezen, the gaoler's book still says that seven of Deskari's faithful escaped one night in the war. The cellar was cold for a week afterwards. Nobody who works there goes down alone.{/n}", requires=(FED_CULTISTS,)),
    p("{n}A Mendevian lord was paid for his cattle out of the crusade's own chest, eventually, and grudgingly, and never found out where they had gone. His drovers' dogs never went north of the Drezen road again.{/n}", requires=(HERD_SETTLED, HERD_HIDDEN)),
    p("{n}In the archive of the Inquisition there is a report from Drezen, in a careful hand, about seven prisoners of the Knight Commander's who were moved to a place the Knight Commander would not name, and a cold in a cellar that would not come out of the stones. It was sent up the chain in the last year of the war. Nobody ever closed it.{/n}", requires=(M + "beat.inquisitor_lied",)),
    p("{n}An inquisitor of Iomedae went down into the cellars under the citadel one morning in the war with a lamp, and did not come up. His acolyte left the order within the year, and would never say why, and would never go below ground again.{/n}", requires=(M + "cost.inquisitor",)),
    p("{n}The gold Melazmera paid the dead sailors' kin went round the Alushinyrra quay as gold for a night and as rocks by morning. The sack had the Commander's old seal in its clay. The debt stood in the Commander's name, and the kin did not forget whose name it was. Melazmera kept a rock from the heap, and told the joke whenever she had company: \"You said pay them. You did not say in what.\"{/n}", requires=(M + "beat.crew_debt_stands",)),
    p("{n}The dead sailors' kin on the Alushinyrra quay were paid twice: once in rocks that had been gold for a night, and once, from the crusade chest, in true gold. Melazmera thought the second payment was the best part. She had paid nobody, and the Commander had paid for all of it.{/n}", requires=(M + "beat.crew_debt_settled",)),
    p("{n}The gold Melazmera carried to the dead sailors' kin on the Alushinyrra quay was weighed out in their own hands. They knew whose gold it was. They had refused to let her land.{/n}", requires=(M + "beat.crew_paid",), forbids=(M + "beat.crew_illusion_gold",)),
    p("{n}During the war, the harpoon captain told the story in the Midnight Isles. Once, a dragon settled above the drinking-house and listened. A stone bearing the Commander's answer reached the roof. Melazmera left the captain alive and took his harpoon off the wall. The shutters stayed closed until she flew back through the Wound.{/n}", requires=(M + "beat.captain_spared",)),
    p("{n}On Colyphyr, the Fulsome Queen wore a grey rock on her head and called it the Knight Commander's crown. When it slipped into her pool, she sent her knights in after it. They came out stinking, and she made them bow.{/n}", requires=(M + "queen_crowned",), forbids=("melazmera.fq_betrayed", "melazmera.queen_fought")),
)

SCENES.append(scene(M + "epilogue.together", "", "MelazmeraEpilogue", 6, "", [
    nar("page", '''{n}Melazmera kept her cave at the edge of the Wound after the war. She liked the country. Nothing grew there, and she could see anyone coming for a day in any direction, and eat them if she chose.{/n}
{n}Her heap stayed forty stones, and the forty-first went about in the Commander's pocket, and the seal stayed on her claw, and the false treasure glittered at the mouth of the cave for any thief who wanted it. A great many thieves came, because the story went round. None of them ever came back. Every so often one of them was a crusader who had heard that the Knight Commander was in the habit of visiting, and thought the dragon might be soft. She was not.{/n}
{n}The Commander visited when the Commander chose, and lay in the hollow of the heap, and was counted. She never once asked the Commander to stay, and she never once let the Commander leave without saying where the stone was. It was always in the same pocket.{/n}''',
        paragraphs=(p("{n}When the Wound closed, the rifts went cold and her easy hunting ended. She complained for a year, then began flying north to hunt in the cold country. She always came back to the heap. On the nights the Commander waited there, she folded down beside the hollow, blood still at her mouth, and demanded to see the sapphire before pulling the thief against her.{/n}", requires=("ending.wound_closed",)),
                    p("{n}The Wound did not close. The rifts along the northern edge stayed open, and things went on coming up out of them warm, and she went on eating them, and the pickets on the north road learned to sleep through the screaming.{/n}", forbids=("ending.wound_closed",)),
                    *COMMON,
                    p("{n}The grey stone the size of a hen's egg lived in the Commander's pocket for the rest of the Commander's life. It was a sapphire from the crown of a drowned king, and it never once looked like anything but a boring rock, and it was never once cold.{/n}", requires=(STONE_KEPT,)),
                    p("{n}Greybor kept refusing Melazmera's coin. She kept offering it. He told the watch to stop sending her to him. She asked for him by name the next time.{/n}", requires=(GREY_WARY,)),
                    p("{n}On the morning the Commander rode out to the last battle, there was a flat grey stone on the windowsill with four words scored into it: ONE PIECE. I COUNT.{/n}", requires=(M + "stone.shirt",)),
                    p("{n}She wore a worn copper coin on a thread round the woman's neck, the kind that buys half a loaf, and when she was angry she bit it. She never said where it came from. A beggar by the well in the lower town of Drezen could have told, and slept badly for a year, and then very well for the rest of her life.{/n}", requires=(M + "beat.copper_kept",)),
                    p("{n}She never learned to share her hoard, and she never pretended to. What was hers was hers, and she said so, often, to anyone standing near the Commander.{/n}")))],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, DEAD, "sacrifice"), **SAC, **EP))
tag(M + "epilogue.together")

SCENES.append(scene(M + "epilogue.commit", "", "MelazmeraEpilogue", 6, "", [
    nar("page", '''{n}The war ended before Melazmera had finished deciding what the Commander was. She had never needed a long time to decide anything; things were food, or they were in her way, or they were hers. The Commander had been all three, in turn, and she found it very tiring.{/n}
{n}In the spring after the war a flat grey stone came through the Commander's window with the old seal pressed into a smear of clay on its corner, and three words scored into its face: COME AND LOOK.{/n}
{n}What the Commander took from the heap, when the Commander went, and what she let the Commander take, belongs to the years after the war. The false treasure still glittered at the mouth of her cave, and the thieves still came for it, and she still ate them. That did not change. She said it never would.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", RETURNED), forbids=(COMMITTED, DECLINED, LEFT_FREE, CLOSED, DEAD, "sacrifice"), **SAC, **EP))
tag(M + "epilogue.commit")

SCENES.append(scene(M + "epilogue.declined", "", "MelazmeraEpilogue", 6, "", [
    nar("page", '''{n}The little crown sat on the Commander's desk to the end of the war: a grey rock with a flake of mica on one side, that everyone who came into the room looked at and nobody asked about. The Commander never threw it away.{/n}
{n}Melazmera hunted the edge of the Wound after the war, and she did not come to the Commander's window. Once, years later, a traveller on the north road said he had seen a dragon lying on a heap of rocks in a crack in the ground, counting them aloud, and that she had stopped at forty-two and started again from the beginning, as if the number would not come out right.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, LEFT_FREE, CLOSED, DEAD, "sacrifice"), **SAC, **EP))
tag(M + "epilogue.declined")

SCENES.append(scene(M + "epilogue.left_free", "", "MelazmeraEpilogue", 6, "", [
    nar("page", '''{n}Melazmera ate the Wound. That is how the soldiers told it afterwards, and it was nearly true: for the rest of the war nothing that came up out of the rifts on the northern edge got further than a mile before something very large came down on it out of the dark. The pickets called her the Night Tax. Nobody knew her name.{/n}
{n}She kept the seal. It was on her claw, as long as anyone saw her, glittering.{/n}''',
        paragraphs=(p("{n}When the Wound closed, she went back through the last of it before it shut, and the Midnight Isles had their dragon again. Somewhere on Colyphyr, in a cave with a hole in its roof, the rain fell on a heap of real stones and one seal, and she lay on them and did not come out for a very long time.{/n}", requires=("ending.wound_closed",)),
                    p("{n}The Wound stayed open, and she stayed on its edge, and for years after the war the Night Tax was paid every night by whatever came up out of the ground, and nobody on the north road ever complained of it.{/n}", forbids=("ending.wound_closed",)),
                    *COMMON))],
    requires=("trickster.ever", LEFT_FREE), forbids=(COMMITTED, DEAD, "sacrifice"), **SAC, **EP))
tag(M + "epilogue.left_free")

SCENES.append(scene(M + "epilogue.closed", "", "MelazmeraEpilogue", 6, "", [
    nar("page", '''{n}The Commander never saw the dragon of Colyphyr again. Somewhere in the Midnight Isles, in a wet cave with a hole in its roof, thieves went on touching a little crown that was really a rock, and something went on eating them.{/n}
{n}Every order that left the Knight Commander's desk for the rest of the war went out under a new seal. The old one had been a mistake. It was in a heap of real stones that looked like nothing, and it would stay there, as long as there was a dragon to lie on it.{/n}''')],
    requires=("trickster.ever", MISTAKE), forbids=(DEAD, "sacrifice"), **SAC, **EP))
tag(M + "epilogue.closed")

SCENES.append(scene(M + "epilogue.mourned", "", "MelazmeraEpilogue", 6, "", [
    nar("page", '''{n}Word reached Melazmera that the Knight Commander had given everything at the end and had not come back.{/n}
{n}On the fourth night a dragon landed on the roof of Drezen's keep. The whole city lay awake and listened to her walk up and down the leads until dawn, looking for something to count.{/n}''',
        paragraphs=(
            p("{n}The Wound had closed. Her cave was cold; nothing came up from below. She lay on the stones and counted them, then began again.{/n}", requires=("ending.wound_closed",)),
            p("{n}The Wound stayed open. For three nights the pickets heard the things below her cave screaming unhunted. On the fourth, she left for Drezen.{/n}", forbids=("ending.wound_closed",)),
            p("{n}She had said that if the war ate the Commander she would find what was left and put it on the heap anyway. There was nothing left to find. She took the Commander's old boots from the room under the roof instead, and nobody tried to stop her, and they are on the heap still, between a ruby and a lump of star.{/n}", requires=(HEAP,)),
            p("{n}The seal on her claw stayed there. She bit the gold when anyone spoke of the Commander. She did not give it back.{/n}", requires=(SEAL,)),
        ))],
    requires=("trickster.ever", RETURNED, "sacrifice"), forbids=("trickster.commander_back", MISTAKE, DEAD, CLOSED, LEFT_FREE, DECLINED),
    ForbidOverrides={DECLINED: COMMITTED}, **EP))
tag(M + "epilogue.mourned")


# --- Registration ----------------------------------------------------------------------------------------------------------

PORTRAIT_GUID = "ca8d2f8a110149b890d75080e01089a5"   # her unit's m_Portrait (the BlackDragon portrait), until custom art ships


def _bind(payload, kind, table):
    for key, value in table.items():
        want = list(value) if isinstance(value, list) else value
        have = payload.setdefault(kind, {}).get(key)
        if have is not None and have != want:
            raise ValueError("Conflicting binding: " + key)
        payload[kind][key] = want


def integrate(payload):
    """Register her own native reads (the Queen's hoard cues, the lair's lifted illusions, the harpoon, the Chapter 5 latch),
    her Derived keys and her portrait fallback. Scenes are added by expansion.py; the merged world keys (melazmera_dead,
    melazmera.ate_sailors, greybor., hepzamirah.dead, nenio....) bind on demand in trickster_world."""
    payload.setdefault("DerivedForbids", {})[HERD_PENDING] = [HERD_SETTLED]
    _bind(payload, "SeenCues", SEEN_CUES)
    _bind(payload, "SelectedAnswers", SELECTED_ANSWERS)
    _bind(payload, "UnlockableFlags", UNLOCKABLE_FLAGS)
    _bind(payload, "Etudes", ETUDES)
    _bind(payload, "Latches", LATCHES)
    for key, groups in DERIVED.items():
        want = [list(g) for g in groups]
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != want:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = want
    # trickster_world binds a Derived key's sources only when it binds the key itself; these bind here first, so their
    # verified native sources (melazmera.fq_*) are bound here from the same table.
    from storylines import trickster_world
    for key in sorted({k for groups in DERIVED.values() for g in groups for k in g}):
        if key in trickster_world.BINDINGS:
            kind, guid, _ = trickster_world.BINDINGS[key]
            value = [guid] if kind in trickster_world.LIST_KINDS and isinstance(guid, str) else guid
            have = payload.setdefault(kind, {}).get(key)
            if have is not None and have != value:
                raise ValueError("Conflicting binding: " + key)
            payload[kind][key] = value
    payload.setdefault("PortraitFallbacks", {}).setdefault("Melazmera", PORTRAIT_GUID)


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'melazmera.trickster.ch4.hunt',
    'melazmera.trickster.ch4.hunt_found',
    'melazmera.trickster.ch5.hunt_window',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]


# Replacement "owed" paragraphs, one per (scene suffix, voyage). Each is told at the place the meeting happens (the camp on
# Colyphyr, a fire in the open Abyss, the hearth at Drezen) and settles the debt in that room; she promises no later visit.
OWED_TEXT = {
    ("ch4.hunt", 0): """"I ate your sailors, so now I owe you." {n}She giggles.{/n} "That is backwards, thief. Things I eat do not send bills. They are inside me, and they are quiet, and they were salty."
{n}She bends close enough to smell your throat. The sentry on the near rock makes a small noise, like a kettle taken off the boil too late.{/n} "You left a ring in my cave and now you sit at your own fire and want to be paid for men I have already finished. Then collect. I am close enough. Name what you want, here, while I am still curious, because when I stop being curious I am only hungry." {n}She waits, and does not blink.{/n}""",
    ("ch4.hunt", 1): """"Even." {n}Her hand goes to her side, where for a heartbeat the gown is torn purple plate.{/n} "Your captain put a hook in me and turned me over in the air in front of my whole island, and you want to call that even with one ring. Nothing is even with me, thief. Things are mine, or they are eaten."
{n}She bends close enough to smell your throat.{/n} "A fresh start. Good. Here is how I start: I sit at your fire, and I eat your pork, and I decide which of you I would swallow first, you or the man with the harpoon. Be quiet a moment. I am deciding." {n}She looks at you, then past you, towards the ships and the men that are not here, for a long time.{/n}""",
    ("ch4.hunt", 2): """"A first gift." {n}She looks delighted and insulted at once.{/n} "You made me go home hungry and you call it a present. A meal that gets away is not a gift, thief. It is a debt, and it is a whole ship's worth of supper."
{n}She bends close enough to smell your throat.{/n} "So I am going to sit at your fire and be hungry at you until I have had my share of looking. That is the interest. Pour me something. No, not that. The thing you are pretending is not in your pockets." {n}She holds out her palm.{/n}""",
    ("ch4.hunt_found", 0): """"I ate your sailors, so now I owe you." {n}She giggles.{/n} "That is backwards, thief. Things I eat do not send bills. They are inside me, and they are quiet, and they were salty."
{n}She bends close enough to smell your throat. Somewhere out in the red dark a demon starts to scream and is cut off, abruptly, by its own good sense.{/n} "You left a ring in my cave and then you let a whole sea of the Abyss lie between us and thought it would do for a wall. Collect, if you want to collect. I am here, and I am close, and nothing in this place is going to tell me no. Name your price." {n}She waits, and does not blink.{/n}""",
    ("ch4.hunt_found", 1): """"Even." {n}Her hand goes to her side, where for a heartbeat the gown is torn purple plate.{/n} "Your captain put a hook in me and turned me over in the air in front of my whole island, and you want to call that even with one ring. Nothing is even with me, thief. Things are mine, or they are eaten."
{n}She bends close enough to smell your throat.{/n} "A fresh start. Good. Here is how I start: I sit at this fire you did not build properly, and I decide which of you I would swallow first, you or the man with the harpoon. Be quiet. I am deciding." {n}She looks past you, out into the dark where the sky has gone the colour of a wound, for a long time.{/n}""",
    ("ch4.hunt_found", 2): """"A first gift." {n}She looks delighted and insulted at once.{/n} "You made me go home hungry and you call it a present. A meal that gets away is not a gift, thief. It is a debt, and it is a whole ship's worth of supper."
{n}She bends close enough to smell your throat.{/n} "So I am going to sit here at the edge of the world and be hungry at you until I have had my share of looking. That is the interest. Empty your pockets on the ground. I will not take anything. I want to see what you carry when you think it might be eaten." {n}She holds out her palm.{/n}""",
    ("ch5.hunt_window", 0): """"I ate your sailors, so now I owe you." {n}She giggles.{/n} "That is backwards, thief. Things I eat do not send bills. They are inside me, and they are quiet, and they were salty."
{n}She bends close enough to smell your throat. Out on the wall a sentry's boots stop, and start again, faster.{/n} "You left a ring in my cave and then you ran home to a room with a shutter and a latch and a whole castle of men, and sat in it, and wanted to be paid for men I have already finished. I am in the room. Collect. Name what you want while I am curious, because when I stop being curious I am only hungry." {n}She waits, and does not blink.{/n}""",
    ("ch5.hunt_window", 1): """"Even." {n}Her hand goes to her side, where for a heartbeat the gown is torn purple plate.{/n} "Your captain put a hook in me and turned me over in the air in front of my whole island, and you want to call that even with one ring. Nothing is even with me, thief. Things are mine, or they are eaten."
{n}She bends close enough to smell your throat.{/n} "A fresh start. Good. Here is how I start: I sit on your hearth, and I eat your supper, and I decide which of you I would swallow first, you or the man with the harpoon. Be quiet a moment. I am deciding." {n}She looks at you, then at the window, then at the dark it opens on, for a long time.{/n}""",
    ("ch5.hunt_window", 2): """"A first gift." {n}She looks delighted and insulted at once.{/n} "You made me go home hungry and you call it a present. A meal that gets away is not a gift, thief. It is a debt, and it is a whole ship's worth of supper."
{n}She bends close enough to smell your throat.{/n} "So I am going to sit in your little stone room and be hungry at you until I have had my share of looking. That is the interest. Open your desk. I will not take anything. I want to see what you keep when you think it might be eaten." {n}She holds out her palm.{/n}""",
}
COUNT_TEXT = """"You told me I owed you for the sailors." {n}She giggles.{/n} "You said it to my face, with your own ring on my finger. Now you are in my hoard with them. Collect from in here.\""""

def integrate_meeting_history(payload):
    """Retain old paragraphs, but retire unselected venue/future-visit claims.

    Called after the cloud voice pass so it cannot overwrite history selection.
    Replacement prose belongs to Claude; voyage predicates remain unchanged.
    """
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    for suffix in ("ch4.hunt", "ch4.hunt_found", "ch5.hunt_window"):
        event = scenes[M + suffix]
        page = next(n for n in event["Nodes"] if n["Id"] == "owed")
        old = page["Paragraphs"][:3]
        for index, paragraph in enumerate(old):
            replacement = dict(paragraph)
            replacement["Text"] = OWED_TEXT[(suffix, index)]
            replacement["Requires"] = list(paragraph["Requires"])
            replacement["Forbids"] = list(paragraph["Forbids"])
            # All meeting scenes require trickster.ever; keep the old surface
            # address and prose while making the inaccurate copy unreachable.
            paragraph["Forbids"] = [*paragraph["Forbids"], "trickster.ever"]
            page["Paragraphs"].append(replacement)
    page = next(n for n in scenes[M + "commit.stone"]["Nodes"] if n["Id"] == "count")
    paragraph = page["Paragraphs"][1]
    replacement = dict(paragraph)
    replacement["Text"] = COUNT_TEXT
    replacement["Requires"] = list(paragraph["Requires"])
    replacement["Forbids"] = list(paragraph["Forbids"])
    paragraph["Forbids"] = [*paragraph["Forbids"], "trickster.ever"]
    page["Paragraphs"].append(replacement)

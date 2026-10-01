"""Hepzamirah on the Trickster path: "Who said a trick is less impressive the second time?"
(Writer/handoffs/trickster/hepzamirah.md; family F06, "Steal the rule, rename the thing").

Canon: Baphomet's nephilim daughter and the archpriestess of his cult (Hepzamirah_main/Cue_0012 95a274da), who "sacrificed
my own mother to him, then did so with hundreds of my brothers and sisters" (Prison_HepzamirahGhost/Cue_0013 f99fcbc6).
She dies in the mines of Colyphyr (Prison_Baph/Cue_0016 96ae71e9) and her soul is bound in her father's prison by his rule
for nephilim (Prison_HepzamirahGhost/Cue_0011 c1c8de12), hounded by the jailers who once grovelled to her (Cue_0012
ac4fdb1e). Her traitor alchemist Mutasafen boasts that "the revival system I created for myself is flawless" and calls her
"princess" (Mutasafen_Letter b3f92e1e); his Apprentice is a canon cambion (MutasafenAssistent cdece553).

F06 root: Alderpash/Answer_0115 1e33632e, "Who said a trick is less impressive the second time around? I steal this cell
and hereby name it the Leavable Prison" (-> Cue_0118 99c33b3b). The Commander steals her corner of the prison the same
way, and later renames the body Mutasafen grows her, so that its maker keeps no key to it. The whole courtship after her
return is hepzamirah_flesh; this module holds the device, the deal, the courier, the terms and the pages.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
REL = "hepzamirah"
P = "hepzamirah.trickster."
GHOST_UNIT = "78549b805f0a63e41805cfe3e02e2ea8"    # HepzamirahGhost (Neutrals; hidden, never killed, by Cue_0016)
BODY_UNIT = "bd2a925967b5f5f489f6da0b03236d03"     # Hepzamirah, Colyphir (Neutrals, no dialog component; the presence copy)
LABYRINTH = "3538511f16d45f44f8249ff710777e2d"     # TheIvoryLabyrinth
DREZEN = "2570015799edf594daf2f076f2f975d8"        # DrezenCapital
SMITH = "15f754455d1d87c42a4e14df456d5415"         # BlacksmithCapitalTrader, the forge by the gate (E12b anchor)
GHOST_LIST = "f457c8326a05b674c83a1c836636f99d"    # Prison_HepzamirahGhost/AnswersList_0004 (not ShowOnce, unconditioned)
GHOST_RETURN = "001f33d929abf1440945839ace51891a"  # Prison_HepzamirahGhost/Cue_0002 "Have you come to mock me?"
DISSIPATE = "a4011b00473994b4dadc6aed381cf504"     # Prison_HepzamirahGhost/Cue_0016 (HideUnit only)
COLY_LIST = "995aaa29e772b594a966a2f133be702c"     # Hepzamirah_main/AnswersList_0002 (Colyphyr, before the fight)
COLY_RETURN = "b03aa7395540e8040a55a62309caaa1a"   # Hepzamirah_main/Cue_0013 "If you want the winged fool, come and get him!"
EMBER_LIST = "f2a35965e9bc601449498bd022b04d9d"    # Companions/Ember/AnswersList_0003
GREYBOR_LIST = "174d6c94b6725f44aad1d2a76993a926"  # Companions/Grimbor/AnswersList_0002

STARTED = "hepzamirah.started"
CLOSED = "hepzamirah.closed"
COMMITTED = "hepzamirah.committed"
DEAD = "hepzamirah.dead"
DISPERSED = "hepzamirah.ghost_dispersed"
LEAVABLE = "alderpash.leavable"
LETTER = "hepzamirah.mutasafen_letter"
SECRET = "hepzamirah.mutasafen_secret"
BOASTED = "baphomet.boasted_souls"
CANARY = "horzalah.gift_delivered"
PRIMED = P + "primed"
RET = P + "returned"
CS = P + "courier_seen"
OFFER = P + "colyphyr_offer"
GRUDGE = P + "cost.baphomet_grudge"
LATE = P + "cost.late"
WRONG_BODY = P + "cost.wrong_body"
BLOOD = P + "cost.blood_sample"
LAB = P + "cost.lab_funded"
MGRUDGE = P + "cost.mutasafen_grudge"
VIAL_PAID = P + "cost.vial_paid"
COURIER_KILLED = P + "cost.courier_killed"
VIAL_FORGED = P + "cost.vial_forged"
LANDLORD = P + "landlord"
ALTAR = P + "cost.altar"
SCAR = P + "cost.horned_scar"                          # the horned mark cut into the Commander's arm (deed_by_fire)
PICK_ITEM = "3b8021631cd1b7d4eb749601047a7bda"       # DreadfulOnslaughtItem, her +5 unholy heavy pick (Colyphyr loot)
PICK_HELD = "hepzamirah.pick_held"
DECLINED = P + "declined"
PRESENCE = "hepzamirah.presence"
PRESENCE_GHOST = "hepzamirah.presence.ghost"
PRESENCE_FAILED = PRESENCE + ".failed"

# The courtship beats (hepzamirah_flesh) that the terms read. Scene ids are completion flags.
FIRST = P + "flesh.first_morning"
PICK = P + "flesh.the_pick"
ARMED = P + "armed"
YIELDED = P + "sparred_yielded"
BESTED = P + "sparred_bested"
EMBASSY = P + "embassy"
CONFINED = P + "cost.confined"
RELEASED = P + "flesh.released"   # Q8 (Sol INT): her three nights in the cells end here; yard beats wait for it
LOOKED = P + "looked"
LOOKED_AWAY = P + "looked_away"
RENT_TAKEN = P + "rent_taken"
RENT_REFUSED = P + "rent_refused"
BLOODLINE_KEPT = P + "bloodline_spared"
COWED = P + "chaplains_cowed"
HORN_CUT = P + "horn_cut"
HORN_KEPT = P + "horn_kept"
FLOWERS_KEPT = P + "flowers_kept"
MORNING = P + "bond.morning"
KNOWN = P + "cost.known"
CALL_SWORN = P + "call_sworn"
CALL_FORBIDDEN = P + "call_forbidden"
LET_GO = P + "let_go"
FOLLOWED = P + "cost.followed"
EYE_KEPT = P + "eye_kept"
EYE_BURNED = P + "eye_burned"
EVE_PROMISE = P + "eve_promise"
FAVOUR_OWED = P + "cost.favour_owed"

EMBER_FORBIDS = ("ember_dead", "ember_gone", "ember.killed_in_kenabres")

RELATIONSHIP = dict(
    Title="The Leavable daughter",
    Description=("Baphomet's daughter walked out of her father's prison behind me, through a wall I stole and renamed. "
                 "She has not thanked me, and she says she never will."),
    Objective="Hear Hepzamirah's terms",
    Guidance=("On the Trickster path, in the Ivory Labyrinth, find Hepzamirah's ghost in her corridor and steal her corner of "
              "her father's prison the way you stole Alderpash's cell. Then find her a body, and visit her by the forge in "
              "Drezen. Leave a day or two between visits."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED, UnavailableFlags=[], FailureFlags=[],
    UnavailableOverrides={},
    TricksterAccess={"ghost": dict(detect=[DEAD], device=P + "ghost.body", returned=RET)},
)

PRESENCES = {
    # The ghost is only hidden by Cue_0016 (HideUnit), so reuse-native unhides her for the late fallback; her placed map
    # object keeps its native dialog, whose list 0004 hosts the entry.
    PRESENCE_GHOST: dict(Unit=GHOST_UNIT, Area=LABYRINTH, Mode="reuse-native", Requires=["trickster", DISPERSED],
                         Forbids=[PRIMED, CLOSED], MinChapter=5, MaxChapter=5, AnswerLists=[GHOST_LIST]),
    # Her Colyphyr unit has no dialog component: a copy stands in the smith's yard by the gate, where she can hear the
    # forge, and Dialog "hub" makes it talkable (E12c). If the smith is absent the anchor fails, the failure is raised
    # and the epilogue page carries the commit (no letter twin: the Chapter 5 letter cap).
    PRESENCE: dict(Unit=BODY_UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=SMITH, Side="right", Distance=2.5),
                   Requires=["trickster.ever", RET], Forbids=[CLOSED], MinChapter=5, MaxChapter=5, AnswerLists=[],
                   Dialog="hub",
                   Greeting="{n}Hepzamirah has taken the corner of the smith's yard where the heat of the forge is worst. "
                            "She does not turn her head. The milk-white eye is on your side.{/n} \"Clown.\""),
}
DERIVED = {P + "late_committed": [["trickster.ever", CS]]}
RENAMED = {"hepzamirah.complete": COMMITTED, "hepzamirah.visit.fathers_hounds": P + "body.hounds",
           "hepzamirah.visit.what_she_wants": P + "body.terms", "hepzamirah.epilogue.leavable": P + "epilogue.leavable",
           "hepzamirah.trickster.ghost.late_eviction": P + "ghost.late_gather", "hepzamirah.trickster.hounds_met": CS}


def hz(id, text, *choices, **kw):
    return n(id, "Hepzamirah", text, *choices, portrait="Hepzamirah", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Hepzamirah", **kw)


def lead(seq, then):
    """Lead-in nodes before a decision node. seq = [(id, fn, text, flag)], the first with flag None. Continue walks through
    every later node whose flag is held, in order, and then to `then`, so the decision node keeps fixed choice indices."""
    nodes = []
    for i, (nid, fn, body, _) in enumerate(seq):
        rest = seq[i + 1:]
        flags = [v[3] for v in rest]
        choices = [c("Continue", rest[j][0], requires=(flag,), forbids=tuple(flags[:j])) for j, flag in enumerate(flags)]
        choices.append(c("Continue", then, forbids=tuple(flags)))
        nodes.append(fn(nid, body, *choices))
    return nodes


def yard(id, title, entry, nodes, requires, forbids=(), delay=24, owner="Hepzamirah"):
    """A scene on her presence by the forge in Drezen (Chapter 5)."""
    SCENES.append(scene(id, title, owner, 5, entry, nodes, requires=requires, forbids=(CLOSED, CONFINED, *forbids), delay=delay,
                        last=5, optional=True, Relationship=REL, Chapters=[5], ContactUnit=BODY_UNIT, Areas=[DREZEN],
                        InteractionHub=PRESENCE, ForbidOverrides={CONFINED: RELEASED}))


# --- Colyphyr (Chapter 4): the one time the Commander meets her alive. A standing offer she laughs at. -------------------

SCENES.append(scene(P + "colyphyr.offer", "A standing offer", "Hepzamirah", 4,
    '[Trust your intuition] "Mutasafen took your army. Your father won\'t forgive that. When he comes for you, look me up."', [
    hz("laugh", '''{n}For a moment the daughter of Baphomet only stares at you. Then she laughs, and the sound goes round the cavern twice before the rock swallows it.{/n}
"Look you *up*? You are a gnat that has flown into the forge, crusader, and you offer the smith a favour?"
{n}Her horns dip. Above her, the angel's chains shift, as if even he wants to hear the answer.{/n}
"My father does not let his heirs die. He tests them. I have passed every test he ever set me. I gave him my mother. I gave him my brothers and sisters by the hundred. What have you ever given anyone, clown, except jokes?"''',
       c('"It\'s a standing offer. It doesn\'t expire."', "shelf"),
       c('[Grin] "I\'ll bring flowers to the funeral."', "shelf"),
       c('"He\'s already weighing you against someone. I can see it on you."', "weighed")),
    hz("weighed", '''{n}The laughter stops as if a door had closed on it.{/n}
"Weighing." {n}She says it very softly.{/n} "You know nothing about my father, crusader. You have never met a god who counts his children like coins and keeps only the heavy ones."
{n}Her crimson eyes are fixed on you, and for one breath she does not answer at all.{/n} "I am the heavy one. I gave him hundreds of better offerings than you will ever see."''',
       c("Continue", "shelf")),
    hz("shelf", '''{n}Something moves behind the crimson of her eyes, quick and cold, the way a spy's hand moves to a knife.{/n}
"Offer it to the angel. He loves a promise. I will take your head instead, and keep it on a shelf, so that when my father proves you wrong you can watch."''',
       c("[Let her have the last word.]", flags=(OFFER,))),
    ], requires=("trickster",), forbids=(DEAD, OFFER), last=4, optional=True, Relationship=REL, Chapters=[4],
    AnswerLists=[COLY_LIST], NativeReturnCue=COLY_RETURN, EntryMythic="PlayerIsTrickster"))


# --- The Ivory Labyrinth (Chapter 5): the setups, inline on her own list, before she can be driven off. ----------------

SNEER = '''"If you take me out, I will never thank you. Not today, not ever. I will owe you nothing and I will pay you nothing, and one day I will kill you for having seen me like this."
"Take it, or leave me to rot, and stop gloating."'''
GHOST_LEADS = [
    ("recognized", hz, '''"You. The clown from Colyphyr." {n}Her dangling eye turns in its socket to find you.{/n} "'When he comes for you, look me up.' You said it, and I laughed, and he came. I hate that you were right more than I hate him. Almost."''', OFFER),
    ("boasted", hz, '''"He told you no soul leaves here, didn't he? He told you he owned us. He always liked the sound of ownership." {n}The ghost's jaw works.{/n} "He says it the way a farmer counts cattle."''', BOASTED),
]


def setup_scene(id, title, entry, open_text, extra_forbids=(), extra_requires=()):
    nodes = lead([("open", hz, open_text, None), *GHOST_LEADS], "sneer")
    nodes.append(hz("sneer", SNEER,
        c('"After you."', flags=(PRIMED, GRUDGE, STARTED), native_next=DISSIPATE),
        c('"On second thought, rot."', flags=(CLOSED,), alignment=("Lawful", 1))))
    SCENES.append(scene(id, title, "Hepzamirah", 5, entry, nodes,
        requires=("trickster", DEAD, *extra_requires), forbids=(PRIMED, CLOSED, DISPERSED, *extra_forbids), last=5,
        optional=True, Relationship=REL, Chapters=[5], AnswerLists=[GHOST_LIST], NativeReturnCue=GHOST_RETURN,
        EntryMythic="PlayerIsTrickster", EntryAlignment=dict(Direction="Chaotic", Value=1),
        TricksterDevice=True, TricksterState="ghost"))


setup_scene(P + "ghost.second_time", "Leavable, again",
    '[Trust your intuition] "I stole the cell next door already. I\'m stealing yours too. It\'s called \'Leavable\' now. Coming?"',
    '''{n}The ghost's outline sharpens, the way a blade does when it is drawn.{/n}
"I heard you steal the lich's cell. I heard the walls give like wet parchment. I heard him *laugh*, the fool, as if a door were a gift." {n}The crushed side of her skull gleams white.{/n} "Nothing is a gift in this place. Everything is a leash with a pretty name."''',
    extra_requires=(LEAVABLE,))

setup_scene(P + "ghost.first_time", "Leavable",
    '[Play a prank on Baphomet\'s prison] "Your father stole this place. I\'m stealing it back. It\'s called \'Leavable\' now."',
    '''{n}The ghost's outline sharpens, the way a blade does when it is drawn.{/n}
"Steal *his* prison? He stole it first, from a bigger thief than you. You are all thieves down here, and I am the only one still locked in." {n}The crushed side of her skull gleams white.{/n} "Say the word again. Leavable. As if a word could open anything."''',
    extra_forbids=(LEAVABLE,))


# --- The late fallback: after the native [Attack] dispersed her, the wall is stolen aloud, on worse terms. -----------

SCENES.append(scene(P + "ghost.late_gather", "The wall, stolen aloud", "Hepzamirah", 5,
    '"Hepzamirah. I know you\'re still in the walls."', [
    nar("gather", '''{n}The cold in the corner thickens until it has a jaw again, then an eye, dangling.{/n}''',
        c("Continue", "demand")),
    hz("demand", '''"You struck at me, and now you come back with a door in your pocket?" {n}The ghost's voice is the scrape of horn on stone.{/n} "The jailers heard me break. They will want to know who let me go."
"So you will pay first. Say it where they can hear. Baphomet's daughter walks out because a clown stole the wall, not because she begged. Say it loud, clown. Let every jailer in this maze learn your name."''',
        c('[Steal the wall aloud, for every jailer to hear] "Attention, prison staff. This wall is mine. I\'ve named it \'Leavable\', and the lady is leaving through it. Complaints to Baphomet."',
          flags=(PRIMED, GRUDGE, LATE, STARTED), mythic="Trickster", alignment=("Chaotic", 2)),
        c('"Stay broken."', flags=(CLOSED,))),
    ], requires=("trickster", DEAD, DISPERSED), forbids=(PRIMED, CLOSED), last=5, optional=True, Relationship=REL,
    Chapters=[5], AnswerLists=[GHOST_LIST], ContactUnit=GHOST_UNIT, Areas=[LABYRINTH],
    TricksterDevice=True, TricksterState="ghost"))


# --- The post-Labyrinth fallback (remote): the Commander left without stealing her corner. Everything burned on the Lord of
# Beasts' altar goes to him, into his prison. Paper would be ignored; the cult's own rite is a mark cut in the flesh
# (the cellar cultists cut his horned head into their forearms), so the Commander cuts it into their own arm and speaks
# the theft into the blood. Polish 2026-09-28: the old paper deed of theft read as the notary crutch (06 registry); the
# main cost is now the scar the Commander carries (cost.horned_scar), with the chaplains' Favors as a secondary price.

SCENES.append(scene(P + "ghost.deed_by_fire", "A deed, by fire", "Memory", 5, "", [
    nar("cellar", '''{n}Three nights after the Labyrinth, the watch finds a cellar under the old grain exchange where a handful of your own soldiers have been cutting a horned head into their forearms. They have an altar down there: a slab of black stone, a brazier, and the old words of the Lord of Beasts' cult scratched round the rim. The chaplains say it answered: the man they caught at it had a cut on his arm that was still bleeding and a scar beside it that had not been there an hour before, and he had been talking to someone.{/n}
{n}Somewhere in his prison, two corridors from the lich's stolen cell, his daughter is still hiding in her corner from men with hooks. You did not steal it. You walked past.{/n}''',
        c("Continue", "deed")),
    nar("deed", '''{n}The cultists did not burn paper. The chaplains found what they burned: nothing. The altar is black with old blood, and every arm down there carries the same cut, a horned head in a circle, because that is how the Lord of Beasts reads his mail.{/n}''',
        c('[Cut his horned mark into your own forearm on his altar, in front of the chaplains] "I steal the corner where Hepzamirah hides. It\'s called Leavable now. Read it in my blood."',
          "burned", mythic="Trickster", alignment=("Chaotic", 2), crusade=("Favors", -200), flags=(PRIMED, GRUDGE, LATE, ALTAR, STARTED, SCAR)),
        c('"Let her rot. Break the altar."', flags=(CLOSED,), alignment=("Lawful", 1))),
    nar("burned", '''{n}The chaplains watch the Commander of the crusade kneel at an altar of the Lord of Beasts and open their own arm on it with a cultist's knife, a horned head in a circle, the lines as neat as you can make them with your teeth set. They do not stop you. One of them begins, very quietly, to write a letter to Nerosyan.{/n}
{n}Your blood smokes green where it touches the stone, and then the stone drinks it. The brazier goes out. In the dark something breathes on the back of your neck, rank as a byre, and a voice that is mostly teeth says one word into your ear, *thief*, and you know that it has read what you wrote, and that it will remember the hand. Somewhere very far down, something gives, like wet parchment. When you climb out of the cellar the candles on the stair are burning sideways, and the cut on your arm has already closed into a scar that looks years old.{/n}''',
        c("[Go up into the air.]")),
    ], requires=("trickster", DEAD, "baphomet.parley.latched"), forbids=(PRIMED, CLOSED), delay=72, last=5, optional=True,
    Relationship=REL, Remote=True, Chapters=[5], TricksterDevice=True, TricksterState="ghost"))


# --- The payoff (remote, 48 h): a haunting with no body, a deal with the traitor who grows them, and the rename. -------

BODY_LEADS = [
    ("letter", nar, '''{n}You still carry the letter you took from her table in Colyphyr, in a hand that loops with self-regard: "the revival system I created for myself is flawless. You can't kill me, even if you manage to kill me." Somewhere, then, there are spare bodies, and a man who knows how to grow them.{/n}''', LETTER),
    ("secret", hz, '''"In Colyphyr I boasted that I was one of the few who know the secret of Mutasafen's mortality." {n}The cold on the chair laughs, a sound like frost cracking.{/n} "You remember. So will he, when he reads my name."''', SECRET),
]
SCENES.append(scene(P + "ghost.body", "The lodger", "Memory", 5, "", [
    *lead([("start", nar, '''{n}Since the Labyrinth, the candles in your quarters burn sideways. The dogs of Drezen whine at your threshold and will not cross it. The chaplain who blesses the citadel doors walks the long way round your corridor now, and does not know why.{/n}
{n}Twice you have woken to a weight on your chest and a voice counting, very patiently, the ways a mortal throat can be opened.{/n}''', None),
           *BODY_LEADS], "flesh_ask"),
    hz("flesh_ask", '''"A ghost cannot hold a pick, clown," {n}the cold says, from the chair.{/n} "It cannot hold anything. I have tried your wine cup forty times. Find me flesh."
"You know who grows it. My alchemist. The traitor. He keeps bodies of himself hidden like a squirrel keeps nuts, and he stole my army with the time he saved on dying. He can grow one more."''',
       c('[Write to the traitor] "Dear Mutasafen. Your old mistress is haunting my chair, and she remembers how you die. Let\'s talk about spare bodies."',
         "terms")),
    n("terms", "Mutasafen", '''{n}The cold goes out at dusk with your letter and comes back at dawn smelling of formaldehyde and triumph. The reply is scratched on a sheet stained yellow where a reagent dripped through it.{/n}
"Commander. A ghost for a postman. You ask me to give a body to the one creature who swore to take my eyes. I decline, naturally.
Then I consider the alternative: a dead princess who walks through walls, talks, and knows where I sleep. I accept, naturally.
My price is one vial of your blood. Areelu's last experiment, walking around unexamined. It is a crime against science.
Understand one thing. Anything I make, I can unmake.
M."''',
      c('[Pay in blood] "One vial. Label it \'Do not open\'."', "body", flags=(BLOOD,)),
      c('[Pay in coin instead] "The crusade will fund one laboratory. Take it, and forget my blood."', "body",
        crusade=("Finances", -1000), flags=(LAB,)),
      c('[Threaten him with his own secret] "No price. She knows how you die. Now so do I."', "body_threat",
        alignment=("Evil", 1), flags=(MGRUDGE,))),
    nar("body_threat", '''{n}His second reply is one line, in a hand gone small and careful: "Very well. No price." The crate that follows it comes all the same.{/n}''',
        c("Continue", "body")),
    *lead([("body", nar, '''{n}It comes on the back of Mutasafen's Apprentice, a cambion with acid-scarred hands who sets it down at your gate and will not cross the threshold. The label says: "Some assembly required.
M."{/n}
{n}Inside, in brine, lies Baphomet's daughter, faithful to the last detail: the crushed side of the skull knitted into a ridge of scar, one horn a broken stump, one eye milk-white. He has grown her exactly as her father left her, down to the grit still in the scar.{/n}''', None),
           ("body_blood", nar, '''{n}He holds out an empty vial and a lancet. The label on the vial already says "Do not open", in his master's looping hand. He will not take the blood at a gate with the crate still sealed, he says: his master's terms are payment on delivery of a living tenant. He hangs the empty vial on your gatepost by its cord, and goes. He will be back for it full.{/n}''', BLOOD),
           ("body_coin", nar, '''{n}He counts the crusade's draft twice, slowly, moving his lips. Then he says, not quite to you, that the laboratory has paid for the flesh. The vial is another matter. His master still wants a vial of the Commander, for his silence about where the princess sleeps, and he will be back to collect it. The price, he says, has gone up. He seems to find this very natural.{/n}''', LAB),
           ("body_price", nar, '''{n}Pinned to the brine-soaked lining is a second note: "You said no price. The price went up. My Apprentice will collect it."{/n}''', MGRUDGE)],
          "rename"),
    nar("rename", '''{n}The cold is on your shoulder now, looking down at itself. It says nothing at all.{/n}''',
        c('[Rename the vessel] "You\'re not his vessel. You\'re a lodger\'s flat. Lodgers have bodies, and they pay rent. Landlords don\'t keep spare keys."',
          "flesh", flags=(RET, WRONG_BODY))),
    *lead([("flesh", nar, '''{n}Somewhere, very far away, a glass vial cracks on a laboratory shelf. The cold on your shoulder is gone. The thing in the crate opens its one good eye.{/n}
{n}She sits up in the brine and touches the scar, the stump and the dead eye, slowly, the way a moneylender counts coins that have been clipped.{/n}''', None),
           ("flesh_late", hz, '''"You came late, clown. The jailers had time to learn your name, and they whispered it all the way to Drezen. I counted every whisper."''', LATE),
           ("flesh_altar", hz, '''"You walked past me in his prison. Then you knelt at his altar in your own city and cut his mark into your own arm, to reach me. I felt the corner come loose like a rotten tooth." {n}Her lip curls, and her eye goes to your sleeve and stays there.{/n} "My father's mark. On you. You used his own post, clown, and you will wear the stamp until you die. I have never been so insulted in my life."''', ALTAR),
           ("flesh_offer", hz, '''"'Look me up.' You said it in Colyphyr, over the angel's head. I have looked you up, clown. Here I am, in a crate."''', OFFER)],
          "first_rent"),
    hz("first_rent", '''"You *mended* me." {n}It is said the way another woman would say "you spat on me".{/n} "Baphomet's daughter, grown in a jar by my own servant and unwrapped by a clown with a crowbar."
"Very well. I am alive, and I owe you rent. Here is the first payment. My father's archpriestess could call him, and he had to come. One day I will find out if that is still true. When I do, you may stand where he can see you. When I kill Mutasafen, you may not. That one is mine."''',
       c('"I\'ll bring snacks."'),
       c('[Intimidate] "You\'ll pay the rent I name."', flags=(LANDLORD,), alignment=("Evil", 1))),
    ], requires=("trickster.ever", PRIMED), forbids=(RET, CLOSED), delay=48, last=5, optional=True, Relationship=REL,
    Remote=True, Chapters=[5], TricksterDevice=True, TricksterState="ghost"))


# --- The courier (remote, 48 h after the return): Mutasafen's Apprentice comes to collect. Her test of the Commander. --

COURIER_LEADS = [
    ("paid_blood", hz, '''"He has come for the vial you promised his master, the empty one he hung on your gatepost. Payment on delivery, he says, and I am delivered. It is the only polite thing he has ever done, and he is doing it with my fingers round his windpipe."''', BLOOD),
    ("paid_coin", hz, '''"He says your laboratory bought my flesh and nothing else. The vial is for his master's silence about where I sleep, the price he raised at your gate. Of course he raised it. I taught that incubus spawn to haggle. So: a vial of you, for silence. Or his eyes, for mine."''', LAB),
    ("paid_threat", hz, '''"He says: 'You said no price. My master heard double.' I think I like your threat better than his arithmetic."''', MGRUDGE),
    ("collectors", hz, '''"And my father's cultists have already knocked for your tiefling, I hear. This one is not Father's. Father's people do not wipe their feet."''',
     "minagho_chivarro.trickster.debt.collectors"),
]
SCENES.append(scene(P + "body.hounds", "The Apprentice at the gate", "Memory", 5, "", [
    nar("door", '''{n}The gate guard's note is three lines long. A cambion with acid-scarred hands asked for "the Commander's small debt to my master". The fourth line is in another hand, much larger, pressed so hard the nib went through:{/n}''',
        c("Continue", "throat")),
    *lead([("throat", hz, '''"Your postman came back. I have him by the throat. He says he is owed a vial of you. He says his master will know if it is not your blood. I say his master will know nothing, because I am going to post his master the Apprentice's eyes, one at a time, in a box with a ribbon."''', None),
           *COURIER_LEADS], "joke"),
    hz("joke", '''"Unless you have a better joke. You usually do. Come down and tell it before I get bored, clown. I get bored quickly now. Flesh itches."''',
       c('[Hand over the vial] "Let him go. A deal is a deal, even with him."', "vial", flags=(CS, VIAL_PAID)),
       c('[Let her have him] "He\'s yours."', flags=(CS, COURIER_KILLED), alignment=("Evil", 1)),
       c('[Send him back with a forged vial] "Here. Areelu\'s last experiment. Mind the label."', flags=(CS, VIAL_FORGED),
         mythic="Trickster")),
    hz("vial", '''{n}By the time you reach the gate she has the Apprentice kneeling in the mud with her boot on his calf. She holds out her hand for the lancet without looking at you, and when you give her your arm instead she takes that too.{/n}
{n}She draws it herself. She is not gentle, and she is not clumsy either: one cut inside the elbow, exactly deep enough, her thumb pressing the vein to make it run faster, and she watches the vial fill the way a moneylender watches a scale settle. It takes longer than you expect. By the end the gate is swaying slightly and your mouth is dry.{/n}
"Understand what you have paid, clown. He does not want this to drink. He wants to grow things from it." {n}She corks the vial with her teeth, spits the wax, and drops it into the Apprentice's scarred hands.{/n} "Somewhere in his cave there will be a jar with a little of you in it, and you will never know what it is becoming. Now you have my reason to want him dead. Good. I like company."''',
       c("[Press a rag to your arm.]")),
    ], requires=("trickster.ever", RET), forbids=(CLOSED, CS), delay=48, last=5, optional=True, Relationship=REL,
    Remote=True, Chapters=[5]))


# --- The terms (the commit, in person by the forge). Her refusal is reachable on every branch and is a hard no. -------

TERMS_LEADS = [
    ("ember", n, None, "ember.present"),
    ("killed", hz, '''"The Apprentice's eyes went to Mutasafen in a box, as promised. I lie awake wondering which of his bodies opened it. It is the best sleep I have had."''', COURIER_KILLED),
    ("forged", hz, '''"Your vial of wine is on its way to Mutasafen's bench. I would give my other eye to watch him run it through his glassware."''', VIAL_FORGED),
    ("confined", hz, '''"And you let your chaplains lock my door from the outside for three nights. I have not forgotten. I am not a woman who forgets a lock."''', CONFINED),
]


def ember_node(nid, text, *choices, **kw):
    return n(nid, "Ember", text, *choices, portrait="Ember", **kw)


TERMS_LEADS[0] = ("ember", ember_node, '''{n}Ember is sitting on an upturned bucket by the forge, holding a jar of wildflowers that has plainly been thrown at least once.{/n}
"She let me stay the whole afternoon today. She only threw the jar once." {n}She points with it at the far wall, where the light does not reach.{/n} "She says she wants the clown. I think she means you."''', "ember.present")

yard(P + "body.terms", "Terms, in person", '"You wanted the clown."', [
    *lead([("open", nar, '''{n}She is by the far wall of the smith's yard, where the light does not reach, arms crossed over a body she did not choose. Her heavy pick leans against the wall beside her, head down, like a hound told to wait.{/n}''', None),
           *TERMS_LEADS], "price"),
    hz("price", '''"Your chaplains pray outside my door as if I were a sickness. Your soldiers make the sign of the Inheritor when I pass, and one of them spat, once. Enough. Listen, clown, because I will say this once."
"I stay. My own door, my own guards, and no priest mends anything else of mine. When I go for Mutasafen, nobody follows. And my father is mine. The day I call him, you will not bargain with him over my head."
"In return I stand beside you in every fight until then. I will not pretend to be grateful. Do not ask me to."''',
       c('[Agree to all of it] "Done. Your door, your guards, your father."', "rent"),
       c('[Counter] "You\'ll serve as my blade. Guests don\'t get conditions."', "refused", flags=(LANDLORD,),
         alignment=("Evil", 1)),
       c('"Why stay at all? The door\'s Leavable. You could walk out tonight."', "why")),
    hz("why", '''"Walk out to where?" {n}She laughs, short.{/n} "My father's cult calls me apostate in your cellars. Mutasafen has his hand in half the Worldwound and wants the rest of me back on his bench. Horzalah would put a spear in me for the pleasure of it, and Vorlesh has my place and would like my soul in a jar to go with it."
"Everything outside your door wants to own me, clown. Inside it there are walls, a crusade's worth of steel between me and all four of them, and a landlord who is easier to kill than any of them if the lease sours. I can do the sums." {n}She looks at the forge.{/n} "That is why. It is not a sentimental reason. It is arithmetic. Now answer me."''',
       c('[Agree to all of it] "Done. Your door, your guards, your father."', "rent"),
       c('[Counter] "You\'ll serve as my blade. Guests don\'t get conditions."', "refused", flags=(LANDLORD,),
         alignment=("Evil", 1))),
    hz("rent", '''"Words. My father gave me words too. *Protection of a rare kind*, he said, and the protection was a leash."
{n}She steps close enough that you can see where the scar pulls the corner of her mouth, and the heat of her comes off her like the heat off the forge.{/n} "Say the other thing. That if I walk out of your door, you let me."''',
       c('"The door is Leavable. So are you. Stay anyway."', "sealed"),
       c("[Say nothing]", "refused"),
       c('[Trickster] "If you walk out, I\'ll rename the whole city Leavable and come after you through the wall."', "sealed_joke")),
    hz("sealed_joke", '''{n}She stares at you. Then something breaks in her face, the way ice breaks on a trough in the first warm morning, and she laughs, helplessly, with her forehead against your shoulder and her horn digging into your collarbone.{/n}
"You would," {n}she says into your coat.{/n} "You would steal a whole city to follow a woman out of it. That is not the answer I asked for, clown. It is a better one."''',
       c("Continue", "sealed")),
    hz("sealed", '''{n}She takes your wrist, not your hand, hard enough to leave marks, and holds it for exactly as long as she decides.{/n}
"Then I stay. Not because you freed me. Because you would let me go."''',
       c("[Let her keep your wrist]", "threshold", flags=(COMMITTED,))),
    nar("threshold", '''{n}She does not let go. She walks backwards through the yard, out of the forge-light, towing you by the wrist like a prize led home from a raid, and the smith finds something urgent to hammer on the far side of his anvil.{/n}
{n}At her door she stops, and shoves you back against it with her forearm across your chest, and looks at your mouth the way she looked at the Apprentice's throat. Her breath is hot and smells of iron. The stump of her horn grazes your temple as she bends her head.{/n}
"You smell of my father's prison still." {n}She says it into your mouth, and the kiss is a bite that forgot to finish.{/n} "I will get it off you."
{n}She reaches past you for the latch herself, and the door gives, and you go through it together, not gracefully. She kicks it shut behind her with her heel. Her hands are a surgeon's and a butcher's at once: the buckles of your coat come open under her fingers one after another, quick and exact, as if she has taken apart harder things than you and enjoyed every one. Her own clothes she simply tears open at the shoulder and lets fall.{/n}
{n}Her skin runs hotter than a mortal's. There is old scar tissue along her ribs, rough under your palms, and when your hand finds it she catches your wrist and presses it there, harder, as if to say *that is mine too, learn it*. She walks you back across the room until your legs meet the furs heaped by the brazier, pushes you down onto them, and follows you down, and pins both your wrists above your head with her pick-hand, easily, the way she would hold a haft.{/n}
"Mine," {n}she says, low, and her good eye is very bright.{/n} "Tonight that is the only rule." {n}Her free hand goes lower, unhurried, taking inventory.{/n}''',
        c("[Let her have her rule.]")),
    hz("refused", '''"I knelt once, to a father who promised me everything. I will not do it for a landlord."
{n}She walks out of the yard without a glance at anyone. By morning her door stands open and her room is empty, except for the jar of wildflowers, unbroken, set in the middle of the floor.{/n}''',
       c('"Then go."', flags=(CLOSED,))),
], requires=("trickster.ever", RET, CS, FIRST, PICK), forbids=(COMMITTED,), delay=24)


# --- Epilogue pages (Owner HepzamirahEpilogue; ordered siblings; no effects). -------------------------------------------

EP = dict(last=6, Relationship=REL)
LEAVABLE_PARAS = (
    p("{n}She kept the scar her father gave her, and the milk-white eye, and never let a priest heal either.{/n}", requires=(WRONG_BODY,)),
    p("{n}Somewhere a vat of Mutasafen's still held a little of the Commander, until the fire.{/n}", requires=(BLOOD, VIAL_PAID)),
    p("{n}The crusade's books listed one laboratory \"in the Worldwound, address unknown\". The address, it turned out, was known to one person.{/n}", requires=(LAB,)),
    p("{n}Mutasafen found the wine in the vial on his second test, and never forgave the joke. He did not live long enough to repay it.{/n}", requires=(VIAL_FORGED,)),
    p("{n}Mutasafen hired himself a quieter Apprentice to replace the one whose eyes came to him in a box with a ribbon, and went on writing to her. She read every letter aloud to the forge, and fed it to the coals.{/n}", requires=(COURIER_KILLED,)),
    p("{n}She called the Commander \"landlord\" to the end, and meant it as a threat, and the Commander learned to take it as something else.{/n}", requires=(LANDLORD,)),
    p("{n}Of her father she spoke once a year, on the day of Colyphyr, and only to say that she had not called him yet.{/n}", requires=(GRUDGE,)),
)
SCENES.append(scene(P + "epilogue.leavable", "", "HepzamirahEpilogue", 6, "", [
    nar("page", '''{n}Hepzamirah stayed at the Commander's side through the Threshold and after it, behind a door that had no lock because she had forbidden one. She never called it gratitude. The spring after the war, word came that a laboratory in the Worldwound had burned with every body in it; she came home with a crystal-cutter's lens on a cord, smelling of formaldehyde and smoke, and never said where it came from.{/n}''',
        paragraphs=LEAVABLE_PARAS)],
    requires=("trickster.ever", COMMITTED), forbids=("sacrifice", CLOSED),
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, **EP))

SCENES.append(scene(P + "epilogue.leavable_on_record", "", "HepzamirahEpilogue", 6, "", [
    nar("page", '''{n}When the Commander was entered among the dead of the Threshold, Hepzamirah broke the door she had forbidden anyone to lock, and walked out through it into the Worldwound with her pick and nothing else. Mutasafen's laboratories burned one a season for years after, each with a single milk-white eye painted on the door. The daughter of Baphomet never called her father. Those who knew her said she was saving it for something.{/n}''')],
    requires=("trickster.ever", COMMITTED, "sacrifice"), forbids=("trickster.commander_back", CLOSED), **EP))

SCENES.append(scene(P + "epilogue.commit", "", "HepzamirahEpilogue", 6, "", [
    nar("page", '''{n}Hepzamirah never gave the Commander her terms in Drezen. She gave them after the Threshold, at a door she had kicked open: "The door was leavable. I left. I came back. That is the only answer you get." She stayed on those terms, and no others.{/n}''')],
    requires=("trickster.ever", CS), forbids=(COMMITTED, CLOSED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, **EP))

SCENES.append(scene(P + "epilogue.refused", "", "HepzamirahEpilogue", 6, "", [
    nar("page", '''{n}Hepzamirah left Drezen through the door she had been promised. For years afterwards Mutasafen's hidden laboratories burned, one a season, each with a single milk-white eye painted on the door. She never called her father. Those who knew her said she was saving it.{/n}''')],
    requires=("trickster.ever", RET, CLOSED), **EP))


# --- Reactions: Greybor and Ember (Baphomet reads her through Minagho's parley). ----------------------------------------

SCENES.append(reaction("Greybor", P + "react.greybor", (RET,),
    '''"I've been paid to kill things that came back. Never twice for the same one." {n}He tests the edge of his axe with his thumb.{/n} "If she wants a price on the alchemist's heads, mine is per head. I hear he has several."''',
    answer_list=GREYBOR_LIST, forbids=("greybor.dead", "greybor.kicked_out"), entry='"Hepzamirah is back. In a body."',
    chapter=5, last=5, portrait="Greybor"))
SCENES.append(reaction("Ember", P + "react.ember", (RET, "ember.present"),
    '''"The sad lady with the broken head has a head again. It's still a bit broken." {n}Ember brightens, then frowns.{/n} "She shouted at me when I brought her flowers. That's all right. People who hurt a lot shout. I'll bring more."''',
    answer_list=EMBER_LIST, forbids=EMBER_FORBIDS, entry='"Hepzamirah is out."', chapter=5, last=5, portrait="Ember"))


def integrate(payload):
    """Register the new relationship's own keys and presences. Scenes are added by expansion.py; world keys bind on
    demand (trickster_world)."""
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    have = payload.setdefault("InventoryItems", {}).get(PICK_HELD)
    if have is not None and have != PICK_ITEM:
        raise ValueError("Conflicting binding: " + PICK_HELD)
    payload["InventoryItems"][PICK_HELD] = PICK_ITEM
    items = payload.setdefault("RemovableItems", [])
    if PICK_ITEM not in items:
        items.append(PICK_ITEM)
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]

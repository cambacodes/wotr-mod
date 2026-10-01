"""Minagho and Chivarro on the Trickster path: the brand re-addressed (F17), through the wrong wardrobe (F01) and the house
always collects (F24). Specs: Writer/handoffs/trickster/minagho.md and chivarro.md (one relationship, two women).

Canon: Minagho bleeds from Baphomet's brand until she "spilled the blood of the one who caused me to fail in Kenabres"
(MinaghoAfterCombat/Cue_0020 234795ef; MinaghoAndAzata/Cue_0025 60906a72), and Baphomet's seals "simply mark their bodies
as mine" (Prison_Baph/Cue_0123 c5f91838). Chivarro: "Minagho and I... were closer than most demons ever get" (Cue_0097
d8b51192); "Any of them can be yours for a night... Or forever, if your pockets are deep enough" (Cue_0081 594482c2). Herrax
asks for the kill in advance (Herraxa_dialogue/Cue_0045_KillChivarro 49135105) and her house strips the dead: rings "cut off a
dead body along with the fingers" (Cue_0052 d6955c2a). "Closets grant you freedom. You can step inside one, and exit from
another..." (SocothBriefing/Cue_0011 2f4be0bd). Authored, and labelled as authored: the Commander volunteering as the
failure of record; the unpaid seal that keeps the body it marks ("The dead do not bleed."); the linen press; Herrax's
house never destroying stock it can sell. The killed-Chivarro device (Sol quality pass, 2026-09-30) is prepared before
the kill and never contradicts it: with the deposit, Herrax's house sends down the Chivarro on its own menu (Sael, the
incubus who wears her face for guests who cannot afford her) in her rings, the Commander kills him knowingly in the native
fight, and the real Chivarro waits in Herrax's cellar, legally dead. That death is a Ledger secret. Without a deposit
nothing was prepared: the Commander killed Chivarro herself, the death stands, and Minagho alone remains (no raise of any
kind; 06 raise budget).
"""
import copy

from story_format import c, n, p, reaction, scene
from storylines import household, trickster_world

SCENES = []
P = "minagho_chivarro.trickster."
REL = "minagho_chivarro"

# Relationship flags (registered: storylines/minagho_chivarro_continuation.py).
STARTED, CLOSED, COMPLETE = "minachiv.started", "minachiv.closed", "minachiv.complete"
# Minagho (minagho.md section 4).
PRIMED, DEBT, TERMS, KNELT = P + "primed", P + "cost.baphomet_debtor", P + "cost.baphomet_terms", P + "cost.baphomet_knelt"
LATE_CLAIM, PALM, BRANDED = P + "cost.late_claim", P + "cost.palm_scar", P + "cost.baphomet_branded"
RET_M, MIN_IN, DELIVERED, DECL_M = P + "returned_minagho", P + "minagho_in", P + "collateral_delivered", P + "declined_minagho"
REFUSED_B, HEARD, CLAIMED, MET = P + "baphomet_refused", P + "baphomet_heard", P + "claimed_debt", P + "pursuers_met"
GIVEN, RECEIPT = P + "pursuers_given", P + "cost.receipt_sent"
# Chivarro and the pair (chivarro.md section 4).
REUNITED, CH_IN, RET_C = P + "reunited", P + "chivarro_in", P + "returned_chivarro"
WAITING, SENT_BACK, DECL_C, DECLINED = P + "chivarro_waiting", P + "chivarro_sent_back", P + "chivarro_declined", P + "declined"
DEPOSIT, FAVOR, LATE, SOCOTH, DOOR = (P + "chivarro_deposit", P + "cost.herrax_favor", P + "cost.late", P + "cost.socoth_owed",
                                      P + "cost.door_marked")
T_OFFER, T_NAME, T_HOUSE, WALKED = P + "tprev.offer", P + "tprev.name", P + "tprev.house", P + "chivarro_walked"
BURNED, OWNED, KEPT = P + "bill_burned", P + "chivarro_owned", P + "kept_in_service"
HALF, PALM_TABLE, WON_BACK = P + "cost.half_the_pair", P + "cost.palm_on_table", P + "cost.won_back"
CELLAR = P + "chivarro_cellar"   # Derived: she was removed from power or exiled to the Lower City (variant read)
# Set with every Trickster commit: the registered endings narrate the RanRomance visits this Commander never had.
CHAIN = P + "committed"
DOUBLE = "trickster.secret.chivarro_double"   # the deposit: the boy who died in her rings (household Secrets)
# A night flag per threshold (Sol BEL): each morning after requires the night it follows, not only the commit.
NIGHT_PAIR, NIGHT_CHIV, NIGHT_MIN = P + "night.pair", P + "night.chivarro", P + "night.minagho"
MORNING = P + "cost.morning_after"   # the night's price, named the next morning (letter commits set it on their own page)
DERIVED = {CELLAR: [["chivarro.removed"], ["chivarro.exiled"]]}

CHIV_UNIT = "b7e819e2a9bb0804abcbffe8e7d91ba6"   # Chivarro.jbp (female, CutsceneNeutrals)
MIN_UNIT = "565ccab37e2475742b043ec912a750fa"    # Minagho_DrezenInThePast (female, Neutrals; the only non-hostile Minagho)
WILCER = "a380d926e92f70e429681eb9654478f9"      # DrezenCapital_Quartermaster, Wilcer Garms (the anchor)
DREZEN = "2570015799edf594daf2f076f2f975d8"
HERRAX_LIST = "43f93812d6216c94db356622859397f1"   # Herraxa_dialogue/AnswersList_0004 (her hub after the contract)
HERRAX_RETURN = "1af69c65d15cc8949a4fe47a45c4f85d"  # Cue_0100 "We have some true gems here."
BAPH_LIST = "cbd2f289d8173fb41a231772290440ba"      # Prison_Baph/AnswersList_0071 (the parley hub)
HEPZ_OUT = "hepzamirah.trickster.primed"               # node variant only (hepzamirah_trickster)
BAPH_RETURN = "2d1a338243b8ddb429bbad5db08ed7de"    # Cue_0127 "Areelu Vorlesh will lead my armies..."
SOCOTH_LIST = "db7f69fa013c7ec49b651e7ad26c67de"    # SocothInCloset/AnswersList_0003
SOCOTH_RETURN = "e52a1d81a098a2843aa5f1f35481ddc1"  # Cue_0002 "Well? Do you have it now?"
DAERAN_HUB = "4d978cbd2aa780d46874255282039f3f"
WENDUAG_HUB = "ced27e744d2dded40bbb5adf17816dbb"
CAMELLIA_HUB = "589d83230bbbfd04bb1220ee4fef1ce1"

PRES_SPARED = "minagho_chivarro.presence.minagho_spared"
PRES_MIN = "minagho_chivarro.presence.minagho"
PRES_CHIV = "minagho_chivarro.presence.chivarro"
PAIR_FO = {"minagho.dead": RET_M, "chivarro.dead": RET_C}   # G6 on every chain scene

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={"minagho.dead": RET_M, "chivarro.dead": RET_C},
    # R2-0 b: the relationship's UnavailableFlags are shared, so every device state detects both deaths.
    TricksterAccess={
        "minagho_dead": dict(detect=["minagho.dead", "chivarro.dead"], device=P + "minagho_dead.brand", returned=RET_M),
        "minagho_alive": dict(detect=["!minagho.dead", "chivarro.dead"], device=P + "spared.brand", returned=None),
        "chivarro_alive": dict(detect=["!chivarro.dead", "!chivarro.searching", "minagho.dead"], device=P + "reunion.wardrobe",
                               returned=REUNITED),
        "chivarro_dead": dict(detect=["chivarro.dead", "minagho.dead"], device=P + "chivarro_dead.bought", returned=RET_C)})
PRESENCES = {
    # E12b spawn-copies beside the quartermaster, clickable (E12c). Minagho has two keys, never wanted together.
    PRES_SPARED: dict(Unit=MIN_UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=WILCER, Side="left", Distance=2.0),
                      Requires=["trickster.ever", "minagho.spared.latched"], Forbids=["minagho.dead", CLOSED, DECL_M],
                      MinChapter=5, MaxChapter=5, AnswerLists=[], Dialog="hub",
                      Greeting="{n}Minagho is sitting on a crate outside the quartermaster's stores, turning one of the crusade's "
                               "daggers over in her fingers, with her marked brow turned away from the street.{/n}"),
    PRES_MIN: dict(Unit=MIN_UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=WILCER, Side="left", Distance=2.0),
                   Requires=["trickster.ever", "minagho.dead"], RequiresAnyGroups=[[MIN_IN, DELIVERED]], Forbids=[CLOSED],
                   MinChapter=5, MaxChapter=5, AnswerLists=[], Dialog="hub",
                   Greeting="{n}Minagho is against the wall of the quartermaster's stores. Nobody in Drezen stands closer to "
                            "her than they must.{/n}"),
    PRES_CHIV: dict(Unit=CHIV_UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=WILCER, Side="right", Distance=2.0),
                    Requires=["trickster.ever", CH_IN], Forbids=[CLOSED, SENT_BACK], MinChapter=5, MaxChapter=5, AnswerLists=[],
                    Dialog="hub",
                    Greeting="{n}Chivarro has taken the quartermaster's bench as though it were a divan. Wilcer Garms counts "
                             "his stores with his back to her and does not turn around.{/n}"),
}


def mg(id, text, *choices, **kw):
    return n(id, "Minagho", text, *choices, portrait="Minagho", **kw)


def cv(id, text, *choices, **kw):
    return n(id, "Chivarro", text, *choices, portrait="Chivarro", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, **kw)


def hx(id, text, *choices, **kw):
    return n(id, "Herrax", text, *choices, **kw)


def baph(id, text, *choices, **kw):
    return n(id, "Baphomet", text, *choices, **kw)


def varied(base_id, speaker, text, variants, decisions):
    """A node followed by optional variant lines, each its own node (paragraphs are for epilogue pages only).
    variants: [(id, speaker_fn, text, flag)]. Continue walks through every variant whose flag is held, in order; the
    decisions sit on the last node shown."""
    seq = [(base_id, speaker, text, None), *variants]
    nodes = []
    for i, (nid, fn, body, _) in enumerate(seq):
        rest = [v[3] for v in seq[i + 1:]]
        choices = [c("Continue", seq[i + 1 + j][0], requires=(flag,), forbids=tuple(rest[:j])) for j, flag in enumerate(rest)]
        for d in decisions:
            d = copy.deepcopy(d)
            d["Forbids"] += [f for f in rest if f not in d["Forbids"]]
            choices.append(d)
        nodes.append(fn(nid, body, *choices))
    return nodes


def physical(id, title, owner, hub, unit, nodes, requires, forbids=(), delay=24, **extra):
    """Ch5, on one of the pair's own click-to-talk presences in Drezen (E12c)."""
    SCENES.append(scene(id, title, owner, 5, "", nodes, requires=requires, forbids=forbids, delay=delay, last=5,
                        optional=True, Relationship=REL, Areas=[DREZEN], Chapters=[5], ContactUnit=unit,
                        InteractionHub=hub, **extra))


def letter(id, title, nodes, requires, forbids=(), delay=24, owner="Memory", **extra):
    SCENES.append(scene(id, title, owner, 5, "", nodes, requires=requires, forbids=forbids, delay=delay, last=5,
                        optional=True, Relationship=REL, Remote=True, Chapters=[5], **extra))


# === Minagho: the brand re-addressed (F17) ==========================================================================

# 5.1 Primers, inline, after her own recital of the brand's terms; the terminal choice hands back to her canon reply
# (Cue_0021 / Cue_0026), which returns to the native kill/spare list, so every native etude still starts.
JOKE = '[Play a cruel trick on Baphomet] "\'Bleed until you spill the blood of the one who failed you\'? Fine. I\'m the one who failed him."'
for sid, ch, lst, nrc, nxt, told in (
        ("setup_c4", 4, "82a0c2ad3e6dc41469ec66a7affdc486", "0aa00bcf3121a694dbf306bea0f62153",
         "99d65001b1b0cfe45b2f47ad7d7dac7c", "minagho.brand_told_c4"),
        ("setup_c3", 3, "b00190e0e55fd9944b7fc8de5c83cbc0", "3c6de45d40c17fa40806e4d931eaf7b5",
         "093724348a359594ebe7f7193e7b86dc", "minagho.brand_told_c3")):
    SCENES.append(scene(P + "minagho_dead." + sid, "Put my name down", "Minagho", ch, JOKE, [
        mg("grin", '''{n}The demoness stops mid-sob. Her eyeless face tilts toward you, and for a moment she forgets to be afraid.{/n}
"You... volunteer? For *his* ledger?" {n}She laughs, high and ugly.{/n} "Do you have any idea what he does to the ones who fail him? Look at my face, Golarian. Look at it."
{n}The mark on her brow is still bleeding. It is bleeding less.{/n}''',
           c('"Looking. It suits you better dry."', flags=(PRIMED, DEBT), native_next=nxt))],
        requires=("trickster", told), forbids=(PRIMED, "minagho.dead"), last=ch, optional=True, Relationship=REL,
        AnswerLists=[lst], NativeReturnCue=nrc, EntryMythic="PlayerIsTrickster",
        TricksterDevice=True, TricksterState="minagho_alive"))

# 5.2 The parley: the one injected answer on Baphomet's Labyrinth hub. His price is his seal on the Commander.
OPEN_CHOICES = (
    c('[Hold up your bleeding palm] "The one who failed you in Kenabres? That\'s me. You\'ve had my blood every morning since. I\'ve come for her body."',
      "terms", requires=(PRIMED, "minagho.dead")),
    c('[Cut your palm on his cage and press it to the seal] "Kenabres. The failure you branded her for. Sign me in as it, in blood, now. Then give me her body."',
      "terms", requires=("trickster", "minagho.dead"), forbids=(PRIMED,), flags=(PRIMED, DEBT, LATE_CLAIM), mythic="Trickster"),
    c('"I put my name on her brand. It bleeds on me now."', "thief", requires=(PRIMED,), forbids=("minagho.dead",)),
    c('"Never mind."', abort=True))
SCENES.append(scene(P + "react.baphomet", "The collateral", "Baphomet", 5, '"About Minagho."', [
    baph("open", '''{n}Baphomet's vision turns its horned head toward you, as though a new smell had come into the cell.{/n}''',
         c("Continue", "primed_alive", requires=(PRIMED,), forbids=("minagho.dead", HEPZ_OUT, "horzalah.trickster.returned")),
         c("Continue", "told", requires=("baphomet.minagho_dead_told", "minagho.dead"), forbids=(HEPZ_OUT, "horzalah.trickster.returned")),
         c("Continue", "base", requires=("minagho.dead",), forbids=("baphomet.minagho_dead_told", HEPZ_OUT, "horzalah.trickster.returned")),
         c("Continue", "daughter", requires=(HEPZ_OUT,)),
         c("Continue", "weaker", requires=("horzalah.trickster.returned",), forbids=(HEPZ_OUT,))),
    # Hepzamirah's node variant (ledger 10: Baphomet never collects from her; he only notices, and does not care).
    baph("daughter", '''"And my daughter walked out of my prison behind you, through a wall you had the insolence to name." {n}The vision's lip curls back from its teeth.{/n} "Do you think that wounds me? I possess none of a father's sentimentality. Keep her, thief. Everything that is mine comes home to me in the end."''',
         c("Continue", "primed_alive", requires=(PRIMED,), forbids=("minagho.dead", "horzalah.trickster.returned")),
         c("Continue", "told", requires=("baphomet.minagho_dead_told", "minagho.dead"), forbids=("horzalah.trickster.returned",)),
         c("Continue", "base", requires=("minagho.dead",), forbids=("baphomet.minagho_dead_told", "horzalah.trickster.returned")),
         c("Continue", "weaker", requires=("horzalah.trickster.returned",))),
    # Horzalah's node variant (ledger: he has not noticed that she resigned; his silence stands, Prison_Baph/Cue_0122).
    baph("weaker", '''{n}The vision's gaze slides past you, as if looking for something it has already dismissed.{/n} "You smell faintly of the weaker branch, mortal. Horzalah. She bet everything, and lost, and called my name on the brink of defeat, and I did not answer. Whatever she has done since, I have not troubled to learn. Why should I nourish the shoots of the weaker branch?"''',
         c("Continue", "primed_alive", requires=(PRIMED,), forbids=("minagho.dead",)),
         c("Continue", "told", requires=("baphomet.minagho_dead_told", "minagho.dead")),
         c("Continue", "base", requires=("minagho.dead",), forbids=("baphomet.minagho_dead_told",))),
    baph("primed_alive", '''{n}The vision laughs, and the bone walls laugh with it.{/n} "I heard. Every seal I own heard. You stood in front of my slave and told her you were the failure of Kenabres, and my brand believed you. I added seals to her for less."
"Very well, debtor. I never forget a debt, and I never forgive a thief. You are both."''', *OPEN_CHOICES),
    baph("told", '''"You heard me say she failed. And now you come to buy the failure. Her debt was paid in screams, and then in her corpse. What could a mortal offer for either?"''',
         *OPEN_CHOICES),
    baph("base", '''{n}The horned vision tilts its head, as a butcher does at a lamb that has walked in by itself.{/n}
"Minagho? Her debt was paid in screams, and then in her corpse. What could a mortal offer for either?"''', *OPEN_CHOICES),
    baph("thief", '''"Then bleed, debtor. Every morning. And know that my seals do not forget which hand they are on."''',
         c('"Noted."', flags=(HEARD,))),
    baph("terms", '''"A thief who comes to the owner with the stolen goods in hand. How refreshing." {n}The pentagram on the vision's brow bleeds.{/n}
"You wish to buy back a corpse that bears my seal? My gifts are always generous, mortal, and my price is simple. Kneel, and say you are mine, and the collateral is returned to you intact."''',
         c("Continue", "terms_late", requires=(LATE_CLAIM,)),
         c('[Kneel] "I\'m yours. Send her home."', "knelt", forbids=(LATE_CLAIM,), alignment=("Evil", 1)),
         c('[Take him at his word] "You said it: the debt is mine, and she is the collateral. Collateral goes where the debt sleeps."',
           "laugh", forbids=(LATE_CLAIM,), mythic="Trickster", alignment=("Chaotic", 1)),
         c('"Keep her."', "keep", forbids=(LATE_CLAIM,))),
    baph("terms_late", '''"And you signed after the fact, in a cage full of bones, with her already cold. A thief who signs late pays in full. Kneel, or leave her to me."''',
         c('[Kneel] "I\'m yours. Send her home."', "knelt", alignment=("Evil", 1)),
         c('"Keep her."', "keep")),
    baph("knelt", '''"Good. You kneel well, for a crusader."''',
         c("Continue", "knelt_initiate", requires=("kyado.initiated",)),
         c("[Rise.]", flags=(TERMS, KNELT, DELIVERED), forbids=("kyado.initiated",))),
    baph("knelt_initiate", '''"Kneel? You joined my flock in Kyado's temple. Say it again, and mean it this time."''',
         c("[Rise.]", flags=(TERMS, KNELT, DELIVERED))),
    baph("laugh", '''{n}The laughter comes from the walls of bone, not from the vision.{/n}
"Words. My seals are not words. They are on your hand, and they will be on your hand when I choose to close it." {n}The eyes narrow.{/n}
"...Very well. My servants will lay her at your door. And they will remember the way."''',
         c('"At my door, then. Mind the stairs."', flags=(TERMS, DELIVERED))),
    baph("keep", '''"Then she rots in my name. My collectors will call on the debtor all the same. Perhaps you will bargain better with them."''',
         c('"Rot is cheap. I\'ll wait for a better price."', flags=(REFUSED_B,))),
], requires=("trickster.ever",), RequiresAnyGroups=[[PRIMED, "minagho.dead"], [PRIMED, "trickster"]],
   forbids=(RET_M, TERMS, REFUSED_B, HEARD), last=5, optional=True, Relationship=REL,
   AnswerLists=[BAPH_LIST], NativeReturnCue=BAPH_RETURN, TricksterDevice=True, TricksterState="minagho_dead"))

# 5.3 Dead return. The servants kept their word to the letter; the knife is hers, the palm is the Commander's.
WAKE = '''{n}You close her fingers around the hilt and draw it across your palm. Technically, she did it. The mark on her face drinks, and dries, and stays; and her chest moves.{/n}
"...You." {n}She licks your blood from her own fingers, slowly, as if tasting a vintage.{/n} "I died cursing you, and I wake up at your door, owing you. Is that the joke? Is *that* your idea of funny?"
"He will smell this on you. Every seal he owns will. You have made yourself his, you idiot, and for what? For me?" {n}Her lips peel back from her teeth.{/n} "I will find the flaw in this. And when I do, I will decide whether you were worth the blood."'''
WAKE_BRANDED = '''{n}You close her fingers around the hilt and draw it across your palm. Technically, she did it. The mark on her face drinks, and dries, and stays; and her chest moves.{/n}
"...You." {n}She finds the fresh seal on your other hand before she finds her own breath.{/n} "He branded you *twice*? For a corpse he had already thrown away? You are the stupidest mortal I have ever owed."
{n}She licks your blood from her own fingers, slowly, as if tasting a vintage.{/n} "He will smell this on you. Every seal he owns will. I will find the flaw in this. And when I do, I will decide whether you were worth the blood."'''
WAKE_VARIANTS = [
    ("wake_knelt", mg, '"You *knelt* to him. For me. I will never let you forget it, and neither will he."', KNELT),
    ("wake_late", mg, '"You signed his ledger in a cage full of bones, with me already cold. Late, Golarian. Everything you do is late."',
     LATE_CLAIM),
    ("wake_kyado", mg, '"Wait. You *are* one of his. Kyado\'s temple. You joked your way into his flock, and now the joke has teeth."',
     "kyado.initiated"),
    ("wake_staunton", mg, '"That dead dwarf in crusader plate. Tell me he stayed dead."', "minagho.killed_by_staunton"),
]
CLAIMED_NODE = mg("claimed", '''{n}Something in her face settles, the way a bad wound settles once it has been named.{/n} "Better. At least that I understand. A debt, with a creditor, and a price." {n}She wipes your blood from her mouth with the back of her hand.{/n} "Do not ever pretend it is anything kinder."''',
                  c("[Let her keep her contempt.]"))


def wake_nodes(text, extra=()):
    decisions = (c('"Then find it."', flags=(RET_M, PALM, MIN_IN, STARTED, *extra)),
                 c('[Intimidate] "You owe me a life. Start paying."', "claimed",
                   flags=(RET_M, PALM, MIN_IN, STARTED, CLAIMED, *extra), alignment=("Evil", 1)),
                 c('"Chivarro has been on the quartermaster\'s bench for days. Ask her."', requires=(CH_IN,),
                   flags=(RET_M, PALM, MIN_IN, STARTED, REUNITED, *extra)))
    return [*varied("wake", mg, text, WAKE_VARIANTS, decisions), CLAIMED_NODE]


KNIFE = ('[Put the knife in her hand] "\'Spill the blood of the one who caused you to fail.\' Go on. I\'ll hold it for you."',)
physical(P + "minagho_dead.brand", "Technically, she did it", "Minagho", PRES_MIN, MIN_UNIT, [
    nar("start", '''{n}Baphomet's servants kept their word to the letter. At dawn the watch found Minagho propped against the door of the quartermaster's stores, below the citadel, the way a merchant props a sample in a shop door. Nobody has dared to move her. Her head hangs. The bar across the door has been lifted off and laid neatly on the step.{/n}
{n}The mark on her brow is wet. The dead do not bleed.{/n}''',
        c(KNIFE[0], "wake", alignment=("Chaotic", 1), crusade=("Favors", -100)),
        c('"Not yet."', abort=True)),
    *wake_nodes(WAKE),
], requires=("trickster.ever", "minagho.dead", PRIMED, TERMS, DELIVERED), forbids=(RET_M, DECL_M),
   TricksterDevice=True, TricksterState="minagho_dead")
letter(P + "minagho_dead.brand_letter", "Technically, she did it", [
    nar("start", '''{n}The watch reported it at dawn, and nobody would say it twice: Minagho had been left propped against a door below the citadel, head hanging, the way a merchant props a sample in a shop door. The mark on her brow was wet. The dead do not bleed. You went down alone, with a knife.{/n}''',
        c(KNIFE[0], "wake", alignment=("Chaotic", 1), crusade=("Favors", -100)),
        c('"Not yet."', abort=True)),
    *wake_nodes(WAKE),
], requires=("trickster.ever", "minagho.dead", PRIMED, TERMS, DELIVERED, PRES_MIN + ".failed"),
   forbids=(RET_M, DECL_M, P + "minagho_dead.brand"), delay=96, TricksterDevice=True, TricksterState="minagho_dead")

# 5.4 Dead, no bargain: his collectors bring the corpse as bait, and the price is his own iron.
IRON = (c('[Hold out your palm to the iron] "Brand me, then. Properly, this time. And leave the bundle."', "iron",
          alignment=("Evil", 1), crusade=("Favors", -150)),
        c('"Hang them at the gate. Iron, bundle and all."', flags=(MET, DECL_M), alignment=("Lawful", 1)))
letter(P + "minagho_dead.collateral", "What the ledger says", [
    *varied("gate", nar, '''{n}Three cultists of the Lord of Beasts are taken at the eastern gate of Drezen with branding irons wrapped in oilcloth, a list with one name on it, yours, and a long bundle that bleeds through the canvas. The dead do not bleed.{/n}
{n}The captain of the gate asks, very carefully, what should be done with them.{/n}''',
            [("gate_refused", nar, '''{n}The list is headed, in a hand that is not a cultist's: "The debtor declined the gift. Deliver it anyway."{/n}''',
              REFUSED_B)], IRON),
    nar("iron", '''{n}The iron is cold, and then it is not. Half the gate watch sees their Commander take the Goat's seal on an open hand without a sound. The other half will hear about it by supper.{/n}
{n}The cultists leave the bundle and go, walking backwards.{/n}''',
        c("[Carry her in. Close her fingers on the knife.]", "wake", flags=(BRANDED, DELIVERED, TERMS))),
    *wake_nodes(WAKE_BRANDED, (MET,)),
], requires=("trickster.ever", "minagho.dead", DEBT, "baphomet.parley.latched"), forbids=(TERMS, RET_M, DECL_M, MET), delay=48,
   TricksterDevice=True, TricksterState="minagho_dead")

# 5.5 Spared: the brand stopped bleeding on her, and she has come to see the thief's hand.
SPARED_OPEN = (
    c('[Show her your palm] "Look at your fingers. It stopped the moment I opened my mouth in that cell. It bleeds on me now. Mornings, mostly."', "terms", requires=(PRIMED,)),
    c('[Cut your palm and say the terms over it] "\'Until she spills the blood of the one who caused her to fail.\' That\'s me. Watch."',
      "terms", requires=("trickster",), forbids=(PRIMED,), flags=(PRIMED, DEBT, LATE_CLAIM), mythic="Trickster",
      crusade=("Favors", -100)))
SPARED_TERMS = mg("terms", '''"What kind of idiot lets their enemy slip away? And what kind of idiot puts their own name in a demon lord's ledger?" {n}She touches the mark. It stays dry.{/n}
"Baphomet will want the thief's name. I could buy my life back with yours, Golarian. Give me one reason I shouldn't."''',
    c('"Because it\'s my name on the brand now. Kill me, and you\'re bleeding again by supper."', flags=(MIN_IN, STARTED)),
    c('[Intimidate] "Because I\'d come back. Ask around. I do that."', flags=(MIN_IN, STARTED), alignment=("Chaotic", 1)),
    c('"Chivarro is on the quartermaster\'s bench. Give her the reason."', requires=(CH_IN,), flags=(MIN_IN, STARTED, REUNITED)),
    c('"No reason. Go, and keep your face dry."', flags=(DECL_M,)))
physical(P + "spared.brand", "It stopped bleeding", "Minagho", PRES_SPARED, MIN_UNIT, [
    *varied("start", mg, '''{n}She has taken one of the crusade's daggers off the quartermaster's rack and is sitting on a crate with it across her knees. Nobody saw her come through Drezen. That is the point.{/n}
"You let me go. Nobody lets me go. So either you are a fool, or you have a use for me, and I came to find out which before the Goat's collectors find me first." {n}She touches the mark on her brow and looks at her fingertips, and does not tell you what she sees there.{/n}''',
            [("terrified", mg, '"I ran from you in that cursed cell. I kept running until I could not. I am tired of running from you, Golarian."', "minagho.terrified")],
            SPARED_OPEN),
    SPARED_TERMS,
], requires=("trickster.ever", "minagho.spared.latched"), RequiresAnyGroups=[[PRIMED, "trickster"]], forbids=("minagho.dead", DECL_M),
   TricksterDevice=True, TricksterState="minagho_alive")
letter(P + "spared.brand_letter", "It stopped bleeding", [
    mg("start", '''{n}The note is pinned to your pillow with one of your own daggers.{/n}
"You let me go. Nobody lets me go. I could buy my life back with yours, Golarian. Give me one reason I shouldn't, and give it to my face."''',
       c('"Because it\'s my name on the brand now. Come and see."', flags=(MIN_IN, STARTED, DEBT), requires=(PRIMED,)),
       c('"No reason. Stay away, and keep your face dry."', flags=(DECL_M,), requires=(PRIMED,)),
       c('[Go down to her yourself, with a knife.]', "late", forbids=(PRIMED,), mythic="Trickster"),
       c('"No reason. Stay away."', flags=(DECL_M,), forbids=(PRIMED,))),
    nar("late", '''{n}The dagger's hilt is scratched with a place below the citadel, and you go there alone, at night. She is waiting with her back to a wall, the mark on her brow wet and running into her collar, and her hand on the dagger's twin.{/n}
{n}You cut your palm in front of her and say the Goat's own terms over it, "until she spills the blood of the one who caused her to fail", and name yourself the failure of Kenabres, and hold the hand out. She stares at it. Then she wipes her brow with two fingers, and looks at them, and they come away dry.{/n}
"...What did you *do*?"''',
        c('"Put my name in his ledger. It bleeds on me now. Come and see."', flags=(PRIMED, DEBT, LATE_CLAIM, MIN_IN, STARTED),
          crusade=("Favors", -100))),
    ],
   requires=("trickster.ever", "minagho.spared.latched", PRES_SPARED + ".failed"), RequiresAnyGroups=[[PRIMED, "trickster"]],
   forbids=("minagho.dead", DECL_M, P + "spared.brand"), delay=96, TricksterDevice=True, TricksterState="minagho_alive")

# 5.6 The collectors: optional, physical only, never twice (pursuers_met). One scene per Minagho presence.
COLLECTOR_CHOICES = (
    c('"Give them to Minagho."', "minagho", flags=(MET, GIVEN), alignment=("Evil", 1)),
    c('"Hang them at the gate. Iron and all."', flags=(MET,), alignment=("Lawful", 1)),
    c('[Play a nice trick on the cultists] "Send them back. Stamp the list: \'Paid. See palm.\'"', "stamp",
      flags=(MET, P + "pursuers_mocked", RECEIPT), mythic="Trickster", crusade=("Favors", -100)))
COLLECTORS = [
    *varied("start", mg, '''{n}Three cultists of the Lord of Beasts are taken at the eastern gate with branding irons wrapped in oilcloth and a list of one name. Yours. The watch drags them to the quartermaster's yard to be counted. Minagho reads the list over your shoulder and smiles with all her teeth.{/n}''',
            [("irons", nar, "{n}The irons are small. They are sized for a palm. Whoever sent them knew the way to your door.{/n}", TERMS)],
            COLLECTOR_CHOICES),
    mg("minagho", '''"Oh, you *do* know how to make a demon feel welcome." {n}She does not hurry. You hear them for most of the night.{/n}''',
       c("[Leave her to it.]")),
    mg("stamp", '''"A receipt. To *him*." {n}She watches the carts go with something that is almost respect and almost fear.{/n} "He keeps receipts, Golarian. Forever."''',
       c("[Let the carts go.]")),
]
physical(P + "debt.collectors", "What the ledger says", "Minagho", PRES_MIN, MIN_UNIT, COLLECTORS,
         requires=("trickster.ever", DEBT, MIN_IN, RET_M), forbids=(MET, CLOSED), delay=120)
physical(P + "debt.collectors_spared", "What the ledger says", "Minagho", PRES_SPARED, MIN_UNIT, copy.deepcopy(COLLECTORS),
         requires=("trickster.ever", DEBT, MIN_IN, "minagho.spared.latched"),
         forbids=(MET, CLOSED, "minagho.dead", P + "debt.collectors"), delay=120)


# === Chivarro: through the wrong wardrobe (F01) and the house always collects (F24) =================================

SHOVE = '[Shove Chivarro into the linen press] "Every wardrobe in this house belongs to a demon who owes me. Get in. Mind the corsets."'
REUNION_OPEN = (
    c(SHOVE, "press", forbids=("closets.door_kept",), flags=(SOCOTH, STARTED), mythic="Trickster", alignment=("Chaotic", 1)),
    c(SHOVE, "press", requires=("closets.door_kept",), flags=(DOOR, STARTED), mythic="Trickster", alignment=("Chaotic", 1)),
    c('"Wrong wardrobe. Sorry."', abort=True))
letter(P + "reunion.wardrobe", "Through the wrong wardrobe", [
    *varied("start", nar, '''{n}The wardrobe in your quarters has a back. You have checked. Tonight you step into it anyway, and step out between shelves of folded silk that smell of incense and old sin.{/n}''',
            [("door", nar, "{n}Socothbenoth is gone, and his closet is still yours. It opens only on rooms you have stood in, and it will not open on this room a second time.{/n}",
              "closets.door_kept")],
            (c("Continue", "silk"),)),
    *varied("silk", cv, '''{n}Chivarro is standing in front of the linen press with a dagger in one hand and a candle in the other. Her eyeless face turns to you as if you were a draught from a window she had nailed shut.{/n}
"You."''',
            [("cellar", cv, "{n}It is not her silk. The shelves belong to a Lower City cellar, and the press is full of other people's laundry. She has come down in the world, and she knows exactly who to thank for it.{/n} \"Come to finish Herrax's errand?\"",
              CELLAR),
             ("fought", cv, '"The one who would not die quietly."', "chivarro.fought_commander")],
            REUNION_OPEN),
    cv("press", '''{n}The linen press should be two feet deep. It is not. It smells of lavender, then of mildew, then of the pine chest at the foot of your bed in Drezen.{/n}
"A linen press. I have climbed out of a *linen press*, honey, into a crusader's bedroom." {n}The smile stays on her lips. Nothing else on her face agrees with it.{/n} "If this is a seduction, it is utterly trite. If it is a joke, I will have your hide for tablecloths."''',
       c('"Ask her which one it is."', "which", requires=(MIN_IN,)),
       c('"She\'s not here. That\'s the other half of the joke."', "alone", forbids=(MIN_IN,))),
    *varied("which", cv, '''{n}Minagho is sitting on your bed. Chivarro looks at her for a long moment, and then at you, and decides something.{/n}
"One night. I take her side of the bed, she takes the other, and you, Golarian, sleep in the corridor. If she wants me gone by morning, I go back through your cupboard, and you will never find the press again."''',
            [("which_debt", cv, '"She says you *own* her debt. Then you and I will discuss the price of her, later, with knives."', CLAIMED)],
            (c('"The corridor it is."', flags=(REUNITED, CH_IN)),
             c('"No. Back through the press, both of your terms with you."', flags=(SENT_BACK,)))),
    cv("alone", '''{n}She looks at your empty bed for a long time.{/n} "Then what am I doing in your bedroom, Golarian?"
"If you killed her, say so now, while I still have the dagger. If you let her die, say that instead. It is the same answer, but I like to know how you lie."''',
       c('"I\'m working on it. She\'s still owed."', flags=(CH_IN, WAITING)),
       c('"Then go back. I\'ll knock when she\'s breathing."', flags=(SENT_BACK,))),
], requires=("trickster", "trickster.ever", "closets.known"),
   forbids=(REUNITED, CH_IN, "chivarro.searching", "chivarro.dead", RET_C, SENT_BACK), delay=0,
   TricksterDevice=True, TricksterState="chivarro_alive")

# 5.2 Killed: a deposit on Herrax's own hub, the moment she asks for the kill (C8).
SCENES.append(scene(P + "chivarro_dead.deposit", "The house special", "Herrax", 4, '"About Chivarro. Before I go looking."', [
    hx("start", '''{n}Herrax lifts one scarred brow.{/n} "Cold feet, lover? She's a bitch in a cellar. It's hardly a siege."''',
       c('[Put a deposit on the house special] "You want her gone forever? Then sell her to me, and send her double down to that cellar to die in her place. Write it down: \'One Chivarro, forever.\' I\'m paying in advance."',
         "ink", mythic="Trickster"),
       c('"Forget I asked."', abort=True)),
    hx("ink", '''"Paying for a corpse before it's a corpse?" {n}She counts something behind her eyes, and whatever the sum is, it pleases her.{/n} "Oh, lover. You've read my menu. Of course there's a Chivarro on it: Sael, my prettiest boy, who wears her face for the guests who could never afford the original. He does her voice better than she does these days."
"So. Tonight my boys lift the real one out of her cellar and into mine, and Sael goes down in her rings and her scent to wait for you. You go in, and you kill him, and the whole Lower City hears that Chivarro died at a crusader's hand. Dead to the city, gone from it forever, in a mortal's pocket: that's everything I asked you for, and I get paid twice." {n}She writes the line herself and blows on the ink.{/n} "He won't know what he's for until the knife. That's the part you're buying. My boys take the house's proof from every job: the rings, and whatever the rings are on. And the price is a favour. When I call. You won't ask what."''',
       c('"Put it on my bill."', flags=(DEPOSIT, FAVOR, DOUBLE), alignment=("Evil", 1)),
       c('"No. No favours with no name."', abort=True)),
], requires=("trickster", "herrax.asked_kill_chivarro"), forbids=("chivarro.dead", "chivarro.searching", DEPOSIT), last=4,
   optional=True, Relationship=REL, AnswerLists=[HERRAX_LIST], NativeReturnCue=HERRAX_RETURN,
   TricksterDevice=True, TricksterState="chivarro_dead"))

letter(P + "chivarro_dead.bought", "The house always collects", [
    *varied("start", hx, '''{n}The letter smells of the Delights: incense, coin and something under both. The hand is round and unhurried.{/n}
"Honey. It went as ordered. The Lower City watched Chivarro die at a crusader's hand, and my tray has her rings to prove it, with Sael's fingers still in them. He did her voice to the very end, poor lamb, and never knew. The real one has been in my cellar since the night before you went down, breathing, furious, and dead in law. What will it be?"
{n}Pinned under the letter is a scrap in another hand, sharp and slanted and shaking:{/n} "If you buy me, buy all of it. A woman with no name in her own city, no house, no chair, and the part of me that will hate you for the receipt. You killed a boy wearing my face to get me. I will not be grateful. I will be *priced*."''',
            [("told", hx, '"Everyone thinks she is dead, lover. You told me so yourself, with his blood still on your sleeve. We are both liars, and now you want to collect the lie. I *adore* you."',
              "herrax.told_chivarro_dead")],
            (c('[Order from the house menu] "One Chivarro. Forever. My pockets are deep enough."', "paid", requires=(DEPOSIT,),
               mythic="Trickster"),
             c('[Order from the house menu] "One Chivarro. Forever. My pockets are deep enough. Write it now; I\'ll sign."', "late",
               requires=("trickster",), forbids=(DEPOSIT,), mythic="Trickster"),
             c('"Nothing. Keep her. Let the dead stay dead."', flags=(DECL_C,)))),
    hx("paid", '''"'One Chivarro, forever. Deposit paid.' My own hand, lover. I laughed while I wrote it. I stopped laughing when my clerk read it back and I understood you'd meant every word of it, the boy included. My house does not deliver short on a paid order." {n}Under it, in the same round hand: "Out-lawyered in my own house. I adore you. Delivered, less the proof."{/n}
"The favour stands. When I call."''',
       c('"Deal."', "sale", alignment=("Evil", 1))),
    hx("late", '''{n}The next page is the order, written while the ink on the first was still wet: "One Chivarro, forever." Your name is waiting for its signature.{/n}
"Nobody ordered her forever in time, lover, so I kept her breathing for whoever would bid the most. That is you, now. Late orders cost double: two favours. And a month of feeding stock nobody had paid for is not free: three hundred in crusade script, and a writ for the rest."''',
       c('"Deal. Both favours."', "sale", flags=(FAVOR, LATE), alignment=("Evil", 1), crusade=("Finances", -300)),
       c('"Too rich. Leave her dead."', flags=(DECL_C,))),
    cv("sale", '''{n}The last page is in another hand, sharp and slanted, written by someone who has had a month in the dark with nothing to do but compose it.{/n}
"Sold. In my own house. To *you*. Under 'goods'." {n}The pen has gone through the paper twice.{/n}
"Here is my price, since nobody asked it. The bill. Burn it, and I come to Drezen owing you nothing and hating you for the favour. Keep it, and I come anyway, and you sleep with one eye open for the rest of your short life."''',
       c('[Burn the bill] "Nothing. Get dressed."', flags=(RET_C, CH_IN, BURNED, STARTED), alignment=("Chaotic", 1), forbids=(MIN_IN,)),
       c('[Burn the bill] "Nothing. Get dressed. Minagho hates waiting."', requires=(MIN_IN,),
         flags=(RET_C, CH_IN, BURNED, STARTED, REUNITED), alignment=("Chaotic", 1)),
       c('[Keep the bill] "Everything. And now I own it."', flags=(RET_C, CH_IN, OWNED), alignment=("Evil", 2))),
], requires=("trickster.ever", "chivarro.dead", "chivarro.dead.latched", DEPOSIT),
   forbids=(RET_C, DECL_C), delay=48, owner="Herrax", TricksterDevice=True, TricksterState="chivarro_dead")

household.secret("chivarro_double", "The boy in her rings",
                 "Herrax sold me Chivarro's double before I went down to kill her: Sael, an incubus of the Delights who "
                 "wore her face for guests who could not afford her. He went into her cellar in her rings, and I killed "
                 "him there, knowing, so that the Lower City would bury her and I could buy her. He never knew what he "
                 "was for. The house still has his fingers on its tray.", portrait="Chivarro", witnesses=(), risk="medium")


# The bill: an owned Chivarro refuses to be courted by the hand that holds her receipt. Nothing of the pair moves until
# it is burned; keeping it is service, never romance (coercion is never consent).
UNOWNED = {OWNED: BURNED}   # ForbidOverrides: an owned Chivarro counts only once the bill is burned
physical(P + "chivarro_dead.the_bill", "Goods", "Chivarro", PRES_CHIV, CHIV_UNIT, [
    cv("start", '''{n}Chivarro is on the quartermaster's bench in borrowed wool, sitting very straight, with a folded paper on her knee. You know the paper. You signed it.{/n}
"Let us be clear, you and I, before you say anything sweet." {n}She unfolds it. "One Chivarro, forever." Your signature. Her own house's seal.{/n} "I am goods. Goods do not take lovers, and they do not keep houses, and they do not say yes. They are used, or they are sold on." {n}She holds it out to you between two fingers.{/n} "So. Which of those am I?"''',
       c('[Burn the bill] "Neither. Watch."', "burned", alignment=("Chaotic", 1)),
       c('[Keep the bill] "Mine. That\'s what you are."', "kept", alignment=("Evil", 1))),
    cv("burned", '''{n}She watches the paper curl in the quartermaster's brazier. She does not thank you. She waits until the last corner of "goods" has gone black, and then she breathes out, very slowly, through her teeth.{/n}
"Late. But burned." {n}She stands, and she is taller than she was a moment ago.{/n} "Now I owe you nothing, honey, and you owe me a great deal. Let us see what you do with that."''',
       c("[Let her go.]", flags=(BURNED, STARTED, P + "cost.bill_answered"), forbids=(MIN_IN,)),
       c("[Let her go to Minagho.]", flags=(BURNED, STARTED, P + "cost.bill_answered", REUNITED), requires=(MIN_IN,))),
    cv("kept", '''{n}She folds the bill again, carefully, and gives it back to you, and her fingers do not touch yours.{/n} "Then I stay. Owned. On paper, in your city, at your door. Do not ever mistake it for anything else, and do not ever come to my bed with it in your pocket. I would take the hand that holds it."''',
       c("[Pocket the bill.]", flags=(KEPT, P + "cost.bill_answered"))),
], requires=("trickster.ever", RET_C, OWNED), forbids=(BURNED, KEPT, CLOSED), delay=24,
   TricksterDevice=True, TricksterState="chivarro_dead")
letter(P + "chivarro_dead.the_bill_letter", "Goods", [
    cv("start", '''{n}The bill comes back to you folded around a note in a sharp, slanted hand.{/n} "I am goods. Goods do not take lovers, and they do not say yes. They are used, or they are sold on. Which of those am I? Answer with the bill."''',
       c("[Burn it and send her the ashes.]", flags=(BURNED, STARTED, P + "cost.bill_answered"), alignment=("Chaotic", 1), forbids=(MIN_IN,)),
       c("[Keep it.]", flags=(KEPT, P + "cost.bill_answered"), alignment=("Evil", 1)),
       c("[Burn it, and send her the ashes and Minagho's direction.]", flags=(BURNED, STARTED, P + "cost.bill_answered", REUNITED),
         alignment=("Chaotic", 1), requires=(MIN_IN,)))],
   requires=("trickster.ever", RET_C, OWNED, PRES_CHIV + ".failed"), forbids=(BURNED, KEPT, CLOSED, P + "chivarro_dead.the_bill"),
   delay=96, TricksterDevice=True, TricksterState="chivarro_dead")


# === The pair's Trickster chain (a Trickster variant of the registered visits, which stay untouched) =================

CHAIN_FORBIDS = (CLOSED, "minagho.dead", "chivarro.dead")
letter(P + "after.what_the_offer_bought", "What the offer bought", varied("start", cv,
    '''"There is a buyer. There is always a buyer. A marilith in the Lower City wants the two lilitu who walked out of Baphomet's ledger and Herrax's, and she has sent a list of what she would pay." {n}Minagho's hand, under Chivarro's, in a harder script:{/n} "She would pay less than you did. Tell us what to do with it, Golarian. We want to see what you say."''',
    [("receipt", cv, "{n}Chivarro, in the margin:{/n} \"The receipt you burned is the only one of its kind. The marilith has asked for a copy.\"",
      BURNED)],
    (c('"Take the buyer\'s list. Sell it back to her."', flags=(T_OFFER, P + "offer_sold_back"), alignment=("Evil", 1)),
     c('"Burn the list. Let them come."', flags=(T_OFFER, P + "offer_burned")))),
    requires=("trickster.ever", REUNITED), forbids=(*CHAIN_FORBIDS, T_OFFER, HALF, OWNED), ForbidOverrides={**PAIR_FO, **UNOWNED})

PRICE_NODES = [
    *varied("start", cv, '''{n}Chivarro is waiting for you by the quartermaster's stores, in borrowed Drezen wool that she wears like a costume.{/n}
"Minagho says you own her debt. Then you and I will discuss the price of her. What is her name worth to you, Golarian?"''',
            [("owned", cv, '"You bought me, on paper, and burned the paper. Her you only bled for. Which purchase do you think I remember longer?"', OWNED),
             ("given", cv, '"You gave her three cultists for supper. I have never seen her so pleased. It was disgusting."', GIVEN)],
            (c('"Name it."', "price"), c('"It\'s worth a joke. Most things are."', "walk"))),
    cv("price", '''"Your hand. The bleeding one. Open, on the table, in front of both of us, while I tell you exactly what I think of your trick. Do not close it until I am finished."''',
       c("[Open your palm on the table] \"There. Say what you think of my trick. I'll hold still.\"", "verdict"),
       c('"No. My hand stays shut."', "walk")),
    cv("verdict", '''{n}She takes her time. She tells you that the trick was vulgar, that the wardrobe was worse, that she has been rescued by better and bought by richer. Minagho, beside her, adds three things Chivarro forgot. Your palm opens at the old cut and bleeds onto the quartermaster's ledger, and neither of them lets you close it.{/n}
"There." {n}Chivarro folds your fingers shut herself, one at a time.{/n} "Now it is worth something."''',
       c("[Keep your hand where she put it.]", flags=(T_NAME, PALM_TABLE))),
    cv("walk", '''"Then it is worth nothing, and so is your bedroom." {n}She is gone before you finish your next sentence. The quartermaster pretends very hard that he did not see a lilitu walk out of his stores.{/n}''',
       c("[Let her go.]", flags=(WALKED,))),
]
physical(P + "after.the_price_of_her_name", "The price of her name", "Chivarro", PRES_CHIV, CHIV_UNIT, PRICE_NODES,
         requires=("trickster.ever", T_OFFER, CH_IN), forbids=(*CHAIN_FORBIDS, T_NAME, WALKED, OWNED), ForbidOverrides={**PAIR_FO, **UNOWNED})
letter(P + "after.the_price_of_her_name_letter", "The price of her name", [
    cv("start", '''{n}The note is written on the back of the quartermaster's inventory, in a sharp, slanted hand.{/n}
"Minagho says you own her debt. Then you and I will discuss the price of her. What is her name worth to you, Golarian? Answer with your hand. The bleeding one. Pressed to the page."''',
       c("[Press your bleeding palm to the page.]", flags=(T_NAME, PALM_TABLE)),
       c('"It\'s worth a joke."', flags=(WALKED,)))],
   requires=("trickster.ever", T_OFFER, CH_IN, PRES_CHIV + ".failed"),
   forbids=(*CHAIN_FORBIDS, T_NAME, WALKED, OWNED, P + "after.the_price_of_her_name"), delay=96,
   ForbidOverrides={**PAIR_FO, **UNOWNED})

letter(P + "after.won_back", "Won back", [
    nar("start", '''{n}Chivarro has taken a room at the far end of Drezen, as far below the citadel as the walls allow, and paid for it with a ring nobody saw her wear. She has not come back. She has also not left Drezen.{/n}''',
        c('[Send the silk] "A bolt of Nerosyan silk, dyed Delights red, and a card: \'Your price. Name it again.\'"', "answer",
          crusade=("Finances", -200)),
        c('"Let her stay gone."', flags=(SENT_BACK,))),
    cv("answer", '''{n}The card comes back the next morning, pinned to your door with a hatpin. On the back, in her hand:{/n} "Red. You remembered. It is still not enough." {n}Under it, smaller:{/n} "Tomorrow. Bring the hand."''',
       c("[Go, tomorrow, and bring the hand.]", "hand")),
    nar("hand", '''{n}Her room at the far end of Drezen has one chair, and she is in it. The bolt of red silk is draped over the bed, unopened, like a guest she has not decided to receive. She points at the table. You put your hand on it, palm up, and the old cut opens as if it had been waiting for her.{/n}
{n}She tells you, at length and without raising her voice, exactly what the wardrobe cost her, and the walk-out, and the three days she spent in this room listening for your knock and despising herself for listening. Your palm bleeds onto her table the whole time. When she has finished she folds your fingers shut herself, one at a time.{/n} "Now it is worth something," she says. "Go home. I will come back to the bench when I choose, and I choose tomorrow."''',
        c("[Keep your hand where she put it.]", flags=(T_NAME, WON_BACK, PALM_TABLE))),
], requires=("trickster.ever", WALKED, CH_IN), forbids=(*CHAIN_FORBIDS, T_NAME, OWNED), ForbidOverrides={**PAIR_FO, **UNOWNED})

letter(P + "after.who_keeps_the_house", "Who keeps the house", varied("start", mg,
    '''"We are going to need a house, when your war is done. Somewhere with thick doors and a cellar nobody else knows about." {n}Chivarro, in the margin:{/n} "And a linen press. For guests."''',
    [("door", cv, '{n}Chivarro adds, lower down:{/n} "Your kept door opens on my old house some nights now. I hear the music through it. Brick it up, or give it to us."',
      DOOR)],
    (c('"Chivarro keeps the house. Minagho keeps the door."', flags=(T_HOUSE, "minachiv.host_ending")),
     c('"Neither. You keep each other, and I keep out of it."', flags=(T_HOUSE, "minachiv.winter_ending")))),
    requires=("trickster.ever", T_NAME), forbids=(*CHAIN_FORBIDS, T_HOUSE, OWNED), ForbidOverrides={**PAIR_FO, **UNOWNED})

# 5.4 The commit: their terms, her refusal on every branch, and the heat to the cut.
PAIR_THRESHOLD = nar("threshold", '''{n}They take you up to your own quarters between them, one on each arm, arguing across you the whole way about which of them the stairs were built for.{/n}
{n}At the door Chivarro stops arguing. She unbuckles your sword belt without looking at it, the way a woman who has undressed a thousand guests knows every buckle ever forged. Minagho is slower and less kind; she drags her nails down the seam of your shirt and watches your face instead of her hands, learning where you flinch. Two mouths, one warm and one fever-hot, and somewhere between them the bleeding palm is lifted and kissed, and licked clean, and pressed flat against a bare hip that is not yours.{/n}
{n}"I have sold ten thousand nights, honey," Chivarro says against your throat, in the voice of a woman closing on a price she means to get. "Every one of them for someone else. This one I am taking for myself, and I intend to get my money's worth, so do not you dare be ordinary." Then, lower: "Our terms. Say it again." You say it again. Minagho laughs, low and ugly and delighted, and pulls you both down onto the bed.{/n}''',
    c("Continue", flags=(NIGHT_PAIR,)))
COMMIT_FORBIDS = (CLOSED, COMPLETE, DECLINED, KEPT, OWNED, *CHAIN_FORBIDS)
COMMIT_NODES = [
    mg("start", '''{n}They have taken the bench outside the quartermaster's stores as if they had owned it for years and you were the one passing through: Chivarro stretched along it, Minagho sitting on its back with her boots on the seat.{/n}
"We have been talking about you, Golarian. We do that now. It is very tiresome." {n}Chivarro, without looking up:{/n} "Ask the question, honey. We have a wager on how badly you phrase it."''',
       c('"Stay. Both of you. On your terms."', "terms"),
       c('[Tell them it was a joke that worked] "You\'re both on my ledger now. That\'s all this ever was."', "refuse")),
    cv("terms", '''"Our terms. We keep our own house. We keep our own names. You visit when you are asked, and you are asked rarely." {n}Minagho:{/n} "And when the Goat calls in his seal, you do not bargain for me again. I will stand where I choose."''',
       c('"Your terms. Agreed."', "threshold", flags=(COMPLETE, "minachiv.future_two", CHAIN)),
       c('"I won\'t bleed for the Goat forever."', "refuse")),
    mg("refuse", '''"No." {n}Minagho stands.{/n} "Not while his seal still bleeds on your hand and you still call it a joke. We are demons, Golarian. We do not stay for jokes. Ask me when it scars."''',
       c('"Then I\'ll ask again when it scars."', flags=(DECLINED,)),
       c('"Then get out of my city. Both of you."', flags=(CLOSED,))),
    PAIR_THRESHOLD,
]
physical(P + "after.before_the_last_road", "Before the last road", "Minagho", PRES_CHIV, CHIV_UNIT, COMMIT_NODES,
         requires=("trickster.ever", T_HOUSE, MIN_IN, CH_IN), forbids=COMMIT_FORBIDS, ForbidOverrides={**PAIR_FO, **UNOWNED})
letter(P + "after.before_the_last_road_letter", "Before the last road", [
    mg("start", '''{n}The letter is in two hands, taking turns, and the ink changes colour wherever one of them snatched the pen.{/n}
"We have been talking about you. Our terms: we keep our own house, we keep our own names, you visit when you are asked. And when the Goat calls in his seal, you do not bargain for me again." {n}Chivarro, below:{/n} "Answer in ink, honey. We will know if you blot it."''',
       c('"Your terms. Agreed."', "came", flags=(COMPLETE, "minachiv.future_two", CHAIN)),
       c('"Then I\'ll ask again when it scars."', flags=(DECLINED,)),
       c('"Get out of my city."', flags=(CLOSED,))),
    nar("came", '''{n}You write two words and send the runner down before the ink is dry. They come up at midnight, through the door, not the wardrobe, and nobody on the stair is fool enough to ask where they are going.{/n}
{n}Chivarro takes the letter off your desk, reads your two words aloud as if pricing them, and drops it in the grate. Minagho does not bother with reading. She has your shirt open before the paper catches, her nails dragging down your ribs, and Chivarro, behind you, unbuckles your belt with a madam's quick, bored fingers and lets it fall. "Ink," Minagho says against your mouth, walking you back towards the bed. "You answered us in *ink*." Then the backs of your knees meet the mattress, and they bear you down onto it between them, Chivarro already astride you and Minagho's teeth at your throat.{/n}''',
        c("Continue", "morning", flags=(NIGHT_PAIR,))),
    nar("morning", '''{n}In the morning the grate is cold and the letter is ash, and both of them are still there, which neither will admit was a decision. Chivarro leaves a bill on the pillow for the night, itemised, with a kiss printed on the total. Minagho binds your palm when it opens at dawn, too tightly, and tells you that next time you will come down to the stores yourself, like someone who means it.{/n}''',
        c("[Pay the bill.]", flags=(MORNING,)))],
   requires=("trickster.ever", T_HOUSE, MIN_IN, CH_IN, PRES_CHIV + ".failed"),
   forbids=(*COMMIT_FORBIDS, P + "after.before_the_last_road"), delay=96, ForbidOverrides={**PAIR_FO, **UNOWNED})

# 5.5 Alone commits: each woman can be won without the other. Devices: the partner's unreturned death may hold.
ALONE_CHIV_NODES = [
    cv("start", '''"She is not coming, or she is not coming yet. I have stopped waiting to find out which." {n}She has taken over the quartermaster's counter; Wilcer Garms has taken refuge behind his own ledgers.{/n} "So. What am I, in Drezen, without her?"''',
       c('"Stay anyway. Keep the house with me instead."', "terms"),
       c('"Go back through the press. There\'s nothing here for you."', flags=(CLOSED,))),
    cv("terms", '''"Then I keep my own house, in your city, on my terms, and you pay the rent. If she walks back in, the terms change, and you do not get a say."''',
       c('"Your terms."', "threshold", flags=(COMPLETE, "minachiv.future_chivarro", HALF, CHAIN), requires=(DEBT,)),
       c('"Not those terms."', "refuse"),
       c('"Your terms."', "threshold_clean", flags=(COMPLETE, "minachiv.future_chivarro", HALF, CHAIN), forbids=(DEBT,))),
    cv("refuse", '''"Then wait. You are good at making demons wait."''',
       c('"Then wait. I\'ll ask again."', flags=(DECLINED,))),
    nar("threshold", '''{n}She does not take you to your quarters. She takes you to hers, a rented room above a chandler's shop below the citadel, and bars the door with a chair, and turns.{/n}
{n}"Rent," she says, and holds out her hand. When you put yours in it she does not take it; she inspects it, turns it palm up, runs one nail along the old cut until you draw breath, and smiles at the sound as if she has just been quoted a price she likes. Then she undresses you the way she once dressed the Delights' best rooms: without hurry, piece by piece, setting each thing exactly where she wants it. Her own gown she leaves for last and lets fall without ceremony, because she knows precisely what it costs you to watch.{/n}
{n}"Ten thousand nights I sold," she murmurs, walking you backwards to a bed too narrow for anything she has in mind. "This one is mine, and I am going to collect every copper of it." She pushes you down with two fingers, climbs astride you in one practiced motion, and leans down until her breath is on your mouth, and there, holding you exactly where she wants you, she stops talking.{/n}''',
        c("Continue", flags=(NIGHT_CHIV,))),
    nar("threshold_clean", '''{n}She does not take you to your quarters. She takes you to hers, a rented room above a chandler's shop below the citadel, and bars the door with a chair, and turns.{/n}
{n}"Rent," she says, and holds out her hand, and when you put a purse in it she weighs it without looking, drops it on the floor, and takes your hand instead. She undresses you the way she once dressed the Delights' best rooms: without hurry, piece by piece, setting each thing exactly where she wants it, and lets her own gown fall last, because she knows precisely what it costs you to watch.{/n}
{n}"A room of my own, in a crusader's city, and a tenant who pays," she murmurs, walking you backwards to a bed too narrow for anything she has in mind. "I have come down in the world. Let us see how far." She pushes you down with two fingers, climbs astride you in one practised motion, and leans down until her breath is on your mouth, and there, holding you exactly where she wants you, she stops talking.{/n}''',
        c("Continue", flags=(NIGHT_CHIV,))),
]
physical(P + "alone.chivarro", "The house she keeps now", "Chivarro", PRES_CHIV, CHIV_UNIT, ALONE_CHIV_NODES,
         requires=("trickster.ever", CH_IN), RequiresAnyGroups=[[DECL_M, WAITING]],
         forbids=(REUNITED, OWNED, CLOSED, COMPLETE, DECLINED), delay=96, ForbidOverrides=dict(UNOWNED),
         TricksterDevice=True, TricksterState="minagho_dead")
letter(P + "alone.chivarro_letter", "The house she keeps now", [
    cv("start", '''"She is not coming, or she is not coming yet. I have stopped waiting to find out which. So: I keep my own house, in your city, on my terms, and you pay the rent. If she walks back in, the terms change, and you do not get a say."''',
       c('"Your terms."', "came", flags=(COMPLETE, "minachiv.future_chivarro", HALF, CHAIN)),
       c('"Then wait. I\'ll ask again."', flags=(DECLINED,))),
    nar("came", '''{n}Her answer is an address below the citadel and an hour: tonight. The room above the chandler's shop is lit by one candle, and she is sitting on the end of the bed with the lease across her knees.{/n}
{n}"Sign," she says. You sign. She folds the lease, sets it on the candle-shelf where the wax cannot reach it, and only then stands and lets the gown slide from her shoulders to the floor, stepping out of it towards you the way she once walked the Delights' hall, knowing every eye in the room is on her. She takes your collar in both fists and falls back onto the bed, and pulls you down after her, and hooks one leg round yours so you cannot get up again.{/n}''',
        c("Continue", "morning", flags=(NIGHT_CHIV,))),
    nar("morning", '''{n}In the morning the rent is gone from your purse and there is a receipt in its place, in her hand, for "one night, paid in full, interest to follow". She is asleep across the whole of the bed, and does not wake when you go.{/n}''',
        c("[Keep the receipt.]", flags=(MORNING,)))],
   requires=("trickster.ever", CH_IN, PRES_CHIV + ".failed"), RequiresAnyGroups=[[DECL_M, WAITING]],
   forbids=(REUNITED, OWNED, CLOSED, COMPLETE, DECLINED, P + "alone.chivarro"), delay=96, ForbidOverrides=dict(UNOWNED),
   TricksterDevice=True, TricksterState="minagho_dead")

ALONE_MIN_NODES = [
    mg("start", '''"You keep looking at the gate as if someone else is coming through it." {n}She does not look at it herself.{/n}''',
       c('"She\'s in Herrax\'s cellar, and the house wants too much for her. Stay."', "terms", requires=("chivarro.dead.latched", DEPOSIT)),
       c('"She went back through the press. Stay."', "terms", forbids=("chivarro.dead.latched",)),
       c('"I killed her. You know I did. Stay anyway."', "killer", requires=("chivarro.dead.latched",), forbids=(DEPOSIT,))),
    mg("killer", '''"I know." {n}Her lip peels back from her teeth.{/n} "Herrax sang it all over the Lower City: the crusader who cut Chivarro down in her own cellar for a madam's favour. I heard it in Drezen before your blade was clean."
{n}She is very still.{/n} "I have killed for less. I have lain down with worse. I have not decided which of those you are, and I will take a very long time deciding, and you will feel every day of it."''',
       c("Continue", "terms")),
    mg("terms", '''"Stay. For a mortal who owns my debt and bleeds for it every morning." {n}Her lip curls.{/n} "My price: you never bargain for me again. Not with him, not with anyone."''',
       c('"Your price."', "threshold", flags=(COMPLETE, "minachiv.future_minagho", HALF, CHAIN)),
       c('"Not that price."', "refuse")),
    mg("refuse", '''"Then ask me when it scars, Golarian. Or do not ask at all."''',
       c('"Then I\'ll ask again when it scars."', flags=(DECLINED,)),
       c('"Then go. Dry."', flags=(CLOSED,))),
    nar("threshold", '''{n}She walks you back to your quarters as though she were the one escorting a prisoner, one hand fisted in the back of your collar. Inside she does not bother with the lamp.{/n}
{n}She finds the bleeding palm in the dark and holds it against her mouth, and you feel her smile against the cut before you feel her teeth. "Mine," she says, "for tonight. His, every morning after." Then she pushes you back against the door, hard enough to rattle the bar, and takes her time: her fingers at your throat, not squeezing, only reminding; her mouth hot and unkind along your jaw; her body pressed to yours from knee to shoulder so that you feel every breath she refuses to hurry. She strips your shirt off one-handed and throws it somewhere you will never find it.{/n}
{n}"On the bed," she says against your ear. "On your back. Hands where I can bite them." When you are where she wants you she follows you down, straddles your hips, pins both your wrists above your head with one of hers, and leans down until her hair falls across your face. There, at the very edge of it, she makes you wait one breath longer than you can bear, and smiles.{/n}''',
        c("Continue", flags=(NIGHT_MIN,))),
]
ALONE_MIN_GATE = [[DECL_C, SENT_BACK, "chivarro.dead.latched"]]
ALONE_MIN_FORBIDS = (REUNITED, RET_C, CH_IN, CLOSED, COMPLETE, DECLINED)
physical(P + "alone.minagho", "One lilitu, dry", "Minagho", PRES_MIN, MIN_UNIT, ALONE_MIN_NODES,
         requires=("trickster.ever", MIN_IN, RET_M), RequiresAnyGroups=ALONE_MIN_GATE, forbids=ALONE_MIN_FORBIDS, delay=96,
         TricksterDevice=True, TricksterState="chivarro_dead")
physical(P + "alone.minagho_spared", "One lilitu, dry", "Minagho", PRES_SPARED, MIN_UNIT, copy.deepcopy(ALONE_MIN_NODES),
         requires=("trickster.ever", MIN_IN, "minagho.spared.latched"), RequiresAnyGroups=ALONE_MIN_GATE,
         forbids=(*ALONE_MIN_FORBIDS, "minagho.dead", P + "alone.minagho"), delay=96,
         TricksterDevice=True, TricksterState="chivarro_dead")
letter(P + "alone.minagho_letter", "One lilitu, dry", [
    mg("start", '''"Stay, you said. For a mortal who owns my debt and bleeds for it every morning." {n}The hand is hard and very straight.{/n} "My price: you never bargain for me again. Not with him, not with anyone."''',
       c('"Your price."', "came", flags=(COMPLETE, "minachiv.future_minagho", HALF, CHAIN)),
       c('"Then I\'ll ask again when it scars."', flags=(DECLINED,))),
    nar("came", '''{n}She does not answer the letter. She answers the door, the same night: you open it and she is already on the other side of it, as if she had been standing there since she sent it.{/n}
{n}"Your price," she says, "paid," and comes in without waiting to be asked, and kicks the door shut behind her. She takes your bleeding hand, opens it, and presses her mouth to the cut until you feel her teeth; then she shoves you back against the bar of the door and strips your shirt over your head, and when you reach for her she catches both your wrists and walks you backwards to the bed, and pushes you down onto it, and climbs astride you with your wrists pinned in one of her hands.{/n}''',
        c("Continue", "morning", flags=(NIGHT_MIN,))),
    nar("morning", '''{n}At dawn your palm opens, as it does every dawn now. She is awake before it does, watching, and binds it with a strip of your own sheet, too tightly, without a word. When she goes, she takes the rest of the sheet with her.{/n}''',
        c("[Let her.]", flags=(MORNING,)))],
   requires=("trickster.ever", MIN_IN), RequiresAnyGroups=[*ALONE_MIN_GATE, [PRES_MIN + ".failed", PRES_SPARED + ".failed"]],
   forbids=(*ALONE_MIN_FORBIDS, P + "alone.minagho", P + "alone.minagho_spared"), delay=96,
   TricksterDevice=True, TricksterState="chivarro_dead")


# The priced second ask after a soft no (R2-1; Sol r2 INT). "Ask me when it scars": the Commander makes it scar, a week of
# mornings at the quartermaster's brazier; Chivarro's "Then wait" is waited out and paid in advance. Letters with narrated
# meetings, so they open whatever presence stands. A fresh refusal (closing the hand) is the permanent no.
SCARRED = P + "cost.scar_burned"
letter(P + "after.when_it_scars", "When it scars", [
    nar("start", '''{n}The palm does not scar. It will not; the Goat's seal opens it every dawn. So you make it scar. Seven mornings running you go down to the quartermaster's brazier before the stores open, heat the flat of a crusade knife until it whitens, and press it to the cut as it opens, until the line across your palm is a ridge of shining, puckered skin that still bleeds every dawn but is, now, unmistakably a scar. Wilcer Garms stops asking what the knife is for on the third morning. On the seventh you send the two of them one line, and the hand to prove it.{/n}''',
        c('[Hold up the scarred palm] "It scarred. Ask your question again, or I\'ll ask mine."', "pair", flags=(SCARRED,)),
        c("[Let it bleed a while longer.]", abort=True)),
    mg("pair", '''"You burned it." {n}Minagho takes your wrist and turns the hand to the light, and runs her thumb along the ridge, hard, until it opens and bleeds anyway.{/n} "It still bleeds. Of course it bleeds; it is his. But you made it scar in spite of him, one morning at a time, and you did not ask either of us to watch."
{n}Chivarro, from the bench:{/n} "I watched. From the stair. Every morning. It was disgusting, honey, and I have never been so flattered. Ask."''',
       c('"Stay. Both of you. On your terms."', "night", flags=(COMPLETE, "minachiv.future_two", CHAIN)),
       c('[Close the hand] "Forget I asked."', flags=(CLOSED,))),
    nar("night", '''{n}They do not take you to your quarters this time. They take you to theirs, the rooms below the citadel with the thick door, and Minagho bars it with her own back. Chivarro strips your gloves off first, one finger at a time, and kisses the burned palm as if she were sealing a contract with it; Minagho has your belt and shirt off before Chivarro has finished, and walks you backwards to the bed with her teeth at your ear. "On your back," Chivarro says, already unlacing, "and keep that hand where we can both see it." They come down onto the bed on either side of you, and then Minagho is astride you and Chivarro's mouth is on yours, and the lamp goes out under somebody's elbow.{/n}''',
        c("Continue", "morning", flags=(NIGHT_PAIR,))),
    nar("morning", '''{n}At dawn the palm opens along its new scar, and two hands reach for it at once. Minagho gets there first and binds it. Chivarro writes the night on your bill, itemised, and adds a line at the foot in her sharp hand: "Scar: paid in advance."{/n}''',
        c("[Keep the bill.]", flags=(MORNING,))),
], requires=("trickster.ever", DECLINED, T_HOUSE, MIN_IN, CH_IN), forbids=(COMPLETE, CLOSED, KEPT, OWNED, *CHAIN_FORBIDS),
   delay=120, ForbidOverrides={**PAIR_FO, **UNOWNED})

letter(P + "alone.minagho_when_it_scars", "When it scars", [
    nar("start", '''{n}The Goat's seal opens your palm every dawn, and it will never close on its own. So for a week of dawns you close it yourself, at the quartermaster's brazier, with the flat of a knife heated white, until what runs across your palm is a scar that bleeds and not merely a cut. You do not tell her. On the seventh morning you go down to her crate with the hand bound, and unbind it in front of her.{/n}''',
        c('[Show her the scar] "It scarred. Ask me, or I\'ll ask you."', "min", flags=(SCARRED,)),
        c("[Let it bleed a while longer.]", abort=True)),
    mg("min", '''"You burned it closed." {n}She does not touch it. She looks at it the way she once looked at the list of names at the eastern gate.{/n} "It still opens. It is still his. But the scar is yours, and you made it every morning for a week without telling me, which is the first thing you have ever done for me without a joke in it."
{n}Her lip curls, and it is not quite contempt.{/n} "Ask, Golarian."''',
       c('"Stay."', "night", flags=(COMPLETE, "minachiv.future_minagho", HALF, CHAIN)),
       c('[Close the hand] "Forget I asked."', flags=(CLOSED,))),
    nar("night", '''{n}She does not go back to her crate. She follows you up to your quarters, and inside the door she takes the scarred hand and bites the ridge of it, gently, and then not gently. Then she has you against the wall with her knee between yours and your shirt in her fist, and walks you to the bed, and pushes you down, and climbs astride you with the burned palm pressed flat over the dry brand on her own brow. "Mine," she says, "on top of his."{/n}''',
        c("Continue", "morning", flags=(NIGHT_MIN,))),
    nar("morning", '''{n}At dawn the scar opens, as it will every dawn. She is awake for it, and binds it with a strip of your sheet, too tightly, without a word, and does not leave.{/n}''',
        c("[Let her.]", flags=(MORNING,))),
], requires=("trickster.ever", DECLINED, MIN_IN), RequiresAnyGroups=ALONE_MIN_GATE,
   forbids=(REUNITED, RET_C, CH_IN, CLOSED, COMPLETE), delay=120, TricksterDevice=True, TricksterState="chivarro_dead")

letter(P + "alone.chivarro_when_it_scars", "Paid in advance", [
    nar("start", '''{n}You wait, as she told you to. A full month, without a letter, a wardrobe or a knock. On the last day of it you send a runner to the room above the chandler's shop with a purse: a year's rent, in advance, and no note at all.{/n}''',
        c("[Send the purse.]", "chv", crusade=("Finances", -200)),
        c("[Wait a while longer.]", abort=True)),
    cv("chv", '''{n}The runner comes back with the purse still in his hand and a message he has been made to learn by heart.{/n} "'A year in advance. Nobody pays a madam in advance, honey; it is terribly bad business. It means you intend to come back. Come and ask me to my face, and bring the purse.'"''',
       c('[Go, with the purse] "Stay. Keep the house with me."', "night", flags=(COMPLETE, "minachiv.future_chivarro", HALF, CHAIN)),
       c('[Keep the purse] "Forget I asked."', flags=(CLOSED,))),
    nar("night", '''{n}She counts the purse first, every coin, on the bed, while you stand and watch. Then she sweeps the coins onto the floor with one arm, pulls you down onto the bed by your collar, rolls you onto your back and settles astride you, her gown already sliding from her shoulders. "Paid in advance," she says, "so I shall take my time."{/n}''',
        c("Continue", "morning", flags=(NIGHT_CHIV,))),
    nar("morning", '''{n}In the morning there is a receipt on the pillow, in her hand: "One year, one night, and the interest, which is not negotiable." The coins are still on the floor. She has left them there, she says, so you can watch her pick them up.{/n}''',
        c("[Keep the receipt.]", flags=(MORNING,))),
], requires=("trickster.ever", DECLINED, CH_IN), RequiresAnyGroups=[[DECL_M, WAITING]],
   forbids=(REUNITED, OWNED, CLOSED, COMPLETE), delay=120, ForbidOverrides=dict(UNOWNED),
   TricksterDevice=True, TricksterState="minagho_dead")


# The morning after each physical commit: the night's consequence in their own voices, and what it costs.
PAIR_MORNING = [
    cv("start", '''{n}Morning. Chivarro is back on the quartermaster's bench before the stores open, in yesterday's borrowed wool and nothing under it, with the air of a woman who has already been paid.{/n}
"Well." {n}She looks you over the way she once looked over the Delights' new stock.{/n} "You were not ordinary. I am almost disappointed; I had a speech ready." {n}She tilts her eyeless face toward the crate where Minagho sits sharpening a dagger.{/n} "And she laughed. Twice. I have not heard her laugh like that since before Kenabres, and I have been trying for a very long time. I am not sure I forgive you for managing it in one night."''',
       c("Continue", "minagho")),
    mg("minagho", '''{n}Minagho does not look up from the dagger.{/n} "Your hand opened at dawn. You did not make a sound. I heard it anyway." {n}Her voice is flat.{/n} "I will hear it every dawn now, lying next to you, because of me. Do not ask me to be grateful for that. I am not." {n}The whetstone stops.{/n} "...I did not leave, either. Note that. It will not happen often."''',
       c('"Noted."', "terms"),
       c('[Show her the palm] "It\'s just blood. I have more."', "terms", alignment=("Chaotic", 1))),
    cv("terms", '''"Good." {n}Chivarro swings her feet down.{/n} "Then the terms stand, and here is the first bill under them: when you come to our house, you knock. On the door. Not the wardrobe." {n}Wilcer Garms, behind his ledger, turns a page with great concentration.{/n}''',
       c('"I\'ll knock."', flags=(MORNING,)),
       c('"No promises about the wardrobe."', flags=(MORNING, P + "morning_wardrobe"))),
]
physical(P + "after.the_morning_after", "The morning after", "Chivarro", PRES_CHIV, CHIV_UNIT, PAIR_MORNING,
         requires=("trickster.ever", COMPLETE, CHAIN, "minachiv.future_two", CH_IN, MIN_IN, NIGHT_PAIR), forbids=(MORNING, *CHAIN_FORBIDS),
         delay=8, ForbidOverrides=dict(PAIR_FO))

CHIV_MORNING = [
    cv("start", '''{n}Chivarro is at the quartermaster's counter at dawn, counting coins she did not have yesterday into a purse she did not have either. They are yours.{/n}
"Rent," she says, before you can speak. "And interest. I charge interest, honey; I was a madam, not a saint." {n}She snaps the purse shut and looks at you properly for the first time.{/n} "You were better than I expected and worse than you think. Both go on the bill."''',
       c('"Put it on my bill, then."', flags=(MORNING,), crusade=("Finances", -100)),
       c('[Take back one coin] "The interest is too high."', "haggle", crusade=("Finances", -100))),
    cv("haggle", '''{n}She lets you take it. Then she takes your wrist, turns your hand over, puts the coin back in your palm, presses it into the hollow of it with her thumb, and closes your fingers on it until it hurts.{/n} "Now it is a keepsake. Keepsakes are free. Everything else goes on the bill."''',
       c("[Keep the coin.]", flags=(MORNING, P + "morning_coin"))),
]
physical(P + "alone.chivarro_morning", "Interest", "Chivarro", PRES_CHIV, CHIV_UNIT, CHIV_MORNING,
         requires=("trickster.ever", COMPLETE, CHAIN, "minachiv.future_chivarro", CH_IN, NIGHT_CHIV), forbids=(MORNING, CLOSED), delay=8,
         TricksterDevice=True, TricksterState="minagho_dead")

MIN_MORNING = [
    mg("start", '''{n}Minagho is back on her crate outside the quartermaster's stores by the time the watch changes, as if she had never left it. Your palm opened at dawn, as it does every dawn now. The bandage you put on it is already red.{/n}
"His. Every morning." {n}She takes your wrist, not gently, and holds the hand up to the grey light as if checking a coin for clipping.{/n} "I lay awake beside you waiting for it. I wanted to see if you would flinch, so I would know what you are worth."''',
       c('"Did I?"', "verdict"),
       c("[Say nothing and let it bleed.]", "verdict")),
    mg("verdict", '''"No." {n}She lets go of the wrist.{/n} "Which means you are a liar or a fool, and I have not decided which. I will spend a long time deciding. You will not enjoy it."
{n}She turns back to her dagger, and then, without looking up:{/n} "Bind it properly, idiot. If you bleed to death on my account I will never forgive you, and I have a very long memory."''',
       c("[Bind it.]", flags=(MORNING,)),
       c('"You bind it."', "bind")),
    mg("bind", '''{n}She keeps sharpening long enough that you think she will refuse. Then she sets the dagger down, cuts a strip from your own sleeve with it, and binds the palm so tightly your fingers go white. Wilcer Garms discovers something urgent at the far end of his stores.{/n} "There. Now it is mine as well as his. Do not mistake that for kindness."''',
       c("[Don't.]", flags=(MORNING, P + "morning_bound"))),
]
MIN_MORNING_REQ = ("trickster.ever", COMPLETE, CHAIN, "minachiv.future_minagho", MIN_IN, NIGHT_MIN)
physical(P + "alone.minagho_morning", "His, every morning", "Minagho", PRES_MIN, MIN_UNIT, MIN_MORNING,
         requires=(*MIN_MORNING_REQ, RET_M), forbids=(MORNING, CLOSED), delay=8,
         TricksterDevice=True, TricksterState="chivarro_dead")
physical(P + "alone.minagho_spared_morning", "His, every morning", "Minagho", PRES_SPARED, MIN_UNIT, copy.deepcopy(MIN_MORNING),
         requires=(*MIN_MORNING_REQ, "minagho.spared.latched"), forbids=(MORNING, CLOSED, "minagho.dead", P + "alone.minagho_morning"),
         delay=8, TricksterDevice=True, TricksterState="chivarro_dead")


# === Epilogue pages (R2-6 and the chain's own endings; the registered endings narrate visits this Commander never had) =

def page(id, title, nodes, requires, forbids=(), any_groups=None, overrides=None):
    extra = dict(RequiresAnyGroups=any_groups) if any_groups else {}
    if overrides:
        extra["ForbidOverrides"] = dict(overrides)
    SCENES.append(scene(id, title, "Epilogue", 1, "", nodes, requires=requires, forbids=forbids, last=99,
                        Relationship=REL, **extra))


PALM_P = p("{n}The Commander's left palm never closed. It opened at dawn for the rest of a long life, a thin red line owed to a lord of the Abyss who never forgot a debt, and every morning one of them was there to bind it.{/n}",
           requires=(PALM,))
KNELT_P = p("{n}Minagho never let the Commander forget the kneeling. Neither did Baphomet.{/n}", requires=(KNELT,))
page(P + "epilogue.pair", "Two runaway lilitu", [
    nar("end", '''{n}Two runaway lilitu kept a house in Drezen after the war, below the citadel, with thick doors, a cellar nobody else knew about, and a linen press that was exactly as deep as it looked, most nights. They kept their own names. The Commander had agreed to their terms before the war was won, and had meant it; they sent one invitation a year, on those terms, written in two hands that took turns with the pen, and the Commander always went.{/n}''',
        paragraphs=(PALM_P, KNELT_P,
                    p("{n}Chivarro kept the ashes of the bill in a snuffbox, and took it out whenever the Commander forgot who had been bought and who had paid.{/n}",
                      requires=(BURNED,)),
                    p("{n}Some nights the kept door in the Commander's quarters opened on the Delights by itself, and music came through it. The Commander never bricked it up.{/n}",
                      requires=(DOOR,)),
                    p("{n}The Commander never once knocked. Chivarro billed for every visit through the wardrobe, and Minagho kept the accounts.{/n}",
                      requires=(P + "morning_wardrobe",))))],
    requires=("trickster.ever", COMPLETE, CHAIN, "minachiv.future_two"), forbids=("sacrifice",), overrides={"sacrifice": "trickster.commander_back"})
page(P + "epilogue.chivarro", "Rent", [
    nar("end", '''{n}Chivarro kept her own house in Drezen after the war and never once let the Commander forget whose name was on the lease. The rent was collected in person, at her convenience, and it went up every year.{/n}''',
        paragraphs=(p("{n}Minagho never came back from Baphomet's ledger. Chivarro kept a second chair at her table anyway, and nobody, not even the Commander, was allowed to sit in it.{/n}",
                      forbids=(MIN_IN,)),
                    p("{n}When Minagho did walk back in, the terms changed, exactly as Chivarro had promised, and the Commander did not get a say.{/n}",
                      requires=(MIN_IN,)),
                    PALM_P,
                    p("{n}The Commander kept the coin. Chivarro never charged for it, and never let anyone else touch it.{/n}",
                      requires=(P + "morning_coin",))))],
    requires=("trickster.ever", COMPLETE, CHAIN, "minachiv.future_chivarro"), forbids=("sacrifice",), overrides={"sacrifice": "trickster.commander_back"})
page(P + "epilogue.minagho", "His, every morning", [
    nar("end", '''{n}Minagho stayed in Drezen with the Goat's mark still on her brow, dry for the first time since Kenabres, and kept the Commander's debt the way other women keep a lover's letters: close, and bitterly, and read over and over. Nobody bargained for her again. She saw to that.{/n}''',
        paragraphs=(PALM_P, KNELT_P,
                    p("{n}She never forgave the house that kept Chivarro in its cellar and wanted too much for her. Some nights she went down to the Lower City and made it pay the difference.{/n}",
                      requires=("chivarro.dead.latched", DEPOSIT), forbids=(RET_C,)),
                    p("{n}She never forgave the Commander for Chivarro, and never pretended to. Every year, on the night of the cellar, she sat at the foot of the bed and sharpened a dagger until dawn, and every year she put it away unused, and never said why.{/n}",
                      requires=("chivarro.dead.latched",), forbids=(DEPOSIT, RET_C)),
                    p("{n}Chivarro came back through the house's back rooms after all, found the terms already signed without her, and renegotiated them, loudly, for a week.{/n}",
                      requires=(RET_C,)),
                    p("{n}Every dawn, for the rest of the Commander's life, Minagho bound the palm herself, too tightly, and never once called it kindness.{/n}",
                      requires=(P + "morning_bound",))))],
    requires=("trickster.ever", COMPLETE, CHAIN, "minachiv.future_minagho"), forbids=("sacrifice",), overrides={"sacrifice": "trickster.commander_back"})
page(P + "epilogue.owned", "Goods", [
    nar("end", '''{n}Chivarro stayed in Drezen, owned, on paper, at the Commander's door, and never once let it be mistaken for anything else. She was never seen to smile at the Commander again. She was never seen to leave.{/n}''',
        paragraphs=(p("{n}Minagho visited her there, and did not speak to the Commander at all.{/n}", requires=(MIN_IN,)),))],
    requires=("trickster.ever", KEPT))
# R2-6: a late commit for a Commander whose chain stopped before the question.
page(P + "epilogue.commit", "One invitation a year", [
    nar("start", '''{n}The war ended before the question was asked.{/n}''',
        c("Continue", "pair", requires=(T_HOUSE,)),
        c("Continue", "waiting", forbids=(T_HOUSE,))),
    nar("pair", '''{n}Two runaway lilitu kept a house in Drezen after the war, below the citadel, with thick doors and a cellar nobody else knew about. The first year, they sent the Commander one invitation, on their own terms, written in two hands.{/n}''',
        c("[Go.]", "went"),
        c("[Send your regrets.]", "regrets")),
    nar("waiting", '''{n}Chivarro kept a room in Drezen after the war, below the citadel, waiting for someone who had not come back, and let it be known that the Commander still owed her an answer. The first year, she sent one invitation, on her own terms.{/n}''',
        c("[Go.]", "went_alone"),
        c("[Send your regrets.]", "regrets")),
    nar("went", '''{n}The Commander went. The door was barred from the inside with a chair, and opened anyway. Chivarro took the Commander's sword belt off on the threshold as if collecting a coat; Minagho took the rest, less politely, walking the Commander backwards across a room neither of them had bothered to light, and between them they bore the Commander down onto a bed that Chivarro announced had been built for exactly three.{/n}
{n}The Commander went every year after that, and some years did not leave until spring.{/n}'''),
    nar("went_alone", '''{n}The Commander went. Chivarro opened the door herself, in a dressing gown and nothing else, and looked the Commander over the way she had once looked over the Delights' new stock. "Late," she said. "Everything costs more when it is late." She pulled the Commander in by the collar, shut the door with her heel, and let the gown fall on the way to the bed. At the bed she did not stop: she pushed the Commander down onto it with one hand flat on the chest, climbed astride, and pinned the Commander's wrists to the pillow above. "Late," she said again, against the Commander's mouth, lowering her hips. "Now you pay the interest."{/n}
{n}In the morning there was a bill on the pillow, itemised, with the interest compounded by the hour, and her signature across the total. The Commander went every year after that. The rent went up every time.{/n}'''),
    nar("regrets", '''{n}The Commander sent regrets. The next year's invitation came anyway, and the year after that. They were patient in the way demons are patient: badly, and with knives.{/n}'''),
], requires=("trickster.ever",), forbids=(COMPLETE, CLOSED, DECLINED, KEPT, OWNED, "sacrifice"), any_groups=[[T_HOUSE, WAITING]],
   overrides={**UNOWNED, "sacrifice": "trickster.commander_back"})
page(P + "epilogue.declined", "When it scars", [
    nar("end", '''{n}They waited to be asked again, as demons wait: badly, and with knives.{/n}''',
        paragraphs=(p("{n}The Commander's palm never scarred.{/n}", forbids=(SCARRED,)),
                    p("{n}The Commander burned the palm into a scar, and showed it, and then closed the hand and never asked. It went on bleeding every dawn, along the scar, for the rest of a long life.{/n}", requires=(SCARRED,))))],
    requires=("trickster.ever", DECLINED), forbids=(COMPLETE,))


# === Reactions (Daeran, Wenduag; Socothbenoth, Camellia; Baphomet is the parley) ===================================

REACTIONS = [
    reaction("Daeran", P + "react.daeran", (RET_M,),
             '''"I told you I enjoy watching lilitu die. You have spoiled it: now I shall have to watch her do it again." {n}He studies your bandaged palm with frank delight.{/n} "You bled for a lilitu. Do tell me she was worth a whole hand."''',
             answer_list=DAERAN_HUB, forbids=("daeran.dead", "daeran.kicked_out"), chapter=5, last=5,
             entry='"Minagho is back."'),
    reaction("Wenduag", P + "react.wenduag", (RET_M,),
             '''"The eyeless one from Kenabres. You bled to buy her back?" {n}She grins.{/n} "In the dark we would have tied her to a post. Keep her afraid, and she will be useful."''',
             answer_list=WENDUAG_HUB, forbids=("wenduag.killed", "wenduag.kicked_out"), chapter=5, last=5,
             entry='"Minagho is back."'),
    reaction("Socothbenoth", P + "react.socoth_fee", ("trickster.ever", SOCOTH),
             '''"Two lilitu through one linen press? My closets are not a bawdy house. Well. Not *only*." {n}He sniffs.{/n} "The fee is one secret from each of them, collected at my leisure. Do tell them I said hello. Do not tell them what I said after."''',
             answer_list=SOCOTH_LIST, forbids=("council.expired",), chapter=5, last=5,
             entry='"About the linen press."', NativeReturnCue=SOCOTH_RETURN),
    reaction("Camellia", P + "react.camellia_bill", (RET_C,),
             '''"Did you keep the receipt?" {n}Camellia's smile is polite and very interested.{/n} "One should always keep the receipt. Otherwise, how would anyone know who belongs to whom?"''',
             answer_list=CAMELLIA_HUB, forbids=("camellia.killed", "camellia.dead", "camellia.kicked_out"), chapter=5, last=5,
             entry='"About Chivarro."',
             # A killed Camellia returns veiled at Fye's bar with no native hub (camellia_trickster PERFORMANCE), so a reaction
             # on her companion hub cannot play for her; CamelliaTricksterTests forbids foreign killed overrides. Her retained
             # death (camellia.dead) is lifted by her return here and by her module.
             ForbidOverrides={"camellia.dead": "camellia.trickster.returned"}),
]
SCENES.extend(REACTIONS)


# === The registered route ===========================================================================================

LOST = {"minachiv.ending_both_lost": (RET_M, RET_C), "minachiv.ending_minagho_lost": (RET_M,),
        "minachiv.ending_chivarro_lost": (RET_C,)}


def integrate(payload):
    """Save-safe edits to the registered pair route: no id, node or choice is renamed, removed or reordered."""
    rel = payload["Relationships"][REL]
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(v) for k, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path the pair can be reached even when Minagho or Chivarro has died: listen when "
                        "Minagho recites her brand's terms, when Herrax asks for Chivarro's head, and when Socothbenoth "
                        "explains his closets.")
    payload.setdefault("Presences", {}).update(copy.deepcopy(PRESENCES))
    for key, groups in DERIVED.items():
        payload.setdefault("Derived", {})[key] = [list(g) for g in groups]
        for member in {k for g in groups for k in g}:   # trickster_world binds scene reads, not Derived members
            kind, guid, _ = trickster_world.BINDINGS[member]
            payload.setdefault(kind, {}).setdefault(member, guid)
    ours = {s["Id"] for s in SCENES}
    for s in payload["Scenes"]:
        if s.get("Relationship") != REL or s["Id"] in ours:
            continue
        base = s["Id"].removesuffix("_completed")
        if base in LOST:
            # G6(a): a lost page never plays for a woman who came back.
            s["Forbids"] += [f for f in LOST[base] if f not in s["Forbids"]]
            for death, ret in PAIR_FO.items():
                if death in s["Forbids"]:
                    s.setdefault("ForbidOverrides", {})[death] = ret
        elif any(f in s["Forbids"] for f in PAIR_FO):
            # G6(b): visits and endings read a returned woman as alive.
            s.setdefault("ForbidOverrides", {}).update({f: r for f, r in PAIR_FO.items() if f in s["Forbids"]})
        if s["Owner"].endswith("Epilogue") and CHAIN not in s["Forbids"]:
            # The registered endings narrate RanRomance visits a Trickster-chain Commander never had; the chain's own pages play.
            s["Forbids"].append(CHAIN)

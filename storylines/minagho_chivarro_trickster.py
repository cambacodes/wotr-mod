"""Minagho and Chivarro on the Trickster path: the brand re-addressed (F17), through the wrong wardrobe (F01) and the house
always collects (F24). Specs: Writer/handoffs/trickster/minagho.md and chivarro.md (one relationship, two women).

Canon: Minagho bleeds from Baphomet's brand until she "spilled the blood of the one who caused me to fail in Kenabres"
(MinaghoAfterCombat/Cue_0020 234795ef; MinaghoAndAzata/Cue_0025 60906a72), and Baphomet's seals "simply mark their bodies
as mine" (Prison_Baph/Cue_0123 c5f91838). Chivarro: "Minagho and I... were closer than most demons ever get" (Cue_0097
d8b51192); "Any of them can be yours for a night... Or forever, if your pockets are deep enough" (Cue_0081 594482c2). Herrax
asks for the kill in advance (Herraxa_dialogue/Cue_0045_KillChivarro 49135105) and her house strips the dead: rings "cut off a
dead body along with the fingers" (Cue_0052 d6955c2a). "Closets grant you freedom. You can step inside one, and exit from
another..." (SocothBriefing/Cue_0011 2f4be0bd). Authored, and labelled as authored: the Commander volunteering as the
failure of record; the unpaid seal that keeps the body it marks ("The dead do not bleed."); the linen press; the priestess of
Nocticula in the Delights' back rooms who raises what the house sells, once (a servant of the goddess, never Nocticula).
"""
import copy

from story_format import c, n, p, reaction, scene
from storylines import trickster_world

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
DERIVED = {CELLAR: [["chivarro.removed"], ["chivarro.exiled"]]}

CHIV_UNIT = "b7e819e2a9bb0804abcbffe8e7d91ba6"   # Chivarro.jbp (female, CutsceneNeutrals)
MIN_UNIT = "565ccab37e2475742b043ec912a750fa"    # Minagho_DrezenInThePast (female, Neutrals; the only non-hostile Minagho)
WILCER = "a380d926e92f70e429681eb9654478f9"      # DrezenCapital_Quartermaster, Wilcer Garms (the anchor)
DREZEN = "2570015799edf594daf2f076f2f975d8"
HERRAX_LIST = "43f93812d6216c94db356622859397f1"   # Herraxa_dialogue/AnswersList_0004 (her hub after the contract)
HERRAX_RETURN = "1af69c65d15cc8949a4fe47a45c4f85d"  # Cue_0100 "We have some true gems here."
BAPH_LIST = "cbd2f289d8173fb41a231772290440ba"      # Prison_Baph/AnswersList_0071 (the parley hub)
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
                               "daggers over in her fingers. The mark on her brow is dry.{/n}"),
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
WAKE = '''{n}You close her fingers around the hilt and draw it across your palm. Technically, she did it. The mark on her face drinks, and closes, and her chest moves.{/n}
"...You." {n}She licks your blood from her own fingers, slowly, as if tasting a vintage.{/n} "I died cursing you, and I wake up at your door, owing you. Is that the joke? Is *that* your idea of funny?"
"He will smell this on you. Every seal he owns will. You have made yourself his, you idiot, and for what? For me?" {n}Her lips peel back from her teeth.{/n} "I will find the flaw in this. And when I do, I will decide whether you were worth the blood."'''
WAKE_BRANDED = '''{n}You close her fingers around the hilt and draw it across your palm. Technically, she did it. The mark on her face drinks, and closes, and her chest moves.{/n}
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
    c('[Show her your palm] "Moved it. It bleeds on me now. Mornings, mostly."', "terms", requires=(PRIMED,)),
    c('[Cut your palm and say the terms over it] "\'Until she spills the blood of the one who caused her to fail.\' That\'s me. Watch."',
      "terms", requires=("trickster",), forbids=(PRIMED,), flags=(PRIMED, DEBT, LATE_CLAIM), mythic="Trickster",
      crusade=("Favors", -100)))
SPARED_TERMS = mg("terms", '''"What kind of idiot lets their enemy slip away? And what kind of idiot puts their own name in a demon lord's ledger?" {n}She touches the mark. It stays dry.{/n}
"Baphomet will want the thief's name. I could buy my life back with yours, Golarian. Give me one reason I shouldn't."''',
    c('"Because it\'s my name on the brand now. Kill me, and you\'re bleeding again by supper."', flags=(MIN_IN, STARTED)),
    c('[Intimidate] "Because I\'d come back. Ask around. I do that."', flags=(MIN_IN, STARTED), alignment=("Chaotic", 1)),
    c('"Chivarro is on the quartermaster\'s bench. Give her the reason."', requires=(CH_IN,), flags=(MIN_IN, STARTED, REUNITED)),
    c('"No reason. Go, and stay unbranded."', flags=(DECL_M,)))
physical(P + "spared.brand", "It stopped bleeding", "Minagho", PRES_SPARED, MIN_UNIT, [
    *varied("start", mg, '''{n}She has taken one of the crusade's daggers off the quartermaster's rack and is sitting on a crate with it across her knees. Nobody saw her come through Drezen. That is the point.{/n}
"It stopped. The moment you opened your mouth, it stopped, and it has not bled since. What did you do?"''',
            [("terrified", mg, '"I ran from you in that cursed cell. I kept running. It did not bleed once."', "minagho.terrified")],
            SPARED_OPEN),
    SPARED_TERMS,
], requires=("trickster.ever", "minagho.spared.latched"), RequiresAnyGroups=[[PRIMED, "trickster"]], forbids=("minagho.dead", DECL_M),
   TricksterDevice=True, TricksterState="minagho_alive")
letter(P + "spared.brand_letter", "It stopped bleeding", [
    mg("start", '''{n}The note is pinned to your pillow with one of your own daggers. There is no blood on it. That is the point of the note.{/n}
"It stopped. What did you do? I could buy my life back with yours, Golarian. Give me one reason I shouldn't, and give it to my face."''',
       c('"Because it\'s my name on the brand now. Come and see."', flags=(MIN_IN, STARTED, DEBT)),
       c('"No reason. Stay away, and stay unbranded."', flags=(DECL_M,)))],
   requires=("trickster.ever", "minagho.spared.latched", PRIMED, PRES_SPARED + ".failed"),
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
       c('[Put a deposit on the house special] "You want her gone forever? Then she\'s on the menu. Write it down: \'One Chivarro, forever.\' I\'m paying in advance."',
         "ink", mythic="Trickster"),
       c('"Forget I asked."', abort=True)),
    hx("ink", '''"Paying for a corpse before it's a corpse?" {n}She counts something behind her eyes, and whatever the sum is, it pleases her.{/n} "Lover, that's the most romantic thing anyone has ever done in this house."
{n}She writes the line herself and blows on the ink.{/n} "The price is a favour. When I call. You won't ask what."''',
       c('"Put it on my bill."', flags=(DEPOSIT, FAVOR)),
       c('"No. No favours with no name."', abort=True)),
], requires=("trickster", "herrax.asked_kill_chivarro"), forbids=("chivarro.dead", "chivarro.searching", DEPOSIT), last=4,
   optional=True, Relationship=REL, AnswerLists=[HERRAX_LIST], NativeReturnCue=HERRAX_RETURN,
   TricksterDevice=True, TricksterState="chivarro_dead"))

letter(P + "chivarro_dead.bought", "The house always collects", [
    *varied("start", hx, '''{n}The letter smells of the Delights: incense, coin and something under both. The hand is round and unhurried.{/n}
"Honey. My boys fetched her out of that cellar with everything else she had left. Rings, fingers, the lot. The house keeps what it collects, and it sells what it keeps.
The house also keeps a priestess of Nocticula in the back rooms, and she raises what the house sells. Once. What will it be?"''',
            [("told", hx, '"You told me she was dead, and she was. Now you want to buy her back from me. I *adore* you."',
              "herrax.told_chivarro_dead")],
            (c('[Order from the house menu] "One Chivarro. Forever. My pockets are deep enough."', "paid", requires=(DEPOSIT,),
               mythic="Trickster"),
             c('[Order from the house menu] "One Chivarro. Forever. My pockets are deep enough. Write it now; I\'ll sign."', "late",
               requires=("trickster",), forbids=(DEPOSIT,), mythic="Trickster"),
             c('"Nothing. Leave her dead."', flags=(DECL_C,)))),
    hx("paid", '''"'One Chivarro, forever. Deposit paid.' My own hand, lover. I laughed while I wrote it." {n}Under it, the priestess's fee is struck through: on the house.{/n}
"The favour stands. When I call."''',
       c('"Deal."', "sale", alignment=("Evil", 1))),
    hx("late", '''{n}The next page is the order, written while the ink on the first was still wet: "One Chivarro, forever." Your name is waiting for its signature.{/n}
"Late orders cost double, honey. Two favours. And the priestess does not work for nothing: three hundred in crusade script, and a writ for the rest."''',
       c('"Deal. Both favours."', "sale", flags=(FAVOR, LATE), alignment=("Evil", 1), crusade=("Finances", -300)),
       c('"Too rich. Leave her dead."', flags=(DECL_C,))),
    cv("sale", '''{n}The last page is in another hand, sharp and slanted, written by someone who has just learned to hold a pen again.{/n}
"Sold. In my own house. To *you*. Under 'goods'." {n}The pen has gone through the paper twice.{/n}
"Here is my price, since nobody asked it. The bill. Burn it, and I come to Drezen owing you nothing and hating you for the favour. Keep it, and I come anyway, and you sleep with one eye open for the rest of your short life."''',
       c('[Burn the bill] "Nothing. Get dressed."', flags=(RET_C, CH_IN, BURNED, STARTED), alignment=("Chaotic", 1)),
       c('[Burn the bill] "Nothing. Get dressed. Minagho hates waiting."', requires=(MIN_IN,),
         flags=(RET_C, CH_IN, BURNED, STARTED, REUNITED), alignment=("Chaotic", 1)),
       c('[Keep the bill] "Everything. And now I own it."', flags=(RET_C, CH_IN, OWNED, STARTED), alignment=("Evil", 2))),
], requires=("trickster.ever", "chivarro.dead", "chivarro.dead.latched"), RequiresAnyGroups=[[DEPOSIT, "trickster"]],
   forbids=(RET_C, DECL_C), delay=48, owner="Herrax", TricksterDevice=True, TricksterState="chivarro_dead")


# === The pair's Trickster chain (a Trickster variant of the registered visits, which stay untouched) =================

CHAIN_FORBIDS = (CLOSED, "minagho.dead", "chivarro.dead")
letter(P + "after.what_the_offer_bought", "What the offer bought", varied("start", cv,
    '''"There is a buyer. There is always a buyer. A marilith in the Lower City wants the two lilitu who walked out of Baphomet's ledger and Herrax's, and she has sent a list of what she would pay." {n}Minagho's hand, under Chivarro's, in a harder script:{/n} "She would pay less than you did. Tell us what to do with it, Golarian. We want to see what you say."''',
    [("receipt", cv, "{n}Chivarro, in the margin:{/n} \"The receipt you burned is the only one of its kind. The marilith has asked for a copy.\"",
      BURNED)],
    (c('"Take the buyer\'s list. Sell it back to her."', flags=(T_OFFER, P + "offer_sold_back"), alignment=("Evil", 1)),
     c('"Burn the list. Let them come."', flags=(T_OFFER, P + "offer_burned")))),
    requires=("trickster.ever", REUNITED), forbids=(*CHAIN_FORBIDS, T_OFFER, HALF), ForbidOverrides=dict(PAIR_FO))

PRICE_NODES = [
    *varied("start", cv, '''{n}Chivarro is waiting for you by the quartermaster's stores, in borrowed Drezen wool that she wears like a costume.{/n}
"Minagho says you own her debt. Then you and I will discuss the price of her. What is her name worth to you, Golarian?"''',
            [("owned", cv, '"You own *me*, on paper. Her you only bled for. Which do you think I resent more?"', OWNED),
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
         requires=("trickster.ever", T_OFFER, CH_IN), forbids=(*CHAIN_FORBIDS, T_NAME, WALKED), ForbidOverrides=dict(PAIR_FO))
letter(P + "after.the_price_of_her_name_letter", "The price of her name", [
    cv("start", '''{n}The note is written on the back of the quartermaster's inventory, in a sharp, slanted hand.{/n}
"Minagho says you own her debt. Then you and I will discuss the price of her. What is her name worth to you, Golarian? Answer with your hand. The bleeding one. Pressed to the page."''',
       c("[Press your bleeding palm to the page.]", flags=(T_NAME, PALM_TABLE)),
       c('"It\'s worth a joke."', flags=(WALKED,)))],
   requires=("trickster.ever", T_OFFER, CH_IN, PRES_CHIV + ".failed"),
   forbids=(*CHAIN_FORBIDS, T_NAME, WALKED, P + "after.the_price_of_her_name"), delay=96, ForbidOverrides=dict(PAIR_FO))

letter(P + "after.won_back", "Won back", [
    nar("start", '''{n}Chivarro has taken a room at the far end of the lower town and paid for it with a ring nobody saw her wear. She has not come back. She has also not left Drezen.{/n}''',
        c('[Send the silk] "A bolt of Nerosyan silk, dyed Delights red, and a card: \'Your price. Name it again.\'"', "answer",
          crusade=("Finances", -200)),
        c('"Let her stay gone."', flags=(SENT_BACK,))),
    cv("answer", '''{n}The card comes back the next morning, pinned to your door with a hatpin. On the back, in her hand:{/n} "Red. You remembered. It is still not enough." {n}Under it, smaller:{/n} "Tomorrow. Bring the hand."''',
       c("[Keep the card.]", flags=(T_NAME, WON_BACK))),
], requires=("trickster.ever", WALKED, CH_IN), forbids=(*CHAIN_FORBIDS, T_NAME), ForbidOverrides=dict(PAIR_FO))

letter(P + "after.who_keeps_the_house", "Who keeps the house", varied("start", mg,
    '''"We are going to need a house, when your war is done. Somewhere with thick doors and a cellar nobody else knows about." {n}Chivarro, in the margin:{/n} "And a linen press. For guests."''',
    [("door", cv, '{n}Chivarro adds, lower down:{/n} "Your kept door opens on my old house some nights now. I hear the music through it. Brick it up, or give it to us."',
      DOOR)],
    (c('"Chivarro keeps the house. Minagho keeps the door."', flags=(T_HOUSE, "minachiv.host_ending")),
     c('"Neither. You keep each other, and I keep out of it."', flags=(T_HOUSE, "minachiv.winter_ending")))),
    requires=("trickster.ever", T_NAME), forbids=(*CHAIN_FORBIDS, T_HOUSE), ForbidOverrides=dict(PAIR_FO))

# 5.4 The commit: their terms, her refusal on every branch, and the heat to the cut.
PAIR_THRESHOLD = nar("threshold", '''{n}They take you up to your own quarters between them, one on each arm, arguing across you the whole way about which of them the stairs were built for.{/n}
{n}At the door Chivarro stops arguing. She unbuckles your sword belt without looking at it, the way a woman who has undressed a thousand guests knows every buckle ever forged. Minagho is slower and less kind; she drags her nails down the seam of your shirt and watches your face instead of her hands, learning where you flinch. Two mouths, one warm and one fever-hot, and somewhere between them the bleeding palm is lifted and kissed, and licked clean, and pressed flat against a bare hip that is not yours.{/n}
{n}"Our terms," Chivarro says against your throat. "Say it again." You say it again. Minagho laughs, low and ugly and delighted, and pulls you both down onto the bed.{/n}''',
    c("Continue"))
COMMIT_FORBIDS = (CLOSED, COMPLETE, DECLINED, KEPT, *CHAIN_FORBIDS)
COMMIT_NODES = [
    mg("start", '''{n}They have taken the bench outside the quartermaster's stores as if they had owned it for years and you were the one passing through: Chivarro stretched along it, Minagho sitting on its back with her boots on the seat.{/n}
"We have been talking about you, Golarian. We do that now. It is very tiresome." {n}Chivarro, without looking up:{/n} "Ask the question, honey. We have a wager on how badly you phrase it."''',
       c('"Stay. Both of you. On your terms."', "terms", forbids=(OWNED,)),
       c('[Burn the bill in front of them] "Stay. Both of you. On your terms. This first."', "terms_burned", requires=(OWNED,)),
       c('[Tell them it was a joke that worked] "You\'re both on my ledger now. That\'s all this ever was."', "refuse"),
       c('[Keep the bill in your pocket] "Stay. The bill says you will."', "service", requires=(OWNED,))),
    cv("terms_burned", '''{n}She watches the paper curl in the quartermaster's brazier. She does not thank you. She waits until the last corner of "goods" has gone black, and then she breathes out, very slowly, through her teeth.{/n}
"Late. But burned." {n}She turns her face back to you.{/n}''',
       c("Continue", "terms", flags=(BURNED,))),
    cv("terms", '''"Our terms. We keep our own house. We keep our own names. You visit when you are asked, and you are asked rarely." {n}Minagho:{/n} "And when the Goat calls in his seal, you do not bargain for me again. I will stand where I choose."''',
       c('"Your terms. Agreed."', "threshold", flags=(COMPLETE, "minachiv.future_two", CHAIN)),
       c('"I won\'t bleed for the Goat forever."', "refuse")),
    cv("service", '''{n}She looks at the pocket, and at you, and at Minagho, who looks away.{/n} "Then I stay. Owned. On paper, in your city, at your door. Do not ever mistake it for anything else, and do not ever come to my bed with it in your pocket. I would take the hand that holds it."''',
       c("[Say nothing.]", flags=(KEPT,), alignment=("Evil", 1))),
    mg("refuse", '''"No." {n}Minagho stands.{/n} "Not while his seal still bleeds on your hand and you still call it a joke. We are demons, Golarian. We do not stay for jokes. Ask me when it scars."''',
       c('"Then I\'ll ask again when it scars."', flags=(DECLINED,)),
       c('"Then get out of my city. Both of you."', flags=(CLOSED,))),
    PAIR_THRESHOLD,
]
physical(P + "after.before_the_last_road", "Before the last road", "Minagho", PRES_CHIV, CHIV_UNIT, COMMIT_NODES,
         requires=("trickster.ever", T_HOUSE, MIN_IN, CH_IN), forbids=COMMIT_FORBIDS, ForbidOverrides=dict(PAIR_FO))
letter(P + "after.before_the_last_road_letter", "Before the last road", [
    mg("start", '''{n}The letter is in two hands, taking turns, and the ink changes colour wherever one of them snatched the pen.{/n}
"We have been talking about you. Our terms: we keep our own house, we keep our own names, you visit when you are asked. And when the Goat calls in his seal, you do not bargain for me again." {n}Chivarro, below:{/n} "Answer in ink, honey. We will know if you blot it."''',
       c('"Your terms. Agreed."', flags=(COMPLETE, "minachiv.future_two", CHAIN), forbids=(OWNED,)),
       c('[Send the bill back, burned at the corners] "Your terms. Agreed."', requires=(OWNED,),
         flags=(COMPLETE, "minachiv.future_two", CHAIN, BURNED)),
       c('"Then I\'ll ask again when it scars."', flags=(DECLINED,)),
       c('"Get out of my city."', flags=(CLOSED,)))],
   requires=("trickster.ever", T_HOUSE, MIN_IN, CH_IN, PRES_CHIV + ".failed"),
   forbids=(*COMMIT_FORBIDS, P + "after.before_the_last_road"), delay=96, ForbidOverrides=dict(PAIR_FO))

# 5.5 Alone commits: each woman can be won without the other. Devices: the partner's unreturned death may hold.
ALONE_CHIV_NODES = [
    cv("start", '''"She is not coming, or she is not coming yet. I have stopped waiting to find out which." {n}She has taken over the quartermaster's counter; Wilcer Garms has taken refuge behind his own ledgers.{/n} "So. What am I, in Drezen, without her?"''',
       c('"Stay anyway. Keep the house with me instead."', "terms"),
       c('"Go back through the press. There\'s nothing here for you."', flags=(CLOSED,))),
    cv("terms", '''"Then I keep my own house, in your city, on my terms, and you pay the rent. If she walks back in, the terms change, and you do not get a say."''',
       c('"Your terms."', "threshold", flags=(COMPLETE, "minachiv.future_chivarro", HALF, CHAIN)),
       c('"Not those terms."', "refuse")),
    cv("refuse", '''"Then wait. You are good at making demons wait."''',
       c('"Then wait. I\'ll ask again."', flags=(DECLINED,))),
    nar("threshold", '''{n}She does not take you to your quarters. She takes you to hers, a rented room above a chandler's in the lower town, and bars the door with a chair, and turns.{/n}
{n}"Rent," she says, and holds out her hand. When you put yours in it she laughs, and draws you down onto a bed that is too narrow for anything she has in mind, and begins, unhurried and expert, to collect.{/n}''',
        c("Continue")),
]
physical(P + "alone.chivarro", "The house she keeps now", "Chivarro", PRES_CHIV, CHIV_UNIT, ALONE_CHIV_NODES,
         requires=("trickster.ever", CH_IN), RequiresAnyGroups=[[DECL_M, WAITING]],
         forbids=(REUNITED, OWNED, CLOSED, COMPLETE, DECLINED), delay=96, TricksterDevice=True, TricksterState="minagho_dead")
letter(P + "alone.chivarro_letter", "The house she keeps now", [
    cv("start", '''"She is not coming, or she is not coming yet. I have stopped waiting to find out which. So: I keep my own house, in your city, on my terms, and you pay the rent. If she walks back in, the terms change, and you do not get a say."''',
       c('"Your terms."', flags=(COMPLETE, "minachiv.future_chivarro", HALF, CHAIN)),
       c('"Then wait. I\'ll ask again."', flags=(DECLINED,)))],
   requires=("trickster.ever", CH_IN, PRES_CHIV + ".failed"), RequiresAnyGroups=[[DECL_M, WAITING]],
   forbids=(REUNITED, OWNED, CLOSED, COMPLETE, DECLINED, P + "alone.chivarro"), delay=96,
   TricksterDevice=True, TricksterState="minagho_dead")

ALONE_MIN_NODES = [
    mg("start", '''"You keep looking at the gate as if someone else is coming through it." {n}She does not look at it herself.{/n}''',
       c('"She\'s dead, and the house wants too much for her. Stay."', "terms", requires=("chivarro.dead.latched",)),
       c('"She went back through the press. Stay."', "terms", forbids=("chivarro.dead.latched",))),
    mg("terms", '''"Stay. For a mortal who owns my debt and bleeds for it every morning." {n}Her lip curls.{/n} "My price: you never bargain for me again. Not with him, not with anyone."''',
       c('"Your price."', "threshold", flags=(COMPLETE, "minachiv.future_minagho", HALF, CHAIN)),
       c('"Not that price."', "refuse")),
    mg("refuse", '''"Then ask me when it scars, Golarian. Or do not ask at all."''',
       c('"Then I\'ll ask again when it scars."', flags=(DECLINED,)),
       c('"Then go. Unbranded."', flags=(CLOSED,))),
    nar("threshold", '''{n}She walks you back to your quarters as though she were the one escorting a prisoner, one hand fisted in the back of your collar. Inside she does not bother with the lamp.{/n}
{n}She finds the bleeding palm in the dark and holds it against her mouth, and you feel her smile against the cut before you feel her teeth. "Mine," she says, "for tonight. His, every morning after." Then she pushes you back against the door, hard enough to rattle the bar, and does not let go.{/n}''',
        c("Continue")),
]
ALONE_MIN_GATE = [[DECL_C, SENT_BACK, "chivarro.dead.latched"]]
ALONE_MIN_FORBIDS = (REUNITED, RET_C, CH_IN, CLOSED, COMPLETE, DECLINED)
physical(P + "alone.minagho", "One lilitu, unbranded", "Minagho", PRES_MIN, MIN_UNIT, ALONE_MIN_NODES,
         requires=("trickster.ever", MIN_IN, RET_M), RequiresAnyGroups=ALONE_MIN_GATE, forbids=ALONE_MIN_FORBIDS, delay=96,
         TricksterDevice=True, TricksterState="chivarro_dead")
physical(P + "alone.minagho_spared", "One lilitu, unbranded", "Minagho", PRES_SPARED, MIN_UNIT, copy.deepcopy(ALONE_MIN_NODES),
         requires=("trickster.ever", MIN_IN, "minagho.spared.latched"), RequiresAnyGroups=ALONE_MIN_GATE,
         forbids=(*ALONE_MIN_FORBIDS, "minagho.dead", P + "alone.minagho"), delay=96,
         TricksterDevice=True, TricksterState="chivarro_dead")
letter(P + "alone.minagho_letter", "One lilitu, unbranded", [
    mg("start", '''"Stay, you said. For a mortal who owns my debt and bleeds for it every morning." {n}The hand is hard and very straight.{/n} "My price: you never bargain for me again. Not with him, not with anyone."''',
       c('"Your price."', flags=(COMPLETE, "minachiv.future_minagho", HALF, CHAIN)),
       c('"Then I\'ll ask again when it scars."', flags=(DECLINED,)))],
   requires=("trickster.ever", MIN_IN), RequiresAnyGroups=[*ALONE_MIN_GATE, [PRES_MIN + ".failed", PRES_SPARED + ".failed"]],
   forbids=(*ALONE_MIN_FORBIDS, P + "alone.minagho", P + "alone.minagho_spared"), delay=96,
   TricksterDevice=True, TricksterState="chivarro_dead")


# === Epilogue pages (R2-6 and the chain's own endings; the registered endings narrate visits this Commander never had) =

def page(id, title, nodes, requires, forbids=(), any_groups=None):
    extra = dict(RequiresAnyGroups=any_groups) if any_groups else {}
    SCENES.append(scene(id, title, "Epilogue", 1, "", nodes, requires=requires, forbids=forbids, last=99,
                        Relationship=REL, **extra))


PALM_P = p("{n}The Commander's left palm never closed. It opened at dawn for the rest of a long life, a thin red line owed to a lord of the Abyss who never forgot a debt, and every morning one of them was there to bind it.{/n}",
           requires=(PALM,))
KNELT_P = p("{n}Minagho never let the Commander forget the kneeling. Neither did Baphomet.{/n}", requires=(KNELT,))
page(P + "epilogue.pair", "Two runaway lilitu", [
    nar("end", '''{n}Two runaway lilitu kept a house in Drezen's lower town after the war, with thick doors, a cellar nobody else knew about, and a linen press that was exactly as deep as it looked, most nights. They kept their own names. They sent the Commander one invitation a year, on their own terms, written in two hands that took turns with the pen. The Commander always went.{/n}''',
        paragraphs=(PALM_P, KNELT_P,
                    p("{n}Chivarro kept the ashes of the bill in a snuffbox, and took it out whenever the Commander forgot who had been bought and who had paid.{/n}",
                      requires=(BURNED,)),
                    p("{n}Some nights the kept door in the Commander's quarters opened on the Delights by itself, and music came through it. The Commander never bricked it up.{/n}",
                      requires=(DOOR,))))],
    requires=("trickster.ever", COMPLETE, CHAIN, "minachiv.future_two"))
page(P + "epilogue.chivarro", "Rent", [
    nar("end", '''{n}Chivarro kept her own house in Drezen after the war and never once let the Commander forget whose name was on the lease. The rent was collected in person, at her convenience, and it went up every year.{/n}''',
        paragraphs=(p("{n}Minagho never came back from Baphomet's ledger. Chivarro kept a second chair at her table anyway, and nobody, not even the Commander, was allowed to sit in it.{/n}",
                      forbids=(MIN_IN,)),
                    p("{n}When Minagho did walk back in, the terms changed, exactly as Chivarro had promised, and the Commander did not get a say.{/n}",
                      requires=(MIN_IN,)),
                    PALM_P))],
    requires=("trickster.ever", COMPLETE, CHAIN, "minachiv.future_chivarro"))
page(P + "epilogue.minagho", "His, every morning", [
    nar("end", '''{n}Minagho stayed in Drezen, unbranded, and kept the Commander's debt the way other women keep a lover's letters: close, and bitterly, and read over and over. Nobody bargained for her again. She saw to that.{/n}''',
        paragraphs=(PALM_P, KNELT_P,
                    p("{n}She never forgave the house that wanted too much for Chivarro. Some nights she went down to the Lower City and made it pay the difference.{/n}",
                      requires=("chivarro.dead.latched",), forbids=(RET_C,)),
                    p("{n}Chivarro came back through the house's back rooms after all, found the terms already signed without her, and renegotiated them, loudly, for a week.{/n}",
                      requires=(RET_C,))))],
    requires=("trickster.ever", COMPLETE, CHAIN, "minachiv.future_minagho"))
page(P + "epilogue.owned", "Goods", [
    nar("end", '''{n}Chivarro stayed in Drezen, owned, on paper, at the Commander's door, and never once let it be mistaken for anything else. She was never seen to smile at the Commander again. She was never seen to leave. Minagho visited her there, and did not speak to the Commander at all.{/n}''')],
    requires=("trickster.ever", KEPT))
# R2-6: a late commit for a Commander whose chain stopped before the question.
page(P + "epilogue.commit", "One invitation a year", [
    nar("start", '''{n}The war ended before the question was asked.{/n}''',
        c("Continue", "pair", requires=(T_HOUSE,)),
        c("Continue", "waiting", forbids=(T_HOUSE,))),
    nar("pair", '''{n}Two runaway lilitu kept a house in Drezen's lower town after the war, with thick doors and a cellar nobody else knew about. The first year, they sent the Commander one invitation, on their own terms, written in two hands.{/n}''',
        c("[Go.]", "went"),
        c("[Send your regrets.]", "regrets")),
    nar("waiting", '''{n}Chivarro kept a room in Drezen's lower town after the war, waiting for someone who had not come back, and let it be known that the Commander still owed her an answer. The first year, she sent one invitation, on her own terms.{/n}''',
        c("[Go.]", "went"),
        c("[Send your regrets.]", "regrets")),
    nar("went", '''{n}The Commander went. The door was barred from the inside with a chair, and opened anyway. The Commander went every year after that.{/n}'''),
    nar("regrets", '''{n}The Commander sent regrets. The next year's invitation came anyway, and the year after that. They were patient in the way demons are patient: badly, and with knives.{/n}'''),
], requires=("trickster.ever",), forbids=(COMPLETE, CLOSED, DECLINED, KEPT), any_groups=[[T_HOUSE, WAITING]])
page(P + "epilogue.declined", "When it scars", [
    nar("end", '''{n}They waited to be asked again, as demons wait: badly, and with knives. The Commander's palm never scarred.{/n}''')],
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
             entry='"About Chivarro."'),
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

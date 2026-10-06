"""Last Call, the extended Trickster ending (Writer/handoffs/04-TRICKSTER-EXTENDED-ENDING.md), and the Trickster's Ledger
(08-TRICKSTER-HOUSEHOLD.md §2.1, the Debts section, built on the E15 journal entries).

The last joke is the flask. Areelu's soul vessel, taken from her laboratory in Chapter 3 (SoulJar/Answer_0006), drinks the
Commander's wound (Cue_0001, Cue_0019) and is "a magical repository for a soul... currently empty" (Cue_0014). In Chapter 5
the Commander drains the wound into it, at the Fool King's table or alone. At Threshold they call last orders: every debt
they themselves ran up is called in, one line each, and the Worldwound finds a Commander whose death is already bottled or
already owed. Nothing is made true by fiat here: the bottle is the Trickster's one signature joke (Kyado Cue_0109), and every
other line is a debt the player created on a route. Pharasma is never cheated: the flask catches a soul before judgment,
and whoever uncorks it collects.

Partner pages, call-in lines and the household groundwork live in lastcall_partners.py."""

import copy

from story_format import c, n, p, scene
from storylines import trickster_world
from storylines import lastcall_ledger as ledger
from storylines import lastcall_partners as partners

REL = "lastcall"
STARTED = "trickster.lastcall.started"
CLOSED = "trickster.lastcall.closed"            # never set: the ledger closes by being settled, not refused
TAKEN = "trickster.lastcall.taken"              # the CommittedFlag: the last joke was told
OPEN = "trickster.lastcall.open"                # last orders called; the call-in lines and the last joke appear
PRIMED = "trickster.lastcall.primed.bottle"
BLESSED = "trickster.lastcall.king_blessed"
PILLAR_BOTTLE = "trickster.lastcall.pillar.bottle"
CREDITORS_CALLED = "trickster.lastcall.creditors_called"   # a power was called in: the Collectors page
HEROIC = "trickster.lastcall.heroic"
COST_BOTTLED = "trickster.lastcall.cost.bottled"
COST_LATE = "trickster.lastcall.cost.late"
COST_ALONE = "trickster.lastcall.cost.bled_alone"
COST_ROUND = "trickster.lastcall.cost.royal_round"
COST_TAB = "trickster.lastcall.cost.royal_tab"
COST_MORTAL = "trickster.lastcall.cost.mortal"
JOKE = {"late": "trickster.lastcall.joke.late", "missed": "trickster.lastcall.joke.missed",
        "funeral": "trickster.lastcall.joke.funeral"}

VESSEL = "lastcall.vessel"
ACTIVE = "lastcall.active"
H1 = "lastcall.h1"
H2 = "lastcall.h2"
ON_RECORD = "lastcall.dead_on_record"

KING_LIST = "6dccfd39947ef4242a8afbe36b21a46c"     # c3/Mythic_Trickster/FoolKing_Tavern/AnswersList_0054 (Chapter 5)
KING_RETURN = "7b050ba0745bf144e815632e39b34853"   # FoolKing_Tavern/Cue_0065 "Beer is a noble drink!" -> AnswersList_0054
# GrandFinal lists that hold the self-sacrifice answer (Answer_0017 "[Step into the Wound]") beside the punchline (Answer_0011).
SACRIFICE_LISTS = ["294126e3264796e488ce19bfb1851355",   # c6/SecondFloor/GrandFinal/AnswersList_0005 (the final decision)
                   "16994192cfa484744bd10852b8dc806f"]   # GrandFinal/AnswersList_0127 (after Iomedae's Cue_0085)
# The Areelu-punchline lists: no self-sacrifice answer there, so the heroic choice is not offered.
AREELU_LISTS = ["b6bc1d5fb28e115499b8bcbbc0d541f9",      # GrandFinal/AnswersList_0052 (Areelu: "I regret nothing.")
                "3d3357c0474ce5a4bb13d68730faecb8",      # c6/SecondFloor/AreeluBurnTheWitch/AnswersList_0071
                "e77c405d6dde5804bb1f873f971958b8"]      # c6/TrueEnding/Suggest/AnswersList_0037
FINAL_LISTS = SACRIFICE_LISTS + AREELU_LISTS
TRICKSTER_PAGE = "fb42f8bd123bf1f40a448f6dbc66cbbe"      # Epilogues/BookPage_0147, the Trickster ending
SACRIFICE_PAGE = "8f234537d0e0e504ba7fa281f02a3601"      # Epilogues/BookPage_0115 ("The great deed demanded a great sacrifice")

RELATIONSHIP = dict(
    Title="The Trickster's Ledger",
    Description=("Every tab I've run, every favour I owe, every creditor who'd rather I stayed alive long enough to pay. "
                 "Somebody ought to keep the accounts. I suppose it had better be me, since nobody else would believe them."),
    Objective="Settle the tab before the last joke",
    Guidance=("Keep the vessel from Areelu's laboratory. In Chapter 5, let it drink from your wound at the Fool King's table, "
              "or alone if there is no King. At Threshold, before the final choice, call last orders."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=TAKEN, UnavailableFlags=["trickster.failed"], FailureFlags=[],
    JournalEntries=[],   # filled below from partners.DEBTS and partners.PARTNERS
)

SCENES = []


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, **kw)


def king(id, text, *choices):
    return n(id, "conversant", text, *choices)


# --- Chapter 5: the bottle ------------------------------------------------------------------------------------------------

JOKE_LINES = (
    ("late", '"Sorry I\'m late."'),
    ("missed", '"Did I miss anything?"'),
    ("funeral", '"Whose funeral?"'),
)


def _round(joke):
    flags = (PRIMED, BLESSED, STARTED, JOKE[joke])
    return king("round." + joke, '''"Ha! Somebody write that down. No, don't. It's funnier if nobody can prove it."
{n}Thaberdine holds his mug out over the vessel the way a priest holds out a hand, and some of the foam slops onto the crystal. He seems to think that is part of the rite.{/n} "Now. A royal blessing costs a round for the whole court. That's the law. I made it this morning."''',
        c('[Stand the whole court a round] "Everybody drinks. On the crusade."', flags=flags + (COST_ROUND,),
          crusade=("Finances", -200)),
        c('[Just the blessing, Majesty] "Put it on my tab."', flags=flags + (COST_TAB,)))


SCENES.append(scene("trickster.lastcall.bottle.king", "Last orders", "Fool King", 5,
    '''[Show the King the flask] "Your Majesty, you once offered me your kingly help. I'm taking you up on it."''', [
    king("offer", '''"My kingly help! I said that, didn't I?" {n}Thaberdine wipes his mouth and squints at the vessel in your hand, at the veins in the crystal, gone from violet to pink.{/n} "I say a lot of things. But a king's word is better than a king's beer, and my beer's excellent. That's the pot you found at the moonshiner's hut. What are you going to brew in it? Not my recipe, I hope. My recipe is a state secret."''',
        c('[Open your shirt] "My own recipe."', "drink"),
        c('[Put it away] "Another night, Majesty."', abort=True)),
    nar("drink", '''{n}The wound under your ribs has not closed since Iz, and tonight it does not pretend to. You press the crystal to it and the vessel drinks, as it drank in Areelu's laboratory: a clear, stinging trickle, moonshine where blood ought to be. Then something else goes. The pull that has lived under your ribs since Iz, the slow drag toward the rift that no healer could name, lets go of you and runs down into the crystal, and settles at the bottom like dark silt. The vessel grows heavy and warm. Nothing is pulling. You had forgotten what that was like. The tavern goes quiet, then louder, because the King has decided this is a performance.{/n}
"A toast!" {n}Thaberdine is up on the bench.{/n} "To the Commander, who is bottling {mf|himself|herself} for later! What's the first thing you'll say when they open you, eh? Make it a good one. It'll be quoted."''',
        *(c("[Decide your first words] " + line, "round." + joke) for joke, line in JOKE_LINES)),
    *(_round(joke) for joke, _ in JOKE_LINES),
], requires=("trickster", "trickster.ever", VESSEL, "fool_king.available"), forbids=(PRIMED, "trickster.failed"), last=5,
    Relationship=REL, AnswerLists=[KING_LIST], NativeReturnCue=KING_RETURN, Chapters=[5]))

SCENES.append(scene("trickster.lastcall.bottle.alone", "Last orders, alone", "Commander", 5, "", [
    nar("alone", '''{n}There is no King to bless it and no court to drink to it. There is a cot, a candle and the vessel from Areelu's laboratory, heavier than crystal ought to be. The wound under your ribs opens without being asked. You press the vessel to it and listen to it fill: a thin, clean trickle that smells of a still in a burned village. Then the pull goes, the slow drag toward the rift that has lived under your ribs since Iz. It runs out of you and down into the crystal, and settles at the bottom like dark silt, and the vessel grows heavy in your hands.{/n}
{n}Nobody asks what you'll say when they open it. You decide anyway, out loud, to an empty tent, so that somebody will have heard it.{/n}''',
        *(c("[Decide your first words] " + line, flags=(PRIMED, STARTED, COST_ALONE, JOKE[joke])) for joke, line in JOKE_LINES),
        c("[Cork it and sleep] Not tonight.", abort=True)),
], requires=("trickster", "trickster.ever", VESSEL), forbids=("fool_king.available", PRIMED, "trickster.failed"), last=5,
    Relationship=REL, Remote=True))


# --- Chapter 6: last orders at the rift -----------------------------------------------------------------------------------

FINAL_RETURN = "{n}The Wound waits. So does everyone you owe.{/n}"


def at_the_rift(id, title, entry, nodes, requires, forbids=(), lists=FINAL_LISTS, **extra):
    SCENES.append(scene(id, title, "Commander", 6, entry, nodes, requires=requires,
                        forbids=(TAKEN, "trickster.failed") + tuple(forbids), last=6, optional=True, Relationship=REL,
                        Chapters=[6], AnswerLists=list(lists), ReturnToList=True, ReturnText=FINAL_RETURN, **extra))


at_the_rift("trickster.lastcall.threshold", "Last orders",
    '''[Call last orders] "Before anyone does anything final: last orders. I've a tab to settle."''', [
    nar("flask", '''{n}The flask is warm against your ribs. It has been warm since the night in Drezen when the wound drained into it like a tap into a jug. Areelu's crystal; Areelu's veins, gone the colour of cheap pink wine. The dark silt at the bottom, the pull you poured into it in Drezen, stirs toward the rift and cannot reach it through the cork.{/n}
{n}Across the rift, Areelu sees it. She knows her own work.{/n}''',
        c('[Uncork the flask] "See this? My death. Bottled in Drezen. You\'ll have to go through the bottle."',
          flags=(OPEN, PILLAR_BOTTLE), requires=(PRIMED,)),
        c('[Hold the flask to the wound] "Last time you drank from me, you tasted of moonshine. Drink up."',
          flags=(OPEN, PILLAR_BOTTLE, COST_LATE, JOKE["funeral"]), requires=(VESSEL,), forbids=(PRIMED,)),
        c("[Put it away] Not yet.", abort=True)),
], requires=("trickster", "trickster.ever", VESSEL), forbids=(OPEN,), EntryMythic="PlayerIsTrickster")

LAST_JOKE_TEXT = '''{n}The rift howls. The violet fire leans toward you as it always has, the way a hound leans toward its master's scent, and finds the wound it made already drained: everything that ran out of it since Iz ran into Areelu's crystal, and the crystal is corked. The fire gropes along the old scar for something to pull, and finds nothing on the other end of it. The Worldwound hesitates.{/n}'''


def last_joke(id, lists, heroic):
    choices = [
        c('[Tell the Wound it\'s too late] "Sorry. My death\'s already been served. Try the flask."',
          flags=(TAKEN, COST_BOTTLED), requires=(PILLAR_BOTTLE,)),
    ]
    if heroic:
        choices.append(c('[Keep the cork in] "If the world needs me in the Wound, fine. It\'ll have to give me back after."',
                         flags=(TAKEN, HEROIC, COST_BOTTLED, COST_MORTAL), requires=(PILLAR_BOTTLE,)))
    choices.append(c("[Not yet] Not yet.", abort=True))
    # The joke waits until every open debt's call-in is resolved (spoken, or explicitly left).
    debts = partners.open_debts()
    at_the_rift(id, "The last joke", '"That\'s everyone. Last call."', [nar("wound", LAST_JOKE_TEXT, *choices)],
                requires=("trickster", "trickster.ever", OPEN), lists=lists,
                forbids=("trickster.lastcall.last_joke.areelu" if heroic else "trickster.lastcall.last_joke",) + tuple(debts))


last_joke("trickster.lastcall.last_joke", SACRIFICE_LISTS, heroic=True)
last_joke("trickster.lastcall.last_joke.areelu", AREELU_LISTS, heroic=False)


# --- Block A: the report, interrupted (native PlayerFinalChoice sequence, E14a) -------------------------------------------

def block_a(id, title, text, requires, after, paragraphs, forbids=()):
    # eng7-f2: these epilogue surfaces are narration, including quoted recollections.
    text = "{n}" + text + "{/n}"
    paragraphs = [{**para, "Text": "{n}" + para["Text"] + "{/n}"} for para in paragraphs]
    # end eng7-f2
    SCENES.append(scene(id, title, "Epilogue", 1, "", [nar("page", text, paragraphs=paragraphs)],
                        requires=("trickster.ever",) + tuple(requires), forbids=("trickster.failed",) + tuple(forbids),
                        last=99, Relationship=REL, EpilogueSequence="PlayerFinalChoice", EpilogueAfter=after))


block_a("trickster.lastcall.page.interrupted", "The Report, Interrupted",
    '''The report should have ended there. I had written the ending, I had underlined it, and I had begun on the lessons. Then the Commander walked out of the rift with a hip flask in one hand, patting at a wound that should have been the end of {mf|him|her}, and I was obliged to take up my pen again. Understand that I do this under protest. An experiment that refuses to conclude is not a success; it is an embarrassment with good timing.''',
    (H1,), TRICKSTER_PAGE, (
        p('''I had already been interrupted once. The Commander asked for a better ending, and I obliged. I did not expect to be asked twice, and certainly not by the ending itself.''', requires=("trickster.rewrote",)),
        p('''The vessel was mine. I made it for a purpose I will not set down here. {mf|He|She} stole it from my laboratory to brew moonshine, and then used it to hold the one thing I had spent the whole war arranging to collect. I would admire it, if it had been done to anyone else.''', requires=(PILLAR_BOTTLE,)),
        p('''The vessel did not settle {mf|his|her} accounts. It only kept {mf|him|her} alive long enough to be dunned. The powers {mf|he|she} had borrowed from came to collect in the first year, and I record their visits in the proper place.''', requires=(CREDITORS_CALLED,)),
        p('''Shyka still waits, as Shyka always does. The Commander who walked out of the rift was the Commander who walked in: not a chorus, not a vessel for other versions of {mf|himself|herself}, one person, badly behaved. The death Shyka meant to share was in a bottle, and Shyka does not drink.''', requires=("ending.trickster_allplanes_fw",)),
        p('''I was the punchline, as {mf|he|she} promised. And the slow death I had arranged for {mf|him|her}, the wound that would have killed {mf|him|her} the moment the rift stayed open, went instead into a flask. I have been told this is poetic. I have been told this by the Commander.''', requires=("areelu.sacrifice_trickster",), forbids=("sacrifice",)),
        p('''The world buried an empty coffin. There were speeches. The Commander attended several of them, disguised, and was once asked to leave for laughing.''', requires=(ON_RECORD,)),
    ))

block_a("trickster.lastcall.page.heroic", "The Report, Interrupted",
    '''The sacrifice was real. I have checked. The Commander of the Fifth Crusade stepped into the Wound, and the Wound closed on everything {mf|he|she} had carried into it: the power the Abyss and I had poured into {mf|him|her}, spent to the last spark to seal the rift. I recorded it, correctly, as the end. I record also what I measured, and do not pretend to understand. The wound in {mf|his|her} chest was mine; I cut it, and I built the Worldwound to finish what it began by pulling through it. By Threshold that wound had been drained, in Drezen, into a crystal vessel of my own making, and corked. When the Wound closed, it pulled on the old cut and found nothing on the other end. Three days later a sentry found the Commander at the edge of the scorched earth where the rift had been, breathing, with the flask still corked in one fist.''',
    (H2,), SACRIFICE_PAGE, (
        p('''{mf|He|She} was carried back to Drezen and set down at the King's table, under a toast. Thaberdine swore afterwards that it was the luckiest round he ever called, and the church of Cayden Cailean has not stopped repeating it.''', requires=(BLESSED, "fool_king.available")),
        p('''{mf|He|She} was carried back to Drezen and laid on the cathedral steps, where the priests had already begun the rites for {mf|him|her}. I am told several of them have not recovered.''', forbids=(BLESSED,)),
        p('''{mf|His|Her} first words were "Sorry I'm late." I will not pretend I did not hear them.''', requires=(JOKE["late"],)),
        p('''{mf|His|Her} first words were "Did I miss anything?" Yes. You missed your own funeral. I attended, for professional reasons.''', requires=(JOKE["missed"],)),
        p('''{mf|His|Her} first words were "Whose funeral?" I have no answer that would satisfy the question.''', requires=(JOKE["funeral"],)),
        p('''What the Abyss and I gave the Commander went into the Wound and stayed there. {mf|He|She} came back mortal, and complained about it at length. The soul is the Lady of Graves' in the end, as every soul is; the Commander has simply arranged to keep her waiting, and to die, when {mf|he|she} does, of the death {mf|he|she} carries rather than the one the Wound intended.''', requires=(COST_MORTAL,)),
    ))

block_a("trickster.lastcall.page.bottle", "The Bottle",
    '''The Commander carried {mf|his|her} own death in a hip flask for the rest of {mf|his|her} life. It did not slosh. It did not grow lighter. On cold nights it was warm.''',
    (ACTIVE, PILLAR_BOTTLE), TRICKSTER_PAGE, (
        p('''The King's round was paid in full, and the court drank to the flask for a week on the crusade's coin. The treasurers of Mendev entered it as "morale".''', requires=(COST_ROUND,)),
        p('''The King's blessing went on the Commander's tab. Thaberdine's tab has no end and no ledger, and he mentions it every time they meet.''', requires=(COST_TAB,)),
        p('''It had been filled alone, in a tent, with nobody to laugh. The Commander was short of breath for a week afterwards and would not say why.''', requires=(COST_ALONE,)),
        p('''It had been filled late, at the rift itself, and the crystal still carries a hairline crack from it. The Commander keeps a thumb over the crack when {mf|he|she} is nervous.''', requires=(COST_LATE,)),
        p('''Whoever uncorks it, collects. The Commander has made sure a great many people know that, and made just as sure nobody knows where it is kept.''', forbids=(H2,)),
    ))


# --- Block A3: the collectors (one paragraph per creditor who was called and could collect) --------------------------------

def _collectors():
    paras = []
    for debt in partners.DEBTS:
        if debt.get("page_called"):
            paras.append(p(debt["page_called"], requires=("lastcall.debt." + debt["key"],),
                           forbids=tuple(debt.get("outlived", ())), any_groups=[debt["called_by"]]))
        if debt.get("page_outlived"):
            paras.append(p(debt["page_outlived"], requires=("lastcall.debt." + debt["key"],), any_groups=[debt["outlived"]]))
    return tuple(paras)


block_a("trickster.lastcall.page.collectors", "The Collectors",
    '''A debtor who cheats death has not cheated the creditors, and the Commander's were patient, numerous, and in several cases not strictly alive. They came in the first year after Threshold, one after another, and I recorded their visits with more satisfaction than is proper in a scholar.''',
    (ACTIVE, CREDITORS_CALLED), TRICKSTER_PAGE, _collectors())


# --- Block C: the last word (the end of the RanRomAdd sequence) ------------------------------------------------------------

LAST_WORD = scene("trickster.lastcall.page.last_word", "The Last Word", "Epilogue", 1, "", [
    nar("page", '''That concludes my report on the experiment called the Commander. It did not end as designed. It did not end at all, which I am told is the point. I have spent a very long time building a death for {mf|him|her}, and I would like it noted, for the benefit of whoever reads this after me, that the death is still in excellent condition. It is simply in the wrong place. Somebody will open it one day. I intend to be there.''',
        paragraphs=(
            p('''I have been asked to rewrite this ending twice now. I am not doing it a third time.''', requires=("trickster.rewrote",)),
            p('''The Fool King reigned over the merry city of Drezen for many years, and hosted one festival after another. People said that anyone who raised a glass to His Majesty's health had luck. The Commander raised a great many glasses, and would tell you that proves it.''', requires=("fool_king.available",), forbids=("fool_king.page_seen",)),
        ))],
    requires=("trickster.ever", ACTIVE), forbids=("trickster.failed",), last=99, Relationship=REL)


# eng7-f2: the separately constructed final page is narrative too.
LAST_WORD["Nodes"][0]["Text"] = "{n}" + LAST_WORD["Nodes"][0]["Text"] + "{/n}"
for _paragraph in LAST_WORD["Nodes"][0]["Paragraphs"]:
    _paragraph["Text"] = "{n}" + _paragraph["Text"] + "{/n}"
# end eng7-f2

# --- The Ledger's lines (E15) -------------------------------------------------------------------------------------------

RELATIONSHIP["JournalEntries"] = ledger.journal_entries()


# --- Derived keys (added to the payload; trickster_world binds the native readers they use) --------------------------------

def derived():
    debts = {"lastcall.debt." + d["key"]: [list(g) for g in d["groups"]] for d in partners.DEBTS}
    finals = ("ending.trickster", "ending.trickster_full", "ending.trickster_allplanes", "ending.trickster_allplanes_fw")
    h1 = [[TAKEN, e] for e in finals]
    h2 = [[TAKEN, "ending.wound_closed", "sacrifice", PILLAR_BOTTLE]]
    out = dict(debts)
    out[VESSEL] = [["lastcall.flask_taken", "lastcall.flask_held"]]
    out[H1] = h1
    out[H2] = h2
    out[ACTIVE] = h1 + h2
    out[ON_RECORD] = [g + ["sacrifice"] for g in h1] + h2
    out.update(partners.derived())
    return out


def integrate(payload):
    """Register the framework, the partner pages and the Ledger lines, and quiet every mourning page on a Last Call run."""
    payload["Relationships"][REL] = copy.deepcopy(RELATIONSHIP)
    # The Ledger as a readable book (E15 book UI, 09-RRT-BOOK-UI.md); the journal quest stays the native entry point.
    payload.setdefault("Books", {})["trickster.ledger"] = ledger.book()
    for key, groups in derived().items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != groups:
            raise ValueError("Conflicting Last Call derived key: " + key)
        payload["Derived"][key] = groups
    # Engine-q2 item 3: each partner coda plays only while her route is open (a return reopens it).
    for key, (groups, routes) in partners.page_guards().items():
        if any(rel not in payload["Relationships"] for rel in routes) or key in payload["Derived"]:
            raise ValueError("Last Call coda guard: unknown route or conflicting key: " + key)
        payload["Derived"][key] = groups
        payload.setdefault("DerivedOpenRoutes", {})[key] = list(routes)
    # Engine-q2 item 3: each call-in is due only while its partner's route is open (and its debt unresolved).
    for key, (groups, routes, forbids) in partners.call_guards().items():
        missing = [rel for rel in routes if rel not in payload["Relationships"]]
        if missing or key in payload["Derived"]:
            raise ValueError("Last Call call-in guard: unknown route or conflicting key: " + key)
        payload["Derived"][key] = groups
        payload.setdefault("DerivedOpenRoutes", {})[key] = list(routes)
        payload.setdefault("DerivedForbids", {})[key] = list(forbids)
    # trickster_world.integrate expands only its own composites, so bind the native readers these composites stand on.
    for leaf in sorted({k for groups in derived().values() for g in groups for k in g}):
        if leaf in trickster_world.BINDINGS and not trickster_world._bound(payload, leaf):
            kind, guid, _ = trickster_world.BINDINGS[leaf]
            payload.setdefault(kind, {})[leaf] = [guid] if kind in trickster_world.LIST_KINDS else guid
    scenes = payload["Scenes"]
    # L6 (doc 04 §4.2): an epilogue that mourns the Commander never plays beside a Commander who walked out of the rift.
    for s in scenes:
        if s.get("Owner", "").endswith("Epilogue") and "sacrifice" in (s.get("Requires") or []) and ACTIVE not in s["Forbids"]:
            s["Forbids"].append(ACTIVE)
    for extra in partners.FORBID_ACTIVE:
        target = next(s for s in scenes if s["Id"] == extra)
        if ACTIVE not in target["Forbids"]:
            target["Forbids"].append(ACTIVE)
    scenes.extend(copy.deepcopy(SCENES))
    scenes.extend(copy.deepcopy(partners.call_in_scenes(at_the_rift_scene)))
    # Block B: each partner's coda plays right after her own ending pages in the RanRomAdd sequence.
    for rel, page in copy.deepcopy(partners.pages()):
        last = max((i for i, s in enumerate(scenes) if (s.get("Relationship") or "tirabade") == rel
                    and s.get("Owner", "").endswith("Epilogue")
                    and s.get("EpilogueSequence") is None and s.get("Owner") != "AeonEpilogue"), default=None)
        if last is None:
            scenes.append(page)
        else:
            scenes.insert(last + 1, page)
    scenes.append(copy.deepcopy(LAST_WORD))


def at_the_rift_scene(id, title, entry, nodes, requires, forbids=(), any_groups=()):
    """A call-in line at the rift: an E14b inline scene on every final list, shown once last orders are called."""
    extra = dict(RequiresAnyGroups=[list(g) for g in any_groups]) if any_groups else {}
    return scene(id, title, "Commander", 6, entry, nodes, requires=("trickster", "trickster.ever", OPEN) + tuple(requires),
                 forbids=(TAKEN, "trickster.failed") + tuple(forbids), last=6, optional=True, Relationship=REL,
                 Chapters=[6], AnswerLists=list(FINAL_LISTS), ReturnToList=True,
                 ReturnText="{n}The thread pulls taut, and holds.{/n}", **extra)


# eng8-q8g: apply the same historical witnesses to every downstream surface.
_eng8_integrate = integrate


def integrate(payload):
    _eng8_integrate(payload)
    entries = {e["Id"]: e for e in payload["Books"]["trickster.ledger"]["Entries"]}
    # esc1-shared: acquisition history changes wording only, including a pending rider return.
    entries["owed.seelah"]["Lines"].extend([
        p("{n}I took the seller's stones without paying him. They were for Seelah's rite.{/n}",
          forbids=("seelah.trickster.cost.seller_paid", "seelah.trickster.cost.seller_taken")),
        p("{n}I had the seller arrested and kept the stones for the rite by my order. The court lost its evidence; I lost its favors.{/n}",
          requires=("seelah.trickster.cost.seller_taken",), forbids=("seelah.trickster.cost.seller_paid",)),
        p("{n}My lift failed. Crusade gold bought the stones and the seller's silence. He left richer. I will have to answer for that.{/n}",
          requires=("seelah.trickster.cost.seller_paid",)),
    ])
    entries["owed.eliandra"]["Lines"].append(p(
        "{n}She asks me a question every morning. She has a hundred years of them saved up.{/n}",
        requires=(partners.EL_DAILY,)))
    entries["owed.wenduag"]["Lines"].append(p(
        "{n}The knife-marked stone she left in my coat is still in my pocket.{/n}",
        requires=(partners.WD_POCKET,)))
    # Last Call activity resolves the spoken calls, not an unaccepted pardon.
    entries["debt.abadar"]["Lines"][-1]["Requires"] = [partners.called("arsinoe")]
    abadar_journal = next(e for e in payload["Relationships"][REL]["JournalEntries"] if e["Id"] == "debt.abadar")
    abadar_journal["SettledWhen"] = [[partners.called("arsinoe")]]
    sunhammer = entries["debt.sunhammer"]
    sunhammer["Lines"][-1]["Requires"] = [partners.KI_SETTLED]
    journal = next(e for e in payload["Relationships"][REL]["JournalEntries"] if e["Id"] == "debt.sunhammer")
    journal["SettledWhen"] = [[partners.KI_SETTLED], ["kiana.sunhammer_dead"]]
    for host in payload["Scenes"]:
        for node in host["Nodes"]:
            for para in node.get("Paragraphs", []):
                if host["Id"] == "trickster.lastcall.page.collectors":
                    if para["Text"].startswith("{n}" + partners._history_debts["sunhammer"]["page_called"]):
                        para["Requires"].append(partners.KI_SETTLED)
                # Retained Kiana ending paragraphs must follow actual release,
                # not the historical fact that a call was spoken.
                if host.get("Relationship") == "kiana" and "kiana.lastcall.called" in para.get("Forbids", []):
                    witness = partners.KI_RECOVERED if "pouch" in para["Text"] or "promise to fetch" in para["Text"] else partners.KI_SETTLED
                    para["Forbids"] = [witness if key == "kiana.lastcall.called" else key for key in para["Forbids"]]
# end eng8-q8g

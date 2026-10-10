"""Nurah's appended promise and outcome readers.

Approved text is authored in the route, continuation, S35, and Last Call
builders. These readers append after existing paragraphs, keeping indices.
"""
from story_format import p

R = "nurah.trickster."
GOOD, CHAOS, EVIL = R + "temper_good", R + "temper_chaos", R + "temper_evil"
IRABETH_ALIVE = ("irabeth.present_now", "crossroute.irabeth.available")

ADD = {}


def add(scene, node, *paras):
    ADD.setdefault((scene, node), []).extend(paras)


TEMPER = (
    p('''{n}The Commander had kept her because she could still write the war properly, and she did: every order, every grave, every name from under the wall at Bottleneck Gate, ticked in her own hand where she had pointed the demons at them. The crusade's chroniclers called it the most accurate book about the Worldwound and the most hateful, and never managed to make the two halves of that sentence disagree.{/n}''',
      requires=(GOOD,)),
    p('''{n}The Commander had kept her because it was funnier with her in it, and the book was funnier than anything anybody had written about the Worldwound, which was a low bar that she cleared by a height. The Queen's court banned it over chapter four, which is about the Queen's court. Nurah had the ban bound into the second edition as a frontispiece.{/n}''',
      requires=(CHAOS,), forbids=(GOOD,)),
    p('''{n}The Commander had kept her to watch her sell them all again, and she obliged. The book named the officers who had hanged Deskari's cultists at Drezen without a trial, with their home towns and the inns they drank in, and what was left of those cults paid her well for an early copy. Two of the officers were found in ditches before the second printing. She sent the Commander the broadsheet notices, underlined in red, with one word written across them: "Watching?"{/n}''',
      requires=(EVIL,), forbids=(GOOD, CHAOS)),
)
IRABETH = (
    p('''{n}Irabeth read the book in one night at the gaol desk. Chapter nine has a halfling reading casualty lists by a stolen candle, and a Commander telling the Knight-Captain it was rats. Irabeth wrote "Literate" in the margin, and never again asked the Commander a question she could not check herself.{/n}''',
      requires=(R + "cost.irabeth_lied_to",) + IRABETH_ALIVE),
    p('''{n}Irabeth bought a copy and found herself in chapter nine, letting a thing go because the Commander asked her to. Nurah had got every word of it, down to the tone. Irabeth never forgave her for that, or the Commander either, and she kept the copy.{/n}''',
      requires=(R + "cost.seen",) + IRABETH_ALIVE, forbids=(R + "cost.irabeth_lied_to",)),
)
TYMON = p('''{n}The Tymon printer who had pirated her second printing found himself in the acknowledgments, his name spelled correctly beside the crusade silver he had taken to keep a certain dedication locked in his forme. He left Tymon that winter, owing money to men who break fingers. Nurah framed the notice of his debts and hung it over her desk.{/n}''',
          requires=(R + "cost.second_edition",))

for sid, nid in ((R + "epilogue.the_margin", "start"), (R + "epilogue.commit", "read"),
                 (R + "epilogue.commit", "went"), (R + "epilogue.book_only", "start")):
    add(sid, nid, *TEMPER, *IRABETH, TYMON)

# the_margin also closes the parent romance (nurah.payoff.ordinary): the terms it quotes must be true there too, and
# the Vhal affair gets its chapter.
add(R + "epilogue.the_margin", "start", p(
    '''{n}Istrene Vhal got a chapter of her own near the end, short and unforgiving. Nurah read it aloud at a Nerosyan salon where half of Vhal's old subscribers were guests, and watched each of them work out which of the anonymous fools was him.{/n}''',
    requires=("nurah.copies_settled",)))

# Last Call: cost.name_above is the Commander's demand for a name above hers, refused (terms/refused). The page had
# it backwards. (Unreachable on a shipped save: that refusal also closes the route; corrected so it cannot mislead.)

# ---------------------------------------------------------------------------------------------------------------------
# Parent continuation (claude-work-queue nurah:D06-D11). Every visit is delivered at Nurah's arrival at the
# Commander's private door in Drezen (nurah.arrival). The other people now come up her stair; nothing narrates a walk
# to a wine merchant's back room that the encounter never stages.
# ---------------------------------------------------------------------------------------------------------------------
P = "nurah."


# Nurah leads the interview: the cruelty is on the table, not in the margin.

S = P + "the_case_goes_missing"


# The chaos settlement and the evil collection: the people the paper hurts are on the page, and she likes it.

# a_margin_for_you/morning: Vhal is not finished on every history. The five outcomes of the copies now have a reader.
S = P + "a_margin_for_you"
add(S, "morning",
    p('''{n}On the table, beside the glove, lies the correction with Vhal's signature under the words "unsupported testimony". Nurah taps it on her way past, the way a cat taps a mouse to see whether it still moves.{/n}''',
      requires=(P + "outcome_correction",)),
    p('''{n}Somewhere in the lower city three families are still at each other's throats over the packets she chose for them. She hums while she dresses.{/n}''',
      requires=(P + "outcome_rivals",)),
    p('''{n}The paired dedications lie on the table. She has inked a pair of donkey's ears over one patron's printed name and left the other clean, so that he will spend a week wondering why.{/n}''',
      requires=(P + "outcome_limited",)),
    p('''{n}Vhal's private files live in a box under your bed now, because Nurah says nobody searches under a Commander's bed. You suspect she has already sold two of them.{/n}''',
      requires=(P + "outcome_collection",)),
    p('''{n}The scrap she kept on the night you refused her the collection is no longer in her sleeve. You do not ask where it went. She notices you not asking, and smiles.{/n}''',
      requires=(P + "outcome_distance",)))

# ---------------------------------------------------------------------------------------------------------------------
# Household S35 (Arsinoe, Nurah): a forged stores demand. Villainy by freight arithmetic becomes her grudge on screen:
# the syrup belongs to the east ward, where the men who caught her lie wounded. Arsinoe still catches it by
# arithmetic (Abadar's ledger is her method); every flag, check and method is unchanged.
# ---------------------------------------------------------------------------------------------------------------------
H = "household.pair.arsinoe_nurah."


# ---------------------------------------------------------------------------------------------------------------------
def _scenes(payload):
    return {s["Id"]: s for s in payload["Scenes"]}


def _node(scenes, sid, nid):
    if sid not in scenes:
        raise ValueError("nurah cloud: missing scene %s" % sid)
    hits = [x for x in scenes[sid]["Nodes"] if x["Id"] == nid]
    if len(hits) != 1:
        raise ValueError("nurah cloud: missing node %s/%s" % (sid, nid))
    return hits[0]


# A harem-row scene from another row: present whenever storylines.harem_rows.register_all ran. The test fixture's
# base story (tests/story_fixture.py, include_harem=False) builds without any row; only then are S35's scenes skipped.
ROW_SENTINEL = "household.pair.herrax_chivarro.turf.live"


REVIEWED_SCENES = ['household.pair.arsinoe_nurah.audit', 'household.pair.arsinoe_nurah.retry', 'nurah.a_margin_for_you', 'nurah.a_page_with_teeth', 'nurah.lastcall.page', 'nurah.the_borrowed_audience', 'nurah.the_case_goes_missing', 'nurah.the_copies_that_survive', 'nurah.the_editor_opens', 'nurah.the_price_of_a_warning', 'nurah.the_subscribers_evening', 'nurah.the_unpurchased_sentence', 'nurah.trickster.epilogue.book_only', 'nurah.trickster.epilogue.commit', 'nurah.trickster.epilogue.the_margin', 'nurah.trickster.prison.night_out', 'nurah.trickster.prison.night_out_late', 'nurah.trickster.react.irabeth_manuscript']

def integrate(payload):
    scenes = _scenes(payload)
    rows_absent = H + "audit" not in scenes and ROW_SENTINEL not in scenes
    for (sid, nid), paras in ADD.items():
        if rows_absent and sid.startswith(H):
            continue
        node = _node(scenes, sid, nid)
        node["Paragraphs"] = node.get("Paragraphs", []) + [dict(x) for x in paras]
    for sid in REVIEWED_SCENES:
        if rows_absent and sid.startswith(H):
            continue
        for node in scenes[sid]["Nodes"]:
            texts = [node["Text"]] + [c["Text"] for c in node["Choices"]] + [x["Text"] for x in node.get("Paragraphs", [])]
            if any("[PROSE PENDING" in t for t in texts):
                raise ValueError("nurah cloud: prose still pending at %s/%s" % (sid, node["Id"]))

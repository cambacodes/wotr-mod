"""The Trickster's household: the Table (Writer/handoffs/08-TRICKSTER-HOUSEHOLD.md), system only.

Built now (memory rrt-harem-order): the hub, the stance hooks (05-HAREM-HOOKS.md), the Ledger's Guest List / Seating Notes /
Secrets sections (09-RRT-BOOK-UI.md contract), the Word Made True counter, the invitation scene kind and their tooltips.
NOT built now: any scene between two partners. Those are written last, through the API below, once every route exists.

THE TABLE (10-HAREM-RESIDENCE.md P1: canon doors only, no new units, no invented hosts)
  The corner table in the Fool King's tavern in Drezen. The door is Thaberdine's own tavern list (FoolKing_Tavern
  AnswersList_0009 in Chapter 3, AnswersList_0054 in Chapter 5, the lists Aranka's round and Last Call use):
  - once at least one partner is eligible, the King offers the table, inline, in his own voice ("household.table.offered");
  - from then on "[The corner table]" (an E16 native opener) sits on the same list. It ends the King's dialog and opens the
    Table menu: the entries available now, six to a page with "[More…]", then "[Open the Ledger]", then "[Leave the table.]".
  The Crossroads is the Table's slot in the Trickster epilogue (08 §9), reserved: EPILOGUE_SLOT below, nothing written.

ENTRY API (for the later pass; see table_entry, invitation, word_made_true)
  table_entry(id, title, entry, nodes, pair=(rel_a, rel_b), trigger="<flag>")  a scene on the Table's hub, gated on the table
      being kept, both women's eligibility, no enmity between them, and a trigger flag that some earlier beat sets. Every
      entry needs a trigger: the hub never offers a scene just because two women exist.
  invitation(id, rel, sender, title, text, trigger)  a rest-delivered note (Kind "invitation": "[<Name> asks you to the
      Table]") whose reply sets the trigger its table_entry waits for.
  word_made_true(text, next=None, use="<id>", flags=())  a choice that spends one of the three uses (08 §10), with a debt.

STANCE HOOKS (05 §2; none of the stance/enmity/attitude flags is set in this pass)
  <rel>.harem.eligible            Derived, for every romance route (below).
  <rel>.harem.stance.joined | .tolerated, <rel>.harem.joined_late, <rel>.harem.enmity.<other>   reserved.
  minagho_chivarro.harem.stance.<minagho|chivarro>.<joined|tolerated> (and enmity/attitude the same way)   reserved.
"""

import copy

from story_format import c, n, scene
from storylines import household_frictions as frictions
from storylines import trickster_world

REL = "household"
STARTED = "household.started"
CLOSED = "household.closed"          # never set: the household is not a romance and cannot be refused
KEPT = "household.table.kept"        # CommittedFlag: the Commander accepted the table
ANY = "household.any_eligible"
KING_GONE = "fool_king.gone"         # trickster_world binding: no King, no tavern list, no door (the UMM button still opens the Ledger)

DREZEN = "2570015799edf594daf2f076f2f975d8"
KING_C3 = "1a17d8053a3be7f47a7908eb6706f2fe"         # c3/Mythic_Trickster/FoolKing_Tavern/AnswersList_0009
KING_C3_RETURN = "814dd1a078a1c2849aefc85e2e15b2d2"  # FoolKing_Tavern/Cue_0008 "Oh, Commander! Nice of you to stop by."
KING_C5 = "6dccfd39947ef4242a8afbe36b21a46c"         # FoolKing_Tavern/AnswersList_0054 (Chapter 5)
KING_C5_RETURN = "7b050ba0745bf144e815632e39b34853"  # FoolKing_Tavern/Cue_0065 "Beer is a noble drink!"
TABLE_HUB = "household.table"        # Rules.TableHub: scenes with this InteractionHub are listed on the Table menu
EPILOGUE_SLOT = "household.epilogue.crossroads"   # reserved (08 §9): the Crossroads page of the Trickster finale

WMT_PREFIX = "trickster.wmt.use."    # the engine counts these (Rules.Complete) into trickster.wmt.left.<n>
WMT_AVAILABLE = "trickster.wmt.available"
WMT_MAX = 3

# The romance relationships at the table (Ember and Aivu are friendship only; lastcall/household are frameworks).
# rel -> (portrait key, display name)
PARTNERS = {
    "tirabade": ("Together", "Anevia and Irabeth"), "anevia": ("Anevia", "Anevia"), "irabeth": ("Irabeth", "Irabeth"),
    "seelah": ("Seelah", "Seelah"), "konomi": ("Konomi", "Konomi"), "jerribeth": ("Jerribeth", "Jerribeth"),
    "kiana": ("Kiana", "Kiana"), "soana": ("Soana", "Soana"), "arsinoe": ("Arsinoe", "Arsinoe"),
    "targona": ("Targona", "Targona"), "gesmerha": ("Gesmerha", "Gesmerha"), "vellexia": ("Vellexia", "Vellexia"),
    "aranka": ("Aranka", "Aranka"), "minagho_chivarro": ("Minagho", "Minagho and Chivarro"),
    "nocticula": ("Nocticula", "Nocticula"), "nurah": ("Nurah", "Nurah"), "dorgelinda": ("Dorgelinda", "Dorgelinda"),
    "hepzamirah": ("Hepzamirah", "Hepzamirah"), "camellia": ("Camellia", "Camellia"), "eritrice": ("Eritrice", "Eritrice"),
    "areelu": ("Areelu", "Areelu"), "chadali": ("Chadali", "Chadali"), "arueshalae": ("Arueshalae", "Arueshalae"),
    "devarra": ("Devarra", "Devarra"), "delamere": ("Delamere", "Delamere"), "kaylessa": ("Kaylessa", "Kaylessa"),
    "nidalynn": ("Nidalynn", "Nidalynn"),
}
# Extra eligibility groups: a woman whose route has a second committed state (Nocticula's acquired harbour).
EXTRA_ELIGIBLE = {"nocticula": [["noct.acq.renewed_agreement"]]}
PAIR_WOMEN = {"minagho_chivarro": ("minagho", "chivarro")}

SCENES = []
ENTRIES = []          # table_entry() registrations (the later pass)
INVITATIONS = []
SECRETS = []          # secret() registrations (the later pass); each shows only when its trickster.secret.<k> flag exists

GLOSSARY = {
    "RRT_Table": dict(Name="The Table",
                      Description="The corner table in the Fool King's tavern, kept for the Commander's household. It "
                                  "lists only what is waiting now: an introduction, an invitation, a seating to settle."),
    "RRT_GuestList": dict(Name="Guest List",
                          Description="Every partner the Commander has won, and where she sits: at the table, at the "
                                      "table but apart from one woman she cannot stand, or not yet at the table."),
    "RRT_SeatingNotes": dict(Name="Seating Notes",
                             Description="The pairs with a real reason to clash, and what might settle each. Settling one "
                                         "takes something done: a trick, an item, a favour, a job. Failing one leaves a "
                                         "woman at the table, apart."),
    "RRT_WordMadeTrueUses": dict(Name="Word Made True: uses",
                                 Description="The Trickster may declare a feud settled and make it so, three times in a "
                                             "campaign. Each use leaves a debt, the women who value the truth notice, and "
                                             "it never works on an atrocity."),
}


def relationship():
    return dict(
        Title="The Table",
        Description=("The King gave me a table in his tavern and a cloth to go on it, and told me I would need the chairs. "
                     "He was right. Now I have to fill them without anybody stabbing anybody."),
        Objective="Keep the Table",
        Guidance=("Visit the corner table in the Fool King's tavern in Drezen. Your partners' introductions and invitations "
                  "wait there. The Ledger's Guest List and Seating Notes show where everyone sits."),
        StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=KEPT, UnavailableFlags=["trickster.failed"],
        FailureFlags=[], JournalEntries=[])


# The native openers: "[The corner table]" on the King's list in each tavern state, once the table is kept.
OPENERS = [
    dict(Id="household.table.c3", Relationship=REL, AnswerList=KING_C3, Text="[The corner table]", View="table",
         Requires=["trickster", KEPT], Forbids=[], MinChapter=3, MaxChapter=4),
    dict(Id="household.table.c5", Relationship=REL, AnswerList=KING_C5, Text="[The corner table]", View="table",
         Requires=["trickster", KEPT], Forbids=[], MinChapter=5, MaxChapter=5),
]


def _table_scene(id, title, owner, entry, nodes, requires, forbids, relationship=REL, **extra):
    """A physical scene on the Table menu (Rules.IsTableScene): no unit, no list; the menu queues it."""
    return scene(id, title, owner, 3, entry, nodes, requires=requires, forbids=forbids, delay=0, last=5,
                 Relationship=relationship, Chapters=[3, 5], Areas=[DREZEN], InteractionHub=TABLE_HUB, **extra)


# --- The one system scene: the King offers the table (inline on his own list; no partner speaks) --------------------

def _king(id, text, *choices):
    """Thaberdine, speaking inline in his own tavern dialog (the native conversant)."""
    return n(id, "conversant", text, *choices)


KEPT_TEXT = '''"Whoever! That's a big word, in my tavern." {n}He thumps the table with the bottom of his mug, which is as close to a royal seal as anything in Drezen gets.{/n} "Sit 'em where you like. But if two of 'em walk in who shouldn't sit together, that's your mess, Commander, not mine. I'm the King. Kings don't do seating."'''


def _offered(id, chapter, hub, back, opening, requires=(), forbids=()):
    return scene(id, "The corner table", "Thaberdine", chapter, '"Your Majesty. Who is the corner table for?"', [
        _king("offer", opening + '''
"My pops always said: a man with more sweethearts than chairs is a man on his way to a stabbing. So! Chairs!" {n}He beams at you as if he had invented furniture.{/n} "Oh. And you're paying for the cloth."''',
              c('"Keep it for me, Your Majesty. Whoever asks for me gets a chair."', "kept"),
              c('"Another time."', abort=True)),
        _king("kept", KEPT_TEXT, c("Continue", flags=(STARTED, KEPT))),
    ], requires=("trickster", ANY) + tuple(requires), forbids=(KEPT,) + tuple(forbids), delay=0, last=chapter,
        optional=True, Relationship=REL, AnswerLists=[hub], NativeReturnCue=back)


SCENES.append(_offered("household.table.offered", 3, KING_C3, KING_C3_RETURN, '''{n}Thaberdine waves you towards the back of the tavern with his mug, and most of the beer goes with the wave. In the corner there is a table with a cloth on it, darned in three colours, and more chairs round it than a corner ought to hold.{/n}
"That one's yours, Commander! Don't argue. It's royal."'''))
SCENES.append(_offered("household.table.offered_c5", 5, KING_C5, KING_C5_RETURN, '''{n}The court has come back from the war louder and fewer. The corner table has not moved. Somebody has put a new cloth on it, darned in three colours, and more chairs round it than there used to be.{/n}
"Kept it for you all through the war, Commander! Well. Kept the corner. Don't argue. It's royal."''', forbids=(KING_GONE,)))


# --- The API for the later pass -------------------------------------------------------------------------------------

def eligible(rel):
    return rel + ".harem.eligible"


def enmity(rel, other):
    return "%s.harem.enmity.%s" % (rel, other)


def table_entry(id, title, entry, nodes, pair, trigger, requires=(), forbids=(), relationship=None, **extra):
    """Register a scene on the Table menu. pair=(rel_a, rel_b); trigger=a flag an earlier beat sets (required).
    `entry` is the menu line (e.g. "[Seelah and Camellia, at the corner table]")."""
    if not trigger:
        raise ValueError("A Table entry needs a trigger flag: " + id)
    a, b = pair
    for rel in pair:
        if rel not in PARTNERS:
            raise ValueError("Unknown household partner %s in %s" % (rel, id))
    body = _table_scene(id, title, PARTNERS[a][0], entry, nodes, requires=("trickster", KEPT, eligible(a), eligible(b), trigger) + tuple(requires),
                        forbids=(enmity(a, b), enmity(b, a)) + tuple(forbids), relationship=relationship or REL, **extra)
    ENTRIES.append(body)
    return body


def invitation(id, rel, sender, title, text, trigger, requires=(), forbids=(), chapter=3, last=5, delay=24):
    """A rest-delivered invitation to the Table (Kind "invitation"). Its reply sets `trigger`."""
    body = scene(id, title, sender, chapter, "", [
        n("start", sender, text, c('"I\'ll be there."', flags=(trigger,)), portrait=PARTNERS[rel][0]),
    ], requires=("trickster", KEPT, eligible(rel)) + tuple(requires), forbids=tuple(forbids) + (trigger,), delay=delay,
        last=last, Relationship=REL, Remote=True, Kind="invitation", Sender=sender)
    INVITATIONS.append(body)
    return body


def word_made_true(text, next=None, use="", flags=()):
    """A choice that spends one Word Made True (max 3 per campaign; Rules.Complete counts trickster.wmt.use.*)."""
    if not use:
        raise ValueError("word_made_true needs a use id")
    return c(text, next, flags=tuple(flags) + (WMT_PREFIX + use, "household.wmt.debt." + use), requires=(WMT_AVAILABLE,),
             mythic="Trickster")


def secret(key, title, text, portrait="", witnesses=(), risk="low"):
    """Register a Secrets entry (the later pass). It shows only when trickster.secret.<key> is held."""
    SECRETS.append(dict(key=key, title=title, text=text, portrait=portrait, witnesses=tuple(witnesses), risk=risk))


# --- Integration ------------------------------------------------------------------------------------------------------

def derived(payload):
    """<rel>.harem.eligible for every partner, and household.any_eligible."""
    rels = payload["Relationships"]
    have = payload.get("Derived", {})
    out = {}
    for rel in PARTNERS:
        committed = rels[rel]["CommittedFlag"]
        groups = [[committed]]
        late = rel + ".trickster.late_committed"
        if late in have:
            groups.append([late])
        groups += EXTRA_ELIGIBLE.get(rel, [])
        out[eligible(rel)] = groups
    out[ANY] = [[eligible(rel)] for rel in PARTNERS]
    return out


def _line(text, requires=(), forbids=(), any_groups=()):
    return dict(Text=text, Requires=list(requires), Forbids=list(forbids), AnyGroups=[list(g) for g in any_groups])


def _others(rel):
    return sorted({f["b"] if f["a"] == rel else f["a"] for f in frictions.FRICTIONS if rel in (f["a"], f["b"])})


def _stance_lines(prefix, name_of_other):
    """Guest List status lines for one seat (a woman, or the canon pair)."""
    lines = [
        _line("{n}At the table.{/n}", requires=[prefix + ".stance.joined"], forbids=[prefix + ".joined_late"]),
        _line("{n}At the table. She came to it late, and on her own terms.{/n}",
              requires=[prefix + ".stance.joined", prefix + ".joined_late"]),
        _line("{n}{g|RRT_AtTheTableApart}At the table, apart.{/g}{/n}", requires=[prefix + ".stance.tolerated"]),
        _line("{n}Not yet at the table.{/n}", forbids=[prefix + ".stance.joined", prefix + ".stance.tolerated"]),
    ]
    for other, name in name_of_other:
        lines.append(_line("{n}She will not speak to %s.{/n}" % name, requires=[prefix + ".enmity." + other]))
    return lines


def guest_entries():
    out = []
    for rel, (portrait, name) in PARTNERS.items():
        others = [(o, PARTNERS[o][1]) for o in _others(rel)]
        forbids = ["tirabade.harem.eligible"] if rel in ("anevia", "irabeth") else []
        if rel in PAIR_WOMEN:
            lines = []
            for woman in PAIR_WOMEN[rel]:
                seat = "%s.harem.stance.%s" % (rel, woman)
                label = woman.capitalize()
                lines += [_line("{n}%s: at the table.{/n}" % label, requires=[seat + ".joined"]),
                          _line("{n}%s: {g|RRT_AtTheTableApart}at the table, apart{/g}.{/n}" % label, requires=[seat + ".tolerated"]),
                          _line("{n}%s: not yet at the table.{/n}" % label, forbids=[seat + ".joined", seat + ".tolerated"])]
            for other, oname in others:
                for woman in PAIR_WOMEN[rel]:
                    lines.append(_line("{n}%s will not speak to %s.{/n}" % (woman.capitalize(), oname),
                                       requires=["%s.harem.enmity.%s.%s" % (rel, woman, other)]))
        else:
            lines = _stance_lines(rel + ".harem", others)
        out.append(dict(Id="guest." + rel, Section="Guest List", Portrait=portrait, Title=name,
                        Text="{n}%s. A chair at the {g|RRT_Table}Table{/g}, if she wants it.{/n}" % name,
                        Lines=lines, Requires=[eligible(rel)], Forbids=forbids, AnyGroups=[], Tooltip="RRT_GuestList"))
    return out


def seating_entries():
    out = []
    for f in frictions.FRICTIONS:
        a, b = f["a"], f["b"]
        key = "household.friction.%s.%s" % (a, b)
        fails = f["fails"]
        lines = [_line("{n}Settled. They share the table.{/n}", requires=[key + ".settled"]),
                 _line("{n}Failed. One of them sits apart now.{/n}", requires=[key + ".failed"])]
        if f["kind"] == "atrocity":
            lines.append(_line("{n}No word of mine will make this true. It needs something done.{/n}"))
        out.append(dict(Id="seating.%s.%s" % (a, b), Section="Seating Notes", Portrait=PARTNERS[a][0],
                        Title="%s and %s" % (PARTNERS[a][1], PARTNERS[b][1]),
                        Text="{n}" + f["note"] + "{/n}", Lines=lines, Requires=[eligible(a), eligible(b)],
                        Forbids=[], AnyGroups=[], Tooltip="RRT_SeatingNotes"))
    # The Trickster's own tool, with the uses left (the engine's runtime counter).
    words = ("{n}Three words left in me.{/n}", "{n}Two words left in me.{/n}", "{n}One word left in me.{/n}",
             "{n}No words left. From here on I settle things the long way.{/n}")
    out.append(dict(Id="seating.word_made_true", Section="Seating Notes", Portrait="",
                    Title="The Word, made true",
                    Text=("{n}Three times, and no more, I can say a feud is over and have the world agree. Each time "
                          "leaves a {g|RRT_Debt}debt{/g}, and the women who keep to the truth will know it was said.{/n}"),
                    Lines=[_line(words[0], requires=["trickster.wmt.left.3"]), _line(words[1], requires=["trickster.wmt.left.2"]),
                           _line(words[2], requires=["trickster.wmt.left.1"]), _line(words[3], requires=["trickster.wmt.left.0"])],
                    Requires=["trickster", KEPT], Forbids=[], AnyGroups=[], Tooltip="RRT_WordMadeTrueUses"))
    return out


def secret_entries():
    return [dict(Id="secret." + s["key"], Section="Secrets", Portrait=s["portrait"], Title=s["title"],
                 Text="{n}" + s["text"] + " {g|RRT_SecretRisk}Risk: " + s["risk"] + ".{/g}{/n}",
                 Lines=[_line("{n}Unknown to %s.{/n}" % PARTNERS.get(w, (None, w))[1],
                              forbids=["trickster.secret.%s.known.%s" % (s["key"], w)]) for w in s["witnesses"]],
                 Requires=["trickster.secret." + s["key"]], Forbids=[], AnyGroups=[], Tooltip="RRT_Secret")
            for s in SECRETS]


def integrate(payload):
    payload["Relationships"][REL] = relationship()
    for key, groups in derived(payload).items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != groups:
            raise ValueError("Conflicting household derived key: " + key)
        payload["Derived"][key] = groups
    if not trickster_world._bound(payload, KING_GONE):
        kind, guid, _ = trickster_world.BINDINGS[KING_GONE]
        payload.setdefault(kind, {})[KING_GONE] = [guid] if kind in trickster_world.LIST_KINDS else guid
    frictions.validate(set(PARTNERS))
    payload.setdefault("Openers", []).extend(copy.deepcopy(OPENERS))
    payload["Scenes"].extend(copy.deepcopy(SCENES + ENTRIES + INVITATIONS))
    payload.setdefault("Glossary", {}).update({k: dict(v) for k, v in GLOSSARY.items()})
    ledger = payload.setdefault("Books", {}).get("trickster.ledger")
    if ledger is None:
        raise ValueError("The household sections need the Ledger book (lastcall.integrate runs first)")
    ledger["Entries"].extend(guest_entries() + seating_entries() + secret_entries())

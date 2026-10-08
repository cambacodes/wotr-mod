"""Nurah Dendiwhar: cloud voice-owner pass (villain-route-nurah, design-first).

Applied last, after every route, harem row, Last Call partner, engine appender and the earlier cloud layers
(expansion._make_expansion), so the paragraphs it appends never shift an index another pass registers
(tools/payoff_contracts.json registers epilogue paragraphs by index; every paragraph here is appended after the
existing ones). Text and flag-gated paragraphs only: no scene, node or choice id, choice text, choice position, Next,
Set, gate, check, cost or GuidFor changes. Review and truth table: tools/route_packs/redesign/nurah/cloud-review.md,
truth-table.json.

Structure fixed here (read-only consumers of flags the route already sets; producer and receipt text made true for
every history that reaches it):
  * the Commander's answer to "Why keep me?" (nurah.trickster.temper_good / _chaos, set by eleven choices across the
    cell scene and the post) had no reader anywhere, and temper_evil was read only as a gate; the epilogue pages now
    read all three, and "you'd sell them all again, and I'd like to watch" is paid off with a sale;
  * Irabeth's reaction to the night walk set nurah.trickster.cost.irabeth_lied_to / cost.seen with no reader; her
    lie and her silence now come back in the book;
  * the Tymon second printing (nurah.trickster.cost.second_edition, 400 crusade gold) had no reader;
  * nurah.a_margin_for_you/morning said "Vhal's book is finished, and so is Vhal" on every history, including the
    ones where Vhal keeps her trade (outcome_collection, _limited, _distance); the five outcome flags of
    the_copies_that_survive had no reader at all;
  * nurah.trickster.epilogue.the_margin told parent-romance players that "the author's terms she had set" held,
    though only the Trickster cell ever stages author's terms;
  * nurah.trickster.react.irabeth_manuscript had Irabeth say the traitor had "our casualty lists" on the ghost-written
    branch, where Nurah never walked out to the archive (that is the pardon branch's night walk);
  * nurah.lastcall.page read nurah.trickster.cost.name_above backwards (the Commander asked for a name ABOVE hers and
    was refused; the page said hers went above the Commander's);
  * claude-work-queue nurah:D06-D11: the parent continuation narrated rooms, stairs and burglaries away from the only
    place the scenes are delivered (Nurah's arrival at the Commander's private door in Drezen). The interview, the
    rehearsal, the case, the reading and the settlement now come to the Commander's chambers and receiving room; no
    travel is narrated that the encounter does not deliver.

Prose that failed CHARACTER-TRUTH 2/12 (villainy as paperwork, treason kept off screen) is rewritten where it fails:
the night walk now ends at the Bottleneck Gate casualty list, ticked by the woman who pointed the demons at them
(05bdab7a); the household audit with Arsinoe is no longer a freight-charge quarrel but Nurah diverting the east
ward's poppy away from the men who caught her; the editor gets a pencil point between his knuckles. Lines that work
are left alone (the cell refusals, "Then I'm stock", the Pulura betrayal, the larva's "first draft").

Canon used (writer knowledge/characters/nurah/native-lines.json): 05bdab7a (pointing out the unit at Bottleneck
Gate), a3972f3e ("Get it together, you maggots"), 0803fd90 (revenge creed), 30c3565a ("You're all so stupid"),
bd7cf740 ("from the very beginning"), 57b14fa6 (gutting the stargazers), f1249f68 ("we could have used their gear"),
d54c2487 (Lann: no regret). No new lore: no new place, title, deity or mechanic; Deskari's cults, the Queen's court
and Tymon/Nerosyan/Mendev are already used by the route.
"""
from story_format import p

R = "nurah.trickster."
GOOD, CHAOS, EVIL = R + "temper_good", R + "temper_chaos", R + "temper_evil"
IRABETH_ALIVE = ("irabeth.present_now", "crossroute.irabeth.available")

# (scene, node) -> [(old substring, new substring)], each old substring must occur exactly once
SUB = {}
# (scene, node) -> (substring the reviewed text contains, new text)
TEXT = {}
# (scene, node, requires, forbids) -> (substring the reviewed paragraph contains, new text)
PARA = {}
# (scene, node) -> paragraphs appended after every existing paragraph
ADD = {}


def sub(scene, node, old, new):
    SUB.setdefault((scene, node), []).append((old, new))


def text(scene, node, expect, body):
    TEXT[(scene, node)] = (expect, body.strip())


def para(scene, node, requires, forbids, expect, body):
    PARA[(scene, node, tuple(requires), tuple(forbids))] = (expect, body.strip())


def add(scene, node, *paras):
    ADD.setdefault((scene, node), []).extend(paras)


# ---------------------------------------------------------------------------------------------------------------------
# Trickster, the cell. The night walk was a woman reading casualty lists for the spelling. It is now the traitor of
# Bottleneck Gate reading the names of the men she pointed the demons at (05bdab7a "There they are, there they are!"),
# and enjoying it (0803fd90). Irabeth's watch report ("laughing at the spelling") already describes this night.
# ---------------------------------------------------------------------------------------------------------------------
NIGHT_OLD = ('''"So I went for a walk. The door opens for a pardoned woman, it turns out, and nobody in Drezen looks at a halfling after dark. I read your casualty lists in the archive and came back before the guard changed, because I wanted to ask you one thing to your face.''')
NIGHT_NEW = ('''"So I went for a walk. The door opens for a pardoned woman, it turns out, and nobody in Drezen looks at a halfling after dark. I read your casualty lists in the archive."
{n}She draws a strip of paper out of her sleeve: a column of names copied in her small stitched hand, with a neat tick beside some of them.{/n} "Bottleneck Gate. The men under the wall when I leaned over it and shouted 'there they are, there they are!' The demons went where I pointed. I ticked the ones I watched go down screaming. Your clerks had misspelled four of them, so I corrected those. Somebody ought to spell them properly, and it was never going to be you lot."
{n}She folds the strip and tucks it in beside the pardon, as pleased with herself as a cook putting away a good recipe.{/n} "Then I came back before the guard changed, because I wanted to ask you one thing to your face.''')
for sid in (R + "prison.night_out", R + "prison.night_out_late"):
    sub(sid, "start", NIGHT_OLD, NIGHT_NEW)

# The ghost-written branch never walks her to the archive: Irabeth cannot say she has the casualty lists.
text(R + "react.irabeth_manuscript", "start", "A traitor has our casualty lists and your handwriting", '''
"The prisoner left with a dedication in a very familiar hand. I hope you know what she will do with it." {n}Irabeth closes the gaol report.{/n} "A traitor walked out of my gaol with a book about this army under her arm and your handwriting on its first page. She pointed demons at my soldiers from the wall at Bottleneck Gate, Commander. I need more than a joke for the watch."''')

# ---------------------------------------------------------------------------------------------------------------------
# Trickster epilogues: the answers to "Why keep me?", Irabeth's lie or silence, the Tymon printing. Appended after
# every existing paragraph on each page that a living, published Nurah can reach.
# ---------------------------------------------------------------------------------------------------------------------
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
sub(R + "epilogue.the_margin", "start",
    "The author's terms she had set held to the last page: her name on the cover, and nobody's above it.",
    "Her terms held to the last page: her name on the cover, and nobody's above it.")
add(R + "epilogue.the_margin", "start", p(
    '''{n}Istrene Vhal got a chapter of her own near the end, short and unforgiving. Nurah read it aloud at a Nerosyan salon where half of Vhal's old subscribers were guests, and watched each of them work out which of the anonymous fools was him.{/n}''',
    requires=("nurah.copies_settled",)))

# Last Call: cost.name_above is the Commander's demand for a name above hers, refused (terms/refused). The page had
# it backwards. (Unreachable on a shipped save: that refusal also closes the route; corrected so it cannot mislead.)
para("nurah.lastcall.page", "page", ("nurah.trickster.cost.name_above",), (),
     "Her name went on the cover above the Commander's",
     '''{n}The Commander had once asked for a name above hers on the cover, and had been told no. The book says so in a footnote, in the smallest type she owned.{/n}''')

# ---------------------------------------------------------------------------------------------------------------------
# Parent continuation (claude-work-queue nurah:D06-D11). Every visit is delivered at Nurah's arrival at the
# Commander's private door in Drezen (nurah.arrival). The other people now come up her stair; nothing narrates a walk
# to a wine merchant's back room that the encounter never stages.
# ---------------------------------------------------------------------------------------------------------------------
P = "nurah."
sub(P + "a_page_with_teeth", "start",
    "Nurah has a visitor waiting with her: a broad-shouldered human woman with ink ground into the creases of her hands. A covered bundle rests against her boot. When you arrive, the woman straightens without bowing.",
    "Nurah comes up the back stair with a visitor on her heels, and shuts your door on both of them before the wine-clerks below can count heads: a broad-shouldered human woman with ink ground into the creases of her hands. She sets a covered bundle against her boot and straightens without bowing.")

sub(P + "the_borrowed_audience", "start",
    "For the rehearsal she has borrowed a small room near the tavern. She leads you there from the appointment, shuts the door, and sets two chairs on opposite sides of a narrow table. A third stands against the wall with a coat hanging over it.",
    "For the rehearsal she takes over your chambers. She bolts the door, sweeps your dispatches off the writing table onto the floor, sets two chairs on opposite sides of it, and hangs a coat over a third against the wall.")

sub(P + "the_editor_opens", "start",
    "Carrow has hired the back room of a wine merchant for the interview. Nurah meets you at the agreed appointment and takes you there by a side street. She has pinned her hair differently.",
    "Carrow wanted the back room of a wine merchant for the interview. Nurah wrote back that editors climb stairs for Commanders and not the other way about, so Carrow has climbed yours, up the kitchen-yard stair she uses herself, with his case in his arms. She has pinned her hair differently.")
sub(P + "the_editor_opens", "start", "The editor rises when you enter.", "The editor rises when you come in from the inner room.")

# Nurah leads the interview: the cruelty is on the table, not in the margin.
sub(P + "the_editor_opens", "her_question",
    "She folds the older proof along its existing crease.{/n}",
    "She folds the older proof along its existing crease. Then she sets the point of her pencil on the back of his hand, between two knuckles, and leans on it until he stops talking.{/n}")

S = P + "the_case_goes_missing"
sub(S, "start",
    '''She leads you to the room she has borrowed and puts the parcel on the bed. The lock clicks when she turns it over.
"He has rooms above the wine merchant. He has also acquired the habit of taking supper where people can see how much business he has. There is a stair at the back. We have time to decide what happens at the top."''',
    '''She puts the parcel on your bed. The lock clicks when she turns it over.
"He has rooms above the wine merchant. He has also acquired the habit of taking supper where people can see how much business he has, and of leaving the case upstairs, because a man who carries a case to supper looks like a man with something in it. I can have it out of his room and up your stair inside a quarter of an hour. What happens to it on your table is the part I want to decide with you."''')
sub(S, "copy_plan",
    '''"Keep it. If we have to leave through the window, you may complain about my handwriting on the way down."''',
    '''"Keep it. If I have to leave through his window, you may complain about my handwriting when I climb back up yours."''')
text(S, "access", "At dusk you take the back stair above the wine merchant.", '''
{n}At dusk the fourth step squeals. Nurah comes in breathing hard, with Carrow's case hugged against her chest like a stolen cat, and kicks your door shut behind her.
"He left it on his desk," she says. "Either he trusts the door, or he is becoming more interesting. Supper, then pudding, then brandy. We have until the brandy."
She sets the case on your table under the lamp and gives you the little knife. Its handle is warm from her sleeve.{/n}''')
sub(S, "informed",
    "Nurah works the door with a narrow strip of metal while you watch the stair. The lock yields on her third attempt.\nInside, the brass clasp faces the room. She stops your hand before you lift it.",
    "Nurah works the clasp with a narrow strip of metal while you watch the door. It yields on her third attempt.\nShe stops your hand before you lift the lid.")
text(S, "unaided", "Nurah opens the door with a narrow strip of metal and stands aside.", '''
{n}Nurah stands at your door with her ear to the wood while you bend over the case. It looks ordinary from across the room. Up close, one hinge sits higher than the other and the lining seems too thick for the depth of the lid.
You cannot tell which irregularity matters without handling it. Down in the kitchen yard somebody is arguing about a missing spoon.
"If he comes up your stair after me," she whispers, "it will be about the spoon. Nobody in Drezen notices a halfling. Everybody notices a spoon."{/n}''')
sub(S, "marked_entry",
    "Footsteps cross the passage outside. Nurah catches your wrist, pulls you down behind the desk, and waits until they pass. Her grip remains hard for several seconds afterward.",
    "Footsteps come up the stair outside. Nurah throws your cloak over the case, sits on it, and catches your wrist until they pass on to the clerks' door. Her grip remains hard for several seconds afterward.")
sub(S, "copied",
    "Outside, the stair seems louder under your feet than it did on the way up. Nurah waits until you have reached the street before she takes your arm. Her hand remains cold through your sleeve.",
    "Nurah carries the case back down your stair before the brandy, and comes up again a quarter of an hour later with nothing in her hands. They are cold when she puts them on your arm. She does not say whether Carrow had finished his pudding.")
text(S, "taken", "Nurah wraps the originals in the blank sheets she prepared.", '''
{n}Nurah wraps the originals in the blank sheets she prepared. When she reaches the threatening letter, she stops, reads the quoted praise once more, and folds it with the rest.
The case looks absurdly empty. Prospectuses and wine accounts slide into the space where the hidden papers had been.{/n}
"He will miss them," {n}she says.{/n}
"That was the plan."
"Yes. I am reminding myself that I like it."
{n}She leaves the parcel with you, because nobody searches a Commander's chest. The empty case she carries back down your stair to Carrow's desk, and comes back up with its little brass key in her palm. You raise an eyebrow.{/n}
"For his next case," {n}she says.{/n} "He should learn to change his habits."
{n}She checks the parcel once, touching it through the cloth, then takes the chair on the far side of the room before you can ask what part of the letter has made her so quiet.{/n}''')

sub(P + "the_price_of_a_warning", "start",
    '''"The evening is still going ahead. Our host has changed the arrangement."''',
    '''"The evening is still going ahead, and it is coming to you. Her subscribers paid to be seen with the Commander, so she has asked to hold the reading in your receiving room. I said yes for you. Our host has changed the arrangement."''')

sub(P + "the_subscribers_evening", "start",
    "You leave together after she has checked the passage. At the hired room, the wine is already being poured.",
    "Downstairs, in your own receiving room, Vhal's people have already moved your table, hung somebody else's lamps and started pouring somebody else's wine.")

sub(P + "the_unpurchased_sentence", "settle",
    "You accompany Nurah to Vhal's hired rooms. The collector has packed her books but left the traveling chest open. Edran stands beside it with a list.",
    "Vhal comes to the settlement, because Nurah will not go to her. Two porters carry the traveling chest up to your receiving room and set it down open, and Edran stands beside it with a list.")

# The chaos settlement and the evil collection: the people the paper hurts are on the page, and she likes it.
sub(P + "the_unpurchased_sentence", "chaos",
    '''"Some names will become public. Some should have been public years ago. I cannot promise every beneficiary will be charming."''',
    '''"Some names will become public. A few of the people under them will lose a post, or a marriage, or a hand, depending on the family. I find I can bear it."''')
sub(P + "the_copies_that_survive", "collection",
    "One former client tried to purchase his own file before Edran finished packing it.",
    "One former client tried to purchase his own file before Edran finished packing it. When he came up your stair this morning to plead, I let him get halfway through, then read him the first paragraph of his grandmother's confession, slowly, until he cried. He paid the higher price.")

# a_margin_for_you/morning: Vhal is not finished on every history. The five outcomes of the copies now have a reader.
S = P + "a_margin_for_you"
sub(S, "morning",
    "Vhal's book is finished, and so is Vhal.",
    "Vhal's book is finished, and whatever is left of Vhal is somebody else's problem.")
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
text(H + "audit", "start", "A teamster waits at the tavern door", '''
{n}A teamster waits at the tavern door, his whip tucked under one arm. Arsinoe has spread a demand for the crusade's stores across the Table: forty jars of poppy syrup and a bale of clean linen, to come off the infirmary's allotment and go south before dawn. Nurah is holding its corner down with her empty cup.{/n}
"The temple is being asked to honor this before the wagons leave. It bears a convincing seal. It also bears Nurah's hand."
"Convincing? I was hoping for impeccable," {n}Nurah says.{/n}
{n}Arsinoe moves the cup and sets the loading tally beside the demand.{/n} "That syrup belongs to the east ward. I want the charge proved before anyone opens the stores."
"The east ward." {n}Nurah smiles past her at the teamster, who is plainly hers.{/n} "Eleven men in that ward were under the wall at Bottleneck Gate when I pointed the demons at them, and lived, and spat on me when they tied my hands after the siege. Let them find out what a night without poppy sounds like. I'll sell the syrup in the lower city and drink to their health."
"And I want my name on my work," {n}she adds.{/n} "Not yours, Commander. Not some fat fool who thinks holding the purse makes him the author."''')
text(H + "retry", "start", "The loading tally has returned.", '''
{n}The loading tally has returned. Arsinoe puts it beside the disputed bill; Nurah swings her feet beneath the bench, watching the priestess rather than the paper.{/n}
"One wagon. Two freight charges. And forty jars of the east ward's poppy. Now there is time to compare them."
"I wondered how long you would take," {n}Nurah says.{/n} "They've had two nights to practise screaming. I'd hate for it to go to waste."
"Long enough to prove it. Take the pen. This correction needs its author's name," {n}Arsinoe says.{/n}
{n}Nurah catches the pen between two fingers.{/n} "Only the correction to this bill. You can find another woman to write a confession of wickedness."''')
for sid in (H + "audit", H + "retry"):
    sub(sid, "audit_held",
        '''"That demand will not reach the stores. The hand is yours, Nurah. The sum does not follow."''',
        '''"That demand will not reach the stores, and the syrup stays on the ward. The hand is yours, Nurah. The sum does not follow."''')
    sub(sid, "audit_held",
        '''"Good. Put yours beside it. I want to know who caught me," {n}Nurah says.{/n}''',
        '''"Good. Put yours beside it. I want to know who caught me," {n}Nurah says.{/n} "Let them sleep, then. I'll think of something else to keep them awake."''')
    sub(sid, "refused",
        "Outside, the teamster shouts for a decision about the crusade's stores. Arsinoe takes the unsigned bill back to her counter.",
        "Outside, the teamster shouts for a decision about the crusade's stores. Arsinoe takes the unsigned bill back to her counter, and the stores stay locked while it is disputed. The east ward gets no syrup tonight either. Nurah laughs all the way to the door.")
sub(H + "audit", "word_held",
    '''"Then we understand each other." {n}Nurah signs.''',
    '''"Harmless. How dull. They'll sleep like babies." {n}Nurah signs.''')
sub(H + "audit", "missed",
    '''"This stays with me. Drezen has lost enough stores to clever people."''',
    '''"This stays with me. Drezen has lost enough stores to clever people."
{n}The teamster leaves with an empty cart. Nurah watches him go with the face of a woman who has already chosen the night she will try again.{/n}''')


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


def integrate(payload):
    scenes = _scenes(payload)
    rows_absent = H + "audit" not in scenes and ROW_SENTINEL not in scenes

    def wanted(table):
        return [(k, v) for k, v in table.items() if not (rows_absent and k[0].startswith(H))]
    for (sid, nid), pairs in wanted(SUB):
        node = _node(scenes, sid, nid)
        for old, new in pairs:
            if node["Text"].count(old) != 1:
                raise ValueError("nurah cloud: %s/%s drifted from the reviewed text (%r)" % (sid, nid, old[:60]))
            node["Text"] = node["Text"].replace(old, new)
    for (sid, nid), (expect, body) in wanted(TEXT):
        node = _node(scenes, sid, nid)
        if expect not in node["Text"]:
            raise ValueError("nurah cloud: %s/%s drifted from the reviewed text" % (sid, nid))
        node["Text"] = body
    for (sid, nid, requires, forbids), (expect, body) in wanted(PARA):
        node = _node(scenes, sid, nid)
        hits = [x for x in node.get("Paragraphs", []) if tuple(x.get("Requires", [])) == requires
                and tuple(x.get("Forbids", [])) == forbids and expect in x["Text"]]
        if len(hits) != 1:
            raise ValueError("nurah cloud: %s/%s paragraph %r matched %d" % (sid, nid, expect, len(hits)))
        hits[0]["Text"] = body
    for (sid, nid), paras in wanted(ADD):
        node = _node(scenes, sid, nid)
        node["Paragraphs"] = node.get("Paragraphs", []) + [dict(x) for x in paras]
    touched = {k[0] for table in (SUB, TEXT, PARA, ADD) for k, _ in wanted(table)}
    for sid in touched:
        for node in scenes[sid]["Nodes"]:
            texts = [node["Text"]] + [c["Text"] for c in node["Choices"]] + [x["Text"] for x in node.get("Paragraphs", [])]
            if any("[PROSE PENDING" in t for t in texts):
                raise ValueError("nurah cloud: prose still pending at %s/%s" % (sid, node["Id"]))

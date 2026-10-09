"""Areelu Vorlesh: cloud voice-owner pass (villain-route-areelu, design-first).

Applied last, after every route, harem row, Last Call partner and engine appender (expansion._make_expansion), so the
paragraphs it appends never shift an index another pass registers. Text and flag-gated paragraphs only: no scene, node
or choice id, choice position, Next, Set, gate, check, cost or GuidFor changes. Review and truth table:
tools/route_packs/redesign/areelu/cloud-review.md, truth-table.json.

Structure fixed here (read-only consumers of flags the route already sets, and producer text that states what its
flags mean):
  * areelu.trickster.cost.late was set by the Chapter 5 lens primer without the lens ever stating the late terms that
    the Threshold and epilogue readers quote back ("you agreed to worse terms"); the lens now states them where the
    flag is set, and the cell's frost branch repeats them;
  * the Iomedae pair (household.pair.iomedae_areelu: three experiment files opened, or a forged apology) had no
    reader anywhere in her route; Threshold's gate and her Last Call page now read it;
  * finale.unnamed told a "Your life. Nothing less." player that no stake had been named; the paragraph is now true
    for every history and term.life has its own reader;
  * her Last Call page spoke in her first person and then switched to a clerk's third person for the household
    paragraphs; those are hers again;
  * stale or branch-false references: stake_only's "locked cellar ... cart of her notes" (never staged), the
    dagger's "The fire took my records" and the prison's "burnt workrooms" on the punchline history where the
    laboratories did not burn (finale.survived).

Prose that failed CHARACTER-TRUTH 2/12 (menace by summary or receipt) is rewritten: the lens now shows her hand at
work on a living subject; the pair scenes give her lines from the table, not the index; the closure and afterlogue
lines are hers, unrepentant, not a settlement clerk's.

Canon used (writer knowledge/characters/areelu-vorlesh/native-lines.json): 670f8e52, f644c7d2, 18901eb6, 4cf21739,
dbfa68f2, 4cf65db7, e44c123f, 753fd1bf, 02a4264d, 4f99b73b. Yaniel's years on Areelu's tables are the route's own
established fact (yaniel.trickster.beat.areelu). No new lore: no child's name, no race, no new place.
"""
from story_format import p

STRUCK_SEEN = "areelu.trickster.wager.struck"
IOM = "household.pair.iomedae_areelu."
RECORDS = IOM + "cost.areelu_records_opened"
FORGERY = IOM + "cost.commander_false_apology"
LIFE = "areelu.trickster.term.life"

# (scene, node) -> (substring the reviewed text contains, new text)
TEXT = {}
# (scene, node, requires, forbids) -> (substring the reviewed paragraph contains, new text)
PARA = {}
# (scene, node) -> paragraphs appended after every existing paragraph
ADD = {}


def text(scene, node, expect, body):
    TEXT[(scene, node)] = (expect, body.strip())


def para(scene, node, requires, forbids, expect, body):
    PARA[(scene, node, tuple(requires), tuple(forbids))] = (expect, body.strip())


def add(scene, node, *paras):
    ADD.setdefault((scene, node), []).extend(paras)


# ---------------------------------------------------------------------------------------------------------------------
# Chapter 5: the lens. Her surveillance stays; the hand on the other side is now seen at work (Yaniel: "I watched her
# sew demons together and graft their limbs onto crusaders"), and the lens states the late terms it sets.
# ---------------------------------------------------------------------------------------------------------------------
S = "areelu.trickster.rivalry.lens"
text(S, "start", "A lens of dark glass has appeared", '''
{n}A lens of dark glass has appeared among your campaign maps. Its silver ring is cold. Nobody admits to leaving it there.{/n}
{n}When you hold it to your eye you do not see the tent around you. You see a table under a hard white lamp, and a man strapped to it at the wrists, the ankles and the throat. His crusader's tabard has been cut off him and folded, neatly, on a stool. A woman's hand opens his forearm along the bone, pins the skin back, and lays a grey strip of demon sinew into the opening. The sinew moves on its own. The man screams into the leather between his teeth. The hand does not hurry.{/n}
{n}Then it wipes itself on a cloth, picks up a pen, and goes on writing in the margin of a page that is already full of you: your hours, your rations, which of your companions you laugh with and which you only answer. The hand is steady. The man is still screaming.{/n}''')

text(S, "terms", "And you make the offer through my own lens", '''
"Neither. And you make the offer through my own lens." {n}The glass stays clear for several breaths. Behind it the hand finds the strapped man's throat, counts something, and seems satisfied.{/n} "You send your wager by glass, instead of bringing it to my face. That is how debtors send their excuses, and I price it the way I price theirs. Late wagers carry late terms, Commander. If I burn at Threshold, you keep nothing of mine. Not a page. Not my name."
"Bring it to Threshold on those terms, or do not bring it. Keep the glass until then. I would like to watch what you do with the time you have left."''')

S = "areelu.trickster.lens.watched"
text(S, "look", "Through the glass you see your own tent from above", '''
{n}Through the glass you see a bench under a lamp, and on the bench a cage, and in the cage a dretch with its jaw wired open. A woman's hand feeds it, one drop at a time from a glass pipette, something that glows violet. The dretch swells. It tries to scream around the wire. The hand writes down the count, and the next drop is already waiting.{/n}
{n}The hand pauses. Frost creeps across the lens from the other side, and letters form in it.{/n}
"You offered me a wager at Iz. I am told gamblers like to watch their opponents' faces. Here is my work instead. Try not to waste it."''')

S = "areelu.trickster.wager.struck"
text(S, "frost", "You made the offer through my lens", '''
"Neither. You made the offer through my glass, late, and you took my terms with it: if I burn, you keep nothing of mine." {n}Her outline steadies in the crystal's light.{/n} "Now say what you will put behind it. I do not accept jokes as collateral."''')

# ---------------------------------------------------------------------------------------------------------------------
# Chapter 6: the gate reads the Iomedae pair (three files opened for a goddess, or an apology forged in her name).
# ---------------------------------------------------------------------------------------------------------------------
# The two Iomedae-pair readers for threshold.welcome/start were removed 2026-10-08: every node of that scene has
# authored answers, so gated paragraphs there crash the native audience (managed NativeAudienceTests). They wait in
# claude-work-queue.json for a structural host (a no-answer beat before the answers).


# ---------------------------------------------------------------------------------------------------------------------
# Epilogue closures: her voice, not a settlement clerk's; true for every history that reaches them.
# ---------------------------------------------------------------------------------------------------------------------
S = "areelu.trickster.finale.unnamed"
para(S, "end", (), ("areelu.trickster.stake_named",), "Neither party had named her work", '''
{n}Nobody had named her work as a substitute for her life. When the final choice came, her life was the only stake left on the table, and it was collected.{/n}''')
para(S, "end", ("areelu.trickster.stake_named",), ("areelu.trickster.graft_drawn",), "Her graft had not been collected", '''
{n}Her work had been named as the stake, and nobody collected it. The graft was still sewn into her when the final choice came, and it went where she went.{/n}''')
para(S, "end", ("areelu.trickster.graft_drawn",), (), "chosen a fate that the stored essence", '''
{n}The Commander had drawn the Abyss out of her into the Council's crystal, and she had screamed for it at the end of the draining. Then the Commander chose an ending the crystal could not buy her out of. The scream bought nothing.{/n}''')
para(S, "end", ("areelu.dead_fight",), ("areelu.sacrifice_trickster", "areelu.incinerated", "areelu.sacrifice_wound",
     "areelu.sacrifice_before"), "She fell in the fight", '''
{n}She fell in the fight, before the wager could be settled, which she had always said was the likeliest result.{/n}''')
para(S, "end", ("ending.wound_closed",), (), "it closed. No stored essence", '''
{n}She went into the Wound to close it, and it closed on her. Nothing of hers had been bottled to go in her place.{/n}''')
para(S, "end", (), ("ending.wound_closed",), "did not come back. No stored essence", '''
{n}She went into the Wound and did not come back. Nothing of hers had been bottled to go in her place.{/n}''')
add(S, "end", p('''{n}At the rift the Commander had asked for her life and nothing less. The terms were met to the letter. She had always preferred terms met to the letter.{/n}''',
                requires=(LIFE,)))

ALIVE_UNRAISED = '''
{n}She lived, with her notes and her power, since no fire had claimed either. The Commander had asked for the stake and nothing more, and she gave nothing more. She packed her case that night and left without saying where.{/n}'''
COMMANDER_BURNED = '''
{n}The Commander went into the Wound. Areelu watched it close from the rim, and then took what the original wager owed her: the Commander's wound, recorded to the last measure on what the fire left. Her own papers were never part of the payment. If the Commander came back, the measurements were delivered and she was not. If not, she worked on without an answer from the dead, and did not pretend to miss one.{/n}'''
for S in ("areelu.trickster.finale.stake_only", "areelu.trickster.finale.report_stands"):
    para(S, "end", (), ("areelu.died_at_finale", "areelu.trickster.commander_burned"), "She lived. Neither her life",
         ALIVE_UNRAISED)
    para(S, "end", ("areelu.trickster.commander_burned",), ("areelu.died_at_finale",), "She recorded the personal wound",
         COMMANDER_BURNED)
para("areelu.trickster.finale.stake_only", "end", (), ("areelu.died_at_finale",), "The locked cellar held no cart", '''
{n}Nothing of hers stayed behind with the Commander: not a page, not a vial, not a forwarding address. A wager for the stake alone had bought none of them.{/n}''')

text("areelu.trickster.finale.lien_bottled", "stands", "with an invoice for the binding", '''
{n}The report on the wound was long and precise and entirely about the wound. She sent a copy to the Commander's door, bound in a pale, fine-grained leather that the Commander did not recognise and did not ask about.{/n}''')

# ---------------------------------------------------------------------------------------------------------------------
# Report pages: two lines that were false on the punchline history (the laboratories did not burn there).
# ---------------------------------------------------------------------------------------------------------------------
text("areelu.trickster.report.dagger", "why", "The fire took my records", '''
"Because I made it, and I want it in my hands again." {n}She looks toward the Commander's boot.{/n} "Some things never went into any notebook: how hard his blood fought the drawing, the hour it stopped fighting. The crystal remembers both. I would like to read them again. Give it here."''')

text("areelu.trickster.report.prison", "start", "Past the burnt workrooms", '''
{n}In the autumn of the sixth year she went back to Threshold, with a wagon, six stonecutters and a writ over the Commander's seal.{/n}
{n}Past the gutted workrooms, to the surviving cells: the cells where Sarkoris had kept its mages, where she had been kept, and from which she had slipped away at night to the demiplane where she first decided to open the Wound. The crusade's quartermaster had them marked for rubble, for the new road. One cell wall held the first working of the Wound, scratched there with a nail, and it was the only copy she had left. The Commander went with her, because the quartermaster would not have let the stonecutters through otherwise.{/n}''')

# ---------------------------------------------------------------------------------------------------------------------
# Last Call: her page is first person; the household lines were a clerk's third person. The Iomedae pair is read.
# ---------------------------------------------------------------------------------------------------------------------
S = "areelu.lastcall.page"
para(S, "page", ("household.pair.yaniel_areelu.cost.areelu_specific_guise",), (), "traded away the use of Yaniel's name", '''
{n}I gave up one face at my laboratory projection: Yaniel's, the name and the likeness. It opened a great many doors in Drezen, and men told it things they would not have told their priests. She may have it back. I keep what I learned wearing it, and I have other faces.{/n}''')
para(S, "page", ("household.pair.nidalynn_areelu.accounted", "household.pair.nidalynn_areelu.no_absolution",
                 "household.pair.nidalynn_areelu.cost.areelu_field_notes_lost", "crossroute.nidalynn.available"), (),
     "surrendered the Windstep field route", '''
{n}I burned a field route through Windstep to keep the Commander walking toward Threshold. Whoever is left out there is harder to find now. Nidalynn inspected the ashes and did not forgive me. She was not asked to.{/n}''')
para(S, "page", ("household.pair.nidalynn_areelu.unanswered",), (), "The Windstep complaint had gone unanswered", '''
{n}The Windstep complaint went unanswered. The pasture is still ash. I did not expect otherwise, and I did not lose sleep over it.{/n}''')
para(S, "page", ("household.pair.nidalynn_areelu.notice.carried", "crossroute.nidalynn.available"),
     ("household.pair.nidalynn_areelu.accounted", "household.pair.nidalynn_areelu.unanswered"),
     "still lacked an inspected answer", '''
{n}Nidalynn's cloth with the mare on it was carried to my cell and carried away again, and nobody has shown her what became of the trail. I could tell her. Nobody has asked me.{/n}''')
add(S, "page",
    p('''{n}I opened three files for the Commander's goddess: a miller, a drover, a mason. She has their names now. I have the rest of the annex, which she did not think to ask for. The goddess who was mortal not so long ago should learn to phrase her demands more carefully.{/n}''',
      requires=(RECORDS,)),
    p('''{n}The Commander once wrote an apology in my name and read it to Iomedae. It is the only forgery of me I have ever found offensive. It was badly argued.{/n}''',
      requires=(FORGERY,), forbids=(RECORDS,)))

# ---------------------------------------------------------------------------------------------------------------------
# Household pairs she shares with non-villain women (Iomedae, Yaniel, Nidalynn): her lines from the table, not the
# index. Their agendas, choices and flags are untouched; J03 pair rows carry no paragraphs, so text only.
# ---------------------------------------------------------------------------------------------------------------------
S = "household.pair.iomedae_areelu.reconstruction"
text(S, "originals.work", "K-22. That mark means extraction", '''
{n}You return to the salvage chest with the quartermaster. Between two warped boards you find the detached intake leaves. Their seals match the bundle; each carries a name, a code and a relative's identifying mark. Back at your desk, you compare the leaves with the index and turn the lens toward the damaged columns.
Frost gathers on its rim. Areelu's corrections appear beside your transcriptions.{/n}
"K-22. That mark means extraction, not release. He was awake for it; the method required that. Do not send his family looking for a man who died on my table."
{n}She rebuilds the three damaged code correspondences, one stroke at a time, and adds a column nobody asked for: the hour at which each man stopped asking for his family. The dispatch candles burn down untouched.{/n}''')
text(S, "families.match", "The brand is sufficient", '''
{n}You read each relative's name and identifying account into the dark glass. Areelu copies them. The witnesses who trusted you can no longer remain anonymous in this inquiry.{/n}
"The brand is sufficient. The disappearance date is not; that column records admission, not capture. The drover sat in a cage for nine days before I had a table free for him."
{n}She restores the damaged cross-references and supplies the matching case observations.{/n}
"Your witnesses are useful. They have corrected an intake error. That does not entitle them to the rest of my work."
{n}You retain a copy of the three cases. She retains hers.{/n}''')

S = "household.pair.yaniel_areelu.inspection"
text(S, "start", "Beside the crystal, a working index lies open", '''
{n}The projection turns toward the folded paper. Beside the crystal lie the pages of the guise, taken down from life while Yaniel lay on her tables: the voice, the stance, the scar, the way she carries her sword hand.{/n} "She survived the Fane and now sends me a likeness. Does she think I have forgotten it? I studied that face for years before I wore it. Unfold it. I can see from here."''')
text(S, "comparison", "That is the face I wore", '''
"Yes. That is the face I wore. It opened doors that would have closed against mine, and men wept to see it and told it everything." {n}The projection indicates a line in the pages without touching it.{/n} "Her name. Her appearance. Useful among crusaders. Less useful now that she walks your walls and can contradict me."
{n}A cult lookout could still be deceived by that face. The comparison lies within your reach.{/n}''')
text(S, "undertaking", "Strike out that entry", '''
"Strike out that entry. Name and likeness, both. I will retire the guise; I have worn better. My notes remain mine. So do my other faces." {n}She watches the pen in your hand.{/n} "And you will not put her name to a lie made from my work. I have enough enemies producing those without your assistance."
{n}Yaniel's original lies beside the pages. The exclusion is still waiting for your pen.{/n}''')
text(S, "retained", "Leave it on the bench", '''
"Leave it on the bench. I may want to wear her again when my work here resumes, and a fresh likeness saves a great deal of guessing." {n}The original is still in your hand. Yaniel lent it for inspection; leaving it would give the witch a fresh likeness to keep.{/n}''')

S = "household.pair.nidalynn_areelu.cell"
text(S, "start", "I followed the displacement east", '''
{n}A field bundle lies beside the cell's apparatus, under a cover marked with a mare. Areelu's projection watches you unfold Nidalynn's cloth; its hands remain smoke and light.{/n}
"Windstep. Yes. I followed the herding families east after the first year. People with animals move slowly, and slow things can be counted. I wanted subjects who had lived beside the rift and not yet been changed by it, and I took them from that trail. Those leaves would still lead a hunter to whoever is left. Or your scouts."
{n}Her gaze passes over the stitched stars.{/n}
"She wants the pasture back. I cannot give her that, and I would not if I could. These leaves are another matter. Take them, and stop calling them an apology. There is no second working copy here."
"I want you at Threshold. I will discard a field route to keep you moving toward it. I will not discard my purpose."''')

# ---------------------------------------------------------------------------------------------------------------------
# Afterlogue (native Cue_0004/Cue_0005 replacements): she reports to Pharasma, unrepentant (37ef9f4c, e8e08c11), and
# Pharasma's native verdict follows unchanged.
# ---------------------------------------------------------------------------------------------------------------------
AFTER = {
    "areelu.trickster.afterlogue.spared": ("The victor spared my life", '''
"The victor spared my life, and I spent what was left of it at the Commander's side, by my own choice and on my own terms. I did not stop working. Your clerks will have found some of my vessels by now. Not all. My child's soul is still unresolved, and I have not withdrawn my claim."'''),
    "areelu.trickster.afterlogue.mortal": ("collected my graft instead of my life", '''
"The Commander collected my graft instead of my life and left me mortal. I went on with my hands, since I no longer had the Abyss. I chose the Commander's company. I did not choose to stop. My child was not returned to me, and I have not forgiven you for it."'''),
    "areelu.trickster.afterlogue.spared_wager": ("The Commander spared my life", '''
"The Commander spared my life. Neither of us burned in the rift. I kept my notes, my power and the purpose for which I opened the Wound, and I left before anyone could mistake a wager for a reconciliation."'''),
    "areelu.trickster.afterlogue.mortal_wager": ("The rift took the essence", '''
"The rift took the essence the Commander had bottled out of me, and left the woman. The wager bought that experiment. It did not buy what remained of me, and what remained of me went back to work."'''),
    "areelu.trickster.afterlogue.return_witch": ("with the Abyss still in me", '''
"The Commander went into the Wound and came back out of it. I stayed alive, with the Abyss still in me. Nothing that followed settled my child's fate, so I went on, as I always have."'''),
    "areelu.trickster.afterlogue.return_mortal": ("My graft had already been collected", '''
"The Commander went into the Wound and came back out of it. My graft had already been collected; I lived without magic and worked with what my hands still knew. My child's fate remained open. I kept it open."'''),
}
for _sid, (_expect, _body) in AFTER.items():
    text(_sid, "line", _expect, _body)


def _scenes(payload):
    return {s["Id"]: s for s in payload["Scenes"]}


def _node(scenes, sid, nid):
    if sid not in scenes:
        raise KeyError("areelu cloud: scene %s not found" % sid)
    hits = [n for n in scenes[sid]["Nodes"] if n["Id"] == nid]
    if len(hits) != 1:
        raise KeyError("areelu cloud: %s/%s matched %d nodes" % (sid, nid, len(hits)))
    return hits[0]


def integrate(payload):
    scenes = _scenes(payload)
    for (sid, nid), (expect, body) in TEXT.items():
        node = _node(scenes, sid, nid)
        if expect not in node["Text"]:
            raise ValueError("areelu cloud: %s/%s drifted from the reviewed text" % (sid, nid))
        node["Text"] = body
    for (sid, nid, requires, forbids), (expect, body) in PARA.items():
        node = _node(scenes, sid, nid)
        hits = [x for x in node.get("Paragraphs", []) if tuple(x.get("Requires", [])) == requires
                and tuple(x.get("Forbids", [])) == forbids and expect in x["Text"]]
        if len(hits) != 1:
            raise ValueError("areelu cloud: %s/%s paragraph %r matched %d" % (sid, nid, expect, len(hits)))
        hits[0]["Text"] = body
    for (sid, nid), paras in ADD.items():
        node = _node(scenes, sid, nid)
        node["Paragraphs"] = node.get("Paragraphs", []) + [dict(x) for x in paras]
    touched = {k[0] for k in TEXT} | {k[0] for k in PARA} | {k[0] for k in ADD}
    for sid in touched:
        for node in scenes[sid]["Nodes"]:
            texts = [node["Text"]] + [c["Text"] for c in node["Choices"]] + [x["Text"] for x in node.get("Paragraphs", [])]
            if any("[PROSE PENDING" in t for t in texts):
                raise ValueError("areelu cloud: prose still pending at %s/%s" % (sid, node["Id"]))

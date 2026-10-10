"""Horzalah: cloud voice-owner pass (villain-route-horzalah, design-first).

Applied last, after every route, harem row, Last Call partner and engine appender (expansion._make_expansion, after
areelu_cloud), so the paragraphs it appends never shift an index another pass registers. Text and flag-gated
paragraphs only: no scene, node or choice id, choice position, Next, Set, gate, check, cost or GuidFor changes.
Review and machine truth table: tools/route_packs/redesign/horzalah/cloud-review.md, truth-table.json.

Structure fixed here (read-only consumers of flags the route or the household already sets, and producer text that
states what its flags mean):
  * the sisters' household pair and docket (household.pair/docket.horzalah_hepzamirah: a warning given away or sold,
    a courier crippled, the trap instructions burned) had readers only on Hepzamirah's side; Horzalah's partner
    pages now read every outcome;
  * beat.threshold's "And if I don't?" promise (she goes to the Worldwound herself) had no reader; the mourned page
    now keeps it; the knife lesson's cut hand (knife_nicked) gets its partner-page reader;
  * epilogue.unanswered withheld its own outcome ("The answer ... came after the war"); she now acts on her own
    terms, the terms the Commander granted in guild.kept ("come and go as I please");
  * branch-false text: letter.invoice had Horzalah's dresser sending his respects although on that branch the
    Commander owns him; mourned P7 put her "through a shut door" on histories that end at the crossroads or on the
    bedroom floor; late.at_night/dismissed quoted the traitor branch's answer on the loyal branch too (it now
    answers her own native farewell, C12);
  * wrong medium and menace by note: late.at_night/no_priest (a note on the pillow), beat.ear (a note to the surgeon,
    "No, I did not hurt him", a note to the barracks) are now her hand, on screen; the Ledger's "report from the
    Guild" (she never sends reports; she comes in person) is the Commander's own account;
  * paperwork in place of menace: letter.invoice and epilogue.ally were a bill and a closed account; the deserter
    arrives hamstrung at the door, and her knives' work is seen;
  * voice: beat.spit's sincere "Thank you" (she never thanks: writer voice.md never_thanks); beat.name's doubled
    "father's priests"; beat.sister's back_departed/back_unavailable said the same warning twice; beat.thousands'
    solstice card (a canary every winter now); her pointed native profanity restored in beat.sister and beat.yozz.

Canon used (writer knowledge/characters/horzalah/native-lines.json): 0ad1af67, 798bf2b5, 34037594, 4de7b0dc,
fc2827ae, 2f36ecf9, ad1ea05a, aaa2721e; handoff C12 (Cue_0007 farewell, Cue_4 "even the guild"). No new lore.
"""
from authoring.generation_errors import OverlayMismatch, overlay_item, overlay_node, record
import copy

from story_format import p

H = "horzalah.trickster."
PAIR = "household.pair.horzalah_hepzamirah."
DOCKET = "household.docket.horzalah_hepzamirah."

# (scene, node) -> (substring the reviewed text contains, new text)
TEXT = {}
# (scene, node, requires, forbids) -> (substring the reviewed paragraph contains, new text)
PARA = {}
# (scene, node) -> paragraphs appended after every existing paragraph
ADD = {}
# (book, entry id) -> (substring the reviewed entry text contains, new text, {old line substring: new line text})
BOOK = {}


def text(scene, node, expect, body):
    TEXT[(scene, node)] = (expect, body.strip())


def para(scene, node, requires, forbids, expect, body):
    PARA[(scene, node, tuple(requires), tuple(forbids))] = (expect, body.strip())


def add(scene, node, *paras):
    ADD.setdefault((scene, node), []).extend(paras)


# ---------------------------------------------------------------------------------------------------------------------
# Chapter 5, the late road: the threat is made in person, not pinned to a pillow.
# ---------------------------------------------------------------------------------------------------------------------
text(H + "late.at_night", "no_priest", "there is a note on your pillow", '''
{n}The priest goes away offended. That night you wake to the soft thud of a knife going into your pillow, a finger's width from your good ear, so thin you did not hear it come. She is sitting on the end of your bed in the dark, where every sentry on the stair will swear that nobody passed.{/n}
"My people among your sentries tell me you sent the priest away. Good." {n}She leans over you and turns the knife in the linen, once, so that the edge whispers against your cheek.{/n} "The day they tell me otherwise, I will know you made a fool of me, and so will every knife that ever bows to that box. It is mine now, mortal. Remember whose." {n}The air folds, and the end of the bed is lighter. The knife stays where she left it.{/n}''')

# Both mercy lists latch horzalah.dismissed.latched; only the traitor answer is attested as "Get out of my sight".
# Her own native farewell (Cue_0007, handoff C12) holds on both.
text(H + "late.at_night", "dismissed", "'Get out of my sight,' you said.", '''
{n}She does not use the window. You wake because the air in the room has folded, the way it folded around her when she left you last, and when it unfolds she is standing at the foot of your bed with a knife in her hand and a night without sleep in her face.{/n}
"I told you my father's favour was not worth dealing with you again." {n}Her voice is hoarse, as if she had been shouting for days, or not using it at all.{/n} "I lied. You sent me off that crossroads with my life, as if it were yours to send, and I went. It did not help."
"Father has said nothing. Not a word, not a whisper, not a cultist at the door. And since last night three of my own masters have followed me from room to room in my own hall, smiling. They heard about the crossroads before I was home. They are waiting to see who says the word 'failure' first, and they are beginning to think it will not need to be Father."''')

# ---------------------------------------------------------------------------------------------------------------------
# Her presence in Drezen: what she does to people who handle what is hers.
# ---------------------------------------------------------------------------------------------------------------------
text(H + "beat.ear", "start", "I sent him a note.", '''
"I will stare at whatever I like. It is mine." {n}She reaches up without asking and pushes your hair back from the scar with two fingers, and studies it the way a jeweller studies a setting.{/n}
"It is healing better now. The edge was ragged at first; your surgeon has no idea what he is doing, and he had started to trim it. So I went to see him." {n}She lets your hair fall back.{/n} "He still has both his hands. I made him lay the left one flat on his own table, and I put my knife down between his fingers, one gap after another, while I told him whose ear it was. He will not touch it again. He will not tell you why, either. Ask him, if you want to watch a grown man sweat."''')
text(H + "beat.ear", "room", "I have had a note sent to the barracks.", '''
"Your guards tell it in the barracks, the night a demon came through the wall and took a piece of the Knight Commander home with her. They argue about which ear. Half of them say the right." {n}She sounds offended on your behalf.{/n} "I went down to the barracks last night and settled it. The loudest of them has a notch in his own left ear now, to help him remember. They all say the left now."''')

text(H + "beat.spit", "backed2", "Thank you. I will not say that again", '''
"You shamed him for me. In front of his friends." {n}She studies the wet knuckle.{/n} "He will hate you for it now, and me twice as much, and one day he will try again, better armed." {n}She shrugs.{/n} "I know that face. I wore it for a hundred years, looking at my sister. It is a good face. It gets things done."
"Do not wait for thanks. You took my answer out of my hands and left him his tongue. Next time I answer first, and you may shame whatever is left of him."''')

text(H + "beat.name", "start", "and by one of my father's own priests", '''
"I always look like that. Today I mean it." {n}She jerks her chin at the street, where a sergeant is marching a file of recruits past the Storyteller's shelves as quickly as their legs will carry them.{/n}
"That one pointed at me this morning and told his boys to keep their distance from *Hepzamirah*. Loudly. So that I would hear." {n}Her fingers drum on her folded arm.{/n} "I have been called Hepzamirah by Yozz's guests, by my father's priests, and once by a nalfeshnee in a bathhouse, who did not live to do it twice. I did not expect it from a mortal with his helmet on backwards."''')

text(H + "beat.sister", "back_departed", "If she comes looking for you again, what is between her and me stays ours", '''
"You brought her back from Colyphyr, and now she has crawled off out of your city." {n}Her teeth show.{/n} "I know it was you. I do not ask how. I will say this once, mortal. What is between her and me is ours. If she comes looking for you again, you will not make us sit at one table and smile, and you will not try to settle it. If she ever comes near my box, I will kill her again myself, and this time I will do it properly."''')
text(H + "beat.sister", "back_unavailable", "If she comes looking for you again, what is between her and me stays ours", '''
"You brought her back from Colyphyr." {n}Her teeth show.{/n} "I know it was you. I do not ask how. Wherever she is keeping herself now, I will say this once, mortal. What is between her and me is ours. You will not make us sit at one table and smile. You will not try to settle it. If she ever comes near my box, I will kill her again myself, and this time I will do it properly."''')

text(H + "beat.thousands", "others", "I still send her a card at the winter solstice.", '''
"Some. There are three or four of my brothers in the Abyss who send me assassins every few years, out of habit, and I send some back. There is a sister in Absalom who pretends to be a mortal and sells perfume. I sent her a canary too, once, and she sent me back a bottle of something that took the skin off my hands." {n}Her mouth curves.{/n} "I liked her for that. I send her another canary every winter. She has not opened one yet. She will, one year, when she is tired, and I hope I hear it from here."''')

# Register: her native profanity is pointed and aimed at the people she despises (aaa2721e "That bitch Hepzamirah",
# "That piece of trash"; 2f36ecf9 "that overdressed fool"); the route had almost none of it.
text(H + "beat.sister", "start", "he never looked at her that long in her life.", '''
"Must I?" {n}She sighs, theatrically, and then she tells you anyway, because it is clear she has been waiting for someone to ask.{/n}
"She was older. She was dumber. She was weaker; everyone knew it. And she hated me from the day I was spawned, because Father looked at me, once, for about as long as it takes to count to three, and he never looked at her that long in her life. The bitch never forgave me those three heartbeats."''')
text(H + "beat.yozz", "start", "Must we discuss him in your street?", '''
"Yozz?" {n}Her lip curls.{/n} "Must we discuss that overdressed piece of trash in your street? His Guild is mine. His household is mine. I have not forgotten what he paid for. What do you want to know?"''')

# ---------------------------------------------------------------------------------------------------------------------
# The ally branch: a bill was standing in for her trade, and the dresser was on the wrong side of the chain.
# ---------------------------------------------------------------------------------------------------------------------
text(H + "letter.invoice", "start", "The dresser sends his respects", '''
{n}It comes by an ordinary courier, a tiefling in the Guild's grey, who waits at your door with his hand out until you have paid. That is how you know what it is before you open it. He has not come up the stair alone. Two of the Guild's porters drop a man on your threshold: a crusader's tabard, a gag, wrists bound behind him, and both heels cut through behind the ankle, cleanly, the way a butcher hamstrings a calf. He weeps into your floor while you read.{/n}
"To the Knight Commander of the Fifth Crusade, from the Assassins' Guild of Alushinyrra.
For services rendered this month, as retained: three doors in Drezen watched, and the cultist who tried the third one buried under your chapel floor; one message carried into the Abyss and one answer carried out; one deserter returned to the crusade, alive, as specified. The specification said nothing about his feet. He will not run from you again.
At the Guild's rates, which are high. Payment on receipt.
Make my dresser earn his keep, now that he is yours. The coat you wore to your last war council was a disgrace. H., master."''')

text(H + "epilogue.ally", "page", "her bills were always paid on time", '''
{n}Horzalah's knives served the crusade to the end of the war, at the Guild's rates and not a day longer. A Mendevian lord who had been selling the army's grain to the cultists was found in his own granary, with as much of it as would fit poured down his throat. A cell of Deskari's faithful in Drezen's lower town woke one morning three heads short. Her people were always where the Commander needed them, and the Commander always paid.{/n}
{n}The Commander kept Yozz's dresser, who worked well and never looked up. Horzalah never asked after the slave. When the war was over she came for her last payment in person, counted it out on the Commander's table coin by coin, and left without touching the Commander's hand. She never spoke to the Commander again. She had been bought once. She knew exactly what happened to things that were bought.{/n}''')

# ---------------------------------------------------------------------------------------------------------------------
# epilogue.unanswered: the wants were heard (guild.kept/wants) and granted; the gift test never came. She decides.
# ---------------------------------------------------------------------------------------------------------------------
text(H + "epilogue.unanswered", "page", "The answer, and what Horzalah did with it, came after the war.", '''
{n}The war ended before Horzalah had finished deciding what the Commander was. She came to Drezen the spring after the Threshold, through no door at all, with a grey-haired man on a thin gold chain a step behind her: Yozz's dresser, a suitor's gift in the idiom of the Abyss.{/n}
{n}She held out the end of the chain across the table, and snatched it back before a hand could close on it, hard enough to bring the old dresser down on both knees on the flagstones. "Too slow," she said. "In my hall the slow ones are the ones we sell." She watched the Commander's face, not the old man bleeding on the flagstones, and whatever she was looking for there, she found, or decided she did not need. She took the dresser home.{/n}
{n}She kept what she had asked for and what she had been granted: she came and went in Drezen as she pleased, on no night anyone could have named in advance, and stood where she liked, and the sentries stepped off the path for her and never knew why. She came to look at what was hers, and left before the bell. She never brought a second gift, and she never called what she took by any name. In her father's realm the ribboned box hung over the Guild's board; neither there nor in the old Alushinyrra hall was a contract on the Commander ever accepted.{/n}''')

# ---------------------------------------------------------------------------------------------------------------------
# The mourned page: branch-true closers, and the Threshold promise kept.
# ---------------------------------------------------------------------------------------------------------------------
para(H + "epilogue.mourned", "page", (), (H + "primed",), "through a shut door", '''
{n}The crusaders had last seen her bleeding at the Commander's mercy, alive because the Commander allowed it, which she never forgave. They knew nothing of her fortunes after she left, or what the death cost her.{/n}''')
para(H + "epilogue.mourned", "page", (H + "primed",), (H + "returned",), "No report of its reception had returned.", '''
{n}She had taken her trophy home before the death. Whether her masters ever bowed to it, nobody in Drezen learned.{/n}''')
add(H + "epilogue.mourned", "page",
    p('''{n}She had told the Commander to come back with everything else attached. When nothing came back, she went to the Worldwound herself with three of her knives, and walked the edge of the rift for a month, killing whatever crawled out of it and turning the dead over with her boot. She brought nothing home. The knives who went with her never spoke of it; the one who joked about it at table stopped speaking of anything.{/n}''',
      requires=(H + "beat.threshold_heard",)))

# ---------------------------------------------------------------------------------------------------------------------
# Partner pages: the sisters' household outcomes and the knife lesson, read on her side too.
# ---------------------------------------------------------------------------------------------------------------------
PARTNER_READERS = (
    p('''{n}Once, for twenty lances, she had given a warning away instead of selling it, and her sister had let the courier walk past her door with his tongue in his head. Horzalah never gave anything away again. The master who asked her at table whether the Guild now worked for nothing carried the next warning through Hepzamirah's street himself, and came back without his tongue.{/n}''',
      requires=(PAIR + "horzalah_terms_kept", PAIR + "hepzamirah_terms_kept")),
    p('''{n}She had sold the patrol's warning out from under her sister's truce, and counted the souls she was paid in before she counted the lances that did not come back out of the third ravine. She never pretended to regret it. The cambion's purse sat on her shelf beside the ribboned box for years, still heavy.{/n}''',
      requires=(PAIR + "horzalah_term_broken",)),
    p('''{n}Her sister had crippled her courier behind the north gate. Horzalah had his knees set, badly, and kept him on the stair of her Alushinyrra hall, crooked-legged, so that he was the first thing anyone saw who came to speak to her of Hepzamirah.{/n}''',
      requires=(PAIR + "hepzamirah_term_broken",)),
    p('''{n}When the Commander would not carry her terms, she sold the patrol's warning to the best buyer in Alushinyrra, exactly as she had said she would. Afterwards, whenever the third ravine was mentioned in her hearing, she said the Commander's name, and not kindly.{/n}''',
      requires=(PAIR + "permanent_refusal",), forbids=(PAIR + "resolved",)),
    p('''{n}She never told anyone what she had read in her sister's trap instructions before she burned them. But no door in her hall was ever locked the way the Ivory Labyrinth's had been, and the locksmith who once offered to fit her one was found in his own strongroom, behind his own lock, which nobody had thought to open for a week.{/n}''',
      requires=(DOCKET + "instructions.destroyed",)),
    p('''{n}On the back of the Commander's hand, from the knuckle almost to the wrist, ran the thin white line she had left there in a lesson. She liked to trace it with one fingertip when she thought nobody was watching, and said, when she was caught, that she was only checking her work.{/n}''',
      requires=(H + "beat.knife_nicked",)),
)
add(H + "epilogue.together", "page", *PARTNER_READERS)
add(H + "epilogue.commit", "page", *PARTNER_READERS)

# ---------------------------------------------------------------------------------------------------------------------
# The Ledger (the Commander's own book): she never sends reports; she comes and shows.
# ---------------------------------------------------------------------------------------------------------------------
BOOK[("trickster.ledger", "owed.horzalah")] = (
    "Her report from the Guild records whether she completed it.",
    "{n}Horzalah cut off my left ear and boxed it in a white ribbon. No priest touches the wound: her Guild must go on "
    "believing she took it from me. That was the price of her story, and her people in Drezen watch that I keep paying it.{/n}",
    {"Her report from the Guild placed the trophy":
         "{n}She came back to show me what it bought: the box hangs over the Guild's board in her father's house, and her "
         "masters bowed to it.{/n}",
     "No report has come from the Guild":
         "{n}The ear is paid. She has not come back to say whether her masters bowed to it, and I do not know where she "
         "keeps it.{/n}"})


def _scenes(payload):
    return {s["Id"]: s for s in payload["Scenes"]}


def _node(scenes, sid, nid):
    return overlay_node(scenes, sid, nid)


def integrate(payload):
    scenes = _scenes(payload)
    for (sid, nid), (expect, body) in TEXT.items():
        with overlay_item():
            node = _node(scenes, sid, nid)
            if expect not in node["Text"]:
                raise OverlayMismatch('overlay.text_mismatch', scene=sid, node=nid, detail=str(expect)[:70])
            node["Text"] = body
    for (sid, nid, requires, forbids), (expect, body) in PARA.items():
        with overlay_item():
            node = _node(scenes, sid, nid)
            hits = [x for x in node.get("Paragraphs", []) if tuple(x.get("Requires", [])) == requires
                    and tuple(x.get("Forbids", [])) == forbids and expect in x["Text"]]
            if len(hits) != 1:
                raise OverlayMismatch('overlay.text_mismatch', scene=sid, node=nid, detail=str(expect)[:70])
            hits[0]["Text"] = body
    for (sid, nid), paras in ADD.items():
        with overlay_item():
            node = _node(scenes, sid, nid)
            node["Paragraphs"] = node.get("Paragraphs", []) + [copy.deepcopy(x) for x in paras]
    for (book, eid), (expect, body, lines) in BOOK.items():
        with overlay_item():
            hits = [e for e in payload["Books"][book]["Entries"] if e["Id"] == eid]
            if len(hits) != 1 or expect not in hits[0]["Text"]:
                raise OverlayMismatch('overlay.text_mismatch', detail=str(expect)[:70])
            hits[0]["Text"] = body
            for old, new in lines.items():
                with overlay_item():
                    matched = [line for line in hits[0]["Lines"] if old in line["Text"]]
                    if len(matched) != 1:
                        raise OverlayMismatch('overlay.text_mismatch', detail=str(old)[:70])
                    matched[0]["Text"] = new
    touched = {k[0] for k in TEXT} | {k[0] for k in PARA} | {k[0] for k in ADD}
    for sid in touched:
        if sid not in scenes:
            record("overlay.scene_resolution", scene=sid)
            continue
        for node in scenes[sid]["Nodes"]:
            with overlay_item():
                texts = [node["Text"]] + [c["Text"] for c in node["Choices"]] + [x["Text"] for x in node.get("Paragraphs", [])]
                if any("[PROSE PENDING" in t for t in texts):
                    raise OverlayMismatch('overlay.text_mismatch', scene=sid, node=node.get("Id"), detail="horzalah cloud: prose still pending at %s/%s" % (sid, node["Id"]))

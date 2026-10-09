"""Heat layer G4 (Claude prose, 2026-10-09): build-up to the explicit boundary.

HEAT (Directive 12): the build-up of every READY explicit slot for Minagho, Chivarro,
Jerribeth, Wenduag, Gesmerha, Hepzamirah and Shamira must reach the START of the act in
her own voice, so the cut lands where the explicit slot (filled later) begins. Ember and
Aivu are friendship-only and are never touched here.

Text only. It runs last, after every appender and every earlier voice layer, so it edits
the finished text of each build-up node and cannot be overwritten by an earlier layer.
Ids, Next, Set, Requires/Forbids, checks, answer order and the slot nodes are untouched;
slot default text still comes from the briefs (tools/route_packs/explicit_slots).
Every rule asserts the exact text it replaces and raises on drift, as the cloud layers do.
"""
import re

# (scene ids or None for any, node id regex, old fragment, new fragment)
RULES = []


def rule(scenes, node, old, new):
    RULES.append((tuple(scenes) if scenes else None, re.compile(node + r"\Z"), old, new))


# (scene id, node id, flag in the paragraph's Requires, old fragment, new fragment)
PRULES = []


def prule(scene, node, flag, old, new):
    PRULES.append((scene, node, flag, old, new))


def _scenes(payload):
    return {s["Id"]: s for s in payload["Scenes"]}


def integrate(payload):
    scenes = _scenes(payload)
    for scene_ids, node_re, old, new in RULES:
        matched = 0
        for sid in (scene_ids or scenes):
            if sid not in scenes:
                raise KeyError("heat g4: scene %s not found" % sid)
            for node in scenes[sid]["Nodes"]:
                if not node_re.match(node["Id"]):
                    continue
                if scene_ids is None and old not in node["Text"]:
                    continue
                if node["Text"].count(old) != 1:
                    raise ValueError("heat g4: %s/%s drifted from the reviewed text (%r)" % (sid, node["Id"], old[:48]))
                node["Text"] = node["Text"].replace(old, new, 1)
                matched += 1
        if not matched:
            raise ValueError("heat g4: no node matched %r in %r" % (node_re.pattern, scene_ids))
    for sid, nid, flag, old, new in PRULES:
        hits = [x for n in scenes[sid]["Nodes"] if n["Id"] == nid for x in n.get("Paragraphs", [])
                if flag in x.get("Requires", []) and x["Text"].count(old) == 1]
        if len(hits) != 1:
            raise ValueError("heat g4: %s/%s paragraph %r matched %d" % (sid, nid, old[:48], len(hits)))
        hits[0]["Text"] = hits[0]["Text"].replace(old, new, 1)
    for sid, scene in scenes.items():
        for node in scene["Nodes"]:
            if "[PROSE PENDING" in node["Text"] and sid in _TOUCHED:
                raise ValueError("heat g4: prose still pending at %s/%s" % (sid, node["Id"]))


_TOUCHED = set()

# ======================================================================================
# MINAGHO / CHIVARRO
# ======================================================================================
MC = "minagho_chivarro.trickster."

# --- Minagho's secret night (stance 0-3): every scene that carries it -----------------
rule(None, r"stance_\d_night_minagho",
     '''{n}Minagho comes after the watch changes. She kicks the door shut, tears your shirt open and presses you against it. Her mouth catches yours; her fingers work the buckle at your waist.{/n}
"Quiet, Golarian. I want her to wonder where I spent the night."
{n}She draws you toward the bed by your open collar.{/n}''',
     '''{n}Minagho comes after the watch changes. She kicks the door shut, tears your shirt open and slams you against it. Her mouth catches yours and her teeth find your lip and stay there until she tastes blood. The buckle at your waist sticks; she rips the strap through instead.{/n}
"Quiet, Golarian. I want her to wonder where I spent the night."
{n}She hauls you to the bed by your open collar and throws you down. Her dress comes off over her head in one pull and the rest of you follows it onto the floor, her claws raking red lines down your ribs. She climbs over you, bare knees either side of your hips, already slick where she settles against your thigh, and grinds down once, slowly, so that you feel exactly how much she wants this.{/n}
"Look what you do to me. Disgusting. Hands."
{n}She drags your hand between her legs and pins it there, breathing hard through her teeth, and bends until her mouth is at your ear.{/n}
"I do not ask twice."''')

# --- Chivarro's secret night (stance 0-3) ---------------------------------------------
rule(None, r"stance_\d_night_chivarro",
     '''{n}She laughs, opens her gown and catches your hands at her bare waist. You pull her close. She draws you back toward the bed, leaving the closed account on the shelf.{/n}''',
     '''{n}She laughs, opens her gown and catches your hands at her bare waist. You pull her close. She lets the gown fall and lets you look for as long as you like, because she likes it more than you do, then walks you back to the bed, pushes you down and climbs over you, bare thighs either side of your hips and loose hair across your chest. The closed account stays on the shelf. Her fingers find the fastening at your waist and take their time with it.{/n}
"I know what you want, honey. I sold the idea of it to better men. Say it, and I may let you have it."
{n}She drags your hand up the inside of her thigh to the heat she has been keeping from you, and holds it there.{/n}
"Quietly. She hears everything."''')

# --- Chivarro's service night (stance 7) ----------------------------------------------
rule(None, r"stance_7_night_chivarro",
     '''{n}She pushes you onto the mattress and follows.{/n}''',
     '''{n}She pushes you onto the mattress and follows, strips you with brisk, practised fingers and settles over you, knees either side of your hips. Her mouth moves down your throat to your chest. One of her hands slides between her own thighs, and she smiles against your skin when you notice, and takes your hand from her waist to put it where hers has been.{/n}
"There. Warm. Do not make a speech about it."''')

# --- Minagho alone: threshold (Minagho, spared Minagho) --------------------------------
rule([MC + "alone.minagho", MC + "alone.minagho_spared"], "threshold",
     '''{n}She pushes you onto the mattress and follows, hair spilling across your cheek as she catches your mouth again.{/n}''',
     '''{n}She pushes you onto the mattress and follows, hair spilling across your cheek. The dress is gone; you did not see where. She kneels over you, bare, and pins your wrists above your head with one hand while the other drags down your stomach to your waistband and under it, and her mouth curls at what she finds there.{/n}
"Already. Good. Mine tonight, Golarian, and I intend to use every minute of it."
{n}She settles her weight against you, hot and wet and rocking, and catches your mouth again.{/n}''')

# --- Minagho by letter: came ----------------------------------------------------------
rule([MC + "alone.minagho_letter"], "came",
     '''and climbs astride you with your wrists pinned in one of her hands.{/n}''',
     '''and climbs astride you with your wrists pinned in one of her hands.{/n}
{n}Her free hand drags your belt open. Her dress is round her waist, then it is not on her at all, and she grinds down against you, slick through the last of the cloth, her breath hissing between her teeth.{/n}
"Paid, Golarian. Now I collect."''')

# --- Minagho when it scars: night ------------------------------------------------------
rule([MC + "alone.minagho_when_it_scars"], "night",
     '''"Mine," {n}she says.{/n} "On top of his."''',
     '''"Mine," {n}she says.{/n} "On top of his."
{n}She tears your shirt up over your head and strips her dress off with the other hand, and her bare thighs clamp your hips. Slowly she lets your wrist go and puts your hand low on her hip, and grinds against you once, hard, until her breath catches on a sound she will deny later.{/n}
"Hands on me. I will not say it twice."''')

# --- The pair, when it scars: night ----------------------------------------------------
rule([MC + "after.when_it_scars"], "night",
     '''{n}They come down onto the bed on either side of you, and then Minagho is astride you and Chivarro's mouth is on yours, and the lamp goes out under somebody's elbow.{/n}''',
     '''{n}They come down onto the bed on either side of you. Chivarro's gown hangs open to the waist and she lets you see all of it. Minagho tears hers off over her head and flings it at the lamp, and then she is astride you, bare and hot against your stomach, and Chivarro's mouth is on yours, tasting of wine, one hand pressed flat to your chest.{/n}
"Share, Minagho," {n}Chivarro murmurs against your lips.{/n} "There are two hands, and I mean to have one."
"Then let it be this one," {n}Minagho says. She takes your wrist and puts it between her thighs, and Chivarro's hand slides down your body to meet it.{/n}
{n}The lamp goes out under somebody's elbow.{/n}''')

# --- The pair before the last road: threshold ------------------------------------------
rule([MC + "after.before_the_last_road"], "threshold",
     '''{n}Chivarro draws both of you toward her bed.{/n}''',
     '''{n}Chivarro draws both of you toward her bed, undoing the last of her gown as she goes. Minagho drags your shirt over your head and bites the muscle of your shoulder; Chivarro strips the belt out of your breeches and drops it on the floor. Then there are two mouths and four hands on you, and the lamp stands crooked on the shelf, throwing their shadows huge across the ceiling.{/n}
"Mine first," {n}Minagho says, and swings a leg across you, bare and hot against your hip.{/n}
"Nothing of yours is first, darling," {n}Chivarro says, pulling Minagho's head back by the hair to kiss her over your chest.{/n} "You simply arrive early."''')

rule([MC + "after.before_the_last_road_letter"], "came",
     '''"I did not bring you here to watch me count." {n}She takes your hand and draws you down with them.{/n}''',
     '''"I did not bring you here to watch me count." {n}She takes your hand and draws you down with them. Chivarro's gown is open before you reach the mattress; Minagho tears yours down the front and kisses along the seam as it parts. Between them you are stripped, pinned and handled with equal impatience, two sets of hands finding every place that matters and neither willing to wait for the other.{/n}
"Mine first," {n}Minagho says, and throws a leg over you, bare against your hip.{/n}
"Nothing of yours is first, darling," {n}Chivarro says, and draws Minagho's head back by the hair to kiss her.{/n} "You simply arrive early."''')

# --- Chivarro alone: threshold / threshold_clean ---------------------------------------
rule([MC + "alone.chivarro"], r"threshold(_clean)?",
     '''and there, holding you exactly where she wants you, she stops talking.{/n}''',
     '''and there, holding you exactly where she wants you, she stops talking.{/n}
{n}Her mouth comes down on yours, slow and thorough, her hair falling round your face. One hand takes yours and guides it up her thigh to the heat she has kept from every guest; the other works your laces loose without looking. She lifts her head an inch to let you hear her breathe.{/n}
"I have faked every sound a body can make, honey. Be careful. Let me find out which ones I do not need to."''')

rule([MC + "alone.chivarro_letter"], "came",
     '''"This evening is mine, honey. I am tired of hearing about everyone else's."''',
     '''"This evening is mine, honey. I am tired of hearing about everyone else's."
{n}She pushes you onto the mattress and unlaces you herself, brisk as a woman closing a shop, then stands over you in the lamplight with the gown at her feet and lets you look. When she kneels over you her skin is warm and her hair brushes your chest, and her fingers are already between your hips and hers, guiding.{/n}
"Now, honey. Not a word about the rent."''')

rule([MC + "alone.chivarro_when_it_scars"], "night",
     '''She pushes you back onto her bed and follows.{/n}''',
     '''She pushes you back onto her bed and follows.{/n}
{n}Over you she is all warm skin and a collector's patience. She strips your shirt away, unfastens you with two fingers, and her mouth finds the hollow of your throat, your chest, the line of your stomach, in no hurry at all. When she lifts her head her lips are wet, and her mouth is daring you to complain.{/n}
"Interest, honey. Compounding by the hour."''')

# --- minachiv base route ---------------------------------------------------------------
rule(["minachiv.a_room_she_likes"], "later",
     '''Then she pushes you down, climbs over you, and finds your laces faster than you can find hers.{/n}''',
     '''Then she pushes you down, climbs over you, and finds your laces faster than you can find hers.{/n}
{n}Her thighs settle either side of your hips, bare and warm in the red light. She does not hurry. She unlaces you, pushes the cloth aside and lets you feel her heat against you, only that, only the promise of it, her hair swinging across your face.{/n}
"A thousand men paid for this, honey. You are getting it at cost. Say thank you."''')

rule(["minachiv.after_the_last_lamp"], "night",
     '''"There. I knew I kept you for something."''',
     '''"There. I knew I kept you for something."
{n}Behind the curtain she shoves the robe down her arms and lets it pool, puts your hands on her hips and walks you back until the bed catches your knees. She pushes you down and straddles you, bare, one knee either side, and drags your shirt up over your head, and bends until her mouth is at your ear.{/n}''')

rule(["minachiv.minaghos_unfinished_sentence"], "hand",
     '''{n}She stands, without letting go of your wrist, and tilts her head toward the room at the top of the stair.{/n}
"Well? The rain, or me?"''',
     '''{n}She stands, without letting go of your wrist, and drags your hand down over her hip and thigh, slowly, so that you feel the heat through her skirt and the muscle shift under it. Her mouth is at your ear, her breath sour with beer and blood. She tilts her head toward the room at the top of the stair.{/n}
"I am wet already, darling. Do not tell me the rain is more interesting."
"Well? The rain, or me?"''')

rule(["minachiv.before_the_last_road"], "together",
     '''The second settles it. The third knocks the case off the table, and nobody picks it up.''',
     '''The second settles it: Minagho's hand is inside Chivarro's gown and Chivarro's is under your shirt, and the couch is shrieking under three people's weight. The third knocks the case off the table, and nobody picks it up.''')

rule(["minachiv.the_unhired_evening"], "minagho_kiss",
     '''The step passes; she pulls you close again.{/n}''',
     '''The step passes; she pulls you close again.{/n}
{n}Her dress is round her hips, and then it is gone. She drags your belt open, sinks her teeth into your shoulder and grinds against you, bare and hot and wet, until you hear her breath break.{/n}
"One hour, Golarian. Hands. All of them."''')

rule(["minachiv.the_unhired_evening"], "chivarro_kiss",
     '''The step passes; she pulls you close again.{/n}''',
     '''The step passes; she pulls you close again.{/n}
{n}She peels the bodice off, takes your hand and lays it over her breast, then guides the other lower, to the heat under her skirts, and shows you exactly how slowly she wants it. She is bare to the waist and breathing like a woman who has stopped counting.{/n}
"Slowly, honey. I have been hurried by experts."''')

rule(["minachiv.the_unhired_evening"], "together_kiss",
     '''and Chivarro bends to kiss the hollow beneath Minagho's throat.{/n}''',
     '''and Chivarro bends to kiss the hollow beneath Minagho's throat.{/n}
{n}Minagho's knee goes between yours; Chivarro's hand finds the buckle at your waist and finds Minagho's fingers already there. For a moment they fight over it in the lamplight, laughing, breathless, all teeth, and then they stop fighting and open it together.{/n}
"Share, Minagho," {n}Chivarro says.{/n} "I am told it is good for the complexion."''')

# --- Epilogue invitations --------------------------------------------------------------
rule([MC + "epilogue.commit"], "pair",
     '''"And you leave when we want the bed to ourselves," {n}Minagho adds, pulling Chivarro close.{/n} "Agreed?"''',
     '''"And you leave when we want the bed to ourselves," {n}Minagho adds, pulling Chivarro close.{/n} "Agreed?"
{n}Her hand is already inside Chivarro's gown as she says it. Chivarro lets it stay, and lets you see.{/n}
"We started without you last night, honey," {n}Chivarro says.{/n} "An excellent rehearsal. Come and find out what it was rehearsing for."''')

rule([MC + "epilogue.commit"], "waiting",
     '''You have my invitation, honey. Read it properly."''',
     '''You have my invitation, honey. Read it properly."
{n}She has dressed for a visit, which is to say barely, and does not pretend otherwise.{/n}
"I have kept that bed warm for years. Come and see how warm."''')

_TOUCHED.update({"minachiv.a_room_she_likes", "minachiv.after_the_last_lamp", "minachiv.the_unhired_evening"})

# ======================================================================================
# JERRIBETH
# ======================================================================================
J = "jerribeth."

rule([J + "future"], "tenant_pinned",
     '''{n}She pushes you back into a pillow that does not exist,''',
     '''{n}She says nothing. She draws one claw down the front of you, pressing just hard enough to part cloth and not skin, and the room she has built shivers like a held breath: the cold carapace of her thighs, the rasp of her wings folding shut over a lamp that is not there, the buzzing that is in your teeth now and at the base of your spine.{/n}
"You offered," {n}she says, close against your ear.{/n} "I have been collecting every time you thought about it. Hold still. I want all of it before I spend it."
{n}She pushes you back into a pillow that does not exist,''')

rule([J + "future"], "tenant_free",
     '''in a room that is only real because you both agree it is. She lowers herself onto you''',
     '''in a room that is only real because you both agree it is. You find the seam beneath the carapace, the one soft place on her, and the sound she makes is like a held note breaking. Her claws shake against your shoulder.{/n}
"Careful," {n}she says, and does not mean it.{/n} "I am not accustomed to being handled. Do that again, and I may let you keep the hand."
{n}She lowers herself onto you''')

rule([J + "room_measure"], "desire",
     '''{n}Then she bends to you.{/n}''',
     '''{n}Then she bends to you. Her claws open your collar and the front of your clothes one fastening at a time, watching to see what each one costs, until the air of the room is on your skin and her mouth is a hand's breadth from it. The buzzing starts low in her chest. She straddles the chair, wings half open to shut out the shelves, and her hips settle onto yours with a slow, deliberate pressure that is already, undeniably, wet.{/n}''')

rule([J + "trickster.epilogue.commit"], "night",
     '''walked the Commander back to the bed by the wrists without once tightening her grip. When the Commander's knees met the mattress''',
     '''walked the Commander back to the bed by the wrists without once tightening her grip. Her mouth, such as it was, found the Commander's throat; the buzzing she kept for private moments came up through her chest and into the Commander's skin until the shiver and the sound were the same thing.{/n}
"I have studied every way you can be undone," {n}she said against the pulse,{/n} "and I intend to run the entire experiment."
{n}When the Commander's knees met the mattress''')

rule([J + "trickster.epilogue.commit"], "night_mind",
     '''She pushed the Commander back into a pillow that did not exist, settled astride''',
     '''They went down the Commander's throat and opened the shirt there with a surgeon's precision, and the cold of her came through the cloth and then through no cloth at all.{/n}
"Here," {n}she said, touching a place low on the Commander's ribs.{/n} "And here. You flinch the same way in every memory. I have been rehearsing the rest."
{n}She pushed the Commander back into a pillow that did not exist, settled astride''')

rule([J + "trickster.visit"], "threshold",
     '''{n}When your knees meet the edge of the mattress she lets you fall, and follows, and settles over you with her weight on her elbows and her wings half open, shutting out the lamp. Her claws close lightly round your wrists and press them into the blanket.{/n}''',
     '''{n}When your knees meet the edge of the mattress she lets you fall, and follows. Her claws open your shirt one fastening at a time, and her cool chitin presses the length of you, and she makes a small, pleased, entirely clinical sound at what she finds. She settles over you with her weight on her elbows and her wings half open, shutting out the lamp. Her claws close lightly round your wrists and press them into the blanket.{/n}
"You are shaking, and I have not started. Fascinating."''')

rule([J + "trickster.visit"], "threshold_free",
     '''She lets you pull her down. Her wings open''',
     '''She lets you pull her down. Your fingers find the pale seam under the carapace, the one place on her that is not armoured, and she hisses, a long dry rasp, and arches into it before she remembers to disapprove.{/n}
"Not there," {n}she says, and moves your hand back to it.{/n}
{n}Her wings open''')

rule([J + "unsold_evening"], "kiss",
     '''{n}She watches your face. She is not imagining it;''',
     '''{n}Her image opens the collar of her carapace the rest of the way, and her breath fogs the glass between you. One claw drags down the surface where your chest is, and you feel it anyway, a cold line from throat to belt.{/n}
{n}She watches your face. She is not imagining it;''')

_TOUCHED.update({"jerribeth.future", "jerribeth.room_measure", "jerribeth.unsold_evening"})

# ======================================================================================
# WENDUAG
# ======================================================================================
W = "wenduag.trickster."

rule([W + "court.cairn", W + "court.cairn.native_visit"], "decide",
     '''Her tail comes round your thigh, and tightens, and holds.{/n}''',
     '''Her tail comes round your thigh, and tightens, and holds.{/n}
"No talking," {n}she says, and her teeth close on your shoulder, deep enough to mark, and her breath hisses out against your neck, pleased and rough.{/n}
"Good. I hate waiting."''')

rule([W + "court.cairn", W + "court.cairn.native_visit"], "roll",
     '''and you are not sure any longer who is winning, and neither, from the sound of her, is she.{/n}''',
     '''and you are not sure any longer who is winning, and neither, from the sound of her, is she.{/n}
{n}Then she stops fighting. She hooks a foot behind yours and takes you down onto the cold stone, bare and furious with wanting, her hair across your face and her hands pinning yours.{/n}
"That's three," {n}she says against your mouth.{/n} "I win. The prize is you."''')

rule([W + "court.cairn", W + "court.cairn.native_visit"], "knife_down",
     '''She catches your lower lip between her teeth as you draw her closer.{/n}''',
     '''She catches your lower lip between her teeth as you draw her closer.{/n}
"Good," {n}she breathes.{/n} "I wanted the knife away. Not because I'm afraid of it." {n}Her hand slides over your ribs and flattens against your heart, firm and warm, and she smiles at how it pounds.{/n} "I wanted both your hands free."''')

rule([W + "court.gongs", W + "court.gongs.native_visit"], "saw",
     '''"Come down. I want that mouth of yours busy before another bell starts."''',
     '''"Come down. I want that mouth of yours busy before another bell starts."
{n}Her thumb drags across your lower lip, and she watches your face to see what it does. Her tail has wound itself round your wrist without asking.{/n}
"I have been thinking about it all night, up here with the bows. Every breath you took. I was not made for patience."''')

rule([W + "court.gongs", W + "court.gongs.native_visit"], "stronger",
     '''"Come down. You've had enough watchmen listening to you tonight."''',
     '''"Come down. You've had enough watchmen listening to you tonight."
{n}Her thumb drags across your lower lip. Her tail has wound itself round your wrist without asking, and she does not unwind it.{/n}
"And I want to hear you say things you would never say with a sentry listening. Walk."''')

rule([W + "court.hunt"], "ate",
     '''{n}She reaches over and wipes it off your chin with her thumb, and licks the thumb.{/n}''',
     '''{n}She shoves the deer aside with her knee and comes closer across the thorn, her leathers open at the throat and her breath coming quick. She takes your hand and drags it down inside them, to skin that is hot and tight and slick, and holds it there while she watches you understand. Then she reaches up with her other hand and wipes the blood off your chin with her thumb, and licks the thumb.{/n}''')

prule(W + "epilogue.pack", "page", "wenduag.trickster.vellexia.hunted",
      '''The succubus pulled her into the alcove, her open gown brushing the huntress's hands. Wenduag answered her kiss and drew her closer.''',
      '''The succubus pulled her into the alcove, her open gown brushing the huntress's hands, and pinned her to the wall by the throat, lightly, to see what the huntress would do about it. Wenduag showed her teeth, hooked a leg behind Vellexia's knee and turned her against the stones. "Predictable," Vellexia breathed, and unfastened the huntress's leathers herself. Wenduag answered her kiss and drew her closer.''')

# --- harem rows that carry Wenduag ------------------------------------------------------
rule(["household.pair.seelah_wenduag.choice"], "wenduag_yes",
     '''{n}Wenduag leads her toward the stairs, leaving her bow beside you.{/n}''',
     '''{n}Her hand has gone under the paladin's tabard, and Seelah's breath comes out hard and amused against her mouth. Wenduag bites the line of her throat, once, to feel the pulse jump; Seelah's hand tangles in Wenduag's hair and drags her head back, and neither of them is pretending the contest is anything but this.{/n}
{n}Wenduag leads her toward the stairs, leaving her bow beside you.{/n}''')

rule(["household.pair.wenduag_arueshalae.choice"], "threshold",
     '''Wenduag pulls her through the door.{/n}''',
     '''Wenduag pulls her through the door and slams it with her heel. Arueshalae's wings fold round them both; a hand pushes under Wenduag's leathers, and Wenduag bites the succubus's lip hard enough to taste blood and growls her approval into the kiss.{/n}''')

# ======================================================================================
# GESMERHA
# ======================================================================================
G = "gesmerha."

rule([G + "the_room_she_chose"], "lover",
     '''{n}Her mouth is still close to yours.{/n}''',
     '''{n}Her hand finds the hem of your shirt and goes under it, rough palm flat against your stomach, reading you the way she reads stone, and what she learns makes her breath catch. Her thumb crosses your hip bone and then lower, and rests there.{/n}
{n}Her mouth is still close to yours.{/n}''')

rule([G + "the_room_she_chose"], "first_kiss",
     '''Then she asks for another kiss.{/n}''',
     '''Then she asks for another kiss.{/n}
{n}It is a longer kiss than the first. Her palms go over your face, your throat, your shoulders, learning the shape of you with all the slow patience of her trade, and where they pass your pulse jumps and she feels it and smiles into your mouth. When she draws back she is breathing hard.{/n}
"I have spent weeks wanting the shape of you. Tell me you want me to learn the rest."''')

rule([G + "trickster.returned.bench"], "terms",
     '''She reaches for your hand and draws it against her waist.{/n}''',
     '''She reaches for your hand and draws it against her waist.{/n}
"I have chiselled since dawn and I am still not tired enough to stop thinking about your hands." {n}Her other hand finds your collar and stays there, and she tips her head so that her mouth is at your ear, her breath warm and unsteady.{/n}''')

rule([G + "trickster.returned.second_ask"], "sat",
     '''I have been thinking about it through every damned finger."''',
     '''I have been thinking about it through every damned finger."
{n}She sets the carving down and puts both your hands, the real ones, against her ribs, and holds them over the quick drum of her heart. Her thumb rubs once across your knuckle, as if checking the grain.{/n}
"Three days I have had your hands in front of me and not once been allowed to do more than measure them. Come here. Let me find out what they do when nobody is posing."''')

rule([G + "what_she_asks"], "touch",
     '''"The door," {n}she says against your mouth.{/n} "Or this bench''',
     '''{n}Her hand has gone to the front of your shirt, firm and unhesitating, and her other cups the back of your head as she kisses her way along your jaw. You feel her smile when your breath stutters.{/n}
"The door," {n}she says against your mouth.{/n} "Or this bench''')

# ======================================================================================
# HEPZAMIRAH
# ======================================================================================
H = "hepzamirah.trickster."

rule([H + "body.terms"], "threshold",
     '''"Mine tonight." {n}She bends to kiss you again. You meet her halfway.{/n}''',
     '''"Mine tonight." {n}She bends to kiss you again. You meet her halfway. Her teeth close on your lip and stay. A hand fists in your hair and drags your head back; the other drives down your stomach and under your belt and closes, with no gentleness at all. The horn stump rakes your cheek as she brings her mouth to your ear.{/n}
"Hold still, whelp. I am deciding how much of you I want."''')

rule([H + "bond.crooked"], "down",
     '''as she bends her head to your mouth.{/n}''',
     '''as she bends her head to your mouth.{/n}
{n}She takes your wrists and drags them to her hips, over the scars, and holds them there hard enough to bruise.{/n}
"There. Both hands. You do not let go until I say. Understood, whelp?"''')

rule([H + "bond.eve"], "face_say",
     '''{n}The good eye opens.{/n} "And you will come for me. Say it."''',
     '''{n}The good eye opens. Her hand fists in your shirt and drags you down until the heat of her is against you through the cloth, her hips driving into yours once, hard, a demand, and the pick slides off her lap and rings on the stones. She does not look at it.{/n} "And you will come for me. Say it."''')

rule([H + "bond.gift"], "kiss",
     '''and loosens it, and steps back.{/n}''',
     '''and loosens it, and steps back.{/n}
{n}The thong lies against your throat, warm from her hands. She breathes through her teeth, and the scarred side of her face and the stump of the horn are both flushed dark, and she does not take her one good eye off your mouth.{/n}''')

rule([H + "bond.her_room"], "sit_say",
     '''"Do not argue. You have seen what I do to people who take my things."''',
     '''"Do not argue. You have seen what I do to people who take my things."
{n}Her hand is still round yours. She drags it up inside her coat, over her ribs and the old scars, and holds it flat against her pounding heart, then lower. Her mouth is at your ear, her voice a low hot rasp.{/n}
"You are mine, so I will have the use of you tonight. All of it. Do not talk to me about gentleness."''')

# ======================================================================================
# SHAMIRA
# ======================================================================================
SH = "shamira.trickster."

rule([SH + "after.night_alone"], "read",
     '''You may look at me while I warm these hands."''',
     '''You may look at me while I warm these hands."
{n}She tilts her head toward the blanket you hold up, and the grey lips curve. Her hands, when she holds them out for you to see, shake very slightly.{/n}
"Cold to the bone, mortal. The coal was a gift and a leash both. Tonight I do not want to be clever. I want skin on skin, and your heat in every place that went coldest."''')

rule([SH + "after.night_alone"], "offered",
     '''You offered. I never give anything back."''',
     '''You offered. I never give anything back."
{n}Her mouth finds the corner of yours, cold, then not cold. She draws your hand under the red silk and flat against her ribs, and holds it there until you feel her shiver and her breath catch.{/n}
"Now, Commander. Warm me. It is the least you can do for a queen you have robbed."''')

rule([SH + "epilogue.late"], "late_initiation",
     '''then drew her lover down onto the warm steps.{/n}''',
     '''then drew her lover down onto the warm steps.{/n}
{n}Her cold hands worked under the Commander's shirt and found the heat there, and she made a low sound of pure hunger against the Commander's throat.{/n}
"Still warm," {n}she said.{/n} "How rude, to be so warm. I mean to take all of it."''')

rule([SH + "harem", SH + "harem_awning"], "cut",
     '''and her palm presses against your hammering heart.{/n}''',
     '''and her palm presses against your hammering heart.{/n}
"Warm, and trembling, and mine for the length of one bell," {n}she says, rocking once against you, slow, to feel it land.{/n}''')

_TOUCHED.update({"wenduag.trickster.court.cairn", "gesmerha.the_room_she_chose", "hepzamirah.trickster.bond.gift"})

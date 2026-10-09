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

"""Nocticula: heat pass (Directive 12), applied last by nocticula_cloud.integrate.

Text only. No scene, node or choice id, choice position, Next, Set, gate or check
changes. Each READY explicit slot keeps its slot node, its successor and its stop
line.

Calibration (2026-10-09, heat batch a): every intimate scene sits at the heat of
the official Wrath of the Righteous romances (knowledge/lore/canon-heat-reference.md).
The act is never narrated. The build-up carries her appetite, the cut is one short
second-person paragraph that stops at the first heated contact or a time-warp line,
and the maturity (audience, power, jealousy, discovery, a hunt) lands through staging
and her frank speech, not through positions or anatomy.

  * SUBS strips anything past the official register out of a build-up node in place;
  * single-exit build-up nodes get an appended heat passage in her voice;
  * build-up nodes that also offer another branch (a conversation, a refusal) stay
    untouched, and the heat sits in the slot node's lead-in instead, so a player who
    declines the intimate answer never reads it;
  * every slot node's text is the cut beat: it ends where the official games cut.
"""

# Exact-substring edits to build-up nodes: (scene, node, old, new). Each old string
# must exist; a missing one is an error, never a silent skip.
SUBS = [
    ("noct.unlit_quay", "later",
     "When she has had enough of your standing she pushes you down onto the cushions and follows you down, a knee on either side of you, her hair falling round both your faces.",
     "When she has had enough of your standing she pulls you down onto the cushions by your open collar, her hair falling round both your faces."),
    ("noct.her_own_face", "night",
     "and she comes down after you, a knee on either side of your hips, her hair falling round both your faces like a drawn curtain.",
     "and she comes down after you, her hair falling round both your faces like a drawn curtain."),
    ("noct.her_own_face", "night",
     "The lamplight narrows to the bright edge of her hair, then vanishes.{/n}",
     "Her mouth leaves yours and travels down your jaw. The gown has slid from her shoulders, and she presses the whole bare length of herself against you, skin hot, the lamp painting her gold and unashamed. Her laugh in your ear has no mask in it at all.{/n}"),
    ("nocticula.trickster.defeated.chair", "threshold",
     "settles astride your hips with a weight that is very real indeed, and leans down",
     "follows with a weight that is very real indeed, and leans down"),
    ("nocticula.trickster.epilogue.commit", "kissed",
     "rose over them, astride, one hand flat on the Commander's chest to keep them exactly where she wanted them, and the lamps of her palace went out one by one, in no hurry at all.",
     "bent over them, one hand flat on the Commander's chest to keep them exactly where she wanted them, while the lamps of her palace burned on, because she wished to be seen."),
    ("nocticula.trickster.epilogue.commit", "knelt",
     "and let her robe fall open over the Commander's head like a tent. Her fingers closed in the Commander's hair, holding them exactly where she wanted them, and the lamps of her palace went out one by one, in no hurry at all.",
     "and let her robe fall open as she stood over the kneeling Commander. Her fingers closed in the Commander's hair, holding them exactly where she wanted them, at her feet, while the lamps of her palace burned on, because she wished to be seen."),
    ("nocticula.trickster.epilogue.commit", "walked",
     "and followed the Commander down, and settled astride, and the last lamp went out while she was still smiling.",
     "and followed the Commander down, smiling."),
]

# Appended to a build-up node (single exit into the slot).
APPEND = {
    ("noct.acq.an_answer_of_her_own", "accept"): '''
{n}Her next line arrives while the ink is still wet, in a hand grown less careful by degrees.{/n}
"I have been honest about my bed, so be honest about yours. I would take you slowly, to teach you what impatience costs, and I would not stop when you begged. Your wrists where I could see them. My name in your mouth more often than you have said it in all your clever letters, and every time you would mean it."
{n}The page smells faintly of night-blooming flowers. Beneath the last line she has drawn one thin black crescent, as if marking where a nail would go.{/n}
"The undertaking I kept is still in my drawer, darling. It is not a kindness, and neither is anything I want from you. Write me what you would let me do."
{n}You dip the pen. The lamp gutters, and your hand is not entirely steady.{/n}''',
    ("noct.acq.the_paid_address", "an_answer_of_her_own.accept"): '''
{n}Her next line arrives while the ink is still wet, in a hand grown less careful by degrees.{/n}
"I have been honest about my bed, so be honest about yours. I would take you slowly, to teach you what impatience costs, and I would not stop when you begged. Your wrists where I could see them. My name in your mouth more often than you have said it in all your clever letters, and every time you would mean it."
{n}The page smells faintly of night-blooming flowers. Beneath the last line she has drawn one thin black crescent, as if marking where a nail would go.{/n}
"The undertaking I kept is still in my drawer, darling. It is not a kindness, and neither is anything I want from you. Write me what you would let me do."
{n}You dip the pen. The lamp gutters, and your hand is not entirely steady.{/n}''',
    ("noct.second_door", "yes"): '''
{n}The dark smells of her: night-blooming flowers, hot wax, something older underneath. Her hands drag your shirt up and off and her teeth find the cord of your neck. She has your belt open before you have breath to laugh.{/n}
"They heard the latch," {n}she says, low, against your collarbone.{/n} "Let them wonder what they cannot hear." {n}Black silk whispers; a robe slides to the floor, and the whole warm length of her presses against you where you stand.{/n}''',
    ("noct.second_door", "power"): '''
{n}The black door slams on the silent Harem. In the dark she shoves you back across the black silk and stands over you, unpinning her hair with slow, insolent fingers. The robe goes next, and she is a long pale outline against the faint red of the window, hungry and delighted with the whole evening.{/n}
"Let him count the minutes," {n}she says, bending over you.{/n} "I am busy with the better half of mine."''',
    ("noct.unlit_quay", "later"): '''
{n}The black dress is gone, a pool of silk on the stone. She drags your shirt open and rakes her nails across the skin she uncovers, watching you shiver, her smile slow and deliberate.{/n}
"Not a word," {n}she breathes.{/n} "You asked for me. Let me be worth the asking."''',
    ("nocticula.trickster.defeated.chair", "threshold"): '''
{n}Her cold hands work beneath what is left of your clothes and find you hot and trembling; the contrast draws a low, delighted sound from her. Your reaching hands close on shadow, and she leans into the nothing of them as if your failing to hold her were the best part of it.{/n}
"Cold," {n}she murmurs,{/n} "and you shake anyway. Good. Do not try to touch me, darling. Let me do all of it. Let me be unforgivably thorough."
{n}Her mouth leaves yours and descends the line of your throat. The throne holds you where she put you, and your breath stutters.{/n}''',
    ("nocticula.trickster.epilogue.commit", "kissed"): '''
{n}Her robe fell open. The Commander's coat went wherever she flicked it, and her mouth followed her hands down the Commander's throat and chest, hungry and entirely unapologetic. She took the Commander's hands and set them on her hips and held them there, her eyes half closed.{/n}
"Years of shadow," {n}she said,{/n} "and you are warm. Let me find out how warm."''',
    ("nocticula.trickster.epilogue.commit", "knelt"): '''
{n}The Commander's hands found her bare hips unforbidden, and she let them, with a long breath through her teeth. Whatever authority she wore, she wore it for the pleasure of being met; when the Commander pulled her mouth down to theirs, the sound she made was nothing like a command.{/n}''',
    ("nocticula.trickster.epilogue.commit", "walked"): '''
{n}Her gown parted at the Commander's hands and fell. She dragged the Commander's shirt up and off, pressed bare skin to bare skin, and bent to bite the Commander's lower lip.{/n}
"Say it again," {n}she whispered,{/n} "that you wanted to hear it twice. I will say it as often as you like. Yes."''',
}

# Slot-node texts: the cut beat. One short narrated paragraph after the last
# heated contact, then the scene resumes at its aftermath.
CUTS = {
    "noct.acq.an_answer_of_her_own.explicit.1": '''{n}You bring the sheet closer and begin to write, slowly, exactly what you would let her do. Her next line arrives before the ink beneath your answer has dried, and it does not ask permission. By the time the lamp gutters the page is black to the margin, your hand is not steady, and the wax beside your name is as warm as skin.{/n}''',
    "noct.acq.the_paid_address.explicit.1": '''{n}You bring the sheet closer and begin to write, slowly, exactly what you would let her do. Her next line arrives before the ink beneath your answer has dried, and it does not ask permission. By the time the lamp gutters the page is black to the margin, your hand is not steady, and the wax beside your name is as warm as skin.{/n}''',
    "noct.acq.epilogue.correspondence.explicit.1": '''{n}Nocticula took the Commander's hand and closed the chamber door. She walked the Commander backwards to the bed, unhurried, a queen collecting something owed, and pushed until the Commander sat. Her robe parted at the throat under the Commander's hands; she let it fall and stood over them in the lamplight, bare and smiling, the half-seal forgotten beside the travel papers.{/n}
"Years of letters," {n}she said, bending to the Commander's mouth.{/n} "I have read every one. Now I would like to be answered in person."
{n}The lamp burned on beside the bed, and for the rest of the night nothing more was written.{/n}''',
    "noct.another_place.explicit.1": '''{n}Nocticula looks at Laulieh, at the blood she has kept on her cheek for effect, and smiles.{/n} "Come here, Laulieh. You've earned it, and the Commander has never seen you earn anything properly."
{n}She crooks a finger at Laulieh, and then at you. The hatbox stays where it is, on the dressing table, for the rest of the night.{/n}
{n}Laulieh is on the couch before the finger has finished curling, green skirts crushed, horns tipped back as Nocticula slips the black robe from her own shoulders and lets it pool on the cushions. The succubus laughs, hot-eyed, and glances up at you with her wicked, bloodied smile, as if to say she has been practising for an audience.{/n}
"Eyes on her, darling," {n}Nocticula murmurs, one fist in green hair, her other hand held out to you, palm up, waiting.{/n} "Then on me. I want you to learn which of us you cannot stop looking at."
{n}You take the hand. Laulieh's laugh is the last clear sound; after it come skin and breath and the three of you, and the night forgets its own length.{/n}''',
    "noct.empty_chair.explicit.1": '''{n}She does not untie it. She puts you against the edge of the table instead, among the wax and the charcoal, and keeps one hand on the ribbon at the back of your head, where the hook is. The painted smile is cold against your cheek when she turns your face to the candlelight; her other hand drags your shirt open and her mouth follows it, hot where the mask is cold.{/n}
"Pull and you leave your hair on my table," {n}she breathes.{/n} "Istrava gives her quarry a head start. I give you none. Keep very still, quarry, and let me hunt."
{n}Her breath is hot beneath the cold paint, and the lodge, the stairs and the candles go out of your mind.{/n}''',
    "noct.her_own_face.explicit.1": '''{n}She draws your head aside with one hand in your hair and lowers her mouth to the side of your throat, where the pulse beats against her lips. Her teeth rest against your skin, not yet closing.{/n}
"Hold still, darling," {n}she whispers.{/n} "Look at me while I decide how much of you to keep."
{n}Then she closes her teeth, and the room goes white and hot, and time ceases to matter. When it returns, the lamp is still burning where she left it, there is the taste of your own blood on her mouth, and her laugh against your ear.{/n}''',
    "noct.last_buyer.explicit.1": '''{n}She does not wait for the stair to empty. She has you against the wall under the nearest lamp, and every chained face in the row is turned toward the light, toward the two of you, unable to look away; she makes sure of that.{/n}
"Say my name for them," {n}she murmurs, pinning your wrists above your head with one hand while the other works at your clothes, quick and possessive, her mouth hot on your throat. The stone is cold against your back.{/n} "Let them remember how it sounds when you pay."
{n}Her breath is at your ear, her skin is fire against the cold wall, and for a long while the only sounds in the cells are the two of you and the small, helpless noise of chains.{/n}''',
    "noct.second_door.explicit.1": '''{n}The latch falls behind you. Through the door, the Harem has gone very quiet. She backs you into the wood and lays your hand over her breast, her breath breaking against your ear.{/n}
"Louder, if you like," {n}she whispers.{/n} "They have waited all night to be scandalised."
{n}Then her mouth is on yours, and the dark closes over the two of you, and time ceases to exist.{/n}''',
    "noct.second_door.explicit.2": '''{n}She pulls you down to the silk and pins your wrists above your head with one hand, smiling with every tooth. Outside the door the courtier is still waiting in front of the whole Harem, and she has forgotten him entirely.{/n}
"Now you may have what I kept you for," {n}she says against your mouth, and for a long while neither of you remembers there is a door.{/n}''',
    "noct.unborrowed_evening.explicit.1": '''{n}You stop talking. She moves the knife to the far end of the sill, out of your reach and well within hers, and pulls you down under the window, with the city burning on the other side of the glass. Her mouth is on yours before you land, hot and sticky with pear, her fist in your collar; she opens the hooks of the black gown one by one without looking, the dried blood at its hem crackling against the cushions, and shoves it off her shoulders.{/n}
"The hunt left me hungry," {n}she says against your jaw, her hand dragging down your chest.{/n} "I have no patience left for you tonight."
{n}She holds your eyes a moment longer, then her mouth takes yours again, and the window, the city and the knife on the sill fall out of the world.{/n}''',
    "noct.unlit_quay.explicit.1": '''{n}She spares one glance over the rail for the man on the rope.{/n} "He will keep," {n}she says, and looks down at you with a smile that is all appetite.{/n} "You will not, darling. Not tonight."
{n}Her mouth comes down on yours, and time lets go of the quay. There is her heat, her breath at your ear, her nails dragged down your back, and the lamps burning on below the rail until you could not say how long.{/n}''',
    "nocticula.trickster.defeated.chair.explicit.1": '''{n}Her cold hand closes over yours, pinning it to the arm of the throne, and her mouth finds yours again, cold turning to heat by degrees you cannot measure. Of the camp, the sentries and the war nothing reaches you but her breath and her slow, delighted laugh. Beyond the darkness, Threshold's fires burn through the night.{/n}''',
    "nocticula.trickster.epilogue.commit.explicit.1": '''{n}She kept the Commander close in the royal chair, her hands in their hair, and bent to the Commander's ear. "Now," said the Queen of Shadows, with a smile that promised to take its time, and her mouth closed over theirs. Her palace, her chair and the long years of shadow ceased to matter until morning.{/n}''',
    "nocticula.trickster.epilogue.commit.explicit.2": '''{n}She caught the Commander's hand and drew them nearer, her robe falling open, her breath coming hard against their ear. "Hold on," she said, almost kindly, and the palace lamps burned on behind her until the night ran out.{/n}''',
    "nocticula.trickster.epilogue.commit.explicit.3": '''{n}She took the Commander's hand and set it at her waist, holding their eyes with hers. "Yes," she said once more, against their mouth, and her breath caught, and the world ceased to exist.{/n}''',
}


def apply(payload):
    by = {s["Id"]: s for s in payload["Scenes"]}
    nodes = {}
    for sid, scene in by.items():
        for node in scene["Nodes"]:
            nodes[(sid, node["Id"])] = node
    for sid, node_id, old, new in SUBS:
        node = nodes.get((sid, node_id))
        if node is None:
            raise ValueError(f"nocticula_heat: missing {(sid, node_id)}")
        if old not in node["Text"]:
            raise ValueError(f"nocticula_heat: {(sid, node_id)} no longer carries {old[:50]!r}")
        node["Text"] = node["Text"].replace(old, new, 1)
    for key, text in APPEND.items():
        node = nodes.get(key)
        if node is None:
            raise ValueError(f"nocticula_heat: missing {key}")
        if text.strip() in node["Text"]:
            raise ValueError(f"nocticula_heat: {key} already carries the heat passage")
        node["Text"] = node["Text"].rstrip() + text
    for node_id, text in CUTS.items():
        sid = node_id.rsplit(".explicit.", 1)[0]
        node = nodes.get((sid, node_id))
        if node is None:
            raise ValueError(f"nocticula_heat: missing slot node {node_id}")
        node["Text"] = text
    return payload

"""Nocticula: heat pass (Directive 12), applied last by nocticula_cloud.integrate.

Text only. No scene, node or choice id, choice position, Next, Set, gate or check
changes. Each READY explicit slot keeps its slot node, its successor and its stop
line; this layer lets the scene's heat reach the START of the act:

  * single-exit build-up nodes get an appended heat passage in her voice;
  * build-up nodes that also offer another branch (a conversation, a refusal) stay
    untouched, and the heat sits in the slot node's lead-in instead, so a player who
    declines the intimate answer never reads it;
  * every slot node's default lead-in is rewritten to end at the boundary where the
    separately filled explicit segment begins. The explicit act itself is not written.
"""

# Appended to a build-up node (single exit into the slot).
APPEND = {
    ("noct.acq.an_answer_of_her_own", "accept"): '''
{n}Her next line arrives while the ink is still wet, in a hand grown less careful by degrees.{/n}
"I have been honest about my bed, so be honest about yours. I would take you slowly, to teach you what impatience costs, and I would not stop when you begged. Your wrists where I could see them. Your mouth where I could use it. You would say my name more often than you have said it in all your clever letters, and you would mean it every time."
{n}The page smells faintly of night-blooming flowers. Beneath the last line she has drawn one thin black crescent, as if marking where a nail would go.{/n}
"The undertaking I kept is still in my drawer, darling. It is not a kindness, and neither is anything I want from you. Write me what you would let me do."
{n}You dip the pen. The lamp gutters, and your hand is not entirely steady.{/n}''',
    ("noct.acq.the_paid_address", "an_answer_of_her_own.accept"): '''
{n}Her next line arrives while the ink is still wet, in a hand grown less careful by degrees.{/n}
"I have been honest about my bed, so be honest about yours. I would take you slowly, to teach you what impatience costs, and I would not stop when you begged. Your wrists where I could see them. Your mouth where I could use it. You would say my name more often than you have said it in all your clever letters, and you would mean it every time."
{n}The page smells faintly of night-blooming flowers. Beneath the last line she has drawn one thin black crescent, as if marking where a nail would go.{/n}
"The undertaking I kept is still in my drawer, darling. It is not a kindness, and neither is anything I want from you. Write me what you would let me do."
{n}You dip the pen. The lamp gutters, and your hand is not entirely steady.{/n}''',
    ("noct.her_own_face", "night"): '''
{n}Her mouth leaves yours and travels down your jaw. The gown has slid from her shoulders, and she presses the whole bare length of herself against you, skin hot, the lamp painting her gold and unashamed. She rolls her hips down once, slowly, so that you feel exactly how long she has waited, and her laugh in your ear has no mask in it at all.{/n}''',
    ("noct.second_door", "yes"): '''
{n}The dark smells of her: night-blooming flowers, hot wax, something older underneath. Her hands drag your shirt up and off and her teeth find the cord of your neck. She has your belt open and is working at the rest of it before you have breath to laugh.{/n}
"They heard the latch," {n}she says, low, against your collarbone.{/n} "Let them wonder what they cannot hear." {n}Black silk whispers; a robe slides to the floor, and the whole warm length of her presses against you where you stand.{/n}''',
    ("noct.second_door", "power"): '''
{n}The black door slams on the silent Harem. In the dark she shoves you back across the black silk and stands over you, unpinning her hair with slow, insolent fingers. The robe goes next, then the rest, and she is a long pale outline against the faint red of the window, hungry and delighted with the whole evening.{/n}
"Let him count the minutes," {n}she says, climbing over you, a knee on either side of your hips.{/n} "I am busy with the better half of mine."''',
    ("noct.unlit_quay", "later"): '''
{n}The black dress is gone, a pool of silk on the stone. She drags your shirt open and rakes her nails down the skin she uncovers, watching you shiver, then rocks her bare hips against yours with a slow, deliberate smile.{/n}
"Not a word," {n}she breathes.{/n} "You asked for me. Let me be worth the asking."''',
    ("nocticula.trickster.defeated.chair", "threshold"): '''
{n}Her cold hands work beneath what is left of your clothes and find you hot and trembling; the contrast draws a low, delighted sound from her. Your reaching hands close on shadow, and she leans into the nothing of them as if your failing to hold her were the best part of it.{/n}
"Cold," {n}she murmurs,{/n} "and you shake anyway. Good. Do not try to touch me, darling. Let me do all of it. Let me be unforgivably thorough."
{n}Her mouth leaves yours and descends the line of your throat. The throne holds you where she put you, and her hips begin a slow, grinding circle that makes your breath stutter.{/n}''',
    ("nocticula.trickster.epilogue.commit", "kissed"): '''
{n}Her robe fell open. The Commander's coat went wherever she flicked it, and her mouth followed her hands down the Commander's throat and chest, hungry and entirely unapologetic. She took the Commander's hands and set them on her hips and rolled against them, slowly, once, with her eyes half closed.{/n}
"Years of shadow," {n}she said,{/n} "and you are warm. Let me find out how warm."''',
    ("nocticula.trickster.epilogue.commit", "knelt"): '''
{n}The Commander's hands went up her bare thighs unforbidden, and she let them, with a long breath through her teeth. Whatever authority she wore, she wore it for the pleasure of being met; when the Commander's mouth found the inside of her thigh, the sound she made was nothing like a command.{/n}''',
    ("nocticula.trickster.epilogue.commit", "walked"): '''
{n}Her gown parted at the Commander's hands and fell. She dragged the Commander's shirt up and off, pressed bare skin to bare skin, and bent to bite the Commander's lower lip.{/n}
"Say it again," {n}she whispered,{/n} "that you wanted to hear it twice. I will say it as often as you like. Yes."''',
}

# Substrings removed from a build-up so that no lamp is snuffed in place of the act.
TRIM = {
    ("nocticula.trickster.epilogue.commit", "kissed"): (
        ", and the lamps of her palace went out one by one, in no hurry at all.",
        ", while the lamps of her palace burned on, because she wished to be seen."),
    ("nocticula.trickster.epilogue.commit", "knelt"): (
        ", and the lamps of her palace went out one by one, in no hurry at all.",
        ", and the lamps of her palace burned on, because she wished to be seen."),
    ("nocticula.trickster.epilogue.commit", "walked"): (
        ", and the last lamp went out while she was still smiling.", ", smiling."),
}

# Slot-node lead-ins: rewritten to end at the start of the act.
CUTS = {
    "noct.acq.an_answer_of_her_own.explicit.1": '''{n}You bring the sheet closer and begin to write, slowly, exactly what you would let her do. Her next line arrives before the ink beneath your answer has dried, and it does not ask permission.{/n}''',
    "noct.acq.the_paid_address.explicit.1": '''{n}You bring the sheet closer and begin to write, slowly, exactly what you would let her do. Her next line arrives before the ink beneath your answer has dried, and it does not ask permission.{/n}''',
    "noct.acq.epilogue.correspondence.explicit.1": '''{n}Nocticula took the Commander's hand and closed the chamber door. She walked the Commander backwards to the bed, unhurried, a queen collecting something owed, and pushed until the Commander sat. Her robe parted at the throat and then lower, under the Commander's hands; she let it fall and stood over them in the lamplight, bare and smiling, the half-seal forgotten beside the travel papers.{/n}
"Years of letters," {n}she said, climbing onto the Commander's lap, a knee on either side.{/n} "I have read every one. Now I would like to be answered in person."''',
    "noct.another_place.explicit.1": '''{n}Nocticula looks at Laulieh, at the blood she has kept on her cheek for effect, and smiles.{/n} "Come here, Laulieh. You've earned it, and the Commander has never seen you earn anything properly."
{n}She crooks a finger at Laulieh, and then at you. The hatbox stays where it is, on the dressing table, for the rest of the night.{/n}
{n}Laulieh is on the couch before the finger has finished curling, green skirts rucked, horns tipped back as Nocticula drags the black robe off her own shoulders and lets it pool on the cushions. The succubus kneels between her lady's knees with a sound like a purr, kisses the inside of one thigh, then the other, and glances up at you with her wicked, bloodied smile, as if to say she has been practising for an audience.{/n}
"Eyes on her, darling," {n}Nocticula murmurs, one fist in green hair, her other hand held out to you, palm up, waiting.{/n}''',
    "noct.empty_chair.explicit.1": '''{n}She does not untie it. She puts you against the edge of the table instead, among the wax and the charcoal, and keeps one hand on the ribbon at the back of your head, where the hook is. The painted smile is cold against your cheek when she turns your face to the candlelight; her other hand drags your shirt open and her mouth follows it, hot where the mask is cold. The black table creaks as she lifts you onto it and steps between your knees.{/n}
"Pull and you leave your hair on my table," {n}she breathes.{/n} "Istrava gives her quarry a head start. I give you none. Keep very still, quarry, and let me hunt."''',
    "noct.her_own_face.explicit.1": '''{n}She draws your head aside with one hand in your hair and lowers her mouth to the side of your throat, where the pulse beats against her lips. Her hips settle against yours, her breath hot, her teeth resting against your skin but not yet closing.{/n}
"Hold still, darling," {n}she whispers.{/n} "Look at me while I decide how much of you to keep."''',
    "noct.last_buyer.explicit.1": '''{n}She does not wait for the stair to empty. She has you against the wall under the nearest lamp, and every chained face in the row is turned toward the light, toward the two of you, unable to look away; she makes sure of that.{/n}
"Say my name for them," {n}she murmurs, pinning your wrists above your head with one hand while the other works at your clothes, quick and possessive, her mouth hot on your throat. The stone is cold against your back. Her hip drives between yours.{/n} "Let them remember how it sounds when you pay."''',
    "noct.second_door.explicit.1": '''{n}The latch falls behind you. Through the door, the Harem has gone very quiet. She backs you into the wood, hooks one leg around yours, and takes your hand and puts it exactly where she wants it, her breath breaking against your ear.{/n}''',
    "noct.second_door.explicit.2": '''{n}She pulls you down to the silk, straddles you, and pins your wrists above your head with one hand. Her other hand slides down between your bodies, deliberate, and she smiles with every tooth. Outside the door the courtier is still waiting, and she has forgotten him entirely.{/n}''',
    "noct.unborrowed_evening.explicit.1": '''{n}You stop talking. She moves the knife to the far end of the sill, out of your reach and well within hers, and pulls you down under the window, with the city burning on the other side of the glass. Her mouth is on yours before you land, hot and sticky with pear, her fist in your collar; she opens the hooks of the black gown one by one without looking, the dried blood at its hem crackling against the cushions, and shoves it off her shoulders.{/n}
"The hunt left me hungry," {n}she says against your jaw, her hand dragging down your chest.{/n} "I have no patience left for you tonight."
{n}She rolls you beneath her and straddles you, thighs gripping, and holds your eyes for a moment as her hips begin to move against yours.{/n}''',
    "noct.unlit_quay.explicit.1": '''{n}She sits back on your hips, spreads her palms on your chest, and spares one glance over the rail for the man on the rope. "He will keep," she says, and looks down at you with a smile that is all appetite. "You will not, darling. Not tonight." She lowers herself over you, slowly, deliberately, taking her time.{/n}''',
    "nocticula.trickster.defeated.chair.explicit.1": '''{n}Her cold hand closes over yours, pinning it to the arm of the throne, and she sinks lower against you, her other hand dragging down your stomach. Beyond the darkness, Threshold's fires burn through the night.{/n}''',
    "nocticula.trickster.epilogue.commit.explicit.1": '''{n}She kept the Commander close in the royal chair, her thighs bracketing theirs, and bent to the Commander's ear. "Now," said the Queen of Shadows, and reached between them with a smile that promised to take its time, and the chair creaked under her.{/n}''',
    "nocticula.trickster.epilogue.commit.explicit.2": '''{n}She caught the Commander's hand and drew them nearer, her robe open, one leg lifted over the Commander's shoulder. The palace lamps burned on behind her.{/n}''',
    "nocticula.trickster.epilogue.commit.explicit.3": '''{n}She took the Commander's hand and guided it low between her thighs, holding their eyes with hers, and rolled her hips against it, slow and deliberate. "Yes," she said once more, against their mouth, and her breath caught.{/n}''',
}


def apply(payload):
    by = {s["Id"]: s for s in payload["Scenes"]}
    nodes = {}
    for sid, scene in by.items():
        for node in scene["Nodes"]:
            nodes[(sid, node["Id"])] = node
    for key, text in APPEND.items():
        node = nodes.get(key)
        if node is None:
            raise ValueError(f"nocticula_heat: missing {key}")
        if text.strip() in node["Text"]:
            raise ValueError(f"nocticula_heat: {key} already carries the heat passage")
        trim = TRIM.get(key)
        if trim and trim[0] in node["Text"]:
            node["Text"] = node["Text"].replace(trim[0], trim[1])
        node["Text"] = node["Text"].rstrip() + text
    for node_id, text in CUTS.items():
        sid = node_id.rsplit(".explicit.", 1)[0]
        node = nodes.get((sid, node_id))
        if node is None:
            raise ValueError(f"nocticula_heat: missing slot node {node_id}")
        node["Text"] = text
    return payload

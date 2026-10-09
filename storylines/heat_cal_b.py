"""Heat calibration, batch b (Claude prose, 2026-10-09): official-register rewrite.

Owner direction: every intimate scene matches the heat of the official WotR romances (no act or
anatomy narrated past the cut; desire, appetite, risk, power and consequence carried by situation
and frank in-voice dialogue). Scope: Minagho/Chivarro, Jerribeth, and four household pair scenes.

Text only. It runs after heat_g4, so it edits the finished text of each node and paragraph. Ids,
Next, Set, Requires/Forbids, checks, choice order and costs are untouched. Every rule asserts that the
fragment it replaces exists and raises on drift, as the cloud and heat layers do.
"""

SCENES = (
    "minachiv.the_unhired_evening", "minachiv.minaghos_unfinished_sentence", "minachiv.a_room_she_likes",
    "minachiv.after_the_last_lamp", "minachiv.before_the_last_road",
    "minagho_chivarro.trickster.after.before_the_last_road",
    "minagho_chivarro.trickster.after.before_the_last_road_letter",
    "minagho_chivarro.trickster.alone.chivarro", "minagho_chivarro.trickster.alone.chivarro_letter",
    "minagho_chivarro.trickster.alone.minagho", "minagho_chivarro.trickster.alone.minagho_spared",
    "minagho_chivarro.trickster.alone.minagho_letter", "minagho_chivarro.trickster.after.when_it_scars",
    "minagho_chivarro.trickster.alone.minagho_when_it_scars",
    "minagho_chivarro.trickster.alone.chivarro_when_it_scars", "minagho_chivarro.trickster.epilogue.commit",
    "jerribeth.future", "jerribeth.unsold_evening", "jerribeth.counterfeit_after", "jerribeth.room_measure",
    "jerribeth.trickster.epilogue.commit", "jerribeth.trickster.visit",
    "household.pair.seelah_wenduag.choice", "household.pair.wenduag_arueshalae.choice",
    "household.pair.camellia_arueshalae.choice", "household.pair.nenio_arueshalae.choice",
    "household.pair.nenio_arueshalae.choice.warded",
)

# (old fragment, new fragment): exact substring, applied to every node and paragraph in SCENES.
SUBS = []
# (start fragment, end fragment, new): replaces from start through end inclusive.
SPANS = []


def sub(old, new):
    SUBS.append((old, new))


def span(start, end, new):
    SPANS.append((start, end, new))


# ======================================================================================
# MINAGHO / CHIVARRO: shared secret-night nodes (every stance scene that carries them)
# ======================================================================================

# Minagho's secret night.
span("{n}Minagho comes after the watch changes.", "\"I do not ask twice.\"",
     '''{n}Minagho comes after the watch changes. She kicks the door shut, tears your shirt open and slams you against it. Her mouth catches yours; her teeth find your lip and stay there until she tastes blood.{/n}
"Quiet, Golarian. I want her to wonder where I spent the night."
{n}Chivarro's step sounds on the stair below and neither of you moves. Minagho laughs without a sound into your throat, one claw hooked in your open collar, and waits for the step to pass before she hauls you toward the bed.{/n}
"She would know my scent on you from across the market. Let her. Let her find it on the sheets and choke on it. Hands, Golarian. I am not made of glass."
{n}Her dress is already sliding off her shoulder when your hands find her hips.{/n}''')

# Minagho's cut after the secret night (farewell-letter scene).
span("{n}Minagho shoves the farewell aside", "You can make speeches when I let you go.\"",
     '''{n}Minagho shoves the farewell aside with her forearm and takes your collar in both hands. The lamp gutters and time goes with it: her hot breath at your ear, her claws on your ribs, a laugh in her throat that turns into something she would deny to anyone but you.{/n}
"You can make speeches when I let you go."
{n}Afterwards she lies across you with her heel hooked over your leg, smug as a cat on a stolen cushion, and listens to the stairs for Chivarro.{/n}''')

# Chivarro's secret night.
sub(''', then walks you back to the bed, pushes you down and climbs over you, bare thighs either side of your hips and loose hair across your chest. The closed account stays on the shelf.''',
    ''', then walks you back to the bed and pushes you down onto it, loose hair across your chest. The closed account stays on the shelf.''')
sub('''{n}She drags your hand up the inside of her thigh to the heat she has been keeping from you, and holds it there.{/n}''',
    '''{n}She catches your hand at her hip and holds it there, and you feel her smile against your mouth.{/n}''')

# Chivarro's service night.
sub('''strips you with brisk, practised fingers and settles over you, knees either side of your hips. Her mouth moves down your throat to your chest. One of her hands slides between her own thighs, and she smiles against your skin when you notice, and takes your hand from her waist to put it where hers has been.{/n}''',
    '''strips you with brisk, practised fingers and bends over you, her mouth moving down your throat to your chest. She smiles against your skin when you stop pretending to be unmoved, and takes your hand from her waist and holds it to her hip.{/n}''')

# Chivarro's cut after the farewell letter / service night.
span("{n}The farewell letter stays folded on the shelf.", "Not in this bed.\"",
     '''{n}The farewell letter stays folded on the shelf. Chivarro bends over you and kisses the next objection out of your mouth. After that there is the lamp's small circle of light, her unhurried breath, and a stretch of time in which she forgets to be quiet at all.{/n}
"No farewells yet. Not in this bed."''')

# The shared "Minagho cut" (Her mouth comes down on yours again...) and the shared "watch passes" cut.
_MINAGHO_CUT = ("{n}Her mouth comes down on yours again, and she does not let you answer. After that there is "
                "her breath hot in your ear, her claws raking your ribs, and a sound she makes that she will "
                "pretend, in the morning, was a laugh.{/n}")
sub("{n}Her mouth comes down on yours again, and she does not let you answer.{/n}", _MINAGHO_CUT)
sub("takes up the kiss exactly where she left it.{/n}",
    "takes up the kiss exactly where she left it, and for a long while neither of you is any good at being quiet.{/n}")

# ======================================================================================
# MINAGHO / CHIVARRO: the pair (throuple) thresholds and cuts
# ======================================================================================
sub('''"Mine first," {n}Minagho says, and swings a leg across you, bare and hot against your hip.{/n}''',
    '''"Mine first," {n}Minagho says, and pushes you down onto the mattress with a palm flat on your breastbone, her bare shoulder hot against your arm.{/n}''')
sub('''"Mine first," {n}Minagho says, and throws a leg over you, bare against your hip.{/n}''',
    '''"Mine first," {n}Minagho says, and pushes you down onto the mattress with a palm flat on your breastbone.{/n}''')
sub('''{n}Minagho bites Chivarro's lip, and Chivarro takes your hand and puts it on the pair of them.{/n}''',
    '''{n}Minagho bites Chivarro's lip, and Chivarro takes your hand and lays it against the two of them, skin on skin. After that there is the crooked lamp, the huge shadows on the ceiling, and three people breathing out of rhythm, one of them swearing inventively.{/n}''')
sub('''{n}The letter catches in the grate and curls. Neither of them looks at it.{/n}''',
    '''{n}The letter catches in the grate and curls. Neither of them looks at it. There is a long stretch of hands and mouths and low argument over who gets what, and Chivarro, at the last, is the loudest of the three.{/n}''')

# When it scars: the pair's night.
sub('''and then she is astride you, bare and hot against your stomach, and Chivarro's mouth is on yours, tasting of wine, one hand pressed flat to your chest.{/n}''',
    '''and then her bare skin is hot against your side and Chivarro's mouth is on yours, tasting of wine, one hand pressed flat to your chest.{/n}''')
sub('''She takes your wrist and puts it between her thighs, and Chivarro's hand slides down your body to meet it.{/n}''',
    '''She takes your wrist and pulls your hand to her hip, and Chivarro lays her own over it, claiming the rest.{/n}''')
sub('''{n}In the dark Chivarro finds your burned hand and kisses the palm, and Minagho laughs low against her shoulder.{/n}''',
    '''{n}In the dark Chivarro finds your burned hand and kisses the palm, and Minagho laughs low against her shoulder. Then it is all breath and skin and two women taking turns at being impatient, and the scarred hand is never free for long.{/n}''')

# Minagho alone: threshold (Minagho, spared Minagho).
span("{n}She pushes you onto the mattress and follows, hair spilling across your cheek.", "and catches your mouth again.{/n}",
     '''{n}She pushes you onto the mattress and follows, hair spilling across your cheek. The dress is gone; you did not see where. She pins your wrists above your head with one hand while the other drags down your chest to your waistband, and her mouth curls at what she feels there.{/n}
"Already. Good. Mine tonight, Golarian, and I intend to use every minute of it."
{n}She bears down on you, hot-skinned and unhurried, and catches your mouth again.{/n}''')

# Minagho by letter.
sub('''and climbs astride you with your wrists pinned in one of her hands.{/n}''',
    '''and follows you down with your wrists pinned in one of her hands.{/n}''')
sub('''and she grinds down against you, slick through the last of the cloth, her breath hissing between her teeth.{/n}''',
    '''and her bare skin is hot against yours, her breath hissing between her teeth.{/n}''')

# Minagho when it scars: night.
sub('''she has you against the wall with her knee between yours and your shirt in her fist''',
    '''she has you against the wall with her forearm across your chest and your shirt in her fist''')
sub('''and climbs astride you with the burned palm pressed flat over the dry brand on her own brow.''',
    '''and follows you down with the burned palm pressed flat over the dry brand on her own brow.''')
sub('''and her bare thighs clamp your hips. Slowly she lets your wrist go and puts your hand low on her hip, and grinds against you once, hard, until her breath catches on a sound she will deny later.{/n}''',
    '''and her bare skin is hot against yours. Slowly she lets your wrist go and puts your hand on her hip, and kisses you hard enough that her breath catches on a sound she will deny later.{/n}''')

# Chivarro alone: threshold and threshold_clean (both spellings).
for _sp in ("practiced", "practised"):
    sub("climbs astride you in one %s motion, and leans down" % _sp,
        "follows in one %s motion, and leans down" % _sp)
sub('''One hand takes yours and guides it up her thigh to the heat she has kept from every guest; the other works your laces loose without looking.''',
    '''One hand takes yours and sets it at her waist; the other works your laces loose without looking.''')
sub('''{n}Chivarro catches your mouth before you can speak and closes her fingers in your open collar.{/n}''',
    '''{n}Chivarro catches your mouth before you can speak and closes her fingers in your open collar. The chair against the door creaks, the lamp gutters, and for once she does not price a single sound.{/n}''')

# Chivarro by letter.
sub('''When she kneels over you her skin is warm and her hair brushes your chest, and her fingers are already between your hips and hers, guiding.{/n}''',
    '''When she bends over you her skin is warm and her hair brushes your chest, and her fingers are already at the fastening of your breeches.{/n}''')
sub('''{n}Chivarro sets the signed lease beyond the candle and kisses you hard enough to stop the next question.{/n}''',
    '''{n}Chivarro sets the signed lease beyond the candle and kisses you hard enough to stop the next question. The candle gutters; her hair falls over both your faces, and for a while the only account she keeps is of your breathing.{/n}''')

# Chivarro when it scars: night and cut.
sub('''She strips your shirt away, unfastens you with two fingers, and her mouth finds the hollow of your throat, your chest, the line of your stomach, in no hurry at all. When she lifts her head her lips are wet, and her mouth is daring you to complain.{/n}''',
    '''She strips your shirt away, and her mouth finds the hollow of your throat, your chest, the scarred hand, in no hurry at all. When she lifts her head her lips are dark from kissing, and her mouth is daring you to complain.{/n}''')
sub('''{n}Chivarro sweeps the coins to the floor with one arm and keeps your hands exactly where she put them.{/n}''',
    '''{n}Chivarro sweeps the coins to the floor with one arm and keeps your hands exactly where she put them. The scar throbs under her mouth, and the lamp, the rent and the room go with it.{/n}''')

# Epilogue commit (Minagho/Chivarro).
sub('''climbed astride, and pinned the Commander's wrists to the pillow above. ''',
    '''followed, and pinned the Commander's wrists to the pillow above. ''')
sub('''Her bare thighs tighten at their hips; she leans down until her loosened hair brushes their throat.{/n}''',
    '''Her loosened hair falls round both their faces, and the room, the debt and the long year of waiting go quiet.{/n}''')
sub('''{n}On the mattress she catches the Commander against her bare body. Her hand closes at their hip; the next kiss stops their reply.{/n}''',
    '''{n}On the mattress she catches the Commander against her bare body, and the next kiss stops their reply. The letter, the lock and Minagho's name are all somewhere outside the door.{/n}''')
sub('''She stifles another laugh against their mouth and pulls them between her knees.{/n}''',
    '''She stifles another laugh against their mouth, and the rest of the night is the two of you trying to be quiet and failing.{/n}''')

# ======================================================================================
# MINACHIV base route
# ======================================================================================
sub('''{n}Minagho bites your lower lip, then your throat, and drops the game stone beyond the couch without looking where it falls.{/n}''',
    '''{n}Minagho bites your lower lip, then your throat, and drops the game stone beyond the couch without looking where it falls. The lamp throws her shadow huge up the wall and then the shadows run together: her hot breath, her claws at your shoulders, the couch complaining under both of you. You lose the stone and the hour with it.{/n}''')
sub('''{n}Her dress is round her hips, and then it is gone. She drags your belt open, sinks her teeth into your shoulder and grinds against you, bare and hot and wet, until you hear her breath break.{/n}
"One hour, Golarian. Hands. All of them."''',
    '''{n}Her fingers close on your belt, and her dress is round her hips, and then it is gone. She sinks her teeth into your shoulder, bare against your hands, until you hear her breath break.{/n}
"One hour, Golarian. She will be counting the minutes from the stair and hating every one. Hands. All of them."''')
sub('''{n}Her fingers close on your belt.{/n}

{n}A step sounds on the stair.''', '''{n}A step sounds on the stair.''')
sub('''{n}She peels the bodice off, takes your hand and lays it over her breast, then guides the other lower, to the heat under her skirts, and shows you exactly how slowly she wants it. She is bare to the waist and breathing like a woman who has stopped counting.{/n}''',
    '''{n}She peels the bodice off, bare to the waist, takes your hand and lays it over her breast, and shows you exactly how slowly she wants it. She breathes like a woman who has stopped counting.{/n}''')
sub('''{n}Chivarro shoves the empty game tray off the couch with her foot and draws you down to her, impatient breath against your mouth.{/n}''',
    '''{n}Chivarro shoves the empty game tray off the couch with her foot and draws you down to her, impatient breath against your mouth. After that there is only skin, lamplight and her low laugh when your hands find her hips, and the stair forgotten.{/n}''')
sub('''Minagho's knee goes between yours; Chivarro's hand finds the buckle at your waist''',
    '''Minagho's mouth is at your ear; Chivarro's hand finds the buckle at your waist''')
sub('''{n}Chivarro catches Minagho in a kiss before she can boast about the last game, and Minagho reaches back for you without letting her go.{/n}''',
    '''{n}Chivarro catches Minagho in a kiss before she can boast about the last game, and Minagho reaches back for you without letting her go. After that the lamp, the tray and the argument over who won are forgotten; there are two pairs of hands, two mouths, and nobody at all keeping score.{/n}''')

sub('''drags your hand down over her hip and thigh, slowly''', '''drags your hand down over her hip, slowly''')
sub('''"I am wet already, darling. Do not tell me the rain is more interesting."''',
    '''"Every nerve I own is awake, darling, and you are the only thing in reach. Do not tell me the rain is more interesting."''')
sub('''{n}Minagho kicks the door shut with one hoof and shoves you back against it, still laughing, the street's grit on her hands.{/n}''',
    '''{n}Minagho kicks the door shut with one hoof and shoves you back against it, still laughing, the street's grit on her hands. She takes your mouth the way she took the street, and the rest goes the way a night goes when she has decided on it: the stair, the bed, her claws, your name said like an insult and then not like one.{/n}''')

sub('''Then she pushes you down, climbs over you, and finds your laces faster than you can find hers.{/n}''',
    '''Then she pushes you down and finds your laces faster than you can find hers.{/n}''')
sub('''{n}Her thighs settle either side of your hips, bare and warm in the red light. She does not hurry. She unlaces you, pushes the cloth aside and lets you feel her heat against you, only that, only the promise of it, her hair swinging across your face.{/n}''',
    '''{n}She does not hurry. She unlaces you, pushes the cloth aside, and leans down over you, bare and warm in the red light, her hair swinging across your face.{/n}''')
sub('''{n}Chivarro pins your wrists to the pillow and takes her time, head tilted, listening to her house through the floor as if it were applause.{/n}''',
    '''{n}Chivarro pins your wrists to the pillow and takes her time, head tilted, listening to her house through the floor as if it were applause. The bed knocks once against the wall; she smiles at the sound and does nothing whatever to stop it.{/n}''')

sub('''She pushes you down and straddles you, bare, one knee either side, and drags your shirt up over your head, and bends until her mouth is at your ear.{/n}''',
    '''She pushes you down onto it and drags your shirt up over your head, bare in the lamplight, and bends until her mouth is at your ear.{/n}''')
sub('''{n}Chivarro settles her weight on you and does not hurry.{/n}''',
    '''{n}Chivarro bends to your mouth and does not hurry; the lamp, the ledger and the coins on the pillow all stop mattering at once.{/n}''')

# ======================================================================================
# JERRIBETH
# ======================================================================================
sub('''the cold carapace of her thighs, the rasp''', '''the cold of her carapace, the rasp''')
sub('''{n}She pushes you back into a pillow that does not exist, settles her weight over you, pins your wrists where you offered them, and lowers herself onto you.{/n}''',
    '''{n}She pushes you back into a pillow that does not exist, bends over you, pins your wrists where you offered them, and the buzzing closes over your skin like a hand.{/n}''')
sub('''{n}The imagined lamp goes out. Her voice stays inside the room she has made until the real dawn reaches your shutters.{/n}''',
    '''{n}The imagined lamp goes out. The buzzing climbs through your skin until you cannot tell her pleasure from your own, and her voice stays inside the room she has made, quiet and satisfied, until the real dawn reaches your shutters.{/n}''')
sub('''{n}She lowers herself onto you with a sound in your skull like pages turning very fast.{/n}''',
    '''{n}She pulls you down against the cold ridge of her with a sound in your skull like pages turning very fast.{/n}''')
sub('''{n}She lets you draw her closer. Outside the imagining, the frame lies dark beside your untouched pillow.{/n}''',
    '''{n}She lets you draw her closer, and the sound in your skull climbs and breaks like a held note. Outside the imagining, the frame lies dark beside your untouched pillow.{/n}''')

sub('''{n}The candles behind her go out. Her voice stays close in the dark, telling you exactly what to do with your hands, and neither of you lights them again.{/n}''',
    '''{n}The candles behind her go out. Her voice stays close in the dark, telling you exactly what to do with your hands, and neither of you lights them again. The glass warms under your palms and fogs with your breath, and she does not stop counting the sounds you make until she has every one of them right.{/n}''')
sub('''{n}She lets the city repeat itself behind her. For once, she has found something she wants more than an audience for her work.{/n}''',
    '''{n}She lets the city repeat itself behind her. Her claw stays at the fastening of your collar, and for once she has found something she wants more than an audience for her work.{/n}''')
sub('''She straddles the chair, wings half open to shut out the shelves, and her hips settle onto yours with a slow, deliberate pressure that is already, undeniably, wet.{/n}''',
    '''She bends over the chair, wings half open to shut out the shelves, and her cool weight leans into you with a slow, deliberate pressure, her breath not quite as even as she would like it to be.{/n}''')
sub('''{n}The lamp burns down. She keeps you exactly where she put you, and you hold still for her, for a very long time.{/n}''',
    '''{n}The lamp burns down. She keeps you exactly where she put you, and you hold still for her, for a very long time: her claws on your skin, the buzzing in your teeth, and at the last a sound out of her that is not clinical in the least.{/n}''')

sub('''She settles over you with her weight on her elbows and her wings half open, shutting out the lamp.''',
    '''She bends over you with her weight on her elbows and her wings half open, shutting out the lamp.''')
sub('''against your ear, and lowers herself onto you.{/n}''', '''against your ear, and the cool length of her settles against you.{/n}''')
sub('''{n}Her wings shut out the lamp. Her voice is against your ear now, and the next watch passes without another knock.{/n}''',
    '''{n}Her wings shut out the lamp. The buzzing is in your skin, then in your breath, then in every part of you that has ever held still for her, and her voice is against your ear until the next watch passes without another knock.{/n}''')
sub('''and shut out the lamp, and the sound you have only ever heard in your skull is in your skin now, everywhere she touches, and she lowers herself onto you.{/n}''',
    '''and shut out the lamp, and the sound you have only ever heard in your skull is in your skin now, everywhere she touches, and she draws you down into the dark under them.{/n}''')
sub('''{n}The sliver of chitin stays in your hand. She laughs against your throat, and her folded wings hide the lamp.{/n}''',
    '''{n}The sliver of chitin stays in your hand. She laughs against your throat, the sound running through you like a struck string, and her folded wings hide the lamp.{/n}''')

sub('''wings half open to shut out the window, settled astride, and lowered herself onto the Commander, buzzing low enough to be felt in the teeth.{/n}''',
    '''wings half open to shut out the window, her cool weight bearing down, the buzzing low enough to be felt in the teeth.{/n}''')
sub('''settled astride with her wings opening over them both, and lowered herself onto the Commander with a sound in the skull like pages turning very fast.{/n}''',
    '''bent over the Commander with her wings opening over them both, and the sound in the skull went through every part of the Commander like pages turning very fast.{/n}''')
sub('''Behind the bedroom door her wings scraped once against the frame, and the household found reasons to be elsewhere until noon.{/n}''',
    '''Behind the bedroom door her wings scraped once against the frame, the buzzing rose until the window glass sang with it, and the household found reasons to be elsewhere until noon.{/n}''')
sub('''{n}The room she made closed around them both. The real breakfast table stood empty until noon.{/n}''',
    '''{n}The room she made closed around them both, and she was thorough in it: every nerve the Commander had, in the order she had catalogued them. The real breakfast table stood empty until noon.{/n}''')

# ======================================================================================
# HOUSEHOLD PAIRS
# ======================================================================================
sub('''and neither of them is pretending the contest is anything but this.{/n}''',
    '''and neither of them is pretending the contest is anything but this.{/n}
"Upstairs," {n}Wenduag says against her ear.{/n} "I want to hear whether you pray when you lose."''')
sub('''{n}The bout continues upstairs. Below them, you keep their watch.''',
    '''{n}The bout continues upstairs. Through the boards you hear a thump, a short laugh, Seelah swearing in a voice no priest of Iomedae taught her, and Wenduag's growl answering it. Below them, you keep their watch.''')

sub('''{n}The lower-town map stays open while they take their argument elsewhere.{/n}''',
    '''{n}The lower-town map stays open on the table while they take their argument elsewhere. Through the door come seven minutes of it: a growl, a laugh in two voices, something heavy knocked against a wall, and Wenduag, hoarse, asking if that is all the Abyss taught her.{/n}''')

sub('''Her hands are all over the mortal's body, hungry, reverent, unashamed: ribs, hips, the long muscle of the thigh. Camellia hoists her up onto the bench by the backs of her knees and stands between them, breathing hard, bare to the waist, her expression the one she wears over a good kill.''',
    '''Her hands are all over the mortal's body, hungry, reverent, unashamed: ribs, waist, hips. Camellia backs her against the bench and holds her there, breathing hard, bare to the waist, her expression the one she wears over a good kill.''')
sub('''{n}Their shadows move across the workbench in the lamplight.{/n}''',
    '''{n}Their shadows move across the workbench in the lamplight, and the vials on the rack chime every time a wing strikes them. Camellia's laugh breaks off once into something she will not admit to, and Arueshalae's answering gasp is not at all innocent.{/n}''')

sub('''{n}Arueshalae draws Nenio close and kisses her. Nenio catches the loosened collar in her fingers; Arueshalae presses into her hands. They leave the observation unfinished and climb the stairs together.{/n}''',
    '''{n}Arueshalae draws Nenio close and kisses her. Nenio catches the loosened collar in her fingers; Arueshalae presses into her hands.{/n}
"This is not for procreation," {n}Nenio says against her mouth.{/n} "It is for pleasure. I shall compare the data afterward."
"Take your notes with your hands," {n}Arueshalae murmurs.{/n}
{n}They leave the observation unfinished and climb the stairs together.{/n}''')
sub('''Nenio catches the loosened collar in her fingers; Arueshalae presses into her hands. They leave the bench for the room above, with seven minutes before the ward expires.{/n}''',
    '''Nenio catches the loosened collar in her fingers; Arueshalae presses into her hands.{/n}
"This is not for procreation," {n}Nenio says against her mouth.{/n} "It is for pleasure. I shall compare the data afterward."
"Take your notes with your hands," {n}Arueshalae murmurs.{/n}
{n}They leave the bench for the room above, with seven minutes before the ward expires.{/n}''')
sub('''{n}The chronometer stays in its case downstairs.{/n}''',
    '''{n}The chronometer stays in its case downstairs. Overhead a stair creaks and a door shuts; a while later Nenio's voice carries down, high and astonished, remarking that this was not in the literature.{/n}''')


# ======================================================================================
def _fields(scene):
    for node in scene["Nodes"]:
        yield node, "Text"
        for para in node.get("Paragraphs", []):
            yield para, "Text"


def integrate(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    hits = [0] * len(SUBS)
    span_hits = [0] * len(SPANS)
    for sid in SCENES:
        if sid not in scenes:
            raise KeyError("heat cal b: scene %s not found" % sid)
        for holder, key in _fields(scenes[sid]):
            text = holder[key]
            for i, (start, end, new) in enumerate(SPANS):
                a = text.find(start)
                if a < 0:
                    continue
                b = text.find(end, a)
                if b < 0:
                    continue
                text = text[:a] + new + text[b + len(end):]
                span_hits[i] += 1
            for i, (old, new) in enumerate(SUBS):
                if old in text:
                    text = text.replace(old, new)
                    hits[i] += 1
            holder[key] = text
    partial = __import__("os").environ.get("RRT_PARTIAL_BUILD") == "1"  # harem-less test build (A109)
    for i, n in enumerate(hits):
        if not n and not partial:
            raise ValueError("heat cal b: fragment drifted (%r)" % SUBS[i][0][:60])
    for i, n in enumerate(span_hits):
        if not n and not partial:
            raise ValueError("heat cal b: span drifted (%r)" % SPANS[i][0][:60])
    for sid in SCENES:
        for holder, key in _fields(scenes[sid]):
            if "[PROSE PENDING" in holder[key]:
                raise ValueError("heat cal b: prose pending at %s" % sid)

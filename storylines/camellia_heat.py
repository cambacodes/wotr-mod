"""Camellia: heat pass (HEAT, Directive 12). Build-up text only, applied last (expansion._make_expansion).

Her slots all cut before the act. The build-up nodes now carry her appetite to the start of it, in her register: the
drawing-room polish that cracks into the hoarse low voice, the false prudery that is a tell (lip-licking, flush,
quick breath), the knife as part of the play and never put away, frank-but-never-crude bed talk. Murderous values
untouched: nothing here regrets, excuses or cures. Slot nodes and exits stay as they are; the act is the later fill.
"""
from storylines.heat_text import extend

B = "camellia.trickster."
VARIANTS = ("", "_alive", "_camp")


def _each(scene, node):
    return [(B + scene + v, node) for v in VARIANTS]


def integrate(payload):
    extend(payload, _each("bond.not_today", "night"),
           "Her cold fingers warm against your neck as she draws you toward the bed.{/n}", '''
{n}She makes you wait at the foot of it. Her mouth is hungry and exact; it leaves yours for your throat and stays there, and you feel her tongue pass over her own lip as she works, the old tell, a woman tasting what she has decided not to spill. She undoes your shirt with the same fingers that hold the knife, one fastening at a time, and draws it off your shoulders. Her pulse is going in her throat so fast that she cannot keep the polish in her voice.{/n}
"Pardon me, my friend, if I am uncivil." {n}It comes out hoarse, the gravel under the drawing room.{/n} "I have thought about this for a very long time, and I have spent all of it not killing you."
{n}Her bodice she opens herself, unhurried, watching your face, and lets it go; the shift beneath is damp where it clings. She backs you onto the bed and straddles you, bare to the waist, flushed from throat to breastbone, and takes your hands and puts them on her, one at her breast, one low on her hip, and holds them there, hard, as if to pin down a promise.{/n}
"Not today," {n}she says, and rocks her hips once against yours, and her eyes half close.{/n} "Today is for the other appetite."''')

    extend(payload, _each("cards.the_deck_again", "silk"),
           '"Don\'t ever tell me whether you did."', '''
{n}The black silk is cool under your back and she is hot everywhere she touches. She finishes the work of the buttons with her mouth instead of the point, trails it down your breastbone, and makes a small, greedy sound when your hands find the laces of her bodice. This time she helps. The cards are crushed under her knees and she does not care. The bodice parts, she drags her shift over her head and throws it across the room, and she kneels over you in the candlelight, bare and flushed and shaking with suppressed laughter, one hand braced on your chest to keep you down.{/n}
"You have cards up your sleeves, and so have I." {n}She guides your palm up her ribs until it covers her breast, and her head drops back.{/n} "Oh, that is good. Do that again. And again."
{n}Her other hand sweeps down between you and tugs at the last of your clothes, impatient, until there is nothing left between her and you. She rides out one long breath, hips rolling slow and wet against you, the blade within her reach and not yours, her eyes locked on yours, daring you to lie to her face.{/n}''')

    extend(payload, _each("cards.two_lies_again", "all"),
           "She drops the knife from the pillow and draws you down into a kiss.{/n}", '''
{n}It is a long kiss, a slow one, the kind she gives when she is spending something. By the time she lets you up her nightgown has vanished and her hair is wild across the pillow, and she lies back and looks up at you with those cool eyes gone black and glittering.{/n}
"Say the first one now," {n}she whispers, and pulls your hand down her belly, between her thighs. She is wet and burning there, and she watches your face while you find out.{/n} "Say it while you touch me. I want to hear whether the voice cracks."''')

    extend(payload, _each("cards.two_lies_again", "mine"),
           '"And the rest? Show me."', '''
{n}You show her. The laces give, the shift slithers to her waist and she arches into your hands with a long, shaken breath. Her skin is hot and fine as porcelain, her heart tripping under your palm, and when she takes your wrist and slides your hand down over her stomach, lower, her thighs open for it without a word.{/n}
"Your heart says you are afraid. Your hands say otherwise." {n}Her voice has lost its polish.{/n} "I like it when they disagree."''')

    extend(payload, _each("day.the_second_dance", "strap"),
           '"Mind the edge. I have further use for those fingers."', '''
{n}Her skirt rides up around your wrist as the strap falls away, and there is nothing under it, nothing at all but warm skin and the pale marks the leather has left. Of course there isn't. She watches you discover it with a prim little smile that does not reach her breathing.{/n}
"A lady dresses for the occasion," {n}she says, and takes the knife from you, and lays it on the boards, and puts your hand back where it was, flat on the bare inside of her thigh.{/n} "Go on. Higher. You have my full permission."
{n}Her own hands are not idle. She has your shirt up and half off, her nails dragging down your side, and she presses her whole body against you until her breath stutters, moving against your hand as the candles circle the walls.{/n}''')

    extend(payload, _each("day.the_second_dance", "leave"),
           '"Nobody has ever wanted me with the knife. They always want me to take it off first. As if that made any difference."', '''
{n}She takes your mouth before you can answer, hard, and the hilt grinds between you as she walks you backwards into the candlelight. Her fingers are at your buckles, then your shirt, then the bare skin beneath, and when your hand slides up her thigh to find the sheathed knife and, above it, nothing but heat, she bites your lip and laughs, shocked and wholly delighted, against your teeth.{/n}
"Yes," {n}she hisses.{/n} "Exactly so. Leave it. I want to feel it against me while you do."''')

    extend(payload, [(B + "bond.witness", "hers")],
           "and she does not look at you once until the dessert, and then she does not stop.{/n}", '''
{n}The dress is the colour of dark wine, cut to come off in one pull, and she is charming to everyone in it. She makes the table weep with laughter over a cousin's wedding, and not once through the soup or the fish does she look at you, though under the cloth her ankle finds yours and rests there, warm and deliberate. At the dessert she looks up. Her tongue passes slowly over her lower lip. Her colour is as high as it was on the steps in the rain, her breath has the same short, quick edge, and her foot slides up the inside of your calf while she tells the table a perfectly ordinary joke.{/n}
"You are very quiet tonight, my friend," {n}she says across the candles, in the voice that is not hers, and under it, low enough that only you can hear, the other one, the gravel.{/n} "I think you are thinking about the steps. Don't stop."''')

    extend(payload, [(B + "evening.the_prisoner", "watch")],
           '"Still watching?"', '''
{n}Her cheeks are flushed. In the cold of the cell her breath smokes, short and quick, and her tongue passes over her lips; the half-smile is a different thing than it was a minute ago. She comes across the flagstones with the clean little knife still in her fingers and stops with her face a hand's breadth from yours. The cell stinks of iron and wet stone and her lilies, and behind her the chains tick once against the wall and are still.{/n}
"You did not look at him," {n}she says. Her voice has gone low and rough, the gravel under the drawing room.{/n} "Not once. You watched me. Do you know what that does to a woman, to be watched like that?" {n}The flat of the blade comes up and rests against your collarbone, cool, then slides slowly down. Her free hand takes your wrist and presses it to her throat, where her pulse is hammering.{/n} "Feel that. That is you."''')

    extend(payload, _each("returned.test", "threshold"),
           '"Beat," {n}she whispers against your mouth.{/n} "Beat. Beat."', '''
{n}You count with her. Then she is done counting. She tears the last knot of her laces out herself and shoves the dress down to her hips, and the lamp finds the white skin, the old fine scars, her breasts rising and falling with every breath, and she lets you look for exactly as long as she chooses. Her hands go to your belt, to the buckles under it, with a thief's quick economy. She strips you, takes what she finds in a firm, appraising grip that makes your breath catch, and watches your face while she does it, lips parted, the tip of her tongue just visible.{/n}
"Still beating," {n}she whispers, hoarse, and the polish is entirely gone.{/n} "Mine is going to burst out of my chest. Tell me I am not the only one."''')

"""Arueshalae: heat pass (HEAT, Directive 12). Build-up text only, applied last (expansion._make_expansion).

Her five slots cut at the first undressing or on a fade ("And the city goes."). The build-up now carries her to the
start of the act in her register: an experienced succubus who leads, whose hunger is in images (taste, warmth, the
edge of a pulse), who counts minutes because the ward is all that keeps her touch from draining. The redeemed
bell-tower night keeps its ward and its cloak; the fallen roof keeps its cruelty and its hostess's mockery. Slot nodes
and exits stay as they are; the act is the later fill. The harem pair rows are not touched here.
"""
from storylines.heat_text import extend, swap


def integrate(payload):
    # Treatment night (redeemed): shared by the ward-limited slot and the released one.
    extend(payload, [("arueshalae.treatment.night", "undress")],
           '"Look at me. Here. With you."', '''
{n}She peels the rest of her own clothes away without ceremony, with the old expertise of a woman who once did this to ruin people, and lets you see her under the stars, bare and unhurried, her wings half unfurled behind her like a canopy. She watches your face take her in. The corner of her mouth lifts, hungry and a little frightening. Then she strips you to the skin with those quick, certain hands, and the wind off the Worldwound raises gooseflesh along your arms until her wings come round to cover it.{/n}
"Hold still." {n}Her palms slide down your chest, over the flat of your stomach, and she takes her time with the rest, discovering you the way she once discovered a mark, with her fingertips and her eyes, and finding you ready. A low, shaky laugh escapes her.{/n} "Oh. You want me too. Good. Say it with your hands."
{n}She guides one of them between her own thighs, to where she is slick and hot and open, pins it there with hers and rolls against your palm with a throaty sound. Then she climbs over you, settling her weight across your hips on the spread cloak, one hand braced beside your head, the other sliding down between you, and stops there with her mouth an inch above yours and her whole body trembling on the edge.{/n}''')

    # The roof (fallen): one text shared by the three scenes that reach `cut`.
    swap(payload, [("arueshalae.trickster.evil.window", "cut"), ("arueshalae.trickster.evil.window_yard", "cut"),
                   ("arueshalae.trickster.fallen.roof", "cut")],
         '''and bends down until her mouth is against your throat. "Now," she says against it. "Don't you dare lose count." And the city goes.{/n}''',
         '''and bends down until her mouth is against your throat.{/n}
{n}Her teeth close on the tendon there, just short of drawing blood, and a shudder goes through her that you feel in your own bones. Her hands strip you with a courtier's contempt for buttons; the rain drums on your bare skin and then her mouth is on it, going down, hot against the cold, taking her time, her wings spread over you both like a tent against the rain. She comes up with her lips wet and her eyes black with appetite, takes your hand and puts it between her thighs, where the rain is not the only thing running, and rocks against it, slowly, making you feel every inch of how hungry she is.{/n}
"You've no idea," {n}she says, in the sweet, mocking hostess's voice,{/n} "how long it has been since I took something that wanted to be taken. Now. Don't you dare lose count." {n}She rises on her knees above you, her whole body poised on the edge of it, the gargoyles grinning over her shoulder, and waits for you to beg.{/n}''')

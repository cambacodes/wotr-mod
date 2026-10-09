"""Anevia: heat pass (HEAT, Directive 12). Build-up text only, applied last (expansion._make_expansion).

Each explicit slot of Anevia (and her two joint nights with Irabeth) ended its build-up at undressing or at a
"draws you down" beat. The build-up nodes now carry desire, situation and appetite in her voice (dry, impatient,
dropped g, practical hands, crude when she is rattled, culpable when she lies to Beth) to the start of the act and
stop there. The slot nodes and their exits are untouched; the act itself is the later fill.
"""
from storylines.heat_text import extend, swap

G = "anevia.trickster.gone."
KEY = "anevia.a_key_that_is_hers"


def integrate(payload):
    # a_crossing: first night, Drezen room, Beth has not agreed; the door left unbarred.
    extend(payload, [("a_crossing", "round2.buildup.night")],
           "Then she leans down, her hair falling around both your faces, and drags you up against her.{/n}", '''
{n}Bare, she is all scout: lean muscle, a pale seam down one thigh, a bruise going yellow over her ribs. She gives you one breath to look before she tows you out of the last of your clothes and tosses them after the scarf. She settles her weight on you and the heat of her lands on your hip, slick and unmistakable. She snorts at herself, caught out.{/n}
"Don't. Don't say it." {n}She catches your hand and drags it between her thighs, makes you feel exactly how wet she is, and holds it there. Her voice has gone rough.{/n} "That ain't Beth's doin'. That's all me, and I've been carryin' it round for weeks. Damn me for it."
{n}A boot scrapes in the corridor, a runner's, slowing at her unbarred door. Anevia freezes above you with her own fist against her mouth, eyes bright and wicked over her knuckles, and her hips do not stop: a slow, shameless roll that wrings a sound out of both of you. The footsteps drift on. She lets her breath out, half a laugh and half a moan, takes the fist from her mouth and rises on her knees, thighs shaking, palms flat on your chest, hovering over you.{/n}
"Eyes on me. No lyin'. Tell me you want it too."''')

    # a_key_that_is_hers: her leased room, honest share, Beth knows what a key means.
    extend(payload, [(KEY, "round2.buildup.night")],
           "climbs astride you with one knee braced against the frame, and pulls your hands to her hips.{/n}", '''
{n}She is warm from the stove and goosebumped where the draught finds her, and she does not bother with modesty. She rolls her hips once against yours, slowly, watches what it does to your face and does it again with a lazy, wicked grin.{/n}
"Been thinkin' about this since the lease. Before the lease, if I'm honest, which I'm not, usually." {n}She pulls your hand up over her breast, drags your thumb across her nipple and holds it there, and her breath stutters.{/n} "Beth knows where I am tonight. Beth knows what a key means. So I don't have to be sorry, and I ain't. Shut up and make it worth the rent."
{n}She drags the rest of your clothes down with her free hand and kicks them off the end of the bed. The old frame lets out a shriek you both freeze at, then both laugh at.{/n} "Landlady heard that," {n}she whispers, delighted.{/n} "Good. Let her." {n}She slides forward until she is flush against you, wet and hot and impatient, and plants her hands either side of your head, close enough that you feel every breath.{/n}
"I ain't goin' to be gentle about it. Don't ask me to."''')

    # Secret nights (Beth does not know): the same bolted-door beat in every history.
    secret = [(KEY, "round2.buildup.partner_secret_night")]
    for suffix in ("commit", "fetched_commit"):
        secret.append((G + suffix, "round2.buildup.partner_answer_1_secret_night"))
    for suffix in ("second_ask", "fetched_second_ask"):
        secret.append((G + suffix, "round2.buildup.partner_price_0_secret_night"))
    extend(payload, secret, "Her mouth finds your neck as she draws your hands to her bare waist.{/n}", '''
{n}The dress is a heap on the chair, and under it she wears nothing but her boots. She would rather kick them off later than waste the time, and tells you so between kisses. Her teeth catch your earlobe while she gets on with your belt, quick and practical, swearing when it fights her.{/n}
"Beth thinks I'm at the north post." {n}She says it flat against your ear, because she will not dress it up.{/n} "I am. After. Don't talk to me about after."
{n}She hauls the last of your clothes away, one boot thumps across the floor, then the other, and she climbs astride you on the mattress, bare and flushed from throat to belly. She grinds down against your thigh, long and deliberate, leaving a wet stripe behind and a sound she tries to bite back, then buries both hands in your hair and pulls your mouth to her breast.{/n}
"Quiet," {n}she breathes, laughing at herself, her hips already working above you.{/n} "I can't promise it for me."''')

    # Beth away: the ring stays on. First door: the letter she owes.
    extend(payload, [(KEY, "round2.buildup.partner_absent_night")],
           "her wedding ring cold against your bare chest.{/n}", '''
{n}She does not take the ring off. She lays that hand flat over your heart, ring and all, and looks you dead in the eye while the other drags her dress up and over her head.{/n}
"Leave it where it is." {n}Her voice is low and not quite steady.{/n} "I want to feel it. I want it to hurt a bit. It ought to."
{n}She is bare and weathered by the sun on the walls, hungry in a way she has stopped apologizing to herself for. She shoves your coat the rest of the way off, strips you with brisk, shaking hands and pushes you flat on the bed. The scout reports slide off the desk behind you and she does not look. She climbs over you, knees either side of your ribs, and the hand with the ring in it slides down your stomach, slowly, and stops just short while she watches your face and makes you wait.{/n}
"There," {n}she says, rough.{/n} "That's honest, at least."''')
    absent = []
    for suffix in ("commit", "fetched_commit"):
        absent.append((G + suffix, "round2.buildup.partner_answer_1_absent_night"))
    for suffix in ("second_ask", "fetched_second_ask"):
        absent.append((G + suffix, "round2.buildup.partner_price_0_absent_night"))
    extend(payload, absent, "She presses you against the bed, the ring on her hand bright in the lantern light.{/n}", '''
{n}Her dress is already open down the back. She shrugs out of it where she stands, and the lantern finds the long line of her: ribs, the flat hard belly of a woman who runs messages along the walls, the pale places the sun never reaches. She does not hurry and she does not hide. She works your shirt off over your head and your belt out of its loops, and when she has you bare she backs you the last step with a palm in the centre of your chest and tips you onto the mattress.{/n}
"Keep the lantern." {n}She climbs after you, straddling your thighs, and the ring on her hand is bright where it spreads over your hip.{/n} "I want to see me doin' it. I want to know I did it with my eyes open."
{n}Her other hand goes between her own legs. She shows you, with a challenging look, how ready she already is, then lifts her fingers to your mouth and lets you taste. Then she rises on her knees over you, one hand braced on the headboard, the ring bright against the wood, and hangs there, trembling, waiting for you to be the one who breaks.{/n}''')

    # the_evening_without_a_case: her chosen evening, no work in it.
    extend(payload, [("anevia.the_evening_without_a_case", "round2.buildup.night")],
           "her hand spreads flat between your shoulders and holds you there, exactly where she wants you.{/n}", '''
{n}Her mouth goes to your throat, unhurried now, the whole evening hers. The quick economy of her scout's hands is gone; she touches you as if she had all night and has decided to spend it, drags her nails down your back, bites softly at your shoulder, laughs when you shiver.{/n}
"Nobody's askin' me for a thing," {n}she murmurs.{/n} "No report. No runner. Just this." {n}She rolls you onto your back under that flat hand and sheds the last of her own clothes, kicking them off the bed without looking where they land. One glance, slow and warning, at the crooked goat still turned to the wall.{/n} "Don't you dare joke. I'll know."
{n}Then she is bare over you, her thighs closing either side of your hips, her hair a curtain round your faces, the wet heat of her sliding against you with every slow roll of her body. Her eyes are steady and a little wild, and they dare you to be the first to look away.{/n}
"There. Properly. Take your time, and I'll take mine."''')

    # Gatehouse: the real door, the cloak, the ring she takes off (it is on the cloak at dawn).
    extend(payload, [(G + suffix, "round2.buildup.threshold") for suffix in ("commit", "fetched_commit", "muster")],
           "half a laugh and half something she has not let herself say since the Coronation.{/n}", '''
{n}The cloak is rough wool and smells of woodsmoke and road. She stretches out on it and hauls you down on top of her, and the shirt you had left goes to rags under her hands, ripped, not unbuttoned. Her dress hikes to her hips and then it is over her head. She works her ring off her finger and drops it on the cloak by her head, deliberately, where she will be able to see it. The lantern on its hook throws her whole bare length gold against the stone: scarred knees, hard stomach, the rise and fall of her breasts.{/n}
"I'm not doin' this halfway." {n}Her heels lock behind your thighs and haul you in; her mouth is at your ear.{/n} "All the way up the road I've been rationin' this. I'm done rationin'. Get between my legs before I do it myself."
{n}She spreads under you, hot and open against your hip, one hand dragging yours down to where she is slick and aching, the other fisted in your hair.{/n}''')

    # The knock: "Probably", the filthiest word she knows.
    extend(payload, [(G + suffix, "round2.buildup.night") for suffix in ("second_ask", "fetched_second_ask")],
           "and pushes you back onto the bed and follows you down.{/n}", '''
{n}She finishes what she started with your shirt and throws it at the door. Her own clothes follow in four quick jerks, and she stands over you at the foot of the bed for a moment, bare and breathing hard, looking you over with a grim appraisal, like a scout counting a camp she means to take.{/n}
"All that thinkin'," {n}she says, and plants a knee on the mattress, then the other, and crawls up your body, her mouth dragging heat over your stomach, your ribs, your throat,{/n} "and it comes down to this. You, a bed, and me wet through before I'd crossed the yard."
{n}Her thighs bracket your hips. She takes your wrist and pins it above your head, sinks her weight onto you and grinds against you once, hard, and watches the sound it drags out of you. Her free hand goes down between her own legs, and she holds there, hovering, breathless.{/n}
"You asked twice. This is my answer."''')

    # Joint nights with Irabeth (the shared host node keeps its anchor and morning beat).
    swap(payload, [("three_open_road", "night")],
         "{n}Irabeth catches her wife's hand and kisses it, then turns toward you. The next kiss leaves very little room for conversation. Anevia rests against both of you, waiting for the moment when Irabeth reaches for her again.{/n}",
         '''{n}Irabeth catches her wife's hand and kisses it, then turns toward you. The next kiss leaves very little room for conversation. She kisses the way she does everything, with a strength held on a short leash, and the leash is slipping; her free hand fists in your shirt and does not ask. The coat parts under Anevia's careful fingers, then the shirt beneath it, and the firelight finds the old scars across Irabeth's ribs and the heavy rise of her breasts. Anevia, who has seen them every night for years, still stops to look, and then leans in and puts her mouth on the nearest.{/n}
{n}Irabeth's breath leaves her in a rush. She reaches back blindly for her wife, finds a hip and pulls, and Anevia comes with a delighted laugh, her own shirt gone over her head, her skin hot against Irabeth's back. Your hands go where theirs leave room: Irabeth's waist, the hard curve of her thigh, the wet heat Anevia has already coaxed there and now guides you toward, murmuring into her wife's ear all the things she means to see done. Your fingers find her slick and Irabeth's hips answer, and Anevia grins against her neck like a woman who has been planning this for a month.{/n}
{n}Anevia rests against both of you, waiting for the moment when Irabeth reaches for her again.{/n}''')
    swap(payload, [("three_rooms_unlocked", "night")],
         "Irabeth's are slower, and heavier, and she does not stop kissing you while they work. The bed gives one unmistakable complaint.{/n}",
         "Irabeth's are slower, and heavier, and she does not stop kissing you while they work. Between them you are stripped in the time it takes to lose an argument. Irabeth's palm flattens low on your stomach and stays, a warm, unhurried weight, while Anevia mouths along your shoulder and tells you in a rough whisper exactly what her wife does when she is ready. You feel Irabeth smile against your mouth. The bed gives one unmistakable complaint.{/n}")

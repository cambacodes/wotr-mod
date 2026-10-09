"""Anevia: heat pass (HEAT, Directive 12). Build-up text only, applied last (expansion._make_expansion).

Each explicit slot of Anevia (and her two joint nights with Irabeth) ended its build-up at undressing or at a
"draws you down" beat. The build-up nodes now carry desire, situation and appetite in her voice (dry, impatient,
dropped g, practical hands, crude when she is rattled, culpable when she lies to Beth) to the start of the act and
stop there. The slot nodes and their exits are untouched; the act itself is the later fill.
"""
from storylines.heat_text import extend, swap, _node


def retail(payload, targets, old_tail, new_tail):
    """Replace the exact tail of each target node's text (the node must end with `old_tail`)."""
    for scene_id, node_id in targets:
        node = _node(payload, scene_id, node_id)
        if node["Text"].count(old_tail) != 1 or not node["Text"].rstrip().endswith(old_tail):
            raise ValueError("heat layer: %s/%s does not end with %r" % (scene_id, node_id, old_tail[:70]))
        node["Text"] = node["Text"].rstrip()[:-len(old_tail)] + new_tail.strip()

G = "anevia.trickster.gone."
KEY = "anevia.a_key_that_is_hers"


def integrate(payload):
    # a_crossing: first night, Drezen room, Beth has not agreed; the door left unbarred.
    extend(payload, [("a_crossing", "round2.buildup.night")],
           "Then she leans down, her hair falling around both your faces, and drags you up against her.{/n}", '''
"Don't. Don't say it." {n}Her voice has gone rough; she has caught the look on your face and knows exactly what it says about the look on hers.{/n} "That ain't Beth's doin'. That's all me, and I've been carryin' it round for weeks. Damn me for it."
{n}A boot scrapes in the corridor, a runner's, slowing at her unbarred door. Anevia freezes above you with her own fist against her mouth, eyes bright and wicked over her knuckles. The footsteps drift on. She lets her breath out, half a laugh and half a groan, takes the fist from her mouth and hangs there over you, palms flat on your chest.{/n}
"Eyes on me. No lyin'. Tell me you want it too."''')

    # a_key_that_is_hers: her leased room, honest share, Beth knows what a key means.
    retail(payload, [(KEY, "round2.buildup.night")],
           "climbs astride you with one knee braced against the frame, and pulls your hands to her hips.{/n}", '''
follows with one knee braced against the frame, and pulls your hands to her hips.{/n}
{n}She is warm from the stove and goosebumped where the draught finds her, and she does not bother with modesty. She leans over you until her hair falls round both your faces and kisses you slowly, watching what it does to your expression, and does it again with a lazy, wicked grin.{/n}
"Been thinkin' about this since the lease. Before the lease, if I'm honest, which I'm not, usually." {n}She draws your hand up over her heart and holds it there, and her breath stutters.{/n} "Beth knows where I am tonight. Beth knows what a key means. So I don't have to be sorry, and I ain't. Shut up and make it worth the rent."
{n}She drags the rest of your clothes away with her free hand and kicks them off the end of the bed. The old frame lets out a shriek you both freeze at, then both laugh at.{/n} "Landlady heard that," {n}she whispers, delighted.{/n} "Good. Let her."
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
{n}She hauls the last of your clothes away, one boot thumps across the floor, then the other, and she pulls you down onto the mattress with her, bare and flushed from throat to waist. Her wedding ring is cold where her hand spreads on your chest, and she does not take it off. She puts your hand over her heart so you can feel it going.{/n}
"Quiet," {n}she breathes, laughing at herself.{/n} "I can't promise it for me. And if the watch comes knockin', I'm a dispatch."''')

    # Beth away: the ring stays on. First door: the letter she owes.
    extend(payload, [(KEY, "round2.buildup.partner_absent_night")],
           "her wedding ring cold against your bare chest.{/n}", '''
{n}She does not take the ring off. She lays that hand flat over your heart, ring and all, and looks you dead in the eye while the other drags her dress up and over her head.{/n}
"Leave it where it is." {n}Her voice is low and not quite steady.{/n} "I want to feel it. I want it to hurt a bit. It ought to."
{n}She is bare and weathered by the sun on the walls, hungry in a way she has stopped apologizing to herself for. She shoves your coat the rest of the way off, strips you with brisk, shaking hands and pushes you back onto the bed. The scout reports slide off the desk behind you and she does not look. The hand with the ring in it travels slowly over your ribs while she watches your face and makes you wait.{/n}
"There," {n}she says, rough.{/n} "That's honest, at least."''')
    absent = []
    for suffix in ("commit", "fetched_commit"):
        absent.append((G + suffix, "round2.buildup.partner_answer_1_absent_night"))
    for suffix in ("second_ask", "fetched_second_ask"):
        absent.append((G + suffix, "round2.buildup.partner_price_0_absent_night"))
    extend(payload, absent, "She presses you against the bed, the ring on her hand bright in the lantern light.{/n}", '''
{n}Her dress is already open down the back. She shrugs out of it where she stands, and the lantern finds the long line of her: ribs, the flat hard belly of a woman who runs messages along the walls, the pale places the sun never reaches. She does not hurry and she does not hide. She works your shirt off over your head and your belt out of its loops, and when she has you bare she backs you the last step with a palm in the centre of your chest and tips you onto the mattress.{/n}
"Keep the lantern." {n}She follows you down, and the ring on her hand is bright where it spreads over your hip.{/n} "I want to see me doin' it. I want to know I did it with my eyes open."
{n}She takes your face in both hands and looks at you a long moment, flushed and not quite steady, daring you to be the first to say what this is. Then she kisses you, hard, and the lantern burns on.{/n}''')

    # the_evening_without_a_case: her chosen evening, no work in it.
    retail(payload, [("anevia.the_evening_without_a_case", "round2.buildup.night")],
           "Her knee draws up along your hip; her hand spreads flat between your shoulders and holds you there, exactly where she wants you.{/n}", '''
Her hand spreads flat between your shoulders and holds you there, exactly where she wants you.{/n}
{n}Her mouth goes to your throat, unhurried now, the whole evening hers. The quick economy of her scout's hands is gone; she touches you as if she had all night and has decided to spend it, drags her nails down your back, bites softly at your shoulder, laughs when you shiver.{/n}
"Nobody's askin' me for a thing," {n}she murmurs.{/n} "No report. No runner. Just this." {n}She rolls you onto your back under that flat hand and sheds the last of her own clothes, kicking them off the bed without looking where they land. One glance, slow and warning, at the crooked goat still turned to the wall.{/n} "Don't you dare joke. I'll know."
{n}Then she is bare against you, her hair a curtain round your faces, her eyes steady and a little wild, and they dare you to be the first to look away.{/n}
"There. Properly. Take your time, and I'll take mine."''')

    # Gatehouse: the real door, the cloak, the ring she takes off (it is on the cloak at dawn).
    extend(payload, [(G + suffix, "round2.buildup.threshold") for suffix in ("commit", "fetched_commit", "muster")],
           "half a laugh and half something she has not let herself say since the Coronation.{/n}", '''
{n}The cloak is rough wool and smells of woodsmoke and road. She stretches out on it and hauls you down beside her, and the shirt you had left goes to rags under her hands, ripped, not unbuttoned. Her dress is over her head. She works her ring off her finger and drops it on the cloak by her head, deliberately, where she will be able to see it. The lantern on its hook throws her bare skin gold against the stone: scarred knees, hard stomach, the quick rise and fall of her breath.{/n}
"I'm not doin' this halfway." {n}Her hand fists in your hair; her mouth is at your ear.{/n} "All the way up the road I've been rationin' this. I'm done rationin'. Come here before I do somethin' stupid, like talk."
{n}She pulls you down into a kiss with nothing careful left in it.{/n}''')

    # The knock: "Probably", the filthiest word she knows.
    extend(payload, [(G + suffix, "round2.buildup.night") for suffix in ("second_ask", "fetched_second_ask")],
           "and pushes you back onto the bed and follows you down.{/n}", '''
{n}She finishes what she started with your shirt and throws it at the door. Her own clothes follow in four quick jerks, and she stands over you at the foot of the bed for a moment, bare and breathing hard, looking you over with a grim appraisal, like a scout counting a camp she means to take.{/n}
"All that thinkin'," {n}she says, and crawls up the bed after you, her mouth dragging heat along your ribs and your throat,{/n} "and it comes down to this. You, a bed, and me half out of my head before I'd crossed the yard."
{n}She takes your wrist and pins it above your head and kisses you once, hard, watching your face while she does it.{/n}
"You asked twice. This is my answer."''')

    # Joint nights with Irabeth (the shared host node keeps its anchor and morning beat).
    swap(payload, [("three_open_road", "night")],
         "{n}Irabeth catches her wife's hand and kisses it, then turns toward you. The next kiss leaves very little room for conversation. Anevia rests against both of you, waiting for the moment when Irabeth reaches for her again.{/n}",
         '''{n}Irabeth catches her wife's hand and kisses it, then turns toward you. The next kiss leaves very little room for conversation. She kisses the way she does everything, with a strength held on a short leash, and the leash is slipping; her free hand fists in your shirt and does not ask. The coat parts under Anevia's careful fingers, then the shirt beneath it, and the firelight finds the old scars across Irabeth's ribs and the heavy rise of her breasts. Anevia, who has seen them every night for years, still stops to look, and then leans in and puts her mouth on the nearest.{/n}
{n}Irabeth's breath leaves her in a rush. She reaches back blindly for her wife, finds a hip and pulls, and Anevia comes with a delighted laugh, her own shirt gone over her head, her skin hot against Irabeth's back. Your hands go where theirs leave room: Irabeth's waist, the hard curve of her hip, while Anevia murmurs into her wife's ear all the things she means to see done. Irabeth's breath breaks, and Anevia grins against her neck like a woman who has been planning this for a month.{/n}
{n}Anevia rests against both of you, waiting for the moment when Irabeth reaches for her again.{/n}''')
    swap(payload, [("three_rooms_unlocked", "night")],
         "Irabeth's are slower, and heavier, and she does not stop kissing you while they work. The bed gives one unmistakable complaint.{/n}",
         "Irabeth's are slower, and heavier, and she does not stop kissing you while they work. Between them you are stripped in the time it takes to lose an argument. Irabeth's palm spreads flat on your chest and stays, a warm, unhurried weight, while Anevia mouths along your shoulder and tells you in a rough whisper exactly what her wife does when she is ready. You feel Irabeth smile against your mouth. The bed gives one unmistakable complaint.{/n}")

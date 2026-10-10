"""Residual key-room secret-night replacement blocked by engine prose classification.

The other heat groups live in their owning builders. Keep this target late
until the cross-route reviewed-reference owner migrates its prose binding.
"""
from storylines.heat_text import extend, _node
from authoring.generation_errors import record

def retail(payload, targets, old_tail, new_tail):
    """Replace the exact tail of each target node's text (the node must end with `old_tail`)."""
    for scene_id, node_id in targets:
        node = _node(payload, scene_id, node_id)
        if node is None:
            continue
        if node["Text"].count(old_tail) != 1 or not node["Text"].rstrip().endswith(old_tail):
            record("heat.retail_tail", scene=scene_id, node=node_id, detail=old_tail[:70])
            continue
        node["Text"] = node["Text"].rstrip()[:-len(old_tail)] + new_tail.strip()

KEY = "anevia.a_key_that_is_hers"

def integrate(payload):
    extend(payload, [(KEY, "round2.buildup.partner_secret_night")], "Her mouth finds your neck as she draws your hands to her bare waist.{/n}", '''
{n}The dress is a heap on the chair, and under it she wears nothing but her boots. She would rather kick them off later than waste the time, and tells you so between kisses. Her teeth catch your earlobe while she gets on with your belt, quick and practical, swearing when it fights her.{/n}
"Beth thinks I'm at the north post." {n}She says it flat against your ear, because she will not dress it up.{/n} "I am. After. Don't talk to me about after."
{n}She hauls the last of your clothes away, one boot thumps across the floor, then the other, and she pulls you down onto the mattress with her, bare and flushed from throat to waist. Her wedding ring is cold where her hand spreads on your chest, and she does not take it off. She puts your hand over her heart so you can feel it going.{/n}
"Quiet," {n}she breathes, laughing at herself.{/n} "I can't promise it for me. And if the watch comes knockin', I'm a dispatch."''')

    retail(payload, [(KEY, "round2.buildup.night")],
           "climbs astride you with one knee braced against the frame, and pulls your hands to her hips.{/n}", '''
follows with one knee braced against the frame, and pulls your hands to her hips.{/n}
{n}She is warm from the stove and goosebumped where the draught finds her, and she does not bother with modesty. She leans over you until her hair falls round both your faces and kisses you slowly, watching what it does to your expression, and does it again with a lazy, wicked grin.{/n}
"Been thinkin' about this since the lease. Before the lease, if I'm honest, which I'm not, usually." {n}She draws your hand up over her heart and holds it there, and her breath stutters.{/n} "Beth knows where I am tonight. Beth knows what a key means. So I don't have to be sorry, and I ain't. Shut up and make it worth the rent."
{n}She drags the rest of your clothes away with her free hand and kicks them off the end of the bed. The old frame lets out a shriek you both freeze at, then both laugh at.{/n} "Landlady heard that," {n}she whispers, delighted.{/n} "Good. Let her."
"I ain't goin' to be gentle about it. Don't ask me to."''')

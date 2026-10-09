"""Chadali: heat pass (HEAT, Directive 12). Build-up text only, applied last (expansion._make_expansion).

The honey/look and sessions/stay extensions end at the canon cut: fabric, hands, mouth,
appetite, no exposed anatomy before the reservation nodes, whose exits and aftermath keep
their saved structure.
"""
from storylines.heat_text import extend, paragraph


def integrate(payload):
    extend(payload, [("chadali.fortunes.honey", "look")],
           '"Lucky me," {n}she whispers, and she does not mean it as a joke.{/n}',
           '''{n}Her fingers close over your hand where it rests at her hip and carry it, slowly, up over the silk to her breast. She presses into your palm with a small, helpless sound that is nothing like her bright Council laugh. The candlelight runs gold over her; the crushed flowers give their scent up into the honey and the warm wax. With her other hand she finds your buckles, one after another, and does not trouble to be neat. A strap goes under the cushions, a pauldron rolls away and rings on the stone, and the knot of her robe, which was never holding much, gives way on its own.{/n}
"I counted everything," {n}she whispers against your mouth.{/n} "The candles. The cushions. The flowers. I never counted this. I couldn't have. You were always going to be the part I couldn't plan." {n}Her bracelets are cold on the back of your neck, and her breath is not.{/n} "Don't make me wait for it. I'm terrible at waiting. Ask the cookies."''')

    extend(payload, [("chadali.sessions.what_chance_wishes", "stay")],
           '"I\'ve been waiting for you to ask. Help me with these, then come here."',
           '''{n}You help. It takes longer than it should, because every cushion she hands you comes with a kiss, and by the fourth she has given up pretending the cushions are the point. She stands in the middle of the Council hall with the candle behind her, in the thin yellow silk, hair loose, hooks her fingers in your belt and tugs you up against her.{/n}
"Wish number two," {n}she says against your jaw, breathless and delighted with herself.{/n} "I get to undress you. Slowly. For once in my life, slowly."
{n}She is not slow. She is quick and greedy and laughing, her warm hands flat on your chest through the cloth, then lower, tracing every line they find as though she meant to learn the shape of you for later. Her bracelets are cold against your throat. Her mouth is not. She backs toward the cushions she laid with her own hands, still holding your belt, and you follow.{/n}
"Lucky charm," {n}she whispers, a breath from your mouth,{/n} "I'm going to make you very glad you asked."''')

    paragraph(payload, "chadali.trickster.epilogue.commit", "page",
              "{n}She had not come only for the cookies. Under the travelling cloak she wore the thin yellow silk the Commander had once seen by candlelight, and she had walked the last mile of the road with the cloak open to the spring air so that it would cling. She set the basket down between them and put one bare foot against the Commander's ankle under the table.{/n}\n"
              "{n}She did not say what she wanted. Her foot said it, sliding slowly up the inside of the Commander's calf, and the colour climbing her throat said the rest.{/n}",
              requires=("chadali.trickster.late_invited",))

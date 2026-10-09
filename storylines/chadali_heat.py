"""Chadali: heat pass (HEAT, Directive 12). Build-up text only, applied last (expansion._make_expansion).

Her three slots stopped at "come here". The build-up now carries her warmth and appetite to the start of the act
in her register: delighted, birdsong-and-filthy, luck and cookies and planning she gave up on, bracelets cold on
warm skin. Slot nodes and exits stay as they are; the act is the later fill.
"""
from storylines.heat_text import extend, paragraph


def integrate(payload):
    extend(payload, [("chadali.fortunes.honey", "look")],
           '"Lucky me," {n}she whispers, and she does not mean it as a joke.{/n}', '''
{n}Her fingers close over your hand where it rests on her hip and move it, slowly, up the soft slope of her stomach to her breast, and she arches into it with a small, helpless noise that is nothing like her bright Council laugh. The candlelight runs gold over her. The flowers crushed under her back give up their scent into the honey and warm wax. She hooks one leg around your hip and tugs, and the robe, which was never doing much, falls open entirely.{/n}
"I counted everything," {n}she whispers.{/n} "The candles. The cushions. I never counted this. I couldn't have. You were always going to be the part I couldn't plan." {n}Her other hand slides down your back to your hip and pulls, and she parts her thighs under you, hot and slick against your skin, her eyes never leaving your face.{/n} "Don't make me wait for it. I'm terrible at waiting. Ask the cookies."''')

    extend(payload, [("chadali.sessions.what_chance_wishes", "stay")],
           '"I\'ve been waiting for you to ask. Help me with these, then come here."', '''
{n}You help. It takes longer than it should, because every cushion she hands you comes with a kiss, and by the fourth she has stopped pretending the cushions are the point. She stands in the middle of the Council hall with the candle behind her, in the thin yellow silk, her hair loose, hooks her fingers in your belt and tugs you up against her.{/n}
"Wish number two," {n}she says against your jaw, breathless and delighted with herself.{/n} "I get to undress you. Slowly. For once in my life, slowly."
{n}She is not slow. She is quick and greedy and laughing, and your shirt is gone before the sentence ends, her warm hands flat on your chest, then lower, tracing every line they find as if she meant to learn the shape of you for later. The silk slides off her shoulders and she lets it, bare and flushed and quite unbothered, and walks you backwards onto the cushions she laid with her own hands.{/n}
"Lucky charm," {n}she whispers, kneeling over you, her bracelets cold against your ribs, her thighs bracketing yours, nothing between you but the heat coming off her skin.{/n} "I'm going to make you very glad you asked."''')

    paragraph(payload, "chadali.trickster.epilogue.commit", "page",
              "{n}She had not come only for the cookies. Under the travelling cloak she wore the thin yellow silk the Commander had once seen by candlelight, and she had walked the last mile of the road with the cloak open to the spring air so that it would cling. She set the basket down between them and put one bare foot against the Commander's ankle under the table.{/n}\n"
              "{n}She did not say what she wanted. Her foot said it, sliding slowly up the inside of the Commander's calf, and the colour climbing her throat said the rest.{/n}",
              requires=("chadali.trickster.late_invited",))

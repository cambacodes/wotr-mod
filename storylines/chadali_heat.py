"""Chadali: heat pass (HEAT, Directive 12). Build-up text only, applied last (expansion._make_expansion).

struct3-d holds the honey/look and sessions/stay extensions for Claude's canon-cut
calibration. Exact exported node targets are registered in prose-pending.json;
reservation nodes, exits and aftermath keep their saved structure.
"""
from storylines.heat_text import extend, paragraph


def integrate(payload):
    extend(payload, [("chadali.fortunes.honey", "look")],
           '"Lucky me," {n}she whispers, and she does not mean it as a joke.{/n}',
           '[PROSE PENDING: CH-A2-01 charged approach at the canon cut; retain appetite, impatient dialogue and aftermath.]')

    extend(payload, [("chadali.sessions.what_chance_wishes", "stay")],
           '"I\'ve been waiting for you to ask. Help me with these, then come here."',
           '[PROSE PENDING: CH-A2-01 sibling charged approach at the canon cut; retain cushions, appetite and aftermath.]')

    paragraph(payload, "chadali.trickster.epilogue.commit", "page",
              "{n}She had not come only for the cookies. Under the travelling cloak she wore the thin yellow silk the Commander had once seen by candlelight, and she had walked the last mile of the road with the cloak open to the spring air so that it would cling. She set the basket down between them and put one bare foot against the Commander's ankle under the table.{/n}\n"
              "{n}She did not say what she wanted. Her foot said it, sliding slowly up the inside of the Commander's calf, and the colour climbing her throat said the rest.{/n}",
              requires=("chadali.trickster.late_invited",))

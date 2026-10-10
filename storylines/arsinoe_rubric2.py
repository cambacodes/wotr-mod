"""ARS-A2-02: retain heat-transformed roof nodes behind earned history."""
from copy import deepcopy

from story_format import n, p


NIGHT = """{n}Arsinoe turned the key in the lock behind her. The lease lay on the sideboard where she had set it, folded, and she did not look at it. Her fingers were already at the Commander's collar.{/n}
"Three renewals, every one paid late, and I entered every one as punctual. I have never falsified an account in my life." {n}She caught their hands and kissed them hard.{/n} "Rent has a date and a sum. This has neither. I have spent a season being patient across a counter, and I am done with it."
{n}She undid the rest of the fastenings herself, quick and exact, and let the robes fall where they fell. Her hair came loose as she pushed the Commander back toward the bed. She drew them down beside her, put their hands on her waist, and held them there until the fingers tightened.{/n}
"The lien stands. This is outside it. Look at me."
{n}Her composure broke on a breath, and she bent to their mouth.{/n}"""
RETURN = """{n}Arsinoe did not stop to remark on the room. She shut the door with her heel and laid her gloves on the table beside the lease, and she looked at neither.{/n}
"I remember the counter, and the pen on the floor, and the tea gone cold in the cup. I remember that I did not once look at the clock." {n}She crossed to the Commander and took their face in both hands.{/n} "The lease has not changed. Neither has this. I have been entering your payments as late for weeks, and I have been in no hurry whatever to collect."
{n}She was out of her robe before the Commander had finished answering, and her hair followed it. She pushed them down onto the bed and kissed them as if there were a debt outstanding.{/n}
"Outside the lease, as before. I intend to be insufferable about it."
{n}Her hands found theirs, and she held them against her waist.{/n}"""


def integrate(payload):
    from storylines import arsinoe_trickster as route
    late = next(s for s in payload["Scenes"] if s["Id"] == "arsinoe.trickster.late.commit")
    if any(n["Id"] == "rubric2_cauldron_night" for n in late["Nodes"]):
        return
    offer = late["Nodes"][0]
    for old, new, beat in (
        ("night", "rubric2_cauldron_night", NIGHT),
        ("late_return", "rubric2_cauldron_return", RETURN),
    ):
        node = next(n for n in late["Nodes"] if n["Id"] == old)
        incoming = next(c for c in offer["Choices"] if c["Next"] == old)
        alternate = deepcopy(incoming)
        incoming["Requires"].append("arsinoe.roof_shared")
        alternate["Next"] = new
        alternate["Forbids"].append("arsinoe.roof_shared")
        # Shared payoff integration gates the saved first answer by index.
        # Its appended twins must consume the same earned outcome explicitly.
        alternate["Requires"].append(route.LATE_COMMITTED)
        offer["Choices"].append(alternate)
        callback = n(new, node["Speaker"], beat, *deepcopy(node["Choices"]))
        account_callbacks(callback, route)
        late["Nodes"].append(callback)


def account_callbacks(node, route):
    """Replace unsupported financial sentences; preserve the surrounding heat."""
    spans = {
        "rubric2_cauldron_night": (
            'Three renewals, every one paid late, and I entered every one as punctual. I have never falsified an account in my life.',
            'The lien stands. '),
        "rubric2_cauldron_return": (
            'The lease has not changed. ',
            'I have been entering your payments as late for weeks, and I have been in no hurry whatever to collect.',),
    }
    text = node['Text']
    # Split exact retained text around the account assertions. Paragraph order
    # preserves the original staging and all non-financial wording verbatim.
    parts = []
    for assertion in spans[node['Id']]:
        before, text = text.split(assertion, 1)
        parts.append(before)
    node['Text'] = parts[0]
    node['Paragraphs'] = []
    def pending(brief, requires=(), forbids=()):
        node['Paragraphs'].append(p(
            '[PROSE PENDING: arsinoe.trickster.late.commit/' + node['Id'] + ' - ' + brief + ']',
            requires=requires, forbids=forbids))
        node['Paragraphs'][-1]['Id'] = 'fix14.account.' + str(len(node['Paragraphs']) - 1)
    pending('Last Call returned the property and closed the lease account; recall settlement, never an outstanding lien or invented payments', (route.CALLED,))
    pending('Property burst without Last Call settlement; the loss account remains outstanding, with only actually pledged collateral',
            ('arsinoe.siphon_burst',), (route.CALLED,))
    pending('Last Call ended with property returned intact without her call; collateral released, rent accounted separately',
            (route.LC,), (route.CALLED, 'arsinoe.siphon_burst'))
    pending('Before settlement or recorded return, recall the existing lease and only its earned collateral; do not invent renewal payments',
            (), (route.CALLED, route.LC, 'arsinoe.siphon_burst'))
    for key, label in ((route.STILL, 'still'), (route.WORD, 'pledged word'), (route.LIEN, 'Worldwound lien')):
        pending('Recall ' + label + ' as the recorded collateral, with release or liability matching the preceding account history', (key,))
    pending('Recall the three waived renewals, without claiming paid late renewals', (route.GRACE,))
    pending('No rent grace was earned; do not claim waived or recorded paid renewals', (), (route.GRACE,))
    # Remaining original fragments keep their wording and relative order.
    for part in parts[1:]:
        node['Paragraphs'].append(dict(p(part), Text=part))
    node['Paragraphs'].append(dict(p(text), Text=text))

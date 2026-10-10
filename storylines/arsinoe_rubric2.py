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


# Spoken inside the quotation the retained fragments open and close. Each line states only what its gate guarantees.
ACCOUNT_LINES = {
    "rubric2_cauldron_night": (
        "The cauldron was handed back at the rift, and I entered the return before anything else. The lease is closed.",
        "The stone burst at Threshold. The loss account is open, your name stands beside the sum, and I have not entered one crown of it as paid.",
        "The stone came through Last Call whole, and I did not call it in. The collateral is released, and the rent has a page of its own.",
        "The lease stands as written and the account stands with it. I have entered nothing there that was not done.",
        "The Fool King's still is entered as security, and the account, not my mood, decides what becomes of it.",
        "Your word is in the ledger as security. It leaves by the account, not by my mood.",
        "The lien is in my own hand, and the lease governs it.",
        "The three renewals waived at the counter stay waived, struck out in the same ink. I have never falsified an account in my life.",
        "I waived no renewal and entered no kindness the lease did not allow. I have never falsified an account in my life.",
    ),
    "rubric2_cauldron_return": (
        "The cauldron was handed back at the rift, and the account closed on the return.",
        "The stone burst at Threshold, and the loss account remains open under your name.",
        "The stone came through Last Call whole and I did not call it in. The collateral is released, and the rent keeps its own page.",
        "The lease stands as written, and I have kept to it.",
        "The Fool King's still is entered as security. Whatever becomes of it, the account decides, and not I.",
        "Your word is entered as security. Whatever becomes of it, the account decides, and not I.",
        "The lien is in my hand and answers to the lease alone.",
        "The three renewals waived at the counter are still struck out, and the entry has not changed.",
        "I waived no renewal, and the terms have not changed.",
    ),
}


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
    texts = ACCOUNT_LINES[node['Id']]
    # (requires, forbids) per line, in order. Lines 0-3 are exclusive and exhaustive;
    # 4-6 read the recorded collateral; 7 and 8 split on the earned grace.
    gates = (
        ((route.CALLED,), ()),
        (('arsinoe.siphon_burst',), (route.CALLED,)),
        ((route.LC,), (route.CALLED, 'arsinoe.siphon_burst')),
        ((), (route.CALLED, route.LC, 'arsinoe.siphon_burst')),
        ((route.STILL,), ()),
        ((route.WORD,), ()),
        ((route.LIEN,), ()),
        ((route.GRACE,), ()),
        ((), (route.GRACE,)),
    )
    for text, (requires, forbids) in zip(texts, gates):
        node['Paragraphs'].append(p(text, requires=requires, forbids=forbids))
        node['Paragraphs'][-1]['Id'] = 'fix14.account.' + str(len(node['Paragraphs']) - 1)
    # Remaining original fragments keep their wording and relative order.
    for part in parts[1:]:
        node['Paragraphs'].append(dict(p(part), Text=part))
    node['Paragraphs'].append(dict(p(text), Text=text))

"""Claude voice for Vellexia's lines in the pair rows this route owns.

CLOUD-QUEUE shared-scene rule: villain-route-vellexia sits above arueshalae,
so it voices household.pair.arueshalae_vellexia.* (row S24). Text only, after
the row builders and the contract controller: no node, choice, flag or gate
changes, and no paragraphs. The staging (the staves, the assault map, the
bout the Commander calls) is kept; only Vellexia's flat lines are put back in
her register: the old mistress of the house Arueshalae fled, who still counts
her among the furniture and wants her hungry again (native 51d80804: "old,
cruel, and utterly insane"; mod pack voice/arueshalae.md: raised in her house).
Arueshalae's lines are left as written (the arue12 pass owns her voice).
"""

S24 = "household.pair.arueshalae_vellexia."

# (old substring, new substring, minimum hits)
SUBS = [
    ('''"How dreary. And how irritating that you did it well."''',
     '''"How dreary. And how irritating that you did it well. I taught you better than sticks, little bird. I taught you to finish."''', 3),
    ('''"Oh, I have plenty. Very few can knock a weapon out of my hands."''',
     '''"Oh, I have plenty. Half of them are holding up my lamps. Very few could ever knock a weapon out of my hands. You were always my favourite."''', 3),
    ('''"And here I thought a war might cure this city's dullness."''',
     '''"And here I thought a war might cure this city's dullness. Run along, then. You always did come back hungrier."''', 4),
    ('''"Do bring me something less tedious next time, Commander. Your war will not last forever."''',
     '''"Do bring me something less tedious next time, Commander. Your war will not last forever, and neither will her diet."''', 4),
]


def register(payload, scenes, refs):
    own = [s for s in payload["Scenes"] if s["Id"].startswith(S24)]
    if len(own) != 4:
        raise ValueError(f"vellexia pairs: expected 4 S24 scenes, got {len(own)}")
    for old, new, minimum in SUBS:
        hits = 0
        for s in own:
            for node in s["Nodes"]:
                if old in node["Text"] and new not in node["Text"]:
                    node["Text"] = node["Text"].replace(old, new)
                    hits += 1
        if hits < minimum:
            raise ValueError(f"vellexia pairs: expected {minimum} hits, got {hits}: {old[:50]!r}")

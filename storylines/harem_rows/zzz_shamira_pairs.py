"""Claude voice for Shamira's lines in the pair rows this route owns.

CLOUD-QUEUE shared-scene rule: villain-route-shamira sits above vellexia and
arueshalae, so it voices household.pair.vellexia_shamira.* (row S17) and
household.pair.shamira_arueshalae.* (row S44). Text only, after the row
builders and the contract controller: no node, choice, flag or gate changes,
and no paragraphs. The staging of each row (the dispatch at the Fool King's
table, the escape hold on the landing, the bracelet, the cushions, the name)
is kept; only Shamira's flat lines are put back in her register: court
menace, legal sneer, one insult when crossed (native 2c48146b, 339f715c,
a05b45a9, 6a624195). The other woman's lines are left as written.
"""

S17 = "household.pair.vellexia_shamira."
S44 = "household.pair.shamira_arueshalae."

# (scene prefix, old substring, new substring, minimum hits)
SUBS = [
    (S17, '''"Your nobles came through my doors when they wanted the queen's attention. You kept them amused. I decided which requests reached her."''',
     '''"Your nobles crawled through my doors whenever they wanted my lady's ear. You kept them amused. I decided which of them she heard, and which of them went home without a tongue."''', 1),
    (S17, '''"You have had your turn. I have not finished."''',
     '''"Sit down, cow. You have had your turn. I have not finished."''', 1),
    (S17, '''"Keep your little audience." {n}Shamira pushes her cup away.{/n} "You will not speak for me again."''',
     '''"Keep your little audience." {n}Shamira pushes her cup away.{/n} "You will not speak for me again. The next mouth in this city that tries it, I keep in a jar."''', 1),
    (S44, '''"Show me, then. If this body disgraces me, I would rather discover it here than before an enemy."''',
     '''"Show me, then. This body was grown in a garden for a customer who never paid. I want to know whether it can break a hold before somebody at my court finds out that it cannot."''', 4),
    (S44, '''"A pity," {n}Shamira says. ''',
     '''"A pity," {n}Shamira says.{/n} "I had girls flayed for less than walking out of my court, little bird. You were always lucky." {n}''', 2),
    (S44, '''"Then I keep my claim," {n}Shamira says. ''',
     '''"Then I keep my claim," {n}Shamira says.{/n} "She was my city's before she was anybody's." {n}''', 2),
]


def register(payload, scenes, refs):
    own = [s for s in payload["Scenes"] if s["Id"].startswith((S17, S44))]
    for prefix, old, new, minimum in SUBS:
        hits = 0
        for s in own:
            if not s["Id"].startswith(prefix):
                continue
            for node in s["Nodes"]:
                if old in node["Text"] and new not in node["Text"]:
                    node["Text"] = node["Text"].replace(old, new)
                    hits += 1
        if hits < minimum:
            raise ValueError(f"shamira pairs: {prefix}: expected {minimum} hits, got {hits}: {old[:50]!r}")

"""E15 RRT book UI content: the glossary tooltips for the new mechanics, and a small in-world guide book.

Glossary keys are what other modules link from text as {g|RRT_Key}words{/g} (the native tooltip). The guide is the
end-to-end demo of the book contract (Writer/handoffs/09-RRT-BOOK-UI.md): sections, entries with portraits, a
conditional line, a condition on an entry, and a closing tooltip link. The Ledger supplies its own book the same way.
"""

GLOSSARY = {
    "RRT_Mailbag": dict(
        Name="The Satchel",
        Description="Letters that arrive while you rest wait here until you read them. Open any of them, in any order; "
                    "the rest will keep. A correspondent's next letter arrives only once you have read the one before."),
    "RRT_LettersKept": dict(
        Name="Letters Kept",
        Description="Every letter you have read, the newest on top. Rereading changes nothing: the words are the same, "
                    "and so is everything that followed from them."),
    "RRT_Ledger": dict(
        Name="The Trickster's Ledger",
        Description="The Commander's own account of the long con: debts owed and owing, who sits at the table, where the "
                    "seating is difficult, and what must never be said aloud."),
    "RRT_Debt": dict(
        Name="Debt",
        Description="A promise made to a power, a person or the world itself. Debts come due. Each is paid, called in, "
                    "cheated through a loophole its own terms left open, or outlived."),
    "RRT_Secret": dict(
        Name="Secret",
        Description="Something you did that some companions must never learn. The Ledger notes who would object and how "
                    "exposed the secret is. Discovery comes from what they notice, never from chance."),
    "RRT_SecretRisk": dict(
        Name="Risk of Discovery",
        Description="How exposed a secret is. Low when the tracks are covered; high when a sharp-eyed or truth-bound "
                    "companion stands close to the evidence. Covering tracks has its own price."),
    "RRT_WordMadeTrue": dict(
        Name="Word Made True",
        Description="The Trickster's rarest move: declare a quarrel settled, and it is. At most three times in a campaign, "
                    "each one written into the Ledger as a debt. Some companions notice when the world has been tampered "
                    "with, and some things cannot be joked away."),
    "RRT_Tolerated": dict(
        Name="Tolerated",
        Description="She stays, but there is one person at the table she will not speak to. She will not harm her, and she "
                    "gets on with everyone else. A worse outcome than it sounds, and never the last word."),
    "RRT_AtTheTableApart": dict(
        Name="At the Table, Apart",
        Description="How the ending remembers a companion who only tolerates the household: present, seated apart, looking "
                    "past one chair."),
}

GUIDE = dict(
    Title="The Courier's Notes",
    Opening="{n}Folded into the lid of the satchel: the courier's own notes, in a careful and very tired hand.{/n}",
    Portrait="",
    Sections=["Letters", "The Ledger"],
    Entries=[
        dict(Id="letters.satchel", Section="Letters", Title="The satchel",
             Text="{n}Letters wait in the {g|RRT_Mailbag}satchel{/g} until you read them. Take them in whatever order you "
                  "like. A correspondent's next letter follows only once the last one has been read, so nobody's story "
                  "arrives out of order.{/n}",
             Tooltip="RRT_Mailbag"),
        dict(Id="letters.kept", Section="Letters", Title="Letters kept",
             Text="{n}Nothing read is thrown away. The {g|RRT_LettersKept}letters you kept{/g} lie in the bottom of the "
                  "satchel, the newest on top. Read them again whenever you like; rereading changes nothing.{/n}",
             Tooltip="RRT_LettersKept"),
        dict(Id="ledger.account", Section="The Ledger", Title="Keeping accounts",
             Requires=["trickster"],
             Text="{n}\"Other commanders keep diaries,\" the courier has written, and underlined it twice. \"Yours keeps a "
                  "{g|RRT_Ledger}ledger{/g}. I have learned not to ask whose names are in it.\"{/n}",
             Lines=[dict(Text="{n}A later line, in different ink: \"Every {g|RRT_Debt}debt{/g} comes due. I only carry the "
                              "letters.\"{/n}", Requires=["trickster.ever"])],
             Tooltip="RRT_Ledger"),
    ],
)


def integrate(payload):
    payload.setdefault("Glossary", {}).update({key: dict(value) for key, value in GLOSSARY.items()})
    payload.setdefault("Books", {})["rrt.guide"] = GUIDE

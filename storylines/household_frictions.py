"""The friction registry of the Trickster's household (Writer/handoffs/08-TRICKSTER-HOUSEHOLD.md §3). DATA ONLY.

A friction is a pair of partners with a real, canon-rooted reason to clash. Only these pairs ever get a household scene;
every other pair defaults to cordial. This pass writes NO scene. It records the pairs, so that:
- the Ledger's Seating Notes can list a friction once both women are at the table (household.py builds the entries);
- the later pass (memory rrt-harem-order: harem pair scenes come LAST) has one reviewed list to write from.

Fields:
  a, b     relationship ids (the pair; a is the side whose portrait the Seating Notes entry shows)
  root     the canon reason, with its citation (merged route file, enGB cue, or spec)
  status   "verified": both halves of the root are checked against merged routes and canon;
           "to verify": plausible, but at least one half still needs a canon check before a scene is written
  kind     faith | rivalry | power | atrocity | law | trust
  tools    the approaches a scene may offer (08 §2.3): at least two different tool types; "word" = Word Made True
  fails    who ends up tolerated, and toward whom, when the Commander fails (rule: exactly one enmity per woman)
  form     the scene form (08 §5: no form more than twice across the registry)
  note     the summary shown in the Ledger's Seating Notes, in the Commander's hand (plain {n} narration)
"""

FRICTIONS = [
    dict(a="seelah", b="camellia", status="verified", kind="faith", form="a vigil for the dead",
         root=("Seelah is a paladin of Iomedae (seelah_trickster.py:112, her canon hub); Camellia kills the people who "
               "call her a friend (camellia_trickster.py:4, Camelia companion quest)."),
         tools=("skill:lore_religion", "item:camellia_confession", "word"),
         fails=dict(tolerated="seelah", enmity="camellia"),
         note=("Seelah prays for the dead. Camellia makes them. Do not seat them where either can see the other's "
               "hands.")),
    dict(a="hepzamirah", b="minagho_chivarro", status="verified", kind="rivalry", form="a shared job",
         root=("Hepzamirah is Baphomet's daughter and archpriestess (hepzamirah_trickster.py:4, Hepzamirah_main/Cue_0012); "
               "Minagho bleeds from Baphomet's brand (minagho_chivarro_trickster.py:4, MinaghoAfterCombat/Cue_0020)."),
         tools=("favour:baphomet_terms", "skill:trickery", "job:common_enemy"),
         fails=dict(tolerated="whichever lost face", enmity="the other"),
         note=("Two of Baphomet's creditors at one table. Each thinks the other owes her. Both are right.")),
    dict(a="arueshalae", b="nocticula", status="verified", kind="power", form="a renunciation before witnesses",
         root=("Arueshalae left the queen of succubi, whose claim on every succubus she still feels (Nocticula_main/Cue_0523 "
               "b84ef61b, 'This demon follows you around only because I allow it'; arueshalae_treatment.py queen). The old "
               "summons debt and court.arueshalae are retired (2026-10-01); the claim, not a debt, is the root."),
         tools=("skill:persuasion_t3", "item:debt_paper", "favour:nocticula"),
         fails=dict(tolerated="arueshalae", enmity="nocticula"),
         note=("The queen wants her rank acknowledged. The defector wants to stop kneeling without meaning to. Neither wants the other's "
               "chair.")),
    dict(a="arsinoe", b="nurah", status="verified", kind="law", form="an audit",
         root=("Arsinoe is a priestess-banker of Abadar (arsinoe_trickster.py:5, Council_5-1/Cue_0041); Nurah's route "
               "turns on forged papers (nurah_trickster.py:13)."),
         tools=("skill:knowledge_world", "favour:lien", "word"),
         fails=dict(tolerated="arsinoe", enmity="nurah"),
         note=("One of them keeps the crusade's accounts. The other has forged several of them. Arsinoe has not noticed "
               "yet.")),
    dict(a="seelah", b="areelu", status="verified", kind="atrocity", form="a restitution inspection",
         root=("Areelu opened the Worldwound; Seelah's objection is already written (areelu_trickster.py:756 "
               "areelu.trickster.react.seelah_objects)."),
         tools=("quest:reckoning", "item:worldwound_record"),   # atrocity: quest or item only, never a check, never "word"
         fails=dict(tolerated="seelah", enmity="areelu"),
         note=("Some things cannot be joked away. Seelah will not break bread with the woman who made the Wound, and I "
               "will not ask her to without earning it.")),
]

KINDS = ("faith", "rivalry", "power", "atrocity", "law", "trust")
TOOL_TYPES = ("skill", "item", "favour", "job", "quest", "word")
ATROCITY_FORBIDS = ("word", "skill")   # 08 §2.3: atrocity frictions are settled by a quest or an item only


def validate(eligible_rels):
    """Build-time checks on the registry itself (no scene is involved)."""
    seen, forms = set(), {}
    for f in FRICTIONS:
        pair = tuple(sorted((f["a"], f["b"])))
        if pair in seen:
            raise ValueError("Duplicate friction: %s/%s" % pair)
        seen.add(pair)
        for rel in pair:
            if rel not in eligible_rels:
                raise ValueError("Friction names a relationship with no eligibility key: %s" % rel)
        if f["status"] not in ("verified", "to verify") or f["kind"] not in KINDS:
            raise ValueError("Friction status/kind: %s/%s" % pair)
        types = {t.split(":")[0] for t in f["tools"]}
        if not types <= set(TOOL_TYPES) or len(types) < 2:
            raise ValueError("A friction needs at least two different tool types: %s/%s" % pair)
        if f["kind"] == "atrocity" and types & set(ATROCITY_FORBIDS):
            raise ValueError("An atrocity friction is settled by a quest or an item only: %s/%s" % pair)
        forms[f["form"]] = forms.get(f["form"], 0) + 1
        if forms[f["form"]] > 2:
            raise ValueError("Scene form used more than twice: %s" % f["form"])
    return True

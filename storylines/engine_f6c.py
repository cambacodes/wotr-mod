"""eng7-f6c: authored reconciliations of existing earned Trickster outcomes.

These variants change dialogue facts, never quest actions or relationship terms.
The Guild retains Horzalah after her paid escape; Greybor runs its contracts.
Irabeth's morale still decides service or retirement. Baphomet retains the debt
transferred in spared.brand. Terendelev's restitution ends the trapped voice.
Cue_0765's action-free funeral address is hidden after restitution; its native
sequence and ShowOnce history stay intact. Answer_0784's valid future question
stays native; only its contradictory reply changes, without a history alias.
"""
from story_format import c, n, p, scene
from storylines.native_facts import key
from storylines.native_overrides import declare


# Native keys/parents verified against blueprints.zip and enGB.json.
EDITS = (
    ("661508b5683d140458f6a0908de98d70", "herrax", "reachable",
     dict(Parent="d69aa03788628cc41848cad53c94e4fb", Dialog="b1a346ae168956b4a8b759845ab8d2de",
          Key="79d1fac5-23ab-460e-8e60-ce60a4a62ae1"),
     [["trickster.now", "herrax.committed", "!herrax.closed"]],
     '''{n}Herrax's smile deepens. She touches the bone sheath at her hip.{/n} "You already know which door I leave open for you. But I have a house to run, darling. Sit with me a while. Let the others wonder what you paid."'''),
    ("62f20840e6aa33844b641c5c8e10f814", "horzalah", "guild",
     dict(Page="9669bef01411fd2498a466d2aef63bca", Sequence="fec3b6f28610c8a48a239f148ed3ed60",
          Key="8ccf1c23-ae95-4b2e-84cc-37b647aabebd"),
     [["trickster.now", "horzalah.trickster.primed", "horzalah.trickster.returned", "horzalah.trickster.guild_survives"]],
     '''{n}After the war, Greybor returned to Alushinyrra and killed four rivals for command of the Assassins' Guild's contracts. Horzalah kept the Guild itself. The Commander's ear had helped her keep her chair when her own masters circled it. She had no intention of surrendering it to a dwarf. Greybor chose his work, set his rates, and made the arrangement profitable enough to survive. Across many planes, the words "sweet dreams" still made people shudder.{/n}'''),
    ("8ae3220fd0a645809f59f54f8d89985f", "horzalah", "trio",
     dict(Parent="8b037c275d3423f44a2e5ecc02c003cf", Dialog="ae58532cb72b28b4eaaccb82eb78eaea",
          Key="1dd07de3-c767-4561-b659-4b9cea9cf6e7"),
     [["trickster.now", "horzalah.trickster.primed", "horzalah.trickster.returned", "horzalah.trickster.guild_survives"]],
     '''{n}She joined forces with Greybor, who commanded the Assassins' Guild's contracts under Horzalah, and Woljif, Alushinyrra's best fixer. The three former companions rose to power over the city's aristocracy. Horzalah took her share and left them to their own appetites. Their enemies hid and waited for one of the three to betray the others. To everyone's surprise, they were still waiting.{/n}'''),
    ("cba964e33d0a0704d847629be452b359", "irabeth", "service",
     dict(Page="ae1f824fe248d9f4aac7d39ec2e12140", Sequence="f8d7f50e3bb88c143834d234c0b24474",
          Key="c174e4f2-0f7f-4fc4-9e21-88b56cb2506b"),
     [["trickster.now", "irabeth.committed", key("irabeth.encouraged")]],
     '''{n}Irabeth meant to retire. The Eagle Watch needed another week, then another month, then years. The complaints grew louder, and no less proud. Irabeth did take her leave at last; she had promised herself a road beyond the next duty roster. She always returned to the Watch.{/n}'''),
    ("2d6b09c6508010e49b882741add89dcf", "irabeth", "retired",
     dict(Page="ae1f824fe248d9f4aac7d39ec2e12140", Sequence="f8d7f50e3bb88c143834d234c0b24474",
          Key="3ad4bedd-1e78-470d-812d-98d51d3ed1b2"),
     [["trickster.now", "irabeth.committed", key("irabeth.broken")]],
     '''{n}After the victory, Irabeth retired to the wilderness of the River Kingdoms. The Lost Chapel still followed her into sleep. Some nights she woke before she recognized the room. There were also quiet mornings, journeys, and letters in Irabeth's square hand. She kept her faith and her sword; she handed back her commission.{/n}'''),
    ("17249a81e2f0d7d4ca67937db86ef858", "minagho_chivarro", "debt",
     dict(Parent="c5f918382f54e4342b40334c2d9f854f", Dialog="257e13519dd1f5b4c8d992865ba0f609",
          Key="7cf9be7f-e702-408c-97b0-76cda664bcc5"),
     [["trickster.now", "minagho_chivarro.trickster.spared.brand"]],
     '''"Her seals have gone dry. You offered them your blood, and now my collectors have another scent to follow. Did you think I would refuse a debtor who has so much more to lose? Minagho still bears my marks. Let her look at them whenever she forgets whose mercy she bought with your hand."'''),
    ("c68d9b3a2b887f645ac539f996a63a92", "terendelev", "beginning",
     dict(Parent="31665b38d6922ef4ab4cb83afa8245fe", Dialog="bf328bcec67a5014f9a56ee6220f3bcc",
          Key="222096f4-434d-4e8c-99c5-67c070fb21c8"),
     [["trickster.ever", "terendelev.trickster.returned"]],
     '''{n}The Storyteller puts his hand to his forehead.{/n} "Terendelev has returned, but the scale remembers an older struggle. Its beginning is still hidden from me. Bring me something else that belonged to her, and perhaps I can learn how the corruption first took hold."'''),
    ("ca71b79bc9a45b741bcc6599ef017fe7", "terendelev", "voice",
     dict(Parent="fd39fd84212de2047b6b887c9a9cf28e", Dialog="bf328bcec67a5014f9a56ee6220f3bcc",
          Key="da750b86-b8b0-4a2f-a6d4-fea3512327b0"),
     [["trickster.ever", "terendelev.trickster.returned"]],
     '''{n}The Storyteller listens, his fingers resting on the scale.{/n} "The voice that cried out in darkness is quiet now. You brought her back. This scale can tell me what she suffered; it cannot tell me what she will choose to do with the life you returned to her."'''),
)


def integrate(payload):
    # Authored job-2 predicate: Guild ownership survives free departure,
    # while her death or loss of the returned body leaves native ownership.
    payload.setdefault("Derived", {})["horzalah.trickster.guild_survives"] = [
        ["trickster.now", "horzalah.trickster.primed", "horzalah.trickster.returned"]]
    payload.setdefault("DerivedForbids", {})["horzalah.trickster.guild_survives"] = [
        "horzalah.dead", "horzalah.returned_actor_lost"]
    declare(payload, source=__name__ + ".eng7-f6c", target="21b10801b6c2b194d92506a137ef1307",
        target_type="cue", action="HIDE", key="terendelev.funeral_introduction",
        spec=dict(Target="21b10801b6c2b194d92506a137ef1307", Relationship="terendelev",
                  When=[["trickster.ever", "terendelev.trickster.returned"]]))
    from storylines.irabeth_partner_stance import cover_native
    for target, relationship, suffix, location, when, text in EDITS:
        identity = relationship + ".native.eng7_f6c." + suffix
        payload["Scenes"].append(scene(identity, "", "NativeEpilogue", 0, "",
            [n("line", "Narrator", text, c())], last=99, Relationship=relationship,
            requires=tuple(k for k in when[0] if not k.startswith("!")) if relationship == "horzalah" else (when[0][0],),
            forbids=tuple(k[1:] for k in when[0] if k.startswith("!")) if relationship == "horzalah" else ()))
        declare(payload, source=__name__ + ".eng7-f6c", target=target,
            target_type="slide" if "Page" in location else "cue",
            action="SLIDE-SWAP" if "Page" in location else "REPLACE",
            spec=dict(location, Replacement=identity, When=when))
    cover_native(payload)


def reconcile_employment(payload):
    # Native morale still governs the independent route, including runs which
    # never committed to the returned route. No new retirement bargain is added.
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    changes = {
        "irabeth.ending_lasting": (
            "After the war Irabeth kept her rank for exactly one more year, trained the officer who replaced her, and then took the fortnight's leave she had been threatening since Drezen.",
            "After the war Irabeth took the fortnight away she had been threatening since Drezen."),
        "irabeth.ending_unfinished": (
            "Irabeth went back to her post and her paperwork.",
            "Irabeth kept the unfinished letter among her papers."),
        "irabeth.ending_ascent": (
            "She went on praying to Iomedae, keeping her post and taking her leave at the lake.",
            "She went on praying to Iomedae and taking journeys to the lake."),
    }
    for identity, (old, new) in changes.items():
        node = scenes[identity]["Nodes"][0]
        if old not in node["Text"]:
            raise ValueError("eng7-f6c: Irabeth employment text drift: " + identity)
        node["Text"] = node["Text"].replace(old, new)
        node.setdefault("Paragraphs", []).extend((
            p("{n}The Eagle Watch kept postponing Irabeth's retirement. She served for years, taking leave between assignments.{/n}",
              requires=(key("irabeth.encouraged"),), forbids=("irabeth.trickster.returned", key("irabeth.broken"))),
            p("{n}Irabeth retired to the River Kingdoms. The Lost Chapel still woke her screaming on some nights. Her letters came from the wilderness, without a rank beneath the signature.{/n}",
              requires=(key("irabeth.broken"),), forbids=("irabeth.trickster.returned",)),
        ))

    # Append Irabeth's marriage account after all pre-existing ending paragraphs.
    from storylines.irabeth_partner_stance import cover_endings
    cover_endings(payload["Scenes"])

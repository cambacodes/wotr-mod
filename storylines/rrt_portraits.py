"""Book-picture fallbacks (art pass 1, 2026-09-28).

A portrait key with no Scenes/<key>.png falls back to a native BlueprintPortrait (the character's own in-game art, the
most recognizable; used for canon companions and NPCs whose native portrait already fits the art brief) or to another
key's shipped file. A custom PNG always wins. See art/ART-PASS-1.md for the per-key sources and inspection verdicts.
"""

# Native BlueprintPortrait GUIDs, verified in blueprints.zip. Proper portraits unless marked initiative (184x244 only).
NATIVE = {
    "Aivu": "1f5bfefa49a8aa2449ad94b1f4f61788",
    "Areelu": "1d19be67a5a2458dacc608493ea4d6b2",
    "Baphomet": "88e4b1b15bf04633b971ca80ef7605bd",  # initiative image
    "Camellia": "d227d31233aa2494fba89cb715afbb87",
    "Daeran": "16456c362f6535c4a81c625d917b30dd",
    "Ember": "0b3d046086ea25b4bad5d5306e6a7612",
    "Finnean": "945a5699771b53c46978009ef8075622",
    "Galfrey": "a3ba06b4723c7a74fb5054ccb2289efb",
    "Greybor": "c542695eee15988478d4fa07a1eddb0e",
    "Kyado": "efcd57ef238d483391bf5360b2821ba9",  # initiative image
    "Lann": "b9fea9f24838d43469948aa54088d600",
    "Mutasafen": "fbbe968abe1d4cdabc31af520526cc8b",  # initiative image
    "Nenio": "2b4b8a23024093e42a5db714c2f52dbc",
    "Nurah": "4409935f79a11c24980c1c8f70b328f6",
    "Regill": "ea0e28ad6b566444885ef21357f76a87",
    "Seelah": "0ebca33b0e5eb514aa75d9989a565f2f",
    "Socothbenoth": "5bc3985a76b94ae3ad133a2cd2e765af",  # initiative image
    "Sosiel": "d721e6b0cf0634e41a070531bcfd1f92",
    "Storyteller": "ca7e9df2ad3b43843894e3a393a5d08d",
    "Ulbrig": "1faff0d995004389a6638388d6d4b5f2",
    "Wenduag": "c883d02a0d8a4b54f903d351c8fd6af7",
    "Woljif": "cd965f50af3cfba4c81b55c9951e7afa",
}

# Keys whose approved art already ships under a scene name.
ALIASES = {
    "Arsinoe": "ArsinoeShop",
    "Gesmerha": "GesmerhaWorkshop",
    "Soana": "SoanaForest",
    "Targona": "TargonaCorrespondence",
    "Vellexia": "VellexiaManorSpeaker",
}


def integrate(payload):
    fallbacks = payload.setdefault("PortraitFallbacks", {})
    fallbacks.update(NATIVE)
    fallbacks.update(ALIASES)

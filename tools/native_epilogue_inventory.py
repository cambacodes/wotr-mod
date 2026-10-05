"""eng7-f5: regenerate deterministic, harness-only cue and synthetic state fixtures.

States are final RRT snapshots, not campaign receipts. No native etudes are written.
python tools/native_epilogue_inventory.py --story development/Story.json
"""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.game_blueprints import find_bindings, game_dir

TARGETS = (
    "78ae1bdc3b0824b4ca2ed618782f1faa",  # Arueshalae dream
    "ccd140dbf2603734aa323261c2445bec",  # Tirabade departure
    "3a3e561c6b05a284d93eb3bff7b712a6",  # Tirabade widow
    "825786e8c5db4511ae30950bb286f0e9",  # Areelu cottage
    "1b53c189b767412f921b8294b980a51c",  # Areelu mortal
    "164c14743ee768f409a04f93a040e678",  # DragonEggs
    "81109ea8fb20dbc478cf67116740f4a1",  # Kiana aftermath
    "a819e8c85ef23324bb0d8117bb9d7df3",  # Kiana aftermath siblings
    "df45181e1968f26459f9e8bc2b995a34",
    "f5906acda82efd5468cb72aff2e68f7e",  # Galfrey realm siblings
    "becde70692b74ab4eba1d0cf82d2958f",
)


def make_cases(story):
    scenes = {s["Id"]: s for s in story["Scenes"]}
    cases = []
    # All registered routes, including friendship pages. Never infer a return from commitment.
    for cue, edit in sorted(story["NativeEpilogueEdits"].items()):
        for index, variant in enumerate([edit, *edit.get("Variants", [])]):
            scene = scenes[variant["Replacement"]]
            for group_index, group in enumerate(variant["When"]):
                flags = set(scene.get("Requires", [])) | {f for f in group if not f.startswith("!")}
                for any_group in scene.get("RequiresAnyGroups", []):
                    flags.add(any_group[0])
                if scene.get("RequiresAny"):
                    flags.add(scene["RequiresAny"][0])
                flags -= {f[1:] for f in group if f.startswith("!")}
                cases.append(dict(Id=f"{cue}/v{index}/g{group_index}", Target=cue,
                                  Dialog=edit.get("Dialog", ""), Page=edit.get("Page", ""),
                                  Chapter=max(6, scene.get("MinChapter", 6)), Flags=sorted(flags),
                                  NativeEligible=[cue], ExpectedCandidate=variant["Replacement"]))
        # Controls change only synthetic snapshots. Existing route rules decide which mourning/closure pages remain.
        base = next(c for c in cases if c["Target"] == cue)
        required = {f for v in [edit, *edit.get("Variants", [])] for g in v["When"] for f in g
                    if not f.startswith("!") and not f.startswith("trickster.") and f != "trickster"}
        controls = {
            "off-Trickster": set(base["Flags"]) - {f for f in base["Flags"] if f == "trickster" or f.startswith("trickster.")},
            "unpaid": set(base["Flags"]) - required,
            "closed": set(base["Flags"]) | {story["Relationships"][scenes[base["ExpectedCandidate"]]["Relationship"]]["ClosedFlag"]},
            "unreturned-sacrifice": (set(base["Flags"]) | {"sacrifice"}) - {
                s.get("ForbidOverrides", {}).get("sacrifice", "trickster.commander_back") for s in scenes.values()},
            "degraded": set(base["Flags"]) | {"rrt.degraded." + scenes[base["ExpectedCandidate"]]["Relationship"]},
        }
        for label, control in controls.items():
            cases.append(dict(base, Id=f"{cue}/control/{label}", Flags=sorted(control)))
        cases.append(dict(base, Id=f"{cue}/control/native-ineligible", NativeEligible=[]))
    for scene in story["Scenes"]:
        if not scene["Owner"].endswith("Epilogue"):
            continue
        if any(c["ExpectedCandidate"] == scene["Id"] for c in cases):
            continue
        flags = set(scene.get("Requires", []))
        for group in scene.get("RequiresAnyGroups", []):
            flags.add(group[0])
        if scene.get("RequiresAny"):
            flags.add(scene["RequiresAny"][0])
        cases.append(dict(Id="page/" + scene["Id"], Target="", Dialog="", Page="",
                          Chapter=max(6, scene.get("MinChapter", 6)), Flags=sorted(flags),
                          NativeEligible=[], ExpectedCandidate=scene["Id"]))
    return dict(Schema=1, Evidence="synthetic final snapshots; not proof of earned campaign history",
                Cases=cases)


def make_policy(story, archive):
    specs = {k: story["NativeEpilogueEdits"][k] for k in TARGETS}
    expected = {k: "BlueprintCue" for k in TARGETS}
    for spec in specs.values():
        for field, kind in (("Page", "BlueprintBookPage"), ("Sequence", "BlueprintCueSequence"),
                            ("Parent", "Blueprint*"), ("Dialog", "BlueprintDialog")):
            if spec.get(field):
                expected[spec[field]] = kind
    records = find_bindings(archive, expected)
    return dict(Schema=1, Source="blueprints.zip; authored test metadata only", Specs=specs,
                Assets={k: records[k] for k in sorted(records)},
                ParentMutation=dict(Cue=TARGETS[0], Continue=["959237a34dfe436eb8f088b4be259daa"],
                                    Source="RanRomance SlideArue; src/NativeEpilogueEdit.cs reviewed ParentContinue"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    parser.add_argument("--archive", type=Path, default=game_dir() / "blueprints.zip")
    parser.add_argument("--output", type=Path, default=ROOT / "tests/native-cue-policy-fixtures")
    args = parser.parse_args()
    story = json.loads(args.story.read_text(encoding="utf-8-sig"))
    args.output.mkdir(parents=True, exist_ok=True)
    for name, data in (("policy.json", make_policy(story, args.archive)), ("states.json", make_cases(story))):
        (args.output / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

"""Read copies of local RRT_* saves using Writer's availability probe; never launch Wrath.

This preflight lists initial availability under both contact assumptions. It cannot prove
physical attendance, Table UI operation, spending, or later scripted choices.
"""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("saves", type=Path, help="local Saved Games directory containing RRT_*.zks")
    parser.add_argument("--probe", type=Path, required=True, help="Writer/tools/rrt_save_probe.py")
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    parser.add_argument("--cases", type=Path, default=ROOT / "harness/system-scenarios.json")
    parser.add_argument("--out", type=Path, required=True, help="report path outside the repository")
    args = parser.parse_args()
    if args.out.resolve().is_relative_to(ROOT):
        parser.error("--out must be outside the repository")
    os.environ["RRT_ROOT"] = str(ROOT)
    spec = importlib.util.spec_from_file_location("writer_save_probe", args.probe)
    probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe)
    story = json.loads(args.story.read_text(encoding="utf-8"))
    model = probe.V.Model(story)
    scenarios = json.loads(args.cases.read_text(encoding="utf-8"))["Cases"]
    scenes = {s["Id"]: s for s in model.scenes}
    report = []
    sources = sorted(args.saves.glob("RRT_*.zks"))
    if not sources:
        parser.error("No RRT_*.zks saves in the supplied directory")
    with tempfile.TemporaryDirectory(prefix="rrt-save-coverage-") as directory:
        for source in sources:
            copy = Path(directory) / source.name
            shutil.copy2(source, copy)
            player, _, _ = probe.load_save(copy)
            item = dict(Save=source.name, Chapter=player.get("Chapter"), Area=player.get("CurrentArea"), Scenarios=[])
            for case in scenarios:
                if case.get("SaveChapter", case["Chapter"]) != item["Chapter"]:
                    continue
                first = next((s for s in case["Steps"] if s.get("Available", True) and not s.get("ProbeOnly")), case["Steps"][0])
                checks = {}
                for contacts in (False, True):
                    state, _, _ = probe.snapshot(model, player, contacts)
                    checks["contacts-present" if contacts else "contacts-absent"] = (
                        probe.available(model, scenes[first["Scene"]], state) if first["Scene"] in scenes else "missing integrated scene")
                item["Scenarios"].append(dict(Id=case["Id"], System=case["System"], FirstScene=first["Scene"],
                                              Blockers=checks, Evidence="initial availability only; no scene touched"))
            report.append(item)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(report)} copied saves inspected; preflight report: {args.out}")


if __name__ == "__main__":
    main()

"""Build the harness-only probe story (E-new 0): development/Story.json plus storylines/harness_probes.PROBES.

  python tools/build-harness-probes.py [--story development/Story.json] [--out harness/probes/Story.json]
                                       [--hosts] [--game <Wrath folder>]

The output lives under harness/probes/ (gitignored) and is installed only by run-harness.ps1 -Probes; the shipped
development/Story.json never contains a probe (tests/test_chapter_zero.py checks both). --hosts also writes
harness/probes/inline-hosts.json with resolve-inline-hosts.py so -Inline can reach the probes' Prologue lists.
"""
import argparse
import copy
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from storylines.harness_probes import PROBES  # noqa: E402


def build(story):
    """The probe story: a copy of `story` with every probe appended (a probe id already present is an error)."""
    out = copy.deepcopy(story)
    have = {s["Id"] for s in out["Scenes"]}
    clash = [p["Id"] for p in PROBES if p["Id"] in have]
    if clash:
        raise ValueError("probe ids already in the story (a probe was registered in expansion.py?): %s" % clash)
    out["Scenes"].extend(copy.deepcopy(PROBES))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--story", type=Path, default=REPO / "development" / "Story.json")
    ap.add_argument("--out", type=Path, default=REPO / "harness" / "probes" / "Story.json")
    ap.add_argument("--hosts", action="store_true", help="also resolve harness/probes/inline-hosts.json")
    ap.add_argument("--game", type=Path, default=Path(r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure"))
    args = ap.parse_args()
    story = build(json.loads(args.story.read_text(encoding="utf-8")))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(story, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("HARNESS PROBE STORY (never ship): %d scenes, probes %s -> %s" % (len(story["Scenes"]), [p["Id"] for p in PROBES], args.out))
    if args.hosts:
        hosts = args.out.parent / "inline-hosts.json"
        subprocess.check_call([sys.executable, str(REPO / "harness" / "resolve-inline-hosts.py"), "--game", str(args.game),
                               "--story", str(args.out), "--out", str(hosts)])


if __name__ == "__main__":
    main()

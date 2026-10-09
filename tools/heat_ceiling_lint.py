#!/usr/bin/env python3
"""Heat ceiling: the official in-game romances never narrate positions or acts (canon-heat-reference.md).

Flags unambiguous above-canon narration in the built export. The patterns are curated against real false
positives ("thrusts the pot", "wet stone", "slick with her own blood"); characters may still talk frankly.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CEILING = re.compile(r"climbs astride|rolling astride|settles astride|straddl|between (?:her|your) thighs|slick between|where she was slick"
                     r"|nipple|hips driving into|under your belt and|rocking against|\bher sex\b|\bcock\b|moves on you", re.I)


def check(story):
    errors = []
    for scene in story["Scenes"]:
        for node in scene["Nodes"]:
            for text in [node.get("Text", "")] + [p.get("Text", "") for p in node.get("Paragraphs") or []]:
                for match in CEILING.finditer(text):
                    errors.append(f"{scene['Id']}/{node['Id']}: above the canon heat ceiling: "
                                  f"...{text[max(0, match.start() - 40):match.end() + 20]}...")
    return errors


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "development/Story.json"
    errors = check(json.loads(path.read_text(encoding="utf-8-sig")))
    for error in errors:
        print("HARD", error)
    print(f"Heat ceiling: {len(errors)} hard failures")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

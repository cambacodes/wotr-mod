#!/usr/bin/env python3
"""gate_lint.py - hard lints on how gates are written (handoff 17, Writer/handoffs/17-GATE-LINT-FINDINGS.md).

E2a singleton groups: RequiresAnyGroups / AnyGroups combine their groups with AND and each group is an OR
    (Story.cs:555 group.Any(state.Has), the same for presences, paragraphs and book entries). In a list of two or more
    groups, a one-flag group is a plain requirement: when every group has one flag the list is an AND written as groups
    ("use Requires or one OR-group"); when only some do, the one-flag group belongs in Requires.
    Checked on scenes, presences, epilogue paragraphs, book entries and book lines.
E2b implicit trio: Scene.Relationship defaults to "tirabade" (Story.cs:254), so a scene that leaves it out joins the trio
    relationship's closed/unavailable gates. Only the frozen legacy trio scenes in tools/trio-legacy-scenes.json may
    leave it out; every other scene must declare its Relationship.

Both work on the raw Story.json dict (before any defaults are filled in). Usage: python gate_lint.py [--story PATH]
"""
import argparse, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TRIO_LEGACY = HERE / "trio-legacy-scenes.json"


def gated_items(story):
    """(where, groups) for every item that carries RequiresAnyGroups or AnyGroups."""
    for s in story.get("Scenes") or []:
        yield "scene " + s["Id"], s.get("RequiresAnyGroups") or []
        for n in s.get("Nodes") or []:
            for i, p in enumerate(n.get("Paragraphs") or []):
                yield "paragraph %s/%s/%d" % (s["Id"], n["Id"], i), p.get("AnyGroups") or []
    for k, p in (story.get("Presences") or {}).items():
        yield "presence " + k, p.get("RequiresAnyGroups") or []
    for b, book in (story.get("Books") or {}).items():
        for e in book.get("Entries") or []:
            yield "book entry %s/%s" % (b, e.get("Id")), e.get("AnyGroups") or []
            for i, line in enumerate(e.get("Lines") or []):
                yield "book line %s/%s/%d" % (b, e.get("Id"), i), line.get("AnyGroups") or []


def singleton_groups(story):
    bad = []
    for where, groups in gated_items(story):
        if len(groups) < 2: continue
        single = [g[0] for g in groups if len(g) == 1]
        if len(single) == len(groups):
            bad.append("%s: every group of %s has one flag, an AND written as groups; use Requires or one OR-group" % (where, groups))
        elif single:
            bad.append("%s: one-flag group(s) %s among %d groups are plain requirements; move them to Requires" % (where, single, len(groups)))
    return bad


def load_trio_legacy(path=TRIO_LEGACY):
    return set(json.loads(Path(path).read_text(encoding="utf-8"))["scenes"])


def implicit_relationship(story, legacy):
    bad = ["scene %s: declare Relationship explicitly; the loader defaults it to tirabade (Story.cs:254)" % s["Id"]
           for s in story.get("Scenes") or [] if "Relationship" not in s and s["Id"] not in legacy]
    ids = {s["Id"] for s in story.get("Scenes") or []}
    bad += ["trio legacy list names %s, which is not a scene (the frozen list only shrinks)" % x for x in sorted(legacy - ids)]
    return bad


def check(story, legacy=None):
    return dict(singleton_groups=singleton_groups(story),
                implicit_relationship=implicit_relationship(story, load_trio_legacy() if legacy is None else legacy))


def report(res, P=print):
    n = sum(len(v) for v in res.values())
    P("\n## E2. Gate lints (handoff 17): %d hard (singleton groups %d, implicit tirabade relationship %d)"
      % (n, len(res["singleton_groups"]), len(res["implicit_relationship"])))
    for k in ("singleton_groups", "implicit_relationship"):
        for x in res[k]: P("     - HARD", x)
    return n


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--story", default=str(HERE.parent / "development/Story.json"))
    ap.add_argument("--trio-legacy", default=str(TRIO_LEGACY))
    a = ap.parse_args(argv)
    story = json.loads(Path(a.story).read_text(encoding="utf-8-sig"))
    n = report(check(story, load_trio_legacy(a.trio_legacy)))
    print("gate lint: %d hard" % n)
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""return_safety.py - static mirror of the inline-scene native return contract in src/Main.cs Build().

An inline scene (Scene.NativeReturnCue) ends by showing a native cue that must only reopen the scene's native answer list.
Main.cs (Phase 1, the "Native audience return" block) disables the whole relationship at load when the cue does anything
else, so a violation here is a relationship that silently vanishes in game. The rules, with the Main.cs lines they mirror:

  Main.cs:228-229  the cue resolves as a BlueprintCue, and the scene's single answer list resolves as a BlueprintAnswersList
  Main.cs:233      cue: ShowOnce, ShowOnceCurrentDialog false; no Conditions
  Main.cs:234      cue: no OnShow and no OnStop actions
  Main.cs:235      cue: no Continue cues; Experience == NoExperience
  Main.cs:236      cue: AlignmentShift.Value == 0; list: ShowOnce false, no Conditions
  Main.cs:238      list: MythicRequirement and AlignmentRequirement at their defaults (None)
  Main.cs:239      cue: exactly one answer, and it is the scene's answer list itself

The pass/fail rules match Writer/tools/retcheck.py (the pair-by-pair research tool); this check is additionally strict
about PrototypeLink/m_Overrides, whose inherited fields it cannot see. Entry answers are inserted before the list's last
native answer (Main.cs:518-521); rrt_verify section F reports lists whose last answer is not a leave line.

Story.cs Rules.Validate already requires exactly one AnswerLists entry for such a scene; the check repeats it because
Main.cs calls AnswerLists.Single(). NativeReturnCue is the only story field that names a native return: ReturnToList
builds its own authored return cue, and NativeNext / ContinueBefore / EpilogueAfter continue into native content
rather than return from it.

Known failures that need a design decision live in tools/return-safety-allowlist.json:
  {"<scene id>": {"cue": "<guid>", "reasons": ["<rule>", ...], "reason": "<why>", "todo": "<what decides it>"}}
An allowlisted scene must still fail with exactly the listed reasons, so a stale or widened entry is itself a failure.

Usage: python return_safety.py [--story development/Story.json] [--game DIR] [--allowlist FILE]
"""
import argparse, json, os, re, sys, zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
GAME = Path(os.environ.get("RRT_GAME_DIR") or r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure")
ALLOWLIST = HERE / "return-safety-allowlist.json"
_HEAD = re.compile(rb'"AssetId"\s*:\s*"([0-9a-f]{32})".*?"\$type"\s*:\s*"[0-9a-f]{32}, (\w+)"', re.S)


def _type(data):
    return str(data.get("$type", "")).split(", ")[-1]


def _ref(value):
    """A blueprint reference as the zip serializes it ("!bp_<guid>", a bare guid, or {"guid": ...})."""
    if isinstance(value, dict): value = value.get("guid") or value.get("m_Guid") or ""
    return str(value or "").replace("!bp_", "")


def _items(obj, key):
    return (obj or {}).get(key) or []


def _default(value, default):
    return value in (None, default, 0)


def cue_problems(cue, answer_list, list_guid):
    """Every Main.cs:233-239 rule the cue / answer-list pair breaks (empty when the return is safe)."""
    bad = []
    if cue.get("PrototypeLink") or cue.get("m_Overrides"): bad.append("cue.PrototypeLink (inherited fields cannot be checked)")
    if cue.get("ShowOnce"): bad.append("cue.ShowOnce")
    if cue.get("ShowOnceCurrentDialog"): bad.append("cue.ShowOnceCurrentDialog")
    if _items(cue.get("Conditions"), "Conditions"): bad.append("cue.Conditions")
    if _items(cue.get("OnShow"), "Actions"): bad.append("cue.OnShow")
    if _items(cue.get("OnStop"), "Actions"): bad.append("cue.OnStop")
    if _items(cue.get("Continue"), "Cues"): bad.append("cue.Continue")
    if not _default(cue.get("Experience"), "NoExperience"): bad.append("cue.Experience=%s" % cue.get("Experience"))
    if (cue.get("AlignmentShift") or {}).get("Value"): bad.append("cue.AlignmentShift")
    answers = cue.get("Answers") or []
    if len(answers) != 1: bad.append("cue.Answers=%d" % len(answers))
    elif _ref(answers[0]) != list_guid: bad.append("cue.Answers[0]=%s is not the scene's answer list" % _ref(answers[0]))
    if answer_list.get("PrototypeLink") or answer_list.get("m_Overrides"): bad.append("list.PrototypeLink (inherited fields cannot be checked)")
    if answer_list.get("ShowOnce"): bad.append("list.ShowOnce")
    if _items(answer_list.get("Conditions"), "Conditions"): bad.append("list.Conditions")
    if not _default(answer_list.get("MythicRequirement"), "None"): bad.append("list.MythicRequirement=%s" % answer_list.get("MythicRequirement"))
    if not _default(answer_list.get("AlignmentRequirement"), "None"): bad.append("list.AlignmentRequirement=%s" % answer_list.get("AlignmentRequirement"))
    return bad


def scene_problems(scene, read):
    """read(guid) -> blueprint Data dict, or None when the guid is not in blueprints.zip."""
    cue_guid, lists = scene["NativeReturnCue"], scene.get("AnswerLists") or []
    if len(lists) != 1: return ["scene has %d AnswerLists (Main.cs:229 calls AnswerLists.Single())" % len(lists)]
    cue, answer_list = read(cue_guid), read(lists[0])
    bad = []
    if cue is None: bad.append("cue not found in blueprints.zip")
    elif _type(cue) != "BlueprintCue": bad.append("cue is a %s, not a BlueprintCue" % _type(cue))
    if answer_list is None: bad.append("answer list %s not found in blueprints.zip" % lists[0])
    elif _type(answer_list) != "BlueprintAnswersList": bad.append("answer list %s is a %s" % (lists[0], _type(answer_list)))
    return bad or cue_problems(cue, answer_list, lists[0])


def check(scenes, read, allowlist):
    """Returns (failures, allowed): failures are hard; allowed are known failures matching their allowlist entry exactly."""
    failures, allowed, seen = [], [], set()
    for scene in scenes:
        if not scene.get("NativeReturnCue"): continue
        sid, cue = scene["Id"], scene["NativeReturnCue"]
        bad = scene_problems(scene, read)
        entry = allowlist.get(sid)
        if entry is not None:
            seen.add(sid)
            if entry.get("cue") != cue or sorted(entry.get("reasons") or []) != sorted(bad):
                failures.append(dict(scene=sid, cue=cue, reasons=bad or ["passes"],
                                     note="allowlist entry is stale: it lists cue %s reasons %s" % (entry.get("cue"), entry.get("reasons"))))
            else:
                allowed.append(dict(scene=sid, cue=cue, reasons=bad, reason=entry["reason"], todo=entry["todo"]))
        elif bad:
            failures.append(dict(scene=sid, cue=cue, reasons=bad))
    for sid in sorted(set(allowlist) - seen):
        failures.append(dict(scene=sid, cue=allowlist[sid].get("cue"), reasons=["allowlisted scene has no NativeReturnCue in this story"]))
    return failures, allowed


def load_allowlist(path):
    if not path or not Path(path).exists(): return {}
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    for sid, entry in data.items():
        missing = [k for k in ("cue", "reasons", "reason", "todo") if not entry.get(k)]
        if missing: raise ValueError("return-safety allowlist entry %s lacks %s" % (sid, ", ".join(missing)))
    return data


class ZipReader:
    """Reads blueprint Data by guid from blueprints.zip; builds its own AssetId index unless given one (guid -> (type, member))."""
    def __init__(self, game, index=None, zip_file=None):
        self.zip = zip_file if zip_file is not None else zipfile.ZipFile(Path(game) / "blueprints.zip")
        self.index = index
        self.cache = {}

    def _build(self):
        self.index = {}
        for info in self.zip.infolist():
            if not info.filename.endswith(".jbp"): continue
            with self.zip.open(info) as fh: m = _HEAD.search(fh.read(400))
            if m: self.index[m.group(1).decode()] = (m.group(2).decode(), info.filename)

    def __call__(self, guid):
        if self.index is None: self._build()
        if guid not in self.cache:
            hit = self.index.get(guid)
            self.cache[guid] = json.loads(self.zip.read(hit[1]).decode("utf-8-sig"))["Data"] if hit else None
        return self.cache[guid]


def report(failures, allowed, total, P=print):
    P("\n## F2. Native return safety (Main.cs:226-239): %d inline scenes, %d hard failures, %d allowlisted known failures"
      % (total, len(failures), len(allowed)))
    for f in failures:
        P("     - HARD %s cue %s: %s%s" % (f["scene"], f["cue"], "; ".join(f["reasons"]), " (" + f["note"] + ")" if f.get("note") else ""))
    for a in allowed:
        P("     - known %s cue %s: %s [%s; TODO %s]" % (a["scene"], a["cue"], "; ".join(a["reasons"]), a["reason"], a["todo"]))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--story", default=str(HERE.parent / "development/Story.json"))
    ap.add_argument("--game", default=str(GAME))
    ap.add_argument("--allowlist", default=str(ALLOWLIST))
    a = ap.parse_args(argv)
    try:
        allowlist = load_allowlist(a.allowlist)
    except ValueError as e:
        print("return safety:", e)
        return 2
    scenes = json.loads(Path(a.story).read_text(encoding="utf-8-sig"))["Scenes"]
    failures, allowed = check(scenes, ZipReader(a.game), allowlist)
    report(failures, allowed, sum(1 for s in scenes if s.get("NativeReturnCue")))
    print("return safety: %d hard" % len(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

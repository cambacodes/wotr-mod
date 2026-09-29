"""Offline host resolver for the harness -Inline mode.

For every scene that RRT attaches to a native answer list (Rules.EntryTargets: explicit AnswerLists, or the Tirabade
defaults), find the native dialog that shows the list, the cue that owns it, and the shortest answer path from the
dialog's first cue to that cue. Writes harness/inline-hosts.json, which run-harness.ps1 copies next to the harness DLL;
the runtime navigator reads the per-host answer distances from it (see HarnessRunner.DriveInline).

  python harness/resolve-inline-hosts.py [--game <Wrath folder>] [--story development/Story.json] [--out harness/inline-hosts.json]

Graph model (a lower bound on what the live game shows; conditions are recorded, not evaluated):
  cue / book page / sequence exit: its Answers (lists expanded) when it has any, else its Continue cues (one click);
  answer: its NextCue cues; check: success and fail (no click); cue sequence: its cues and its exit (no click).
"""
import argparse
import json
import re
import sys
import zipfile
from collections import defaultdict, deque
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TIRABADE_LISTS = {"Anevia": ["33960c7f7af40cd43b7f801a76c87a0b"], "Irabeth": ["871af36f2ab2b1f40b5de77976c54276"],
                  "Together": ["33960c7f7af40cd43b7f801a76c87a0b", "871af36f2ab2b1f40b5de77976c54276"]}
DIALOG_TYPES = {"BlueprintCue", "BlueprintAnswer", "BlueprintAnswersList", "BlueprintDialog", "BlueprintCueSequence",
                "BlueprintSequenceExit", "BlueprintCheck", "BlueprintBookPage"}
HEAD = re.compile(rb'"AssetId"\s*:\s*"([0-9a-f]{32})".*?"\$type"\s*:\s*"[0-9a-f]{32}, (\w+)"', re.S)
INF = 10 ** 9


def g(ref):
    """'!bp_<guid>' or '<guid>' or {'Cues': [...]} -> guid list."""
    if ref is None: return []
    if isinstance(ref, dict): ref = ref.get("Cues") or []
    if isinstance(ref, str): ref = [ref]
    return [r.replace("!bp_", "") for r in ref if isinstance(r, str) and r]


def conditioned(d, key):
    return bool(((d.get(key) or {}).get("Conditions")) or [])


def entry_targets(scene):
    """Mirror of Tirabade.Rules.EntryTargets (Story.cs); hubs and non-physical scenes have no native entry."""
    if scene.get("Remote") or scene.get("Owner") == "Memory" or (scene.get("Owner") or "").endswith("Epilogue"): return []
    if scene.get("ContinueBefore") or scene.get("InteractionHub"): return []
    if scene.get("AnswerLists"): return list(scene["AnswerLists"])
    if scene.get("Relationship", "tirabade") == "tirabade": return TIRABADE_LISTS.get(scene.get("Owner"), [])
    return []


def load(game):
    """guid -> (type, name, data) for every dialog-system blueprint in blueprints.zip."""
    out = {}
    with zipfile.ZipFile(game / "blueprints.zip") as z:
        for info in z.infolist():
            if not info.filename.endswith(".jbp"): continue
            with z.open(info) as fh: head = fh.read(400)
            m = HEAD.search(head)
            if not m or m.group(2).decode() not in DIALOG_TYPES: continue
            data = json.loads(z.read(info))["Data"]
            out[m.group(1).decode()] = (m.group(2).decode(), Path(info.filename).stem, data)
    return out


class Graph:
    def __init__(self, bps):
        self.bps = bps

    def t(self, x): return self.bps[x][0] if x in self.bps else None
    def name(self, x): return self.bps[x][1] if x in self.bps else x
    def d(self, x): return self.bps[x][2] if x in self.bps else {}

    def answers(self, holder, seen=None):
        """Answers shown for a holder's Answers field, lists expanded in order."""
        seen = seen if seen is not None else set()
        out = []
        for a in g(self.d(holder).get("Answers")):
            if a in seen: continue
            seen.add(a)
            if self.t(a) == "BlueprintAnswersList": out += self.answers(a, seen)
            elif self.t(a) == "BlueprintAnswer": out.append(a)
        return out

    def lists_held(self, holder, seen=None):
        """Every answer list a holder shows, directly or nested."""
        seen = seen if seen is not None else set()
        for a in g(self.d(holder).get("Answers")):
            if a not in seen and self.t(a) == "BlueprintAnswersList":
                seen.add(a)
                self.lists_held(a, seen)
        return seen

    def edges(self, node):
        """(label, next) pairs; label is an answer guid, 'continue' (one click) or None (automatic)."""
        t, d = self.t(node), self.d(node)
        if t in ("BlueprintCue", "BlueprintBookPage", "BlueprintSequenceExit"):
            ans = self.answers(node)
            if ans: return [(a, c) for a in ans for c in g(self.d(a).get("NextCue"))] + [(a, None) for a in ans if not g(self.d(a).get("NextCue"))]
            return [("continue", c) for c in g(d.get("Continue"))]
        if t == "BlueprintCheck": return [(None, c) for c in g(d.get("m_Success")) + g(d.get("m_Fail"))]
        if t == "BlueprintCueSequence": return [(None, c) for c in g(d.get("Cues")) + g(d.get("m_Exit"))]
        return []

    def dialog_of(self, x):
        # A SequenceExit has no ParentAsset; it belongs to the CueSequence whose m_Exit names it.
        if not hasattr(self, "_exit_owner"):
            self._exit_owner = {e: s for s, (t, _, d) in self.bps.items() if t == "BlueprintCueSequence" for e in g(d.get("m_Exit"))}
        seen = set()
        while x in self.bps and x not in seen:
            if self.t(x) == "BlueprintDialog": return x
            seen.add(x)
            x = (self.d(x).get("ParentAsset") or "").replace("!bp_", "") or self._exit_owner.get(x, "")
        return None

    def speaker(self, cue):
        return ((self.d(cue).get("Speaker") or {}).get("m_Blueprint") or "").replace("!bp_", "") or None


def resolve_host(gr, dialog, owners):
    """Shortest click path from the dialog's first cues to any owner cue, plus answer distances for the navigator."""
    firsts = g(gr.d(dialog).get("FirstCue"))
    # Forward reachable set.
    reach, q = set(firsts), deque(firsts)
    while q:
        n = q.popleft()
        for _, m in gr.edges(n):
            if m and m not in reach: reach.add(m); q.append(m)
    # Backward relaxation: dist(node) = clicks needed from node's display to a cue showing the list.
    dist = {n: (0 if n in owners else INF) for n in reach}
    changed = True
    while changed:
        changed = False
        for n in reach:
            if dist[n] == 0: continue
            best = INF
            for label, m in gr.edges(n):
                if m is None: continue
                cost = dist.get(m, INF) + (0 if label is None else 1)
                best = min(best, cost)
            if best < dist[n]: dist[n] = best; changed = True
    answer_dist = {}
    for n in reach:
        for label, m in gr.edges(n):
            if label and label != "continue" and m is not None and dist.get(m, INF) < INF:
                answer_dist[label] = min(answer_dist.get(label, INF), dist[m] + 1)
    start = min(firsts, key=lambda c: dist.get(c, INF), default=None)
    if start is None or dist.get(start, INF) >= INF:
        why = "owning cue not reachable from the dialog's first cue" if firsts else "dialog has no first cue"
        return {"reachable": False, "reason": why, "answerDist": {}}
    # Walk one shortest path for the log.
    path, n, guard = [], start, 0
    while dist[n] > 0 and guard < 200:
        guard += 1
        step = None
        for label, m in gr.edges(n):
            if m is None: continue
            if dist.get(m, INF) + (0 if label is None else 1) == dist[n]: step = (label, m); break
        if step is None: break
        label, m = step
        item = {"at": gr.name(n), "take": "auto" if label is None else ("continue" if label == "continue" else gr.name(label))}
        if label not in (None, "continue") and (conditioned(gr.d(label), "ShowConditions") or conditioned(gr.d(label), "SelectConditions")):
            item["conditioned"] = True
        if conditioned(gr.d(m), "Conditions"): item["nextConditioned"] = True
        path.append(item)
        n = m
    return {"reachable": True, "clicks": dist[start], "path": path, "answerDist": {k: v for k, v in sorted(answer_dist.items())}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", type=Path, default=Path(r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure"))
    ap.add_argument("--story", type=Path, default=REPO / "development" / "Story.json")
    ap.add_argument("--out", type=Path, default=REPO / "harness" / "inline-hosts.json")
    args = ap.parse_args()
    story = json.loads(args.story.read_text(encoding="utf-8"))
    gr = Graph(load(args.game))

    scenes, wanted = {}, set()
    for s in story["Scenes"]:
        lists = entry_targets(s)
        if not lists: continue
        kind = "return-cue" if s.get("NativeReturnCue") else "return-to-list" if s.get("ReturnToList") else "dialog"
        scenes[s["Id"]] = {"kind": kind, "lists": lists, "explicit": bool(s.get("AnswerLists")), "contact": s.get("ContactUnit"),
                           "entry": {l: "RRT_entry." + s["Id"] + ("." + l if kind == "return-to-list" else "") for l in lists}}
        wanted.update(lists)

    # Owning cues: every cue-like blueprint whose Answers hold the list (directly or through a nested list).
    holders = defaultdict(list)
    for guid, (t, _, d) in gr.bps.items():
        if t in ("BlueprintCue", "BlueprintBookPage", "BlueprintSequenceExit") and d.get("Answers"):
            for lst in gr.lists_held(guid) & wanted: holders[lst].append(guid)

    hosts = {}
    for lst in sorted(wanted):
        entry = {"list": lst, "listName": gr.name(lst), "hosts": []}
        if gr.t(lst) != "BlueprintAnswersList":
            entry["reason"] = "list is not in blueprints.zip (parent-mod or runtime list)" if lst not in gr.bps else "not a BlueprintAnswersList"
            hosts[lst] = entry
            continue
        by_dialog = defaultdict(list)
        for cue in holders.get(lst, []):
            dlg = gr.dialog_of(cue)
            if dlg: by_dialog[dlg].append(cue)
        # The list's ParentAsset is its owning cue; list it first.
        parent = (gr.d(lst).get("ParentAsset") or "").replace("!bp_", "")
        for owners in by_dialog.values(): owners.sort(key=lambda c: c != parent)
        if not by_dialog: entry["reason"] = "no cue in any dialog shows this list"
        for dlg, owners in sorted(by_dialog.items()):
            firsts = g(gr.d(dlg).get("FirstCue"))
            h = {"dialog": dlg, "dialogName": gr.name(dlg), "cues": owners, "cueNames": [gr.name(c) for c in owners],
                 "speaker": next((sp for sp in [gr.speaker(c) for c in firsts + owners] if sp), None)}
            h.update(resolve_host(gr, dlg, set(owners)))
            entry["hosts"].append(h)
        # Reachable hosts first, then fewest clicks.
        entry["hosts"].sort(key=lambda h: (not h["reachable"], h.get("clicks", INF), h["dialogName"]))
        hosts[lst] = entry

    resolved = 0
    for sid, s in scenes.items():
        ok = [l for l in s["lists"] if any(h["reachable"] for h in hosts[l]["hosts"])]
        s["resolved"] = bool(ok)
        if ok:
            resolved += 1
            h = next(h for h in hosts[ok[0]]["hosts"] if h["reachable"])
            s["host"] = {"list": ok[0], "dialog": h["dialog"], "dialogName": h["dialogName"], "cue": h["cueNames"][0], "clicks": h["clicks"]}
        else:
            s["reason"] = "; ".join(l[:8] + ": " + (hosts[l].get("reason") or "no reachable host (" + ", ".join(
                h["dialogName"] + " " + h["reason"] for h in hosts[l]["hosts"]) + ")") for l in s["lists"])

    inline = {k: v for k, v in scenes.items() if v["kind"] != "dialog"}
    summary = {
        "entryTargetScenes": len(scenes), "resolved": resolved,
        "inlineOnlyScenes": len(inline), "inlineOnlyResolved": sum(v["resolved"] for v in inline.values()),
        "answerListScenesWithoutContact": sum(1 for v in scenes.values() if v["explicit"] and not v["contact"]),
        "answerListScenesWithoutContactResolved": sum(1 for v in scenes.values() if v["explicit"] and not v["contact"] and v["resolved"]),
        "lists": len(hosts), "listsWithReachableHost": sum(any(h["reachable"] for h in e["hosts"]) for e in hosts.values()),
    }
    out = {"generatedFrom": {"story": args.story.name, "blueprints": str(args.game / "blueprints.zip")},
           "summary": summary, "scenes": dict(sorted(scenes.items())), "lists": hosts}
    args.out.write_bytes((json.dumps(out, indent=1, sort_keys=False) + "\n").encode("utf-8"))
    print("inline hosts: %(resolved)d/%(entryTargetScenes)d entry-target scenes resolve to a host "
          "(inline-only %(inlineOnlyResolved)d/%(inlineOnlyScenes)d; explicit AnswerLists without ContactUnit "
          "%(answerListScenesWithoutContactResolved)d/%(answerListScenesWithoutContact)d); lists %(listsWithReachableHost)d/%(lists)d reachable" % summary)
    for sid, s in sorted(scenes.items()):
        if not s["resolved"]: print("  unresolved %s [%s]: %s" % (sid, s["kind"], s["reason"]))
    print("wrote " + str(args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())

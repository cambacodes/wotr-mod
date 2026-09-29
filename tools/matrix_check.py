#!/usr/bin/env python3
"""matrix_check.py - structural gate for handoffs/trickster-matrix.json (02-TRICKSTER-ENGINE-API.md section 4).

Objective checks only; it never judges prose. For every character it lists each missing or malformed field, per
state and per scene object, then prints a summary table. Exit code 1 when any checked character has a problem.

Checked per device state (a state with a setup, fallback_setup or payoff scene object):
  ids        every scene id is <rel>.trickster.<state>.<beat> (rel = one of the character's relationship ids)
  chapters   min_chapter / max_chapter are integers (min <= max); chapters[] optional, integers inside the window
  delay      delay_hours is an integer >= 0
  delivery   physical: answer_lists[] GUIDs, or contact_unit GUID + areas[] GUIDs; remote: remote: true; epilogue: owner
  gates      setup requires live `trickster`; fallback_setup requires `trickster` or `trickster.ever`; payoff requires
             `trickster.ever` plus <rel>.trickster.primed / .returned* when the state has a setup
  bindings   every key read (detect all/none, requires, forbids, requires_any_groups) is bound in top-level bindings{}
             with key + 32-hex GUID + kind, or is a latch / derived / runtime key, or is set by the matrix, or exists in
             Story.json (--story)
  cost       cost.flags[] non-empty, each <rel>.trickster.cost.<name>; cost.read_by[] non-empty
  test       rules_test {name, world[], expect_available[], after_choice{scene, choice:int}, expect_flags[],
             committed_flag_reachable} (v1: an `acceptance` string "world {..} -> .. available; after choice N -> flags {..};
             CommittedFlag reachable")
  reactions  >= 2 per device state, each {reactor, answer_list GUID | remote: true, requires[], gist}
  todo       no open TODO(B) marker anywhere in the character (use --allow-todo to report without failing)
Characters with relationship_status pending-signoff are reported and skipped.

Runtime-rule mode (--rules, see tools/matrix_rules.py): checks every scene object against what Rules.Validate and
Main.Build enforce, reading blueprints.zip from --game: inline native_return_cue safety, native_next type/terminal/
same-dialog, no mythic/alignment on epilogues, trickster_device for scenes that must run while their relationship's own
unavailable flag holds, remove_item whitelist. Each finding is FATAL (whole mod disabled), DEGRADES (relationship
disabled), BLOCKED (scene never available) or GATE (build gate fails). It also executes every state's rules_test against
the matrix compiled into Rules-compatible scenes (rrt_verify's Python port of Rules.Available: Derived, Latches,
UnavailableOverrides, ForbidOverrides, TricksterDevice, RequiresAnyGroups) -> TEST; checks each relationship has a
CommittedFlag producer -> ROUTE; lints singleton requires_any_groups (DEGRADES), delays anchored on unstamped native keys,
scene/choice sets contradictions and textless node references (WARN). Exit 1 on any finding except WARN.

Usage: python tools/matrix_check.py [MATRIX] [--story development/Story.json] [--json OUT] [--allow-todo] [--quiet]
       python tools/matrix_check.py [MATRIX] --rules [--game DIR] [--json OUT] [--quiet]
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUID = re.compile(r"^[0-9a-f]{32}$")
KINDS = {"Etudes", "CompletedEtudes", "CompletedQuests", "SeenCues", "SelectedAnswers", "StartedDialogs",
         "UnlockableFlags", "QuestObjectives", "InventoryItems", "StartedQuests", "MainCharacterFacts"}
RUNTIME = {"trickster.ever", "loss", "ascended", "inhuman", "chapter_one", "chapter_later",
           # runtime contact evidence (Rules.Validate contactEvidence)
           "konomi.missed_contact_available", "konomi.missed_contact_invalidated", "konomi.retained_dead", "konomi.retained_hostile",
           "konomi.return_contact_available", "konomi.return_correspondence_available",
           "irabeth.return_correspondence_available", "irabeth.return_meeting_arrived",
           "nurah.correspondence_available", "nurah.meeting_arrived"}
RUNTIME_PREFIX = ("revive.", "served.", "rrt.degraded.")
TODO = re.compile(r"TODO\(B\)")


def is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def rel_ids(c):
    raw = (c.get("relationship_id") or "").split("(renamed")[0]
    return re.findall(r"[a-z][a-z0-9_]*(?:\.[a-z0-9_]+)*", raw)


def states_of(c):
    return c.get("states") or c.get("native_states") or []


def story_keys(path):
    if not path or not Path(path).is_file():
        return set()
    story = json.loads(Path(path).read_text(encoding="utf-8"))
    keys = set()
    for sec in ("Etudes", "CompletedEtudes", "CompletedQuests", "SeenCues", "SelectedAnswers", "StartedDialogs",
                "UnlockableFlags", "QuestObjectives", "InventoryItems", "StartedQuests", "MainCharacterFacts", "Latches", "Derived"):
        keys |= set((story.get(sec) or {}).keys())
    for s in story.get("Scenes", []):
        keys.add(s["Id"])
        for n in s.get("Nodes", []):
            for ch in n.get("Choices", []):
                keys |= set(ch.get("Set") or [])
    for r in (story.get("Relationships") or {}).values():
        keys |= {r.get("StartedFlag"), r.get("ClosedFlag"), r.get("CommittedFlag")}
    return keys


def check_character(c, matrix, known, allow_todo):
    """Returns (problems[list of (where, message)], todo_count, device_state_count)."""
    probs = []
    rels = rel_ids(c)
    rel_rx = "(?:%s)" % "|".join(re.escape(r) for r in rels) if rels else "(?!)"
    id_rx = re.compile(r"^%s\.trickster\.[a-z0-9_]+\.[a-z0-9_]+$" % rel_rx)
    cost_rx = re.compile(r"^%s\.trickster\.cost\.[a-z0-9_]+$" % rel_rx)
    primed_rx = re.compile(r"^%s\.trickster\.(primed|returned)(_[a-z0-9_]+)?$" % rel_rx)
    bindings = matrix.get("bindings") or {}
    derived = set((matrix.get("derived") or {}).keys()) | set((matrix.get("latches") or {}).keys())
    produced = set()
    for x in matrix.get("characters", []):
        for st in states_of(x):
            for k in ("setup", "fallback_setup", "payoff"):
                v = st.get(k)
                if isinstance(v, dict):
                    produced.add(v.get("id"))
                    produced |= set(v.get("sets") or [])
                    ch = v.get("choice")
                    for choice in (ch if isinstance(ch, list) else [ch] if isinstance(ch, dict) else []):
                        produced |= set(choice.get("sets") or [])
            produced |= set((st.get("cost") or {}).get("flags") or [])
    for key in ("relationship_id", "relationship_status"):
        if not c.get(key): probs.append(("character", "missing " + key))
    if "rotation_key" in matrix.get("characters", [{}])[0] and not c.get("rotation_key"):
        probs.append(("character", "missing rotation_key"))
    if not isinstance(c.get("forbids_never", []), list):
        probs.append(("character", "forbids_never must be a list of flags"))

    def bound(key, where):
        k = key[1:] if key.startswith("!") else key
        if k in bindings:
            b = bindings[k]
            if not isinstance(b, dict) or not GUID.match(str(b.get("guid", ""))) or b.get("kind") not in KINDS:
                probs.append((where, "binding %s needs key + 32-hex guid + kind in %s (has %s/%s)" % (k, sorted(KINDS), b.get("guid"), b.get("kind"))))
            return
        if k in derived or k in RUNTIME or k.startswith(RUNTIME_PREFIX) or k in produced or k in known:
            return
        probs.append((where, "unbound key %s (not in bindings{}, latches, derived, runtime keys, matrix sets or Story.json)" % k))

    devices = 0
    for st in states_of(c):
        name = st.get("state", "?")
        det = st.get("detect") or {}
        if isinstance(det, dict):
            for k in list(det.get("all", [])) + list(det.get("none", [])) + list(det.get("story_keys", [])):
                bound(k, "%s/detect" % name)
        objs = [(k, st.get(k)) for k in ("setup", "fallback_setup", "payoff") if isinstance(st.get(k), dict)]
        v1_ids = [st.get(k) for k in ("setup_scene_id", "device_scene_id") if st.get(k)]
        if not objs and not v1_ids:
            continue
        devices += 1
        has_setup = any(k in ("setup", "fallback_setup") for k, _ in objs) or bool(st.get("setup_scene_id"))
        for sid in v1_ids:
            if not id_rx.match(sid): probs.append((name, "scene id %s is not <rel>.trickster.<state>.<beat>" % sid))
        if v1_ids:
            probs.append((name, "v1 state: needs scene objects (setup/payoff) with min_chapter, max_chapter, delay_hours, delivery"))
        for role, o in objs:
            where = "%s/%s %s" % (name, role, o.get("id", "?"))
            if not id_rx.match(str(o.get("id", ""))):
                probs.append((where, "id is not <rel>.trickster.<state>.<beat> with rel in %s" % rels))
            lo, hi = o.get("min_chapter"), o.get("max_chapter")
            if not is_int(lo) or not is_int(hi):
                probs.append((where, "min_chapter/max_chapter must be integers (have %r/%r)" % (lo, hi)))
            elif lo > hi:
                probs.append((where, "min_chapter %d > max_chapter %d" % (lo, hi)))
            if "chapters" in o and (not isinstance(o["chapters"], list) or not all(is_int(x) for x in o["chapters"])
                                    or (is_int(lo) and is_int(hi) and any(x < lo or x > hi for x in o["chapters"]))):
                probs.append((where, "chapters[] must be integers inside min..max"))
            if not is_int(o.get("delay_hours")) or o.get("delay_hours") < 0:
                probs.append((where, "delay_hours must be an integer >= 0 (have %r)" % o.get("delay_hours")))
            kind = o.get("kind")
            if kind == "remote" or o.get("remote") is True:
                if o.get("remote") is not True: probs.append((where, "remote scene needs remote: true"))
            elif kind == "epilogue":
                if not o.get("owner"): probs.append((where, "epilogue scene needs owner"))
            else:
                lists = o.get("answer_lists") or []
                unit, areas = o.get("contact_unit"), o.get("areas") or []
                ok_lists = bool(lists) and all(GUID.match(str(g)) for g in lists)
                ok_unit = bool(unit) and GUID.match(str(unit)) and bool(areas) and all(GUID.match(str(g)) for g in areas)
                if not ok_lists and not ok_unit:
                    probs.append((where, "physical scene needs answer_lists[] GUIDs, or contact_unit GUID + areas[] GUIDs (or remote: true)"))
            req = list(o.get("requires") or [])
            if role == "setup" and "trickster" not in req:
                probs.append((where, "setup must require live 'trickster'"))
            if role == "fallback_setup" and not ({"trickster", "trickster.ever"} & set(req)):
                probs.append((where, "fallback_setup must require 'trickster' or 'trickster.ever'"))
            if role == "payoff":
                if "trickster.ever" not in req:
                    probs.append((where, "payoff must require 'trickster.ever' (not the live 'trickster')"))
                if has_setup and not any(primed_rx.match(k) for k in req):
                    probs.append((where, "payoff must require <rel>.trickster.primed or .returned"))
            for k in req + list(o.get("forbids") or []) + [x for g in (o.get("requires_any_groups") or []) for x in g]:
                bound(k, where)
            for g in ([o["native_next"]] if o.get("native_next") else []) + ([o["native_return_cue"]] if o.get("native_return_cue") else []):
                if not GUID.match(str(g)): probs.append((where, "native cue %r is not a 32-hex GUID" % g))
        cost = st.get("cost")
        if isinstance(cost, dict):
            flags = cost.get("flags") or []
            if not flags: probs.append((name, "cost.flags[] is empty (R4: every trick leaves a scar)"))
            for f in flags:
                if not cost_rx.match(f): probs.append((name, "cost flag %s is not <rel>.trickster.cost.<name>" % f))
            if not cost.get("read_by"): probs.append((name, "cost.read_by[] is empty (a later scene or ending must read the cost)"))
        elif st.get("cost_flag"):
            if not cost_rx.match(st["cost_flag"]): probs.append((name, "cost flag %s is not <rel>.trickster.cost.<name>" % st["cost_flag"]))
        else:
            probs.append((name, "missing cost {flags[], read_by[]}"))
        rt = st.get("rules_test")
        if isinstance(rt, dict):
            for f, ok in (("name", bool(rt.get("name"))), ("world[]", isinstance(rt.get("world"), list) and bool(rt.get("world"))),
                          ("expect_available[]", isinstance(rt.get("expect_available"), list) and bool(rt.get("expect_available"))),
                          ("after_choice{scene, choice:int}", isinstance(rt.get("after_choice"), dict) and bool(rt["after_choice"].get("scene"))
                           and is_int(rt["after_choice"].get("choice"))),
                          ("expect_flags[]", isinstance(rt.get("expect_flags"), list) and bool(rt.get("expect_flags"))),
                          ("committed_flag_reachable", bool(rt.get("committed_flag_reachable")))):
                if not ok: probs.append((name, "rules_test missing " + f))
        elif isinstance(st.get("acceptance"), str):
            if not re.search(r"world\s*\{.*\}.*available.*after choice.*flags\s*\{.*\}.*CommittedFlag reachable", st["acceptance"], re.I | re.S):
                probs.append((name, "acceptance string lacks 'world {..} -> X available; after choice N -> flags {..}; CommittedFlag reachable'"))
        else:
            probs.append((name, "missing rules_test (acceptance test)"))
        reactions = st.get("reactions")
        if reactions is None and isinstance(c.get("reactions"), list):
            reactions = c["reactions"]
        reactions = reactions or []
        if len(reactions) < 2:
            probs.append((name, "needs >= 2 reactions (has %d)" % len(reactions)))
        for i, r in enumerate(reactions):
            if not isinstance(r, dict):
                probs.append((name, "reaction %d is not an object {reactor, answer_list|remote, requires, gist}" % i)); continue
            miss = [f for f in ("reactor", "gist") if not r.get(f)]
            if not isinstance(r.get("requires"), list) or not r.get("requires"): miss.append("requires[]")
            if not (r.get("remote") is True or GUID.match(str(r.get("answer_list", "")))): miss.append("answer_list GUID | remote: true")
            if miss: probs.append((name, "reaction %d (%s) missing %s" % (i, r.get("reactor", "?"), ", ".join(miss))))
    todo = len(TODO.findall(json.dumps(c, ensure_ascii=False)))
    if todo and not allow_todo:
        probs.append(("character", "%d open TODO(B) marker(s)" % todo))
    return probs, todo, devices


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("matrix", nargs="?", default=str(ROOT.parents[1] / "handoffs/trickster-matrix.json"))
    ap.add_argument("--story", default=str(ROOT / "development/Story.json"), help="Story.json whose keys count as known")
    ap.add_argument("--json", help="write the per-character findings here")
    ap.add_argument("--allow-todo", action="store_true", help="report open TODO(B) markers without failing on them")
    ap.add_argument("--quiet", action="store_true", help="summary table only")
    ap.add_argument("--rules", action="store_true", help="runtime-rule mode (validate_rules); exit 1 on any finding")
    ap.add_argument("--game", default=r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure",
                    help="game folder whose blueprints.zip the --rules checks read")
    a = ap.parse_args()
    try:   # matrix text carries arrows and em dashes; never crash a Windows console on them
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    matrix = json.loads(Path(a.matrix).read_text(encoding="utf-8"))
    if a.rules:
        import matrix_rules
        story = json.loads(Path(a.story).read_text(encoding="utf-8")) if a.story and Path(a.story).is_file() else {}
        results = matrix_rules.validate_rules(matrix, matrix_rules.Archive(a.game), story)
        for name, more in matrix_rules.run_rules_tests(matrix, story).items():
            results.setdefault(name, []).extend(more)
        total = matrix_rules.print_rules(results, a.quiet)
        if a.json:
            Path(a.json).write_text(json.dumps({k: [dict(severity=s, where=w, message=m) for s, w, m in v] for k, v in results.items()},
                                               indent=1, ensure_ascii=False), encoding="utf-8")
        sys.exit(1 if total else 0)
    known = story_keys(a.story)
    out, rows = {}, []
    print("# matrix_check: %s (%s, %d characters); known Story.json keys: %d"
          % (a.matrix, matrix.get("schema", "?"), len(matrix.get("characters", [])), len(known)))
    for c in matrix.get("characters", []):
        name = c.get("character", "?")
        status = str(c.get("relationship_status", ""))
        if status.startswith("pending"):
            rows.append((name, status, 0, 0, 0, "SKIP (%s)" % status))
            continue
        probs, todo, devices = check_character(c, matrix, known, a.allow_todo)
        verdict = "PASS" if not probs else "FAIL"
        rows.append((name, status, devices, len(probs), todo, verdict))
        out[name] = dict(status=status, device_states=devices, todo=todo, problems=["%s: %s" % p for p in probs])
        if not a.quiet:
            print("\n== %s (%s) [%s]: %s, %d device state(s), %d problem(s), %d TODO(B)"
                  % (name, c.get("relationship_id"), status, verdict, devices, len(probs), todo))
            last = None
            for where, msg in probs:
                if where != last: print("   %s" % where); last = where
                print("      - %s" % msg)
    print("\n%-22s %-26s %8s %9s %6s  %s" % ("character", "status", "devices", "problems", "todo", "verdict"))
    print("-" * 84)
    for r in rows: print("%-22s %-26s %8d %9d %6d  %s" % (r[0][:22], r[1][:26], r[2], r[3], r[4], r[5]))
    failing = [r for r in rows if r[5] == "FAIL"]
    print("-" * 84)
    print("%d characters: %d PASS, %d FAIL, %d SKIP" % (len(rows), sum(r[5] == "PASS" for r in rows), len(failing),
                                                      sum(r[5].startswith("SKIP") for r in rows)))
    if a.json: Path(a.json).write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    sys.exit(1 if failing else 0)


if __name__ == "__main__":
    main()

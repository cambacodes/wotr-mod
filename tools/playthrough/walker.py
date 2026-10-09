r"""walker.py: deterministic playthrough walker over the committed export.

    python tools/playthrough/walker.py --policy trickster_all_romance [--out DIR]
    python tools/playthrough/walker.py --all

Runs the repo's E9 campaign simulator (tools/rrt_verify.simulate_rest_budget: Rules.Available / sim_play mirrors,
unchanged) under a named player POLICY from policies.json and writes runs/<policy>/trace.json: an ordered list of
events (world changes from natives/derived composites, and scene visits with chapter, day, node path, chosen choice
index + text, visible paragraph indices, flags set). The trickster_all_romance policy uses the ideal-run kit
(tools/ideal-run-kit: natives/, w6/, avoid.txt) exactly as final_sim.py does. Other policies replace only the
player's choice scoring (same traversal, same Requires/Forbids/EnterSet/crusade/check semantics as sim_plan) and the
scheduled native world. Only the export (development/Story.json) is read; no game install is needed.
Each policy runs in its own process (memory), with PYTHONHASHSEED=0 (determinism).
"""
import argparse, collections, glob, inspect, json, os, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
KIT = ROOT / "tools" / "ideal-run-kit"
NEVER = "__player_never_takes_this__"


def reexec_if_needed():
    if os.environ.get("PYTHONHASHSEED") == "0" and os.environ.get("PYTHONUTF8") == "1": return
    env = dict(os.environ, PYTHONHASHSEED="0", PYTHONUTF8="1")
    sys.exit(subprocess.run([sys.executable, str(Path(__file__).resolve())] + sys.argv[1:], env=env).returncode)


def load_kit():
    """The ideal-run kit, parsed exactly as final_sim.py parses it."""
    SKIP = {"seelah.trickster.dismissed.setup", "camellia.trickster.killed.setup_hub", "camellia.trickster.killed.setup_q3",
            "camellia.trickster.killed.setup_q1"}
    avoid_flags = set(open(KIT / "avoid.txt", encoding="utf-8").read().split()) | {
        "soana.friendship_chosen", "soana.courtship_waiting", "soana.later_friends", "soana.late_friends", "soana.friendship_kept",
        "soana.later_friend_evening"}
    avoid_text = {"\"It's worth a joke.", "[Put a deposit on the house special]", "\"Let her stay gone.\"", "[Kneel] \"I'm yours. Send her home.\""}
    plain, timed, never, banned, after, off = {}, {}, set(), [], {}, set()
    for fn in sorted(glob.glob(str(KIT / "natives" / "*.txt"))):
        if os.path.basename(fn).startswith("_"): continue
        for line in open(fn, encoding="utf-8"):
            s = line.strip()
            if s.startswith("#@"): s = s[2:].strip()
            raw = s.split("  #")[0].strip() if s.startswith("-choice") else s.split("#")[0].strip()
            if not raw: continue
            if raw.startswith("-choice "): banned.append(raw.split()[1]); continue
            if raw.startswith("!"): never.add(raw[1:].split(":")[0].strip()); continue
            k, v = raw.rsplit(":", 1); k = k.strip(); v = v.strip()
            if "+" in v:
                c, d = v.split("+"); timed[k] = (int(c), float(d)); continue
            plain[k] = min(plain.get(k, int(v)), int(v))
    for fn in glob.glob(str(KIT / "w6" / "*.extra.txt")):
        for line in open(fn, encoding="utf-8"):
            line = line.split("#")[0].strip()
            if not line: continue
            if line.startswith("!"): SKIP.add(line[1:].strip()); continue
            if "@" in line: k, sc = line.split("@", 1); after.setdefault(sc.strip(), []).append(k.strip()); continue
            k, v = line.rsplit(":", 1)
            if int(v) < 0: off.add(k.strip())
    for k in list(plain):
        if k in timed or k in never or k in off: plain.pop(k)
    for ks in after.values():
        for k in ks: plain.pop(k, None); timed.pop(k, None)
    return dict(skip=SKIP, avoid_flags=avoid_flags, avoid_text=avoid_text, plain=plain, timed=timed, never=never,
                banned=banned, after=after, off=off)


def completes_path(path):
    if not path: return False
    last = path[-1]
    return not last["Abort"] and last.get("Check") is None and last["Next"] is None


def make_policy_planner(V, policy, rel_flags_all, model):
    """Same traversal as rrt_verify.sim_plan (depth 80), with the policy's objective tuple."""
    rules = []
    for r in policy.get("rules", []):
        rules.append((r.get("alignment"), re.compile(r["text"]) if r.get("text") else None,
                      re.compile(r["set"]) if r.get("set") else None, int(r["weight"])))
    pursue = policy.get("pursue", [])
    pursued_rels = set(model.rels) if pursue == "*" else set(pursue)
    committed_pursued = {model.rels[r]["CommittedFlag"] for r in pursued_rels if r in model.rels}
    committed_all, closed = rel_flags_all["committed"], rel_flags_all["closed"]
    weights = {}

    def weight(c):
        w = weights.get(id(c))
        if w is None:
            w = 0
            for align, text, sset, wt in rules:
                if align and c.get("Alignment") and align in c["Alignment"].get("Direction", ""): w += wt * int(c["Alignment"].get("Value", 1))
                if text and text.search(c["Text"]): w += wt
                if sset and any(sset.search(f) for f in c["Set"]): w += wt
            weights[id(c)] = w
        return w

    def score(keys, got, w, done, depth):
        out = []
        for k in keys:
            if k == "commit": out.append(0 if got & committed_pursued else 1)
            elif k == "no_commit": out.append(1 if got & committed_all else 0)
            elif k == "closures": out.append(len(got & closed))
            elif k == "closures_desc": out.append(-len(got & closed))
            elif k == "weight": out.append(-w)
            elif k == "complete": out.append(0 if done else 1)
            elif k == "depth": out.append(depth)
            else: raise ValueError("unknown objective key " + k)
        return tuple(out)

    def plan(model_, s, st, rel_flags):
        keys = policy["objective_pursued"] if s["Relationship"] in pursued_rels else policy["objective_other"]
        nodes = model_.nodes[s["Id"]]
        worst = score(keys, set(), -10 ** 6, False, 10 ** 6)

        def best(node, held, gained, depth, resources, w):
            if node not in nodes or depth > 80: return worst, []
            found = None
            entries = set(nodes[node].get("EnterSet", []))
            gained, held = gained | (entries - held), held | entries
            for c in nodes[node]["Choices"]:
                if not all(f in held for f in c["Requires"]) or any(f in held for f in c["Forbids"]): continue
                cost = c.get("Crusade")
                balances = None if resources is None else dict(resources)
                if cost:
                    if cost["Amount"] < 0 and (V.payment_key(s, c) in held or balances is None
                            or balances.get(cost["Resource"], 0) + cost["Amount"] < 0): continue
                    if balances is not None: balances[cost["Resource"]] = balances.get(cost["Resource"], 0) + cost["Amount"]
                now, got = held | set(c["Set"]), gained | (set(c["Set"]) - held)
                nw = w + weight(c)
                nxt = c["Check"]["Success"] if c.get("Check") else c["Next"]
                if c["Abort"]: sc, path = score(keys, got, nw, False, depth), []
                elif nxt is None: sc, path = score(keys, got, nw, True, depth), []
                else: sc, path = best(nxt, now, got, depth + 1, balances, nw)
                if found is None or sc < found[0]: found = (sc, [c] + path)
            return found or (worst, [])

        return best(s["Nodes"][0]["Id"] if s["Nodes"] else None, set(st.flags), set(), 0, st.crusade_resources, 0)

    def wanted_for(rel):
        return policy.get("wanted_pursued" if rel in pursued_rels else "wanted_other", "romance")

    return plan, wanted_for


def run_policy(name, policies, out_dir):
    sys.path.insert(0, str(ROOT / "tools"))
    import rrt_verify as V
    policy = policies["policies"][name]
    story = json.load(open(ROOT / "development/Story.json", encoding="utf-8"))
    model = V.Model(story)
    kitcfg = policy.get("kit", {})
    kit = load_kit() if any(kitcfg.values()) else None
    plain, timed, never, after = {}, {}, set(), {}
    skip = set()
    if kit and kitcfg.get("natives"):
        plain, timed, never, after = dict(kit["plain"]), dict(kit["timed"]), set(kit["never"] | kit["off"]), kit["after"]
        for k in kit["off"] | {k for ks in after.values() for k in ks}: model.native.pop(k, None)
        if kitcfg.get("natives_exclude"):
            # Kit natives are observed on the Trickster ideal run; another path keeps only the path-neutral progress keys.
            drop = re.compile(kitcfg["natives_exclude"])
            for d in (plain, timed): [d.pop(k) for k in list(d) if drop.search(k)]
            after = {sc: [k for k in ks if not drop.search(k)] for sc, ks in after.items()}
    if kit and kitcfg.get("skip"): skip = set(kit["skip"])
    forced_on = {k: int(v) for k, v in (policy.get("natives_on") or {}).items()}
    bad = set(forced_on) - set(model.native)
    if bad: raise ValueError("policy %s schedules non-native flags: %s" % (name, ", ".join(sorted(bad))))
    for k in forced_on: never.discard(k); timed.pop(k, None)
    plain.update(forced_on)
    # Player bans: data only, as in final_sim.py (a ban is an unsatisfiable Requires).
    if kit and kitcfg.get("bans"):
        for b in kit["banned"]:
            sid, nid, i = b.rsplit("/", 2)
            c = model.nodes[sid][nid]["Choices"][int(i)]
            c["Requires"] = list(c["Requires"]) + [NEVER]
    if kit and kitcfg.get("avoid_text"):
        for s in model.scenes:
            for n in s["Nodes"]:
                for c in n["Choices"]:
                    if c["Text"].strip() in kit["avoid_text"]: c["Requires"] = list(c["Requires"]) + [NEVER]
    mythic = policy["mythic"]
    mythic_enum = "PlayerIs" + mythic.capitalize()
    unlocked = mythic.capitalize() + "Unlocked"
    if policy.get("enforce_mythic"):
        # Rules gate a choice's Mythic and a scene's EntryMythic by the player's path; the E9 mirror ignores both.
        for s in model.scenes:
            if s.get("EntryMythic") and s["EntryMythic"] not in (mythic_enum, unlocked): skip.add(s["Id"])
            for n in s["Nodes"]:
                for c in n["Choices"]:
                    if c.get("Mythic") and c["Mythic"] not in (mythic_enum, unlocked): c["Requires"] = list(c["Requires"]) + [NEVER]

    rel_flags_all = {"committed": {r["CommittedFlag"] for r in model.rels.values()}, "closed": {r["ClosedFlag"] for r in model.rels.values()}}
    if policy["planner"] == "kit":
        avoid = kit["avoid_flags"] if kit and kitcfg.get("avoid_flags") else set()
        code = inspect.getsource(V.sim_plan).replace("depth > 24", "depth > 80")
        ns = {}; exec(code, V.__dict__, ns); deep = ns["sim_plan"]
        def plan(model_, s, st, rel_flags):
            rf = dict(rel_flags); rf["closed"] = set(rel_flags["closed"]) | avoid
            return deep(model_, s, st, rf)
        wanted_for = lambda rel: "romance"
        closed_for_wanted = rel_flags_all["closed"] | avoid
    else:
        plan, wanted_for = make_policy_planner(V, policy, rel_flags_all, model)
        closed_for_wanted = rel_flags_all["closed"]
    orig_wanted = V.sim_wanted
    current = {"scene": None}

    def wanted(p):
        rel = current["scene"]["Relationship"] if current["scene"] else None
        mode = wanted_for(rel)
        if mode == "romance" and policy["planner"] == "kit": return orig_wanted(p)
        _, path = p
        if not path: return False
        got = set().union(*[set(c["Set"]) for c in path])
        commits = bool(got & rel_flags_all["committed"])
        closes = bool(got & closed_for_wanted)
        done = completes_path(path)
        if mode == "romance": return commits or (not closes and done)
        if mode == "complete": return commits or done
        if mode == "closes_or_completes": return closes or done
        raise ValueError("unknown wanted mode " + mode)

    def plan_tracked(model_, s, st, rel_flags):
        current["scene"] = s
        return plan(model_, s, st, rel_flags)
    V.sim_plan = plan_tracked
    V.sim_wanted = wanted
    _avail = V.sim_available
    V.sim_available = lambda m, s, st: False if s["Id"] in skip else _avail(m, s, st)

    EVENTS, ST = [], []
    snap = {"flags": set()}
    mythic_flag = mythic

    def world_event(st, why):
        now = set(st.flags)
        on, offf = sorted(now - snap["flags"]), sorted(snap["flags"] - now)
        snap["flags"] = now
        if not on and not offf: return
        if EVENTS and EVENTS[-1]["type"] == "world" and EVENTS[-1]["ch"] == st.chapter and EVENTS[-1]["hour"] == st.hour:
            e = EVENTS[-1]
            e["on"] = sorted((set(e["on"]) | set(on)) - set(offf)); e["off"] = sorted((set(e["off"]) | set(offf)) - set(on))
        else:
            EVENTS.append(dict(type="world", why=why, ch=st.chapter, day=st.hour // 24 + 1, hour=st.hour, on=on, off=offf))

    chstart = {}
    _complete = V.sim_complete
    def complete(model_, st):
        chstart.setdefault(st.chapter, st.hour)
        if mythic_flag != "trickster" and st.chapter >= 1:
            st.flags.discard("trickster"); st.flags.add(mythic_flag); st.times.setdefault(mythic_flag, 0)
        for k, (c, d) in timed.items():
            if st.chapter > c or (st.chapter == c and st.hour - chstart[c] >= d * 24): st.flags.add(k); st.times.setdefault(k, st.hour)
            else: st.flags.discard(k)
        st.flags.difference_update(never)
        r = _complete(model_, st)
        world_event(st, "native/derived")
        return r
    V.sim_complete = complete
    _init = V.SimState.__init__
    def init(self, *a): _init(self, *a); ST.append(self)
    V.SimState.__init__ = init

    _play = V.sim_play
    def play(model_, s, st, rel_flags, p=None):
        world_event(st, "native/derived")
        current["scene"] = s
        p = p or V.sim_plan(model_, s, st, rel_flags)
        before = set(st.flags)
        # visible paragraphs, replayed along the path with the runtime's node-entry state
        state = set(before)
        if not V.is_epilogue(s) and s["NativeReturnCue"] is None:
            sf = model_.rels.get(s["Relationship"], {}).get("StartedFlag")
            if sf: state.add(sf)
        steps = []
        for c in p[1]:
            node = next(n for n in s["Nodes"] if any(x is c for x in n["Choices"]))
            state |= set(node.get("EnterSet", []))
            vis = [i for i, para in enumerate(node.get("Paragraphs", [])) if all(f in state for f in para.get("Requires", []))
                   and not any(f in state for f in para.get("Forbids", [])) and all(any(f in state for f in g) for g in para.get("AnyGroups", []))]
            steps.append(dict(node=node["Id"], index=next(i for i, x in enumerate(node["Choices"]) if x is c), text=c["Text"],
                              paragraphs=vis, set=list(c["Set"]),
                              check=c.get("Check") and {k: c["Check"][k] for k in ("Skill", "DC") if k in c["Check"]},
                              crusade=c.get("Crusade"), alignment=c.get("Alignment"), native_next=c.get("NativeNext")))
            state |= set(c["Set"])
        end_node = None
        if p[1]:
            last = p[1][-1]
            nxt = last["Check"]["Success"] if last.get("Check") else (None if last["Abort"] else last["Next"])
            if nxt and nxt in model_.nodes[s["Id"]]:
                n = model_.nodes[s["Id"]][nxt]
                state |= set(n.get("EnterSet", []))
                end_node = dict(node=nxt, paragraphs=[i for i, para in enumerate(n.get("Paragraphs", [])) if all(f in state for f in para.get("Requires", []))
                                and not any(f in state for f in para.get("Forbids", [])) and all(any(f in state for f in g) for g in para.get("AnyGroups", []))])
        ok = _play(model_, s, st, rel_flags, p)
        for k in after.get(s["Id"], []): st.flags.add(k); st.times.setdefault(k, st.hour)
        now = set(st.flags)
        EVENTS.append(dict(type="scene", id=s["Id"], rel=s["Relationship"], owner=s["Owner"], title=s.get("Title"),
                           ch=st.chapter, day=st.hour // 24 + 1, hour=st.hour, remote=V.is_remote(s),
                           table=V.is_table_scene(s), epilogue=V.is_epilogue(s), completed=ok,
                           steps=steps, end_node=end_node, set=sorted(now - before), unset=sorted(before - now)))
        snap["flags"] = now
        return ok
    V.sim_play = play

    for c, d in (policies.get("chapter_days") or {}).items(): V.SIM_CHAPTER_DAYS[int(c)] = float(d)
    res = V.simulate_rest_budget(model, natives=plain)
    st = ST[-1]
    world_event(st, "end of campaign")
    if policy.get("epilogues"):
        # Epilogue pass (approximation): every epilogue page whose gates hold on the final state, in export order.
        for s in model.scenes:
            if not V.is_epilogue(s) or s["Id"] in skip or not V.sim_available(model, s, st): continue
            p = V.sim_plan(model, s, st, rel_flags_all)
            if p[1]: V.sim_play(model, s, st, rel_flags_all, p)
    summary = dict(
        policy=name, description=policy.get("description"), mythic=mythic,
        chapter_days=res["chapter_days"],
        scenes_visited=sum(1 for e in EVENTS if e["type"] == "scene"),
        scenes_completed=sum(1 for e in EVENTS if e["type"] == "scene" and e["completed"]),
        chapters_reached=sorted({e["ch"] for e in EVENTS if e["type"] == "scene"}),
        committed=sorted(r["relationship"] for r in res["relationships"] if r["committed"]),
        closed=sorted(rk for rk, r in model.rels.items() if r["ClosedFlag"] in st.flags),
        unavailable={rk: sorted(f for f in r.get("UnavailableFlags", []) if f in st.flags and (r.get("UnavailableOverrides") or {}).get(f) not in st.flags)
                     for rk, r in model.rels.items()},
        natives_scheduled=plain, natives_timed={k: list(v) for k, v in timed.items()}, natives_kept_off=sorted(never),
        skipped_scenes=sorted(skip))
    summary["unavailable"] = {k: v for k, v in summary["unavailable"].items() if v}
    out_dir.mkdir(parents=True, exist_ok=True)
    trace = dict(schema="rrt-playthrough-trace/1", summary=summary, chapters=res["chapters"], relationships=res["relationships"],
                 events=EVENTS, final_flags=sorted(st.flags))
    with open(out_dir / "trace.json", "w", encoding="utf-8", newline="\n") as f:
        json.dump(trace, f, ensure_ascii=False, indent=0, sort_keys=False)
    print("%-24s scenes %4d (completed %4d) chapters %s committed %2d/%d closed %d unavailable %d" % (
        name, summary["scenes_visited"], summary["scenes_completed"], summary["chapters_reached"], len(summary["committed"]),
        len(model.rels), len(summary["closed"]), len(summary["unavailable"])))


def main():
    reexec_if_needed()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--policy")
    ap.add_argument("--all", action="store_true", help="run every policy, one process each, sequentially")
    ap.add_argument("--policies", default=str(HERE / "policies.json"))
    ap.add_argument("--runs", default=str(HERE / "runs"))
    a = ap.parse_args()
    policies = json.load(open(a.policies, encoding="utf-8"))
    if a.all:
        rc = 0
        for name in policies["policies"]:
            rc |= subprocess.run([sys.executable, str(Path(__file__).resolve()), "--policy", name, "--policies", a.policies, "--runs", a.runs]).returncode
        sys.exit(rc)
    if not a.policy or a.policy not in policies["policies"]:
        ap.error("--policy must be one of: " + ", ".join(policies["policies"]))
    run_policy(a.policy, policies, Path(a.runs) / a.policy)


if __name__ == "__main__":
    main()

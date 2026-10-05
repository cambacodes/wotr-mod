r"""final_sim.py [OUT_JSON] [rel ...]
ONE combined all-romance run: the repo's E9 simulator (rrt_verify.simulate_rest_budget; Rules.Available mirror unchanged)
with every natives\*.txt (files starting '_' skipped) merged as --sim-natives, plus the player-policy steering the
per-route agents needed:
  - '#@ key:CH+D' timed natives (order inside a chapter), '#@ !key' natives this run never produces, '#@ -choice s/n/i' bans
  - w6\*.extra.txt: '!scene' never offered (inline on a closure list the run never opens), 'key@scene' native turns on right
    after that scene, 'key:-1' kept off
  - SKIP below: inline scenes hosted on native closure lists (dismissal / kill) the run never opens
  - AVOID_FLAGS: flags the planner treats as closures (steers to the romance branch); AVOID_TEXT: choice texts never taken
  - planner depth 80 instead of 24 (long folded pages); Ch6 = 45 sim days (the Threshold chain plays in ONE native answer
    list in game; the sim plays one scene per relationship per day)
Prints conflicts between natives files, the committed table, and dumps the full log."""
import sys, json, glob, os, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import rrt_verify as V
HERE = os.path.dirname(os.path.abspath(__file__))
story = json.load(open(ROOT / "development/Story.json", encoding="utf-8"))

SKIP = {"seelah.trickster.dismissed.setup", "camellia.trickster.killed.setup_hub", "camellia.trickster.killed.setup_q3",
        "camellia.trickster.killed.setup_q1"}
AVOID_FLAGS = set(open(os.path.join(HERE, "avoid.txt"), encoding="utf-8").read().split()) | {
    "soana.friendship_chosen", "soana.courtship_waiting", "soana.later_friends", "soana.late_friends", "soana.friendship_kept",
    "soana.later_friend_evening"}
AVOID_TEXT = {"\"It's worth a joke.", "[Put a deposit on the house special]", "\"Let her stay gone.\"", "[Kneel] \"I'm yours. Send her home.\""}

plain, timed, never, banned, after, off = {}, {}, set(), [], {}, set()
src = {}
conflicts = []
for fn in sorted(glob.glob(os.path.join(HERE, "natives", "*.txt"))):
    if os.path.basename(fn).startswith("_"): continue
    who = os.path.basename(fn)[:-4]
    for line in open(fn, encoding="utf-8"):
        s = line.strip()
        directive = s.startswith("#@")
        if directive: s = s[2:].strip()
        raw = s.split("  #")[0].strip() if s.startswith("-choice") else s.split("#")[0].strip()
        if not raw: continue
        if raw.startswith("-choice "): banned.append(raw.split()[1]); continue
        if raw.startswith("!"): never.add(raw[1:].split(":")[0].strip()); src.setdefault(raw[1:].strip(), []).append(who + "(never)"); continue
        k, v = raw.rsplit(":", 1); k = k.strip(); v = v.strip()
        if "+" in v:
            c, d = v.split("+"); timed[k] = (int(c), float(d)); src.setdefault(k, []).append("%s(%s)" % (who, v)); continue
        ch = int(v)
        if k in plain and plain[k] != ch: conflicts.append("%s: chapter %s vs %s (%s)" % (k, plain[k], ch, who))
        plain[k] = min(plain.get(k, ch), ch); src.setdefault(k, []).append("%s(%s)" % (who, v))
for fn in glob.glob(os.path.join(HERE, "w6", "*.extra.txt")):
    for line in open(fn, encoding="utf-8"):
        line = line.split("#")[0].strip()
        if not line: continue
        if line.startswith("!"): SKIP.add(line[1:].strip()); continue
        if "@" in line: k, sc = line.split("@", 1); after.setdefault(sc.strip(), []).append(k.strip()); continue
        k, v = line.rsplit(":", 1)
        if int(v) < 0: off.add(k.strip())
for k in sorted(never):
    if k in plain or k in timed: conflicts.append("%s: forced on by %s but kept off by another file" % (k, src.get(k)))
for k in list(plain):
    if k in timed or k in never or k in off: plain.pop(k)
for ks in after.values():
    for k in ks: plain.pop(k, None); timed.pop(k, None)

model = V.Model(story)
# Native scripts may schedule observed game state, never grant authored costs or returns.
forced = set(plain) | set(timed) | never | off | {k for ks in after.values() for k in ks}
invalid = forced - set(model.native)
if invalid:
    raise ValueError("Kit schedules non-native flags: " + ", ".join(sorted(invalid)))
for b in banned:
    sid, nid, i = b.rsplit("/", 2)
    c = model.nodes[sid][nid]["Choices"][int(i)]
    c["Requires"] = list(c["Requires"]) + ["__player_never_takes_this__"]
for s in model.scenes:
    for n in s["Nodes"]:
        for c in n["Choices"]:
            if c["Text"].strip() in AVOID_TEXT: c["Requires"] = list(c["Requires"]) + ["__player_never_takes_this__"]
for k in off | {k for ks in after.values() for k in ks}: model.native.pop(k, None)

# deeper planner (same scoring as rrt_verify.sim_plan), closures widened by AVOID_FLAGS
import inspect
code = inspect.getsource(V.sim_plan).replace("depth > 24", "depth > 80")
ns = {}; exec(code, V.__dict__, ns); deep = ns["sim_plan"]
def plan(model_, s, st, rel_flags):
    rf = dict(rel_flags); rf["closed"] = set(rel_flags["closed"]) | AVOID_FLAGS
    return deep(model_, s, st, rf)
V.sim_plan = plan
_avail = V.sim_available
V.sim_available = lambda m, s, st: False if s["Id"] in SKIP else _avail(m, s, st)
chstart = {}
_complete = V.sim_complete
def complete(model_, st):
    chstart.setdefault(st.chapter, st.hour)
    for k, (c, d) in timed.items():
        if st.chapter > c or (st.chapter == c and st.hour - chstart[c] >= d * 24): st.flags.add(k); st.times.setdefault(k, st.hour)
        else: st.flags.discard(k)
    st.flags.difference_update(never | off)
    return _complete(model_, st)
V.sim_complete = complete
LOG, ST = [], []
_init = V.SimState.__init__
def init(self, *a): _init(self, *a); ST.append(self)
V.SimState.__init__ = init
_play = V.sim_play
def play(model_, s, st, rel_flags, p=None):
    p = p or V.sim_plan(model_, s, st, rel_flags)
    ok = _play(model_, s, st, rel_flags, p)
    for k in after.get(s["Id"], []): st.flags.add(k); st.times.setdefault(k, st.hour)
    LOG.append(dict(rel=s["Relationship"], id=s["Id"], title=s.get("Title"), ch=st.chapter, day=st.hour // 24 + 1,
                    remote=V.is_remote(s), delay=s["DelayHours"], completed=ok,
                    choices=[dict(text=c["Text"], check=c.get("Check") and {k: c["Check"][k] for k in ("Skill", "DC") if k in c["Check"]},
                                  commander=bool(c.get("Check") and c["Check"].get("CommanderOnly")), set=c["Set"]) for c in p[1]]))
    return ok
V.sim_play = play
V.SIM_CHAPTER_DAYS[6] = 45
for kv in filter(None, os.environ.get("CHDAYS", "").split(",")):
    c, dd = kv.split(":"); V.SIM_CHAPTER_DAYS[int(c)] = float(dd)
res = V.simulate_rest_budget(model, natives=plain)
st = ST[-1]
print("natives: %d plain, %d timed, %d kept off, %d after-scene, %d banned choices, %d skipped scenes" %
      (len(plain), len(timed), len(never | off), sum(map(len, after.values())), len(banned), len(SKIP)))
print("CONFLICTS between natives files:", len(conflicts))
for c in conflicts: print("  ", c)
n = sum(1 for r in res["relationships"] if r["committed"])
print("COMMITTED %d/%d" % (n, len(res["relationships"])))
for r in res["relationships"]:
    print("  %-22s %-4s day=%-4s %s" % (r["relationship"], "yes" if r["committed"] else "NO", r["day"], r.get("blocked") or ""))
for c in res["chapters"]:
    print("  ch%d days %s rests avail %d used %d needed %d letters %d missed %d load %.2f" % (c["chapter"], c["days"], c["rests_available"], c["rests_used"], c["rests_needed"], c["letters"], c["missed"], c["load"]))
if len(sys.argv) > 1 and sys.argv[1] != "-":
    json.dump(dict(result=res, log=LOG, final_flags=sorted(st.flags), natives=plain, timed=timed, never=sorted(never | off)),
              open(sys.argv[1], "w", encoding="utf-8"), indent=1)
want = set(sys.argv[2:])
for e in LOG:
    if e["rel"] in want:
        print("\n[%s] ch%d day%d %s%s %s (delay %dh)%s" % (e["rel"], e["ch"], e["day"], e["id"], " (letter)" if e["remote"] else "", e["title"], e["delay"], "" if e["completed"] else " [NOT COMPLETED]"))
        for c in e["choices"]:
            print("    > %s%s" % (c["text"][:160], ("  {%s DC %s%s}" % (c["check"].get("Skill"), c["check"].get("DC"), ", Commander" if c["commander"] else "")) if c["check"] else ""))

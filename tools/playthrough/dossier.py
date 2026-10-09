r"""dossier.py: per-chapter checkpoint dossiers from a walker trace, for continuity reviewers.

    python tools/playthrough/dossier.py --policy trickster_all_romance [--knowledge PATH] [--max-kb 120]
    python tools/playthrough/dossier.py --all

Reads runs/<policy>/trace.json and development/Story.json and writes runs/<policy>/chapter-<N>[-part-<k>].md and
runs/<policy>/index.md. Each dossier holds: the ordered scenes of the chapter (id, title, owner, how it is reached,
gameplay it touches, placement among native progress), the full player-visible text along the path taken (node text,
the conditional paragraphs visible with the flags held at that node, the chosen answer and the other answers offered),
the flags set, a state-so-far table, and an appendix per woman present (knowledge file paths + her 10 most relevant
native lines). Deterministic; reads the knowledge repo, never writes it.
"""
import argparse, collections, json, math, os, re, subprocess, sys
from pathlib import Path
from admission import atomic_json, digest, load
from dossier_evidence import evidence, node_states, timeline as chapter_timeline

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DEFAULT_KNOWLEDGE = os.environ.get("RRT_KNOWLEDGE", r"C:\Users\Z\Documents\Projects\Writer\knowledge")
STOP = set("""that this with have from your they them their there what when where which while would could should about
into over than then were been being will just like only more most some such very also does done because before after
again against those these here her his him she he you are was for and the not but all any can our out who why how its
it's i'm i'll don't you're she's said says say yes""".split())


def reexec_if_needed():
    if os.environ.get("PYTHONHASHSEED") == "0" and os.environ.get("PYTHONUTF8") == "1": return
    env = dict(os.environ, PYTHONHASHSEED="0", PYTHONUTF8="1")
    sys.exit(subprocess.run([sys.executable, str(Path(__file__).resolve())] + sys.argv[1:], env=env).returncode)


def clean(t):
    t = re.sub(r"\{n\}(.*?)\{/n\}", lambda m: "_" + m.group(1).strip() + "_" if m.group(1).strip() else "", t, flags=re.S)
    t = re.sub(r"\{mf\|([^|}]*)\|([^}]*)\}", r"\1/\2", t)
    t = re.sub(r"\{[a-z]\|[^}]*\}|\{/[a-z]\}", "", t)
    return t.replace("{name}", "<Commander>")


def words(t):
    return [w for w in re.findall(r"[a-z][a-z']{3,}", clean(t).lower()) if w not in STOP]


class Ctx:
    def __init__(self, knowledge):
        sys.path.insert(0, str(ROOT / "tools"))
        import rrt_verify as V
        import run_guide_check as G
        self.V, self.G = V, G
        self.story = load(ROOT / "development/Story.json")
        self.model = V.Model(self.story)
        self.knowledge = Path(knowledge)
        idp = self.knowledge / "identities.json"
        self.ids = load(idp)["characters"] if idp.exists() else []
        self.roster = [c for c in self.ids if c.get("roster")]
        self.by_rel = collections.defaultdict(list)
        self.by_alias = {}
        for c in self.roster:
            for r in c.get("relationship_ids", []): self.by_rel[r].append(c["character_id"])
            for a in c.get("aliases", []) + [c.get("display_name", "")]:
                if a: self.by_alias[a.lower()] = c["character_id"]
        self.names = {c["character_id"]: c.get("display_name", c["character_id"]) for c in self.ids}
        self.lines_cache = {}

    def women_of_scene(self, s, ev):
        out = []
        if s["Relationship"] in self.by_rel and s["Relationship"] not in ("tirabade",):
            out += self.by_rel[s["Relationship"]]
        owner = re.sub(r"Epilogue$", "", s["Owner"]).lower()
        if owner in self.by_alias: out.append(self.by_alias[owner])
        for st in ev["steps"] + ([ev["end_node"]] if ev.get("end_node") else []):
            sp = (self.model.nodes[s["Id"]][st["node"]].get("Speaker") or "").lower()
            if sp in self.by_alias: out.append(self.by_alias[sp])
        for wid in s.get("ParticipantWomen", []):
            if wid.lower() in self.by_alias: out.append(self.by_alias[wid.lower()])
            else:
                for c in self.by_rel.get(self.story["SeatWomen"].get(wid, {}).get("Relationship"), []): out.append(c)
        for p in s.get("Participants", []):
            out += [c for c in self.by_rel.get(p, []) if p not in ("tirabade",)]
        return list(dict.fromkeys(out))

    def native_lines(self, cid):
        if cid not in self.lines_cache:
            p = self.knowledge / "characters" / cid / "native-lines.json"
            self.lines_cache[cid] = load(p).get("lines", []) if p.exists() else []
        return self.lines_cache[cid]


def reach(ctx, s):
    G, V = ctx.G, ctx.V
    if V.is_epilogue(s): return "epilogue slide (end of game)"
    parts = []
    if V.is_table_scene(s) or s.get("TableHosted"):
        parts.append("The Table: household menu hub (rest / tavern)")
    elif s.get("NativeReturnCue") or s.get("AnswerLists"):
        parts.append("inline answer inside a native dialogue (%d native answer list%s)%s" % (
            len(s.get("AnswerLists") or []), "" if len(s.get("AnswerLists") or []) == 1 else "s",
            ", returns to the native cue" if s.get("NativeReturnCue") else ""))
    if V.is_remote(s):
        kind = "memory" if s["Owner"] == "Memory" else (s.get("Kind") or "letter")
        parts.append("remote %s delivered at rest (mailbag)%s" % (kind, ", manual read from the Satchel" if s.get("ManualOnly") else ""))
    elif s.get("ManualOnly"):
        parts.append("manual read (Satchel / book page)")
    if s.get("InteractionHub"): parts.append("interaction hub `%s`" % s["InteractionHub"])
    if s.get("Areas"): parts.append("area: " + " / ".join(G.AREAS.get(a, a) for a in s["Areas"]))
    if not parts: parts.append("talk to %s (companion / NPC contact)" % s["Owner"])
    if s.get("Parcel"): parts.append("parcel/item delivery")
    return "; ".join(parts)


def gameplay(ctx, s, ev):
    out = []
    for st in ev["steps"]:
        if st.get("check"): out.append("check %s DC %s" % (st["check"].get("Skill"), st["check"].get("DC")))
        if st.get("crusade"): out.append("crusade %s %+d" % (st["crusade"].get("Resource"), st["crusade"].get("Amount", 0)))
        if st.get("alignment"): out.append("alignment %s %+d" % (st["alignment"].get("Direction"), st["alignment"].get("Value", 1)))
        if st.get("native_next"): out.append("hands off to a native dialogue cue")
    for st in ev["steps"]:
        c = ctx.model.nodes[s["Id"]][st["node"]]["Choices"][st["index"]]
        if c.get("RemoveItem"): out.append("removes item")
        if c.get("StartEtude"): out.append("starts a native etude")
        if c.get("Revive"): out.append("revive")
        if c.get("Mythic"): out.append("mythic-gated answer (%s)" % c["Mythic"])
    natives = sorted({f for f in ev["set"] if f in ctx.model.native})
    if natives: out.append("sets native state: " + ", ".join(natives[:6]))
    if s.get("RestAllowance"): out.append("spends rest allowance `%s`" % s["RestAllowance"])
    if s.get("DelayHours"): out.append("waits %dh after its trigger" % s["DelayHours"])
    return "; ".join(dict.fromkeys(out)) or "none (text only)"


def render_scene(ctx, ev, state, natives_before, natives_after, chosen_only=False):
    s = ctx.model.by_id[ev["id"]]
    m = ctx.model
    L = []
    L.append("### %s (%s)" % (ev["title"] or ev["id"], ev["id"]))
    L.append("- Owner: %s; relationship: `%s`; chapter %s, day %s%s" % (
        ev["owner"], ev["rel"], ev["ch"], ev["day"], "" if ev["completed"] else "; NOT COMPLETED (aborted or stalled)"))
    L.append("- Origin: authored mod scene, not a native transcript. Native state identifiers do not prove played native history.")
    L.append("- Trace reference: `trace.json#/events/%s`; scene state: `states.json#/events/%s` (before/after)." % (ev.get("_ordinal", "unknown"), ev.get("_ordinal", "unknown")))
    L.append("- Entry / host / return / presence evidence: `" + json.dumps(evidence(ctx, s), ensure_ascii=False, sort_keys=True) + "`")
    L.append("- Reached: " + reach(ctx, s))
    L.append("- Gameplay touched: " + gameplay(ctx, s, ev))
    L.append("- Placement: after scheduled native/derived world event %s; before world event %s" % (natives_before or "(chapter start)", natives_after or "(nothing later this chapter)"))
    if s.get("Entry"): L.append("- Entry answer: " + clean(s["Entry"]).replace("\n", " "))
    L.append("")
    held = set(state)
    sf = m.rels.get(s["Relationship"], {}).get("StartedFlag")
    if sf and not ctx.V.is_epilogue(s) and s["NativeReturnCue"] is None: held.add(sf)
    nwords = 0
    def node_text(nid, vis):
        nonlocal nwords
        n = m.nodes[s["Id"]][nid]
        sp = n.get("Speaker") or "Narrator"
        body = clean(n.get("Text") or "").strip()
        out = ["**[%s] %s:** %s" % (nid, sp, body) if body else "**[%s] %s:**" % (nid, sp)]
        for i in vis:
            out.append("> [p%d] %s" % (i, clean(n["Paragraphs"][i]["Text"]).strip().replace("\n", "\n> ")))
        nwords += len((n.get("Text") or "").split()) + sum(len(n["Paragraphs"][i]["Text"].split()) for i in vis)
        return out
    snapshots = node_states(ctx, ev, state)
    for step_index, st in enumerate(ev["steps"]):
        n = m.nodes[s["Id"]][st["node"]]
        L.append("- Node-state reference: `states.json#/events/%s/nodes/%s` (export replay; before entry, visible, after choice; off flags are absent from held flags)." % (ev.get("_ordinal", "unknown"), step_index))
        L.append("- Choice/paragraph gates: `" + json.dumps({k: snapshots[step_index][k] for k in ("choice_gates", "paragraph_gates")}, ensure_ascii=False, sort_keys=True) + "`")
        held |= set(n.get("EnterSet", []))
        L += node_text(st["node"], st["paragraphs"])
        c = n["Choices"][st["index"]]
        tag = []
        if st.get("check"): tag.append("check %s DC %s, success" % (st["check"].get("Skill"), st["check"].get("DC")))
        L.append("- **Chose [%d]:** %s%s" % (st["index"], clean(c["Text"]), (" {" + "; ".join(tag) + "}") if tag else ""))
        others = []
        for i, o in enumerate(n["Choices"]):
            if i == st["index"]: continue
            ok = all(f in held for f in o["Requires"]) and not any(f in held for f in o["Forbids"])
            if ok: others.append("[%d] %s" % (i, clean(o["Text"])[:90].replace("\n", " ")))
        if others: L.append("  - other answers satisfying flag gates (Mythic/item/resource availability unproved): " + " | ".join(others))
        held |= set(c["Set"])
        L.append("")
    if ev.get("end_node"):
        L.append("- Node-state reference: `states.json#/events/%s/nodes/%s` (terminal entry replay)." % (ev.get("_ordinal", "unknown"), len(ev["steps"])))
        L += node_text(ev["end_node"]["node"], ev["end_node"]["paragraphs"]); L.append("")
    vis_set = [f for f in ev["set"] if not f.startswith("rrt.payment.")]
    L.append("- Flags set: " + (", ".join("`%s`" % f for f in vis_set) if vis_set else "none"))
    if ev.get("unset"): L.append("- Flags cleared: " + ", ".join("`%s`" % f for f in ev["unset"]))
    L.append("- Played text: ~%d words" % nwords)
    L.append("")
    return "\n".join(L) + "\n"


def state_table(ctx, flags):
    m = ctx.model
    rows = ["| relationship | women | status | detail |", "|---|---|---|---|"]
    for rk, r in m.rels.items():
        started, committed, closed = r["StartedFlag"] in flags, r["CommittedFlag"] in flags, r["ClosedFlag"] in flags
        ov = r.get("UnavailableOverrides") or {}
        gone = [f for f in r.get("UnavailableFlags", []) if f in flags and ov.get(f) not in flags]
        returned = [f for f in r.get("UnavailableFlags", []) if f in flags and ov.get(f) in flags]
        harem = (rk + ".harem.eligible") in flags
        if not (started or gone or closed or returned): continue
        status = "unavailable (physical role/history requires verification)" if gone else "closed" if closed else "committed" if committed else "started"
        if returned and not gone: status += " (returned)"
        detail = []
        if committed and status != "committed": detail.append("committed earlier")
        if harem: detail.append("harem-eligible")
        if gone: detail.append("unavailable: " + ", ".join(gone))
        if returned: detail.append("returned via: " + ", ".join(ov[f] for f in returned))
        women = ", ".join(ctx.names.get(c, c) for c in ctx.by_rel.get(rk, [])) or "-"
        rows.append("| `%s` | %s | %s | %s |" % (rk, women, status, "; ".join(detail) or "-"))
    path = [k for k in ("trickster", "angel", "legend", "demon", "lich", "aeon", "azata", "devil", "swarm", "dragon") if k in flags]
    return "Mythic path flag: %s\n\n" % (", ".join(path) or "none") + "\n".join(rows) + "\n"


def appendix(ctx, women, texts):
    L = ["## Appendix: women present", ""]
    for cid in women:
        d = ctx.knowledge / "characters" / cid
        L.append("### %s (`%s`)" % (ctx.names.get(cid, cid), cid))
        files = sorted(p.name for p in d.iterdir()) if d.exists() else []
        L.append("- Knowledge: " + (", ".join("`%s`" % str(d / f) for f in files) if files else "(no knowledge directory)"))
        lines = ctx.native_lines(cid)
        tokens = collections.Counter(words(texts.get(cid, "")))
        if not tokens: tokens = collections.Counter(words(texts.get("*", "")))
        scored = []
        for i, ln in enumerate(lines):
            t = ln.get("text", "")
            if len(clean(t)) < 30: continue
            ws = set(words(t))
            sc = sum(math.log(1 + tokens[w]) for w in ws) / math.sqrt(1 + len(ws))
            scored.append((-sc, i, ln))
        scored.sort(key=lambda x: (x[0], x[1]))
        if scored:
            L.append("- Native lines (10 most relevant to this part, by shared vocabulary):")
            for _, i, ln in scored[:10]:
                L.append("  - \"%s\" (`%s`)" % (clean(ln["text"]).replace("\n", " ")[:300], ln.get("cue", ln.get("key"))))
        else:
            L.append("- Native lines: none on file")
        L.append("")
    return "\n".join(L) + "\n"


def build(ctx, policy, runs, max_kb, contract_rel):
    rdir = Path(runs) / policy
    trace = load(rdir / "trace.json")
    for old in rdir.glob("chapter-*.md"): old.unlink()
    events = trace["events"]
    # replay flag state; collect per-chapter streams
    flags, chapters = set(), collections.OrderedDict()
    state_refs = {}
    provenance = {}
    for ordinal, original in enumerate(events):
        e = dict(original, _ordinal=ordinal)
        key = "epilogue" if e["type"] == "scene" and e.get("epilogue") else str(e["ch"])
        ch = chapters.setdefault(key, dict(items=[], start=None))
        if ch["start"] is None: ch["start"] = set(flags)
        if e["type"] == "world":
            flags |= set(e["on"]); flags -= set(e["off"])
            ch["items"].append(("native", e, e["on"]))
            for f in e["on"] + e["off"]:
                provenance[f] = dict(event=ordinal, hour=e["hour"], origin="scheduled native/derived (earning unknown)", held=f in flags)
        else:
            ch["items"].append(("scene", e, set(flags)))
            before = set(flags)
            flags |= set(e["set"]); flags -= set(e.get("unset", []))
            for f in e["set"] + e.get("unset", []):
                provenance[f] = dict(event=ordinal, hour=e["hour"], origin="scene aggregate delta (authored/native/derived attribution unknown)", held=f in flags)
            state_refs[str(ordinal)] = dict(scene=e["id"], before=sorted(before), after=sorted(flags),
                nodes=node_states(ctx, e, before), provenance=dict(provenance))
        ch["end"] = set(flags)
    budget = max_kb * 1024
    written = []
    declared = []
    atomic_json(rdir / "states.json", dict(schema="rrt-dossier-states/1", trace_digest=digest(rdir / "trace.json"), events=state_refs))
    for key, ch in chapters.items():
        items = ch["items"]
        nat_idx = [i for i, it in enumerate(items) if it[0] == "native"]
        def fmt_n(it): return "day %s: %s" % (it[1]["day"], ", ".join("`%s` (%s)" % (f, ctx.model.native.get(f, "derived/world state")) for f in it[2][:4]) + (" +%d" % (len(it[2]) - 4) if len(it[2]) > 4 else ""))
        blocks = []   # (text, women, scene_text_by_woman, state_before)
        timeline = [(items[i][1]["hour"], "- " + fmt_n(items[i])) for i in nat_idx]
        for i, it in enumerate(items):
            if it[0] != "scene": continue
            ev, st = it[1], it[2]
            prev = [j for j in nat_idx if j < i][-1:] ; nxt = [j for j in nat_idx if j > i][:1]
            text = render_scene(ctx, ev, st, fmt_n(items[prev[0]]) if prev else "", fmt_n(items[nxt[0]]) if nxt else "")
            s = ctx.model.by_id[ev["id"]]
            blocks.append((text, ctx.women_of_scene(s, ev), st, ev))
        timeline_name = "chapter-%s-timeline.md" % key
        (rdir / timeline_name).write_text(chapter_timeline(ctx, key, items, trace), encoding="utf-8", newline="\n")
        declaration = dict(chapter=key, timeline=policy + "/" + timeline_name, parts=[])
        declared.append(declaration)
        if not blocks: continue
        def render_part(part, pi, total):
            women = list(dict.fromkeys(w for b in part for w in b[1]))
            texts = collections.defaultdict(str)
            for b in part:
                for w in b[1]: texts[w] += b[0]
                texts["*"] += b[0]
            first, last = part[0][3], part[-1][3]
            lo, hi = first["hour"], last["hour"]
            tl = [ln for h, ln in timeline if lo - 72 <= h <= hi + 72]
            H = ["# Checkpoint dossier: %s, chapter %s%s" % (policy, key, (" part %d/%d" % (pi, total)) if total > 1 else ""), "",
                 "Policy: %s" % (trace["summary"].get("description") or policy), "",
                 "Whole-chapter timeline: [%s](%s). State references: [states.json](states.json)." % (timeline_name, timeline_name), "",
                 "Scenes %d (of %d this chapter), days %s-%s. Review under [the reviewer contract](%s); every claim must cite an address `scene/node` or `scene/node/pN` or a flag." % (
                     len(part), len(blocks), first["day"], last["day"], contract_rel), "",
                 "Simulated, not played: native quests are represented only by the native state keys the export reads. "
                 "Checks always succeed; Crusade resources are assumed sufficient.", "",
                 "## State at the start of this part", "", state_table(ctx, part[0][2]),
                 "## Scheduled native/derived world events around this part (in order, within 3 simulated days)", ""]
            H += (tl[:30] + (["- ... %d more" % (len(tl) - 30)] if len(tl) > 30 else [])) or ["- none"]
            H += ["", "## Scenes played (in order)", ""]
            H += ["%d. `%s` %s (%s), day %s%s" % (k, b[3]["id"], b[3]["title"] or "", b[3]["owner"], b[3]["day"], " [letter]" if b[3]["remote"] else "")
                  for k, b in enumerate(part, 1)]
            H += ["", "## Scene text along the path taken", ""]
            body = "\n".join(H) + "\n" + "".join(b[0] for b in part)
            end_flags = (set(part[-1][2]) | set(part[-1][3]["set"])) - set(part[-1][3].get("unset", []))
            body += "## State at the end of this part\n\n" + state_table(ctx, end_flags) + "\n" + appendix(ctx, women, texts)
            return body
        # pack by estimate, then halve any part whose rendered size exceeds the budget
        parts, cur, size = [], [], 0
        for b in blocks:
            bl = len(b[0].encode("utf-8"))
            if cur and size + bl > budget * 0.55:
                parts.append(cur); cur, size = [], 0
            cur.append(b); size += bl
        if cur: parts.append(cur)
        changed = True
        while changed:
            changed, out = False, []
            for part in parts:
                if len(part) > 1 and len(render_part(part, 1, 2).encode("utf-8")) > budget:
                    h = len(part) // 2; out += [part[:h], part[h:]]; changed = True
                else: out.append(part)
            parts = out
        for pi, part in enumerate(parts, 1):
            name = ("chapter-%s.md" % key) if len(parts) == 1 else ("chapter-%s-part-%02d.md" % (key, pi))
            body = render_part(part, pi, len(parts))
            (rdir / name).write_text(body, encoding="utf-8", newline="\n")
            written.append((name, len(body.encode("utf-8")), len(part)))
            declaration["parts"].append(policy + "/" + name)
    atomic_json(rdir / "dossier-manifest.json", dict(schema="rrt-dossier-manifest/1", policy=policy,
        trace=policy + "/trace.json", trace_digest=digest(rdir / "trace.json"),
        states=policy + "/states.json", chapters=declared))
    s = trace["summary"]
    idx = ["# Playthrough run: %s" % policy, "", s.get("description") or "", "",
           "- Scenes visited: %d (completed %d); chapters reached: %s" % (s["scenes_visited"], s["scenes_completed"], s["chapters_reached"]),
           "- Committed (%d): %s" % (len(s["committed"]), ", ".join(s["committed"]) or "none"),
           "- Closed (%d): %s" % (len(s["closed"]), ", ".join(s["closed"]) or "none"),
           "- Unavailable at end: " + (", ".join("%s (%s)" % (k, ", ".join(v)) for k, v in s["unavailable"].items()) or "none"),
           "", "| dossier | KB | scenes |", "|---|---|---|"]
    idx += ["| [%s](%s) | %.1f | %d |" % (n, n, b / 1024.0, k) for n, b, k in written]
    (rdir / "index.md").write_text("\n".join(idx) + "\n", encoding="utf-8", newline="\n")
    print("%-24s %d dossiers, largest %.1f KB, total %.1f KB" % (policy, len(written), max((b for _, b, _ in written), default=0) / 1024.0, sum(b for _, b, _ in written) / 1024.0))


def main():
    reexec_if_needed()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--policy"); ap.add_argument("--all", action="store_true")
    ap.add_argument("--runs", default=str(HERE / "runs"))
    ap.add_argument("--knowledge", default=DEFAULT_KNOWLEDGE)
    ap.add_argument("--max-kb", type=int, default=120)
    a = ap.parse_args()
    names = sorted(p.name for p in Path(a.runs).iterdir() if (p / "trace.json").exists()) if a.all else [a.policy]
    if not names or not names[0]: ap.error("--policy or --all")
    ctx = Ctx(a.knowledge)
    for n in names: build(ctx, n, a.runs, a.max_kb, "../../reviewer-contract.md")


if __name__ == "__main__":
    main()

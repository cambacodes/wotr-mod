#!/usr/bin/env python3
"""rrt_verify.py - fast static integrity verifier for RanRomanceTirabade (RRT).

Pure stdlib. Reads the mod READ-ONLY. Mirrors src/Story.cs Rules.Available / Rules.Validate and
src/Main.cs Build()/State() semantics closely enough to find unreachable content, cross-route
lockouts, chapter traps, lint problems and bad native GUID bindings, without Unity.

Usage:
  python rrt_verify.py [--story PATH] [--game DIR] [--json OUT] [--no-zip] [--quiet]
  python rrt_verify.py --drafts          # also build + check unregistered storyline drafts (from a scratch COPY)

Sections: A producers | B reachability per mythic world | C chapter/delay traps | D cross-route forbid matrix
          E lints | F native GUID bindings | G runtime-risk metrics | H Trickster roster matrix | I TypeId lint
"""
import argparse, collections, difflib, hashlib, importlib, json, os, re, shutil, sys, time, zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The mod root is, in order: $RRT_ROOT, the repository this script lives in (tools/..), or the default checkout.
MOD = Path(os.environ["RRT_ROOT"]) if os.environ.get("RRT_ROOT") else (
    HERE.parent if (HERE.parent / "expansion.py").exists() else Path(r"C:\Users\Z\Documents\Projects\RanRomanceTirabade"))
GAME = Path(os.environ.get("RRT_GAME_DIR") or r"D:\SteamLibrary\steamapps\common\Pathfinder Second Adventure")
SCRATCH = HERE / "scratch"

MYTHIC = ["trickster", "angel", "demon", "lich", "aeon", "azata", "devil", "dragon", "legend", "swarm"]
CONTACT_EVIDENCE = {"konomi.missed_contact_available", "konomi.missed_contact_invalidated", "konomi.retained_dead",
                    "konomi.return_contact_available", "konomi.return_correspondence_available",
                    "irabeth.return_correspondence_available", "irabeth.return_meeting_arrived",
                    "nurah.correspondence_available", "nurah.meeting_arrived"}
CHECK_SKILLS = {"SkillAthletics", "SkillMobility", "SkillStealth", "SkillThievery", "SkillKnowledgeArcana",
                "SkillKnowledgeWorld", "SkillLoreNature", "SkillLoreReligion", "SkillPerception",
                "SkillUseMagicDevice", "CheckDiplomacy", "CheckBluff", "CheckIntimidate"}
NURAH_CAPITAL = "2570015799edf594daf2f076f2f975d8"
NURAH_CONTACT = "f999fc37ddb225640b7f98c0a05d6948"
ANEVIA_LIST, IRABETH_LIST = "33960c7f7af40cd43b7f801a76c87a0b", "871af36f2ab2b1f40b5de77976c54276"
HIST_WORDS = re.compile(r"dead|death|killed|kill|married|wedding|marri|elan|rejected|refused|accepted|freed|free\b|saved|"
                        r"condemned|complete|finished|sold|chosen|choice|betray|sacrific|lost|gone|ran_|ending|revived|"
                        r"banish|exile|spared|destroy|prison|fight", re.I)
DEFAULT_LIMITS = dict(node_chars=1400, choice_chars=220, entry_chars=160)


# --------------------------------------------------------------------------------------------- model
def norm_scene(s):
    d = dict(Owner="Anevia", Relationship="tirabade", AnswerLists=[], NativeReturnCue=None, Areas=[], Chapters=[],
             Remote=False, ManualOnly=False, InteractionHub=None, Recovery=None, AfterRecovery=None,
             AfterDeparture=None, ContactUnit=None, AdditionalContactUnits=[], MinChapter=1, MaxChapter=5,
             DelayHours=0, Optional=False, Requires=[], RequiresAny=[], RequiresAnyGroups=[], Forbids=[],
             ForbidOverrides={}, Nodes=[], Entry="", Title="")
    d.update({k: v for k, v in s.items() if v is not None or k in ("NativeReturnCue",)})
    for n in d["Nodes"]:
        n.setdefault("Speaker", "Narrator"); n.setdefault("Portrait", ""); n.setdefault("Text", "")
        n.setdefault("Choices", [])
        for c in n["Choices"]:
            for k, v in dict(Text="Continue", Next=None, Abort=False, Revive=None, Check=None, Set=[], Requires=[],
                             Forbids=[]).items():
                if c.get(k) is None and v is not None:
                    c[k] = v
                c.setdefault(k, v)
    return d


def is_remote(s): return bool(s["Remote"]) or s["Owner"] == "Memory"
def is_epilogue(s): return s["Owner"].endswith("Epilogue")


def is_nurah_hub(s):
    return (s["InteractionHub"] == "nurah.arrival" and s["Relationship"] == "nurah" and s["Owner"] == "Nurah"
            and not is_remote(s) and s["ContactUnit"] == NURAH_CONTACT and not s["AnswerLists"]
            and list(s["Areas"]) == [NURAH_CAPITAL] and list(s["Chapters"]) == [5]
            and "nurah.meeting_accepted" in s["Requires"] and "nurah.meeting_arrived" in s["Requires"])


def entry_targets(s):
    if is_remote(s) or is_epilogue(s): return []
    if s["InteractionHub"] is not None:
        if is_nurah_hub(s): return []
        raise ValueError("Unrecognized authored interaction hub: " + s["Id"])
    if s["AnswerLists"]: return list(s["AnswerLists"])
    if s["Relationship"] == "tirabade":
        if s["Owner"] == "Anevia": return [ANEVIA_LIST]
        if s["Owner"] == "Irabeth": return [IRABETH_LIST]
        if s["Owner"] == "Together": return [ANEVIA_LIST, IRABETH_LIST]
    raise ValueError("No dialogue attachment points for %s (%s)" % (s["Id"], s["Owner"]))


def next_nodes(c):
    if c.get("Check"): return [c["Check"]["Success"], c["Check"]["Failure"]]
    return [c["Next"]] if c.get("Next") else []


def completes(s, c):
    return not is_epilogue(s) and c.get("Next") is None and c.get("Check") is None and not c.get("Abort")


class Model:
    def __init__(self, story):
        self.story = story
        self.scenes = [norm_scene(s) for s in story["Scenes"]]
        self.by_id = {s["Id"]: s for s in self.scenes}
        self.rels = story.get("Relationships") or {}
        self.etudes = story.get("Etudes", {})
        self.permanent_etudes = set(story.get("PermanentEtudes", []))
        nk = {}
        for sec in ("Etudes", "CompletedQuests", "SeenCues", "SelectedAnswers", "StartedDialogs", "CompletedEtudes"):
            for k in story.get(sec, {}): nk.setdefault(k, sec)
        self.native = nk
        self.revivals = story.get("Revivals", {})
        self.derived = {"loss", "ascended", "inhuman", "chapter_one", "chapter_later"} | CONTACT_EVIDENCE | \
                       {"revive.%s.available" % k for k in self.revivals}
        # producers: flag -> list of (scene, node, choice-index or None)
        self.producers = collections.defaultdict(list)
        for s in self.scenes:
            for n in s["Nodes"]:
                for i, c in enumerate(n["Choices"]):
                    for f in c["Set"]:
                        self.producers[f].append((s["Id"], n["Id"], i))
                    if completes(s, c):
                        self.producers[s["Id"]].append((s["Id"], n["Id"], i))
            if not is_epilogue(s) and s["NativeReturnCue"] is None and s["Relationship"] in self.rels:
                self.producers[self.rels[s["Relationship"]]["StartedFlag"]].append((s["Id"], None, "start"))
        self.authored = set(self.producers) | {s["Id"] for s in self.scenes}
        for r in self.rels.values():
            self.authored |= {r["StartedFlag"], r["ClosedFlag"], r["CommittedFlag"]}
        self.nodes = {s["Id"]: {n["Id"]: n for n in s["Nodes"]} for s in self.scenes}
        self.gate_flags = {s["Id"]: list(s["Requires"]) + list(s["RequiresAny"]) + [x for g in s["RequiresAnyGroups"] for x in g]
                           for s in self.scenes}
        allf = set(self.authored) | set(self.native)
        forb = set()
        for s in self.scenes:
            forb |= set(s["Forbids"])
            for n in s["Nodes"]:
                for c in n["Choices"]: forb |= set(c["Forbids"])
        forb |= {r["ClosedFlag"] for r in self.rels.values()}
        forb |= {s["Id"] for s in self.scenes}   # a completed scene can never run again (Available checks state.Has(scene.Id))
        self.scene_sets = {s["Id"]: {f for n in s["Nodes"] for c in n["Choices"] for f in c["Set"]} for s in self.scenes}
        self.choice_req_scenes = collections.defaultdict(set)
        for s in self.scenes:
            for n in s["Nodes"]:
                for c in n["Choices"]:
                    for f in c["Requires"]: self.choice_req_scenes[f].add(s["Id"])
        # must-analysis only needs flags that are ever forbidden (projection commutes with union/intersection)
        self.persistent = frozenset(f for f in allf if (f in self.authored or self.is_persistent_native(f)) and f in forb) |             ({"loss", "ascended"} & forb)
        self.forbidden_any = frozenset(forb)
        self.static_ctx = {}
        for f, lst in self.producers.items():
            for (sid, nid, i) in lst:
                if i == "start": self.static_ctx[(sid, nid, i)] = frozenset()
                else:
                    c = self.nodes[sid][nid]["Choices"][i]
                    self.static_ctx[(sid, nid, i)] = frozenset((set(c["Requires"]) | set(c["Set"])) & self.persistent)

    def is_persistent_native(self, f):
        sec = self.native.get(f)
        if sec is None: return False
        if sec != "Etudes": return True
        return (f in self.permanent_etudes or f.endswith("_dead") or f.endswith("_gone") or f.startswith("ascend_")
                or f in ("sacrifice", "true_lich"))

    def all_referenced(self):
        """flag -> list of (where) references"""
        ref = collections.defaultdict(list)
        for s in self.scenes:
            for k in ("Requires", "Forbids", "RequiresAny"):
                for f in s[k]: ref[f].append((s["Id"], k))
            for g in s["RequiresAnyGroups"]:
                for f in g: ref[f].append((s["Id"], "RequiresAnyGroups"))
            for a, b in s["ForbidOverrides"].items(): ref[b].append((s["Id"], "ForbidOverride"))
            for n in s["Nodes"]:
                for i, c in enumerate(n["Choices"]):
                    for k in ("Requires", "Forbids"):
                        for f in c[k]: ref[f].append(("%s/%s/%d" % (s["Id"], n["Id"], i), "choice." + k))
        for rk, r in self.rels.items():
            for f in r.get("UnavailableFlags", []): ref[f].append(("rel:" + rk, "UnavailableFlags"))
            for f in r.get("FailureFlags", []): ref[f].append(("rel:" + rk, "FailureFlags"))
        for k, e in (self.story.get("ParentEpilogueEdits") or {}).items():
            for f in e.get("Requires", []): ref[f].append(("parentEdit:" + k, "Requires"))
            for f in e.get("Forbids", []): ref[f].append(("parentEdit:" + k, "Forbids"))
        for r in self.story.get("ParentEpilogueLossRules") or []:
            for f in r.get("Requires", []): ref[f].append(("lossRule:" + r["Id"], "Requires"))
            for f in r.get("Forbids", []): ref[f].append(("lossRule:" + r["Id"], "Forbids"))
        return ref


# ------------------------------------------------------------------------------------ world / reachability
class World:
    """Abstract native state. true: natives forced held; false: natives impossible. Everything else free."""
    def __init__(self, name, true=(), false=()):
        self.name, self.true, self.false = name, set(true), set(false)


def mythic_world(m, model, name=None, true=(), false=()):
    others = [x for x in MYTHIC if x != m and x in model.native]
    fl = set(others) | set(false)
    tr = set(true)
    if m and m in model.native: tr.add(m)
    if m != "lich": fl.add("true_lich")
    return World(name or (m or "none"), tr, fl)


class Reach:
    """Monotone over-approximation of reachability honoring forced native state, plus a sound 'must-hold'
    analysis that removes scenes/choices whose authored Forbids are guaranteed held by their own prerequisites."""
    def __init__(self, model, world, chaptered=True):
        self.m, self.w, self.chaptered = model, world, chaptered
        self.dead_scenes, self.dead_choices = {}, {}
        for _ in range(6):
            self._forward()
            newly = self._must()
            if not newly: break

    # native/derived possibility ----------------------------------------------------------
    def native_possible(self, f, ch):
        m, w = self.m, self.w
        if f in w.false: return False
        if f in m.native: return True
        if f == "chapter_one": return (ch == 1) if ch else True
        if f == "chapter_later": return (ch > 1) if ch else True
        if f == "inhuman": return self.native_possible("swarm", ch) or self.native_possible("true_lich", ch)
        if f == "ascended": return any(self.native_possible(a, ch) for a in ("ascend_all", "ascend_alone", "ascend_areelu", "ascend_companions"))
        if f == "loss": return any(self.native_possible(a, ch) for a in ("irabeth_dead", "anevia_dead", "irabeth_gone", "anevia_gone", "sacrifice"))
        if f.startswith("revive.") and f.endswith(".available"):
            k = f[7:-10]; d = m.revivals.get(k, {}).get("DeathFlag")
            return k == "konomi" or (d is not None and self.native_possible(d, ch))
        if f in CONTACT_EVIDENCE:
            if f == "konomi.retained_dead": return True
            return True
        return False

    def forced(self, f, ch):
        w = self.w
        if f in w.true: return True
        if f == "chapter_one": return ch == 1 if ch else False
        if f == "chapter_later": return (ch or 0) > 1
        if f == "inhuman": return "swarm" in w.true or "true_lich" in w.true
        if f == "loss": return any(a in w.true for a in ("irabeth_dead", "anevia_dead", "irabeth_gone", "anevia_gone", "sacrifice"))
        if f == "ascended": return any(a in w.true for a in ("ascend_all", "ascend_alone", "ascend_areelu", "ascend_companions"))
        return False

    def possible(self, f, ch):
        return f in self.held or self.native_possible(f, ch)

    # scene gate (ignores authored forbids except via must-analysis) ------------------------
    def scene_gate(self, s, ch):
        m = self.m
        if s["Id"] in self.dead_scenes: return "dead:" + self.dead_scenes[s["Id"]]
        if self.chaptered:
            if ch < s["MinChapter"] or ch > s["MaxChapter"]: return "chapter"
            if s["Chapters"] and ch not in s["Chapters"]: return "chapter"
        for f in s["Requires"]:
            if not self.possible(f, ch): return "requires:" + f
        if s["RequiresAny"] and not any(self.possible(f, ch) for f in s["RequiresAny"]): return "requiresAny"
        for g in s["RequiresAnyGroups"]:
            if not any(self.possible(f, ch) for f in g): return "requiresAnyGroup"
        for f in s["Forbids"]:
            if self.forced(f, ch):
                o = s["ForbidOverrides"].get(f)
                if not (o and self.possible(o, ch)): return "forbid-forced:" + f
        if is_epilogue(s): return None
        rel = m.rels.get(s["Relationship"], {})
        rec = m.revivals.get(s["Recovery"]) if s["Recovery"] else None
        if rec and not self.native_possible("revive.%s.available" % s["Recovery"], ch): return "recovery"
        for f in rel.get("UnavailableFlags", []):
            if rec and f == rec.get("DeathFlag"): continue
            if s["AfterDeparture"] == "irabeth" and f == "irabeth_gone": continue
            if self.forced(f, ch): return "unavailable-forced:" + f
        if s["Relationship"] == "tirabade" and self.chaptered and not is_remote(s) and ch == 4: return "tirabade-ch4"
        return None

    def choice_ok(self, s, c, ch):
        for f in c["Requires"]:
            if not self.possible(f, ch): return False
        for f in c["Forbids"]:
            if self.forced(f, ch): return False
        return True

    def _forward(self):
        m = self.m
        self.held, self.reached, self.choices = set(), {}, set()   # reached: scene -> earliest chapter
        self.why = {}
        waiting = collections.defaultdict(set)
        chapters = [1, 2, 3, 4, 5, 6] if self.chaptered else [0]
        for ch in chapters:
            # re-walk scenes reached earlier that are still inside their window (chapter-dependent choices)
            queue = [s for s in m.scenes if s["Id"] not in self.reached]
            rewalk = [m.by_id[sid] for sid in self.reached if not self.chaptered or
                      (m.by_id[sid]["MinChapter"] <= ch <= m.by_id[sid]["MaxChapter"])]
            newf = []
            for s in rewalk: newf += self._walk(s, ch)
            for f in newf:
                for sid in waiting.pop(f, ()): pass
            while queue:
                nxt = []
                for s in queue:
                    if s["Id"] in self.reached: continue
                    g = self.scene_gate(s, ch)
                    if g:
                        self.why[s["Id"]] = g
                        if g.startswith("requires"):
                            for f in m.gate_flags[s["Id"]]: waiting[f].add(s["Id"])
                        continue
                    self.reached[s["Id"]] = ch
                    self.why.pop(s["Id"], None)
                    new = self._walk(s, ch)
                    while new:
                        more = []
                        for f in new:
                            for sid in waiting.pop(f, ()):
                                if sid not in self.reached: nxt.append(m.by_id[sid])
                            for sid in m.choice_req_scenes.get(f, ()):
                                if sid in self.reached and sid != s["Id"]:
                                    ss = m.by_id[sid]
                                    if not self.chaptered or ss["MinChapter"] <= ch <= ss["MaxChapter"]:
                                        more += self._walk(ss, ch)
                        new = more
                queue = nxt

    def _walk(self, s, ch):
        m = self.m
        new = []
        if not is_epilogue(s) and s["NativeReturnCue"] is None:
            sf = m.rels.get(s["Relationship"], {}).get("StartedFlag")
            if sf and sf not in self.held: self.held.add(sf); new.append(sf)
        nodes = m.nodes[s["Id"]]
        seen, stack = set(), [s["Nodes"][0]["Id"]] if s["Nodes"] else []
        while stack:
            nid = stack.pop()
            if nid in seen or nid not in nodes: continue
            seen.add(nid)
            for i, c in enumerate(nodes[nid]["Choices"]):
                key = (s["Id"], nid, i)
                if key in self.dead_choices or not self.choice_ok(s, c, ch): continue
                self.choices.add(key)
                for f in c["Set"]:
                    if f not in self.held: self.held.add(f); new.append(f)
                if completes(s, c) and s["Id"] not in self.held:
                    self.held.add(s["Id"]); new.append(s["Id"])
                stack.extend(next_nodes(c))
        return new

    # must-hold analysis ---------------------------------------------------------------------
    def _must(self):
        m = self.m
        forced_native = frozenset(self.w.true)
        P = m.persistent
        prods = collections.defaultdict(list)
        for f in self.held:
            for (sid, nid, i) in m.producers.get(f, []):
                if sid not in self.reached: continue
                if i == "start" or (sid, nid, i) in self.choices:
                    prods[f].append((sid, m.static_ctx[(sid, nid, i)]))
        must_flag = {f: None for f in self.held}
        reached = list(self.reached)
        ms = {}
        for _ in range(40):
            for sid in reached:
                s = m.by_id[sid]
                base = (set(s["Requires"]) | forced_native) & m.forbidden_any
                for r in s["Requires"]:
                    mf = must_flag.get(r)
                    if mf: base |= mf
                if len(s["RequiresAny"]) == 1 and s["RequiresAny"][0] in m.forbidden_any: base.add(s["RequiresAny"][0])
                ms[sid] = base
            changed = False
            for f in must_flag:
                acc = None
                for sid, sctx in prods.get(f, ()):
                    ctx = (ms[sid] & P) | sctx
                    acc = ctx if acc is None else (acc & ctx)
                acc = (acc or set()) | ({f} & m.forbidden_any)
                if must_flag[f] != acc:
                    must_flag[f] = acc; changed = True
            if not changed: break
        self.must_flag, self.must_scene = must_flag, ms
        newly = False
        for sid in reached:
            s = m.by_id[sid]
            mss = ms[sid]
            if sid in mss:
                self.dead_scenes[sid] = "requires-chain needs this scene's own completion"; newly = True; continue
            for f in s["Forbids"]:
                if f in mss:
                    o = s["ForbidOverrides"].get(f)
                    if o and (o in self.held or self.native_possible(o, None)): continue
                    self.dead_scenes[sid] = "requires-chain holds forbidden '%s'" % f; newly = True; break
            if sid in self.dead_scenes: continue
            rel = m.rels.get(s["Relationship"], {})
            if not is_epilogue(s) and rel.get("ClosedFlag") in mss and s["Recovery"] != "konomi" and s["AfterRecovery"] is None:
                self.dead_scenes[sid] = "requires-chain holds relationship ClosedFlag '%s'" % rel["ClosedFlag"]; newly = True; continue
            for n in s["Nodes"]:
                for i, c in enumerate(n["Choices"]):
                    key = (sid, n["Id"], i)
                    if key in self.dead_choices or not (c["Forbids"] or c["Requires"]): continue
                    ctx = mss | (set(c["Requires"]) & m.forbidden_any)
                    for r in c["Requires"]:
                        if must_flag.get(r): ctx = ctx | must_flag[r]
                    if sid in ctx and not s["Owner"].endswith("Epilogue"):
                        self.dead_choices[key] = "choice requires a flag only producible after this scene completes"; newly = True; continue
                    bad = [f for f in c["Forbids"] if f in ctx]
                    inscene = m.scene_sets[sid]
                    bad2 = [f for f in c["Requires"] if f in s["Forbids"] and not s["ForbidOverrides"].get(f) and f not in inscene]
                    if bad or bad2:
                        self.dead_choices[key] = "choice forbids/requires contradiction: %s" % (bad or bad2)
                        newly = True
        return newly


# ------------------------------------------------------------------------------------- blueprint index
def build_bp_index(game):
    rx = re.compile(rb'"AssetId"\s*:\s*"([0-9a-f]{32})".*?"\$type"\s*:\s*"([0-9a-f]{32}), (\w+)"', re.S)
    idx, typeids = {}, set()
    with zipfile.ZipFile(game / "blueprints.zip") as z:
        for info in z.infolist():
            if not info.filename.endswith(".jbp"): continue
            with z.open(info) as fh: h = fh.read(400)
            mm = rx.search(h)
            if mm:
                idx[mm.group(1).decode()] = (mm.group(3).decode(), info.filename)
                typeids.add(mm.group(2).decode())
    return idx, typeids


def parent_bindings():
    """GUIDs created by the parent RanRomance mod (from decompiled source in scratch, else reviewed manifest)."""
    out = {}
    src = SCRATCH / "ranromance"
    if src.is_dir():
        rx = re.compile(r'(\w+)Configurator\.New\(\s*"([^"]+)"\s*,\s*"([0-9a-fA-F-]{32,36})"')
        for p in src.rglob("*.cs"):
            for mm in rx.finditer(p.read_text(encoding="utf-8", errors="replace")):
                g = mm.group(3).replace("-", "").lower()
                kind = mm.group(1)
                kind = {"Answer": "BlueprintAnswer", "AnswersList": "BlueprintAnswersList", "Cue": "BlueprintCue",
                        "Etude": "BlueprintEtude", "Dialog": "BlueprintDialog", "Quest": "BlueprintQuest",
                        "UnlockableFlag": "BlueprintUnlockableFlag", "CueSequence": "BlueprintCueSequence",
                        "BookPage": "BlueprintBookPage", "QuestObjective": "BlueprintQuestObjective",
                        "Unit": "BlueprintUnit", "Check": "BlueprintCheck"}.get(kind, "Blueprint" + kind)
                out[g] = (kind, "parent:" + p.stem)
        for p in src.rglob("*.cs"):
            for mm in re.finditer(r'"([0-9a-f]{32})"', p.read_text(encoding="utf-8", errors="replace")):
                out.setdefault(mm.group(1), ("?parent-literal", "parent-literal:" + p.stem))
    # Every reviewed parent manifest in the repo (expansion, nurah, nurah runtime cues, aranka, targona, ...).
    # Declared bindings give GUID+type; Configurator.New("name", "guid") calls quoted in Evidence give the
    # parent-created blueprints those bindings live in (e.g. the RanRomAdd epilogue sequence).
    ev_rx = re.compile(r'(\w+)Configurator\.New\(\s*\\?"([^"\\]+)\\?"\s*,\s*\\?"([0-9a-fA-F-]{32,36})\\?"')
    for man in sorted((MOD / "reference/canon-review").glob("*parent*bindings*.json")):
        try:
            data = json.loads(man.read_text(encoding="utf-8"))
        except Exception:
            continue
        records, stack = [], [data]
        while stack:  # any object carrying Guid+Type, at any depth (Bindings, SequenceTopology, ...)
            o = stack.pop()
            if isinstance(o, dict):
                if isinstance(o.get("Guid"), str): records.append(o)
                stack.extend(o.values())
            elif isinstance(o, list):
                stack.extend(o)
        for b in records:
            if b.get("Type"):
                out.setdefault(b["Guid"].replace("-", "").lower(), (b["Type"], "parent-manifest:" + man.stem))
            for mm in ev_rx.finditer(b.get("Evidence", "") if isinstance(b.get("Evidence"), str) else ""):
                kind = mm.group(1)
                kind = {"CueSequence": "BlueprintCueSequence", "BookPage": "BlueprintBookPage", "AnswersList": "BlueprintAnswersList"}.get(kind, "Blueprint" + kind)
                out.setdefault(mm.group(3).replace("-", "").lower(), (kind, "parent-evidence:" + man.stem))
    return out


def rrt_guid(name):
    return hashlib.sha256(("RanRomance.Tirabade.v1/" + name).encode("utf-8")).digest()[:16].hex()


def build_names(model):
    """Every New<T>(id) name Main.Build() registers, in order (mirrors src/Main.cs)."""
    names = []
    scenes = model.scenes
    effects = []
    for s in scenes:
        for n in s["Nodes"]:
            for c in n["Choices"]:
                for f in c["Set"]:
                    if f not in effects: effects.append(f)
    keys = []
    for k in [s["Id"] for s in scenes] + ["hour." + s["Id"] for s in scenes] + effects + ["hour." + e for e in effects] + \
            [x for r in model.rels.values() for x in (r["StartedFlag"], r["ClosedFlag"], r["CommittedFlag"])]:
        if k not in keys: keys.append(k)
    flagkeys = list(keys)
    names += [("flag." + k, "BlueprintUnlockableFlag") for k in keys]
    extra_unguarded = ["konomi.return_meeting_retry", "nurah.private_meeting_retry"]
    names += [("flag." + k, "BlueprintUnlockableFlag") for k in extra_unguarded]
    for k in ["irabeth.return_meeting_retry", "irabeth.return_meeting_accepted", "hour.irabeth.return_meeting_accepted",
              "irabeth.return_meeting_declined", "irabeth.return_reply", "irabeth.return_first_words"]:
        if k not in keys: names.append(("flag." + k, "BlueprintUnlockableFlag"))
    names += [("etude.konomi.personal_return", "BlueprintEtude"), ("etude.irabeth.personal_return", "BlueprintEtude"),
              ("etude.nurah.private_meeting", "BlueprintEtude")]
    for rid in model.rels:
        suf = "" if rid == "tirabade" else "." + rid
        names += [("quest" + suf, "BlueprintQuest"), ("objective" + suf, "BlueprintQuestObjective")]
    for s in scenes:
        for n in s["Nodes"]:
            i = s["Id"] + "." + n["Id"]
            names.append(("cue." + i, "BlueprintCue"))
            if s["NativeReturnCue"] is None: names.append(("page." + i, "BlueprintBookPage"))
        for n in s["Nodes"]:
            ch = n["Choices"]
            ending = is_epilogue(s)
            if ending and len(ch) == 1 and ch[0]["Next"] is None and ch[0]["Check"] is None and not ch[0]["Requires"] \
                    and not ch[0]["Forbids"] and not ch[0]["Set"] and ch[0]["Text"] == "Continue" and not ch[0]["Abort"] and ch[0]["Revive"] is None:
                names.append(("answer.%s.%s.continue" % (s["Id"], n["Id"]), "BlueprintAnswer")); continue
            for i, c in enumerate(ch):
                names.append(("answer.%s.%s.%d" % (s["Id"], n["Id"], i), "BlueprintAnswer"))
                if c["Check"]: names.append(("check.%s.%s.%d" % (s["Id"], n["Id"], i), "BlueprintCheck"))
            if not ending and (s["ContactUnit"] is not None or is_remote(s)):
                names.append(("answer.%s.%s.contact_lost" % (s["Id"], n["Id"]), "BlueprintAnswer"))
        if s["NativeReturnCue"] is None: names.append(("dialog." + s["Id"], "BlueprintDialog"))
    if any(is_nurah_hub(s) for s in scenes):
        names += [("page.nurah.arrival_hub", "BlueprintBookPage"), ("cue.nurah.arrival_hub", "BlueprintCue")]
        names += [("answer.nurah.arrival_hub." + s["Id"], "BlueprintAnswer") for s in scenes if is_nurah_hub(s)]
        names += [("answer.nurah.arrival_hub.leave", "BlueprintAnswer"), ("dialog.nurah.arrival_hub", "BlueprintDialog")]
    for s in scenes:
        if is_epilogue(s) or is_remote(s) or s["InteractionHub"] is not None: continue
        names.append(("entry." + s["Id"], "BlueprintAnswer"))
    return names, flagkeys


# ------------------------------------------------------------------------------------------ validate port
def validate(model):
    """Python port of the structural parts of Rules.Validate (src/Story.cs). Returns list of errors."""
    errs = []
    st, rels = model.story, model.rels
    ids = set()
    relflags = set()
    for k, r in rels.items():
        for f in (r["StartedFlag"], r["ClosedFlag"], r["CommittedFlag"]):
            if not f or f in relflags: errs.append("Empty or shared relationship state: %s/%s" % (k, f))
            relflags.add(f)
    for k in model.permanent_etudes:
        if k not in model.etudes: errs.append("Unknown permanent etude: " + k)
    hexre = re.compile(r"^[0-9a-fA-F]{32}$")
    for s in model.scenes:
        sid = s["Id"]
        try:
            tg = entry_targets(s)
        except ValueError as e:
            errs.append(str(e)); tg = []
        if s["InteractionHub"] is not None and not is_nurah_hub(s): errs.append("Invalid Nurah hub contract: " + sid)
        if s["Relationship"] == "nurah" and not is_remote(s) and not is_nurah_hub(s): errs.append("Physical Nurah scene without hub: " + sid)
        if s["ManualOnly"] and not is_remote(s): errs.append("ManualOnly non-remote: " + sid)
        if not sid or sid in ids: errs.append("Duplicate or empty scene: " + sid)
        ids.add(sid)
        if s["Relationship"] not in rels: errs.append("Unknown relationship: %s (%s)" % (s["Relationship"], sid))
        for g in tg + list(s["Areas"]) + ([s["ContactUnit"]] if s["ContactUnit"] else []) + list(s["AdditionalContactUnits"]):
            if not hexre.match(g or ""): errs.append("Bad GUID in %s: %s" % (sid, g))
        if s["AdditionalContactUnits"] and not s["ContactUnit"]: errs.append("AdditionalContactUnits without ContactUnit: " + sid)
        if s["Recovery"] and (s["Recovery"] not in model.revivals or model.revivals[s["Recovery"]]["Relationship"] != s["Relationship"] or not is_remote(s)):
            errs.append("Invalid recovery scene: " + sid)
        if any(c < s["MinChapter"] or c > s["MaxChapter"] for c in s["Chapters"]) or len(set(s["Chapters"])) != len(s["Chapters"]) or s["DelayHours"] < 0:
            errs.append("Invalid chapter/timing: " + sid)
        if not s["Nodes"] or s["MinChapter"] > s["MaxChapter"]: errs.append("Invalid scene: " + sid)
        for a, b in s["ForbidOverrides"].items():
            if a not in s["Forbids"] or a not in model.authored or b not in model.authored or a == b:
                errs.append("Invalid forbid override %s/%s" % (sid, a))
        nodes = {}
        for n in s["Nodes"]:
            if n["Id"] in nodes or not n["Text"].strip() or not n["Choices"]: errs.append("Invalid node: %s/%s" % (sid, n["Id"]))
            nodes[n["Id"]] = n
        for n in s["Nodes"]:
            for c in n["Choices"]:
                if set(c["Set"]) & CONTACT_EVIDENCE: errs.append("Authored contact evidence: " + sid)
                if c["Next"] is not None and c["Next"] not in nodes: errs.append("Missing node: %s/%s" % (sid, c["Next"]))
                ck = c["Check"]
                if ck and (c["Next"] is not None or c["Abort"] or c["Revive"] is not None or is_epilogue(s)
                           or ck.get("Skill") not in CHECK_SKILLS or ck.get("DC", 0) <= 0 or ck.get("Success") == ck.get("Failure")
                           or ck.get("Success") not in nodes or ck.get("Failure") not in nodes):
                    errs.append("Invalid skill check: %s/%s" % (sid, n["Id"]))
                if c["Revive"] is not None and (c["Revive"] != s["Recovery"] or c["Next"] is not None or c["Abort"]):
                    errs.append("Revival must be terminal recovery choice: " + sid)
        if s["Nodes"]:
            seen, stack = set(), [s["Nodes"][0]["Id"]]
            while stack:
                x = stack.pop()
                if x in seen or x not in nodes: continue
                seen.add(x)
                for c in nodes[x]["Choices"]: stack.extend(next_nodes(c))
            if len(seen) != len(nodes): errs.append("Unreachable node in %s: %s" % (sid, sorted(set(nodes) - seen)))
    return errs


# --------------------------------------------------------------------------------------------- helpers
def scene_source_map(mod):
    """scene id -> source .py file (first file containing the id as a string literal)."""
    files = [mod / "story.py"] + sorted((mod / "storylines").glob("*.py"))
    lit = {}
    rx = re.compile(r'''["']([A-Za-z0-9_.\-]+)["']''')
    for p in files:
        for mm in rx.finditer(p.read_text(encoding="utf-8", errors="replace")):
            lit.setdefault(mm.group(1), p.name)
    def find(sid):
        if sid in lit: return lit[sid]
        pre = sid.rsplit(".", 1)[0]
        return lit.get(pre, "?(generated id)")
    return find


def load_loc(game):
    p = game / "Wrath_Data/StreamingAssets/Localization/enGB.json"
    try:
        d = json.loads(p.read_text(encoding="utf-8-sig"))
        return d.get("strings", d)
    except Exception:
        return {}


def native_words(loc):
    blob = " ".join(v if isinstance(v, str) else (str(v.get("Text", "")) if isinstance(v, dict) else str(v)) for v in loc.values())
    return set(re.findall(r"\b[A-Z][a-z]{2,}\b", blob))


QUOTE_START = ('"', "\u201c", "'")
THIRD = re.compile(r"^(She|He|The|Her|His|You|Your|They|Their|It|Its|A|An|Nothing|Something|Somewhere|For a|After|When|Then)\b")


def narration_lint(text, speaker):
    """Return list of (kind, line) for lines that look like narration but are not {n}-tagged."""
    out = []
    inside = False
    for raw in text.split("\n"):
        line = raw.strip()
        if not line: continue
        tagged = inside or line.startswith("{n}")
        # track multi-line {n} blocks
        opens, closes = line.count("{n}"), line.count("{/n}")
        if line.startswith("{n}"): inside = opens > closes
        elif inside and closes > opens: inside = False
        if tagged: continue
        plain = re.sub(r"\{[^}]*\}", "", line)
        if plain.startswith(QUOTE_START):
            # quote followed by an untagged attribution clause:  "Hi," she says.
            if re.search(r'["\u201d]\s*,?\s+(she|he|they|you|her|his)\s+[a-z]+', plain):
                out.append(("attribution-outside-{n}", line))
            continue
        if speaker != "Narrator":
            out.append(("unquoted-prose-in-speaker-node", line))
        elif THIRD.match(plain):
            out.append(("untagged-narration-in-narrator-node", line))
    return out


# ------------------------------------------------------------------------------------------------ main
def run(story_path, game, use_zip=True, drafts=False, out_json=None, quiet=False, story_obj=None, label="development"):
    t0 = time.time()
    R = collections.OrderedDict()
    story = story_obj if story_obj is not None else json.loads(Path(story_path).read_text(encoding="utf-8"))
    model = Model(story)
    lines = []
    def P(*a):
        lines.append(" ".join(str(x) for x in a))
    P("# rrt_verify report (%s): %d scenes, %d relationships, %d native bindings" % (label, len(model.scenes), len(model.rels), len(model.native)))

    # ---- structural validate
    verrs = validate(model)
    R["validate_errors"] = verrs
    P("\n## Validate port (structural subset of Rules.Validate): %d errors" % len(verrs))
    for e in verrs[:40]: P("  -", e)

    # ---- A. producers
    refs = model.all_referenced()
    no_producer = {}
    for f, where in refs.items():
        if f in model.producers or f in model.native or f in model.derived: continue
        no_producer[f] = where
    # flags only produced by epilogue scenes but required by non-epilogue content
    R["no_producer"] = {f: w[:6] for f, w in no_producer.items()}
    P("\n## A. Flags referenced with NO producer (no choice Set, no scene completion, not native/derived): %d" % len(no_producer))
    for f, w in sorted(no_producer.items()):
        kinds = collections.Counter(k for _, k in w)
        P("  - %-45s used %d x %s  e.g. %s" % (f, len(w), dict(kinds), w[0][0]))
    # forbid-only flags with no producer are harmless; requires ones are fatal
    fatal = {f: w for f, w in no_producer.items() if any(k in ("Requires", "choice.Requires", "RequiresAnyGroups", "ForbidOverride") for _, k in w)}
    R["no_producer_required"] = sorted(fatal)
    P("  => of which REQUIRED somewhere (hard dead gates): %d %s" % (len(fatal), sorted(fatal)[:30]))

    relnp = []
    for rk, r in model.rels.items():
        for kind in ("ClosedFlag", "CommittedFlag"):
            if r[kind] not in model.producers: relnp.append("%s.%s=%s" % (rk, kind, r[kind]))
    R["relationship_flags_without_producer"] = relnp
    P("  Relationship Closed/Committed flags that NOTHING sets (route can never close/commit; journal objective never completes): %s" % relnp)

    # ---- B. reachability per mythic world
    worlds = [mythic_world(m, model) for m in MYTHIC] + [mythic_world(None, model, "none")]
    reach = {}
    for w in worlds:
        reach[w.name] = Reach(model, w)
    any_reached = set().union(*[set(r.reached) for r in reach.values()])
    free_reached = set()
    for w in worlds:
        free_reached |= set(Reach(model, w, chaptered=False).reached)
    never = [s for s in model.scenes if s["Id"] not in any_reached]
    R["unreachable_all_paths"] = {}
    P("\n## B. Scenes unreachable on EVERY mythic path (fixed point, chaptered): %d of %d" % (len(never), len(model.scenes)))
    by_rel = collections.defaultdict(list)
    for s in never:
        why = reach["trickster"].why.get(s["Id"]) or reach["trickster"].dead_scenes.get(s["Id"]) or "?"
        if s["Id"] in free_reached: why = "CHAPTER-TRAP (reachable if chapters ignored) / " + why
        R["unreachable_all_paths"][s["Id"]] = why
        by_rel[s["Relationship"]].append((s["Id"], why))
    for rel, lst in sorted(by_rel.items()):
        P("  [%s] %d" % (rel, len(lst)))
        for sid, why in lst[:25]: P("     - %-55s %s" % (sid, why))
        if len(lst) > 25: P("     ... +%d more" % (len(lst) - 25))
    # per path reachability of relationship start/commit
    P("\n## B2. Per mythic path: relationship entry / committed-flag reachability (E=entry scene reachable, C=CommittedFlag reachable, X=ClosedFlag)")
    hdr = "  %-22s" % "relationship" + "".join("%-10s" % w.name[:9] for w in worlds)
    P(hdr)
    matrix = {}
    for rk, r in model.rels.items():
        row = "  %-22s" % rk[:22]
        matrix[rk] = {}
        for w in worlds:
            rr = reach[w.name]
            ent = any(s["Relationship"] == rk and not is_epilogue(s) and s["Id"] in rr.reached for s in model.scenes)
            com = r["CommittedFlag"] in rr.held
            clo = r["ClosedFlag"] in rr.held
            cell = ("E" if ent else "-") + ("C" if com else "-") + ("X" if clo else "-")
            matrix[rk][w.name] = cell
            row += "%-10s" % cell
        P(row)
    R["path_matrix"] = matrix
    dead_choice_ct = collections.Counter()
    for k, v in reach["trickster"].dead_choices.items(): dead_choice_ct[model.by_id[k[0]]["Relationship"]] += 1
    all_dead = set()
    for rr0 in reach.values():
        for k in rr0.dead_choices:
            if not any(k in r.choices for r in reach.values()): all_dead.add(k)
    R["dead_choices_all_paths"] = ["%s/%s/%d" % k for k in sorted(all_dead)]
    P("\n  Choices dead on every path (forbid/requires contradiction inside own chain): %d" % len(all_dead))
    for k in sorted(all_dead)[:40]:
        why = next(r.dead_choices[k] for r in reach.values() if k in r.dead_choices)
        P("     -", "%s/%s/%d" % k, why)
    unused_choices = []
    for s in model.scenes:
        if s["Id"] not in any_reached: continue
        for n in s["Nodes"]:
            for i, c in enumerate(n["Choices"]):
                if not any((s["Id"], n["Id"], i) in r.choices for r in reach.values()) and (s["Id"], n["Id"], i) not in all_dead:
                    unused_choices.append("%s/%s/%d" % (s["Id"], n["Id"], i))
    R["unreachable_choices_in_reachable_scenes"] = unused_choices
    P("  Other choices never selectable inside otherwise-reachable scenes (no path found; see why): %d" % len(unused_choices))
    for x in unused_choices[:25]:
        sid, nid, i = x.split("/")
        c = model.nodes[sid][nid]["Choices"][int(i)]
        P("     - %-55s req %s forb %s" % (x, c["Requires"], c["Forbids"]))

    # ---- H. Trickster roster matrix with blocking states
    P("\n## H. Trickster access per relationship (world = trickster etude playing; variants force a native state true or false)")
    tri = {}
    for rk, r in model.rels.items():
        rel_scenes = [s for s in model.scenes if s["Relationship"] == rk and not is_epilogue(s)]
        cand_true = set(f for f in r.get("UnavailableFlags", []) if f in model.native and f not in MYTHIC)
        cand_false = set()
        for s in rel_scenes:
            for f in s["Forbids"]:
                if f in model.native and f not in MYTHIC: cand_true.add(f)
            for f in list(s["Requires"]) + list(s["RequiresAny"]):
                if f in model.native and f not in MYTHIC and f != "trickster": cand_false.add(f)
        base = reach["trickster"]
        base_ent = [s["Id"] for s in rel_scenes if s["Id"] in base.reached]
        res = dict(entry=bool(base_ent), committed=r["CommittedFlag"] in base.held, entry_scenes=len(base_ent),
                   total_scenes=len(rel_scenes), blocks_entry=[], blocks_commit=[])
        for f in sorted(cand_true):
            rr = Reach(model, mythic_world("trickster", model, "tri+" + f, true={f}))
            e = any(s["Id"] in rr.reached for s in rel_scenes)
            if not e: res["blocks_entry"].append(f + "=true")
            elif r["CommittedFlag"] not in rr.held and res["committed"]: res["blocks_commit"].append(f + "=true")
        for f in sorted(cand_false):
            rr = Reach(model, mythic_world("trickster", model, "tri-" + f, false={f}))
            e = any(s["Id"] in rr.reached for s in rel_scenes)
            if not e: res["blocks_entry"].append(f + "=missed")
            elif r["CommittedFlag"] not in rr.held and res["committed"]: res["blocks_commit"].append(f + "=missed")
        tri[rk] = res
        P("  %-17s entry=%-5s committed(%s)=%-5s scenes %d/%d reachable" % (rk, res["entry"], r["CommittedFlag"], res["committed"], res["entry_scenes"], res["total_scenes"]))
        if res["blocks_entry"]: P("       entry blocked by:", ", ".join(res["blocks_entry"]))
        if res["blocks_commit"]: P("       commit blocked by:", ", ".join(res["blocks_commit"]))
    R["trickster"] = tri
    # roster characters without a relationship
    roster = []
    rp = MOD / "ROSTER.md"
    if rp.is_file():
        for line in rp.read_text(encoding="utf-8").splitlines():
            mm = re.match(r"^\|\s*([A-Z][A-Za-z' ]+?)\s*\|", line)
            if mm and mm.group(1) not in ("Character", "Candidate") and not line.startswith("| ---"):
                roster.append(mm.group(1).strip())
    alias = {"minagho": "minagho_chivarro", "chivarro": "minagho_chivarro", "anevia": "anevia", "irabeth": "irabeth"}
    drafts_by_char = collections.defaultdict(list)
    registered_mods = registered_modules(MOD)
    for p in (MOD / "storylines").glob("*.py"):
        if p.stem not in registered_mods: drafts_by_char[p.stem.split("_")[0]].append(p.stem)
    R["roster"] = []
    P("\n## H2. Roster matrix (ROSTER.md) x Story.json")
    P("  %-22s %-18s %-6s %-6s %-6s %s" % ("character", "relationship", "reg?", "T-ent", "T-end", "notes"))
    for name in roster:
        key = name.lower().split()[0]
        rk = alias.get(key, key)
        if rk in model.rels:
            t = tri[rk]
            note = "; ".join(t["blocks_entry"][:4] + ["commit:" + x for x in t["blocks_commit"][:3]])
            P("  %-22s %-18s %-6s %-6s %-6s %s" % (name, rk, "yes", t["entry"], t["committed"], note))
            R["roster"].append(dict(character=name, relationship=rk, registered=True, trickster_entry=t["entry"],
                                    trickster_end=t["committed"], blocks=t["blocks_entry"], commit_blocks=t["blocks_commit"]))
        else:
            d = drafts_by_char.get(key, [])
            P("  %-22s %-18s %-6s %-6s %-6s %s" % (name, "-", "NO", "-", "-", ("draft modules: " + ",".join(d)) if d else "no Story.json relationship and no draft"))
            R["roster"].append(dict(character=name, relationship=None, registered=False, drafts=d))

    # ---- C. chapter / delay traps
    P("\n## C. Chapter-window / delay traps")
    traps = [sid for sid, why in R["unreachable_all_paths"].items() if why.startswith("CHAPTER-TRAP")]
    P("  Chapter traps (reachable only if chapter order ignored): %d %s" % (len(traps), traps[:20]))
    # delay chains inside single-chapter windows
    def window(s):
        return tuple(s["Chapters"]) if s["Chapters"] else tuple(range(s["MinChapter"], min(s["MaxChapter"], 6) + 1))
    memo = {}
    def chain(sid, depth=0):
        if sid in memo: return memo[sid]
        if depth > 60: return (0, [sid])
        memo[sid] = (0, [sid])
        s = model.by_id[sid]
        w = window(s)
        best = (0, [])
        for r in s["Requires"]:
            cand = None
            for (psid, _, _) in model.producers.get(r, []):
                ps = model.by_id.get(psid)
                if not ps or set(window(ps)) - set(w) or psid == sid: cand = (0, []) if cand is None else min(cand, (0, [])); continue
                c = chain(psid, depth + 1)
                cand = c if cand is None or c[0] < cand[0] else cand
            if cand and cand[0] > best[0]: best = cand
        memo[sid] = (best[0] + s["DelayHours"], best[1] + [sid])
        return memo[sid]
    long_chains = []
    for s in model.scenes:
        w = window(s)
        if len(w) == 1 and not is_epilogue(s):
            h, path = chain(s["Id"])
            if h >= 120: long_chains.append((h, w[0], s["Id"], path))
    long_chains.sort(reverse=True)
    R["delay_chains"] = [dict(hours=h, chapter=c, scene=sid, chain=p) for h, c, sid, p in long_chains]
    P("  Scenes in a single-chapter window whose minimum in-window delay chain is >= 120h: %d" % len(long_chains))
    for h, c, sid, p in long_chains[:15]: P("     - ch%d %4dh %-45s chain len %d" % (c, h, sid, len(p)))
    remote = [s for s in model.scenes if is_remote(s) and not s["ManualOnly"] and not is_epilogue(s)]
    comp = {}
    for ch in range(1, 6):
        comp[ch] = collections.Counter(s["Relationship"] for s in remote if s["MinChapter"] <= ch <= s["MaxChapter"] and (not s["Chapters"] or ch in s["Chapters"]))
    order = []
    for s in model.scenes:
        if is_remote(s) and not s["ManualOnly"] and s["Relationship"] not in order: order.append(s["Relationship"])
    R["remote_order"] = order
    P("  Rest-letter delivery: NextRemote picks the FIRST available remote scene in list order. Relationship priority order:", order)
    for ch, c in comp.items(): P("     ch%d competing remote scenes by relationship: %s" % (ch, dict(c)))
    # volatile etudes used as history
    vol = []
    for f, where in refs.items():
        if model.native.get(f) == "Etudes" and not model.is_persistent_native(f) and f not in MYTHIC:
            hist = bool(HIST_WORDS.search(f))
            vol.append((not hist, f, hist, collections.Counter(k for _, k in where), where[0][0]))
    vol.sort()
    R["volatile_etudes"] = [dict(flag=f, looks_historical=h, uses=dict(u), example=e) for _, f, h, u, e in vol]
    P("\n  Etude bindings read only while IsPlaying (NOT permanent in State()) but used as gates: %d; name looks like one-time history: %d"
      % (len(vol), sum(1 for v in vol if v[2])))
    for _, f, h, u, e in vol:
        P("     %s %-38s %s  e.g. %s" % ("HIST" if h else "    ", f, dict(u), e))

    # ---- D. cross-route forbid matrix
    P("\n## D. Cross-route forbid conflicts (flag produced by route A, forbidden by route B)")
    prod_rel = collections.defaultdict(set)
    for f, lst in model.producers.items():
        for (sid, _, _) in lst: prod_rel[f].add(model.by_id[sid]["Relationship"])
    forb = collections.defaultdict(lambda: collections.defaultdict(list))
    for s in model.scenes:
        for f in s["Forbids"]:
            for a in prod_rel.get(f, ()):
                if a != s["Relationship"]: forb[a][s["Relationship"]].append((f, s["Id"], "scene"))
        for n in s["Nodes"]:
            for i, c in enumerate(n["Choices"]):
                for f in c["Forbids"]:
                    for a in prod_rel.get(f, ()):
                        if a != s["Relationship"]: forb[a][s["Relationship"]].append((f, "%s/%s/%d" % (s["Id"], n["Id"], i), "choice"))
    for rk, r in model.rels.items():
        for f in r.get("UnavailableFlags", []) + r.get("FailureFlags", []):
            for a in prod_rel.get(f, ()):
                if a != rk: forb[a][rk].append((f, "rel:" + rk, "relationship"))
    R["forbid_matrix"] = {a: {b: [list(x) for x in v] for b, v in d.items()} for a, d in forb.items()}
    nconf = 0
    for a, d in sorted(forb.items()):
        for b, v in sorted(d.items()):
            flags = sorted(set(x[0] for x in v))
            scenes_hit = len(set(x[1] for x in v if x[2] == "scene"))
            nconf += 1
            P("  %-16s -> %-16s flags %s  (%d scenes, %d choice gates)" % (a, b, flags[:6], scenes_hit, sum(1 for x in v if x[2] == "choice")))
    if not nconf: P("  none")

    # ---- D2. coexistence (Directives v2): no route may depend on another romanceable being dead/departed/hostile/closed
    P("\n## D2. Coexistence: scenes/endings/choices whose gates depend on ANOTHER relationship's loss/closure or romance state")
    chars = {rk: set() for rk in model.rels}
    for rk in model.rels:
        base = rk.split(".")[0]
        chars[rk] |= {base}
    chars.setdefault("tirabade", set()).update({"anevia", "irabeth", "tirabade"})
    for k in ("minagho_chivarro",):
        if k in chars: chars[k] |= {"minagho", "chivarro", "minachiv"}
    for k in list(chars):
        if k.startswith("nocticula"): chars[k] |= {"noct", "nocticula"}
    tok2rels = collections.defaultdict(set)
    for rk, cs in chars.items():
        for c in cs: tok2rels[c].add(rk)
    flag_owner = {}
    for rk, r in model.rels.items():
        for f in (r["StartedFlag"], r["ClosedFlag"], r["CommittedFlag"]): flag_owner[f] = {rk}
    def owners(f):
        if f in flag_owner: return flag_owner[f]
        tok = re.split(r"[._]", f)[0]
        o = set(tok2rels.get(tok, ()))
        for rk, r in model.rels.items():
            if f in r.get("UnavailableFlags", []) and f not in MYTHIC and f != "true_lich": o.add(rk)
        return o
    LOSS = re.compile(r"dead|gone|away|absent|killed|condemned|prison|unavailable|early_fight|final_fight|detached|closed|departure|departed|hostile|killing|rejected|lost|victims_revived|native_devastated|searching")
    ROM = re.compile(r"committed|lover|courtship|started|romance|complete|renewed|kept|trusted|affair")
    coex = []
    for s in model.scenes:
        rk = s["Relationship"]
        mine = chars.get(rk, set())
        def other(f):
            o = owners(f) - {rk}
            if not o: return None
            if any(tok in mine for tok in [re.split(r"[._]", f)[0]]): return None
            return o
        pos = list(s["Requires"]) + list(s["RequiresAny"]) + [x for g in s["RequiresAnyGroups"] for x in g]
        for f in pos:
            o = other(f)
            if o and LOSS.search(f): coex.append(("REQUIRES-OTHER-LOSS", s["Id"], f, sorted(o), is_epilogue(s)))
        for f in s["Forbids"]:
            o = other(f)
            if o and ROM.search(f) and not LOSS.search(f): coex.append(("FORBIDS-OTHER-ROMANCE", s["Id"], f, sorted(o), is_epilogue(s)))
        for n in s["Nodes"]:
            for i, c in enumerate(n["Choices"]):
                for f in c["Requires"]:
                    o = other(f)
                    if o and LOSS.search(f): coex.append(("choice-requires-other-loss", "%s/%s/%d" % (s["Id"], n["Id"], i), f, sorted(o), is_epilogue(s)))
                for f in c["Forbids"]:
                    o = other(f)
                    if o and ROM.search(f) and not LOSS.search(f): coex.append(("choice-forbids-other-romance", "%s/%s/%d" % (s["Id"], n["Id"], i), f, sorted(o), is_epilogue(s)))
    R["coexistence"] = [dict(kind=k, where=w, flag=f, other=o, epilogue=e) for k, w, f, o, e in coex]
    cc = collections.Counter((k, s_rel(model, w), tuple(o)) for k, w, f, o, e in coex)
    P("  %d gate uses. By (kind, route -> other):" % len(coex))
    for (k, a, o), n in sorted(cc.items(), key=lambda x: (x[0][0], -x[1])):
        ex = next((w, f) for kk, w, f, oo, e in coex if kk == k and s_rel(model, w) == a and tuple(oo) == o)
        P("     %-30s %-18s -> %-28s x%-3d e.g. %s [%s]" % (k, a, ",".join(o), n, ex[0], ex[1]))

    # ---- D3. epilogue guards (Rules.Available returns true for Epilogue owners BEFORE relationship Closed/Unavailable checks)
    P("\n## D3. Epilogue scenes not guarded against their relationship's ClosedFlag / UnavailableFlags (Story.cs:205 skips those checks)")
    eg = []
    for s in model.scenes:
        if not is_epilogue(s): continue
        r = model.rels.get(s["Relationship"])
        if not r: continue
        pos = set(s["Requires"]) | set(s["RequiresAny"]) | {x for g in s["RequiresAnyGroups"] for x in g}
        guards = [r["ClosedFlag"]] + [f for f in r.get("UnavailableFlags", [])]
        # a scene that REQUIRES any loss/closure flag is an explicit loss ending: exempt
        if pos & (set(guards) | {"loss", "inhuman"} | set(r.get("FailureFlags", []))): continue
        req_mythic = pos & set(MYTHIC + ["true_lich"])
        missing = [f for f in guards if f not in s["Forbids"] and not (req_mythic and f in MYTHIC + ["true_lich"])]
        if missing: eg.append((s["Id"], s["Relationship"], missing))
    R["epilogue_unguarded"] = [dict(scene=a, relationship=b, missing_forbids=c) for a, b, c in eg]
    byr = collections.Counter(b for _, b, _ in eg)
    P("  %d of %d epilogue scenes lack at least one guard. By relationship: %s" % (len(eg), sum(1 for s in model.scenes if is_epilogue(s)), dict(byr)))
    for a, b, c in eg[:25]: P("     - %-45s %-16s missing forbids %s" % (a, b, c))

    # ---- E. lints
    P("\n## E. Lints")
    src_of = scene_source_map(MOD)
    lint = collections.OrderedDict()
    ent = collections.defaultdict(list)
    for s in model.scenes:
        try:
            for t in entry_targets(s): ent[(t, s["Entry"].strip().lower())].append(s["Id"])
        except ValueError:
            pass
    dups = {"%s | %s" % k: v for k, v in ent.items() if len(v) > 1}
    lint["duplicate_entry_text_same_list"] = dups
    P("  Duplicate entry text on the same native answer list: %d" % len(dups))
    for k, v in list(dups.items())[:10]: P("     -", k[:90], v)
    per_list = collections.Counter(t for (t, _), v in ent.items() for _ in v)
    lint["entries_per_list"] = dict(per_list.most_common())
    P("  RRT entry answers injected per native answer list (each evaluates ShowConditions+SelectConditions -> State()):", dict(per_list.most_common(8)))
    # portraits
    art = MOD / "art/CustomNpcPortraits/RanRomance-Tirabade/Scenes"
    have = {p.stem for p in art.glob("*.png")} if art.is_dir() else set()
    need = collections.Counter()
    for s in model.scenes:
        for n in s["Nodes"]:
            key = n["Portrait"] or ("Together" if n["Speaker"] == "Narrator" else n["Speaker"])
            need[key] += 1
    miss = {k: v for k, v in need.items() if k not in have}
    lint["missing_portraits"] = miss
    P("  Portrait keys without Scenes/<key>.png (page shows native/blank picture): %d keys, %d nodes %s" % (len(miss), sum(miss.values()), dict(sorted(miss.items(), key=lambda x: -x[1])[:15])))
    # sizes
    over, emp = [], []
    for s in model.scenes:
        if len(s["Entry"]) > DEFAULT_LIMITS["entry_chars"] and entry_targets_safe(s): over.append(("entry", s["Id"], len(s["Entry"])))
        if not s["Entry"].strip() and entry_targets_safe(s): emp.append(("entry", s["Id"]))
        for n in s["Nodes"]:
            if len(n["Text"]) > DEFAULT_LIMITS["node_chars"]: over.append(("node", "%s/%s" % (s["Id"], n["Id"]), len(n["Text"])))
            if not n["Text"].strip(): emp.append(("node", "%s/%s" % (s["Id"], n["Id"])))
            for i, c in enumerate(n["Choices"]):
                if len(c["Text"]) > DEFAULT_LIMITS["choice_chars"]: over.append(("choice", "%s/%s/%d" % (s["Id"], n["Id"], i), len(c["Text"])))
                if not c["Text"].strip(): emp.append(("choice", "%s/%s/%d" % (s["Id"], n["Id"], i)))
    lint["overlong"] = over; lint["empty"] = emp
    oc = collections.Counter(k for k, _, _ in over)
    P("  Overlong (node>%d, choice>%d, entry>%d chars): %s; empty: %d" % (DEFAULT_LIMITS["node_chars"], DEFAULT_LIMITS["choice_chars"], DEFAULT_LIMITS["entry_chars"], dict(oc), len(emp)))
    for x in sorted(over, key=lambda x: -x[2])[:8]: P("     -", x)
    # formatting
    fmt = collections.defaultdict(collections.Counter)
    narr = collections.defaultdict(collections.Counter)
    narr_examples = collections.defaultdict(list)
    for s in model.scenes:
        src = src_of(s["Id"])
        texts = [s["Entry"], s["Title"]] + [n["Text"] for n in s["Nodes"]] + [c["Text"] for n in s["Nodes"] for c in n["Choices"]]
        for t in texts:
            fmt[src]["em-dash"] += t.count("\u2014")
            fmt[src]["en-dash"] += t.count("\u2013")
            fmt[src]["double-hyphen"] += t.count("--")
            fmt[src]["double-space"] += len(re.findall(r"[^ \n]  +[^ ]", t))
            fmt[src]["unbalanced-{n}"] += int(t.count("{n}") != t.count("{/n}"))
            fmt[src]["odd-quotes"] += int(t.count('"') % 2 == 1)
            fmt[src]["curly-quotes"] += t.count("\u201c") + t.count("\u201d")
        for n in s["Nodes"]:
            for kind, line in narration_lint(n["Text"], n["Speaker"]):
                narr[src][kind] += 1
                if len(narr_examples[src]) < 3: narr_examples[src].append("%s/%s: %s" % (s["Id"], n["Id"], line[:90]))
    lint["formatting_by_file"] = {k: dict(v) for k, v in fmt.items() if sum(v.values())}
    lint["narration_by_file"] = {k: dict(v) for k, v in narr.items()}
    lint["narration_examples"] = narr_examples
    P("  Formatting by source file (non-zero):")
    for f, c in sorted(fmt.items()):
        c = {k: v for k, v in c.items() if v}
        if c: P("     %-38s %s" % (f, c))
    P("  Narration-tag lint by source file (lines that read as narration but lack {n}...{/n}):")
    for f, c in sorted(narr.items(), key=lambda x: -sum(x[1].values())):
        P("     %-38s %s  e.g. %s" % (f, dict(c), narr_examples[f][:1]))
    # name collisions
    loc = load_loc(game)
    nw = native_words(loc)
    corpus_lower = set()
    per_rel_names = collections.defaultdict(set)
    for s in model.scenes:
        texts = [n["Text"] for n in s["Nodes"]] + [c["Text"] for n in s["Nodes"] for c in n["Choices"]]
        for t in texts:
            corpus_lower.update(w for w in re.findall(r"\b[a-z]{3,}\b", t))
            for mm in re.finditer(r"(?<![.!?\"\u201c\n] )(?<!^)\b([A-Z][a-z]{2,})\b", t):
                per_rel_names[mm.group(1)].add(s["Relationship"])
    coll = {w: sorted(r) for w, r in per_rel_names.items() if len(r) > 1 and w.lower() not in corpus_lower and w not in nw}
    lint["invented_name_collisions"] = coll
    P("  Invented proper names (not in native enGB localization) used in >1 relationship: %d" % len(coll))
    for w, r in sorted(coll.items()): P("     - %-14s %s" % (w, r))
    # unregistered modules
    unreg = sorted(p.stem for p in (MOD / "storylines").glob("*.py") if p.stem not in registered_mods)
    lint["unregistered_modules"] = unreg
    P("  Unregistered storyline modules (not imported by expansion.py):", unreg)
    # choice-index stability vs previous exports
    for prev_label, prev_path in previous_exports():
        try:
            prev = Model(json.loads(Path(prev_path).read_text(encoding="utf-8")))
        except Exception as e:
            P("  (could not read %s: %s)" % (prev_path, e)); continue
        prev_names = set(n for n, _ in build_names(prev)[0])
        cur_names = set(n for n, _ in build_names(model)[0])
        removed = sorted(prev_names - cur_names)
        drift = []
        for s in prev.scenes:
            cs = model.by_id.get(s["Id"])
            if not cs: continue
            cn = {n["Id"]: n for n in cs["Nodes"]}
            for n in s["Nodes"]:
                if n["Id"] not in cn: continue
                a, b = n["Choices"], cn[n["Id"]]["Choices"]
                for i in range(min(len(a), len(b))):
                    if difflib.SequenceMatcher(None, a[i]["Text"], b[i]["Text"]).ratio() < 0.6 or a[i]["Set"] != b[i]["Set"]:
                        drift.append("%s/%s/%d" % (s["Id"], n["Id"], i))
        if prev_label.startswith("released-") and removed:
            R.setdefault("released_names_removed", []).extend(prev_label + ": " + x for x in removed)
        lint["vs_" + prev_label] = dict(removed_blueprint_names=len(removed), removed_examples=removed[:20], index_drift=drift[:200], index_drift_count=len(drift))
        P("  vs %s: %d RRT blueprint names registered then but NOT now (saves referencing them fail to resolve); %d answer slots whose text/Set changed at the same index"
          % (prev_label, len(removed), len(drift)))
        for x in removed[:6]: P("     removed:", x)
        for x in drift[:6]: P("     drift:", x)
    R["lint"] = lint

    # ---- G. runtime risk metrics / Build() mirrors
    names, flagkeys = build_names(model)
    cnt = collections.Counter(n for n, _ in names)
    dupn = {n: c for n, c in cnt.items() if c > 1}
    guids = collections.defaultdict(list)
    for n, t in names: guids[rrt_guid(n)].append(n)
    hashcoll = {g: v for g, v in guids.items() if len(set(v)) > 1}
    extra_dups = [k for k in ("konomi.return_meeting_retry", "nurah.private_meeting_retry") if k in flagkeys]
    contact_units = set()
    for s in model.scenes:
        if s["ContactUnit"]: contact_units |= {s["ContactUnit"], *s["AdditionalContactUnits"]}
    text_keys = collections.Counter()
    P("\n## G. Build()/State() mirrors")
    P("  New<T> registrations: %d (flags %d). Duplicate names (=> New throws 'Blueprint collision', Build aborts): %d %s"
      % (len(names), sum(1 for _, t in names if t == "BlueprintUnlockableFlag"), len(dupn), list(dupn)[:8]))
    P("  SHA256 GuidFor collisions between distinct names: %d; unguarded retry flags also authored (flags.Add dup => Build aborts): %s" % (len(hashcoll), extra_dups))
    P("  State() per call: %d UnlockableFlag reads, %d etude facts, %d quests, %d seen-cue sets, %d contact-unit scans (each walks game.State.Units), %d revival scans"
      % (sum(1 for _, t in names if t == "BlueprintUnlockableFlag"), len(model.etudes), len(story.get("CompletedQuests", {})),
         len(story.get("SeenCues", {})), len(contact_units), len(model.revivals)))
    worst = max(per_list.values()) if per_list else 0
    P("  Worst native answer list carries %d RRT entries -> up to %d State() snapshots each time that list is shown (Show+Select)" % (worst, worst * 2))
    R["runtime"] = dict(new_names=len(names), duplicate_names=dupn, guid_collisions=hashcoll, retry_dups=extra_dups,
                        contact_units=len(contact_units), worst_list_entries=worst)

    # ---- F. GUID bindings against blueprints.zip
    if use_zip:
        tz = time.time()
        idx, typeids = build_bp_index(game)
        par = parent_bindings()
        want = []
        for k, g in story.get("Etudes", {}).items(): want.append((g, "BlueprintEtude", "Etudes." + k))
        for k, g in story.get("CompletedEtudes", {}).items(): want.append((g, "BlueprintEtude", "CompletedEtudes." + k))
        for k, g in story.get("CompletedQuests", {}).items(): want.append((g, "BlueprintQuest", "CompletedQuests." + k))
        for k, v in story.get("SeenCues", {}).items():
            for g in v: want.append((g, "BlueprintCue", "SeenCues." + k))
        for k, g in story.get("SelectedAnswers", {}).items(): want.append((g, "BlueprintAnswer", "SelectedAnswers." + k))
        for k, g in story.get("StartedDialogs", {}).items(): want.append((g, "BlueprintDialog", "StartedDialogs." + k))
        for k, v in model.revivals.items(): want.append((v["Unit"], "BlueprintUnit", "Revivals." + k))
        for s in model.scenes:
            for g in ([s["ContactUnit"]] if s["ContactUnit"] else []) + list(s["AdditionalContactUnits"]): want.append((g, "BlueprintUnit", "ContactUnit@" + s["Id"]))
            try:
                for g in entry_targets(s): want.append((g, "BlueprintAnswersList", "AnswerList@" + s["Id"]))
            except ValueError: pass
            for g in s["Areas"]: want.append((g, "BlueprintArea", "Area@" + s["Id"]))
            if s["NativeReturnCue"]: want.append((s["NativeReturnCue"], "BlueprintCue", "NativeReturnCue@" + s["Id"]))
        for k in (story.get("ParentEpilogueEdits") or {}): want.append((k, "BlueprintCue", "ParentEpilogueEdit"))
        for r in story.get("ParentEpilogueLossRules") or []:
            for g in r.get("SuppressPages", []): want.append((g, "BlueprintBookPage", "LossRule.SuppressPages"))
            for g in r.get("SuppressCues", []): want.append((g, "BlueprintCue", "LossRule.SuppressCues"))
        want += [("ed4baeaf69394754902344f0598d7e5a", "BlueprintCueSequence", "Main.epilogue"),
                 ("ced82f299d246f448b48afa0b630dd70", "BlueprintCueSequence", "Main.aeon")]
        bad, seen, parent_untyped = [], set(), []
        for g, t, where in want:
            if (g, t) in seen: continue
            seen.add((g, t))
            hit = idx.get(g) or par.get(g)
            if not hit: bad.append(dict(guid=g, expected=t, where=where, actual=None))
            elif hit[0] == "?parent-literal":
                parent_untyped.append(dict(guid=g, expected=t, where=where, source=hit[1]))
            elif hit[0] != t and not (t == "BlueprintArea" and hit[0].startswith("BlueprintArea")) and not (t == "BlueprintCue" and hit[0] == "BlueprintCue"):
                bad.append(dict(guid=g, expected=t, where=where, actual=hit[0], path=hit[1]))
        # hard-coded GUIDs in src/*.cs
        srcg = collections.defaultdict(set)
        for p in (MOD / "src").glob("*.cs"):
            for mm in re.finditer(r'"([0-9a-f]{32})"', p.read_text(encoding="utf-8")): srcg[mm.group(1)].add(p.name)
        src_missing = {g: sorted(f) for g, f in srcg.items() if g not in idx and g not in par}
        # RRT GUIDs colliding with native or parent
        rrt_coll = [(n, rrt_guid(n)) for n, _ in names if rrt_guid(n) in idx or rrt_guid(n) in par]
        # answer list tails (Count-1 insertion assumes trailing exit)
        tails = {}
        lists = sorted(set(g for g, t, _ in want if t == "BlueprintAnswersList"))
        with zipfile.ZipFile(game / "blueprints.zip") as z:
            for g in lists:
                if g not in idx: tails[g] = "parent/unknown"; continue
                d = json.loads(z.read(idx[g][1]))["Data"]
                ans = d.get("Answers") or []
                if not ans: tails[g] = "EMPTY list"; continue
                last = ans[-1].replace("!bp_", "")
                if last not in idx: tails[g] = "last=%s (parent/unknown)" % last; continue
                ad = json.loads(z.read(idx[last][1]))["Data"]
                cues = ((ad.get("NextCue") or {}).get("Cues") or [])
                key = ((ad.get("Text") or {}).get("m_Key") or (ad.get("Text") or {}).get("Key") or "")
                txt = loc.get(key, "")
                if isinstance(txt, dict): txt = txt.get("Text", "")
                txt = re.sub(r"\{[^}]*\}", "", str(txt))[:60]
                exitish = (not cues) or bool(re.search(r"leave|farewell|goodbye|go now|that.s all|nothing|later|bye|excuse me|must go|have to go|must be going|until next time|another time|see you", txt, re.I))
                tails[g] = ("exit-ok" if exitish else "LAST ANSWER IS NOT AN EXIT") + " [%s] %r cues=%d" % (Path(idx[last][1]).stem, txt, len(cues))
        R["bindings"] = dict(checked=len(seen), failures=bad, src_hardcoded_missing=src_missing, rrt_native_collisions=rrt_coll, list_tails=tails,
                             index_size=len(idx), parent_guids=len(par))
        R["_typeids"] = typeids
        P("\n## F. Native GUID bindings vs blueprints.zip (%d blueprints indexed in %.1fs; %d parent-mod GUIDs)" % (len(idx), time.time() - tz, len(par)))
        P("  Checked %d (guid,type) pairs: %d failures; %d resolved only as a GUID literal in parent source (type unverified): %s"
          % (len(seen), len(bad), len(parent_untyped), [x["where"] for x in parent_untyped][:6]))
        for b in bad[:30]: P("     -", b)
        P("  Hard-coded GUIDs in src/*.cs not found in blueprints.zip or parent: %d %s" % (len(src_missing), list(src_missing.items())[:10]))
        P("  RRT GuidFor() ids colliding with native/parent blueprints: %d" % len(rrt_coll))
        nonexit = {g: v for g, v in tails.items() if not v.startswith("exit-ok")}
        P("  Target answer lists: %d; lists whose LAST answer is not a plain exit (Count-1 insertion assumption): %d" % (len(tails), len(nonexit)))
        for g, v in list(nonexit.items())[:15]: P("     -", g, v)
    else:
        R["_typeids"] = set()

    # ---- I. TypeId lint
    tids = []
    for p in (MOD / "src").glob("*.cs"):
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            for mm in re.finditer(r'\[TypeId\("([^"]*)"\)\]', line): tids.append((mm.group(1), "%s:%d" % (p.name, i)))
    parent_tids = set()
    if (SCRATCH / "ranromance").is_dir():
        for p in (SCRATCH / "ranromance").rglob("*.cs"):
            parent_tids |= set(x.lower() for x in re.findall(r'\[TypeId\("([^"]*)"\)\]', p.read_text(encoding="utf-8", errors="replace")))
    tbad = []
    c = collections.Counter(t.lower() for t, _ in tids)
    for t, loc in tids:
        if not re.fullmatch(r"[0-9a-fA-F]{32}", t) and not re.fullmatch(r"[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}", t):
            tbad.append("%s %s: not a 32-hex GUID (len %d) -> TypeIdAttribute ctor Guid.Parse throws FormatException; Harmony PatchAll reflects it" % (loc, t, len(t)))
        if c[t.lower()] > 1: tbad.append("%s %s: duplicate TypeId" % (loc, t))
        if t.lower().replace("-", "") in R["_typeids"]: tbad.append("%s %s: collides with a game TypeId" % (loc, t))
        if t.lower() in parent_tids: tbad.append("%s %s: collides with parent-mod TypeId" % (loc, t))
    R["typeid"] = dict(found=tids, problems=tbad)
    P("\n## I. [TypeId] lint over src/*.cs: %d attributes, %d problems" % (len(tids), len(tbad)))
    for x in tbad: P("  -", x)
    R.pop("_typeids", None)

    # ---- drafts
    if drafts:
        R["drafts"] = check_drafts(story, P, game)

    P("\nruntime %.1fs" % (time.time() - t0))
    text = "\n".join(lines)
    if not quiet: print(text)
    if out_json:
        Path(out_json).write_text(json.dumps(R, indent=1, default=lambda o: sorted(o) if isinstance(o, set) else str(o)), encoding="utf-8")
    return R, text


def s_rel(model, where):
    return model.by_id[where.split("/")[0]]["Relationship"]


def entry_targets_safe(s):
    try: return entry_targets(s)
    except ValueError: return []


def registered_modules(mod):
    t = (mod / "expansion.py").read_text(encoding="utf-8") + (mod / "story.py").read_text(encoding="utf-8")
    regs = set()
    for mm in re.finditer(r"from storylines import ([^\n]+)", t):
        regs |= {x.strip() for x in mm.group(1).split(",")}
    for mm in re.finditer(r"import storylines\.(\w+)", t): regs.add(mm.group(1))
    return regs


def previous_exports():
    out = []
    inst = GAME / "Mods/RanRomanceTirabade/Story.json"
    if inst.is_file(): out.append(("installed-game-copy", inst))
    # Committed snapshots of every RELEASED Story.json; names they registered must never disappear (hard failure).
    for rel in sorted((MOD / "tools/released-stories").glob("*.json")):
        out.append(("released-" + rel.stem, rel))
    dists = sorted((MOD / "dist").glob("expansion-*/Mods/RanRomanceTirabade/Story.json"))
    if dists: out.append(("latest-dist-" + dists[-1].parts[-4][-17:], dists[-1]))
    return out


def check_drafts(story, P, game):
    """Import each unregistered storyline from a scratch COPY (never in-place), validate structurally and
    run producer/reachability checks as if registered."""
    work = SCRATCH / "draftcopy"
    if work.exists(): shutil.rmtree(work)
    work.mkdir(parents=True)
    for name in ("story.py", "story_format.py", "expansion.py"):
        shutil.copy2(MOD / name, work / name)
    shutil.copytree(MOD / "storylines", work / "storylines", ignore=shutil.ignore_patterns("__pycache__"))
    if (MOD / "reference/expansion").is_dir():
        shutil.copytree(MOD / "reference/expansion", work / "reference/expansion")
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(work))
    unreg = sorted(p.stem for p in (MOD / "storylines").glob("*.py") if p.stem not in registered_modules(MOD))
    res = {}
    P("\n## DRAFTS (unregistered modules, imported from a scratch copy)")
    base_ids = {s["Id"] for s in story["Scenes"]}
    for name in unreg:
        r = dict()
        try:
            mod = importlib.import_module("storylines." + name)
            scenes = getattr(mod, "SCENES", None)
            if scenes is None:
                r["status"] = "no SCENES attribute (exports: %s)" % [k for k in dir(mod) if k.isupper()]
                res[name] = r; P("  %-40s %s" % (name, r["status"])); continue
            merged = json.loads(json.dumps(story))
            for k in ("ETUDES", "COMPLETED_QUESTS", "SEEN_CUES"):
                sec = {"ETUDES": "Etudes", "COMPLETED_QUESTS": "CompletedQuests", "SEEN_CUES": "SeenCues"}[k]
                if hasattr(mod, k): merged.setdefault(sec, {}).update(getattr(mod, k))
            relname = None
            if hasattr(mod, "RELATIONSHIP"):
                rid = scenes[0].get("Relationship") if scenes else None
                if rid: merged["Relationships"].setdefault(rid, getattr(mod, "RELATIONSHIP")); relname = rid
            clash = [s["Id"] for s in scenes if s["Id"] in base_ids]
            merged["Scenes"] = [s for s in merged["Scenes"] if s["Id"] not in {x["Id"] for x in scenes}] + json.loads(json.dumps(scenes))
            if hasattr(mod, "integrate"):
                try: mod.integrate(merged); r["integrate"] = "ok"
                except Exception as e: r["integrate"] = "FAILED: %r" % e
            m = Model(merged)
            errs = [e for e in validate(m) if any(s["Id"] in e for s in scenes) or "relationship" in e.lower()]
            ids = {s["Id"] for s in scenes}
            refs = m.all_referenced()
            nop = sorted(f for f, w in refs.items() if f not in m.producers and f not in m.native and f not in m.derived
                         and any(x[0].split("/")[0] in ids for x in w) and any(k in ("Requires", "choice.Requires", "RequiresAnyGroups") for _, k in w))
            reached = set()
            tri = None
            for mth in MYTHIC:
                rr = Reach(m, mythic_world(mth, m))
                reached |= set(rr.reached) & ids
                if mth == "trickster": tri = set(rr.reached) & ids
            r.update(scenes=len(scenes), validate_errors=errs, required_without_producer=nop, reachable_any_path=len(reached),
                     reachable_trickster=len(tri or ()), id_clash_with_registered=clash, relationship=sorted({s.get("Relationship", "tirabade") for s in scenes}))
            r["status"] = "ok" if not errs else "validate-errors"
            P("  %-40s scenes %3d  validate-errs %2d  reachable(any) %3d  reachable(trickster) %3d  dead-required-flags %s%s"
              % (name, len(scenes), len(errs), len(reached), len(tri or ()), nop[:5], ("  ID-CLASH %s" % clash[:3]) if clash else ""))
            for e in errs[:4]: P("       !", e)
        except Exception as e:
            r["status"] = "IMPORT/BUILD FAILED: %r" % e
            P("  %-40s %s" % (name, r["status"]))
        res[name] = r
    sys.path.remove(str(work))
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--story", default=str(MOD / "development/Story.json"))
    ap.add_argument("--game", default=str(GAME))
    ap.add_argument("--json", default=str(HERE / "rrt_verify_report.json"))
    ap.add_argument("--text", default=str(HERE / "rrt_verify_report.txt"))
    ap.add_argument("--no-zip", action="store_true")
    ap.add_argument("--drafts", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--strict", action="store_true", help="exit 1 on hard failures (for build gates)")
    a = ap.parse_args()
    R, text = run(a.story, Path(a.game), use_zip=not a.no_zip, drafts=a.drafts, out_json=a.json, quiet=a.quiet)
    Path(a.text).write_text(text, encoding="utf-8")
    hard = len(R["validate_errors"]) + len(R["no_producer_required"]) + len(R.get("typeid", {}).get("problems", [])) \
        + len(R.get("bindings", {}).get("failures", [])) + len(R["runtime"]["duplicate_names"]) + len(R["runtime"]["retry_dups"])         + len(R.get("released_names_removed", []))
    for x in R.get("released_names_removed", [])[:20]: print("SAVE BREAK (name from a released build no longer registered):", x)
    print("\nHARD FAILURES: %d  (report: %s)" % (hard, a.text))
    if a.strict and hard: sys.exit(1)


if __name__ == "__main__":
    main()

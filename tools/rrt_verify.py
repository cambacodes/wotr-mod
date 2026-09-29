#!/usr/bin/env python3
"""rrt_verify.py - fast static integrity verifier for RanRomanceTirabade (RRT).

Pure stdlib. Reads the mod READ-ONLY. Mirrors src/Story.cs Rules.Available / Rules.Validate and
src/Main.cs Build()/State() semantics closely enough to find unreachable content, cross-route
lockouts, chapter traps, lint problems and bad native GUID bindings, without Unity.

Usage:
  python rrt_verify.py [--story PATH] [--game DIR] [--json OUT] [--no-zip] [--quiet]
  python rrt_verify.py --drafts          # also build + check unregistered storyline drafts (from a scratch COPY)
  python rrt_verify.py --matrix ../handoffs/trickster-matrix.json   # TT-20 roster matrix: entry / commit / coexist per character

Sections: A producers | B reachability per mythic world | C chapter/delay traps | D cross-route forbid matrix
          E lints | F native GUID bindings | G runtime-risk metrics | H Trickster roster matrix | I TypeId lint
          E9 rest budget: Trickster full-roster simulation with the E8b mailbag (default) or E8 post bags (report only;
             --delivery, --rest-cadence, --chapter-days, --bag-size, --queue-cap, --sim-natives); also run per matrix supply
             profile in --matrix mode
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
CONTACT_EVIDENCE = {"konomi.retained_hostile", "konomi.missed_contact_available", "konomi.missed_contact_invalidated", "konomi.retained_dead",
                    "konomi.return_contact_available", "konomi.return_correspondence_available",
                    "irabeth.return_correspondence_available", "irabeth.return_meeting_arrived",
                    "nurah.correspondence_available", "nurah.meeting_arrived"}
CHECK_SKILLS = {"SkillAthletics", "SkillMobility", "SkillStealth", "SkillThievery", "SkillKnowledgeArcana",
                "SkillKnowledgeWorld", "SkillLoreNature", "SkillLoreReligion", "SkillPerception",
                "SkillUseMagicDevice", "CheckDiplomacy", "CheckBluff", "CheckIntimidate"}
MYTHIC_PATHS = ("Aeon", "Angel", "Azata", "Demon", "Devil", "Dragon", "Legend", "Lich", "Locust", "Trickster")
MYTHIC_ENUM = {"PlayerIs" + p for p in MYTHIC_PATHS} | {p + "Unlocked" for p in MYTHIC_PATHS}
ALIGNMENT_DIRECTIONS = {"LawfulGood", "NeutralGood", "ChaoticGood", "LawfulNeutral", "TrueNeutral", "ChaoticNeutral",
                        "LawfulEvil", "NeutralEvil", "ChaoticEvil", "Good", "Evil", "Lawful", "Chaotic"}
CRUSADE_RESOURCES = {"Finances", "Materials", "Favors"}
CUE_BASE_TYPES = {"BlueprintCue", "BlueprintBookPage", "BlueprintCueSequence", "BlueprintCheck"}
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
             ForbidOverrides={}, Nodes=[], Entry="", Title="", Reaction=False, TricksterDevice=False, TricksterState=None,
             EpilogueAfter=None, EntryMythic=None, EntryAlignment=None, EpilogueSequence=None, ReturnToList=False, ReturnText=None,
             ContinueBefore=None)
    d.update({k: v for k, v in s.items() if v is not None or k in ("NativeReturnCue",)})
    for n in d["Nodes"]:
        n.setdefault("Speaker", "Narrator"); n.setdefault("Portrait", ""); n.setdefault("Text", ""); n.setdefault("Paragraphs", [])
        n.setdefault("SpeakerUnit", None)
        n.setdefault("Choices", [])
        for c in n["Choices"]:
            for k, v in dict(Text="Continue", Next=None, Abort=False, Revive=None, Check=None, Set=[], Requires=[],
                             Forbids=[], Mythic=None, NativeNext=None, Alignment=None, Crusade=None, RemoveItem=None).items():
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


def presence_relationship(key):
    """E12: "<rel>.presence" or "<rel>.presence.<name>" -> rel."""
    mm = re.match(r"^(.+?)\.presence(?:\.[a-z0-9_]+)?$", key or "")
    return mm.group(1) if mm else None


def is_presence_hub(s):
    """E12c: a physical scene offered in a presence's click-to-talk hub."""
    h = s["InteractionHub"]
    return (h is not None and presence_relationship(h) is not None and h != "nurah.arrival" and not is_remote(s) and not is_epilogue(s)
            and not s["AnswerLists"] and s["NativeReturnCue"] is None and not s.get("ReturnToList") and not s.get("ContinueBefore"))


def entry_targets(s):
    if is_remote(s) or is_epilogue(s) or s.get("ContinueBefore"): return []
    if s["InteractionHub"] is not None:
        if is_nurah_hub(s) or is_presence_hub(s): return []
        raise ValueError("Unrecognized authored interaction hub: " + s["Id"])
    if s["AnswerLists"]: return list(s["AnswerLists"])
    if s["Relationship"] == "tirabade":
        if s["Owner"] == "Anevia": return [ANEVIA_LIST]
        if s["Owner"] == "Irabeth": return [IRABETH_LIST]
        if s["Owner"] == "Together": return [ANEVIA_LIST, IRABETH_LIST]
    raise ValueError("No dialogue attachment points for %s (%s)" % (s["Id"], s["Owner"]))


def device_detects(rel, s):
    """ER-2: unavailable flags a TricksterDevice scene ignores (mirrors Rules.DeviceDetects)."""
    acc = rel.get("TricksterAccess") or {}
    if s.get("TricksterState") is not None:
        entries = [acc[s["TricksterState"]]] if s["TricksterState"] in acc else []
    else:
        entries = [e for e in acc.values() if e.get("Device") == s["Id"]] or list(acc.values())
    keys = {k for e in entries for k in e.get("Detect", []) if not k.startswith("!")}
    return keys & set(rel.get("UnavailableFlags", []))


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
        for sec in ("Etudes", "CompletedQuests", "SeenCues", "SelectedAnswers", "StartedDialogs", "CompletedEtudes",
                    "UnlockableFlags", "QuestObjectives", "InventoryItems", "StartedQuests", "MainCharacterFacts"):
            for k in story.get(sec, {}): nk.setdefault(k, sec)
        self.native = nk
        self.revivals = story.get("Revivals", {})
        self.derived = {k + ".failed" for k, p in (story.get("Presences") or {}).items() if p.get("At")} | \
                       {"loss", "ascended", "inhuman", "chapter_one", "chapter_later"} | CONTACT_EVIDENCE | \
                       {"revive.%s.available" % k for k in self.revivals}
        self.builtin_derived = set(self.derived)
        # E1 latches: authored flags the runtime records from native sources (never set by a choice).
        self.latches = {k: list(v) for k, v in (story.get("Latches") or {}).items()}
        self.derived |= set(self.latches)
        # E4 data-driven composites (OR of AND-groups).
        self.composites = {k: [list(g) for g in v] for k, v in (story.get("Derived") or {}).items()}
        self.derived |= set(self.composites)
        # E14g count composites.
        self.counts = {k: (list(v.get("Of") or []), int(v.get("Min", 1))) for k, v in (story.get("Counts") or {}).items()}
        self.derived |= set(self.counts)
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
        allf = set(self.authored) | set(self.native) | set(self.latches)
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
        self.persistent = frozenset(f for f in allf if (f in self.authored or f in self.latches or self.is_persistent_native(f)) and f in forb) |             ({"loss", "ascended"} & forb)
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
        if sec in ("UnlockableFlags", "InventoryItems", "QuestObjectives"): return False   # values can change back
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
            for f in (r.get("UnavailableOverrides") or {}).values(): ref[f].append(("rel:" + rk, "UnavailableOverride"))
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
    if m != "trickster" and "trickster.was" in model.native: fl.add("trickster.was")  # only a former Trickster
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
        if f in m.latches: return any(self.native_possible(x, ch) for x in m.latches[f])
        if f in m.composites: return any(all(self.possible(x, ch) for x in g) for g in m.composites[f])
        if f in m.counts: return sum(1 for x in m.counts[f][0] if self.possible(x, ch)) >= m.counts[f][1]
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
        if f in self.m.latches: return any(self.forced(x, ch) for x in self.m.latches[f])
        if f in self.m.composites: return any(all(self.forced(x, ch) for x in g) for g in self.m.composites[f])
        if f in self.m.counts: return sum(1 for x in self.m.counts[f][0] if self.forced(x, ch)) >= self.m.counts[f][1]
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
            ov = (rel.get("UnavailableOverrides") or {}).get(f)
            if ov and self.possible(ov, ch): continue   # E2: an authored return can lift this block
            if s["TricksterDevice"] and f in device_detects(rel, s): continue   # ER-2: the device serving this state
            # A Revivals DeathFlag is an observation of the corpse, not a latch: the confirmed revive clears it at runtime,
            # so a world forced into the death reaches the relationship again once that state's return is possible.
            if any(r.get("DeathFlag") == f and r.get("Relationship") == s["Relationship"] for r in m.revivals.values())                     and any(f in (e.get("Detect") or []) and e.get("Returned") and self.possible(e["Returned"], ch)
                            for e in (rel.get("TricksterAccess") or {}).values()): continue
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
    names += [("flag.served." + rid, "BlueprintUnlockableFlag") for rid in model.rels if "served." + rid not in keys]
    for k in model.latches:
        names += [("flag." + x, "BlueprintUnlockableFlag") for x in (k, "hour." + k) if x not in keys]
    names += [("etude.konomi.personal_return", "BlueprintEtude"), ("etude.irabeth.personal_return", "BlueprintEtude"),
              ("etude.nurah.private_meeting", "BlueprintEtude")]
    for rid in model.rels:
        suf = "" if rid == "tirabade" else "." + rid
        names += [("quest" + suf, "BlueprintQuest"), ("objective" + suf, "BlueprintQuestObjective")]
    for s in scenes:
        if s["ContinueBefore"]:   # E14e: one registered line (Main.BuildContinueBefore)
            names.append(("cue.%s.continue" % s["Id"], "BlueprintCue"))
            continue
        if s["ReturnToList"]:   # E14b: one inline graph per list (Main.BuildReturnToList)
            for lst in s["AnswerLists"]:
                pre = s["Id"] + "." + lst
                names.append(("cue." + pre + ".return", "BlueprintCue"))
                names += [("cue.%s.%s" % (pre, n["Id"]), "BlueprintCue") for n in s["Nodes"]]
                names += [("answer.%s.%s.%d" % (pre, n["Id"], i), "BlueprintAnswer") for n in s["Nodes"] for i in range(len(n["Choices"]))]
                names.append(("entry." + pre, "BlueprintAnswer"))
            continue
        for n in s["Nodes"]:
            i = s["Id"] + "." + n["Id"]
            names.append(("cue." + i, "BlueprintCue"))
            if s["NativeReturnCue"] is None:
                names.append(("page." + i, "BlueprintBookPage"))
                names += [("cue.%s.p%d" % (i, k), "BlueprintCue") for k in range(len(n.get("Paragraphs") or []))]
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
    for key, p in (model.story.get("Presences") or {}).items():   # E12c presence hubs (Main.BuildPresenceHub)
        if p.get("Dialog") != "hub": continue
        names += [("page.%s.hub" % key, "BlueprintBookPage"), ("cue.%s.hub" % key, "BlueprintCue")]
        names += [("answer.%s.hub.%s" % (key, s["Id"]), "BlueprintAnswer") for s in scenes if s["InteractionHub"] == key]
        names += [("answer.%s.hub.leave" % key, "BlueprintAnswer"), ("dialog.%s.hub" % key, "BlueprintDialog")]
    for cue in (model.story.get("NativeEpilogueEdits") or {}):   # E14d replacement cues
        names.append(("native-edit." + cue, "BlueprintCue"))
    if any(is_nurah_hub(s) for s in scenes):
        names += [("page.nurah.arrival_hub", "BlueprintBookPage"), ("cue.nurah.arrival_hub", "BlueprintCue")]
        names += [("answer.nurah.arrival_hub." + s["Id"], "BlueprintAnswer") for s in scenes if is_nurah_hub(s)]
        names += [("answer.nurah.arrival_hub.leave", "BlueprintAnswer"), ("dialog.nurah.arrival_hub", "BlueprintDialog")]
    for s in scenes:
        if is_epilogue(s) or is_remote(s) or s["InteractionHub"] is not None or s["ReturnToList"] or s["ContinueBefore"]: continue
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
    for k, p in (st.get("Presences") or {}).items():
        rel = presence_relationship(k)
        if (rel not in rels or not hexre.match(p.get("Unit") or "") or not hexre.match(p.get("Area") or "")
                or p.get("Mode", "reuse-native") not in ("reuse-native", "spawn-copy")
                or (p.get("Mode") == "spawn-copy" and (not (p.get("Position") or p.get("At")) or not p.get("Requires")))):
            errs.append("Invalid presence: " + k)
    for k, r in rels.items():
        for a, b in (r.get("UnavailableOverrides") or {}).items():
            if (a not in r.get("UnavailableFlags", []) or b == a or (b not in model.authored and b not in model.latches and b not in model.composites)
                    or b in model.native or b in model.builtin_derived or b.startswith(("rrt.degraded.", "served.", "hour.", "revive."))
                    or b in r.get("UnavailableFlags", []) or any(x["ClosedFlag"] == b for x in rels.values())):
                errs.append("Invalid unavailable override %s/%s" % (k, a))
    known = model.authored | set(model.native) | model.builtin_derived | set(model.latches) | set(model.composites)
    for k, groups in model.composites.items():
        if (not k or k in model.authored or k in model.native or k in model.builtin_derived or k in model.latches
                or k.startswith(("rrt.degraded.", "served.", "hour.", "revive.")) or not groups or any(not g for g in groups)
                or any(x not in known for g in groups for x in g)):
            errs.append("Invalid derived key: " + k)
    def cyclic(k, path):
        if k in path: return True
        return any(cyclic(x, path | {k}) for g in model.composites.get(k, []) for x in g if x in model.composites)
    for k in model.composites:
        if cyclic(k, frozenset()): errs.append("Derived cycle through: " + k)
    for k, src in model.latches.items():
        if (not k or k in model.authored or k in model.native or k in model.builtin_derived or not src or len(set(src)) != len(src)
                or k.startswith(("rrt.degraded.", "served.", "hour.", "revive."))
                or any(x not in model.native and x not in model.builtin_derived for x in src)):
            errs.append("Invalid latch: " + k)
    hexre = re.compile(r"^[0-9a-fA-F]{32}$")
    for s in model.scenes:
        sid = s["Id"]
        try:
            tg = entry_targets(s)
        except ValueError as e:
            errs.append(str(e)); tg = []
        if s["InteractionHub"] is not None and not is_nurah_hub(s) and not (
                is_presence_hub(s) and ((st.get("Presences") or {}).get(s["InteractionHub"]) or {}).get("Dialog") == "hub"
                and presence_relationship(s["InteractionHub"]) == s["Relationship"]):
            errs.append("Invalid interaction hub: " + sid)
        if (s["Relationship"] == "nurah" and not is_remote(s) and not is_epilogue(s) and not is_nurah_hub(s) and not is_presence_hub(s)
                and not ((s["TricksterDevice"] or s.get("Reaction")) and s["InteractionHub"] is None and s["AnswerLists"])):
            errs.append("Physical Nurah scene without hub (or a TricksterDevice on explicit AnswerLists): " + sid)
        if (s["EntryMythic"] is not None or s["EntryAlignment"] is not None) and (
                is_remote(s) or s["InteractionHub"] is not None or is_epilogue(s)
                or (s["EntryMythic"] is not None and s["EntryMythic"] not in MYTHIC_ENUM)
                or (s["EntryAlignment"] is not None and (s["EntryAlignment"].get("Direction") not in ALIGNMENT_DIRECTIONS
                                                      or not 0 < s["EntryAlignment"].get("Value", 0) <= 100))):
            errs.append("Invalid entry mythic/alignment: " + sid)
        if s["ManualOnly"] and not is_remote(s): errs.append("ManualOnly non-remote: " + sid)
        if s["TricksterDevice"] or s["TricksterState"] is not None:
            rel = rels.get(s["Relationship"], {})
            acc = rel.get("TricksterAccess") or {}
            rec = {e.get("Returned") for e in acc.values()} | set((rel.get("UnavailableOverrides") or {}).values())
            sets = [f for n in s["Nodes"] for c in n["Choices"] for f in c["Set"]]
            if (not s["TricksterDevice"] or not acc or s["Reaction"] or is_epilogue(s)
                    or (s["TricksterState"] is not None and s["TricksterState"] not in acc)
                    or not ({"trickster", "trickster.ever"} & set(s["Requires"]))
                    or not any(f in rec or ".trickster.primed" in f or ".trickster.returned" in f or ".trickster.cost." in f for f in sets)):
                errs.append("Invalid Trickster device: " + sid)
        if s["Reaction"]:
            own = rels.get(s["Relationship"], {})
            others = {f for k, r in rels.items() if k != s["Relationship"] for f in (r["StartedFlag"], r["ClosedFlag"], r["CommittedFlag"])}
            chs = [c for n in s["Nodes"] for c in n["Choices"]]
            if (len(s["Nodes"]) != 1 or is_epilogue(s) or (not is_remote(s) and not s["AnswerLists"])
                    or any(c["Next"] or c["Check"] or c["Revive"] or c["NativeNext"] for c in chs)
                    or any(f == own.get("ClosedFlag") or f in others for c in chs for f in c["Set"])
                    or any(f in others for f in list(s["Forbids"]) + [f for c in chs for f in c["Forbids"]])):
                errs.append("Invalid reaction: " + sid)
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
            closed = {r["ClosedFlag"] for r in rels.values()}
            if (a not in s["Forbids"] or (a in model.authored) == (a in model.native) or a in model.builtin_derived
                    or (b not in model.authored and b not in model.latches and b not in model.composites) or b in model.native or b in model.builtin_derived
                    or a == b or a in closed or b in closed):
                errs.append("Invalid forbid override %s/%s" % (sid, a))
        nodes = {}
        for n in s["Nodes"]:
            if n["Id"] in nodes or not (n["Text"].strip() or n["Paragraphs"]) or not n["Choices"]: errs.append("Invalid node: %s/%s" % (sid, n["Id"]))
            if n["Paragraphs"] and not is_epilogue(s): errs.append("Paragraphs outside an epilogue page: %s/%s" % (sid, n["Id"]))
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
                if c["Mythic"] is not None and (is_epilogue(s) or c["Mythic"] not in MYTHIC_ENUM):
                    errs.append("Invalid mythic requirement: %s/%s %s" % (sid, n["Id"], c["Mythic"]))
                al = c["Alignment"]
                if al is not None and (is_epilogue(s) or al.get("Direction") not in ALIGNMENT_DIRECTIONS or not 0 < al.get("Value", 0) <= 100):
                    errs.append("Invalid alignment shift: %s/%s" % (sid, n["Id"]))
                cr = c["Crusade"]
                if cr is not None and (is_epilogue(s) or s["MinChapter"] < 3 or cr.get("Resource") not in CRUSADE_RESOURCES
                                       or not cr.get("Amount") or abs(cr.get("Amount", 0)) > 100000):
                    errs.append("Invalid crusade cost: %s/%s" % (sid, n["Id"]))
                ri = c["RemoveItem"]
                inv = st.get("InventoryItems") or {}
                if ri is not None and (is_epilogue(s) or ri not in (st.get("RemovableItems") or [])
                                       or not any(inv.get(k) == ri for k in list(c["Requires"]) + list(s["Requires"]))):
                    errs.append("Invalid item removal: %s/%s" % (sid, n["Id"]))
                if c["NativeNext"] is not None and (not hexre.match(c["NativeNext"]) or s["NativeReturnCue"] is None or c["Next"] is not None
                                                    or c["Check"] or c["Abort"] or c["Revive"] is not None):
                    errs.append("Invalid native continuation (terminal choice of an inline scene only): %s/%s" % (sid, n["Id"]))
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
    fatal = {f: w for f, w in no_producer.items() if any(k in ("Requires", "choice.Requires", "RequiresAnyGroups", "ForbidOverride", "UnavailableOverride") for _, k in w)}
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
    # E9 rest budget (report only; never a hard failure)
    rb = simulate_rest_budget(model, **(REST_OPTIONS or {}))
    print_rest_budget(rb, P)
    R["rest_budget"] = rb
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
        for k, g in story.get("UnlockableFlags", {}).items(): want.append((g, "BlueprintUnlockableFlag", "UnlockableFlags." + k))
        for k, v in story.get("QuestObjectives", {}).items(): want.append((v[0], "BlueprintQuestObjective", "QuestObjectives." + k))
        for k, g in story.get("InventoryItems", {}).items(): want.append((g, "BlueprintItem*", "InventoryItems." + k))
        for k, g in story.get("StartedQuests", {}).items(): want.append((g, "BlueprintQuest", "StartedQuests." + k))
        for k, g in story.get("MainCharacterFacts", {}).items(): want.append((g, "BlueprintFeature", "MainCharacterFacts." + k))
        for k, v in model.revivals.items(): want.append((v["Unit"], "BlueprintUnit", "Revivals." + k))
        for s in model.scenes:
            for g in ([s["ContactUnit"]] if s["ContactUnit"] else []) + list(s["AdditionalContactUnits"]): want.append((g, "BlueprintUnit", "ContactUnit@" + s["Id"]))
            try:
                for g in entry_targets(s): want.append((g, "BlueprintAnswersList", "AnswerList@" + s["Id"]))
            except ValueError: pass
            for g in s["Areas"]: want.append((g, "BlueprintArea", "Area@" + s["Id"]))
            if s["NativeReturnCue"]: want.append((s["NativeReturnCue"], "BlueprintCue", "NativeReturnCue@" + s["Id"]))
            if s["EpilogueAfter"] and not s["EpilogueAfter"].startswith("scene:"):
                want.append((s["EpilogueAfter"], "BlueprintCueBase", "EpilogueAfter@" + s["Id"]))   # a cue or a book page
            for n in s["Nodes"]:
                if n.get("SpeakerUnit"): want.append((n["SpeakerUnit"], "BlueprintUnit", "SpeakerUnit@%s/%s" % (s["Id"], n["Id"])))
            if s["ContinueBefore"]:
                want.append((s["ContinueBefore"].get("Cue"), "BlueprintCue", "ContinueBefore@" + s["Id"]))
                want += [(g, "BlueprintCue", "ContinueBefore.Parents@" + s["Id"]) for g in s["ContinueBefore"].get("Parents") or []]
            if s["EpilogueSequence"]: want.append(("a3096e5b145badb448827a7336d86d02", "BlueprintCueSequence", "EpilogueSequence@" + s["Id"]))
            for n in s["Nodes"]:
                for c in n["Choices"]:
                    if c["NativeNext"]: want.append((c["NativeNext"], "BlueprintCue", "NativeNext@%s/%s" % (s["Id"], n["Id"])))
        for k in (story.get("ParentEpilogueEdits") or {}): want.append((k, "BlueprintCue", "ParentEpilogueEdit"))
        for g in story.get("RemovableItems") or []: want.append((g, "BlueprintItem*", "RemovableItems"))
        for g, e in (story.get("NativeEpilogueEdits") or {}).items():
            want += [(g, "BlueprintCue", "NativeEpilogueEdits"), (e.get("Page"), "BlueprintBookPage", "NativeEpilogueEdits." + g),
                     (e.get("Sequence"), "BlueprintCueSequence", "NativeEpilogueEdits." + g)]
        for k, p in (story.get("Presences") or {}).items():
            want.append((p.get("Unit"), "BlueprintUnit", "Presences." + k))
            want.append((p.get("Area"), "BlueprintArea", "Presences." + k))
            if (p.get("At") or {}).get("NearUnit"): want.append((p["At"]["NearUnit"], "BlueprintUnit", "Presences.At." + k))
            for g in p.get("AnswerLists") or []: want.append((g, "BlueprintAnswersList", "Presences." + k))
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
            elif hit[0] != t and not (t == "BlueprintArea" and hit[0].startswith("BlueprintArea")) and not (t.endswith("*") and hit[0].startswith(t[:-1]))                     and not (t == "BlueprintCueBase" and hit[0] in CUE_BASE_TYPES):
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
        # E5: a native continuation must belong to the dialog that owns the scene's answer list (same ParentAsset).
        with zipfile.ZipFile(game / "blueprints.zip") as z:
            def parent(g):
                """The owning BlueprintDialog: ParentAsset names the immediate owner (a list's cue, a cue's dialog...)."""
                seen = set()
                while g in idx and g not in seen and idx[g][0] != "BlueprintDialog":
                    seen.add(g)
                    g = json.loads(z.read(idx[g][1]))["Data"].get("ParentAsset")
                return g if g in idx and idx[g][0] == "BlueprintDialog" else None
            for s in model.scenes:
                for n in s["Nodes"]:
                    for c in n["Choices"]:
                        g = c["NativeNext"]
                        if not g or not s["AnswerLists"] or g not in idx: continue
                        if parent(g) is None or parent(g) != parent(s["AnswerLists"][0]):
                            bad.append(dict(guid=g, expected="BlueprintCue of the answer list's dialog", where="NativeNext@%s/%s" % (s["Id"], n["Id"]),
                                            actual="cue dialog %s vs answer-list dialog %s" % (parent(g), parent(s["AnswerLists"][0]))))
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


# ----------------------------------------------------------------------------- E9 rest-budget simulator
# Chapter lengths are ESTIMATES to calibrate against real Trickster playthroughs (in-game days).
SIM_CHAPTER_DAYS = {1: 2, 2: 6, 3: 30, 4: 12, 5: 40, 6: 1}
SIM_REST_CADENCE = 16   # in-game hours of travel between successful rests (default; per chapter via --rest-cadence)
REST_OPTIONS = {}       # set from the command line (--delivery, --rest-cadence, --chapter-days, --bag-size, --queue-cap)


class SimState:
    def __init__(self, chapter, hour):
        self.chapter, self.hour, self.flags, self.times = chapter, hour, set(), {}

    def has(self, f): return f in self.flags


def sim_complete(model, st):
    """Mirror of Rules.Complete: latches, then Story.Derived composites."""
    for k, src in model.latches.items():
        if any(x in st.flags for x in src): st.flags.add(k)
    changed = True
    while changed:
        changed = False
        for k, groups in model.composites.items():
            if k not in st.flags and any(all(x in st.flags for x in g) for g in groups):
                st.flags.add(k); changed = True
    for k, (of, least) in model.counts.items():
        if k not in st.flags and sum(1 for x in of if x in st.flags) >= least: st.flags.add(k)


def sim_available(model, s, st):
    """Mirror of Rules.Available with every contact present and the player in the right area (Recovery scenes excluded)."""
    ch = st.chapter
    if ch < s["MinChapter"] or ch > s["MaxChapter"] or s["Id"] in st.flags: return False
    if s["Chapters"] and ch not in s["Chapters"]: return False
    if not all(f in st.flags for f in s["Requires"]): return False
    for f in s["Forbids"]:
        ov = s["ForbidOverrides"].get(f)
        if f in st.flags and not (ov and ov in st.flags): return False
    if s["RequiresAny"] and not any(f in st.flags for f in s["RequiresAny"]): return False
    if not all(any(f in st.flags for f in g) for g in s["RequiresAnyGroups"]): return False
    if is_epilogue(s): return True
    if s["Recovery"] is not None: return False
    rel = model.rels.get(s["Relationship"], {})
    if rel.get("ClosedFlag") in st.flags and s["AfterRecovery"] is None: return False
    detects = device_detects(rel, s) if s["TricksterDevice"] else set()
    for f in rel.get("UnavailableFlags", []):
        ov = (rel.get("UnavailableOverrides") or {}).get(f)
        if f in st.flags and not (ov and ov in st.flags) and f not in detects: return False
    if s["Relationship"] == "tirabade":
        if not is_remote(s) and ch == 4: return False
        if s["Owner"] == "Together" and ch >= 5 and ("irabeth_away" in st.flags or "anevia_away" in st.flags): return False
    held = list(s["Requires"]) + [f for g in s["RequiresAnyGroups"] for f in g if f in st.flags]
    last = max([st.times[k] for k in held if k in st.times] or [st.hour - s["DelayHours"]])
    return st.hour - last >= s["DelayHours"]


def sim_bag(model, st, served, size, queued=(), cap=10 ** 9, skip=()):
    """Mirror of Rules.NextRemoteBag (E8); `skip` holds letters the simulated player declines."""
    def key(rel): return (model.rels.get(rel) or {}).get("RotationKey") or rel
    groups = collections.OrderedDict()
    for s in model.scenes:
        if not is_remote(s) or s["ManualOnly"] or is_epilogue(s) or s in queued or s["Id"] in skip: continue
        if sum(1 for q in queued if q["Relationship"] == s["Relationship"]) >= cap: continue
        if sim_available(model, s, st): groups.setdefault(key(s["Relationship"]), []).append(s)
    ranked = sorted(groups.values(), key=lambda g: (min(x["MaxChapter"] for x in g), max(served.get(x["Relationship"], -10 ** 9) for x in g)))
    bag = [g[0] for g in ranked[:max(0, size)]]
    order = {id(s): i for i, s in enumerate(model.scenes)}
    return sorted(bag, key=lambda s: order[id(s)])


def sim_key(model, s):
    return (model.rels.get(s["Relationship"]) or {}).get("RotationKey") or s["Relationship"]


def sim_mailbag(model, st, skip=()):
    """Mirror of Rules.MailbagArrivals (E8b): every deliverable letter, one per rotation key (its first in story order);
    the simulated pursuing player reads them all. `skip` holds letters the player declines."""
    groups = collections.OrderedDict()
    for s in model.scenes:
        if not is_remote(s) or s["ManualOnly"] or is_epilogue(s) or s["Id"] in skip: continue
        if sim_available(model, s, st): groups.setdefault(sim_key(model, s), s)
    return list(groups.values())


def sim_plan(model, s, st, rel_flags):
    """Best path through one scene: (score, choices); score = (commits? 0:1, closures set, completes? 0:1, length).
    Abort keeps the relationship open but leaves the scene unfinished."""
    committed, closed = rel_flags["committed"], rel_flags["closed"]
    nodes = model.nodes[s["Id"]]

    def best(node, held, gained, depth):
        if node not in nodes or depth > 24: return (1, 9, 1, depth), []
        found = None
        for c in nodes[node]["Choices"]:
            if not all(f in held for f in c["Requires"]) or any(f in held for f in c["Forbids"]): continue
            now, got = held | set(c["Set"]), gained | (set(c["Set"]) - held)
            nxt = c["Check"]["Success"] if c.get("Check") else c["Next"]
            if c["Abort"]: score, path = (0 if got & committed else 1, len(got & closed), 1, depth), []
            elif nxt is None: score, path = (0 if got & committed else 1, len(got & closed), 0, depth), []
            else: score, path = best(nxt, now, got, depth + 1)
            if found is None or score < found[0]: found = (score, [c] + path)
        return found or ((1, 9, 1, depth), [])

    return best(s["Nodes"][0]["Id"] if s["Nodes"] else None, set(st.flags), set(), 0)


def sim_wanted(plan):
    """A pursuing player opens a scene only when it commits, or completes without closing anything."""
    score, path = plan
    return bool(path) and (score[0] == 0 or (score[1] == 0 and score[2] == 0))


def sim_play(model, s, st, rel_flags, plan=None):
    """Plays one scene along its best path. Returns True when the scene completed."""
    if not is_epilogue(s) and s["NativeReturnCue"] is None:
        sf = model.rels.get(s["Relationship"], {}).get("StartedFlag")
        if sf and sf not in st.flags: st.flags.add(sf); st.times[sf] = st.hour
    _, path = plan or sim_plan(model, s, st, rel_flags)
    for c in path:
        for f in c["Set"]:
            if f not in st.flags: st.flags.add(f); st.times[f] = st.hour
        if c["Abort"]: return False
    if path and path[-1].get("Check") is None and path[-1]["Next"] is None:
        st.flags.add(s["Id"]); st.times[s["Id"]] = st.hour
        return True
    return False


def simulate_rest_budget(model, chapter_days=None, cadence=None, bag_size=3, cap=2, rests_per_chapter=None, caps=None, label="default",
                         natives=None, delivery="mailbag"):
    """E9: a Trickster full-roster campaign. Every relationship is pursued, physical scenes are visited daily for free,
    remote letters arrive only at rests: in the E8b mailbag (default: every deliverable letter, one per rotation key, all read)
    or in E8 post bags of `bag_size` (delivery="postbag", the opt-out). Natives: `trickster` from Chapter 1; every other native
    progress key a scene Requires turns true at the earliest MinChapter that requires it (loss, departure, hostility and
    other mythic paths are never forced)."""
    days = dict(SIM_CHAPTER_DAYS)
    days.update({c: d for c, d in (chapter_days or {}).items() if d > 0})
    cadence = cadence or {}
    loss_like = re.compile(r"dead|gone|away|absent|killed|hostile|departed|dismissed|lost|fail|kicked|unavailable|sacrifice|ascend|lich|swarm|locust")
    native_on = {}
    # Branch markers (a native some scene forbids: a fight, a rejection, a death) stay absent; pure progress keys turn on.
    # An inline scene (NativeReturnCue) forbidding a key marks a window inside a native dialog ("before she hears the
    # answer"), not a branch, so its forbids do not keep a progress key off.
    forbidden = {f for x in model.scenes if not is_epilogue(x) and not x.get("NativeReturnCue")
                 for f in list(x["Forbids"]) + [g for n in x["Nodes"] for c in n["Choices"] for g in c["Forbids"]]}
    for s in model.scenes:
        for f in list(s["Requires"]) + [x for g in s["RequiresAnyGroups"] for x in g] + list(s["RequiresAny"]):
            if f in model.native and f not in MYTHIC and not loss_like.search(f) and f != "true_lich" and f not in forbidden:
                native_on[f] = min(native_on.get(f, 99), s["MinChapter"])
    native_on.update(natives or {})   # --sim-natives: extra native keys forced true from a chapter
    rel_flags = {"committed": {r["CommittedFlag"] for r in model.rels.values()}, "closed": {r["ClosedFlag"] for r in model.rels.values()}}
    by_rel = collections.OrderedDict((rk, [s for s in model.scenes if s["Relationship"] == rk and not is_epilogue(s)
                                           and (not is_remote(s) or s["ManualOnly"])]) for rk in model.rels)
    st = SimState(1, 0)
    served, played, ever, commit_at, delivered, declined = {}, set(), {}, {}, collections.Counter(), set()
    per_rel_ch = collections.defaultdict(collections.Counter)
    chapters = []
    for ch in sorted(days):
        st.chapter = ch
        st.flags -= {"chapter_one", "chapter_later"}
        st.flags |= {"trickster", "chapter_one" if ch == 1 else "chapter_later"}
        st.flags |= {f for f, c in native_on.items() if c <= ch}
        hours = int(days[ch] * 24)
        step = cadence.get(ch) or (hours / rests_per_chapter[ch] if rests_per_chapter and rests_per_chapter.get(ch) else SIM_REST_CADENCE)
        available_rests = rests_per_chapter.get(ch) if rests_per_chapter and rests_per_chapter.get(ch) else int(hours // step)
        info = dict(chapter=ch, days=days[ch], rests_available=available_rests, rests_used=0, letters=0, missed=0, backlog_peak=0)
        start, next_rest, next_visit, rests_done = st.hour, st.hour + step, st.hour, 0
        end = start + hours
        while st.hour < end:
            sim_complete(model, st)
            if st.hour >= next_visit:   # a daily round of physical visits and manual reads: free
                next_visit += 24
                for rk, visitable in by_rel.items():
                    for s in visitable:
                        if s["Id"] in declined or not sim_available(model, s, st): continue
                        plan = sim_plan(model, s, st, rel_flags)
                        if not sim_wanted(plan):
                            declined.add(s["Id"]); continue
                        ever.setdefault(s["Id"], ch)
                        if sim_play(model, s, st, rel_flags, plan): played.add(s["Id"])
                        sim_complete(model, st)
                        break
            if st.hour >= next_rest and rests_done < available_rests:
                next_rest += step
                rests_done += 1
                for s in model.scenes:   # letters a pursuing player would decline are never requested
                    if (is_remote(s) and not s["ManualOnly"] and not is_epilogue(s) and s["Id"] not in declined
                            and sim_available(model, s, st) and not sim_wanted(sim_plan(model, s, st, rel_flags))):
                        declined.add(s["Id"])
                waiting = [s for s in model.scenes if is_remote(s) and not s["ManualOnly"] and not is_epilogue(s)
                           and s["Id"] not in declined and sim_available(model, s, st)]
                for s in waiting: ever.setdefault(s["Id"], ch)
                info["backlog_peak"] = max(info["backlog_peak"], len({(model.rels.get(s["Relationship"]) or {}).get("RotationKey") or s["Relationship"] for s in waiting}))
                bag = sim_mailbag(model, st, declined) if delivery == "mailbag" else sim_bag(model, st, served, bag_size, (), cap, declined)
                if bag: info["rests_used"] += 1
                for s in bag:
                    if not sim_available(model, s, st): continue
                    served[s["Relationship"]] = st.hour
                    if sim_play(model, s, st, rel_flags): played.add(s["Id"])
                    delivered[s["Relationship"]] += 1
                    per_rel_ch[s["Relationship"]][ch] += 1
                    info["letters"] += 1
                    sim_complete(model, st)
            for rk, r in model.rels.items():
                if r["CommittedFlag"] in st.flags and rk not in commit_at: commit_at[rk] = st.hour
            # Jump to the next event (a daily visit round or a rest); nothing else changes in between.
            targets = [next_visit, end] + ([next_rest] if rests_done < available_rests else [])
            st.hour = max(st.hour + 1, int(-(-min(targets) // 1)))
        missed_ids = [sid for sid, c in ever.items() if sid not in played and model.by_id[sid]["MaxChapter"] == ch]
        info["missed"] = len(missed_ids)
        if delivery == "mailbag":
            # A rest delivers every waiting route at once, so rests bound only each route's chain: the worst rotation key
            # needs one more delivery moment per letter it missed.
            per_key = collections.Counter(sim_key(model, model.by_id[sid]) for sid in missed_ids)
            info["rests_needed"] = info["rests_used"] + (max(per_key.values()) if per_key else 0)
            info["load"] = round(info["rests_needed"] / float(max(1, info["rests_available"])), 2)
        else:
            info["rests_needed"] = info["rests_used"] + -(-info["missed"] // max(1, bag_size))
            info["load"] = round((info["letters"] + info["missed"]) / float(max(1, info["rests_available"] * bag_size)), 2)
        chapters.append(info)
    rels = []
    for rk, r in model.rels.items():
        missed = sorted(sid for sid, c in ever.items() if sid not in played and model.by_id[sid]["Relationship"] == rk)
        over = []
        if caps:
            for ch, n in per_rel_ch[rk].items():
                limit = caps.get("ch%d" % ch)
                if limit is not None and n > limit: over.append("ch%d %d>%d" % (ch, n, limit))
        why = None
        if rk not in commit_at:   # the nearest unplayed scene and what keeps it shut at the end of the run
            cands = []
            for x in model.scenes:
                if x["Relationship"] != rk or is_epilogue(x) or x["Id"] in played: continue
                miss = [f for f in x["Requires"] if f not in st.flags]
                forb = [f for f in x["Forbids"] if f in st.flags and not (x["ForbidOverrides"].get(f) in st.flags)]
                cands.append((len(miss) + len(forb) + (1 if x["Id"] in declined else 0), x["Id"], miss, forb, x["Id"] in declined))
            if cands:
                _, sid, miss, forb, dec = min(cands)
                why = "%s%s%s%s" % (sid, (" needs " + ",".join(miss[:3])) if miss else "", (" forbidden by " + ",".join(forb[:3])) if forb else "",
                                     " (declined: only aborts or closes)" if dec else "")
        rels.append(dict(relationship=rk, committed=rk in commit_at, day=(commit_at[rk] // 24 + 1) if rk in commit_at else None,
                         letters={("ch%d" % c): n for c, n in sorted(per_rel_ch[rk].items())}, missed=missed, over_caps=over, blocked=why))
    return dict(label=label, chapter_days=days, bag_size=bag_size, queue_cap=cap, delivery=delivery, chapters=chapters, relationships=rels)


def print_rest_budget(res, P):
    days = res["chapter_days"]
    if res.get("delivery", "postbag") == "mailbag":
        P("\n## E9. Rest budget [%s]: Trickster full-roster simulation, E8b mailbag (every deliverable letter at each rest, one"
          " per rotation key; the player reads them all). Load = delivery moments needed / rests available" % res["label"])
    else:
        P("\n## E9. Rest budget [%s]: Trickster full-roster simulation, E8 post bags of %d, <= %d unread per relationship"
          % (res["label"], res["bag_size"], res["queue_cap"]))
    P("  Chapter lengths in in-game days (ESTIMATES, calibrate against real Trickster runs): %s"
      % ", ".join("ch%d %s" % (c, d) for c, d in sorted(days.items())))
    P("  Physical scenes and manual reads are visited daily at no rest cost; native progress keys (required somewhere, forbidden")
    P("  nowhere, not loss/departure) turn true at the first chapter a scene needs them; each scene follows its committing path, else a path that completes without")
    P("  closing anything; scenes that would only abort or close (partings, refusals) are declined and cost nothing.")
    P("\n  RESTS NEEDED vs AVAILABLE")
    P("  %-8s %6s %10s %10s %11s %8s %8s %13s %6s" % ("chapter", "days", "available", "used", "needed", "letters", "missed", "peak waiting", "load"))
    for c in res["chapters"]:
        flag = "  OVER" if c["rests_needed"] > c["rests_available"] or c["load"] > 1.0 else ""
        P("  ch%-6d %6s %10d %10d %11d %8d %8d %13d %6.2f%s" % (c["chapter"], c["days"], c["rests_available"], c["rests_used"],
                                                             c["rests_needed"], c["letters"], c["missed"], c["backlog_peak"], c["load"], flag))
    P("\n  %-24s %-9s %-6s %-26s %s" % ("relationship", "committed", "day", "letters per chapter", "scenes that missed their window"))
    for r in res["relationships"]:
        letters = " ".join("%s:%d" % kv for kv in r["letters"].items()) or "-"
        missed = ", ".join(r["missed"][:4]) + (" (+%d)" % (len(r["missed"]) - 4) if len(r["missed"]) > 4 else "") if r["missed"] else "-"
        over = ("  CAP " + ", ".join(r["over_caps"])) if r["over_caps"] else ""
        P("  %-24s %-9s %-6s %-26s %s%s" % (r["relationship"][:24], "yes" if r["committed"] else "NO", r["day"] or "-", letters[:26], missed, over))
        if r.get("blocked"): P("  %-24s   stops at %s" % ("", r["blocked"]))
    n_commit = sum(1 for r in res["relationships"] if r["committed"])
    P("  => %d/%d relationships reach CommittedFlag; %d scenes missed their window; chapters over budget: %s"
      % (n_commit, len(res["relationships"]), sum(len(r["missed"]) for r in res["relationships"]),
         [c["chapter"] for c in res["chapters"] if c["rests_needed"] > c["rests_available"] or c["load"] > 1.0] or "none"))

# ----------------------------------------------------------------------------------------- TT-20 matrix mode
LOSS_LIKE = re.compile(r"dead|gone|hostile|killed|departed|closed")


def matrix_rel_ids(c, rels=None):
    """'nocticula (+ nocticula.acquisition)' -> ['nocticula', 'nocticula.acquisition'] (registered ids only when rels given)."""
    raw = c.get("relationship_id") or ""
    toks = re.findall(r"[a-z][a-z0-9_]*(?:\.[a-z0-9_]+)*", raw.split("(renamed")[0])
    if rels is None: return toks[:1] + [t for t in toks[1:] if "." in t]
    return [t for t in toks if t in rels]


def matrix_states(c):
    return c.get("states") or c.get("native_states") or []


def matrix_scene_ids(st):
    """Device scene ids of one state: v2 setup / fallback_setup / payoff objects, v1 setup_scene_id / device_scene_id."""
    ids = []
    for k in ("setup", "fallback_setup", "payoff"):
        v = st.get(k)
        if isinstance(v, dict) and v.get("id"): ids.append(v["id"])
    for k in ("setup_scene_id", "device_scene_id"):
        if st.get(k): ids.append(st[k])
    return ids


def matrix_world_keys(model, st, guid_to_key):
    """(true, false, unresolved) native keys one state forces. Authored keys are left for scenes to produce."""
    det = st.get("detect") or {}
    if isinstance(det, list): det = {"story_keys": det}
    pos = list(det.get("all", [])) + [k for k in det.get("story_keys", []) if not k.startswith("!")]
    neg = list(det.get("none", [])) + [k[1:] for k in det.get("story_keys", []) if k.startswith("!")]
    true, false, unresolved = set(), set(), []
    for keys, into in ((pos, true), (neg, false)):
        for key in keys:
            if key in model.native or key in model.builtin_derived: into.add(key)
            elif key not in model.authored and key not in model.derived: unresolved.append(key)
    for kind in ("etudes", "cues", "answers", "quests"):
        for g in det.get(kind, []):
            g = str(g).replace("!bp_", "").lower()
            if g in guid_to_key: true.add(guid_to_key[g])
            else: unresolved.append("%s:%s" % (kind[:-1], g[:8]))
    return true, false, unresolved


def matrix_rest_budget(model, matrix, P):
    """E9 in --matrix mode: the default cadence plus every supply profile in matrix.rest_budget (rests per chapter)."""
    budget = matrix.get("rest_budget") or {}
    opts = dict(REST_OPTIONS or {})
    opts["bag_size"] = budget.get("pages_per_rest", opts.get("bag_size", 3))
    caps = budget.get("per_relationship_caps")
    runs = [simulate_rest_budget(model, caps=caps, label="cadence", **opts)]
    for name, supply in (budget.get("supply_profiles") or {}).items():
        rests = {int(k[2:]): v for k, v in supply.items() if k.startswith("ch")}
        runs.append(simulate_rest_budget(model, rests_per_chapter=rests, caps=caps, label="profile " + name,
                                         **{k: v for k, v in opts.items() if k != "cadence"}))
    for r in runs: print_rest_budget(r, P)
    return {"rest_budget": runs}


def run_matrix(matrix_path, story_path, strict=False, out_json=None, extra=None):
    story = json.loads(Path(story_path).read_text(encoding="utf-8"))
    matrix = json.loads(Path(matrix_path).read_text(encoding="utf-8"))
    model = Model(story)
    guid_to_key = {}
    for sec in ("Etudes", "CompletedEtudes", "CompletedQuests", "SelectedAnswers", "StartedDialogs", "UnlockableFlags", "InventoryItems"):
        for k, g in (story.get(sec) or {}).items(): guid_to_key.setdefault(str(g).lower(), k)
    for k, v in (story.get("QuestObjectives") or {}).items(): guid_to_key.setdefault(str(v[0]).lower(), k)
    for k, v in (story.get("SeenCues") or {}).items():
        for g in v: guid_to_key.setdefault(g.lower(), k)
    cache = {}

    def reach(true, false):
        key = (frozenset(true), frozenset(false))
        if key not in cache:
            world = mythic_world("trickster", model, "matrix", true=true, false=false)
            # A state that detects `none: trickster` (the lost path) is not also forced into the live Trickster world.
            world.true -= set(false)
            cache[key] = Reach(model, world)
        return cache[key]

    chars = matrix.get("characters", [])
    # forbids_never: flags of one relationship that no scene of ANY other relationship may Require or Forbid.
    never = {}
    for c in chars:
        fl = set(c.get("forbids_never", []) if isinstance(c.get("forbids_never"), list) else [])
        for x in list(c.get("coexistence_constraints", [])) + list(matrix_states(c)):
            if isinstance(x, dict): fl |= set(x.get("forbids_never", []))
        never[c.get("character")] = fl
    explicit_never = any(never.values())
    # The combined Trickster world: every device state's detect forced at once.
    # Only implemented device states (scenes in Story.json, detect keys bound) are forced; planned ones are spec-only.
    combined_true, combined_false, combined_spec = set(), set(), 0
    for c in chars:
        for st in matrix_states(c):
            ids = matrix_scene_ids(st)
            if not ids: continue
            t, f, unresolved = matrix_world_keys(model, st, guid_to_key)
            if unresolved or any(i not in model.by_id for i in ids):
                combined_spec += 1
                continue
            combined_true |= t; combined_false |= f
    conflict = combined_true & combined_false
    combined_true -= conflict; combined_false -= conflict
    combined = reach(combined_true, combined_false)
    story_reactions = collections.Counter()
    for s in model.scenes:
        if s["Reaction"]: story_reactions[s["Relationship"]] += 1

    lines = []
    P = lines.append
    P("# TT-20 Trickster matrix %s (%s, %d characters) vs %s" % (matrix_path, matrix.get("schema", "?"), len(chars), story_path))
    P("# world  = trickster playing + the state's detect keys forced (authored keys must be produced by scenes)")
    P("# entry  = each state's device scenes (setup/payoff) reachable; a state with no device needs any scene of the relationship")
    P("# commit = the relationship's CommittedFlag reachable in each evaluated state")
    P("# coexist= CommittedFlag reachable with ALL implemented device states forced at once, and none of the relationship's scenes Requires or")
    P("#          Forbids another character's forbids_never flag%s" % ("" if explicit_never else " (no forbids_never in the matrix: other relationships' ClosedFlag/loss flags, Requires only)"))
    P("# spec-only = the relationship, its device scenes or a detect key are not in Story.json yet (reported, never failing)")
    hdr = "%-18s %-22s %-16s %-24s %-14s %-22s %s" % ("character", "relationship", "status", "entry", "commit", "coexist", "reactions(story/spec)")
    P(""); P(hdr); P("-" * len(hdr))
    rows, failures = [], 0
    for c in chars:
        name, status = c.get("character", "?"), str(c.get("relationship_status", "?"))
        rids = matrix_rel_ids(c, model.rels)
        soft = status.startswith("pending") or status.startswith("draft") or status.startswith("new")
        row = dict(character=name, relationship=c.get("relationship_id"), registered=rids, status=status, notes=[])
        spec_react = sum(len(st.get("reactions") or []) for st in matrix_states(c))
        story_react = sum(story_reactions[r] for r in rids)
        if not rids:
            row.update(entry="spec-only", commit="spec-only", coexist="spec-only")
        else:
            rels = [model.rels[r] for r in rids]
            rel_scenes = [s for s in model.scenes if s["Relationship"] in rids and not is_epilogue(s)]
            ent_ok = ent_n = com_ok = spec = 0
            for st in matrix_states(c):
                t, f, unresolved = matrix_world_keys(model, st, guid_to_key)
                ids = matrix_scene_ids(st)
                missing = [i for i in ids if i not in model.by_id]
                if unresolved or missing:
                    spec += 1
                    why = (["scenes " + ",".join(missing)] if missing else []) + (["keys " + ",".join(unresolved[:3])] if unresolved else [])
                    row["notes"].append("%s: spec-only (%s)" % (st.get("state"), "; ".join(why)))
                    continue
                rr = reach(t, f)
                ent_n += 1
                # Canon fate stands (doc 03 §2.7): the path is lost and the character is unavailable. Nothing may
                # defy it: the state passes when no Trickster device of the relationship is reachable and needs no commit.
                canon = not ids and "trickster.failed" in t and bool(t & {u for r in rels for u in r.get("UnavailableFlags", [])})
                if canon:
                    devices = [s["Id"] for s in rel_scenes if s.get("TricksterDevice") and s["Id"] in rr.reached]
                    ok = committed = not devices
                    if devices: row["notes"].append("%s: canon fate defied by %s" % (st.get("state"), ",".join(devices[:3])))
                    ent_ok += ok; com_ok += committed
                    continue
                # A primer that Forbids its own state's event runs before it; a world forced into the event from the
                # start cannot reach it, so the state is judged by its fallback and payoff instead.
                # Likewise a setup that Requires a flag only such a primer plants (every producer Forbids the event).
                def primed_before(i):
                    return any(model.producers.get(f) and all(set(model.by_id[p]["Forbids"]) & t for p, _, _ in model.producers[f])
                               for f in model.by_id[i]["Requires"])
                need = [i for i in ids if not set(model.by_id[i]["Forbids"]) & t and not primed_before(i)] or ids
                ok = all(i in rr.reached for i in need) if ids else any(s["Id"] in rr.reached for s in rel_scenes)
                committed = any(r["CommittedFlag"] in rr.held for r in rels)
                ent_ok += ok; com_ok += committed
                if not ok or not committed:
                    row["notes"].append("%s: %s%s" % (st.get("state"), "" if ok else "entry unreachable ", "" if committed else "commit unreachable"))
            tail = " +%d spec-only" % spec if spec else ""
            row["entry"] = ("spec-only" if ent_n == 0 else ("PASS" if ent_ok == ent_n else "FAIL") + " %d/%d" % (ent_ok, ent_n)) + (tail if ent_n else "")
            row["commit"] = "spec-only" if ent_n == 0 else ("PASS" if com_ok == ent_n else "FAIL") + " %d/%d" % (com_ok, ent_n)
            if explicit_never:
                # Characters sharing this relationship (Minagho/Chivarro) are not "another entry".
                watched = set().union(set(), *[never[x.get("character")] for x in chars
                                               if not set(matrix_rel_ids(x, model.rels)) & set(rids)]) - set(never.get(name, set()))
            else:
                own_unavail = {f for r in rels for f in r.get("UnavailableFlags", [])}
                watched = {r["ClosedFlag"] for k, r in model.rels.items() if k not in rids} | {
                    f for k, r in model.rels.items() if k not in rids for f in r.get("UnavailableFlags", [])
                    if LOSS_LIKE.search(f) and f not in own_unavail and f not in MYTHIC}
            # The character's own G6 grief rule and cross-route allowlist (matrix) excuse exactly the designed reads:
            # G6(b) a Forbids <death> lifted by ForbidOverrides {<death>: <return>}; G6(a) a grief page that Requires
            # <death> and Forbids <return>; an allowlisted scene that Requires the other character's return flag.
            grief = {g["flag"]: g["return_flag"] for g in (c.get("grief_rule") or [])
                     if isinstance(g, dict) and g.get("return_flag") not in (None, "", "n/a")}
            grief_of = {ret: flag for flag, ret in grief.items()}
            allow = {k.split(" ")[0]: set(v) for k, v in (c.get("cross_route_allowlist") or {}).items() if isinstance(v, list)}
            deps = []
            for s in model.scenes:
                if s["Relationship"] not in rids or s["Reaction"]: continue
                pos = set(s["Requires"]) | set(s["RequiresAny"]) | {x for g in s["RequiresAnyGroups"] for x in g}
                deps += ["%s requires %s" % (s["Id"], f) for f in sorted(pos & watched)
                         if f not in allow.get(s["Id"], ()) and not (f in grief and grief[f] in s["Forbids"])]
                if explicit_never: deps += ["%s forbids %s" % (s["Id"], f) for f in sorted(set(s["Forbids"]) & watched)
                                            if not (f in grief and s["ForbidOverrides"].get(f) == grief[f])
                                            and not (f in grief_of and grief_of[f] in pos)]
            committed_all = any(r["CommittedFlag"] in combined.held for r in rels)
            row["coexist"] = "PASS" if committed_all and not deps else "FAIL" + ("" if committed_all else " commit") + (" %d dep" % len(deps) if deps else "")
            if deps: row["notes"].append("coexistence: " + "; ".join(deps[:3]) + (" (+%d more)" % (len(deps) - 3) if len(deps) > 3 else ""))
        row["reactions"] = dict(story=story_react, spec=spec_react)
        failed = any(str(row[k]).startswith("FAIL") for k in ("entry", "commit", "coexist"))
        row["failed"] = bool(failed and not soft)
        failures += row["failed"]
        P("%-18s %-22s %-16s %-24s %-14s %-22s %d/%d" % (name[:18], (",".join(rids) or matrix_rel_ids(c)[0] if matrix_rel_ids(c) else "-")[:22],
                                                        status[:16], row["entry"], row["commit"], row["coexist"], story_react, spec_react))
        for n in row["notes"][:5]: P("      - " + n)
        if len(row["notes"]) > 5: P("      - ... %d more" % (len(row["notes"]) - 5))
        rows.append(row)
    P("")
    P("combined Trickster world: %d native keys forced true, %d false; %d conflicting keys dropped %s; %d planned device states not forced (spec-only)"
      % (len(combined_true), len(combined_false), len(conflict), sorted(conflict)[:6], combined_spec))
    P("rows: %d; FAIL rows among registered relationships: %d (draft/new/pending rows report without failing)" % (len(rows), failures))
    result = dict(schema=matrix.get("schema"), rows=rows, failures=failures,
                  combined_true=sorted(combined_true), combined_false=sorted(combined_false))
    if extra is not None:
        result.update(extra(model, matrix, P))
    text = "\n".join(lines)
    print(text)
    if out_json: Path(out_json).write_text(json.dumps(result, indent=1, default=str), encoding="utf-8")
    return result, (1 if strict and failures else 0)

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
    ap.add_argument("--matrix", help="TT-20: check a trickster-matrix.json against the story (report; --strict fails on registered rows)")
    ap.add_argument("--matrix-json", default=str(HERE / "rrt_verify_report.matrix.json"))
    ap.add_argument("--rest-cadence", help="E9: hours of travel per rest, one value or per chapter '3:16,5:12' (default 16)")
    ap.add_argument("--chapter-days", help="E9: in-game days per chapter, e.g. '3:30,4:12,5:40' (defaults are estimates)")
    ap.add_argument("--delivery", choices=["mailbag", "postbag"], default="mailbag",
                    help="E9: E8b mailbag (default: every letter at each rest) or the E8 post bag opt-out (--bag-size per rest)")
    ap.add_argument("--bag-size", type=int, default=3, help="E9: letters per rest (E8 PostBagSize; --delivery postbag)")
    ap.add_argument("--queue-cap", type=int, default=2, help="E9: undelivered letters per relationship (E8 QueueCapPerRelationship)")
    ap.add_argument("--sim-natives", help="E9: extra native keys held from a chapter, e.g. 'seelah.souls_returned:5,vellexia.native_finished:3'")
    a = ap.parse_args()
    try:   # matrix text carries arrows and em dashes; never crash a Windows console on them
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    def per_chapter(text, cast):
        if not text: return {}
        if ":" not in text: return {c: cast(text) for c in range(1, 7)}
        return {int(k): cast(v) for k, v in (x.split(":") for x in text.split(","))}
    REST_OPTIONS.update(cadence=per_chapter(a.rest_cadence, float), chapter_days=per_chapter(a.chapter_days, float),
                        bag_size=a.bag_size, cap=a.queue_cap, delivery=a.delivery,
                        natives={k: int(v) for k, v in (x.split(":") for x in a.sim_natives.split(","))} if a.sim_natives else {})
    if a.matrix:
        _, code = run_matrix(a.matrix, a.story, strict=a.strict, out_json=a.matrix_json, extra=matrix_rest_budget)
        sys.exit(code)
    R, text = run(a.story, Path(a.game), use_zip=not a.no_zip, drafts=a.drafts, out_json=a.json, quiet=a.quiet)
    Path(a.text).write_text(text, encoding="utf-8")
    hard = len(R["validate_errors"]) + len(R["no_producer_required"]) + len(R.get("typeid", {}).get("problems", [])) \
        + len(R.get("bindings", {}).get("failures", [])) + len(R["runtime"]["duplicate_names"]) + len(R["runtime"]["retry_dups"])         + len(R.get("released_names_removed", []))
    for x in R.get("released_names_removed", [])[:20]: print("SAVE BREAK (name from a released build no longer registered):", x)
    print("\nHARD FAILURES: %d  (report: %s)" % (hard, a.text))
    if a.strict and hard: sys.exit(1)


if __name__ == "__main__":
    main()

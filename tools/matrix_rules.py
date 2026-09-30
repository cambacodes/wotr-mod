"""matrix_rules.py - runtime-rule checks for trickster-matrix.json scene objects (used by matrix_check.py --rules).

Mirrors what src/Story.cs Rules.Validate and src/Main.cs Build enforce, per scene object (setup / fallback_setup / payoff
and their *_alt / extra variants), against blueprints.zip. Every finding carries a severity:

  FATAL     Rules.Validate throws: Story.json fails to load and the WHOLE MOD is disabled.
  DEGRADES  Main.Build disables the scene's relationship (rrt.degraded.<rel>), saves stay resolvable.
  BLOCKED   loads fine, but the scene can never be available (its relationship's own unavailable flag blocks it).
  GATE      runtime works, but the build gate (rrt_verify --strict section F) fails.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rrt_verify as rv  # noqa: E402  (blueprint index, parent bindings, enum tables)

GUID = re.compile(r"^[0-9a-f]{32}$")
# Native NPC answer lists used as hosts. Fye leaves the capital (Fye_Bartender_NotInCapital 60d1237d) once the tavern is
# lost; the quartermaster Wilcer Garms is always present but anchor hosting is the fallback only (05 ERRATA).
DEFAULT_ANCHORS = {
    "9b15b09c244076047b02f317e55ef5e3": {"name": "Fye", "hidden_by": "60d1237d", "fallback_only": True},
    "3c58e83a970a0f643a88e15f2323c805": {"name": "Wilcer Garms", "fallback_only": True},
}
SCENE_KEYS = ("setup", "fallback_setup", "payoff", "setup_alt", "payoff_alt", "setup_c5", "foresight_setup", "primer")
MYTHIC_PATHS = {"Aeon", "Angel", "Azata", "Demon", "Devil", "Dragon", "Legend", "Lich", "Locust", "Trickster"}


def truthy(o, *names):
    return any(bool(o.get(n)) for n in names)


NON_SCENE_KEYS = {"detect", "cost", "reactions", "rules_test", "rules_tests_extra", "additional_rules_tests",
                  "extra_rules_tests", "rules_test_extra", "todo", "exclusive_with"}


def is_scene(o):
    return isinstance(o, dict) and isinstance(o.get("id"), str) and any(k in o for k in ("kind", "min_chapter", "requires", "remote"))


def scene_objects(state):
    """Every scene object of a state: setup / fallback_setup / payoff first, then any other key holding scene objects
    (setup_alt, payoff_alt, primer, continuation(s), epilogue(s), extra_setups, ...)."""
    keys = [k for k in SCENE_KEYS if k in state] + [k for k in state if k not in SCENE_KEYS and k not in NON_SCENE_KEYS]
    for key in keys:
        v = state.get(key)
        for o in (v if isinstance(v, list) else [v]):
            if is_scene(o):
                yield key, o


def choices(o):
    out = []
    for key in ("choice", "choices", "alt_choices", "entry_choice", "swap_choice", "crusade_on_terms_choice", "choice_raised"):
        v = o.get(key)
        for x in (v if isinstance(v, list) else [v]):
            if isinstance(x, dict): out.append(x)
    return out


def mythic_ok(value):
    return value in MYTHIC_PATHS or value in rv.MYTHIC_ENUM


def alignment_ok(value):
    if isinstance(value, dict): value = (value.get("Direction") or value.get("direction"), value.get("Value") or value.get("value"))
    return (isinstance(value, (list, tuple)) and len(value) == 2 and value[0] in rv.ALIGNMENT_DIRECTIONS
            and isinstance(value[1], int) and 0 < value[1] <= 100)


def terminal(ch):
    return not ch.get("next") and not ch.get("then") and not ch.get("check") and not ch.get("abort")


class Archive:
    def __init__(self, game):
        self.idx, _ = rv.build_bp_index(Path(game))
        self.parent = rv.parent_bindings()
        self.zip = zipfile.ZipFile(Path(game) / "blueprints.zip")
        self.cache = {}

    def type(self, g):
        if g in self.idx: return self.idx[g][0]
        return self.parent.get(g, (None,))[0]

    def data(self, g):
        if g not in self.idx: return None
        if g not in self.cache: self.cache[g] = json.loads(self.zip.read(self.idx[g][1]))["Data"]
        return self.cache[g]

    def dialog(self, g):
        """(dialog guid or None, reason) walking ParentAsset from a cue or list to its BlueprintDialog."""
        seen = set()
        while g in self.idx and g not in seen:
            if self.idx[g][0] == "BlueprintDialog": return g, None
            seen.add(g)
            nxt = (self.data(g) or {}).get("ParentAsset")
            if not nxt:
                return None, "%s %s has no ParentAsset" % (self.idx[g][0], g[:8])
            g = nxt
        return None, "ParentAsset chain leaves blueprints.zip at %s" % (g[:8] if g else g)


def refs(d, field):
    v = d.get(field)
    if isinstance(v, dict): v = v.get("Cues") or v.get("Actions") or v.get("Conditions")
    return [str(x).replace("!bp_", "") if isinstance(x, str) else x for x in (v or [])]


def check_return_cue(ar, cue, lst, where, out):
    t = ar.type(cue)
    if t is None:
        out.append(("DEGRADES", where, "native_return_cue %s is not in blueprints.zip or a reviewed parent manifest" % cue)); return
    if t != "BlueprintCue":
        out.append(("DEGRADES", where, "native_return_cue %s is a %s, not a BlueprintCue" % (cue, t))); return
    d = ar.data(cue)
    if d is None:
        out.append(("DEGRADES", where, "native_return_cue %s is parent-owned; Build's safety checks cannot be verified offline" % cue)); return
    bad = []
    if d.get("ShowOnce") or d.get("ShowOnceCurrentDialog"): bad.append("ShowOnce")
    if ((d.get("Conditions") or {}).get("Conditions") or []): bad.append("Conditions")
    if ((d.get("OnShow") or {}).get("Actions") or []): bad.append("OnShow actions")
    if ((d.get("OnStop") or {}).get("Actions") or []): bad.append("OnStop actions")
    cont = (d.get("Continue") or {}).get("Cues") or []
    if cont: bad.append("Continue cues %s" % [str(c).replace("!bp_", "")[:8] for c in cont])
    if d.get("Experience", "NoExperience") != "NoExperience": bad.append("Experience %s" % d.get("Experience"))
    if ((d.get("AlignmentShift") or {}).get("Value") or 0) != 0: bad.append("AlignmentShift")
    answers = [str(a).replace("!bp_", "") for a in d.get("Answers") or []]
    if len(answers) != 1 or answers[0] != lst:
        bad.append("answers %s != [the scene's list %s]" % ([a[:8] for a in answers], (lst or "?")[:8]))
    if bad:
        out.append(("DEGRADES", where, "native_return_cue %s fails Main.Build's native-return checks: %s" % (cue[:8], "; ".join(bad))))
    if lst and ar.type(lst) == "BlueprintAnswersList":
        ld = ar.data(lst) or {}
        lbad = []
        if ld.get("ShowOnce"): lbad.append("ShowOnce")
        if ((ld.get("Conditions") or {}).get("Conditions") or []): lbad.append("Conditions")
        if ld.get("MythicRequirement", "None") not in ("None", None): lbad.append("MythicRequirement " + str(ld.get("MythicRequirement")))
        if ld.get("AlignmentRequirement", "None") not in ("None", None): lbad.append("AlignmentRequirement " + str(ld.get("AlignmentRequirement")))
        if lbad: out.append(("DEGRADES", where, "answer list %s of an inline scene fails the native-return checks: %s" % (lst[:8], "; ".join(lbad))))


def validate_rules(matrix, ar, story=None):
    """{character: [(severity, where, message)]}"""
    story = story or {}
    rels = story.get("Relationships") or {}
    bindings = matrix.get("bindings") or {}
    removable = set(matrix.get("removable_items") or [])
    # anchor_lists: {list_guid: {name, hidden_by?: native flag that removes the NPC, fallback_only?: true}}
    anchors = dict(DEFAULT_ANCHORS)
    anchors.update(matrix.get("anchor_lists") or {})
    results = {}
    for c in matrix.get("characters", []):
        out = []
        name = c.get("character", "?")
        rids = re.findall(r"[a-z][a-z0-9_]*(?:\.[a-z0-9_]+)*", (c.get("relationship_id") or "").split("(renamed")[0])
        own_rel = rids[0] if rids else None
        overrides = dict(c.get("unavailable_overrides") or {})
        access = c.get("trickster_access") or {}
        hub_presences = {}
        for key in ("presences", "presences_add"):
            v = c.get(key)
            if isinstance(v, dict): hub_presences.update({k: x for k, x in v.items() if isinstance(x, dict)})
        if isinstance(c.get("presence"), dict) and c["presence"].get("key"): hub_presences[c["presence"]["key"]] = c["presence"]

        def unavailable(rel):
            flags = set((rels.get(rel) or {}).get("UnavailableFlags") or [])
            if rel == own_rel or rel in rids:   # declared overridable flags, plus an explicit list if the spec gives one
                flags |= set(overrides) | set(c.get("unavailable_flags") or [])
            return flags

        returned = set(overrides.values()) | {a.get("returned") for a in access.values() if isinstance(a, dict) and a.get("returned")}
        for st in c.get("states") or []:
            det = st.get("detect") or {}
            detected = set(det.get("all", []) if isinstance(det, dict) else [])
            for role, o in scene_objects(st):
                sid = o["id"]
                where = "%s/%s %s" % (st.get("state"), role, sid)
                kind = o.get("kind") or ("remote" if o.get("remote") else "physical")
                epilogue = kind == "epilogue" or str(o.get("owner") or "").endswith("Epilogue")
                remote = kind == "remote" or o.get("remote") is True
                inline = o.get("native_return_cue")
                lists = [g for g in o.get("answer_lists") or [] if isinstance(g, str)]
                chs = choices(o)
                req = set(o.get("requires") or [])
                # 1. inline scenes
                if inline:
                    if o.get("contact_unit"):
                        out.append(("FATAL", where, "inline scene (native_return_cue) also sets contact_unit; Rules.Validate throws"))
                    if remote or epilogue or len(lists) != 1:
                        out.append(("FATAL", where, "inline scene must be physical with exactly one answer list (has %d%s)" % (len(lists), ", remote" if remote else "")))
                    if any(ch.get("revive") for ch in chs):
                        out.append(("FATAL", where, "inline scene cannot carry a revive choice"))
                    if not GUID.match(str(inline)):
                        out.append(("FATAL", where, "native_return_cue %r is not a 32-hex GUID" % inline))
                    else:
                        check_return_cue(ar, inline, lists[0] if len(lists) == 1 else None, where, out)
                # 2. native_next (scene-level means the scene's terminal choice)
                nexts = [(ch.get("native_next"), ch) for ch in chs if ch.get("native_next")]
                if o.get("native_next"): nexts.append((o["native_next"], None))
                for nn, ch in nexts:
                    if not GUID.match(str(nn)):
                        out.append(("FATAL", where, "native_next %r is not a 32-hex GUID" % nn)); continue
                    if not inline:
                        out.append(("FATAL", where, "native_next %s outside an inline scene (needs native_return_cue)" % nn[:8]))
                    if ch is not None and not terminal(ch):
                        out.append(("FATAL", where, "native_next %s on a non-terminal choice (next/then/check/abort)" % nn[:8]))
                    if ch is not None and ch.get("revive"):
                        out.append(("FATAL", where, "native_next %s on a revive choice" % nn[:8]))
                    if inline and nn == inline:
                        out.append(("FATAL", where, "native_next equals the scene's own native_return_cue"))
                    t = ar.type(nn)
                    if t != "BlueprintCue":
                        out.append(("DEGRADES", where, "native_next %s is %s, not a BlueprintCue" % (nn[:8], t or "missing from blueprints.zip")))
                    elif lists:
                        d1, why1 = ar.dialog(nn)
                        d2, why2 = ar.dialog(lists[0])
                        if d1 is None or d2 is None or d1 != d2:
                            out.append(("GATE", where, "native_next %s does not reach the answer list's dialog (%s)"
                                        % (nn[:8], why1 or why2 or "cue dialog %s vs list dialog %s" % (d1[:8], d2[:8]))))
                # 3. epilogue pages
                if epilogue:
                    if o.get("entry_mythic") or o.get("entry_alignment") or any(ch.get("mythic") or ch.get("alignment") or ch.get("crusade") or ch.get("remove_item") for ch in chs):
                        out.append(("FATAL", where, "mythic/alignment/crusade/remove_item on an epilogue page"))
                else:
                    for ch in chs:
                        if ch.get("mythic") and not mythic_ok(ch["mythic"]):
                            out.append(("FATAL", where, "unknown mythic %r" % ch["mythic"]))
                        if ch.get("alignment") and not alignment_ok(ch["alignment"]):
                            out.append(("FATAL", where, "invalid alignment %r (direction, 1-100)" % (ch["alignment"],)))
                        cr = ch.get("crusade")
                        if cr and (not isinstance(cr, (list, tuple)) or len(cr) != 2 or cr[0] not in rv.CRUSADE_RESOURCES
                                   or not isinstance(cr[1], int) or cr[1] == 0 or abs(cr[1]) > 100000):
                            out.append(("FATAL", where, "invalid crusade %r (Finances/Materials/Favors, non-zero int)" % (cr,)))
                        elif cr and isinstance(o.get("min_chapter"), int) and o["min_chapter"] < 3:
                            out.append(("FATAL", where, "crusade cost in a scene starting before Chapter 3"))
                    if o.get("entry_mythic") and (remote or not mythic_ok(o["entry_mythic"])):
                        out.append(("FATAL", where, "entry_mythic %r needs a physical entry and a Mythic name" % o["entry_mythic"]))
                    if o.get("entry_alignment") and (remote or not alignment_ok(o["entry_alignment"])):
                        out.append(("FATAL", where, "entry_alignment %r needs a physical entry and (direction, 1-100)" % (o["entry_alignment"],)))
                # 5. remove_item whitelist and holding gate
                for ch in chs:
                    ri = ch.get("remove_item")
                    if not ri: continue
                    if ri not in removable:
                        out.append(("FATAL", where, "remove_item %s is not in top-level removable_items" % ri))
                    gate = set(ch.get("requires") or []) | req
                    if not any((bindings.get(k) or {}).get("kind") == "InventoryItems" and (bindings.get(k) or {}).get("guid") == ri for k in gate):
                        out.append(("FATAL", where, "remove_item %s is not gated on an InventoryItems binding for that item" % ri[:8]))
                # 4. TricksterDevice
                device = truthy(o, "trickster_device", "TricksterDevice", "tricksterdevice")
                rel = o.get("relationship") or own_rel
                own_flags = unavailable(rel) if rel else set()
                if not epilogue:
                    # An inline scene that does not Require the flag is the native-moment hook (e.g. a deathbed answer),
                    # played before the fate is recorded; every other scene of the state runs while the flag holds.
                    # Continuations run after the return is recorded (the override lifts the flag), so only an explicit
                    # Require of the flag marks them as serving the blocked state.
                    core = role in SCENE_KEYS and not (inline and not (req & own_flags))
                    held = (req | (detected if core else set())) & own_flags
                    held -= set(o.get("forbids") or [])
                    if held and not device and not (req & returned):
                        out.append(("BLOCKED", where, "blocked by own unavailable flag %s: set trickster_device: true (and a trickster_access entry detecting it)" % sorted(held)))
                    if device:
                        if not access:
                            out.append(("FATAL", where, "trickster_device without a trickster_access map"))
                        state_name = o.get("trickster_state") or o.get("TricksterState")
                        if state_name and state_name not in access:
                            out.append(("FATAL", where, "trickster_state %r is not a trickster_access key %s" % (state_name, sorted(access))))
                        if not ({"trickster", "trickster.ever"} & req):
                            out.append(("FATAL", where, "trickster_device must require 'trickster' or 'trickster.ever'"))
                        sets = set(o.get("sets") or []) | {f for ch in chs for f in ch.get("sets") or []}
                        if not any(f in returned or ".trickster.primed" in f or ".trickster.returned" in f or ".trickster.cost." in f for f in sets):
                            out.append(("FATAL", where, "trickster_device sets no returned / .trickster.primed / .trickster.cost. flag"))
                        if held:
                            ignored = set()
                            for k, a in access.items():
                                if isinstance(a, dict) and (not state_name or k == state_name):
                                    ignored |= set(a.get("detect") or [])
                            if held - ignored:
                                out.append(("BLOCKED", where, "trickster_device does not ignore %s: no trickster_access detect lists it" % sorted(held - ignored)))
                elif device:
                    out.append(("FATAL", where, "trickster_device on an epilogue page"))
                # Nurah physical scenes need the hub, an explicit-list device or a presence hub
                hub = o.get("interaction_hub") or o.get("InteractionHub")
                if rel == "nurah" and not remote and not epilogue and not (device and lists) and not (hub and rv.presence_relationship(str(hub))):
                    out.append(("FATAL", where, "physical Nurah scene outside the arrival hub must be a trickster_device on explicit answer_lists"))
                # Attachment point (mirrors Rules.EntryTargets): a physical, non-continuation scene needs explicit answer
                # lists or a recognised hub, else Rules.Validate throws "No dialogue attachment points" (whole mod FATAL).
                cont = o.get("continue_before") or o.get("ContinueBefore")
                if not remote and not epilogue and not cont:
                    if hub:
                        if hub == "nurah.arrival":
                            pass
                        elif rv.presence_relationship(str(hub)) is None:
                            out.append(("FATAL", where, "interaction_hub %r is neither nurah.arrival nor a presence key" % hub))
                        elif lists or inline or truthy(o, "return_to_list", "ReturnToList"):
                            out.append(("FATAL", where, "presence-hub scene %s must have no answer_lists, native_return_cue or return_to_list" % hub))
                        elif (hub_presences.get(hub) or {}).get("Dialog") != "hub":
                            out.append(("FATAL", where, "interaction_hub %s names no presence of this character with Dialog: \"hub\"" % hub))
                    elif not lists and not (rel == "tirabade" and o.get("owner") in ("Anevia", "Irabeth", "Together")):
                        out.append(("FATAL", where, "physical scene with no attachment point: add answer_lists or an E12c interaction_hub"))
                    # Anchor hosting: a scene whose only lists belong to a native NPC who can vanish is a dead route.
                    if lists:
                        hosts = [anchors.get(g) for g in lists]
                        if all(h and h.get("hidden_by") for h in hosts):
                            out.append(("ROUTE", where, "every answer list is a conditional anchor (%s); add a list or hub that survives it"
                                        % ", ".join(sorted({h["name"] for h in hosts}))))
                        elif any(h and h.get("fallback_only") for h in hosts) and not device:
                            out.append(("WARN", where, "hosted on anchor list %s (fallback only): prefer an E12c hub" % ", ".join(
                                sorted({h["name"] for h in hosts if h and h.get("fallback_only")}))))
                # E14b return-to-list scenes
                if truthy(o, "return_to_list", "ReturnToList"):
                    if inline or o.get("contact_unit") or remote or epilogue or not lists or len(set(lists)) != len(lists) or hub:
                        out.append(("FATAL", where, "return_to_list needs a physical scene with explicit distinct answer_lists and no native_return_cue, contact_unit or hub"))
                    rt = o.get("return_text") or o.get("ReturnText") or ""
                    if len(str(rt).split()) > 25:
                        out.append(("FATAL", where, "return_text is longer than 25 words"))
                    if any(ch.get("native_next") or ch.get("check") or ch.get("revive") for ch in chs) or o.get("native_next"):
                        out.append(("FATAL", where, "return_to_list choices cannot use native_next, check or revive"))
                    for g in lists:
                        t = ar.type(g) if GUID.match(str(g)) else None
                        if t != "BlueprintAnswersList":
                            out.append(("DEGRADES", where, "return_to_list list %s is %s, not a BlueprintAnswersList" % (g, t or "missing")))
                elif (o.get("return_text") or o.get("ReturnText")):
                    out.append(("FATAL", where, "return_text without return_to_list"))
                # E14a placement / ER-3 / E14h anchors
                seq = o.get("epilogue_sequence") or o.get("EpilogueSequence")
                after = o.get("epilogue_after") or o.get("EpilogueAfter")
                if isinstance(after, str) and after.lower().startswith("none"): after = None
                if seq is not None:
                    allowed = ("fb42f8bd123bf1f40a448f6dbc66cbbe", "8f234537d0e0e504ba7fa281f02a3601")
                    if seq != "PlayerFinalChoice" or not epilogue or str(o.get("owner") or "") == "AeonEpilogue" \
                            or not after or (after not in allowed and not str(after).startswith("scene:")):
                        out.append(("FATAL", where, "epilogue_sequence must be PlayerFinalChoice on a non-Aeon epilogue page, after BookPage_0147 or BookPage_0115 (or scene:<id>)"))
                if after and not str(after).startswith("scene:"):
                    if not epilogue or not GUID.match(str(after)):
                        out.append(("FATAL", where, "epilogue_after %r needs an epilogue page and a native page/cue GUID or scene:<id>" % after))
                    elif ar.type(after) not in ("BlueprintCue", "BlueprintBookPage", "BlueprintCueSequence", "BlueprintCheck"):
                        out.append(("GATE", where, "epilogue_after %s is %s, not a cue or page" % (after[:8], ar.type(after) or "missing")))
        # E12 / E12b / E12c presences
        pres = {}
        for key in ("presences", "presences_add"):
            v = c.get(key)
            if isinstance(v, dict): pres.update({k: x for k, x in v.items() if isinstance(x, dict)})
        v = c.get("presence")
        if isinstance(v, dict) and v.get("key"): pres[v["key"]] = v
        for key, p in pres.items():
            where = "presence " + key
            mode = p.get("Mode", "reuse-native")
            at = p.get("At") or p.get("at")
            prel = rv.presence_relationship(key)
            if prel is None or not re.fullmatch(r"[a-z0-9_]+", key.split(".presence")[-1].lstrip(".") or "x"):
                out.append(("FATAL", where, "presence key must be <relationship>.presence or <relationship>.presence.<name>"))
            elif prel not in rids:
                out.append(("FATAL", where, "presence key names relationship %r, not this character's %s" % (prel, rids)))
            if mode not in ("reuse-native", "spawn-copy"):
                out.append(("FATAL", where, "Mode must be reuse-native or spawn-copy"))
            if mode == "spawn-copy" and (not (p.get("Position") or at) or not p.get("Requires")):
                out.append(("FATAL", where, "spawn-copy needs Position or At, and non-empty Requires"))
            if isinstance(p.get("Position"), dict) and not all(isinstance(p["Position"].get(k), (int, float)) for k in ("X", "Y", "Z")):
                out.append(("FATAL", where, "Position needs numeric X, Y, Z (use At for an anchor)"))
            for field, want in (("Unit", "BlueprintUnit"), ("Area", "BlueprintArea")):
                g = p.get(field)
                t = ar.type(g) if GUID.match(str(g or "")) else None
                if not t or not t.startswith(want):
                    out.append(("DEGRADES", where, "%s %s is %s, not a %s" % (field, g, t or "missing", want)))
            for g in p.get("AnswerLists") or []:
                if ar.type(g) != "BlueprintAnswersList":
                    out.append(("DEGRADES", where, "answer list %s is %s" % (g, ar.type(g) or "missing")))
            if at is not None:
                near, loc = at.get("NearUnit"), at.get("Locator")
                if (near is None) == (loc is None):
                    out.append(("FATAL", where, "At needs exactly one of NearUnit or Locator"))
                elif near is not None and ar.type(near) != "BlueprintUnit":
                    out.append(("DEGRADES", where, "At.NearUnit %s is %s, not a BlueprintUnit (presence disabled)" % (near, ar.type(near) or "missing")))
                if at.get("Side") not in (None, "left", "right", "front", "behind") or (at.get("Offset") is not None and len(at["Offset"]) != 2):
                    out.append(("FATAL", where, "At.Side must be left/right/front/behind, or Offset [dx, dz]"))
            for other_key, q in pres.items():
                if other_key <= key or q.get("Unit") != p.get("Unit") or q.get("Area") != p.get("Area"): continue
                a_req, a_forb = set(p.get("Requires") or []), set(p.get("Forbids") or [])
                b_req, b_forb = set(q.get("Requires") or []), set(q.get("Forbids") or [])
                a_lo, a_hi = p.get("MinChapter", 1), p.get("MaxChapter", 6)
                b_lo, b_hi = q.get("MinChapter", 1), q.get("MaxChapter", 6)
                a_groups = [set(g) for g in p.get("RequiresAnyGroups") or []]
                b_groups = [set(g) for g in q.get("RequiresAnyGroups") or []]
                if not (a_req & b_forb or b_req & a_forb or a_hi < b_lo or b_hi < a_lo
                        or any(g <= b_forb for g in a_groups) or any(g <= a_forb for g in b_groups)):
                    out.append(("FATAL", where, "shares unit and area with %s but they are not mutually exclusive (Requires/Forbids or chapters)" % other_key))
            if p.get("Dialog") not in (None, "hub"):
                out.append(("FATAL", where, "Dialog must be \"hub\" (E12c)"))
        results[name] = out
    return results


SEVERITY_ORDER = {"FATAL": 0, "DEGRADES": 1, "BLOCKED": 2, "GATE": 3, "ROUTE": 4, "TEST": 5, "WARN": 6}
FAILING = ("FATAL", "DEGRADES", "BLOCKED", "GATE", "ROUTE", "TEST")


def print_rules(results, quiet=False, file=sys.stdout):
    P = lambda *a: print(*a, file=file)
    P("# matrix_check --rules: runtime rules (Rules.Validate / Main.Build), rules_test execution and authoring lints")
    P("#   FATAL    Rules.Validate throws: the WHOLE MOD is disabled")
    P("#   DEGRADES Main.Build disables the relationship, or a gate cannot mean what was written (singleton requires_any_groups)")
    P("#   BLOCKED  the scene can never be available (its relationship's own unavailable flag blocks it)")
    P("#   GATE     the build gate (rrt_verify --strict section F) fails")
    P("#   ROUTE    the relationship cannot commit (nothing sets its CommittedFlag)")
    P("#   TEST     a state's rules_test fails when executed (world -> expect_* / after_choice -> expect_flags / commit reachable)")
    P("#   WARN     reported, not failing (delay anchored on unstamped native keys, scene/choice sets contradictions, textless nodes)")
    if not quiet:
        for name, out in results.items():
            if not out: continue
            P("\n== %s: %d finding(s)" % (name, len(out)))
            for sev, where, msg in sorted(out, key=lambda x: (SEVERITY_ORDER[x[0]], x[1])):
                P("   %-8s %s\n            %s" % (sev, where, msg))
    keys = list(SEVERITY_ORDER)
    P("\n%-24s " % "character" + " ".join("%8s" % k for k in keys) + " %8s" % "failing")
    P("-" * (25 + 9 * (len(keys) + 1)))
    tot = dict.fromkeys(keys, 0)
    for name, out in results.items():
        n = {k: sum(1 for x in out if x[0] == k) for k in keys}
        for k in keys: tot[k] += n[k]
        P("%-24s " % name[:24] + " ".join("%8d" % n[k] for k in keys) + " %8d" % sum(n[k] for k in FAILING))
    P("-" * (25 + 9 * (len(keys) + 1)))
    P("%-24s " % "TOTAL" + " ".join("%8d" % tot[k] for k in keys) + " %8d" % sum(tot[k] for k in FAILING))
    return sum(tot[k] for k in FAILING)


# ------------------------------------------------------------------------------ compile the matrix into a Story
BINDING_SECTIONS = {"Etudes": "Etudes", "CompletedEtudes": "CompletedEtudes", "CompletedQuests": "CompletedQuests",
                    "SeenCues": "SeenCues", "SelectedAnswers": "SelectedAnswers", "StartedDialogs": "StartedDialogs",
                    "UnlockableFlags": "UnlockableFlags", "QuestObjectives": "QuestObjectives",
                    "InventoryItems": "InventoryItems", "StartedQuests": "StartedQuests", "Quests(started)": "StartedQuests",
                    "MainCharacterFacts": "MainCharacterFacts"}


def rel_ids(c):
    return re.findall(r"[a-z][a-z0-9_]*(?:\.[a-z0-9_]+)*", (c.get("relationship_id") or "").split("(renamed")[0])


def committed_flag(story, rid):
    return ((story.get("Relationships") or {}).get(rid) or {}).get("CommittedFlag") or rid + ".committed"


def scene_sets(o):
    return [f for f in (o.get("sets") or []) if isinstance(f, str)]


def compile_story(matrix, story):
    """Story.json + every matrix scene object, as a Story dict the rrt_verify model understands.
    A matrix scene replaces a Story.json scene with the same id (the spec is what is being tested)."""
    out = json.loads(json.dumps(story or {}))
    out.setdefault("Scenes", [])
    rels = out.setdefault("Relationships", {})
    sections = set(BINDING_SECTIONS.values())
    for k, b in (matrix.get("bindings") or {}).items():
        sec = BINDING_SECTIONS.get(b.get("kind"))
        if not sec or not b.get("guid") or any(k in (out.get(x) or {}) for x in sections): continue
        if sec == "SeenCues": out.setdefault(sec, {})[k] = [b["guid"]]
        elif sec == "QuestObjectives": out.setdefault(sec, {})[k] = [b["guid"], b.get("state", "Completed")]
        else: out.setdefault(sec, {})[k] = b["guid"]
    out.setdefault("Derived", {})
    out.setdefault("Latches", {})
    for k, v in (matrix.get("derived") or {}).items(): out["Derived"].setdefault(k, v)
    for k, v in (matrix.get("latches") or {}).items(): out["Latches"].setdefault(k, v)
    matrix_ids = set()
    compiled = []
    for c in matrix.get("characters", []):
        rids = rel_ids(c)
        if not rids: continue
        own = rids[0]
        r = rels.setdefault(own, dict(Title=c.get("character", own), StartedFlag=own + ".started", ClosedFlag=own + ".closed",
                                      CommittedFlag=own + ".committed", UnavailableFlags=[], FailureFlags=[]))
        r["UnavailableFlags"] = sorted(set(r.get("UnavailableFlags") or []) | set(c.get("unavailable_overrides") or {})
                                       | set(c.get("unavailable_flags") or []))
        r["UnavailableOverrides"] = dict(r.get("UnavailableOverrides") or {}, **(c.get("unavailable_overrides") or {}))
        r["TricksterAccess"] = {k: dict(Detect=a.get("detect", []), Device=a.get("device"), Returned=a.get("returned"))
                                for k, a in (c.get("trickster_access") or {}).items() if isinstance(a, dict)}
        for st in c.get("states") or []:
            for role, o in scene_objects(st):
                if o["id"] in matrix_ids: continue
                matrix_ids.add(o["id"])
                kind = o.get("kind") or ("remote" if o.get("remote") else "physical")
                owner = o.get("owner") or ("Epilogue" if kind == "epilogue" else "Memory" if kind == "remote" else c.get("character", "Narrator"))
                base = scene_sets(o)
                compiled_choices = []
                for ch in choices(o) or [{}]:
                    compiled_choices.append(dict(Text=ch.get("text") or ch.get("prefix") or "Continue", Next=None,
                                                 Set=sorted(set(base) | set(f for f in ch.get("sets") or [] if isinstance(f, str))),
                                                 Requires=[f for f in ch.get("requires") or [] if isinstance(f, str)],
                                                 Forbids=[f for f in ch.get("forbids") or [] if isinstance(f, str)],
                                                 Abort=bool(ch.get("abort")) and not ch.get("sets")))
                groups = [g if isinstance(g, list) else [g] for g in o.get("requires_any_groups") or []]
                compiled.append(dict(Id=o["id"], Title=o["id"], Owner=owner, Relationship=o.get("relationship") or own,
                                     MinChapter=o.get("min_chapter") if isinstance(o.get("min_chapter"), int) else 1,
                                     MaxChapter=o.get("max_chapter") if isinstance(o.get("max_chapter"), int) else 6,
                                     Chapters=[x for x in o.get("chapters") or [] if isinstance(x, int)],
                                     DelayHours=o.get("delay_hours") if isinstance(o.get("delay_hours"), int) else 0,
                                     Remote=kind == "remote", AnswerLists=[g for g in o.get("answer_lists") or [] if isinstance(g, str)],
                                     ContactUnit=o.get("contact_unit"), NativeReturnCue=o.get("native_return_cue"),
                                     Requires=[f for f in o.get("requires") or [] if isinstance(f, str)],
                                     RequiresAny=[f for f in o.get("requires_any") or [] if isinstance(f, str)],
                                     RequiresAnyGroups=groups,
                                     Forbids=[f for f in o.get("forbids") or [] if isinstance(f, str)],
                                     ForbidOverrides=dict(o.get("forbid_overrides") or {}),
                                     TricksterDevice=truthy(o, "trickster_device", "TricksterDevice", "tricksterdevice"),
                                     TricksterState=o.get("trickster_state"), Recovery=None,
                                     Nodes=[dict(Id="start", Speaker="Narrator", Text="x", Choices=compiled_choices)]))
    out["Scenes"] = [s for s in out["Scenes"] if s["Id"] not in matrix_ids] + compiled
    for rid in {s.get("Relationship", "tirabade") for s in out["Scenes"]}:
        rels.setdefault(rid, dict(Title=rid, StartedFlag=rid + ".started", ClosedFlag=rid + ".closed", CommittedFlag=rid + ".committed"))
    return out


def gate_reasons(model, s, st, chapter_known):
    """Why a scene is unavailable (gates only: no delay, contact or area). Empty list = available."""
    why = []
    if s["Id"] in st.flags: why.append("already completed")
    if chapter_known and (st.chapter < s["MinChapter"] or st.chapter > s["MaxChapter"] or (s["Chapters"] and st.chapter not in s["Chapters"])):
        why.append("chapter %d outside %s" % (st.chapter, s["Chapters"] or "%d-%d" % (s["MinChapter"], s["MaxChapter"])))
    why += ["requires %s unset" % f for f in s["Requires"] if f not in st.flags]
    for f in s["Forbids"]:
        ov = s["ForbidOverrides"].get(f)
        if f in st.flags and not (ov and ov in st.flags): why.append("forbids %s" % f)
    if s["RequiresAny"] and not any(f in st.flags for f in s["RequiresAny"]): why.append("needs any of %s" % s["RequiresAny"])
    for g in s["RequiresAnyGroups"]:
        if not any(f in st.flags for f in g): why.append("requires_any_groups %s unmet (groups are ANDed)" % g)
    if rv.is_epilogue(s): return why
    rel = model.rels.get(s["Relationship"], {})
    if rel.get("ClosedFlag") in st.flags and s["AfterRecovery"] is None: why.append("relationship closed (%s)" % rel["ClosedFlag"])
    detects = rv.device_detects(rel, s) if s["TricksterDevice"] else set()
    for f in rel.get("UnavailableFlags", []):
        ov = (rel.get("UnavailableOverrides") or {}).get(f)
        if f in st.flags and not (ov and ov in st.flags) and f not in detects:
            why.append("blocked by unavailable flag %s%s" % (f, "" if s["TricksterDevice"] else " (not a trickster_device)"))
    return why


def parse_world(tokens):
    flags, chapter = set(), None
    for t in tokens or []:
        if not isinstance(t, str): continue
        m = re.match(r"^chapter\s*[:=]\s*(\d+)$", t)
        if m: chapter = int(m.group(1)); continue
        if re.match(r"^(area|hour|hours_since)", t) or ">" in t or "<" in t: continue
        if t.startswith("!") or t.startswith("-"): flags.discard(t[1:]); continue
        flags.add(t)
    return flags, chapter


FLAG = re.compile(r"^[a-z][A-Za-z0-9_.]*$")


def run_rules_tests(matrix, story):
    """{character: [(severity, where, message)]} for rules_test execution, commit producers and authoring lints."""
    compiled = compile_story(matrix, story)
    model = rv.Model(compiled)
    results = {}
    for c in matrix.get("characters", []):
        out = []
        name = c.get("character", "?")
        rids = rel_ids(c)
        if not rids:
            results[name] = out
            continue
        commit = committed_flag(compiled, rids[0])
        if not model.producers.get(commit):
            out.append(("ROUTE", "character", "no commit producer: no scene or choice sets %s" % commit))
        for st in c.get("states") or []:
            for role, o in scene_objects(st):
                where = "%s/%s %s" % (st.get("state"), role, o["id"])
                groups = o.get("requires_any_groups") or []
                singles = [g for g in groups if isinstance(g, list) and len(g) == 1]
                if len(singles) >= 2:
                    out.append(("DEGRADES", where, "requires_any_groups %s: %d singleton groups are ANDed (likely OR written as AND; use [[%s]])"
                                % (groups, len(singles), ", ".join(str(g[0]) for g in singles))))
                s = model.by_id.get(o["id"])
                if s and s["DelayHours"] > 0:
                    anchors = list(s["Requires"]) + [f for g in s["RequiresAnyGroups"] for f in g]
                    if not [f for f in anchors if f in model.authored or f in model.latches]:
                        out.append(("WARN", where, "delay_hours %d is anchored only on native/derived keys %s (no hour. stamp): effectively 0 h"
                                    % (s["DelayHours"], anchors or "[]")))
                base = set(scene_sets(o))
                chs = choices(o)
                own_sets = [set(f for f in ch.get("sets") or [] if isinstance(f, str)) for ch in chs]
                if base and len(chs) >= 2 and any(own_sets) and len({frozenset(x) for x in own_sets}) > 1:
                    out.append(("WARN", where, "scene-level sets %s apply to every terminal choice, but the choices set different flags %s"
                                % (sorted(base), [sorted(x) for x in own_sets])))
                for ch in chs:
                    clash = base & set(f for f in ch.get("forbids") or [] if isinstance(f, str))
                    if clash: out.append(("WARN", where, "scene-level sets %s but a choice forbids them" % sorted(clash)))
                nodes = o.get("nodes")
                ids = set(nodes) if isinstance(nodes, dict) else set()
                for ch in chs:
                    for key in ("next", "node"):
                        ref = ch.get(key)
                        if isinstance(ref, str) and ids and re.match(r"^[a-z_][a-z0-9_]*$", ref) \
                                and (ref not in ids or not str(nodes.get(ref) or "").strip(" .[]")):
                            out.append(("WARN", where, "choice %s %r references a node with no text" % (key, ref)))
            for key in ("rules_test", "rules_tests_extra", "additional_rules_tests", "extra_rules_tests", "rules_test_extra"):
                v = st.get(key)
                for t in (v if isinstance(v, list) else [v]):
                    if isinstance(t, dict) and t.get("world") is not None:
                        out += execute_test(model, t, "%s/%s" % (st.get("state"), t.get("name", key)))
        results[name] = out
    return results


def execute_test(model, t, where):
    out = []
    flags, chapter = parse_world(t.get("world"))
    state = rv.SimState(1 if chapter is None else chapter, 100000)   # "chapter:0" is the Prologue (E-new 0)
    state.flags = set(flags)
    rv.sim_complete(model, state)

    def check_scene(sid, expect, label):
        s = model.by_id.get(sid)
        if s is None:
            out.append(("TEST", where, "%s: scene %s is not defined in the matrix or Story.json" % (label, sid)))
            return
        if chapter is None: state.chapter = s["MinChapter"]
        why = gate_reasons(model, s, state, chapter is not None)
        if expect and why: out.append(("TEST", where, "%s: %s blocked by: %s" % (label, sid, "; ".join(why))))
        if not expect and not why: out.append(("TEST", where, "%s: %s is available but expected unavailable" % (label, sid)))

    for sid in t.get("expect_available") or []:
        if isinstance(sid, str): check_scene(sid, True, "expect_available")
    for sid in t.get("expect_unavailable") or []:
        if isinstance(sid, str): check_scene(sid, False, "expect_unavailable")
    ac = t.get("after_choice")
    if isinstance(ac, dict) and ac.get("scene"):
        s = model.by_id.get(ac["scene"])
        idx = ac.get("choice", 0)
        chs = s["Nodes"][0]["Choices"] if s else []
        if s is None:
            out.append(("TEST", where, "after_choice: scene %s is not defined" % ac["scene"]))
        elif not isinstance(idx, int) or not 0 <= idx < len(chs):
            out.append(("TEST", where, "after_choice: %s has no choice %r (%d choices in the matrix)" % (ac["scene"], idx, len(chs))))
        else:
            ch = chs[idx]
            miss = ["requires " + f for f in ch["Requires"] if f not in state.flags] + ["forbids " + f for f in ch["Forbids"] if f in state.flags]
            if miss: out.append(("TEST", where, "after_choice: choice %d of %s is not selectable: %s" % (idx, ac["scene"], ", ".join(miss))))
            state.flags |= set(ch["Set"]) | ({s["Id"]} if not ch["Abort"] else set())
            state.flags |= set(f for f in ac.get("world_add") or [] if isinstance(f, str))
            rv.sim_complete(model, state)
    for f in t.get("expect_flags") or []:
        if isinstance(f, str) and FLAG.match(f) and f not in state.flags:
            out.append(("TEST", where, "expect_flags: %s not set after the choice" % f))
    for f in t.get("expect_not_flags") or []:
        if isinstance(f, str) and f in state.flags:
            out.append(("TEST", where, "expect_not_flags: %s is set" % f))
    for key, expect in (("then_available", True), ("expect_available_after", True), ("then_unavailable", False), ("expect_unavailable_after", False)):
        for sid in t.get(key) or []:
            if isinstance(sid, str): check_scene(sid, expect, key)
    commit = t.get("committed_flag_reachable")
    if isinstance(commit, str) and FLAG.match(commit):
        natives = {f for f in state.flags if f in model.native}
        authored = sorted(f for f in state.flags if f not in model.native)
        story = model.story
        seed = dict(Id="__rules_test_world__", Title="w", Owner="Memory", Remote=True, MinChapter=1, MaxChapter=6,
                    Relationship="__rules_test_world__",
                    Nodes=[dict(Id="start", Text="x", Choices=[dict(Text="c", Set=authored)])])
        rels = dict(story.get("Relationships") or {}, __rules_test_world__=dict(
            Title="w", StartedFlag="__w.started", ClosedFlag="__w.closed", CommittedFlag="__w.committed"))
        m2 = rv.Model(dict(story, Scenes=story["Scenes"] + [seed], Relationships=rels))
        world = rv.mythic_world("trickster", m2, "test", true=natives) if ("trickster" in state.flags or "trickster.ever" in state.flags) \
            else rv.World("test", true=natives)
        if commit not in rv.Reach(m2, world).held:
            out.append(("TEST", where, "committed_flag_reachable: %s is not reachable from this world (no reachable scene sets it)" % commit))
    return out

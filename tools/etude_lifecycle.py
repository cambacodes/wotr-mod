#!/usr/bin/env python3
"""etude_lifecycle.py - native etude lifecycle table and the "Playing-only etude read out of its window" gate.

Main.BuildState reads a Story.Etudes binding as held only while the etude IsPlaying (PermanentEtudes and the _dead/_gone/
ascend_/sacrifice/true_lich suffix rule also read Completed). A native etude can stop Playing without its event being
undone (Writer/handoffs/18-ETUDE-BINDING-AUDIT.md):
  area         it (or an ancestor) is linked to an area part: dormant everywhere else;
  cascade      a ChapterNN ancestor is completed at the interchapter: every started child reads Completed from chapter NN+1;
  conditional  it (or an ancestor) has an ActivationCondition (e.g. SeelahInParty): dormant while the condition fails;
  never_reads  (audit ruling) it can never read as the event the key names.
So a Playing-only binding used where only its history can hold (a remote letter, a relationship's UnavailableFlags or
TricksterAccess detect, a Derived composite, a scene in another area or a later chapter) is a HARD failure. The fix is
data: a latch (recorded where the etude plays), PermanentEtudes (a cascade), or a better native signal (SeenCues...).

  python tools/etude_lifecycle.py [--story development/Story.json] [--game DIR]   # regenerate tools/etude-lifecycle.json

rrt_verify imports check() (section E3) and unreadable() (its reachability model), reading the checked-in JSON only.
"""
import argparse, json, os, re, sys, zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TABLE = HERE / "etude-lifecycle.json"
GAME = Path(os.environ.get("RRT_GAME_DIR") or r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure")
CHAPTER = re.compile(r"^Chapter0(\d)$")
SUFFIX_PERMANENT = ("_dead", "_gone")

# Audit rulings (18-ETUDE-BINDING-AUDIT section 3.2 triage), keyed by etude GUID. "reviewed" = the Playing-only read is the
# intended current-state meaning where it is used (reported, never failing); "never_reads" = the etude cannot read as the
# event its key names anywhere (a HARD failure wherever it is bound as Etudes).
RULINGS = {
    "543a6e475aeb9bf4eafb43903e3e186b": ("never_reads", "ArueshalaeRomance_Fail is the one-strike warning; the second strike "
                                         "completes ArueshalaeRomance in the same dialog, so it never reads 'failed'"),
    "6d3fb96f9b60c0449a01add4be5c4a49": ("reviewed", "VictimsRevived: live-intended; native Arsinoe_Dialogue_Conditions gates her own "
                                         "dialogue on NOT Playing, and she is in the Temple (its area) while it plays"),
    "10f5e03534e6fe74fbc8a94dc2e2c15c": ("reviewed", "FoolKingGone: every use is a Chapter 5 King's-list or capital-area scene, where "
                                         "it plays (area DrezenCapital, Chapter05 playing, Trickster lost)"),
    "260454e5186fbd34694a0393097f77b5": ("reviewed", "IrabethNotInDrezenCh5_WithGalfrey: live-intended (away now); the Coronation "
                                         "completion means she is back; users are capital scenes or Anevia's capital contact"),
    "baa4820ac052d664bbaa261d17ce9b08": ("reviewed", "Marhevok rules: current leadership is the intended meaning ('while Marhevok rules')"),
    "89f8c2f1a7a8ea24794bf4af231e89a1": ("reviewed", "CamelliaRomance: current romance is the intended meaning (dance branch)"),
    # Found by this gate beyond the audit's list, reviewed 2026-09-30:
    "806ece7bcf18a374e9ad1f7b9e3bc580": ("reviewed", "ChivarroWasTeleportedAway: only an OR branch beside the stable chivarro.removed, "
                                         "which the same cue starts"),
    "20927a9471c00814b808fd69e88879c7": ("reviewed", "Nurah's killing mechanism: every use sits beside its stable parent nurah.dead_drezen "
                                  "(UnavailableFlags, the same Forbids list or RequiresAnyGroup)"),
    "b5f301fbc4c44535a6309d610d5bd28a": ("reviewed", "Konomi's office: the out-of-capital use is konomi.private_absence, which Requires "
                                         "konomi.private_departed (she has left the office), so a false read there is the true state"),
}


# ------------------------------------------------------------------------------------------------ generation
def _index(game):
    """Every BlueprintEtude (parent, linked area, activation condition) and every StartEtude/CompleteEtude target."""
    etudes, names, completes = {}, {}, {}
    with zipfile.ZipFile(Path(game) / "blueprints.zip") as z:
        for n in z.namelist():
            if not n.endswith(".jbp"):
                continue
            raw = z.read(n)
            is_etude = b"BlueprintEtude\"" in raw[:400] or b", BlueprintEtude" in raw[:400]
            if not is_etude and b"CompleteEtude" not in raw:
                continue
            try:
                d = json.loads(raw.decode("utf-8-sig"))
            except ValueError:
                continue
            g, data = d.get("AssetId"), d.get("Data") or {}
            names[g] = n
            if str(data.get("$type", "")).endswith(", BlueprintEtude"):
                act = (data.get("ActivationCondition") or {}).get("Conditions") or []
                etudes[g] = dict(parent=(data.get("m_Parent") or "")[4:] or None,
                                 area=(data.get("m_LinkedAreaPart") or "")[4:] or None,
                                 conditional=[c.get("$type", "").split(", ")[-1] for c in act if c])
            if b"CompleteEtude" in raw:
                for m in re.finditer(r'CompleteEtude"[^{}]*?"Etude": "!bp_([0-9a-f]{32})"', raw.decode("utf-8-sig")):
                    completes.setdefault(m.group(1), []).append(n)
    return etudes, names, completes


def _name(names, g):
    return Path(names.get(g, g)).stem


def build(story, game=GAME):
    etudes, names, completes = _index(game)
    guids = {}
    for sec in ("Etudes", "CompletedEtudes"):
        for key, g in (story.get(sec) or {}).items():
            guids.setdefault(g, []).append(key)
    out = {}
    for g in sorted(guids):
        if g not in etudes:
            out[g] = dict(name="(parent mod / not in blueprints.zip)", traits=["parent_mod"], chain=[], areas={},
                          conditional=[], completed_by=[], cascade_chapter=None)
            continue
        chain, areas, conditional, cascade, cascade_chapter, x = [], {}, [], [], None, g
        while x and x in etudes:
            e = etudes[x]
            chain.append(_name(names, x))
            if e["area"]:
                areas[e["area"]] = _name(names, e["area"])
            if e["conditional"]:
                conditional.append("%s: %s" % (_name(names, x), ", ".join(sorted(set(e["conditional"])))))
            if x != g and completes.get(x):
                cascade.append(_name(names, x))
                m = CHAPTER.match(_name(names, x))
                if m and cascade_chapter is None:
                    cascade_chapter = int(m.group(1)) + 1
            x = e["parent"]
        traits = (["area"] if areas else []) + (["cascade"] if cascade_chapter else []) + \
                 (["conditional"] if conditional else []) + (["self_completed"] if completes.get(g) else []) + \
                 (["event_cascade"] if cascade and not cascade_chapter else [])
        out[g] = dict(name=chain[0], chain=chain, areas=areas, conditional=conditional,
                      completed_by=sorted({Path(p).stem for p in completes.get(g, [])})[:8],
                      ancestors_completed=cascade, cascade_chapter=cascade_chapter, traits=traits or ["hold"])
    for g, (kind, note) in RULINGS.items():
        if g in out:
            out[g]["ruling"], out[g]["note"] = kind, note
    return out


# ------------------------------------------------------------------------------------------------ uses and gate
def _chapters(s):
    if s.get("Chapters"):
        return sorted(set(s["Chapters"]))
    return list(range(int(s.get("MinChapter", 1)), int(s.get("MaxChapter", 5)) + 1))


def contexts(story):
    """key -> list of use contexts: {kind, where, chapters, areas, remote, lists}."""
    uses = {}

    def add(key, **ctx):
        uses.setdefault(key.lstrip("!"), []).append(ctx)

    for s in story.get("Scenes", []):
        epi = str(s.get("Owner", "")).endswith("Epilogue")
        ctx = dict(kind="epilogue" if epi else "scene", where=s["Id"], chapters=[6] if epi else _chapters(s),
                   areas=list(s.get("Areas") or []), remote=bool(s.get("Remote")) or s.get("Owner") == "Memory" or epi,
                   lists=bool(s.get("AnswerLists")) or bool(s.get("ContactUnit")))
        keys = list(s.get("Requires") or []) + list(s.get("Forbids") or []) + list(s.get("RequiresAny") or [])
        keys += [k for grp in s.get("RequiresAnyGroups") or [] for k in grp] + list((s.get("ForbidOverrides") or {}).values())
        for n in s.get("Nodes") or []:
            for c in n.get("Choices") or []:
                keys += list(c.get("Requires") or []) + list(c.get("Forbids") or [])
            for p in n.get("Paragraphs") or []:
                keys += list(p.get("Requires") or []) + list(p.get("Forbids") or []) + [k for grp in p.get("AnyGroups") or [] for k in grp]
        for k in set(keys):
            add(k, **ctx)
    anywhere = dict(chapters=list(range(1, 7)), areas=[], remote=True, lists=False)
    for rk, r in (story.get("Relationships") or {}).items():
        for k in r.get("UnavailableFlags") or []:
            add(k, kind="relationship", where=rk + ".UnavailableFlags", **anywhere)
        for st, a in (r.get("TricksterAccess") or {}).items():
            for k in (a.get("Detect") or a.get("detect") or []):
                # Runtime: a device scene ignores these unavailable flags (ER-2); not a gate read, so never HARD.
                add(k, kind="detect", where="%s.TricksterAccess.%s" % (rk, st), **anywhere)
    for dk, groups in (story.get("Derived") or {}).items():
        for k in {k for g in groups for k in g}:
            add(k, kind="derived", where="Derived." + dk, **anywhere)
    for dk, flags in (story.get("DerivedForbids") or {}).items():
        for k in flags:   # engine-q2: a negated Derived input (trickster.now)
            add(k, kind="derived", where="DerivedForbids." + dk, **anywhere)
    for ck, c in (story.get("Counts") or {}).items():
        for k in c.get("Of") or []:
            add(k, kind="derived", where="Counts." + ck, **anywhere)
    for lk, sources in (story.get("Latches") or {}).items():
        for k in sources:
            add(k, kind="latch", where="Latches." + lk, chapters=list(range(1, 7)), areas=[], remote=False, lists=False)
    for pk, p in (story.get("Presences") or {}).items():
        for k in list(p.get("Requires") or []) + list(p.get("Forbids") or []) + [k for g in p.get("RequiresAnyGroups") or [] for k in g]:
            add(k, kind="presence", where="Presences." + pk, chapters=list(range(1, 7)), areas=[], remote=False, lists=True)
    return uses


def engine_permanent(story, key):
    """Main.BuildState: which Etudes keys also read Completed."""
    return (key in (story.get("PermanentEtudes") or []) or key.endswith(SUFFIX_PERMANENT) or key.startswith("ascend_")
            or key in ("sacrifice", "true_lich"))


def verdict(entry, permanent, ctx, chapter=None):
    """(level, reason) for one use: level OK | WARN | HARD. chapter narrows a scene context to one chapter (the Reach model)."""
    if entry is None:
        return "WARN", "unclassified (regenerate tools/etude-lifecycle.json)"
    if entry.get("ruling") == "reviewed":
        return "OK", "reviewed: " + entry.get("note", "")
    if entry.get("ruling") == "never_reads":
        return "HARD", "never reads as its event: " + entry.get("note", "")
    if ctx["kind"] == "latch":
        return "OK", "latch source (recorded where it plays)"
    if ctx["kind"] == "detect":
        if not set(entry.get("traits") or ()) & {"area", "cascade", "conditional"}:
            return "OK", ""
        return "WARN", "TricksterAccess detect of a Playing-only etude (%s): the device's matrix state assumes its history" % "/".join(entry["traits"])
    chapters = [chapter] if chapter else ctx["chapters"]
    cc = entry.get("cascade_chapter")
    if cc and all(c >= cc for c in chapters):
        if permanent:
            return "OK", "Completed by the Chapter%02d cascade; PermanentEtudes reads it" % (cc - 1)
        return "HARD", "Playing-only, but the Chapter%02d cascade completes it before chapter %s" % (cc - 1, "/".join(map(str, chapters)))
    areas = entry.get("areas") or {}
    if areas:
        where = "area %s" % "/".join(sorted(areas.values()))
        if ctx["areas"]:
            if set(ctx["areas"]) <= set(areas):
                return "OK", "delivered in its " + where
            return "HARD", "Playing-only in its %s, delivered in another area" % where
        if ctx["remote"] or ctx["kind"] in ("relationship", "derived", "epilogue"):
            return "HARD", "Playing-only in its %s, read by a %s outside it" % (where, "remote scene" if ctx["kind"] == "scene" else ctx["kind"] + " use")
        return "WARN", "Playing-only in its %s; a native-list/contact scene with no Areas (area unproven)" % where
    if cc and any(c >= cc for c in chapters) and not permanent:
        return "WARN", "Playing-only; the Chapter%02d cascade completes it inside this scene's chapter window" % (cc - 1)
    if entry.get("conditional") and ctx["kind"] in ("relationship", "derived"):
        return "WARN", "dormant while an ActivationCondition fails (%s)" % "; ".join(entry["conditional"][:2])
    return "OK", ""


def check(story, table):
    """Rows for every Etudes/CompletedEtudes binding: key, guid, lifecycle traits, permanence and each non-OK use."""
    uses = contexts(story)
    rows, hard, warn = [], [], []
    for sec in ("Etudes", "CompletedEtudes"):
        for key, g in sorted((story.get(sec) or {}).items()):
            entry = table.get(g)
            permanent = sec == "CompletedEtudes" or engine_permanent(story, key)
            row = dict(key=key, binding=sec, guid=g, name=(entry or {}).get("name"), traits=(entry or {}).get("traits", ["unclassified"]),
                       read="Completed" if sec == "CompletedEtudes" else ("Playing|Completed" if permanent else "Playing"),
                       ruling=(entry or {}).get("ruling"), uses=len(uses.get(key, [])), problems=[])
            if sec == "Etudes":
                for ctx in uses.get(key, []):
                    level, why = verdict(entry, permanent, ctx)
                    if level != "OK":
                        row["problems"].append((level, ctx["where"], why))
                        (hard if level == "HARD" else warn).append("%s @ %s: %s" % (key, ctx["where"], why))
            rows.append(row)
    return rows, hard, warn


def load(path=TABLE):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))["etudes"]
    except (OSError, ValueError, KeyError):
        return None


def unreadable(story, table, key, scene, chapter):
    """Reach model: True when an Etudes key can never read as held for this use (scene None = a relationship-level use)."""
    if table is None or key not in (story.get("Etudes") or {}):
        return False
    entry = table.get(story["Etudes"][key])
    if scene is None:
        ctx = dict(kind="relationship", where="", chapters=list(range(1, 7)), areas=[], remote=True, lists=False)
    else:
        epi = str(scene.get("Owner", "")).endswith("Epilogue")
        ctx = dict(kind="epilogue" if epi else "scene", where=scene["Id"], chapters=_chapters(scene), areas=list(scene.get("Areas") or []),
                   remote=bool(scene.get("Remote")) or scene.get("Owner") == "Memory" or epi,
                   lists=bool(scene.get("AnswerLists")) or bool(scene.get("ContactUnit")))
    return verdict(entry, engine_permanent(story, key), ctx, chapter or None)[0] == "HARD"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--story", default=str(HERE.parent / "development/Story.json"))
    ap.add_argument("--game", default=str(GAME))
    ap.add_argument("--out", default=str(TABLE))
    a = ap.parse_args()
    story = json.loads(Path(a.story).read_text(encoding="utf-8"))
    table = build(story, a.game)
    # Keep GUIDs a previous table classified (bindings retired since stay documented) unless regenerated here.
    old = load(a.out) or {}
    for g, e in old.items():
        table.setdefault(g, e)
    Path(a.out).write_text(json.dumps(dict(source="blueprints.zip + 18-ETUDE-BINDING-AUDIT rulings (tools/etude_lifecycle.py)",
                                           etudes=table), indent=1, sort_keys=True) + "\n", encoding="utf-8")
    rows, hard, warn = check(story, table)
    print("%d etude GUIDs classified -> %s; %d HARD, %d WARN" % (len(table), a.out, len(hard), len(warn)))
    for x in hard:
        print("HARD", x)


if __name__ == "__main__":
    main()

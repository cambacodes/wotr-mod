"""Harem schedule lint (doc 16 section 8c.2): classification, protected schedule and consolidation proofs.

Reads tools/harem-schedule.json (data only; no scene is generated from it) and, when given, development/Story.json.

Checks (each failure is HARD, exit 1; a malformed file is exit 2):
  K1  completeness: every doc 11 section 3 row is classified, expanded per woman (43 rows -> 48 candidates), exactly once,
      in source order. When Writer/handoffs/11-ROSTER-PLAN-2.md is present, its section 3 table must match the snapshot.
  K2  classification: merged/promoted rows name a destination; cordial rows name none; promoted rows exist in `rows`.
  K3  protection: an atrocity/captivity/custody obligation is never cordial and lands on an X row; every protection ref
      resolves to a schedule entry; every promoted row has a schedule entry.
  K4  schedule: orders unique and ascending; Ch5 primary entries are 5.01..5.49 contiguous; every Arueshalae entry needs a
      positive key (unknown state offers none); a recovery waits >= 48 h; counts match `expected_counts`.
  K5  names: every woman is a relationship id or a mapped seat woman; proposed outcome flags never use attitude, strain,
      enmity, tolerated or stance words.
  K6  existing reads: every `reads`/`forbids_existing` key is a scene id, a choice Set flag, a Derived flag or a binding key
      in Story.json (skipped without --story).
  K7  consolidation proofs: an executable rules walk of every packet (P1-P9, P11), exhaustive over attendance and child
      outcome states, plus the rejected-packet rules. P10 and P12-P14 are integration acceptance and are listed only.
"""
import argparse
import itertools
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "tools" / "harem-schedule.json"
DEFAULT_DOC11 = ROOT.parent / "Writer" / "handoffs" / "11-ROSTER-PLAN-2.md"
ARUE_KEYS = ("arueshalae.redeemed", "arueshalae.corrupted")
BANNED_OUTCOME_WORDS = ("attitude", "strain", "enmity", "tolerated", "stance")
OBLIGATIONS = ("atrocity", "captivity", "custody")
PROTECTED_PREFIX = "household.protected."


def load_json(path):
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


# --- the proposed docket flags (unimplemented; names only) -------------------------------------------------------------

def outcome_flags(ref):
    base = PROTECTED_PREFIX + ref.lower()
    return dict(trigger=base + ".trigger", resolved=base + ".resolved", unsettled=base + ".unsettled", spent=base + ".recovery_spent")


# --- doc 11 section 3 ---------------------------------------------------------------------------------------------------

def parse_doc11(text):
    """Rows of the 'Friction registry input' table: (new woman, [partners])."""
    sect = text.split("## 3. Friction registry input", 1)
    if len(sect) < 2:
        return None
    body = sect[1].split("\n## ", 1)[0]
    rows = []
    for line in body.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0] in ("New woman", "") or set(cells[0]) <= set("-"):
            continue
        rows.append([cells[0], [p.strip() for p in cells[1].split(",")]])
    return rows


def expand(doc11_rows):
    out = []
    for a, partners in doc11_rows:
        for b in partners:
            out.append((a.lower(), b.lower()))
    return out


# --- the rules walk -----------------------------------------------------------------------------------------------------

def child_requires(entry):
    """The facts a singleton settlement of `entry` Requires (symbolic; mirrors G_i in the plan)."""
    ref = entry["ref"]
    req = {"trickster", "O:" + ref, "T:" + ref, "aged:" + ref}
    for w in entry["women"]:
        req.add("A:" + w)
    return req


def child_key_ok(entry, facts):
    keys = entry.get("keys")
    return not keys or any("key:" + k in facts for k in keys)


def singleton_available(entry, facts, outcomes):
    """Ordinary scene(): no automatic enmity Forbids; Forbids its own .resolved and .unsettled only."""
    return child_requires(entry) <= facts and child_key_ok(entry, facts) and outcomes.get(entry["ref"]) is None


def acknowledgment_available(entry, facts):
    """Witness-side acknowledgment: O and the witness's own channel only (P11)."""
    w = entry.get("witness")
    return bool(w) and {"trickster", "O:" + entry["ref"], "A:" + w} <= facts


def packet_available(packet, by_ref, facts, outcomes, enmity):
    kids = [by_ref[r] for r in packet["children"]]
    if "KEPT" not in facts:
        return False
    if any(outcomes.get(k["ref"]) is not None for k in kids):
        return False
    if any(not (child_requires(k) <= facts and child_key_ok(k, facts)) for k in kids):
        return False
    women = {w for k in kids for w in k["women"]}
    if any("E:" + w not in facts for w in women):
        return False
    return not any(frozenset(e) <= women for e in enmity)   # a joint meeting is refused under any participant enmity


def recovery_available(ref, facts, outcomes, spent):
    return outcomes.get(ref) == "unsettled" and "token:" + ref in facts and ref not in spent


def walk_packet(packet, by_ref, errors):
    kids = [by_ref[r] for r in packet["children"]]
    women = sorted({w for k in kids for w in k["women"]})
    refs = [k["ref"] for k in kids]
    base = {"trickster", "KEPT"} | {"O:" + r for r in refs} | {"T:" + r for r in refs} | {"E:" + w for w in women}
    pid = packet["id"]
    states = 0

    def check(facts, outcomes, enmity, label):
        nonlocal states
        states += 1
        pk = packet_available(packet, by_ref, facts, outcomes, enmity)
        all_ready = all(child_requires(k) <= facts and child_key_ok(k, facts) for k in kids)
        none_done = all(outcomes.get(r) is None for r in refs)
        joint_ok = not any(frozenset(e) <= set(women) for e in enmity)
        if pk != (all_ready and none_done and joint_ok):                                   # P1, P2, P3, P6, P7, P9
            errors.append("%s %s: packet availability %s disagrees with its children" % (pid, label, pk))
            return False
        for k in kids:
            ready = child_requires(k) <= facts and child_key_ok(k, facts)
            single = singleton_available(k, facts, outcomes)
            if single != (ready and outcomes.get(k["ref"]) is None):                         # independence (P2, P4, P6, P9)
                errors.append("%s %s: singleton %s depends on a sibling" % (pid, label, k["ref"]))
                return False
            if ready and outcomes.get(k["ref"]) is None and not (single or pk):              # coverage
                errors.append("%s %s: %s is ready but unreachable" % (pid, label, k["ref"]))
                return False
        return True

    # Exhaustive: attendance per woman x child outcome (absent/recorded) x no enmity or one participant edge.
    # .resolved and .unsettled gate identically here (both Forbid re-entry); P7/P8 below separate them.
    edges = [None, frozenset(women[:2])]
    for attend in itertools.product((True, False), repeat=len(women)):
        facts = base | {"aged:" + r for r in refs} | {"A:" + w for w, on in zip(women, attend) if on}
        for outs in itertools.product((None, "resolved"), repeat=len(refs)):
            outcomes = dict(zip(refs, outs))
            for e in edges:
                if not check(facts, outcomes, [e] if e else [], "attend=%s outs=%s" % (attend, outs)):
                    return states
    # Exhaustive timing (P6): every subset of aged children, all present, no outcomes.
    for aged in itertools.product((True, False), repeat=len(refs)):
        facts = base | {"A:" + w for w in women} | {"aged:" + r for r, on in zip(refs, aged) if on}
        if not check(facts, {}, [], "aged=%s" % (aged,)):
            return states
    # P7/P8: a packet interrupted after recording some children; recovery rules.
    full = base | {"A:" + w for w in women} | {"aged:" + r for r in refs}
    for n in range(1, len(refs)):
        outcomes = {r: "unsettled" for r in refs[:n]}
        if packet_available(packet, by_ref, full, outcomes, []):
            errors.append("%s P7: re-entry allowed after a partial outcome" % pid)
        for r in refs[n:]:
            if not singleton_available(by_ref[r], full, outcomes):
                errors.append("%s P7: %s stranded after a partial packet" % (pid, r))
        r0 = refs[0]
        if recovery_available(r0, full, outcomes, set()):
            errors.append("%s P8: recovery offered without its own token" % pid)
        if not recovery_available(r0, full | {"token:" + r0}, outcomes, set()):
            errors.append("%s P8: recovery not offered with .unsettled plus its token" % pid)
        if recovery_available(r0, full | {"token:" + r0}, {r0: "resolved"}, set()):
            errors.append("%s P8: recovery offered after .resolved" % pid)
    return states


def delayed_clock_errors(scene, story):
    """Every selectable OR alternative must bring a timestamp, unless an unconditional Requires already does."""
    if not scene.get("DelayHours"):
        return []
    timestamped = set(story.get("Latches", {})) | {s["Id"] for s in story.get("Scenes", [])}
    timestamped |= {flag for s in story.get("Scenes", []) for n in s.get("Nodes", [])
                    for c in n.get("Choices", []) for flag in c.get("Set", [])}
    timestamped |= {flag for s in story.get("Scenes", []) for n in s.get("Nodes", []) for flag in n.get("EnterSet", [])}
    if any(flag in timestamped for flag in scene.get("Requires", [])):
        return []
    if any(group and all(flag in timestamped for flag in group) for group in scene.get("RequiresAnyGroups", [])):
        return []
    return ["K8: %s delayed step has no timestamped clock on every AnyGroups alternative" % scene["Id"]]


def scene_load_errors(story, data):
    """Caps apply to authored household registrations only; protected discoveries are structural."""
    errors = []
    scenes = [s for s in story.get("Scenes", []) if s.get("HouseholdCategory")]
    for s in scenes:
        category = s["HouseholdCategory"]
        if category not in ("protected", "pair", "mend", "dynamic", "letter"):
            errors.append("K8: %s has an unknown household category" % s["Id"])
        expected = "household.protected" if category == "protected" else "household.pair" if category in ("pair", "mend") else None
        if s.get("RestAllowance") != expected:
            errors.append("K8: %s category/RestAllowance mismatch" % s["Id"])
        if category == "protected" and any('.cap.' in f for f in s.get("Forbids", [])):
            errors.append("K8: protected discovery %s has a Counts cap" % s["Id"])
        errors.extend(delayed_clock_errors(s, story))
    for chapter, caps in data.get("load_caps", {}).items():
        chapter = int(chapter)
        arcs, starts, carried = {}, set(), set()
        for s in scenes:
            if s["HouseholdCategory"] != "pair" or chapter not in s.get("Chapters", range(s["MinChapter"], s["MaxChapter"] + 1)):
                continue
            arc = s.get("HouseholdArc")
            if not arc:
                errors.append("K8: optional step %s needs an arc id" % s["Id"])
                continue
            arcs.setdefault(arc, set()).add(s["HouseholdWitness"])
        for s in scenes:
            if not s.get("HouseholdArcStart"):
                continue
            arc = s.get("HouseholdArc")
            chapters = s.get("Chapters") or range(s["MinChapter"], s["MaxChapter"] + 1)
            if chapter in chapters:
                starts.add(arc)
            if any(ch < chapter for ch in chapters):
                carried.add(arc)
        # Earlier starts consume their remaining steps even when this chapter allows additional new starts.
        maximum = sum(len(arcs[arc]) for arc in carried if arc in arcs)
        maximum += sum(sorted((len(steps) for arc, steps in arcs.items() if arc not in carried), reverse=True)[:caps.get("arcs", 0)])
        if any(arc not in starts | carried for arc in arcs):
            errors.append("K8: Ch%d optional arc has no registered start" % chapter)
        if chapter == 3:
            mends = {s["HouseholdWitness"] for s in scenes if s["HouseholdCategory"] == "mend"
                     and chapter in (s.get("Chapters") or range(s["MinChapter"], s["MaxChapter"] + 1))}
            maximum += min(len(mends), caps.get("mend", 0))
        if maximum > caps.get("optional", 0):
            errors.append("K8: Ch%d optional step sum %d exceeds %d" % (chapter, maximum, caps['optional']))
    return errors


# --- the checks ---------------------------------------------------------------------------------------------------------

def lint(data, story=None, doc11_text=None):
    errors, notes = [], []
    cands, rows, sched = data["candidates"], data["rows"], data["schedule"]
    seat = data["seat_women"]

    # K1 completeness
    expected = expand(data["doc11_rows"])
    if len(data["doc11_rows"]) != 43:
        errors.append("K1: doc 11 section 3 snapshot has %d rows, expected 43" % len(data["doc11_rows"]))
    if doc11_text is not None:
        live = parse_doc11(doc11_text)
        if live is None:
            errors.append("K1: 11-ROSTER-PLAN-2.md has no section 3 table")
        elif [[a, sorted(b)] for a, b in live] != [[a, sorted(b)] for a, b in data["doc11_rows"]]:
            errors.append("K1: the doc 11 section 3 table changed; reclassify (snapshot is stale)")
    got = [tuple(c["pair"]) for c in cands]
    if got != expected:
        errors.append("K1: candidates do not match doc 11 section 3 in order (%d vs %d)" % (len(got), len(expected)))
    ids = [c["id"] for c in cands]
    if len(set(ids)) != len(ids):
        errors.append("K1: duplicate candidate ids")

    # schedule index
    by_ref, by_order = {}, {}
    for e in sched:
        if e["ref"] in by_ref or e["order"] in by_order:
            errors.append("K4: duplicate schedule ref/order %s/%s" % (e["ref"], e["order"]))
        by_ref[e["ref"]], by_order[e["order"]] = e, e

    # K2/K3 classification and protection
    for c in cands:
        cls = c["class"]
        if cls not in ("merged", "promoted", "cordial"):
            errors.append("K2: %s bad class %s" % (c["id"], cls))
        if (cls == "cordial") != (c["row"] is None):
            errors.append("K2: %s %s row mismatch" % (c["id"], cls))
        if cls == "promoted" and str(c["row"]) not in rows:
            errors.append("K2: %s promoted to undefined row %s" % (c["id"], c["row"]))
        if cls == "promoted" and sorted(rows[str(c["row"])]["pair"]) != sorted(c["pair"]):
            errors.append("K2: %s row %s names other women" % (c["id"], c["row"]))
        if not c.get("reason") or not c.get("evidence"):
            errors.append("K2: %s needs a reason and its evidence status" % c["id"])
        if c["canon"] not in ("verified", "authored", "unsupported", "pending"):
            errors.append("K2: %s bad canon status" % c["id"])
        ob = c.get("obligation")
        if ob in OBLIGATIONS:
            if cls == "cordial" or "X" not in (c.get("kind") or ""):
                errors.append("K3: %s %s obligation demoted (class %s, kind %s)" % (c["id"], ob, cls, c.get("kind")))
            if not c["protection"]:
                errors.append("K3: %s %s obligation has no protected beat" % (c["id"], ob))
        if ob == "dynamic" and "5.dynamic" not in c["protection"]:
            errors.append("K3: %s dynamic obligation must reserve 5.dynamic" % c["id"])
        for p in c["protection"]:
            if p not in by_ref and p not in by_order:
                errors.append("K3: %s protection %s has no schedule entry" % (c["id"], p))
    for num, r in rows.items():
        if not any(e.get("row") == int(num) for e in sched):
            errors.append("K3: promoted row %s has no scheduled beat" % num)
        if r["rom"]:
            errors.append("K3: new row %s may not be romance-eligible in a classification pass" % num)
        if r["kind"] == "X" and (r["start"], r["ceiling"]) != ("fixed", "fixed"):
            errors.append("K3: X row %s must be fixed (no ladder)" % num)

    # K4 schedule order and counts
    def key(o):
        head, _, tail = o.partition(".")
        return (int(head), tail if not tail.isdigit() else "%03d" % int(tail))
    orders = [e["order"] for e in sched]
    if orders != sorted(orders, key=key):
        errors.append("K4: schedule orders are not ascending")
    ch5 = [e for e in sched if re.fullmatch(r"5\.\d\d", e["order"])]
    if [e["order"] for e in ch5] != ["5.%02d" % i for i in range(1, len(ch5) + 1)]:
        errors.append("K4: Ch5 primary orders are not contiguous")
    for e in sched:
        if e["chapter"] != key(e["order"])[0]:
            errors.append("K4: %s chapter disagrees with its order" % e["order"])
        if "arueshalae" in e["women"]:
            if not e.get("keys") or not set(e["keys"]) <= set(ARUE_KEYS):
                errors.append("K4: %s reads Arueshalae without a positive key" % e["ref"])
            elif singleton_available(e, child_requires(e) | {"trickster"}, {}):
                errors.append("K4: %s plays in the unknown Arueshalae state" % e["ref"])
        rec = e.get("recovery")
        if rec and rec.get("delay_hours", 0) < 48:
            errors.append("K4: %s recovery waits under 48 h" % e["ref"])
        if e["type"] in ("atrocity",) and not e.get("witness"):
            errors.append("K4: %s atrocity docket needs a witness for its unilateral acknowledgment" % e["ref"])
    cnt = data["expected_counts"]
    primary = sum(e.get("count", 0) for e in ch5)
    ideal = primary - sum(e.get("count", 0) for e in ch5 if e.get("keys") == ["arueshalae.corrupted"])
    saving = sum(len(p["children"]) - 1 for p in data["packets"])
    s52 = 1 if "S52" in by_ref and by_ref["S52"].get("conditional") else 0
    computed = dict(ch5_primary=primary, ideal_redeemed=ideal, ideal_redeemed_no_s52=ideal - s52,
                    consolidated=ideal - saving, consolidated_no_s52=ideal - saving - s52, packet_saving=saving)
    for k, v in computed.items():
        if cnt.get(k) != v:
            errors.append("K4: count %s is %s, data says %s" % (k, v, cnt.get(k)))
    notes.append("counts: " + ", ".join("%s=%d" % kv for kv in computed.items()))

    # K5 names
    rels = set(story["Relationships"]) if story else None
    for e in sched:
        for w in e["women"] + ([e["witness"]] if e.get("witness") else []):
            if rels is not None and w not in rels and w not in seat:
                errors.append("K5: %s names unknown woman %s" % (e["ref"], w))
        for f in outcome_flags(e["ref"]).values():
            if any(b in f for b in BANNED_OUTCOME_WORDS):
                errors.append("K5: proposed outcome %s uses a banned word" % f)
    for c in cands:
        for w in c["pair"]:
            if rels is not None and w not in rels and w not in seat:
                errors.append("K5: %s names unknown woman %s" % (c["id"], w))
    for w in ("ember", "aivu"):
        if any(w in e["women"] for e in sched) or any(w in c["pair"] for c in cands):
            errors.append("K5: %s is friendship-only and never in the harem schedule" % w)

    # K6 existing reads
    if story is not None:
        known = {s["Id"] for s in story["Scenes"]}
        for s in story["Scenes"]:
            for nd in s["Nodes"]:
                for ch in nd["Choices"]:
                    known.update(ch.get("Set", []))
        for k, v in story.items():
            if isinstance(v, dict) and k not in ("Relationships", "Glossary", "Books"):
                known.update(v)
        for e in sched:
            for f in e.get("reads", []) + e.get("forbids_existing", []):
                if f not in known:
                    errors.append("K6: %s reads %s, which Story.json neither produces nor binds" % (e["ref"], f))
        produced = sorted(f for f in known if f.startswith(PROTECTED_PREFIX))
        notes.append("household.protected.* producers in Story.json: %d (expected 0 until the pair builds land)" % len(produced))

    if by_ref.get("S46", {}).get("status") != "retired" or by_ref.get("S46", {}).get("count") != 0:
        errors.append("K4: S46 must stay retired with count 0")
    for entry in sched:
        if entry.get("retry", 0) not in (0, 1):
            errors.append("K4: %s has more than one retry" % entry["ref"])
    if by_ref.get("DYN", {}).get("cap") != 3 or not by_ref.get("DYN", {}).get("protected_discoveries_uncapped"):
        errors.append("K4: optional dynamic cap is 3; protected discoveries stay uncapped")
    if story is not None:
        errors.extend(scene_load_errors(story, data))

    # K7 proofs
    states = 0
    packeted = {}
    for p in data["packets"]:
        for r in p["children"]:
            if r not in by_ref:
                errors.append("K7: %s child %s is not scheduled" % (p["id"], r))
            elif r in packeted:
                errors.append("K7: %s is in two packets" % r)
            packeted[r] = p["id"]
        if any(r not in by_ref for r in p["children"]):
            continue
        before = len(errors)
        kids = [by_ref[r] for r in p["children"]]
        if any(k.get("conditional") for k in kids):
            errors.append("K7: %s contains a conditional child" % p["id"])
        for k in kids:   # P5: no packet child reads Arueshalae's branch
            if k.get("keys") or "arueshalae" in k["women"]:
                errors.append("K7: %s P5: child %s reads Arueshalae's branch; keep it out of packets" % (p["id"], k["ref"]))
        if any("iomedae" in k["women"] for k in kids):
            errors.append("K7: %s seats Iomedae at the tavern" % p["id"])
        for rj in data["rejected_packets"]:
            if len(rj["children"]) == 1 and rj["children"][0] in p["children"]:
                errors.append("K7: %s contains rejected child %s" % (p["id"], rj["children"][0]))
            if len(rj["children"]) > 1 and set(rj["children"]) <= set(p["children"]):
                errors.append("K7: %s joins rejected children %s" % (p["id"], rj["children"]))
        if len(errors) == before:   # walk only a packet whose composition is legal
            states += walk_packet(p, by_ref, errors)
    # P4 seat separation: Minagho present, Chivarro absent.
    for p in data["packets"]:
        kids = [by_ref[r] for r in p["children"] if r in by_ref]
        women = {w for k in kids for w in k["women"]}
        if {"minagho", "chivarro"} & women:
            refs = [k["ref"] for k in kids]
            facts = ({"trickster", "KEPT"} | {"O:" + r for r in refs} | {"T:" + r for r in refs} | {"aged:" + r for r in refs}
                     | {"A:" + w for w in women if w != "chivarro"} | {"E:" + w for w in women})
            for k in kids:
                if singleton_available(k, facts, {}) == ("chivarro" in k["women"]):
                    errors.append("K7: %s P4 seat separation fails for %s" % (p["id"], k["ref"]))
    # P11 unilateral acknowledgment with the accused absent and uncourted.
    for e in sched:
        if e["type"] == "atrocity":
            facts = {"trickster", "O:" + e["ref"], "A:" + e["witness"]}
            if not acknowledgment_available(e, facts):
                errors.append("K7: %s P11 acknowledgment needs the accused" % e["ref"])
    notes.append("rules walk: %d packet states checked (P1-P9, P11); P10, P12-P14 are integration acceptance" % states)
    return errors, notes


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--data", default=str(DEFAULT_DATA))
    ap.add_argument("--story", default=None, help="development/Story.json, for the K5/K6 existence checks")
    ap.add_argument("--doc11", default=str(DEFAULT_DOC11), help="11-ROSTER-PLAN-2.md (skipped when absent)")
    args = ap.parse_args(argv)
    try:
        data = load_json(args.data)
        story = load_json(args.story) if args.story else None
    except (OSError, ValueError) as exc:
        print("SCHEMA: %s" % exc)
        return 2
    doc11 = Path(args.doc11)
    doc11_text = doc11.read_text(encoding="utf-8") if doc11.is_file() else None
    try:
        errors, notes = lint(data, story, doc11_text)
    except (KeyError, TypeError) as exc:
        print("SCHEMA: missing or malformed field: %r" % (exc,))
        return 2
    for n in notes:
        print("NOTE  " + n)
    if doc11_text is None:
        print("NOTE  doc 11 not found; the section 3 snapshot was not compared")
    for e in errors:
        print("HARD  " + e)
    print("harem schedule lint: %d candidates, %d scheduled beats, %d packets, %d hard"
          % (len(data["candidates"]), len(data["schedule"]), len(data["packets"]), len(errors)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

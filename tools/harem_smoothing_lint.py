"""Harem smoothing lint and form audit (doc 16 section 8c.3; data only).

Checks tools/harem-smoothing.json (per-woman smoothing repair metadata) and prints the combined form audit over the friction
registry (storylines/household_frictions.py), the smoothing repairs, the extra design reservations and, when present, the
consolidation packets of tools/harem-schedule.json (doc 16 section 8c.2).

Hard errors (exit 1): roster or tag drift from doc 16 section 2.3, seat overrides, indifferent rows with repairs, a susceptible
woman without one, unknown forms in the smoothing data, bad nearest-three, duplicate mechanisms or motive-action pairs, Arueshalae
variants not keyed on positive states, malformed enGB keys, a relationship the household does not know, and (with --story) any
reserved smoothing/strain/mend name already present in Story.json (this unit produces none).

Form cap (08 section 5: no form more than twice across frictions, repairs, reservations and packets). Rulings D1/D2 (W0b): the
vocabulary is expanded and the allocation passes; build-expansion.ps1 runs with --strict-forms, which fails on any form over the cap
or any form outside the vocabulary. Counting (D2): mutually exclusive variants of one woman charge a form once, and a repair marked
"retry": true is not charged. The test pins the arithmetic so drift is visible.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "tools" / "harem-smoothing.json"
SCHEDULE = ROOT / "tools" / "harem-schedule.json"
ENGB = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure\Wrath_Data\StreamingAssets\Localization\enGB.json")
DOC16 = Path(r"C:\Users\Z\Documents\Projects\Writer\handoffs\16-HOUSEHOLD-DYNAMICS.md")
KEY = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
RESERVED_IN_STORY = re.compile(r"household\.smooth\.|\.harem\.strain\.|\.harem\.mend\.")
FRIENDSHIP_ONLY = {"ember", "aivu"}


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def household_maps():
    sys.path.insert(0, str(ROOT))
    from storylines import household, household_frictions
    return household.PARTNERS, household.PAIR_WOMEN, household_frictions.FRICTIONS


def parse_doc16_tags(text):
    """The 16 section 2.3 defaults table -> {tag: [woman ids]} (lower-cased first names)."""
    out = {}
    for m in re.finditer(r"^\| \*\*(possessive|competitive|communal|indifferent)\*\* \| ([^|]+) \|", text, re.M):
        names = [re.sub(r"\s*\(.*?\)", "", x).strip().split()[0].lower() for x in m.group(2).split(",")]
        out[m.group(1)] = names
    return out


def repairs(data, include_retired=False):
    for w in data["women"]:
        for r in w.get("repairs", []):
            if include_retired or not r.get("retired"):
                yield w, r


def lint(data, story_text=None, engb=None, partners=None, pair_women=None):
    errs = []
    E = errs.append
    if partners is None:
        partners, pair_women, _ = household_maps()
    forms, tags = data["forms"], data["tags"]
    women = {w["id"]: w for w in data["women"]}
    if len(women) != len(data["women"]):
        E("duplicate woman id")
    if FRIENDSHIP_ONLY & set(women):
        E("Ember/Aivu are friendship-only and never in the smoothing data")
    expected = {wid: tag for tag, ids in data["doc16_tags"].items() for wid in ids}
    if set(expected) != set(women):
        E("roster drift vs doc 16 section 2.3: missing %s, extra %s"
          % (sorted(set(expected) - set(women)), sorted(set(women) - set(expected))))
    seat_of = {}
    for seat, o in data["seat_overrides"].items():
        if o["tag"] != "communal" or o["mode"] not in ("pair_first", "own_household"):
            E("seat override %s must be communal with a known mode" % seat)
        for wid in o["women"]:
            seat_of[wid] = seat
    if data["seat_overrides"].get("tirabade", {}).get("mode") != "pair_first" or \
            data["seat_overrides"].get("minagho_chivarro", {}).get("mode") != "own_household":
        E("seat overrides drift from doc 16 section 2.3")
    for seat, ws in (pair_women or {}).items():
        if seat in data["seat_overrides"] and tuple(data["seat_overrides"][seat]["women"]) != tuple(ws):
            E("seat %s women differ from household.PAIR_WOMEN" % seat)
    for wid, w in women.items():
        if w["default"] not in tags:
            E("%s: unknown tag %s" % (wid, w["default"]))
        if expected.get(wid) not in (None, w["default"]):
            E("%s: default %s, doc 16 says %s" % (wid, w["default"], expected[wid]))
        if w.get("seat") != seat_of.get(wid):
            E("%s: seat field must match seat_overrides" % wid)
        rel = w["rel"]
        if rel not in partners:
            E("%s: relationship %s is not a household partner" % (wid, rel))
        if rel != wid and not (rel in (pair_women or {}) and wid in pair_women[rel]):
            E("%s: relationship %s only allowed through PAIR_WOMEN" % (wid, rel))
        if w["provenance"] not in ("R", "S", "P"):
            E("%s: provenance must be R, S or P" % wid)
        if w["provenance"] == "R" and not w["terms_source"].startswith("06 "):
            E("%s: R provenance needs a 06 terms_source" % wid)
        for k in w.get("canon", []):
            if not KEY.match(k):
                E("%s: malformed enGB key %s" % (wid, k))
            elif engb is not None and k not in engb:
                E("%s: enGB key %s not found" % (wid, k))
        live = [r for r in w.get("repairs", []) if not r.get("retired")]
        if w["default"] == "indifferent":
            if w.get("repairs"):
                E("%s: indifferent women have no repair (16 section 2.4)" % wid)
            if not w.get("null_note"):
                E("%s: indifferent row needs a null_note" % wid)
        elif not live:
            E("%s: a susceptible woman needs at least one repair" % wid)
    mech, pairs = Counter(), Counter()
    for w, r in repairs(data):
        wid = w["id"]
        where = "%s/%s" % (wid, r.get("variant") or "-")
        for f in ("mechanism", "form", "action", "cost", "reaction", "nearest", "distinction"):
            if not r.get(f):
                E("%s: missing %s" % (where, f))
        if r.get("form") not in forms:
            E("%s: form %r is not in 08 section 5" % (where, r.get("form")))
        near = r.get("nearest", [])
        if len(near) != 3 or len(set(near)) != 3 or wid in near:
            E("%s: nearest must name three distinct other women" % where)
        for o in near:
            if o not in women:
                E("%s: nearest %s unknown" % (where, o))
            elif women[o]["default"] != w["default"]:
                E("%s: nearest %s has a different default tag" % (where, o))
        mech[r.get("mechanism")] += 1
        pairs[(w.get("motive", "").strip().lower(), r.get("action", "").strip().lower())] += 1
        dc = r.get("dc_proposal")
        if dc is not None and (len(dc) != 2 or not str(dc[0]).startswith(("Skill", "Check")) or not isinstance(dc[1], int)):
            E("%s: dc_proposal must be [Skill..., int]" % where)
    for m, k in mech.items():
        if k > 2:
            E("mechanism %s used %d times (cap 2, 16 section 2.3)" % (m, k))
    for p, k in pairs.items():
        if k > 1:
            E("duplicate motive-action pair: %s" % (p[1][:60],))
    a = women.get("arueshalae")
    if a:
        variants = {r.get("variant"): r for r in a.get("repairs", [])}
        if set(variants) != {"redeemed", "corrupted"}:
            E("arueshalae: exactly the redeemed and corrupted variants")
        for v in ("redeemed", "corrupted"):
            r = variants.get(v, {})
            if r.get("requires") != ["arueshalae." + v]:
                E("arueshalae/%s: must Require arueshalae.%s (positive key, no absence fallback)" % (v, v))
    for w, r in repairs(data):
        if w["id"] != "arueshalae" and r.get("requires"):
            for f in r["requires"]:
                if f.startswith("arueshalae."):
                    E("%s: reads an Arueshalae personality key" % w["id"])
    if story_text is not None:
        hits = sorted(set(m.group(0) for m in RESERVED_IN_STORY.finditer(story_text)))
        if hits:
            E("Story.json already uses reserved smoothing/strain/mend names %s: build sheets must replace this data-only check" % hits)
    return errs


def form_audit(data, frictions, packets=()):
    """Combined form counts. Returns (rows, totals); rows = [(form, friction, smoothing, reservations, packets, total)]."""
    vocab = list(data["forms"])
    fr = Counter(f["form"] for f in frictions)
    sm = Counter(form for _, form in sorted({(w["id"], r["form"]) for w, r in repairs(data) if not r.get("retry")}))
    rs = Counter(x["form"] for x in data.get("extra_reservations", []))
    pk = Counter(p["form"] for p in packets)
    allforms = vocab + sorted((set(fr) | set(sm) | set(rs) | set(pk)) - set(vocab))
    rows = [(f, fr[f], sm[f], rs[f], pk[f], fr[f] + sm[f] + rs[f] + pk[f]) for f in allforms]
    cap = data["form_cap"]
    totals = dict(frictions=sum(fr.values()), smoothing=sum(sm.values()), combined=sum(fr.values()) + sum(sm.values()),
                  with_reservations=sum(fr.values()) + sum(sm.values()) + sum(rs.values()),
                  packets=sum(pk.values()), charged=sum(r[5] for r in rows), capacity=cap * len(vocab),
                  over_cap_forms=sum(1 for r in rows if r[0] in vocab and r[5] > cap),
                  unapproved_forms=[r[0] for r in rows if r[0] not in vocab])
    return rows, totals


def report(data, frictions, packets):
    rows, t = form_audit(data, frictions, packets)
    cap = data["form_cap"]
    print("Harem form audit (08 section 5 cap %d; frictions + smoothing + reservations%s)" % (cap, " + packets" if packets else ""))
    print("  %-40s %4s %4s %4s %4s %5s  %s" % ("form", "fric", "smth", "resv", "pack", "total", "cap"))
    for f, a, b, c, d, tot in rows:
        state = "UNAPPROVED FORM" if f not in data["forms"] else ("over by %d" % (tot - cap) if tot > cap else "ok")
        print("  %-40s %4d %4d %4d %4d %5d  %s" % (f, a, b, c, d, tot, state))
    print("  combined %(combined)d, with reservations %(with_reservations)d, packets %(packets)d, charged %(charged)d, "
          "capacity %(capacity)d, forms over cap %(over_cap_forms)d" % t)
    print("  awaiting form allocation: friction rows %s; retries/later opportunities await build sheets"
          % ", ".join(data.get("unassigned_friction_rows", [])))
    print("  status: %s" % data.get("form_cap_status", ""))
    return t


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--data", default=str(DEFAULT_DATA))
    ap.add_argument("--story", help="development/Story.json: reserved names must stay unused")
    ap.add_argument("--engb", nargs="?", const=str(ENGB), help="check every canon key exists in enGB.json")
    ap.add_argument("--doc16", nargs="?", const=str(DOC16), help="check doc16_tags against the 16 section 2.3 table")
    ap.add_argument("--strict-forms", action="store_true", help="fail when any form exceeds the cap")
    a = ap.parse_args(argv)
    data = load_json(a.data)
    partners, pair_women, frictions = household_maps()
    story = Path(a.story).read_text(encoding="utf-8") if a.story else None
    engb = None
    if a.engb:
        d = load_json(a.engb)
        engb = d.get("strings", d)
    errs = lint(data, story, engb, partners, pair_women)
    if a.doc16:
        if parse_doc16_tags(Path(a.doc16).read_text(encoding="utf-8")) != data["doc16_tags"]:
            errs.append("doc16_tags snapshot differs from the 16 section 2.3 table")
    packets = load_json(SCHEDULE).get("packets", []) if SCHEDULE.is_file() else []
    t = report(data, frictions, packets)
    if a.strict_forms and (t["over_cap_forms"] or t["unapproved_forms"]):
        errs.append("form audit failed (strict): %d forms over cap, unapproved %s" % (t["over_cap_forms"], t["unapproved_forms"]))
    n = sum(1 for _ in repairs(data))
    print("Smoothing metadata: %d women, %d repairs, %d errors" % (len(data["women"]), n, len(errs)))
    for e in errs:
        print("  ERROR " + e)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())

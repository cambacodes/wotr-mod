"""Derive Arueshalae's flag truth table from an export (development/Story.json).

Usage: python tools/route_packs/redesign/arueshalae/truth_table.py [export] [baseline-export] > truth-table.json

Universe: every flag read or set by a Devarra scene (devarra.*, the
household.pair.nidalynn_devarra.* row, her Last Call account) plus every flag whose name starts
with "devarra". For each flag: every producer (choice Set, node EnterSet,
Derived rule, native SeenCues/SelectedAnswers/Latches/UnlockableFlags) and
every consumer (scene gate, choice gate, paragraph gate, Derived/DerivedForbids,
Ledger book line, Last Call or other scene that reads it).
"""
import json
import sys

# Flags this pass touched (see cloud-review.md section 1).
RETIRED = ("arueshalae.trickster.dead.starving", "arueshalae.trickster.insurance", "arueshalae.trickster.evil.diagnosis", "arueshalae.trickster.evil.late_referral", "arueshalae.trickster.evil.second_opinion", "arueshalae.trickster.evil.wager", "arueshalae.trickster.evil.wager_yard", "arueshalae.treatment.the_glover")
NOTES = {
    "arueshalae.trickster.returned": "Retired-producer-only: set only by the retired death returns (dead.starving, evil.second_opinion, gated off with chapter_later). Its whole downstream (evil.reunion*, evil.terms*, sergeant/daybook/token/the_boys/the_other_one/window*, epilogue.kept_fallen, lastcall.call, Nocticula's court.arueshalae) is legacy-save-only (rubric: pre-release states).",
    "arueshalae.evil_recruited": "Native EvilArushaRecruited 005c2284: the live fallen road (home_visit -> native recruit -> fallen.house_call / lock / roof / sergeant / the_other_one -> epilogue.fallen).",
    "arueshalae.trickster.cost.sent_away_hungry": "S1: 'Not a drop' (house_call:refuse) now has an on-screen consumer on the live road (fallen.sergeant) besides Lann's hearsay and epilogue.fallen P3 (re-voiced: act, not report).",
    "arueshalae.trickster.fallen.sergeant": "S1 new: the feed at Fye's, set by all three answers.",
    "arueshalae.trickster.fallen.sergeant_stopped": "S1 new: steel drawn; read by epilogue.fallen.",
    "arueshalae.trickster.fallen.sergeant_watched": "S1 new: the Commander watched (Evil 2); read by epilogue.fallen.",
    "arueshalae.trickster.fallen.sergeant_bought": "S1 new: a Scroll of Death Ward spent (RemoveItem 89e10c3f); read by epilogue.fallen.",
    "arueshalae.trickster.fallen.the_other_one": "S2 new: live twin of the retired-road evil.the_other_one.",
    "arueshalae.trickster.fallen.other_happy": "S2 new: read by epilogue.fallen.",
    "arueshalae.trickster.fallen.other_starving": "S2 new: read by epilogue.fallen.",
    "arueshalae.trickster.evil.home_offered": "S3: was set-never-read; now read by fallen.house_call:start (appended paragraph).",
    "arueshalae.committed": "S5 overload (noted, no split): redeemed 'Both' / 'Yes' and fallen 'Open the door' set the same key; every live consumer pairs it with evil_recruited / corruption, the only blind reader (nocticula.trickster.court.arueshalae:her_side) is legacy-only.",
    "arueshalae.trickster.cost.fed_on_you": "Retired on the live road (house_call:price>0 requires and forbids it: no unwarded touch); epilogue.fallen P0 is legacy-only.",
    "arueshalae.corrupted": "Derived: evil_recruited | returned+debt/favour | reunited | fallen.house_call | arueshalae.fallen. Every pair row and Shamira reaction splits on it.",
}

OWN = ("arueshalae.", "household.pair.seelah_arueshalae.", "household.pair.galfrey_arueshalae.", "household.pair.nenio_arueshalae.")


def gates(obj):
    out = []
    for key in ("Requires", "Forbids"):
        out += [(key, f) for f in obj.get(key) or []]
    for group in obj.get("RequiresAnyGroups") or obj.get("AnyGroups") or []:
        out += [("RequiresAny", f) for f in group]
    for f, over in (obj.get("ForbidOverrides") or {}).items():
        out += [("ForbidOverride", over)]
    return out


def scan(export):
    prod, cons, own_flags = {}, {}, set()
    def P(flag, where):
        prod.setdefault(flag, []).append(where)
    def C(flag, where):
        cons.setdefault(flag, []).append(where)
    for s in export["Scenes"]:
        sid = s["Id"]
        own = sid.startswith(OWN)
        local = []
        for kind, f in gates(s):
            C(f, "%s [scene %s]" % (sid, kind)); local.append(f)
        for n in s["Nodes"]:
            for f in n.get("EnterSet") or []:
                P(f, "%s:%s [EnterSet]" % (sid, n["Id"])); local.append(f)
            for i, para in enumerate(n.get("Paragraphs") or []):
                for kind, f in gates(para):
                    C(f, "%s:%s#%d [paragraph %s]" % (sid, n["Id"], i, kind)); local.append(f)
            for i, c in enumerate(n.get("Choices") or []):
                for f in c.get("Set") or []:
                    P(f, "%s:%s>%d %s" % (sid, n["Id"], i, c["Text"][:70])); local.append(f)
                for kind, f in gates(c):
                    C(f, "%s:%s>%d [choice %s]" % (sid, n["Id"], i, kind)); local.append(f)
        if own:
            own_flags.update(local)
    for f, rules in export.get("Derived", {}).items():
        for rule in rules:
            P(f, "Derived(%s)" % " & ".join(rule))
            for g in rule:
                C(g, "Derived -> %s" % f)
    for f, forb in export.get("DerivedForbids", {}).items():
        for g in forb:
            C(g, "DerivedForbids -> %s" % f)
    for key in ("SeenCues", "SelectedAnswers", "Latches", "UnlockableFlags", "CompletedEtudes", "CompletedQuests"):
        for f, src in (export.get(key) or {}).items():
            P(f, "native %s %s" % (key, json.dumps(src)[:80]))
    for bid, book in (export.get("Books") or {}).items():
        for e in book.get("Entries") or []:
            for kind, f in gates(e):
                C(f, "book %s/%s [%s]" % (bid, e["Id"], kind))
            for i, line in enumerate(e.get("Lines") or []):
                for kind, f in gates(line):
                    C(f, "book %s/%s line %d [%s]" % (bid, e["Id"], i, kind))
    universe = sorted(f for f in set(own_flags) | {f for f in set(prod) | set(cons) if f.startswith("arueshalae")})
    return universe, prod, cons


def main():
    export = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "development/Story.json", encoding="utf-8"))
    base = json.load(open(sys.argv[2], encoding="utf-8")) if len(sys.argv) > 2 else export
    universe, prod, cons = scan(export)
    _, _, base_cons = scan(base)
    retired = tuple(RETIRED)
    rows = []
    for f in universe:
        live_prod = [x for x in prod.get(f, []) if not x.startswith(retired)]
        live_cons = [x for x in cons.get(f, []) if not x.startswith(retired)]
        status = ("set-never-read" if f in prod and not cons.get(f) else
                  "read-with-no-authored-producer" if f in cons and not prod.get(f) else
                  "retired-producer-only" if prod.get(f) and not live_prod else
                  "read-only-by-retired" if cons.get(f) and not live_cons else "live")
        row = {
            "flag": f,
            "status": status,
            "producers": prod.get(f, []),
            "consumers_before": len(base_cons.get(f, [])),
            "consumers": cons.get(f, []),
            "unread": f in prod and not cons.get(f),
            "unproduced": f in cons and not prod.get(f),
        }
        if f in NOTES:
            row["note"] = NOTES[f]
        rows.append(row)
    json.dump({"source": "development/Story.json (see cloud-review.md for base and branch)",
               "flags": rows}, sys.stdout, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()

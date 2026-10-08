"""Derive Devarra's flag truth table from an export (development/Story.json).

Usage: python tools/route_packs/redesign/devarra/truth_table.py [export] [baseline-export] > truth-table.json

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
NOTES = {
    "devarra.trickster.cost.egg_withheld": "S1: the smallest-egg debt; named on every page that can show it (called) or collected from whatever is nearest (unanswered); refused pages: never collected.",
    "devarra.lastcall.called": "S1: P31 used to print the same 'never named' text as P32; now the answer at the rift, price named afterwards.",
    "devarra.lastcall.left_unspoken": "S1: read implicitly by the unanswered paragraphs (they forbid lastcall.called); no gate change.",
    "devarra.trickster.debt_claimed": "S2: the Commander's 'Then you owe me'; pair row no longer says she claimed it; paid in the_hoard (three readers).",
    "devarra.trickster.marked": "S3 overload: absent / smashed / ordered (and the retired 'I watched'); tithe:watch and the_clutch:nest re-voiced to fit all three.",
    "devarra.tower.twelfth_lied": "S4: 'I will add them together' now read on epilogue.woken and epilogue.commit.",
    "devarra.tower.coin_stolen": "S4: the Queen of Iobaria, read on both committed pages.",
    "devarra.tower.vault_refused": "S4: 'Say no to me again' read on both committed pages.",
    "devarra.tower.looked_away": "S4: 'Remember that' read on both committed pages.",
    "devarra.tower.warned": "S4: 'I will let you say that once' paid on the_dwarf:protect.",
    "devarra.tower.battle_price_accepted": "S5 (queue D03/D05): withheld battle with consequence (before_the_end:climb, epilogue P13).",
    "devarra.tower.battle_offered": "S5 (queue D04/D06): her unannounced column, witnessed before the finale (before_the_end:climb, epilogue P29).",
    "household.pair.nidalynn_devarra.resolved": "S6: the S50 feed now reaches her own epilogue (deserter at the kiln door).",
    "devarra.trickster.late_accepted": "S7: epilogue.commit now carries the same history readers as epilogue.woken.",
}

OWN = ("devarra.", "household.pair.nidalynn_devarra.", "trickster.lastcall.account.devarra")


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
    universe = sorted(f for f in set(own_flags) | {f for f in set(prod) | set(cons) if f.startswith("devarra")})
    return universe, prod, cons


def main():
    export = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "development/Story.json", encoding="utf-8"))
    base = json.load(open(sys.argv[2], encoding="utf-8")) if len(sys.argv) > 2 else export
    universe, prod, cons = scan(export)
    _, _, base_cons = scan(base)
    retired = ("devarra.trickster.dead.",)
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

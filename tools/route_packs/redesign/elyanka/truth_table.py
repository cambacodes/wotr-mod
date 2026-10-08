"""Derive Elyanka's flag truth table from an export (development/Story.json).

Usage: python tools/route_packs/redesign/elyanka/truth_table.py [export] [baseline-export] > truth-table.json

Universe: every flag read or set by an Elyanka scene (elyanka.*) plus her
secret, Last Call debt and Dorgelinda ledger flags, and every flag whose name starts
with "elyanka". For each flag: every producer (choice Set, node EnterSet,
Derived rule, native SeenCues/SelectedAnswers/Latches/UnlockableFlags) and
every consumer (scene gate, choice gate, paragraph gate, Derived/DerivedForbids,
Ledger book line, Last Call or other scene that reads it).
"""
import json
import sys

OWN = ("elyanka.",)
EXTRA = ("elyanka", "trickster.secret.elyanka", "lastcall.debt.whispering_way", "dorgelinda.ledger.current_other.elyanka", "dorgelinda.ledger.undisclosed.elyanka", "dorgelinda.ledger.disclosed.elyanka")


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
        P(sid, "%s [scene completion: the runtime sets the scene id]" % sid)
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
    universe = sorted(f for f in set(own_flags) | {f for f in set(prod) | set(cons) if f.startswith(EXTRA)})
    return universe, prod, cons


def main():
    export = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "development/Story.json", encoding="utf-8"))
    base = json.load(open(sys.argv[2], encoding="utf-8")) if len(sys.argv) > 2 else export
    universe, prod, cons = scan(export)
    _, _, base_cons = scan(base)
    rows = []
    for f in universe:
        rows.append({
            "flag": f,
            "producers": prod.get(f, []),
            "consumers_before": len(base_cons.get(f, [])),
            "consumers": cons.get(f, []),
            "unread": f in prod and not cons.get(f),
            "unproduced": f in cons and not prod.get(f),
        })
    json.dump({"source": "development/Story.json on cloud/villain-route-elyanka; consumers_before = count in the stubbed build of main 723ccae",
               "flags": rows}, sys.stdout, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()

"""Derive Nocticula's flag truth table from an export (development/Story.json).

Usage: python tools/route_packs/redesign/nocticula/truth_table.py [export] [baseline-export] > truth-table.json

Universe: every flag read or set by a Nocticula scene (noct.*, nocticula.*,
the household.pair.*nocticula* rows, arueshalae.trickster.evil.second_opinion)
plus every flag whose name starts with "noct". For each flag: every producer
(choice Set, node EnterSet, Derived rule, native SeenCues/SelectedAnswers/
Latches/UnlockableFlags) and every consumer (scene/choice/paragraph gate,
Derived/DerivedForbids, Book line). The frozen ".acquired.*" clone families
are folded into their base scene (counted, not listed) to keep the table
readable; "retired" = a scene that Requires noct.retired.
"""
import json
import sys

# Flags this pass touched (see cloud-review.md section 1).
NOTES = {
    "nocticula.partner_stance.exclusive": "OVERLOAD (mitigated, recorded): set by her promise (with partner.exclusive_chosen), by accepting her refusal (with partner_exclusive_refused) and by 'Yes. We are finished.' (with exclusive_refused + noct.closed / noct.acq.closed). Every live reader pairs it with chosen or refused; the closing producer also closes the route. No split needed.",
    "nocticula.partner_stance.secret": "S1/S2: re-voiced readers; Threshold discovery no longer cites letters or a broker; epilogue discovery is by her mark, not paper.",
    "nocticula.partner_secret_exposed": "S2: Threshold discovery re-staged (runner, shadow); letter-route discovery re-voiced.",
    "nocticula.partner.letters_burned": "S2: Threshold 'hidden' branch burns the four crescents off (a marked gift); choice relabelled '[Keep her marks. Let them show.]'.",
    "nocticula.trickster.cost.shade_paid": "S3: refused_page/inn p24/p25 named the favour twice; now naming (council chair, second spring) then dinner.",
    "nocticula.lastcall.account_due": "S4: Last Call re-staged without paper; account_due implies cost.shade_paid via favour_due, so choice 0 of nocticula.lastcall.call (Forbids noct.dead) is unreachable (recorded R2).",
    "noct.crimson_mark": "S6: was set-never-read; now read on noct.ending_company/alliance/limit.",
    "noct.mark_hidden": "S6: was set-never-read; now read on noct.ending_company/alliance/limit.",
    "noct.lodge_appetite_admitted": "S6: now read on the harbor endings.",
    "noct.lodge_vigilance_admitted": "S6: now read on the harbor endings.",
    "noct.lodge_danger_desired": "S6: now read on the harbor endings.",
    "noct.lodge_desire_contested": "S6: now read on the harbor endings.",
    "household.pair.arueshalae_nocticula.unsettled": "S6: was set-never-read; now read on noct.acq.epilogue.correspondence.",
    "nocticula.harem.attitude.arueshalae.respect": "S6: was set-never-read; now read on noct.acq.epilogue.correspondence.",
    "household.pair.nocticula_shamira.resolved": "S6: was set-never-read; now read on noct.acq.epilogue.correspondence.",
    "nocticula.harem.stance.joined": "R3: no producer anywhere (Ledger guest line always reads the no-stance line); household-stance writer is structure, not this row.",
    "nocticula.trickster.cost.favour_burned": "R: set only in retired court.arueshalae (Forbids chapter_later); inert.",
}

OWN = ("noct.", "nocticula.", "household.pair.nocticula_", "household.pair.galfrey_nocticula", "household.pair.iomedae_nocticula", "household.pair.arueshalae_nocticula", "arueshalae.trickster.evil.second_opinion")


def fold(sid):
    return sid.split(".acquired.")[0] + (".acquired.*" if ".acquired." in sid else "")


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
        sid = fold(s["Id"])
        if "noct.retired" in (s.get("Requires") or []):
            sid = "RETIRED " + sid
        own = s["Id"].startswith(OWN)
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
    for key in ("SeenCues", "SelectedAnswers", "Latches", "UnlockableFlags", "CompletedEtudes", "CompletedQuests", "Etudes", "StartedDialogs", "PermanentEtudes", "StartedQuests"):
        table = export.get(key) or {}
        if not isinstance(table, dict):
            continue
        for f, src in table.items():
            P(f, "native %s %s" % (key, json.dumps(src)[:80]))
    for bid, book in (export.get("Books") or {}).items():
        for e in book.get("Entries") or []:
            for kind, f in gates(e):
                C(f, "book %s/%s [%s]" % (bid, e["Id"], kind))
            for i, line in enumerate(e.get("Lines") or []):
                for kind, f in gates(line):
                    C(f, "book %s/%s line %d [%s]" % (bid, e["Id"], i, kind))
    universe = sorted(f for f in set(own_flags) | {f for f in set(prod) | set(cons) if f.startswith(("noct", "nocticula"))} | (set(NOTES) & (set(prod) | set(cons))))
    return universe, prod, cons


def main():
    export = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "development/Story.json", encoding="utf-8"))
    base = json.load(open(sys.argv[2], encoding="utf-8")) if len(sys.argv) > 2 else export
    universe, prod, cons = scan(export)
    _, _, base_cons = scan(base)
    retired = ("RETIRED ",)
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
            "producers": sorted(set(prod.get(f, []))),
            "consumers_before": len(base_cons.get(f, [])),
            "consumers": sorted(set(cons.get(f, []))),
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

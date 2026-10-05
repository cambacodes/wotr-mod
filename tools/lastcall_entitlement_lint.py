"""eng7-l13 E-Q7-07: parity of the existing Last Call entitlement readers.

Debt records remain historical obligations. Partner calls/codas additionally
need live eligibility. A name discussion and a cairn alone never pay a stake
or create a relationship. This contract supplements L4's prose/producer proof.
"""
import argparse
import json
from pathlib import Path


def errors(story):
    out = []
    scenes = {s["Id"]: s for s in story["Scenes"]}
    if "nenio.lastcall.page" not in scenes:
        return out  # small synthetic stories have no Last Call framework
    for route in ("anevia", "nenio"):
        page = scenes[route + ".lastcall.page"]
        early, late = route + ".committed", route + ".trickster.late_committed"
        if early in page["Requires"] or not any(set(g) == {early, late} for g in page.get("RequiresAnyGroups", [])):
            out.append(route + ".lastcall.page: early OR earned late entitlement missing")
    actual, optional = "nenio.trickster.name_gone", "nenio.trickster.cost.name_filed"
    surfaces = {
        "nenio.lastcall.callable": story["Derived"]["nenio.lastcall.callable"],
        "nenio.lastcall.call": scenes["nenio.lastcall.call"].get("RequiresAnyGroups", []),
        "owed.nenio/book": next(e for e in story["Books"]["trickster.ledger"]["Entries"] if e["Id"] == "owed.nenio")["AnyGroups"],
        "owed.nenio/journal": next(e for e in story["Relationships"]["lastcall"]["JournalEntries"] if e["Id"] == "owed.nenio")["OpenWhen"],
    }
    for name, groups in surfaces.items():
        inputs = {k for g in groups for k in g}
        if actual not in inputs or optional in inputs:
            out.append(name + ": reads optional name discussion instead of actual paid name stake")
    for group in story["Derived"]["wenduag.lastcall.callable"]:
        if "wenduag.trickster.partner" not in group:
            out.append("wenduag.lastcall.callable: constructed cairn without partner entitlement")
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=Path(__file__).resolve().parents[1] / "development/Story.json")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    findings = errors(json.loads(args.story.read_text(encoding="utf-8-sig")))
    print("Last Call entitlement parity: %d findings" % len(findings))
    for finding in findings:
        print(finding)
    return int(args.strict and bool(findings))


if __name__ == "__main__":
    raise SystemExit(main())

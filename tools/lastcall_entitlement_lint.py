"""eng7-l13 E-Q7-07: parity of the existing Last Call entitlement readers.

Debt records remain historical obligations. Partner calls/codas additionally
need live eligibility. A name discussion and a cairn alone never pay a stake
or create a relationship. This contract supplements L4's prose/producer proof.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


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
    # eng8-q8g: historical claims share an explicit, mutation-tested inventory.
    out.extend(history_errors(story))
    # end eng8-q8g
    return out


# eng8-q8g: use the existing SAT proof, including ALL incoming choice paths.
CONTRACTS = Path(__file__).with_name("lastcall_history_inventory_contracts.json")


def history_errors(story, contracts=None):
    from tools.crossroute_checks.common import AND, NOT, OR, Proof, blocks, fields, lit, when
    from tools import rrt_verify

    contracts = contracts or json.loads(CONTRACTS.read_text(encoding="utf-8"))
    # Keep every native/Derived/relationship definition, but normalize only
    # inventoried graphs. Unrelated manuscripts do not supply history proof.
    scene_ids = {row["surface"][0] for row in contracts["surfaces"]}
    scene_ids.update(row[0] for row in contracts.get("retired_choices", []))
    model = rrt_verify.Model({**story, "Scenes": [s for s in story["Scenes"] if s["Id"] in scene_ids]})
    proof = Proof(model)
    surfaces = {(b.scene["Id"], b.node["Id"], b.slot): (b.context, b.text) for b in blocks(model)}
    for book, spec in story.get("Books", {}).items():
        for entry in spec.get("Entries", []):
            ctx = fields(entry, "AnyGroups")
            surfaces[(book, entry["Id"], "text")] = ctx, entry["Text"]
            for i, line in enumerate(entry.get("Lines", [])):
                surfaces[(book, entry["Id"], "line[%d]" % i)] = AND(ctx, fields(line, "AnyGroups")), line["Text"]
    for rel, spec in story.get("Relationships", {}).items():
        for entry in spec.get("JournalEntries", []):
            surfaces[(rel, entry["Id"], "description")] = when(entry["OpenWhen"]), entry["Description"]
            surfaces[(rel, entry["Id"], "settled")] = AND(when(entry["OpenWhen"]), when(entry["SettledWhen"])), ""
    failures = []
    for row in contracts["surfaces"]:
        address = tuple(row["surface"])
        label = "/".join(address)
        if address not in surfaces:
            failures.append(label + ": declared Last Call history surface missing")
            continue
        ctx, text = surfaces[address]
        target = AND(*(lit(k) for k in row.get("requires", [])),
                     *(lit(k, False) for k in row.get("forbids", [])),
                     *(OR(*(lit(k) for k in group)) for group in row.get("any_groups", [])))
        if not proof.implies(ctx, target):
            failures.append(label + ": narrated history lacks its declared witness")
        if proof.implies(ctx, NOT(ctx)):
            failures.append(label + ": declared history surface is impossible")
        for token in row.get("absent_text", []):
            if token.lower() in text.lower():
                failures.append(label + ": unearned history text: " + token)
    for key, groups in contracts.get("derived", {}).items():
        if story.get("Derived", {}).get(key) != groups:
            failures.append(key + ": recovery reader differs from actual release witnesses")
    scenes = {s["Id"]: s for s in story["Scenes"]}
    for row in contracts.get("producers", []):
        scene = scenes.get(row["scene"], {})
        node = next((n for n in scene.get("Nodes", []) if n["Id"] == row["node"]), {})
        choices = node.get("Choices", [])
        if len(choices) <= row["choice"] or not set(row["sets"]).issubset(choices[row["choice"]].get("Set", [])):
            failures.append(row["scene"] + "/" + row["node"] + ": enacted debt receipt missing")
    for receipt, expected in contracts.get("unique_producers", {}).items():
        actual = sorted(s["Id"] + "/" + n["Id"] + "/" + str(i)
                        for s in story["Scenes"] for n in s["Nodes"]
                        for i, c in enumerate(n["Choices"]) if receipt in c.get("Set", []))
        if actual != sorted(expected):
            failures.append(receipt + ": unregistered release/pardon producer")
    for scene, node, index in contracts.get("retired_choices", []):
        address = scene, node, "choice[%d]" % index
        if address not in surfaces or not proof.implies(surfaces[address][0], NOT(surfaces[address][0])):
            failures.append("/".join(address) + ": generic settlement is not retired")
    return failures
# end eng8-q8g


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

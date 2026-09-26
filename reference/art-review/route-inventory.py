"""Audit configured route text from installed-DLL IL references and call reachability."""
import collections
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
GAME = Path(r"D:\SteamLibrary\steamapps\common\Pathfinder Second Adventure")
source = json.loads((ROOT / "ran-route-il.json").read_text(encoding="utf-8-sig"))
localization = {row["Key"]: row.get("enGB", "") for row in source["Localization"]}
assert len(localization) == len(source["Localization"]), "Duplicate localization keys"
methods = {method["Token"]: method for method in source["Methods"]}
by_type = collections.defaultdict(list)
for method in methods.values():
    by_type[method["Type"]].append(method)


def walk(root):
    pending = [root["Token"]]
    reached = set()
    while pending:
        token = pending.pop()
        if token in reached:
            continue
        reached.add(token)
        method = methods[token]
        pending.extend(call["Token"] for call in method["Calls"]
                       if call.get("Target", "").startswith(("RanRomance.", "Epilogue."))
                       and call["Token"] in methods)
        pending.extend(item["Token"] for item in by_type[method["Type"]] if item["Method"] == ".cctor")
    return reached


def plain(text):
    return " ".join(re.sub(r"\{[^}]*\}|<[^>]*>", "", text).split())


def words(text):
    return len(re.findall(r"\b[^\W_]+(?:['’][^\W_]+)*\b", plain(text)))


routes = {}
names = {"Noct": "Nocticula", "Nura": "Nurah", "Targ": "Targona", "Tere": "Terendelev", "Aran": "Aranka", "Mina": "Minagho"}
owners = collections.defaultdict(list)
for short, name in names.items():
    root = next(method for method in methods.values() if method["Type"] == "RanRomance." + short + ".Main" and method["Method"] == "Configure")
    reachable = walk(root)
    keys = collections.defaultdict(list)
    for token in sorted(reachable):
        method = methods[token]
        for literal in method["Strings"]:
            key = literal["Value"]
            if key in localization:
                keys[key].append({"method": method["Type"] + "." + method["Method"], "method_token": token, "il_offset": literal["Offset"]})
    unique_text = {plain(localization[key]) for key in keys}
    routes[name] = {
        "entrypoint": root["Type"] + "." + root["Method"],
        "reachable_method_count": len(reachable),
        "localization_key_count": len(keys),
        "keyed_words": sum(words(localization[key]) for key in keys),
        "deduplicated_normalized_text_words": sum(words(text) for text in unique_text),
        "distinct_normalized_text_count": len(unique_text),
        "keys": {key: {"words": words(localization[key]), "references": refs} for key, refs in sorted(keys.items())},
    }
    for key in keys:
        owners[key].append(name)

for name, route in routes.items():
    shared = [key for key in route["keys"] if len(owners[key]) > 1]
    route["shared_with_other_romance_keys"] = shared
    route["shared_with_other_romance_words"] = sum(words(localization[key]) for key in shared)

all_referenced = {literal["Value"] for method in methods.values() for literal in method["Strings"] if literal["Value"] in localization}
loader = next(method for method in methods.values() if method["Type"] == "RanRomance.Main+BlueprintsCaches_Patch" and method["Method"] == "Init")
configured = walk(loader)
active_keys = {literal["Value"] for token in configured for literal in methods[token]["Strings"] if literal["Value"] in localization}
report = {
    "method": "Static reachability from installed route Main.Configure methods, including referenced callbacks and visited type initializers; count each matching localization key once per route",
    "word_rule": "Remove brace/angle-bracket markup, normalize whitespace, count Unicode alphanumeric words with internal apostrophes; rendering placeholders contribute zero words",
    "input_sha256": {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in [GAME / "Mods/RanRomance/RanRomance.dll", GAME / "Mods/RanRomance/LocalizedStrings.json", GAME / "Mods/RanRomance/readme.txt"]},
    "loader_errors": source["LoaderErrors"],
    "unresolved_method_operands": sum("Error" in call for method in methods.values() for call in method["Calls"]),
    "total_localization_keys": len(localization),
    "referenced_localization_keys": len(all_referenced),
    "loader_reachable_localization_keys": len(active_keys),
    "unreferenced_keys": sorted(localization.keys() - all_referenced),
    "referenced_but_not_loader_reachable": sorted(all_referenced - active_keys),
    "configured_keys_outside_six_romance_initializers": sorted(active_keys - owners.keys()),
    "configured_words_outside_six_romance_initializers": sum(words(localization[key]) for key in active_keys - owners.keys()),
    "words_outside_loader_reachability": sum(words(localization[key]) for key in localization.keys() - active_keys),
    "largest_initializer_plus_all_configured_unallocated_words": max(route["keyed_words"] for route in routes.values()) + sum(words(localization[key]) for key in active_keys - owners.keys()),
    "largest_initializer_plus_all_unallocated_localization_words": max(route["keyed_words"] for route in routes.values()) + sum(words(localization[key]) for key in localization.keys() - owners.keys()),
    "routes": routes,
    "shared_key_owners": {key: names for key, names in owners.items() if len(names) > 1},
    "limitations": [
        "Static configuration reachability, not runtime branch reachability or a single playthrough.",
        "Counts include dialogue, answers, titles and journal text when their keys are referenced by the initializer.",
        "Separate loader-configured shared NPC helpers/revisions may add route-related text not attributed to these six initializers.",
        "Distinct keys with identical rendered text count separately in keyed_words; the normalized-text total removes that duplication.",
        "No quality or character-fidelity score is inferred from word counts.",
        "The whole mod's localization total is not a per-character benchmark.",
        "Some merged BlueprintCore helper types could not load due to game accessibility; all requested gameplay namespace methods were inventoried against the local type list, and no method operand failed to resolve.",
    ],
}
(ROOT / "ran-route-word-inventory.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
for name, route in routes.items():
    print(name, route["localization_key_count"], route["keyed_words"], route["deduplicated_normalized_text_words"], "shared", route["shared_with_other_romance_words"])
print("Unreferenced:", report["unreferenced_keys"])
print("Not loader reachable:", report["referenced_but_not_loader_reachable"])
print("Configured keys outside six routes:", len(report["configured_keys_outside_six_romance_initializers"]))

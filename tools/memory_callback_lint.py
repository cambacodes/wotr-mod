"""Memory callbacks and reviewed authored-reference registry integrity.

Registry declarations are evidence, never game-state writes. This bootstrap
checks bindings and coverage; static implication and executed-history evaluation
are separate jobs. No registry-valid result certifies a played history.
"""
import copy
import hashlib
import json
from pathlib import Path
import re
from tools.player_text_lint import surface_records, surfaces, PATTERNS
from tools.draft_contract_lint import targets


def structural(value):
    if isinstance(value, dict):
        return {k: structural(v) for k, v in value.items() if k != "Text"}
    if isinstance(value, list):
        return [structural(v) for v in value]
    return value


CONTRACTS = Path(__file__).with_name("memory_callback_contracts.json")
REGISTRY = Path(__file__).with_name("narrative_consistency_contracts.json")


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


def text_digest(text):
    """Hash the exact exported UTF-8 text, including markup and newline bytes."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def review_structure(value):
    if isinstance(value, dict):
        return {k: review_structure(v) for k, v in value.items() if k not in {
            "Text", "Title", "Entry", "ReturnText", "Description", "Objective", "Guidance", "Opening", "Name"}}
    if isinstance(value, list):
        return [review_structure(v) for v in value]
    return value


def inventory(story):
    """Full authored inventory; native originals are not part of this export.

    Addresses are default ID seeds only. Reviewers retain semantic IDs when moving
    text and refresh its locator/digests. UI paths retain dictionary keys containing
    slashes and distinguish list indices from dictionary keys.
    """
    world = digest(review_structure({k: v for k, v in story.items() if k != "Scenes"}))
    scenes = {s["Id"]: digest(review_structure(s)) for s in story.get("Scenes", [])}
    for sid, location, text, speaker, kind, address in surface_records(story):
        if not isinstance(text, str) or not text:
            continue
        yield dict(surface_id="surface." + digest(address), address=address, text=text,
                   text_digest=text_digest(text), context_digest=digest(
                       [address, world, scenes.get(sid) if address["kind"] == "scene" else None]),
                   source_locator="export:" + json.dumps(address, ensure_ascii=False, sort_keys=True),
                   speaker=speaker)


DISCOVERY = {
    "reference": re.compile(r"\b(?:remember\w*|again|your mercy|the empty chair|what we agreed)\b", re.I),
    "knowledge": re.compile(r"\b(?:I saw|I heard|you told|she told|witness\w*)\b", re.I),
    "life-history": re.compile(r"\b(?:dead|died|alive|returned|rescue\w*)\b", re.I),
    "promise": re.compile(r"\b(?:promise\w*|owe\w*|will return|will come)\b", re.I),
}


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def load_registry(path=REGISTRY):
    """Reject ambiguous JSON rather than silently accepting the last binding."""
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=_unique_object,
                      parse_constant=lambda value: _invalid("non-JSON constant: " + value))


def _invalid(message):
    raise ValueError(message)


def _object(value, required, where, optional=()):
    if not isinstance(value, dict) or not set(required) <= value.keys() or value.keys() - set(required) - set(optional):
        _invalid(where + ": wrong fields (required " + ", ".join(required) + ")")


def _string(value, where):
    if not isinstance(value, str) or not value.strip():
        _invalid(where + ": expected nonempty string")


def _strings(value, where):
    if not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value) or len(value) != len(set(value)):
        _invalid(where + ": expected unique string list")


def _review(value, where):
    _object(value, ("reviewer", "disposition"), where)
    if value["disposition"] != "verified":
        _invalid(where + ": review is not verified")
    _string(value["reviewer"], where)


def _address(value):
    if not isinstance(value, dict):
        _invalid("address: expected object")
    if value.get("kind") == "scene":
        slot = value.get("slot")
        required = ["kind", "scene", "slot"]
        if slot in {"text", "paragraph", "choice"}:
            required.append("node")
        if slot in {"paragraph", "choice"}:
            required.append("index")
            if type(value.get("index")) is not int or value["index"] < 0:
                _invalid("address: invalid index")
        if slot not in {"entry", "Title", "ReturnText", "text", "paragraph", "choice"}:
            _invalid("address: unknown scene slot")
        _object(value, required, "address")
        for key in set(required) - {"index"}:
            _string(value[key], "address." + key)
    else:
        _object(value, ("kind", "path"), "address")
        if value["kind"] not in {"Books", "Journals", "Relationships", "Glossary", "Openers", "NativeTextEdits",
                                 "NativeAnswerEdits", "NativeWorldReconciliations", "ParentEpilogueEdits", "ParentEpilogueLossRules"}:
            _invalid("address: unknown text section")
        if not isinstance(value["path"], list) or not value["path"] or any(
                not (isinstance(p, str) and p or type(p) is int and p >= 0) for p in value["path"]):
            _invalid("address: invalid path")


def _validate_registry(story, registry, rows):
    """Validate metadata shape and foreign keys, without proving its semantics."""
    _object(registry, ("version", "scope", "surfaces", "facts", "claims", "obligations"), "registry")
    if type(registry["version"]) is not int or registry["version"] != 1 or registry["scope"] != "authored":
        _invalid("registry: unsupported version or scope")
    ids, tables = set(), {}
    for table, key in (("surfaces", "surface_id"), ("facts", "fact_id"), ("claims", "claim_id"), ("obligations", "obligation_id")):
        if not isinstance(registry[table], list):
            _invalid(table + ": expected list")
        tables[table] = {}
        for row in registry[table]:
            identity = row.get(key) if isinstance(row, dict) else None
            if not isinstance(identity, str) or not re.fullmatch(r"[a-z0-9][a-z0-9._:-]*", identity) or identity in ids:
                _invalid(table + ": invalid or duplicate stable ID")
            ids.add(identity)
            tables[table][identity] = row
    addresses = {digest(row["address"]): row for row in rows}
    if len(addresses) != len(rows):
        _invalid("inventory: duplicate exported address")
    reviewed_addresses = set()
    for row in tables["surfaces"].values():
        _object(row, ("surface_id", "address", "text_digest", "context_digest", "source_locator", "subjects", "claims", "review"), "surface")
        _address(row["address"])
        addr = digest(row["address"])
        if addr in reviewed_addresses or addr not in addresses:
            _invalid(row["surface_id"] + ": duplicate or missing exported address")
        reviewed_addresses.add(addr)
        for key in ("text_digest", "context_digest"):
            if not isinstance(row[key], str) or not re.fullmatch(r"[a-f0-9]{64}", row[key]):
                _invalid(row["surface_id"] + ": invalid " + key)
        _string(row["source_locator"], "source locator")
        _strings(row["subjects"], "surface subjects")
        _strings(row["claims"], "surface claims")
        _review(row["review"], "surface review")
    model = None
    if tables["facts"]:
        from tools.rrt_verify import Model
        # Model normalizes nodes in place. Keep registry checks read-only even
        # for small raw fixtures and exports not previously normalized.
        model = Model(copy.deepcopy(story))
    known = set(model.authored) | set(model.native) | set(model.derived) if model else set()
    def refs(values, table, where):
        _strings(values, where)
        if any(v not in tables[table] for v in values):
            _invalid(where + ": unknown " + table + " binding")
    def producer(value):
        if isinstance(value, dict) and set(value) == {"surface"}:
            refs([value["surface"]], "surfaces", "display producer")
        elif isinstance(value, dict) and set(value) == {"native", "evidence"}:
            if not model or value["native"] not in model.native:
                _invalid("producer: unknown native reader")
            _string(value["evidence"], "native producer evidence")
        else:
            _object(value, ("scene", "node", "choice"), "producer")
            nodes = model.nodes.get(value["scene"], {}) if model else {
                n["Id"]: n for s in story.get("Scenes", []) if s["Id"] == value["scene"] for n in s.get("Nodes", [])}
            node = nodes.get(value["node"])
            index = value["choice"]
            if not node or not (index == "enter" or type(index) is int and 0 <= index < len(node.get("Choices", []))):
                _invalid("producer: missing node or choice")
    for row in tables["facts"].values():
        _object(row, ("fact_id", "meaning", "time_scope", "subject", "predicate", "producers", "invalidators", "evidence", "review"), "fact")
        for key in ("meaning", "time_scope", "subject", "evidence"):
            _string(row[key], "fact." + key)
        groups = row["predicate"]
        if not isinstance(groups, list) or not groups:
            _invalid("fact predicate: expected OR of nonempty AND groups")
        for group in groups:
            _strings(group, "fact predicate group")
            if not group or any(flag.removeprefix("!") not in known for flag in group):
                _invalid("fact predicate: unknown engine flag or empty arm")
        if not isinstance(row["producers"], list) or not row["producers"]:
            _invalid("fact: missing producers")
        for source in row["producers"]:
            producer(source)
        _strings(row["invalidators"], "fact invalidators")
        if any(flag not in known for flag in row["invalidators"]):
            _invalid("fact: unknown invalidator")
        _review(row["review"], "fact review")
    for row in tables["claims"].values():
        _object(row, ("claim_id", "surface", "span", "speaker", "kind", "facts", "time_scope", "knowledge", "appearance", "statement", "exception", "review"), "claim")
        refs([row["surface"]], "surfaces", "claim surface")
        surface = tables["surfaces"][row["surface"]]
        text = addresses[digest(surface["address"])]["text"]
        span = row["span"]
        if not isinstance(span, list) or len(span) != 2 or any(type(i) is not int for i in span) or not 0 <= span[0] < span[1] <= len(text):
            _invalid("claim: invalid Unicode text span")
        for key in ("speaker", "time_scope"):
            _string(row[key], "claim." + key)
        if row["kind"] not in {"references", "states", "reacts_to"}:
            _invalid("claim: unknown kind")
        refs(row["facts"], "facts", "claim facts")
        if not row["facts"]:
            _invalid("claim: missing fact binding")
        knowledge = row["knowledge"]
        _object(knowledge, ("mode", "facts"), "knowledge")
        refs(knowledge["facts"], "facts", "knowledge facts")
        if knowledge["mode"] not in {"none", "witnessed", "reported"} or (knowledge["mode"] == "none") != (not knowledge["facts"]):
            _invalid("knowledge: missing or unexpected evidence binding")
        appearance = row["appearance"]
        _object(appearance, ("form", "subject", "facts"), "appearance")
        _string(appearance["subject"], "appearance subject")
        refs(appearance["facts"], "facts", "appearance facts")
        if appearance["form"] not in {"none", "body", "speech_now", "letter", "memory", "projection"} or appearance["form"] != "none" and not appearance["facts"]:
            _invalid("appearance: missing form/history binding")
        if row["statement"] is not None:
            _object(row["statement"], ("family", "value", "time_scope"), "statement")
            for key in ("family", "value", "time_scope"):
                _string(row["statement"][key], "statement." + key)
        if row["exception"] is not None:
            _object(row["exception"], ("kind", "reason", "facts"), "exception")
            if row["exception"]["kind"] not in {"lie", "hypothesis", "correction", "change_of_mind"}:
                _invalid("exception: unknown kind")
            _string(row["exception"]["reason"], "exception reason")
            refs(row["exception"]["facts"], "facts", "exception facts")
            if row["exception"]["kind"] in {"correction", "change_of_mind"} and not row["exception"]["facts"]:
                _invalid("exception: missing transition binding")
        _review(row["review"], "claim review")
    for surface in tables["surfaces"].values():
        refs(surface["claims"], "claims", "surface claims")
        actual = {c["claim_id"] for c in tables["claims"].values() if c["surface"] == surface["surface_id"]}
        if actual != set(surface["claims"]):
            _invalid("surface: claim span inventory disagrees with bindings")
    for row in tables["obligations"].values():
        _object(row, ("obligation_id", "trigger", "owed", "observer", "targets", "window", "cancellations", "fallback", "review"), "obligation")
        producer(row["trigger"])
        for key in ("owed", "observer"):
            _string(row[key], "obligation." + key)
        refs(row["targets"], "surfaces", "obligation targets")
        if not row["targets"]:
            _invalid("obligation: missing callback targets")
        _object(row["window"], ("delivery", "deadline"), "obligation window")
        if row["window"]["delivery"] not in {"immediate", "automatic", "player_optional"}:
            _invalid("obligation: unknown delivery mode")
        _string(row["window"]["deadline"], "obligation deadline")
        refs(row["cancellations"], "facts", "obligation cancellations")
        refs(row["fallback"], "surfaces", "obligation fallback")
        _review(row["review"], "obligation review")
    return tables


def check_registry(story, registry=None):
    rows = list(inventory(story))
    for row in rows:
        row["discovery_hints"] = [dict(kind=kind, span=[m.start(), m.end()], text=m.group())
                                  for kind, pattern in DISCOVERY.items() for m in pattern.finditer(row["text"])]
    hard, covered = [], set()
    try:
        registry = load_registry() if registry is None else registry
        tables = _validate_registry(story, registry, rows)
        reviews = {digest(row["address"]): row for row in tables["surfaces"].values()}
        for row in rows:
            review = reviews.get(digest(row["address"]))
            if review is None:
                row["status"] = "unreviewed"
            elif any(row[key] != review[key] for key in ("text_digest", "context_digest")):
                row["status"] = "stale"
                hard.append(review["surface_id"] + ": stale text/context review")
            else:
                row["status"] = "reviewed"
                row["surface_id"] = review["surface_id"]
                covered.add(digest(row["address"]))
        missing = sum(row["status"] == "unreviewed" for row in rows)
        if missing:
            hard.append("registry: %d unreviewed authored surfaces" % missing)
    except (ValueError, TypeError, KeyError, OSError) as exc:
        hard.append("registry: " + str(exc))
    return dict(hard=hard, inventory=rows, reviewed=len(covered), total=len(rows),
                complete=not hard, proof_status="not-evaluated")


def extract(story, registry=None):
    """Propose whole-surface reviews while retaining existing semantic identities.

    New/changed surfaces are pending. Removed addresses require explicit reviewed
    retirement and are retained as pending. No extraction creates fact bindings.
    """
    registry = load_registry() if registry is None else registry
    _object(registry, ("version", "scope", "surfaces", "facts", "claims", "obligations"), "registry")
    result = copy.deepcopy(registry)
    result["surfaces"] = []
    previous = {}
    for row in registry["surfaces"]:
        _address(row["address"])
        key = digest(row["address"])
        if key in previous:
            _invalid("extract: duplicate reviewed address")
        previous[key] = row
    for row in inventory(story):
        old = previous.pop(digest(row["address"]), None)
        proposal = {k: v for k, v in row.items() if k not in {"text", "speaker"}} | {
            "subjects": [], "claims": [], "review": {"reviewer": "", "disposition": "pending"}}
        if old:
            proposal.update({k: copy.deepcopy(old[k]) for k in ("surface_id", "source_locator", "subjects", "claims")})
            if all(old[k] == row[k] for k in ("text_digest", "context_digest")):
                proposal["review"] = copy.deepcopy(old["review"])
        result["surfaces"].append(proposal)
    for row in previous.values():
        old = copy.deepcopy(row)
        old["review"] = {"reviewer": "", "disposition": "pending"}
        result["surfaces"].append(old)
    return result


def check(story, contracts=None, registry=None):
    contracts = json.loads(CONTRACTS.read_text(encoding="utf-8")) if contracts is None else contracts
    scenes = {s["Id"]: s for s in story["Scenes"]}
    hard, executed, absent = [], [], []
    for contract in contracts:
        sid, target, gone = contract["scene"], contract["node"], contract["gone"]
        if sid not in scenes:
            if contract.get("optional_absent"):
                absent.append(sid)
                continue
            hard.append(sid + ": missing callback host")
            continue
        nodes = {n["Id"]: n for n in scenes[sid]["Nodes"]}
        key = sid + "/" + target
        original, gap = nodes.get(target), nodes.get("gap." + target)
        incoming = {(n["Id"], i) for n in nodes.values() for i, c in enumerate(n["Choices"]) if target in targets(c)}
        if incoming != {tuple(v) for v in contract["vias"]}:
            hard.append(key + ": incoming callback contract drift")
        if not original or not gap or structural(gap["Choices"]) != structural(original["Choices"]):
            hard.append(key + ": missing gap or changed continuation")
            continue
        twin = scenes.get(contract["twin"], {})
        twin_gap = next((n for n in twin.get("Nodes", []) if n["Id"] == "gap." + target), {})
        if (twin or not contract.get("optional_twin_absent")) and (structural(twin_gap.get("Choices")) != structural(gap["Choices"])):
            hard.append(key + ": twin gap drift")
        for via, index in contract["vias"]:
            original_choice = nodes.get(via, {}).get("Choices", [])[index]
            alternatives = [c for c in nodes[via]["Choices"] if c.get("Next") == "gap." + target]
            incoming_indices = [i for node_id, i in contract["vias"] if node_id == via]
            # Appended copies follow the incoming answer indices, even when effects match.
            ordinal = incoming_indices.index(index)
            expected = {**original_choice, "Next": "gap." + target,
                        "Requires": list(dict.fromkeys(original_choice.get("Requires", []) + ["trickster.ever", gone])),
                        "Forbids": [f for f in original_choice.get("Forbids", []) if f != gone]}
            if (gone not in original_choice.get("Forbids", []) or len(alternatives) != len(incoming_indices)
                    or ordinal >= len(alternatives) or structural(expected) != structural(alternatives[ordinal])):
                hard.append(key + ": unguarded incoming choice " + via + "[%d]" % index)
            else:
                executed.append(dict(scene=sid, via=via, index=index, sold_node=gap["Id"], unsold_node=original["Id"]))
    review = [dict(scene=sid, location=location, code="vision-justification", start=m.start(), end=m.end(), match=m.group())
              for sid, location, text, _, _ in surfaces(story) for m in PATTERNS["vision-justification"].finditer(text)]
    callback_hard = sorted(set(hard))
    consistency = check_registry(story, registry)
    if consistency["hard"]:
        hard.append("narrative registry: " + "; ".join(consistency["hard"]))
    return dict(hard=sorted(set(hard)), callback_hard=callback_hard, executed=executed,
                no_change_needed=absent, review=review, consistency=consistency)


def main():
    import argparse
    import sys
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("story", type=Path)
    parser.add_argument("--registry", type=Path, default=REGISTRY)
    parser.add_argument("--mode", choices=("check", "report", "extract"), default="check")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    story = json.loads(args.story.read_text(encoding="utf-8-sig"))
    try:
        registry = load_registry(args.registry)
        result = extract(story, registry) if args.mode == "extract" else check_registry(story, registry)
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(json.dumps({"hard": [str(exc)], "complete": False}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(args.mode == "check" and bool(result["hard"]))


if __name__ == "__main__":
    raise SystemExit(main())

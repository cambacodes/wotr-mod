"""Generate authored milestone test metadata from the integrated export, never story content.

Missing ix-a/ix-b contracts remain explicit failing cases. Regenerate after their integration.
Fixtures supply prerequisite leaves; they do not certify the campaign earned those leaves.
"""
import argparse
from collections import deque
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IX_A = ["targona.trickster.react.ix_a.yaniel", *(
    "iomedae.trickster.react.ix_a." + suffix
    for suffix in ("galfrey.queen", "galfrey.crown", "galfrey.kitrane", "targona", "yaniel")), *(
    "yaniel.trickster.react.ix_a.galfrey." + suffix for suffix in ("queen", "crown", "kitrane"))]
IX_B = [*("gesmerha.react.soana." + truth + "." + ruler + "." + bear
           for truth in ("truth", "illusions") for ruler in ("marhevok", "chief") for bear in ("lost", "orso")),
        *("aranka.react.arueshalae." + branch + yard
          for branch in ("fallen", "dreamer") for yard in ("", ".yard")),
        "nenio.react.fallen_arueshalae.scholar", "nenio.react.fallen_arueshalae.replacement"]


def answer_path(scene, effect=None, skip=0):
    """Shortest explicit terminal path, retaining original choice identities; no hidden-answer fallback."""
    nodes = {n["Id"]: n for n in scene["Nodes"]}
    queue = deque([(scene["Nodes"][0]["Id"], [], False, set(scene.get("Requires", [])), set(scene.get("Forbids", [])), set())])
    while queue:
        key, path, earned, required, banned, produced = queue.popleft()
        if len(path) > len(nodes):
            continue
        for index, choice in enumerate(nodes[key]["Choices"]):
            if choice.get("Abort") or choice.get("Check") or choice.get("Revive"):
                continue
            needs = set(choice.get("Requires", [])) - produced
            forbids = set(choice.get("Forbids", []))
            if needs & banned or forbids & (required | produced) or needs & forbids:
                continue
            next_required, next_banned = required | needs, banned | forbids
            next_produced = produced | set(choice.get("Set", []))
            walk = [*path, (key, index)]
            has_effect = earned or effect in choice.get("Set", [])
            if choice.get("Next") is None:
                if effect is None or has_effect:
                    if skip == 0:
                        return [scene["Id"] + "/" + node + "/" + str(i) for node, i in walk]
                    skip -= 1
            elif choice["Next"] in nodes:
                if choice["Next"] not in {node for node, _ in walk}:
                    queue.append((choice["Next"], walk, has_effect, next_required, next_banned, next_produced))
    raise ValueError("No scripted terminal path for " + scene["Id"] + ": " + str(effect))


def generate(story):
    scenes = {s["Id"]: s for s in story["Scenes"]}
    derived = story.get("Derived", {})
    cases = []

    def seeds(keys, blocked):
        result = set()
        denied = set(blocked)

        def add(key, stack=()):
            if key in denied:
                return False
            if key in derived:
                if key in stack:
                    return False
                denied.update(story.get("DerivedForbids", {}).get(key, []))
                if result & denied:
                    return False
                for group in derived[key]:
                    old = result.copy()
                    old_denied = denied.copy()
                    if all(add(k, (*stack, key)) for k in group):
                        return True
                    result.clear()
                    result.update(old)
                    denied.clear()
                    denied.update(old_denied)
                return False
            result.add(key)
            return True

        for key in keys:
            if not add(key):
                raise ValueError("Unsatisfiable fixture prerequisite " + key)
        return result

    def case(system, sid, chapter, effect=None, extra=(), suffix="", attempt=0):
        scene = scenes.get(sid)
        if scene is None:
            cases.append(dict(Id=system + "/" + sid + suffix, System=system, Chapter=chapter,
                              SaveChapter=3 if chapter == 3 else 6, Steps=[dict(Scene=sid)]))
            return None
        reply = None
        played_effect = effect
        if sid == "kiana.morning" and effect == "kiana.partner_stance.share":
            played_effect = "kiana.partner_early.share_sent"
            reply = scenes[sid + ".elan_reply"]
        script = answer_path(scene, played_effect, attempt)
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        selected = [nodes[a.rsplit("/", 2)[1]]["Choices"][int(a.rsplit("/", 1)[1])] for a in script]
        blocked = set(scene.get("Forbids", [])) | {sid}
        blocked.update(f for c in selected for f in c.get("Forbids", []))
        keys = [*scene.get("Requires", []), *extra]
        for group in [scene.get("RequiresAny", []), *scene.get("RequiresAnyGroups", [])]:
            if group:
                keys.append(next(k for k in group if k not in blocked))
        for rel in scene.get("Participants", []):
            keys.append(rel + ".harem.eligible")
        for woman in scene.get("ParticipantWomen", []):
            keys.extend(story["SeatWomen"][woman]["Requires"])
        produced = set()
        for choice in selected:
            keys.extend(f for f in choice.get("Requires", []) if f not in produced)
            produced.update(choice.get("Set", []))
        try:
            flags = seeds(keys, blocked)
        except ValueError:
            if attempt >= 64:
                raise
            return case(system, sid, chapter, effect, extra, suffix, attempt + 1)
        # Check derived branch guards as well as direct guards. Effects can invalidate a composite during the walk.
        live = set(flags)
        for choice in selected:
            held = live - set(derived)
            for _ in range(len(derived)):
                added = {key for key, groups in derived.items() if key not in held
                         and any(set(group) <= held for group in groups)
                         and not any(flag in held for flag in story.get("DerivedForbids", {}).get(key, []))}
                if not added:
                    break
                held.update(added)
            if not set(choice.get("Requires", [])) <= held or set(choice.get("Forbids", [])) & held:
                if attempt >= 64:
                    raise ValueError("No stable derived branch script for " + sid)
                return case(system, sid, chapter, effect, extra, suffix, attempt + 1)
            live.update(choice.get("Set", []))
        step = dict(Scene=sid, Answers=script, ExpectFlags=sorted(produced))
        if scene.get("InteractionHub") == "household.table":
            step["Table"] = True
        if scene.get("RestAllowance"):
            step["ExpectRestSpent"] = {scene["RestAllowance"]: 1}
        value = dict(Id=system + "/" + sid + suffix, System=system, Chapter=chapter,
                     SaveChapter=3 if chapter == 3 else 6, FixtureFlags=sorted(flags), Steps=[step])
        if reply is not None:
            reply_script = answer_path(reply, effect)
            reply_nodes = {n["Id"]: n for n in reply["Nodes"]}
            reply_flags = {flag for a in reply_script
                           for flag in reply_nodes[a.rsplit("/", 2)[1]]["Choices"][int(a.rsplit("/", 1)[1])].get("Set", [])}
            value["Steps"].append(dict(Scene=reply["Id"], Answers=reply_script,
                                       ExpectFlags=sorted(reply_flags)))
        cases.append(value)
        return value

    # Pair production and read-only W5 readers share the actual outcome from the scripted deed.
    pair = "household.pair.seelah_nenio.question"
    current = "household.readers.w5.s10.seating"
    ledger = next(e for e in story["Books"]["trickster.ledger"]["Entries"] if e["Id"] == current)
    c = case("pair-w5", pair, 5, "household.pair.seelah_nenio.question.answered", ledger["Requires"])
    c["Steps"].insert(0, dict(Scene=pair, Table=True, Available=False, Remove=["foresight.page_taken", "trickster.foresight.accepted"]))
    c["Steps"].insert(1, dict(Scene=pair, Table=True, Available=False, Add=["seelah.closed"]))
    c["Steps"].insert(2, dict(Scene=pair, Table=True, Available=False, Remove=["trickster"]))
    c["Steps"].insert(3, dict(Scene=pair, Table=True, Available=False, Add=["seelah_dead"]))
    for succeeded in (False, True):
        c["Steps"].insert(3, dict(Scene=pair, Table=True, Available=succeeded, ProbeOnly=True,
                                 RestSpent={"household.pair": 1}, RestSucceeded=succeeded))
    c["Steps"].append(dict(Scene=pair, Available=False, Table=True, LedgerEntries=[current]))
    c["Steps"].append(dict(Scene=pair, Available=False, Add=["seelah.closed"], HiddenLedgerEntries=[current]))
    c["Steps"].append(dict(Scene=pair, Available=False, Add=["sacrifice"], HiddenLedgerEntries=[current]))
    for row, sid in (("s20", "jannah.circle.seelah"), ("s21", "household.pair.seelah_yaniel.watch"),
                     ("s29", "household.pair.seelah_kiana.ward"), ("s30", "household.pair.eliandra_targona.charges")):
        current = "household.readers.w5." + row + ".seating"
        ledger = next(e for e in story["Books"]["trickster.ledger"]["Entries"] if e["Id"] == current)
        reading = case("pair-w5", sid, 5, extra=ledger["Requires"])
        reading["Steps"].append(dict(Scene=sid, Available=False, LedgerEntries=[current]))
    case("household-pairs", "household.pair.seelah_wenduag.spar", 5)
    case("household-pairs", "household.pair.delamere_hepzamirah.open", 5)
    case("w4-ensemble", "household.ensemble.ch3.supper", 3, "household.ensemble.ch3.supper.seen")
    case("w4-knowledge", "household.knowledge.nenio_seelah", 3, "household.knowledge.nenio_seelah.seen")

    # Every implemented stance value uses its real terminal effect, including a legitimate exclusive refusal.
    sid = "anevia.a_key_that_is_hers"
    for stance in ("share", "exclusive", "secret"):
        case("partner-stance", sid, 5, "anevia.partner_stance." + stance, suffix="/" + stance)
    # Sweep the other stance producers by effect identity, not by prose or visible answer order.
    effects = sorted({flag for s in scenes.values() if not s["Owner"].endswith("Epilogue")
                      for n in s["Nodes"] for choice in n["Choices"] for flag in choice.get("Set", [])
                      if re.search(r"\.partner_stance\.(share|exclusive|secret)$", flag)
                      and not flag.startswith("anevia.")})
    for effect in effects:
        candidates = [s for s in scenes.values() if not s["Owner"].endswith("Epilogue")
                      and s["MinChapter"] >= 3 and s["MinChapter"] <= 6
                      and any(effect in choice.get("Set", []) for n in s["Nodes"] for choice in n["Choices"])]
        candidates.sort(key=lambda s: (s["MinChapter"] < 5, s.get("ContactUnit") is not None, bool(s.get("Areas"))))
        for candidate in candidates:
            try:
                extra = ("soana.partner.corven_separated", "soana.partner.corven_known_alive") if effect == "soana.partner_stance.exclusive" else ()
                case("partner-stance", candidate["Id"], candidate["MinChapter"], effect, extra, suffix="/" + effect.rsplit(".", 1)[1])
                break
            except ValueError:
                continue
        else:
            raise ValueError("No bounded stance script for " + effect)
    call = case("lastcall", "anevia.lastcall.call", 6)
    call["Steps"].insert(0, dict(Scene="anevia.lastcall.call", Available=False,
                                Remove=["anevia.trickster.cost.socoth_listening", "anevia.trickster.cost.stolen_door",
                                        "anevia.trickster.cost.wrong_door"]))
    call["Steps"].insert(1, dict(Scene="anevia.lastcall.call", Available=False, Add=["anevia.closed"]))
    call["Steps"].insert(2, dict(Scene="anevia.lastcall.call", Available=False, Remove=["trickster"]))
    entitlement = case("lastcall-entitlement", "trickster.lastcall.last_joke", 6, "trickster.lastcall.taken")
    entitlement["Steps"].insert(0, dict(Scene="trickster.lastcall.last_joke", Available=False, Add=["anevia.trickster.cost.socoth_listening"]))
    for sid in IX_A:
        case("ix-a", sid, 5)
    for sid in IX_B:
        scene = scenes.get(sid)
        case("ix-b", sid, max(3, scene["MinChapter"]) if scene else 5)
    return dict(Schema=1, Cases=cases)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    parser.add_argument("--out", type=Path, default=ROOT / "harness/system-scenarios.json")
    args = parser.parse_args()
    result = generate(json.loads(args.story.read_text(encoding="utf-8")))
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    missing = [c["Id"] for c in result["Cases"] if "FixtureFlags" not in c]
    print(f"{len(result['Cases'])} scenarios; {len(missing)} missing integrated scene contracts")


if __name__ == "__main__":
    main()

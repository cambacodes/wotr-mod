"""Advisory CHARACTER-TRUTH / EDGE screen; never a prose quality verdict.

Run against a fresh expansion export. Counts include all alternatives, retired
scenes and generated clones, not a selected playthrough. No SAT reachability or
native-rate claim is made. Review context, selfish motives, canon exceptions,
victim confrontations and acts manually using edge_rubric_row.md.

--strict enforces ONLY frozen displayed text for explicitly locked scene IDs.
voice_locks.json accepts a list of IDs or {"scenes": [IDs]}; after approved
rewrites its optional scene_text_sha256 map freezes the new text, retaining
the original before-numbers in edge_baseline.json.
--write-baseline is an explicit coordinator operation, never run implicitly.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PACKS = ROOT / "tools/route_packs"
WORD = re.compile(r"\b[^\W\d_]+(?:['’][^\W\d_]+)?\b", re.UNICODE)


def terms(pattern):
    return re.compile(r"\b(?:" + pattern + r")\b", re.I)


PATTERNS = {
    "business": terms(r"accounts?|accounting|agents?|reports?|fees?|terms|clauses?|signatures?|negotia\w*|contracts?|ledgers?|receipts?|invoices?|bookkeep\w*|commissions?|counterfoils?|guarantors?|cargo weights|settlements?"),
    "menace": terms(r"kill\w*|eat|eaten|devour\w*|blood\w*|throats?|teeth|slav\w*|scream\w*|kniv\w*|knife|tortur\w*|flay\w*|murder\w*|punish\w*|cruel\w*|humiliat\w*|dominat\w*"),
    "profanity": terms(r"fuck\w*|shit\w*|bitch\w*|whores?|bastards?|damn\w*|cunts?|assholes?|arseholes?|son of a bitch"),
    "exit": terms(r"the door(?: is open| works)?|you (?:may|can|could) (?:also |always )?(?:go|leave|decline|refuse|stop|say no)|you (?:need not|do not have to|don['’]t have to) (?:stay|come|answer)|room to move|(?:leav\w*|left) (?:you )?room|come closer if you want|if you want|nobody(?:['’]s| is) holding you here|opening the door is still your choice|you need not keep proving that you could have left|her own side remains open|you may stop inviting me|nothing in the letter makes either of you answer|without turning the ending into a test|I will stop waiting for an invitation|knock first"),
    "therapy_clinic": terms(r"therap\w*|clinic\w*|doctors?|patients?|prescriptions?|intake|relapse\w*|discharg\w*|doses?|dosage|case notes|quacks?|diagnos\w*|treatment|medical condition|permission|consent|boundar(?:y|ies)|ask first|may I kiss|earlier affection|each movement answered rather than assumed|somebody else carried half|not what you(?:['’]re| are) measuring|before you (?:reach for|touch|kiss) me|tell me if this is where you want to be"),
    "modern_ethics": terms(r"rights?|dignity|deserv\w*|honest\w*|consent|refus\w*|grateful|autonomy|restitut\w*|reparations?|address her rather than|I will tell you when they conflict"),
    "moral_authority": terms(r"may I|I(?:['’]m| am) asking you|say which|(?:you|Commander)[^.!?\n]{0,70}(?:permission|allow|approve|decide whether|say whether)|(?:if|when) you (?:permit|allow|approve)|tell me (?:if|whether)[^.!?\n]{0,60}(?:kill|spare|want)|I (?:will|shall)[^.!?\n]{0,55}if you (?:wish|want|say)|because you (?:did not|didn['’]t|do not|don['’]t) want me to|shared burden"),
    "tenderness": terms(r"as if by accident|does not let go|doesn['’]t let go|stays there|something crosses her face(?: and is gone)?|for (?:one|a) heartbeat|her shoulder(?: comes to rest)? against yours"),
}
EVIL_SPEAKERS = {"Nocticula", "Jerribeth", "Minagho", "Chivarro", "Hepzamirah",
                 "Melazmera", "Areelu", "Camellia", "Wenduag", "Shamira", "Vellexia",
                 "Nurah", "Devarra", "Herrax", "Horzalah"}


def layer(scene):
    sid = scene["Id"]
    if sid.startswith("arueshalae.") and {"fallen", "evil"}.intersection(re.split(r"[._]", sid)):
        return "fallen"
    if sid.startswith(("noct.acq.", "noct.join.")):
        return "acquisition"
    if ".trickster." in sid:
        return "trickster"
    return "base"


def surfaces(scene):
    """Displayed scene fields only; never count IDs, flags or mechanics."""
    for key in ("Title", "Entry"):
        yield key.lower(), "Narrator", "ui", scene.get(key, "")
    for node in scene.get("Nodes", []):
        nid, speaker = node["Id"], node.get("Speaker", "Narrator")
        yield nid, speaker, "node", node.get("Text", "")
        for i, paragraph in enumerate(node.get("Paragraphs", [])):
            yield f"{nid}/paragraph/{i}", speaker, "paragraph", paragraph.get("Text", "")
        for i, choice in enumerate(node.get("Choices", [])):
            yield f"{nid}/choice/{i}", "Commander", "choice", choice.get("Text", "")


def text_hash(scene):
    # Includes locations and speaker attribution, but no story gates/flags.
    value = json.dumps([surface for surface in surfaces(scene) if surface[-1]],
                       ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def narration_spans(text):
    return [(m.start(), m.end()) for m in re.finditer(r"\{n\}[\s\S]*?(?:\{/n\}|$)", text)]


def stock_phrase(text):
    """Combine grammatical variants without altering quoted evidence."""
    phrase = text.lower().replace("’", "'")
    phrase = phrase.replace("doesn't", "does not").replace("for a heartbeat", "for one heartbeat")
    phrase = phrase.replace(" comes to rest", "").removesuffix(" and is gone")
    return phrase


def mouth_review(register, words, count):
    """Only qualitative mismatches supported by the supplied targets."""
    return bool(words and ((register == "zero" and count > 0)
                           or (register in {"foul", "occasional"} and count == 0)))


def check(story, targets):
    """Return deterministic per-relationship/layer counts and exact evidence."""
    buckets, findings = {}, []
    women = defaultdict(Counter)
    repeated = defaultdict(set)
    for scene in story.get("Scenes", []):
        route = scene.get("Relationship") or "unassigned"
        band = layer(scene)
        key = (route, band)
        row = buckets.setdefault(key, dict(route=route, layer=band, scenes=0, words=0,
                                         counts=Counter(), speaker_profanity=Counter(), speaker_words=Counter()))
        row["scenes"] += 1
        for location, speaker, kind, text in surfaces(scene):
            row["words"] += len(WORD.findall(re.sub(r"\{[^}]*\}", "", text)))
            spans = narration_spans(text)
            for code, regex in PATTERNS.items():
                for match in regex.finditer(text):
                    narrated = any(a <= match.start() < b for a, b in spans)
                    voice = "Narrator" if narrated else speaker
                    if code in {"exit", "moral_authority"} and kind == "choice":
                        continue
                    if code == "modern_ethics" and (kind not in {"node", "paragraph"}
                            or narrated or (speaker not in EVIL_SPEAKERS
                            and not (speaker == "Arueshalae" and band == "fallen"))):
                        continue
                    row["counts"][code] += 1
                    if code == "profanity" and kind in {"node", "paragraph"} and not narrated:
                        row["speaker_profanity"][speaker] += 1
                        women[speaker]["profanity"] += 1
                    if code == "tenderness":
                        repeated[stock_phrase(match.group())].add(route)
                    findings.append(dict(route=route, layer=band, scene=scene["Id"],
                        location=location, speaker=voice, kind=kind, code=code,
                        match=match.group(), start=match.start(), end=match.end(),
                        quote=text[max(0, match.start() - 120):match.end() + 120]))
            if kind in {"node", "paragraph"}:
                speech = re.sub(r"\{n\}[\s\S]*?(?:\{/n\}|$)", "", text)
                speech_words = len(WORD.findall(re.sub(r"\{[^}]*\}", "", speech)))
                women[speaker]["words"] += speech_words
                row["speaker_words"][speaker] += speech_words
    rows = []
    for key, row in sorted(buckets.items()):
        counts = {code: row["counts"][code] for code in PATTERNS}
        business, menace = counts["business"], counts["menace"]
        row.update(counts=counts, speaker_profanity=dict(sorted(row["speaker_profanity"].items())),
            speaker_words=dict(sorted(row["speaker_words"].items())),
            rates_per_10000={code: round(count * 10000 / row["words"], 3) if row["words"] else 0
                             for code, count in counts.items()},
            business_to_menace=round(business / menace, 3) if menace else None,
            business_exceeds_menace=business > menace)
        rows.append(row)
    profanity = []
    for name, target in sorted(targets["women"].items()):
        words, count = women[name]["words"], women[name]["profanity"]
        per_layer = []
        for row in rows:
            own_words = row["speaker_words"].get(name, 0)
            if not own_words:
                continue
            own_count = row["speaker_profanity"].get(name, 0)
            register = target.get("layer_registers", {}).get(row["layer"], target["register"])
            per_layer.append(dict(route=row["route"], layer=row["layer"], register=register,
                words=own_words, count=own_count,
                rate_per_10000=round(own_count * 10000 / own_words, 3),
                review=mouth_review(register, own_words, own_count)))
        profanity.append(dict(woman=name, target=target, words=words, count=count, layers=per_layer,
            rate_per_10000=round(count * 10000 / words, 3) if words else 0,
            review=mouth_review(target["register"], words, count)))
    totals = []
    for route in sorted({row["route"] for row in rows}):
        own = [row for row in rows if row["route"] == route]
        counts = {code: sum(row["counts"][code] for row in own) for code in PATTERNS}
        words = sum(row["words"] for row in own)
        totals.append(dict(route=route, scenes=sum(row["scenes"] for row in own), words=words,
            counts=counts, rates_per_10000={code: round(count * 10000 / words, 3) if words else 0
                                          for code, count in counts.items()},
            business_to_menace=round(counts["business"] / counts["menace"], 3) if counts["menace"] else None,
            business_exceeds_menace=counts["business"] > counts["menace"]))
    return dict(schema=1, route_totals=totals, routes=rows, findings=findings, profanity=profanity,
                repeated_tenderness=[dict(phrase=phrase, routes=sorted(routes))
                                    for phrase, routes in sorted(repeated.items()) if len(routes) > 1])


def baseline(story, report, revision):
    return dict(schema=1, source_revision=revision,
        scope="All exported alternatives, clones and retired scenes; not playthrough counts.",
        route_totals=report["route_totals"], routes=report["routes"], profanity=report["profanity"],
        repeated_tenderness=report["repeated_tenderness"],
        scene_text_sha256={s["Id"]: text_hash(s) for s in story.get("Scenes", [])})


def locked_regressions(story, frozen, locks):
    """Structural changes are free; locked displayed text is frozen verbatim."""
    ids = locks if isinstance(locks, list) else locks["scenes"]
    current = {s["Id"]: text_hash(s) for s in story.get("Scenes", [])}
    before = {**frozen.get("scene_text_sha256", {}),
              **(locks.get("scene_text_sha256", {}) if isinstance(locks, dict) else {})}
    return [dict(scene=sid, code="locked-text-regression",
                 reason="missing baseline" if sid not in before else
                        "missing scene" if sid not in current else "displayed text changed")
            for sid in sorted(set(ids)) if sid not in before or current.get(sid) != before[sid]]


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    parser.add_argument("--targets", type=Path, default=PACKS / "voice/profanity_targets.json")
    parser.add_argument("--baseline", type=Path, default=PACKS / "edge_baseline.json")
    parser.add_argument("--locks", type=Path, default=PACKS / "voice_locks.json")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--write-baseline", action="store_true")
    parser.add_argument("--revision", default="unspecified", help="baseline provenance revision")
    parser.add_argument("--json", type=Path, help="write full quoted evidence as UTF-8 JSON")
    parser.add_argument("--summary", action="store_true", help="omit individual quotes on stdout")
    args = parser.parse_args(argv)
    if args.strict and args.write_baseline:
        parser.error("strict cannot refresh its own baseline")
    story = load(args.story)
    report = check(story, load(args.targets))
    if args.write_baseline:
        args.baseline.write_text(json.dumps(baseline(story, report, args.revision),
                                           ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    failures = []
    if args.strict and args.locks.exists():
        failures = locked_regressions(story, load(args.baseline), load(args.locks))
    report["hard_failures"] = failures
    if args.json:
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("EDGE advisory screen: exported alternatives include clones; human review required.")
    for row in report["routes"]:
        print(f"{row['route']} / {row['layer']}: {row['scenes']} scenes, {row['words']} words; "
              f"counts={row['counts']}; business:menace={row['business_to_menace']} "
              f"(business exceeds menace={row['business_exceeds_menace']})")
    for row in report["profanity"]:
        print(f"MOUTH {row['woman']}: {row['count']} own-speech hits / {row['words']} words, "
              f"target={row['target']['register']}; review={row['review']}")
        for band in row["layers"]:
            print(f"  {band['route']}/{band['layer']}: {band['count']} own-speech hits, "
                  f"target={band['register']}; review={band['review']}")
    for row in report["repeated_tenderness"]:
        print(f"REPEATED {row['phrase']!r}: {', '.join(row['routes'])}")
    if not args.summary:
        for row in report["findings"]:
            print(f"REVIEW {row['code']} {row['route']}/{row['layer']} "
                  f"{row['scene']}:{row['location']} ({row['speaker']}): "
                  f"{json.dumps(row['quote'], ensure_ascii=False)} [match={row['match']!r}]")
    for failure in failures:
        print(f"HARD {failure['scene']}: {failure['reason']}")
    print(f"EDGE: {len(failures)} hard failures")
    return int(args.strict and bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())

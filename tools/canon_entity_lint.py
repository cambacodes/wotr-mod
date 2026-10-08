"""Read-only, heuristic entity inventory for a freshly exported Story.json.

CANON means lexical attestation in game localization, not proof of a lore claim.
Blueprint display-name references supply additional provenance; internal asset
filenames never whitelist names. UNKNOWN is a review candidate, not a verdict.
Claim support is directional and sentence-local. Missing evidence is advisory:
localization is not an exhaustive setting encyclopedia. No network/NLP dependency.
"""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
WORD = r"(?:[A-ZÀ-ÖØ-Þ][a-zà-öø-ÿ]+|[A-ZÀ-ÖØ-Þ]{2,})(?:[-’'][A-Za-zÀ-ÿ]+)*"
NAME = rf"(?:Lady|Lord)\s+in\s+{WORD}|{WORD}(?:\s+(?:(?:of|the)\s+)*{WORD})*"
NAMES = re.compile(NAME)
# Closed-class words and common dialogue imperatives are not entities. This is
# deliberately fixed, rather than learning an allowlist from the mod being linted.
COMMON = set("I You Your Yours We Our Ours They Their Theirs He His Him She Her Hers It Its My Mine Me Us Them Who What When Where Why How Which This That These Those A An The And Or But Nor For So If Then As At By From To Of In On With Without Into Out Yes No Not Now Here There Well Perhaps Maybe Please Thank Thanks Good Bad Very More Less All Any Some Each Every Both Neither Either One Two Three First Second Third Last Next Once Again Still Even Only Just Also Too Can Could May Might Must Shall Should Will Would Do Does Did Is Are Was Were Be Been Have Has Had Let Look Listen Tell Take Keep Come Go Get Make Give Stop Wait Sit Stand Leave Speak Ask Say See Think Remember Enough Nothing Something Everything Anything Nobody Somebody Everyone Anyone Never Always Today Tonight Tomorrow Yesterday Before After Until Since During Through While Whether Though Because Unless Despite Fine Really Surely Sorry Welcome Careful Indeed Commander Narrator Flirt Lie Intimidate Diplomacy Bluff Knowledge Perception Athletics Stealth Mobility Lore Arcana World Religion Nature Continue End Return Read Open Close Accept Refuse Agree Decline Attack Kiss Embrace Stay Touch Hold Reach Draw Turn Find Bring Show Put Send Pay Choose Check Offer Explain Promise Try Meet Watch Follow Call Hear Feel Allow Use".split())
COMMON_FOLDED = {word.casefold() for word in COMMON}
# Fixed lexical exclusions, never learned from route text. Keep unknown proper
# names even at sentence starts; do not discard every capitalized -ly word.
COMMON_FOLDED.update("afterwards afterward ordinarily meanwhile normally occasionally usually otherwise already almost rather sometimes suddenly finally properly loudly halfway whenever face landlady about farther half old fund paperwork copying bucket annoyingly recognizing recorded accurate acceptable calculations clerks treasury captain lieutenant sergeant soldier clerk servant rent retired fold folded withdraw finances late supper limp news behind".split())
COMMON_FOLDED.update("abominably accurately admirably astonishingly bitterly briefly brightly cheerfully coldly considerably convincingly crisply critically curtly drily embarrassingly enormously fiercely flatly fondly genuinely grudgingly immensely indirectly irritatingly likely lonely marginally openly painfully partly permanently poorly privately productively reasonably reluctantly repeatedly reply rigorously scientifically serenely sharply steadily successfully temporarily truthfully weekly wonderingly cap'n name's home's".split())
CONTRACTION = re.compile(r"(?i)^(?:i|you|we|they|he|she|it|that|there|who|what|could|would|should|had|has|have|did|does|do|was|were|is|are|can|must|will|won|shan)(?:['’](?:ve|ll|re|d|s)|n['’]t)$")
KIN = r"brother|sister|mother|father|daughter|son|wife|husband|aunt|uncle|cousin|lover|consort"
REL = rf"(?:{KIN}|queen|king|lord|lady|priest|priestess|captain|ruler)"
FIELDS = {"Text", "Title", "Description", "Objective", "Guidance", "Opening", "Name", "Entry", "Speaker"}


def plain(text):
    # Keep display branches and hyperlink labels, discard engine keys/tags.
    text = re.sub(r"\{(?:g|d)\|[^}]*\}", "", text)
    text = re.sub(r"\{mf\|([^}]*)\}", lambda m: m[1].replace("|", " / "), text)
    return re.sub(r"\{[^}]*\}|<[^>]*>", "", text)


def entities(text):
    """Retain sentence-initial unknowns too, and connector-bearing titles."""
    for match in NAMES.finditer(plain(text)):
        words = match[0].split()
        while words and (words[0].casefold() in COMMON_FOLDED or CONTRACTION.fullmatch(words[0])):
            words.pop(0)
        while words and (words[-1].casefold() in COMMON_FOLDED or CONTRACTION.fullmatch(words[-1])):
            words.pop()
        if words:
            name = " ".join(words)
            # Possession and contracted auxiliaries aren't part of identity.
            yield re.sub(r"[’'](?:s|ll|ve|re|d)$", "", name)


def surfaces(story):
    """Walk all displayed fields, not only reachable dialogue nodes.

    Metadata (flags, IDs, owner labels, evidence/reasons) is excluded. Displayed
    NPC speaker names are included even if the dialogue never names its speaker.
    Route comes from explicit Relationship, inherited by nested UI entries.
    """
    def walk(value, path, route="shared", speaker="Narrator"):
        if isinstance(value, dict):
            route = value.get("Relationship", route)
            speaker = value.get("Speaker", speaker)
            for key, child in value.items():
                address = f"{path}/{key}"
                if key in FIELDS and isinstance(child, str) and child:
                    yield dict(route=route, address=address, speaker=speaker, text=child)
                elif isinstance(child, (dict, list)):
                    # Relationship UI keys are route IDs, not prose.
                    child_route = key if path == "Relationships" else route
                    yield from walk(child, address, child_route, "Commander" if key == "Choices" else speaker)
        elif isinstance(value, list):
            for i, child in enumerate(value):
                ident = child.get("Id", str(i)) if isinstance(child, dict) else str(i)
                yield from walk(child, f"{path}/{ident}", route, speaker)
    for key, value in story.items():
        yield from walk(value, key)


def claims(text, speaker="Narrator"):
    """Extract explicit and possessive kinship plus 'the X of Y' titles.

    'her sister' remains unresolved: guessing its antecedent would invent
    evidence. First-person claims bind only to an explicit NPC speaker.
    """
    text = plain(text).replace("’", "'")
    atom = rf"{WORD}(?:\s+{WORD})*"
    patterns = [
        (rf"(?P<subject>{atom})\s+(?:or|and)\s+(?:her|his)\s+(?P<relation>{KIN})\s+(?P<target>{atom})", "coordinated"),
        (rf"(?P<target>{atom})\s+(?:is|was)\s+(?P<subject>{atom})'s\s+(?P<relation>{REL})\b", "named"),
        (rf"(?P<target>{atom}),\s+(?P<subject>{atom})'s\s+(?P<relation>{REL})\b", "appositive"),
        (rf"(?P<target>{atom})\s+(?:is|was)\s+(?:the\s+)?(?P<relation>{REL})\s+of\s+(?P<subject>{atom})", "relation-of"),
        (rf"(?P<target>{atom})(?:,|\s+(?:is|was))\s+the\s+(?P<relation>{REL}|{WORD}(?:\s+{WORD})*)\s+of\s+(?:the\s+)?(?P<subject>{atom})", "named-title"),
        (rf"(?P<subject>{atom})'s\s+(?P<relation>{REL})\b(?:,?\s+(?:(?:named|called)\s+)?(?P<target>{atom}))?", "possessive"),
        (rf"\b(?P<pronoun>(?i:my|your|her|his|their|our))\s+(?:(?:dear|beloved|late|elder|younger|older|little|loathsome)\s+)?(?P<relation>{KIN})\b(?:,?\s+(?:(?:named|called)\s+)?(?P<target>{atom}))?", "pronoun"),
        (rf"\b[Tt]he\s+(?P<relation>{REL}|{WORD}(?:\s+{WORD})*)\s+of\s+(?:the\s+)?(?P<subject>{atom})", "title"),
    ]
    seen = set()
    for pattern, kind in patterns:
        for match in re.finditer(pattern, text):
            row = match.groupdict()
            if kind == "relation-of" and row.get("target") in {"He", "She"}:
                # A lore entry with one prior named entity has an unambiguous
                # local antecedent (e.g. Socothbenoth's glossary definition).
                prior = set(entities(text[:match.start()]))
                row["target"] = next(iter(prior)) if len(prior) == 1 else None
            if kind == "pronoun":
                # Ignore case only on pronouns; a lowercase target isn't a name.
                target = row.get("target")
                row["target"] = target if target and NAMES.fullmatch(target) else None
                row["subject"] = speaker if row["pronoun"].lower() == "my" and speaker not in {"Narrator", "Commander"} else None
            row = {k: v for k, v in row.items() if k != "pronoun"}
            for field in ("subject", "target"):
                if row.get(field):
                    row[field] = next(entities(row[field]), None)
            identity = (row.get("subject"), row["relation"].lower(), row.get("target"))
            if identity in seen:
                continue
            seen.add(identity)
            yield dict(row, relation=row["relation"].lower(), kind=kind, claim=match[0])


class Canon:
    def __init__(self, localization, blueprints):
        data = json.loads(Path(localization).read_text(encoding="utf-8-sig"))
        self.strings = data.get("strings", data)
        self.names = defaultdict(list)
        self.claims = defaultdict(list)
        self.genders = {}
        for key, value in self.strings.items():
            if not isinstance(value, str):
                continue
            for name in set(entities(value)):
                # Also index subnames of longer phrases, with the same citation.
                parts = name.split()
                for start in range(len(parts)):
                    for end in range(start + 1, min(len(parts), start + 8) + 1):
                        part = " ".join(parts[start:end])
                        if parts[start][0].isupper() and parts[end-1][0].isupper():
                            evidence = self.names[part.casefold()]
                            if len(evidence) < 3:
                                evidence.append(dict(key=key, text=value[:600]))
            for row in claims(value):
                if row.get("subject"):
                    identity = self.identity(row)
                    if len(self.claims[identity]) < 3:
                        self.claims[identity].append(dict(key=key, text=value))
        self.blueprints = defaultdict(list)
        units = {}
        with zipfile.ZipFile(blueprints) as archive:
            for info in archive.infolist():
                # Display names from units, areas, factions, and deities. Do not
                # mistake cue IDs or programmer filenames for canon entities.
                if not info.filename.endswith((".jbp", ".json")) or not info.filename.startswith(("Units/", "World/Areas/", "Kingdom/", "Deities/", "Root/")):
                    continue
                record = json.loads(archive.read(info))
                data = record.get("Data", record)
                for field in ("m_DisplayName", "DisplayName", "m_AreaName", "Name", "LocalizedName"):
                    ref = data.get(field)
                    if not isinstance(ref, dict):
                        continue
                    key = ref.get("m_Key", ref.get("Key", ref.get("stringkey")))
                    label = self.strings.get(key, "")
                    if info.filename.startswith("Units/") and field == "LocalizedName" and label:
                        units[record.get("AssetId")] = label
                    for name in entities(label):
                        if data.get("Gender") in {"Female", "Male"}:
                            self.genders[name.casefold()] = data["Gender"]
                        bucket = self.blueprints[name.casefold()]
                        if len(bucket) < 3:
                            bucket.append(dict(path=info.filename, guid=record.get("AssetId"), key=key))
            # Bind native first-person kinship to the cue's actual unit, never
            # to a guessed narration antecedent or an internal asset filename.
            for info in archive.infolist():
                if not info.filename.startswith("World/Dialogs/") or not info.filename.endswith((".jbp", ".json")):
                    continue
                record = json.loads(archive.read(info))
                data = record.get("Data", record)
                ref = data.get("Speaker", {}).get("m_Blueprint")
                speaker = units.get(ref.removeprefix("!bp_")) if isinstance(ref, str) else None
                text_ref = data.get("Text")
                if not speaker or not isinstance(text_ref, dict):
                    continue
                key = text_ref.get("m_Key")
                value = self.strings.get(key, "")
                for row in claims(value, speaker):
                    if row.get("subject"):
                        bucket = self.claims[self.identity(row)]
                        if len(bucket) < 3:
                            bucket.append(dict(key=key, text=value, path=info.filename, guid=record.get("AssetId")))
        # A localized full unit name permits its unambiguous given-name alias.
        aliases = defaultdict(set)
        for name in self.genders:
            aliases[name.split()[0]].add(name)
        def variants(name):
            result = {name}
            first = name.split()[0] if name else ""
            if name in aliases.get(first, set()) and len(aliases[first]) == 1:
                result.add(first)
            elif name in self.names and first in self.genders and len(aliases[first]) == 1:
                result.add(first)
            return result
        for identity, evidence in list(self.claims.items()):
            subject, relation, target = identity
            if not subject or not target or relation not in KIN.split("|"):
                continue
            for owner in variants(subject):
                for relative in variants(target):
                    self.claims[(owner, relation, relative)] = evidence
                    if relation in {"brother", "sister", "wife", "husband"}:
                        gender = self.genders.get(subject, self.genders.get(owner))
                        reverse = ("sister" if gender == "Female" else "brother") if relation in {"brother", "sister"} else ("wife" if gender == "Female" else "husband")
                        if gender:
                            self.claims[(relative, reverse, owner)] = evidence

    @staticmethod
    def identity(row):
        return tuple((row.get(k) or "").casefold() for k in ("subject", "relation", "target"))

    def evidence(self, name):
        return dict(localization=self.names.get(name.casefold(), []), blueprints=self.blueprints.get(name.casefold(), []))


def validate_registry(registry, root=ROOT):
    names = set()
    for row in registry.get("entities", []):
        if not all(row.get(key) for key in ("name", "role", "source", "introducing_text", "introducing_route")):
            raise ValueError("Registry entries require name, role, source, introducing_text, introducing_route")
        path = (root / row["source"]).resolve()
        if not path.is_relative_to(root.resolve()) or not row["source"].startswith("storylines/"):
            raise ValueError(f"Invalid registry source: {row['source']}")
        text = path.read_text(encoding="utf-8-sig")
        if row["introducing_text"] not in text or row["name"] not in row["introducing_text"]:
            raise ValueError(f"Registry evidence missing: {row['name']}")
        for name in [row["name"], *row.get("aliases", [])]:
            folded = name.casefold()
            if folded in names:
                raise ValueError(f"Duplicate registry entity: {name}")
            names.add(folded)


def check(story, canon, registry):
    registered = {name.casefold(): row for row in registry.get("entities", []) for name in [row["name"], *row.get("aliases", [])]}
    routes = defaultdict(lambda: dict(entities=[], claims=[]))
    count = 0
    for surface in surfaces(story):
        count += 1
        text = surface["text"]
        base = {k: surface[k] for k in ("address", "speaker")}
        for name in sorted(set(entities(text))):
            evidence = canon.evidence(name)
            entry = registered.get(name.casefold())
            if entry and entry.get("introducing_route") != surface["route"]:
                entry = None
            category = "CANON" if any(evidence.values()) else "MOD" if entry else "UNKNOWN"
            routes[surface["route"]]["entities"].append(dict(base, name=name, classification=category, evidence=evidence if category == "CANON" else entry, excerpt=text[:600]))
        for row in claims(text, surface["speaker"]):
            supported = canon.claims.get(canon.identity(row), []) if row.get("subject") else []
            if row.get("subject") and not row.get("target"):
                # An unnamed brother claim needs existence evidence, not a
                # fabricated identity for that brother.
                supported = [e for identity, evidence in canon.claims.items()
                             if identity[:2] == canon.identity(row)[:2] for e in evidence][:3]
            canon_subject = any(any(canon.evidence(row[k]).values()) for k in ("subject", "target") if row.get(k))
            status = "SUPPORTED" if supported else "UNSUPPORTED_CANON_CLAIM" if canon_subject else "UNRESOLVED" if not row.get("subject") else "MOD_OR_UNKNOWN_CLAIM"
            routes[surface["route"]]["claims"].append(dict(base, **row, status=status, evidence=supported, excerpt=text[:600]))
    unknowns = sum(row["classification"] == "UNKNOWN" for r in routes.values() for row in r["entities"])
    return dict(schema_version=1, surfaces_scanned=count, unknown_occurrences=unknowns, routes=dict(sorted(routes.items())))


def markdown(report, top=12):
    lines = ["# Canon entity inventory", "", "Fresh export; read-only lexical/claim review. CANON attests a name, not its surrounding lore. UNKNOWN may include ordinary capitalized prose. Unsupported claims require human review; absence is not contradiction. Pronoun antecedents are not guessed.", "", f"Scanned {report['surfaces_scanned']} text surfaces; {report['unknown_occurrences']} UNKNOWN occurrences.", ""]
    for route, data in report["routes"].items():
        unknown = defaultdict(list)
        for row in data["entities"]:
            if row["classification"] == "UNKNOWN":
                unknown[row["name"]].append(row)
        unsupported = [r for r in data["claims"] if r["status"] == "UNSUPPORTED_CANON_CLAIM"]
        lines += [f"## {route}", "", f"UNKNOWN: {len(unknown)} distinct / {sum(map(len, unknown.values()))} occurrences; unsupported canon claims: {len(unsupported)}.", ""]
        for name, rows in sorted(unknown.items(), key=lambda item: (-len(item[1]), item[0]))[:top]:
            lines.append(f"- UNKNOWN **{name}** ({len(rows)}): `{rows[0]['address']}`")
        grouped_claims = {}
        for row in unsupported:
            grouped_claims.setdefault((row.get("subject"), row["relation"], row.get("target")), row)
        for row in list(grouped_claims.values())[:top]:
            claim = row['claim'].replace('\n', ' ')
            lines.append(f"- UNSUPPORTED: {claim} (subject: {row.get('subject')}; target: {row.get('target') or 'unnamed'}) — `{row['address']}`")
        if not unknown and not unsupported:
            lines.append("No findings in these two classes.")
        lines.append("")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json", help="Fresh expansion.py export (caller regenerates it)")
    parser.add_argument("--localization", type=Path, default=Path("/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json"))
    parser.add_argument("--blueprints", type=Path, default=Path("/wrath/blueprints.zip"))
    parser.add_argument("--registry", type=Path, default=ROOT / "tools/route_packs/mod_entities.json")
    parser.add_argument("--json", type=Path, help="Write full JSON; otherwise stdout")
    parser.add_argument("--markdown", type=Path, help="Write per-route top findings")
    parser.add_argument("--strict", action="store_true", help="Nonzero on every UNKNOWN not in registry")
    args = parser.parse_args(argv)
    try:
        registry = json.loads(args.registry.read_text(encoding="utf-8-sig"))
        validate_registry(registry)
        report = check(json.loads(args.story.read_text(encoding="utf-8-sig")), Canon(args.localization, args.blueprints), registry)
        report["inputs"] = {k: str(getattr(args, k)) for k in ("story", "localization", "blueprints", "registry")}
        payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.json:
            args.json.write_text(payload, encoding="utf-8")
        else:
            print(payload, end="")
        if args.markdown:
            args.markdown.write_text(markdown(report), encoding="utf-8")
        return 1 if args.strict and report["unknown_occurrences"] else 0
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"canon-entity-lint: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

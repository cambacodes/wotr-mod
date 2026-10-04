"""eng7-l09: review diagnostics for player text, never an automatic prose rewrite."""
import json
from pathlib import Path
import re

EXCEPTIONS = Path(__file__).with_name("player_text_exceptions.json")


def surfaces(story):
    """Yield only displayed text, including conditional paragraphs and Book/journal text."""
    for scene in story.get("Scenes", []):
        sid = scene["Id"]
        yield sid, "entry", scene.get("Entry", ""), scene.get("Owner", "Narrator"), "entry"
        for node in scene.get("Nodes", []):
            nid = node["Id"]
            yield sid, nid, node.get("Text", ""), node.get("Speaker", "Narrator"), "node"
            for i, para in enumerate(node.get("Paragraphs", [])):
                yield sid, nid + "/paragraph/%d" % i, para.get("Text", ""), node.get("Speaker", "Narrator"), "paragraph"
            for i, choice in enumerate(node.get("Choices", [])):
                yield sid, nid + "/choice/%d" % i, choice.get("Text", ""), "Commander", "choice"
    def extra(value, path):
        if isinstance(value, dict):
            for key, child in sorted(value.items()):
                if key in {"Text", "Title", "Description", "Objective", "Guidance", "Opening", "Name"} and isinstance(child, str):
                    yield path, key, child, "Narrator", "ui"
                elif isinstance(child, (dict, list)):
                    yield from extra(child, path + "/" + key)
        elif isinstance(value, list):
            for i, child in enumerate(value):
                yield from extra(child, path + "/%d" % i)
    for section in ("Books", "Journals", "Relationships", "Glossary"):
        yield from extra(story.get(section, {}), section)


PATTERNS = {
    "embedded-commander-speech": re.compile(r'(?:["”][^\n]{0,40}\b(?:you (?:say|tell|ask|reply|answer|suggest)|the Commander (?:says|asks|replies))\b|\byou (?:say|tell|ask|reply|answer|suggest)\b[^\n]{0,60}["“])', re.I),
    "tooling-residue": re.compile(r'\b(?:mod(?: romance)?|handler|observer|manuscript|registered caller|native (?!born\b)|parent (?:portrait|ending)|book-event|hidden (?:romance )?penalt\w*|implementation|teleport behavior|live inventory|game verification|(?:existing|verified) ending|route reachability|encounter-result|continuation|[a-z_]+\.[a-z_]+\.[a-z_.]+)\b', re.I),
    "commander-gender": re.compile(r'\bCommander\b[^.!?\n]{0,160}\b(?:he|him|his)\b|\b(?:he|him|his)\b[^.!?\n]{0,160}\bCommander\b', re.I),
    "vision-justification": re.compile(r'\b(?:a vision (?:showed|told)|another life|another playthrough|save file|the player)\b', re.I),
}
THERAPY = re.compile(r'\b(?:permission|consent|boundar(?:y|ies)|you may refuse|ask first|may I kiss|earlier affection)\b', re.I)


def check(story, exceptions=None, draft=False):
    policy = json.loads(EXCEPTIONS.read_text()) if exceptions is None else exceptions
    rows, counts = [], {}
    for sid, location, text, speaker, kind in surfaces(story):
        for term in THERAPY.finditer(text):
            route = sid.split("/")[1] if sid.startswith("Relationships/") else sid.split(".")[0].split("_")[0]
            counts[route] = counts.get(route, 0) + 1
        for code, regex in PATTERNS.items():
            if code == "embedded-commander-speech" and kind in {"choice", "entry"}:
                continue
            searched = re.sub(r'\{mf\|[^}]+\}', lambda m: " " * len(m.group()), text) if code == "commander-gender" else text
            for match in regex.finditer(searched):
                if any(e["scene"] == sid and e["location"] == location and e["code"] == code
                       and e["match"] == match.group() and e.get("reason") for e in policy.get("exceptions", [])):
                    continue
                rows.append(dict(scene=sid, location=location, code=code, start=match.start(), end=match.end(),
                                 match=text[match.start():match.end()], draft=draft, severity="review"))
        # A standalone reply between two spoken lines may be an unselected
        # Commander turn. Attribution is a human decision, not a voice verdict.
        if kind in {"node", "paragraph"}:
            for match in re.finditer(r'(?m)^[ \t]*"[^"\n]+"[ \t]*$', text):
                before = text[:match.start()].rstrip().splitlines()
                after = text[match.end():].lstrip("\r\n").splitlines()
                while after and after[0].strip().startswith("{n}") and after[0].strip().endswith("{/n}"):
                    after.pop(0)
                if before and after and before[-1].lstrip().startswith('"') and after[0].lstrip().startswith('"'):
                    rows.append(dict(scene=sid, location=location, code="speaker-attribution-review", start=match.start(),
                                     end=match.end(), match=match.group(), draft=draft, severity="review"))
    rows = [row for row in rows if not any(e["scene"] == row["scene"] and e["location"] == row["location"]
            and e["code"] == row["code"] and e["match"] == row["match"] and e.get("reason")
            for e in policy.get("exceptions", []))]
    budgets = policy.get("therapy_budgets", {})
    return dict(review=rows, therapy_counts=counts, therapy_budgets=budgets,
                therapy_warnings=[dict(route=route, count=count, budget=budgets.get(route, 0))
                                  for route, count in sorted(counts.items()) if count > budgets.get(route, 0)])

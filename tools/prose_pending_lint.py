#!/usr/bin/env python3
"""Validate integration placeholders or signed held scaffold targets; forbid both at milestones."""
import argparse
from pathlib import Path
import re

try:
    from . import voice_authority as authority
except ImportError:
    import voice_authority as authority

ROOT = Path(__file__).resolve().parents[1]
MARKER = re.compile(r"prose[ _-]pending|\bplaceholder\b", re.I)


def text_surfaces(story):
    for scene in story.get("Scenes", []):
        for node in scene.get("Nodes", []):
            yield (scene["Id"], node["Id"], "node", None), node.get("Text", "")
            for field, surface in (("Paragraphs", "paragraph"), ("Choices", "choice")):
                for index, item in enumerate(node.get(field, [])):
                    yield (scene["Id"], node["Id"], surface, index), item.get("Text", "")


def check(story, data, job=None, milestone=False, integration=False):
    """Validate schema, exact text targets, registration and held-job authority."""
    if (not isinstance(data, dict) or set(data) != {"version", "pending"}
            or type(data["version"]) is not int or data["version"] != 1
            or not isinstance(data["pending"], list)):
        raise ValueError("invalid prose-pending schema")
    targets = {}
    for key, text in text_surfaces(story):
        targets.setdefault(key, []).append(text)
    registered, errors = set(), []
    for entry in data["pending"]:
        if (not isinstance(entry, dict) or set(entry) != {"scene", "node", "surface", "index", "text_sha"}
                or not isinstance(entry["scene"], str) or not entry["scene"].strip()
                or not isinstance(entry["node"], str) or not entry["node"].strip()
                or entry["surface"] not in ("node", "paragraph", "choice")
                or (entry["surface"] == "node" and entry["index"] is not None)
                or (entry["surface"] != "node" and
                    (type(entry["index"]) is not int or entry["index"] < 0))
                or not authority.valid_sha(entry["text_sha"])):
            raise ValueError("invalid prose-pending target schema")
        key = tuple(entry[field] for field in ("scene", "node", "surface", "index"))
        if key in registered:
            errors.append(f"{key}: duplicate prose-pending target")
        registered.add(key)
        matches = targets.get(key, [])
        if len(matches) != 1 or authority.digest(matches[0]) != entry["text_sha"]:
            errors.append(f"{key}: missing/ambiguous/stale prose-pending target")
        elif not MARKER.search(matches[0]):
            errors.append(f"{key}: pending target has no placeholder marker")
    for key, matches in targets.items():
        if any(MARKER.search(text) for text in matches) and key not in registered:
            errors.append(f"{key}: unregistered prose placeholder")
    if registered:
        if milestone:
            errors.append("milestone builds forbid prose-pending entries")
        elif not integration and (not job or (job["kind"], job["status"]) != ("scaffold", "held")):
            errors.append("placeholders require a signed held scaffold job")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--story", type=Path)
    parser.add_argument("--job", type=Path)
    parser.add_argument("--milestone", action="store_true")
    parser.add_argument("--integration", action="store_true", help="allow exact registered integration placeholders")
    args = parser.parse_args(argv)
    root = args.repo.resolve()
    story_path = args.story or root / "development/Story.json"
    try:
        base, policy, _ = authority.trusted(root)
        job = authority.verify_job(root, story_path, args.job, policy, base) if args.job else None
        path = root / authority.PENDING
        data = authority.read_json(path) if path.exists() else {"version": 1, "pending": []}
        errors = check(authority.read_json(story_path), data, job, args.milestone, args.integration)
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors = [str(error)]
    for error in errors:
        print("HARD Prose pending:", error)
    print(f"Prose pending: {len(errors)} hard failures")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())

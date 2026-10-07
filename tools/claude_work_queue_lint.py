#!/usr/bin/env python3
"""Validate Claude work requests separately from exact placeholder targets."""
import argparse
from pathlib import Path

try:
    from .voice_authority import read_json
except ImportError:
    from voice_authority import read_json

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "tools/route_packs/plans/claude-work-queue.json"


def check(data):
    if not isinstance(data, list):
        return ["work queue must be a list"]
    errors = []
    required = {"scene", "woman", "beat", "ruling"}
    allowed = required | {"node", "choice", "why", "finding", "dependency"}  # audit finding id, motivation, blocking dependency
    for index, entry in enumerate(data):
        if (not isinstance(entry, dict) or not required <= set(entry) <= allowed
                or any(not isinstance(entry.get(k), str) or not entry[k].strip()
                       for k in ("scene", "woman", "beat"))
                or "node" in entry and (not isinstance(entry["node"], str) or not entry["node"].strip())
                or not (isinstance(entry.get("ruling"), str) and entry["ruling"].strip()
                        or type(entry.get("ruling")) is int and entry["ruling"] > 0)
                or "choice" in entry and ("node" not in entry or type(entry["choice"]) is not int
                                           or entry["choice"] < 0)):
            errors.append(f"request {index}: invalid work request schema")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, default=QUEUE)
    args = parser.parse_args(argv)
    try:
        errors = check(read_json(args.queue))
    except (OSError, ValueError) as error:
        errors = [str(error)]
    for error in errors:
        print("HARD Claude work queue:", error)
    print(f"Claude work queue: {len(errors)} hard failures")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())

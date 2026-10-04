"""eng7-l04: validate the Q3 adapter contract before publishing an export.

Only adapter/schema parity; q6a L1-L6 remain responsible for cross-route lints.
The arrays are read from Rules (also used by Main.Load), never copied here.
"""
from functools import lru_cache
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


@lru_cache(maxsize=1)
def requirements():
    source = (ROOT / "src/Story.cs").read_text(encoding="utf-8-sig")
    def array(name):
        body = source.split(" " + name + " =", 1)[1].split("};", 1)[0]
        return tuple(re.findall(r'"([^"\n]+)"', body))
    return array("Q3RecoveryFullOutcomes"), array("Q3RecoveryPartialRequirements")


def supported(group):
    full, partial = requirements()
    return isinstance(group, list) and all(isinstance(flag, str) for flag in group) and "trickster.now" in group and (
        any(flag in group for flag in full) or all(flag in group for flag in partial))


def check(payload):
    gate = payload.get("NativeGates", {}).get("kiana.q3_recovery")
    if gate is None:
        return []
    if (not isinstance(gate, dict) or gate.get("Target") != "2b4a5c01a192d1f4aa8c9d32aa149727"
            or gate.get("Relationship") != "kiana" or not gate.get("When")
            or any(not supported(group) for group in gate["When"])):
        return ["NG14: invalid kiana.q3_recovery; expected reviewed target, Kiana, current Trickster and full paid outcome or returned+guests_robbed"]
    return []


def validate(payload):
    failures = check(payload)
    if failures:
        raise ValueError("\n".join(failures))


if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("story", type=Path)
    failures = check(json.loads(parser.parse_args().story.read_text(encoding="utf-8-sig")))
    for failure in failures:
        print(failure)
    raise SystemExit(bool(failures))

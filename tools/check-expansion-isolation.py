"""Verify repeated authoring builds do not mutate imported scene templates."""
import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from expansion import make_expansion

first = make_expansion()
frozen = copy.deepcopy(first)
second = make_expansion()
assert first == frozen == second, "Repeated assembly changed an earlier result."
first["Scenes"][-1]["Nodes"][0]["Text"] = "Mutation isolation probe"
assert make_expansion() == second, "Returned scenes share mutable authoring templates."
print("PASS: repeated assembly and returned scene mutation isolation")

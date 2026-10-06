"""eng8-q8g: every declared history witness is enforced, including negative receipts."""
import copy
import json
from pathlib import Path
import unittest

from tools.lastcall_entitlement_lint import CONTRACTS, errors, history_errors

ROOT = Path(__file__).resolve().parents[1]


class LastCallHistoryInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8"))
        cls.contracts = json.loads(CONTRACTS.read_text(encoding="utf-8"))
        # Keep the complete definition tables and all inventoried producers;
        # unrelated scene graphs are irrelevant to these targeted mutations.
        ids = {r["surface"][0] for r in cls.contracts["surfaces"]}
        ids.update(r["scene"] for r in cls.contracts["producers"])
        cls.fixture = {**cls.story, "Scenes": [s for s in cls.story["Scenes"] if s["Id"] in ids]}

    def test_shipped_surfaces_and_all_thirteen_findings(self):
        self.assertEqual(len(self.contracts["findings"]), 13)
        self.assertEqual(errors(self.story), [])

    def test_removing_each_declared_historical_witness_fails(self):
        # Remove the witness from all effective local contexts and Derived
        # definitions: a redundant entry guard must not conceal the mutation.
        def remove(value, keys):
            if isinstance(value, dict):
                for field, item in value.items():
                    if field in ("Requires", "Forbids", "RequiresAny", "RequiresAnyGroups", "AnyGroups", "OpenWhen", "SettledWhen"):
                        value[field] = strip(item, keys)
                    else:
                        remove(item, keys)
            elif isinstance(value, list):
                for item in value:
                    remove(item, keys)

        def strip(value, keys):
            if isinstance(value, list):
                return [strip(v, keys) for v in value if not isinstance(v, str) or v.lstrip("!") not in keys]
            return value

        mutations = 0
        for row in self.contracts["surfaces"]:
            clauses = [{key} for key in row.get("requires", []) + row.get("forbids", [])]
            clauses += [set(group) for group in row.get("any_groups", [])]
            for keys in clauses:
                with self.subTest(surface=row["surface"], witness=sorted(keys)):
                    mutant = copy.deepcopy(self.fixture)
                    remove(mutant, keys)
                    for field in ("Derived", "DerivedForbids"):
                        for key, groups in mutant.get(field, {}).items():
                            mutant[field][key] = strip(groups, keys)
                    result = history_errors(mutant, {"surfaces": [row]})
                    self.assertTrue(any("lacks its declared witness" in f or "surface is impossible" in f for f in result), result)
                    mutations += 1
        self.assertGreater(mutations, 60)

    def test_generic_called_cannot_become_a_release_reader(self):
        mutant = copy.deepcopy(self.fixture)
        mutant["Derived"]["kiana.lastcall.guests_recovered"].append(["kiana.lastcall.called"])
        self.assertTrue(any("recovery reader differs" in f for f in history_errors(mutant)))

    def test_release_and_pardon_producers_are_enforced(self):
        for producer in self.contracts["producers"]:
            for receipt in producer["sets"]:
                with self.subTest(producer=producer, receipt=receipt):
                    mutant = copy.deepcopy(self.fixture)
                    host = next(s for s in mutant["Scenes"] if s["Id"] == producer["scene"])
                    node = next(n for n in host["Nodes"] if n["Id"] == producer["node"])
                    node["Choices"][producer["choice"]]["Set"].remove(receipt)
                    self.assertTrue(any("receipt missing" in f for f in history_errors(mutant)))

    def test_old_continue_cannot_be_reenabled(self):
        mutant = copy.deepcopy(self.fixture)
        host = next(s for s in mutant["Scenes"] if s["Id"] == "kiana.lastcall.call")
        host["Nodes"][0]["Choices"][0]["Requires"].remove("kiana.sunhammer_dead")
        self.assertTrue(any("generic settlement is not retired" in f for f in history_errors(mutant)))


if __name__ == "__main__":
    unittest.main()

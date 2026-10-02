"""Harem schedule lint (doc 16 section 8c.2): the shipped data passes, and each class of defect is caught."""
import copy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import harem_schedule_lint as lint  # noqa: E402

DATA = lint.load_json(lint.DEFAULT_DATA)


def errors(data, story=None):
    return lint.lint(data, story, None)[0]


def entry(data, ref):
    return next(e for e in data["schedule"] if e["ref"] == ref)


def candidate(data, cid):
    return next(c for c in data["candidates"] if c["id"] == cid)


class ShippedData(unittest.TestCase):
    def test_clean(self):
        self.assertEqual(errors(DATA), [])

    def test_doc11_parser_matches_snapshot(self):
        text = "## 3. Friction registry input\n\n| New woman | Pair | Root |\n|---|---|---|\n" + "".join(
            "| %s | %s | x |\n" % (a, ", ".join(b)) for a, b in DATA["doc11_rows"]) + "\n## 4. Next\n"
        self.assertEqual(lint.parse_doc11(text), DATA["doc11_rows"])
        self.assertEqual(len(lint.expand(DATA["doc11_rows"])), 48)


class Defects(unittest.TestCase):
    def setUp(self):
        self.d = copy.deepcopy(DATA)

    def test_missing_candidate(self):
        self.d["candidates"].pop(5)
        self.assertTrue(any(e.startswith("K1") for e in errors(self.d)))

    def test_obligation_demoted_to_cordial(self):
        c = candidate(self.d, "C29")
        c.update({"class": "cordial", "row": None, "kind": None})
        self.assertTrue(any("C29" in e and e.startswith("K3") for e in errors(self.d)))

    def test_dangling_protection(self):
        candidate(self.d, "C01")["protection"] = ["S99"]
        self.assertTrue(any("S99" in e for e in errors(self.d)))

    def test_arueshalae_without_positive_key(self):
        entry(self.d, "S44").pop("keys")
        self.assertTrue(any("S44" in e and e.startswith("K4") for e in errors(self.d)))

    def test_count_drift(self):
        self.d["expected_counts"]["consolidated"] = 40
        self.assertTrue(any("consolidated" in e for e in errors(self.d)))

    def test_rejected_packet(self):
        self.d["packets"][0]["children"] += ["S08", "S44"]
        errs = errors(self.d)
        self.assertTrue(any("rejected" in e for e in errs))
        self.assertTrue(any("P5" in e for e in errs))   # Arueshalae children never ride in a packet

    def test_iomedae_in_packet(self):
        self.d["packets"][2]["children"].append("S40")
        self.assertTrue(any("Iomedae" in e for e in errors(self.d)))

    def test_conditional_child_in_packet(self):
        self.d["packets"][1]["children"].append("S52")
        self.assertTrue(any("conditional" in e for e in errors(self.d)))

    def test_child_in_two_packets(self):
        self.d["packets"][1]["children"].append("S23")
        self.assertTrue(any("two packets" in e for e in errors(self.d)))

    def test_short_recovery_delay(self):
        entry(self.d, "S02")["recovery"]["delay_hours"] = 24
        self.assertTrue(any("48" in e for e in errors(self.d)))

    def test_unknown_read(self):
        rels = lint.load_json(ROOT / "development" / "Story.json")["Relationships"]
        story = {"Scenes": [], "Relationships": rels}
        errs = errors(self.d, story)
        self.assertTrue(any(e.startswith("K6") and "kaylessa.unmasked" in e for e in errs))
        self.assertFalse(any(e.startswith("K5") for e in errs))


class RulesWalk(unittest.TestCase):
    def setUp(self):
        self.by_ref = {e["ref"]: e for e in DATA["schedule"]}
        self.k3 = next(p for p in DATA["packets"] if p["id"] == "K3")

    def facts(self, women, refs, absent=()):
        return ({"trickster", "KEPT"} | {"O:" + r for r in refs} | {"T:" + r for r in refs} | {"aged:" + r for r in refs}
                | {"A:" + w for w in women if w not in absent} | {"E:" + w for w in women})

    def test_p4_chivarro_absent(self):
        refs = self.k3["children"]
        women = {w for r in refs for w in self.by_ref[r]["women"]}
        f = self.facts(women, refs, absent=("chivarro",))
        self.assertFalse(lint.packet_available(self.k3, self.by_ref, f, {}, []))
        self.assertTrue(lint.singleton_available(self.by_ref["S48"], f, {}))
        self.assertFalse(lint.singleton_available(self.by_ref["S23"], f, {}))

    def test_p3_enmity_withdraws_packet_only(self):
        refs = self.k3["children"]
        women = {w for r in refs for w in self.by_ref[r]["women"]}
        f = self.facts(women, refs)
        self.assertTrue(lint.packet_available(self.k3, self.by_ref, f, {}, []))
        self.assertFalse(lint.packet_available(self.k3, self.by_ref, f, {}, [frozenset(("herrax", "minagho"))]))
        self.assertTrue(all(lint.singleton_available(self.by_ref[r], f, {}) for r in refs))

    def test_p11_acknowledgment_without_accused(self):
        e = self.by_ref["S47"]
        self.assertTrue(lint.acknowledgment_available(e, {"trickster", "O:S47", "A:yaniel"}))


if __name__ == "__main__":
    unittest.main()

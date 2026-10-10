"""Partner decisions use earned route gates and preserve native marriage state."""
import copy
from tests.structure import without_prose
import unittest
from itertools import zip_longest
from storylines import irabeth_independent
from storylines import irabeth_partner_stance as stance

def walk(book, flags=(), entry=None):
    nodes = {node["Id"]: node for node in book["Nodes"]}
    pending = [(entry or book["Nodes"][0]["Id"], frozenset(flags))]
    seen = set()
    endings = []
    while pending:
        node, state = pending.pop()
        if (node, state) in seen:
            continue
        seen.add((node, state))
        selectable = [c for c in nodes[node]["Choices"]
                      if set(c["Requires"]) <= state and not set(c["Forbids"]) & state]
        if not selectable:
            raise AssertionError("No answer at " + node)
        for answer in selectable:
            after = state | frozenset(answer["Set"])
            if answer.get("Next"):
                pending.append((answer["Next"], after))
            else:
                endings.append(after)
    return endings

class IrabethPartnerStanceTests(unittest.TestCase):

    def setUp(self):
        self.books = copy.deepcopy(irabeth_independent.SCENES)
        self.baseline = copy.deepcopy(self.books)
        stance.commitments(self.books)
        self.road = next(b for b in self.books if b["Id"] == "irabeth.a_road_she_would_choose")
        self.battle = next(b for b in self.books if b["Id"] == "irabeth.the_hour_before_battle")
        stance.discovery(self.battle)

    def test_existing_choices_keep_indices_and_destinations(self):
        for old, new in zip(self.baseline, self.books):
            self.assertEqual(old["Id"], new["Id"])
            self.assertEqual(old["Requires"], new["Requires"])
            self.assertEqual(old["Forbids"], new["Forbids"])
            for before, after in zip(old["Nodes"], new["Nodes"]):
                self.assertEqual(before["Id"], after["Id"])
                self.assertTrue(all(new is not None for old, new in zip_longest(before["Choices"], after["Choices"]) if old is not None))
                for left, right in zip(before["Choices"], after["Choices"]):
                    self.assertEqual(left.get("Next"), right.get("Next"))
                    self.assertTrue(set(left["Set"]) <= set(right["Set"]))
        frozen = copy.deepcopy(self.books)
        stance.commitments(self.books)
        self.assertEqual(without_prose(frozen), without_prose(self.books))

    def test_share_secret_and_refused_exclusive(self):
        ends = walk(self.road, entry="lasting")
        self.assertTrue(any(stance.SHARE in s and "irabeth.committed" in s for s in ends))
        self.assertTrue(any(stance.SECRET in s and "irabeth.committed" in s for s in ends))
        exclusive = [s for s in ends if stance.EXCLUSIVE in s]
        self.assertTrue(exclusive)
        self.assertTrue(all("irabeth.closed" in s and "irabeth.committed" not in s for s in exclusive))
        for state in ends:
            self.assertLessEqual(len(set((stance.SHARE, stance.SECRET, stance.EXCLUSIVE)) & state), 1)
            self.assertFalse(any(s.startswith("anevia.") for s in state))

    def test_widow_does_not_invent_partner_permission(self):
        ends = walk(self.road, ("anevia_dead",), "lasting")
        self.assertTrue(any("irabeth.committed" in s for s in ends))
        self.assertTrue(all(not set((stance.SHARE, stance.SECRET, stance.EXCLUSIVE)) & s for s in ends))

    def test_secret_discovery_has_no_free_continuation(self):
        for native in ((), ("anevia_dead",), ("anevia_gone",), ("anevia_gone", stance.RETURNED)):
            ends = walk(self.battle, (stance.SECRET, "irabeth.committed", *native))
            self.assertTrue(ends)
            self.assertTrue(all("irabeth.closed" in s for s in ends))
            if "anevia_dead" not in native and ("anevia_gone" not in native or stance.RETURNED in native):
                self.assertTrue(all(stance.EXPOSED in s for s in ends))

    def test_current_wife_state_and_stance_are_read_by_endings(self):
        paragraphs = stance.ending_paragraphs()
        for state in (set(), {'anevia_gone'}, {'anevia_dead'}, {'anevia_gone', stance.RETURNED}, {'anevia_dead', 'anevia_gone'}, {'anevia_dead', 'anevia_gone', stance.RETURNED}, {'irabeth_dead'}, {'irabeth_dead', 'irabeth.trickster.returned'}, {'irabeth_gone'}):
            selected = [p for p in paragraphs if set(p['Requires']) <= state and (not set(p['Forbids']) & state)]
            unset = [p for p in selected if set((stance.SHARE, stance.EXCLUSIVE, stance.SECRET)) <= set(p['Forbids'])]
            unset_account, = unset
            self.assertTrue(set((stance.SHARE, stance.EXCLUSIVE, stance.SECRET)) <= set(unset_account['Forbids']))
            fate_account, = [p for p in selected if p is not unset_account]
            self.assertTrue(fate_account['Requires'] or fate_account['Forbids'])
        for flag in (stance.SHARE, stance.SECRET, stance.EXCLUSIVE, stance.EXPOSED):
            self.assertTrue(any((flag in p['Requires'] for p in paragraphs)))
if __name__ == '__main__':
    unittest.main()

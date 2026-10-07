"""Measurable W5 reconciliation; this oracle does not enable P3."""
import unittest
from math import dist

from tools.residence_contract import assign_seats, NATIVE_SPOTS, SEATS


class ResidenceContractTests(unittest.TestCase):
    def test_picker_order_and_index_ties(self):
        self.assertEqual(assign_seats(["seelah", "wenduag"]), {
            "seelah": SEATS[0][1], "wenduag": SEATS[1][1]})
        self.assertEqual(assign_seats(["wenduag", "seelah"]), {
            "wenduag": SEATS[0][1], "seelah": SEATS[1][1]})

    def test_enmity_maximizes_minimum_distance(self):
        selected = ["seelah", "wenduag", "camellia"]
        result = assign_seats(selected, [("seelah", "camellia"), ("wenduag", "camellia")])
        expected = max(range(2, len(SEATS)), key=lambda i: (
            min(dist(SEATS[i][1], result[w]) for w in selected[:2]), -i))
        self.assertEqual(result["camellia"], SEATS[expected][1])
        self.assertGreaterEqual(min(dist(result["camellia"], result[w]) for w in selected[:2]), 8)

    def test_pair_refused_without_eight_metre_separation(self):
        close = (("one", (0, 0, 0)), ("two", (7.99, 0, 0)))
        with self.assertRaisesRegex(ValueError, "eight"):
            assign_seats(["seelah", "wenduag"], [("wenduag", "seelah")], seats=close)
        exact = (("one", (0, 0, 0)), ("two", (8, 0, 0)))
        self.assertEqual(len(assign_seats(["seelah", "wenduag"],
                                         [("seelah", "wenduag")], seats=exact)), 2)

    def test_native_spots_and_no_duplicate_council_women(self):
        fixed = {w: NATIVE_SPOTS[w] for w in ("chadali", "eritrice")}
        result = assign_seats(["seelah", "chadali", "eritrice", "wenduag", "camellia", "aranka"],
                              native_positions=NATIVE_SPOTS.values(), fixed_positions=fixed)
        self.assertEqual({w: result[w] for w in fixed}, fixed)
        for woman, position in result.items():
            if woman not in fixed:
                self.assertTrue(all(dist(position, other) >= 1.5 for other in NATIVE_SPOTS.values()))
        self.assertEqual(len(set(result.values())), 6)
        self.assertEqual(len(result), 6)

    def test_fixed_native_enmity_checks_both_picker_orders(self):
        fixed = {"chadali": (0, 0, 0)}
        seats = (("near", (2, 0, 0)),)
        for order in (["chadali", "seelah"], ["seelah", "chadali"]):
            with self.assertRaisesRegex(ValueError, "eight"):
                assign_seats(order, [("seelah", "chadali")], seats=seats, fixed_positions=fixed)

    def test_limits_and_no_seat_reuse(self):
        for order, capacity in [(list("abcdefg"), 6), (list("abcde"), 4), (["a", "a"], 6)]:
            with self.assertRaises(ValueError):
                assign_seats(order, capacity=capacity)
        with self.assertRaisesRegex(ValueError, "unoccupied"):
            assign_seats(["a", "b"], seats=(("only", (0, 0, 0)),))
        self.assertEqual(assign_seats([]), {})
        self.assertEqual(len(assign_seats(list("abcd"), capacity=4)), 4)

    def test_native_clearance_and_overlapping_candidate_positions(self):
        seats = (("blocked", (1.49, 0, 0)), ("clear", (1.5, 0, 0)))
        self.assertEqual(assign_seats(["seelah"], seats=seats,
                                      native_positions=[(0, 0, 0)])["seelah"], (1.5, 0, 0))
        overlapping = (("one", (0, 0, 0)), ("two", (0.99, 0, 0)))
        with self.assertRaisesRegex(ValueError, "unoccupied"):
            assign_seats(["seelah", "wenduag"], seats=overlapping)
        shyka_seat = dict(SEATS)["ShykaLocPlayer"]
        self.assertLess(dist(shyka_seat, NATIVE_SPOTS["shyka"]), 1.5)
        result = assign_seats(list("abcdef"), native_positions=NATIVE_SPOTS.values())
        self.assertNotIn(shyka_seat, result.values())


if __name__ == "__main__":
    unittest.main()

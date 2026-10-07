"""Route-local residue: earned terms and the late con's unchanged price."""
import unittest

from storylines import herrax_house as house
from storylines import herrax_trickster as route


SCENES = {s["Id"]: s for s in [*route.SCENES, *house.SCENES]}


def available(scene, flags):
    return (set(scene["Requires"]) <= flags
            and not set(scene["Forbids"]) & flags)


class HerraxRound4Tests(unittest.TestCase):
    def test_labyrinth_and_morevet_death_do_not_earn_unpaid_terms(self):
        base = {"trickster.ever", route.MADAM, route.MET, house.LABYRINTH,
                "herrax.present_now"}
        living = SCENES[house.B + "honeyed_tongue"]
        absent = SCENES[house.B + "unpriced_guest"]
        for primed in (False, True):
            for committed in (False, True):
                for dead in (False, True):
                    flags = base | ({route.PRIMED} if primed else set())
                    flags |= {route.COMMITTED} if committed else set()
                    flags |= {route.MOREVET_DEAD} if dead else set()
                    self.assertEqual(committed and not dead, available(living, flags))
                    self.assertEqual(committed and dead, available(absent, flags))
                    self.assertFalse(available(living, flags | {route.CLOSED}))
                    self.assertFalse(available(absent, flags | {route.CLOSED}))

    def test_late_con_keeps_bluff_and_both_existing_prices(self):
        nodes = {n["Id"]: n for n in SCENES[route.H + "late.next_move"]["Nodes"]}
        check = nodes["earnest"]["Choices"][0]["Check"]
        self.assertEqual({"Skill": "CheckBluff", "DC": 22,
                          "Success": "earnest_taken", "Failure": "earnest_doubted"}, check)
        blood = nodes["earnest_taken"]["Choices"][0]
        gold = nodes["earnest_doubted"]["Choices"][0]
        for answer in (blood, gold):
            self.assertEqual("promised", answer["Next"])
            self.assertIn(route.COST_LATE, answer["Set"])
            self.assertIn(route.PRIMED, answer["Set"])
        self.assertIn(route.LATE_RING, blood["Set"])
        self.assertIn(route.LATE_PAID, gold["Set"])
        self.assertEqual(-500, gold["Crusade"]["Amount"])


if __name__ == "__main__":
    unittest.main()

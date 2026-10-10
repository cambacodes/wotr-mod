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
        check = select_answer(nodes["earnest"]["Choices"], ((None, False, 'earnest_taken', 'earnest_doubted', (), ()),), expected_position=0)["Check"]
        self.assertEqual({"Skill": "CheckBluff", "DC": 22,
                          "Success": "earnest_taken", "Failure": "earnest_doubted"}, check)
        blood = select_answer(nodes["earnest_taken"]["Choices"], (('promised', False, None, None, (), ()),), expected_position=0)
        gold = select_answer(nodes["earnest_doubted"]["Choices"], (('promised', False, None, None, (), ()),), expected_position=0)
        for answer in (blood, gold):
            self.assertEqual("promised", answer["Next"])
            self.assertIn(route.COST_LATE, answer["Set"])
            self.assertIn(route.PRIMED, answer["Set"])
        self.assertIn(route.LATE_RING, blood["Set"])
        self.assertIn(route.LATE_PAID, gold["Set"])
        self.assertEqual(-500, gold["Crusade"]["Amount"])




def answer_key(answer):
    """Identify an answer by its destination/check and gates, never localization."""
    check = answer.get('Check') or {}
    return (answer.get('Next'), answer.get('Abort', False),
            check.get('Success'), check.get('Failure'),
            tuple(answer.get('Requires', ())), tuple(answer.get('Forbids', ())))


def select_answer(answers, keys, expected_position=None):
    # A destination is independent of its availability gates. Gates disambiguate
    # parallel answers that intentionally share a destination.
    matching = [answer for answer in answers if answer_key(answer)[:4] in {key[:4] for key in keys}]
    try:
        answer, = matching
    except ValueError:
        matching = [answer for answer in answers if answer_key(answer) in keys]
        try:
            answer, = matching
        except ValueError as error:
            raise AssertionError(('missing or ambiguous answer', keys,
                                  tuple(answer_key(answer) for answer in answers))) from error
    if expected_position is not None:
        # Save addresses retain answer order even when prose or gates change.
        slot = expected_position if expected_position >= 0 else len(answers) + expected_position
        saved_answer = next(candidate for position, candidate in enumerate(answers) if position == slot)
        if saved_answer is not answer:
            raise AssertionError(('saved answer order changed', keys, expected_position))
    return answer

if __name__ == "__main__":
    unittest.main()

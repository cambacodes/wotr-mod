"""S30 attendance and terminal contracts, including later loss after return."""
import unittest

from tests.story_fixture import fresh_story
from storylines import household
from storylines.harem_rows import s30
from tools import rrt_verify as verify


class S30Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = verify.Model(cls.story)
        cls.scene = cls.model.by_id[s30.SCENE_ID]

    def state(self, extra=(), omit=(), chapter=5):
        state = verify.SimState(chapter, 1000)
        state.flags.update({"trickster", "trickster.foresight.accepted",
                            "trickster.foresight.cost.promise", household.KEPT,
                            "eliandra.committed", "targona.committed", "eliandra.met_ch5",
                            "eliandra.trickster.leave_granted", "targona.trickster.met",
                            "targona.trickster.after.ward"})
        state.flags.difference_update(omit)
        state.flags.update(extra)
        verify.sim_complete(self.model, state)
        return state

    def available(self, **kwargs):
        return verify.sim_available(self.model, self.scene, self.state(**kwargs))

    def test_earned_body_and_page_allow_one_ch5_alliance(self):
        self.assertTrue(self.available())
        self.assertEqual(self.scene["ParticipantWomen"], ["eliandra", "targona"])
        self.assertEqual(self.scene["RestAllowance"], "household.pair")
        self.assertEqual(self.scene["HouseholdCategory"], "dynamic")
        for chapter in (3, 4, 6):
            with self.subTest(chapter=chapter):
                self.assertFalse(self.available(chapter=chapter))

    def test_meeting_memory_and_barrier_contact_are_not_drezen_bodies(self):
        for history in ((), ("eliandra.met_ch3",), ("eliandra.trickster.lights_seen",)):
            with self.subTest(history=history):
                self.assertFalse(self.available(omit=("eliandra.met_ch5",), extra=history))
        self.assertFalse(self.available(omit=("targona.trickster.met",)))

    def test_page_and_current_path_guard_the_deed_that_earns_friendship(self):
        # J02 derives friendship from this row's actual answer and costs;
        # requiring that result on entry would make its producer unreachable.
        self.assertTrue(self.available())
        self.assertFalse(set(s30.FRIENDS) & set(self.scene["Requires"]))
        for key in ("trickster", "trickster.foresight.accepted"):
            with self.subTest(key=key):
                self.assertFalse(self.available(omit=(key,)))
        self.assertFalse(self.available(extra=("trickster.failed",)))
        self.assertFalse(self.available(extra=("fool_king.gone",)))

    def test_current_closure_departure_and_condemnation_block(self):
        for key in ("eliandra.closed", "eliandra.dead", "eliandra.attacked",
                    "eliandra.trickster.ch5.road_letter", "eliandra.returned_actor_lost",
                    "targona.closed", "targona.dead_lab", "targona.dead_lair",
                    "targona.condemned", "targona.returned_actor_lost"):
            with self.subTest(key=key):
                self.assertFalse(self.available(extra=(key,)))

    def test_lab_return_lifts_only_its_named_loss_and_never_a_later_epoch(self):
        returned = ("targona.dead_lab", "targona.trickster.returned")
        self.assertTrue(self.available(extra=returned))
        for loss in ("targona.dead_lair", "targona.condemned", "targona.closed",
                     "targona.returned_actor_lost", "targona.epoch_unavailable"):
            with self.subTest(loss=loss):
                self.assertFalse(self.available(extra=(*returned, loss)))

    def test_enmity_keeps_only_existing_directional_reconciliation(self):
        for a, b in (("eliandra", "targona"), ("targona", "eliandra")):
            enmity = a + ".harem.enmity." + b
            self.assertFalse(self.available(extra=(enmity,)))
            self.assertTrue(self.available(extra=(enmity, a + ".harem.reconciled." + b)))

    def test_terminal_history_and_rest_allowance_are_not_replayed(self):
        root, people, answered, declined = self.scene["Nodes"]
        self.assertEqual([n["Id"] for n in self.scene["Nodes"]],
                         ["start", "people", "answered", "declined"])
        self.assertEqual([c["Next"] for c in root["Choices"]], ["people", "declined", None])
        self.assertTrue(select_answer(root["Choices"], ((None, True, None, None, (), ()),), expected_position=2)["Abort"])
        self.assertEqual(select_answer(root["Choices"], ((None, True, None, None, (), ()),), expected_position=2)["Set"], [])
        self.assertEqual(select_answer(answered["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"], list(s30.ANSWERED))
        self.assertEqual(select_answer(declined["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"], list(s30.DECLINED))
        for terminal in (s30.ANSWERED, s30.DECLINED):
            self.assertFalse(self.available(extra=terminal))
        state = self.state()
        state.rest_spent["household.pair"] = 1
        self.assertFalse(verify.sim_available(self.model, self.scene, state))

    def test_no_affection_native_success_or_intimate_interval_is_produced(self):
        flags = {f for n in self.scene["Nodes"] for c in n["Choices"] for f in c["Set"]}
        self.assertEqual(flags, set(s30.ANSWERED) | set(s30.DECLINED))
        self.assertTrue(all(f.startswith(s30.PREFIX) for f in flags))
        self.assertTrue(all(not n["Paragraphs"] for n in self.scene["Nodes"]))
        self.assertFalse(any("explicit" in n["Id"] for n in self.scene["Nodes"]))
        self.assertFalse(self.scene["AnswerLists"])
        entry = next(e for e in self.story["Books"]["trickster.ledger"]["Entries"]
                     if e["Id"] == s30.PREFIX + "seating")
        self.assertEqual(entry["Requires"], [s30.PREFIX + "charges.seen"])
        self.assertEqual(entry["Lines"][0]["Requires"], list(s30.ANSWERED))

    def test_repeated_registration_does_not_duplicate_own_or_shared_entries(self):
        import copy
        from storylines import lastcall_ledger
        from storylines.harem_rows import register_all
        from types import SimpleNamespace
        from unittest.mock import patch
        before = copy.deepcopy((household.ENTRIES, lastcall_ledger.EXTRA_ENTRIES))
        first, second = fresh_story(), fresh_story()
        for payload in (first, second):
            payload['Scenes'] = [s for s in payload['Scenes'] if s['Id'] != s30.SCENE_ID]
            ledger = payload['Books']['trickster.ledger']['Entries']
            ledger[:] = [e for e in ledger if e['Id'] != s30.PREFIX + 'seating']
            # Exercise the real discovery/drain boundary for this owned row;
            # unrelated registrars reject already-registered assembled scenes.
            with patch('storylines.harem_rows.pkgutil.iter_modules',
                       return_value=[SimpleNamespace(name='s30')]):
                register_all(payload, payload['Scenes'], payload['Etudes'])
                register_all(payload, payload['Scenes'], payload['Etudes'])
        self.assertTrue(first == second, "Repeated registration changed the generated story")
        self.assertEqual(before, (household.ENTRIES, lastcall_ledger.EXTRA_ENTRIES))
        self.assertIn(contract_identities([s for s in first['Scenes'] if s['Id'] == s30.SCENE_ID]), {1: (('household.pair.eliandra_targona.charges',),)}[1])
        self.assertIn(contract_identities([e for e in first['Books']['trickster.ledger']['Entries'] if e['Id'] == s30.PREFIX + 'seating']), {1: (('household.pair.eliandra_targona.seating',),)}[1])




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

def contract_identity(value):
    """Project saved identities and gates; paragraph wording is irrelevant."""
    if isinstance(value, dict):
        if 'Id' in value:
            return value['Id']
        check = value.get('Check') or {}
        return (value.get('Next'), check.get('Success'), check.get('Failure'),
                value.get('Abort', False), tuple(value.get('Requires', ())),
                tuple(value.get('Forbids', ())))
    if hasattr(value, 'flags'):
        return tuple(sorted(flag for flag in value.flags if flag.startswith('household.')))
    if isinstance(value, (tuple, list)):
        return tuple(contract_identity(item) for item in value)
    return value


def contract_identities(values):
    return tuple(contract_identity(value) for value in values)


if __name__ == "__main__":
    unittest.main()

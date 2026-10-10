"""S29's reviewed choice graph and loss/history guards, independent of discovery."""
import copy
import json
from pathlib import Path
import unittest
from tests.story_fixture import fresh_story

from storylines.harem_rows import s29
from tools import rrt_verify, savecompat


class S29Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Preserve the other rows required by final assembly and its delivery
        # contracts. Isolate only S29's registration surface for these tests.
        cls.base = fresh_story()
        cls.base["Scenes"] = [s for s in cls.base["Scenes"] if s["Id"] != s29.P("ward")]
        for woman in s29.PAIR:
            cls.base.get("SeatWomen", {}).pop(woman, None)
        # register_all likewise clears stale cap snapshots before each row.
        cls.base["Counts"] = {key: value for key, value in cls.base.get("Counts", {}).items()
                              if not key.startswith("household.cap.")}

    def setUp(self):
        self.payload = copy.deepcopy(self.base)
        s29.register(self.payload, self.payload["Scenes"], self.payload["Etudes"])
        self.scene = next(s for s in self.payload["Scenes"] if s["Id"] == s29.P("ward"))
        self.nodes = {n["Id"]: n for n in self.scene["Nodes"]}

    def choices(self, node, flags):
        return [c for c in self.nodes[node]["Choices"]
                if set(c["Requires"]) <= flags and not set(c["Forbids"]) & flags]

    def test_history_and_partner_wrappers_have_exactly_one_answer(self):
        # Include contradictory old history: current state wins without writes.
        history = ("kiana.wedding_seen", "kiana.history_betrothed")
        partner = [flag for _, flag, _ in s29.ACCOUNTS]
        for mask in range(1 << len(history)):
            flags = {f for i, f in enumerate(history) if mask & (1 << i)}
            _single_result, = self.choices('patient', flags)
        for mask in range(1 << len(partner)):
            flags = {f for i, f in enumerate(partner) if mask & (1 << i)}
            _single_result, = self.choices('account', flags)
        self.assertEqual(select_answer(self.choices("patient", set(history)), (('wedding', False, None, None, ('kiana.wedding_seen',), ()),), expected_position=0)["Next"], "wedding")
        self.assertEqual(select_answer(self.choices("patient", {history[1]}), (('postponed', False, None, None, ('kiana.history_betrothed',), ('kiana.wedding_seen',)),), expected_position=0)["Next"], "postponed")

    def test_root_indices_terminal_witnesses_and_no_new_mechanics(self):
        root = self.nodes["start"]["Choices"]
        self.assertEqual([c["Next"] for c in root], ["patient", "declined", None])
        self.assertTrue(select_answer(root, ((None, True, None, None, (), ()),), expected_position=2)["Abort"])
        self.assertEqual(select_answer(root, ((None, True, None, None, (), ()),), expected_position=2)["Set"], [])
        self.assertEqual(select_answer(self.nodes["private"]["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"], list(s29.HELPED))
        for node in self.nodes.values():
            self.assertNotIn("Paragraphs", node)
            for choice in node["Choices"]:
                self.assertTrue(all(f.startswith(s29.PREFIX) for f in choice["Set"]))
                self.assertFalse(set(choice) & {"Check", "Crusade", "StartEtude", "Revive"})
                if choice["Next"]:
                    self.assertIn(choice["Next"], self.nodes)
                    self.assertFalse(choice["Set"])
                elif not choice["Abort"]:
                    self.assertIn(s29.P("ward.seen"), choice["Set"])

    def test_registration_is_additive_and_save_safe(self):
        s29.register(self.payload, self.payload["Scenes"], self.payload["Etudes"])
        self.assertIn(contract_identities([s for s in self.payload['Scenes'] if s['Id'] == s29.P('ward')]), {1: (('household.pair.seelah_kiana.ward',),)}[1])
        self.assertEqual(savecompat.check(self.payload, savecompat.inventory(self.base)), [])
        self.assertEqual(self.payload["Relationships"], self.base["Relationships"])
        self.assertEqual(self.scene["RestAllowance"], "household.pair")
        self.assertEqual(self.scene["HouseholdCategory"], "dynamic")
        self.assertEqual(self.scene["Chapters"], [5])
        self.assertFalse(self.scene.get("HouseholdArcStart"))

    def test_current_loss_page_and_meeting_block_entry(self):
        model = rrt_verify.Model(self.payload)
        scene = model.by_id[s29.P("ward")]
        def state(extra=()):
            st = rrt_verify.SimState(5, 1000)
            st.flags.update(self.scene["Requires"])
            st.flags.update(("seelah.payoff.ordinary", "kiana.payoff.ordinary"))
            st.flags.update(extra)
            return st
        self.assertTrue(rrt_verify.sim_available(model, scene, state()))
        for missing in ("trickster", "foresight.page_taken", "seelah.present_now", "kiana.present_now", s29.P("met"), s29.P("conscious")):
            st = state()
            st.flags.remove(missing)
            self.assertFalse(rrt_verify.sim_available(model, scene, st), missing)
        for loss in ("kiana.closed", "seelah.closed", "seelah.plot_departed", "kiana.presence.failed", "kiana.epoch_unavailable", "seelah.epoch_unavailable"):
            st = state((loss, "seelah.trickster.returned", "kiana.trickster.returned"))
            self.assertFalse(rrt_verify.sim_available(model, scene, st), loss)
        st = state()
        st.rest_spent["household.pair"] = 1
        self.assertFalse(rrt_verify.sim_available(model, scene, st))

    def test_possession_and_meeting_are_separate_from_commitment(self):
        model = rrt_verify.Model(self.payload)
        st = rrt_verify.SimState(5, 1000)
        st.flags.update(("availability.observed", "kiana.committed", "kiana.possessed", "kiana.soul_lost"))
        rrt_verify.sim_complete(model, st)
        self.assertNotIn(s29.P("conscious"), st.flags)
        self.assertNotIn(s29.P("met"), st.flags)
        st.flags.add("kiana.trickster.returned")
        rrt_verify.sim_complete(model, st)
        self.assertIn(s29.P("conscious"), st.flags)
        self.assertIn(s29.P("met"), st.flags)

    def test_enmity_suppression_only_uses_existing_named_reconciliation(self):
        model = rrt_verify.Model(self.payload)
        scene = model.by_id[s29.P("ward")]
        for a, b in (s29.PAIR, s29.PAIR[::-1]):
            st = rrt_verify.SimState(5, 1000)
            st.flags.update(self.scene["Requires"])
            st.flags.update(("seelah.payoff.ordinary", "kiana.payoff.ordinary"))
            st.flags.add(a + ".harem.enmity." + b)
            self.assertFalse(rrt_verify.sim_available(model, scene, st))
            st.flags.add(a + ".harem.reconciled." + b)
            self.assertTrue(rrt_verify.sim_available(model, scene, st))




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

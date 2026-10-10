"""S24's indexed outcomes, current attendance and delayed retry contract."""
import copy
import json
from pathlib import Path
import unittest
from tests.structure import without_prose
from tests.story_fixture import fresh_story, row_registration_fixture

from storylines import household
from storylines.harem_rows import s24
from tools import rrt_verify, savecompat


class S24Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = row_registration_fixture(s24)
        s24.register(cls.payload, cls.payload["Scenes"], cls.payload["Etudes"])
        cls.model = rrt_verify.Model(cls.payload)
        cls.rows = {s["Id"]: s for s in cls.payload["Scenes"] if s["Id"].startswith(s24.PREFIX)}

    def state(self, branch="good"):
        state = rrt_verify.SimState(5, 1000)
        scene = self.rows[s24.P("settle." + branch)]
        state.flags.update(scene["Requires"])
        # These native/earned inputs justify rather than merely assert adapters.
        state.flags.update(["trickster", "trickster.foresight.accepted", "trickster.foresight.cost.promise",
                            "arueshalae.committed", "vellexia.committed", "vellexia.trickster.unmirrored"])
        state.flags.add("arueshalae.fallen" if branch == "fallen" else "arueshalae.changed")
        state.flags.update(["arueshalae.recruited_drezen"])
        return state

    def available(self, suffix, state):
        return rrt_verify.sim_available(self.model, self.model.by_id[s24.P(suffix)], state)

    def test_personality_precedence_unknown_and_present_path(self):
        state = self.state()
        self.assertTrue(self.available("settle.good", state))
        state.flags.add("arueshalae.corrupted")
        self.assertFalse(self.available("settle.good", state))
        self.assertTrue(self.available("settle.fallen", state))
        state.flags.difference_update(["arueshalae.redeemed", "arueshalae.corrupted"])
        self.assertFalse(self.available("settle.good", state))
        self.assertFalse(self.available("settle.fallen", state))
        for flag in ("trickster", household.PAGE_TAKEN, household.KEPT, household.STANCE_ELIGIBLE,
                     *s24.BODY_REQUIRES):
            state = self.state()
            state.flags.remove(flag)
            self.assertFalse(self.available("settle.good", state), flag)
        for chapter in (3, 4, 6):
            state = self.state()
            state.chapter = chapter
            self.assertFalse(self.available("settle.good", state))

    def test_current_losses_mirror_window_and_directional_enmity(self):
        for suffix in self.rows:
            scene = self.rows[suffix]
            for flag in s24.BODY_FORBIDS:
                self.assertIn(flag, scene["Forbids"])
            for woman in s24.PAIR:
                state = self.state()
                state.flags.add(self.payload["Relationships"][woman]["ClosedFlag"])
                self.assertFalse(self.available("settle.good", state))
            for flag in ("vellexia.trickster.kept_as_mirror",
                         "engine.l12.commander_unreturned", "trickster.failed"):
                state = self.state()
                state.flags.add(flag)
                self.assertFalse(self.available("settle.good", state))
        for a, b in (s24.PAIR, s24.PAIR[::-1]):
            state = self.state()
            state.flags.add(household.enmity(a, b))
            self.assertFalse(self.available("settle.good", state))
            state.flags.add(a + ".harem.reconciled." + b)
            self.assertTrue(self.available("settle.good", state))
        for woman in s24.PAIR:
            state = self.state()
            state.flags.add(woman + ".trickster.returned")
            state.flags.update(self.payload["Relationships"][woman].get("EpochUnavailableFlags", []))
            self.assertFalse(self.available("settle.good", state), woman)

    def test_fixed_indices_terminal_witnesses_and_no_extra_mechanics(self):
        for sid, scene in self.rows.items():
            step = "retry" if ".retry." in sid else "settle"
            fallen = sid.endswith("fallen")
            nodes = {n["Id"]: n for n in scene["Nodes"]}
            root = nodes["start"]["Choices"]
            self.assertIn(contract_identities(root),
                    {4: (((None, 'bounded', 'botched', False, (), ()),
                          ('refereed', None, None, False, (), ()),
                          ('declined', None, None, False, (), ()),
                          (None, None, None, True, (), ())),
                         (('refereed', None, None, False, (), ()),
                          ('failed', None, None, False, (), ()),
                          ('declined', None, None, False, (), ()),
                          (None, None, None, True, (), ())))}[4])
            self.assertTrue(select_answer(root, ((None, True, None, None, (), ()),), expected_position=3)["Abort"])
            self.assertFalse(select_answer(root, ((None, True, None, None, (), ()),), expected_position=3)["Set"])
            for choice in root:
                self.assertFalse(choice["Set"])
            if step == "settle":
                self.assertEqual(select_answer(root, ((None, False, 'bounded', 'botched', (), ()),), expected_position=0)["Check"], dict(Skill="SkillAthletics", DC=20,
                                                      Success="bounded", Failure="botched", CommanderOnly=True))
                self.assertEqual(select_answer(nodes["bounded"]["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"], list(s24._success(step, fallen)))
            self.assertEqual(select_answer(nodes["refereed"]["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"], list(s24._success(step, fallen)))
            failure = select_answer(nodes["failed" if step == "retry" else "botched"]["Choices"], ((None, False, None, None, (), ()),), expected_position=0)
            self.assertEqual(failure["Set"], [s24.P(step + ".seen"), s24.P(step + ".failed"), s24.P("bout.interrupted")])
            self.assertEqual(select_answer(nodes["declined"]["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"], [s24.P(step + ".seen"), s24.P(step + ".declined")])
            self.assertEqual(scene["RestAllowance"], "household.protected")
            self.assertNotIn("HouseholdArcStart", scene)
            self.assertNotIn("Remote", scene)
            for node in scene["Nodes"]:
                self.assertFalse(node.get("Paragraphs"))
                self.assertTrue(without_prose(node["Choices"]))
                for choice in without_prose(node["Choices"]):
                    for flag in choice["Set"]:
                        self.assertTrue(flag.startswith(s24.PREFIX))
                        self.assertNotIn(".harem.attitude.", flag)
                        self.assertNotIn(".enmity.", flag)
                        self.assertNotIn(".committed", flag)

    def test_retry_requires_timestamp_and_never_reopens_success_or_refusal(self):
        state = self.state()
        self.assertFalse(self.available("retry.good", state))
        state.flags.add(s24.P("settle.failed"))
        state.times[s24.P("settle.failed")] = state.hour
        self.assertFalse(self.available("retry.good", state))
        state.hour += 48
        self.assertTrue(self.available("retry.good", state))
        for suffix in ("settle.kept", "settle.declined", "retry.seen"):
            blocked = copy.deepcopy(state)
            blocked.flags.add(s24.P(suffix))
            self.assertFalse(self.available("retry.good", blocked))
        state.flags.remove("vellexia.present_now")
        self.assertFalse(self.available("retry.good", state))

    def test_registration_is_repeatable_save_safe_and_ledger_is_historical(self):
        before = copy.deepcopy(self.payload)
        entries = list(household.ENTRIES)
        consumers = dict(household.CONSUMERS)
        s24.register(self.payload, [], {})
        self.assertEqual(self.payload, before)
        self.assertEqual(household.ENTRIES, entries)
        self.assertEqual(household.CONSUMERS, consumers)
        self.assertEqual(savecompat.check(self.payload), [])
        ledger = next(e for e in self.payload["Books"]["trickster.ledger"]["Entries"]
                      if e["Id"] == "seating.arueshalae.vellexia")
        self.assertNotIn("vellexia.present_now", ledger["Requires"])
        pending = next(line for line in ledger["Lines"] if line.get("Forbids") == [s24.P("retry.seen")])
        self.assertEqual(pending["Forbids"], [s24.P("retry.seen")])

    def test_respect_requires_every_deed_and_has_no_higher_rung(self):
        for a, b in (s24.PAIR, s24.PAIR[::-1]):
            stage = a + ".harem.attitude." + b + "."
            self.assertEqual(self.payload["Derived"][stage + "respect"],
                             [[s24.P(w) for w in s24.RESPECT_WITNESSES]])
            self.assertEqual(self.payload["DerivedForbids"][stage + "rival"], [stage + "respect"])
            self.assertNotIn(stage + "friend", self.payload["Derived"])
            self.assertNotIn(stage + "lover", self.payload["Derived"])


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

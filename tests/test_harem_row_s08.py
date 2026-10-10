"""Row reservations stay stable; J03 explicitly activates only approved contracts."""
import copy
import unittest

from storylines.harem_rows import s08
from storylines import household
from tests.story_fixture import fresh_story


class HaremRowS08(unittest.TestCase):
    def test_unresolved_contract_is_inert_even_with_all_success_history(self):
        payload = {"Scenes": [], "Derived": {"existing": [["history"]]},
                   "Relationships": {"household": {"ClosedFlag": "household.closed"}}}
        before = copy.deepcopy(payload)
        s08.register(payload, payload["Scenes"], dict.fromkeys(s08.COMMON_REQUIRES, True))
        self.assertEqual(payload, before)
        self.assertEqual(len(s08.BLOCKERS), 4)

    def test_discovery_has_no_draft_side_effects(self):
        payload = fresh_story()
        draft_ids = {body["Id"] for body in s08.draft_scenes()}
        self.assertTrue(draft_ids <= {body["Id"] for body in payload["Scenes"]})

    def test_review_does_not_register_consumers_or_entries(self):
        consumers = dict(household.CONSUMERS)
        entries = copy.deepcopy(household.ENTRIES)
        s08.draft_scenes()
        self.assertEqual(household.CONSUMERS, consumers)
        self.assertEqual(household.ENTRIES, entries)

    def test_chapter_body_channel_and_later_loss_guards_on_every_wrapper(self):
        for scene in s08.draft_scenes():
            with self.subTest(scene=scene["Id"]):
                self.assertEqual(scene["Chapters"], [5])
                self.assertEqual(scene["Participants"], ["arueshalae"])
                self.assertEqual(scene["RestAllowance"], "household.protected")
                self.assertIn("arueshalae.present_now", scene["Requires"])
                self.assertIn("nocticula.reachable_by_letter", scene["Requires"])
                self.assertIn("noct.acq.seal_received", scene["Requires"])
                self.assertIn("noct.acq.renewed_agreement", scene["Requires"])
                for loss in ("noct.acq.council_fight", "noct.closed", "noct.acq.closed",
                             "arueshalae.closed", "arueshalae.epoch_unavailable",
                             "nocticula.epoch_unavailable"):
                    self.assertIn(loss, scene["Forbids"])
                    self.assertNotIn(loss, scene["ForbidOverrides"])
                for a, b in (("arueshalae", "nocticula"), ("nocticula", "arueshalae")):
                    self.assertEqual(scene["ForbidOverrides"][household.enmity(a, b)],
                                     a + ".harem.reconciled." + b)

    def test_unknown_personality_offers_neither_and_corruption_has_precedence(self):
        for scene in s08.draft_scenes():
            if scene["Id"].endswith("redeemed"):
                self.assertIn("arueshalae.redeemed", scene["Requires"])
                self.assertIn("arueshalae.corrupted", scene["Forbids"])
            else:
                self.assertIn("arueshalae.corrupted", scene["Requires"])

    def test_retry_uses_failure_clock_and_wrappers_share_exhaustion(self):
        for scene in s08.draft_scenes():
            retry = ".retry." in scene["Id"]
            step = "retry" if retry else "settle"
            self.assertEqual(scene["DelayHours"], 48 if retry else 0)
            self.assertEqual(scene["HouseholdWitness"], s08.P(step + ".seen"))
            self.assertIn(s08.P(step + ".seen"), scene["Forbids"])
            self.assertIn(s08.P("resolved"), scene["Forbids"])
            self.assertIn(s08.P("permanent_refusal"), scene["Forbids"])
            if retry:
                self.assertIn(s08.P("settle.failed"), scene["Requires"])

    def test_reserved_answers_abort_and_destination_safety(self):
        for scene in s08.draft_scenes():
            nodes = {node["Id"]: node for node in scene["Nodes"]}
            root = nodes["start"]["Choices"]
            self.assertIn(contract_identities(root),
                    {4: (((None, 'held', 'failed', False, (), ()),
                          ('held', None, None, False, (), ()),
                          ('refused', None, None, False, (), ()),
                          (None, None, None, True, (), ())),),
                     3: ((('held', None, None, False, (), ()),
                          ('refused', None, None, False, (), ()),
                          (None, None, None, True, (), ())),)}[3 if '.retry.' in scene['Id'] else 4])
            self.assertTrue(select_answer(root, ((None, True, None, None, (), ()),), expected_position=-1)["Abort"])
            self.assertFalse(select_answer(root, ((None, True, None, None, (), ()),), expected_position=-1)["Set"])
            self.assertIsNone(select_answer(root, ((None, True, None, None, (), ()),), expected_position=-1)["Next"])
            for node in nodes.values():
                for choice in node["Choices"]:
                    if choice["Next"]:
                        self.assertIn(choice["Next"], nodes)
                    if choice.get("Check"):
                        self.assertIsNone(choice["Check"]["DC"])
                        self.assertIn(choice["Check"]["Success"], nodes)
                        self.assertIn(choice["Check"]["Failure"], nodes)
                    for flag in choice["Set"]:
                        self.assertTrue(flag.startswith(s08.PREFIX), flag)
                        self.assertFalse(any(token in flag for token in
                                             (".harem.attitude.", ".enmity.", ".stance.",
                                              ".closed", ".committed", ".returned", ".changed")))
                    if node["Id"] != "start":
                        self.assertFalse(choice["Abort"])

    def test_scene_drafts_have_no_conditional_paragraphs_or_intimate_slots(self):
        for scene in s08.draft_scenes():
            for node in scene["Nodes"]:
                self.assertNotIn("Paragraphs", node)
                self.assertNotIn("explicit", node["Id"])




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

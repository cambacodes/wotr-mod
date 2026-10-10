"""Route-local regressions for paid returns, separate stances and closing history."""
import copy
import unittest

from tests.story_fixture import fresh_story


def visible(paragraph, flags):
    return (set(paragraph.get("Requires", ())) <= flags
            and not set(paragraph.get("Forbids", ())) & flags
            and all(set(group) & flags for group in paragraph.get("AnyGroups", ())))



def by_contract(items, contracts):
    """Find a structural outcome; gaps and overlaps violate the contract."""
    matches = [item for item in items
               if any(all(item.get(field) == value for field, value in contract.items())
                      for contract in contracts)]
    try:
        result, = matches
    except ValueError as error:
        raise AssertionError('Expected one matching structural outcome') from error
    return result

class VellexiaRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = fresh_story()
        cls.scenes = {s["Id"]: s for s in cls.payload["Scenes"] if s["Id"].startswith("vellexia.")}

    def private_callbacks(self, ending):
        page = next(n for n in self.scenes['vellexia.' + ending]['Nodes'] if n['Id'] == 'start')
        return [p for p in page.get('Paragraphs', ())
                if {'vellexia.farewell_lovers', 'vellexia.trickster.late_committed'}
                in [set(group) for group in p.get('AnyGroups', ())]]

    def test_opening_does_not_depend_on_jerribeth_availability(self):
        answer = by_contract(by_contract(self.scenes['vellexia.unfinished_likeness']['Nodes'], [{'Id': 'start'}])['Choices'], [{'Next': 'warning', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])
        self.assertEqual("warning", answer["Next"])
        self.assertFalse(any("jerribeth" in f for f in answer["Requires"] + answer["Forbids"]))

    def test_night_delay_starts_with_lovers_farewell(self):
        night = self.scenes["vellexia.trickster.after.night"]
        flags = {"trickster.ever", "vellexia.committed", "vellexia.invited"}
        self.assertFalse(set(night["Requires"]) <= flags)
        # Rules.Available anchors delays to the latest held requirement.
        flags.add("vellexia.farewell_lovers")
        times = {"vellexia.committed": 0, "vellexia.invited": 24, "vellexia.farewell_lovers": 72}
        anchor = max(times[f] for f in night["Requires"] if f in times)
        self.assertFalse(83 - anchor >= night["DelayHours"])
        self.assertTrue(84 - anchor >= night["DelayHours"])

    def test_both_physical_hosts_collect_cost_before_stance(self):
        for host in ('after.visit', 'after.visit_quarters'):
            nodes = {n['Id']: n for n in self.scenes['vellexia.trickster.' + host]['Nodes']}
            self.assertTrue({'unmirrored', 'diminished', 'want', 'collect'} <= nodes.keys())
            closing, = nodes['collect']['Choices']
            self.assertIn('vellexia.closed', closing['Set'])
            self.assertNotIn('vellexia.committed', closing['Set'])

    def test_rescue_only_endings_do_not_invent_a_shell_or_private_contact(self):
        flags = {'vellexia.prediction_known', 'vellexia.trickster.returned', 'vellexia.trickster.cost.diminished'}
        for ending in ('ending_interrupted', 'ending_ascent', 'ending_sacrifice'):
            callbacks = self.private_callbacks(ending)
            self.assertTrue(callbacks)
            self.assertFalse(any(visible(p, flags) for p in callbacks))
        mirror = self.scenes['vellexia.ending_mirror']
        self.assertIn('vellexia.mirrored', mirror['Requires'])
        self.assertFalse(self.private_callbacks('ending_mirror'))

    def test_closed_return_has_no_unplayed_play(self):
        page = next(n for n in self.scenes['vellexia.ending_closed']['Nodes'] if n['Id'] == 'start')
        memory, = (p for p in page['Paragraphs'] if p['Requires'] == ['vellexia.hour_kept'])
        flags = {'vellexia.closed', 'vellexia.trickster.returned', 'vellexia.trickster.visited'}
        self.assertFalse(visible(memory, flags))
        self.assertTrue(visible(memory, flags | {'vellexia.hour_kept'}))

    def test_returned_commander_keeps_exactly_one_earned_cost_copy(self):
        flags = {'vellexia.farewell_lovers', 'vellexia.trickster.cost.diminished',
                 'vellexia.trickster.cost.bored_once'}
        for ending in ('ending_lovers', 'trickster.epilogue.commit'):
            callbacks = self.private_callbacks(ending)
            for extra in (set(), {'sacrifice', 'trickster.commander_back'}):
                for cost in ('diminished', 'bored_once'):
                    selected, = (p for p in callbacks if 'vellexia.trickster.cost.' + cost in p['Requires']
                                 and visible(p, flags | extra))
                    self.assertIn('vellexia.trickster.cost.' + cost, selected['Requires'])
            self.assertFalse(any(visible(p, flags | {'sacrifice'}) for p in callbacks))

    def test_interrupted_contact_never_repeats_private_costs(self):
        flags = {'vellexia.prediction_known', 'vellexia.trickster.cost.diminished',
                 'vellexia.trickster.cost.bored_once', 'vellexia.trickster.late_committed'}
        callbacks = self.private_callbacks('ending_interrupted')
        self.assertTrue(callbacks)
        self.assertFalse(any(visible(p, flags) for p in callbacks))

    def test_final_company_and_delay_exclude_late_romance(self):
        forbidden = self.payload["DerivedForbids"]["vellexia.trickster.late_committed"]
        for stance in ("vellexia.farewell_friends", "vellexia.farewell_slow"):
            self.assertIn(stance, forbidden)
            self.assertIn(stance, self.scenes["vellexia.trickster.epilogue.commit"]["Forbids"])
        self.assertIn("vellexia.trickster.night_kept", self.scenes["vellexia.trickster.epilogue.commit"]["Forbids"])

    def test_daeran_cameo_requires_positive_presence(self):
        page = by_contract(self.scenes['vellexia.trickster.epilogue.commit']['Nodes'], [{'Id': 'start'}])
        cameo, = (p for p in page["Paragraphs"] if "daeran.in_party" in p["Requires"])
        self.assertFalse(visible(cameo, set()))
        self.assertTrue(visible(cameo, {"daeran.in_party"}))
        self.assertFalse(visible(cameo, {"daeran.in_party", "daeran.dead"}))

    def test_explicit_cut_is_on_night_path_without_new_effects(self):
        nodes = {n["Id"]: n for n in self.scenes["vellexia.trickster.after.night"]["Nodes"]}
        slot = "vellexia.trickster.after.night.explicit.1"
        self.assertEqual(slot, by_contract(nodes['threshold']['Choices'], [{'Next': 'vellexia.trickster.after.night.explicit.1', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Next"])
        self.assertEqual("morning", by_contract(nodes[slot]['Choices'], [{'Next': 'morning', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Next"])
        self.assertEqual([], by_contract(nodes[slot]['Choices'], [{'Next': 'morning', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Set"])
        self.assertEqual(slot, nodes[slot]["Id"])


if __name__ == "__main__":
    unittest.main()

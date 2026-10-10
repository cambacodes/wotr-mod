"""History-sensitive dialogue and voluntary payment at both recovery hosts."""
import unittest

from tests.story_fixture import fresh_story


def available(choice, flags):
    return (set(choice.get("Requires", ())) <= flags
            and not set(choice.get("Forbids", ())) & flags)



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


def only(items):
    """Require a single structural outcome, rejecting gaps and overlap."""
    try:
        outcome, = items
    except ValueError as error:
        raise AssertionError('Expected one structural outcome') from error
    return outcome

class VellexiaRound3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenes = {s["Id"]: s for s in fresh_story()["Scenes"]}

    def nodes(self, suffix):
        return {n["Id"]: n for n in self.scenes["vellexia." + suffix]["Nodes"]}

    def test_each_lesson_and_refusal_matches_acquisition_at_both_hosts(self):
        histories = (("unmirrored", "unmirrored", "footstool"),
                     ("diminished", "cost.diminished", "charm"),
                     ("entry", "entry", "Vask"),
                     ("provoked", "provoked", "Upper City"),
                     ("unpaid", "unpaid", "halfway"))
        for host in ("after.visit", "after.visit_quarters"):
            nodes = self.nodes("trickster." + host)
            for history, flag, anchor in histories:
                flags = {"vellexia.trickster." + flag}
                with self.subTest(host=host, history=history):
                    start = [c for c in nodes["start"]["Choices"] if available(c, flags)]
                    self.assertEqual([history], [c["Next"] for c in start])
                    lesson = nodes[by_contract(nodes[history]['Choices'], [{'Next': 'gave', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Next"]]
                    replies = [c for c in lesson["Choices"] if available(c, flags)]
                    self.assertIsNotNone(only(replies))
                    given = nodes[by_contract(replies, [{'Next': 'gave_end', 'Requires': ['vellexia.trickster.unmirrored'], 'Forbids': [], 'Set': [], 'Abort': False}, {'Next': 'gave_diminished', 'Requires': ['vellexia.trickster.cost.diminished'], 'Forbids': ['vellexia.trickster.unmirrored'], 'Set': [], 'Abort': False}, {'Next': 'gave_entry', 'Requires': ['vellexia.trickster.entry'], 'Forbids': ['vellexia.trickster.unmirrored', 'vellexia.trickster.cost.diminished'], 'Set': [], 'Abort': False}, {'Next': 'gave_provoked', 'Requires': ['vellexia.trickster.provoked'], 'Forbids': ['vellexia.trickster.unmirrored', 'vellexia.trickster.cost.diminished', 'vellexia.trickster.entry'], 'Set': [], 'Abort': False}, {'Next': 'gave_unpaid', 'Requires': ['vellexia.trickster.unpaid'], 'Forbids': ['vellexia.trickster.unmirrored', 'vellexia.trickster.cost.diminished', 'vellexia.trickster.entry', 'vellexia.trickster.provoked'], 'Set': [], 'Abort': False}])["Next"]]
                    kept = nodes[by_contract(nodes[history]['Choices'], [{'Next': 'kept', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}, {'Next': 'kept_diminished', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}, {'Next': 'kept_entry', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}, {'Next': 'kept_provoked', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}, {'Next': 'kept_unpaid', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Next"]]
                    self.assertNotEqual(given["Id"], kept["Id"])
                    # Both responses still pay their original lesson/secret latch
                    # at the shell, before the player chooses a relationship.
                    for response, latch in ((given, "lesson_given"), (kept, "cost.trick_kept")):
                        exits = [c for c in response["Choices"] if available(c, flags)]
                        self.assertTrue(exits)
                        for exit in exits:
                            shell = nodes[exit["Next"]]
                            self.assertIn("vellexia.trickster." + latch, by_contract(shell['Choices'], [{'Next': 'ask', 'Requires': [], 'Forbids': [], 'Set': ['vellexia.trickster.visited', 'vellexia.trickster.lesson_given'], 'Abort': False}, {'Next': 'ask', 'Requires': [], 'Forbids': [], 'Set': ['vellexia.trickster.visited', 'vellexia.trickster.cost.trick_kept'], 'Abort': False}])["Set"])

    def test_later_shell_does_not_turn_social_lessons_into_magic(self):
        nodes = self.nodes('trickster.after.voice')
        for flag in ('cost.diminished', 'entry', 'provoked', 'unpaid'):
            for latch in ('lesson_given', 'cost.trick_kept'):
                flags = {'vellexia.trickster.' + flag, 'vellexia.trickster.' + latch}
                answer, = (c for c in nodes['trick']['Choices'] if available(c, flags))
                self.assertIn(answer['Next'], nodes)
                self.assertNotIn('vellexia.trickster.unmirrored', answer['Requires'])
                expected = 'trick_' + ('given_' if latch == 'lesson_given' else 'kept_') + flag.removeprefix('cost.')
            self.assertEqual(expected, answer['Next'])

    def test_painter_disclosure_has_a_refusal_without_return(self):
        for host in ("sword.likeness", "sword.likeness_stores"):
            nodes = self.nodes("trickster." + host)
            disclosure = nodes["spell"]
            accept, decline = disclosure["Choices"]
            self.assertEqual("sitting", accept["Next"])
            self.assertTrue(decline["Abort"])
            self.assertFalse(decline["Set"])
            self.assertFalse(accept["Set"])
            self.assertIn("vellexia.trickster.cost.sat_for_painter", by_contract(nodes['sitting']['Choices'], [{'Next': 'wake', 'Requires': [], 'Forbids': [], 'Set': ['vellexia.trickster.cost.sat_for_painter'], 'Abort': False}])["Set"])
            self.assertIn("vellexia.trickster.returned", by_contract(nodes['wake']['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': ['vellexia.trickster.returned', 'vellexia.trickster.cost.diminished', 'vellexia.trickster.presumed_dead', 'vellexia.prediction_known', 'vellexia.started'], 'Abort': False}])["Set"])

    def test_vellexia_owns_the_demonstration_and_unload_is_staged(self):
        for host in ("mirrored.unmirror", "mirrored.unmirror_stores"):
            nodes = self.nodes("trickster." + host)
            for node in ("reading", "undone"):
                self.assertEqual("Vellexia", nodes[node]["Speaker"])
                self.assertEqual("a32a07903e428d34cb0e98a804d40569", nodes[node]["SpeakerUnit"])
            self.assertTrue(nodes["start"]["Choices"])
        for host, node in (("mirrored.speaks", "crated"), ("mirrored.fetch", "paid")):
            self.assertTrue(self.nodes("trickster." + host)[node]["Choices"])

    def test_mirror_threat_is_an_earned_memory(self):
        page = self.nodes("ending_mirror")["start"]
        memory, = (p for p in page["Paragraphs"] if p["Requires"] == ["vellexia.trickster.cost.watched"])
        self.assertEqual([["vellexia.trickster.cost.watched", "vellexia.trickster.kept_as_mirror"]], memory["AnyGroups"])

    def test_merged_last_call_is_safe_for_the_kept_mirror(self):
        coda = self.scenes['vellexia.lastcall.page']
        self.assertIn('vellexia.trickster.kept_as_mirror', coda['Forbids'])
        call = self.scenes['vellexia.lastcall.call']
        self.assertIn('vellexia.mirrored', self.scenes['vellexia.ending_mirror']['Requires'])
        self.assertTrue(call['Nodes'])


if __name__ == "__main__":
    unittest.main()

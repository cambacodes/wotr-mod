"""Echo-origin histories and inherited text/identity compatibility, without exporting files."""
from tests.story_fixture import fresh_story
import json
from pathlib import Path
import subprocess
import unittest

from storylines import wenduag_echo as echo



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

class WenduagEchoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Engine round 3 requires the echo departure page during finalization.
        # Compare against the actual integration export instead of assembling an
        # impossible payload with its required integration disabled.
        cls.before = json.loads(subprocess.check_output(
            ["git", "show", "HEAD:development/Story.json"],
            cwd=Path(__file__).resolve().parents[1]))
        cls.story = fresh_story()
        cls.scenes = {scene["Id"]: scene for scene in cls.story["Scenes"]}

    def test_existing_scene_nodes_choices_keep_saved_identities(self):
        old_ids = [scene['Id'] for scene in self.before['Scenes']]
        self.assertEqual(old_ids, [scene['Id'] for scene in self.story['Scenes'] if scene['Id'] in old_ids])
        for original in self.before['Scenes']:
            if original.get('Relationship') != 'wenduag':
                continue
            current = self.scenes[original['Id']]
            old_node_ids = [node['Id'] for node in original['Nodes']]
            self.assertEqual(old_node_ids, [node['Id'] for node in current['Nodes'] if node['Id'] in old_node_ids])
            for old_node in original['Nodes']:
                new_node = next(node for node in current['Nodes'] if node['Id'] == old_node['Id'])
                fields = ('Set', 'Abort', 'Check', 'Crusade', 'Revive', 'NativeNext', 'StartEtude')
                if original['Owner'].endswith('Epilogue'):
                    fields += ('Next',)
                expected = [{k: a.get(k) for k in fields} for a in old_node['Choices']]
                actual = iter({k: a.get(k) for k in fields} for a in new_node['Choices'])
                self.assertEqual(expected, [next(actual, None) for _ in expected], (original['Id'], old_node['Id']))

    def test_preparation_payment_and_wrong_branch(self):
        scene = self.scenes[echo.E + "prepare"]
        paths = []

        def visit(node_id, flags, spent):
            node = next(node for node in scene["Nodes"] if node["Id"] == node_id)
            for choice in node["Choices"]:
                updated = flags | set(choice.get("Set", []))
                cost = spent - (choice.get("Crusade") or {}).get("Amount", 0)
                targets = ([choice["Check"]["Success"], choice["Check"]["Failure"]]
                           if choice.get("Check") else [choice["Next"]] if choice.get("Next") else [])
                if targets:
                    for target in targets:
                        visit(target, updated, cost)
                else:
                    paths.append((updated, cost))

        visit("start", set(), 0)
        ready = [(flags, cost) for flags, cost in paths if echo.E + "ready" in flags]
        self.assertEqual({150, 200}, {cost for flags, cost in ready})
        self.assertTrue(any(echo.E + "misread" in flags and cost == 200 for flags, cost in ready))
        self.assertTrue(any(echo.E + "abandoned" in flags and cost == 50 for flags, cost in paths))
        self.assertFalse(any(echo.E + "ready" in flags and echo.E + "abandoned" in flags for flags, cost in paths))
        self.assertEqual([["trickster.now", "trickster.foresight.accepted"]], self.story["Derived"][echo.PAGE])

    def test_pickup_is_down_until_terminal_transport_choice(self):
        pickup = self.scenes[echo.E + "pickup"]
        rescued = [(node, choice) for node in pickup["Nodes"] for choice in node["Choices"]
                   if echo.E + "rescued" in choice.get("Set", [])]
        transport_node, transport_answer = only(rescued)
        self.assertEqual("shelter", transport_node["Id"])
        self.assertEqual(-150, transport_answer["Crusade"]["Amount"])
        for node in pickup["Nodes"]:
            for choice in node["Choices"]:
                self.assertNotIn(echo.W + "returned", choice.get("Set", []))
                self.assertNotIn("wenduag.committed", choice.get("Set", []))
        for id in ("hidden", "open"):
            node = next(node for node in pickup["Nodes"] if node["Id"] == id)
            self.assertIn(echo.E + "cost.used_lann", by_contract(node['Choices'], [{'Next': 'shelter', 'Requires': [], 'Forbids': [], 'Set': ['wenduag.trickster.echo.abyss.cost.used_lann'], 'Abort': False}])["Set"])

    def test_every_inherited_burial_branch_has_exclusive_echo_variant(self):
        for suffix, old, new in (("court.trial", "which_back", "which_echo"),
                                 ("court.cairn", "own_built", "own_echo"),
                                 ("court.stinger", "plain", "plain_echo")):
            scene = self.scenes[echo.W + suffix]
            choices = [choice for node in scene["Nodes"] for choice in node["Choices"]]
            self.assertTrue(any(choice.get("Next") == old and echo.E + "returned" in choice["Forbids"] for choice in choices))
            self.assertTrue(any(choice.get("Next") == new and echo.E + "returned" in choice["Requires"] for choice in choices))
        self.assertIn(echo.E + "returned", self.scenes[echo.W + "react.regill_watch"]["Forbids"])
        coda = by_contract(self.scenes['wenduag.lastcall.page']['Nodes'], [{'Id': 'page'}])["Paragraphs"]
        self.assertIn(echo.E + "returned", by_contract(coda, [{'Requires': ['lastcall.dead_on_record', 'lann.in_party'], 'Forbids': ['wenduag.trickster.echo.abyss.returned', 'lann.dead', 'lann.kicked_out', 'lann.plot_absent'], 'AnyGroups': [['wenduag.trickster.cairn_built', 'wenduag.trickster.abyss_cairn', 'wenduag.trickster.street_cairn']]}])["Forbids"])
        self.assertTrue(any(echo.E + "returned" in paragraph["Requires"] for paragraph in coda))
        entry = next(entry for entry in self.story["Books"]["trickster.ledger"]["Entries"] if entry["Id"] == "owed.wenduag.echo")
        self.assertIn(echo.E + "unavailable", entry["Forbids"])


if __name__ == "__main__":
    unittest.main()

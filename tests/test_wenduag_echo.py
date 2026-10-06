"""Echo-origin histories and inherited text/identity compatibility, without exporting files."""
import unittest

import expansion
from storylines import wenduag_echo as echo


class WenduagEchoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        integrate = echo.integrate
        try:
            echo.integrate = lambda payload: None
            cls.before = expansion.make_expansion()
        finally:
            echo.integrate = integrate
        cls.story = expansion.make_expansion()
        cls.scenes = {scene["Id"]: scene for scene in cls.story["Scenes"]}

    def test_existing_scene_nodes_choices_keep_saved_identities(self):
        old_ids = [scene["Id"] for scene in self.before["Scenes"]]
        self.assertEqual(old_ids, [scene["Id"] for scene in self.story["Scenes"] if scene["Id"] in old_ids])
        for original in self.before["Scenes"]:
            if original.get("Relationship") != "wenduag":
                continue
            current = self.scenes[original["Id"]]
            old_node_ids = [node["Id"] for node in original["Nodes"]]
            self.assertEqual(old_node_ids,
                             [node["Id"] for node in current["Nodes"] if node["Id"] in old_node_ids])
            for old_node in original["Nodes"]:
                new_node = next(node for node in current["Nodes"] if node["Id"] == old_node["Id"])
                for index, old_choice in enumerate(old_node["Choices"]):
                    # Primary origin selectors reserve their already-serialized echo index;
                    # the new orchard answer follows it. Native twins append their echo.
                    if (not original["Id"].endswith(".native_visit")
                            and old_choice.get("Next") in ("which_orchard", "own_orchard", "plain_orchard")):
                        index += 1
                    new_choice = new_node["Choices"][index]
                    for field in ("Text", "Next", "Set", "Abort", "Check"):
                        self.assertEqual(old_choice.get(field), new_choice.get(field),
                                         f"{original['Id']}/{old_node['Id']}[{index}]/{field}")

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
        self.assertEqual(1, len(rescued))
        self.assertEqual("shelter", rescued[0][0]["Id"])
        self.assertEqual(-150, rescued[0][1]["Crusade"]["Amount"])
        for node in pickup["Nodes"]:
            for choice in node["Choices"]:
                self.assertNotIn(echo.W + "returned", choice.get("Set", []))
                self.assertNotIn("wenduag.committed", choice.get("Set", []))
        for id in ("hidden", "open"):
            node = next(node for node in pickup["Nodes"] if node["Id"] == id)
            self.assertIn(echo.E + "cost.used_lann", node["Choices"][0]["Set"])

    def test_every_inherited_burial_branch_has_exclusive_echo_variant(self):
        for suffix, old, new in (("court.trial", "which_back", "which_echo"),
                                 ("court.cairn", "own_built", "own_echo"),
                                 ("court.stinger", "plain", "plain_echo")):
            scene = self.scenes[echo.W + suffix]
            choices = [choice for node in scene["Nodes"] for choice in node["Choices"]]
            self.assertTrue(any(choice.get("Next") == old and echo.E + "returned" in choice["Forbids"] for choice in choices))
            self.assertTrue(any(choice.get("Next") == new and echo.E + "returned" in choice["Requires"] for choice in choices))
        self.assertIn(echo.E + "returned", self.scenes[echo.W + "react.regill_watch"]["Forbids"])
        coda = self.scenes["wenduag.lastcall.page"]["Nodes"][0]["Paragraphs"]
        self.assertIn(echo.E + "returned", coda[1]["Forbids"])
        self.assertTrue(any(echo.E + "returned" in paragraph["Requires"] and "hooked shaft" in paragraph["Text"] for paragraph in coda))
        entry = next(entry for entry in self.story["Books"]["trickster.ledger"]["Entries"] if entry["Id"] == "owed.wenduag.echo")
        self.assertIn(echo.E + "unavailable", entry["Forbids"])


if __name__ == "__main__":
    unittest.main()

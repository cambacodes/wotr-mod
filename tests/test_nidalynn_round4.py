"""Local residue: actual native combat, retrieval costs, and later-loss reports."""
import itertools
import json
import unittest
import zipfile
from pathlib import Path

from storylines import nidalynn_trickster as route


def selectable(node, flags):
    return [choice for choice in node["Choices"]
            if set(choice["Requires"]) <= flags
            and not set(choice["Forbids"]) & flags]


def only(items):
    """A continuation is deterministic only when there is exactly one answer."""
    try:
        (item,) = items
    except ValueError as error:
        raise AssertionError("Expected one structural continuation") from error
    return item


class NidalynnRoundFourTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        story = json.loads(Path(__file__).resolve().parents[1].joinpath(
            "development/Story.json").read_text(encoding="utf-8"))
        cls.scenes = {scene["Id"]: scene for scene in story["Scenes"]}

    def nodes(self, suffix):
        return {node["Id"]: node for node in
                self.scenes[route.P + suffix]["Nodes"]}

    def test_both_failed_checks_reach_native_combat_for_both_egg_decisions(self):
        nodes = self.nodes("eggs.lamp_black")
        for check in nodes["look"]["Choices"][:2]:
            self.assertEqual(check["Check"]["Failure"], "fist")
            self.assertEqual(check["Check"]["Success"], "taken")
        for failed, destroy in itertools.product((False, True), repeat=2):
            with self.subTest(failed=failed, destroy=destroy):
                flags = set()
                node_id = "fist" if failed else "taken"
                while node_id != "held":
                    choice = only(selectable(nodes[node_id], flags))
                    flags.update(choice["Set"])
                    node_id = choice["Next"]
                choice = next(c for c in nodes[node_id]["Choices"]
                              if (route.CRUSHED in c["Set"]) == destroy)
                flags.update(choice["Set"])
                node_id = choice["Next"]
                while node_id:
                    choices = selectable(nodes[node_id], flags)
                    choice = (next(c for c in choices if "nidalynn.trickster.rock_joke" in c["Set"])
                              if node_id == "rock" else only(choices))
                    flags.update(choice["Set"])
                    node_id = choice["Next"]
                self.assertEqual(choice.get("NativeNext"),
                                 route.GOLEM_ALARM if failed else None)
                self.assertEqual(route.PRIMED in flags, not destroy)
                self.assertEqual(route.CRUSHED in flags, destroy)

    def test_native_alarm_chain_switches_the_whole_golem_group_hostile(self):
        game = Path("/wrath/blueprints.zip")
        if not game.exists():
            self.skipTest("native blueprints unavailable")
        prefix = "World/Dialogs/c3/IvorySanctum/Golems_DragonEggs/"
        with zipfile.ZipFile(game) as archive:
            alarm = json.loads(archive.read(prefix + "Cue_0034.jbp"))
            combat = json.loads(archive.read(prefix + "Cue_0032.jbp"))
        self.assertEqual(alarm["AssetId"], route.GOLEM_ALARM)
        self.assertEqual(alarm["Data"]["Continue"]["Cues"],
                         ["!bp_" + combat["AssetId"]])
        switch = next(action for action in combat["Data"]["OnStop"]["Actions"]
                      if action["$type"].rsplit(",", 1)[-1].strip() == "SwitchFaction")
        self.assertEqual(switch["Target"]["Spawner"]["EntityNameInEditor"], "Golem1")
        self.assertEqual(switch["m_Faction"], "!bp_0f539babafb47fe4586b719d02aff7c4")
        self.assertTrue(switch["IncludeGroup"])

    def test_clean_and_detected_vault_histories_keep_costs_through_both_deliveries(self):
        nodes = self.nodes("eggs.vault")
        palms_page = next(paragraph for paragraph in
                         self.nodes("epilogue.salt")["page"]["Paragraphs"]
                         if route.PALMS in paragraph.get("Requires", []))
        for detected, late in itertools.product((False, True), repeat=2):
            with self.subTest(detected=detected, late=late):
                flags = {route.CH5} if late else set()
                node_id = "clerk" if detected else "coal"
                while node_id:
                    choices = selectable(nodes[node_id], flags)
                    choice = only(choices)
                    flags.update(choice["Set"])
                    node_id = choice["Next"]
                self.assertTrue({route.PRIMED, route.VAULT, route.EGG_OWED} <= flags)
                self.assertEqual(route.CLERK in flags, detected)
                self.assertEqual(route.PALMS in flags, detected)
                self.assertEqual(route.HEARTH in flags, late)
                self.assertEqual(set(palms_page["Requires"]) <= flags, detected)
                treatment = selectable(self.nodes("hearth.listening")["hand_check"], flags)
                self.assertEqual(only(treatment)["Next"], "palms" if detected else "kiln")

    def test_both_druid_hosts_remember_hunt_without_reviving_lost_mother(self):
        for suffix in ("kiln.the_druids", "kiln.the_druids.chosen"):
            nodes = self.nodes(suffix)
            for hunting, present in itertools.product((False, True), repeat=2):
                flags = {flag for flag, held in
                         ((route.DV_HUNTING, hunting), (route.DV_PRESENT, present)) if held}
                with self.subTest(host=suffix, hunting=hunting, present=present):
                    choices = selectable(nodes["tell"], flags)
                    self.assertEqual(only(choices)["Next"],
                                     "hunted" if hunting and present else
                                     "hunted_absent" if hunting else "end")
            self.assertEqual([(c["Next"], c["Set"]) for c in nodes["hunted_absent"]["Choices"]],
                             [(c["Next"], c["Set"]) for c in nodes["hunted"]["Choices"]])
            self.assertIn("hunted_absent", nodes)


if __name__ == "__main__":
    unittest.main()

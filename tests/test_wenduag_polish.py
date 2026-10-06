"""Reviewed Wenduag history routing and source/export twin contracts."""
import json
from pathlib import Path
import unittest

W = "wenduag.trickster."
E = W + "echo.abyss."


class WenduagPolishTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads(Path(__file__).resolve().parents[1].joinpath("development/Story.json").read_text(encoding="utf-8"))
        cls.scenes = {s["Id"]: s for s in cls.story["Scenes"]}

    def node(self, suffix, id):
        return next(n for n in self.scenes[W + suffix]["Nodes"] if n["Id"] == id)

    def enabled(self, node, flags):
        return [c for c in node["Choices"] if set(c.get("Requires", ())) <= flags
                and not set(c.get("Forbids", ())) & flags]

    def test_orchard_origin_is_produced_by_return_only(self):
        hunt = self.scenes[W + "exile.ch5_hunt"]
        producers = [(n["Id"], i) for n in hunt["Nodes"] for i, c in enumerate(n["Choices"])
                     if W + "orchard_return" in c.get("Set", ())]
        self.assertEqual([("back", 0)], producers)
        self.assertNotIn(W + "death_promised", self.node("exile.ch5_hunt", "sava")["Choices"][0]["Set"])
        orchard = set(self.node("exile.ch5_hunt", "back")["Choices"][0]["Set"])
        for twin in ("", ".native_visit"):
            for scene, node, target in (("court.trial", "her", "which_orchard"),
                                         ("court.cairn", "stones", "own_orchard"),
                                         ("court.stinger", "her", "plain_orchard")):
                with self.subTest(scene=scene, twin=twin):
                    self.assertEqual([target], [c["Next"] for c in self.enabled(self.node(scene + twin, node), orchard)])
                    self.assertNotIn(target, [c["Next"] for c in self.enabled(self.node(scene + twin, node), {W + "returned"})])
            promised = orchard | {W + "death_promised"}
            self.assertEqual(["promised"], [c["Next"] for c in self.enabled(self.node("court.stinger" + twin, "her"), promised)])

    def test_echo_and_orchard_selectors_are_exclusive(self):
        echo_return = set(self.node("echo.abyss.return", "stay")["Choices"][0]["Set"])
        for twin in ("", ".native_visit"):
            for suffix, node, target in (("trial", "her", "which_echo"),
                                         ("cairn", "stones", "own_echo"),
                                         ("stinger", "her", "plain_echo")):
                for flags in (echo_return, echo_return | {W + "orchard_return"}):
                    self.assertEqual([target], [c["Next"] for c in self.enabled(self.node("court." + suffix + twin, node), flags)])

    def test_betrayal_reckoning_has_an_exit_in_bought_and_unbought_histories(self):
        for twin in ("", ".native_visit"):
            start = self.node("court.trial" + twin, "start")
            for flags, target in ((set(), "her"), ({"wenduag.q3_betrayed_you"}, "her"),
                                  ({"wenduag.q3_betrayed_you", "wenduag.q3_spared"}, "reckoning_select")):
                self.assertEqual([target], [c["Next"] for c in self.enabled(start, flags)])
            select = self.node("court.trial" + twin, "reckoning_select")
            self.assertEqual(["reckoning"], [c["Next"] for c in self.enabled(select, set())])
            self.assertEqual(["reckoning_bought"], [c["Next"] for c in self.enabled(select, {W + "bought"})])

    def test_regill_legacy_location_and_echo_exit(self):
        self.assertFalse(self.scenes[W + "react.regill_watch"].get("Reaction", False))
        start = self.node("react.regill_watch", "start")
        for receipt, target in (("cairn_built", "neathholm"), ("abyss_cairn", "abyss"), ("street_cairn", "street")):
            self.assertEqual([target], [c["Next"] for c in self.enabled(start, {W + receipt})])
        self.assertEqual([], self.enabled(start, {W + "orchard_return"}))
        echo = self.scenes[W + "react.regill_echo"]
        self.assertTrue(echo["Reaction"])
        self.assertEqual(["start"], [n["Id"] for n in echo["Nodes"]])
        self.assertNotIn([W + "cairn_built", W + "abyss_cairn", W + "street_cairn"], echo.get("RequiresAnyGroups", []))
        self.assertEqual(1, len(self.enabled(echo["Nodes"][0], set())))
        self.assertFalse(echo["Nodes"][0]["Choices"][0].get("Next"))

    def test_all_intimacy_branches_reach_matching_cut_and_twin_completion(self):
        for twin in ("", ".native_visit"):
            for rescue in (set(), {E + "returned"}):
                scene = self.scenes[W + "court.cairn" + twin]
                for branch in ("decide", "knife", "roll"):
                    flags = set(rescue)
                    node = self.node("court.cairn" + twin, branch)
                    seen = set()
                    while True:
                        self.assertNotIn(node["Id"], seen)
                        seen.add(node["Id"])
                        enabled = self.enabled(node, flags)
                        self.assertEqual(1, len(enabled), (twin, rescue, branch, node["Id"]))
                        answer = enabled[0]
                        flags.update(answer.get("Set", ()))
                        if not answer.get("Next"):
                            self.assertEqual("cut_echo" if rescue else "cut", node["Id"])
                            self.assertIn(W + "court.cairn", flags)
                            break
                        node = next(n for n in scene["Nodes"] if n["Id"] == answer["Next"])
                    if branch == "knife":
                        self.assertIn("knife_down", seen)
                        self.assertIn(W + "cairn.knife_held", flags)

    def test_twin_structure_and_terminal_effects_match_templates(self):
        for suffix in ("trial", "gate", "stinger", "cairn", "morning", "vellexia", "yaniel", "neathers", "hunt", "gongs"):
            primary = self.scenes[W + "court." + suffix]
            twin = self.scenes[primary["Id"] + ".native_visit"]
            def topology(scene):
                def address(id):
                    return id.replace(".native_visit.explicit.", ".explicit.") if id else id
                return {address(n["Id"]): (n["Speaker"],
                    {(address(a.get("Next")), tuple(f for f in a.get("Set", ()) if f != primary["Id"]))
                     for a in n["Choices"] if a.get("Next") != "remembered"})
                    for n in scene["Nodes"] if n["Id"] != "remembered"}
            # The engine inventory adds a saved primary-only unavailable-participant
            # acknowledgment after cloning, splits some history selectors, and
            # appends the primary completion receipt on twin terminal answers.
            # The route nodes, destinations and route effects still agree.
            if suffix == "vellexia":
                self.assertIn("remembered", {n["Id"] for n in primary["Nodes"]})
            self.assertEqual(topology(primary), topology(twin))
            for node in twin["Nodes"]:
                for answer in node["Choices"]:
                    if not any(answer.get(k) for k in ("Next", "Check", "Abort")):
                        self.assertIn(primary["Id"], answer.get("Set", ()))

    def test_departure_accounts_and_immediate_orchard_arrival(self):
        hunt = self.scenes[W + "exile.ch5_hunt"]
        her = self.node("exile.ch5_hunt", "her")
        for flags, target in ((set(), "nobody"),
                              ({W + "orchard.escape_seen"}, "escape_account"),
                              ({W + "orchard.dyra_retreat_seen"}, "dyra_account"),
                              ({W + "orchard.escape_seen", W + "orchard.dyra_retreat_seen"}, "escape_account")):
            self.assertEqual([target], [a["Next"] for a in self.enabled(her, flags)])
        self.assertNotIn("Tomorrow", self.node("exile.ch5_hunt", "back")["Text"])
        self.assertIn("walks inside", self.node("exile.ch5_hunt", "back")["Text"])
        offers = self.enabled(self.node("exile.ch5_hunt", "offer"), {"savamelekh.dead"})
        self.assertFalse(any(a.get("Next") == "sava" for a in offers))
        self.assertTrue(any("Savamelekh is dead" in a["Text"] for a in offers))
        self.assertEqual("c04f08ae1806ab941864a97da25b90d3",
                         self.story["SeenCues"][W + "orchard.dyra_retreat_seen"][0])

    def test_slots_are_single_encounters_and_later_gong_return_needs_first_night(self):
        for twin in ("", ".native_visit"):
            suffix = "court.cairn" + twin
            slot = self.node(suffix, W + suffix + ".explicit.1")
            for flags, target in ((set(), "cut"), ({E + "returned"}, "cut_echo")):
                self.assertEqual([target], [a["Next"] for a in self.enabled(slot, flags)])
            for id in ("saw", "stronger"):
                node = self.node("court.gongs" + twin, id)
                before = self.enabled(node, set())
                after = self.enabled(node, {W + "court.cairn"})
                self.assertEqual(1, len(before))
                self.assertFalse(before[0].get("Next"))
                self.assertEqual([W + "court.gongs" + twin + ".explicit.1"], [a["Next"] for a in after])

    def test_restored_yaniel_wins_over_killed_and_freed_memories(self):
        for suffix in ("early.yaniel", "court.yaniel", "court.yaniel.native_visit"):
            flags = {"yaniel.trickster.returned", "yaniel.freed", "yaniel.killed"}
            self.assertEqual(["returned_yaniel"],
                             [a["Next"] for a in self.enabled(self.node(suffix, "start"), flags)])
            # Shared captor-presence guards remain a separately reported blocker.
            # The route can override its own early-discussion flag for changed news.
            if suffix != "early.yaniel":
                self.assertEqual("yaniel.trickster.returned",
                                 self.scenes[W + suffix]["ForbidOverrides"][W + "early.yaniel"])

    def test_echo_has_one_funeral_and_discovery_has_her_response(self):
        page = self.scenes["wenduag.lastcall.page"]["Nodes"][0]
        flags = {"lastcall.dead_on_record", E + "returned"}
        funerals = [p for p in page["Paragraphs"] if "lastcall.dead_on_record" in p.get("Requires", ())
                    and set(p.get("Requires", ())) <= flags and not set(p.get("Forbids", ())) & flags]
        self.assertEqual(1, len(funerals))
        for suffix in ("react.lann_secret", "react.lann_secret_quiet"):
            scene = self.scenes[W + suffix]
            self.assertFalse(scene.get("Reaction"))
            response = next(n for n in scene["Nodes"] if n["Id"] == "fallout")
            self.assertIn("No more knocking", response["Text"])
            self.assertIn("muster", response["Text"])
            self.assertEqual("Lann", response["Speaker"])
        quiet = self.node("react.lann_secret_quiet", "start")["Choices"]
        self.assertFalse(quiet[0].get("Next"))
        self.assertEqual([], quiet[0]["Set"])
        self.assertEqual("caught", quiet[1]["Next"])


if __name__ == "__main__":
    unittest.main()

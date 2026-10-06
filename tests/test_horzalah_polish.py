"""Reviewed Horzalah factual branches; no new courtship eligibility or costs."""
import copy
import itertools
import unittest

from storylines import horzalah_guild as guild, horzalah_trickster as route


def shown(block, flags):
    return set(block.get("Requires", ())) <= flags and not set(block.get("Forbids", ())) & flags


class HorzalahPolishTests(unittest.TestCase):
    def scene(self, suffix):
        return next(s for s in [*route.SCENES, *guild.SCENES] if s["Id"] == route.H + suffix)

    def node(self, suffix, node):
        return next(n for n in self.scene(suffix)["Nodes"] if n["Id"] == node)

    def test_native_yozz_receipts_and_death_precedence(self):
        self.assertEqual(route.SELECTED_ANSWERS[route.YOZZ_KILLED], "da63ff8f158beaf42825a5d821128a96")
        self.assertEqual(route.SEEN_CUES[route.YOZZ_CONFESSION], ["1a302027ad5c3e94ebbd2313cb3f1e6e"])
        for killed, spared in itertools.product((False, True), repeat=2):
            flags = {key for key, yes in ((route.YOZZ_KILLED, killed), (route.YOZZ_SPARED, spared)) if yes}
            expected = "leash_dead" if killed else "leash" if spared else "leash_unvisited"
            for source in ("start", "own"):
                choices = [c for c in self.node("beat.yozz", source)["Choices"]
                           if c.get("Next", "").startswith("leash") and shown(c, flags)]
                self.assertEqual([c["Next"] for c in choices], [expected])
                self.assertEqual([c["Next"] for c in self.node("beat.yozz", expected)["Choices"]], ["keep", "suits"])
        self.assertIn("corpse", self.node("beat.yozz", "leash_dead")["Text"])
        for target in ("leash", "leash_dead", "leash_unvisited"):
            self.assertIn("Before I brought you his dresser" if target != "leash_unvisited"
                          else "before I brought you his dresser", self.node("beat.yozz", target)["Text"])

    def test_confession_and_new_admission_share_one_optional_beat(self):
        for heard in (False, True):
            flags = {"trickster.ever", route.WANTS, guild.YOZZ}
            if heard:
                flags.add(route.YOZZ_CONFESSION)
            scenes = [self.scene(s) for s in ("beat.used", "beat.used_first")]
            self.assertEqual([s["Id"] for s in scenes if shown(s, flags)],
                             [route.H + ("beat.used" if heard else "beat.used_first")])
            flags.add(guild.USED)
            self.assertFalse(any(shown(s, flags) for s in scenes))
        for suffix in ("beat.used", "beat.used_first"):
            for terminal in ("nobody", "little"):
                self.assertIn(guild.USED, self.node(suffix, terminal)["Choices"][0]["Set"])
            self.assertTrue(self.scene(suffix)["Optional"])

    def test_canary_histories_are_exhaustive_and_disjoint(self):
        for delivered, given, visited in itertools.product((False, True), repeat=3):
            flags = {key for key, yes in ((route.CANARY, delivered), (route.GIFT_GIVEN, given),
                                          (route.GUILD_SEEN, visited)) if yes}
            expected = "canary" if delivered else "no_canary" if given else "no_box_visited" if visited else "no_box"
            for source in ("last", "out"):
                self.assertEqual([c["Next"] for c in self.node("beat.sister", source)["Choices"] if shown(c, flags)], [expected])

    def test_optional_memories_do_not_become_courtship_gates(self):
        self.assertEqual(self.scene("beat.hat")["Entry"], '"I bought a hat."')
        self.assertIn(route.GUILD_SEEN, self.node("beat.hunger", "start")["Choices"][0]["Requires"])
        bare = self.node("beat.bare", "start")["Choices"]
        self.assertEqual(bare[1]["Next"], "look")
        self.assertEqual(bare[2]["Next"], "look_first")
        self.assertIn(route.SCAR_NOTED, bare[1]["Requires"])
        self.assertIn(route.SCAR_NOTED, bare[2]["Forbids"])
        self.assertNotIn(route.SCAR_NOTED, self.scene("beat.bare")["Requires"])
        self.assertNotIn("sausage", self.node("beat.thousands", "end")["Text"])
        for suffix in ("commit.her_move", "commit.her_move_night"):
            self.assertNotIn("Nobody has ever", self.node(suffix, "go")["Text"])
            self.assertEqual(self.node(suffix, "go")["Choices"][0]["Set"], [route.LEFT_FREE])

    def test_room_copies_keep_the_gift_and_report_factual(self):
        self.assertIn("cobbles again", self.node("test.the_gift", "free")["Text"])
        for suffix, prefix in (("test.the_gift_night", ""), ("guild.kept", ""),
                               ("unmet.knife", "eng8.guild."), ("late.at_night", "eng8.guild.")):
            target = "free" if not prefix and suffix == "test.the_gift_night" else prefix + "free_6"
            text = self.node(suffix, target)["Text"]
            self.assertIn("your floor again", text)
            self.assertNotIn("Storyteller", text)
            if suffix != "test.the_gift_night":
                self.assertIn("headquarters in Father's realm", self.node(suffix, prefix + "looks")["Text"])
                self.assertIn("I brought the box back", self.node(suffix, prefix + "hall")["Text"])
                self.assertIn(route.RETURNED, self.node(suffix, prefix + "threat_end")["Choices"][0]["Set"])
                if prefix:
                    self.assertIn("ribboned box", self.node(suffix, "eng8.guild.arrival")["Text"])

    def test_reactions_use_the_paid_ear_and_correct_owner(self):
        witness = self.scene("react.greybor_witness")
        self.assertIn(route.LATE, witness["Forbids"])
        late = self.scene("react.greybor_ear_late")
        self.assertIn(route.LATE, late["Requires"])
        self.assertIn(route.H + "react.greybor_ear", late["Nodes"][0]["Choices"][0]["Set"])
        self.assertIn(route.EAR, self.scene("react.greybor_amateur")["Requires"])
        no_ear = self.scene("react.greybor_amateur_no_ear")
        self.assertIn(route.EAR, no_ear["Forbids"])
        self.assertIn(route.H + "react.greybor_amateur", no_ear["Nodes"][0]["Choices"][0]["Set"])
        self.assertEqual(self.scene("react.wenduag_cheek")["Relationship"], "wenduag")

    def test_death_wins_over_all_historic_romance_outcomes(self):
        pages = [s for s in route.SCENES if s["Owner"] == "HorzalahEpilogue"]
        self.assertEqual(len(pages), 9)
        self.assertTrue(all(route.DEAD in s["Forbids"] for s in pages))
        mourned = self.node("epilogue.mourned", "page")
        self.assertNotIn("box", mourned["Text"])
        self.assertEqual(mourned["Paragraphs"][-1]["Requires"], [route.EAR])
        self.assertIn("held no body", mourned["Paragraphs"][4]["Text"])
        self.assertNotIn("retied", mourned["Paragraphs"][1]["Text"])

    def test_knife_and_missed_chamber_endings_have_no_retroactive_receipts(self):
        paragraphs = self.node("epilogue.together", "page")["Paragraphs"]
        self.assertIn(route.P_KNIFE, paragraphs[11]["Forbids"])
        self.assertEqual(paragraphs[-2]["Requires"], [route.CAME, route.P_KNIFE])
        self.assertEqual(paragraphs[-1]["Forbids"], [route.CHAMBER])
        self.assertIn("bare skin", paragraphs[-1]["Text"])
        self.assertTrue(all(not c["Set"] for c in self.node("epilogue.together", "page")["Choices"]))
        self.assertIn("snuff the candle", self.node("epilogue.commit", "page")["Text"])
        self.assertNotIn("unbuckle her collar", self.node("epilogue.commit", "page")["Text"])
        self.assertEqual(self.node("beat.second_night", "cut")["Text"],
                         "{n}Her mouth closes on yours. She reaches toward the bedside candle, and the room goes dark.{/n}")

    def test_sister_hook_uses_current_presence_and_separates_actual_departure(self):
        payload = {"Scenes": copy.deepcopy([*route.SCENES, *guild.SCENES])}
        # The hook consumes the participant owner's generated current guards.
        # This test exercises the route-local result; its exporter hook is escalated.
        guild.polish_sister_consumers(payload)
        scenes = {s["Id"]: s for s in payload["Scenes"]}
        current = "participant.hepzamirah.available"
        for suffix, prefix in (("guild.kept", ""), ("unmet.knife", "eng8.guild."),
                               ("late.at_night", "eng8.guild."), ("beat.name", ""), ("beat.sister", "")):
            scene = scenes[route.H + suffix]
            target = prefix + "sister" if suffix in ("guild.kept", "unmet.knife", "late.at_night") else "sister_here" if suffix == "beat.name" else "back"
            for present, departed in itertools.product((False, True), repeat=2):
                flags = {route.HEPZ_BACK}
                if present:
                    flags.add(current)
                if departed:
                    flags.add(route.H + "sister_departed")
                start = next(n for n in scene["Nodes"] if any(c.get("Next") == target for c in n["Choices"]))
                relevant = [c for c in start["Choices"] if (c.get("Next") or "").startswith(target) and shown(c, flags)]
                expected = target if present else target + ("_departed" if departed else "_unavailable")
                self.assertEqual([c["Next"] for c in relevant], [expected], suffix)
                text = next(n["Text"] for n in scene["Nodes"] if n["Id"] == expected)
                if not present:
                    self.assertNotIn("eating onions", text)
                    self.assertNotIn("she is not dead", text)
                    if not departed:
                        self.assertNotIn("has left your city", text)


if __name__ == "__main__":
    unittest.main()
